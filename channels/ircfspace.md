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
<img src="https://cdn1.telesco.pe/file/ksYu6dJwHZ7F6OgDgz36W9DpHfGDVjCwv0TH8PMHjsIAto-JzJHHKPyirrOOEAC4Idl9dlq2lHPptNDQX7_2hIYg914ei4g4NU-8TSX7x177kvDtX5gLtnPdFF-0XWCU3GzSrBbEZjHjL5YqV5N2DEF5FMs1PpUkZhe1ae5JXssXklIk5ippjGhsNy7i5-5qgxYPU6PA9J7x0T9jH_s-Cws2i3KYxfwu8t5N2p4DfAoolQTmZUF2t8BqkzX9K1C6YsTj1OICXSI_nvow9CmIzO-pV7BAHGLPTV0FER59EWx-uI_3TEc26pqqKh-MSG5KZYdJy4WpCLYDlRNtVLCNLg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.1K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jo896Wi6VZhT2kMCL0TsxwmpVzQlOwLH9jvJUatOwGcx2T8T9FB61bFlsjwB-SapRh4DFBPfYt6efFiv1x6HptsAfpeLUEdG2sfJjWGSVjPf0xteV1LmdDLEh2CnEiBUKsZp1FFpMQKWEHs-1AMktt2Ed0fMqeAtJzYnvv-puJzxF5g4vADTMzQR5vNDakk6qXLYXOgGiao1rKJDckWYgCRNOdn77fKgVGrVaqzP9OY_cKdQY2tYhLMNIMlQAwBYFhuJpjKj15dhbZr-W9LS6vhpnJdt4YeHYYEOYRNc2XhpiBzSFnKRBUmj4v_1crNz_NiQSDQljYE5-KXHqdhXAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DifBAQHvQot1pqIAC0rnsN6eQt9PrHSx7wX4aVXs1zEP44NqATgIzhGdeRoRwb6C_U8G3QWlkckMQmk0cuLusshsJRSXICRoB8MlrLsxBHcqL7co8zrWPbgDYTnu5fcwFyDZfh5LH-ct1mRTTyCJ3edFMd40k5ezryfgb9B-6B2vfxT3Pjg9oGjmwuRaMBRymkEjLV_Ju6fWlDLPboFjkz5gLSl5MJ4S47vyxQTa1nLYHO6vPIX-sfsX3e1SDJGvkibjfMVSYDSdpRfVCg9-49seacNLhDnisOP3PjwO-sfALY13jqeviczvRCcnaIdLGmdmlmW_P41GyPxDTTnp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B3oToLbE7R8H1Qb_BI39tP_-7iUVBmvKCpmwb7dCW5YAg-O4lJQOsrx3Ev1P1Df8ReIjMFllsSIx7VSZJ5X9VIu2D-XbLrXf3IVv2zX-KmPLC7c51bDW6b29Vxb-furfVSwcQkhTDmWvl83pn-4t2mm7EIIMBUbs5-TVn86whRZT063mNXpSxyloYyAYInoxIXgteGEb4wsfagoJzxpfXf0Qr5EcB86MxQXkGKEAlorneoS7bIPqhYKDO0lgKDsp9mO6_b8lmRMQR9hW_PwcabTOFhC0CLRZpsTszOXfwR1Q1aVvZ7cVjNmHPFM4-VNGvGzXpVN7DXAqHOvNLTQ93w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d7uuoOrUlSTyAhzmu8iEqZbzY_CSJuiJDWv-VJnOFX2fgs7BW9rFsvV1Z2b18lPtjRZLt6Y5GHp--SKTDYGNbjgtjTNYLUh5xZyu6r7JfBaOxrc4pzLXV7knjreMvMLL59_SEJliF2DjjGuT5GPU6N977Wf1wIbW9LbzFhG-C850msL6pRYFgYmlXrfy3sj-eWG1CBFslTNW2yg714A5wh7HU-d97vUxFdbz9Es9_BD6wKyjXFh3yofmeSqA1hyuW7HWhF3krslBhU4I2_8K98p7M3tnaOJaECuDoIc7V_QMnb8mHleLKFo3AvRIW5g7w7oomCmuhQzFzz2yjcT6JA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXxBz53jZobB5C7i2o1zKlc_YuVcylCrfUPtyYXRZJgTODGal_DiBUtzEz80cmEGIeiPHj39nJDxfvtwHqC-x_Sik3jZHnRph1R6WziEbJ2TCa8dqHp-2ujcNkrHB1MS2nZilZXU5Sz3ksJLcBCsQBrB5MS6Z3zGZQXG0gfxAAqVohg0ObPiD4_Xt5X-uGIu7hkRY_bURFk-hSzweGaBbqxWBcWTQaNraNYINoP5J9lOiX-Q8O-qDxDfO8iBtVkbPgPsCqpQV-B8DeuUMsQY0q3tRN-oRUAMvSqsVelK_h_PF3rhn73MqgZ7fMde60XUZhAql4yTFQCI5_uhNxBniQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyjeELC-FKng_hJrA0aSd4P5Mgt9qiyYRvK42i9RZH8V2sm5YrhDDOC4MkSA7Ixw-PDufbuSOITmV968kVWFaxHkZ9unnHN2zoIY1GfrGWkucFPYbX2jYGa1PdTy6PdJhrX12Hfyk_BpJ-4aFPW4n15TpisoDcRqwmOAbzgMA56P1fepIhLpAmmyH5cNro-dL37hYjqRlror6UG7kXFbnxJAxAMOogO09EUTcTyimB3kSGYyc1eSoXVZq4KgdQkSMMcmhbd738-M6otaoUGwx88DSdAjqLNkqwBbyj52sy9N0PYUmxVKhk35H2G7C-tTEHals3K46rDgP40SaBY3xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GrKPK5pLlR5SKT9iPGPl0aP86DI3sHM1GWj0SCuP7B1af163E071k0oYSYVte3mS5WckbcegGS9rVve5K8Zz57dHWxh3hpOQjQylSPkEYB0aumvUY9_8U8DIIufDq19sktHhV_6CNwlp6jpcybcmTI3Ysh98gFZ9njrR8KHGdOEsM_3rAqDxitAT8i9bTxDMbuWmntc6t4b-iGePn-j5ufMNK4IMeghbm2QXe3GB2kYB8CQV9ixxVzIqSGA3dRpT7rTV8l34SshxcvOGNL4f_7-GPkNScLEXFcBYRFLlNChOLbISXDyMvb4jG6jP5m32yV2eiRzZ2gHwEMW3SNxj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sH2keiFBTG5oXhEWf1W7V-6aKYxvcxUGjCiPX2fiRqdYxkAx9dwETtjBX0eEQ7pa1Lk3KQNk6mnuTpjuAOdmiHOVLlT_9afCSiLUu6Tul49lFv8UmXeEZCbH1E-8MXq-NZ_3thoRs3ZiR71KsFS6BkYwrxWVxp7tBuZsL1k01_4QMa4mNB5Mq6HeE_w0IfpNhzDHss46j5LuC64EfjXrpJEg_mE8GuR1kdHfuPN5YmUYV-EOKdVsMTmVCF1fjK_cvcaVXg70rz9sXvEdKz5G5wYoKJ2WP8V-HToak2pdlxxmZBQUtGRgo9S_ol7b-sOvNMIMDmW0e_kz37L7sNIsVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vaJIdgUI7RAI8iinnKE3Fxqq2VNCLHLdouF7z-nnCaokCgIuS43pz6WAiJSmz5HUQ9BsOTUEI2zBiyw9t8upNOBe8t1TJ1jvHIk7siWS0XQewHQcwnlkEYY6Y7bptCbJsDXlhEYMC2CRXmAiQ01taMnuIcShYre4VfBg2aCwL7DqWfSO4c17W0srnKKzL8sQ9sIPnydi-Rd7nMapKruKj94eLNXgW0P_NIMzNKtj2kA_prrs2_QV41gs0RhssO2OtP6VoVRPjeBPeLJeRx2VFJ6-bYy4xyu5nkAxJVOPT0qGjjNjhAd_9pqm9V9UlKzhEfWZ-G0YWtGAmnK-1Yo_Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UMVR2ciAM9navHq_D4fei8RzvnxY2OdiC_Mkn9PSTQbaJ7N_mdvX6mtFHcgg0qT8wyaeLfxlRNUGsdl5jDe_kkV2mGemianzqLtVtAEikrYoJy3o87dF7BLnrHmHIe_-_o0GJWtx2vQ2HDbcgpYwTYi7d2xt5tnYcY3jWHwc7Ul32wJIHpRDTlASF4iBfP---BLeq7o0nC_wvbZifbFUw2o9B7H7Y9zT2gMHROAI2W5o93ZeVSpncwr5-vPIN4nBHAM57k3OYecKbS4BJhVM2AhVPMhw60BkkuVQYUhRUVA6qzlVSyknaiep3cAIqoyVTl9m2kj5rYdmCHOUQKIw1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kpQp8xo67vbsV9BmP7sv47eav4-J0Qa3UjC8fUBAX5TlP_LgkF0UYAT7Iv68w-WSs2CiRC2qHusowcHM7112xnU2sKYZBhX9iIElh0hrLlXhPZ5H88zhHr61XhiBYunCMfTB1On9RlcTVovEqqDtW2RR32JhIqATY_Bd2BbsOLsddJd8GQEC2JgMvAP6FlKf9tCGeDLrAItbgtzBK1ANAFfHNxIJBA81tWCecySmh3-zgB49HxFTy1RWKBzrnsvNVu5Daw-OodHiGKYnhaRJEZB_uxSxO_vD3BtYr33CvlaqD48yqH55UxLzt-Xv_lcFq0wctp5FGDDmL2aLGUbZeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPmlFwd66YhN1unM0dr_CtxjrQV4wNObhOa0rFXlejsc9l0fUG9xulq72CWKoTnFmo6dZM74-c_tKG9vXRmPMGvEr8mHxg2P0o9UjzuqcdI_Qgya05196giFp82pEfz1ELUra3MjSVOewYfsz9wlpMeI4y8M7tZn82Nymgu6_eXjnhdAnrtF2iq8WPy5cy5OMBuqbEroOgD2NeG5zzaYYA0Mm4h1EmNqSc8RGG5TT8NfTQggT5vcSBssvBEZWCOTna82Lk-giPYPSKIbwIh_D3eBRiK20xJNpNRLL1DN8Nv7y5KLsnZc8jwFMZnufgZRK1gZiYh3VmVEaD97Rftqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jc0cZJjB7lQGDHMiy2_0kO9xixfQsFRn4rLYvqb5qwUsR_uEq2yWUr_D5-zszrr3TKt0aIMpHjlhrLYltj4v10FowkZgqdIUpZAQnEsRXulVhOAORWIl_5JI8SXsr4cXJKWn3tGuZDtdHltPffzob9iClv6yl_fftADzaJQ_lvVx2UV5eV7jjelRp85Npv_qneYZ2IiJUeSlQ9PqChizWJyjy-S5b8c6piXLtVmJTbmZ3muGLbe_VZtuB7BjOJZhuuM6TbMMb_tAPlI3eldE_L-vOzK6aGJpmXddcbIpEMY0FVliA8D5_onD7KdmEOSjxbxP132dhjCUjk10f6SGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dvr50_Tnq1RAxuzSUxUKC0QgQB3pr7lZylGaBMIBOZzm57PLhC-OTV6o6FzVfdu1uoH_txQHt5k3GmgKpW8LzV5hWBXR0NZQyq0GW3YjLmEV_bdg6IZnkGUXrG0kKq5yMxYNTs_XgA8Jlgh_mc7IgQziEJNbMUkV_wSffFU1HjHAwtG9uxYOuq4nGUgJdYqtyIPzeGmlbVRkiCzUdMVTybNJJp3tqJNerFsBqEMBOI8WMfXy-6vEFAvB23U3V64SwaSdXP3X94y2AkxTNA5d_oFf_0B08qoeCExNDYqZqaajSkl2b24BKDRyylhwL1A26cXcXJgHqYFczJ-iSsItvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JS9P8s2RZvXIhqtK4PXgh-b4nAxsPICzrSswMGCq1XksnvwjIfoLDt9gSwfoIl5RvHlmUhvVHZYJhCUtMsYSyKSpaD14_ZG-9mJ9YFaf5RpqZDOckMxV0XpO5FsQEjlc2Z3HLSxjhBQTDYOt5tW0KwBooyZamdwSfdZj-bghaHOuTp6cAVDL_QJeoXcZaoWwIGXOR2nn2r29N8vG6sgN9F8h__Z5P9w6QEGm5Y-KSyJBp37IWZ2Eo0ryZtdwNESYerFALkCGAmRcE431jyLdrlPlc_ALwmsuk4LcCTxO3GM90Bavu0edN8qFxK5Op0K_XESSp0e4hhmxAuj8mit9AA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IpFGimPc9R0LjGP1mO87ikOf7ue9-X26gk4Co9Z0KzElCi6-OXm_DzKm6fhwQtzHVJTLRwg5IQaghUWQsNR1yiO8nQiGAZ8VqOPT90RTnNftX1IwqaaZheWUC66QG7qh0Q1Qz5RZQNoN_oWWPojIl2IlTNSJYeIN740f5ehnDHLWMfVoAgXfuh6gsy2O9-UbVJQ-_FZEijHlBvQXC6hWm5gZ31HAWyjIPsWoGpAfX_yoNhBJB0OTrzpyfzlk1ZYkMT-arg0AHNsaMy3L_qbg9ofWtvGCyUkj9VueuGnkO_9nEE2EZXy1zkZRA8hlYN-zVaYHQueoGOshU7gJTvW8tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WG8GJYGqRezI5S3yVoCc6nkVsByNQ3HxmWfFUNJvsMqNntJh8dVWMgLkO5iP0yZCYua3Gf5bQANrAtUuo1d7cXyOeGAXy5hhB7mgii3QndYKk4OY4fr4RxmSX-VwBFkSSLhsAyh0IvkZkEH_Ol39mGzMYM_xJxKhg8qn920y5EmKeVphg2kuw9qsmAdxNh_Tvg4O8mN7a1MaZBTkhgbNbeIFhZPoVWww-f_sjaWp-V7DLiNniJZzjlbv1CPoQj8oIm2QuG6dGVp1tgzePPPZVrh89KM3hwc77M7RMVPro4p3eKIXSsp0gEJPrZ2KXdgE-EfvenDbY_4hVybv7aZ5EA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nH3uYNNA4ZCdQwFhHOmpVKYCJtvd0bFYuba1Ik13Fkh6-DW2ROcq837pwqjSnYHnTbaueG6qDRVyWyUemX952p5qPM7lGu0eCy1VPWeBlfQhkml0NPrj-CQ7MlyhHroxBdtlBiMiEKnDIdQfzEdYVJEB8SbgMMNGdGaj9cHOrKs-BO-fUaYKe_S7ajiqaGiMz3DxZ1Jd8xNNQi4_kE4qVPbBWdgYg-lBCumClhCyl7L4EGWzz4CHnofBu0HUvBQZxaPeGwDEQrsxMJOlpS-cd7xG8UK_DtB6vSy21aSwPRdvJJNd6GH9vwZqkzajEZ19jDTNUVZjpzl7vwqU21GtZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sAp4JCIItCjKhA0GO0CAN2bbjtu8l_RG42SSlHzFU0OZATJKFqDnOf3RHYfeyATSrHeW6pAKgVkSBFTwDAzLnZpeotpgm0IkgfeK7FVsZRtNrWploDHRZeVB8gWw_86V1NPgYTZ45UFZqePkBC5jak719QKMLzCgqJciIKLRTZSs7FNhZKFnlozUA3BMZ7wMKKzbWebP6uDkwD9_RCIK9K0v1QguglvZVVHdMzv4wNoeHZgo5F58Jreq2Tid5QbtN7rA1tAWu-OdB1QlPJD63gncR-mPIb8nnukt-wj3yR8XvbQKMKsCATWP0mNWqH9IZNmTcTnD8Nezlbftago09A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kn5t0P6ODEMtuyYhM0aqey1sG-nc-lnJfWX9TRWdqZJtBChf8GjXMWkYY_JRB6KsK5HhGaZ6KjkYPn2hhp8fZXJvMKQouWoiO3MgdnGYXJ4Kh5tLFJbKG1PVhkHF4gbwnOLsOaoPp26cPREz8x_5_WwZ7MHU5a5HqcMKrrtAryMhCFcBfz8nw0l69ft3HyTHi_C9NexDpiwTDmDPQSK_2bkkXFWq0g4wyeGdfMmstwh33fo-E6cB4p5s6t-S0FffoazCf5A67dUt4ZTp5s3LsXH17N8YEH_THprpJLzLkcCh6tSm0w8AqIFIrqE6monaGiUNB4nbQZ-vtLOj2OFxHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkMXWvgiMsCnX6J6qyCrwp3epTV9IhyNZeuXpF8_XbagnAKCNMYh1C8cmyTf7OaK9T_2mDA0BxJye_IbJ-h3btQEd7q1KjnrVmunlEuASRoY8cb2JyqwqufzUz9A5kJr2KsdI1i5wlW1FmIrEBNr4aGXsZ5SXcTlCdPcV3PEOiVZf0edl-NuO1P4VNJ3NfPY-EgAtH6CUAEHPOwyDyP7ntp56ti3E7ckgDtqUrgJZ5_Tn1uMAAILXofoSlW36J13a8v6zSNzRKj9t1lIYob_Llh6brLSce09AHKypF7qpIy1yDfEQbbYspBucCe-PrvykMltKedd6S8JvhnHrYHDJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n6lvqwWM_09SvYHGm-rh43ZDcxTbquOdgT4ZoJbHuC0IrtF4DhjGBi6Bp2qL2aX71ATiqr100xuBtpxNgofnIUPjC9sNdP3ZE6YjwcdnrFAO6BGQhl3NxWs6I9fBTlGeUtlRGXWP2Y51OKYpt-Jp0yEBzwlKKU7i9JeO_hjkl-QHklCjDnPQgzhTBxwTjVWB20kxH33w7QEV9pVyAqutWrZOJ1xaNvOkg4O3eXnvQ77OUP30sA11F2RvQduVhgsGxo9M8UQTLKNtgYwLE3gEPqaCAt2dKj_B9h6x_p7cRFi3hwun-3egHhznalhs4vP3aLxZTfg19sCgwDZm5ZHm5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cJgvU0vqvzA8K0ZaIDNPjyUAeDVNRiTPKlygp-JsomI-MZpEUX_gb9CG1sPr4zFtR7oYZfeahy3QSzS4WxO9vIsVOFzzJXoUEQzx6oC3NtNGTS_ZZqQ80RIcUVAK76sMG-E-0xaZAvz4t3kIzednMlINFCRzLMja_zlE4aHCRhXRuo_EGRDLVPRPrwAVKOnE356LEylP-I-QDktFWATgU6NNGKeTgJsnW65WAYSFnrVKVbOF0nLmpmZowyQXnBecC4bxb-fvlM9lkmRdr51DeecRxhaL_xZZVrh_6VT0Cf0D25MydFIRD2PRly4iABliioKCzZzeqK9KDe_f_tb8BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MwQds1C_k4sRZt6sgxlXJECYAFe85V6zmQj6TJXUmYG8STouWJxhwZx3SW_oPlM8dv-5VpauATh8A62Y9Wu9aDGgdXYnD37xEk3UTUhxloj9uY3MWCXLACd8UXmxtgX583-dkaB1rjrvZV3eEQtCSTRrnkICFY2ilwBLpU5l1gt2EtP5rsLnVdGxJ4cDnCLd51X2390rf5FHSKIcHh3aZgLhfKELgDNTDgJIENRWjnpXl6KGvvHFBqq6d5G0P9kv1u5hhNxFyb3wl6b0lGWfkuEGX_fBNABePVMJAZrJoCnfrZQuWgaNxL4JE8XXVqka2FkMkSHSLq5tLnAY0Y0idQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arGly6JnpYBf0HLqPfnRaGpO-Hnika0iJ6OxJEb6VI0Imp41zHE8RpjsHTedjKACEq4042psbRROQi_1yXh5H10DdnfekkW4SXRCQzmVDyjDgU6eobn9g2eYXJJ38iOs0e_CcPR0fjyy3nkhT8ISHQ4nvdzKv62zPQYs3385TByfrohiqXkZ77gyhs9h2pKGvgb12Ed9odI-OcYM0G0_5QMs-7hmEvzgjajkkEeApDC-i56Gdu3X5MRUINsDrzkcvldsXNbYElKyG2i4FPNq6iKawCV3i585Lkcoz0VpcqIcmOF20zWDM0Wb2s9KGuloDZZaEj0Qu1c2r91n0uj-zw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t8gDPTDpOx09sIpxiaZu5R5xnaUE48Lm59cXI7p-h8QHac9KrtrVuwWRMsm5_NxJx8Ygmm4ZEYlj-xbaPdX0HMilxcqUciTv4fPvu8Ukkf5Vl_aE7vJlWOr1WCqPFvam_klJwEkeVELL3gjLwVopBUhB0wl4jAnJrjypFnWIAdWbQpM3NW5tjDn5jEBHmkKrB_1mQoyP4qYSgk62-4XFAVWuorVPwFFtehCnig1d9ThZfdcs8A2yt2rDJUr5BV2h6bLrEs-0OkiosT1hQ416J6GGSGcCB0YN0JU8uYu36mkolLBJ3WsbTR4P9qNvc_-L3DvGjJLEL247StE4rzaDqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bMStX9f00jjx4HwwT-crbvP07TlkVYDzYgnv8LcdmG-_bZP0G4IC2SzlXzdJ4c6CzGZlf0Cv1bQSDDllMwBc_sqOkq1n1Pyz1Q-BUocrHNVKaJceSrTEujicM_rVt4MmBdkZ6uxAM5U5yZUPZE9kb4K6GGy0rOeWN3oBFkDL7Fm7eGVqnhQVc-98eT-VhwmroQ1gU4Fh7ue_ndFAUUAI-RVeoID3XZsKd6HYuPnEP5Rpx-WUQyKOJ2XInpMXupJkQxGY6DuDuuQko7p2gS4joXVDpovvnRNFkc8vITlw4vVIITdAsAtMCjVvYKBwcSa1VzXoULVZ4vX1FpBeZPP7bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1yGlA0tsTujfMVfL2EBUxwoF_nXyPoMC3IOfOaaR1HCtm1qPmY6Xm8DBFXGcsrljZL_vAXGYx7g433PXwjpVxwzfF9XfilKmHqlFMVmQOqFLSLfZ0FC8CqnmXtOS8-nC4HafGFQYbXCdiGhn0mro6Vw71vweCuh7jaahXSyf1RA6AopF0M75OKC6Tkgdgk6CclFhg1LOrV0p5cRNGJ6ZNM6PMXz2ZExBihNZbHAPa_3UZlXm_PMtk4Rq3pV5-Z8kx61b8cxNDZl0uxkXyELfEIoWL6aICXgnDYvHY_V-zJ7NG-HxTusoW9wf_UxMK7HNqzFYeEQ9UpScrZg_16qxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VJZCBuZej5J1ynJLiGeZ6x9r2eCEf-F2AuxfHAnuDLKgbcc7OKZJ1b8nHgi_ApYW3vEYyARbqhRWtvzkAWVMRcU7kX_VyMtdfHeXhKJL_Sw9e2QL-Tek89Xn5yqMxCvS7fPgGoWRYV-9rxeDVHhGdODSZmmdeg87jChxmXANuvaTAnWtfj4mVrIh3vUdC-TwKNdtyw04Vp2NQWKwJSlw0i7389-G8TnX0b7WAj2ii09zckG0j0wGsOpUdc21CXLQvdObPMDpIuMSLBoF6cKES9Xsvw-8hdnXXCUi3vCMNHwW4EYvb2Wgx1t7Uwsbj2uGU-gCPGclshmKbEfnVZd9JQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=HpYRk9jIv5Zuz_hkfiMGFgnYiNvJK_zdJbJssso8aoKDYLULoA4RZB7djVRzQZOlyHUs8TpplFFEohDeThQ0Zk2H3iGS_qiaVHRIpIqqXgYJ_iv67WbZcO_0fB6kyANnJAh3lBbpiWPyrTkxpzxoLIzKB-HX_wmaiHONuqroeg-BhU2REZdd6jlUyHYetl6DN0J1MwkDBhTXAwMqtazUDxpXc-bBOtTINgbawbi75buDApucy3K1hzmKbaE6LBlDB7Phlf4IEz4K0_65ENqPLymx117Y5igonqqlMmlN7lPkVCg_bqxKJ7gBnbf_Tl_-F-T_RaQtWYTfeZXE0K-j3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=HpYRk9jIv5Zuz_hkfiMGFgnYiNvJK_zdJbJssso8aoKDYLULoA4RZB7djVRzQZOlyHUs8TpplFFEohDeThQ0Zk2H3iGS_qiaVHRIpIqqXgYJ_iv67WbZcO_0fB6kyANnJAh3lBbpiWPyrTkxpzxoLIzKB-HX_wmaiHONuqroeg-BhU2REZdd6jlUyHYetl6DN0J1MwkDBhTXAwMqtazUDxpXc-bBOtTINgbawbi75buDApucy3K1hzmKbaE6LBlDB7Phlf4IEz4K0_65ENqPLymx117Y5igonqqlMmlN7lPkVCg_bqxKJ7gBnbf_Tl_-F-T_RaQtWYTfeZXE0K-j3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/drRSgWNCsuDyq24rnEIKnAblIGv0nw6fVceoLAjDjY41xq180k8gwgxVoreqfO3qOUGzglh2jr_DjkbWWkevTzv_3Q6VEK1IWyH25g-7RoBKoD-61T0tPV5_pvlGIJMS6HEINKH0dyhOb3E-M2uufhUcDkWB_khF7s-4jYjss_avFcKyKuLVbRoUKEH6WFnyxz7p8XY8eDvscmjPNlBuQxjYpznZOj-m5KgCKuIv7-0Eysu3lIMxK8GcFNu6_xvxig7JecY_7naPy6iDQzuCappRXtKFjjbe85qIv5Pj2sOJfoVkZKCRyPQYWv-D_Co5eq2t8fC7MBw_u0snUL3fCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CO2w7jBmkKcB6l_eAb454ACrop1mACYNUUwthw8BeVeMYeBVG5hw7EbwPr3VJ0YZTOQcULBBFbY33_ol80NtWQLcrvuhkZd1vB-454vfmn9j6Z7pNDc00PYvqH4Pd8WLZyHjiC3f4Z1_RVf4PasNm3hE9FwzQ6mTB3lq8tFV0XlKgfwP9K0oPOKtIE4rE5OaPgW0hBRpXQJjzI4v5QzDYnDnLNVgvIQ1hMqsc6URGYV3UoQPSbPk-EO2EHL42pnmsdqRfKwy-5urs0-qu8TV-Se9t58HnaJSROdPp7oCqR3u2AJNg3rfLdbGMWx4kQsM10qNyvv8_9OWtK-N0Wqetg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zxgcwe0ify3ZhCemSA6kEPZxN3CVxYPePyYuHV9fecFmeoLbKUtDEQu5Lk3utjqKVd9MIDsQOdUtZli8zengW3hO_bMzyzRpaatSF1pKU0_sy-efSejnIotLHSJVVhooEQZEZSDQvCbSMUHzxgBP_l4WdQwudfc8LBkjHZEeMp4wAzjxbY1aPpskJeUnJ36elIOOYAQC6YXSEFWEgMhFV3Ksw2bpVOdsz6oC_9IHzAl2zF8A_1msvU2_a05cSrd3FeTdMHxpFymgNLeHRIk6AjGprgOgsLZUExv6SpOS-cnd59XIl3F9RpzX2KOldrj4fUjDEgexpcgvHtu8BR-GZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZ3dOoRFD8wEQphDmjfsGP8G0Zy8ILuKeisXwXmWIr9x9YXmV4c1P56xjt6k6ruAzT77jGF89d6LC7h1d9hTExlODTJc3sRbVJbdpYiTDQWSf4fBnoLFSVb78ICEA29lXxGldylrJuxc7_l_HC16CUdNNCqXpkb8hogtYuqs6hAcGKjn1xIpMCg91Ohr2cxIjLoo68tdM4QpNfBwDsJTTsrPdMTfBFKXK6Xnzl9j4NZWwvbtqMcSicotdvHz1-Lqn8kVT1KTOqOGTOB4vpLocAFt4Dv1CcArcAx3IXcKzhOa_TUWyF9WUNVKFcBRshJYF3EzEd7Tw3LN4fYad6xPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MpZqndNQaaTrpisJGs_TczoEkaUyvg7OsCBkwEGng7mhiVqYgxNmJ4RtQgO-mhWsWn84v_2hgKuGWWVqRcEMHc2xYz4pWe3e0wioFroCciRtsl4eeKcrV526OiYY7MUaEJUQAU8dsWtPnKbkE0pztngUmfN2NVTwwI2pVJ0d6OjKUFWBkkcIJHICGbtg83ToI0dIKHh9AFkCu_dAWITXGn0FO6WXcGz3IWfpoAVZXXXOVXPr9s-k1ECa6NCS-rr263eKx8oBsLiohQlgYvR2MM8FbTJMZce7hbLx8NaOsB0bH1Dvh-BA-ew4CpJqJcyYu9Uo5UphrNKcw1V2xva0LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjgElsFMJfB0pQ3QPz7lBMki91j3mSk99-cFCvi3T9G5VzfY8_N1pFyUbY8kDCEPV7elhKJSRniEHjkwuEmPQnCZgk9FNctBnazX9LK3Eh8lgD6-2d8M5lJi-bx21OafFnPQaLkK65gveitzfPq1AoQ2hsjda8beDTOotzlrRv49i0gEwYDJvwCRwMX_vHIjJHj-Bw841gDTrSzJUB1R10DuRZP9Kh31glrpqMkhMtVWenFvWGGuhbBM02qwpmgqf7YXlgXW8wo8HrZSbgYxdOYd_0JNUE5FOS5G_7asPr1GvAtNY86-mgQCJcJ9QvSPHEkqlb95J0oJ8Uz44Kak6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gfUdPAYRs6ac0DGi9WNYtu7CGscdlzlojlvouTtj4ZpjM_tPPDa0PmLd-RDzhTidCqsOsSlW-YINR_dGpijZzWUET-OJGg09_xwlWhOqHqvx4XVH1qF2JXgRoNu8azoaNL2UaYLceqpwgo2CqFFTo6n-5DL_ZqJisAuJzsaep8mW94ScDhGNHE0cRywqJpsh8VIGmRr3wi8Ml9DH8FCFxZQ7iDZOutJaNtTmGHs0YaPeZbvdP--EE0p-VQyer0osLklSPBI91N_5aFtpdG-ahxOi6bQYvF1tDdlN-kkjPTX2N5IzA42aram2fCLCRlxYGGsO32C8tsZJbaxH1RxZog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UivqhnMfrYJSeKMtJ36AnIkxrzs-YlkgOF8zus9-BIqyizbtGs-etz5jJGs9_G5CILR2Hcp2oJ8Ior-IQI3hZEBeVPsbj2MBdoB2WJxwpfOm8US_Zs7YnPidPsS4N-QoasTpKQ84BEJJ2k6-gm4IEsf9a2BAEjUFwobqaXjgQpv91LcfBD6mmC_Zhtff7hrOUgzH3Hw-z8LUPyO9lFm_6ySRC5DYwNMLDTrpFPNYy7mJJH79BK9ITB4Leh1JDmWL8zAGu_8jfprahHXmm8fUV4m22bDuyxC47gmarZ4q8VxpccFdjyOLT05CIId7LfXBLWRnJMpzqVAfyALpb7gEUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HelvywsDVAD8qhEL94si5a2xDZpT7EcZdN1wik_7XDlK89PQYNhaebrRIJHKUatu6zzh4uk3g58vtDIjPNEdH4viMQYdNmTQ3fOk67schRfnj-FPOTQyEIdzADSj4RHq650KwH4ohVyJl_wfpX0RbVKT3MUrNsncu_rdP-Cyde0DqrxmuKRGzegknbUv2UOR0w1Ha9Zd7lyBaxPYUbLXpfgHs9UrUE6-FHUM1aZ6dTfuMODlBvQXHKMCM6sd34Qr_9wKgR5RcDMAN6LwK37x9qPaFUhUOtwSKH9wGv7M7AF8_17UI90ji00Ge7bzrU24QzFR4Wq6hx39_FHEr9ZA_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQ0eCusktSIVif5LAl2hg8DKmQg_L5_W4aqfdvjKPAuNL1UajG3gIVUEJFQAV1oI3u6h8Xa0zs_V3ikknZPbVZc-BvNpySpJ794YDsgaxPFDEZqebombI2KRbscY8LV-_-0f9oKZ3obv49W1uWJhRf8k_J5tr4m9ksgKFjbXmqi7Ufg7I1crKOWcZgRhnLqS0HIx9UWO5LDozpxFwy4PrYU8kRp0koZwwBoCk2gcU9cMPwv0WEBdcaDqohiwyvPK9wIEEvZ9TrEf8QLp3cRXHoZftFd-GYYmyRfz1JwjcVmQtEgzPzEv33dSx97RNijPBhY3OJVSG1abCm8VpCEssw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MMu1ZxTuL00oJbukHVGrA40-z5WcisQEysLb8aDTLCkQv0143QsxAaX2JxDWe4XPEY5444Rl7go8-_U7uVTVb-ELZ0xJ5vFwEPWjAp1r6e_Y2acjy3tPe2X-vpTi3Scd2oGUpmd1quaVHTNNginPlBMglUzfqj1iO9fzQLara31RITQ7B_toTx6r-deRZ-nLU9RuHideywX0d1XrdkNSapU1xUesYC0-DgwLBDD2lyo9OwtMPjo3iCckVI3GJXS5sKTDAnnIbZo6EBxVerbGwhYEQlbyXjmNdix3fiZvAkYTCsjsb6-ZBriERUsKEu2A6IJem3Fsxr5x7gk9R2IPXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LaxoBOMXR29UMzBgRy-f17YNV5TTvffx1omHShfwUPnTkIQA6ZFVH3PMC4nOwM2kT4P9x3YYjoIVt4Tg72xMo1Z3MaLLbWnOUrxTiK5UdmrIbZfUcMq-7Gua5B2PfmQ5wwhLIcyx1Ow-FcyRT6cpeINyWr9kF9gF-znR84Ql-kjgQpHziaF1ZN68_9xiG_dG9i0r61yPcDlTFgaYYP_zHHEWqkqjQ1g1mNsaZA_GPKfmiPdlXVtszSKyw1Kq9oodA13v3q3xFzvIQr9QPkLNlAxyfjpTnULTHuAvxmGm1aUAlA4gBwzQZy0t8FDlyifnefzJav3dHvj34yTfpTGyfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fqH6z_aXK-GOU2qvqWJshdQuXpntI0X6DuVjLfsM6Y63xk6Old-94f9-Ritn0xnv8yXmZWBJly76XbtpBPsfDWub9Jw09GmRQlyprkZkz53ovWSf_Az5Vb1QIEEVGiP5Fc9848pg-a3Xv2bykUX8Z75y5szBpGboy40l-kYDXvaVH-PyRUnK4BJfDpwwKSBhA5on34-JJSwrFbwnfcqY-v4TnYA7Ra80XKdkdPNiMutB9xvl9-1SXQ8b29k3_F3oXbeiB6jTpYVeGI7l75KWrFxMNIEmI0FfNOU1JNpVJiZgWZY-LYo-8ku9r7FzogkrmmETQ3gHSIdr3tD8PS2b3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3AVzLMQuBxem8w9xiGNqR_jNNfof5o_O2hLOKZ4biuJj43y29dO9-C6cnkrxksbenZJUCKZ4nWBctyHRQYrv-KLB0bVnV2_J41YLFEon1mkYLTzBJYnhdOOXJ3QSkCXj9bxitFzLdr_CTVXAEpcEfydLxZ5XV26DRRjbVVElbtecuL1vYYoPlQFS_6JnBSVC9YZoJIKn3henSyO-i6uPQm35dqGYixm5jawisvf4xTVlN8DffclZres0EOXbRNVF2WlK1cRNlAX7HaYI6IAHSRAZud6jlrgYd4FqTX9kf_B7zZ2--MNgSGrViBGgW8IlrBMImZmXNWq_mxpS2YVVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IN43TKJWOwjyiQS2jMCxAvoz98mVEk6wFnFOLLnE0vqJEPLpAR0kdlx81RKkHzw2TJKG5u9apo7up3UNo3QKxM4BjPva-dvnzB8k0QBwj6FW6tPcFxBl_NMAZ6f0-_UWl767MYI-GDYvLwlsRfC9-2I65rcLb7Eg7swxQIdZDz4ro3TU9ZYZAJ7ntd5b7xAnWSGj3iawASuybAeJ6pUrzg5WAAUzavJac4PIFo1rcw2L1UrLtZC_0iGwsLABqF5xONOutszpf4Y-ST3r53xOEAmXQfzyCXc8dCxKZdxG3gBZKcdwqiSJ6rzt3YEsP4g3_bj4HHpCYmgLujxraN2CAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ovtTKYIIFnCR1H05zkV3xtCJDL6tRLPy4px80hzt3u9SqHtwuGDv6BTG_Ju-J1C8hCjZGXBA3qdC4-swwFSioeQdeocy_kN0WmRYzcKUeIt56bk6-Y2NREG3MRq3k7qijHU8vzMdRrfV6_VPTN9c2EuPEtSnY310ufH-xoy2jYG2gfE6LzHZ9x6wKqWQj_w2dJ_ROlyKOUNRbXZT2Gt20YnXXqa9a-ganRp0rU_fpzObTstoEMSk8JGXGa2jObshF6ziQkSs8dWzoe2jgN9_UkxKSTsXpC22RWlycaTE39mkQG5xORgEzw5XMtwnWfHdz9IhAxhi1lPFB3TI9l9lOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GdJVRSrKCqt_RGWxjrj8ionYv0vhRkXf-Ioo_MloV47nJzAR7InuksqDKJZNxSBqL5fQIlLWLyDZdcRM5AGbw6ITXGh0J3HCkSUHlhJl_b9R7I9Sxzy77x6jzoAFqaBh0PzcvLsOxP4V62vZqS9TwocD1DUM_xGuPpdDZVAKHKTmoyAyZmBLxXJPvURAOulU0ZKGZuOED0nGJDbf3Eon6WKpr-UsTqqDN8rVb3PuSamaV_l3swXNMy60sO6yehpRRNY2F5c-f0CVpT3P6IElNrqrUEmBfHGfQ6WDg53YGTxyr_L1I6UZaAJEke2lcmTbKhw2GT_Jg-kaOYsWyIb8dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WCI604_Zl7v-F4zEYPhIKZPKWC16XLuOQSClaU-9F74_ZdUYFQ5V_zomxul_QPuNAPmPeask_1FuCy9bMa7BMheU5Q7K7Mt0XkEHfjOTNuc4fmt_uIlk3vK6t2-0rB0IRVkdO4O8fwCkUaFaIuPn4LtvYNSyvK_eqRbI1tTdwPzwiEnQ9GihuN9zP293SSoTAYw0BAtpzC8dyL01Md7lDC-RqGT_9vIGgORFHbpv45WESvoQCDJE4iff3UOSUpenHa5YHXsCMepIhe2xfOpa29EFub1VvCXu_Oc08u1c3_fkzNo-ldVKR_wMT1CqNnkfE3-ADOMWPamGcwDyooCVXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RFSkPw9XDSenXtSx1GvIqNE5Q4wRAJUztoAKAYk7DVos_JMxuPknJVYNXAhrraxdKjYgRx5AvNWQVrpodU0EDlFIAfKa1AEQL3qbo1avnuwylDe6LWwEGaMeWd86U4wbnq9S1Ml9JSDu0MHUytqzp80sB6kDlJrdZ_EH9qo4DtWirjM2RnszhN-OXU-6qqjmpPlKTQsFnOqTo0pPKxv2e_i3mOFKQShA5SSavY90IbsZ_a-pTepEdga2RDwS3pj6H-3_lS6eAeU6QBZHWLxCNLCY0wZF0Ivatg71d2dGmTHITzKUvY3jNdSYgofyyIjzSfuddkXYzEBtFL8P7mf0IQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hu4JzsheODAT5b45NSAat7yZYuwk1h0q95wolRc95mKIYlGAIMInrEGsFAYiSg1ABMN1toshdTp-W7kCX8PNtVhVR5rySfIAwVWJLTEfbJf56C26ihQy5XTF6N1F1kwalQb7KFODVtvxXa1BCfJ7Fwd1dKdGwS0CyQ1pZVhGKsVLWVMU82mtm9KFtdi_rRqW0oUd7AGsn_IdCAQdFygxe8K3x1xr3b_QvVy25mWcTWg2KcLi7XksYejKMi1fs-2KJFSnWMaL3i1LQi3TbLer4zk9Vgd-5UmxgVb9mhBG44_fzij09O7RKPkIrg-mgy8jsPreMOuBlMLOwNCRTnRFIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NjpTEzWf_RYfSqsYUlIO709f7am_ep8xCLrOYxcnpy_3gsWJDad8Pc5cpz2iLV-qQNUJKAE501pPJxtzJfwpUT0U8AStuzd2sXYcyzAaHv6gFJtof51_X9A4y6lyjiqOFH68bDL-QaQ6s9TPXEZjDgkVIKzvj_aW3CnjKR5RrRPgYq8DuVuQE94z7iNTa8upDGG_C5HC3QrJuBcvHjpi9LlsX6VajEMzGLOb2e58h-fQtPYV1zDaxH1KCBe0KWPt3AIQ_N7Jx6D6aIHlL11yIMBxKvxeUri8H6jftBgrBxeOrHrL1FW5IoXOdzy4ZOr6lZGdV9LERwenD3zzoWEEQQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-8vfqNBB3Os-QnD5sIk81Y4jOzWzuoV0vWKHy16DbDINiRiKOJItx6Kbzhk9tnIUTcdyc5cPqRJnlihSctGlxRURMG5jWKWjUnm-GNu1XesXSOakkIyDeu4OpVyIDM1MnUP9jr-wwpfQrKSAnXx2KPXvjibXUOIYumoN0dwZNXYJxLG3v6TdT8qR3Udpva8R6XvSoFIE7TFT6Hije6uzETD00zVIXzT0mYXVvKSrl5MfXMVDKnM6h8s08Pv3U4vn9cp-4IBMaKsitfbNyA9Uk1nHwK_dTijijqorBlJfNFKfoTyWgAR9Brp1Bn5pFoJ6qxWjDzO7PhXxtBZpKRJtw.jpg" alt="photo" loading="lazy"/></div>
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
