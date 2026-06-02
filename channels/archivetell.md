<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/q7PUYAvXGMoLc70LeGdoNorZxhNCntRc4ixPGaipzyg5ixPCr9L0oPdaoUwnARaFh_8F0pWO-Ru6qZkpE16c-QMMj1wm4cqH-3Sk2yvObOal56Wt2OsKbZ0a3JZayjtuix4dJGuG8aSv_z2b-kDpPwiJgYyPIuKuBKRlR_rurbigFowtQg1SjdfVNR7xFo2xohhsxCDY1FltDd0HgtcVh-yvYsxu6RqEGjr3_9jYKrAvv0pVObzHhy2N4CJzR1K0zqQ55yXJVfFkKZZFVmr48ksrYbh0W4zoxYz0vgiTRr0Dfu_B5hPy8Wfv6U95zsJhh4Rp1G95G-DlhfRLh4e2Rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 8.91K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Gemini Omni تولیدکننده ویدئوی هوش مصنوعی رایگان
پشتیبانی از ورودی متن، تصویر، صدا و ویدئو، قابلیت تولید کلیپ‌های ویدئویی با کیفیت سینمایی
https://omniaipro.app/
@ArchiveTell</div>
<div class="tg-footer">👁️ 95 · <a href="https://t.me/archivetell/5894" target="_blank">📅 17:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zb9UFnXGN2Qc_5HheV1ElrTAdMtivi5i7KfPuW4-Pp2TjZSvPnRBoynDSpL67_kDDNqbuqP30d1ZLgkUlxkGH7V1xLT2_F_cfpjURpB3ZNrNv6wlO7fwQAAAYm8vX4vCSPgX3hXTYPoajKTbFN7RNMwpdSKKacdsF1285q92zjDY38a2Iz6sKOu6ScWaI6O3XO65zpCwPhGZ84T0ZcxmNgs3tqFZKdvWr0GJLe-1EFq5ckT59F_-dUa2RQ03h7dqZsswA4I06xPWtocukwcONOlc2PE9L4i5IsToadX9RetVi0gKQwdwdtIr98uu45fLEkPfYNjROznQbi8pEuqr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">slipnet-enc://AVYDFT1SX5QRahOVGapvCIQOi5iX+F+Ayz7d82kXBzKUgbDFGOsXcyY12oASii0n3Ye5Fj9LOHfyxzQpTH6aZzsHCccHQuHa78SADfbTQRNENnLD6CeHOuPxRffHOjkB+5tHdtQ89Kfk8TzpeVOxfFMxXDMxDhTuX7D/hrMsm9KchoxYpj3l1HNlOSDSMkO6td9WttjNX/TrOGk9jSX3n+bBnR1t64wJs9TYIUUycW/wKH9ntwehzsQ0l7MkpkxjVGD4Qqx8G/AGiOGcqy0OHxb4WsNfWIvP+mR1UcoObW2qJCMqPvMmimZQGTCI0cHIbpH1Kx0GLVXI9USz59N6D+2py/TLS4sGIKK40X2xohmjXthNyo3zcIw20FmuSnV8Dez5RVaSAbUhuCY8Iqa5G/B9U2PmqAMcZSVUh+yr4IoK/7Uelbj4rUAT6SfYQlZiliDE6Wkx7eM5dd8rR2Zxmtjl/Lr1X/qtrMeQgbJ5w5QAlxmAltcolUJt3BH58ZOqpwTe</div>
<div class="tg-footer">👁️ 406 · <a href="https://t.me/archivetell/5893" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">OBITO.conf</div>
  <div class="tg-doc-extra">530 B</div>
</div>
<a href="https://t.me/archivetell/5892" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 423 · <a href="https://t.me/archivetell/5892" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-obito.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5891" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 437 · <a href="https://t.me/archivetell/5891" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هر کی دلش وایرگارد میخواد
دست بالا کنه....؟!
@Sina_1090</div>
<div class="tg-footer">👁️ 629 · <a href="https://t.me/archivetell/5890" target="_blank">📅 16:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">100GB مولتی لوکیشن
vless://d49eb175-facd-4c33-b1be-32c746701184@maple.cloudureld.com:443?security=reality&encryption=none&pbk=-VM1_ol58XU8fQHPvCnllupmpqyI6E1_bp6vpD6hD0w&headerType=none&fp=qq&type=tcp&flow=xtls-rprx-vision&sni=maple.cloudureld.com&sid=7e52de801e7c71de#%F0%9F%87%A8%F0%9F%87%A6%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@island.cloudureld.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&fp=qq&type=xhttp&sni=island.cloudureld.com&sid=a7f9e69f037466b1#%F0%9F%87%AC%F0%9F%87%A7%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=9e327f04ce93c187#%F0%9F%87%B3%F0%9F%87%B1%20%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@developer.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=developer.projectauths.com&fp=random&type=xhttp&sni=developer.projectauths.com&sid=68d14e7adba07698#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
vless://d49eb175-facd-4c33-b1be-32c746701184@dev.projectauths.com:443?mode=auto&path=%2F&security=reality&encryption=none&pbk=U-aI9goYn0iGJ31emKZ1ltON45Ry0LjCl15MnumMD2c&host=dev.projectauths.com&fp=random&type=xhttp&sni=dev.projectauths.com&sid=8a9d1d8916227e5b#%F0%9F%87%A9%F0%9F%87%AA%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 901 · <a href="https://t.me/archivetell/5889" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4i1uvH-NvE3ObcmSzKOT6NMG8FYiQGKnC-peHPvbkJZabGjccVw328WRN-Yyw_1Or3h-61aj7VG83kbatCVCx9vTBxCvpwdZ0BYAzlDZdnoWQs9dz6KHgb5fSNDsyAcFVBC4yU5dVLx0yRWj7Bq5EYvTT5oLcBMNx8EH2rs80mP0c_7tqBbetTsJW4otKUURzFjF_NrD4I7TYdDudREyrGNbO5rH4IGYr78gC8IppizyL6JDTFwEBD0SOyze6IySdOVD1YUOajJQ7BQs1KX7graVSpIV5_SO7NXHgFgqpjGtwfCYn5G9z5xtcHKf1NK6480sYxHhKWeuoSgF7mrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری اندپوینت endpoint برای
کانفیگای وارپ
اسکن کنیم
داخل لینوکس یا ترموکس این رو بزنید
pkg update -y && pkg upgrade -y && pkg install curl -y
bash <(curl -fsSL https://raw.githubusercontent.com/bia-pain-bache/BPB-Warp-Scanner/main/install.sh)
به سوالاتی که میپرسه جواب بدین میگه چندتا اسکن کنم یا سریع باشه یا نرمال. ipv4 رو انتخاب کنید
دقت کنید که اسکن باید بدون فیلتر انجام بشه. اگه فایلش واستون دانلود نمیشه فقط قسمت دانلود فایل رو با فیلترشکن انجام بدین بعد قطع کنید و اسکن کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/5888" target="_blank">📅 15:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3617290e-f2e0-4eb5-9576-a610aa6f2c95@104.167.199.23:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=104.167.199.23&mode=auto&path=%2Fmohraz&pbk=wtVFe9j0FtOMtxUBKJqjd7NZs9-47lsjbnUlWq_MGEs&security=reality&sid=a99c6c05&sni=www.samsung.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/archivetell/5887" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">vless://cc074e81-342d-402c-9fa6-fa907728222a@85.198.20.217:80?type=tcp&encryption=none&security=none#tunnel%2050gb
50gb tunnel
تست شده بر روی : ایرانسل , سامانتل , رایتل , اپتل , مخابرات
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/archivetell/5886" target="_blank">📅 14:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید. warp-generator.github.io/warp/‎ فرقی نداره کدومش باشه از Amnezia باشه فقط.  اندپوینتشو تغییر بدید به این 188.114.97.6:7281 بزنش داخل Amnezia WG با همراه و ایرانسل و مخابرات وصله.  @ArchiveTell</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/archivetell/5885" target="_blank">📅 14:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه کانفیگ از اینجا بگیرید.
warp-generator.github.io/warp/
‎
فرقی نداره کدومش باشه از Amnezia باشه فقط.
اندپوینتشو تغییر بدید به این
188.114.97.6:7281
بزنش داخل Amnezia WG
با همراه و ایرانسل و مخابرات وصله.
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/archivetell/5884" target="_blank">📅 14:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ابزار خط‌فرمان دور زدن DPI روی همه پلتفرم‌ها — با pool تطبیقی چند-IP/چند-SNI
به‌جای یک upstream ثابت، ابزار به‌طور مداوم ترکیب‌های (IP، SNI) را بررسی می‌کند و هر اتصال را از طریق سالم‌ترین جفت هدایت می‌کند — بدون قطع شدن اتصال‌های فعال.
روی Windows، macOS، Linux و Android (Termux) کار می‌کند و برای روش پیش‌فرض نیازی به دسترسی root ندارد.
روش نصب
git clone
https://github.com/hjfisher/SNI-Spoofing-HJ.git
cd SNI-Spoofing-HJ
pip install .
snispf-hj --info
https://github.com/hjfisher/SNISPF-HJ
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/5883" target="_blank">📅 14:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0023e0a6bf.mp4?token=FZKSGbJktwKV9G_HcXNRS_ZPdk1fYK06XwR9y4Ab0Ytm3vSj9r04-WYu--vv3QStHU6E4-V9kcXynuCp0SS4rYLQDFWstRWof_HolHoixefsJp-w_eBDtYwYJAHyZY787S5kJB-7q25S7sCff6nGzTuPH-i9kta2xgTgHymCwxPSbURXuEqpDi9rey07v8N_KUCGpjGduY2ioDm4sV2C0qVhc2DHe-29v9nzq6lf9ZPX9jp9AJfkgc6zZKffqdEmoggqF2LKgqPl-ogU5lU_sjcRBrGdJ1VXYE4Kt8FZB7p04anrx3CST5OywYgloAJIywe-bU_IKVAJzxKnQcyD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0023e0a6bf.mp4?token=FZKSGbJktwKV9G_HcXNRS_ZPdk1fYK06XwR9y4Ab0Ytm3vSj9r04-WYu--vv3QStHU6E4-V9kcXynuCp0SS4rYLQDFWstRWof_HolHoixefsJp-w_eBDtYwYJAHyZY787S5kJB-7q25S7sCff6nGzTuPH-i9kta2xgTgHymCwxPSbURXuEqpDi9rey07v8N_KUCGpjGduY2ioDm4sV2C0qVhc2DHe-29v9nzq6lf9ZPX9jp9AJfkgc6zZKffqdEmoggqF2LKgqPl-ogU5lU_sjcRBrGdJ1VXYE4Kt8FZB7p04anrx3CST5OywYgloAJIywe-bU_IKVAJzxKnQcyD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
قاتل ChatGPT و Claude از PewDiePie جامعه هوش مصنوعی را منفجر کرد: مخزن Odysseus تنها در دو روز تقریباً ۲۵٬۰۰۰ ستاره در GitHub جمع‌آوری کرد و حتی Anthropic نیز به این پروژه علاقه نشان داد.
این جایگزینی برای چت‌بات‌های شرکتی است که بدون محدودیت و نظارت ساخته شده است. Odysseus پاسخ OpenAI، گوگل و دیگر غول‌های صنعت است.
چرا این پروژه اینقدر سروصدا به پا کرده است:
🕤
راه‌اندازی روی کامپیوتر یا سرور — بدون حساب کاربری.
🕤
تمام داده‌ها در اختیار مالک باقی می‌مانند.
🕤
عامل‌های داخلی: مرور وب، ویرایش فایل‌ها، تحلیل اسناد، مرتب‌سازی ایمیل‌ها و غیره.
🕤
پشتیبانی از تحقیقات عمیق.
🕤
API برای اتصال مدل‌های محلی.
🕤
رابط کاربری آسان و کار با گوشی هوشمند.
🕤
امکان کار آفلاین.
https://github.com/pewdiepie-archdaemon/odysseus
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/archivetell/5882" target="_blank">📅 14:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">vless://fec5f560-7e78-4b71-9432-418621738d3f@snapp.ir:80?encryption=none&host=netrox.cnxman.ir&path=%2F&security=none&type=ws#netrox%20--tunnel1gb
1 گیگ تانل
تست کنید با ری اکت بگید</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/archivetell/5881" target="_blank">📅 13:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">۲۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😁
❤️
ایرانسل تست شده ، بقیه نتا وصل بود استفاده کنید..
vless://3638b964-5404-4145-b19c-89f7cc8c237b@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=57e7bd&sni=www.amazon.com&type=tcp#@ArchiveTell%2020.00GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/archivetell/5880" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینترنت امروز فقط برای من خرابه یا نه  همه اوپراتور ها یا پینگ یا 1-</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/archivetell/5879" target="_blank">📅 12:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کانفیگ نامحدود اهدایی یکی از ممبرای عزیز کانال
⚡️
❤️
trojan://4bdbapq0n755s7cr@168.222.43.197:48309?host=168.222.43.197&path=%2FEmpty&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/5878" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینترنت امروز فقط برای من خرابه یا نه
همه اوپراتور ها یا پینگ یا 1-</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/5877" target="_blank">📅 12:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">۵۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://81a1e8f2-3b97-41e5-8c60-7d7d1576e028@185.92.181.217:80?encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&fp=chrome&host=185.92.181.217&mode=auto&path=%2Fmohraz&pbk=SqXIQC6Q68_mpLX_JVFXLHwCeSLHpyk5JhKvrd1P7DA&security=reality&sid=bbe112&sni=www.nvidia.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/archivetell/5876" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5875">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF4A4bwvjLHq8qmJBtrozGeiJTobupt1PxpvPmxkxcOU-OpNWqPe8ZrpD21zBaT_c3n7GM3YW4riAM80LwmXkSFjdmHCtaFl3vg5EE0HbwMgN2uzrPwyQe7Iz3aelgfFv7ompBUTrdxrGb7HiI93MfAndDGHTZnKA7F8iP368teL3XT9oNMyjI57z_wpqGSGEGXI11EWCRRJOj-2ZDw5GLpUG9Fnt-kqq22P8m1xqTcb6dBsvQtgVCZfFHPILzaK7Dd3qdKotSY-i9W1_F-nUE5_AS5wX4nlEy-cIQ5ddVJHvTx_R4rHZFcsxQqTvXfbeTDe082WT3O9SouYIvEA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌏
یادگیری زبان از طریق دیالوگ‌های زنده با هوش مصنوعی — PrettyPolly، سرویسی برای کسانی که به خوبی می‌خوانند و زبان خارجی را می‌فهمند اما در مکالمه معمولی دچار مشکل می‌شوند.
🕤
هم‌صحبت هوش مصنوعی برای تمرین مکالمه — می‌توانید بدون خجالت و ترس از اشتباه، زبان انگلیسی و زبان‌های دیگر را تمرین کنید.
🕤
سناریوهای آماده برای گفتگو — سفر، مصاحبه‌ها، مکالمات روزمره، صحبت‌های کوتاه و موقعیت‌های واقعی دیگر.
🕤
کمک در حین گفتگو — ترجمه، راهنمایی و تصحیح عبارات به صورت آنی در دسترس است.
🕤
بررسی پس از مکالمه — سرویس اشتباهات، نقاط ضعف و کلماتی که باید تکرار شوند را نشان می‌دهد.
🕤
سیستم حفظ پیشرفت — عبارات جدید را می‌توان تثبیت کرد و به تدریج در تمرین‌ها تقویت نمود.
http://prettypolly.app/app
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/5875" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2e603b0b.mp4?token=AORmk0wCjD64zM30u7DMTJ-Bj8UANjeT8g-6Lgxde59zOHHZ4uviPAdF-Vn6jgg_cN8OWvZF1BlDv4ktAY25PKUbUI0Fm-Nge70Z1jzvjjGILzXN1PUE8caSrxnrZkOEMejdIoZn3LAdFAqglVRgnWTl3wkxJ9jek7aA7w1j8kdcar1TlOT9dYh8rpjP5TbbNu2qKlA37DhEY9-Qi6mkHd7E6UmyFOO8mJJGC8lZ46ab8_P6QX1SEpYatziEva62ZEqk2vAaObztL1MyutwZY7YbgDwSGzDhO410CXP7qGpemEJmxQWe55iEKHt2Wmu1ZMrvBPloeY9y7rEz57rToA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2e603b0b.mp4?token=AORmk0wCjD64zM30u7DMTJ-Bj8UANjeT8g-6Lgxde59zOHHZ4uviPAdF-Vn6jgg_cN8OWvZF1BlDv4ktAY25PKUbUI0Fm-Nge70Z1jzvjjGILzXN1PUE8caSrxnrZkOEMejdIoZn3LAdFAqglVRgnWTl3wkxJ9jek7aA7w1j8kdcar1TlOT9dYh8rpjP5TbbNu2qKlA37DhEY9-Qi6mkHd7E6UmyFOO8mJJGC8lZ46ab8_P6QX1SEpYatziEva62ZEqk2vAaObztL1MyutwZY7YbgDwSGzDhO410CXP7qGpemEJmxQWe55iEKHt2Wmu1ZMrvBPloeY9y7rEz57rToA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل راهنمای رسمی پرامپت‌نویسی در Gemini Omni را منتشر کرد
در راهنما چیزهای بسیار جالبی وجود دارد: کنترل دوربین از طریق اصطلاحات حرفه‌ای (dolly zoom، locked off، oner)، همگام‌سازی نور ساختمان با موسیقی، تولید ویدئو بر اساس استوری‌بورد، تغییر سبک با حفظ حرکت، ترکیب ویدئو، تصویر و صدا در یک پرامپت.
نکته کلیدی: کوتاه بنویسید چه می‌خواهید. نیازی به شرح هر فریم نیست.
https://deepmind.google/models/gemini-omni/prompt-guide/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/archivetell/5874" target="_blank">📅 12:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">۱۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
https://cdn.mozcloud.ir/XS_AZ/cue4q8rhm47n4120
بدون فیلترشکن از بخش اسکنر استفاده کنید و بهترین گزینه رو اعمال و کپی کنید
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/archivetell/5873" target="_blank">📅 11:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">AVG Secure VPN  Code:AAUNB7-KK3HT2-4Z4J56  @ArchiveTell | 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/5872" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5871">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۱۶۰ گیگ پروکسی اهدایی یکی از ممبرای عزیز کانال
😁
❤️
https://t.me/proxy?server=hdi.mahdii-coder.eu.cc&port=443&secret=dde9a1ae9b1c4ff69a688d03b7257db653
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/archivetell/5871" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/archivetell/5870" target="_blank">📅 11:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚀
حالا تقریباً هر کسی می‌تواند اولین اپ خودش را بسازد!
دیگر برنامه‌نویسی فقط حفظ کردن کدها و سینتکس‌ها نیست؛ مهم‌تر از همه این است که بتوانی دقیق توضیح بدهی چه می‌خواهی.
🤖
📱
گوشی اندرویدی را به لپ‌تاپ وصل کن، Cursor یا Windsurf یا VS Code AI را باز کن و ایده‌ات را بنویس. هوش مصنوعی بخش زیادی از کار را انجام می‌دهد و نتیجه را مستقیم روی گوشی خودت تست می‌کنی.
💰
مثال:
یک اپ مدیریت هزینه‌های شخصی که آفلاین کار کند، هزینه‌ها را دسته‌بندی کند و آمار روزانه، هفتگی و ماهانه بدهد.
🛠
مراحل:
🔹
گزینه USB Debugging را فعال کن
🔹
گوشی را به لپ‌تاپ وصل کن
🔹
پروژه را با Expo اجرا کن
🔹
خطاها را برای AI بفرست تا رفعشان کند
🔹
نسخه نهایی را روی گوشی نصب کن
💡
ایده‌هایی برای شروع:
✅
ردیاب عادت‌های روزانه
✅
فلش‌کارت درسی
✅
تایمر تمرین ورزشی
✅
اپ یادداشت شخصی
✅
مدیریت مشتریان (Mini CRM)
✅
برنامه‌ریز محتوای تلگرام
🔥
نکته مهم:
امروز لازم نیست از روز اول یک برنامه‌نویس حرفه‌ای باشی. کافی است مشکلت را بشناسی، ایده‌ات را توضیح بدهی و با کمک AI اولین ابزار کاربردی خودت را بسازی.
🌍
دوران جدیدی شروع شده؛ جایی که ساختن نرم‌افزار از همیشه در دسترس‌تر است.
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/5869" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">AVG Secure VPN
Code:
AAUNB7-KK3HT2-4Z4J56
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/archivetell/5868" target="_blank">📅 10:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA44hGNG-hkv3B_fxy_zqtjsNU9GKNl5aPx8bBIuZTl5XgBiYOUSEDb5-ZIh8eSWukTIIp51owNpU0hVS4CqY9ZwFEWMgiV_RNDdNv5XzDVIi4m9InkG1dLSRiKotg-2I_7QYydrHd2ORlSQILP_GI_9obZ6SfUNzEE7O5gnz6cpLJo60mfGtzgS4efQ-dJG8WLtO-Yz2sQxOO-GvcI2Lo3ADsKLSMhsm5BY1EsdVXt_gqF1gPbfl31kp35tgArAb-DpbzeueLnsPOTtOwEClURgndi-1c5f5gkBbI1FnIrQdvCZyonNO7-I5jNAmUVdAB03JHzBofID2qx1rdXJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✴️
استایل‌های سفارشی در Krea 2 اکنون برای همه باز شده‌اند
Krea LoRA را برای مدل جدید خود عرضه کرده است، بنابراین می‌توانید آن را با استایل، شخصیت یا شیء خود آموزش دهید و سپس در تولید استفاده کنید.
قبلاً این ویژگی به صورت بتا برای Max و Business بود، اما اکنون دسترسی گسترده‌تر شده است.
https://www.krea.ai/image/k2-large?style=y45oxkkdp
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/archivetell/5867" target="_blank">📅 09:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://2ddbde64-5bed-4209-b0bf-6a3f090d198c@se.sanaz.online:20609?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%2C%22scMaxEachPostBytes%22%3A%221000000%22%7D&fp=chrome&host=se.sanaz.online&mode=stream-one&path=%2Fstream&pbk=aVfj7ITwEFsWQP4YjFuM-FBb8PWmfBYOwKu_Ag8dVVI&security=reality&sid=d675939d&sni=www.yahoo.com&type=xhttp#@ArchiveTell_@Lozkc
کانفیگ پینگ پایین منطقه ای
اگ وصل نشد خاموش و روشن کنید احتمالا درست شه چون شبکه باگ میخوره گاها
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/5866" target="_blank">📅 09:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIoL8HHHvgQI1MZf6ldbp0dRmjnnvPokhQc393F0OrjKUI5ubHnSpeYEYdNSMQ2cA-0K06uQGyjWfIgEjrPspEyQOKE_yahEIDNWf6W9pe3nVikydSOX1h3chvzbHDMbEA1lCjybqjM1XvXb_hRH__2FZBgMG_r3wTQSQ2e7W8EJQ_Tk8_vGgxL7wARHEIgzxQAbs0FukKmmyBm__gSalV96IsimXAn7Uk3RcbxoqLF8PqT4Lnb-24fyiHMGijcyWhLJ8K9fGeAwu308GDHKrh7weNGijdGEycahrU6zlOOUpRttgna8PCpfW_ElVHrQOUN_3X64jrWsd5stmoR5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
ما در حال ارتقای Gemini به حداکثر هستیم - افزونه‌ی Voyager را پیدا کردیم که ویژگی‌هایی را که در ابتدا فاقد آن بود، اضافه می‌کند. مناسب برای کاربران AI Studio و کاربران معمولی:
🕤
حذف واترمارک از تصاویر.
🕤
مدیریت پیشرفته‌ی چت: حذف دسته‌ای چت‌ها، نقل قول پاسخ‌ها، انتخاب مدل پیش‌فرض و موارد دیگر.
🕤
به شما امکان می‌دهد پوشه‌هایی برای مکالمات با همگام‌سازی از طریق Google Drive ایجاد کنید.
🕤
به شما امکان می‌دهد پیام‌های مورد علاقه را ذخیره کرده و از آنها در Gemini، AI Studio و سایر وب‌سایت‌ها استفاده کنید.
🕤
جدول زمانی راحت: در پاسخ‌ها، رشته‌های مکالمه و پیام‌های مورد علاقه حرکت کنید.
🕤
Markdown، نمودارها و چارت‌ها را به خوبی رندر می‌کند.
🕤
مکالمات را به PDF، Markdown و JSON تبدیل می‌کند.
🕤
تاریخچه‌ی افکار را از Deep Research استخراج می‌کند.
🕤
در Chrome، Edge، Firefox و Safari کار می‌کند.
https://voyager.nagi.fun/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/archivetell/5865" target="_blank">📅 09:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Klbmay0_L6dILiPa_pKUTjXVJEIU9q7qca5Z0ZAJxxSS7x2kn0VLDKchYgU0XxC8cRV8mxQ9LKJJYd69iTNNtk63Nu4M5gpHKw8V4VY2JiUByTnPucxlwdjx30HxmE3wGEuhAeOUFcMGO0EI6TLL7SR_gYbC_2DLE-XiOe2s1osleIFz_q-c_7troakTcaKPW37l4CReu9ZJVkY0rpxPsZdxQRKCGnsvExpmoGTAi0P8_lFxLKgy1S5Bv9-3SniInn1W_l-6C7AfGrjj4cWqvjglmcTi1j-9XyXTZto83wwCn9tNIqHPK4PxDPT8eVa3I9PatVMjldLcSEobMoAmYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JePDge7s-o-mcXchTrEiygSv-B8m6iZB94yNmz4g8hyVC47mxMS8n2kID8qVAkifBIbPl1Ma5GVTcUxE2xL1cv_g4ivHY-NkHnQ42D_Ltsp7-13fs15v9SndndomwUwuGoM3KOIGx9186G02vsSCzNW_aCYOcY9xHfbB89hitJcjGaba1wmqobZEJav_ubkDB-1GScomY7POqB6g9z0s1kIXErXnYBemzn10ID0EGTQrGNYe4XkzQimzbQeB0Fm4EdvJaaCqeLAR89trZmpKKmLKsbSh1HIG54VlSxhLSwK1Ahpwf6JevBOj2wa2-jZwfe7MnZdHFA4WC-b-BVTX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TG9QGjNfWotqCMatC1jdRxR7ETFc7wAO-SCcoPgPZYUmug_sZWy81SealOkzSrEev1NsukpB1AaQa4rhX-6g73yCYsfw5flP7_Z3n4pKK2t9CQxxYeoE4aCJ0UUKpsPa2yOUGwUJp8nGEd9c9l6TMY_LZy-oVtZqFsGBiD3Mn9jUqaw3x6jQCoLkzZY2yTH8jZgapXT12yEsdf-qf9Bd68A54-3DPso_PeKBtouvdLKW7pW1DgMG9UTDaGM3t3BVWciYi22u5jkU31bl4_eiYm2npoTyx3tF3OPz7GNjZrkQ5ByVCNIDm2wHLsZCV7Ec2ZSL91Y5YIVSWDTIoQFRmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منبع بی نظیر بازی های PSP
@Ppssppiso2025
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/archivetell/5862" target="_blank">📅 09:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GjSN8utlqmx3jg1MtNmq6MMOdZPU5_i77bJ18VWulrEEtlmBjWCgQrJyWibUUkxHFLA54ru9-1I-kI71YK1AqK_GKF9Db-CMOUl-57BASzGkVpi6p6WTxgXMCV7v33arMjeMXUbj5_LBeR2HiUYoZDcVHj0_yXwnd5PRIRhae-L7oWgj3D6CVlgtXBwK7gSEQEDvVbkBG9TfduY_6IEN3yNcj8Gvxl_mI8XC4XjgmuyWc4VI4cd0e8VyWazXUvJCiKMAUCzayFPwQ9CUdL6K_s6TF1sWPj55QAWbR6OslB6zb15XFnb3d8L6Ozvfnr6q4bhmXepp-mq6XTCayXflaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QnLM1fwhxvxHww-UZE8R6iDJIYTf93H7Tt_4htS_Wwz3U1InpiWov4lsSB2HZJV3AVG2TAMPJtkslMME9RcH9oL4Ehk2eGuy-Niwxo2Fp7xdKjcmUSkq7L5LO_faxgpFBCXlbcDKNqCkem2N1w7-daiiNPy7qXhwuo08h7pqq87Knp9sk-LYKP5dqCJDYwo_by8_1AqKpEan56_YPJqSJxgTL_1FB47BHe4pM907C_Swmu0b5amxmVoGmvIv6aca-zSwoc6fkhCx2JEMC-3wAPu9LWtZNG_gbc1m9hTIh_AgoNz748jWJMbfAM2JFcCL7bsGk6Ero36kgjn8f5KUDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
اکنون می‌توان PSP را مستقیماً در مرورگر اجرا کرد — یک علاقه‌مند نسخه وب شبیه‌ساز افسانه‌ای PPSSPP را منتشر کرده است.
🕤
همه چیز بسیار ساده کار می‌کند: سایت را باز می‌کنیم، فایل ISO بازی را بارگذاری می‌کنیم و در عرض چند ثانیه بازی را بدون نصب نرم‌افزار جداگانه اجرا می‌کنیم.
🕤
رابط کاربری تقریباً کاملاً مشابه PPSSPP معمولی است، پشتیبانی از گیم‌پدها و بارگذاری بازی‌ها مستقیماً از دستگاه وجود دارد.
🕤
God of War، Tekken 6، GTA: Vice City Stories و دیگر بازی‌های محبوب به راحتی روی کامپیوتر، تبلت و گوشی‌های هوشمند اجرا می‌شوند
https://root-hunter.github.io/ppsspp-web/
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/archivetell/5860" target="_blank">📅 08:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اپن سورسه پروژه
البته باید کدش بررسی بشه
ولی شدیدا روونه
و کلا انگار ی اپ دیگه اس
😂
خیلی خوشگله
در کل جای کار داره و ابتدای کارشه پروژه ولی خیلی باحاله
اپشنای خوبیم داره بررسی کنین</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/5859" target="_blank">📅 03:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMonoGram</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">monogram-arm64-v8a-0.1.0-release.apk</div>
  <div class="tg-doc-extra">49.1 MB</div>
</div>
<a href="https://t.me/archivetell/5855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/5855" target="_blank">📅 03:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6jOcwIN4YR16Kye10ihGho2BDVMa1K08sQkZIOhCj6ujeoqU9eZSMMQm8CaOFRHTHGvKLR9POvoJ1KHfw_k2_L_Nc0Vk2b8nuf2qxnVbsRPcOfaFhMdYuFDwzsKHBlnyEuXn9xHqJ2SjsMeAfAj7uw6PIBiqnMk_fdDsLpXaTubmZ4pmHBCf24AxhazecUhA_xurZxP3nyUz4MDxsrAcXxHf_K0jS_tLsqAn9SyOD1nhRdYy-IrIRKTaPBwhS_gT0bdOKDo1RqNoly50PWnP4yQwMCllMv-ySuvFm6RzJDoRhy0_YlOmIfTST31SAbxqCo0Ithwqc3gLFVuQvl1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛠️
MonoGram؛ یک کلاینت متن‌باز و مستقل برای تلگرام
MonoGram یک اپلیکیشن غیررسمی تلگرام برای اندروید است که برخلاف بسیاری از کلاینت‌ها، از صفر و بر پایه TDLib توسعه داده شده و فورک نسخه رسمی نیست.
✨
ویژگی‌ها:
• رابط کاربری مدرن با Material 3
• عملکرد سریع و روان
• قفل بیومتریک و ذخیره‌سازی امن
• پشتیبانی از جستجوی داخل چت
• مدیریت بهتر فایل‌ها، رسانه‌ها و استیکرها
• متن‌باز و قابل بررسی توسط همه
📌
توسعه‌دهندگان اعلام کرده‌اند که MonoGram روی تجربه پیام‌رسانی، طراحی مدرن و عملکرد بهینه تمرکز دارد و قابلیت‌های NFT و کریپتویی تلگرام را اضافه نخواهد کرد.
این پروژه هنوز در حال توسعه فعال است، اما با انتشار نسخه 0.1.0 امکانات و پایداری آن نسبت به قبل به‌طور محسوسی بهتر شده است.
🔗
GitHub:
https://github.com/monogram-android/monogram
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/archivetell/5854" target="_blank">📅 03:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">100GB
⚡
vless://29f8120c-fa78-4b20-b5a5-5390d9cfbbc9@greblox.forum:443?mode=gun&security=reality&encryption=none&authority=greblox.forum&pbk=Tb21e9Z3rtr5NoprXQQtcqLLRZOgIVyIbuZmqPJkGXM&fp=firefox&type=grpc&serviceName=grpc&sni=greblox.forum&sid=a28e08feb9324fb0#%F0%9F%87%B3%F0%9F%87%B1%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/5853" target="_blank">📅 03:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇫🇷
ss://YWVzLTI1Ni1nY206ZjRlN2NjM2ItMWZkZS00ODYxLTlhN2UtMjk0NzI4ZDhhMTZh@51.195.235.71:2083#%F0%9F%87%AB%F0%9F%87%B7%20%40ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/5852" target="_blank">📅 03:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚡️
چینی‌ها از Qwen3.7-Plus رونمایی کردند؛ یک مدل چندوجهی و Agent محور جدید!
🤖
شرکت Alibaba مدل جدید
Qwen3.7-Plus
را معرفی کرده؛ یک مدل چندوجهی (Multimodal) که بینایی و زبان را در یک معماری واحد ترکیب می‌کند و برای اجرای وظایف پیچیده طراحی شده است.
🔥
قابلیت‌های کلیدی:
🔹
فعالیت به‌عنوان یک Agent کامل در محیط‌های GUI و CLI
🔹
تحلیل همزمان تصاویر و متن
🔹
کمک به برنامه‌نویسی و انجام وظایف بهره‌وری
🔹
پشتیبانی از ورودی‌های چندفرمتی
🔹
درک تصاویر، استدلال روی آن‌ها و ارجاع پاسخ‌ها به اشیای مشخص
🔹
استفاده از جستجو برای افزایش دقت پاسخ‌ها
🔹
سازگاری با فریمورک‌های مختلف Agent
💡
به زبان ساده، Qwen3.7-Plus فقط یک چت‌بات نیست؛ بلکه یک Agent چندرسانه‌ای است که می‌تواند تصویر ببیند، متن تحلیل کند، کد بنویسد و در محیط‌های مختلف عملیاتی شود.
📌
این مدل از طریق API در Alibaba Cloud Model Studio در دسترس قرار گرفته است.
🔗
وبلاگ معرفی:
https://qwen.ai/blog?id=qwen3.7-plus
🔗
نسخه آزمایشی:
https://chat.qwen.ai/?models=qwen3.7-plus
🔗
مستندات API:
https://modelstudio.console.alibabacloud.com/
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5851" target="_blank">📅 00:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5850">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ji_4eY6Lps-Fr7v0jWCeX4H9OMSQEB3Ymtvv2YAJHhZH0YXK2RF6EkDzANIkp1mJGuP-70gc3GMTCVqVQNx6cfks3pqeeFID3HVZACHgcpCfJXQrnVUPM5YT2i4qzHcb-KXcPP-MM8wa8Q5k4e0pjhzbZMv2gQgrQEdN2JVbMTClEfjbKmFFSkeuaSoaorwQLy8MY1Law3KSLfs5hl0C3LSwjQR4uoPEy8GvieLt3qCRLtbXGfTDAGI6oyCQcv1L1mY_XDbnxFf8JT1VbqIfnuIBtdQWQscccz8Xe2WXJ1zDCAaM8BFSjRWfgThY0-bEh8rcBLs2Bw4ukLMOYBYlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Golazo پخش زنده متنی فوتبال
⚽️
فوتبال را مستقیماً از طریق ترمینال تماشا کنید
https://github.com/0xjuanma/golazo
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/5850" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترجمه پیام Void Verge: از زمانی که اینترنت ایران توسط دولت بازگشایی شد، تغییرات گسترده‌ای در سراسر شبکه داخلی کشور در حال رخ دادن است. پس از هفته‌ها قطعی، تقریباً تمام روش‌هایی که در آن دوره استفاده می‌شد، مستندسازی شده و به مقامات تحویل داده شده است. سیستم فیلترینگ در حال آماده‌سازی برای مرحله بعدی قطعی‌هاست. روش‌هایی مانند DNS tunneling، MITM و Domain Fronting قطعاً در قطعی‌های آینده دیگر کار نخواهند کرد.
علاوه بر این، مقامات فیلترینگ گام‌های مهمی برای ایجاد ارائه‌دهندگان واسط برداشته‌اند که خدمات خارجی را با محدودیت‌های شدید به ایرانیان ارائه می‌دهند، یا وب‌سایت‌های ضروری را که نمی‌توانند از روش‌های قبلی استفاده کنند، NAT می‌کنند.
در این شرایط، انتشار علنی و عمومی روش‌ها هیچ فایده‌ای ندارد جز اینکه کار مقامات فیلترینگ را آسان‌تر کند. این مکانیزم باید زیر رادار عمل کند — به صورت سورس‌بسته و بی‌صدا.
در عین حال، مافیای اینترنت ایران قدرت بیشتری پیدا کرده است — مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، ISPها و دیتاسنترهایی که فروش اینترنت نامحدود به فروشندگان VPN را با قیمت صدها میلیون تومان از طریق مکانیزم‌هایی مانند سرویس‌های پروکسی و سرورهای اختصاصی با قابلیت NAT آغاز کرده‌اند.
این مافیا چنان قدرتمند شده است که موفق شده شورای عالی فضای مجازی ایران را به سمت محدودتر نگه داشتن اینترنت سوق دهد تا سود خود را به حداکثر برساند، آن هم علیرغم شرایط بحرانی و جنگی هفته‌های گذشته.
ارائه‌دهندگان ساده میزبانی وب در ایران، تنها پس از دو ماه قطعی، به فروشندگان میلیونر VPN تبدیل شده‌اند.
ما در هفته‌های آینده به جمع‌آوری و انتشار داده‌های لازم ادامه خواهیم داد. اگر این وضعیت ادامه یابد، هدف بعدی ما باید مافیای اینترنت در ایران باشد.
امیدواریم این روزهای سخت برای همه ایرانیان بگذرد. دردی که دشمنان داخلی و دزدانی که به بهانه جنگ مردم را غارت می‌کنند ایجاد می‌کنند، به مراتب بدتر از خود جنگ است!
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/archivetell/5849" target="_blank">📅 23:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">SNI Spoofing
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.18.35.46
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
replit.com
"
}
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
45.85.118.176
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
shad.ir
"
}
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5848" target="_blank">📅 22:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚀
آموزش راه‌اندازی VLESS WS با دامنه اختصاصی ابر آروان (روش True CDN Proxy)
این روش آی‌پی سرور خارج شما را کاملاً مخفی می‌کند و با عبور دادن ترافیک از سرورهای داخلی، سیستم فیلترینگ (DPI) را به طور کامل فریب می‌دهد.
پیش‌نیازها
:
* یک سرور مجازی (VPS) خارج و پنل 3x-ui نصب شده.
* یک دامنه بین‌المللی برای سرور اصلی (استفاده از پسوندهایی مثل .shop به جای دامنه‌های ملی، امنیت شبکه شما را بالا می‌برد).
* یک دامنه ارزان .ir برای ثبت در شبکه ابر آروان (به‌عنوان ماسک).
🛠
مرحله ۱: تنظیمات DNS در ابر آروان
1. دامنه .ir خود را در پنل ابر آروان ثبت و تایید کنید.
2. به بخش
رکوردهای DNS
بروید و یک
رکورد A
جدید بسازید.
3. در بخش مقدار (Value)،
آی‌پی سرور خارج
خود را وارد کنید.
4. حتماً نماد
ابر را روشن کنید
(پروکسی شبکه فعال باشد).
⚙️
مرحله ۲: تنظیمات پنل 3x-ui
1. وارد پنل شوید و از بخش Inbounds یک کانفیگ جدید با پروتکل
VLESS
بسازید.
2. پورت را روی یکی از پورت‌های امن و مجاز آروان (مثل
443
یا
8443
) قرار دهید.
3. در تنظیمات Transport، بخش شبکه (Network) را روی
ws (وب‌سوکت)
بگذارید.
4. مسیر (Path) را روی یک عبارت دلخواه تنظیم کنید (مثلاً /secure-tunnel).
5. در فیلد
Host
، نام دامنه .ir خود را که در آروان ثبت کرده‌اید بنویسید و تنظیمات را ذخیره کنید.
📲
مرحله ۳: ویرایش نهایی برای کلاینت (v2rayNG/v2rayN)
1. لینک کانفیگ ساخته شده را از پنل کپی کرده و در کلاینت خود ایمپورت کنید.
2. به بخش ویرایش کانفیگ (Edit) بروید.
3. قسمت
Address (آدرس سرور)
را پاک کرده و
دامنه .ir آروان
خود را جایگزین آن کنید.
4. بررسی کنید که فیلدهای
SNI
و
Host
(یا Peer) نیز دقیقاً همان دامنه .ir باشند. ذخیره کنید و وصل شوید!
💡
چرا این روش عالی و بدون قطعی است؟
در این معماری، کلاینت شما مستقیماً به آی‌پی‌های تایید شده داخلی ابر آروان متصل می‌شود. فایروال محلی فقط یک اتصال امن و داخلی را می‌بیند و ترافیک را مسدود نمی‌کند. سپس خود زیرساخت آروان در نقش یک تونل معکوس، ترافیک شما را به‌صورت کاملاً مخفیانه به سرور خارج منتقل می‌کند! آی‌پی سرور اصلی شما هرگز لو نمی‌رود.
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/archivetell/5847" target="_blank">📅 22:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترمینال برنامه‌نویسی هوش مصنوعی با عملکرد بالا
🔥
یک ترمینال کدنویسی بومی هوش مصنوعی مبتنی بر Rust که از همکاری چند عامل هوشمند، رابط کاربری TUI و محیط ایزوله امن پشتیبانی می‌کند و مخصوص توسعه سریع طراحی شده است.
https://github.com/Agions/synerix
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5845" target="_blank">📅 20:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgfmDuELfxJTt67iPlQuvGRkThmEgZmiKZcf_xDut-GWXPXE72fD6hg9VPX1eIv12Uy0cogUcwOJO2ynl3D1V-WZuUzI3YiOlPBxYfBQAmG9Fe5dJWzwzCh1iMbeLp4q8BwCnER_vC0D7XN-hzHrpdVh6FVQZ_HZCcj3K_ksVy8qLPvXIYp4ql4Tc-3E-EocHW_-tlJLv65JyAw4xq4Rm2F2SbdhZFjhPA_yMAXfaSxt_0oUIESGQIYtBZZ420C3d_nW-agW0QyRkGbpVq-GwYu84DF4D0WALtwI4wUR70AaoINiawhzbxGs2L1Lo1nAxwJRbnCkP2QQeewapcKtkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
TON رسماً به Gram تغییر نام می‌دهد!
🪙
پاول دوروف اعلام کرد که ارز داخلی اکوسیستم TON از این پس با نام Gram شناخته خواهد شد. این نام در واقع همان نامی است که در اولین وایت‌پیپر پروژه تلگرام استفاده شده بود.
🔹
فرآیند ری‌برندینگ حدود ۳ هفته زمان خواهد برد.
🔹
شبکه بلاکچینی همچنان با نام TON به فعالیت خود ادامه می‌دهد.
🔹
Gram به عنوان نام توکن و ارز اصلی اکوسیستم شناخته خواهد شد.
این اقدام چهارمین مرحله از برنامه ۷ مرحله‌ای «Make TON Great Again» است که دوروف برای بازگرداندن هویت اولیه پروژه TON معرفی کرده است.
📌
خلاصه:
✅
TON = نام شبکه
✅
Gram = نام جدید ارز اکوسیستم
✅
زمان تکمیل تغییرات: حدود ۳ هفته
🪙
به نظر می‌رسد نام تاریخی Gram پس از سال‌ها دوباره به اکوسیستم تلگرام بازگشته است.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/archivetell/5844" target="_blank">📅 19:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1m7mzlcLeDNC5VJWgzbVREHzi37uu2MPDEb4ggS6qVSxJmcETN4NGJzShMUXofI2ECbnu31o7-qRauQyCZzU36IIiDw10dfCAeX8uoNOp8o1LMGbEIFO4wa6oMbfwIq59RxKzLH4b-1jAR2M4-aR2NyL1Ru1qICY5hV3Mp8oWQ7YkGD4L18rfPz7CopF0kRVCGrHk3WV_R5BYFDK0nc5ET536vxHZGnxUDEB0VyHtWrgkrklMnNWU8Vr5r1LyrvJ-RrelwHXGyrbIr_Sy1nsur9SnXADrvWAoNmL8QolWMOEnQkbbxSlQ93bfJOeuAfXs0UNWTtPkcwfRDCOWJy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!  اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت [نام شهر شما] را در پرامپت زیر با…</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5843" target="_blank">📅 18:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚡️
پوسترهای فوق‌العاده حرفه‌ای از شهر خودتان با هوش مصنوعی!
اگر دوست دارید در چند ثانیه یک پوستر سه‌بعدی و لوکس از شهر خودتان بسازید، این پرامپت فوق‌العاده را امتحان کنید.
🛠
مراحل استفاده:
🔹
وارد GPT Image شوید.
🔹
عبارت
[نام شهر شما]
را در پرامپت زیر با نام شهر دلخواهتان جایگزین کنید.
🔹
پرامپت را ارسال کنید و منتظر نتیجه بمانید.
🎨
خروجی چه شکلی خواهد بود؟
• پوستر گردشگری سه‌بعدی و ایزومتریک
• نمایش معروف‌ترین جاذبه‌ها و نمادهای شهر
• معماری مینیاتوری بسیار واقع‌گرایانه
• افکت‌های سینمایی و نورپردازی حرفه‌ای
• دریا، ساحل، پل‌ها، جزایر و مناظر شاخص (در صورت وجود)
• تایپوگرافی اختصاصی با نام شهر
• مناسب برای پروفایل، چاپ، پوستر یا شبکه‌های اجتماعی
💡
نکته جذاب اینجاست که مدل به‌صورت خودکار مشهورترین بناها، خیابان‌ها، سواحل و نمادهای شهر را تشخیص می‌دهد و آن‌ها را در قالب یک دیورامای شناور و لوکس ترکیب می‌کند.
Create a premium stylized 3D isometric travel poster of [شهر] designed as a floating miniature world placed on top of a large ticket, postcard, or stamp platform with perforated edges. Automatically include the most iconic coastal landmarks, skyline, architecture, cliffs, islands, harbors, bridges, beaches, or sea views associated with the location. Arrange everything in a compact cinematic composition with realistic geography and recognizable visual identity. Style the scene as: - ultra detailed 3D diorama - photorealistic miniature architecture - cinematic travel advertisement - luxury tourism aesthetic - highly immersive but minimal - clean and elegant composition - realistic textures and reflections - soft atmospheric haze - subtle depth of field - premium Instagram-worthy artwork Environment details: - beautiful coastline and ocean integrated into composition - tiny boats, ferries, or sailboats in water - curved shorelines and waterfront promenades - lush greenery or terrain matching the destination - floating soft volumetric clouds around the city - warm cinematic sunlight - subtle shadows and reflections Add tiny realistic miniature people naturally placed near landmarks or waterfronts: - tourists taking photos - couples walking - tiny silhouettes for scale only - avoid crowds or clutter Typography: On the blank white ticket/poster area, automatically add: - the destination name in large bold elegant typography - a short poetic luxury-travel-style tagline matching the location Typography style: - modern sans-serif - premium travel poster design - minimal and elegant - subtle shadows and clean spacing Background: - smooth vibrant gradient background - color palette should naturally match the destination - minimal distractions - lots of negative space around the floating platform Composition: - floating centered platform - isometric perspective - balanced proportions between sea, architecture, and typography - destination should feel suspended in air - cinematic framing - visually clean and uncluttered Aspect ratio 1:1 Extremely detailed, cinematic, modern, premium, luxurious, artistic, visually striking, travel-poster aesthetic.
🔥
نتیجه نهایی معمولاً شبیه پوسترهای تبلیغاتی حرفه‌ای گردشگری و کارت‌پستال‌های لوکس خواهد بود.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/5842" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پروکسی متصل سامانتل و مخابرات تست شده
https://t.me/proxy?server=87.248.129.52&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5841" target="_blank">📅 18:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">trojan://humanity@198.62.62.23:443?host=www.calmlunch.com&path=%2Fassignment&sni=www.calmlunch.com&type=ws#@ArchiveTell
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/5840" target="_blank">📅 18:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک استارتاپ هوش مصنوعی چینی یک مدل ۱ تریلیون پارامتری ارائه کرد - کاملاً رایگان و متن‌باز.
👀
نام آن Kimi K2.6 است - ۱۲ روز پیش توسط Moonshot AI منتشر شد و در حال حاضر توجه‌ها را به خود جلب کرده است.
اعداد و ارقام باورنکردنی هستند. ۱ تریلیون پارامتر. فقط ۳۲ میلیارد پارامتر در هر درخواست فعال می‌شود - به این معنی که با وجود حجم عظیمش، به طور کارآمد اجرا می‌شود. پنجره زمینه ۲۵۶ هزارتایی. کل پایگاه‌های کد، اسناد حقوقی و مقالات تحقیقاتی را در یک مرحله مدیریت می‌کند.
اما چیزی که آن را واقعاً خاص می‌کند این است - Cursor، یکی از پرکاربردترین ابزارهای کدنویسی هوش مصنوعی در جهان، مدل Composer 2 خود را مستقیماً بر روی Kimi ساخته است. این اعتبارسنجی نهایی است.
این مدل کدنویسی، استدلال، ساخت وب‌سایت، ایجاد اسلاید، تجزیه و تحلیل داده‌ها و اجرای وظایف چند مرحله‌ای مستقل را انجام می‌دهد - همه در یک فضای کاری تمیز.
و برخلاف GPT یا Claude - کاملاً متن‌باز است. استفاده، اجرا و توسعه رایگان است.
🔗
https://kimi.com
👑
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5839" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMypnebZUIGj_1MDBC0aDlngVVqo9NJPqT9QoEOH2kTxG-81FjE0eT9jHITGbeuFV-yTY9soOdQ8NvTYwdIM_ZRX5mDR30lghU0e4nj-JkEkUOPffS2YKrrQ2J5NByIhqL0v-ULaJhEWdA_Ewp4tSXkohe74dtdNaWy1onecuCObhEJ-sb57hLKb0d3Ddg8HaR9O6OYJzYb46sggZn8KfnUza8bkJiIeIa0lReDW2uU658AI6lft2BSQjExjPrD7G7n7SP01kE75zSt059fymPQeDgSkPcDaAznTACirAU_fdPgkC0iGslYN3TLt8aKoh7f-WItXcRk3XlzIYSMZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گوشی اندرویدی را به یک میکروفون حرفه‌ای تبدیل کنید!
📌
پروژه MicYou به شما اجازه می‌دهد از گوشی اندروید به‌عنوان میکروفون برای کامپیوتر استفاده کنید.
📶
اتصال از طریق Wi-Fi
🔌
پشتیبانی از USB
🔊
حذف نویز و کاهش اکو
🎚
کنترل خودکار حجم صدا (AGC)
💻
سازگار با ویندوز، لینوکس و macOS
⚡
راه‌اندازی سریع با پشتیبانی از Virtual Audio Device
💡
گزینه‌ای کاربردی برای جلسات آنلاین، استریم، ضبط پادکست یا زمانی که میکروفون مناسبی در اختیار ندارید.
📥
لینک پروژه:
github.com/LanRhyme/MicYou
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5838" target="_blank">📅 15:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎁
دسترسی آزمایشی به Claude، GPT و Gemini در یک پنل!
📌
سرویس Bind چندین مدل هوش مصنوعی را در یک داشبورد واحد ارائه می‌کند و برای کاربران جدید دوره آزمایشی دارد.
🤖
Claude Sonnet
🧠
GPT
✨
Gemini
🔄
جابه‌جایی سریع بین مدل‌ها
📋
مدیریت همه چت‌ها در یک محیط
🛠
شروع کار:
🔹
وارد سایت Bind شوید.
🔹
یک حساب کاربری ایجاد کنید.
🔹
گزینه Free Trial را فعال کنید.
🔹
در صورت نیاز، پلن‌های آزمایشی و امکانات تیمی را از داخل پنل بررسی کنید.
💡
اگر می‌خواهید چند مدل مطرح AI را در یک محیط تست کنید، Bind می‌تواند گزینه جالبی باشد.
🌐
app.getbind.co
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/5837" target="_blank">📅 14:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArchiveTel(𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣⚡️)</strong></div>
<div class="tg-text">رفقا سلام!
✋
در این پست آموزش جامع راه‌اندازی اسکریپت بی‌نظیر CFnew (نسخه 2.9.8) رو براتون آماده کردیم. در این آپدیت، تمام باگ‌های یک ماه گذشته برطرف شده. این ابزار روی کلادفلر (Workers و Pages) اجرا میشه و یکی از کامل‌ترین پروژه‌هاست.
🔥
ویژگی‌های اصلی CFnew:
* پشتیبانی همزمان از پروتکل‌های VLESS، Trojan و xhttp.
* پنل گرافیکی قدرتمند: مدیریت کانفیگ‌ها تحت وب با دیتابیس KV (اعمال تغییرات در لحظه بدون نیاز به دیپلوی مجدد).
* Sub-converter داخلی: تولید کانفیگ کلاینت‌ها (Clash, Sing-box, V2rayNG و...) بدون نیاز به سرویس خارجی.
* پشتیبانی از ECH: دور زدن محدودیت‌های پیشرفته.
* تست پینگ داخلی: تست و انتخاب خودکار بهترین آی‌پی‌ها.
* پشتیبانی از رابط کاربری فارسی.
🛠
پیش‌نیازها:
یک اکانت کلادفلر + ساخت یک UUID معتبر از سایت
https://www.uuidgenerator.net
(این UUID رمز ورود شما به پنل خواهد بود).
💻
نصب روی Cloudflare Workers:
1. ساخت KV: در کلادفلر، از Storage ➔ KV یک Namespace جدید بسازید.
2. ایجاد Worker: در Workers & Pages یک ورکر جدید بسازید، کدهای قبلی را پاک و سورس CFnew را از گیت‌هاب پیست کنید (Deploy بزنید).
3. تنظیم متغیرها: در Settings ➔ Variables، متغیری با نام U (حرف بزرگ) بسازید و مقدارش را UUID خود قرار دهید.
4. اتصال KV: در Settings ➔ KV Bindings، دیتابیسی که ساختید را با نام C (حرف بزرگ) متصل (Bind) کنید.
5. تاریخ سازگاری: در Settings ➔ Runtime، گزینه Compatibility Date را روی 2026-01-20 تنظیم و ذخیره کنید.
6. اتصال دامنه: در Triggers ➔ Custom Domains، دامنه خود را متصل کنید.
🌐
نصب روی Cloudflare Pages:
1. آپلود فایل‌ها: در Workers & Pages یک Pages ایجاد کنید. با گزینه Direct Upload، فایل Zip پروژه را آپلود کنید.
2. تنظیمات: مشابه روش قبل، در Settings متغیر U (برای UUID) را ساخته و KV Bindings را با نام C متصل کنید.
3. تاریخ سازگاری: در Settings ➔ Runtime، تاریخ را روی 2026-01-20 تنظیم کنید.
4. دیپلوی مجدد (حیاتی): چون متغیرها فوراً اعمال نمیشن، به تب Deployments رفته، Create deployment را بزنید و همان فایل Zip را دوباره آپلود کنید تا پروژه از نو ساخته شود.
🔓
نحوه دسترسی به پنل مدیریت:
مرورگر را باز کرده و آدرس دامنه خود را به همراه UUID وارد کنید (مثال:
yourdomain.com/UUID
). در این پنل گرافیکی و فارسی، می‌توانید لینک‌های اتصال (Subs) بگیرید، ECH را مدیریت کنید و آی‌پی‌های تمیز وارد کنید.
🔄
نحوه آپدیت برای نسخه‌های بعدی:
* اگر از Worker استفاده می‌کنید: کدهای جدید را کپی، جایگزین کدهای قبلی کرده و Deploy کنید.
* اگر از Pages استفاده می‌کنید: در تب Deployments فایل Zip جدید را آپلود کنید (بدون نیاز به تنظیم مجدد).
📥
سورس کد و دانلود زیپ:
https://github.com/byJoey/cfnew
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/archivetell/5836" target="_blank">📅 14:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آیپی تمیز کلودفلر مخابرات و ایرانسل تست شده
45.130.125.96
27.50.48.49
208.103.161.170
45.130.125.0
45.130.125.160
45.130.125.69
66.81.247.155
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5835" target="_blank">📅 14:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۵ گیگ کانفیگ از پشت cdn رد شده همراهم میاره
vless://6053415d-763c-4132-9445-e4a0329a594b@snapp.ir:80?encryption=none&host=netrox.cnxman.ir&path=%2F&security=none&type=ws#netrox%20--cdn%20-%20tunnel
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/archivetell/5834" target="_blank">📅 14:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">۱۰ گیگ کانفیگ تانل
🔥
vless://a5400c9e-2f0f-41c9-aa4d-5a77c0787af3@cnxman.ir:17544?security=none&encryption=none&headerType=none&type=tcp#tunnel
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5833" target="_blank">📅 14:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5832">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">1 ترابایت اهدایی از یکی از ممبر های عزیز
❤️
vless://ZoRoVpn@104.253.18.220:80?security=reality&encryption=none&pbk=D4tCeuAMOZViac1SOVD5ABdN86EkAn9ql3NEuQlneXQ&headerType=none&fp=chrome&spx=%2F1vwstnEi2HFdu63&type=tcp&sni=www.yahoo.com&sid=88ab02c0#1.00TB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5832" target="_blank">📅 13:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWT2wxNGW-IeFLZQMTTVJzwTTama6KjPjnw6_hHDGEq9iGdACVAG1s1_FcnNniS-WWMBQ7goKPHmrUgBLedrQgrjfJoJl8el8Bi-uBGvahDAxy_PGwS4hj2rehmDxGYo6TIF2cjAn-LxBagotYsBpTmmeLUVdos3XuyPLoY3lHQkb6WLFiviieD2xzjir08GFYz6Mk_YsVkbwQ8USHkiyMcdnXkTE2Y4eEt3zFJ05ptN_MTqxprw5tgOUnU09HIhxtIKL-EROjKGKAhfPiJBARmtvD1CkzciJ8v-LVtt_uD6khKizBqLIpmitzy7T7ZBE6A0WjVFdxUKkt9nJJiLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://3e809b21-e29b-49ec-a7fb-5301ec7c1cee@food.artmisserver.site:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#Artmis
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/archivetell/5830" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5jrnYqWv_m30uETCEsYqEQghFJLRjjmIH6__rca9oIpt2k6Z2z-fFroVeH4sAoN1hVth6pYbRCB2qPP_0agRgUmM_-KmsRZEDR3EfKKdkgvuntV_S70dm1WnLBKoTdPTTnvwU7_VeHiPx6QgqOcRcJN9AeVzZKFds20W0fcn4BgpfN8jQC7-59cJbyGO8ivi-tTCPSSKkHnUk4reHlZijLBYrzkHE_jlK1UAwrRv_4FmfkGekdee1gV7A7UiYD9_TPEZTB6w-Zw6TihL03ckxhvRsjSsQZIVUodSq_jxGobxoaDfCrAG_U-Otaiy6sGcnGgbmghsNsNn7o3iT3FUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📝
تبدیل خودکار هر صدا به متن و خلاصه!
📌
ابزار DeLive صدای در حال پخش روی سیستم را به‌صورت لحظه‌ای دریافت می‌کند و از آن زیرنویس، متن و یادداشت تولید می‌کند.
🎙
تبدیل گفتار به متن در لحظه
💬
نمایش زیرنویس روی صفحه
🌍
پشتیبانی همزمان از دو زبان
👥
تشخیص گوینده‌های مختلف
📋
تولید خلاصه و گزارش از محتوا
❓
امکان پرسش از محتوای ضبط‌شده
💡
مناسب برای کلاس‌های آنلاین، ویدیوهای آموزشی، پادکست‌ها، استریم‌ها و جلسات کاری؛ بدون نیاز به یادداشت‌برداری دستی.
💻
پشتیبانی از ویندوز، لینوکس و macOS
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️
https://github.com/XimilalaXiang/DeLive</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/archivetell/5828" target="_blank">📅 12:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">0BITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/5827" target="_blank">📅 12:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://9e48e5db-e5cb-462f-ab0b-6f573aa73728@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=941935f2d0e82539&sni=www.amazon.com&type=tcp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/5826" target="_blank">📅 12:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🕵️‍♂️
مرورگر شما چه اطلاعاتی را روی سیستم ذخیره می‌کند؟
📌
یک راهنمای فورنزیک نشان می‌دهد که در مرورگرهای Chrome، Firefox و Edge تقریباً همه ردپاهای کاربر روی سیستم ذخیره می‌شوند.
🔖
بوکمارک‌ها و سایت‌های ذخیره‌شده
🌐
تاریخچه مرور و جستجوها
🔑
رمزهای عبور و لاگین‌ها
🍪
کوکی‌ها و اطلاعات نشست‌ها
📂
فایل‌های دانلودشده
🧩
افزونه‌ها و تنظیمات مرورگر
🖼
تصاویر کش و فاوآیکون سایت‌ها
🛠
همچنین ابزارهایی مثل Hindsight، DB Browser for SQLite و LaZagne برای بررسی و استخراج این داده‌ها وجود دارد.
💡
اگر کسی به سیستم شما دسترسی پیدا کند، بخش زیادی از فعالیت‌های اینترنتی شما قابل بازیابی خواهد بود؛ حتی مواردی که مدت‌ها قبل مشاهده کرده‌اید.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5825" target="_blank">📅 11:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🤖
یک لیست طلایی از ابزارهای رایگان هوش مصنوعی!
📌
اگر از بین صدها ابزار AI نمی‌دانید کدام‌ها واقعاً ارزش استفاده دارند، این مجموعه می‌تواند نقطه شروع خوبی باشد.
🎨
تولید تصویر: Raphael AI ،Krea AI ،Magnific AI
🎬
تولید و ویرایش ویدیو: Runway ،Kling AI ،Hedra
🎙
صدا و موسیقی: ElevenLabs ،Suno
💻
برنامه‌نویسی: Cursor ،Replit
،Bolt.new
📊
تولید محتوا و ارائه: Gamma ،Napkin AI ،Notion AI
🔎
جستجو و تحقیق: Perplexity ،Phind
🤖
چت‌بات‌ها و مدل‌ها: Claude ،Poe ،Hugging Face
💡
مجموعه‌ای از ابزارهای کاربردی برای تولید محتوا، برنامه‌نویسی، طراحی، تحقیق و ساخت پروژه‌های شخصی؛ بدون نیاز به جستجوی طولانی بین صدها سرویس مختلف.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/5824" target="_blank">📅 11:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">80 گیگ کانفیگ از لوکیشن های
🇳🇱
🇫🇷
🇮🇩
🇩🇪
vless://aa918a17-0c07-49b2-aec5-b72809d91a17@185.211.101.214:38200?mode=auto&path=%2Flightyagami&security=reality&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=JL7JvLV0E3dvB48lp5UpSyzx1ATHPS3Kgjv2Ox9HtjQ&fp=chrome&spx=%2F&type=xhttp&sni=www.yahoo.com&sid=4306#OBITO
vless://c649466f-e700-4d78-be2c-a9d915434f34@82.40.62.67:80?fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22debug%22%3Afalse%2C%22disablePathMTUDiscovery%22%3Afalse%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22initStreamReceiveWindow%22%3A8388608%2C%22keepAlivePeriod%22%3A10%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIdleTimeout%22%3A30%2C%22maxIncomingStreams%22%3A1024%2C%22maxStreamReceiveWindow%22%3A8388608%7D%7D&fp=chrome&type=xhttp&sni=www.yahoo.com&sid=49a5ec2ac3&mode=stream-one&path=%2Fm4rg&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=QWHdk8IaYGGm_CkKaBTLeLlOKhFGLx2pA3qBBRmiM3Y&host=light.96s.dpdns.org&spx=%2FMwzynVriGAhj8A1#OBITO-20.00GB%F0%9F%93%8A
vless://1b16b6f8-b8dd-43d7-84f9-8eb8a7e15504@sina.35o.ir:25645?security=reality&encryption=none&pbk=GnAQ0pqW4HGqMuOY7crTmcQ56FuABKPP9YaiJzOS3X8&headerType=&fp=chrome&spx=%2F&type=tcp&sni=www.yahoo.com&sid=d6372f1a0a#OBITO
vless://0c3f5b49-d0ec-451b-bf30-f50e229b645c@panel.96s.ir:8080?fm=%7B%22quicParams%22%3A%7B%22congestion%22%3A%22bbr%22%2C%22initStreamReceiveWindow%22%3A8388608%2C%22maxStreamReceiveWindow%22%3A8388608%2C%22initConnectionReceiveWindow%22%3A20971520%2C%22maxConnectionReceiveWindow%22%3A20971520%2C%22maxIncomingStreams%22%3A1024%7D%7D&fp=chrome&type=xhttp&sni=www.yahoo.com&sid=775a6745d1&mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=0ySdtEa5hyO50lsKB3FdbcHaGCn0tw6BeYvabtJpb2s&host=panel.96s.ir&spx=%2F#%DA%A9%D9%84%D9%88%D8%AF-0BITO
@Sina_1090</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5823" target="_blank">📅 10:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حذف واترمارک ویدئو، PDF، PPTX و اینفوگرافیک‌های NotebookLM به صورت محلی در مرورگر، بدون آپلود فایل.
لینک:
https://notebooklmremover.org/
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/5822" target="_blank">📅 09:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گل سر سبد ربات های سرچ تلگرام
@oksearch
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5821" target="_blank">📅 09:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پروکسی متصل
https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5820" target="_blank">📅 09:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">OBITO.conf</div>
  <div class="tg-doc-extra">532 B</div>
</div>
<a href="https://t.me/archivetell/5819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@Sina_1090</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5819" target="_blank">📅 08:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehg1NOX7UkWwolk8WMsETkiqG0xoHd6GTFfi9wDCLuhzRrN9xrmv1GLh5tN4WXWsYmekJeWwq-stT_ltq8cbFyjiwcwHrpdPG8mmcqsTL1vMH2rv1u_QNGZF-3POvYFWJ0a675baCyOUTsAM_IVYdwlfekzlzXLfDSupuEx1u69iYuF30Shj9QyA9w7V50qGN1-kAPvr5tUjRtG4QHiASyxn7fLvYAnBqvpYMSpf2Aj-ue8a1jpgzJfRdKcCxSFcb7BlfvVd8c8w79P3PqZvOzYDij6iWEaLUQrrWSaCPCi1HO6tRHQ-ec280WnBZiKWwyO9_jDFWtwYwit8ZqQ7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی دلش وایرگارد میخواد....؟  @Sina_1090</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5818" target="_blank">📅 05:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کی دلش وایرگارد میخواد....؟
@Sina_1090</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/archivetell/5817" target="_blank">📅 05:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">vless://f6108273-3a0a-4f6c-bd82-62dc234d2945@yasin.mohraz.top:80?mode=auto&path=%2Fyasin&security=reality&encryption=none&pbk=UkHH1vDkeIQkCWeVeOAyEnYAC2yZSfq8caBjQ-H_ihQ&host=yasin.mohraz.top&fp=chrome&spx=%2FF4vpNKDpUgGorWY&type=xhttp&sni=www.yahoo.com&sid=b44e2473841b#VIP</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/archivetell/5816" target="_blank">📅 04:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
⚡️
❤️
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTo4QW5Za3J3VDByMzlIZFJ6REtDNlNPeUE@45.39.241.51:25083#%D8%A7%D9%87%D8%AF%D8%A7%DB%8C%DB%8C%2050%20%DA%AF%DB%8C%DA%AF%20%DA%A9%D8%A7%D9%86%D8%A7%D9%84%20%0A%0A@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/archivetell/5814" target="_blank">📅 00:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">۵۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز کانال
😎
❤️
vless://ead394bc-06b3-4cc0-a904-668a607aac0b@31.56.229.237:443?encryption=none&flow=xtls-rprx-vision&fp=chrome&pbk=rT-KdyGuCqbP8c-CilgD2sSWMkSSLe8xbEeRNxypsSk&security=reality&sid=57e7bd&sni=www.amazon.com&spx=%2FSBDHPWNzLaqiYei&type=tcp#3alqhl5fyg-49.38GB%F0%9F%93%8A
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/archivetell/5813" target="_blank">📅 23:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ss://YWVzLTI1Ni1nY206ZjRlN2NjM2ItMWZkZS00ODYxLTlhN2UtMjk0NzI4ZDh
ss://YWVzLTI1Ni1nY206N2UxZGQ0YzU1YmY4NWRhNQ%3D%3D@212.192.15.225:20129#%F0%9F%87%AD%F0%9F%87%B0%20%40ArchiveTell</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/archivetell/5812" target="_blank">📅 23:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:443?m
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:2082?mode=auto&path=%2FMohraz&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=D6IW407GuNM0FT8slImWUQL2ABfzYnf2pet0FdpGFwc&host=95.182.101.96&fp=chrome&spx=%2FzlropzOvVbv1I3R&type=xhttp&sni=www.yahoo.com&sid=cae7dd3426354120#MOHRAZ-yasin-20.00GB%F0%9F%93%8A
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:49612?security=reality&encryption=none&pbk=JRLAhrl2S4BFWT64IDgXHvJSozFfocZ3I0Z6yiozkWc&headerType=&fp=chrome&spx=%2FP262IStz3xi6uwS&type=tcp&sni=www.microsoft.com&sid=d0df63a4af11#MOHRAZ%20-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:2030?path=%2F&security=&encryption=none&type=httpupgrade#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:20828?security=&encryption=none&type=grpc#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:8000?path=%2F&security=&encryption=none&type=ws#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:18442?security=reality&encryption=none&pbk=Y8MrhrV6WraccHAPfCv8NNdyGsmAhmbD_9t7Blh49m4&headerType=&fp=chrome&spx=%2FeHjIIQnd5E35bJz&type=tcp&sni=www.samsung.com&sid=e478f43b0c25df12#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:38796?security=reality&encryption=none&pbk=LuelZgJCGhzxoQwgZRbxpFyza95n3jmoSt7eAgXr318&headerType=&fp=chrome&spx=%2FqdZ5PJq0TTISh4c&type=tcp&sni=www.bing.com&sid=412082ae#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:38956?security=reality&encryption=none&pbk=UMF9YjdC1voBk_82jBmWYR6ikJrruBwbtgReKatAQmo&headerType=&fp=chrome&spx=%2Fso8Gm7hC851Caio&type=tcp&sni=www.microsoft.com&sid=1f495c03ce#MOHRAZ-yasin
vless://b50688d7-d5e5-4391-9220-c3ac2558f1fe@95.182.101.96:44535?security=reality&encryption=none&pbk=-0MP4KyHJ12AZ-z1YA5ITIjMOh8FUnGzSOSu2DFSgmI&headerType=&fp=chrome&spx=%2FYTBOOoz6loWLYfx&type=tcp&sni=www.yahoo.com&sid=de50a62ae9c03b#MOHRAZ-yasin
20GB</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/archivetell/5810" target="_blank">📅 23:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromaaa</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">New Text Document.txt</div>
  <div class="tg-doc-extra">55 KB</div>
</div>
<a href="https://t.me/archivetell/5809" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/archivetell/5809" target="_blank">📅 22:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr Killer</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SNI_SPOOFINGconfig.txt</div>
  <div class="tg-doc-extra">10.8 KB</div>
</div>
<a href="https://t.me/archivetell/5808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/archivetell/5808" target="_blank">📅 22:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">rstaspoof.go</div>
  <div class="tg-doc-extra">47.7 KB</div>
</div>
<a href="https://t.me/archivetell/5806" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/archivetell/5806" target="_blank">📅 22:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️
تریاک ناب آماده شد
❤️
+sni spoof
و زنده کردن کانفیگ مرده و افزایش سرعت اینترنت رو گوشی حتی بدون روت!
توجه: این آموزش روی گوشی غیر روت  ضبط شده است!
قدم اول
برنامه ترموکس رو دانلود و نصب کنید
اینم لینک مستقیم ترموکس
حتما وی پی ان رو روشن کنید و دستور هات انجام بدین...
قدم بعدی زدن این دستورها در ترموکس....
اولین دستور:
apt update && apt upgrade -y && pkg install golang
دستور دوم:
termux-setup-storage
دستور سوم:
cd /sdcard && go run rstaspoof.go -listen :40443 -connect 104.17.121.71:443 -sni www.hcaptcha.com -method combined
و در آخر فیلتر رو خاموش و پینگ بگیرید..
دوستان اگه ای پی تمیز کلود فلر دارین می تونین با این ای پی جایگزین کنین.
گروه رفع مشکل...
@archivetell</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/archivetell/5805" target="_blank">📅 22:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🤖
ساخت اپلیکیشن بدون حتی یک خط کدنویسی!
📌
پلتفرم Anything.com به شما اجازه می‌دهد فقط با توضیح دادن ایده‌تان، اپلیکیشن یا وب‌سایت بسازید؛ بدون نیاز به دانش برنامه‌نویسی.
⚡
ساخت اپلیکیشن اندروید، iOS و وب
🎨
طراحی رابط کاربری با کمک هوش مصنوعی
🔐
راه‌اندازی خودکار…</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/archivetell/5804" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5802">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🤖
ساخت اپلیکیشن بدون حتی یک خط کدنویسی!
📌
پلتفرم
Anything.com
به شما اجازه می‌دهد فقط با توضیح دادن ایده‌تان، اپلیکیشن یا وب‌سایت بسازید؛ بدون نیاز به دانش برنامه‌نویسی.
⚡
ساخت اپلیکیشن اندروید، iOS و وب
🎨
طراحی رابط کاربری با کمک هوش مصنوعی
🔐
راه‌اندازی خودکار ورود کاربران
💳
اتصال سیستم پرداخت
🛠
رفع خودکار برخی خطاها و مشکلات
🖼
تولید تصاویر و المان‌های گرافیکی
💡
اگر ایده‌ای برای ساخت یک اپ دارید اما نمی‌خواهید درگیر کدنویسی شوید، این ابزار ارزش امتحان کردن را دارد.
🎁
در حال حاضر برای برخی کاربران اعتبار رایگان جهت شروع پروژه‌ها ارائه می‌شود.
🌐
anything.com
🔵
@ArchiveTell
|</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/archivetell/5802" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5801">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خفن ترین ربات پینترست در تلگرام
@PinterestAllBot
🔥
دانلود فوری ویدیوها و تصاویر پینترست
🔍
جستجوی مستقیم پینترست در تلگرام
👤
بررسی هر پروفایل پینترست
⚡
استفاده از جستجوی درون خطی در هر چت
👥
همچنین در گروه‌ها کار می‌کند
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/5801" target="_blank">📅 21:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۵۰۰ گیگ کانفیگ اهدایی یکی از ممبرای گل کانال
😎
vless://d02f9d1f-7e41-4e0b-8d11-439e0f719e74@95.182.85.120:80?encryption=none&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&host=ata.photodrop.ir&mode=auto&path=%2FMySecurePath123456789&security=none&type=xhttp#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5800" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اقایون گویا یه روش اومده که میتونید
Sni spoofing
روی گوشی بدون روت اجرا کنید
+آموزش رو بزارم.....؟
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/archivetell/5799" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اقایون کانفیگ sni کی داره
دارم یه چیو تست میکنم.....?
@Sina_1090</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5798" target="_blank">📅 20:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پروکسی ایرانسل ، سامانتل و مخابرات تست شده
https://t.me/proxy?server=87.248.129.51&port=15&secret=ee1603010200010001fc030386e24c3add63646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/archivetell/5797" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پروکسی مخابرات و ایرانسل
https://t.me/proxy?server=fresh.t-proxy.info.&port=25565&secret=ee104462821249bd7ac519130220c25d0963646e2e79656b74616e65742e636f6d
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/archivetell/5796" target="_blank">📅 18:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdbc4c5695.mp4?token=HGKxX-KO0F36tAvrImK-rpOd311tGLFdSLRmXlqaYr5cyvn5L1ABPdRT1vNmfKzMiUrRmwvf3d8HwwqTAg_u6wztjbm6jZtPWK1zreKNsFCYQJLxoHpuazTt6OyglAesmMLJ5Ho4XLVmxP7NFRGg3FQrkiBJNl353EBE9E-IdQNRK3VYr-aS4HW8w2Uu8rtJPVT3lDV8uxEoUpu376e1mQsy1u0JTWPk9cVIb249gze02k2CVobpkGo7nvtF3pYuu5hXz6xJrcMNrJ8o-uECDgXjUt72TM6t3pc4TzlxGbk7JNR6SyfwRJX95rhNRc0b-T-_Tus64QmIFCdXVpiU9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdbc4c5695.mp4?token=HGKxX-KO0F36tAvrImK-rpOd311tGLFdSLRmXlqaYr5cyvn5L1ABPdRT1vNmfKzMiUrRmwvf3d8HwwqTAg_u6wztjbm6jZtPWK1zreKNsFCYQJLxoHpuazTt6OyglAesmMLJ5Ho4XLVmxP7NFRGg3FQrkiBJNl353EBE9E-IdQNRK3VYr-aS4HW8w2Uu8rtJPVT3lDV8uxEoUpu376e1mQsy1u0JTWPk9cVIb249gze02k2CVobpkGo7nvtF3pYuu5hXz6xJrcMNrJ8o-uECDgXjUt72TM6t3pc4TzlxGbk7JNR6SyfwRJX95rhNRc0b-T-_Tus64QmIFCdXVpiU9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دوبله ویدیو با حفظ احساسات واقعی صدا!
📌
شرکت ElevenLabs نسخه جدید Dubbing Studio را معرفی کرده که می‌تواند ویدیوها را به بیش از ۹۰ زبان دوبله کند؛ آن هم بدون اینکه حس و لحن گوینده اصلی از بین برود.
⚡
پشتیبانی از بیش از ۹۰ زبان
🎭
حفظ احساسات، لحن و سبک صحبت
👥
تشخیص چندین گوینده در یک ویدیو
🎵
جداسازی خودکار موسیقی پس‌زمینه
🎬
هماهنگی دوبله با زمان‌بندی ویدیو
💡
اگر گوینده بخندد، هیجان‌زده شود یا آرام صحبت کند، هوش مصنوعی تلاش می‌کند همان حس را در زبان مقصد نیز بازسازی کند.
🎥
ابزار بسیار جذابی برای تولیدکنندگان محتوا، یوتیوبرها، مدرس‌ها و کسانی که مخاطب بین‌المللی دارند.
🌐
elevenlabs.io/dubbing-studio
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/archivetell/5794" target="_blank">📅 18:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">برنامه‌ریزی هوش مصنوعی برای هفته کاری ایده‌آل
reclaim.ai
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/archivetell/5793" target="_blank">📅 18:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5792">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04ea6eda3.mp4?token=WrEM-8_3KYX7thiXKd8JlxxG8x8aAN5av74DIlZTlzXq3SdYBSKuQ8hbfBr2G-48zeFnUR-YuyoMew0YnsX7UDaCx_khR0_RnVU17x0lcRvW9XEafZ8r91FnfI3yer4YukRWkpkDff1OykknUlIxLaPCSmbCE2Des9cCn9XK1mRCUlXrPeheQ6sIOWiTBO084bEAnlkhVoDGTfDY0-N6B011twsOeMGrIr4hBUjEGrMKPvNX6QBzIv7XIV3FGco2FbR1_Y1PZ17710QFnai839iKfyVUrWSbFeO1Z_E9DqZPw-e2V7e1CsCl43t17Pp3iKKso5lUUvZEQpdqvSQS7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04ea6eda3.mp4?token=WrEM-8_3KYX7thiXKd8JlxxG8x8aAN5av74DIlZTlzXq3SdYBSKuQ8hbfBr2G-48zeFnUR-YuyoMew0YnsX7UDaCx_khR0_RnVU17x0lcRvW9XEafZ8r91FnfI3yer4YukRWkpkDff1OykknUlIxLaPCSmbCE2Des9cCn9XK1mRCUlXrPeheQ6sIOWiTBO084bEAnlkhVoDGTfDY0-N6B011twsOeMGrIr4hBUjEGrMKPvNX6QBzIv7XIV3FGco2FbR1_Y1PZ17710QFnai839iKfyVUrWSbFeO1Z_E9DqZPw-e2V7e1CsCl43t17Pp3iKKso5lUUvZEQpdqvSQS7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📄
یک ابزار رایگان و متن‌باز برای ویرایش PDF!
📌
پروژه Every PDF به شما اجازه می‌دهد فایل‌های PDF را بدون نیاز به اشتراک‌های گران‌قیمت و نرم‌افزارهای سنگین ویرایش کنید.
✏️
ویرایش مستقیم متن PDF
🖼
افزودن تصویر، لوگو و واترمارک
📑
ادغام چند فایل PDF
✂️
تقسیم فایل‌های حجیم به چند بخش
💻
پشتیبانی از ویندوز و macOS
💡
اگر فقط برای چند تغییر ساده مجبور به استفاده از ابزارهای پولی می‌شوید، این پروژه متن‌باز می‌تواند جایگزین خوبی باشد.
📥
لینک پروژه:
github.com/DDULDDUCK/every-pdf
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/5792" target="_blank">📅 17:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5791">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKF-ZVHqtYrPtLAnVD0lGlfDT-yMWZ4eBCvSgmhG_nle4ATAhAso0It3P9SO3Rblie82ZTjOiRDnDWMj8_KsmVFu5wjaFzAnFDcTGFqYnTf9-NczFTlqcH5NR0ZPrRZmhWy9z_hV6UjnYcy6A0Se87TBbHYMj_yZTnJK6sYcItstpd9Bw5ylcjwUmjo7GX5EnXTVrRpIRtIn4Ye814QoimZyokoOrqA_qIZ4jkshuFi6gCVAiS0HkF-IKV-0cvTd7KIFXVpQqV6N-4AAHEKHzlLs6N7RzMJrIbrQR4Bc7fDNbwiNqsrMma67hJaQJLDwAlJ2lxl2JKIncfinU_mF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💧
دستگاهی که آب دریا را شیرین می‌کند و همزمان لیتیوم استخراج می‌کند!
📌
پژوهشگران آمریکایی فناوری جدیدی برای نمک‌زدایی آب دریا توسعه داده‌اند که بدون نیاز به برق و تنها با استفاده از نور خورشید کار می‌کند.
⚡
بدون مصرف برق
☀️
متکی به انرژی خورشیدی
🧼
قابلیت خودتمیزشوندگی
🌊
تبدیل آب شور به آب شیرین
🔋
امکان استخراج لیتیوم از نمک‌های باقی‌مانده
💡
نکته جالب اینجاست که نسخه پیشرفته‌تر این فناوری می‌تواند لیتیوم را به‌صورت انتخابی از مواد باقی‌مانده پس از نمک‌زدایی جدا کند؛ عنصری که نقش مهمی در تولید باتری‌های مدرن دارد.
🔬
اگر این فناوری به تولید انبوه برسد، می‌تواند هم به بحران کم‌آبی و هم به تأمین مواد اولیه باتری‌ها کمک کند.
🔵
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/5791" target="_blank">📅 17:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پروکسی
https://t.me/proxy?server=r33.proxytg.space&port=8443&secret=eec38451cb166b3ed3a1bbf1d4e7e382817233332e70726f787974672e7370616365&&
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/5790" target="_blank">📅 17:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiI0MTA1MjgzZi1iMDM2LTQwNDMtYTE2NS0xM2MyYjA1MTY0MDgiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgwMl9zNDk3ODM2LTIwNC44ME1C8J+TiiIsInNjeSI6ImF1dG8iLCJzbmkiOiIiLCJ0bHMiOiJub25lIiwidHlwZSI6Im5vbmUiLCJ2IjoiMiJ9
vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiJkNWZhZjU3OS04YmMyLTRlZmUtOWFlYi05YTRhOWFiM2VlYWYiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgwM19hXzIyNjYtMjA0LjgwTULwn5OKIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
vmess://eyJhZGQiOiJzbmFwcC5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoiZC5hbGlzZWN2aWNlLmlyIiwiaWQiOiI4NDJmYmM5NC1kNzMwLTQyNTAtODYyNi05MzQ1M2NjMWE1NmYiLCJuZXQiOiJ3cyIsInBhdGgiOiIvIiwicG9ydCI6IjIwODIiLCJwcyI6IjgyODYtMjA0LjgwTULwn5OKIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5789" target="_blank">📅 17:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">vmess://eyJhZGQiOiJhbnRlbi5pciIsImFpZCI6IjAiLCJhbHBuIjoiIiwiZnAiOiIiLCJob3N0IjoidDIuYWxpc2VjdmljZS5pciIsImlkIjoiMmJiODVkNzQtNGE0NC00NWY2LTg3NzUtMDc3M2I0NjZjNjRlIiwibmV0Ijoid3MiLCJwYXRoIjoiLyIsInBvcnQiOiIyMDk1IiwicHMiOiJOZXctNzk1Xy0xMC4wMEdCIiwic2N5IjoiYXV0byIsInNuaSI6IiIsInRscyI6IiIsInR5cGUiOiItLS0iLCJ2IjoiMiJ9
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/5788" target="_blank">📅 17:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2JMF5f3B_411CbSj7uC58M_Liuq5dtc2FdTLALIx-3957uDuyf7_Fh35ZoaauVR9-kZqyDmmFUbnSRb9tVFdGMRjnu8Kf6x9ZrzQsLHZ7PSIVj1C0a4_hFaRKw26eYlHCI5jTl5KOXvICsZiEzNUDdmAlmV1TIeXLCzRiYy-b4avpUhz_-klSgomUqET_JVMAsOQkkq1KE_bwMhat7nO833cpEkUC_oM9skDe8B7fvY12qCFE5ZFRy6mX5oM0u3Hn_HlEMqwkiFOsaAKUw7YUr32tBsINAxTPaEI4POxmKlMrqVL332JpIZgjSpbh6KF4C1Z66v3sBWOWSTm-tXNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7DS6ohmrEYQ65Oa5I8ioE82gMFOWJbvASK14NNKFE5uFgAZ2zdOoT1dDJfwJRbLecSz9eHLr1g5395GQ5BhZ8XVOWwRGVo9avMH1ZMyaqIeiPEHzqr4BPOTImL5r0P7PhF_HrU1J8C0GxzTfVR2Hsr06W4v9azlvSs28FKyIcgEUeGco42EtZrz7qPeMOyoXPxIagFMVBwfqY79ON2nP-Id8_jWCmGYVc8BtTdWS_r7l2LLVOCABwwE61XD9G3f4FFUAy1lo96RTna5c14qVmZXkaRNUjmwFsoHbIJkTSSqv9CLB3gIP00Ti99iGcv62DTV15C3vmYnz4HAeypCGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
نسخه جدید MidONe Scanner منتشر شد!
اگر دنبال IP تمیز CDN، کلودفلر یا DNSهای سریع هستید، این اپ اندرویدی می‌تواند کارتان را راحت‌تر کند.
✅
اسکن حرفه‌ای CDN و Cloudflare
✅
پیدا کردن IPهای سالم از روی رنج
✅
تست و رتبه‌بندی DNSها
✅
تشخیص IPهای ناپایدار و محدودشده
✅
ذخیره و کپی نتایج با یک لمس
برخلاف خیلی از اسکنرها، فقط پینگ نمی‌گیرد؛ اتصال واقعی را تست می‌کند تا نتیجه به چیزی که در عمل تجربه می‌کنید نزدیک‌تر باشد.
⚡
📥
دانلود:
github.com/mwhammadrezss/midonescanner-android
توسعه دهنده
@mwhamadreza
یکی از ممبرای عزیز کانال
❤️
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/archivetell/5786" target="_blank">📅 16:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHyyM8hvoA_0R3mi0wwQaig-1mu-yuYEtqhBf3jQ_OLHqck7XqDU2NeqqmLYdyNvIT6KM-CE_qn6Pd1vaK7wqfwgZO9AkBy-fmC7ednvPYCEhhGjHb9VyyojN3UZmLTT1wha62Yt6KuJgKOzLmrwsp2wbnfjlHuWnTFUMNX-NtyEs_bMIN-yEkF-el0zL0CrKyzzql3Y2XMhOEA9RoUVW9Bko9SIIPqdHAkBGvPMa01ReRMV4BYiImVO2gNz7AGJJeRFDuL6JvEoHmJvfiK3vKDAph8XNpLgsurvnsNr0O68o90AIQxhF9sX6LtEFHecTrLIMY8io2EpKLWlexTKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📂
انتقال فایل بین گوشی، ویندوز، مک و لینوکس بدون نصب هیچ برنامه‌ای!
توسعه‌دهندگان LocalSend نسخه تحت‌وب این سرویس را منتشر کردند و حالا فقط با مرورگر می‌توانید فایل جابه‌جا کنید.
🚀
✅
بدون ثبت‌نام
✅
بدون نصب برنامه
✅
بدون محدودیت حجم فایل
✅
سازگار با همه سیستم‌عامل‌ها
کافیست هر دو دستگاه به یک Wi-Fi وصل باشند، سایت را باز کنید و انتقال را شروع کنید.
🌐
web.localsend.org
🔵
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/5782" target="_blank">📅 15:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2F8ck815PxxCEu4wnKRansJHKn_0gYkuwdcT-rpRStC46s9Nj3qAbOcZSyPvH7jX7UJAd_U1oYbJyr9gMynhabKBNASSUbHsuIF2fhOblV5XYK6jtVmhvryBsQcHgE21JufXOQWrdeEuq8wrWw0jHWMevqhjA2TwoUNdhwPiTXq852_i0AQWTAWDM3vVxfJ7CsvInH6e9zVmoBDSHYXWBRH4HtX4kDLpa4Qf_ntB_aDg7_n3_TkWe38aqVW27v8A5o6vdXvft0qHF7VskmSGqpleUY62OlUxHHz35HabZXQ5zR3yV77wpCzFi_pXw-sbR67obfodrReNabpP6Gl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://14037bcc-1d1d-41dd-9ff6-be16926c44e2@dood.rostamiarp.ir:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#@ArchiveTell @ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/5781" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5779">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">۲۰۰ گیگ کانفیگ اهدایی یکی از ممبرای عزیز
😁
❤️
vless://14037bcc-1d1d-41dd-9ff6-be16926c44e2@dood.rostamiarp.ir:8443?encryption=none&host=ap.isowli.ir&path=%2F&security=none&type=ws#@ArchiveTell
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/archivetell/5779" target="_blank">📅 15:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانفیگ نامحدود ۱ ساعته اهدایی یکی از ممبرای عزیز
😁
❤️
vless://614ad5da-e5cc-479d-bc90-3db549ca96e4@84.75.220.223:33434?encryption=none&fp=chrome&pbk=CBLftLCz0w2EX8H3sQ4ahU_lc9_aWJZO_8OHJEWGjDo&security=reality&sid=0af57b636837&sni=www.yahoo.com&type=tcp#ArchiveTell%201
vless://afce710f-2261-403e-ada6-459dbcb44b64@84.75.220.223:80?encryption=none&fp=chrome&pbk=XnjRQWaZ2QGrIJBGPuYOePg2wLl_ZM_gkCyJ2aKxylQ&security=reality&sid=7797159c&sni=www.yahoo.com&type=tcp#ArchiveTell%202
vless://3d1dbf5c-6f7d-47ee-9138-e217e0a77265@84.75.220.223:41034?encryption=none&mode=auto&path=%2F&security=none&type=xhttp#ArchiveTell%203
vless://5c5cb739-1112-4eea-bad1-282db5c24512@84.75.220.223:443?encryption=none&fp=chrome&pbk=g_oiiXO-P1L5MgEzE9qx7Vt0x-Z1-vI5QjXmscfh6Uw&security=reality&sid=27fd6d7ea3&sni=www.samsung.com&type=tcp#ArchiveTell%204
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/archivetell/5778" target="_blank">📅 13:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtE4Z3PhdQM_OeskgZlzpUjChs8unq73MRcdSkSu7K-S3YtUWxO51tu7Q_6hN6CbtSeM8H5hf2MAgPGkicBqqqFWwlzBGIMp6nUTmRT1jVg_vqxlh0A7cYbmCq9YJAjtd4FVc0cEQVM9HLSvj29svWmvXRIfsvDOXi1q1Kq2c8Q9IplPpoPr1ylhUc_nEU0JyhhHCrTcR1YZZuNFzq5NcG3rn03TwpNsV5j8ZlcD3zXtJPuWvxfuixYkYazOwwKEtGau1w211gR1Mhwr36cnXe37RGesRfqJzM4x4Vjx3X2y2dIVjHd4UY8rEWSvpOOzf4D4NFJfO11ONVadai64Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
افزونه Advanced Proxy Manager منتشر شد!
📌
اگر از v2rayN استفاده می‌کنید ولی نمی‌خواهید کل ترافیک ویندوز از پراکسی عبور کند، این افزونه می‌تواند فقط مرورگر کروم را به پراکسی متصل کند.
⚡
اتصال مرورگر بدون تغییر پراکسی کل سیستم
🔄
پشتیبانی از SOCKS5 ،SOCKS4…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/5777" target="_blank">📅 13:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌐
افزونه Advanced Proxy Manager منتشر شد!
📌
اگر از v2rayN استفاده می‌کنید ولی نمی‌خواهید کل ترافیک ویندوز از پراکسی عبور کند، این افزونه می‌تواند فقط مرورگر کروم را به پراکسی متصل کند.
⚡
اتصال مرورگر بدون تغییر پراکسی کل سیستم
🔄
پشتیبانی از SOCKS5 ،SOCKS4 و HTTP
📋
پروفایل‌های آماده و قابل ذخیره
📶
نمایش پینگ اتصال
🔒
کاملاً لوکال و متن‌باز
💡
مناسب برای زمانی که می‌خواهید فقط مرورگر از فیلترشکن استفاده کند و برنامه‌های دیگر مثل بازی‌ها یا نرم‌افزارهای بانکی بدون پراکسی کار کنند.
📥
آموزش نصب سریع:
فایل
.zip
رو از بخش Releases گیت‌هاب دانلود و اکسترکت کنید. بعد توی کروم برید به آدرس
chrome://extensions/
، حالت Developer Mode (بالا سمت راست) رو روشن کنید و روی
Load unpacked
بزنید و همون پوشه‌ای که اکسترکت کردید رو انتخاب کنید. تمام!
🔗
لینک دانلود و سورس‌کد در گیت‌هاب:
🐙
https://github.com/johncarterjourney-rgb/advanced-proxy-manager
👨‍💻
Dev:
@Bachedev
#Proxy
#Extension
#Chrome
#V2rayN
#OpenSource
➖
➖
➖
➖
➖
📢
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/archivetell/5776" target="_blank">📅 13:16 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
