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
<img src="https://cdn1.telesco.pe/file/oue_kPyb2XmrE1Q_UEuRv0Pct9B82TOgZIcyNZ-KuKWjcHlRMfgvRtTh3k1E53duG_4YRzv9JINuNWyzbd_ILOnlOtjOiEMPy_QjzcFWfDtwQ5Q5BKPozYI7zwPa5SVDAUgc_WskURhJTmwsuabeVzGS1G5WdPN3SbpjJWjt9Bo68RNLSe9aDumOACUUyy0MoZ4T12hK7dj5VTbmVflcXwxNmtly8lAGRzIDPIRZSvEPxKsVlt3YZgaQW_HZkm6mNkaW8xtp8SwR32l51ZYgtcFftFZBtzns3t-J6WavFy2xcjeDMDyKhNW576a3GEp6eEyiky2MJTKG8LGtdAXNEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 03:18:30</div>
<hr>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pM00-heOl2Z_GVgXPGusXRrYWSdvPG-DKUz4wvYpkCjbKBPtU9HLCxbLPiXZdo3ZphBCHXvArMZEwrlY113q0kJ3d5DdLcenS6hPPbxZpk0HugtBXD3pDluPqWEcANcPGeLjdTKJD9cpaMycPlTx7e-U9JIhKrj4NK_yNPxjSl68am5wTdTJe7JI14AzUsNGVNqc6ZqIUoKh24MX2OrUESa_Ra32R0eM6T8PoJKhrVcO-UkOzJgO3XMAXTBssobjxKWumckFIUPFtMN1r-Ixbgy7hxevYRBM4YefUwROwTRebQM7X--axI_ZoigAzjqK1N5SFrmtOzDTNh6t6zBddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYJxiSkGge8iOwc_1vyJvvg750-rCMOpd6e4FelOncTRPLFH3Bo0WYlzZ7zm3N4aR7u_lXmQnxtauzwWSknD0KmZvehyCUXfwjRC37_eLs8nKcduXB_GlIfA5yFQA64j3xCQS5giSdqXNPop66c5VabgInRIKEu2IJ6jT39zxcnI-_5rqEkLdhkQ-Xmli0y7tNPB_cavf0em7mhOpv7UE_tqpVMmbt6cGmxqh9XbMd05JBK86ETQSqF9EcDoQnNul5h_H68pOPK4ayq6v_Ug3WGrAXj9eGXgD48zElSfxd2c7l2lGdiTXZBktDwVfUNu1R8nPjFbtJVhLVQDGsTNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0IW-ZyjtCFSfU3NxGgYF9dm_Ps8oA48aReXRj0VSHkEUNZ_jJtIeH8alm9dOx-bnKFoQuOVI4PbPlSFrxt8AmjFahxERpc4A37QImKY9OiVa5MKNubWFIw19Quy-nau4iB-bZVDSJc5-pxChR-pZqBtjm4lPq9ymnOsozfOA2bNr7zI1YxEUCmUCil7V6FtFhjd_PHamDJ9xm8BJcB4xTqpBWAvNl37xPBHaT1w8suM35o_BPTq7ETw2NpSNSGWS7CRg_GpCHQDH2bamm2XZwE2Q8OgbAeLHOEM6rwFp6LpHTHc-elh69C0CLQao93Cjdzl2ZrIg-y_cKtUHd1Sag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GcuIOY7V8LGEuUC8FUQGA4i5TUzFPlAKf5vtQdDgWRmKqjNpSAWyCHJcJMX6HJbp2EZvlDv9Z9FKTuEkj9cvunHmo9B9PWMloxO40MF-KKB0BnlByWN649byHaeg9VbAxQU-Y_E3bNeGy8d7Su8xLS11k5437FVNbQ3i0nW7x8bOWxrNCS_n1HpD9Xuikue9iDyqDnKwXQd7zQHqJXEgXnqvwoQlizt3sztyF5kqHFVv15rneqJwZ_RVqKheVqNdkdBQqhL2glwys7L48LEDfx6JVIoelAJebmXYZ6b1gDz28RFQYrx2_5daLdGFu24yCCXZhYhhE0aX__0zngVV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQueWsTU0EGXbDDY7sRA0OMd9RwFTjW-z3q3zFMBbbxdRa4QLRTyEeeuLLKo6Wm38vzwkEcOE0RsNVdEDCM7ImHJNiwwGV93CxGOYadzpnA9qL7RBqGnmmGJ0pGa9NJASj-SIsgiLwZrSrMJhmweRY8AyMJDt0gYA5YqVs9SELBlzQrcUlHXQO3pFwsay8N2A8a_fX5uJ-FXgqvOo8KRzMkWMe1MVBgPKY3jXz8Sng8Ck5JVlfBhpVFppDT2VKZI04zDlbFBeGnmM3-LN_IscqSYe5dUqSq58lVwy3GTl-gdWpHd9sTJUBKkiNJZjZv_GdyznRzj1rlAWWDfX7d0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYlP_EZHoB20tu7THPCKVAw6GfzIsITph8KJhauVD39yrtoXU44MDpGq5lXAFfMhv7KPTy2f4zoLR5MknhCqzzIVQ5tcz1EZ0nvuqpz9TfdIgOrqVZ7IpVUcpKxiVVw6gM69-VOzRL1X-wirrpuPjylua-nzNIsd9EWG3y2XO8lHCFYaCvKwD5TJCit-hdtyZkocooBHyo_Q65rAt4-VM9QPos4GVFRzOXS2W0DZqvTALjlj6j-8gBh2Wk2_3CFwyyTtvSbPIsIy94O3Qvy4iK_JHc86SPPrwbSjxQWTUeg5VzrcaEcd1_GS4ZZ7dIrZTJEIfkLJMVMX6NcDfb1YAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODf8mkIWHdJelJr-cd6AoFcZwX4p0WQb1OFGcvOfjpw3PXsKfGBacpJ7pE3bIlJifMUN0prmOd9zz01Ifl23XGE_j-n-p5p8NzH6CQZnnIRB26VuPfsg-WiXKjpHY5nPtUh-W6WB6rL3P0Z82UBQoQM4m9aL0yw7SdQ9n7QiT5D1Zzp8jZlJPTZOvpojeUHCglBQX6xJIyAmoqgi65M023W7PbUYkfJZqP9JiqIyVfplTSzLvIE2wqlR_XVLbeSElQuDqDf8F1C0LPaTL2hoOKidVlwK7iLpEdbOxxhLDOFJKxwiaPQI2L4DQxDBGS_9CO8BP2UXc6uvoNDaY-Quhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oBnAef97OFQLqO51vVRAsb9d0a1xAp84c_WtztovMaA6lw2E62jy6w01SGjbAXjnJyDCpxhHfO0DT-ZHrrerq_QdFXrxFwhOxlaVX-JPKepj3XlTSYJn9kfSmdOjAyogNnyIUJK-hDMIgI08gaXbF-lHFVxrY1IvCSAQ7plLIXXSo-sqiJ29rISvAqcv0VhHJlAEGbWEb2Z2xEGvYvj7l9l3ZjZAfdUrDrbCrtnQrYf77HhTAoc4mDUAKrkviMYhAy4laHJ227gTAKVNnuvL_r8tA4gxZdcR_Vt6gCxFwINk20POoEPDLvPllHlL4Qf3LyUAZqgJcqKPykvpygTUNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vJVkBlubI0SelcRR9lDE-CYsoThkA_qBSNn5CXYKFvWEMCHUfdkDK-L_Y6cN5bo4wZ2F4D_o5Rzxq6O-a-1LYpQlMuUmS8QSBWrp23SbETatXkyjd3bTd6qVoh-WR6RBMGBUHZM4PCNTFzGJLHwVxDDpJKN-bfXwCnSfeW7_0Z7jpP87-vMfwYhXRUqnqNfa4xHNFxcc5xDiuWnyFVyZlBEG2tulcsZl0AskB8_nEsYO0plXFoMwmxtYZN51kglHe0vzbtOzXVCpiiBxdFKDhAF-TxI2ucEpAbu0IEbB0E8JKjc3f1DSwTr3uY4hHYQ8u78WbA4SB4h0jytDoFug7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/swS7MPivQZkK8jV3lzeSBk_Bmh7SGuZoHGNrKL44mEXisSdBxrxaTGilUoJ0R4l7nYf-c6gS50rkf2rqA35ugaMUxhwus4W_AMdELqOl0RB6xWWAdHaxnSqQ9ADhElLM5dojnXIFCRpyaUBvWeJCwBt55RNIVtKcVICaDbZx_7J44fwxZ63Wr6snzCmwhJ-G0WnBxqm6m227pEyrCXDML9JDojY1dK6P78ZmjgN-3LjjGFoTYgL8SU22T9Pca5i8wzH0mR1QhC6Yrz5Wy8Mf9TX6kKGngpy5FPQpJ9oN0cgIQ46iBCtvPNcl-_OWt4hjME_eMbaUJnvisQvzvvrHHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oqH52yIGEXU0xeuzNIotvJmW-2SBFtfIo2jCmXUUkU4HNop9x2wDGhoZJlPbqHilCAwlwYKbycB7dsac704dEqlRlac6zN6yvhQLEBC0Q7E4EoxH_KugPXSJT4ZbtDVVH52FyVkEknOcfNJa9X7gr0pNiaskIyOFe8-Vk5gdIc3GO1W6iSgeon_4HXb9VwBfAkkFtKnbZEEkUyKr8FUcPiGREZJ7MAyH81ukY_p2kB4X74R4ecEMoBtbe1wfeR6cp4xZWI02eigYJ6vqdRmWKHcL7r922r9qQN3mn0u2KoQepYAQLKzToJGYwHskTNylDmPIJ4WiD5hyQune7JNGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GtFWLG3m7M2Fg50XeSjSsoymZqtdArCPsk7aVTZxwYruNgUkGjFfaf90c3659OBwZvnNmEbsPEMzdUKEnpHxgA8c2NU8MDk-lqt8vcGpTLAoWxQUKGLyBa8Py14CuzWTHj7QFHC8IfA25CKehJ9fJMuRMHIIWmWzO-I3nLKxpA-PbDUU0D_wrm4hrNntQJUQh8CIQjCVJ1RSSwJsMrNb8TVNQUrvnzS01j_JT2HFmFCA6-FTEJHcrp8ufH1Kk4xoz6PR-ybYHS0WzjhCX72A_XXaKGFJt25A0CgsmAs7wGGPILG2P8qINAkWb8BzH-nrvKi61zqvULYnQU27zTciiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rsm6reUIWb2zEmsM_J2UF0h8d8saHXbR8mrJEJkLLsTMORvPG_1PCgL85RFdrpPl5rJ9my414hnlUl2C5WjK0EiHBU8jCd5JJRaEqEmkJFbyFmthD4ilOOWkMi4GAuRhet1AboCSaK53uv5GLhXvAhcXdaFFf3O-goMSJrH5IDEXHOvX--LgcxF90fxl_0RTr8xq1eOLpZa1A3U-wuv_yGV8b1pWDuAjI6dgJk0pcomEle2im5Mzo6Wxn2mfVfof5R8KamRtqhKbbw4b6Y-PXKJiqUEB0B_AYwdBDVX0teZeHOD0_Xb-vFoIkjhJBX0MRd2lRl-mVRVnhN-idw-9pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ncHSOtMMWudUiI8ljQEiHEDi90ERDna2f-PGw3TQjBT8fVZTz4mWt3EMz45e2g0kG76ldgQ86ILTubR3ikTu15ocIZO8KqCcfuvweyq5jRM8egENHDzup1UiIQIVkpGL0S5sfTDNnKLDy59j16wgXgll1XEFYk4wPnk-FmmP5-D9b8Hxliif20IJeiMWRkBv-5Gt21LwhfZm0E2EbNjcg2hjI7wmbuq7oiU9-aEIJ5BPhM0k53hW85kHZh4lP7A2NOFhE2L22oOQbBzTcL9CcqDSHezZlHIDYyK8ICJ7W-iMr9UETmHAxkRC-u2Tu_6xZFw_Ms5rL9VlNh3DwHPT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihfZ1_KlgPV-UQZWbhyVndpydbFvzSpoyXS28rGEgaawlcGpDRh5XUTvpaxY4Zsyx4C4ZFHfI75cqm654nVBXz_ALHy6ELOT1W75up01RqN8UlERY3fE-wM_ICYODhFZt6u_LgYWd2k8vDx-6Aewyct44KWWKBXYumBL1jaJKGthig8D3Wy1VbgBL-71vJXsrxG0VzKtMH0iM5sca_i4O33lHmWCmfH4Lynwhwu18lRlktRaGiKjXR7cD3c9gtq7fWvjJhF6AoDqLPOVL8q2yp8EKn06ghsLqumNyzVoTwYQLknG3_KCwI2tcIziORz6vKw1uVSY-yTrF2S9syLKuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LRduCLiaakZJqeBiCBxA9GIIGVAGMnbkukPo9JZuqskK0MXGgk8ONt_6QTeNaP-yBDZZ_zT0awKwGgyPOq95zkR0rT3V2BFO97UiJtN7ktpKwnfJkZO5Ib-Q7yDpJw9DyehVbVYZoOWnmg-RRgMv5Mpr4V5jbWyu4XprIpdzysEmdhuU4ko5APkBWSHXEOUbCGBHYEZY4Nj4A6qezHdd1XBIKKTlq_RIKHwbdaL4UKMezDeD7DSGI41qtFUKwQx_Hk1q7esq61ftkkO2-0eE9Z2XLXZ8x89cHf_wdoOE4URdfZjXZ2J6R4QrVX7R7qqTIMN9NeaG36WvnVaI9gFP7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qG4dFD11WUmGINoyH7q4S-O1XLYctrssD_ktc4Myd164Zw_DZ0rdub7CYQhutAq5te9T1U3yOscOT9kYm3ox95GrYEveFC6_bbLyVzdCH6B_AO9GFtC98tS5n58dZWa9-HHyvH0kFOfd_cQSJkGK-N6GU0lcRbyunzUotm6twYn8iD3uQUycEyF1sfSNlT8w-TwBNBrmXjXKaA5_tCAZ7J-UTqfbBQaxY71gxcibeaPupFHzK0pkiu-0jKKwpGtGYrlY4Ck7ihm8Cf8lXLO7AX3UnmlDQ92s1gxkILLoi2jAWX5lW-5v3qlFuP8xI9XJus0kgZ3INTwUZtbTdRtg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NOJZRfgXm5UyiobjKPW9uKht-GmGTpRSH1VK-ZKnPWERjImtvEZ-KrQh1mVogGNNO_8REjE7rUSHCvyM3NWB0VR3UDkGQ1GO3eS7NIv2UciRojV1t4tsWja2BdE0112guFqMG0aETQsL8O_tBF7RE2AQu5Ld-4nW4BnQTeyJMR2l1gUlAl_LtrilLHaN-_7Cn89BG5V5ffRdOkhZ0e3wVX0ckRMiwfAkGeYFfiDqz-bk3l74ckm0nsK9r5kQX7b5W2-RvouqPew5kPrCQjM3g_h0AylSgf3hgFsClpEcBH9ftPHi8LQMh8wgli4FDQbjVsrjMjDZdG5X3zxbgZbdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TN3fU-lc1rXsgpnY5WpW5X5UzXw4SrVx16xYFb02CmvBLUux9M5TSn9IIyaRV21i23jZyasev9Z7fWw8Wyt8ZpNIysZ3R2DLJ57ZJsl48JCI4QAAm8rJY6mG9O5NSCY6vRqRbUgpNb1nN1iHRSwkHr3-aQ_GSg0Gns4atVSl_yTt96hAgCz6_osLNEnb6B7Z9MbVHQcVwm3AgVuiqUmd1WzfhZY9t4HN3KbeDxQ1GNDYh8hVqyCcm87gdjJXAXfW2Fwem0sZyiBORpGpoSivQjCGIVhr5Z9BjGn91Zn8bIW6C7DRIHdVDk8y2fzwndlMTDu-L2i2HuHZl5aq9Zck6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LxzwcDflip8U4WMPvcyI9tOAkkvkTL7mszcnWpkG5AWkPjsO3YXZbTMpGH3NWFe6DkBW8Z-s1VV8H3vCVYdN2qStbmHNr9c89F8p4YRH0xoMEE4Zzl9Y3V1rq_objf1swOm5KcKNQhIH1F4dBqDmn3iyvlE25KBD_Yqma31Zu-Vgz9O2ugW3XycGH8EEtDqbAoOeXeALfFFclej2kjiRzXhzjTZIo2UzDeo0tFQRNfzK4deCiZbHs6Vc8ESkVpTmw6nNjOfsicBsmlpEWheHC6IodCkGc15lK9AvHwa4Lp6gqhFZDGrxED6-UR4gMErtwSKv6BF2_vzzUrVM0KizqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JOMgEn6S6yFtuB3vFNSpUN2zKL_jSexx63wVJT026pFaNI08z9XFpdj3a7Li7GBapjAzF056h8BA69jmr7mf8ZYMGAedKLb-88SWy6gqs6r7uj09aRlTkQDIqhx9BOzw9JtWZlTvMb8S_Os5_2z5oGNYFTVaxKrMFnQWvg49PGebSMh01whmfaIeQF__x0wJMppTVvTB-QvuJztRCcE_XBRsbO8ZTxPGgQ4G_F-rM35fWcdO1xbb8GyZ8LZZ5jhVqPP4hPbDmlkhm8m1o3nvb0_F2UirZT0YTNgNMagi_sjmhHmsLFboiyXzNXwnIlUoEngYEXtIgJ4jSRjPhKl5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mVj7BDZh2cODEn92fTJ8eALV39wfmmlfOhorphJp_o_V7Nt4H8gGzU18_or2Ql2RtT91AHHJ4QH1m-uHDX66sCwmuaneDWEgJ6XRs36eoV3vrHtEeUJWJIvQpi3Dsbl3T9jZgol3Cf3W88lYEKxKRRQQspbeMhwno6I8G1ZF7N6gd31f6ixwmr0zMmRSLXdmzDHaAHM1wC3oPJuY1bvn5-VLvgC9OsZB1rx5HJZ44WVFSZ_0MeEqxcNe_eiXTjrPBbBUjCGjZ1eLTz0bFM7Qnd5j3YlpkeINsmD0RbZn-eKrBslC5byZ3T9UyToT03HuIp9CrVVeeoK3UHjw_LRx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VK87nWwVtmko_8GtnB1WDfDCi_gcOrHxj0P0VeLvofaxmjcQDgiR2eOvFeIwyYtLtvWZhpjqRtjydYZDSjcMy_fK3sKBG6NtMDb5-jX2oZOxcpj-V6Ak3Plh0iEPxc-2UMXTIta5DdFa3oWddPO580URGUFQGhqMfK5dCSaqt65gM2eEKIcUaFIv16CCbR2-dXgvZZuEotsC7U3yUndzSyu_plFeU0lf9Q_JFcQXI738-4YpfgAiqmxrLduvDZTfYzrXCHz9S2JkXQLm0S-cJ_lsYPLVmevPueNqelM3IA4Gt85NTjimFROABVLCv20IrzgASFbFryrfc33-LB_4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qo95i3OtYxmOKS4O3fd50WS29WLtzt7-XITtixKkqJdE_TCJCSHcSxWKl2zSY8yjG_JqGlqBGuafl9qbfJ4clzITT4DJ0REBKbzIFmYvI8OptwO-vfAE-1QyrTEwd3bIN6vSjSUN3qqlmAMTGXBlkVo2zMk-GgLAZrfQ7Go9tYJGnm_Ih0iV2mxD8479o6coTEVijbcqgO7vgKd-qrWQY01ZALktBjqiEy50CacrlmNIMlcvOENSfeFGOOyskVo1GO8qqTnI-0LA7kRua3tn9eNdqeNrU0Sep5IruWL4_g1lvsHtV4ZUGqK7P-Lj81kV-GrDbBCzAW83UIMF-H5U_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UI56WHL_cFM36PTcn1ToB0jONaAr7uW_drZWu2pEq0zLgqIRSK6aERSnu7mamQ0N_i8xnjal8NyPxRKUSMoXwrJE3jN_xTC5HvVOHBqyLkKOQY0CebAIoXDI0APwboglS_JJI1qcpkA57UtlSsKtY4ACbq0f6Vsb2CCFCp2yFd8L4O2J6UjEMbB7R3QidUIwwt67-K2UEIwQfcRpnbP27iokEvDoPhk8fFi5dHR5Fewosr9LxKldFqlrni0sxbQmOZwLqMUCrrpjhq19Ruqh-rXOY3xyyUsz7B5jCJyjrBa7qps41h_s-U7Izig1olXRN135VF9h_64mFhP1HyS0aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IVkJXNQS6mHIb_vrewfoBItpAJXY1S_S783Y-T3_hNI48LdKrIT_wxz4ag5cHC7zpaQUMATLq9zSDRgvdSQ0PmtiTO8G_1zKVGS9S1VCopltpmHjkPHj-RlgrRUEYOfJEEF7EiQ5PdqFNdh6bQoJgt5FbwdEz_mu1tF3cn6DyrpeS55ZztStXYvieVvVbitmNK5hyZ_g77xlZY9K8KR97plR9ueYKy93Xeh-idXIphCe6KLW9nKZBDImqKiryRRgdwgK48ymZeZy98HaQAmbquP-tIM9xIwgJ5ffaQgnfDxa0MvF6bEdurzBWAYgrR4gI_M8WM6QJIcgOsI_X8qgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oqr3_yU2NXXYhQRp4VGdVSOlbOvE2gaF0ZrqMsShbVgOeIDarZ3nz1-vfi7HkrRK6_KI8TMlzSA-cW5v-NrCTadTlPUMa8M4sKgQLchBYqT5Z0JeEkzNOpYY_p21pgwZGK-9iyVWW8pj_7XxY0VpimHWbazM_wWK86EFU2A-B-BkqEqHCB7_HRaAZDm71c6HOL4wUFOVWOjQz8K7pMnTcC4X6R5grxXKqomH3ubZDcQsxXsXph6BDs-FPzVXSZda0krN0uaMAxeY3bMjSS7a2T-sl99tihVgdYY5p25xtNVmv44ewfVCiCg2XdB2shiaGvIqJADr8NXB-bTE0NBAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WxwKrfD_muU65DUtzVpBr1oMZMxO5f5z0ii4icMoedp9XGbn7wf4-r1XrLnDjZ8JnYacifO628YEmgCfk22lxMEpxlc1YEMBvps4G94E6DPnix4pOXJ9GQA_lblMVMrBj1vkam488-Aywy06L8Fbcmyv2IXcoMWDOpF7jIJarOs4X2toQF4ZJqCm6eTnzFaGOMke7H_3K7Xi05VT3iZ7fsENqNFc_xLcFxwbwEas2-ALmR892Cb9DhP0Pyci5ejSX5jSOjNDC1azp5sno-twnWcJVU-8c0dyORwlBmFmsYMv-RmJiGOFajyw11yM2yjVxP1qwLC8XIJrDW_kEPAiAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXxbIPux8IiAEYvLezKws_k_PUJ2HFUcqKLjxJen3SkqIxLSpSolovXfrMArBwrE6N5EhdYeR_sISvgsacW5e2tZblYxptc-tRLXQHaB4QhFFiqfkkHaPa1UD7HXrx62sCkc64rdSKeLu2D4DsRcHhiqUFKTSb9awGE9GU95cixY7ZpclF9lYULiKR0ERJciLr8U9OPznMuDPcgx4KdaXtXTnzApJoosQP1gwdF9E4ryOJy6FDuQLhBs4qdTY1XBk78bh-R09iYni2cwnkRo36aBOTVxfsyEhzUPCW7nF1GNfZJDhug8i-4UO4Y0Ds5_vtOtOZ5dATZIbjU0hPI8UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JCVshzqjc-IR5QkJfBvXq42uttxmwVN9Ycd9CnaETMk7hEAKEZUszWwx5j7UwsWNeCorwzDgZFC8v8fE3V1DZBWbi0G_b0jpRok2vbwXS5WSlha6awT6OaRArhuq0A5zW7i_WjkkvACr_uutGvDAt9y-ElkMo79BZB7DpVMsFfY77WHCXmOo9qSZ9PU2LZ7QtLXWCHyPCXjvPKRlF5jcNSw67t5df8h0o7lO6SNylqiMyjGRarvJIpusOJEsMDz3eqcyovY-rppQaoACVd0SVvdLstM6hgynb1Kugz797A1upm51BqbXX8Olwqme6ahQHTlLJBtfyj5wQcV2jbPfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lRC1tBT2OkNVyHU6UuDpXHJgbXm8LW6CAQnaB9dmyuIOnKUft9BscMVv4p5iK54DKQyCDioVf_gqQ-vrqAyLvTOMltWGXIdzG6HNC81myqLs5vovlq3N5RP7bJ1BtU05PTwdLU-mybXVEMD5OvijvkgVzJ6v90i0B40Lzv-gl00t-JVOALf47u0Pf-yW4PA1QoW9tn0sZu1eS_YIEbAinaIgf24fkNlhgxs8BWBU2D4pprJb-MpRCevNJ5eeGSRW_UmjfutPL0OYePZhNUujcAHABR_bz-OELLc3PA_Ax4stSZyxbXTLW0Qw68jJavk_5HhoZOk5cCKNW9ROW7YQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kwIcyFNe5_0uDLKL4GajGOTUAlfpQpLB-yM2b6e7aV0xCbatbr8ibv566iuS1nuDdWFJSzxaUMTO-JvdzfkWsKC0WtnnpUWBdusakM49YZu6o7Hvnnp_k-7mJUDI1LOQZE9dUu8Tzxtrya9OhDY0ER_TT_FgcRNYWoQE3nlElfZBC-nAbGRU4cxbzJbRVUnqcCrjMA2Y1-EeisRJnP7BnC39XEJXUalI_Pkvk8OmvzKjeblceBlupnt0G3X79688NmRYzz6dlymLmCDOMRNry2cimQa9fN1TKqyHopLcOf5CJpfwyN_BV5OU7yOE-aGn0xEIcAVYtzyzebO_yep2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4sR_fP6lHuFiKJgz8TaimDPNM45HQx204RSMZRS7idKGNIzY_uQVej-A2USe6mYrF6mylyyyzi6-R7CRIXYjbDXIrwg_kGF3godjUshk27NoZ2xxHrqOZo952FDqteQaAxkFi1c05n6djMfZIJ83V76cb3HXHAZBu47lfcrpLJuh4_eDITH0dTnMRYfymkIyXkbN3UCT0nf4BbLUQkovjVpo90uKx7CLEmOJ4zsWF9AsJZN7MbHcZ7tPSt9IOixDm4Vy0jWMYCpIY68LyRkWEttiqfsKn0Dw_N_M3avrZ5apP55tpzxj-t3s5jBGqCWGI_-9hI_TpmT-WX-o1PnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WeBE6GO6W08eH7gPm4-a-0CqMORnKW3dJZagB5i65a0vXMXCCqF1GNv62KhC9oIczGaSOqXnGR0Kl20tlG0GfB5XeQzGAJOnpiM-u8cqG05krn0c3EbaYlUc4O4PpSRaURjFSTjySJTnxn2yuB4Ejn1MpSxUaUoGMB8X22zB340DtaSRZ8Xab0gLTzIJ3RZ07veqFK3w0QXgMiQc0EvfwRhnjVJ-qcIw9OCe_CKnsnQ73Wr7fDsvU6AEAwkQ8dWXH2Z-73kXHPd0ohzu2MWBjFPAmQ3sTPQjHseZIl2HgHxSS4pQ84_oaJHwSWc0qEE6ODkmrDOQeOdr2MEPsk0KKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VJFQhsmrTJNTzXAl026aN2TntnhnDv2dRixotOltfr1Mqfad8b1gfDh8DgKsWhxogAY-aiYRNSKf3pOvl-tMyos4bxENC-24CF8JooXUubCH4LhzZfa9T-hFguvQALNasxrWS2jJPdVq8OSTkKjL8nZzpXcaEx1owdsaxwi9zfivHNQ10xRRCwxXsLGw5puRVj7mlhjmV4D2WfjKkcy9iOeVo3EJTRzAeIeF3cCqPPQLAw7oPj5MzDuz0SZudb2MWG8r82YL-a804uw8hOb8lvfW8z7zXPjYbZidRIKAjSRtDmQUxJZCqtSty7RXFwjSyyCxhqBDcDb1yKKEparzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8u_FW8fVt4LYvXYEZ3PoJ4eufNcYLr0J5zh4v18qC3QEBAMfQIEp0cum1et15SRxIRNTMw9RUaEh20aE6RfmwC8hXpsVCXTllpc08Uz3zwl48CnXTiuiKKT4CfsXygRsDuOfiynVTrOHTPp4cLq-_OB3Cb4HBEEbzlwKuDVdvCa4F-hSoSCM2oqPClKIlFTV0ITzHSTBL2BD2cHLSxSFkS2tzNmAFTySo1T-qwHpwU4XWl2Vnghhs2msFD9ueTYyl9QsBTYazFDAoMALa4ei7hI95SM2kPnQ_rrC1ft3ccSPvrRaOwXLM0MyKCyy-1uTByBIGwdXLhQBb3UTkzl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khQuKR75lgF8LPzCxnvzoF0MfY2FYvPWcnY0wY1LhHvSDD3ucG9lENzAWBIJ5F6GENOfD49Bb5dgr1hC4jYKmmqMiu9OTZZ6NIFJaGaXX5Tg4oxOjNOHRdehPC9_o6zMVlE_0mH38Wd9l8YrE3twhZbDIyIqdOoA7Tc_v2Nh-CoaDkeZcqCUyrNAqIRUvU1VHxhtLjDXSVIGyHgHeL8nHSJs8xhS2ae1pd7BPTd7H008ci6pOE9zK1aFsBN-N8PdPOh7U7LEtg3DwLeacLsgc9xQaB4b6RbkpGYtVwxjZUiYalSboCneS8LcuQ2XnYIMMuGXryTSoEcHxZBxpm2rHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aVHJwiW1nUcFVpEgcqujpcZrVvXqcYXfgpbhJSN1hfFe1mr_MdpDEA8eHmV0gDMlQ7gFxAXAGR5rqczCNn_oXYQkoU6lIbepU-voa_xQFIPoU0yVyTvyvvfvXo2JNb27PT-r-AUI4AfPwb957sXCIf7DlbmkIXZMaEXRnIFKxmQt1j1U7hd9d6oUJ3og9fj5jrFyZwAMiK-4Hy8uHwk7XhlIXrv0OF7A0Qv1oj8t70Z4ESttiFlW3w8j5w8OzVMJ1Td92FRvfUmmoYwYtGTkQIOGVC2x6qw7h5J0whXtbeN_mCDwC-xMM696uXsIQGy0U1xD3RGsG_3QnmQisICc2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tpdxQ6Fyd8GzaOjBoNwsykKjwc3E6qNI7FXlnd7FE8tw7WvAbzFLCHcdoSlC4dNLphjuEQeJjy-19633izsWnE1Tf9dEhH9W7ERF9WbepXTWxIV5M-MDlmwXIQwH-p5F7oWWTGAZd_Tomn8cTLxN-e-cqRh6E1IeNTXAg3Z0UdZ0Lwbk0NIejuEbdobnKSYaASpyJTuP8cBANoidpDxvgVlhRnGeNQ1wyy30cNekKbQhu_0x6XppKrkvuHkZq4TmF9F_gBkc37pADphOO45KfpJywoHmzXFUixxD9l8YqE9NtQEes4As_tLg5wbBDPbqKOXV2k5hLOeAiYFUbW0GYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ebPK1j1zEKZczUXln-UTaViAsvvet4f-_xQVvl9pN8udh_lptHt7voc_knt7Ysgp4_TPH_P2QbuJdJnh7xj8wdx-j6zbEdB9ZMrmKx0kCO3gAr4OHcmt761WjL8LNvT6AOXQh8Bzizd4xct2OZiAjogrtGlXoQGgEjdZkR7NFpHQaguDdNiWUN8D1sgt7ComYzSLUwZj7-gLR72r54J7yGPUVlpPromwCYykDt4daTHxKzCXpMg8HxkhImCXwNGlFsEnHyyEM359BzRgYaW-6fn2V6GSACnLaFnS7haYvwBpsPahXvq-MhuFPqnPhESw9E8-GNGj6NstrllwJ8vxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ye7-U_H8iXWZ646p-bJ5HnTq0fnRCiZ8ZyzL5CPI_3Bm9_yqV03vAvkA0z_cDA2l9Ex9MJSegEvNkv7laVkR3b7BK-h3s3T4AKoGfkNuvLlI2_4HJAfTYgvsceel7NNQdqFBxrEm3JLjNe987xMv3P3jyoYW-M0nuMrtmEqKE8CZztqcGq3y8NW1XaoQM03ra7OAAMoyrZvFyhlvAlohWlMp9in64m3P3hxg8sF1Fc7_d86YNS_TW-hI8PA58v4qT8Pt67PPlm6Xr8L8L0DfY1FEncwycRpmTtnk86AoO6tIevgy4ktzRhSNLtCJSaJuvn-F70Gm4QxGRZFiIkGe-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QDRNkVFWh2jmFnWP_7R5YRWCoGD9cYHlDtgxMbyKTtN84KBwTO_YPeXtzBFUYhKO3O2dUyfC7A02bTkUprMSmf12vO5Lk3WXOMJIY1r-KVXUSm0Pb7tvd2DSvH6WcPcGtxi1oaqfUqSAEFhmhWTUF2NRlBsy-t_yuFl7PetF0MqWlnFMlzuIAm0G1b9XFvYf9AN6oa5Kz8rF806hz4SSbJR5K7KVLxQeTv0iDOxOBC2NzlnX5_lnpAb_KbNGPE-jhGFS-X0yuS5xmUIt4ncY0qrcBSqZjwMycZcXR9pmfKPOkCNobui8i8o-2M3xKRsrNles3y6vnazZK9hdhrwCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JjYHfslFjM1bnyXeQ91-mhBFVMqcJh3Ng7KSGvjuWj9GbDAPDO8h78n5acVfqnVMcd9yItIOkDXd2sIn8GlGZfscXWytF8DTRVCknhroVJWi2clr18omClrqUaKZS_ALn8EnFTmn3onCehX6raGZgFKJfv4_p9rNba86vBpMJpyVHZIFfFXLCWO4aYkuxC1-VaXuwm6_b9SDs5qPeXeXKnw2TXTcLI5gulUBXt1uP07u18-KJ0OefICi0DmOn_xcRo-nwf8-Hj4kcYCL44SPlxnJZu6fC7JtXdZ4tncQFzGnt1LrChJrfUfsarfcVvbItzCXiGbcTpSPJ08pgMmIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Cg9Zuh8WA2b6EAzpAwkgqIyfvsrOUr7qfGeJnlOLraeP7fQo4fNuZaJZZwP9bRoVu0pMtMp1Dwk7ezSN6mbWQD56gpDD76ascFVnU0phsvJSFncXCYIvAnx2OJpUgOyffCuvHQtrl57MQUretExKyioCDFN8BdLMNScsvGKCLZKBYbfq0W41aMYFQzrqU5uWPlZd1q_MW2ynxUQrjodxG558TysaUHWP5s1J0QwqXr5mvcK2gYhMx4SvpSVN8p32j6hD9RVs2EfFRfURemrOvT4GjyGuceetrqNpHwQ23vNM9Ti8QHSFOYhuc5QVbBLpguWXgoNkNTj8Q_iDFZ1TKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=Cg9Zuh8WA2b6EAzpAwkgqIyfvsrOUr7qfGeJnlOLraeP7fQo4fNuZaJZZwP9bRoVu0pMtMp1Dwk7ezSN6mbWQD56gpDD76ascFVnU0phsvJSFncXCYIvAnx2OJpUgOyffCuvHQtrl57MQUretExKyioCDFN8BdLMNScsvGKCLZKBYbfq0W41aMYFQzrqU5uWPlZd1q_MW2ynxUQrjodxG558TysaUHWP5s1J0QwqXr5mvcK2gYhMx4SvpSVN8p32j6hD9RVs2EfFRfURemrOvT4GjyGuceetrqNpHwQ23vNM9Ti8QHSFOYhuc5QVbBLpguWXgoNkNTj8Q_iDFZ1TKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kn6iYpMgDk9EhLnfzDTXph2nHplgLji4v81E3o4Q8-33LcJxkQ-7ZZAUXv0A_bq7afd1XfEFVkguYlAfvejS-X9tzGIDLCMuNkVF_C0QtJC3IvyOpsNOr7T2wnjSxHISh6quXbnxW6NguvGZS-zZcIGYaobwOZonPZg8PJ_cD69STMuWF6rEinDH0S07IcqV-zEvJFjdIgueseZpFODY5b88YDjzMRS-EbBf9ilQNucqLu5G1api0F4yFXhs6ZN6fehviPwII-wpFaD6rJyHTs4kijk9acGZLOWOFjIS0vjQEapRu-0nWgUBbcCK5PSBYGhaHVfIvqUoxfj5tfbFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WcwfGRxW6LTtXEJSevmVKHXDvzwpneFB-Pr6WbJWZ0TzA4XWufQtv2pygwHhV8j6qOxBzR-whWoTz9VdrbvtzGYRLOjaLSSd6j0NngDVXQVtm-cVAjRmahg8h2YWj3NQQSPHEZm2ehLouDhtdXQswp8w7HFk5gKMLg7fAAE8Wbua3GfkumlgUgBweBUgOr0NEl3MjbxFWawcVUBku_L-wTetco6uHYKvIhxwjKwR7ikqhQuhG4WFVHZ6_WWwkMIsNKZAUxrwYqlJzmHLNHv97LhmamUJsx-7zbhQV3grI3oQJ1s_x4vUdy4x6QHA3VpU-lUsUB513QLM0cQaAK504Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HafvsqlVw2nmo0flCGswA4IyeC8g-KkFmoNWXHSfR4pmP_NVX_8-zQBwOoxkSlqeahs9ZIUBV67YBSOvsscxGlJGo9zNuSOIBnYTdDqny5KpYcJyrZs5ncgO3sdgTNQ-fdoyKA5jrOZ6y9ct3cAz4jtxZKg99kY2OJTRzpAyquPYbhAx5wWlKhHXC5eoMgwKAbXoZ_zqGgD2WyB1nAbSE9xPiwFedMN9RRUbhR14fv3RQiRERHSTNf1RiSn-_D7o_EFXKNIyeFeU3Brt-G2qvAccK0cPJWgxe6R3jwVA4qqChEIT2NqbBd3n-lRw0rMdISz8NmeV4J04ru7Tu3Kw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TC42H5aEddc5KIsIITeMVTgAIMgRMaAJNF4vhr0oxjUMrUIfENTJaD4Nm1ieF0eK7CdbXdUsm_KP8Ortb8SJfIpnDLBLCzdpabf27tvg4i-SlOQgR5Iqk2V9heke9F0JxuEssIDUdyj3iw11x1fiEHaikbVSxVwEDRPLfxYijOM0ZNFt74gospf-nuBoAnKz7olG8GBltIeowdT2b84FgIPy_WcrK41a4qtrnvVXvK4cXG-KMgf8Y7eegshcGzXzkt9oNBnZalAj8wkgtfYkBIQtd8mHrU-hePuuU2SIUrvDp6fP8hctctnichbSCgddawrwB_86mRjAuYRDgff-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZmImAx7W4ZL4LNuFwtm7mAPBAtjTppev4Tvw3VxWu0p6UO6dD6ZahdvzA0UQlWAc2hz8ZHdk38qaW6sCGlwY0DY82klw2Ngd7F_C2hJrR5rRrQHHhe2r5NQrfHItlMHTmBSXKck7DUL4io1J45aSs_xKced-t2pgI9awAfr-Yohh2wHcRyn2lfWp7Ehb_bZDnPpoUF2L-xwtwdT-y36TEiQDsCF8XhtnIYb0p7OcGi59XzyZ_TrMUZZoOv19AM6xydWM48rDaqUOIHeKxSkW8QSUKAgdomaoD3x14gPW32XOpjvFVI2DZTcUelm8X5rmjn30xYOsODQ9iFFqIvE_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VvZE6g9mR89Tb_-GNe5ke2PTVoylaP-2h_t29nXD3sTcY9w01ejSIPWymZ-iHZ5CVVdixKZoCXymEsVCIMCsHsN2gUvOIPxu0zaVhNlFF_l6--vl7Dki9bLDYuKFwP_I0r21DfIqAcRoVKEmDvj8R1ErQ9uY30ek21hAuJWe7O7wFz9aRoVzClltUn1zUhefRJ3IZRutFSZBOws602IIPpMhJ_lrb_zu-jG_nawfB2yl4NJczdQkhmI1Za-R5LxvS5FLU9VIx8T9TNuBmIh5lo4BZTXENUrMP51p_C8giy7o4NKZ0jfO9aTuUnzTuqBsZr4UHir0ZUp3oj9ficyblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cvcMr6oC5AOCDOfqnYaCbUjG17temF2IEO_7-vLJWAO7MfKz2zmgSixU7YA1Dx26QEhTTHjvHBRG98WIK0XQeEev20zRPZVlIyKGjxKq3PvNy3pPgyzmjzXMKb95VjBzV3-lN3aPMGD0PTJ7U2TjtM8zPgZ2np1JPUNAlV_uRM-lM1qtpW528oSaarj35NSHLG5rtmjQEhoGmCrNJC-LIVGrLRRZySXi5e66yMfKd1Ve32xcFLAe7XelKWFPFuq6uAzn5S94M-WwJtDEmXThonTCbu9U_109litF50HhytaqwsNZC7H00b9nq2FPZg5E23fPiJOZucBZbIkXxc6j3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CYJxJoVbwLYhZuyz4AIX8Ad407Mc-nmP_mcms7MS-0V6GNg5hTv4beco-orR4_ugKMebMlfpOS8rbxJPRwOLy3cGGUVMpM1JNFO14tVU5-K29Wbi8bqDxQeb-UTdP5VyZmDl1swrBhhX5w4npmPQAO-5ejVaybOM2dGw_Z3XEs2pZyWuEbrg59otM3HHYK9gY4YjV9c7rGeHPiF5jJw85UyD3XmL180B5spFdUsCWznWgFqwzdzoyPmbqKprgpoOQjyWK2mYPhCev8KzmftGyDHA-JnYfSneiaHRcFDyBxuC6Wney6S2MvYLT0nxWsW_VlczdfheGg4Dh5U4Xm_J8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qhxdlosY9QJp5HmurLBvpCp_B0xNdCe4hcmO24RQTBs-vd1ii34V2PwgkL3Wv_sVkwyXKNHbxADqB2L9Tu8Wc1eYWvWvRBkh29hAcB6xgi20CHYsUp6X0-sSmciGd6A05Bfng7A_ZsWp5MHb6UIWVahNGMe4YlDqrWwn4fJwchzNDpwDyMFIFKGkJmqY3BWVRbK0Qldd1hbvAPZTnRuRHvs_qxqKKdO28cyD2C9J0YIqy-r-npa5mW_y_c4nrfRJC9VrMvIa6ttuPXjwyVI8EJYJaRpS0RAuIo_ks0raZqcBE6v6FgVTvLtNPIdkZDqxSExAn2CuOC88WSk3HEjEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EjAwGxRTbMyGnwifw0N8OIdIj5q9qoHNkk_VYQ-pMjRy2XGEpA83r7JdRNyfL_MPDnPy0457sbh8RUX4WA5yLudEfwQJWolkAtR0id4rI_RcKwIPnk2_rnCrbsRD2vOMMz1Sn2r5FteazTgsOzzM_jVw3zkQaEca7QGMCTYASZKFWmFXdUaZi3D4xsEN4MKtwpnQIz4UmD6GUj2rHGhJHzem3cefGwVpIDzyCvhqXCfh23KpnuCc6vFF684mUAuNMO2_qV0sg3yIQvcC5Le6Htp7JKlYXlVL0qYquANEbiuxaq_xIP_Mp-dorvnx-AflYxlTnxZDbm1n-jNVvaZpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LC7fzJEXr6YXS1ABteu0J4s2yEG-TOcvIloHvdhThvUFMEowDn-RTZJfucs1vMiZTUwM6lFw9kXLrpxH05LFoM4Bc7N2qGizRs0ZRnS91S_0GSvUoff--GicrvCvHOr0iVD05CTHz_3_QVSmZKzzGco-tScUmP-1CnjoiU37H8YdfgcMLCkqHaEGNwEzvm5H7D87S02n7OsLx8iRia-m5e6UH8UNnvXY6y18JG-ajcZD2pDfWclmuYeSKjFUac15aQdROM0eg3BNp92X1Caf86bsxMS_xgIy44iq3h5ESsGZztXSJPcsVctYVOzIMEajPvml-Mq9faPJESO6iottJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ITrF1MciGXjGfUf-Ly9buV4cjiHwcGG0D8CjLJISc-NMWipBgeZgsWlDMpHmIGZRL7mZTWJCc1D7isxYLovgZLEwlcAdifW2xwTjWmyenX69NGFmczf25RlpV6krFr-euXZHRdq1BWj7ndUnWMLpvBI8b0YAFL_QxJsX6k8_ot7MJedVeb8XMhAbWRZp79cpUlANl49W-Qy5JkL9eM_8eQBJnfMqz8q6z7vj5m0eZ6F9JFQ3CbtOd4aHmDjh6sLKaWH_YwKv0A_Rd2UYAhZJebdvBTT4XzaVVvkNNpHryOZGIRN8Hq7y11854GKsk5uAOJgLwjJe3bZpaYqe1olzQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NcUJ1S66ZaNsJ7JnAqgJlXyBKbV3f_b9qYVVdtyYMtlhmz6L8nn9joOKA7Bu3iwpQsrGFCTm_xhOXGMt4gyYU8fbdU-h1R7wUzK5UvlCIjqPF-EXg_aZL4rWuuGLeqxHAxtTM1gqZgLcnJpjEopapPHx3wwGIReL6ikJS5wihKZwJdpwTfK-S1a-s3vyp6JL1Vo_8Ild694CsRouB8jSR7mPUsITjJ3owZ-BQn4fU32XUC39ongNv2XdxqHY6PXAJtw0QLyBnu9JZ90mxWj1eE3qAygaP2T6F9IHKkL4qJmH5pbpXtibUpwOp07Ga2oaA9DXOCmD4Kf5YXHn3Hnvyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_vXEnN3dJSuVqvnJLoRlNzK9lULFrAkW-4LIh36JiLUIWtNFEpxSpFtf056-VVjiYba-d6S4T41JMxkkAVJ246E2ZZkZf4Ok_ZhxZCHurOUsIt2M-HICdPZlJIMTMnlP5jHDLRk3CoEV-idWsWJrJldLTZ0yy5tvgqR2yn26M8whp1V4IQVyBmD0PGVrnAl4bGgDrQgOiJUk24biaeB4Gh2bbhJmyXjd0NgU6bwbruPOSPCWvIBJDemuDayt_fFFlQjddk3g5vFji6q9CIye9GAGk9KoX5SQ7e5az6E_XlYASs8pW5ZOA3dUIDn2gyCWNKNBQk77HpPv72QfAzNGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bglSJYpyR7ivbGR9uII7a8Zblvc7AOCpdlPqRpnDPJDFZ6hgWty4A-AwAwgVQHVRhos8ahyHkm7QhWE4Vmw0nYtHBuhv-Bs8emZ_QpnKTg9Xh7ZxFXbVl7chq6Ge3rnfQZ98hf1aLY93bjLOa9_MLbUc7TRxWNHDyrvTiaeNqt5yj2FElmzvea3zAD7LhhgTmbBXnw2WIz6pCGiFdcnhPCDSDvoPjxGyUyRCxtC3Ym7aGfWPTVIo1DD9i4j7MuO4zBLOL1uZU5OyLeccVugIITAN8usmdkDD3ka3Pk2Gf37ar0eXGT1ig4RUNMF_Rz2LSe4T6I2riHYH-5UgsG4rEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HrvIqkKybT-ifNRfbfYLZ3HSK7FJiKK-2W7tlKu--OFid80oEaaeyXHWzbjRhkE2UaxAwh3pdINyGUKFv4iMNxYeT1twvK_cn2tmDD6_TVHkMFhSvW0leaTiNSMoybvW96UpzD0-gk_U2RAhzo-S-MvYe7eF8ryPpeVOANCodSAKbWjRy_rWUyZ90xEGvOVdN2Lf3uz2p8w867sgMZPfS4dnA46nuO5LwxRb_oeC991OHIYN_udHFP2dHNFfiE4nYvGQFHWu3-QM7rGMqq9Yd3C7ah1U2tMbshUcbps6vvrMATJ1EmjSfkLWnB0zvv6MTqavhGFamA0hX5PwD0AO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EgpASHU95pLbxsGWNPuTEzO3sPz-WQXTy9xAkFfuU-sjsfq643MWgEQIDDGo6UXlAaRHQAENlp8OLVzir6EvPchZrejqneEC6lZ-FWO15EJ6PJ8wJxPh4LgVPthJePQE7xjcdmiFhugcuv9VpznO0Sjnc62yg9L2tVw2LeHNXxLg90EZKlXPE0qX7djrltOYFJOLTPwGCatrcsdf5dI1QatyNf8RZFCCXDPKydWNMfAx69F_TkWBlWPYbT97DtB5B0IOFkjn-0TkK5OV1IaxknuT7_9FaRWS1nGrA61YFAbyImOqh-wEjiR_7FDAXhNevGMfLLYmijY2tzTI5hwv6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vom-TUlEi8vFc4XFzCJw_jHJ0vSEyxTaiWxNeQ_371C6GdNv0bmd6wo4LPJoOKpPCBLIC2IoXgLF6uqNG38sRtDfegzrTfgP3w5yxL51JmnKVEGgXUoXkOlt-edH0exZlWxSGRqO7Hlu4IM3b-rUg2OUmAysGz-JF___WynZMTRBOpMZvcybsjuVXLHBySyQRpeHmWg1jerGRces7V0-2qz03NxKEOdTW0JLW92Irx-KNMeQUcIl9JIXjLeTdubMzynxXIOFo0H-czf8FVWBNIy0mEhcKxWZnx0i8jKeqx-GyOJLbzwMHl3nxSWFRkcHxOk_IpOhxZDhgqSn_JFDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJ2VlcAVijNUCsuYHqy2_uvj6HCk8hweqgqxXSD0QPOZmyQ1Fr2-YZuY6SU2s_DJpZ1_wmX9Db11iwZjWxxrm2VuE9TRML3o-1G-oFZ2FR4mGeo6sA8RF2kgGOKN_4fNXiW5RffGJJzaEP9cNSurUj_vmcZqXmQbtppL3ng8b5qRFzPQA7Lu8xv3bZq1ugKmMPedqdB2ZXWUfF2H58E8WhDpv2S7znzabcXQBdeXT_dZUCt9sl6FTphqYlewpn4NgVUkUHgH5QJdnRVR9V00EcSOTtzYs-HFFbHXo05IvHQqOq60Uh80xXZ8R7oUS5_vSKxLiBLpkkvGhW4gy3r8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UFysDf5LHLqSrwMUtYbiFpdOYXIGONW7kMiIAETakgv1KkRynKvLKfCxP-e3GjO8ipvLsIoug5P1rn6K01SdPB3m5wWshoZeQ5gKOcDg6RU4Ur5qEqTfl-8UXwmJWGSxJb6o8LKk4NunCuoPkYz3saHUZLM5GYBAcyEFY0m8SMHtUj4j_78xUIMNDakfkvwBL041xoFxkR1VGQuauk4Yq1gakybKBXfymudNvjku_yd8wzpEz0Pncx2O6qHM6Ky0y46Z0ZsSNT_7akLjA7_nGl8VQ81aJ3H4zPgFIIQ8cSsHUXcWdTdJM4LOzav_FS6TGiWvDSdJPKv6991r1uKuRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XxvqsBwFaCDV6tnO2UPbfcErD7pjBAaib1Yn7176ltIt6U4np01L_Y_5wHdRwJE9WxyX95_PwRvIu6seOwXs9QZ8h5tdEPhJO0a4X8BDqNpp4uLnByiXKfrbYO5npCT27DvIK8rvW120QwX_8Ieg1LqOMVRjy-lfWncZpaTByGkctSxXedkHg8UOXSJzb67kCX53vdsqum_0gqzapWgzleJEMLBxVsWxm1bJdkhwQjGhraDUIQGwGT0eNyGewKyDGROpUTGMuSpwViNfMLOhdlF961R-Vawe-bPWzhqq1hDo4sIMApYTsEOwGs3Xyf1iL19VkhzEorweORhQO3qQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFaF9MGjLsAp8o9gQ1s3tt-VcUNbXerjr2vINZHBDcekd91vC0nmoRe-GC6gXcrqEFnaMs69swoVRrVN3diOMMvx36k1VQ7IZU5ss-Yji3scpouKNpNIRcLL_khuIdzvpVZPd_Gg4B1C9HRzFM4D0XTog6tUq5_LX6ycgmasrCJdNW8LceUeeFsm6M1-eZt35DXuHS_uVqdjiz3uLU3idPrvBIyYCSzR4JB4gL-v98K6mRbKIfbeah24OtU0tMtZ2CCC5poe_HgxM8zOJuKJNWX196L0D5zYmptGxE4ZaoUUtlxNofu6ekFEd_lPm8VFWNRMvsanLqMj3zdyYL59aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QK0Mt2hAJJvuiGbtoXaHilOIuA77fRKUZnQHdX7IN0_oU8-uTfWsu0X4nK7m9K7jHynb91YvoEXTSPFqhNBy7qvvgNyUorKtzsGCWyqXQsppASXEh4LJC01Y5-h7v9U_n4BeaBBbHPmJzHdDA0XFnRiA9xMleDN6nBpujpddIuozFbtZ1aZwZN97n0a1KUn6wu-rkR9blNqgXZiq2AdvjwhN_AHinS-cUgEK7o5DnLdpPY6ZMv34lh1viZpQjTDCMtxiWlhxHgoSrkFwUJz9JKL9N2XovEja8jU0lfBjX6LMPQMq1vI38xWqj9NoM97cnEeHay2lJ-A-1eMbWWxYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gf9aiMl4VAY9wb64X0E4HW0KUz00KxI7fePwnRDlWWbasIXB4geaIaINvqDnPk-nYXshyD-baaQ7pcBOzfe3PElj1NpJLaFuhFNJjWPx8CH-uvwG67hndK4cKJ0LKdJuqQR2SwQRrH67tuCkgxAgEHyS5RzX3_S8Akh2yJfDojuwrfeEMMIYPOgCci4I_DvRD9rlqB16NFu6Kfk5pqwidl4hpUJZ9HCQH5-cwWgg4nvKYT5E15dt42BlgcSDVsZuQwllPhc942H04J_ookHnZHnfxuNmwFypxVnpn3kwjCJpOiMW87s8qU52QfzYgiiLjbr43Ogxawi6dLQPYDOXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r8L5K9oEGgj8g9RoY6jhxitzIAv8GACM-O_4cU2L3EPNIp-EGtb6jID0vgJDmxA3mnkAVBjzlE-4gmQbteQfKPcE9OpKOjngQU45oMpb1xHAICcws3bQ98ToYqq9Meq__-9iBwAGY8hTnhafNN4DfjWM-jL0wYLBTNKlAyQ6zK_TpKHTyuIsm07Uu15llyJYM1O7LboooDG6Oz-rM0qIiO6pi_FDsu27DZHMJOAWcgVHFLOrHghFsF2xRSGZaWesZh8dHvEEPMkHbA8NDHqj1csbWlD9nlDvI9aQ33MNvE-8IckkWwzYLq3S6NgBNgpspHlqcMZ22tUVczV8hvzVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JajLFAXN3gTN9GsOj064dv4cEKlI66AiB5QrLqLL35l-UJTuGRn3LUh-tDeqbEegcjpve__E1GBmzlAW1jumyXZpVQotbEDZlXPDw2-7uJ2jHlIxKDlFlekxz4x6h-CCkjwZtZeacVVg6NFY8hyu43iPKos4t7agg3Pimnk_OUA-m0Cue3COVA3jC_hzgnEh3G2VN0-Gi8ZyWyL8Ung8E954ZNytrqG5Cy6JIWfn19mWmEZ3Upgdaiui1cTdogr8N5bEh-nWEfhpBsx4qtZTBcOQW8Ft0AM5yeDLHbQfQMisxIgyxpz4f0lW2ny_yAMH8T1awi4qGYVTIsnszBgxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYn0GnSTIKzlluS-eJGnTeVdkbOl7fkkjgNJaa5b0756uay1R6of-yhrv3bA1FVUH9dDfoplkwm6YU2XSt263q4HvTdGC_CK59Ho_4UtEYAxZpR9_YzzLcs6RIwsX_IiwiYP93QiZ7GrXFfvw7QEbAGZYnM_iUdhBr4XI2rajgdlIQz5nkbBcJk4cur1WQEC6anO4fYL-hs_lqx8kIYc-ApdwPHNoKfWEk2zgHzG6Lz8Sxmws-WcXzGarsjJ0AE093zTLUpYXwXTgJCWUmJwrIh3dMzv8iQheVhYknw3HfpyJzfeBH3T1Rdn94RzAfmklSiGAhh1tMy-idPbFhaC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQDUNjDy70yMYAXJewP788o6O1f0MxLJthzORip1Yfz4_BwGBRtAIAuA69PbOuNNbqBx2P7F-WY787fHhwpLMtxodpo257EZf0uHDQrzb1ojCPIk0YdMxyr9xrVs8C2ym-jxFVTWiJQhw0GUJz_WIIcqt0YPPLx0QT-LEM2iPCxTaeNt9tDjPYfllUIiaci-mwiQIObIrUyCEfnCgOvc1IaoudMAkmW2P7m5MxjxlXrE1mrvTmpr_GDP8YSvXxGGMdaiuIsHUAebbR6NNyF7XOTdyCxOtS8y7-ZQseX68vIXd4ZDJEV8u3u2padfYN7jyi1mwSVcnDQGhawBnYNQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GZvupOdgE2KQavj3816fOJApl31OW2OHerQlTieZgywySvRfi8cEOatemczNFms3tG3dUrxKDSsp5VsKz4PSz6A82Un3nn6NiB9Sy3R5JNznKyoDzFKCwdm-olDyqPXwjD3qBK69-F9tmhJnHloW9l9dVKOd5V_QMG6vuBB8srD2-TdcLyJfzidcN0YeL8EQ43PCNv2Yjh65X1nCd1XOLG60vIvNHbGk8j9oqfr1w1p2OARH_tTLd4Us_YN6c4oKzwT8TnO2HDmQOvrftpI7P5aJVZY4WaSzxfSpkqQuQZwrfhM1ZTaBdNA-e8JAmFEZwmGL5R9SIB15wSxa4qjQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTbB-DOK_xBCjgxxF5Wd69d4Z0S6WWD-AckFfIK63innj2UcNWa5bhLS1WovNLkTMthlg3NOl6G-IQxIX_c8W4CFGNts6RpkYI6nnIKCvEhk2PP0A2a2Yf-75nCgUqbbVVEjV3WJMU6RplPFBcYeQrcq6n7Fpf0gLx63OcE9-4diyUyCfTDJ2moiVewCyBf2OoOtSpioIGVO4aaFc1yDDZSFmUQ6Cgn7aEbyph_bRabt6hhQCwks2sKv5chZBoCp0K3W9jUbKIbxeYdP3mi-T0hBHpGgyMG2PLK4-FdRrm5dxbi25l5sca-FhOZcw3TVEanvosAgYu1jYSgY5crurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/wCV_Dzxr4z--IC_Cwpxr1TAXlsZBHUcScOTw1Acd8vIp61OdTUaKv3vuvGskWt5kEyaXgINwfzWhShkpqe5N4W2hJUPSCKO_0_z1z75g1_DZCsyFxGABnOgoVjxXONekkEqE8L62sNAlTYeFQcd8-uOkyGREZ7NgE8zkhreKPFhBrzthndyQHvil6V7JNoozWsOS1xk1GUxqqNiks_J5PBG_I9pxhbFFQ9mWpP6vSi9rDksK0yNsRfh4QSVMB9bzzPEbWrNG-VE8dAEclOP-x6fTqVn9Q_7sMv4BOGZ1x8S7ncOS4vtMWhR1X2SKdm7qDB5bcIDgbh7rE0_e9vRZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kXeOTf09quV8PKo9jgYmWMwy7nSkgFj6u3m_QzCkSBLO7Iy9FYsYtUXq8B9U1JKqiTcBRVodqCpgIwEHrcb7FZ70CEJlSY7VFrvie4c9-vodujz_LjxH1f0jlXnHsBmWT-_1oYDlFwg41r9CYJ3c962mLu8-hdbFSksM6S8rLVx_BgRmzxu3gmYLGxpC7HufVeNosXW-VhH4W3ya-FozFL-8dobeI3TQNRCpWAteBmVR7g3pK8dkmK9IT9QznRtiY-698DqgP-oHEDtP-xjBvcXLPREw9JtIM3iGnm4NDAFgCmeq0YO6ejK-VaMMKv0WmetDT1IMF-xg4v3k7gSuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E42OB1muZr5_6qUIuX0yp1PZbaJtdj2RG7J4HjL2abWyQPFx7yR46_IL3TqA591GXnvXSj72GH_C3LVwFaIe_kWVRWYYSsPZ3RYkxneui3QRx5ryQ3RvtR56N0LaaR7CQgkMfabijXibLR__UxlUzwefBt_Z29t4lHOcmtuesRqNqhckW43oyW5cfXRtZWXq7eOu7kXDndhESAO3uHlxevU3KKnmbQQcYbA2gpWwOrdSaxRLuGVpeVPA2fiT-58fjQZQOClOkQevjbOZzFvmMWNuC_eShrd0Ptui6F-vcLUkNvUR6RIH5ZlnAjzJva7oA5uS1vc6zrXVLs680CTSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rY0IDJSL1Gl_Chk_4_a7wKSshClL3yBuLci3xdSLzmU2_MvtCnvIw9d1FAhlxroFkRI5fE-2cD7i1-ntru-uA_6lpXxI7fJWrRn_mi7ZtGPwiKSHtqAYNeQ8gkvDtZ5KVnOwQXK2S6FAahWH9yXwQkl2-fK07gpTvqZQDJ2zkg0CJEo9O1lN-u0d6PKTK9HMM1a62aeLKiI1lDUVAAg_Gz7utfJPMFyWvgtSARnTEAOPNXWn8dYpYzP2gA0GsmWSVvlqEWL1pxT5ZPceR05BVPcwKHhYDZjVdWyMPKuEF2fLkCMPA2PfUmpzQZAV5JdRPY1_zgbzTioMVqlAybnAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1bCyhLtuub_coEm3VgvPo9M8IhZzQdy1bJpLViLKiArKEIVx43P7-ij3aPt3r2Vz3aCDUYjUu50AEdxex-dtEPWpCIZhycWwtTgtoWYf8j68p58TqNQNIPJ0hIrkpESMbXRBcdRq1yUePJxjU1_c0cm1NwpgmNwQhnC7ZfjaXGhq6PRN1JyA3M8piNiJaO8EETfP9jJhIOWDpyoy_pgLkkQ3H6k4tr_9n7S6dOAIL_0hClfUyU0zfJw0hMN8XBrcn3KEsM7-slcO5labV1eHYqIppm7pFUqQwox0F_2e6lTJaI5PSJ7UH9ZJCjiL_jHANihfcBZy-P6vrB4D5AlFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AF2O_7FRncD69uiF9YGuXfZ3x9DKk6dFtEDBaQ379JIwktSEZ7uWua3Eh_hfzPelkm0h6hA9VScwuLbA01GyUyNtbUNbIdXuDhh2NdJHrze8MFv2keP8Na67nfXn7KbJEd2_y623DgwuVRB9wAka-ocx4qrGdBfsXIyLvQ2aF_rjTTp8IcniFbbRJJNek3bzubj2up5WUQAVSxGBeAr3o2q4sqGIpDpnpfYzuGgT9lyrr5DXPc_6eqMvFGf-omW9cQu_fVDRfX_qYjqpthHTtyF9k3IVaM6QsOsdX6F3U5PtbOFhjLbl8ZXx_Iwje6Zl3uEmkC_FdvTLJ43JlqNW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
