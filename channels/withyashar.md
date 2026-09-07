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
<img src="https://cdn4.telesco.pe/file/RoZXVF4XL_9VAl7bGhhd-jQs7IyXEonstcbFuo-I8GrSh385wYJeuGojLacGxQNtyNzZDjL-iiAhg73ZKSQZ_mB1ySj22HZ-XpnJGiapxLhRakwcGAyPOOxVrz9294C-CljMKZbM6cbCvuxkCiiZlMGuniWiy1LaRy4wN8e-5yPEVjGUPOFDYBp-l4snIE6orhOVDevo0w4e0SNSwMpvs8HTkT5xd5ttCBMHZ1QNuZfVxx8lEXxRJMPFXc_cG3Qs3hSBvCsNBKRa-pltvZxnkVLGZo4sLfxz_9lT5kZ8QYyPOLTVTaXuv5KhVEKLlUjANMwMRRoUVUQlUxDj630anw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 449K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 02:24:48</div>
<hr>

<div class="tg-post" id="msg-22525">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh2a_g4FfWgeZlBRWVEmm5EdPUHDA7EnhWxJqLSRuSoB4ZDfPow4AGA8PhwfzKfu1MLB4s2dkkVA4dfvM8BCi2NbqdteDOAC5xCyh2cr8XhbHaARFQa0uVCv8HqLQ6kXjAthjc1vPw_H3WVpYIH6PQYU5vwwPu7r6hu9kexkz0f6Sry07VUJDFD2QJEHXTYo4AgBOX2o9j8LMNJ158CF7L0Qb1LPylOGxdL790itD_GjnazO6t92oXaa4v6eKp9jbITL1nLLFguRQsX_59mhFFKT7NbOPf-iFpskDUVqM_i8_PVEE-iDYHHGZ1Ijig9AHyLoC8ZpOYIlQzTg00k61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : نیرو دریای ایران
@WarRoom</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/22525" target="_blank">📅 01:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22524">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش هایی ااز پمپ بنزین پاسداران و پیروزی هم دارم ، ایست شدید و چک کردن گوشی ها هم انجام میشه کاربری گفت گوشی دوستشو چک کردن و گرفتنش
@WarRoom</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/22524" target="_blank">📅 00:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22523">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بوشهر صدای تیز اندازی گزارش شده
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/22523" target="_blank">📅 00:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22522">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش ارسالی تایید نشده : پمپ بنزین شهر ری‌در همین لحظه به آتش کشیده شد
@WarRoom
🚨
🚨
🚨
در انتظار تایید و فیلم ها هستم</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/22522" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22521">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1Fu9jEQIH62zjCKdsvSwkxqz7CA0Y6gaVnIuzy4E0oazKdtnW0oGv_SPp8y5tWBVPJLC2kC8k8YjIvnlcu6Mi0J6FPQFcBr0jSa2-MzC_hI7a-BlffDsSRLCv_2ni0pQo5jXFhkNK_grjs-khts8gIFn5gFK7TMtnB_fmHEmk1ygmhxukURtd33yesMP8EpHuO2LORTCIVzlI9v6YfYCbdIXN9wdgNlE9JvGqqdOhIY9tp2ZFmMwylqZgUuL098Rszvuq6eSnYIJANYSnyNcXMXYmueihIMUPtjz1Iu6kIozw8JzpJ5EJOq9rWDTXL1l2ctvII4I7qvMEyiT262TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک فروند هواپیمای جنگ الکترونیک و تهاجمی ایی‌ای-۱۸جی در جریان عملیات پرواز شبانه، از عرشه پرواز ناو هواپیمابر جورج اچ. دبلیو. بوش به پرواز درمی‌آید؛ این ناو در حمایت از اجرای محاصره آمریکا علیه ایران در دریای مکران فعالیت می‌کند. تا امشب، نیروهای فرماندهی مرکزی آمریکا برای اطمینان از اجرای کامل محاصره، مسیر
۹۴ کشتی
تجاری را تغییر داده‌اند، ۳ کشتی را از کار انداخته‌اند و ۲ کشتی را با سوار شدن نیروها بازرسی کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/22521" target="_blank">📅 00:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22520">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نرخ سوم بنزین, از همین لحظه ۱۰،۰۰۰ تومان شد
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/22520" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22519">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کپلر: تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
بر اساس داده‌های شرکت کپلر، که در زمینه اطلاعات، داده‌ها و تحلیل‌های مربوط به کالاها و کشتیرانی فعالیت می‌کند، تردد کشتی‌ها در تنگه هرمز هفته گذشته ۲۸ درصد کاهش یافت و به ۷۷ فروند رسید
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22519" target="_blank">📅 23:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22518">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxNyuvsD724Ke2BxCgY7pBlaIlAS4um-eFBqqjSVaIFZK1leWBjzegTz7fDszU5q0R_rJB52_IKxrXbRn-fsNnkAUYvx-gvjohYPwdstbOOTAx0KzdpySnec0BywGpvr-FNj4KBsAnFECOT3pzSaY5wC-hZsfebal3yM2tz-mZ2G9hZz5YTAMSGQmGC7fP08koeEG7TathS-nn8WBtWaWLrKtC5qjxUvNfheojSGyaSwpBb--4eaG_5MkMa_m1m_hM1q7cNWrmLWa8d-ZKh_5is-7o7auQ-lvABkL13zYaDf39SNjOmYlQSiIbVomEZAVLdVFfOjGf5o7ifysGLnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : چند پرتاب از سیریک به تنگه و صدای انفجار از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22518" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22517">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=IKoWD63Bgxgd9Qfi3ij7trjFXLwafRGN7uVVxUw2iDcpBQEw4ur08ugjgFvzHIkTKnSxjVAw0bO6mURp81mOeXCCRY2uftO36QkZhPFqZE4t-HtiVtyM0PavlyWhaEGo66-M6P1_H5j_ClmsQ18stqPH0WxoOHKDCGCtqOYbkwlMM_aZLZNT9a5MzDm3lEdJl1QWVTwyLnfmOKNkIJ-q3e7Sk0gqS92cllNNzCpKKKwjmEOV0XdxRRrChdwu4P5NbF9W7HajK47PDvuKG1Ln7nuifN3UWw2non0bbdYyXsQeqLErv9tW6MPRkUHC_CNYJ-pTeJdYEw6OUhHjkJNljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e71f020c05.mp4?token=IKoWD63Bgxgd9Qfi3ij7trjFXLwafRGN7uVVxUw2iDcpBQEw4ur08ugjgFvzHIkTKnSxjVAw0bO6mURp81mOeXCCRY2uftO36QkZhPFqZE4t-HtiVtyM0PavlyWhaEGo66-M6P1_H5j_ClmsQ18stqPH0WxoOHKDCGCtqOYbkwlMM_aZLZNT9a5MzDm3lEdJl1QWVTwyLnfmOKNkIJ-q3e7Sk0gqS92cllNNzCpKKKwjmEOV0XdxRRrChdwu4P5NbF9W7HajK47PDvuKG1Ln7nuifN3UWw2non0bbdYyXsQeqLErv9tW6MPRkUHC_CNYJ-pTeJdYEw6OUhHjkJNljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : سلام یاشار این اوضاع امشب قشم یه ماشین بزرگ سیاه هم جلو بود پر آدم
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22517" target="_blank">📅 21:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22516">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">یاشار خوبی داداش
داداش تهران به شدت جو امنیتی شده من رفتم بنزین بزنم غروبی تو تمام خیابون ها داره موتوری‌های یگان ویژه میچرخه،سره میدان ها یگان ویژه وایسادع حتی جلو پمپ بنزین ها
رفیقمم از پاساژ علاالدین گفت که خواستیم اعتصاب کنیم اطلاعات اومد نزاشت.
داداش تهران منتظره یه جرقه‌است</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22516" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid</strong></div>
<div class="tg-text">یاشار جان من رفیقم تو اگاهیه
میگه امشب اماده باشن
ک ی موقع مردم نریزن ببرون
😅
😅</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22515" target="_blank">📅 21:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گزارش ۲ پرتاب از سیریک ۹:۲۰ دقیقه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22514" target="_blank">📅 21:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رجب طیب اردوغان، رئیس‌جمهور ترکیه، با انتقاد شدید از اقدامات اسرائیل گفت که دروغ‌ها و خرابکاری‌های این کشور باعث شکست تفاهم‌نامه اسلام‌آباد میان ایران و آمریکا شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22513" target="_blank">📅 21:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">روزنامه تلگراف انگلیس: رئیس جمهوری سابق ایران ( روحانی) خواهان برگزاری رفراندوم برای پایان جنگ شد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22512" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر در گفت‌وگو با CNN گفت
اولویت قطر بازگشایی تنگه هرمز، کاهش فشار اقتصادی و جلوگیری از تشدید درگیری‌هاست.
او تأکید کرد قطر به دنبال
راه‌حلی پایدار و گفت‌وگویی فراگیر میان کشورهای منطقه
است و معتقد است تحریم‌ها تاکنون نتیجه مطلوبی نداشته‌اند. همچنین قطر چند طرح، از جمله
یادداشت تفاهم
، برای رسیدن به توافق ارائه کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22511" target="_blank">📅 20:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22510">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U95bTNbZagiPbR1nrPePrzhDuK7IBoYzJtyfCyrEbqolKpC3Lf6sGZVi7Wi6DFujdiIplDsHbBCtyuFXIGe_5pWAxBJu7pcwmTv0ZTjGqTrdmQnsUcDkuur9mWGQDf1R5BV6-FS_G-1IWF8zeKITTtJDzDCpJlBykqqqBWHAqM42Fv4trmuR3_KlshmoWiMrc_9JntsxFR0zztEYG34R5oXrQKMJRiOATVnuqWxbSpGDdw73BgpOEQrG4IbYxX0ys_G9mFNVeWqVaXSUiwKga2-7XNyTehiZJ8KoY-ff0ERw-CINYh85xb_mncirhWMThGKCTfRtJOo00tauILY_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث، گزارشی از
وال‌استریت ژورنال
را با این مضمون منتشر کرد:
مسعود پزشکیان و محمدباقر قالیباف
بر ضرورت
پایان دادن به جنگ و مذاکره برای خروج از آن
تأکید کرده‌اند و خواستار تقویت اقتصاد ایران در شرایط فعلی شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22510" target="_blank">📅 19:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22509">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ : در انتخابات میان دوره ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22509" target="_blank">📅 18:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22508">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=Hw6eVqI_aNRZFG9o9w14gfn6LgA2pfASDw003VUP1Qq_bKiJ5kaP-iBIOVbDGn1EQjcDU72tYms-cW7xaFDa-dAI3KSxQq7FPC_LTSXnxzcEjcEixfEM6tABq9IW2eXK3pGrvBooryC6KLTLjmlJW5AWGbuqPTkAVjgfS1rBNUYsFMTA8YDr4-3Bx3sKJH8_JwrKiLwMsmSel-w_SULHmUTSVCQEaJUrVzUdqBo2UZXyY5EbEAzi_qleobbHFTG7HojcD65oXJs_TwRL_idXLb-vMX2iIkYN6yRFsCEeZrZYgS7S090Emp6TWI4wjEFNh5tS0JjnTnRgybdJ2f-0kR9XNPbMgMLvw9nOueDHEnB7VXW_yPulBRocIiSq7FTpi5xXDjMT5dCaNARxKAZmapRUMPr7azaOHqsaPyC7EqyDkqPaxM_ddLRc_XZehmgmw-ctpaEW19wVgnklh69H_ag_RV9-yyuvfFxqVSyGiTcjPcv-E6IE1L9zIXgQocgktMvY-DMk99XsJlL_i8GE3Du4m1EJtzvAAAYPaY3UDULkQlicsCuw3DpiaztnhML1jDeIC8chheypDgDX8Aupl_iu-22K_6ZfVb8WkNC0Vu_tQlyWXtXyc3tvimjyWxucq3_6_1YAeMUnY8AuDho6JNX4FNH83wgDZvpYA8Q9TWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688ebf7bb6.mp4?token=Hw6eVqI_aNRZFG9o9w14gfn6LgA2pfASDw003VUP1Qq_bKiJ5kaP-iBIOVbDGn1EQjcDU72tYms-cW7xaFDa-dAI3KSxQq7FPC_LTSXnxzcEjcEixfEM6tABq9IW2eXK3pGrvBooryC6KLTLjmlJW5AWGbuqPTkAVjgfS1rBNUYsFMTA8YDr4-3Bx3sKJH8_JwrKiLwMsmSel-w_SULHmUTSVCQEaJUrVzUdqBo2UZXyY5EbEAzi_qleobbHFTG7HojcD65oXJs_TwRL_idXLb-vMX2iIkYN6yRFsCEeZrZYgS7S090Emp6TWI4wjEFNh5tS0JjnTnRgybdJ2f-0kR9XNPbMgMLvw9nOueDHEnB7VXW_yPulBRocIiSq7FTpi5xXDjMT5dCaNARxKAZmapRUMPr7azaOHqsaPyC7EqyDkqPaxM_ddLRc_XZehmgmw-ctpaEW19wVgnklh69H_ag_RV9-yyuvfFxqVSyGiTcjPcv-E6IE1L9zIXgQocgktMvY-DMk99XsJlL_i8GE3Du4m1EJtzvAAAYPaY3UDULkQlicsCuw3DpiaztnhML1jDeIC8chheypDgDX8Aupl_iu-22K_6ZfVb8WkNC0Vu_tQlyWXtXyc3tvimjyWxucq3_6_1YAeMUnY8AuDho6JNX4FNH83wgDZvpYA8Q9TWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تفنگداران دریایی و ملوانان ناو آبراهام لینکلن، مشغول عشق و حال در کلابهای  پاتایا، تایلند. @WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22508" target="_blank">📅 18:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22507">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد: در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را «معکوس‌کننده‌ی انقلاب» می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده، معکوس کند. در مورد ایران نیز تأکید می‌شود…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22507" target="_blank">📅 18:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22506">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول،…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22506" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22505">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الجزیره: ایران به آمریکا اطلاع داده که در صورت اشغال کامل تپه علی‌الطاهر توسط اسرائیل، مستقیماً وارد عمل می‌شود، این منطقه محل استقرار تاسیسات مهم و استراتژیک حزب‌الله است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22505" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22504">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سی‌بی‌اس نیوز:
وزارت دادگستری آمریکا در حال احیای یک قانون قدیمی مربوط به
توقیف کشتی‌ها و محموله‌های نفت ایران
است تا بتواند نفتکش‌های ایرانی را هدف اقدامات حقوقی قرار دهد. این موضوع بخشی از فشار اقتصادی آمریکا بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22504" target="_blank">📅 17:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22503">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=LmZaUfFR0CFQmLy6xznsmUe2i7nkO6JdWGLXuJ6niqouoH0h-7Yav_ZwU81RUT5lgYrim1fQZIurD2i2t7hcHEUGCyV_0XJaSQSamlx6zv5xTk-FLuaK_uRIRueggomqeHxEJJZhWIhlNmevtm8a0XtzhokSE7igjCWrS8pbdEIIIbN8xSwAv8vCvcAizur-K6YKFbIaLh0_0GThd5Ue1ry835htLXh7vFLb4Fr8v_6G7UQzKuzXtWijN9Xa7spYnwCS5DlaFc0GdoHkdA7NbsoGoEKtxApLU_eQItXZmGPXwFiJ4axXoDyk_4L6E-RPk7ebQ0tKuNe8gby32IthsQZgDws-relZAiKGeos-JskYUXmHxC3mUCQzWOGj7sdFoVjy__AfiLVfn8CC4WdYr4DMTmGsOUsGJvSw2GudbJse0eI1aztU35_g12JZ-oKBAU9wp5IE4L6AgIhxsQzT268k7D2Vo8Bck-l8-m-9hUK9sNNh8k5uQ6Iu9WOFqx8HznmEfAGcdH1exbaXneoPaizXU47Egxft7IlqI_p0vAGU8EOUyRy2A1c3yGc45lUWVNdyyCEj9-RWjX1PNwLlzCWDHuc3z9BwDMBXn8eLoBDHY6PwyF5S4syRdZgbZTdUMGhT-_WtB3D5JtF6VMoI0IK-2eCLQ4l3Gop6nwWRlhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dd84c2849.mp4?token=LmZaUfFR0CFQmLy6xznsmUe2i7nkO6JdWGLXuJ6niqouoH0h-7Yav_ZwU81RUT5lgYrim1fQZIurD2i2t7hcHEUGCyV_0XJaSQSamlx6zv5xTk-FLuaK_uRIRueggomqeHxEJJZhWIhlNmevtm8a0XtzhokSE7igjCWrS8pbdEIIIbN8xSwAv8vCvcAizur-K6YKFbIaLh0_0GThd5Ue1ry835htLXh7vFLb4Fr8v_6G7UQzKuzXtWijN9Xa7spYnwCS5DlaFc0GdoHkdA7NbsoGoEKtxApLU_eQItXZmGPXwFiJ4axXoDyk_4L6E-RPk7ebQ0tKuNe8gby32IthsQZgDws-relZAiKGeos-JskYUXmHxC3mUCQzWOGj7sdFoVjy__AfiLVfn8CC4WdYr4DMTmGsOUsGJvSw2GudbJse0eI1aztU35_g12JZ-oKBAU9wp5IE4L6AgIhxsQzT268k7D2Vo8Bck-l8-m-9hUK9sNNh8k5uQ6Iu9WOFqx8HznmEfAGcdH1exbaXneoPaizXU47Egxft7IlqI_p0vAGU8EOUyRy2A1c3yGc45lUWVNdyyCEj9-RWjX1PNwLlzCWDHuc3z9BwDMBXn8eLoBDHY6PwyF5S4syRdZgbZTdUMGhT-_WtB3D5JtF6VMoI0IK-2eCLQ4l3Gop6nwWRlhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت , وزیر انرژی امریکا
:
ماموریتی که نیروی دریایی ما انجام می‌دهد فقط اسکورت کشتی‌ها نیست ! بلکه ، جلوگیری از خروج هرگونه نفت یا محصولات صادراتی جمهوری اسلامی میباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22503" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22502">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=ikg10pvffh72wfNFb6qHdwQlw0dPxYA6dp9bKaIbIQKLMsthAgCxcSZPeh4ustJ3WILWiWbfbgoCEMXHWs5c_CqbeuE_TviZJLS4qqO8ykliuxGDNU91hYmqF68almn-i3LlDo6QSnSgnash0XvNHFoxvxKOPzl7Poa6_Yv7craj4ZLoY5dCaSLRq8CDqlO5z8FdTiwp1k2rVwYv_eEy5Ev5roplBnT6ZBk0uEZokG9UaYB_8-l9cM2w5x3Ql9a-KDzA-VloYfbNNZARGtgXmm4jBPG681eKvplFVCu9F4QpgotZG_zFwbKS8dutIxK4N1VGykZs6XAokUBlT8AsnERH49cHUv8DdSfbh1LugA39W8dmN0hBnibBZbE7Ak1syQWaNHGlLSGu_jRKQBUmMquYhTcXnEF5B_dlA6cHtmizyvb2o7QDiwbvcXHlL-Uh4YzWMqlXJY09Sh0a0_dPNsbsFbP9DdD5qu1_W-XmmDlY-kA6h7L6TrGjMYd6fMK5LHOLl3n8V2b_3_zF-bJD8HxK68i_DFtTh6WkGTBs3Y1ElWZbTf1zeEA3IvoR-6esJEH6_znsd6tnHnTgEKno_3raJDqs0h5jCzThUhLr3_DsIl3WxcpWxUFMYnVdvT9z6cBE0B_nWE_uLNuJW5tZIpqxAfUYr1XFacRN_EZ-te8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4abd87594.mp4?token=ikg10pvffh72wfNFb6qHdwQlw0dPxYA6dp9bKaIbIQKLMsthAgCxcSZPeh4ustJ3WILWiWbfbgoCEMXHWs5c_CqbeuE_TviZJLS4qqO8ykliuxGDNU91hYmqF68almn-i3LlDo6QSnSgnash0XvNHFoxvxKOPzl7Poa6_Yv7craj4ZLoY5dCaSLRq8CDqlO5z8FdTiwp1k2rVwYv_eEy5Ev5roplBnT6ZBk0uEZokG9UaYB_8-l9cM2w5x3Ql9a-KDzA-VloYfbNNZARGtgXmm4jBPG681eKvplFVCu9F4QpgotZG_zFwbKS8dutIxK4N1VGykZs6XAokUBlT8AsnERH49cHUv8DdSfbh1LugA39W8dmN0hBnibBZbE7Ak1syQWaNHGlLSGu_jRKQBUmMquYhTcXnEF5B_dlA6cHtmizyvb2o7QDiwbvcXHlL-Uh4YzWMqlXJY09Sh0a0_dPNsbsFbP9DdD5qu1_W-XmmDlY-kA6h7L6TrGjMYd6fMK5LHOLl3n8V2b_3_zF-bJD8HxK68i_DFtTh6WkGTBs3Y1ElWZbTf1zeEA3IvoR-6esJEH6_znsd6tnHnTgEKno_3raJDqs0h5jCzThUhLr3_DsIl3WxcpWxUFMYnVdvT9z6cBE0B_nWE_uLNuJW5tZIpqxAfUYr1XFacRN_EZ-te8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حاوی الفاظ رکیک ولی به جا
,
دقت فرمایید.
⚠️
جمهوری اسلامی در یک تصویر
، خودش لنگان لنگان با لباسی ژولیده، بدنی نحیف و لاغر،خرکش بدون تعادل همه پرچم ها را یکجا را بر دوش میکشد
😂
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22502" target="_blank">📅 15:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22501">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">روسیه و کره شمالی نخستین پل ارتباطی میان دو کشور را افتتاح کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22501" target="_blank">📅 15:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22500">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الجزیره: حملات هوایی اسرائیل به جنوب لبنان، از سر گرفته شده است. @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22500" target="_blank">📅 15:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22499">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=Q2hEVipXJ0S_7_QHqK-rM68xCVfkVAhjqeviDu4TIHwwPii5Ka84KzHBdic-arnQBf0WCcA80vA0i6l2kJpOHNwfRwBwxbqCznsjWn_Ctad54NOdyJaS5OPLND6L-TSsM4egn72PbikEsG1JlpyY8Nt6pCpw-Sc2Jwsne2Ip6nZCQlWw0rpFDSrL6ZpeeWH15S4TlOHDkHw8biCCTX96aykV6jub3WldZioyQ1GzzCJstxrQCaN7e6s59-l0oWtsPIQiWGJquP-64aCHsdZHoVXEyrKXrD9jBKzhv18GeT-YAB6MKZePvkshM0e162O7DAIhONAW8dyNTDVCCLG3Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b12d040c7.mp4?token=Q2hEVipXJ0S_7_QHqK-rM68xCVfkVAhjqeviDu4TIHwwPii5Ka84KzHBdic-arnQBf0WCcA80vA0i6l2kJpOHNwfRwBwxbqCznsjWn_Ctad54NOdyJaS5OPLND6L-TSsM4egn72PbikEsG1JlpyY8Nt6pCpw-Sc2Jwsne2Ip6nZCQlWw0rpFDSrL6ZpeeWH15S4TlOHDkHw8biCCTX96aykV6jub3WldZioyQ1GzzCJstxrQCaN7e6s59-l0oWtsPIQiWGJquP-64aCHsdZHoVXEyrKXrD9jBKzhv18GeT-YAB6MKZePvkshM0e162O7DAIhONAW8dyNTDVCCLG3Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ اگه را داشت ماشین ریاست جمهوری رو هم الان معاملشو بسته بود ، یه ایرانی هم گذرموقتش میکرد میاورد ایران دور دور
😂
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22499" target="_blank">📅 15:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22498">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یک منبع اسرائیلی به i24NEWS: مشخص نیست جرقه‌ای که باعث شعله‌ور شدن اعتراض در تهران شود چه زمانی خواهد بود، اما خواهد آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22498" target="_blank">📅 14:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فایننشال تایمز گزارش داد
تأسیسات نفتی شرکت آرامکو در منطقه جازان عربستان سعودی امروز هدف حمله جدید قرار گرفته‌اند.
میزان خسارت در حال بررسی است و به گفته یک منبع مطلع، ابعاد حمله با حمله ماه گذشته به این تأسیسات مشابه بوده است.
جازان به‌دلیل نزدیکی به مرز یمن، طی ماه‌های اخیر چندین بار هدف حملات حوثی‌ها قرار گرفته است. آرامکو در حمله قبلی اعلام کرده بود اختلال ایجادشده
تأثیر قابل‌توجهی بر عملیات یا وضعیت مالی شرکت نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22497" target="_blank">📅 14:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22496">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommorteza</strong></div>
<div class="tg-text">علاالدین داشتن اعتصاب میکردن اطلاعات ریخت بالا گفت باز کنید یا بازداشت میشین</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22496" target="_blank">📅 14:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromyasaman sh</strong></div>
<div class="tg-text">یه دونه‌ای
دلم گرفته بود داشتم گریه می‌کردم. وویست رو باز کردم گفتی زارتان زورتان خندیدم.</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22495" target="_blank">📅 14:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=R7R3FhYYl9EpgX2aqNCHo8HsWPMj3mjaT3HmCh7ca_DexhhHWdhQi_ZSFqrMM7r09YRcDSiawG3vTTTG2qHjXXMGppNUCSbPrhw2MqhBOmLBImfEN1aEQwbX0J5iOoApi0S-HKL8UnrbuvcS4UW-dnxVdorfkPf3PKzLmshyzdfXuOt0ZgquQSDyQ8bQv_l249IzI21IOQA5fw7Kip3AKaScBPV7z6nGArPxEv57nLHw-23YhuQW0yP9OUvsOm4yanCZexHhECE4WLysOqIRErNAJAiL7rjiOrb-mzWOga62LvJb8vdv8yj3sA9cYPDZoD8YuWY1AnaWzXY5isGEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2827c98c29.mp4?token=R7R3FhYYl9EpgX2aqNCHo8HsWPMj3mjaT3HmCh7ca_DexhhHWdhQi_ZSFqrMM7r09YRcDSiawG3vTTTG2qHjXXMGppNUCSbPrhw2MqhBOmLBImfEN1aEQwbX0J5iOoApi0S-HKL8UnrbuvcS4UW-dnxVdorfkPf3PKzLmshyzdfXuOt0ZgquQSDyQ8bQv_l249IzI21IOQA5fw7Kip3AKaScBPV7z6nGArPxEv57nLHw-23YhuQW0yP9OUvsOm4yanCZexHhECE4WLysOqIRErNAJAiL7rjiOrb-mzWOga62LvJb8vdv8yj3sA9cYPDZoD8YuWY1AnaWzXY5isGEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : مردم شریف ایران، شرایط ایمنی حمل‌ونقل کشور به‌شدت نگران‌کننده شده است.
در بخش هوانوردی، گزارش‌هایی از اختلال سامانه‌های ناوبری گزارش شده همچنین بعد از‌جنگ اکثر سامانه های راداری نابود شده اند و از ترس حملات خاموش کردن عمدی ترانسپوندر برخی هواپیماها منتشر شده است؛ موضوعی که می‌تواند شناسایی و تفکیک هواپیماها را برای کنترل ترافیک هوایی دشوار کند و خلبانان در موارد بسیار بصورت چشمی هدایت را انجام میدهند ، در ویدئوی تازه در این رابطه نیز یک هواپیمای کاسپین در فاصله‌ای حدود ۳۰۰ متری از یک هواپیمای تابان عبور کرده است.
در جاده‌ها نیز وضعیت بدتر است فرسودگی ناوگان و مشکلات نگهداری به علت هزینه بسیار بالا سرویس ، خطرات جدی ایجاد کرده است. تنها در تازه‌ترین حادثه، نقص سیستم ترمز یک تانکر حامل بنزین در محور سنندج–همدان باعث برخورد با خودروهای دیگر و آتش‌گرفتن تانکر شد؛ ۱۱ نفر در این حادثه جان باختند و ۷ نفر مصدوم شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22494" target="_blank">📅 14:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران، پیگیری کسانی که آن‌ها را اعزام می‌کنند و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد. @WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22493" target="_blank">📅 13:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو: ما به نابودی خرابکاران،
پیگیری کسانی که آن‌ها را اعزام می‌کنند
و تخریب زیرساخت‌های تروریسم در کرانه باختری ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22492" target="_blank">📅 13:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آمریکا و اتحادیه اروپا در تلاشن شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای تصویب کنه که پرونده هسته‌ای ایران رو به شورای امنیت سازمان ملل ارجاع بده.
جمهوری اسلامی هم تهدید کرده که اگه این کارو انجام بدید، جواب متقابل میدیم. بالاخره از ان‌پی‌تی خارج میشن.
پیمان NPT در سال
۱۹۶۸
برای جلوگیری از گسترش سلاح‌های هسته‌ای ایجاد شد و در
۵ مارس ۱۹۷۰
به اجرا درآمد. ایران
از دوره پهلوی
عضو NPT بوده و جمهوری اسلامی در سال ۱۹۷۹ از این پیمان خارج نشد و عضویت ایران ادامه پیدا کرد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22491" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22490">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22490" target="_blank">📅 13:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22489">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5pITdcVjxiF3hep_uNhVZ-9g3oItQZy9F41Cni7W8mk0-UtvF_1MoWoPD2LUEOz-f8uGlygSAXH73_czYeMtrYQjeCuNzMiQsGU09NHpti5XOrrfPRrNFbHJXe7MjqqHrCVb1Td5DM5WbYolD4T9jT3y1-WFCFrE90GZvTpomF7yFHHUv1CtPKa5bfIbWCR4vfZOdM-k5pGAjS3G60gyL_uAmPfJ7l8xQ9p8jvR7Isrh4QlRdHlhM7ZSGPtRRiLmMNxQqj52wUL061rxQ3OEU2Na8katiUaFKvWul1Es5WuJVDkwbPQxNwg8Q8Dxu9aVnXXu2CyUwksVMmpn3YSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث ویدیو برنامه مارک لوین را بازنشر کرد:
در این گفت‌وگو، ویکتور دیویس هنسون ترامپ را
«معکوس‌کننده‌ی انقلاب»
می‌نامد؛ یعنی رئیس‌جمهوری که قصد دارد روندی را که طی۵۰سال آمریکا و سیاست خارجی آن را تغییر داده،
معکوس کند
. در مورد ایران نیز تأکید می‌شود که ترامپ برخلاف سیاست رؤسای جمهور پیشین،
به دنبال مهار موقت جمهوری اسلامی نیست، بلکه می‌خواهد تهدید اصلی رژیم را از میان ببرد
؛ به‌ویژه
توان هسته‌ای و موشکی و ظرفیت آن برای تهدید آمریکا و متحدانش
. هنسون این رویکرد را بخشی از همان
«معکوس‌کننده‌ی انقلاب» گسترده‌تر ترامپ
می‌داند؛ یعنی
شکستن سیاست‌های گذشته و بازگرداندن ابتکار عمل به آمریکا
. نکته امیدوارکننده برای مردم ایران این است که در این نگاه،
جمهوری اسلامی صرفاً یک حکومت مزاحم برای مذاکره و مهار نیست، بلکه یک تهدیدی است که باید قدرت آن از بین برود.
این گفت‌وگو همچنین بر این ایده تأکید دارد که در صورت
تضعیف قدرت رژیم، مردم ایران و نیروهای مخالف جمهوری اسلامی می‌توانند نقش مهمی در تغییر آینده کشور داشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22489" target="_blank">📅 13:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbH4gfxSkgq19uS9IL7xQ3LjU3JsFja2xzz5hrROawnQgtP-KHl_-xZSfIx0qbAr2dAvfmKoGhgfccdUIVDhKplKSReWSeAsURSuMwZcmfVXZxswHeshbhLk3cIb9KLPkkVWzjujANnRlMSy2oNukmkO2miiMCtjJ-OeZbH1yBqSXqzhteLTHYu4H-GpqPlvhsFIMCBNM9buavB_RI_YQGl_-ghR6skcaEEKFDJJKwHpDQMQGRLpnUMZgdY2U8LjtEqDB5X1j7kynmj59gipVwDCquUK0YaTMw53jgM1q6CId67Dw9dICmFvk7QbgMH3uX6r1h0Kzb4rOY_Wl-GWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث و نظارت بر نابودی قایقهای تندرو
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22488" target="_blank">📅 13:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22487">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=gIG_GbIxgdVdX06EMo-BIo78zrWlxr9PM3p5UyvCj8gA6zINVvFXk8VEnM38yXkXUJBG0MNg06HJdeM0IHBu5dwHijheluwW5HIcC0Ti6PkvaI9EHWTfR7g9bOqRL_sVnlZCSuySsvK3WCbSjpHbfOG42ZvUMGLOuelycmr-XR7KNu2pW_M4IeU-UPhTohMgjo3NW0iUC2ryUOpe-29I7MhpuFuxa2yx8qlWQC1LFCwM4VViX7FvcCF96cbHhCTUM3wRghaH8ukKOeV0x7iDInjlTieciwPpcTKhz2izmlc2NeE02cHQYUcph6pgiHmkmN1hz991yWzeu6bm2ZzVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dbc57d78d.mp4?token=gIG_GbIxgdVdX06EMo-BIo78zrWlxr9PM3p5UyvCj8gA6zINVvFXk8VEnM38yXkXUJBG0MNg06HJdeM0IHBu5dwHijheluwW5HIcC0Ti6PkvaI9EHWTfR7g9bOqRL_sVnlZCSuySsvK3WCbSjpHbfOG42ZvUMGLOuelycmr-XR7KNu2pW_M4IeU-UPhTohMgjo3NW0iUC2ryUOpe-29I7MhpuFuxa2yx8qlWQC1LFCwM4VViX7FvcCF96cbHhCTUM3wRghaH8ukKOeV0x7iDInjlTieciwPpcTKhz2izmlc2NeE02cHQYUcph6pgiHmkmN1hz991yWzeu6bm2ZzVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام یکی از آسیب دیدگان چشمی به ناو هواپیمابر آبراهام لینکلن در تایلند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22487" target="_blank">📅 12:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22486">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش های
تایید نشده
از منهدم کردن یک کشتی جدید در
خارگ
توسط امریکا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22486" target="_blank">📅 12:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22485">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارسالی : سلام یاشار امروز از تعزیرات اومدن گفتن تمام لاستیک های کهنه که جلوی آپاراتی ها هستش باید فوراً جمع کنن کلا 24ساعت مهلت دادن برای جمع‌آوری گفتن به خاطر این دوباره ممکنه اعتراضات شروع بشه اگه مردم لاستیکا رو از جلو در مغازتون برداشتن و تو خیابون آتیش زدن  خسارتش رو باید مغازه دار بده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22485" target="_blank">📅 12:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22484">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بقایی سخنگوی وزارت امور خارجه: ظرف روزهای آینده، تفاهم ایران و عمان درباره تنگه هرمز نزد سازمان بین‌المللی دریانوردی ثبت خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22484" target="_blank">📅 11:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22483">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بقایی: بنا داریم در نشست مجمع عمومی سازمان ملل مشارکت کنیم به شرط آنکه آمریکا ویزایمان را به موقع صادر کند
فرانسه، انگلیس و آلمان به دنبال تشدید اوضاع هستند، حتما ایران در قبال اقدام نسنجیده‌ سه کشور اروپایی و آمریکا تدابیر لازم را می‌اندیشد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22483" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22482">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=daHztKY9159pFIW-qgekN47MqS0CEp4wnSDcDl9WVT21v2QYD9FB61GAT3xAqcbWj2QNsiZxEDcIjrHsO5eWkDbhQKCt4lb-JA56R92LoqBDOqlOXr2uCuuqVOVamF4iCzRFbVs03ZOhXxwWbTnvezjWVU7jD0sauObbagswyxcWB_FV3j8yePtqwN3sAXFCWXQ0kjBMwoSNXfkxO1gwjrgRNZ31yQXlni8C3uLAbT4xzGVJounUORpLqMuAZV4nxNvl-KLyjaV88CNLW0rB59y7-Aefld1e1BnFH8zh2-eLevgGvTH8G5DynJCVpyC2_Iuz0kBMTd3dmte_sj3sa1tLMYkxeB3Em6XSyDwI1vLTfP6iTnJBccrV3H3EoGOghMv8FkqUJnrXAck-D1KqSe8RTsF16_6PAlue5EOy1V3mImzRzQuUftDH43cqC6tMeFBAAPTXMnzSidFuj0ggP9Ydtjc_Dn31G7WOcS1SSMjwRwSypsQ-2gpCWMLTbDaTPuZ3ESKDNfvVpnUm70dEHw8ACoTx0WxakQ_76cAetucOG_trb6AB_h6OaUBe6geli81mEXVxcwGCmoPOH4qvg3jt0_0RaIZqiFgVzhYJf5L8BADWBRg-pfRmvvME_Z2Fdv-opGO-S-D78WvhkvwdqTl0VRcZktBR18YgQb7D_BY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b940d08b.mp4?token=daHztKY9159pFIW-qgekN47MqS0CEp4wnSDcDl9WVT21v2QYD9FB61GAT3xAqcbWj2QNsiZxEDcIjrHsO5eWkDbhQKCt4lb-JA56R92LoqBDOqlOXr2uCuuqVOVamF4iCzRFbVs03ZOhXxwWbTnvezjWVU7jD0sauObbagswyxcWB_FV3j8yePtqwN3sAXFCWXQ0kjBMwoSNXfkxO1gwjrgRNZ31yQXlni8C3uLAbT4xzGVJounUORpLqMuAZV4nxNvl-KLyjaV88CNLW0rB59y7-Aefld1e1BnFH8zh2-eLevgGvTH8G5DynJCVpyC2_Iuz0kBMTd3dmte_sj3sa1tLMYkxeB3Em6XSyDwI1vLTfP6iTnJBccrV3H3EoGOghMv8FkqUJnrXAck-D1KqSe8RTsF16_6PAlue5EOy1V3mImzRzQuUftDH43cqC6tMeFBAAPTXMnzSidFuj0ggP9Ydtjc_Dn31G7WOcS1SSMjwRwSypsQ-2gpCWMLTbDaTPuZ3ESKDNfvVpnUm70dEHw8ACoTx0WxakQ_76cAetucOG_trb6AB_h6OaUBe6geli81mEXVxcwGCmoPOH4qvg3jt0_0RaIZqiFgVzhYJf5L8BADWBRg-pfRmvvME_Z2Fdv-opGO-S-D78WvhkvwdqTl0VRcZktBR18YgQb7D_BY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاخ سفید : در روشن‌ترین روز، در تاریک‌ترین شب، هیچ پلیدی از دید من پنهان نخواهد ماند. بگذار کسانی که قدرت پلیدی را می‌پرستند، از قدرت من برحذر باشند... نور فانوس سبز!
کد سیگنال این پیغام
:در داستان اصلی «Brightest Day»،
Entity منبع اصلی حیات و نیروی زمین
است که پس از حملات نکرون و نیروهای تاریکی به‌شدت تضعیف می‌شود.
Entity به دلار آمریکا، منبع اصلی قدرت اقتصاد جهانی، تشبیه شده که بر اثر سال‌ها سیاست انفعالی و بی‌ثباتی‌های ناشی از جمهوری اسلامی تضعیف شده است.
حلقه فانوس سبز نیز نماد
اراده، غلبه بر ترس و ایجاد تغییر
است؛ و جهت‌گیری آن به سمت سرزمین ویران‌شده، به حرکت ترامپ و آمریکا به سوی خاورمیانه و به‌ویژه
ایران، به‌عنوان مرکز ثقل منطقه
تعبیر می‌شود. در پایان داستان، نور سفید نگهبانی را برای احیای زمین انتخاب می‌کند؛ این تصویر نماد
آغاز دوره‌ای تازه برای بازگرداندن ثبات و امنیت به منطقه
است.
پیام نهایی: پایان دوران مماشات با جمهوری اسلامی، اراده برای تغییر و آغاز روند بازسازی نظم خاورمیانه با محوریت ایران
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22482" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22481">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مدیرعامل شرکت فرودگاه‌ها:
۲۷ فرودگاه در جنگ آسیب دیدند
که آسیب‌ها در سطوح مختلف پروازی، باند، ساختمان های ایمنی، دستگاه‌های کمک ناوبری و بازرسی، ترمینال های مسافری و...بودند.بارها گفته‌ایم که بعد از آتش‌بس جنگ ما تازه شروع شده است.
بازسازی آنها کار سختی بود، ولی انجام شد، زیرا در بخش ساخت و ساز فرودگاهی توان خوبی داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22481" target="_blank">📅 10:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=oQWJGjJojS-C0lnA-Qv95rV3ULmCsq369n29lJbhEU3FuIyzjmwNJgsds4bi-Dq3w4KzssLyCKQEWKyQ5hpsSp4X9wNXLZNHQDKhDjGCDYnbsf7v5s6ssgYacpuOV2calArKgyHOTpbBGGRgmpi2kI60WxUNYxRykZU2-dw8Hsfqoi7SquM57Y3t2MuJADOSKY4FaTHMzB3_ZmFDKHXY3u4M1U3RldGjwLURckU07LjyAP5QZkfK9CQWoEfjXsBZHTBXQAFOfuOj_yPF22IzEoUYVadB1trx9Sys4A32pjBhjc_dOp4VVzcpAX76UmNNwiJG6lZHiFI5hmnkA5m2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4f398265.mp4?token=oQWJGjJojS-C0lnA-Qv95rV3ULmCsq369n29lJbhEU3FuIyzjmwNJgsds4bi-Dq3w4KzssLyCKQEWKyQ5hpsSp4X9wNXLZNHQDKhDjGCDYnbsf7v5s6ssgYacpuOV2calArKgyHOTpbBGGRgmpi2kI60WxUNYxRykZU2-dw8Hsfqoi7SquM57Y3t2MuJADOSKY4FaTHMzB3_ZmFDKHXY3u4M1U3RldGjwLURckU07LjyAP5QZkfK9CQWoEfjXsBZHTBXQAFOfuOj_yPF22IzEoUYVadB1trx9Sys4A32pjBhjc_dOp4VVzcpAX76UmNNwiJG6lZHiFI5hmnkA5m2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرگزاری عراقی «بغداد الیوم» گزارش داده بیش از ۱۵۰ نفر آزادی خواه ایرانی به محل اسکان دانشجونماهای عراقی گروه تروریستی «حشدالشعبی» حامی جمهوری اسلامی در دانشگاه سمنان هجوم برده و شماری از آنان را مورد ضرب‌وشتم قرار دادند. تعدادی زخمی شدند و ادعا کرده پول، تلفن همراه و ساعت برخی از آنها نیز گرفته شده. گزارش‌هایی از تجمع مقابل خوابگاه و محاصره تعدادی از دانشجویان عراقی منتشر شده است. پلیس رژیم جمهوری اسلامی در محل حاضر شد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22477" target="_blank">📅 10:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=ny9ig1GhZWEFapAiWHfCZlnFgGSgQFKs8anbU-uDxP7glkVaOz02TmNiv17WjB9RDiysUZnqKzhi4okF15e8hIeywr3QUWqHXMiF5914hz3Deml74h15Lyv1rAFSsLlmnsKN0suGpvubtXYGYEvfmIOL9rEBwsd63e5fLENzK_lEI-R4BOY4PWDNVcY1iGgrarrhLezs8LW0stkj0nYkr2ZFLNZ5Ld_RwsjKrhU0-7JtwLWkicVqqfyvVEBqCC3ZnWdZDoBM9P-2FCpXhnyK7H9pEYfeaWBxMiwtujmVd9W3VvlEhqRCdVYr2NFyxad5OQS0yUOPyDao664Gx5cNVI9PTGVeNTOj7y9YxQ5k3l2zrM1_jO6sVjaitBe0-42Kaa0TcpQpgp9hM50AW81jfs7Hi9_XtWAgcG6pBeJkpJuJIj1zzjMQG8vAp64PrRHOVcduXftgH7d0Nq0-u4Cpc5LEN9Ujd1tamgayPeeTSY-Zpqn_VR7HYnkMDpUAJFPBAj-SFr7R-pn2kQpjqiPzdhXPdCmd2NY2OSRnDp94qXipk5WGV6in2JpGmYr4lFp7O-0dk6NMhhMO1WrWV_H3bUZfHt6S9ZaU0Oy9dGiB1LL52YFJHIkmMr9hyZ6hQnzKfTJc3GTFNzJpIo9Fo68CPKIOqAtissMXEmPAeTjTF-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc3ca6006.mp4?token=ny9ig1GhZWEFapAiWHfCZlnFgGSgQFKs8anbU-uDxP7glkVaOz02TmNiv17WjB9RDiysUZnqKzhi4okF15e8hIeywr3QUWqHXMiF5914hz3Deml74h15Lyv1rAFSsLlmnsKN0suGpvubtXYGYEvfmIOL9rEBwsd63e5fLENzK_lEI-R4BOY4PWDNVcY1iGgrarrhLezs8LW0stkj0nYkr2ZFLNZ5Ld_RwsjKrhU0-7JtwLWkicVqqfyvVEBqCC3ZnWdZDoBM9P-2FCpXhnyK7H9pEYfeaWBxMiwtujmVd9W3VvlEhqRCdVYr2NFyxad5OQS0yUOPyDao664Gx5cNVI9PTGVeNTOj7y9YxQ5k3l2zrM1_jO6sVjaitBe0-42Kaa0TcpQpgp9hM50AW81jfs7Hi9_XtWAgcG6pBeJkpJuJIj1zzjMQG8vAp64PrRHOVcduXftgH7d0Nq0-u4Cpc5LEN9Ujd1tamgayPeeTSY-Zpqn_VR7HYnkMDpUAJFPBAj-SFr7R-pn2kQpjqiPzdhXPdCmd2NY2OSRnDp94qXipk5WGV6in2JpGmYr4lFp7O-0dk6NMhhMO1WrWV_H3bUZfHt6S9ZaU0Oy9dGiB1LL52YFJHIkmMr9hyZ6hQnzKfTJc3GTFNzJpIo9Fo68CPKIOqAtissMXEmPAeTjTF-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخیراً تماس هایی از مبداء نامشخص
(شماره نمایشی سوریه) با مردم بومی جنوب کشور حاصل میشود و درخواست میکنند که طی درگیری های پیشِ‌رو هیچگونه حمایتی از سپاه نداشته باشند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22476" target="_blank">📅 10:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS.A.H74</strong></div>
<div class="tg-text">سلام آقا یاشار گل خوبی من بندرکنگ هستم سمت دریا ساعتای ۶صدای مهیب انفجار اومد نمیدونم چی بوده</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22475" target="_blank">📅 10:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">العربیه: در حملات اسرائیل به کفررمان در جنوب لبنان تا این لحظه 9 نفر کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22474" target="_blank">📅 10:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد: داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود ۱۰ کشتی در روز رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22473" target="_blank">📅 08:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش صدای انفجار یا پرتاب موشک از چابهار
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/22472" target="_blank">📅 08:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز , تنگه هرمز در پایین‌ترین سطح تردد:
داده‌های کپلر نشان می‌دهد میانگین عبور کشتی‌های حامل کالا از تنگه هرمز در ۱۰ روز گذشته به حدود
۱۰ کشتی در روز
رسیده که پایین‌ترین سطح از ماه مه است. همزمان ایران اعلام کرده قصد دارد یک منطقه ممنوعه جدید در نزدیکی تنگه ایجاد کند؛ در مقابل، عملیات دریایی آمریکا همچنان فشار شدیدی بر مسیر صادرات نفت ایران وارد می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22471" target="_blank">📅 07:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSGMmQxFHdjFqH6JFX5NiUCcbPPq1MTVBMzY6HwdXVvaC7PKiWKGCACEEj7dwPUAMG7KCIYXfu-MHyuCzpxMsYKL6hH0SnFaX4ilOXouqFnEgznoMFucVeMMdt1y3EwPxRj15Lx_520dGjYtpq6Zfx7GqhSddlTcPKS6O5zbLzYIri-s8rpwgucSTHiMWHuBDPsmMsvRNmTgFz1tXRaYpfMnGlhplKi2wxMJm84jC_d_mTjqoKX5nGbb4NATUmsrVLnhzOiHASmAm3DSPuOD2MjBCf-RCXZYrV1dm2WCQV6F-ZvXnMg2IrQwjEH3ALc_pPSCkCjk6zWKCdCvxYgQhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : سلام یاشار جان امشب اینو دیدم تو خیابون تهران رو زمین بود ، به نظر از این تراکت ها تو تعداد پخش شده باشه تو شهر ، آخر این حکومت رسیده و جشن آزادی بزرگی قراره بگیریم
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/22470" target="_blank">📅 00:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pbpita0doYeyzyDqzDqsCLDo-1ut_-o3ENH-lDPU3bpkVeTVUXdagDuEFBDXCwq2KEH53-FoVD9zY2-t5N7p1ew1jrVh38oI_r2xNVAXVmc0ny8w-_0Pa7Qs0G5DXR8UUAcqHJE_H4W82KTEWXj3_9nylan50V_Lonzi7x5j4SlhfYUhYyQCV8_SwcPJ2qpkcNolVVXdU5-4Pjy3IJhsmNCgkQns97WsJBTuk7MedtJmhjXnMXgbgGYcKUYsCGfSvErWVHQfQWV4leW1MGwd-ZXbyqOtG0q3FDY9P5wmNMGcwgHvw4Zvu4TAVmxGWrbvGDavbXS_ifkIYhw3QVqlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنی که جمهوری اسلامی او را «شاه‌مهره» می‌نامد، اکنون در زندان قم جانش در خطر است، برای نجاتش کمک کنیم
نازنین برادران، معروف به
«رها پرهام»
، پس از اعتراضات دی‌ماه توسط اطلاعات سپاه بازداشت شده و بنا بر اطلاعات خانواده، اکنون در
زندان قم
نگهداری می‌شود. رسانه‌های حکومتی مدعی شده‌اند او
معاون و دست راست بیژن کیان
، رئیس اندیشکده «صدای آزادی»، بوده و برای
هدایت اعتراضات و اجرای طرح براندازی جمهوری اسلامی
آموزش دیده است. آنها همچنین مدعی ارتباط او با
آدام لوینگر، افسر سابق پنتاگون
و دیدار او با
تام کاتن، سناتور آمریکایی
شده‌اند. نهادهای حکومتی همچنین می‌گویند او در تدوین ساختار حقوقی دوران پس از جمهوری اسلامی نقش داشته است.
اعضای خانواده وی به من گفتند که او قانون پس از براندازی جمهوری اسلامی را نوشته و آن را به سازمان ملل برده است.
اعضای خانواده وی می‌گویند
او از نخستین روز بازداشت ممنوع‌الملاقات بوده و حتی اجازه تماس تلفنی و شنیدن صدایش را نداشته‌اند
و اکنون
کیفرخواست پرونده‌اش در حال صدور است
. خانواده نسبت به وضعیت و امنیت جانی او به‌شدت نگران هستند و خواستار توجه رسانه‌ها و نهادهای حقوق بشری به پرونده او هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22469" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIL5UpTxe34KzeVYl_KoZ7r-7wgd2cYiaFM45ehO9sYMCZmco2mqpTHxy8NispRESmYK4FX0jVUwkj7XcUK5uqc3_VA7zVIO35cvmZCXds6QYRQ_O1tCzkpY7Cb4QeflOh_1PfRAG9j-_iCsqL0OLeViqBeW6Dl4z9h1Y6ZsBice_RF50C-VgjblVXlCKnmYHb_wtCQjetBMO2clF8zkf_WL_X9FNdUy__WfJwjbEK9cNFRRa7LBnwuFVpF-k0ZkzfcWyRsNVVxWTo4dviUp_hYfarPIGu-mdIM52sxTXjdkuIbM6_RPhp6kI0A6PIJUYzCOzT8ZMk_GYmyaNW15gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند. @WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22468" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22467">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">درگیری میان نیروهای امنیتی و مهاجمین در زاهدان؛ بر اساس آمار اولیه، ۲ تن از نیروهای امنیتی کشته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22467" target="_blank">📅 23:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22466">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bitCwdYmjMHEP9j0EH1_OpLbdVzdxvNUp0XJpA2Nlo372sZcxkBogXIBnymuxugnoVD49oDLK4RmF-ngH4u1kzivvzeHarrNX4hjxS3MlpQfLDC06ube_Qzf7bjFJNuO4rOAvqcZt6DwZQqnXyYdjBeY99NjAGA2xHvebmLR6xENZY6qfhQpzmT6bR-MiNGNvBuf3RxtyKo29_YcDZZwKwRQW_pcS6b-fNDFYEsNifrf45aMsh3ygO4E5G4Drh5LI9aa4I46YtQSNIFkSNWaXG17_mBGn6nQbmtRAOOepXWkYHAm7VxqyQiDCl6wNq7KWwrMawX_ef02-FzvGM-PkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران کشوری در حال فروپاشی است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/22466" target="_blank">📅 23:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22465">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPb2Axfw2-H8cc2MQ01Q-iWvULGa2gbX_10FKYEkdkfYF5epsUaYGIfOyUvNW07LSGMHwp1SWSGOvlXJPoAhimAkqQOp1u3CNq1dd_5BUNa2xYRpdvm1FybvZhBTtqukwjqQ1ZXMMOeDI07SaojMBkggh12OgxD4eGTLLEjXeszKEUBaWEqjYuSM0TB8Rr_YBV5MiOJYovziEov4vreq6-L_vDsfINwV5OOIeg4mNWrPzynmYF5-g3nfNZwflLpYh6AfseqNyvHj7nZIaj6UxcypcV6qhMp50FGiDRIuKSUNFByZjpNdB4sUDDZfsaY6hf4wJTqlcCwpYawd-7gvMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : حجم نفت هرمز برگشته است!
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/22465" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZklIk10gORPOXnM1OLlaGigF5nbFtR1GiGImrGlHXA1RJrczWCTbcWYg7d4RwnlTVlPUmkLh-dk5T2ltIAmxwFFhbofNW_SxXYJ4YPM1Q6TwZSVZo7icX5CLmZZtTyaSSTGYzoJsTFa1r8FhMTZPuakfJbuIp7HMmMVJDE2jaJzw_wG1QrG2eX1X0jD4v9sOUDc_LkHeqPfiRJBGRwA1C3qQCA21k8aNAMZpOgm3Hd2RxBYvGlsVUOpx2yXqvsFfYVXK3HbkWPc2_Mf2TaDrizd_mL-zAwAfaO6sDfg25iNuYCtzcUYEMB6HbiU-UhEEA4A-tp4S_cF0ZFrUxfittg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : کابوس برایشان بساز
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/22464" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22463">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYjp9vpsiVjgMS_M8Wu36iwiwo_LpqBCZITs7LIkI41lXYRIbdh8XqCORBq3jNARC3o8tigs5svhEHzlUgIhBhCrrVZBwoez_i_a5MVl_XGmUTFeNxuP9pwxkuqe5wjlDfBjW5s1li0hU5XQojOiQlIz_baPRa_1X0gnPj__USi8jP5so07Pg6rKUoZQOnlW4Y8PG6eSHIccNZ9hLg_1rEXaixKL3i9m6vielScrjPMlhIfCZztni-8nJpfPTVzUi4pygeJ15QpIIXYzQjxv51QezCOs6LHLz2IwNlT_ORU-lsDGKgMnUx_YHl5g_nVJrhoOP4dtRfCH-drJMfmVlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : صادرات نفت ایران در حال سقوط است
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22463" target="_blank">📅 22:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22462">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ6r53UoCtv2drhz3dVsK-lQvCUjUQdsIPomnxP7VmHoNC0fdjCn9qFKJ6dMU3xIWGLGF1hn2xM2EV3hUak4-dCGd7hKtVNbizdi5w8ivt4o8wzm0Ctz0vlzYZOfzsSqwyrSl02MiSix_qHmz8T8LEQ2KAbAcw-VY2icel0fsJe37bUquALGy8iDJWy5__DlFgHxZbsM-pdVl2j-2vTpV4moVCOkf9sytC71zfkVNnYW7A9j0-4PjptzNzzxDkP2kNOY58omUJbj3idV02QmLAMmNYj-5IQBoaoDnXX2sUFl3fk8vosjKdTSShy5X9Sx_AKQ4lgup1djBt05Ti_35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
ایران دچار ابرتورم است
پول ایران نابود شد
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/22462" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22461">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbtR0Zp7hLfsgcZ2_9DWiJOBRCOM6lc-ZlMrcrIhpXk4pynjfEzp2QwudOt59HRtxE8EMAukPIJVGaKqPjn8Pp2bpcf3qaT7BZ89bwKrigMKUIwdrq8PYlvJ_iR9UsmxvXCbdjntpvDmJ5wHc5n1DW8_0izqOSNVHOhFG7I-TzPVcW3vgNh69LPSS18RuVj2dakSOt2S6Z-YWiWs3O3SIXSEC3o9zZGueGq8Ni0rj-oBFhSV-EiTuSi76KkTpqqjEhBQcfjoUJaE116aKysShCN2A8CrN3Cii_DCp4uQJIBzDPBEevQWLB2QcL-BMG8wbzBU9Y-fgk5NKoB9yDq7Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : خداحافظ خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/22461" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22460">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش اسرائیل پس از شلیک دو پهپاد انفجاری حزب‌الله به سمت نیروهایش در ارتفاعات علی‌الطاهر، موج تازه‌ای از حملات را در جنوب لبنان آغاز کرد. اسرائیل اعلام کرده
انبارهای تسلیحاتی، مراکز فرماندهی و زیرساخت‌های زیرزمینی حزب‌الله
را هدف قرار داده و برای انهدام دو مسیر زیرزمینی در زیر ارتفاعات علی‌الطاهر نیز آماده می‌شود. همزمان گزارش‌ها از
انفجارهای شدید و درگیری‌های سنگین در منطقه نباطیه و اطراف علی‌الطاهر
حکایت دارد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22460" target="_blank">📅 22:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22459">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCslDpQ-51cNWwPsPP33k0v_tpavCYyx480oq3GGFgXXcs0oaGWCrWCt032Anb1EI_nUFZ1BRDrTjMJA8IZQkTyqU7pk_51MbwaiEWmrNxutwDUNhL7EZpqOdp3sp641aP7JPieGCeGqnxNa8RVFH8xfNceauXc78aA_OC9o5IDZJi-9SunhM5VEBqH6VDWOH4l4qxdCZyFykA7wIDv8yBwaIbF7QkIL1DfNFOUyD0Cew_doT0lfHeKpUPajhN3pFGD-rdovgwO4oBD-26vOIPV8dca3-3zXVDMbR3X6DT6vODMAG91SOI3EDhA2bEFtZZNRQz8J6ksfH32ZU8SBVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: نقشه ایران رو برعکس کنید میشه تصویر من
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/22459" target="_blank">📅 21:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22458">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/22458" target="_blank">📅 21:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22457">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رژیم:نرخ سوم بنزین تغییر کرد/ سهمیه اول و دوم بدون تغییر
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند. افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/22457" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22456">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کان نیوز:
ارتش اسرائیل قصد دارد
شبکه تونل‌ها و زیرساخت‌های زیرزمینی حزب‌الله در منطقه علی الطاهر در جنوب لبنان را به‌طور کامل منفجر کند
و بر اساس گزارش‌های اسرائیلی،
در انتظار تأیید مقامات سیاسی برای اجرای این عملیات است.
گزارش‌های پیشین نیز از آماده‌سازی مواد منفجره در این منطقه خبر داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/22456" target="_blank">📅 21:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22455">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22455" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22454">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/22454" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22453">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin</strong></div>
<div class="tg-text">یعنی خوشم میاد شهید سید علی خامنه ای پدر ایران خیلی میسوزونه شمارو
😂</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22453" target="_blank">📅 20:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22452">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو: ما مصمم هستیم که مأموریت سرنگونی رژیم ایران را به پایان برسانیم.
پایان جمهوری اسلامی نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22452" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22451">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=ZKsnEdGrsQstHFgHxfiPFX1gNZzjLo-PegMfY7uErrsS6-ggyG8Tnt0RrkuNJafpXjCrYp1hfe5r_H3Id-ShRcYWpYmnUZQxCV1kr10GC_GkqoZ3Ss2-AQAY1BA-ZN_KGiWy9qxyjMrqP7rc-JP64oAKTS3C3bMXWEwGqA9amiE3lpuqseV9jK3EE7k7Eh4JxLVTia7vzhWP2IOXGMyhROIyj_nF1dTxUa0mrExOyMQ54ylsaVKFjANKaCWa-dCeHebqn-p2D-Y6h99784dDsIZRGwcR4lFb6wKGsODyFwrMQMmrFFKZJwKwOdT54XLnItUKTqm1edXNZK6Vahc4iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee397b868b.mp4?token=ZKsnEdGrsQstHFgHxfiPFX1gNZzjLo-PegMfY7uErrsS6-ggyG8Tnt0RrkuNJafpXjCrYp1hfe5r_H3Id-ShRcYWpYmnUZQxCV1kr10GC_GkqoZ3Ss2-AQAY1BA-ZN_KGiWy9qxyjMrqP7rc-JP64oAKTS3C3bMXWEwGqA9amiE3lpuqseV9jK3EE7k7Eh4JxLVTia7vzhWP2IOXGMyhROIyj_nF1dTxUa0mrExOyMQ54ylsaVKFjANKaCWa-dCeHebqn-p2D-Y6h99784dDsIZRGwcR4lFb6wKGsODyFwrMQMmrFFKZJwKwOdT54XLnItUKTqm1edXNZK6Vahc4iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جرد کوشنر: در دنیا چیزی به نام دشمنی ابدی یا دوستی ابدی وجود ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22451" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22450">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، در مصاحبه با
مارتا رادزاتز، خبرنگار ارشد ABC News
در برنامه
This Week
درباره ادامه جنگ و سیاست آمریکا در قبال برنامه هسته‌ای ایران گفت:
ممکن است دولت ترامپ به توافق هسته‌ای با ایران دست پیدا نکند و در عوض، توانایی تهران برای دستیابی به سلاح هسته‌ای را از بین ببرد.
رایت تأکید کرد هدف اصلی آمریکا جلوگیری از هسته‌ای شدن ایران و کاهش توانایی این کشور برای تهدید منطقه است و گفت
اگر توافقی حاصل نشود، گزینه نظامی برای نابود کردن این توانایی همچنان روی میز خواهد بود.
او همچنین گفت آمریکا در حال وارد کردن
«درد کوتاه‌مدت»
به اقتصاد و بازار انرژی است تا به گفته او به وضعیت بلندمدت بهتری برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22450" target="_blank">📅 20:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22449">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بهنام صمدی خبرنگار بورسی: از امشب نرخ سوم بنزین ۱۰ هزار تومان خواهد شد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22449" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22448">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f35315292.mp4?token=lyhWxVYZWMBBO9ZrXxG-Zj0AIm56Q99bWNUUffJ5RCI55tZ6Enw2NzLAY3mG2PGkbeQGYmt2t8JnFuxOofzKRMMuY235hQpRgU-CScP6iepoL3iCDVx_m52YGv6yWsGmCXk4_26e_Qd2iVyFV4VYDx3VCscRDBR1kCV33Q7fGJ5TbUTrP7xbOQhaNOFjKBni2aXEy_d2gSf0D1GvcwIVIqEaRABY4J2C8igpLvzo_4pVbm5DHRx7N9S0j0tvZeiv4oDfpp8LzozensyPK-7oSOtUzvKp9AJBiJCGn_2o96Bbmy7Wwxccgi373FyaNVzboyaA7zICWZ72m_o-Y5CGuVJJMfFPAc16BKl-Lusjxn4sOjQ9UD7CHjiAxMl0nVo3UjH7K6eYZzJYNajFYwFhZo55XkIsEmNji7IZgRj4-fp7wfq2wfMHyYRrptFfAkxISJd8gzyfeW0YkvQMJ2NPhoKPGevH0K8Qdwh9HwIbXHjDsnsCD3ByayEZtpzueX5CxVSTMjNR_wp3SaSZZfoVesz2SUzTHoTvBFWp5wexiZWtodjLYJE5betAb6OrrjesfQCQ6230NmTA4porKJxdSo0YtA3QuXBc-yVYKA0ICMvOaEagzjpJOGi6vpVTmuSEdVg0-RPnYWFzMeXe8ELKfku8q4Ktm20fVl6wAdwNLBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f35315292.mp4?token=lyhWxVYZWMBBO9ZrXxG-Zj0AIm56Q99bWNUUffJ5RCI55tZ6Enw2NzLAY3mG2PGkbeQGYmt2t8JnFuxOofzKRMMuY235hQpRgU-CScP6iepoL3iCDVx_m52YGv6yWsGmCXk4_26e_Qd2iVyFV4VYDx3VCscRDBR1kCV33Q7fGJ5TbUTrP7xbOQhaNOFjKBni2aXEy_d2gSf0D1GvcwIVIqEaRABY4J2C8igpLvzo_4pVbm5DHRx7N9S0j0tvZeiv4oDfpp8LzozensyPK-7oSOtUzvKp9AJBiJCGn_2o96Bbmy7Wwxccgi373FyaNVzboyaA7zICWZ72m_o-Y5CGuVJJMfFPAc16BKl-Lusjxn4sOjQ9UD7CHjiAxMl0nVo3UjH7K6eYZzJYNajFYwFhZo55XkIsEmNji7IZgRj4-fp7wfq2wfMHyYRrptFfAkxISJd8gzyfeW0YkvQMJ2NPhoKPGevH0K8Qdwh9HwIbXHjDsnsCD3ByayEZtpzueX5CxVSTMjNR_wp3SaSZZfoVesz2SUzTHoTvBFWp5wexiZWtodjLYJE5betAb6OrrjesfQCQ6230NmTA4porKJxdSo0YtA3QuXBc-yVYKA0ICMvOaEagzjpJOGi6vpVTmuSEdVg0-RPnYWFzMeXe8ELKfku8q4Ktm20fVl6wAdwNLBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلنسکی، رئیس جمهور اوکراین: در طول یک سال گذشته، فکر می‌کنم ما قوی‌تر شده‌ایم. افراد ما کار بزرگی انجام می‌دهند و به دیپلماسی فرصت می‌دهند. بدون یک موضع قوی در میدان نبرد، یک موضع قوی اوکراینی، فقط اولتیماتوم وجود خواهد داشت. اما امروز، دیپلماسی امکان‌پذیر است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22448" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22447">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dc505262.mp4?token=cnW4oNeESqFD-AjCkZgH9fVaQ52UG5ibjZACxUS220loIGd5HAPyqFaQLQ0c8SjZBAY27sncO3lJ64YIz1fcEaYqp5x2iS8n_Fnq3RIQcaMP48P8Fwy9h6SMKl0G1zDcpACJfkVxDrspkjPyg9pUrmNGJcZMShfFEm_AkU8-KUuLYoCWgOcrf89IVwZAANuJuF99_0uIbBb9hZK77x5ny6Ea_S-ulwc0QOG0o5s_AeTKblxMRAif1RM7QFRHe2eZLoQPslCPWeCXVut6Q4mLPwLS7PxONzD5qGlN82tjg4KjpEHstlAiLlEFKNoMX_REvPksocudIeA2qh0jce7gbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dc505262.mp4?token=cnW4oNeESqFD-AjCkZgH9fVaQ52UG5ibjZACxUS220loIGd5HAPyqFaQLQ0c8SjZBAY27sncO3lJ64YIz1fcEaYqp5x2iS8n_Fnq3RIQcaMP48P8Fwy9h6SMKl0G1zDcpACJfkVxDrspkjPyg9pUrmNGJcZMShfFEm_AkU8-KUuLYoCWgOcrf89IVwZAANuJuF99_0uIbBb9hZK77x5ny6Ea_S-ulwc0QOG0o5s_AeTKblxMRAif1RM7QFRHe2eZLoQPslCPWeCXVut6Q4mLPwLS7PxONzD5qGlN82tjg4KjpEHstlAiLlEFKNoMX_REvPksocudIeA2qh0jce7gbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: هنوز کارهای بیشتری برای انجام دادن باقی مانده است. این رژیم در ایران به پایان آن نزدیک است. آن ضعیف است، برای بقای خود می‌جنگد، لنگ‌لنگان حرکت می‌کند و هنوز مأموریتی برای تکمیل باقی مانده که ما عزم جزم بر انجام آن داریم. این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22447" target="_blank">📅 20:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کوشنر: رئیس جمهور ترامپ می‌خواهد چارچوبی برای دستیابی به صلحی جامع و پایدار ایجاد کند، نه فقط پایان دادن به جنگ فعلی در اوکراین.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22446" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ویتکوف: ما برای از سرگیری روند مذاکرات به کیف آمدیم و از دستاوردهایمان احساس خوبی داریم و مشتاقانه منتظر دستاوردهای بیشتر هستیم. روسیه و اوکراین باید برای پایان دادن به جنگ امتیازاتی بدهند
ماموریت من و کوشنر این است که طرف‌های روسی و اوکراینی را گرد هم آوریم و شکاف‌ها را کم کنیم تا به یک تصمیم مشترک برسیم که به جنگ پایان دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22445" target="_blank">📅 20:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پرواز پهپادهای ایرانی بر فراز تنگه هرمز!
سازمان دریایی بریتانیا (UKMTO) اعلام کرد که پهپادهای متعلق به نیروی دریایی سپاه ، در حال پرواز بر فراز کشتی‌های تجاری در تنگه هرمز هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22444" target="_blank">📅 19:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=q8cczxQeTDWBz_VjQMm4aTb6zRPmKQx5eqKlyiCIW_KGu79HT_rRJp76OVxTDDAcV8LPLc4jNoTAqFDQpLX-HCV1i3_Zk96hJ95ja3W9CMWVn9qXD1XcULeie8zqoD_3cadBPLYJ8go7-w1zfVBgK5QpOF2HEdn_SAic5_O5g-7hiLcZ2A34NhEn6Qif0KC9cR74QWRWdXUg5xaovQeSUBdd4W3Zun5MetnW-4Hw3L7e8KZgYZ4WWXZxXvzkL3khV9T1y5xPhVPA6uSjJTpa9rknCnM7U1W8V7Aazy8vQJWHUtnCDo2LHQjir1d9gz0LcnLkREpkTSihiTSBMPEgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e697dcc2d7.mp4?token=q8cczxQeTDWBz_VjQMm4aTb6zRPmKQx5eqKlyiCIW_KGu79HT_rRJp76OVxTDDAcV8LPLc4jNoTAqFDQpLX-HCV1i3_Zk96hJ95ja3W9CMWVn9qXD1XcULeie8zqoD_3cadBPLYJ8go7-w1zfVBgK5QpOF2HEdn_SAic5_O5g-7hiLcZ2A34NhEn6Qif0KC9cR74QWRWdXUg5xaovQeSUBdd4W3Zun5MetnW-4Hw3L7e8KZgYZ4WWXZxXvzkL3khV9T1y5xPhVPA6uSjJTpa9rknCnM7U1W8V7Aazy8vQJWHUtnCDo2LHQjir1d9gz0LcnLkREpkTSihiTSBMPEgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو، نخست وزیر اسرائیل، درباره ایران:
آنها به ما حمله نمی‌کنند. ایران از این کار اجتناب می‌کند و دلیلش را هم می‌داند: چون اگر این اشتباه را مرتکب شوند و به ما حمله کنند، ضربه‌ای خواهند خورد که حتی تصورش را هم نمی‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22443" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8aijz7ueedMYotlTnAWumt61Mf-_jwlK_9SdQovfOEuAVH5tOcRFe8h6fIzjjJq4u0LVfIqqVYoWpXPH5ONZdpqUuETYwuwJCT9a5xkI4gFGc5T-pBjCwlA3wCR5iegySAhBCglI6kM7fPIXqfKz4Sh3i_y_BYAGIf7E0fBoGvpKU2f9ZV3xeOqQLC4zaMaKXISBcP6p5lII8x25Fv7894JjQtEmuRywbudEFFyx4FGRNLNPmde6RuzexAhaZ39O8Bbz_ui-cozoweuyZVsjM-MS1xeRRDuANQepEEIkCIsWq-me8eG8aJPmmWbbmDi6-hy1ofOUHs3wb9xRBsrBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث خطاب به رابرت دنیرو : حتی این احمق هم داره متوجه میشه!
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22442" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22441">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niLwl-OiWmhqWZLGB8IV_niLQnKmwV01WGLGrqbTQRvpicxZBg-kVtd5ZKa4jUiXNZOgcdN7-tVogcFvMNEbOLU6LHRv-zi0FBOwJEIb9Z_R15a37zkf2aBuTmqMJJraC_qMLZTIzRLyPaBIC28H9QN9RsLxSCqD05eLQXKHR0x8fVMtRczwa3rSc6WuHHpb2aD8b5fj5UuK211uhcAbQm7Oc4PAC-KPQne-NlAiAdeYt_vhEugboyW3wkT871w0yULzI7-oTNPSluI1XmKOzulMxnnOntep7wAMBUbtNUTd7lWcKpDGVlCWUJBnxVEVqQ05oCM4jv5uJExjFNrl4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استیو ویتکاف فرستاده ویژه آمریکا: از مذاکرات جدی و مهم با اوکراین راضی و به ادامه آن خوش‌بین هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22441" target="_blank">📅 18:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22440">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGxjja_tRKz3-3zIpNucxJRKyqF4nyjTgKC6USLSc9fWBI7oSQK2OPmZc3nZdmM_iHb0YUq0rEDlTDBbK_27QuBSQQgA6hzEplBaBdSHyhUcd4oswk3rrJ5FQYC70Bzb_1WRgKkYsakgT_zKIyHIgOIk1v72kRhkMEkp8bzufOLEwwL3dB1U5xf_UA0f__98VLvit7qxFGoUkMUT4zYKAN7wqaGingYsTwXa0AAEtfVTDAgOXbW1De4oyX-FZmpjJL7f6jAVpvo_bLm5DVJ0Q7OKkK4zq8OWIn7qG5kqT-Q_qJoTjuNO1QgDsSlyY9pLIDCG1Z0ntm34vk6Kpcnoqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ رنگ موهاشو تیره تر کرد
@WarRoom
😁</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22440" target="_blank">📅 18:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22439">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وال استریت ژورنال :
سالانه میلیاردها دلار از منابع مالی ایران
با وجود تحریم‌ها، از طریق حساب‌های تسویه بانک‌های آمریکایی و بانک‌های خارجی دارای روابط کارگزاری با آمریکا جابه‌جا می‌شود. در سال ۲۰۲۴ حدود
۹ میلیارد دلار منابع مرتبط با ایران
از مسیر بانک‌های آمریکایی عبور کرده است. شرکت‌های پوششی و شبکه‌های پیچیده انتقال پول، شناسایی این تراکنش‌ها را دشوار کرده‌اند. مقام‌های آمریکایی با یک دوراهی روبه‌رو هستند؛
سخت‌گیری بیشتر ممکن است به جایگاه دلار آسیب بزند و تساهل بیشتر، مسیر انتقال پول ایران را بازتر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22439" target="_blank">📅 18:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22438">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تلگراف: لیبی کلاینر، همسر یکی از سربازانی که پس از سرنگون شدن هواپیمایشان در غرب عراق کشته شدند، در یک پست در شبکه‌های اجتماعی نوشت که دولت ترامپ او را برای دریافت غرامت‌های مالی واجد شرایط ندانسته است، زیرا کنگره به طور رسمی جنگی را علیه ایران اعلام نکرده است.
تلگراف هم گفت پنتاگون از پرداخت غرامت به خانواده‌هایی که توسط ایران در خاورمیانه کشته شده‌اند، خودداری می‌کند، "زیرا آن را جنگ رسمی نمی‌داند."
اما نکته مهم این است که
پنتاگون در نهایت غرامتِ مرگ را کلاً قطع نکرده است.
پرونده‌ای که خبر از آن شروع شد، مربوط به بیوه یک افسر نیروی هوایی،
الکس کلینر
، بود. به او گفته شده بود فقط برخی مزایای مرتبط با منطقه جنگی، از جمله
combat pay
و معافیت مالیاتی، به دلیل اینکه «جنگ رسمی نیست» شامل حال خانواده نمی‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22438" target="_blank">📅 18:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22437">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX6PFWp1LnAdp43iUVpfx1taCNK5DFxcciiMq8moR29H4lPKfACbhPZY0p1KJdARrLDFRfpDrmdK7tus-dXic9rK1fnk7QCjGI6r2wwYrr4Q5M_gwKSkFxR4kDGS9NdEU5cCxoF2bBBvsGff3hvSXEntux7PW5j2ko_7d9rQJnwiVQg5VTrFoD2yNqRw14QcPqpIxh-HYhkC9rPghJwZEqAcXMHBj8tfP94nmB42HIvKqHYCJxMI6beFdV1F-K9-2fNIgpJKzHlLMZI4eSD3JPb5zu1SVvNfRZBbXeuCJhjkT7SiY-3wwFCuokoX_BJfPUphSahCn_6vwlYEiwIpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوه کلنگ گز لا (Kuh-e Kolang Gaz La / Pickaxe Mountain)
در شهرستان نطنزِ استان اصفهان و حدود
۱.۵ تا ۲.۵ کیلومتر جنوب مجموعه هسته‌ای نطنز
قرار دارد. مختصات ثبت‌شده‌اش حدود
33.7051, 51.7081
است.
@WarRoom
https://maps.app.goo.gl/LJq8rZ2kNdve6xiVA?g_st=ic</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22437" target="_blank">📅 18:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22435">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشهای بسیار از شنیده شدن صدای انفجاری مهیب در اراک
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22435" target="_blank">📅 17:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22434">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اتاق جنگ با یاشار : با تماسی‌که با منابع داشتم نفتکش هایی که دیروز که آمریکا هدف قرار داد ۱ عدد با مالکیت ایران بوده ولی ۲ عدد آنها فقط در اجاره ایران بوده که حتمأ بیمه هم داشته اند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22434" target="_blank">📅 17:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22433">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3N78dWTrvoCCjAZL-iO5B5cXqgqK08cot0dC2TYN8kmYwJXsZi_83GlIyGqj3Ctiv-A5cjVuJw2ZenO8Oq8YSs0RfNWjrbN8tXsusSBU4sjtv_jr9Esuz5DvPJ4XJZ6N3DhntL8-ZwePREMYSmMtlKPgYFc9cmqkAQSNJ9don2v1fxTHEYkgofyncEqGTJMn79Ypjhy5z16-GjMeaMVi6tgiu9p6CmrjPIkgI-xCiRqvmrLh6witX4LT8EY_EZrUu-A7IxaugkfbWB2aEcUTEZitOQkjDlUzlkM7zoZMTBM_eJKRBTKwUzRLGzw9T0bPbrnc3rSe7BYCdhdEa-CcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار  @WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22433" target="_blank">📅 17:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22432">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=nLJehuu_SSjVtR4wKeBZ18iwW0Odagbh5DYVQwAtwudEMIU8Hwkvrt3rljDxtr1BMYLJVD8QmYi9qbFQmDv9UVvtVhWZFhIaYPghmzU82xe0bsiOcp-4N6L3XEbnarXRdqb0HUuhaGGqbypUQBnZA1otw402ubJfMDFIFCTUvQ067pZDw0tL5qBTCd8WMMopbGHu1qNzvgzymEiskxTyk4vkOhszm5LKJleESAtYdBwf2Q1cY5PaL7tvU_maB04_xMKhRoTRRc_KVWHA0vmS_a470_h0F03hg9L-qv9cRYTf0Su9Eqsib-Ud6rBqirs6mb8dce8PiIAsSZr_oS2JtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e8d0bd6c.mp4?token=nLJehuu_SSjVtR4wKeBZ18iwW0Odagbh5DYVQwAtwudEMIU8Hwkvrt3rljDxtr1BMYLJVD8QmYi9qbFQmDv9UVvtVhWZFhIaYPghmzU82xe0bsiOcp-4N6L3XEbnarXRdqb0HUuhaGGqbypUQBnZA1otw402ubJfMDFIFCTUvQ067pZDw0tL5qBTCd8WMMopbGHu1qNzvgzymEiskxTyk4vkOhszm5LKJleESAtYdBwf2Q1cY5PaL7tvU_maB04_xMKhRoTRRc_KVWHA0vmS_a470_h0F03hg9L-qv9cRYTf0Su9Eqsib-Ud6rBqirs6mb8dce8PiIAsSZr_oS2JtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکار سوخترسان آمریکای توسط دیدبان اتاق جنگ با یاشار مانند پلنگ جگوار
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22432" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22431">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=osp8JwvxIh3wSgZwHWcZe5WqtghjkVSMVAkI-exYbqN1mz_IYWxBik3AMtmJ_onb4GN84sSkvhJn8qUyi4RVxMiWVcVA7qbS3VlNtUcURGgG6HaA3hFzJnqNqgfO_gGsAaK09X_THZG4yyDJhfW8M08eolvFiSRfSeG9ByhqTfG94efmslkI23al_wTzz6etzVNED0bvsaSK6znr2rQ8wEO0yGa8eyM2hbEUXZsKNeoBk65N7K2mgucVykVCDX169EPZsyWJ9iRHDksnPVWHshvjifFeolzcwvGDRiAeJz7tIWwt2O-Lrk4OqqQbr8zY3LFP2O6YpEXyrtZ9aSDDWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2dc5c16b1.mp4?token=osp8JwvxIh3wSgZwHWcZe5WqtghjkVSMVAkI-exYbqN1mz_IYWxBik3AMtmJ_onb4GN84sSkvhJn8qUyi4RVxMiWVcVA7qbS3VlNtUcURGgG6HaA3hFzJnqNqgfO_gGsAaK09X_THZG4yyDJhfW8M08eolvFiSRfSeG9ByhqTfG94efmslkI23al_wTzz6etzVNED0bvsaSK6znr2rQ8wEO0yGa8eyM2hbEUXZsKNeoBk65N7K2mgucVykVCDX169EPZsyWJ9iRHDksnPVWHshvjifFeolzcwvGDRiAeJz7tIWwt2O-Lrk4OqqQbr8zY3LFP2O6YpEXyrtZ9aSDDWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از موشک‌های هواپرتاب بالستیک Blue Sparrow استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به ۲ تن که از جنگنده شلیک…</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22431" target="_blank">📅 17:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22430">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_75lRcibUpOErA2tHujtdo0-rqYIQhrqycUbaZVA-VZuYgCYd7Qle-8Xx4i2NkhLjChFkw1edcy2h9jaM7_R-iKmqlkLwDeOo-jLIQrqN4bK3vOdf9DXWGSRYIa0vkLykNqabNTz9gKSqISn8yU0vxFZwHIqLZSfPynF_Z7QGiHXjuEwajELjX7Ubg7jqmh8980xlO_ipQ-loMzz_sHeBQa0bkD0hyHqZbN-MQrQUiIFLFpqZUHutOKTA3UJk6eU3RTlws0xM3Sugmq4rgPoEliIqwb0HM4es6PT5uIB8dtU4J-licOFHCc7_-jfKaH_cgICtj1rvAjBIxjdINmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگراف: حمله به بیت رهبری با موشک‌های «بلو اسپارو» انجام شد
روزنامه تلگراف گزارش داده اسرائیل در حمله ۲۸ فوریه به مجتمع رهبری جمهوری اسلامی در تهران از
موشک‌های هواپرتاب بالستیک Blue Sparrow
استفاده کرده است؛ موشک‌هایی با وزنی نزدیک به
۲ تن
که از جنگنده شلیک می‌شوند و پس از رسیدن به ارتفاع بالا با سرعت بسیار زیاد به سمت هدف شیرجه می‌روند.
گزارش‌های اولیه از پرتاب حدود
۳۰ بمب
به این مجتمع خبر داده بودند، اما گزارش‌های بعدی استفاده از موشک‌های Blue Sparrow را مطرح کردند. با این حال، مدل دقیق تمام مهمات استفاده‌شده هنوز به‌طور رسمی تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22430" target="_blank">📅 17:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22429">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">روزهای بسیار حساس در انتظار پرونده هسته‌ای ایران
؛ نشست فصلی شورای حکام آژانس بین‌المللی انرژی اتمی از فردا با حضور نمایندگان ۳۵ کشور برگزار می‌شود و پرونده هسته‌ای ایران یکی از محورهای اصلی آن خواهد بود. آمریکا و سه کشور اروپایی در این نشست چندروزه به دنبال تصویب قطعنامه‌ای برای ارجاع پرونده هسته‌ای ایران به شورای امنیت سازمان ملل متحد، به دلیل عدم پایبندی تهران به تعهدات پادمانی خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای هستند
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22429" target="_blank">📅 16:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22428">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22428" target="_blank">📅 15:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22427">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp2aa4x2r5eehLLrlyFNoe-hhfyIWkQagN57Jf4BgUttYjkZioTmTBDMrTGhIYllkJjPpr5Sd5G-nClWTDwOKitrMz_2dR6zNwGie0nViq8l0ttxp0oyy4XIIPApCKIGkHaVSu969E14glm26tfmneBP532lpkLjuYuJmJ8gLbL31JNE394AYLjG58zMUtWrIU_fAa1sLYscoPNo92RF3-XSMLeRvzRz60kQhLrnbGBtnmcGpAUNVzrJpo1VVXlOU9LJGoYapulH254IPnM3iSlUK4zvKcQUkrE6ddngqeKitjotpEKk68qDx2wBgnTysz4LuCpjZ0XpN8hru4yBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت جوری شده که حتی اوستاد هم نمیتونه تحلیلش کنه
😂
خدایاااا بسته دیگه
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22427" target="_blank">📅 15:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22426">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4gxVZa6tX9n7O13FnvjA5Tu0A-3AF3j5phSqR4okkL8-7LcThu1VHPfQfG1kRa0CXnHE1MmWYdsMm7B1KCVcjcQ3WBIRfMgw0NHDsycxoxz65PdnXxu45_kRdrzU9_UVPSlTiNnjUlJw7xQ17Bl-gTeXzB06mbx1bxmqPwO0w0WB26ucJJ-90R4D4UWR4--QaVE5cSY5zyEuD5PVZupVQSmEdnW8szNYrlUYNWpYuO71t0zGi2GBTEkxqH8In-L16s0dS3XCCarFsjmOJbGAdCuXx0ffh1FuwBor5lxcgVgAOpBvvzUuCG7zVatYW3pNboUX1hdBZUfxAkyHPPUIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در حالی که نیروهای سنتکام همچنان به اجرای
محاصره دریایی علیه ایران ادامه می‌دهند
، بر فراز آب‌های منطقه‌ای گشت‌زنی می‌کند. تا امروز ۱۵ شهریور، نیروهای آمریکایی 92 کشتی تجاری را تغییر مسیر داده‌اند، 3 کشتی را غیرفعال کرده و 2 کشتی را توقیف کرده‌اند تا از رعایت دقیق این قوانین اطمینان حاصل کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22426" target="_blank">📅 15:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22425">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">منچ‌ اوسینت : از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در مسیر جنوبی تنگه هرمز، پس از شلیک هشدار نیروی دریایی سپاه، تغییر مسیر داده و برگشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22425" target="_blank">📅 15:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22424">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز:
اوپک‌پلاس امروز در حال بررسی حفظ سیاست فعلی تولید نفت برای ماه اکتبر است و انتظار می‌رود افزایش بیشتر تولید پس از ماه سپتامبر متوقف شود. رویترز می‌گوید
جنگ ایران و اختلال در صادرات نفت از تنگه هرمز
یکی از عوامل مهم این تصمیم است؛ در عین حال اعضای اوپک‌پلاس همچنان پایین‌تر از سهمیه‌های تعیین‌شده تولید می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22424" target="_blank">📅 14:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرگزاری i24:
ارتش اسرائیل امروز یک رزمایش ناگهانی و چندجبهه‌ای با نام
«Breaking Dawn 2.0»
آغاز کرد. این رزمایش به دستور رئیس ستاد ارتش اسرائیل انجام می‌شود و هدف آن سنجش آمادگی نیروها برای سناریوهای همزمان در چند جبهه و تقویت توان ارتش برای مقابله با تهدیدهای ایران عنوان شده است. پیشتر افشا شد که
ایران در حال آماده‌سازی یک حمله هماهنگ و چندجبهه‌ای علیه اسرائیل
است که از نظر ابعاد و هماهنگی، با حمله ۷ اکتبر مقایسه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22423" target="_blank">📅 14:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=G4CBmstX1S3PJL0hEqGvDP7KdLrLp0ebaDmriea78idNYz8DgXHRhBzWvAOFQCLTVvbIPfvz99ZkTTthdcpdownZR4N4TZbAc_MiEYTDoFMmEMm9M3BkcxjVooQKeYtZbpD_1OtMDDTr6kS56haex8I-iziXeLm_hgmkYzRejnLuizPQz2iTYwIy1hK6Fet-07OC3z7h_7v6sOt376M-aeXGs0cNvdTpAr2wt9z_3WQh5yEb_2XgyIkcPasyXAoG9X2Q5wlzn5sLz0RsYysyRMyAvTfkhMGHs3ke9hXThiwu8oi21hD6-5bH1BfYQ6ziE7IC63snq-9VppJcCz0veX6XxV7qI_-f8gtcf7YFhfsNMeu3yKRAAmwjD7UjmFRG17FQVr_ZaQf8gIRHwCv_EyPyWyVktq4bLjU7KdFlC71Zcm4YsRnJfhgtXsrVvyNa7XsyHWgYK2rkoFGI9sy-mbAv07im8aR6Ffb-KqL7J0OMtLFmgxfjAcORduST0bWfOAgQaKmaDPw_k4trSoHArF1toIkrOBDWgz1dq7SeMQpjEtt9Khc8FmdWsAl4lrANtZ2VOUkf24HwFjF_yu_VxKiKxa8qt_7e6VNDx3ZlcIQVonC5hd2BQbOXx97TmEHcT9qIpaxw_kjCX4euVSBvUtjdpicstGVQ80A0QWKBr1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2c28d2cd.mp4?token=G4CBmstX1S3PJL0hEqGvDP7KdLrLp0ebaDmriea78idNYz8DgXHRhBzWvAOFQCLTVvbIPfvz99ZkTTthdcpdownZR4N4TZbAc_MiEYTDoFMmEMm9M3BkcxjVooQKeYtZbpD_1OtMDDTr6kS56haex8I-iziXeLm_hgmkYzRejnLuizPQz2iTYwIy1hK6Fet-07OC3z7h_7v6sOt376M-aeXGs0cNvdTpAr2wt9z_3WQh5yEb_2XgyIkcPasyXAoG9X2Q5wlzn5sLz0RsYysyRMyAvTfkhMGHs3ke9hXThiwu8oi21hD6-5bH1BfYQ6ziE7IC63snq-9VppJcCz0veX6XxV7qI_-f8gtcf7YFhfsNMeu3yKRAAmwjD7UjmFRG17FQVr_ZaQf8gIRHwCv_EyPyWyVktq4bLjU7KdFlC71Zcm4YsRnJfhgtXsrVvyNa7XsyHWgYK2rkoFGI9sy-mbAv07im8aR6Ffb-KqL7J0OMtLFmgxfjAcORduST0bWfOAgQaKmaDPw_k4trSoHArF1toIkrOBDWgz1dq7SeMQpjEtt9Khc8FmdWsAl4lrANtZ2VOUkf24HwFjF_yu_VxKiKxa8qt_7e6VNDx3ZlcIQVonC5hd2BQbOXx97TmEHcT9qIpaxw_kjCX4euVSBvUtjdpicstGVQ80A0QWKBr1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولودیمیر زلنسکی : «روسیه اجازه نداد هیئت آمریکایی با هواپیما وارد اوکراین شود، با وجود اینکه فرودگاه‌های ما برای ورود آن‌ها آماده بودند.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22422" target="_blank">📅 14:43 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
