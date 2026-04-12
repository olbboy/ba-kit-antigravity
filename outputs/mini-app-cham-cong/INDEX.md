# Mini App Chấm Công — EAMS

*Updated: 2026-04-11 | 12 modules · 5 phases · 53 US · 12 API specs · 12 DB schemas · 12 test suites · 1 RTM*

## Cấu trúc dự án

- [README — Tổng quan dự án](./README.md)
- [EAMS v2.1 — Tài liệu nghiệp vụ toàn diện](./eams-v2-comprehensive.md)
- [📊 AUDIT-REPORT — Báo cáo sức khỏe dự án](./AUDIT-REPORT.md)
- [🔗 RTM — Ma trận truy vết yêu cầu (482 TCs)](./RTM.md)

### Tổng quan

- [Tổng quan 12 modules](./overview/modules-overview.md)
- [BRD-01 Nhân viên](./overview/BRD-01-Nhân-viên.md) — 6 chức năng ESS (EMPLOYEE)
- [BRD-02 Quản lý](./overview/BRD-02-Quản-lý.md) — 7 chức năng (MANAGER, DEPT_HEAD)
- [BRD-03 HR Admin](./overview/BRD-03-HR-Admin.md) — 13 chức năng quản trị (SITE_HR, GLOBAL_HR)
- [BRD-04 IT & System Admin](./overview/BRD-04-IT-và-System-Admin.md) — 10 chức năng kỹ thuật (IT_ADMIN, SYS_ADMIN)
- [Demo Plan Sprint 8](./overview/demo-plan-sprint-8.md)

---

### Phase 01: Thiết lập hệ thống — Sprint 8


- **m05 Quản lý Nhân sự** — [BRD](./modules/m05-quan-ly-nhan-su/README.md) · [API](./modules/m05-quan-ly-nhan-su/api-spec.md) · [DB](./modules/m05-quan-ly-nhan-su/db-schema.md)
  - [US-EMP-01](./modules/m05-quan-ly-nhan-su/us-emp-01-so-do-co-cau-to-chuc.md) · [US-EMP-02](./modules/m05-quan-ly-nhan-su/us-emp-02-quan-ly-phong-ban.md) · [US-EMP-03](./modules/m05-quan-ly-nhan-su/us-emp-03-danh-sach-nhan-su.md) · [US-EMP-04](./modules/m05-quan-ly-nhan-su/us-emp-04-bulk-import-nhan-vien.md) · [US-EMP-05](./modules/m05-quan-ly-nhan-su/us-emp-05-dashboard-hien-dien.md) · [US-EMP-06](./modules/m05-quan-ly-nhan-su/us-emp-06-danh-muc-cap-bac.md)
- **m06 Ca làm việc** — [BRD](./modules/m06-ca-lam-viec/README.md) · [API](./modules/m06-ca-lam-viec/api-spec.md) · [DB](./modules/m06-ca-lam-viec/db-schema.md)
  - [US-SHIFT-01](./modules/m06-ca-lam-viec/us-shift-01-danh-sach-ca-lam-viec.md) · [US-SHIFT-02](./modules/m06-ca-lam-viec/us-shift-02-cau-hinh-gio-va-ngay-lam-viec.md) · [US-SHIFT-03](./modules/m06-ca-lam-viec/us-shift-03-gioi-han-thoi-gian-cham-cong-punch-limit.md) · [US-SHIFT-04](./modules/m06-ca-lam-viec/us-shift-04-cau-hinh-gio-nghi.md) · [US-SHIFT-05](./modules/m06-ca-lam-viec/us-shift-05-import-nhan-vien-vao-ca.md) · [US-SHIFT-06](./modules/m06-ca-lam-viec/us-shift-06-phan-ca-theo-pattern.md) · [US-SHIFT-07](./modules/m06-ca-lam-viec/us-shift-07-xem-lich-phan-ca-team.md)
- **m07 Lịch nghỉ** — [BRD](./modules/m07-lich-nghi/README.md) · [API](./modules/m07-lich-nghi/api-spec.md) · [DB](./modules/m07-lich-nghi/db-schema.md)
  - [US-HOL-01](./modules/m07-lich-nghi/us-hol-01-quan-ly-danh-sach-ngay-nghi.md) · [US-HOL-02](./modules/m07-lich-nghi/us-hol-02-cau-hinh-policy-nghi-va-rule-nghi.md) · [US-HOL-03](./modules/m07-lich-nghi/us-hol-03-logic-sync-batch-job.md) · [US-HOL-04](./modules/m07-lich-nghi/us-hol-04-api-hien-thi.md)
- **m09 Thông báo** — [BRD](./modules/m09-thong-bao/README.md) · [API](./modules/m09-thong-bao/api-spec.md) · [DB](./modules/m09-thong-bao/db-schema.md)
  - [US-NOTIF-01](./modules/m09-thong-bao/us-notif-01-cau-hinh-kenh-thong-bao.md) · [US-NOTIF-02](./modules/m09-thong-bao/us-notif-02-cau-hinh-su-kien-kich-hoat.md) · [US-NOTIF-03](./modules/m09-thong-bao/us-notif-03-quan-ly-policy-thong-bao.md) · [US-NOTIF-04](./modules/m09-thong-bao/us-notif-04-quan-ly-template-email.md)

### Phase 02: Định danh Camera AI — Sprint 8


- **m08 Camera AI** — [BRD](./modules/m08-camera-ai/README.md) · [API](./modules/m08-camera-ai/api-spec.md) · [DB](./modules/m08-camera-ai/db-schema.md)
  - [US-CAM-01](./modules/m08-camera-ai/us-cam-01-quan-ly-danh-sach-thiet-bi.md) · [US-CAM-02](./modules/m08-camera-ai/us-cam-02-mapping-nhan-vien.md) · [US-CAM-03](./modules/m08-camera-ai/us-cam-03-health-check-va-monitoring.md) · [US-CAM-04](./modules/m08-camera-ai/us-cam-04-dang-ky-khuon-mat-nhan-vien.md)

### Phase 03: Vận hành chấm công — Sprint 8


- **m01 Chấm công** — [BRD](./modules/m01-cham-cong/README.md) · [API](./modules/m01-cham-cong/api-spec.md) · [DB](./modules/m01-cham-cong/db-schema.md)
  - [US-ATTEN-01](./modules/m01-cham-cong/us-atten-01-hub-cham-cong.md) · [US-ATTEN-02](./modules/m01-cham-cong/us-atten-02-thong-ke-hieu-suat-thang.md) · [US-ATTEN-03](./modules/m01-cham-cong/us-atten-03-xem-chi-tiet-nhat-ky-cham-cong.md) · [US-ATTEN-04](./modules/m01-cham-cong/us-atten-04-trung-tam-canh-bao-va-thong-bao.md) · [US-ATTEN-05](./modules/m01-cham-cong/us-atten-05-nhap-cham-cong-thu-cong.md)

### Phase 04: Xử lý đơn từ — Sprint 9


- **m04 Trung tâm Đăng ký** — [BRD](./modules/m02-trung-tam-dang-ky/README.md) · [API](./modules/m02-trung-tam-dang-ky/api-spec.md) · [DB](./modules/m02-trung-tam-dang-ky/db-schema.md)
  - [US-REG-01](./modules/m02-trung-tam-dang-ky/us-reg-01-dang-ky-nghe-phep.md) · [US-REG-02](./modules/m02-trung-tam-dang-ky/us-reg-02-dang-ky-doi-ca.md) · [US-REG-03](./modules/m02-trung-tam-dang-ky/us-reg-03-dang-ky-tang-ca.md) · [US-REG-04](./modules/m02-trung-tam-dang-ky/us-reg-04-theo-doi-don-tu-va-han-muc.md) · [US-REG-05](./modules/m02-trung-tam-dang-ky/us-reg-05-cau-hinh-chinh-sach-phep-nam.md) · [US-REG-06](./modules/m02-trung-tam-dang-ky/us-reg-06-dang-ky-cong-tac-va-wfh.md)
- **m03 Giải trình** — [BRD](./modules/m03-giai-trinh/README.md) · [API](./modules/m03-giai-trinh/api-spec.md) · [DB](./modules/m03-giai-trinh/db-schema.md)
  - [US-EXPL-01](./modules/m03-giai-trinh/us-expl-01-danh-sach-loi-can-giai-trinh.md) · [US-EXPL-02](./modules/m03-giai-trinh/us-expl-02-yeu-cau-sua-cham-cong.md)
- **m10 Phê duyệt** — [BRD](./modules/m10-phe-duyet/README.md) · [API](./modules/m10-phe-duyet/api-spec.md) · [DB](./modules/m10-phe-duyet/db-schema.md)
  - [US-APPR-01](./modules/m10-phe-duyet/us-appr-01-inbox-phe-duyet.md) · [US-APPR-02](./modules/m10-phe-duyet/us-appr-02-cau-hinh-chuoi-phe-duyet.md) · [US-APPR-03](./modules/m10-phe-duyet/us-appr-03-phe-duyet-hang-loat.md)

### Phase 05: Báo cáo & Hoàn thiện — Sprint 10


- **m05 Báo cáo cá nhân** — [BRD](./modules/m04-bao-cao-ca-nhan/README.md) · [API](./modules/m04-bao-cao-ca-nhan/api-spec.md) · [DB](./modules/m04-bao-cao-ca-nhan/db-schema.md)
  - [US-RPTPRS-01](./modules/m04-bao-cao-ca-nhan/us-rptprs-01-dashboard-hieu-suat-ca-nhan.md) · [US-RPTPRS-02](./modules/m04-bao-cao-ca-nhan/us-rptprs-02-bang-kpi-va-highlights.md)
- **m11 Báo cáo tổng** — [BRD](./modules/m11-bao-cao-tong/README.md) · [API](./modules/m11-bao-cao-tong/api-spec.md) · [DB](./modules/m11-bao-cao-tong/db-schema.md)
  - [US-RPT-01](./modules/m11-bao-cao-tong/us-rpt-01-dashboard-quan-ly.md) · [US-RPT-02](./modules/m11-bao-cao-tong/us-rpt-02-xuat-bao-cao-va-payroll.md) · [US-RPT-03](./modules/m11-bao-cao-tong/us-rpt-03-bao-cao-tuan-thu.md) · [US-RPT-04](./modules/m11-bao-cao-tong/us-rpt-04-khoa-ky-luong.md)

### Cross-cutting — Sprint 8-10


- **m12 Quản trị hệ thống** — [BRD](./modules/m12-quan-tri-he-thong/README.md) · [API](./modules/m12-quan-tri-he-thong/api-spec.md) · [DB](./modules/m12-quan-tri-he-thong/db-schema.md)
  - [US-SYS-01](./modules/m12-quan-tri-he-thong/us-sys-01-quan-ly-chi-nhanh.md) · [US-SYS-02](./modules/m12-quan-tri-he-thong/us-sys-02-audit-log-viewer.md) · [US-SYS-03](./modules/m12-quan-tri-he-thong/us-sys-03-employee-offboarding.md) · [US-SYS-04](./modules/m12-quan-tri-he-thong/us-sys-04-chot-cong-thang.md) · [US-SYS-05](./modules/m12-quan-tri-he-thong/us-sys-05-employee-onboarding.md) · [US-SYS-06](./modules/m12-quan-tri-he-thong/us-sys-06-cau-hinh-data-retention-policy.md)

