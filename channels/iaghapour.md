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
<img src="https://cdn4.telesco.pe/file/W-TJyFJTXie5Tcz0uOoMAw2_0cTPKMpDQ6mEMK5EnOpvwR_9jjzstwlffU2-Xuqr7fUceJyjDBKSaM_KP25P-JfE6b-jE-rR6JJnB9oLmaO7Vf7aKHYic9kqkDiUgTZ5at8wPKKZvvPzo70zyP_rTcL6RGAZUjRK-BE4tTPldBHh9BosZUMJ1oUYDxhb0uqC2z0nSazlRheyOkgR_uUceRq0AZJixxedFv-u-PVGj-QFud_cN6_2Iqkmu5g-GhxZc8TFtnZB49fl8B6P1oYuSeN2ayFwndwIs-Uw-aRxN5f31tsCMioXmyjXmDgLU_Nw_pH72GhhDwDA3gopappW3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
<hr>

<div class="tg-post" id="msg-3124">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from👇👇👇</strong></div>
<div class="tg-text">📱
تا داشتن
شماره مجازی تلگرام
کشور دلخواهت، کمتر از یک دقیقه فاصله داری!
⚡️
🌎
از هر کشوری، حتی
ایران
🇮🇷
💵
کمترین قیمت
💎
بالاترین کیفیت
✅
اکانت‌ها به‌صورت
آماده ساخته شده
هستن
❌
پس احتمال
دیلیت و فریز
تقریباً صفره!
🚀
سریع، مطمئن و باکیفیت
👆
برای سفارش وارد ربات بشید:
⏺
@yoozseenfabot</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/iaghapour/3124" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3123">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">📌
پیش از خرید از سرویس‌های تبلیغ‌شده، قوانین زیر را بخوانید
👇🏻</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/iaghapour/3123" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3122">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/iaghapour/3122" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3121">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/iaghapour/3121" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3116">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/iaghapour/3116" target="_blank">📅 16:32 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3115">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJZMoUPE9J_NhZaYZeNi0Gu2jL-GXVdhu7ciOeNk6V5nPrwSQKIsZ_UMhbb2p95HNg4O2Cn-d7rC4qx6rvN7j2-iA9nx4oWL6aYTzu-Q6Fh-PzBHZh-ifsaZ-kuMY4ODOoePI30eZCB6Q2a1eMPsmm0WOLWSjhAsqOWUUrK5gxm2YHw1DmxmxZkUvD1g3rWPjJK8wf0c_ax51zOSC_zWUDI23cTbL_etjPxWLFDJ1gXcJOs3fyEs4LJA2AMbKTEj2JI-SVfe2CWVgV2JEI1qeFu3GcUzffXbLESVDNvCDq8m6g7M5WI3d8yopYBjsu3tFh5NinKG8xU1cW0llEy-eA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3115" target="_blank">📅 14:10 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3113">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3113" target="_blank">📅 20:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCbKmWl0vNH1pw1Pqyg04GGIOcENjI9-o_y0z_I-zdRJcVyVUG6UYShLdkJ_qgM_PPRVamlE-tuERhxRsnED_sH5OYHub3susIaZKUcoCgYtTFkxY49K0YBtVpkEhDYFQ0qu6-ySsr32Q0Ix_u_lLXkbOT-GFLQATY9Cott5LHsIV0qBjjxo4QFVR_wvdwvLUTMWv8fhohtvt7g2n-us-939Ao8k6bSUNfPx5y2dJ2e-vWT0fQmAgm6Sabob53ZS_TqNLXp_FFv_H92TLTwWD7lv2EvcWK9Is6Dsvltge_CI4NHP1sOYSd4Okq5KlBddvg5vT34IG5QmZL83m-nyiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3112" target="_blank">📅 16:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3110">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3110" target="_blank">📅 20:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taWMRb-7gga2ViXf612UoPOI8hT6kNsOgJNs6hwujNidbHkkk127S7wQ3aZJAJtNinvYC0nAdz_iepTKf1thmZChbA_WZIIlTaBPlT5f6eP7Qac41wzBY01gmLPZdvd4fH5wa44bAQpyCyyUjGVkQifVMOlBOB-pCyshzPGmUFXgaoVqZFG3hzLl3EqXPUAPQ5PySsNeB7tXlw-WqEbfTpcrPKi4W2KmonnIpU1HXX3rc_u-M_92pgBK6B9ZiWYpwojAEozXgk53hCG0IH9KQZ0zrhfK0ZlQ5KeI_FPRUSiX10N_li9C8poYn479KlYlamESMHq2A3p5UDHOJ22ERA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3109" target="_blank">📅 14:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3107">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3107" target="_blank">📅 19:58 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3106">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB9qpAhvflxvN96jZMCbvMFmYI5Kdmzc2AVha9A0M5UtS-WDEBaR_G0kn8JBWE4N16c_51RWOOpwODM-I6uAa7yigdC4HC60Ywp3heM2qpesMYCPeUAeg5DoNP4jNLmTvkRKYK3qYVlFYSrUpjE6yk_ha2leXbXV3vnMAEogc3yVTjUQZ-KSI4fopS6vRM6gk_6K0GT-QIScIPkibGVYziWGUUrhknnU4plw02i7IvHBAlDLzL7JIliQYIpnQUN-j-6Bn684AY8m6lN4Cmu5VUlEPYvcqOQa2_1K_TLwJyyvKxtz-ttAWaL_4f205iAyv4wBisKzgWO1OUcNx42C5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3106" target="_blank">📅 16:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3104">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/3104" target="_blank">📅 20:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3103">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3103" target="_blank">📅 19:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3099">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3099" target="_blank">📅 20:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3098">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3098" target="_blank">📅 19:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3097">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3097" target="_blank">📅 14:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/iaghapour/3095" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnigqFuwXJ0xYOTXrWpPKkMCqMpzPHSzI0uuDW4ZmRIySUIZNToY_QoBzsmgSzDrexZoZlOZdXojiXawD03D_W5vfkQd74QTBrrn7iRAc8nTWFeX9Es7tbKK5zX2-7N_0TglTTTSOANVekPdvN5LQX7k7J4Zr2f5Fp47cJjfXy8jG6Uq3H7VWl1MF2SDMpIR_cTIFAgePTjY_F_PedNiJAg0zYdAUNI12kWUoaZ4skgJ_rVD5cQbZQWMY3oY0gyLFBFTMoxnMxG3hiokICGAsXtGIBItoVz87gJkUYWIlHAdxYCYLNaHqLR9GcA1N31OCRigRYCbT3jIo2fEFP1elg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/iaghapour/3094" target="_blank">📅 16:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/3092" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKPLYRfZ2Jo7vq648TGJVAYZtPsPzu9eHHJV4EM0UtoiFWI8blJAeF3OBrt-f_5jhr3f0dKLRb54DE6LiLg7OylKl-sAKJNKMXmT0nzASz82GrkQmSWAQzBcTM6ew6HwlmU8QcUK3oWdyg1jGBh561OTxOgMi0rzm9Plo72DAUOmItii0hNCN6Y_BzThNj6UDhyCqzpRcu6p6xQDu09GJCAwS6FmTj-SB5VMB8gHwOH8GpM_nnXrXPjBcPeJMd-Xufx2pusFKEaGgPbogs4pylsKPUYrI8a-hNy5mnojIlNTeX1hsXFM5Wnpy-2tXNq4q3vjr391DqAFxFWqbNRZxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/iaghapour/3091" target="_blank">📅 17:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myHmp2MpkFOval-NVdXuQv_9XpFy31nXOk1zaHqsuFkIc1yJuKkOg1I-Rwv2wegIxmY3XwAHSZAXcjFPFuL7vhPHgLjg4KommJwagUzkj4zA0QCioJYPcxk3ypl0eL4PnhbMj4eUiv_Q5COl7C79ihfd7fvIQE4GJTXhM6NpG1MbyC89oOxyasBDUvI9Uh1jZD8-E2KhxeFcOc4HhK-kFdNXe7i0-ffZ8FsNfBgUjY-84G7JxQhwf30ic-dxtoN98E3S9WsbGIybqwNGjD-M9KsvfDezAT_H1-hEYM-K6q-_lY3lRAuXbEGHYvs_uD7_CQ0s1UQJiRoSgPd9dX_HYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/3089" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سلام بچه‌ها، وقتتون بخیر.
به دلایلی حساب‌های توییتر (X)، اینستاگرام و چند تا از پلتفرم‌های دیگه‌مون رو خودم موقتاً غیرفعال کردم. از طرفی طی روزهای آینده رویکرد و مسیر کانال هم یه سری تغییرات داره و از مباحث فیلترشکن و... فاصله بیشتری میگیریم.
فعلاً نیازی به توضیح بیشتر نیست؛ سر وقتش کامل براتون توضیح میدم. ممنون از همراهی همیشگی‌تون.
💚</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/iaghapour/3082" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3081">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNGFRzRVodiCUD_1lEgCqkXu_xdiySmTuzHZAoU-O2tEFnjtFHhfFIAHNjM1xl0lX3NYjZahCMcefzrlibJDLy--I8TWUezG9K1qMRyfmeS_tSMq_5Uegd1o-pWSrb3FWBDLa5yfdI-YX33vw129wlvLeNUQjeOroMYMuZRgybLoR-ACUmla_H04YEETbRuXjlEYrWIiKC-G31CK7fGTuBkwwIbg8hb5qbfpsxnLvGmVkhG36C_1S2zJBoegcU9D8qbGziSujT8tNlIMrIGIOc3rdYlV1O5gnYdVM-8yAHEnYoH55PLvEbaXkl7rEHZ8-TcqVUOMPo0owZ2ps730Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/iaghapour/3081" target="_blank">📅 19:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPSB1zkS9reSp-TJn59Fg-4dVdaEnktsZkma4df4XPfbQqd4N56ybdjlBf6LS36AzVNYCvsEwWI-9F40OW31kV-gFrCaRiXi0-naRqIAhDsR-MJaeY5Ee1IJ7BMAOSCb_4Yn7A4CgeKdG-zVy6UZbC6AvLGmm5rMnyc7DO-ZaVVy-Kh2DBmtEdSQXpDuUjw2AYNOnNVFh4LiUYsHSNjat5nDP6tIoj8R5VFOfaoYfPLMF3xuhorgnekY4-ugTO3A8a_lhTlQRZZrcdqoEf7orz7NJ__vyLFv_svUWaUATDjKKAcplKQqDxjDnbEnenXUxHIzyrqFQOZgwQRplKBz2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCTaLXeEr6L0QmdV-emLTkgql-DsdUPViHJt0rs5L1E5q3LZ_CAwOu2DQ1hJgpFCxQIkF3VJUP8zjlQ_VDG4VumtUkm1gye-N2MUWXpyRG1Badx2omThbaZajlhrwabvXeEKEM1635ITSk7sUh5DK8BzKcRPzXFlPorfR3HJt1DTl5qkAPTifPLSXlYhBLHHDc98NZLJ1PPtdaLhcfDfKPhtLV0qN_oFVvMuR4htXwjj6pf0Xsc4g1Se8Ck16-0H0Y3Gf_9-h5DrvmS3CKEaAGAUBcWOvONmFvQBJ1-_o8Vlxj8AV7RgB2Pioux8ikGnw8yAC0CTjmmSp_2NEOK8ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0MUwd9xAWCnc7mi1iGfC6l0Vn_1y-BooJ9nb4UDyBxfDrTQaIn_9ndiVzo3kP7phFNeu_LGj2cPI_HLdxebb1_LXjh3ppxdN_nIqfCk9acc8COqZ1LpDqFZ8zEHWTT8Vh3RC85XOR_zrChgkLbBE2m1P3N0xkQUPwzRxpwg1NNo1ZemkCPAVQHOvR2fS7HFhPJIUY7n_eLgPBxNosteQvpFas8g4-JChVM3aHqoElmVA6FTqVw2no5MgZqo1iHcOsQBB9xZOvD4NjUN5idD-JkEE-8mdsv-U1qPp8Cqe6DCXqPgi6111r-9RdHzEEZqfNqKs2Wwlb7e5LF2wzHRfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABBXgMlWNuszMRtYN4KlA3VptAhmUridlMk7zoQkcZpK3ySvznLpxVi-NO5x5-tpdTIIT_werLOWlqfF9JCi4Wd_cMv6iawCZvVuPd59kkFQfyBpetHWVb1YN5C1IE0hJIuD6BdOam5ec8dY3Odc0-UavqWGjj65SRUfktDPrq4AEtBIthfXEI-hIR5-tPZ0giyY8Dz1LrEssFL9-3bsz0rCADTFONK6oQSXyf26XD1dyLXHOdAjyVzv2YpljxWYiaSQMIDF-Jjz6Z8KoekpWL-ajD3m_eEUENoRgx51BIEEiKVFn0pXUGTd6DvNFu3l0CzEfvbNVfpXIrl3aHKxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Znnv05WLPz5ngN2Tua-EdjoqGoKgooa2rnNANhUM7dg3HBieDC0z7UEKN2m5KAQv-UPVlLxG935S4z2v_6i6JS5lR910koras7971j5bR5xTJp9uVi1Kd0qK3_C3evzEVkqvpNfFGLRSXiljno3-xdQNAuL9hyCWutyouV-ZbTBiRjSYRkkOZy3xVIJuqVXpbcBZz5nkNRMF53c8AxnhbKGZFyNNU1voHXOluYrnCPq4IeBsCDNjTvx4hXH4jYXTH3iktBtuq2o-XSWZait5LeE5gIIabaYsDYBZl19My1RpzsLKAX07jhMtuaFTMtwSihJv_MW7-l7s-N5RujseSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=LjaSD3H8ZA12edPDkiCSTUeWmkE3dK-ymdTYmkgiyw8gQIWz5pOMjyQaIzAx66AxkXB73IpgCZVkIJiO-Q0snDTuFJRGS6gIIWvFnx8PtiYTGKN248B4SZHFV01y9HUMegvFGc-aiqjWlbHYeiO_Xe42WcOKlb-vlJesRxBV2IcsGMl4BrjxXU05I98eGrGCw82IFkWxBRX5KsZpRTcF089xdfeRWF4HC83N11bOOBFjWQG47OqLr5WHtHBwvrmm1qPPrbYvYH917GDXKfhibrv_VC2ykE2HSzrw-AjIfdTeF1D4c0tRpArcN5b1GIQkmBdzI9tfFJqmdqXNRCNvkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=LjaSD3H8ZA12edPDkiCSTUeWmkE3dK-ymdTYmkgiyw8gQIWz5pOMjyQaIzAx66AxkXB73IpgCZVkIJiO-Q0snDTuFJRGS6gIIWvFnx8PtiYTGKN248B4SZHFV01y9HUMegvFGc-aiqjWlbHYeiO_Xe42WcOKlb-vlJesRxBV2IcsGMl4BrjxXU05I98eGrGCw82IFkWxBRX5KsZpRTcF089xdfeRWF4HC83N11bOOBFjWQG47OqLr5WHtHBwvrmm1qPPrbYvYH917GDXKfhibrv_VC2ykE2HSzrw-AjIfdTeF1D4c0tRpArcN5b1GIQkmBdzI9tfFJqmdqXNRCNvkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHcL9jqx303puSx-MFCN7Dehu0Usz6letkwwcAi_RgzVbC4cvs2Os7mp-DmS6ZQrxyQK31gZRGTspmmGRV39-X8kw3Cgz9cL3_0n22U4YzuSh7AMpHz-1dMKtG-rzLUmgh5U_ucAlodOq8BEs1gA30K6D-DTneK3lDw9lC_YopdFpZLVx60vBPzn3gc3kB8-WbUv1haJ0CxwofhAp7QcXVzoDBzdHtmFibrSVrMbVPncJ6FOins_3fI5BXMS6lQ6GgGErBNbfSbUsDY__XKAYk_855pW2XEgB8u-Q4JQ9J863RiQO9okhoX8Q8GJYBfDqf0rbZtBmk4tSK4A2yVXKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYq2EiX4uLyLj_g_wTRZQey9euFnPXIYaTNhjU_6nD_CBPlPDZJJce-Oiq5-t6k_x0yCmpNTQDqcfdS0m7OWCfr8aTaPMKtNvYOp19zpzRJtIQlhKYKqIoB8-By284MI0EVxcTiItxTSuMI-ovjSvJYhz_pAFrGkcOUC-G3ndhPzJEcUVAX-y3BE0Z42dwqz6Z-X7OOddI4XengpbBuM6uuphKxppe7fJloCbH4eVnxTbWurjMatBa2fW8qA5RK7XZs1vOrn62HUOlKRAm0xdPezc0EP9kZjibBuQLJIqepl59GatMI7wcgDeVL8n8TK1pP_DC5s2RlQblU-1m8NJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beKbEZ-CZzMSuNtt6N7y8x1yC6H428y3ymR4zkYY7_8wIT-NoDlih9bjSIOX-YKjxIpN8pSI5P6C4ujHkoYQjnxZmCO72aU-tFKDdWYMA4D8-fvBxzKpGxWUVMyFODyEDVv_cobSkBzh0egScS92kN9sTaXzoQg5vbS57tCJ8MeOVHhka4hh_BhNh048GENxZR7tTQiDjA-wNg-hHfyPqWSv6vA700dvN6FYpn46T_a0fr6zsoWIJyi5Nk8KANkjaVSpKPJe2_LaczH-CuFY4t7f-bKLCridGeIfcx1ofe5zmjtgFD1GAhuxP8lyYxiDQnMAfdzkOznpX5V9n1HiSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETlOII0lS-s2dPJdTZ7XL5u3BWYH6CgtqLesuj6sgDJC52fz3RsZ0PUMOt_ZZM_4q3RBNQrgZlGPd-MX5cZAH5DqN48B0Q0BX2f_VOdkVBfE48XCbwp0GzAac1vq3hIKXDX77JaqRJ16t7bzh7CdhWQl2PAM3P_xSWTc2vN47hvrGzM086tIwD4hMzJZjLzjCO7FCme-QU5dgYXbbQr-948-JQ289qfm5j4-Ipi2ui239uzRwTqBxXrPNE521jzUPrthfGTZh8d8h79kOJwo4sHm1hAGL2PmLOdZEsgSpian9ge8cNIW_eyR9_nj0-wJfJnhDbGh3Gnt8kuo2AKodA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UryKxsy8a6DnMbhw3IvKVcyhSkyMSk-YGRkiQjHOZD94g59jcw_JqUVK49cCGQbTlV_p16js_OGzgZ6QHrzTHx0UoMQcO8t_AKzHE4oTuDoOTJQXpRHd9mrYfFhYBZNhxyoeDQLltV1PS_h7WkNZSuE-XApZwDRj537qJXXs4SFecXY1PsYNC3JoMaHrlIItfrFEKs_esyL_axSazpfEUpQfXnvozeoXiTZL2La61waSj75PcWqCksq25OXpQbDv4LjSBA7ltwvidKcW9MqLdNf_8F9tllgDkRQTommwbCKxyt5z978aipixSEB-4RmPjhOILmquvZVfgB4gmoJ1Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWykzSQzGPZgMbIdFxbK138oVV4qeSLTVk8JoOI7dhaoNYQ7b78YfPzLjwctbx0Mw0U1gF_Iq3saew7FNBK5PjiHGpvA2gHRo-817MSj71R1O7ftYYruyP6UGInk_ZDexTIBlwBCuUUj_B44Lo07PsrB-h9oZbnZ6juOqlDTC2WhfpRRZ_lHIjCH9gFbOeAyzGUPdOZ7ePOMaciR10l6IRx5_VYF1H8qre1szTOT7v3V3r8s4v4gtS4khJyclBkhvu5WMb0-K3s5OdG3u-ppS-FlBYEqeCBlpWyyenD2VnC3lMnd064U1VreLxtZ8TzO8HsWO_Rbr_zKCQKZ7F2k5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=D9YYwTKufxamAjt_IWmSln4itFP6TzzcA4CVFgxpdrgCKrLD0kPKjWFKzwr8rN3wGyVVL0sjtchOlfzkcdKjj_KE4CON26cWl-vb_7CNmerGL9Gh5xE3AAs9jL7q2qY222F87F8Sd8UBkr5-jiIwcNS28kgimafWIJbXnCBTer8Q-SBnB0JELiFZxdkrj4CBnuqGwQf2igL7Y5ONnXbLPXriQSlQ5Py5rVasBLhulCkgHUVz8CaerAEiwqFFxdnfh52wOjTg-6l_xHbCX_2xFpOLapvJIZ_6oyAvbyD5cHesZvVwlOFk7BeLbqTYaCT2iVs9dMWoVSrbjlsC-lAowg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=D9YYwTKufxamAjt_IWmSln4itFP6TzzcA4CVFgxpdrgCKrLD0kPKjWFKzwr8rN3wGyVVL0sjtchOlfzkcdKjj_KE4CON26cWl-vb_7CNmerGL9Gh5xE3AAs9jL7q2qY222F87F8Sd8UBkr5-jiIwcNS28kgimafWIJbXnCBTer8Q-SBnB0JELiFZxdkrj4CBnuqGwQf2igL7Y5ONnXbLPXriQSlQ5Py5rVasBLhulCkgHUVz8CaerAEiwqFFxdnfh52wOjTg-6l_xHbCX_2xFpOLapvJIZ_6oyAvbyD5cHesZvVwlOFk7BeLbqTYaCT2iVs9dMWoVSrbjlsC-lAowg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY17jXElyjdNgspCAVVYl853LBW3KHPGpeaooamFcYAhTWooGMyxB0HiUydHwpdhSO_N7q8yXsUxeAwQy1AnAfZhzqD9lvbK4iZvSJqKvJBeOUuEZ49DcfjScyjQr0E6oknqoBehon78ifctfIQv8Zxqa9Z1nUFz98GEkdBJ7vFY-zL-6WZ4x7CQx8N-tELtQ3PI4ZcmPKFm2rei9EidT8EeHGdYLAhPbCfgFVi1vQr21nSBanbSpNCJxt5dYO94q_h91lhjliOesBjTCFS2s73xfKRjEVaMIB_j4e5Y19Bxipgvf2wzoyor7i_P3_rOXmRtWMrK0sMFQ386X720KA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0zdPLKA9Whzlei48-s50py9rrHQ_OKS85C-uNf04jcqIVjO_HJaGNAeW_rv-IUhskHxYIAiKOfMVQE8ykliWjGMAa4rsOx2kRd_w6DXmx8eXpvY8zG52TZhrdCKOXQ3diVRQzycBQeKCe7ZHXyeW-Ym4puoYWLh5bzI5aEaB9n6qms3BwkSmfF2xj4i7cQON4XZBFbmaO0Z-8mY3Ukx13raCsx2PUhd29iQT2z50jQP3zxy0taiklqPuGPUAPRFXAfvVzfMDpY-6WtitiKSZngeHbTxhigT23oSxljbvmWZrUUcw-SJlo3vCwEX6HX90-Erm6co3qnzCgYnwKXo4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WX5YqGxgzp9XgfX0bFBDtOX9-foBZBUH7XC6o2pAzznJSLZ6Or6INZfF-5LgK__GgnpI_b_MibP2HkgMEWmHOJI0ckHk_VAETRYagwEsBEL64RlpyChOmdvw4MQlYdGbkKN2cxnK3oXANynYQ15AwiwiMuSli6GLFFKFNRDtbLN3LuUSWCQagti2OgnvN3UIqbOvIdwKuyJegww_IqlVbPndBlpmTiEgYVOflLyAV-O4_nZXXHncLRnRvwjFEBI9c0Zn-SoCBQQFGhn-rC2hw3j0fiKT-W6gLi9zAPyJkF1kgfAaiB-p6LXlxN3_27qsv86ijvZc6LkxAHcG-k-jxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFEPH6M4mcLVgAMY40ffR9RgzHmmBGqg1uOnkK7hxMsjirEjOnv3k1lKNxjEP3GKVrSCyR-eb1MRZm6iG53B36ZhEjt7k4wPrF40HyNW-od5IObhrQBmi-ShO79akvhEONOjJ8uXCDihzisqwXd8lOd2EQVCsSYMvY12uwsClJ7f6mEiJSg98IGohUQ-dfoWDz8GA71eOlmtjN5XIuwqneanh0vLAxvtkoOh_jGpQ61IPzkwGk8aP1Gfo6IH4nP_dDZmyq1nx5z9ugvwYIofblh8LO-K0yTwYnNhNKW00IKbXFThoFId8SjgFsgPpjMK_bYnIZN3Is1tnlS-CFOZsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwoLBoC7HjD4qCjibs97LkLycvcTnZT8YMc52XlMQ6XwEvJwpmeT-RiwkHUa9T9dt7mGPBVOEpX3beiZ_ca2g6PSBVQ92A4pO-b2Hd_G5yaNGc_YSz8PaI9_JwtrXQlZaD5h0DgYTcYMCO5bjZDHA2lyZ0crb1La1ldI4p6mnsRNx8t8JqGAA9VUCF_srCFOzJycTH0rj5cTmz5UtKPSJ8jEs_4G7wi7YQrOnEOUY5G2pFmqTIlH1hZW7nad2CfZONlO0-NgWNBrt49oOi4UNreeJLzjOZ9bRa-ZLRIU-vnOSk_lQu7s0Q-2vuIlLtxigU0hBvIPaHc4jACgRsUyzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRx92-BDWOJVIG94joGTuD0gldLGDkQES1yWWda9TXphdbEINYfmKurWzW_P8D19M0H7CbmVqFfvd1yI-gUaECD2OKFBa6eSE34TlWzXUJshQ3SCGjeoKpeGoOeYUlVC5DBOOYOwpbGZ-f7rzQC58E_DyNYQNzKwCaEFBye9Fu2OTEgDvU_AmlDjHQl1rTgvCRQmASM8ucEydmQWPMa6mUKA257sZffy_eiH_okr-BaYzQLqFYl0LP7sN7yqPto0ZDzFGXTgpWL8YErtcIfqtmuMJoZa1vg2G11rfkEvZvXvIB2O2uEr_hPctypqUp2kp_aAzE_81uV-3kSx9h4UvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbKb_OU9UApPx3jPgLaAcXy7D0B0N_YhFbXCrlQxoFy7Khjfb93FLmamNRDLXPM5Byu1Y-jJ8_WgyH6tThMHnwy8UbzP73ceZ_IJX79lhahE4oFtJDKLaQ7eW4abW2gLwbkYnTUTg2exvgxLitssvEFVtwb5oEfVYCPT-YEeKdUAOsLZ0e1A9KJcDiHxJRcgRD9-uES7mDvSY-JowmWGs47j3EYXJ-SBZKWNDHXJnscJqQTVe5RaLVWIsW4MobSVIyznJ4y_L-Ub7MzoMYiO5xGIqDfEFGuzrpAA_8FMoOWoyKgaNnC-i-owUyLzms-mMXRaBcnzXQ3B3WA_kTtwKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQG-cMB2WSPc6evsSfdM-WVZpXU-sDRntEQvUUEUHVCLaBEy9HEM83s6ZOh3AdtufgAfP2QWhOAPiTNLdQ00_pYBt6iDm3sAGjta11RAfssq_b6FxynP0MT7Av4vykCUY39op5tSzMffNczEgd-snrt0ha4YcuCzszel8OaGFaJ5tjfLLgLd0N0qTgE-zzIHgr00Q3928J2spZPInUlqBmqEOHAT-FcLbchYS7PmB19ifbXcZxQPwMvBAyJDPdlLGk-LTc9zLmpxND5c-BIplxYfnYcFb8EIgo-pKJ4YT8mJd5x60OdbbOErcs_S9D7Jg7_EGnZ_UYD34RLrvpxeAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvNv4uGcUjA97eVIYoz632flxcn-KmeLu7ljWuOj0YOIA9eI8gOQBy3NpqJke11-XiUn490U3FCa1f4P-RQL42_RG44_mxRlA0HaMUz0NQrR7tjdIdW-ibE_TGMM09rI9S9_Fonnh_Sz1Gjbr1-Ovdjz33Es3oKHomA0iM40FWcIEizxBEMnb3VkaUEeByC2H4MY8OPPhUrWC_rGDfsS5vlwMlYST29pcVKWjs4RjCh7xitPeZGyy4b5sv7_gzq-kPgIh_sncjvJ0Ts7Vjh8SD17H8vAwUoQTnui0e-AfogH37rVl4UTp7KDwvNRnPOw0-1FeumUTLGnyw2Wqip55w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzAJ1R-npqaxHARj53z_bQW3bCtqzXtf2i_KmQiUgGvdsRXkvGVIGL5EsZffsIb_epPsCd0v3y0nReKMnzIrfyu77M8u2eDh_J-941PQ02iVOJoSCjSsZ2a2Dy2iL49usfJ_oPvDdRElG3CCUGwiI8upcle0OR2xrBXOGYF1PCj-O0YJEVGIkjo3sJrfKl-By5Ezz_gY7tYoabNcctmPxsLTB88-JqgeYpbvaOv8S2zJWXZJAgYo8Pj-Yl9kOayTLFY-TXtlW3wIkE-dkZgBg0CPT9krO4oboTi2areuaolVpKB8_XANL-9FBA-0c3KnbYoJ5AJsq_8NvYAV8X5_hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=v57h7CN_zlEkAqhBH_dPOG435AnxTCv_Co5hTwa81CvC0Xwd7YpctjNnqEpqIAJs16wQugKZBRDj8pj75_tNKbrZAKgabP3rI3Eib7H9k-DdkdBmBQqSYkdPMSI648mv8y9gqmfety70LYG7dIHEfIlZHnbxFMJO1C166t4NokS_9c9ZJVPP7U1E_EjX575jETB2eYH86zUDIQXLiYL3AA3IHQ1wruRziNwORflO6hbTg2n5GubMf0zHXRGgpNpeSTP71F8yU1IfJTUXvqG2GFWVDDRbDn8Iu5T_fdoPWBbYIQhNy5cfvYOjl10UVAEzF5citQBBQKK8mWZIi9TH2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=v57h7CN_zlEkAqhBH_dPOG435AnxTCv_Co5hTwa81CvC0Xwd7YpctjNnqEpqIAJs16wQugKZBRDj8pj75_tNKbrZAKgabP3rI3Eib7H9k-DdkdBmBQqSYkdPMSI648mv8y9gqmfety70LYG7dIHEfIlZHnbxFMJO1C166t4NokS_9c9ZJVPP7U1E_EjX575jETB2eYH86zUDIQXLiYL3AA3IHQ1wruRziNwORflO6hbTg2n5GubMf0zHXRGgpNpeSTP71F8yU1IfJTUXvqG2GFWVDDRbDn8Iu5T_fdoPWBbYIQhNy5cfvYOjl10UVAEzF5citQBBQKK8mWZIi9TH2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY06QaulYiVYr6uH0HEZsI91kSLQGSXyKbNfOh9-_adUPSu3jWdVQNZv5atBrjO2JlESKIo0Mla9fMaRg_sEJohSWDk19aFn3WK9K0e5iKJCCgWrlvL3E-ImQJ6SlxKvfBFSJDY7c-4czX5i0Knu5HKMrI2vv_VVWlleNSjiqenVWt-k2gWHTM7zPd4miz7krW4qxXdl9wVQf-hjnYziqad1bwIpwhUH434E2y0qCoXJL9RdZ-q7UD9s2fMWiWGRnZ4y_u4DnJsHXY1fCSMT3l9pQaGOQIucICAKy3RfP7MuG3XJrft9xg4Hn_gxRGPYpYXM88_2M9mkE22uJbW7Zg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxbOCFXaD8meGQi5Q2v81Z2P9fbHya4u-GBOdyaI68N1PULi3KkzImlkaPcYDY6FZczt8hpDM2GWlezOzZuJbbD24BCEG6QoE7G61iv_78Qu36GnFqXFo5-8nOT7PmxWn96gpF2873U5dlI0AXzDzfACevNQshXeidIxM2EwwKTKGmOSJvRoOZ7_7M94kWDpSBVrEkFsyXT2YE8n3CbU4A44kDsS7mYHvZmT4aUU2yd5DBUbjy1M-Ur8aAo2CefswTWUBDShsGW4Ohlok_PSMZ3cCyDB-nqeCNsy6BI8Q7YxFmTTTkNMqJyycCLm_PZRykWbnQdz7-Q8zvXmc-jtmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpIWSxdkMM7t7O2CuiONpSe_kc09R3X6gLXPPCvYoSu7sBHB0xVghjH9SRplXT_MomEdHHp7QjGwXdFVzu3Y_28u_UMuwZb7bMpq4UabspZp2dyauWjfjK5b2ukrxSSrXDkCqmpR08ni1Qa9PR_GqRquBrBMFAV235erPJWj0tPS-mDDz9azzv1dC6jXnK-ZO5P18sQpdh2LaWfmYl4zpOhqzDF47MGATaoczjFDm8oTs722DZfBu2gAssRBDYbguKqtILQzlgJr1SacjBQyPohoq2Sl1nMFUfHAaCx2CmqdgF0atMaQTFc_FcW2aDihb0_3jofSn1_DKVYc1fZu9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0Y6bvlXr9iYB2yCJC7OUyKmosng9nBEdbrvyprXc3F6gSbdjJ1-_ubuiomV6X4UPPgajVw6aUQblVhOoLj-Od2Umu0jpa8SPl08p--7teyLOjOjEItDA6sK0saaQm2wFOP9TMFsrdjiX5QAYvgerTfv4n3DsYqXeXkL6KNki4-W4j-DjDGxyLlvnfqpFnL9CaODPV8_f4-g114HXvLP4PFQFNVI5qxulIPUQ3A2qjAPd-79AfH9R7MlnwMeMViXXoFa6IVTWoY8G8dfLeb5MxtqM_vRuwxyFhha5B7rzQWkTcSvu1sePQ36l43QbR3skpcNULyzwMYPhztJHqDAJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N69aUPTEBRmrHOXTk68CKbVd9yDzGjVR3tefOLQH8pwQpSl8GPk1MFLlV405P6NEGRO25j6q_53xYFT8emYHjMMRolmPgZaxMXHUGunSuCwoY2adK8oKHWHxtQ--jECiMWIFFYXKp6kt4G3sdybrrxQoX95SC9PZFG65MqvFeM4wTKKIHG4_n7Rn4SZIBTq2yTQk5A6f-qYFSagK2qPQnu4PC4ClQ7kbRv1LZ43XODhGuV4JFaYdXNplh0iLimzty7Amf0TeUZ79Ul2zifyEdOAiko7uly0iFvdBxnUtTd35yB8JDZkhRvVzW3X7maM5g416WQmb8LxcQe0Ip9A05Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD5DnT6jakSkieIca_5aYgcfDcvXOLAD4w6ck3wNCtoyH5K4nA6tPzWoEmrQ5BylR9qDNgVhZWt8jYgZ5xMznlr-uptnPXFUxZPvZAwLaLgAlLGpVwXe0oqDrk_XztLfH6dT_H3W3C-PWIv_-wlvbvpStBrR00fqrjcGe9H3i4Oxyw2J_E2iV9Fr99yK2QC3hmQCuUXiH8ySqSuV4VTT1cGcLsXBeRCbDQch07LpL8HRzo-QEFjS5_83zyvWeuOg_J5-yvj4Jds7yLYQV-pclgdpxHngYKDLLVm5Ory4ax_bL5IBsILRgQkvbxUUqHH6EzDvZl_VJCGrTbMrI2P-5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=TmoMcAzKOKW9tZISn8g5iMnzgVEBy6m-vcPKL5PxGA03HeWGOWLuFWCZnmPozwfnlGrZmNsvkj1R3WoL1WuhRzWK59DQOBJcBfS1LEceKFZ2yX4Z2IiNkOk2G18fBF0BgA52Qhxmmv47iUOWopYm9NbCkeFLhIYPBaS53zL0znmL88c3Lfno9G4k-ieYiJgMNRNExMscWgraFuEdd9LTXyH8jRLyc6AoW5PV2tZWWWmUDj554fOJt5Y4KAPV9tmnjKWD-h8d-8yG1BLmpKNPQTL8B1pU-5kNkqL28iq5x0ktGNyZbkIpSbQhFIiRiBErMpQeDCDJ7xfIwuK_xnhUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=TmoMcAzKOKW9tZISn8g5iMnzgVEBy6m-vcPKL5PxGA03HeWGOWLuFWCZnmPozwfnlGrZmNsvkj1R3WoL1WuhRzWK59DQOBJcBfS1LEceKFZ2yX4Z2IiNkOk2G18fBF0BgA52Qhxmmv47iUOWopYm9NbCkeFLhIYPBaS53zL0znmL88c3Lfno9G4k-ieYiJgMNRNExMscWgraFuEdd9LTXyH8jRLyc6AoW5PV2tZWWWmUDj554fOJt5Y4KAPV9tmnjKWD-h8d-8yG1BLmpKNPQTL8B1pU-5kNkqL28iq5x0ktGNyZbkIpSbQhFIiRiBErMpQeDCDJ7xfIwuK_xnhUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrvbwAYuIwxaTj6VDWp4iKsP07jol8_KTLbhUqjZgH8D_ojxZl1zzw7nKcD8WA6oFWt4ayPRfBbBUdtIH5Wsa1DzKOTNW4IEVlSqaVqRN8T4dlczpztJJz5gwtlSQaTZlmqX2Mf4bLpwSv-jLbl6-h9I1rDcRAddN2_9wf_KqPXEkbhfOoWpclIXGpAvnGTK7YYiwmzallltHWBsEVUS5CL18URjfVz80XEFiBJUSBOGotE0EoRloHgUpfGbzVAirieP7vRgq6OpPFCLcoxLlIGR3uYUZqrynbIN7W1zWlBKNEXNiBv1CvbTwh8SbGmW5-pCC17wyrXLQhU-UQttwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq28l4hKmrduvd2OnYOYqxv205nwnFOnHmosFsiUOySHVesHMGZLcMJNHpOuC3QqjcTgTnzsd_eAQr1mpa25nVVPAr8fKkhe6Vj0s25UIyvev_704t7yC1bAFn8YYLPHMSfGFY7lMNyF-a1M36KREXG5Q-gdtGSiiOwCXfQJDV_tqwmvxwoiLut8Mr5OI3f6kgX1ow0XvmoN9wIJ2xYL5TY23_BCrChor3e5jWJPzF85SGMcQDQAZGkgjqaEeKnHbjQPWXr33rE-BmbjMkuxUejwMbj2QIzqWD7xb1B5BQ86zhYNNqoT7YNpHf0NKpL8K1YK8rhtcp1L2qbnQrZ0Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlOaPnreKtSfPQv2jK4RELryRAIWJDKFIWMboVKXYfeKXpORA2jXn1VXV-ZHQ_RNa151ZdMYEEeaE3-tXyxUInQNiY5JQi3Ma49kPB6fCWRI85y8xWKhTfq93Tr-SR0fDhj22J0e2B8OucsgM6f3mtFVL2LKPwK2sy-cKpQ1e7r8L-lepS9YqOTBinsOfjEF7DJLsFCzzQvdkqgqKwMSLw-g2Z2E3-JGd2yA0FHF12hxhenn9cB5j-wAvx3Ocpn-peY7062Yb7qF82n_5BUuJ9H8x3XyVww64MynHkDCFNXimt5Bv3sQEvvyxRYYo08WbYFp-5o-LzfOoa9DQftqeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ33ucunR5rcdmbx5iSN6UcZczlXbQxEmdxbKFkABfOWi9zbZQVctUSsKi23C_RLHkJ06CkB-DMyq8qhdJP9L-uh7DoBzLgTehQ0VENXwxIvXQf0isJyhGLczo7nklcC7nBDsyEG_7ltCkx7X6UOk2-hisCqELFrPRCDM1U2s5qXgvSDNchNvVGtiIXjNx1I9nT2PPXTWvhQz7ym7Ni91U1yf5oQobIQfhLijzXiZtq9_QL_qcnqj7RtLoxncSfJw8cE8_-aP0H1PU0mhYfDN7LQWW9hTYNEzDHDGAXb1O1XW3DpLioAAl2EUfDO2ClRWVfW30mepf04uPvRNJAf7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyAtIcKF2VtPpxXeoZuL8vrUSveeWgwI8qrqS_vFiFsNt-EeNbFpfNVrbDkjViUAdk6_HclmG2MoONFTkiNOkPiJ4ABSSAHqH2go7y0mLeGGNfgjyY48_ILqqK5XozsBPzcPh6XM92fqCNeitHi7lCkawUScGkMiEPJP_gklgxJs_UWx2FqeIgfZ5zL6Qpp2XXLX99tckTViXLao9TlSPXgt4G1atrRWXgYjWCxRSrusmUV6-YdU01nHkr0Hro2VtieQQ7mwxANIdKABTu6xbiR7UTK4pJkjEW3JC7KXI1U_uW818xbr9tEboKGPoID_pWamxxiec0csvLfENbnzRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgGqXS8NRGRy4tf__4Nt40mhhAz1v4LbvIAF8Cn60I9mkHoof8AuLAE2SVQw5weqMegxwrP68gBtrzRlr9pzBiodLKtnZuiL0G4YTef507MHckf_ntlhuGCg6sWvI74166vGJIznzmH_46sQL69OW3FwrF3FfVStQGv8Yt-dtoZY6yuOpTif-NKw8Z788jtsq0oVnMvLBv1IivxST2wEtdjUwDnzYTa_9rGUN33Yo1Sb1HnXMdwFUV-ffoTiLT4LVevxGLRe2PCV-mfWAYH7PFWu5jHLQAiTTAaD-O4txn3kQ8VLtYAml8apmwrOmCOu27xrTexP5p096Mjc1x8ZTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCNT3-qIP5zaiIIG43OPDwv0mRBVXV59zf6HrqK1KLB4EPopaERsjfwbYbrgiu0AOL8wvTvl-EJsdVSVUYPeW_v781ZjxA3uxS3_icaGIqgfe7lYpxl1jDqRpkOCKFWbHLAcbRvREuYtgDpBqPRev6s6YFoipF-perWvjIa7rfne5-BbSK97tHEGBqjKDgLZgCrwspe-acRPNuWDoD5NCiTnBsQrALcyXjENmYbtCZ_m2DvG0CjxvL2eO6hSG1E1b-rIsiMj1bPHpCI7mufmdUwc8UazFA4Oa0NPxgyGWQgBBvOl0kUCC5cD-FdE1vGtZ5X9_CWsINDVsWKMt6MW5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=O6xORxMBSykCuzZerwgBzYez7kyHkhsdZB4-nI0RNAtEHLBH_E2B5QJLS33cXTzRc1DDBjvjwYqcLZkiPF2rQEQ5HczE1IyKiKlQjLUBIBNCpZcZ1IETlOUUgfrkiCiK8EZANOdUFL4UFXCXJRxoT_i608-zDpihxxV2ICH3-38e1HP0DPisztAYSazFDx-Vc2WJGN9QhnlGX4IOxlpakJ_bCwd9GefaIG86gbxFYAvm-EgwCa2Qwfzj9O63gSjMheqkKhjFggZYoXU1O2XWmb7vdyHtU5n_s7JVgsLiN48PPnIPTy6Rp4pM0rOriHbTQLnbcAvivxLOVVKVqwvpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=O6xORxMBSykCuzZerwgBzYez7kyHkhsdZB4-nI0RNAtEHLBH_E2B5QJLS33cXTzRc1DDBjvjwYqcLZkiPF2rQEQ5HczE1IyKiKlQjLUBIBNCpZcZ1IETlOUUgfrkiCiK8EZANOdUFL4UFXCXJRxoT_i608-zDpihxxV2ICH3-38e1HP0DPisztAYSazFDx-Vc2WJGN9QhnlGX4IOxlpakJ_bCwd9GefaIG86gbxFYAvm-EgwCa2Qwfzj9O63gSjMheqkKhjFggZYoXU1O2XWmb7vdyHtU5n_s7JVgsLiN48PPnIPTy6Rp4pM0rOriHbTQLnbcAvivxLOVVKVqwvpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXW36SbbIV3R6daEVfSiHxyekOWCKp02W_3lfIfPKfE1FqI-dpBQwAIsRpvu_SpRaPE0q59ERqfiYA8hMA3U93FlBVv6T2fH9pwOAhee1vWG8tpJrUjdwQEV6tccxwiINNBs4L8Y_RlrcEDIrMGFPMBjHJXqNRScwCzpXVV5I0rh5DyIWB7AxEMpLl9UtWqI79Df9N6c564nCyJGRnaFUr9R7XG6CpbGK8ItG56brG1VXDM2WLK1xLtAHEPFNDhVpZLixwFW3fR6nRwiduTELci4kn30fHw-pp_PGDsJE0PCTIYXbJOrpnCnidSy9wwzfWj8xdfLxl5hNW7iRuUMdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=K0-IJxdizUfl7vyxJVkK83FoNRzUN3Sqb-WeYkxd1jOiNHOmOBJk79Ug0UMc2tn0-5dwBqMKm2FPXU4ViyEHlmMk6trrkq6cF70daXd8ByLn-VDOLsk8dztWhV6JmbL_N9nvrk6V8ocdePrmFoLaJIQoYlF7rgrTTEnZQ52P_PwFJf9K_jU1C2wIxWVcVM_sJbxkZ1-S0kF6w0x-Kf1HROiRjZT7cliztK6xyPxTvZt1FX9zEi1woNvSMyWzYwtaM328DnWdgCokuGV5p1HOEVxNRjiQu4uih1Og0gdID-pY_78noGQJkTU6TZnhi5ggn95xHInFIDlu1VYTOrMb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=K0-IJxdizUfl7vyxJVkK83FoNRzUN3Sqb-WeYkxd1jOiNHOmOBJk79Ug0UMc2tn0-5dwBqMKm2FPXU4ViyEHlmMk6trrkq6cF70daXd8ByLn-VDOLsk8dztWhV6JmbL_N9nvrk6V8ocdePrmFoLaJIQoYlF7rgrTTEnZQ52P_PwFJf9K_jU1C2wIxWVcVM_sJbxkZ1-S0kF6w0x-Kf1HROiRjZT7cliztK6xyPxTvZt1FX9zEi1woNvSMyWzYwtaM328DnWdgCokuGV5p1HOEVxNRjiQu4uih1Og0gdID-pY_78noGQJkTU6TZnhi5ggn95xHInFIDlu1VYTOrMb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9CvwZSXtsm4LYRO-XuEJNz_Hkl8N3vNW3WBAY8COccV6Oh6U3Wy0rSn78CgrKuJSAFR-Z5Ko-v9aEgzjdUzw12u38O-qvRM8KaVbL2Lr7Yi06hOFlXC9V-QPGYSGxofnfk1tU0vjGSM__5T_eBJRwhbmR3T8TPQ9IwYVaWDmqFtPhGtCzC9s3pUsnWxrREaioJBTGG7e19ibfDXJ12j0G4W731J3eePi9Il8CJkrFIM-magw1otrAfJcPKa0SxOCMzHPBi-T85J7WL8VQ0SIRiVZjks9PSsuCIvMMnfHGHcsraOw16O8sDNcCtGLIw6f17SIE14mC79pesBvfeIAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evOhc0EJ2EUUMJ1JNw041ErqVu44mlZH6kO_hln2Yh2JR-z8VuRByLEbY-Ez7UzoAFi7qA0KdhBUz8jVrWeZvquN23f9QezqWQ7PYLJ65Sgjg9W1HR_he_p9iPjDUwilTnmhsnwIuVFKOxomeDc-78oOcKxkxJlFL8ieazJnvAYlel8Dgaz2XiVjXaPFVNjnEqwc7W9WqcPbm1xuh8AGLSyTf0ELfGJJ_SlRRb6AzzIqATVC2ktTfk4swI8g2beeRPNCuJKBsmyiIThbVyle0qgn1xm-w2Lwmo32h23ENUyjc-CgtR5MGAnosJDWqqrO6xY6MYepj_i63asNXDhYGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWhdD8EcI_eA02r6dlMJHOoUBl6mObnL5D4IBCO270lJ7xVG_1lbtHFRAXUuQbhript7dbcQvcetFhcmN2BJjFdscl72wLMxJwXE0PsVaQQznUS9ejSOweKhXC8CYvfn-u3YztszsND64qf4oLmjWw7gha1mN4tA44k3UeNwI3vhYkEl81_tEaYiJMTL3zggdX7E1-LLvRpDZFHR9b3szYL_lwflj82hr6XRct_It0W2lkOO_oQNFhczqO5xsj4-U39LUe0MT80lRAoiuXw9ITb2yKFwpq9-l8NEEZBh367ee3jttty7bw4ILOvMO2uJFIIetkaK_X9cJu8vGLNsJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA1MDoOB--J-1sHYtWsyLG_qmvAZA0Z-MNqLdls8wsVTzfX-1CKbAKFEwuZfRXblm13_fSV4GMHu3vtovjOf6TleY3_i_wIHsJuVuVyhTZa7NBPxOYpEKe4OjBYmRXnfKrA3_NKGcwR3T1BlVGB1wVZfr5ShGCsPrDUGpohfc04bN_F2CtACQf5L0J4t0jlNjOb1k-TuE4mV6Y-wDf5CuFyykelQAR1dI_TES8nChRqTjL0y9cThh6z6fje-tZWX4xyBiGJPppg0kU3o9r1fZELVb_N_RQzKLo13wAl8YTfo-7_A1baPbjJlbvip2emWw6Sq5q2zSxvZmzJ_JeUVeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKGdnsDi0aqaR0OaNnoKRw04cmfvkPTQ1J_OlSzmUF5dtvY1noUWzfVt38HChkooF0o7LZSfp5H-0tGdrP3Zir2IDs_XDx0nPZjOrJh3voiVEZtscFFvQ6XoLulU5p_32xehvvUys_W9sZs1J0tFsYoKX2wb6VapnFtERM3kSuTr1nTRj5sG9L8EmI0DTmXJIF9q73F29OV_J8pJw_rpMc6NaH1nLpolFqsxioPfCEebTib38cZkIUyMfW7rGXpw7J-F1Ji0HIcwsmDtTAjOS0fUziTfikVJHB1jxY-6_e-gbENqsHhIyNPpytxepqa91QsR5KVz_KX0C26GQttV4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE6xRC3RIpPhs1egDaiPYvwino9JDYvpblt_SqN8D7J2SKdlYypIhLyGclTr-ssimvCK4XNJNVdbQ7XvMddmy_w9PofNQ6DwQrfV7OC_0p6_brveTAPrPKpmIXeKFSTl2FYKeEusFJj009WDGyUe3baLdBLnv5Ez89JLgq9umt11vitUvtc-Pn-yvRLAh6wtd4nOws9-jNt2C4fgSIuzyaqs-gCgr-e29ngtoa1W_ohGxm06gl4XlI6X4UcZtyd-ShOKFB9XA5kyJOcWSjXsbcRjKYhvUn7tsIwUu3uHzS1U8O0YdW8ECfOuEhtBXtuL1V_QYNePso-awfOuDrBH7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVkS3P7A7bGQPMORVNWBs-wlEfj7YcNn8yysqe0rH3Fkp9-t7OgPcNossAlHd2FnLLE3UXeRbse0MCrk6So82efRrmQ6iHCzXjKM3QAEdzKDMq41m1pxkcS1AP2JYDJTam1e9aucJPfW3_UDAqx66SSCzDu9-v4oH3V5KsxUpTjr4eIIsiD0xSvoLOrSPxKGSa2ge4sYOyHZZamTUc1D40xg55A9YInqbi5pWUVXcEO0Dt2rvtznEANleU7sMdFD820qH9TYQT73Hr51KK57PqIXd5D-wdJnyaBnkIN6ATsvRZWVfYL2OKrW61GcNCp1TAe24oBQZGHv8hm7NkXYlw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKVYgtabE0V4MZnPDU-sAr_J1eNi37YK9wA5pd_s6836s9QzJCWrQgCYKUAMU802E19fNN54lNRmJqhU14NYAl81aqk5j8Px9M2WxMLToD0dA6Y-hRxaIDGd8OaJBhvcb1u7QDv0Xv1fA_ikPTwdZd92XS1vuEF79q4Z5QT5Kq68bSAUbxEKAzLyWfdL3WlkDDjsqZaAFDW7sdTxqVTbvpF1ZR35HERJJJLKGVETNQCRfgb4P1fZU4UXrsAEo5TyBbrIBbEbMkauOA7lQ5fKMAfEXf6KYYUEv7tK0RnWNYTPv34FJqI56a-eb2It1fRakGfed_Fjw5HhC8y4E0CzCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=BwgxZsBquLNTduhoBKPzA7c-v5SFRHxssh_6j8EPCvXHsPtr_0IjJsmup1GIqPLJ4gX8Z9sIfoN-yZpcdfEDWvn8F9eqRF_a6D1UTUwxMAZlhvhnQYbrVBhFv3XROtcof9L80Rf6u_Z63FactkiqSUwdrStnF5D2cZ7eXZv4OA_gtr3DH5BgsqAn2b2FHIM_UlMgmG0lhzcoiBrrmGl_nHwRkpn19_XZS0pws2OtPUI4fh7Pwvr1dPakNIUrzuoTpvE5agB6oP5SS9UKvNbLg_d0H2kM9lsfQneWM4-syvRDCMT-p6Ze3M9UQ2CPnaUVESqNDaA76I-UHWQbMu4vpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=BwgxZsBquLNTduhoBKPzA7c-v5SFRHxssh_6j8EPCvXHsPtr_0IjJsmup1GIqPLJ4gX8Z9sIfoN-yZpcdfEDWvn8F9eqRF_a6D1UTUwxMAZlhvhnQYbrVBhFv3XROtcof9L80Rf6u_Z63FactkiqSUwdrStnF5D2cZ7eXZv4OA_gtr3DH5BgsqAn2b2FHIM_UlMgmG0lhzcoiBrrmGl_nHwRkpn19_XZS0pws2OtPUI4fh7Pwvr1dPakNIUrzuoTpvE5agB6oP5SS9UKvNbLg_d0H2kM9lsfQneWM4-syvRDCMT-p6Ze3M9UQ2CPnaUVESqNDaA76I-UHWQbMu4vpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkEnCf5DnrK-XmDNkJV0A1WPEp-fTfYThAOtdc1xROYSaxbqUF6RRc2TzMy3-dVHBAvax9en0LUigpBXvw0XFNwWey-f46e2LD2Tnkyvjn6-IwL0z3CFtmp32rmy_8c5eRbsrRVz9bxUFvENB4Mwja14Xy8eUzYBfWxMLs0pc04ovFY1USysM40-FgyqwgvMrQ7wfDs1yKI0tgWpKcSAfughJL-o-egh9FnPoAk9cq_vpo4GHBGQpt_MZ0oZ6oMV3Cs20R31Jn4LYFSIr2MJzF2D2TKCmPA1eZ2Kn0ecFixCOEdAMTu1_YcG4DUvHwwtfcHp3xi183oCf_g12cwtvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnS-BhqS4yL58HWt4JtCj86rt1sxf4SDlG8I8kQkARoQtHmG5btzkbKpZDkh7t88iXnGKVP_A3bEH1UT20BeOGcPH1dq6sC4UYq8iFfq--UHFS422Z8npBj8OoVVGD9x65Mgf_abCvfo2RNLm-MjWfkHUP2zNGOvgtAYzSw1Wte4KL5Swl68dkzy_MLza0tbMOcWb6Jlx9TW6hhek0Hs5-_e4YcGjwg43-FYkn538QH7W0oXkoZi_XF-Dd5EZfLV_mBdPvvUAJNku-NStc_Mm0B_0nGfbeaKjyWQT1lcoY6pQvbSHIBifQRr-M1NAllv2cnPPK3wFvvmD-o7yZECiw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj-0_0V7qYTfxUZXgYxkKTjst8GGWzZM9DKCgjRB5HBDih8dznwWNTGl9R2VKFF9NhhvibFkYsKkq_QyRvHgcgAfOZNqIQyFlpsJVmvSFNtbtc3MEGySMWyEntWC1IvLlwyFwX7Hp5-jUTWqp9UE9WnDnqn7E_W_a2YoaVuLi0DMdZWnlAJEf4bqy8ooCOdlTxM975l3lLFl29p6DVYA06POC744JDFN9NVL6WTJimEupoh40CsaSeF3JxM4KfYjKSlRHvF0DTtIrKM5yTtcDza2ZVHZXFMR3k8h4NL_Y9mHa5UwW-A6N-ZuIJShu29feOSr6edEcRnULeB0tcYYzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHO2l4zyvtU_jM0_CgvJsTADxD4pKqjTpd9aRPKMTjW-69sGxbCWcnXu8Zu8gYK4Fb9Nb6pYahtL0SAL9EGmZ0u9EgcpvC1MngMww_P4dX-3bztG5TBTZs8sywIeY7mgVLOQZA5OOOwZ3uR1OmRghtfn8y4EvbnI6Yat1-bEELEIUa2gZ6-7qnCNq9qqtbh8204Be1bvlEYQPGYphLGNUWYVDMQE4CJWjNb7FI3iC3qzairplGdGNNFNfJoXrHgOUaK1KhpNCOTO6n1WNIFYkctyc5h_ZXInzQsongglnHOlNZddiYpJ604ar4kLJx5Ohi05-bjw8X5q1ht021-uWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=v4kHp43gODRVE6H807iJkdbebE-fPThGKU6QAblwQ-23fmxHtFhz3k9EEMvl0wcQdcCaXsU1Sz9W0PW2wFzDG0b50m13gsmAq2YptJJ-fmLyyBPh4f5R-JQqONfjenD8OBHnMvXq7_rjrJmkGgC0t9edDu6G1fHtfwwRj31pUcG-c4oJObPb6tncqbBkK6SFlkXskNaXYVQIRT7iBMJDvTORVABZE09BU5Fe4OAqnjNubriX62QTmFxdWhvA80cxtlCrUiSXHNWzmRYNQu5c27DGN_YdGPrBxhf33ZsD-Egrq0prAQbrgWnUt5vRXt1UsnJ_RDKI1Jj0uQYewndaWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=v4kHp43gODRVE6H807iJkdbebE-fPThGKU6QAblwQ-23fmxHtFhz3k9EEMvl0wcQdcCaXsU1Sz9W0PW2wFzDG0b50m13gsmAq2YptJJ-fmLyyBPh4f5R-JQqONfjenD8OBHnMvXq7_rjrJmkGgC0t9edDu6G1fHtfwwRj31pUcG-c4oJObPb6tncqbBkK6SFlkXskNaXYVQIRT7iBMJDvTORVABZE09BU5Fe4OAqnjNubriX62QTmFxdWhvA80cxtlCrUiSXHNWzmRYNQu5c27DGN_YdGPrBxhf33ZsD-Egrq0prAQbrgWnUt5vRXt1UsnJ_RDKI1Jj0uQYewndaWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ko76f5eSPRnMOoWMbdrDcKrEBsW3TZvf-QfxZIVfkR0_vuXhjbPlViZHR5Y_49GiQi3kE9Tgz4uN5XDgz6rsCFariFY_Sxz2tmbFo28sGNuhGhD0rBx3Q9e-f8OPaX62H2N7uRs0W3IOrAiyhNNC8ya_VwDlz-ii7EVBGYe1yMfZNWMPQsGqmZ7nTv6dQ28Dfyn75CMwhjv9mAHuNFtLXZ3WD451Ca1PcU0Ja5o8KTgVHTqdWhEEw8OMSt8ifDBsxzUVkxTi3ptV5GqKIu5N0LBABj-r-RoPg_7X4rlYHuJxqIIf0k0ZZUjtsSiFxbdbbcNq9rqHLQUbk8O5dcf9nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQkbL3aiWVRaQKYFcCFlbsNRHyyNDqYutkjz3AqDcF6yS0WQ6BmfJznNJBEm9iCIlxZYb5lbUylTHmYWsViGJxkdCf-gb27GzIkYwEmtufq1PHPt6Qc_Sroz27vPaCfKgpZ8RR1B-XrOhytnECE8yhnrCMaCTr4WhFhrvnjYVXeOgZetaMlQ7e180-qpOuwANoMoGrhy9V6igL4oFxMZ35JSaUARClxJtJeGN2s3CBFYB3Il3X1FmyeGiFCcRgTNS1D_uOgm0tDJnvR5HM0zWthuRHwH2vazVvB2btj1rQo_oVw4kjvdVpsNDPnAMjbaIYK3zdUaVZUqktYI3zBpVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT3MfDF7Sp_7hwnfqFVNGofHzfg4ejzXNK9pHNMd99YBQfuvDoeK3qyxezjwiz0QeWRwwv8pLV8s9mcCQ31KF6slGf1nYhP0EkgHy4qWhGD7BXiOum52h5Wp7oGTLChocIKtTZbj9RpC3toqtqL4ml_jtzXUAAdzQdY5Daum7NSeuBbThlL6vNCXhjRR_GHbiUPYcfGkrNWNDlSMyqgm7DnU4Syq1Ro0JHfHRmdcOl5Ujgq0gN5Nwd8wH3EPceajpHlsqYxxEaU5ilcMR51zNkyzzx9mPJ7wP8NH4Fp7T4BGxQPXY0BD_trYEQ31KhLGF12kOw4J6cWQRegz39Sh1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2HuQbXmyXSIcoFK-plMrWq_gQ5IJcInNfhKEPqM_e3ARFyf2OjkrVZq60xIoAycxU9qh7UHL-tj_d_wXvSEOv_eS8kh8XmgjBpozdeQWoWG05IQH-YB1D8kSg_f-2K8pAAwyW99xhnkP9lGfOdAbEy0OWhEq0xETSak6-RlZHrIvAVpjoAtfaFbsilTjlhTBxQClzmBcMJS7HGgTGGICm1wCpD7myzfrtTsEPN_5iDjUw9aY_XhjqZHAXHjpTC6odN7aq-xJPZzYXxfQQYrJPmQUJxaxX8wKGtrnRnurcZvz6AaAq6rYq8O-HgwjexZk9j6IZUjbvVLrNZ1ltdHqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9K40q1VuHNahYscax43mfNE5mW2D0Jm2Ye-21GWNUHCii65_PNgtBR9FnAOw3_4SJk9bUKp040ba_2cjbKPhHnXM6pE61orioesXYZ2Uz2JnVk19TXwWF1Qyu-r_1dDHIzgqOx5xRAszskm1zz9jv_ypVDNF7nYYWQ9j93zB9CJaAN3FbMi3aeGr1h9ZkK8GUslCJsg9TMsdI6erLQHGoaCuqkbnGe9Cm5Kgu02Zhhs00mBBV0ztL8ExuAH4M_K5_2bDU2iw16nUbmBNWrq5Q7ua8_gyrFY8ZfSo4Usoi1pPhrdkeDuJEOL0R6ut90LxCrpnhRpIMxRWsumBbCwuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvOS8NnPWidf9ciAEmzYnJOLuVLHx1p7gD-nEBe9G2xQM9RIoBJiVPVn1_CP_Hf6yzOxgxrnDQA5GUw3YZE5RsDwDaBVYKwKaDPXa7z91x4ozSR0Wo1JfjKnzQphiW5H4Cxyz79tIJ3YtzjhA4xWWtQXX-p_bTw3NtjrciUfSZbKqZxMy452YCXQQSXQJVshxDZBNsAFbrEWEZVrdnebgPlTE6Lp0VtQHZv7CnAPIogUYVuE8S26ep1xQLETE6HzZBZOTRSAjWhT_7M9rCmQpH2Ntt5S4Y2BCKBCIy4SekmYA5A4_4YQItzuYMAfVn91Jc9m75WCNqs8ffSxRG8-yQ.jpg" alt="photo" loading="lazy"/></div>
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

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=Z5c813nwMQTeNbZr_0m6JjoX2OJiqNc45OdjH7beEbLPj5-K-qynHXMVE3YshcOJ8COHIRf6MiTaaPo27kEVJb0P9IPLtNbHRvN3s7KYeBWStfNxay9sSVGNmPb0DAy08DD-TE3WJtPdSEIas0xEu9PP1s2HmT5SdmhnWRg-hca71lRDg6VNlBi6VOSYgf2Sd4QnsIqCWGNhFq7Fq4lA5V8qC5TBqBUTRjbYSeSn22USRU6y9gMpc4FvJ8D_y5zk13E9LWyQSnJ7rGj0C7hGDLMcjQGRmRLyEGfFvUmytSi5-MaHM0Fyu2d2GiFWyRExE5WkNh_QOeheel-MPCnsRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=Z5c813nwMQTeNbZr_0m6JjoX2OJiqNc45OdjH7beEbLPj5-K-qynHXMVE3YshcOJ8COHIRf6MiTaaPo27kEVJb0P9IPLtNbHRvN3s7KYeBWStfNxay9sSVGNmPb0DAy08DD-TE3WJtPdSEIas0xEu9PP1s2HmT5SdmhnWRg-hca71lRDg6VNlBi6VOSYgf2Sd4QnsIqCWGNhFq7Fq4lA5V8qC5TBqBUTRjbYSeSn22USRU6y9gMpc4FvJ8D_y5zk13E9LWyQSnJ7rGj0C7hGDLMcjQGRmRLyEGfFvUmytSi5-MaHM0Fyu2d2GiFWyRExE5WkNh_QOeheel-MPCnsRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره هفتم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی pinkpantheranim مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسر عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در ویدیو بعدی باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
