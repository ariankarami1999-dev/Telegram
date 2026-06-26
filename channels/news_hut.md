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
<img src="https://cdn4.telesco.pe/file/U3MfJiXJ6lyJ-mSvlAvGo1gTMsKafdfL3tuwCJ7tC-VfMv-0FYjL9mKoUssHD-f-3MuCsn4NpqaVjPueQshbAEk-Yusl9nt3V1fZxUk829e79LlE4n9rLyRtSnVuqkfg5B-5pb3ckDpVHxZmY5xCSHlGHB3qp3MgU_vpLuIH78fEt0GsJOM1dLOTvwo6rgI4MEf4q6bnBbNDbCahq61vvAsRUmTal4jdluFOZOCsMB1q4Q1WXcxMNOgdE9rartWPTf_Lctklo_p1EPwC_SVl4XD1dXmR50zZPLWLzcp4x5K6NDr1tHdY62clUBFrIq-87QNByfkggNtxY3YwQGhhyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 00:32:49</div>
<hr>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkiGCAYrMkEcIiEKerwXI8yjSyj2J_fmpcZhuFpg18dKLC8aRWNPupQyzQBC94UtZ0i-FT4WLgPW_ikcb2awnNCecJHV8fRKP3e36VNEcFmrli29iVY7CFsQ5s32ulgiJ9nEO71uQRh_GWAcWkVzIbseopNmFHlJf4Lygu_xGxoqMj3FELFHzeoVdFDezSNew66jdm8Ub0-0TpMG1VtIyenIfdXXl1BVSUI4QVPX9UMkvq5giNL-xhXNbzk_SPZeOQvXddNfajOkmVxY35CMnoVvOq2NKAQXyqS7MzJ4FJxsFh0lGPQ9Pgd3nLewM8mpDdggUk7vFLYR78Zn9vD8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=vwVEsuMDWl_TBj2XDd5a1luIc2BlpDxic1z206h5DEucN9kgK3XqenJAEAZUpcKOkq4yZRcpyGriIAxZGLjOQzSIhtqoZBn7GMEIUN0w_wJfQrlYlPHwzZBLJ0wZdeQB_34lAyYEjZhWmzEA6UNvdpLDHJOq5x-0lvzmlPU1IRET4eGeA8-E-gYgVSVBwnvPBNxs6lGT2ef7V2av-Z9bohovNJ79wbcPFU831wf15baGRSoq0tIT7f1C71xKOlUIQiJX-inZcMkFxTQjAwV3xiafXtvIxKXfnnSZW81xy1WhGBnfQsth0bTH4OOiST_IUaVYPwoqBy0OmI_72mYkTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=vwVEsuMDWl_TBj2XDd5a1luIc2BlpDxic1z206h5DEucN9kgK3XqenJAEAZUpcKOkq4yZRcpyGriIAxZGLjOQzSIhtqoZBn7GMEIUN0w_wJfQrlYlPHwzZBLJ0wZdeQB_34lAyYEjZhWmzEA6UNvdpLDHJOq5x-0lvzmlPU1IRET4eGeA8-E-gYgVSVBwnvPBNxs6lGT2ef7V2av-Z9bohovNJ79wbcPFU831wf15baGRSoq0tIT7f1C71xKOlUIQiJX-inZcMkFxTQjAwV3xiafXtvIxKXfnnSZW81xy1WhGBnfQsth0bTH4OOiST_IUaVYPwoqBy0OmI_72mYkTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=DaEZlypaPVr5zaVOzbZ_Cw8CB7pe38pICsGHou1xVTRm4IHagHLNhMH5Zh0_v4x010uEEEKCbGDAHKpwBG0MVCdL6U5_qOB5Gyk4J3Ke8979r25sFnzhlAbR9j8cifEaLkwkJHAUQKAglOp_d8Ya0WVEwHkry_eZ48t-l9G2EebTiv-5WfkZp3EtniUkueZ6OYdz85FWSEj-5sHq9cuVyC417OoHeFfbmYF6QLdVW9nUzX3MzXSX4XgNfWyYIOSr3RAcD18UHHmG94Qmwa78vl0kuo8r_J01gEKbxixu3Pg1P8dq4dwdI8MI5-T5-LrcxvlxFZRp1vNztBINiAl3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=DaEZlypaPVr5zaVOzbZ_Cw8CB7pe38pICsGHou1xVTRm4IHagHLNhMH5Zh0_v4x010uEEEKCbGDAHKpwBG0MVCdL6U5_qOB5Gyk4J3Ke8979r25sFnzhlAbR9j8cifEaLkwkJHAUQKAglOp_d8Ya0WVEwHkry_eZ48t-l9G2EebTiv-5WfkZp3EtniUkueZ6OYdz85FWSEj-5sHq9cuVyC417OoHeFfbmYF6QLdVW9nUzX3MzXSX4XgNfWyYIOSr3RAcD18UHHmG94Qmwa78vl0kuo8r_J01gEKbxixu3Pg1P8dq4dwdI8MI5-T5-LrcxvlxFZRp1vNztBINiAl3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-Uc-UD93Eyf8x3S8Yzj46Ohk46_61VT2VLQF2oVCw6RsDtPRYqhBxeg6pbpx_e9hjb0ps_Zts8OCL2UZwt-x1xcZ3zZNfiz7MPqIGCjONmBi_Qq_n5dWvST8NM3yzxH0S7ReD9R2CU_oAihZQVm6gwxgyzsdd14vuqnIRouuWkGwUX23ZGcXsKbdH9SopxbI3GiAWPUaKwJ4hWeiV1K5ChhRehnsTzFTpL5ryLQdMRgpGoEXaOdbACqoM3kxs_HwYpO3cHSGJWmAo8UCXDekWDCsgjSJq_wOQ_ZjX3kjomusAF9SeIJVfF5UrL-pbsKo-8l88DMjHBNLrFFIN8Fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=UbhHhM8lYtnHNbCzwKzK6uCsxDhHb7NVeC4Yeuq7zoDWCUMLuBYr9N7r_EkrNKKAQJWZ5F_zYYl4KeWxRFf6muYo-pIz0e8tU_rhBF42OV5bXQKCqx6J2FCfzkob55jZn5VZu-OrxzTuv9EJdhSW3_Ny0LaMwHW5ae_mGw-VDioW9RMPVryc8Ytnobq-l1C6T4Aid5uZR-KKsqBp8ZsKk2LQtBJohDxhltXLQ2bFOuaqk72KGVshpXxFKtAZBN2mEwfeK7NGdA8NUoSl-nP7oFQgB1s30yf4ViodKfHHKw0PQjdfXKIEfewy2sf9udKzXXeFIiKumN07jcsesZVt9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=UbhHhM8lYtnHNbCzwKzK6uCsxDhHb7NVeC4Yeuq7zoDWCUMLuBYr9N7r_EkrNKKAQJWZ5F_zYYl4KeWxRFf6muYo-pIz0e8tU_rhBF42OV5bXQKCqx6J2FCfzkob55jZn5VZu-OrxzTuv9EJdhSW3_Ny0LaMwHW5ae_mGw-VDioW9RMPVryc8Ytnobq-l1C6T4Aid5uZR-KKsqBp8ZsKk2LQtBJohDxhltXLQ2bFOuaqk72KGVshpXxFKtAZBN2mEwfeK7NGdA8NUoSl-nP7oFQgB1s30yf4ViodKfHHKw0PQjdfXKIEfewy2sf9udKzXXeFIiKumN07jcsesZVt9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU1RBzQTBUbidDg2yMXAf_nMJck74b_xjwLmAP8MihLGmDwuJfXa7DeC9FybPRzttvU_7STN7_lKrj5HfP5B2ut2PHL2fi47qQL9Bq8BmqLSB8MX0LQZt1rqCYjh6dEbbyKkYBPbKBbRqbAOCKGOsF4XrMNi4JdXW76mTM3PNUM20VWI6MgNsgI_lhFyPLnkDdTCDYSMk7iQZijCKA0Zd8cIMzK2fQya-iEAg4Qu9u3cxZ3xQD38i6Suci1_7nKVMA3ix9wnB0JeZ_me7-5dmEqKulYDu493hkjAKheWG6tbEYm8XU0c87XXrQb6qz43Wf2_xhuzHYx1wPjFpNIQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=q0Y2mkVuajJXQLghNY-3QjU5zTJRomKrXiR4hAJ54I3XXZPFv-VsMN_bOLyIXaB3js1hk-5ORxJwXcw-0xl7g7TYVFb64IXEA2EDE6QpBPZV8-dLTJVwZDZXFZ8xeofJgvzCUtPp-nB5agbl1os7YSn0WFIG1YsmTmKvJFDN6-4vO4VPUk_fH1UwUlJ5rTAB97sDssuEpTrzEgrBU0RyUv3xmNISgrkxNF78vFz_pfXkXh3uZRatWizx4cq_5EOzcshXmlEA5e1rHIjY9B_TqMPamkYcHIF6Lqth9HCJL1GarLEpDkpw005kdXHUUTh3eVi_X6GLUtDythEaYhnaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMbU3vzuDXvf5urw_4PfR-LOW4cQqHFWwCuZF9DCCxbpU9uFC-19MFjn7lTK8XXK0-UtHaxdXD-4XfLc79o_aQQkIaL-UyyTJefeWXqmxD1EyK56G6tZGJkPfKRHkIetetVbrmRv2DfMLKaPZVtJoDcr0tjIa1iA85bYscSauDcZ_gVIQ_0CcVIJkVuwnJmdcdPa00Nt_chS2CVYX-yFnATzbgGgRbWS35QlpoO1-szE8V8NkmIbyT4maIlveTtn-DySgNj7Lcbzjr80znWwNpFN6rZ7Z9rnZ8cuziX3y2nHkmIzm1pg8APYAT1ND673c8qBUYURMUMQAcY4gr6ChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LG-5sqZX1xQBmZW5c3NWWez7I749Bp0nnvfe30Prm4GleJehkcM6oPeUHhoLeM27sHa4g9pNOrDKt4CyjG0Ft5SvdJcnpUKSWQtgb63mcEDYGnrsd6RjFvY2U8iIK3SUTD-BQELaY4-cHq8wnvoRCZ9etkYCTF0eDnEy-kRIowWOWav_UkeJNCfU7Sm5PN6GYAvjSV4sUfLC6Zx1lBhpsiEml_gyIk8QFddUOKIyzbXMVz4AF4XL048NSe3MueZbL5zVBM2keDLXhO-jybmwJrEZ86eoGcG5S23zLeTt0UpxqnVJ0jRKgtgSxfJlaSaI7ESe5hV6T6lj0EfSa8TeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsHKqb_La8m_yyO26AyQT6qASjMDPTr8_5eT-qtWr5WpFsdyE87azjqgXTAyZwsHgjpP4jIzN1SHCFCEvs1LUU2hpmZ5Wf18j03q-Y-MFtjl8n4cCyZ-CStrGXZs-Epacj7bd6eQpr0ar8-7023tYYx5S6TbacozT0jn2_uF5pOvw7Mj6_3KEl5KLQhwVOqKVOBusi2rkEND4gGbF8Qrko8RNZPVclWolU0BNkiCst9sxoP5BT0177BsivmWF8ThHlTc81Px6yxMCaqqsM70gjbww8o_Fb4wv1NZV62tsIjTwklc31zH3SVFSCiD88l9qij8S3gNVm9XkCy8RWtUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FC5ZRQdOHVYFW6-raQ7qbkHYmgLrtVsDhur_vZGBjpii03a74u84a7BDTwyST3nLpqBEanB-AhUmMOj8AG6OXw58UttWDLsm3sDErD_l57t0SkOAlHXj8mk3XiTeLTaM18ZGSqfYLlde6yBDZVCdZ7F-QBJ3UwXk8a8d2gNZQltqHPy_EJ_3O20IG62TfX7HEtdr1AKMz90l5DyIqMSveEbhaQ6-UxYCb-iq5mm3f-3djA6x0BR4SvTmx81Xer5ElWwH3nApZijhVhTHc9enQVKSvGJ0plXHYghFf-qmUo_b6BRkLsF8CSvgQxUouKpAIvp7FtIvlBRJMeSvU3faiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jisNc-GuII3jgAhWpUFfEh8_DkmhJpAbVbNipvktTQPIMAGqKrsWTuoQpMX5cpxdAtQHguCkHWDcBXeZ3PdY9xI1DsafwKSvpzUBCNnAMP7kk4t6fHFBuw47VPVOw9D0ezIawTbIzlwT0vFBHBBKHxYLjS0uGDxp-l--z5zNuP9-U4-bIBg7WMX0f6mUvNNsH6pPCH5XCIEkUuqQGo-fHNDzsaEUnY3gnb8-86aAuMjhPPNjUkR6TGZT5qR4QIHo7ADouJUDoyG5eBn9G6jxFPqFzfN-CBYPXXsqScvd8kifQe5lgZVOzA2SCrIBVx8G1Z9bF0j1Bxxvbaj_d8ca9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1yqSKDWR0Bv6ahAGlnWbRraAdHbTvkN_2842ibZPmSPE-06xgLfhpSxPY8hLHSFYnQYbzIxONNs5dsTmIrQ5esuEwNVycaLKgouKI9A6IpmNEPFzCLe2MW1XnVYY69kceI3B0I6aWNbNHS5tXnDRTQfFEBPHUYudvbqderK7WaRE0kkPrBSXQbid4MyTZihOwaK6SnnVxmvQmK-PY2hVEQ621bJ4CJwcDfqEr8d9SiqzXTcI20JgfqMSS7i885qe0DHyEfN8OM3dwtyBARgxWWHEpvJ67F1W57__8LKNi7Eb3CdvF58MN0cx2LVI1RIKzqOoS8PS2ODKoy4GWcX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYBRVtc_ofzWPFR4BTiR-rJwZcjIuU-eBXaVTO5I1cFhFZM49PNXO0UG9izG2sZpLZaQCOaZSNiXF4LB7NzOSW7DIG130sq_DPELtbsRyy_pQBnlkC7GESPJcBGwog0S0vJG5jvC8pwo-SAxaWsFGvAbvmc0ebJ3HGWjDAuw_gFUI072PTqNPArs0Q1ISRkkjasZhJEtpci9XebvHM858yMkatiqSpzafWbNZ5TIcSTln-o3uxa79mN935l80WF6wxj27giVqJO61FGtvHkeM7DXGgH3rE7IhjeL1Pz1cvYfgVtsdt9H6UIJXUg243q4e9yUHBal00NRUr7pMtEdxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=qWd6rbHpA3Le4b9EHhBeSoJ1TAC9XTTczaAqSAI389W9YGwsR91vYig3uL4Sl3zySKlkuORY_QPOCfO7G8Zr0cYZwiWaLhX0a3YKop9pNUjZKEhQmCPnEszw3UoRLBRfe5XYJ9bPEyXU-uRS81tDet24k6lQEyhVo7rax7ZVlR-6EtItHk79uw9j2FyWrNFtSIpxKQNF34dBZweLo-Wjcv46_6M0yyVRUcohs1hIcFcUl0iwbLcioze-OnyjCg21MXIoIQ_hsitSbpB18EyEgbmiEaQ1rJzESdwLE3NxrHBYB5ggjw8pULAnAGsXbAl1dxg-1ClH-vsQUzPRipgyPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU1OWhfM8N0SaZAh-Y5yeieVZjEdV3q65BCJIFksxXudlwziIFfTtAtfTRCh4c7U3BiXrPUYr8sfnuBNBaq2T5OeMeqDSLXM0vTbbshy93x_IKDiPJHfGFVMrxfOv2CnKJZYcd8S5aI3WbnBy1wjdC2XhuLO2WWwEjDz1qJ2IybUjrZNX7VZ6YjRc5Ae0TpRUxg5Yn7YV4EymSVg-se2SXlM9I5ymBW2w0bmmgxQ9iUZtJHD54VxXYOpljofOI04_BVoannKeyHgqtdBAJ9hMkzXjtjnOL91nhgV3sdx-Yfq2CU-nE7qR17k0Rk46slMBD7r9EQGZ3tRV2NR3nsofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=CWIGrBnjgfKVpN8dm7e7jfnNgTP9MsuZh80R-B7582cc0sQ9u1UD3A0eEDEBBpiyQeyYbyG4IK4A4hVrmJB00A3peASuDuRVc5xpitSllP8SqBedv_VNaZooMsW_E6mpCTymdMhL8LYKX_FJQFFJ2X6BZstaGXPgtzp_Dp2WxBb7YVus-uKNsZMxfxS7zulp0yxL8JSVxWbF7SJxwEGYNbe4HOsX2OOMgRCLRBlx8JF_rjOTvs2yHPdFNwT8e_ZzCLE3GZeImVuiNTyc4ORpob6ViZOK-uJyvz70Qe48T_Vla2ZlqfWRq7Mwl5s8ky9mNL3GrObu7gbvQQa8TAvwVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5BhspcJvWsUHX1l_ZSYx4BLbOVS6NIKr1ZiUlW-0WrO697-hC_lJ-kpoKxfLSTVwjNOb0ik0kv_Ww3wN34HHUpC-OQ4KchX8LX8UzRbc-22AiW6Bh0BpXI1c0d25PVLjd8ObxX5aZoFyHsQc9aog595GIsCCEdzn7dGlbKrPxgI0L-6DS5AK8qI8X7RXR1-RGPHT5obwGalHPNNN-noqKQ5EvRTnFIhPxAgqR0PrTdjwXVcXht2R5JK-simj_R_EDkVafF6GOYIjgAyeBOIKkNG7jAdJynwVR4dH9tGMo_sWQLxWw6DQfwx__NyknA5UnevSAj0A4mU_MINzdII7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3zO2oKfXJ-fEiVMpWDXugkY72dmBbcNReNvbG79Y4uyc6RMPDeUviPVQaFJQBfa9hmfL52Hj7ea_vbMs6ozTzO_dzfdzci5UR1fWJK4ETDvvJ0npnusiZ1L0PjrZpidZH92rKkebdgpuK98N1OJujIvo1rCEROUSxEFFdIXuDoNMgJOYI3uNWuKSC1Fes1l56Di7W-aZSeOLM-6D_1FrqgISi_0lZpMBgFJnNB8rB0PmNsPXlHw0yQz7YsjWMSLgTRZc3hMzcTNIYeicskdwXP8mP3L5eVD1mNlWgE1IOUN4AMygwkCZQzgSI004U5iUuYNrh90QFeXDBd9GdrPug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=SkKEvnqzppPGYocJopTE1efTmVJfAR_OOx0ZhgKXPOlr3nFhuQ3MBOHaPKnNdz9KVKy4QiKD_KJEwfwQ4p9QzdsAgwK1slcp5Fpu8_UlTb2Mf6_a068uqGudflNOir9hBdZm5acb5G7EKEL0hmUcEeNNgQi91zjJ1EPKEgDhV_SuU6Ty7Ih5g8t3rbDpipIZef1WrxE8Rw5gS93MUqkxDvK8E4Fm02L_-Gn80ZDW-c5JZ4AOXFkD45GhgBgGdI31HrbS30QVtXwYkD28MiGJ13W5w0728_H9WKEuRWzEk9_tVLEWJ2XmunjYtSeAXU3m7jIYEscdBBtWP755SvqaGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=SkKEvnqzppPGYocJopTE1efTmVJfAR_OOx0ZhgKXPOlr3nFhuQ3MBOHaPKnNdz9KVKy4QiKD_KJEwfwQ4p9QzdsAgwK1slcp5Fpu8_UlTb2Mf6_a068uqGudflNOir9hBdZm5acb5G7EKEL0hmUcEeNNgQi91zjJ1EPKEgDhV_SuU6Ty7Ih5g8t3rbDpipIZef1WrxE8Rw5gS93MUqkxDvK8E4Fm02L_-Gn80ZDW-c5JZ4AOXFkD45GhgBgGdI31HrbS30QVtXwYkD28MiGJ13W5w0728_H9WKEuRWzEk9_tVLEWJ2XmunjYtSeAXU3m7jIYEscdBBtWP755SvqaGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=Bno6dqFGbg5gGeG4E7PFD8BoIrQv_vhe_Cypp27SuEy9fEMJQhYuNmX10aRBHeKbN0Zs6Url_YSId55ruIKJCbeaiiydlY3HnT8lKeGQDIJh829ex6khDsWNxEaBp2ebA9ggwNzraHNLpPGEpdXOP8juueW51lV2GEI5NZRNhI6cXmJldmC2m4FDFhd4qx_xU63BdDvmkVP4Sktew7-JW5EUvXwGLokHRyefUiUYx31HDACdA1vD8Gw0WvZaeSNJuKjZEqG_MIGwfPRUWc8Q02kQOD7aj7sTMji5zpKPME6Qm5ZvuXEEJHtvbjCjuToeah_tnPvPqN4Wb-wJ1chpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=HmhlsvLs2aoaWWWlO_Bjy4uwWJE0N_9B2zpI0GlEO4awMfhyzwkE_WfjrfDvmc7yC3Tbmblb5xY9ZvvCLceNHreOe1n9p0yj240QWMUjpjQal0gGry0fCsMLHjCEy_VIp3Jt00IPq_CpBq4nQpu0kaRFBvLnH2uP4VtwTGGlKex-HDg6bysO57oj0W44j1zAqDRn_KKES-_VbJtNpKmzUizJggZfh2DNp2HN2fJcGIt5BX9Zgg-ItoI0JHAjk1J21ewIPxCTJbQywlueTeCzGuZUr5Gh0a1LT0Nj3cVC7MH3Kn_64wQHjC3EvxDrkrs82jB5qEqmCXE4LzFAocO0M3vwAMWhhoU7cMTb3rLXDCjujP9JRo4cNJvg1cgjUfoznE9VT6L8aMZstB6D25HkF8Q1GidzAcBKVCmGsolxazQ3iLdz5umakFZ2PgRtOtjQwcSFExaqnO4HJ8DZBwER34ohif9WDnDW5tisv_8oghDKCSU_EQ7Yv4la9o6ehbakaLnE_G38xCMTFBvFeFKs9djaI5_0Lhm1XW4PN2iIBOEW5461H4n0_R5aJRv9Kd5dFu8ujN9hTCHLyNfNSrqzfblG4_z48j9PDW0OlTVGu4fWMxL-tTY92Fgb3334oevBUF68QXXBqxvXbH_hJaHKlmF6M6udzaX3jrARA7y9JRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzAlNAuqqwSgXqo8NvmErGWn7enByHW8GRYhiXiKN-CS_a7OpbXtNvNyWBELH_und9x2t9cokX2yvYW7Yvkem9F2vconDE--oCR3eWK6u8CfR2AkJVXmmZGvL2910oOL-bQO0WEhjFP_KqDxrygyUN6KwWDDsdYcBO2LDWFXM33Aurf1u7vuvnVtWfADO1if9bj4GyKRatj3e87rxpFyk9UIQZJKONf4A3THfNahMwuCuQHCLck3lmPVyKjHceAcGjzCxAD8d3GpX7krns8nKSJhA6jH7ltD3PqVi0imRp4QDYbfYuKoUw3mMm8T5pC2CEgVGT1Qlib04rvIJwEe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K3fXCXlqSWhH1d0hwhiYuvSUvmEVOQuYRcwm3FV-cH5wfgW6Ky4f01aEDl6X_yFoLtk2t57Ho_09T_rSz-mIxbwZYAocp5fUFlth1zELr0EMptBJ8EU4Kvj4s5j_H6-OYq1msV91nOLo75aIAcg0SfXggnxWlnX0BDobYxz-JQRdNSau8raZzI21ALnCIKeg3uPn314KLUo2lPZigRGpdU-r57kSY39Y_iIKkXg3-RFro9iXgjF8fyDGm4O4hYBOdrY40k3GIrQKxcodBz4YS7CA-Emv2DbOGthfBi-WdhelhlviiA65sYnYLbf9LZMFOXVgvbuevoa_dHFc46za5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=DcwtL8FSBd5SOddOrh65SX8J6WkuLCsnkcHGwHQdGQAkaf2HtlTnB1aMEDXDi7vEJBeMVfk2H9gIhVqhWKTNrMEGCk5Ctl5AU0ew5EjzwGANZCbLi8zIvMZuCG0Pk9j-wtYUYRHwLRvHcMdPsKJxT9i7om-XiyIz6Dk8zzl79Kxn_WGyFNwQmLCvZlLxMhpZnrlJZV6-vDVgI5htUFra5XmBTULj-bt8IVbTeHISZTuSMFb2Tle5_Ri32trNB_02Obi5Ry5P_tc4DF_v73IRGx3-IWFXmmN7r3E_2VGxlPKAKkwr2oudq9RmPgJYYuzwdFlxYpX55Bd_Djf-segz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=DcwtL8FSBd5SOddOrh65SX8J6WkuLCsnkcHGwHQdGQAkaf2HtlTnB1aMEDXDi7vEJBeMVfk2H9gIhVqhWKTNrMEGCk5Ctl5AU0ew5EjzwGANZCbLi8zIvMZuCG0Pk9j-wtYUYRHwLRvHcMdPsKJxT9i7om-XiyIz6Dk8zzl79Kxn_WGyFNwQmLCvZlLxMhpZnrlJZV6-vDVgI5htUFra5XmBTULj-bt8IVbTeHISZTuSMFb2Tle5_Ri32trNB_02Obi5Ry5P_tc4DF_v73IRGx3-IWFXmmN7r3E_2VGxlPKAKkwr2oudq9RmPgJYYuzwdFlxYpX55Bd_Djf-segz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=pxiFAN8cwWtbMRTqhBvCcAfQZd_pzWsnMiVwHhZmcU_w1fq9EPKjULoaBGRoOaMePbH5QeF7XNQCU2P3BY2Mvg-Jeu2cf0ENPpJBDBzhZOi12ZCoROUG50k0aybB_xCxLLgP34aynjk4Y3_mRc36Qi9RgeI8Y2llLTprrCFyJjTv4Nz-oHpBNqIpMx5NPpOeSYIrC2gpCeTtvCI9bAiBr_BB_3QSMkozBwqLOnb__J35ZcYZuYuvqPegecvBfFv0780-h8f-tJu4nShuFN8tYxdQufbPLXYlBPR5lxQr9eAG4HjvGiRqIk_fVxvsaThoVthJXjCUntXR6_OoY6NcQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y73wSNy3qj0gtSE6ZcnalFuZl7sdV2H_jurV5ILpUF59Llfpih46m_x6qNTTzYLjaNqI3MMgDNcDgrHmZKhwPZ-1mA5_ZPTlh7AckrcaKpedGRD1Fsg_tE7Q1cGkZE30T5kqSQvALKe61WuJHMnbi3nUZawj7IWOXhq49Nl1PhgdXd9Ph4iaKLfTM8eoAEPpjXHBIsj9DqlYYgZmidZ0XwQBzF08BfwI0B80LmF80fHLQbMknaHyPWnhAHHxIQXKKdHdMB26q1uHsRF1YSwulW7dNR6MvsR36ERW_B6uTSb8p3iwKAFQ7VEIXgo8Q6pPT8SlaMgM4iP1Gpvi9K6KVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OlYKvXcpx9Utnvx0hq3ftMymGIWxO_v6KNic31lK-A2YvERf4M8WjXGH1CXRZw5xdBZObA5ZKsPeAeRNz7cQIHQSRYyvjU-Z9weld-LEOfHQbDEg0aA3_fsMplpJ_9RUEuKfsUNDPDh9_sZP6xgelN-EPAioyivNbKaq_SNiNfS0E0o3ZE07Vk9h4mdTBa2NrlsDeSDyYVQzFe1V64amlnVfX1rqDzF9emghd55rEs0CWJteaiyEbOiEEciEEF0gWOC7m4AjNd5uMS0yIRW-ygeX470nPR_JuMYpLY9cH8CNXycI4Vp-ehFrj1I3K1A1Ti9jPCkiUeimMEJ-8WsR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jqtWFRuh4BTN0Z-Wqr3pU-QPrUISnzI5PhA3AQH9NmeP9VbZTnJSEIfzw36tlS51FeJ8UQ-q230RFlkxnp7tIG6IhmYz0sJimycPlppZUqGs4c2-cChWIyNqIhWi0wnM93eC5eP9J5608kSYE0YZh1Gs7G-tHKoELJlxCMrY3L2N85odxLqzsC4eI2_aQ0fIHoq0He7EXAcVXNNvx7NR1i7QvKhuIBdU5B_StF7Ppu7Am9OT8EW67E8nOgjccUHyIcYJ0iOz4oeL-TQBaWlj1oalcsQQLndhbzsxwlgUHn_4PvQAUWt5bfc_E0GPls9Rwdl69ghsODDlPwEww5WHGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=ucCTgh3LVIJi1NMvytBy5nawrMKBQaUkhryqDAC01kPu859zo26u0SP4-LxAz3Ij7NI8DeK3u70DQAAoqzKe4ub5h3UhlrPxMXxLKNJtfW_HEpmdiQON8V4u61Fam8sS-xR-arhO0ofO5XT0z43PpISY6GTr_drPA_S_5E4gcrUO5fea8yyHwp8s8wAJoGNAWFYAao8G-0kWLwC_C2VWJutr4KosrHAVoD0N0hG4sdvN9bmcSghWvgJcxCwem7FLHBUWaE8U8ysYPGvTw-Tjv_pv_PbX9JB0jFqLeVfskb05THo1Nrp7qscR1xDcLo3741oOD0GmgssyYI-U26b15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c046_dadHsQqq5JS4ASedRzxcSZy2q-vNKDH6aRm_6BAkkuLw_DicIRpVeD9z1IREAHv4EHL1dDkp9fddH5WdZUDB5fQu4hyfpaq8rG6cufm033WmsHbFzFLml8bWTQD7DZBbAy7FgT0vFJh7QUOdM_zAnewAwMTjPgPfWdEPszRSMvNY0jezVXbqBYvTUfnrlqHO11zmvUhdQ7PRF2iqpOksVyylWjs3RVDhR3PZ-PvIPfSX0cJompRJyAW_waFfBGpmsAdYmj1wXkRLvAAfFOCqcUIg-bwcy5dNhIrtvqJgCnQKGfd4tcaMyNtyi1xFlvpfEQjBUinm5W4MeNHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=Xt32rYwSObWs3GW1P51MQcfaTqtS0STS5JizaF0BFIYwHxY9E9152UzI4GTwnMv0KflGDHsaNcuMlPsxaHCefMx2njLwSMVVVdIFnnxDlNh7TnF_AFeVtmKYxM51hUuXXOZoOzeXIiEYb3omAN9vK0b4I2K1oqCfgXDYGMjjgpWRmzmji3DSBH6prM8_xO23hT4_-lHcTwFfqU-sxgtFrfJkYxvXiJX5TQ7u4DYyJOZeDEVUqeIfOFV_wnsxASJetk4XEZNQ4cKpFzmiu7RRgXqZnu-8Wl5LcvbTI0ED4TIsfULfzfv-DOiW_NLU3R_v7F_Lq6vWcKUUrgr3tVXHSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=k7aueevpsP-NzGIGg7bff1cRVp3Fs8E8Kg5tPjY8Gt2cPffh3quB-Ir3LYGjoY0RpNoO3Q3GcsX_MXQdhWHpanpKwZuCxU6M-JVKhdETsJeOOHgKOg-i4jeT5RTN-YfRAvfO2qR5P3PuiwXiOAYfnBAtKhXhWDJ03ljFUlI8H_49M8ntu9gMICwhU3_PiDqKJOLii--uzO_83ZtECy73Wnc80Df1-0VVzXTLmU4pyPqD8fK8N2c-NcA3OoafnLpVq1EM8i6nuAImFLjyUs0UUlmyVhXQJQ995hRIT-cn_5d_uxRbcp4tPetUNf0bkL2ttK47UtX2XI7IcW7RJckzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=k7aueevpsP-NzGIGg7bff1cRVp3Fs8E8Kg5tPjY8Gt2cPffh3quB-Ir3LYGjoY0RpNoO3Q3GcsX_MXQdhWHpanpKwZuCxU6M-JVKhdETsJeOOHgKOg-i4jeT5RTN-YfRAvfO2qR5P3PuiwXiOAYfnBAtKhXhWDJ03ljFUlI8H_49M8ntu9gMICwhU3_PiDqKJOLii--uzO_83ZtECy73Wnc80Df1-0VVzXTLmU4pyPqD8fK8N2c-NcA3OoafnLpVq1EM8i6nuAImFLjyUs0UUlmyVhXQJQ995hRIT-cn_5d_uxRbcp4tPetUNf0bkL2ttK47UtX2XI7IcW7RJckzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=a-Ba72ryLxW9l9ddIXQnmDn0Elyu08JVs2oXcKllvk4een3jot2ihSgbL_AURtHSrTkXQNISFPrzOahLD8Yy5XS0cGAAy9VqprYkzmEYE0J5mLk1liTmDcDolX2U-Rg7Yd_5aRvS7W-ZAs2UxHpaF1-QgrpKvRCaVo0NZvtF_jwC4R5FtK-kQVWpxrD-9dB7Ohx-SFmV9jWlP0m9kkujS7FOa6ibQYtLUkmtlzCVFWobSCoPo7UwIvb6FGsisrUmlSGUNcc6JkVCPuuBw3dedit1_arfYthTmtzi2pduiJW7NGCDdleAJTQLMUSXBsZs_TIzUfVid4h6bmy0MaTRwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=a-Ba72ryLxW9l9ddIXQnmDn0Elyu08JVs2oXcKllvk4een3jot2ihSgbL_AURtHSrTkXQNISFPrzOahLD8Yy5XS0cGAAy9VqprYkzmEYE0J5mLk1liTmDcDolX2U-Rg7Yd_5aRvS7W-ZAs2UxHpaF1-QgrpKvRCaVo0NZvtF_jwC4R5FtK-kQVWpxrD-9dB7Ohx-SFmV9jWlP0m9kkujS7FOa6ibQYtLUkmtlzCVFWobSCoPo7UwIvb6FGsisrUmlSGUNcc6JkVCPuuBw3dedit1_arfYthTmtzi2pduiJW7NGCDdleAJTQLMUSXBsZs_TIzUfVid4h6bmy0MaTRwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPQUC0SIln-GBvTVmri-YP94KUOkabvqvb0Z3-Skzj6gWt_tCbYWMeobfqOVnZHS0SCd0Pu9VeltPDouQv_p6uBHRTrBeHg7rZys-7mGW77Zu7m88QMmDDbGJSp7Ey4Qoj87Yoi7LfXI1fkQQElC1E5Aj2hDizMnABaTukk19rVYC_6vdMBmgPbcJy9FIPeUa4tdnB68LlB1gwuJgPPiPcdUvGqGC0P-uvxscH8YJQFE2fbt5JSoKYHfOZuXUqJAdPmSjpibTzvvF0vSM4Qw6nOWzZkYT_xlz1HWS4KybqAtVpAHLxl6b8d3F2xKYE3i7rcdM4zgWqLFF7srFYQq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OErZ6O-Dl70n6b8KG9lEu-DQLIyjsafbwZrOJBYYykNUOcD32G06c_bSsuJfz2ZCoeOpLkuUnuy37yxlFO4utc6bhxiElp31H_j2KBF1zXxGZ1_EFfaKcrUZ6rDT5FmSL-Uz_TBScrvLNBj1nPDKSCaq8v-5-h-bVEOdTdKUQ_lfB2CyqrXPoiuep0BiJ7kWlqORBo1m8XScHdSurM9OsqpSLL94L8E0q-FLfwipt56zg9GEno8xky42mlFjxb2vIp2lLF9oNWYu_24tTwWOBCJttKfRI2rkQi9gNRUZ8hjNa8Q5ISOhpxQyOmYim55gb8d5w1MT4YVWMFoiWsPPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bG2yV7eSXeJzsmwSGK1ZE2Rwvhgidr6mj7xidMdv1hl20A0SYfm8rfIsENPRoYvm4iZwf0nhZUC-K2YKmjYCtKaQQ_vLpcbF5XPel_chUdfJu9xHkOC_iF0Ccfh56-23a_2tXMAWacLsYpum97fTtd9z0lXRyVzGbqmt80tSuqd9RnMftyo-6-97ZwqkQ8_gyrtMnntmmGrly7xsHJ1eUEAiNVb46QjRb3hkZEdDgL1FX8tt1WFef0UOzLNFSjbj9O9o2uqyVvY_lqBV0LUugmhO8vZy7QHxO6FyC_fphic6IhSyKskaxCfqZzzDOTDo26D8FoM2DKQbZe7UUPZnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNlpUzCt9AGhGZLtdAlaRNbdydTM_pe7-U5uGWypFA66Fwg9TNjE7306YzcaEc-a4OtgEaj7LFcUrSBTc4rc6Bm3DW2gJN2ex7VPqplnqEKgUbrtDC67K40JasGncTUmkYn2JBTLfyfWTbrTcKQ0VmjgCJP0sQQl7H7wABlXfYHzTqlncpcISlthFeKCnNwvzHywCcrHAifBshsKPqJzM8wmPyKEj546tmZ5wlovIUii1eq8EqyUqZcVpGkeWwfDPh1rr8UXHc5fc6u8ZeB8jn-vjtO2Z5zSC6qaDddzllTFUwQQGJcogmOtTondSFm1_bQePGcBVEI_2OvavHqJ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=flFXNMLi-nmcsqH8ku0SZbWS55tlHZc7LjSue_xR_lT_8KSzjPTRFSykhNL9GH9fc-bE-vETK5k03jXc_D3nJ7ADVoshrB4JiTRxAXLWYSiB_KaMFpJP_zYX4_lpacZXt17-ARkIhl-R1TYiyhcxGA4fCXNWjyfrilOplxXJ_6u16jpVpa-J6lRgtjtsKXgjgVNPdXvg_29ViH8RpXOhc1YMSqmfNAJEul5Wh3q0AuS8zN84WRjTD-bEbEUqH0r999S74H3SHO3p7XFX209jw6Vt7IHRctrq3JcoLwVvIGeje2hxJbipbCmX1HxMR90nEEfOSQv4De2zRQy-IhebIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=flFXNMLi-nmcsqH8ku0SZbWS55tlHZc7LjSue_xR_lT_8KSzjPTRFSykhNL9GH9fc-bE-vETK5k03jXc_D3nJ7ADVoshrB4JiTRxAXLWYSiB_KaMFpJP_zYX4_lpacZXt17-ARkIhl-R1TYiyhcxGA4fCXNWjyfrilOplxXJ_6u16jpVpa-J6lRgtjtsKXgjgVNPdXvg_29ViH8RpXOhc1YMSqmfNAJEul5Wh3q0AuS8zN84WRjTD-bEbEUqH0r999S74H3SHO3p7XFX209jw6Vt7IHRctrq3JcoLwVvIGeje2hxJbipbCmX1HxMR90nEEfOSQv4De2zRQy-IhebIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=lt4dTll9Q-BnVSbH2MsHTEw2lZ_35Vz8UhhYSnGv9O6hr5B0qzzUz66MefiAUdL6I7RcU602e2Z0E1FHcm2-rP7dEJ1U3je_82SqkuDD9CR8uabIqyJpmov83_MeuJ8W2YT3ftW9uvbX_RAHw4bOtuYnSUcRWhNkwQOEsSg2NDqOGkvrx9cR7uivMbF4RQwZ7Q-ffhztK98J-jjctyCjmx8Y0mNt1Ty-WrKVeNMZMIIu6cSXbdtDY80WL2tbf1wvM4MwB4rKts9LCaHi6-HP_XlrkKiUBS2KlOu5s1wAptHm9pBnbUkIRVPo0yzSCr896LHQR8ip8bKZdfbh-RRQpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=o_mLHprdH0Uo6mBHCrxzZFuTm_Yy-wH9NwtUQyTMqUHqC1EWH97PBsSHsnrHjJGhk7g11xOIEgB4FUnEBdAQER3eaNu3ZTG0AQigmMFvsOH3ASYMlSFJyj7l-gTS3WqzeYOaWJDEiW6mq-5OwXbcJj9ggcUBAVjVEG64Sw4rKqOCk34J4xOjzrCaarG_W3krNIG8XbhY5RSieEIaPDE_ice5fXNs_skoZLxHDv8D3G1ljQMmzlEMiwtM6h0gusoAuoiAjZ7Gc62UPYMqHxpAjTkn9A3nhO1q23dNrA-oN-R47PrQm-CoNAzxQbZjPgh9TtZDNGTjMV7-HyxBoH38lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=o_mLHprdH0Uo6mBHCrxzZFuTm_Yy-wH9NwtUQyTMqUHqC1EWH97PBsSHsnrHjJGhk7g11xOIEgB4FUnEBdAQER3eaNu3ZTG0AQigmMFvsOH3ASYMlSFJyj7l-gTS3WqzeYOaWJDEiW6mq-5OwXbcJj9ggcUBAVjVEG64Sw4rKqOCk34J4xOjzrCaarG_W3krNIG8XbhY5RSieEIaPDE_ice5fXNs_skoZLxHDv8D3G1ljQMmzlEMiwtM6h0gusoAuoiAjZ7Gc62UPYMqHxpAjTkn9A3nhO1q23dNrA-oN-R47PrQm-CoNAzxQbZjPgh9TtZDNGTjMV7-HyxBoH38lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc5mOI0_j8wtn0MnxOc0bT4vN8oWN-mKdCj7RSkvMADOex_0MSSE6w9g1haFagFWZM9F2ddHvSRXWxAR3-MgVEixLEKwSMEU6Gjm0aQ6FegBlupWPkG1E0YeFhxT2UZSaY-paOutPI5e1sxfJDf0K32JJKIbLzsagcKLbACEf0mz88ameMtXg5PotX8Ma7TcRsYKHP5flMwvqWEvopMcW41M78XCevusrt_EaSBRgH3xgdpNR3_kxat_H49tE093EcLkfgeYjyrItXYMpILjO84rS9dPKSdwOGTDPqWV7OmZHJMMVyImJ4EcDt_Vb1IecIriL940ex-eik_YPGLeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=HyAYqO82N0lHMZfSurU0Ap6CXagv17jkXWnx8we6tMwYnKCakTHZ89ahUyJMqfKDGfkBd5KW27i2Tkv6sHk0pJs3sEQZOpioU2D7Xj1RWoMXrJFp7PxJMtde04gTFX1srBCBY6c9PVqGlff7HTbHAwjcE4WDtaUb5Cu2DGr0YfGf4MO5TrUC9xshJbwLBPhdgwJ-WL2NOKR0AypuYzBy0B_dnvbEEp5syPlcB7YSigWfUs9HJZiVE2GzTHKADOiFWage3M0Y93fFQwLeSMDKfcKgQnzrqdW-lP0rHryr7IhusckfDP_WIMYvyp-By_FP92gSaOEhSO1dF_QOW5m58g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=HyAYqO82N0lHMZfSurU0Ap6CXagv17jkXWnx8we6tMwYnKCakTHZ89ahUyJMqfKDGfkBd5KW27i2Tkv6sHk0pJs3sEQZOpioU2D7Xj1RWoMXrJFp7PxJMtde04gTFX1srBCBY6c9PVqGlff7HTbHAwjcE4WDtaUb5Cu2DGr0YfGf4MO5TrUC9xshJbwLBPhdgwJ-WL2NOKR0AypuYzBy0B_dnvbEEp5syPlcB7YSigWfUs9HJZiVE2GzTHKADOiFWage3M0Y93fFQwLeSMDKfcKgQnzrqdW-lP0rHryr7IhusckfDP_WIMYvyp-By_FP92gSaOEhSO1dF_QOW5m58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=jrCvPMsDoCgddJzF1GClCXv5rPgSXxM9cCPXWYx2gZQqbGI65uq-2Aa-UcioCU3U2aIhWlUuhrAuRIfp4GnHDH1FJWAiBEnz5sVbqSg1hey0iEIs5r17Y32sKXbTQTPpZRL968at3UaiMu0Ceia0Y0uig-A38cYFj5hzZDlWWf4awJpdeK6j6pgyDGVKpesJuxT77O82fz27sQQrv_XVokiy8IYEVPSZYXD9qzzn2AMiWz3T_WkKYXJgfZkUaboALl4qh5YVMCaV3jXPbe-oWUHyyJo3BFVRfpMCuVjqjFd-xSpQUaysgVK0jemMEmDeZNUKOoOrTsACm1QCZSJ7NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=jrCvPMsDoCgddJzF1GClCXv5rPgSXxM9cCPXWYx2gZQqbGI65uq-2Aa-UcioCU3U2aIhWlUuhrAuRIfp4GnHDH1FJWAiBEnz5sVbqSg1hey0iEIs5r17Y32sKXbTQTPpZRL968at3UaiMu0Ceia0Y0uig-A38cYFj5hzZDlWWf4awJpdeK6j6pgyDGVKpesJuxT77O82fz27sQQrv_XVokiy8IYEVPSZYXD9qzzn2AMiWz3T_WkKYXJgfZkUaboALl4qh5YVMCaV3jXPbe-oWUHyyJo3BFVRfpMCuVjqjFd-xSpQUaysgVK0jemMEmDeZNUKOoOrTsACm1QCZSJ7NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC5m7Wbc6UJx3fVocnE8Naz5rVlC5c69noVxrEo_tN1YY1FuqehnHRKPrREol8NIc3TSSZq5kRPZvuBa7y2vBjPqTK4jjSkjedegnf2BRyJcy3s8m9p_BzFZY2EZCKAXV9PuN0RPtlouNqdrcKrQKd-aiM2Zj5jIsOiru8_KiLcJ3mFQWBVfmrGl6NlPov0iNc4r_iV0_CDTK0UK8Yo8U9GQYfZ-muPOyRDeJOMrab_yU3iP64_o3SjXzLZIwc5m86A7y3BWFDYqnhyDX7uq4Rdry6RCT68Gp2UsSFDGtV1B5OvGzftK_aNJNjCfB-qH1mtEF7RjwmgxxA72UPO17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=KI_aqSdYt7s7cYh7LZNt4mBqcL_yd_pQqpEl2uMDl5AmF7Of836yXov9GqRQ4KBPP_o4vIj2G_nzhdvuQkQ4ZTtAU9yLEdMwX2r26eJteh90qHEc_xup2xYmvBYoyQGsGgelR7JWdaPtrjRg45orzR_Q5yw-OyrEJystncJA2Of0JlS0vEPGjlK5Y__UNy4HzFHRdDaLgQ35wUhtuY_ByE9xNC_r64VktCV55IZ_QQ69y_EQkuM3dZgMOg9-NGlb5IcMCzLHjf8m87bd3XYHabQP7-Ag2Wi5n9PwthTmkraXqs-HY7gCIi6fdN__kdK1Jr-AcrDis5V2b0g_yXnzVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=KI_aqSdYt7s7cYh7LZNt4mBqcL_yd_pQqpEl2uMDl5AmF7Of836yXov9GqRQ4KBPP_o4vIj2G_nzhdvuQkQ4ZTtAU9yLEdMwX2r26eJteh90qHEc_xup2xYmvBYoyQGsGgelR7JWdaPtrjRg45orzR_Q5yw-OyrEJystncJA2Of0JlS0vEPGjlK5Y__UNy4HzFHRdDaLgQ35wUhtuY_ByE9xNC_r64VktCV55IZ_QQ69y_EQkuM3dZgMOg9-NGlb5IcMCzLHjf8m87bd3XYHabQP7-Ag2Wi5n9PwthTmkraXqs-HY7gCIi6fdN__kdK1Jr-AcrDis5V2b0g_yXnzVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7VzpXg8h9yYJPebvcRVzv4Axbtkgnt2CZX06h1MrZRLZO0AB_CNvXY6IeDwa21lcSNNtODCBahOjvytsSB5w0boPVMEXGghaeOvyaXYkOBgil_8okeRyVmFlYX_waNmDqTHlJEohPln1_oPJEDU50fzHqzLVtQkPZEVWiGL0qKBAoZx553zT4rRyM7RHj0aoLJzFxjBe54YqImj7pykT61-5o3QblUvwZT7IEQkJIdDBlQE6J9J4GhsqoexKS04Q0A21DrpUlVvfzyLfvC5yD3H5cPR-Pr_N_duC-IxsMNqQ3oC3W3WtpqknHeR08dbrmlZH-B9wdXOL63nbQ6hGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3B6bA-LpNM7npdemGTpUYxauu7YTczSPz1SBesxLDIfYdK_77HyEYrup1mW01S5q8VoxSIBacziwtNI1sLlucwf4BfHafuVI6WMiRkVe0Orp3a5WCWW3sROTSZobmcXOg6PJWAKObi_USIWygBw1CisRIFhwYSnBZwN8IZaBWMJ-Dr3CQT3TCod_rKgU5Zae9nkcLCP1VtO68k6hU1gja5DuSi1HyijcRwLmRol-prEDimQy83-cp-ZaYgObcnekTxgKmcY44N3lWMu-ZMbfeai1nQdq9pSRNn0F7h-ZxhpSpJ6bn5NXP5sOqKg-xouX2-scalnI-iiq9_OObDuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=e7rnRjJkE7GjNhaj_ibwAAQKVsrq3l0vGbEfo9ogaVxTBCjwsSwfAWYHw01shwi5AFdfaCEPClDKOHFuyb9pJwxYMHwhSmibupr3V9CwK5BxxLMeWIxtLvlFIWFdpFKRydiLvjhHnNCss7gOgpf51r5VjTUneaVz7DvjQlA5HQrGHMcGSP5t3C_Ej9KXqzgx0Notmda82iLb0PAzpMcsfTPk_8H-wNYozVHDSgAf0aaxvIsn4BziJ_xl27lkGH4QS0a3aXFcv6hgVXIkTJqD49FWA0DTXYCq9rUhx0IPO0BrwKhN3xiuj-XUcWe2cTKQD-UWO5HQXI15g4dPqaiqdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=e7rnRjJkE7GjNhaj_ibwAAQKVsrq3l0vGbEfo9ogaVxTBCjwsSwfAWYHw01shwi5AFdfaCEPClDKOHFuyb9pJwxYMHwhSmibupr3V9CwK5BxxLMeWIxtLvlFIWFdpFKRydiLvjhHnNCss7gOgpf51r5VjTUneaVz7DvjQlA5HQrGHMcGSP5t3C_Ej9KXqzgx0Notmda82iLb0PAzpMcsfTPk_8H-wNYozVHDSgAf0aaxvIsn4BziJ_xl27lkGH4QS0a3aXFcv6hgVXIkTJqD49FWA0DTXYCq9rUhx0IPO0BrwKhN3xiuj-XUcWe2cTKQD-UWO5HQXI15g4dPqaiqdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=d_AAJ-NR5_VlWyqyv9cbQpKFxdiZNDpnB16O3ZfIp_y_VVyfvFz7eiDTZvu73WhKilIcFXKKuKnvwpTVSoQdTuJoZ-z5fO4OqxLkb2OXNcTBRFe3OZaEan-SqSjWgIs9G_LpBRg4OQf7cRazudympyIL6eZou8oj8ChDZWeFqYxwTm8ZgGkf46V7LDy0OJx7lL4suxNCk2oLpOTEEPbEOvNLm0sAMFniXdqNWqT_ALtbepU1oUIsel1kkBRd-ekFJhn5SkQOenM_G3nPvfmse4_6FkpixaIiD2zKvMAx9tV0ARFKW-HcUzsUXGF7Ea_PI9pW1i1GYMh70tYTfSKwWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=d_AAJ-NR5_VlWyqyv9cbQpKFxdiZNDpnB16O3ZfIp_y_VVyfvFz7eiDTZvu73WhKilIcFXKKuKnvwpTVSoQdTuJoZ-z5fO4OqxLkb2OXNcTBRFe3OZaEan-SqSjWgIs9G_LpBRg4OQf7cRazudympyIL6eZou8oj8ChDZWeFqYxwTm8ZgGkf46V7LDy0OJx7lL4suxNCk2oLpOTEEPbEOvNLm0sAMFniXdqNWqT_ALtbepU1oUIsel1kkBRd-ekFJhn5SkQOenM_G3nPvfmse4_6FkpixaIiD2zKvMAx9tV0ARFKW-HcUzsUXGF7Ea_PI9pW1i1GYMh70tYTfSKwWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC_9kV_q66NAZunf46195jRcfPOoj-9RAlkBwU0HLeLtgKlGtgbkEY4xI-josGyMkfCwgObTJqQs50lvktzRTQ4vaUkPxOc7J3pdn4hMYh4zUpfWfY8_5jq7_GgSqEN9q4MtVAHMUVdeCkHuRn8TSzRdfMq9GRZRHlPT0rOhjnNgKOYrbSYoGZCtLnfzWdpyRjPHsCbpWY95Br9qUcdDwpBI3hexxo_twyzIi63yCVK123uH4KM15bJSIIbCo_ZW9pkBUEro0SvDlG9K7DhmQqQCpEA7pfe0YWi6PfcQ_0gD2KFLN01O4UhFffTlkymDOtIij5c_ru8WqyT3VqFhfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCbam467A_QvTvm-DSqSsuLhn_LCbkUj2BCFh_WobxI7ODaHDDS1lsbPhir3VgGDzddyaVGnqL-wd-WDrhcrhiw8JC67ictVKE6jxwxKry3oxx5ZdIXQIkcXZaYqbhIzKoH6IhzxTUmSC_Xm4RDaQOUsj6qv9GcmTNd_lYibtoI_4JuiL0W_2Gil-6b6HLIUg6e0kzHGo8IBifcIhdhBvFIPpYYfyTdMIMCByVqkphFtVZO0ocyOIa6EVSVXXvgbgfLV8zFr18QJmgAh28xqnOspSFvZNXzI389HQdHgVyEoxUIa8TTuPqpjb41Gz4NUupS5M9N1Kyv1wVqopgCYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=k_CpKXIjAWmELKRJoPDEsiz_ei65Ae4G6fNK-SwTR7r_R-ZmMK7MNVPBxAmdyXqx00p6F0fukgOkw3D7zxDFsW9y6gwl2KwsPkJXaPuJIeaWMLuxv2Unp5PxcW4nCLUwDrkik-g6RJfdO045tqo1IHikqx__BF7sDT8ZZ-TQv5tW6vIG1o22hfOMy-6c-I-fjeiNHno5tlMi7cLQ8pnfqDNXuyHHJYf6vhu-59Bh-_64591d9l-vJ4MGnoFIxIIir0pnhfAXuTm5MwGgfSEkXsSkmBSgTDW6pVUJMznKwm3VMU_Acm3vS2_hc9MHbciHMhkMzSB1mFYCkqmSi2Axqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=k_CpKXIjAWmELKRJoPDEsiz_ei65Ae4G6fNK-SwTR7r_R-ZmMK7MNVPBxAmdyXqx00p6F0fukgOkw3D7zxDFsW9y6gwl2KwsPkJXaPuJIeaWMLuxv2Unp5PxcW4nCLUwDrkik-g6RJfdO045tqo1IHikqx__BF7sDT8ZZ-TQv5tW6vIG1o22hfOMy-6c-I-fjeiNHno5tlMi7cLQ8pnfqDNXuyHHJYf6vhu-59Bh-_64591d9l-vJ4MGnoFIxIIir0pnhfAXuTm5MwGgfSEkXsSkmBSgTDW6pVUJMznKwm3VMU_Acm3vS2_hc9MHbciHMhkMzSB1mFYCkqmSi2Axqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=F5ui8z3ekc8gVkJe_lYRoS7bVvKy1O-3hn4wvIeceRVDZEQiO4gQi8spCLazZnJt7PeMvqNgzffAQv36FLyunXfn51uLTLrTqbllWAulMCJD7qrjp9tl3chxblcyP2ZkF50UAXiqfx0fb9AAUk5i3yl5LSAcLE7JN6kNAzG9T1G7bWMxd4wewbvL8SMRtagRkvkSo5TgLPW5DwKia1PvnHN7t6LjvfsLIV1vaZM7IXpMsQW8ixYzJQHxaVQ0phL7hasFPRGdnMUzldh2-isrzwhWzbs__a-A-BFadG1ilSBm_1SpeYgdnZCuLmARvPwzvRwjeMSstaU18q41UCYp8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=F5ui8z3ekc8gVkJe_lYRoS7bVvKy1O-3hn4wvIeceRVDZEQiO4gQi8spCLazZnJt7PeMvqNgzffAQv36FLyunXfn51uLTLrTqbllWAulMCJD7qrjp9tl3chxblcyP2ZkF50UAXiqfx0fb9AAUk5i3yl5LSAcLE7JN6kNAzG9T1G7bWMxd4wewbvL8SMRtagRkvkSo5TgLPW5DwKia1PvnHN7t6LjvfsLIV1vaZM7IXpMsQW8ixYzJQHxaVQ0phL7hasFPRGdnMUzldh2-isrzwhWzbs__a-A-BFadG1ilSBm_1SpeYgdnZCuLmARvPwzvRwjeMSstaU18q41UCYp8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=iAumE8FHoInZ9jcftbztblkUhyTPqsFA_1pIl0wGqaawXT9dfFgwplw-mb3XLXAeoqIdO56ng2tTMCRRaI7ch6HMSf3SV1G-ETU1qqXSQStzehnnoO48ceo2z5HXX3L9p9v2tsjSQ_VjN9bdsfajOre_rSeNTy_KhxtBm9B2Jkp1UV20kNzi2eD2JuE9Yb-m8cxj35h1RsJbkZS6PtjbdZL9D6ShZXzyB3gNZoez3f_g3xFRAICME-neB247i3ysrXtjXuATmASM3bohstVCy-F_-FUE7IL5n_R6TlFqcAtDKsOssnAS4zP-FESTkhzOkcrkkKwLsWVoV0gkIlF5vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=iAumE8FHoInZ9jcftbztblkUhyTPqsFA_1pIl0wGqaawXT9dfFgwplw-mb3XLXAeoqIdO56ng2tTMCRRaI7ch6HMSf3SV1G-ETU1qqXSQStzehnnoO48ceo2z5HXX3L9p9v2tsjSQ_VjN9bdsfajOre_rSeNTy_KhxtBm9B2Jkp1UV20kNzi2eD2JuE9Yb-m8cxj35h1RsJbkZS6PtjbdZL9D6ShZXzyB3gNZoez3f_g3xFRAICME-neB247i3ysrXtjXuATmASM3bohstVCy-F_-FUE7IL5n_R6TlFqcAtDKsOssnAS4zP-FESTkhzOkcrkkKwLsWVoV0gkIlF5vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=sccUkaAQTD4m1CdauYBgY2KihtbdaSgKRScbvV5WpYo_basY4O66wgb5JHkCiG7U0JNnFZd0tMAEv-zk4BHAj9uriFcPdXeLM0jp4YQvzB2w0-60EJ1HnExbIw7W9VV59y4HOPBsrUwItwn-wXQGQ0T7q8heoCX0kKvU7tQ3Y2HAL1Sgei3ha2eVlgdQM__E6pWJLYygoyxzf6acrsZ-ECMzhPNDQeg07asuKr_ZCbg--omFmPodqGPBFKsmTOXdhuGrMNegC--IyYP3-JFQx8Mn87iHfm9cwQA2pLnB0w_iMoPCrgTJ4xdQwBmjxanVNBxMMb0-IaHWaNEJJBAUQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=sccUkaAQTD4m1CdauYBgY2KihtbdaSgKRScbvV5WpYo_basY4O66wgb5JHkCiG7U0JNnFZd0tMAEv-zk4BHAj9uriFcPdXeLM0jp4YQvzB2w0-60EJ1HnExbIw7W9VV59y4HOPBsrUwItwn-wXQGQ0T7q8heoCX0kKvU7tQ3Y2HAL1Sgei3ha2eVlgdQM__E6pWJLYygoyxzf6acrsZ-ECMzhPNDQeg07asuKr_ZCbg--omFmPodqGPBFKsmTOXdhuGrMNegC--IyYP3-JFQx8Mn87iHfm9cwQA2pLnB0w_iMoPCrgTJ4xdQwBmjxanVNBxMMb0-IaHWaNEJJBAUQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRiOEdI1aK__BgKj2D1rorzkiQGmt6tIE_rJml_3zi-jjklbIgZmmUuW-tp145-yAaxlUzAFwVBOELyQLZGqZJBVZgLPK0V1dWZsuthBBR3GbPfJtIQkm8W5OYeKxp6PTd9IhUtqw5ClOzeIPBjlnvznfwQbF9FNU_9HyPGHGNHSIO-5rmWk2_yVPZn9lZjXSMws6lEoEIOaF64uGnzSUF4iOJ81-Eflf5CNunTgI8bgv5sFRclhPjbV1OK2oCMa_r4Gf7qSpCXfJfnk48qGycQzvzohG1FlL_UgCBXHU5cmhA2_kbjDp-16Q7zukY-piySsg1UX7EzplrOVyhw-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=Osly0RO0cHMCf6wxTeS5lamE-BVvzbdcErv565VQndMBWS88HdBtS8XoqT7k9BuTWe-LBlXnmZK1RpMbkhydNiZEkkHSOj1HqeB-soRDCV5_A7b4on3jwIp7O4RGpK8lT4ieLkY_aHXq8GxG3xm5Gndx9D4IgmXvoBEem_M3Wg4I4BWZy4KKuxHWZbXk9MwxXQRUQOJ62OSq9NngPJwW0OlOPVLMmyppWI2euIUqDtZkXRYDXXJ5MEOzM1ZK6MWf6ZATVgyL9PXUkiHDznKYO-oK5WuPrWFA_6tWhaLkl2f8r4o3O6VQV364meX-jjjleg4L2j6OBNYVlYzGd-yVVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=Osly0RO0cHMCf6wxTeS5lamE-BVvzbdcErv565VQndMBWS88HdBtS8XoqT7k9BuTWe-LBlXnmZK1RpMbkhydNiZEkkHSOj1HqeB-soRDCV5_A7b4on3jwIp7O4RGpK8lT4ieLkY_aHXq8GxG3xm5Gndx9D4IgmXvoBEem_M3Wg4I4BWZy4KKuxHWZbXk9MwxXQRUQOJ62OSq9NngPJwW0OlOPVLMmyppWI2euIUqDtZkXRYDXXJ5MEOzM1ZK6MWf6ZATVgyL9PXUkiHDznKYO-oK5WuPrWFA_6tWhaLkl2f8r4o3O6VQV364meX-jjjleg4L2j6OBNYVlYzGd-yVVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktIPzVN_zKYyJIKYK3QIqQCTuPZDFbdPCTlfYDazklNR1HnzP0JfclhpHQ_MFqUD87L7_6d1BFm2Te7JEyqN4t6_be4aeiya_j2WWYzJUi5gitZz2EZwz-KnB4KCFpyCiCVZDQDK6Y9BgdfExCyYQGLWwPP7awmfRfGPffPacRyKrl95jjCE9imkFKgnNS8nRlJn7N2BqYe269TgxEDgtZ12tdWI_1AOCBN7OWATEnA2taMgz95gANOBZpAUgYGevYg8g8BfJik7iR9qyigQdPo76T5r3qoBJPmgn1WEDAwwGHmvtFUNqgtBhK6y6tOkpykfVfzk3XgXWmyZyYNHHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=fTQSa2f6j64i_Nx_zIE6wGDxcdwxw6ZQ5FpARhif8GEE5XgyVL-FZriqQ9UTJSzS_DeNHgg16Yu22Uml32oeeQZhUHEvO2RoZktWHvpEmiOan-2GRwcE81WaxdQEg6nkNH0oZVLJb1Oe34VgWHcNlQjiAeVgNpOkn8eg4haD9GjfcIIjUqhkHFONdw6FqsM6qLt9meTFDsqSMnTp7OmXQ6qwhPTfa4syrQcXu6K1IgKPIkHqwB7iEHSWY-xLWNGMfv1udwwcBMG4JwTq_kqDlMF9K-KwzQfc4d1nMLLHSL-5_2LMU8Ta6Nvd7b20DsjxuvOYECI2dOJugyi7P90CJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=fTQSa2f6j64i_Nx_zIE6wGDxcdwxw6ZQ5FpARhif8GEE5XgyVL-FZriqQ9UTJSzS_DeNHgg16Yu22Uml32oeeQZhUHEvO2RoZktWHvpEmiOan-2GRwcE81WaxdQEg6nkNH0oZVLJb1Oe34VgWHcNlQjiAeVgNpOkn8eg4haD9GjfcIIjUqhkHFONdw6FqsM6qLt9meTFDsqSMnTp7OmXQ6qwhPTfa4syrQcXu6K1IgKPIkHqwB7iEHSWY-xLWNGMfv1udwwcBMG4JwTq_kqDlMF9K-KwzQfc4d1nMLLHSL-5_2LMU8Ta6Nvd7b20DsjxuvOYECI2dOJugyi7P90CJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxfmRtwUAfYwhsYsGStxwZ__agQqilXpX8GHmjfgzy7t7CRPz8fMYuYBJ2p1kv6FHUcVOFPBDqIOcvw1urXOGkTtNxlrtnECASHTfuzXrajcU2LO8IWnYPDUsFkPpEfLWMa-cvnmG6j2FMmeJ8KsUIVKBJ_CYgH5pLA9Oqc0hwTYKU0oY0E7m5mAjRs2x5ZJmqNQhLp80rGWQ_3GXII4A6XrN0ltV8N03gjB_UgQ9Zw1NBw3qVI92cVTcx9V4DKbTzzxPuibLTy0XArDLfrZ51KIPtlT9qestKDxr-T3PtsqDgOR75Z5IGk2tVHLb0myltmJCG4AZy-WvrQRqwQ0fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=abuMMsQb8_yDf9zEz37S5h80UJ-2LJ_VLG71CU8vr153g9ftnkm48NN0KrrNeBAihYnK-QRLwjHzg7haD1UDdxnKOwWa3ACFU4gMvBzPS0p89_bRkEAv4sCEYowqb8zCeT-9srL3erwfR6JafqPJMr_pUPtkypgoeli6QQU67Xq97b08SOQckWynh60s1OCgLQUKcBElz0VOdbqxhjnddKPA68spwJQnwtFq4PZeEpnFL21B_yP__6ouaZvENW3_7t9qozqCiKxmmXxkadSDOELETbKuoR1oHhNmuT_UsSftpThVrkcuiuBkpYjQHcOALpQ_191Nij8y0wlZ1ZEfNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=abuMMsQb8_yDf9zEz37S5h80UJ-2LJ_VLG71CU8vr153g9ftnkm48NN0KrrNeBAihYnK-QRLwjHzg7haD1UDdxnKOwWa3ACFU4gMvBzPS0p89_bRkEAv4sCEYowqb8zCeT-9srL3erwfR6JafqPJMr_pUPtkypgoeli6QQU67Xq97b08SOQckWynh60s1OCgLQUKcBElz0VOdbqxhjnddKPA68spwJQnwtFq4PZeEpnFL21B_yP__6ouaZvENW3_7t9qozqCiKxmmXxkadSDOELETbKuoR1oHhNmuT_UsSftpThVrkcuiuBkpYjQHcOALpQ_191Nij8y0wlZ1ZEfNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7E7IZfoGpgcpmnlU20ccMp4FDLXtkRE0r4oJmOqyKFx7rHQIFcAZlODLmPDZMV--mBKjJWCHWpdU3QB_l1rOYUrRoximc1SZbBANi6qxN4853kF_sFWO_RNP_apSG2JBDh-bn1BXRF2ISb9KfZE01x4kzplK68hhQBIidUILcHc5U-9TtM0R-m2hYV_R15s20wbzVIVLV35oRdPaNN02s3z33irj5ZePDqft3ibqRNS-TIj9o4ngwv0fsyySECDc11ti79JM38K2lJLW-OUhoqz07l-jyH2v7VNkooy8GfT5y7M-9wBHBgHfpRp9Q9AhGHmbIitgDv1_WLvDU8B8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=oRYARo48NcL0KHl3l0K0l_QVbc_XbU6TeAMpjeIIYZZ9EjH3bkca8Wx2EYb2NkVZdggofCTff8MEo6zknEdDfvk6Rnk3RVJfkbQC-8_7ifOzJSlBZizIVWwaM6BATQskXnAu4lyiFnQtjrMm8CN6Q59RzgkdaRH5-YbYFJR0XfqFdf5v3hdygPOpusTvGZR2gc-nLN29tLkvnftFMZNOUoVI49rTCuQgAtG4pxulo8Uam4rdkpqjNq5rCIjo9y1B52V3lDy3W7-A_NsoGvNpHoRP46nGDJACdALFclByfdtnLpcKJV51T3CdCWUhfSDZ0RMW2ifDblmXzGlAgQ4C4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=oRYARo48NcL0KHl3l0K0l_QVbc_XbU6TeAMpjeIIYZZ9EjH3bkca8Wx2EYb2NkVZdggofCTff8MEo6zknEdDfvk6Rnk3RVJfkbQC-8_7ifOzJSlBZizIVWwaM6BATQskXnAu4lyiFnQtjrMm8CN6Q59RzgkdaRH5-YbYFJR0XfqFdf5v3hdygPOpusTvGZR2gc-nLN29tLkvnftFMZNOUoVI49rTCuQgAtG4pxulo8Uam4rdkpqjNq5rCIjo9y1B52V3lDy3W7-A_NsoGvNpHoRP46nGDJACdALFclByfdtnLpcKJV51T3CdCWUhfSDZ0RMW2ifDblmXzGlAgQ4C4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=TEhou6wep20n645XHQ0_9YFXj_w-VOFm4I1mkdmXsbAxu6Yb6AdSUyLGDuy1kskHdMYI1dgqR8hhT9P9miL51ZLSqvGjGPmY0XlpmDDmgi8X534Q5JfYHnWn9dH9WB1kSmJO1DxOQ5oy1vzb8tSh1qdkoVDsM4BF5LTubeqIs3gOA-rmU8bTnn4gCQReNP5J1RYZD2ykv45ZZKeyojzlUkFwEmUrTcEc07s1KWOwzVTU73IvCFK4di7jt9A--V08d7c6tG1DfOhJYaB7bQ21rVQYNWd_9AdFPHUt-uAfkI8EZkov1_Bkvm8faCtrU7e_AWZV5wFCxjoEL_yLe4lUbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=TEhou6wep20n645XHQ0_9YFXj_w-VOFm4I1mkdmXsbAxu6Yb6AdSUyLGDuy1kskHdMYI1dgqR8hhT9P9miL51ZLSqvGjGPmY0XlpmDDmgi8X534Q5JfYHnWn9dH9WB1kSmJO1DxOQ5oy1vzb8tSh1qdkoVDsM4BF5LTubeqIs3gOA-rmU8bTnn4gCQReNP5J1RYZD2ykv45ZZKeyojzlUkFwEmUrTcEc07s1KWOwzVTU73IvCFK4di7jt9A--V08d7c6tG1DfOhJYaB7bQ21rVQYNWd_9AdFPHUt-uAfkI8EZkov1_Bkvm8faCtrU7e_AWZV5wFCxjoEL_yLe4lUbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixwuK6hX9B4kJ--9PKL7oayvo85liQlDVlIn2NbF5n5T6R1GGbsjlgSYAqXHRCdQW8J7UeNz0kiM8XHukWFNckU2vnfQqy8tHFrhl5sY1_VuHJfou2pZZWV_n_6VkV8M60VsQq9cRK93lFl7mNc5pO3HCBBlMISwDg8r8IZri9raHfK1AmxZST4fApKy3U2FGAOZsMqyLbhrnD3dsWOH3LtiZuiTEdBSf1M6WvZ5xQ0aVnReh31Wm3z7_xw2IRsyhvWOxgyGwSRQX1wSL0HFtEX5cHwZKVFKYH_h-e6qeHtYg8DasN98SxkOvDCWZST4Sptku7XVDqJ6UX6DLFP02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=o_iN84k8sQL3nJOPr1bszE8yfkGvFKJ56PZiimxHmX1zai2wgxD-8vrlVE1Xh91ynElPtRpVhRYaZobHUIlIRsmb5X7mJBv3mUE0Ff0kPWxTE63JAurQ-ZZw2znjU9FS6j46ZmDtsutSbUdsvoo4XZ7f8NASN-SKW43NT9hjtZJYlVhSKsG8QKWFrZCqvQhqLXhumvvyOmF-c4n-89JAICFOFkoV2FPNuvlLhQ7COn472Rc9N8bcvdyUq7bpQPj62CHu1gSRSmR1CmcdRZL3-gCaDs0U5tw0IXhvNegIIbK-WpRcHrrW9Oj0_A5eDURcnMk0ClBaCDqcjv3bxWz6ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=o_iN84k8sQL3nJOPr1bszE8yfkGvFKJ56PZiimxHmX1zai2wgxD-8vrlVE1Xh91ynElPtRpVhRYaZobHUIlIRsmb5X7mJBv3mUE0Ff0kPWxTE63JAurQ-ZZw2znjU9FS6j46ZmDtsutSbUdsvoo4XZ7f8NASN-SKW43NT9hjtZJYlVhSKsG8QKWFrZCqvQhqLXhumvvyOmF-c4n-89JAICFOFkoV2FPNuvlLhQ7COn472Rc9N8bcvdyUq7bpQPj62CHu1gSRSmR1CmcdRZL3-gCaDs0U5tw0IXhvNegIIbK-WpRcHrrW9Oj0_A5eDURcnMk0ClBaCDqcjv3bxWz6ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=Ruv3T5SrakJMteXnMzhqcTvT092Tu75iNeM10sxzA4yXJUAjmlpUym8c2qjmgSUg-U7HY79KjZQrv1_4YZtIC06aIN7bih_nXBRgnUYL_pecsplW_dyaa9qxSyhqR6voynF1fe-WQb9kI6F3cy7F5puPsN-Uiz4qHsb4K0K-kJaaYl9tb1vXLEJQW8CA-YTustpmiQu0OJYMOqsPjLpHcLB1GEKhpaM7v13BkLoyqacNmZmsLFUlt9Mrdzx9qi8SgSlcXOp-xs1-ZShVkgE4qldQ1d17ZKo0noZ8MAgP6Nm4UX3_SeDoXgOud6zrbDDE-oHn3F7qgPsb5uV54tGdJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=Ruv3T5SrakJMteXnMzhqcTvT092Tu75iNeM10sxzA4yXJUAjmlpUym8c2qjmgSUg-U7HY79KjZQrv1_4YZtIC06aIN7bih_nXBRgnUYL_pecsplW_dyaa9qxSyhqR6voynF1fe-WQb9kI6F3cy7F5puPsN-Uiz4qHsb4K0K-kJaaYl9tb1vXLEJQW8CA-YTustpmiQu0OJYMOqsPjLpHcLB1GEKhpaM7v13BkLoyqacNmZmsLFUlt9Mrdzx9qi8SgSlcXOp-xs1-ZShVkgE4qldQ1d17ZKo0noZ8MAgP6Nm4UX3_SeDoXgOud6zrbDDE-oHn3F7qgPsb5uV54tGdJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=OMO_OPl5QGrx9VgbQ9WziitrZ2CVhGS5jgNtb3_d4fyrCFPdU7MAISy9tmHeDmv8fMy6U6eS8ZYRRPkP8CLUpgs7WVCpSp1kXub0WXdXE19ZkqUJ9gsd5-pyaeJQ9tXmuAsf_djKUrsyWIeNe8CqWBrALwdPJ52Sto5VPs7fjPz2MTedWd8S3z64JSPigBrKK6XKqnwq70taJNF_gk9dVMyi_6BZ-XK92GnJm8-kGmfgXJk3x540HzxUlafAv2VgzpoDaO4xLT0flmzxUjxOgVvbsNI1vFwaUbY_Ucd6SreTC7M84wyBDARvM3eKi5oAQAZjUVZua1kx85BEKUvHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=OMO_OPl5QGrx9VgbQ9WziitrZ2CVhGS5jgNtb3_d4fyrCFPdU7MAISy9tmHeDmv8fMy6U6eS8ZYRRPkP8CLUpgs7WVCpSp1kXub0WXdXE19ZkqUJ9gsd5-pyaeJQ9tXmuAsf_djKUrsyWIeNe8CqWBrALwdPJ52Sto5VPs7fjPz2MTedWd8S3z64JSPigBrKK6XKqnwq70taJNF_gk9dVMyi_6BZ-XK92GnJm8-kGmfgXJk3x540HzxUlafAv2VgzpoDaO4xLT0flmzxUjxOgVvbsNI1vFwaUbY_Ucd6SreTC7M84wyBDARvM3eKi5oAQAZjUVZua1kx85BEKUvHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=EX6amF4sflWuvrH3JYbgXzax2c0kskisnGjgL1bcdgnoYlTHjfigR5y6Eat0Hda7yGy1yxEyBX8iVaNqtTL6r9WO3a5TKlJvBR67JTMK7zewvcQD-bCMt3iGISVPaBhmbANm3D7_1-zUMeYH8HYb5NzpX-cplK6O_Y60m6dfFgq2l7gU7ojudpQgVZBpO061xVlEZBc_qgJS1dn_WinUV0x44GFgV3YRM82znvm_YV30a_9s_oT0E6wh0DmvAvIiqOzw283DUCs6Uv65AcqhQVMeehWm3EEkrONCxrEvWO3ZalOh-kxRzKoW8yMq93nTzJGocnKjG4g7-NXLLT8mYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=EX6amF4sflWuvrH3JYbgXzax2c0kskisnGjgL1bcdgnoYlTHjfigR5y6Eat0Hda7yGy1yxEyBX8iVaNqtTL6r9WO3a5TKlJvBR67JTMK7zewvcQD-bCMt3iGISVPaBhmbANm3D7_1-zUMeYH8HYb5NzpX-cplK6O_Y60m6dfFgq2l7gU7ojudpQgVZBpO061xVlEZBc_qgJS1dn_WinUV0x44GFgV3YRM82znvm_YV30a_9s_oT0E6wh0DmvAvIiqOzw283DUCs6Uv65AcqhQVMeehWm3EEkrONCxrEvWO3ZalOh-kxRzKoW8yMq93nTzJGocnKjG4g7-NXLLT8mYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=hBlxNQk8TrnP9X5vN3mwWSI2UdWjkeXxHy-0RO8nF2hhQ-VccCFyZlJgAxzECTKOFCGZmOxl4q5Tvq5gRIsrr046PvUVmjgWoKCUDZKQQ9n-Qs0mRrPD8zJVzi2KdVOo64pRhKFnGU-W8M1T3WpxbLFVz-grc606tfOidAKij7xvyrVMvBdiqiKhaCLrct6ZJ8WeuZmPnchtaRZL7dDCqYTT2CsniUYV1RF5eD8yT3wOMx9gJ2YcpoiFXcSCt0v7aFoppiMQu-R6COvLZlDStDxfNkGS5VEBLseKXjXH5UotqBzbxTorusxJjQKzuE_lk4XPypKMknA5-QQ5hZD8HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=hBlxNQk8TrnP9X5vN3mwWSI2UdWjkeXxHy-0RO8nF2hhQ-VccCFyZlJgAxzECTKOFCGZmOxl4q5Tvq5gRIsrr046PvUVmjgWoKCUDZKQQ9n-Qs0mRrPD8zJVzi2KdVOo64pRhKFnGU-W8M1T3WpxbLFVz-grc606tfOidAKij7xvyrVMvBdiqiKhaCLrct6ZJ8WeuZmPnchtaRZL7dDCqYTT2CsniUYV1RF5eD8yT3wOMx9gJ2YcpoiFXcSCt0v7aFoppiMQu-R6COvLZlDStDxfNkGS5VEBLseKXjXH5UotqBzbxTorusxJjQKzuE_lk4XPypKMknA5-QQ5hZD8HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=Ol7UmJ9DOxdbKKMFLOaxYOPJIywr9l9okyrDvCknzDiNGQ620fAJCaY1pqWrRgGHiWmCXOB55lSYMDN_EeQ_Dv7DKZycvl0IcvhHVsRyolEidUuNWdXiqqVabDlvBjmJSKfaSHFNoDV13_2VXssZkTqlGF3h5glTp0UoFQSQz7OibJrnhy7-wOYWAgutuwHO7wkw50q2V-0RcMpmzSOV2H_s6vJV0RRf_Yn_w_u29xfW8A3Za3dg2yYjmmsq3DK5SVtfjhs0u_WF8K1oNrILTWmBzYwwl8FORTunCe93rOTtkOMoLKqplE8q6Qm6uHUsVyqA3gMnAgdR_I7PTcWkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=Ol7UmJ9DOxdbKKMFLOaxYOPJIywr9l9okyrDvCknzDiNGQ620fAJCaY1pqWrRgGHiWmCXOB55lSYMDN_EeQ_Dv7DKZycvl0IcvhHVsRyolEidUuNWdXiqqVabDlvBjmJSKfaSHFNoDV13_2VXssZkTqlGF3h5glTp0UoFQSQz7OibJrnhy7-wOYWAgutuwHO7wkw50q2V-0RcMpmzSOV2H_s6vJV0RRf_Yn_w_u29xfW8A3Za3dg2yYjmmsq3DK5SVtfjhs0u_WF8K1oNrILTWmBzYwwl8FORTunCe93rOTtkOMoLKqplE8q6Qm6uHUsVyqA3gMnAgdR_I7PTcWkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghjVJtEedxPXrBvEQ2FfwWmd7m3au0_pcm0ADW_eaUB2QbpfndeGMGrfWVEnPO7SacpvqVq3LO5VGqU2Nxuc7ieaZv0HZUBHRFsix-EeOCucfkiBQMnDj0_2d8kLO4X_Is3qunLgV5RqzRrm-DO9C-n8ftX-2jolA_Thou3NJCCjzq9qfpbh5PYjMHPeY4Hpvpyzj2k4E8z8fhw7YoUCccLMVD9SQXCqdRAvRJxusxrzcv_gBRJzgWu4B7fj6wka51XZwzsDRjmU7kSiIVypbnc_j31P6nXznxqZiE7icheORHCGJjzRzWLtdNhiBejB1zm3uwZUXvREbexUOb57Lf28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_ghjVJtEedxPXrBvEQ2FfwWmd7m3au0_pcm0ADW_eaUB2QbpfndeGMGrfWVEnPO7SacpvqVq3LO5VGqU2Nxuc7ieaZv0HZUBHRFsix-EeOCucfkiBQMnDj0_2d8kLO4X_Is3qunLgV5RqzRrm-DO9C-n8ftX-2jolA_Thou3NJCCjzq9qfpbh5PYjMHPeY4Hpvpyzj2k4E8z8fhw7YoUCccLMVD9SQXCqdRAvRJxusxrzcv_gBRJzgWu4B7fj6wka51XZwzsDRjmU7kSiIVypbnc_j31P6nXznxqZiE7icheORHCGJjzRzWLtdNhiBejB1zm3uwZUXvREbexUOb57Lf28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=BZc_iqkXyN-blfUFgQu-tcAQWK5B9OKypLAgxwFUnxjdkrqiIkfVJHKOlHn-_UbqOA6IsbNQERx6n80WM8YQYiS3JsfDpOSMgbZIwNuJPcKU-asfh6_bRayef7nMwTuasbKrq9JNfTe41YCnaHySzfzUmY0uv1Zdg88lPqx6wW_zALYfYXe0qGQSA4_P_wVbqDl4op-Q2_0RbRO_Oqys_oNoJ-63QVbVlv_r_TrVwuJSu3r6iagOlQ8qcWfOpftmCn7vwEOmRx0SbDz-52ztndrD4UgpJfQsW1RQs0DdNRa1YC443ZaEP5inZrCKw3Nrxm14gG6yMX6gbG2xGnoV2w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=BZc_iqkXyN-blfUFgQu-tcAQWK5B9OKypLAgxwFUnxjdkrqiIkfVJHKOlHn-_UbqOA6IsbNQERx6n80WM8YQYiS3JsfDpOSMgbZIwNuJPcKU-asfh6_bRayef7nMwTuasbKrq9JNfTe41YCnaHySzfzUmY0uv1Zdg88lPqx6wW_zALYfYXe0qGQSA4_P_wVbqDl4op-Q2_0RbRO_Oqys_oNoJ-63QVbVlv_r_TrVwuJSu3r6iagOlQ8qcWfOpftmCn7vwEOmRx0SbDz-52ztndrD4UgpJfQsW1RQs0DdNRa1YC443ZaEP5inZrCKw3Nrxm14gG6yMX6gbG2xGnoV2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCNg6lomeJjhsbyBk4A__fAZRI__UT3wbs44A9JnwmAC2W1WVm94v7wyeENZa4hHekaOt13BDYEL0qMFW95cmZiKGFSvY0hPOVugqmcU9926eT5-L9nxh2ZyXBsPOet2d_oyjyp2n2ujpPQ1iEKo40pWQWRD8czDir1u14kY3zGGTyz3fwCFSV6Q-DlfsYndJf0l1avfFjEHdp7wJ3hsR8CWfhNPVewbaxmBDu51oZ2j910cSyu9-CMGQEKXEPcDL9mY95fADl-cV8GQn-N9NFcN1007UdfoFUSDk0mpSUhYh19XR-_P9l2Kxrd4HxXCwt-Ub8VSIxxYD30ki2sxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LKXw3bXxWdV0UJiqdoeWbbR55EYddB25Ghvfg9xokjnPe366Rim9YXWz1zzJyIe8Y2RCslkf0ORRaFEzuYwpULLUhCf8iquMIQ-FjJE2anIerWJKkkeotu-tusvNfw9ZN1u0G3KnSZ5U67M3iyeeE6zA0Mv9tTdNfeNVfhRTzcIB09ElW7lfAP2y9YVzPjhEtuyJ3anLmr6ihwBpJ0iAeeKJljeRshizZE4TGKIoR623bVXMHXXBqOYN-Ztp0o2dFl9AeUsmhDN0md4vP5wSfKgqo2AgKI8SRugiE-GezT7KUomNC5oBzprRB2EDVgZBvWAmGo5Ae0rHK7-dEnIUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=PyuFcMcnyCN0Q1nJXpvWNjb4oPZ2445EbOMrl_pXzXyasqSE8rQFQjU_ESkDvBFmbTAUEzH6kEeJmXSeqXcpb6zjpB3z962AMcCjYaV-vCRYYfenP8VC1fclIuwswCbHNqTJeX4kKv-4c5hKVPzccXVi_Qu0CuV9KFUALWnlmsly_XrDH91xnMVRdBoDeCV4y_763rMIjSNyc8oTif4y3kDO6T9ezAZS_hUPhQNqGmuDE8XCKYt_lt_maMfmmRP1drN3zkxX1milGgsXR-SLkVal4MLAX9ivYIPsbsFGOcmhzFM34FvB0X0Y38kltwRa98AxnUBAUxz27hhuwAcqgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=PyuFcMcnyCN0Q1nJXpvWNjb4oPZ2445EbOMrl_pXzXyasqSE8rQFQjU_ESkDvBFmbTAUEzH6kEeJmXSeqXcpb6zjpB3z962AMcCjYaV-vCRYYfenP8VC1fclIuwswCbHNqTJeX4kKv-4c5hKVPzccXVi_Qu0CuV9KFUALWnlmsly_XrDH91xnMVRdBoDeCV4y_763rMIjSNyc8oTif4y3kDO6T9ezAZS_hUPhQNqGmuDE8XCKYt_lt_maMfmmRP1drN3zkxX1milGgsXR-SLkVal4MLAX9ivYIPsbsFGOcmhzFM34FvB0X0Y38kltwRa98AxnUBAUxz27hhuwAcqgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=JYtOZuLpwc8Uw6KvjfAmM8aPMmxE71MzqesgCZSzyyjeXOt1cFAETbFGK1T5akEYrKaz7X87QuVx8P_Q6H6kGkuAdYBdjxMGYv4XSjqDt0KViYhcWVKSoZgZl1N8gHnv3nDJZjHQFHhT18PGUI6F2SxBQeKWCkZXTtRUa1aAMlvC3MTlpNgYruRCeIHlltjR6Gjt2c7XjC_JqEmqE8ojmZRIWvORBwkN85w3noNVbqHV0Ae5UqYrImrOWL2Ca9VaeVQhs34RuaBS3xAp1M-N_0R45Zt2Z0mhRrv5nsp0Rj-FE9pwU_v3ahI1QZIBXEcHMvF9-DcHEY7EQAJ9muiJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=JYtOZuLpwc8Uw6KvjfAmM8aPMmxE71MzqesgCZSzyyjeXOt1cFAETbFGK1T5akEYrKaz7X87QuVx8P_Q6H6kGkuAdYBdjxMGYv4XSjqDt0KViYhcWVKSoZgZl1N8gHnv3nDJZjHQFHhT18PGUI6F2SxBQeKWCkZXTtRUa1aAMlvC3MTlpNgYruRCeIHlltjR6Gjt2c7XjC_JqEmqE8ojmZRIWvORBwkN85w3noNVbqHV0Ae5UqYrImrOWL2Ca9VaeVQhs34RuaBS3xAp1M-N_0R45Zt2Z0mhRrv5nsp0Rj-FE9pwU_v3ahI1QZIBXEcHMvF9-DcHEY7EQAJ9muiJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=v-rv07lQS70NzmwpP11t8OutVFgSve8Bjsvc2SIiE2dzzZRsEAdA0z30sqEMtZytXmP4G5FhBZWibGs6hcwPLNj4UDvhNEG04rAiC-nG5l_86s0UehYFPCi9vsg414nkFrELzYog-7_FKvhrNz83iORh5G3zFBulom2oH5p1vHuDnPleETKOCMPj1I3snotf0CpywWuFqI4pc5k4TMZ5_M33MVMzy9z__Jo0WFX9HIJA9mb0_rxneBeYacraUXO7b5XMhHJtmiVghq32Fdth5v-Xe87WBwDUGT9nUVx9gfbsdn4adEUjl3R5ahU8mEM8hvyPMBIm8F5B9sTLnQRVjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=v-rv07lQS70NzmwpP11t8OutVFgSve8Bjsvc2SIiE2dzzZRsEAdA0z30sqEMtZytXmP4G5FhBZWibGs6hcwPLNj4UDvhNEG04rAiC-nG5l_86s0UehYFPCi9vsg414nkFrELzYog-7_FKvhrNz83iORh5G3zFBulom2oH5p1vHuDnPleETKOCMPj1I3snotf0CpywWuFqI4pc5k4TMZ5_M33MVMzy9z__Jo0WFX9HIJA9mb0_rxneBeYacraUXO7b5XMhHJtmiVghq32Fdth5v-Xe87WBwDUGT9nUVx9gfbsdn4adEUjl3R5ahU8mEM8hvyPMBIm8F5B9sTLnQRVjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=jy23-JG3InCF8WMM_i4f32610bSSiIE0ZVzxn2Wjx4RNcHbXxR1SigVlrJ490Z9lLh_oLx2oyyySR9lcZ3OX4AfhHLRGd2Urn22ya7CWwnWR04jivRz2TLxqN7RnSv5EgDILIdTxlR_dC5jI-QGicocoOe4pFpmUqAQBK14N4OUBf5-6BTnS7FHXGKmHxEF8-ums1Yx_ot5CBVN_drcZpFViEiruO7iLZtJnyLkVeSflupx2LdtBHpt_c1sFI3YtB7o8ANDsiu1HuHzQSiyPdP61RIZ3CKB5zWFkF6Dm4MTVRIbylC9_TAqEJKPNfyHUhcmR_czIUXS-3yOl28bF2SV9_K5OTO3xssoPAd6q-086WVpofy1VT3aT42WRXWE7zIFtkD3cjsVJy_EUPCoOklMrKaYn9vz5iOcAMGzwmpqNA7Jwf-kVI-3qcLpUcla5dv41nj4qswOyoEuTGFUMeIhLQyp_anjEBZzpq3Mq5S5ezi9VmCSd8hnc7Mm3_y8IT5i9uEY3flx_XBKVhRuxFy4NSEYJQSbxnO0DCDvWTVnIr9bM5PbNVAOqxBDnxdxq1M0YehCQaZAOEmqxs_jkbXSaGq4hGWzfyTSXWWjP3huubgwZhU7dTH9pf58gwEiZnk3TsAvJk1Ga6hkwEuAWQ8n3Sk628JM3HDejhTIFjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=jy23-JG3InCF8WMM_i4f32610bSSiIE0ZVzxn2Wjx4RNcHbXxR1SigVlrJ490Z9lLh_oLx2oyyySR9lcZ3OX4AfhHLRGd2Urn22ya7CWwnWR04jivRz2TLxqN7RnSv5EgDILIdTxlR_dC5jI-QGicocoOe4pFpmUqAQBK14N4OUBf5-6BTnS7FHXGKmHxEF8-ums1Yx_ot5CBVN_drcZpFViEiruO7iLZtJnyLkVeSflupx2LdtBHpt_c1sFI3YtB7o8ANDsiu1HuHzQSiyPdP61RIZ3CKB5zWFkF6Dm4MTVRIbylC9_TAqEJKPNfyHUhcmR_czIUXS-3yOl28bF2SV9_K5OTO3xssoPAd6q-086WVpofy1VT3aT42WRXWE7zIFtkD3cjsVJy_EUPCoOklMrKaYn9vz5iOcAMGzwmpqNA7Jwf-kVI-3qcLpUcla5dv41nj4qswOyoEuTGFUMeIhLQyp_anjEBZzpq3Mq5S5ezi9VmCSd8hnc7Mm3_y8IT5i9uEY3flx_XBKVhRuxFy4NSEYJQSbxnO0DCDvWTVnIr9bM5PbNVAOqxBDnxdxq1M0YehCQaZAOEmqxs_jkbXSaGq4hGWzfyTSXWWjP3huubgwZhU7dTH9pf58gwEiZnk3TsAvJk1Ga6hkwEuAWQ8n3Sk628JM3HDejhTIFjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEVBaRayfsGlxIPbDNQIvqDrQIY5qGaYSZrRKCr5k-tS2zAk8XQfiKqySky1PtfsftifXQ69-02iJOws0GCPTpnbmEezRcydgY9eV_c64MX58SGmQq1piWhYrd6XtrghxpVnpazJ1CoVT6FxSybPLdx7lStnXojHoT4mTyOextTbGZqzeEqiZ0Sjfi9NkrpCAQL86fuVM1bh4BtmYJWJ6g7E0gXqXZll43u-UpSehpLOxoTJZGYKuTKjXCZz6rEWNbXplzMrhZxz5hszDfyK0j-uM3Mxd3APXmLXVlWA3B-4derUp9KY-1BSwWd7Y_3cpJ3qtfqWLudsbD38jDplqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
