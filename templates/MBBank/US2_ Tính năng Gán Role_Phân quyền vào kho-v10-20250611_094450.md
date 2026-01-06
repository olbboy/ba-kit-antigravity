US2: Tính năng Gán Role/Phân quyền vào kho
SME.TRADE FINANCE
Exported on  06/11/2025


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
 –  2
Table of Contents
1 TÀI LIỆU ĐẶC TẢ PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG..........................................4
2 I. THÔNG TIN YÊU CẦU.............................................................................................5
3 II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG...............................................................6
3.1 2.1. Mục tiêu thực hiện (CARD) * ...................................................................................................6
4 IV. MÔ TẢ YÊU CẦU...................................................................................................7
4.1 4.1. Mô tả yêu cầu chi tiết (CONVERSATION)................................................................................7
4.2 4.1.1. Sơ đồ quy trình, thao tác xử lý nghiệp vụ..........................................................................7
5 V. NỘI DUNG KHÁC.................................................................................................12
5.1 5.1. Tài liệu bổ sung .....................................................................................................................12
6 VI. YÊU CẦU PHI CHỨC NĂNG ...............................................................................13
6.1 6.1. Yêu cầu về an ninh/bảo mật và phân quyền sử dụng *......................................................13
6.2 6.2. Yêu cầu về mã hóa dữ liệu *.................................................................................................13
6.3 6.3. Yêu cầu về quản lý vận hành và lưu vết (lưu logs) *...........................................................13
6.4 6.4. Yêu cầu về khả năng chịu tải của hệ thống * ......................................................................13
6.5 6.5. Yêu cầu về chính sách lưu trữ dữ liệu.................................................................................14
6.6 6.6. Yêu cầu khác..........................................................................................................................14


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
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


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
TÀI LIỆU ĐẶC TẢ PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG –  4
1 
TÀI LIỆU ĐẶC TẢ PHÂN TÍCH YÊU CẦU NGƯỜI DÙNG


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
1 mailto:dungnt.sgd@mbbank.com.vn
I. THÔNG TIN YÊU CẦU –  5
2 I. THÔNG TIN YÊU CẦU
Tên yêu 
cầu *
Tính năng Gán Role/Phân quyền vào kho
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
@ Tên DEV 
lead
<<Phòng/TT/Khối  VD: 
Phòng CNKHCN >>
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


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG –  6
3 II. MỤC TIÊU THỰC HIỆN VÀ ĐO LƯỜNG
3.1 2.1. Mục tiêu thực hiện (CARD) *
2.2. Tiêu chí đo lường về hiệu quả kinh doanh/nghiệp vụ *2.3. Tiêu chí đo lường về mức độ sử dụng *
III. XÁC ĐỊNH VẤN ĐỀ
3.1. Khảo sát sơ bộ *
3.2. Xác định vấn đề với các bên liên quan bao gồm cả người dùng cuối *


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
IV. MÔ TẢ YÊU CẦU –  7
4 IV. MÔ TẢ YÊU CẦU
4.1 4.1. Mô tả yêu cầu chi tiết (CONVERSATION) 
4.2 4.1.1. Sơ đồ quy trình, thao tác xử lý nghiệp vụ
4.2. Tham chiếu chi tiết *
4.3. Tác động của phát triển đến hệ thống
4.4. Tiêu chí nghiệm thu (Confirmation) *
Đẩy lên MO:
Luồng gán hợp lệ (Thỏa mãn Bảng quy định các chức danh phù hợp cho các vị trí quản lý): 
Bước 
Thao tác
Kết quả
1
Inputter CN/PGD đẩy duyệt bản ghi
Tạo bản ghi trên MO
2
Các cấp phê duyệt phê duyêt/từ chối trên 
MO
Đẩy thông tin phê duyệt/từ chối về hệ
thống
Luồng gán không hợp lệ (Không Thỏa mãn Bảng quy định các chức danh phù hợp cho các vị trí quản lý): 
Bước 
Thao tác
Kết quả
1
Inputter CN/PGD đẩy duyệt bản ghi
Tạo bản ghi trên MO
2
Các cấp phê duyệt phê duyêt/từ chối trên MO
Đẩy thông tin phê duyệt/từ chối về hệ thống
3
Sau cấp phê duyệt cuối cùng (tại CN/PGD) phê 
duyệt
Hệ thống gửi Email cho HO
4
HO từ chối/phê duyệt qua mail
Hệ thống xác định kết quả
Bảng quy định các chức danh phù hợp cho các vị trí quản lý
Đơn vị
Thành viên
Chức danh chính được 
UQ cấp CN tự phê duyệt
Chức danh khác quy 
định cấp HO phê duyệt
Hình thức
Tại chi nhánh
Thành viên 1
Giám đốc Chi nhánh
Tất cả các chức danh còn 
lại của CN và PGD/CN
Ủy quyền
Giám đốc Dịch vụ


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
IV. MÔ TẢ YÊU CẦU –  8
Phó Giám đốc Chi nhánh 
KHCN
Phó Giám đốc Chi nhánh 
SME
Thành viên 2
Giám đốc Dịch vụ (trường 
hợp CN không có T/PP 
DVKH và KSV)
Trưởng Phòng DVKH
Phó Phòng DVKH
Kiểm soát viên
Thành viên 3
Trưởng Quỹ
Đề cử người 
thay thế
Kiểm Ngân
Giao Dịch Viên
Tại PGD/CN
Thành viên 1
Giám đốc PGD/CN
Ủy quyền
Phó Giám đốc PGD/CN
Giám đốc Dịch vụ (nhân 
sự CN xuống hỗ trợ)
Phó Giám đốc Chi nhánh 
KHCN (nhân sự CN xuống 
hỗ trợ)
Phó Giám đốc Chi nhánh 
SME (nhân sự CN xuống 
hỗ trợ)
Thành viên 2
Trưởng Phòng DVKH 
(nhân sự CN xuống hỗ
trợ)
Phó Phòng DVKH (nhân 
sự CN xuống hỗ trợ)


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
2 https://confluence.mbbank.com.vn/download/attachments/501426136/
QC%C4%90H.B4.TT.MB.01%20M%E1%BA%ABu%20Q%C4%90%20giao%20nhi%E1%BB%87m%20v%E1%BB%A5%20TV%20qu%E1%BA%A3n%
20l%C3%BD%20kho%2C%20k%C3%A9t%20%282%29.docx?api=v2&modificationDate=1749180134859&version=1
3 https://confluence.mbbank.com.vn/download/attachments/501426136/
M%E1%BA%ABu%20Gi%E1%BA%A5y%20%C4%91%E1%BB%81%20ngh%E1%BB%8B%20ph%C3%A2n%20c%C3%B4ng%20v%C3%A0o%20kho
%20ti%E1%BB%81n.docx?api=v2&modificationDate=1749180212491&version=1
IV. MÔ TẢ YÊU CẦU –  9
Kiểm soát viên
Thành viên 3
Kiểm Ngân
Đề cử người 
thay thế
Giao Dịch Viên
Các File trình ký MO:
File gán role cho 3 quản lý: QCĐH.B4.TT.MB.01 Mẫu QĐ giao nhiệm vụ TV quản lý kho, két (2).docx2
File phân quyền vào kho: Mẫu Giấy đề nghị phân công vào kho tiền.docx3
ST
T
Scenario
(kịch bản)
Given
(trạng thái)
When
(điều kiện)
Then
(kết quả mong 
muốn)
1
Inputter PGD/CN 
xem thông tin "3 
quản lý kho" và 
danh sách các User 
Tôi là Inputter 
PGD/CN  và đã log 
in và hệ thống
Tôi click vào menu “Gán Role 
& Phân quyền vào kho”
Hệ thống hiển thị màn hình 
“Gán Role & Phân quyền 
vào kho”
Gồm 2 phần thông tin
3 quản lý kho
Các User trong hệ
thống
2
Inputter PGD/CN 
tạo bản ghi gán 
Role cho 3 quản lý
Tôi là Inputter 
PGD/CN  và tôi 
đang ở màn hình 
“Gán Role & Phân 
quyền vào kho”
Tôi chọn các user cho 3 Role 
quản lý
Hệ thống verify user theo 
từng vị trí quản lý 1, quản lý 
2, quản lý 3 (Bảng quy định 
các chức danh phù hợp cho 
các vị trí quản lý)
Nếu hợp lệ => Đẩy bản ghi 
lên MO
3
Inputter PGD/CN 
tạo bản ghi gán 
Role cho 3 quản lý
Tôi là Inputter 
PGD/CN  và tôi 
đang ở màn hình 
“Gán Role & Phân 
quyền vào kho”
Tôi chọn các user hợp lệ cho 
3 Role quản lý + Chọn User 
phê duyệt MO
Hệ thống tạo bản ghi trên 
MO


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
IV. MÔ TẢ YÊU CẦU –  10
ST
T
Scenario
(kịch bản)
Given
(trạng thái)
When
(điều kiện)
Then
(kết quả mong 
muốn)
4
Inputter PGD/CN 
tạo bản ghi phân 
quyền vào kho cho 
các user hệ thống
Tôi là Inputter 
PGD/CN  và tôi 
đang ở màn hình 
“Gán Role & Phân 
quyền vào kho”
Tôi nhập thời gian ra/vào 
kho cho các user + Chọn 
User phê duyệt MO
Hệ thống tạo bản ghi trên 
MO
5
Các cấp phê duyệt 
phê duyệt/từ chối 
bản ghi MO (Áp 
dung cho việc gán 3 
Role quản lý)
Tôi là CPD và tôi 
đang ở hệ thống 
MO
Tôi phê duyệt/từ chối bản 
ghi 
Hệ thống ghi nhận được 
kết quả từ MO trả về
TH1: Nếu từ chối => Trả
bản ghi cho Inputter PGD/
CN
TH2: Nếu phê duyệt
TH2.1: Luồng gán đúng role 
được quy định => Hoàn 
thành
TH2.2: Luồng gán khác role 
được quy định
=> Gửi Email cho đầu mối 
của HO
6
Inputter PGD/CN ghi 
nhận được kết quả
phê duyêt/từ chối 
của HO với luồng 
gán khác role được 
quy định (Áp dung 
cho việc gán 3 Role 
quản lý)
Tôi là Inputter 
PGD/CN 
HO phản hồi kết quả qua 
Email
Hệ thống dựa vào nội dung 
của Email (Từ chối/Đồng ý) 
để cập nhật trạng thái cho 
bản ghi
7
Các cấp phê duyệt 
phê duyệt/từ chối 
bản ghi MO (Áp 
dung cho việc phân 
quyền User)
Tôi là CPD và tôi 
đang ở hệ thống 
MO
Tôi phê duyệt/từ chối bản 
ghi 
Hệ thống ghi nhận được 
kết quả từ MO trả về
TH1: Nếu từ chối => Trả
bản ghi cho Inputter PGD/
CN
TH2: Nếu phê duyệt => 
Hoàn thành


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
IV. MÔ TẢ YÊU CẦU –  11
ST
T
Scenario
(kịch bản)
Given
(trạng thái)
When
(điều kiện)
Then
(kết quả mong 
muốn)
8
Inputter PGD/CN 
tạo bản ghi phân 
quyền vào kho
Tôi là Inputter 
PGD/CN  và tôi 
đang ở màn hình 
“Gán Role & Phân 
quyền vào kho”
Bước 1: Tôi chọn danh sách 
các User
Bước 2: Tôi chọn thời gian 
ra vào kho (áp dụng cho 
toàn bộ các user đã chọn)
Bước 3: Tôi chọn các user 
phê duyệt trên MO
Bước 4: Tôi chọn button 
"Gửi duyệt"
Hệ thống tạo bản ghi trên 
MO
9
Các cấp phê duyệt 
phê duyệt/từ chối 
bản ghi MO 
Tôi là CPD và tôi 
đang ở hệ thống 
MO
Tôi phê duyệt/từ chối bản 
ghi 
Hệ thống ghi nhận được 
kết quả từ MO trả về


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
V. NỘI DUNG KHÁC  –  12
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


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
VI. YÊU CẦU PHI CHỨC NĂNG –  13
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


SME.TRADE FINANCE  –  US2: Tính năng Gán Role/Phân quyền vào kho
VI. YÊU CẦU PHI CHỨC NĂNG –  14
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


