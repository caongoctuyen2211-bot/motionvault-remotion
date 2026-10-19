# Nguồn gốc và quyền phân phối SoundVault
Ngày kiểm tra: 19/10/2026. Từng tệp có author, source_url, download_url, original_filename, license_files, checksum và review_status trong catalog.json.

## 16 WAV gốc
Tổng hợp bằng công thức/seed cho SoundVault, PCM16 mono 22050 Hz. Giữ nguyên từng byte và đường dẫn từ commit 9a806b7. Danh mục gốc không nêu cá nhân tạo âm, nên không tự gán tên tác giả cá nhân. Nguồn gốc này được ghi riêng với bản thu bên ngoài.
CC0 theo README/PROVENANCE của bản gốc. Không dùng các âm này để khẳng định đó là âm thanh hiện trường công trình.

## Kenney — 332 tệp OGG không trùng
Tác giả: Kenney Vleugels / Kenney.nl. Tải từ đúng link ZIP trên bốn trang chính thức:
- https://kenney.nl/assets/ui-audio
- https://kenney.nl/assets/interface-sounds
- https://kenney.nl/assets/impact-sounds
- https://kenney.nl/assets/rpg-audio
Mỗi gói thực tải có License.txt ghi Creative Commons Zero. Bản license nguyên gốc được giữ tại licenses/kenney/<pack>/License.txt; đường dẫn trong ZIP và SHA-256 ZIP được ghi trong catalog. Không tự suy ra mọi tệp Kenney là bản thu thực địa; ghi là thư viện SFX của nhà cung cấp.
334 tệp OGG gồm các tệp preview kèm gói; 2 duplicate đã được ghi trong duplicates_not_imported với canonical_path. Không sửa tên audio đã tải.

## BigSoundBank — 6 WAV
Trang giấy phép: https://bigsoundbank.com/licenses.html. Từng trang nhập đều ghi CC0/public-domain và cho phép chia sẻ, chuyển thể, phân phối cả thương mại. Tác giả trong mục Technical details: Joseph SARDIN. Giữ tên số nguyên gốc 1442.wav, 2147.wav, 0984.wav, 1776.wav, 0510.wav, 1490.wav; tiêu đề thật và mô tả được lưu trong catalog.
BWF/WAV lấy từ URL encoding do chính trang công bố. Đây là bản thu theo mô tả nhà cung cấp, chưa nghe xác nhận độc lập. Máy xúc là động cơ Volvo EC55B; xe nâng là Manitou telescopic handler. 1490.wav là nhả phanh xe Kia Carnival, không phải xe tải; bản phanh xe trộn bê tông ở Freesound được ghi riêng.
Nguồn không kèm file license tải riêng: licenses/bigsoundbank/SOURCE-LICENSE-NOTES.md là ghi chép kiểm tra, không giả làm tài liệu do nhà cung cấp phát hành. Full CC0 legal text ở licenses/CC0-1.0.txt.

## Freesound — 3 MP3 HQ preview, không phải bản gốc
- https://freesound.org/people/martinimeniscus/sounds/199332/ — martinimeniscus / Florentine Films SFX, sand pour on sand FF662.aif.
- https://freesound.org/people/cejordi84/sounds/232396/ — cejordi84, Bricks.wav, bản thu hai viên gạch được xử lý chồng lớp.
- https://freesound.org/people/buzkill/sounds/825460/ — buzkill / Ramble Recordings, phanh xe trộn bê tông.
Cả ba trang ghi CC0. Bản gốc yêu cầu đăng nhập; chỉ tải đúng HQ MP3 preview được liên kết công khai trên trang, không vượt xác thực. Giữ tên file CDN đã tải và tên gốc nguồn riêng trong catalog. Không đổi đuôi MP3 thành WAV để giả chất lượng gốc. Bằng chứng giấy phép trong licenses/freesound; bản gốc còn trong original_versions_not_downloaded.

## OpenGameArt — 15 tệp
- https://opengameart.org/content/scratch-vocal-sound — farfadet46, scroutch_0.ogg, mô phỏng scratch bằng giọng, không phải tiếng đĩa thật.
- https://opengameart.org/content/swishes-sound-pack — artisticdude, 13 WAV swish cho Summoning Wars.
- https://opengameart.org/content/boing — Aeva, boing.flac, tổng hợp bằng Arturia MicroFreak.
Trang nguồn ghi CC0; file giấy phép/readme trong gói được giữ nếu có. Notes trong licenses/opengameart là bằng chứng kiểm tra do SoundVault ghi, không giả là file license gốc do nguồn gửi.

## Nguồn chỉ lưu link
Pixabay: https://pixabay.com/service/license-summary/ — cấm phân phối nội dung độc lập; không đưa raw sound lên thư viện GitHub.
Mixkit: https://mixkit.co/license/#sfxFree — chưa xác minh đầy đủ quyền phân phối từng tệp, chỉ lưu link, không tải/đăng âm thanh.
Không coi “miễn phí dùng video” là “được phát hành lại thư viện âm thanh”. Không có audio từ hai nguồn này trong kho.

## Demo và kiểm duyệt
Demo 30 giây là bản phối có chủ ý từ nhiều hiệu ứng và đoạn bản thu, không phải một cảnh hiện trường liên tục. Công thức thời gian/gain/nguồn/giấy phép trong demo/mix-recipe.json. Chỉ dùng audio CC0 đang có trong catalog.
Mọi tệp và demo: not-listened. Đã kiểm byte/hash, giải mã, thời lượng, metadata và peak số học; chưa nghe để xác định độ phù hợp, tạp âm hoặc nội dung giọng nói nền. Không có dấu “đã nghe kiểm duyệt”.
