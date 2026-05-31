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
<img src="https://cdn4.telesco.pe/file/G1Ocn9n7OZ4Tz06IFAzgAVoDR9rT5RK6mNdR1jGgGK8S0YETH0zrSS3If5Dc5EsxACwpwcJH5XMvjcAJ9CfvbXHXNmYjm0_j42QzmZVaeUmUAatBExJzRCzz-wsC1jkPfiZhgEzMwQHYgj_1IJDYwGuUKXElf7PwmdeqMn6n4kx37kXI_iy8B9RAeJdwcMJLzcF8SXyuCKYTincKrOVHjyNCHOSVvkPSZvlQwOF5BRfEvQ2LtghTj9HBPYv6HO3tLzIKcfGwL8CDvS-E8TiN5OPaSvjM-YZhmyrBYmieVH0bxFxgZHfxGBafmyz77oasEtDXBXp_xqgJYgDdH6YCCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 102K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhisperInHeaven</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 13:13:25</div>
<hr>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=UEvcSwfKm94fbldScRGlrttg7-baBPPbsL2uT58Ul2t2HGn-WS1F8P5UonxGwb2hJdK3bn_NJWjNSe7ajgKd9FIZO7pYFWgYRA42p-iGmsGyW-I7-KaYaZaqJXBN-9PtGZiUGHwp7RnodA42wNN6VcRSwmKP4Bk8VwFwQfwFJE3drfcHCrsd59V1RcdnSq5Va69VXlNgWW9zesTQt6EKK1lHBKCLDEvijGPr5YnGcepwHtcHry6vcgt8yZ8EU08_KgGFoGI04GreyhNxOCNZaXMoGsTagkfqTvEHiX1ddfeqB_GgWtZmMUY3ZEvM7l7MEAQ3UJXxfsP8HUwIuE6N5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89b2fd3cd.mp4?token=UEvcSwfKm94fbldScRGlrttg7-baBPPbsL2uT58Ul2t2HGn-WS1F8P5UonxGwb2hJdK3bn_NJWjNSe7ajgKd9FIZO7pYFWgYRA42p-iGmsGyW-I7-KaYaZaqJXBN-9PtGZiUGHwp7RnodA42wNN6VcRSwmKP4Bk8VwFwQfwFJE3drfcHCrsd59V1RcdnSq5Va69VXlNgWW9zesTQt6EKK1lHBKCLDEvijGPr5YnGcepwHtcHry6vcgt8yZ8EU08_KgGFoGI04GreyhNxOCNZaXMoGsTagkfqTvEHiX1ddfeqB_GgWtZmMUY3ZEvM7l7MEAQ3UJXxfsP8HUwIuE6N5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنین کاربران نسخه دسکتاپ می‌توانند از قابلیت
تبدیل کانفیگ‌ها به IPهای سفید
به‌صورت مستقیم در داخل اپلیکیشن استفاده کنند.
🚀
Tools > V2Ray White IP Generator
@WhiteDNS
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/885" target="_blank">📅 04:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQKpGdSFh44463GTmB0sW1UQo_EIerr0ill3cO6qpZ56umsuB4EciMzxX4ai0Xhqmb-xcwV6Zoz6pJ3Y9TqptKm9vN64PRYn2O_8pVdiYdPxupfK7jkqVrNOw2LI-T9JhlbZe2EY4bCz1z_sJrcZrtJscpPAla7ayxD09JF6za9LbcIN88KISFupv2EerGtB6V0d3g9FZIc33MNPcvyEyJ3Pkci5gYZ65YlogW2KgNLsxd5uI9fUgI0jnTZPHqqDTEpyHqCmFilvCZKSck75zCCD4B_Ovs0zI6Dmxpjs2FqgqwEIOTM_ge6oS8H9NcagMKDm29dI9gSZVdZjRP9XVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/whitedns/883" target="_blank">📅 03:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سلام خدمت همگی
❤️
الان تنها راه اتصال پایدار و بی‌دردسر اینه که شما یکبار اسکن کنید، آی‌پی مناسب پیدا کنید و بذارید جلوی کانفیگ‌هاتون.   متاسفانه فرمول یکسانی وجود نداره که برای همه کار کنه.   این روش رو میتونید برای کانفیگ‌های رایگانی که از ربات ما هم دریافت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/whitedns/882" target="_blank">📅 02:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/881" target="_blank">📅 02:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/whitedns/880" target="_blank">📅 02:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdNfI_RbTeVa7UNzWn_gkWgPXEqfSKzY5FLbzbA9fP1LtSxxeADBNgsFdBB4E3YNPYB14DJ8MCb6lzXbz_l0ickgmeu1Jx3I84Yp_BPUWFSFo_pHQiYeVaBDxxk3-TqGDK5ndskOeZIzjtJf_ybko44RcZT4eJYztNLaGXdZ2gXZAB1XdfcLF3O-uSZEYCmTEvdzQHG734nCsSLXUschR8Z3VsmIsd2rpCuMq-o4z2CLYfcIitzQLr12aaXHJU-6a8acXNYCWpQ1FrNhDNqKRk4WbukzD-LTF5bGkU6PWGQr5v9tJLps810VORyJsmoAlPWngFej5LR8zAoI-Fn4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در شرایط سخت و روزهای «خاموشی دیجیتال»، تلاش کردیم با ساخت ابزارهای مختلف، آموزش‌های کاربردی و راهکارهای ساده‌، کنار مردم باشیم و کمک کنیم تا حداقل دسترسی آزاد به اینترنت حفظ شود.
اگر در تمام این مسیر فقط توانسته باشیم یک نفر را دوباره به اینترنت آزاد جهانی وصل کنیم، برای ما ارزشمند و افتخارآمیز است.
اولویت و هدف تیم WhiteDNS همیشه ساده‌تر کردن ابزارهای پیچیده و تسهیل در دسترسی به آموزش بوده تا به هموطنانمان کمک کند وابستگی به بازار سیاه، واسطه‌ها و مافیای VPN کمتر شود؛ با این نگاه که هر شخص قادر باشد ابزارها و اتصال‌های امن خود را بهتر شناخته، بسازد و مدیریت کند.
امیدواریم هرچه زودتر شرایط بهتر شود و حق اولیه و ساده‌ی دسترسی آزاد به اینترنت دوباره به همه‌ی مردم برگردد.
از تمام اعضای تیم WhiteDNS و تمام وطن‌دوستانی که در این روزهای سخت کنار مردمشان ایستادند، صمیمانه تشکر می‌کنیم.
دم همه‌تون گرم
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/whitedns/879" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-878">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNSkPf-Kfwqdhj3LekKNjMY0yPz9fr1c-5rY0RCb92UBe3VuVnTf2_SgfaeFKTfYZYQGeW6j1ajVtZcW_pTvvjNiPC48HST7KNpLgI1zZt_9_S3CeYmvU-jdLhcB6hAytR9CTMm_bH2YCB_uh1-QGL4XiBne_-ZP192EVBlSaX0ctQOLCsGhITBqgIrqL5WrghZf2I6lN-mW26C3H3Fq78eIPFek-gWS4rIqyakQanyPcpL4JPT73RW1HzpdP10l1IAJWx1z3VBhGptfSIDSwgBbOZXA0sBQmGQVERxlX2VNTM_dsueVzpQ5emzCamaoEsLYz_uoIXNCASgoJrr1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/whitedns/878" target="_blank">📅 11:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-877">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر  - آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن - آموزش استفاده از V2Ray  - آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی  https://guardts.ir/f/6f56591f7b7a…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/whitedns/877" target="_blank">📅 10:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">#موقت
ارسال شده در تاپیک سرور ها
سرور اهدایی از بامداد عزیز برای MasterDNS  قابل استفاده در  اپ WhiteDNS
🔑
Encryption Key
aaf4b6-@JavidnamanIran-aaf4b6fff
💻
Domains
: جداگانه امتحان کنید
b.bamak.xyz
b.igoii.org
b.namad.xyz
b.jnir.my
b.irdmc.com
b.javidnaman.com
Encryption Method
: XOR
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
🎞️
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/875" target="_blank">📅 04:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/873" target="_blank">📅 02:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🤩
آمورش کامل استفاده از اپ WhiteDNS در نسخه کامپیوتر
- آموزش استفاده از کانفیگ های MasterDNS  / StormDNS و اسکن کردن
- آموزش استفاده از V2Ray
- آموزش استافده از Scanner, Validator, White IP Generator
⭐️
دانلود از لینک داخلی
https://guardts.ir/f/6f56591f7b7a
https://up.theazizi.ir/download.php?t=ecabdec17d6cbb16f37a13fe28c724cdb591
😊
مشاهده از یوتیوب
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/whitedns/872" target="_blank">📅 18:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔥</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/whitedns/870" target="_blank">📅 16:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگر در اجرای نسخه مک مشکل خوردید دستور زیر رو اجرا کنید
xattr -cr "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/869" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-linux-amd64.deb</div>
  <div class="tg-doc-extra">19 MB</div>
</div>
<a href="https://t.me/whitedns/865" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/whitedns/865" target="_blank">📅 11:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/whitedns/861" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/861" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8qkN6Gfkrw8w7xcdkIsiWHVBYv8W5m3H97mqoGH6o1QdQs3QwCHDPrSnnBAuHXGCh72a_I4TJiaQKvqbVIfP9LFNtvqrCaH2rwIAVT8Q04ML8vi0M6feZbdlN0dW6VSBrO5oYrOwQlhPHLRgQKARbqgDKcK6LOvGzFswUv0ZoW-RDqP9apzNwY2aUR42A_uaPtcjhJiR0L5qUfQ4w4nIIreRYcJYi7FK3u9oYQk-n9kGSAOAm3DkrFH6QJqwKX_YbuvhN1o960tS6pvy1aCMFPgnYNjAOqQJ3kQPyQ_wN1s0E5jhnKm3kvnsc7uyZtFZ3iQ7ndiCqR4_9dUkRQ5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انتشار نسخه v1.0.0-beta5 اپیلیکشن کامپیوتر WhiteDNS
⚪️
تغییر هسته از Sing-box به Xray
🔴
اضافه شدن امکان اسکن آی‌پی‌های شرکت‌های زیرساخت ایرانی. با این قابلیت، اگر رکوردهای A+، A یا B پیدا شوند، می‌توانید از آن آی‌پی‌ها به‌عنوان سرور برای کانفیگ‌های خودتان استفاده کنید. شما همچنین میتونید لیست خودتون رو برای اسکن وارد برنامه کنید.
⚪️
بازطراحی بخش کانکشن‌های V2Ray. این بخش حالا برای مدیریت تعداد زیادی کانفیگ مناسب‌تر شده است.
⚪️
اضافه شدن امکان Speed Test برای کانفیگ‌ها.
⚪️
اضافه شدن پشتیبانی از پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، Hysteria2، WireGuard، SOCKS و HTTP Proxy.
⚪️
اضافه شدن قابلیت سفیدسازی کانفیگ‌ها. ابزار جدیدی در بخش Tools اضافه شده که با وارد کردن کانفیگ V2Ray، آن را به کانفیگ‌هایی پشت آی‌پی‌های سفید سرویس‌های مختلف تبدیل می‌کند. همچنین می‌توانید لیست آی‌پی‌های سفید دلخواه خودتان را وارد کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/whitedns/860" target="_blank">📅 11:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIdL9TVAFGSl1pjsKxVBRGgLWBdOW1sMN4iJtEqNvAFfzKV8gWOxqJ-mAzMPmEKtgeQyLfDpAWNNmYzeOeZ-G3yBLe9TtlJj3m0LpwNAGNzZLZmfkdXGS1jcs42tPVNOaUYZNgK3LMuJS0j1pMmGtjxp8rdDaKkR4nK-UluiXk7ayWNQgyyYIbw2JoO6KJoXFpEgFxKUsQAorGhhP4U_iFB8uGD0hIUNp1zF40_tTrhKOl-gp5iP9MFH-LzqShoGae1b7yBlydWQNo8b9Mrf3iAC6NsQxhFnjEIan5Bh_3rLirDLCXCMP1xetYvO9ljIEpPWrvKBeWXExIqX-wfc-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/whitedns/859" target="_blank">📅 04:36 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/whitedns/852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/852" target="_blank">📅 04:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">☠️
پروژه‌ی SenPai Scanner — اسکنر IPهای Cloudflare   چی کار می‌کنه؟   از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.  چطور اجرا می‌شه؟   فقط فایل مخصوص…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/851" target="_blank">📅 03:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SrxlF63ZY8GugneUavcl73s2ziebLzSJP1CzVRAWrNnwLIF3WsE0qjetBxwAfVdy_b9Bb6XgCKkcNUSLgxywNQsGPjO-P3q977LDRTgQCC8qOJoI_kMtQrg5s63llpCtVyWH2OwZTvhIzOZchQbp9DzbTV0pni3uq7zOKJ2sBTAp5ZOC5uTLRqSQZBFUB6_gqmZfkwx1cobR3aW_8nMLylZ8bpmLK826h4h8K3xhzCGy6JEKjDYT9oSo9asIYpcj1m3uYEC0323bcgrhsGSrmSxJFTh2-OBLi-4-yrePXNx45xzJed36Xe2wsUkR4J0onoczVG2A_Naozzx4lG11Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/850" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5A1ZRANho8xX4vZVmCgyllr33Zefo8STixDd7uf8NI9jwH4M3EIhtAiAfrHE2nBHXXTx4TyjRVrQYBepXxjXEHOxGSB1T9W7G4hrfedPgf9ADPo_FEHKU9v1hL6UdDT95PSbUOumS0Kc0njFk-gWiZnTjO_SdFUHwhhhr1IEDbaQlFPYQPp-ceS-DS46s4aGs2TUpwDRgdxcROD1XgnZ0fJpnsBoJywPkLubBrVml8CXEQ1Ce_NwPMaYoJRdfs1WFB3y2ypPBIKPq_QKzRNmG9fqYSh5rNycoOhInHKQvQE2emnpvyG8vu5nUPQWYRYm2DRPdtYO1HyDNhnEpCyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/whitedns/848" target="_blank">📅 17:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/847" target="_blank">📅 14:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-841">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayNG_2.1.8-fdroid_universal (1).apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/whitedns/841" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آپدیت آخر V2rayNG fdroid
🔴
🔴
🔴
دوستان برای اتصال به کانفیگ های بات از این اپ استفاده کنید.
@WhiteDNS_Installer_Bot
@WhiteDNS</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/whitedns/841" target="_blank">📅 13:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/840" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rd5iApztgCLGKqWOJKu2pg0LNbWazO4_J1Kiw_ueqqGvC7anDqM3SX9dMyih-b9IWNzGTncHSB1kfNecW8bqBT1JkIqSMcN_zFG28blLWkztj3ihPxu0KkJIQTl7MspCP4WXy2M0nkXrUh8axFc9yjRgWkIbp0rHO8-bzqLTS65SRq5cGn6OljUAujhSTpoXo-gUv5ySp1X5n9eTGJIx5ONi2LpPw8g4ApSGWRvRCWEKImAzpVDVu86xeUMe5m00qp3A_IrSrT_VOoKe13zcz9Rg57HnB_mtDmW1YJymJlCRfM7iUmwXTOg3e7106w8dI6SbhpI3Ch4ikTw8AUc2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gu-ThUoTizcDxSyQ9SA7NCOSiR3M70EbbirqstFQRPcvE-XkJQNJLkgaYDMIyjq224PUEpTDG-9sPvyXbKF5htP89LtkSD7ZHZ4EL4LaIHmxO6MvEBtT8ZkK6pqCtpiWPFTc49BIfixA9u5O0E8dZ7ZGOReg8yfxsN5Bl24Ozkq1pngsFX7xuf5I5wr0jQGYkIvQLpT-xqqyo8ZfIkJD1SJiTgigmdPx9r57FyE_IlDi73sFZPRFgSjJZ4vu5CtBgZRa28llddvJQ_fdsy0cItr1tpZtVv0jl7m6wfh8BPRdP9DKgDdFkpbDqrjW5yelLLIQtElj3gUi6XO-f4vEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K4MVDwZlL1A_XLvG9RXzKC5gm8DhqqNsAwhFsgC6Kj7st0FdfS1rKekwLPKHSvPzdB-izKnStIgBk8M50GV-W1dkDhML3ZUqdBTmwkUXMaUEshstvwo1qytlIFMa2iAInd5zX-02CJw1PMEcn2BA-TqLcJ17zTDozBPyqhXyC-oYSLTrgMq1DZt-yFKrWijh40s5LPo5NB--cMg3pTx43wNunLt3F8vz2UeHHDKjdkSahjzZJvhLLyK1Fc4lyTNlGv8VzwF0OAepZ7CR2Rmi5lJOv5zBe5H1eT69H9K2rHY-8xnkCT6EnKXxuGc8R-A0hgD7ZCXdxB3x68RTSG1lLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YBSRJ1Oa5oaWtU2bTzfUglwFpzhg27asYbTlpd93Szvykt0PRxMNqsx_XwI7VHZzR6jr3Kb49qbJrfKWEudeYm_EnY19j2qCMS7oWUO3rF7cRqeoUxkhb9WHA3teppPtgcNvioOon2XNQb_I5vftoIn2TH_E7t9I3KngVcbyTqHYFmyA2vaaRtDM0NQajr4xzB73GqgX9IzfOIY2aalAwHwgrMaNt_Q0VS3D0YBatKFrtg0Y2hauBTHupc_xQXY4Q2lXhI-oyc-HpIWD_xnTodeTC8kXQvt_xbU-Unr4NgUXs-cSeCx0eYc8OTj6Vct8eqarftnGPw5mrKTkMSNjuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vxdrrSS2NESH0h26nSQuFa3jruBPa5a1bS5gnj36X1Eglmz1AaNtTlQqGkfkDjeYZJ3-tmQGp0sj-kgczo57izlwLyEE1KrbrlQTFNXi4Vun1tyBF95WAtpnxbK3UUHLNXns2M-phAStwIpzawD4E84aVU2gg8zcsmQyZ3pjZl3XqR0LEwqbDwcZmWlhjmicSUsS4p_6zREcRHwQouAWVQfwkx0PpKBWGbzbG3i8En51ZzlSQlVb_rdEstK9eh8lyG1M79wHYrd3CWZGI6uF0iZt3uEZE6YR7koRYvkF-zQdlkOI7Ult46tzRpG1W0z1zUk6KJ88yUXSqiv5FsZHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VwXtTGIGRgNOGcDCBRs17s201ugNWKouQxAGKbvl7Wb9L5_EfS7d2V_h7Q7Wih_bApeHG8EP7KYI6mK_C3kln_u-YjcUTjxix54BP-ewPfQEox0N9WMSpDd4JL0hDedfjMzpfSGbu5eTLXV9_bLRQes6L9WYlYHdo8dWtM5ABzaIp0-s2MNdSqsLUffYANMdml_ECpn36ScB_oc6QqyqMR7DHU7YO6H_XNmXJlN0SKg5Yd85o82zZ6oLXD5DuVH86WllNVSZWfEfApCRkHJoLIVAeXc3JKgFNbrUrwvKSGn8mr3vFz34zbL5udtXYsqg16Nn_h3lwoWXZ9TwpYrxwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ggx7jFrl1x3VNlH9v9uDAA6WlHMfjEDWJVtB_DHQWsGSoEpeJIft8I2xNzKpudLKeHr4S5MP0yyf84Ma8cz-Fw0UT3IfDeTudkeLkrd6E9OTX8_kp31YmggLmWiIqG0WNzuIHZk6OpTlles0ksrS2IwPdJLkDE7EKgmyYJgI_ZuYUiAW0wa7mdzVagkDgy4HaduySsiBNgVye9JikdEoekhzSsmhatvP-o8wtyMtoTPN1gtT03Cgcr7qLsbG7b-w98GK8rP3foRKzfO3sIQYtMiTdT7QECEqlHMs697Oh0uZ0h2BasaTQhXnCt7aLQJT3KEWaeR-h_TSthPvovX1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FSYGD-BSTqhKgptGcsicZym8imyumMZFKK7cQOG0IirTtoz9cSiCq7OIcsTf_-5oK1O47Q9GrGnkY-O85xB7VYVAzhm4NZggx-bgkmpGxyRtBa81LNlk4aBL5n375-WwFn94kN61dxv_LZ60Si-u_MYRO6Tk2xL4ARLTisBRneK0dOwWQHPVslP6LQSuHab5Hbp_VxC7teJ0HZyLfNYhyoFHT79j3D4sGr2PmO9dXjvzM9sCanB1AtJZRkmCrAkbw94a-pSDEv3-mXrVGOH_MKuQV5Q3M5wvnVvvksNaP_VyM6kvFe1YE4FFE6NnUr_Gy5hnQYEwSvc89zaHo9Jpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bmnfoWEcx6nFHs2LE1hgIQ2h3VScIRvhiV0KT5XvTGd0412QeIHh2kKdSsDmiqYsZaToxL3Ao4QmtHvR5SdKZ-4X-JINe2bFHrOSxc7Vf77iIqIANjh_2QAfyb7th4RGvJxeRXNyYKT_5QGlV-A6IdF6aRR7o_Kr9FIkma8TJUHS_Ba9rTNYsfDot380u27x3WV1FhvXNJdINIzdav3DLKB-O6xo7wTtQVSi7OfaXDU5aU2SLIPVzOLGm3FN-l-RyO_daUzxkirgPyNTBq43dBRnZC5KIBFN7rj9mq8xT-dRodtcaFtrA5vo3Dzon3WlCtvMPdyHK7x2Nm6nH_aMmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.  @WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر…</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/whitedns/831" target="_blank">📅 13:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7iBtirSffCQFhC4ID4y76ilz898K14ShrvPPpSX5dehoBI1DxEd2bBhA70CnnN4ojUUYAR5gugq_0XJ7PgmXKAP9T3GNlXUmngBI-x7z8_AvtQbuf337ysC3HEv5FV3-4sZ8VQiw4Hl1V3rUo6S11vdk8meshlYOkjwYTZY-xcTVAmgccS69J8-XiSt_5fmQX_obCzFIhGbK2VhcQhRqCpKMgzuirEhDmB1k6m9xFvQ-8UaNwU1yXUBNsacEwPecqolFYP9yfd2JYBabva-rg1s7qrxtDcavw5zx0w_hEO5apdXaObsfaEYRm-3IpTzsBfuUbLZ2hLKo7tbpi1PUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی،
🎁
با استفاده از ربات ما می‌تونید روزانه ۵۰۰ مگابایت کانفیگ رایگان V2Ray دریافت کنید.
@WhiteDNS_Installer_Bot
🌐
فایل خروجی شامل ۲۴۷ کانکشن متفاوت هستش. دلیل تعداد بالای کانکشن‌ها اینه که شانس وصل شدن شما روی اینترنت‌ها و شرایط مختلف بیشتر بشه و پایداری بهتری داشته باشید.
بعد از عادی شدن شرایط، تعداد خروجی‌ها کمتر و بهینه‌تر میشه.
⏳
همچنین بعد از ۲۴ ساعت می‌تونید دوباره درخواست جدید ثبت کنید و کانفیگ جدید بگیرید.
ممنون از حمایتتون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/whitedns/830" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/whitedns/824" target="_blank">📅 12:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-820">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-linux-arm64.rpm</div>
  <div class="tg-doc-extra">24.8 MB</div>
</div>
<a href="https://t.me/whitedns/820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4  با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.  در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/whitedns/820" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-818">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/818" target="_blank">📅 11:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-817">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوستانی که از نسخه اندروید اپ WhiteDNS  استفاده میکنند.
برای بیشتر کردن سرعت و پایداری
، میتونید با وارد شدن به بخش ریزالور ها، یک پروفایل جدید با مقادیر زیر بسازید
1.1.1.1
1.0.0.1
8.8.8.8
8.8.4.4
9.9.9.9
149.112.112.112
208.67.222.222
208.67.220.220
94.140.14.14
94.140.15.15
برای کم کردن مصرف
، سپس وارد بخش تنظیمات و پیشرفته بشید و‌مقادیر زیر رو تغییر بدید.
Upload Dup = 1
Download Dup = 2
اگر سرعت شما قابل قبول نبود، دوباره مقادیر Dup رو بالا ببرید.
توجه کنید که این مقادیر فقط مناسب اینترنت پایدار هستش. در صورت بازگشت اینترنت به وضعیت قبلی، باید کانفیگ های متفاوتی اعمال کرد.
ممنون
تیم White DNS</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/whitedns/817" target="_blank">📅 11:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آموزش اتصال V2Ray در نسخه کامپیوتر
دریافت لیست کانفیگ ها برای ایمپورت کردن
https://t.me/whitedns/804
https://t.me/whitedns/805</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/816" target="_blank">📅 11:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta4-release-windows-x64.zip</div>
  <div class="tg-doc-extra">23.8 MB</div>
</div>
<a href="https://t.me/whitedns/812" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/whitedns/812" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1QyVoyZpqtkQxX1TQ4DjSXltXWhvygmM1_ZyfUmjrZvx3wyba90JdWXgMHn9N0AYmv0ThFa7L1Fgisu_XpwHiZlVUZXix3S0WKjpcfNUYhTs8rrOvXBQOxZyMQTSyuJhsfd6TN2kLwN_FpQzohLycx2JFlj4WajM8Afw2OC1diovokSSv0mhHLUH7ARyox91UepySAY5iqo9Kdt3-jvNzJZ-A9reH6CrsWBxb6GIydblFqAFAaPb-9W24eSNamPu82b8s2wIZkgwPcpJXNKQd-fFKgxnua9uwtVR0oqgUtu494_l2sCxGNtXaIHQmrA4IZF7xnXZqhDz1xsQZilxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نسخه WhiteDNS Desktop V1.0.0-beta4
با کمی بازتر شدن شرایط فیلترینگ و قابل‌استفاده‌تر شدن روش‌های پایدارتر، تصمیم گرفتیم پشتیبانی از V2Ray را به نسخه کامپیوتر اضافه کنیم.
در این نسخه VLESS، VMess و Trojan پشتیبانی می‌شوند، امکان وارد کردن کانفیگ و Subscription اضافه شده، و ابزارهای داخلی برای مسیر‌دهی هوشمند، مسدود کردن تبلیغات و عبور مستقیم ترافیک سایت‌های ایرانی از شبکه داخلی فراهم شده است.
اتصال MasterDNS هم پایدارتر و کم‌مصرف‌تر شده؛ درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت حالا تقریباً شبیه یک VPN معمولی است.
✅
پشتیبانی از V2Ray اضافه شده است.
✅
پشتیبانی از VLESS، VMess و Trojan اضافه شده است.
✅
امکان وارد کردن کانفیگ و Subscription اضافه شده است.
✅
آدرس‌های خصوصی و داخلی مستقیم وصل می‌شوند و از مسیر V2Ray عبور نمی‌کنند.
✅
سایت‌ها و آی‌پی‌های ایرانی با geosite-ir و geoip-ir مستقیم از شبکه داخلی عبور می‌کنند.
✅
تبلیغات، بدافزارها، فیشینگ و ماینرها مسدود می‌شوند.
✅
همه ترافیک‌های دیگر از پروکسی V2Ray انتخاب‌شده عبور می‌کنند.
✅
کش داخلی sing-box برای لیست‌های قوانین آنلاین فعال شده است.
✅
MasterDNS پایدارتر و کم‌مصرف‌تر شده است.
✅
درخواست‌های تکراری حذف شده‌اند و مصرف اینترنت تقریباً شبیه یک VPN معمولی شده است.
✅
سرعت اتصال بهتر شده و Packet Loss کمتر شده است.
✅
ریزولورها به گزینه‌های بین‌المللی و قابل اعتماد مثل
1.1.1.1
و
8.8.8.8
تغییر کرده‌اند.
✅
حالت تاریک، Scanner جدید، بکاپ کامل و رفع باگ‌های زیاد هم اضافه شده‌اند.
@WhiteDNS</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/whitedns/811" target="_blank">📅 11:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Defyx VPN
🚀
یک اپلیکیشن VPN مدرن، هوشمند و متن‌باز که با Flutter ساخته شده و با تمرکز بر امنیت، حفظ حریم خصوصی و تجربه کاربری جدید، دسترسی آزاد و رایگان به اینترنت را فراهم می‌کند.
🌐
🔓
🔹
متن‌باز و قابل بررسی
📜
🔹
رابط کاربری مدرن و روان
💻
🔹
تمرکز بر حریم خصوصی و امنیت
🔒
🔹
مناسب برای دور زدن محدودیت‌های اینترنت
🕸
بروزرسانی جدید
⬇️
GitHub:
https://github.com/UnboundTechCo/defyxVPN
📂
@whitedns</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/whitedns/810" target="_blank">📅 10:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Orbot for Android v17.9.4 BETA 2 (tor
0.9.4.8
)
بروزرسانی جدید
Orbot 17.9.4 (2.7.0) برای اندروید منتشر شد
📲
این بروزرسانی، موتور Tor را ارتقا داده، روش‌های اتصال جدید اضافه کرده و چند مشکل اتصال را برطرف می‌کند
🔒
🔧
.
✨
تغییرات مهم:
• ارتقا به Tor
0.4.9.8
برای پایداری و عملکرد بهتر
🚀
• اضافه شدن پشتیبانی از Shadowsocks داخل خود Orbot
🌐
• امکان استفاده همزمان با پل‌های obfs4 ،Meek و WebTunnel
🌉
• گزینه جدید «بدون پروکسی» برای خاموش کردن سریع پروکسی بدون حذف تنظیمات
⚙️
• بروزرسانی پل‌ها و ابزارهای دور زدن فیلترینگ
🛡
• بهبود DNSTT برای اتصال بهتر در اینترنت‌های محدودشده
📡
• رفع چند باگ و مشکل اتصال
🐛
📱
مناسب برای افرادی که از Tor برای دسترسی آزادتر و امن‌تر به اینترنت استفاده می‌کنند
🔐
🌍
.
دانلود
📥
https://github.com/guardianproject/orbot-android/releases/tag/17.9.4-BETA-2-tor-0.4.9.8
@whitedns</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/809" target="_blank">📅 10:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دوستان سلام :
این یک مدت به همه سخت گذشت ، شاید شما اسم دو نفر را بیشتر شنیدید ولی بدونید یک تیم ۳۰ نفره بی نام و نشان پشت این کار بودند  توی بدترین شرایط از همه چیز زدند تا شاید یک روزنه کوچکی باز بمونه ،
ببخشید کم بود ، کافی نبود ،ولی در حد وسع خودمون تلاشمون را کردیم
یک تعداد زیادی از  دوستان پیام دادن ، تشکر کردند و گفتن ادامه بدیم ، خواهش کردند بمونیم
ما هستیم کنارتون ، مگه میشه این همه عشق و محبت را رها کرد
یکم استراحت کنیم ،همه با قدرت بر میگردیم
توی این مدت مراقب خودتون باشید
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/whitedns/808" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-807">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBL5vUKrfRAOV_0gncqBuDOs-Wh8poegYBWM6ZnGlGBq6nY_fd3o3VF3pkDZ7hPVEol4IImMmeJaCV3rll76Q5dLg8lzFrPIe5aJBL2VVeqKi9hGsKIBWm15C1bxoiYhbKfymeRnRsbMfPLR22ZKiWe1upZzoPXa-nNSBsAJaLZVFpWaqV2NlbF-5WpjyFrePXymfku8KN9FyrqzjiY5HKaaFovaLHB_1UQRj9K2NdvNiS2JXsJBQSDKIK4dGv_shvCqa1WgGeJ_EcVG8kKEUf1YsfNnkqpG33XQfii4cmOXlAPwRRYupO5jmN73X_cZhe6P_wqAzExeTU3qXOsxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#موقت
یادمون نره کسانی که از ظلم پول در آوردند.</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/whitedns/807" target="_blank">📅 19:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">برای استفاده از کانفیگ های بالا میتونید از اپ v2ray یا دیگر اپ های مشابه استفاده کنید
👆
👆
👆
اپ های قابل استفاده:
npv tunnel
happ
nekobox
MahsaNG
v2raytun
v2box
V2rayN</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/whitedns/806" target="_blank">📅 19:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-805">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2rayconfigs_with_WhiteDNS_2.txt</div>
  <div class="tg-doc-extra">30.2 KB</div>
</div>
<a href="https://t.me/whitedns/805" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">115 کانفیگ تست شده دیگه پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/whitedns/805" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-804">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">v2ray_configs_WhiteDNS.txt</div>
  <div class="tg-doc-extra">38.3 KB</div>
</div>
<a href="https://t.me/whitedns/804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">141 کانفیگ تست شده روی مخابرات پینگ 100-200
ممنون ازعلی عزیز برای تست و پاکسازی لیست
@WhiteDNS</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/whitedns/804" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-802">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bu0_Mb1yqM0icBYO9IjbzlR-xlsMFY2b3p8JJ7EuEhhzrG74Thou4HAevTSRVyIuG1ie_hdR9Bb6ln3RwETODEpzUo8K9hROrTlk54QH9N2iJH-WpWvPj5jtrgs9nYlb5PUS4bSS39BjFjX0qLoB5YelmeNKKvGPw2Uzs0Frl-PnpoTcDoHgsFlYFWRxEMLVVxIyDbJP4k7OCi4cy1QROX60wvxxSPJ_AgTKDWDnpRSgtKZqL5-FUq0F54yfh8RS2hBiLg1APXJELrSXXLCIQtxCFC48-H1OKn0akHc0jmxU1aZDYYuEeWxFEIK_dKZ-Nylz2NXOeF3JY9gVn3Nvjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nh2Pwko5yKBpcwcc9wqT82fyL5cojm9DUHufNO53YLvN1ZhWTKXUu95F3PPGwvKvZ531aGooJq8CwcJRP7D7TDCkFGD3VBNuBEOot4Lyh4vMb6QCAcJwpexoxhmG9SZTuTGdFzO0UTsMpPMSgKP_mwqf0uzsDVQnUiOeZFyG3GMoGRTDjSxdv10H_-JPYEpV4fB0wtl0ky_60LQ-Nk1b8JcK6dd26O8U4fe4e-9PqT7shnvrtXiD6SgfYp5BRxbs-pFSwzsYKx7nEZTRUxgM3ESU0ilzOfSWPDEiFJ6jP46ZT9D-gSRYdaGhNj1b88VeFiFEPKzEBu114APahhrXrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این هم یک تست سرعت با ریزالور های درست و با اختلال کمتر
🤌</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/whitedns/802" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-801">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">“}
سلام خدمت همه عزیزان
❤️
امیدواریم این روند ادامه‌دار باشه و اینترنت به‌زودی برای همه اپراتورها به حالت پایدار برگرده.
برای دوستانی که فعلاً به سرویس‌های دیگه دسترسی ندارن، می‌تونید از ریزالورهای زیر استفاده کنید:
1.1.1.1
8.8.8.8
همچنین بهتره مقدار
Duplicate
رو کمتر کنید تا مصرف اینترنت پایین‌تر بیاد و اتصال داخل اپ پایدارتر بمونه.
حتی در صورت برگشت کامل اینترنت، سرورهای WhiteDNS همچنان فعال می‌مونن و می‌تونید ازشون استفاده کنید.
یادمون نره، مارو از کمترین حقوق شهروندی محروم‌کرده بودند. فراموش نمیکنیم.
دم همگی گرم بابت همراهی و صبوری‌تون
🔥
@WhiteDNS</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/whitedns/801" target="_blank">📅 17:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-800">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">در طول ۳ روز گذشته، کاربر های ما ۱۰۰۰ سرور جدید اختصاصی با ربات WhiteDNS ساختن
🎉
@WhiteDNS_installer_bot</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/whitedns/800" target="_blank">📅 09:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوستان گرامی :
ما هیچ گروه و کانال دیگری در هیچ پیام رسان خارجی و  داخلی نداریم
تنها گروه رسمی ما :
https://t.me/whitedns_group
تیم whitedns
@whitedns</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/whitedns/799" target="_blank">📅 03:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-797">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQcJrldiN45hq7xMk6OdT0P3Gs4C1Tcon5LHaNvWi7W2TO6LrAj8jWMuPUy9kEWANhIpncEa36Yf-ue3-IhL69MeryIR1iyxdw68Wbbmq8uzrhsgn4_pZfFXYuRJ0wyQXy3luaJLcLSn0Yf9kb01VBUNIZiHbOhELXGTw2n--TcFL6MJhcNoRckT5Qjx8_ctGD-11yFq1N_NysLaGiZsMpnWN32AujMulpaOzhlbstkkG2yBv5z7_ssetv3g-kkp10ZqzZUkLDHZqKGPdNXxGPczthWM52kXAwyFdDcoudmDicee1iPzb9GaAXJ4RBJD7i0gSrBFw7pqIwLUhgQepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کیه این تک دلقکو همیشه میزنه
😂
؟
به افتخارش نفری یدونه بزنید ببینه دلقک کیه
🤡</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/whitedns/797" target="_blank">📅 16:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-796">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaFjwEgaTK883Z6WfT4sMGE01OXTCUhZSxApeDhGZRvF58unhbuEfLu9F7UEqeNSvEwW8nZqK9ZHRydwJJRssVoyzg__rlIFWqd6vB2sql3IyerhgHwcGFTHg6yttPfprT_jJWd9ikeb4Sfj2HX6vXS2tZSdsvDOvXprdQlIySsYO0gnoveUNs5ZCkhwgwshY8Rzp_LM38S87ShzzRZPKKi1nILZt2qm5L9skm-s8a0v_O53QvXHPB0AEnTabw-UYpkR50KAFZQDGwviiCSdNX6vCd3qLu4zUgCOS0wFNmMdKKp3EqdOUeybDwqZob4Eqxxs2kCZ2N8FVnhoN6csQERU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaFjwEgaTK883Z6WfT4sMGE01OXTCUhZSxApeDhGZRvF58unhbuEfLu9F7UEqeNSvEwW8nZqK9ZHRydwJJRssVoyzg__rlIFWqd6vB2sql3IyerhgHwcGFTHg6yttPfprT_jJWd9ikeb4Sfj2HX6vXS2tZSdsvDOvXprdQlIySsYO0gnoveUNs5ZCkhwgwshY8Rzp_LM38S87ShzzRZPKKi1nILZt2qm5L9skm-s8a0v_O53QvXHPB0AEnTabw-UYpkR50KAFZQDGwviiCSdNX6vCd3qLu4zUgCOS0wFNmMdKKp3EqdOUeybDwqZob4Eqxxs2kCZ2N8FVnhoN6csQERU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/whitedns/796" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-795">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xjo0Sw5kfUkbsOyz0qrp9eyQ0vSdcy_DPzjwHUkgKAVAawhnhlKxuuaYvjL6icNuOJfhJofX2VIokO7c6vZN-giODXZLZuQQYA7khGvDQC9Xbk7GWIDjqNUtxSnXYphg6mYgpIDm3c51cYyBggGulq-7ZoVqNaQGM5bzKA_Px27IVIiHPUJezFt40C3s3KBsfKUzJ4Vl4BFFdSbrQQRIqCLPcXga1cw8E_WMzu-Z3oQZc_jH6hm3MnFnGyMpgSlalGvOCvGxVeWBnjODolWWjtUDWSwAnfRSjHa6xnFGva0CbabXM3wmVxp-AoheCSua14XynTcFX_eBcV5ZAZZmvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاضر مشغول تست نسخه جدید اپلیکیشن دسکتاپ WhiteDNS هستیم.
در این نسخه، علاوه بر اضافه شدن حالت دارک مود، تغییرات مهمی در عملکرد داخلی برنامه اعمال شده است.
یکی از تغییرات اصلی این نسخه، تغییر کلاینت داخلی اپ از StormDNS به MasterDNS است.
این تغییر به این معنی نیست که سرورهای StormDNS دیگر قابل استفاده نیستند یا وصل نمی‌شوند. سرورهای StormDNS همچنان قابل استفاده هستند.
اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/whitedns/795" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">White DNS
pinned «
دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و... ترجیحا نخرید. نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه. جای مطمئنی برای دامنه دیدم معرفی میکنم
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/793" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-792">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان گزارش دادن که Hostinger پولشون رو بلوکه کرده و پشتیبانی جواب نمیده و...
ترجیحا نخرید.
نکته اینکه شما با دامنه .ir هم میتونید انجام بدید این متد رو اما خب توصیه نمیکنم به شخصه علتش هم واضحه.
جای مطمئنی برای دامنه دیدم معرفی میکنم</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/whitedns/792" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-791">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز  ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.   تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.   من پیشنهاد میکنم برای راحتی کار شما، بعد…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/whitedns/791" target="_blank">📅 16:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💥
موقت
🚫
دوستان :
اگر سروری دارید از جایی  میگیرید که پورت ۲۲ نمیده اصلا خرید نکنید
ظاهراً یک عده دوباره دارند سر مردم کلاه میگذارند
داستان داریم به خدا
لطفا اگر توی گروه های ما کسی داره کلاهبرداری میکنه با ذکر ID گزارش کنید
@WhisperInHeaven
🚫</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/whitedns/789" target="_blank">📅 12:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-787">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/whitedns/787" target="_blank">📅 05:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-786">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/786" target="_blank">📅 05:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-785">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ7BeSUkqcK0c4qxfrvQJDTrOiLqDjiBxSbxuC532QAZfiy1wqFcHwVnnlKL30bYgmn8M3awKvM1-CyHwYXxhyk3bOwmyqVa_6AiUvOkW6gOGZaTODcYssk-U77hXA6XRjQJw3YYOpFi2EjCp4CVFq26zkixy7_PNJLu5zY5j3cNSTOae15x6OzvZZkSDEjtV-4203mEra4VlI2H7AsupEH4OqGCDMkuH5LanVTLCDbfXIj8oRV9z2Cy4fKGMQsGzYa7TAZy1YX6C2P6IPbJHWQusT8s8XNZY4e6p0-FWnIfpMADC1OhZF7ffMa67WzamqIQPVhruqbbZYuc3Z28XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot
این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی و از طریق تلگرام مدیریت کنید.
✅
نصب خودکار MasterDNS روی VPS
✅
مدیریت سرور از داخل تلگرام
✅
دریافت اطلاعات اتصال و Encryption Key
✅
بررسی وضعیت سرور
✅
ری‌استارت و مدیریت سرویس
✅
مناسب برای استفاده شخصی، دوستان و خانواده
🔐
نکات امنیتی:
اطلاعات کاربر، اطلاعات ورود به سرور، رمز عبور، کلیدها و مشخصات VPS به هیچ عنوان ذخیره یا لاگ نمی‌شود.
اطلاعات فقط در همان لحظه برای اتصال به سرور و اجرای دستور مورد نیاز استفاده می‌شود و بعد از پایان نصب یا اجرای هر دستور، توسط ربات نگهداری نمی‌شود.
بعد از انجام عملیات، اطلاعات ورود و مشخصات سرور توسط هیچ‌کس قابل مشاهده یا دسترسی نیست.
به همین دلیل، کاربران همچنان مالک کامل سرور، دامنه و تنظیمات خودشان هستند.
این ربات فروشنده سرور یا دامنه نیست.
کاربران باید:
* دامنه خودشان را تهیه کنند
* سرور خودشان را تهیه کنند
* دی‌ان‌اس های لازم را روی دامنه تنظیم کنند
هدف ما این است که راه‌اندازی و مدیریت سرور شخصی برای کاربران ساده‌تر شود؛
نه این‌که همه وابسته به چند سرور عمومی و متمرکز بمانند. ما باور داریم کاربران سرعت و پایداری بیشتری با سرورهای شخصی و غیرمتمرکز خواهند داشت.
⚠️
این ربات در اولین نسخه عمومی منتشر می‌شود و ممکن است هنوز باگ یا مشکل داشته باشد.
لطفاً مشکلات و بازخوردها را برای ما ارسال کنید تا سریع‌تر بهترش کنیم.
ویدیو آموزشی خرید سرور و دامنه و تنظیم دی‌ان‌اس به زودی داخل چنل قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/whitedns/785" target="_blank">📅 21:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-784">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI3sFmC1xETmsQx0UgzMTYAdYtxfZwqzyNUHNXQH23yw5XswiqQBE8t6LKWYWCJzbjIHLQRKk8E_L928PWJdoZj8fowMElryQXlN4pt2_CpgZS1ZnDSIJyMiBbjYR9EP2kglzui8JRxGHCSooSiYlNgu1KJMebMnlQa96vaS6OLHcNPnTnUfG79x2ys1dN_TMuiw5tuAqHlaY9rmtUqULGFmCgGz7wLFlT3COLZQkiy37BR13I3gOxS6TeGnXwfSwiQQL5bgRLIfiX4kr1UAV8JDeBAiGP_-GYbdrhTJr_B3YTg64FBDI5GtNTI0busDQw5Sy6_bl8I_sY8UBBjFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
پروژه جدید WhiteDNS در حال آماده‌سازی است
♨️
تیم WhiteDNS بر روی سیستمی کار میکند که کاربران بتوانند فقط با داشتن یک VPS و یک دامنه، سرور شخصی MasterDNS خودشان را مستقیماً داخل تلگرام راه‌اندازی کنند.
هدف این پروژه این نیست که ما به کاربران سرور یا دامنه بفروشیم یا مدیریت کنیم.
هدف تنها ساده‌تر کردن فرآیندی است که امروز برای خیلی‌ها پیچیده، زمان‌بر و فنی محسوب می‌شود.
در این سیستم، کاربر فقط:
• VPS خودش را تهیه می‌کند
• دامنه خودش را تهیه می‌کند
• DNS Record ها را تنظیم می‌کند
و باقی مراحل توسط ربات و Mini App تلگرام به‌صورت خودکار انجام می‌شود.
سیستم به‌صورت اتوماتیک:
• وضعیت DNS Record ها را بررسی می‌کند
• اتصال دامنه به سرور را تست می‌کند
• MasterDNS را نصب و راه‌اندازی می‌کند
• اطلاعات نهایی مثل Domain و Encryption Key را به کاربر تحویل می‌دهد
در عمل، کاربران می‌توانند بدون درگیر شدن با دستورات پیچیده لینوکس و تنظیمات طولانی، سرور شخصی خودشان را راه‌اندازی و مدیریت کنند.
این پروژه متن‌باز خواهد بود تا همه بتوانند کد آن را بررسی کنند.
در حال حاضر پروژه در مراحل نهایی توسعه قرار دارد و طی روزهای آینده نسخه اولیه آن منتشر خواهد شد.
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/whitedns/784" target="_blank">📅 09:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-783">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/783" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CawAyk_qwW1KUPnPSeD01z6pLiANjRyFYMIzyGkbtVlFEiB_Bh-ZUK-z37o-vAuRup7F1eUBx29qZ9exsRUBJ8PXN0C6cKH_AjAYQfWk7h94ayHecdwWjEG3vDygpBljpccpm3pJ8zKciAX7FdVN43s60u6QxSOmG_EIIRF-EcCnzM37H-XiAhvKpYUCMBDuCnLetv6iEOvJHS2AwkrMPTf9dP5QI7x2sAGig4BjDvKipZv1wcHvmiq6y9fwa7jTgyw3tFtFHvTUF8zuSbNMRzDZGFSgnHQb5QEhYaWh0kPu7NPo38v8gviIRP-jgFsDW6D6n1WKHEVqtROzdpvfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام دوستان
👋
چون سوالات خیلی تکراری و بی‌هدف شدن
🤔
ما یک گروه با تاپیک‌های مختلف درست کردیم
📂
لطفاً اونجا عضو بشید و توی تاپیک خودش سوال کنید
✅
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/whitedns/782" target="_blank">📅 18:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-781">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdcRmIQ9s_6cuTRt3L77LuQmYt3VFmUXwRNzc9akvhcnMJtOGUnhp5_9ElZGP7v3uH4g-Tvc03GySxtsPdiYoPtoeY4QCrWXL4B_RFgh65ApKBwgT3f3oWElEKQGdDN19TA58WPI2CY1DpXTzhlXkH5BEWMkK4VmQ1QTV14EKQIjw_YhOZN_Z7RoSnXwTuSmwymvDqz-4ObazeHqkJxPtrHQcdjshiDnfCCADGU7kTq_B4jdLvqWQlXn73MzVrB9BtTP1_KdZno4TmeZoRoPJATI0envRdmz5938NunfnyAzOwn0BiXeGa2CUSnfnhSIk-MPMhhc3zm9Oy6O3SFXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش پروکسی و تانل کردن ویندوز
در این ویدیو نحوه پروکسی کردن فایرفاکس با نرم افزار WhiteDNS
پروکسی کردن کردن کروم ادج
و همینطور تانل کردن کل ویندوز با متود جدید آموزش داده شده است !
لینک دانلود ویدیو ( داخلی ) :
https://dl.toolschi.com/view.php?f=9f27edab8159500e.mp4
لینک دانلود نرم افزار  TunnelX ( داخلی ) :
https://uplod.ir/75m7wx9r6c17/TunnelX-v2.1.0__Whitedns.zip.htm
لینک گیت هاب TunnelX
:
https://github.com/MaxiFan/TunnelX/releases
امکان هست که آنتی ویروس  TunnelX رو حذف کند. در صورت نیاز اون رو به لیست نرم‌افزار های سفید آنتی ویروس خود اضافه کنید.
منبع تصویر کانال اینترنت آزاد
1️⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/whitedns/781" target="_blank">📅 17:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-780">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">+۲۵۰ ریزالور جدید به ربات تلگرام WhiteDNS اضافه شده
برای دریافت وارد بات شوید
@dns_resolvers_bot
و بعد دستور زیر را اجرا کنید
/dns_master</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/whitedns/780" target="_blank">📅 16:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-779">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/779" target="_blank">📅 16:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-778">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">لینک داخلی آموزش ساخت سرور شخصی StormDNS & MasterDNS
https://guardts.ir/f/d68436b0fc33</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/whitedns/778" target="_blank">📅 10:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJREsY94xI6gAkcvQXGoY88_-YfwRiaOt_Mppi1CNpYTPF9jBj7zfriLq2tnaqcUDB4lUVd7O6uTJoy9uRElsA54LIrOQJv23_hS4YaT9x7rONZUNGqMJdgdLN-sPYrj2l6pRXGuG1xHm48Per4OPdkTumFqr5xI18BZGS2iOsR-QkNifedEB_W-lUyyA7rutCmvlOZ3qoI40Hh6g-R04nWHzhXYT4VaEnU1L1BiUSk1TlB7jZ6NIGHbhalaJqUDEvqyOnZ7QE3XBYVu8vY7D3lx4Yd44LALejidb6jJ_269pIpbDSkmA46r0JHJgowNQ3_c77cgAQmS8MZW9U8V_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEjZ2OBy_kFk8oJW14OGMtBg20wIDUGUQ8ZcsZY4QUg8DPtPOyio1jtk-BMBbMwTLSnudZCQsoD4Y-nHQMEUrEj76uCEoRkIds2fSviIPkYam0R1uZhRoreBiJTfDSccUo65n1-A9YTASXufB_xn-NHn9Enk8Ak0NLdeWJd-Z37kaxU990NmaDLkAh9rFVNubmERaq4Mq8SzNg_F7IC6eVpr94t-oJG00YY70XE1A4Qy9Pqejw-MioVSb6f7ONm2JxBLiwqdFosWeYqfKPPs2BBpS5K0rQYZmGprds1GdWpN56328woVsWcsUsZBWhhUuQHPI2jcwEvfxhWNrM4oBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzoGl_LSTIKhLTUZ4zWGNCM3hzKPvW6RopacwSbDzIuETJAAPOoZQ7ruqm_wb4qeEHG65eUvH6OLXJkUCuRYJjQoHVd6Xl1lMM6ZwCeQB24FbxtxljoRes5jz2_KmYvGU2k29FvPI1Dk82J_qqiI05tENWYkPf2Mq5Ixt2NdgyT2ilxSpybUXuzOlLUTXTKPD9vemUOshomkDe9U6Fc-ciI5-F5qKwZIqhqaOyr7cDK8Y23O99YksFB-avFfwzJYfyj8emSRc0dxBDDoCTdvbYS6usQSpT0NS6vu5naMxP8YRBspd5nCpXNM2aXQlzx3hdGRWmzAy5ju3Lh5RIXDjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">- برای پیدا کردن سرور برای وصل شدن به تاپیک سرور برید
- برای راه اندازی سرور شخصی به تاپیک سرور شخصی برید
- برای آموزش و یادگیری اولین شروع با این ابزار به تاپیک اولین شروع برید
🫡
لینک گروه اصلی
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/whitedns/774" target="_blank">📅 07:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-773">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جمع‌بندی نهایی
تیم WhiteDNS تمام نشده، رها نشده و قرار نیست فقط به چند سرور عمومی محدود بماند.
برعکس، هدف ما این است که استفاده از WhiteDNS از حالت وابسته به سرورهای عمومی خارج شود.
کاربران می‌توانند با آموزش، سرور شخصی یا گروهی خودشان را راه‌اندازی کنند و اتصال پایدارتر و اختصاصی‌تری داشته باشند.
این روش برای اتصال حیاتی، شرایط سخت و دسترسی ضروری طراحی شده است؛ نه برای مصرف سنگین، دانلود زیاد یا انتظار سرعت VPNهای تجاری.
تیم WhiteDNS همچنان کنار شماست.
فقط قرار است از این به بعد، به‌جای اینکه فقط ماهی بدهیم، بیشتر ماهی‌گیری یاد بدهیم.</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/whitedns/773" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-772">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هدف اصلی WhiteDNS
هدف WhiteDNS کمک به دسترسی آزادتر به اینترنت در شرایط سخت و محدود است.
WhiteDNS یک پروژه غیرانتفاعی است و تمرکز ما روی ساخت ابزار، آموزش و کمک به کاربران برای داشتن راه‌های پایدارتر اتصال است.
ما همچنان مسیر توسعه اپلیکیشن، بهبود کیفیت، آموزش و نگهداری زیرساخت‌های فعلی را ادامه می‌دهیم.
اما می‌خواهیم کاربران کمتر به سرورهای عمومی وابسته باشند و بیشتر بتوانند اتصال اختصاصی خودشان را بسازند.</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/whitedns/772" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-771">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آیا دانش فنی زیادی لازم است؟
برای راه‌اندازی اولیه کمی دقت لازم است، اما آموزش‌ها طوری آماده می‌شوند که کاربران معمولی هم بتوانند مرحله‌به‌مرحله انجام دهند.
اگر هیچ تجربه‌ای با سرور نداشته باشید، شروع کار ممکن است کمی سخت به نظر برسد.
اما بعد از یک بار راه‌اندازی، استفاده از آن بسیار ساده‌تر خواهد بود.
هدف ما این است که این مسیر را تا حد ممکن ساده‌تر، قابل فهم‌تر و قابل انجام‌تر کنیم.</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/whitedns/771" target="_blank">📅 07:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آموزش‌ها کجاست؟
ویدیوها و آموزش‌های مربوط به نسخه اندروید، نسخه دسکتاپ و راه‌اندازی سرور شخصی داخل کانال قرار داده شده‌اند.
لطفاً قبل از پرسیدن سوال، داخل کانال سرچ کنید.
برای پیدا کردن آموزش‌ها می‌توانید این عبارت‌ها را جستجو کنید:
آموزش
سرور شخصی
دسکتاپ
اندروید
StormDNS
MasterDNS
Resolver
آموزش‌ها مرحله‌به‌مرحله منتشر شده‌اند و با کمی جستجو قابل پیدا کردن هستند.
همچنین داخل گروه اصلی تاپیک اولین شروع همه چیز رو توضیح داده
https://t.me/whitedns_group/32380/38590</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/whitedns/770" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگر سرور کند بود، مشکل از اپلیکیشن است؟
نه لزوماً.
کندی یا قطعی می‌تواند دلایل مختلفی داشته باشد:
- شلوغ شدن سرور عمومی
- ضعیف بودن Resolverها
- اختلال یا محدودیت سمت اینترنت ایران
- کیفیت پایین مسیر شبکه
- تنظیمات نامناسب
- استفاده تعداد زیادی کاربر از یک سرور مشترک
کیفیت نهایی اتصال به سرور، Resolverها و شرایط شبکه هم بستگی دارد.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/769" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چه انتظاری نباید داشته باشید؟
از WhiteDNS نباید انتظار سرعت بالا برای مصرف سنگین داشته باشید.
ممکن است شبکه‌های اجتماعی باز شوند، اما همیشه سرعت عالی نخواهد بود.
برای مواردی مثل این‌ها مناسب نیست:
- دانلود زیاد
- ویدیو با کیفیت بالا
- وب‌گردی سنگین
- استفاده هم‌زمان چندین اپلیکیشن پرمصرف
- انتظار سرعت شبیه VPNهای تجاری
این روش بیشتر برای دسترسی ضروری طراحی شده، نه مصرف سنگین روزمره.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/whitedns/768" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این روش برای چه کاری مناسب است؟
WhiteDNS و روش‌های مبتنی بر MasterDNS/StormDNS بیشتر برای شرایط سخت، محدود، ناپایدار و اضطراری ساخته شده‌اند.
این روش برای مواردی مثل این‌ها مناسب‌تر است:
- اتصال حیاتی
- پیام‌رسان‌ها
- دسترسی ضروری
- شرایط محدودیت شدید اینترنت
- استفاده سبک و کنترل‌شده
این روش جایگزین کامل VPNهای پرسرعت تجاری برای مصرف سنگین نیست.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/767" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استفاده گروهی با دوستان و آشناها
یکی از بهترین روش‌ها این است که چند نفر با هم یک سرور تهیه کنند.
اگر دوست، خانواده یا آشنایی خارج از ایران دارید، می‌تواند برای تهیه یا راه‌اندازی سرور کمک کند.
بعد از راه‌اندازی، اطلاعات اتصال داخل WhiteDNS وارد می‌شود و همان سرور به‌صورت اختصاصی‌تر برای شما یا گروه کوچک‌تان قابل استفاده خواهد بود.
این روش معمولاً از استفاده از سرورهای عمومی شلوغ پایدارتر است.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/whitedns/766" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هزینه تقریبی سرور شخصی
هزینه راه‌اندازی سرور شخصی معمولاً خیلی بالا نیست.
به‌صورت تقریبی:
شروع کار: حدود 7 دلار
هزینه ماهانه بعدی: حدود 6 دلار
البته ممکن است سرورهای ارزان‌تر هم پیدا کنید.
یک سرور حدوداً 6 دلاری معمولاً می‌تواند برای حدود 5 تا 10 کاربر سبک و معمولی کافی باشد.
اگر چند نفر با هم هزینه را تقسیم کنند، هزینه ماهانه برای هر نفر بسیار کمتر از اکثر سرویس‌های VPN خواهد شد.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/whitedns/765" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-764">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مزیت سرور شخصی
راه‌اندازی سرور شخصی یا گروهی چند مزیت مهم دارد:
- فشار کاربران عمومی روی سرور شما نیست
- پایداری معمولاً بهتر است
- در بعضی شرایط سرعت بهتری می‌گیرید
- احتمال پیدا کردن Resolverهای مناسب بیشتر می‌شود
- کنترل کامل‌تری روی تنظیمات دارید
- هزینه آن معمولاً از خرید VPN کمتر است
- می‌توانید با دوستان یا خانواده به‌صورت گروهی استفاده کنید
ابزار WhiteDNS برای همین ساخته شده که فقط محدود به چند سرور عمومی نباشد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/764" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-763">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چرا سرور عمومی جدید منتشر نمی‌کنیم؟
وقتی یک سرور عمومی در کانالی با ده‌ها هزار کاربر منتشر می‌شود، خیلی سریع زیر فشار زیاد قرار می‌گیرد.
در نتیجه:
- سرعت کم می‌شود
- اتصال ناپایدار می‌شود
- سرور گاهی از دسترس خارج می‌شود
- کاربران فکر می‌کنند مشکل از اپلیکیشن است
در حالی که مشکل اصلی معمولاً فشار زیاد روی سرور، محدودیت‌های شبکه، یا وضعیت Resolverهاست.
طبیعتاً یک سرور عمومی نمی‌تواند هم‌زمان برای هزاران نفر مثل VPN اختصاصی کار کند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/763" target="_blank">📅 07:48 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وضعیت سرورهای فعلی
سرورهایی که تا امروز توسط تیم WhiteDNS ارائه شده‌اند، همچنان نگهداری می‌شوند و تا جایی که امکان داشته باشد فعال خواهند ماند.
اما از این به بعد برنامه‌ای برای انتشار مداوم سرورهای عمومی جدید از طرف تیم نداریم.
اگر سروری متعلق به خود تیم WhiteDNS باشد، فقط داخل تاپیک «سرورها» اطلاع‌رسانی خواهد شد.
تمرکز اصلی ما از این به بعد آموزش، مستندات و کمک به کاربران برای راه‌اندازی سرور شخصی یا گروهی است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/whitedns/762" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تمرکز جدید کانال
از این به بعد تمرکز اصلی ما بیشتر روی این موارد خواهد بود:
- آموزش استفاده بهتر از WhiteDNS
- آموزش راه‌اندازی سرور شخصی MasterDNS و StormDNS
- آموزش نسخه اندروید و دسکتاپ
- آموزش پیدا کردن و تست Resolverها
- معرفی تنظیمات بهتر
- رفع اشکال و راهنمایی کاربران
- بهبود اپلیکیشن و اطلاع‌رسانی نسخه‌های جدید
هدف ما این است که کاربران فقط مصرف‌کننده چند سرور عمومی نباشند.
نرم‌افزار های ما طوری طراحی شده که بتوانید از سرورهای خودتان، سرورهای دوستان‌تان، یا هر سرور سازگار با MasterDNS و StormDNS استفاده کنید و اتصال پایدارتر و اختصاصی‌تر بسازید.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/761" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سلام به همه همراهان WhiteDNS
از امروز رویکرد ما در WhiteDNS کمی تغییر می‌کند.
WhiteDNS از ابتدا برای استفاده با سرورهای MasterDNS ساخته شده و همچنین از فورک StormDNS هم پشتیبانی می‌کند.
یعنی استفاده از WhiteDNS فقط محدود به سرورهایی نیست که از طرف کانال معرفی می‌شوند.
هر سرور MasterDNS و همچنین سرورهای سازگار با StormDNS می‌توانند داخل اپلیکیشن WhiteDNS استفاده شوند.
تا امروز، در کنار توسعه اپلیکیشن، تعدادی سرور آماده هم در اختیار کاربران قرار دادیم تا شروع استفاده برای همه راحت‌تر باشد.
👇
اما در ادامه یک سوءبرداشت ایجاد شد:
بعضی از کاربران فکر می‌کنند اگر سرورهای معرفی‌شده شلوغ شوند، کند شوند یا موقتاً در دسترس نباشند، یعنی خود اپلیکیشن WhiteDNS مشکل دارد یا قابل استفاده نیست.
در حالی که WhiteDNS فقط یک اپلیکیشن وابسته به چند سرور عمومی نیست.
قدرت اصلی WhiteDNS این است که هر کاربر یا هر گروه کوچک می‌تواند سرور MasterDNS یا StormDNS خودش را راه‌اندازی کند و از همین اپلیکیشن برای اتصال استفاده کند.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/whitedns/760" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">White DNS
pinned «
سرور جدید WhiteDNS   Domain: v.wdn.best Encryption Key: bad99364093861634030e96f11fe3132 Encryption: XOR @WhiteDNS
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/759" target="_blank">📅 07:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-758">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.wdn.best
Encryption Key:
bad99364093861634030e96f11fe3132
Encryption: XOR
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/whitedns/758" target="_blank">📅 06:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/754" target="_blank">📅 16:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0LCide5Dg6Vm_QaI9gw8gcfcdF9wPlQkbGLxCUPBTY0ieExmVn3RYJ7RcD_IiJvvKiK0GUc1uSYjOYcaBUk-gmrX9ABRygcnoWWDfuc36MLYouBB2DVDI8Koy6acgftn4UcqKZ1nchDDcR2gPSsdS_891w2eF3xReYSNwJpj2CSTPq__XaWTx8mkCn_L9sQw_913M6qEgfJYqoe_s1YRKNpCscbZenqp4kOszXg7XRyW0Ibibij34wfKctEHH6UeHJnGgWeBqqbqtGSZB8lK24wVc_ietDvxLSnfubsALdHpbWA43cl7Um0ytAkKUGwodtPk2_xMgJwONdcXB5tzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/753" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompythash</strong></div>
<div class="tg-text">سرور ها آپدیت شدن
دقت کنید هم رمز و هم دامنه تغییر کردن
سرور StormDNS اختصاصی چنل Pythash/پای هش
StormDNS Server Configs
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
@pythash
Domain:
v1.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
@pythash
Domain:
v2.pythash.tr
Key:
Telegram-Channel------->@pythash
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
نحوه اتصال:
windows , android:
https://t.me/pythash/74
linux:
https://t.me/pythash/81
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🌀
@pythash
🌀
@pythash</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/whitedns/752" target="_blank">📅 15:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/whitedns/751" target="_blank">📅 14:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/749" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VIN1tKXVeN0QFbUq0YrIegs7Kfs0hcr2yj6Azg9XIBa0_k3KZbouFBIvxgUZYK3Jq38qZzU-a4fYsbr8yfqascCCaBy4j7DmWnb7W8XfUr4V5j2-jAtHqTQ_ez5Xf5Vj6fIIQod7eps1tNAuGkngj99s5IlNy6CtLFB5f5LO6tLrHXzcAwHgEsKTiOE14dN6YHcMYalxU_nhsGYxQdHlv7UOAXatj6KxywuGwSwza_JbNsIuYXE-H3CcJ9mY4e9kWDCbMi1TrIYPE9RmH5eAPXTzMyaJMmZrw9JU04iyC7nd2srKqhCCSNjlgfiXqah1-MoNLmX9vMKrZT0MaSA0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/whitedns/748" target="_blank">📅 14:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-747">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-poll">
<h4>📊 🌷نظرتون در مورد نسخه جدید Whitedns windows چی هست ؟👀⚠️</h4>
<ul>
<li>✓ عالی</li>
<li>✓ خوب</li>
<li>✓ متوسط</li>
<li>✓ بد</li>
</ul>
</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/whitedns/747" target="_blank">📅 13:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-745">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leEPZOBsoAhmKdR0exaamayHGQf-r78YWRyzIYKGmtFPTxOFW1I5q8kkwQanr6itX6lqj4s7R_n27LgmZBL-TyKdBEPh-0Adac7TsaAzNkrrgc8ts-VmcUUvqnGSFzvNquXsRAHNgEAxQMuhCdgIZVTiUx3SyJ0kPE1abqZfViVEO4Wzn7IE5YZ3tffOGMWPxCo0hpOXAuQyiChBwiiftwJsV4tcdpmFGxtQxvGUJXokMo4kng_m6EdAedphNd4rvKACAgO4NTFamzAKKHL9cZpugJ2oAB1aaqRZXPvbw5CAOaIsfHr-x11_VInPjytguJJ1gOl1mGYes-JxJA1OVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYkGi4vXGpdKlZ6ZKTcAoLZeci9mXDGvyz1FC2G4P1HKknV1O2d_Z4JsCLMA_02ZPKiWZ3dwz4BKI-2cLSDGCcVHb5p4IfXLpwOdEZlK6JDwjk3kbhcMrHOKsKaOmN6UwRwA8LvVNbZrBRhupvcvZdkKeG0dy8k43nptAJR7I4O_SSUQwXZHbmx8xbL676v5dromeabj7AlNqA3Wogd99zhpWOBBWUF6Q1PL2BPkhX1Rargkhdo9-TaCw7FsUkF8M20TlZLrI8cRZMqwaodqVADMKE6AdWsFtBW4ONBdLfh7ig4akz7MeLiRmIL3wzbhvQ5FStxejTlfxMjgsPzZVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♨️
نسخه 1.0.0 Beta 3 ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS   نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/whitedns/745" target="_blank">📅 11:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-744">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
این گروه توسط جمعی از فعالین این حوزه مدیریت می‌شود و هدف، دسترسی مردم به اینترنت آزاد است.
چت کردن، صحبتی به غیر از دسترسی به اینترنت، تبلیغ، سؤال راجب فروشنده‌های VPN = مستقیم بن
گروه اصلی:‌
https://t.me/Ir_Blackout
گروه کانفیگ:
https://t.me/Ir_Blackout_Config</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/whitedns/744" target="_blank">📅 10:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-743">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">لینک های داخلی برای دانلود اپلیکیشن های دستکتاپ
⬇️
Windows
|
Linux
|
Mac
1
.0.0 Beta3
باتشکر از چنل
@masir_sefid</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/whitedns/743" target="_blank">📅 09:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-741">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-arm64.deb</div>
  <div class="tg-doc-extra">15.5 MB</div>
</div>
<a href="https://t.me/whitedns/741" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/whitedns/741" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-735">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/whitedns/735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/whitedns/735" target="_blank">📅 09:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-734">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1fa6eZgIARsg1HJMtSaA5UC5o8fc845W9Oud68Fs9GysfcQvsTyjg5FIqwBdPrnLdgoyD2J-KZj-jV-jbln5H_0NSpuNnpXBL6_acKqz3_YC9BvBrEhpF5iwxN9kCoX9bnmNTrELtoJRTZln-_TAMIDo0Na9Klk9e20XVEm1qGTxNaiXCYvMUNGmMy5Dec1e3YFcJ38Q2yixWhlr7AHNhblzXC_HplxDhK6T3hY7ZL9EZ9koKOy2O3fE38xxNqbRJn_uxVx5E8VNdLaWGK8a6QbYp3-1yZQnOE2fjxV5vE2d5F592pdxLovnRBB3rCMdvDP3E2FrYHT8EQ8RmArdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♨️
نسخه
1.0.0 Beta 3
ویندوز WhiteDNS منتشر شد
♨️
سلام به همراهان عزیز WhiteDNS
نسخه جدید ویندوز منتشر شده و در این آپدیت تمرکز اصلی روی بهتر شدن تجربه کاربری، تست سریع‌تر تنظیمات، مدیریت راحت‌تر سرورها و ریزالورها و رفع مشکلات گزارش‌شده بوده است.
🔅
قابلیت‌های جدید
✅
اضافه شدن قابلیت
Parallel Test
برای پیدا کردن بهترین تنظیمات اتصال
✅
اضافه شدن دکمه‌های جدید برای حذف لاگ، کپی لاگ، خروجی گرفتن از سرورها، ایمپورت DNS، خروجی گرفتن و ایمپورت تنظیمات
✅
امکان انتخاب نتایج اسکنر و ساخت پروفایل جدید بعد از اسکن
✅
امکان کپی همه نتایج اسکن، انتخاب دستی نتایج و کپی موارد انتخاب‌شده
✅
اضافه شدن قابلیت مرتب‌سازی تنظیمات، سرورها و ریزالورها
✅
نمایش IP ویندوز برای اشتراک‌گذاری اینترنت با موبایل و سایر دستگاه‌ها
✅
اضافه شدن قابلیت ریست تنظیمات برنامه
🔅
بروزرسانی‌ها و بهبودها
✅
بازطراحی و رفع مشکلات تب داشبورد
✅
اضافه شدن اسکرول در بخش‌های سرورها، ریزالورها و تنظیمات
✅
بهبودهای مختلف بر اساس گزارش‌های کاربران
لطفاً نسخه جدید را تست کنید و اگر مشکلی دیدید، همراه با لاگ و توضیح دقیق در بخش مربوطه گزارش دهید تا سریع‌تر بررسی شود.
ممنون از همراهی و گزارش‌های ارزشمند شما
🙏
@WhiteDNS</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/whitedns/734" target="_blank">📅 08:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-732">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.8 MB</div>
</div>
<a href="https://t.me/whitedns/732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
دوستان عزیز Linux, اپ دسکتاپ WhiteDNS Beta2 برای لینوکس هم آماده کردیم و میتونید دانلود کنید.
این نسخه بتا هستش  و ما در روز های آینده دایما با فیکس ها و فیچر های بیشتر آپدیت میدیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/whitedns/732" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-731">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8zBvx3TEfUQE6I1fKJGSOmJSn9DnSQpcrRtMpTqx85XTP9W7GeMwsEU63doDNaQU5fmQdVVRisuvupoZc7uGV6sPQNF869rIb7zugHZsnawCLB_5HXo40u-jv1_BPyrYH8QWApTNHs4c0wix0ocfWxRT8bslp3XnkhsH4QC04beaUwrHaGSYWgDadsDbT92-Ur5qSVkVlkLADCXKyO9LV23nZWCEmXZrJejAWC3u_2YsVKKVsvVCsj-K3lSGCu0iQ6n9vVfE0bTcZ4ymVKJB-4dS3dbhTKIbXslRTpOV7GoJ9kQq_rS11SJUluoGWk-7ahy_Uf9hiiHR-478_iChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل گروه اصلی تاپیکی ساختیم به اسم «اولین شروع» که یک توضیح کامل از وایت دی ان اس هستش + یک سری رکورد صدا که آموزش و نحوه استفاده کلی از اپلیکیشن رو آموزش میده.
لینک گروه
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/731" target="_blank">📅 17:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-730">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">لیست ۱۰۰ ریزالور موقفی که در ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدن
80.75.7.2
31.214.169.244
185.208.183.29
62.60.144.87
93.115.127.9
5.160.128.142
109.230.89.90
185.142.158.162
134.255.206.205
185.53.142.174
94.232.173.28
185.88.178.196
2.188.21.58
46.245.80.82
62.60.144.85
185.255.91.60
185.109.61.27
2.188.21.70
74.63.24.210
185.208.174.167
185.141.105.139
185.51.201.58
217.66.203.211
2.188.21.46
85.185.157.181
5.202.252.30
172.64.32.0
173.245.58.0
93.118.127.118
108.162.192.0
78.39.234.140
178.252.128.66
158.58.184.147
37.191.95.70
164.138.17.122
185.50.37.52
46.32.31.30
185.53.141.230
92.246.87.191
93.118.109.213
5.160.140.16
2.188.21.146
2.188.21.138
2.188.21.62
5.160.227.78
5.160.2.55
5.160.137.130
109.72.197.1
74.80.77.246
80.210.40.53
74.80.77.247
80.210.40.50
207.211.215.145
185.191.79.210
74.80.77.244
81.16.121.151
78.157.41.60
217.218.59.18
45.135.241.33
194.61.120.143
74.80.77.245
217.219.76.102
85.185.1.10
185.129.170.75
46.209.44.74
43.226.5.169
87.107.9.233
79.175.172.101
2.188.21.78
172.253.228.147
185.213.11.85
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/whitedns/730" target="_blank">📅 16:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سلام عزیزان، امیدوارم در این اوضاعِ به شدت خراب و زندگی در کشوری که توسط یک رژیم فاسد اداره میشه همچنان قویی باشید و حال دلتون عالی باشه. همونطور که میدونید ما
به شدت
با پروسه‌ی فروش
مخالف
بوده ایم و تمام فعالیت های ما برای
تمام
مردم ایران به صورت
کاملا
رایگان
بوده؛ اما جا داره که از تمام کسانی که چه با کریپتو و چه با استارز زدن به پست ها از ما حمایت میکنند تا فعالیت چنل و سرورها مداوم باشه، تشکر کنم. در این مدت دقت کردم که تمامی پست های چنل حداقل یک استارز خورده و بدونید که تمام این حمایت ها حتی یک استارزی که میزنید برای ما خیلی با ارزشه و از شما قدردانی میکنیم که در این راه دشوار و مبارزه با این حکومت خون‌خوار در کنار ما ایستاده اید!
❤️
- کوچیک شما Patrick.
WhiteDNS-Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/whitedns/729" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">لینک داخلی تمام پلتفرم های برنامه‌ی WhiteDNS Desktop:
Macos-amd64:
https://guardts.ir/f/736498ddfb14
Macos-arm64:
https://guardts.ir/f/4594c5008167
Windows-x64(amd64):
https://guardts.ir/f/2549b69980b3
Windows-arm64:
https://guardts.ir/f/05e3847a8a43
@WhiteDNS</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/whitedns/728" target="_blank">📅 13:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/727" target="_blank">📅 13:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فیلم آموزش استفاده از نسخه WhiteDNS Desktop</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/whitedns/726" target="_blank">📅 11:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtiIHaeu5bMz_w1hEygNxly5H5o1bIe41RXd59UjO4qGeltfsOvn8JQJVYAs0xNWeuQBDMJ_bBQAfeTrt8IL0kD0N7FO_8sVATpxUh7awRyT9Qf_HUIvQobvirksk-jMPWy_rx_Sdi7_UaN59cb_SNtn5RX7R6LYYAkV0Q8H4sFsvY0ypzs-1yUjGnMHHIakJUid_jikloSz-Lq_ogducOXKPjUKp5T5qHG00unnj_UyfGCZEj8K80_LpgG601FdEUD46zgEB_ss2fwTm7EnVRNkf21gRHQA5htYbwGAx9j_gD6W4pe4QWgOTpAIGVAPN2XP4r3d7rzWgxOhOZcCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی مک، دوستانی که مشکل باز کردن اپ رو دارید، دستور زیر رو اجرا کنید
chmod +x "/Applications/WhiteDNS Desktop.app/Contents/MacOS/WhiteDNS Desktop"
xattr -dr com.apple.quarantine "/Applications/WhiteDNS Desktop.app"
open "/Applications/WhiteDNS Desktop.app"</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/whitedns/725" target="_blank">📅 11:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta2-macos-amd64.zip</div>
  <div class="tg-doc-extra">25.8 MB</div>
</div>
<a href="https://t.me/whitedns/721" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه WhiteDNS Desktop V1.0.0-beta2
✅
حل مشکل باز کردن در ورژن های قدیمی مک
✅
حل مشکل وصل نشدن و خطا بعد از ۴۵ ثانیه
✅
حل مشکل وارد کردن کانفیگ به صورت گروهی
✅
حل اضافه شدن دگه ذخیره برای ریزالور های سالم و. فعال به صورت جداگانه
✅
حل مشکل مشکی شدن صفحه در ویندوز
✅
اضافه شدن نسخه های لینوکس</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/whitedns/721" target="_blank">📅 10:53 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
