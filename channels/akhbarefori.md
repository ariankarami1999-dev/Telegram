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
<img src="https://cdn4.telesco.pe/file/AISTfjBj_wPqBOHU0SBZqdOVDami_CwZ3xI_njsOFyyzxr_Y1SmbENZ8jRcnadOBhR_PN4SHZLb2oVdOlEAs1oqlos-FkDk94Ilx1oOG2g7HnhpbRIfyuhSDUVWTkxm-p8Oz9BwP5oSG14NlDWRiEwMwCWAoBFfiwJJ4ByNHhmRJDZWRMNgDsDKpiw7jV0TigOVapRJYPAXds6nUQ_5iEiLyUDnetGQRT3ZnkxmmenOe0whvL37POgd2QiWJYBmezwoaqLanmG1SoG4LeWlfhnoBxMYPsrA4_0NMXW1jHD4DnOk2PS4Xe8yN8V3pjBZOrSctAl3Os2-x2KWKCq_0eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 15:17:58</div>
<hr>

<div class="tg-post" id="msg-679987">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c92dd8ed3.mp4?token=Trr084xFkgaLrtwmSH7Ki-52Hn6VDfpMWOJSX3hsFOrGDwxW1iBu93-6REIwg5ewerEL7i1sGoXnxM_yE98ohbwtcA557K3fJe5sM6t0FmL-SDcbZHioC2Z7fY_FoFUGKlZ8gdPziMKXGNVR_NfuIkgq6PvpwZQeRfI1nTYteJEbx5iPFghXB4KmGHQhebIQJrqCER-S216WfSZCixVDhODi5LgNyV015E0dqLfomyl4s1Ls8mUTCqkNxPf74gVQMaF9W6CL6YM81GaJPIX6U8PS5-VkMnYu_XmjxRSSP2vsf0UCAOiK87_Oq-GBI1CpzSoHzaNK2Nvo898fVAb7_VwZnBGG2I7HWasCcgUcV6ybqis0ZEnmhOHXz9QLvJZ5_00Bn2bQjsaxxX0ze_TOREo5ANadhNKrh0e5dYlGsF8GcgvfGqgRl0GjHyjNQr145P4P1Q8ljprhZjTOMk2VkGZYNPWq4Hob5DmOm262dJ9XadR1lvc7Vxa18yxaXX_zxl6Qzjn1CsXe1C9_qF2LJlFE3OSJqjrEDnfb4KsIpPzJ9atBqDu9MsaWJ8LqGF3ohw_iK1ZHjWhoexItoQnmvek37Brpbmg8IlDZCyuDPUzIiuWxNiESh8haqjjGSPwTupOSoPf_T6WvbV1NwrQi-di5xQrwlJsc-whr8t0q7CI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c92dd8ed3.mp4?token=Trr084xFkgaLrtwmSH7Ki-52Hn6VDfpMWOJSX3hsFOrGDwxW1iBu93-6REIwg5ewerEL7i1sGoXnxM_yE98ohbwtcA557K3fJe5sM6t0FmL-SDcbZHioC2Z7fY_FoFUGKlZ8gdPziMKXGNVR_NfuIkgq6PvpwZQeRfI1nTYteJEbx5iPFghXB4KmGHQhebIQJrqCER-S216WfSZCixVDhODi5LgNyV015E0dqLfomyl4s1Ls8mUTCqkNxPf74gVQMaF9W6CL6YM81GaJPIX6U8PS5-VkMnYu_XmjxRSSP2vsf0UCAOiK87_Oq-GBI1CpzSoHzaNK2Nvo898fVAb7_VwZnBGG2I7HWasCcgUcV6ybqis0ZEnmhOHXz9QLvJZ5_00Bn2bQjsaxxX0ze_TOREo5ANadhNKrh0e5dYlGsF8GcgvfGqgRl0GjHyjNQr145P4P1Q8ljprhZjTOMk2VkGZYNPWq4Hob5DmOm262dJ9XadR1lvc7Vxa18yxaXX_zxl6Qzjn1CsXe1C9_qF2LJlFE3OSJqjrEDnfb4KsIpPzJ9atBqDu9MsaWJ8LqGF3ohw_iK1ZHjWhoexItoQnmvek37Brpbmg8IlDZCyuDPUzIiuWxNiESh8haqjjGSPwTupOSoPf_T6WvbV1NwrQi-di5xQrwlJsc-whr8t0q7CI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری رییس کمیسیون عمران مجلس
:
خیلی از پروژه‌ها را در کشور که اولویت نداشتند، به دلیل فشار و لابی شروع شده است
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی از پروژه ها در کشور در اولویت نبودند یا نیاز کشور نبودند، اما با فشار افراد مختلف این پروژه ها را در کشور داریم؛ از جمله فرودگاه‌ها ، سدها و غیره.
🔹
از سال گذشته دولت سختگیری می‌کند که پروژه جدیدی شروع نشود مگر اینکه پروژه قبل تمام شود‌.
🔹
دولت هم نباید از زیر بار نیاز یک منطقه به یک پروژه عمرانی به این بهانه فرار کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 309 · <a href="https://t.me/akhbarefori/679987" target="_blank">📅 15:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679985">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان کل کشور: قرار نهایی پرونده مدرسه شجره طیبه میناب به زودی صادر می‌شود
🔹
انفجار کنترل‌شده مهمات عمل‌نکرده در بندرکوهستک سیریک امروز انجام می‌شود.
🔹
خودکشی نظامی صهیونیست؛ هاآرتص: آمار در ارتش اسرائیل نگران‌کننده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/679985" target="_blank">📅 15:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679984">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
وال استریت ژورنال فاش کرد: ۴۲ هواپیمای آمریکایی در حملات ایران منهدم شدند یا آسیب دیدند
وال‌استریت ژورنال:
🔹
حملات ایران (بیش از ۲۰۰۰ حمله در منطقه) به ۲۰ سایت آمریکایی در ۸ کشور آسیب زده، ۴۲ هواپیمای نظامی آمریکا را منهدم یا آسیب‌رسانده و ۱۳ میلیارد دلار خسارت تجهیزاتی و تأسیساتی به آمریکا تحمیل کرده؛ درحالی‌که پنتاگون برای دفاع از پایگاه‌هایش آمادگی کافی ندارد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/679984" target="_blank">📅 15:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679983">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c9a00d27b.mp4?token=nRoX3rDaTJHtUTEBNwwxwG_QyoxLO1okg5jTbr_xGEBo7NumpwhMA3Ayw8_Oy-kGRgFxCO_4eLphobU2k12SQRoah-RNKQQ8Xkwlw99qMe5P-x29r0RFn3pNlLs29cY1x0uPbKsE_pl6kEfbDw788fyM0blw6ZGKnngTFIKsyRoJ3-n01Rxk80iN4z8ra5rNNO4-M3gPQR7Ur-MiUWdD7CTTVHsclPQcJxQfeUrHdJ0zozMJpCTNOjPFmT_tHYvOzycKFf7f9tbZZ4bT91gTxBRNbjwOuJHDCP9e6ricEuuKQ33SZLtGBxe_h0QGdAYM_s16N-GfiM_xNa3dEKK-yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c9a00d27b.mp4?token=nRoX3rDaTJHtUTEBNwwxwG_QyoxLO1okg5jTbr_xGEBo7NumpwhMA3Ayw8_Oy-kGRgFxCO_4eLphobU2k12SQRoah-RNKQQ8Xkwlw99qMe5P-x29r0RFn3pNlLs29cY1x0uPbKsE_pl6kEfbDw788fyM0blw6ZGKnngTFIKsyRoJ3-n01Rxk80iN4z8ra5rNNO4-M3gPQR7Ur-MiUWdD7CTTVHsclPQcJxQfeUrHdJ0zozMJpCTNOjPFmT_tHYvOzycKFf7f9tbZZ4bT91gTxBRNbjwOuJHDCP9e6ricEuuKQ33SZLtGBxe_h0QGdAYM_s16N-GfiM_xNa3dEKK-yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی هیئت رئیسه مجلس شورای اسلامی: معاهده کنوانسیون خزر یک معاهده پرچالش است که باید در مجلس تصمیم‌گیری شود/ فعلا لایحه‌ای رسما ارسال نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/akhbarefori/679983" target="_blank">📅 15:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679982">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_9VXOTJSbpQpE_G8n5hWWdd2nAwsozJOC7TM1QQ-6R12rafDzTAOtqRp_34qYAs2RnYnivjriNpuXNlviPZboIMTFfcYchgAwtfUgJmlZVbjmb-vYz9DqBG-cQ9c2FxeaW04nMDwL9hVMeQMNlIK0PjNzlbX_EEplMXeMxhPrabvpwTuEYYqQ8UcNj9DPj_ARx35CMkoezSkn44ToRoGDXtNspEH7Jcy_lo6k5cmL8M6Ex-ZcYzdqaS-2In315Km5rEmx8OHjwe7pMxAZXycnrat5i09-onwxSu5tH-FBRfkCeILbQCjnIEDR2fAOWQApY0_9_3W_zJszRUOSr7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ۱،۰۰۰،۰۰۰ تومان تخفیف، خودروتان را برای سفر آماده کنید
💯
🔸
تعویض انواع لاستیک دولتی
🔸
تعویض روغن موتور با قیمت مصوب
🔸
خرید و تعویض لنت و سایر لوازم خودرو
تمام این خدمات با تضمین کمترین قیمت و یک تومان تخفیف در اختیار شما قرار دارد.
کد تخفیف: RWELXT
مهلت استفاده: ۲۳ مرداد
حداقل خرید: ۳ میلیون تومان
همین حالا وارد سایت تپسی‌گاراژ شوید، نزدیک‌ترین مرکز خدماتی را انتخاب کنید و سفارش خود را نهایی کنید.
👇
https://tapsi.link/mrip0</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/akhbarefori/679982" target="_blank">📅 15:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679981">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
چرا نباید ایران از تنگه دست بردارد؟
🔹
دست‌کشیدن از تنگه هرمز یعنی ازدست‌رفتن اهرم بازدارندگی ایران؛ چون قطر، عراق، کویت، امارات و عربستان ۷۸ تا ۱۰۰٪ صادرات نفتشان را از این مسیر انجام می‌دهند و مدیریت تنگه، کنترل اقتصاد و تورم کشورهای نفتی منطقه را در اختیار ایران می‌گذارد./ فرهیختگان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/679981" target="_blank">📅 15:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679980">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=qzV-7a6_d8LgCnWfsU8nTFw7uqgP5ICjPQT5gzp5zDtfmM1QRjgEb54AeTD2NPYUJV06wjtuTVyKvABjgpOgZou8TTp1eLQboea8_rfgu5hCAQ-2Dp8zFJFfuYdaWOWQ67kg7N1UQFaJr2TCgXlox4ZsYePam9jy7CRQ28U_MWPFwyshwOTuOaPFs56uLbRXH79OY592P7Jqroqjqj8ZxQ55VMkJo4BYNtEKWnVJ9hL8V1u3rRhM9qE9dRRyLCpIXxxtuUczHX1bgu_jwkss43bYfYMe7Vi_gTOUP5cWieMLz0wrmrzTVGy_WqLDRWkvL6yKI9OyIFHeSbrzVvZZ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec49f80d3b.mp4?token=qzV-7a6_d8LgCnWfsU8nTFw7uqgP5ICjPQT5gzp5zDtfmM1QRjgEb54AeTD2NPYUJV06wjtuTVyKvABjgpOgZou8TTp1eLQboea8_rfgu5hCAQ-2Dp8zFJFfuYdaWOWQ67kg7N1UQFaJr2TCgXlox4ZsYePam9jy7CRQ28U_MWPFwyshwOTuOaPFs56uLbRXH79OY592P7Jqroqjqj8ZxQ55VMkJo4BYNtEKWnVJ9hL8V1u3rRhM9qE9dRRyLCpIXxxtuUczHX1bgu_jwkss43bYfYMe7Vi_gTOUP5cWieMLz0wrmrzTVGy_WqLDRWkvL6yKI9OyIFHeSbrzVvZZ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری پزشک قلابی عمل‌های زیبایی در شهریار تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/679980" target="_blank">📅 14:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679979">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688432cc6d.mp4?token=J0-jVCoYPPhpAOPg2Njpe3nnaMlj3n2FvSt9qdUB-PlbNsBK2sJzS8jaV028P_-Slp5XIQm6fw2CdPP1zafrqARUqrvwWWoYqyEKTfil1639pw_3WLS1hdAbHBrTUrzsi2h3PiKgFw6G3nGKEzPyxVSmslpWjkuGLK-6fdvxRePy-uUWmmDJQeyDUhlf-8UqsJuGivFNjQin8KPQQ4OAdCrEbIW6u5swmZK3Idc9WqQhmCHX0GFNwzS1PQGaJ3JpdU3RkBYuH1gcZTPAX14O2BwvHSBTirE4L-2ORHeOfEP6YuA84BdF8YmXiwq_Dm14DM09QTII2QxqSFuW3LagCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688432cc6d.mp4?token=J0-jVCoYPPhpAOPg2Njpe3nnaMlj3n2FvSt9qdUB-PlbNsBK2sJzS8jaV028P_-Slp5XIQm6fw2CdPP1zafrqARUqrvwWWoYqyEKTfil1639pw_3WLS1hdAbHBrTUrzsi2h3PiKgFw6G3nGKEzPyxVSmslpWjkuGLK-6fdvxRePy-uUWmmDJQeyDUhlf-8UqsJuGivFNjQin8KPQQ4OAdCrEbIW6u5swmZK3Idc9WqQhmCHX0GFNwzS1PQGaJ3JpdU3RkBYuH1gcZTPAX14O2BwvHSBTirE4L-2ORHeOfEP6YuA84BdF8YmXiwq_Dm14DM09QTII2QxqSFuW3LagCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید سپهبد موسوی: هرچی تنبیهی من خوردم، بخاطر خنده‌هام بود
🔹
۱۹ مرداد ماه، سالروز ولادت فرمانده شهید نیروهای مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/679979" target="_blank">📅 14:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679978">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrJz9kaDJZ7on2Dle_OGbwV6HufVwVnExr-0j5kneIHxaNvNByQVYqb3G9nBtzw5N-dpIA7BLlpraxJyiefHokHRHbJdHQr5tZx6d3siBbYDaicA6tFhMk6G5uaotkKpno2HbGFBkUks3cldkBacVz5JU19h6ABP-o2md7RVptD8J6HLbps_R6tjgzCiAb6EygOWgpgfFJIwHd9QPNKQXvt6F4NjAuOs7oBuP1iY__HCjDbwMUiGAE6MmAZ9aaBmRGZY1vuNv5jIxjvHwXruwxl7WRH-feOqmOGiIwMofqLtpNSogoYNNKzmZ0NEqpITok6WSi2lfyehHXw4s8dOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات سایبری؛ عامل بیش از ۶ درصد ترافیک اینترنت کشور
🔹️
بیش از ۶ درصد ترافیک در سطح کشور بدلیل "دیداس" و حملات سایبری است که عدد بسیار بزرگی است.
🔹
حملهٔ دیداس نوعی حملهٔ سایبری است که در آن، مهاجم با ارسال حجم زیادی از درخواست‌ها به یک وب‌سایت یا سرور، باعث ازدسترس خارج شدن آن سرویس می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/679978" target="_blank">📅 14:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679975">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f40a99260e.mp4?token=PSJ4EAvCGHin37RyIp2o9en1CllFQAe3WJatwumh7C43aXEkt0G5Ty-D54NYxZ9NYV_zsm-QFIu53BHGKNtarM2GYKIEywTR91Ye4jqPPinn7Oseo50JbAgSltCWAvMEW72VyFRIpQLoFAS5py20yIc2DG_5Cbr9m7tVfg6YfYDFrasbG6IQdqXnzcrKxHCnhv1AhFKNWuTAGhtz8_x6dzy-puDI1sPn4tW5Zk9hLGMXXMPAFxnKYx0WKbDr5akIoqdU-DCATSdNiIlwsuT6cbybNPGw90FZhyVLe8I4ggomePgN7cXjw4CG2kNLEZoHvZSjvSAh789ca4NlwfjPR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f40a99260e.mp4?token=PSJ4EAvCGHin37RyIp2o9en1CllFQAe3WJatwumh7C43aXEkt0G5Ty-D54NYxZ9NYV_zsm-QFIu53BHGKNtarM2GYKIEywTR91Ye4jqPPinn7Oseo50JbAgSltCWAvMEW72VyFRIpQLoFAS5py20yIc2DG_5Cbr9m7tVfg6YfYDFrasbG6IQdqXnzcrKxHCnhv1AhFKNWuTAGhtz8_x6dzy-puDI1sPn4tW5Zk9hLGMXXMPAFxnKYx0WKbDr5akIoqdU-DCATSdNiIlwsuT6cbybNPGw90FZhyVLe8I4ggomePgN7cXjw4CG2kNLEZoHvZSjvSAh789ca4NlwfjPR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی کمتر دیده شده از سینه زنی رهبر انقلاب در مراسم تشییع فرزند مرحوم آیت‌الله استادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/679975" target="_blank">📅 14:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679974">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45066d47b4.mp4?token=HGF-NR9UCAu2fVnSWKEHvEr2ndmArRO3CoP7mZTG7hdky6dNFX4Vt1vi_9_jiAW1jyoFBwr2uz_GUn3GUz3uraGrSzNQ02k5xoRMB4CtY6C7OHlNz-C7bh8zD5ZQjLcT57Cxi-tJP86MwNMIP4YiCweVPZKv34LwwGmch9GkV0ZE80zd6WYWKpWMiSFqs1qKHkCCMX3zWMoAzkYPWyom4x8AvNmPfC9pFsfAhtii4uDRuyJ3GmSKw1VRI9SH2iZa5Pd8uJ-iIKJ8Y9VMzwa0O4A56qibi05es7NXlUmReMuIqCC5wDwmK_7hN3TcdYabnJIn5coBtEMIve9nVigifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45066d47b4.mp4?token=HGF-NR9UCAu2fVnSWKEHvEr2ndmArRO3CoP7mZTG7hdky6dNFX4Vt1vi_9_jiAW1jyoFBwr2uz_GUn3GUz3uraGrSzNQ02k5xoRMB4CtY6C7OHlNz-C7bh8zD5ZQjLcT57Cxi-tJP86MwNMIP4YiCweVPZKv34LwwGmch9GkV0ZE80zd6WYWKpWMiSFqs1qKHkCCMX3zWMoAzkYPWyom4x8AvNmPfC9pFsfAhtii4uDRuyJ3GmSKw1VRI9SH2iZa5Pd8uJ-iIKJ8Y9VMzwa0O4A56qibi05es7NXlUmReMuIqCC5wDwmK_7hN3TcdYabnJIn5coBtEMIve9nVigifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه رشد لاله مردابی
🔹
یکی از اشتباهات رایج، یکی دانستن لاله مردابی با نیلوفر آبی مصری است؛ با توجه به مرکز گل می‌توان تفاوت این دو گیاه را تشخیص داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679974" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679973">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa2d0a474.mp4?token=PnNWIRituQlHOGWforseksjVOCgOmrcFhXrc-zi1R1xkt-VGh9CJJBBGIb3BwTFRUJE1cCFGQ_za5lZprdBpM7hILIwuypXg4NjhNQgmqoMt0NYGJP3DX7gXGETGVt5Jfb6uJ_A0zkwhEyLWwViC8tPyc1vjMRp2p68ryPthnXvEbTiLowIpV1tB1_mrPlviswPLzL8fGKtVtzrPOhEX3fbcgsyQDXsUXRrDMoc-jsExbaH_JmWrW6UI0CC08WBF9A9GWZPRQGXVJZ1O8nwHmMoBAE7rAvJzDQH9C5wEKkdEAflTYS3w4DFhq4C9RxG3V5PBA7gxrGEfdvR_acuPCJxk2zh8ypU0EJ7O9Q7IKuCx6nU3GJ63X2Ihn_t_lRQk8FJOYJ3tYVGMpqUs1WvO6uTUF4HEetd8OkU6RY3GM5N54ZGhKI756fPa2N_E8UAAkA9lc3PWzZ94fv3Niuqki7SXHGm1cTIiGTzlQx_XNFfN92ZesrM_q1bqLQncqqaOAS_eNubF2B4nxlR8XhTBV0dI-rP6sPoEefHpUTZkdcYRLPaOT777NcAfKREbHH2qASGoKvjXs1pw_4DWUbwZM0mEKS6sjRLrVtvZdUKRoLnuUKEFL5rhjmexU1_cjyuoOpUb74apEAAfeNkKb87aLBj2DSefPMWdtew7ItuGnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa2d0a474.mp4?token=PnNWIRituQlHOGWforseksjVOCgOmrcFhXrc-zi1R1xkt-VGh9CJJBBGIb3BwTFRUJE1cCFGQ_za5lZprdBpM7hILIwuypXg4NjhNQgmqoMt0NYGJP3DX7gXGETGVt5Jfb6uJ_A0zkwhEyLWwViC8tPyc1vjMRp2p68ryPthnXvEbTiLowIpV1tB1_mrPlviswPLzL8fGKtVtzrPOhEX3fbcgsyQDXsUXRrDMoc-jsExbaH_JmWrW6UI0CC08WBF9A9GWZPRQGXVJZ1O8nwHmMoBAE7rAvJzDQH9C5wEKkdEAflTYS3w4DFhq4C9RxG3V5PBA7gxrGEfdvR_acuPCJxk2zh8ypU0EJ7O9Q7IKuCx6nU3GJ63X2Ihn_t_lRQk8FJOYJ3tYVGMpqUs1WvO6uTUF4HEetd8OkU6RY3GM5N54ZGhKI756fPa2N_E8UAAkA9lc3PWzZ94fv3Niuqki7SXHGm1cTIiGTzlQx_XNFfN92ZesrM_q1bqLQncqqaOAS_eNubF2B4nxlR8XhTBV0dI-rP6sPoEefHpUTZkdcYRLPaOT777NcAfKREbHH2qASGoKvjXs1pw_4DWUbwZM0mEKS6sjRLrVtvZdUKRoLnuUKEFL5rhjmexU1_cjyuoOpUb74apEAAfeNkKb87aLBj2DSefPMWdtew7ItuGnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین‌پاک، کارشناس جبهه مقاومت: رژیم صهیونیستی ۷۰ درصد غزه را اشغال کرده است/ اگر دوباره خطای حمله به ایران را تکرار کند، با ضربات متفاوت و تسلیحات پیشرفته‌تر ایران روبه‌رو خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679973" target="_blank">📅 14:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679972">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
فیلتر پلتفرم‌ها بدون تایید رییس جمهور ممنوع شد
؛
دولت اختیار محدودسازی کسب‌وکارهای دیجیتال را مشروط به تأیید رئیس‌جمهور کرد
🔹
بر اساس این مصوبه، دستگاه‌های اجرایی دیگر نمی‌توانند به‌صورت مستقل درباره محدودکردن فعالیت پلتفرم‌ها تصمیم بگیرند و هرگونه اقدام در این زمینه باید ابتدا در «ستاد راهبری و ساماندهی فضای مجازی» بررسی و در نهایت به تأیید رئیس‌جمهور برسد.
🔹
اهمیت این مصوبه فقط به تعیین یک مسیر اداری جدید محدود نمی‌شود؛ دولت برای تصمیم‌هایی که خارج از این چارچوب اتخاذ شوند نیز اعتبار قانونی قائل نشده است. بر اساس ابلاغیه هیئت دولت، هر تصمیم یا اقدامی که بدون طی این فرایند برای انسداد، تعلیق، تحدید یا ممنوعیت فعالیت سکوها و کسب‌وکارهای فضای مجازی انجام شود، «فاقد اعتبار» خواهد بود.
🔹
فرد ذی‌ربط در صورت واردشدن خسارت، مطابق قوانین و مقررات مسئول جبران آن خواهد بود./ شرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/679972" target="_blank">📅 14:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679971">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=qFFGxLOl4ctt-HNgVLJv_FgB4tw8Ph4a1i_JMeYWhtwoEOuVcmcGzqDv86fOvE5V4JdeEcSSLz8mDmiou4_dB0Nk38cldwhtTmAP5QGADW8TBeDH4mjtkNuRhtk4XjDZPf84h2V0O5crYk214NVDW-G66I6zfef71SqMoZfD2M7PaQaL6srTwklReWnbfnseQ1tpN98MYR7tGUYKfd6fXXVdVFQ2YP0xKRvqh1FaG9cXFdtx4KhAXdE8NMgJhxfdwtB8b0-RjIaJz6gPrk1-ocadHBPh2ngNi-PRqhw2YpaedmDEVArdmY6x0Ccmp55qfUo8T_n_B0s3uOR1wgE5HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f43b18398.mp4?token=qFFGxLOl4ctt-HNgVLJv_FgB4tw8Ph4a1i_JMeYWhtwoEOuVcmcGzqDv86fOvE5V4JdeEcSSLz8mDmiou4_dB0Nk38cldwhtTmAP5QGADW8TBeDH4mjtkNuRhtk4XjDZPf84h2V0O5crYk214NVDW-G66I6zfef71SqMoZfD2M7PaQaL6srTwklReWnbfnseQ1tpN98MYR7tGUYKfd6fXXVdVFQ2YP0xKRvqh1FaG9cXFdtx4KhAXdE8NMgJhxfdwtB8b0-RjIaJz6gPrk1-ocadHBPh2ngNi-PRqhw2YpaedmDEVArdmY6x0Ccmp55qfUo8T_n_B0s3uOR1wgE5HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هیچ قدرتی نمی‌تواند مردم ما را وادار به تسلیم کند
🔹
مردم با حضور در میدان، تهدیدها را به فرصت تبدیل کردند و همۀ معادلات دشمن را با وحدت و همدلی شکست دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/679971" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679970">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهفتم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای سید امید متقی که بخاطر خواب آلودگی در حین رانندگی دچار سانحه تصادف و ضربه مغزی شده و یک‌ ماه در کما به سر می‌برد و با رؤیت جد بزرگوارشان امام موسی‌بن‌جعفر، شکستگی‌های داخلی در بدن که بیمارستان متوجه آن نشده بود، شفا می‌یابد و به او سفارش رعایت حق‌الناس و طلب حلالیت از انسان.ها در دنیا می‌شود، را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سید امید متقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/679970" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679969">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3Vy33Wz8HUQLG08nKaGUQ9O960dqmxQNyAifja3yMQrnOiu0EHFTc_2Djs5Dw2-FdcsJXPvtuIPZg06MYzyk7ZcoS-TnHNVcMVzuA0FsNlxL05tV6VjfAJxS95ata-cI5nechwxzhwU2fD5Ipa5DtMhxzyytquSSqdzTCfNRNTVx1dkQhKSB77rrgPUcjEMFZv1wBqCud0WKMSFdJf40FyoTmkJuX7-ZHD4yrwdacG_zrUF5eMVKbmaeOu3KfmdeX2B_WzeiuNZTONA6cdqXTNkQMc_g9-l7d0aJg9yYiFdXFZtJB6XDT0Uq6iVaYa6GEQUPYDkrBQHLdGX5HnMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر کتونی مناسب چه مدل شلواریه؟
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/679969" target="_blank">📅 14:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679968">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
افزایش شهدای حشدالشعبی به ۲۰ نفر
🔹
حشد الشعبی در بیانیه‌ای اعلام کرد که در پی حملات آمریکا و عربستان تاکنون ۲۰ نفر شهید و ۳۲ نفر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/679968" target="_blank">📅 14:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679967">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e7d6feab.mp4?token=ko4kCBwsVYLiNSS6HL4EiGJi10ZArdaLAagwz0sNvqb5kDy3_A07DvKbRa5kv8evwOpc-osBOGSJx0FWWu332XjaO0U4AgqIEX1XBdIcprJ_BYOGn5q0U9x9wN26_UDdQPWZ2i_vm7w2Q8f-bv0UoYwFAg4B1HswVV6cJu09xBEt2ZRQMKlyw5-S3-WkaaMkg6egjh_WTfQMYNVDOj2UEiLDfaHrrKScvIo-p1gf_yyCfRH0kWtYdACC0v77CEDSWWcGTVn8Wel6hiX-ZKxVn2c3AJkq4By4sDMDig9YmCxEc0zgNajmMMSMslZwiIiQwxXXk4WOuJ9WNqGQrDsc6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e7d6feab.mp4?token=ko4kCBwsVYLiNSS6HL4EiGJi10ZArdaLAagwz0sNvqb5kDy3_A07DvKbRa5kv8evwOpc-osBOGSJx0FWWu332XjaO0U4AgqIEX1XBdIcprJ_BYOGn5q0U9x9wN26_UDdQPWZ2i_vm7w2Q8f-bv0UoYwFAg4B1HswVV6cJu09xBEt2ZRQMKlyw5-S3-WkaaMkg6egjh_WTfQMYNVDOj2UEiLDfaHrrKScvIo-p1gf_yyCfRH0kWtYdACC0v77CEDSWWcGTVn8Wel6hiX-ZKxVn2c3AJkq4By4sDMDig9YmCxEc0zgNajmMMSMslZwiIiQwxXXk4WOuJ9WNqGQrDsc6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باید برخاست؛ برای ایران، با هم و کنار هم
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/679967" target="_blank">📅 14:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679966">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4c320e7.mp4?token=mCOY_lMdF9HfBE58zscZGtXDQ4hoZ7u-UMsDgJkSC7jibZAk7u7dsXJtQAv-JVWdPn9QpsIOcIGL0lkRHbwM4lUbo_xw8YmNfdE75fEyl03VH_2IVLgBXkkKUtCHvyVo1DbtZ3aFDFBBqouwp3S_AV0vsmRBGRhkD1qqXJxk7oMJ496omNP0GHEOR9zptaF-SBcme2K4ZE8sBodFdA7XIqsr5KSNv2PYTHlXuRx7kALj91PL--krXjSxrYxR5amsxi3ir0rHik7cd9cQQiSDmGwqUhjDSse0aJ1OHPwrLr3XkMhlKMFgPZ7eTMotozwKpY7CSZqf0ea6LrqVI2yjf10YB9hCYGIbxuSH7O-vVMOdt370Y00f_1dA-FL_9DAZ9Kk0v6z1rzY0cbSx842fp1JPGdCO1QOOVp1lpyfwhsBK59hWMRGpQnNC62DJaajUHhmdyH3-EFS7c_Q5cKqqyyJRFfj6nB5-tQJB90hVZHGGAHUiQHtEvDgg6fqgypztdNXFoXFMtVbLCBVwiPzmNHC4JtUGiSQI9fuQy-1xweTC6vOxvRhEJwY3AS_CxUE2TZ-0MlpG8mYbU-pchzjMmDXiD2F052RIHbU0lB0qe_4zoalJCzoKlkunoR_7c9pHFdNvf6gFW5d-PlRwciogWWzIexr1xHsAG-q8SQ0ie5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4c320e7.mp4?token=mCOY_lMdF9HfBE58zscZGtXDQ4hoZ7u-UMsDgJkSC7jibZAk7u7dsXJtQAv-JVWdPn9QpsIOcIGL0lkRHbwM4lUbo_xw8YmNfdE75fEyl03VH_2IVLgBXkkKUtCHvyVo1DbtZ3aFDFBBqouwp3S_AV0vsmRBGRhkD1qqXJxk7oMJ496omNP0GHEOR9zptaF-SBcme2K4ZE8sBodFdA7XIqsr5KSNv2PYTHlXuRx7kALj91PL--krXjSxrYxR5amsxi3ir0rHik7cd9cQQiSDmGwqUhjDSse0aJ1OHPwrLr3XkMhlKMFgPZ7eTMotozwKpY7CSZqf0ea6LrqVI2yjf10YB9hCYGIbxuSH7O-vVMOdt370Y00f_1dA-FL_9DAZ9Kk0v6z1rzY0cbSx842fp1JPGdCO1QOOVp1lpyfwhsBK59hWMRGpQnNC62DJaajUHhmdyH3-EFS7c_Q5cKqqyyJRFfj6nB5-tQJB90hVZHGGAHUiQHtEvDgg6fqgypztdNXFoXFMtVbLCBVwiPzmNHC4JtUGiSQI9fuQy-1xweTC6vOxvRhEJwY3AS_CxUE2TZ-0MlpG8mYbU-pchzjMmDXiD2F052RIHbU0lB0qe_4zoalJCzoKlkunoR_7c9pHFdNvf6gFW5d-PlRwciogWWzIexr1xHsAG-q8SQ0ie5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: هیچ دولتی در حوزه مسکن خوب عمل نکرده است
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه در کشور برای حوزه عمرانی جایی برای بخش خصوصی پیش بینی نکردیم.
منابعی که در بودجه سالانه برای حوزه عمرانی پیش بینی می کنیم یک پنجاهم چیزی است که نیاز داریم.
🔹
باید قبول کنیم خیلی از پروژه های عمرانی را در کشور کلنگ زدیم؛ حتی درصدی پیشرفت فیزیکی دارد، اما نیاز کشور نیست.
🔹
در حوزه عمرانی کشور را گران اداره می کنیم.
#فوکوس
@TV_Fori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/679966" target="_blank">📅 13:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سلیمی
عضو هیئت رئیسه مجلس در اخطار قانون اساسی: تفاهم‌نامه احتمالی ایران و عمان، باید در مجلس تصویب شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/679964" target="_blank">📅 13:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
کشف جسد «دنیل سیاد» از مرتبطان پرونده اپستین در پاریس
🔹
جسد دنیل سیاد، از چهره‌های کلیدی در پرونده جفری اپستین که متهم به تأمین دختران جوان برای او بود و قرار بود بازجویی شود، در پاریس پیدا شد.
🔹
وی دومین فرد مرتبط با این پرونده است که در فرانسه جان باخته…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/679963" target="_blank">📅 13:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: تنگهٔ هرمز از زمان خلقت حضرت آدم تا ۹ اسفند پارسال باز بود!
🔹
اتفاقات اخیر ناشی از تجاوز آمریکایی-صهیونیستی است؛ آمریکا که همچنان از محاصره بنادر ایران می‌گوید، جایگاه اخلاقی و حقوقی برای شکایت از بسته‌بودن تنگه ندارد و این مشکلی است…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/679961" target="_blank">📅 13:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679958">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdXl3g_1M0wd-2ImhkTUk14b3sf-ZkeyEODaoJELJkEP7RWpFeQY5A9_nWCGxTlAaH_0nYODDLaUTepx46DPbBuqDicwxOTAb9AJjL4n6qw7w5Nttoih9WBL_ahtuH9tDwaDwU2WaVGs5nD5YS54wRHk3j-gbJ9bpW5T3yM-3MeNCyRE8G8onqWmTPgxcTzvEiIc5f3NX-zvLNHb54K7ZC1Xiru2XcLbUztdDg_mKRIFdrsG3J_McyVlXLJEwxKUbWZFiBEDWyvTCs3q5hFA-U3tyHzqcEO4tmnUtXEeZ4odyZjEsZqLRPXvU3krAegkdAAAmSkVa5banOtlUbkkmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYEaIj56K5X8Axmi7TB5ivsNFzVrLTyu37YwbwK_vX5qEILMoQ2yluxeagizZjqZDpRKA4YEX7ro7VEEzbtQB8YlSHbv63xXg0yuQUgcKGARubKmtjIkso47-A5AiM3DeJm_S0DolIdwrnpWisF_ajCoIE5BmehXUE06pC-bx0STk7jf2QDh1UHdOLMfavSh98hx42khQCSSdSOd-WlFUtNYFPLjjHqx_Gl1oJZtrObnJWN5NCEuGD-ySElJaBfa-Q7ouz8jKob8-Pbe7mjcUr4olVwLCpC_pOB_mki-diWwGxCzbeMZyJxhY-OdzG2vo3c5m2qTD0F75RoKVp0JXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TQGvrwost6tTf2ahK0_xtKD4ik2k71TL3dpmuw5tGCA58NP485tLzMRYwWhpcc1yHN1SCc7CkNNjgRFNXPcVzvXkT_FUYnPea09NH1n5269Bs8NtIEhA63MCXXPZ52_COaE01oTyZhFl6HMNs3r7_unw_34pNPm8Mem6NqTbFb8Ku4EZsSl7492kUVjwWKdS3DgfGmNFM_m6AmqAcpuLkedz5pspghNHY6n2mNIngNtlZ-xEZ652_4uiiyc7KJSfvv2Eg3Jzsc2MAZtBWMU8tQKe4ncudBsyDsYxyK_fB4mT3grc7IYysuYUMFWXAugeQd_-RjUO6E32W23B1e4TIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شمشیر کوتاه هخامنشی
🗡
🔹
اکینکه‌ی زرین یا شمشیر کوتاه هخامنشی، متعلق به سده‌های پنجم تا چهارم پیش از میلاد است که در اکباتان (همدان امروزی) کشف شده و اکنون در موزه ملی ایران نگهداری می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/679958" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679957">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
الجزیره: انصارالله یمن در حملاتی موشکی و پهپادی پایگاه‌های نیروهای هم پیمان عربستان موسوم به شبوه در منطقه بیحان را هدف قرار داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/679957" target="_blank">📅 13:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679956">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdd3a47ed.mp4?token=LirSty3wpxhEcTI8aD5wmn-jqDusLStM_wFxAJJotIfnUMSByQWdttuI3um5yPwbCprcYRNpyGkmFzahTOMqLaLhx5J-CwgwJn1UO2txV6G802f2fQRQTBpd_frw2C0f8Z11aGSsAo-KJJnZrqeIBeaYOQdzPxhbeMkMyCEnuNM7RCG_xeLQ5pRiL8fUibpE7CtlpGNXjhLLDHEWWgGaQyvfPl5-ESWapxNn6-4ewi2ldII0kWgdprirW_B0i3zYlCXhchgjSL_ZwhyNMmJDV4EDn48lW_E0EbF-8_BFesshmGkkKZs79v8G0Y7obN_Uk_WlW5Xn3dLbjFKwAv-Q0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdd3a47ed.mp4?token=LirSty3wpxhEcTI8aD5wmn-jqDusLStM_wFxAJJotIfnUMSByQWdttuI3um5yPwbCprcYRNpyGkmFzahTOMqLaLhx5J-CwgwJn1UO2txV6G802f2fQRQTBpd_frw2C0f8Z11aGSsAo-KJJnZrqeIBeaYOQdzPxhbeMkMyCEnuNM7RCG_xeLQ5pRiL8fUibpE7CtlpGNXjhLLDHEWWgGaQyvfPl5-ESWapxNn6-4ewi2ldII0kWgdprirW_B0i3zYlCXhchgjSL_ZwhyNMmJDV4EDn48lW_E0EbF-8_BFesshmGkkKZs79v8G0Y7obN_Uk_WlW5Xn3dLbjFKwAv-Q0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبلیغ متفاوت نتفلیکس برای فیلم «آخرین خانه»
🔹
نتفلیکس برای تبلیغ فیلم «آخرین خانه»، مردی را سه روز داخل اتاقی ساخته‌شده درون یک بیلبورد در لس‌آنجلس مستقر کرده است؛ اتاق به کتابخانه، کارت بازی، دوربین دوچشمی و تخته سفید برای ارتباط با رهگذران مجهز شده و با فضای داستان فیلم هماهنگ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/679956" target="_blank">📅 13:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679955">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWwVh9A33FG-OcqAAdjgXmzNPQRSL2NwhhiY0BW9GIzuCmSLDRQQr9cegwB4RVn7PU8t_jFqz4793Ec0Xt-N9QRtvEqFYy6OZQ7uGQ1fUSBZToqucSpgT0OrkF_7uIXo_UESR_vWeGbTMMaRqTa2TEcuQOlhKfSHM5YDc5D14xVmOYIeMaKY7mduI3VpZ7EeiOPmv6RTusOkTebsRB4xjsmw4ui7iO6-pqzbIvE2u37VJq3zGbWAmRIAEY0v1IA2-_gWXTH7XDuqWBZd4U9NjO4B2AxfsJnjcj1XFE15gj1WYC8dOU6RsSlcrg3xOqQ3UK3UgLZ1yfGikXXR3skaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۹ مرداد ۱۴۰۵؛ ساعت ۱۳:۰۰
🔹
دلار در معاملات امروز با افت هزار تومانی نسبت به نرخ پایانی دیروز، به کانال ۱۸۵ هزار تومان عقب‌نشینی کرد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/679955" target="_blank">📅 13:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679954">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efnoHij_6gXvG4AhievbY0utBDmNqWWchqcIyCuhRdCxjKXs1yaJH-cEqC5JrA5-5pcMC4lzMhwWE8iq09XLnDh1oOywCo7ck8i2iCddc3TfkGHGGHWDQsgJ75_-liN0Hj3MsjvH4-VZFg1MATTQh6MRfHDRq17ZP5A7_V6DW4AaGicxLWFV0UIdE1SBlaHq28eI21zl4E0_uhdMBifqREfBXx9dGEJHq3HnAXtRYQBh8t9IHG5aPhMoIZj0pGei5rtfXGSLXjNB6Z3sRvqL1XkjXZWBcm45TJQ9rSiMB8KZ9lRQNyVdAv5Y3So6AGuUmfIsdJtvkBzTwbsuwsDtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصمیم‌های بزرگ نوری برای آینده سهامداران؛ از افزایش سرمایه و تقسیم سود تا تثبیت سرمایه‌گذاری‌های راهبردی شرکت
🔹
تصویب افزایش سرمایه به ۹۶ هزار میلیارد ریال و تقسیم ۳۸۵۰ ریال سود به ازای هر سهم
🔹
مجامع عمومی فوق‌العاده و مجمع عمومی عادی به‌طور فوق‌العاده شرکت پتروشیمی نوری، امروز یکشنبه ۱۸ مردادماه با حضور سهامداران در سالن همایش ضرغام تهران برگزار شد و تصمیم‌های مهمی درباره آینده مالی، سرمایه‌گذاری و توسعه‌ای شرکت اتخاذ شد.
در این مجامع، افزایش سرمایه پتروشیمی نوری از ۶۰ هزار میلیارد ریال به ۹۶ هزار میلیارد ریال به تصویب رسید و در مجمع عمومی عادی به‌طور فوق‌العاده نیز با تصویب سهامداران، ۳۸۵۰ ریال سود به ازای هر سهم تقسیم شد.
بررسی و تصویب صورت‌های مالی سال ۱۴۰۴، گزارش عملکرد سالانه، اصلاح اساسنامه و انتخاب حسابرسان از دیگر محورهای این مجامع بود.
*سودآوری در کنار سرمایه‌گذاری؛ تصویری از منابع و تعهدات نوری*
در جریان ارائه گزارش عملکرد مجمع، دکتر غلامرضا جمشیدی، مدیرعامل موفق پتروشیمی نوری، با تشریح وضعیت مالی شرکت تأکید کرد: ارزیابی عملکرد نوری تنها با تمرکز بر سودآوری و توجه به جنبه های تک بعدی امکان‌پذیر نیست، بلکه باید همزمان میزان به مقولات متعددی همچون سرمایه‌گذاری‌های کارشناسی شده سودآور ، تعریف پروژه های نوین، مدیریت هدفمند هزینه ها،  تخفیفات خوراک، بدهی‌ها و نیازهای نقدینگی شرکت مورد توجه قرار گیرد.
*«هنگام» از سرمایه‌گذاری تا تولید؛ حفظ دارایی‌های ارزشمند برای سهامداران*
یکی از مهم‌ترین محورهای گزارش مدیرعامل بزرگترین شرکت آروماتیکی ایران، به ثمر رسیدن سرمایه‌گذاری در پتروشیمی هنگام بود؛ پروژه‌ای که در شرایط فشار نقدینگی و وجود بدهی خوراک، با تأمین منابع مورد نیاز به مرحله تولید رسید.
دکتر جمشیدی با اشاره به اهمیت این سرمایه‌گذاری اعلام کرد: آثار سودآوری پتروشیمی هنگام می‌تواند از سال ۱۴۰۵ در پرتفوی نوری نمایان شود و در بودجه سال جاری نیز حدود ۶.۸ همت سود برای این شرکت پیش‌بینی شده است.
مدیرعامل نوری همچنین تأکید کرد مدیریت برای تأمین نقدینگی می‌توانست نسبت به واگذاری بخشی از سهام هنگام یا سایر دارایی‌های شرکت اقدام کند، اما با استفاده از ابزارهای تأمین مالی، اعتبار و ال‌سی، از فروش این دارایی‌ها جلوگیری شد تا سرمایه‌گذاری‌های سودآور و بلندمدت برای سهامداران حفظ شود.
*از یورو ۶ تا عبور از بحران؛ بازگشت مقتدرانه نوری به مدار تولید*
پروژه تولید محصول با استاندارد یورو ۶  به عنوان محصولی ارزشمند و راهبردی نیز از دیگر طرح‌های مهم مورد اشاره مدیرعامل نوری در مجمع بود.
این پروژه مهم که به مراحل پایانی رسیده، اکنون کاتالیست آن بارگذاری شده و آماده افتتاح رسمی است.
دکتر جمشیدی خاطرنشان کرد : این پروژه با ظرفیت فعلی حدود ۱۳۰ هزار تن، از منظر توسعه بازارهای صادراتی و ایجاد فرصت‌های جدید در حوزه بانکرینگ دارای اهمیت ویژه‌ای است که ظرفیت افزایش تولید نیز برای آن وجود دارد.
مدیرعامل نوری در بخش دیگری از گزارش خود به آسیب‌های عملیاتی ناشی از جنگ اشاره کرد و گفت کارکنان پتروشیمی نوری طی ۶۷ روز تلاش شبانه‌روزی، بازسازی ۱۸ خط و حدود ۵ کیلومتر خطوط انتقال را انجام دادند و در مجموع حدود ۹۶ هزار نفرساعت برای بازگرداندن واحدهای آسیب‌دیده به مدار تولید صرف شد؛ تلاشی که در نهایت به بازگشت شرکت به چرخه تولید انجامید.
در کنار این اقدامات، نوری در سال ۱۴۰۴ موفق به ثبت رشد حدود ۵۰ درصدی فروش داخلی و ۵۱ درصدی صادرات شده است  که توانسته جایگاه این شرکت را در بازارهای داخلی و جهانی به طور ویژه تقویت کرده و ارتقا دهد.
*خلق ارزش ؛ از رشد عملکرد تا رضایت بینظیر سهامداران*
گفتنی است پس از ارائه گزارش عملکرد شرکت توسط دکتر غلامرضا جمشیدی، مدیرعامل پتروشیمی نوری، این گزارش با استقبال بینظیر و تشویق پرشور سهامداران حاضر در مجمع مواجه شد؛ واکنشی که با توجه به عملکرد درخشان نوری، رضایت صد درصدی سهامداران و تشویق های مکرر آنها در حین ارائه عملکرد شرکت، نشان دهنده این بود که مجموعه پتروشیمی نوری در سال ۱۴۰۴ توانسته است رضایت سهامداران خود را به بهترین شکل ممکن فراهم کند که می توان آن را دستاوردی بینظیر در صنعت پتروشیمی کشور دانست .
این استقبال به‌ویژه در زمان تشریح رکورد تولید ۱۱۲ درصدی، عملکرد فروش و صادرات، حفظ دارایی‌های ارزشمند و اقدامات انجام‌شده برای عبور از چالش‌های نقدینگی و تأمین خوراک، جلوه بیشتری یافت.
مجموعه تصمیم‌های اتخاذشده در این مجامع، از افزایش سرمایه و تقسیم سود تا حفظ و به ثمر رساندن سرمایه‌گذاری‌های راهبردی، توسعه پروژه‌های جدید، تصویری روشن از رویکرد پتروشیمی نوری برای تقویت بنیان‌های مالی، حفظ ارزش دارایی‌ها، توسعه پایدار و خلق ارزش بلندمدت برای سهامداران ارائه کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/679954" target="_blank">📅 13:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679953">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نایب رئیس مجلس: بازگشایی تنگه هرمز هیچ راه‌حل نظامی ندارد.
🔹
الهام علی‌اف: باکو در کنار ملت ایران ایستاده است.
🔹
تعزیرات: سهمیه آرد نانوایان گران‌فروش قطع یا کاهش می‌یابد و واحدهای متخلف ممکن است تعطیل شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/679953" target="_blank">📅 13:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ad7XoWYT3WvXEEA0fO1Kg8S_Fa9GuLrAuq56leOcBjXuTW75g8PZubX20IHfWwsa1e3ev3ZgAn7Um0z-HSlgwP119BJIOvImIoopydMv25ag6toGAhFO4HMfS8HpOnqkAzzoA13ZXmy6RoGpellyxhRcbVBFp9K-C5f7k835SbnlGirVT5Naj4qU_tHoZCQ1BGHug32jQuFJBgFpvlbBHSyCZvJrACZ4gny4Ghi_YnMIhbvnWpAL_5p8k9edm6sECjsVbNrqTi3VHLHTavjJtiDLttwv_wP83lgIxD6E4hJbc7ic7UMzK9OTIBrFwIudhTdSoTJZ0qbtXKqSr8R7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCjofCTTj4PF8szqiFkdUy5VUqOi7BrUP2xrdWBbrm1XNEcjhU1OtevdzsiYwQz7zho0NnVrrKKoOcSJ8yTGeXEyEcy9z_sEvUwmaKC0CQDPqiSNlyncgKzzODjJyMSMkXzI8_q7dWF4kbOcgfneV3ngmT2SNKEqh8nVXk3HC1uaM721KNQB8WockWe-frpDX08uuYHtT3AdeZ6w3_PGVpTiDY8id042QGU4qHTXwG4B317ESu3AikUM0ezfEn1dcYQOXZbm8EdqG-kxl3G2w7lOO5eQ126WNJbHqoO_C4Nk0_0_a7cDcuLgfehVLcE3q74da-1Mf1HeLLhuKEXwsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMqaJV4gTNq-ywEDOMhZl-Iu3yDF3ojciEml9etrhnI95BW_ea40RXKIAgnFXm3Zx9CBglLzMg0_FXfMWRWbqtb_LZWeNeGwi5PKT9JlWrox7nGiatPo5wMFhBjyax7f_8ikCGxcxBQR6TuD9R3F853QgYztP96q7G9Kap22mkwZAEGyzBKRn-zhzxWwpx-PJb6ggll90zACOPluCFB5IdbEsnzw6YnD9RJtctbqHYSCnq7DYBMi0ENxdvYpjUnJYbOYWehUFcSmV2YSNbh0CObxsSlEWtsPGSWsx-TZZY0IXG-XyWh_0dsUni3iPK8MbE4PHGlzXHKoPmVvcS3C8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wu2CJceHM3fs_5IAGgbXkjqCe9jfegsrRDljmryUIM-bTYdBptTr9b7Wuo_BiGDWYSyzmMiDq3ij5jCxnmEfNAmxf_6Oba9RGbx7usevpmaPckcumV2HMl2KdGl8sMHm9YFQoyw3UqyocN12eRl4M5zFPIK4vm0KfvGZmUQ4BoFV-qpHY9kdalifmCSqDPiMWkf4lDPM1v4DcTLUqPYvdhuanRPtMQ3F4JQ_qG6OB5TBkHxjN18Zww_icPjEGdbaPQ-HVa26x4LZuP4VvA5BR_zhwTqRWr1dqBcakqhZHVFaZ1_Tty_ELdPQJCfR46SPfMkv9u6vdy2wBvFsFmGSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi7wNIIdjVgFELQDVYoBUfo7OTbqwrrUgc9vXFwGqn6RxzZoHhpT-0qoMRJlQ16tfasWFPm21AfdoQS4MPpFBuX-7XWTVQsFfCFt3qpFa-M8keCsNiwoBMzFZE-AlLGCeV59xmFQ-RvPOXKgR1uVZ1Y64z0kGJGvUX_ATkKipw6xVK4EFtUZT2H83oDkMgepNBizE4J7tMoilFnLZ32J8LMN1ooxtjScWsqYcaUb43K33kbHAuHJEjNfo-eJOU1iTBtxmscJnRUr3SxmZi9mC83kAlUCADdPbNhVDWWj0_Vv34uUIfyc239y60mRd0EG-IpYBhFq_7tbz2IxqcCuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZNloHJ5WtFUrUZR38cybRTgNpytyVgAdyTubQv3_5As22IOUGt4zTw5sEw-r_Gz6TOuEGz3k5X_s0rnUMr0hhsyizJKl261drbPyq2wP9r9G8Efg8j_Beq3KFYTJKPfyMo2MHUPNb628N5po1tOWhWFGmyLrskE4OWe-9qINjCb2aRfR2FcQPSvOpfq_4bc8yXPuLy8SKJlmScjKqxv_dd_TdYh2VZW0cuvJNkP6hKfEExtsnaO-bCDVcQ_FY6pXv2ABjocWnpJ0RP0LBNucj_uVm2M1LtQ2ouA7LciEmum0FO2S5dds9WdVXHd01wuaCi2Dq8yBiXZ3jLGk-aJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlQoEZDenYKmshT-QQ-DJVyGdEAu-mWWTBSgPSOBV_2ZmS6Xq14vsDfI27utCEWmcysEa7dKpB0u3o3Do1xKKC2l8upBZgZN34pv7dMmgbghzgFYr7x5JKUbVT6IFCUDr1wc_Nw-RunOJbt5XEFxt2jGZnqnEJz8nNVBApesNyDoC6SWae1ui-6OqS2ui3KumzHX9LbSRgEewyRL8ykS0nZFOgisTZpqOnzB0Zo1cbSE_NdHktZZhCp3vrc3XDPvdjUOo7b5IDe2yJiEkotulQpaBzVwJklPSGa8E70Aw9Gl5yzPjU4FGfZ1ZOCDAkN6wH9vx7SqVICJUL6xhPEUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faxtueQRpBaVsIKeDC2nPp0yutN7CLFjAgXyihI0_wnrHO9P9qgn8kvc1hM9iZ6wRqRyfvk5R6QyFcTNExSIj_4t5kQ5m10VkGyZqXqKUkpqlSRjOXV6_CLw8TdMY8SlQbDceuHDc4v4gO-bA1Cmn7ECwTaOBdKTO_fUCz-wN0s7hGo49Zrkl2dlQfwmh87gA7gyUIIh7Rpdl60W5HjRB-BLrRAr8YsM674A7LQhiOOyiCD963s5UgKd9Mj2VgW_hGhy3-Ig1_UrvPiRvccXgdtnsqi-TgDm04R7HXBHpLwmKucxHr4btWZ3TTdl5HW0iybYHS6u8anpNo2ZSjQopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsz2YUc0qpnN5CPBJ2h_Q7KPY4t3YQkqdonO9uEEKDVDnSL4C1Wpw7D5zN10Wz5G9nPUjraclUXAx8aHfSu-pUdUWQeV8QCEL7HVd3MELVwsSojA9uwEcbEzMD7vbYPius0mPW2NySGuSrOmQAe4e96PQXPcedfalvz9s9YXnYwc-SmtA4I_8FhF55qQnkzzqIF4tlC3tfET6B-JabODBBCu7R7KpUW87Ca4vCAsixlgwnvI8aH0Q44MYdCQZ3DolkXx5qgAsrBM2MEEGHhvEmZo6gx7W3XoTJwv9pbZah4qn3fws0a_Jb1jVxpTUlGQDZcWWpYgK4Gd2Q1SFsFpHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حال و هوای موکب هیئت قرار در مسیر عاشقی
🔹
موکب هیئت قرار در محل تپه سلام مسیر ورودی به مشهد مقدس درحال خدمات به زائران پیاده امام مهربانی است، چندین هزار زائر پیاده از روزهای گذشته به سمت مشهد در حال حرکت هستند
🔹
هیئت قرار با همت کارکنان هلدینگ تبلیغاتی و رسانه‌ای خبرفوری راه‌اندازی شده است
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/679943" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679942">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXwjBIlfysuwK0JWYup7OiaFazlaY_AtvQCS2zstFHtAMPxMwJVLRKHnYmjaqGwTlPCbYsvuMg9eWkaVQ__aXOm1ftrTXv0daAShSEakFoIBLWX5ZavKxlEbNsPi2BRg6YjM5dfP5jlcGDKJb00elgckVjRqHRX3mPPkGiozKpVG2vAsAd0i3cwiV6f4mQ92N2kX9F9xDVMSqys648D9nzKi0hK6Qp_rOSisI8tKubVzgk92tdkVIboD_FMERQw97j-eeR2WR8_O-iw-SGi_KvasIwhAYgzwHSr9kvN-rnozbVi47h6IS08bgF_jZJ-t_gAwhiwg69Pmo2TvedOL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر رئیس جمهور: با حکم ریاست جمهوری اسلامی ایران دکتر مسعود پزشکیان، محسن رضایی به عنوان دبیر شورای عالی امنیت ملی منصوب شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/679942" target="_blank">📅 12:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
قطع برق کمپ کشتی آزادی هنگام تمرین ملی‌پوشان
🔹
به‌دلیل بدهی مجموعه ورزشی آزادی، برق کمپ کشتی برای چندمین‌بار قطع شد و آزادکاران مجبور شدند با برق اضطراری، در تاریکی، بدون تهویه و گرمای شدید به تمرین ادامه دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/679941" target="_blank">📅 12:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679939">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LM7aZ11D8cFYfhH3Y7NL2y80oWo69i6-9G7x3HshdAseDNcQYEBBu5boeFmGcCfPAlRUDR9bVBigbkbKsC7CLrQDDltfaFIkKV7owcJhZpkjuaSgz_lpDTtGb79Qe-8bywxEXwD_F5__BAe18EZRwrkhzDmPiyVTnlGtxlsYD1V_zNfBuSLkAG-kY7BagMmqqw85MB6RXG_EOE6Tf2m3CETpaRFm6Ikz4wDg3mh4Og5yrEr7e_bMp03IhC0_d3z5tLCMRts_uZd6t8lITblJewy25rtMifhGg4k8jtQR-Iupw2RaWZc6ZGpdQ4-NMd4Ai2vGsNtZyYMidteqI3yJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dd93d429.mp4?token=qB9DQ4fIMrQ-ODvgTfIRyGX0McZ_zFh3UVX35qe5W24av_EqQQKOTCjgbJ0aKiqNwfF7gHGEOmtrN755SopQAEzqszjcaO-SGLxZE_yrFGq9G3x6tajhZA4Qgoh7GVLLk3fAPP394BpLgUgpik9oVXmOQLP_WVaIncUc5-Zn5qnUqCVCCs_m3xjp_x1SfhlaeMwBRlFeWy4pJ6p2R6brJa0DZmKghbfEawXS5JQdbPK4iiy0C2v3DZN_QpSxrrHv8BsTq2MNaHNsYmpFhJ6egVonCg9w3nmn2TQJ_kDZyvPKHHrDw9FFmeYhV4dkpLFPrRal1ubhA14HlW-6oA5H1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dd93d429.mp4?token=qB9DQ4fIMrQ-ODvgTfIRyGX0McZ_zFh3UVX35qe5W24av_EqQQKOTCjgbJ0aKiqNwfF7gHGEOmtrN755SopQAEzqszjcaO-SGLxZE_yrFGq9G3x6tajhZA4Qgoh7GVLLk3fAPP394BpLgUgpik9oVXmOQLP_WVaIncUc5-Zn5qnUqCVCCs_m3xjp_x1SfhlaeMwBRlFeWy4pJ6p2R6brJa0DZmKghbfEawXS5JQdbPK4iiy0C2v3DZN_QpSxrrHv8BsTq2MNaHNsYmpFhJ6egVonCg9w3nmn2TQJ_kDZyvPKHHrDw9FFmeYhV4dkpLFPrRal1ubhA14HlW-6oA5H1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرتضی پورعلی‌گنجی به پاختاکور ازبکستان پیوست‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/679939" target="_blank">📅 12:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679938">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3ROz5xpb5mf4mhojeuzFZ9Fgjy4gDBLzSrdY0ida8pSt9Sg3Ly6jzLjZOGnhVtRKIgYudATjuzNtkD84NzE86qTFvNJ86J-a6ByCtnv200Va_N2W40ocIpfgi7EOJwBNL2GaRAMeTuYB7361cD4mk0vL5cqde66Rphd9R1GZSzTgyLuWiCEqtuxqiImHBzR36zgAOoNT6JFVf7rPB7AgP2Qpmv2T4kn81Oskvl5wgkLgSs4Zj2TmTSDzKeTJYxmf5ViCPproSed9cq6Kncuq58Hadkg_RKCzQ1mjSpweG4oU4_VEE5K2KqVqD5bdeKat97l_-pek_i5HSd2rSUe8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/679938" target="_blank">📅 12:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=PG4cvn73lbWC0eFFMaMBg2J36qPWhf05CnpFjSCZ9biu8Z31445SC91VRLsXxZ7PcZtyA4VEfX-r414KlWCoAInlKntBuuSTHjIyGs48WLIXirqX0-mcnv2KWxnN3DuufkrLxIsCiF5gURDkim-JQyNW28Q0KcJKuVHcTPBopFDhZbdaQ8gfzGDNc12OilsxT7JbzyppBH3M3o28Cz4n8Zrs5ug_3iHeoDuAOfpkS1gD8HdqP3m_i0pInCNl7stHdvReZUMa44k1pUeXB2HCbYU8AiK6DThCNF9Ab63Ys0mz8InMOhHAGwIlyMMuUQspsa_Jtt0KKzaebPh3Iaf7VCDPNUVTUxwUR65ThT8Sceby7JmYXEjhaMe_aVrNJQNtxIHuH1Ma8E5f2JQ4R3fpMEa0Js7_8loh6wNzdchkVHiMrKvIw09gsM2CsuVHYlLX_0gVQynzG950CkB33jW9M5EHlXP4bdX8_jdjjSZ3dR9e__d3rhBPHhIu3MPz2B3OnfSkIGdhiGESJ2pB0o3JfLLd6GoYmerAnYx2ddHnG3JnYrcnTND1EanIAaM6En-s84kLRFxxTPf_SD4DJ1IjbUomXu4TUl4ixSMi6mCUmwzN4q1oCOXSMrO4TQ7kyJLL8QFyuL4o1vIOJxzk_Xhg23VhiBCgAWRKivnezjeLzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ba817d81.mp4?token=PG4cvn73lbWC0eFFMaMBg2J36qPWhf05CnpFjSCZ9biu8Z31445SC91VRLsXxZ7PcZtyA4VEfX-r414KlWCoAInlKntBuuSTHjIyGs48WLIXirqX0-mcnv2KWxnN3DuufkrLxIsCiF5gURDkim-JQyNW28Q0KcJKuVHcTPBopFDhZbdaQ8gfzGDNc12OilsxT7JbzyppBH3M3o28Cz4n8Zrs5ug_3iHeoDuAOfpkS1gD8HdqP3m_i0pInCNl7stHdvReZUMa44k1pUeXB2HCbYU8AiK6DThCNF9Ab63Ys0mz8InMOhHAGwIlyMMuUQspsa_Jtt0KKzaebPh3Iaf7VCDPNUVTUxwUR65ThT8Sceby7JmYXEjhaMe_aVrNJQNtxIHuH1Ma8E5f2JQ4R3fpMEa0Js7_8loh6wNzdchkVHiMrKvIw09gsM2CsuVHYlLX_0gVQynzG950CkB33jW9M5EHlXP4bdX8_jdjjSZ3dR9e__d3rhBPHhIu3MPz2B3OnfSkIGdhiGESJ2pB0o3JfLLd6GoYmerAnYx2ddHnG3JnYrcnTND1EanIAaM6En-s84kLRFxxTPf_SD4DJ1IjbUomXu4TUl4ixSMi6mCUmwzN4q1oCOXSMrO4TQ7kyJLL8QFyuL4o1vIOJxzk_Xhg23VhiBCgAWRKivnezjeLzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدرالحسینی، کارشناس مسائل غرب آسیا: پس‌ از ۶۰ سال تنگهٔ هرمز کاملاً ایرانی شده/ حاکمیت و مدیریت ایران بر عبور و مرور در تنگه تثبیت شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/679937" target="_blank">📅 12:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55254c2963.mp4?token=bP26LZdVMPkuWGPCw6ng32OSkTEnAgE7lfx3R0U1_x8IWOPjOZR90GIYbvOhWu1x9v9B1EH6DT_Z_XYl93jBQ3kR-O4LtrW7r7QH0ZDWWuIfKUy8E0zavUdP7_jpFwleakhX12gVM6Bf59xANVmmwgHXTtdlZWGxsbs2XUn8cNIjrlMmU_75pODiFGlF33OcRak2cSvkc__Wpo242syOB16l40noGe1CrHRJrA9U2tqgCy44ZW9HlOc2bIbwXLW3YWPe-2ShpYsXQMmVcrb-viBRqOPiIep7LTLOrC-E2KpjBW402FGoyx71bEP7hypYOoN-iOyw5R9f5lCBE7BtsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55254c2963.mp4?token=bP26LZdVMPkuWGPCw6ng32OSkTEnAgE7lfx3R0U1_x8IWOPjOZR90GIYbvOhWu1x9v9B1EH6DT_Z_XYl93jBQ3kR-O4LtrW7r7QH0ZDWWuIfKUy8E0zavUdP7_jpFwleakhX12gVM6Bf59xANVmmwgHXTtdlZWGxsbs2XUn8cNIjrlMmU_75pODiFGlF33OcRak2cSvkc__Wpo242syOB16l40noGe1CrHRJrA9U2tqgCy44ZW9HlOc2bIbwXLW3YWPe-2ShpYsXQMmVcrb-viBRqOPiIep7LTLOrC-E2KpjBW402FGoyx71bEP7hypYOoN-iOyw5R9f5lCBE7BtsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان زندگی مستربین؛ خاطره‌ای برای همه‌ ما
❤️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/679936" target="_blank">📅 12:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDS8fSBAhqrH1uDdkpugN1qFOlHNDP2cdzjGuMtMVTzaPTJvfinQv-Hugygfw_WqbZrpI--AStoGs0-PqPn6jrky9z7TrkB6AnFab7-PxqA52hfUO6teAwjaAPOgkaEtoomzXsBp3V-JS3-cDdxwhgjrvD6XMuD947jvB4sLFnT0Kbv8rFoTgVJcj24qKce87jpLs7rySng6eRepBhMF24INAwBgEVBQsdY0RDh5JR9zcbXNF4gVDO5ZdO5TRRDcW9JUNwHhMPo1KRcJrLqeVv7oiR0RcygKXl1G-pOyHzK54b0MdOOXUhJsMEvvubsT5OjFPOqM0EVSPJrHqSJnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با عبور از ۵ میلیون و ۶۰۰ هزار باز هم رکورد تاریخی زد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۹۴ هزار واحدی به ۵ میلیون و ۶۵۴ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/679935" target="_blank">📅 12:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679925">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88f47e1bd3.mp4?token=rLpvQD6xUjk_DZWCZevfrSY0R7xWk3rS6aO9OsmCHEvX56rF56qZeEsFxQIxYycnbMXZNAmVXCDPCJOSmNBREhCLg47NfEQEskLo2-VPYVVihIKDakYxmLBOA5Wfae2DmBW8Cpq4hGF7wR385P6HIxP5WfiKBRXZbhipgmLvWyI2z5Ydb13SIcfgDsNyWDRR4cAAeWLx4MHuowgVoEo84i5u0fDmWUX0IjUz7CRQILrfZ6B5qkkJvuYGPQkuvWWAo2BUhXiR0RO8aesykMtsvPShgI0fB6iSvS4iGOE8OcERMMf9C77iKed2XPOHGJ4NLY-PHy6pIGanuJWgt40vgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88f47e1bd3.mp4?token=rLpvQD6xUjk_DZWCZevfrSY0R7xWk3rS6aO9OsmCHEvX56rF56qZeEsFxQIxYycnbMXZNAmVXCDPCJOSmNBREhCLg47NfEQEskLo2-VPYVVihIKDakYxmLBOA5Wfae2DmBW8Cpq4hGF7wR385P6HIxP5WfiKBRXZbhipgmLvWyI2z5Ydb13SIcfgDsNyWDRR4cAAeWLx4MHuowgVoEo84i5u0fDmWUX0IjUz7CRQILrfZ6B5qkkJvuYGPQkuvWWAo2BUhXiR0RO8aesykMtsvPShgI0fB6iSvS4iGOE8OcERMMf9C77iKed2XPOHGJ4NLY-PHy6pIGanuJWgt40vgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم  سخنگوی وزارت امور خارجه:
🔹
همچنین حقابه ایران موضوعی حیاتی و راهبردی در مذاکرات با افغانستان است و در سال آبی اخیر پیشرفت‌های ملموسی حاصل شده؛ رایزنی‌ها برای تحقق کامل تعهدات…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/679925" target="_blank">📅 12:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679924">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d434b9cefc.mp4?token=atdtmxcHhALkxhwALd3JFn9G0t797AGPS-JJgzJdMbOex8DqY3UXvbgvq5A6ugp7eSPylUyyWs5_dyA5K36BF-UQjkgiUeEJDsx7NZYchOFd67gewh_BsQjGNtMvMgPtCWEX2nBQ0eoxze8Hq7rkMLtrkZU60Q70A9nhkFROU1pvwSkDPRMZlCnkhQ8zkfaorbuZSV-_R2HX4a7AtshsKoc0FXmAiZLqBq_fcKR8jGItszXapd0AHCPtU_yhh8VLFYuW00-UQKU_iuCAne-NpW9ioYmIBti4rdz6rNUMKl7bmNbd-o3MzgdnmppxP5Yap-d8ndZ7SspglrgiahprBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d434b9cefc.mp4?token=atdtmxcHhALkxhwALd3JFn9G0t797AGPS-JJgzJdMbOex8DqY3UXvbgvq5A6ugp7eSPylUyyWs5_dyA5K36BF-UQjkgiUeEJDsx7NZYchOFd67gewh_BsQjGNtMvMgPtCWEX2nBQ0eoxze8Hq7rkMLtrkZU60Q70A9nhkFROU1pvwSkDPRMZlCnkhQ8zkfaorbuZSV-_R2HX4a7AtshsKoc0FXmAiZLqBq_fcKR8jGItszXapd0AHCPtU_yhh8VLFYuW00-UQKU_iuCAne-NpW9ioYmIBti4rdz6rNUMKl7bmNbd-o3MzgdnmppxP5Yap-d8ndZ7SspglrgiahprBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«نترسید… پای وطن بمانید»
🇮🇷
ایران، تکه‌تکه نیست؛ یکپارچه و جاودانه است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/679924" target="_blank">📅 12:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679923">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOJAHS2gV97tOC4WMsEV4w9-nY5J1kekDWiAnxvH_YkWEodiY2XGPaoaYa1J2v0eDqWWIEK2tf9mrI0Vd5NDj8DwSMWNFwKne9fOKQRocVv1j3ENVRAQvdG_7gYNldyx4fo643IeOe6CA7tkRiB3DnfwXpZ8hUadXEqw7R3o9XwKv9Lk6su1PHapWwUVDZjsuGuYj1JHtjVVwH6-ZlD1lH_dU6I4z7I_kAHCqFZjdR64hk2N7rVVE8gNvsP6kZ-ryRDltyzjKsS8XkhJ3dS644auOOjmKFV7KBXOisZi5MAPKKxzb2OULK-bY_3njDKcXM40Brc6KZydlSvEQ2wuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
يايان يك وابستگی راهبردى
🔹
بهره‌بردارى از نخستين و تنها توليدكننده الكترود و محصولات گرافیتی در خاورميانه با سرمايه‌گذاری فولاد مباركه
🔹
تامین ۵۰ تا ۶۰ درصدی نیاز کشور به الکترود گرافیتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/679923" target="_blank">📅 12:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679922">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c24c2ca.mp4?token=pwANrxO2j99BZCY5v7uPabcEkRc9nJAyWKin4HRfgAcONcr_zDx2AOD9aZiixlzmzUPtjzEnHnk6k1vkZrPkeADCTRqx0asvCNbisWgS2ZGOZjVwqodH1F6sRtx3SfBm9BMydW1FGqea9ksjz8N8mCHP1ciwAzpCnZq5wiHmGh1OpCc4EF0icHb2ZP2kTODBAYWBzQaKMgTpvsMue_MhyBQ6VR44M0vkBS9CTaEAEQin7eV01_MOIgij8AgcnGwoh-rst57kkg6d-rlUzSPxjbameb5hNRezQT1mRs8Eapiat0lH1DROZ8Y2cVoHb1XUEoqOV-yM86u5BPdDyx_XrGlG-zzC1VP_PNSowZXPuN04_aClR2AKaoBd0kv_CYok9ezTIivSjG8AYpe1DtesxhMqhqg_ZnLpDbhgzOZGXjXsbHuFtxSOAlArzrFUeRfaYukMwqcojDIDRcISsQAZIoAcwvb_cvsoBXDDMnAzgKHRGb1z3BvQy_NT2qyjYxgI--YSTzw1y1t_b4obIANb7DWpC4Yp7TPNWD0Vh2Q9sy8uCk2Pxv0Ly3oUmGmdFdpXuQFAeS8nt16cLNcyXwfDaQ9SKH1XdIr3NHaiu-frvNpTS3DrlgzPvmO08wAtBy9aRN4cLusV6yEL6q95Y4794CXuV9cF-odpvZuyaZD8xmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c24c2ca.mp4?token=pwANrxO2j99BZCY5v7uPabcEkRc9nJAyWKin4HRfgAcONcr_zDx2AOD9aZiixlzmzUPtjzEnHnk6k1vkZrPkeADCTRqx0asvCNbisWgS2ZGOZjVwqodH1F6sRtx3SfBm9BMydW1FGqea9ksjz8N8mCHP1ciwAzpCnZq5wiHmGh1OpCc4EF0icHb2ZP2kTODBAYWBzQaKMgTpvsMue_MhyBQ6VR44M0vkBS9CTaEAEQin7eV01_MOIgij8AgcnGwoh-rst57kkg6d-rlUzSPxjbameb5hNRezQT1mRs8Eapiat0lH1DROZ8Y2cVoHb1XUEoqOV-yM86u5BPdDyx_XrGlG-zzC1VP_PNSowZXPuN04_aClR2AKaoBd0kv_CYok9ezTIivSjG8AYpe1DtesxhMqhqg_ZnLpDbhgzOZGXjXsbHuFtxSOAlArzrFUeRfaYukMwqcojDIDRcISsQAZIoAcwvb_cvsoBXDDMnAzgKHRGb1z3BvQy_NT2qyjYxgI--YSTzw1y1t_b4obIANb7DWpC4Yp7TPNWD0Vh2Q9sy8uCk2Pxv0Ly3oUmGmdFdpXuQFAeS8nt16cLNcyXwfDaQ9SKH1XdIr3NHaiu-frvNpTS3DrlgzPvmO08wAtBy9aRN4cLusV6yEL6q95Y4794CXuV9cF-odpvZuyaZD8xmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در حال بد شریک‌عاطفی‌مون چه رفتاری باید داشته باشیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/679922" target="_blank">📅 12:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679921">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dff1a45c5.mp4?token=svRhEWotZiqzUY63DlNIYM9JxkrpsKBWvoScuT8wgqKLjdDpLG68xrxJY0BTHLp4tIRJOkfjQsmy_fGBlzTTDZZA5A5dGx6IX1BnRkN89Yo1t2ExSeObZA2uHbqcQWvv7FDN0HiGI_NQ-xyoTl384HCAUDRhsWgjia6Ad5CHwFmBx-mV7bDfGPmdB0iuyDTzaamwhn-70qT_u_RHminw55SbqS87MKXD_OETpeIGx7DPhi7UifdKgxn0t5vok8gihn_b7Bxqc9W8t7CxLiYlgSyiceiX-UNZ4J2Nk1Kknoa42BD10vbjSoRyAhRUPNUYoVf3biK3uNyIzanYYH2Kjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dff1a45c5.mp4?token=svRhEWotZiqzUY63DlNIYM9JxkrpsKBWvoScuT8wgqKLjdDpLG68xrxJY0BTHLp4tIRJOkfjQsmy_fGBlzTTDZZA5A5dGx6IX1BnRkN89Yo1t2ExSeObZA2uHbqcQWvv7FDN0HiGI_NQ-xyoTl384HCAUDRhsWgjia6Ad5CHwFmBx-mV7bDfGPmdB0iuyDTzaamwhn-70qT_u_RHminw55SbqS87MKXD_OETpeIGx7DPhi7UifdKgxn0t5vok8gihn_b7Bxqc9W8t7CxLiYlgSyiceiX-UNZ4J2Nk1Kknoa42BD10vbjSoRyAhRUPNUYoVf3biK3uNyIzanYYH2Kjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم  سخنگوی وزارت امور خارجه:
🔹
همچنین حقابه ایران موضوعی حیاتی و راهبردی در مذاکرات با افغانستان است و در سال آبی اخیر پیشرفت‌های ملموسی حاصل شده؛ رایزنی‌ها برای تحقق کامل تعهدات…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/679921" target="_blank">📅 12:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679920">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae87096f27.mp4?token=oAtFTRvS5HA-G9K4sMPbUZPgc_ZmaOc2axyVnGtEbhuzZTA0ENgdmkt7Yb-qmWUtBll1EydLYMWYEp0i7EDCIPtW2btPA4cG2rxq-E6dLDkKJbcT8e9qfsyp_JT0UfS11mE8Cp_vZPFIKnb2S4o0UqXYZ8BUJ-W_PiP3FK-E_BE1ildTDwmbv7oYh1mEEroaKFLZue4A1spNKSJqqRq-ZZ2Ix3jn_uoragbUGsk2xKm3EHyiWsZeSql6N0fHcyi-acdDVkr6GZ0mJ_IKR_5nG9VENXRA0xLntIu8i2YV4gupzeIJ09x9I63wTB4luR0fe_GnQQwojcWlzuC84DPHOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae87096f27.mp4?token=oAtFTRvS5HA-G9K4sMPbUZPgc_ZmaOc2axyVnGtEbhuzZTA0ENgdmkt7Yb-qmWUtBll1EydLYMWYEp0i7EDCIPtW2btPA4cG2rxq-E6dLDkKJbcT8e9qfsyp_JT0UfS11mE8Cp_vZPFIKnb2S4o0UqXYZ8BUJ-W_PiP3FK-E_BE1ildTDwmbv7oYh1mEEroaKFLZue4A1spNKSJqqRq-ZZ2Ix3jn_uoragbUGsk2xKm3EHyiWsZeSql6N0fHcyi-acdDVkr6GZ0mJ_IKR_5nG9VENXRA0xLntIu8i2YV4gupzeIJ09x9I63wTB4luR0fe_GnQQwojcWlzuC84DPHOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار مکانیکی از دل ضایعات!
🔹
مردی روستایی در چین یک بازوی مکانیکی غول‌پیکر را تنها با استفاده از ضایعات فولادی و کار دستی ساخته؛ بدون پرینتر سه‌بعدی یا تجهیزات پیشرفته.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/679920" target="_blank">📅 12:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679919">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: تا آمریکا رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد
🔹
شورای عالی امنیت ملی هرگز کوتاه نخواهد آمد؛ چه در جنگ و چه در مذاکره.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/679919" target="_blank">📅 12:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679918">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5b92e1fd.mp4?token=Q15KY9Gh54NxKlORImy8DfbSfpZckEMNYlFGW6PObK7x1akVk9qGp2QNWcX4bfg4LuXXgKh3Oa4_JymFP8OgLXFOKzs_9zlTYp-SGvYvxp-tWFUSM9vWeyvNz1yJx2ILa2ypwiUjU03MOTnEFOJW6PfX4zhr8ZZaEQBB_4lVoxehP4BYsEY4Wy-v_cEuH3mJN8aHO0Mnod6MpRSLWi7EyXVUXJhKkleY0sar3h9MYW3IK5lWvxengQsBEA8aEgvNvMyMCg-UvbVC8fxjLEo7mqNy2QqwkSpGnQzHeaNX8kc34eZXmPpaY5qzP5Cwl-uBpsatnePoxCfz6TbM4XlXDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5b92e1fd.mp4?token=Q15KY9Gh54NxKlORImy8DfbSfpZckEMNYlFGW6PObK7x1akVk9qGp2QNWcX4bfg4LuXXgKh3Oa4_JymFP8OgLXFOKzs_9zlTYp-SGvYvxp-tWFUSM9vWeyvNz1yJx2ILa2ypwiUjU03MOTnEFOJW6PfX4zhr8ZZaEQBB_4lVoxehP4BYsEY4Wy-v_cEuH3mJN8aHO0Mnod6MpRSLWi7EyXVUXJhKkleY0sar3h9MYW3IK5lWvxengQsBEA8aEgvNvMyMCg-UvbVC8fxjLEo7mqNy2QqwkSpGnQzHeaNX8kc34eZXmPpaY5qzP5Cwl-uBpsatnePoxCfz6TbM4XlXDTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطع برق کمپ کشتی آزادی هنگام تمرین ملی‌پوشان
🔹
به‌دلیل بدهی مجموعه ورزشی آزادی، برق کمپ کشتی برای چندمین‌بار قطع شد و آزادکاران مجبور شدند با برق اضطراری، در تاریکی، بدون تهویه و گرمای شدید به تمرین ادامه دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/679918" target="_blank">📅 12:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679917">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOzsRDLELFTHiN6Q_Sich4iJBXFLPD6H7sMEJaCzfSCQyu-Wpkd_7p1BExpG-GTfPQkD4PO245jLQbI5QN7YJwhNS4kMAC-m0ZHdhD7Ry9tMKow8L8Uit-DO47dBPQNp_HS4ZHsqkdtCiPiGHP9ip0ixZg6jFh_GZBA38ODijqGQ7eKsl2Pd1T6htwfHD8YCmYxbZqnHf_TrmsGCzJbMDcjQHhfuhCfK9G-PS38xBZyCTARDV9J3-N9yItsIeJKGtN-ODFleP1y1VQjhcdhaztQH_BZy3aryM5arKNlLm0YBzEzLZ9oIX6lo9HY28ltZHfwot3neMvaCCoaJSfCs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نیت خیر شما، لبخندی بر لبان کودکانمان خواهد شد.
امروز بیش از 14 هزار کودک، تحت حمایت محک در حال پیمودن مسیر درمان هستند.
با حمایت از کودکان مبتلا به سرطان، امید رسیدن به فردا را به آنان هدیه دهید.
روش حمایت از کودکان
#محک‌
پرداخت آنلاین:
https://mhak.ir/makakcharity1
تو می‌تونی فردا رو رقم بزنی
❤️
موسسه خیریه حمایت از کودکان مبتلا به سرطان محک</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/679917" target="_blank">📅 12:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679916">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b0b97643a.mp4?token=t-NpXnPGUF1pDpwDhbV_72x7b0vrypHqV4SUWGx0hxuRJCf-EYvxggUKLz3bg1rSvPOzNukeFqVqD6YdVtJxwv4uzwXT9KYNuzlYqGsNaQH7MH5aets8_DxPtPmUWsoTYdWj7V4jhtBiaVbNmXBa4gOwP7-loiBv7gbJJEIwbiFASKz2JMTRYQ10oSF3EM_DySlQfwNe0mw7AnIEXnbLUKq2yx0T1p13xjmFY6NDLYIdd9ja1DTZNaiuNSTCTYg-HtQNY5bpuv7fttJgYal6BYp0IWOGScPLoMJw7a4sOKvqhQcaP7nDaafkfvsRgDKMKiAoFI-hgVNfHbWSXklKtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b0b97643a.mp4?token=t-NpXnPGUF1pDpwDhbV_72x7b0vrypHqV4SUWGx0hxuRJCf-EYvxggUKLz3bg1rSvPOzNukeFqVqD6YdVtJxwv4uzwXT9KYNuzlYqGsNaQH7MH5aets8_DxPtPmUWsoTYdWj7V4jhtBiaVbNmXBa4gOwP7-loiBv7gbJJEIwbiFASKz2JMTRYQ10oSF3EM_DySlQfwNe0mw7AnIEXnbLUKq2yx0T1p13xjmFY6NDLYIdd9ja1DTZNaiuNSTCTYg-HtQNY5bpuv7fttJgYal6BYp0IWOGScPLoMJw7a4sOKvqhQcaP7nDaafkfvsRgDKMKiAoFI-hgVNfHbWSXklKtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قاعدتاً خدمات دریایی مابه‌ازایی دارد و باید آن را دریافت کنیم
سخنگوی وزارت امور خارجه:
🔹
همچنین حقابه ایران موضوعی حیاتی و راهبردی در مذاکرات با افغانستان است و در سال آبی اخیر پیشرفت‌های ملموسی حاصل شده؛ رایزنی‌ها برای تحقق کامل تعهدات ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/679916" target="_blank">📅 11:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679914">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بقائی: استفاده از تسلیحات ممنوعه در لامرد و میناب مستندسازی شد
سخنگوی وزارت امور خارجه:
🔹
ایران جنایات جنگی آمریکا و رژیم صهیونیستی در مناطقی مانند میناب، لامرد و قشم، از جمله استفاده از بمب‌های فسفری و مهمات خوشه‌ای را مستندسازی و پرونده آن را به مراجع بین‌المللی ارسال کرده است؛ پیگیری‌های حقوقی تا احقاق حقوق قربانیان ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679914" target="_blank">📅 11:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679910">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c90ea6259.mp4?token=W8OKC0mEZbmBCgUJexHvVLTIJI7CR4vH_mLKhbceyXTORt3jR2VzCjOjcQrtdlcU_DpDCMAl3GC19POMuI8Gu7K1KuNLRtGaxh-rVIxNrDETMesG02VBlKAv07HJTwaFcbdLP3SVZ9qUcdCaKF_dI6xY_pc21WAxXx7AxsWpFzvPb4ZO8unDduFa4QzrHecXCkkg7-Gt0zXCMIa5bB2ULfg8jAVHgj7Gm6PaT1oRSkJqJ8BgzZ3_a5QWyyibgJCkjOeg-_DMqPGlYnb865VmbDf6ECdCrYdQHnMrBIT05EzODUyohlXFgan_Y7DYn9FsBT-fL3puNA6u5KnMNw6PlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c90ea6259.mp4?token=W8OKC0mEZbmBCgUJexHvVLTIJI7CR4vH_mLKhbceyXTORt3jR2VzCjOjcQrtdlcU_DpDCMAl3GC19POMuI8Gu7K1KuNLRtGaxh-rVIxNrDETMesG02VBlKAv07HJTwaFcbdLP3SVZ9qUcdCaKF_dI6xY_pc21WAxXx7AxsWpFzvPb4ZO8unDduFa4QzrHecXCkkg7-Gt0zXCMIa5bB2ULfg8jAVHgj7Gm6PaT1oRSkJqJ8BgzZ3_a5QWyyibgJCkjOeg-_DMqPGlYnb865VmbDf6ECdCrYdQHnMrBIT05EzODUyohlXFgan_Y7DYn9FsBT-fL3puNA6u5KnMNw6PlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: ایرانیان شطرنج‌بازان حرفه‌ای هستند
/
ایران توانمندی‌های خود را برای مواجهه با هر رویدادی لحظه‌ای ارتقا می‌دهد
سخنگوی وزارت امور خارجه:
🔹
چه چراغ خاموش و چه چراغ روشن؛ ایرانیان نشان داده‌اند که شطرنج‌بازانی حرفه‌ای هستند.
🔹
هنوز از ادعای اوکراین درباره حمله به کشتی ایران قانع نشدیم؛ اوکراین یا باید جبران کند یا خودمان جبران خواهیم کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/679910" target="_blank">📅 11:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679907">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
سوال یک خبرنگار درباره نقل حکایت سخنگوی وزارت خارجه از عبید زاکانی و تهدید ترامپ: نفهمید چه موشکی شلیک کردید
بقایی:
🔹
وقتی با خوک‌ها کشتی بگیری، لاجرم گل‌آلود هم می‌شوی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679907" target="_blank">📅 11:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679904">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwrvfrwgmTGINv65qO9Lrvh5njzU5bJSImZ1TkG6uaM_Aws1q03o7aduGG4a6RSiIc2A9y0s_1iAYhBvZrqpZRG67lclEk3T_8GH4PV1Of30oS7Nvdb9LAg8z4zj6c1Dw0VbuwV8LO1s377g_Sm9wEvIUmu8hYQqMRDuDXFRHMCCDs-HbpXN6UVrwOzLkzimUF-TBlpGs9AsrUpVefGZZdEV56U4DUm8Azx721j8N6DQAQS1LbPnh_YtpEWNpe9COGBXaRp7Huw54hTPY2Sl3PJ9HyQr8hiAvOezs52WhMtOFCHVl9z23Jlzl-xkaNDplB_sLHAGJOPCXIJsBibYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
سجاده متبرک حرم حضرت معصومه (س)
یادگاری معنادار از حرم کریمه اهل‌بیت(س)؛
انتخابی خاص برای استفاده شخصی یا یک هدیه متفاوت و ماندگار.
💰
قیمت اصلی: ۳٬۸۰۰٬۰۰۰ تومان
✨
قیمت ویژه: ۲٬۹۸۰٬۰۰۰ تومان
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/679904" target="_blank">📅 11:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679903">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d36785b85.mp4?token=Wl2yvwnJD25ElL1FYyQuDL12tzrVj-a_upDDnXsZ2Vx0E_R8wCe0FYvci5twl2KVyzCm2Wk7-zo9d5FD5fM1g-EYAxev38uhag00YV_KUEgcVyy2h3LENUequq-4QYBPfze1vxgCV_SIRyXQ8MrSHJnYO9_Z-5W7DsFMmcwquNvcpJUoGxOo3kxSC1SSo2oc0q_0BhGCI3lZlp_--Fag0OgMTgeA6QQv1dzsdHDZeM_-y0KiAbp6lxYbfaFe9_1VyQxqkppX98HMZ3hlvIDi7w65DMAzQJpsPvavQyYOVaE-6OfZuAQZ9W8Ki01lFAiiZrPl_aVvj6G5MDaqGyofRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d36785b85.mp4?token=Wl2yvwnJD25ElL1FYyQuDL12tzrVj-a_upDDnXsZ2Vx0E_R8wCe0FYvci5twl2KVyzCm2Wk7-zo9d5FD5fM1g-EYAxev38uhag00YV_KUEgcVyy2h3LENUequq-4QYBPfze1vxgCV_SIRyXQ8MrSHJnYO9_Z-5W7DsFMmcwquNvcpJUoGxOo3kxSC1SSo2oc0q_0BhGCI3lZlp_--Fag0OgMTgeA6QQv1dzsdHDZeM_-y0KiAbp6lxYbfaFe9_1VyQxqkppX98HMZ3hlvIDi7w65DMAzQJpsPvavQyYOVaE-6OfZuAQZ9W8Ki01lFAiiZrPl_aVvj6G5MDaqGyofRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: مدیریت و تأمین امنیت تنگه هرمز بر عهده ایران است؛ نقض عهد آمریکا در تنگه هرمز عامل اصلی بروز درگیری‌ها بود
سخنگوی وزارت خارجه:
🔹
تنگهٔ هرمز به‌خاطر اختلاف‌نظر ایران و عمان بسته نشده که با توافق ایران و عمان باز شود. بازشدن تنگهٔ هرمز منوط به تحقق شرایطی است که در پی تجاوز نظامی آمریکا و رژیم صهیونیستی به ایران تحمیل شده؛ ما هنوز در جنگ هستیم و تا وقتی که محاصرهٔ دریایی آمریکا ادامه داشته باشد و سایر نقض‌های آمریکا نسبت به تفاهم‌نامه جبران نشود، تنگه باز نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/679903" target="_blank">📅 11:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679901">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907b318f4.mp4?token=KOA_8qYQK4N-v_zPccegHg59-aC6qwUek4ondst63FoOn0qJo78FqoXR8A-hp-7bcCMHX_TM2Ja9zi3M7G9OjCgV_v56u7WxAqKP2iWCs8NoTeHNNY0GDNBEgwbnoAPgnNBNBvPBc5TCFOFogtqWLbvVnZ-JM6OsbaVtoHBAN2zVQghAMUO9gmikBJJUAWmEfaAgHFLRS-3d6gSAw7BNma6ymPAkQfszvRnkcC29G5viN6rGYvtJZ5ytIIraNMjHllYpNkcqP2rpH62BLN0Dsxn1q5LM5kcKRBekda35jy2hZz5UBWuA4QERbq8EuVgX1euU8LZtHoz9oKEqIBEANA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907b318f4.mp4?token=KOA_8qYQK4N-v_zPccegHg59-aC6qwUek4ondst63FoOn0qJo78FqoXR8A-hp-7bcCMHX_TM2Ja9zi3M7G9OjCgV_v56u7WxAqKP2iWCs8NoTeHNNY0GDNBEgwbnoAPgnNBNBvPBc5TCFOFogtqWLbvVnZ-JM6OsbaVtoHBAN2zVQghAMUO9gmikBJJUAWmEfaAgHFLRS-3d6gSAw7BNma6ymPAkQfszvRnkcC29G5viN6rGYvtJZ5ytIIraNMjHllYpNkcqP2rpH62BLN0Dsxn1q5LM5kcKRBekda35jy2hZz5UBWuA4QERbq8EuVgX1euU8LZtHoz9oKEqIBEANA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا پزشکیان به نیویورک می‌رود؟   بقائی:
🔹
تصمیم قطعی در خصوص حضور رئیس‌جمهور در مجمع عمومی سازمان ملل گرفته نشده است؛ امسال هم در نظر داریم از این فرصت استفاده کنیم.
🔹
همچنین دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/679901" target="_blank">📅 11:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJ9AJrGkjnLFBfpFrxNdLa9z-iolP5TqB6d7d-y5rPrwU_Xeh9DWbc6zVS_3VSeFOXBNYjICFIdStX6sCoQ62al5R4Ij6UGj9ltwZ_c0nliNH_ocGx8MaZ8BN7Wm-iNtmlZB6MROIZVoErNOneHwZdTFaA6RPWcTzlZoR1-cVv_3tnTnAOu9EAKNVZ4F6F05JgZHo4hJ13cQwiW0MrKIPHUoBxMfcp_RguWmK1l_0wbPh2v6gLBKZ9j2yBdsBag9tjtfpHfZ0I1dDnNeJAd94Vb2hZgJkZF3wwgWrZGzOpu-6-VXSXrHpeQMnr8AE4isfNhIJpDF_YvpWu47mDRi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ns8esu2Jb7C7trjAgu13sJP_D_LhgbIWWx1W4lIkJ-p9OeWE6WUXSqMTepNNmWsf9paBzjOwYUMAcoSWUJAUFIancepjaWbtGLqW1VKDXja6BewXJwjv6F93fFmTn_c5l1B9xtbUb1BakNIENALeUwfwEfFSEkaoGs1RfITr_9xFqvU8rAn7DST9UKVGSCon3EKCr1Bx-fm5KE0S_z7qlYEmTOxg2-rcZ9Gh_4ErPgsewVLQnIs6ZjRlGcdOy7hODLUy9WfCX4efg51yMUAmRi7Co1XFEk6NEM8pku5VMNu4btwuYsUn2mg27RmAINJ1QO97XalAJgIoMVIcv-jCng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو تصویر متفاوت از محسن رضایی در کنار رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/679899" target="_blank">📅 11:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69fb622a4.mp4?token=jXdGTEPBu4bfYwixgCa45CFT98iHkIYwu1oHt9ARTUgvPTmJ3wFpoVMuqW7EIZhogjMSkuvosxNWUigeEPKbMfWCAELE_7Dh33HtUfwAR-HGH2xM43vpXdsKItxT0a8hlTaVNG-J4gDEvSN4zQMI0yjMvtAUd6frveXSxDY7XynJwm1QdmUyeuJRzTUxyzjS2QsIi_jvXEUhLRyxUnI-1Cg4JiKEZ7eFa4n3vhIoC6usExuqvkFbybUMYkl7Ieo0WK-b-4ePGgCbyiG7vdszn7tAPO_pbeNtde-t9bfMtWI9l7zvz8xDI4DBP9AOcqdTx9q7juKRfLLGveIZazbD5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69fb622a4.mp4?token=jXdGTEPBu4bfYwixgCa45CFT98iHkIYwu1oHt9ARTUgvPTmJ3wFpoVMuqW7EIZhogjMSkuvosxNWUigeEPKbMfWCAELE_7Dh33HtUfwAR-HGH2xM43vpXdsKItxT0a8hlTaVNG-J4gDEvSN4zQMI0yjMvtAUd6frveXSxDY7XynJwm1QdmUyeuJRzTUxyzjS2QsIi_jvXEUhLRyxUnI-1Cg4JiKEZ7eFa4n3vhIoC6usExuqvkFbybUMYkl7Ieo0WK-b-4ePGgCbyiG7vdszn7tAPO_pbeNtde-t9bfMtWI9l7zvz8xDI4DBP9AOcqdTx9q7juKRfLLGveIZazbD5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا پزشکیان به نیویورک می‌رود؟
بقائی:
🔹
تصمیم قطعی در خصوص حضور رئیس‌جمهور در مجمع عمومی سازمان ملل گرفته نشده است؛ امسال هم در نظر داریم از این فرصت استفاده کنیم
.
🔹
همچنین دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر وقت که زمینه مناسب باشد این سفر انجام خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/679898" target="_blank">📅 11:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ig7IN9gX6df-uTfwhCEHl_Tv9GOb9h1nxuwmvkICXxCO8QDesrm-wZKn2Fgu20rEGGu0_bcQUGS3WPQJz9xq64g-yRmWDC-ap06uuq3RQjgt8MHRqPBRE-jyDlZ0CpL93NrddQ1y2okxViYdAjy7g6qcJlYFNC8szLleqJlhQzXe1FSIjMulNfIBRyLJ8L45RlGYaScD5SjFPSQpX74-srrh1DCwgb-ZGC7Xiv6Ukw3sXdgO4MA6U5fH-fSaWZTl-48sgIiDwv6pR4PdVJck2VE9HEFiGfxFzXVaGUY2uMOuMHWogU16s-6zUYQD7xh8grVEyWGsj2Lzbypm_2TKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از احمدی‌نژاد در جلسه مجمع تشخیص مصلحت نظام؛ روز گذشته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/679897" target="_blank">📅 11:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4bafcaab.mp4?token=Uo-sUwl_0djO2z5rvLm3jsUlggUMA6-v9ga6v4YWRAYl1L1aVVBwz2P0kwsEbKkWS5XYcEIpW3CJ3zZbVqA1Sl97MmVgi6livDDsKqICX5NguUCXCem6BPam_fL_hsNJ-mS7uq75nx9h1EdjNL8Tt3538WbU2znBs3bHJ9E9LSv_T6vVNca8hX5ueZ6sdKjl34Ob0J6CbBf-pobo3-8pqsN5socT4exfXzg9INeKyl0btLjz0pJLoPn_g93lk9PTTAnL3D3f6jecYnQR01BCzTzBTAeGqHRTAvGs9iE65XxtG5oMfGmW1Nhuu6rtpqgwrF4C0-S9mkW5ax3177kMkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4bafcaab.mp4?token=Uo-sUwl_0djO2z5rvLm3jsUlggUMA6-v9ga6v4YWRAYl1L1aVVBwz2P0kwsEbKkWS5XYcEIpW3CJ3zZbVqA1Sl97MmVgi6livDDsKqICX5NguUCXCem6BPam_fL_hsNJ-mS7uq75nx9h1EdjNL8Tt3538WbU2znBs3bHJ9E9LSv_T6vVNca8hX5ueZ6sdKjl34Ob0J6CbBf-pobo3-8pqsN5socT4exfXzg9INeKyl0btLjz0pJLoPn_g93lk9PTTAnL3D3f6jecYnQR01BCzTzBTAeGqHRTAvGs9iE65XxtG5oMfGmW1Nhuu6rtpqgwrF4C0-S9mkW5ax3177kMkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/679895" target="_blank">📅 10:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd277d9b53.mp4?token=mXLQ8NRStjDcokD8-JVKd_4S8PcYgQQOxJ8D0w_TtqQd9F-SN0-wxyCjLo9J1eCCZ4iSkYJC_G8r1CSrTPGXwdj7T7g8jppwhQtzCigOx8Sz-9qLv1J1DD7LwHQmn6kunYHfe6C_OQun8daoyv6d-jv54TY845gNlAjqjIz0cZCvBe8qqdYq8pgNxwbVRhdxP1_lJfXjWqKPxpyWS2b3b1Q994GkF3VlOnEZzjwyTuenNbqB3GfhoHp6ATV2si0L2BVNne7MA8iqTTngUWtzSyLHk5AcktPjS9txx_zmJlTPKBlACM7CEyBVm10ytYx2LesCk2eOEudm-SeqpyeHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd277d9b53.mp4?token=mXLQ8NRStjDcokD8-JVKd_4S8PcYgQQOxJ8D0w_TtqQd9F-SN0-wxyCjLo9J1eCCZ4iSkYJC_G8r1CSrTPGXwdj7T7g8jppwhQtzCigOx8Sz-9qLv1J1DD7LwHQmn6kunYHfe6C_OQun8daoyv6d-jv54TY845gNlAjqjIz0cZCvBe8qqdYq8pgNxwbVRhdxP1_lJfXjWqKPxpyWS2b3b1Q994GkF3VlOnEZzjwyTuenNbqB3GfhoHp6ATV2si0L2BVNne7MA8iqTTngUWtzSyLHk5AcktPjS9txx_zmJlTPKBlACM7CEyBVm10ytYx2LesCk2eOEudm-SeqpyeHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/679894" target="_blank">📅 10:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679891">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmUjtUOS5bN0JnBfxh_sBnEjncFG_cs7hEzch6mTG2FcvhzjGWIs3VrLY_tb4jD6_Iw3rQQp5gTg2ZBNJEtGgF6uG-_MdybZSEuB3WtuafmpZ_FitKJy_mj8GgSZ1oNLMDAnvqp4HNe_3ROgEMokLLznbqIFstZSLi-lGgv4m-xT8N9MfBmn4UR3U4AluMrqZHdkSxI-HaoQBC3jxZTNueaMEjS3eUmN2CLUJPbHF52sg2FUNSny58oQlR-LruPufA7p_6rJebM1yLnEG4NApha7A01EYLBlHZN6EP0IXO024KYHAAk57scbUXRWNujMs2ysu2DIi6BJzt_J9Y7cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«ونوین» در بازار رکوردشکنی کرد / ارزش بازار بانک اقتصادنوین از ۱۰۰ هزار میلیارد تومان عبور کرد
🔹
در مقایسه با بانک‌های بورسی، رشد ارزش بازار «ونوین» همواره جزو بالاترین‌ها بوده است، به طوری که هم ارزش بازار و هم رشد ارزش بازار این نماد، رتبه‌های برتر را به خود اختصاص داده است.
اطلاعات بیشتر:
https://www.enbank.ir/s/mfa8Od</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/679891" target="_blank">📅 10:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679890">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a024cee033.mp4?token=S6HP6IwtNgvQhxwtixsx1b2e1ihKW-1Uug9ElVA5YBPPSG0taeGQvYY7pDleq2ZU_t6lWYxWmTHMl4GQEcMdvDdqgS26CDM8Y6anoNW9cIBvbhjSeLZBeebNW5oUrvBCM67X1EYeXMS1ErUobb9Zt2yzGBLheUSxl3lkqKNe9HETpH74TfA6TdFHu1Nh0-6Xr7LpqMIUdt2Ia2-b48iiE7ST0aQr2KLJCSxSoFPXSR1x10Qi0Qq6bgvDxl14PfIrLDT75vY8V5ZbJWJjfFt2lt-L0GlJmt0vQhTARVtjDX0Jzenwp9govFN9WFmnkhKuNzOLM0jP4HBNIYxTPsvedA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a024cee033.mp4?token=S6HP6IwtNgvQhxwtixsx1b2e1ihKW-1Uug9ElVA5YBPPSG0taeGQvYY7pDleq2ZU_t6lWYxWmTHMl4GQEcMdvDdqgS26CDM8Y6anoNW9cIBvbhjSeLZBeebNW5oUrvBCM67X1EYeXMS1ErUobb9Zt2yzGBLheUSxl3lkqKNe9HETpH74TfA6TdFHu1Nh0-6Xr7LpqMIUdt2Ia2-b48iiE7ST0aQr2KLJCSxSoFPXSR1x10Qi0Qq6bgvDxl14PfIrLDT75vY8V5ZbJWJjfFt2lt-L0GlJmt0vQhTARVtjDX0Jzenwp9govFN9WFmnkhKuNzOLM0jP4HBNIYxTPsvedA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در سفر شی جیگ پینگ، رئیس‌جمهور چین به ایران، دستشویی هتل خراب بود!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/679890" target="_blank">📅 10:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679886">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMh7J5ezHZmeG5kpZlPPG2er1H-XhflV6AYHJ_FeMSsUeM3gKLETBUnt-ujlaCjfGZcx9hYts5_Kosuizbo40DVjqekYwBH1yaJWBUC0ZmFq805jkoysv_presnY2pZucavpOIIjyQW7ztHOiDhlWmwdz_ZYQsZrF2fGVFSwNKcqfkPcvv9vQgcjH01bhhWUXebY8cTLEUuY0sk3rTaNyvoG0-jNjLrOtM4hL2QeB4YEcrFqF8tfrRJ6EsQihFo8TIXIfVvPG9FpNDV1mFNDScNaW2zI_GOnC2KamEdrh1oN1jSWhK9m84OvKzkC2YipsMD3OK3hchm1vFvLgCtvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میدان نیلوفر؛ ۱۶۳ روز بعد از موشک باران
🔹
حدود ساعت ۹ شب دهم اسفند ۱۴۰۴ میدان نیلوفر و خیابان عشق‌یار، موشک‌باران شد؛ بقایای آن حمله بعد از ۱۶۳ روز به وضوح قابل مشاهده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/679886" target="_blank">📅 10:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679885">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره تخصصی اتاق تهران برای توسعه تجارت در بازارهای خلیج فارس
🔺
اتاق بازرگانی تهران با ارائه مشاوره تخصصی، شرکت‌ها را برای ورود و توسعه تجارت در بازارهای کشورهای حوزه همکاری خلیج فارس همراهی کرده و مسیر صادرات را کم‌ریسک‌تر و هدفمندتر می‌کند.
👈🏻
دریافت مشاوره:
۸۸۷۲۵۲۶۹
(۰۲۱) |
۰۹۱۰۲۶۶۹۷۱۴
|
service.tccim.ir/intl</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/679885" target="_blank">📅 10:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CmXrqop1uanWMAkRw13GqhSFo4mPqrQGksmt-ll05lh1YehjiIGwSOwY9z1q84D5bDZ3--F49ugbsfnqC4ARZngDvCkz-nVa5yciKPrHAO3N8OWVArvm5otj-CtKobNl82o0etCKao86OgagZHZjbaoEihcn-Z0B_Xp8PPMmziHbyiUJ_UfnlP2DaE7Bfj5bjiYXiH_TrTIAlTllbeuom0jYHyj-L7siwmBqKjLOdoN5dltHNk73FsN79ie-dbeMDhbFy3h5kOcg0Bm75gmXyZBLBs300qyxWtuifs2oY6jF3bqwEp261RRSI1ZXYvq5u0pIMSwJgTnaWrTnR6oRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWSeHEY04ZqjLOPJJlM_qvjHCrivOrP0tI7nlUOCPmFne4UoNyQQntaoEyhu50nVPJa5dfMfIKIT-u_BVKZxDcRfsASKy3dEmMYbLAuGWNyDulm-aR_Q30rUp7Qx-kfLiUfGIe7lRWt_l2u6Yp7I_UpWyAwKxUwOC-TgudSQUaCYpLDTzW9hyq8PNijPZ1PZAQBSRbI6cDZRFtaLcOq1PWFt50f36ifz2VPqhqeiYMOuMaJs9Mh2WShkcuc0sZlcHVRsiY6qe6qHchhGhvWU0xi94ELvIW5Lt8gbfkeE0Z__oXFj1K9GrbUpyEKo1hAedIAmfiiR9yasSHzBlM7u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b53MUZ6sfo9nG1bb_-FIhYNvoF-O1x_1kiQTFUTWUO5zlCwIJGyYU4xmhcSEKVFdb9zSr7xhYOdvDFWRzcVl5i_XyHPvfPBiYh4Ut6rQyWHrfn7N6W3lFgUB1VlWKU90CGj6zWh4bK_y84sEvNk3Jozj2eCM5Nukm3wC_T1v-MFX0HRtgu0CQ9uR8kXmfkBLeHpESxxR-1PpnUtanb4qrbSGk6SiTzWvhewYXXgMEaryJPSIm2zdW9-U7XSIpH3RAAHfRO6GTRsQVjZWapDe6RYsiTzERH4gVBwsf2A_PapLB-YW_iDI897WeGJ7NmsjX4HVcnx37g2LJjGHBfOYdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چنگیز وثوقی، بازیگر و برادر بهروز وثوقی در بیمارستان بستری شده است
فرح‌بخش کارگردان سینما:
🔹
بیش از یک هفته است که چنگیز وثوقی به دلیل بیماری‌های قلبی و کمی عفونت و همچنین مشکلات ناشی از کهولت سن در بیمارستان است و مشغول مداوا است./ ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/679881" target="_blank">📅 10:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
اولین تصویر از کلثوم اکبری بعد از بازداشت/ زنی، اهل ساری که متهم به قتل ۱۳ مرد که همسرهای صیغه‌ای او بودند/ رکنا  #اخبار_مازندران در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/679880" target="_blank">📅 10:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da51d32c6.mp4?token=pvVS-deP6XkbfPb7pLty-qrtdSwC8VIwCpnqODhvGEUBvFb3y-WQpO4X9F4asA-Av16aMt1NecgYQQOs0rB3zVztjOCiyg5azLsGj9uiKF_jKdAnFI77qD8RGuXdP1ud61aIcMNWas1oGqpyqPHfOwiL2H7IWF21Yd9AY7EqfdA2aXb04KFBLBcQ7EGlyorJkpjNLNPOc8o_cG48cFlaS-tfT9SjCEREZS1JY0yqnn-5j9RcA3EHbSP7PWpNR7DP4VsWl_5QpfDbeBlLsH3fZaDD-hPc5-qgb1EvPOlmqs4Sc6OTOCskRJiIV_HyCD6YT1rx5DPylCIaaXU31k47ybKMQA6LuDT7q3kgjqdPKAka8PXiMqZiEPOlWhAe8RNw0k1B6N257SanrJZeLEwZXKJMOXRnn54m37PtBA8eGNi_bve8jT3ZSDTSab9vaQsDRk7DxAKPHZi_MxqP60xeFNc8vl1MIq66jOKoC8bWOMWVWOiOZdg6CWvk5flC5lbGmUljw_waJCBDt2gkEmjbMnOr5fUnNiES6RiRPb0yG222Qhw5ImZjCV7298fvjoEaH6RlJs-RHJfkRAWrEHG0QVQEm145BcGTAi0YuMjABb6BMg7A0_tFg9RX3ZBkHJHqOXgensns9_6OrKbh0YmaRyyJLQ2RxUFnKbyKi8xTFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da51d32c6.mp4?token=pvVS-deP6XkbfPb7pLty-qrtdSwC8VIwCpnqODhvGEUBvFb3y-WQpO4X9F4asA-Av16aMt1NecgYQQOs0rB3zVztjOCiyg5azLsGj9uiKF_jKdAnFI77qD8RGuXdP1ud61aIcMNWas1oGqpyqPHfOwiL2H7IWF21Yd9AY7EqfdA2aXb04KFBLBcQ7EGlyorJkpjNLNPOc8o_cG48cFlaS-tfT9SjCEREZS1JY0yqnn-5j9RcA3EHbSP7PWpNR7DP4VsWl_5QpfDbeBlLsH3fZaDD-hPc5-qgb1EvPOlmqs4Sc6OTOCskRJiIV_HyCD6YT1rx5DPylCIaaXU31k47ybKMQA6LuDT7q3kgjqdPKAka8PXiMqZiEPOlWhAe8RNw0k1B6N257SanrJZeLEwZXKJMOXRnn54m37PtBA8eGNi_bve8jT3ZSDTSab9vaQsDRk7DxAKPHZi_MxqP60xeFNc8vl1MIq66jOKoC8bWOMWVWOiOZdg6CWvk5flC5lbGmUljw_waJCBDt2gkEmjbMnOr5fUnNiES6RiRPb0yG222Qhw5ImZjCV7298fvjoEaH6RlJs-RHJfkRAWrEHG0QVQEm145BcGTAi0YuMjABb6BMg7A0_tFg9RX3ZBkHJHqOXgensns9_6OrKbh0YmaRyyJLQ2RxUFnKbyKi8xTFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین باهم یک دسر انبه یخچالی درست کنیم
🔹
یک عدد انبه بزرگ
🔹
یک بسته پودر ژلاتین
🔹
یک عدد رانی انبه
🔹
یک بسته بیسکویت پتی‌بور
🔹
نیم‌کیلو خامه قنادی #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/679878" target="_blank">📅 10:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679876">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
شهید علی لاریجانی پس از شنیدن خبر رد صلاحیتش توسط شورای نگهبان: این‌ها اشتباهی هستند و این‌ها باید بروند؛ من هرگز روی صورت انقلاب، پنجه نمی‌کشم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/679876" target="_blank">📅 09:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679875">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea5aa23a3.mp4?token=Ls_dQtS7OLUcx8sKR5kdMnUHN6av3yS4PQW3rPgG6vpb34PEh-6PPnMtmMcHhbduv3IKHIvCIGtsgS3WbbUxmUDn1ezWqlHoB01F5TaMU36msyVjvalRc1tnrFNC--UjeO6DIzPjvHZ7jsZJxa6dX-YrQ0cYLKBcKLrSMU-R6CerDwHKFFH7S3s1LSzrAjguWqy1hxkVio_QjeSZFIvQKiagZT2_kN35NKtCRfpQcD9ekwTf-l6PHV5hbkCK6Ezq9eROv-7aIMaL1KTOID0efU0gnQIWhlLPKYA3bZDKgRa_7T0DYgABwaWqHfaiECRHY6YAKFKBM0Sc_pLLnaISGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea5aa23a3.mp4?token=Ls_dQtS7OLUcx8sKR5kdMnUHN6av3yS4PQW3rPgG6vpb34PEh-6PPnMtmMcHhbduv3IKHIvCIGtsgS3WbbUxmUDn1ezWqlHoB01F5TaMU36msyVjvalRc1tnrFNC--UjeO6DIzPjvHZ7jsZJxa6dX-YrQ0cYLKBcKLrSMU-R6CerDwHKFFH7S3s1LSzrAjguWqy1hxkVio_QjeSZFIvQKiagZT2_kN35NKtCRfpQcD9ekwTf-l6PHV5hbkCK6Ezq9eROv-7aIMaL1KTOID0efU0gnQIWhlLPKYA3bZDKgRa_7T0DYgABwaWqHfaiECRHY6YAKFKBM0Sc_pLLnaISGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا همسرت همیشه صورتش را می‌پوشاند؟
عثمان دمبله:
🔹
همسر من یک زن بسیار مذهبیه، پوشاندن صورت در اسلام اجباری نیست، اما اون واقعا بهش پایبنده؛ گاهی بهش میگم که حداقل صورتت رو در جمع نشون بده، اما اون همیشه به من میگه: عثمان من میخوام فقط تو صورت من رو ببینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/679875" target="_blank">📅 09:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679869">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJ8oG3YZx51UAt1sCWnvbHB_Qc2ZXsDZnlehi6J7h-ATN1mdjaGIROtrwPxfITMdNyLSWZ9_MgNI7AVbFsFMnZkGPqgimQPR6D9t8rmP8SSXpbTSVyHdtUVa0tU8I6cgnLNrTjWO0LUHEC5RpHV3t4NtVkM_Bm7gyrapMEsCRKz_RGKD9qxfSBQt8hIzn0LyNKro-I-FieWTzyxfUoTjfslYJjUGqVOyKBlWmSl4tKq6o5ShVK3CY6znpHoHBESkr9tVOV-ZBd0V5XaRnxF22V618vCGZBv23HC3EnqAnLxxlwhj6uoMRfxut6NTZgE6IzF9YbTTZ37vMnlivMPfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb8oStzC402R6PqtOPqWasWeXNDK72rcUzRnEmHsTcVd_PDcSW0tZvm_taiyVt3yU8CXIGvTRwRHxGRLgB2CtLXjs-GP52tL7CyBqGRPv3B24NLasiSOV2yPNYvQE7Rh1WPflGRCQ6c9ggGnclLEYotEkHqTAOFIbimHinPEoP_bRlBER8B5aF15SvIE8JzGREl-xm86795TXjsyBeuppOGyRmI58Sh9QxbyLYAx34JtfItQWmhV-0hz-N1ju73yT1-re3th9S09BgMaL-yD6OIs_JA9F6j0ZClvUZ_pp2JsAwSCGWIGDExZy1xCHu9x-wKj2mgF0y2FykE464ceoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSIqP2RRfs6F3aMjfK6BCAxJ89TOp-pmIDstxWqzkyEPez4PZoE6YkSKOGtVoQX2P_gpT7Q7j56x-LTfH1fiI_oj_AdTXrbKiKod_WLXai5CcO-5o8qHtxhWsZUh5kWgVG_Ga7WfZNyMDqUSglMswQ2vBKrcf_WZzkWRr2xCCJEOI7HOV0CrCdIv30bF17AaqUkYRYve88_JrOTYOVIuaUpQzlavEPnFzX0TcQ0VChxTFdKmgLwP6b1PnFyLPyjjXpUGGjef7InnjPwqFUio6vTqKjDOQqW2FxjPf3PDNYkjwpnUpHEdAXMNl0dqIc4pznRRpqGlfVNqi_4McOb0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HeqfZ0QGvNdwxWkpMP92X645464dXmsdJEwaZsBlxvxH0P7k5y4xVq7at3GpOnqM20jC1L2CESH0yEo4-9fr_A9gqOxQeftRsu4hgvTaiZIxmDx8LxEgLtgqupCZEdMMIVAqFYOW9xCup9IYBWZu_xPVCRB5jpf6LwGYfjNtRq6fVxIsUOVGPTgP4VGLoGp_4B0GTckBwV2laxAqWu2DZeW6fdX0RDB4TYRZtAx3JzQ_gmBdp7eD9w-65vxQs2dybIkoJ0SVJDiQ-7TB3XDXci_X2hvGQCp8pxKk68EpRoxegWAIp2DGZE2DEqFbPMHaDFuQSP0mKLExynYMMb02rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3tALI-gC-rJIkE_Q-MR84Mmx6OMm6-DgZ2B2l9AeIZ728mWKVsiqOKvg3Pu0hQiiwX9Wk2IcTzFjGXImF3vKIw3OhRbm8W7MJ74GE17zpwcu0nf0EbJT9qRtxEyXzx-2YLj3AySvyLLj5zIxebvmNm8AZixp8AYVVeXbdar7YJkhPjQMQ28eEDXrsLeThKytz98KCLYHRQNow5bJ-qLw16GYg-4Oi40vc-kWCpQPrf47c0TGaFdB_WrtiL5dq-3EEijl9dLDmAqXXssECw0sUhV-SyLkbiA-t-qLqeNRJMlROo2U1BKOgfpG52VLx9cCdYYXfJPZCyI6JH_1ZHLEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵
نوشیدنی ساده و خوشمزه که می‌تونن حال بدنت رو بهتر کنن
😍
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/679869" target="_blank">📅 09:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679861">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c42b704b33.mp4?token=Op5LnSYb4Ulf3hkj_fWDp32j-QiPdKqanNJrJUQDkKDjql155MC1AkmMMHaRqCzfTQRBAmuhw4hBiaw1u6zoSYlrV4-RMyLA0fsfXsxcCDoOAi1V5VHy6LvEH7oFSbQGL2YRE0tm5XIE0e4vYY2dbtGjMoi422t9p6RIZwz4lVWGrzJVBY4v8RME6xH_5BG0F09IVATWCClUwIs56JW1ZsE-oPw1e993abZSbG5FqBaIAQPNJgbtIHSUa1USf-SyVcuzwblnYNxc8CANDMPrJjZx_u-_UAV_e1aEv8p0N6i-AfpIYp-hNP1gI27zj7CEdbXZBiS3OtRNJo7di5-XvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c42b704b33.mp4?token=Op5LnSYb4Ulf3hkj_fWDp32j-QiPdKqanNJrJUQDkKDjql155MC1AkmMMHaRqCzfTQRBAmuhw4hBiaw1u6zoSYlrV4-RMyLA0fsfXsxcCDoOAi1V5VHy6LvEH7oFSbQGL2YRE0tm5XIE0e4vYY2dbtGjMoi422t9p6RIZwz4lVWGrzJVBY4v8RME6xH_5BG0F09IVATWCClUwIs56JW1ZsE-oPw1e993abZSbG5FqBaIAQPNJgbtIHSUa1USf-SyVcuzwblnYNxc8CANDMPrJjZx_u-_UAV_e1aEv8p0N6i-AfpIYp-hNP1gI27zj7CEdbXZBiS3OtRNJo7di5-XvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کادوپیچی تیشرت با یک کاغذ؛ ایده‌ای ساده اما متفاوت و تماشایی
🎁
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/679861" target="_blank">📅 08:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679859">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خورشیدگرفتگی کامل در راه است/ روز در کدام نقاط زمین شب می‌شود؟
🔹
چهارشنبه این هفته، برای اولین بار در دو سال اخیر، خورشید گرفتگی کامل در بخش‌هایی از گرینلند، ایسلند، شمال اسپانیا و شمال شرقی پرتغال قابل رویت است و برای دقایقی، با ناپدید شدن کامل خورشید، آسمان برای لحظاتی تاریک می‌شود.
🔹
این خورشیدگرفتگی در بخش‌هایی از اروپا، آفریقا و آمریکای شمالی، به صورت جزئی دیده خواهد شد و در آن تنها بخشی از نور خورشید از دید پنهان می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/679859" target="_blank">📅 08:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682e4ae741.mp4?token=E0teNFPDEr6rrHiPYrKxXeEYJOvVfUXsIOfsG_vvXeKkFRUwfFOquXbaR91Gq-UmDN0TwwTCkA1XuIjJ6XwAtNvJOq4QPOV5KO2lrKJgvfwcUT7hOHmRYBPa8v19AAxfA9KBE7-RP1YlJg1OcPff0XQmf0thwcfqIA0L0wGp-9t74_YViXAJC2QJszrZx3yqxMfnK1QOcgxxjGITYuDNvE-KktK9hyuKQf-NItLGFZVAdlha7QsDsrUjA8x6MXxfVoqirloX1eOmLY26enSbPavX-OfIacfhXD0msCl26cRi2ISpDooCi9RxGRpb2haLwUbmZBkRKhTAPklxRwGGCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682e4ae741.mp4?token=E0teNFPDEr6rrHiPYrKxXeEYJOvVfUXsIOfsG_vvXeKkFRUwfFOquXbaR91Gq-UmDN0TwwTCkA1XuIjJ6XwAtNvJOq4QPOV5KO2lrKJgvfwcUT7hOHmRYBPa8v19AAxfA9KBE7-RP1YlJg1OcPff0XQmf0thwcfqIA0L0wGp-9t74_YViXAJC2QJszrZx3yqxMfnK1QOcgxxjGITYuDNvE-KktK9hyuKQf-NItLGFZVAdlha7QsDsrUjA8x6MXxfVoqirloX1eOmLY26enSbPavX-OfIacfhXD0msCl26cRi2ISpDooCi9RxGRpb2haLwUbmZBkRKhTAPklxRwGGCYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاس گل عجیب بازیکن ایرانی در روسیه چشم‌ها را خیره کرد
🔹
رسانۀ انگلیسی one football با انتشار ویدئوی پاس گل نادر محمدی نوشته: «عجب پشتکی!»؛ محمدی در تیم اسپارتاک کوستروما در دستۀ دوم روسیه بازی می‌کند.
🔹
رسانۀ انگلیسی که در اینستاگرام بیش از ۱۰ میلیون دنبال‌کننده دارد، به تمجید از این حرکت پرداخته و با تعجب نوشته: «او به معنای واقعی کلمه توپ را با یک چرخش از جلو به داخل محوطه جریمه پرتاب می‌کند».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/679857" target="_blank">📅 08:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90d15cee9.mp4?token=SV5Pgh0Zu-39faHZ4v-aAxmDQ3ulE085P1GfOIL1sVjWlDK5bon1jmdFZWFDrajMKBzGyEVJGjD-QdD8s8AQPHVRurXb4kakofZd76eXBMESvC-VKKCHRhb6UFh-R3KVDNE7prE7FnwncilGQWl6Wc5-jRM8xTgF5LGFDO8bhszapVFbLwMqRH-AKaFCQ0diXizS2R2MsLqYvL3DMZVAMDCFCau7yOuBJD7IaEcwRSnc7buPNVByrW0K7yg6FfbkScZJ5yDhn2xca8XvzvK5T1BB7xRMsC7TfF9oGw3jxiDSQrcqlcu7bsiEcisha-ESEwPOr_fXwdfWE8tYQtPvtR4T2DHlkmeW9d1mfDziMJZp0fBFVkZ6GVdKykwVnMg68_2eF_9lKXsWAf0OvS_Pj-ha5LutKZic9VWK4y9hP21FMpNRfJW1FEz4UAAmBOiNgkc7mEdRw2HDz4aFI1JqwFpi-XAvocTSNfONFx7om_CEYYmFjkVgapAM8vM8ChbLN3rG2AI_U7v5SqQhLNdQEosXIm88xNyow548_UN_bJBM8CFhwEatqcdm6kEf-Q2SBT9czTXFvwpydZV4euF_E_RCZVtqev_ZFK6aQJAehfmzv4SzV-m40RgtjVmA58ttlKRZeEKFJXa1hEk_23mVBlKgwc4gzAMWJekzfySj8RU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90d15cee9.mp4?token=SV5Pgh0Zu-39faHZ4v-aAxmDQ3ulE085P1GfOIL1sVjWlDK5bon1jmdFZWFDrajMKBzGyEVJGjD-QdD8s8AQPHVRurXb4kakofZd76eXBMESvC-VKKCHRhb6UFh-R3KVDNE7prE7FnwncilGQWl6Wc5-jRM8xTgF5LGFDO8bhszapVFbLwMqRH-AKaFCQ0diXizS2R2MsLqYvL3DMZVAMDCFCau7yOuBJD7IaEcwRSnc7buPNVByrW0K7yg6FfbkScZJ5yDhn2xca8XvzvK5T1BB7xRMsC7TfF9oGw3jxiDSQrcqlcu7bsiEcisha-ESEwPOr_fXwdfWE8tYQtPvtR4T2DHlkmeW9d1mfDziMJZp0fBFVkZ6GVdKykwVnMg68_2eF_9lKXsWAf0OvS_Pj-ha5LutKZic9VWK4y9hP21FMpNRfJW1FEz4UAAmBOiNgkc7mEdRw2HDz4aFI1JqwFpi-XAvocTSNfONFx7om_CEYYmFjkVgapAM8vM8ChbLN3rG2AI_U7v5SqQhLNdQEosXIm88xNyow548_UN_bJBM8CFhwEatqcdm6kEf-Q2SBT9czTXFvwpydZV4euF_E_RCZVtqev_ZFK6aQJAehfmzv4SzV-m40RgtjVmA58ttlKRZeEKFJXa1hEk_23mVBlKgwc4gzAMWJekzfySj8RU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ دقیقه تمرینات عضلات پا بدون تجهیزات در خانه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/679856" target="_blank">📅 08:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679852">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i93s7XiZ-PglaExZlzCJDlv8HoNRZ8o10E_QraSesWh5tgFmcPMENKNgFSJPkP67wGfgH-g0ln6MdCIYPPvXWw03EZUrOGmpgO7EuzhZkCktO9E3DPuVx9kzxBA-uMooOJkQPQ-QE_Y-vgTTNk6fDoKWqJ24Q3T6oOeSW58nWRay-ebKPAZeZvhkF7BlxS7aZlCekjNPhsvp_bY2OM6SE1FFOlMz9feY8lVJ_yWBC69clSOULhsXSxHjLcZ7FBv42pXpVYJgbudRLvm4nJKbMCxWbHebNpblGBBBqsk70dWxL1bmz7DrtZLYkedPbS4igdCEckxM7xwzepQGvljcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGkj9agRqoNXf6qWC6ZP1FC-gA-jGiVQP1qaQScEr7cq2zTmfKaRZu9pyw_efl4MzCAalkkcBo_5k9LppuvGesvp6xcoCV1XUWHKY2XfgGGUDHeaF0nzaIOIIV847Z5Msx9ZFJT25vSCJTMjgQ9Gqfkib6gzhqn47kuusi6UzsiRjLQVEdklL_aX7lVZc_De0ZStE1JRrUgv2mIsjbCWLIpxVb4yMAyY8BJoJgUwiBzNay8cosvFdvhtWS6btD3M1jS9by2IyGgHXutYpcZ93E9F2EYtjZvMbolc5_1Xa-Kc0uRDhFfuuhb4bGOrfkUQJiu6QanDDKbADRO-eYjDVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcMunhkPZhHQIxlx5j8Aket_Re2VKcv_yIJZLVveU8w94WrYmLwtG7T07fk-BSv0RFxiw8It2pKJLRGDoGOF6H58nATO-mIXU8Iy5ygHQCZtJC--W42ipM-IbccBAfAh2dIm8BGMHVcbNOQ9aTVgofd6TtjcU5Brq693QE4SzW2k2yK-3z9XQ_fECaA99MQBvWXUYsGmYiGJyRn2rW3VsJfGBTAkC-Scmzto-082ibc2CnnKh5uvg4Sub1or5i-hJQJZ8KKqptjo-8lz1TrKM4wDJD42RfGUtiVnXoUy7zf_IBbdob-jiyCcF2EW0RHiUhf6SzYMtfUUl6raslLdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4UIUTGw9Idp6NPXcvRpNcBZkvriXXKa-309yDc4mFvn3kjf084au_d3D10Ey2XpZV3iNNbSrTXw0HUYjtCpGDXqi86yfPkTRqxLog8HdDFWbkbW0uVk2GuLcIUvmijDFkRula_6QWi9CQVrO-fzWU5wrlhHlFf6R4iN4I-BwnNEd3M_HM9IzCI50sG7UGoTYqdLEAgknDIhudUgialuuhcMsyqnkWmrOmFk10KGo_zUW7j1qKkWGfzlJbF8vgySQ_WeaNDlHWTp7Cdp6nWRIBAP9vmFxL4sSpCevgowWNkzbq2GxbscECwsgZc0epMm4D0GEyskE7pSOFjjRHF-EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بلیت پرواز تهران - مشهد از ۱۰ تا ۱۹ میلیون تومان
🔹
قیمت بلیت پروازهای تهران - مشهد در روزهای دوشنبه و سه‌شنبه به صورت یکطرفه در بازه ۱۰ میلیون تومان است و از روز چهارشنبه قیمت‌ها نزولی می‌شود و به پنج میلیون تومان به صورت یکطرفه می‌رسد.
🔹
همچنین قیمت بلیت این مسیر برای پروازهای کلاس پریمیوم اکونومی و  بیزینس نیز از حدود ۱۲ میلیون تومان آغاز شده و تا حدود ۱۹ میلیون تومان نیز ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/679852" target="_blank">📅 07:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679850">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
چین یکی از گسترده‌ترین اقدامات تلافی‌جویانه تجاری علیه آمریکا را آغاز کرد
خبرگزاری CNBC:
🔹
این اقدامات شامل ممنوعیت معامله شرکت‌های چینی با هفت نهاد آمریکایی، تشدید کنترل صادرات پهپادها و فناوری‌های مرتبط به آمریکا، و ممنوعیت همکاری با نهادهای انطباق و گواهی‌دهی آمریکایی است.
🔹
چین همچنین نخستین تحقیق امنیت ملی خود در حوزه تجارت خارجی را علیه تجهیزات چاپ و کپی وارداتی با نرم‌افزار خارجی آغاز کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/679850" target="_blank">📅 07:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679849">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8MKHdg0x4pSCqVXX06S2xkNxbqkMVAaoGnoHP-2_voZkWTldh4tPcRnbAJrygBnQCSUWmn_yllzm90WT95dufIxNIEW80BrmMlm0sJo7r8kifn2y1HJWb9HWSkmFZIp1X-eR3AU4WvO_wxaSkOqkGNBF-JefyydAW7vz5Urc9vgCAhn_aJ41wcEXKegfh6szkdUYjwojbw3zYg_wB2qmUwoNkZ9tyzQbzdeG_WfXaTJ0HbeKbnrZ7TgaURnbm8_0A3YpzaKth4QHIm9jZ3OYGIx5uz1bDRn3zji2_qfpHL6DpZBaNQP4SABBovqNyv36H2kbBArNiTTLRzWW_I0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۹ مرداد ماه
۲۶ صفر ‌‌۱۴۴۸
۱۰ آگوست ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/679849" target="_blank">📅 07:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679848">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b634713d8b.mp4?token=ASh81L-mZV7F1y8vLGS42lDvZrqVxO-p1j5Vth5K8FWcR_HRcyoNq2QJBZY4-6YncBuzc9iaf071zZTXRPvUtmSFuxvXx1HrXVawfAVVUnajCJj3_Hw8ztYSBMt3pHq8qtiUKTYrXLmdDLh2pY9Ci6eCDaQG6t2k1vxXoZzDa8FuzgWCSrNiFXT79mjDYxH4dfzlFKvU-b0Rr7N8lt7YQ26NHTR20AGzSvU4wAyP1fsb5bJwLQ6Y1mxrwUy1C4HY-5CgdAvTWQC5_xVhnKyaBV9VPrSkU8KVI_kLVQuWXORyNxBBaaEexv-BWrhO-n3P4WYrPFz6kgnsLOCOrXOMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b634713d8b.mp4?token=ASh81L-mZV7F1y8vLGS42lDvZrqVxO-p1j5Vth5K8FWcR_HRcyoNq2QJBZY4-6YncBuzc9iaf071zZTXRPvUtmSFuxvXx1HrXVawfAVVUnajCJj3_Hw8ztYSBMt3pHq8qtiUKTYrXLmdDLh2pY9Ci6eCDaQG6t2k1vxXoZzDa8FuzgWCSrNiFXT79mjDYxH4dfzlFKvU-b0Rr7N8lt7YQ26NHTR20AGzSvU4wAyP1fsb5bJwLQ6Y1mxrwUy1C4HY-5CgdAvTWQC5_xVhnKyaBV9VPrSkU8KVI_kLVQuWXORyNxBBaaEexv-BWrhO-n3P4WYrPFz6kgnsLOCOrXOMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهپیمایی بزرگی در مونترال کانادا در اعلام همبستگی با غزه و مردم فلسطین در حال برگزاری است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/679848" target="_blank">📅 04:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a71c940c21.mp4?token=LcXKanvBrI_5deC2oQBVa_LBrC8i5ETu-XAesq2gqfy1BbyY8y980RORXbtfdIcfXFHtLWItKkSLqq-jxtX8EXA9s-xPDv2DIIMEB5dTpez0CAhtfKoeDpYLf50Uzde24nmCQiymhvAa5ugIAjuwLmtrbAMf4QY40AsNkT9B3hn4ZKBtAQxn0OtFh0bXz581Qcn17SE97NrhWNAspIiq2GnGkbrGOqvhcZeqo-Z2RY4vmPeZ0Hibz5AmLkFkZM90Q3kl753x72u4UsZE-l44R5gPRTeCTHkDsMeolBEVcTa7TeVGbO2WcATciAiM7W7nlGg_fplBxm7Nzt5VBBm5f2QN2L9pe8yqNktxJ7L8yx1g-8ZgJ5mu2_j-qptZeT4HOgOl2V95UGnF1UiIlQZXcupIatsDXRsZmubU_ZdFxXIdPi6g8VmbWSsbIB7I6yixuDHdkXsGBGerGngmJpUVbdeHtpzSQPdWrOE4udLutLPyKSifw4iyG3sOJa-exbL5dQqK12jrq-CiwpO-1teOtRrgh_Uxf6trNQocLPhR_6BoWIwv0vR5ndhZSN_wZq-vN6iyHuKR1LmjSNTEDK0Mzj-MzebS_aXu3vYDjd9PXjV9_clhcI9y_gRyKX_VDY2QGVtsiCWZehqdMWo8i-LBIvjw7mh0lrcT0gC9u-QBz18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a71c940c21.mp4?token=LcXKanvBrI_5deC2oQBVa_LBrC8i5ETu-XAesq2gqfy1BbyY8y980RORXbtfdIcfXFHtLWItKkSLqq-jxtX8EXA9s-xPDv2DIIMEB5dTpez0CAhtfKoeDpYLf50Uzde24nmCQiymhvAa5ugIAjuwLmtrbAMf4QY40AsNkT9B3hn4ZKBtAQxn0OtFh0bXz581Qcn17SE97NrhWNAspIiq2GnGkbrGOqvhcZeqo-Z2RY4vmPeZ0Hibz5AmLkFkZM90Q3kl753x72u4UsZE-l44R5gPRTeCTHkDsMeolBEVcTa7TeVGbO2WcATciAiM7W7nlGg_fplBxm7Nzt5VBBm5f2QN2L9pe8yqNktxJ7L8yx1g-8ZgJ5mu2_j-qptZeT4HOgOl2V95UGnF1UiIlQZXcupIatsDXRsZmubU_ZdFxXIdPi6g8VmbWSsbIB7I6yixuDHdkXsGBGerGngmJpUVbdeHtpzSQPdWrOE4udLutLPyKSifw4iyG3sOJa-exbL5dQqK12jrq-CiwpO-1teOtRrgh_Uxf6trNQocLPhR_6BoWIwv0vR5ndhZSN_wZq-vN6iyHuKR1LmjSNTEDK0Mzj-MzebS_aXu3vYDjd9PXjV9_clhcI9y_gRyKX_VDY2QGVtsiCWZehqdMWo8i-LBIvjw7mh0lrcT0gC9u-QBz18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات گسترده در سئوتا؛ معترضان در اعتراض به مدیریت دولت در بحران مهاجرتی اخیر، خواستار استعفای دولت مادرید شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/679846" target="_blank">📅 03:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: از آغاز عملیات «خشم حماسی»، ایران بیش از ۲هزار حمله هوایی، موشکی و پهپادی به پایگاه‌های آمریکا انجام داده و به ۲۰ سایت در ۸ کشور آسیب زده
🔹
خسارت وارده به تجهیزات و تأسیسات آمریکا ۱۳ میلیارد دلار و ۴۲ هواپیما منهدم یا آسیب دیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/679845" target="_blank">📅 03:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqOwy7XGurEy1ZQhHv9QrFaxxSyAgu5M3VsRQq4FVLn8bS-YQEYvebIYAL-M25Mdrc-O4Yn1q1NuaWlxtCESfvWVJ9E-_EBIpDIVI50LwmJ3y06BOdvWx-LhGRHoXqairvC9pYjif6WwTu2yk7RgHqRfwxIDLhKkTY2980Y52ymnvrPracLMjkbKia9jz51ddpx1Bioq5JZT8eGSTN3SgvImcINncXsKqpZKzFkjY3-a9r4BT4jjmiiUoRiGyJ2Bc0xi2tTe-dyRjBiiRMcC3s-pvR-WKO7cjOBxdhxmjxOafMopmbsd00VhQLFMOjJj94GaXO8Mtpe8dYLAKbp2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای یمنی:
امیدوارم توافق دفاعی مشترک، شامل کمک به سعودی برای خاموش کردن آتش‌سوزی‌ها هم باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679843" target="_blank">📅 02:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679841">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
برای آزمایش بمب جان ۱۵۰ هزار نفر [توسط آمریکا] در وهله‌ی اول از بین میره...
🔹
به مناسبت جنایت آمریکا در هیروشیما و ناگازاکی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/679841" target="_blank">📅 02:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679839">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
افزایش قیمت نفت: ۸۴.۸۳ دلار/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/679839" target="_blank">📅 02:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679837">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8104959d0.mp4?token=KJ3PLe0lI5utC80-BZVsNTtUuEMQBb4SK2ONUME0a8FOJ-b9PEj7iXGEgsUB-86jmGjb5T3Ydckko0M_KmU6yrlP2_rlRu4O-0NKTcgMnNLcZ0rBgew56G3IOohqGaLSV1ywi0SWGri9tgZyrKBuAzJ8cwZGAXNxYFsdi4yudWUUdBhhoHbpDbr4o5YRX3MYbo7kHqgVEV-fEKb7w1w8FhhFiDelSxRnoe--c_AwBe3iXowo7hXp17Vp-8mf6JS1eDMD7n--bEBHPCv-af1w7sTD3BzVaoafKAL9ccEdwIN35wAEr0UFhdQAxNJMkLIJIu949SSOXFUS9rTHhdMGKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8104959d0.mp4?token=KJ3PLe0lI5utC80-BZVsNTtUuEMQBb4SK2ONUME0a8FOJ-b9PEj7iXGEgsUB-86jmGjb5T3Ydckko0M_KmU6yrlP2_rlRu4O-0NKTcgMnNLcZ0rBgew56G3IOohqGaLSV1ywi0SWGri9tgZyrKBuAzJ8cwZGAXNxYFsdi4yudWUUdBhhoHbpDbr4o5YRX3MYbo7kHqgVEV-fEKb7w1w8FhhFiDelSxRnoe--c_AwBe3iXowo7hXp17Vp-8mf6JS1eDMD7n--bEBHPCv-af1w7sTD3BzVaoafKAL9ccEdwIN35wAEr0UFhdQAxNJMkLIJIu949SSOXFUS9rTHhdMGKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صفحه فارسی AFC با انتشار ویدیویی نوشت: وقتی علیرضا بیرانوند روی خط دروازه می‌ایسته، گل زدن بهش تبدیل میشه به سخت‌ترین کار دنیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/679837" target="_blank">📅 01:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هکرها با ترفندی جدید بیش از ۱۰۰ میلیون دلار بیت کوین از کیف‌پول‌های سرد سرقت کردند
🔹
هکرها موفق شدند بیش از ۱۰۰ میلیون دلار بیت‌کوین را از بیش از ۷ هزار کیف‌پول سرد شرکت Coinkite به سرقت ببرند. این نفوذ درحالی رخ داده که کاربران از کلیدهای سخت‌افزاری فیزیکی استفاده می‌کردند و تصور می‌شد این کیف‌پول‌ها امنیتی نفوذناپذیر دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/679834" target="_blank">📅 01:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef5_QAIu8fb2U9U8quVBwuYSSMDCIxH3uG4-SMDjzcfNLW5gTAA4AhYaLLBgUAKGKawoNjLzs2Y_2PFeV1l7NrcQZ3-Wul1WwPGBIJDAfEu2y9kbgzvR8zY8Ju707s2WkEUQjqMPjJwk5ZLgSr7-8WSpWsK0C0YL51ZRGPyYdYqaABQteS6a2W6laiGqh4aqm90QTLeBYfcH79LS0O7dQVOne4tg7ALlrgCygg6BcfDCZcYkrc2UlwxzYLUKN9ury76Uxg_22tN9__D6qvrk_6Qk2_E9QuR9XTrPf2I5SfcIwY8mZKIYn5PxXzfDT_iL85lDGY_SUAkAfJciIIZ4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: همین حالا باید جلوی خسارت‌های ترامپ را بگیریم حتی با توافق بد
کریس مورفی:
🔹
من حتی از یک توافق بد هم برای پایان دادن به این جنگ حمایت می‌کنم، چون باید همین حالا جلوی خونریزیِ فزاینده خسارت‌های ترامپ را بگیریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/679833" target="_blank">📅 01:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54f13a0af.mp4?token=WISAQ054ZsEb0J4Q6g5zXeYTz3N5Rj08GoR1WhXXNfp3Nf0zXtrtA8n2eHYvDXMqiBHvyR1txTDVIzZwlcmS6igXE7VBSbJAdie09SPeKEhEJ8TF4wsI3OFHzxqAbTonO8eNAT-roIWZG75U3LeX8KlcqqPAWUx60K-jAJBq27ugb66N2tY_BXIReyomQv7xPdaiUeYY5qsTXgdOKLnpL9dAEJ1WCoR_HdpPa27o2rTtidtrUxfhOZK4Kd8_K6eNwyjLqhFrsmBNYsLZXGfVjMgD6QpjiIQVq3e4gVQOd_5MrA5t8xjK3J2zvQs6Sas9Iyx1TD8OOJ5go7aGV3TkvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54f13a0af.mp4?token=WISAQ054ZsEb0J4Q6g5zXeYTz3N5Rj08GoR1WhXXNfp3Nf0zXtrtA8n2eHYvDXMqiBHvyR1txTDVIzZwlcmS6igXE7VBSbJAdie09SPeKEhEJ8TF4wsI3OFHzxqAbTonO8eNAT-roIWZG75U3LeX8KlcqqPAWUx60K-jAJBq27ugb66N2tY_BXIReyomQv7xPdaiUeYY5qsTXgdOKLnpL9dAEJ1WCoR_HdpPa27o2rTtidtrUxfhOZK4Kd8_K6eNwyjLqhFrsmBNYsLZXGfVjMgD6QpjiIQVq3e4gVQOd_5MrA5t8xjK3J2zvQs6Sas9Iyx1TD8OOJ5go7aGV3TkvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرنگونی یک پهپاد متخاصم در جنوب ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/679832" target="_blank">📅 00:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
برخی منابع خبری از شنیده‌شدن صدای انفجار در نزدیکی تنگۀ هرمز خبر می‌دهند
🔹
شبکه راشا تودی گزارش داد، شعله‌های آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/679831" target="_blank">📅 00:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
برخی منابع خبری تصاویری از لحظاتی که یک کشتی در نزدیکی سواحل عمان، در مجاورت تنگه هرمز، مورد اصابت قرار گرفت و آتش گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/679830" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c140aa3b9.mp4?token=XbxGdmAl30pJWEkZ-4KxZCAQahjTvFbTR9sSazMFCxx3ArwICZ5I3jwoy8sEoZLgvwJewJ545GS2WEuomT820bZu1qg6b-8tSZ7h1CZ7yFZ8HOoNqXhhenaKinFMYxD_a9GjYgdaSRXBL8NdMexdzTy6IVi3PngAUbSQyDxwgY_Fj0cT0XNRJGd9m-91daRQF-jm-iM57ndPmymp0SFZ6vrIam4OCWT5-N8XxLFbWevOS2MaHe_lNuDk7f-HDBLcxd2qr8Ql94sBezGicDzhw7F29xBnD-8bHczB2jHSD6xNRg_uMCvaZokcoKGC9OsRZV2dYrzJ2uHTTw5IGvr3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c140aa3b9.mp4?token=XbxGdmAl30pJWEkZ-4KxZCAQahjTvFbTR9sSazMFCxx3ArwICZ5I3jwoy8sEoZLgvwJewJ545GS2WEuomT820bZu1qg6b-8tSZ7h1CZ7yFZ8HOoNqXhhenaKinFMYxD_a9GjYgdaSRXBL8NdMexdzTy6IVi3PngAUbSQyDxwgY_Fj0cT0XNRJGd9m-91daRQF-jm-iM57ndPmymp0SFZ6vrIam4OCWT5-N8XxLFbWevOS2MaHe_lNuDk7f-HDBLcxd2qr8Ql94sBezGicDzhw7F29xBnD-8bHczB2jHSD6xNRg_uMCvaZokcoKGC9OsRZV2dYrzJ2uHTTw5IGvr3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منایع محلی از شنیده شدن صدای انفجار در آبهای خلیج فارس خبردادند
🔹
منبع این صداها هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/679829" target="_blank">📅 00:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679828">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_7xFaJRtkFjKVdn-eE3b7U-jpZVFG-9q7yHuK3p1m-LuyAJID6SaaS7ztQpKOiklepRe2l24Fbc4p1bbE1Rvg0r-2lI8C5w68TGVz61UfTEJWImPB2d-Tnlc4sS0mlF2p1tSSGl3gRlkCU5Pzoxb7kb2TJRksewAyJhYplVAVDa0rUiKuyrQv_S2doFYkDFNP_0i39cbn3qLxarjG2g9PK_hqEnIt_RJavvXsXZVjG4yWjUrW3wc4ljVPHqGx8Ono8BeBjgR0XMUB5iQCFCdbcfgxvHHh-ryvtpTjDpG9-jpAvJUS9ExKEApRl6QAO1FQK-bk0tEOTc0_S6GhuqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دوباره به پول ایران حمله کرد
🔹
دونالد ترامپ طبق معمول پست گذاشتن در شبکه اجتماعی خود را امشب هم آغاز کرده و در پستی به پول ملی ایران حمله کرده و مدعی شد:
«نتیجه
۵۱ سال رفتار بد! ایران هیچ پولی ندارد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/679828" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679827">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
برخی منایع محلی از شنیده شدن صدای انفجار در آبهای خلیج فارس خبردادند
🔹
منبع این صداها هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/679827" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679825">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
موشک‌های پاتریوت عربستان هم ته‌ کشید
خبرگزاری رویترز:
🔹
عربستان در ۳۸ روز نخست جنگ، حدود ۲۴۰۰ موشک رهگیر PAC-۳ شلیک کرده است؛ رقمی معادل تقریبا ۸۶ درصد از کل ذخایر این کشور معادل ۲۸۰۰ موشک که باعث شد تا آوریل گذشته، تنها ۴۰۰ موشک برای عربستان باقی بماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/679825" target="_blank">📅 00:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679824">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
اندیشکدۀ آمریکایی: قدرت سایبری ایران در مسیر تبدیل شدن به تنگۀ دوم
🔹
کارشناس سایبری مرکز مطالعات راهبردی و بین‌الملل در گزارشی تحلیلی نوشته ظرفیت‌های سایبری ایران به نحو چشمگیری ارتقا یافته و عملیات‌های موفق اطلاعاتی علیه مقامات ارشد امنیتی آمریکا و اسرائیل، گواه آن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/679824" target="_blank">📅 00:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e44b695b75.mp4?token=kacZ2vn1feS89UAklSWLYMhCNeEumv4Q3MRShDDJ8y9GPSGLgrk1ems59P2hy9VmaktwP4CqqjVrCdFEVa96GHgzQBmHLtvKLOxa8xbt4KLavkY9sRAvZO6Fa8PVcshmVaCcq1t-7V6Imt8kgM5WHVi1GF4a-qRKG4mbQB6OYuvPH5eCn65qSIKCSmb7rLrcuLfUPh5T5hemPWCBOc4GJxGO9C0hGU_R2kn6QoEgIhWa0lIUUeXJmTny9LF2FCUS1xLQWS-k-DPDH83UOmxjqoUOnvxDIIN38Z8YlbMKAfrOMeum7zxrvinbkFmJKQstJf-6Azk4dGHl3SvW35pVCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e44b695b75.mp4?token=kacZ2vn1feS89UAklSWLYMhCNeEumv4Q3MRShDDJ8y9GPSGLgrk1ems59P2hy9VmaktwP4CqqjVrCdFEVa96GHgzQBmHLtvKLOxa8xbt4KLavkY9sRAvZO6Fa8PVcshmVaCcq1t-7V6Imt8kgM5WHVi1GF4a-qRKG4mbQB6OYuvPH5eCn65qSIKCSmb7rLrcuLfUPh5T5hemPWCBOc4GJxGO9C0hGU_R2kn6QoEgIhWa0lIUUeXJmTny9LF2FCUS1xLQWS-k-DPDH83UOmxjqoUOnvxDIIN38Z8YlbMKAfrOMeum7zxrvinbkFmJKQstJf-6Azk4dGHl3SvW35pVCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رجزخوانی مهدی رسولی در خونخواهی رهبر شهید انقلاب
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/679822" target="_blank">📅 00:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpmUk7zx3tkW0oUQPrb4rfay1b3kJ4pwxUzZKjWkkcJDgfJjMYaL2c2LXhnuxZje7MfrdI49h7hh9gRrqS6Kt4JxhodYbRjZZAo2vykeO4oPXK8rNe6ROY_rqXdkpUt5-vJiMMnjf6FG75NtB3_pK7qFroJROkexaAnplso7k2xXbZbNYLUvayk5wA-0PZwZh-IJih3R3v_bwHY66TsTesVeRQFDl2QrVXO6EZnrLLHomvLImGYxZcTTFUDkKSIVL9QSz-gEdsfUEzr0Kc-iVj_81Y-g121C3Faosf5RB17AIKSdOBUgJWvoMKeD8Ii9ciaj6Qj7zcFRi251OFRfAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/679821" target="_blank">📅 00:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679820">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/140c7347c8.mp4?token=TMFVz6yNlD6MKkxGmmPrdI0FzrHv57PXvuBPjLwcDkOA6xyo3vcDiy5MfN-dzYzENKiIRCpeq6GOilfq8O-wb4_Coe2wQLWh-uw1s9Oa466m2oh1X6ry0JFn1ubAJcUMbwAyXDMGDe1Glw5QREuI9lDY9Ixhjphl0R1OGUe_WDH20kggblbXQN_2oeUpaXBRgrsMEIP46jXK3eLfvlQ78xykDCkaveL3rFMs9qtUsc2Qr4GQ71js9He24S3Bu38PlnsrSfeZNrPBH_6xgg9OXGEcxuplQjJzCKQxBFCZcf3Nsde61OGGM7xZLOeTf2HrejgcnFPIA6M6ECSHgRPdaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/140c7347c8.mp4?token=TMFVz6yNlD6MKkxGmmPrdI0FzrHv57PXvuBPjLwcDkOA6xyo3vcDiy5MfN-dzYzENKiIRCpeq6GOilfq8O-wb4_Coe2wQLWh-uw1s9Oa466m2oh1X6ry0JFn1ubAJcUMbwAyXDMGDe1Glw5QREuI9lDY9Ixhjphl0R1OGUe_WDH20kggblbXQN_2oeUpaXBRgrsMEIP46jXK3eLfvlQ78xykDCkaveL3rFMs9qtUsc2Qr4GQ71js9He24S3Bu38PlnsrSfeZNrPBH_6xgg9OXGEcxuplQjJzCKQxBFCZcf3Nsde61OGGM7xZLOeTf2HrejgcnFPIA6M6ECSHgRPdaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای نخستین بار | فرماندهی که در میدان مسئولیت و خانه، بار مسئولیت را عاشقانه بر دوش کشید
🔹
به یاد سپهبد شهید سید عبدالرحیم موسوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/679820" target="_blank">📅 23:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdm8vjTf51xmFSOeR3sBHD4gWy51rGFzpAQ6M452l-AY7rkh-wFSS919RMaDjWDYq5dpjfYMgPbmu4E-rIqvZpJh6fYLW4uvWtSAHYELIZUO8kSIRRClyrIhzBdeDRhZvNhnr5tzFJ4AjK0VNBnNbk-FG01ilTGc0e8NFgYeT8XCxeojfD6QpxfQnfPQeODvnGLcdJ2jsf8PLwCGiqIuokLMMLuoByayfR9Fdp2DS5FqVEEOT3kxS2iguAOOQ4EWVQffHPBwLeempayK3gf_12fFTVLfT7Fq_yelPoI903CWnOZUYz6YsPnHVirMTvzgFe6lHlJbdIRsmaTUPIuSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروژه‌های ناتمام در ایران
/خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/679819" target="_blank">📅 23:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679818">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gytxxFTngwD7D54RvtPa3kj5Ghg7rCcKh0Z-J5TQkkHvISJZ5rtEgBd-wkCYoCLrUOG_gFRjcmFWQ2YASVQAD7u8B_ftvdUYx7TvZS-2SThWjv8kRLTuhgAFlCVDCs4sNIQWRSg4znUCdcOKn--rAA9MlEcOjGWR3dDOPyN2P67X3YQg3Id7s7B9h2K7H-yL4XKKIah8loVwm145NSnKCeg2k7ufS9WXdM4Z3mSWcfIk0TMDMaXS4Rwh1DCG7v-kT_I9sNzcEetnxEsSYCMdT0TB6rWdx6OsUdZVjltDbdRGdEr-4q1tsjdhBADPZrnEBwwrUKNeQt-edhN1qLBCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین برآورد موسسات از قیمت جهانی طلا
@Titretejarat</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/679818" target="_blank">📅 23:47 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679817">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f416e4e6d6.mp4?token=l2Um50z-TaNw1qb0RWrWZT4lbNXwXV1L1RAZTuWb-phhdj7jG4Hw4YgBqgm_7E3du9FXGfY3gsfTf7ADdAPQWKugep7KDllnnVjVHxA5QQYB_v4hGrBuO0OwLPPZnTj-ByoKTPEy1i9PALSS0Um4npZrr1q8qWbfioCRdsHMhI-WuiK0tFDX-3Rh0DEb83NQO4lzLb_QtD_yqcp0DFRICZmF81XTK2BVZxMUdrYqtl85PawFUYYWP_UIa7hjEVtkyYnXETQGXEtsQBKsxISsu1gRx2cIPHm7rBfGc2CasgHkcT57-rHcBD78jGNc1w0CkAsytTfG3hsnWfms1cc2pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f416e4e6d6.mp4?token=l2Um50z-TaNw1qb0RWrWZT4lbNXwXV1L1RAZTuWb-phhdj7jG4Hw4YgBqgm_7E3du9FXGfY3gsfTf7ADdAPQWKugep7KDllnnVjVHxA5QQYB_v4hGrBuO0OwLPPZnTj-ByoKTPEy1i9PALSS0Um4npZrr1q8qWbfioCRdsHMhI-WuiK0tFDX-3Rh0DEb83NQO4lzLb_QtD_yqcp0DFRICZmF81XTK2BVZxMUdrYqtl85PawFUYYWP_UIa7hjEVtkyYnXETQGXEtsQBKsxISsu1gRx2cIPHm7rBfGc2CasgHkcT57-rHcBD78jGNc1w0CkAsytTfG3hsnWfms1cc2pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌‌های آخر الزمانی در کانادا؛ آسمان نارنجی بریتیش کلمبیا در پی آتش‌سوزی‌های جنگلی
🔹
با ادامه آتش‌سوزی‌های گسترده در غرب کانادا، ویدئوهای رویترز از نارنجی شدن آسمان یک روستا در استان بریتیش کلمبیا خبر می‌دهند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/679817" target="_blank">📅 23:39 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679816">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
اگر فرصت مرور همه خبرهای امروز را نداشته‌اید، جذاب‌ترین‌ها در دسترس شماست
🔹
🔹
سناریوی تازه درباره احتمال حمله آمریکا به کوه کلنگ
👇
khabarfoori.com/fa/tiny/news-3236499
🔹
جزئیات تازه از پرونده قتل یک مداح؛ پای یک زن در میان است!
👇
khabarfoori.com/fa/tiny/news-3236583
🔹
ادعاهای جدید محمدباقر خرازی درباره رهبری آیت الله سیدمجتبی خامنه ای و شهادت سید ابراهیم رئیسی + ویدئو
👇
khabarfoori.com/fa/tiny/news-3236624
🔹
جنجال جراحی زیبایی ۴۰ میلیارد تومانی خواننده زن | چهره او چه تغییری کرد؟
👇
khabarfoori.com/fa/tiny/news-3236501
🔹
سلاح های خطرناک ترکیه | آنکارا با این چند اقدام مرموز می خواهد قدرت اول منطقه شود
👇
khabarfoori.com/fa/tiny/news-3236597
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/679816" target="_blank">📅 23:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43fe88aaf.mp4?token=pPxtiXmGrsYoU9Z3i2x__PVBf300UShfD2OEisV6qysXPU0w_viG4F23aeo4aRDPb-CQusP0QTMKfaZuvG9yi7jFnQiAMMLqCEUSyQyv49VYjL8OraA8BTnbT-4GJEUOu0zmn_5J9kws3U9oH-o9EgdQXIFVRKgHwwVhJ8PkqkZYyNEZ5bHDmQB6tI2bhaPM76KzNXpkEM2_e6IdP-VPiG0ji-iCu_TunEDT0BM6U1XavnTFUXe3Z_3tAVxkHEZQxa8zRjp2OdBkgZ46_HcNj4ShWlt_mVs6aAXY-u1Ix08NeIGFsp2Bd9xjcLHhzKeIhhvtz7kG8NFnO-vGYxuFIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43fe88aaf.mp4?token=pPxtiXmGrsYoU9Z3i2x__PVBf300UShfD2OEisV6qysXPU0w_viG4F23aeo4aRDPb-CQusP0QTMKfaZuvG9yi7jFnQiAMMLqCEUSyQyv49VYjL8OraA8BTnbT-4GJEUOu0zmn_5J9kws3U9oH-o9EgdQXIFVRKgHwwVhJ8PkqkZYyNEZ5bHDmQB6tI2bhaPM76KzNXpkEM2_e6IdP-VPiG0ji-iCu_TunEDT0BM6U1XavnTFUXe3Z_3tAVxkHEZQxa8zRjp2OdBkgZ46_HcNj4ShWlt_mVs6aAXY-u1Ix08NeIGFsp2Bd9xjcLHhzKeIhhvtz7kG8NFnO-vGYxuFIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشاره‌ رئیس‌جمهور به فعالیت شبانه‌روزی وزیر‌خارجه با چاشنی شوخی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/679814" target="_blank">📅 23:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukSVwJac2Pmgs3preeG-vIK4HDHli5oXn4NF9OJtQDsYSn3o7zG9bHjtEf-57Ns4MS4bJfuqZUhPF-rCjGr4hZBgfUtnqghQmHy7FxS6Ss7G4e_sqiVTaPpokbiu6xLKesgN4gFWJjwSFuJZWjp64YZC37P8hdgmmTMW3Rp9R8E0Jsk9LqGYL46lsZfuq6_1zNVxHQARxeG06YrTdm1bUiYY6O94jItsVQAs-v-MAk12Co9PAtUin9k0Bepq9XCsGwNP31g5rH1Q9GUqANq_EYrBRpCGA1TEdJ3AAF3-FRdFJMcsgvILl-L6JzYTKqfW3jr3_sDfG9-x7QEjmVkFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448edf4631.mp4?token=rHpnRfMuyqXwEsA18QCu7esM4EWMWZmRvF2SUNvud4vVQ4ENAtlBe0GEiJVfwn1OzBJpP59K4QCVJCokqY2bZEC6LvX9TedJgXR0614FQrgngLMbTwfo_pB8LvmcVaPlGYjXyi38n1RP56NUwPPT5uKfzyMgmhRS6hFj9vYb3sb6cdkRbiBzYqSTrH3GfXvFCiFYoXkKvlMSgf6GdXOgeCCfc9C6HBpyld16vfmp3CzG2sX1Pqqfdcc6cB6NIHQ_JAz8fhOmEbd2IAvu5XVJPvFoRaBvS8tPFBWVbVQP1lA5gRxZenmCCvglq4wrt14clVtW2IoYDuUhkSpHGHC7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448edf4631.mp4?token=rHpnRfMuyqXwEsA18QCu7esM4EWMWZmRvF2SUNvud4vVQ4ENAtlBe0GEiJVfwn1OzBJpP59K4QCVJCokqY2bZEC6LvX9TedJgXR0614FQrgngLMbTwfo_pB8LvmcVaPlGYjXyi38n1RP56NUwPPT5uKfzyMgmhRS6hFj9vYb3sb6cdkRbiBzYqSTrH3GfXvFCiFYoXkKvlMSgf6GdXOgeCCfc9C6HBpyld16vfmp3CzG2sX1Pqqfdcc6cB6NIHQ_JAz8fhOmEbd2IAvu5XVJPvFoRaBvS8tPFBWVbVQP1lA5gRxZenmCCvglq4wrt14clVtW2IoYDuUhkSpHGHC7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توئیت سفارت ایران که آمار بازدیدکننده زیادی پیدا کرد
🔹
ترامپ رسماً از رئیس‌جمهور به اسب شخصی نتانیاهو ارتقا یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/679811" target="_blank">📅 23:12 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
