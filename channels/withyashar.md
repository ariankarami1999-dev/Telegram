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
<img src="https://cdn4.telesco.pe/file/sUayCqhsaXomu0GcDXiCvYhm0eNJ1Jv7ooLf8njMzmT-TWDuK7ExgC05MgTTEU1OUv6z_9xaccLEUPIgBPmAz-3zeqpAbw2EdY6h09BVSfjc6TxvfSnlo7odI-1_Htd5RDT2JLhVDYO9MnrDwjw72Yi8HJzHNMpnvCzqkaipBRSRcj8t2uTjRoHqIV7IS2-VxquqkQackEk-f5O6Kep2-xWrY9AEQ9qVfcU7jqjlWWEoI3fDxDOV-GIgewiDj52LARFw_9UufdE4mCDqmALiUH26fofa7qmovjE-jnvYauecmmQyX6dZrk9BvYL3hF5ORoG5zSygfJirbvN76-siag.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 477K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262002a591.mp4?token=SrAU954ZlJNCSoocTHDrw_v5tRw678TErNnfZ0LdRz2tc_R97G_osjs-m9EKDn8vzVovHfN21_ZyIh6mf2LXB_nN5AmpLh0t8UhWfLmflj1ph6YEqaCL7UwUrBa_BYlSVt3tBRSpStmUFN6qdTez9bq8WwSi-GKsw_9eI78Wie2eILe25PdQM7ZGLfTwVdwJ1DWFCn5HzmsppejnKYd0JYcumu-fzQsoyBKwb7ZRyQqP8ZWf0rWZefdxmgGDtkEW89Y0nSjAi78JpoyszKifRsob4S2W6YGlz0eCqc-PLZb3_ChSrDnk-yLPEdnBkQK-V8iTjYn-VT6PGXzzC-o74Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262002a591.mp4?token=SrAU954ZlJNCSoocTHDrw_v5tRw678TErNnfZ0LdRz2tc_R97G_osjs-m9EKDn8vzVovHfN21_ZyIh6mf2LXB_nN5AmpLh0t8UhWfLmflj1ph6YEqaCL7UwUrBa_BYlSVt3tBRSpStmUFN6qdTez9bq8WwSi-GKsw_9eI78Wie2eILe25PdQM7ZGLfTwVdwJ1DWFCn5HzmsppejnKYd0JYcumu-fzQsoyBKwb7ZRyQqP8ZWf0rWZefdxmgGDtkEW89Y0nSjAi78JpoyszKifRsob4S2W6YGlz0eCqc-PLZb3_ChSrDnk-yLPEdnBkQK-V8iTjYn-VT6PGXzzC-o74Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار ۲۵۵،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/24491" target="_blank">📅 16:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14e804573.mp4?token=apCABodHK2wnxCzpDb-f9Xi6vP01oqr1ZXuuMKiS9tGGtLcYis-OQCHeCLgwIEh76nymyGc5EYbMYvsh9dK-YKua6YrC--kiP2_GZvs28NcqRbzPvmwyaX42TyJUqwbJBl6JvK4CmtRLr9CPX-2YJtK3zQ439YZ8XZ2gUCGYIjiuU2o1CEXO-2xYBx4raPb-WfuehI66Aup56242WIBQov6cwAC9V0n8aFtG95TRh_7m8_f8HS3usV2GtEUvIrudT0hxg6XmbBTyB7hRAl4ZT0OosPzJrvuKQr9VRwdDG5LE4nIWzAh-4SlXGF5pxgh2cKyYNkT0P01Ln0awvzYuyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14e804573.mp4?token=apCABodHK2wnxCzpDb-f9Xi6vP01oqr1ZXuuMKiS9tGGtLcYis-OQCHeCLgwIEh76nymyGc5EYbMYvsh9dK-YKua6YrC--kiP2_GZvs28NcqRbzPvmwyaX42TyJUqwbJBl6JvK4CmtRLr9CPX-2YJtK3zQ439YZ8XZ2gUCGYIjiuU2o1CEXO-2xYBx4raPb-WfuehI66Aup56242WIBQov6cwAC9V0n8aFtG95TRh_7m8_f8HS3usV2GtEUvIrudT0hxg6XmbBTyB7hRAl4ZT0OosPzJrvuKQr9VRwdDG5LE4nIWzAh-4SlXGF5pxgh2cKyYNkT0P01Ln0awvzYuyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشنا نیست ؟ خودمم ندیده بودم !
@WarRoom</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/24490" target="_blank">📅 16:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری آناتولی:
یک فروند هواپیمای
کاسپین ایرلاینز ایران
به شماره ثبت
EP-KPB
در فرودگاه استانبول به دلیل بدهی حدود
۳ میلیون یورویی
به یک شرکت خدمات هوانوردی ترکیه، توقیف و از پرواز به ایران بازماند. شرکت
ACM Temsil Gözetim
به دلیل طلب خود علیه کاسپین ایرلاینز اقدام قانونی کرده بود و پس از صدور حکم، وکلا و مأموران اجرای حکم در فرودگاه حاضر شدند. هواپیما که مسافران خود را سوار کرده و آماده پرواز به ایران بود، با دستور مأموران متوقف و
مسافران و خدمه از هواپیما پیاده و به ترمینال منتقل شدند
و سپس عملیات توقیف هواپیما انجام شد. روند حقوقی میان کاسپین ایرلاینز و شرکت طلبکار همچنان ادامه دارد. این هواپیما یک
بوئینگ ۷۳۷-۵۰۰
است.
@WarRoom</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/24489" target="_blank">📅 16:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
ما معتقدیم
رهبر جمهوری اسلامی ایران زنده است.
برای اینکه هرگونه توافقی میان آمریکا و ایران امکان‌پذیر باشد،
ایران باید رفتارش را تغییر دهد و به تعهدات موردنظر آمریکا عمل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/24488" target="_blank">📅 15:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHfA00YCTByW373qyMDd1MYl97gbH53s24u6oGDJn1Hz1X9BvhLK8ZcZ8AHuGTtHiojFPTyJdLnrpvRZQJtUSfb5brudfR_YIOB3sk_AduoNgQoq3K_keGMBBOMdOi7jLO1UU-a6vGfkfCN5bM2rOQUk9oBR8hf0r7m80nak_TgJLUJB_eHeJML5DU_yd9V41iKcqQDo7eOhM4mst3U8MwcrIY63tJbvlflGKbKk3HxB_k7HdOYTKdIoGFvrHcVnhPxbrjajNAKoSFDwTK0lpFYxbHhhUFjRVzstq0zDLKC3wgm-iresUMf4YeW8m6yfq9IM7dECsnb-l0QHTOcpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان ۴۷ هاموی و ۵ کامیون از آمریکا دریافت کرد
ارتش لبنان در چارچوب برنامه‌های کمک نظامی آمریکا، ۴۷ خودروی هاموی و ۵ کامیون دریافت کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/24487" target="_blank">📅 15:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8fb30205.mp4?token=lcrRenkwNkX01Ly-4xwi-VAirP3bYnEjsCcMJRn19ckpEOBo9wmQCM1fiXHzFUzDDbusQH0Rqhe69WaWUtNqw0c_wslkOdEHdHtml68pOqn4RGMs5vBI5-swXZ0MCWoEfMQP-O8tGrb8NdkUTCHkMvGpAqrOFGWHcW6efwgEIJLzilby-Oq1CdR9q-JBOJFvp5UQfC8n09rOOeBkBGELu0vr6T1odaE9dtedITrl-4bS5q_hbDhf5YgJtYJ8a-fyTrJabZ7IBmoAkp1javo7-UQwdlbrLwjY-3hwxcbSO636dxg2IhjglD0yMTqQEcAYOy1sNiZp5yVLiiHnd8osYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8fb30205.mp4?token=lcrRenkwNkX01Ly-4xwi-VAirP3bYnEjsCcMJRn19ckpEOBo9wmQCM1fiXHzFUzDDbusQH0Rqhe69WaWUtNqw0c_wslkOdEHdHtml68pOqn4RGMs5vBI5-swXZ0MCWoEfMQP-O8tGrb8NdkUTCHkMvGpAqrOFGWHcW6efwgEIJLzilby-Oq1CdR9q-JBOJFvp5UQfC8n09rOOeBkBGELu0vr6T1odaE9dtedITrl-4bS5q_hbDhf5YgJtYJ8a-fyTrJabZ7IBmoAkp1javo7-UQwdlbrLwjY-3hwxcbSO636dxg2IhjglD0yMTqQEcAYOy1sNiZp5yVLiiHnd8osYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
دشمنان ما ممکن است پیش از انتخابات به اسرائیل حمله کنند.
در هفته‌های اخیر بیش از ۱۰۰ تروریست را فقط در غزه از بین برده‌ایم و در لبنان نیز به عملیات ادامه می‌دهیم. اجازه عقب‌نشینی از دستاوردهای نظامی را نمی‌دهم و به دشمنان هشدار می‌دهم که بازوی بلند اسرائیل هر جا و هر زمان به آن‌ها خواهد رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/24486" target="_blank">📅 15:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا به دولت عراق اجازه می‌دهد پروازها بین عراق و ایران را تحت شرایط آمریکا انجام دهد:
. پروازها فقط از فرودگاه بین‌المللی نجف
. پروازها فقط به مدت یک ماه
. پروازها فقط از طریق هواپیمایی عراق
. باید اطلاعات تعداد مسافرانی که جابه‌جا می‌شوند، نام‌ها و شماره گذرنامه‌های آنها، و مبالغی که هواپیمایی عراق در ایران برای سوخت، تعمیر و نگهداری و سایر خدمات هزینه کرده است، در اختیار آمریکا قرار گیرد
@WarRoom</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/24485" target="_blank">📅 15:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsw1l4S2rfGs_R-9n4BO1QdGNx4gl7hb3nzi_luEKA2u-N1R4FkJoSHk12pMeLCJVPkYVxre239JY1mZYm-BxW7WrDg_rOqD-b0c1cwvK0mK7jiHyRQ4tlHZQ5XzOh-Em5tkMntbSo0Q-EoHM6_lr5bnilPwuLKAOnvZBurQ9b_S-U4PnM9fG0DBhTvwjAJlmHOK7-50oxb2FhOzz09rHajWVMOvZ9Ez2k6fB5sI793xT7l59hD6CSJbzNCwdN4mMS-lV42ad-YQjglmcXRAq0fH_smBHtfnRfkDRUUlVtrKSr1zla3kFkaFgO_vpwFODLF0-wo8tL9MQpOxHacejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار دریایی UKMTO: طبق گزارش دریافتی، در ۲۸ سپتامبر یک کشتی در تنگه هرمز هدف پرتابه‌ای ناشناس قرار گرفته و دچار آتش‌سوزی شده است. آتش مهار شده و کشتی در حال حاضر در وضعیت اضطراری نیست. خدمه سالم هستند و گزارشی از خسارت زیست‌محیطی یا میزان خسارت وارده منتشر نشده است. از کشتی‌ها خواسته شده با احتیاط تردد کرده و هرگونه فعالیت مشکوک را به مقامات دریایی گزارش دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/24484" target="_blank">📅 14:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فیلم جدید The Fix با بازی لیام نیسون (Liam Neeson)
، داستان عملیات مخفی برای خارج کردن «مریم رجوی»، دختر فریبا رجوی، از ایران را روایت می‌کند؛ که در ازای نجات دخترش، اطلاعاتی درباره شبکه مخفی آمریکا و وقایع سال ۱۹۷۹ ارائه می‌دهد. فیلم با نمایش اسناد محرمانه درباره
خمینی، دولت آمریکا و سیا
، روایتی جنجالی از ارتباطات پنهانی آمریکا در تحولات منتهی به انقلاب ۱۳۵۷ و سقوط شاه ارائه می‌کند و همچنین به
مجاهدین خلق (MEK)، باج‌گیری، خرابکاری و ارتباط با قدرت‌های خارجی
می‌پردازد
منابع معرفی فیلم نیز تأکید کرده‌اند که بر اساس یک داستان واقعی ساخته نشده است.  مجاهدین خلق  پول خرج کردن باز بیان تو هالیوود ؟!! باید فیلم را کامل دید…
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/24483" target="_blank">📅 14:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دلار تتر ۲۵۲،۳۰۰ @Waratoom
🚨</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/24482" target="_blank">📅 13:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دلار تتر ۲۵۲،۳۰۰
@Waratoom
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24481" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وال‌استریت ژورنال:
یک گزارش مهم از کمیته تحقیقات سنای آمریکا می‌گوید
۸۴ درصد از ۸۴۶ کیف پول رمزارزی تحریم‌شده مرتبط با ایران، عمدتاً از USDT تتر استفاده کرده‌اند
. گزارش مدعی است این شبکه‌ها برای دور زدن تحریم‌ها، معاملات نفتی و تأمین مالی شبکه‌های وابسته به ایران استفاده شده‌اند. موضوع برای بررسی بیشتر به وزارت خزانه‌داری و دادگستری آمریکا ارجاع شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24480" target="_blank">📅 12:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد
عزالدین البیک، فرمانده تیپ شمال غزه در گردان‌های عزالدین قسام، در حمله اسرائیل کشته شده است.
البیک از فرماندهان ارشد نظامی حماس در شمال غزه بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24479" target="_blank">📅 11:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نرخ دلار ۲۵۰،۱۰۰ تومان (رکورد تاریخی)
تتر  ۲۴۹،۶۰۰ تومان(رکورد تاریخی)
بیتکوین ۸۴،۰۵۶ $
انس جهانی طلا ۴،۱۴۰ $
نفت برنت ۹۸،۶۹$
@WarRoom
۱۱:۳۰ ظهر تهران</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24478" target="_blank">📅 11:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراق: پرواز نجف به ایران برای یک ماه برقرار می‌شود
اما تنها شرکت هواپیمایی العراقیه، مجاز به انجام پرواز میان دو کشور است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24477" target="_blank">📅 10:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ممباقر
: هم آمریکایی‌ها و هم سایر کشورها بدانند در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت
خطاب به ترامپ: «بچرخ تا بچرخیم
!»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24476" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اتاق جنگ با یاشار : چند فروند جنگنده اف-۲۲ رپتور طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی لنگلی به پرواز درآمده‌اند.علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی آمریکا با نام عملیاتی CORONET نیز به پرواز درآمده‌اند که احتمالاً در حال پشتیبانی…</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24475" target="_blank">📅 10:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس‌نیوز: اسرائیل برای ازسرگیری حملات به ایران آماده است.
فاکس‌نیوز گزارش داد
اسرائیل کاتز، وزیر دفاع اسرائیل، هشدار داده است که عملیات نظامی علیه ایران ممکن است دوباره آغاز شود
و ارتش اسرائیل برای اجرای عملیات مستقل علیه ایران آمادگی دارد. کاتز پیش‌تر نیز گفته بود ارتش اهدافی را برای حمله احتمالی به ایران مشخص کرده و در حالت آماده‌باش قرار دارد. با این حال، گزارش فاکس‌نیوز به دیدگاه‌هایی در اسرائیل نیز اشاره می‌کند که از ادامه فشار و محاصره بدون بازگشت فوری به جنگ حمایت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24474" target="_blank">📅 09:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز:
پرونده امنیتی
RAF Fairford
وارد مرحله جدیدی شده است؛ پلیس ضدتروریسم انگلیس اعلام کرده پنج مظنون، همگی شهروند بریتانیا و ساکن لندن، پس از بازداشت به قید وثیقه آزاد شده‌اند و تحقیقات درباره احتمال دخالت ایران ادامه دارد و پلیس احتمال ارتباط‌های دیگر را نیز بررسی می‌کند.سفارت ایران در لندن هرگونه ارتباط با این حادثه را رد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24473" target="_blank">📅 09:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وال‌استریت ژورنال:
صادرات نفت خاورمیانه به‌طور محسوسی افزایش یافته و صادرات عربستان، امارات و عراق به حدود
۱۳ میلیون بشکه در روز
رسیده است؛ بخش قابل‌توجهی از جریان نفت از مسیرهای جایگزین یا با استفاده از تدابیر جدید دریایی عبور می‌کند. در مقابل، صادرات نفت ایران تحت فشار محاصره دریایی آمریکا کاهش شدیدی داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24472" target="_blank">📅 09:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c37bfc6165.mp4?token=dn1T95CvE--4cdpjm59xhpilJeQNZ786kr4Evl1KpDR5PhNalPO_d14xr5K3a4zp5YOjs_SYTXdE1ozEvI_9cL2m5YaYxBf4UId4_blL-XnYgCS_Y_sVG5ojynQjNF3Uql1IewTPHAMdDleCP8CY1ymNF161ZNGqMTm3hQ_u9NjLIhalGc9g1oqA0dqI0tlinpvsQWZusJY0DNyJWwPaCjbJeJAkFpThFgUnEJkkX2vjEJy0sn8bJOwBh7szcXIoNGdCrT_N-B_jw0ncFVOTAEMt_lUAOdFfppoXf0j1PiRTsyMjzr7XEOXlWocHc1qTF_18bJylXXT8Xp88U4s-2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c37bfc6165.mp4?token=dn1T95CvE--4cdpjm59xhpilJeQNZ786kr4Evl1KpDR5PhNalPO_d14xr5K3a4zp5YOjs_SYTXdE1ozEvI_9cL2m5YaYxBf4UId4_blL-XnYgCS_Y_sVG5ojynQjNF3Uql1IewTPHAMdDleCP8CY1ymNF161ZNGqMTm3hQ_u9NjLIhalGc9g1oqA0dqI0tlinpvsQWZusJY0DNyJWwPaCjbJeJAkFpThFgUnEJkkX2vjEJy0sn8bJOwBh7szcXIoNGdCrT_N-B_jw0ncFVOTAEMt_lUAOdFfppoXf0j1PiRTsyMjzr7XEOXlWocHc1qTF_18bJylXXT8Xp88U4s-2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام): ویدئویی از برخاست جنگنده‌های
F/A-18E/F سوپر هورنت و F-35C لایتنینگ ۲
نیروی دریایی آمریکا از ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» منتشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24471" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وار زون : یک فروند جاسوسی SR-71 Blackbird با شماره NASA 844، آخرین SR-71 پروازکننده در تاریخ، از محل نمایش عمومی خود در مرکز تحقیقات پرواز آرمسترانگ ناسا در پایگاه ادواردز ناپدید شده و اوایل امسال به یک آشیانه دیگر منتقل شده است. این اتفاق پس از انتشار تصویری…</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24470" target="_blank">📅 08:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیروی دریایی آمریکا : یک فروند هواپیما هنگام فرود روی ناو هواپیمابر «یو‌اس‌اس دوایت آیزنهاور» در نزدیکی نورفک ویرجینیا،آمریکا محل استقرار ناو در ساعت ۱۸:۱۸ روز ۲۸ سپتامبر (به وقت شرق آمریکا)
دچار سانحه
شد. دو خلبان با خروج اضطراری نجات یافتند. در این حادثه چهار ملوان نیز زخمی شدند که یکی از آن‌ها با جراحات غیرتهدیدکننده حیات به بیمارستان منتقل شد.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24469" target="_blank">📅 08:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبرنگار فاکس‌نیوز:
اگر ایران به سلاح هسته‌ای دست پیدا کند، تنگه هرمز و خاورمیانه چه وضعیتی پیدا خواهند کرد؟
مارکو روبیو:
ایران تلاش می‌کرد با انباشت
پهپاد، راکت و موشک
به نقطه‌ای برسد که دیگر نتوان برنامه هسته‌ای آن را از نظر نظامی متوقف کرد و سپس پشت این «سپر تسلیحات متعارف» به سمت سلاح هسته‌ای برود. ترامپ مانع رسیدن ایران به این نقطه شد؛ وضعیتی که می‌توانست
«کره شمالی در خاورمیانه»
ایجاد کند. اگر ایران سلاح هسته‌ای داشت، می‌توانست
تنگه هرمز را کنترل کرده و بر جریان انرژی جهان اثر بگذارد.
او همچنین حکومت ایران را مسئول کشتار
ده‌ها و شاید صدها هزار نفر از مردم خود
دانست و گفت داشتن سلاح هسته‌ای می‌تواند تهدیدی برای آمریکایی‌ها، اسرائیلی‌ها و دیگر کشورهای منطقه نیز باشد. روبیو تأکید کرد مشکل،
مردم ایران نیستند، بلکه «رژیم» حاکم بر کشور است
و تصمیم‌گیران اصلی را
روحانیون شیعه تندرو با دیدگاهی آخرالزمانی
توصیف کرد و تاکیید کرد تصمیم‌گیران اصلی،
آن مقام‌هایی نیستند که با کت‌وشلوار در برنامه‌هایی مانند Meet the Press حاضر می‌شوند، بلکه روحانیون شیعه رادیکال هستند.
ترامپ کاری را انجام داد که رؤسای‌جمهور پیشین آمریکا درباره آن صحبت کرده بودند اما انجام نداده بودند:
جلوگیری از دستیابی ایران به سلاح هسته‌ای.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24468" target="_blank">📅 08:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مارکو روبیو: ایران اکنون به‌سرعت به سمت یک
فاجعه اقتصادی
پیش می‌رود؛ موضوعی غم‌انگیز، زیرا ایران کشوری با ظرفیت‌های عظیم و مردمی
باهوش، سختکوش و پرتلاش
است که از
تاریخی کهن و دستاوردهای فراوان
برخوردارند. ایران پیش از روی کار آمدن روحانیون افراطی، یکی از مرفه‌ترین کشورهای خاورمیانه بود. مسئله فقط تحمیل فشار اقتصادی بر حکومت ایران نیست؛ این حکومت طی ۳۰ سال گذشته هر زمان به درآمدی، از جمله از محل فروش نفت و گاز یا کاهش تحریم‌ها در دوره اوباما، دست یافته، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم هزینه نکرده است. ایران این منابع را برای
ساخت سلاح، صدور انقلاب و تأمین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق
و همچنین حمایت از تروریسم و طرح‌های ترور در سراسر جهان به کار گرفته است. محدود کردن درآمد نفتی و اعمال تحریم‌ها فقط مجازات حکومت ایران نیست، بلکه مانع دسترسی آن به منابعی می‌شود که می‌تواند برای
کشتن آمریکایی‌ها و دیگران، کشتن مردم خود، ساخت سلاح، تهدید جهان و در نهایت پیشبرد برنامه تسلیحات هسته‌ای
مورد استفاده قرار گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24467" target="_blank">📅 08:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مارکو روبیو در مصاحبه با فاکس ترکوند ، غوغا کرده
🔥</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24466" target="_blank">📅 08:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرگزاری آسوشیتدپرس: ممنوعیت واردات کالاهای کانادایی به ارزش یک میلیارد دلار از سوی آمریکا اجرایی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24465" target="_blank">📅 08:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تتر ۲۴۹،۰۰۰ (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24464" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تتر: حدود ۵۵۰ میلیون دلار USDT مرتبط با ایران را مسدود کردیم.
شرکت تتر امروز اعلام کرد در سال ۲۰۲۶ و در همکاری با مقام‌های آمریکایی، حدود
۵۵۰ میلیون دلار از دارایی‌های USDT مرتبط با بانک مرکزی ایران و شبکه‌های دور زدن تحریم‌ها
در کیف پول‌های مختلف مسدود شده است. تتر همچنین اعلام کرد با بیش از ۳۴۰ نهاد انتظامی در ۶۷ کشور همکاری دارد و تاکنون از بیش از
۲۹۰۰ تحقیقات و پرونده در سراسر جهان
پشتیبانی کرده که بیش از
۱۶۰۰ مورد آن مربوط به نهادهای آمریکایی
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24463" target="_blank">📅 02:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">روبیو: من با وزیر امور خارجه عربستان سعودی درباره امنیت و ثبات منطقه‌ای، از جمله موضوعات مربوط به ایران، غزه، سودان و یمن، گفتگو کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24462" target="_blank">📅 02:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">وزارت خزانه آمریکا : بسند در‌ دیداری از دولت لبنان خواست تا اقداماتی را برای مختل کردن شبکه‌های مالی مرتبط با ایران و حزب‌الله انجام دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24461" target="_blank">📅 02:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=BM-ZAcX7Uv-oy_tU71vGO_qNGMCcLQNFzX9njUogequNClu-VYVDT4jk16IESjjB76bK1JbZ5QThdopbeSC8w-dg8CsCCcWHwvWUlu6P_8MIpbIl3rBlADVoBcqumBOaBtWvCUxB3v8xU2EbhGp6ezvb9ZVaWhKXZfIdVCWnEDwOiL0WjTAbXMgpRlVaLUxZ_4rStn8dNsA5w11avtHPYxA_VbJ3n_zOPXH1z5KAk2-oCJtiFAHCFHYh5xjw1T7BEqjhh7AMQFrJUK5i8a2AiZej9pdJTUtO3WMyTGGQ3IPO2F5AcOnQSVJAkTjjyMhBnW69GbkyWl92ztM9M-SvG2ZE2dMBHXSp_CXcDx5EbCFrE6e5ETmeOM3pw7H_-4sQisPHfqMR6fHKNEvobkKjzco07-K7R5jviJ8cit7pLw6A-5qAbIUk64tui_XAwrWpnB8OWsKvDVt-CCMT4L3yxsZvNQcpbTs6e1emG2RYdSOKMlm5OBBT_FT-IFL4PJ1sv-fdCZdqQXxEeUjaig6upMIm6gCkv9wmU47nDGgCqnNJ2fnho2U8zECEyhtX7uO42qujBW4w49vcCLH2PYtR9hniOtNA7bUm_Pdh-7pwT49aq7pG2Yrx9DUwAkwQ5Cm399XXQ_OddV18IrISe6BpGpQq87VEQAckZD1TyOaKnMo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6ac7d7f6.mp4?token=BM-ZAcX7Uv-oy_tU71vGO_qNGMCcLQNFzX9njUogequNClu-VYVDT4jk16IESjjB76bK1JbZ5QThdopbeSC8w-dg8CsCCcWHwvWUlu6P_8MIpbIl3rBlADVoBcqumBOaBtWvCUxB3v8xU2EbhGp6ezvb9ZVaWhKXZfIdVCWnEDwOiL0WjTAbXMgpRlVaLUxZ_4rStn8dNsA5w11avtHPYxA_VbJ3n_zOPXH1z5KAk2-oCJtiFAHCFHYh5xjw1T7BEqjhh7AMQFrJUK5i8a2AiZej9pdJTUtO3WMyTGGQ3IPO2F5AcOnQSVJAkTjjyMhBnW69GbkyWl92ztM9M-SvG2ZE2dMBHXSp_CXcDx5EbCFrE6e5ETmeOM3pw7H_-4sQisPHfqMR6fHKNEvobkKjzco07-K7R5jviJ8cit7pLw6A-5qAbIUk64tui_XAwrWpnB8OWsKvDVt-CCMT4L3yxsZvNQcpbTs6e1emG2RYdSOKMlm5OBBT_FT-IFL4PJ1sv-fdCZdqQXxEeUjaig6upMIm6gCkv9wmU47nDGgCqnNJ2fnho2U8zECEyhtX7uO42qujBW4w49vcCLH2PYtR9hniOtNA7bUm_Pdh-7pwT49aq7pG2Yrx9DUwAkwQ5Cm399XXQ_OddV18IrISe6BpGpQq87VEQAckZD1TyOaKnMo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن سبطی (یگال سبطی) پژوهشگر، روزنامه‌نگار و سخنگوی سابق فارسی‌زبان دولت اسرائیل: مجتبی خامنه‌ای زنده‌ست ولی هرچیزی میگه برعکسش انجام میشه ، اسرائیل منتظر درگیری بین رهبران رژیم مانند آخرای شوروی یا قیام مردمه.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24460" target="_blank">📅 02:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عراقچی: من پس از چند ساعت به تهران باز خواهم گشت و امیدواریم که سه شنبه پاسخ نهایی را از طرف آمریکایی‌ها دریافت کنیم.
هیچ تغییری در مواضع ما در رابطه با برنامه هسته‌ای ایجاد نشده است و شرایط ما برای بازگشایی تنگه هرمز کاملاً مشخص است.باید حرف رهبر اجرا شود
ما همیشه برای جنگ آماده هستیم و همچنین چیزهایی برای گفتن در عرصه دیپلماسی داریم. موضوع فعلی که مطرح است، صرفاً تنگه هرمز است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24459" target="_blank">📅 01:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عراقچی داره برمیگرده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24458" target="_blank">📅 01:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24457" target="_blank">📅 01:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24456" target="_blank">📅 01:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyij6qEHRTx5HOhXhYSPLtMlAx-zMFxmNlopjvZYu_GO5M7kkYNyjkmXv2R3n8y0hpvHfgzmVmOZn1o4KscRdmp69h8E2SJwBdQ-_RPwLcgfOs8xAtG_mM91hEWsQ9CwN2SfxY6z9Q50ols79k2Mz0Ttdk1vDP54TyOXYCPwz_ZB7x_KP4v3uGVbrvCX1lWg5Jh8gbgKqroV1NoSQ5obdOP9W4eg1x6uUcgfjWkMGUBfiP7MQus2ZwQsqT6Ji6NwSuBj1KE6sVFBaZmttNN8TXQcUDvg0dmesQrJcapj975DbtyX-e7W3fIKNA9FWsE8aw1EZqTeRQgeZJ37WvmVYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «آکسیوس به‌تازگی گزارشی منتشر کرده که در آن ادعا شده من به ایران
رفع تحریم‌ها و دسترسی به دارایی‌های مسدودشده
پیشنهاد داده‌ام. این ادعا نادرست است. من
هیچ چیزی به ایران پیشنهاد ندادم!
گزارش آکسیوس، مانند بسیاری از گزارش‌های دیگر، یک
جعل
است که صرفاً برای اهداف سیاسی منتشر شده است. آنها باید
فوراً این گزارش جعلی را پس بگیرند!
»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24455" target="_blank">📅 01:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24454" target="_blank">📅 01:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی ) دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی ) @WarRoom
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24453" target="_blank">📅 01:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXVGdxYaW6O1DG0B5y10o3HYjC-vI6zKHRGhFuAfTXfkwolyBh594hKOGqvxBj48ZpUXElVM0LDBrbHlU16ji-mYXX1Lt76S8-tOm5Hc9JModbct6f8fWvfdqGM22FNN9yNAQTqNi4UO6SaSnWfeCQTPP3efW4cd2V4-vMfdTe_rlx2IQQtMD9rwdVcCjk6IQonZQNziTsGUKry4rCOHl1BjaNT74Zn7s8AopUPVTofAn0HcWzR06hTawfLw-Q80sbWE5omPM-bGaaTf2egrLtMUb1Qm6VkMfoI3bWsZ-EWvRkrbC7lCqYXfmSu5rnJgGQz3qwRClMsHg286qHkzcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوی باشید ، تمام دایرکت شده نا امیدی غر نزنید ، بله اجماع شکل گرفته !
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24452" target="_blank">📅 00:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24451">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه  چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24451" target="_blank">📅 00:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from....</strong></div>
<div class="tg-text">داداش یاشار کی مث قبل لایو میذاری بگی تا صبح بیداریم امشب شب خطرناکیه
چرا نمیان پیر شدیم</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24450" target="_blank">📅 00:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وزارت دفاع عربستان سعودی: خالد بن سلمان، وزیر دفاع عربستان، از شیخ منصور بن زاید آل نهیان، معاون رئیس امارات و رئیس دفتر ریاست‌جمهوری، برای سفر به عربستان در روز سه‌شنبه ۲۹ سپتامبر ۲۰۲۶ دعوت کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24449" target="_blank">📅 00:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پرتاب موشک هم اکنون از هرمزگان بندرکنگ به سمت تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24448" target="_blank">📅 00:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.  @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24447" target="_blank">📅 00:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دفتر نتانیاهو : بنیامین نتانیاهو و همسرش روز گذشته به دعوت شیخ محمد بن زاید، رئیس امارات متحده عربی، به امارات سفر کردند. نتانیاهو در این سفر توسط رئیس شورای امنیت ملی، رئیس موساد، دبیر نظامی و مشاور سیاست خارجی همراهی می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24446" target="_blank">📅 00:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس: پیت هگست، وزیر دفاع آمریکا، در یادداشتی به تاریخ ۲۲ سپتامبر، به پنتاگون دستور داده از
توانمندی‌های اطلاعاتی و سایبری برای مقابله با مداخله خارجی در انتخابات آمریکا
استفاده کند. این دستور شامل جمع‌آوری اطلاعات درباره تهدیدهای خارجی علیه انتخابات و انجام عملیات مشترک سایبری با وزارت امنیت داخلی است. با این حال، این دستور
شامل حضور نیروهای نظامی در محل‌های رأی‌گیری یا توقیف تجهیزات رأی‌گیری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24445" target="_blank">📅 00:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتایج یک نظرسنجی جدید در «کانال ۱۴» نشان می‌دهد که اکثریت اسرائیلی‌ها در مورد هشدارهای پیش از ۷ اکتبر، به روایت بنیامین نتانیاهو، بیش از تحقیقات روزنامه‌نگاران اعتماد دارند؛ به‌طوری که ۵۴ درصد معتقدند این گزارش‌ها با انگیزه‌های انتخاباتی منتشر شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24444" target="_blank">📅 00:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شکایت «شین‌بت» از شبکه ۱۲ به دلیل افشای خبر سفر به امارات
سازمان امنیت داخلی اسرائیل این شبکه را متهم کرد که با افشای خبر سفر نخست‌وزیر به امارات در زمانی که هواپیمای او هنوز خارج از حریم هوایی اسرائیل بود, یعنی حدود ۵۰ دقیقه پیش از فرود , جان او را به خطر انداخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24443" target="_blank">📅 00:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-zecgd33Z3d-zMe7VkQ3wJOin_-O52rN6MNTUkfp93EhG0yxQ_lKPl9rl42TWxTcqDO24n0tkp0UTNcc5PLvFw3jKZX-zuU0GExu53irFE4urc3hX9Rkh_73O0q8_g3krp3ognIchJx0ZesFI2sHTTGyLTRA7I650EbWooShc4Cy2p5xxX-2CEveAudrtaRomPP6f5bqaAXoiXoF-CrID_krpYuFjcB7X8tHLp1bOFqZppRn4BPbvLuvfpEqdqLrz5V-m6g4j0W4uhBzjTys9AexElS4ZnGN5uwMPaarejx6ScGeDcG7GUIA9YiDskScITo5DeNJIN-w5mJLei7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت توییتر کاخ سفید: ظرف دو هفته چیزی از اقتصاد ایران باقی نخواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24442" target="_blank">📅 00:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=NyQyQHLn9aJ9KTSO92uOgf2Y85RZKWQeGaYQPXcJEoDeI4WSfLrdUYKxrMghCdAa-gkIqF-jgCc95pFjis5dUGxFxrUMVfQz1eCl7u08UccVmtzsAKfjPUjprfoj8628WSZiktoc1Rh040Ht0Ej2JC_q3f2zj2_znNxhaKJ7bdKorhiYUShQsJ_bx3wdqKxenuZJ3JNzysu9qeIb0aaborihVETYYKvFX71lLqoRoxFVZ7O7nNJLgg6mBS8JbhBhKDolt4_VhX-QaJ_0m-MVtLMpR55eL88KXzo7jDUDxDrQLMAHJUYVIfq4aUoPr1dYHu0RMKYpNZ3tDRp-uRvXew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4109be46a.mp4?token=NyQyQHLn9aJ9KTSO92uOgf2Y85RZKWQeGaYQPXcJEoDeI4WSfLrdUYKxrMghCdAa-gkIqF-jgCc95pFjis5dUGxFxrUMVfQz1eCl7u08UccVmtzsAKfjPUjprfoj8628WSZiktoc1Rh040Ht0Ej2JC_q3f2zj2_znNxhaKJ7bdKorhiYUShQsJ_bx3wdqKxenuZJ3JNzysu9qeIb0aaborihVETYYKvFX71lLqoRoxFVZ7O7nNJLgg6mBS8JbhBhKDolt4_VhX-QaJ_0m-MVtLMpR55eL88KXzo7jDUDxDrQLMAHJUYVIfq4aUoPr1dYHu0RMKYpNZ3tDRp-uRvXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا تیم شما امروز با ایران صحبت کرده است؟
ترامپ: بله.
خبرنگار: با میانجی‌ها؟
ترامپ: بله.
خبرنگار: چیز دیگری هست که بتوانید با ما در میان بگذارید؟
ترامپ: ما پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24441" target="_blank">📅 23:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تنگه صدای ناله های حسن خرسی میاد</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24440" target="_blank">📅 23:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">قشم صدا میاد</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24439" target="_blank">📅 23:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24438">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">نیویورک پست: به نقل از یک مسئول آمریکایی، دیدار مقامات ایرانی با کوشنر و ویتک در نیویورک، منجر به مذاکراتی از طریق واسطه‌ها درباره امکان باز شدن تنگه هرمز شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24438" target="_blank">📅 23:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8EQKd6ekgezZFQYUW4z95vqXEIrjWvrCoQ7ZR4XM0YCQEJjpzoEhC1h_HoYZORMOmUOzPXHvJTyNi-8JPmscl0xcG6z1EMwyPAxjvwRbScF6GwK8WrdOyWgvVtZF1OYLS_cqxedWRHCvllkaYGf1McsjTWvU4zPj_xyU5zRsVtMSGyx3_zeyeWcIU-ikZtuG7VlEFBMhbsV5QnxW1Y4gVGwMXzRU3eHa2Av3SwXwXdp4d8QtnHT71HCUrk-hCgahoSPbWEIkv_FjIHCiKVQya5lh79yRylLRMIWTnddfxJwSLUBBfMt-dZqxC4fHNYmkvlP4tVwCHJsfpZaokwVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حضور
پنج فروند هواپیمای سوخت‌رسان، یک فروند T-38A Talon (هواپیمای آموزشی جت مافوق‌صوت)، یک فروند پهپاد MQ-4C (پهپاد شناسایی و مراقبت دریایی دوربرد) و یک فروند E-3B Sentry (هواپیمای هشدار زودهنگام و کنترل هوایی)
در محدوده تنگه هرمز و خلیج فارس رصد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24437" target="_blank">📅 23:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=d1kIEQc9wGiN0zTyOug0VBcHPjmtSyeRkDZXaLFvOSklQRgG6m8rqpnEJgic4TM55Jl7r63Yxy-uEjAarOr62o7p32WLkpRf-8O1lsTeA10AEkr6p-ubBo0q9IaKU-yTwdT6vZ3hnIuR_liuIoUCkhnQfjcMBKClO9ne_-55CpuFeBjN93pAL9XxlT-ihAe5RTiHA7umLO000E4iCg6_Tt2-1CfX8M2zEHWiOxwwBfwn-0x_rEqHq7SGwa63_azDsIhNAKiHsOMKfMI7SvCc1fhE4ju__s1iRxV1QdqXavS1UuEFE5RM9o0q__GzO_9ivNwfbg2Im2Y4qLne60eg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e37e38e4cc.mp4?token=d1kIEQc9wGiN0zTyOug0VBcHPjmtSyeRkDZXaLFvOSklQRgG6m8rqpnEJgic4TM55Jl7r63Yxy-uEjAarOr62o7p32WLkpRf-8O1lsTeA10AEkr6p-ubBo0q9IaKU-yTwdT6vZ3hnIuR_liuIoUCkhnQfjcMBKClO9ne_-55CpuFeBjN93pAL9XxlT-ihAe5RTiHA7umLO000E4iCg6_Tt2-1CfX8M2zEHWiOxwwBfwn-0x_rEqHq7SGwa63_azDsIhNAKiHsOMKfMI7SvCc1fhE4ju__s1iRxV1QdqXavS1UuEFE5RM9o0q__GzO_9ivNwfbg2Im2Y4qLne60eg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «من وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاقاتی باشد که تا به حال برای جهان رخ داده؛ برای ما، اما در درجه اول برای جهان. اسرائیل همین حالا از بین رفته بود. دیگر اسرائیلی وجود نداشت، خاورمیانه‌ای وجود نداشت و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا روانه می‌شدند. و من جلوی آن را گرفتم.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24436" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=MGoYG-8VozcRhbNi6Ec96YS2VoUAJpc8eMlKAk62aaHSSDYWELfP6R73vOAmM-nAkqdT-HgU8x2QEKO65QHUEVclcbIJnrwc6HYlz3Mm8BixNBEw1u-1f73XRDcRnejTFhgPI_hZnISrrEztjUqNBxICDhNDV7Kaw4S6TfBXpOSmF73VFB_Pna5poFG5XVe_PJiCkUPDHIEzcZpEjGsZR5zO64bdnjsAZhvtLCEevUBA0Q3zWUWwMg6AonT-rPjoe-Q5mF-DUyy6ePaIEAtOZOLtQSSwAyYcy8ZVs9KZAf51DNhmDGsYJUdijZEAjxqXT-z7XwupgzzuYnJiM5UWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcbc9a39f.mp4?token=MGoYG-8VozcRhbNi6Ec96YS2VoUAJpc8eMlKAk62aaHSSDYWELfP6R73vOAmM-nAkqdT-HgU8x2QEKO65QHUEVclcbIJnrwc6HYlz3Mm8BixNBEw1u-1f73XRDcRnejTFhgPI_hZnISrrEztjUqNBxICDhNDV7Kaw4S6TfBXpOSmF73VFB_Pna5poFG5XVe_PJiCkUPDHIEzcZpEjGsZR5zO64bdnjsAZhvtLCEevUBA0Q3zWUWwMg6AonT-rPjoe-Q5mF-DUyy6ePaIEAtOZOLtQSSwAyYcy8ZVs9KZAf51DNhmDGsYJUdijZEAjxqXT-z7XwupgzzuYnJiM5UWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «به‌محض اینکه این جنگ تمام شود، تورم به‌طور کامل از بین خواهد رفت. کاملاً. هیچ‌کس درباره این موضوع صحبت نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24435" target="_blank">📅 22:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24434">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=K02htWXhp4IIBA8b3OzeYkZ-daxz5fkrZRNHQ9ud2lig64KlL4343Y9iewf3OHd3zw7LltxAnSVAEZu2qgfFu_Bgq7Qv9nrjBfZUyvYKbnXKbFxCCnpq8qqRiZqe8rZct5EL80PuPPMTl7wphXcA-Bu8QqyQAcoX1ntu2XewScL3eJZQckIPAiWGX3nZOJKmj7BiEOp-yL0ENsl_ggZKt_KGPQn_quhjc2KNSF_Luqt27h-iQkf5TWZ7Jn9rcIHL2-X858xejeJb8-aSWTJ2MSSEigw-9C7o9yqTmW2NLrHhMyKnc_RqHP_XIe3TlSpKdpDci22PyKecqYskhqh8Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd292496.mp4?token=K02htWXhp4IIBA8b3OzeYkZ-daxz5fkrZRNHQ9ud2lig64KlL4343Y9iewf3OHd3zw7LltxAnSVAEZu2qgfFu_Bgq7Qv9nrjBfZUyvYKbnXKbFxCCnpq8qqRiZqe8rZct5EL80PuPPMTl7wphXcA-Bu8QqyQAcoX1ntu2XewScL3eJZQckIPAiWGX3nZOJKmj7BiEOp-yL0ENsl_ggZKt_KGPQn_quhjc2KNSF_Luqt27h-iQkf5TWZ7Jn9rcIHL2-X858xejeJb8-aSWTJ2MSSEigw-9C7o9yqTmW2NLrHhMyKnc_RqHP_XIe3TlSpKdpDci22PyKecqYskhqh8Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: «اگر می‌خواهید شاهد آشوب و یک فاجعه باشید، بگذارید آنها یک شهر را با سلاح هسته‌ای هدف قرار دهند. من فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. بگذارید آنها با یک سلاح هسته‌ای به خود ما حمله کنند؛ خطاب به تمام آن آدم‌های احمقی که فکر می‌کنند چنین چیزی اشکالی ندارد. آنها دیوانه‌اند. هیچ شکی در این باره نیست. آنها واقعاً آدم‌های دیوانه‌ای هستند. من همیشه این را به آنها می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24434" target="_blank">📅 22:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=Cw3K5Luj5UmFuE27Yob0biPpspOCtC73xIuvpG11RS8G4Lc1w8G9vA1uADEhy4CjrEu9hiUo5AFNDk1ESzqs8UfiW-x8nCD8kEvq47WXttPfs31tLIquYp4wFAImQSK78mqN8Ek2P3-pO6CtGZC0VK7MM1vT0THch5xDwT1ZAw1S5yq7DW_3dSROwsbtSweXiZgnuKrHWD41Y7gWcj65d40mumxHR6EknxSw1kaApEC7ku17YccEpYlbm3gcFQB8bmv9KfyAC1L3t1A17i2lPDmZBbFRFs9XzCXRnmRcUjwbet2Iw_2c6tGODhzfado6OK_inBPcPHHUt80Y4ZgdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec45ce4fdf.mp4?token=Cw3K5Luj5UmFuE27Yob0biPpspOCtC73xIuvpG11RS8G4Lc1w8G9vA1uADEhy4CjrEu9hiUo5AFNDk1ESzqs8UfiW-x8nCD8kEvq47WXttPfs31tLIquYp4wFAImQSK78mqN8Ek2P3-pO6CtGZC0VK7MM1vT0THch5xDwT1ZAw1S5yq7DW_3dSROwsbtSweXiZgnuKrHWD41Y7gWcj65d40mumxHR6EknxSw1kaApEC7ku17YccEpYlbm3gcFQB8bmv9KfyAC1L3t1A17i2lPDmZBbFRFs9XzCXRnmRcUjwbet2Iw_2c6tGODhzfado6OK_inBPcPHHUt80Y4ZgdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا حادثه پایگاه RAF Fairford به ایران مرتبط است؟
ترامپ:
«ممکن است مرتبط باشد، اما باید بگویم از اینکه آنها [افراد بازداشت‌شده] را آزاد کردند،
متعجب شدم. من این کار را نمی‌کردم.
»
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24433" target="_blank">📅 22:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24432">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ: امروز از طریق واسطه‌ها با ایران گفتگو داشته‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24432" target="_blank">📅 22:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24431">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6885716a79.mp4?token=TZ7arRvyGBYk8h3NWmADO5c6lDBmVI20YWofr5linv5Xl9ZpLFVD-30WAKQh__yXh7rTp43MfwzvuEBpa5orbHhpsKWoHmgy4pRysf4eudU3oAr9nXK5GZQj6YYMq2dUr_jzuB_qbE4MbLF-q2Az6MZu668RoCiOjev88aF1_yXJouc43--UgI3HlyvpePe7ffSCbsxYiHf3CrgLLRrjZL4OjCzkpGUuFP65x7PPjN3JljCHygfmnl4pK2OnPe_0Z3fdU3FeT4hmG9tZuTP-NKJprRxeejNaeYVjq-RuCJNjPj2cvDDtGdSqWKCrVhPYqmEzoCG7eaUl4mW3VxuAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6885716a79.mp4?token=TZ7arRvyGBYk8h3NWmADO5c6lDBmVI20YWofr5linv5Xl9ZpLFVD-30WAKQh__yXh7rTp43MfwzvuEBpa5orbHhpsKWoHmgy4pRysf4eudU3oAr9nXK5GZQj6YYMq2dUr_jzuB_qbE4MbLF-q2Az6MZu668RoCiOjev88aF1_yXJouc43--UgI3HlyvpePe7ffSCbsxYiHf3CrgLLRrjZL4OjCzkpGUuFP65x7PPjN3JljCHygfmnl4pK2OnPe_0Z3fdU3FeT4hmG9tZuTP-NKJprRxeejNaeYVjq-RuCJNjPj2cvDDtGdSqWKCrVhPYqmEzoCG7eaUl4mW3VxuAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ما
خیلی زود در این جنگ پیروز خواهیم شد.
این جنگ تمام خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24431" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24430">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=QYfL49RwoHbzZ6qhBZrU4803uZ3xE1K4Jib9FOd13nJ5Bdk5E7Y2PCsIhVXvhnrCIkOjzVkprxAzlvhfRyIJxUgjSqXoTKrQiXTrTOmVvSOrOpDOt0D-_NsrpKG6lqJ8lUTRF2WfVrzM8Hk9D-4xvH6pHqtqmcUx42RfP7FxhUTUl1UuQShVbDYdnzGdlZlvItX2RN7kJWzpgg5586JYP5hsceMUUxVNyjz4Xdn1S-s3Al0-BbFnwWE_MD3x_y7wViv1tlGnDMDZaj1oQMdPsuKrTJrLj2nCP9ivZ5UIjiJN_H8i7FG7lif0hf08XDDLxeuNKewJ0mxTYcwJ1G1d6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e7e5f951.mp4?token=QYfL49RwoHbzZ6qhBZrU4803uZ3xE1K4Jib9FOd13nJ5Bdk5E7Y2PCsIhVXvhnrCIkOjzVkprxAzlvhfRyIJxUgjSqXoTKrQiXTrTOmVvSOrOpDOt0D-_NsrpKG6lqJ8lUTRF2WfVrzM8Hk9D-4xvH6pHqtqmcUx42RfP7FxhUTUl1UuQShVbDYdnzGdlZlvItX2RN7kJWzpgg5586JYP5hsceMUUxVNyjz4Xdn1S-s3Al0-BbFnwWE_MD3x_y7wViv1tlGnDMDZaj1oQMdPsuKrTJrLj2nCP9ivZ5UIjiJN_H8i7FG7lif0hf08XDDLxeuNKewJ0mxTYcwJ1G1d6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ:«اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، به هر فرد بزرگسال ۵ هزار دلار پرداخت خواهیم کرد. و ما می‌توانیم این کار را انجام دهیم.
دموکرات‌ها نمی‌توانند، چون هیچ درآمدی ندارند و کشور را به سمت رکود اقتصادی خواهند برد. آنها هیچ پولی نخواهند داشت.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24430" target="_blank">📅 22:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnyHYm_4ZpZt94xs-NXqzJw3QVCHNaGhhY9grwTJTtExZm_m98V1kL-tc_3ur2rQ7D1Ur3kT2mk4bFugVdB0sRzqs4DipKMvrI9bk8GXHip2htiQ82m-C3DSI-BfAiMU4iNYw-fTdkZIt3rm4pdKLE5pXkXwFHo-WER_DGXMYr6Ub8vyBcgtwjH9Qp_6ssgZNYVNkIViJiGdH_owoseQjDnyWZeFa7IWrET_ZfpnxD59f-L1pTju-pDGeyYAQ296MEY6SIBG6sa2Wt596CsPR6WsYzuul2Z_qeDaNazgO_kogOHzQ4B0i9kJuLNyTqOip1Ral1Mk5ECggqA2bjjaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بزرگترین کارخانه فولاد در آیووا ساخته خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24429" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">باراک راوید ، آکسیوس :به گمانم ایالات متحده می‌خواهد شاهد آن باشد که ایران بازرسان آژانس بین‌المللی انرژی اتمی را دوباره دعوت کند؛ کاری که در جریان مذاکرات سوئیس متعهد به انجام آن شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24428" target="_blank">📅 21:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24427">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امارات متحده عربی سفر نخست وزیر اسرائیل به این کشور را تکذیب کرد</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24427" target="_blank">📅 21:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70875dba60.mp4?token=VK3IVN1SnibS3_GN-H57U5nl9phrx6PP4BLkJja2_SKUWqxNR2W7RTDSFJVFzC0Dbh-ywM4PwnerOJGx_Vw85wruB6kF7kBhjoWz6KMvTbJNekl__kXnk6AmkWFjb6e-h330DAqQu1ojkjNcP9-almx4PwUIYnjBbVfuX1zrU45Zy7wDbncCPovEo2UDcfndoDEDY0dIgyc4zvsSygRCi5lH8ACA1nE9xxmC1vTqm71F2SIoMZcLJXm74zqNarV7P1itoP6Wad2NcTnha5SCYTWE3Yjss8NNrdFrxu5dJhQxU6enVxak9Nkhay_LtxoXtdJAv3YUhBrk5ns0GfPh25XbbuhCavIigqhx5YKz3D_t7Sn0w01otymunUuTaBQbUPzmXyPvd1l-XwxBPUdYxQFCZWioWytM0iUvf4UWn5TMenvR36MIELsLnoSpdvuXibPc1-PXnk_cERAoxm8cuWZAz2q6WDGfYom6Mp2iLnegjVm7j9847sLmWQMaepi1LJ2H57XVP-7ZB569RSnK-RYmKFd1EZp8vfmoHpDSmvt6IE1LFXIiW4x9YPPNiZ8VfHQWVcWUdZU84-QorGZtu12gGVn6sTzUN5xXsH_bVXK1CVPyPzcLyLmZVKrm1hSMTB60xwZoIkoV5CT82VlACImQldajq8tp0XE9rSfWKWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70875dba60.mp4?token=VK3IVN1SnibS3_GN-H57U5nl9phrx6PP4BLkJja2_SKUWqxNR2W7RTDSFJVFzC0Dbh-ywM4PwnerOJGx_Vw85wruB6kF7kBhjoWz6KMvTbJNekl__kXnk6AmkWFjb6e-h330DAqQu1ojkjNcP9-almx4PwUIYnjBbVfuX1zrU45Zy7wDbncCPovEo2UDcfndoDEDY0dIgyc4zvsSygRCi5lH8ACA1nE9xxmC1vTqm71F2SIoMZcLJXm74zqNarV7P1itoP6Wad2NcTnha5SCYTWE3Yjss8NNrdFrxu5dJhQxU6enVxak9Nkhay_LtxoXtdJAv3YUhBrk5ns0GfPh25XbbuhCavIigqhx5YKz3D_t7Sn0w01otymunUuTaBQbUPzmXyPvd1l-XwxBPUdYxQFCZWioWytM0iUvf4UWn5TMenvR36MIELsLnoSpdvuXibPc1-PXnk_cERAoxm8cuWZAz2q6WDGfYom6Mp2iLnegjVm7j9847sLmWQMaepi1LJ2H57XVP-7ZB569RSnK-RYmKFd1EZp8vfmoHpDSmvt6IE1LFXIiW4x9YPPNiZ8VfHQWVcWUdZU84-QorGZtu12gGVn6sTzUN5xXsH_bVXK1CVPyPzcLyLmZVKrm1hSMTB60xwZoIkoV5CT82VlACImQldajq8tp0XE9rSfWKWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وس استریتینگ، وزیر دفاع بریتانیا، درباره ایران:
«فکر می‌کنم حمایت از اقدام دفاعی آمریکا، کار درستی بود.
کاملاً درست است که بگوییم جنگ در ایران، جنگی نبود که ما انتخاب کرده باشیم؛ اما در عین حال، هیچ شکی نیست که ایران نیرویی شرور و مخرب است که بریتانیا، منافع ما و متحدانمان را تهدید می‌کند.»
پلیس گلاسترشر گفت ساکنانی که به‌دلیل احتمال وجود توطئه‌ای برای حمله به پایگاه هوایی سلطنتی فیرفورد (RAF Fairford)، از حدود ۸۵ خانه در اطراف این پایگاه تخلیه شده بودند، اکنون می‌توانند به خانه‌های خود بازگردند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24426" target="_blank">📅 21:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک منبع آمریکایی به شبکه العربیه گفت: اختلافات و موانع بزرگی بین تیم‌های مذاکره‌کننده آمریکایی و ایرانی وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24425" target="_blank">📅 21:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ8KZCbDVSp-mgN84JWI4f8OrkzrkPv2bXsGLvj8TCSth5EOwF6-RXU2qoekJFSzFr4q05LooN48ozqiqDToCJ2bwpxHg-bR9OaXhzKM1EXdwpTpYh63qqDsDZwg6i6yMW3Kx1LsgQ6oyRxXSUJXY5Yq5v0Juyi920pOiv1JYLiKmu_m1PwcnLkGzJRsiCwhwCe62sFxYAdgxNqXu0Dm2UlFwTXzeH_PZWPyZSkMCrRIi72FnqXWVjkjUAdOWuzgM755PJi_ln05z5MbYGVQCPzKCJQh-XIczd1cp2YUn7QfDAPAVaCEZVN1c3BBptA9pA-5rZdNlJQ8FStD8LIipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
عملیات طرد اقتصادی باعث شده که ریال به رکورد‌های پایین‌تری برسد.
ما به تخریب توانایی رژیم ایران برای تأمین مالی تروریسم و توسعه سلاح هسته‌ای ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24424" target="_blank">📅 21:37 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش اسرائیل : لحظاتی پیش، یک موشک رهگیر به سمت یک هدف هوایی مشکوک در منطقه‌ المطلة  که سربازان  ما در جنوب لبنان در حال عملیات هستند شناسایی شده بود، شلیک شد.جزئیات در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24423" target="_blank">📅 21:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کانال ۱۲ اسرائیلی:
نهادهای امنیتی اسرائیل در حال آماده‌سازی برای احتمال از سرگیری درگیری‌ها با ایران هستند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24422" target="_blank">📅 21:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frjC1r3K_0ZN8ixPL6G5UV5EZjTP34gV-7nnNXpJ_e9DJgY4yppS7fBXI0C8b0wRLdlPSLnMj4yrwtMdVP9Qa2gM-xvLEg0oRm20CgbK5c_6wxufk43Xwf4maupr-PRWik8zQM82V52tc2rxQVcRbTK8zpLzW6N7Ahou9qgInWGS0NBrgNJC9I1tKp_SyzeHI84zUtAyO6sWGXrJgvDJxODgJ7vtrcfIoGriXMij-PEqNH9dcdIWHjH4DvyuJZLc6cYf5P9PifRkVBYIyxN9yorRHZFd8h56_ZwZ5Y9uFmxKp-DMZRPQbg8UUX9heuqgQmZUs22m5eVzPn8pYJcSWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل:
شَدی ابوحطیرا، از تأمین‌کنندگان مالی حماس که شبکه انتقال پول «ژنو» را هدایت می‌کرد، در یک حمله هوایی دقیق در غزه کشته شد. ارتش اسرائیل مدعی است او
ده‌ها میلیون شِکِل ارز خارجی
را برای شاخه نظامی حماس منتقل کرده
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24421" target="_blank">📅 18:39 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مورگان اورتگاس، معاون فرستاده ویژه آمریکا در امور خاورمیانه: «سناتور لیندزی گراهام هرگز از باور به شما (مردم ایران)دست نکشید. او باور داشت که شما دوباره آزاد خواهید شد. او هرگز از تشویق رئیس‌جمهور ترامپ و وزیر خارجه روبیو برای حمایت از آنها (مردم ایران) دست نکشید.»
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24420" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W__UtOoe4jlFnODNDSi8eqKc3EuAnIG0bKHzTF8Bp80MdzS4MIE2kaqrgwHavknajYLrGL6vPXf7hchen7Z3HZCX0VubPyEMeZ6knH1hLr2gWJa9Qu41xdCivO0INqeKRcBv2oe_GHXI2j-5ONklltyIBF1fxHW_V12bcT-P4_AHzqmvyiDvSNde5izwtcw0nTR9LPcfwVQrh4jzboETLJH1D5xQzRCNeW40BEPoIAbizGTnNV4VI_4lmm0_Q_5wr69GSQ3_zqd_7DgXj4Dk3o3Lun_GVKIj9Db_gmRpzlYxiKvLUyGpWM4TTzex-SSFU3ZPJTN3Mu0ipQCovdvFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه عراقچی موفق شده یه ناو جدید اعزام کنه ۳ دسته هر کدام ۵ فروند هرکولس و ۱ اسکادران اف-۲۲ ، این است «قدرت مذاکره»
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24419" target="_blank">📅 18:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24418">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تسنیم : عراقچی امروز با میانجی‌گران در نیویورک دیدار می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24418" target="_blank">📅 17:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران: کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت ۱۸:۳۰ یک جلسه سیاست‌گذاری در کاخ سفید و ساعت ۲۰:۰۰ و ۲۰:۳۰ دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت ۲۱:۳۰ ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و…</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24417" target="_blank">📅 17:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارشهای بسیار‌ از دو انفجار سنگین در تنگه هرمز
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24416" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMarkvqFkRH5P6PRgBAwaGOgguPkJ95OC7NNDVzW2HbgRCaYFoMxIw62gWm6ll56uKhfiI3_7Vc9mIbD0868BrSHwX1HVcWoA-TWM0m9EBdarIwAaQwlqVCZ_b5UVmy9UkqI9SX4Vn65YnlB2qDMEXPNALcHkd0EPedcFojCfeJlwHhUW_O76UKWkGy8ta-maoreUK_kff8H1jJ-jgwCtvhMD0mxYO9zpDZuY_6pb605XxcxHg6wdgtclz3nTf5ocXTagqtydDYDoFEREGxHQ065aL5mfHQZr5g9n2KK0W-wqQavKyPSE_kdpnBI6XGl8sqlUlYgy0D1tos0RJQFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : فلکه دوم فردیس لانچر و موشک آوردن
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/24415" target="_blank">📅 17:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">برنامه امروز دونالد ترامپ به وقت تهران:
کاخ سفید اعلام کرده ترامپ امروز دوشنبه ۲۸ سپتامبر، ساعت
۱۸:۳۰
یک جلسه سیاست‌گذاری در کاخ سفید و ساعت
۲۰:۰۰
و
۲۰:۳۰
دو جلسه دیگر در دفتر بیضی خواهد داشت. سپس ساعت
۲۱:۳۰
ترامپ در دفتر بیضی مقابل خبرنگاران حاضر می‌شود و
یک اعلام رسمی مهم
خواهد داشت؛ موضوع این اعلام هنوز رسماً اعلام نشده، اما گزارش‌های منتشرشده آن را مرتبط با
هوش مصنوعی
می‌دانند. ترامپ ساعت
۲۳:۰۰
نیز با خبرنگاران رسانه‌های چاپی دیدار و گفت‌وگو خواهد کرد. شام خصوصی ترامپ با
داریو آمودی، مدیرعامل Anthropic و سازنده Claude
مربوط به شب گذشته بوده است. همچنین فردا ترامپ و مایک جانسون قرار است با مدیران شرکت‌های بزرگ هوش مصنوعی دیدار کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24414" target="_blank">📅 17:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">امروز ترامپ بیانیه ویژه ای ارائه خواهد داد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24413" target="_blank">📅 16:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24412" target="_blank">📅 16:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4WYEUtoICkRKpLE9J0AgkZ4W181YUs642TIE4WdhN6r0M-mnNMqwcuEu18GusJid6iOIJxYi960g10BDRP4njF4jAZY3sPGI3k9ASNNZ0kPbPgx0JS3i4To3uAjU1Uat4mJEaKxejUW8riO0LHU1eq3bdawXepnPftLxbvdAkKKKaYZLmApeMlcQcXMylXAkNeVQC4nwM8ZsmhKL6igkAXRmtmKTDHce9_yyQEI2Odtbt_JCn5ZzTNcvbDbcBkzL5ikOlpcVsajOQAjiLpdHoLDW16gEExYgd15zX7hNDGgnPoqo3RmKmpA2exOecfjgWmnMg6D9RFUOiBRO5qGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092268a67d.mp4?token=vztEtPrDdaipurfaIT2Hzyh0v2InOgNJHcGNH9qVlpsI_B5EEU0Yhnne4_wK4IaFPjVKcMUQx3KNFH2L6ULTfzUd2jPQddZvvvL-h0Dpjjj-ErY7DoGvbQX6usb5JB1rIXUlWIMyf6mpMrETlw-Cu_rCirGoFVNH3c0iH0-oW7eLsMXsXxd2SoVrCnlRaZHO6MnfL4doGeGYQ8-EB8viQ8P1_rhh6cJOkZldYcsK9lFKnzsAVuaxE594-Twy9UYQHmlc7kfDrnBKJ22xrhpoxQz9syHcrpyGEm9HzD4-LcpOI0QaaoRx-bYFkJt0a3j20moki1z0XcSHzQSjua6m5grOFQ1zi9md8deJf5yXqBSYeAEClYtqcLXtVHooGK_72BZrOFu-UTLwACtY0V8uynq4NDpsYnYo5vHOCiHQ7urcsvw2zR8HkxgYBlTfVBsESvi0NbfQVo6W9NQe24fbf5kehr4p8qzE6cAHguOt5hjTnQuEee1HYUGqouOTzLYNxRfvIxCVDtZ0kZsrl-Rb7sNNALHJEc77doKdvdfKozRDb64Ln4nxuggAJXWxUS2lksRROgyiDILLy1tBH4f0Wz3E9mYJb82j4sLd47bRViaoXhGhzG1Owo_oDzqJo-Q2vPHkMKDLn6_cEnUYE31zG7VjtENOX9NM8zcZFm2RsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092268a67d.mp4?token=vztEtPrDdaipurfaIT2Hzyh0v2InOgNJHcGNH9qVlpsI_B5EEU0Yhnne4_wK4IaFPjVKcMUQx3KNFH2L6ULTfzUd2jPQddZvvvL-h0Dpjjj-ErY7DoGvbQX6usb5JB1rIXUlWIMyf6mpMrETlw-Cu_rCirGoFVNH3c0iH0-oW7eLsMXsXxd2SoVrCnlRaZHO6MnfL4doGeGYQ8-EB8viQ8P1_rhh6cJOkZldYcsK9lFKnzsAVuaxE594-Twy9UYQHmlc7kfDrnBKJ22xrhpoxQz9syHcrpyGEm9HzD4-LcpOI0QaaoRx-bYFkJt0a3j20moki1z0XcSHzQSjua6m5grOFQ1zi9md8deJf5yXqBSYeAEClYtqcLXtVHooGK_72BZrOFu-UTLwACtY0V8uynq4NDpsYnYo5vHOCiHQ7urcsvw2zR8HkxgYBlTfVBsESvi0NbfQVo6W9NQe24fbf5kehr4p8qzE6cAHguOt5hjTnQuEee1HYUGqouOTzLYNxRfvIxCVDtZ0kZsrl-Rb7sNNALHJEc77doKdvdfKozRDb64Ln4nxuggAJXWxUS2lksRROgyiDILLy1tBH4f0Wz3E9mYJb82j4sLd47bRViaoXhGhzG1Owo_oDzqJo-Q2vPHkMKDLn6_cEnUYE31zG7VjtENOX9NM8zcZFm2RsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : چند فروند جنگنده اف-۲۲ رپتور طی ۳۰ دقیقه گذشته از پایگاه نیروی هوایی لنگلی به پرواز درآمده‌اند.علاوه بر این، سه فروند هواپیمای سوخت‌رسان KC-46A نیروی هوایی آمریکا با نام عملیاتی CORONET نیز به پرواز درآمده‌اند که احتمالاً در حال پشتیبانی از انتقال جنگنده‌های رپتور به خاورمیانه هستند:
GOLD21: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 17-46034)
GOLD22: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 16-46021)
GOLD31: هواپیمای سوخت‌رسان KC-46A (شماره ثبت 18-46051)
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24410" target="_blank">📅 16:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=mj3M2W96F9c22UP5b85LzzrMSRQvU5GVEEdYjI45-2rwcw3m0N0IKBcd9jK2c-EU3eY3k57nI97XD3CWdx0ZO9flu75cgTUagAhUXtrdp5WJ4MDaXRBH2uK_2S7yYnqbGC54awxH888hZipTwPgiwYQbjoDr22G9_x2uKh3ZJ7HN5sYf5UeOgjPjZ9pSUyqPxPBNvKJ0oZBGCrh9IvdqxwA3M3C121CI7FQmXwy9FzjR0radX6fYT7KTXuePawRwi-Gxh5_PPVtKkA2NUm5sSWy_qtnawnsld9aA2jOjJ33InQ0tnla1F_K7QgRJaEv5f1uKxASH-1z-9aBxclqunw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efe2963dc.mp4?token=mj3M2W96F9c22UP5b85LzzrMSRQvU5GVEEdYjI45-2rwcw3m0N0IKBcd9jK2c-EU3eY3k57nI97XD3CWdx0ZO9flu75cgTUagAhUXtrdp5WJ4MDaXRBH2uK_2S7yYnqbGC54awxH888hZipTwPgiwYQbjoDr22G9_x2uKh3ZJ7HN5sYf5UeOgjPjZ9pSUyqPxPBNvKJ0oZBGCrh9IvdqxwA3M3C121CI7FQmXwy9FzjR0radX6fYT7KTXuePawRwi-Gxh5_PPVtKkA2NUm5sSWy_qtnawnsld9aA2jOjJ33InQ0tnla1F_K7QgRJaEv5f1uKxASH-1z-9aBxclqunw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراضات به گرانی دانشگاه علامه طباطبایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24407" target="_blank">📅 16:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv_n5pnAL2WxeZONX5HrgcMCXMqCCwWm6_nLyV4ItfOXGwdW_hS8BZ10BIGGqcqbH-00RXQkC8yT0AVG89FMqNzX3bX2sKI_GOncp7e6xJWzq5BhxL4xIuYp2RTQiBPe21960XcHDYsrHU57hGLHIZ39pgSt0vDiC8mzCj3WsYmUNm8pMvuU-j28xyRSY0HV_hEFleX6GAS3K0-oDYb9aH6LXjdx5LzDQnAO1Pa8JHwpoV7eUoAZlBhMCC4TVrI1h5wGOs36TfNQmFUpPqu01Jvp16ULoJ-2ylVWRCMvJEh5ws7m6X4SOCjO0gSQczaVLHJAqWJTXJ6HN38zWAT22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
تتر ۲۴۵،۰۰۰ تومان ( رکورد تاریخی )
دلار کف بازار ۲۵۵،۰۰۰ تومان ( رکورد تاریخی )
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24406" target="_blank">📅 15:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9k_n-rkEWrB1UonAAql7r7Cmef2jzvKXPTgbJ6j44sLcLupmW2FKe1y6hjhRABbzFkD7t-JIXGpCYLnnxgf9mDdJeMCFSavEx_DlajAARNhvh7nRyuTfq4sI8yCngxX77IUqNOTKkzWRldFfxgpKF1cEYbK86c4K-e1t-b_OqlDHwYsVGNKfXodfBcZAigU7BwU4hwhC8hHnDpgLxHMf6xjXCjZlFfFkQTW_E8WGw1JReIJEAuvW9xAJLNHMZXHM85MmeRxGZKlgx_S8wehU59PZgv_SE1FccQysKd_lGVYn3nmDwCPSEe2OOwDRjxK7wXKozYdIJ7oKub02T2DiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب سنتکام:
ادعا رژیم :
یک فرمانده ارشد سپاه پاسداران امروز گفته است ایران از طریق «نیروی دریایی» خود
کنترل کامل تنگه هرمز
را در اختیار دارد. این ادعا
نادرست
است.
واقعیت:
ایران نیروی دریایی ندارد، زیرا
نیروهای آمریکایی آن را غرق کردند.
ایران همچنین کنترل تنگه هرمز را در اختیار ندارد؛ همان‌طور که
هزاران کشتی آزادانه از این تنگه عبور کرده‌اند
و تنها طی چند ماه گذشته،
بیش از یک میلیارد بشکه نفت
از این مسیر عبور کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24405" target="_blank">📅 15:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEQ3</strong></div>
<div class="tg-text">یاشار بندر عباس طرف پارک شهدا صدای دو تا انفجار اومد با فاصله 3 دقیقه از هم</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24404" target="_blank">📅 15:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش صدای انفجار بندر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24403" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترکیه تودی :
پروازهای باقی‌مانده شرکت‌های هواپیمایی ایران به ترکیه نیز ممکن است
از اوایل اکتبر ۲۰۲۶ / اواسط مهر ۱۴۰۵ متوقف شود
. این رسانه به نقل از
دو منبع مطلع
گزارش داده که به‌دلیل تشدید تحریم‌های آمریکا علیه صنعت هوانوردی ایران، انتظار می‌رود تمام پروازهای شرکت‌های ایرانی به ترکیه لغو شوند. یک منبع نزدیک به صنعت هوانوردی ایران نیز این موضوع را تأیید کرده است. با این حال،
مقامات ترکیه هنوز چنین تصمیمی را رسماً اعلام نکرده‌اند
و یک منبع دیگر نیز نتوانسته این خبر را تأیید کند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24402" target="_blank">📅 14:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24401">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اینوستینگ :
بیت‌کوین امروز تا حدود
۸۳ هزار دلار
عقب‌نشینی کرد و حدود ۱.۷ درصد کاهش داشت. افزایش بازده اوراق خزانه آمریکا و نبود پیشرفت محسوس در مذاکرات ایران و آمریکا، اشتهای سرمایه‌گذاران برای دارایی‌های پرریسک را کاهش داده است. اتریوم نیز حدود ۲ درصد افت کرد و آلت‌کوین‌ها عمدتاً در مسیر نزولی قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24401" target="_blank">📅 14:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24400">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رویترز:
طلا امروز حدود
۳ درصد سقوط کرد و به پایین‌ترین سطح بیش از هفت هفته اخیر رسید
؛ علت اصلی، افزایش قیمت نفت و بالا رفتن انتظارات برای افزایش نرخ بهره عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24400" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اورشلیم پست:
منابع حوثی مدعی شده‌اند حملات عربستان به مناطقی در تعز تلفات سنگینی برجای گذاشته و حوثی‌ها تهدید کرده‌اند در واکنش،
پل‌های داخل عربستان
را هدف قرار دهند. اصل حمله و میزان تلفات هنوز از سوی منابع مستقل تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24399" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مقوا ای آی : انقلاب اسلامی
سلطه و وابستگی ایران به قدرت‌های خارجی را پایان داد
و ایران را به کشوری مستقل تبدیل کرد. او سیدحسن نصرالله را شخصیتی کم‌نظیر دانست و گفت
پرچم او اکنون در دستان شیخ نعیم قاسم
است. وی مخالفان مقاومت لبنان را به
بی‌تدبیری و حتی خیانت
متهم کرد. خامنه‌ای ایران را
قدرت اول جهان بر اساس «محاسبات الهی»
خواند و مدعی شد دشمنان ایران پس از ضربات رزمندگان، دیگر حتی از
دریای عرب جلوتر نمی‌آیند و به‌زودی از این منطقه نیز خارج خواهند شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24398" target="_blank">📅 14:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرگزاری
NBC:
در جزئیات تازه‌ای که امروز منتشر شده، اعلام شد در
۲۳ شهریور ۱۴۰۵ (۱۴ سپتامبر ۲۰۲۶)
، یک موشک کروز ضدکشتی ایران در
تنگه هرمز
به یک شناور حامل نیروهای آمریکایی اصابت کرده و
۸ تفنگدار دریایی آمریکا
زخمی شده‌اند. به گفته سه مقام آمریکایی، هر ۸ نفر دچار
آسیب ناشی از استنشاق دود
شده‌اند و برخی نیز علائم
ضربه مغزی و احتمال آسیب ناشی از موج انفجار
داشته‌اند. این افراد شامل ۷ سرباز و یک افسر از نیروهای تفنگدار دریایی بودند. هیچ‌یک از مجروحان وضعیت وخیمی نداشتند و هر ۸ نفر پس از مدت کوتاهی به خدمت بازگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24397" target="_blank">📅 14:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وحیدی :  اشتراک چت جی‌پی‌تی مون رو تمدید کردیم ، یه پیغام از مقوا براتون میزارم تا ساعاتی دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24396" target="_blank">📅 13:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دلار ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
تتر ۲۴۴،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24395" target="_blank">📅 13:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24393">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">در فرودگاه بین‌المللی مهرآباد تهران طی ساعات گذشته، یک فروند هواپیمای C-130 هرکولس متعلق به نیروی هوایی ارتش جمهوری اسلامی و یک فروند هواپیمای ایلیوشین-۷۶ (Il-76) متعلق به نیروی هوایی ارتش یا نیروی هوافضای سپاه پاسداران در این فرودگاه به زمین نشسته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24393" target="_blank">📅 13:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رئیس سازمان هواپیمایی کشوری با اشاره به تلاش‌های مستمر این سازمان برای احیای مسیرهای پروازی، از رایزنی با وزارت امور خارجه و ثبت شکایت رسمی نزد سازمان بین‌المللی هوانوردی غیرنظامی (ایکائو) در واکنش به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی ایران خبر داد.
@WarRoom
یاشار : بدجور دارن تو باتلاق دستو پا میزنند ولی هی میرن پایین تر</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24392" target="_blank">📅 13:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نرخ دلار ۲۴۱،۰۰۰ تومان (رکورد تاریخی)  تتر  ۲۴۰،۰۰۰ تومان(رکورد تاریخی)  بیتکوین ۸۳،۱۵۸ $ انس جهانی طلا ۴،۱۶۳ $ نفت برنت ۹۸،۷۳$ @WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24391" target="_blank">📅 12:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43823eee78.mp4?token=uVLm9sNL-FYR0wfag1Kqx8YHElJH40i7gbv7oD6n0ydgqww8wPf2GvfliU0fbx1HQ1zJxLzLgPueiUNqaQO827sFJQ2ArcGhB_N-kaJmwTNZ-l1z5TdC-um-DJP7mWWNwkDCCGrwu1F5hNlhIfnyL5ewp7YTNR18RPg_lfWo0OKvtdEPpvLtjp-P_bDGvbnmtN0srunf8RXiHrg5Fc9Oee3VMOzK2WdyKWvTJWpdSeNWnAXBdXOHWwzqsKaeZheCRONAOD33ulAZHkMZN5PkIYjTBQ5hVU2lfrtIvcm7fxO2_8XwzEeRRJadhnxFVvtJ4OOdpjzYESdSsN30XxhRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43823eee78.mp4?token=uVLm9sNL-FYR0wfag1Kqx8YHElJH40i7gbv7oD6n0ydgqww8wPf2GvfliU0fbx1HQ1zJxLzLgPueiUNqaQO827sFJQ2ArcGhB_N-kaJmwTNZ-l1z5TdC-um-DJP7mWWNwkDCCGrwu1F5hNlhIfnyL5ewp7YTNR18RPg_lfWo0OKvtdEPpvLtjp-P_bDGvbnmtN0srunf8RXiHrg5Fc9Oee3VMOzK2WdyKWvTJWpdSeNWnAXBdXOHWwzqsKaeZheCRONAOD33ulAZHkMZN5PkIYjTBQ5hVU2lfrtIvcm7fxO2_8XwzEeRRJadhnxFVvtJ4OOdpjzYESdSsN30XxhRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏دیوید پردو، سفیر ایالات متحده در چین: شی جین پینگ در ماه مه موافقت کرد و در اینجا نیز آن را تکرار کرد که آنها از عدم وجود سلاح هسته‌ای در ایران حمایت می‌کنند، این بسیار مهم است
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24390" target="_blank">📅 12:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دریادار سیاری، از فرماندهان ارشد ارتش: «غرب تنگه هرمز و خلیج فارس تحت کنترل کامل نیروی دریایی سپاه پاسداران قرار دارد. در شرق تنگه نیز کنترل کامل در اختیار نیروی دریایی ارتش ایران است.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24389" target="_blank">📅 12:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رسانه های رژیم : بیژن مرتضوی به ایران بازگشت
@WarRoom
تکذیب کرد</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24388" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
