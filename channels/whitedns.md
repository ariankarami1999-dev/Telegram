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
<img src="https://cdn4.telesco.pe/file/hNbnge03M_oKQV-8zZCnIWI7-Jl_xrmQniJvYdvEvOaVc_CNt80_nbnwEOBuD3vdGAsvMa1nsIXNEMGksUHRzE7ox3PG-w2AqRUIftI1J0-RCopjx-DzeknSko2FNO3602zRAOavMfM17CS6FcYdV46V-uaCefr4331dZvDDVwzXkn3dajkciT1cybZ22V4b6bO38uICnRtzvDdk0OHA1VGAFFhMaO5KkDaDMVFLrQeq8yeRGzRuc9V16LdZ_7tCXZUpICpMsWjLYfPefko5-bHTIH5SSFmC56u4RPRxHCvuDSTVK4EEczes6OY7AthsxP4Y99utRHusCfMXFIc0AQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 22:49:51</div>
<hr>

<div class="tg-post" id="msg-1823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.9.3-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/whitedns/1823" target="_blank">📅 14:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/T_bT1SoLKP0Qd_tsOXHBG1pJ75RVEQtzhF7siNVL9vNCGybc-cCwTPpu8YNWX70ttx9S1N8tx58xrWqICL2KsxH4yzs7HmSSosALrF4nMFb1uDoQJsEQTEhEPl3adqJDQuRrVuqvQ9IKcecSX4etuwq5hW7IXd1pUFthcxfZUfnSkVRcsuTH2Xhv0_hM0d747QZ9NWNmUj-1ebd8K_qNkq5o7pow4kBf9B6CuAy-rqzMG4upwM1QMwIc1w9PfQ-DGz15YgvxJALuIwV1oM9sH48tl3Er-5ZQFXthfzG_7Dif5bMuVPGKt8LWnk5D2YaMEhkj-psbT-V6UsMutDQYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
Mobile 1.9.3 — نسخه پایدار
🔥
نسخه پایدار 1.9.3 منتشر شد. برای به‌روزرسانی می‌توانید از قابلیت جدید داخل اپ استفاده کنید یا فایل را مستقیماً روی نسخه فعلی نصب کنید.
برنامه را حذف نکنید تا هویت و تنظیماتتان حفظ شوند.
قابلیت‌های جدید
آپدیت مستقیم از داخل اپ
کارت «نسخه جدید منتشر شده» حالا می‌تواند فایل به‌روزرسانی را دانلود و نصب کند.
این قابلیت فقط زمانی فعال است که:
پوشش اتصال روی «کل دستگاه» باشد.
فایل با همان کلید نسخه نصب‌شده امضا شده باشد.
ابزارک صفحه اصلی
بدون باز کردن برنامه، اتصال را برقرار یا قطع کنید. برای افزودن ابزارک، در Settings دکمه Add را بزنید.
هنگام جست‌وجوی مسیر نیز دکمه قطع اتصال در دسترس خواهد بود.
مشکلات رفع‌شده
مشکل نسخه 1.8.0 که ممکن بود برای یک هویت دو رکورد نگه دارد، برطرف شده است. اگر نصب شما در این وضعیت گیر کرده باشد، با اولین اتصال خودکار اصلاح می‌شود.
جست‌وجوی طولانی finding a working route اکنون محدودیت زمانی دارد. این فرایند قبلاً روی شبکه‌های دشوار ممکن بود تا ۲۷ دقیقه طول بکشد.
هنگام جابه‌جایی بین وای‌فای و دیتای موبایل، تونل تا جای ممکن به شبکه جدید منتقل می‌شود و از ابتدا ساخته نخواهد شد.
اتصال MASQUE in MASQUE اصلاح شده است. اگر روش اول برای هاپ داخلی پاسخ ندهد، روش دوم نیز آزمایش می‌شود.
تمام اصلاح‌های نسخه 1.8.1 نیز در این نسخه قرار دارند.
روش نصب دستی
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.3
فایل مناسب معماری گوشی را دانلود کنید.
اگر نمی‌دانید کدام فایل مناسب است، نسخه universal را بگیرید و آن را روی نسخه فعلی نصب کنید.
در صورت مشاهده مشکل، از مسیر Settings ← Diagnostics گزینه Send diagnostics را بزنید و گزارش را ارسال کنید.
⚠️
@whitedns</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/q6C8wabB5UuOt6P2y5N9zUJ3QebtDVnVbKSlF1IBUPZfpk38eK2VzzLst_0k-JnWjz8L0fOOc4NG8b5bgoGY3LfXo0y6JSeREJBLWKxzNUyibu-9d4sAL6i15ZzkipaPNS_gd-kYMg9loR3JGO9-vYu-Y5wqU-oEnnQvppgCqtsshjAYqKX3CCt2hcZgfAvrlrXzaLNHKRS7L2DiaHSV12P2JJEtSO3BPGcwyknDX2q-3yj9UBSdjZqsQO6wq6upfiRU9B9wKww9uopju_HZXY2YDjwX8irULQFBGS4XExVHNsKkt4so7ECtSyKEm5NW_OT3fSZdkPyuVpU1563XFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/whitedns/1821" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/I-ixn9C1nLmzyAST31-4UkOBTCocelY8zqW4W7U1NiWCRBfkwn8hekA6h0cy7AnfVQVm_DoFd_t4FTrTjRqbW-5dWPgR6PtpXTE4i3mblXGH4oYh8mosyffA0gInqL5GxLDsVq1TYPZ5DDAsBoRC5hGVRMHx3ExQAMfYAnvhlBrPbFl_NwKthYoIywE_xmGnTOZcyIYSbcBBtdsSTdiSPpgTTzcnKssMghW2sLUKV9B0wX0eZPjznpiWLEADmAUsAudso9X7ahE1NpGqDSMkEbFVHPmZEuEUWiXtRtuhWS__DN7pFtyb15zsHCmts6Ym6qC9f6oqW0f7XE2zqNxbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
CottenRouter v1.2.13
منتشر شد!
سریع‌تر، پایدارتر و آماده برای ترافیک سنگین
⚡️
• رفع مشکلات نصب
SlipGate
روی سرورهای تازه
• جلوگیری از Down شدن Router هنگام قطع نصب یا SSH
• رفع تداخل Domain و Port بین Backendها
• امنیت بهتر
CottenDNS
و
StormDNS
0
٪ Query Loss
در تست ۵۱۲ کلاینت همزمان
• پردازش بیش از
۲۲K Query/s
• بهبود TUI، خطاها و سیستم Purge
✅
آپدیت مستقیم بدون حذف Routeها، Backendها و تنظیمات قبلی
💻
GitHub
https://github.com/TaJirax/CottenRouter
📋
لیست کامل تغییرات
v1.2.13
https://github.com/TaJirax/CottenRouter/blob/main/docs/releases/v1.2.13.md
@whitedns</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/whitedns/1820" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CDTjbpZjlwMEZR96eOizTLsKbdsMmrmYcvjaKMPR2rc3PuuRsOBFQ55aC4e1FawoMtfu1RxbIhxjLetXvYbNmVU0SxEBIrwpEIGX8WC38L_9ZVtSueQGRTM2jY8MDbburHBebwK9i_Ngg0v5AxwN_7E5LBm-w7j6zJ6JCQg4y1qY42ihdr0-oRG6mrZJTFMgVVdYpYgzjNvsSbeaSCkkO8RsnX2ng6r6YNoZHmvQP3N-_ho2KDBqhBJJYl54nrpHCPbfAdLy789EpQqCIYBIb5R0cKPRFHfSu45L3XiV3Fr25ZbQVAw4C2C0wKjdCRuh7Lv_2pZgntPumOg-aBR2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihbr58jbBQ_YoZT8TFR16ADpSOerdsgSZRXYY3rpkf7CkvBs2KGJho00h5ycdoI5Ko5CDbfWe4wg6TusGIiWD1czDMIy0GCE4jSLLf6NCU30Er8_0Ir2ZOp2rn54-h1gXZsGQXNvU6l1JCwzHMbZwgPsTVvOkLoe_oNIs0nRY5VxTQv3Gex5TEQqXToWmSGFNeiXB36iFIijyjCa3U57-QOnYTihdI2fl_pkYYbqoJzIo1nt06uStQn1VrXu1dUYiAFk6X2Bzcq4qprFNDxfrm7A5y3XWZyqFeRcezQmzDGtWBE2255jwliYVNmYCfYV18fQRsty-jC7ituo3tEq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/q9Gj1raSiSrZFd55en9xQ7qNGXbyXWbJ10K5lb1Zc3oiNHFsnS0uT8Mh0wCb8QrFRd9nn-_GyqccUz7oHbO0y3XrP5EH_mvVozzlTLOe9AdeO3z7ahBKgTJMDyUG6fWxjoEZm-LVcphZvX2ycv8P8xGkGnqMgmbqDFp6rqd7gWLpGwUPpG_FesKWkmJG82TtegEwZqpm9_an_Or4DJlZ1WUJNrHgi9jK4IJrVBsaOtu1FWl0aRrFZEqjjDAIXzpHNT790Yoc6v3IPiFYnAyNKuTz-LJyGQiDrJ8xdNHQv8TzftjpX-niymS2ic7Sr2NNkn43PE3vGEA_QpjTeSsfrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Fuk-Cjxndm9020BsEkmVHLYDzG-9qaWQkOc2F4jHuY6Y3OcS2eaKwsTXTiQyzQonqj_9yKsTQbdClNA8hEDnEbif_VK7OYn8_UCicCCZf1qHMtsC8RX7UrOUaomysMyk9W2StofH6Pu42dTqsmZzOdjEMWDVgQY2T5o4zOB4s_l3t6KmjKENAFCqodCiEng-HKaFCVOU27r-NNJHsKHe1F44euC-w8gmLDAdSFxrooEsTZ7aq9q9sse2pauJOrYq3-Sh47-aHn8nH5_NMggygZ-rLbbwIP5Mo_0U0ptdzz8IG6IGZ2ltN96nyhickfakyz8aGNdbkT60CV2laG8pbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1805">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">💬
دوستان ما هرشب سرور های اختصاصی رو روی WhiteVPN بروز میکنیم تا از فیلتر شدن سرور ها جلوگیری کنیم.
متاسفانه این‌چند روز سرور سنگاپور رو نداریم ، توی یک شب ۳۰ ترابایت مصرف شد و هزینه زیادی داشت. وقتی خاموشش کردیم، دیگه سرور سنگاپور ارایه نمیداد.
باید دوباره موجود بشه و براتون یکی به زودی میسازیم.
🔒
اگر براتون مستقیم وصل نمیشه، به یک سرور عمومی وصل بشید و اختصاصی رو زنجیر Chain بکنید تا آی‌پی ثابت بگیرید.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1805" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/QSE2tPmideAbGtlodOp6x6RNo_fDSrUz29r17VxY4zvKrLzvpzCyhMSPzWr1a4Ofdf_vNl-DtbMFty5ErV0PUG2o2UcoxN7Gl2OTDGmM2jZbzducN8CpZFBLa3ETB-mTnE5RBo65GiZr9SUtSPDTRsFEKlzeIrQuGtS-wpZ_dBTS_B8DPtAFhlvblqkct8tWYog7pV2Ar8cMU24wFFijo3Xhhl6YAzNowSBxN73KqTFuoldqXjZ7_mEtzyKsdx8DeHhtGLxwhLB9owEhwrWBhd7JTGCbTEnKo2A5fR2MnMWrMaGO9tuyNTvfZ82VCbB-xHjG34dA0U0wHjrArINL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر به هر دلیلی نیاز به کانفیگ (cottondns,masterdns,stromdns) برای اپ
WhiteDNS
دارید از ربات زیر میتونید با محدودیت حجم و روزانه کانفیگ بگیرید.
⚠️
این کانفیگ 1 روزه و با حجم 0.5 گیگ هست
در حال حاضر تعداد کانفیگی که میتونیم بدیم خیلی محدود است و فقط با تاییدیه ادمین برای شما ارسال میشه
⛔️
لطفا اگر اشنایی ندارید و کنکجاوید و یا میخواید ازمایش کنید و... درخواست ندید
@MasterDnsManager_bot
WhiteDNSاپلیکیشن
دانلود اندروید
•
دانلود دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1793" target="_blank">📅 09:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/C-vX1lGiwCzBfePU3gYEmLOBfVQ6ziHclbvduhrfqJ6DXWevhT1EUifbwqfFn8wfQIi8UhB6JH5UvMehfc9Q4ixM9lIpNVL-STEkNgYO3QPUZdxUeeKqNyoGUMe2HrISA59yhiomrDFGBp6air_Bqtth7HMYpozeuHa0PmHWkrX2vtYZ4eHGmwmrjscM2QVRMudxN0mSXxqRNTqaXgofDR-b8u3NQOkQYdqDRda1u7XyjRzyG7fg_iNJAFRZKrLplJ9b4OkxLVtglWpRF-RuhEB6OVoWn5XNHArpozpcGzZxjcOEr3rrkyOwsjOKu6bRYirvgk_qTqmipPeYjqG8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
🤖
قابلیت جدید : (نسخه ازمایشی )
⚠️
⚠️
⚠️
گفت‌وگو با هوش مصنوعی در ربات
🔥
WhiteDNSResponder V.5
نسخه ازمایشی حتما باگ هایی دارد  و  دچار اشکالاتی خواهد شد که با پشنهادات و کمک شما هر روز بهبود خواهد یافت
👀
از این پس می‌توانید مستقیماً داخل ربات با هوش مصنوعی گفت‌وگو کنید، سؤال بپرسید، متن تولید یا ترجمه کنید و درباره موضوعات مختلف توضیح بگیرید.
این امکان جدید به صورت محدود و با درخواست کاربر فعال میشود.
⚠️
@WhiteDnsResponder_bot
🔐
نحوه درخواست دسترسی
1️⃣
وارد گفت‌وگوی خصوصی ربات شوید.
2️⃣
از منوی ربات گزینه /airequest را انتخاب کنید.
3️⃣
درخواست شما برای مدیر ارسال می‌شود.
4️⃣
پس از تأیید، دسترسی به‌صورت خودکار فعال شده و نتیجه از طریق ربات به شما اعلام می‌شود.
نیازی به پیدا کردن یا ارسال شناسه عددی تلگرام نیست.
🔹
روش استفاده
پس از فعال‌شدن دسترسی، سؤال خود را بعد از دستور /ai بنویسید:
/ai تفاوت DNS و VPN چیست؟
یا:
/ai یک متن رسمی برای درخواست همکاری بنویس
🔹
دستورات کاربردی
/ai سوال شما
شروع یا ادامه گفت‌وگو با هوش مصنوعی
/ainew
پاک‌کردن گفت‌وگوی قبلی و شروع مکالمه‌ای تازه
/aistatus
مشاهده سهمیه روزانه، میزان مصرف و تعداد درخواست‌های باقی‌مانده
📊
محدودیت‌های فعلی
• سهمیه روزانه براساس تأیید مدیر: ۵ یا ۱۰ پیام
• حداکثر ۳ درخواست در هر ۵ دقیقه
• حداکثر ۲۰۰۰ نویسه برای هر پیام
• نگهداری موقت چهار بخش قبلی مکالمه برای ادامه بهتر گفتگو
• قابل استفاده فقط در گفت‌وگوی خصوصی با ربات
• سهمیه روزانه در نیمه‌شب به وقت UTC تمدید می‌شود
🔒
امنیت و حریم خصوصی
• هوش مصنوعی به سرور، فایل‌ها، دستورات سیستمی یا اطلاعات خصوصی تلگرام شما دسترسی ندارد.
• متن مکالمات توسط این قابلیت در پایگاه داده ذخیره نمی‌شود.
• تنها شناسه کاربر، وضعیت دسترسی و میزان مصرف سهمیه ثبت می‌شود.
• لطفاً رمز عبور، اطلاعات بانکی، کلید API یا اطلاعات محرمانه ارسال نکنید.
⚠️
این قابلیت فعلاً به‌صورت محدود و آزمایشی ارائه می‌شود. درخواست‌های تکراری ارسال نخواهند شد و در صورت استفاده نادرست یا ارسال خودکار پیام‌ها، دسترسی کاربر ممکن است غیرفعال شود.
🤍
WhiteDNS — دسترسی ساده‌تر به ابزارهای کاربردی هوش مصنوعی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1790" target="_blank">📅 15:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✍️
موقت
اگر روی ویندوز و یا اندروید نسخه قدیمی دارید
⚠️
⚠️
ویندوز :
گزینه reset app data را بزنید و بعد uninstall کنید و جدیدترین نسخه را نصب کنید
اندروید :
حتما ورژن قدیمی را uninstall کنید و ورژن جدید را نصب کنید
@whitedns</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1789" target="_blank">📅 04:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✍️
موقت
برای جمینای و بقیه هوش مصنوعی ها بر اساس تستی که کردیم روی سایفون و تور راحت باز میشه - اگر تور و سایفون مستقیم وصل نمیشه اول با اتر وصل بشید و بعد خروجی را روی سایفون و یا تور تنظیم کنید.
در ضمن اگر روی یک اپراتور جواب نمیگیرید حتما حداقل یک اپراتور دیگه را هم تست کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/whitedns/1787" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-poll">
<h4>📊 امشب ساعت 8 به وقت ایران لایو بگذاریم جواب سوالات را بدیم ؟</h4>
<ul>
<li>✓ بله😍</li>
<li>✓ خیر😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1785" target="_blank">📅 14:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jZ-c3a2ZUj-g5JfH41EhdkvPWwlEkvqDvFx2YPSc2VCJCo9u18hW3vQMxuQTbSMhMnNrZrwYJ2mpZNTFO2R0Ipe0WSLUaj8P0rGqO7rvfqOb0eqRCDypzBKsARQ1xELRaI6ufWoMqWoONjTJePferi1wOofztHeWMyKLLll3wFShJo_1nFCTuj_eMRIW_BoKLSH7NMPCmRwi3iLh__yTMFv4Us5P1a0NFHqrCiFxzAGDJxMkUq4e63VljXSNpPG4xSbkIAKeh91sfDTDBN3D7QgEpMmnnzbREawcTXfo4QgQRukpUJWV6vYvivkgYDs7Pr_lqoFjlr_ZkZU406zc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
💬
Support Bot:
@WhiteDnsResponder_bot
🔗
WhiteDnsChain
@WhiteDnsChainbot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/whitedns/1784" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1778">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oDbwdVI_5cQR3nr4e9yTSOApApIrys9c6_MAau3S06038j3uGekRkeMH0_URSjkYrt3S55X1c3U-qLSN0YbtMFNY7QGvWzFVY56z7pacQWtZA6oG5LGDVMv-FPoXGnrtWuL52w28I3bO_RHsBYmvpej0TTiBYymQwVzrwNOOHHnfp6nSHQjUqmi8X_fx8rq0iW37YsUrz8y-oG2ets3e4fiy3zIoRoDURezHxZKJqsYQ2y0r0W7vgXZ6V22A16F1_LH9FXwz1sZ4Ux2_pGSzQ8ZsyASnBd6fnl2Z9noynmQy1Ra0uPQvfouz37B0TZood1o3c4hf9DiYQT1wgRbG2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
WhiteAesther mobile 1.6.1 (stable)
دوستانی که منتظر اپدیت بودند الان میتونند اپدیت کنند
⚠️
✨
چه چیزی جدید است؟
🔗
زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی. حامل اول چیزی است که شبکهٔ شما می‌بیند و حامل دوم چیزی است که سایت‌ها می‌بینند.
مسیرها ← حامل ← «خودم انتخاب می‌کنم»
⚡️
سایفون بهتر
سایفون به سرورهای بیشتری دسترسی دارد و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد، پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
🤖
حالت خودکار (آزمایشی)
اگر روشنش کنید، برنامه خودش اتر، سایفون و تور را هم‌زمان امتحان می‌کند و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود. راهی که روی هر شبکه کار کرد را هم یادش می‌ماند و دفعهٔ بعد سریع‌تر وصل می‌شود.
فعلاً پیش‌فرض خاموش است تا بیشتر امتحان شود. برای روشن کردن: مسیرها ← حامل ← «خودکار (آزمایشی)»
🛠
اگر نسخهٔ آزمایشی ۱.۶.۰ را نصب کرده بودید و وصل نمی‌شدید، این نسخه آن مشکل را برطرف می‌کند.
💡
نکته
اگر اتر روی اینترنت شما وصل نشد، سایفون را امتحان کنید:
مسیرها ← حامل ← «خودم انتخاب می‌کنم» ← سایفون
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.1
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.1-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.1-universal.apk
روی نسخهٔ فعلی به‌روزرسانی می‌شود و تنظیمات شما می‌ماند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید (همراه اول، ایرانسل، وای‌فای خانگی و…).
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1778" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1777">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SMRNb9xQZzWMK61V45kgzTFcrGDkUs_FAZpWY06WNma7qmSVVzNBaFXYXMLjr4qtQsgw_8T7oO_LdiOW1cvpXk95D0FzK38nKWTWkJsYDknEZXQqnxpiigNkm-F2DwkpWqLxEb1DcE5CgtUmKtlwAc_F5Iq83faCNXVFwIcLE_4p7abPUTv3NLZ3PO6uTn00V2uPejy-yRC3Fqj8W4L8pZ_jNxNPvelE_YHarhFe1Ne9bheMmiDjmbYu6bJlRi30uXdKBbQ5-lgmhrh4VV0u5ISTfWddf3akHlNKGO74rh321vwIy7pXHhoYmlJhCfcBp3fQiIWo71iwinI8Io5pzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther desktop  1.9.1 (stable)
🔥
دوستانی که منتظر اپدیت بودند الان دیگه میتونند اپدیت کنند
⚠️
پنج ایراد درست شد که سه‌تایشان را فقط وقتی می‌دیدید که شبکه سخت می‌شد.
دکمهٔ «یکی که کار می‌کند را پیدا کن» حالا واقعاً می‌گردد
تا امروز، جست‌وجو روی همان گزینهٔ اول می‌ایستاد و می‌گفت وصل شد — حتی وقتی نشده بود. هیچ‌وقت به سایفون، تور و شش ترکیب زنجیره‌ای نمی‌رسید. حالا هر راه را تا آخر امتحان می‌کند، و یکی را فقط وقتی قبول می‌کند که یک درخواست واقعی از آن رد شده و برگشته باشد.
⚠️
یک نشتی در حالت زنجیره‌ای بسته شد
اگر پروتکل را روی WireGuard یا MASQUE H3 گذاشته بودید و بعد سایفون یا تور را جلویش می‌گذاشتید، Aether از کنار آن کریر بیرون می‌رفت — یعنی از همان آدرسی که زنجیره برای پنهان کردنش وجود داشت. حالا پشت هر کریری خودکار روی MASQUE H2 قفل می‌شود.
به هر کریر همان‌قدر وقت داده می‌شود که لازم دارد
جست‌وجو قبلاً هر تلاش را سر ۹۰ ثانیه می‌برید، در حالی که سایفون در اولین اتصال روی شبکهٔ سخت تا ۵ دقیقه وقت می‌خواهد. نتیجه‌اش این بود که روی سخت‌ترین شبکه‌ها — دقیقاً جایی که این دکمه برای آن ساخته شده — هیچ‌وقت جواب نمی‌داد.
و چند چیز کوچک‌تر
• جست‌وجو ساعت نشان می‌دهد و از اول می‌گوید چقدر ممکن است طول بکشد
• سایفون می‌گوید اولین اتصالش روی شبکهٔ سخت چند دقیقه است، تا فکر نکنید هنگ کرده
• عمق جست‌وجو (از turbo تا thorough)
حالا واقعاً رعایت می‌شود
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.1
ویندوز → .exe
مک (اپل سیلیکون) → macos_arm64.dmg
مک (اینتل) → macos_x86_64.dmg
لینوکس → .AppImage یا .deb / .rpm
@whitedns</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1777" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1776">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RdtrCLNpCyOSuZWI8pnx7Pv6dNa73qpCGlLeVbSGSTKYwJjZksM11Ksk70jqu2e2DbDiPO02L2zVClLoiTcejD1MBmDby58IMNQZ19lfM_rYjaijJKQHLGVAdY8s_g4io4bvE256mR5wPsvNMEUcE5P-Mz8bri45kx6gnmIs0OUkQQ9W2OzA0xe1b61qoH8sLHO5mRUZ94s2Sncv8FnvBcA_MhJ-LpCbCvfuyK0z2fIKxwdFePJPzIlKw6G8xAje2DKlH5kAf2vbKad6E_rPmUVNVxRKFwchFuvvEktjJgqYNAgpa_PJOX4Qr2XtegcK5B9kgTLacBCmLafteqUAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه پایدار WhiteAesther به‌زودی منتشر می‌شود!
🚀
تجربه‌ای سریع‌تر، امن‌تر و مطمئن‌تر در دسکتاپ و موبایل. منتظر باشید
💚
@whiteaesther</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1776" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DMQ13MUiK3uN32C1JyIwb7IVZSRslnlAuIEq1-ZRneKOMb9Y5gsHrlokFvXw8AatrUde6PQfHyKQ5vT20qeV9gUqii4EYSUd4V2-qPIChSakCoJV0ce74kmv6QemEq_LrNGCwmSHqTaBKuEYMBfesKkjlPh-kiFxHmzta8GI7BRku7Q0opFGM2W7flVllBhpMvTTSr9CIFxUz_j5Ge2rOK-r4ml8C7TYPgYiGFMNyIIdheup7icFwg_94NqqmoiQM8NCWx6MxY7YiJ4Hg7zkf7pwRZ4w-3aD_oP0E5M4MGGj1M4m89LK5JRtR_KlBsLBppRexK7xB8fECuKeX40rKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1772" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان :
⚠️
⚠️
اگر پست ها را کامل نخوندید . لطفا توی گروه ها پیام ندید . چون کاملا مشخص هست خیلی از دوستان حتی 10 ثانیه هم وقت نگذاشتند . این مدل پیام دادن فقط باعث گمراهی بقیه میشه . لطفا کاملا پست ها را مطالعه کنید .برنامه را کاملا بررسی کنید . تنظیمات متفاوت را انجام دهید وفقط با توجه به روشی که توی پست های بالا گفته شده گزارش کنید
سپاس</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1771" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YDbLwkR4ZtJXeOdvui6HVIqCodbBIW3x-FTSKq56Ib_jLO5IKcLq6_Zh5c_Y9irwt3uxd2KwGWRpuGJu37VUZHjGNHekfx7Ctjr5JeU8gFe4s7tTrE-6ZS3AA2l-0HMZntFRolHeIj7DPNEpWPa2ynTK_efkvb46kv_51sdFC6rdSZdx8faQjVPVn0pEBShpW1Kv-hkm0k698TgRMocaqWztdja6I4LW9YbVDofJi0lT0hhiQr8RTphR8Bar7Z0gWU2rVBLTnQuIRGKGm3mBrYYAfT6W0GHuRlaGxdt3fMLcjaqXno3gRiF6VGB7qdHqgNCGSfkNZVsUFJcaQmSfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا توی نسخه اندروید هم شما حالت اتوماتیک دارید ، خودش می‌گرده و بهترین حالت را انتخاب می‌کنه و وصل میشه
#WhiteAesther_Mobile_1
.6.0</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1770" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteAesther Mobile  1.6.0
حالت خودکار: فقط دکمهٔ اتصال را بزنید
🔥
🔥
🔥
🔥
⚠️
این نسخه آزمایشی است و ممکن است باگ داشته باشد. داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود.
✨
چه چیزی جدید است؟
دیگر لازم نیست بدانید اتر، سایفون یا تور کدام روی اینترنت شما کار می‌کند. در حالت «خودکار» برنامه خودش اول اتر را امتحان می‌کند و اگر نشد سایفون و تور را، و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود.
راهی را هم که روی هر شبکه کار کرد یادش می‌ماند؛ دفعهٔ بعد روی همان وای‌فای یا همان سیم‌کارت خیلی سریع‌تر وصل می‌شود.
📱
استفاده
برای بیشتر کاربران خودکار از قبل روشن است؛ فقط دکمهٔ اتصال را بزنید.
اگر قبلاً حامل را دستی انتخاب کرده‌اید: تب «مسیرها» ← کارت «حامل» ← «خودکار (پیشنهادی)».
⏳
اولین بار روی یک اینترنت سخت ممکن است چند دقیقه طول بکشد؛ لطفاً صبر کنید. روی صفحه نوشته می‌شود الان کدام راه را امتحان می‌کند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.0
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.0-universal.ap
@whitedns</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1769" target="_blank">📅 15:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bHGiU9RlA7yRHFubmHyQyct-6AdK3EKYnex44ytgS7f9mRGAqfv5SwPFlHxY0d_Igdo8MyzhZUPajrBvwpVL-bUKZrnI0MYUu0RjIwC6ijrb1vY_GmndJFwVHt6gJQkQdCSCQlYJfCnx5teyrOWyVEBCcxfk_8t8H3R8Nf3H840Un8j4ukcb13gz1wIb0KpUPZuzAr8kzkF2Ra8NgGrtnZ2lMa6krd7nwFCJjSM_1I1jj6doyQqlEWvFDOfv7jLiZcnwv-SYORPgJj_ELL-JzTjrUf3XlRUrTPhrXBv20zO6ZbAoOlxz1EkpsNJZfdUOADNrNLFWh0rjm5kKBRNL6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی نسحه دسکتاپ یک گزینه اتوماتیک ما داریم . که خودش بهترین کانکشن را براتون پیدا میکنه
#
WhiteAesther_desktop_1
.9.0</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1768" target="_blank">📅 14:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستان :
اموزش هایی که ما توی پست های کانال میگذاریم به خدا برای شماست - والا ما خودمون بلدیم !
خواهشا وقت بگذارید مطالعه کنید</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1767" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-poll">
<h4>📊 توی این نسخه ازمایشی whiteaesther مشکل شما برای اتصال و استفاده از هوش مصنوعی حل شد ؟</h4>
<ul>
<li>✓ 😏اتصال اوکی شد ولی هوش مصنوعی کار نمیکنه</li>
<li>✓ ❤️هوش مصنوعی و اتصال اوکی شد</li>
<li>✓ کلا نتونستم وصل بشم😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1766" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther mobile 1.5.0
⚠️
⚠️
⚠️
⚠️
این یک نسخهٔ آزمایشی است و ممکن است باگ داشته باشد. برای همین داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود. اگر به اتصال پایدار نیاز دارید، فعلاً روی نسخهٔ فعلی بمانید.
━━━━━━━━━━
✨
چه چیزی جدید است؟
۱
. زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی که بخواهید. حامل اول چیزی است که شبکهٔ شما (اپراتور) می‌بیند و حامل دوم چیزی است که سایت‌ها و اینترنت می‌بینند.
۲. سایفون بهتر
سایفون حالا به سرورهای بیشتری دسترسی دارد (از جمله سرورهای داوطلبانهٔ Conduit) و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد؛ پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
━━━━━━━━━━
📱
چطور استفاده کنم؟
۱
. به تب «مسیرها» بروید و در صفحهٔ «چطور وصل می‌شود» پایین بیایید تا به کارت «حامل» برسید.
۲. در بخش «اول — چیزی که شبکه شما می‌بیند» حامل اول را انتخاب کنید.
۳. در بخش «بعد — چیزی که اینترنت می‌بیند» حامل دوم را انتخاب کنید. اگر فقط یک حامل می‌خواهید، «هیچ‌چیز دیگر» را بزنید.
۴. با دکمهٔ «ترتیب را جابه‌جا کن» جای دو حامل با یک لمس عوض می‌شود.
۵. «پوشش» باید روی «کل دستگاه» باشد؛ سایفون و تور در حالت «فقط پروکسی» اجرا نمی‌شوند.
۶. به «خانه» برگردید و وصل شوید. آنجا مسیر کامل نوشته می‌شود، مثلاً «متصل از طریق سایفون، بعد اتر»، و وضعیت هر حامل جداگانه نشان داده می‌شود.
━━━━━━━━━━
🔀
کدام ترکیب برای چه کاری؟
🔹
اتر ← سایفون
اتر وصل می‌شود ولی می‌خواهید سایت‌ها آی‌پی خارجی سایفون را ببینند، نه کلودفلر. کشور خروجی را هم می‌توانید در کارت «کشور خروجی» انتخاب کنید.
🔹
اتر ← تور
بیشترین حریم خصوصی، ولی کند.
🔹
سایفون ← اتر
وقتی اتر روی شبکهٔ شما مستقیم وصل نمی‌شود: سایفون راه را باز می‌کند و اتر از داخل آن بیرون می‌رود.
🔹
سایفون ← تور
وقتی تور مستقیم بسته است.
🔹
تور ← اتر / تور ← سایفون
برای شبکه‌هایی که فقط تور (با پل) از آن‌ها بیرون می‌رود. این دو ترکیب کمتر از بقیه آزمایش شده‌اند و نتیجهٔ شما برای ما خیلی ارزشمند است.
اگر یک ترتیب وصل نشد، «ترتیب را جابه‌جا کن» را بزنید و دوباره امتحان کنید. اینکه کدام ترتیب جواب بدهد به شبکهٔ شما بستگی دارد.
━━━━━━━━━━
💡
نکته‌ها
• زنجیره از یک حامل تنها کندتر است. اگر یک حامل به‌تنهایی برایتان کار می‌کند، همان را نگه دارید.
• وقتی اتر حامل دوم است، خودکار از H2 استفاده می‌کند و انتخاب پروتکل اثری ندارد.
• وقتی تور حامل دوم است، اسنوفلیک کار نمی‌کند؛ تور مستقیم، با پل obfs4 یا با پل‌هایی که به شما داده شده وصل می‌شود.
• اولین اتصال سایفون ممکن است چند دقیقه طول بکشد؛ صبر کنید.
• اگر برای سایفون کشوری انتخاب کرده‌اید و وصل نمی‌شود، «بهترین گزینهٔ موجود» را انتخاب کنید.
• اگر در تنظیمات اندروید «VPN همیشه روشن» همراه با «مسدود کردن اتصال‌های بدون VPN» روشن است، ممکن است سایفون و تور وصل نشوند؛ خاموشش کنید.
━━━━━━━━━━
🐞
گزارش باگ
اگر به مشکلی خوردید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده». لطفاً بنویسید کدام ترکیب را امتحان کردید و روی چه اینترنتی بودید (همراه اول، ایرانسل، وای‌فای خانگی و…).
━━━━━━━━━━
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.5.0
⚠️
در صورت امکان ورژن قبلی را کاملا uninstall کنید و ورژن جدید را نصب کنید تا کاملا بروز شود
⚠️
• بیشتر گوشی‌ها: WhiteAestherMobile-1.5.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.5.0-universal.apk
روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان حفظ می‌شود. برای برگشتن به نسخهٔ پایدار (1.4.2) باید اول این نسخه را حذف کنید.
@whitedns</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1762" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther desktop 1.9.0
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
این نسخه «آزمایشی» (Pre-release) است و ممکن است باگ داشته باشد. بنا به درخواست تعداد زیادی از شما، آن را زودتر در اختیارتان می‌گذاریم.
✅
اگر نسخهٔ فعلی برایتان بدون مشکل کار می‌کند، فعلاً نیازی به به‌روزرسانی ندارید.
✨
چه چیزهایی جدید است؟
🔗
زنجیر کردن دو راه خروج
حالا می‌توانید Aether، سایفون و تور را دوتادوتا و به هر ترتیبی پشت هم بگذارید. اولی شما را از شبکهٔ فیلترشده بیرون می‌برد، دومی تعیین می‌کند با چه IP و از چه کشوری دیده شوید.
مثلاً Aether ← سایفون: سرعت Aether برای بیرون رفتن، و کشور خروجِ سایفون.
🔍
دکمهٔ «یکی که کار می‌کند را پیدا کن»
اگر نمی‌دانید روی شبکهٔ شما کدام راه جواب می‌دهد، اپ خودش همه را یکی‌یکی امتحان می‌کند و اولی را که وصل شد نگه می‌دارد.
🟢
سایفون خیلی بهتر وصل می‌شود
خیلی‌ها گفته بودند با اپ خود سایفون وصل می‌شوند ولی با حالت سایفونِ ما نه. علتش را پیدا کردیم: سایفونِ ما نمی‌توانست از پروکسی‌های داوطلبانهٔ خود سایفون (in-proxy) استفاده کند، یعنی همان راهی که در ایران بیشتر از همه جواب می‌دهد. فهرست سرورهایش هم به‌روز نمی‌شد. هر دو مشکل برطرف شد و سایفون حالا برای وصل شدن تا ۵ دقیقه صبر می‌کند (قبلاً ۲ دقیقه بود).
📥
دانلود:
https://github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.0
⚠️
دوستان حتما  delete cache/data را بزنید تا کاملا بروز از برنامه استفاده کنید
⚠️
🪟
ویندوز: WhiteAesther_1.9.0_windows_x86_64.exe
🍎
مک با چیپ M1 و جدیدتر: WhiteAesther_1.9.0_macos_arm64.dmg
🍎
مک اینتل: WhiteAesther_1.9.0_macos_x86_64.dmg
🐧
لینوکس: فایل AppImage یا deb یا rpm (نسخهٔ x86_64 یا arm64)
🐞
اگر به مشکلی خوردید:
دکمهٔ Advanced ← عیب‌یابی ← در بخش «گزارش»، دکمهٔ «ذخیرهٔ گزارش» یا «کپی» را بزنید و برای ما بفرستید. آدرس‌های IP به‌طور پیش‌فرض در گزارش پنهان می‌شوند.
📘
آموزش نسخهٔ 1.9.0
١) کجاست؟
بالای برنامه دکمهٔ Advanced را بزنید ← از منوی کنار، «مسیرها و پروتکل‌ها» ← کارت «راه خروج».
٢) یک راه خروج (مثل قبل)
در ردیف «خروج از این شبکه با» یکی را انتخاب کنید (Aether، سایفون یا تور) و ردیف «و سپس خروج از» را روی «هیچ‌چیز دیگر» بگذارید.
٣) زنجیر کردن دو راه خروج
در ردیف اول چیزی را بزنید که شما را از شبکه بیرون می‌برد، و در ردیف دوم چیزی که می‌خواهید IP و کشورِ خروجتان مالِ آن باشد. زیر این دو ردیف یک کادر دقیقاً می‌گوید این ترکیب چه چیزی به شما می‌دهد و چه چیزی نه.
💾
برای اینکه انتخابتان بعد از بستن برنامه هم بماند، «ذخیرهٔ پروفایل» را بالای صفحه بزنید.
چند ترکیب کاربردی:
• Aether ← سایفون: وقتی Aether وصل می‌شود ولی IP از کشور دیگری می‌خواهید. کشور را از «کشور خروج» انتخاب کنید (فهرست کشورها بعد از اولین اتصال سایفون ظاهر می‌شود).
• سایفون ← Aether: وقتی Aether به‌تنهایی وصل نمی‌شود ولی سایفون می‌شود. خروجتان همچنان نزدیک خودتان است و کشورتان عوض نمی‌شود. شرطش این است که قبلاً حداقل یک بار با خود Aether (بدون زنجیره) وصل شده باشید.
• تور ← سایفون: وقتی نه Aether و نه سایفون به‌تنهایی وصل نمی‌شوند. کندتر است، ولی یک راه دیگر است.
نکته: وقتی تور نفر دوم زنجیره است، از «پل‌ها» استفاده نمی‌کند؛ کارِ بیرون رفتن را نفر اول انجام داده.
نکته: زنجیره‌ای که سایفون یا تور در آن باشد UDP را عبور نمی‌دهد. سایت‌ها و بیشتر برنامه‌ها عادی کار می‌کنند، ولی بعضی تماس‌های صوتی و تصویری یا بازی‌های آنلاین ممکن است کار نکنند.
٤) پیدا کردن خودکار
در همان صفحه، کادر سبز «نمی‌دانید کدام کار می‌کند؟» را پیدا کنید و «یکی که کار می‌کند را پیدا کن» را بزنید.
اپ اول تک‌ها را امتحان می‌کند (Aether، سایفون، تور) و فقط اگر هیچ‌کدام وصل نشد سراغ ترکیب‌ها می‌رود. به هرکدام تا ۹۰ ثانیه فرصت می‌دهد و نتیجهٔ هر تلاش را همان‌جا نشان می‌دهد. هر وقت خواستید، «توقف جستجو» را بزنید.
٥) درباره سایفون
اولین اتصال سایفون ممکن است چند دقیقه طول بکشد، مخصوصاً وقتی از طریق پروکسی‌های داوطلبانه وصل می‌شود. عجله نکنید؛ تا ۵ دقیقه صبر می‌کند.
⚠️
مشکلات شناخته‌شده
• زنجیره‌هایی که به Aether ختم می‌شوند (مثل سایفون ← Aether) ممکن است بعد از چند ثانیه قطع و دوباره وصل شوند (وضعیت reconnecting). روی رفعش کار می‌کنیم.
• ترکیب سایفون ← تور، و قابلیت Kill switch (قطع ترافیک هنگام افتادن تونل) در حالت زنجیره، هنوز کمتر آزمایش شده‌اند.
ممنون که با ما هستید
🤍
گزارش‌های شما مستقیم به بهتر شدن نسخهٔ پایدار کمک می‌کند.
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1761" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1759">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.   بعدش دوباره وصل بشید.   خود اپ هم…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1759" target="_blank">📅 15:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1758">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sh3AncrnfgEeS4eLZuOYzUjpleA6plwg5SkoXMd6ESch4aj2Uoe4BdWgewk05n0rKx6LJgz4TvaT_na4dcmJFM5Jbv9RJXAEFOCxkhzFNHZsea3KsJPPFc54mA1McU2oJyu5k6CnXs_-lZwMXxmc9mSAtkrhxhfiH2ZxYmD97q9KnC0giYyvKJcC6_uvrs88E8Ge95wTColq-BjbvsLreEONML6Tj-ttF3kPCql6EA_oJ_NVUI1MWWFl8Yp2WjOfN_wTNYuSb5THI0sYQPP4oK6yOrD9jA--VA-rdSmlOUPSWOtqtkAMbmoFlql8s-OVTjZZ0JURTgc13HEhyaoTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
WhiteVPN Desktop v1.0.22 منتشر شد
این نسخه چند مشکل مهم را برطرف می‌کند که می‌توانست باعث
عدم اتصال، ذخیره‌نشدن تنظیمات و ناسازگاری برخی کانفیگ‌ها
شود. همچنین از این نسخه،
سرورهای اختصاصی WhiteVPN
هم به نسخه دسکتاپ اضافه شده‌اند.
━━━━━━━━━━━━━━━━━━
در این نسخه چه مواردی اضافه شد و چه باگ هایی رفع شد :
🖥
سرورهای اختصاصی و عمومی، هر دو در دسکتاپ
تا امروز نسخه دسکتاپ فقط از سرورهای عمومی استفاده می‌کرد، در حالی که نسخه موبایل روی سرورهای اختصاصی قرار داشت.
حالا هر دو فهرست داخل برنامه در دسترس هستند و از صفحه
Subscriptions
می‌توانید مشخص کنید از کدام منبع متصل شوید.
نصب‌های جدید به‌صورت پیش‌فرض با
فهرست اختصاصی
شروع می‌شوند.
اگر یکی از فهرست‌ها در دسترس نباشد، برنامه دیگر همان‌جا متوقف نمی‌شود و به‌صورت خودکار منابع دیگر را بررسی می‌کند؛ از جمله:
• فهرست داخلی دیگر
• سابسکریپشن‌های شخصی شما
• کانفیگ‌هایی که دستی وارد کرده‌اید
برنامه همچنین اعلام می‌کند اتصال از کدام منبع انجام شده است. انتخاب اصلی شما تغییر نمی‌کند و در اتصال بعدی دوباره همان منبع امتحان خواهد شد.
━━━━━━━━━━━━━━━━━━
🛠
رفع مشکل «هیچ سروری وصل نمی‌شود»
در نسخه‌های قبلی، اگر روی فهرست داخلی فیلتر
کشور
یا
نوع اتصال
انتخاب می‌کردید و بعد به سابسکریپشن شخصی خودتان می‌رفتید، همان فیلتر روی فهرست جدید هم اعمال می‌شد.
در نتیجه ممکن بود تمام سرورهای شما رد شوند، بدون اینکه مشخص باشد مشکل از کجاست.
حالا هر فهرست تنظیمات و فیلترهای خودش را نگه می‌دارد.
وقتی وارد فهرست دیگری می‌شوید، آن فهرست از حالت
Automatic
شروع می‌شود و وقتی برمی‌گردید، انتخاب قبلی شما همچنان حفظ شده است.
━━━━━━━━━━━━━━━━━━
⚙️
رفع مشکل ذخیره‌نشدن تنظیمات
برخی گزینه‌های صفحه Settings تغییر می‌کردند، اما پس از خروج از صفحه به حالت قبلی برمی‌گشتند.
این مشکل برای گزینه‌هایی مثل:
Amnezia Noise
و
این‌ها مستقیم خارج شوند
برطرف شده است.
حالا تغییرات مثل نسخه موبایل، به‌درستی ذخیره می‌شوند.
━━━━━━━━━━━━━━━━━━
🔗
پشتیبانی بهتر از کانفیگ‌ها
پشتیبانی از موارد زیر اصلاح و کامل‌تر شده است:
anytls
socks
HTTP Proxy
قبلاً کانفیگ‌های anytls ممکن بود اصلاً در فهرست نمایش داده نشوند.
کانفیگ‌های socks و HTTP Proxy هم ذخیره و نمایش داده می‌شدند، اما هنگام اتصال به‌درستی کار نمی‌کردند.
این مشکلات در نسخه جدید برطرف شده‌اند.
━━━━━━━━━━━━━━━━━━
🐧
رفع مشکل آیکون Tray در لینوکس
در برخی نسخه‌های لینوکس، کلیک روی آیکون WhiteVPN کنار ساعت باعث بازگشت پنجره برنامه نمی‌شد.
این مشکل در نسخه 1.0.22 برطرف شده است.
━━━━━━━━━━━━━━━━━━
⚠️
کاربران لینوکس، این بخش را حتماً بخوانید
نام فایل‌های لینوکس تغییر کرده است.
فایل‌های بدون پسوند amd64 و arm64 حالا از
WebKitGTK 4.1
استفاده می‌کنند و مناسب سیستم‌های جدید هستند، از جمله:
• Ubuntu 24.04 و جدیدتر
• Debian 13
• Fedora 40 و جدیدتر
اگر از
Ubuntu 22.04
یا
Debian 12
استفاده می‌کنید، نسخه webkit40 را دانلود کنید:
WhiteVPN-Desktop-1.0.22-linux-amd64-webkit40.deb
در نسخه‌های قبلی، نام‌گذاری فایل‌های Linux بین amd64 و arm64 یکسان نبود و همین موضوع می‌توانست باعث انتخاب فایل اشتباه و خطای Dependency شود.
این نام‌گذاری حالا اصلاح شده است.
✅
برای کاربران Linux با پردازنده Intel/AMD، ساده‌ترین گزینه همچنان
AppImage
است:
WhiteVPN-Desktop-1.0.22-linux-amd64.AppImage
━━━━━━━━━━━━━━━━━━
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
📥
راهنمای سریع انتخاب فایل
🪟
Windows — Intel / AMD
windows-x64
🪟
Windows — ARM / Snapdragon
windows-arm64
🍎
Mac — Apple Silicon / M1 و جدیدتر
macos-arm64
🍎
Mac — Intel
macos-amd64
🐧
Ubuntu 24.04+ / Debian 13
linux-amd64.deb
🐧
Ubuntu 22.04 / Debian 12
linux-amd64-webkit40.deb
🐧
Fedora / RPM-based Linux
linux-amd64.rpm
━━━━━━━━━━━━━━━━━━
📢
@whitedns</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1758" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1757">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.
بعدش دوباره وصل بشید.
خود اپ هم هر ۳۰دقیقه اتوماتیک ساب رو آپدیت میکنه.
کشور ها ثابت میمونه و فقط آی‌پی ها عوض میشن.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1757" target="_blank">📅 10:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1756">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🛡
انتشار نسخه WhiteVPN 1.6.7
👆
دوستانی که این ورژن رو قبلا دانلود کرده بودند. دوباره نصبش کنید چون سرور های عمومی یک باگی داشت که رفع شد.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1756" target="_blank">📅 10:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.7-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1751" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1751" target="_blank">📅 10:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWLgjUP6AYZeKeLqzczAubhjhwX3gNvNjPpItbPoITBgnkeRO6Eks8sUZY_E1s6fTulXzGa0o-4v0o2nh-vTpNna3y2lEUnv8lQI_H24gTJA0hcYaeh6bDrmWQgdh7EqRIYY34FbxJ48VOgVtodiLnWQctAHbkVUOlWIfilDLoecROxKXsPtm1i2K5Xo4_VUpLmSxQ8jXfPDtT5Xye6_LY3F9x2Tl7Re1RHz8dCid5o7zfk382u7Rn_mbWLubtFbnDULZrbcbr7j9qZ5Z3R42t2APXMYf81CRVOfpgLDczQrDC5aovVm2oDssq4fxQFaVYxxVXzfU3tvpxrcp_B6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه WhiteVPN 1.6.7
✍️
تغییرات این نسخه
🟢
توی این نسخه، ما سرور های اختصاصی خودمون رو هر چند ساعت یکبار تازه میکنیم تا پایداری بیشتر بشه. و فیلترنشن.
🟢
۳ کشور جدید به سرور های اختصاصی اضافه کردیم
🇺🇸
🇩🇪
🇸🇬
🟢
با کمک تیم پس‌کوچه
@paskoocheh
یکسری حفره امنیتی رو رفع کردیم
🟢
حالا میتونید همزمان تست سرعت بگیرید و هرکدوم رو خواستید کنسل کنید.
پیشنهاد میکنم حتما این ورژن رو بگیرید تا آپدیت های سرور های اختصاصی براتون بیاد.
⭐️
دانلود کنید، به بقیه معرفی کنید و نتیجه تست هاتون رو برای ما بفرستید تا مارو هم خوشحال کنید.
💻
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/whitedns/1750" target="_blank">📅 10:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستان عزیز من مجبور به پاک کردن ورژن آخر شدم. ساب های عمومی کار نمیکردند داخل اپ. به زودی آپدیت میکنم و دوباره پست رو میفرستم براتون.
سرور های اختصاصی توی این ورژن جدید که دانلود کردید باید درست کار کنه.
شرمنده همگی
❤️</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1749" target="_blank">📅 09:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1746">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⭐️
امروز یک آپدیت جدید برای WhiteVPN داریم
توی این ورژن، یکسری تغییرات امنیتی داشتیم به کمک بچه های تیم پسکوچه.
👨‍💻
مهمتر از همه، سرور های اختصاصی رو اپدیت میکنیم تا هر چند ساعت آپ‌پی های جدید بهتون بده.
این یکم هزینه های مارو بیشتر میکنه اما اینطوری کار فیلترچی رو سخت‌تر میکنیم و سرویس ها دیگه فیلتر نمیشن.
🥺
دیروز مادربزرگ خودم برای اولین بار از ابزار هامون استفاده می‌کرد و چنان دعای خیری برام کرد که انرژی ۲۰برابر شده.
هیچی چیزی ارزشش از این بیشتر نیست که بتونیم با عزیز هامون در ارتباط بمونیم.
هوای هم دیگرو داشته باشید
ارادت
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1746" target="_blank">📅 06:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1745">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">با WhiteAesther به Tor و Psiphon وصل شو!
🔥
https://youtu.be/WiybhJ7ylps
آخرین نسخه WhiteAesther
🦋
WhiteAesther Windows
WhiteAesther Android</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1745" target="_blank">📅 02:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1743">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
وایت‌اِستر موبایل نسخهٔ 1.4.2 منتشر شد
WhiteAesther Mobile v1.4.2
حالا سه راه خروج دارید، نه یکی.
از این نسخه اگر شبکه جلوی یک مسیر را گرفت، بدون نصب برنامهٔ دیگری می‌توانید مسیر بعدی را امتحان کنید.
⚡️
اِتر | Aether
همان موتور اصلی برنامه؛ سریع‌ترین مسیر و حالت پیش‌فرض.
🌐
سایفون |Psiphon
از شبکهٔ سایفون استفاده می‌کند. کمی کندتر است، اما ممکن است روی شبکه‌هایی که اِتر جواب نمی‌دهد متصل شود.
🧅
تور | Tor
عبور از سه بازپخش؛ مناسب زمانی که حریم خصوصی اهمیت بیشتری دارد. کندترین گزینه بین سه مسیر.
✅
تمام قابلیت‌های قبلی با هر سه مسیر کار می‌کنند:
• زنجیرهٔ خروج
• تقسیم ترافیک
• قوانین مسیریابی
• کلید قطع اضطراری
✨
تغییرات مهم نسخهٔ 1.4.2
• انتخاب کشور خروجی برای سایفون
• دریافت پل تور با یک دکمه
• امکان فراموش کردن نقطهٔ پایانی و جست‌وجوی دوباره
• رفع مشکل ثابت ماندن آدرس بدون تونل
• رفع نمایش اشتباه آی‌پی در حالت سایفون
• اضافه شدن سه موتور با فقط حدود ۱۴ مگابایت افزایش حجم
⬇️
دانلود نسخه موبایل
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
📖
آموزش کامل استفاده
برای مشاهده، بخش زیر را باز کنید
👇
۱️⃣ انتخاب راه خروج
وارد این بخش شوید:
پیشرفته ← مسیرها و پروتکل‌ها
در کارت
«راه خروج»
سه گزینه دارید.
اِتر
| Aether
همان حالت قبلی و سریع‌ترین مسیر.
سایفون
|Psiphon
پیدا کردن خودکار مسیر و امکان انتخاب کشور خروج.
تور
| Tor
مناسب‌تر برای ناشناس‌ماندن، اما کندتر.
مسیر موردنظر را انتخاب کنید و سپس
اتصال
را بزنید.
⚠️
در حالت سایفون و تور، تنظیمات نقطهٔ پایانی و انتخاب پروتکل اثری ندارند؛ این موارد فقط مخصوص اِتر هستند.
━━━━━━━━━━
۲️⃣ انتخاب کشور خروج در سایفون
بعد از انتخاب سایفون، گزینه
«کشور خروج»
ظاهر می‌شود.
🔸
در اولین استفاده ممکن است فقط
«بهترین گزینه موجود»
نمایش داده شود.
این طبیعی است؛ فهرست کشورها بعد از اولین اتصال موفق دریافت می‌شود.
🔸
انتخاب کشور یک ترجیح است، نه تضمین.
بعضی کشورها ظرفیت کمتری دارند و ممکن است اتصال به آن‌ها موفق نشود.
اگر یک کشور متصل نشد، گزینه
«بهترین گزینه موجود»
را انتخاب کنید تا سایفون از تمام سرورهای قابل دسترس استفاده کند.
🔄
تغییر کشور نیازمند اتصال مجدد است.
━━━━━━━━━━
۳️⃣ تور و پل‌ها
بعد از انتخاب تور، بخش
«پل‌ها»
نمایش داده می‌شود.
خاموش
اتصال مستقیم به تور.
همراه برنامه
استفاده از پل‌های داخلی.
گزینه‌های ترابرد:
obfs4
snowflake
meek
چسبانده‌شده
برای وارد کردن پل شخصی.
در این حالت می‌توانید پل را دستی وارد کنید یا گزینه
«از تور پل بگیر»
را بزنید.
🔑
هنگام دریافت پل، کشوری را وارد کنید که از آن متصل هستید.
مثال:
IR
منظور کشور فعلی شماست، نه کشوری که می‌خواهید آی‌پی خروجی آن را داشته باشید.
💡
ابتدا با اِتر یا سایفون متصل شوید و بعد پل بگیرید.
پل‌های جدید به فهرست اضافه می‌شوند و موارد قبلی حذف نمی‌شوند.
━━━━━━━━━━
۴️⃣ نکته مهم درباره تور
تور فقط ترافیک زیر را عبور می‌دهد:
TCP
برنامه درخواست‌های ناسازگار را مدیریت می‌کند تا اتصال بی‌دلیل معلق نماند.
برای بازی، تماس تصویری و استفاده‌های حساس به تأخیر، اِتر یا سایفون انتخاب مناسب‌تری هستند.
━━━━━━━━━━
۵️⃣ اگر راه خروج قطع شود
اگر پردازش سایفون یا تور متوقف شود، وایت‌اِستر آن را تشخیص می‌دهد، وضعیت را
«خطا»
نشان می‌دهد و زنجیره اتصال را می‌بندد.
اگر گزینه
«اگر تونل قطع شد، ترافیک را مسدود کن»
فعال باشد، ترافیک بسته باقی می‌ماند تا خارج از تونل ارسال نشود.
برای بازگرداندن اتصال، ابتدا
قطع اتصال
را بزنید.
@whitedns</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1743" target="_blank">📅 19:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1741">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚀
وایت‌اِستر دسکتاپ نسخهٔ ۱.۸.۰ منتشر شد
WhiteAesther Desktop v1.8.0
حالا سه راه خروج دارید، نه یکی.
تا امروز ترافیک شما از مسیر کلادفلر عبور می‌کرد. این مسیر سریع است، اما معمولاً کشور خروج شما را تغییر نمی‌دهد.
از نسخهٔ ۱.۸.۰ دو مسیر جدید اضافه شده است:
⚡️
اِتر
Aether
همان حالت قبلی و سریع‌ترین گزینه برای استفاده روزمره.
🌐
سایفون
Psiphon
مسیر مناسب را پیدا می‌کند و امکان انتخاب کشور خروج را می‌دهد.
در حال حاضر
۲۵ کشور
در دسترس است.
🧅
تور
Tor
ترافیک را از چند بازپخش عبور می‌دهد؛ مناسب‌تر برای حریم خصوصی، اما کندتر.
پل نیز پشتیبانی می‌شود و امکان دریافت خودکار پل وجود دارد.
✅
هر سه مسیر با قابلیت‌های زیر کار می‌کنند:
• زنجیرهٔ خروج
• کل دستگاه
• تونل کامل
تنظیمات قبلی شما تغییری نکرده است. اگر چیزی را تغییر ندهید، برنامه مثل قبل کار خواهد کرد.
⬇️
دانلود نسخه دسکتاپ
https://github.com/WhiteDNS/WhiteAesther/releases/latest
📖
آموزش کامل مسیرهای خروج جدید
برای مشاهده، بخش زیر را باز کنید
👇
۱️⃣ انتخاب راه خروج
وارد این بخش شوید:
پیشرفته ← مسیرها و پروتکل‌ها
در کارت
«راه خروج»
سه گزینه دارید.
اِتر
Aether
همان حالت قبلی و سریع‌ترین مسیر.
سایفون
Psiphon
پیدا کردن خودکار مسیر و امکان انتخاب کشور خروج.
تور
Tor
مناسب‌تر برای ناشناس‌ماندن، اما کندتر.
مسیر موردنظر را انتخاب کنید و سپس
اتصال
را بزنید.
⚠️
در حالت سایفون و تور، تنظیمات نقطهٔ پایانی و انتخاب پروتکل اثری ندارند؛ این موارد فقط مخصوص اِتر هستند.
━━━━━━━━━━
۲️⃣ انتخاب کشور خروج در سایفون
بعد از انتخاب سایفون، گزینه
«کشور خروج»
ظاهر می‌شود.
🔸
در اولین استفاده ممکن است فقط
«بهترین گزینه موجود»
نمایش داده شود.
این طبیعی است؛ فهرست کشورها بعد از اولین اتصال موفق دریافت می‌شود.
🔸
انتخاب کشور یک ترجیح است، نه تضمین.
بعضی کشورها ظرفیت کمتری دارند و ممکن است اتصال به آن‌ها موفق نشود.
اگر یک کشور متصل نشد، گزینه
«بهترین گزینه موجود»
را انتخاب کنید تا سایفون از تمام سرورهای قابل دسترس استفاده کند.
🔄
تغییر کشور نیازمند اتصال مجدد است.
━━━━━━━━━━
۳️⃣ تور و پل‌ها
بعد از انتخاب تور، بخش
«پل‌ها»
نمایش داده می‌شود.
خاموش
اتصال مستقیم به تور.
همراه برنامه
استفاده از پل‌های داخلی.
گزینه‌های ترابرد:
obfs4
snowflake
meek
چسبانده‌شده
برای وارد کردن پل شخصی.
در این حالت می‌توانید پل را دستی وارد کنید یا گزینه
«از تور پل بگیر»
را بزنید.
🔑
هنگام دریافت پل، کشوری را وارد کنید که از آن متصل هستید.
مثال:
IR
منظور کشور فعلی شماست، نه کشوری که می‌خواهید آی‌پی خروجی آن را داشته باشید.
💡
ابتدا با اِتر یا سایفون متصل شوید و بعد پل بگیرید.
پل‌های جدید به فهرست اضافه می‌شوند و موارد قبلی حذف نمی‌شوند.
━━━━━━━━━━
۴️⃣ نکته مهم درباره تور
تور فقط ترافیک زیر را عبور می‌دهد:
TCP
برنامه درخواست‌های ناسازگار را مدیریت می‌کند تا اتصال بی‌دلیل معلق نماند.
برای بازی، تماس تصویری و استفاده‌های حساس به تأخیر، اِتر یا سایفون انتخاب مناسب‌تری هستند.
━━━━━━━━━━
۵️⃣ اگر راه خروج قطع شود
اگر پردازش سایفون یا تور متوقف شود، وایت‌اِستر آن را تشخیص می‌دهد، وضعیت را
«خطا»
نشان می‌دهد و زنجیره اتصال را می‌بندد.
اگر گزینه
«اگر تونل قطع شد، ترافیک را مسدود کن»
فعال باشد، ترافیک بسته باقی می‌ماند تا خارج از تونل ارسال نشود.
برای بازگرداندن اتصال، ابتدا
قطع اتصال
را بزنید.
❓
اگر سؤال یا مشکلی داشتید، در گروه وایت‌دی‌ان‌اس مطرح کنید.
@whitedns</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1741" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1740">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/T6o3eeoekGI507DbvASBaOVZ5ZQkHUPL1dz_92c7FCZiN5RE7dMFrH14RyrwQ2fgzU0oGd3rNbnzx2vCWlTExB8OmbWFY1eOI4e5QFjEFKhlFbBRaflO0fITg3OlUNRBSTD5aUpOWaco2cCO0YJvUuAV_mmCfhDHm6UqVgm5O9qjIfohkVH6UghpKoAeT_A9U_Qjauj3JyvlzBBKX05yOt8lx_9UKiQK0JI0e6AYWVQJzKxn9kpYi2TvXp7nD9o1wPu4TGiZgB4cndB21rmy8l0gzJhpy7GB-2mNCc4OPyR1dtRX7mO6jWDsrZ8tIeXshj5ogBStf1YtbwF6g5La5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon
🔥
@whitedns</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1740" target="_blank">📅 11:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1738">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-poll">
<h4>📊 سرور های اختصاصی براتون وصل میشن؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1738" target="_blank">📅 11:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1737">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzYCNpuEtUK4BTHxaSrmFd0uFwA78xHJ9O5RiJorVL0nS-QX6TuTbNtjj-9NjdehbQoC9Ua1r0UzdepTYqcv1YNZO-8DpV2Q4q9Xu0Z7EvXt3ORjG7caOiR8QQpR0qp-GzaqlBwnc6BKWrWW7Vsg8UBavOGKXCSx2jUFUvG8-MmWNYbjgsxz0J1qEjS0F8pYsqmW_PXASgz4-9sBZQhzwvvHxbB47GLrAk7QibgR5fXHok1pXxglnvPPkhG54_JvG6g4a69e_RZDuXVRl3AGFt0A1oStMM0IUGstaoKMmu7rc8qKHQzLN0fkn9KiM-6F9KDSHCv89ORDahOzjrEbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
💬
Support Bot:
@WhiteDnsResponder_bot
🔗
WhiteDnsChain
@WhiteDnsChainbot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1737" target="_blank">📅 08:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1736">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">از دیروز تا حالا تعداد اتصال‌ها چند برابر شده؛ از کامنت‌هاتون هم معلومه که این تغییر رو حس کردید
🙌
جالبه بدونید ما با فقط ۱۰ تا سرور و ماهی ۱۵۰ دلار هزینه، داریم هر هفته به حدود ۵۰ هزار کاربر فعال داخل اپ WhiteVPN، رایگان سرویس می‌دیم!
این تازه بدون حساب کردن کاربرهای ویندوزه؛ با اون‌ها، آمار خیلی بیشتر هم می‌شه.
😑
آدم این عددها رو که می‌بینه، بیشتر حرص پول‌هایی رو می‌خوره که تا امروز به فیلترشکن‌فروش‌ها داده
واقعاً ممنون از انرژی مثبتی که بهمون می‌دین و وقتی که می‌ذارید تا تجربه‌هاتون رو زیر پست‌ها بنویسید. همین بازخوردها کمک می‌کنه بفهمیم کجا خوب پیش رفتیم و کجا هنوز باید بهتر بشیم.
به‌زودی WhiteVPN Desktop رو هم با سرورهای اختصاصی آپدیت می‌کنیم تا کاربرهای دسکتاپ هم از این اتصال‌ها استفاده کنن.
🎮
یه سورپرایز هم برای کاربرهای WhiteAesther و بچه‌هایی داریم که دنبال سرویس مخصوص گیمینگ بودن
ممنون که کنارمونید
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1736" target="_blank">📅 06:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1735">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ما سعی میکنیم هر ۲
یا
۳ روز سرور هارو عوض کنیم تا تا جای ممکن از فیلتر شدن آی‌پی ها جلوگیری کنیم
.
همچنین کشور های دیگه رو هم اضافه میکنیم تا آپشن های بیشتری داشته باشید
❤️
🛡
سرور های اختصاصی رایگان، امن و مدیریت شده توسط
تیم ما هستن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1735" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1734">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید. امیدوارم همه بتونید به سرور های اختصاصی وصل بشید.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1734" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1729">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">36.1 MB</div>
</div>
<a href="https://t.me/whitedns/1729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/whitedns/1729" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1728">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDzOMevjIMZOgcW8d6pnCHeim4gFDL162yPLNti_7wz43pj_oNnmfVYMKOYZ74K0NKUuOW-m7wqSHBZU0ekPQzH_596w1Shv5yMVNYavolakFTrbK5snbZ8eDC09IU5-58YZySRuyCCoPjYGsAbdHnJjNtxxV0BqC6bmRb-7rHEApcjPqy_gYm2EoZGp1n0WBX1OtDaNs-6bFn5dMmPSQ3m9HDWWzUyOrNS27xb1mI4KAgVdrJ0NCaugy5IuUxdPD_N5q5_0RsQ13bhcd1zmbYbn1PDRzHuJW3pgNRNhLaPPdNxXyIua4eOSMqb5QVnQKD4vZQk4WIj2smdd9JwI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
🟢
توی این نسخه ما ۱۰سرور اختصاصی WhiteVPN گذاشتیم. همه داخل فنلاند هستند.  بعد از تست کردن سرور کشور های دیگه رو هم اضافه میکنیم.
در صورت فیلتر شدن سرویس ها، سرور هارو جایگزین میکنیم.
🟢
توی این ورژن، اپ اول سعی میکنه به سرور های اختصاصی WhiteVPN وصل بشه، در صورتی که امکان‌پذیر نبود بعد سرور های عمومی رو امتحان میکنیم.
📱
دانلود آخرین نسخه از گیتهاب
✍️
دوستانی که ورژنی که دقیقه هایی پیش فرستادیم رو گرفتن، دوباره دانلود و نصب کنید.
❤️
نتیجه اتصال رو برای ما بفرستید.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1728" target="_blank">📅 14:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✍️
یه زودی یک آپدیت جدید داریم برای WhiteVPN روی اندروید.
توی این ورژن سرور های اختصاصی WhiteVPN رو اضافه کردیم. برای شروع ۱۰تا سرور اختصاصی فنلاند به صورت آزمایشی اضافه کردیم.
اگر بازخورد ها خوب بود، سرور های کشور های مختلف رو اضافه میکنیم.
توی این ورژن جدید، اپ اپل سعی میکنه به سرور های اختصاصی ما وصل بشه، بعد میره روی سرور های عمومی.
خیلی زود برای دستکتاپ هم آماده میشه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1725" target="_blank">📅 13:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚀
نسخه جدید WhiteDNS Clean IP Finder منتشر شد — v1.4.3
این آپدیت، قابلیت‌های جدید و اصلاحات مهم نسخه‌های v1.4.1 تا v1.4.3 را یک‌جا ارائه می‌دهد.
✨
مهم‌ترین تغییرات:
⚡️
اضافه شدن حالت اسکن سریع
Fast Scan Mode
🌐
اضافه شدن انتخابگر شبکه‌های Edge
Edge Network Picker
☁️
پشتیبانی از سرویس‌های مختلف از جمله:
Cloudflare • Cloudflare Pages • Vercel • Render • Railway •
Fly.io
• Netlify • Koyeb • Glitch
🎯
اسکن هوشمند بر اساس دامنه‌های اختصاصی هر پلتفرم، برای پیدا کردن IPهای واقعاً قابل استفاده
🔐
افزایش دقت در اسکن‌های Scoped با بررسی معتبرتر Certificate و پاسخ دامنه
🌍
اصلاح تشخیص روی Port 80 و جلوگیری از نتیجه‌های اشتباه مبتنی بر CDN Header
🚂
بازگشت دامنه
railway.app
به دامنه‌های شناسایی Railway
🛠
بهبود منطق اسکن، افزایش دقت نتایج و رفع چندین باگ
📱
💻
نسخه‌های منتشرشده برای:
Android • Windows • Linux • macOS • Termux
اگر هنوز از نسخه‌های قبلی استفاده می‌کنید، پیشنهاد می‌شود مستقیماً به v1.4.3 بروید.
🔗
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.4.3
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1724" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب
https://youtu.be/h920xIQCMP4?si=gjpsrzgky62iOy25
@whitedns</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1723" target="_blank">📅 20:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">موقت :
دوستان گرامی ، اون کانفیگ هایی که ما توی ربات
@WhiteDnsChainbot
می‌دیم خدمت شما برای
"exit chain
" هست ,
توی v2ray و بقیه آپ ها میزنید و بعد پیام میدید چرا کار نمیکنه ؟ خوب معلومه نباید کار کنه
روزی ۱۰۰ - ۲۰۰ پیام اینجوری داریم میگیریم ،و نمیشه هی تکرار کرد ، خواهش میکنم قبل از استفاده از هر چیزی مطالب کانال را مطالعه کنید ،
پست زیر را بخونید خواهشاً ،
https://t.me/whitedns/1608
اگر موردی هست که سوال دارید و جوابتون را پیدا نکردید  از ربات پاسخگو بپرسید
@WhiteDnsResponder_bot
@whitedns</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1721" target="_blank">📅 13:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">📦
WhiteDNS Tools — Downloads
━━━━━━━━━━━━━━━━━━
📱
WhiteAesther
• Mobile:
https://github.com/WhiteDNS/WhiteAestherMobile/releases
• Desktop:
https://github.com/WhiteDNS/WhiteAesther/releases
━━━━━━━━━━━━━━━━━━
🛡
WhiteVPN
• Mobile:
https://github.com/WhiteDNS/WhiteVPN/releases
• Desktop:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases
━━━━━━━━━━━━━━━━━━
🌐
WhiteDNS — مناسب دوران قطعی
• Android:
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
• Desktop:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases
━━━━━━━━━━━━━━━━━━
🔎
WhiteDNS Clean IP + Resolver Finder
• Desktop & Mobile:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
━━━━━━━━━━━━━━━━━━
🍎
CoreForge VPN + DNS — iOS
• TestFlight:
https://testflight.apple.com/join/DRkT6zny
━━━━━━━━━━━━━━━━━━
🎓
آموزش‌ها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVPN
https://youtu.be/yx-jFqv9pYM
🛡
آموزش کامل WhiteVPN
https://www.youtube.com/watch?v=tm0ls3r4ppw
📱
آموزش کامل WhiteAesther
https://www.youtube.com/watch?v=cRfqxbDY1Dg&t=1s
🌐
آموزش کامل WhiteDNS
https://www.youtube.com/watch?v=tz8cj7HzHVI
🍎
آموزش کامل CoreForge
https://www.youtube.com/watch?v=filwdiPKN90
🔎
آموزش کامل اسکنر WhiteDNS
https://www.youtube.com/watch?v=N5hKuWXp37w
━━━━━━━━━━━━━━━━━━
@whitedns
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1718" target="_blank">📅 20:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1712">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/KHVuYE_KeAhmW5AOynpg65XmjpbvISj3EWyb1smtBwWaJuyLZERYPJ-7YQ04E48MSB7FIWXCtu3YZhrzqUiGIdnZyumOUO1GWSsmPMdkB1hmmG53lNe0maT53lq5asZLfGRXTxh8-qaBAXrGjJR8njfGclwDs0WUoPQ4DM1YSOFmjZtnxv_vSa3cX1bs-rPPIxDF3sruOMavOaAQ060i_Rn_6iPUjQHiAdq_CWXm6yOoRUcMYT-QcJH8PAQg7krQi36_1QIfT6XP83SY8BISgFH-7j29fWkDMEddAAyRH2BXUV2EZPhbdKLOwDoDpIwar_Tjf6vNLhACk4dvap8kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1712" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1711">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/f-3W6N19VIg8cjvjh2FLehNJ2Qaihy67_lrPI3lO4Ul6_hRAYgNh60WAU3HJA8Msa4_vT42McUoXlbZ-IiaDD3ATXsImn-xBl_d8xjG0a5uiu1It91iRufE6YsyzJKq_5Qd20GwfA1Vp6FAReweM8PlCN3cA7kEEhD_ssYtraPeBE0pJNIWaC9W-NaSW4-lUlx9D7-h22bbhDybePqB_YGWCUf_9w9vUA1N-9mL82Rr8gMZ-R_PjiD2aHVZBrBm8_k5330RBswjFBkeSKhrb-KcjPGC9XGDv-pyd4_SclQmPDQyYA9kBtaN1NZxQGkDOf2BLGD36x65M8J4A9T2gOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/whitedns/1711" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1710">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">WhiteAesthe Desktop 1.7.1 — حالا کامل فارسی منتشر شد
🔥
🔥
از این نسخه، تمام برنامه فارسی است. نه فقط صفحهٔ اول — تمام تنظیمات پیشرفته، زنجیرهٔ خروج، جستجوگر دروازه و پیام‌های وضعیت.
اگر انگلیسی بلد نیستید، دیگر لازم نیست حدس بزنید کدام کلید چه کار می‌کند.
━━━━━━━━━━━━━━━━━━
🔤
چطور فارسی کنم؟
هیچ کاری لازم نیست.
اگر ویندوز یا سیستم شما فارسی است، برنامه خودش بالا می‌آید فارسی.
اگر می‌خواهید دستی عوض کنید: بالا سمت راست پنجره، کنار آیکون تنظیمات، دکمهٔ فا را بزنید. برای برگشت به انگلیسی همان‌جا EN را بزنید.
انتخاب شما ذخیره می‌شود و دفعهٔ بعد هم همان می‌ماند.
━━━━━━━━━━━━━━━━━━
📐
کل چیدمان راست‌به‌چپ شد
فقط کلمه‌ها ترجمه نشدند — منوی کناری، ردیف‌های تنظیمات، دکمه‌ها و نوارها همه به سمت راست منتقل شدند، همان‌طور که یک فارسی‌زبان انتظار دارد.
سه نکته که عمداً برعکس نشدند:
• نمودار تأخیر — زمان همیشه از چپ به راست می‌رود، هر زبانی که باشد. اگر آینه‌اش می‌کردیم، «اکنون» سر قدیمی‌ترین نقطه می‌افتاد. • اعداد لاتین ماندند — آی‌پی، پورت و میلی‌ثانیه با ارقام فارسی خواناتر نمی‌شوند، بدتر می‌شوند. ارقام فارسی فقط داخل متن‌ها استفاده شده‌اند. • اسم‌های فنی — MASQUE، WireGuard، DNS، TLS و مثل این‌ها دست‌نخورده ماندند. ترجمه‌شان فقط گیج‌کننده بود.
━━━━━━━━━━━━━━━━━━
🔍
جستجوی تنظیمات، هر دو زبان
Ctrl + K را بزنید و تایپ کنید.
فارسی تایپ کنید یا انگلیسی — هر دو کار می‌کند. اگر اسم انگلیسی یک تنظیم را از قبل بلدید یا در یک پست انجمن دیده‌اید، لازم نیست معادل فارسی‌اش را حدس بزنید.
مثال: هم «مسیرها» جواب می‌دهد، هم routes. هم «تونل کامل»، هم full tunnel.
━━━━━━━━━━━━━━━━━━
⚙️
موتور به Aether 1.8.0 ارتقا پیدا کرد
چهار مورد که مستقیماً به کار شما می‌آید:
۱. پروکسی بالادستی با یوزر و پسورد — اگر در تنظیمات «اتصال از طریق یک پروکسی محلی» را با نام کاربری و رمز پر کرده بودید، موتور در نسخهٔ قبل رمز را اصلاً نمی‌فرستاد. درست شد.
۲. تونل WireGuard بعد از یک خطای داخلی بالا نمی‌آمد و تا ری‌استارت کامل برنامه برنمی‌گشت. چون پیش‌فرض ما WireGuard است، این را احتمالاً دیده‌اید.
۳. حالت WARP in WARP کرش می‌کرد و بعدش دیگر وصل نمی‌شد.
۴. یک آسیب‌پذیری امنیتی شناخته‌شده در یکی از کتابخانه‌های رمزنگاری حذف شد.
━━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
ویندوز · لینوکس (deb / rpm / AppImage) · مک (اینتل و اپل سیلیکون)
از این نسخه به بعد، وقتی آپدیت جدید بیاید خود برنامه بالای صفحه به شما خبر می‌دهد.
━━━━━━━━━━━━━━━━━━
💬
اگر ترجمه‌ای به نظرتان نامفهوم یا اشتباه است، همین‌جا بگویید — عوضش می‌کنیم.
@whitedns</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1710" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1709">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎉
نسخهٔ ۱٫۳٫۰ WhiteAesther android منتشر شد —
برنامه فارسی شد
بزرگ‌ترین تغییر از زمان انتشار .
🔥
رابط کاربری کامل فارسی
همهٔ برنامه، حدود ۴۵۰ عبارت — از صفحهٔ اول تا تنظیمات پیشرفته، اعلان‌ها، و کلید تنظیمات سریع.
زبان را خودتان انتخاب می‌کنید، نه گوشی. در تنظیمات ← زبان سه گزینه هست: سیستم، English، فارسی.
چرا مستقل از گوشی؟ چون این دو برای خیلی‌ها یکی نیست: گوشی‌ای که انگلیسی مانده چون همه‌جا همین‌طور فروخته می‌شود، ولی صاحبش فارسی می‌خواند — و برعکس، کسی که گوشی‌اش فارسی است ولی اصطلاحات انگلیسی را ترجیح می‌دهد.
🔤
فونت وزیر
متن فارسی با فونت وزیرمتن نمایش داده می‌شود، با فاصلهٔ سطر تنظیم‌شده برای خط فارسی.
فونت داخل خود برنامه است، نه اینکه هنگام اجرا از اینترنت گرفته شود. برنامه‌ای که کارش نفرستادن ردپا از شماست، نباید برای یک فونت درخواستی بفرستد که نام دستگاه شما را ببرد.
🔢
عددها
در متن، عدد فارسی. در مقادیر فنی — آدرس IP، پورت، سرعت، مدت اتصال — عدد لاتین.
آدرسی با رقم فارسی نه خوانا است و نه قابل کپی.
🐞
دو کرش وارپ‌در‌وارپ رفع شد
▫️
موقع قطع شدن: برنامه هنگام پایان نشست ناگهان بسته می‌شد.
▫️
موقع وصل شدن: همان موردی که در ۱٫۲٫۷ رفع شد و اینجا هم هست.
⚙️
هستهٔ Aether به ۱٫۸٫۰ رفت
کتابخانه‌های رمزنگاری به‌روز شدند و خواندن هدر پروکسی سریع‌تر شد.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
💬
اگر ترجمه‌ای به نظرتان نارسا بود یا جایی متن از کادر بیرون زد، همین‌جا بگویید. زبان چیزی است که فقط با استفادهٔ واقعی درست می‌شود.
@whitedns</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1709" target="_blank">📅 16:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1708">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObuYmcvPjJ6DaVkD4Z-RWpFNXYGfvOGkUii5r9zEMN8F5jJThClf3GDX6sNrv5o0qX6ucIW5qVlIiaacW65k2IFqz-YSyevycrs8l-HkIyIDzRlsUOsfasmKtRMy-6P-RtTQaHwZ1qCIVcBxnQTRO0yqxRlFZVNm4hOVmk_cUVPPtC20cKOnKNVydL7NT3MuVJ5XpGQoVCO2pzQL_aDlHXMd9HNbpPNMHWpVkF8jjzO831lJ76vcPiwhB2mkD_itLUp7K9QPKSXTYVCDv5vMu7OJzhHXd-OO2kf7D9x6R9SUPnLXUGHGj12ZzJSmTkF9WWfoelE7PkkbixWCcgEmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
این هم یکی دیگه از تست‌های موفق ما بود؛ تستی که با همراهی و بازخوردهای شما، کنار هم مشکلاتش رو برطرف کردیم.
👑
بیش از ۶ ساعت اتصال پایدار و بدون قطعی
به‌زودی ظرفیت سرورهای اختصاصی WhiteVPN رو چند برابر می‌کنیم. این سرورها فقط از طریق خود اپلیکیشن در دسترس شما قرار می‌گیرن.
تیم WhiteDNS، یک تیم کوچک و با محصولاتی کاملاً رایگانه و هیچ درآمدی از کاربرانش نداره؛ تنها پشتوانه‌ی ما، حمایت شما از کانال یوتیوب و یوتیوب WhiteDNSـه.
❤️
ممنون که کنارمون هستید و کمک می‌کنید این مسیر رو ادامه بدیم.
به امید روزی که نیاز به هیچکدوم ازین ابزار ها نداشته باشیم.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1708" target="_blank">📅 16:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1697">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/whitedns/1697" target="_blank">📅 18:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1695">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1695" target="_blank">📅 17:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1694">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616b32759e.mp4?token=Ah50hOv1JDAwWTLUsZE0_7QKLtDeqhZ7iF8jlOveHCIwq5uRfrSkpUpXZmancHSf5j0yqMb9yjRmFMsef2cSlAmFppN2lNsdRPOhTbIEkvsKoCnHPmJt_6pMyQ6nXniumVsjbDh-VbXZ47RvsVxR4oxJ1ynDQpE0yZY6w_HADGT54Z4Fr21kVTV0Dsruhb3YagkWrntplg6ZNe8XDEUHeVQBHTRDjSflqBBo__OWEzzZ68l06SBTV5lV4N34X_Wsys-OSXpyvBCWnFGu1V1xYvypzYUEMZYQw1KQvFQCa6iIDTeMyyqDQ6VuXoQLiw2I1aatXUhE_edc6lhVd68uOFj0N4bBSdoi05OaXmyp5azkYQacW0LtEAR27BHAZZiMju-2rvXqSTlXM6WGqxUy-ytHmyGYzPueFapV65qN5V984gB6F1kWVyR3QdYrF7eJF8zWh0Wx00xwDds90-Mg_LdBEfi6rJ_iuVNPKTXugx_I_WK3Q7WkCNM88hi_6VpZQ0rzm9kiCf6vgOQYeCatMVMLAlL-YJejce1Ko_8uJOP45kC6TJu7NtPkzQ9ZQBubLaoSvCOoKPJ0S3xS5dsNbai1lMieMVowIiJ0iBGUYKBLS7n_QgEA1a2ZNzmVSeWR3FM-Y4ErO7rQqA531mOULiqta3Pn8HwLWJHfoZKCEZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616b32759e.mp4?token=Ah50hOv1JDAwWTLUsZE0_7QKLtDeqhZ7iF8jlOveHCIwq5uRfrSkpUpXZmancHSf5j0yqMb9yjRmFMsef2cSlAmFppN2lNsdRPOhTbIEkvsKoCnHPmJt_6pMyQ6nXniumVsjbDh-VbXZ47RvsVxR4oxJ1ynDQpE0yZY6w_HADGT54Z4Fr21kVTV0Dsruhb3YagkWrntplg6ZNe8XDEUHeVQBHTRDjSflqBBo__OWEzzZ68l06SBTV5lV4N34X_Wsys-OSXpyvBCWnFGu1V1xYvypzYUEMZYQw1KQvFQCa6iIDTeMyyqDQ6VuXoQLiw2I1aatXUhE_edc6lhVd68uOFj0N4bBSdoi05OaXmyp5azkYQacW0LtEAR27BHAZZiMju-2rvXqSTlXM6WGqxUy-ytHmyGYzPueFapV65qN5V984gB6F1kWVyR3QdYrF7eJF8zWh0Wx00xwDds90-Mg_LdBEfi6rJ_iuVNPKTXugx_I_WK3Q7WkCNM88hi_6VpZQ0rzm9kiCf6vgOQYeCatMVMLAlL-YJejce1Ko_8uJOP45kC6TJu7NtPkzQ9ZQBubLaoSvCOoKPJ0S3xS5dsNbai1lMieMVowIiJ0iBGUYKBLS7n_QgEA1a2ZNzmVSeWR3FM-Y4ErO7rQqA531mOULiqta3Pn8HwLWJHfoZKCEZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✍️
اگر WhiteVPN فقط با زدن دکمه 《اتصال》 براتو کار نمیکنه، میتوین کانکشن هارو دستی تست کنید و بعد وصل بشید.
⛏
این ویدیو ۱دقیقه بهتون یاد میده چطوری این کار رو انجام بدید.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/1694" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1693">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvLWGUezfXllHsmC2WdpY3CIEKBqIPZNHiY5QB8p1zdFQ9egGr57h2b6fZXIpZjMPhhAt97R7ymHLT9tBuR1uJQCBYbge6GViTlZvbRgKygsNWGk5xQQLGrrbhJjp3xKheAXFihuQETWAPd-Yvogvv_-fmPKBODjfeaSMO5ZXQUU1_TuFrzL934458yAzel7Ow0k6Zs6KR6Sk30Tx1q_iTC5Sx5vEjAco2UvFbTmATGPRhLHAbRPohuc1BeqXWklLVVMMGyDTO5TGYo7ItLXDTlcDaquUsvjFpBNHPcSQqyS49BFOA25y_Z4HOET_Cra2L8BltNFY02HORDBOZjVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
ما تصمیم گرفتیم محتوی متفاوت در زمینه تکنولوژی داخل
چنل یوتیوب WhiteDNS
بذاریم
این اولین ویدیو متفاوت از موضوع هایی هست که تا  امروز داشتیم و توی این ویدیو دایانا ۵ ابزار کاربردی
و
رایگان هوش مصنوعی برای تولید محتوی در موضوع های زیر معرفی میکنه.
🎙️
Speechma — تبدیل متن به گفتار و ساخت صدای AI به‌صورت آنلاین
🎨
Leonardo AI — تولید تصویر، آثار هنری و تصاویر خلاقانه با هوش مصنوعی
🧪
Google Labs — آشنایی با پروژه‌ها، ابزارها و آزمایش‌های جدید هوش مصنوعی گوگل
📸
Clipdrop — مجموعه ابزارهای هوش مصنوعی برای ادیت و ویرایش عکس
🎶
Suno AI — ساخت آهنگ باکلام و بی‌کلام با استفاده از هوش مصنوعی
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1693" target="_blank">📅 11:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1690">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hD2wDADl6DyO2t46l9GtWtrrI-rFmB5vnUAX6WQt5aHaUONH5GCfoLC3y_nDbI5FLxRlwfenE267eW9qevCXXUONOFl_P3v__P-w-qfjITenb20rHewCYboQaXvGjmge9UkG-spRsRVkAF0Yp9vzmWnf1hfrQgSwgEmCz3aQR5YneHGu9lYAAZdlrK4kwByCQQWcDqo9sGygcUxe4tR2V5c-gXrUMt6Coh3saDNX9bemhRYWHD80ZsxsUl1GxnkiiDr8XOlzKEI-21eotytrrLyWi9W_2SGzuPBFcUD28a1-Kh0WRFzdfgTjCrjI8dV0HsWjj-j2EGVgunBfnP_kwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1690" target="_blank">📅 11:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1689">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚠️
اصلاحیه
نسخهٔ ۱.۲.۷ منتشر شد
اگر نسخهٔ ۱.۲.۶ را نصب کرده‌اید، لطفاً به‌روزرسانی کنید.
🐞
مشکل چه بود
در نسخهٔ ۱٫۲٫۶، اگر پروتکل را روی وارپ‌در‌وارپ می‌گذاشتید و دکمهٔ اتصال را می‌زدید، برنامه بسته می‌شد.
بقیهٔ پروتکل‌ها سالم بودند. فقط وارپ‌در‌وارپ.
🔧
چرا این اتفاق افتاد
در نسخهٔ ۱٫۲٫۶ یک باگ قدیمی را رفع کردیم که باعث می‌شد روی وارپ‌در‌وارپ مرورگرها باز نشوند. برای آن رفع، اندازهٔ بسته‌ها را به عددی تغییر دادیم که این تونل واقعاً می‌تواند حمل کند.
ولی آن عدد از حداقلی که پروتکل IPv6 لازم دارد کمتر بود، و اندروید این حداقل را اجباری می‌کند. نتیجه‌اش این شد که ساختن تونل رد می‌شد و برنامه بسته می‌شد.
یعنی رفع ما مشکل بدتری ساخت: قبلش وصل می‌شد و مرورگر کار نمی‌کرد، بعدش اصلاً وصل نمی‌شد.
بابت این اشتباه عذرخواهی می‌کنیم.
✅
در نسخهٔ ۱٫۲٫۷
حالا وقتی تونل نتواند IPv6 را حمل کند، برنامه آن را روشن نمی‌کند به‌جای اینکه بسته شود.
نتیجهٔ عملی: وارپ‌در‌وارپ فقط با IPv4 کار می‌کند. این محدودیت واقعی این تونل است، نه چیزی که بشود دورش زد.
هم اتصال درست کار می‌کند و هم مرورگرها باز می‌شوند.
به‌جز این، هیچ چیز دیگری نسبت به ۱٫۲٫۶ عوض نشده. تمام قابلیت‌هایی که در پست قبلی گفتیم سر جایشان هستند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1689" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1687">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔗
نسخه جدید اندروید whiteaesther منتشر شد -
🔥
1.2.6
این نسخه یک باگ مهم را رفع می‌کند و بخش زنجیرهٔ خروج را برای فهرست‌های بزرگ بهینه می‌کند.
پایین همه‌چیز با آموزش آمده.
🐞
رفع باگ: مرورگرها روی حالت وارپ‌در‌وارپ باز نمی‌شدند
اگر روی پروتکل وارپ‌در‌وارپ وصل می‌شدید و همه‌چیز درست به نظر می‌رسید ولی هیچ سایتی بالا نمی‌آمد، این همان مشکل بود.
چه اتفاقی می‌افتاد: اپ به گوشی می‌گفت بسته‌های بزرگ‌تری بفرست از آن‌چه این تونل می‌توانست حمل کند. درخواست‌های کوچک رد می‌شدند و هر چیز بزرگ‌تر بی‌صدا می‌افتاد.
برای همین بعضی برنامه‌ها مثل تست سرعت کار می‌کردند ولی مرورگرها نه — مرورگر بسته‌های بزرگ می‌فرستد.
این باگ از نسخهٔ ۱٫۲٫۲ بود و حالا رفع شده.
⚡️
زنجیرهٔ خروج برای اشتراک‌های بزرگ
اگر اشتراک شما صدها یا هزاران کانفیگ دارد، این بخش عملاً غیرقابل استفاده بود. چهار مشکل داشت که همه رفع شدند.
۱) باز شدن صفحه گوشی را قفل می‌کرد
اپ همهٔ ردیف‌ها را یک‌جا می‌ساخت، حتی آن‌هایی که روی صفحه دیده نمی‌شدند. حالا فقط همان‌هایی ساخته می‌شوند که می‌بینید.
۲) دکمهٔ تست همه تمام نمی‌شد
روی هزار کانفیگ حدود شانزده دقیقه طول می‌کشید و هیچ نشانه‌ای از پیشرفت نمی‌داد. حالا دکمه می‌گوید چند تا تمام شده، و همان دکمه متوقفش می‌کند.
۳) فقط چند تای اول پینگ می‌گرفتند
همهٔ تست‌ها یک‌جا فرستاده می‌شدند، یعنی صدها درخواست هم‌زمان از یک تونل. تونل اشباع می‌شد و بقیه به نتیجه نمی‌رسیدند. حالا دسته‌دسته فرستاده می‌شوند.
۴) اتصال، لحظه‌ای گوشی را قفل می‌کرد
اپ کار سنگینی را روی رشتهٔ اصلی انجام می‌داد، دقیقاً وقتی تونل بالا می‌آمد.
🆕
قابلیت‌های جدید در زنجیرهٔ خروج
مسیر: تب Routes ← گزینهٔ Exit chain
🔍
جست‌وجوی کانفیگ
بالای فهرست یک کادر جست‌وجو هست. بخشی از نام را بنویسید تا فیلتر شود. روی فهرست هزارتایی، این تنها راه پیدا کردن یک کانفیگ خاص است.
✅
انتخاب چندتایی
کنار هر کانفیگ یک تیک هست. چند تا را انتخاب کنید تا روی همه‌شان کار کنید.
⚠️
تیک با انتخاب کانفیگ فعال فرق دارد. برای عوض کردن کانفیگی که ترافیک از آن می‌رود، روی خودِ ردیف بزنید نه روی تیک.
🗑
حذف از فهرست
بعد از تیک زدن، دکمهٔ حذف ظاهر می‌شود.
⚠️
نکتهٔ مهم: کانفیگ‌های اشتراک واقعاً پاک نمی‌شوند، چون اپ دفعهٔ بعد دوباره اشتراک را می‌گیرد. اپ فقط آن‌ها را از فهرست کنار می‌گذارد.
اپ تعدادشان را نشان می‌دهد و یک دکمهٔ بازگردانی دارد، تا کانفیگی که ناپدید شده با اشتراک خراب اشتباه نشود.
🏓
دو نوع تست
هر دو دکمه حالا بالای فهرست هستند، نه پایین آن.
▫️
Test all — همه را امتحان می‌کند. روی فهرست بزرگ چند دقیقه طول می‌کشد.
▫️
Test selected — فقط آن‌هایی که تیک زده‌اید.
راه عملی برای فهرست بزرگ: با جست‌وجو چند تا را پیدا کنید، تیک بزنید، و دومی را بزنید. خیلی سریع‌تر از امتحان کردن هزار تا.
📶
مرتب‌سازی خودکار
فهرست خودش مرتب می‌شود: سریع‌ترین‌ها اول، بعد آن‌هایی که هنوز تست نشده‌اند، و آخر آن‌هایی که این نسخه نمی‌تواند به آن‌ها وصل شود.
📺
اندروید تی‌وی
تیک‌های جدید با کنترل تلویزیون و دستهٔ بازی هم کار می‌کنند و حلقهٔ فوکوس دارند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد. از این شروع کنید
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
اگر مشکلی داشتید، از مسیر
Settings
←
Diagnostics
گزارش بگیرید و بفرستید.
@whitedns</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1687" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1683">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نسخه جدید
🎯
WhiteVPN Desktop  منتشر شد -v1.0.20
این نسخه بیشترین تغییرات کاربری چند وقت اخیر را دارد.
سایت‌های ایرانی دیگر از تونل رد نمی‌شوند
بزرگ‌ترین درخواست شما بود: لازم نباشد برای باز کردن بانک یا سامانه‌های دولتی، وی‌پی‌ان را قطع کنید و بعد یادتان برود دوباره روشنش کنید.
مسیر: تنظیمات ← سایت‌هایی که از تونل رد نمی‌شوند
سایت‌های انتخابی مستقیم از خود دستگاه شما خارج می‌شوند. سریع‌تر باز می‌شوند، و آن‌هایی که آدرس خارجی را قبول نمی‌کنند درست کار می‌کنند.
▪️
فهرست از قبل پر است. اولین مورد، کل دامنهٔ کشوری ایران را یکجا می‌گیرد
▪️
دیجی‌کالا، آپارات، ورزش سه، دیوار، اسنپ و شاپرک هم در فهرست هستند
▪️
هر کدام را می‌توانید حذف کنید و هرچه خواستید اضافه کنید
▪️
محدودهٔ آی‌پی هم می‌شود اضافه کرد، مثلاً برای شبکهٔ محل کار
▪️
چسباندن آدرس کامل اشکالی ندارد و بخش‌های اضافه خودکار حذف می‌شوند
پیش‌فرض خاموش است. آپدیت نباید بدون انتخاب خودتان مسیر ترافیکتان را عوض کند، پس اول سوئیچ بالای همان صفحه را روشن کنید.
⚠️
هر چیزی که در این فهرست باشد با آدرس واقعی شما خارج می‌شود، دقیقاً مثل وقتی که وی‌پی‌ان خاموش است. هدف همین است، ولی یعنی هرچه نمی‌خواهید دیده شود جایش در این فهرست نیست.
🪟
یک پنجره، هرچند بار که کلیک کنید
تا حالا هر بار اجرای برنامه یک آیکون تازه در نوار وظیفه می‌ساخت. دو بار، سه بار، و هر کدام یک موتور جداگانه که سر پورت با بقیه درگیر می‌شد.
حالا اجرای دوباره فقط همان پنجرهٔ موجود را جلو می‌آورد. مخصوصاً وقتی پنجره را بسته‌اید و برنامه کنار ساعت است، که از بیرون شبیه خاموش بودن به نظر می‌رسد.
🐧
حالت تونل روی لینوکس
تا حالا فقط روی ویندوز کار می‌کرد. حالا روی لینوکس هم هست و رمز را از طریق پولکیت می‌پرسد. اگر پولکیت نصب نباشد، گزینه اصلاً نشان داده نمی‌شود، به‌جای اینکه باشد و همیشه شکست بخورد.
🎨
رنگ آیکون کنار ساعت
حالا وضعیت اتصال را از رنگ آیکون می‌فهمید، بدون باز کردن پنجره:
🟢
متصل
🟠
در حال اتصال
🔴
ناموفق
⚪️
قطع
🔌
پورت اشتراک‌گذاری روی شبکه
وقتی اتصال را با گوشی یا تلویزیون به اشتراک می‌گذارید، حالا پورت را خودتان تعیین می‌کنید. قبلاً اگر پورت اشغال بود، برنامه بی‌صدا پورت دیگری برمی‌داشت و دستگاهی که تنظیمش کرده بودید به جای خالی وصل می‌ماند.
هر دو پروتکل روی همان یک پورت کار می‌کنند.
🧪
تست همهٔ اشتراک‌ها در یک اجرا
دانلود
ویندوز، مک و لینوکس، همه از این نشانی:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1683" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/p0Ab6Ia3P17TkiOkl3rWx6sWRvHpY5j7eSWWlTw-LRT9z2Q8hKTpD_SOYreeq2SByFOMAxSNZFkFQX2q3jUIzCSbmYE939Sv4rlbLWKIpsAnQMuHpjSNl5qgN37e3oSxJuFF-ubVwUj16zYqmEfmvZHfIDrPVavsaDD7tQBC9SwJj0f43CdgQPfbSB40IqyoqM9qNdqA4y1uaQLmiyOmd0mE2QjAZKr_8YoG2CrqCyy66ndnrSSPvxhOQRUdZy3SBaAdtPzoR6o26FxFd9gVkkVj9U1SR4VL5pHXUCTthU-vq9szJpuBJXCWGl49pWLGvAHAcjO0v2MSLow5bWEAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
نسخه جدید WhiteDNS Clean IP Finder منتشر شد.
🔭
تغییرات اصلی:
🟢
پشتیبانی بهتر از IPv6
🟢
انتخاب IPv4، IPv6 یا هر دو در ASN Scanner
🟢
بهبود حالت‌های Fast و Thorough در DNS Scan
🟢
بهبود DoH / DoT و مدیریت Timeout
🟢
گزارش‌دهی و مرتب‌سازی بهتر نتایج
🟢
بهبود Nearby Discovery برای IPv4 و IPv6
🟢
بهبود نسخه‌های Android و Desktop
🟢
بدون نیاز به تغییر تنظیمات نسخه‌های قبلی
📱
دانلود آخرین نسخه از گیتهاب
📱
تماشا آموزش اسکنر WhiteDNS Clean IP Scanner
⭐️
اگر پروژه براتون مفیده، توی GitHub استارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1680" target="_blank">📅 09:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=cbsGiffSk9Woz3XnPCsax7jrxKk2U5MHkBQOzPWCUiUxg3zaD7HLYs62YArhP-ECojbGwst3lmhnk7hOFUaTTYA5gv45IHP_kR3e8C4ElK4BPgfsUCpHj2ZEwgICg_jmfwjpreNZAyLa_rK4KBAbX0CNh3rWTJ5Kg6Whgy1swoKLlKy7G8aHeGkgXp0Xe0VNyNJmPCwcFj5-BUNIKYkBz2Zlr-AWdI74EbQvBirdpF_H-Bk_TNWhBIkoxekBrdeWKNLkcXvsV1I-POxSvlg5HsWffkY6M2jW4Aw9pGZ2FZA3ATYe-OMljBsQgh4N-U3a9BWFV3PczwQwtret7fxucQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=cbsGiffSk9Woz3XnPCsax7jrxKk2U5MHkBQOzPWCUiUxg3zaD7HLYs62YArhP-ECojbGwst3lmhnk7hOFUaTTYA5gv45IHP_kR3e8C4ElK4BPgfsUCpHj2ZEwgICg_jmfwjpreNZAyLa_rK4KBAbX0CNh3rWTJ5Kg6Whgy1swoKLlKy7G8aHeGkgXp0Xe0VNyNJmPCwcFj5-BUNIKYkBz2Zlr-AWdI74EbQvBirdpF_H-Bk_TNWhBIkoxekBrdeWKNLkcXvsV1I-POxSvlg5HsWffkY6M2jW4Aw9pGZ2FZA3ATYe-OMljBsQgh4N-U3a9BWFV3PczwQwtret7fxucQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
اگر برای باز کردن اپلیکیشن های
x.com
یا اپلیکیشن های AI مشکل دارید، میتونید از داخل WhiteVPN مسیر زیر رو طی کنید
تنطیمات > اتصال ها > یکپارچگی TLS
Settings > Connections > TLS Integrity</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1679" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1676">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1676" target="_blank">📅 10:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1675">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
🔼</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/whitedns/1675" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/whitedns/1670" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/whitedns/1670" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1669">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDJH8xbD-jUHQCduV2wMLnRiBEHTLHhmF2SKcEM5cacMxxZyP13kAhSTSqEEjRCaE_8MBIxej4C9KN9dbyRNOfWDVz9RmVDr62daeZxfXa5bKX7fF0WmKBAGjlw-T9D9fSJjrYNFGzs7J5yKyq0o-NUsAk5Sj3TSmD5voONvPk6aYiSOQPjdF3VojAyK3aCAL3xcGnfF71Pubedheji3yPMaTclPFSinD059Bgod5AtLfV-3EYlih8or-DYthiB5ppYUfxmR7pgyajXui1-dSYYyKnzMrGyAtqboOCJjG-SLODBM--RWxnlr7yX5cSjd2bjoC3rRAI-T2tzjJFSuVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/whitedns/1669" target="_blank">📅 09:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1665">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NVu93HmJYVRKVxBRhJeqArZrP2coIOvugO1SB7Uwh8iAQnB4pcZrNurlCj1ZXFARpOZpmWv9QiJnk09r4hXZXHEgvq3LpE4DyKgmmWO99LzZjH4klb-D69NwA_oVybJiLrJdV1slJZnPggV2B8isz-qVTSVeHpy9ZC_Vye1aD7ubQEije37Qqsxrw5nhZOLWYa-f-TcjrT72u5OEHVeVy7yxdZBGrUG3BpI8ag4NnbNCqWnbLIxcmOTxRAQzE8mT-v8rqkF7KIT9u_iv5HZ1tefNqoLyK6FB_JffUCyDnaG-TILVnCLV7sXsz226oBZXXuL3ANZogyx9TruGBajmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه رسمی و شفاف‌سازی مجموعه WhiteDNS
دسترسی به اینترنت آزاد، پایدار و امن حق طبیعی هر کاربر است. مجموعه
WhiteDNS
با هدف تحقق این هدف و تسهیل ارتباطات، خدمات و زیرساخت‌های خود را در اختیار عموم قرار داده است.
بدین‌وسیله رسماً اعلام می‌گردد:
۱۰۰٪ رایگان بدون هیچ قید و شرط:
تمامی خدمات، سرورها، کانفیگ‌ها، دی‌ان‌اس‌ها و آموزش‌های ارائه‌شده در چنل رسمی
WhiteDNS
کاملاً رایگان بوده و خواهد بود.
عدم وجود هرگونه اشتراک پولی (VIP):
این مجموعه هیچ‌گونه اکانت ویژه، پولی، پلن VIP، یا سرویس اختصاصی فروشی ندارد.
ممنوعیت کامل خرید و فروش:
هرگونه خرید، فروش، واسطه‌گری یا سوءاستفاده مالی از نام، کانفیگ‌ها یا سرورهای
WhiteDNS
غیرقانونی، غیرانسانی و نقض صریح قوانین این پروژه است.
هشدار نسبت به کلاهبرداری:
اگر فرد یا گروهی تحت عنوان ادمین، نماینده یا پشتیبان
WhiteDNS
به شما پیشنهاد خرید سرویس، اکانت یا پرداخت هزینه داد، سریعاً او را مسدود (بلاک) کرده و موضوع را گزارش دهید.
تنها مرجع رسمی:
کلیه اطلاع‌رسانی‌ها و به‌روزرسانی‌ها صرفاً از طریق کانال تلگرامی ما منتشر می‌شود:
🔗
کانال رسمی تلگرام:
https://t.me/whitedns
❤️
حمایت شما تنها از طریق معرفی کانال به دوستانتان و اشتراک‌گذاری اینترنت آزاد با دیگران و تماشای ویدیوهای ما در
کانال یوتیوب
و دادن
⭐️
به پست های ما و همچنین boost کردن کانال و حمایت از
گبت هاب
ما  امکان پذیر است
کلیه خدمات  WhiteDNS همواره رایگان در کنار شما می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1665" target="_blank">📅 06:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1663">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔥
درود دوستان عزیز :
با توجه به رای گیری که شد و نظر دوستان عزیز
مقدار حجم روزانه کانفیگ های ربات به
4 گیگ
تغییر کرد
❤️
اگر از این خدمت استفبال شود احتمالا به زودی سرورهای بیشتر با لوکیشن های بیشتر در اختیار شما عزیران قرار خواهد گرفت که هر چه بیشتر امکان دسترسی رایگان شما فراهم شود .
بازم تاکید میکنیم که این کانفیگ ها فقط و فقط برای استفاده در قابلیت " exit chain " در برنامه های whiteaesther و whitevpn است . متاسفانه هنوز یک تعداد زیادی پیام دریافت میکنیم که دوستان میگن چرا این کانفیگ های توی v2rayng , hiddify و .......... کار نمیکنه
.
⚠️
لطفا تمام مطالب پست زیر را با دقت کامل بخونید
https://t.me/whitedns/1608
لازم به ذکر کرد در صورت مشاهده هر گونه سواستفاده از این کانفیگ ها لطفا به ادمین ها گزارش دهید
درصورتی که مشاهده شود که کانفیگ ها توسط افراد سودجو  در حال فروش به دیگران است این خدمت به طور کل حذف خواهد شد - پس خواهشمندیم خودتون در حفظ این امکان کوشا باشید
ربات :
@WhiteDnsChainbot
ارادتمند
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/whitedns/1663" target="_blank">📅 05:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1658">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-poll">
<h4>📊 محدودیت حجم کانفیگ ربات را از 1 گیگ به چقدر تغییر بدیم که برای انجام کارهای روزمره کافی باشه ؟👀</h4>
<ul>
<li>✓ 1.5</li>
<li>✓ 2</li>
<li>✓ 3</li>
<li>✓ 4</li>
<li>✓ همین خوبه☺️</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/1658" target="_blank">📅 13:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1656">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ov4td3sFCuGrfJw0V0jrIaRUJNIf7uxWnEyi-GahFvouTMIE7ef1uCwtEsDLOkiKUTopcq0Pn-fnuS3q9NZJnB4skzlxAN16d50CHmqwwXUJQUC0eC43k5CJymbB5hm9JfZXjpEZy7CLuUS6DLV4IK0j3Dz6LX2C3bG8XaH5zaV8a6IFX9UhUuBD-4nkRdCm6y1sp6aMc709slG00_dna1IcPxifXuJaCFlLO2hpB4KSrx_ZhT-c8bhLludxMMkrdlXL6D-lmmUKN4ssftNXvh_H6gZMtUnzTJCi_nrGhqR9P-wBo08rIYz7ZXLZ8eMFssxJCJHkLIwUjk_3KXEz3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#آموزش
اگر WhiteAesther mobile با یک بار زدن دکمه اتصال وصل نشد، یعنی هنوز باید تنظیمات درست شبکه خودت را پیدا کنی.
📡
این راهنمای کامل را قدم‌به‌قدم بخوان:
📖
https://github.com/WhiteDNS/WhiteAestherMobile/blob/main/docs/GUIDE.fa.md
@whitedns</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1656" target="_blank">📅 09:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1654">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/I19-J3nHOk3IczYPS5O_j4qNJHWxKZ2GrSENfD9yX9yMAkZTNscW2E5q8zmQm7981glMdF8A7-NHtB4m4rxr3OZ8iRUeldJRbqY_B5i7dFMLQpn0vnk0mT4pNdKoYADWN4nTXQuuiiR6UsBZy37SbpfjzQ6lGC6D5d3RRnVckX7d-ZBre3-pndYHJm5DTsoR1AV3_8l3ElqPMPdJYTl0X0f3dNBDT3h4aaeM94sX3iUKMrUsw8Wa7smYGY_vNkWG83zOXnYIscXxc6lbiunuztesxvkoR7ON4RLLc_MJr5KVj7CQRCD5Bvnq7IXO80I9OZWNZmaQIBc5J4Vv3-TGkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان عزیز
👋
چند تا کانفیگ جدید به ربات اضافه کردیم  که شاید بهتر بتونید متصل بشید و برای سرویس های خارجی مشکلات کمتری داشته باشید . کانفیگ ها تست شده است و مشکلی نداره
✅
از حالا به بعد شما میتونید تا
3 کانفیگ
را انتخاب کنید
😃
❤️
لطفا برای اطلاعات بیشتر حتما پست زیر را مطالعه کنید
⚠️
⚠️
https://t.me/whitedns/1608
Bot
🤖
:
@WhiteDnsChainbot
@whitedns</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1654" target="_blank">📅 05:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1653">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qGkKmp_hkMxrfqcpQjCELJ_h2vSHaA0hn-sF7FOPrMt8rVwFlZWpM4JyHfoXqUEVzo-kShMFDDw630jzdLGyNpI3KpOZBApJ3m-HlMbFrqccGQo02MBIsnN3yrQAp0dsr9iI7JkWCd2Ffa9qwSrcx-FPJni7vLIcONhErsv7oV250qm_CFVVriWR2dAv_ubc0BJkhB3LlSFanFA517J55BbPP8XH-ir4HLaK1iPrCCNh3nfVNhWP8wumZpY9fOjJf4nmldrj__WbXiGKDWi43Zd_Ctk6TZUIVFxiqIuekQCJDMSiStq79hmpphh3WuRD48m_MnEEGOPoOw-a2jipXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1653" target="_blank">📅 05:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1652">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ceCy2bV3RpcwXA0eAaQt7Pjd-MX-oCNfzW3RqAUIsA9u7rizIpnSY9EZU2MgI4cLO8z9a-kSy5S5IKoNLhvFb1ovZYGSZRzBegzUSElVhrZcJciuHoaxl-O3NNzhX8AFnp8WwuUP2i6ZjSlks7KmoFxKVgvDYBr0Wvmt0WXsN0uGKtqwanTwib-lA73HbZAA71Qt0MAC9L8xuvlpcnx5CTUUVqxH0OwoaZjOc2IX2yr1kQHp35a4cqES0_ACtR_bRIZ4HTw5Mi6m58ZovjZczTipaEAR8eavUMx4Qtx5IjEN2C8jfHphGurPtuYH0gkNRwRByp1Z9z5UfyVFh3bbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1652" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1651">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/C_Od0BE_srpM2lLn3C3PFFMcNFiGDzvXIeLwWIOhrIt-CmBbUOEAcw39ot1-q2BEFiUdMFS12ScXMD1B32Fj5I5ieaVLvmV3PaeCAbNT4BlE1X-StATfm5_7Tuh8j2WAUzR9MOvj_3DGzl2W0H2jt4Rtg-9PDBtu04eGWPW7p9Yq0MF3zP1fOJF_Gf0W_HgFu-j9kocTF3pPEPY481-yjrpFKuw_4Ws_Qy1n0wFUdEXClUis6GuAo-7I_mKxlE1H6Jub5FwQXKu2fT7XG10PcfOEjZfIlp2-thOdt3c5byi_Um8CBN8P3uoCvpTAM0TdPFQMZiWGRyyb2eawaYBQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
آپدیت WhiteAesther — نسخه 1.2.5
🔥
⚠️
⚠️
⚠️
در این ورژن رفع باگ Android TV انجام شده است و دوستانی که روی گوشی استفاده میکنند لازم نیست اپدیت کنند
⚠️
⚠️
⚠️
مشکل کنترل با ریموت در Android TV برطرف شد. پیش از این، بعد از رسیدن به بخش «Connected for»، امکان حرکت به قسمت‌های پایین‌تر صفحه وجود نداشت.
حالا با دکمه‌های بالا و پایین کنترلر می‌توانید به‌راحتی بین تمام بخش‌های صفحه Home حرکت کنید و اطلاعاتی مثل آدرس، ترافیک مصرفی و جزئیات اتصال را ببینید.
این تغییر فقط مربوط به حالت Android TV است و عملکرد نسخه موبایل تغییری نکرده.
🔗
دانلود رسمی از گیت هاب
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1651" target="_blank">📅 16:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1650">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjEx6PDdSw_NER47AVJKOquAP8cDTSkQK4-Ef_FaWMH9dasIp9F3SOU5j2gkxRjE_mxgn4wLFi3OyK8xYFkLIeAtRVNXBTsuUssKzLeRC64bz3cqfIVQjzUDH-D-sAN5X1CIFW--41GH2k7p6-HGQgD1XJ5NZAbGzlFk845RO1aFmcz43D18Jjpr5lZ4PkaFQAdL3saG57_pu2zb5lSIa3WVENyiFm3ZZz_aFCgiK2Vt031CTMntyJZe6N6gnVGhYZIXnMNJOcPOhB76F-YEbKDUj2j2tjqSTJbZt6DeRWm_myOSNK033Y5OkWZevcW-8ssMLXHFQhNHhP869S4AeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
نسخه Android TV و Google TV برنامه WhiteAesther منتشر شد
از نسخه v1.2.4 به بعد می‌توانید WhiteAesther را روی تلویزیون، TV Box و دستگاه‌های Google TV فقط با ریموت یا دستهٔ بازی کنترل کنید؛ بدون نیاز به صفحهٔ لمسی.
حداقل نسخه موردنیاز: Android 8
🔗
دانلود رسمی از گیتهاب
⚠️
برنامه را فقط از لینک رسمی بالا دانلود کنید.
🦢
🦢
🦢
🦢
🦢
🦢
📥
کدام فایل WhiteAesther را برای تلویزیون دانلود کنیم؟
برای بیشتر تلویزیون‌ها و TV Boxهای جدید:
"WhiteAestherMobile-1.2.4-arm64-v8a.apk"
اگر مدل پردازنده را نمی‌دانید یا فایل بالا نصب نشد:
"WhiteAestherMobile-1.2.4-universal.apk"
نسخه Universal روی دستگاه‌های بیشتری اجرا می‌شود، اما حجم بیشتری دارد.
گزینه‌های دیگر:
• نسخه "armeabi-v7a": مخصوص دستگاه‌های قدیمی ۳۲ بیتی
• نسخه "x86_64": بیشتر برای شبیه‌سازها و بعضی دستگاه‌های خاص
• فایل "AAB": برای نصب مستقیم مناسب نیست
🦢
🦢
🦢
🦢
🦢
🦢
🛠
نصب WhiteAesther مستقیماً روی Android TV
۱. مرورگر تلویزیون یا برنامه‌ای مثل Downloader را باز کنید.
۲. وارد صفحه رسمی انتشار شوید.
۳. فایل APK مناسب دستگاه را دانلود کنید.
۴. فایل را باز کرده و Install را بزنید.
اگر اجازه نصب داده نشد، گزینه Install unknown apps را برای مرورگر یا Downloader فعال کنید.
این تنظیم معمولاً در یکی از مسیرهای زیر قرار دارد:
Settings → Apps → Special app access → Install unknown apps
یا:
Settings → Security → Unknown sources
بعد از نصب، بهتر است این دسترسی را دوباره غیرفعال کنید.
🔗
دانلود نسخه رسمی از گیتهاب</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1650" target="_blank">📅 10:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1649">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEvO6hhRfS6wxpwz2ZwRX3AhPkoUoZ37ADotLif3BpVAGzzZG5AUgh7fkzcvyTsgeDyBo_wC67wqhmN2195aH-9DAj7tfXrniiCoKhnH4_RZx9AtQzA_flLxNd5Zjgh9a2brP9TZ3GIu6js5SbD1OossIA5VH2qm-at7q44M0XW15c94ucFkXkSZWCXylDD2wAqupy0f9uiWmYJamf6SUVgGn6CxzpUzixV2KgSJPWod0hwcd2Cz1H7qgcFJTL3Dc3DAPXFhwiwAtqvcwRGoDg1ycTPFQEHFsGp7JvNrVKKq6T9mvxbr9ATERyO1lGp4YamRulZ_yKNFUw0yX9zZ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
داریم تست های نهایی رو برای WhiteAesther روی AndroidTV  انجام میدی
م</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1649" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1645">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/SgT95T9ZhT00sG_gZEaBGJN8iAgzNMYoW51Xe2CgnT5v24s-gc5-KdQDA9XYVQZamVCBVekdbL09xVELpdegLhm_PYIPta573JFxqSWnrnlZ5H9ngbg3vOE3kn2gOt8WODdk52irl9vJGmfCpfjo_6RD6uXhPtWzf-SB0DdNTnRuNV_veJ75r1QN6vYV7Ef3NT381ie4BUoNpd3cwVigsT3SVTFvXeRGuqrg4qCotBTqH-NQC-9dSF-kWCbIAy_omWQjn3KRlBMHtbE4V3KU3mF1TAcxAf0jiDpnSMa6kilyoyDp1I9VQ3I0TJlifkEPGcB_rcE4qaTgYmZJ4rrD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/YwNAZAmZa8WExM_08yIXQxxuumU3Vntd4wvg0EODHwhb9o_SYsFGqZ0LSB2uiyTNnAOO4Wasod4whjc23AoeC8H3_JEi2x6P4KBwVJBqbyV-tN36IHeR3xsh1FzdghY45xd6TleFT1xvx011DM7PUz0SCyWwxrWdS063PrMWg8GGOACB9im0HLws-evRMSJ_A5DGaiLmzIwz5jbmAX_5Fe4AqCR62kH89V-nsaJxzpeONkkrobveD5ZGEstLg2IhxLcUAouDSGS658RU96Ft-SqPzUVZa0ZNMXktn9mbOx5hyxdKyLxWBJYj2ri0DKif_yPE2odwpUM0A8w5vk1tpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/J-KJ2eSks16P1ozAvjUAOiBlgt5GA9lBWMsXyLwDe9iWRzMG5j2GXsg6ApwaMtpIQRijPkZ0AgljxvOC_oL8nzJAVtgve2qOj5bWAQzK6eOUypw8qOuAt9vEd1z9KJ2p9_2EeriGm3PBPO70cmvsRbvvko0ba_YGtIYEelvFwEnYxG134kIV4iqpBf1BqQsLl8q063UY_cdOA05UL0gwC7trQcBZyrIkbaU8FUWJQluhMst3T5H80TaKc-duYGxnmVBBkPvtoOYtQTvkabbe87cS6hp4KgxLaQKcfY9ihdgkVw9zNDrjmx4inKly_Eev6kYrs0Q4ymbbrJRAzlA5Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/whitedns/1645" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1644">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG/PattN کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  پروژه های خوبی وجود دارند که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1644" target="_blank">📅 06:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1641">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مطالب اموزشی نسخه 1.6.0 دسکتاپ whiteaesther
🔥
🔥
خلاصه :
🔧
تغییرات و قابلیت‌های جدید
▫️
حالت
Full Tunnel
یک کارت شبکهٔ مجازی ایجاد می‌کند تا تمام ترافیک سیستم از تونل عبور کند؛ حتی برنامه‌هایی که تنظیمات Proxy را نادیده می‌گیرند.
▫️
خروج سایت‌های ایرانی از تونل
شامل ۲۹۰۶ رنج IP و ۴۱٬۷۲۹ دامنه ایرانی است که مستقیماً داخل خود برنامه قرار گرفته‌اند و نیازی به دانلود جداگانه ندارند.
▫️
دریافت خودکار دسترسی Administrator
هر زمان دسترسی ادمین لازم باشد، برنامه خودش پیام تأیید ویندوز را نمایش می‌دهد و با سطح دسترسی لازم دوباره اجرا می‌شود. دیگر نیازی به راست‌کلیک و انتخاب
Run as administrator
نیست.
▫️
اطلاع‌رسانی نسخه‌های جدید
در صورت انتشار نسخه جدید، یک نوار اطلاع‌رسانی بالای برنامه ظاهر می‌شود که با یک کلیک شما را به صفحه دانلود می‌برد.
▫️
چهار تنظیم جدید موتور
تنظیمات بیشتری برای موارد زیر اضافه شده است:
Local Proxy
Domain Sniffing
Identity Re-registration
Keepalive
مقدار پیش‌فرض
Keepalive
نیز از ۵ ثانیه به ۲۵ ثانیه تغییر کرده است.
▫️
عبور مستقیم ترافیک شبکه محلی
ترافیک دستگاه‌های داخل شبکه مثل Printer، Router و NAS دیگر به نود خروجی فرستاده نمی‌شود و مستقیماً در شبکه محلی باقی می‌ماند.
▫️
رفع مشکل آیکون‌های مرده در Taskbar
حالا در تمام حالت‌های خروج از برنامه، آیکون آن به‌درستی از Taskbar و System Tray حذف می‌شود.
▫️
حذف اتصال خودکار
برنامه دیگر بدون اجازه کاربر به‌صورت خودکار متصل نمی‌شود. زمان اتصال کاملاً در اختیار شماست.
▫️
باز شدن صحیح پنجره با کلیک روی آیکون برنامه
مشکلی که در حالت اجرای برنامه با دسترسی Administrator باعث می‌شد ویندوز فرمان باز شدن پنجره را مسدود کند، برطرف شده است.
🛡
۱. حالت Full Tunnel — جلوگیری کامل از DNS Leak
تا الان دو حالت داشتیم:
▫️
فقط همین برنامه
▫️
کل دستگاه
مشکل حالت دوم این بود که فقط برنامه‌هایی را پوشش می‌داد که از تنظیمات Proxy ویندوز استفاده می‌کنند.
خیلی از برنامه‌ها این تنظیمات را نادیده می‌گیرند و مستقیماً به اینترنت یا DNS وصل می‌شوند. در نتیجه ممکن بود بخشی از ترافیک خارج از تونل عبور کند.
حالت جدید
Full Tunnel
یک کارت شبکه مجازی ایجاد می‌کند و
تمام ترافیک سیستم
را از تونل عبور می‌دهد؛ حتی برنامه‌هایی که Proxy سیستم را نادیده می‌گیرند.
این حالت بهترین گزینه برای جلوگیری از DNS Leak است.
🔹
روش فعال‌سازی
۱. برنامه را باز کنید و متصل شوید.
۲. پایین صفحه اصلی سه حالت وجود دارد.
۳. گزینه سوم یعنی Full Tunnel را انتخاب کنید.
۴. ویندوز برای دسترسی لازم از شما اجازه می‌خواهد. گزینه Yes را بزنید.
۵. برنامه به‌صورت خودکار بسته و دوباره با دسترسی لازم اجرا می‌شود.
دیگر لازم نیست روی برنامه راست‌کلیک کرده و Run as administrator را انتخاب کنید.
✅
برای تست
بعد از اتصال، سایت زیر را باز کنید:
dnsleaktest.com
سپس گزینه Extended Test را اجرا کنید.
سرورهای نمایش‌داده‌شده باید مربوط به کشور نودی باشند که به آن متصل شده‌اید.
━━━━━━━━━━━━━━━━━━
🇮🇷
۲. خروج خودکار سایت‌های ایرانی از تونل
دیگر لازم نیست برای باز کردن بانک‌ها، دیجی‌کالا، آپارات و سرویس‌های داخلی، هر بار VPN را خاموش کنید.
سایت‌های داخلی معمولاً نیازی به عبور از تونل ندارند. عبور آنها از تونل فقط می‌تواند سرعت را کاهش دهد و پهنای باند نود را مصرف کند.
حالا می‌توانید کاری کنید که:
سایت‌های ایرانی مستقیم باز شوند و بقیه ترافیک از تونل عبور کند.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS → Routing Rules
سپس گزینه زیر را روشن کنید:
Iranian sites bypass the tunnel
لیست موردنیاز داخل خود برنامه قرار دارد و شامل:
▫️
۲۹۰۶ رنج IP ایران
▫️
۴۱٬۷۲۹ دامنه
است.
هیچ فایلی هنگام اتصال دانلود نمی‌شود؛ بنابراین این قابلیت حتی زمانی که دسترسی آزاد به اینترنت ندارید نیز قابل استفاده است.
━━━━━━━━━━━━━━━━━━
📱
۳. اشتراک اینترنت با گوشی، تلویزیون و دستگاه‌های دیگر
حالا می‌توانید کامپیوتر خود را به یک Proxy Server تبدیل کنید و دستگاه‌های دیگر را از طریق آن به اینترنت متصل کنید.
بدون نیاز به نصب WhiteAesther روی گوشی.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS
در بخش:
Share with other devices
گزینه اشتراک‌گذاری را روشن کنید.
برنامه یک آدرس مشابه این نمایش می‌دهد:
192.168.1.24:1080
بار اول ویندوز ممکن است از شما اجازه Firewall بخواهد.
گزینه:
Allow access
را انتخاب کنید.
اگر اجازه ندهید، Proxy فقط روی همان کامپیوتر قابل استفاده خواهد بود.
📱
در Android
وارد تنظیمات Wi-Fi شوید.
شبکه متصل را باز کنید و به بخش تنظیمات Proxy بروید.
حالت Proxy را روی Manual قرار دهید.
برای مثال:
Hostname:
192.168.1.24
Port: 1080
همان IP و پورتی را وارد کنید که WhiteAesther نمایش داده است.
🍎
در iPhone
به مسیر زیر بروید:
Settings → Wi-Fi
روی علامت (i) کنار شبکه بزنید.
سپس:
Configure Proxy → Manual
را انتخاب کرده و IP و Port نمایش‌داده‌شده در WhiteAesther را وارد کنید.
🔐
نکته امنیتی مهم
اگر Username و Password تعیین نکنید،
هر دستگاهی که به همان شبکه Wi-Fi متصل باشد می‌تواند از Proxy شما استفاده کند.
در شبکه خانگی شاید این موضوع مهم نباشد، اما در محل کار، دانشگاه، هتل یا کافه حتماً هر دو فیلد زیر را پر کنید:
Username
Password
خود برنامه نیز در صورت خالی بودن آنها با یک هشدار زرد به شما اطلاع می‌دهد.
یک Port برای هر دو پروتکل استفاده می‌شود:
HTTP
و
SOCKS5
بنابراین همان شماره Port را برای هرکدام که دستگاه شما پشتیبانی می‌کند وارد کنید.
━━━━━━━━━━━━━━━━━━
⚡️
۴. پشتیبانی بهتر از Hysteria2 و TUIC
اگر در Subscription شما نودهای Hysteria2 وجود داشتند و همیشه علامت — نمایش داده می‌شد، این مشکل اکنون برطرف شده است.
مشکل از اندازه Packet بود.
این پروتکل‌ها Packetهایی با اندازه حدود ۱۲۸۰ بایت ارسال می‌کنند، در حالی که تونل قبلی فقط ۱۲۵۲ بایت ظرفیت داشت.
در نتیجه حدود
۲۸ بایت کمبود ظرفیت
باعث می‌شد Packet قبل از ارسال حذف شود.
🔹
روش استفاده
به مسیر زیر بروید:
Advanced → Routes & Transports
سپس Protocol را روی:
WireGuard
قرار دهید.
برای این نودها از MASQUE استفاده نکنید.
در حالت MASQUE این محدودیت از سمت Cloudflare وجود دارد و برنامه نیز کنار نود توضیح می‌دهد که چرا قابل استفاده نیست.
━━━━━━━━━━━━━━━━━━
🔔
۵. اطلاع‌رسانی نسخه‌های جدید
از این نسخه به بعد، وقتی نسخه جدید WhiteAesther منتشر شود، خود برنامه به شما اطلاع می‌دهد.
یک نوار اطلاع‌رسانی در بالای برنامه نمایش داده می‌شود.
با زدن گزینه:
Get it
مستقیماً وارد صفحه دانلود نسخه جدید خواهید شد.
━━━━━━━━━━━━━━━━━━
🔧
سایر تغییرات
▫️
نودهای REALITY حالا با برچسب Not Supported مشخص می‌شوند.
موتور فعلی از آنها پشتیبانی نمی‌کند، بنابراین بهتر است وضعیت آنها واضح باشد تا اینکه نودی نمایش داده شود که هیچ‌وقت متصل نمی‌شود.
▫️
Subscriptionها کامل‌تر پردازش می‌شوند و مشکل جا افتادن بعضی نودها برطرف شده است.
▫️
مشکل باقی ماندن آیکون‌های قدیمی برنامه در Taskbar برطرف شده است.
▫️
برنامه دیگر به‌صورت خودکار متصل نمی‌شود. تصمیم برای اتصال کاملاً با کاربر است.
▫️
تنظیمات بیشتری برای Local Proxy، Keepalive و گزینه‌های پیشرفته اضافه شده است.
▫️
موتور برنامه به نسخه زیر ارتقا پیدا کرده است:
Aether 1.7.0
@WhiteDNS_Laurie</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1641" target="_blank">📅 05:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1640">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JSPPGdaCnmM3KyPdJYeILWIEKZ0UqWCekrnzl4Z14jby3EbW3m3rZo_ygMQ0MNJsvwJgnFWOSkJ3RP7Y03ygDxnmAgnAxfnpzz2-0csiPPMrb9Xi_wccd0X8koPefeiZJw4nqNXHgvsCIcqaSrkhHR3tTiJ42eg_kZ87kXvd7cklsJj-5QgDgcFix1shrQvC6UGEXQr4CWEIz53gKc1TfK_HVXkR2Ld9FibUhZr91PNxXT-Sj-Tny1P8DCQIE_n4GwFXm-gAcBgPti0t6kYziMTAfIUgGZzyoo4wEZe59IzeJBWtvQdX-fQbDF4DVdgzzobPS--mNTga0YvvbOtOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه 1.6.0 دسکتاپ  WhiteAesther منتشر شد
بزرگ‌ترین آپدیت WhiteAesther تا امروز.
حالا می‌توانید:
▫️
کل کامپیوتر را تونل کنید
▫️
سایت‌های ایرانی را از تونل خارج نگه دارید
▫️
اینترنت را با گوشی، تلویزیون و دستگاه‌های دیگر به اشتراک بگذارید
━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
نسخه‌های موجود:
▫️
Windows
▫️
Linux —
deb / rpm / AppImage
▫️
macOS Intel
▫️
macOS Apple Silicon
━━━━━━━━━━━━━━━━━━
⚠️
نکته مهم قبل از تست
اگر برنامه رسمی
Cloudflare WARP
روی سیستم شما نصب است، قبل از استفاده از WhiteAesther حتماً آن را کاملاً
Disconnect
کنید.
اجرای همزمان دو VPN روی مسیر شبکه می‌تواند باعث تداخل، قطع اتصال یا نتایج گیج‌کننده شود.
━━━━━━━━━━━━━━━━━━
💬
اگر سؤال یا مشکلی داشتید، همین‌جا مطرح کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1640" target="_blank">📅 05:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش تغییر لوکیشن با Exit Chain
داخل اپ‌های WhiteVPN و WhiteAesther
🔥
واسه gemini و بقیه AI هایی ک نیاز دارین عالیه
https://youtu.be/yx-jFqv9pYM?si=VuY0qqm5qbFUJOO6</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1636" target="_blank">📅 03:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1634">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔗
نسخه ۱.۲.۳ اندروید WhiteAesther منتشر
شد ......!
در نسخه جدید سه بخش مهم اضافه شده:
🛡
قفل ایمنی
🧭
قواعد مسیریابی
⚙️
چند تنظیم جدید برای موتور اتصال
پایین، همه موارد را همراه با آموزش توضیح داده‌ایم.
🛡
۱. قفل ایمنی — Kill Switch
چه مشکلی را حل می‌کند؟
تا الان اگر تونل بعد از چند بار تلاش وصل نمی‌شد، برنامه تسلیم می‌شد و گوشی بی‌صدا به اینترنت معمولی برمی‌گشت.
حالا می‌توانید مشخص کنید که در چنین شرایطی، به‌جای برگشت به اینترنت عادی،
تمام ترافیک اینترنت مسدود شود.
آموزش
۱) وارد بخش Traffic شوید.
۲) بخش Advanced را باز کنید.
۳) گزینه زیر را روشن کنید:
Block traffic if the tunnel fails
تمام! از این به بعد اگر تونل از کار بیفتد، هیچ ترافیکی از گوشی خارج نمی‌شود.
🔸
حالت سخت‌گیرانه‌تر
بعد از فعال کردن گزینه بالا، گزینه دیگری ظاهر می‌شود:
Keep blocking after you disconnect
اگر این گزینه را روشن کنید،
حتی زمانی که خودتان اتصال را دستی قطع می‌کنید، اینترنت همچنان مسدود می‌ماند
تا خودتان آن را آزاد کنید.
⚠️
توجه:
در این حالت گوشی واقعاً اینترنت نخواهد داشت. اگر فراموش کنید این گزینه فعال است، ممکن است فکر کنید اینترنت یا شبکه مشکل دارد.
برای برداشتن قفل دو راه دارید:
▫️
از نوتیفیکیشن Traffic is blocked
▫️
یا از صفحه اصلی برنامه و دکمه Lift the block
اگر دوباره به تونل متصل شوید، قفل به‌صورت خودکار برداشته می‌شود.
🧭
۲. قواعد مسیریابی — Routing Rules
چه مشکلی را حل می‌کند؟
بعضی سایت‌ها و اپلیکیشن‌ها با IP خارجی درست کار نمی‌کنند؛ مثل بعضی بانک‌ها، اپ‌های داخلی یا سرویس‌های ایرانی.
قبلاً برای استفاده از آنها مجبور بودید VPN را کاملاً خاموش کنید.
حالا می‌توانید مشخص کنید که
فقط بعضی سایت‌ها یا سرویس‌ها از تونل عبور نکنند
و بقیه ترافیک همچنان از تونل استفاده کند.
آموزش
۱) وارد بخش Routes شوید.
۲) در کارت اول، گزینه Routing rules را که زیر Exit chain قرار دارد انتخاب کنید.
۳) دو کادر خواهید دید:
🔹
کادر
Never connect
هر چیزی که اینجا قرار بگیرد، اصلاً اجازه اتصال نخواهد داشت.
مناسب برای مسدود کردن تبلیغات، ردیاب‌ها و دامنه‌های ناخواسته.
🔹
کادر
Skip the tunnel
هر چیزی که اینجا قرار بگیرد،
بدون تونل و با IP واقعی شما
باز می‌شود.
مناسب برای بانک‌ها، سایت‌ها و اپلیکیشن‌های داخلی.
هر قانون را در یک خط جداگانه بنویسید.
مثال:
bank.example.ir
digikala.com
snapp.ir
نوشتن یک دامنه، زیرمجموعه‌های آن را هم شامل می‌شود.
برای مثال:
digikala.com
شامل این مورد هم خواهد شد:
www.digikala.com
حالت‌های پیشرفته
▫️
فقط همان دامنه دقیق:
full:
example.com
▫️
هر آدرسی که یک کلمه خاص داخل آن باشد:
keyword:tracker
▫️
یک محدوده IP:
cidr:
10.0.0.0/8
▫️
یک پورت مشخص:
port:25
▫️
کل شبکه محلی:
private
▫️
هر خطی که با # شروع شود، به‌عنوان توضیح در نظر گرفته شده و اجرا نمی‌شود.
⚠️
مهم:
هر چیزی که داخل Skip the tunnel قرار دهید، با
IP واقعی شما
به اینترنت متصل می‌شود. بنابراین این لیست را فقط برای موارد ضروری استفاده کنید.
🔸
نکته مهم درباره دامنه‌ها
در مسیر زیر:
Traffic ← Advanced
گزینه‌ای وجود دارد با نام:
Match rules on domain names
این گزینه به‌صورت پیش‌فرض روشن است و بهتر است روشن بماند.
اگر آن را خاموش کنید، قوانینی که با نام دامنه نوشته شده‌اند ممکن است کار نکنند؛ چون برنامه در اندروید معمولاً ترافیک را در سطح IP دریافت می‌کند.
در صورت خاموش بودن این گزینه، خود صفحه Routing rules نیز هشدار خواهد داد.
⚙️
۳. تنظیمات جدید موتور
تمام این تنظیمات در مسیر زیر قرار دارند:
Traffic ← Advanced
🔹
تنظیم DNS داخل تونل
گزینه:
DNS inside the tunnel
می‌توانید DNS دلخواه خودتان را وارد کنید.
مثال:
8.8.8.8
,
1.1.1.1
اگر خالی بگذارید، DNS پیش‌فرض موتور استفاده می‌شود.
آدرس‌های نامعتبر نیز به‌صورت خودکار نادیده گرفته می‌شوند.
🔹
اتصال تونل از طریق یک پروکسی دیگر
گزینه:
Dial out through a proxy
این قابلیت یکی از مواردی بود که کاربران زیادی درخواست کرده بودند.
اگر ابزار دیگری روی گوشی شما در حالت پروکسی فعال است، مثلاً
Psiphon
، می‌توانید اتصال WhiteAesther را از داخل آن عبور دهید.
مسیر اتصال به این شکل می‌شود:
گوشی ← WhiteAesther ← Psiphon ← اینترنت
برای مثال اگر پروکسی SOCKS روی پورت ۱۰۸۰ فعال باشد، وارد کنید:
socks5://127.0.0.1:1080
پورت را باید با پورت واقعی برنامه پروکسی خودتان جایگزین کنید.
پروکسی HTTP نیز پشتیبانی می‌شود:
http://127.0.0.1:8080
🔹
تنظیم WireGuard Keepalive
این گزینه می‌تواند روی مصرف باتری تأثیر داشته باشد.
سه مقدار قابل انتخاب است:
▫️
۵ ثانیه
▫️
۱۵ ثانیه
▫️
۲۵ ثانیه
مقدار پیش‌فرض در نسخه جدید
۲۵ ثانیه
است. در نسخه‌های قبلی مقدار پیش‌فرض ۵ ثانیه بود.
هر بار که این زمان می‌گذرد، گوشی یک بسته کوچک ارسال می‌کند تا اتصال فعال بماند.
در حالت ۵ ثانیه، این کار بسیار بیشتر انجام می‌شود و مخصوصاً روی اینترنت موبایل می‌تواند باعث مصرف بیشتر باتری شود.
مقدار ۲۵ ثانیه نیز مقدار رایج استاندارد WireGuard است.
⚠️
اگر بعد از آپدیت متوجه شدید اتصال WireGuard بعد از چند دقیقه بی‌کاری قطع می‌شود، مقدار را دوباره روی
۵ ثانیه
قرار دهید.
🔹
جایگزینی هویت ردشده
گزینه:
Replace a refused identity
این گزینه به‌صورت پیش‌فرض روشن است.
اگر Cloudflare هویت ذخیره‌شده روی گوشی را دیگر قبول نکند، برنامه به‌صورت خودکار یک هویت جدید دریافت می‌کند.
بدون این قابلیت ممکن است تونل ظاهراً متصل شود، اما هیچ ترافیکی از آن عبور نکند.
📌
خلاصه محل تنظیمات
بخش
Routes
▫️
Protocol
— مثل قبل
▫️
Endpoint
— مثل قبل
▫️
Exit chain
— مثل قبل
▫️
Routing rules
—
جدید
بخش
Traffic ← Advanced
▫️
Obfuscation
— مثل قبل
▫️
Local proxy port
— مثل قبل
▫️
Share with this network
— مثل قبل
▫️
DNS inside the tunnel
—
جدید
▫️
Dial out through a proxy
—
جدید
▫️
WireGuard keepalive
—
جدید
▫️
Block traffic if the tunnel fails
—
جدید
▫️
Match rules on domain names
—
جدید
▫️
Replace a refused identity
—
جدید
⬇️
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— مناسب تقریباً همه گوشی‌های سال ۲۰۱۷ به بعد؛
اول این نسخه را امتحان کنید.
▫️
armeabi-v7a
— مخصوص گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید؛ حجم این نسخه تقریباً سه برابر است.
اگر با مشکلی مواجه شدید، از مسیر زیر گزارش بگیرید:
Settings ← Diagnostics
و برای ما ارسال کنید.
@whitedns</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1634" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1632">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ldsImC3nk0cngi7QfZi6x-_su5HVJL5A0FQMM-NBImGAgtuzNXbYCnv2L90nByGEBoWVYLEh8HbGVYcThBKnMm21A-NwVvdI8B-fvrVaOL3KKQ2r8SToWrxdlYPKy7RhRAckTr-m-TMVTplJr56XO0JVACs4FnZnLsjzabt0t2JMm-N_tO-Fnzrd33EYUHvxEWdSo8-CKUXFd8uWaN14d9BFGqjbv_Anf8fJ2WZQF21mRe2y1PWXnzVcSiAZufUkyFhHRXbuzz2XKMZbAYLJXQmAuwNhHKyDAob60rA0TFs-P5wQ20V0w4ocl2R7WIjoXpQngaTjM3K2Dtn864JARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به‌زودی:  WhiteAesther  اندروید نسخه ۱.۲.۳
🔥
🔥
🔥
▫️
قفل ایمنی (Kill switch) — اگه تونل بمیره، ترافیک بی‌صدا لو نمی‌ره
▫️
قواعد مسیریابی — بگین کدوم سایت‌ها بدون تونل باز بشن (بانک، اپ‌های داخلی)
▫️
اتصال یه پروکسی دیگه (مثل سایفون)
▫️
امکان DNS دلخواه داخل تونل (برای کاهش پینگ)
▫️
بهینه‌سازی مصرف باتری روی WireGuard
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1632" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1631">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/B3OhF-B4c6ukYtxUJVrJMYuB7-wGBN0c9sZHaEP9l246d35730hdmHcHGs5Kpd-bi9nXkq8oB3bCnKLXMt1ZLG_jm2m4mT9WfR_iEcDRY81l9bZ3flY7Coe7jTc3XZHrt6W9_jxILH_oirjtzM8Ln3C_PWbOKE1xPDeE35HApJB_dk5ZWgeAHi0KANdRqPA_bw5Jnjo0HRyH-g0asynncbNVbOTYYl3VmtJ41kEJvNtVGy1Fgfg632s59Q93Tgg-guAm5AiQ1bKwAWeQyAwMu5nmwlyC5Y-ZE2F9Ey2bxvs9OfT8CAxfan8Iyjx4Y-5UGx5-apXyM8cRnfm6Do1Glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1631" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1630">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AHz8dzoKP2U8RWVt5-LNumrrNzqb7UXrI4Vk1PusZgqZ0ZzQtsZcVKo2xKolGkmAqiIGyw5A0-r3tc_wHyDxgQWTeB77xSzJQ2w7q8bq9EFLT-uhdbehomphSDE9xOpTQaU9nw1M-OXHEyj2TLqfwczD7qE3AjH2aikXmMjCES7gz53QEWdvn8bSqqYs6cS_KQB18qPKM7kIAa9q9m9cmQe_C-5zIbDOCg7rPrtIK2GqnEVRsqFNGTI08JVgotrpS3wJKrPJetRrT0Gfh-8dEGHCtuW9higxPOlrArnlWA0VPcH2YksGclJgN3jdOyhS9sEG5DHdcZyBOX0jlJncMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1630" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1627">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سابسکریپشن WhiteDNS برای اپ های WhiteVPN / Karing / Clash Mi / Clash Party / FLClash :
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1627" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1626">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1626" target="_blank">📅 18:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1618">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMKfQMDc0n4E4dPXE7xekmrB9acrM1X9PYjWaVm1BC4ftFfkhhkCH1CNGbLM_jmDhOt6-yLgyRhyBv8GrH_WVNADQGM6_OmFM11JMlywXvPppEksnzo3k8Z2ztkm_lwbHuIwbRCoj19gOZx_p5I1Y1h2CpPSNK9MmvkZKSSzzoTbA3YuIDHSVPBk9SLqXq5i5ASjBv0g9KfY0vVAMW5koEsOT7CZVt3HEdFzoJ9Z2V7WQED9MOft9xzLfJKjMy1qG9G6dYpn-KqadftkQny066D4N4w0R9LpFpbCGitlbpRAIbpXSbR1RppMBhFjg89QnoGHg8f_A-iTWbXqzaL_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
یک پورت برای حکومت بر همه!
آموزش نصب و راه‌اندازی CottenRouter
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
اگر روی یک سرور چند DNS Tunnel مختلف داشته باشید، خیلی زود به یک مشکل می‌خورید: همه‌شون پورت عمومی 53 رو می‌خوان.
سرویس CottenRouter دقیقاً برای حل همین مشکل ساخته شده. جلوی تمام سرویس‌ها قرار می‌گیره، دامنه هر درخواست رو تشخیص می‌ده و بدون دست‌کاری Packet، اون رو به Backend درست می‌فرسته.
یعنی می‌تونید CottenDNS، MasterDnsVPN، StormDNS، thefeed و سرویس‌های مدیریت‌شده با SlipGate رو هم‌زمان روی یک سرور و یک IP اجرا کنید؛ بدون جنگ بر سر پورت 53.
✍️
توی این ویدیو می‌بینیم:
• سرویس CottenRouter دقیقاً چه مشکلی رو حل می‌کنه
• مسیریابی درخواست‌ها بر اساس Domain چطور انجام می‌شه
• چطور چند DNS Tunnel روی یک IP اجرا می‌شن
• پشتیبانی از DNS، DoT و HTTPS
• تفاوت نصب مستقیم با Docker
• پنل مانیتورینگ، محدودسازی ترافیک و قابلیت‌های امنیتی
• نحوه نصب و اتصال Backendها
سرویس CottenRouter هیچ Label یا داده اضافه‌ای وارد Packet نمی‌کنه؛ پس فضای قابل استفاده Tunnel و MTU رو هم کاهش نمی‌ده.
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
🔗
سورس‌کد و راهنمای نصب:
https://github.com/TaJirax/CottenRouter
اگر با DNS Tunnelها کار می‌کنید، این پروژه احتمالاً کلی دردسر از مدیریت سرورتون کم می‌کنه.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/whitedns/1618" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔭
یک خبر خوب برای کاربران WhiteVPN
🟢
یک فیلتر جدید به سابسکریپشن
اپلیکیشن ‌های
WhiteVPN اضافه کردیم تا کانفیگ‌هایی که هنگام استفاده از ChatGPT و سرویس‌های OpenAI خطا ایجاد می‌کردند، به‌صورت خودکار از لیست حذف شوند.
🟢
از این به بعد، با تمام کانفیگ‌های موجود در سابسکریپشن باید بتوانید بدون دردسر به ChatGPT و سایر سرویس‌های OpenAI دسترسی داشته باشید.
🟢
برای دریافت لیست جدید، کافی است سابسکریپشن WhiteVPN را یک‌بار به‌روزرسانی کنید.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1616" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/N6X4j1bcEY3nNWMSgLW7rAqyirnRqhRCZxn1Ua57Jb8pZl4nxuJkW7nbKKH6b7ogD5OcwLKBuFVeLT4lt61ZiUzvh4clap2BeMLvP9mEKqLOnD1W323iaRi8W4-Z8xhv4NzmS8J-ZpesE_x21CTImMrTmh8N3i97n6TCDAFl8_pOc9iLXnImEVVjUZvPYBPW7_p6JNp1WFTvAblphI4sDOQPgsxZjB5t-1ewxXPW-Tj2GGILO0KUabqWHFl4GGoLSDpoxGGQAHvCekaJof3xoA-_MeMCAtmkyR6ZUOUeGY-LNdJ7kDFYIbA9qq8hmdgQFK89M8yYx8z03zEXEFlsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1610" target="_blank">📅 11:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1608">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">"exit chain "
⚠️
✍️
راهنمای استفاده از
#exit_chain
در اپ whitevpn# اندروید
ساب را وارد کن - برو تنظیمات - برو زنجیره اتصال - برو افزونه بعد - اشتراکی که وارد کردی را از اون بالا انتخاب کن - یک تست اتصال بگیر - یکی از کانفیگ ها را انتخاب کن - وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# اندروید
📱
برو route - گزینه exit chain را روشن کن - یا ساب و یا کانفیگ را وارد کن - برگرد صفحه اول و وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# دسکتاپ
برو advanced - برو exit chain - ساب و یا کانفیگ را وارد کن - برگرد simple - کانکت را بزن - تمام
✅
👨‍💻
این سه پست را مطالعه کنید :
https://t.me/whitedns/1601
https://t.me/c/3869114465/152008
https://t.me/c/3869114465/151806</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1608" target="_blank">📅 10:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HQ5ADUrd5wdRTia28D2DBU8uTcTO6sWLQaz_-BIuu_s48hi_MX2pj2OiX7XETUtLPPJ4_uVGHL3-2Hom3_bJ0PJMFQNNJuwl1KXPpU9OpneMo5HsawQr8B-5rRMaaqxZRc0Nj03sMIaZqMFZnAXt40eE2gAvmogXioT4-24NmnE94uISHyqMI3xcmuWkpCTIU1UEmeHPq-tqCVHI3dS28X-LWq7S-cuBiBX9ReoA_BTqV7iE9uBniv2dfq-5ULcCinFcaTp4EkMwSb_XKluMy1rZQjoKCOx30Fo_ula2x5sG2lxWuQKCWBOYUuaBv5j-netJ9UdBZTNJXU6-A8ZS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
Wh
iteAesther
✍️
نسخه ۱.۲.۲  برای اندروید منتشر شد !
— موتور جدید و چند قابلیت
این آپدیت موتور تونل رو عوض می‌کنه و چند چیزی که کاربرها خواسته بودن اضافه می‌شه.
🟢
⚡️
موتور جدید (Aether 1.7.0)
▫️
مصرف حافظه محدود شد
— قبلاً هرچی اتصال طولانی‌تر می‌شد، حافظه‌ای که اپ می‌گرفت بیشتر می‌شد تا جایی که تونل می‌افتاد. حالا سقف داره.
▫️
WARP in WARP وقتی یک طرفش قطع بشه دوباره وصل می‌شه
به‌جای اینکه کلاً بمیره.
▫️
پیام خطای واقعی از Cloudflare
— اگه ثبت‌نام رد بشه، حالا می‌گه دلیلش چیه: آی‌پی علامت‌خورده، یا ثبت‌نام زیاد از این آدرس. قبلاً فقط می‌گفت شبکه مشکل داره.
✍️
نودهای hysteria2 و tuic توی Exit chain کار می‌کنن
اگه توی ساب‌تون نود hysteria2 یا tuic دارین و تا حالا هیچ‌وقت بالا نمی‌اومدن، دلیلش پیدا شد و درست شد.
✍️
ولی یک شرط داره:
باید پروتکل رو روی
WireGuard
بذارین (از
Routes ← Manual ← Protocol
).
روی MASQUE همچنان کار نمی‌کنه و این دست ما نیست — محدودیت خود Cloudflareست. اپ هم اگه ببینه روی MASQUE هستین بهتون می‌گه.
🟢
نودهای REALITY حالا مشخص می‌شن
اگه توی ساب‌تون نود REALITY دارین، قبلاً یا اصلاً نمی‌اومد یا می‌اومد و وصل نمی‌شد و معلوم نبود چرا. حالا با برچسب نارنجی
not supported
نشون داده می‌شه و قابل انتخاب نیست.
نود سالمه — موتور فعلی هنوز نمی‌تونه باهاش احراز هویت کنه. وقتی بتونه، خودبه‌خود دوباره کار می‌کنه.
🟢
اشتراک تونل با شبکه (LAN sharing)
می‌تونین تونل گوشی رو با بقیه دستگاه‌های همون وای‌فای به اشتراک بذارین — مثلاً لپ‌تاپ یا تلویزیون.
از
Traffic
حالت رو روی
Proxy
بذارین، بعد بخش Advanced رو باز کنین و
Share with this network
رو روشن کنین. اپ آدرسی که باید توی دستگاه دوم بزنین رو بهتون نشون می‌ده.
⚠️
رمز اختیاریه ولی حواستون باشه:
بدون رمز، هرکی روی اون وای‌فای باشه می‌تونه از تونل شما استفاده کنه و ترافیکش با هویت شما بیرون می‌ره. روی شبکه خونه خودتون مشکلی نیست؛ توی کافه و هتل و خوابگاه حتماً رمز بذارین.
🟢
صفحه اول: آی‌پی و مصرف
•
آی‌پی قبل و بعد از تونل
— که ببینین واقعاً عوض شده
•
سرعت لحظه‌ای دانلود و آپلود
و مجموع مصرف هر نشست
نکته: آی‌پی «بدون تونل» فقط وقتی خونده می‌شه که اپ باز باشه و وصل
نباشین
. اگه مستقیم بزنین connect، اون خونه خالی می‌مونه — این عمدیه، چون خوندنش وسط اتصال یعنی فرستادن آدرس واقعی‌تون از کنار همون تونلی که قراره مخفی‌ش کنه.
🟢
کلید روشن/خاموش توی پنل سریع
از
Settings
دکمه
Add a quick settings tile
رو بزنین. بعدش از پنل بالای گوشی بدون باز کردن اپ وصل و قطع می‌شین.
🟢
مشکل «Allow background running» که نمی‌رفت
روی بعضی گوشی‌ها (مخصوصاً شیائومی) هرچی اجازه می‌دادین، اون کارت باز هم می‌موند. دلیلش این بود که این گوشی‌ها تنظیم باتری خودشون رو دارن و اجازه رو فقط اونجا ثبت می‌کنن، ولی جواب استاندارد اندروید همچنان «نه» می‌مونه.
حالا اپ خودش می‌فهمه این اتفاق افتاده، شما رو می‌فرسته به تنظیمات درست گوشی، و یک دکمه
I've done this
داره که کارت رو ببنده.
📥
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
(۵۴ مگ) — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کنین
▫️
armeabi-v7a
(۴۸ مگ) — گوشی‌های قدیمی‌تر
▫️
universal
(۱۵۷ مگ) — اگه مطمئن نیستین
اگه مشکلی خوردین، از
Settings ← Diagnostics
گزارش بگیرین و بفرستین.
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1605" target="_blank">📅 08:01 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
