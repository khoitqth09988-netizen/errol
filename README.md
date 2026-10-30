<div align="center">

# 🌸 Tiny & 20/10 — Chuyến bay chúc mừng ngày 20/10

**Web tương tác dành tặng phái đẹp nhân ngày 20/10**  
Hành trình cùng Tiny nạp năng lượng, cất cánh và gửi gắm lời chúc ngọt ngào ✈️💛

🌐 **[Trải nghiệm ngay →](https://khoitqth09988-netizen.github.io/errol/)**

</div>

---

## ✨ Giới thiệu

"Tiny & 20/10" là một trang web **tương tác kể chuyện** (storytelling) được viết hoàn toàn bằng HTML/CSS/JS thuần — không framework, không build step. Người xem đồng hành cùng nhân vật **Tiny** qua các phân cảnh:

| Cảnh | Điều gì xảy ra |
|------|-----------------|
| 🌤️ Mở đầu | Tiny xuất hiện giữa bầu trời đầy sao, phong cảnh chuyển động theo cảm xúc |
| ❓ Câu hỏi | Tiny đặt câu hỏi dễ thương, biểu cảm mắt sinh động |
| 🎀 Phân cảnhHealth | Chú chim & bướm sinh động (GIF có hoạt ảnh, tự chuyển bản tĩnh PNG khi ra khỏi màn hình để tiết kiệm pin) |
| ✈️ Cất cánh | Máy bay cất cánh, đồng hồ năng lượng vơi dần về 0% theo easing mềm mại |
| 🎉 Finale | Thiệp chúc 20/10 hiện ra theo nhịp stagger — chia sẻ Facebook, sao chép link, **tải mã nguồn trên GitHub**, cài đặt ứng dụng |

Sau mỗi bước, người xem có thể **chạm vào màn hình để thả tim**, tua lại từ đầu hoặc gửi link cho bạn bè.

---

## 🚀 Tính năng chính

- 🎬 **Trải nghiệm tương tác nhiều cảnh** — tiến về phía trước bằng nút, phím Space/Enter/→, cảm ứng
- 💌 **Chia sẻ dễ dàng** — link tự đồng bộ theo URL đang xem (không hardcode domain), nút chia sẻ Facebook, sao chép link
- ⬇️ **Mã nguồn mở** — nút GitHub ngay trong màn cuối, ai cũng tải ZIP về được
- 📲 **Cài đặt như app (PWA)** — có `manifest.json` + `sw.js` (service worker): cài trên **Android, iPhone/iPad, PC**; hỗ trợ xem offline
- ⚡ **Tối ưu thiết bị** — chuyển bản tĩnh khi ra khỏi màn hình, tôn trọng `prefers-reduced-motion`, tối ưu LCP (preload ảnh hero), giao diện responsive từ điện thoại nhỏ đến desktop rộng
- 🎨 **Hiệu ứng đẹp mắt** — stagger entrance, shimmer tiêu đề, hào quang quanh panel, pháo giấy ăn mừng, trái tim bay lên khi chạm

---

## 🛠️ Công nghệ

- **Ngôn ngữ thuần**: HTML5, CSS3, JavaScript (ES2019+) — không React/Vue, không bundler
- **43 file CSS + 13 file JS** tách theo chủ đề (mỗi cảnh/phần một nhóm file, dễ bảo trì)
- **PWA**: Web App Manifest + Service Worker (network-first cho trang, stale-while-revalidate cho asset)
- **Font**: Google Fonts (`Courier Prime`, `display=swap`)
- **Hosting**: GitHub Pages (HTTPS → PWA hoạt động)

---

## 🖥️ Chạy thử trên máy

Chỉ cần một static server bất kỳ — ví dụ Python:

```bash
git clone https://github.com/khoitqth09988-netizen/errol.git
cd errol
python3 -m http.server 8000
# mở http://localhost:8000
```

> ⚠️ Nên chạy qua `http://localhost` thay vì mở `index.html` trực tiếp bằng `file://` — service worker và một số API (clipboard…) chỉ hoạt động trên origin có http/https.

---

## 📦 Cấu trúc dự án

```
errol/
├── index.html          # Trang chính (kết nối toàn bộ css/js)
├── manifest.json       # PWA manifest (icon, màu, chế độ standalone)
├── sw.js               # Service worker (cache offline)
├── css/                # 43 stylesheet theo từng phân cảnh + tối ưu thiết bị
├── js/                 # 13 module: main.js (luồng chính), starfield.js, …
└── media/              # Ảnh, GIF (chim/butterfly), favicon, icon PWA 192/512
```

---

## 📲 Cài đặt lên điện thoại / máy tính

| Nền tảng | Cách làm |
|----------|----------|
| **Android (Chrome)** | Mở trang → menu ⋮ → *"Cài đặt ứng dụng / Add to Home screen"* — hoặc bấm nút 📥 trong màn cuối |
| **iPhone/iPad (Safari)** | Bấm nút **Chia sẻ ↗** → *"Thêm vào màn hình chính"* — hoặc bấm nút 📥 trong màn cuối để xem hướng dẫn |
| **PC (Chrome/Edge)** | Bấm icon cài đặt ở thanh địa chỉ, hoặc bấm nút 📥 trong màn cuối |

> Service worker chỉ kích hoạt trên **HTTPS** (GitHub Pages) hoặc `localhost`.

---

## 🚢 Deploy lên GitHub Pages

1. **Fork/clone** repo này về tài khoản của bạn
2. Vào **Settings → Pages**, chọn nhánh `main` (hoặc `arena/...`) và thư mục gốc `/`
3. Chờ ~1 phút → trang chạy tại `https://<tai-khoan>.github.io/<ten-repo>/`
4. Nhớ mở trên HTTPS để PWA hoạt động

---

## ❤️ Credits

- Code, ý tưởng & lời chúc: **khoitqth09988-netizen**
- Nhân vật **Tiny**, icon & hiệu ứng: chế tạo riêng cho dự án 🌸
- Font: [Courier Prime](https://fonts.google.com/specimen/Courier+Prime)

> Dự án mang mục đích cá nhân – gửi tặng ngày 20/10. Rất vui nếu bạn **⭐ Star** repo hoặc góp ý qua Issues!

<div align="center">

**⬇️ Tải mã nguồn:** [github.com/khoitqth09988-netizen/errol](https://github.com/khoitqth09988-netizen/errol) → nút **Code → Download ZIP**

</div>
