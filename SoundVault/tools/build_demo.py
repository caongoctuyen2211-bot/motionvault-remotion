"""Build a 30-second demonstration montage, not a continuous field recording."""
from pathlib import Path
import argparse,json,subprocess,wave,math,hashlib
import numpy as np

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--ffmpeg',default=str(root.parents[1]/'tools/ffmpeg-static/package/ffmpeg.exe'))
args=parser.parse_args()
catalog=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
entries={e['id']:e for e in catalog['local_audio']}
def find(predicate):return next(e['id'] for e in entries.values() if predicate(e))
swish=find(lambda e:e['original_filename']=='swish-8.wav')
click=find(lambda e:e.get('source_pack_id')=='interface-sounds' and e['original_filename']=='click_001.ogg')
boing=find(lambda e:e['original_filename']=='boing.flac')
events=[
 (0.3,'impact-tight',0,.2,-12,'Nhấn hook bằng hiệu ứng tổng hợp'),
 (1.2,swish,0,.6,-10,'Chuyển cảnh swish'),
 (2.3,click,0,.2,-10,'Hiện chữ'),
 (3.2,'ui-pop',0,.15,-12,'Hiện giá mẫu'),
 (4.1,'notification-ding',0,.65,-14,'Chốt thông tin'),
 (5.1,'bsb-truck-engine',1,3,-18,'Minh họa động cơ xe tải'),
 (8.4,'freesound-truck-air-brake',1,1.3,-15,'Minh họa phanh xe trộn bê tông; MP3 preview'),
 (10,'bsb-excavator-engine',2,1.7,-20,'Minh họa máy xúc'),
 (12,'bsb-forklift',5,1.7,-20,'Minh họa xe nâng dạng cần vươn'),
 (14.2,'freesound-sand',3,2.3,-13,'Minh họa cát đổ; MP3 preview'),
 (17,'freesound-bricks',0,.638,-12,'Gạch va, bản thu được nguồn xử lý chồng lớp'),
 (18.3,'bsb-steel-bars',0,1.7,-17,'Thép tấm va'),
 (20.5,'bsb-gravel-footsteps',0,2.3,-14,'Bước chân trên sỏi'),
 (23.2,boing,0,.9,-14,'Boing tổng hợp bằng MicroFreak'),
 (24.5,'oga-scratch',0,.5,-14,'Scratch mô phỏng bằng giọng'),
 (25.4,'tension-riser',0,1.5,-14,'Tạo tò mò bằng riser tổng hợp'),
 (27.3,swish,0,.6,-10,'Chuyển cảnh cuối'),
 (28.6,'success-chime',0,.8,-14,'Chốt demo')]
rate=48000;mix=np.zeros((30*rate,2),dtype=np.float64);recipe=[]
for at,id,offset,length,gain,label in events:
    e=entries[id]
    result=subprocess.run([args.ffmpeg,'-v','error','-i',str(root/e['path']),'-ss',str(offset),'-t',str(length),'-f','f32le','-ar',str(rate),'-ac','2','pipe:1'],capture_output=True)
    if result.returncode:raise RuntimeError(result.stderr.decode(errors='replace'))
    pcm=np.frombuffer(result.stdout,dtype='<f4').reshape(-1,2).astype(np.float64)
    if not len(pcm):raise ValueError('No samples: '+id)
    fade=min(240,len(pcm)//4)
    if fade:pcm[:fade]*=np.linspace(0,1,fade)[:,None];pcm[-fade:]*=np.linspace(1,0,fade)[:,None]
    pcm*=10**(gain/20);start=round(at*rate);end=min(len(mix),start+len(pcm));mix[start:end]+=pcm[:end-start]
    recipe.append({'at_seconds':at,'sound_id':id,'source_path':e['path'],'source_offset_seconds':offset,'requested_duration_seconds':length,'actual_duration_seconds':len(pcm)/rate,'gain_db':gain,'purpose_vi':label,'source_url':e['source_url'],'license':e['license']})
peak=float(np.max(np.abs(mix)));target=10**(-3/20);attenuation=min(1,target/peak) if peak else 1
mix*=attenuation
pcm16=np.round(np.clip(mix,-1,1)*32767).astype('<i2')
dest=root/'demo';dest.mkdir(exist_ok=True);out=dest/'hien-xa-sfx-DEMO-not-field-recording-30s.wav'
with wave.open(str(out),'wb') as audio:audio.setnchannels(2);audio.setsampwidth(2);audio.setframerate(rate);audio.writeframes(pcm16.tobytes())
metadata={'type':'demonstration-montage-not-continuous-field-recording','duration_seconds':30,'sample_rate_hz':rate,'channels':2,'sample_format':'PCM16','peak_dbfs':20*math.log10(float(np.max(np.abs(pcm16)))/32768),'aural_review':'not-listened','license':'CC0-1.0','sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'file_size_bytes':out.stat().st_size,'events':recipe}
(dest/'mix-recipe.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in metadata.items() if k!='events'},indent=2))
