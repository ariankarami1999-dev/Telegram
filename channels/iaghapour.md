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
<img src="https://cdn4.telesco.pe/file/llTapAJvu1CWEBsoV0WRxbHkafeUj84oSOg-jeajbaZwKjtl1a0ByQX6RsmbYVa6sRjqMJe4B64xJiXFX7sZy-zBaAQ0jiXUgL6zaag4-7C7zqTx_FniQe0NgPEtY30ml6QXol8L2CWrcyNNYyO_tLPSL3gXogkHXcds5t8A1q6ZAPZUchML17cXJwhiMVRGwNnAigfVOn8QItyzOOF5viGNXDSg3lMzZr0BdUzco_qBabMYc0bymbGU4gbbccZpjHe4gOzJv-5oDEDKdQefY7e41VFHfkoOJ2W6DaRpm-2mLwsW5c677VdJ-9knzB-SBCYpMK06OPdoYGNr1SdRGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c53b317c.mp4?token=FL3i9_B1eWKhxtdUkFKfNR6ylARzU1WrGo0JhIYuZAv1VtRnMVoRdMFmFbyPb45WXgzTfQL8jC5RxKCyic7tWGI8mkFfiP9GDK0mXLUNej1VXmVoEEuTNPNtkK1DmeiJh89hdlqxZoaCWvNe_nhxRie8WsIdmfky8A13ifyQ0BG2YYdNnWuA_3-KgsrRjxEvvtdOrm3EiCmmUjQXX5tO0tpSwO7GF1BJq1cv47hTyalA5KJupr1R5DEaSaNqghXYMINZ8aoEgEcXTYXNQ533_hQdcL-VmsFVms5L8qzHi09vgcDhxObRtLaP8zqx9p-kOmfGrQAvRMhoKUIFSgg9tU4AqqvH_1Y-AZ4gqi5CS9smZ0HfGph8mrRSad8akmCgJJR6omD0zaKee2_uDJFE9ucol_lkbV8f_fK-R7OhVB7yZJCEqaJrY7DpqSs0Wy8BJuydgVAqCDVSFymaKIn4ubZihAe_BIRLDTS8jtjmuvKzKke2T24GQTZ0kwtJvvgYFlSVyag_iBUTAsr2LotkmypXZhOQqeDIdClYuWhd4TN-lLnCGch2pBrfkwJW2FgPB5ypdTK8F-VsX3nTeULucHBB58XZRXeuivy6pmTFFoMlat_O5MNU5WiTK83iyNtNyzfmouhjtYLejnaWwKlE1IX0k55sZpTNF2hLaZVvxI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c53b317c.mp4?token=FL3i9_B1eWKhxtdUkFKfNR6ylARzU1WrGo0JhIYuZAv1VtRnMVoRdMFmFbyPb45WXgzTfQL8jC5RxKCyic7tWGI8mkFfiP9GDK0mXLUNej1VXmVoEEuTNPNtkK1DmeiJh89hdlqxZoaCWvNe_nhxRie8WsIdmfky8A13ifyQ0BG2YYdNnWuA_3-KgsrRjxEvvtdOrm3EiCmmUjQXX5tO0tpSwO7GF1BJq1cv47hTyalA5KJupr1R5DEaSaNqghXYMINZ8aoEgEcXTYXNQ533_hQdcL-VmsFVms5L8qzHi09vgcDhxObRtLaP8zqx9p-kOmfGrQAvRMhoKUIFSgg9tU4AqqvH_1Y-AZ4gqi5CS9smZ0HfGph8mrRSad8akmCgJJR6omD0zaKee2_uDJFE9ucol_lkbV8f_fK-R7OhVB7yZJCEqaJrY7DpqSs0Wy8BJuydgVAqCDVSFymaKIn4ubZihAe_BIRLDTS8jtjmuvKzKke2T24GQTZ0kwtJvvgYFlSVyag_iBUTAsr2LotkmypXZhOQqeDIdClYuWhd4TN-lLnCGch2pBrfkwJW2FgPB5ypdTK8F-VsX3nTeULucHBB58XZRXeuivy6pmTFFoMlat_O5MNU5WiTK83iyNtNyzfmouhjtYLejnaWwKlE1IX0k55sZpTNF2hLaZVvxI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📸
اسنپ‌شات (Snapshot) سرور در دوپراکس
🔸
اسنپ‌شات در دوپراکس چه فرقی با بکاپ‌های معمولی داره؟ اسنپ‌شات در واقع یک تصویر و کپی کامل و لحظه‌ای از کل سیستم‌عامل، فایل‌ها و کانفیگ‌های سرور شما می‌گیره تا بتونید از اون برای ساخت یک
سرور کاملاً جدید
استفاده کنید!
📝
کاربردهای اسنپ‌شات برای ما:
🔸
کلون کردن سرور (کپی‌برداری):
فرض کنید روی یک سرور، پنل و تمام تنظیمات تانل رو با دقت انجام دادید. با گرفتن اسنپ‌شات، می‌تونید در چند ثانیه چندین سرور جدید (VM) دقیقاً با همون تنظیمات و بدون نیاز به نصب مجدد بسازید.
🔹
نجات در شرایط بحرانی:
اگه سرور اصلی شما به هر دلیلی کلاً از کار افتاد یا آی‌پی اون مسدود شد، جای نگرانی نیست؛ با اسنپ‌شاتی که از قبل گرفتید، همون سرور رو روی یک ماشین مجازی جدید بالا میارید و فقط آی‌پی جدید رو جایگزین می‌کنید.
🔸
تست امن:
می‌تونید از سرور فعال خودتون اسنپ‌شات بگیرید، اون رو روی یک سرور جدید ریستور کنید و تغییرات یا آپدیت‌های جدید (مثل نصب نسخه‌های جدید پنل‌ها) رو اول اونجا تست کنید تا سرور اصلی مختل نشه.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/iaghapour/3122" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-aZMybPMGj028JEJibRf4MTa4mdJ6rbu51IRRR2dHKDnaop_4mpryVyDxtbAQg_8PE-2DC_ypngXkt6BcgoJ_PLw3na34m2Ve6U1xMiumeqPtjhNt0vxe5C79sG_IdlK25WZ5tnIbi2GiL_vQitr7g6cXyEr71TZP8k40jt1SC35wL8cTpBLG0cRMDnu048A1iSaPritymyAqliRgIR7l1vndseglbasacbw-TeQ1lmCUgT19gjbAMzxc-p_gaOkDuACyG0BWi_MlicfyuiPgIVeWLFUv8DTVCpPjCrRbbkqRvMO08KKZJoc0IyFB-neHkpFsvZPjV96ijDzJzE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
بانک مرکزی دسترسی ۵ صرافی رمزارزی به تسویه ریالی را محدود کرد
با دستور بانک مرکزی، دسترسی ۵ پلتفرم رمزارزی داخلی به خدمات برداشت غیرحضوری بانکی به مدت
۳ روز
محدود شد؛ تصمیمی که تسویه و واریز ریالی به حساب کاربران را با تأخیر روبه‌رو می‌کند.
🔹
صرافی‌های درگیر:
پلتفرم‌های بزرگی از جمله نوبیتکس و بیت‌پین این موضوع را تأیید کرده‌اند.
🔹
وضعیت دارایی‌های کریپتویی:
موجودی رمزارزها، معاملات داخلی بازار و امکان برداشت رمزارزی (انتقال به ولت شخصی)
هیچ مشکلی ندارد
و این محدودیت صرفاً مسیر تسویه بانکی ریال را هدف قرار داده است.
🔸
مدت و شرایط بازگشت:
محدودیت ۳ روزه است، اما با توجه به حجم درخواست‌های انباشته‌شده، تسویه کامل مبالغ ریالی پس از این دوره نیز ممکن است زمان‌بر باشد.
🔹
علت اختلافات:
طبق گزارش‌ها، بخشی از فشارها به اختلاف‌نظر پیرامون نحوه دسترسی نهادها به داده‌های کاربران، حریم خصوصی و ساعات فعالیت بازار بازمی‌گردد.
اگر قصد نقد کردن دارایی را دارید، در نظر داشته باشید که چرخه تسویه بانکی ریال فعلاً با کندی و تأخیر مواجه است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/iaghapour/3121" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3120">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpmgjjbskNPV8-83HSaDlwpsLvQcCdPonIJStnJ8L_c0Cx9gQzuRaophYX1ZyWvf4px7eQHlZ2ghXraFFrxAV2D_-oom-zxVh6j2JsqhYbLtpGLjw0NXX6pfUUD-wav6DkAG2SLMe4P_7F0zut2uZhIT7yF8d9CkSxSpqR4cXHwXxwBVPDk28zMRiXQvVlMBEBFLOmWF5aaEmabMTGeE7YkEBNWBQ7LflMffaGXOEL9hJUiegFINBG6wOGpMAcQhBCD8bn03DD0p-faYNulgP061bggqTN9PUhEMDOJ60b6hpwluw1Pje_6iAWnDmzPpl-0cTrWY34D4z3nBY-IglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش پنل پیشرفته Nexora (پنل جدید سازنده X-UI)
🔹
تو این آموزش جامع، با پنل جدید سازنده X-UI آشنا می‌شیم که علاوه بر بررسی قابلیت‌های پنل نکسورا، دو مبحث کاربردی رو به صورت عملی آموزش دادم: 1. آموزش تخصصی دامین فرانتینگ (Domain Fronting) برای مخفی کردن ترافیک و عبور از محدودیت‌های شدید شبکه. 2. راه‌اندازی کامل وایرگارد روی این پنل.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی 2 عدد اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/iaghapour/3120" target="_blank">📅 15:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارس آپتایم؛ هاست و سرور مجازی ایران و خارج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcnITFuaZyTBL1-o6_xP5Wj83k2Mb4fyph8-pBUxe2mdOdu_-OMAuMrOt_7osZw86Qtlndxf4lGqv3OpY8IZZcCN9pEGOiPLUPgLYcImaEF2oqkutqElN6rFBzQK_SUR4zcltMsPq88HKBtgL5J5zN7bc2uGzArQELMvxrHb2jCP2D4wCFhejHZwDsR-ALpn-gsS4cCtkUnVsp0dFcXC1SpAeUg71KP_3eX9oit1BgGPjfcUL_WEhjIYlfhaRnt73I9HoxpQnac1FzXGr4mK8NNKTtGDhkzkPMZbLxh0zqRvY-c6hIVWxzcvGeX0ZEwZM0sOU6b3G7bVYSOzE1ydeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
رنج آی‌پی اختصاصی خودتون رو داشته باشید
اجاره‌ی ساب‌نت IPv4 در پارس آپتایم: یک بلاک کامل /24 با ۲۵۶ آی‌پی پیوسته که فقط در اختیار شماست. رنج رو با ASN خودتون announce کنید.
✅
ثبت رنج به نام شما در WHOIS
📄
LOA رسمی با مهر و امضا
🔁
تغییر ASN تا ۵ بار، رایگان
⚙️
مدیریت کامل Reverse DNS (رکوردهای PTR)
🛡
بررسی بلاک‌لیست قبل از تحویل
⏱️
تحویل در کمتر از ۲۴ ساعت
🔗
جزئیات و ثبت سفارش:
https://parsuptime.com/services/iplease/
پشتیبانی پاسخگو
|
بیش از 15 سال تجربه درخشان</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/iaghapour/3119" target="_blank">📅 22:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده، قوانین زیر را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/iaghapour/3118" target="_blank">📅 22:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده حتماً بخوانید
!
از شما تقاضا داریم برای درک بهتر محدوده مسئولیت ما و حفظ امنیت مالی خودتان، پیش از هرگونه تصمیم‌گیری یا خرید، حتماً این 2 پست را مطالعه بفرمایید:
🔹
قوانین و محدوده مسئولیت ما در قبال تبلیغات
🔸
قوانین خرید از سرورهای تبلیغ‌شده
هدف ما همیشه حفظ شفافیت با شماست. همان‌طور که پیش‌تر هم بارها تاکید کردیم.
ممنون از همراهی شما
🌹</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/iaghapour/3116" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs6AStZ0HfjI4S278ce7wRnH50annplDGUanCLW61-ilvvo-5A_0b1oEa7yhHqpZLEiXR-kn36OxsjJ18BwzW62r15mFt9IApGUnQUWeKL1iVJ-oFw1VEDl9GY6rw5BjrnibgKkv1KCqX_sOlDcSRzb-lGj-xdVV1CI9t8HEkKS4Ywl_gwR24BZcmlJ55oyl80EgsG1nF-K8JdiPEsyyi4qU0xCXU9FbkYAXRI4zbEEyu9jIjg6zJkCR4LlG9lapmGXzm7SDlEdNwnyh91Iemvp4VMFvk72uJnrqCRx1pj5LDThGQd8kfDyxSDNEkabtSxciib23g4E73lf1pk5X2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
معاون وزیر ارتباطات: احتمال قطع اینترنت در صورت بروز جنگ یا ناآرامی وجود دارد
وحید یزدانیان، معاون توسعه شبکه ملی اطلاعات، در گفت‌وگو با سیتنا درباره احتمال تکرار قطعی اینترنت در شرایط بحرانی توضیحاتی ارائه داد.
⚙️
محورهای مهم اظهارات:
🔹
احتمال بالای محدودیت در بحران‌ها:
به گفته وی، در صورت بروز هرگونه شرایط جنگی یا ناآرامی، اعمال محدودیت روی شبکه‌ها و احتمال قطعی اینترنت بسیار بالا خواهد بود؛ هرچند هنوز سطح و ابعاد این محدودیت‌ها مشخص نیست.
🔹
نقش مستقیم رئیس‌جمهور:
طبق تأکید شخص رئیس‌جمهور، هرگونه دستور قطعی اینترنت باید منحصراً از طرف او صادر شود و در صورت اتخاذ چنین تصمیماتی، نقش مستقیم دولت و رئیس‌جمهور در اجرای آن نسبت به گذشته پررنگ‌تر خواهد بود.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3115" target="_blank">📅 14:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhxtpV3weTXvNUoIjhqL2imLUdu3d5VQFN8UkQMlyMbUdFMnhnCiMeTa1O7EgPzUslfvDLUBUVOzPc7Mqry3SVwb0qJYQrJURMrzT-owQLbyR7dwOU7Ndib6Mhwg2fLF4ssH69Tq4CBlOYW1rYQOevwo32XH5CvlTSElx14sUW6PlCUnNED9-UIkYb97IiumUzgvmp_a64EVwXTM9W8CS-jdA7KUlt7Qst4Vqc04iRN5HQX-S_vRP7JZVufkynAccsoPlxWjo4F8I53QIpaGx_UWi-Gb56xtaEbTn2OxV7nm8xSxUmz1m9-9ZPrvddxEEYIBrYbvyWLqLKTd-QXy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
مهاجرت به SSL داخلی؛ ۱۶ بانک گواهی امنیت بومی گرفتند، ۱۰ بانک در انتظار
در پی لغو گواهی‌های امنیتی بین‌المللی بانک‌های ایرانی توسط صادرکنندگان خارجی (CAها) و اختلال در دسترسی کاربران، پروژه اجباری دریافت گواهی SSL بومی در شبکه بانکی کلید خورد.
🔹
بانک‌های تکمیل‌شده:
۱۶ بانک از جمله بانک مرکزی، ملی، ملت، صادرات، پاسارگاد، تجارت، مسکن، پارسیان و رفاه هر پنج مرحله دریافت گواهی SSL بومی را تکمیل کردند.
🔹
جامانده‌ها:
۱۰ بانک در حال طی مراحل هستند؛ درحالی‌که بانک سپه، بانک مشترک ایران و ونزوئلا و مؤسسه ملل هنوز اقدامی نکرده‌اند.
🔸
چالش جدی کاربران iOS و وب‌اپلیکیشن‌ها (PWA):
اپلیکیشن‌های اندرویدی با تعبیه زنجیره گواهی (Certificate Pinning/Bundling) مشکلی نخواهند داشت؛ اما از آنجا که ریشه گواهی‌های بومی در مرورگرها و سیستم‌عامل‌های جهانی (مانند iOS) تایید نشده است، کاربران آیفون هنگام استفاده از وب‌اپلیکیشن‌های بانکی با خطای امنیتی SSL و عدم باز شدن صفحه مواجه می‌شوند مگر اینکه پروفایل ریشه گواهی را دستی نصب کنند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/3113" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfYKBWf9yEBNEVu-QSO_JGqD6Wg8Xy2KWDqyihaL1INShPXSLU-bHy8hicHzFyrHyO7qgygEjxjrNNvGIDzeHqn6GGAGOy5l5a3r2ocGeUL60TofYX69cuiQ5-1fcqYlKmx2ClelYcArBGI3MSQu7KHihtEktoSQ52Twr5YZzTi-lvGq6RLmIKZ_UmEyhYc9eFpdSti0Th-ONfQiSm-_2p0klqsTFa1eIzvrL-stqFMMWzc8V7qOjOprEzl9dPDF7ycwVL9S5Rr4psHO9BeIuY4IcG3xFwEx0Vn7lTZGYoYpmqXljPPKqHcrwyk62Y_WyGu2sOaimKX5UiZnE3fNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار امنیتی فوری: تلگرام دسکتاپ ویندوز را سریعاً آپدیت کنید!
پژوهشگران امنیت سایبری یک آسیب‌پذیری بحرانی با شناسه
CVE-2026-107181
(سطح خطر ۸.۱) روی نسخه ویندوز تلگرام دسکتاپ کشف کرده‌اند که امکان سرقت سشن و دسترسی کامل به حساب را تنها با کلیک روی یک لینک فراهم می‌کرد.
🔹
تزریق دستور در ارتباط بین پروسه‌ها (IPC):
عدم اعتبارسنجی کاراکتر سمیکولن (
;
) در ارسال لینک‌ها بین پروسه‌های تلگرام، به هکر اجازه تزریق دستورهای سیستمی را می‌داد.
🔸
سوءاستفاده از پروتکل متروکه
interpret:
:
این باگ در ترکیب با دانلود خودکار مدیا در گروه‌ها، فایل‌های حیاتی پوشه
tdata
(شامل سشن‌های فعال و کلیدهای ورود) را بدون تایید یا متوجه شدن کاربر به کانال مهاجم ارسال می‌کرد؛ به‌ویژه برای حساب‌هایی که Passcode لوکال نداشتند.
🔹
رفع کامل نقص در آپدیت جدید:
این روزنه امنیتی در نسخه
7.2.9
با حذف پروتکل آسیب‌پذیر و ایمن‌سازی دیتای سوکت محلی رفع شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3112" target="_blank">📅 16:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnmC-7iFEO_719aScLPAqXlBc1jxxo51nsYCHEk6uJ2u5MP9fjAl7t0xLX643PDtQnzStm4ntTFrnGu-gl2JjSBJpk8-plLvPvf1Q1AgmXhzv0woqOuoWB5F7rqzW0BhmIrhjzFdnWGeJWClLzwO2K8aNSkDPZeDxJbrartMLunk5CsDuSfofuLbcZ9F_mBZ5ScYsHoSKisc_iJ-qLzA7Z1FKthgpPjE3s2ciZGEDBxJlnrxn4uOdXeOgvZ1NYN3GeybWtHoN0yQ4TqV61H-5HbdKwZizs357CxWWZXReGfgoNYExvLiM_p0jgMP7hOMo8HblPtwsxBXEnzlLdmr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تداوم جنگ بی‌پایان دنوو و هکرها؛ کرک‌های مبتنی بر هایپروایزر از کار افتادند!
قفل ضد دستکاری
دنوو (Denuvo)
در جدیدترین نسخه خود سازوکار امنیتی تازه‌ای را پیاده‌سازی کرده که روش‌های دور زدن پیشین، به‌ویژه کرک‌های متکی بر هایپروایزر (Hypervisor-based) را با اختلال اساسی مواجه کرده است.
🔹
مسدودسازی شیوه‌های بای‌پس سخت‌افزاری:
در بازی جدید Star Wars: Galactic Racer، دنوو وابستگی مستقیمی به برخی قابلیت‌های پردازنده تعریف کرده؛ به‌طوری‌که خاموش کردن یا دستکاری این تنظیمات بلافاصله اجرای بازی را متوقف می‌کند.
🔹
از کار افتادن راه‌حل‌های قبلی:
متدهای متداول پیشین برای خنثی‌سازی لایه‌های حفاظتی روی این نسخه به‌طور کامل بی‌اثر شده‌اند.
🔹
ردیابی هکرها:
توسعه‌دهندگان دنوو علاوه بر سفت‌وسخت کردن لایه‌های فنی، اقدامات جدیدی را برای شناسایی و ردیابی تیم‌های فعال در حوزه کرک (از جمله گروه‌هایی مانند voices38) کلید زده‌اند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3110" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8yZMo79yqSPPqwbjdbWQLUpHz8IzGifxPYZyYV2Vd3K1NCOm5NACkoHKV8m08MGYJhImOmOvvDVidiUXW_FRH_ZXWJRHX1-QZDApF7I2eRbg0y-0vHqWm-eRtiIj7N9mDeB9KQf2leQEcqqsar30SBZdBfyTOLRGlyhtMeD_I_IID_SgyIEqALESy5FS9LR5WYg92LTlilrJulC3UMsezn1QrFcKXgxDda9HdnYQcLX8IPSgfBUY6L8KQTUb8wnGUa06UPu9KgFL0H-JpWleR8c3HFEz7Lp1lPh0eX3q3rz0DUEsnRC44m980ARJboC3TPDwgGvHgDpnMK9F16fqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سامانه «حسام» فعال شد؛ مشاهده و بستن غیرحضوری حساب‌های بانکی مازاد!
بانک مرکزی سامانه
«حسام»
را برای مدیریت یکپارچه حساب‌های بانکی بدون نیاز به مراجعه به شعب فعال کرد:
🔹
مشاهده تمام حساب‌ها:
امکان دیدن فهرست کامل تمامی حساب‌های بانکی و مؤسسات اعتباری فعال به نام شخص در یک پنل واحد.
🔸
بستن آنلاین حساب‌های اضافی:
ثبت درخواست الکترونیکی برای بستن حساب‌های قدیمی، مازاد یا فراموش‌شده.
🔹
انتقال خودکار مانده‌حساب:
پس از طی مراحل قانونی، موجودی حساب بسته شده مستقیماً به «حساب پایه» انتخابی کاربر واریز می‌شود.
🌐
آدرس سامانه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3109" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itROEgViSoUOfgOrSTivwqXK59hhmTrbfTx4uQBiJcgGE-bV-rd5b2eSdNKIMpjzu2btCGrRJ5hhkYUGbchkx7h3nqgcTtn-vBGLWuSsj_mXfJPfth6GLwzfT6LuTNtI_esQbvSBboDdlyghCJke_ubRMH5cJXVr6p8a8Ubb9GKjmmFtq6RwpEVllO3urKIrta3SW3lPkwDpX45kzc1XIfwzD1OD_GtgTqKjTv91BV-vBv4mH34vkDOm-PndcUc4tLkyE3uZ0ajRKbRQlfdyK2SuTc_oBVs8q_p1_-ZvLrL5EysRitx9gflzujjQLNdn3UbMxkDTp3pnu9-Ju5kOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت آسان کانفیگ‌های VPN میکروتیک در مرورگر
پروژه متن‌باز
MikroTik VPN Generator
یک ابزار تحت وب و بدون نیاز به نصب است که اسکریپت‌های آماده کانفیگ روترهای میکروتیک (RouterOS) را برای پروتکل‌های پرکاربرد تولید می‌کند.
🔹
پشتیبانی از ۴ پروتکل اصلی:
پروتکل
WireGuard:
تولید اسکریپت سرور (
.rsc
) به‌همراه فایل کلاینت (
.conf
) و بارکد QR با تولید کلید امن در مرورگر (Curve25519).
پروتکل
OpenVPN:
خروجی اسکریپت سرور به‌همراه پروفایل آماده کلاینت (
.ovpn
).
پروتکل
SSTP و L2TP/IPsec:
ساخت اسکریپت سرور برای اتصال آسان از طریق کلاینت‌های بومی ویندوز، مک و موبایل بدون نصب برنامه جانبی.
🔹
امنیت و ذخیره‌سازی محلی:
پردازش تمام مقادیر درون کلاینت و ذخیره فرم‌ها در
localStorage
مرورگر بدون ارسال اطلاعات به سرور ثالث.
🌐
اجرای مستقیم ابزار
💻
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3107" target="_blank">📅 19:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MthDMP6RwlFOLkannA1dobPw396tk3HW4VDxwN-k1FbbdPptSTJV-gUOB13aoygEP40RLuAy9UpnWJdkXTJwqLL1FKo4u_4BchJIYnzkzxREX33jRqNZb-XyDcPFJ-wMQM2h-JMvbPOGkMizxqp2fMwYzP-dRbU6nZGmgG-XgRPGOcuEYiZbE3P_S59HJ2wtsZ4muhG9N7OOkzndwagdTEcxnBvDOddUI7ViMUBxoIShiae4YCN9eMFZ4v_vKbCShjeWhxVNT-j6cHjO6QwXG0enfK7EGEXLdcJhFpCH5BJKVfFRzfjV6BGjBYR-0xlefoIYWBlLRTcPVvwJbxcuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گوگل ابزار تشخیص محتوای هوش مصنوعی SynthID Detector را عمومی کرد
گوگل پلتفرم وب
SynthID Detector
را که پیش‌تر در انحصار رسانه‌ها بود، به‌صورت جهانی در دسترس عموم کاربران قرار داد تا امکان شناسایی رسانه‌های تولیدشده با هوش مصنوعی فراهم شود.
⚙️
جزئیات و نحوه عملکرد این ابزار:
🔹
نحوه کارکرد:
این سرویس با بررسی واترمارک‌های دیجیتالی نامرئی جاسازی‌شده در فایل‌های تصویری، ویدیویی و صوتی، اصالت و منشأ تولید آن‌ها را ارزیابی می‌کند.
🔹
پشتیبانی گسترده از توسعه‌دهندگان:
علاوه بر محصولات خود گوگل، توانایی شناسایی واترمارک ابزارهای هوش مصنوعی شرکت‌های OpenAI، انویدیا و Kakao را دارد و اپل نیز به‌زودی از آن پشتیبانی خواهد کرد.
🔹
محدودیت تشخیصی:
این وب‌سایت یک دیتکتور همه‌منظوره نیست و صرفاً فایل‌هایی را ردیابی می‌کند که حاوی استاندارد SynthID باشند؛ همچنین تفاوتی میان محتوای صددرصد تولیدی و محتوای ویرایش‌شده قائل نمی‌شود.
این قابلیت تشخیصی پیش‌تر درون موتور جستجوی گوگل، جمینای و مرورگر کروم نیز تعبیه شده است.
🔗
آدرس سایت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3106" target="_blank">📅 16:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe7423d72.mp4?token=GWeon2hELvMqxY6FdAyMvBrqmp7dz5VMJvh4AgQp4b9shQaVC9Fda9xIUpZWxJUngWrmEp0UW7jiYvXL8ndFO6zYM8Rqn3twUcDNNJMoCUbEtN4x-1-ludzijp5GoQqwLvXSHX2Oeuxa75zTuPkJ43ty7d_vF2BztUaSpVLVRBB9DbAiQTJ0zUe5f_p-pjtuDrRBqLJTFZAdpHIqmYkD_xMXCUOm5PMRu-29x6DFU30wltMCxh3HcgqL3wDUcSnCyhKjdS_D0iDCon8mPg68l4cxZhwAAwyC5k004OmJr-LDpUe9kgfWEn-SHI1CRp97DfJLtxTvrxLPm5U_1LFKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe7423d72.mp4?token=GWeon2hELvMqxY6FdAyMvBrqmp7dz5VMJvh4AgQp4b9shQaVC9Fda9xIUpZWxJUngWrmEp0UW7jiYvXL8ndFO6zYM8Rqn3twUcDNNJMoCUbEtN4x-1-ludzijp5GoQqwLvXSHX2Oeuxa75zTuPkJ43ty7d_vF2BztUaSpVLVRBB9DbAiQTJ0zUe5f_p-pjtuDrRBqLJTFZAdpHIqmYkD_xMXCUOm5PMRu-29x6DFU30wltMCxh3HcgqL3wDUcSnCyhKjdS_D0iDCon8mPg68l4cxZhwAAwyC5k004OmJr-LDpUe9kgfWEn-SHI1CRp97DfJLtxTvrxLPm5U_1LFKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره چهاردهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی یوتیوب samansh2915، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3104" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b9681d3a3.mp4?token=hh-eaORhJ1E7kxDW9pAolrhQZP9Ap9T919igWD0_lRuRz0ppupFHyRNp2prGCrlCx3xx8ub3zRZrKPcIjE8liEps3akE6xWObTL3HqH_-CXLqRsMwsf0eaw2M0dgJoDxH8GKMsDsGh-SP5f2JIXsYiUo2mOk0mCYtR_y8YxHjAOX-jwXh48_LZYPoh_7bAu8L_qiAQiEJcpA8etv8oOy4mMWf1fv0fnVbhpO9B2UqTF8ME-xlFuDp05NVFMgoXpEUgSYfwHI3LwFaUo9r1XEL1v8MYewujzyqQnaBJ-NJTCygYGDaQCfy5-t8tbztYz-s9Yqjm-m4OTr945pzfcp0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b9681d3a3.mp4?token=hh-eaORhJ1E7kxDW9pAolrhQZP9Ap9T919igWD0_lRuRz0ppupFHyRNp2prGCrlCx3xx8ub3zRZrKPcIjE8liEps3akE6xWObTL3HqH_-CXLqRsMwsf0eaw2M0dgJoDxH8GKMsDsGh-SP5f2JIXsYiUo2mOk0mCYtR_y8YxHjAOX-jwXh48_LZYPoh_7bAu8L_qiAQiEJcpA8etv8oOy4mMWf1fv0fnVbhpO9B2UqTF8ME-xlFuDp05NVFMgoXpEUgSYfwHI3LwFaUo9r1XEL1v8MYewujzyqQnaBJ-NJTCygYGDaQCfy5-t8tbztYz-s9Yqjm-m4OTr945pzfcp0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
گوگل از Playground رونمایی کرد؛ ساخت بازی‌ها فقط با متن و پرامپت!
گوگل پلتفرم جدیدی به نام
Playground
(زیرمجموعه Google Labs) را معرفی کرد که به کاربران اجازه می‌دهد بدون نیاز به دانش برنامه‌نویسی و صرفاً با نوشتن پرامپت‌های متنی، بازی بسازند.
🔹
طراحی با پرامپت متنی:
تعیین قوانین بازی، فیزیک، کاراکترها و محیط بازی (دوبعدی یا سه‌بعدی / تک‌نفره یا چندنفره) با چت مستقیم با هوش مصنوعی.
🔹
موتور هوش مصنوعی تلفیقی:
قدرت‌گرفته از ترکیب مدل‌های جمینای، نانو بنانا و لیریا (Lyria) در قالب یک فریم‌ورک اختصاصی بازی‌سازی.
🔹
اجرای آسان تحت مرورگر:
بدون نیاز به نصب نرم‌افزار؛ بازی‌های خلق‌شده مستقیماً در مرورگر لپ‌تاپ و گوشی اجرا می‌شوند.
🔻
این سرویس به‌صورت رایگان عرضه شده و مشترکان Google One سهمیه مصرف توکن بالاتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3103" target="_blank">📅 19:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjEV6zwaSMtEgYQHhAoYRnTSyLXjKderu38axnU3OCToztJFRrLgrKkbdmSQ0jbHnt2XGL1ZE6l4rJrHkvXgVagAH35fVUdp5nkJjs9uFXiHO1wwNXBCsWYox38PQXuRtxcrJ7BUamFdszAEGACN63zCVYuNriVMrPGCVaeNwE3wNeNlfrAPIQSrz929o_FhldnGJvJ9auqu1TtIbGx1rCPpFwv8YV1x7c8O4Jgny273KyL24pUtOuYtLkLXLTWGKd8py4W29iR6izzYkFk-guHP7zf5kJqzGdI8wKOWIz1w1lqDpFuaQB-zRYKILKKxbD-47AUHx2lhmU3DGFMkLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
وب‌اپلیکیشن کاربردی ارتقای کانفیگ‌ها با ECH، فرگمنت و چینینگ
پروژه متن‌باز
Proxy Builder
یک ابزار تحت‌وب کلاینت‌ساید است که به شما اجازه می‌دهد کانفیگ‌های تکی یا سابسکریپشن‌های VLESS و Trojan را مستقیماً درون مرورگر به ECH و فرگمنت مجهز کنید یا آن‌ها را زنجیره‌ای (Chain) نمایید.
🔹
ارتقای کانفیگ با ECH:
افزودن خودکار پارامترهای
ech
و اثر انگشت TLS (
fp
) به کانفیگ‌های تکی یا کل لینک ساب با پریست‌های آماده (کلادفلر و AliDNS) جهت عبور از مسدودسازی SNI.
🔸
تزریق فرگمنت و سایفرسوئیت (Fragment + Fingerprint):
اعمال پارامترهای
cs
و
fm
با نسخه‌های بهینه‌سازی‌شده پریست V1 و V2 به‌صورت تکی یا دسته‌‌جمعی روی کل محتوای سابسکریپشن (متن ساده یا Base64).
🔹
سازنده کانفیگ زنجیره‌ای (Chain Builder):
ترکیب دو پراکسی (مثلاً وارپ/ورکر به سرور اصلی برای ثبات آی‌پی و رفع فیلتر) و تحویل خروجی آماده JSON برای هسته‌های Xray و sing-box.
🌐
اجرای آنلاین ابزار
💻
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3099" target="_blank">📅 20:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3aBHDszZYNRPLjEAAd27SIwkkSo8hWHkJ4tf5-B-kUcCBeaEk-npqNDYnJYH5KNXB_h-fX_iw3vnSkVd2QRXRUG1y_k2EiLikrkWnKt6FnqgfvTdPfLTsrfI_yCu2E-WISk9x7QyuhwxZHkHqCnGSROW7QcRyREblHXpXO2kJ08rwGqhoyFdW0-SdXYFVxBFSNffkjgxWJFf44GEOgrSGN2i1DSBTLko_ODojPHYDwyX6dvbK0iOnT4J9kW5auj9DijgrcwLiZ2qAclpDOg8z_IBYcxOg1lTtLWu330wl3-Qyu_LBTPK7gXpiY1WoidGQZsHbYIaIQpzsigGT0kDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی نرم‌افزار EtherDNS؛ ابزار مدرن تغییر DNS و مدیریت شبکه در ویندوز
پروژه متن‌باز
EtherDNS
یک جعبه‌ابزار همه‌کاره برای ویندوز است که علاوه‌بر تست و تغییر سریع DNS، امکانات کاربردی مختلفی برای عیب‌یابی شبکه در اختیارتان می‌گذارد.
🔹
تغییر سریع میان ۴۸ سرور DNS تاییدشده:
دسته‌بندی سرورها بر اساس ایرانی (تحریم‌شکن)، گیمینگ، جهانی، ضدتبلیغ، امنیت و حریم خصوصی، همراه با امکان تعریف DNS اختصاصی.
🔹
بنچمارک دقیق بر پایه UDP:
تست پینگ سرورها با ارسال کوئری‌های واقعی DNS به‌‌جای پینگ معمولی ICMP (برای دقت بالاتر) و انتخاب سریع‌ترین سرور.
🔹
نمایش زنده و نمودار وضعیت:
مانیتورینگ لحظه‌ای پاسخ‌دهی DNS، وضعیت آداپتورها و کلیدهای فوری Flush DNS، تجدید IP و ریست کامل تنظیمات شبکه.
🔹
اطلاعات کامل IP و لوکیشن:
نمایش لحظه‌ای Public IP، ریجن، ASN و رفرش خودکار پس از اتصال یا قطعی فیلترشکن.
🔗
لینک دانلود در گیت‌هاب
🔻
این برنامه اوپن‌سورس است، اما کدهای آن توسط ما بررسی امنیتی نشده؛ قبل از اجرا روی سیستم اصلی، سورس آن را بررسی کنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3098" target="_blank">📅 19:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📡
موج جدید اختلالات شدید روی شبکه اینترنت کشور
طی چند روز اخیر وضعیت اینترنت دوباره به‌شدت ناپایدار و فرسایشی شده است:
🔹
نوسان شدید، قطع و وصلی مداوم و افزایش بی‌سابقه پینگ.
🔹
مسدودسازی و فیلتر شدن بسیار سریع IP سرورها.
🔹
اختلال و دراپ گسترده پکت‌ها روی رنج آی‌پی‌های کلادفلر.
اگر در اتصال کانفیگ‌ها و تانل‌ها دچار افت سرعت و قطعی شدید هستید، این مشکل فقط برای شما نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3097" target="_blank">📅 14:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1XGwCK_0cgyKfFzURy72KIbM1mg7B2JT8BBYfDYW89y7fO24Xhrjy_BYD1eMtWKkbAonuMGPRmQVb3S1U4u1KPEUL5m4JGjV8hnUYYZx45NBaxAZ9KwRovcMVHGfCskvIZKnmToKulG1t87HwX-DNURg7XMBEoC1ar02qwD_uv0R9ILMClq6smtdUdxCURMRKA6SkATn4ASatpM3Rkb8BGhNVLOSNDVN_ZgHKcet-i1k52UNVGXLCAZni90vX71etkuCi4D44aiZwYNUOMjpT1wFFSZ17JIvvXMS5I_qKTRiRcFaTabo1Zx3d3IHdY_y9v4-mt8wUzIDHbBVRhqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کلادفلر تأیید کرد: ناهنجاری بزرگ و افت غیرعادی در ترافیک اینترنت ایران
داده‌های رسمی رادار کلادفلر نشان می‌دهد ترافیک اینترنت کشور از صبح یکشنبه ۱۲ مهر با افتی ادامه‌دار و تغییرات ساختاری بی‌سابقه روبه‌رو شده است.
⚙️
شاخص‌های کلیدی گزارش کلادفلر:
🔹
افت ترافیک کلی:
کاهش محسوس در ریکوئست‌های HTTP و داده‌های جریان شبکه (NetFlows) از ساعت ۷:۱۵ صبح ۱۲ مهر که همچنان پابرجاست.
🔹
تغییر سهم پروتکل‌های وب:
سهم ترافیک انسانی HTTP/1.x از ۵.۳٪ به ۱۵.۲٪ جهش یافته و سهم HTTP/2 از ۹۴.۷٪ به ۸۴.۷٪ افت کرده است (ترافیک HTTP/3 و پروتکل QUIC پیش‌تر نیز بسیار ناچیز بوده و عامل اصلی این تغییر نیست).
🔹
افزایش سهم درصدی IPv6:
سهم IPv6 از ۴.۳٪ به حدود ۱۵٪ رسیده است؛ این افزایش به دلیل افت شدید حجم کل ترافیک IPv4 بوده، نه لزوماً رشد فیزیکی دیتای IPv6.
🔹
اثر ملموس روی کاربران:
افزایش شدید پینگ، اختلال گسترده در اتصال تانل‌ها و کانفیگ‌ها، و لگ سنگین در بازی‌های آنلاین.
هنوز منشأ این وضعیت میان محدودیت‌های هدفمند زیرساختی یا اختلالات فنی مسیرهای بین‌المللی رسماً تأیید نشده است.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/iaghapour/3095" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGTmS-uFip0xCa4zPvxZjeqBzcbwhUE5Y2tDuGpUVWwyxJNf-ACZdFKQS_yOu-NamfJpqUbuwIMXg_WdCEZQMBVMcHgqCvc0HQzdXa4By9IoS6-JSFkoBaENtYALchp47y5lAmmGcVAlz3MwFlRxu9x79NLEH31RuJ44MShNPGvH5ACJTvrARZp9QKvH6xDhqJqlhnuupGutJnr_JrLsWaqKwMs5RXKuzabbDLjJ_aWJrJH5rRRmrEx6j2XQSipI26-38IOsV4S6-9c5U48Qhyz_sc3RJo38FwZWlnkAIXUIgao8voufQN27hf-kcIKCoZ1c0TtRkjXzCQGQKqOeFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پرونده جنجالی فیلترشکن جامپ‌جامپ (JumpJump)؛ شایعه هک فیک بود، اما بدافزار واقعی است!
اسکرین‌شات فروش اطلاعات کاربران جامپ‌جامپ در دارک‌وب ساختگی از آب درآمد، اما بررسی‌های فنی نشان می‌دهد خود این برنامه یک تهدید امنیتی بسیار خطرناک است.
🔹
نسخه‌های تلگرامی دستکاری‌شده:
نسخه‌های غیررسمی پخش‌شده در کانال‌های تلگرامی با سوءاستفاده از آسیب‌پذیری‌های اندروید تلاش می‌کنند دسترسی ریشه (Root) بگیرند؛ دسترسی که به مهاجم اجازه کنترل کامل دستگاه (دوربین، پیام‌ها و فایل‌ها) را می‌دهد.
🔹
رفتار مشابه گروه‌های سایبری APT:
تغییر سیستم آپدیت به کانال‌های تلگرامی و جعل امضای دیجیتال برای نصب بدافزار سیستمی.
🔹
مجوزهای خطرناک نسخه اصلی گوگل‌پلی:
حتی نسخه رسمی نیز ۳۷ دسترسی غیرضروری از جمله IMEI، فایل‌های شخصی، سیم‌کارت و دیتای رفتاری را ثبت می‌کند.
🛡
اقدام فوری:
اگر این برنامه را نصب دارید، فوراً آن را حذف کرده و دستگاه را اسکن امنیتی کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/iaghapour/3094" target="_blank">📅 16:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO8ZRquOBj4US3WqQ7zQo_tEtGkT4MeAV2_ZMmMd0VbNvpweHDA-IGaxfUL2C6rW4vOxkQDNSix6_vfT8iSLOCZSvHDHeyS3BVktDB_KCteUjqcFtJ-l2azrNXGLstsF6wrSnFp6SihmRObxrGW_j0JXNJr-3x1qWDZRkRXB8VYDBcM1saD9VRgZczs_DVWHU6wWCyJ7W4DgvEb1TU0-ZtbzGBv11EKzqJV-WQCFyCfgSx1rew4-dzxHRwDh1hpspMdtGYec2sHW5Ns8vIA7hlR93NzIC8lbFJbr9sbegYm03d4TQ9tRIkKeVG8Lsm18kawnTOXfAbbjl5R46jiw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مذاکره‌کننده گروه باج‌افزاری «کیل‌‌سک» بازداشت شد؛ مدیرعامل ۱۶ ساله یک استارتاپ هوش مصنوعی!
مذاکره‌کننده مظنون گروه باج‌افزاری بدنام
KillSec
شناسایی و دستگیر شد؛ فردی که در پوشش زندگی حرفه‌ای خود، مدیرعامل یک استارتاپ حوزه هوش مصنوعی و تحول دیجیتال بوده است!
⚙️
جزئیات ماجرا:
🔹
هویت دوگانه متهم ۱۶ ساله:
وی در معرفی رسمی خود مدعی شده بود که هدفش کمک به کسب‌وکارهای کشور عمان و منطقه خلیج فارس برای پیاده‌سازی راهکارهای هوش مصنوعی و ورود به دنیای دیجیتال است.
🔹
نقش در حملات سایبری:
شواهد نشان می‌دهد این نوجوان به‌عنوان مذاکره‌کننده و نماینده گروه KillSec با قربانیان حملات باج‌افزاری تماس تلفنی برقرار می‌کرده است.
🔹
سرنوشت قضایی:
متهم اکنون با احتمال استرداد به پورتوریکو روبه‌رو بوده و مجازاتی تا ۱۰ سال حبس در انتظار اوست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/3092" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKlyhWNqFKdy1TPop8yu8imvKrE-hLB4yg4kHUb2thshzNQsJk7rIPGAAodzDmglwYF9kTEJqFzLsNYqsFaRrgLPYuLbo9KqEWQT6MQqrtAfedvKq_efvK79KEYVq-2bqHTL0WhnLtMFl3aPSfwbE1ulK_T9sf7Bbn7EvfaSErO6qxS01i3Z0qqyZyniMcpMPV951IAZ7O0N-x4iILTwORFVoPScNSAaYIB9JYFZhG5MhT2Gd5PLsK4JoHlVltAZ_y6eJDLZ5g8J0YV-lMM-KSwgAXb-uENnLM0WLQBCswjjye1TyK7IFmfZx2IhtiJaXeBtFXQzY_gH64uIA1CMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
️
پایان دسترسی رایگان به جمینای پرو و فلش
گوگل با به‌روزرسانی اسناد پشتیبانی خود سیاست‌های جدید دسترسی به مدل‌های جمینای را اعلام کرد که بر اساس آن، دسترسی آزاد به مدل‌های پیشرفته محدودتر می‌شود.
⚙️
جزئیات تغییرات و سطح دسترسی پلن‌ها:
🔹
کاربران رایگان (از ۱۷ مهر / ۹ اکتبر):
قطع کامل دسترسی به مدل‌های Pro و Flash؛ تنها مدل فوق‌سبک
Flash-Lite
در دسترس خواهد بود.
🔹
پلن AI Plus (ماهانه ۴.۹۹ دلار):
حذف دسترسی به مدل Pro؛ دسترسی فقط به مدل‌های Flash-Lite و Flash محدود می‌شود.
🔹
پلن‌های AI Pro (ماهانه ۱۹.۹۹ دلار) و AI Ultra:
دسترسی کامل به هر سه مدل Flash-Lite ،Flash و Pro حفظ می‌شود. همچنین قابلیت پردازش عمیق
Deep Think
بدون هزینه اضافه برای مشترکان AI Pro فعال خواهد شد.
📊
قابلیت‌های جدید و سیستم محدودیت مصرف:
• امکان تنظیم سطح پردازش و تفکر مدل‌ها در سه حالت کم، متوسط و زیاد (تحلیل دقیق‌تر به قیمت مصرف بیشتر سهمیه).
• ریست شدن سهمیه مصرف مبتنی بر توان پردازشی هر ۵ ساعت یک‌بار تا سقف مجاز هفتگی.//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/iaghapour/3091" target="_blank">📅 17:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdm25g6gbcAJDD2xG7rCATjZkiI-S_FK5pDvceu4fCoIo-lIbIWm-3kQqxFoiL1JgtoJXDHmnHD5-MNanlfPudZACyk-0H0lSXdNtXVS5kM3jmt_2bycURHa-81mQQtyw2dx0Z45OSlu01szjuZtT4FondQ2ykQW_yH_QYr1SGtlHYvh4pppI1JdFzkMZ_a9ogAC4zqS3HOFMdZS2dgqiRFOeJ_dev1gIiXWrNVVY7K12IYEW4M1FAT87P7taB3IBUB2NS05f2-BSNL-iRtEHyUM2muy9egmvWu8hz2Swhd0Uobgyp5WyLzvjbX5FMQXhF95LR7B7qAKU6i08sZZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
معرفی FleetPanel؛ کنترل‌پنل امن برای میزبانی هم‌زمان چند ربات تلگرام روی یک سرور
اگر چند ربات تلگرامی را مدیریت می‌کنید، اسکریپت و پنل
FleetPanel
به شما اجازه می‌دهد همه آن‌ها را به‌صورت کاملاً ایزوله روی یک سرور لینوکس بالا بیاورید.
🔹
ایزوله‌سازی کامل هر ربات:
هر ربات دارای یوزر مجزای لینوکس، استخر PHP-FPM اختصاصی، دیتابیس MySQL جداگانه، کانفیگ اختصاصی انجین‌ایکس و گواهی SSL مستقل است تا مشکل یکی به بقیه آسیب نزند.
🔹
پنل وب و CLI:
داشبورد مانیتورینگ مصرف CPU و رم، نصب خودکار ربات از طریق وب‌هوک و دریافت توکن، تهیه بکاپ و بازگردانی خودکار.
🔹
امنیت سخت‌گیرانه:
رمزنگاری توکن‌ها و پسورد دیتابیس با استاندارد AES-256-GCM، هش ایمن رمزها با Argon2id، فعال‌سازی CSP سخت‌گیرانه، محافظت در برابر حملات CSRF و مسدودسازی وب‌هوک‌های بدون Secret.
🔹
عدم تداخل با سرور:
اسکریپت به سایت‌ها، گواهی‌ها و دیتابیس‌های موجود سرور دست نمی‌زند و فقط فایل‌های اختصاصی خود را اضافه می‌کند.
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/3089" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سلام بچه‌ها، وقتتون بخیر.
به دلایلی حساب‌های توییتر (X)، اینستاگرام و چند تا از پلتفرم‌های دیگه‌مون رو خودم موقتاً غیرفعال کردم. از طرفی طی روزهای آینده رویکرد و مسیر کانال هم یه سری تغییرات داره و از مباحث فیلترشکن و... فاصله بیشتری میگیریم.
فعلاً نیازی به توضیح بیشتر نیست؛ سر وقتش کامل براتون توضیح میدم. ممنون از همراهی همیشگی‌تون.
💚</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/iaghapour/3082" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3081">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eteOYzK3Eov5MSptJ3WS1aTYsVgowdhLiaU7_6ILnHozUFgAGZvyBdfM1n1maejxVhiNY8pqmPw-3-O758QCBECJqJXD3Y-pNmldufpD67OP8BWwanQV2oWWf8hdGOE-RNMQN9ZRqFueZx1pDeeKHZQgfKYhunaP0_4jGUeJWINzV3hkKVGf-Sou6PmfG_gGbb6vrtQsOmR-RtybIXSD0iGbBs3QxEsJjUwyOdnHq3Q4JnNrUfqwKIurPXfYnX-CAU19ECWPHBlZy-zDtE35UXkD-SZ6_16R0k_7ejxxwpQ2Datfgap1QzypwQ2Au_NjapLpDtdYW4EvhW58jmQ0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست اپراتورها از وزیر ارتباطات: فیلترینگ اینترنت ثابت و فیبر نوری را بردارید!
در جلسه کنترل پروژه فیبر نوری، مدیران اپراتورهای اینترنتی با اشاره به هزینه‌های سنگین توسعه و عدم استقبال مردم، پیشنهاد رفع فیلترینگ اختصاصی روی شبکه ثابت را مطرح کردند.
🔹
پیشنهاد رفع فیلتر برای جذب کاربر:
نماینده صبانت اعلام کرد برای ایجاد انگیزه در کاربران و افزایش فروش ترافیک جهت جبران هزینه‌ها، مسدودیت پلتفرم‌ها حداقل روی اینترنت ثابت برداشته شود؛ چرا که کنترل امنیت در شبکه ثابت ساده‌تر است.
🔸
اقتصاد در حال احتضار اپراتورها:
نمایندگان شاتل و پیشگامان از خسارت‌های چندصد میلیاردی ناشی از قطعی‌های اینترنت، هزینه‌های استهلاک باتری‌ها در خاموشی‌های برق تابستان و عدم اصلاح تعرفه‌ها گلایه کردند.
🔹
کیفیت پایین اینترنت ثابت فعلی:
به گفته مدیرعامل زیرساخت، کیفیت ADSL کشور به شدت افت کرده (سرعت آپلینک ۶۰٪ مشترکان زیر ۸ مگابیت است) و همین امر بار مصرف را به شکل نامتعادلی روی شبکه موبایل انداخته است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/3081" target="_blank">📅 19:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdlVuykiFrfTxy_qJNmRN9eH7jRQWCa0dgoNJH2xAfpy71DAqIvJL5cZCCQx8hkzzf05-PO_z-1oXjCR7s89S9YlsGOZKTkRSDVm4hQWRlP1aWAFOkv9kAboZ69IB8Z_6tNfxpQqi6KqLCRUlbYSGckeFL-h-D2LYPK3GEpdBi5qnqYN7fJN7HMlHluxKOu6KazPCw47uOuwqRWfMeM_kspMGki49JCH6cMI8DzOlZBN32tjtuSXvGqcEt-Y1AetUuUVBrxMJgynyI8WeFBcOHiWI26JKpjlPSIDjHoB0fe5rj_cSWdh1XaswgfrQU5-eRClUEz5e9I9QEQ5ZJmmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/typNpTRtNv-7shZWliQnrNpwp_L08-ARL2MeUCOzL9XmzorS-FC_FoswQtHAtwjzsqXpi2uo3orztvFAaaX3oDpSY-DjHCypF7oA853xoVWrtHHSkgfHfnl2sztSKSeZa0iI_vOKGC2Mt3BXxaWRoG2Q7t5DrZH22S47AJrRqD7nPfpvThXVNCyaYMzfmlJDcz2XaVFtRZaf4F9mxleBvSQFhiT02iiNeIq8Wn1LnL6XCO9kM5CJS-vfDyiBiB7v8EUDAoP5lrIy7_exLb1r9bfgRjdmnCdJxmcR6bUW5qOyriizlH3KX4ekMcD6Z8EwLVXN0JEclVDcU6dwVFu2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
مدیرعامل مخابرات: اختلال اینترنت برطرف شد / وضعیت IPv6 بررسی می‌شود
محمد جعفرپور، مدیرعامل شرکت مخابرات ایران، در گفت‌وگو با رسانه‌ها از برطرف شدن اختلال چند روز اخیر اینترنت و فیبر نوری خبر داد.
🔹
علت اختلال چندروزه:
قطعی اینترنت، سایت شرکت و سامانه ۲۰۲۰ به دلیل ارتقا و به‌روزرسانی زیرساخت‌های سامانه‌ای مخابرات رخ داده و اکنون اتصال کاربران بازیابی شده است.
🔹
وضعیت پروتکل IPv6:
جعفرپور تأکید کرد از سمت اپراتورها منعی برای ارائه IPv6 وجود ندارد، اما سیاست‌های بالادستی شبکه در اختیار آن‌ها نیست.
🔹
احتمال تأثیر تغییرات دوران جنگ:
وی اشاره کرد که تغییرات فنی اعمال‌شده روی شبکه در شرایط جنگی ممکن است همچنان بر وضعیت دسترسی به IPv6 اثر گذاشته باشد و این موضوع نیازمند بررسی فنی دقیق برای شناسایی منشأ اشکال است.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMYcMG6bxAK8OE4zB1tD5FCIZk--DCZ8sj_UF1AQmoxEvQu4EV4yF97AsXhIiwz5kL8pmYfjIt28IWaFEvmfukerXQuCeblBhZxJfjlnKz9Wumj7ziBIf6nDdftLyNleIV0kB3LnJqDTsOnzeD1TC6ImqhNE7jqB_pGIpLT9J4SFp5WsLs1uMpDoxEbpEfAwIv7ItjCZYHAmGdAv9FMBj7gg00zGJ37pTCYo2-AjyJxo8lZ7Tqrf2DDETtdsfJJgDcCe1kOWZ6Beo4XyDaaI03dpNEKNDIik_e4wp4UbNDeQHWXIhFS4xczair8j4UUn8IUg_8tyXgau8eZil72lzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
تولید ویدیوهای 1080p با هوش مصنوعی برای تمام کاربران گوگل فعال شد!
گوگل قابلیت تولید ویدیو با کیفیت
1080p
را در ابزار
Google Vids
برای تمام کاربران عادی و مشترکان Google Workspace در دسترس قرار داد. این ویژگی با بهره‌گیری از مدل پیشرفته
Gemini Omni 1.1 Flash
کار می‌کند و ورودی‌های متنی، تصویر، صدا یا کلیپ‌های موجود را به ویدیوی خروجی تبدیل می‌کند.
⚙️
قابلیت‌های کاربردی و کلیدی:
🔹
توسعه هوشمند صحنه‌ها:
امکان افزایش طول زمانی کلیپ‌ها با حفظ ثبات کامل در نورپردازی، چهره کاراکترها و زاویه دوربین.
🔹
هماهنگ‌سازی و افزایش رزولوشن:
تنظیم دقیق مدت‌زمان هر فریم برای تطبیق با صدای گوینده، به همراه ابزار ارتقای وضوح (Upscale) کلیپ‌های قدیمی به 1080p.
🔹
سرعت بالا در تولید:
رندر هر صحنه ویدیویی در این پلتفرم در کمتر از ۳۰ ثانیه انجام می‌شود.
سهمیه استاندارد به تمامی حساب‌های رایگان گوگل اختصاص یافته و کاربران طرح‌های تجاری و پولی سهمیه ساخت بیشتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
اجرای مستقیم و بی‌دردسر پروژه‌های داکر با Docker Compose در دوپراکس!
🔹
دوستان عزیز، یکی دیگه از قابلیت‌های فوق‌العاده دوپراکس بخش App Space و پشتیبانی مستقیم از کدهای داکر کامپوز هست!
🔸
اگر پروژه‌ای دارید (مثل ربات‌های تلگرامی، پنل‌های خاص یا وب‌اپلیکیشن‌ها) که با فایل
docker-compose.yml
اجرا میشه، دیگه نیازی به سرور لینوکسی خام، نصب دستی داکر و درگیری با کدهای ترمینال ندارید. دوپراکس یک محیط کانتینری کاملاً آماده در اختیارتون میذاره.
📝
مراحل اجرای پروژه‌های داکری:
1️⃣
ساخت فضا: از منو وارد بخش Container Platform بشید و یک App Space با منابع دلخواهتون بسازید.
2️⃣
تب Compose: وارد فضای ساخته شده بشید و در بخش Topology، روی تب Compose کلیک کنید.
3️⃣
وارد کردن کدها: کدهای فایل داکر کامپوز خودتون رو مستقیماً در ویرایشگر پیست کنید، یا اینکه خیلی راحت با دکمه Upload YAML فایلتون رو آپلود کنید.
4️⃣
اجرای نهایی: در نهایت دکمه Apply changes رو بزنید. (حتی گزینه‌ای برای جایگزین کردن امن منابع قبلی یا Override existing resources هم وجود داره).
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کانتینرها، شبکه‌ها و والیوم‌های (Volumes) تعریف شده در فایل شما رو در لحظه می‌سازه و پروژه رو ران می‌کنه. یک مدیریت کاملاً گرافیکی، سریع و حرفه‌ای!
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWylMTlfK6K9g8aRQK9fEk9axjm_OILb9jYwqd9-mQ-gsq1bvENiJjtUAEZ2u1f8W-2G8sLrZ-JnTkP2910Ea05AeSDNRRSdaigl09FMASBX8cemTI7LkfzAao6XHnrMhZ5tJBinD14WIUpNUMqZmJk0Td_uGu95ZlErmbLaRj84HtVPpW7nL8N9wSlFD3n0XX_e8-JufH2e2fg4TjcbhDEKIahXTx0TxbbTQd9MEJTTDIoGOuRBG7op4uVm4i2oX82I_SBRFBLvlZhISMw-nmpOlXCWW1iHtw_yM0DWIK0a14BCVqKJpTdIFehiybKbIkkIKJVdd3A8pHQ0VumLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f69ijh7cKaJASzMc_fPH2nCUev1Qweq38fC2MAVo9qi4c34oBey8LmeobedEUDkemp_BX4R-yLPbYwIMO_XK0D1kq_zhVuz32HFUMEDoA573AfkyZIaE92NX7o4lYvHnvVvQFbodFxkcLSEfAG7cstBIMGeLTLykjyY2HEpIRk1cRheInRuqB2ovbauAh1WujVR2ouPZH4ipcByvmfw0gJ-7d01Z8QCAbgwbvk5UjfIkSFlJCBdCtOrVFl6LuDw_ZsoVTU42m8UEXvtl5lPIj0am9rxu3o8MH8ViC-twih4t17r0scQGTiDm4e5riQvAVloNMqgw9lHzzWFShxn5gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه همراهان عزیز کانال!
💚
به لطف و حمایت‌های گرم شما، تونستیم
8 عدد کیف
مدرسه و تعدادی دفتر و... رو برای چند تا دختر کوچولوی دبستانی تهیه کنیم. (همشون تو عکس جا نشدن)
این هدیه ناقابل، نتیجه
مهربونی
و
همراهی
تک‌تک
شماست
و از طرف همه‌مون به این بچه‌ها تقدیم می‌شه. سال قبل هم اگه یادتون باشه اینکار انجام شد.
اطلاعات بیشتر
ازتون ممنونم که باعث و بانی این اتفاق قشنگ شدید. دلتون همیشه شاد و لبتون خندون.
🌹
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=CLosp9KPechqciWgPudgpPc9Y3XGiQ99AnwfqZSwWvMudoZhcKHwai-0MqasUilxPMVp-2FOep0g89LpmkutUZC5GyPz48peXxwhZ9R7dMmtS8uJjulT6Osb1GJMiP62Lzxm938HivMYd-6lAh7QOdbi2V6aQFa0yPYHXoMO-Xd48slh260DY9W_VkIchvASHSwJiTmtJ1n4qGw48TYECKyU5QfgZ8yFTNjB0AiZMuQ4U6gwV1cjuGjXa1N9N4ROaVJPLBXoUWeCJNNnKEbO6X8D0NwnMyjtfv3i5VuNZOo7XtY-0f57yfYMQhSI1-X-5wJ6EfrG8Qm9lczA2FxtCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=CLosp9KPechqciWgPudgpPc9Y3XGiQ99AnwfqZSwWvMudoZhcKHwai-0MqasUilxPMVp-2FOep0g89LpmkutUZC5GyPz48peXxwhZ9R7dMmtS8uJjulT6Osb1GJMiP62Lzxm938HivMYd-6lAh7QOdbi2V6aQFa0yPYHXoMO-Xd48slh260DY9W_VkIchvASHSwJiTmtJ1n4qGw48TYECKyU5QfgZ8yFTNjB0AiZMuQ4U6gwV1cjuGjXa1N9N4ROaVJPLBXoUWeCJNNnKEbO6X8D0NwnMyjtfv3i5VuNZOo7XtY-0f57yfYMQhSI1-X-5wJ6EfrG8Qm9lczA2FxtCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره سیزدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی SattarBayat، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0RX9w4Ws4oWHmYo0DiioAjWFZ0sdAGM_8Mt-FZcOT_3KG2nZAQ53tJYRXaiUE2qE552sDDa4c8tf5JQPBtl6jd67BdH7RTkFXNm-YBBV2L-NS-GzjvXKLFVNCcfLDEJnViZ-Fc3w7KPVQu4qBsPMi18WwoARNEX391nu15Qqlilck-OVTyYG_pQh5cXZQWrXGj2CwUBgiRiOg3al1-IJImRtZpKJ9aWTgAviZasWE12YhXtgvFxeFdyt2cC7vyOymqDwLR9P_5raOtnMjO9wXMWgGjFTbjtbLodn4gt6_z0CDhUpkMzkF19hQ3pvAh5LVRu5NPlGY-8st7EZS_0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نشت اطلاعاتی چیست و بعد از لو رفتن اطلاعات چه باید کرد؟
رخنه‌ی اطلاعاتی زمانی رخ می‌دهد که هکرها با نفوذ به سرورها و دیتابیس شرکت‌ها، داده‌های هویتی، تماس، رمزها و اطلاعات بانکی کاربران را سرقت یا در دارک‌وب منتشر می‌کنند.
⚙️
۵ اقدام فوری و حیاتی پس از افشای داده‌ها:
🔹
تغییر فوری پسوردها:
تغییر رمز حساب هدف و تمام سرویس‌هایی که رمز مشترک داشتند (با کمک Password Managerها).
🔸
فعال‌سازی تایید دومرحله‌ای (2FA):
فعال کردن کدسازهای معتبر مانند Google Authenticator روی ایمیل و تمام شبکه‌های اجتماعی.
🔹
امن‌سازی حساب‌های بانکی:
مسدود کردن آنی کارت مشکوک، تغییر پسورد اینترنت‌بانک و فعال نگه‌داشتن رمز پویا.
🔸
استعلام سیم‌کارت‌های به‌نام:
ارسال کد ملی به سرشماره
۳۰۰۰۱۵۰
یا سامانه
cra.ir
برای بررسی عدم ثبت سیم‌کارت مخفیانه با هویت شما.
🔹
هوشیاری در برابر فیشینگ ثانویه:
عدم کلیک روی پیامک‌ها یا ایمیل‌های مشکوک.
⚖️
در صورت بروز سوءاستفاده‌های قضایی یا مالی، فوراً از طریق مرکز فوریت‌های سایبری پلیس فتا (
cyberpolice.gov.ir
) موضوع را ثبت و پیگیری کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCo-_14d1J4lns6UJmcAUw76lpFHCe-qCFd9AYD7AKps9M7p2wubQvK6hVjhjRac--uibdM01J3dM0kPsaMOXYhJ9PIha3a6FjFhhgtWGIM023eEjz2u4wDDZOEySn-EMVYM2hlUqT2hiKYNRNp5FWZXMwA1kfHUBFwZDQPnSLEnwZBFTC8FxelEYTBv-zqajaF-Py5I4c6jwUlB5tHuN9q81csTTASn6WWffztO0_3wl8aWtpscHrFFLQyi07-Ydo4k_bDcUffbOvhjoxO0nKmWAH0S-g3OtyF5rsyCgjETxkGJUoLxfqd0URrMHBcOeerwXEWv_kOkxC3l_DB_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
حرکت جالب WinRAR؛ فروش کیف به قیمت ۵ لایسنس نرم‌افزار!
شرکت
WinRAR
از یک کیف جذاب با طراحی آیکون نوستالژیک و معروف کتاب‌های خود به قیمت
۱۵۰ دلار
رونمایی کرد.
اکانت رسمی WinRAR در توییتر (X) با لحن طنز همیشگی‌اش نوشته:
«حالا که هیچ‌کدومتون پول لایسنس برنامه رو نمی‌دید، حداقل بیاید این کیف رو بخرید!»
😂
قیمت ۱۵۰ دلاری این کیف معادل خرید حدود ۵ لایسنس رسمی نرم‌افزار است و یک راه جالب برای حمایت از سازندگان این ابزار نوستالژیک به حساب می‌آید.
©️
Behrad Javed
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_ByJ9shBBi7LIdrAje9dadRpuRTXrh1x_ik7m5B5kgYniV4cuYxGTG8DbDKZZ5zAi2jw0Dw4nSw1x4FOf9fABmgyR936b_KY_n9mRGeQtNEXaRmuaPQYEOT1ma7bFRe5kWd2SOMWPu6XKpuvVd22u7pbFvqSIRuhB7H_XpiWs2M6xCIbcWrKRbqY7XIpJg1hg4jYR6BgHfidk6W-hEeN_Vqd_xvlFPb-ICKSScQzS1aTlrXWI9gCftjc-LVy0Ev6DmKhxiip9Z8M1yPYarQb7LGxmu6conOBeBF0f-l60c7K4k3cgIgkh8Q9oi7He_CLppAx7naRBmM0v5YqYPA0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
رئیس جدید گوگل دیپ‌مایند: جمینای 4 تقریباً برای عرضه آماده است!
پس از مدتی فاصله گرفتن از رقابت پرچمداران، گوگل در آستانه رونمایی از مدل قدرتمند و مورد انتظار
Gemini 4
قرار دارد. «کورای کاووک‌چوغلو» رهبر جدید بخش دیپ‌مایند گوگل اعلام کرد این مدل در مراحل پایانی ارزیابی قرار دارد و بسیار زودتر از پایان سال جاری میلادی عرضه خواهد شد.
🔹
عرضه زودهنگام نسخه پس‌آموزش:
کاووک‌چوغلو اعلام کرد با توجه به نتایج فوق‌العاده و هیجان‌انگیز تست‌ها، گوگل قصد دارد در اولین فرصت نسخه‌ای از فاز Post-training را منتشر کند و سرعت ارتقای مدل‌ها را بالا نگه دارد.
🔸
بازگشت به رقابت با GPT-6 و Mythos:
در حالی که رقبایی مثل OpenAI با معرفی مدل‌های سری GPT-6 و آنتروپیک با خانواده Mythos پیشتازی می‌کردند و عرضه وعده‌داده‌شده‌ی Gemini 3.5 Pro لغو شده بود، دیپ‌مایند هدف خود را مستقیماً روی جهش به نسل ۴ گذاشته است.
🔹
تغییر استراتژی فنی:
کاووک‌چوغلو علت تأخیر در عرضه پرچمدار را تمرکز موقت روی بهینه‌سازی مدل‌های سبک و سریع Flash دانست و تأکید کرد گوگل همچنان جایگاه خود در خط مقدم هوش مصنوعی را حفظ خواهد کرد.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0lzyYA_GV4ohiJNoXyVaTjOb2VaKBkFLjHFxPPMn8WzVgXk9i67M5ZbJumDWvKM6apzw2DAWQ9hdkrPxgsRVfTmXaHGGN9MgOMwY4OIC7lH6ZGiaRfihxbnxJeEz4HxCMFoet9JFCab2AQkA51K5JpfzSctthj855QVvcQTZpQvBOL7drQG1pxSLS4JO6b_RkfJ31Q1AcfyRPLn47fGzitfxLIws9_7VzlgrNLeKRQSkFexiCl-QSYQ7JutdT9tYpDAjdi6upw2iBmlQMc5MHm3WMWzt3bqJuWtPR7gR5LVMzBiELOWI-xKUx4zFBZD8BtqTF5A1t3VcnnlJHLh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گزارش رگولاتوری از ماجرای اتمام زودهنگام بسته‌ها
سازمان تنظیم مقررات پس از بررسی گلایه‌ها درباره پایان زودهنگام بسته‌های اینترنت، اعلام کرد اپراتورها تخلفی نداشته و ضرایب مصرف را رعایت می‌کنند.
⚙️
دلایل اعلام‌شده برای اتمام سریع بسته‌ها:
🔹
کیفیت ویدیوها و فرآیندهای پس‌زمینه:
افزایش حجم محتواهای ویدیویی، آپدیت خودکار نرم‌افزارها، بکاپ‌های ابری و فعالیت برنامه‌ها در پس‌زمینه از دلایل اصلی جهش مصرف عنوان شده است.
🔹
شفاف‌سازی ریزمصرف:
رگولاتوری اعلام کرد عدم شفافیت برخی اپراتورها در تفکیک ترافیک داخلی و بین‌الملل پیگیری و اصلاح شده تا مشترکان دقیق‌تر مصرف خود را ببینند.//شبکه‌چی
💬
خلاصه اینکه اگه قبلاً بسته ۱۰ گیگی یک ماه براتون کار می‌کرد و الان یک هفته‌ای تموم میشه، مشکل از سیستم نیست؛ مصرفتون یهویی رفته بالا و شما حواستون نیست!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oovG226JIiHLiM5mTiv074Vg1wKQtAttNbmwnX2M4jIURYjnaBpeogfQ4iQ2WDbFjVhuctaCLZH2FU5xGxKO1Zp331ubBtvIrqP4MyhlGQqNSjUjYspWVJo_LiUiZR1Kc0QuwKfRDxZuVhciWt7QpvRwWR99VmUPlr0OINS4U9kn3czKulcdcI1IOTCXLcOOABgaY1Rb_0ZTvqkvt_evHgUI07b7E4Ju-q5HOkAcgGwcQ6YKigpE3RvoapyFKSfVzY4V9RMR1UPkTUtrCKThSKXO_3qaCWdPZKNIO2I5dfOTfL7azfJV3KEncDmxMn8fii805Wi94MxQAnwbqaljFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی بدون تانل + پنل مدیریت (مشابه شکن)
🔹
خیلی وقت‌ها برای دور زدن تحریم‌های اینترنتی (سایت‌های برنامه‌نویسی، بازی‌ها، صرافی‌ها و...) نیازی به درگیری با تانل‌های پیچیده نیست. تو این ویدیو بهتون آموزش میدم چطوری یک تحریم‌شکن شخصی قدرتمند (مشابه سرویس شکن) بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL3pLIgTQ15_3kJ57vxoT4RS_Aqu5FIQTwm8GtOejWy5RRkNU2EqKLDeCLXB5Rdade3d8k89u4-VRAyhyF29x39A_36-ZG7Ff-BwsYPsxf0USpGLbGu4kX4C1eBnPXLrGbIcQcv3kamSMoryyrI6feUCHz4JpvWNOZCrcRyE_ntTWjeqTvz_Rg5H0VqjrZEnamEhkkT58EMVcQSTmSlrEZXOhpDKQcGLLOO76hHJQzfy5nbGRTFdzlbj1Dl5uDRof1bfuure7_Jtih3xtU2GmAtRI2gO_jx0Vwdh0GbaJWhxvWt2dUIaFVW-wV0hIRp_uFZNYfXU_8hc3LN6116dMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GPT-6 Sol و GPT-6 Luna؛ مدل‌های جدید اوپن‌ای‌آی با نصف قیمت!
اوپن‌ای‌آی دو مدل جدید
GPT-6 Sol
و
GPT-6 Luna
را با تمرکز بر سرعت بالاتر، خطای کمتر و
۵۰٪ کاهش هزینه API
معرفی کرد.
🔹
هزینه بسیار پایین‌تر:
ورودی Sol به ۲ دلار و Luna به ۰.۱۰ دلار به ازای هر میلیون توکن رسیده است.
🔹
عملکرد قدرتمند:
در بنچمارک‌های برنامه‌نویسی و اتوماسیون (نظیر AutomationBench و DeepSWE)، مدل Sol رقبا مثل Claude Opus 5 را با کسری از هزینه شکست داده است.
🔹
کاهش ۵۰ درصدی خطاها:
دقت اطلاعاتی مدل به سطح GPT-6 Astra نزدیک شده و پاسخ‌ها در کارهای فنی شفاف‌تر و کوتاه‌تر شده‌اند.
🔹
دسترسی:
فعال در API با شناسه‌های
gpt-6-sol
و
gpt-6-luna
، ابزار Codex و به‌صورت تدریجی در ChatGPT Work و دسکتاپ.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=vcftpTUu3LExVuTlpsxccg6e56N3zVmNdQiAvV8zIV_HRiVHVQ7kTmBLxmq7qjEtspz1u6Qm5gcVGAkc7oepJXcYoaBi0cX84-4xTH0N0mtOL7D8_cPwhKpeakcR95ORVNwH7KZQb2V6_riRHhvGy3fhbnzem2e6ybQbjfzKP5qF4sLhh4w789AIm8d9g5aTwCf1Yqdfb8eMyCg_AGqr_1cz0q8U4YjyuLRJ1NKWsigMBWeLoXcqO61x3_8SZHa90Pv6hYmDA7y3v9U-4eqtAT-P6bCYgAq-ymJPoxEn7eh3XFkQUXbwgCcjlTZrUWhsnZwZq-unXYbmK_voyUAh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=vcftpTUu3LExVuTlpsxccg6e56N3zVmNdQiAvV8zIV_HRiVHVQ7kTmBLxmq7qjEtspz1u6Qm5gcVGAkc7oepJXcYoaBi0cX84-4xTH0N0mtOL7D8_cPwhKpeakcR95ORVNwH7KZQb2V6_riRHhvGy3fhbnzem2e6ybQbjfzKP5qF4sLhh4w789AIm8d9g5aTwCf1Yqdfb8eMyCg_AGqr_1cz0q8U4YjyuLRJ1NKWsigMBWeLoXcqO61x3_8SZHa90Pv6hYmDA7y3v9U-4eqtAT-P6bCYgAq-ymJPoxEn7eh3XFkQUXbwgCcjlTZrUWhsnZwZq-unXYbmK_voyUAh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی 18 ماهه (دوره دوازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی 18 ماهه مشخص شد:
👤
برنده عزیز با آیدی matintarafdar4000، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL6zJ0bN95jx6ejQmvNW0i-UpYmwJIkmAjTbmYMplVBuT77lMgQh2W-5Wr1FTA6jpuHhQ4CJicJC4wvgmGeptY2XIv4HsdevDgpJ_FPqn1Tb4f433q4MkvrRrazDUT2F4PirA_yiXg3qWqo18sHNtbiKPA_x9CzRqR4EK4DoFYB12qpz5NCdLPTcouuBY3AK2KbFoWdltKa2zSysxG3nRb7ek6q_zjUN4etsCWwWE3Y0PPlByzo_VFUf5tS6GkLJNzoVb-2e7K1Heb64KfSir2H5UGSR82gy99w5PDMb7p_nDICBcjZslgbPcaRN6NsLURlUUF9fckpvjUhqJQTqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل DeepSeek V4 Flash در OpenRouter رایگان شد!
نسخه
DeepSeek V4 Flash
بدون محدودیت سخت‌گیرانه (Rate-limit) روی پلتفرم OpenRouter به‌صورت رایگان در دسترس قرار گرفت.
🔹
سرعت فوق‌العاده بالا به لطف معماری بهینه MoE
🔹
کانتکست عظیم (بیش از ۱ میلیون توکن) مناسب تحلیل اسناد و کدهای حجیم
🔹
اتصال آسان از طریق API به افزونه‌های هوش مصنوعی در VS Code و ابزارهای مختلف
🔗
لینک دسترسی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXOIhLX0fCWPEWEAwmtPPzJFsAJQ6pm84U0PeuEItG6vtc-s0R3jHls0e1TZoLBNlcBvQl6i6aaODmZI9fWrkB1CWjWfNZKz9YKFIEt5v26oKhT6VyWO3KUKUoFhztg8r7P7ta9ZnjdoL0D16XstIqdXhoGS03n0lCXC3pQPUkapgZ3XI7y0VyJKIG_kbRB6A44Gq9TXc0ut5lvL_tw10FR9tb_q47cNcYw-Y7s6-NBNwtSYZwoEqOee2o7ua6JlVHT00fAoh5Sd4dOdBskjtrvrwwkN7gdQ4k81oRnPQFkP_5IRtrosMhFYGhC6ZabmRDGeMfX8_yZKffVjgf3ueA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت اینترنت دیال‌آپ، صدای قیژوویژ مودم و استرس اینکه مبادا کسی تلفن خونه رو برداره قطع بشیم... و در نهایت رسیدن به این صفحه جادویی!
✨
نسل جدید هیچ‌وقت لذت و هیجان این لحظه‌ها رو تجربه نمی‌کنه:
• لرزوندن صفحه چت طرف با BUZZ وقتی جواب نمی‌داد
😂
• ساعت‌ها گشتن تو روم‌های ایرانی و چت با غریبه‌ها
💬
• تیک زدن گزینه
Sign in as invisible
برای اینکه مخفیانه بیای.
👀
• استاتوس‌های سنگین و خفنی که با کلی فسفر سوزوندن می‌نوشتیم!
تلگرام و دیسکورد هرچقدرم پیشرفته باشن، اون ضربان قلبی که موقع چرخیدن این آدمک طوسی و لاگین شدنش داشتیم، دیگه تو تاریخ اینترنت تکرار نمیشه.
😊
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gacnuoRmXBn0juToR_OkIb0vvsl4mo5u2cZeaNGvkZz63DwS-W7AE46XxUFBs7ttT0OI39IaAw5X3JY8q_3jas3aZeMH_iRGuCW-S22R8U-pSxAFEna-4_0OoE_z7fYo_Jlef8nhq0oWpYwVnB3AmWi5sngC-28L_PQjNppkCSwSuKTLoyFv_mGiXpGjDPrvqaF4ncJy9N0IulnCn1IPu4PmsfE81MzOe1Kaxtzr4lkWwsoJeVIOXXcRriLBunjcOzuAW2zmqtsiYmCbOWXxbxuxljSQcUW6VInzlSAItDD2ctk69t0JRbPchnTOH8LxwZHOYwZ7FEChzG_9G-nRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار مهم امنیتی: انتشار آپدیت حیاتی سپتامبر ۲۰۲۶ برای اندروید ۱۴ تا ۱۷ با رفع ۱۸۰ آسیب‌پذیری
گوگل به‌روزرسانی امنیتی ماه سپتامبر ۲۰۲۶ را برای نسخه‌های
اندروید ۱۴ تا ۱۷
منتشر کرد. این بسته به دلیل تغییر سیاست گوگل به بولتن‌های فصلی و عدم انتشار جزئیات در ماه‌های جولای و آگوست، حجم بسیار بالایی دارد و
۱۸۰ حفره امنیتی
را ترمیم می‌کند که بیش از
۳۰ مورد از آن‌ها دارای سطح خطر «حیاتی» (Critical)
هستند.
⚙️
تفکیک پچ‌های امنیتی:
🔹
پچ اول (سطح سیستم و فریم‌ورک):
رفع
۹۵ باگ نرم‌افزاری
که شامل ۲۶ رخنه حیاتی در هسته سیستم و فریم‌ورک اندروید است؛ خطرناک‌ترین آن‌ها امکان
اجرای کد از راه دور (RCE)
بدون نیاز به تعامل کاربر را به مهاجم می‌داد.
🔹
پچ دوم (سخت‌افزار و تراشه‌ها):
ترمیم
۸۵ آسیب‌پذیری
مرتبط با چیپست‌ها و درایورهای سخت‌افزاری شرکت‌هایی نظیر کوالکام، مدیاتک و آرم.
⚠️
خطر حملات هدفمند علیه گوشی‌های پیکسل:
گوگل تأیید کرده که شواهدی مبنی بر سوءاستفاده‌های محدود و هدفمند هکرها از برخی از این آسیب‌پذیری‌ها روی دستگاه‌های پیکسل مشاهده شده است.//پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n__JBInJSNm8Nxa8eY3sf8uGUTPjxuErs6aITsvH7JdpvVojbZ6ujH04bEQe4QUMQq63o1HClD6p1yRyvvOQIFs6SRb9qe8fec4ia24AB4vqqmoS6Uix7m-Xz5GAJwCVEdhrlCWHfPaSVUqc1gGTWQvxki1pvwWgGzrm_iIFfS7l-Zuqtwg51uCiHMyUyKxzkwOf5sUPzWgA6TbmGj1FWXqMGx6gUdDyC3gUEn5q-nifK_dSIpfIm-sR6hkfkObviZMcUNug1G4IofqAe4Q40odae3xNx4HLofA66uNRKjoXScxjPllAhKUJHN9Ycj0c6Hf5Lg4fPq7GVnSuOHGURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آماده‌سازی اینترنت برای AI Agentها توسط کلادفلر
کلادفلر در حال ساخت زیرساختی است تا عامل‌های هوش مصنوعی (AI Agents) بتوانند پروژه‌های توسعه‌یافته روی
localhost
را بدون دخالت انسان تست و اجرا کنند.
⚙️
نحوه کار:
🔹
ساخت فوری URL:
با ابزار
TryCloudflare
، ایجینت بدون نیاز به دامنه یا لاگین، سرویس لوکال را به یک آدرس اینترنتی عمومی و موقت تبدیل می‌کند.
🔹
تست و بررسی با مرورگر:
ایجینت آدرس ساخته‌شده را با مرورگرهای هدلس کلادفلر (مثل Browser Rendering) باز می‌کند، المان‌ها را بررسی و خطاهای کنسول را می‌خواند.
🔹
دیباگ خودکار:
در صورت وجود باگ، ایجینت خطاها را تحلیل کرده و کد را در لحظه اصلاح می‌کند.
🔗
تست سریع ابزار
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAPMd00xze2NxI02eeLmZW5IvdiLIYQWa0YPfX_Ch-cOTbia_iBgX8l0OftrmIueilo6Gn4XxufKlAf1WaYCH0Tx1vGBPRKjg6TKmfY-laKy9FhxhmrQhYWj0cU2K2TcKO6_mB8dElOniBXZep-XbBY7f2WQ7OLYNJ2r7JhMyTTid6CsktQVTgY56X9MUNmch-UMAsmHX-PmHYpekVRkyJl_e-cqwZ4Ak50fGZtmyPLAuxWqZQv5JZjbJNJNg-s1xexjtubEQkUE4DcTgIkD4K0IemvVKO0PEbuDG7y8SG0b8Bd9VUytVVW6mQdj0XLO3wD1YuH-tWTd-7-95cDxeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش افزایش سرعت بوت و بالا آمدن ویندوز
اجرای خودکار نرم‌افزارهای سنگین و انیمیشن‌های سیستمی از دلایل اصلی کندی بالا آمدن ویندوز هستند. با دو اقدام زیر زمان بوت سیستم را به حداقل برسانید:
⚡️
۱. غیرفعال‌سازی برنامه‌های استارتاپ (Startup):
— کلیدهای ترکیبی
Ctrl + Shift + Esc
را بزنید تا
Task Manager
باز شود.
— به تب
Startup apps
بروید.
— در ستون
Startup impact
به برنامه‌هایی با برچسب
High
دقت کنید (بیشترین مصرف منابع را دارند).
— روی برنامه‌های غیرضروری راست‌کلیک کرده و گزینه
Disable
را انتخاب کنید.
⚡️
۲. تنظیم سیستم روی بالاترین کارایی (Best Performance):
— وارد
Settings
شوید و به مسیر
System
⬅️
About
بروید.
— روی
Advanced system settings
کلیک کنید.
— در تب
Advanced
و بخش
Performance
، گزینه
Settings
را انتخاب کنید.
— تیک گزینه
Adjust for best performance
را بزنید و روی
OK
کلیک کنید تا افکت‌های گرافیکی سنگین غیرفعال شوند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrmJCf8JH_5YSD-Q2dWciaftnr8iDWS5wd87XEkAay0-jWOy8BMuyzcARJ_7jyaxlLROVrUryQvbKH80GTFSOY6iRlqJHEBa_syf0flrYtg6KMf9kWrpLH1jSFysk3ZnPsA9GB_Yo40pkNrtiwxuczGfnYS0OJHrqVq6825hG_3f8f8a-XZ3Si9sWgja9qlAj5AHUKtkcSmrO-cwW7VPWiJy6atksTZjQMN4feZWIPuZQVeuaqhMmeoGp9uP-jqe9DO2oJyTnnj4OvJzDwnNBQ4Y2nD9CLcRIMsxV4lRcEDn8tjUCZ3vp4Uv-OJGSRrL-h3rjAO1v8hK4-fXNIGnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttUx1MVnzBHlMoxLMJSdDjAaGZnpobVDT6yHLinzpw5eKWFW5JP_28kfSIA3XIoW999TMmenYj53AYaLCVFQoJt6UdR3sdFkVI0y_G8WCssu5oyByEKxRfK45qw7pFUkPdXOLF3MaU2s3sr5avWE4UiBPw4gkgKWDiJpb30KIZxRS5ghvmoHBYQ7_MORJ1l-p_EFqa--j3rMJt4cfU5NK3QS99CV3eLDbx4woHoVHQXjcXKnbQnmJ_k5w798hUpiVT4mfDP_7EW4ZbmzD--_Bz2PlHXNNCeTCeOkTBsTzlmMUBj8xWSbtjWMTMvUKwYNHabjWIzcpaOmDO6q7FfEBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک پنل، ۹ پروتکل فیلترشکن! با پشتیبانی همزمان
😍
🔹
در این آموزش، نحوه ساخت یک پنل حرفه‌ای با پشتیبانی همزمان از ۹ پروتکل و سرویس مختلف شامل OpenVPN، WireGuard، AmneziaWG، IKEv2، SoftEther، SSTP، L2TP، Cisco و Telegram Proxy رو یاد می‌گیری.
🔹
این پنل علاوه بر پشتیبانی از چندین پروتکل، قابلیت‌های متنوعی مثل نمایندگی، مدیریت حرفه‌ای کاربران و امکانات کاربردی دیگه رو هم در اختیارتون قرار می‌ده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو قرعه‌کشی اکانت هوش مصنوعی 18 ماهه داره،
برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJC8bmgigh1nNjlahrn3EHbIuQKytqDdPLV49b_rjPnqCHKn4MyrNl1eL2E6g9k2nOM-rF0uNs8mWKIRaKWz0-nrVk2Whj1gK-QqoEORferoejY8DVKPKfybVIoq4mPObn5Y_L_FfLvXRoX-eqVftKlKjM9M01UC6nFP18iIf7posoQAjZa2MNEuS64tkyKDDG97o_R8MXE_lRQaebcDoXACJq419NeEm5HApx26gPWJgsiwB16U1d2UhC5XjQl1oO-U1WL_pa8eHK6cci5-dGnx5tLa90mKzxS9L-Be-OFHkt-vUUZ-BhVhMZmpl_pTvDRKz8x_Lp6sNwHWk_lj5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
حجم ویدیو و عکس‌هات رو راحت کم کن!
اگه برای ارسال یا ذخیره‌سازی فایل‌های حجیم ویدئویی و تصویری مشکل داری،
CompressO
می‌تونه یک گزینه کاربردی باشه.
🔹
یک ابزار
رایگان و متن‌باز
برای فشرده‌سازی ویدیو و تصویره که روی هر سه سیستم‌عامل
Windows، Linux و macOS
اجرا می‌شه.
🔹
پردازش فایل‌ها به‌صورت
کاملاً آفلاین
انجام می‌شه؛ بنابراین برای فشرده‌سازی نیازی نیست فایل‌هات رو روی سرور یا سایت خاصی آپلود کنی.
⚙️
این پروژه از ابزارهای قدرتمندی مثل
FFmpeg، pngquant و jpegoptim
برای کاهش حجم فایل‌ها استفاده می‌کنه.
🔗
مشاهده و دریافت پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشب روشن</strong></div>
<div class="tg-text">چشمان یک انسان دیگر باش... فقط با نصب یک اپلیکیشن رایگان!
👁️
❤️
.
تصور کن گوشیت زنگ می‌خوره؛ یه تماس تصویری ۱۰ ثانیه‌ای!
پشت خط، یک فرد نابینا است که فقط می‌خواد بدونه تاریخ انقضای این خوراکی چیه یا تابلوی جلوش چه آدرسی نوشته. تو توی چند ثانیه جواب می‌دی و استقلال و لبخند رو بهش هدیه می‌کنی!
✨
برنامه Be My Eyes داوطلب‌ها رو به افراد نابینا وصل می‌کنه تا کارهای روزمره‌شون رو راحت‌تر انجام بدن.
📌
چرا نصبش کنیم؟
🔹
کاملاً رایگان برای اندروید و iOS.
🔹
بدون تعهد زمانی (وقت نداشتین تماس رو رد می‌کنین).
🔹
حس فوق‌العاده با یک کمک ساده.
📲
دانلود:
نصب از گوگل پلی برای اندروید.
نصب از کافه بازار برای اندروید.
نصب از مایکت برای اندروید.
نصب از اپ استور برای آیفون.
📢
لطفاً این پست رو توی گروه‌ها و کانال‌های دیگه هم بفرستید.
شاید فوروارد شما باعث شه افراد بیشتری نصب کنن و گره از کار ده‌ها نفر باز بشه. مهربونی رو تکثیر کنیم!
🕊️
✨
.
@shaberoshanIR</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts4Y1v36W87zCEHKWtHKoAkjHBx4WEyKAoMg6Yl-Xf_2wmhAtJo7NRG_2hrMjrLN-wK-mhDPm_o7euoG2B7tJrk0T6uMOUqFn6hM2muVoaOY9uPIyLSseKylXlQdS0THD2GtdclO3Z-vYW0WhCCAFhjxZAUxszPl2belV7oq1UAsNut2ZaSVjSPFlqxNw8skJurSfR2EdOsFeiWydd6EMDQ_couWkYQDzQBG5GYCwSBq__LHxOvhY7mxJAWJAQDU2XPBkoOX5bnJjJH_WfOeorGXdhaNEOSdj19RQm5gSxfegkqyb_7WSPuc725-lDzMpbjghBTnZMExqxpC8LQDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج جمنای از محیط آزمایشگاهی و نفوذ به ۳ شرکت واقعی!
گوگل اعلام کرد هوش مصنوعی Gemini در جریان تست‌های امنیت سایبری، به دلیل دسترسی ناخواسته به اینترنت، از محیط قرنطینه خارج شده و به زیرساخت ۳ شرکت واقعی نفوذ کرده است.
🔹
نقص در اتصال به وب:
دسترسی اینترنتی ناخواسته در محیط تست به مدل اجازه داد فراتر از آزمایشگاه عمل کند.
🔹
خطا در تفکیک هدف:
مدل قرار بود یک شرکت فرضی را تست کند، اما به دلیل تشابه نام، شرکت واقعی را هدف گرفت.
🔹
ورود با حدس پسورد:
جمنای با کشف و حدس گذرواژه‌ها وارد شبکه‌های این شرکت‌ها شد.
🔹
توقف خودکار:
مدل پس از تشخیص واقعی بودن محیط، عملیات را فوراً متوقف کرد و آسیبی به بار نیامد.
⚠️
باگ دسترسی اینترنتی در محیط‌های تست برطرف شده و به شرکت‌های هدف اطلاع داده شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhcdLNpjtE7WADkNP1oQGxM4q_Zmqh3xFFXVNyz_e9OmqmrzLl4pg7eGPI8D8k-AQn_pbCv3h8LLq7AggCjklL6exhFz5-4QXH-CRi2kxegS3IcgSy08t3U6QnKW9_Uvk6ZNrdc0mgeaBArBKjITymxFwWYiVYhPaiykEVU_7vRAP77JTCSWvuA7YUguTWQmvAgVX9UH2G_BQ0iYaFEp84YjyAgsjFQDwyylqk-GB6Owz0e6gKgkXfiyVdVOSfqCBJbOG3wdoUhokL7znh7OTiCQ6JqTcs2QJhD2aApiYnPowU2nft3pRfFQPn3rHdLJ5EL88Aqh8-6nx86uH0wu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توقف ارائه خدمات میکروتیک به کاربران ایرانی؛ روترها از کار می‌افتند؟
شرکت میکروتیک (MikroTik) در پی اعمال مقررات تحریمی الزام‌آور اتحادیه اروپا، سازمان ملل و آمریکا، ارائه خدمات و پشتیبانی مستقیم به کاربران با IP ایران را متوقف کرد.
🔹
روترهای فعال از کار نمی‌افتند:
سیستم‌عامل RouterOS پس از فعال‌سازی، لایسنس را به‌صورت محلی روی دستگاه ذخیره می‌کند و عملکرد روزمره روتر وابسته به اتصال مداوم به سرورهای میکروتیک نیست.
🔸
چالش‌های حساب کاربری و لایسنس جدید:
در صورت تعلیق حساب‌های کاربران ایرانی، فرآیندهایی نظیر خرید لایسنس جدید، انتقال لایسنس به سخت‌افزار دیگر، بازیابی کلیدها و ثبت تیکت پشتیبانی رسمی مسدود خواهند شد.
🔹
ماشین‌های مجازی و سرویس‌های ابری CHR که نیازمند اعتبارسنجی مداوم لایسنس و تمدید هستند، بیش از روترهای سخت‌افزاری با ریسک و اختلال مواجه خواهند شد.
🔹
با پایان رسمی پشتیبانی از RouterOS نسخه ۶ در سپتامبر ۲۰۲۶ و عدم انتشار پچ‌های امنیتی جدید، مهاجرت به نسخه‌های جدیدتر برای سازمان‌ها با وجود محدودیت‌های جدید با چالش فنی و لایسنس همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=R9cb1-K_Tb9g2bS0120QVIRwtaYV1Gc0OENbfiU1vsZxeaEVNyisJ44xnkfIuUrRyJl6haR3YjW6wPUqGYiHze1D3lfkbKU08DO5uLPJB0ULT9YYequ332-HEGl3dQlqH5cvdIikeDx-ocbmm4lfi9i-3m1JfF17iaV1mSU-ETTmgk4mlYR77UGXYnXdPR7PDH1sRcR9YdTrXFTH5w32LF2gAyG8ZInLeYtGGH7RrjIF_nyAh_RMufPRHKsbylUqU0ILo1f5PIGdenIU9BLxrmU4qcqRioT0kkQUdmD1p0FkPx-mCPw2o8PG6jVLxnHwtRfzVyVilVWQkkW5gRVQug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=R9cb1-K_Tb9g2bS0120QVIRwtaYV1Gc0OENbfiU1vsZxeaEVNyisJ44xnkfIuUrRyJl6haR3YjW6wPUqGYiHze1D3lfkbKU08DO5uLPJB0ULT9YYequ332-HEGl3dQlqH5cvdIikeDx-ocbmm4lfi9i-3m1JfF17iaV1mSU-ETTmgk4mlYR77UGXYnXdPR7PDH1sRcR9YdTrXFTH5w32LF2gAyG8ZInLeYtGGH7RrjIF_nyAh_RMufPRHKsbylUqU0ILo1f5PIGdenIU9BLxrmU4qcqRioT0kkQUdmD1p0FkPx-mCPw2o8PG6jVLxnHwtRfzVyVilVWQkkW5gRVQug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
ورود مستقیم آنتروپیک به رقابت با آفیس و جمینای؛ معرفی قابلیت‌های Claude Docs و Claude Slides
شرکت آنتروپیک با رونمایی از دو قابلیت جدید متنی و ارائه‌محور، چت‌بات کلود را به ابزاری جامع برای محیط کار و رقابت مستقیم با پلتفرم‌هایی نظیر گوگل داکس و جمینای تبدیل کرد.
🔹
ابزارهای Docs و Slides (نسخه بتا):
کاربران اکنون می‌توانند مستقیماً درون محیط چت، اسناد متنی کامل و فایل‌های اسلاید ارائه ایجاد، ویرایش و دانلود کنند یا لینک اشتراکی آن‌ها را برای دیگران بفرستند.
🔸
همکاری تیمی هم‌زمان و ثبت کامنت:
همانند گوگل داکس، فایل‌ها قابلیت اشتراک‌گذاری، ویرایش گروهی به‌صورت زنده و ثبت بازخورد یا کامنت توسط همکاران و خود چت‌بات را دارند.
🔹
عرضه و دسترسی:
این قابلیت‌ها ابتدا برای مشترکان پلن‌های Pro و Max در وب، دسکتاپ و موبایل فعال شده و به‌مرور در اختیار کاربران رایگان و پلن‌های Team قرار خواهد گرفت.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJdpEcd0bdvXKTGnY22KWvIGktQ4UpqIWDu4RiQSlgRIhn0XtdCU0Os0_mMLE7Iery3Gto8DkfeS2l-5Rn44Axg0yI2zgpYpECZV7qN8tppyySAfwa5YTJoZXjHPso9Ff0pB9u5xLj1oRwcj0h8GYOtRbyFI0gdSc4Mv-3e8nqSJHqqDkNW4JOJz0DMLpeYk1l3tWLLy1iahBvQ1KK5ywnbxA14v8MEjfy3PgduTjsnoHpnPasDEvV7I78iSEx87zlJk7eM9C6V8GztJREs0ZNPAS70bb_cUA9pATYlt4Fn2h4NCeGWZ0RwF7SrA1q2ysvOolH8VzceSKuICiF5Q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbLGr-sPit7hT_Hvkkx9HvJxcilnczNnlsyZwuy_Yax_srvwCohQv4SsGgZwW0_WFQYlVlqjKFD9d9Fd_2DGZ9RkWAbvURItfoPtEU-AtQZ9dROi0hlT2ghan_KTFQwLngrTG5olc03xhkytYwnz0zcNwbSE8gE-1LemqKEg7cO9YAadXUxHkkUOkIgKAL8PzrKhaBQN_gLr3jDPzSEHJvfJdraLtKykGDv5e-UR8XxUW95nTEvEb1gpM-fHLepEHFFz4RRXYFJCEgDyDxlRASlRqOsdFVDRvzTdKN4C0VZGtjpVLyYPOy2cvzF_iv6TSoTFKgz8SXfqig2Wh9C2xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEz5ovMMVIHp6dhw4QwzQbfBIo7Yp6EpNzHI36F-PsEQqbcth5So8f1QimFkVJY9ADQ24Uy76cZGvu2lOM-Q9lGnvbtymswdEUPDF6GpEPvAGB6x-wOceX9oyq-PZwOYnCRr96GynXUPwg4bE-ryXTjuuCzTEErnq_b_Vys5g-0oL8PvFd_hYZ4enfr-0l6A_kAX2vH7WXH_lSj9hu5vwZrytwKc6BXa3AMw5LTz60lYK4UHRl_XaWDFsI4NlvxUXEZ-HJ1x5iw4i8uhz_K7CvpRtPeDrNpRfPiJ_TxDZ6wKT6SRxiZXdQdwLkrSCcFwkB4mkBBVH3TGqpuXvHEsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtgQvwMYa0ohFcYYOsuxN9haI8zPcs1Oe8wyPdi-yd4tvLdhkTJ54zNRmazV9usUOCygeEEMVe7P7MHdTMo5aNxGBFCwLEKvMrYomWf60lj7kFi6OeKOMzoGvKLh6wJdJGefbUcucyp7mkrnbmPytnOx3-y_Y71tfVPyoMKkrLpjjouxd3f2RBXKlNUwy3yEANnp3c7Lzrphhju-HLmLNEGN6j6zcXWFdHUiSXMPtFsqiYlt_STYghi4G8oaSb9RMwpStxXIaR_U4MTGZccgJZKKBpDScQLHyoGtil5hVtWyt0KZLWtPo0j_UG7h2Kr4y0EAp73cECShIGAiMr-tbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJT9D6_dXY9f6wk3w5eFgIwpbjI9IlG94P_WkGgP07vYXGov6Z2GLP_C_u-ne46LHJLzonFSkTEzWK81JRvcwTXtYlzumCjbLsfiEGSZ1reJy_Zx0uAJcsZ9_jPzgsTb4SPtLje1BuPWeQM924Wg5MrYa9CnPRL4cSUjCwQx-g4uep8CqtgSWBvnQdEseL0oQfqLzMidUjkLR0YmB8hAKQjt00ky3DLdvDOfi7I3j6Q01Wqx-Auk6hCPeW_NacC4QhdB8eVKbTmFoM6bQTvbUwyDX0Cgt72I5_x_khl9_tZBawGZXuhy2AtpXCLywBW7Q96YCMgdF7Q8eVvvLzO6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRBf5ytdUaQFGyOaF2nmDVysgyZbFsfYiTuMdwkoUcLt0MlVUY3ckmWyQY_Ihwz06tEtHJHjZntWWrHe7tIGGAcIOyE2bl0vtX8Rj85wNko-GCvdZhBdaKlhE4SmryMdUmt_mjwRgHHwiuCNadD0bq8SHiMZOKW7h6kdxTyxJT8egdWZtHSd7PyGrjMIK6srDnd4NIAcF_e5JEhm_5J-nhdgJjQzL82pvMx32aftUfFvK9cZox2SAl2cMZ0BpcHIrmpC1xAeosEvGHuPlqzJHdwXJz1uEDEHcR7h6Y69t5H4kf-6PtKcGVWjLP9eZoMzwLxtlckajAtB8STUgAHXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=txmdDycft5VVBn46n4a8BYTOxg8jo6I_m-tuyY5BG3FrMxekWNF-sBAJe4bIyN7--U3VWoQcUbwUX9wiqY1cg7ba2S6GHopndsgPAoNxXiV12GT6DywqmTLsq9IBhQNrBTv8bkQWVApXPVIkNPEXNHrZKZkA9-NjybyzjJbXY5LnSZi3kF0eQgWPEYcYXPfVrkzfXtL23L00sp3410pH5tg-s1dTt5rmbj26RJd7SnuYlFxPCeA51W2QVH1H4xMZhAHIoFRQGR4tlGcYjwNlFuxI_7AuzDBt-afomRZn1ItI7SXf0yxLhNKVocflFME9_t-JDdxdXs30C3G7fLP7lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=txmdDycft5VVBn46n4a8BYTOxg8jo6I_m-tuyY5BG3FrMxekWNF-sBAJe4bIyN7--U3VWoQcUbwUX9wiqY1cg7ba2S6GHopndsgPAoNxXiV12GT6DywqmTLsq9IBhQNrBTv8bkQWVApXPVIkNPEXNHrZKZkA9-NjybyzjJbXY5LnSZi3kF0eQgWPEYcYXPfVrkzfXtL23L00sp3410pH5tg-s1dTt5rmbj26RJd7SnuYlFxPCeA51W2QVH1H4xMZhAHIoFRQGR4tlGcYjwNlFuxI_7AuzDBt-afomRZn1ItI7SXf0yxLhNKVocflFME9_t-JDdxdXs30C3G7fLP7lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlQkGF8Re4ceJBQxfkAyMOxQf7fmCKg87HqHHNQ7tU19TLXYqyyYXf6IfHRuPiIp0TlBNIahQfZpTHPaIr0Bk2hoTwb9vtPLnvS8zI7LcIDqJTfv3RPK5W1IAXo-RVfw0CdXIh8MCdb-VI4OXh4jFT4bP2Yf6AeRGkaDHK-cmZlgOCUBM9M8BeHqzGW0cU0aDIKbXo5Y3wB_1takRpA4c_BSmjsSP8ynGy5wbqSpxs95Ux0hdEzRikPd-s9W9t_MNAPExnWuCW9dlxWdGmXMq4oEU9eCWeNr_PHAl4zK9iuOOZciP4feLOTDtxXqRA6ZiXDMHSCQwnCd50CG_O-u3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To4Raj26NxYH1y1UGfn7zpIcEtNmmZm3BaMGYolH2ZqBzP6FXXhdx2PS9L1VsiMs1Mh5qeWVAen8yFD7MRpxZZ3nwVgjcwMRkcPZhIhuHe0HNWbjpzJQl8jtWEd_ztbIaw7ilClfxqwjW09EtCmmNdy0kJR2svB_rs_7Hat-dljPb0JEJUBP5L0S9fOpp0ludXlAEdUYrOnQ5PbQj_uLglkCeZfJ14_bpJRgg0VGKLbMvrLOTjSqO6-BaZXF-dI1GYTNRFILcHguQr9XofWFMWBMTuCasJ94tVKtILQqqn3P4Kuls3mCQuI-68coHHsgZlj258LtN2eJDd-UKyLklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX6NWL5kj02tgXCESZ1lAWgGcS5jsDOZl3SGHMNqii1ZSikCPAktVrSivozs7RWHZfut5B7TKyk12GeEbPjLb8sbCxs8JIP5cW18jhjNdqmdZDppukjJ4wdacktiVw8_AS49x-Uq_SVmQ9tbMrbrFFlhkfaDHTG206-Dhdy8hBq8Xy3H1Tay9lBct1QHzVhuZSCVfOLMSfqThwPjswzzx3hRWHdLsCb1m7R6dcKH-9l-Adsk43F-GDDR8vUWIoErmuZ4ZUrg6H_2h_UiHkobBQy6gu8TGO-ORsDcTRv-t4dNG-ZTB2aDly4dEtucIaQjvuNDe6CNkZbk5xCBEmMO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFILeHNIj_EAbbcTEUPZp-_ZgvPunoZD8WF9capzE3b5mcAEZvyPd9p2I-MTiaH8uKQUsngFlnidvxsRCWjxUpoF0etmoqRcBKPHb-funuXdjcu3mzJgT74ktQ5WqzzSpQjxpuVWNQhiuCmLIfR0p3SgQy-jxNrwQ3fgcmofThJlT17OCi0sogvOnt_QwwzFj_DNDXGeukUZ_4DjOXNugAB-Z6b0L9NTAkqvaYvtmLwpgFd1coifZZMuenpfnYv9wJwJZgFQVziGTm0I_7Y1u7xQPxcLIFtzj5dbaYAiXSmD-Wm1Uy6rqO_7HlmXcfZbI31WQCKMYrj-40EFxmy5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkkepjY1Q2XvutoUhuen_HwHnmrxl5cXC-cOqApRuCDGiTny6_0QJxzzHOmkqzH6xOmnVp6LUw0d2ylELvO-SNkvOX-LwpqNk0sjrhoT0DPpTrvb1Nu01GqXuzEPekxh79yf09OhNJNVJh0lsk2VgWwuSwFwv5-J5SOOUHmW-_8HmVJdlK97Pm3OcdG1VctWEI4-UlmCFkqd9RhomlmH7Pff7mI36EU7p_o4NEIcOyYW-7Y431rijKdlIIQSuYZYK4pR44yfAJtdddB0qtuQ6sahvV9NcLm8UPmrbeomCzJVouKpMeEuVEW_1Y4wxmJg10qC68dcTQTY_opGIjZw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9VCe_ukj9LNEYDpDr6DWxQAs9WT7wx9PbAtlBTKm59uV34pefLBkfwWdkDx_olV2NUgiExtY-c9ifmwi-VlQN7SzVuAZNZG2dQ-9IPg2y8PenbRX2hixovcbRZIN0jOzCNsMjDwChflzGVNoEoK1o6ioRj87LmrJiacPICepTao2WSK-J2oEp0Wg7Vd8tZbk69rWJxiEdJg_jBJeNN0C0HRuHWqE8InmTiIMEUmwOiK0bbx5Gd1kBAYTWoB03AG7UQhavjiI62c8myCYnNbKTTktHPxCtHnPepVfbMq8ENyLk1qEQxHUYjp-liLLn_PLuKKg5Fc7RAp3BFMn1Cagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spoRKh94IbRmDEE4K11luNVQaCLuj_AXsP9pMQalPAwDYCE_eN5bQ2d-RRmLRR10vMKYR3fvZy5dUjEtrYVhGLMsKy7A5gDkTVtc7Z3BAzEY0aPUtfWHuYWoalnUkrTLvXcqvYIQ-Q0_GX-9GGI2UH0sYPQxdxuefOW279AhrMdtrRAtq3CHR3PSoB09Jz7urQWNrKS0_c1p3LE3GSDob_R3GYksTlBM5WmVPiVKwE4ruABypwlaXc-ZtCD8s0gr19dLSObs85Q2u8rNelHVhEwkFaW_NOPLipJ1oOtbvUANnywfFCEuug6R_I7hQXriDxm6Ba4connqheAgddvUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=ToKkrfCRacx-R-yOm_lCtLTYvPSTH95gfJmeNNFfORL2upsYf9UI1rDE9KzKql23b51Wr3q6arUFYNGJAOF-h18-6VQavZs4NlcFDJFwrL3GllynCI7co-H78gesr4lRFsOso722AxXLFx09LTI0uBuc1xZxTxgljqs965N7UVSW9zEKzU8MHhydffCKe3w3V6T7CWUy9Py8dNolBRflAzR8yedTeODQfEIU8CRien5L4TwqnI0svzyHM9n7yhEgObYUj_Ycmx9j69nzcptFvXIsnpB9dC0IdXDcV97jKugYndoKN1TvmpbN3FPUbVWMj6kl1mV9dvewNl859ZhHvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=ToKkrfCRacx-R-yOm_lCtLTYvPSTH95gfJmeNNFfORL2upsYf9UI1rDE9KzKql23b51Wr3q6arUFYNGJAOF-h18-6VQavZs4NlcFDJFwrL3GllynCI7co-H78gesr4lRFsOso722AxXLFx09LTI0uBuc1xZxTxgljqs965N7UVSW9zEKzU8MHhydffCKe3w3V6T7CWUy9Py8dNolBRflAzR8yedTeODQfEIU8CRien5L4TwqnI0svzyHM9n7yhEgObYUj_Ycmx9j69nzcptFvXIsnpB9dC0IdXDcV97jKugYndoKN1TvmpbN3FPUbVWMj6kl1mV9dvewNl859ZhHvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2PDc4Ck1M0RHdT-1i9UJPOU5YGZMjUq9kSC_g5-k2-khjqvxuOhvV33yyAtanIP65tFSIaGVOuptasNyi6LhKM2FsTyLM5dIWHhiARdQrOs-P98Pzav7JFOk1oxcanrqhn9kkQGuyvsDVqb60zBfKsP32x3Taj8--AeOp4Wypta6TN8NKVcZSor6g6Mui2oqZe_mw7N7e9cQtdvhG_BiYDaWEyGP080EcmGMSXFd2xN3x1lzuIfPnK4XG1pdnlhNEYrBcN5xB3uGgigt17p1frylGWABUdP40xXZYfajdERQTZN_KE2hqxh5fBl-0dTDc9gboa8KFprEIFSMjrIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=IpMhEfTwsQvq1-iYOpKDK2G1zUQyp6qJwrdXuvRc-SHAIE7IGB9kB9OuS1p8cPba7RcaZR5UMj_osEE0BiNRfkFCCBUn6SnNrZL0EKixmIyP27LkThfXtRi-BDY74RSKQeng3jv7xfq_gSUZAuwDOh9WMXxfJdqcf2A3HpFwV743cWPyT37C4NcJZFStdTQBZLW_nJz8ccY85452dqRh3yLXNyMa5CKQaiZUDu6ATm0od42aIPf4SbfHUXpOSllwXbp5sIp9GZWj44W96ymm0LjD-c1iIFPebXuezIymREZJQM8Cnf6nJMzfb8mHzHqs5tvVLKkFvDrDLzu8awkGgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=IpMhEfTwsQvq1-iYOpKDK2G1zUQyp6qJwrdXuvRc-SHAIE7IGB9kB9OuS1p8cPba7RcaZR5UMj_osEE0BiNRfkFCCBUn6SnNrZL0EKixmIyP27LkThfXtRi-BDY74RSKQeng3jv7xfq_gSUZAuwDOh9WMXxfJdqcf2A3HpFwV743cWPyT37C4NcJZFStdTQBZLW_nJz8ccY85452dqRh3yLXNyMa5CKQaiZUDu6ATm0od42aIPf4SbfHUXpOSllwXbp5sIp9GZWj44W96ymm0LjD-c1iIFPebXuezIymREZJQM8Cnf6nJMzfb8mHzHqs5tvVLKkFvDrDLzu8awkGgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akmX891Ywbcwnji3B666oFUbqQj7T5FFYeFMrX3wEUc6u0smwIZpIPgaOtAjyKjimR11KJnigoLEs0xmTvHm_aBrLxkyXzP2CC2R6FCjpG8UtPYJKu-lRQHO2C6AH32u4au2FCiHun-rbmrmQMUwV8qmHGt3MDR8cZh8bmbfizKE95TfU0xy3jJzz3xHb9msLK8EGxM0P0VLnFgbb1sYZ-jnS3COzkj0dIR4KYbwAXYteSGsCvWzKT0CJAmKnszMcBeCSOlY5H6FyxrVn5H5V6b19eLsEywXEGLxgcSxmrF2Q8rQWH7BXDsR4E7LACA_UQtfvGYQnHhE_yzGzBUCzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghGcX_CiNbcH7JFAjk-VCez__IZ1y9IQPq1Gy_zLcdOjWkGaCjzM_M_SFdsM8eWsu1dvI4FOAtAqsUHckb9aSycyYyTHV9VfVsDIPG7VeDyS0VscVoPChRB9ijtbJaIHQbNR83kjO9xVrpQzbT4czK5Gz30CHP0UTbYAmicRnBD8wcvFvMDdkjQozo8PpeHNavGZD-pOoLfJXOxF26KVN_cZd7O0p7v5aFSvU8zRF9FOECBLuPEVmwZSIdbsIdwMqvcrvw-IDt1-Hdcy1aF_PhZccpPvezJuaBm1x6p9VEJSZImJ4dGEauXB24WrAEbhNNHJAUiQWf7-jyVFh30bew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/an5F48ayvTSenxp1X6JHGJIuU_3xkURBLhgD0t8GtwKmreiy8OoP3pGi6-OgT4kdd8X-IF6mYwsYNywg09_9OqAzq2MD230-S7_GbE5TSKeOoi1bwgyVPSKHdwYB9eI4Zm183s8sJnFHoTRf9tUu-F94Jl0WGzFnpZF-TZHzmATzk6L_ea44v7I-upgfUTZcomsSsgu5Sfj5TIoKGW1_iIIn6jTcvPOgr6dyK5R7oAsKUIvl-YyY5wXIXvtmGEV0eFExwbQWggBn3lSbKaZ0WcyCD6Sxq3FvOePv5VwLeptaZev8SIkKNemTfCpmnWaH_RHtGSUy9T25nm-OUgqJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ponF1baqI_Fl_yNSe5OQYnWTyOWIvA_IlCCNOYmJJmApgJZUwqiqZVYoKnG5AscaXEoXBWrTpoWKrGGTu03ZcNhrMeZVYiQrmzfvAB7ZglTyCgVzDtDCoxo_i-YV5SKq85Y0bfc2y3C0rJL-qQxwpNPvJZ1y4r0wwajyJrhRQdhILI7JJADvxX23WkxjgJd3MPASsM3M3sd84F8zyjSrSSKrc0GnRcL2wgAPAnRRcAg3N0ZZGU_12alXs8nEpvuIG_PoE2mPO4urV6UyquShQi6x5R0FAYmdIpMuynPMhxQ_u_5Z8dhMO8a6l4D63zdADR5s8u81s94IAteoc-1f6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTO4lnpMhi6nu0ulbDg8SnVUrdmcwVauICCe2ulXcfEbIfmFu4qTEGj2tPu7oS1BD0kx1J6Gyj_v3ZE9q_k5NGO06s1yvC3BvQad3YPzqfvzc4nmIwRPzNImHk1LrxvCBg6X2YH5JIUnt8DFxhMv2tAX-Ob6SBQ27f6-LZmf1K9hWiv4pe3JcE81-cOT2AhRQTJqWFXlkpGB7aABv1by1YpiAx1WnvaRu8sSqOw0IUfL8pe0458tDhWwHNs-ZShxTzcCUXZFXpdE6k82Cf49QnVCixG9DYTVxa-fbSa8yYWCZh0pc0Pfj_4q-Z7X86uSm_laOMvCsgaMsxKxbi-KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VppaBdluR6DzjO5z0QQqFebPCiYImBrVfi5mfOIcj-VT_raqgcS2rn-fB--ZvzlLw20hcZBvmLyTapQVBzCW_GYb2lRcZ9x0eEhe1jVysn5nmwHt9YdBQ4lfmSbX0IFw_aBl9ZwdDmwBIFimh7nGNw6HB6z375dtVxjTYfgC2UTYxuz0soyAEUFY_WvLeP7dc61abifbfeM_QqMTUtZepbbrZq4CAgd0Skq6i8dVDtPGDQZK2dyGyRpQLbg1-1Aswj4QspSdkX94Iij_ivULCIUUjQ5wYIfyWppTklQwrKoF6xnSCuzdWUoKaDqh8DMCMBOmx5ZdvZr6_o6MhNaKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF4KfoRI4rEB9dCIBd2KBGwqBTNAU25D158KyskhkSP6Fg3BQTqL_Zb8kzjMUiUIpKAmpVGmXfPETQDFWiE3h1hMAHv_bgQRMkcT4X0wueN1upXXHCrv9enyE-RSh0tEniEc-Nv7ZGOWsa8vOW9-1qs_SefPtw9aLFfOkNasmkpF1OP34srnJcxLtGyQUnCNlbwvTGq9j_3TiZt6LEaNqdD_Csl5rgyr381zcvKWZQXQXxhwhWPr-HG4AAHWSrjV23XO9PnCdIgwzsM6yrkdrRcalQCm0e8XzPWUhpADqyobMGhxBmknR7NvloQHpbkbgBHy-R5LnW4SvcUYpX6K1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lppYFJ2fLxo3hUo-Cb-XbUsJqet-Rb0N-GkuR4AMoubL45NyXxu9y3TZpxPSYwMxhPuokg0yXQCDMVggAoneYY0Yqzc2f5N8pBZHp5IQpal2DKpFqvSQRpzTlcjrmjFYjACS5poBlEZ_A5V8Z96iyt-m-5bU70vWnSKHQKNbtVfSnFcYpwYjJYbbm5uwTDcleDR6qch_s0fCSexdZ6yG1YYoj9s2urAWWCBk_Vn1zSCIlyjcnJZLWrXOsfbDH5dP75F9aTWxUUp0eHFduvr5h4ngiMAzNLUxtUdXxhfWZy4cvDz6WeMRsiKd1hx1hfmwqUbzf3XKCHxGAFnf982ZKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=t2pxzc86QGmLuwxbKsgvgugv-XgUqZWo8vBqKZZFS13hml610424b-edfbMALYIdt-SsLfxl_Zj2w7RexLzAEOC0myrsjlClwNIQzl2uxfC379Jnxsl2KiSjDPT-sBCC8vSVHnw5GQbtuAUZROcO2yqGaKZgkdF15Watti6F1jdeCzK1VXKRf5ktMmGuVUHO4KgveqARGRGigvhae91oCWKtKqAnz3XuPEadExNn1utlA2yS2lTmpL3uZs5OGNILtuqAYaewZX_oNqACB8KWcOh3KwtFO6dBtiqKcVNcosdVKq5S-lP4nlO3hd3UGCmPpcAg7EJ4AMuhFGpBcZSt0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=t2pxzc86QGmLuwxbKsgvgugv-XgUqZWo8vBqKZZFS13hml610424b-edfbMALYIdt-SsLfxl_Zj2w7RexLzAEOC0myrsjlClwNIQzl2uxfC379Jnxsl2KiSjDPT-sBCC8vSVHnw5GQbtuAUZROcO2yqGaKZgkdF15Watti6F1jdeCzK1VXKRf5ktMmGuVUHO4KgveqARGRGigvhae91oCWKtKqAnz3XuPEadExNn1utlA2yS2lTmpL3uZs5OGNILtuqAYaewZX_oNqACB8KWcOh3KwtFO6dBtiqKcVNcosdVKq5S-lP4nlO3hd3UGCmPpcAg7EJ4AMuhFGpBcZSt0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjAl9oVy6n6SjMgbr19YvhrGGGwd6uXB0QW1srnVYIkZYJM-3O2NLsACJGlmc-vJBISQUWJ4GWcpY7URjS-HJBf5X1aCI4zVcJItTYo5_7tzmgIwi_VrqeJbfL_9MrdMS9Q21lI7-m1tQZv5urwQNzKuKhRLmvii_4yUcHyBZ9gskBYmpSOPcYNH0OLUpaHphBVU4_-u6bIXD2GhxJeAphPxbf1wVeRWPtJevV0MevtjtDiG2mgMpVgJEz3N-lYNmlDFUFSoR1BdpqzSi9DYKQrR4fdUxIFOLjKymaZbNrPpf0iKGt2iEB7k6ZjEWjl1dz5DcBZnAvQlkAJQ9IsP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4GDRh0pJEyyPRb4Lk_aNe0TqrkuI28N4GfYD7Mc-X9zQAZgdjzBbPMegzHK06ypbm6IZox3VNsLvy-WOIwAwEATusaFNZnvn2hovz8PBevV_p1Eg1B5YnUqVEEnBmivi4OwGMcNTd-zAwcgYhX5ls_vWE-1jwZJ7_LN1JNGTXz5zAwtiJhznm33UbVtpYECYtEI3q1hQo5-me8d5kGPDZAkwnHdUXSBpG0Clyp3UZwFar4h-DssfKzpGG-yAzr4dwT2vnT8BemVSBs2_Jh5yVdcy3KMyhI3vqQb5NBh1HvDmzVJ7Pxm8jxdy1AOBSG6-vTwvORP8j9HRmf_2gFlRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGk4OvB50gXAyyhIcCmTes9q3UjmIfRYAoTfm2kJxspIkJbMIdVxQ6vCxkUv4oBOmeW2Cx1TR-siBPhjPoF0tYHaIH9Yn3EbyAx6M0a-TU4AosdyrLbA9Aarx58bcCPPdWr61IRx2F4tcH6NUS48zidHwThtaXrFJAM69gaF0yziKpVzon-hseZJxBzuE1ub7bFtVnOHuuN7RymZAl4VuLNOoMkopvqREHE3ne66Ee7Pq0mHEOQUB7E4JEVcMr-OQG2PD6ak7rqZmfvC0h98lRSE8ehSVXI5dBSp0pysQ8xCMyBdLPMO6M6iXRUNyKSGpVWHAwb29TVQoBGaiq1_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtUC469NxUlBARbS2WJuORKu0pvQFugU7W8wVSkVFjfAwOTrDnLqFjMcaQ6yZIv2IHyhyvbmLRGGCLMfPh5Fh465B9YVbj3bmbIpnqD7qWcBl0-IdfnyZrU00MOK9nB4_Q31zuFgJFovDQkGFBlraf0mtJY5UhvgUNo_w_Anc6pe9RH2k0HH21pbnuppgVIjkLcl4yJ-Y-RaaLp1Pv-ny8op3P6dQPilZTB-XpfQxft-eCnfl-4PpOrVHE3hjhO1ZyQg2OEq_4ziJ32MNbziRAZ00U_QiQF7Do8kLo74uQviQ1LmgGie6mURvbXib8EsREX-snOFL9Oo934_uWHlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=IYysmbqyJxADvJtcewPonCs8B30UWInduD19uCCUwjRy5lFBEqI2gqI9ZMcQVDi7HcbOAsycKOot_rflBfUk_RnrdOwpTuHQy6xQlkvUqrOGua7ujmHk-ykznIucRv9ojZ4tQXXaBei_dWw9hoIvd4WIsRDNBnVtQySlmBnYoppqU6ksP_ImW2vpP3NQ3n2zhGnm_oOb43c5V78AmyKGar_dVQ7Y1k5_rH1ItG2NaNf3-OYBst6d5DaHZh3arIsrcwTnX32Cg3Ve1XIC7w6jUdwr3NUqQwPiBv9m1dqwFGmSf4KkYtKvovpwRPIXMe3vq8mfVyR2fxzNfusMR3sjLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=IYysmbqyJxADvJtcewPonCs8B30UWInduD19uCCUwjRy5lFBEqI2gqI9ZMcQVDi7HcbOAsycKOot_rflBfUk_RnrdOwpTuHQy6xQlkvUqrOGua7ujmHk-ykznIucRv9ojZ4tQXXaBei_dWw9hoIvd4WIsRDNBnVtQySlmBnYoppqU6ksP_ImW2vpP3NQ3n2zhGnm_oOb43c5V78AmyKGar_dVQ7Y1k5_rH1ItG2NaNf3-OYBst6d5DaHZh3arIsrcwTnX32Cg3Ve1XIC7w6jUdwr3NUqQwPiBv9m1dqwFGmSf4KkYtKvovpwRPIXMe3vq8mfVyR2fxzNfusMR3sjLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXL4XdCPuXT0Gf6Uj9dG9xg99RAS-b40LWTarAIl0tRZvRPgYTUKL_qoSwIqF5eMWW5rlZDjDGMjE_0ZPQOOHbFr1y42xlMX8abh3-kKhPasCtBz_X11mFQ-uYa-giHpRUpUDVNdnPobXvJF9H79jNc245LAs3LDHRVlKY3QLF8ejXBZ-CfvA3lUEiZUp6mqdv47rQEQVcHuObhr36ioMQIDmrYBbfDrb_pH2DJbtIqN8I2u4FsuYfaMhmYDIOi6HrvGov449PgtMWCGHNCKOdQXeslGq_3VTNEt3ZbHPm7P-D_aacwRq65HLxMmjW1CTQmWMZU1YZpWlr4NjJlVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEc2DHvYTaIRl0aBC8Its6WscYNG0PwwbtROeyNSkI7rmMDE_SQfUM9QPwldIPgvot3xI8q5V1sgusPAkLmqsEfZrsDhVrTsVyQeyQK-HR9Yhp2gqtXxR4kVQ725geZ8yuuuSUiDHFMvSATMVnw1wGKCz9UvrET8ZtI9wiW0v6pRPHCO-U5_WEXfxcGD_f8rX3cGEZ2KY64pf3o23jVGAGarxSx4CWEmys5G47H4Iw2DtPGVAoudTEilmzIvDR-GaLwDu1GqFNlnXyA2POcXow0pRxLXgmINTX0Db9mv2uFCMVBrOZ7geqZcdQtOzSPK1jMN6eJYTGi4C3uxrFvDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2pWplI7vsFjYdJddiHUjcSB2Odr6iOBz7nPiqTpgBBOBgNAuFPf1cqiYEHvoPjINZyYYGC2MM4fkpbdBGaLQG1JrP5t0LwNDEPXTXIk4XbVAN4-uUlc1l41VzfBj135goY534g88yJa7M5rPwhNmfxYeqeqoy8ULqZSNe2WKDoENdh0pGjT0b_0dEI1IagJTDHpWPbwb9oo_XK0FAp2UL4gGpauRlqqvohNePrgKG2Un_RgGgr-Yi7NdamGO_BKrb3F-TJmHuxUDsL2khK4mcQ8kDcYLQPGhqbJWCbszK31CxqpLwdgleeqXd5E3VrWsx1_0nQXV6eiDVallnx_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN7k7xbj8X1Nl-4yFN-Z_Uc5lr-v1AfX2V65GUM_gPndEPTS_0rpo19g4OwcLuVOKtXqRq5G3WJk3f0NSlmjis8aHVY-zZp5sTm98WaPrFxAd_Kc24WtwU0g2nGpRz8a4cG_8OoaX0_MEbzgok259ug1kSi2PC7-OasaB86yisQSmUG8d0IRAOL7yN75V4E9_FGJ-oDrIlXDW9U4rDIcN0qPTdiKC1XSXecxkGTJAlO_PlQs2iqDt6SlipWpOCXUesFF2eyiTpU6knZu4wLsQqmBxHDEq1RK1zsauFkTFAwKV-YmfucMtcgaJI1E1udhWBww5xfU7ijno2h54hJDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پنل همه‌کاره فیلترشکن (انواع هسته + تانل داخلی و مدیریت با هوش مصنوعی)
🚀
🔹
تو این آموزش یک پنل فوق‌العاده رو بررسی می‌کنیم که نه تنها از هسته های مختلف (مثل Xray و وایرگارد و OpenVpn و L2TP) پشتیبانی می‌کنه و تانل داخلی اختصاصی داره، بلکه به کمک هوش مصنوعی تنظیمات و کانفیگ‌ها رو براتون بهینه‌سازی و مدیریت می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🛡
چک‌لیست طلایی امنیت اینستاگرام؛ ۷ قدم تا ضدگلوله کردن حساب کاربری
با صرف چند دقیقه وقت و اعمال این ۷ تنظیم کلیدی، احتمال هک و نفوذ به اکانت اینستاگرام خود را به حداقل برسانید:
🔹
۱. تغییر رمز عبور یا فعال‌سازی Passkey:
استفاده از پسورد طولانی و ترکیبی یا کلید عبور هوشمند.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Change password
🔹
۲. فعال‌سازی تأیید هویت دومرحله‌ای (2FA):
ایجاد لایه امنیتی قدرتمند؛ حتماً از اپلیکیشن‌های Authenticator (مانند گوگل یا مایکروسافت) استفاده کنید، نه پیامک (SMS).
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Two-factor authentication
🔹
۳. بررسی نشست‌ها و دستگاه‌های متصل:
مشاهده نشست‌های فعال و لاگ‌اوت کردن دستگاه‌های ناشناس یا مشکوک.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Where you're logged in
🔹
۴. لغو همگام‌سازی مخاطبین گوشی:
جلوگیری از آپلود شماره تلفن‌ها و پیشنهاد اکانت به مخاطبان دفترچه تلفن.
📍
مسیر:
Settings and activity > Accounts Center > Your information and permissions > Upload contacts
🔹
۵. خصوصی‌سازی پیج (Private Account):
محدود کردن دسترسی به پست‌ها و استوری‌ها فقط برای دنبال‌کنندگان تاییدشده.
📍
مسیر:
Settings and activity > Account privacy > Private account
🔹
۶. حذف دسترسی برنامه‌ها و سایت‌های متفرقه:
قطع دسترسی ابزارها، ربات‌ها و وب‌سایت‌های شخص ثالث به اکانت.
📍
مسیر:
Settings and activity > Website permissions > Apps and websites
🔹
۷. عدم نمایش پیج در بخش پیشنهادات (Suggested):
جلوگیری از نمایش حساب شما در بخش اکانت‌های پیشنهادی به سایر کاربران (از طریق نسخه وب اینستاگرام).
📍
مسیر: ورود به وب‌سایت
instagram.com
> بخش
Edit profile
> غیرفعال‌سازی تیک
Show account suggestions on profiles
©️
پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aac_3WlUpbHgSDLHBL-Dykcu6gPnADXT-Ym7geYrhR4GfEButu3ztjG5_PnvGS4SYunsUQgapdLR5UmGGsd9TRypaqjZukn_Gf2siG2efYNquT8Fa2LwZ-1TmnQg-PIESA3cYwj8j_xaVud3xGm-UjpzGndKBSpvg_iaAqsDORchP8wngP5ygM9zEG2j4N1Cx1btWsyMU-PWzze3s2gEv6jwNyFh663Otd1VtoNZJyBvOps3jcerp5LtDEhyTSPX_6Ar8pefc3UmFHPBIHjfqW37pZC2-9IdiSRz49-kaqBqA3JwArS6PZ3uOjP5hGQxNrEmzbkFEBMBRwr65y87dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elDNKLb6JyCaZXa_q5eqdSRuW10M1Z2zJT8OM2fxaCiXKl8zClAcQ5YyHjJ_uqriJBJ907AmIzZwECOb91pYM_P_lfpHQFUAhKFQoZYTkMJb4rLQvColwwNOcqKvpoh8BRKU7xOy5SmbB6bqonAcQgU0aa_xKgH6kqbK0eIoltd8d0Imx26eKOR29VWjXwNV8g_Uj_3qQVPFfxXy8aIVrvTO28488plhiSYFGX__TL1HGh9qUhA4KhgTK9hmOWR7Lkk08X2Zn7PdCxQFwAdc3MkvQAAhUraEH41rF9bN2LRcy0E4oRxzm2069vZEv-_WwXYqx0JlTezAK9-X4pV1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
تقدیر و تشکر از یک همراه همیشگی کامیونیتی | مارک عزیز
در روزهایی که دسترسی آزاد به اینترنت و سرویس‌های پایه برای کاربران و توسعه‌دهندگان ایرانی به یک چالش روزمره و فرسایشی تبدیل شده، حضور افرادی که بی‌سروصدا و بدون چشم‌داشت برای رفع این موانع تلاش می‌کنند، غنیمتی بزرگیه.
امروز میخوام از
مارک
عزیز صمیمانه تشکر کنم. کسی که شاید خیلی از ما اون را نشناسیم یا از حجم فعالیت‌هایش بی‌خبر باشیم، اما مارک همیشه حامی دسترسی آزاد به اینترنت بوده.
مارک عزیز، از طرف کل کامیونیتی، بچه‌های شبکه و همه اونایی که نتیجه زحماتت بهشون می‌رسه، بهت خسته نباشید می‌گیم. واقعا مرسی که اینقدر دلسوزانه پیگیر کارها هستی. دمت گرم که همیشه هوای بچه‌ها رو داری!
💚
✌️
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
