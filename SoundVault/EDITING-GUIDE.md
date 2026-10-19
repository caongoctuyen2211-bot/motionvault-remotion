# Chọn và phối âm thanh

Giọng nói là lớp chính. Bắt đầu với hiệu ứng nhỏ hơn giọng, nghe lại trên loa điện thoại rồi điều chỉnh. Không có một mức dB phù hợp cho tất cả file.

- Đặt đầu tiếng click/impact đúng khung hình hành động; whoosh có thể bắt đầu trước chuyển cảnh một chút.
- Fade ngắn ở điểm cắt để giảm tiếng tách. Đừng kéo dài tiếng không cần thiết.
- Hạ nhạc ở đoạn cần nghe tiếng vật liệu thực tế.
- Chỉ chọn vài điểm nhấn; có khoảng yên giữa các hiệu ứng.
- Kiểm tra đồng hồ peak khi cộng nhiều lớp; hạ gain nếu bị clipping.
- Với tiếng máy móc, dùng bản thu phù hợp cảnh. Không dùng impact điện tử để giả định đó là tiếng gạch hoặc thép thật.

## Clip giao cát 30 giây
| Mốc | Hình | Âm thanh |
|---|---|---|
| 0–3s | Hook | impact-tight nhẹ |
| 3–8s | Xe tiến vào | Bản thu động cơ xe tải trong INDEX.csv — chưa nghe kiểm duyệt |
| 8–18s | Nâng ben, cát đổ | Cát đổ MP3 preview đã có; riêng thủy lực nâng ben chưa có |
| 18–25s | Kiểm tra cát | Âm tại hiện trường; click ở chú thích |
| 25–30s | Chốt | notification-ding một lần |

## Kiểm tra gạch
Hook: impact-tight. Hiện bước kiểm tra: ui-click. Cảnh gõ gạch: ưu tiên tiếng gõ thật; không phủ chime lên tiếng cần nghe. Kết quả: success-chime ngắn nếu phù hợp.

## Video báo giá
Hiện từng con số: digital-type hoặc ui-pop. Trước công bố: tension-riser nhỏ. Chốt giá: ding. Giá và điều kiện mua phải rõ; tiếng không che lời.

## Quy trình nhập thêm
Lưu URL gốc, tác giả, giấy phép, bằng chứng giấy phép, thời lượng, định dạng, checksum và quyền phân phối trước khi đưa file ngoài vào repo. Nghe kiểm tra tiếng rè, cắt cụt, giọng nói không mong muốn và độ phù hợp. Nguồn chưa rõ chỉ lưu link, không ghi là đã nhập.

## Kho mở rộng và demo 30 giây
Hiện có bản thu theo nguồn cho xe tải, phanh xe trộn, động cơ máy xúc, xe nâng dạng cần vươn, cát, gạch, thép và sỏi. Tra INDEX.csv/catalog.json để dùng đúng loại âm. Không dùng tiếng phanh Kia Carnival rồi mô tả đó là xe tải; không gọi tiếng động cơ máy xúc là cảnh xúc đất nếu chưa kiểm tra.
Nghe demo/hien-xa-sfx-DEMO-not-field-recording-30s.wav. Đây là montage minh họa dựng âm, không phải tiếng hiện trường liên tục. Đoạn 0–5 giây minh họa hook/chữ/giá, 5–23 giây lướt qua các bản thu máy/vật liệu, 23–30 giây dùng hài, riser và chime. Xem mix-recipe.json để biết từng điểm cắt.
Demo dài đúng 30 giây, WAV PCM16 stereo 48 kHz, peak đo được khoảng -10,1 dBFS, không thêm giọng đọc/nhạc. Không tự nâng toàn bộ demo lên 0 dB: cần chừa chỗ cho giọng nói. Chưa nghe kiểm duyệt.
44 tệp nguồn có float peak vượt full scale sau giải mã. Nên hạ gain khoảng 6 dB trước khi chuyển PCM16 và xem peak sau khi cộng lớp. Giữ một bản gốc, chỉ chỉnh trên bản sao; không ghi đè tệp thư viện.
Bản cát/gạch/phanh xe trộn hiện là MP3 preview HQ công khai. Chúng không tương đương bản gốc AIFF/WAV; nếu cần hậu kỳ mạnh hoặc chất lượng lưu trữ tối đa, lấy bản gốc khi đã đăng nhập Freesound. Không gửi mật khẩu/token vào chat.
