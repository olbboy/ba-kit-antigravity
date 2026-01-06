US1: Tính năng Quản lý user
SME.TRADE FINANCE
Exported on  06/11/2025


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
 –  2
Table of Contents
1 TÀI LIỆU ĐẶC TẢ PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG..........................................4
2 I. THÔNG TIN YÊU CẦU.............................................................................................5
3 II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG...............................................................6
3.1 2.1. Mục tiêu thực hiện (CARD) * ...................................................................................................6
4 IV. MÔ TẢ YÊU CẦU...................................................................................................7
4.1 4.1. Mô tả yêu cầu chi tiết (CONVERSATION)................................................................................7
4.2 4.1.1. Sơ đồ quy trình, thao tác xử lý nghiệp vụ..........................................................................7
5 V. NỘI DUNG KHÁC.................................................................................................13
5.1 5.1. Tài liệu bổ sung .....................................................................................................................13
6 VI. YÊU CẦU PHI CHỨC NĂNG ...............................................................................14
6.1 6.1. Yêu cầu về an ninh/bảo mật và phân quyền sử dụng *......................................................14
6.2 6.2. Yêu cầu về mã hóa dữ liệu *.................................................................................................14
6.3 6.3. Yêu cầu về quản lý vận hành và lưu vết (lưu logs) *...........................................................14
6.4 6.4. Yêu cầu về khả năng chịu tải của hệ thống * ......................................................................14
6.5 6.5. Yêu cầu về chính sách lưu trữ dữ liệu.................................................................................15
6.6 6.6. Yêu cầu khác..........................................................................................................................15


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
 –  3
•
•
•
•
Áp dụng từ 
09 Aug 2024  
Các mục có dấu * là bắt buộc
Trường hợp US thực hiện đo lường độc lập với Epic và các US khác (đã tích hợp các thông tin tiêu chí 
đo lường trong Phiếu Yêu Cầu vào biểu mẫu này) → điền đầy đủ thông tin tiêu chí đo lường 
Trường hợp US thừa kế tiêu chí đo lường và thực thi đo theo Epic → điền link confluence Epic và 
không cần điền tiêu chí đo lường nữa



SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
TÀI LIỆU ĐẶC TẢ PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG –  4
1 
TÀI LIỆU ĐẶC TẢ PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
1 mailto:dungnt.sgd@mbbank.com.vn
I. THÔNG TIN YÊU CẦU –  5
2 I. THÔNG TIN YÊU CẦU
Tên yêu 
cầu *
Tính năng đăng ký user
Loại yêu 
cầu *
Yêu cầu PHÁT TRIỂN MỚI tính 
năng/sản phẩm
Yêu cầu CẢI TIẾN tính năng/sản 
phẩm đang có
Đề xuất ngày 
hoàn thành *
Độ ưu tiên *
CAO
TRU
NG 
BÌNH
THẤP
Cán bộ soạn thảo - Phòng thuộc Đơn vị yêu cầu
Cán bộ soạn thảo - Phòng thuộc CNTT
Người yêu 
cầu *
Họ tên & 
Chức danh
Ngô Tiến Dũng
Business 
Analysis (BA) 
*
Nguyễn 
Hữu Hồng 
Sơn
Phòng BA TTTM&SQ
Email & 
Điện thoại
dungnt.sgd@mbbank.
com.vn1
SA/DEV Lead
Phòng/TT/
Khối *
<<Ghi tên đơn vị đưa ra yêu cầu phát 
triển/cải tiến>>
Designer
@ Tên nhân 
sự thiết kế
<<Ghi tên Phòng/TT/
Khối>>
Link tài liệu liên quan
Link Epic/
Phiếu YC
<<Link confluence mô tả yêu cầu nếu 
US thừa kế tiêu chí đo lường ở Epic đã 
khai báo>>
Jira Link
<<link Jira của US>>
Test 
Design
<<Link file Test Design đã thiết kế>>
Tài liệu TKCT
<<Link file Tài liệu thiết kế chi tiết>>
Ý kiến của 
TCKT
Không ý kiến
Cần nghiệm thu        <<Liên hệ PhuongNT7>>


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG –  6
•
•
•
•
•
•
•
•
3 II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG
3.1 2.1. Mục tiêu thực hiện (CARD) *
HIỆN TRẠNG
BẤT CẬP
GIẢI PHÁP ĐỀ
XUẤT
Tại các CN/PGD, việc quản lý/giám sát các 
thành viên ra vào kho tiền đang được thực 
hiện thủ công
Việc ủy quyền nhân sự vào kho đang được 
phê duyệt qua văn bản cứng
Các nhân sự ra vào kho đang được giám 
sát bằng con người
Việc quản lý thông tin các nhân sự ra vào 
kho của từng phiên đang được ghi chép/
theo dõi thông qua “Sổ theo dõi ra vào 
kho”
Gây khó khăn trong việc quản lý
việc tuân thủ của các CN/PGD theo 
quy định quản lý kho của NHNN và 
MB
Tiềm ẩn nhiều nguy cơ mất mát, 
rủi ro cho kho tiền
Triển khai hệ thống 
nhận diện giám sát 
tiền cảnh báo cho 
kho tiền của MB để
phục vụ nhu cầu 
kiểm tra, thống kê 
và theo dõi tập 
trung
Hệ thống gồm 3 
Module chính:
Module 1: Quản 
trị user
Module 2: Cảnh 
báo/giám sát
Module 3: Báo 
cáo thống kê 
2.2. Tiêu chí đo lường về hiệu quả kinh doanh/nghiệp vụ
2.3. Tiêu chí đo lường về mức độ sử dụng *
III. XÁC ĐỊNH VẤN ĐỀ


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
IV. MÔ TẢ YÊU CẦU –  7
4 IV. MÔ TẢ YÊU CẦU
4.1 4.1. Mô tả yêu cầu chi tiết (CONVERSATION) 
4.2 4.1.1. Sơ đồ quy trình, thao tác xử lý nghiệp vụ
4.2. Tham chiếu chi tiết *
4.3. Tác động của phát triển đến hệ thống
4.4. Tiêu chí nghiệm thu (Confirmation) *
S
T
T
Scenario
(kịch 
bản)
Given
(trạng 
thái)
When
(điều kiện)
Then
(kết quả
mong muốn)
Mockup
(thiết kế mô 
phỏng)
1
Inputter CN/
PGD Xem 
danh sách 
User của chi 
nhánh
Tôi là Inputter 
CN/PGD  và đã 
log in và hệ
thống
Tôi click vào “Quản lý 
User”
Tôi thấy "Màn hình 
Danh sách User của 
chi nhánh"
2
Inputter CN/
PGD Xem 
danh sách 
bản ghi đăng 
ký User
Tôi là Inputter 
CN/PGD  và đã 
log in và hệ
thống
Tôi click vào “Quản lý 
User”
Tôi thấy "Màn hình 
Danh sách bản ghi 
đăng ký User của 
chi nhánh"
3
Inputter CN/
PGD tìm 
kiếm các 
tiêu chí ở
danh sách 
User/danh 
sách bản ghi 
đăng ký User 
của chi 
nhánh
Tôi là Inputter 
CN/PGD và tôi 
ở "Màn hình 
Danh sách 
User/Danh 
sách bản ghi 
đăng ký User 
của chi 
nhánh"
Tôi tìm kiếm theo các 
điều kiện (Họ và tên/
Chức danh/Chi nhánh/
PGD...)
Hệ thống hiển thị
các bản ghi thỏa 
mãn điều kiện tìm 
kiếm


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
IV. MÔ TẢ YÊU CẦU –  8
S
T
T
Scenario
(kịch 
bản)
Given
(trạng 
thái)
When
(điều kiện)
Then
(kết quả
mong muốn)
Mockup
(thiết kế mô 
phỏng)
4
Inputter CN/
PGD đăng ký 
User
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình Danh 
sách User của 
chi nhánh"
Tôi click button "Thêm 
mới"
Tôi thấy "Màn hình 
Đăng ký User"


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
IV. MÔ TẢ YÊU CẦU –  9
•
S
T
T
Scenario
(kịch 
bản)
Given
(trạng 
thái)
When
(điều kiện)
Then
(kết quả
mong muốn)
Mockup
(thiết kế mô 
phỏng)
5
Inputter CN/
PGD tạo bản 
ghi  đăng ký 
User 
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình Đăng ký 
User" 
Nhân sự MB:
Bước 1: Click tab 
"Nhân sự MB"
Bước 2: Nhập CCCD 
(Hoặc có thể là mã 
nhân viên)
Hệ thống lấy 
thông tin user (Mã 
nhân viên/Họ và 
tên/Email/Chức 
danh/Đơn vị) từ
hệ thống nội bộ
MB (HCM) và Ảnh 
của user (Ảnh 
chân dung) từ hệ
thống nội bộ MB 
(ECM)
Hiển thị cảnh báo 
nếu không có 
thông tin từ 1 
trong 2 hệ thống 
(Cho phép chỉnh 
sửa)
Bước 3: Hệ thống 
verify chất lượng ảnh
Bước 4: Click button 
"Gửi duyệt"
Nhân sự ngoài:
Bước 1: Click tab 
"Khách"
Bước 2: Nhập CCCD 
(Hoặc có thể là mã 
nhân viên)
Hệ thống lấy 
thông tin user (Họ
và tên/CCCD/SĐT) 
và ảnh của user 
(Ảnh chân dung) 
từ hệ thống nội 
bộ MB (ECM)
Hệ thông đẩy bản 
ghi đăng ký User 
lên cấp Authoriser 
CN/PGD


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
IV. MÔ TẢ YÊU CẦU –  10
•
S
T
T
Scenario
(kịch 
bản)
Given
(trạng 
thái)
When
(điều kiện)
Then
(kết quả
mong muốn)
Mockup
(thiết kế mô 
phỏng)
Hiển thị cảnh báo 
nếu không có 
thông tin từ ECM 
(Cho phép chỉnh 
sửa)
Bước 3: Hệ thống 
verify chất lượng ảnh
Bước 4: Click button 
"Gửi duyệt"
6
Inputter CN/
PGD chỉnh 
sửa bản ghi 
đăng ký 
User 
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình Danh 
sách User của 
chi nhánh"
Tôi click icon "Chỉnh 
sửa"
Tôi thấy "Màn hình 
chỉnh sửa bản ghi 
Đăng ký User"
7
Inputter CN/
PGD chỉnh 
sửa bản ghi  
đăng ký 
User 
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình chỉnh sửa 
bản ghi Đăng 
ký User"
Bước 1: Chỉnh sửa 
thông tin bản ghi 
đăng ký User
Bước 2: Click button 
"Gửi duyệt"
Hệ thông đẩy bản 
ghi dăng ký User 
lên cấp Authoriser 
CN/PGD
8
Inputter CN/
PGD chỉnh 
sửa User 
(Nhân sự
MB)
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình Danh 
sách User của 
chi nhánh"
Tôi click 1 User Nhân 
sự MB
Tôi thấy "Màn hình 
chỉnh sửa User"


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
IV. MÔ TẢ YÊU CẦU –  11
S
T
T
Scenario
(kịch 
bản)
Given
(trạng 
thái)
When
(điều kiện)
Then
(kết quả
mong muốn)
Mockup
(thiết kế mô 
phỏng)
9
Inputter CN/
PGD chỉnh 
sửa User 
(Nhân sự
MB)
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình chỉnh sửa 
User"
Bước 1: Chỉnh sửa 
ảnh
Bước 2: Hệ thống 
verify chất lượng ảnh
Bước 3: Click button 
"Gửi duyệt"
Lưu ý: Đối với nhân 
sự MB, chỉ được chỉnh 
sửa ảnh 
Hệ thông đẩy bản 
ghi chỉnh sửa User 
lên cấp Authoriser 
CN/PGD
10
Inputter CN/
PGD chỉnh 
sửa User 
(Nhân sự
ngoài)
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình Danh 
sách User của 
chi nhánh"
Tôi click 1 User Nhân 
sự ngoài
Tôi thấy "Màn hình 
chỉnh sửa User"
11
Inputter CN/
PGD chỉnh 
sửa User 
(Nhân sự
ngoài)
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình chỉnh sửa 
User"
Bước 1: Chỉnh sửa 
thông tin user/ảnh
Bước 2: Hệ thống 
verify chất lượng ảnh
Bước 3: Click button 
"Gửi duyệt"
Hệ thông đẩy bản 
ghi chỉnh sửa User 
lên cấp Authoriser 
CN/PGD
12
Inputter CN/
PGD xóa lô 
User
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình Danh 
sách User của 
chi nhánh"
Bước 1: Chọn 
checkbox các User
Bước 2: Click button 
"Xóa"
Bước 3: Hệ thống 
hiển thị popup cảnh 
báo
Bước 4: Click button 
"Xác nhận"
Hệ thông đẩy bản 
ghi xóa User lên 
cấp Authoriser CN/
PGD


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
IV. MÔ TẢ YÊU CẦU –  12
•
•
S
T
T
Scenario
(kịch 
bản)
Given
(trạng 
thái)
When
(điều kiện)
Then
(kết quả
mong muốn)
Mockup
(thiết kế mô 
phỏng)
13
Inputter CN/
PGD đơn lô 
User
Tôi là Inputter 
CN/PGD  và 
đang ở "Màn 
hình Danh 
sách User của 
chi nhánh"
Bước 1: Click 
icon"Xóa"
Bước 2: Hệ thống 
hiển thị popup cảnh 
báo
Bước 3: Click button 
"Xác nhận"
Hệ thông đẩy bản 
ghi xóa User lên 
cấp Authoriser CN/
PGD
14
Authoriser 
CN/PGD Xem 
danh sách 
bản ghi đăng 
ký User/User 
Tôi là 
Authoriser CN/
PGD  và đã log 
in và hệ thống
Tôi click vào “Quản lý 
User”
Tôi thấy "Màn hình 
Danh sách bản ghi 
đăng ký User/User 
của chi nhánh"
15
Authoriser 
CN/PGD phê 
duyệt/từ
chối bản ghi 
đăng ký User 
theo lô
Tôi là 
Authoriser CN/
PGD và đang ở
"Màn hình 
Danh sách các 
bản ghi đăng 
ký User/User"
Bước 1: Chọn 
checkbox các bản ghi
Bước 2:
TH1: Click button 
"Phê duyệt"
TH2: Click button 
"Từ chối" thì 
nhập Comment
TH1: Phê duyệt => 
Cập nhật User vào 
hệ thống
TH2: Từ chối => Trả
bản ghi về Inputter 
CN/PGD
16
Authoriser 
CN/PGD phê 
duyệt/từ
chối bản ghi 
đăng ký User 
đơn
Tôi là 
Authoriser CN/
PGD và đang ở
"Màn hình 
Danh sách các 
bản ghi đăng 
ký User/User"
TH1: Click button 
"Phê duyệt" tại 
bản ghi
TH2: Click button 
"Từ chối" tại bản 
ghi thì nhập 
Comment
TH1: Phê duyệt => 
Cập nhật User vào 
hệ thống
TH2: Từ chối => Trả
bản ghi về Inputter 
CN/PGD


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
V. NỘI DUNG KHÁC  –  13
5 V. NỘI DUNG KHÁC 
<<Đơn vị bổ sung các nội dung khác theo đề xuất>>
5.1 5.1. Tài liệu bổ sung
(Mô tả)
Tên tài liệu
Link tài liệu 
Ghi chú
1
....
2
....
3


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
VI. YÊU CẦU PHI CHỨC NĂNG –  14
•
•
•
•
•
•
•
•
•
•
•
•
•
•
•
6 VI. YÊU CẦU PHI CHỨC NĂNG
6.1 6.1. Yêu cầu về an ninh/bảo mật và phân quyền sử dụng *
(Mô tả và ví dụ)
<<Xác định loại dữ liệu mà ứng dụng/hệ thống lưu trữ xử lý (dữ liệu nhạy cảm, dữ liệu thẻ, hoặc dữ liệu cá 
nhân, ...) để tuân theo các yêu cầu bảo mật dữ liệu liên quan (PCI DSS, Nghị định 13/2023,…):
Tham chiếu các văn bản nội bộ của MB đối với các loại dữ liệu như dữ liệu nhạy cảm, dữ liệu thẻ, hoặc 
dữ liệu cá nhân, ... (ví dụ: dữ liệu thẻ thì tham chiếu các yêu cầu theo Quy chế ATTT và Phụ lục 05 của 
Quy chế Thẻ,…)
Phối hợp với TT ATTT hoặc Khối Dữ liệu để tư vấn, xác định các yêu cầu Luật định (như PCI DSS, Nghị 
định 13/2023, ...)  liên quan đến dữ liệu thẻ, dữ liệu cá nhân, và các dữ liệu nhạy cảm khác>>
Tùy theo yêu cầu phát triển mà tuân thủ checklist LTAT (ví dụ: nếu là yêu cầu phát triển app mobile thì cần 
tham chiếu đến phụ lục về yêu cầu ATTT Mobile....)>>
Lưu ý:
Nếu YCPT không phát sinh thêm các tiêu chuẩn bảo mật riêng (trên hệ thống có sẵn) thì ghi: Không 
phát sinh thêm và tham chiếu đến tài liệu thiết kế gốc
Nếu có phát sinh các phần yêu cầu bảo mật bổ sung thì ghi rõ đầy đủ các yêu cầu về An ninh/Bảo mật
Không phát sinh thêm và tham chiếu đến tài liệu thiết kế gốc
6.2 6.2. Yêu cầu về mã hóa dữ liệu *
(Mô tả và ví dụ)
<<Mô tả các yêu cầu về mã hóa dữ liệu truyền nhận>>
Tùy theo yêu cầu phát triển mà tuân thủ checklist LTAT (ví dụ: nếu là yêu cầu phát triển app mobile thì cần 
tham chiếu đến phụ lục về yêu cầu ATTT Mobile....)>>
Lưu ý:
Nếu YCPT không phát sinh thêm phần mã hóa dữ liệu (trên hệ thống có sẵn) thì ghi: Không phát sinh 
thêm và tham chiếu đến tài liệu thiết kế gốc
Nếu có phát sinh các dữ liệu cần mã hóa ghi rõ đầy đủ các yêu cầu về mã hóa dữ liệu (Lưu ý các dữ
liêu mô tả đầu ra đầu vào nếu các dữ liệu nào nhạy cảm cần bổ sung thêm phần mã hóa dữ liệu)
Không phát sinh thêm và tham chiếu đến tài liệu thiết kế gốc
6.3 6.3. Yêu cầu về quản lý vận hành và lưu vết (lưu logs) *
(Mô tả và ví dụ)
<< Mô tả các yêu cầu về đáp ứng hoạt động quản lý vận hành, lưu vết (lưu logs) theo quy định của Quy chế ATTT 
(tham chiếu điều 26 Giám sát và ghi nhật ký hoạt động của HTTT)>>
Không có
6.4 6.4. Yêu cầu về khả năng chịu tải của hệ thống *
(Mô tả tiêu chí và ví dụ)
<<Mục này ghi rõ quy mô sử dụng của người dùng: Số lượng user sử dụng hệ thống, quy mô dữ liệu>>


SME.TRADE FINANCE  –  US1: Tính năng Quản lý user
VI. YÊU CẦU PHI CHỨC NĂNG –  15
•
Ước lượng các tham số để đánh giá về hiệu năng hệ
thống *
Giá trị
1
Dự kiến/ kỳ vọng mức độ tăng độ tăng trưởng của số
lượng khách hàng/ người dùng nội bộ theo thời gian 
(hàng quý, hàng năm...) là bao nhiêu
2
Số lượng người dùng truy cập đồng thời mong muốn 
tại thời điểm cao điểm là bao nhiêu
3
Tổng số lượng số lượt sử dụng (volume transaction)
bình quân dự kiến trong 1 khoảng thời gian (giây/phút)
Ước lượng các tham số để đánh giá về hiệu năng hệ
thống *
Giá trị
1
2
3
6.5 6.5. Yêu cầu về chính sách lưu trữ dữ liệu
(Mô tả và ví dụ)
<< Mô tả các yêu cầu về chính sách lưu trữ dữ liệu (Data Retention/Archiving Policy). Tham chiếu biểu mẫu Yêu cầu về
chính sách lưu trữ dữ liệu của Quy trình Archiving dữ liệu>>
Không có
6.6 6.6. Yêu cầu khác
(Mô tả và ví dụ)
•
•
<<Mục này mô tả các yêu cầu phi chức năng khác không phân loại được vào các loại trên>>
<<Yêu cầu khác nên tách thành ES độc lập>>



