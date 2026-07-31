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
<img src="https://cdn4.telesco.pe/file/hEaXEPqc5wZqFPvjE-PWQZLCCoG971HU_uIZWBgIUvSaPQjXfSfxd5voGELwPsmwWUBUcD2_qNDlDUMA_BVxF1d4_DapZzp3o4OHNIKClJlyO2oAa-lrDaEnQxxs6KP7mBd6_n6zsdadpu0RqxfdjlO1IbwABunwyIkzEw57FQu0F2s2-6gc3wTOMT0YF6MvT-H3kQUifopxsWE3qli7sjwn3-49C89Y1sxyBnbIY4qBcXW0yjOZUM6FSD3wmxIYsYmMwWdRaUhcA59ERwoyO2ArOAegUNk0O-oJ9JUSwA07KNuvdjDbaY2sEiyaGBC6shcGJ1m_eZ_EdSwHMTDKXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 12:12:47</div>
<hr>

<div class="tg-post" id="msg-676935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-zBN7e9t4wA1WLhJL30U2F49KmzTAcR_jzqp5BOQ3nypvSeRd-kLZvW6mxzmj6Z2hO5j-hO1q8fqHGYFqKnUaeiurkabHycItKq09k2wqP8rRoF8wXRESSqfdLbFFxq9HrsQf8B5iHuKdOla1A9bT4ARd6mOUV_zAFnfTSJN4qCphooc6pn-fdJfuqNAWehKwCkxJHu8pJwY0XFRhPiV2XjtxyyqnIPtXkRjU7CLrpzNwJ0ON0T82H1tNj-mWPFC9VMmEDJbEMmB9_ZY0xzDqbQxgezz1oKldIxV7Og2EgDPHXjlAap7Oxw6abl7OrC4VHgRBx_0a9SQg_UiToSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک هجوم پناهندگان مراکشی به سئوتا، اسپانیا را به آخرالزمان زامبی‌ها تشبیه کرد و تصاویری از فیلم "جنگ جهانی زد" را منتشر کرد
🔹
وزارت کشور اسپانیا اعلام کرد طی ۲۴ ساعت، ۴۹ هزار مهاجر وارد شهر خودمختار سئوتا شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/676935" target="_blank">📅 12:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V137SyVs-8O1HccH4oRLRUfC4r-7vdbInOBNae9m3k9iugiCcUGv42HmE_vvdZ0DTQoehSU2-YVjDdkbfPB4HQu33-isoOerNfXtAFqG8x6xqlrS8Zt-b5X_I87BvtTMuNbpTF73598UMgFtINixITwB3yE-FV1a9a42kBIyOX8Ax7P6TzBgtP1_e2PxYMT3PWq-4dsimekLqY0cFFPOnLhB597CKXJ8rw8l2suH_yuXhcVaHFWvXWT60RtIWcYLiSTjuUyplJaWuigBykOW2wj_KX-Un2d9jE_K5AMA5ySSw_rwNGLjTRKIGLi1zj3EDIbPUK0k1Ci0V-tH8sx6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرنوشت جوان مفقود فلسطینی در تصویر سربازان اسرائیلی
🔹
خانواده «محمود الدریملی» پس از دو سال جست‌وجو، سرنوشت فرزند مفقود خود را از طریق تصویری که سربازان اسرائیلی در حال تحقیر و آزار او با دستان بسته و چشمان پوشیده منتشر کرده بودند، یافتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/676934" target="_blank">📅 12:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پلیس به زائران اربعین: بازگشت را به روزهای آخر موکول نکنید
🔹
دادستان انگلیس: یک شهروند انگلیسی در قبرس به اتهام جاسوسی برای ایران بازداشت شد
🔹
استانداری ایلام: از اول ماه صفر تاکنون یک‌میلیون و ۶۵۰ هزار نفر از مرز مهران گذشته‌اند.
🔹
پارلمان لبنان: «توافق چارچوب» مرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/akhbarefori/676933" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d85e4810.mp4?token=CV-Al6dMNklv6ueyjh8lM40tlNZ4Zj3Eb8sEFP5RkK4tJpg3b0gGBOQyTew1KLKQletkmghPmWDgD2bbjACQn-YlmK5ueqv4iRDXN5lBRCxNmGBQE5Y3Z4ogE_RDz5BgV93fQXEKjASbvBqpAN9wNAn1YqcIoaKfRTNca1MfgJdF7S3F_hz70wbcNY68455N85zBklfD0OVBM36Kbf0jR-HyXa4NdeT5AnjmOo-gzegqWQy0MiaTc0Qi76b3tHh6tOXdd-FDzCXlqIltqKO_M-4A2bBern4_M1TpTVjulLXOrYwaBf5vuUg4lsTbWKhqj7S4wnalaGdGAo8TWyvJ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d85e4810.mp4?token=CV-Al6dMNklv6ueyjh8lM40tlNZ4Zj3Eb8sEFP5RkK4tJpg3b0gGBOQyTew1KLKQletkmghPmWDgD2bbjACQn-YlmK5ueqv4iRDXN5lBRCxNmGBQE5Y3Z4ogE_RDz5BgV93fQXEKjASbvBqpAN9wNAn1YqcIoaKfRTNca1MfgJdF7S3F_hz70wbcNY68455N85zBklfD0OVBM36Kbf0jR-HyXa4NdeT5AnjmOo-gzegqWQy0MiaTc0Qi76b3tHh6tOXdd-FDzCXlqIltqKO_M-4A2bBern4_M1TpTVjulLXOrYwaBf5vuUg4lsTbWKhqj7S4wnalaGdGAo8TWyvJ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
عشق رانندگان به آقا امام حسین
🔹
موکب به موکب، قدم به قدم، اشک به اشک می‌آیم آقا، نه با پای سالم که با دل مشتاق، اگر لایق باشم این قدم‌ها را به‌حساب زیارتت بنویس.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/676932" target="_blank">📅 11:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
دیدار خصوصی ونس و نتانیاهو درباره ایران
مقام‌های مطلع به اکسیوس:
🔹
معاون رئیس‌جمهور آمریکا و نخست‌وزیر رژیم صهیونیستی در نشستی صریح و دوستانه، اختلاف‌نظرها درباره جنگ با ایران را بررسی کردند و بر ادامه همکاری در قبال اولویت‌های مشترک در غرب آسیا توافق داشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/676931" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا در حال بازنگری در حضور نظامی خود در کویت است
🔹
ایالات متحده در حال بازنگری در سطح حضور نظامی خود در کویت است. واشنگتن روابط مستحکمی با کویت دارد و این کشور را شریکی مهم در حفظ ثبات منطقه می‌داند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/676930" target="_blank">📅 11:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676927">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f2d8ddf.mp4?token=uLwb910FeoGzu7p8RXOUrmXudWTqPphnI9AEBUJfYGO9XLNNjGYLInxljE3fLtz_dAh2Ohb_w-4nOR68jWPKD0Yn1DFJwRekxzcJGStHNuyXg-nW-2LePJkzn1fPieOcQrhIYIq_tL_1Ju5OK8b5oDbWRVAs2cxn6iKSMHdAXbKHzUrNFd8F8xFjvIy3fzgV0hX-x3LJxMbU_JY6cQMU4uxRdjSM4GRlOSpjKQ1phCN9OuiQW-G90D4O82coQH0zgeR9NZFBld_ZZW5jwsTIdwfhZoZUtf6lTGivXm-eZ6-MDD4M7HnyJkyo_uDoorPIf72VtTYP4DjhoegOxA-qWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f2d8ddf.mp4?token=uLwb910FeoGzu7p8RXOUrmXudWTqPphnI9AEBUJfYGO9XLNNjGYLInxljE3fLtz_dAh2Ohb_w-4nOR68jWPKD0Yn1DFJwRekxzcJGStHNuyXg-nW-2LePJkzn1fPieOcQrhIYIq_tL_1Ju5OK8b5oDbWRVAs2cxn6iKSMHdAXbKHzUrNFd8F8xFjvIy3fzgV0hX-x3LJxMbU_JY6cQMU4uxRdjSM4GRlOSpjKQ1phCN9OuiQW-G90D4O82coQH0zgeR9NZFBld_ZZW5jwsTIdwfhZoZUtf6lTGivXm-eZ6-MDD4M7HnyJkyo_uDoorPIf72VtTYP4DjhoegOxA-qWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ورود مهاجران به قلمروی اسپانیا
🔹
همزمان با تداوم بحران مهاجرت، گزارش‌ها حاکی از آن است که بیش از ۲۰ هزار مهاجر بدون مواجهه با مقاومت نیروهای امنیتی مراکش، از مرز زمینی وارد شهر خودمختار سئوتا در شمال آفریقا شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/676927" target="_blank">📅 11:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676926">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
استفاده ارتش چین از هوش مصنوعی آمریکایی برای توسعه توان نظامی
رویترز:
🔹
پژوهشگران نظامی چین با استفاده از خروجی مدل‌های پیشرفته هوش مصنوعی شرکت‌های آمریکایی «اوپن ای آی» و «انتروپیک»، سامانه‌های بومی هوش مصنوعی را برای تقویت توان دفاعی و نظامی این کشور آموزش داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/676926" target="_blank">📅 11:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676925">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3d9857e6.mp4?token=KsGN9E18kQ946btoMgS1EUEQAaba8Rl2pWirPqiDsUwMa7cbBFSWUIRW59UIUX4DGAGNhZXo2QF7vVi48IJh2rP9MxncxXe8ugeFpKvQ2I8bZtXk3_Jo3dTneytBrZgn3Esc5LOmNEA2gFlRr_M6NemdiJmQB04QAjta0QMked7n5n9zN-4ZV6Xlz1SSetpMtTKW0d1btTc1u7rtE9SyyuTDz1sV3teIjUROYUoAoi1QKS0Aed9rwB-CnGx5uXQauxR3fw5K0Z4oSGVvbOfO3PnqANC3UHEkS2rzaciKKLFiaUevIqNx0p_eRNAYFfjCHn2bHnIzPUTjGGAz-B41bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3d9857e6.mp4?token=KsGN9E18kQ946btoMgS1EUEQAaba8Rl2pWirPqiDsUwMa7cbBFSWUIRW59UIUX4DGAGNhZXo2QF7vVi48IJh2rP9MxncxXe8ugeFpKvQ2I8bZtXk3_Jo3dTneytBrZgn3Esc5LOmNEA2gFlRr_M6NemdiJmQB04QAjta0QMked7n5n9zN-4ZV6Xlz1SSetpMtTKW0d1btTc1u7rtE9SyyuTDz1sV3teIjUROYUoAoi1QKS0Aed9rwB-CnGx5uXQauxR3fw5K0Z4oSGVvbOfO3PnqANC3UHEkS2rzaciKKLFiaUevIqNx0p_eRNAYFfjCHn2bHnIzPUTjGGAz-B41bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مایباخ S۵۸۰؛ ماشین جدید بنز
🏎
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/676925" target="_blank">📅 11:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676924">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TuMODDt__9T7BVHc49u37DvY71ZXnwq_IRzsxAkkhO0qSCWR9PDr0sk0oK7PMq1Fsw5mVFzoJcRepLW95R4BVUhpn-EDekx0g5GBVoxMoA680cE771a_rhPYKYl5NiZX3roqQW_I_BTVJvSFQvtgxrFDEBbpg_AlumfnXI4N3X_DkUKeosw2LDMihngbVMfvbnJTEIryNfLE2SgeZZYEpej1CvpBB7E257JVE8j5YSJjRckq76RwCy1Zr_3AtDOUuBbwMXioNqDE9i29yKyHj8id7wQjuQGadeMp7uNGO40sTM7Upuh0BXPEJfAvNybw1nbyS-KpoCZEPcks2qJX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور حجت‌الاسلام محمدجواد محمدی گلپایگانی داماد رهبر شهید انقلاب و سید پرویز فتاح رئیس ستاد اجرایی فرمان امام در موکب امام رضا(ع) در عمود ۲۸۵</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/676924" target="_blank">📅 11:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a5326a9c.mp4?token=WqZh5AbeKzd8uUkJnz0OgslLr2fOHFRhWHy2uMsIMdFtkUD3y67Rp4JpN0Y9yWgOPIaAnSUGWQvAYTQQAeDRBlSjt968CSIArldiTuKl1sktaqKErUwv8Q0Pgzsz-uo_62sqkiJPcMqCZvBS-AeEQGwWtKS61OtvKc8ZLjsdTUX7FxSb03whzRXoQVEyjxz3BDIC6dudM-SexVda7lWGIxd-GJ2s-B_YjHtGns1s3MeBW0nDMv_HiQROHphjtUhnRkkNYYMEEsjpShjMfVrOnsFibfF0CiLl4P44Hqs_BdbR6MF3aaVvqV66_b6V0omjAp9lxntxwFJyYCP2i_mEx3qdHHt5KpLoyrXLQVLu_psreIiVvFjpxZU1qeCJhbvY7dTc5_8UvQWXaFRcqjfr0-jtKoKwUqeearqAa6193bPRmoDZz_CML5Icc6p5hX837lDfSqYGsBK-nwS3wDrTORPsfPMEiRnV3IJmm8RkgpPYaOzDAmeGKfyyjI_zT21qdwGXJ7pY-SVrO-aXB3TtXd3JVqgxo2Dly_1Edv6wO6fJNN8bkzplCe3a4gR1YoTmyEQ9DnpcZj6zjyZz3vkix9J12oPhadMQud6GxfGQzz3B9WydFklW5dmxhelDnJUYUJtHnQmOaYhIomMeXDFspMaZAuRrVJUvNz1Cv5FZFW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a5326a9c.mp4?token=WqZh5AbeKzd8uUkJnz0OgslLr2fOHFRhWHy2uMsIMdFtkUD3y67Rp4JpN0Y9yWgOPIaAnSUGWQvAYTQQAeDRBlSjt968CSIArldiTuKl1sktaqKErUwv8Q0Pgzsz-uo_62sqkiJPcMqCZvBS-AeEQGwWtKS61OtvKc8ZLjsdTUX7FxSb03whzRXoQVEyjxz3BDIC6dudM-SexVda7lWGIxd-GJ2s-B_YjHtGns1s3MeBW0nDMv_HiQROHphjtUhnRkkNYYMEEsjpShjMfVrOnsFibfF0CiLl4P44Hqs_BdbR6MF3aaVvqV66_b6V0omjAp9lxntxwFJyYCP2i_mEx3qdHHt5KpLoyrXLQVLu_psreIiVvFjpxZU1qeCJhbvY7dTc5_8UvQWXaFRcqjfr0-jtKoKwUqeearqAa6193bPRmoDZz_CML5Icc6p5hX837lDfSqYGsBK-nwS3wDrTORPsfPMEiRnV3IJmm8RkgpPYaOzDAmeGKfyyjI_zT21qdwGXJ7pY-SVrO-aXB3TtXd3JVqgxo2Dly_1Edv6wO6fJNN8bkzplCe3a4gR1YoTmyEQ9DnpcZj6zjyZz3vkix9J12oPhadMQud6GxfGQzz3B9WydFklW5dmxhelDnJUYUJtHnQmOaYhIomMeXDFspMaZAuRrVJUvNz1Cv5FZFW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نور طبیعی به‌جای قهوه صبحگاهی
☕️
🔹
استاد عصب‌شناسی استنفورد توصیه می‌کند برای افزایش انرژی و هوشیاری، بلافاصله پس از بیداری به‌جای قهوه در معرض نور خورشید قرار بگیرید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/676923" target="_blank">📅 10:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059f1d5219.mp4?token=VXmq-6awRbghjpyqClIKbqnEMtoi1cnVMYBC1H76k2Eq70HuYyfyTYskY5t_8ObGby7BCu7BUxBIF8WttKDJo1ZJwm4jYPBM8nnsPThMQDdgk5kDES72rjTMh_bQO14X0liDouz3eYuSTZbIwZNrILJkqI4D6xa85yntsg8In9BCzZsa4eZFa8ZfOEpAvHhTfmHmAjAVrh2V35LIJVk34CkHgGoKZWTRbGKpwvDhG-gmjbxBgv47hWoTdtLGDiGFkpGmj36ARugsgD3BW_RO9NDUki82f6Oahic4M5EDBxPpKlxGiuYf-AUh1zHH56StLxpxZCnSsOsc-XbV8zwZYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059f1d5219.mp4?token=VXmq-6awRbghjpyqClIKbqnEMtoi1cnVMYBC1H76k2Eq70HuYyfyTYskY5t_8ObGby7BCu7BUxBIF8WttKDJo1ZJwm4jYPBM8nnsPThMQDdgk5kDES72rjTMh_bQO14X0liDouz3eYuSTZbIwZNrILJkqI4D6xa85yntsg8In9BCzZsa4eZFa8ZfOEpAvHhTfmHmAjAVrh2V35LIJVk34CkHgGoKZWTRbGKpwvDhG-gmjbxBgv47hWoTdtLGDiGFkpGmj36ARugsgD3BW_RO9NDUki82f6Oahic4M5EDBxPpKlxGiuYf-AUh1zHH56StLxpxZCnSsOsc-XbV8zwZYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به‌ اندازه نیاز خرید کنیم؛ از خرید و انبار کردن بیش از نیاز خودداری کنیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/676922" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PojrETwmlylAx-LAh5iWniZtA0DHXKWNT5L5QGj_8YWzmgGr5v-fEBGiAKpo1aMGazeMpUG5njl7aqBKtxCulzX61fF0FZ-QLYQJ0u9jbOTBG4kPXHemonazfm1Q9JF_71PeEGanCkh5sKQ5Pgtfa_hkC1ppsWQGqQ0amXucHp_Hhh7piD4ulO-jq12o0F1dHBT28Li3jxLhr1wVNt2p8-EA94HMkno_wvW277OhWakyck8UZzAhUhkvSrhnPMnc4Jp40-NXflGrYVonRI8VgBpPWtGIrOd6r75-pBNWCL9NfCfHc7Bp5n9UjAR1CObEYKPgn7484TfEUaSdTjQB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PD-KkHq8cOr4lRGyOZgwXuQTZYWpG-ZapBaXOB8cKI45DD6jroe_xBPzA2DxFu8MiwcEw2RNYUfBpoSgwOXJ3l0jKXPwtH4SBojANKYvXqxCHTOHYz8ZqfCLCVMcK97k9Xalm0HNGgQV8V-fvX2WxWNZZn1VsIIi2L2aoKzzbLbSSESEW9QYILL4HpWHWdP00tpt8qWxOug-UPP398VfV43vBVMlzXkb-_R3pPIjvNs-w_1sBXV59IU6UUdHAnXtY8EXHiEtbT36y9u6xFVegEo-dzMZdF-9_rkB6RuU_IarnqAR2FBl5OEx1kXhRRVUrhT86UdcVd6UN_iGDoPfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOiMkzrIMBFEnjvdnPpgefTXojxmI6MiGRctkC7t0Xj56FuyXTA1JhRLsldLQA7XQ6yZ-nmv_xg7Z0vrHpsK0nnmX38MHIYcGJr4Iz7FjstBbxovhqa3wdmvDtcMj49Srwkw2_Y7WKJrR5vH59WqPJ6sl7ah_P5Rqpwfr7nHpP91ugU7m39-b3oLkuGKOuhMsRQydePRD6Evhgma1jRlYG1bc_02w2OAq5aQvA4lEeRjUnnqwsHnlGbNOpoqufeHMNa3hTfYn4eKAIaM---VBlRSSHLaD88JHqKxczlRSEKSNN1TlyD3xnY_y77FfXl2OK5cm_6h6JbK4bsdqWMv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ati2kYWK6it0BKFzbCdeFin9h09Az6iWY1GbHBM2FOnZa7hX3HqwfE_dxHquF93moB-JdAMi41EFSnkJW_VJlhNo9J0RYvmsbBP5giLAqCKQAWjP2qO-fXOFGLzfZ7tadnTnszqR7Uk5wuzF3KSlfnyWaIoRcRZUz51MqzhmbS05_FrOV3Fv5f1mRgYa5ViJmCxitpUCks6oIsVCBky8vyKp7f-AiCuWmLKxC6Z_KmlsHQ5B-7AVm4rbLl1350FUYtonM2DBGSWVCe-ilAlxPCTzXyMF0SNQcZqJdP44wprrYMw116hm8SycS1ptjs0vWRHi7RowVT1Nlwla8y5eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJv9Z-qjQQe-9IKJLKobA4I-nb9z51lSJYQFz0iicXBJkTMgqYQ4AnkYt7mX7xZXrfRzrGhIifXaFF96m643CSONm6z2P6V_9SpGMz0edJ62dq4O432ytTovTUQDGiL55AHLMFluYUvmHHP9bN9enWtfDr_ilW5oJ00QnIRMVRGb4ARFIU2kC9SS5UEo5PAhKV9S7hWu6Q9uoNImI5t9l4Jg-THndjtDY-nYSLbJpIWMlN7A1_0p0iJt1vLGS2PSyuWbA8SaYEu68J6rAZabuvNFAtF4bvexLBqFlpK2wj7xJ9gQ6fs2YdHt78s8o1VmuwzwylkA9OKyYwKeoNE09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kmbxSBiROCb8pD3nszNj74Ykgq9mQYMhc_iwiJMFwlzcvRWgsFSv3KFkrcqfDokyCN5e0gZk2PDdO2cjmnjVx730Kt0x-HZ29Q6LM-kZ_oVexSOtxu_uQJCoMGlcmLSTfqU47Kn0i-H6aYUBfqaSjNFoQYPuWM-9-1m0t6lBT1U08f8n7Wsy-1CIqvngkrQ_9yVBbktScTlnWkkeWlp8lqB-iJb44MciJP7DSbebgDJdN9TxBI7P1XsBvzcyUhkqd8tnlPGnOMlVhumwFMIHMOeM3t7f3lzAHnG3I0eXW8k-SKsV1MU7pKIxhcQ-Av_33oQqBLirCB0lU8K8Q51FzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWvhSFwLTopxUI3ZGfd6vV5xPkcL7DmHtz0ZEP-ZtMZZXua7BGtkzIqL59xPiB_akp8tQc57tblYvvEhFEeR5EUBx1d_T3J13I_s6zNb8wJUgxM5V50kgqRulTqTa6F1wdn_DGoXUlXhRP6TATVKpvxVk6gKF9mcBFvyRQmXX6mgfy0ozKPCMT4vnYC6RV7uNVsQ5bV9I4m-g0mWHmuo4VwzxZd3bxysSt8upUjBAuX-yOzMJZznvOCUoMGOzbFDznn0-NlBfACSlBXs1z-77Ila9bxA6epIivHw93432cA4ZcdUcRotYSWz7GwF9NJo2i72vIP9tAXk2I0J0vS7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qhl4mIudyq4FBaq6y9deryV79uT7XOADtku-pQWzbtvsUz0rkwPPRkdXkS0AdirlkMbr4aulQibr6Y9l0NrboJlhoxEK-4P3MCc-r2yR2i2nyVkssjr5UBXHYmf8F7ej83Hw-9rJdJw8tPtBGC8IEV-lJASbOQk0MVQvCYIpQRc7yKdsJ6KdaZOaKb07YICXOPFpY5NpHrSZbhKgKwEjxqiRG7lRHPAqTQE8v32KtzxyzZas2RHU26JstTC35m7XJcbE4esa7pq02kU2O3e0WwnQc-0hfKYvEpgg31xGDWAWOj43dpKAPdnmWgSmIZ-8jfaUymsaubdB8czT-SVlwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keaOAh0jayiCeFdM-LDn7MKkjrLvHew48CF15pqu3uCK7SmMRi6DeCyuTK8DuPZ-GhT1WZmofsFNZ2qkjQ3GijWCz6ibBOGxkOsj-qeiY1jL1kzFsPBMhRaBL2uVMyhRX6b6qdLwSHzMtSbX84fVdSAgrzE03Of4gkXUuQpo_Xe9B7nOEZKD5Y9pKjMO9XHbzw1rgnyJDfDiy29jGX2hvTWSoDJNWRQlV4JvpVsWVsI12GL-GiUsEaDwKkSZ0ZtDT3o4uM3uVSAkRqONelnHXMnVvLyPwHaw-b2MfKiBuYV9hyjWMGY1YKCpJL28EIP5bqQhS56zzdvCGTD9ZIJjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx6fgXgeqJK2mdgxhT8CGc8gjKo34021TJ4F1WI9I62S_vudxlhkEK17KpSPN0r2Z60PnCZzSrFQqfvvJ1oMK2HXi-t9771CVP6Eyqr9dPKzJhyqx9b2Gg9uJLLNqvJ1JjEyMhzYjHhruEkVvpk0uHwfUW3DyPsu6t_jXXtNDUOiUPQ5c3Wt9n0khE68cb7LCLdhBn51B1FZwXlyeiuMqbdZQgpkhLIiXeAVfDj7CzTMpY7b-c_nR44sTOVRp1ogHsM-PHFL_rBG8HAQrF3Zknh2DZZyIlp9nUCibqepMWUCMvxgLKI41t0_twjc3PEWiBFzaa8Eo4J-aCxdW9Q1lA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از روش‌های قدیمی تا ترفندهای جدید؛ ۱۰ نکته کاربردی خانه‌داری
😍
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/676911" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99839d8959.mp4?token=nvuGbiClqpvGws6DJHnCMzrRHw6tMlz2cQtyVnDn7RRBNcJ_MFKZySQ_xEk4OJ37JgTUNqFPRSKLZ_U-dLRIT-dZDEzm9ioMm60B8yh2DwYZkpDY3Al4E-p-7SmyurG6Rl8Jh_YylslkXm-LUt8-7fEjocl7hA7GlRByDIBFe7W2LPxz1G5Iqc2oVAbjR8Ij5aK9aXAq5cKL4ZfbjTu7bGuQSBHv54YrMaSFmfCy7POvDdwkGKFbCSo-8xhxdishjCfL7YJhJwd1o0fwE6MQ9cchuf-8UHjl94xpUqRpDoLdPHWrZPAgIC5nhSuj3gjJ6IyPCZEyJMRHyJ7GeQDxWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99839d8959.mp4?token=nvuGbiClqpvGws6DJHnCMzrRHw6tMlz2cQtyVnDn7RRBNcJ_MFKZySQ_xEk4OJ37JgTUNqFPRSKLZ_U-dLRIT-dZDEzm9ioMm60B8yh2DwYZkpDY3Al4E-p-7SmyurG6Rl8Jh_YylslkXm-LUt8-7fEjocl7hA7GlRByDIBFe7W2LPxz1G5Iqc2oVAbjR8Ij5aK9aXAq5cKL4ZfbjTu7bGuQSBHv54YrMaSFmfCy7POvDdwkGKFbCSo-8xhxdishjCfL7YJhJwd1o0fwE6MQ9cchuf-8UHjl94xpUqRpDoLdPHWrZPAgIC5nhSuj3gjJ6IyPCZEyJMRHyJ7GeQDxWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مرگبار معدن زغال‌سنگ در پاکستان با ۳۴ کشته
🔹
بر اثر انفجار در یک معدن زغال‌سنگ در جنوب پاکستان، دست‌کم ۳۴ معدنچی جان خود را از دست دادند. این حادثه در ایالت بلوچستان رخ داده؛ منطقه‌ای که به دلیل نبود استانداردهای کافی ایمنی در معادن، همواره شاهد حوادث مرگبار مشابه بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676910" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-bQy7PlkzUa6y5G0Y2jIc9bY1OxP0uaLZzG2yJGaLVaEAWmAqQTuUUbgA50uQCmbUzh-g1BY8JKaAMDdXz0KyB5wvC62M8XeDw78yHH6fhsLA7s8M3sisSNbVkMkOsYKABY_e1NXTUNzVCHMocSRUFEua4c0CoDQTDUizhfDL38ElH9n5IXAA5cRmzRsErbAaj1hygaVr77q5N-i6nZ-KRLVkVmxz-6QuhjYpZWbNFVrhRdeOuOsicx_3uxX4TN33aY3m7JdGE45UDxUoe671gL2wLNYgHXYEDU7tUSsJ78CV2Dfq_8fZADIVf4IzuW-onwVpB4OUNJanJZho9LuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/676909" target="_blank">📅 10:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b780c515.mp4?token=Fcy4NkzCV1H-02Ygxmx4qzU4bTy-8AJy4kGklbG9Fph7k0e3qmyqJdWsPZ18Q3NYpoldkf0rfqMQcXYXtafc5h2sn8FY5ilRwC1CJYCC5DlVjzsD5vGGXLAVc3zBTvraTy41vn3lYr6T_tQrOBOEMLTAMy3aGc9YJ3AMsTE7gefq1aYAM7IYO4efeXKYqGd3kVtpTPfLs7EhY2h0QntkL3CQE3z2o4xq_38YAB5OzIonYAO9yRQse6YxdF0qvXqq44UBTDNxBdSZxrz01WFTng_OXUAQ456sxifLZwfzOHUlvq7kmkCYUKO7QuE14IECy4OeUeZepEvKWocyY6cmKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b780c515.mp4?token=Fcy4NkzCV1H-02Ygxmx4qzU4bTy-8AJy4kGklbG9Fph7k0e3qmyqJdWsPZ18Q3NYpoldkf0rfqMQcXYXtafc5h2sn8FY5ilRwC1CJYCC5DlVjzsD5vGGXLAVc3zBTvraTy41vn3lYr6T_tQrOBOEMLTAMy3aGc9YJ3AMsTE7gefq1aYAM7IYO4efeXKYqGd3kVtpTPfLs7EhY2h0QntkL3CQE3z2o4xq_38YAB5OzIonYAO9yRQse6YxdF0qvXqq44UBTDNxBdSZxrz01WFTng_OXUAQ456sxifLZwfzOHUlvq7kmkCYUKO7QuE14IECy4OeUeZepEvKWocyY6cmKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزیزهای عراقی چه دلبری کردید
برای مردم ایران برادری کردید
آهای اهل عراق، آبروی شیعه شدید
🔹
شعر تازۀ احمد بابایی در وصف حماسۀ مردم عراق در حمایت از ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/676908" target="_blank">📅 10:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676906">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738a793d14.mp4?token=Lq_j-z4A3uEwNaU1Wkn4cBjOZtwxDY-2W2gh7-i-NWInVGxk3GiX1aSTaO1dF8DOiYPFzlcqkWGdcfJ0MRfmk0JEUeL7OwrwtfDDwnAbCnz1niHQIAzjitR8tsoJJAX_lCLI-pvoG3G4tPO4nVU0H5h-m23FyPJMMS87nG6FsImiLwhUqgg-D4Zvnm44r3I8yQ_lh7EDzoCxo8mYDKj2L8_MxyJYpuna0cuJZOFvf1Bp9fbO4AZ12pqLvfACQdpIIx-MdeqXYBNYS0FqlyK5aYALOw8RFDN2ExUxWFlPAENukJGPZYPRd6RJe49XjscbFC6sDzzlk6PFdaOLCTAlhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738a793d14.mp4?token=Lq_j-z4A3uEwNaU1Wkn4cBjOZtwxDY-2W2gh7-i-NWInVGxk3GiX1aSTaO1dF8DOiYPFzlcqkWGdcfJ0MRfmk0JEUeL7OwrwtfDDwnAbCnz1niHQIAzjitR8tsoJJAX_lCLI-pvoG3G4tPO4nVU0H5h-m23FyPJMMS87nG6FsImiLwhUqgg-D4Zvnm44r3I8yQ_lh7EDzoCxo8mYDKj2L8_MxyJYpuna0cuJZOFvf1Bp9fbO4AZ12pqLvfACQdpIIx-MdeqXYBNYS0FqlyK5aYALOw8RFDN2ExUxWFlPAENukJGPZYPRd6RJe49XjscbFC6sDzzlk6PFdaOLCTAlhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات به تجزیه‌طلب‌های ضدایرانی در أربیل
🔹
منابع محلی صبح امروز از وقوع انفجارهای متعددی در منطقه کردستان عراق خبر دادند. مقر گروهک‌های تروریستی جدایی‌طلب ضد ایرانی در استان‌های أربیل و دهوک هدف حملات هوایی قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/676906" target="_blank">📅 10:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676905">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
الجزیره: ۷۰ درصد نفت خاورمیانه جایگزینی برای تنگه هرمز ندارد
رسانۀ الجزیره:
🔹
اختلال‌ها در تنگه هرمز باعث شده تولید نفت کشورهای منطقه به میزان بیش از ۱۴ میلیون بشکه در روز کاهش یابد و این موضوع فقط در هقته‌های اول جنگ علیه ایران بیش از ۱۵ میلیارد دلار به آن‌ها ضربه زده.
🔹
برخی از کشورها مانند عربستان و امارات تلاش کرده‌اند با استفاده از خطوط لوله موجود، اثرات این بحران را تعدیل ببخشند اما در نهایت بیش از ۷۰ درصد نفت کشورهای حاشیۀ خلیج‌فارس راهی برای دور زدن تنگه هرمز ندارد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/676905" target="_blank">📅 10:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676904">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3548ced87.mp4?token=PLWxuU7XgUVzlYLTX-icZCucyFMmrbcM2spBq40d4XE2Qugk2GRMfraluDorZebSuNzz_uXX_T5bM9zz9JGhNx33-47pfuaW_06ZN--y32uuqGvqLXIWWap3_8E9eaqOJW1dgVobqyY5lWgxcGePBdoo9by5V4ul2kl5_jfconzcrjs-qenCOIPONJErG3O0jx09dJ8u9HTGi1yAFyuzrF6fHJ2XAbJWfnJkRa_yZ7eiWj0yN_7OdUcZEkaVQ3WUve1aLovbShlE8qGBfwlrdTPjgIr1pxvSzyJc0gTb6Ovw2KUkYCJNSXzPllCSgLIzCyNWQG9zNYfZiOOjPZrzTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3548ced87.mp4?token=PLWxuU7XgUVzlYLTX-icZCucyFMmrbcM2spBq40d4XE2Qugk2GRMfraluDorZebSuNzz_uXX_T5bM9zz9JGhNx33-47pfuaW_06ZN--y32uuqGvqLXIWWap3_8E9eaqOJW1dgVobqyY5lWgxcGePBdoo9by5V4ul2kl5_jfconzcrjs-qenCOIPONJErG3O0jx09dJ8u9HTGi1yAFyuzrF6fHJ2XAbJWfnJkRa_yZ7eiWj0yN_7OdUcZEkaVQ3WUve1aLovbShlE8qGBfwlrdTPjgIr1pxvSzyJc0gTb6Ovw2KUkYCJNSXzPllCSgLIzCyNWQG9zNYfZiOOjPZrzTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی شدید در نزدیکی نیروگاه هسته‌ای انگلیس
🔹
صدها نفر در پی وقوع آتش‌سوزی گسترده در منطقه ساحلی سافک در شرق انگلیس تخلیه شدند و مقام‌های محلی وضعیت اضطراری اعلام کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/676904" target="_blank">📅 09:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676903">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
پاکستان: مذاکرات میان تهران و واشنگتن ادامه دارد
سخنگوی وزارت امور خارجه پاکستان:
🔹
اسلام‌آباد نهایت تلاش خود را برای بازگرداندن ایران و آمریکا به اجرای تعهدات‌شان در یادداشت تفاهم پایان جنگ به کار می‌گیرد.
🔹
مذاکرات میان طرفین با وجود درگیری‌های اخیر ادامه دارد. پاکستان از طرفین می‌خواهد که حداکثر خویشتنداری را به کار گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/676903" target="_blank">📅 09:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3224fc1b2.mp4?token=Q3_F0WetKN-1fiebGs55op2FL5g4YWaf-O6ObKpT4pKLmiBdgxkJTQIRFFbtnB2sDc7zDT2hZNLLion4dSkP1UIlbxN0rjQ2V4AvnZr0_Tgr0g3Rn8CjxeZzbDYK7wH-EyRlhaGgVbxble3IHxxudf08M1oFGGaZ-1JANDd_Hf8U7JkN8XTQsAiG0nf-hhzwueVGoWGRIrSW4dKNPt8zc2kyMu27u5VyhgK08yqxW_2DhQ1xMgl3-g-HkfoIWD962053r59capGxphUQusrD5gxwFzsJJbEENnB__w9X4NMrsfVwBnArtYylVjs9XWag1Pq3lzDMzxoGG5oN_tpu2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3224fc1b2.mp4?token=Q3_F0WetKN-1fiebGs55op2FL5g4YWaf-O6ObKpT4pKLmiBdgxkJTQIRFFbtnB2sDc7zDT2hZNLLion4dSkP1UIlbxN0rjQ2V4AvnZr0_Tgr0g3Rn8CjxeZzbDYK7wH-EyRlhaGgVbxble3IHxxudf08M1oFGGaZ-1JANDd_Hf8U7JkN8XTQsAiG0nf-hhzwueVGoWGRIrSW4dKNPt8zc2kyMu27u5VyhgK08yqxW_2DhQ1xMgl3-g-HkfoIWD962053r59capGxphUQusrD5gxwFzsJJbEENnB__w9X4NMrsfVwBnArtYylVjs9XWag1Pq3lzDMzxoGG5oN_tpu2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی نزدیک از فلامینگوهای تالاب میانکاله
🦩
🔹
مهدی محبی پور ، مرداد ۱۴۰۵
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/676902" target="_blank">📅 09:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اعتراف تل آویو به استفاده از ۷۰۰ تن مواد منفجره در حمله به جنوب لبنان
🔹
نخست وزیر و وزیر جنگ رژیم صهیونیستی با صدور بیانیه مشترک اعتراف کردند که ارتش این رژیم در حملات شب گذشته خود علیه جنوب لبنان از ۷۰۰ تن مواد منفجره استفاده کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/676901" target="_blank">📅 09:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqzohLgVMS_VX3U_p3QUYCFyMsL4XwSaAXWnHTuEe3Zbh70Pu3NZ53PBnRr4CGWqhrumH90WLY2F2_403vwK5bfViT77tEZy8FCL7hi12fknjOxMrKK3z1r0UvtXmQMpWFktDwENEXnQD8PnqOc9rL8mHidjw4eq-WVXUAwBZ-LwK8I-VmN5sUfCzXnhHTEAptZLJ06dofewYtof9ijHcPRk66mY0AgPDmX5YBoCd9xvvCef1S1oFHUfRaBb1aykxVHtrYJoV6scDJh7AdfsjdIL-cF0Xvz762-nrqJSh2yfsl6i_6-Skd5DB0Tv4lshCx2BvNm9C8Jy1CgKMJovDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/676900" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CI2DRXrEZ7TUfCPIsJRgkrBWKTwHn1BF8omPyMnUnuhrCvslt_D4PVEBsIXD01tMjGvXiCAkSpwkmXwUlVhuHZsXQoGcT0KO0oGvYJPK5qnt373RCXHB3pxXfCBl2uTaN17Ot_MmdEOSvYS-KbjVgYgNmNRvv6CKW2A9HhI-E_up84ShEWLlUYFaEwFQDJqphvltbhfGbuZWN9s0x4OjY9uQMKzslit_FzdG-q_i3RxCKoFyfzM4F8lp-qd33wrKGBYw-BsYR3QiSKfMbhC8M0dLDB15NTG7H8dTYhvyxNzYQP3IYR0hq2s_i3ZR5bgjPJzgZ-2QNsZ9SxvJy4KuIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuzcH0E_B3sJrc3UN_Cp3Wy92ykJ5Jt5gD_glyHi2ab8HKcG_e_dUaYK5mrZk0Pig6CbvbX2hFAoerPfK7sOjNO6VkCuK-rJ0sBfyizfyjeIRo_7FOvnOeitVFbEF5eY-50UAUvIQYJnNQ604EgcoLELb8LlRKgBSUJSzKEBB-_l3rqN5k7fSc2BrEXcOgkRy72yX61jLg6D7gLbM4XbF5hHaHRPEEZ-0xTwnbsmQwGtxTUj7kNayqTEdA-qHBixBnkbUDQ36iZ43ZEPqLPSDLbYrzmrqTbGGLPAWWDsn_RtcLHGZOPREV90ipUdMWzUh-q7JCNDK4I6wZUf345vOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تشییع پیکرهای مطهر پنج شهید ایرانی که در حمله شب گذشته آمریکا و عربستان به شهادت رسیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/676896" target="_blank">📅 09:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676891">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E4T8q4wa-JfLEwBYooEuCCxVCWiWw_Km3N5Fg0uUfnabP8KDZQC-rMd2jNb_ENuvGx9uWKcPHYcDPWqlp2wnDhvF6cKXAzG6oD3fjZQBIdJ66jFJXcCo7_tnbeRJsewMQ6ykTOYjjULTtpyLft5sfwOzmuD6Ph2oQFG9ro28U9OG5TdzE96VkmxpcYlXzlt5hedlmoFWDAPVjbmAqQMVp3_p5QqYnpjye3_ljZ1FiUzt848KgBVq4_ghKmmlOLW4yD05fN44UP_FchHS8Xq6tnSMdOLPlZ8x1JkeD9dUy5LjBcyeqhljLQS0DH3ThHp1puZiI4sSl0_0Wr1oiZiQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEaUAPENAl2ZV59I-vaxI1sPJHeNcDCTaJAgVXxrYYv8vPeEhbWQVsNpxMw342ecJfxk1u3VaAGiSLVyxQDG5yg-fghW-zyCrxDZnVaclCs-ALX7z8XBkeFoivB50yhcZNQEruqkKlDojK9wSxxkbszZ4-f5xoJgkWLf2Z0zuLxBZ_CysK-U-HirSYHT3ZVkhMJ4sm55e3soEvIRokISkb5wLK7itFOu0P_vncLvYWOgIogRyjYSX_VmQuAde-6PECOe79Jt3hKKOiFUQFnqhdvv_v9MVa3VVNBTtd7JcwKjvWdFTrcAkNgcIQh96tlBPaTk4y1H81OoseLdo_tz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiODNAOphy4DZVflhqnvj5EDyTB1zZJTDOmM_y33bmd2_19rAHSyrog9_Bts9tDZaHesZWl9O6RRz3ErEkYHENtCyqxQaVzFwv5VK3IO1dDJhq7xtItZtKS_7jqxeWfe5wgvyf79ydFuP0kqaaZdznS6u505iqiKP1rk2fEpULa1fk8Mc_nWG_aQv9peE7XSztMEFXql-06TkNr_t1jasfCLm3T1EDJGOEvrqUdSlPvYqifhh0Nid-0myJecdg2DP1K8ymhZ-eYKkF24eQ2ADGDhwDn04nEAN8J2ZE8GHa6f-4JLvMPpdMAzoYtgXM5FunfTl9gvRocqzrONQvF1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJ-nCQ5JWLNgLvNDCsW4vtwQcn3SZQayE8kf_mRtR0V6NHQOWJcjECVzGI-_TmzNy6uHdthcSnyNZIGo4ce1XeB3mnoc3IZCPR9ZVAe8cGEbNYxxXD7XYz-HfY4AOZieVT_dbXq8U3BbYVqxjWNdsG1caNoXOHhEW_rJBU2irYwNLHtOyzVMmeDIgR7n0rLTN3gBfMTfMPxRvRvsBORcK0deELHzhzVwZkUAdOpLG7Wep87Mx6gT3FRWYJ7Q_n7naxsc3XA15fgwVIJigLEQ4g2DdpHPWSLTEKcXkIAirT32ifUD8O-3sZxM_eNTAEte82wStmknYiugtgUwph2X4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3nVGjbyTlC9jZ0iCqdUEms8LmJ7TKZu9SzhDkc64Ijrc-rd6qgGhjRim_ljdoZVETJfVKO2kHHopkE2ts7qn0A5c47yYVCfxLkNkew3I51MQvL8B2jegO3nXjiP4YHkfMKGTDVJBE7lejffmzEYuaSyBKGtKGQpBxufzMsfocqk4ZoGEXvjNFL2-akFSua-HfbueZfiJgICkca5kp21gJOEh9LHISN5Qq61RHx0FGED6gNh05-RHlQPQeJTntNpOF5n_8b_KgvogfOD9CMmTlG0JcwdpM45u7A-f_wD184MoHfBBLRAWNgFixwfVa1yvmWyd-jYjjUlEk5m9cr4Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵
دستور محبوب برای تهیه سوسیس و کالباس خانگی
🍖
🍖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/676891" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676890">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhAjeE6soeP3qZmH9JDy39N92_oH4AV1f8tdXL8AcL1ydG7wHSCQd30T5XSg5YMFiijLDuEF-aVkX7VYz9pRwtnj_JSxMY0WfyIzKx-OH-a4wD7NnszM512dMOU3fCCa76fy0PjSCjMna7Ema95_CGT-gmylBuq8_lN_31X0COvAUFPQMkzvti4vvRHR8s6og8t1u2A2t0Vdgv3FH6k1fAV7LudWWrZVDb9I3h_VCL67i5i-PL-gcbCFbF9xflC4oa5_8vcZk0869TNN2idDdwkgcxZA8fHs-GkVYE-y4K22yMGrDQVqUfwNQWkRti5fMXYfZJtnPvvH7X2wzsTwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار: حماس خلع سلاح شد
ترامپ:
🔹
امروز، شورای صلح به یک توافق تاریخی در مورد خلع سلاح کامل حماس و تمام گروه‌های مسلح دیگر در غزه دست یافت. این یک گام بزرگ به سوی صلح و امنیت پایدار است.
🔹
این توافق، یک گام حیاتی برای این است که دولت فلسطینی جدید، که با شورای صلح برای کمک به مردم فلسطین همکاری نزدیکی خواهد داشت، سرانجام بر غزه حکومت کند. در عین حال، اسرائیل امنیت مورد نیاز خود را به دست خواهد آورد، زیرا غزه دیگر به عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
🔹
این یک نقطه عطف مهم در اجرای طرح ۲۰ ماده ترامپ است. این توافق به صورت مرحله‌ای و با ساختاری مشخص اجرا خواهد شد. با تکمیل فرآیند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و نیروهای بین‌المللی حفظ صلح با پلیس فلسطینی جدید همکاری خواهند کرد تا امنیت غزه را برای ساکنان و همسایگان آن تضمین کنند.
🔹
یک سال پیش، جنگ وحشتناکی در جریان بود، بحران انسانی وجود داشت و افراد به عنوان گروگان در اسارت وحشیانه نگهداری می‌شدند. ما به پیشرفت تاریخی دست یافته‌ایم و هنوز کارهای زیادی باید انجام شود.
🔹
می‌خواهم از میانجی‌ها - مصر، قطر و ترکیه - به خاطر تلاش‌های مهمشان تشکر کنم، و به ویژه از تیم برجسته‌ام که تلاش‌های بی‌وقفه آنها، این پیشرفت تاریخی را ممکن ساخت.
🔹
تهدیدی که از غزه در ۷ اکتبر ایجاد شد، دیگر فرصتی برای بازگشت نخواهد داشت. در چارچوب این توافق، غزه سرانجام به دست دولت فلسطینی جدیدی خواهد افتاد که به مردم خود خدمت خواهد کرد.
🔹
به همه تبریک می‌گویم برای این دستاورد شگفت‌انگیز که، همانطور که همه می‌گفتند، هرگز قابل تحقق نبود
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/676890" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676888">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04c147610.mp4?token=ecg67hVoCW9lT9cgCA7YjeADk2ncDFNBVKj0OuBSQARg2AINMlWAJ4GFzObIj92IA18BdhEhtlViZAOznGCEMcu9grHaX2wwSbF0QGBx4kINudfssZITAbtVKSzA11hNZfzZBPad0M8zFoCMsYJOil9nxZs86Xdb7K9rftXfVoEi-MeyIGfLn2ELV460x0zafsQtnwsHhOo9oovHCiGUXSOpVWHGhUNC0H05bxnFnUTRV9QDN6l0qdnjgOaRWt_0bH8oKDrVFaPVOQjyVidnNAwdjKXxgkSyRqF0cJye_O_COF72tZVoA95aWBm-U2s-569CtYXyOcG-6fVf8I0Mo0hAFjg8zKaPXfyLt9LqCd1aF2y6fHdJ8YTxGKmRBVMj8Ngz_YKuv9A5LBt0dXLv-ZRaUseXoe2bjx5oh3uponU_sHYD4m281GGFx42V8nrrEn7afd6H0Qg6Lo6P54uBgPxw2czIZ0JBJJrlqHfkWa9gicKDJK97a9Z6qe6yNLy1Azt03ez00OJj21QizRNYR_9AhtIHHTN51HbPUpvnRH8nE2JLy6W9GVQIMtZx3VL2rlloqXhRtKrKfw3WZ6iymZdYtdH-xSNHVlUr04mhhJKdBtbu9VcjtVnbEvujDrpQcQQ2w-kkZmzW6iOERKgSfpMLYVKgHnZXSiWRBPEWgys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04c147610.mp4?token=ecg67hVoCW9lT9cgCA7YjeADk2ncDFNBVKj0OuBSQARg2AINMlWAJ4GFzObIj92IA18BdhEhtlViZAOznGCEMcu9grHaX2wwSbF0QGBx4kINudfssZITAbtVKSzA11hNZfzZBPad0M8zFoCMsYJOil9nxZs86Xdb7K9rftXfVoEi-MeyIGfLn2ELV460x0zafsQtnwsHhOo9oovHCiGUXSOpVWHGhUNC0H05bxnFnUTRV9QDN6l0qdnjgOaRWt_0bH8oKDrVFaPVOQjyVidnNAwdjKXxgkSyRqF0cJye_O_COF72tZVoA95aWBm-U2s-569CtYXyOcG-6fVf8I0Mo0hAFjg8zKaPXfyLt9LqCd1aF2y6fHdJ8YTxGKmRBVMj8Ngz_YKuv9A5LBt0dXLv-ZRaUseXoe2bjx5oh3uponU_sHYD4m281GGFx42V8nrrEn7afd6H0Qg6Lo6P54uBgPxw2czIZ0JBJJrlqHfkWa9gicKDJK97a9Z6qe6yNLy1Azt03ez00OJj21QizRNYR_9AhtIHHTN51HbPUpvnRH8nE2JLy6W9GVQIMtZx3VL2rlloqXhRtKrKfw3WZ6iymZdYtdH-xSNHVlUr04mhhJKdBtbu9VcjtVnbEvujDrpQcQQ2w-kkZmzW6iOERKgSfpMLYVKgHnZXSiWRBPEWgys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خط و نشان تحلیلگر عمانی برای دشمنان؛ رژیم صهیونیستی نابودی‌اش قطعی است؛ ایران تا ابد می‌ماند و هرگز شکست نمی‌خورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/676888" target="_blank">📅 08:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676883">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0476622c9d.mp4?token=HBhvgLAie26tJ9O4CBr-KxlenOOZDthQe8VlemBL_WRTrGVO_G29ue-9O7VLbL_pBv5ijnxleRMinxJj3tOAEyGEjkOoDW6f-VAxIQJaVOmLJn_eqBpUnXzabHA5Cwop7joE2IalKZbElpxwRGeoOfHT-Acx_min0AgqCHiqufA73ntp_IR-i4YaShq5cpZzy287rXvW9crdoSVcFMjp1q9U4-5SVXX9MzdnJIPQiU3yNT9NSsN8dEyPS_tKrdi07iafSSwWsxd1_s0sGXWCQ9FZSxM_rdYxeNvzg1lAypyLWHeeohKsmdHIIAzFQC1irG1uJiWZ0GcOWHvGhWPusw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0476622c9d.mp4?token=HBhvgLAie26tJ9O4CBr-KxlenOOZDthQe8VlemBL_WRTrGVO_G29ue-9O7VLbL_pBv5ijnxleRMinxJj3tOAEyGEjkOoDW6f-VAxIQJaVOmLJn_eqBpUnXzabHA5Cwop7joE2IalKZbElpxwRGeoOfHT-Acx_min0AgqCHiqufA73ntp_IR-i4YaShq5cpZzy287rXvW9crdoSVcFMjp1q9U4-5SVXX9MzdnJIPQiU3yNT9NSsN8dEyPS_tKrdi07iafSSwWsxd1_s0sGXWCQ9FZSxM_rdYxeNvzg1lAypyLWHeeohKsmdHIIAzFQC1irG1uJiWZ0GcOWHvGhWPusw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از لحظهٔ اصابت پهپاد به مقر تروریست‌ها در اربیل عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/676883" target="_blank">📅 08:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676882">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cbb6ca0bd.mp4?token=CobBhiiuN_OPI6ysH8zi7Ot2H5-oeAyc5p4xbq2QX-0w5d25UTiYB7RYyh9ZVOvIlWSNT9DvdArP4M7eLgOYSUo7hoNrO0mOp9DF1dGM6WhbMNBvdeTPvwFRPpYB5m0OulIB_H3flzJxeW8ZrU_GH3qO8tSwwi40QPwXpVN-YlNu1XytrG-nzFK27wT4t6JlK9KlBdLaYmM83hlaw2-VTG87V_AWlmagvrWFatTIEQHlSQ7I5b8KOZQp-x-p-BBeoa-pCZG0gad_JO1KmwpJN0vgYJLLdxJQ67CSdHXjKqKJJqIlzH2_hnbdvvPlMtjxojAEhvf7EP23HhG_iy-vEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cbb6ca0bd.mp4?token=CobBhiiuN_OPI6ysH8zi7Ot2H5-oeAyc5p4xbq2QX-0w5d25UTiYB7RYyh9ZVOvIlWSNT9DvdArP4M7eLgOYSUo7hoNrO0mOp9DF1dGM6WhbMNBvdeTPvwFRPpYB5m0OulIB_H3flzJxeW8ZrU_GH3qO8tSwwi40QPwXpVN-YlNu1XytrG-nzFK27wT4t6JlK9KlBdLaYmM83hlaw2-VTG87V_AWlmagvrWFatTIEQHlSQ7I5b8KOZQp-x-p-BBeoa-pCZG0gad_JO1KmwpJN0vgYJLLdxJQ67CSdHXjKqKJJqIlzH2_hnbdvvPlMtjxojAEhvf7EP23HhG_iy-vEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به‌ اندازه نیاز خرید کنیم؛ از خرید و انبار کردن بیش از نیاز خودداری کنیم
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/676882" target="_blank">📅 08:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676880">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7544b67e8d.mp4?token=FZNEMRJkyrEVkCgEe9ir3y7DUhaQe4xama8LYqF5IbO6PjKsvO0UZvKCqb8UVGicUI2qPZW5N_BalkwC1Ep4GjpqcVPPoPGLIJ7lVUZW0CAoE0SWGpr8DDeW_G8L_8ifbjpte71RsH5Y7Gm8b0dYtzcANz8PCao91sulMm7MX0TrCx9Yd1RNwL4HAdgZ2LLnFdemNlw7I2edIs4cwTrnlI_4yaloUnalhHZfCqIhp1HQTVqXsg_dQY_tbYbr47YTU5citbc2zG3T-jZbg8tdWgdLzMa_O2FG4ZlIfcWoYjfH_uwTKZ_EPnLKDZhpx4_qQiO1QhllTKtNLgbFFbc5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7544b67e8d.mp4?token=FZNEMRJkyrEVkCgEe9ir3y7DUhaQe4xama8LYqF5IbO6PjKsvO0UZvKCqb8UVGicUI2qPZW5N_BalkwC1Ep4GjpqcVPPoPGLIJ7lVUZW0CAoE0SWGpr8DDeW_G8L_8ifbjpte71RsH5Y7Gm8b0dYtzcANz8PCao91sulMm7MX0TrCx9Yd1RNwL4HAdgZ2LLnFdemNlw7I2edIs4cwTrnlI_4yaloUnalhHZfCqIhp1HQTVqXsg_dQY_tbYbr47YTU5citbc2zG3T-jZbg8tdWgdLzMa_O2FG4ZlIfcWoYjfH_uwTKZ_EPnLKDZhpx4_qQiO1QhllTKtNLgbFFbc5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای رایزنی گراهام و نتانیاهو برای تعویق حکم بازداشت لاهه
🔹
تصاویر تازه منتشرشده از گفتگوی سناتور افراطی و جنگ‌طلب گراهام، با نتانیاهو نشان می‌دهد دو طرف درباره راهکارهای به تأخیر انداختن روند صدور و اجرای حکم بازداشت او از سوی دیوان کیفری بین‌المللی (ICC) رایزنی کرده‌اند.
🔹
بر اساس این گزارش، گراهام در این گفتگو بر جلب حمایت دوحزبی در کنگره آمریکا و افزایش فشار سیاسی بر دادستان دیوان تأکید کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/676880" target="_blank">📅 07:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676879">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHcLfTjDls7K150yirFccCvD8yxbwChp8mPTqYz6f5mmLZnlQnuHCOGZt8Z8g5nF8QrLC33QQ8iSbofdCOZjGkZlI1EDGQPhuyhpBenkXh60I-Ubycgm6vYyyZjIIEaZB-r-WftanceQSNoZWY_XAdC03Sk6MS09WZdeBcDb-5X6mXYeeryGMqXy2wMZV24SBBkJVmNuWOwy6sc-WXrgjrxT8F5sE5ypSvW30ShkwIQ2uosElCt-HfSbCbwxBDhFxRnJ6T1scScienZ38Y_HN9WjwwxKS2UNQUZbgVF97uDt8kNUaggMN3eGHB_8_2RnZKyU8rMaeATk8JJm_CMbqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۹ مرداد ماه
۱۶ صفر ۱۴۴۸
۳۱ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/676879" target="_blank">📅 07:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676878">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=Vh_h9hl_KZt3PaZ97oAGVZa9MSe43FiVpsOJJDcCFKx5t_d57dat3KaQiITNHrebRHFumpBA3CPtKuzU1k8r3OyP1QDXDJ0jC1J2YqTpu2EPTvZoYpkMGZUNIlEljesb4-dlWgglC_8GsMUNmPnu7djoiXoHcs_PdSk4bXY4kRFGPy41y_Gh7FAt0knbr2d6UTY7GZoNjfjgpKxIktAGDz99M1TjNIS7ZP9jmjLwmciAElFrWvutFLLBBK9MlzrN2KyLQ-qxZt-XgCtKCi5wQlSFrUMOfeM8uNqwtzK1360xS5yxDOOt8B4vWfzobmlwMrQXRcqD3aqq0zsA0Rk6Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=Vh_h9hl_KZt3PaZ97oAGVZa9MSe43FiVpsOJJDcCFKx5t_d57dat3KaQiITNHrebRHFumpBA3CPtKuzU1k8r3OyP1QDXDJ0jC1J2YqTpu2EPTvZoYpkMGZUNIlEljesb4-dlWgglC_8GsMUNmPnu7djoiXoHcs_PdSk4bXY4kRFGPy41y_Gh7FAt0knbr2d6UTY7GZoNjfjgpKxIktAGDz99M1TjNIS7ZP9jmjLwmciAElFrWvutFLLBBK9MlzrN2KyLQ-qxZt-XgCtKCi5wQlSFrUMOfeM8uNqwtzK1360xS5yxDOOt8B4vWfzobmlwMrQXRcqD3aqq0zsA0Rk6Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله بیست و هفتم عملیات صاعقه ارتش؛ مراکز راهبردی آمریکا در کویت هدف پهپادهای ارتش قرار گرفت
روابط عمومی ارتش:
🔹
در بیست و هفتمین مرحله از عملیات صاعقه و در پاسخ به تجاوزات اخیر ارتش تروریستی آمریکا به کشورمان و حمله وحشیانه به  منزل مسکونی در جزیره قشم، ساعاتی قبل، «آشیانه جنگنده ها»،«سامانه‌های ارتباطات ماهواره‌ای» و «انبارهای تجهیزات» این ارتش کودک کش، در پایگاه احمدالجابر کویت، هدف پهپادهای انهدامی ارتش قرار گرفت.
🔹
پایگاه احمدالجابر کویت، نقش عمده‌ای در عملیات های هوایی و نظارتی آمریکا ایفا کرده و فراتر از نقش عملیاتی، از کانون‌های حیاتیِ پشتیبانیِ هواییِ برای ارتش تروریستی آمریکا محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/676878" target="_blank">📅 07:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676875">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb71f4ae0.mp4?token=M_PO9-reKAGTC2y1b26khQrFBDvLEFQ-2NWpxrgjNRijERsx2aJwJK6t2ks3FerYI2j5tPK8vinJXg0fQhcM8R7E_Cbw_fjji-SXrZJUpmMBp8HnW7LnSebOJFvAQNhbgO84FtcpNNgAxDLAvOCfeHIo6YoNtAh9PmOBJLnBQfIMbkfvxWYtsto89NfsnwBPCOPefR6X5RdtTg7mTaOcotpN0YA9M4CSBA_WHe4X-FVTjl9WSVBr3vS2cwIY34VnDIrrAZeIu2xhcKrswJ2ieAIfoOqjGcFTDTw7oULMtg7ilEUvBKT0KpFA03mWbhx2PmI6D3RuSrEwPuggC_7L2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb71f4ae0.mp4?token=M_PO9-reKAGTC2y1b26khQrFBDvLEFQ-2NWpxrgjNRijERsx2aJwJK6t2ks3FerYI2j5tPK8vinJXg0fQhcM8R7E_Cbw_fjji-SXrZJUpmMBp8HnW7LnSebOJFvAQNhbgO84FtcpNNgAxDLAvOCfeHIo6YoNtAh9PmOBJLnBQfIMbkfvxWYtsto89NfsnwBPCOPefR6X5RdtTg7mTaOcotpN0YA9M4CSBA_WHe4X-FVTjl9WSVBr3vS2cwIY34VnDIrrAZeIu2xhcKrswJ2ieAIfoOqjGcFTDTw7oULMtg7ilEUvBKT0KpFA03mWbhx2PmI6D3RuSrEwPuggC_7L2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تازه ماهواره‌ای از آسیب به پایگاه علی‌السالم کویت در پی حملات ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/676875" target="_blank">📅 06:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676871">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4bbc91c80.mp4?token=dCs0HIVf_Cv-GvkLnPqnlx-HXMFnH-G_VjUzRg2P79ZTxugwUzYxD4saYa7J6A1xRnsrNFBs_Z0tk1Zl4FXcXIBSauRofF3Of3EOMnAjteSRLQEUOTZsgCh2FRVdSudbXJCu4Ps1BJnFqWqXo6MOTZXq8y3njmTh-ucKDshqoN0sCFH39tfLbwR43-_i6x3dLI690H6WSGp3OPOvbdFwdKO1ZI5PEHWYWI1s3298JP0HyMcrQg9cp0YO3TdBU9vY5XrUWA2_NPy-NhvgtuwSCUmaGz4EdAHwrE7Qk2Sk25bTt_wxFBdrI1bD-7xFevVT0tKpzBF53hIoB9AWNToYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4bbc91c80.mp4?token=dCs0HIVf_Cv-GvkLnPqnlx-HXMFnH-G_VjUzRg2P79ZTxugwUzYxD4saYa7J6A1xRnsrNFBs_Z0tk1Zl4FXcXIBSauRofF3Of3EOMnAjteSRLQEUOTZsgCh2FRVdSudbXJCu4Ps1BJnFqWqXo6MOTZXq8y3njmTh-ucKDshqoN0sCFH39tfLbwR43-_i6x3dLI690H6WSGp3OPOvbdFwdKO1ZI5PEHWYWI1s3298JP0HyMcrQg9cp0YO3TdBU9vY5XrUWA2_NPy-NhvgtuwSCUmaGz4EdAHwrE7Qk2Sk25bTt_wxFBdrI1bD-7xFevVT0tKpzBF53hIoB9AWNToYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش در اسپانیا
🔹
ده‌ها هزار مهاجر مراکشی با هماهنگی  صهیونیست‌ها، وارد اسپانیا شدند و حالا امشب تعدادی از شهرهای اسپانیا رو به آشوب کشیدن و ماشین‌ها رو آتش زدن و مغازه‌ها رو غارت کردن.
🔹
این آشوب‌ها بخاطر حمایت محکم دولت اسپانیا از فلسطین، لبنان، ایران و…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/676871" target="_blank">📅 06:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676870">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/676870" target="_blank">📅 04:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676867">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac84668d0b.mp4?token=F00UAQ8vHjcnlzacaoJYYFPyYFV_shKHMS1LT1u4GJV8pXYQaobyaHrloueI0X8Y6AbCtDv2MV27uzTAue9VzHgFBroMqoXW3tQEn3vOTRa1yTx67lJbophe27QnCHAzHKdSQz5mn25vXIP0qQ3UjjOdd2ISObrN0NuBmGoQeG_e5_k43E1yivoo-aEvhR1V-vYNc2DiJl0eqvJ0AbmCNy6Uxh3oZWa5NzqbxxyDEM9wVo-O5Sutprpjh3ESWDz9FX9agnYkVcNAiLRCCpW5Ixiv9dT1Rm3M3gKS8g2QdWDfq_DabT7cHbpiyfSrwsBgmcDBk7KwTmHQkbE0VcK8dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac84668d0b.mp4?token=F00UAQ8vHjcnlzacaoJYYFPyYFV_shKHMS1LT1u4GJV8pXYQaobyaHrloueI0X8Y6AbCtDv2MV27uzTAue9VzHgFBroMqoXW3tQEn3vOTRa1yTx67lJbophe27QnCHAzHKdSQz5mn25vXIP0qQ3UjjOdd2ISObrN0NuBmGoQeG_e5_k43E1yivoo-aEvhR1V-vYNc2DiJl0eqvJ0AbmCNy6Uxh3oZWa5NzqbxxyDEM9wVo-O5Sutprpjh3ESWDz9FX9agnYkVcNAiLRCCpW5Ixiv9dT1Rm3M3gKS8g2QdWDfq_DabT7cHbpiyfSrwsBgmcDBk7KwTmHQkbE0VcK8dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش در اسپانیا
🔹
ده‌ها هزار مهاجر مراکشی با هماهنگی  صهیونیست‌ها، وارد اسپانیا شدند و حالا امشب تعدادی از شهرهای اسپانیا رو به آشوب کشیدن و ماشین‌ها رو آتش زدن و مغازه‌ها رو غارت کردن.
🔹
این آشوب‌ها بخاطر حمایت محکم دولت اسپانیا از فلسطین، لبنان، ایران و محور مقاومت است که پروژه آشوب‌ها توسط صهیونیست‌ها در این کشور استارت خورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/676867" target="_blank">📅 04:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN_vXyF_XOVLfMiPh3yEF9VErx4nH2Mp8pX4Q7nyTJ-lp4bP2MqCNAMYR6VD7q_4z0lyl9UT0K_lBo53tODiDpTlI-6krlwJg05gbkdOErxdBXVIWCIOyd7h0beXaQ3TRTcl3GZXvFuNUV3KsyNH4PAZ0pWAhoBU-plEzjMwZkCTdMgHFyX8JxMsyTkAIo8uZzRwfesWRXGpmbHWs3USTvkN4OrEkzHZsv5jKImLsKi1UBEepbFVsCpjszwVBijQaBPradeqqld-LoyUa7HEnYAYOlZLXHxsm4lkanjGEF18c1h7-xNK2KCycXd5E2bapi4r4MRstO0HfGUJGpbqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای هشدار دهنده E-3G همزمان با حرکت تعدادی از هواپیماهای سوخت‌رسان آمریکایی که از تل‌آویو و ریاض می‌آیند، به پرواز در نزدیکی کویت ادامه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/676865" target="_blank">📅 02:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676864">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0PXIq6hybZmGpQT6-YgNgB6MeR1Wt1DisuH3YCT2OVnMLwsElBl2AbtF3RdA0wdqH9PoshiFGgaZJfhax3WRoKecD9V96Q2JzBhuND7xjiAA-s51Cqr7X4uRJ17e1lv1mk0Fq1QnSu8so3LHwTolMMxwVgZof8oFWPDxgy5mCr9wnuUry5Q4N6sPgYPSKIF0tCstyJO9vB157hqcnlyjvr8wblSnjmJ7qKxZkjl7tkC788jNyQyHaJkl1NH3wziEY4pmKDwsdd7ltGpJkaU_H0s0DUqaeWi9_fVVD0V7OD9JTADCPNwwP6E2GObdyCENsqzcvmP5m8UrmWFPKuGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از حملات تروریستی عربستان سعودی به عراق، ملت عراق تصویر ولیعهد این رژیم خبیث را روی سطل آشغال ها نصب کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/akhbarefori/676864" target="_blank">📅 02:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/676863" target="_blank">📅 02:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/akhbarefori/676862" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/676861" target="_blank">📅 01:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676860">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
احمد الشرع با بن سلمان تماس گرفت
🔹
رسانه رسمی سعودی ادعا کرده که احمد الشرع در تماس با بن سلمان حمله به تاسیسات نفتی سعودی را محکوم کرده و این حملات از سوی نیروهای نیابتی ایران در عراق انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/676860" target="_blank">📅 01:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676857">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48c959043.mp4?token=Sgv013d-JfenihorM5g3BA9NUpkQE-vZAYlw0Kj2P6vCo37VRA68z47HFM5bsyEpw8wHAzmbC8OT1MODdoc4i7mO7y4sAaH4embyLCWlS2xrdpn4cijZUxJ_U1jtLiTrWhZ5LMfPsN2V-XfrGkjx31ud4hLiRAb9r9j65hQv07Ca9IS9ncCu5BH45Q8m-_x8fd-htwW6daBeMuRQuEzjFjttXJq73d4Nocu0nEkie8lIEhan32beQKOqz8IiQhtCV2NNtFbAj-ZwiXwqaQfhkDQIeFeoSli1RBLm1Ufyj_hiBXGypZNJBMQfm7tHPbgzrGjg2hZNRuyiQFcCJdIIUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48c959043.mp4?token=Sgv013d-JfenihorM5g3BA9NUpkQE-vZAYlw0Kj2P6vCo37VRA68z47HFM5bsyEpw8wHAzmbC8OT1MODdoc4i7mO7y4sAaH4embyLCWlS2xrdpn4cijZUxJ_U1jtLiTrWhZ5LMfPsN2V-XfrGkjx31ud4hLiRAb9r9j65hQv07Ca9IS9ncCu5BH45Q8m-_x8fd-htwW6daBeMuRQuEzjFjttXJq73d4Nocu0nEkie8lIEhan32beQKOqz8IiQhtCV2NNtFbAj-ZwiXwqaQfhkDQIeFeoSli1RBLm1Ufyj_hiBXGypZNJBMQfm7tHPbgzrGjg2hZNRuyiQFcCJdIIUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران در اسپانیا به خاطر سیل پناهجویان از مراکش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/676857" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676854">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A28hifWJqorG6TWl8AaIUAsdNwraPRRAie_cE5F6Juie8ydWSoFaQXAeT9OkVdmr4IwNcFZ9DVXrD1mxnLAFnweBt0AMkvmSUk3dbNLUVhoLnQbROSufMEQUUgz_wqBR2uHz7E2Rq2P1yNqw7PUAGAqkEB5PZbRYQC9kcevNndWcOKQHmEPYw79NNCfHvbGXdzeFwb3RpJ2J91Du9xI65IwqYOsEQzdJBSpxK7DRdev5De6g70UCHQisMEiAiGY1ecvP28vruChnFvaoi63VHJ55dUFiGnk0QF-IIY4uXGPCph9EOivwD0-VErHpqUTZR4XKG8VK2Pf1h_eGb0GIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aa4dbef7.mp4?token=kI2N7l9jcY5DTKM5jWZehhQcia1HQK7y-9G1kj3H5CItqAIexTlGjU3H7OmJcHWos_blP_JJmAuHzOH1weBMkFfbkQ4JlO12KKa6pOcCl6qUvswaQ3Oq2ONxsYy15JpTphh28ciYPb1CLCgOcMohCwkC5ANTdE_eMIwwVOraJ-nI6qzhFqAcDllGAvr9hON4Y8_cpFPLeD0pEAqqnwOfIlNiLZA-CAxGkevBkmiU0dimogtuzGSzEx864bzGfLNuaoK2tyKZoChXyVikSndyDKS8SOXS92d3_mYLzZFD6ugC_rckZChP6xXeuZGrxA_1JfcHKXAjQzm6hDS48bGJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aa4dbef7.mp4?token=kI2N7l9jcY5DTKM5jWZehhQcia1HQK7y-9G1kj3H5CItqAIexTlGjU3H7OmJcHWos_blP_JJmAuHzOH1weBMkFfbkQ4JlO12KKa6pOcCl6qUvswaQ3Oq2ONxsYy15JpTphh28ciYPb1CLCgOcMohCwkC5ANTdE_eMIwwVOraJ-nI6qzhFqAcDllGAvr9hON4Y8_cpFPLeD0pEAqqnwOfIlNiLZA-CAxGkevBkmiU0dimogtuzGSzEx864bzGfLNuaoK2tyKZoChXyVikSndyDKS8SOXS92d3_mYLzZFD6ugC_rckZChP6xXeuZGrxA_1JfcHKXAjQzm6hDS48bGJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای شدید در جنوب لبنان
🔹
بنیامین نتانیاهو و یسرائیل کاتز وزیر جنگ رژیم صهیونیستی در بیانیه مشترکی مدعی نابودی و انفجار یک تونل متعلق به حزب‌الله در نزدیکی قلعه «الشقیف» شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/676854" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676853">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339d6a9891.mp4?token=h5hRYZX7YxlzID75d5rE82GtwTXhwNOOszQbgEFsJ1R62OG7yre7MA0DP2b2E8zWyCbUVT62ohOshmbEGc_yAAYDNHyT9f21LCDRwTrPrguVmv_ZCw4GWGJ-5EGbEyGpkqrrxDhn2e9AX6s2gHUfKCWRDz1zbtlK1dMNhU1BFKoXe2zeZndBW4L-gGoYjGJDrtsT11BkV4xeEqNw1OUJ63ste4LisFHPOW_DRBhanEejk3ZyPZVWgKEyU1-I5UCvPyUzdFPhw2yuYMn4EVlvg4MiozQdp0mEZTlu8BHUerlAPVQrv4oHvIofFx6oQp1cFzqDLyN8ewWSaOb_3V6fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339d6a9891.mp4?token=h5hRYZX7YxlzID75d5rE82GtwTXhwNOOszQbgEFsJ1R62OG7yre7MA0DP2b2E8zWyCbUVT62ohOshmbEGc_yAAYDNHyT9f21LCDRwTrPrguVmv_ZCw4GWGJ-5EGbEyGpkqrrxDhn2e9AX6s2gHUfKCWRDz1zbtlK1dMNhU1BFKoXe2zeZndBW4L-gGoYjGJDrtsT11BkV4xeEqNw1OUJ63ste4LisFHPOW_DRBhanEejk3ZyPZVWgKEyU1-I5UCvPyUzdFPhw2yuYMn4EVlvg4MiozQdp0mEZTlu8BHUerlAPVQrv4oHvIofFx6oQp1cFzqDLyN8ewWSaOb_3V6fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از عادل فردوسی پور و وزیر ارشاد در حاشیه مراسم یادبود اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/676853" target="_blank">📅 01:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676852">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/676852" target="_blank">📅 01:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676851">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f579c094.mp4?token=AOQuc56XXQcAhEpgpHytTtz1vQSDOQLMj1Ts5SYTwSKZc9HkWB3Q9P2FWrKRQtGCNejBRCZkh2GZlMzDH6F3WNQKyth8EBdYjCfWzBHAibqVIL4b1jpJD1VYP_d44U6XCvr_WeqTDZ7Sq8ZviCbRRuL-KYgdhNUTkRJ2Gzbw8LqzhveL9hFzZhLyDmPzQIoJ-vuS6Pbv443F1sKjzGwn-DsW3dBNz4X-ycEzCU30EK1kmX4JjWAzP2lGCqqqxQkd81gnfeX02j4ddzGc0PswXFgx-__guW199O8umPCT4i26IMtNK8J9h4Q8RTvwCXu9VtMlUggqpwNHMkv22G6r_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f579c094.mp4?token=AOQuc56XXQcAhEpgpHytTtz1vQSDOQLMj1Ts5SYTwSKZc9HkWB3Q9P2FWrKRQtGCNejBRCZkh2GZlMzDH6F3WNQKyth8EBdYjCfWzBHAibqVIL4b1jpJD1VYP_d44U6XCvr_WeqTDZ7Sq8ZviCbRRuL-KYgdhNUTkRJ2Gzbw8LqzhveL9hFzZhLyDmPzQIoJ-vuS6Pbv443F1sKjzGwn-DsW3dBNz4X-ycEzCU30EK1kmX4JjWAzP2lGCqqqxQkd81gnfeX02j4ddzGc0PswXFgx-__guW199O8umPCT4i26IMtNK8J9h4Q8RTvwCXu9VtMlUggqpwNHMkv22G6r_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر شهدای حمله آمریکایی-سعودی به نجف اشرف رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/676851" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676850">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2544901f6.mp4?token=GZBrYJImeDm-tfXW-vhIBW7QpDjg7T_XbITvovkIlRxgFhcMwRTu-kjFcsMa8N1md02lkdF6qiBGBzkZ8wxGXdUC80jThUWAziGyiPYhGYcx9slE3EwuAsSAORtzmszG-yNGzZjVqF-cQ-eZVTGJIUfHxxxkm31Uie_4-2LpwTxoSkyNdxnRSO4OGKFJAmBj-puQtesuQXOdLP3CtkpqSFevZn4qQ46sFGbLO2DLcWzKnG9DrYtjFGKpJISj1ouyd2BAZEFWvwTnbR_S21OjdLomCme5-tmvW1Cl3kq_MQWdQicDXhB5f9yTtlsxMnNCBRhTqpfylbCswKtHlam7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2544901f6.mp4?token=GZBrYJImeDm-tfXW-vhIBW7QpDjg7T_XbITvovkIlRxgFhcMwRTu-kjFcsMa8N1md02lkdF6qiBGBzkZ8wxGXdUC80jThUWAziGyiPYhGYcx9slE3EwuAsSAORtzmszG-yNGzZjVqF-cQ-eZVTGJIUfHxxxkm31Uie_4-2LpwTxoSkyNdxnRSO4OGKFJAmBj-puQtesuQXOdLP3CtkpqSFevZn4qQ46sFGbLO2DLcWzKnG9DrYtjFGKpJISj1ouyd2BAZEFWvwTnbR_S21OjdLomCme5-tmvW1Cl3kq_MQWdQicDXhB5f9yTtlsxMnNCBRhTqpfylbCswKtHlam7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیماهای جنگی آمریکایی در آسمان استان نینوا عراق پرسه می زنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/676850" target="_blank">📅 01:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676849">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
‏
نتانیاهو و یسرائيل کاتس در بیانیه‌ای مشترک اعلام کردند که ارتش تونل‌های موجود در زیر قلعه الشقیف در جنوب لبنان را منهدم کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/676849" target="_blank">📅 01:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676844">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igbQAcQQ0GyIt8Myc8Sj8bjk53BhpOIdSSpQrfz1w7axbQ2qOCHrG-DSiNOV36Eh0DgmviWMBBzcnRIpZqiV3fLpBgnTqxwStwGblP8MZjstr7Dm4Nvb9704yOci6R4hA-ZI5WPCLnM8FykSxAXCPFa2PZKCbP0jLYBAi0tRBM0Yg7t63H9ClVglFPRrBqA3OTL9CDwvTgaGeTZpDQjC6lEx_li-qumEDbZIfUfuMTLgLPnkbEA5ulkIM8xc2qNLn70iq2vZxG12W-uz58NKTBv1Yx3Tzvbgb22X_2OFbpxtq8vC4wUXpNrvL_8UPSU1lO1ZBpiZR1jnb5ROzjJ1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svhxwxrTwWm1D2sL4EfMxSUJ__lZp-hIKcpliYnD1v_K_mm9Iewle49qTUhgmAV9Ubf82sVgwsclmKViNjD49UoDSAsBL7egMSmxgE0O6VtOQ1tKLXhMZa62w2NHNvbuIgdV23p7kRj7-eQ9wmNqx30oBqL85Xnu23HmM6WOKnDZ162tXFcQk8VEFetqmw8JIjefipLw4vFATxIV0w50-gG88mLi8aprP0K_11-li2vDdXqQ4odA6hTMcmSDgiBsBvyJTSfXzQDEcfczL1wCawfzAYtNsJe16-fBRVlV2MbeATKA_gXsfdAg0wP-jXcbpjUYoFkGw-znttFoL-pVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx8Fa8uqePLjFGDfv0A98A_3xJCLcws6bheBgd8fg7OqazpUs4_QUsIX5cufjVPQXd9FufYRtoTE23KetIzYoGH1pMxPnnQlW5ubZLDVz39c9bFIog5IXrfWFuM3fxEBVaV3if4Z_dnDXNlAM9GclNHSoOVvBrKTLZ8P9R_EenliklR96VRSosud3sX8Q3sbe56ozzFW11RlTHR99XQggFpgvhx3AbLGqtK3MiUd1jdA6m6JKrP5mp3cs1iwwLTZYvtVtLf0UZN_bsOCngKpDF0SzIIlLlWPYT6Qc7tsUNOAUoS0_CyB7esyI2uYbuGJ8WdBeFT8P_Zh5lfxGxBWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIIolyPKkWGC1IGKzxG9TM2cRIcNhfs2SeVCJG4w1fbaXpU5U7ThzegYbvfbRxsfbeqISrQWl4XkcLAh8T2IDwcj4F64tb7-H-oHB69UhYUHc3oI92UYG0lG8LEJTK89p4Nu7nTv0SHmW9R29AGnv8VU9300ZqZUAndxomlK72LvPovWXLGeyq6p0cHtpdFh2nJJV8QEzkRHY6Kckoq26OGkLLdg5OLXODfyExTAahpesX9RAAanQwfDnDPqXlp2RFJv8F_-6TjEM1MyA3U-y-gRFplRLTEfBtJPEzR3l5BuC1WJDgGFIdpMqCJvPjQvSI48yR_rk9MKPBzKTspp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SApfhH2oWPhYbF_i19nZuvW_aE5LMqbpsBT3mbhXiZMJHj1mZsqatUzmZ7ol-Hen5kvtPL1M2rTj-XXyrfsUUGbFhwBq_X9px34x_J1Rwup5XdcuQP0U2ioZDeW5M1jfR8K7VQIUNhFxQ8M9-gFMUKtr0cychALiN7kqfUyL5WpnLuzrSLT_JIxR6ldf5gwCdEtWTrZMcLS4OO7rjV5alWSbuQsFz3KOOvIeeoEBN1tvBoaCi399mF6xiAmecDabbOyDemlbhF2B6PDhZl6i1KHY6jB3yFYuedGnYf1tfd6hpgKPqH2AhWUUb15McahoUEUGKdCkFwQL7x1aZhnaew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
غروب زیبای مسیر طریق‌العلما به کربلا
🔹
عکاس: نسترن کرمانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/676844" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676843">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQzMY3uUy9GGHIjkH4A4JyYfqTOPcQ3wJHMDGrioRs5tLsufV3rfyGdWew3cu77HRhEs_Z0uU4N-VMhevn8Ug8JVTXn-NZ9OgpsiIJW_r-4y7zhQex3p_r1srXynN8NBDMQpCcgJDVVNffQP5NGtFoMWMVjy4-hhDx2q1vCeLAiSBqxhMsmP2XvHBdeAAiMsRspGm2SNxOsbvJjMIWnoYLFVWIlZdk59YyvtRoTkzvu83Gw3__8cJeHK-jqGNKRmHw4F7K-MFgCjRV8L9_dBitjFNCZzRL3lIXVtVIfeo3mr-16dUyvID2aZ5okcIHdIZDxdJVbrtBCcrSxhIyGIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عبری از انفجار با صدایی مهیب در تنگه باب‌المندب در نزدیکی یک کشتی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/676843" target="_blank">📅 00:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676842">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCNqHHV3n-qF8eHLG5Qm6-4kQ7WgBhQ3pIl7xl3Rzlzye9adLuLcHDt0NGDfPOBuO8zpvPRWIRjXfuEI23KMFQADnlHVhym5Ydp8LJ8uThAZw5GCMllznuQ-ZOQ7Ol7PCXrsJqTONh35HNTYNNw4raWy5CK1Ie20uh15t4ZbtrsoHkEqAHssno9e_gOV3EfQuKCPOeM7ewPZncIH3_9QRP5xL9MyyOkE-IRdnizj5-sXYDIb9SjCxe1IdktT8tI6yxsng_1KHfLFKO1PzItcwnfyLY4g7eOVtsuzMfNAAipMDKoxdz1xaFMuIYi4PNx7ZiArccyka08hCCrmv0V0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبح انتقام
🔹
شب گذشته حمله هوایی آمریکا با استفاده از بمب های سنگر شکن دو منزل مسکونی در جزیره قشم را هدف قرار داد که در پی آن پدر، مادر و یکی از فرزندان یک خانواده به شهادت رسیدند و دو کودک دیگر مجروح شدند. نیروی هوافضای سپاه در پاسخ به این جنایت رمپ استقرار و سوله تعمیراتی جنگنده های f۳۵ آمریکا در پایگاه هوایی الازرق را با چند فروند موشک بالستیک هدف قرار داد که سه فروند f۳۵ به طور کامل منهدم و سه فروند دیگر آسیب جدی دیدند و شماری از نیروهای فنی و نظامی مستقر در این پایگاه نیز کشته شدند
🔹
هشتصدوبیست‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/676842" target="_blank">📅 00:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676841">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d06e1b886.mp4?token=fuVzT2pc-U22eSiDrONH6JNQ-j_4rSzXMfOy4UQYZ5f25MY08d4Dbk7TOrrYxA8g5VQoLjXvhMTyQye89g9pMEnU5roWace_lSUgoFeGa7P9WePj2tuCAum9T-BoOvhizsCUw6IT93KaP2cYD_pjmjuK2ynJMjWV_hCOtkEARkopgtLpzxPlpK8NjG5lunLhzi7QQp7tDi6Se4SMFOaeugAW5tA9Sd-0kHdyFmGDznS_XiM_P4PyevHZHS0sP9CvB2CRSDqQhy4jNw0QYba7qbd7bZ9L14tDXtCDFD4QuNVdQQ1iTXfuR3zNeRdJQwQF45-30gRGszFmgVvS26O3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d06e1b886.mp4?token=fuVzT2pc-U22eSiDrONH6JNQ-j_4rSzXMfOy4UQYZ5f25MY08d4Dbk7TOrrYxA8g5VQoLjXvhMTyQye89g9pMEnU5roWace_lSUgoFeGa7P9WePj2tuCAum9T-BoOvhizsCUw6IT93KaP2cYD_pjmjuK2ynJMjWV_hCOtkEARkopgtLpzxPlpK8NjG5lunLhzi7QQp7tDi6Se4SMFOaeugAW5tA9Sd-0kHdyFmGDznS_XiM_P4PyevHZHS0sP9CvB2CRSDqQhy4jNw0QYba7qbd7bZ9L14tDXtCDFD4QuNVdQQ1iTXfuR3zNeRdJQwQF45-30gRGszFmgVvS26O3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت سختی‌ دور شد شدن از فضای مجازی به روایت تصویر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/676841" target="_blank">📅 00:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676839">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921eea2f4c.mp4?token=F6VNE7H7yUOb05xMxzUpRclSgYkvRVTNPIZh0Q3dh6xreyStSQvllXnhosiFW9TncUWhIatnnN8tFwHUlnosRWfDppogGA0eipg39Ku3UvD0eNaF0Gzq01JJ-nCbRp4c9P8lVje5on5hSvhpxstfPAq9TAEeLdTAjZq1WAB5oj4YGYhKb7jVsbtsKgIk3qheLjhf4xNdIsCLoq8qnLvPhYybvMhj8TFrgAtPnDcDLjhHVy2RAFX3CCHSsU6sQa42M69gmIBkx04vxwnZ8d9ch_Hid-4DS4JkfMvQXNLd8YnDTSWSLl-Ng930GKQle6yQTqVLgbkEMCAfe4AaBsXp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921eea2f4c.mp4?token=F6VNE7H7yUOb05xMxzUpRclSgYkvRVTNPIZh0Q3dh6xreyStSQvllXnhosiFW9TncUWhIatnnN8tFwHUlnosRWfDppogGA0eipg39Ku3UvD0eNaF0Gzq01JJ-nCbRp4c9P8lVje5on5hSvhpxstfPAq9TAEeLdTAjZq1WAB5oj4YGYhKb7jVsbtsKgIk3qheLjhf4xNdIsCLoq8qnLvPhYybvMhj8TFrgAtPnDcDLjhHVy2RAFX3CCHSsU6sQa42M69gmIBkx04vxwnZ8d9ch_Hid-4DS4JkfMvQXNLd8YnDTSWSLl-Ng930GKQle6yQTqVLgbkEMCAfe4AaBsXp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال جالب مامور مرزبانی عراق از زوار ایرانی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/676839" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676838">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hicfS2T_OruIghrm6dXaW5o4LqSSeSC7p5L0ZVVXWwrZvxVjdCiggnbdirXPFiwe4uZsTCGqjr-MmIhlCZMUFN-TqeM78NHfD4BQBbdc7VXeUuCOsCHfVd-Y7xaGR3a9zXtRpeuNM8F1AYicXcZLPwSHWgk6f25l2JDDPzQ96Zf16aQ45XyyfApyynpSxnn8Rjo0iTaccvP0fznkDexjUtpUtDE6kwQgmNl-ztvGk9gO3loqXas0GtviPAHX0GjETh-KBNG4c6P6hvsAssqV17If7QVmlTGicJmI858WeHGpijAzhjwqO9lEP2si6Ld78vJxT8dlGgEGn4lhYxXWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکمل ترک اعتیاد
‼️
‼️
✅️
کاملا محرمانه برای اولین بار در ایران
بدون نیاز به بستری بدون درد خماری 100%گیاهی دارای نشان
سیب سلامت و تائیدیه سازمان غذا و دارو
🔻
اطلاعات بیشتر جهت ثبت نام
🔻
📝
برای اقدام به درمان فرم سامانه زیر را جهت مشاوره پر کنید
👇
👇
https://app.epoll.ir/80475925
https://app.epoll.ir/80475925
در داخل کشور تولید شده
😍
😍
✅️
حتما تا ۹ام شب اقدام کنید تخفیف ۳۰ درصدی و از دست ندین
خدارو شکر در این اوضاع و شرایط
برای همچین اتفاق بزرگی
🙏
☎️
جهت مشاوره سریعتر عدد ۵ را به شماره تماس زیر ارسال کنید
👇
📞
09379940040
📞
09379940040</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/676838" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676837">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
جدید‌ترین تصاویر از حمله به بندر دمیاط در مصر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/676837" target="_blank">📅 00:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676836">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glgOi9Dlb0yFIh82KyS4RwH-6fMTrRhgrSPdzE4W7F4FnWLgqaYFg3pBTRaaJ7bGnmwlM8mdmX9husR2eGsy9j1PPKoucD7vlEaZuMCW4FQJT0NDwbE8LJCfiQjIByq0CJ39PltXt9s0SbR-0YJd-qyVbdgk5_29unjgFM4-wTb0m344GVpoNzDVFRsCOVN_7rBDx8JdUu6hoOQQG7wDUwy1JYveymlqZNfdJ69VD5Hf5vhQc3-Vlmz6pyaHRcClQn9WYpWH1se1ms5SL9J2IkvKak3fpgx4J6RU_MkkiR664NBKQiLyomcPKWNenMjE3ZxSwROMdFN7XQG4CoZtaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این تکنیک ها از هوش مصنوعی پاسخ حرفه ای بگیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/676836" target="_blank">📅 00:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676834">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG3NuoxcszluUnUzSOvQocemyp8y6yqExgmkQ1jaRG-fphJuaiMXf-NO-udMFiVccDrLPZi9h7otBgmoA1iimbETseR4SPurftpP6PH9vqb9Ee_eKK-qDPwh2-H9bCtBKbb0V6TumH1CbNPZ2FK2yDvgYIvv1XOHSUDEtDTVJaolLrUvoAeibxWzSPiZQ3KpFlXcQM1vLgUZBuIY-daWHuWCrg9mYynVL71WiyZo8YlBk5uNUKbgRrfjznxCGSQdmJ1G9cbnyhfq9OwGbm-alLAKcdeaFQsyTd3oUFPM1xbQdwZKlX-8teCL97XfESmEsNGYj8bhBrVPXSVNme5rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک موشک بالستیک روسی، کارخانه تولید پهپاد در کیف متعلق به یک شرکت ثبت‌شده در ایالات متحده را منهدم کرد
🔹
این کارخانه، پهپادهای تهاجمی هدایت‌شونده با هوش مصنوعی تولید می‌کرد و گزارش شده که کسی در این حمله کشته نشده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/676834" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676833">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bc94ec90.mp4?token=Xp1s9-juMqQqRYKjlFA_zou2fe-7U_i828Us1JzOHLrRS7siLOsfvvZZ7rJZDWqNE-zfdUF2-E6l7EaFgwV5xB4GdWaN9VS4ywU8ulQGj66GhwdbYfTg_Tgz7yFTHD-spG0ouoYKISb5R9z3MYQOuXqo26Hxr3iQ-Zv10Hi5cdyIfF_RXeqvAKnAqSzkj4ScGeQ4xvAm4k-7Zi7iJZOstgKJOSz2YdWEsvieBAwZNT0YGNiUB9S8zoSlTAazN66Ry7gmCWBaabEOmh4uPyduMVzrED82TYdlrJVRckPXUlO8JHQq1qG5kpBWfpTrMq2KVMAs4sbKgr6hTJWzysQvghXI2FHWb3yTuh71WOeNZuPwgYymh5t6k4ROpZOpPUzSwlEPCsgIpYFCnRZLNJnAAhai4bDUm-E3rirCaPueEfmNo1pj5Rk3y2DYWf9MZ4uSjoqFTsgWfaNmM3qGgwEfUR-qaXi_BthhR2OxXp1jfrFUw3e_C4vdPbxgGU7Ag-AxCWamRmZqNBSxNc1XRQjsW89KKoNPzDFN0B9DO6MJGfDnJgLNZ_gjtGtRxO70xiUuyAYqjn6k1Sp_3yh6f-NkfUk8jDC3VDONNyS4qxdNDHHfviDbyv1ogBnzhen5AJ8dVG9qJ0SYJDMiJnE7zCthJX9mbAbJtQ1XCTmB9PJwyw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bc94ec90.mp4?token=Xp1s9-juMqQqRYKjlFA_zou2fe-7U_i828Us1JzOHLrRS7siLOsfvvZZ7rJZDWqNE-zfdUF2-E6l7EaFgwV5xB4GdWaN9VS4ywU8ulQGj66GhwdbYfTg_Tgz7yFTHD-spG0ouoYKISb5R9z3MYQOuXqo26Hxr3iQ-Zv10Hi5cdyIfF_RXeqvAKnAqSzkj4ScGeQ4xvAm4k-7Zi7iJZOstgKJOSz2YdWEsvieBAwZNT0YGNiUB9S8zoSlTAazN66Ry7gmCWBaabEOmh4uPyduMVzrED82TYdlrJVRckPXUlO8JHQq1qG5kpBWfpTrMq2KVMAs4sbKgr6hTJWzysQvghXI2FHWb3yTuh71WOeNZuPwgYymh5t6k4ROpZOpPUzSwlEPCsgIpYFCnRZLNJnAAhai4bDUm-E3rirCaPueEfmNo1pj5Rk3y2DYWf9MZ4uSjoqFTsgWfaNmM3qGgwEfUR-qaXi_BthhR2OxXp1jfrFUw3e_C4vdPbxgGU7Ag-AxCWamRmZqNBSxNc1XRQjsW89KKoNPzDFN0B9DO6MJGfDnJgLNZ_gjtGtRxO70xiUuyAYqjn6k1Sp_3yh6f-NkfUk8jDC3VDONNyS4qxdNDHHfviDbyv1ogBnzhen5AJ8dVG9qJ0SYJDMiJnE7zCthJX9mbAbJtQ1XCTmB9PJwyw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز بزرگ تنگه هرمز؛ چرا غرب از این قانون حرف نمی‌زند؟
🔹
همه می‌گویند ایران حق بستن تنگه هرمز را ندارد؛ اما آیا واقعاً متن حقوق بین‌الملل هم همین را می‌گوید؟
🔹
یک ماده قانونی و نکته‌ای که کمتر درباره آن صحبت می‌شود. اگر فکر می‌کنید پرونده تنگه هرمز فقط یک موضوع سیاسی است، این ویدئو نظرتان را تغییر می‌دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/676833" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676832">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b287c28801.mp4?token=UgKaq7ONZdWrzKKApBQckIk5jMgOjKSTo2pn8iyHma0jrbOcHbIv0N2pNFqAcW-4LycfdizQgk0RXSohEq5We37IfFQyYx-seQ0jQpouh0D2zeplvkffA3VRZodwnouDTacNIL4rGnSSrR-MW7YNWJWNarRAgV2gf1vo8lPOQ2ytRLvjeRIPysY3FS_iO1u6865lYxeGlHhsKSxnDwmHGYLqFW-6KxCdrSwXTeslyVOeCvi9iSUnGKNMdU-3m5laANw6xoaHayC0gUuR4XBdTOo8L7yjsXqMoJiL5IK_0byHb6jV6p1JxGNtWzkkYHh_K2MKMHOW6sEPjPvpGLL6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b287c28801.mp4?token=UgKaq7ONZdWrzKKApBQckIk5jMgOjKSTo2pn8iyHma0jrbOcHbIv0N2pNFqAcW-4LycfdizQgk0RXSohEq5We37IfFQyYx-seQ0jQpouh0D2zeplvkffA3VRZodwnouDTacNIL4rGnSSrR-MW7YNWJWNarRAgV2gf1vo8lPOQ2ytRLvjeRIPysY3FS_iO1u6865lYxeGlHhsKSxnDwmHGYLqFW-6KxCdrSwXTeslyVOeCvi9iSUnGKNMdU-3m5laANw6xoaHayC0gUuR4XBdTOo8L7yjsXqMoJiL5IK_0byHb6jV6p1JxGNtWzkkYHh_K2MKMHOW6sEPjPvpGLL6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی حتی متحدان هم برای نتانیاهو ارزش قائل نیستند، استقبال از نتانیاهو با شلوارک
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/676832" target="_blank">📅 00:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ste7UOOgYjLgZWo4Z0Q0_L60B37CD5vJRH7aSFJhXfRoTWB3SKvSgAOFHt-8YC_htzyvJ9rIUUViD4NM909Sx1u394QPh-WJ8B2oNrq0pQqgz-fzlG0o1N9mR0FCPhLeDt9_j9u-UVACdgJ-qt2yTRXvxchyUJDfwOPeDugyZ4Nl5uwwY1d3VL_HiwRjb0iN1UIgOCEonfkSJ4YLlobDZhZmNnA6GMOT0rt66qTFZnlX7JcZ5oDGNJh4To9BcQWdaY9AAibgb-Gp8NQgpvt-JP0yyWpnoKY_DOTxOxhEMHW7sE_J864HIJikqFwzwCxVTpPNae3f2okizLm2vyzV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/676830" target="_blank">📅 00:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcNOzD01Cb58EU9Scr4scTfPj6dezUr5DBCH_ZFxW048kBnj8cUP8cE79sx6_HJvmTtGskWNYF-ay3kbdDjgAoIqGV8q_OzFedsWWBq87QIE2Trn2Wt7wTLMaxbsqMBfePQgxkJXkKxLCavpU6sN0mBMZkDu369zy8bDIX2Z5_-jNks1VkSSiCvWWC8Q2HpKMflQq-GZKjPQcf-mjmRtleWECYN0QckuN1c83wwLZCT_C56ecR_KAfvuTkkirHk5Wii9-cVNq-g3Ue6U3eqklwA3hMx-7CEGEvLOxRtNh96y9rkyLZHtGXfesQXDrL09hdJECPg-AJ2WUUnZ7YecQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکا سیلی‌هایی را که در میدان نبرد می‌خورد با جنایت و ریختن خون بی‌گناهان جبران می‌کند، تاوان خواهند داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/676828" target="_blank">📅 23:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0d758643e.mp4?token=uIwP4Vvi5iRMWumC4l2vXA8zhH0d7o4SFt2Ix6WSbsEcbOAr8AtfZpvRsqE1ryxKkgMdE3Y9cD1DVW-MOwk5Lx3CrrNoAsCbfGxPfQJ3mJBBEP5vnWq5UaG73iJY0rKzLSeFLs9MyKfI4wi97TdyjbZ8AI4C-B0-XlmgoFMru9NMdPhnYMktY-f0sBoJ6NyKHWquBa66zD8k5f6ZuHcBeC3KO2rq2sSO3keOO7OhMCrOMqDheiuToDEcZBL5Yu1zZCSSJIt0bfxxbr5Ry_kqKdxgWJof-k-dgM_CLAJw0ZUxAzAFL8GUT4ERongHa8YVPt84GUC9MfjC3ccEDPyjSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0d758643e.mp4?token=uIwP4Vvi5iRMWumC4l2vXA8zhH0d7o4SFt2Ix6WSbsEcbOAr8AtfZpvRsqE1ryxKkgMdE3Y9cD1DVW-MOwk5Lx3CrrNoAsCbfGxPfQJ3mJBBEP5vnWq5UaG73iJY0rKzLSeFLs9MyKfI4wi97TdyjbZ8AI4C-B0-XlmgoFMru9NMdPhnYMktY-f0sBoJ6NyKHWquBa66zD8k5f6ZuHcBeC3KO2rq2sSO3keOO7OhMCrOMqDheiuToDEcZBL5Yu1zZCSSJIt0bfxxbr5Ry_kqKdxgWJof-k-dgM_CLAJw0ZUxAzAFL8GUT4ERongHa8YVPt84GUC9MfjC3ccEDPyjSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش نتانیاهو کودک کش به ویدیو افشای اطلاعات ملانیا ترامپ توسط ایران
🔹
آن‌ها میخواهند ترامپ را بکشند، همین تازگی یک ویدیو و برگه اطلاعات درباره ملانیا و بارون برای ترور منتشر کردند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/676827" target="_blank">📅 23:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676826">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز: امارات ده‌ها حمله هوایی علیه ایران انجام داده است، اما این موضوع را به طور رسمی اعلام نکرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/676826" target="_blank">📅 23:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676825">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8aWLI9cXjlLWQffZZMfD8UR5xeSmXT26BH51m-0rHXMHnlztOvvLgwYO6yvVmYuyMz9xxcejBipZa6SpigFw2tmuURDqCwLt58kH6h4B8NJIEwxHB_u2vs4Cmzd-9G4eiKEVrHsVFSbXY--9zNkbJsgOzv5P4tFdef-YD08R1uvRC3IAV3lnMZ16ZwrnbOxkI4l1qnca23xpjg5PUJRlQaqCTZeO7BjUwqMLcvsXWXAScYNDYhtLwYEWqDX8NYmCv5UTnwlbfkbNmkDcMh6KsnKJ4BiUJTyxBWtysrBJhyaXu9Nxrsys5R3SjehQKNU27cHdQ4Oalg1XvgC0U32zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس: دو سوم آمریکایی‌ها می‌گویند جنگ با ایران ارزشش را نداشت
🔹
طبق نظرسنجی جدید مرکز تحقیقات امور عمومی آسوشیتدپرس-NORC، حدود دو سوم بزرگسالان آمریکایی می‌گویند جنگ با ایران ارزشش را نداشته است. این شامل اکثریت قریب به اتفاق دموکرات‌ها و مستقل‌ها و همچنین حدود ۳۷ درصد از جمهوری‌خواهان می‌شود.
🔹
اکنون تنها ۲۸ درصد از بزرگسالان آمریکایی نحوه برخورد ترامپ با ایران را تأیید می‌کنند که نسبت به ۳۴ درصد ماه گذشته اندکی کاهش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/676825" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بودجه حوزه سلامت از ۸۲۶ به ۱۲۰۰ همت رسید
محمد پاک‌مهر، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
بودجه حوزه سلامت از ۸۲۶ همت به ۱۲۰۰ همت افزایش یافته است اما تورم شدید در حوزه دارو، تجهیزات پزشکی و افزایش نرخ ارز عملاً این افزایش را بی‌اثر کرده است.
🔹
بیمارستان‌های دولتی با ضریب اشتغال پایین زیان‌ده هستند و توزیع امکانات و نیروی متخصص در کشور عادلانه نیست. تجهیزات پزشکی به دلیل استفاده نادرست زودتر از موعد از کار می‌افتند و هزینه‌های سنگینی به سیستم تحمیل می‌کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/676824" target="_blank">📅 23:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6b7a57df.mp4?token=k6hf11PxzXrEYLj_w1xf51cwuV1rH86iMz8P4Q6ZuHRLUJa7lUL8sW5gSeEYprwATSD7ParC3tii7yMf3RTgTZ8DPd3DvdvPHWXL1YTqZr6Lu7IN_Xf3SF-eA7HEilMNKl5RxgGA_Emvs_Np3Qa9yxrEADqcJblzcgY6kV_Qi0t3s1FnNpWuB3UFrFTZGbodtsZkxCOMMdAWlg_YNx6TwiLbYQvbE1hustrbWb_dqHxlRH1RIrkx_TDmowWE6uDZQWB_-WqoMLzSmBWzKtalYCde_G--6QbozL1hvQcLO5xYf_XC8mu_4Mog1UMGMdAt_5Ehg7U0XWt-zQFy_0Et4KApAVAxFsOGBgQ0wYUQuuWlX8EbBm283FbDDb9-aoP-vTWWAPB2ls91RCpXhFPkdQGOc38MUC_aAhywoy0jWBQhjwwcjhTuFDsA5AcTpx2JD24r9tgxUItWqGANGVwk-uW87ptZJzgwoWVItaPIOWVLF4HMFA0xIH6FXPS-7b_wWfecei8YI4qIyIlhVXWSE8tZWXkG4D125yW13omuL_6LEb_YQ-eHE4EB08L4DYl1FlS1x0PmJ0mQIhMj6e95c96D9GpW20nbjlNk9hmvO5f4gS3sLpML4CIE5iEQkXl-FqGRRSDSMeRdZyqvWDDli_R2Ii3gf0ZXEahyAanG-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6b7a57df.mp4?token=k6hf11PxzXrEYLj_w1xf51cwuV1rH86iMz8P4Q6ZuHRLUJa7lUL8sW5gSeEYprwATSD7ParC3tii7yMf3RTgTZ8DPd3DvdvPHWXL1YTqZr6Lu7IN_Xf3SF-eA7HEilMNKl5RxgGA_Emvs_Np3Qa9yxrEADqcJblzcgY6kV_Qi0t3s1FnNpWuB3UFrFTZGbodtsZkxCOMMdAWlg_YNx6TwiLbYQvbE1hustrbWb_dqHxlRH1RIrkx_TDmowWE6uDZQWB_-WqoMLzSmBWzKtalYCde_G--6QbozL1hvQcLO5xYf_XC8mu_4Mog1UMGMdAt_5Ehg7U0XWt-zQFy_0Et4KApAVAxFsOGBgQ0wYUQuuWlX8EbBm283FbDDb9-aoP-vTWWAPB2ls91RCpXhFPkdQGOc38MUC_aAhywoy0jWBQhjwwcjhTuFDsA5AcTpx2JD24r9tgxUItWqGANGVwk-uW87ptZJzgwoWVItaPIOWVLF4HMFA0xIH6FXPS-7b_wWfecei8YI4qIyIlhVXWSE8tZWXkG4D125yW13omuL_6LEb_YQ-eHE4EB08L4DYl1FlS1x0PmJ0mQIhMj6e95c96D9GpW20nbjlNk9hmvO5f4gS3sLpML4CIE5iEQkXl-FqGRRSDSMeRdZyqvWDDli_R2Ii3gf0ZXEahyAanG-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه در مراسم تشییع پیکر امام شهید در عراق دیدیم، فراتر از تصور بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/676823" target="_blank">📅 23:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
تعویق آغاز سال تحصیلی جدید؛ مدارس در مهرماه بازگشایی نمی‌شوند
👇
khabarfoori.com/fa/tiny/news-3234330
🔹
عادل فردوسی پور دست وزیر ارشاد را بوسید؟/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3234255
🔹
گزارش تایمز از تلاش‌های سیا و موساد برای یافتن محل اقامت رهبری
👇
khabarfoori.com/fa/tiny/news-3234329
🔹
کدام یک از موشک های ایرانی می توانند به خاک اوکراین برسند؟
👇
khabarfoori.com/fa/tiny/news-3234300
🔹
تصویری تلخ از تعرض دو سرباز زن اسرائیلی به یک مرد فلسطینی
👇
khabarfoori.com/fa/tiny/news-3234345
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/676822" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXR8kw3eAgxxXyrLc0n3Jp5LyKNAfjkAN9_EVboYwCdDFzvKvFYGzTu__Hdg9AQoqYufnrqSvYMdeQJKMW455RiBY1kWSVfXTIjWJaKSKldjR50BBEeZu9fFPQfolkuXvOH_YaIMqbwmHnDf9BVN-ITyFivONDU_dNot7ntcc032J-ysNJMja6qhA77yW8wmM8iaaP1_K5OJGxOKblayGC7PLS-Gehz0H7-oGfqurDfszB2r_pmIj5UWlvkmSTD1YtjPXrPjkpxw2VKhujahYoYDCKRI-ols36Q1djPXacE-uEFgcfjMdjtvHVDR_OSngM1cE86dxX8dgxbXNrVxEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار عراقچی نسبت به عملیات‌های پرچم دروغین اسرائیل
در منطقه
🔹
مصر دوست و شریک مهمی در منطقه است و امنیت آن برای ما از بالاترین درجۀ اهمیت برخوردار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/676821" target="_blank">📅 23:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676820">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crw4-vQ116H3R2s5qRJBj611Cx8wyMy6dS3-F9yg1x8zOg-mt3-YMrAGM-mHfQeZTYigFxywSIy68UM67qCIIgAZHJZf7doegNZNuHZDWzR7HpO_cYvnxx2GX-Xdr5IfkEKOrDnjFFOpvqwTbyEQT3PxA85DBCLQwpomI6VEy4s5_EoAzb_HP5zMm_JKQpOanb-EwT5igaoCgTrG_5gk4wKqMhfLj3og1oMqT6UAQd8nfx0xudtGzX-mK37_Yn67QY9GU4Px03c25l4C1hXN4jzX1e-Vx8go_hT7luAuVVISw4zULhPgrtyiaagRb5zz9jxgdriE6gHlNHOh334nZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: ائتلاف تحت رهبری عربستان حتی حاضر نیست کوچکترین اقدامی علیه اسرائیل انجام دهد؛ اما در عوض تلاش خواهد کرد مردم یمن را که از غزه حمایت کرده‌ اند، هدف قرار دهد؛ همه چیز اکنون برملا شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/676820" target="_blank">📅 23:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036392c48.mp4?token=iKBlmDmXlBy3BHdsFDlMCMOuT3A7_-wKL9ygJvMFa1hB7Yx9uVwyORlRNC78txYlZ6dHQvEOKvfsmOaB-hh3_WyNR1cZ_yl7RZaNSM_TTKIQPq6fPC2khPQgV03pdxU7gGQNOiuILmgOosRGuY06f8pZmJFgObWMhbieWCQLHZ0vqBWkXQ6O09GgwT2FiSfJpAyio0kvmTw00hVbsym4JBZIbxr0YfyhJp1Aw9N5DReCLg-r7O54VDhqfvIJ6_eLGFbZwRVRjBJg_odri1lnONbDtlQP8v21KIzLVp6gN3ZevpPzCDylhGP5-7qY0PHjCc0lvt3Uh18nCvCLM7miow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036392c48.mp4?token=iKBlmDmXlBy3BHdsFDlMCMOuT3A7_-wKL9ygJvMFa1hB7Yx9uVwyORlRNC78txYlZ6dHQvEOKvfsmOaB-hh3_WyNR1cZ_yl7RZaNSM_TTKIQPq6fPC2khPQgV03pdxU7gGQNOiuILmgOosRGuY06f8pZmJFgObWMhbieWCQLHZ0vqBWkXQ6O09GgwT2FiSfJpAyio0kvmTw00hVbsym4JBZIbxr0YfyhJp1Aw9N5DReCLg-r7O54VDhqfvIJ6_eLGFbZwRVRjBJg_odri1lnONbDtlQP8v21KIzLVp6gN3ZevpPzCDylhGP5-7qY0PHjCc0lvt3Uh18nCvCLM7miow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همانطور که ما برای ایرانی‌ها از خُلق و خوی عراقی‌ها حرف می‌زنیم، عراقی‌ها هم در رسانه‌های خود از ما حرف می‌زنند.
گمان نکنید عبور از تعصب "عرب بودن" و ابراز علاقه به فارس و ایرانی اتفاق معمول و ساده‌ای است. قرن‌ها دستگاه‌های تبلیغاتی عرب را علیه فارس و ایرانی شورانده و کینه و دشمنی تولید کرده‌اند. هدیه دادن آلوچه و آب‌نبات هم از پس این فاصله‌ی دراز تاریخی بر نمی‌آید. اما معجزه انقلاب اسلامی و شکوه حماسه ایران در دو جنگ تحمیلی یکسال اخیر باطل‌السحر همه‌ی این تبلیغات بوده‌. نه فقط برای شیعه‌ی عراقی که برای سنّی مستضعف آفریقایی، سنّی حنفی پاکستانی، سنّی مغرور عثمانی، سنّی اخوانی مصری و تونسی و...
ایرانی حالا محبوب‌ترین ملت در بین همه‌ی جهان اسلام است حتی در میان ملت‌های کشورهای خلیج فارس که ساکنان سرزمین جنگ میان و آمریکا بوده‌اند. و این بزرگترین دستاوردی است که آمریکا و اسرائیل در پی نابود کردن آن هستند و نابود کردن آن فقط از یک راه امکان دارد: "شکاف داخلی و آشوب اجتماعی و معرفی جمهوری اسلامی به عنوان حکومتی ناتوان در داخل و بدون پشتوانه مردمی."
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/676819" target="_blank">📅 23:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676814">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvaTL5-Z2X6aLAFKbXQ0sExdnHwxNfPVqQiiJUtQ9fLepHPIdv-bbSZmJ4SoGfcH3VBt1mbDqUqlvKB-ePZVScHmiVseKYVn3RvcVkSbp0GqTfVkZ1BvS2IPC_f3nOUCsfSb14tuUKEmfS46Vhobs5dwMH7gqvBCBHRGJi5rP8ThcnKXYfXpYj_YXChn4AHC5zhUC1L7ga6t4t3pg5WBBgmeaqUGWnLQwb3p9-Ax0tFLZheBkJkv7CVyxycZlOE5HY1Pp3bJeQim2dl3bhLFq8xvUyh-qRkyyhejrdoDgrYcoA6ECUAdeh_AKdM7MViHyeXLW-xvuqQSiMpAoftDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQDuwB6CzNcu0UUwerH1us2MFYqbuwZWkzmWpBed27_TACiWiHesjmkRg6DiIp1z_T_TZcaaCSDyRXZZ7sdVONT23WhyXRwVwVSpGN2rlRQSqQXOVWnpCl9thqYyAWAoU5GZ_Eh6KA3UmY-r8LpbR0JO3CC4hVS2OHoQ8SJC9Tas44gVBV7g4Gh_pV5IE4iM7ngMay4dJrFFtV-vTsBQWDZ8UnDaVLl1He0MbCiOfLsbSx6781pGAXPAj5UlsrrdMqCc4R7MhXMEBxC11e31QyJIsfcGThvUphI3K85wI9RK5D3FZvUugPlAXaw40RiZhz7I6cAxJk9Vu4JEmK7EwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nabIUMQkXSdV6_d-6xsxvTmaYNp98a7XXOUR9Wr7xyV4nr9VclM4Ey_mJ71T-qTLu4B0ZV3qlnzmQbyIl4Uqv2_SDA3UAbKn0JHOShgYBtBxxBmf_hLpMKrJPveNoQZE0jE3UfumPZVd8RQChoD1DemgJpRCWJNwtBmAskVBLxC64uoiqalbMu2oRyRtXrmblLd8XT59M8U32CXWUhZnjUJ046ILfJLjRQSWdyMTKfzPzfHjWWh85K7Ku7JL3Fq5QokMgm9bF2JkSZ4CojjhqLdFD1A2CXsFgMoK_pagVR6ScP2nBKVo2E8w4F2yre7Xv0qyxA47nhhoR_WQ4bTkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0ZiQASbXD9THEYxbQB-5iUTzgsrNGVyPbtExCRkcm79kXouv4CikPk9gnD88NTmDiYQR82zQ0ddMN9q_-xE8fhmi5RZD3n-e92Dnv4MdXNZSmg35ZxWYVupW2bg08_10N8gcBQzPfFE4QgjiEiE9kp8eFcnnlC0prWrdVJCRMi1X2bsDwoXLtW9zlFDpvPzOKGflHSMA0aywLbvFKO_1O_ufiKGcXNXF5jgyN4cYlc-VWf2T2PM0PoJJ0l4_lNCAKA36R76eEzxaFipZZuqHLXdEDZ5hzJtuUnME0VmjPMV24JA1-NRCMNMnNR3pfqZG79QNJO5k6b_n5wrYjKb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRGleSQzzzpw0GUghSNy0aBGDEkA3c0wem51VOWCAd4nzsmE4JEXLfuWuhcvMyp46pKW_0mnFk-6IB_MTjOZMY71V9am5577N8sCQXrrWvTK91bBQ1R3gqDlvqjIJdw5Z3t6177U1lIAaHSgMWhcWuiocbi1IQV3H23NTOguMVvh3srQbJDOFuge2wuYw03HZAEHQ1xO_cpp756gAQEwN9nl1TyXWYb3tA-MjcLTKRMSX7ZIT4_qQ_hrTOVY25SO6S2Nie9sfzeqjRfDkRfbmexkzMlTuWrA9pShhQ-RzkvsxRD1qCJlsKRuXoejripWJvB0sB9vu4j1vXqwMPmSzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۲۰۰ متر از خط ریلی گرگان-تهران زیر گل‌ولای رفت
🔹
به‌دلیل بارش‌های رگباری در بندرترکمن و بندرگز ۲۰۰ متر از مسیر ریلی دچار گل‌ولای و رسوب شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/676814" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676809">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNVv-6pHKVvR7jYft3DJY7HS76KVeudizRXxK16VWeQITl4qc631wDus50Nm3aGQtXPcNpwzAOjsEjOaYX13cSmL7yGkLNmJTMN_4xv63c4dIgSIaPcn0yiayLLhGPZmoOR9oz4J53Yusib0fz5mKePzk8z6zKHyJ61f_OLusRZAMNeOVZxB3HRJ3EwozBH3CwPSHY3V7l3Evlpjs5GPE7R_XYwKqWlG5xld00qgW2huzA_qeMryNU71GPpCFC2Dg2tkrQcQNw-W5vbV7JbBV3JlOnPgFOZHUpTc8uOG5I3rMtqoQbrk_S90K-8bvNOji8slIWyzu4uE9MJ3T6JDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf5pA-qLTWOXC6_hjrOw3616U_c6b1KHR6njnxwpIeB3TOsETwWhy50IPPSAEAn_smAPnMJN94cDmF4W884YwbzXXvUBsmukQ7yV9xqvjAKON22yppJOdcRlxRUdQ3Cv3kDIuw8GIC9qKsFNZ72RmrvOzt_28uTL4bfQLMvOgzv6pbiBofcr8FGDr1l0wFmHbEUh5ceNqLQil9-cvDOWaTuppo578YBDuTJEiWZWZITxKBuxx01TZDHNrglQJZp8uaBmf0u_gXxNXkaR7PuVVS0wop7q0NDscVKf3z4GC6wCBzB25DtvsnKkWhR4lOtotus2iIMKsuCxjEsG0zyswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-e5Ad7TdLzUjQCylCjElxs1yZZ-NmBLcesfrMGpNWhptEjWsW9Oy4zKLm0S7ympkDmDjjJHj5lBPmAIRD0qUrbYrmxJ0_zg0WOu0St88xHBjreQWx9DqMD77h0BJMqJ8i4bWTiucg1110HwQzB1qddXAjNygbRtpuqZgYdqzR3IG3w28oBBl1E6cj0xGmFdKyIeb5GgsRNhVjsff6o_XalgHLba3F-chbBX4YTG5AUXhGFoyu83caeQJnplBAVJQrpiCIJfIUhLSw0KbNEboq29asooiz8F8rGNKhpLIW9DsViletWqm6pCvAHtb3n8Z_MSgeAQGwoqTU5pzWIubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RuhKskg98ls2zV7zFviBjolF_orA4gobCYzcKbQ9WlxKzWPVNp6XNNOJFr7Bwruzr8UQK4RRHkdK8RqLyAs06g3HE3OfE3xpzMsq1kNDwsiQNpbMh87gR3v0qJeszMq8WiYUNUIM7YibKWqfbDHjOaUOelAeB3iienZ1H63uVhhnjfpMLz2m0MWOwWevPDkQ6n3IdfDSmckIjhzIG2M3u7QmQJFBYyeqWKqZXSoOY4HFfkBCnSurZIyaEzCtpF8zL8zmigctYdTIOYCGM4NwAXSfPm-vQGPiySGJwgVdG9IN6bs9CWvEuKM0TC7oQxvDr6iJHsLoOG6Rrqe0wLauKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
در مسیر اربعین، هر دستی که برای خدمت بلند می‌شود، روایتگر یک عشق بزرگ است
▫️
اعضای کاروان رسانه‌ای خبرفوری در موکب «قرار محفل اهالی رسانه» همراه زائران حسینی شدند؛ جایی که خدمت، زبان مشترک دل‌هاست.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/676809" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676808">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
شکاف دلار به ۲۱ درصد رسید
🔹
فاصله نرخ دلار آزاد و مرکز مبادله بار دیگر به حدود ۲۱ درصد رسید. شکافی که می‌تواند انگیزه فعالیت‌های رانتی و ورود سرمایه به بازار ارز و طلا را افزایش دهد و به زیان بورس تمام شود.
🔹
با این حال، افزایش تدریجی نرخ ارز در مرکز مبادله همزمان با رشد دلار آزاد، از تغییر رویکرد سیاست‌گذار حکایت دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/676808" target="_blank">📅 23:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676806">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7Odqj58AgJcs9dx2fCdmvEDyE0HDUDsP8oDi0tvnRBCi_UNJpnvg5OEQK9t750bQA4M4Lobnbe2ZYckcd--gPSLkgIVAxhgVV-_c16RjXx4tYwRMZZAnh9gbyQA4X1_iVRechY9LJ9wBQVs2I7xNdta06rWS9JYGpvDAokyuO8pzS4pvavMcmLR_uJP4aAa7ssT0rJsXeALRrm8DkoFpJuQ6bhYTu6q0zyMk6ioCZ8-DtpJHLiYdzQvwSXjA0vMzF5FOhYhXzvqvterENvsZqdfjNBONgt8mjA4nYiz-rRJHWHSJ8gq7bm1ns3xy2Ejbo2MwYgzOTfiyttd3aI6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولویت تدبیر پیران بر دلاوری جوانان
🔹
امام علی (ع) معتقد است تدبیر پیران به دلیل تجربه و بینش عمیق، بر چابکی و شجاعت جوانان برتری دارد. اگرچه نیروی جوانی در میدان نبرد ضروری است، اما بدون نقشه و استراتژیِ پخته، به نتیجه نمی‌رسد. بنابراین، جوانان باید برای…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/676806" target="_blank">📅 23:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676804">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb6cb7ee6.mp4?token=CA-pALVCQM8xODc6i78wlltyw7RnwOkxM5qboYIedNius5nzOQG1ZBSi3SFGtEZPedmpZMVlI7Wx066XeMX9lO5TMLRz6o5Ii09A3LbkPN1-053ogoe9zJvOF9YBB7SrL7H2tCT20588rpLLF1wZyhPY2bYClsNNHa37ocwZ9lbEBEXmUBsODyMoQ649TNnvOo_dGxgubCoknmim-tmL6sNcfB-iS1i4g1kM4FLoPe9ifXuxzISE61d9oO0MQBc7DFQ39dBZVkN42UfP5vtEokc8eyJOq88ui89j07Q77_ATrT8bv6ZhMYvjN1WHxlSNw379pqaSSnwqTlJOKj52qmQ7GxGmg0EzsMZf75dwXBWTqErILhlhIMTRFLBLnu21VDyNRA8reKtTTwK_hBvBdYmKzpYZJxXKeabZBYUwzKFf0GW46SaRjeclw2CY-3L1OwAZpPK6PC0N3eKM1pgS3hPIH_uRI7xOgEodN8n01hRRKUcl8PyZO7R1CdrJEshvQRlNFPZln9lxciKW4ARehCiaDPOk1tFjWxgCrvfrR0avduWVJ-dRjMT3KC5ED5Up6dJHUHYsNrlRNjv1JPuhO6EyALJZd_qb75hYjK0PvTOdCxACJDzXE5MQ4f6HMREMGck7ninafz-fFMz19VX6pqYQ1EAlN_1yIdzS-niK7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb6cb7ee6.mp4?token=CA-pALVCQM8xODc6i78wlltyw7RnwOkxM5qboYIedNius5nzOQG1ZBSi3SFGtEZPedmpZMVlI7Wx066XeMX9lO5TMLRz6o5Ii09A3LbkPN1-053ogoe9zJvOF9YBB7SrL7H2tCT20588rpLLF1wZyhPY2bYClsNNHa37ocwZ9lbEBEXmUBsODyMoQ649TNnvOo_dGxgubCoknmim-tmL6sNcfB-iS1i4g1kM4FLoPe9ifXuxzISE61d9oO0MQBc7DFQ39dBZVkN42UfP5vtEokc8eyJOq88ui89j07Q77_ATrT8bv6ZhMYvjN1WHxlSNw379pqaSSnwqTlJOKj52qmQ7GxGmg0EzsMZf75dwXBWTqErILhlhIMTRFLBLnu21VDyNRA8reKtTTwK_hBvBdYmKzpYZJxXKeabZBYUwzKFf0GW46SaRjeclw2CY-3L1OwAZpPK6PC0N3eKM1pgS3hPIH_uRI7xOgEodN8n01hRRKUcl8PyZO7R1CdrJEshvQRlNFPZln9lxciKW4ARehCiaDPOk1tFjWxgCrvfrR0avduWVJ-dRjMT3KC5ED5Up6dJHUHYsNrlRNjv1JPuhO6EyALJZd_qb75hYjK0PvTOdCxACJDzXE5MQ4f6HMREMGck7ninafz-fFMz19VX6pqYQ1EAlN_1yIdzS-niK7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خانواده‌های شهدای میناب اربعینی شدند
🔹
استقبال از خانواده شهدای میناب در قرارگاه حمل‌ونقل جاده‌ای زائران اربعین حسینی در مرز شلمچه با حضور نماینده ولی فقیه در استان خوزستان و مسئولان سازمان راهداری و حمل‌ونقل جاده‌ای
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/676804" target="_blank">📅 22:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676803">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e1bad2a1.mp4?token=C_SG9RUvaY_TuMEP04KOpFXELs5FHzk46taklkpSmFSjVE-udPgr7PLANywvjA6Fg7I1KjBIWx5TH5Hp7wVgWhSD7VH6ULThZZh1x0CcO7NA4BL6o3YOI3D41_nk5hI38Sl3Q_eEyK_J9TIOdWiiaUbU6PuUnwYWVkYoHLdGagv3THvVhofWgQ9OjeV8XMzM13wcyzkhPwi-Vy4YQ1G1kWWbSJT4nQ147P8R9xmLUAcX8qkZlYJ-Wqh5efktsjPc6xKWEYaUKtiJI0Xp58jCUUEUIDorbvoatJMS9fJdzcGk0TFmtnpw0Gw6xB-CHlTfsi8FrqGvMvL6f4aY5FxSaLX1XM4V_cMK8IMbZER9xql_pVNVt8UkXRFfXKXatDo5Aw959G15-_8vkTQHsaMfv5u0CCLsRM5Hq8rYp2Qfmk2MJcguMiZW2zt2txAgHhH1CAbbbH2oj5dteLqSEC_NI7oLTtpIvvp0XIpU8PaoYNTWW2fY-zDmaoiO7jzehI-IgBrwDpWuI7B8anB0KZT_Y61_-HiSpHjWfUZ5iL-GFNBplGxnFFKRvimPYTY-XqA0WOwgih3vpB3sCBPii4bb5ArL1VxQCbGOtqJWgdYhOhIUTGu9RMKFztHmsTeEOBGDdIpURqUwPn1GE1QxeIWGt2nBHcduk1va6N8unnQDt7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e1bad2a1.mp4?token=C_SG9RUvaY_TuMEP04KOpFXELs5FHzk46taklkpSmFSjVE-udPgr7PLANywvjA6Fg7I1KjBIWx5TH5Hp7wVgWhSD7VH6ULThZZh1x0CcO7NA4BL6o3YOI3D41_nk5hI38Sl3Q_eEyK_J9TIOdWiiaUbU6PuUnwYWVkYoHLdGagv3THvVhofWgQ9OjeV8XMzM13wcyzkhPwi-Vy4YQ1G1kWWbSJT4nQ147P8R9xmLUAcX8qkZlYJ-Wqh5efktsjPc6xKWEYaUKtiJI0Xp58jCUUEUIDorbvoatJMS9fJdzcGk0TFmtnpw0Gw6xB-CHlTfsi8FrqGvMvL6f4aY5FxSaLX1XM4V_cMK8IMbZER9xql_pVNVt8UkXRFfXKXatDo5Aw959G15-_8vkTQHsaMfv5u0CCLsRM5Hq8rYp2Qfmk2MJcguMiZW2zt2txAgHhH1CAbbbH2oj5dteLqSEC_NI7oLTtpIvvp0XIpU8PaoYNTWW2fY-zDmaoiO7jzehI-IgBrwDpWuI7B8anB0KZT_Y61_-HiSpHjWfUZ5iL-GFNBplGxnFFKRvimPYTY-XqA0WOwgih3vpB3sCBPii4bb5ArL1VxQCbGOtqJWgdYhOhIUTGu9RMKFztHmsTeEOBGDdIpURqUwPn1GE1QxeIWGt2nBHcduk1va6N8unnQDt7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف پیرس مورگان و افسر پیشین سازمان سیا: آمریکایی‌ها در ایران همه‌چیز را امتحان کرده‌اند و هیچ‌کدام جواب نداده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/676803" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676802">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
حمله پهپادی به بندر دمیاط مصر چرا مهم بود؟
ادعای ریانه New Arab:
🔹
بندر دمیاط مصر و ترمینال صادرات LNG آن هدف حمله پهپادی قرار گرفت؛ تأسیساتی که یکی از مهم‌ترین مراکز صادرات گاز مایع در شرق مدیترانه به شمار می‌رود. این بندر نقشی کلیدی در تأمین گاز مصر و انتقال بخشی از گاز اسرائیل به بازارهای جهانی، به‌ویژه اروپا، دارد.
🔹
دمیاط در اوج بحران انرژی سال ۲۰۲۲ با ثبت صادرات حدود ۴ میلیون تن LNG، به یکی از شریان‌های اصلی تأمین انرژی اروپا تبدیل شده بود و هرگونه اختلال در فعالیت آن می‌تواند پیامدهایی فراتر از مرزهای مصر داشته باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/676802" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676800">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حاجی‌دلیگانی: فارغ‌التحصیلان در اسنپ کار می‌کنند
حسین‌علی حاجی دلیگانی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بزرگ‌ترین مانع ایجاد اشتغال پایدار عدم تعادل میان نیاز بازار کار و خروجی دانشگاه‌ها و مراکز آموزشی است.
🔹
بسیاری از فارغ‌التحصیلان با وجود تحصیلات عالی در مشاغل غیرمرتبط مانند تاکسی و اسنپ فعالیت می‌کنند، در حالی که واحدهای تولیدی با کمبود نیروی کار ماهر مواجه‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/676800" target="_blank">📅 22:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676796">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
گزارش کانال ۱۳ اسرائیل از تنش شدید ترامپ با مسئولان امنیتی کاخ سفید درباره جنگ علیه ایران
کانال ۱۳ عبری به نقل از مقام‌های آمریکایی:
🔹
دونالد ترامپ در جلسه‌ای برای دریافت گزارش وضعیت جنگ علیه ایران، با مسئولان امنیتی آمریکا به‌شدت برخورد کرد و از نبود راهبرد واحد ابراز عصبانیت کرد.
🔹
به ادعای مقام‌های آمریکایی، ترامپ در این نشست برخی مسئولان امنیتی را مورد حمله لفظی قرار داد، بر سرشان فریاد زد و به آنها ناسزا گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/676796" target="_blank">📅 22:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676795">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
دادستانی تهران علیه افراد حامی محکومان بی‌رحم و سنگدل کودتای دی‌ ۱۴۰۴ و جنگ رمضان اعلام جرم کرد
🔹
پس از اجرای احکام قانونی تعدادی از عناصر کودتاگر دی ۱۴۰۴ و عوامل دشمن در جنگ رمضان عده‌ای قلیل از چهره‌ها و افراد با اتخاذ مواضع دور از انتظار به طرفداری مستقیم و غیرمستقیم از چهره‌های اغتشاشگر سنگدل و بی‌رحم آن وقایع پرداختند.
🔹
این حمایت و طرفداری سوال‌برانگیز در برابر حکم قانونی دادگاه که همه مراحل دادرسی را طی کرده و در چندین مرجع قضایی و زیر نظر قضات باتجربه رسیدگی شده بود واکنش افکار عمومی را هم به همراه داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/676795" target="_blank">📅 22:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676794">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d052f2261.mp4?token=MUQtRa21B-XYfEf6DeHJIequRCL25UZvmHLums2YjHgCHs8Q3pJRIMxB_XWadsy34GawtLmg9yGs8zapMvzPxM2DFvV29pZA0Ut9Hyk0g99YfZkq0EJDnhyrtgSLFUGskHYM-T45hXXaouAFT-aTIS_NM5GlHoIJH0fR6WJ4b2KQ_H2XprJzkfMXF7B3CbrnoHoo18ho7fssaWHY1Nwweqk5T6aS2styR9eIVvPJbSQX2n9DnCoMlreHQ_aRVFfjn72TTIr7Q-XjmCyBrowUPaAdmfx2euL1yjNhVj0I14hmpuaMqxRdAxFViN_Y2jjwlLangO8s6qWIyymTYlMkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d052f2261.mp4?token=MUQtRa21B-XYfEf6DeHJIequRCL25UZvmHLums2YjHgCHs8Q3pJRIMxB_XWadsy34GawtLmg9yGs8zapMvzPxM2DFvV29pZA0Ut9Hyk0g99YfZkq0EJDnhyrtgSLFUGskHYM-T45hXXaouAFT-aTIS_NM5GlHoIJH0fR6WJ4b2KQ_H2XprJzkfMXF7B3CbrnoHoo18ho7fssaWHY1Nwweqk5T6aS2styR9eIVvPJbSQX2n9DnCoMlreHQ_aRVFfjn72TTIr7Q-XjmCyBrowUPaAdmfx2euL1yjNhVj0I14hmpuaMqxRdAxFViN_Y2jjwlLangO8s6qWIyymTYlMkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد متفاوت نسرین مقانلو با هوادارش در حاشیه مراسم اکبر عبدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/676794" target="_blank">📅 22:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOo4_lRwiaCqeEQDPdyyNsSDSPRS4KFwfa3v-n5nzpK8A2Csx2J9cnPzkT6l_3C3dOcYFT-p05XrFh5wOsS34UUDvr2MqCaa4b07zQ8gxJRmKbzJHNCJFzl1xGVavpMWj0XT6aS2OKbSHR_801LVJN-qxFzf-4ZYM-DP-m-uY_Xe-ER66BuIcoUli6d5UsiL6dDkj6NP5KOK5T8goj1Sy7IyZc3Mz8aeq4YOFHC8sUn8J0-cyjK9t7iFuPlVYu8NgbnfIofj5anruPJG9Ro5_ZVpLKsEtS4N_95KFmfsVmbsEGgddleixGqXZvpXbaaTRsuhmq2gG4EAujfolFQT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJjGyRuw_yZZx05HJHLfKfRcb5KxLgHBESL62arPEgMgGB_2s8dub-UvrRNNga3Xrz9d__RXgHOPwOSjcEGlgQRBe7Ko2u9oSTiQ6PX5W9HjZ5-sN5s8zEEgbAgRs4rNirSPFohu7y3RqGrIVwmQSIYpyFE18yDkWCUcnP3NSGFSworbfR9vUlhMS7exBZQ_C02J9ic2MjQLJfzy9ekQh96X-6NtvMqSo0QZehCuUU-fQyKXeykwuLFXIuXM7P3SXaZo0A1ugFM2CD30p7_lMCwh5duT0ydsTaFZewz-ubXqr54WAiPLfASc0xZAfuS3b9nAy8ep6H6aPeWv-Cvqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDMwKZtTRuKzEBLO-gqz5Y5OKZe2SlUoAlXclVrrKLYU7Bs-6pXj9OYPZuQqN0E5D9a1dKGBUNUH1Vimv9l5mADkUWZuzleGK_8qs19qhZA9wC7OUrdW1KQjQ9SLf5Q5BGLUsd9ELhiDIgFIy8-kl9F1EmFx8CZljAw9xSSO06ryxgFMpXpPqqlxZ1KDQ2yAWDdIhEqaTmYmh8dHXCYrVREKWpSoVOcA5q2uFd0Y_PLQiF6R8OK770rlA95SxOO1rB37GTw6NwgE7A3a-t7o-v7IZei9zMIgQt9ozsMGKPeg2P8KhA3DIjTunABuh3T36K0HQzr5rQFwmZ9z2lwHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVJfU1_bx8bLQDnROcGCqFI-kk_ECpwEVV0_P3R-znKa4ymB52tX0oeNj58SfQaUkPu--WL8aXc74Va4rBj5cDMhWGA5cGiH5FbYLjqv5PCkzeRb2pj3Ns8GIIJaWjuLGzJVAdXMRErk6_x3YEQoZDZyVIXEEaozdklLM5JrZ6GfBdi4KoCgSYLgqkNX5JJXjrr_cMDwxQ3QuiwsamhGQtDwknTefnmA21HFRmReklw13HG1qqb_V-BQb9pxYEirmWIoKTWS5z7cc6qC1Xohrg0SKAkeWGG7iTnDysdgtZ93RNjkdnW7Nl0O9EWVkOfUXuo_vHdHmCcRiVBeHyFpQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نه به دورریز غذا
🔹
به‌اندازه نیاز خرید کنیم و از دور ریختن نان و غذا جلوگیری کنیم. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/676789" target="_blank">📅 22:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676787">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEY4Jk92FL2OOJfmUt4-WGShjjiyT2T3w7O77iFOsFR9P8veZ1B3eCk6nvsRdhHQRQfq5tNdFFX80jdj4yHmqNCiynyzyfg09ZjQz9Gaf3fQCVWk_lt8X-f1upolirtK88xr93Ey86RMpLuHQ7b1pE67pv7U__0eNpVby5y0fbSGAGCKkjDVmfU7D5cCdGAaC68XYA2KXzM2ctwd8gvU1D96BXJztM0yT7DeFAcvKr0I1_4ePbxvS_y0BZ1zYOMIRnjh42swHuHVEqW0eAXPAD-8vvWoKUyktEr53LIeBg3o_kmoiwl86sXKkr5SQG-tEZWqm3vvoul0vN4LtsjFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: آدم برفی
🔹
ژانر: کمدی، درام
🔹
خلاصه فیلم: عباس خاکپور (اکبر عبدی) بعد از چند حرکت شکست خورده برای گرفتن ویزای امریکا، به پیشنهاد یک دلال ایرانی تغییر چهره داده و به ظاهر یک زن در می آید. با این ترفند او می تواند ویزای مهاجرت به آمریکا را بگیرد…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/676787" target="_blank">📅 22:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676786">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTtR03R9SY82P0z8oKnMnIgT7BDXtWYuD-ryEhcJwdiNINTp6HiK_4Fw8vStx0yLVrBJI1Psj4NpwR_AR2jcSwGj7nu8V2RP5YvcgXVmxxK6klFIprPiWpzivaXqtn8awPiiMkySUzzR6arv_27zpYIc-uBjIyv3Y_Tc6fmUDxQPR4ntQFCRV0AeR46rZWyfHm4FbKvc2A1PUBNq0pkfzXJxw1UeJ0FPPxH1a4l36xHXG7wWvb5eH2Y4Td8YhuvrZAaxNWrdWk0sDVYVTJDboccJWpyqWYZo6W2z5tY4x1NEJiThoDaSeXxsQ_dLEXfPxMgJ93cbQ2h2lX3p71pvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه پیدا شدن پیکر بی جان کودک دو ساله در حمله امروز آمریکا به قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/676786" target="_blank">📅 21:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676781">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDr8rqW8SU7GBq4FHCQRPBVHkbFMwggyR77ho3B2yrYe8Q1mlTl8d8scsT6cjC6G0P5qSvARcfTwKzroCtuAyNQwayl2Tyqb__MiULSb_Gzh-QBFgUZ7mcZ2MLCtAaJ-aYUXwqZ8sZF1RJtyKPpeLIvVdbgFRFxkzfNIdKEZ0fYdnz0aRm9SnVGqlFx18s1hMhejsgNYv2GdRypVn3mHGUdoSdBQQSUBxqtnGfk9uEPzr9Fm9wYWN7roJ_vYXNVlYqfh-LQfUplZk8v5i3OImNRGWtNtviPrR6h_suveG6I5xf8a1VIOQ-Dpa3k8bq3CP_mc1XvAIQ5AvqO3XADLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس بارگاه امام حسین (ع)
یادمانی از کربلا؛
برای خانه‌ای که با نام حسین(ع) معنا می‌گیرد.
💰
قیمت ویژه: ۴٬۴۳۹٬۰۰۰ تومان
۴٬۹۹۹٬۰۰۰ تومان
⏳
موجودی محدود
🛍
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/676781" target="_blank">📅 21:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676780">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: با حذف دو دهک بالا، سهم کالابرگ هر نفر فقط ۲۵۰ هزار تومان بیشتر می‌شود
صمصامی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
نحوه محاسبه کالابرگ یک‌میلیون‌تومانی دی‌ماه مشخص نیست و گزارشی درباره آن ارائه نشده است. با حذف ارز ۲۸۵۰۰ تومانی، اگرچه یک میلیون تومان به مردم پرداخت شد، اما حدود ۵ میلیون تومان به هزینه‌های آنان افزوده شد.
🔹
به‌صورت کلی، ۹۹۶ هزار میلیارد تومان برای کالابرگ در نظر گرفته شده بود؛ سیاست کالابرگ به ضرر مردم تمام شد و حذف دو دهک پردرآمد نیز تنها حدود ۲۵۰ هزار تومان به سهم هر نفر اضافه می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/676780" target="_blank">📅 21:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676779">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXYMlV0KyuqyTe3MNk4k8-btnSwoFfvW_KMUAFnIV1GnCLpqZGzWT5WF2ct0xU2MJa9Eeex8sxI4R9qIOmo6j5XdD60dXJMH55vIpHWyDhweUBGtmyuUPuRGRuhEmbRI05FU_aQAL-HwgHPm5EgMeMd8pmZVQbusNtiN4Wxw6lb11in2OySrDSRGc5q9QDOPXWEgNfNhDkNfaOpKlGvrzsKNPV7sOMWQnoBM9rzV6knJYGxa1w_kIUYzJ-J5sjCNbJYSi0UNdXAd7Si0lZEi2pa_TCWl5J6S4pZ1AsVTY7r07ITQ2EWKiht_r4EwRfR_CFGTjgTjoaV-s0j7rAdGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باید روی تابوت و تجهیزات جدید امریکایی بایستیم
سرلشگر علی عبداللهی فرمانده قرارگاه مرکزی خاتم الانبیاء(ص):
🔹
آمریکایی ها و مزدورانشان امروز تا اعماق وجودشان متوجه شده اند که تابوت آنها بخشی از تجهیزات آنها در منطقه شده است.
🔹
آن رهبر شهید گفته بود که زمان «بزن و فرار» تمام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/676779" target="_blank">📅 21:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
گلدمن ساکس: تداوم محدودیت در تنگه هرمز می‌تواند نفت را به ۱۲۰ دلار برساند
🔹
بانک سرمایه‌گذاری گلدمن ساکس هشدار داد در صورت ادامه محدودیت عبور نفتکش‌ها از تنگه هرمز، قیمت جهانی نفت در سه‌ ماهه چهارم سال می‌تواند از ۱۲۰ دلار عبور کند. با این حال، سناریوی پایه این بانک همچنان نفت ۸۰ دلاری است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/676777" target="_blank">📅 21:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROkZFp-ob9G1TkFYwGaWivjVj5eqUuWjsVABZyDYQ526fhyONhj7bhrcD9mXs8ytFdiMSNhn9hYtIQAupZ1BwhxmJZLWQGcZ8G3LKZrS67nn6PbcDBc0MXzYbruYTIfDVDZ8AKF6a_OPc4X3PwiIhGMTvrI6_UYsGxVtX8eaT_1FDaAhtEwuWyihCEz94qkXoSQEAmBDdnHTKepQhfW5TZ2oaSnN0n0MoH4imfor8i0y981p5UmRCWeR-9NPDMWlwbJic-LVsW5T-MhY6vTzlIoSLMFAoUz09vGY2MTYTAwRoW0-_7wjaIbkcYUejYUlwRwZrUZuFcjNNphR-rV60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها گسترده‌ترین شبکه حمل بار هوایی را دارند؟
🔹
آمریکا با امکان ارسال و دریافت مستقیم بار با ۱۶۷ کشور، گسترده‌ترین شبکه حمل بار هوایی جهان را در اختیار دارد. پس از آن بریتانیا، چین، امارات و هند قرار دارند.
🔹
ایران با دسترسی مستقیم به ۷۹ کشور در رتبه یازدهم این جدول قرار گرفته است.
🔹
هرچه شبکه حمل بار هوایی یک کشور گسترده‌تر باشد، تجارت خارجی، زنجیره تأمین و جابه‌جایی کالا با سرعت و هزینه کمتری انجام می‌شود..
📊
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/676776" target="_blank">📅 21:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgAHC7qkQKtRUb0VnfrR3zKQA0oDcZ0ote3TF-oPL7FUQ3wh1Qe8HJzNFPMbxti-w6RkoRmY2vmFDcyirtYYyp5RZXhDKb1P1ggBI3f4AgpBJKjEQuT9vohwPOZyzIAvS_xk5A_xUaHHNZ7iRTfzqimZStBqW3z-vDDQiZalebKcsn1VCMUmjRId9-xz45mfgNFDf8jYBQmhtZVJSMGf8HdVvhIWZGDuWx3KyhfTgs4BRn0v0WbmeShHMRhaKEMULZ6_qPY4_Zwse5JSS4kjseg3DRMxHwbzQsKhDoXpTV5vEmTQQdOKv0VXqjY3jtVY2kllSsqvtkmoZsSI0TITEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آ
مریکایی‌ها از ترس ویدیوی افشای اطلاعات ملانیا ترامپ دست به دعا شدند
انجمن شفاعت‌کنندگان امریکا IFA ضمن دعوت از مردم برای شرکت در دعای دسته‌جمعی:
🔹
پروردگارا، لطفاً به ویژه از ملانیا و بارون ترامپ، و همچنین از تمام خانواده ترامپ و تمامی مقامات دولتی محافظت بفرما.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/676775" target="_blank">📅 21:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676773">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
میزان مستمری‌های ناکفاف برای خانوارهای بهزیستی
یاسر اسلام‌دوست کاربند، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
مستمری خانوارهای تحت پوشش بهزیستی در سال ۱۴۰۵ نسبت به سال ۱۴۰۴، ۵۰ درصد افزایش یافته است و مبلغ مستمری ماهانه برای خانوار یک‌نفره ۲.۱ میلیون، دو نفره ۲.۹۸۵ میلیون، سه نفره ۴.۲ میلیون، چهار نفره ۵.۳۷ میلیون و پنج نفره و بیشتر، ۶.۵۷ میلیون تومان تعیین شده است.
🔹
حق پرستاری برای افراد دارای معلولیت شدید و خیلی‌ شدید ۸۰ درصد و برای افراد دارای آسیب نخاعی و اختلال طیف اوتیسم حدود ۹۰ درصد افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/676773" target="_blank">📅 21:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676772">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBESDQrU5rnmHTi9Df92Awsgm9lf0iIwpU9UyRCPQWa80PR8YKh9HQ3V4CFUl51OzD4wBwxvqHnWCetpWJOdSzlU1mRo9__nnkrNc64MVlGn5OpdFqK2zsMD_eRoS79bXW5ZRDJpkNcO1rMCm-ZIdOIH7EO24LiTCG_QBhPJG6UfJFYoYfwIfxOqqQ6wa1Gv5sfbUTXQJSs1tNfo2iW4rqqSJejY_w4DbGhdM0wJufVy_qQZSzrLeNDs4h6-UxKhc43nF_4LhRyxIMUyxLgqQM89l2yXGofsW0K9jb9cmil4PSz6bvkaIM5b9t0sUOtbdAkiWsvNCyQDzq0HvGzeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر اولیه از سولۀ تعمیر و نگهداری جنگنده‌های آمریکایی در پایگاه موفق سلطی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/676772" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676771">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=pk3nj98xnCKXOfDhaTyxN8pb4RS4d_pM0BxR7McsJ7ZoEHhsC1p5qtUzwhjg0UDPLLqAaYQitkOB81eNLRDCSNiFF1hUHrBcWaKD8vKyiiqQ2zOcec7grDTzlFdBOoqdFBlox_3YLaICfh5xZ-goJzgEpodUvIIBYfueJFLLH4Xz1Ba_CgTwxbK5bsOFGFEaZ3Uvxu3X_D0bVojfCjYfmannj3fAwRi1npo-VD4KHp2ak7t9dMFV4grOSRCYrLju5KAgc4v17Gu8BTSbGlu29dF5fLkNMS1Vw_yNGGtBIUqZ3Rlz6SpnuJwXPjHhwqaHkj00jbHLwiyB-WSB6NsNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=pk3nj98xnCKXOfDhaTyxN8pb4RS4d_pM0BxR7McsJ7ZoEHhsC1p5qtUzwhjg0UDPLLqAaYQitkOB81eNLRDCSNiFF1hUHrBcWaKD8vKyiiqQ2zOcec7grDTzlFdBOoqdFBlox_3YLaICfh5xZ-goJzgEpodUvIIBYfueJFLLH4Xz1Ba_CgTwxbK5bsOFGFEaZ3Uvxu3X_D0bVojfCjYfmannj3fAwRi1npo-VD4KHp2ak7t9dMFV4grOSRCYrLju5KAgc4v17Gu8BTSbGlu29dF5fLkNMS1Vw_yNGGtBIUqZ3Rlz6SpnuJwXPjHhwqaHkj00jbHLwiyB-WSB6NsNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مرحله بیست و ششم عملیات صاعقه، ارتش جمهوری اسلامی ایران با تایید ضربه زدن به تاسیسات برق و ناوبری و ساختمان‌های اداری و وارد شدن خسارت به پایگاه، پایگاه‌های آمریکایی در پایگاه شیخ عیسی بحرین را با پهپادهای انتحاری مورد هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/676771" target="_blank">📅 21:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676769">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: آمریکا، ایران را پشت حمله سایبری به سیستم‌های آب مینه‌سوتا می‌بیند
ادعای نیویورک‌تایمز:
🔹
به گفته مقامات آمریکایی و ایالتی و سایر افراد آشنا با این موضوع، محققان معتقدند که حمله سایبری این هفته به ده‌ها سیستم آب شهری در مینه سوتا احتمالاً کار هکرهای ایرانی بوده است، اقدامی تهاجمی که در برهه‌ای حساس از جنگ آمریکا علیه ایران رخ می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/676769" target="_blank">📅 21:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676768">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25731386ee.mp4?token=LR-7SEFoH0TlfjZ0KAm9ir2g-CI0xdZ9iu0daltY9R4NWQ-wn1pWcFt0515LjQTXddd1zvLdQ4gMortQZZ_KQgAr9zJasEjvxZobhFSDlVdWmWN-syGSuuokOTgJdA9n_yo83yVtaAgfg_vXH-u2Dog5ppu9c7As1ieKpMLWIJ1LvjE7uUijlB6YMqebv-GgOpkMHVIq-nKEb6ghM3XMeaPnSiRqXtjXlfdCQ-f7HbvWLcqqrZSYF_9-_xUH2nZoqYR-xfulUPQ-pwKdQvWQOgpOD5VlhjxhmcFjdjR-xQiI-slF-sijS8vE5Ut_LofTg99W4hi2kBdmO0q1tVqPVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25731386ee.mp4?token=LR-7SEFoH0TlfjZ0KAm9ir2g-CI0xdZ9iu0daltY9R4NWQ-wn1pWcFt0515LjQTXddd1zvLdQ4gMortQZZ_KQgAr9zJasEjvxZobhFSDlVdWmWN-syGSuuokOTgJdA9n_yo83yVtaAgfg_vXH-u2Dog5ppu9c7As1ieKpMLWIJ1LvjE7uUijlB6YMqebv-GgOpkMHVIq-nKEb6ghM3XMeaPnSiRqXtjXlfdCQ-f7HbvWLcqqrZSYF_9-_xUH2nZoqYR-xfulUPQ-pwKdQvWQOgpOD5VlhjxhmcFjdjR-xQiI-slF-sijS8vE5Ut_LofTg99W4hi2kBdmO0q1tVqPVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنای آمریکا به طرح توقف جنگ علیه ایران رأی منفی داد
🔹
مجلس سنای آمریکا به طرحی که خواستار توقف هرگونه عملیات نظامی علیه ایران در صورت عدم دریافت مجوز از کنگره بود، رأی منفی داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/676768" target="_blank">📅 20:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676767">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWKaxWawWKIH-80bN7g9UlkI_NdhZmIJLcGlaRNDe8v9DlyQoAdCgUzmz8wF02PRAiUHx7Vxhcof1H39TJ_7EnhRfPu4c6ykv6ydjZIHp_yZkl4t4ryPrOGdLPxK2aGrc56yK01hWCiX2POa3e2KauIinX_cqmxb60GtA8q_kGE_fUPv_-f6A0SEMBkZGjOYRSl649Mk8zKVbXDGtgX5_z13C2B8-BFroTVyEUwzw9mPV5EJ_e8qkSmoVita1JbAhusTp9uqHKgmZtYSsuBPswc9ShxxBkxFyuEcxdj2TB3HqhYjLBtavytHRi9A7PncbGLEnJPCTX_2Ryf3-VIBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌹
یک قدم تا زیارت کربلا…
با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و فرصت خود را برای برنده شدن یکی از ۱۰۰۱ سفر زیارتی کربلا امتحان کنید.
✨
این سفر معنوی به همت هیئت قرار برگزار می‌شود؛ شاید نام شما یکی از زائران این کاروان نور باشد…
📲
همین حالا عدد ۲ را ارسال کنید و در این پویش حسینی همراه شوید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/676767" target="_blank">📅 20:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676765">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
المیادین: وزیر خارجه اوکراین در تماس با عراقچی از ایران عذرخواهی کرد
🔹
یک منبع آگاه در تهران به شبکه المیادین گفت آندری سیبیها، وزیر امور خارجه اوکراین، در تماس تلفنی چند روز پیش با سیدعباس عراقچی، بابت حادثه اخیر از ایران عذرخواهی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/676765" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676764">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTHkUm2BI8h-nYJ_hq9uypkcWtVxuTKUl2Tlug0Z6npUFn208ymoEu-pa6KcwKq87oY1YiCafb0O9_Iv25JFL_-XVykbsmTK8XUu6T6aXd03vDbR01-fHRutytvSp0L63V4F3IpfqlJiPN901BqYa_geuk-v8WAxtCBI2GtyVjBDcW-SH-tmY8hq7bSyepvyDkZqwHWl8uCacviwzOM_1YFdP-nRGXQ_2htE97F3RxD8XLyQXX2vfRtc9mUeivBMZkIZSQlyV9BirKMV4-riMOwQGDG2ewz5osdvFsZ4Rhbbnjx1Y9501kuyZOSD1YMLEsJhFBS82wH23ug2PbmaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدم‌های سبز، قلب‌های سفید، قلم‌های سرخ؛ روایت ریحانه طاهری از سفر اربعین با کاروان شاعران و نویسندگان
🔹
ریحانه طاهری، شاعر، در یادداشتی با عنوان «قدم‌های سبز، قلب‌های سفید، قلم‌های سرخ» از تجربه حضور در کاروان شاعران و نویسندگان راهیِ کربلای معلی نوشته است؛ روایتی ادبی از سفری که در آن، زیارت تنها مقصد نیست، بلکه مسیری برای همدلی، روایت، مسئولیت و تجدید عهد با آرمان‌های عاشورا است. او در این یادداشت، از هم‌قدمی اهالی قلم، اشک‌ها، دلتنگی‌ها و رسالت نویسندگان و شاعران در روایت حقیقت سخن می‌گوید.
🔹
طاهری در بخشی از این روایت، دیدار تأثیرگذار خود با یکی از شاعران حاضر در فرودگاه و دلتنگی او برای رهبر شهید را بازگو می‌کند و در ادامه، از «قلم» به‌عنوان سلاحی برای ثبت حقیقت و مقابله با فراموشی یاد می‌کند.
🔹
متن کامل این یادداشت را از طریق لینک زیر بخوانید
👇
https://www.khabarfoori.com/fa/tiny/news-3234297
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/676764" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676763">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سخنگوی آموزش‌وپرورش: مدارس همانند سال‌های گذشته، در زمان مقرر بازگشایی خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/676763" target="_blank">📅 20:41 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
