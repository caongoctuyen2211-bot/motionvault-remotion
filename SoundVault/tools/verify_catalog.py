"""Verify SoundVault file integrity and decoding. Does not claim auditory review."""
from pathlib import Path
import argparse,json,hashlib,subprocess

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--ffmpeg',default=str(root.parents[1]/'tools/ffmpeg-static/package/ffmpeg.exe'));args=parser.parse_args()
c=json.loads((root/'catalog.json').read_text(encoding='utf-8'));seen=set();listed=set();failed=[]
for e in c['local_audio']:
    p=root/e['path'];listed.add(p.resolve())
    assert p.resolve().is_relative_to((root/'audio').resolve()),e['id']
    assert p.is_file(),e['path']
    h=hashlib.sha256(p.read_bytes()).hexdigest();assert h==e['sha256'],e['id'];assert h not in seen,e['id'];seen.add(h)
    for key in ['name','group','duration_seconds','format','author','source_url','license','review_status']:assert e.get(key),f'{e["id"]}: {key}'
    assert e['audition_status']=='not-listened';assert e['review_status']['aural']=='not-listened'
    assert e['redistribution_allowed'] is True
    assert e['license_files'] and all((root/f).is_file() for f in e['license_files'])
    result=subprocess.run([args.ffmpeg,'-v','error','-i',str(p),'-f','null','-'],capture_output=True)
    if result.returncode:failed.append({'id':e['id'],'error':result.stderr.decode(errors='replace')[-1000:]})
actual={p.resolve() for p in (root/'audio').rglob('*') if p.is_file()}
assert actual==listed,{'unlisted':[str(p) for p in actual-listed],'missing':[str(p) for p in listed-actual]}
assert len(listed)==c['summary']['unique_library_files']
assert not failed,failed
demo=root/'demo/hien-xa-sfx-DEMO-not-field-recording-30s.wav'
if demo.exists():
    result=subprocess.run([args.ffmpeg,'-v','error','-i',str(demo),'-f','null','-'],capture_output=True);assert result.returncode==0
print(f'PASS: {len(listed)} unique audio files, matching checksums, licenses present, decoding successful. Aural review: NOT performed.')
