# Báo cáo SoundVault — 19/10/2026

Đường dẫn kho làm việc: C:\Users\ADMIN\Documents\Codex\MotionVault\soundvault-maintenance\SoundVault
Repo gốc: https://github.com/caongoctuyen2211-bot/motionvault-remotion
Đã dùng checkout riêng từ origin/main (9a806b7) để bảo toàn nhánh Remotion đang phát triển. Không sửa code Remotion. 16 WAV cũ đối chiếu SHA-256, giữ nguyên từng byte.

## Số lượng thật
- Đã tải/giải nén 358 tệp âm thanh mới: 41.912.271 byte (~41,91 MB dữ liệu âm thanh trước loại trùng, không phải tổng lưu lượng mạng ZIP).
- Không nhập 2 bản OGG trùng checksum; giữ 356 tệp mới: 41.899.559 byte.
- Tổng thư viện: 372 tệp không trùng, 42.260.775 byte (~42,26 MB), chưa tính demo.
- 332 tệp Kenney không trùng, 6 WAV BigSoundBank, 3 MP3 preview Freesound, 15 tệp OpenGameArt. Hai bản preview tổng hợp trong gói Kenney được đánh dấu riêng.
- Demo riêng: hien-xa-sfx-DEMO-not-field-recording-30s.wav, 30 giây, 5.760.044 byte.

## Kiểm tra
372 tệp có metadata, source URL, author, license và SHA-256; giải mã thành công, không có audio ngoài catalog và không có checksum lặp. Full CC0 và file License.txt nguyên gốc Kenney được giữ. Hai bản trùng được ghi canonical_path, không mất nguồn/tên alias. Metadata macOS trong ZIP không bị tính là WAV.
44 tệp nguồn có float peak overshoot; giữ nguyên raw file, ghi cảnh báo trong catalog và hướng dẫn hạ gain trước phối/đổi PCM16. Demo không clipping theo đo số học. Không nghe kiểm duyệt thẩm mỹ bất kỳ tệp nào; tất cả ghi not-listened.

## Phạm vi và nguồn còn thiếu
Cát/gạch/phanh xe trộn: đã có MP3 HQ preview chính thức, chưa có bản gốc AIFF/WAV yêu cầu đăng nhập Freesound. Không yêu cầu mật khẩu/token và không vượt xác thực. Phanh Kia Carnival tách riêng, không giả làm tiếng xe tải. Xe nâng là telescopic handler, máy xúc là tiếng động cơ.
Chưa có bản thu riêng thủy lực nâng ben, cảnh máy xúc đào đất, nền công trình; các mục này vẫn có trạng thái thiếu/partial trong RECORDING-BACKLOG.csv.
Pixabay và Mixkit chỉ lưu link, chưa có file. Pixabay cấm phân phối âm thanh độc lập; Mixkit chưa được duyệt đầy đủ quyền tái phân phối nên không nhập. Kho không chứa raw audio từ hai nguồn này.

## Demo
Demo là bản phối minh họa nhiều nguồn, không phải âm thanh hiện trường liên tục. Dùng 18 điểm âm trong 30 giây, có công thức tái tạo và bảng nguồn/gain. Chưa nghe kiểm duyệt.

## Sao lưu
ZIP nguồn được lưu riêng ở C:\Users\ADMIN\Documents\Codex\MotionVault\backups\SoundVault-sources-20261019. Lịch sử Git trước cập nhật có bundle trong thư mục backups của MotionVault. Không ghi đè checkout Remotion cũ.

## Đồng bộ GitHub
Chỉ SoundVault được đưa vào commit. Kết quả commit/push thực tế được ghi trong báo cáo giao cho người dùng và đối chiếu trên GitHub. Không force-push.
