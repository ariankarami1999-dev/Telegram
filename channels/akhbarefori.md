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
<img src="https://cdn4.telesco.pe/file/PvhePQbDwlmvTt6lD6Eoj88CkRUaojBHP4hmNUDqrZX0aUfDJ-_sCcjwFVNgstue2JXS-af4FWDkviMDnnWmHIY_iRyU6QkqiLKR_yvzNXZ71oz6-nERdoL1IzNqZh-9qTG8X7r5WSTBK4_i3B-Z-cy7ZPPassBiUVDxlmYitNbiV9mFknLJZKq4hWuIBkd32JH7ic9BCZbkjm5S2-KuQPzaZ0NtYVAE1ujdVHql83dA2fznMe4OTS7pET7CseVDuWH1kUk8FcW3ZrpjKHbaF9Tum8NvmD0GV6viddBHmAXy9Mfse32r0a-EeZd15t6595P37RSuL2_-i7DzimaX5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.25M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-689066">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvgN0_OyxX6RrRt4jzYCkAOjcDGQ8oR5pcNl8JnqHm7UM77sBU6-SUsbWD1g1vsNGgESzeUQ-s-suulefAqpH3WECxTo8RSxFbiadcIiikvmJzxtPdFKuxH184Ld16f2pk0DrraIyZi5v5O_gyVeniFdAgyO2rhQwR7DbS54ULlHxUGQ9ZiSg6DX8k_8Zvw3vVQ9qkd6_dDg5SM3M5H2RtdWLfdyZr5NNIsMAMzQmG3wKXZuTMX3Kyb_htlnXXimcb9R3KuUXe99T2f7A_yzo5e7yI6OScwW4bs6mAYPPKl2uvUsvEJ4aUiY0ffxen2TcuX6kJu0AsguL4zY-sAMLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هتل رو از جایی بگیر که بقیه می‌گیرن...
🥇
علی‌بابا، رتبه یک همسفری
🏨
کامل‌ترین پوشش هتل‌های ایران
🌍
بیشترین تنوع هتل‌های سراسر جهان
⭐️
بررسی نظرات مسافران و مقایسه هتل‌ها
💳
رزرو با نرخ‌های ویژه
جستجو در علی‌بابا، مرجع رزرو هتل در ایران
👇
https://albb.ir/8g6Rx3</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/689066" target="_blank">📅 19:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689065">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: استفاده ایران از هوش مصنوعی آمریکایی علیه ناوهای آمریکا
وال‌استریت ژورنال:
🔹
ایران از مدل هوش مصنوعی آمریکایی برای ردیابی ناوهای جنگی آمریکا استفاده کرد.
🔹
آنتروپیک مدعی شده این مدل برای تحلیل تصاویر و اطلاعات و شناسایی نقاط ضعف ناوها به‌کار رفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/689065" target="_blank">📅 18:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689064">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyvNiq39iodp6LJa2Bg_rTvmR72WYL_a9UZLFcIqTmSXBVJnklax4eEHo6-97E4wh337rES64GsCLjvdAokigsvRV0tmz1RyLl7OEGNits7ic9o3biR0IjRumAGIqfFtIrXm_iXG6vKOLMIN7rVbz1LqGq02-BKknXL1kBnzaYmZSMOlrEJVOe2ORdex1GAe1RFrrE3O5xn-YkGZpxL5bBvUt5Av-Lyrc7AhTqoMqMVsgwidIT3Ji2hJMZARQpPrNSV9y6ayQZ7OMvbmy_G9ZlH6aCz8Vmc8d5K51ZqqWqzVf2cKjff-Q9M0yrpuZSMcfLFujff_HHhZmj2VOYEZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ مدل قند خوشمزه و رنگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/akhbarefori/689064" target="_blank">📅 18:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689063">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تبلیغ دارو ممنوع شد
رئیس سازمان غذا و دارو:
🔹
معرفی دارو فقط در چارچوب علمی و برای جامعه پزشکی مجاز است و تبلیغ مستقیم آن برای مصرف کننده ممنوع است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/689063" target="_blank">📅 18:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689062">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
هشدار مدیریت بحران کشور نسبت به تردد و اتراق در مسیر رودخانه‌ها به دلیل احتمال سیل
🔹
این هشدار برای مناطق نیمه جنوبی آذربایجان شرقی، نیمه شمالی زنجان، شمال قزوین، ارتفاعات تهران و البرز و دامنه و ارتفاعات استان‌های گیلان و مازندران معتبر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/689062" target="_blank">📅 18:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689061">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVYTfRKdp3xFNfkvTep6WGq24QpIkod7Fk-JkGE96UUYfAKn1NJg_u4x_6o7PawOCrCmKyPdJZJtCB0eiMnLZMdKQMpD-IyhMWntDcWFx_g3TH46hieG3BcSdGD99xt-v6oStxaxTNrjfH3YfVDUeG57axqktN-q_OEubQ8xjD7BuUrGNYUxFyYQy4SGizghvIN4mEYugDp-szT7uV5i8F6MNfolmlW_LSMjj5EpAoyL_9wLjsJhq0lEMmgnfiI5hvHkdWQDHH9nCoggeg-RjDPQcpEyExdMijOZO8jYT9JJdB6rVlPkB5W9gjfmhf1iqzFCQOhkDSgt9DCDP9d87g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانبرهای عمومی کامپیوتر به همین راحتی یاد بگیر!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/689061" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689060">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P93OmX3s1LCM8jaNvs8SVS1PMOeWRLfLsceRDqyVkM8T0JqynXG5axw8rqjhBkkU6GNfGQ1Fq-YNVyOYfF5j9CZqX2_IdKYZ7Zteegz1GcL1_AGQuqIr-O3gS14NvfeyrviXCj3tInSwRVwGH1VCHM7yVMO-KPyA6zBIcl5cMQU6lX5z9ttVzblqiNrd_PZoxxYaBN3lm3anhLakFSRFc_iY1SfqE36xOKmokFaVnCRwT5Pv9DB3fuikbsYOAAso-puUaAYUK7f69SJ5KsE3cOdWrS4OyfIYvOD2wfWsJguosMFBPImGU_zlPj-G3R2IIgsDcatdX8cETDjSw8mLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/689060" target="_blank">📅 18:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689059">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaaafda3c8.mp4?token=cHJeNXsfv0zMDlvQal-4Sg3wI0ra8crJz8G476vYXHTy2EOVjr5KhGsFM76diFiidbSzvw31tpwAN8dxS_vhFR_13LOQ3JSMtXjrmgqnDs3cxwcq-vDpsLAqqn2Tt0tc9jCEeSUNLXCupQBsQntKwF6N0vvc9qZWblKXd2dXRpOlbFGWSeSwmyxX7v8n7OLIn8fFZoVJws0GA5NnlS5apT_OFZdDcQ0wAJYCBkWn3feYDuImiGGAoEXWl0ohiEWkgx9M9y19Qxss3A-_h_N8Yi9GWBLkV5ll7-resDn7f0VoP4Oo4bNI3Vb9FUcNN3ot3fpWf9u5FPhq05SjyPsy3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaaafda3c8.mp4?token=cHJeNXsfv0zMDlvQal-4Sg3wI0ra8crJz8G476vYXHTy2EOVjr5KhGsFM76diFiidbSzvw31tpwAN8dxS_vhFR_13LOQ3JSMtXjrmgqnDs3cxwcq-vDpsLAqqn2Tt0tc9jCEeSUNLXCupQBsQntKwF6N0vvc9qZWblKXd2dXRpOlbFGWSeSwmyxX7v8n7OLIn8fFZoVJws0GA5NnlS5apT_OFZdDcQ0wAJYCBkWn3feYDuImiGGAoEXWl0ohiEWkgx9M9y19Qxss3A-_h_N8Yi9GWBLkV5ll7-resDn7f0VoP4Oo4bNI3Vb9FUcNN3ot3fpWf9u5FPhq05SjyPsy3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای خرابی ماشینت رو خودت تشخیص بده!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/689059" target="_blank">📅 18:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689058">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYfzMgp7wkfYD8IDOsYa07E3ZsnEKoYNE1iyLOBLa7GuU6mQAPfyeYs59547M9S9blay0Esu4sUMIRywFsgZma18fyCemmooHXjar8F75Ms_5IjV9p9RwMMUlpOc_2E-FpX9wY6oHcKQ9mJhgdd8ib-dd5luf0jBc34NJNJWJ8yx90U3K0umuE3squq0Qyj9Z3VwHzKTBuYeHxTcGdgGf5aE8rmBMsydx18Tm42QcwKSePf84FLL359ocxE4L5qug_w7Cb2h8ZN6Q56PexNwPXSVsWv2j5hd34XSHbXqM0D3KCI-VSUVzpEdiUyVDRbsiy2IBnSTs7xwG5w0p-3vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهروندان کدام شهرهای جهان بیشترین زمان را در ترافیک تلف می‌کنند؟
🔹
در میان شهرهای مختلف جهان، لیما (پایتخت پرو) با هدر دادن سالانه ۱۹۵ ساعت از وقت شهروندان، بدترین وضعیت ترافیکی را دارد.
🔹
دوبلین ایرلند با ۱۹۱ ساعت و مکزیکوسیتی با ۱۸۴ ساعت در رتبه‌های بعدی قرار دارند.
🔹
تهران نیز با اتلاف سالانه ۱۸۰ ساعت از زمان شهروندان در ترافیک، چهارمین شهر جهان از نظر هدررفت زمان است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/689058" target="_blank">📅 18:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689057">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای گستاخانه ترامپ: ایران حامی شماره یک تروریسم در جهان است و هرگز به سلاح هسته‌ای دست نخواهد یافت./ الجزیره
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/689057" target="_blank">📅 17:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689056">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مینو محرز: واکسن آنفلوآنزا به دلیل جنگ و تحریم در دسترس نیست
متخصص بیماری‌های عفونی:
🔹
سال‌های گذشته، واکسن آنفلوآنزا طی چنین روزهایی در دسترس بود. شرایط به نحوی بود که نه تنها واکسن در کشور تولید می‌کردیم، بلکه واکسن به کشور وارد می‌شد. در حال حاضر، واکسن آنفلوآنزا به دلیل مشکلات ناشی از جنگ و تحریم‌ها در دسترس نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/689056" target="_blank">📅 17:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689055">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
گزافه‌گویی وزیرجنگ آمریکا: ما تنگه هرمز را کنترل می‌کنیم و به این نبرد پایان خواهیم داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/689055" target="_blank">📅 17:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689054">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/689054" target="_blank">📅 17:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689053">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a5c03b6f.mp4?token=aL7QGtZEo1-vO4yumLsM0QJZN1s3mAX-J--wrcZ53QEC38uulvfEyGftlWkKsfmzcJZU3tX70IxV7BDtjWOieqCKYQb072GDD4FjSfsvm4pVwJdNCeh8Xu61H4DkRiUvw8V-TTtiI9RCzfTz6rhJfTQVsb2BIiH3OXtxy81uhhgDkETvYbVRq2wkhxzCbfoH8xrejJMKIdk-CziEOI8npHsVwQtaWlZESVlqrDQVhLfLYZUqkCaj2L2FlkzH8j-QBmvA2gb1O8usVJRA2__jrVQyfqYLvzby4KeejSzjvAZbuDWX_2T_cahIYmqmzU5XAE4BROW6Lr1W3SMNqLRVEhgZl6Kpq3fkVn4LnUwCX2WXwAnyGSXPxZz9cyx9qrHj27PEXXisZ5UW_0Bg7c4sATc3JBF4UdrWSyOrGD9BSpjQPtTXA3sSh_zwfutA-TIFFAVAmvQn1ELH88NvFNVhBPZLdHgkWjmyW2S1G6h-H4T0tljfW_wfmYsOd8oV0dD5W_YyAVB0Z3SC-k149VrlWiBqbO4JrqpNoGr3NAUxg7Cb-KpBEt4B9ngh6oiy6442D7wueO9uL1m-XdmKDR_3j41O7GoHPx5rI0BxOPozJf1Puge36SK1j_1Z7potgGI9eb3ujJmHgV7_y32wtWOk95sBCZupRTaxg-0M14rTTRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a5c03b6f.mp4?token=aL7QGtZEo1-vO4yumLsM0QJZN1s3mAX-J--wrcZ53QEC38uulvfEyGftlWkKsfmzcJZU3tX70IxV7BDtjWOieqCKYQb072GDD4FjSfsvm4pVwJdNCeh8Xu61H4DkRiUvw8V-TTtiI9RCzfTz6rhJfTQVsb2BIiH3OXtxy81uhhgDkETvYbVRq2wkhxzCbfoH8xrejJMKIdk-CziEOI8npHsVwQtaWlZESVlqrDQVhLfLYZUqkCaj2L2FlkzH8j-QBmvA2gb1O8usVJRA2__jrVQyfqYLvzby4KeejSzjvAZbuDWX_2T_cahIYmqmzU5XAE4BROW6Lr1W3SMNqLRVEhgZl6Kpq3fkVn4LnUwCX2WXwAnyGSXPxZz9cyx9qrHj27PEXXisZ5UW_0Bg7c4sATc3JBF4UdrWSyOrGD9BSpjQPtTXA3sSh_zwfutA-TIFFAVAmvQn1ELH88NvFNVhBPZLdHgkWjmyW2S1G6h-H4T0tljfW_wfmYsOd8oV0dD5W_YyAVB0Z3SC-k149VrlWiBqbO4JrqpNoGr3NAUxg7Cb-KpBEt4B9ngh6oiy6442D7wueO9uL1m-XdmKDR_3j41O7GoHPx5rI0BxOPozJf1Puge36SK1j_1Z7potgGI9eb3ujJmHgV7_y32wtWOk95sBCZupRTaxg-0M14rTTRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی قدیمی از نتانیاهو در کنگره آمریکا؛ طرحی که از تغییر فرهنگ و سبک زندگی ایرانیان سخن می‌گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/689053" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09abc8db34.mp4?token=pbvEzNagOPerwB46ZyVaN3rtpDyIQ50ANoBOQVl-516kmy88uVAf1bmc-quvoMrevOHPPkwkOOrTCjde6QNTNURlUUpzQLp-Qkm-XLijcUV5VEM2eBYVid5hTFbCcYLJ0TzcDI4w-dCxN0PcAC_O_02WELC_T_ZrtijmKlwMxjpacQ1z5j178Y_MK_3mH0PTAJfYUSAmUWlbl6Ct_LmtkH_cKokaGHA2tPJ-Hiuf6Y0MMtM6FgXviHtONTIbPE2jgeV_dM3Bc4VThjJQ-NcpLctpoElUheNbQW5iOPj3DqTZNkLYxtjrbyNGipuoNsQ4fsHp73_Oz7To-rElFt73ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09abc8db34.mp4?token=pbvEzNagOPerwB46ZyVaN3rtpDyIQ50ANoBOQVl-516kmy88uVAf1bmc-quvoMrevOHPPkwkOOrTCjde6QNTNURlUUpzQLp-Qkm-XLijcUV5VEM2eBYVid5hTFbCcYLJ0TzcDI4w-dCxN0PcAC_O_02WELC_T_ZrtijmKlwMxjpacQ1z5j178Y_MK_3mH0PTAJfYUSAmUWlbl6Ct_LmtkH_cKokaGHA2tPJ-Hiuf6Y0MMtM6FgXviHtONTIbPE2jgeV_dM3Bc4VThjJQ-NcpLctpoElUheNbQW5iOPj3DqTZNkLYxtjrbyNGipuoNsQ4fsHp73_Oz7To-rElFt73ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غیررسمی| وضعیت مرز بازرگان/تعدادی از هموطنان‌مان پشت مرز ترکیه ماندند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/689050" target="_blank">📅 17:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
وزارت خارجه ایران: روز دوشنبه با مشارکت عراق و کشورهای خلیج فارس، نشستی در مورد تنگه هرمز برگزار خواهیم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/689049" target="_blank">📅 17:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689047">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQeOr99T268VBCoNwGTSY4ttfqhvXwefgGwP_Vipe-Zx3L1FNuXwfyOKZ_L_BheytMVh_WxyUsFWb_PJYBohat7AJosj9n0FECcphYzTglSuvbkKCdtp6MY3AQxRGQBGCeH4aWNaGp9wHYCt-6LfZkZ7h80U4pyX-Jkx3jWCga5P_xo7epwzQOxLyki8mgbtsp88i0Gw3DA8IPQYIXIRCpon2YoB-JFhUsykEJ4P6dpo81PHQEyllHpLAGG0LEuQrd7fM5opb-xst_wrX31PUTBitF3saGlNCewS1d0Ce9Ov6bVC1ijF43G_mupZ-as6YQo4JsNNE2MfUuF77z9YBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از انفجار در خط لوله نفتی شرق–غرب عربستان در جنوب مدینه منوره پس از حمله اخیر یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/689047" target="_blank">📅 16:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689046">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd837a201.mp4?token=NyeIEqPLAw5s0Z0cgaUFVKUWMRCxZ3OpyzbZDdLCQ80V9VxInNIfp8xrv3J-c2LWnadr0CwOjqJWzZwnafFhbe7J7nhxYPchjsfKtWpgX2_RM_la8aK4mgKZVWNf33NKG33NSMaUH7KDOXIo8H4glfAwQO4CtnAcf53MWqb-4Q6RUh006GdvAqnvHA0hMa7db6t3whtTHlwhaHf0hCfK0gXgCgywa20AYH-CjUGeRcu5wfgYAANi2Jyqox00gM9MxMVdRZXQUPpbQI0r0oOJlHdVh8ArxD1VizLegrmaJRKOELdWjE0xOsIBPA5pusz-KUq71Uw1wOZpzcBxltvR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd837a201.mp4?token=NyeIEqPLAw5s0Z0cgaUFVKUWMRCxZ3OpyzbZDdLCQ80V9VxInNIfp8xrv3J-c2LWnadr0CwOjqJWzZwnafFhbe7J7nhxYPchjsfKtWpgX2_RM_la8aK4mgKZVWNf33NKG33NSMaUH7KDOXIo8H4glfAwQO4CtnAcf53MWqb-4Q6RUh006GdvAqnvHA0hMa7db6t3whtTHlwhaHf0hCfK0gXgCgywa20AYH-CjUGeRcu5wfgYAANi2Jyqox00gM9MxMVdRZXQUPpbQI0r0oOJlHdVh8ArxD1VizLegrmaJRKOELdWjE0xOsIBPA5pusz-KUq71Uw1wOZpzcBxltvR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیفون تاشو اپل؛ دوربین نامرئی زیر صفحه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/689046" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689045">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
یمن: ۵۴۰۰ کیلومتر را آزاد و ۹ جنگندۀ سعودی را سرنگون کردیم  ارتش یمن:
🔹
نیروهای متجاوز سعودی از ۶ شهرستان در تعز و الحدیده بیرون رانده شدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/689045" target="_blank">📅 16:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689044">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxWTU1j-qU4R1j3-eh3y1arMds8bcAixspHNmwI2SR0HLUBJ_plYTfr5VFJCod8HKR6wVhTAHQJEQBy1XBAHOeKGEnLqqKSb0Lrap9FVOIs5JuKZsC4JtJjyrUe-SOntvnkCbdyX2zktmiKxCVlAV_L8x4OY7OGdHT8Q_q80enrGt6tR61vwkzz6zQP6GFJA0Tjupc2gDwuENY2o6DKkze-kpe9kdrSwcqagmHZCoBGTcxnYxALIzZ7HGs5x8wSYIvAYC9TJb6vdGfsySQBguYjf_jiVH0acCo_vDKpu_UAwc3A0xo_PrXKL2ldV97WkW6SpFVp12dDeLQqg5ZmleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: جهان روزبه‌روز اعتماد خود را به نظام مالی آمریکا بیشتر از دست می‌دهد
وزیر امور خارجه:
🔹
وزیر خزانه‌داری آمریکا با خوشحالی به خود می‌بالد که می‌خواهد ایرانیان را فقیر کند و اقتصاد ما را به فروپاشی بکشاند. اما در عوض، او درمانده و ناتوان در برابر افکار عمومی قرار گرفته است؛ در حالی که جهان روزبه‌روز اعتماد خود را به نظام مالی آمریکا بیشتر از دست می‌دهد.
🔹
بحران ناشی از هزینه تأمین مالی بدهی‌های آمریکا تنها آغاز ماجراست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/689044" target="_blank">📅 16:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689043">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e945671e.mp4?token=a10QDNdzpJis2HySyeRucV1vle0R8BLEK5bAvejQExSH0fv5ch5r1eZBW5zvlix4O_O5TAOwhtx54AHVoMw8jNqq_b5ArO8D9QWUtoBOUwtQ4IHvKpMroE2dmx2rAwcgZClIjXzjK-KQXwdFPlKh3SgusA2AC9IwkCi27yqmqJIgx4CUR9eoZpYV2XiJVj_jUYE82bGZ2vMtXOs9QIIzkk6gXxRkCsu9_3HIUFMDP6GbGxZ4LklQCUPNZUW2MHkJnyJJpc2Txv0sjFSz2k3YSNJ6XlHONcnn8UG1UdN8P2HPxsj2Yh3Rf7k00s0ZIO1iBfTGFd0R4mQGlvgnDwXaZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e945671e.mp4?token=a10QDNdzpJis2HySyeRucV1vle0R8BLEK5bAvejQExSH0fv5ch5r1eZBW5zvlix4O_O5TAOwhtx54AHVoMw8jNqq_b5ArO8D9QWUtoBOUwtQ4IHvKpMroE2dmx2rAwcgZClIjXzjK-KQXwdFPlKh3SgusA2AC9IwkCi27yqmqJIgx4CUR9eoZpYV2XiJVj_jUYE82bGZ2vMtXOs9QIIzkk6gXxRkCsu9_3HIUFMDP6GbGxZ4LklQCUPNZUW2MHkJnyJJpc2Txv0sjFSz2k3YSNJ6XlHONcnn8UG1UdN8P2HPxsj2Yh3Rf7k00s0ZIO1iBfTGFd0R4mQGlvgnDwXaZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسنت: ایرانی‌ها تلاش می‌کنند مشکلات اقتصادی در ایالات‌متحده ایجاد کنند، با دستکاری در نرخ بازده اوراق قرضه، یا با دستکاری در قیمت نفت با استفاده از اکانت‌های توئیتری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/689043" target="_blank">📅 16:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689042">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
انتشار بیانیه‌ی نیروهای مسلح یمن درباره یک عملیات نظامی گسترده و ویژه؛ به زودی...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/689042" target="_blank">📅 16:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689040">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/461e74698c.mp4?token=PwC1fG6rpWLSN4wHFtuXkNxrig9ByTI9bTjEz3l_Q2T-RCW21OffynWmSEa2-z2HKX1lmYQFAKMyGDfLcfBKPwlzbOt95UmWckjUitq2YupViBvfthmMictlfWJtStNgBLzGAesdB_qVAbbn9Sdc2KoG-YRa5VVI2zl6l4kV4LYwc6fJ8L6FcTSAV49MEGqjDRt4XHMKEKM4JFURQheMcp02iC_o60L5cthuwflwxhGpU0ILlc1aB2wayV4B5B5g4sc1385XYwG8XrD9S0PsjlU3NxDVpHeRBi-xL6yzosjODIFYu4TNyBQZYjQVIvC1SwiD0yDZYVV6kZASiaZLCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/461e74698c.mp4?token=PwC1fG6rpWLSN4wHFtuXkNxrig9ByTI9bTjEz3l_Q2T-RCW21OffynWmSEa2-z2HKX1lmYQFAKMyGDfLcfBKPwlzbOt95UmWckjUitq2YupViBvfthmMictlfWJtStNgBLzGAesdB_qVAbbn9Sdc2KoG-YRa5VVI2zl6l4kV4LYwc6fJ8L6FcTSAV49MEGqjDRt4XHMKEKM4JFURQheMcp02iC_o60L5cthuwflwxhGpU0ILlc1aB2wayV4B5B5g4sc1385XYwG8XrD9S0PsjlU3NxDVpHeRBi-xL6yzosjODIFYu4TNyBQZYjQVIvC1SwiD0yDZYVV6kZASiaZLCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پوتین: کشورهایی که فشار تحریم را علیه روسیه و ایران آغاز کردند خودشان با افت صنعتی و کسری بودجه روبرو شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/689040" target="_blank">📅 16:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689038">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پزشکیان: یکی از پیشنهادات ایران برای بریکس راه‌اندازی صندوق بیمۀ ۱۰ میلیارد دلاری برای پروژه‌های بزرگ زیرساختی و انرژی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/689038" target="_blank">📅 16:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689037">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
عکس یادگاری سران بریکس باحضور پزشکیان و پوتین در کنار یکدیگر
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/689037" target="_blank">📅 16:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689036">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf797f04f.mp4?token=rs93nVbfm6Wjg4FVpWm_Z8UaZzONPhvjBzMEt8bnl_H2MpRN70-LZDFUenYBR28c5Hp6eCymw8LXIWGWDFtRBd7-MujUgA3qF1PtQNDX5TxkipeSrG7tkQsoydH-HuWUt120gxjpFVy3G25z4ba4cq7Obs9BuNpuKgs9Srde9FaFlfYtvFVxHboQKX4yqhpIKJQem1ORuEjC5LiPjaK5FXgDP0Ef1XlTRUI7lvv5AJwq8yt37iEWNk0As3Fw6VnSJ4QN4beYLbVWbBp-gXsRL299cYHAbbzR72f6j9mDQ9J9WebkWhwHbpngLhiHcrotTqqZdw4d44ypBPhvMYILYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf797f04f.mp4?token=rs93nVbfm6Wjg4FVpWm_Z8UaZzONPhvjBzMEt8bnl_H2MpRN70-LZDFUenYBR28c5Hp6eCymw8LXIWGWDFtRBd7-MujUgA3qF1PtQNDX5TxkipeSrG7tkQsoydH-HuWUt120gxjpFVy3G25z4ba4cq7Obs9BuNpuKgs9Srde9FaFlfYtvFVxHboQKX4yqhpIKJQem1ORuEjC5LiPjaK5FXgDP0Ef1XlTRUI7lvv5AJwq8yt37iEWNk0As3Fw6VnSJ4QN4beYLbVWbBp-gXsRL299cYHAbbzR72f6j9mDQ9J9WebkWhwHbpngLhiHcrotTqqZdw4d44ypBPhvMYILYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس یادگاری سران بریکس باحضور پزشکیان و پوتین در کنار یکدیگر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/689036" target="_blank">📅 15:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689035">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6466595315.mp4?token=XfsTm2GtQCXpUA1-xVNuRZlL1UFqzqLAWHBNlvj6ViYTTc3ZZDgx60UELzNaxJIg4F5bjfblEI6bWt8I6EyGN7e8cL5DvlRJqGfNbSPnk65Xd56LIbw-HGnhpsfijxOAZ63kPIqA6uZThSyBMgV2CRHlmPOILYtv-vA-VsPXaTiEGCuVCCDEOBcoBWlEZ04dQsUIOPRKNg15Dxsxi7Df5mzaLuTMvLxD9sFfSlQwRPZASLgRc74as61Tn5CflRziKwuQpuKbxwJgkDXorDY56FATJUYT1yPrg5fkBlz_2K1NAlQD_oMHyIexSPivtm5WGo6I9GhRVu1g8WBB6kc8sINx5ic3WxCVtB2LzqYCb1amPzkKdE6gcebquZKiG67KcoId1Mq4s1SYtUXqYaXiVEd8gn64lVm57jw_1fQB9AQ2gHpAsZZe1kDXJzxf7ggb9ciAfJosEa1q3QwILwoW-KNfVquvwmoFv-3jwD9cm_jyhVdijg0DA5OgFliZHHbemu8Ll39W6whp9q8HiZL8_L0bU2GjjX9LorhmjiMziWND3p1TNCrvbz8QxANcYY1lmUsc6l6-ppJFBSOYUXZm_VaXtPLD7vDkQVvxjV7lLnBY1kpQ6jVmIpdup4Lf2rAh9ksH0IFILFK6Mg7Sf37DcMP7WA7Ai8yRfkZ9_VYTbP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6466595315.mp4?token=XfsTm2GtQCXpUA1-xVNuRZlL1UFqzqLAWHBNlvj6ViYTTc3ZZDgx60UELzNaxJIg4F5bjfblEI6bWt8I6EyGN7e8cL5DvlRJqGfNbSPnk65Xd56LIbw-HGnhpsfijxOAZ63kPIqA6uZThSyBMgV2CRHlmPOILYtv-vA-VsPXaTiEGCuVCCDEOBcoBWlEZ04dQsUIOPRKNg15Dxsxi7Df5mzaLuTMvLxD9sFfSlQwRPZASLgRc74as61Tn5CflRziKwuQpuKbxwJgkDXorDY56FATJUYT1yPrg5fkBlz_2K1NAlQD_oMHyIexSPivtm5WGo6I9GhRVu1g8WBB6kc8sINx5ic3WxCVtB2LzqYCb1amPzkKdE6gcebquZKiG67KcoId1Mq4s1SYtUXqYaXiVEd8gn64lVm57jw_1fQB9AQ2gHpAsZZe1kDXJzxf7ggb9ciAfJosEa1q3QwILwoW-KNfVquvwmoFv-3jwD9cm_jyhVdijg0DA5OgFliZHHbemu8Ll39W6whp9q8HiZL8_L0bU2GjjX9LorhmjiMziWND3p1TNCrvbz8QxANcYY1lmUsc6l6-ppJFBSOYUXZm_VaXtPLD7vDkQVvxjV7lLnBY1kpQ6jVmIpdup4Lf2rAh9ksH0IFILFK6Mg7Sf37DcMP7WA7Ai8yRfkZ9_VYTbP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس سابق انجمن واردکنندگان خودرو: یک سال تمام هر کارشکنی که دوست داشتند علیه مدیریت خصوصی ایران‌خودرو انجام دادند
مهدی دادفر:
🔹
روزی که ایران‌خودرو را به بخش خصوصی واگذار کردند تا یک سال هر کارشکنی که دوست داشتند را انجام دادند. از شکایت بگیرید تا کمیسیون اصل ۹۰.
🔹
منافعی داشتند که ایران‌خودرو را دست بخش خصوصی ندهند. سال گذشته با توجه به برنامه‌ای که بخش خصوصی داشته، تیراژ تولید محقق شده و حتی از نظر تعداد تولید در سال ۱۴۰۴ جلوتر از برنامه هم بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/689035" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689033">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0d825838.mp4?token=GvT_1AVQCD_w4UYGk00ALuymvRajamZnhKIl2dZjRHHMJHWUR-bVLJxj9k4YtGVwhOO-MHtPwCW87frEAdBZGX8gecvG5fwar0o-i9Ts_ocCCiTmlgMqJTpQBMTBjyu9RGHvajUramI07qeoFW-FPSivSpL63506jFP4ONwq9_4B7yOb55FIuH-0LNBdEl-AtFWAZHld8cgGmmdzoGk-nSy_kVV2JiDk973G2WOVHx-KZseL2MezdJwNMPXF1vRkX_AeCg-ORcKZFsqYzT5ON6vivP9hwNoioSCpaLKDaHoTQ1DZO12bPbLA0gIUED_KkuAJfBhUFf0aWdepmII3DgWGpaIPyxaTPYh-WdV6IGPpr0k8WJMqLSvSyZuamXUNoGtxvjQr7WHtkSlAGnfarJHx2zL1kgWhKWIsvDr6csQIDPphVoJ_tI67bLWTTnXEp8O18nnytU8ij4J480yIAtSXco-Cp3-YwGR4ujj_1yalSHndNjh4TXBKbOdf-vz7xOoZkXuRT212v_o7X2P_ssbZ6m9cHo_UBasOmkbXhqIJJJilrHUXV4Hr8-4hN-XwA0TI7kXXtWKM6H6vJI2gNKp1PDYsmIudeO_DjDaixLae2kqskbAaGFt153zCrqic8tiuS0rzJ_xCzKXLBNuAhJzwmO3tI-gTPII8KzwVnEc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0d825838.mp4?token=GvT_1AVQCD_w4UYGk00ALuymvRajamZnhKIl2dZjRHHMJHWUR-bVLJxj9k4YtGVwhOO-MHtPwCW87frEAdBZGX8gecvG5fwar0o-i9Ts_ocCCiTmlgMqJTpQBMTBjyu9RGHvajUramI07qeoFW-FPSivSpL63506jFP4ONwq9_4B7yOb55FIuH-0LNBdEl-AtFWAZHld8cgGmmdzoGk-nSy_kVV2JiDk973G2WOVHx-KZseL2MezdJwNMPXF1vRkX_AeCg-ORcKZFsqYzT5ON6vivP9hwNoioSCpaLKDaHoTQ1DZO12bPbLA0gIUED_KkuAJfBhUFf0aWdepmII3DgWGpaIPyxaTPYh-WdV6IGPpr0k8WJMqLSvSyZuamXUNoGtxvjQr7WHtkSlAGnfarJHx2zL1kgWhKWIsvDr6csQIDPphVoJ_tI67bLWTTnXEp8O18nnytU8ij4J480yIAtSXco-Cp3-YwGR4ujj_1yalSHndNjh4TXBKbOdf-vz7xOoZkXuRT212v_o7X2P_ssbZ6m9cHo_UBasOmkbXhqIJJJilrHUXV4Hr8-4hN-XwA0TI7kXXtWKM6H6vJI2gNKp1PDYsmIudeO_DjDaixLae2kqskbAaGFt153zCrqic8tiuS0rzJ_xCzKXLBNuAhJzwmO3tI-gTPII8KzwVnEc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه جالب از بندر المخاء؛ تصاویری از یک مکان در دو مقطع زمانی، از حضور نیروهای پیشین تا کنترل آن توسط انصارالله
🔹
ویدئوی شبکه الجزیره نشان می‌دهد بندر مخا که محل دپوی سابق سلاح و تجهیزات مزدوران وابسته به آل‌سعود بوده، اکنون به‌دست مجاهدین جبهه حق افتاده…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/689033" target="_blank">📅 15:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689031">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f384f506b4.mp4?token=Bf-2rBKe6SmqxG6jYcimFwOvWoUMRnTLX6G1ZxV1-3x_OfNj1Psb91sC1KUeWXxnQxC9E_PEeSA2cZoq3wqt_mAGj7CWtgUqPquqIeRJxARfcfXfynxNZXOIYGeWwuXC1vgSOsA4SVpOVASu238sNJKfdlk_S2ITf7PXXTZUTWCfodkZOBizRduWLLe8FpQBuRu1zFqDMvr_XtWKTjIveVi-_d-dnjh0Rq-PWIjJnE8ea-A0s4qQ4ul1-7LqJypYA3xZjPX9QvueAtXeIpk-YtV-pWqG9nvJS9fOFj5TKGTkebCIjZ93PAdmLjiW27belzAw1980kxHMSwv1xV8c3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f384f506b4.mp4?token=Bf-2rBKe6SmqxG6jYcimFwOvWoUMRnTLX6G1ZxV1-3x_OfNj1Psb91sC1KUeWXxnQxC9E_PEeSA2cZoq3wqt_mAGj7CWtgUqPquqIeRJxARfcfXfynxNZXOIYGeWwuXC1vgSOsA4SVpOVASu238sNJKfdlk_S2ITf7PXXTZUTWCfodkZOBizRduWLLe8FpQBuRu1zFqDMvr_XtWKTjIveVi-_d-dnjh0Rq-PWIjJnE8ea-A0s4qQ4ul1-7LqJypYA3xZjPX9QvueAtXeIpk-YtV-pWqG9nvJS9fOFj5TKGTkebCIjZ93PAdmLjiW27belzAw1980kxHMSwv1xV8c3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا چگونه از میان شن و ریگ جدا می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689031" target="_blank">📅 15:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689029">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7d8296a4.mp4?token=DF6WVEF6FRInAx2hwykP4jRujBHn9dnY9LmmPqxzn2zzAygSiyU54VeCsR3oyq4uvFn9JzUx4UdMnfHMCAb8HoVCGC7kUSWrxKvJyI1p55IoLtbZqIwpNxYkMjEuKpBjxVzUV4_P_3xTy_ZeyStjnNFC3c6YVzqbfRdlE4V-rRYBvkIbWSvW2wWNyBmHYNqaj6RXB_8TCwCQgt-sXqSBGb9r6V8Gjb0mFWAcPvAfpMv4cglEcTfxTcRYBvBkkmz0MFXPvCffZsM3DbtFLwlnzuF_ePzA_gfDDnUHyzxZhovnuNuK9yMkWDeW-E6TzFag4npPCUSeyyTl82zZcZX2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7d8296a4.mp4?token=DF6WVEF6FRInAx2hwykP4jRujBHn9dnY9LmmPqxzn2zzAygSiyU54VeCsR3oyq4uvFn9JzUx4UdMnfHMCAb8HoVCGC7kUSWrxKvJyI1p55IoLtbZqIwpNxYkMjEuKpBjxVzUV4_P_3xTy_ZeyStjnNFC3c6YVzqbfRdlE4V-rRYBvkIbWSvW2wWNyBmHYNqaj6RXB_8TCwCQgt-sXqSBGb9r6V8Gjb0mFWAcPvAfpMv4cglEcTfxTcRYBvBkkmz0MFXPvCffZsM3DbtFLwlnzuF_ePzA_gfDDnUHyzxZhovnuNuK9yMkWDeW-E6TzFag4npPCUSeyyTl82zZcZX2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ جذاب از مجاهدین یمنی و ابراز ارادت به رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/689029" target="_blank">📅 15:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689028">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oy9PXT2LcYwt2yjktYtsjYo_YARHzVkBpkyYxFINM5p5vho_MZek-yWzC2w2H5XstUnKRndF5GuoiJNCmcYxDLwnQzr61GSChlvaq5lCI3o4k58o5gO_bO_qH2k1GmKx0juDBZFV9QaYFQJJQ92yKSkxlJvrk5da9ZxpIyYD3TjWQ1V60zM44GNVPfiOGLDoIyJi-_qIDSxD04jf7JtMgT9S_Er5M-GwbO7cavZnGoTo842Mmd_dvtLG-LMZTCVFfVjEkr6k3HRhXWB-x61Ft5dL4FEIgESoMtQwpDGgVfGtSjINhl0xWxZTC6AuIJ915XyOjyy6KOY-K5yjJFeyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبح پنج‌شنبه ۱۹ شهریورماه ۱۴۰۵ محمدعلی سالاری از مدافعان امنیت کشور در جزیره بوموسی در پی حملات آمریکا به فیض شهادت نائل آمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/689028" target="_blank">📅 15:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdb8a90c6.mp4?token=HCxq-Uyz1jBEKmSCfGRH5AmzSE4gO_RIqYSJ7tiLnWDS7hsalyAnQh2Ghca9zenGR6WwL_f6oKxKFm1A_tLgo1uXthuOtGWVxmutmUuZzv6jBffnMKtCvBi_Pp4Wd9qViCBGM_tL9YR3U8sZ53brOzRqrcR9vfHcjiOvf03OQ68Rd5jcTXCxMoRSDZmELJU9zJTCx9uEpU73J5brTbYsnz9Zv6U-LM2gJ2fsQB5jxU9oqEYqsU5-KtTn74vbymm4xVS1H-GiGKQS33NeIxx37pPX3EUZ8jnm-fpHefTWo3xwAn5jz7-d0HuCDjdYpRQWuEScxtxAyp7A94E9Xo6K8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdb8a90c6.mp4?token=HCxq-Uyz1jBEKmSCfGRH5AmzSE4gO_RIqYSJ7tiLnWDS7hsalyAnQh2Ghca9zenGR6WwL_f6oKxKFm1A_tLgo1uXthuOtGWVxmutmUuZzv6jBffnMKtCvBi_Pp4Wd9qViCBGM_tL9YR3U8sZ53brOzRqrcR9vfHcjiOvf03OQ68Rd5jcTXCxMoRSDZmELJU9zJTCx9uEpU73J5brTbYsnz9Zv6U-LM2gJ2fsQB5jxU9oqEYqsU5-KtTn74vbymm4xVS1H-GiGKQS33NeIxx37pPX3EUZ8jnm-fpHefTWo3xwAn5jz7-d0HuCDjdYpRQWuEScxtxAyp7A94E9Xo6K8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/689027" target="_blank">📅 15:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
با تایید رسمی نیروهای تحت حمایت ائتلاف عربی، ایستگاه دریافت هزینه عوارضی انصارالله در بندر مراد و جزیره پریم (میون) دایر شده و زین پس عبور و مرور کشتی های خارجی ملزم به دریافت مجوز از انصارالله خواهد بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/689026" target="_blank">📅 15:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad652c96e6.mp4?token=OnOpI7hxGJCQo-yUlS0dBvEYATKFJOjlwyV2Vo5h9BMMSiPAnyohQxgObl1kkjulGLbRVZjXdgGppSy_1eLCaD5ZZF-o1_mJzsCOVfp3pcQitgcZQvKe9Tz_DIKYmnGkZb_1YCQTOqNpCLx4h0Bz-r9NAaUJJaGaeiJQCCFmlCxWNzPBQvV71UBJDR6EkWoJ4kQlDMI8EzDhPnYqYg64WOvfG_YgL05gMGfmgam_B95VZL1_Lm7d2JDO--MQ6GrVuNb6uCKF4qJmrgTmKDlHumhMNjVxG2bqZtL9Y53CZ8wayl7xSYJmR0Tz2poarpObX7DVP1arvoRG1u3WYMo_mKkHoOdiHVciQkwq-P9ThTmG7Ok0rAPe7MoyLALFKWmxiJWMv8t-pkMFYnLf0dESGgJ13QbBO6GPg2ydPxj3d4qq_vUjm1Ij_SrZNo80FmKkRVXSkSzLkeNTVpFMMmgpTqh4UWAX2DKGDwTf-bIulTCqMJ95bzql97Xj9h5lNkxp1vXEuyrclV2Tzke6yR0TQDICtHEbLNTGBPZHx9ZbFyx8EuygSu8JfMH2nRu_qjaY6j-wKsOYcK_xe3rVsPCXcxuhmrFGd9lhZth4ptZus-6O2N6iPKaNNYMohgFNdXs9iUZ8kVu2aXpRV3A2HFnxBb4V20ouGCc_OuCSlhtUTq0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad652c96e6.mp4?token=OnOpI7hxGJCQo-yUlS0dBvEYATKFJOjlwyV2Vo5h9BMMSiPAnyohQxgObl1kkjulGLbRVZjXdgGppSy_1eLCaD5ZZF-o1_mJzsCOVfp3pcQitgcZQvKe9Tz_DIKYmnGkZb_1YCQTOqNpCLx4h0Bz-r9NAaUJJaGaeiJQCCFmlCxWNzPBQvV71UBJDR6EkWoJ4kQlDMI8EzDhPnYqYg64WOvfG_YgL05gMGfmgam_B95VZL1_Lm7d2JDO--MQ6GrVuNb6uCKF4qJmrgTmKDlHumhMNjVxG2bqZtL9Y53CZ8wayl7xSYJmR0Tz2poarpObX7DVP1arvoRG1u3WYMo_mKkHoOdiHVciQkwq-P9ThTmG7Ok0rAPe7MoyLALFKWmxiJWMv8t-pkMFYnLf0dESGgJ13QbBO6GPg2ydPxj3d4qq_vUjm1Ij_SrZNo80FmKkRVXSkSzLkeNTVpFMMmgpTqh4UWAX2DKGDwTf-bIulTCqMJ95bzql97Xj9h5lNkxp1vXEuyrclV2Tzke6yR0TQDICtHEbLNTGBPZHx9ZbFyx8EuygSu8JfMH2nRu_qjaY6j-wKsOYcK_xe3rVsPCXcxuhmrFGd9lhZth4ptZus-6O2N6iPKaNNYMohgFNdXs9iUZ8kVu2aXpRV3A2HFnxBb4V20ouGCc_OuCSlhtUTq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه CNN با مهندس هوش‌مصنوعی شرکت آنتروپیک که روز گذشته از سمت خود استعفا داده و هشدار داده است که هوش‌مصنوعی ممکن است در آینده‌ای نزدیک بشریت را نابود کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/689025" target="_blank">📅 15:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
از حفظ خدمات در روزهای جنگ تا بازسازی خانه‌های آسیب‌دیده؛ روایت همراهی اسنپ با جامعه
شرق نوشت:
🔹
مسئولیت اجتماعی شرکت‌ها در سال‌های اخیر از کمک‌های مقطعی فراتر رفته و به بخشی از فعالیت آن‌ها برای حمایت از جامعه تبدیل شده است؛ اسنپ نیز با اجرای بیش از ۱۶ طرح در این حوزه، در مسیر همراهی با جامعه گام برداشته است.
🔹
در جریان جنگ ۳۹ روزه، اسنپ برای حمایت از کاربران و حفظ دسترسی به خدمات، به ۳۷ کاربر آسیب‌دیده ۳ میلیارد و ۵۱۵ میلیون تومان کمک بلاعوض پرداخت کرد و ۱٬۵۰۹ کاربر راننده از تسهیلات بدون سود بهره‌مند شدند. همچنین راهکارهایی برای مقابله با اختلال اینترنت و GPS توسعه پیدا کرد.
🔹
این همراهی پس از جنگ نیز ادامه یافت و اسنپ در تأمین و بازسازی ۲۰ خانه آسیب‌دیده برای زنان سرپرست خانوار در هرمزگان مشارکت کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/689024" target="_blank">📅 15:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689013">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-EpyAwddiKEJW0ywcjxbk_Fmk1hcDyj-cNODsqgiUsdra5FJpekzT8ibhfTvDWgbvPjNKu3XHkr9_g_ccke4mIrUlIMEcECAe8fdQtXqrLg2mmXhMxjwbM3rroqoboVLq7qOy6ZgJrtAArZkEo68tf0oWHhCWp6vIKlpC4uG2PN8yYDEn18Dk9kNlf9sGfNYrIHJVUhNrBzwNWQlyroYOzZEe3ZFsrdX9oEgGlR5Z8ZvcrEqdqtZr4MQXxrJUnWp12HrjbAI8WYITzwG6raM-3DG7JFCHtseWMSB3rmsKp3zB0PK1hgt0n9YYbqcSBP123MmsRwgWhHma3UThYrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGnERH8A1vXINKY5hlP4xp3pSKtiXwS_W2fJ0lG3zyOoStMiDsaJN2OOSh59I0GYz8LR0Juj5FaahCuJY4cYo9shE3pVh_V8vBIpZGpv9KxmachGhN-yga4T-m2n-vEOkPMx7LpkeA5xbhrzKLS_No-DKX6oe9nVlsIDmVuOWW2j6cdqwu4XbJEidllrzebFbA3AIe9iVQ_iaNTU-wSVHqgtWDL-9xkYelVIDlj1oQg-XwoRIiV58b8tTyD2KR8zI-5PeEoTn2aCojdhZ_gd7S13y13mzAccwmCZJ_MGav0DgqS8SIvu66JbdcsWh8tuoijfPX-lu2KN2wapqYKJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oknFwXbTsZhRdy353AKGxLFWmMXdEnr5M7vG_jg4TEKpi8cwPZEn7afck0tdFdEXTK1-wPgJ-2XHOo_hbTgBJFa2iRs0wBeQmLa-kYZ15qwWyshYPwXrA7BfAqHUxxgmZifRImJpShx_ThUPU_p02Rhhv8LF5K9hqTolext2BBBRF1qO4DpXtkX_bI1O90P9oVTcaCPzOzadjhmRIcLFLraCXgcg5BjFautUQPZG1GVMm3qrB_MpVRurlqZYPMHbdiK-sQEDt5IgOaC-1uYQEnFQ6iu4Rg_Yf5lyT7LRdgOOk17yJ1Z0qMB_TONqDzCSvQWpmkTWStgHzia0dky3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Knm92FLT9-DCk6CT7B2qP4sMhJjESlXzX3_BodiV0B6Vyxb_ZrX2IgEGHRgAHEizvAd6_MTeuWpWt8-ZJaohwyHau2RqRohZ_TbxmCSTKeoce-q7XUSt0oTyF-zspzA4s-GfrHy3Ri6Zih847JSSL0UBPTYgTu9iO2KG2KgvyYGOsQTjQAQrL6uW99wrq-lWd_RpyMel409QyaeRvmXuf0iGL16N4_YHfKrdPzzikirG-bt25Cs08BfaKknM6S_VUJGWIhUvmMgvIWNA32lS13F7mWfucmL9AopyZmgMT8aKz3aiKpnSvseTGwqfTBD-n7f0Wal4Wb0jEyWUfFbujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7r2hdMAA5U0X493e5uDSAd2uZWYClEPq2jDEz_z4-ciLk5UwknsRJB-H9JJ4vrpZcVMwCnM2YMSX9Ww-xSA-51jcaOGlMqy92EmYRyPMy1Hkq6pwFGuhDZ_i_eTJht1zPfBPinULqt8bK0vlwlExfUSWFwcJ4yMO2xUu_H9GuY_iXz2wiozfPLtu5zxWl0fiRnWXipF-TNSEO5vc_ZE7IVQVOq_Q88JYHn5ltKn4kBKHSbbdR4hwm_PBfGlhE6bTbBOwMdTlE-yd_E2ti5GnYMUs3o17TVesPAmD5DR1tFj9p_PDamuf_gbSYmT_MtB8EUV9Fll1j6dWoPRkgoEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qciD9i4ZNCGqVAAqJa7EH2PdZbeHhVniHjV8aARBa9AIvYgj5o1M1JC5WhR50aT_JuHrmM88X-pUiDw7y2kwdtCN_i5qQ7Dq3qoAYajiT7YcY3cUltNHUY7kh2McMyzUqHhJr68VEnVGmRVSCzjtBiZDjKcoan7bfTLiW013d6oCFly1-JQ1rO67kRwahIG0ny533Apbu6Z4EPFo0tPEqXlz1htUT8bQY-x-G7TR1tnk6AX-d0NB4lgaSZAj9xCXaNkvmoFRm3TbAcvq_EfMxhY0w64-fLgPIoEOlRxS48BfIIk-nQBre4Y_TNYf9GOwOd7L0MW76SNrVgJRjnKYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q0hUf5BJewZHGVu96QHohzLJTRIbVq1HmpMoLZFfV3LXhWRPkkv0iYHEt9b9Pr7HUl9Y-HDY7-CCeQ6zMKayBwUwnNWgapP3F39WIev29AF9Nh7Z938ehNU0554Fcby6zTF26MfDAxJhB0OuR2Ez3dl0SAu_ekCiRSzFyR642YW8shvxzAyJIemburtou3XyKl4s8jsB5FCiqW2l1f7fBhF_BBRW2m3LZvAZQ6EeywGuSJs3KG-h6P0yyn4GbYPx4VLK8Yf1pjkLViGw9nh9BhjfZZ717xgg3DnmJeEsYUPgwzEWQG81IG2yWeVjSb9TVvBx_ZF3AxK3O_JiaoHS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/viR8cqUEBUVxLhF_yDa8d-ggFo6Tzicn5BmeMKfhY8viXi-ios3dlQzuZ1TGlGR01hGJk-9C7LhXE25iNVcB0OP3Oet-Tk18PDYlS1gWn98yowayBAR_e4thFsu3oRlETGTNHa9s2WVMNur8oiLjqUktD86pz3HuZbFidQ5OtnCfJvff-SF8RkZz_HK8kJS3LnFENxFcSLEUGntL7eo2FAGjl5pV3W3AgnrzjL4WSqbhSFjfr31VCy1bEbyCHhSDieKCwxxFa_XAxszE2yNm0G6nRqyoeiFtZXcc947n8l1r5sOnQPfMIzEtHAyf5OrYtMM4Udt8SAwyR-9HDX9dBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPISHbvLsoRRpDJXoGcsYE3H6eA-NB2c3Xj9uWAXKFmxCUM0980YY70HmuhKsG3BSifXnSyGZGnO6mulHu7xFUqp4yB76U4aPnMadvHqpQxJ9APoht8jmK3Cpw3dOHAdS7YVxiF1njEzFCZUdTo5nwvZOR-wj_SvRISJEs27M9hA3basEld8izphBpKQjkeYg5A0bRajGRA0Pm1WtI5VHWQZP45n_vquoZ3jM4N67D1l61z3Aj4Oxu7d3UIFxEbyuoaflAkl5iuVCLhircdOJZ9-BHjXE5UE2nDKjfAVdJzuF1JBeyblcrjymcKyc72L1sI61FOMU15tiHvlPxi_pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
بازتاب دغدغه‌ها و مشکلات شما مخاطبین عزیز برای شروع سال تحصیلی جدید
🔸
روایت خود را در قالب  متن کوتاه  ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/689013" target="_blank">📅 14:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689012">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrLu2zs8VpY83Alf1dIYghISgzBgAwzHFaJXivf0sIvOp66h0z17ZEDxK-SCZFlt5tnkoEYnQZA8l36HKjjKJq6yqFxkaYQHdtcsbNlSKLeZZfhRVyKWwbNZJmuCILlDxjfDWoZ6fv0fUVYGVIA13dhA03Td4sCnBbxTBvhRf9VOfBcVz0YyayzPl2MVk7QYpBDoysTAyrMhuYXcF6n6U2zuvZ7U5wmrkj_PoGeTYvojyxl-sQsn0ZhQWcnSD96lUQ2-n0XWg8MSa5eXnNCDIitTM8MTkCSw9rm5oOHI-XbwGvRaQfzANW7gx4_NFKjd0kNGnIxClh-bxKcwI3HDYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: فتح‌مبین انصارالله ثابت کرد امنیت خریدنی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/689012" target="_blank">📅 14:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689011">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e5aee1199.mp4?token=gyysFzaAD3D3qVg2vc31-h7N_LdW60LzFGYLb-OOXGmsHbJ7BRCNx1t5Y-mzG7e95kpePNUJAe_bEM_PWedz1rpgZjxuqgR2bBIv1y0l8c_0if5cH_gqZ6XaTxjr1d3DTYsbWNVBBGn5zF3ubrr_gKRgYbMWwDXeC4ARS1xzhKKs7YCH4teHW6_d3slrzmQzWMaz7lUICAjK86tRDaxZMVboKVzBrGRCJkSq3cbr4tGxMKQFuyLqXf6kJgJinovbG1UrML8gJYOPR5N45-jZX2abnS06Y3YgB4ssz1aVBLkcr-SCVp3GKAYBW44P2Hs18XF-sD6mGRH7er1SQyJH5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e5aee1199.mp4?token=gyysFzaAD3D3qVg2vc31-h7N_LdW60LzFGYLb-OOXGmsHbJ7BRCNx1t5Y-mzG7e95kpePNUJAe_bEM_PWedz1rpgZjxuqgR2bBIv1y0l8c_0if5cH_gqZ6XaTxjr1d3DTYsbWNVBBGn5zF3ubrr_gKRgYbMWwDXeC4ARS1xzhKKs7YCH4teHW6_d3slrzmQzWMaz7lUICAjK86tRDaxZMVboKVzBrGRCJkSq3cbr4tGxMKQFuyLqXf6kJgJinovbG1UrML8gJYOPR5N45-jZX2abnS06Y3YgB4ssz1aVBLkcr-SCVp3GKAYBW44P2Hs18XF-sD6mGRH7er1SQyJH5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/689011" target="_blank">📅 14:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689010">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خبرفوری
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/689010" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689009">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/injAyme6zg01s8m7wqugvIWkeC8YNpfU9oAls-C3XrFTPbro1zgHDLIgekDTz4W0mEea6V676WYwKwqct3ACJpJQ18jmK5Bc0qJLecInJk6VBjItPrDfwMJcHPXyiiadGAmaZJnsMNFZAFmLpazVCB7bPX5-8Tl_7mOlwlCffen01slpkuM2YoH1VqCboNVBy13f4pnSumlUmN9vYkWAMSO74KQgEpLSnTCWVjwKH_8B8V5_h0780J7b2sMbsVKFIFSvPwhpQDmvgoekHCvqbejPzfXc79Ri1Xuv0SDiKAjg9jBdXH5nEoK-ZdSYJDPiKVv6S67tPZT1jj6NygkEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار بیانیه‌ی نیروهای مسلح یمن درباره یک عملیات نظامی گسترده و ویژه؛ به زودی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/689009" target="_blank">📅 14:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689008">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda9e6a4c5.mp4?token=BlSfrjhjNmnHHxaluuj16OZHC9lX72YauMI1ck_s5Bczyd5hgXMVXDwtqul1x1_qVN9wrSRRBesp8WHxd6hUETSn-wC-bQr-yoTC5V71BjGrJhV7c_6o3RCUyJS4LdIk-06IgZ_bH4JnqhlspMXJ8jJ3lMtq8IiQZCWhM0xqIIZKT84-JrXD13o6o-z01qXJlcyAjBwgjsKl5XkvqQGq8FtP1sPhwXtibMX93mCy89LPdEQjNkCKyYlsR-wzbmTbNwinKALzfZYtD9G83BW9yaEakLmM6OgQ0zD0EYdWT8eDZB74Qy0YHDfOdtlpcheq6s337-iurj6qVkDSTNcztQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda9e6a4c5.mp4?token=BlSfrjhjNmnHHxaluuj16OZHC9lX72YauMI1ck_s5Bczyd5hgXMVXDwtqul1x1_qVN9wrSRRBesp8WHxd6hUETSn-wC-bQr-yoTC5V71BjGrJhV7c_6o3RCUyJS4LdIk-06IgZ_bH4JnqhlspMXJ8jJ3lMtq8IiQZCWhM0xqIIZKT84-JrXD13o6o-z01qXJlcyAjBwgjsKl5XkvqQGq8FtP1sPhwXtibMX93mCy89LPdEQjNkCKyYlsR-wzbmTbNwinKALzfZYtD9G83BW9yaEakLmM6OgQ0zD0EYdWT8eDZB74Qy0YHDfOdtlpcheq6s337-iurj6qVkDSTNcztQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرفوری/ یک شهپاد آمریکا امروز توسط نیروی دریایی سپاه مورد اصابت قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/689008" target="_blank">📅 14:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689007">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
در فصل تابستان امسال در آلمان ۱۴هزار نفر بر اثر گرما جان باختند./ در سراسر اروپا ۳۳ هزار نفر در اثر گرما قربانی کمبود وسایل خنک کننده و گرانی انرژی و عدم رسیدگی اورژانسی به گرمازدگان شده‌اند
🔹
عجیب است که آلمانی‌ها با حقوق فقط یک‌ماه می‌توانند بنز بخرند، ولی از خرید کولر ناتوانند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/689007" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689005">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
فرمانده تروریست‌های سنتکام برای بررسی تحولات جنگ یمن به عربستان سفر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/689005" target="_blank">📅 14:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689004">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84db58b274.mp4?token=FMjog-lXEkMvDct7oFr4S5mI2AK5HVDLGFL1qqcrs6nnA_Z23mgtvVbuO5BIdFOf0Zw7AJsNctg4Wlvx5khWiITEtEUM95jPfqU4JHnX9XwVn82WSleRdcrCyg1zNSANK_jxPhUeAFHZYGNWzxvGWh-fB0qY2K40NJ4sX17gXO4TUpBBi2529Yr0PE7Nm3rwTgr3TSKLDQA3RoqlpkZ-lJc7LjjGjbgt1DMFDHktYSqpWUYcnUqkFCOLsf_nLMc9AfPQmzf-HoWrx0eFhnn1xtMBUDX7gATlcEfxd7qGepH53uBvbOo0QcS2tcEgxriAzy4kxzf8zu82h1gKwIHrmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84db58b274.mp4?token=FMjog-lXEkMvDct7oFr4S5mI2AK5HVDLGFL1qqcrs6nnA_Z23mgtvVbuO5BIdFOf0Zw7AJsNctg4Wlvx5khWiITEtEUM95jPfqU4JHnX9XwVn82WSleRdcrCyg1zNSANK_jxPhUeAFHZYGNWzxvGWh-fB0qY2K40NJ4sX17gXO4TUpBBi2529Yr0PE7Nm3rwTgr3TSKLDQA3RoqlpkZ-lJc7LjjGjbgt1DMFDHktYSqpWUYcnUqkFCOLsf_nLMc9AfPQmzf-HoWrx0eFhnn1xtMBUDX7gATlcEfxd7qGepH53uBvbOo0QcS2tcEgxriAzy4kxzf8zu82h1gKwIHrmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک فروشنده داشت از جنس فوق‌العاده شلوارها برای مشتری تعریف می‌کرد و تضمین می‌داد که هیچ‌جوره پاره نمیشه؛ که درنهایت این شاهکار خلق شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/689004" target="_blank">📅 14:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689003">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD_g5AEcchz0UJ4qsF0C5al1FubVc23SiJreiOFi5-3JpjotY6yXBMpiIPcCaWV0TkCTrgSRZI9FlGv5545VJ0ROPfLkLdtB2YjHRx9_g0QWM0NQOpKM_pQqMjpQJsG8fgk54ipW5Vb1nD6cAmn_SLga1TrZsrRNDF82UgGHlDYM0qQ-5pmoMU6JJ2jMSSlm3adcTEGsAVFQfN9M4AMizzzQS0z-CT0jSyApIDj_fVsjGsUejHRNCPJc2bwtHMV_hRcQ4x-xNREwHa2Y-4D9xCgM8ZI0EdhpWRw8dHv_cQi440_gaOUwIKxUqmCMM940cTtlaRdqxdIXJZRfO8s0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه الحدث عربستان نیز اعتراف کرد جزیره استراتژیک پریم به کنترل انصارالله درآمده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/689003" target="_blank">📅 14:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689002">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFIwniBS9PN2V5K4LwqUaYxnA07luPKZqTwA_U_6eIzFsfZQZh20dKrlBGX05N7ZOwkWb7NCy7G2auiV48mFJjin0aD_IdyvvZO6GP2Ez6lXq9fggHiaVPHUshF04V3uIMIfQo9wQSP_07Em7JD8UseTi2UYhGuwNLDXizgbKIVM7IA7O1c4KYpeH_UIEllMmsLqlhLJFyH7uP5LzZI7Ny9rIUTRk6ezihq7WGHHoEbwK7664KvX1hWmEQNbnNMhx2mshoqbGq-xzxfwv7TvftpiwpQuCnomW1oFmRI73HobsNX_BfG0fP-zJK2jNSeiZtTI6YDZLY3UBLjamgcHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه را یهودی‌ها کشیدند، آمریکا اجرا کرد، تقصیر را انداختند گردن افغانستان و رسانه‌ها هم سناریو را نوشتند؛ تمام!
🔹
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2098341193172341123?s=46</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/689002" target="_blank">📅 14:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689001">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb2b81260.mp4?token=unBXAYKLX5tCIKkhV7XdPXteNiaWr9ZO9JnnB-MgeverloMYyIxp_YIgmizyQ8oxkUwDOsmx_ldFvyNRvax0nCAsjSgDzgL0YlKTISknoKvcfwmVa8fhZhM-_rGSgWJB-KcO6ejGmMkvHCz0Wp8XouNanUcd2-3KAUUyUtpIsyyGOf_zo-24_oxwWVakx_IT-aFtfask6xBbkqBZDa94Sf0dvYMMVOVNmDWIdf92kORbiqqT3x0PEJAneN5vzRQ-SRYhyN524GqEJAwRCxHA9ADRLLNM6sJ_PAjhFAi_wSbsNFECSCsePfEXvylGTOkx2W9AbJNgSmVNZnag15u8GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb2b81260.mp4?token=unBXAYKLX5tCIKkhV7XdPXteNiaWr9ZO9JnnB-MgeverloMYyIxp_YIgmizyQ8oxkUwDOsmx_ldFvyNRvax0nCAsjSgDzgL0YlKTISknoKvcfwmVa8fhZhM-_rGSgWJB-KcO6ejGmMkvHCz0Wp8XouNanUcd2-3KAUUyUtpIsyyGOf_zo-24_oxwWVakx_IT-aFtfask6xBbkqBZDa94Sf0dvYMMVOVNmDWIdf92kORbiqqT3x0PEJAneN5vzRQ-SRYhyN524GqEJAwRCxHA9ADRLLNM6sJ_PAjhFAi_wSbsNFECSCsePfEXvylGTOkx2W9AbJNgSmVNZnag15u8GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشخیص چای اصل و روش درست دم‌کردن از زبان چای‌فروش تبریزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/689001" target="_blank">📅 14:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689000">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=PuwcNiKnOrkOYF-9z1JXs-DIWkhL3z_-vcysLJ83aoxWmjuTYGSF-gcTbzmjgpefobbHlTtKbY-juaqwE5ipZ3BMO3x5z2nQ0f6IMf4-uvqNF9CriEMPkRp7ewxATPTdVSMRDPXqjYZtP5G1rBl4RQaKH_ZS8veQArHlLc40GBiSG9pPI1kWz1-DZUUE85hdSboJdPYhRrKz7WHONcTie9PuVYUxZR1Pji4tGJE-OtxfgmFzyEePpRE_gD1i1oZn9dp94dQGJHazuvK3eJJJiSTeyPy4w529LD0tCpTK-UsGPd5R2lyKjBzezeh78uEHG4TjW5RTBJGaaZFbIqjv3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=PuwcNiKnOrkOYF-9z1JXs-DIWkhL3z_-vcysLJ83aoxWmjuTYGSF-gcTbzmjgpefobbHlTtKbY-juaqwE5ipZ3BMO3x5z2nQ0f6IMf4-uvqNF9CriEMPkRp7ewxATPTdVSMRDPXqjYZtP5G1rBl4RQaKH_ZS8veQArHlLc40GBiSG9pPI1kWz1-DZUUE85hdSboJdPYhRrKz7WHONcTie9PuVYUxZR1Pji4tGJE-OtxfgmFzyEePpRE_gD1i1oZn9dp94dQGJHazuvK3eJJJiSTeyPy4w529LD0tCpTK-UsGPd5R2lyKjBzezeh78uEHG4TjW5RTBJGaaZFbIqjv3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎉
فروش فصل پاییز شروع شد
🎉
جا نمونی !
🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
*
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه*
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/689000" target="_blank">📅 14:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688999">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
ادعای العربیه به‌نقل از منابع پاکستانی:تهران و اسلام‌آباد برای ازسرگیری مذاکرات و کاهش تنش در همه جبهه‌ها رایزنی کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/688999" target="_blank">📅 13:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688998">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90319df618.mp4?token=RVN3zXsWdYe9mezGgtu6nB7BPpMBp3gIDjq-lNEHZkv81aicsLav6KbC_z471JXcBWytqWo_8zFHx1Ym_griw8Rs8m9BF26MNXRXTeDFCdhxwZ3hEpGThDPGxMAtjxcWy10nHNtLtvE9lN4_ClnNfbw1PYwPnAPQRBei8YEA4XAKLCKa8ggMicLERg6tL2gcNIvPvvh3OtCs0M9QDZD8_JM81kp2Mxt98hJ10hKCatAMVSbovw1lGqOcFibmri6_gstnmCwCcWk3_LwwjixO0fRI_XWHKW2cTUlNV5U4njKtTfd1OsPpWSlgM7tsZHaD3U4PrApsSqGV4HkQe1bwp3r1Wh8mX-Q2nMSCgdUWSqrzGAEYtrPtGgNoZyJ7V6gHB8SP58EubDDBpUBrT03GTpkhwBhZr1Xp2SzgWhOcxG8I3mnJ6lT5bhZKGHF4dZNZHnwJOYTUIEf-iKiy7lEz5QMxfkxJrUisAHT8yvu3-YxI8eDipxaCcgRLEHaqpFBxeenl7BZfLkEt-jgmb4gA3jS7_dLRCVBEyiWJinQaFZCDjv3xdXpY0EQeysJ1ezvIdkRW9PgxdSvyJ4mn_f67EbJ_72EvkQ6V0ef9ocBb9a1jdRevWYIr9EzjqKbygWANZm4ftuv3cLH7VECtJE7n_Lseu6anj117QLsM5bm8kgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90319df618.mp4?token=RVN3zXsWdYe9mezGgtu6nB7BPpMBp3gIDjq-lNEHZkv81aicsLav6KbC_z471JXcBWytqWo_8zFHx1Ym_griw8Rs8m9BF26MNXRXTeDFCdhxwZ3hEpGThDPGxMAtjxcWy10nHNtLtvE9lN4_ClnNfbw1PYwPnAPQRBei8YEA4XAKLCKa8ggMicLERg6tL2gcNIvPvvh3OtCs0M9QDZD8_JM81kp2Mxt98hJ10hKCatAMVSbovw1lGqOcFibmri6_gstnmCwCcWk3_LwwjixO0fRI_XWHKW2cTUlNV5U4njKtTfd1OsPpWSlgM7tsZHaD3U4PrApsSqGV4HkQe1bwp3r1Wh8mX-Q2nMSCgdUWSqrzGAEYtrPtGgNoZyJ7V6gHB8SP58EubDDBpUBrT03GTpkhwBhZr1Xp2SzgWhOcxG8I3mnJ6lT5bhZKGHF4dZNZHnwJOYTUIEf-iKiy7lEz5QMxfkxJrUisAHT8yvu3-YxI8eDipxaCcgRLEHaqpFBxeenl7BZfLkEt-jgmb4gA3jS7_dLRCVBEyiWJinQaFZCDjv3xdXpY0EQeysJ1ezvIdkRW9PgxdSvyJ4mn_f67EbJ_72EvkQ6V0ef9ocBb9a1jdRevWYIr9EzjqKbygWANZm4ftuv3cLH7VECtJE7n_Lseu6anj117QLsM5bm8kgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غیررسمی
|
وضعیت مرز بازرگان
/
تعدادی از هموطنان‌مان پشت مرز ترکیه ماندند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/688998" target="_blank">📅 13:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688997">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ابوترابی: وحدت ملی فتح‌الفتوح ایرانیان است
حجت‌الاسلام والمسلمین ابوترابی در خطبه‌های نمازجمعه تهران:
🔹
وحدت و اتحاد مستحکم ملت، هماهنگی میدان، خیابان، دیپلماسی و خدمت رمز اقتدار ایرانیان است.
🔹
امروز نقطه ثقل راهبرد دشمن پس از تجربه شکست در میدان نظامی و سیاسی بر هم زدن ثبات و کاهش تاب آوری ملّی است .
🔹
دستیابی به رشد اقتصادی پایدار از
مهم‌ترین ضرورت‌های امروز و فردای کشور است؛ ارتقاء سطح رفاه عمومی و افزایش قدرت خرید مردم مرهون تولید، صادرات و افزایش درآمدهای ارزی است با نگاه به این واقعیت انرژی از مهم‌ترین نهاده‌های تولید و پیش نیاز رشد و توسعه کشور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/688997" target="_blank">📅 13:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688996">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5b8d5aea.mp4?token=hd4q-QebjKdtOcvBR1qnzK59LMY_IbTlG8JxTvoItMupAKJFCSe4sG1K7DRRU2JCCUVnAzNk3tKK2FRPdvonK6BqRRog3x7xw0kt9AUUd29JYFyR26pEDDuWoxMVTwa4xMNpVzqRcxpoqrXE94ewqRcLLW39MhKh4iGkhOnnvQGteZ5J9S1pS_FmRHbCt3Y5HU6bbrO9tWT9c8OJOjpanC24JnCiEw2OC0Li_UGxOw64l3AkfJ7VjiRvh2y4-GhZLSx1hSJ0klBndvSqVp3hL0q4VZG0_-21W9K8vhKwYsHGBL-ZB5PJ8HaUiwx_ir7Z2Pg7p8dyPob-qRtqvRB60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5b8d5aea.mp4?token=hd4q-QebjKdtOcvBR1qnzK59LMY_IbTlG8JxTvoItMupAKJFCSe4sG1K7DRRU2JCCUVnAzNk3tKK2FRPdvonK6BqRRog3x7xw0kt9AUUd29JYFyR26pEDDuWoxMVTwa4xMNpVzqRcxpoqrXE94ewqRcLLW39MhKh4iGkhOnnvQGteZ5J9S1pS_FmRHbCt3Y5HU6bbrO9tWT9c8OJOjpanC24JnCiEw2OC0Li_UGxOw64l3AkfJ7VjiRvh2y4-GhZLSx1hSJ0klBndvSqVp3hL0q4VZG0_-21W9K8vhKwYsHGBL-ZB5PJ8HaUiwx_ir7Z2Pg7p8dyPob-qRtqvRB60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شرایط عادی زندگی در صنعا، همزمان با تصرف کامل باب‌المندب توسط نیروهای ارتش یمن از زبان یک شهروند یمنی به زبان فارسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/688996" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688991">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFZ84dqzVINcJWV--Obyl7h78hNfNCyMknW-S9np4xQ_BNkPNa3R5uLXD0XVtUpjpE6FRcIrf90Ti9gGlG5cxgLZ4UFpiXTKtAnPZmNPlvTJx4t5RZzL67xM5-cqg73SfuVZuwuNwKvNeE5CSQcTWJZenmq5xYFjCHImQ-4txlSERR7heFTkMAOxjeUo_k4HB462k-8TZqffMgGgJqygivkpLeVB2-_ooSmXJ5p2YWWwbxqVdQGEx-m3Mq6LrzNc3oHqW4k2d_pdZzwd4jmXWsfi2DCJEAc5WBUSlnxXWhA-ir4lf8ePXRAUu8WWQVIvaSi_ZH21af0IqGYOTZJUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nB2fNT6Z1QhyJf2LXnflMogSV9Vfe4zXXDYzJfD372nFzVHGdM9oAvFdjlYE0eeKsbyWJtBPLdIwhdLPhNnRVJRwkbb9qDclBdJ7fsrpP0EvrFYnG0L4qEMuzqT22V6EBlAjNZ7C6-Y2g6Zjy1KtZwA0HR32Eh1d3_MjhgGJH2bDCjbdKSWLbXmxM7b_KsI1sQwbc1rjMG6e-Lw5BHIQdc4wY_lTvH2W1RSRRDy5wHcDd8R1Zk8OkivX5VMEomsUcrFXAFrnNseHQwP7hef4sSFGZrg6kaaoCFz2oHuVvxsOdpQ1kHQNXr8Kv_QV_1_e4safAtG4OFcB2BPE07GLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYOOr-SIE8cUUAjV1ifncYaryTVWKUqEE_5lSOgHa_iyU0GWftDX6lkCYAZud6-pd-KLoAlbcgsjHs3Tj0fwfvMGIxSpyPOqt-Z9I7HfMVfesy3X_hh8q2scj7INbx5gsVdm2bv85QJqO80FFk6k9IF8bAFkvtHkORM2mqhe5nHOYQXcI2VLnsiRHlPNUyF-ulIah0c34tGdGsf7R7852Y6M9be1RAt1iu6VXGmNZw-6H9p54Yix-Z-Im891otkwzDQTmm_BSij3-hLoJUSE51ybDLNypNXdG534Mufh3jKYP_awKIJ5BWN4uzQcU2vOiVXDDHfncFtHUH4WEy19zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXb8vaaEycgF2IRBvBp7lEAiJczCXNPzfb9cB1hs7EuEAMRIm1XyXma0XJKR28X1SS_b8WxwMas2t6sGt93SExw59-LfKQLElonlq8icNBzlAHVhKiQR58ZKHjJmX1Uhm5aH2nBMfKb29a8Jw6hReP5HBXXXrHg-FgKcd4cPIzDeoXnzXMFM1MTJxiGewfxmhswou39LJSo0hTlPs_xkYGTKA1DLWtceFBkCts_mKq72Tmj_BC_UHGnoqGUAOxZhgJ0BGysawWQ1HIpKeXYCynuxQMQchqXkFshQgXOV18R1C0BtHLGlIRlBpEfmOU1BYs-9ga_3k_52OBnanIjOlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deQGE-A6dO1xfGk8DV5j-YJ2AntBwh9syhNM5LK-1bUlSpzl5EyGA-cHmuDRQbEt-ajM9tAafHfOPplwYGhq7h_NXMdJW6X0qpw6MjqDl-JfhYyx4dG5n-yXz8OhWAkG0GgLkwGvx023CKSbYNJ4q1dnroNeRcmOOVJz7epuTXCOWOrRaBRXJYVpfO8JpUUFPIsMQy_4OA6-5MTAG-0y9_Y6SUbixJUtswzvz006nQakstE6RlF0-HOxldWfZ6HnsKtvwEVDIgTuRZqNI5q4Pjd-1nNaEef_LDIYZe_uPcbz4xgaKwURjipBG9W8xTKv8MiqKRKoP-rX2yd6ddsr8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نوشیدنی‌های عالی؛ جایگزینی برای نوشابه‌های مصنوعی و پر از قند
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/688991" target="_blank">📅 13:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688988">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
لغو ناگهانی بازگشت صیادان ایرانی؛ امارات بدون ارائه دلیل مانع خروج شد. با وجود صدور بلیت و انجام هماهنگی‌ها، خروج صیادان هرمزگانی در آخرین لحظه متوقف شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/688988" target="_blank">📅 13:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688982">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f35df25a1.mp4?token=pcDyS0P0XhM0ru9JE1MScKR1RZPDlob6ZmLST8XTyi5PWO6icnJzI5s-4alyiLE75IVlcCwTGXLxwEzAsrYLSEJoRQLaSvnsbql9pfHRZxGofbCf54bVcsmgI1OkQ6w8I0vL9wymDCU3eR9QKma6lEO0OAnmwVd-UAr3NvQd_KDJL0aMPB1fW3VkqQYkTko_RyMtJ8FsN_7wvNDDiO5MQEO-1LZ6zcp84K01Eh9M2yHlQuln-JSTOXfGk1y6fKGSUjGUJktTfndZKpkBbmEVZ5BTcK3z1pDmxX77GHW7LjrOv6IBQJxNtc44qAb17UexbM_Tr8BOwLsAqRYj5pKwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f35df25a1.mp4?token=pcDyS0P0XhM0ru9JE1MScKR1RZPDlob6ZmLST8XTyi5PWO6icnJzI5s-4alyiLE75IVlcCwTGXLxwEzAsrYLSEJoRQLaSvnsbql9pfHRZxGofbCf54bVcsmgI1OkQ6w8I0vL9wymDCU3eR9QKma6lEO0OAnmwVd-UAr3NvQd_KDJL0aMPB1fW3VkqQYkTko_RyMtJ8FsN_7wvNDDiO5MQEO-1LZ6zcp84K01Eh9M2yHlQuln-JSTOXfGk1y6fKGSUjGUJktTfndZKpkBbmEVZ5BTcK3z1pDmxX77GHW7LjrOv6IBQJxNtc44qAb17UexbM_Tr8BOwLsAqRYj5pKwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازسازی برج‌های دوقلو با ۲۹۹۷ پهپاد نورانی
🔹
پهپادها ابتدا به صورت مارپیچ در هوا پرواز کردند و سپس به صورت گروهی از آسمان‌خراش‌های ویران شده درآمدند. تعداد پهپادها با تعداد قربانیان حمله تروریستی مطابقت داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/688982" target="_blank">📅 13:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688980">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e952a2f5b6.mp4?token=qpnCE2GsL1v6SQkqKNS4wgIfR3I-qQ-yY-ge6bdxscGWwy_tpfySE10jYyrL5awQGc5vBAOMq6KR10KYdW5Qe4X8PBtx4sXU5ywgIbGYVpLtH8YzqZQwuqL14kcj9BvhljJ8FSvPnwcuucVthwg7P8s-qWskHiD-Y5bneCQtNDxz2-7ABJl4fh9hLl56B_Z3-L_NLckOX_JHXBoR_13ieosMZRSzgN7IQ3yqvC98psqH3YKTr331A1f-Mb2H5NlzWfWkeFS2Zoej-etHotN_OiRPWj99QDbMw6MjCK0xCsQRpOP1nn5N6CUmeOLlQfX4_pdRYL7miU8QDOlBzAPgAZEzuayEcI9OxLlcHLJb6Utlm_Bnky38Di-bf7RwPfAx3rZtz3g-_rQcvwBewpYRjWr6WAHFszAJQcY0Oyj6FjiTF2aeeeC_aRIc81Lhf_gvdkZEbMfc74x-O5Ci52Y4XFcD-a_YpBpicxRYnb52fSKblFulyTc-YUrHaTRskKpzUYcGcdHLGfAeEi0viS7p5VN0yVPI-XLDpZ-Tj0j9YdgUW8jXCFjurjMuHjEOaFYBJuPtMbaEXPkMSvsR1rhNKUtARjcLU7Kxyc-tz5K7yL_x5k42e7gF5XX8yRrYtwYJtGtZ6Y2rarCIqci4WKKWZqyEJqFdtwDVOXUa3ga9aYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e952a2f5b6.mp4?token=qpnCE2GsL1v6SQkqKNS4wgIfR3I-qQ-yY-ge6bdxscGWwy_tpfySE10jYyrL5awQGc5vBAOMq6KR10KYdW5Qe4X8PBtx4sXU5ywgIbGYVpLtH8YzqZQwuqL14kcj9BvhljJ8FSvPnwcuucVthwg7P8s-qWskHiD-Y5bneCQtNDxz2-7ABJl4fh9hLl56B_Z3-L_NLckOX_JHXBoR_13ieosMZRSzgN7IQ3yqvC98psqH3YKTr331A1f-Mb2H5NlzWfWkeFS2Zoej-etHotN_OiRPWj99QDbMw6MjCK0xCsQRpOP1nn5N6CUmeOLlQfX4_pdRYL7miU8QDOlBzAPgAZEzuayEcI9OxLlcHLJb6Utlm_Bnky38Di-bf7RwPfAx3rZtz3g-_rQcvwBewpYRjWr6WAHFszAJQcY0Oyj6FjiTF2aeeeC_aRIc81Lhf_gvdkZEbMfc74x-O5Ci52Y4XFcD-a_YpBpicxRYnb52fSKblFulyTc-YUrHaTRskKpzUYcGcdHLGfAeEi0viS7p5VN0yVPI-XLDpZ-Tj0j9YdgUW8jXCFjurjMuHjEOaFYBJuPtMbaEXPkMSvsR1rhNKUtARjcLU7Kxyc-tz5K7yL_x5k42e7gF5XX8yRrYtwYJtGtZ6Y2rarCIqci4WKKWZqyEJqFdtwDVOXUa3ga9aYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معادلات در یمن چطور در حال تغییر است و چه تاثیری بر نبردهای منطقه دارد؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/688980" target="_blank">📅 13:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688979">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5938cb26c9.mp4?token=ZW4hnWAd-NmiR0b_V5mBm4Y66LTNyuYVOclyrhPClrzrW97nwBdyFYFKvFU0D0zqB1xODuecfTZRFDCvna1SBulhMpFordvzojr3n5HW1FGCf943s-5UCo2YOjJ4F4N7EsqcuQ7mk8Z_rElf7bZVRPdCuPvvXSg9iDbRcatmkD5peYkpfpdgM9BAO_jtdqLQfW1sVrKphVBkP-912mt8_CxvtWetTYGyYbrE2Zk0t67f9PVJypN8ckNKVex-IhxjRPMh8SkJtsIOf_Ae6S3f3xke1QpcdRPqTR7AaD_IEDY-U8n07veY-MzawM93MM1PBFmq5rEoYy82vSBq9jFo5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5938cb26c9.mp4?token=ZW4hnWAd-NmiR0b_V5mBm4Y66LTNyuYVOclyrhPClrzrW97nwBdyFYFKvFU0D0zqB1xODuecfTZRFDCvna1SBulhMpFordvzojr3n5HW1FGCf943s-5UCo2YOjJ4F4N7EsqcuQ7mk8Z_rElf7bZVRPdCuPvvXSg9iDbRcatmkD5peYkpfpdgM9BAO_jtdqLQfW1sVrKphVBkP-912mt8_CxvtWetTYGyYbrE2Zk0t67f9PVJypN8ckNKVex-IhxjRPMh8SkJtsIOf_Ae6S3f3xke1QpcdRPqTR7AaD_IEDY-U8n07veY-MzawM93MM1PBFmq5rEoYy82vSBq9jFo5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه به شهادت رسیدن ۲ نیروی حزب‌الله که از یک حفره زیرزمینی در ارتفاعات «علی‌‌الطاهر» درحال جنگیدن با ارتش تروریستی اسرائیل بودند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/688979" target="_blank">📅 13:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/688978" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBNKvHubR-ptM4xnNNiHxaRk0TzsQDJLWKzdHEUtmDuI0rrqjqLMadjiZl6rm-BfBRS81ZSivwKq9cuxXe4p7M6NWL4CbyDLXpYsFBxYRZWkDjTnf3L9MrDRj1JxdrEpNj3fmt2Wb3q2aC_Z6G7dmwNv4jjRx8m_5CFJ5eURTuWSPbOQSw-zam_oyVsnY4oKwISE6k7ROOONIGYenIEuscuC8FMkJj22rjbwmdjEHgJDLwgmNUWQK2zd4RzZx69GkNSU5cxE6qwndkHZcaL-4VFuSXMsMB_xMFX6iWviJr9ZruOKP65kBeNpdE7-ohmkDhciKsV6Xb05fDduk9Q2nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینستاگرام امکان نمایش پست‌های تگ‌شده در صفحه اصلی پروفایل را فراهم کرد
🔹
قابلیت جدید اینستاگرام به کاربران امکان می‌دهد پست‌هایی را که در آن‌ها تگ شده‌اند، به صفحه اصلی پروفایل خود اضافه کنند. این پست‌ها بدون ایجاد نسخه جدید، همان محتوای اصلی را نمایش می‌دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/688977" target="_blank">📅 13:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688976">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌
♦️
۴
جان‌باخته تجمعات مشهد با دستور رهبر انقلاب، شهید محسوب شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/688976" target="_blank">📅 13:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688975">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
اقتصاد ایران بیشتر از دوره ترامپ دوام می‌آورد
🔹
فارین پالیسی نوشت: اقتصاد ایران ممکن است از ریاست‌جمهوری ترامپ بیشتر دوام بیاورد/ تهران مقاوم، ابزارهای فراوانی برای تاب‌آوری اقتصادی دارد
نشریه امریکایی فارین پالیسی در آخرین مطلب خود نوشت:
🔹
با وجود آنکه مشکلات اقتصادی ایران روزبه‌روز آشکارتر می‌شود، واقعیت میدانی نشان می‌دهد که اقتصاد ایران، علیرغم همه آسیب‌ها، همچنان ایستادگی می‌کند و سناریوی فروپاشی قریب‌الوقوع، بیش از آنکه مبتنی بر واقعیت باشد، حاصل محاسبات اشتباه کاخ سفید است.
🔹
فارین پالیسی اضافه می‌کند: تجربه‌ سال‌های تحریم نشان داده که اقتصاد ایران توانایی شگفت‌انگیزی برای جذب شوک‌ها و تطبیق با شرایط جدید دارد.
🔹
شبکه‌های گسترده‌ تجارت رسمی و غیررسمی، تنوع‌بخشی به تولید داخلی و سازوکارهای تأمین اجتماعی، چتر حمایتی را گشوده‌اند که اجازه نداده قفسه‌های فروشگاه‌ها خالی شود و معیشت پایه‌ای مردم از هم بگسلد.
🔹
ذخایر ۴۵ میلیارد دلاری طلا، درآمدهای نفتی فراتر از سال ۲۰۲۰ و تنوع جغرافیایی ایران، عوامل کلیدی‌ای هستند که اقتصاد را در برابر محاصره مقاوم نگه داشته‌اند.
🔹
حاکمیت همچنین با تکیه بر تجربه‌ مدیریت نقدینگی، بازار ارز و واردات در شرایط جنگی، می‌تواند فروپاشی را در ماه‌های پیش‌رو مهار کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688975" target="_blank">📅 13:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688972">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a30512e6.mp4?token=vJesbQXGfQVRId7Vx5Uk5XVyOkKKTMLsqyBYueCEzkA236PdgeGUXjGyf6kgQWS1A6ykpG7kFZKcR-MjR8B3nU4CZOKx74lqWkJWYDnYFUKH75YED1KgAnX1r93GOef6IXGf1pR5ckOAWE0NdjM7SYYVqZ__QrzTnnh8COdfZKOWKrLS9D0_shL1fqo61ue2D-1qGXOPgnLxJgPw8I-c1-HSyrOF8ZMBrE661hqCKgM8X7BkihG2PQHiKAme6a1RInqqxs-UrgUtF_-pQhOSTEpyb5YkOZTeeeUjNyZ95PJutxzZ9z6FElGc9s9hZ0dMJw-MFek0xqq4pn0BlLcHFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a30512e6.mp4?token=vJesbQXGfQVRId7Vx5Uk5XVyOkKKTMLsqyBYueCEzkA236PdgeGUXjGyf6kgQWS1A6ykpG7kFZKcR-MjR8B3nU4CZOKx74lqWkJWYDnYFUKH75YED1KgAnX1r93GOef6IXGf1pR5ckOAWE0NdjM7SYYVqZ__QrzTnnh8COdfZKOWKrLS9D0_shL1fqo61ue2D-1qGXOPgnLxJgPw8I-c1-HSyrOF8ZMBrE661hqCKgM8X7BkihG2PQHiKAme6a1RInqqxs-UrgUtF_-pQhOSTEpyb5YkOZTeeeUjNyZ95PJutxzZ9z6FElGc9s9hZ0dMJw-MFek0xqq4pn0BlLcHFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی مهیب در مدرسه‌ کنگو/ ۲۶ دانش‌آموز جان خود را از دست داده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/688972" target="_blank">📅 13:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688971">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شرایط قانونی دریافت خسارت تأخیر تأدیه چیست؟
🔹
نخست اینکه موضوع تعهد، پرداخت وجه رایج باشد. دوم اینکه طلبکار، طلب خود را از مدیون مطالبه کرده باشد. این مطالبه می‌تواند به شکل رسمی، مانند ارسال اظهارنامه یا طرح دعوا، یا در مواردی به شکل غیررسمی انجام شود؛ برای نمونه، پیامک، ایمیل یا سایر ادله‌ای که بتواند مطالبه طلب را اثبات کند. حتی مطالبه شفاهی نیز در صورت امکان اثبات، می‌تواند مورد استناد قرار گیرد.
🔹
سومین شرط را تمکن مالی مدیون و امتناع او از پرداخت می‌باشد؛ اگر مدیون توانایی پرداخت نداشته باشد، نمی‌توان صرفاً به دلیل عدم پرداخت، خسارت تأخیر تأدیه را به او منتسب کرد.
🔹
شرط دیگر نیز این است که شاخص قیمت‌ها بر اساس شاخص اعلامی بانک مرکزی تغییر کرده باشد؛ به‌گونه‌ای که شرایط مقرر قانونی برای تعلق خسارت تأخیر تأدیه فراهم شود./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/688971" target="_blank">📅 13:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688969">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25559859ad.mp4?token=YuoOG6EOg-bY7fupBpV1auXbXMGBGr68bco0EvsRnnelx0hJ2gDrEaQkH8Wi_EWey6vgEOS6nsUWUakfZ-4saSur4uJRv5Ci8kHTMl9zdtfXh08lOqjE1pryc2wx0HPN2fAptiE6TK7JLMGUjbqT7st7d1USQV3p3h4_505xemvGG7rlxCJM5hFzPydeDijTzr6RcbR4wASYMkxB_Un-OFKLzEX3rYp35X_qxnoT46LQJOAwHT39GIyXXYhpn5mUkPqlDJ0dh1IQhiQ6V26VzUjMZuixsHUWWjH_fHA-uhbNKAOHENDnCRBlqVhj3TVaIwjetITxxymxzLq7cfW5IYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25559859ad.mp4?token=YuoOG6EOg-bY7fupBpV1auXbXMGBGr68bco0EvsRnnelx0hJ2gDrEaQkH8Wi_EWey6vgEOS6nsUWUakfZ-4saSur4uJRv5Ci8kHTMl9zdtfXh08lOqjE1pryc2wx0HPN2fAptiE6TK7JLMGUjbqT7st7d1USQV3p3h4_505xemvGG7rlxCJM5hFzPydeDijTzr6RcbR4wASYMkxB_Un-OFKLzEX3rYp35X_qxnoT46LQJOAwHT39GIyXXYhpn5mUkPqlDJ0dh1IQhiQ6V26VzUjMZuixsHUWWjH_fHA-uhbNKAOHENDnCRBlqVhj3TVaIwjetITxxymxzLq7cfW5IYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از طوفان شدید در ایتالیا
🇮🇹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/688969" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688968">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4904b61bd.mp4?token=P_VsTRh7IscZmvjfSejh_vQe_7uFjK_Cpl9hmQTK2xVV7ik25ygnbxRU-SNuvQdm-Kt7PYi4fltUgUGJK7MVG4SUa1_FZzRRGmRfh3coTszxna_3htNzI672Yl_T7RMKibXZogzh2SDcAMdVPxWRTX_DMdqfZNSUvCDmVIh6xZwQatLwVbk4xSi80NhH_qhhHQrWmNvcc9fuOcjer6aWCncK-l1GHIfUfc6yWfL_kdRfUZeMRRt97mC1rStSc7EwoSK7NdI5k9dUxiHPmartLyQZSLv4jV0l-Ol6eZii5B1jXl7Izr59Nv7dBUOAPLUcQ64yhbwRDQ5RU8q_icbkkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4904b61bd.mp4?token=P_VsTRh7IscZmvjfSejh_vQe_7uFjK_Cpl9hmQTK2xVV7ik25ygnbxRU-SNuvQdm-Kt7PYi4fltUgUGJK7MVG4SUa1_FZzRRGmRfh3coTszxna_3htNzI672Yl_T7RMKibXZogzh2SDcAMdVPxWRTX_DMdqfZNSUvCDmVIh6xZwQatLwVbk4xSi80NhH_qhhHQrWmNvcc9fuOcjer6aWCncK-l1GHIfUfc6yWfL_kdRfUZeMRRt97mC1rStSc7EwoSK7NdI5k9dUxiHPmartLyQZSLv4jV0l-Ol6eZii5B1jXl7Izr59Nv7dBUOAPLUcQ64yhbwRDQ5RU8q_icbkkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گره طناب برای بکسل‌ کردن؛ روشی ساده برای مواقع ضروری
🪢
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/688968" target="_blank">📅 12:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688967">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy4CfZCNcsFtjhiRwFhcPw8U5UX92R-VO_MiHI5bZhy6b_vrLOFR3COqQpw4A71sIaDYrXpJpz73XKKh0g3pHr5-8J1Ux0g7eIM37nSjMCqF4UceblfKSwincrXGo5KnPaYYVOALGla2KNLUPEd5gPt6pjEKQHEU_iv86-W_DJzrDNa8j94C0S9uBi3JdmO_R6qqV-MqBRpZdwvwRv_amtBTA6t2jUc8Aut_uD8l9sQzd45uO0esSpL8yzKW6nDr9iwUq3Cp0BEMKlswRJzowBjBhwMLdLy-2uP-Vq_BDKSfq3eQAVFkR5K85zfWL2SG5JOevzAXIRR3pdNe8V_0gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پک ویژه «علوی»؛ سه تکه از بهشت، همراه شما
نجف، نه فقط یک نقطه روی زمین، که نقطه‌ی آغازِ دلدادگی است…
برای آن‌هایی که دلشان در ایوانِ طلا جا مانده، یک مجموعه اختصاصی از عطر، نور و غیرت حیدری آماده کرده‌ایم. مجموعه‌ای که با عشق در کنار هم چیده شده‌اند تا عطر و نام مولا، پیوسته همراه روزها و خلوت‌هایتان باشد.
✨
محتویات پک اختصاصی علوی:
▫️
مهر تربت بوتراب: خاکی متبرک برای زلال‌ترین سجده‌ها
▫️
عطر حرم امیرالمؤمنین (۲۰ میل): یادآور نسیم سحرگاهی ایوان نجف
▫️
گردنبند ذوالفقار: نشانه‌ای از اقتدار، اصالت و پیوند با نام علی (ع)
💰
جمع کل در خرید تکی: ۱,۳۲۴,۰۰۰ تومان
🔥
قیمت ویژه کل پک: ۱,۱۱۰,۰۰۰ تومان
⏳
موجودی این پک کاملاً محدود است.
📩
ثبت سفارش و مشاوره:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/688967" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688966">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551a668ee8.mp4?token=LkXStghObzNPfb9HOhIMCnI-Po977FpIbD31b2clds9Q82Lw0cOwHn3DqQg4RGMO6EbfOOsd-WS0wfwB8Yj-bqJ_gp4RSN-NM_8fKBnna7wXdJR_PzIfARiC46-TdxRhbFCso5_I3rodC8pIwCAVML8oW6PmmTlX2lp0Rfv7XdyEh2SA-3I3c3p_buDCMolj6vEMUMU2BdqvCrDxDKR7DbV98H2SaoQI7jLiBMKGIIb7bEixPtHeSMSfg6CguliZdDQ-byANZD8THX1Rz42Wb9HGnJ5FFTc0oNS1g8hn3s-QvA88d_wRv5mRY0lffiQG9FlrXOPCBpn6vo4j3qbcnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551a668ee8.mp4?token=LkXStghObzNPfb9HOhIMCnI-Po977FpIbD31b2clds9Q82Lw0cOwHn3DqQg4RGMO6EbfOOsd-WS0wfwB8Yj-bqJ_gp4RSN-NM_8fKBnna7wXdJR_PzIfARiC46-TdxRhbFCso5_I3rodC8pIwCAVML8oW6PmmTlX2lp0Rfv7XdyEh2SA-3I3c3p_buDCMolj6vEMUMU2BdqvCrDxDKR7DbV98H2SaoQI7jLiBMKGIIb7bEixPtHeSMSfg6CguliZdDQ-byANZD8THX1Rz42Wb9HGnJ5FFTc0oNS1g8hn3s-QvA88d_wRv5mRY0lffiQG9FlrXOPCBpn6vo4j3qbcnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید اسرائیل از سوی عضو هیأت‌ رئیسه مجلس
علیرضا سلیمی:
🔹
ایران همواره پشتیبان مقاومت بوده و خواهد بود.
🔹
نیروهای صهیونیستی حرارت آتش اقدامات ایران را خواهند چشید./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688966" target="_blank">📅 12:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688964">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/688964" target="_blank">📅 12:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
پزشکیان: به جلیلی گفته‌ام هر کجا که می‌تواند، اختیار می‌دهم مشکلات را حل کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/688963" target="_blank">📅 12:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688962">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837de8e830.mp4?token=NOVgGWnh0K5KS9RhaUVazKEURJ-cJJZViOl_Q5D8cT3_GudFnYsIgWW2wehHepCihYrXmtxzHlIbXGxgQLRu26wP7osn1zNglVd1I72WA2qvysUMQX_vhTAO9ta4yU2WCtBlaUM5U_40i_TV2lXADFhJLBKrmzsGVsAk1GjqTVXMgPYCCZFORHokZDf1-EpScnc-NYF-L_iPQD-1wzX1xmy1apuNhGhNiU9QDV-p_90ae_Si6K6M-UyrSUo2IP7jN7mxxX4bJ4GS2iN7FtOaZVOuqj6uVhgHHWv3n2Ak7uDoKxsT_L3g10tn9VII-itCYUODVFNCpKCyKh0GlAe3NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837de8e830.mp4?token=NOVgGWnh0K5KS9RhaUVazKEURJ-cJJZViOl_Q5D8cT3_GudFnYsIgWW2wehHepCihYrXmtxzHlIbXGxgQLRu26wP7osn1zNglVd1I72WA2qvysUMQX_vhTAO9ta4yU2WCtBlaUM5U_40i_TV2lXADFhJLBKrmzsGVsAk1GjqTVXMgPYCCZFORHokZDf1-EpScnc-NYF-L_iPQD-1wzX1xmy1apuNhGhNiU9QDV-p_90ae_Si6K6M-UyrSUo2IP7jN7mxxX4bJ4GS2iN7FtOaZVOuqj6uVhgHHWv3n2Ak7uDoKxsT_L3g10tn9VII-itCYUODVFNCpKCyKh0GlAe3NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند ساده برای آشپزی بهتر و راحت‌تر
✨
🙂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/688962" target="_blank">📅 11:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688961">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrR9I5AmkkdJjgTPVTAgPgKevVl-3J6RBPQGPJupBvBjurcrzx_LXxQ8E96DZ7lydggX3PzOOuErbHVELBo44Pfh1bnFOR-04JSPbx7Ur1OMdwkvzWMeTqeWoLHBLWq1y4gqu-vD3eBtBXH2qkFEjEzycMK_ORsL_LPzXRZHZV0HXZVvVnf6kUGwNla9rtIAFHAARyimTp4YgAqU_8zZ6f0L05cYgHowEmJAc94JzlmqSI1-JlE7HC6UTUOHZ_AVjJRmtGq7tY4LhRGKjUhM2H9QeebITaPC0kkmo3dB83i0B-C-rTzTH2_Is1EeUSduSiDtXUA1uD0rCUpEPuqRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صعود
ایران به نیمه‌نهایی والیبال قهرمانی آسیا
🔹
ایران ۳ - ۱ چین تایپه
🇮🇷
۲۵ | ۲۵ | ۲۱ | ۲۵
🇹🇼
۱۹ | ۱۹ | ۲۵ | ۱۸
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/688961" target="_blank">📅 11:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سخنگوی هیات رئیسه مجلس: ادعای افزایش ۵۰ درصدی حقوق نمایندگان کذب است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/688959" target="_blank">📅 11:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688957">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی فدراسیون فوتبال: برگزاری بازی‌های فوتبال، بدون تماشاگر ممنوع شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/688957" target="_blank">📅 11:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688956">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
همه‌چیز درباره بریکس / در هند چه می‌گذرد؟ / قدرت‌نمایی منهای آمریکا
🔹
این روزها نگاه‌ها به هند است، کشور میزبان اجلاس گروه بریکس که اتحادی به‌دور از قدرت‌های غربی را تشکیل می‌دهد. از پوتین تا پزشکیان مهمانان این اجلاس هستند و موضوع ایران احتمالا داغ‌ترین بحث در جلسات سران کشورهای عضو.
در این‌باره بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3243892</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/688956" target="_blank">📅 11:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688954">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6902f42c.mp4?token=q8DK6CHa3ixNXr1OW6fX7jcjXLkTZgE1Ap97c1Nn90u-6OdaXkxkO59QnRE_Wnk4mBDQM3zBQutjOgGUVxIJ3Eq8E1o2G2hqWXzSt2hKMk7Zpic0J1dJvm7hShcqKxKJ3vQ_tfW0cjXtW8AOocXxMo5EzDe1ZGaCk4HDRRQr23Dr_W53w94NtUCkrOzO6QqWSl5K_RIAe4bBU0n6i5rPiXC-lktPlUJWjf7NtKQfheCeb7YD-N7uyReEdvFEVpS90eQlPQc_l8hxEJNODzlmvfWA4GecpFbxUee44CSy-tOCi80w2XkuR5K23vGXtN5-IDJntqJiPGInsP8R4rzo9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6902f42c.mp4?token=q8DK6CHa3ixNXr1OW6fX7jcjXLkTZgE1Ap97c1Nn90u-6OdaXkxkO59QnRE_Wnk4mBDQM3zBQutjOgGUVxIJ3Eq8E1o2G2hqWXzSt2hKMk7Zpic0J1dJvm7hShcqKxKJ3vQ_tfW0cjXtW8AOocXxMo5EzDe1ZGaCk4HDRRQr23Dr_W53w94NtUCkrOzO6QqWSl5K_RIAe4bBU0n6i5rPiXC-lktPlUJWjf7NtKQfheCeb7YD-N7uyReEdvFEVpS90eQlPQc_l8hxEJNODzlmvfWA4GecpFbxUee44CSy-tOCi80w2XkuR5K23vGXtN5-IDJntqJiPGInsP8R4rzo9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصب گلس با دستگاه مخصوص؛ روشی متفاوت برای نصب دقیق و بدون حباب
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/688954" target="_blank">📅 11:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688953">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ضربۀ‌ کاری انصارالله جهت افزایش تسلط بر دریای سرخ، جزیرۀ زقر هم آزاد شد  خبرگزاری‌فرانسه به‌نقل از منابع یمنی:
🔹
نیروهای مسلح یمن پس از تسلط بر المخا، جزیره راهبردی زُقر را نیز تحت کنترل گرفتند و در مسیر گسترش نفوذ در سواحل دریای سرخ هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/688953" target="_blank">📅 11:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688952">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d286b54d.mp4?token=cUWo_5ZGVswrg0Sv2FUbmktvJ-VvAbMVv_h3CWrSbptAojVyNF5wvTsZI8CjNNK3eBs-OmEM2ldQo-n-XzDP4dBEj8SME7NZ_dep9NP3PvW1o2Ms-Du2PlW8M1ELVHGd7O_Be0FOtdzgKLRDMbI0hFx3JvbzZEF_wepgCcIbzsBjE0hL-SFu1gkbb5gsNmS_n7dMvtUT9g2Vk_6d7_UnthIia1j0RjxzCA7Er5Ql1irMUepPfnoRQ-J1UEPDD1tLJMDjY5H2btrrX08daz-gYf1Q9NovNTOJ5ZVfZHBxWVW51ptsoEy-YE4wwU2y0-4J5Mnet8gFpux2Bg-MGynw-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d286b54d.mp4?token=cUWo_5ZGVswrg0Sv2FUbmktvJ-VvAbMVv_h3CWrSbptAojVyNF5wvTsZI8CjNNK3eBs-OmEM2ldQo-n-XzDP4dBEj8SME7NZ_dep9NP3PvW1o2Ms-Du2PlW8M1ELVHGd7O_Be0FOtdzgKLRDMbI0hFx3JvbzZEF_wepgCcIbzsBjE0hL-SFu1gkbb5gsNmS_n7dMvtUT9g2Vk_6d7_UnthIia1j0RjxzCA7Er5Ql1irMUepPfnoRQ-J1UEPDD1tLJMDjY5H2btrrX08daz-gYf1Q9NovNTOJ5ZVfZHBxWVW51ptsoEy-YE4wwU2y0-4J5Mnet8gFpux2Bg-MGynw-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرایی ترور علی لاریجانی از زبان رئیس سابق MI6
جان سائرز:
🔹
علی لاریجانی عامدانه توسط اسرائیل ترور شد چون تهدیدی محسوب می‌شد و تنها فردی بود که می‌توانست به توافق صلحی برسد که برای هر دو طرف قابل قبول باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/688952" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688951">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d4f91d52.mp4?token=U9KRWH4HxMsb9dtBaLf-kl2wa7b6_JPngeGeGgE_DYTaV2rXZRtpAiiRVdMxFDYDXhTgMzZ05fTRIJhWsV10Lsmp05HDaq0chya3zbCFV0S55t0x7Pk683m6r1UdBr0Z_2QvSu76VYEw0a0_-aewTpyMS0QeVSSqtngDPPdYvSAuIj4UZuLWnLWoDv--WPJ1uiTWnJdqF8ETEecQBAFmRLw36T5vPJM6cLcMmK6Iy8v_zOxY92h-tc_BYltmjgeIBPihGm_G1JIIGjmcUW0yXYUZJvehNcgAc9wubRhz1Bo6YHgAFynu0BpfHm3rCnJivsyQI94aL-45DO22JtO3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d4f91d52.mp4?token=U9KRWH4HxMsb9dtBaLf-kl2wa7b6_JPngeGeGgE_DYTaV2rXZRtpAiiRVdMxFDYDXhTgMzZ05fTRIJhWsV10Lsmp05HDaq0chya3zbCFV0S55t0x7Pk683m6r1UdBr0Z_2QvSu76VYEw0a0_-aewTpyMS0QeVSSqtngDPPdYvSAuIj4UZuLWnLWoDv--WPJ1uiTWnJdqF8ETEecQBAFmRLw36T5vPJM6cLcMmK6Iy8v_zOxY92h-tc_BYltmjgeIBPihGm_G1JIIGjmcUW0yXYUZJvehNcgAc9wubRhz1Bo6YHgAFynu0BpfHm3rCnJivsyQI94aL-45DO22JtO3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لباسشویی سنتی در رومانی؛ شست‌وشوی لباس‌ها با جریان طبیعی آب!
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/688951" target="_blank">📅 10:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688949">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای فایننشال‌تایمز به نقل از منابع مطلع: وزرای خارجه کشورهای خلیج فارس برای پیشبرد توافق هرمز با عراقچی دیدار می‌کنند
🔹
این نشست قرار است روز دوشنبه در شهر ساحلی صلاله در عمان برگزار شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/688949" target="_blank">📅 10:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688948">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cic24i0ql5n61-i9eI9S3HYN9HqhpC-Fv1CMaMtjDmF0c9L4m6sZ1jrD8yYigKe8Gc4dRY2_YwFEn_Jgml4VZLvsVE2KwwhNiBhZFj7gqzb3pJhxJi2qe6IjGguEJTULvcAQ5PC5y18dwqcLXXy4TlUCUMvOD6LpoxV4-CllcQ7zFUknUPrZm47qvsL1dP7JBZpcYKTy9h3v4cNEI8-D4Jql7mprlXzfOHEwQed-G6sFElmkz-wv6qckbDuZ1r78nwr7KW-Bte-LIoMR767Le7P9_n9eaT11VYgGBj_ksaeYsgUjqFypz_t38yVmCjSftBSQULfbdkT5X05_SJOkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ مدل نوشیدنی خوشمزه با هویج
🍹
😋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/688948" target="_blank">📅 10:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای جدید ترامپ: هیچ هواپیمای نظامی آمریکایی در حمله ایران به پایگاه هوایی در اردن آسیب ندیده است
🔹
در حالی ترامپ این ادعا را مطرح می‌کند که شبکه خبری سی‌بی‌اس آمریکا از خسارت گسترده به تجهیزات نظامی این کشور در جریان حمله موشکی ایران به پایگاه هوایی «موفق…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/688946" target="_blank">📅 10:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
پزشکیان: بسیاری از ساختمان‌های دولت از جمله سعدآباد را در زمستان تعطیل می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/688945" target="_blank">📅 10:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0ba2da91.mp4?token=TCBPxNkmoy7sdre_zJl5ppXNzLPkjLskcxQK3fA8Jqtxqfvn87W1gLPz6aM8dpexXwW1BTZ52ubRjjzhc5NM-CgniAGyqUvxCbDmf39fju0wk9X3X3-0DGzKWRlAd6nkW0TXRukeE2Vp4Mbt9ErTcu-HCSY3WYCZXRUet4iCWhZtIrd4nO7y2Svp0-7B_arBT47HoTpOeSlihY4NKU7QgpfuBluKTBBk1inAwoai3AHZ-8-ol9U7fBCcPfyPi3e3n9fRgRnwLINto5R5OaN2Awk-3b3s-FKFgaHpAAbehqV50fpOZGT57am2YEvKBV7f-5BxalK58vlxeMxdD4kfMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0ba2da91.mp4?token=TCBPxNkmoy7sdre_zJl5ppXNzLPkjLskcxQK3fA8Jqtxqfvn87W1gLPz6aM8dpexXwW1BTZ52ubRjjzhc5NM-CgniAGyqUvxCbDmf39fju0wk9X3X3-0DGzKWRlAd6nkW0TXRukeE2Vp4Mbt9ErTcu-HCSY3WYCZXRUet4iCWhZtIrd4nO7y2Svp0-7B_arBT47HoTpOeSlihY4NKU7QgpfuBluKTBBk1inAwoai3AHZ-8-ol9U7fBCcPfyPi3e3n9fRgRnwLINto5R5OaN2Awk-3b3s-FKFgaHpAAbehqV50fpOZGT57am2YEvKBV7f-5BxalK58vlxeMxdD4kfMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مستندی درباره فلسطین در جشنواره ونیز رکورد تشویق را شکست
🔹
مستند «NAZA» رکورد تاریخ جشنواره ونیز را با ۲۵ دقیقه تشویق ایستاده شکست. «نازا»، درباره نسل‌کشی اسرائیل در غزه ساخته شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/688944" target="_blank">📅 10:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688942">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
تمدید دسترسی رایگان ماهواره‌ای آیفون
🔹
اپل قابلیت‌های ماهواره‌ای از جمله پیام و تماس اضطراری را برای کاربران آیفون‌های سری ۱۴، ۱۵ و ۱۶ یک سال دیگر رایگان نگه داشت؛ هزینه پس از پایان دوره هنوز اعلام نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/688942" target="_blank">📅 10:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688940">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دپوی شیرخشک و کره در کشور/ انجمن تولیدکنندگان شیرخشک: ۴۰ تا ۵۰ هزار تن کره در کشور دپو شده است
سیاوش سلیمی، رئیس انجمن تولیدکنندگان شیرخشک صنعتی در
#گفتگو
با خبرفوری:
🔹
حدود سه برابر نیاز داخلی در کشور، ظرفیت صادرات شیرخشک داریم اما به دلیل افزایش قیمت شیر خام و بالا رفتن قیمت تمام شده، این محصول دیگر قابلیت رقابت مناسب در بازارهای منطقه را ندارد و صادرات آن با مشکل مواجه شده است.
🔹
در پی این مشکل، بخشی از شیرخشک تولید شده در کشور دپو شده و از سوی دیگر، جنگ باعث از دست رفتن بخشی از بازارهای جنوبی کشور و کاهش تقاضا شده است.
🔹
همچنین حدود ۴۰ تا ۵۰ هزار تن کره نیز در کشور دپو شده که این حجم از موجودی، پرداخت مطالبات دامداران را با مشکل مواجه کرده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/688940" target="_blank">📅 10:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688939">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3f719970.mp4?token=ABVyEXlTAd6Ghl-skeAp643ZCtNGxdfeeLtazNKrGtgZ_qMsZzJoW0T2RZhdQ6CTourjwIHQhdNkVRd5fT2WiVp12HprHmNbMN_4dhZBiXP4U_yOzZ-W1AQWH2cS-TUxGtGKuJYHC30PWOTeyuYWRGURaMlSFV0L8a2gzuXAWa3s1sSqCCTcW4Lcj7g_CAb6UXLO3V8OxhOolFPz4YJMGtDD7pVLhh3-CX0_m1I1aJaHjUi6-n3zLkI8lULr7vcICKEvYYK47W_3bp3stsCK16cJgUU3Zb1C0kVCuspP36JCt2qPXI60gRAywmTZVQEJsWQgVI7wCexTARFalwUR9wcqaLdisymlTgL4aV-nR8u9xb2r7pv4DnASkCQlbG9Ig1IBOU9K8haMRNp1SjmfDUikvHl309jw80dfZ-GhiqHmvJMVk621g_Au4bzeuXnRrOoVSuKo_RjbaBhnfaRl7gJOdRudDeWnhPK9sVlt3lPgfJ0VIxkZ3mexUV75HuSjYCZa_NnIGcP0v46hB8wkFNtF3S_D2_2FhdFT7gW7xZK6HTdhyG3Vhbuc8oR4DvwLxvkJas1zeKelYE0oZbcXIYiUjygSrh8cL52OTSivdMK43c0Ay-pmagZBBqUr4cF5rsenBVf526ySvZ8qDxCOt_TAiorbJHrCI2jnOZ1ht1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3f719970.mp4?token=ABVyEXlTAd6Ghl-skeAp643ZCtNGxdfeeLtazNKrGtgZ_qMsZzJoW0T2RZhdQ6CTourjwIHQhdNkVRd5fT2WiVp12HprHmNbMN_4dhZBiXP4U_yOzZ-W1AQWH2cS-TUxGtGKuJYHC30PWOTeyuYWRGURaMlSFV0L8a2gzuXAWa3s1sSqCCTcW4Lcj7g_CAb6UXLO3V8OxhOolFPz4YJMGtDD7pVLhh3-CX0_m1I1aJaHjUi6-n3zLkI8lULr7vcICKEvYYK47W_3bp3stsCK16cJgUU3Zb1C0kVCuspP36JCt2qPXI60gRAywmTZVQEJsWQgVI7wCexTARFalwUR9wcqaLdisymlTgL4aV-nR8u9xb2r7pv4DnASkCQlbG9Ig1IBOU9K8haMRNp1SjmfDUikvHl309jw80dfZ-GhiqHmvJMVk621g_Au4bzeuXnRrOoVSuKo_RjbaBhnfaRl7gJOdRudDeWnhPK9sVlt3lPgfJ0VIxkZ3mexUV75HuSjYCZa_NnIGcP0v46hB8wkFNtF3S_D2_2FhdFT7gW7xZK6HTdhyG3Vhbuc8oR4DvwLxvkJas1zeKelYE0oZbcXIYiUjygSrh8cL52OTSivdMK43c0Ay-pmagZBBqUr4cF5rsenBVf526ySvZ8qDxCOt_TAiorbJHrCI2jnOZ1ht1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هنرنمایی دیدنی دختربچه برزیلی با اسب
🐴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/688939" target="_blank">📅 09:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f0571ecb.mp4?token=E8bu8_TzzbBcMCGUHRyTclt2m2sEqjGeWlVC20tcZ1vImJS4UnfT_b6kY9vtvA2dzy5IaClN1Rv7BlSYS0lCZZvSEOtubZGg0gQqVBYjmEcQT5GHYfDC7U2b3PylbaogWxAiX4UyiNYKpsjbQYSZFMy28BCUSPALiGTa65djSnYQOexAfUq_XD8BeqeKcDd4CzOq6PVe5Ztx4XPSe_Pqlz8sWQW1fc6g1znfV2pc1aF4p0Wi7JcvttVT_eTqowBFnHIvI1X_qPRg_rsWh3AuL3xp2itODiPwnMGGsPzfmh02AWwNsQc_ZSa_mikewe_3qGP2d_RQFQtDWb-LcVwlnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f0571ecb.mp4?token=E8bu8_TzzbBcMCGUHRyTclt2m2sEqjGeWlVC20tcZ1vImJS4UnfT_b6kY9vtvA2dzy5IaClN1Rv7BlSYS0lCZZvSEOtubZGg0gQqVBYjmEcQT5GHYfDC7U2b3PylbaogWxAiX4UyiNYKpsjbQYSZFMy28BCUSPALiGTa65djSnYQOexAfUq_XD8BeqeKcDd4CzOq6PVe5Ztx4XPSe_Pqlz8sWQW1fc6g1znfV2pc1aF4p0Wi7JcvttVT_eTqowBFnHIvI1X_qPRg_rsWh3AuL3xp2itODiPwnMGGsPzfmh02AWwNsQc_ZSa_mikewe_3qGP2d_RQFQtDWb-LcVwlnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی سنتکام از سوخت‌گیری هوایی F-۳۵ آمریکا بر فراز خاورمیانه
🔹
سنتکام ویدیویی از سوخت‌گیری هوایی جنگنده‌ F-۳۵ نیروی هوایی آمریکا از یک فروند هواپیمای سوخت‌رسان KC-۱۳۵ منتشر کرد. این تصویر هنگام گشت‌زنی جنگنده‌های آمریکایی در آسمان خاورمیانه ثبت شده است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/688938" target="_blank">📅 09:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469234ffb1.mp4?token=U8-tWbMvfzU_suHf7sToelBGjTsWFAsRNk5mkZ7H041W1x08mH0ni-LkJO-j_PXWGaTYRaIRPcek_25IARYWsKE2nkrsMt-e1VgxuBvjcLXeObI53fMIYLi6Zf2TjAgaDTlzux3CsM9y3jPbqNDH98suPAw9fMQWlartHk2JxQV1YZq2Zz7RWr0wCTADzz4AGQx_ldvKuCUnzGbRIoKUoCfvYXVnuT4KNXw-E47AmmAGkFskgNr9pcmctz-LiAcsHbhk-14M3ndZCesbcfZq4dYfoSrWWOmcirMGr5D3UenCMMUs7b_sHMZ5LLOekgmv32OyJtMOge2OYgH_WQwfoLVpOFdNuXXyzeXE3OCM81JkOuuZNosfTk2e7wTd28MchYZYVGqDicdWmtPixUFb_ozQgYf6NSv9Jp-_SKvt33E6kaLhXx0R9Zf25tS50zmWfedrlsCXnKnDOY--RD8t8Igd3Wdmu-4zbGBSLQzIIZ_l32AORSDc2fXqqrDe3DGSqss-pV7Xd2bi9Gz7d5gukygkzgm9NGRg-25uNcFcFL5f_WbIJtBnPGdEC-w5DxlDJ9BZc1EhOXJwQPeuw5bKgsMOVwfgXqxwcBrFtNeRUhqA8mUFouZkaZVQbVf8yrBXj9EE7Np-TMUtVXbI3bdiJTR2PIXH5dfIZx7koh43Iuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469234ffb1.mp4?token=U8-tWbMvfzU_suHf7sToelBGjTsWFAsRNk5mkZ7H041W1x08mH0ni-LkJO-j_PXWGaTYRaIRPcek_25IARYWsKE2nkrsMt-e1VgxuBvjcLXeObI53fMIYLi6Zf2TjAgaDTlzux3CsM9y3jPbqNDH98suPAw9fMQWlartHk2JxQV1YZq2Zz7RWr0wCTADzz4AGQx_ldvKuCUnzGbRIoKUoCfvYXVnuT4KNXw-E47AmmAGkFskgNr9pcmctz-LiAcsHbhk-14M3ndZCesbcfZq4dYfoSrWWOmcirMGr5D3UenCMMUs7b_sHMZ5LLOekgmv32OyJtMOge2OYgH_WQwfoLVpOFdNuXXyzeXE3OCM81JkOuuZNosfTk2e7wTd28MchYZYVGqDicdWmtPixUFb_ozQgYf6NSv9Jp-_SKvt33E6kaLhXx0R9Zf25tS50zmWfedrlsCXnKnDOY--RD8t8Igd3Wdmu-4zbGBSLQzIIZ_l32AORSDc2fXqqrDe3DGSqss-pV7Xd2bi9Gz7d5gukygkzgm9NGRg-25uNcFcFL5f_WbIJtBnPGdEC-w5DxlDJ9BZc1EhOXJwQPeuw5bKgsMOVwfgXqxwcBrFtNeRUhqA8mUFouZkaZVQbVf8yrBXj9EE7Np-TMUtVXbI3bdiJTR2PIXH5dfIZx7koh43Iuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگ کلیه چطور به‌وجود می‌آید؟
مهم‌ترین عوامل را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/688937" target="_blank">📅 09:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688927">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnfp_SiJ9QTuVn-YXeIeT6SnuQbIpqOeGYC6HBubqX8yucaJyH4JUmam1SK5stpNJMU3P2EXztXNuPoqoYbnt9sQMhbiZPc-eRSBdBqiMx8AgUUSuLVnOUlFY1N32GbIHqk9RHItlCfa5tyME5--qW6Ol38xl1dlgvw6QQ4tN0nVYFmko5HZLOh7q27gCT0TE4gUqWXJBfEHLh9Nc52fegjI9_YBOvfIgNXO4pcT-PuvJ_iUqQlq7niwg3-ZJtAPegwYg1pzue_ypdEeeMPxkrq-8S7ZvJtTD9pqLuK7YP5xI0sbOcux8nwHKSeL4yD959bpZizKjg0-YC5AR9wAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LcGQ44Rr-oY3_maI-DjWrDDMikBNq1-63IDqB7l-hv9-ulkwzL2V9AsZf4FODTvmE5mZmoE0trgFYYZVmZyUxduT7mHklm06Z1GUXgUAS9lnp9YE3YhHuRu4zILGH6FCSgMNMB1_XcxFujsHE81bJMh-iGIMTbQRR59ba2S0FcDRPtsn8zq1Z1u5Y7vxOwbr2TH2dFjv0hQT8YmBq4wrz-d8lojvSDMoNE2XWNF99tiNDYfRhXLaOHu-9ZS2TMogGh4wulSdGORMKPrW-YgCTvLsQAgQ5a-UcYXcj4K-nLHEVo0a6tJtkdsBZzHLxkhTJEUnbToHKYKACkL4MbRzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrmXGmI6Wwfuyg1T314l-3GnyBPlXocieiC5wvmqVKnVXHlg1g0GujqzFo0SNFq2VKNNaI4QFHJsPwB7Hp1_2MJj7TOcImRp0qKWIG5zSA5bLbvYAdbphxAreu6D7Z_WFhmKDkDiKtRc5j9Cr8u8evt29gQmjCXalpDRREm_yC8Y-Kauos_3VBeVAJYKEEkg2n2q6hdHYVrzszg4Sc_OwyRL55V2UlfczAzhyltFPHSlS_93GSA0jRiDzV2xKkHtDGmoSe3IT6f6KoL4v_On8iYRLXAsXI1dHZXiHzF6BRDo2VjCrD71gV7wprNv21U133_FQIYEap3oueicPomK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bddv7sT27vz_bh3D7lmEzVy8fItLUc_2voBSqtL_xXHghV9LpcG_mNT9-YFI4FiMDEOAPfKxzj4WYmcuf476ltR0eedCRre5SC1VZG1XkHl0D63bwLcW-tWfT56Z3JYPwc3WDhQHxpPZ4CC0mwycL2jSqkHNYysmx27FQj3dI9sF7dP8PwDP4QKo2KwZZO47_4D3aaU5gBud5-9BUZPDQYGN-VUnFt_uvR4VxKgyvkRxebEW7irHWETCk19kqtBVqG_01cdzrYCbr1Il9nqzraXjBGXiSYVsIXCXneh1swYqg7jesqNszwk32_BquejmCuYyEZoDkJeNF_SsoZhJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8OdSrUYQYyNuB3M3ZoW_MwZKAkfrCLs-9jjUY6nIfSs_jL7zj--vXlj59oagIGYLJbilvtKslQG6-E-p4-7VEcZNNiC6KBTLP68rV2bBkV-knyWa07DUVIOiuDokz40POgCUkxRw8TWEpW1f2oR1SI99fyz0w1oYn3w4XssZQ5nEwxk8NymCPtGUOgP5N3nJN5b6eer3RrnEoU4V5j93QWhlGp_UnNLsfgNT901w9x3YCFArSd915C88SO7flhXQNH9NO1Guph4RR8jZj5rSquujXvKk7NUSiJme-kzyYryOoFNAIeY6k_dBpyxT6dPqtBWXx7EKktxFT5ckzF9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mviliLIsc5OCscXegVgWPQpVYB-YGwjMflmJw_42qx-bC8vt-D1sM2feamSSs8bD2_7seS2IEAAkjDYJj6tkvy4iaoIf7MdtzkQNOo8-qFCV--YTbGmdsdxm7lrbUg_L1kJiN1tv_8w4PX7XYduqcV__baldXEZvycco8pQcxWKPeFnaeABcDxAnufUmcAiDgnR7WADqC-dCd49fjzAe8XflR5XvYwGMuVT3vkSnrdCpJ5i9ybOGlW9bsRWpGi0vmtVj03Ds8KdV62bFwgZljLzD6ILlcaKdhSj6vVxWC2nbQJri9EzVq-17tO1eheTU6vZXUtvKVd3I59NMkH4H9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMoeUMAMaPHSMnrz3RYFiUWAR0XQYPkKH6tFGwccWIONBV5zR_TtV5WIP7Plc1iDDvofG-iBPBmj13jbhIl2NbfsuZDJnyWcEdfnruki-tkCzfFkH59Z8gw7XNqKfrO4ebUcZqSElgTFyHUJEPkATVMnV4rHOvuxqMDV1Tag6c0PgfKMJXKKyPpa6V6Rkp9mErwnU9lS76xPzfFu-eJX-q44QUw7kuurlGG_EtFkgFwOZ3De1IclKLqEzvk57GbrzhnJJDHJLKlTGbbHrHGRjHbyNhgfkl6FsWt2LJjh4bSR7OqdjFeXHMCBWr4og9gkBzMitNQs8Pu-NeEdJI6SEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_ISQ_ji3HYqOWqe3haPYdkIbfyks8-72Ss6QkRAz25_nfTwmrwNTe9HNYMmENv0lbR8iYxy78ZgBTeFQcFI2W122pE9XWdN5XIcx0BpXEfF4QMVlaTlTpYnEMx9ZmoPANy9vl8z6an_QqC77SrL2cnRcQCVqKkcgP9bekiY1Nlvrb4lvVB1jFaJQ2aABSbD1-Kavu_Gc7Xi2llJTtQcYNKne2xzcVS9smns9qP1j_tRhelplgSKpYuWYeuZah52T270dWOwtyxmjSZz2SsUxcxzunq5WOPYsgSTfnaDNrf7GRL-5t4D0ljALiQNMvUnc2fq3HitVEjNGL0OTj0dqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGQaUqowfFvBc-VDarPCB5LidLtT1oAuLS2OGVi5nc2SJn5T6SGnSHcmNbI4PjZAh1mdq_MhUshf9kVJ62IY8qplQX50vdUsWDEARbiV95clMzRmTiyJJsYSQTMvJLWSMNeS69lHy8gBVrlUsJZgaFd8BFHi_xGOQrJLryOTaWdQGEhcLVXnsIBdI3gf3T1uSj9c5RG5SZStXNwHVTzKxKkLODPOxL6Tr9ykeXuIxKCqQfVilifOncLaKegtd3JOleC2LE3REMioq56KNdrX4yy0p9qZkFp3OgZQcKVQR_-vYORafZnHuTrtaWZxqN1l7dbjY_QAKHU6ZX6qKDuXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwPyeeWcIlkI2F6b5VzqEssTNBLw2cpmE43VEzl8YyXFF5fx4lK9WFI1ZOaTJBdhRcsK0OT26cQeantanYJelUUseRfz9rU4eNLp1eADnT_Hdb2JXLMWB1rd98PblM7pQD2ZmS4sbdjazS0_MqnMt_dTHinPFlGVIJD-YcS1TRYSZjA6ARGVeyYV51HDsFB6v5S2EQpoLF3e7aFoC75-q2a2JD57lMafpkQ5APUUXLhT3J4rTSv0TLB7gcIw42-WehW-7rwY9qPEt9jJcSK_w4tpLL6V9hCuPXWs8tpxs4o44DER09fvVg5foVBQn19srlu2wcpsurD7Ca5Rf_3NUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاسِ مشکلات و دغدغه‌های  مخاطبین الوفوری برای شروع سال تحصیلی جدید.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/688927" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688926">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: نتایج اولیه کنکور اوایل مهر اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/688926" target="_blank">📅 09:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688925">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای آکسیوس: محمدبن‌سلمان از ترامپ خواست مقرهای نیروهای مسلح یمن را هدف قرار دهد/ ترامپ این درخواست را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/688925" target="_blank">📅 09:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688923">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
جمینای گوگل برای ویندوز منتشر شد
🔹
اپلیکیشن بومی جمینای حالا برای ویندوز ۱۰ و ۱۱ در دسترس است و کاربران می‌توانند با میانبر Alt + Space به‌سرعت آن را روی هر پنجره‌ای اجرا کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/688923" target="_blank">📅 09:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688922">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7LxH98NySFbCVfXxT4IXthT3zRDJCJiixgZB_5bPL8Hb6rcuccfg2YpCC53bF93o378mBtVDAzHwRffcU7aku2BYM_UGJYXLmo9YdKbY2c10siMm_cjBCx6FizzJA2srUkLGWuXTgIWZLx8g_6SJsJ3LyZ0iANIWtHjkLTi9ocVNTaU4LgOzE9fqHF4OiX9UKXQ_JXXl-p9hAMEU4un36vMJCRk4BpBYw8dyMFBEMl1hMLz-jZWoxgUD_hAq0-guYfGoHDqh1PnmR6PZ-LkZHkEFUKn_0IkuQpOAKdAwt1eR67v58uC0CW9D5jdMq9-fOkNJqrnzr_rH9K8J5Bs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری بی‌نظیر از شاهین آبی با ترکیب رنگی خیره‌کننده
😍
🔹
برای ست کردن رنگ لباس‌هاتون از طبیعت الگو بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/688922" target="_blank">📅 09:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688920">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: ضریب ۲.۷ برابری برای اینترنت خارجی باعث گران‌تر شدن اینترنت شده است
علی جعفری‌آذر، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
ضعف یا نبود پوشش اینترنت و تلفن همراه در شهرها، روستاها و جاده‌ها، عدم تمدید یا بازگشت هزینه بسته‌های اینترنتی در دوران جنگ توسط اپراتورها و محاسبه ۲.۷ برابری مصرف اینترنت خارجی و نیم‌بها نبودن اینترنت داخلی باعث گران‌تر شدن اینترنت برای کاربران شده و توضیحات وزیر ارتباطات نتوانست نمایندگان را قانع کند و مجلس به او کارت زرد داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/688920" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688919">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdaaa3818e.mp4?token=RFqLJvfGC49671rlvzJXFecS1L4__fS-U6Q1dcR_NDRB-l5_eROg-73dzrBlVrgVeda0JD4vmu5kcYc5XvecHOOPo7gWN_u9i-Ng0DhsN655fpGUllJzQwcOBIVOU-QSMTG5t1tYifBJ1qkKklrt49tyquGctfySCYqRiS-yzJes3XymbDZuUAHhdpQ2ilhHur-f_CSb0eW4xPi_v3HX4IQ6SoArQP3fIVkxv1o0Us1FVJbmj_azu0Kqw5YU8DUCsJwXqZkQKeu-kJfz3YBnOye2sVXZzIFuC_Tlm8-NhL9MHrfTDEKnIT6nCDYajRk3NGVIS_0xc7gLA4Vb6EyK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdaaa3818e.mp4?token=RFqLJvfGC49671rlvzJXFecS1L4__fS-U6Q1dcR_NDRB-l5_eROg-73dzrBlVrgVeda0JD4vmu5kcYc5XvecHOOPo7gWN_u9i-Ng0DhsN655fpGUllJzQwcOBIVOU-QSMTG5t1tYifBJ1qkKklrt49tyquGctfySCYqRiS-yzJes3XymbDZuUAHhdpQ2ilhHur-f_CSb0eW4xPi_v3HX4IQ6SoArQP3fIVkxv1o0Us1FVJbmj_azu0Kqw5YU8DUCsJwXqZkQKeu-kJfz3YBnOye2sVXZzIFuC_Tlm8-NhL9MHrfTDEKnIT6nCDYajRk3NGVIS_0xc7gLA4Vb6EyK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «آقایان، آیا امکان دارد که با هم ملاقات کنیم؟»
🔹
ما با آن‌ها به شکل بسیار متفاوتی برخورد می‌کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/688919" target="_blank">📅 08:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688918">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35ee08b5.mp4?token=MXiJasV7pzN285EAqIVuKQJQFH54yIjkgKe1TT1wBm4z75OKRiZcMZG8Kho2rguBaw7PmpyVy6Orq4HLNiLYV1U-Ky9S0yzsKAgPq1a0BbZsD6NeOq5xo-9PqmOiZsejsDMoyTKc7g-5C8ilinXSaohztBp07fq45Sqgb92DDUl9Z58qUKud3N0Zihq6yYcsjOy_zthwihq75ti-VY7tytPPRN7-JF2bmGS4pCIedC183mc8rejDRMvMiWK93d9S-n2sSc4d7DuqW5mJzKKWqu7fpGLp0KSjwI1ty8Q0T5kEsIF2Zw2y5BqE-IbrgCml2cUTmg48YT90D3BiGxG3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35ee08b5.mp4?token=MXiJasV7pzN285EAqIVuKQJQFH54yIjkgKe1TT1wBm4z75OKRiZcMZG8Kho2rguBaw7PmpyVy6Orq4HLNiLYV1U-Ky9S0yzsKAgPq1a0BbZsD6NeOq5xo-9PqmOiZsejsDMoyTKc7g-5C8ilinXSaohztBp07fq45Sqgb92DDUl9Z58qUKud3N0Zihq6yYcsjOy_zthwihq75ti-VY7tytPPRN7-JF2bmGS4pCIedC183mc8rejDRMvMiWK93d9S-n2sSc4d7DuqW5mJzKKWqu7fpGLp0KSjwI1ty8Q0T5kEsIF2Zw2y5BqE-IbrgCml2cUTmg48YT90D3BiGxG3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ درباره پایان جنگ ایران:
من نمی‌خواهم بگویم دقیقاً چه زمانی، اما فکر می‌کنم این اتفاق درست بعد از انتخابات رخ خواهد داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/688918" target="_blank">📅 08:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688917">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53bb0ad15.mp4?token=eJGjVqlLryMB3d_SJjNNvbFd0RFXbyzrKXG4vGQHpUVtKztgY1XM2udMF0Z34vvldwCHVt603Zpo3yA7KjkmsI_QsWsJa6P4JThahaDnSWILkZ5ZqIzGOFcXWOUy9C5JyTClSQKS7staZl0lXJq_JoecjKyHuPm2H2ezYNTieX-DSY9QvdnH18wSbCKY8T7ecVfMtn6NhVSzShhTlSLiPF-knActB_g9AbOWUOgEwa49GBS_vA5qHRBJ2xcA9W-APlDPnHX-qY9a6Z5P2A0B4aY7ngYAcgFI0NQ4N41rYXx4EyUUHog4WBWmjCgDkclHWIK5yBMCfnJ7V5orJ16pqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53bb0ad15.mp4?token=eJGjVqlLryMB3d_SJjNNvbFd0RFXbyzrKXG4vGQHpUVtKztgY1XM2udMF0Z34vvldwCHVt603Zpo3yA7KjkmsI_QsWsJa6P4JThahaDnSWILkZ5ZqIzGOFcXWOUy9C5JyTClSQKS7staZl0lXJq_JoecjKyHuPm2H2ezYNTieX-DSY9QvdnH18wSbCKY8T7ecVfMtn6NhVSzShhTlSLiPF-knActB_g9AbOWUOgEwa49GBS_vA5qHRBJ2xcA9W-APlDPnHX-qY9a6Z5P2A0B4aY7ngYAcgFI0NQ4N41rYXx4EyUUHog4WBWmjCgDkclHWIK5yBMCfnJ7V5orJ16pqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار فاکس‌نیوز: همه می‌گویند اگر می‌خواهید وارد ایران شوید، به طور کامل وارد شوید. فقط وارد شوید و آن‌ها را از بین ببرید
🔹
ترامپ: خب، شاید من این کار را انجام ندهم، چون انتخابات در راه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/688917" target="_blank">📅 08:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688915">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
قیمت نفت به ۱۱۰ دلار رسید
🔹
قیمت معاملات آتی نفت خام برنت در جریان معاملات شبانه با جهشی نزدیک به ۶ درصد به ۱۰۹.۹۷ دلار در هر بشکه رسید که بالاترین سطح آن در چهار ماه گذشته محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/688915" target="_blank">📅 08:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688914">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJX9RnM2r6uccL_hXKEENMmvC2KG6N8MVFoR5QvSBjUXVpVtWfEqZ1hOnqIFYhVFJTl1arEt_TUAQ5xOE0t70XBRHDM-yXIpiM1hwdmEQZsmcUSMnBs-sQipQehvQweea3-kSB5SC4n4lAhVvIzpRMD0qP8mZ02xEdLDJDu9byhkra5OXtT7zubTfkuQ5ywM6ZW3Ndj7J8Gn7lawmPhyuQ2uoQH73k-l-gaT8aKLacQcPSjeIFl1d2EXPW1uq-kZw-odkSiIfy1-Bc1aZdtxBQRcTMnRy1jWZJssDqD0JdQH7bd6qwxeGOWyZKGHD92kDWBvnJItPTxIn23qdt-yew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در واکنش به تهدید عربستان برای بمباران شدید بندر المخا، محمد الفرح، عضو انصارالله، منطقه نفتی رأس‌تنوره را تهدید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/688914" target="_blank">📅 08:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688913">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b1f0f285.mp4?token=guhFgI4jy2q5GaRGjQbO4mhtuW0htbEuUou4G-YReW4UEsjEecz_-3pisc_e2qOr78uiBtYX_QntEIAQXSZxd7y9haQhdvd_kj2NB17614Tl7Nr8Y3Wgr09c2aNHrrfWbBZOdm03sf2byh5rX7qd2ZwJL3u6W8apUCIIOrykOPerAZ9FvSbG0h2b9Hz0wGsq-GNX5Vs1XJP-DV_JeQH6iFfx6Uw2fcsY-v4rbvB8Is7umZjHeDjKVm7khy4-YdI9O4_F8GPy6MU5t3pCmiwt779j3ksD8MzYNs7s3JT7qW4GJrJMMzh8sITabnUCttQ53nd8tEBGLjEy3FO-85IGUhK8B4P2cy42fpHOEfzSs9TZByFOinQJtMpGnI10ns60MCT9iQGjDOLClKUodxofblQYdQ7inKoDTijXwcEFCwtn2mZqvMwPcUXzFPCHQnj8AnVBf8E1HdVZf51oE7GXfSizWO2qz8c0zVkO1wuzTsq9S8cTk1O7naxsZ5cUGOaKku6bZlTt8MpiXGMtuYGQkstRhPm5pJBkNhvQTFng6CuLPKJ9zLPObE6H28VttByVNgNssx-AeLdNxzB2JuWeeZ4Z_1ah0DnfIUGxbTu9uqmIsE5Rnz0MFrKH8nuPYUCbow6gkyeRcn5dNqeUIxivPCqPW9wcE6p9u_PUntkJaxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b1f0f285.mp4?token=guhFgI4jy2q5GaRGjQbO4mhtuW0htbEuUou4G-YReW4UEsjEecz_-3pisc_e2qOr78uiBtYX_QntEIAQXSZxd7y9haQhdvd_kj2NB17614Tl7Nr8Y3Wgr09c2aNHrrfWbBZOdm03sf2byh5rX7qd2ZwJL3u6W8apUCIIOrykOPerAZ9FvSbG0h2b9Hz0wGsq-GNX5Vs1XJP-DV_JeQH6iFfx6Uw2fcsY-v4rbvB8Is7umZjHeDjKVm7khy4-YdI9O4_F8GPy6MU5t3pCmiwt779j3ksD8MzYNs7s3JT7qW4GJrJMMzh8sITabnUCttQ53nd8tEBGLjEy3FO-85IGUhK8B4P2cy42fpHOEfzSs9TZByFOinQJtMpGnI10ns60MCT9iQGjDOLClKUodxofblQYdQ7inKoDTijXwcEFCwtn2mZqvMwPcUXzFPCHQnj8AnVBf8E1HdVZf51oE7GXfSizWO2qz8c0zVkO1wuzTsq9S8cTk1O7naxsZ5cUGOaKku6bZlTt8MpiXGMtuYGQkstRhPm5pJBkNhvQTFng6CuLPKJ9zLPObE6H28VttByVNgNssx-AeLdNxzB2JuWeeZ4Z_1ah0DnfIUGxbTu9uqmIsE5Rnz0MFrKH8nuPYUCbow6gkyeRcn5dNqeUIxivPCqPW9wcE6p9u_PUntkJaxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ سال پیش، ۱۱ سپتامبر، روزی که آمریکا از طرف یک عرب اهل عربستان سعودی که در پاکستان مخفی شده بود مورد حمله قرار گرفت و بعد تصمیم گرفت برای تلافی به عراق و افغانستان حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/688913" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
