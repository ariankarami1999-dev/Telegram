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
<img src="https://cdn1.telesco.pe/file/dsbZ20LS5o8O_I1egKXHqwXr3LSmueDJH72raozXmyjCrUwtkzHFp1N1qroxj1lWzlyUcIA_KhUxSiu1MrI2rK9tGJAx78vjtC8dIjjCh7TLa7QOiVtG0dbot3sNrk6sOEBDEX6z_XlP1GxRLkCriAI97IKIPaej3VafWGelV7QuWhSCvD_PsG7oZizCmGeFhAyBMvbMGtXQhXWPmZ93X-b4YrBB2JqWkGeZyNvl3hvSuizHAMhuuLOJpJ_zUFidPAxXTfIvvl56yFJSP783jHNjIU2XuNBFWlXzpvftSAQfjQE10r0_woqg4MFwlNtflYZ8zxvQhH9RpQu3Z0aO8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 98K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 23:31:29</div>
<hr>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOzrL1UHZrauA1LId9gq8qEBIohR_GV7LG3hvmSIodFMeSU8nXxc7_052Z-SJlN7_qk-d0v0cOHBtbxFgYc6v1pboDulKaru77ihv40CSFdETaY5AgYa96YTpum8371IjACtIW15yKveKW0RK8T-salTva7pYCSUWqBq5uZJOUq3gWllG8HqNGyjgsrAuKtR0AAfqeiVxzU5HVF7PvW1NGm_RRXkIxTmusmr4nwgOwzNrxjJZugVkKyVF6EXjTXhOa0tOFdY-Hm3MG6h8W8pd9fF3I1ZSc01CQLJm9-2lIvDc-FRtQpRIsECY13qtYPYJYxaKs7UD0jN2itA0qFBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0-sozI0UFiEmmZD9E6bqyWSeVuupfa04PiAB8Y6RzwwO0PdgoG-8ZNHAVVgCioh_4AeY7Xslgg5QLj-ACbqeah7PKQmvmu34eAQ8wwqOc_O5kSsIrKhJC4cAGNMClNDF2CFSj0nCrdExkOCNJ7U0LAOS8vYz7R-Y9urddasvxbeMWhXUWxxmH5hKlGKtct3ALLyPd4gFHRjXelNus0pLVgck9WE9SiajwXcwnHKcUIb6POEsiEfm8BMl_6xNy1jfztSdzLXb7mw9JiyP62mzL14bp3-khrPqWD9zjEg7GOT0HJySGJvUvxW-dH_jw5p4bddrFSeDpkL_Qjjh7Zg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zeykm4bAkjLIb9XD5soGFPQd-41cYWbGDT-pUAcx_HppZGpbyfLow38Hj23YgiJzCeuqc6Vkj4PHT77a3lf9GqkLDjTbCkaaSzFU1_32Xss9bwPg_nFzbC_xLyJDE6yH55J34R6_kI33rE7dUKiImd1t1H7f2rNSBRonCPhJ-XW15KLFJB3FOJQf1m2EmKHFPDvs3Hu42kf99afY3d65DumrukXd7DB-P9AVP8QQhNmzK1ylPmy3EQIlyLfmkBH0NwUnkExzWPyt4_PjRammCTocgoMbihlpUNFZrqSGf3lFkgQVyhb9Bdknc3CLIdRVPXqJFfOhAdSHEOCDrv8KpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2sz1aUuuatP9_VOmrtRfoXdFE32lFvvvmm4k5HpAAjZe4g2fIveB14_v_LOm2b2mAILf9PUmrSFiIKCSvkt10QZRefo7hsil7KuT9wvyoWsCszXNnSaBQwBZ3AFzQ6ps6LHSx92HuCRnGdo7RVHEOhzjqtw6g5WlehJFm8Njww6UyyxePhqUO5Wp_q9juwaNew9U6twPpAAlMBEWWy6hWnypNHa_PPRC4ygYNkumQ1_wYRAXhaj55kZFjaZOGom2v5ariRA_RIt_90WnKguos6BaO-gWTwYMZRKwPqGyAICWNPx0c13Go0ALJLZd90jNfjO4d7eGr3K443kKtP10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dly7fCRUVYHG43hzCYtCtumOUfDDBoENKeoxPzQx1SGbC37Mykpk8jN39pNynOSl1Nq5Erv3ee6fFI914ausYys5NwAh-ho_epn7KJbr6jNpjmXiYgiwLTyeq9k3Xdp-_uQ3f6gHIg8WfvMSvME0epIMz-EEChQHGQBm5gt346FwlBz42CP6G5dyKFH9o30Aj_unNynBZYK_1xPGLq4RN4ML6StWY3gJd2j66eSDcwxuWVVFrecEw5vDYpQKJ8yjbQiE2pReIXfsS_v70BSbqhEOrTAXjms5uraU6FwUcGcpDUfOoYLVuBjy6_AbvxoArARRavB6xzme0o76G5HUVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrvRqgsbdgPPAWxgQ2nXzKunXlxHzRN1PBjKSV0_0iBpyXobd7ydu7CgnshScpG6TnoR2JAyF7jwb3zZ50Bp8kkuyDx_c7KLdwNmqq1fvULXn4PvtWoHQWaZ-PwYQWoRD1poJ5shtUg2KrmWKOy1ZLlADzvFl_nC9ZTbi5P_sSlNlJB1ZTJV2wzY41sUIJBa7MyQ6CFlqiBa2yzQj_AgKFQH2KK4c31ng-cPJ3wLxaa14RatkUM27VrJVd0Ro7_cbnf3kf-3ugxDLzOFXj8IPaww0SBeixHawG_q6WBbS4zXz2Y9X5oT7-r4EeInNYlFzS2DSXMiiGrqYeeWugC_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_HR_NXzKzDTuOM3T8wkBj1OMBwoXIF5-anw3xZtQMTihH7D-lKVnnbyzB__A2lsXEXDynkPy8UZEyg4L5dY9rqrrpWxQBXg54xdv3gDpdeWO6uc77G52zjQaJfaleWRJS3-Dyj91NJLdupa9fSecvYEvb7KEqIRe2WVsG44JvPbeLZWqpGWXL-u9OCbLMKeZljlPB9GlnzeyyTVQLNjuIJLgfIzwB2UUisd5mJg7o19q-qhoIqBL8IUE6jQ860Pqkq3QiEmshnbkvcK3TTqc03DbJfdEfwyxwe9bTGUES3gKp2R-8aMuFx4NnNcDgJroG-8G9qf9rxvtry4bSvTjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FzjwijzUiEcw2VvADCjBL8Vdo0idaUMQCI-WO9KacQiEq5Y1iFH2qf1K-YuQ3fITOBgKJampHGfbZexR6jRbEJBX6TRKfF5978ZZtuXfjlujSDz0WoPMeVjMVj9tzK5ozvbbZTY5AHRsj1D1fnZRGe0-nyrdYU-xFmr0bOpRzg8v5hiV979fYJxZypGEZod20izVrXto2-NM8NfM7XAcnjg6nUZGvPgjA8wPN5rOsWQHgT6wYIMotTlvzBO8ZReCVGiTJqoKEUqB7iU_ITxxa2fnmcI7dJePlrU89CqwqXvtNVLUTS8kYW-Bxm5VL7sidiMpjjUJP8ihQpd-OmjgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvzF-CIczi3dJKAdcpghSFVj1V8PDrWzNI-A60ROYfCRVBMB1rIqd3P13NdKJR4dviqFpRFcH_jngx9Y9wB8sMP0toqp97X9AozVcrtHu_PDCs5nB-yvFZzk8PgzMaMftMf07s4KrF3aaYU6vOhgCTKSk-zCmbL7T3zyi9_dhc6itk7W067eS29ZUwi7qyYR8Qz8NcAYgCfbwasxcRPDe1DwJADHhH4ztyW5p_vvcTH6gUw16VYhHXQkJZeL8zUw3z9WF_RKl3s9pPMUhxVLBTNamaGr2poGh16aVjoU-MAXc-4caTdlh1q_zOLKK5IKEAB0EvGppYUQOHyD1XinCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DyFjIcn76YlNteZYVgdwZX-RzDJt9ZU0_t4bXoLdcbFc2aDu6VmxUJGyvmexE1qQyjSM8mSM4p6hOGwaseRwZ9hhdkbg39KJyI4XKgOPacIg7c5fjrp4yejB2u_IMQsiT4a8qAB3wxew6jurUulR_KIfj8HA1moc7bR4XbAvkXFhVGkQfQ4VzSsPBrXyF0_sDbwpZvoKZHi4lawLDk5CVyn-xKBxC6OwDODNQ2OxlPGhZSPvKOswd--Tl-5MelHHfJxvbiQW--PjfxLw_hVmmzld1bYboRsaQmH4fp5yZ44C_ueDaRt2vFLJX6ZyhO2YMPFIOyjX-te_L2rsq0RPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RNF6Le8o0IG1rr-mbbFpi8gfYMul6jPcgBNLRT_xpF7vR60garCNubE31doyAQnjMtLsTniKN6hHbFx_Xekw4rdkln6ogWr2tHdyjEgkoCg2cDyrd923T7-aGiSCYLOYO50IFO5Svj2tKpoWS7gINikzvA_9E2Dt3e6bPEsJonXD30scXNnHYy2qYBKHb04ZVRnFs1j7_AfjLrHsFmxDFvSd1FEbUBboZroShe857HDwPnQ14yDbhBCUNn_kvlFvuvljQ5pm0i5qKqKBW5EHqy6LiEzkj90m1Vk4O_170g0p8dBRkamHd4_Vs5NEhZ-IgXyBxkTB5jqOvmXhMazV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVCJGkTmPMMGr9sv3IPuOuMvZekKtuui5k8nGhGEd7di2wEDmcUjickrN_C7v4sbAa0t-U8ntuyUExAOcUuFuwjd1JY7joy4MOhpB3W0DW5CeO5oHg0iMIfgnnGibZUPkez27qt5N9mx5abdn9gYqh_mNon0je8QbOkEB8ff7EgtMCCQAMHedY7GQVYyIsBGRBTJrK5Sj6cSafrGuk2GSj4Mi3OIWAId8ibmCnUaV53n26ryFG0824bev7B8Hk1yUv5l2t7GxY-KGgJ0bQJ-5m1CH04LHiULgWHOEE8yW-dzmo_8ZIy0gjQpAACX_0okC7_XhtQ_fQF6O593Ql5AIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xtu4NRys1aOPXDuLoojT75WuEcV5tpj25r6erNN3_BR86XS3gXLLCsa44VSt0xc7h_gvb8FUw7LetCnCGxWuJB6naKj34Cqtxurw6BRBrTUpW3orohV9KcIUawrZrkIJ3qcSRSSLw0rFVqNuZWtbseBSi_CKjBLa0BwhjRLeoilWTUjomXRndeyzjyo8QvV8yhx8wZWim3wgwBsPiAgAfPr_Eky762_4yVzse6DXgBPhCymyWZw_1m016BO3oeWp8RBNU_6BFmk3W9-lCSObTbiDDihlW0yuBAqHqooqyV_AsJPV2xp1yXj-_L-MOgPO1tp581DGktniDoT-8hLzgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Eb28Zw5dO_1QXXFdZi37lHl6Pr5MKZm2RHjwZYX2_IrkCrP8SxLb0pU4HDPVzuG346A0QJuSggNdJd1-QYCsGVbVdNJZn_mYcK_VEHaNbYrVb6CAA4XXbGOZTurwUD-f-4ujN4_SDOZhK0RQiCvh3qCqDvGD5V5GZAzccN5nk-t6D1O4UbxmclGdyYRnU86Y1djY4j9MD28ZM11AJCy-iWzJglIrzmhYLKyqm82ajxsicgrYr-Jvqx20iyWO4HJDsGMsFu-mmSah-WpTH83VvL0giyEIXSw5KP-Du5mDJOJBNaWG9cUOlfVA9WN76bpI9A_1haM4_EQM5CI3bTcqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NdRCd_ufCyveXGaYKBiXTj34KpCvJarGAW43gxSsoI6K5Pd71WYNWfCxxbOi2Q2nmtaLWOyzcx0XZk16c2akYZvu2hP6aNMr4lfnMGJnX79RQqL_9FvJ8qp4VGq1gTvJlHQkK4_Jt-vyHjsdnZIpmD9Tf5hxXLjy-5bgpr2sp1Vyql-FrmP6-iKdX_e8tu4ERH-g1xYZIs2yEEuzndm_UJKB7Hv6JawASQtOsplol9MfPnuP4VAfQKJ-mMUQzBUgTt05I5bTDCHJ5492P-G1Nj-EfWDeHU1KHMtmjz6KAp-T0lezxWqxGv2zI-BeL_XUA0D1MWzkQfigYefyafMMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZNmp5HKeMH-NH4h4QcU7WeqT-SC1n3S6T4rTIrtnWehKZx4aDhkh8a2n68XvZeVp1OrFtqj3MPDCfWASn5qEJv6NQJQIsh_uUhA4eQnVWEiU_lWFt2UPnghr261cHXyGdbpyb2X8mbR1Rycy6VhyJTp5BlI44R3hEGlO1yAfHdzDO11SjFzDN31QIzLITKdpsYBRH6BcafiCWbh93UX9Rz9T5XtEQ_nnyttX4tBeV-iyl6OTgxktu7Sqn5iTOLxg0UqH59ZENoWZ7TQRXqh9ANFpTy5XsqWd3Nekog7ZTghRBFOYAPcFVfFSZMuUNrmBLxVbnAZesTgv46Rc9FAQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xlj3l_J3qdLqtBfm1vDMbzXD1st-9HQdWNxmQKJHzbU1IHsB8cbDfyQvEsBi9Dl8_UMdmosGzZv-2u8KQ6myUyoPu-H8_JnIZxrC3yQUlzfY8C4Hgm_NOufinSZxhGFbBpLh_bQ-d9INlG6PNkq05bS1gpyf4Oxh370XBXTfRLOxuZTskK0rJlF1lMkX0KE2IDhpjHTqt-dfpAu7lc1w5ZUCqrqWs0uffVV0bRR4BRhv6oeBl9mv_x6sBb4hKMZtGk0GU2hXp1GZkmmGfaNaslxt6hRE5RWMNOwgym2EH-99FmGTDpUFzMEg1rAeaOljaOsNsaz2cwX3WptXV6I1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dFa5byI3EnvCWQ8FmmK4nYB8So3FlTpXwZmGixH-MKnpsoxcPSW3nzVL9mbZeICiepW8NfIktwaabAEPgaE06sD39CGpPmA7eoIe93DqtXJj1NJ00wQW4YUhpFgqPRl53_3XT-G2W1bz82mBuxbu-_vSucepvePyTAHeNNI_Y6l6Ihbz0O1XZTPys8PfQXEJOKLQyU2V-bTcvndpGdDbbiyhlgAaOwxDjayTbtQMobGpXYzngGluuo5f0Ikwp0C0smtN8QvEASQX98rdfLDMsV4Obh3_FGBnrpRZouLeSS5Q2UR_oA--LIcc96hnOHYocGzlNEgbQivaCKc320I-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BhQEwG9apTqPjbiqapyJ5nuF39KiUL7nzwx6_No-mQ79bP9VNn6nfPayxEf065ptorp1jfl7lRpyGageQktC-k65o9SjnMzm348HU_g3v7MHxFdW60dkGJqLS7VzH4i1VVb-PxnLpBzK_laYB4jNOMd4GpvF0BVFpySCQeOuQnOYPZ020p34UWKUX4BojsyOTxz5sJsuinwhtZn0lnyoA4n1xLkNplJOmKPrqWUTax9xGFhtJi5tLxeE08i8qdDEuIvfi7sDiqYZPpYtwe9gRuMJ3Jl2tG6OLE5HYWJDolOJhRbxmZObjEpU914_o9D9ioo4bkPUbwdi4zOCgYNvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bp_iLXIvUE7-3Kz0rEAh0d5l9NKk-TIOf1u64-MLfC5lQnlHdlsWULZBmQ92GB0r5X0lqHN_hH79iq5huJGdpTxhrzRR4RT25HClU7vcdAZ6-muKqUxtTKVO4ptyBmzLolDVWE3BU8BZgM7YopoTnGin-UEa5qESOe7vUeiomm5AZWbjvVngPD7GYQDg7gd9xo0YcFSl86t8izh1eWIUm9Sr0h9Iee-YljfKi0BwPVEhyRZT2DRYSjumzu9Ypba1nJ1gd00Xwt7LlZLpaCkBmhtYdHkhOoe3NaWrhmQQA65FGGR2BmSJbHKR4V3tT9VvZrBcVb2BuOLPiooDrQPH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y9hisKxyicbCmfXF1p-xOtJvdyUEF-629G5YZDCLAz2ey7Kpw7M_yIQw2hmKTSMJX67fxfOsDaZUj7a6lp5HGkBMn9WHatBg9QdHjuRADbLVoMVpEgZXYmmGKAV1QwhrH0M3frabiCqzGLAY1u3b83WRKZcRtl0_HEoo-0b7haNYFKFlHXre8Y85LRt73hbws_hClY3Sgpyym3MtuUEuB9TBozJPGHgnvkI3ynWK4tvwwiG0LM24JebptkbR91inb4r8isk9YK-AxvuKEPR1RKko9w3Ur6T4GZE5RjlqTbwO-hYXHhq93Zfocx1YhuqkYKP7zW7OdfPhiAY3ImJUsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mQiGHFf90XCB07nm5lpCy_3pwyxzIWQymlv5Vjiokx4XiAnt8a6mCRuoNlgaD6z5f3gGwBuus_QpZfTGqTsx0nsbNIyKbgJRL9xJUY4eKqVWht0cDu19pitkBwxcPRhKBLQ8pV0hId4fh2URRW5d7omHbR7K0fLDZ-EP6byCj1Yua6Twe8kBWsRp3NHQ_euDwosoguaxdFDhDtKs7RvqPdeHbHJji2r1iGGKpe3YohEJNVYdlATW3cXh5oalMFDu13WKrLZafZgZlhET0EUa-M0_Io-Idwo7J6pXT4vPB53mKF9sfL4DJOhKpepcKF_xI9LrPkMB31WSiwfFvqqj9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2467">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارش تحقیقاتی
HalcyonAi
نشون میده شرکت
ابرناک
(مالک جدید دامین ویکی‌تجربه) مستقر در تهران تحت پوشش یک شرکت آمریکایی به اسم Cloudzy مشغول ارائه زیرساخت فنی به هکرهای حکومتی کره شمالی، چین، روسیه، ایران و چند کشور دیگه‌ست. زیرساخت این شرکت برای ۹۰ روز زیر ذره‌بین کارشناس‌ها میره و مشخص می‌شه نه تنها گروه‌های هکری حکومتی، بلکه گروه‌های باج‌افزاری از جمله شرکت تحریم‌شده اسرائیلی Candiru جزو مشتری‌های این شرکتن و بین ۴۰ تا ۶۰ زیرساخت‌هاش به فعالیت‌های مخرب و مجرمانه سایبری اختصاص داره.
آدرس خارج از ایران این شرکت (که قبلا اسمش Router Hosting بوده) به دو کشور قبرس و آمریکا منتهی میشه. نشانی آمریکا به یک مرکز خرید در ایالت وایومینگ می‌رسه که آدرسش با بیش از دو هزار شرکت دیگه مشترکه. ثبت‌کننده کلادزی در آمریکا شرکتیه به اسم Cloud Peak Law که تخصصش ثبت شرکت ناشناسه.
گزارش تاکید کرده بعیده مدیران کلادزی یا همون ابرناک ندونن که بیش از نیمی از زیرساخت شبکه‌شون داره برای کارهای مجرمانه استفاده میشه. این شرکت در واقع به عنوان command-and-control provider به هکرها فعالیت میکنه و برای استفاده ازش فقط داشتن آدرس ایمیل و رمزارز کافیه. ابرناک در ایران در سال ۹۹ با نام «آلان فن آوری ابری» ثبت شده. دانش بنیانه، بسیار هم فعاله و در حال حاضر ۳۴ فرصت شغلی باز در سایت جابینجا داره. مدیر این شرکت محمد حنان نوذری به رویترز گفته فقط ۲ درصد از زیرساخت‌هاشون در اشغال فعالیت‌های مخربه. همینطور گفته نباید چاقو فروش رو مسئول خلاف مشتری دونست.
دور از انتظار نیست اگر اسم این شرکت و عوامل اصلیش رو توی فهرست تحریم‌های آینده ببینیم. ابرناک حساب‌های توییتر، اینستاگرام و لینکدین خودش رو غیرفعال کرده. نکته آخر اینکه غلامعباس نوذری که در شرکت ابرناک شریک محمد حنان (احتمالا پدرش) هست، دیپلمات ایران در نیوزلند بوده. حنان هم در پروفایل لینکدینش به تحصیلات در نیوزلند و در پروفایل کوچ‌سرفینگ به ۱۵ سال زندگی در این کشور اشاره کرده.
©
arashzd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2467" target="_blank">📅 08:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2466">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CJBQp7XR4gvwedkb3g59p7VGh-X0V61rIYir4VEbqy55fRnvKOa2OPq_99z7wf5n3DEO6R6FqjYKGglAon6e0tPM0gTENE3cOGf6iGj_yDbb5yQU2IXJM_95IiIDPqCofFNtsxIVgIlJ_D1aSVEq7_NuZ1eYB2ro4lYNfDliIl8x7z1nMs9UdhA8g-WwB79A6VYSXWSw_ONPQaUgB3OQeImCZYZoPm-1NALdw3MjSdW1VifPzZDiw63CDqAyqBWI5GxBOuPm1Z1dT7aJxinx8rdluVd1Zj-ETaIvQIqFtbrfi0K9_41jcPeeC9s_L2qjvoK2js7tGN0IJNNf0-4O2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از رتبه‌بندی جهانی اسپیدتست حذف شده. شاید فکر کنید چون دیگه حتی ته جدوله، رتبه بدترین اینترنت هم توصیف مناسبی نیست، یا دیگه زیر ۰ و منفی جوابگو نیست.
نه، چون چیزی که داره ارائه میشه اسمش اینترنت نیست!
👉
speedtest.net/global-index
©
Mehrdadlinux
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2466" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2465">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/owvvgAvl5qdmNqh7Zd6Xf5_sNKELzqM66xzFRroZVSpCzcNfDOcxTDc7Bz_JNabdJFZmzGj7NkBPAICbpvDMhQAv29PDe5s8bEGUIgLBa1eK05sLhtKzI3FcAQJDEcymzk10zH0MBsrDDzhQ5UoNCYcMdO0KnHExFH3WYphGJ1XtuAsxdQ99VXl0c-vnFwLOGHPNjIU_qk3s7EGpFiFwoXMssRBa-EG9YAN46qSPIi8PqpFM2zvIjC-e5KHDGwu01bbWY9W3RCnWQXtFu1Uhusb5WOZ5sVC2Q6VYAD-4A1J0sDZtt5UNjtl6HG5tzzwh7BpJA62dQlk7Eze7CNRbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این چندروز احتمالا در مورد اکانت ویکی‌تجربه و سرنوشت نامشخصی که برای مالک ناشناسش رقم خورده چیزهایی شنیده باشین. متاسفانه دامینشون رو در ایام جنگ و قطع سراسری اینترنت نتونستن تمدید کنن. بعدش این دامین توسط ابرناک ثبت شده و با یک پیام مسخره و کینه‌توزانه، صفحات سایت تغییر پیدا کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2465" target="_blank">📅 08:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2464">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sNoc1xVIIdTexO8o_DOS9YqGvgWhomrItZ_2oN0NEUBIOZGde9XUHZ5yj8fGNE4X2uguBJq7wAD_NAKlw5e4Kg1CjlLSVspzm-4RU5fxGB3uI3MsV9ky2GJlwWcTa1xeNjjiIcEYKfuJhAdpz_2g8IbCfCnPTNz3l9UO74owaqalAhUWNakZwqR01son55p6Iq89PyTBV_VeEWPDpE6QHQH0pFpusEEgVn-cVfKv_YbKNb2ZGbRKFaRwMEabXnoasvO3mtx1ikzh7KIjPqieE2df1z5nHxKCKXZYiWr7LZiBn5CYz-l_2FFQq4pqrOSp0ExAFuiZWciVAvp7Nf0E3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از
#لینوکس
استفاده می‌کنین، فیلترشکن دیفیکس در جدیدترین بروزرسانی خودش پشتیبانی از این سیستم‌عامل رو اضافه کرده.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2464" target="_blank">📅 12:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2463">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ogzHQEIBCJ0P9VaIyWOnKS2O3JMX5CQhukbUzun2hL_hYbfiZHym0nZPOEEhyzSC4Lu0XafKCygJECfsJqILOIqBeNflss1LCB0N8BQydc_Jd7D35CslJ3Wg9OfmJiWg8LIE8amB5OSnXs6nz_4JQQUQd3Aa9ZknqxuxIaoslXXfvrw7zzatk-sDSrZM3pmBKjLHRtokbA--fAxtfeVpVDdp3DKXpuTi9fu3wnAEC3y30CAjjALZhIGN4u9YyvYzIhMZW7bvqI3GNJAYWVzfO4_oj9BroozxLrCiL5mBvh71uagEJfOkbsH3VLznLOLNWL4XjPC0tg4GJwLR5sRXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ RedCloud VPN یک کلاینت متن‌باز و رایگان برای ویندوز و اندروید هست، که با استفاده از هسته Xray توسعه داده شده و امکان اتصال از طریق کانفیگ‌های VLESS، VMess، Trojan و Shadowsocks رو فراهم می‌کنه.
این برنامه تمام ترافیک دستگاه رو از طریق تانل‌های رمزنگاری‌شده هدایت می‌کنه، از قابلیت اسکن و سنجش همزمان IPهای کلودفلر هنگام اتصال بهره می‌بره و همچنین با استفاده از قابلیت Sniffing، ترافیک HTTP، TLS و QUIC رو شناسایی می‌کنه تا عملکرد اتصال بهبود پیدا کنه.
👉
github.com/Devtahas/RedCloud-windows/releases
👉
github.com/Devtahas/RedCloud-Android/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2463" target="_blank">📅 07:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2462">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بانک ملی از اختلال مجدد در خدمات کارتی خودش واسه ساعت ۲۲ تا ۲۴ روز جمعه خبر داده بود، که گزارش کاربران نشون میده این اختلال در روز شنبه هم همچنان وجود داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2462" target="_blank">📅 07:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2461">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الان خرید کردن با کارت بانکی مثل دستشویی رفتن شده. اول باید چک کنی آب وصله، بعد کارتو بکنی؛ وگرنه ممکنه گیر کنی.
©
shokhmatic
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2461" target="_blank">📅 18:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2460">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">در حالی که با اعلام شرکت خدمات انفورماتیک اختلال خدمات کارت محور بانک‌های کشور برطرف شده‌اند، بررسی‌های کاربران نشان می‌دهد که همچنان بخشی از اختلال‌ها در خدمات‌دهی بانک‌ها برجاست. اغلب اختلال‌های موجود در بستر نرم‌افزارها و همراه‌ بانک‌ها برجاست و این موضوع کاربران را در برطرف کردن نیازها روزمره دچار مشکل کرده است. /ایسنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/ircfspace/2460" target="_blank">📅 18:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2459">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h3S73PZF1cn3EQTWZJkYo02yTfc8x82gdk7O9fOh1zRNmRaXHq5QjXZfTTtUOEwwZw83q0-_id9oqmTOwPcWZ3Pv1Qg-MPPRSthVwE6Z0nbPIvyk673U0Tb5zH9Zu03DAn9iFoINMPZvd36PefYGCIBIgmDWol2513zTSYJkR2E4-mT0Dyau4y2QRMnG865Lt2na8suHnIuXvgAN03yJr-HPMlejAkDJJuIElIaTF7ZXo12oum3iRH-BnurmOYLzRK2MddMp8k0x-Gc0Wu3qV3Y452lzTVdkazXLOkAwMeUSOnBvgjhlBtcW4EZkt4QhRVuiWGhX7WQQ_RC6eLwAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسیون اقتصادی مجلس طی نشستی با ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات، از عملکرد این وزارتخانه در دوران جنگ تقدیر کرد. /دیجیاتو
بابت تقدیر یه کاسه دادن دست وزیر قطع‌ارتباطات؛ اما بابت ۸۸ روز
ریدن
به اینترنت باید یه لگن بهش تقدیم میشد!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/ircfspace/2459" target="_blank">📅 20:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خدمات‌دهی دست‌کم ۸ بانک کشور با اختلال مواجه شده. شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، حملات سایبری را تایید کرد و نوشت "شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است". /iranintl
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/ircfspace/2458" target="_blank">📅 16:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2456">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اختلال خدمات بانک ملی بعد از چندروز نه‌تنها برطرف نشده، بلکه این اختلال فقط محدود به همین بانک نمیشه و خیلی‌هارو گرفتار کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/ircfspace/2456" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2455">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">جنگ شد، اینترنت رو بستن، تنگه رو بستن، آتش‌بس شد، توافق کردن، تنگه رو باز کردن، اینترنت رو بصورت تدریجی برگردوندن، گشایش شد، مسابقات جام جهانی سر رسید یا هر نمایش و کوفت دیگه‌ای؛ ۸۸ روز قطع سراسری اینترنت، سرکوب، اعدام، زندان، شکنجه و کشتار ده‌ها هزار نفر معترض دی‌ماه رو به فراموشی نمی‌سپریم.
خون‌هایی که روی این خاک ریخته شد و نسلی که هزینه آزادی رو با جون خودش پرداخت، از حافظه ما حذف نمیشن. بین ما و شما دریایی از خون فاصله هست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/ircfspace/2455" target="_blank">📅 09:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m5NoDH1NrkTvStCJFmC0zEMQyW7yk47sUCZJEFBdzn3gt-GF0GSfm7taSnA-mkPVlWGYsCAzLQFychFhMcYSVAEjoni-49T468Nfb5LjAeqpboaAuJXXy2n3I-rXZ7XmuwOKHoKxz-W6rqsBFvACHwl2o4MIjynkTCdDIywr8eh_in-8fHLVFM2wcjS3UAgS1j3mWIIvK9r0t-zVfAv7moNHPgdLuDB-XLrSFpjrCC1-hjecXx2Pay4RcvInuX0ntwwWT9xP_kChH08IaYTwAVhnBpyQTVvLdDUGGpJXpo-_gFmtM3lnPMIZJ4xhw3hOpMxdQ3tmcQlSAbgjMJ5OrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل V2X یک ابزار مدیریت اشتراک سبک و متن‌باز برای VLESS روی WebSocket + TLS هست، که به شما اجازه میده با دیپلوی پروژه روی سرویس‌هایی مثل Render، Railway یا DockFly، برای خودتون و خانوادتون اشتراک اختصاصی با قابلیت بروزرسانی خودکار ایجاد کنین.
این پنل امکاناتی مثل مدیریت کاربران و کانفیگ‌ها، تعیین حجم و تاریخ انقضا، نمایش آمار مصرف، مدیریت IPها، اسکنر داخلی و ارسال گزارش و هشدار به تلگرام رو در اختیار شما قرار میده.
👉
github.com/SulgX/SulgX-Panel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/ircfspace/2454" target="_blank">📅 09:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GxrZktf_Zw2jJlVTImfowSjHT-QgI9WkHcHgiRGnEQn6sL-RTzKXKU3xsEQUtgGf-WJTML5LtiuB7CLCdfxT9NDtZwgtjT7u9iEhRbcdBbKdVSRXo3zwm_AZfuRimpWssF_rzWMXZh_2HiJAxE7agOLhgpfJ9Qf3xSEzIX0sXTRiwywIsr6GTSRY6Wt2wyHOaGODAV6pODm-swVTZk54DcSTAbRB0JKOmP0UUQutnBFUd2-GQSd4RTiLWBdaMG7zRWMpOGrPyF2tWuc1CPOOiXByYmOnBo-mhL8VWHzYm7Pt4BY0e5Si4uTMcPCxFqiCNoRL6IkGu4Ob2f9tV-ljcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کاربران ایرانی به نام MrArrow دو مشکل مرتبط با فرگمنت در v2rayNG رو برطرف کرده، که از نسخه ۲.۲.۵ به بعد این اپ اندروید در دسترس هستن.
این کاربر توضیح داده که "چون تو شرایط فعلی اینترنت ایران Fragment نوع
tlshello
روی خیلی از اپراتورها دیگه مثل قبل جواب نمیده و بین حالت‌های مختلف،
1-1
معمولاً عملکرد بهتری داره و حتی با مقادیر پایین Length و Interval هم میتونه از فیلترینگ مبتنی بر SNI عبور کنه، یه سری مشکل در برنامه وجود داشت".
مشکل اول این بود که با وجود اینکه هسته Xray از Fragment نوع
1-1
پشتیبانی می‌کرد، اصلاً گزینه‌ای برای انتخابش توی رابط کاربری v2rayNG وجود نداشت. مشکل دوم هم این بود که v2rayNG عملاً فقط
tlshello
رو استفاده می‌کرد. یعنی حتی اگر توی تنظیمات نوع دیگه‌ای از Fragment انتخاب میکردی، موقع اجرای کانفیگ دوباره مقدارش به
tlshello
تغییر می‌کرد و انتخاب کاربر نادیده گرفته میشد.
👉
github.com/2dust/v2rayNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2453" target="_blank">📅 09:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pr5BXGERJyAvEt3zDKtt_zaE4COqy_gyn_WgT6JWgLPDcWFsR57ew034zGF9vcFsUH4Xp1hnb2PvyPlZnUBA37BplmJKlG9FvpUGMzkYo4_Myb6ZKxXKmLBwdljpDeqabjzSoo4GPDS87ojKmMBNvv1NFyyILQVDXrvRd5U8NPLuPLRK2IQWNvkjuS4dHnW6wc4L3IxBTd0cdvsNbWCCx1OxIvhrM4QNy7WEI92xGVtDuFJFn51Os8evJbomRGllSHBLtxjTV5zvE3zY_0GOh8zKHzDTglhLyeGQs53cM4RbJ3eXE8RfUKihzJwQMCAXhZsPdu0C9g26mpD1r-zDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکت اندروید F-Droid (که کاربران میتونن بدون وابستگی به گوگل‌پلی، اپلیکیشن‌های آزاد و متن‌باز رو ازش دریافت و نصب کنن) هشدار داده که گوگل قراره از سپتامبر ۲۰۲۶ قوانین جدیدی رو روی اندروید اعمال کنه.
طبق این ادعا، توسعه‌دهندگان برای اینکه برنامه‌هاشون روی دستگاه‌های اندرویدی قابل نصب باشه باید در گوگل ثبت‌نام کنن، هزینه بپردازن، مدارک هویتی ارائه بدن و اطلاعات مربوط به برنامه‌ها در اختیار گوگل قرار بگیره.
منتقدان میگن این تغییر میتونه نصب برنامه‌های مستقل، پروژه‌های متن‌باز، نرم‌افزارهای شخصی و حتی برنامه‌هایی که خارج از گوگل‌پلی منتشر میشن رو با محدودیت جدی روبرو کنه. به همین دلیل F-Droid و برخی فعالان حوزه آزادی نرم‌افزار معتقدن اندروید بتدریج از یک پلتفرم باز فاصله میگیره و کنترل بیشتری روی اینکه چه نرم‌افزاری روی گوشی کاربران نصب بشه، در اختیار گوگل قرار میگیره. به همین خاطر کمپینی با عنوان Keep Android Open راه افتاده تا کاربران و توسعه‌دهندگان نسبت به این تغییرات آگاه بشن و به اون اعتراض کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2452" target="_blank">📅 08:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کاربران میگن "ظاهرا" دسترسی دیتاسنترهای داخلی به اینترنت داره برقرار میشه. فکر کنم هنوز از اون زمانبندی که نامسئولان قطع‌ارتباطات گفته بودن "بازگشت اینترنت درحال تکمیل شدنه" چند دقیقه باقیمونده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2451" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h_pj5BUFlwuIe5pRlo7shEHBRUVge536SK_LzQzom-RjZXd_SNO9L6mcbgnWPuGRKzWQMsS1kTj9tqs8JXM-N7YoOpFtsRodWe9fg7kJ2mF5ZrpOusyPXG0Wb4Pj2h86M4Gg4aKOboJUkO6d2zeY2tS4pI-LWEMEdP5-mAF0V6H8G-bVE_6Zc4v4StMfPDMYwdak5oSWZYoHHPgmsmRuLkfn5X8EU00ldhmL8o49ZBtF-ZRVZBe1JTBuTwNuqv4OuMI36dNetitZhaYlgiIv7QwZhBk1DoOD0raE5313aHlywwE9xB356E2-tOVOzfki_IhliAOLYYy71-kFEXB64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما تنگه را مفت ندادیم، زندگی یک ملت را مفت دادیم. سال‌هاست حرص و ناکارآمدی‌تان را «سیاست‌گذاری» نامیدید، ماشین قراضه را ده برابر فروختید و گفتید حمایت از تولیدملی، اینترنت را خفه کردید و گفتید «مدیریت»، فقر را گردن تحریم انداختید در حالی که رانت و انحصار رگ‌های مردم را بریده بود. جوانی را به مهاجرت، کسب‌وکار را به «تاب‌آوری»، آینده را به سکوت فروختید. اگر چیزی واقعاً مفت رفته، نه تنگه هرمز، نه یک وجب خاک؛ عمر مردم، آرزوهایشان و فردای سوخته‌شان بوده. این صورت‌حساب واقعی است.
©
rassssoo
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2450" target="_blank">📅 08:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این اختلال GPS بخصوص در مناطق مرکزی شهر تهران برای چیست؟
داداش طرف اومد نقطه زنی کرد و رفت و تمام شد. الان GPS رو مختل کردید که چی بشه؟ ملت اونجا سرگردون و گم بشن؟
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2449" target="_blank">📅 08:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TACu08cae4FrBnRB2NKhoa3ubSpYPv_l_6aAiTzUpUrtv7ASgULwZGUt7EdMQEn0PTaR__Um_n6Gc5B8zHhdVq3uBEFsth-Z3LhuYs7TVEhzOjOTYwggFB25ECIL5bOUf9_t2k_I9JHji9QUyFEDQj4uceyYBAoVSr6gVIaD3-mTHP-AYIbay6u3uwtAqKESI9g_BDChymFvAj9NvLW4YPWbs9GYZvWNF_uIcGp2Ll4c5XB41AExWWkc3oIQh__HxRs4TGn8cY713bmytQUJfP8yaXMPtnofzR9-lHggGJFJSoKZGcPss3GPEz4cfE3Y-Ozyjqsw0mc0MAEto9ADyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه CandyTunnel یک ابزار متن‌باز و رایگان برای ایجاد تانل روی سرورهای لینوکسی هست، که با استفاده از تکنیک‌هایی مثل تغییر و پنهان‌سازی آدرس IP، رمزنگاری ترافیک، بازیابی بسته‌های ازدست‌رفته و روش‌های مختلف عبور از فیلترینگ، تلاش می‌کنه ارتباط کاربران رو شبیه ترافیک عادی شبکه جلوه بده.
این ابزار از پروتکل‌های انتقال مختلفی مثل UDP، ICMP، Proto58، TCP، QUIC، IPIP و GRE پشتیبانی می‌کنه.
👉
github.com/AmiRCandy/CandyTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2448" target="_blank">📅 08:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfeiiavh-NVxlfiwkPEyO9obJ-KI5s4ogUBAd3s5RJByVaSJ-jDqUQJyGpzjKfJwBaEU1FzEuAJurQNr5cODhRWClnWGv90gY0NhNIT9XPKu2y1M0nzRUKQwHVha2kib7aKvXgtrod9J6loj7QrtgFgb20T1TfCX7dSCaRiPnaEeepqLJMLUWUEdHtH1owquWspSZireo-40cUV38sigi3GbCJTleSa8FOgoNbsDoVdUgMq04bYMInsC6igtrxf_sscCPYTEVf-EJkaJ03o-KV_cztSDeWLf8880EyXQ3EcTP0zXyq4hP4zcs2A8dIp76NP-QcZQ9fYEb6YosWeOjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Config Converter یک وب‌اپلیکیشن متن‌باز هست، که ۳ ابزار پرکاربرد مبدل V2Ray، مبدل WireGuard و مبدل Clash/Sing-box رو در یک محیط یکپارچه گردآوری کرده.
این ابزار امکان دریافت مستقیم کانفیگ‌ها از لینک‌های سابسکریپشن رو فراهم می‌کنه و ورودی‌های Raw، Base64 و JSON رو با تشخیص خودکار فرمت، پشتیبانی کرده. همینطور کاربران میتونن بصورت گروهی آی‌پی، دامنه یا پورت تمامی کانفیگ‌هارو ویرایش بزنن.
👉
darknessshade.github.io/Config-Converter
💡
github.com/DarknessShade/Config-Converter
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2447" target="_blank">📅 08:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cqlHHceKezKd8cZqMBoewsVuxlQWLHbp1C_7Kh1DorUxsTdTFZ6YbkBJefNDLqcYEEFfG6y4iJyGbMahQAyFC2w_VpiONEpHAbIP0DDJPqqdUpE8YyNDUojTSMM-wNBfIwMF4-qM7OoHx6AP9BhlopCxQAk94cFXLl3g5z5xnsGS3j_kESsXOIOMrpIyZYUiAlMp13XUvU0fvItyJrysyrZ3HNLLr1x8atHhcfDVP3DnHUQVRIh1FxKH4ucXeQgCg0OUCcpau9Hpj6B7sD80F1YW9-rHxGywPZW-87eanHDOvKs0CJOofEuAnWfNdlM3NJoX0TF4tfP1NGF4Xoj8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند. در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2446" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L5qETOucnpYvCd2J1WlR5gGCPnCPquncT427T4P8JIkWeh-NdHeUseiI5Rxvav4GI-mJNv05-T98HWNMNk10u9t9Ey0twpWadvqiukkGpo823xsp2_ogwLrZIryWSaBEDPUMVpVi9ebir4Ep3Jeg6s1cnYOGh1t1VzL-R_6VkGoNBWuRfpbJIltec6D03o9n9gj1QGC5Vw2WvZp_n353n7VifXj9JsNuAkByIVA-ADkXeGT5HXaWnzM4wtvJ4turGEZh8-1CYSBOiga1ufgkY4pamFU_aDbcDF4iQWmZ8iuMKgdR_VaLfdTsk17oewQPSjwmdsorHqirCwwfJJZy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه NipoVPN یه ابزار پروکسی سبک و قدرتمنده که درخواست‌های واقعی HTTP رو بین ترافیک عادی وب مخفی می‌کنه. این پروژه با معماری Agent-Server کار می‌کنه؛ یعنی برای استفاده ازش، اول باید هسته رو روی یه سرور راه‌اندازی کنین و بعد کلاینت‌ها به اون وصل بشن. در حال حاضر هم کلاینت رسمی اندرویدش به‌صورت متن‌باز و رایگان منتشر شده.
👉
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2445" target="_blank">📅 08:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2444">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXG05CK8d36893LDl5KUJRoPQB7pR64v2elNvbVVzlMpH4OvE2EzfnIUtXDF2GKjwb3CO7N7S6586IcX6_77kK8LI7Sv9wzd4u8WjtM0kzw1hwnZWmnO9EDpYas78xh_bBqTsDhL5Fi3SgKBEN2mn_kahzxjBVucgz_WaKYbe_GvBU5yxl3xZwfuptra8jc2uODqUZ80LAfnHwYKT8UbCWq3gdRM4PEAZZ6tklB88l7VbsD5nodSzJTgxXM7OETDX3ENZzWDXvTG-AYZIV7_8W1Kj4WfNu8DzrZzUBqFintN2GUiDpIXKYWGFVSzUGV1EfqQuMD01vHefvn_sWMz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ InviZible Pro در بروزرسانی‌های اخیر نسخه بتا، با اضافه کردن Tor Snowflake و پشتیبانی از پل‌های DNSTT، قابلیت‌های ضد سانسور خودش رو برای عبور از محدودیت‌های اینترنت گسترش داده ...
👉
github.com/Gedsh/InviZible/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2444" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2443">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پاول دورف، مدیرعامل تلگرام در واکنش به محدودسازی استفاده از شبکه‌های اجتماعی برای افراد زیر ۱۶ سال در بریتانیا گفته: این ممنوعیت فقط اونهارو بیشتر در معرض خطر قرار میده و کودکان به استفاده از VPNها روی میارن، که در نتیجه به محتوای غیرقانونی و به‌مراتب خطرناک‌تری دسترسی پیدا می‌کنن. برای مثال هم به استفاده بالای فیلترشکن در روسیه و ایران اشاره کرده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2443" target="_blank">📅 08:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2442">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">از میان ۴ بانکی که اختلال برایشان پیش آمده، ۳ بانک در بستر ایران‌اکسس فعالیت می‌کنند و دسترسی مستقیم به اینترنت ندارند. یعنی هیچ ارتباطی بین آن اختلال‌ها و وصل شدن اینترنت نیست.
©
emirhussein_rz
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2442" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2441">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPIiceRIjFmeRM0BHxsj14cONDRUX5MLIm1nGRk5cBbOkHYHObyn2TS4DhKihOX6kMu6fm-1yUAQifyGZRtgrWe3wTdrc5y3U2oAh-0zT9qQCyTEdWhiAY9jovDugCEqEIGceIk0YOEhowVzlg2n9TLW_fgQO6J88CjYjY_9NA-Zc95qbuuQBOWVYkNkgHOtSPVLyVyU6ircfjIgapYuSEhGnzW3Mf4n6BdFyQDo2XIl9B9016lgSKheMnepRmhQxGNQ4rVTLJ4HAG7yM4msTmN3VhdYsLpqWOnB6XQMMOSHoQxzMK75UIpWxepNsQTyVUNgvuRlG9yXGihi6Kx-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویروس زارع‌پور به هندوستان رسید؟
دولت هند اعلام کرد که دسترسی به تلگرام رو در هند تا اول تیر مسدود کرده، چون از این پلتفرم برای کلاهبرداری از داوطلبان شرکت‌کننده در آزمون ورودی پزشکی استفاده شده. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2441" target="_blank">📅 08:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2440">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ipa5-H8L8qiZnsdqqT0Jy5EO32cVWLu8ElRTU-QMbOeETgfRyVN0ncnI1OnGLHwJFJ08P-UdxaZ-V_im4rTuld6xleOf3zCflrjf4kQyEQ4TOqKJwmPMPFqF3U8fJMvcFRusy5B-CYXGbBLCYMpRiGXuHoJDxYKAwzC7jIvZaHYbksjXKrYZsLq4xNJWaALHdyK4l7aQxnIzIYvFBte-lFz9KYIVKadJtAdgZLBI9ftlx27U5RP9xoTMYN0m4Bwqondatk2iNLVOjPf9AnW0E0blVHKv_Cn7mlSvWfZB-lgXBxEvF_EiKYP3cMBLedhU_TgdrZ4geQpmxIDt9ohGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ سیمرغ یک کلاینت VPN متن‌باز و رایگان برای اندروید هست، که با پشتیبانی از کانفیگ‌های XRAY، پروفایل‌های NipoVPN و موتور اختصاصی MSP، تلاش می‌کنه بهترین مسیر اتصال رو با کمترین پیچیدگی در اختیار کاربر قرار بده.
اسکن هوشمند آیپی، انتخاب خودکار کانفیگ سالم، پشتیبانی از کانفیگ‌های ServerLess، پروکسی محلی، ذخیره IPهای تمیز، بررسی سلامت کانفیگ‌ها و ... از جمله امکانات این برنامه هستند.
👉
github.com/rezakhosh78/SIMORGH/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2440" target="_blank">📅 20:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2439">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">با وجود ادعای رفع مشکل قطعی و اختلال در خدمات ۴ بانک بزرگ دولتی، این اختلال‌ها برای سومین روز متوالی ادامه دارد. نیما اکبرپور، کارشناس فناوری، معتقد است طولانی شدن روند بازیابی، نشان‌دهنده ناکارآمدی سامانه‌های پشتیبان است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2439" target="_blank">📅 19:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2438">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=GBqoKVmfh_HUID-ER_HlSjO7gSK10ZY-p-PIQ1c8jerihV4lUWeii4DEwsm-sI-HopXGV0GcC-JpvHTZVwiP-TnoqhhT-Ofu4L9PVAfThjUEv9l4R9XDUq74KPoVbtg0L2X7UicPTy8w4p7jpuaKvQPPDAgGSzqii1qUqChQuFUxJ8DdXgts512SzJDbJ5VFf-Gu9dfN32kSYkiDNMnRYjOzAA6QK6jIiQugpneTLTA42Nxq8L4qmtd_DvVqE5pJULPSuWg_OdxaMj6n9DMXJbLIeksACXItLa2xN3uh-xmnTKz9VsP_gLAyOQkGebtDmDmYCi7caAxmNu4NxXVRfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/672c6641f0.mp4?token=GBqoKVmfh_HUID-ER_HlSjO7gSK10ZY-p-PIQ1c8jerihV4lUWeii4DEwsm-sI-HopXGV0GcC-JpvHTZVwiP-TnoqhhT-Ofu4L9PVAfThjUEv9l4R9XDUq74KPoVbtg0L2X7UicPTy8w4p7jpuaKvQPPDAgGSzqii1qUqChQuFUxJ8DdXgts512SzJDbJ5VFf-Gu9dfN32kSYkiDNMnRYjOzAA6QK6jIiQugpneTLTA42Nxq8L4qmtd_DvVqE5pJULPSuWg_OdxaMj6n9DMXJbLIeksACXItLa2xN3uh-xmnTKz9VsP_gLAyOQkGebtDmDmYCi7caAxmNu4NxXVRfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانفینگ
😄
©
miladiels
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2438" target="_blank">📅 19:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2437">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در پی تجمع مخالفان توافق ایران و آمریکا، خبرهایی از اختلال در
#ملانت
و پیامرسان‌های رانتی منتشر شد. خواهشاً اینترانت ملی رو قطع نکنین؛ عده‌ای اگر مدت کوتاهی از پروپاگاندا و خوراک تبلیغاتی حکومت محروم بشن، ممکنه ناخواسته شروع کنن به فکر کردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2437" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2436">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فاجعه یعنی اینکه اول حمله سایبری رو تکذیب کردن، اما بعدش بصورت رسمی تایید شد. الانم نشت اطلاعات مشتریان رو تکذیب کردن، احتمالا چون قبلا هرچی بوده و نبوده پابلیک شده!
شورای هماهنگی بانک‌های دولتی، اعلام کرد: به پیرو اختلال پیش‌آمده در سامانه‌های ۴ بانک ملی، تجارت، صادرات و توسعه صادرات، تیم‌های فنی بلافاصله پس از شناسایی نشانه‌های غیرعادی، اقدامات پیشگیرانه و حفاظتی لازم را برای صیانت از داده‌های مشتریان و زیرساخت‌های بانکی کشور به اجرا گذاشتند. بررسی‌ها نشان می‌دهد حمله سایبری محدود به چهار بانک بوده و هیچ نشت اطلاعاتی رخ نداده است./ انتخاب
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/ircfspace/2436" target="_blank">📅 23:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2435">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ایرانسل و همراه‌اول با گذاشتن ضریب روی بسته‌های بین‌الملل قشنگ
عَنِ
دزدی رو در آوردن. گِل بگیرن در اون وزارت ارتباطات و سازمان حمایت از مصرف‌کننده رو، که دزدی اینقدر راحت و علنی شده. البته چیز دیگه‌ای هم نباید انتظار داشت، یه مشت دزد دور هم جمع شدین!
©
Mohsen_935
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/ircfspace/2435" target="_blank">📅 17:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2434">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/peMhAf4oYlSTLDucOTD5Re2XFuYUIBIrHG5zPqwDCcLMK3SqOPgXmt766YSGhY9sfa7Fu8g7dehqbquGekJ_jgPCWUGf5Zu7vSqRKyFPXf6ZR8BSlJDbYNo2wyvwMRuf4at8-Zlzj4C0fMqUTvdR8agYLh4-pmLTo45P6NTsouB-V9h4km2KA36TsVAcOLfcJrg4h5MvX8OL3TZiC9OxeUv-sUZPVJ4BMbqzDoby4TwkVRPyV31COV90nAI2xrdb3nmnJMGS3ZYvYQvkVxcgnY9guHeRFyko3Ts-eBdNCIlnHrU-8yC-uSAtw-8j3-jq2airKAP8d13zwbl7GUPU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به دنبال بروز مشکل در ارائه خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات از صبح امروز، پیگیری‌ها نشان می‌دهد عامل اختلال بروز مشکلات زیرساختی در شرکت ملی خدمات انفورماتیک بوده و ارتباطی با حمله سایبری ندارد.
البته تاکنون زمان دقیقی برای رفع کامل اختلال اعلام نشده است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/ircfspace/2434" target="_blank">📅 17:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2433">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VlLnqrPDSAARcJ_NtM59xYg5wUFkLrtSQRufl89yQW-YoRNvDi3d2akrl3GDxE7dzW46igDzgYIddHQj4huNoDKQu3NJImGU76JyOY49jXTuYRMmIk9zgZi29Wqom_1o4sXNpVXGDVipPcZen0yv4oUwUfxCKvdhsBoJUgmA_ALq9bNU6kiXyflMafC14XM887D3JLhllV0RrHGbEczZT-mJ6s6iD7TInQ5fO9CShWqNOjlQsgQf2pcl92HkFFbzMRhicVDM1oSIlxQ03Dq6yLQWSVtFCRRU9HNfjZ4_qOFb_vp9mOnOV3mz5UvRoH1KCaVl1E9bgWdd9wHto4eRgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اعلام کرد پس از دریافت گزارشی درباره فعالیت ده‌ها کانال یوتیوب مرتبط با اشخاص و نهادهای تحریم‌شده ایرانی، علیه برخی از حساب‌های ناقض سیاست‌های خود اقدام اجرایی انجام داده است. این شرکت جزئیاتی درباره تعداد کانال‌های مشمول این اقدام یا نوع محدودیت اعمال‌شده منتشر نکرده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2433" target="_blank">📅 17:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2432">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HrH57J_fKlhByTi8MGMjMk6gKdpbtl0Ed3MEf-23XVBlwkbUX065rVsBnUz-poVYb2QAFw4OkS3N6IR21vvDoIR2BaO3YCOWwQxNxP_WkERr1rt2Ty26PMaO7hQ8oH3m120ZX0-8hLsDNvvRpGAjJNcZhgFVsSDmLK8V8knnFw0RYTeG6lOHx98eo8gB1SNZ5zCVwXBp_CzFdGNn54bfEuRBZnWymdfWWwtdcsIowTaPqN2mo69ah0DBzEMbwqIAP2ML1S94PPgG2qsMzWP5pjehR3PoYs74oUSwkc0kiFHnWKlaTiNWqEZ0IfHCOWb-WSXILxNsuATcrvNRcUYNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستار هاشمی، وزیر قطع‌ارتباطات اعلام کرد پیش از بازگشایی اینترنت حجم ترافیک استارلینک با کل ترافیک اینترنت کشور برابری می‌کرد. او همچنین طرح وایت‌لیست اینترنت را برای جمعیت ۹۰ میلیونی ایران غیرعملی و غیرقابل اجرا دانست و گفت به آنکه ایده‌اش را مطرح کرده بود گفتم ماستت را بخور. /یورونیوز
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2432" target="_blank">📅 08:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2430">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ITSGeK1-jTVORcLBN9p7v9OrIAJCM5qqZN9gztCL2UbKU6G9qmJhwaIsfuNQMssQ1qveXrhjqQ2UvFUBiKuo5scFDqaCslSGmLg2gmrFsczIoTpkktpRJs8c752TN3lBlNQDhwMBivm0kgfq80oGwu7yTfqg6NAC1fWfWMn-7A8nTnqEdWuFnja9UZ3LjWJQbcyxTdRRJaVH9Dgl5VIklkPqBpQ3iAHiRdrtpE4N9N55p4Rp41y8rT4e-TtvhV1jIgoFM_5M6efcQN9x72lmm6i3zCCbPBC6_RK1gK4YCcjRT6Zh0JKISjS0AYuQRP1WKPSQJ9FrOY5nXQatg2GpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌دنبال توافق‌نامه‌ای که در اردیبهشت میان شرکت ارتباطات زیرساخت ایران و آذربایجان برای توسعه ترانزیت داده و زیرساخت ارتباطی به امضا رسید، بخشی از داده‌های ترافیک اینترنت ایران به اپراتور Delta Telecom در آذربایجان منتقل شد.
داده‌های موجود نشان می‌دهد که آذربایجان در مدتی کوتاه از رده چهل‌وچهارم مصرف ChatGPT در جهان به رده سوم رسیده، که انتقال ترافیک اینترنت ایران از مسیر یک اپراتور آذربایجانی این اتفاق را رقم زده است. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2430" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2429">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور گفته "نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه".
از اونجایی که دولت کلاً هیچ‌کاره هست، نگرانیم بیشتر شد!
😒
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/ircfspace/2429" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2428">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BBCzcLVnlVfZ7J-s_e8mDgIID1S1rU80ZzJRI1qdSypsFN-G26LNSoWqc_9QO-nOP-rBplPhb3p79YoIxHhhOjn_kwfEM5WhU8JV78aEASD-qrf6M_664rc5QiPZVOdeq0Y5hNe4y1764pqo77laMn77HQftHee9QJ8-diWANkSUlGTRc3JG0zs0HRrlqzDvtJ7p2Kgpr7srJE92Tg6xGlo099Kvn7FqE6kNsaVqxfMlsNJCFkWMPKfsf5u4z12cVBe0BMYTzt5qD_ACMAc-0WNRdCCVDK-V8svgqY_qGK33pUe11lm90fcxCACqCdx_WTvu2JrnI8eXzTbgaZdYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن متن‌باز و رایگان pyWarp که برای ویندوز، لینوکس و مک ارائه شده، ۹ مسیر اتصال به وارپ (با انتخاب گزینه Auto در Protocol) چک میشه و در نهایت اگر اتصال امکان‌پذیر باشه، بهترین رو انتخاب میکنه.
👉
github.com/saeedmasoudie/pywarp/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/ircfspace/2428" target="_blank">📅 08:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2427">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هنوز موشک‌ها توی آسمونن و به زمین اصابت نکردن، پهنای باند رو کاهش دادن و گزارش کاربران از کندی اینترنت و افزایش اختلال‌ها حکایت داره!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/ircfspace/2427" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2426">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بعد از ۸۸ روز قطع سراسری اینترنت و برگشتن دسترسی‌ها، هنوز اوضاع اینترنت به قبل از دی‌ماه برنگشته که دوباره دارن واسه همدیگه خط و نشون می‌کشن. انگار باید خودمون رو برای یه قطع سراسری دیگه آماده کنیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/ircfspace/2426" target="_blank">📅 20:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2425">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tUeLDq6YEJBdn2QPUp4wNqfBmJdJf02t04NFBM7tA19apROQ8NUHCmMyPjjuOLbX0leO1xSrUiHMhen1Ai5WeutsstrGSnd6kUcjrEiH3vcfjl1BMSV5Dq3Rb9_4d6Cw2oOUlRUjyn7eeOkmPyPzfdZtEGwGhtj27ro6al9EOKCcz-vX5myDXQ2UGO1Gto0sI5HB1o3syXuXoMMQXyEsNYzQBY5oxMzIxmKFU7F9Qm2ol_1iQnawGxeSsKszfdmxvk1N33WgpF-2vzCNineWY3ccifKcAlNhCapYjYWZSGRcBeYZGUgLf82FEvEFHiT_6wXCmtjufFhUOlLg0S0WVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه
#نهان
یک راهکار متن‌باز مبتنی بر Workers کلودفلر هست، که امکان راه‌اندازی کانفیگ رایگان Vless و Trojan رو بدون نیاز به سرور مجازی فراهم می‌کنه. این اسکریپت از داشبورد مدیریتی، امکان پشتیبانی از چند کاربر، ربات تلگرام، قابلیت مخفی‌سازی ترافیک و قابلیت تغییر آیپی تمیز از داخل پنل برخورداره.
👉
github.com/itsyebekhe/nahan/blob/main/README_FA.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/ircfspace/2425" target="_blank">📅 08:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2424">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d4tv10eUFAyalS4Grnxv07lkpeFhZN3JCZqNtLZQ1or88eaTyVuMAKkamJT8u_GGrpC9KH58gOKPurMXFUVT5IfcURPowlx3RaqOVRCDGRs6FI2xO0HtO18-T6eAP47fBcQbM9tXamWbZfP-U2CiuQR9U3rInCm54P9PuAV8-V5fsMpCMgKgOqS4dT_UXANjuLGO6f0CuZ_ViOuqhYJp1AVxt7MJvguaX8dnYJHuM86plOoTjUCD-obI4GbCmzN7VvRBrdz5JTxNgYxCzmZ4BwLIdJK2rvw9YIHE6W21UsI9ZgpjaXbj_PU9YwuAVwGjYya7nk6nHDYoijooxuD9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه موضوع حادتر از دستکاری DNSها هستش و هر روز ابعاد جدیدی ازش کشف میشه، هرچند سرقت ترافیک تعبیر درستیه. همینقدر بگم که این مساله اصلا درایت/اراده‌ی زیرساخت برای کمک به کاربران یا چیزی مثل تحریم‌شکن نیست بلکه بخشی از پروژه‌ی وایت‌لیسته، با هدف قطع مجدد اینترنت در آینده‌.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/ircfspace/2424" target="_blank">📅 07:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2423">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h2v_sOxE-DTrXuzEMvNK8S4sDZgP-Fkt8yQ3shXF0HV_tuEkJFkuUusRJEpiKMYxk_JmjUbjxV-8jl0kmGXOwNWC6lmRcmCCiAfDRSzMuJY1rEkcNiJOrZzgpaxXSCXNXM_gOegIiVOZQ4n2VSNT_57uYigCyLz9y-2LoMcID4g0R9Yt14eGak-h2xWaNC7nghIYybj2YOiet-bYa8MbHEkxt7QQLNS3GMd97zfqCjE2EYAtlx2My2JM0SVttHRaKQ6oC84VHYB2QeBVZMyFbhZPfXrocM9zgOwSKbor0vz5k1-TKxu5hwGk6YXxVgpiDmjW0xtTmNSJt9Bh-xw_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GenyConnect یک کلاینت متن‌باز و رایگان برای شبکه‌های خصوصی و ارتباطات رمزنگاری‌شده هست، که با تمرکز بر کارایی، حفظ حریم خصوصی و مدیریت دقیق ترافیک شبکه طراحی شده و ضمن پشتیبانی از هسته ایکس‌ری، برای اندروید، ویندوز، لینوکس و مک در دسترسه.
👉
github.com/genyleap/GenyConnect/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/ircfspace/2423" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2422">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/duaLMHl-Q12os2y58TrDWlKEDxYJ2T1QSCeDv2MGOLHbyrTd3Bwz3iDo2imT9ssTCEBQ82Ik3uHW9nPy08q7gPB1RW7UuOtTaJwdv3gqOtS72hIFq77wRA0qmYaDBpGt_whj5CXcwC_WVbV7pemdNTz2ZhhvHxcWej6eW5z5gqn8pbc50UdlJ3adKVj7vMD9QYnCfNdK-0yeogNlUzEOx7heQg1pYtLMcQo2-CqGOgfg0fW4rVA3BkdNlLAQ9qGRQq8K_oZvTd5zbYwwo3p8flQ3dXPIGvYmANGGx6ZJ2cNT1EUzvSLCfl52IkcpSYVi6Mf1tbDBog2y9Ac19mNCEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه آیفون از فیلترشکن
#شیروخورشید
با نام AzadiTunnel در اپ‌استور منتشر شد.
👉
apps.apple.com/ca/app/azaditunnel/id6776486891
💡
github.com/polamgh/AzadiTunnel/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/ircfspace/2422" target="_blank">📅 18:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2421">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKRq9XQaUmwi4wxgC4QuMapykfnIQFuOYwVR6WR-zmsmLYtjMLWlleEagOE91r4DYTaygF3mTQchMrB5ynIuwewRHMKnQ4cOTTTUvn3FpGxg80hB-nYAGxI2XK2VQwylwyh8pTUc6rOxr2sox2fiFkAHM6Zwh5EjM1TBtQxKzXjRnmS8OgWia2JKDuHUf1ce4kLElJMDLQy45SRyuyMx6MSbO7cmmPUHPasmt_Kw8OW0TdGVPXihVWxCuh_o7EzFOiDulgsYAep18-39VR5fFJ8xrjHO_K2UvkuvBPB-bx3SB93ZeSpXhxvIzBBJqYeo57wV14wOxSoUFkOpIXASuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در آپدیت جدید از فیلترشکن
#دیفیکس
که برای اندروید، آیفون و ویندوز روی استورها در دسترسه، قابلیت Health Monitor به بخش ترجیحات اضافه شده. این قابلیت بصورت دوره‌ای وضعیت اتصال رو بررسی می‌کنه و اگر کانفیگ فعلی از دسترس خارج بشه یا کیفیت مناسبی نداشته باشه، برای اتصال به یک کانفیگ جدید تلاش می‌کنه.
اینطور که تیم توسعه‌ش گفتن این ویژگی از قبل در هسته برنامه وجود داشته، اما به‌دلیل اختلال‌های شدید و ناپایداری اینترنت در ایران، گاهی قطعی‌های موقت شبکه رو به اشتباه به‌عنوان خرابی کانفیگ تشخیص می‌داد و باعث میشد اتصال کاربران پس از مدت‌ها تلاش، مدام قطع و وصل بشه. الان استفاده ازش اختیاری شده و میشه فقط درصورت نیاز فعالش کرد.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5927
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2421" target="_blank">📅 23:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2420">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مرکز ملی فضای مجازی اعتراف کرده که "از منظر فنی، قطع یا محدودسازی دسترسی عمومی به اینترنت، به‌تنهایی مانع اجرای عملیات سایبری پیشرفته از سوی بازیگران دارای توان تخصصی، زیرساخت مستقل و سطح دسترسی بالا نمی‌شود. این دسته از بازیگران، با بهره‌گیری از مسیرهای ارتباطی اختصاصی، لینک‌های مستقل و زیرساخت‌های غیرمتعارف، قابلیت تداوم عملیات خود را حفظ می‌کنند".
این مرکز اضافه کرده "به‌عنوان نمونه، حملات مشاهده‌شده علیه برخی سامانه‌های بانکی نشان داد که محدودیت دسترسی عمومی، لزوماً به معنای انسداد کامل مسیرهای نفوذ به زیرساخت‌های حساس نیست. بر اساس بررسی‌های فنی و ارزیابی‌های عملیاتی انجام‌شده، تأکید می‌شود که اقدام قطع یا محدودسازی دسترسی عمومی به اینترنت در شکل اجرایی اخیر، تأثیر معناداری بر خنثی‌سازی حملات سایبری پیشرفته نداشته است".
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2420" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2419">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!
©
DigiHubAI
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2419" target="_blank">📅 22:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2418">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">محققان امنیت سایبری یک آسیب‌پذیری در Visual Studio Code کشف کرده‌اند که به مهاجمان امکان می‌دهد توکن احراز هویت گیت‌هاب (GitHub OAuth token) کاربران را به سرقت ببرند. تنها با کلیک روی یک لینک، مهاجم می‌تواند توکنی را بدزدد که دسترسی کامل به تمام مخازن کد کاربر، از جمله مخازن خصوصی، را فراهم می‌کند. این آسیب‌پذیری از طریق سوءاستفاده از مکانیزم انتقال پیام میان پنجره اصلی VS Code و نماهای وب عمل می‌کند و به مهاجم اجازه می‌دهد افزونه‌های مخرب نصب کرده و توکن OAuth ارسال‌شده به سرویس
GitHub.dev
را استخراج نماید.
این حمله همچنین از قابلیتی به نام «افزونه‌های محلی فضای کاری» در VS Code بهره می‌برد که نصب افزونه را بدون نمایش هیچ هشدار اعتماد اضافی ممکن می‌سازد و بدین ترتیب بررسی اعتماد ناشر را دور می‌زند. گفتنی است این آسیب‌پذیری در دوم ژوئن ۲۰۲۶ به گیت‌هاب گزارش شد و تنها یک ساعت پس از آن جزئیاتش به‌صورت عمومی منتشر گردید. مایکروسافت این آسیب‌پذیری را تأیید کرده و اعلام نموده در حال توسعه یک وصله امنیتی (fix) است، همچنین تصریح کرد که این مشکل نسخه دسکتاپ VS Code را تحت تأثیر قرار نمی‌دهد.
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2418" target="_blank">📅 22:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2417">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eaW-UNc252_1Jw9_i0QehOdmYUWE-vhKxaKQGQ5PjwYNes-KhRuZtwnhqhZx8bvJLs-OhB5ReLoEv5gXVUcq0AjRftcA6E8swuoPddEK-9GC33T76lBVOVHXau6F_9ewbMOriVKXeJctxCyf3KuT8ouFN_cmJ7ZFq6urOtROjSrpRfrAKDHzbtxisjyqTxQK1-gczgtBSP9bg5ZU9lmUGmZHpfZlktjzGLIoYNc0yskWw67ApKw0E-J6-7b8SLE20sWjzCo7CWSxf6X6FPYO9SWA-9_sPQJEh5W7vaaN9OXu1qNPRWD8NBioBUYKp8ch1OcYEV59fxWsaj0NHLz3UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر RKh CFS یک ابزار رایگان و متن‌باز برای پیدا کردن آیپی‌های تمیز کلودفلر هست، که از IP تکی و CIDR پشتیبانی می‌کنه و در نهایت نتایج رو بصورت رتبه‌بندی‌شده برمیگردونه.
👉
github.com/rezakhosh78/RKh-CF-Scanner/releases/tag/v0.1.4
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/ircfspace/2417" target="_blank">📅 08:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2416">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صرافی‌های دیجیتال نوبیتکس، بیت‌پین، رمزینکس و والکس به دلیل دور زدن تحریم‌ها و انتقال ثروت به خارج از کشور، توسط وزارت خزانه‌داری آمریکا در فهرست تحریم‌ها قرار گرفتند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2416" target="_blank">📅 08:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2415">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بامداد امروز سیگنال تمام اپراتورهای تلفن همراه و همچنین تمام سرویس‌دهندگان اینترنت خانگی بصورت همزمان در شیراز و چند شهر دیگر استان فارس، همچنین شهرهای خط ساحلی جنوب کشور در حدود ساعت ۲ صبح به مدت تقریباً ۲۰ دقیقه “کاملاً قطع” شد. به عبارت دیگر هیچ دستگاه تلفن همراهی آنتن نداشت، هیچ وای‌فایی متصل نبود و هیچ امکانی برای ارتباط حتی با شماره‌های اضطراری میسر نبود.
قطع برنامه‌ریزی شده جهت یک اقدام امنیتی، تست زیرساخت، حمله گسترده سایبری یا مسائل مرتبط به جنگ الکترونیک؛ مشخص نیست در آن ۲۰ دقیقه چه رخ داد!
©
iliahashemicom
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/ircfspace/2415" target="_blank">📅 08:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2414">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ClACKsQ55Jh0zudkBzDO79kvm6DKUCk3qQHqYWuxWSZCbAdrPySzlI1Rmbez8PwH2k8w4xo5aSdnto2LPf0_4uTJ8pvWYRCM_YqrP3mLPUKaylJDFnCrjWVHEK4KXBNjEEN2oChTYchRfY2dltFHvNCb9IOPV648S1fV105bcNDtB2Ja_op9vEaU9CcjbjPBGKzfYPOKqSY4w_cmlzdAq-ga0c6NKUehY4ddkss8pcpIEdcoy7oTkIbpH4p8NkV5Z39MSdesT_r86isy_ImIpim3j7LINqOvtRbYY9Cdr097gskMYkJ-8T-Tn8KISt399jh1pst_ClMwrvG7SjXqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در نسخه ۳ از اپ متن‌باز و رایگان OnionHop که برای ویندوز، لینوکس و مک منتشر شده، موتور اتصال برنامه کاملاً بازنویسی شده و با قابلیت Smart Connect می‌تونه بصورت هوشمند بهترین روش اتصال رو با توجه به شرایط شبکه و میزان فیلترینگ انتخاب کنه.
این فیلترشکن از روش‌های مختلف دور زدن سانسور مثل Obfs4، Snowflake، WebTunnel، Conjure، Meek و DNSTT پشتیبانی می‌کنه و یه اسکنر داخلی هم داره که میتونه Bridgeهای سالم و قابل دسترس رو پیدا کنه.
👉
github.com/center2055/OnionHop/releases
💡
t.me/PersianGithubMirror/5793
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2414" target="_blank">📅 08:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2413">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xy3XmPHmj5I5vdPHh8ms15nlDBRubDXyHgVZ_afmJHcQuA6QEYMgss45JxLmMXFdnX4YLcaRtnmMCBXKKcwqtsikzJTcBul-0xLlyiGDFSmgDDOpmuanYLBSBwJ26MC7wxPGxtriWel00K3B1QGwvApRYYOvyiLqBatAsB2DwFfNKXTcXFGjiETRpjiVvUjqo7cgDBIIcAF7vo4pYJyM8SjkHQ7AqsPzldOV5_OBUcwor4A4IsQaxXaShs-jmDXcw-2BsFsEBSmr0W3mO3PY9MMNAR5Cgfy5OYt6Yn-x-DvIcJKK2W-PXdx_FB91jcs1GRW91B7zs8p-SSBB-lreaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظرسنجی جاب‌ویژن درباره تاثیر جنگ (و البته بحران قطع سراسری اینترنت) بر کارجویان نشون میده ۵۲ درصد از پاسخ‌دهندگان اعلام کردن که شغل خودشون رو از دست دادن و حالا به‌ دنبال یافتن فرصت شغلی جدید هستن. این آمار همچنین میگه نیمی از اونها برای تامین هزینه‌های ضروری با مشکل جدی مواجهن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2413" target="_blank">📅 07:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بر اساس گزارش‌های دریافتی، اینترنت بین‌الملل در برخی دیتاسنترهای کشور مجدداً برقرار شده است.
با این حال همزمان محدودیت روی بسیاری از تانل‌ها و پروتکل‌های ارتباطی ادامه دارد و بخش قابل توجهی از این روش‌ها از دسترس خارج شده یا با اختلال و ناپایداری شدید مواجه شده‌اند. ارتباط از خارج به داخل کشور نیز همچنان با اختلال همراه است و بسیاری از سرویس‌ها و مسیرهای وابسته هنوز به‌طور کامل در دسترس قرار نگرفته‌اند.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2412" target="_blank">📅 07:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2411">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/ircfspace/2411" target="_blank">📅 07:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2410">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وضعیت قطع اینترنت طوری شده که همدستان فیلترچی که روزی روزگاری با هم عکس یادگاری میگرفتن هم به شکایت رسیدن.
یک سیستم فاسد همیشه به سمت فساد بیشتر میل میکنه؛ در ادبیات فنی بهش میگن فیدبک مثبت. یعنی سیستم هی فساد خودش رو تشدید میکنه و در این مسیر بیشتر و بیشتر از آگاهی تهی میشه.
©
vahidfarid
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/ircfspace/2410" target="_blank">📅 19:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2409">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rFEyPanp7ymVezP6iytgsGMEBnfVj1kRJZ0AlKa4xPOD1geQ_adcy75fz0a6paUIljN2bspIfo8YNa2dJoSrU7MbrsN4Wg0EISPC5oRCqCyiZG9h1VkyAZIo2imWxOg1yuOvaShNP9VPOAmXuU8fOtg3x2iAkMFLxMb-00svB-lV0gUsldlFhnjUf0JjqQ7Qz24Gd4CTNLVK_0fRIOUmkn2aIe3SQpxsavABeySYALy6GDE4JxC33U7JjT7fSC9Ouf9F8r3B0uW6zQXzebHzP8ZND8xuUJp6muZ5BEMtG3LIvuGMKCnCplT2WQNgA_USRGz3fZBhrLKe82qgM2Z-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح اسکندری، عضو مؤسس و عضو شورای مرکزی شریان، در خبرگزاری فارس کمپینی با عنوان «گزینه قطع داوطلبانه دسترسی به اینترنت بین‌الملل را فعال کنید» راه‌اندازی کرده است. این کمپین طی پنج روز گذشته تنها حدود ۳۴۰ حامی جذب کرده است.
در حالی که میلیون‌ها ایرانی برای کار، آموزش و ارتباطات به اینترنت جهانی وابسته‌اند، ترویج ایده قطع اینترنت بین‌الملل بیشتر از آنکه همسو با نیاز مردم باشد، نشان‌دهنده فاصله طراحان چنین طرح‌هایی با واقعیت زندگی شهروندان است.
©
alirezaer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/ircfspace/2409" target="_blank">📅 19:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2408">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RUskOLqhnXxiav-dRsGUaOxzsIFtZ8UlP9OsREfuI9z92YUU6ESfXygIDk0IdgwCKYl8pq4K60mS0X6eK1psesAvZ7X0MpyNXM0vhLENCuHzdG_IvguiRU8aSFkvkjQXY5Ip31U2CC0Q3VKIAsTTwHgJn6Agjrz53DWQvGlluCqiCd2MBIiah4LVvWqM9cqY-A3QHLkVn7LUXR0HFQquikVl1auN3wa4SgOkpH4lodqlqhL4MfNB-VyVDD3BkqhJqGyAVFRbtbVLFHS6wTN2-G2aG2rtrC_QFoRUwIMv0jR9_zncHeju8uqPyNDsKaYxanY6qApAwUCL-u8Clidw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SenPai Scanner یک ابزار متن‌باز برای پیدا کردن IPهای مناسب کلودفلر در ویندوز، لینوکس و مک هست، که با تست عمیق از بین هزاران آیپی مربوط به محدوده‌های رسمی، اون‌هایی رو پیدا می‌کنه که هم پایدارتر هستن و هم کمترین تأخیر و مشکل ارتباطی رو دارن؛ تا بشه در کانفیگ‌های واقعی ازشون استفاده کرد.
👉
github.com/MatinSenPai/SenPaiScanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2408" target="_blank">📅 12:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2407">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IhvB98Ed88N4HZF8l81IjK3NVUiXL5C3A27svGj7ivY9vjteIYAanugfe2ewxwzywIrUkA4xIlHIZhKAb90OpK8xttrWw6BePgsRaPdE2IsAKGsoIG7DTp8Ra0PjEFjRjhR5jPkzSyUjJNnfP-O2zH7qLff9CUqRWFL7_HTYbV9YtY8KEwkms-xzVYNQTJ-vOWw76oPgmXi-Tj7jPtUWkFojTAZMutWNzbdHewuYipKU5RV5qvxfGoZ9QupMRpcSlQUO79vNEVI3cq1UOU6q9XfGP6l2D7o6JfeMkNq8tcc7pRLk_skPlAfCfUrQPvLuFEJSiX4sMgmH7NQtjQ_JVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ SpoofGUI یک نسخه گرافیکی برای SNI-Spoofing در ویندوز هست، که از هسته‌های Xray و Sing-box برای مدیریت ترافیک خروجی استفاده می‌کنه. این ابزار در اصل برای اجرای یک مکانیزم محلی SNI Spoofing طراحی شده که به کمک اون می‌تونه مسیر ارتباطی بعضی از درخواست‌هارو به شکل کنترل‌شده دستکاری کنه.
در این برنامه کاربر می‌تونه فرآیند SNI Spoofing رو فعال یا متوقف کنه و وضعیت اتصال‌هارو به صورت زنده ببینه. همچنین امکان مدیریت چندین پروفایل مختلف برای Spoofing وجود داره، که در هرکدوم میشه تنظیماتی مثل آدرس و پورت اتصال، IP مقصد و حتی SNI جعلی رو تعریف کرد و در نهایت بین اون‌ها سوییچ کرد.
👉
github.com/ZethRise/SpoofGUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2407" target="_blank">📅 12:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2406">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UXWaihgX-Z5dEDhza-d84xQrRiU3i_pAawU5IjFwQrxA0Wi4PFginpIdCfzX87w8iQ6Q1oY33B7OdJwRrQqxv36_rBNIVlttIgRcb9meWb_rK-Q_LAhHgizSWHDlYXKGbASN23eX4WZEmLEmWwOnuCIG82ZMl3CNB-B-8hyGNOMvykU60cAKExslSxlHMgvzzzGFK757jkvHFRKGifavmq6u2vuH3ZnXWBBCr4DHm76moXdUGNDwFIUBgcV0UgGjC6ys9l3AJGRqRgwFXOuZMTLmLHKQd5sdBIkgUP32H05NgItsxMYbzVYgZPGt6jXiZu5-T3Y6svgdZcI7lh14yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر CrimsonCF یک وب‌اپ برای اسکن سریع IPهای کلودفلر هست، که آیپی‌هارو با L4 TCP Handshake روی لوکال تست می‌کنه و خروجی‌های آماده برای Xray, sing-box, Clash میسازه ...
👉
github.com/amir0zx/CrimsonCF/blob/main/README.fa.md
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/ircfspace/2406" target="_blank">📅 12:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2405">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pvNgpy0qkIRPoUYeLn60NzowacUT9W0Nvc72gfWehxlSqHhqmGyVSa5Q54RK-4KQyCJDebxoViBPrmZw8z7X50ODgiPYI2wCIol-MBD7Xotw1AVIcSGzHf092sereJDMPSCVMcqJStWDG9jkpVZv1kVjMwWROjfyYx2Zi1_iEVTEGld3lPMuI0JqG53OjRqG5UDq3_WzBASd8RY6zMwR61WmbI8a8vVFLUDdaOLj6xvwya6N1v_9lRhMVret8hqxqSIMxsuwoRjJTJ1S_9YIRGLoU9-eewworNw8_pnUJbgrBbJnRiLlxOmAwjbFLdQGVbehPXntyehOupI8tsYcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتماد به نفس اگه اپلیکیشن بود
©
mansheyeh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2405" target="_blank">📅 10:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2404">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینترنت صرفا برای توقف روزشمار نت‌بلاکس وصل شده، یا هدفتون برقراری ارتباط بوده؟
چون با هرکی صحبت می‌کنم تقریبا ارتباط پایدار نداره ...
©
ArashNalchegar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/ircfspace/2404" target="_blank">📅 19:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2403">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت. انگار که درب ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشیتون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.
©
nimaclick
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2403" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2402">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تقریبا اکثر IPهای خارجی خاکستری هستند، یعنی در هر کانکشن شما مجاز هستید حداکثر ۶ پکت به سمت سرور خارجی بفرستید؛ این محدودیت به شدت سختگیرانه است و تقریبا هیچ سرویسی نمیتواند با این محدودیت کار کند. به طور مثال برای کانکشن‌های Https صرفا میتوان یک ریسپانس ساده Http را دریافت کرد و  شما حتی نمی‌توانید درخواست دیگری بفرستید.
برای بعضی از IPهای خارجی خاکستری مثل IPهای CDNها و ...، SNIهای محدودی سفید شده، یعنی اگر شما یک درخواست TLS با یک SNI سفید به یک IP خاکستری ارسال کنید، آن کانکشن سفید میشود و می‌توانید به صورت نامحدود پکت ارسال کنید! به طور مثال با اینکه الان تمام IPهای کلودفلر خاکستری هستند، ولی اگر شما یک درخواست با SNI سفیدی مثل
www.speedtest.net
ارسال کنید، کانکشن سفید شده و محدودیت ۶ پکت برداشته میشود.
در حال حاضر SNIهای سفید به صورت وایت‌لیست بسیار محدود هستند. با وجود میلیون‌ها وبسایت میتوان گفت عملا اینترنت همچنان قطع است و صرفا دسترسی به سرویسهای خاصی امکان پذیر است. حکومت برای بهبود کیفیت اینترنت مجبور است بسیاری از دامنه‌ها را بدون بررسی دقیق به لیست وایت‌لیست اضافه کند؛ به طور مثال الان تمام دامنه‌هایی که در لیست نیم‌بها ثبت شده‌اند همگی سفید هستند. نکته‌ی قابل تامل این است که اکثر این دامنه‌ها را فیلترشکن فروشها ثبت کرده‌اند (زیرا قبلا شما می‌توانستید صرفا با بالا آوردن یک وبسایت فیک و ثبت درخواست، دامنه خود را در لیست نیم‌بها ثبت کنید). بنابراین فیلترشکن فروش هایی که دامنه‌شان را در لیست نیم‌بها ثبت کرده‌اند حالا دارند سود خوبی به جیب می‌زنند.
این سیاست‌های بستن و وایت‌لیست کردن اینترنت موجب رانت و فساد زیادی شده و شک نکنید که خشم خدا را در بر خواهد داشت.
تکنیک SNI Spoofing باعث میشود که یک SNI فیک توسط فایروال دیده شود و کانکشن سفید شود و محدودیت ۶ پکت ارسال برداشته شود. روش اولی که منتشر شد اکنون در بسیاری از نت‌ها بسته شده (یعنی فایروال SNI اصلی را می‌بیند)، ولی طبق گزارشات همچنان بر روی ایرانسل و بسیاری از مناطق حاشیه‌ای برقرار است. روش دیگری که آن را Plan B نامیده‌ام، دیروز (با تشکر از دوستانی که نکات فنی خوبی را متذکر شدند و باعث جرقه ایده جدید شدند) با موفقیت تست شد، ولی به ۳ دلیل فعلا قصد انتشار ندارم؛ اول اینکه بسیاری از فیلترشکن‌های رایگان اکنون وصل میشوند (به طور مثال سایفون به راحتی با فستلی وصل میشود)، دوم اینکه همانطور که گفتم روش اول همچنان بر روی ایرانسل و بسیاری از مناطق فعال است، و سوم اینکه بسیاری از سرویس‌ها مثل اینستاگرام، واتس‌اپ، یوتیوب و ... به طور مستقیم با MITM در دسترس هستند.
©
patterniha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2402" target="_blank">📅 19:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2401">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اینترنت در یکی از بحرانی‌ترین وضعیت‌های خود قرار دارد!
اکنون وضعیت اینترنت در کشور به یکی از عجیب‌ترین و ناپایدارترین حالت‌های خود رسیده است. در حالی که بخشی از اینترنت بین‌الملل برای کاربران خانگی و شخصی برقرار شده، اینترنت دیتاسنترها که بخش اصلی زیرساخت کشور و میزبان بسیاری از سرویس‌ها هستند همچنان با اختلال و قطعی گسترده مواجه است. همزمان بسیاری از VPNها از کار افتاده‌اند و شرایط اتصال نسبت به زمانی که اینترنت کاملاً ملی شده بود، برای بخش زیادی از کاربران حتی دشوارتر و بی‌ثبات‌تر شده است.
کاهش شدید پهنای باند و افت محسوس کیفیت اتصال باعث شده دسترسی به سرویس‌های خارجی و حتی داخلی با اختلال و کندی همراه باشد. از سوی دیگر، گزارش‌هایی از بروز مشکل در گواهی SSL برخی سایت‌های مهم و حتی سرویس‌های دولتی منتشر شده؛ موضوعی که می‌تواند امنیت اطلاعات کاربران را تحت تأثیر قرار دهد. همان‌طور که قطع اینترنت فوری انجام شد، وصل شدن آن هم می‌تواند فوری باشد؛ اما فعلاً روند بازگشت به‌شکل قطره‌چکانی پیش می‌رود و همچنان بخش زیادی از کاربران و سرویس‌ها درگیر محدودیت‌ها هستند.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/ircfspace/2401" target="_blank">📅 19:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2400">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">توی یک لحظه دسترسی مردم رو قطع میکنن، بعد میخوان به همون فیلترنت سابق برگردونن میگن این روند تدریجیه!
مشت‌مشت خاک بر سرتون.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2400" target="_blank">📅 15:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2399">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nuyu9rGSOFo4tUnfB-_0tOHYxDQAAZy250LTL8U3EL99LvHNpTM0TZeNBMPlyGVgYQdO2KXv0o0rI6-Rkkwn3rQ2IW9Etav3uxKBxhuly0RO-QydgSz8MV7U2QYK0evXc2HD1DGfFHGeQ-wKi_DB_gujYXcnsiVRH5Cbwyb5-dn-j53AfY6yPocUtY4CaNGK3kv8Zmb0J3IxWbddyMaC7Gi66PjSJxtR207iagNfGtadfXO-2d3P7YasTYxMtni5fhnoj6PkqicgDjW2hp2-6olTcu4pa4ekMypYcnW1dVCA2Qs08CJYIYbx3hyVoUd3_DkGdoog71bwoFh26Gqq5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جدیدترین بروزرسانی از فیلترشکن رایگان و متن‌باز
#دیفیکس
فرایند دریافت کانفیگ از API بهبود داده شده، متد CDN Fronting رو به‌همراه اسکنر داخلی به بخش روش‌های اتصال اضطراری در قسمت ترجیحات اضافه کردن و همچنین روی بهبود عملکرد، افزایش پایداری و رفع چندین مشکل گزارش‌شده در نسخه‌های اندروید، آیفون و ویندوز تمرکز داشتن.
👉
defyxvpn.com/download
💡
t.me/PersianGithubMirror/5676
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/ircfspace/2399" target="_blank">📅 10:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2398">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vl9JJHGLN_2vPIXK1GgvlcqUCNUI0YbzAAOvQLLFMUcJ-cdJ4E5BgVgnur1a1Bp3fG6Olo2YHTfMyiCpuTs5zaE6MqlSk3iGCjFvFYDMFrn8ALxe9X17WC8TcdYQPrIyHoniKlqxvQuQlvfYcuSSEfEyUa6H__PXdnEsjl3xa9CFHdouIQMekyjrWCHFraXDUkGbvi4sLKhdWE3uGyEGt8jhIIJ5yUmR1F4EFaoQc3AYk1m4UkqO-vf4qVOhwmR47iiirb-P_6Bzd8fJVFnFzIuGpBrgNQfRQ48jD0T-APC_yR_N-u5oqilY0yDeQwXVJ9FpVu4kyRpc9cJWtb5HGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بروزرسانی جدید از کلاینت NexaTunnel امکان پشتیبانی از کانفیگ‌‌های Xray در کنار Stormdns, SSH over VPN, WhiteDNS برای iOS فراهم شده.
👉
apps.apple.com/us/app/nexatunnel/id6766783641
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2398" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2397">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئیس کمیسیون تحول، نوآوری و بهره‌وری اتاق بازرگانی تهران گفت: خسارتی که کسب و کار‌ها و به‌ویژه فعالان حوزه اقتصاد دیجیتال در این مدت متحمل شدند، اصلا قابل جبران نیست. /ایلنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2397" target="_blank">📅 19:45 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
