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
<img src="https://cdn4.telesco.pe/file/YlG2sO76_HUFt5GnPwJRZsFzY0Afvtpvl1rxxhQ439-Tv_f0HL-bBdMzGEhN_GUqtdT-k3rPALhrJAB8iRFYIpmBD7OwCdftr7Poxk6Ma4UiIw_AijY1HTjesugHxNFBw0X--n4OkiU8g6Bg2Dk0OpQGKb46WBRw2X6HTaDcqLySzmsQ24SV7QJQaxN86p92D5NlRzkzbwk_rvLdNQaLlHQPoNSMimnGs1r-3S2K1vQlPj_zTi4HLUv9EhLgx0lrFw1yl6ERNCnIyvfgw8h4EeCIEvqOacSL54EzuYg_WtRJcNBfep6Ga1ndxvl9bI4ZOzy-Wozgysu4UTQ2I9rFZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 108K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 09:44:46</div>
<hr>

<div class="tg-post" id="msg-1171">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CWC1kFoxSYWgDRGijNdxdreAlpBoKDY2k1b6h1ibYsMS3V2khVGbCrtut_bE5lnT8iodIpW5MVBLV-GBskcrla4jhNt6Cepm3W3csxrr-47ACr-Rsl85Qcu5d5BVW38-6gh_ZD_dTGkDHylgoI_I51DMCQnd9NToFXlQl0YW9U-JltZ8C7xGfZ6Bk_eoRnICCHQW_Eucd1OOJW35rA599i5ASDkkhdsNAwhvdunQuKLRHXkhCHtWhIf7bPn88PWp7VYwUuExb-aIK0LSpc5Xnd9eSL1lzpSmHTd0OSd1-IUDnJy0egJ6sJVlHWyUEMa_e1hBCFb70SgOgLZcw57f8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش کامل راه‌اندازی V2Ray با پنل قدرتمند 3x-ui از صفر تا صد!
🎓
اخیراً با کاهش محدودیت‌های اینترنت، روش‌های باکیفیت و پایدار دوباره فعال شده‌اند. در این ویدیو،
WhiteDNS
🛡
تمام مراحل راه‌اندازی سرور شخصی و فیلترشکن اختصاصی را به زبان ساده و کاربردی آموزش می‌دهد:
🔹
سرور و دامین:
نکات کلیدی برای انتخاب سرور خارج و ثبت دامین در کلادفلر
☁️
.
🔹
نصب پنل 3x-ui:
نحوه نصب این پنل کاربردی با استفاده از هسته Xray بر روی سرور
🛠
.
🔹
ساخت Inbound:
آموزش مرحله به مرحله ساخت اولین ورودی برای فیلترشکن
🔄
.
🔹
تنظیمات کلادفلر (Cloudflare):
نحوه ثبت DNS ریکوردها و تنظیمات امنیتی ضروری
🔒
.
🔹
استفاده از آی‌پی تمیز کلادفلر (Cloudflare Clean IP):
روشی برای بهبود سرعت و دور زدن فیلترینگ با جایگذاری آی‌پی‌های تمیز
🚀
.
🔹
ساخت کاربر و استفاده از کانفیگ:
نحوه اضافه کردن کاربر و دریافت کدهای تنظیمات برای استفاده در برنامه‌هایی مثل v2rayNG
📱
.
این ویدیو یک راهنمای کامل برای کسانی است که می‌خواهند فیلترشکن اختصاصی خود را با امنیت و سرعت بالا راه‌اندازی کنند. اگر هنوز شروع نکرده‌اید، این فرصت را از دست ندهید!
✨
برای دیدن آموزش کامل، روی لینک زیر کلیک کنید:
👇
🎥
https://www.youtube.com/watch?v=vVjqNQBUGIc
🆔
@WhiteDNS</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/whitedns/1171" target="_blank">📅 09:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s0WoPALi9wMlRgoFJtRkOrhSYEHujGY9J7Jjjav_W9-fqkGegKdmpuZ2exmHtw6MZSlRu1YxIH5IqC3d2uZ0dHGWjho1rdHu6P7-Bp1vXHQAdiH1QLkBx2LZ-De4dsGJGsPELg8chXiofUzmGuenWZPPmLUogiOdVJHJyKIjwm3E_Hpoini5MYsBnyCrSJ2zDQ8N7tFDF1wjXwq7cHiWTerdrDenqLKcPF_G0mI329YXcV3xLTGVWfi7dgIJfntv4vfHn7J5ePoI_dJ8OBGI7QV9zEc-ckgn87KkA6-8lZZCLP1js9jJHDHFaxQRDwqkU6LslDQ-iav2FkKXslYv7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
اتصال رایگان و پرسرعت با پروژه Aether + پروتکل ویژه گیم Wireguard
⚡️
لینک پروژه‌ی اصلی:
https://github.com/CluvexStudio/Aether
لینک پروژه GUI من:
https://github.com/MatinSenPai/Aether-GUI
دستور نصب از ترموکس:
curl -fsSL https://raw.githubusercontent.com/CluvexStudio/aether/main/aether.sh -o aether.sh && chmod +x aether.sh && ./aether.sh install
دستور غیرفعال کردن محدودیت مصرف CPU و باتری:
termux-wake-lock
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره. حتی نیاز به اکانت کلودفلر هم نداره
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/whitedns/1170" target="_blank">📅 13:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1169">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kHYsnfVbu1a2qtbN7OVKs3KcU_1TMj16KE8-PQ9rcYcVrVKS8Km0UfXTFWcBZ-e1Ot2hlzoyVaG2opnW3DPkyQB_XLTwwheKPZLmAQlBiWLChkkh_Kg1f6P-lSTGtpJeBMHKoA5yE05bYzuFS2MNYIsf__l8Sgnia3enGTGVHm5nCOel8sIKKUDDZ4OhETMylzwJ31nadZfB9X4pL9TRKB7JxLMk6fyljN2F0V125ic7Qz13bwSp6aVah0TBlTczugfdHscqnesnvZTJsBYggwaJPDA4Z3i64wtH1wl5uZyJpCQ0gNWgbncOH_9H26n-FITdX3azawbBPlQDU-W_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر برای استفاده از سرویس‌های هوش مصنوعی (AI) مشکل دارید
🤖
این پراکسی را چک کنید
🔍
برنامه یک اپلیکیشنِ نوار منو (Menu bar)  و یک داشبورد محیط ترمینال است که به عنوان یک
مرکز کنترل و مانیتورینگ برای ایجنت‌های Claude Code
عمل می‌کند.
به طور خلاصه، این ابزار کارهای زیر را انجام می‌دهد:
نظارت یکپارچه بر ایجنت‌ها:
وضعیت تمام ایجنت‌های در حال اجرای Claude Code را در یک نگاه نشان می‌دهد؛ بنابراین دقیقا می‌دانید کدام ایجنت در حال کار است، کدام متوقف شده (خطا داده) و کدام منتظر تایید شماست.
بررسی وضعیت اینترنت و سرور:
به صورت مداوم وضعیت اتصال اینترنت شما و سرورهای Anthropic را چک می‌کند تا در صورت توقف کار ایجنت، دلیل واقعی آن (مثلاً کندی اینترنت یا مشکل خودِ Anthropic) را به شما بگوید.
حفظ لوکیشن (Location Fencing):
ایجنت‌های شما را روی یک کشور خاص قفل می‌کند. اگر VPN شما قطع شود، به جای اینکه ایجنت‌ها با خطای دسترسی (مانند خطای 403) از کار بیفتند، درخواست‌های آن‌ها را موقتاً متوقف نگه می‌دارد تا دوباره به اینترنتِ همان کشور متصل شوید و کارشان را از سر بگیرند.
ردیابی مصرف (Usage Tracking):
میزان مصرف واقعیِ محدودیت‌های اکانت شما را (با خواندن دیتای خود Claude) به طور دقیق نمایش می‌دهد.
https://ghhrmnzdh.github.io/tower/
🔗
@whitedns</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1169" target="_blank">📅 09:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1168">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns 15.7.2026.txt</div>
  <div class="tg-doc-extra">48.7 KB</div>
</div>
<a href="https://t.me/whitedns/1168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1168" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1167">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/VBqJXR0wp7DjVGkhnxoplnbs6A72lGy75v1YeeeCDfmxadHkKF-WAcwpX1v_NCASHEvbUUMVQc3hhe-gm4JE70nZxuU4rITb_4BbHffwCRBsUHTDpaxEEGpP2mdjIKpOAY3PhI34uMI-c8IoZgdm7hAFklOjPXapHL1B7fscA0nACdbZZjNn2Xk1AUC2-FheJ2wrwHiKxwcn_vU7V8gPh7inlenvGlmparWP_odxr_N8FWWslB-l6kJhY87f6UBlbpz8oV_xfsjenTyjUsdFiblNNZRsXY4t_FhWwXp714XGbjmrHKRzk2AwM6c66qnQKgTjP78lTfFdHZRWsvgUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">15.7.2025
📅
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1167" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1166">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سلام به همه
👋
یک موضوع مهم که خیلی از کاربران VPN با آن آشنا نیستند، مسئله‌ی DNS Leak یا همان نشت DNS است.
شاید برای شما هم پیش آمده باشد که VPN روشن است و آی‌پی شما تغییر کرده، اما بعضی سایت‌ها یا سرویس‌ها همچنان شما را به‌عنوان کاربر ایرانی شناسایی می‌کنند یا دسترسی‌تان را محدود می‌کنند.
DNS نشت یعنی چه؟
وقتی وارد یک سایت می‌شوید، دستگاه شما ابتدا از یک سرویس DNS می‌پرسد آدرس واقعی آن سایت چیست. اگر این درخواست به‌جای عبور از داخل VPN، از طریق اینترنت اصلی یا شرکت ارائه‌دهنده اینترنت شما ارسال شود، به آن DNS Leak می‌گویند.
به زبان ساده، با اینکه VPN روشن است، بخشی از اطلاعات اتصال واقعی شما هنوز قابل مشاهده است.
چرا مهم است؟
DNS Leak ممکن است باعث شود:
• موقعیت یا کشور واقعی شما تشخیص داده شود
• بعضی سایت‌ها همچنان دسترسی شما را محدود کنند
• حریم خصوصی شما کاهش پیدا کند
• اتصال VPN شما آن‌طور که انتظار دارید کامل و امن نباشد
چطور تست کنیم؟
1. ابتدا VPN را روشن کنید
2. وارد سایت زیر شوید:
https://ipleak.net
3. چند ثانیه صبر کنید تا نتیجه نمایش داده شود
4. بخش DNS Addresses را بررسی کنید
اگر در نتیجه نام شرکت اینترنت شما، کشور واقعی شما یا DNSهای مربوط به اینترنت اصلی‌تان نمایش داده شد، احتمالاً VPN شما DNS Leak دارد.
پیشنهاد می‌کنیم همیشه از VPNهایی استفاده کنید که نشت DNS ندارند تا هم حریم خصوصی بهتری داشته باشید و هم سرویس‌ها کمتر بتوانند موقعیت واقعی شما را تشخیص دهند.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1166" target="_blank">📅 08:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1165">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Whitedns-14.7.2026.txt</div>
  <div class="tg-doc-extra">241.5 KB</div>
</div>
<a href="https://t.me/whitedns/1165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1165" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1164">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZpMIOIReKPgU7mWnnkqXfVfLzbSZ5VSmN9pyhdDm4j-_f-HmvCXHAden6u8lsLfVnSTCC2x3WgbNHpmk3-0S1OCnsjegZLOKDh5_KfjBKbOz6SVVh6mNHoDYD90nBS-yigihxNNYWw_XUWblDTxRH8jlHJvW57zvZinMxl0iojj2PIhg_aXYUpQOcYe1BivSvvY966Md-5-BBmuga7q-nu5eDgDzluHo-zwqFsth8s41d5ngDiTsx0EDad6W_hfExi8ft3GyGLtjYa8XxceD-hOaWQEwVPndzw445CrFL9TAoBI4tLtYt-KWhbHsbp_W-XbODmqt4CeMvr2tvBoavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14.7.2026
فایل زیر را دانلود کنید
⬇️
1. کانفیگ‌های داخل فایل را کپی و در برنامه v2ray وارد کنید
📋
یا
2. خود فایل را از طریق گزینه import locally در برنامه v2ray وارد کنید
📥
@whitedns
🔗</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1164" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/c-iOKgnX6MKdB_c74ohXA6_5xtp7AoXryK2izY7_4s1SNyIX8fgSbeS1FPvvIdYgVHC2I5c3cd0gz4NkNs9p7iBdn9gO6geEDfieerorsyA7yCALG3sSDQuP0h9tbf7NCaCoMG3-zlTYoxfN-7DIkAZ1FTbL498lC9uqwQwjTS1Y73bvN3ilTzk2alq8p_lcT78Q5waj-Y5jom2p9-rr4v5pQEfgtzB-YwEpR_xzw4at9vwnyN7X-Aa0VWlyxuamj-FCPs1VQQXI9tGIrs-jTfQZ1rXsu_xrL7TXwZMTNCp71SohDSmTfaAyWqe9yL3INd8EWahqKS3zV1qxzxOtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1163" target="_blank">📅 17:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">White DNS
pinned «
👆
⭕️
⭕️
⭕️
⭕️
موقت :   پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد   این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1162" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👆
⭕️
⭕️
⭕️
⭕️
موقت :
پرونده اتصال سریع و اسان برای افرادی که دانش و امکان درست کردن کانفیگ ندارند با چند پست بالا بسته شد
این مدل اتصال در صورت قطعی  سراسری کار نخواهد کرد
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1161" target="_blank">📅 17:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-IP-Scanner-x86_64-release.apk</div>
  <div class="tg-doc-extra">15.6 MB</div>
</div>
<a href="https://t.me/whitedns/1156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اگر براتون سوال پیش اومده که لیست ipfronting ها را از کجا آوردیم . پاسخ خیلی ساده است
😊
👇
با استفاده از Whitedns Ip finder
🛠
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
📂
@whitedns
📱</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1156" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Zo3_3oxGEnIviOYBR3X98xmQ4zOvI98pU3nJ_1ih9JG7Y_VVIBGgHQ4Gr4uwus9HYXuAbrczah2xQi0MwxfEMwbyXwz6FzT8JzSKaoXo-qG-52tZYfp4UCzDh01aFv9WWGgOIYlC24XRTvyK74ZbamQdZE1dT7ro56kI9L8QDrserJzsan2c8s7SFQoiQtBYz4mQjTPQNgytvdUI8wtfjS-Drbk9pWlkzaWGjo8X1aMPhhl3RJlKLV_ut3mEMR7zxNGfzn3W9EgpeU638gePrKZlYaUN3WjGQYEAV77A22mJiK7Sw466Qg_q5UJOeCV-qk1mQL4HMhV2b4hh4KkMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1155" target="_blank">📅 17:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lax9HollXsr_zRFmXDKPAqUmWqJHYN2_HO5yN7jw06jLSwJ83c5f4e8miF9_1DKqShVgOBTJdUfT-ErO8ju89FfNbCsN6D51z8PlR47FicPHZot_wAbdyaIVgC1kUWc2G27sjx31H4uwl7hVFdhWJuD2c9oCVyHiCbQBLHQu1OhUez6MMavEZkViO77560DFGh6gVLNjeZQTGYyQRr4p-_MU26rChYXEzyQFQhyAGSEMY0syrEYwpvygCFUKTqXVYA0nwt4UjjaxFvEMKt4-tX5TrM1dFujuckqduDDJStQ3MfXo5ISS4BydWuKiVyPnwlTAq1ofIr8b00aa9M4zPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان :
در صورتی که موفق نشدید با برنامه whitedns vpn وصل بشید
🙄
🔌
وارد قسمت advanced بشید و ای پی های زیر را دونه دونه امتحان کنید
👇
🛠
2.189.86.45
2.189.86.102
2.189.86.42
2.189.86.46
2.189.86.41
185.8.173.179
2.189.86.44
45.149.77.160
194.62.43.166
94.101.184.211
37.152.185.169
37.152.182.54
185.226.118.234
185.231.182.55
185.226.118.234
185.231.182.55
185.226.117.67
185.228.236.4
2.189.86.43
2.144.21.79
2.144.21.120
2.144.21.79
2.144.23.129
2.144.21.120</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1154" target="_blank">📅 17:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">White DNS
pinned «
دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1152" target="_blank">📅 16:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوستان :
👋
یک مورد کوچیک در مورد whitedns VPN بگم
📱
این اپلیکیشن بر اساس کانفیگ های متناسب با هسته x-ray یا سینگ باکس هست ، به طور مثال vless ,vmess, Trojan ,....
⚙️
اگر وصل شد حتما اول با مرورگر یک تست بگیرید
🌐
، اگر هیچی باز نشد ، دکمه refresh را بزنید
🔄
اینقدر این کار را تکرار کنید تا یک کانکشن پایدار متناسب با وضعیت شما براتون پیدا بشه و هر بار تست کنید روی مرورگر
🧪
✅
تیم whitedns
👥
@whitedns
📩</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1151" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1146">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن Whitedns vpn 0.0.8
📱
یک برنامه بر پایه هسته‌های x-ray و singbox است که بدون نیاز به وارد کردن اطلاعات و تنها با فشردن دکمه‌های Connect یا Refresh، به راحتی یک اتصال اینترنت مناسب ایجاد می‌کند
🚀
🌐
.
ٌ
@Whitedns</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/whitedns/1146" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1145">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/R72vSP74vYAcCkOojcSBvYjqqJIZ7BOV-9yOg3zMqTJBHuobf8T34oNF2ZF9sUHxOROGz69nzYVbM4_OQPHS3jGZG9pPa_eFTZybOgLAuGVJi5iaEnl7dRlJq4t_MRPBClTN4nhbgR3QGVkIghUGzDFn8lT_HXZo3jjzd3SWXk_bI-kc_TEuHN5oodwkp96wjzkcKcz78HayYwhrwRruKnDAWDBPYNXBRSMLOhuLY4dPt5atp68UE74dikLm0L0ZFNgpRJg4acrq1HxNSugKnMKu1diYgh5LgiV9Din3KBeaA9TZy1nw4WjhHDukLzlmXvc2L2e2TPSsj8Gm0JpjfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1145" target="_blank">📅 16:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">برای اینکه دوستان قاطی نکنند، ما دو نوع اپلیکیشن برای اتصال داریم
📱
:
۱
. اپلیکیشن بر پایه پروتکل‌های DNS محور مثل masterdns, stormdns, ...
🌐
مثل Whitedns 1.5.1
۲. اپلیکیشن بر پایه هسته‌های x-ray, singbox که پروتکل‌هایی مثل vless, vmess, ... دارند
⚙️
مثل  0.0.8 whitedns vpn</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/whitedns/1144" target="_blank">📅 16:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1136">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-poll">
<h4>📊 وضعیت اینترنت چطوره ؟</h4>
<ul>
<li>✓ ☺️مثل قبل هست  , وصلیم</li>
<li>✓ 😔اختلال داره ولی وصلیم</li>
<li>✓ 😡اختلال شدید ، به ندرت وصل میشیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1136" target="_blank">📅 16:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1135">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🛡
مدتی پیش اپلیکیشنی برای اسکن Resolverهای متد DNS ساختیم که می‌توانید آخرین نسخه‌ی آن را از لینک زیر دانلود کنید:
https://github.com/WhiteDNS/IP-Range-Scout-Android/releases/tag/v0.1.2
اگر امکان اسکن Resolverها را ندارید، می‌توانید از ربات ما استفاده کنید:
@dns_resolvers_bot
همچنین اگر برای اولین‌بار از WhiteDNS استفاده می‌کنید، پیشنهاد می‌کنیم در گروه اصلی، تاپیک «اولین شروع» را مطالعه کنید.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1135" target="_blank">📅 03:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1134">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه. با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1134" target="_blank">📅 03:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1133">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
با توجه به شرایط کنونی خاورمیانه، ترجیحا هم اپلیکیشن WhiteDNS را نصب/آپدیت کرده و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1133" target="_blank">📅 00:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1129">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn4LRK-rAo1GRJVRs-L0wb2PBNGyt9DIZFqrTAAvU1VN4NBH_vNItUJL9VIDdJkOApZpyPCn4yfH73fKchtCkkPvWEJ9YJ8yZgBXCERhbuMw2_pcr_BiXKNK6veUrk1e38_c05bNhfwZffQWd7Iw9_bM4_BrmRPImSyRPG-8MiNqJxkJ6MNUraV2hD1olOZYZmrPcxsD_Ll-Ms4-CJ6_7Sh9CSjOae2wRpea4NCGxLSEbYsAqKGongah0sl6ldGjSFw7OoRyWM_hYpzbSiyjlDxdB_b-LfVfSL9FtTcYSD0aSpNvtOJ7nzZju1ZEYANgpgd4UH0a2vf_hAPUpoztxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/whitedns/1129" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1127">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1127" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1126">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AIOor5yKvLMmPdk0y3rNvkgO-Q5_xU8fkWE6lydtsxlZxqQi6BbtyUCSkqiXjUXohfbKtOvaaFFE2Swvj4vxECXX-afu7Fepq_Uw9t3ENmEMjqQGPERTBe_xD9WxpBVqlUcref6uWMIpQ6Y1e29VkFzBg3ojiRYCmUPcEodcNORenWF2H53wgs8B9SA7D49tInxguZJmG7NvFDGUP0vemInKrcqIyj2FoZxftQ4jy1GiwdEynivL5m2CW7cnDnz-aso_2rFeA5JSKJuJ-hXT9li7Sk3joUH8v67rPTOKc2--jJNYp0N0yCSknju8w3XEXKX-lV3p4Qi-0jgGSp8D1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsResponder_bot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/whitedns/1126" target="_blank">📅 13:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1125">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">White DNS
pinned «
⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم  با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.  در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1125" target="_blank">📅 10:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1124">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🌎
آموزش کامل WhiteDNS Desktop براز مان قطعی اینترنت
لینک مشاهده ویدیو
https://www.youtube.com/watch?v=Mc--GlKw2wg</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/whitedns/1124" target="_blank">📅 05:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1123">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/whitedns/1123" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1122">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMasterDnsVPN</strong></div>
<div class="tg-text">👋
درود،
⬅️
ایران موشک بخوره یا موشک بزنه اعضای اینجا زیاد میشن، همه چیز آروم باشه اعضای اینجا کم میشه، تعداد ممبرای این کانال شده یه چیزی مثل «شاخص پیتزای پنتاگون»
😂
⬅️
ولی من واقعا دوست ندارم، اینترنت قطع بشه و شمارو دوباره سر همون موضوع قبلی اینجا ببینم
😕
امیدوارم وضعیت اینترنت جوری درست بشه که اعضای این کانال صفر بشن، ولی مارو یادتون نره
😁
❤️
پیروز و سربلند باشید.
🤨
با تشکر فراوان،
امین محمودی
🗓
18 تیر ماه 1405</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/1122" target="_blank">📅 02:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1120">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/whitedns/1120" target="_blank">📅 10:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1119">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS فیلترشکن ساده و قدرتمند مخصوص آیفون  دوستان عزیز،  اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight: https://testflight.apple.com/join/u1vfEHur   CoreForge برای…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/whitedns/1119" target="_blank">📅 10:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1118">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🛡
معرفی CoreForge برای iOS
فیلترشکن ساده و قدرتمند مخصوص آیفون
دوستان عزیز،
اپلیکیشن CoreForge برای iOS آماده تست عمومی شده و می‌تونید از طریق TestFlight نصبش کنید.
📥
نصب CoreForge از TestFlight:
https://testflight.apple.com/join/u1vfEHur
CoreForge برای شرایط سخت اینترنت طراحی شده؛ مخصوصاً زمان‌هایی که اختلال شدید داریم، خیلی از روش‌های معمول وصل نمی‌شن، یا حتی اینترنت به سمت حالت بسته و محدود می‌ره. خلاصه برای همان روزهایی که اینترنت تصمیم می‌گیرد انسانیت را ترک کند.
این اپ دو حالت اصلی دارد:
✍️
RelayForge
حالت پیشنهادی و روزمره برای استفاده عادی
مناسب وب‌گردی، اپلیکیشن‌ها، تماس، شبکه‌های اجتماعی و استفاده عمومی
✍️
DnsForge
حالت اضطراری برای زمان‌هایی که بیشتر روش‌ها بسته شده‌اند
این حالت از تونل DNS استفاده می‌کند و برای شرایط قطعی شدید یا اینترنت ملی می‌تواند کمک‌کننده باشد. سرعتش مثل VPN معمولی نیست، اما برای دسترسی اضطراری، پیام‌رسان، وب ساده و کارهای ضروری طراحی شده.
🛡
قابلیت‌های مهم CoreForge:
• مخصوص iPhone / iOS
• اتصال ساده و سریع
• پشتیبانی از کانفیگ و اشتراک
• تست و انتخاب بهترین مسیر اتصال
• حالت Full Tunnel
• حالت اضطراری DNS Tunnel
• مناسب دوران اختلال شدید و قطعی اینترنت
• طراحی شده برای استفاده ساده، حتی برای کاربران غیر فنی
📌
نکته مهم:
DnsForge آخرین راه‌حل است. یعنی اول از RelayForge استفاده کنید، اگر روش‌های معمول جواب ندادند، سراغ DnsForge برید. اینترنت خودش به اندازه کافی اذیت می‌کند، ما دیگر لازم نیست داوطلبانه سخت‌ترش کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/whitedns/1118" target="_blank">📅 10:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1117">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♨️
معرفی ربات جدید WhiteDNS برای راه‌اندازی و مدیریت سرور شخصی MasterDNS
♨️
ربات جدید WhiteDNS آماده استفاده است.
👉
@WhiteDNS_installer_bot   این ربات به شما کمک می‌کند بدون نیاز به درگیر شدن با مراحل پیچیده نصب، سرور شخصی MasterDNS خودتان را روی VPS راه‌اندازی…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/whitedns/1117" target="_blank">📅 06:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1116">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8AJ6bxwn7dn8TBmRygdhc15re-sMugMuKCbFrz3k9NAx-DLSX7DQxv6IbGBuGyq_UPSufPng4UhUW_0MPXp7PrTVM9JSOH0d1J6iOSrzrNEpMfp6f_rPHi7KZLZE4RSKhzXa5ntfhUYGGEY34mEDSLeDn-gsuoXlIlG1bQn-kRCW_nNK76uWw7uct40x9jWHZKebo8rpveCxFC1LQOkPMGkgXLi6hBk8XrgSO2t3PvnI2X0t7iQBg7mDltXDcQnEa2GiZYfQvXR_ccXML-SSqquUAOzf9XpO4lWn3ASQw_C8w0XakTiROc06nHyxWY_SHlvcDT5QauESrnwGFIMsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1116" target="_blank">📅 06:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1115">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✍️
دوستان :
آیدی ادمین که توی دیسکریپشن کانال گذاشته شده، برای حل مشکلات شخصی شما نیست. ممنون که لطف می‌کنید و درد دل‌های روزانه خودتون رو برای ما می‌فرستید، ولی متاسفانه قادر نیستیم پاسخگو باشیم چون تعداد پیام‌ها خیلی خیلی زیاد هست.
اینکه موبایل شما و یا کامپیوتر شما دچار مشکل شده، یا اینترنت شما کار نمی‌کنه، شرکت تامین‌کننده اینترنت شما کلاه سرتون  می‌گذاره، و یا اپلیکیشن‌هایی که ما گذاشتیم دچار فلان مشکل هست و غیره رو برای آی‌دی ادمین نفرستید، توی گروه مرتبط با خودش مطرح کنید.
آیدی ادمین فقط و فقط برای مواردی هست که شما قادر نیستید توی گروه های عمومی ما براش پاسخی پیدا کنید (که تقریبا غیر ممکن است )و یا گزارش و یا یک مورد خیلی فوری را میخواهید به دست تیم ما برسونید
در ضمن بازم تاکید می‌کنیم برای اون دسته از دوستان طلبکار و بی ادب  ، شما حقوق ما را نمی‌دید و ما هم از جایی بودجه نمی‌گیریم ، ما بدهی به شما نداریم ، بی ادبی شما جوابش فقط بلاک شدن و حذف شما از کانال و گروه های ماست ،
از امروز مواردی غیر مرتبط به هیچ عنوان پاسخ داده نمیشود
سپاس
❤️
تیم whitedns</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/whitedns/1115" target="_blank">📅 10:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
اگر داخل پنل های نهان و bpb یا هر فیلترشکنی که دارید مشکل باز شدن یه سری اپلیکیشن ها رو دارید(تلگرام،یوتوب و...) طبق تنظیمات زیر داخل هر کلاینت برید این تنظیمات رو داره:
Dns:
💎
9.9.9.12
8.26.56.26
8.8.8.8
8.8.4.4
208.67.220.220
208.67.222.222
Fragment:
✅
Google.com
Length:10-20
Interval:10-20
Packets:1-1
💡
نکته:قسمت فرگمنت بیشتر برای مشکل آپلود یا باز نشدن اپ هاست لذومی نیست حتما روشن کنید.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/whitedns/1114" target="_blank">📅 04:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1113">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oyy9URg9u1fNZc8uAEmJfxWLqs4GapsdFZ4afPHGkX0WqUglRuqQMG1L8bhgtFUbHoPcLs0oEpEiFXZWuvr3tAKd58Hmp2_ETFOTKnh5IEC5fIevxsUpWozEUZgwA5VWAfyh96AI9C7GAOGSb2XiiuIPxPGXlSZGPkWe1bWcwgvuOsIIRZeZXqNq9N3bYaVcECmueDu5HCkeJ0YYQswiYZkB72YOurFGmolLXYeDzzhNwb2ptlGNvfmIeErfeufrwFH6NaeyJLn3qMhU3pZ53fY2Ks0KMknlAV4o01j-70T5qo_o-eCyGc7KwvN4WzFhgR8edMQBGCS6xgq_ckSEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/1113" target="_blank">📅 20:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhitednsProxyProfiler-Android-v1.0.7.apk</div>
  <div class="tg-doc-extra">55.4 MB</div>
</div>
<a href="https://t.me/whitedns/1110" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروفایلر پروکسی WhiteDNS نسخه ۱.۰.۷
🛠
پروفایلر پروکسی WhiteDNS یک ابزار تشخیصی برای ویندوز و اندروید است که بهترین ترکیب‌های پروتکل پروکسی/VPN را در یک شبکه پیدا می‌کند. این ابزار می‌تواند هم بررسی‌های محلی بدون VPS و هم تأییدات عمیق‌تر مبتنی بر VPS را اجرا کند.
🌐
ویژگی‌های اصلی
اسکن شبکه محلی:
آزمایش سریع بدون نیاز به اعتبارنامه‌های VPS.
🏠
اسکن VPS:
تأیید از راه دور عمیق‌تر با استفاده از اعتبارنامه‌های VPS شما.
🖥
تست پروتکل‌های VLESS، VMess، Trojan، Shadowsocks، WireGuard، Hysteria و HTTP.
🚀
پشتیبانی از انتقال‌های TCP/RAW، WebSocket، gRPC، XHTTP، HTTPUpgrade و mKCP.
🔄
پشتیبانی از ترکیب‌های TLS، REALITY و بدون امنیت (در صورت معتبر بودن).
🔒
تشخیص دسترسی‌پذیری، فیلترینگ، پورت‌های مسدود شده، مشکلات SNI/TLS و رفتارهای شبیه DPI.
🔍
نمایش نتایج تشخیصی دقیق و اطمینان از شواهد محلی.
📊
کمک به شناسایی ترکیب‌های ایمن‌تر پروتکل، پورت، انتقال و امنیت.
🛡
نحوه استفاده
برای یک آزمایش سریع بدون VPS، گزینه
اسکن شبکه محلی
را انتخاب کنید.
⚡️
از
تنظیمات پیشرفته
برای تست پروتکل‌ها، پورت‌ها، مقادیر SNI، انتقال‌ها و انواع امنیتی بیشتر استفاده کنید.
⚙️
وقتی به شواهد قوی‌تر سمت سرور نیاز دارید، گزینه
اسکن VPS
را انتخاب کنید.
🌍
آی‌پی VPS، پورت SSH، نام کاربری و رمز عبور یا کلید SSH خود را وارد کنید.
🔑
اسکن را شروع کنید و پروفایل پیشنهادی کارآمد یا نتایج تشخیصی را بررسی کنید.
✅
نکته مهم
اسکن محلی نشان می‌دهد که شبکه فعلی شما به چه مواردی دسترسی دارد. اسکن VPS شواهد قوی‌تری ارائه می‌دهد زیرا هم سمت کلاینت و هم آنچه واقعاً به VPS می‌رسد را بررسی می‌کند.
🧐
نسخه:
۱.۰.۷
🏷
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/whitedns/1110" target="_blank">📅 19:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام
❤️
توی این آموزش، تمام بخش‌های برنامه V2Ray را از مبتدی تا حرفه‌ای به‌صورت کامل بررسی کردیم؛ از اضافه کردن کانفیگ و Subscription گرفته تا تنظیمات پیشرفته، Routing، آپدیت برنامه و حالت‌های مختلف Tunnel.
🇺🇦
لینک آموزش در یوتیوب:
https://youtu.be/i1-XenoSalk?si=5jbQK3BrGAe4ctsu
اگر موضوع یا نرم‌افزار دیگری هست که دوست دارید آموزش کاملش را ببینید، داخل کامنت‌های یوتیوب یا گروه تلگرام پیشنهاد بدید تا برای آن هم آموزش تهیه کنیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/whitedns/1109" target="_blank">📅 18:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr Alan(Dr . A)</strong></div>
<div class="tg-text">چجوری کانفیگ رایگان بسازم بدون دردسر؟
🤔
همه چیز با یک کلیک در WhiteDNS BPB
🚀
مرحله 1:
اول از همه برنامه رو نصب کنید و وارد برنامه بشید
📲
مرحله 2:
وقتی وارد برنامه شدید دکمه Connect CloudFlare رو بزنید
☁️
مرحله 3:
وقتی به مرورگر هدایت شدید، اطلاعات حساب Cloudflare خود را وارد کنید
🔐
مرحله 4:
بعد از وارد کردن اطلاعات به یک صفحه منتقل میشید که از شما میخواد اجازه استفاده WhiteDNS BPB رو از اکانت کلادفلر خودتون رو بدید. برای این کار به پایین صفحه اسکرول کنید و دکمه آبی رنگ Authorize رو بزنید
✅
مرحله 5:
دو حالت وجود دارد. یا شما میخواد یک برنامه رو انتخاب کنید که باید برنامه WhiteDNS BPB رو انتخاب کنید. یا به یک صفحه دیگه منتقل میشید در این حالت به برنامه WhiteDNS BPB برگردید و دکمه I Finished رو بزنید
🏁
﻿
مرحله 6:
بعد از اتصال حساب کلادفلر شما به برنامه، به تب(بخش) Bpb Deployment برید و دکمه eCreat Panel رو بزنید
⚙️
مرحله 7:
به یک صفحه منتقل میشید که میتونید تغییرش ندید و بزارید در حالت پیش فرض بمونه و دکمه آبی رنگ Create Panel رو بزنید
مرحله 8:
بعد از کمی صبر پنل شما با موفقیت ساخته میشه. دکمه Subscriptions رو بزنید و اولین ساب رو کپی کنید
📋
مرحله 9:
میتونید اون لینک ساب رو در برنامه های v2ray / v2box ... وارد کنید یا از داخل تب VPN در برنامه WhiteDNS BPB لینک رو وارد کنید و همونجا به کانفیگا وصل بشید
🌐
⚠️
توجه:
به هیچ وجه از ایمیل های فیک و رندوم استفاده نکنید
🚫
حتما باید اکانت کلادفلر شما Verify شده باشه در غیر این صورت با خطا مواجه میشید
❌
اگر از فیلترشکن استفاده می‌کنید، توجه داشته باشید که باید ایپی شما ثابت
باشه
🛡️
لینک دانلود نرم افزار:
https://t.me/whitedns/1018
@WhiteDNS
با تشکر
🙏</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/whitedns/1108" target="_blank">📅 04:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1106">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🛡
آموزش کامل نصب و راه‌اندازی سرویس MTProto با ابزار MTProxy
فیلترشکن قوی و پرسرعت برای تلگرام
https://www.youtube.com/watch?v=pyvB6VSPhwg
@WhiteDNS</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/whitedns/1106" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا یکی از بچها زحمت کشید یه ویدیو کوتاه واسه این ابزار درست کن با کمی بهینه و میانبر واسه دریافت توکن که میتونید ببینید و واسه خودتون و خانوادتون فیلترشکن رایگان بسازید
✅
ویدیو یوتیوب:
📹
https://www.youtube.com/watch?v=e8FNffowfYo
بات دکی:
👑
@itsyebekhebot
نوا پروکسی دریافت توکن:
✅
https://novaproxy.online/install
داشبورد کلودفلر:
💎
https://dash.cloudflare.com
ایمیل فیک:
⚡️
@TempMail_org_bot
خلاصه: داخل ویدیو نحوه دریافت توکن آسون تر شده و این که یه سری بهینه سازی هم داخل ویدیو هست
❗️
@yebekhe
👑
@mehdisedighinasab
💎
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/whitedns/1105" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">↗️
تعداد کانکشن های موفق WhiteDNS VPN در ۲ هفته به ۱۰۰هزار رسیده
.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/1102" target="_blank">📅 15:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSaFNoiGUVrxPVFrZMl3Jwn0vRLEdkWZly-pz8g2yibv9Ts_d3hjxTm7g7Wez6ownSb9kGjzXdSzQIblJMzMuMJb0S1il8SCWZjVNDqQIW4MvE63gd-C4cResXdKve_EyDp6dBiiTE5Ch19ZRT5REjmGCTeVABvR-lz4Yey44AbTnQH7OUyz0dcRcefDZzqDR_AhGwk2xd9jEDvckuAN0VCrQcOOVd8Gk6BW4FRZyY337PVv-VnqtVIIYFCuT0V3IunDqaY4cXBU3UPVLKtyCXD63yjbZPLucNZJ0qIDSKRY6zyYqNjuicAuH0dxzMCeXsPVlqvMyDCK7IUG4Bozkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
دوستانی که امکان اسکن ندارند، می‌توانند از تاپیک «IP تمیز» در گروه استفاده کنند. دوستان دیگر IPهای تمیز را آنجا به اشتراک گذاشته‌اند و می‌توانید از همان‌ها استفاده کنید.
لینک گروه
https://t.me/+-Uc2AHI2d8Q2MzA0
آموزش استفاده از IP سفید
https://youtu.be/N5hKuWXp37w?t=1092&si=mdL0Q8Q9H039IAiL</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/whitedns/1101" target="_blank">📅 08:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1100">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=LJvyJzPSftNqpM3yBlf47oQgf1QhrSP8hgBqFGhoHrzCr9wErBSKgEIsPqPTSK7StSNlOcVfljgzIUzwyadSpsY0fLyAn9X_ojLy_8fsgs9XaC2G7mvmopr6d3NqowWF-FdrLl0FmxhO5u37MGahkBmI7wQQv9N0ixeD6Mudok0vZAgEzh7dX4kpxczYJ59cnAGnqjddDtYaVMXbKlKEMFDOkFl_Hh_wm-1HKmU3rNfaMZ8FNIBIB79fiALi0bhh7WhSchZdLgGsvB4dYGVBujVYAn69bJ2z3mfy7umxWhSZ6smbhbNKh8-XWJXWANjXWMXHWWyHcR2kt8MQD4I8poi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56bbdb4680.mp4?token=LJvyJzPSftNqpM3yBlf47oQgf1QhrSP8hgBqFGhoHrzCr9wErBSKgEIsPqPTSK7StSNlOcVfljgzIUzwyadSpsY0fLyAn9X_ojLy_8fsgs9XaC2G7mvmopr6d3NqowWF-FdrLl0FmxhO5u37MGahkBmI7wQQv9N0ixeD6Mudok0vZAgEzh7dX4kpxczYJ59cnAGnqjddDtYaVMXbKlKEMFDOkFl_Hh_wm-1HKmU3rNfaMZ8FNIBIB79fiALi0bhh7WhSchZdLgGsvB4dYGVBujVYAn69bJ2z3mfy7umxWhSZ6smbhbNKh8-XWJXWANjXWMXHWWyHcR2kt8MQD4I8poi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://www.youtube.com/watch?v=Z069VNFAgAc
ایجاد بی‌نهایت آدرس ایمیل با یک دامنه روی کلودفلر
📧
آیا می‌دانستید می‌توانید با استفاده از قابلیت Email Routing در ، بی‌نهایت ایمیل شخصی‌سازی‌شده برای دامنه خود بسازید و همه آن‌ها را در یک صندوق دریافت مدیریت کنید؟
در این ویدیو، نحوه راه‌اندازی این سیستم کاربردی را یاد می‌گیرید که برای مدیریت بهتر ایمیل‌ها و جلوگیری از اسپم عالی است.
@whitedns</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/whitedns/1100" target="_blank">📅 17:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🛡
ویدیو آموزش استفاده از WhiteDNS Scanner
+
WhiteDNS VPN
https://youtu.be/N5hKuWXp37w
با استفاده از اسکنر WhiteDNS می‌تونید آی‌پی‌های تمیز و مناسب Cloudflare رو پیدا کنید، تست سرعت بگیرید، خروجی دقیق بگیرید و بعد از آی‌پی‌های سالم برای اتصال بهتر داخل اپ WhiteDNS VPN استفاده کنید.
در این آموزش یاد می‌گیرید:
- دانلود و نصب WhiteDNS Scanner
- اسکن IP و CIDR
- پیدا کردن IPهای تمیز Cloudflare
- تست سرعت و کیفیت آی‌پی‌ها
- استفاده از خروجی اسکنر
- دانلود و راه‌اندازی WhiteDNS VPN
- اتصال رایگان با گوشی موبایل
- انتخاب IP مناسب برای اتصال پایدارتر
📹
ویدیو
https://youtu.be/N5hKuWXp37w
📥
دانلود WhiteDNS Scanner
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
📱
دانلود اپ WhiteDNS VPN
https://t.me/whitedns/1072
📢
کانال تلگرام WhiteDNS
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/1099" target="_blank">📅 15:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1098">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔭
برای دوستانی که می‌خوان سرور شخصی خودشون رو راه‌اندازی کنن، کیفیت VPSهای این سایت واقعاً خوبه:
https://yottasrc.com
چند نکته مهم:
* شماره و کشور ایران رو قبول می‌کنه
* پرداخت با ارز دیجیتال داره، روی شبکه‌های مختلف
* آی‌پی‌های سرورها کیفیت خیلی خوبی دارن
* پورت ۱۰ گیگابیت ارائه می‌ده، که برای سرعت و پایداری واقعاً مهمه
* لوکیشن‌های متنوعی هم داره
برای ساخت سرور شخصی، VPN، DNS یا تست‌های فنی، گزینه‌ی خیلی مناسبیه.
منبع
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/1098" target="_blank">📅 11:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/1097" target="_blank">📅 14:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1096">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB_jQ7Sf4ugxIzLiclEMhQzUcgfd_F4InRit6xhlVf87iqG1AaLiDkKm-1upXx1NnOKk77Tg4mJ0eqeSyDA7liRdoqtV66Au7Jy2o3663kWtbZmUUW087AabE9xuLRAah-xodAQ4pzo98yExog-NiXD9ojoXjdutWQuqa32qfSgkdgwLNHmb_8-aBqeqXhvbjODjEmIrXk9exKFlu1mr6KTEtIvJ-9ss2PyJVQFbGPDR7dF0KhRFkS6hYr_tcnZJ8KbWz1k5hTLb5ocGtWDraCbzwqZGdZWTnx7GBYmTS8AhcxLgiAl8hv77z-_U_so0f4D0jCP-d18UuH_72bOqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/whitedns/1096" target="_blank">📅 10:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1095">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/whitedns/1095" target="_blank">📅 05:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1094">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/whitedns/1094" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1093">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/whitedns/1093" target="_blank">📅 05:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1088">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop  منتشر شد
👆
👆
👆
👆</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/1088" target="_blank">📅 11:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/whitedns/1082" target="_blank">📅 11:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1081">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX3hsD1lVGIHNmrxPdI4THszUO0KxhC1Lg3bOdugfflNE61xu0BzyitoCTNTvXo-zKl8t_xidCweClIJElMOhgQ2aeU90_z0CzYaW7JB4nQIWS3qcByAAcykhntBxw9x2ZXgnR5xB5zbmnHnxZBHzsmCbJUhCms84w31DPo7kxJZ5wYfVfvJggElD-f3M2XeObVmZvxMEqoMOV3y_5kooFkPZ3gjPIbdQ6ublSkBcUZBIXz5dMpD1fxaZskOu3LZJGeJxQpNvWGpIPXU5QhdjAj3143gh5X0PSdk7V-oafGeRG-RTVpsLvyI2V7Me9Jf-I6EmVMTyhTFm6jeXFAE3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/whitedns/1081" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1080">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
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
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/whitedns/1080" target="_blank">📅 04:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqkZ59yf2cPP8kv75HWlYHCcPNYnitMe6Ztpr9kCPZzF96ZYuXja6UxtRSn59FQlkBGS991ySWwuda4kvAmahjdtWUjnildILh7pIt5QJkV4iY6mT_zTIWqxRAi-y9wPfNldx9EIEZn6HNopMic6Zn34UKSLGnKMUDhGmUKgfbmIWlNs8Ew32b08-LPnvWMRRi0XLO515qxDOBAu_sWOmO2U8zlDX_EDGrfzKSF8u2VLtSA5ur6g4AkZqUix7jk_5aCBvmtz12HyhlPaNDx4aR0IvL3ZN_xYhV6bewK9XUdnshdskIIIveQVEG0F7tsfdS6qopr3g8t-k_ZWvSSvEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
ورژن جدید WhiteDNS Desktop تقریبا آماده شده
در این ورژن همان وی‌پی‌ان داخل اپ اندروید
برای ویندوز، مک و لینوکس قابل دسترسی خواهد بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/whitedns/1079" target="_blank">📅 16:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/whitedns/1077" target="_blank">📅 03:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgVSyc9BucZOMOYrYn48wbfu9OB-rbbp8DFeGiioN5dqQ795ENPeKK0BEDM4Ns-_QPePubpTCnW5KE198wbSq6rpgwhFljtTBtFDKL2XHMXHXBw2ul81xirqctKNjF9ZxxaEt-Y7vhDy-44mNyba-sDlL2n3GdFlMRIkTvrjafa87Ik7kTsTct_r8TomaoRXrBbzWAEXcniYoPu8nHHuofGGISloBz7Y1HcCReKgRIrC9mCKD-OywmNMmJ1dp4rEtKTOd5YUkqtVlv38KOeR3VWRNbXwYoO1X7AkbmmrPZFxnPi7YpkQrH3DKJpWjbdVJkk5uD-Y9ZYjURlu_X4hcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3.4
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/whitedns/1076" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1074">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1074" target="_blank">📅 17:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1073">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq0mZFOxQFcP9KKU99uo5UE5BJptSMVez4HZD6N91jnvHlLflZF7NgZP3qIOMc2IKZqQN3ReLHuKXtI6DaDoUuds6S2S7ii0ANnzXMoQKYZ4kxdk2H7KLrN_jfVZVSPC2auI55ZmAAVQG29GXF2dPpxkVWC3rpfrJxZD8vJ_3q_azZVs1_UM5TIeOrZx7Uw246Mgn7XEY5OJby4Q4rDiEOeI865fE0tWbjWbcNp1aewhwfqFqxLQcWMfAHYtnAIjoBJ57T5tODysjpBAWOSqZzSFuVEBbU8cECl6k1Rqyuyk_oqnwOn663gogZuPDz7_lUqWg3rVnqtVBnwl1OlnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شد
😎
۷۰۰ اتصال موفق در ۳۰دقیقه گذشته.
ممنون از همه دوستان که کمک ما تست کردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/whitedns/1073" target="_blank">📅 16:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1068" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/whitedns/1068" target="_blank">📅 15:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1062">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
👆</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/whitedns/1062" target="_blank">📅 13:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1057" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/whitedns/1057" target="_blank">📅 12:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1056">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUzK3Wiv8Grs6GCDWavhQOh2JEr21tgYQSv20ZYDHQ4pCDMyGqHM5NkyBmEyK-THJhKSt9CvGs0ArzhMKxLigodpPqPCBngOjW2kwYCnxdITvkfHAW63nvvotOUKMg6u8YUhLWW_diyXpaV_w20_JPdESAciAgDsG7orh7AvSxmPA8fBgWfS6LuFJQXo8vs0OhI1e-P5dZIsrr3mbXXQacj9mhFBFGnU0QS6UnqJYvx9FSpiE29tn4wN30hYJbxwqiy_ov9LsvKluMy6hP2clwwOdKEpgUvITUla-YkJXPsqjIqXkcBm9GaoFohFtUxQ33OvJOki2HhS0edwbzxKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.6 منتشر شد
با مشکلاتی که دیروز برامون پیش اومد، فرصت این رو پیدا کردیم همزمان با درست کردن مشکل کردن اسکنر  ها، روی سرعت اتصال هارو هم بهتر کنیم و تا شاید کاربر های بیشتری بتونن بدوم IP Fronting وصل بشن.
🌈
در این ورژن، سرعت اتصال شما با اختلاف زیادی بهتر شده
🌈
اپ پایدار تر از همیشه هستش.
🌈
اپ از نظر ظاهری بهتر شده.
🌈
مشکل اتصال و نمایش کشور اشتباه حل شده.
نتیجه اتصال و سرعت خودتون رو زیر همین
پست بهمون بگید
ممنون از همراهی شما
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/1056" target="_blank">📅 12:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1055">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🛡
سلام به همه دوستان عزیز
بابت اختلالی که امروز توی سرویس WhiteDNS VPN پیش اومد واقعاً عذرخواهی می‌کنیم.
متأسفانه یه مشکل فنی برای سرورها ایجاد شده بود که باعث شد بعضی از اتصال‌ها درست کار نکنن. خوشبختانه مشکل برطرف شده و سرورها دوباره در دسترس هستن.
برای اینکه لیست جدید سرورها داخل اپ براتون آپدیت بشه، یکی از این کارها رو انجام بدید:
• یک‌بار دیتای اپ WhiteDNS VPN رو پاک کنید.
• یا اپ رو حذف و دوباره نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا اپ خودش تنظیمات جدید رو از سرور بگیره.
شاید سرعت کانکت شدن کمی پایینتر آمده باشد اما به زودی اون مورد هم حل میکنیم.
ممنون از صبوری و همراهی‌تون
❤️
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/1055" target="_blank">📅 08:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1054">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/whitedns/1054" target="_blank">📅 13:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یکی از اولین آدم‌هایی که از این پروژه حمایت کرد،
ویکی‌تجربه
بود. زمانی که اینجا فقط حدود ۱۰۰۰ نفر بودیم.
شاید خودشون هیچ‌وقت ندونن، ولی با به اشتراک گذاشتن پروژه، یکی از کسایی بودن که به ما انگیزه دادن ادامه بدم. بعضی وقتا یه حمایت کوچیک، بیشتر از چیزی که فکر می‌کنیم روی مسیر یه نفر تاثیر می‌ذاره.
خیلی وقته دیگه خبری ازشون نیست. حتی دیدم دامنه سایتشون هم تمدید نشده.
کار درست انجام دادن توی ایران سخته. درست موندن و باوجدان زندگی کردن هم سخت‌تر.
من حتی این عزیز رو از نزدیک نمی‌شناسم و اسم واقعیشون رو هم نمی‌دونم، ولی همیشه قدردان لطفشون بودم.
امیدوارم هرجا هستن، سالم باشن و حال دلشون خوب باشه.
🥲</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/whitedns/1052" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wn6uJJULwxg0OqmCFjCiAJLC53pH3vm95loizz0srFNhDarwx3sZS_NE9VHbxLUKFdEAa2QjOL9_RviCg11ooJgZWSJZkV5fxUNCWrY7N1ijd_86tVRQenFaH1izQ2SPVG2Shy3zJm33HvmVQKDEz2N3d0Yrr5eTDBtfBLhD3HcMiMPT-fpbeiCXfnhl7freq4E63kfp4iuf-UuymLGorSgrUpMoYMQeHQ2qFaekJIbjsFOtk7PgTqXqANUdU6cxIgrdvUn_GE1sBNbRw03ErwF5Qpq9neSlNB4jhzsMAAjQfbBLUWs-oYuLrTlXiMnzcE-MOm8Kvn2lH1LHds23KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویکی تجربه یکی از معدود گروه‌هایی بود که بدون هیچ وابستگی و فاند و رانتی، محیطی رو فراهم کرده بود که افراد نظر واقعیشون رو راجب شرکت‌های ایرانی بگن و نظر بدن.
سر همین خیلی از شرکت‌ها می‌گفتن که کامنت‌هایی که راجب ما گذاشتن رو پاک کن وگرنه شکایت می‌کنیم و فلانت می‌کنیم و... یا حتی می‌گفتن بهت پول میدیم، اما قبول نمی‌کرد.
و همینطور یکی از عواملی بودش که باعث شد آموزش‌های من به دست خیلیها برسن، چون همیشه مطالب رو share میکرد و با وجود هزینه‌های سرسام آور سرورهاش و شرایط سخت مالی، توی قطعی نت کنارمون بود.
و آخرین پست کانال تلگرامشون توی
تاریخ ۲۷ مارچ
(۹۰ روز پیش و اواسط جنگ) بود و همه نگران بودیم که نکنه اتفاقی واسه‌ی مالکش افتاده باشه یا دستگیر شده باشه.
و نتونسته دامنه
https://tajrobe.wiki
رو تمدید کنه. امروز دیدم که دامنه‌ی ویکی تجربه توسط ابرناک گرفته شده(احتمالا یکی از شرکت‌هایی که تهدیدش می‌کرد). و در عجبم از اینهمه بی‌شرفی، که میراث شخصی رو که مشخص نیست مرده یا زنده‌ست یا دستگیر شده یا... رو برداشته و اسم تمام اون پلتفرم رو گذاشته انتقام‌گیری.
امیدوارم که حال ویکی تجربه خوب باشه. دامنه و اینها کمترین اهمیت رو داره</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1051" target="_blank">📅 16:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">↗️
تعداد کانکشن ها موفق WhiteDNS VPN به ۱۰،۰۰۰ کانکشن روزانه رسیده .
✍️
در حال حاظر تمرکز اصلی ما روی اضافه کردن وی‌پی‌ان به نسخه ورژن ویندوز، مک و لینوکس هستش.
✍️
مواردی گزارش DNS Leak توی کانکشن‌ها داشتیم. درحال آماده کردن سیستمی هستیم که علاوه بر تست‌های سرعت، امنیت و پایداری، تست DNS Leak  هم از کانفیگ ها گرفته بشه.
ممنون از همگی
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/whitedns/1050" target="_blank">📅 10:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-poll">
<h4>📊 به ورژن جدید  WhiteDNS VPN تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
<li>✓ ویندوز یا IOS استفاده میکنم</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/whitedns/1049" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-armeabi-v7a-release.apk</div>
  <div class="tg-doc-extra">33.1 MB</div>
</div>
<a href="https://t.me/whitedns/1043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بیلد کامل اندروید SenPai Scanner، با تشکر از
Hidden-Node
عزیز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/whitedns/1043" target="_blank">📅 02:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/whitedns/1042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">به زودی نسخه یونیورسال هم ارسال میکنیم.</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/whitedns/1042" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🛡
چطور آی‌پی اسکن بکنیم؟
یک آموزش براتون ساختیم تا بتونید با اپ SenPaiScanner روی گوشی اندرویدی خودتون آی‌پی های کلادفلر یا رنج های خودتون رو اسکن بکنید.</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/whitedns/1041" target="_blank">📅 18:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
👆</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/whitedns/1039" target="_blank">📅 09:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1034">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.5-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/whitedns/1034" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/whitedns/1034" target="_blank">📅 08:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1033">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N84zND0j7evF6dgPJFgLUHZsjPAXXKDr6CG3aOF1nGhuYBwSm_YppsixDQxTccFhgFDFenPaDRA8jr7LwdJid68o2xurrFsGRQat9l9oCVGDttSPXtVaMnwIxktyd9fKfF6h_9wE3H2H3np8eho-k84dApp8h7Tu4uIKa8iAgjfbEGEAYfxtx45w7oEbYUnw4SGOfA6Hooj24xklazKF6XpeLF8PsBbJGQs8XKDbKb9HNeJFU_i43f5FdKn0sw4COpef_03cNUk7H--CP1X1kjTqCKd483HGODACn5KcN3FBWgRioC8Z3KvrJ6IixpkPWB_3NhdDwyrYDeb8zjmhsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS VPN 0.0.5 منتشر شد
توی این نسخه چند تغییر مهم داشتیم تا اتصال راحت‌تر، سریع‌تر و قابل‌کنترل‌تر بشه:
• موتور اصلی اپ از XRay به Mihomo تغییر کرده
• تم دارک به اپ اضافه شده
• امکان اضافه کردن تا۵ آی‌پی تمی در بخش IP Fronting
• رفع مشکل «کانکت میشه ولی چیزی لود نمیکنه»
• اتصال سریع‌تر بعد از قطع شدن، با استفاده از کش
• اضافه شدن دکمه Refresh برای گرفتن کانکشن جدید و شاید بهتر
• نمایش سرعت دانلود و آپلود
• نمایش آی‌پی‌ای که در حال حاضر به آن متصل هستید
اگر برای اتصال مشکل دارید، احتمالاً باید برای خودتون آی‌پی تمیز اسکن کنید و داخل بخش IP Fronting قرار بدید.
تیم ما همچنان در حال تست و بهتر کردن اپه تا اتصال پایدارتر و ساده‌تری داشته باشید.
ممنون که همراه WhiteDNS هستید
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/whitedns/1033" target="_blank">📅 08:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1032">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان
👋
بچه‌های تیم به صورت مداوم در حال اسکن و بررسی IPها هستن تا همیشه بهترین و تمیزترین IPها داخل اپ در دسترس باشه و شما کمتر درگیر اسکن کردن و پیدا کردن کانفیگ مناسب بشید.
هدف ما اینه که تا جای ممکن فقط اپ رو باز کنید، یک دکمه بزنید و متصل بشید.
اگر فکر می‌کنید قابلیت یا امکانی هست که می‌تونه تجربه استفاده از اپ رو بهتر کنه، حتماً زیر همین پست برامون بنویسید. اگر با مسیر و هدف کلی اپ هم‌خوانی داشته باشه، با کمال میل بررسی و به لیست توسعه اضافه می‌کنیم.
ممنون از همراهی همیشگی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/whitedns/1032" target="_blank">📅 13:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1031">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1031" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1030">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سلام به همه همراهان عزیز،
متاسفانه یکی از اولین اعضای خوب خانواده WhiteDNS که از روزهای اول قطعی اینترنت خالصانه در کنار ما بود، به علت بیماری سرطان از میان ما رفت.
از طرف تیم WhiteDNS، این اتفاق دردناک رو به خانواده، دوستان و همه کسانی که دوستش داشتند تسلیت می‌گیم و آرزوی صبر و شکیبایی داریم.
یاد و خاطره‌اش همیشه در قلب ما می‌مونه.
🖤</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/whitedns/1030" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1029">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود رفقا...
پروژه نهان که قبلا متین معرفی کرد رو محصول داداشم دکی واسه دسترسی رایگان به اینترنت آزاد با روش ورکر رو بلدید دیگه؟
حالا میشه آسون تر حتی واسه کسایی که مبتدی و هیچ ایده ای ندارن هم ساخت با کمک ربات:
@itsyebekhebot
شما وارد ربات میشید ساخت پنل نهان رو میزنید وارد سایت کلودفلر میشید و طبق راهنمای کامل پیش میرید و ظرف دودقیقه حتی کمتر با کمترین اطلاع و دانش از ورکر یا هر چیز سخت دیگه ای فیلترشکن رایگان خودتون رو بسازید به صورت رایگان
❗️
نکته:از بات ایمیل فیک هم داخل کلودفلر میتونید استفاده کنید:
@TempMail_org_bot
هر جا هم گیر کردید بهتره که به من پیم بدید
😆
آموزش ساخت پنل نهان
@yebekhe
👑
@xsparvin
🍷
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/1029" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1027">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه • ظاهر اپلیکیشن تغییر کرده  • امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.  • پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.  • با کمک یکی از بچه های…</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/whitedns/1027" target="_blank">📅 15:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1022">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">23.5 MB</div>
</div>
<a href="https://t.me/whitedns/1022" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/whitedns/1022" target="_blank">📅 15:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1021">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECra9b1YKgnGDt8zoMo1JYNyAY11HvrhBX7VkdE6XWSQgh2MpfwNzwmxH1gwxA8vkBlYFKzQw6IPjbZN1ypTSADWb0coI0SSV1xHuSZVcMq0oE0Y33-2WOJo2evrruBfi6TRPmNljYBEru4AtkWXTUaweUkgMv-0Itrq4maVd-s98i0gdjsbOhKR8t5mqRx47gC1FZxiYNwg2t1Ucr9LoEc3GQhnURa9R9lrKeZBbW-4D9eEtGVHYcjGFaqWm9_S8dTJ2CCmSg1pC_mBWocm4FM778EllZxxAfVWxn4HUj_GEp7Z96h5jDULmWyGPLBW-fgkn6EDbMPTJBjbGljERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید WhiteDNS VPN V0.0.4
⛏
در این نسخه
• ظاهر اپلیکیشن تغییر کرده
• امکان اضافه کردن آی پی تمیز خودتون اضافه شده تا اگر اسکن میکنید با آی پی های خودتون به کانفیگ ها وصل بشید.
• پرچم کشوری که بهش وصل شدیدرو بهتون نشون میده.
• با کمک یکی از بچه های گروه، یکسری از مشکلات امنیتی اپلیکین رفع شده.
💬
اگر براتون وصل نمیشه، فقط و فقط مشکل از شبکه شما هستش. آی پی تمیز پیدا کنید و داخل فیلد IP Fronting قرار بدید و براتون کار میوفته.
@WhiteDNS</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/whitedns/1021" target="_blank">📅 15:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1020">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-0.7.2-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">34.7 MB</div>
</div>
<a href="https://t.me/whitedns/1020" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/whitedns/1020" target="_blank">📅 14:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1019">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bw-ChWPVtDXYmUsFhj27TUI-gGQvaaXDLURlw4ZIzk3Hb59oqnLfiBke12xt02ttEifx2bBDKnvsLShOzCH0TzGP1Nj2ih6fieIM5H4g22w2ZDWaPxbo0U0KguDfZ5D9Qr1KxHAiuKxgS4GjAVJZINZabR37_sfCQYmZFJRI68xVDidyi-ZlH6l-OffgpH9EYBdBXlNA5VpvzgA2kHJwJVU_F8B9x87D0YAQU6A0gIapyTkROEg9UqkbVJtebuVh6ENY3ffOtLP-ehbv_LhxyZA-tSWnEivL4YUzBtAiNkP4v9TmGtpH5urEDo3S-RoCLHtURDYnZeQ2lFQqO2Z1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از contributerهای پروژه‌ی senpaiscanner، دوست عزیزمون hidden-node، نسخه‌ی اندروید اسکنر رو توسعه دادن. طرز کارکردش دقیقا شبیه به اسکنر دسکتاپه. نصب کنید و یه تست بکنید
👇</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/whitedns/1019" target="_blank">📅 14:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1018">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-1.2.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/1018" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌎
آپدیت جدید WhiteDNS BPB V1.2.0
در این نسخه مشکل ورود با Cloudflare برای بعضی کاربران رفع شد.
قبلا بعد از انتخاب WhiteDNS BPB در مرحله برگشت از مرورگر، گاهی برنامه پیام خطا می‌داد که کد ورود آماده نیست.
از این نسخه، برنامه لینک برگشت Cloudflare را نگه می‌دارد و بعد از تمام شدن بررسی قبلی، ورود را درست کامل می‌کند.
✍️
نتیجه:
ورود با Cloudflare پایدارتر شده و احتمال خطای برگشت از مرورگر خیلی کمتر است.
روش استفاده تغییری نکرده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/whitedns/1018" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1017">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخدماتی حامد📱</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آموزش (1).mp4</div>
  <div class="tg-doc-extra">15.1 MB</div>
</div>
<a href="https://t.me/whitedns/1017" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آموزش ساخت پنل BPB بوسیله برنامه
WhiteDNS BPB
😎
😎
😎
ارسالی ادمین am
❤️
برنامه نصبی مورد نیاز
👉
سلام برای ساخت پنل به این نکات دقت نمایید قبل از ساخت پنل شما به یک اکانت کلادفلر که تایید شده باشه نیاز دارید.
بعد از انجام آن وارد برنامه white dns bpb بشید به بخش dasburd  برید .
گزینه connect cladflarرا بزنید تا گزینه sing in cladflarنمایش داده بشود روی اون ضربه بزنید تا صفحه مرورگر داخلی گوشی باز بشود در نهایت با زدن گزینه ابی رنگ  در تصویر اکانت ایجاد می گردد .
بعد از اون دو گزینه نمایش داده میشه که شما باید برنامه white dns bpb رو انتخاب کنید سپس به تب bpb deployment برید و گزینه  create  رو بزنید تا پنل ایجاد بشه یک نکته دیگر که مهم هست .
اگر در حالت عادی به ارور برخورد کردید با یک vpn روشن وارد پنل بشید یا نت خودتان رو تغییر بدهید تا به پنل وارد شوید باقی مواردش مانند پنل bpb می باشد .
در صورتی که خواستید می توانید ایپی تمیز برای پنل خودتان قرار بدهید و از آن در کلاینت های خودتان استفاده نمایید.
@whitedns
❤️
اشتراک گذاری یادتون نره
🌈
‌‌
@hamedvpns
☑️
لایک   |   Like
👍
❤️
اشتراک بزارین   |   Share
⭐</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/whitedns/1017" target="_blank">📅 03:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1016">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان عزیز
❤️
در چند روز گذشته متوجه شدیم که بعضی افراد و کانال‌ها، به جای همکاری و ساختن، مسیر تخریب و سوءاستفاده را انتخاب کرده‌اند.
این افراد که ظاهراً در فضای اینترنت آزاد و کانال‌های مشابه فعالیت می‌کنند، برای جذب مخاطب بیشتر حاضرند هر کاری انجام دهند؛ حتی اگر نتیجه‌ی کارشان آسیب‌زدن به پروژه‌هایی باشد که با زحمت و هدف کمک به کاربران ساخته شده‌اند.
چند روز پیش اپلیکیشن WhiteDNS VPN را معرفی کردیم؛ اپلیکیشنی که هدفش این است کاربران بدون نیاز به تنظیمات پیچیده، فقط با زدن یک دکمه به بهترین کانفیگ‌های آماده و تست‌شده‌ی ما وصل شوند.
اما متأسفانه برخی کانال‌ها شروع کرده‌اند به استخراج کانفیگ‌های داخل اپلیکیشن و انتشار آن‌ها خارج از برنامه.
دوست عزیز، اگر مسئله فقط بستن مسیر دسترسی شما بود، ما ده‌ها راه برای رمزنگاری، تغییر مدل درخواست‌ها و محدود کردن این رفتارها بلد بودیم. اما شرایط اینترنت آزاد و محدودیت‌هایی که کاربران با آن درگیرند باعث شده ما تا حد ممکن ساده، باز و قابل استفاده طراحی کنیم.
مشکل اینجاست که همین رفتارهای مخرب در گذشته به پروژه‌های خوب و ارزشمندی مثل Slipnet ضربه زد. وقتی هر ابزار مفیدی به جای حمایت، هدف استخراج، کپی و سوءاستفاده قرار بگیرد، در نهایت انگیزه و امکان ادامه دادن از بین می‌رود.
واقعاً هدف چیست؟ آن کانفیگی که با زحمت استخراج می‌کنید، همان چیزی است که بخش زیادی از آن در لینک‌های ساب ما هم وجود دارد. چیزی که روزانه هزاران نفر را متصل نگه می‌دارد فقط یک لیست کانفیگ نیست؛ پشت آن اسکنرها، تست سرعت، بررسی مداوم، فیلتر کردن کانفیگ‌های خراب و یک سیستم کامل قرار دارد.
ما این ابزارها را در مدت کوتاهی، با انرژی و فشار زیاد ساختیم تا به کاربران کمک کنیم. لطفاً به جای تخریب، کپی‌برداری و گرفتن انگیزه‌ی تیم، سازنده باشید.
ما از نقد، همکاری و حتی پیشنهادهای جدی استقبال می‌کنیم؛ اما سوءاستفاده از ابزارهایی که برای کمک عمومی ساخته شده‌اند، نه کمکی به اینترنت آزاد می‌کند و نه به کاربران.
اجازه بدهید این مسیر ادامه پیدا کند.
✍️
@WhiteDNS</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/whitedns/1016" target="_blank">📅 05:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1015">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✍️
دوستان برای جلوگیری از هرگونه سردرگمی، ما در حال حاضر سه اپلیکیشن مختلف داریم:
🛡
۱. WhiteDNS Application
این اپلیکیشن بر پایه‌ی MasterDNS ساخته شده و مخصوص زمان‌هایی است که فیلترینگ و اختلالات اینترنت خیلی شدید می‌شود.
در شرایط عادی فعلاً کاربرد خاصی برای استفاده روزمره ندارد.
🛡
۲. WhiteDNS VPN
این یک اپلیکیشن ساده‌ی VPN برای کاربران اندروید است.
اگر فقط می‌خواهید راحت وصل شوید، این گزینه برای شماست.
🛡
۳. WhiteDNS BPB
این اپلیکیشن برای ساخت و راه‌اندازی BPB روی گوشی اندروید است.
یعنی بیشتر برای کسانی است که می‌خواهند خودشان یک پنل BPB بسازند و مدیریت کنند.
🛡
۴. WhiteDNS Installer Bot
آیدی بات:
@WhiteDNS_installer_bot
در این بات می‌توانید کارهای زیر را انجام دهید:
• نصب MasterDNS Server
• دریافت لیست IPهای سفید Cloudflare
• دریافت کانفیگ رایگان VLESS
• تبدیل کانفیگ‌های خودتان به کانفیگ‌هایی که پشت IPهای سفید Cloudflare قرار می‌گیرند
🛡
۵. WhiteDNS Installer Wizard
لینک گیت‌هاب:
https://github.com/iampedii/WhiteDNS-Wizard
این ابزار برای کانفیگ خودکار سرور شخصی شما استفاده می‌شود.
با استفاده از آن می‌توانید سرور خودتان را همراه با پنل شخصی 3X-UI راه‌اندازی و تنظیم کنید.
❤️
یک نکته مهم:
اینکه اسم برند ما WhiteDNS است، به این معنی نیست که همه‌ی سرویس‌ها و اپلیکیشن‌هایی که می‌سازیم حتماً بر پایه DNS هستند.
ما از اسم WhiteDNS به عنوان نام برند استفاده می‌کنیم، اما راهکارهایی که ارائه می‌دهیم می‌توانند VPN، BPB، MasterDNS یا تکنولوژی‌های دیگر باشند.
@WhiteDNS
🌎</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/whitedns/1015" target="_blank">📅 04:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برای این ساب، ما هر ۳۰ دقیقه بیشتر از ۲۵۰هزار کانفیگ رو بهشون وصل میشیم، تست دسترسی، امنیت و سرعت میگیریم و بهترین هاشون رو تو ساب قرار میدیم. که خروجی بین ۲۰۰ تا ۵۰۰ کانفیگ میشه.
تمام این کانفیگ ها قابلیت این رو دارند که از Cloudflare IP هم براشون استفاده کنید.
بروزرسانی فقط برای این ساب جدید نیست. تمام آدرس های قبلی هم بروز میشن و همین محتوی رو دارند.
اگر ساب براتون اررور میده، احتمالا آدرسش رو فیلتر کردند. اولین بار با وی‌پی‌ان ساب رو وارد کنید.
ممنون</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/whitedns/1005" target="_blank">📅 10:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1004">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان عزیز WhiteDNS
🤍
ساب جدید WhiteDNS برای اپلیکیشن‌های مختلف آماده است.
برای اپ‌های زیر از این لینک استفاده کنید:
💠
ClashMi, Clash Party, FlClash, Karing
https://sub.whitedns.shop/sub/mihomo.yaml
💠
V2Box, V2Ray, WhiteDNS Desktop App ....
https://sub.whitedns.shop/sub/base64.txt
آموزش استفاده از Clash Party را هم می‌توانید از این ویدیو ببینید:
https://www.youtube.com/watch?v=gMFH88yRghg
این ساب شامل حدود ۵۰۰ کانفیگ پرسرعت Cloudflare Proxy شده است که به‌صورت مداوم بررسی و به‌روزرسانی می‌شوند.
پیشنهاد ما این است که اگر از اپ‌های Clash-based مثل Clash Party، FlClash، ClashMi یا Karing استفاده می‌کنید، حتماً لینک Mihomo را اضافه کنید تا بهترین نتیجه را بگیرید.
@WhiteDNS
برای اینترنت آزادتر، پایدارتر و قابل‌استفاده‌تر
🤍</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/whitedns/1004" target="_blank">📅 05:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1003">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SFj5O_6h3PnD10KVcDrtcXfbHGrmOnywzMsiguXpizJilxtnJ22rZTrgoz7hKdzhK4DpC6rM8Oyz6EHDe9-BYMof2bp1KufbFE9tx8uykbT-XGvcvaFyDB4Ikrk4Pi1ANiHoypjWaTLi7p_nMH6NZSfL9bPMiHMhjHXjgiCH1Qxd7lkAZvJuK4cB-O_-rt-oNQjXwdv5W0UlDHeKjFCWACYkBfxnGrx0yRCEqr2GpncsFFwfOukYpskFmmR5qzLtLG39xFrVW-9hNoskVkB9Lxx9WuT6kikjUeUPbvp50rLbrIF71eiqcLyZcdQUkb8n0FfHq6vwRNky5nd-CZkbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما با این مدل افراد به نظرتون باید چیکار کنیم ؟</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/whitedns/1003" target="_blank">📅 19:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1002">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آموزش کوتاه استفاده از :   WhiteDns BPB  1.1.0
📱
📡
@whitedns
🔗
✨</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/whitedns/1002" target="_blank">📅 15:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1001" target="_blank">📅 14:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1000">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1000" target="_blank">📅 14:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-999">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/2df17bf874.mp4?token=GYxWpuN9z6jFgqPtTHurJyMu928kBJgrdwyHXvehEQ7UlBqyt697WnwOQkmKoMJxsO4AkZkFtPf_48wiCHhHdX85XHEsNXJ96dwbRJB8yTNHQqkQUAbYLe3aYiHFy6bWw85NuR4KoK-ynh1QRJRx-DNyqtLP14xIDu3HZcS3RNiJ1lKmbXHDewklHzxeIgEhaB7YLRwKVB4DUmlreFctharR4DDCISFYiNm_-yUW1993skL84eUdvgezKxnsC5pAGy68__QHz2L5WDEvAYEwGk_ZmduFtxbixSWKL75QhQZfuRwUXuHTro-2D722HXw7zKrfsrIe8TQ3yQwG035ZT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/2df17bf874.mp4?token=GYxWpuN9z6jFgqPtTHurJyMu928kBJgrdwyHXvehEQ7UlBqyt697WnwOQkmKoMJxsO4AkZkFtPf_48wiCHhHdX85XHEsNXJ96dwbRJB8yTNHQqkQUAbYLe3aYiHFy6bWw85NuR4KoK-ynh1QRJRx-DNyqtLP14xIDu3HZcS3RNiJ1lKmbXHDewklHzxeIgEhaB7YLRwKVB4DUmlreFctharR4DDCISFYiNm_-yUW1993skL84eUdvgezKxnsC5pAGy68__QHz2L5WDEvAYEwGk_ZmduFtxbixSWKL75QhQZfuRwUXuHTro-2D722HXw7zKrfsrIe8TQ3yQwG035ZT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کوتاه استفاده از :
WhiteDns BPB  1.1.0
📱
📡
@whitedns
🔗
✨</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/whitedns/999" target="_blank">📅 14:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">WhiteDNS-BPB-v1.1.0.apk</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/whitedns/997" target="_blank">📅 13:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-BPB-v1.1.0.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/whitedns/996" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه ۱.۱.۰ اپلیکیشن WhiteDNS BPB
در این نسخه مشکل وارد شدن به
پنل  Cloudflare برای دوستانی که ارور داشتند حل شده.
پست اول هم آپدریت شد به این ورژن. پس اگر اول لود رو دانلود کردید دیگه نگران این ورژن نباشید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/whitedns/996" target="_blank">📅 13:19 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
