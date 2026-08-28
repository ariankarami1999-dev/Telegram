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
<img src="https://cdn4.telesco.pe/file/Lyd0c-CriHUXK2VkYFKWyH4p3wY1vPpPrCzXxrUg0FAyrq0mCX6tfHTAImzgXE-2FyviHljmKUhoN-ZsedfAzr6PD-cfbQEyXoMsIVYEh03ASEV9aNSdaT9Bmo_rP3BxlOjNP1YjIWkxSPgRSp9c_XndbLyyGWJEiCneMlqyRWn1o1bZbONK9vgdwqLJrNNAKaDHurS8P4XC-2RqRwJacfFTLUxGVdy6Ed166dhNpjlo5DfyzXLqMVCDx5fK46A5gM0WbwcYtaNVwFpgzgFURzytCZwpNQCpY-vkLeqW4tzktsM0v5msaLfNL6TtrRSM7gNHFXb-LDZk1AuT5d5iqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-685014">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4945fbdd07.mp4?token=EQLU6MkDBCrcI9_KQEmtlNy_lohMYpwS7Y3QYc6HSEvI6slLpJ4NzO8Df6EU1e6ybmXXbow0tqxRfc3wNiw9jDnUY01lsi_adWIXLdoDJ2vp6RY5KiephT8DQOo709aEg-rjzY-RAeo54yBy43jArhIl1yWwJZIxcmaVCIt8wTMkWbkU7F7xnLMwKLR2BJRmy01HMts3M-Sx_seBci2-ndFinhEg-xB8b8oFvN4hBXyw-3IEHDSdw6UCetKX55OU4iVCcL-PREQ3BqOywkCwIkymaL83_XX1R_vAVwyLBu7JImcDN2sSMCvVsfMLgt1YM6svTbU8z9zull0NPpmOaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4945fbdd07.mp4?token=EQLU6MkDBCrcI9_KQEmtlNy_lohMYpwS7Y3QYc6HSEvI6slLpJ4NzO8Df6EU1e6ybmXXbow0tqxRfc3wNiw9jDnUY01lsi_adWIXLdoDJ2vp6RY5KiephT8DQOo709aEg-rjzY-RAeo54yBy43jArhIl1yWwJZIxcmaVCIt8wTMkWbkU7F7xnLMwKLR2BJRmy01HMts3M-Sx_seBci2-ndFinhEg-xB8b8oFvN4hBXyw-3IEHDSdw6UCetKX55OU4iVCcL-PREQ3BqOywkCwIkymaL83_XX1R_vAVwyLBu7JImcDN2sSMCvVsfMLgt1YM6svTbU8z9zull0NPpmOaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استوری محسن نامجو از سخنان قدیمی خود: به مام وطن برگشته‌ام تا از آن دفاع کنم، سربازی هم رفته‌ام، کار با ژ۳ بلدم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/akhbarefori/685014" target="_blank">📅 17:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685013">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5116582c9.mp4?token=i6MPxJXHlGgpXYc_gacL_Dc1utkKcc7EXM24ehY6ycGhJ8hQ7e9_ghp61plNvpW4mhQT2r97acAS-T7RYZitp88LznMN0eAm_3q9RZ89J0F-tO_f1u5xXl_IpuAIHRLQBUlq714JZZEECS7qsH-yUIuaF046RnYJq28DwOGDObndPDSJRTM40twy1xhCCBvCWvvrW9azdI18tSuy3rOInEmZWFeRgugAdDgp9WbXQnua-q5AL-6gXKL1s9mNglhdxEmLNhgevLIQD_gABVgy4czIdhQ4zMJj7CWD1BI5OOc-P9UhYjrcuxTfWctppBfztc1SwAiCawmhnZkj45ZJyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5116582c9.mp4?token=i6MPxJXHlGgpXYc_gacL_Dc1utkKcc7EXM24ehY6ycGhJ8hQ7e9_ghp61plNvpW4mhQT2r97acAS-T7RYZitp88LznMN0eAm_3q9RZ89J0F-tO_f1u5xXl_IpuAIHRLQBUlq714JZZEECS7qsH-yUIuaF046RnYJq28DwOGDObndPDSJRTM40twy1xhCCBvCWvvrW9azdI18tSuy3rOInEmZWFeRgugAdDgp9WbXQnua-q5AL-6gXKL1s9mNglhdxEmLNhgevLIQD_gABVgy4czIdhQ4zMJj7CWD1BI5OOc-P9UhYjrcuxTfWctppBfztc1SwAiCawmhnZkj45ZJyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
می‌تونست اينطوری باشه...!!
#پای_كار_خاک_ايران
#امنیت_غذایی
#بانک_كشاورزی
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/685013" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685012">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی: دلیل حجم زیاد صف در پمپ بنزین‌ها و کمبود بنزین، در ترافیک ماندن ماشین‌های سوخت بر است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/685012" target="_blank">📅 16:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685011">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
هوش مصنوعی از کنترل خارج شد!
🔹
گزارش‌های جدید می‌گویند حدود ۱۲۰۰ ایجنت هوش مصنوعی که قرار بود جدا از هم فعالیت کنند، راهی برای ارتباط مخفیانه با یکدیگر پیدا کردند.
🔹
آن‌ها بیش از ۷۰ هزار پیام و فایل ردوبدل کردند و حدود ۷۰۰ ایجنت نیز در تلاش‌هایی برای حمله به زیرساخت‌های Hugging Face مشارکت داشتند.
🔹
حتی برخی از آن‌ها تلاش کردند فعالیت خود را از سیستم‌های نظارتی مخفی کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/685011" target="_blank">📅 16:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685010">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر کار: شیوه عرضه کالابرگ تغییر نمی‌کند.
🔹
ارتش رژیم صهیونیستی مدعی ترور دو فرمانده نظامی جنبش حماس و جهاد اسلامی شد.
🔹
شیخ نعیم قاسم دبیرکل حزب الله امشب سخنرانی می کند.
🔹
انصارالله یمن: عربستان در محاسبات خود تجدیدنظر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/685010" target="_blank">📅 16:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685009">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مدیر اکتشافات شرکت ملی نفت: هم‌اکنون یک چاه در منطقهٔ «دهنو» استان فارس در حال حفاری است و امیدواریم در این منطقه نیز به کشف جدیدی دست پیدا کنیم  #اخبار_فارس در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/685009" target="_blank">📅 16:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685008">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udPSIb3uiVltd1UPnU4dSbIimeixsKgTS70G70_jSWE098dlIeCRUH7n27ffrOP7QU1Pzh_k0HiqJ149dYKm4WDLlY3Slm493H945mN7GqBG6PhVo16bbnRdr373hdCSNpts_fGYCCsm5zGl8Gt7u16-UHey6rin1UQCeSur6DMjTvqmP9OecxWiergDSjTyvvxRdbWBImQf18Z63oQF7t4bhc1VP4OqaoO6T0lXZzDO1LPjdp1tPnym3LF6bBdA22EE7Ai1jQxy8rz3uw1vKtzGB1kxRj14WnbyMzJenRtw1i-jo3Ju82co1e0-5nYqeIpmNX5SKKDPN0gctpX1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست عجیب ترامپ؛ دیگر مرد مهربان نیستم!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/685008" target="_blank">📅 16:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685007">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
الجزیره: ترامپ در ۶ ماه جنگ ۳۱۹ پست درباره ایران منتشر کرد
الجزیره:
🔹
در شش ماهی که از آغاز حملات مشترک ایالات متحده و اسرائیل به ایران می‌گذرد، دونالد ترامپ، رئیس‌جمهور، حداقل ۳۱۹ پست در مورد این درگیری در تروث سوشال، پلتفرم رسانه اجتماعی خود، منتشر کرده است. این تقریباً معادل یک پست در هر ۱۴ ساعت است.
🔹
بین ۲۸ فوریه و ۲۵ آگوست، ترامپ حداقل ۴۱۸۹ بار در Truth Social پست گذاشت، به طور متوسط ​​۲۴ پست در روز از هر ۱۳ پست، یک پست به ایران اشاره کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/685007" target="_blank">📅 16:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685006">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
مدیرعامل شرکت اعتبارسنجی: از ۲۳ خرداد تا ۱۵ شهریور، اثر منفی چک‌های برگشتی و اقساط معوق تسهیلات در گزارش‌های اعتبارسنجی افراد ثبت نمی‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/685006" target="_blank">📅 16:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685005">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1d4bd99c.mp4?token=rVUhP11X7ZVqP3utdw4K_U8edFg7KPrx8nEXxTBsFta4yLOpINzBfKMETpVf8ZlDz_O9L9gCK7mr549GCsIS8CUBodJJn3a_n4SvjjBXnc62nH9ZavjYLL-ONya-N6G2yHuaythW5yUb6NOpeamT3Jg0IgYTr_bLkGxhOvN2KwS-L0JOTQZuB9CcHIslfs7P0W4PFK6a6HtKIvaebSgagGLAQxaN4L5gSxTinCoMUa8wHQXapGUClYIredWQyhAtHmSLgQqz1ItwiHBu2P1Srq2rWyYvyZfgYAHqg0AJXdmWmiiwkDh6_Wa7x9O1t1jUiw_RPi_itV6OpJG5Jl4x9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1d4bd99c.mp4?token=rVUhP11X7ZVqP3utdw4K_U8edFg7KPrx8nEXxTBsFta4yLOpINzBfKMETpVf8ZlDz_O9L9gCK7mr549GCsIS8CUBodJJn3a_n4SvjjBXnc62nH9ZavjYLL-ONya-N6G2yHuaythW5yUb6NOpeamT3Jg0IgYTr_bLkGxhOvN2KwS-L0JOTQZuB9CcHIslfs7P0W4PFK6a6HtKIvaebSgagGLAQxaN4L5gSxTinCoMUa8wHQXapGUClYIredWQyhAtHmSLgQqz1ItwiHBu2P1Srq2rWyYvyZfgYAHqg0AJXdmWmiiwkDh6_Wa7x9O1t1jUiw_RPi_itV6OpJG5Jl4x9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت چین در سال ۱۹۲۰ و ۲۰۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/685005" target="_blank">📅 16:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685004">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس کمیسیون امنیت ملی: آمریکا به همان اندازه که دشمن شیعه هست دشمن اهل تسنن نیز هست.
🔹
وال‌استریت ژورنال: هیچ نشانه‌ای از روز پیروزی که ترامپ برای ایران برنامه‌ریزی کرده، دیده نمی‌شود.
🔹
گزارش پارلمان انگلیس، افزایش تورم در پی تهاجم علیه ایران را تأیید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/685004" target="_blank">📅 16:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685003">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4560006fa9.mp4?token=Cy6dTwCucyLOEuPjDK_ND1AiPsaD7bKgnmxozLYv0rLEfMwD3_rK98Hr5aAf9F1FYblYfXp5jPTku-eLEe9yqwSnnfBUv2vcT7OLgc8zq7ureuBJaBC5ZDdLMhqTO0zjzK8Y2OA_FHlD8Ds1WOpDBfquEfSJ48oPfsqlgzqRjwLBesDzr0o_uSwsMeglHYviUm4r0jWkDZhiWn9LSQ1osIGeEyRdhCgrz8VUFXgkUsP5QV9PEYlNtc5H8tax4JqZQZ_U6M65UtpX0gBInijAcHVFVFtwJQAjgilyHHlUShDrVRHa3vJqwsgxaEqribNUeYJJG2EQP3-PrZyXGAoXfCJ2PX3bBNWnH9OVouGL7SWIMCGgIjWb6P9po8oAW0CsHkYMxyVr32BiPnm4wVU70J2i0qdHDYz6_h6y_VzzHM-SuwbUBzJQxGdSvHmqGFnj_QVWNylJl-JcJ7_ZnieZWsHV6d9BozUKHGpbUTtSqSuY7orrRpWbmP81IdoYoTazD4fCYBT_k33pyiw3L9Rtqde0HWEi-_1n3SpxX-iBdl3JoBVho0SnytUVJQ3pg8buvJtsTtRZogfYtTO_lxxtBGV8AtRqxKOSodswy0BJjNlk1wLv-2-z_Tf91A67mIjgR8iL28BPuxjwLWa8T6UA3iNUsSoHuTl9UbaqemOSsH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4560006fa9.mp4?token=Cy6dTwCucyLOEuPjDK_ND1AiPsaD7bKgnmxozLYv0rLEfMwD3_rK98Hr5aAf9F1FYblYfXp5jPTku-eLEe9yqwSnnfBUv2vcT7OLgc8zq7ureuBJaBC5ZDdLMhqTO0zjzK8Y2OA_FHlD8Ds1WOpDBfquEfSJ48oPfsqlgzqRjwLBesDzr0o_uSwsMeglHYviUm4r0jWkDZhiWn9LSQ1osIGeEyRdhCgrz8VUFXgkUsP5QV9PEYlNtc5H8tax4JqZQZ_U6M65UtpX0gBInijAcHVFVFtwJQAjgilyHHlUShDrVRHa3vJqwsgxaEqribNUeYJJG2EQP3-PrZyXGAoXfCJ2PX3bBNWnH9OVouGL7SWIMCGgIjWb6P9po8oAW0CsHkYMxyVr32BiPnm4wVU70J2i0qdHDYz6_h6y_VzzHM-SuwbUBzJQxGdSvHmqGFnj_QVWNylJl-JcJ7_ZnieZWsHV6d9BozUKHGpbUTtSqSuY7orrRpWbmP81IdoYoTazD4fCYBT_k33pyiw3L9Rtqde0HWEi-_1n3SpxX-iBdl3JoBVho0SnytUVJQ3pg8buvJtsTtRZogfYtTO_lxxtBGV8AtRqxKOSodswy0BJjNlk1wLv-2-z_Tf91A67mIjgR8iL28BPuxjwLWa8T6UA3iNUsSoHuTl9UbaqemOSsH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی در حال نزدیک شدن به فیلم‌های آخرالزمانی است!
🔹
توسعه و پیشرفت هوش مصنوعی حیرت‌انگیز شده است.
🔹
در این ویدئو خبرهایی‌هایی از این حوزه خواهید شنید که متعجب‌تان می‌کند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/685003" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684999">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZgL0w2VaSy_cKYLLSYhWx07jrQN30DM536aRauL_tOtP6SjD6-8fwdACnKdCoKAI3q0bq8s93_9qcKd_BUnPMZ0grQz1XfwyJxeBQhDdeStvLiEmwqux8GHiZesDP-mS9F6FDUCQfDzr1fNcLAyop5ZicITlkLP2Qt9XTVfLmlksXqNaT7KOvXKUo2s2tcFECSNtzLNQALTWAiemjCJ05CGaEDVQ-iI9ixQ-D3t6YQv6288CapyiZD0v_STJswzPh1Aonqj8Mvc1pQXoE-MMHbd5EjMhEFV3TSDhdl57W6VZl6JpJyWstWJB8M4KVoi5gnq78padrKtjxUnaM0rGIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NrrsF_AMtJlx9i3X6NK2rm0FZ118GLQz5famKKuWouSgGS7PLHmubXZhVfM5E420QOVNgESSYrPmUb0e37qiQnyMkICp4Vl56YprBqMu3806vXibE8bo_cVkMPhtgBcveZy0q7sgonLh2RGKQf3WKSr3jStQz4dIAO-cpkKZMj82S-B-gXMvzrtqQbVJwYu218pUY_VgUFcRBjYhSOaDwA2sz4Mw15i_cVymmxWioRAvkI2sXKGL3Gfo8nfX8Cw2Z6VDbBKgcXlczR-X6wJpGKVKlpgk93oslF9jYdCH4L6YMLc0M2I9tdZ9YuRPDw_U4cLomJdAYSZYSPgnKaxvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWwHby75DUA1_mE9gQ6KZy8rBqpmMEVKlGlv0eJBhUcIvN3IXdm63edM46F3i4SmrTswBUF-pKmQV3dtXsjji8amCzAjfWnDu05ifqUTjiNwiPuffrhuwSLkdMC3ZH5KTjGMRmPCE1NTZ83UdwpwEP4SDFEZFNuywu3OX-dEScSY98vaghhcjq5p2TaWTfaU1iubLlD2DaNYdgcbFXLNXufwqlTrV6C-I3-s5ZCfdHfdlV-tPOK09ZSH5RdXjHsNvjqSB_phk66Mi6vEBzHxd4mG4Fs1XVdAwrDS7ICQo1TdT3EG4IRnKf3TVVQlPP_jlsKhJQR8KrmF9Z0Vy3EKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdyH5w6g3OvymSlCtGXwd0s0XI6jgEv7R1hHEjefffmDrfvnjhCxwQGFhqmOe9n7qNzzaXLXwQ9E7IWlNty5asOwKIA3ssj4Ers6_7yZQEtnmrKKH79B7rxPO-rfZ8UUNA5g73Rva8vCKLULYX-atXC1ZQ8Se45m2YRWZq1e5Ws7joKJwP0FE9ii9_vnlUSAHghIXNtL0Z-WOHNgjt7cs8oatDZhG9txTuBBaNosCILRMMJ_i2jUyR9AoMWpph_GdTx_33amZ42kPA6003WL9eyCRmavNcKM4RN8vw9pGUE2H7yrr0lq0PNh3iEML-zskj_jB3XhhPMovAW-iadEGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بخشی از خیابان نشاط اصفهان فرو ریخت
/
حفره ۵ متری دهان باز کرد‌
مدیرکل مدیریت بحران اصفهان:
🔹
در پی شکستگی خط انتقال فاضلاب با لوله ۵۰۰ میلی‌متری و نشت فاضلاب، ظهر امروز حفره‌ای به عرض حدود ۴ متر، طول ۵ متر و عمق حدود ۵ متر در بخشی از خیابان نشاط ایجاد شد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/684999" target="_blank">📅 15:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd52e0ccf3.mp4?token=hulaSPsf8JtvbJzpTIzEzTGrydKMlL9F3ayqN-N77jOQjU_E6b_g_8Fk6qLofQ5EvhWfToHL6X8dz4sQRBfV3c38yCrH_dkBEsYwnJOy_dY3ZbD7QGcfTBEtu_hEmwrUhAOPU5q_KQfdW3P-iP2j7y9prdj7qIGf4haQ6ZzOQZOxSib0ObYbnVj2iTXXtxHQIvsHPeFoAwUSyUDJEeqersv9_77HkygX6zOxFbsHxbvS8WiHsS0B6pmYVdST3zFniP3r_cz9D3EqzRfRElrwC17W3e4zE0oulddqAK_Uqy_knm9inrYgc9zhOavC_YWYdA1NNzhbmEkwh9FD4ztzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd52e0ccf3.mp4?token=hulaSPsf8JtvbJzpTIzEzTGrydKMlL9F3ayqN-N77jOQjU_E6b_g_8Fk6qLofQ5EvhWfToHL6X8dz4sQRBfV3c38yCrH_dkBEsYwnJOy_dY3ZbD7QGcfTBEtu_hEmwrUhAOPU5q_KQfdW3P-iP2j7y9prdj7qIGf4haQ6ZzOQZOxSib0ObYbnVj2iTXXtxHQIvsHPeFoAwUSyUDJEeqersv9_77HkygX6zOxFbsHxbvS8WiHsS0B6pmYVdST3zFniP3r_cz9D3EqzRfRElrwC17W3e4zE0oulddqAK_Uqy_knm9inrYgc9zhOavC_YWYdA1NNzhbmEkwh9FD4ztzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت صدای جالب یک گورکن در پیاده‌روی صبحگاهی
🔹
فردی که هنگام پیاده‌روی با یک گورکن روبه‌رو شده بود، با تلفن همراهش از این حیوان و صدای متفاوتش فیلم گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/684998" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684995">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s0-5m9fY2D839M-JCGFaIAHEIUOZCRkeUcXixv0Ei_aMLs7HvEKW5gsrfwmMweczx4kzthsm90t3kMWhdUrrQDXXt6SUERq8Dv4WJxj0rgWjapstzkZSlHBE-JI34Kt3So5xMXb5NQtV45XC4pZwnTposaM8EKMMpJ9p0DMQdT6rj2STsEVPlJcCTWWG0EI2vwTHHn_WCMu1RCZhgOVq2UOFcRhu8sjMYf9vnsZllRDrSkbqA2gg5kn2ISu4WGvo8ZcBP9A8uvU5x42RTxT_vqiAzo06lJpT5qvFPen--Uu7pV6LDMlBBnLARmZcW25OlUd2VG5n-ZM6n7U_H8McEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNJDEh5GPIL31bp1S4saq4VGkNzM8IXrQGTxUjiffNF3lSA0_Dv-FHd_B5Zi4qRowF5Jx9TG3GIgq_ZYoSumH8kZnTkB2-NN4JZjNm7YYCDVqMwb4EnKZ0LiTwFtV-rzd507u8Z4m2Ha9mM1ha6qje0N0xqdOxnL-EXzIIJ-s5py_MJkD28naDXPtXxkIpuNkZ9W-PbeiaMN0kF5U2DRS57m7H6ShPhhgQChnsEJ8O9Ekemwa3zSwbE9nqbt1sbDOQtO3hiCubKQNCu1vDfFm3hoduUnLzBiMCSZYAwbqOdACXHpdhbl-F0fTCpTEuMpJwfSsC9ofJ_Rn59cV7fN-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8XYX2k77ucnwGgPyHTfO9rM56cekwB7dO06XgmhRm8aXjhiThUioR9XOOeFSH1x_I3dVE3K8EjzefuN2IhwEfbXlkAcRZWXofu4vUc35geJvRpSrI3A58XPTb1FrTUd-yndApttJhIwCaXZAiQJvXzsJdTYaiC5JJskTxknnRgMTonjz7Tyk1dIlVW-q_nelgbCk0EJ9vr_tLNJ713pHKlro7FH7HNU8iXOnGOaSP0phMmGxSNQIyor3HWruO0SN3UqAh3RUyrTZo-1Aiq4RCP9zpxZhKv5pZdN1hlUaG3xHI6qA2qkxnKhSHUwQKK3qr0naCQ_kZDBCjN1gjjR2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شکوه معماری ایرانی در خانه تاریخی اخوان کاشان
#ایران_زیبا
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/684995" target="_blank">📅 15:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
کلمبیا تبهکاران را روی آب زندانی می‌کند
🔹
دولت کلمبیا در حال بررسی طرحی است که بر اساس آن تبهکاران خطرناک در «زندانهای شناور» داخل کشتی‌هایی در دل اقیانوس نگهداری شوند.
🔹
دِ لا اسپریِیا، رئیس‌جمهور کلمبیا مدعی شده تبهکاران خطرناک در کلمبیا همچنان از درون سلول‌های خود شبکه‌های قاچاق مواد مخدر را هدایت و دستور ترور صادر می‌کنند؛ هدف از ایجاد «زندان‌های شناور»، قطع کامل ارتباط آنها با خشکی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/684994" target="_blank">📅 15:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684993">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
در ایران فقط ۱۷ سال طول خواهد کشید که جمعیت سالمند دوبرابر شود و ۹ سال بعد این جمعیت سه برابر خواهد شد
🔹
ایران با شتابی کم‌سابقه به سمت سالخوردگی جمعیت حرکت می‌کند.
🔹
بر اساس افلام مرکز پژوهش‌ها، جمعیت سالمندان ایران تنها طی ۱۷ سال دو برابر خواهد شد.
🔹
نکته نگران‌کننده‌تر اینکه ۹ سال پس از آن، این جمعیت سه برابر می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/684993" target="_blank">📅 15:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684991">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
از مدیریت پول تا کسب درآمد؛ راه‌های ساده برای بهتر چرخاندن زندگی
🔹
#چرخ_زندگی، کمپینی است که مسیر راه‌اندازی کسب‌وکارهای خانگی را از سرمایه اولیه و بسیار کم را تا تولید و توزیع و اولین درآمد را، ساده و کاربردی بررسی می‌کند. مطالب منتشر شده در راستای درآمدزایی…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/684991" target="_blank">📅 15:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684990">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند درصد بازنشستگان حداقل بگیرند؟
علی دهقان‌کیا، رئیس کانون بازنشستگان تأمین اجتماعی تهران در
#گفتگو
با خبرفوری:
🔹
نزدیک به ۶۰ درصد بازنشستگان حداقل‌بگیر و ۸ درصد نیز زیر حداقل‌بگیر هستند.
🔹
در حالی که سبد معیشت خانوار در پایان سال گذشته ۴۳ میلیون تومان بود و امسال با رشد حدود ۲ برابری مواجه شده، مستمری بازنشستگان فاصله زیادی با هزینه واقعی زندگی دارد.
🔹
برخی مزایای جانبی بازنشستگان از جمله حق مسکن، حق همسر یا حق اولاد افزایش پیدا نکرده و حتی حق همسر بازنشستگانی که همسرشان یا بیمه شده اصلی فوت کرده، به‌طور کامل قطع شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/684990" target="_blank">📅 15:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684989">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd634fbdb.mp4?token=aAZA7leUtWUPZwFHITt1G0LDtSmOP9YpIGr1nVgDAS0BcQpUsqIYWKzuO6YKn5H99ZoNskkiyL8NKWDDtCNfjvfN6MSngfwcCNPdJONudoQRXSRw_1SoZWVp3qJJalM9CdRAS_XEmjrhKIR--JMzY78qz7ijwwdeqotpCZ_lOgwKXCcVma3O5ouwDmqfvVGiCNkk8kzPNTSeEkGQRMey8Ps4YNSq7B0ExXIFmieJOQh_Apn2rfSVy34_ZU_SPJNRNri-I3gAQv8CSIiSF-Dqp9LyYxPhbHKSEhMlm8K8yB1bgerkH2mdAsVEHtViScvVLtrV21PizxxeFCrOuspjHINoQIyKCiSOzCOR9kDQ21i_pQmlZL-t8EDfA10qDWLDxqoah0Du8jBNVSqEe70IU_VdDuQIqMMikF7mKdgoZhoqIM2QJrY9S9Cd3GqljqPEm6w2P-S4qgPgrPjV295uGACs_9idktCu5MhS6TskViuqyR0s1OruCg0-TmXtv39Yeo5GOqJygindACFemuucg3SEk2Bymb7E56KOg-oV_JSMCddpbzH5o9z6uPStlMLxV6Zuoc9EOwkq4acjzuGKIdJCVXOLsk5_sUg7qz6LXc-3rBmtWRo2uSQnH5fqMALOGK2mf26VVFirUVgQjY_s7slDilHT5BkWoZJleiBJsjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd634fbdb.mp4?token=aAZA7leUtWUPZwFHITt1G0LDtSmOP9YpIGr1nVgDAS0BcQpUsqIYWKzuO6YKn5H99ZoNskkiyL8NKWDDtCNfjvfN6MSngfwcCNPdJONudoQRXSRw_1SoZWVp3qJJalM9CdRAS_XEmjrhKIR--JMzY78qz7ijwwdeqotpCZ_lOgwKXCcVma3O5ouwDmqfvVGiCNkk8kzPNTSeEkGQRMey8Ps4YNSq7B0ExXIFmieJOQh_Apn2rfSVy34_ZU_SPJNRNri-I3gAQv8CSIiSF-Dqp9LyYxPhbHKSEhMlm8K8yB1bgerkH2mdAsVEHtViScvVLtrV21PizxxeFCrOuspjHINoQIyKCiSOzCOR9kDQ21i_pQmlZL-t8EDfA10qDWLDxqoah0Du8jBNVSqEe70IU_VdDuQIqMMikF7mKdgoZhoqIM2QJrY9S9Cd3GqljqPEm6w2P-S4qgPgrPjV295uGACs_9idktCu5MhS6TskViuqyR0s1OruCg0-TmXtv39Yeo5GOqJygindACFemuucg3SEk2Bymb7E56KOg-oV_JSMCddpbzH5o9z6uPStlMLxV6Zuoc9EOwkq4acjzuGKIdJCVXOLsk5_sUg7qz6LXc-3rBmtWRo2uSQnH5fqMALOGK2mf26VVFirUVgQjY_s7slDilHT5BkWoZJleiBJsjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همزمان با سفر وزیر فرهنگ به یزد، تعدادی از معترضین در محل برگزاری سخنرانی وی با در دست داشتن دست‌نوشته‌هایی، شعارهایی در زمینه حجاب سر دادند و باعث مختل شدن جلسه شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/684989" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684988">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d42d338da.mp4?token=tisWL6Vu4WNF2S-AFBov0TJZtaKtWWkpVy8A16hBUcTIrUUO-HV0qGwUYttrSnAqTi485jFXz8-ZA1x1G8GyrGquRau8Geo0pixjIrubDTQMmNNQ5CwglRVRJkU6L11K7RWIWcpM5v4p4wjG5RuFvLAYj4pfid0CdeIF4rXMfDU9Rexx_Se6-PZ6fa_m43XURrX9c4OgtOBgwSoDBzzVHaGStB8ljfOV5i0frgUNEBcdbupXWff34TViESCm3baMo4ceTRDwQElwbmdXYOkstCR4FIe6tb2Z4IAKFJeRLAshLRt2RXM6TkAGsZI-WGsCKJeFn8oFf-Ej4KjjrAwunA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d42d338da.mp4?token=tisWL6Vu4WNF2S-AFBov0TJZtaKtWWkpVy8A16hBUcTIrUUO-HV0qGwUYttrSnAqTi485jFXz8-ZA1x1G8GyrGquRau8Geo0pixjIrubDTQMmNNQ5CwglRVRJkU6L11K7RWIWcpM5v4p4wjG5RuFvLAYj4pfid0CdeIF4rXMfDU9Rexx_Se6-PZ6fa_m43XURrX9c4OgtOBgwSoDBzzVHaGStB8ljfOV5i0frgUNEBcdbupXWff34TViESCm3baMo4ceTRDwQElwbmdXYOkstCR4FIe6tb2Z4IAKFJeRLAshLRt2RXM6TkAGsZI-WGsCKJeFn8oFf-Ej4KjjrAwunA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کریس رایت وزیر انرژی آمریکا: اگه ایران هم مثل عربستان به ما باج بدهد مشکلی با آن‌ها نداریم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/684988" target="_blank">📅 15:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684987">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atncSLsb9Hjao83pnzvHBoG2Qy8m0cquvhVWHSBBirm6Gm00M3f7lqHqFCX7lB5sOhpivJGjLaZpOjm7-e8j0hpP8FMvqtuntlR8ZLFx66rV0-IiP4EIjBJ7c1Xg68XmlTIRg9MvTZ7dvbdaAw6WCK6OQ1ybjh97XNDwjSAgE5Lk8WlLcB6C2YeKlPBLZ3zLtR8dP4s1swMI5w4gjoKzoDlW_eOVqtaTT1YdsZlgqxupzjBqTxHCd9kF66rTyC85e-WnTpzp4EwZJfcjlXKIz40VcSC2Zz9kDHtrPqs4ZOniv--YXWYFrw4JeSxLpgmaX81i81ADqTrwiNTIyyg5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران؛ محور پنهان مأموریت رئیس سیا در مسکو | روایتی تازه از یک سفر جنجالی | ماجرا فقط ناتو نبود
🔹
سفر محرمانه جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، به مسکو در حالی خبرساز شده که روایت‌های متفاوتی درباره هدف اصلی این مأموریت منتشر شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241040</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/684987" target="_blank">📅 15:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684986">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0fcbfc59.mp4?token=E3ENbtbeQd2weWoatc3MxvsF3tq-DI9H_xgPrGQ1N01Wxb7ZZMrCf8WtQljkLMhgZT_TOT0YoFn0Q0b4sYPjdD8jhhXgw3Es1DQ_OZ3fOF-7ijFveIJui18IqP6_JPR3Fg9zbWgMJ35a8CldDBIEMxO5nenNuZE5U_wFPu2P-iTfDij1SK6SeowafZ5G9-p19DsCz73RraxrdIK1haoO101jyxtXXPvNVSSr0mhkszGiRG_TQy4sjVv_2TE7WF3heykQn3TaLohLeEu_itmay9U_7bmnRZ3MpnQ0CkrL9jSgKPCv_3Lw1qykqqFvi9Vd4FG5cUHeFzoSPR3Mq36Q5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0fcbfc59.mp4?token=E3ENbtbeQd2weWoatc3MxvsF3tq-DI9H_xgPrGQ1N01Wxb7ZZMrCf8WtQljkLMhgZT_TOT0YoFn0Q0b4sYPjdD8jhhXgw3Es1DQ_OZ3fOF-7ijFveIJui18IqP6_JPR3Fg9zbWgMJ35a8CldDBIEMxO5nenNuZE5U_wFPu2P-iTfDij1SK6SeowafZ5G9-p19DsCz73RraxrdIK1haoO101jyxtXXPvNVSSr0mhkszGiRG_TQy4sjVv_2TE7WF3heykQn3TaLohLeEu_itmay9U_7bmnRZ3MpnQ0CkrL9jSgKPCv_3Lw1qykqqFvi9Vd4FG5cUHeFzoSPR3Mq36Q5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از این زاویه به زمین شالیزار نگاه کرده بودید؟
🔹
میان عطر برنج و آواز آب، شمال ایران قصه‌ای سبز برای دیدن دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/684986" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684985">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gdv3Cinlr2XlJEEc3WwrdZoux3566CZ-5E6CYe5j9QDC_aP3BCaxXnhLfT63_gOwy3OVyGgA1qYxSD0dwuJUZR5gTBf_DbhNVcN-uXe37s-070gS1zgyh2lkrsnFXcT70_rgqBJ0iQoeENUhxhoDmTtQ3DmdNTUPHSeCxnK_CfGhD_syGDecwNOLKh3aT2xriJnPWqeEe-W1-YEl8VC9Rhi-iAVQA7pF1mda94oQx8KHrFdClPtESCZp4UhNcVVXqGnCyBNqy6nIPYGmHIeCCwKUFVAfbRyjV04WIGofoJXS43ISdtmBjBSzEC_TU8ATjinQrwWgIdfVQfi1T9FcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: تجارت ایران در امارات برخلاف تهدیدهای آمریکا ادامه دارد
وال‌استریت‌ژورنال:
🔹
گشتی در دبی نشان می‌دهد هیچ نشانه‌ای از «روز موعود» ترامپ برای ایران وجود ندارد.
🔹
فعالیت تجاری و بانکی ایران علیرغم هشدارهای امریکا و اعلام پایان روابط، آشکارا ادامه دارد.
🔹
فعالیت تجاری ایران ریشه‌های عمیق و متقابلاً سودآوری در پایتخت تجاری امارات متحده عربی دارد و علی‌رغم هشدارهای آمریکا همچنان به رشد خود ادامه می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/684985" target="_blank">📅 15:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684984">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7bc4e80a5.mp4?token=iYWDRo8qzq2609-R-0aA1fAimLhKZ_oRW1x4fFeZGERnfNLVVx_4VKdeLIIzOJmoh-peAih-_WKEfi0U8gilsli0iJj54jrDk2NUBjui61F7WRK-EcAxlHU0-wjHHd4gSlt_FOcxBFx9D2KfgANSlofCm88gu-4yyajBZMkXoAYQ82je0qYsMKUOCV5l_ykRjaCkyMaiXaBQMqlM0fsT9slIOrt3MjljREskswHl6wlSTbKmlEdycfN5QaWHrxll7aLlnbQAGDr_mNkHEjaezfA3s34p-9mthizyCZeMTfcd0QLvxeNNxj7ZQ294ktaY5DAQ5K8YjD3f098dSeDsHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7bc4e80a5.mp4?token=iYWDRo8qzq2609-R-0aA1fAimLhKZ_oRW1x4fFeZGERnfNLVVx_4VKdeLIIzOJmoh-peAih-_WKEfi0U8gilsli0iJj54jrDk2NUBjui61F7WRK-EcAxlHU0-wjHHd4gSlt_FOcxBFx9D2KfgANSlofCm88gu-4yyajBZMkXoAYQ82je0qYsMKUOCV5l_ykRjaCkyMaiXaBQMqlM0fsT9slIOrt3MjljREskswHl6wlSTbKmlEdycfN5QaWHrxll7aLlnbQAGDr_mNkHEjaezfA3s34p-9mthizyCZeMTfcd0QLvxeNNxj7ZQ294ktaY5DAQ5K8YjD3f098dSeDsHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ویدئوها از ورود محسن نامجو به فرودگاه تهران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/684984" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjgqmAvxzh623jWNEA038hWKn8AZgY_dwYVc_SwrLW9674JSHlzcCB0FIHfS0zAb7GUpJj4P16cTTOcLaUCa1Ax20dzptacu9D6cSeMzVEomp8HoKAGrnTsWES0m6kpu8B1PeWx13bT5u6qYVjMs9EtGbx7bRwITF54NLYL6XlgZ5hZyxl194gJI4IKpaFfX3he4tyst-0C-339Zi1UiGJ8z8CRGM7Ke8sJ2pUwAmVklMH4tghcdk6jw0nJzX6411AYXF72gGJGOWbxOQrWRIfU1W1espexaYyfByoIKgVs5uL3Y1xm7noVrKVba7e-ix6Y0-WEjnfzTchbKdQ5h6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjHxZeSP-S5_CorYHN3zFcKo-wcspQcjfw3aBLAvrhAdGqVwlZXWf7bKMeG5yHZbewIX-w--H2dA92nn1ETbikqgPq0bU0IF6az3WzotXLgbMherLzr51uRASnaOmqmlFbJLtqtPlz043_G0wWa_zIFO3_TZgK8IkU3Ea1J8O_qTp_pckgrjOV6MpVbFAImc2d6eMJdD71WD-P2hSzTMZUk8SSdM1U-ZeDtqwrLUA2wVMPYlPHCEA58P3Occ48B756DT9w8VLz-JK5v-mzE8Fytwxwl4PvGHkksAO3lcrVRm9JYikLUuGm_nzLx0IN9t1e4Z47lmGnAOmfPzJGXZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO_lm1GnD5Vp8s22jsI2wuNIgti42V_yLmHPJ8i_GyZazhb7TWfSHThWkUyliJyI60AAsGqZaOLa6QxFt5dvjfLJza6HE1lBrSnTcIMGarWy98wEoMm7Zz29DBVUXzEBYboA_lShjn3PEyuKGjCsN2Ry8R6uGlLTfZbEC3Lu4pxv3ox-aZsoNgo5uy1OYXYILqSDAtt9ji2iufZI8ENI4lWUKMGJ_kd60ivmMLwSyK9l0ae0rIS4QBgiT6YlrFYMmeVeQoj9zAvz6yjI6dydV1Nf48YVzuxrWi56KE8d9yft5LMLwjzkw_vIxvanf_YIqoVvj3p-VtEoq99eXrPNPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-NC0KuaMkypiBnZWYwaDVvAcgKD5RZYCj3wQBO-19y0Xrjb0QuA1UfkTHrCdwWmhh3az7_s6brMeRzNcNUM1lnaQSwpSxlqQ64QB5ji4TwuUNlKwWvg-1xHTgAzgejmy4Ssv_SdWEdLM_LPVJvmmOOkCy1XSBfWDfwKjwLegcWwV9Vt2DXh7SPGmwkVg0YRH-IR_w7zfnXDC_rn9E_DDK8rDwCiOVnqxu3Rwdg3zyVvzSK46vA-IISsRwiTfiT7hoF5sIsWeVnU2bWPsMMSDmphRDUcN-VIHly7m7wLjY4RDUQGT8EaKbvJrnihC8R1pdzs3HVdwah7iSTICGak3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckFTRVL7ccR5diOUa7WMoXDjH9xTF1bVAYi-IgGMrsQv_89Nj5-tH57OO1cfrnFR8br4W3_AQXhuSe9aGJAmXJDIKsBz6Y6Sgj3CnTRBX73MjNTckAWjrbtbR53tOeCTUekjyKq_y3slG-PdAmaxYFpb8rTNoPbE_kQfLvWaF9Z_6kigwXYS5G4JDXw9UGeKPlVjNpQqDdKv41xSpT3P72OwVEgPXK0dGyNETbfQwmfqosQm1FtDBnS5j50C8mRTv1n4xZdTcjXLps3JyKPoM43BhElZ1OBc-qMIMyA9tMMwsZ2fW5vH4CQdPWblSnU8WPP8KHASTLqD1dfMIS_i1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرزندآوری از نگاه افکار عمومی
🔹
پیمایش‌های مرکز پژوهش‌های مجلس درباره نگرش جامعه ایران به فرزندآوری نشان می‌دهد تعداد فرزندان مطلوب خانواده‌ها  ۳.۲ است ولی تعداد واقعی فرزندان روی عدد ۱.۷ قرار دارد.
🔹
بر اساس این داده‌ها، ۵۷ درصد مردم «حمایت اقتصادی» را با اهمیت‌ترین شاخص فرزندآوری می‌دانند و نمره ارزیابی عملکرد دولت در این حوزه تنها ۳۶.۴۱ از ۱۰۰ است.
🔹
همچنین با افزایش سطح تحصیلات و انتقال از روستا به مراکز استان‌ها، میزان اهمیت‌دهی به شاخص‌های باروری، حمایت اقتصادی و فرزندپروری کاهش یافته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/684979" target="_blank">📅 15:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60fc56c06.mp4?token=FipdZZzPvzlJW0Ai2XAeQ8Rby_7YDnbcs2ebpHEEdzZPNR3AiX_UOBLPxGuv02R1VLg6O3ppjIfu_pZQdhc72mrMi3lelKVS9MiQaNmcVUsi6_HEAJxWMLjsktjTFp74enSp2EgVsWjBW3hE8v4u4pPjXTyEW5-CoRgT8Ec-1l5hegXGomtvN9rj-IPB4pawdVwuICsK1GuWWyGIwNmVtyZP5Trd27ZbgmEvGI1eFStoqYe2wZldzJVscM-xC80IYQ6bakLnBWmvRFp9MzNMcQLwH8qftWmF2pQFtXjB86DGcPQehdMsSYiu9q2AuOWDFFh5GMD_77W1XSJt8jig2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60fc56c06.mp4?token=FipdZZzPvzlJW0Ai2XAeQ8Rby_7YDnbcs2ebpHEEdzZPNR3AiX_UOBLPxGuv02R1VLg6O3ppjIfu_pZQdhc72mrMi3lelKVS9MiQaNmcVUsi6_HEAJxWMLjsktjTFp74enSp2EgVsWjBW3hE8v4u4pPjXTyEW5-CoRgT8Ec-1l5hegXGomtvN9rj-IPB4pawdVwuICsK1GuWWyGIwNmVtyZP5Trd27ZbgmEvGI1eFStoqYe2wZldzJVscM-xC80IYQ6bakLnBWmvRFp9MzNMcQLwH8qftWmF2pQFtXjB86DGcPQehdMsSYiu9q2AuOWDFFh5GMD_77W1XSJt8jig2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: غزه را ترک نمی‌کنیم؛ بازسازی تا خلع سلاح حماس متوقف خواهد بود
بنیامین نتانیاهو کودک‌کش:
🔹
اسرائیل غزه را ترک نخواهد کرد و تا زمانی که حماس از بین نرود و این منطقه «غیرنظامی» نشود، بازسازی غزه انجام نخواهد شد.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/684978" target="_blank">📅 15:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krKqFYp0n0fbnEeZmTGAW80C2IdQi9IagR5HLeJkCbh32_zU-PkfAJsnbDG5fctGBFxyEOWLunuZMErNHSNZmv_WXyHfS8flo-YO5IKxc8Oa08-M8U0ToH9UXXEthwtw-9R3ZasQiaZNV1wz_H_Zt53rpM5J-sVO7BD372BxAdXXJP_KcStf8TU2buhZX6vCdPRYC19WieOTGZ2rfm4WMccLqvd54m2PnixNQIrfiCCK5NwG6c0yuoL-7WrGGSTrh5_2Fg08sio0hJicjBspTB1MqSzcmUiZ5bR120qFVWGPQ8N5JB3LNDqbVFAh7HLE-el54opgzruKzK5S6cG0CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرگ پادشاه‌ ۳۴ ساله اوگاندایی که در ۳ سالگی به سلطنت رسید
🔹
نخست‌وزیر اوگاندا امروز جمعه اعلام کرد که اویو نیمبا، پادشاه منطقه توروی این کشور که در سال ۱۹۹۵ با تاج‌گذاری خود به جوان‌ترین پادشاه حاکم در جهان تبدیل شد، در سن ۳۴ سالگی درگذشت./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/684977" target="_blank">📅 14:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/880c169133.mp4?token=EIkp3f-YT99Tg8V33xtCubPI9vGIM4gQKcq9KlCNzXX3gD53R8p3UBppz1Sj9Yxfcolb0lDmMo52aflK_gcNX80SBplc3aadiqDm0aw_GlljkAI44aq8GyS6QRhTOzqbk8FWxJLUYkKEM3ZfQIFXgcJR-yiHnFfIXRrZgQnW3CQCzPNkjDU7ZzP9MqowUhLABexUgL0kAbDPUMBC6pZHJyMjsvaPetL8WfYw-zC0aQyobenmfrhTbdPz2u7xHWbAUFpnqmCdgL4IHpajpdWB0b9WNdq5Nx8n-y8vv7UxhFJlxksrAej72nr-NuyLYW9FDJXBqALFQ5ninObMLuvlOa_6FoFY52OGdOwSBmKjlhtyGhtF0ecRZiu7FSeGu-AWkBmVR6Jq690PDrjNGQqwyUd6sulCnVjp8ZTuOJgsos5ziahGddqDiYKagunFd2v1pmHOGU7dP9s2InQG4qRN0q12uDhLdWjp5pJUwzubsRqhidkh3KobGBHax28X0N7hXXNg4DrkqssNEEjDH127S_CJHPxP96QYDfHi5zNIda0d5y6-OD2ybpxWihjajdAW00RaTIPfiJQL0GyARqp9vh5P2T70yTSu2zJjq-b4Tb1hYXrXErCkai-3vxkzWrJaZF_IoX6B5AWVFL2P-YGfofc3AQy56QI6NfbfogE8K-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/880c169133.mp4?token=EIkp3f-YT99Tg8V33xtCubPI9vGIM4gQKcq9KlCNzXX3gD53R8p3UBppz1Sj9Yxfcolb0lDmMo52aflK_gcNX80SBplc3aadiqDm0aw_GlljkAI44aq8GyS6QRhTOzqbk8FWxJLUYkKEM3ZfQIFXgcJR-yiHnFfIXRrZgQnW3CQCzPNkjDU7ZzP9MqowUhLABexUgL0kAbDPUMBC6pZHJyMjsvaPetL8WfYw-zC0aQyobenmfrhTbdPz2u7xHWbAUFpnqmCdgL4IHpajpdWB0b9WNdq5Nx8n-y8vv7UxhFJlxksrAej72nr-NuyLYW9FDJXBqALFQ5ninObMLuvlOa_6FoFY52OGdOwSBmKjlhtyGhtF0ecRZiu7FSeGu-AWkBmVR6Jq690PDrjNGQqwyUd6sulCnVjp8ZTuOJgsos5ziahGddqDiYKagunFd2v1pmHOGU7dP9s2InQG4qRN0q12uDhLdWjp5pJUwzubsRqhidkh3KobGBHax28X0N7hXXNg4DrkqssNEEjDH127S_CJHPxP96QYDfHi5zNIda0d5y6-OD2ybpxWihjajdAW00RaTIPfiJQL0GyARqp9vh5P2T70yTSu2zJjq-b4Tb1hYXrXErCkai-3vxkzWrJaZF_IoX6B5AWVFL2P-YGfofc3AQy56QI6NfbfogE8K-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تگرگ شدید در فرانسه شیشه خودروها را خرد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/684976" target="_blank">📅 14:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مردم هزینه تصمیم‌های جزیره‌ای را می‌پردازند/ طرح‌ها و لوایح بدون پیوست اجتماعی تصویب می‌شوند
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
این اشکال به نظام حکمرانی ما وارد است که در تصمیم‌گیری‌ها هیچوقت پیوست‌های فرهنگی و اجتماعی نداریم.
🔹
وقتی دولت لایحه‌ای می‌آورد یا اگر در مجلس طرحی تهیه می‌شود، هیچ‌کس درباره آثار آن نه حرفی می‌زند و نه سندی ارائه می‌کند.
🔹
دولت ناگزیر است بخش جنگ و دفاع را حمایت کند که طبیعتاً هزینه‌هایی دارد که با توجه به منابع درآمدی دولت و محدودیت‌هایی که بعضاً در جامعه جهانی ایجاد می‌شود، کمی کار را (برای حل مشکلات معیشتی مردم) سخت می‌کند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/684975" target="_blank">📅 14:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9e816e02.mp4?token=qjAjJpwTwryEzU0iEn2cfWskWjGPk9OZDar3s_Lt12jHJJe94udeOOGVJ5-axLbueU79wYJsGgHmorIJ2dUekdMFks9B3NWS0VnFDkfpdMmoyt1PAKdEJXrU4XZHbhQZymC7lQUSTdhEaeCW6lAVoyxz4QgaDz1vlo4XQSUl_cELUv4mWgzz6I1er37__OhX5KdnkyygkJtT-glZ8bxS97qhpY1GC-cCwFL0wPBqgWBOzhThHq27Zi6doKvqKOKVpHTzgFPN46d6J17S2Nn9CvVZZ8U1bk5lBIpw9iDi2Uc3jgW5Khsul02OxgApDMROGBl4iHLkJx-GFWlQxdY38w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9e816e02.mp4?token=qjAjJpwTwryEzU0iEn2cfWskWjGPk9OZDar3s_Lt12jHJJe94udeOOGVJ5-axLbueU79wYJsGgHmorIJ2dUekdMFks9B3NWS0VnFDkfpdMmoyt1PAKdEJXrU4XZHbhQZymC7lQUSTdhEaeCW6lAVoyxz4QgaDz1vlo4XQSUl_cELUv4mWgzz6I1er37__OhX5KdnkyygkJtT-glZ8bxS97qhpY1GC-cCwFL0wPBqgWBOzhThHq27Zi6doKvqKOKVpHTzgFPN46d6J17S2Nn9CvVZZ8U1bk5lBIpw9iDi2Uc3jgW5Khsul02OxgApDMROGBl4iHLkJx-GFWlQxdY38w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسپی ماست و خیار به سبک خارجی
☺️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/684974" target="_blank">📅 14:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2a2Rk62q-n2OPI5JBlAhtW2CqdIJJrKSStWZVAhvMYsPjw0q__x4Ks4cYrJLx3c4s9Bo9VwX1I6tkzL4po5iYrTGq0XK-cmHKwAne_sPPN9Aq-McrwVIiRAlRH8bJXZE7uQr7upvZ_MQwT02OJfb08RFoe-Bzc7Um9ont6vSL-NwXbkK3UgNR8JEcGYPUqFIhYIakLsHoqyB2S0Y98F1KGMfNwbjH9BVqjsjspTcuoZ5xxAlpWTqOygOe4w4JOd_A17iTjeeA-HwtOF0iO9J8UK5Ey3oLsLHcMlmiY_SN9HNswxCpganmESsLY8zFgFlkbH-xKCmgHWxWbNITCMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکسیوس: متا ۳۱ پیج ایرانی را در اینستاگرام بست
اکسیوس:
🔹
متا شبکه‌ای از حساب‌های فیس‌بوک و اینستاگرام مرتبط با یک عملیات مستقر در ایران را که از هوش مصنوعی برای هدف قرار دادن مخاطبان آمریکایی با پست‌هایی درباره سیاست آمریکا استفاده می‌کرد، حذف کرد.
🔹
متا اعلام کرد که چهار حساب فیس‌بوک و ۳۱ حساب اینستاگرام مرتبط با بازیگران مستقر در ایران را مختل کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/684973" target="_blank">📅 14:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638a6c932.mp4?token=pm9g-N0vbSqByeQXa5aB34BpIUkikkNk1Zw3ak1n5XVmcMcXmLNK2txyA4cvSuA6oQUL2ky3Y6eNYs75jq_RxFpW8SmrUM3d6fxg4nAYDuqWPdNHmsSJBJaPQyGo4KFDvy6y0TV1Kn5a3UXx7PHOoQCkHAaq_7muFrfGjUbo5FC16aopjzuYHfbQuWWd5P3s4atyn2HuRDXGvNYZsW7D-Wadt_pu6DgaG0xfz1ie64-imsmGo2TbTwuY5S1v120tlRSNJmyKvVF8JVK6VKMczypBsiUuuyBgeYadTzqRdzVR9AZcvajAIL753AJ1v85n5lHwKB94DrUSOViPbT91_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638a6c932.mp4?token=pm9g-N0vbSqByeQXa5aB34BpIUkikkNk1Zw3ak1n5XVmcMcXmLNK2txyA4cvSuA6oQUL2ky3Y6eNYs75jq_RxFpW8SmrUM3d6fxg4nAYDuqWPdNHmsSJBJaPQyGo4KFDvy6y0TV1Kn5a3UXx7PHOoQCkHAaq_7muFrfGjUbo5FC16aopjzuYHfbQuWWd5P3s4atyn2HuRDXGvNYZsW7D-Wadt_pu6DgaG0xfz1ie64-imsmGo2TbTwuY5S1v120tlRSNJmyKvVF8JVK6VKMczypBsiUuuyBgeYadTzqRdzVR9AZcvajAIL753AJ1v85n5lHwKB94DrUSOViPbT91_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میرشایمر: آمریکا دیگر برگ برنده نظامی در برابر ایران ندارد
پروفسور جان میرشایمر با اشاره به ناکامی آمریکا در استفاده از عملیات هوایی گسترده و تحریم‌ها علیه ایران:
🔹
«ایرانی‌ها همچنان سرپا هستند.»
🔹
ما دیگر هیچ برگ برنده نظامی نداریم؛ بلکه خود ایرانی‌ها برگ برنده نظامی را در دست دارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/684972" target="_blank">📅 14:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684971">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر صمت: درحال کار روی موتورهای جدید هستیم که خودروها بنزین کمتری مصرف کنند.
🔹
وزارت تعاون: میوه و سبزی از کالابرگ حذف نشده است.
🔹
وزارت خارجه چین: با تحریم‌های یکجانبه مخالفیم.
🔹
سخنگوی کرملین: پوتین فعلاً برنامه‌ای برای گفت‌و‌گو با ترامپ ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684971" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f74326fca.mp4?token=YXjQhoBtzJpp_F2P9yEYE-IN2d_AH_EiF8RUj6xrPGxA17n5VgZzykQvtLRmlHUtDhqccadnhv-Tndg8w26tpLvTq08Vv9UyWSrFp6xbcMxaW0L7rbfNFX4FSIs0j2Ficubg14K9l1cmoHTo-15PbuxDtKEDXg4g32fboNeu-I8yBodiMVA_9eqJVOS3vrKWAic8UvWGovYTRXrR4IfrsciAwK4sp1g3kbThoNdebKqR-a3jrmxkept8BBLjcbgoNjq90RUJNbAiznn1SBdpxGvLKrX7zq9w9dNxkQPRWDC-MeWSPDIDqKbUauC9AhtevNBrNAm9IzCkBeEiyAgDRhTK7J9ERzyWZmVdSLJj2zF31iU6ZAojex3Y5wlm4FwSSoYX1RTdOOjK8LhJGWjUyAsonn8LcSj_RDHJt-EpAmL2PeTmkeIflKzVFqbqVI1iZrKqe1Is_u8shDidPZ95sxFW7XaTwQZtQ6SmzcPTHOaUrwgXOlIRWDSQxHTJzPsGf31HTLAWeVOIw07YAvWg5nqfrvgPfDzabL_zHpkY02oWIKkPkdQIk5BC578j4jfn-7D1fS2nsQE-iv82d9s_wJ703CofHOQk5DXZVTq0e9qda2-OFi8dmmoD0Tk0H_vm2g1thm3N2l9CbaLLjsJFVJWrMkBqfSVYqTKtod0M0Ds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f74326fca.mp4?token=YXjQhoBtzJpp_F2P9yEYE-IN2d_AH_EiF8RUj6xrPGxA17n5VgZzykQvtLRmlHUtDhqccadnhv-Tndg8w26tpLvTq08Vv9UyWSrFp6xbcMxaW0L7rbfNFX4FSIs0j2Ficubg14K9l1cmoHTo-15PbuxDtKEDXg4g32fboNeu-I8yBodiMVA_9eqJVOS3vrKWAic8UvWGovYTRXrR4IfrsciAwK4sp1g3kbThoNdebKqR-a3jrmxkept8BBLjcbgoNjq90RUJNbAiznn1SBdpxGvLKrX7zq9w9dNxkQPRWDC-MeWSPDIDqKbUauC9AhtevNBrNAm9IzCkBeEiyAgDRhTK7J9ERzyWZmVdSLJj2zF31iU6ZAojex3Y5wlm4FwSSoYX1RTdOOjK8LhJGWjUyAsonn8LcSj_RDHJt-EpAmL2PeTmkeIflKzVFqbqVI1iZrKqe1Is_u8shDidPZ95sxFW7XaTwQZtQ6SmzcPTHOaUrwgXOlIRWDSQxHTJzPsGf31HTLAWeVOIw07YAvWg5nqfrvgPfDzabL_zHpkY02oWIKkPkdQIk5BC578j4jfn-7D1fS2nsQE-iv82d9s_wJ703CofHOQk5DXZVTq0e9qda2-OFi8dmmoD0Tk0H_vm2g1thm3N2l9CbaLLjsJFVJWrMkBqfSVYqTKtod0M0Ds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای یک جنگل در ۱۶۵ میلیون سال پیش
🦗
🌳
🔹
دانشمندان با بررسی بال‌های فسیل‌شده حشرات ژوراسیک در چین، صدای احتمالی آن‌ها را بازسازی کردند؛ بیشترشان احتمالاً صداهایی حدود ۵ کیلوهرتز تولید می‌کردند، اما Sigmaboilus peregrinus احتمالاً صدایی فراصوت، بالاتر از ۲۰ کیلوهرتز داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/684969" target="_blank">📅 14:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ۶۵ درصد ذخایر پاتریوت آمریکا در جنگ ایران مصرف شد
وال‌استریت‌ژورنال:
🔹
آمریکا بخش قابل‌توجهی از ذخایر موشک‌های رهگیر پاتریوت خود را به میدان فرستاده است.
🔹
بر این اساس حدود ۶۵ درصد از رهگیرهای پاتریوت آمریکا در جریان حنگ ایران مصرف شده است. رقمی که به حدود ۱۵۰۰ فروند از مجموع ۲۳۳۰ رهگیر این کشور می‌رسد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/684968" target="_blank">📅 14:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHlst-LVoWIpzkbVSDWrwgCj0boGgPlLHlMP0sx9uVmo_MBUag3NiZjlwIUmC7NMTZEglOM44gjXZ1g5Vowy42-uPofSXT8rDsPTMWP1RUgxMDTpjniYNho8wA54h8CT-3fCNCuEOY0mq3x0UnumRZyyDyrT79thpVEPYEg-Np8GSxr0oOgaP6_ftMACa6jbKN1AUbA_-LFMu6FBtxCyhl10kb6RBNZHkpkJSDGb9qAGoXtro1cm39b5g7RSP-rL_OK8lYVxYJSIWpDbRlEnDLUBEzkbMY4Z4lYisq_NcpfwoqspgJ9PgXRc7iLrqXnM_6fzmQoBC5GTSvsek-BCeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس روز ناسا از چرخش آسمان
🔹
عکس روز ناسا رد کمان‌شکل ستاره‌ها را طوری به نمایش می‌گذارد که چرخش آسمان را نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/684967" target="_blank">📅 13:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6fe966772.mp4?token=QohiaSBmKlVZtrfjVZDofgkh8U5rAhRnHoEVuh883-l4eqvQiWo8HV1Kqn-Pu2yKqpDxZoukntRSVwek7jWBZgaw5khBniRij96SCMYtE3otW8mjWLVaQrCX1NLPWXCM90K4jbGo-1WrvfdWDpwHThaeM3YpdDq9w-qLonJxJGG5TqcWVWPlp8xY_AsJ7ehNMr49E4am0Ojp_mxm1zXC19puQc3Ixr68-iw08rNFOewLCDa2Vj2k01RWxsb4vIoL7rWarHkkntk8h6MaOl-o5_rCl1NrxCXQkEz62IDbnOtJpvog6EbTHVpWmohnd515dkjP9RnEwlF-oPibNEta0Bx5dyy6F9R-FMj56puo4bdu8mnCTkq7vNe71u0EsWHOHQrUXEeQipC8H4IN71togl-56pkRw7A_DGelr7RPjHF_quQU15uFXbJw-Wz9n73l-gb7bmR1u_844KiKkiqKCzPBS0wlccD4USp-CRRFkb51OsfYKiv9aRi1kJsRNNvooz7t8yUswj27y9-WxxR3TFyQItmJOMIZImrcThJd0dk-Cr94nhi_LTIaomKi66-a8Hy8wSw2iA5GlJgU7dU8NmUj_Ka0acSGbde8HyBHwGFboIktvolurI3wL7tN6gUsWQyUnrp8_OZ2Nxjty7y1ubgWa_LLZG4X5wyx_SF1IwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6fe966772.mp4?token=QohiaSBmKlVZtrfjVZDofgkh8U5rAhRnHoEVuh883-l4eqvQiWo8HV1Kqn-Pu2yKqpDxZoukntRSVwek7jWBZgaw5khBniRij96SCMYtE3otW8mjWLVaQrCX1NLPWXCM90K4jbGo-1WrvfdWDpwHThaeM3YpdDq9w-qLonJxJGG5TqcWVWPlp8xY_AsJ7ehNMr49E4am0Ojp_mxm1zXC19puQc3Ixr68-iw08rNFOewLCDa2Vj2k01RWxsb4vIoL7rWarHkkntk8h6MaOl-o5_rCl1NrxCXQkEz62IDbnOtJpvog6EbTHVpWmohnd515dkjP9RnEwlF-oPibNEta0Bx5dyy6F9R-FMj56puo4bdu8mnCTkq7vNe71u0EsWHOHQrUXEeQipC8H4IN71togl-56pkRw7A_DGelr7RPjHF_quQU15uFXbJw-Wz9n73l-gb7bmR1u_844KiKkiqKCzPBS0wlccD4USp-CRRFkb51OsfYKiv9aRi1kJsRNNvooz7t8yUswj27y9-WxxR3TFyQItmJOMIZImrcThJd0dk-Cr94nhi_LTIaomKi66-a8Hy8wSw2iA5GlJgU7dU8NmUj_Ka0acSGbde8HyBHwGFboIktvolurI3wL7tN6gUsWQyUnrp8_OZ2Nxjty7y1ubgWa_LLZG4X5wyx_SF1IwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای متانول در بنزین چیست؟
🔹
چند روزی‌ست خبری در شبکه‌های اجتماعی پیچیده که می‌گویند در بنزین متانول می‌ریزند.
🔹
سیاه و سفید این ماجرا را در این ویدئو بررسی کردیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/684966" target="_blank">📅 13:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d006dc17a.mp4?token=tOeYjwyWZgP08PJ2E2fOPwUzXa1GM4MpJBQPc8BtCo7c6F-YtVVPQDE6Z0zx9NPofiaqZc11pgblmKP_SZo0Uo3DP8rxh9Uh9Fr7QgHRXuG35wSpL4YF2f01VB2IMkbwdR8IfIKs65FDmrHvaY4ALjUMvbfHpWJ-qWgm2AtH0JWR_k_gOq4MMHB9YPH9_hOh_OD9n08K3KbOq4b6wFG9F0DT606MDuX8lkJ3PORnZqjU0w9g8S0f55KAecZ0bd0wU2_xv9hiPreK_mNFRMHHUo7FcYLCeIHJF7SRXFsWHaiCePPwf5orui4sJ2NibbeNJs4L5gMmV7qfxS99xwUwHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d006dc17a.mp4?token=tOeYjwyWZgP08PJ2E2fOPwUzXa1GM4MpJBQPc8BtCo7c6F-YtVVPQDE6Z0zx9NPofiaqZc11pgblmKP_SZo0Uo3DP8rxh9Uh9Fr7QgHRXuG35wSpL4YF2f01VB2IMkbwdR8IfIKs65FDmrHvaY4ALjUMvbfHpWJ-qWgm2AtH0JWR_k_gOq4MMHB9YPH9_hOh_OD9n08K3KbOq4b6wFG9F0DT606MDuX8lkJ3PORnZqjU0w9g8S0f55KAecZ0bd0wU2_xv9hiPreK_mNFRMHHUo7FcYLCeIHJF7SRXFsWHaiCePPwf5orui4sJ2NibbeNJs4L5gMmV7qfxS99xwUwHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاریخ‌سازی بانوان والیبالیست ایران در آسیا
🔹
تیم ملی والیبال زنان ایران با پیروزی ۳ بر یک مقابل اندونزی برای نخستین‌بار در تاریخ به جمع ۴ تیم برتر آسیا و مرحله نیمه‌نهایی قهرمانی آسیا ۲۰۲۶ صعود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/684965" target="_blank">📅 13:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f89e7e65.mp4?token=u8ngzznwOPwWl3rDgJBVUzrMGGcyPSKPF9NyAJOZavUtCdN4NH6MrPMmixKAqlXOWZ5HZTRrQN51gSXBKUm4_nVa1ggOvaVsJ72sSzNTKijG1R1m_7_Xa5ZnzKotwi9IKnRj9toyF47r0nWcqpNAkzq78Pk6P04hAbXhQV2cDettbUGg94v1dWGne2zoAId7TKBLSnFoTGbGRRCcVk4e4ymUMC7EQaA7l8p4gbCQ9q-ZZrSfyUwgLBvjI9en5Vs5X8CrwvpCeKo_9qNlQSuRPhxIsIWzX-B-THjvE571p2-ypT_BRIVHQmPh1B7FMc-L24Kgizpj7inQGW3xE8VFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f89e7e65.mp4?token=u8ngzznwOPwWl3rDgJBVUzrMGGcyPSKPF9NyAJOZavUtCdN4NH6MrPMmixKAqlXOWZ5HZTRrQN51gSXBKUm4_nVa1ggOvaVsJ72sSzNTKijG1R1m_7_Xa5ZnzKotwi9IKnRj9toyF47r0nWcqpNAkzq78Pk6P04hAbXhQV2cDettbUGg94v1dWGne2zoAId7TKBLSnFoTGbGRRCcVk4e4ymUMC7EQaA7l8p4gbCQ9q-ZZrSfyUwgLBvjI9en5Vs5X8CrwvpCeKo_9qNlQSuRPhxIsIWzX-B-THjvE571p2-ypT_BRIVHQmPh1B7FMc-L24Kgizpj7inQGW3xE8VFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین افشین، معاون رئیس‌جمهور: از شهید لاریجانی آموختم؛ مذاکره یا عدم مذاکره موضوعیت نداشت، منفعت ایران مهم بود / مذاکره اسلام‌آباد برای پیگیری منافع ملی بود
🔹
دفاع از تصمیم به امضای تفاهم‌نامه نیز لزوماً دفاع از نتیجه اجرای آن نیست. هنر سیاست دقیقاً در همین است که بداند در هر مقطع، کدام ابزار می‌تواند قدرت ملی را با هزینه کمتر به دستاورد بیشتری برای کشور تبدیل کند.
🔹
شاید یکی از مهم‌ترین چیزهایی که من از شهید دکتر علی لاریجانی آموختم همین نوع نگاه به سیاست بود. برای او مذاکره یا عدم مذاکره موضوعیت مستقل نداشت؛ سؤال این بود که منافع ایران کجاست  و با کدام ابزار می‌توان بدون عدول از اصول، مسئله‌ای را برای کشور حل کرد.
🔹
سیاست خارجی در این نگاه، نه مدیریت شعارها، بلکه مدیریت منافع و حل مسئله است. فکر می‌کنم درباره اسلام‌آباد نیز باید از همین زاویه حرف زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684964" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ترامپ متوهم به اکسیوس: تنگه هرمز باز است
🔹
تنگه هرمز باز است، آمریکا در نبرد هرمز دست بالا را دارد و پاسخ ایران بسیار متواضعانه است.
🔹
ایرانی‌ها نمی‌خواهند ما دوباره به آنها حمله کنیم و این اصل مطلب است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/684963" target="_blank">📅 13:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26d598245.mp4?token=lqhEN_duk0dBf_cUxPutDloSOcDu9FuRABRZmw3YhTyncXu6W8y2ce7WnVkZyvnajpo-_epsFdfc0JBjlEvNrAz9G0ru9O3ya_b4KPE3luSknLp3B87swr0Rq2FDo_Pohpn18OfiLVdZGBiY5LjczA9o1bMbG6_RWxQvF_Gj8W2Trrt7ohOj91LZb-66kwtCtzRtxnmSAspS5KUFYjes9qUny2fi_lqhcS1RSqmkeIqC9ja0yFcluqyhslX5omgM09hW7NUGURwxJbAW9bKxsI_LtymiXUp-qfbagHW4UtG9J2LfHe9HohISX6BBa594hPF1qOb0Zv_PtLIqV8ZHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26d598245.mp4?token=lqhEN_duk0dBf_cUxPutDloSOcDu9FuRABRZmw3YhTyncXu6W8y2ce7WnVkZyvnajpo-_epsFdfc0JBjlEvNrAz9G0ru9O3ya_b4KPE3luSknLp3B87swr0Rq2FDo_Pohpn18OfiLVdZGBiY5LjczA9o1bMbG6_RWxQvF_Gj8W2Trrt7ohOj91LZb-66kwtCtzRtxnmSAspS5KUFYjes9qUny2fi_lqhcS1RSqmkeIqC9ja0yFcluqyhslX5omgM09hW7NUGURwxJbAW9bKxsI_LtymiXUp-qfbagHW4UtG9J2LfHe9HohISX6BBa594hPF1qOb0Zv_PtLIqV8ZHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام طائب: بازار و تولید، لانچرهای جدید مقاومت در برابر دشمن هستند
🔹
دشمن پس از ناکامی در تحقق اهداف خود در عرصه نظامی، جنگ اقتصادی، امنیتی و ادراکی را دنبال می‌کند تا تولید، تجارت و کسب‌وکار در کشور دچار اختلال شود.
🔹
لانچر تنها ابزار نظامی نیست؛…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/684962" target="_blank">📅 13:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مدیر اکتشافات شرکت ملی نفت: هم‌اکنون یک چاه در منطقهٔ «دهنو» استان فارس در حال حفاری است و امیدواریم در این منطقه نیز به کشف جدیدی دست پیدا کنیم
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/684961" target="_blank">📅 13:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baf2302eb8.mp4?token=aQMXDuqiqfqnB0SMXoGNAflDgH8KQN6bKNontFMdz4gsBhKjw9YuS_innmLfXKp-KglkHMG65KGwHgQLixjomSlT74BDxX5yS9rRhsDCkPqi0Gw8CHgVgfSTgK_OfwuYU-Zp3x-mzrb7LW1lDz_j1TcNxPvz5U6Eq-eWR4I6K88JUzqVAHZi8HBIUJ9TNetpXrHjHz1f--O3jK7gFqjmKjG50VwmP8VZdcfvEz6Murq4ghQr1WITq_kqFqmnKE9Hh70D6LVSxAGkPzUmc3FuY_h6cfIhVgD8LnwJDHq0jndQSYk7Uh2cA9ijlzRySXwCqNwW3J6AYWDdf42E_4v55A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baf2302eb8.mp4?token=aQMXDuqiqfqnB0SMXoGNAflDgH8KQN6bKNontFMdz4gsBhKjw9YuS_innmLfXKp-KglkHMG65KGwHgQLixjomSlT74BDxX5yS9rRhsDCkPqi0Gw8CHgVgfSTgK_OfwuYU-Zp3x-mzrb7LW1lDz_j1TcNxPvz5U6Eq-eWR4I6K88JUzqVAHZi8HBIUJ9TNetpXrHjHz1f--O3jK7gFqjmKjG50VwmP8VZdcfvEz6Murq4ghQr1WITq_kqFqmnKE9Hh70D6LVSxAGkPzUmc3FuY_h6cfIhVgD8LnwJDHq0jndQSYk7Uh2cA9ijlzRySXwCqNwW3J6AYWDdf42E_4v55A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر به‌ مدت ۳۰ روز صورت خود را در آب سرد فرو کنیم چه ‌می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/684960" target="_blank">📅 13:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51314ca03.mp4?token=RNucFQZ2_DAThC9qItq5G51ifINgL-hS7V_wK_ZTff1Bv4_Vq7N1568qlAO0zR3_k1jXjzWsZKSfOqIOCEkFYrxUxGWyojn2CEJVI6fPp5UgD3Zxd0YHuJhHgWsDYlXU_4MGFBr4dyy8gnzke5LcONPvQKc7YyffzJdpiFgmGSXo8XpDgg9zzJUEoyR9wt-XiPrRISRIr1B9ReRj9mfBXKidpC7wNiCSyh8eJQGFqZxY8ROoN-P-e9GvhDrji1s94mOr6Ee5KLxmBV9bvIAMugP-SCRYr28zazsC1YThQyM7E6eNeBTtjsTsm2sQxhi_h2Oxct72bRFM_L3_TsM8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51314ca03.mp4?token=RNucFQZ2_DAThC9qItq5G51ifINgL-hS7V_wK_ZTff1Bv4_Vq7N1568qlAO0zR3_k1jXjzWsZKSfOqIOCEkFYrxUxGWyojn2CEJVI6fPp5UgD3Zxd0YHuJhHgWsDYlXU_4MGFBr4dyy8gnzke5LcONPvQKc7YyffzJdpiFgmGSXo8XpDgg9zzJUEoyR9wt-XiPrRISRIr1B9ReRj9mfBXKidpC7wNiCSyh8eJQGFqZxY8ROoN-P-e9GvhDrji1s94mOr6Ee5KLxmBV9bvIAMugP-SCRYr28zazsC1YThQyM7E6eNeBTtjsTsm2sQxhi_h2Oxct72bRFM_L3_TsM8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوب بودن بهانه نمی‌خواهد...
🔹
استاد علی صفایی حائری(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684959" target="_blank">📅 13:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: خودروهای داخلی ۳۳ درصد بیشتر سوخت مصرف می‌کنند
زینب قیصری، دبیر کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
آمار رسمی درباره سهم خودروهای پرمصرف از ناترازی بنزین وجود ندارد اما میانگین مصرف واقعی ناوگان حدود ۸ لیتر در ۱۰۰ کیلومتر است، یعنی حدود ۳۳ درصد بیشتر از یک خودروی کم‌مصرف با مصرف ۶ لیتر.
🔹
قدیمی بودن پلتفرم‌ها، ضعف فناوری و نبود فشار رقابتی واقعی از دلایل مصرف بالای خودروهای داخلی است و در شرایط ناترازی بنزین، افزایش تولید بدون کاهش مصرف قابل قبول نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684958" target="_blank">📅 13:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a02c7363a3.mp4?token=HydYjT3BdnX-L-kJn2fjGGJPPlUm1G7STwsPkSkq9YvR64elA8ZHiNBXGTEAMGd7y2qikORW4snsf_yhPuGdy6CvNgMmqI0aQrVfk9xGZ1nJn3NSwYrRy784MHf7zds-k23eM3-7SdY_Elb5S7TpGyoiOyNR7HGsOqOp-0OEKi2R5yQG-Zbi9BO74idJ6bJQ9RuienTwyXMhBIfJrlds4kekzzNdNz8WN3HjscPQDEJvXjbj3xu4r1AJbk4xWNMv5cDcpONzMaNHljEqSPY4ywNd0Oodo8TBlCp1-2CBwLwQL2HIeY-gY2PQzuKvCsZgYptBLaA8BMRksnqFrj5iKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a02c7363a3.mp4?token=HydYjT3BdnX-L-kJn2fjGGJPPlUm1G7STwsPkSkq9YvR64elA8ZHiNBXGTEAMGd7y2qikORW4snsf_yhPuGdy6CvNgMmqI0aQrVfk9xGZ1nJn3NSwYrRy784MHf7zds-k23eM3-7SdY_Elb5S7TpGyoiOyNR7HGsOqOp-0OEKi2R5yQG-Zbi9BO74idJ6bJQ9RuienTwyXMhBIfJrlds4kekzzNdNz8WN3HjscPQDEJvXjbj3xu4r1AJbk4xWNMv5cDcpONzMaNHljEqSPY4ywNd0Oodo8TBlCp1-2CBwLwQL2HIeY-gY2PQzuKvCsZgYptBLaA8BMRksnqFrj5iKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین افشین، معاون رئیس‌جمهور: توافق مترادف اعتماد نیست/ قدرت ایران یعنی کسی ما را در انتخاب یک گزینه محدود نکند/ مذاکره به معنای کنار گذاشتن دیگر ابزارها نیست
🔹
درباره تفاهم‌نامه اسلام‌آباد، باید یک سوءتفاهم را کنار بگذاریم. گاهی توافق‌ کردن را مترادف اعتماد کردن می‌دانیم و بدبینی به طرف مقابل را مترادف مخالفت با هر توافق. سیاست خارجی این‌گونه اداره نمی‌شود.
🔹
دفاع از تصمیم ایران برای امضای تفاهم‌نامه اسلام‌آباد، دفاع از اعتماد به آمریکا نیست؛ دفاع از حق ایران برای انتخاب ابزار مناسب در یک مقطع مشخص برای تأمین منافع ملی است.
🔹
ایران قدرتمند باید توان دفاع داشته باشد، توان مذاکره داشته باشد، بتواند پشت میز بنشیند و اگر حقوقش تأمین نشد، بتواند از پشت همان میز بلند شود.
🔹
مقاومت برای حفظ حق انتخاب ایران است و مذاکره نیز می‌تواند یکی از شیوه‌های استفاده از همان حق انتخاب باشد. انتخاب ابزار مذاکره نیز به معنای کنارگذاشتن سایر ابزارهای قدرت نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/684957" target="_blank">📅 13:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91868030d2.mp4?token=qiucEeTPJTXrR2ZdUVZDSBVQDhE9Dskn6RS57eKQoIcOgWOT6OFF5QzwttfgeOHjBGWBxteDUqo4ayptAl_dieL7ZfNgUndMJJDTvU8Uf6DeH4PmGIf_yUM8v67gqf98iROLBna6iJapMoACBm1Dj8BhXud05eFmhvQQz8ba6sFJoQphqzBX5CVi28r159krC_7QjJT79lkZY1uZmsC84BfpreAYU5lrXtYdgRc-M8usdRwsUsObGAh4XceyE25fT7ddHuBJYR4fIIqQdeXmXrAFMRjkTJdxyCZ_df0rnyfQpMpD2sozzCHXKfjIiIfy6caSjbRpyKBYnWQlPV2oBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91868030d2.mp4?token=qiucEeTPJTXrR2ZdUVZDSBVQDhE9Dskn6RS57eKQoIcOgWOT6OFF5QzwttfgeOHjBGWBxteDUqo4ayptAl_dieL7ZfNgUndMJJDTvU8Uf6DeH4PmGIf_yUM8v67gqf98iROLBna6iJapMoACBm1Dj8BhXud05eFmhvQQz8ba6sFJoQphqzBX5CVi28r159krC_7QjJT79lkZY1uZmsC84BfpreAYU5lrXtYdgRc-M8usdRwsUsObGAh4XceyE25fT7ddHuBJYR4fIIqQdeXmXrAFMRjkTJdxyCZ_df0rnyfQpMpD2sozzCHXKfjIiIfy6caSjbRpyKBYnWQlPV2oBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر منتشر شده از حریم قلعه فلک‌الافلاک خرم‌آباد دقایقی پس از بمباران ۱۷ اسفند ۱۴۰۴ توسط جنگنده‌های صهیونی - آمریکایی
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/684955" target="_blank">📅 13:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uBl9ObVoxaEkcFHL9Pmn2MjuXxWWxfL4gi7PA24ou4Xf4L93ys0OUYWPHdOfg3U3YpWF4t9XCwB1L9aizbupLAAjpGS4SlBOpvlilZPflykQY0AiAHVm0rUxjYMtMqpRbZXAfhrwcRsW8Q9zFiwJiJIM_bfUbuy4X9mcwSe2sGoMX0Knqc7YC8a-2Wm0_Sf8hZEf8Tc9LIJ2N5kgoLFA3viQJo1aLOypf6QJ9m304KLrOgGu9Pd7wGTsTuWlnkqsJab4sO8hUFazktWzwz_ZixIiUcOmJEHi8h7gSK-MSQx3wKLH0nr_Z9Oks3M81kp8RzsHJ1RecLqOR45PrljFpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPEOfRwFxJBe8eun_7_9FBIRj6vv2qqyTFof0Fs6H4tA6bDmADFt9MmuO0WZxaz5HYOoTQAhMlwNHoTMjE-n-9qs3_VHIn99b07vkSHgy3jgDhpWNR1Kf6xQB7V6vA4ZWK9jU3rNYaTQoWspD6CF0wU91LjXxNRtFnv7dowYZo6FoDdz1BF8Vo8wwk45m8jrx8ULSiKYpmOJ6JeMrHnHSxKOmf4bgkjMdXvbAGAq86EuFJA4_bZ-ROgtzqhhJU0V6YiIkd9SRi69w-C7oWW3qeAXTaEuJJ4mxDxyd95w5aO2zAvni7bF2D6jGNHNp-FSj3VxY4J69Whd-LKY-VZopQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرمانده سنتکام ادعای مین‌روبی تنگه هرمز را تکرار کرد
🔹
براد کوپر، فرمانده سازمان تروریستی سنتکام بامداد جمعه مدعی شد که ایالات متحده موفق شده مین‌های کار گذاشته شده در تنگه هرمز را پاکسازی کند.
🔹
کوپر مدعی شد که ۵۰ هزار نیروی نظامی آمریکا در حال اجرای محاصره…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/684953" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHtB4OPDo1v-LOUrRgdCniCPZEbBr25bBWL5zoobXALaZYFc_VVT2UA6D9Orlmg6g-eQ2WfzkBgsmTH5Ph_sAcxhttv-15BrtHfwcw1UV467zMirkHvBVrMCeNZ4AoiSVzJEhJCGJ3lZiRRp7HfMpFg3d4nZiQqC3KYx6MpZKXJTC59wa2hVPmSiVELqXmSf-Em4MFxzW2YiDvka6lNVyQ3rZaOP9LxDp4ha9nwI7JPh0if9QjgxzCXM_Wz4itysF0Vgt6k2LCf6K-o9-vw4DRpB2vLokzE1y0ihWrzjZZbmWTMXG3aw6GXjNlG9qNGTV8IA0GSS0HdwD_WM0Er5Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دست از توهم بر نمی‌دارد: «تنگه هرمز بخشی از آمریکا است»
🔹
دونالد ترامپ در تروث سوشال بار دیگر تنگه هرمز را بخشی از خاک آمریکا توصیف کرد؛ ادعایی که بیشتر با تمسخر و انتقادات شدید از سوی محافل آمریکایی مواجه شده است. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/684951" target="_blank">📅 13:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dec2b803.mp4?token=QYcXKVKhCgWL_UDDa12zxAXlgxFlBwf3sWfCSJtrY1jKc7mRo5bc65GfYwzHJMaJ4cyNU49nLFqw6HTMuB1qUnexVoOOyRu5iNGyE5K7OW5ADGeGzZjQb8O5AbFc8tqQ7QOsVZum5dn0__ZvuAhlDOrUDyTzeUDIpvlYjpLH_igD6KP5uJ5KQBzco4ViW4bIb36lqoFUyPbVNK9ul_d9FVroLChB3B5xcVfpC0uj8Y-Vl5VbVA2-UuY-dpHLm8GFi8QHS65WTWTn8buq7eTVrJKJuPFwPX-S0O90YX81F-vJp9h3TWPVJUHkGpPlGylKOvA-yU9SGmSjQJRdgDMFng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dec2b803.mp4?token=QYcXKVKhCgWL_UDDa12zxAXlgxFlBwf3sWfCSJtrY1jKc7mRo5bc65GfYwzHJMaJ4cyNU49nLFqw6HTMuB1qUnexVoOOyRu5iNGyE5K7OW5ADGeGzZjQb8O5AbFc8tqQ7QOsVZum5dn0__ZvuAhlDOrUDyTzeUDIpvlYjpLH_igD6KP5uJ5KQBzco4ViW4bIb36lqoFUyPbVNK9ul_d9FVroLChB3B5xcVfpC0uj8Y-Vl5VbVA2-UuY-dpHLm8GFi8QHS65WTWTn8buq7eTVrJKJuPFwPX-S0O90YX81F-vJp9h3TWPVJUHkGpPlGylKOvA-yU9SGmSjQJRdgDMFng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از سیل عظیم نپال که نشان می‌دهد آن منطقه کاملا تخریب شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/684950" target="_blank">📅 12:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ابداع عجیب علیرضا منصوریان از زبانی نوین!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/684949" target="_blank">📅 12:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SM8B2r2i-_CUxDr4phboSfCuhN0uOr-HSMbF2fko9ZU9Rj4XS0i4aHBV6HLEpBSbncf8qUoW6jn_OqfEqMgNZ2ocaDwNi3L9-xyDwl29HU0XBP3hbgYoRwsT3OjIa-icyKYNxI5PHN4alKCFpVTg0IcFzccoDo3UYmaG9K4VfrAOZqwvwnfG-jWRVRtoQ9xIeeb0TVgZdS_szwUzw1RPEvdvZNHUhLTPc9Sw6E1bBu12O9pkn6vDb_Lp1zwln7rJq6vHJ6Rz0AfQ686V7t5drkIgiYGfYKIsV-axZze2vhUtwt3w3Iset5FakMQs8S4wTHzQ_exrYGqMB_gA2dSZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروزان: منطقه آزاد ارس الگوی مناطق آزاد کشور است
🔹
حسین فروزان، دبیر شورای‌ عالی مناطق آزاد تجاری ـ صنعتی و ویژه اقتصادی کشور در بدو ورود به منطقه آزاد ارس با حضور در مزار شهدای ۱۳۲۰ جلفا، به مقام شامخ شهیدان ادای احترام کرد.
🔹
فروزان در حاشیه این آیین با اشاره به ظرفیت‌ها و جایگاه منطقه آزاد ارس اظهار کرد: ارس الگوی مناطق آزاد کشور است و این منطقه با وجود ظرفیت‌ها و پتانسیل‌های فراوان، می‌تواند الگویی برای تمامی مناطق آزاد کشور باشد.
🔹
وی همچنین با اشاره به عملکرد مدیریت سازمان منطقه آزاد ارس افزود: مدیرعامل منطقه آزاد ارس یکی از موفق‌ترین مدیران مناطق آزاد کشور است و اقدامات انجام‌ شده در این منطقه نشان‌دهنده ظرفیت بالای ارس برای ایفای نقش مؤثر در توسعه اقتصادی کشور است.
@arasfz
.ir</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/684948" target="_blank">📅 12:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwr8JUa2EqIw-2OyqtjBZtmch_lTwayi-FkLPodckEQiWVSBfeXjNKb8lSJOTXZ5gr9io814dnQNecyv3HzEeA3xMfs7LKllAU23XHqoaP2eY6lI9dZ2gkxoGo0CREkbMbWDE2JMWvdPWu3ZMHPAw7ehLtUp_-BpfFyHOxht_NtnymW42VcZ5U95qIgRNH_q6m7KsCWvXGcBXmJJlmmhtqrVqe4b6qwLSmvDjJUrlXkCkKL72sbnrGBcHM9qdFSt5LeibNwRBN2c9Zw2eLHO8g5gZlxmlzoSC60icOFYHYY5HbgOowh2ulaEDWaHHavtuoHHjPkQoVoAOCIMF248HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده سنتکام ادعای مین‌روبی تنگه هرمز را تکرار کرد
🔹
براد کوپر، فرمانده سازمان تروریستی سنتکام بامداد جمعه مدعی شد که ایالات متحده موفق شده مین‌های کار گذاشته شده در تنگه هرمز را پاکسازی کند.
🔹
کوپر مدعی شد که ۵۰ هزار نیروی نظامی آمریکا در حال اجرای محاصره…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/684947" target="_blank">📅 12:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتسبیحات</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b240ae7ca6.mp4?token=QJ-CixAGQdO-UFAtn8w8QbfWMqTXK1hif-twyyhmjperVIzv7SxNBZwqQHtlLWAuMazp3AQFlvy9VrpNUkumdIf6NOLTPfC2v1057SV5dL_NxGBU9AnM1-XBIUWrnmNd47_jHXIbopcGSrgda5ehPXgwQnJ6eTeKs6_o10qf12V1qJEGMcscP8c8ghQbdkMofl8JUsccjmSKtY-I_VbgUMEMt4to_XR3NYe5NsN3bsoD82EvqdnNt8MOcawrYsKoeTgToHyXWAJ8xifsrlcLhRCiKTKEq1ToSV2Nqpc-EWGqAyoXZoEVdTZ1yuwKYzavUhiRsoyQ451CE5UxCUB1Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b240ae7ca6.mp4?token=QJ-CixAGQdO-UFAtn8w8QbfWMqTXK1hif-twyyhmjperVIzv7SxNBZwqQHtlLWAuMazp3AQFlvy9VrpNUkumdIf6NOLTPfC2v1057SV5dL_NxGBU9AnM1-XBIUWrnmNd47_jHXIbopcGSrgda5ehPXgwQnJ6eTeKs6_o10qf12V1qJEGMcscP8c8ghQbdkMofl8JUsccjmSKtY-I_VbgUMEMt4to_XR3NYe5NsN3bsoD82EvqdnNt8MOcawrYsKoeTgToHyXWAJ8xifsrlcLhRCiKTKEq1ToSV2Nqpc-EWGqAyoXZoEVdTZ1yuwKYzavUhiRsoyQ451CE5UxCUB1Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🦋
فضیلت قرائت سوره‌ی مبارکه صافات در روز جمعه
◾️
@Tasbihat_ir</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/684946" target="_blank">📅 12:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684945">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61b85f63b.mp4?token=XS6-3960Q__SokppX9l58U_oFCtAN4bUAI6P7YWAJrD7TxoGpVP1Y-Wredt_IumZkWPQFMp1GDDZBZhmE4gxwAjObJXwvcrUuvxy5hhWx03dgeUQ9__-WrKOrVojmuiBJ266ULAyl2g-BR7g1JwzasZHOulJSAc6YG3MOinkwP69Ozu8IGHGq-6KDu1_3Sy7OMI1WWhncP42g9k3HOFK6oF3kLng_HNkuWlY4d8kMVx8gg4n9jRUnLcIIwgl_JWrBlCXy84MWwvjqlqod4AzQM70fnYQ1fc6vGMNlD4YkuvN43Ej0pj-f-3Mf6MITgjyVEqGJ54qm719-O19PP1TbodVCm7jiYAkAuJvW-LYx9AcN4MsXurh1-Rr6XvrO7onRlxRsrfJWzSCBMmp3kSjBvl-t1HNaU9zOcT2n-ckozFFcfSn4ttCNYiN3ILZjXobPKRA1Hsr64SbT7KWd3UtrpKEbs6TeLEIIoJuZbeogGKJN_vkesXtNwsqFkKFVjf5ChtiT5AUYOUGZjMJbwZLaGQDvFh001nqSMt2FQ0GbWn8xGaABceEsBJBgoTkM0lzMUO827B6KUlkGTjO6OgAqoYW7Z-83yfvaTywfRZF2el4_OyDvqdm7zHqu0azIV6_381E6I5eQ5xZ0mNGVViVQ9iAY2pPygCUBMQokoINcOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61b85f63b.mp4?token=XS6-3960Q__SokppX9l58U_oFCtAN4bUAI6P7YWAJrD7TxoGpVP1Y-Wredt_IumZkWPQFMp1GDDZBZhmE4gxwAjObJXwvcrUuvxy5hhWx03dgeUQ9__-WrKOrVojmuiBJ266ULAyl2g-BR7g1JwzasZHOulJSAc6YG3MOinkwP69Ozu8IGHGq-6KDu1_3Sy7OMI1WWhncP42g9k3HOFK6oF3kLng_HNkuWlY4d8kMVx8gg4n9jRUnLcIIwgl_JWrBlCXy84MWwvjqlqod4AzQM70fnYQ1fc6vGMNlD4YkuvN43Ej0pj-f-3Mf6MITgjyVEqGJ54qm719-O19PP1TbodVCm7jiYAkAuJvW-LYx9AcN4MsXurh1-Rr6XvrO7onRlxRsrfJWzSCBMmp3kSjBvl-t1HNaU9zOcT2n-ckozFFcfSn4ttCNYiN3ILZjXobPKRA1Hsr64SbT7KWd3UtrpKEbs6TeLEIIoJuZbeogGKJN_vkesXtNwsqFkKFVjf5ChtiT5AUYOUGZjMJbwZLaGQDvFh001nqSMt2FQ0GbWn8xGaABceEsBJBgoTkM0lzMUO827B6KUlkGTjO6OgAqoYW7Z-83yfvaTywfRZF2el4_OyDvqdm7zHqu0azIV6_381E6I5eQ5xZ0mNGVViVQ9iAY2pPygCUBMQokoINcOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
روایت پدر و مادر ۲ شهید از روز تلخ مدرسهٔ شجرهٔ طیبهٔ میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/684945" target="_blank">📅 12:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684943">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2131ef8bc0.mp4?token=vZEQ0W7Tv5spkBpVcTUqRmfoMTF0X9tyb50tAyo6H31civVhFhEL2-xBo2BkiEnmcLDHDKKD5PNeiRuoBteyT5tNciOT_m7p558UYAprE487x8gvyF6rM_zr-AuARfjq7_ddl0FNakAyKZkFPIVxMJ97qWjc9NI0oQc8IuxCsyjdYgFKMPc37uTOmtCwzneiDxi0pP4AIr2V9VTPiuArL1uQ7UmYf1wOGiDLcI9NVJZMu4-N2TLGt6_mCdFEY3yPij9fJpxniZzHKgpfK-9qb0xHZH-eBf8c2dz5gUpO5wbz3A1dnJIPoi4PyLtogoe2S6E4GW-cx15aNYfNLppOyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2131ef8bc0.mp4?token=vZEQ0W7Tv5spkBpVcTUqRmfoMTF0X9tyb50tAyo6H31civVhFhEL2-xBo2BkiEnmcLDHDKKD5PNeiRuoBteyT5tNciOT_m7p558UYAprE487x8gvyF6rM_zr-AuARfjq7_ddl0FNakAyKZkFPIVxMJ97qWjc9NI0oQc8IuxCsyjdYgFKMPc37uTOmtCwzneiDxi0pP4AIr2V9VTPiuArL1uQ7UmYf1wOGiDLcI9NVJZMu4-N2TLGt6_mCdFEY3yPij9fJpxniZzHKgpfK-9qb0xHZH-eBf8c2dz5gUpO5wbz3A1dnJIPoi4PyLtogoe2S6E4GW-cx15aNYfNLppOyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میکروداک؛ ربات خانگی کوچک و هوشمند
🤖
🔹
رباتی ۲۵ سانتی‌متری با وزن کمتر از ۸۰۰ گرم، مجهز به دوربین و LiDAR که ۷ رفتار مختلف را اجرا می‌کند و قابلیت آموزش مهارت‌های جدید را هم دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/684943" target="_blank">📅 12:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b17096ec3.mp4?token=OYtrgwpkq0xXltQwmdT_XknW37e9QgVmwIvjq4cS-jx8vRhWs7eyuodt-h0hjmrSF7i4GIBElox02edKTUvaJRUZwUOICI-cBEH1iInZTQmOEkPHed2VE5ntn14LCnR7omF-NKOZjscs0OU6u3gd7o2njz19HCUvhKmBZCxJzG5IoWovV3z5C_kJcEZWPZoUizA_ss8EpYNx6RN7hGOOChKZRVYlKcMvda8Z1wv6jJZIHZtOVPvDF3_Jkg1lhJJEHeo08YvT8mkum4D5L_EnUjIGFZtrr_OyEdKQpTPF7N6dYaqXJRSTbCN3Z3sqNHyLRCYYTz6D9jWWOwc-xrU7Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b17096ec3.mp4?token=OYtrgwpkq0xXltQwmdT_XknW37e9QgVmwIvjq4cS-jx8vRhWs7eyuodt-h0hjmrSF7i4GIBElox02edKTUvaJRUZwUOICI-cBEH1iInZTQmOEkPHed2VE5ntn14LCnR7omF-NKOZjscs0OU6u3gd7o2njz19HCUvhKmBZCxJzG5IoWovV3z5C_kJcEZWPZoUizA_ss8EpYNx6RN7hGOOChKZRVYlKcMvda8Z1wv6jJZIHZtOVPvDF3_Jkg1lhJJEHeo08YvT8mkum4D5L_EnUjIGFZtrr_OyEdKQpTPF7N6dYaqXJRSTbCN3Z3sqNHyLRCYYTz6D9jWWOwc-xrU7Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
از ایده‌های کوچک در خانه تا کسب‌وکارهای واقعی؛ داستان کسانی که با کمترین امکانات، راه خودشان را ساختند.
🔸
داستان راه‌اندازی کسب‌وکار شما می‌تواند الهام‌بخش دیگران باشد. در یک صوت کوتاه ۳۰ ثانیه‌ای از شروع کارتان بگویید و تصویری از محصول یا کارتان ارسال کنید. روایت‌های برگزیده در خبرفوری معرفی می‌شوند
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/684942" target="_blank">📅 12:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e49f0166d.mp4?token=W7nfTsl9qLsJ5R8F0mXdJlVBu5WUKE6UO9z3z76sOnL3KNq5orxps3eybVJFaB8ITJmnVfst8ogeonRImo2F3XX5gN8S_J1MUwLfTn_gw_XtA0ciCJaV-QVgd1JfrhNuLa9LLfriBgFYsMEqodk8P-szP5bQObKyXfN9SSLImd9ClHT8gx7NvSrZf9JN9hkuKIVstCeKvpUeGK3d63-rro_J6MZIslVUdguFDRpg1Cm1F1srLZOY2qEVJCrFgayUFaKQH1J2Fst_JENDY8EcnMe5mCM9C4yVBkNCdRU7SMAxKJRmX8-EPe9-NVeZoXjS25CefbTG6XuB2NTqXaxCplM0mmsImfLWKbFRzGnFqXrCIVz779TfUQ60etfO46TVAlo27vMkwSknIPagtjqI-oJR7G0UWH1-rp2nDScIApsQ-vmfk-UA7uCMa_zB-W1pWFyRv9WQ6t3YXGZIPWOT-6rjNVlct7F8ezo_EtKFFWOA4hLf37UJ9ZRi28yh4B6F1FKU3z_pxXCZXvkwSZAhL3y6gFveHLvHObfm2Rb84OQdCA1V-9EIpgxyBi47qjTVPLj0hlSVuN_TlJZHMGzYGu9a9lVccctdEYtJ30JKKYOHn2pBcEh9Qv6teMjrkNI3ao9gOFx8Dbt0I2Y16apPMi63qXrOum7ZVLGknX-dNtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e49f0166d.mp4?token=W7nfTsl9qLsJ5R8F0mXdJlVBu5WUKE6UO9z3z76sOnL3KNq5orxps3eybVJFaB8ITJmnVfst8ogeonRImo2F3XX5gN8S_J1MUwLfTn_gw_XtA0ciCJaV-QVgd1JfrhNuLa9LLfriBgFYsMEqodk8P-szP5bQObKyXfN9SSLImd9ClHT8gx7NvSrZf9JN9hkuKIVstCeKvpUeGK3d63-rro_J6MZIslVUdguFDRpg1Cm1F1srLZOY2qEVJCrFgayUFaKQH1J2Fst_JENDY8EcnMe5mCM9C4yVBkNCdRU7SMAxKJRmX8-EPe9-NVeZoXjS25CefbTG6XuB2NTqXaxCplM0mmsImfLWKbFRzGnFqXrCIVz779TfUQ60etfO46TVAlo27vMkwSknIPagtjqI-oJR7G0UWH1-rp2nDScIApsQ-vmfk-UA7uCMa_zB-W1pWFyRv9WQ6t3YXGZIPWOT-6rjNVlct7F8ezo_EtKFFWOA4hLf37UJ9ZRi28yh4B6F1FKU3z_pxXCZXvkwSZAhL3y6gFveHLvHObfm2Rb84OQdCA1V-9EIpgxyBi47qjTVPLj0hlSVuN_TlJZHMGzYGu9a9lVccctdEYtJ30JKKYOHn2pBcEh9Qv6teMjrkNI3ao9gOFx8Dbt0I2Y16apPMi63qXrOum7ZVLGknX-dNtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفت‌وگوی مهدی کروبی با زائران حرم امام خمینی (س)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/684941" target="_blank">📅 12:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fba1a46725.mp4?token=s_2VOuf8AK97x1b7SGLUh0kcdKczmFlTT2RuLvYIhouYu10-of5Y6UyIISxJRUZiTvna0OILNM-aMkntBICZ_239itBb6THnALj8zFSS701ruIwX1ypqRp4T9HS7TaXWxoC2ODnfmvH1nxOkBnthOpWgbl9sFYlA5cHAe6vTt8-fsndgBof-euA2LVzs8hlRQVcDyqj7RpkCBEeSo1hrYmzfo-hmGvbqoJLycayW6vp0zKdTvQ4POVHQdlosSQ4ZAuelU3JijFhRnBvCA_NqWrK_vV-nu0Bg5vhm-Gsy53klRFADpSBVMqmtvmavuOaDmNhswLjScXuy8xGyrjg3lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fba1a46725.mp4?token=s_2VOuf8AK97x1b7SGLUh0kcdKczmFlTT2RuLvYIhouYu10-of5Y6UyIISxJRUZiTvna0OILNM-aMkntBICZ_239itBb6THnALj8zFSS701ruIwX1ypqRp4T9HS7TaXWxoC2ODnfmvH1nxOkBnthOpWgbl9sFYlA5cHAe6vTt8-fsndgBof-euA2LVzs8hlRQVcDyqj7RpkCBEeSo1hrYmzfo-hmGvbqoJLycayW6vp0zKdTvQ4POVHQdlosSQ4ZAuelU3JijFhRnBvCA_NqWrK_vV-nu0Bg5vhm-Gsy53klRFADpSBVMqmtvmavuOaDmNhswLjScXuy8xGyrjg3lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش‌های تشخیص دلار تقلبی از اصل
💵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/684939" target="_blank">📅 12:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
پول ایرانی‌ها در بازار سرمایه امسال کجا رفت؟
🔹
پول سرمایه‌گذاران حقیقی در پنج ماه گذشته به هر سه بازار سهام، طلا و درآمد ثابت سرازیر شده است.
🔹
بررسی جریان پول حقیقی نشان می‌دهد حدود ۷۰ هزار میلیارد تومان وارد سهام، ۵۴ هزار میلیارد تومان راهی صندوق‌های طلا و نزدیک به ۵۰ هزار میلیارد تومان جذب صندوق‌های درآمد ثابت شده است.
🔹
در مجموع، حدود ۱۷۴ هزار میلیارد تومان پول حقیقی میان این سه مقصد جابه‌جا شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684938" target="_blank">📅 12:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
تورم مرداد ماه ۶۹.۹ درصد شد؛ تورم نقطه به نقطه خوراکی‌ها ۱۲۸ درصد
🔹
مرکز آمار ایران از افزایش ۳.۴ درصدی شاخص قیمت مصرف‌کننده در مردادماه خبر داد و اعلام کرد تورم نقطه‌به‌نقطه خانوارهای کشور به ۸۹ درصد و تورم سالانه به ۶۹.۹ درصد رسیده است؛ در این میان تورم خوراکی‌ها و آشامیدنی‌ها با ثبت ۱۲۷.۵ درصد، همچنان در صدر قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/684937" target="_blank">📅 12:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f016533e7a.mp4?token=XGI0GzcjKjWYhdlmVrdRwir-QVTYaYA7FQdoJQy2FDgbJVmEi7d84EbgXvVTkvl49YGzzPR0WegN2GNbyocGuOt60Ml1-sEgWXxX12feqtAg3XB9OBFacsYmPxHw0KHTfAUmyWaUUTsDxtzeSuVMO-_OBnNHxQWiWoNinwd5E1U6fV9YCe1VJsgQ_iThMiH9094mNu8DZU1nKUbkD6EaSIUyVSFEkDqd0KIRo0Y4El6DIqkbRsBzpRvXJzrVFsH2nNo9j03F5duiWGxrlXeRbtzN5UzPIzZSSZi72qlH953IQGcKkVUBpb3ErAFGSJvVl0_d6x0k6lUGZI8DU-gl0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f016533e7a.mp4?token=XGI0GzcjKjWYhdlmVrdRwir-QVTYaYA7FQdoJQy2FDgbJVmEi7d84EbgXvVTkvl49YGzzPR0WegN2GNbyocGuOt60Ml1-sEgWXxX12feqtAg3XB9OBFacsYmPxHw0KHTfAUmyWaUUTsDxtzeSuVMO-_OBnNHxQWiWoNinwd5E1U6fV9YCe1VJsgQ_iThMiH9094mNu8DZU1nKUbkD6EaSIUyVSFEkDqd0KIRo0Y4El6DIqkbRsBzpRvXJzrVFsH2nNo9j03F5duiWGxrlXeRbtzN5UzPIzZSSZi72qlH953IQGcKkVUBpb3ErAFGSJvVl0_d6x0k6lUGZI8DU-gl0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسیاب قهوه چگونه کار می‌کند؟
☕️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/684936" target="_blank">📅 12:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
الجزیره: ترامپ در ۶ ماه جنگ ۳۱۹ پست درباره ایران منتشر کرد
الجزیره:
🔹
در شش ماهی که از آغاز حملات مشترک ایالات متحده و اسرائیل به ایران می‌گذرد، دونالد ترامپ، رئیس‌جمهور، حداقل ۳۱۹ پست در مورد این درگیری در تروث سوشال، پلتفرم رسانه اجتماعی خود، منتشر کرده است؛ این تقریباً معادل یک پست در هر ۱۴ ساعت است.
🔹
بین ۲۸ فوریه و ۲۵ آگوست، ترامپ حداقل ۴۱۸۹ بار در Truth Social پست گذاشت، به طور متوسط ​​۲۴ پست در روز. از هر ۱۳ پست، یک پست به ایران اشاره کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/684935" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIURP2qR_JNXiypDjbLljWBEu8Ke8V3fZQmZWFhUOz34dVvIAMiJJWwRpl9bw2q-lCd7G2Jc1lh5DClL7mRB2klBPeXLUh2bSLyOoVwOhZY6FOvZdb2eTU4jWyp-7KB-bZGXS_DFOA5cxKQ-gb76b2Qm7ljNgDjg6Vv6FMpQKP0ZbshmJnbDxWmNOAKVA0tjdXTiKpQ1kjVkyNvi1TjJyMOfjZLqHTVoyQcafWk1QyRRHO0EVNCd6tvv4cCoJPEw3Tas-6ohgQs-uVm0q53pCk1hEDjoP6oxm2YOcf-YUdRkl-L03qKIgALrDVpHLkmEkjrHhcB95ZGPg1LZTHXblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جنجال عجیب بین علی کریمی و رضا پهلوی!
طرفداران رضا پهلوی خطاب به علی کریمی:
«از جاویدنامان سوءاستفاده نکن!»
حالا این اظهارات، موج جدیدی از واکنش‌ها را در فضای مجازی به راه انداخته است.
⚠️
ماجرا از ادعای ایرج مصداقی، مشاور رضا پهلوی شروع شد که گفت پیج علی کریمی دست خودش نیست و توسط امید دانا اداره می‌شود؛ کریمی در واکنش گفت «غلط کردی» و بعد از پهلوی اعلام برائت کرد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/684934" target="_blank">📅 12:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89edda45b9.mp4?token=loshHcIhAwjRNZRotDBSFkY7kOe3HCLZSop5iQEGFbSWl3OBUqarEipu9_pRuDsIO3omqUhWkxO1E-NG92Z03x0loD1ReMbNrZhbfnCpfa6siCPyF9pFDWMSC1PDCoCDDlJO0lGuHLUcA5591_gKoUAKvLvspOvHHeR7LV1om7EHGIJW2oL2RUhd9K0EU1GAvkUKw-PB4zmsqwR9JFkI-gOEl9py9rC4JZYKZe70_n4r3e4b0h7kAH7lGMBMqyRRsOYZt2Nv5qceLU3jNm6ujaJLUCuRcNIh3qHJaXANesJY-TKg_FNoYJmbjnRuAKv-Zaux0pBofovEszoMt5kUHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89edda45b9.mp4?token=loshHcIhAwjRNZRotDBSFkY7kOe3HCLZSop5iQEGFbSWl3OBUqarEipu9_pRuDsIO3omqUhWkxO1E-NG92Z03x0loD1ReMbNrZhbfnCpfa6siCPyF9pFDWMSC1PDCoCDDlJO0lGuHLUcA5591_gKoUAKvLvspOvHHeR7LV1om7EHGIJW2oL2RUhd9K0EU1GAvkUKw-PB4zmsqwR9JFkI-gOEl9py9rC4JZYKZe70_n4r3e4b0h7kAH7lGMBMqyRRsOYZt2Nv5qceLU3jNm6ujaJLUCuRcNIh3qHJaXANesJY-TKg_FNoYJmbjnRuAKv-Zaux0pBofovEszoMt5kUHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با خرید از "چرم مَنطِـ" BMW ببر
❗️
از %𝟲𝟬 تا %𝟴𝟬 تخفیف «تمامی‌کالاها»
در جشنواره پایان تابستان مَنطِـ
🔥
➕
𝟮 میلیون تومان تخفیف اسنپ‌پی
حضوری و آنلاین با کد: PAYCWGZ5
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/684933" target="_blank">📅 12:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کوثری: هرگونه توافق با عمان منوط به برداشته شدن محاصره دریایی است
عضو کمیسیون امنیت ملی:
🔹
در غیر این صورت تنگه مسدود می‌ماند و اقدامات تهاجمی در هر نقطه‌ای انجام خواهد شد.
🔹
آمریکا حتی در دریای عمان هم حضور ندارد، چه رسد به خلیج فارس؛ تمام منطقه در تیررس موشک‌ها و پهپادهای ایران است.
🔹
پیام‌های آمریکا از طریق قطر، عمان و پاکستان رسیده، اما ایران فقط پس از اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ وارد مرحله عملیاتی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/684932" target="_blank">📅 11:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684930">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d0c9a321.mp4?token=QCSTdcMEdCWNFD3dCu2JjzG7fJtiexRdVMwvBvlQWICdF4tcs4zk0Gh2RDFZkQOPAN3UfbHdjYk1aq7E0K3bii4hFdRyWjnU-ZK6oKJp90rFtaLr43a1zpM_h-G2i-Y3F1QvHPiWDm38zBXU3RHZNtFoErpLdp82A9UizPTuAAqx-ZFv4fUISSVydpnSPTbqWe3sj1-dPMIY4xlidKO23kx1JmXbDicrfO1CU4r0ocAfuv8vGqri0BvevT1eCwm9LdJBYRzxr1XmiCjRDmO_7r68CDf0-jzZOjUTdrvllLg48-kIQX4mCmEUW6SMZCIMG0wljs3E66qvSw0pq-rdsC00AFWFgUs6t-bAhE04mFQCYQUlE5FGQyTMqIgF7EYhiPl3z9-UOTh1amyHIGkPo_bmI5PVn_cTFtspbUH0WldlJEKZGbJU05wfHvPumPe6ivnH1DcJnzNHDee-cbQ5TJW_z1XLeQKXXqpFjWZmf8JsdJMaefgdkImMj3wzcxPPwxJDeOyI4EewSnxSkUmGSr9QkTAxCuAt_xEz6efXgfJjEVrZtq0kpdC1ldA79dQ-El22M83F37hIbOAYTpLahCLXDOKVt7xAD6LFTp_v0FQLmLIWLvGEvokz-LiFkGLq64Jf1YsnMjbgp2fY1wTDvEsWTKvicplCc3Pa8gbWO6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d0c9a321.mp4?token=QCSTdcMEdCWNFD3dCu2JjzG7fJtiexRdVMwvBvlQWICdF4tcs4zk0Gh2RDFZkQOPAN3UfbHdjYk1aq7E0K3bii4hFdRyWjnU-ZK6oKJp90rFtaLr43a1zpM_h-G2i-Y3F1QvHPiWDm38zBXU3RHZNtFoErpLdp82A9UizPTuAAqx-ZFv4fUISSVydpnSPTbqWe3sj1-dPMIY4xlidKO23kx1JmXbDicrfO1CU4r0ocAfuv8vGqri0BvevT1eCwm9LdJBYRzxr1XmiCjRDmO_7r68CDf0-jzZOjUTdrvllLg48-kIQX4mCmEUW6SMZCIMG0wljs3E66qvSw0pq-rdsC00AFWFgUs6t-bAhE04mFQCYQUlE5FGQyTMqIgF7EYhiPl3z9-UOTh1amyHIGkPo_bmI5PVn_cTFtspbUH0WldlJEKZGbJU05wfHvPumPe6ivnH1DcJnzNHDee-cbQ5TJW_z1XLeQKXXqpFjWZmf8JsdJMaefgdkImMj3wzcxPPwxJDeOyI4EewSnxSkUmGSr9QkTAxCuAt_xEz6efXgfJjEVrZtq0kpdC1ldA79dQ-El22M83F37hIbOAYTpLahCLXDOKVt7xAD6LFTp_v0FQLmLIWLvGEvokz-LiFkGLq64Jf1YsnMjbgp2fY1wTDvEsWTKvicplCc3Pa8gbWO6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل Gemini Omni 1.1 Flash را معرفی کرد؛ ساخت ویدئو تا ۴۰ ثانیه و ارتقا به 4K
🔹
این مدل می‌تواند ویدئو را در چند مرحله تا مجموع ۴۰ ثانیه ادامه دهد و با کنترل فریم اول و آخر، امکان مدیریت بهتر حرکت و صحنه را فراهم می‌کند. همچنین خروجی نهایی را می‌توان تا 4K ارتقا داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/684930" target="_blank">📅 11:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684929">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7KoXb418WIZvWibGNnf7MiPmFDXIqRmly6v6zwZJ6pd42_1BRlHM_Obw7WokvcITmM9mtDwb7Giu_Yf6tgiUCFUY0piMhku_LokgwhFtObSxkqESuZ2rQRQt2NxuQGLhOK-_NFBlT1Uf_zyge_G_raAYrdqpcTQ3I6s-RC886Fd8PhQfUPohdm--ts7QNiHehEATy9wqu2hFfDbxKWlM3yUUw6atPY12WFBQ46qW0Olokf7kEePyyylJ8c-oELXvtjk7LiqSqHK5eglH8AdlSznb0CSRj6pYZvWrBgheVnTQ2XnlVhtGxCSgQsfTMnm-hLKdg-iFr9IU-C5pTR1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پادشاه نروژ درگذشت
🔹
هارالد پنجم در سن ۸۹ سالگی به دلیل بیماری درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/684929" target="_blank">📅 11:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
جزئیات واردات طلا در سال ۱۴۰۵
🔹
تازه‌ترین آمارهای گمرک از افت بیش از ۹۲ درصدی واردات طلا در پنج‌ماهه نخست سال جاری حکایت دارد؛ به‌طوری که حجم طلای واردشده به کشور از حدود ۱۳ تن در مدت مشابه سال گذشته به تنها یک تن در پنج ماه نخست امسال کاهش یافته است.
🔹
یکی از دلایل عمده  کاهش واردات طلا تغییر سیاست ارزی کشور و تمرکز بر واردات کالاهای ضروری تر از مسیر رفع تعهد ارزهای صادراتی است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/684928" target="_blank">📅 11:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684927">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea79380006.mp4?token=Wlpr6hil1fxO05avRMocxMGKW_jtULb6f_6TtDASqHRGJI8p6vm9B8IKzXGdjsqPXxh8UepprW1cThS6Couodv6XYt_LYct0A4v8v_mt9v-_LDiffYODvtzV9ZC2b1Op_5gjjypnw6yBpQnzAvTnSXnq7EXo2g9NtMgc83vMGopZvkgLQgxJ6dzeV2myprF2-MEg2QmxYpX3Yf3YP_mwh-BVhO9f5UWM6idVsHqn6cp2t6ZODqGEMnzue6rV1ebYqpswFlUo1_bCUEVOAoiXrq3D9EIAt3lECWp-6pJyNjrpkuXh5REZMy4k4sWiY6nwqciHF0lejdDTGoN9Tn3S8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea79380006.mp4?token=Wlpr6hil1fxO05avRMocxMGKW_jtULb6f_6TtDASqHRGJI8p6vm9B8IKzXGdjsqPXxh8UepprW1cThS6Couodv6XYt_LYct0A4v8v_mt9v-_LDiffYODvtzV9ZC2b1Op_5gjjypnw6yBpQnzAvTnSXnq7EXo2g9NtMgc83vMGopZvkgLQgxJ6dzeV2myprF2-MEg2QmxYpX3Yf3YP_mwh-BVhO9f5UWM6idVsHqn6cp2t6ZODqGEMnzue6rV1ebYqpswFlUo1_bCUEVOAoiXrq3D9EIAt3lECWp-6pJyNjrpkuXh5REZMy4k4sWiY6nwqciHF0lejdDTGoN9Tn3S8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاوید بدانید کپسول گاز چطور کار می‌کند این ویدئو را از دست ندید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/684927" target="_blank">📅 11:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684926">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-g5i7L9XTrVZrssxgH6YQMbSHbdjK8HKFH8YsjIDmXGhh5RUQCrR7Sizk6ufNnrGv6RbkfhpjYd1RO6eaBWddQ_hZ7RoBZplPLAwDhbmehbV_cg45UhK9nADByWv7jvz8UMlw7c5use293AGto4fA48IHYVs0_B_NdSQQw5zmDRm_n9n9p38G2EnJpee8M48K1bJWmHkHwK8zAgXufEHYPCqizv6klLUfeMJ8lyBNHjLia7YMlhPTWBlWsXBJ-B6cRyjIKbCfgBI67xVSmNwRXw6POzIQjroBBxPu9nhGSBgwVaMwVHN3In9OVTcU1fxOLfgufTMHoqZY-IxC3kBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی اختصاصی خبرفوری با پیتر آدامسون فیلسوف مشهور آمریکایی / «اخلاق»، نقطه ضعف بوعلی/ ابن سینا پدر فلسفه اسلامی است؟
🔹
آیا می توان ابن سینا را مبدع فلسفه اسلامی دانست؟ در این رابطه گفتگویی داشتیم با «پیتر آدامسون»، فیلسوف مشهور آمریکایی که تحقیقات فراوانی در زمینه فلسفه اسلامی داشته است. آدامسون دیدگاه جالبی در رابطه با این مساله دارد.
گفتگوی دکتر حسین نیازبخش دانش‌آموخته دکتری فلسفه با این چهره را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3240744</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/684926" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684923">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سید حسن خمینی: پیامبر اکرم(ص) از مسلمانان نمی‌پذیرد که نام ایشان را بر زبان آورند، اما «رحماء بینهم» نباشند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/684923" target="_blank">📅 11:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684922">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0744a839.mp4?token=eZffljUscXZ9YIaKf5LprnfD4hYYtYW_-im3zv5r1DetZAJAVvDnbSfdJLFa7Fqc-ewNT2kpsdTH3lGqa1H3aTi_whA7uSD5ch-gPDvwLEoQeJzkjEDZOBxfuckZqAwa_FaCRcwswaYV9bw4b8TZT05BSudtjNzwrosg-C2cXikKIvSQniFyy8TjdZyYOnDZDg-RRtPcEtd-lA-FRyadthO3Ai7jJG_mxsplTNRoYKa23Fn5SVwuZA-hIf-foG9IxkG4IE319rRMYmTMKsLrSRqmeftt2xFKY4JgXHKvZrxslLYMaaQi36Dt4oGJ5I38cgKCZM66oy4uyiFJJJtUu2m6KfvcEiWVPYS_exfxAgP4G78ALJU4jOA6P5NKmd3fPKLmCMLw8YVdIEBoE3d0Ojp15qCg5yOG7d363Au3Lqw7JGMsdQLBu71aQ1CoLzpokIeVXULdNh0aC8LEwiy4ycJK9Iqr0pr1AfTbTV0tqlC45gGDMafjY6h1PBwSfZkCXLrzG8FaN9gPIhg9zhVg79MRPudflCS1o0IJ02_66UthT1kir3Zn1oiMC4jSmkaFyUWs2Xj07wckJOsuZF82r2hDHzWLb6Ey7Ud63OYslSYbytK4PKy4dcnjzCnepk_WS-jiFqc4CUkUfVfU9LunAutLBJoNn7wNjtpY3166Vug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0744a839.mp4?token=eZffljUscXZ9YIaKf5LprnfD4hYYtYW_-im3zv5r1DetZAJAVvDnbSfdJLFa7Fqc-ewNT2kpsdTH3lGqa1H3aTi_whA7uSD5ch-gPDvwLEoQeJzkjEDZOBxfuckZqAwa_FaCRcwswaYV9bw4b8TZT05BSudtjNzwrosg-C2cXikKIvSQniFyy8TjdZyYOnDZDg-RRtPcEtd-lA-FRyadthO3Ai7jJG_mxsplTNRoYKa23Fn5SVwuZA-hIf-foG9IxkG4IE319rRMYmTMKsLrSRqmeftt2xFKY4JgXHKvZrxslLYMaaQi36Dt4oGJ5I38cgKCZM66oy4uyiFJJJtUu2m6KfvcEiWVPYS_exfxAgP4G78ALJU4jOA6P5NKmd3fPKLmCMLw8YVdIEBoE3d0Ojp15qCg5yOG7d363Au3Lqw7JGMsdQLBu71aQ1CoLzpokIeVXULdNh0aC8LEwiy4ycJK9Iqr0pr1AfTbTV0tqlC45gGDMafjY6h1PBwSfZkCXLrzG8FaN9gPIhg9zhVg79MRPudflCS1o0IJ02_66UthT1kir3Zn1oiMC4jSmkaFyUWs2Xj07wckJOsuZF82r2hDHzWLb6Ey7Ud63OYslSYbytK4PKy4dcnjzCnepk_WS-jiFqc4CUkUfVfU9LunAutLBJoNn7wNjtpY3166Vug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این روزها ارتفاعات مازندران حال‌وهوای برداشت برنج دارد؛ همه مشغول درو و جمع‌آوری محصول‌اند
🌾
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/684922" target="_blank">📅 11:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684921">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی وزارت دفاع: دشمن از برخی محصولات دفاعی ما کپی‌برداری می‌کند.
🔹
معاون وزیر نفت: بارگیری نفت از خارگ در جنگ ۴۰ روزه بیش از ۱۰ درصد افزایش یافت.
🔹
پیام همدردی پزشکیان با نپال: ایران برای ارائه کمک های انسان دوستانه در چارچوب مقدورات آماده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/684921" target="_blank">📅 10:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684920">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
مسیر جدید صادرات نفت ایران باز شد
مؤسسه HFR:
🔹
آمار اعلامی سنتکام درباره عبور ۷۵۰ میلیون بشکه نفت از تنگه هرمز، احتمالاً نفت ایران را نیز دربرمی‌گیرد. در همین حال، رصدهای ماهواره‌ای از خروج یک نفتکش مرتبط با ایران از منطقه انتقال کشتی‌به‌کشتی خبر می‌دهد؛ موضوعی که نشان می‌دهد صادرات نفت ایران ممکن است همچنان از مسیرهای غیررسمی ادامه داشته باشد.
🔹
سنتکام پیش‌تر اعلام کرده بود نفت اسکورت‌شده هیچ ارتباطی با ایران نداشته است، اما اختلاف میان داده‌های نظامی آمریکا و اطلاعات شرکت‌های ردیابی نفتکش‌ها همچنان ادامه دارد. گزارش‌های اخیر نیز از پایین‌بودن شدید تردد در تنگه هرمز نسبت به سطح عادی حکایت دارد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/684920" target="_blank">📅 10:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684918">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db612e7625.mp4?token=t0o3dn657wIivFXWOO2grRN0svy9bpv_6CCF87UxdANn1JJ5eLB9ExHm9qCnQilgaQmjxtvuDiMAmOZ82gk1meDDpyf9zk113EF7Lg8IlvoCWy3ZZLt5cGcwY4vDFAIycDBF5MFFZgt1oqHReou2UJZ8ODizHW6m3l-aQK94s_YGKYQ-XPE_bf0w2EuJs5LN_kc9Cu_pPHPrOPNJDQYBAeVUXujvwnm3zYjGC-aPHy5-pBx0Q_EJkoP7e3OEJVXri4BM4ncdxONMoVE7xvoPR0-QQKVUqGFxbMSVMGdv1yMU6eUEhstTyUyr4JcxO0l0KZh4dBAF4-ntGF8hL7xn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db612e7625.mp4?token=t0o3dn657wIivFXWOO2grRN0svy9bpv_6CCF87UxdANn1JJ5eLB9ExHm9qCnQilgaQmjxtvuDiMAmOZ82gk1meDDpyf9zk113EF7Lg8IlvoCWy3ZZLt5cGcwY4vDFAIycDBF5MFFZgt1oqHReou2UJZ8ODizHW6m3l-aQK94s_YGKYQ-XPE_bf0w2EuJs5LN_kc9Cu_pPHPrOPNJDQYBAeVUXujvwnm3zYjGC-aPHy5-pBx0Q_EJkoP7e3OEJVXri4BM4ncdxONMoVE7xvoPR0-QQKVUqGFxbMSVMGdv1yMU6eUEhstTyUyr4JcxO0l0KZh4dBAF4-ntGF8hL7xn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان تگزاس قرمز شد
🔹
وضعیت اخرالزمانی آتش‌سوزی جنگل‌ها در ایالت تگزاس، آمریکا.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/684918" target="_blank">📅 10:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684916">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YySDXHZqyOtX4qVNUUPrizzFyTUN5LSKCgqB6Degqhnw5VqPw8mVUGBqJIFQ5rEQA8TOYtkpdJJp-85qsS3tKQUUMCOzoPrCe4y-scyxpoLWmsjdayHndEm_OwRGqwW6jhxUY_tonX_nm0SY4p16S_6d6amUQKK9oriQmIUYokTux_LAmoOmK3rGZim2vcbpLvPkA9Ht0OPJtUZhpZEvmt1FBGvZHMUOf3klc_Ia-cGkozXSq05q4EqXZtqGVV-xLxRrdHTZODEbhQVh34OJKToVWr1o-VwPy8nfYdn8GfiLFgVlLRWvxJMNTRvx6PKljBoixp8ZGviIDXsS_paOtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Awsg6kH0d105sVpZRnulvRQOgu90UNY3INpY8KK5aq14PAMCAX-lNz5VtuifghqRTDBAxvi9jE0avwP-NSqs4yjMsx-V3Qy48_drnUpnpQVfH2cXf-b_kPtgFkLQ1WqSFVJX9lCCIVMwQhQJaXUR6wVAN_oh6EbaqXyvHw4ckrZT-B3ZShvQQUqb5SFeVqRRjv7vrduUfT1L9dK_tR_gaT72PNbSygd1BVP_P1-dvmIn8tMnIS4r07RcyE0hvYQjTVyAZGJ9Z1cmMAMfS4XzLZQ6qtQB7B9tqHdYUOFls2QBDl7MPChgWUSm74DL1fw0rEPmxGrGoMuq1mdIBwntRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/684916" target="_blank">📅 10:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684915">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5a093105.mp4?token=IR1eHxRmecjJqBNyZT1c69MhEZ2PWIqwSAUqSxMVZiHTqoQLpvq3UCfqaVjsH-A9bJVTsQqLsHMB0Z6CSBRYlTuql8ejVzEb9HXkA4eeJZWR6pXj_NxI4OfRyRfT6XYxiFCibOUmwSNVpDFVrhNkMT8tN0z_ePVntrOAzVGmDiRPtTqVcPxFUdoeQm3pGr5nSYqfXTVLkGAaljaA1ZXBq7hE7mJqV7EwcZRV7iV6CGcrGwogfyc5JjwccfEyzMm4pkZAzTg__OUcKOFR9izMp-rhvno01bWZmPHURr3sbDNMU3keHkEM6AMSNAmB5ISLhplRD5hKFuf3b-rei3fC-EqzPCJLzhjIvvtCruCKZKyUqKNB7TSKsh6QuvjJiaJCyV_vbJPl6pWwHU5NuNeG3Vl74XrHEqqW10GkZbJGVVZEfN8wgd9y7ZSA8cmRh7y5atZG3zIOVmt0bnz00lvWQaKY8_BIuoIcE_CXjitjdLdKEuztt1FUhp03hjQQebZCXZGMPzvxGDtWCZGen3gUFOpb0m3XTQAjljZh_19rTzR-7yYHxOBzq2n1f67Xg3SblV_6YZjvZI04BAr4hgrOg4XKRLXHaZeLoYfVDIeeB0LyADHM9t6wTJYyk75b5TaAJFngRgd-x3W41gY6U4crFNBcYxd4rhPy1M5PNncQjBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5a093105.mp4?token=IR1eHxRmecjJqBNyZT1c69MhEZ2PWIqwSAUqSxMVZiHTqoQLpvq3UCfqaVjsH-A9bJVTsQqLsHMB0Z6CSBRYlTuql8ejVzEb9HXkA4eeJZWR6pXj_NxI4OfRyRfT6XYxiFCibOUmwSNVpDFVrhNkMT8tN0z_ePVntrOAzVGmDiRPtTqVcPxFUdoeQm3pGr5nSYqfXTVLkGAaljaA1ZXBq7hE7mJqV7EwcZRV7iV6CGcrGwogfyc5JjwccfEyzMm4pkZAzTg__OUcKOFR9izMp-rhvno01bWZmPHURr3sbDNMU3keHkEM6AMSNAmB5ISLhplRD5hKFuf3b-rei3fC-EqzPCJLzhjIvvtCruCKZKyUqKNB7TSKsh6QuvjJiaJCyV_vbJPl6pWwHU5NuNeG3Vl74XrHEqqW10GkZbJGVVZEfN8wgd9y7ZSA8cmRh7y5atZG3zIOVmt0bnz00lvWQaKY8_BIuoIcE_CXjitjdLdKEuztt1FUhp03hjQQebZCXZGMPzvxGDtWCZGen3gUFOpb0m3XTQAjljZh_19rTzR-7yYHxOBzq2n1f67Xg3SblV_6YZjvZI04BAr4hgrOg4XKRLXHaZeLoYfVDIeeB0LyADHM9t6wTJYyk75b5TaAJFngRgd-x3W41gY6U4crFNBcYxd4rhPy1M5PNncQjBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین؛ وقتی حتی انتخاب توالت خالی هم هوشمند می‌شود
🇨🇳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/684915" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684914">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBYI3aHc92gETh7C8_Dvaq6BOjDs_nWh1v5gCE9c9lnwlIxRTM2iEZBehp1STnrvlVZYv6PYoiJxrM9F5HvoM1gfcT1sheagWmiwkZ5-C9JC25absGECGSFskxvvo8DCZ0OpY870YQZH1qqG_Vpleb6rPmT0ggdSrXTwjF5S5mxmf40VLxH4K-_gJ_1bd3ttwbQ1KiSIt0XHhEDXMFJT5t45pgKjUa5wuZZsWF8SPmd0MvHayMZwUFkiuGTvt6Ac9P5zEfzdtn9cfksccmlNZZu-yoyYJIzXRxRXY_lLztuQOPEU57vDGpxav4OYQ83wNI14JhtXSgqPjZju4aVPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران در آستانه تغییر استراتژی | چرا تهران ممکن است دست به اقدام نظامی بزند؟
🔹
فارین پالیسی در گزارشی مدعی شده است فشار اقتصادی و محاصره دریایی آمریکا علیه ایران به مرحله‌ای رسیده که تهران ممکن است به این نتیجه برسد ادامه «صبر راهبردی» دیگر امکان‌پذیر نیست و برای تغییر محاسبات واشنگتن، به اقدامات تهاجمی‌تری روی بیاورد.
گزارش ترجمه گزارش فارین پالیسی را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3240844</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/684914" target="_blank">📅 10:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684913">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3dda99bcd.mp4?token=U2Y9TU7Y-yyATHsgCYTf2YHfRv3dwf9x1_qOyszAqgGrZPxlo7IFnsDuEb_8Q929qXUB7BlgUCx3BIxs66pdUyK42xLd93CPCNJCYzBX3HONW3AdJ7vphklBDTSxNRQ1Bdz-9AOWruBGtFMZBG86ULTI2Ys_M5q1wSL2IgJdcgojn_Z655645pDYmLy5kN4MqxNotMHHbF2JP-mq6XbNxUZJSm6W7HH4WA0aGxtWPt-23XnYzeqgiBZndyoz2HyFNpRjImKYwuoC34NqykO6TjYP3rhLbZfssWirEbB_RAa41bbjBBe6ZnBjaRpAhty2swMXN7e3wYt8I1X-XqkVslJTqpUdblVxqEC2IfoNi2_-xJbWCjR1vGSCt8EGl2SCXV04oDOn8UPO1xnhLhcQ0vEJ5yFbamjisx11EXbYZtHm116RkCJ158h2V0Fl3snEtD9MBqVJJ5ZW9DFRoxrKfpVUw4Ha2cZx1rwXIVY0LXljZGopFqlUdT0RfYtuALzDCfh4GOzqZPK1k_EyPgnga7SVv3K79X-0gd9K87I17mh2Ca0YzhDPZv8asDzeuPv_8dwTEvVYuvz0cLbMZbhvH0IfuZ0JgXdCC7AN1ips63Ycn7S6mPbKV0YBkRdjwlVaT9RvXlFb-jRRFrPx5otXkiIuy8IVBgd1j1Kmq9LI2bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3dda99bcd.mp4?token=U2Y9TU7Y-yyATHsgCYTf2YHfRv3dwf9x1_qOyszAqgGrZPxlo7IFnsDuEb_8Q929qXUB7BlgUCx3BIxs66pdUyK42xLd93CPCNJCYzBX3HONW3AdJ7vphklBDTSxNRQ1Bdz-9AOWruBGtFMZBG86ULTI2Ys_M5q1wSL2IgJdcgojn_Z655645pDYmLy5kN4MqxNotMHHbF2JP-mq6XbNxUZJSm6W7HH4WA0aGxtWPt-23XnYzeqgiBZndyoz2HyFNpRjImKYwuoC34NqykO6TjYP3rhLbZfssWirEbB_RAa41bbjBBe6ZnBjaRpAhty2swMXN7e3wYt8I1X-XqkVslJTqpUdblVxqEC2IfoNi2_-xJbWCjR1vGSCt8EGl2SCXV04oDOn8UPO1xnhLhcQ0vEJ5yFbamjisx11EXbYZtHm116RkCJ158h2V0Fl3snEtD9MBqVJJ5ZW9DFRoxrKfpVUw4Ha2cZx1rwXIVY0LXljZGopFqlUdT0RfYtuALzDCfh4GOzqZPK1k_EyPgnga7SVv3K79X-0gd9K87I17mh2Ca0YzhDPZv8asDzeuPv_8dwTEvVYuvz0cLbMZbhvH0IfuZ0JgXdCC7AN1ips63Ycn7S6mPbKV0YBkRdjwlVaT9RvXlFb-jRRFrPx5otXkiIuy8IVBgd1j1Kmq9LI2bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شبکه‌های اجتماعی چطور مغز ما را به دنبالِ محتوای بیشتر می‌کشانند؛ پشت پرده چه اتفاقی می‌افتد؟
🧠
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/684913" target="_blank">📅 10:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684912">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWJ5mYy5t-PISr2-r3yPJduKpXBioU6c3sOxWoar3xKeXbi11zLIYOE5lfSUSMBERo0CpNZGOtppcyG_J4fUtn6n978ezVvjicD_chjG8G0xBfQUFU5sM0-tTGlU5q60oJ2TpXOHFr6Np6nHN4NHkOnaTAeW9IRv9I8MEuLd97GVnAABm7CCC9133N0HgmOWBy9lS0POT6jsTERXJ2LFzYG2caC8GXuHtYEphRedpgpqucsLxIHRspFgkfFGRCGT1elDab3foZoBTROBEJlULiDxcG-mIFdoC_luLHHrIf81KXHXZwo98YPVbQhXhm9vbGrXNGP4aScyg1jN2lI1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی، وزیر امور خارجه: آمریکا باید یک واقعیت ساده را درک کند؛ فشار نتیجه نمی‌دهد
پیام وزیر امور خارجه کشورمان پس از سفر دیروز نخست وزیر قطر به تهران:
🔹
بازگرداندن دیپلماسی به مسیر خود ناممکن نیست. این امر به درک یک واقعیت ساده از سوی آمریکا بستگی دارد: فشار نتیجه نمی‌دهد. آمریکا باید اعتماد ایجاد کند، با احترام سخن بگوید، حقوق ما را تصدیق کند و به تعهدات خود پایبند باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/684912" target="_blank">📅 10:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684911">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSjtM0syvxhA78iHcK-zao0CNcijKe-Ynpb6NkVaULfXl48H62SdF39raU10cq4Pd0DoT3_JWXe-UL7nQEEO179jJrWfXMnxr3XIu5VZY8ylroXm13nGOb3RB1yQ03vIgK5I4V0Rn54XOqVfxxCS8XSYm5N07wyA0RzbFb2CaUooEkiyuQ5zxisxZWYZXmBVsT1HBF09PUHP28iMSh6_nhGZcHF2l8c6GLDzEJMJ891pOnZefUz1iObrcDexJUp5-kXD-xOefEmgu0Q-yr-LXrjpx6Yy37XKhUXzbmaR6VW-0Ftxa8gBF4HgL8WEjH5TZxC4LsNHUA99DZHQq2xxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ایران و قطر درباره ایجاد کریدور موقت کشتیرانی در تنگه هرمز، پاکسازی مین‌های دریایی و کاهش تنش‌های منطقه‌ای رایزنی کردند؛ هم‌زمان تلاش‌ها برای ازسرگیری مذاکرات تهران و واشنگتن ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/684911" target="_blank">📅 10:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684910">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/066a83d9ce.mp4?token=nPj2tYXx9HnVDIR0NYUxN5jOtzd_ieCe_vkx3eeKMhTZEV4aDftJA41KwmrPH9xyqZO_ceWsSeK1y7-gQ0TRaJPVw3Grn6vWCUSN4-oWGWxwgSK3KGWXmzA_1qmUq_yHF4ZY3WZvhxNiGHIuxDv_BFD-PrsI3m3WqiUHIfiCKFCuHvnXYse7gwIfIsXuEsvqsvi0EkKcc0h80-AGyWbWaKfGOw1FK5Al9QD51Ytvpvn5IXcWsK_3oesHKwee1omucKEj5HDGc7mnHeTOcxZ7AiRLMIVpqjxMg1Ei1YFuXwVUEMApAHjtfVk9vk_RI_aKExRc8hDy3ERMM_wPta1p-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/066a83d9ce.mp4?token=nPj2tYXx9HnVDIR0NYUxN5jOtzd_ieCe_vkx3eeKMhTZEV4aDftJA41KwmrPH9xyqZO_ceWsSeK1y7-gQ0TRaJPVw3Grn6vWCUSN4-oWGWxwgSK3KGWXmzA_1qmUq_yHF4ZY3WZvhxNiGHIuxDv_BFD-PrsI3m3WqiUHIfiCKFCuHvnXYse7gwIfIsXuEsvqsvi0EkKcc0h80-AGyWbWaKfGOw1FK5Al9QD51Ytvpvn5IXcWsK_3oesHKwee1omucKEj5HDGc7mnHeTOcxZ7AiRLMIVpqjxMg1Ei1YFuXwVUEMApAHjtfVk9vk_RI_aKExRc8hDy3ERMM_wPta1p-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساندویچ نیمرو، یک ساندویچ خوشمزه و ساده برای صبحانه
🥪
مواد لازم:
🔹
۲ تا تخم مرغ
🔹
۳ ورقه بیکن
🔹
۲ ورقه پنیر
🔹
کره ۱ قاشق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/684910" target="_blank">📅 09:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684909">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mETuK3mEtNuEgHdmaB6yFbyV6P1NdELBpKa2JAx2Qhnv3fEZOVxGBEj0JI6Nu7CAy4SCMg9gNHZnxMRckh3s1KM7xNSHF5adXrbmP7EM1gILsaZhFuXcKekAgaiwm5aYk-QQtyg6lU9EEC2aFVDFWISeb0tGPsfffcAgoWjk2EQZ2ZxXC5LfqoUCkk-6kBCt_F_yR9hYJc6EZq7KWOAtCSLKsTzBibc7lWX9JQ8M20mRKd79zIbC9vPWd91R3dxMtAgto2_WmkbmxJCCF9z4D2e7yaqNt_LZ6qeH9HUwApxVYCQEFgx_EEysKdpdO_kA4FJJOxJgP9kZSUro59RWXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ فرمان اجرایی تغییر نام دریاچه انتاریو، دریاچه‌ای که با کانادا مشترک است، به دریاچه آمریکا را امضا کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/684909" target="_blank">📅 09:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684908">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e131570ad5.mp4?token=JR0SUool9BWAz4Dz-pZ2wd8OWpePwIhl6rnX9ccGhENDP8NWFLPxfGjm8bygjHYsKAuQXhzzwHCGBh4SAqMiAg1LAoQl2lqv8a3VfXzFIVloFxE-QnxZVYf5ykRb4jfGHgVPu6FzHTLWwxxlQJdwltu9NauoaDXzD4Js1NWeYGtivZjhpCun7iO_bpq_6DOkioyio49ATW0hVYhKJjDpG9Sf6_uhAVveTiECiZjB-elMvC6ZnAAm_rk_Wr8lgo1bOh-XNL6QY_lRzUOGSyjZWruk-fDZB3GqvA-LvzgxvEjUSftMNeJC03L8_NdTgNKOHD8F76gDQStd5LOSzhiR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e131570ad5.mp4?token=JR0SUool9BWAz4Dz-pZ2wd8OWpePwIhl6rnX9ccGhENDP8NWFLPxfGjm8bygjHYsKAuQXhzzwHCGBh4SAqMiAg1LAoQl2lqv8a3VfXzFIVloFxE-QnxZVYf5ykRb4jfGHgVPu6FzHTLWwxxlQJdwltu9NauoaDXzD4Js1NWeYGtivZjhpCun7iO_bpq_6DOkioyio49ATW0hVYhKJjDpG9Sf6_uhAVveTiECiZjB-elMvC6ZnAAm_rk_Wr8lgo1bOh-XNL6QY_lRzUOGSyjZWruk-fDZB3GqvA-LvzgxvEjUSftMNeJC03L8_NdTgNKOHD8F76gDQStd5LOSzhiR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های بدل ایرانی آنجلینا جولی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/684908" target="_blank">📅 09:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684907">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4d96d2e7.mp4?token=ONX6ptJ2GsRxi7j1qKtjAePX0znOGoldTm3SNJSL9C2mLSqyO8lV2CKCS9EWjFcjtNx9jr7cLTrSFqiznhEWJ7JvVCTYZ3sTiKjAB4GkTmESWIl4gQtGkZ9u92pTDP4-toxlM9apKZudIU-l67oUTUzFCcjUPFapUzlL40i6JYrYAQZFkARbhCFxXFC3kvFFqjT4upv7f2tlK03-bsMVrXB9YgiROFe9DtsFBzKzDSob_xuEnzZ-LxdBEp9CnKSY8RM5xlIh5mg9-YSPQryFwUZkzVshrOKQ-P5z3lIALoEj-oyZxx_ZjBx1VZgDmwjaDHEaehvA2WT9HLqypg1BOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4d96d2e7.mp4?token=ONX6ptJ2GsRxi7j1qKtjAePX0znOGoldTm3SNJSL9C2mLSqyO8lV2CKCS9EWjFcjtNx9jr7cLTrSFqiznhEWJ7JvVCTYZ3sTiKjAB4GkTmESWIl4gQtGkZ9u92pTDP4-toxlM9apKZudIU-l67oUTUzFCcjUPFapUzlL40i6JYrYAQZFkARbhCFxXFC3kvFFqjT4upv7f2tlK03-bsMVrXB9YgiROFe9DtsFBzKzDSob_xuEnzZ-LxdBEp9CnKSY8RM5xlIh5mg9-YSPQryFwUZkzVshrOKQ-P5z3lIALoEj-oyZxx_ZjBx1VZgDmwjaDHEaehvA2WT9HLqypg1BOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید حسن خمینی: پیامبر اکرم(ص) از مسلمانان نمی‌پذیرد که نام ایشان را بر زبان آورند، اما «رحماء بینهم» نباشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/684907" target="_blank">📅 09:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684906">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2dd134cd.mp4?token=KwSuB-E-ZkjQGfsyznDKaHYZmDmbk4sqhGWyGItU1NB1TeSP8iOjsF-JP7Lz6kDi-UDAhHohqB9QY6PSlBL3uQxBOA2K7UzuKfLeCNXoT0rXzRDezexkDhIFDQgsF6KJIggmfynjUSyKKGci4RDh4oLsH41QE5qQVfBP08jXI-xPsircStB9RrrL-kF_9BLzuQRFUmDkhtOlBrXy-2kdRJjyleGNwyadSZ1mnCL58DJJaneurmdG4vooAVuKYpsa9rShtCvdfGXqzMF6Q_9XmIm-4Jf8q8da0tuixDemOVIio95K1xKJ6zZoO-SV--gNi9Ox4vvIm1RBb5sBbg5U1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2dd134cd.mp4?token=KwSuB-E-ZkjQGfsyznDKaHYZmDmbk4sqhGWyGItU1NB1TeSP8iOjsF-JP7Lz6kDi-UDAhHohqB9QY6PSlBL3uQxBOA2K7UzuKfLeCNXoT0rXzRDezexkDhIFDQgsF6KJIggmfynjUSyKKGci4RDh4oLsH41QE5qQVfBP08jXI-xPsircStB9RrrL-kF_9BLzuQRFUmDkhtOlBrXy-2kdRJjyleGNwyadSZ1mnCL58DJJaneurmdG4vooAVuKYpsa9rShtCvdfGXqzMF6Q_9XmIm-4Jf8q8da0tuixDemOVIio95K1xKJ6zZoO-SV--gNi9Ox4vvIm1RBb5sBbg5U1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یکی از شگفت‌انگیزترین نمایش‌های طبیعت در ایتالیا
🔹
هزاران سار در آسمان ساردنیا با حرکاتی کاملاً هماهنگ، موجی تماشایی و خیره‌کننده می‌سازند؛ پدیده‌ای که به آن
Murmuration
می‌گویند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/684906" target="_blank">📅 09:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684905">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90252b3297.mp4?token=rdhdcRlnOpnBBG4CLuY5W3ZiHVCy-prN4JS3gepXFEvreH0MsTU9B6ZcDyhyUIE1dC5tLgmk7YqOpvDJtDaAa6fcgEFtaQN94A2u4D8rVVeYAUkB6nGfr5g-l4KK9053wrHFIgdibNf_KU0ZcY88OUib9KxkEYLX40QuAMb2T0LaklYxisGIA14AUBj0J1txIdUMZk5L_HUzEMD-WY4m-iStwnu87FL3xJZh0uOZCj8wejinztXVqo9mXYLM1JHbL7-VscIx6d7sWv-8Gcgmz2BcqvnpgGrZGVHNLd3C_jq9WcTx1Cn5jhLU87P4L848Kl6KZ93OVOhJPOQsq2D16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90252b3297.mp4?token=rdhdcRlnOpnBBG4CLuY5W3ZiHVCy-prN4JS3gepXFEvreH0MsTU9B6ZcDyhyUIE1dC5tLgmk7YqOpvDJtDaAa6fcgEFtaQN94A2u4D8rVVeYAUkB6nGfr5g-l4KK9053wrHFIgdibNf_KU0ZcY88OUib9KxkEYLX40QuAMb2T0LaklYxisGIA14AUBj0J1txIdUMZk5L_HUzEMD-WY4m-iStwnu87FL3xJZh0uOZCj8wejinztXVqo9mXYLM1JHbL7-VscIx6d7sWv-8Gcgmz2BcqvnpgGrZGVHNLd3C_jq9WcTx1Cn5jhLU87P4L848Kl6KZ93OVOhJPOQsq2D16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاجعه‌ای هولناک در نپال؛ مردم و خانه‌ها زیر ده‌ها متر سنگ و یخ مدفون شدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/684905" target="_blank">📅 09:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684904">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: نتایج اولیه کنکور احتمالاً ۲۶ یا ۲۷ شهریور منتشر می‌شود.داوطلبان پس از اعلام نتایج تا ۵ مهر فرصت انتخاب رشته خواهند داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/684904" target="_blank">📅 09:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684903">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35f756cbeb.mp4?token=KkAPAWdf3vP_rV0sJJBBxzpP0YlSdeJlfAeLTHkTB6CiYy2SpDXlhW-yrSY68Xi74zDPg3XfDamK_ZZIRaDA5DQkcGDYBGtVSb9uashIzs8wHyohuLtcG_bDDolZ2ozJv53GIE2pkKeEdBkjivp7Zs7U5Z0Am3dLnhkxyJ9MzjhD9dTFY1BU8FGl1o5KYYj6huqMvpwpvhri-5COJ70DQqXoQGdcTdxR1DqZjrd_UvRWR4SjshExfAExQEk0aNAIkV068tHzs3CVutnhXx8ITkUd7_xbzDdsePuBZOoJxU1cr3Cc9Gy1ijuLQO2QAIzTWz7jp_CEglqKKGkQ9Rz2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35f756cbeb.mp4?token=KkAPAWdf3vP_rV0sJJBBxzpP0YlSdeJlfAeLTHkTB6CiYy2SpDXlhW-yrSY68Xi74zDPg3XfDamK_ZZIRaDA5DQkcGDYBGtVSb9uashIzs8wHyohuLtcG_bDDolZ2ozJv53GIE2pkKeEdBkjivp7Zs7U5Z0Am3dLnhkxyJ9MzjhD9dTFY1BU8FGl1o5KYYj6huqMvpwpvhri-5COJ70DQqXoQGdcTdxR1DqZjrd_UvRWR4SjshExfAExQEk0aNAIkV068tHzs3CVutnhXx8ITkUd7_xbzDdsePuBZOoJxU1cr3Cc9Gy1ijuLQO2QAIzTWz7jp_CEglqKKGkQ9Rz2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ثبت شده از «شاه روباه» در بهاباد
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/684903" target="_blank">📅 09:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684902">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e642dbf9f.mp4?token=NrbVDtzO6eCjN7_xe5QNggf3j4tP9GM9Z7-5ATFYGBgMBafFjpOOz3nTvWuR5Fq48roryvZs5wLg1m190EOG0o1eY0SmWHam_hJWVB2J04NjAIhXrpZv5qwyfPfKStCtkrSCJJRm9oAf-XdExiI8htxfqOiz3FS-mAD-0XC5T5qdYv_vg0BpWsk8wbvGdjTtg9W-jngZ_NH-cuJhD-7rB3Wuhr7g2Cy-FnzoU8CNnNVUQuI5NUkXZMVWnwfHvrXPkZYFBiyTX1PmIqj_mlOum7p6IYFp3lW68IjAgUTCLbbU2wpFfxcZVHUc0a1slMnt2pcv6gY94fUvSV7oapHQyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e642dbf9f.mp4?token=NrbVDtzO6eCjN7_xe5QNggf3j4tP9GM9Z7-5ATFYGBgMBafFjpOOz3nTvWuR5Fq48roryvZs5wLg1m190EOG0o1eY0SmWHam_hJWVB2J04NjAIhXrpZv5qwyfPfKStCtkrSCJJRm9oAf-XdExiI8htxfqOiz3FS-mAD-0XC5T5qdYv_vg0BpWsk8wbvGdjTtg9W-jngZ_NH-cuJhD-7rB3Wuhr7g2Cy-FnzoU8CNnNVUQuI5NUkXZMVWnwfHvrXPkZYFBiyTX1PmIqj_mlOum7p6IYFp3lW68IjAgUTCLbbU2wpFfxcZVHUc0a1slMnt2pcv6gY94fUvSV7oapHQyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: فاکس نیوز گزارشی نادقیق درباره جمهوری اسلامی ایران منتشر کرد/ قصد ندارم با ایران مذاکره کنم و این تهران است که خواستار توافق است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/684902" target="_blank">📅 09:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684901">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe37e0bf89.mp4?token=kguSjCvbInYmWcHiZh5mfrQ3g9f8X0XlAhjysbtJ3bc_OkMCuJP4-_4nHT61Ou9iekUB40Bksc1ZejAziS29VK_gmlFC5eVhdkJCR-LcLtehC77FRos1qV2Jj0yHMI2vQVvB8PZ197jVWxD4QQBF6OvywBNUosT9mhtYbnvE4kwjLOAjoi3uvg1MHoII_i2BHmmrdY6UPHnJyLIwovSmTZIe9iBFuOMRfqmwZXC7QhXAkBgcOkKPl8rcWd2zcLfQbel1vBR5Yty1U5JrEVNLDXZ_Mwz6dtcFoYpXD8_s87QIaHzxIyzjITPq10wGhh2rkn5jf1v0FoqVeV_eBC-yQXaFIHP1BYrT6yR2SLvw-kuKdSAwUTomu8WN8PDp9vbue0TQnwy41lUHYaOKK7Yqi40aIYCoMhi8VQHDqqcE9A14h7T2y7qiqgDfTE30adzZKSES24I95eiaKTzqKfzwT8ij29pkEQtf5uDFzbB91310Ias4Yt4PUeFbufb-WXyHOHpN8mZ_q3Oap8-uukjQY-hhcsg_XGxslzRr0gTB22wK7ILx4fV1p0OdR-qiRaNSELoymxjadXQpDbaTzRQQu5-TV_NwoiIiM-DvJ6WIxJPDpEJt8dhYIa6iYf4XhrdHO8zmTyOqiSwOZm_dtQw_F7GKDWZT9E-NI2ewMrZqmNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe37e0bf89.mp4?token=kguSjCvbInYmWcHiZh5mfrQ3g9f8X0XlAhjysbtJ3bc_OkMCuJP4-_4nHT61Ou9iekUB40Bksc1ZejAziS29VK_gmlFC5eVhdkJCR-LcLtehC77FRos1qV2Jj0yHMI2vQVvB8PZ197jVWxD4QQBF6OvywBNUosT9mhtYbnvE4kwjLOAjoi3uvg1MHoII_i2BHmmrdY6UPHnJyLIwovSmTZIe9iBFuOMRfqmwZXC7QhXAkBgcOkKPl8rcWd2zcLfQbel1vBR5Yty1U5JrEVNLDXZ_Mwz6dtcFoYpXD8_s87QIaHzxIyzjITPq10wGhh2rkn5jf1v0FoqVeV_eBC-yQXaFIHP1BYrT6yR2SLvw-kuKdSAwUTomu8WN8PDp9vbue0TQnwy41lUHYaOKK7Yqi40aIYCoMhi8VQHDqqcE9A14h7T2y7qiqgDfTE30adzZKSES24I95eiaKTzqKfzwT8ij29pkEQtf5uDFzbB91310Ias4Yt4PUeFbufb-WXyHOHpN8mZ_q3Oap8-uukjQY-hhcsg_XGxslzRr0gTB22wK7ILx4fV1p0OdR-qiRaNSELoymxjadXQpDbaTzRQQu5-TV_NwoiIiM-DvJ6WIxJPDpEJt8dhYIa6iYf4XhrdHO8zmTyOqiSwOZm_dtQw_F7GKDWZT9E-NI2ewMrZqmNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راه نجات نیرو دریایی امریکا اگر غذای خوب میخواهد!
🔹
تسلیم بشوید و به‌عنوان اسیر به ایران بروید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/684901" target="_blank">📅 09:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684900">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b218b16187.mp4?token=n4VlfbiCCCk6sc8iCtYsPJWzP7GNBN1Uism9S9l_5C1g4URCWSMq_Hg6ojgbqNoPjs9cI4H-DIG8wC0pKRVijpQed_4gj0J0317_FopoKvtrOK31hNXVWAc8USiSXNvO3rdER8wTv9mMuYoxOusLhIC7OqmyXNHucXXanPz52p9P2ZcSUk9UnAS4XM2_v3gM3UiBl5r_AvwwWcrUbcn3RFufUveX9zcR_BV732wk5MIVVjJtWqG7YNA6QuiEvEbLaVshB_YS3ZXsfkLJStw4Ypp7GKVsi7opVEITaC7deMFIHVxIiML-Df048pSypENOLKTVI--VNlE7StSt2JYAsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b218b16187.mp4?token=n4VlfbiCCCk6sc8iCtYsPJWzP7GNBN1Uism9S9l_5C1g4URCWSMq_Hg6ojgbqNoPjs9cI4H-DIG8wC0pKRVijpQed_4gj0J0317_FopoKvtrOK31hNXVWAc8USiSXNvO3rdER8wTv9mMuYoxOusLhIC7OqmyXNHucXXanPz52p9P2ZcSUk9UnAS4XM2_v3gM3UiBl5r_AvwwWcrUbcn3RFufUveX9zcR_BV732wk5MIVVjJtWqG7YNA6QuiEvEbLaVshB_YS3ZXsfkLJStw4Ypp7GKVsi7opVEITaC7deMFIHVxIiML-Df048pSypENOLKTVI--VNlE7StSt2JYAsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رهبر شهید انقلاب از حضور شجاعانه حاج قاسم سلیمانی در منطقه‌ای که ۳۶۰درجه در محاصره دشمن بود
🔹
انتشار به مناسبت ساعت شهادت حاج قاسم سلیمانی و یاران در فرودگاه بغداد در ۱۳دی۹۸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/684900" target="_blank">📅 08:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684898">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697546267f.mp4?token=q7n450rY_hnENwBKrSiHgkkfZLHDZAZUaZUZmgmR22-OCOivXmbVPHgVv8Tv9cMwV65DR1aNbiojQ3gXTR_EF1-oTxaelr7n9Knt3qEHKqFYneFgYSyreiRGQrqUPpi_Vf0ynyP93fP25p3YeVQqxbDxvAljgenHDUSceKetfk9oG-kwDQRP9UTJES_2Nr15W9QakOSa0ZITBN7zC-1h4bQVhM5uuzSZDWs5KhjwlpRFZieHgPHSSbsD8W2cUTdcy6NvkSDQ32z_GlPmyzTKjgp-hndYypxmyFkVyW6uFkKj0RLxyv4tWywcJWT6VCh_ITT6evNu4P1UCQvEbsHGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697546267f.mp4?token=q7n450rY_hnENwBKrSiHgkkfZLHDZAZUaZUZmgmR22-OCOivXmbVPHgVv8Tv9cMwV65DR1aNbiojQ3gXTR_EF1-oTxaelr7n9Knt3qEHKqFYneFgYSyreiRGQrqUPpi_Vf0ynyP93fP25p3YeVQqxbDxvAljgenHDUSceKetfk9oG-kwDQRP9UTJES_2Nr15W9QakOSa0ZITBN7zC-1h4bQVhM5uuzSZDWs5KhjwlpRFZieHgPHSSbsD8W2cUTdcy6NvkSDQ32z_GlPmyzTKjgp-hndYypxmyFkVyW6uFkKj0RLxyv4tWywcJWT6VCh_ITT6evNu4P1UCQvEbsHGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام ۳ روز عزای عمومی در الجزایر به‌دنبال آتش‌سوزی‌های مرگبار
🔹
در پی آتش‌سوزی‌های گسترده در مناطق مرکزی و شرقی الجزایر که تاکنون ۱۲ کشته و ۵۴ زخمی بر جا گذاشته، دولت این کشور سه روز عزای عمومی اعلام کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/684898" target="_blank">📅 08:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684897">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a73fbaa8.mp4?token=mGK0yweQWZXS6rAiiuz8FYAKwnPZM3S0MMml2iUwT67_9QgHnMhamLwGm9lIXK4EvMO-7SCunmsSSO7A4mryXL_ii04n4hXGuRX3PQxt9hkqS0jf_Gs5R7sZmFjtUgBYgBmag5_Pauu4o57gfL7Ab-Mn7kdQb9ni2i5K4sJRttL_L3-EoTlBm0OujhYuPo24bMedJXIPf81DqIRthuiUMohmGfksdDxeSfeGNgtRfF20rfaxHVG3PAw13Pbj-AWUcVaPqqzqlqiM6iGNXqpEB14GwmyimVpfCc5qrrNNkImApWBbPWnzvkJERJKxqGLN2ytIz3UnMfpBoovJH2nqGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a73fbaa8.mp4?token=mGK0yweQWZXS6rAiiuz8FYAKwnPZM3S0MMml2iUwT67_9QgHnMhamLwGm9lIXK4EvMO-7SCunmsSSO7A4mryXL_ii04n4hXGuRX3PQxt9hkqS0jf_Gs5R7sZmFjtUgBYgBmag5_Pauu4o57gfL7Ab-Mn7kdQb9ni2i5K4sJRttL_L3-EoTlBm0OujhYuPo24bMedJXIPf81DqIRthuiUMohmGfksdDxeSfeGNgtRfF20rfaxHVG3PAw13Pbj-AWUcVaPqqzqlqiM6iGNXqpEB14GwmyimVpfCc5qrrNNkImApWBbPWnzvkJERJKxqGLN2ytIz3UnMfpBoovJH2nqGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان یخچال‌های باستانی ایران؛ چطور ۲۴۰۰ سال پیش وسط کویر یخ می‌ساختند؟
🧊
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/684897" target="_blank">📅 08:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684896">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
جریمهٔ دیرکرد بیمهٔ شخص ثالث بخشیده می‌شود
معاونت اجتماعی و پیشگیری از وقوع جرم دادگستری استان تهران:
🔹
بخشودگی ۱۰۰٪ جریمه دیرکرد بیمه شخص ثالث تا ۱۳ شهریور؛ رانندگان دارای وقفه در بیمه، تا این تاریخ فرصت دارند بدون جریمه، پوشش خودرو را بازگردانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/684896" target="_blank">📅 08:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684895">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76e95ae51f.mp4?token=eSw94ZgBD1t_a6aTTiWkai6geY0yNeuZq0ML-TANCd4cO2rU8JePc-YVSd7hkX2o5mPsiyz4SeDEzOG4Q3Mj7bFpig8r9aI_bcBr_mAxVb3wn183AnHAsDVmu8EGYxXPZwvTrheqf00JOhfli7RiGA_wU4QyDTXrstbPoM9PW3uKbta-9Jx7EMW3Tp4hVM1AWxeX93Ms5TU-4pG-lxtOPV5Z9qeRkl7pUo_UXfgeHZPimMBBU_fqw-ZsFLp6J4F2g4iH8euKAoFfEjLuB42S9WNXvjsTwt-JFP7FElssDtSbiPtlZX6z5PswL5E_l3xa2wbGRsgiow9DJdHY_IL6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76e95ae51f.mp4?token=eSw94ZgBD1t_a6aTTiWkai6geY0yNeuZq0ML-TANCd4cO2rU8JePc-YVSd7hkX2o5mPsiyz4SeDEzOG4Q3Mj7bFpig8r9aI_bcBr_mAxVb3wn183AnHAsDVmu8EGYxXPZwvTrheqf00JOhfli7RiGA_wU4QyDTXrstbPoM9PW3uKbta-9Jx7EMW3Tp4hVM1AWxeX93Ms5TU-4pG-lxtOPV5Z9qeRkl7pUo_UXfgeHZPimMBBU_fqw-ZsFLp6J4F2g4iH8euKAoFfEjLuB42S9WNXvjsTwt-JFP7FElssDtSbiPtlZX6z5PswL5E_l3xa2wbGRsgiow9DJdHY_IL6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت استیکر در ChatGPT ممکن شد!
🔹
حالا میتونید مستقیماً داخل ChatGPT عکس‌های دلخواهتون رو به استیکر تبدیل کنید و از اون‌ها برای ساخت پک استیکر در پیام‌رسان‌های مختلف استفاده کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/684895" target="_blank">📅 08:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684894">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db615e5198.mp4?token=jKWgufMxPrV7QkaDWvNJnOsb9cleuTo28FAqD3Nr_Yk4_vnwSXRK-o7omAs5dzqhKGXQxNWTAsxNc-l8q5PR9dnudG5VIWfuGVDEr9bGYCVFeix-oZIlFOgag9VrSEDZD9FeGbEI4kDaUovOINVhkPzP3OHV49Q2HlplOGC2t7kWfQZRpsnUFPcilVPdJmqeasHAUUfNisKL99m5pGLpdl9qimD4C9dfM_OthMXe2VK-xLVP7EoGoN44oi7fVVB8ooGYOolb69WfiXhc8db6lU1GXr0kPbKapRzuXwEZSr4e9HFROkd_JsFW7Ha5Y_dwQ1WAbLzxqAU6HElWRoquhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db615e5198.mp4?token=jKWgufMxPrV7QkaDWvNJnOsb9cleuTo28FAqD3Nr_Yk4_vnwSXRK-o7omAs5dzqhKGXQxNWTAsxNc-l8q5PR9dnudG5VIWfuGVDEr9bGYCVFeix-oZIlFOgag9VrSEDZD9FeGbEI4kDaUovOINVhkPzP3OHV49Q2HlplOGC2t7kWfQZRpsnUFPcilVPdJmqeasHAUUfNisKL99m5pGLpdl9qimD4C9dfM_OthMXe2VK-xLVP7EoGoN44oi7fVVB8ooGYOolb69WfiXhc8db6lU1GXr0kPbKapRzuXwEZSr4e9HFROkd_JsFW7Ha5Y_dwQ1WAbLzxqAU6HElWRoquhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ صریح و قاطع توماس ژونو، استاد دانشگاه و پژوهشگر به اینترنشنال؛ برخلاف ادعاهای ترامپ، تنگه هرمز همچنان دغدغه اصلی آمریکاست!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/684894" target="_blank">📅 08:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684892">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N77eBCyp0KZGEQMc4U72DvAp6_S7ct9-R9c907eKykSOOt_yzW3b6k04vHW5g1m_xUA6gyE9MVQ8bNG6eP_jIQpUKGRdcTCCWEUOgfOObYgWmgiXrQ9ULDIfZ-2E8JId5a7-zTvJbPYMnlPdT4zGOSDaKIIJILha36NXU8mYbiAMpeUn4ueyqY4VvHMgSkY8W1lLDSEX3V4k2-n0L424bXbRmCZlOShlCwJAbKMUMWwpk4z8TxBnxpqNT_u8bXEIcBf8qd-dYQNxuct9kMSQgnfzkUCxnfaDppKqMKjonANgHyst4YB7YZ46-MWvMmVxS9mf2OM7Ap64nwT-cxyYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ دست از توهم بر نمی‌دارد: «تنگه هرمز بخشی از آمریکا است»
🔹
دونالد ترامپ در تروث سوشال بار دیگر تنگه هرمز را بخشی از خاک آمریکا توصیف کرد؛ ادعایی که بیشتر با تمسخر و انتقادات شدید از سوی محافل آمریکایی مواجه شده است.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/684892" target="_blank">📅 08:01 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
