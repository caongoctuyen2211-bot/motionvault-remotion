# SoundVault — Kho hiệu ứng âm thanh cho TikTok Hiền Xa

**372 tệp âm thanh không trùng, tổng 42.260.775 byte (~42,26 MB), chưa gồm demo.** Giữ nguyên 16 WAV tổng hợp ban đầu; bổ sung **356 tệp mới**, 41.899.559 byte. Đã tải/giải nén 358 tệp âm thanh mới và không nhập 2 bản trùng SHA-256. Không cộng link ngoài vào số tệp.

## Dùng ngay
- Mở thư mục audio rồi chọn nhóm phù hợp. Các tệp mới được chia nhóm và nguồn; 16 WAV cũ giữ nguyên đường dẫn để không làm hỏng dự án đang dùng.
- Mở INDEX.csv để tìm theo nhóm/tên/tác giả. catalog.json là danh mục đầy đủ từng tệp, gồm thời lượng, định dạng, tác giả, URL, giấy phép, SHA-256 và trạng thái kiểm tra.
- Demo: [hien-xa-sfx-DEMO-not-field-recording-30s.wav](demo/hien-xa-sfx-DEMO-not-field-recording-30s.wav). Đây là bản phối minh họa 30 giây, **không phải bản thu hiện trường liên tục**.
- Kéo tệp vào phần mềm dựng có hỗ trợ WAV/OGG/MP3/FLAC. Giữ nguyên tệp gốc; chuyển đổi bản sao nếu phần mềm không nhận OGG/FLAC.

## Các nhóm
| Thư mục | Nội dung |
|---|---|
| audio/transitions | 13 swish/whoosh CC0 mới |
| audio/hook-impact | Va chạm/nhấn hook từ thư viện Kenney, không tự nhận là bản thu vật liệu thật |
| audio/text-price-ui | Click, ding, giao diện, nhấn hiện chữ/giá |
| audio/comedy | Scratch thư viện, scratch mô phỏng bằng giọng, boing MicroFreak |
| audio/curiosity | Tick/question từ thư viện |
| audio/construction | Động cơ xe tải, máy xúc, xe nâng dạng cần vươn và phanh; nguồn/loại xe ghi riêng |
| audio/materials | Cát đổ, gạch va, thép tấm rơi, bước chân trên sỏi |
| audio/foley | Bước chân và vật dụng từ thư viện Kenney, không giả định là hiện trường công trình |
| audio/pack-previews | Hai bản nghe thử tổng hợp được Kenney kèm trong gói |

Whoosh, impact, pop, ding, boing/slide, riser/tick tổng hợp của bộ gốc vẫn nằm ở audio/*.wav. Chúng là âm điện tử, không phải bản thu công trình.

## Nguồn mới thực sự có tệp
| Nguồn | Tệp không trùng nhập vào |
|---|---:|
| Kenney UI Audio / Interface Sounds / Impact Sounds / RPG Audio | 332 OGG (có 2 pack preview) |
| BigSoundBank, chọn từng bản thu | 6 WAV |
| Freesound, bản HQ preview công khai | 3 MP3 |
| OpenGameArt: scratch, Swishes, boing | 15 tệp |

4 ZIP Kenney có 334 tệp OGG thực tế, khác tổng 330 trong thông tin quảng bá. Hai tệp footstep_carpet trùng checksum được ghi alias trong catalog, không sao chép lần hai. Tệp AppleDouble ._*.wav trong ZIP Swishes chỉ là metadata macOS, không phải âm thanh, đã loại khỏi quy trình nhập.

## Kiểm tra và giấy phép
372/372 tệp giải mã thành công; checksum khớp, không có file audio ngoài catalog. 16 WAV cũ được đối chiếu và giữ nguyên từng byte. **Chưa nghe kiểm duyệt bằng tai**, chưa xác nhận độ hay, tạp âm, tiếng nói nền hay độ hợp cảnh. Trạng thái tất cả tệp là not-listened, không ghi đã nghe.
Giữ nguyên file License.txt trong từng gói Kenney tại licenses/kenney. CC0 và bằng chứng kiểm nguồn mới ở licenses/; PROVENANCE.md giải thích rõ từng loại nguồn. Giấy phép MIT của code Remotion không tự áp dụng cho audio.
44 tệp có peak vượt full-scale khi giải mã ra float; tệp gốc vẫn được giữ nguyên. Hạ gain khoảng 6 dB trước khi đổi sang PCM16/phối, rồi xem peak toàn bản phối. Đây là kiểm tra số liệu, không phải kết luận đã nghe thấy méo.

## Những gì còn thiếu
- Ba bản gốc Freesound cần đăng nhập: AIFF cát đổ, WAV gạch và WAV phanh xe trộn. Hiện có MP3 HQ preview công khai, không giả thành file gốc chất lượng cao.
- Chưa có bản thu riêng thủy lực nâng ben và nền công trình; tiếng máy xúc hiện là động cơ, chưa phải cảnh đào đất. Xem RECORDING-BACKLOG.csv.
- Pixabay và Mixkit chỉ lưu link/điều kiện trong catalog, không có tệp. Không tái phân phối raw audio có giới hạn giấy phép.
- Chưa có lượt nghe kiểm duyệt thẩm mỹ. Hãy nghe và cân âm với giọng nói thực tế trước khi xuất video.

Xem EDITING-GUIDE.md để phối, VALIDATION.json để xem kết quả kỹ thuật. tools/verify_catalog.py kiểm lại kho bằng FFmpeg; tools/build_demo.py tái tạo demo bằng Python + NumPy và FFmpeg có sẵn, không cần cài phần mềm hệ thống cho lần thực hiện này.
