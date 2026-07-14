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
<img src="https://cdn4.telesco.pe/file/OFmAsl6AJkLnCDdVMTYWn0Nvq4a6zMxJkG7jW0LVOWH0zYiDhf8XYAfIYYEbtUaHMt9KBURRypRn607pWUJOE9IA78uZwioSJPKGswfd1ruU0z6iQaJjwa_BrpbbqkrQDIMzzOSAIY8XouiewMkIyl_W8k4UZ_TZHpL1Y9fEuCUrb_jmqcLUhGAAT4zBwd5_mTMUXrD1FFB1Y6PyvCrUKEj30I6qGNc51Udtn9IPVyPkf0rwqP9vbr5CMKDo7COiNh4M2nKEZtAf1ZOiFsmmKu6rN3csrbxgZw_emlj4uyQ8zgNyC9piy1cPnelRsnxLk0FKWmc3CzW_uMN449fR0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 918K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-134067">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Hlk5SvB2-WZtzlmPr84qMRP7JAr9FpIOvN8YcfK2zUwyHCcIKlX9MgutSZONrcTG1WYtPxYOD7oRpOYsOi3NJd7Dcdj832OWPMhd4bbWrCn3EPDeQa4X__tgSuELqN-odpvx-Lr3p06mtZsYk8N6iLTiSdFElWkaoAwe_cBe8pjnmITb4pEw--NCeOpUNkG6pw2hjpyvN2z4mXSyvVY38merMOKcQMCjZgK6jA68Gym9U0iqJwwzdHAae7xtFRVAlyaQvSWEtR-A5LLSc27sI6JWpuAoyCMuBEumFOfWE5PyJSOhg1ERWmF2GCdcH3DlLTKa1seOA-4yP_3Ainz8sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97470ef355.mp4?token=Hlk5SvB2-WZtzlmPr84qMRP7JAr9FpIOvN8YcfK2zUwyHCcIKlX9MgutSZONrcTG1WYtPxYOD7oRpOYsOi3NJd7Dcdj832OWPMhd4bbWrCn3EPDeQa4X__tgSuELqN-odpvx-Lr3p06mtZsYk8N6iLTiSdFElWkaoAwe_cBe8pjnmITb4pEw--NCeOpUNkG6pw2hjpyvN2z4mXSyvVY38merMOKcQMCjZgK6jA68Gym9U0iqJwwzdHAae7xtFRVAlyaQvSWEtR-A5LLSc27sI6JWpuAoyCMuBEumFOfWE5PyJSOhg1ERWmF2GCdcH3DlLTKa1seOA-4yP_3Ainz8sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه امروز رگباری از پهپادها و موشک‌های بالستیک را به سمت کی‌یف شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://telegram.me/alonews/134067" target="_blank">📅 16:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134066">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhG3PMDCY2uMGbmBwIgie5HYX_8dPcsp96AJvvBZ2maORCfN9s4xpIV4Ibq6OPLCy0z6eEUupVFzoHXesC5hemTFOwzXo5S6k6UknfC1a8J0X4L702CPnuVvdr6l9VAnMhyC-cOYEFJYRYtipQdENPUIFctLAp1svRlR2NqIlW82RTYQRRgeWxrfmTkYK2TMGz6tGO233fbP7rky41up10cDTruawUsEg8A0ZP-fPT8Woq_g-mBsT8GIaIG3X6Palyqr0T3iNNN0ehsk_1VnKhhpXhmndn4qTH7m537ro-9VeFsiH1QQ8-8em5pOPZWqnUvJVw3v4LXYuBcIGhWQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلسه صبح امروز دکتر احمدی نژاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://telegram.me/alonews/134066" target="_blank">📅 16:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134065">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6da19594.mp4?token=p_omIrwdKccLZFw4bHKrwAZY1faQbvkSTSCVFvxmjATBOnLulWeZZQCqmIwFV9Z8Ik74IiXSLMsDgA2sqH28WRq3-mdnyytjNEc_avcBftHJgG32OambXbwJR18n0OoNcYKHCDDuUPjPenVfsp0GIx4lk44cwDChv4wehKkLUNXW5Q8_Gz56QqUvSuAfN1l1UOiRLvGijqTgWHRmqLkbyFraGaULaMUhrvoLyw-QA5F_6HYU0bh6_Z3POEOnCKQg0iPtb_sfn3TITfHu8ed9eHN3JYh9Trrizlnt6ZzOrw-IUYMNc-8nMryzxI03wQf2q9V3ljC0RoaGp_WN6QG6mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6da19594.mp4?token=p_omIrwdKccLZFw4bHKrwAZY1faQbvkSTSCVFvxmjATBOnLulWeZZQCqmIwFV9Z8Ik74IiXSLMsDgA2sqH28WRq3-mdnyytjNEc_avcBftHJgG32OambXbwJR18n0OoNcYKHCDDuUPjPenVfsp0GIx4lk44cwDChv4wehKkLUNXW5Q8_Gz56QqUvSuAfN1l1UOiRLvGijqTgWHRmqLkbyFraGaULaMUhrvoLyw-QA5F_6HYU0bh6_Z3POEOnCKQg0iPtb_sfn3TITfHu8ed9eHN3JYh9Trrizlnt6ZzOrw-IUYMNc-8nMryzxI03wQf2q9V3ljC0RoaGp_WN6QG6mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی که یکی از سربازان ارتش آمریکا منتشر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://telegram.me/alonews/134065" target="_blank">📅 16:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفارت ایران در ابوظبی: ۵۵ صیاد اهل سیستان و بلوچستان و هرمزگان که به دلیل اختلال در سامانه‌های ردیابی توسط گارد ساحلی امارات بازداشت شده بودند، پس از بیش از دو ماه آزاد شدند و در حال بازگشت به کشور هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://telegram.me/alonews/134064" target="_blank">📅 15:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134063">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
👈
فارس: انتخابات ریاست کمیسیون امنیت ملی مجدد برگزار می‌شود
🔴
یکی از اعضای کمیسیون امنیت ملی مجلس: انتخابات هیئت‌رئیسه کمیسیون امنیت ملی، در هاله‌ای از ابهام قرار دارد. قرار شد امروز عصر انتخابات در سطح ریاست، مجدد برگزار شود.
🔴
علاءالدین بروجردی و ابراهیم…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://telegram.me/alonews/134063" target="_blank">📅 15:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134062">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک کارشناس:
آمریکا ممکن است در جریان جنگ با ایران بین یک سوم تا نیمی از ذخیره مهمات حیاتی خود را مصرف کرده باشد
🔴
این موضوع نگرانی‌هایی را درباره کمبود‌های آتی ایجاد کرده
🔴
یک سرهنگ بازنشسته تفنگداران دریایی آمریکا می‌گوید «اگر امروز سفارش یک پاتریوت جدید بدهید، تا چهار یا پنج سال دیگر آن را تحویل نخواهید گرفت»
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://telegram.me/alonews/134062" target="_blank">📅 15:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134061">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f866843be5.mp4?token=PQQKX4-hRQjYyf1NPNqoGmxQz5dWssAG2Mo7deaDGlhpPnxgFRmOaweJnlI_ioeB42qojzGEUUQjqzn5ViI7MbatCiWWtB9-d1IB2gYT4VIWR4TJskRL3uIiaWCQSp2BAdW_l4iLTQWNMkKuFgm4WBsdu_uUzvQv08flXa5yUU5ODX5gFXIRAXx7pafpNJRsnjafMQDV9HOGQSAj4ofrFDYvMl5IusFzpMf3Fff_OZP9r6L801PgTv3kjJ6mj6ZCeq5-v2-ON8EWahXOrcOTl4AcasvtbgR7o2xZ6tyFGdhz0-ukfS2MGdu9MjO2J-xjfhGpGvjpQuOyUDj8QXCT6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f866843be5.mp4?token=PQQKX4-hRQjYyf1NPNqoGmxQz5dWssAG2Mo7deaDGlhpPnxgFRmOaweJnlI_ioeB42qojzGEUUQjqzn5ViI7MbatCiWWtB9-d1IB2gYT4VIWR4TJskRL3uIiaWCQSp2BAdW_l4iLTQWNMkKuFgm4WBsdu_uUzvQv08flXa5yUU5ODX5gFXIRAXx7pafpNJRsnjafMQDV9HOGQSAj4ofrFDYvMl5IusFzpMf3Fff_OZP9r6L801PgTv3kjJ6mj6ZCeq5-v2-ON8EWahXOrcOTl4AcasvtbgR7o2xZ6tyFGdhz0-ukfS2MGdu9MjO2J-xjfhGpGvjpQuOyUDj8QXCT6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیام صدراعظم آلمان، مرز، به مسکو:
زمان آن فرا رسیده است که به میز مذاکره بیاییم.
🔴
زمان آن فرا رسیده است که بر سر آتش‌بس توافق کنیم.
🔴
زمان آن فرا رسیده است که خونریزی غیرضروری در اوکراین را پایان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://telegram.me/alonews/134061" target="_blank">📅 15:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134060">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
آژانس ایمنی هوانوردی اتحادیه اروپا (EASA) به دلیل تشدید مجدد تنش‌ها میان آمریکا و ایران، به شرکت‌های هواپیمایی دستور داد از حریم هوایی بحرین، کویت، قطر و امارات متحده عربی و همچنین بخشی از دریای عمان اجتناب کنند.
🔴
این هشدار برای «تمام سطوح ارتفاعی و پروازی» اعمال می‌شود و تا ۲۹ جولای معتبر خواهد بود، مگر اینکه زودتر مورد بازبینی قرار گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://telegram.me/alonews/134060" target="_blank">📅 15:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134059">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فرودگاه بن گوریون : حجم سوخت‌رسان زیاده، دیگه نمیزاریم چیزی فرود بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://telegram.me/alonews/134059" target="_blank">📅 15:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134058">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
واکنش شرکت مخابرات ایران به انتقادات درخصوص گرانی بسته های اینترنت ثابت: قیمت بسته افزایش نداشته است، فقط حجمشان کاهش داشته است :/
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://telegram.me/alonews/134058" target="_blank">📅 15:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134057">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ8XetlnNs96csF08Vqt0qFpWZhXhJIYcQEAokaT041k2xtSbk6AY8KukIxJb9DuQZODg6YSZ7Hq4ax_Tvvz724IF2vqPsxZmibZSzXsLk3njFWJ6o8faCd-b9RLRosdSpz7TmoRc6KWFm7dH-6P7oIjL5zAex_UIO9y9UKGL2vcDNnKuhxB3YYdEPwDv7ZsQEFVfaUl0UdOhW1kvGDjZ7i6xpXZ-Z0JP5tMJBpLtM7BtpGbt7D3F2Ri0BCcb_xhjSbvnqCwVoW10YuH09zg766wvmHj5BOym0Jpffw7gPgiHVI3FaoElUSPdr4TEDJr0I3lY3BzUlNrjUF4XOdbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه آمریکایی: ترامپ در مورد وضع ۲۰ درصدی عوارض بر تنگه هرمز جدی است و او ماه‌ها به این طرح می‌پرداخته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://telegram.me/alonews/134057" target="_blank">📅 15:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134056">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر خارجه روسیه: حملات کی‌یف به کشتی‌های غیرنظامی در دریای آزوف، تروریسم محض است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://telegram.me/alonews/134056" target="_blank">📅 15:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134055">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از یک فرد آگاه نوشت که مقام‌های کشورهای حاشیه خلیج فارس مظنون هستند ایران یا گروه‌های هم‌پیمان آن از توافق‌های رومینگ میان اپراتورهای تلفن همراه منطقه برای ردیابی نیروهای آمریکایی سوءاستفاده کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://telegram.me/alonews/134055" target="_blank">📅 15:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134054">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ-qSr1Ob_o_Oxu-m-CCl4i0I0BX-t7UyISo3KK2d-M8Y64qmhlpi5euTjk0XsJdHOiQNQD0rNMkmSosA3qmcIsLK5Chw00UIeohn2X2yzJ82qCpqCRj363md25cPLzB83-vSgXt2nZj6AodIQxUfG0PT3pu3x0LtoFbRYkQ3upwCsJQCwQztguNGyd5juSy6Yp0uyZs8-XSBFN7kXDdO1QqdfXyPy4UqmR0cLkgtRCIky3QdLBgr6B8jitpuX0VlzKWTv8460pSsxIMDpk_zUtK1TYYmpLbEwU7XSAW9D5nIraH9oW-K8yjUyyniJEg1OS3AVSbs2G74zA9Sm4imA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش نشریه واشنگتن اگزامینر، در طول 26 روزی که از امضای توافق‌نامه تفاهم بین ایالات متحده و ایران گذشته بود تا زمانی که تحریم‌های آمریکا دوباره اعمال شد، تهران بیش از 6 میلیارد دلار محصول نفتی به خریداران خارجی صادر کرد.
🔴
با این حال، تحریم‌ها قبل از آنکه ایران بتواند ظرفیت ذخیره‌سازی خود را به طور کامل خالی کند، دوباره اعمال شدند. در نتیجه، حدود 30 میلیون بشکه نفت خام قابل ارسال نشدند.
🔴
با در نظر گرفتن صادرات انجام شده و کشتی‌های بازگشته، حدود 60 میلیون بشکه ظرفیت ذخیره‌سازی همچنان در داخل محدوده تحریم‌ها موجود است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://telegram.me/alonews/134054" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134053">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d196b16ee9.mp4?token=UbHV7fKS1Pk3KjAluEyyz8cEakZv7UVKoPzeGRhXHUkl_8gRuZ32ruW1c4Y33QA4a8HOiGFe9xTfl7fbab42dfvSyuPk26Sh36clsUAMZUS_tjnDLUfFn_R8_LH98LHiVFhTi9NchkilfwPFXIRGO72g0R6hDxlom0gVhlf3tEXA-FwClp8NnzgUG4CwWqtdBTbOPR3I40Bt3e6SbhZnDMzIM5NbTLI_jgbifwe-xGWBhGV7ad80rA75T_Jmhvq2MVr4CwVA30Uk7aa-zjqeOfWvE80QxQM_umB1V5QiJ78ni3FMTT0MmUZEnLq4Rbqfmzm3UN_kUhr15URluQjFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d196b16ee9.mp4?token=UbHV7fKS1Pk3KjAluEyyz8cEakZv7UVKoPzeGRhXHUkl_8gRuZ32ruW1c4Y33QA4a8HOiGFe9xTfl7fbab42dfvSyuPk26Sh36clsUAMZUS_tjnDLUfFn_R8_LH98LHiVFhTi9NchkilfwPFXIRGO72g0R6hDxlom0gVhlf3tEXA-FwClp8NnzgUG4CwWqtdBTbOPR3I40Bt3e6SbhZnDMzIM5NbTLI_jgbifwe-xGWBhGV7ad80rA75T_Jmhvq2MVr4CwVA30Uk7aa-zjqeOfWvE80QxQM_umB1V5QiJ78ni3FMTT0MmUZEnLq4Rbqfmzm3UN_kUhr15URluQjFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما از جنوب کشور :با بسته‌ماندن تنگۀ هرمز کشتی‌ها همچنان در خلیج فارس لنگر انداخته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://telegram.me/alonews/134053" target="_blank">📅 14:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134052">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
استانداری هرمزگان: در حملات جدید آمریکا به برخی نقاط استان هیچ مصدوم غیرنظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://telegram.me/alonews/134052" target="_blank">📅 14:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134051">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پهپادهای اوکراینی شب گذشته به ۱۱ شناور در دریای آزوف حمله کردند، که شامل پنج تانکر، پنج کشتی باری و یک یدک‌کش بود. این حمله، نهمین روز متوالی از یک عملیات گسترده برای هدف قرار دادن کشتی‌های روسی است.
🔴
نیروهای سامانه‌های بدون سرنشین اوکراین اعلام کردند که بین ۶ جولای و ۱۴ جولای، به ۱۱۶ شناور روسی حمله کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://telegram.me/alonews/134051" target="_blank">📅 14:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134050">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVWsoM2mosONBaeTROk5ZVlbRGuM9HOWMX4jHDftKhP7igjZu5cgM_y0SRpXUr86qxWCYoX-dcwjdBuJbONaST5zew3AN95sOezy_Bsc5nj6DXmmseiEimit5eaGOWShfgSLbv0r4GwmeqTtmLypxE2RCP4_9ZVvgfP02k67-3ATZ1s3IjzfzJI4tQyxVXLtoD5C7j3N8AGUx1DXJiaLbwCZRrODUkl_UZq5K3D7CDiFaaEYnJ_TVUNi4aBcfpjhgRyijg2e1Cmrq6CMKSrjdetdOngjqzwIecyjfaxGhl_28R2PpI8ScTwaYNgH_ZjOxHSbT-jrZDXRpEVrEu-wAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان:
پاکستان به شدت حملات آشکار انجام شده علیه کشور برادر، عربستان سعودی، را در شب گذشته محکوم می‌کند.
🔴
این اقدامات ناپسند، نقض حاکمیت و تمامیت ارضی عربستان سعودی محسوب می‌شوند و می‌توانند به تضعیف بیشتر صلح و ثبات منطقه‌ای منجر شوند.
🔴
پاکستان بار دیگر از حمایت قاطع خود از امنیت این کشور حمایت می‌کند و در این زمان حساس، همبستگی کامل خود را با کشور برادر، عربستان سعودی، اعلام می‌دارد.
🔴
از سوی خود، پاکستان به حمایت از تمامی تلاش‌های صادقانه که با هدف ترویج صلح، ثبات، امنیت و درک متقابل در سراسر منطقه انجام می‌شوند، ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://telegram.me/alonews/134050" target="_blank">📅 14:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134049">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فرانسه: هیچ قصدی برای ورود به درگیری‌ نظامی در خاورمیانه نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://telegram.me/alonews/134049" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134048">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌
👈
فارس: انتخابات ریاست کمیسیون امنیت ملی مجدد برگزار می‌شود
🔴
یکی از اعضای کمیسیون امنیت ملی مجلس: انتخابات هیئت‌رئیسه کمیسیون امنیت ملی، در هاله‌ای از ابهام قرار دارد. قرار شد امروز عصر انتخابات در سطح ریاست، مجدد برگزار شود.
🔴
علاءالدین بروجردی و ابراهیم عزیزی ۲ کاندیدای جایگاه ریاست در مجلس هستند که طبق اعلام اولیه نتیجه انتخابات، ابراهیم عزیزی به‌عنوان رئیس معرفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://telegram.me/alonews/134048" target="_blank">📅 14:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134047">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مذاکرات بین اسرائیل و لبنان در رم آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://telegram.me/alonews/134047" target="_blank">📅 14:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134046">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
استان خوزستان: منطقه ای در شهر آبادان مورد اصابت موشک‌هایی قرار گرفت که توسط نیروهای آمریکایی شلیک شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://telegram.me/alonews/134046" target="_blank">📅 14:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134045">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGlAXB-4dbd5Kjru09U57Lo3j5iDryD2R7f1nNRRntGZTgKQiQDasPnQlKpplmH99i-AdDwmcHWKNUtRrkbjYspdjHTFCWBjls1XQN45bW9bL_mTbOD28DMrlQiuN_Hm4D_M0BaqlQODqbM_H5ij8SeuS0wXHZKuLylzsuk0swCpSSj88ZZffX8jz2qUkMNRBlip9PrNgXnExA3Im76gpqtUp8Xak0JCc1IFxZYH9qAFSJ7YOO4_E9X-ksKEx4QFw6iJ6fDfe-wspYslSj1ieDAcYnQT02Yoe1wwkyiJENM6G4VqawWZasNd1d_yOSChUu3nedGlWXTZT_QaNJwNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی پیش، آتش توپخانه‌ای ارتش اسرائیل مناطق حومه شهر قنطره در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://telegram.me/alonews/134045" target="_blank">📅 14:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
روزنامه اطلاعات: کالابرگ دیگر گره‌گشا نیست؛ تدبیر دیگری باید کرد
🔴
ارزش یارانه یک میلیونی تا آخر امسال به ۳۰۰ هزار تومان می رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://telegram.me/alonews/134044" target="_blank">📅 14:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ce5ac263.mp4?token=lyAfjbRYaYDItq_jiLmA_YvsKGJX5oVevIZPT2cMbikDVO0Pt_WTEJuQ36_VbULwHcItPDkBzzWPkKYn_BglaNBQLXnz1I4K0Puo1tBe2Fr9Ne60bvUYXptDu8ZE5104dRo3HdpUD49Oj5Il2NDSWAD5YCZyC2zJEyB2wAq0AkgdIYK6HspJCDA1gPPGs92lPK8fvuLSZaP6VweoGz9Pv35FdoGaST10myBMxFasGN_JSXE6__KIiq-Q0pM_UlcfiKfih5lleTpmKge_APqQa8ZLtcwfa1yRBwgIZaSoxhHeoH1htKvvB62pRtKDw60HgvTpo1_CGJRt9K5vPznckw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ce5ac263.mp4?token=lyAfjbRYaYDItq_jiLmA_YvsKGJX5oVevIZPT2cMbikDVO0Pt_WTEJuQ36_VbULwHcItPDkBzzWPkKYn_BglaNBQLXnz1I4K0Puo1tBe2Fr9Ne60bvUYXptDu8ZE5104dRo3HdpUD49Oj5Il2NDSWAD5YCZyC2zJEyB2wAq0AkgdIYK6HspJCDA1gPPGs92lPK8fvuLSZaP6VweoGz9Pv35FdoGaST10myBMxFasGN_JSXE6__KIiq-Q0pM_UlcfiKfih5lleTpmKge_APqQa8ZLtcwfa1yRBwgIZaSoxhHeoH1htKvvB62pRtKDw60HgvTpo1_CGJRt9K5vPznckw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پایگاه هوایی شاهزاده حسن، اردن؛ تصاویر ماهواره‌ای خسارت‌های وارد شده را ثبت کرده‌اند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://telegram.me/alonews/134043" target="_blank">📅 14:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCTpwYBKFzEEtgaLgkhb--hCu3Pu8vgZQNh7PpvJF269b8d-3ZNNNZ_ebkj5iuD230oA6oLkoUQEtYG4WqEDrh5BOQCPs3ecFTqWPjLzYLuP-ap7PZvIGQuFlqGpW3gr3zQ4ad29JE1ZDm6QnNtPEsKHbliZ9vyCcOxHXopyhrB5H1qzC0kY_s2GSbQ_o21BdRnqzTNK8qy5U8G7vEFx8EdcN60-b9uFKNxdPvB2m2zEah3ojvbQkcivh8Cr2ktJUrOuNTImB1OfWUnFM_x4_timzqA1-fmDjHOJt1Vgd4a7Za34b4w9wSz-vuYwlqNgl2KbZ1hM-S9n210bB3h0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوستر جدیدی تو تهران نصب شده :
خون در برار خون
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://telegram.me/alonews/134042" target="_blank">📅 14:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw8HA2zeIFP9vGcindOQ1kHNHlA0Te9HrVhTzIvb-f2-nU4pUHdI6F6sX1tkfW21m_oDAz3ap5h4_gG-26tBkjiQj-eVJDkHsS02twiRAbGWN_3-yw1tNcfWaltp10CfJYRaIOaG8ABNl4Xg5G8cs1B6kNvWy1N3oIwWIe2GL_pQ0109WLnJ7wxXNcJrWGR3R024iGG1bCreUxXfTBDUL9GriVXntLN1w-OdBQMiOgnrruZLjM3soq2IaqQ4Z2ESGYTLgc6ibuIVRGIUwMGsuHQX-HCRTz4YH9KdfeXh1-LT2AT8h3TuklF8YRg09UktggwmEtjZun_FWTpJoBSqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۸۷.۲۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://telegram.me/alonews/134041" target="_blank">📅 14:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
یک منبع ارشد در تهران به سی‌ان‌ان گفت اگر دونالد ترامپ تهدید اخیر خود مبنی بر حمله به کوه کلنگ (Pickaxe Mountain) را عملی کند، ایران «پاسخی ویرانگر» خواهد داد
🔴
این منبع افزود: «اگر ترامپ به تهدیدهایش عمل کند، ما پاسخی ویرانگر خواهیم داد و بهای آن را سربازان آمریکایی و شرکای منطقه‌ای او خواهند پرداخت.»
🔴
این منبع همچنین تأکید کرد که ادعاهای آمریکا درباره انجام فعالیت‌های هسته‌ای در کوه کلنگ نادرست است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://telegram.me/alonews/134040" target="_blank">📅 14:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خبرگزاری دانشجو (SNN): یک حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://telegram.me/alonews/134039" target="_blank">📅 13:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJEFYIDorVzp8yFUCqYHxXBEEHr0A6BtbwPbH7VsLfk4rvq8D_zgxy34zrlKxnkrcWXys4PpTiVlrddwSUsXWrs4W-PC_Ru00ZXrWIUsXULdGetbxbKGRdzpbSxBiP0_Q8An_Mgk39VblrrUV48iEQ8wpLGp2Y-fGc20kLQ4L_Nh9l4nUFY_PUl1ycO-U3s8CxCWbsXru12GbWM1M0Ae_W6ZV2P2hiV1w0F-YuLHMvfMd_aWc6vemRfqWFGR_1-OJfqvejkSg5K9sAfDkd4wAnYA9Y1g1-yHXi4BG-6ABYWnI1AYS6T3LAEyL-IN6a0dm1eadxaBQenyO0sJ4bnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حالا که کنار گذاشته شدید، توییت بزنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://telegram.me/alonews/134038" target="_blank">📅 13:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/062bc90f38.mp4?token=oJwi_16cqobd1vlIYVoXe9UTBFLWA8jPZFU1OqCgNiY2ejwyQSzbw6fqzIWnv7ooM0ivDB6TXSKP7nIXR_7m-1o5hxEyI42APVT3O32J-BaXQyHa9b_mlQn0cC7sSFbNl8AEiveGbT__PzA5OQQOAhzeT162cZV_TTNVfuooNyMFevroh9BeXwaTKKkHkJUXM2K0qm1suLd_PdL-JbiWspzcLgxfRDzjvo9bsk62Y5Gmwc-bgH-UR5ln0vi6w47m08alsYvS236bvi6IwQrXd66X_Ky6UP0SrXR442flOI4WLgUEdbCaUubLiy286WWEhE5Km-XS3i51EVMJd7WnFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/062bc90f38.mp4?token=oJwi_16cqobd1vlIYVoXe9UTBFLWA8jPZFU1OqCgNiY2ejwyQSzbw6fqzIWnv7ooM0ivDB6TXSKP7nIXR_7m-1o5hxEyI42APVT3O32J-BaXQyHa9b_mlQn0cC7sSFbNl8AEiveGbT__PzA5OQQOAhzeT162cZV_TTNVfuooNyMFevroh9BeXwaTKKkHkJUXM2K0qm1suLd_PdL-JbiWspzcLgxfRDzjvo9bsk62Y5Gmwc-bgH-UR5ln0vi6w47m08alsYvS236bvi6IwQrXd66X_Ky6UP0SrXR442flOI4WLgUEdbCaUubLiy286WWEhE5Km-XS3i51EVMJd7WnFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روح الله زم در سال ۱۳۹۷:
محمود احمدی نژاد هرکاریم بکنه؛ نظام جلوش کوتاه میاد و کاری باهاش نداره.‌ چون سند و مدرک زیادی از مجتبی خامنه ای داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://telegram.me/alonews/134037" target="_blank">📅 13:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مهندس ایرانی‌تبار در آمریکا به اتهام صادرات غیرقانونی فناوری محکوم شد
🔴
بر اساس گزارش رویترز، یک مهندس ایرانی‌تبار در آمریکا به اتهام صادرات غیرقانونی فناوری با کاربرد بالقوه در پهپادهای نظامی به یک شرکت ایرانی که یکی از مشتریان آن سپاه عنوان شده است، مجرم شناخته شد.
🔴
دادستان‌های آمریکا مدعی شدند مهدی صادقی به همراه یک تاجر ایرانی، در ساخت سامانه ناوبری مورد استفاده در پهپادهای نظامی ایران نقش داشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://telegram.me/alonews/134036" target="_blank">📅 13:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
دلار هم اکنون 184,000
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://telegram.me/alonews/134035" target="_blank">📅 13:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134034">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ درباره لیندزی گراهام:
پزشکان گفته‌اند که یک بخش خاص از بدن او به معنای واقعی کلمه منفجر شد، این وضعیتی است که پدرش هم داشت. در پاسخ به تئوری توطئه، دوست دارم بگویم بله، اما فکر می‌کنم او مشکلاتی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://telegram.me/alonews/134034" target="_blank">📅 13:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134033">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Gymfl6Kcz6peISrQCy20MF3sh3rCrpctOCVhK2L0FY5HBXupzRszJr40OUggnbMkZVGEzUvdsGyTNmjC1xRoaMBvf61HcIUux5IT2Kq-G_YHTUto9iU3N7-jGgLFnf3XNcM1BIpzwPet4yMuA2jDHB-KcaZtqeraDG-QThFkhQdM_JvWidksCYvwr7BvJnhiOhsWcZnNJvxS_CQktzf6FLEwEEartsRN6FQee3gzEKr1MUiePSuHAxRo8V7JPaMZ1cNHfr8seFVhD6R6Cd6h0h2W4BGwGwVs8hKguxcVl-x6mf7dNSfhyT4ZGuvMjuGmmGCyJghVzSh8ZiikhZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتست به بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://telegram.me/alonews/134033" target="_blank">📅 13:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134032">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: ارتش آمریکا تخلیه هواپیماهای سوخت‌رسانی آمریکایی از فرودگاه بن گوریون را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://telegram.me/alonews/134032" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134031">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دقایقی پیش؛ صدای ۵ انفجار در غرب بندرعباس شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://telegram.me/alonews/134031" target="_blank">📅 12:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134030">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
دقایقی پیش؛ صدای ۵ انفجار در غرب بندرعباس شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://telegram.me/alonews/134030" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134029">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZCFc_Og6v91tbwKWFvqNiJzZB8SIdypPRbIK-Sak4E703B9fU0cvNUaXKfNArhGzdScS1udb9Tl_VflwmgeHn4_20VEUQ7sRvv6lv287zRh7LVSh0P1bLud_8_VMhs4UWxVBFNE2Np8H9WOtzCdVaR-toqQ245_FbOAVJDtpbmy0oH6gXqQkyvybe97SD97WbfuxC3V0RtEYaXYQz3pk9i_Dpzl6mv-hQP3a6HEBo3Zo0ah02AJBZzUwlBCs7CrFvI_IOm2VDR4z8FW6Zafq4NDvY0N1fUOpHMTreyoW1BEK1yOyGZ64Hp3gem1sv1pejVgmY2dazyQROtP4dVVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وایچرت: بن‌سلمان خود را برای جنگ زمینی آمریکا با ایران آماده می‌کند
🔴
برندون وایچرت، نویسنده و تحلیلگر آمریکایی:  دلیل حمله سعودی‌ها به حوثی‌ها این است که محمد بن سلمان به وضوح می‌داند که ترامپ به زودی قصد دارد حمله زمینی آمریکا به ایران را آغاز کند.
🔴
در آن زمان، حوثی‌ها به هر حال به سمت سعودی‌ها حمله خواهند کرد.
🔴
بنابراین، محمد بن سلمان در تلاش است تا پیش از آنکه آمریکایی‌ها نقشه دیوانه‌وار خود را آغاز کنند، به طور پیشگیرانه شرایط را به نفع خود تغییر دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://telegram.me/alonews/134029" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134028">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VbpGBmj-GDgzP2_A7HLhdqvMuwYy6Qs81pUXivqukp-qtpqGw7Kk1gT2lpSRKS1-4HdEgY_ZkqSlf0F53xay0SdpygGVXujASo-UiM1569Ppd_G0V9If-lNcHlQRdpUGVhGqrJbKjWuoRVG4Ag-keez6HMrTMfb0Cbzcf6Z96wIzsO72nqwC2SQLQRsY37t-IR2h4wWEsd6ncs7q_t7sPMK4pQI6iBSlpYQIUFZGG04eakWLOoZ7_IrSh-kFyJy5xINOe5I0-WOoT4k5jQYBcqY6Wt1DmkWVz2OGg1HxxQ3j7xYrTX1brfXnTC8t_1qWzk5ncQjlYgG3Pwdq3rU_dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محدودیت کامل سرویس های گوگل و گیت هاب در روسیه اعمال شد
🔴
هم‌چنین سایت اپل نیز از دسترس خارج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://telegram.me/alonews/134028" target="_blank">📅 12:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134027">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqbjpxmLkNUXPplYbNn6ocPWuLotfYvPN5EmKbH_X_dsPH2A67jLeVV0V-ZL8NJfte2tz1Vhz2Zwc_gItGQsMBbZHNIZvITKoMRTsavVXXr6PvjA6-ZElQwg9kYQj9w2nPGS_g8VyoFeN69EhTYkTmJ3j4MG8r2YKU2KOuW6DB9QSNT-7Hah0psf3cHwA4lfZLgEpHURlTtp7hod9FJZ_Zn-zRdeHdmOPAiaKQRP3r4_TofnJO9pLoMDveKlrPwuwcSM-bubRePzUbkXXYkSV-7Cqk8ciIHRTz9SvhaTv9mLvM3OHICWmy0_WE12mG2lOILpTlW9qrpoEBn0JKtT1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ندا خدایاری ، خبرنگار حوادث : انتقام از نامزد سابق، به مرگ دختر همسایه ختم شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://telegram.me/alonews/134027" target="_blank">📅 12:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134026">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
روزنامه «واشينگتن پست»: 19 ناو جنگی آمریکا در خاورمیانه مستقر هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://telegram.me/alonews/134026" target="_blank">📅 12:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134025">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مترو و اتوبوس‌های بی‌آرتی به مدت ۲ ماه دیگر رایگان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://telegram.me/alonews/134025" target="_blank">📅 12:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134024">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: در حال حاضر، مذاکرات پیچیده‌ای در جریان است تا یک توافق بلندمدت حاصل شود که از آزادی تردد در تنگه هرمز اطمینان حاصل کند.
🔴
ما مسئولیت داریم که با ايران و جامعه بین‌المللی همکاری کنیم تا به توافقی دست یابیم که آزادی تردد در تنگه هرمز را تضمین کند.
🔴
خطرناک‌ترین تهدیدات برای امنیت خلیج فارس، نه از داخل آن، بلکه از تصمیمات و اقدامات موجود در خارج از آن، به ویژه در تل‌آویو، سرچشمه می‌گیرند.
🔴
باید روابط با آمریکا را بازنگری کرد تا با واقعیت‌های استراتژیکی که جنگ آشکار کرده، همخوانی بیشتری داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://telegram.me/alonews/134024" target="_blank">📅 12:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134023">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/کان نیوز: ارتش آمریکا هواپیما های سوخت رسان خود را مجدداً در فرودگاه بین المللی تل‌آویو مستقر کرده و برنامه ریزی برای بازگشت سوخت رسان ها به اروپا را نیز لغو کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://telegram.me/alonews/134023" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134022">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۸۲ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://telegram.me/alonews/134022" target="_blank">📅 12:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134021">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2041b839.mp4?token=eiqdI1jWlmOk3-7TwgKEa3R05wIpRmIkTbY79JDOuBEon0sCJfEC7o82d5HMJslH3_zPKp--5e6MCy5eGjid60TxHmfNw9sd7KzcUmQbf2DTpPGtwJrGhUZSJX-CmEZcLpO2UgAwXbKjZWzaD5F8S9XJrBFlyt5KYDOSu3SlGL2GfeyQbYRp8C28kLGhktbGZiwnkGfPFsRQqkFykhpBrNjalCbBM8aTx88IvJ1bM_vJoaFeIUJYtTcFLjUcwpuMCVLy_hXcUGDZePaZK6YbML_grOXpV7spxeYex-Y0JFCuwj7fb91-uDF6Pq0JhxnLKJA1Myxj7jORbQyNmyyJWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2041b839.mp4?token=eiqdI1jWlmOk3-7TwgKEa3R05wIpRmIkTbY79JDOuBEon0sCJfEC7o82d5HMJslH3_zPKp--5e6MCy5eGjid60TxHmfNw9sd7KzcUmQbf2DTpPGtwJrGhUZSJX-CmEZcLpO2UgAwXbKjZWzaD5F8S9XJrBFlyt5KYDOSu3SlGL2GfeyQbYRp8C28kLGhktbGZiwnkGfPFsRQqkFykhpBrNjalCbBM8aTx88IvJ1bM_vJoaFeIUJYtTcFLjUcwpuMCVLy_hXcUGDZePaZK6YbML_grOXpV7spxeYex-Y0JFCuwj7fb91-uDF6Pq0JhxnLKJA1Myxj7jORbQyNmyyJWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای ارتش اسرائیل: در حملات جداگانه‌ای در نوار غزه، یک فرمانده حماس و سه عضو دیگر این گروه را کشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://telegram.me/alonews/134021" target="_blank">📅 12:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134020">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
داریوش فرضیایی» مجری و برنامه‌ساز شناخته‌شده تلویزیون که سال‌ها با نام «عمو پورنگ» در میان مخاطبان شناخته می‌شود، در غم از دست دادن مادر خود عزادار شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://telegram.me/alonews/134020" target="_blank">📅 12:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134019">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffac33808d.mp4?token=LJwz1-OliN2WFuxL6iMyJ53gxqFQT1mcV1IdA7ceELXgX3IfpbCYgm19b_ER2dIL31TuD94pr0miMLjxB13aRIvRIuVAsnoQg_olX_vyhZypejXk6nUxMcCx4644qEm_PNGvVrmOzLhVajG3ZKRzL1vnuKVwxZNvJhLUUN2keBSoarLYouvEE_hmtt8zq2sQjmpC7Si2R2bMNg5l_-sz3vlhQpCrs9Wp9D5fSrDKaVVh2w5tf089x22oveLKPfJXQZYUzEp_nnFFg0ZJjR7n1zoY8hClqdvyuI8KhUUj4aDtZsVyXeGfNGwIFJEXABuVRVPH8_1dJ7ROzI-zcxkGo4DV_VVeCFY0CSoP9iuEnPuXdV1bAfJhpWjWQfgEtQ9baGH2_E9TYorp3obFwQwQC_8qaDB9KWBVDjoYI0xk5KQnCCJ4Nwh2jGZXrIOVjf3WoWN_JswLJSZsRpWIqtJA75_cPQhP6IQpTr3uaRU345KBwiyRkvzgUJKmbWYcXKdhHi1Dz3_l4fptDOSyyutOx1Lh76oizmFz1sfJptDIQtfA48c37Z5hC2J6U_MA56LsmFaokTKdpllFJT3-TRhPqj42oaKpVVmSj-qY4IannChH7ra8xLW1FWIbCVK2FEb1D86Gz8KHdeHZnZLQGodNG6iRUS8fK6OzIvsA6lHeriE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffac33808d.mp4?token=LJwz1-OliN2WFuxL6iMyJ53gxqFQT1mcV1IdA7ceELXgX3IfpbCYgm19b_ER2dIL31TuD94pr0miMLjxB13aRIvRIuVAsnoQg_olX_vyhZypejXk6nUxMcCx4644qEm_PNGvVrmOzLhVajG3ZKRzL1vnuKVwxZNvJhLUUN2keBSoarLYouvEE_hmtt8zq2sQjmpC7Si2R2bMNg5l_-sz3vlhQpCrs9Wp9D5fSrDKaVVh2w5tf089x22oveLKPfJXQZYUzEp_nnFFg0ZJjR7n1zoY8hClqdvyuI8KhUUj4aDtZsVyXeGfNGwIFJEXABuVRVPH8_1dJ7ROzI-zcxkGo4DV_VVeCFY0CSoP9iuEnPuXdV1bAfJhpWjWQfgEtQ9baGH2_E9TYorp3obFwQwQC_8qaDB9KWBVDjoYI0xk5KQnCCJ4Nwh2jGZXrIOVjf3WoWN_JswLJSZsRpWIqtJA75_cPQhP6IQpTr3uaRU345KBwiyRkvzgUJKmbWYcXKdhHi1Dz3_l4fptDOSyyutOx1Lh76oizmFz1sfJptDIQtfA48c37Z5hC2J6U_MA56LsmFaokTKdpllFJT3-TRhPqj42oaKpVVmSj-qY4IannChH7ra8xLW1FWIbCVK2FEb1D86Gz8KHdeHZnZLQGodNG6iRUS8fK6OzIvsA6lHeriE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئو از شلیک موشک‌های سپاه به پایگاه‌های آمریکا تو منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://telegram.me/alonews/134019" target="_blank">📅 12:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bunWOpTSxVjKphnf-HH7OAuvHjpnsGHa-19jq2HNau1CViC5T3FUi-EcWdZyo4kPpw8oH2Yn9nCBS1k5qcVzI7WM2hJ5gE3PzQNyIcQmLzUeWXczk6BtRTFd5hSsCtd1Al7Asi-yJ3sZXK1Y_KLPZ488Zaf1NARAblycpBd-Yc9M5gcTkTca6Yf5GLqz85GPjc2tA2c8y4nr3g6qCq1Q94Gxu5ahU-KjTsF6jLUxmyP2XxKTSOo1uJJnG5MVUGjLVB-bb1ZZ4T2Me8huKww8XUmheEMCk9GwTwhnrtnQrJFjPze5uuKxd9ykiNTvsGhD9dBu4j_Pi2q6316HZIo8bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۸۶.۵۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://telegram.me/alonews/134018" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ایندیپندنت کیف: وزارت دفاع امارات مدعی شد که موشک‌های کروز ایران که به دو نفتکش اماراتی در تنگه هرمز حمله کردند منجر به کشته شدن یک خدمه و زخمی شدن هشت نفر، از جمله دو اوکراینی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://telegram.me/alonews/134017" target="_blank">📅 11:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMjhJCRlJN1wIz8LOZxY9sXoWeRCuk0uwsNuYvN0Fk6kJX2ZUyqHn6j_i7mwS3wiAg7mioNxUNM-BKUO7aebMWV7BgtBG_1Uib2k87V4S0GQozMGDK00GGxjbBukaS5FDzsLMNB44miJghhBR5uNw-skj6PzbvTyO76eSIDf11kc2ywgQnTXvnGpjaN2SUhEz-KWifG5jX2eYSx1iEda7dAsLx-sYZQ2KgzKGCaVBmBLpMm2uK6fQonKwC1OgqJGycTm4ekUv1w78sgVr9eusCWHR1iPXrJvl2fmO8dOQVf9w_vWcyw2OjZB1b91lMOBGlXLAbNemfGqIdizpN492A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سیستم ردیابی هشدار قرمز لبنان نشان می‌دهد که فعالیت گسترده پهپادهای اسرائیلی بر فراز مناطق جنوبی حومه بیروت (دهیه) وجود دارد. هشدارهای متعددی در مناطق غوبری، برج البراجنه و برج حمود متمرکز شده‌اند، و همچنین فعالیت‌هایی در نزدیکی شهر زحله در دره بقاع گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://telegram.me/alonews/134016" target="_blank">📅 11:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نبویان و ابراهیم رضایی از هیئت رئیسه کمیسیون امنیت ملی مجلس کنار گذاشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://telegram.me/alonews/134015" target="_blank">📅 11:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک دادگاه عراقی، ۱۸ نفر را به دلیل تبلیغ حزب بعث ممنوع، در شبکه‌های اجتماعی، به سه سال حبس محکوم کرد. این حکم بر اساس ماده ۱۰ قانون شماره ۳۲ سال ۲۰۱۶ صادر شده است که فعالیت این حزب و سایر گروه‌های افراطی را ممنوع می‌داند. این خبر توسط رسانه‌های دولتی اعلام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://telegram.me/alonews/134014" target="_blank">📅 11:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0db543ef.mp4?token=tM3ZjbArqr-BLKf5Rhk_SEu6S58GwKkBJBaaHoxDKTgzwuHaWKQXC5mZKoJO7TF0DkXs15yyTlD_1pUZo8B9teItaa9TuKbwe9uT1qPWt3PnFh4ccsEECrG7vxV_YgJsQ7qKKZEnol9afKkkDoj9W-o3HuT7FvEiczjFS4HAFFfAXadsNl_26XwWWYtViCZFGldb-5iU41hGmgOU1KQeV_fXfCkEyiQWfrBfpVURk-RvzjE46gqy-JRJpwo9cgTh3DKPI3dQdBEkAzwwynUJcf5rgKdnWPYWwz815Q9t8Wtw-kKbvxAqXGX_8A417X_CSWypFIBPxFuRwfO5VBvhGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0db543ef.mp4?token=tM3ZjbArqr-BLKf5Rhk_SEu6S58GwKkBJBaaHoxDKTgzwuHaWKQXC5mZKoJO7TF0DkXs15yyTlD_1pUZo8B9teItaa9TuKbwe9uT1qPWt3PnFh4ccsEECrG7vxV_YgJsQ7qKKZEnol9afKkkDoj9W-o3HuT7FvEiczjFS4HAFFfAXadsNl_26XwWWYtViCZFGldb-5iU41hGmgOU1KQeV_fXfCkEyiQWfrBfpVURk-RvzjE46gqy-JRJpwo9cgTh3DKPI3dQdBEkAzwwynUJcf5rgKdnWPYWwz815Q9t8Wtw-kKbvxAqXGX_8A417X_CSWypFIBPxFuRwfO5VBvhGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آتش‌سوزی گسترده در محوطه نگهداری کانتینرهای بندر بیروت رخ داد و ستون‌های عظیمی از دود سیاه را به آسمان پایتخت فرستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://telegram.me/alonews/134013" target="_blank">📅 11:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQRSG-YDEDSfgYQ2rrjK-gbUsyArOVbbzuxre2i0kVyqQ9Oq22Iy3KOHaw-s-m0gkYt19QmWBW4uphHx5j4HFEJsNWhIwntOT1kFJVmMa5GwW1sDImnYZbbBNrQMk4ajMl0RB6wQldX968EoYr5hRdSJJX4ZlYauPtT9l8AACFCT6BWJTzukjtIAp9BThmmxTTmVPCQDIcY1fXHZ8g9W3Ebhtn2UuyUqQDOCN1acZGcBOtDa3WV6bm3JFo5mvMEswekkvFR5he8URvdk4pJvmPO12cO4YgLF0scIA2ynb6RZIuqNFNreqpak985bCyKX8-prdgGkZDDVUvA7A3u18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیلی تصویری از یک خودروی نظامی را منتشر کردند که در جریان جنگ، توسط یک پهپاد انتحاری حزب‌الله در منطقه‌ای در امتداد مرز لبنان تخریب شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://telegram.me/alonews/134012" target="_blank">📅 11:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
چین: درباره از سرگیری درگیری‌ها بین آمریکا و ایران نگران هستیم
🔴
به تلاش‌ برای کاهش تنش‌ها ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://telegram.me/alonews/134011" target="_blank">📅 11:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idvuh2KqkCZPZlwByOURGhMnxNWjq2GdpaGlSzh9UX7W9Uybg0oJ9Mn0uqo5iVLpfuL9fytzREYnTWzETMDiSngaE5zooootVJWO56Jex0ie7Rx8oPHfCw-uCfzFhBKI666nSnKGRM46d1WenbHepBPZSe6KGk30lG6eQejVz-FPkhZaT5-trsFkuk-gxDSyelgIKMXZuDVZnrtMfPpq6y4WSF_fV6Ucjr-rjy93HgHElnQ583hifCL_3yZqidedygEhusnGyDX600FuNspWuqAHcXLPckB7oYSe-VkaaW9QLovbzLgpmcrHF6Q2cVGm2HMMvDgG_Ab7X7z4tbrnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از نقاطی که دیشب توسط آمریکا مورد هدف قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://telegram.me/alonews/134010" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNnCLGZzEZEIoXLw1BUEk4F8JT0geKBeyvoeHuMzBlWbwmtO_pJ6GQBrnOk-5N0iM4pKlIL3prepzFDL6JBe987fLmYvcHbZ2RZTknHFSFcU4_dEiShKEmW2YF_n9_vQd2_-kdq6DqvkDn63m77n93Hf77QatfLgw8kfc7WwNKJrIFi1Kd81dOo0xZBHv0M-aOTk1G296QVBQv9Hm06nTlXKmY23Qgns3gZ8_64zCsn63Ku1y5E-WwEvKl_LzxBpfgA17zfaFyDObJR-5a6eKaFAgJepQKbpoZl4R3dBhnZYvLflLjWlqL8JKCz1xLfWqbKfuHImKRbLYAay6TCNdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مسیر حرکت شناور انتحاری آمریکایی و ورود به منطقه نظامی
🔴
شناور انتحاری آمریکا بدون هیچ مشکلی و براحتی وارد اسکله نظامی سپاه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://telegram.me/alonews/134009" target="_blank">📅 11:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhfH0Oh4QZ7l1_KMfieEUIYccFbRiLyauu5UbGCtcJE-r9STejsAFlVZ4vLeXtBK5ZX3w2Amdk4-P-cNTn3w6qhwT9N5E0ejFgpRKl2L37adaZHGj1XsK7y42-WhYEbk2V8bOPWwkY63ZKzn0b6M_fdlm4Xr9-05o82vBKJ6NLNBLj3b1bjkCnLi5p_XAFOn1OwhZ-fw2EDFJa7LQgc2J-qk8hHSGrDkCpG8Ng1cSGBZmYxcIgzUv_H1o2Yka67sboeZc4VN8GIiPinWHSJYtHv_mbj1Uzpr3cwtjp9rkEQ1UF-OLXmlM_iW01Jp6OV3ugt715EYz_jqdgeGnY02gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
الونیوز پول میگیره تا منو خراب کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://telegram.me/alonews/134008" target="_blank">📅 11:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134007">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رئیس جمهور لبنان: حملات به عربستان سعودی، اردن و کشورهای خلیج فارس با هدف تضعیف ثبات کل منطقه انجام می‌شود
🔴
هرگونه تجاوز به حاکمیت برادران عرب ما، تجاوز به اصل لبنان و جهان عرب است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://telegram.me/alonews/134007" target="_blank">📅 11:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JvCvUMfPUfQSwx72w5YtuNop39zatkZJk4qNwSr-2H8TwjfCh8jcYNcjSzDI-gzSaXrXCUZnVryX9RoLieW1b7Xd8VLK0pmqI6NOoT-KTHIHg3UfpdTGRzTXT_kU63SadcbRqf1cudGglDGsEPsC4gdIw7kKu-rMEC4s6VFaEgzqNJOVfof2jM6fs_RirtV5DYxa6Z7dDSumz7NjsUmizKwCM6gMxmdrkNBSSDnMJpjAALrBWylBxTbwiSGOBGhEXE31FuiS3JuIMUwQ0HLnZH1O_cH-imTy6nB4-mjvybfD0iMHPxrndCuIIPCxppm4AeKgXOAVXdTTAvbFOylRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dtwvGXrJn1ttzgcITwzOiMsLKZcYW1fDvthG_1LllQtW7R8lCG4XMsYIagNfbGNZTRUHFs0-UmnFIilapaw-5qALQgiRieC88z9FKtjEA1tW_XmxkS9J5nVozac0Nf4KE0DNaChyYIJuLQzHwPLr2GmR4_GArbVph4xzmTBUKgzT07cPJgIeHnwfQVWO8qP8hYzc-kl1BLFgcDKw90Pr2GyfvfZASBTtXItz55kb0fGBYXzaqIEaUx9Jc06yXHPe4Eu1AKDFeTV2O6blvVA3S6El0gHnZ-lPM-3Uv7tbL0kVXCzC_vlfV7at0cbCxy0tVMyPumpgAI79-vUUAZ96QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله آمریکا به رادار AN/MPQ-55 با قابلیت اسکن مداوم که به طور محلی با نام جویا شناخته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://telegram.me/alonews/134005" target="_blank">📅 11:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp-csJnB1oZ7TMT5Q2uF-OsAhv4i2-f0xFDT2EvEObC_wYm3LV4BfZfp6SE2Smb8QYwMeUIecPZt9sPPQx6LFCVjIfZTpBYXcp0fSThgPEdbxS3Iv2P5msYxO51jcHc4geQFLfw36rGabIN3eDC6NJnHZN0506GHpiftEdbw4XWfSQBWLvDy3Hf3fnhoLPFIqjFg4wevzeeoLZjvEBHl_FaJf6tBL_8sO7lygM5sQVGGyq04Mmb6m8je2MlLrc9Nq2idUS21Diq3w5zfpxs9q_euOWX-yRyJhTcxlSeI_g0t1DyBqL_Fs6eEQXdMw8EBJ6QE95kmcvPUpFuiz283NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا: گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
🔴
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://telegram.me/alonews/134004" target="_blank">📅 11:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134003">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733e135f00.mp4?token=qLJCv8Tz7BPxW_ZxgxmBx0GSYe6vMot18XI4iF3djPn_uevNqtSP4HLDwU0AsQRmK9uT6mrUB02LYLXIGFj0IxonFpSIp38VcLQexQ7GE73fNfRr79SnKlCldMRvf-dgWEr2xkXux9wcIP68Wa3iVi4c0jyYwln-8Ma5meHxBCfHusvIa4m0EHgkoesQHYiV3fe70pk2TGJT1XYzg7xjEKQeJb2HLWP6X5LpZgJeErcEEa_DL3W3SySI7PFMLDHDnCp2oreEyZEXlt0wbveYGIdLTlsb9ZhIs5vmgNzWm0dMk4hnH2zn-ZY156OaP3V6j9-mc7GXBGE0MowofOdogg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733e135f00.mp4?token=qLJCv8Tz7BPxW_ZxgxmBx0GSYe6vMot18XI4iF3djPn_uevNqtSP4HLDwU0AsQRmK9uT6mrUB02LYLXIGFj0IxonFpSIp38VcLQexQ7GE73fNfRr79SnKlCldMRvf-dgWEr2xkXux9wcIP68Wa3iVi4c0jyYwln-8Ma5meHxBCfHusvIa4m0EHgkoesQHYiV3fe70pk2TGJT1XYzg7xjEKQeJb2HLWP6X5LpZgJeErcEEa_DL3W3SySI7PFMLDHDnCp2oreEyZEXlt0wbveYGIdLTlsb9ZhIs5vmgNzWm0dMk4hnH2zn-ZY156OaP3V6j9-mc7GXBGE0MowofOdogg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پالایشگاه دیگر روسیه هدف قرار گرفت
🔴
پهپادها به یک پالایشگاه نفتی در شهر سالاوات در جمهوری باشقیرستان روسیه حمله کردند و دودی از این تأسیسات به هوا برخاست.
🔴
طبق گزارش رسانه‌های اوکراینی، این پالایشگاه نفتی تقریباً ۱۴۰۰ کیلومتر از خط مقدم جنگ، فاصله دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://telegram.me/alonews/134003" target="_blank">📅 10:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e8bc26f53.mp4?token=AkIWyoYKPdk8u6MdIUWThJ2WN9IYdQF0yW_zu8giC9LxMZgbdsxggKys6t5aUi6rbKioG97-t5WngilcEZt1Jilv66Ubldf6XVLYFofIrvQHSiYP9TiuYj_c6objZKh7ct9Qtp48s11X1-2o6AoEWc97JFHiY4ekXJ2agF-8pCpS0hgfMSLnUwg_emcUno-GziKtp95LlAsGDEy4ytyMyZDNh6IsmBxp0ougg5tz51BZICMHKS7G05pLtq5sYiCVQDsa-1wlsGPDkLBPG7cht03vdfbLZ_d-eC7s-ym0zUHyw2573YSST0sa3Uf73ubQBAmJ5Mlv9QdcR8VbnSvATw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e8bc26f53.mp4?token=AkIWyoYKPdk8u6MdIUWThJ2WN9IYdQF0yW_zu8giC9LxMZgbdsxggKys6t5aUi6rbKioG97-t5WngilcEZt1Jilv66Ubldf6XVLYFofIrvQHSiYP9TiuYj_c6objZKh7ct9Qtp48s11X1-2o6AoEWc97JFHiY4ekXJ2agF-8pCpS0hgfMSLnUwg_emcUno-GziKtp95LlAsGDEy4ytyMyZDNh6IsmBxp0ougg5tz51BZICMHKS7G05pLtq5sYiCVQDsa-1wlsGPDkLBPG7cht03vdfbLZ_d-eC7s-ym0zUHyw2573YSST0sa3Uf73ubQBAmJ5Mlv9QdcR8VbnSvATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خلبان پرواز یمن: هر خلبان دیگری هم بود همین کار را می‌کرد؛ ما فقط خوشحالیم که پرچم را بالا نگه داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://telegram.me/alonews/134002" target="_blank">📅 10:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e48bf79671.mp4?token=HyMrZNx-u-urxyocDfOqyF143qZFtALYMWF9vpBm2B9U1YzK0PyAdI13b4LsycKHMyM6Er1FSDqX9ZtymPTILVZMwRvk6See990JDtF4ZDdjK1eYYhHUKYe18kYrXbVYa-i3qLWdRZcy9LC3u7A9aNr3s40XvPBPDD8PJBc-kRf4FWWkF_ewX1qWqsmcVDZHXnUJdkFk7zpNrbzpBeTdAA-sIXelyAEqdtLehiIOgsjRmSfjPyA6G0mbPAhJ7uqLySuKicTwF5W3Jx7MavVdp11BMvbeq8a3RWpN31OIsgMlqcQAW-S2abk39tcHpscqMqf7wlvZ48dxThp_P5lxHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e48bf79671.mp4?token=HyMrZNx-u-urxyocDfOqyF143qZFtALYMWF9vpBm2B9U1YzK0PyAdI13b4LsycKHMyM6Er1FSDqX9ZtymPTILVZMwRvk6See990JDtF4ZDdjK1eYYhHUKYe18kYrXbVYa-i3qLWdRZcy9LC3u7A9aNr3s40XvPBPDD8PJBc-kRf4FWWkF_ewX1qWqsmcVDZHXnUJdkFk7zpNrbzpBeTdAA-sIXelyAEqdtLehiIOgsjRmSfjPyA6G0mbPAhJ7uqLySuKicTwF5W3Jx7MavVdp11BMvbeq8a3RWpN31OIsgMlqcQAW-S2abk39tcHpscqMqf7wlvZ48dxThp_P5lxHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از ساعاتی پیش، آتش‌سوزی گسترده‌ای در محوطه کانتینرهای بندر بیروت در لبنان رخ داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://telegram.me/alonews/134001" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: تماشای ویرانی غزه، حس خوبی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://telegram.me/alonews/134000" target="_blank">📅 10:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
علی بابایی کارنامی با رأی اعضای کمیسیون اجتماعی مجلس، بار دیگر به‌عنوان رئیس این کمیسیون انتخاب شد.
🔴
موسی احمدی با رأی اعضای کمیسیون انرژی مجلس، در سمت ریاست این کمیسیون ابقا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://telegram.me/alonews/133999" target="_blank">📅 10:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ابراهیم عزیزی با رأی اعضای کمیسیون امنیت ملی و سیاست خارجی مجلس، به ریاست این کمیسیون انتخاب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://telegram.me/alonews/133998" target="_blank">📅 10:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133997">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=KKQ0zLvky4A9njb3Jl4gyBZYTG_nlDEuIfJ-9_jple74ZKa5ZC0SIWIxLiuq8axgfbToBqvA2hlkH8_MAhhvgZZpZyUMaLndTMi-vc33FhxVUQyDEOePKKcoP0fG7COrUf3h-pxCqhu0nwAZ9Sa-D9mSGv10GYuWUCa7IKMQ2RaC2VS_HHMLSNWz2RNp76bivLL40nuisV0GHVQCC4on4FaHp9eR4aqUWi7o2HVniKJ0LpBmmWCbx9ftWbMm-IiORDH83bcYoFnSq0a4l8Dy4a9XgPahUx2iuJHKFqKeb71IP9_w6qEnrg4ZGPNdLXbjZdMgk4umtK-DhANdt_ANwg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57cf9a082f.mp4?token=KKQ0zLvky4A9njb3Jl4gyBZYTG_nlDEuIfJ-9_jple74ZKa5ZC0SIWIxLiuq8axgfbToBqvA2hlkH8_MAhhvgZZpZyUMaLndTMi-vc33FhxVUQyDEOePKKcoP0fG7COrUf3h-pxCqhu0nwAZ9Sa-D9mSGv10GYuWUCa7IKMQ2RaC2VS_HHMLSNWz2RNp76bivLL40nuisV0GHVQCC4on4FaHp9eR4aqUWi7o2HVniKJ0LpBmmWCbx9ftWbMm-IiORDH83bcYoFnSq0a4l8Dy4a9XgPahUx2iuJHKFqKeb71IP9_w6qEnrg4ZGPNdLXbjZdMgk4umtK-DhANdt_ANwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسخ چمران به سوالی درباره قطعی برق بدون اطلاع قبلی: اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://telegram.me/alonews/133997" target="_blank">📅 10:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133996">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
منابع خبری لبنان از پرواز پهپادهای ارتش اسرائیل در آسمان ضاحیه جنوبی بیروت با ارتفاع پایین خبر دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://telegram.me/alonews/133996" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133995">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرگزاری یونیوز لبنان گزارش داد که دقایقی پیش، صدای انفجارهای پی‌درپی در بحرین شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://telegram.me/alonews/133995" target="_blank">📅 10:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133994">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نیویورک‌تایمز: هزینه‌‌ای که ترامپ می‌خواهد از کشتی‌های عبوری از تنگه هرمز دریافت کند، می‌تواند هزینه‌ حمل نفت را دو برابر کند
🔴
نیویورک‌تایمز نوشت: هزینه‌ی «بازپرداخت» که رئیس جمهور ترامپ می‌خواهد از کشتی‌های عبوری از تنگه هرمز دریافت کند، می‌تواند هزینه‌ی حمل نفت از طریق این تنگه را دو برابر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://telegram.me/alonews/133994" target="_blank">📅 10:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
منابع اروپایی: اگر آتش‌بس فعلی به‌طور کامل فرو بریزد، بازگشت به میز مذاکره به مراتب سنگین‌تر از امتیازاتی خواهد بود که امروز برای رسیدن به صلح می‌پردازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://telegram.me/alonews/133993" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbGtiB3FWvKYqQp4-mPmnNNUqEV3905SpiTdvHy75CYL4Ex4S20uobwlmZACxNo1Cd4SU7FbL6h3vct0sglj_3lKEuFnsehCyjMT2iQjsUAHjGQJIFiVigrrxULHQvl12J50kovhCmonIW49B678Wif_VrTbssGwNJzS7M3Y1jHQNeKcUwwLMQWUBxCRN08EVd8cI9S0cqImyhXHzF6L9lMEQHobsNJBYgvszHNAr_45rWRMRxjxPO9VFrkJFIxAbZ4_bkdlKiTijNgTOqls-3RLgl70slPYnLip-zPVoo7Vc1C_qZXB_zjVMw9VIE-mD6x9RzkTLqYhwIoGgdLL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIOPG_SXVkGeacrQghPsErdpdUa_O54ys6mzxgMFtsevKHOyNJY19hbZHR9DGGNo5MPBFsl55MioPgRAOGFait3QlBYBsG_6I-FwAqIc5e7xcVhNJ3nGyapF2PIhjc4hmYXLcVyYBeDrwPLa9lZ33t4fHiK6FuEzg3TVDUaPeZZ8pATyr_qyUkuJ6go2bX4-rNrxPb9NUZw3-pEUgrvydZ9oGFG6GIrc5X_dzfNaKzfEEh9D1BLPKeY2PmeU7O-MDAuFvLkr0ug_n-n-kLrm_NhhrGZZhWMs5_ZEGNoBEHFFvLA77V3IyShc3IGfWyV0RyFk8_WLEyLARicY_bhkHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نفتکش‌های اماراتی که هدف حمله قرار گرفته‌اند، از بزرگ‌ترین نفتکش‌های جهان به شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://telegram.me/alonews/133991" target="_blank">📅 10:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133990">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
دقایقی قبل صدای انفجار براثر خنثی سازی در شهر اصفهان شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://telegram.me/alonews/133990" target="_blank">📅 10:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133989">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی و سیاست خارجی مجلس: زمان آن رسیده که ایران بمب هسته‌ای بسازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://telegram.me/alonews/133989" target="_blank">📅 10:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133988">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biTXZdyjahPfirMjEA3xuY3VH7Wz7MDYcEpu88n4jHCPXyRLMX6pHOwK7JhfL_r46MKf8UEbiSePulz2O0Qd207LgPNF5O-Iev18ZkydlnxR67fkIiK_GYqE99ZdERKFdxTCtedK-zIPz6r3KRyRyQzrqa7g7hlGfRSVHPY96ErIffe1HqWEcgZAnDGAVRc3kSPtpw3sShcLSTj3IJn1OibCuu-SEWDmWtiyVoz60Sqwigy0Zq5LMOsYhG3HKgw-FOw7GcyZW2B3cZe6fvmkNacg_zo9UF2i5M25d1Rj-BR-xDYc7AofHA5HgLwK-2KbhAavdUCZUUvikBM4kjcuog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایپا دوباره محصولات خود را گران می‌کند!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://telegram.me/alonews/133988" target="_blank">📅 09:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133987">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atMk9Ed_7MujNSC3gxViu2StoIUUfE8iahcVv7utxsowX6bTohcPodARm9XUKdAMsJlvh2X3K-oryHJm_FpegTzaYDFFt9-QiEPIztdPLAW6vjGsLuY3tz6B-oqGS6qXJv3aasI3pMmXidBK80fkNSB5Jnfkx2MXEQOBx_tETD_SfNrrKBVSi_qlTNuLHugeQsxy1U2xqr_F2sHcxGyL3bvEpooDb8n85GpTpOmmh09kwyI-GTK9dM3NLT5022RITajS63B0FRPTwYjRZ6NMcVZH7vHBvBXhpqJNnLRx9bhqi39iMex7tQ1I2rU54KLLldYOCVyqS1Cm47Pcj06azg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دارلین ، خواهر لیندسی گراهام ، به طور موقت وظایف سناتور ایالت کارولینای جنوبی را تا پایان دوره تصدی در سال 2027 بر عهده خواهد گرفت.
🔴
فرماندار کارولینای جنوبی پس از پیشنهاد ترامپ او را انتخاب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://telegram.me/alonews/133987" target="_blank">📅 09:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133986">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام هندی: فراخوان معاون سفیر ایران در دهلی نو پس از کشته شدن یک ملوان هندی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://telegram.me/alonews/133986" target="_blank">📅 09:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133985">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6paNmvk6A045ULGR94l0xHTx0cg1fu3HZ_G69jZrQXnE6C3GSa4Idh3XdkDGrey-w8fxb26YJ4MYzG8KfPToES-EQXSc4bedRpweeAzTlzVBiodXisxjK1RK0Vn5lv_AFVBGYm669tLPY7zSj5lqybZSAgtxb8ZRB7FD1JdoJND04k59E9OQ92fZ8qmRZ9lllAT6DZadJZKNdG5pouq13CgHNiM3kZXnUPOET65cNM83MIV8OLpU5McE2cX07xyBPJRmblYyinmvq8IPF0b-HK0MobfVPp2QvJn_9qx4MutO9ZhOhzP1taotSHqMOCBNmcGSwL0fHU3rYL8qfQmNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بندر فجیره در امارات که برنامه ریزی شده برای اینکه بزرگترین هاب نفتی امارات شه ، بازم در امنیت کامل نیست ، با اینکه نیازی به عبور از تنگه هرمز ندارن اما بازم در خروجی تنگه قرارمی‌گیره و در تیررس و برد موشک های کروز دریایی و پهپاد ها قرار میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://telegram.me/alonews/133985" target="_blank">📅 09:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133984">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
صادرات ۸۰ میلیون بشکه‌ای نفت ایران در ۲۶ روز
🔴
تانکر ترکرز: در فاصله زمانی بیست و شش روزه از امضای یادداشت تفاهم اسلام‌آباد میان جمهوری اسلامی ایران و  آمریکا، بیش از ۸۰ میلیون بشکه نفت خام و فرآورده‌های نفتی ایران صادر شده است که ارزش کنونی آن بالغ بر ۶ میلیارد دلار برآورد می‌شود.
🔴
در حال حاضر، حدود ۳۰ میلیون بشکه از نفت خام ایران همچنان در انتظار صادرات باقی مانده است.
🔴
در صورت اعمال هرگونه محدودیت بر تولید نفت ایران، ظرفیت ذخیره‌سازی شناور در محدوده جغرافیایی محاصره، بالغ بر ۶۰ میلیون بشکه برآورد می‌شود که می‌تواند به‌عنوان راهکاری موقت در مدیریت عرضه نفت در دستور کار قرار گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://telegram.me/alonews/133984" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO-5T2VDDE4vtTQs66Z9GW8pTa-AQBSfJXB-TmI0JJgXcYUvfHJ_1NTLhWsRjpGUkKa2N0HXgjxD-Aox6Zvu0kRCIkohgyNoO30eNKv6lpB6P28SbkOpoyXiaGrSK_5DoAGX7yikmB-CxTQhoZ21xKXuMr5cR0oc5d_OjtPHhDSjdYFrh363z2pghkD4w4ZZqDP9Pqo4cLErCD7vXhjHdZz1zgpp7_C5mICSL3Gwliq8_tQaaRdRACoQ4MQpaySMKkqw4Aho42kljFO7hOgYxMT-Qrh2FU9cdYwpQgnTEZKZUTiyKpmCi7KfgsscSNxrAeE-4M8H4Vkr-M37sMaynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: باید باب المندب را ببندیم.
🔴
موشک‌های ایران برای بستن این تنگه توان دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://telegram.me/alonews/133983" target="_blank">📅 09:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: بیش از ۵۰ هزار نیروی آمریکایی در سراسر خاورمیانه مستقر هستند
🔴
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که تعداد نیروهای آمریکایی مستقر در خاورمیانه از ۵۰ هزار نفر فراتر رفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://telegram.me/alonews/133982" target="_blank">📅 09:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133980">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4abef50eae.mp4?token=gLJcLMXEqKKi91fsu98ofA-4r1XZ_DMWQvY_NdTmjw9VFIjona6ZJOcv7_mPa5iwcPvl9RjqjudW642qUIo-9ok4PE-otBocOAsYvIVmbbwwkzL4O3T379Wpz51N8rUKYFsIDw4f8iN4SUxtQrOFDfu1edsZ89NmncBmFnMdQWCNnUSVjExVGK32mggvDhfpTFTIvTYJ72zQplIXiMMZpfedTrWg9Qfoh1mZfwiUBwJ58lYbfbCxS6PI850XBW8VteJgcS3yrIPyXPFse_ixpPYvJTYaQnxnK_dh_iUUdR27SGFvcsrJ3HacBIji1a-DyYaDem2NdTgGF7SgFbbIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4abef50eae.mp4?token=gLJcLMXEqKKi91fsu98ofA-4r1XZ_DMWQvY_NdTmjw9VFIjona6ZJOcv7_mPa5iwcPvl9RjqjudW642qUIo-9ok4PE-otBocOAsYvIVmbbwwkzL4O3T379Wpz51N8rUKYFsIDw4f8iN4SUxtQrOFDfu1edsZ89NmncBmFnMdQWCNnUSVjExVGK32mggvDhfpTFTIvTYJ72zQplIXiMMZpfedTrWg9Qfoh1mZfwiUBwJ58lYbfbCxS6PI850XBW8VteJgcS3yrIPyXPFse_ixpPYvJTYaQnxnK_dh_iUUdR27SGFvcsrJ3HacBIji1a-DyYaDem2NdTgGF7SgFbbIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم هایی از  حمله دیشب آمریکا به سراوان در استان سیستان و بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://telegram.me/alonews/133980" target="_blank">📅 09:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133979">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01790095ff.mp4?token=X5-_PErT7ae0j2zehk8TjV-FdU_HqsZyMWHIN2ElarZYB2HAQiGDh-2HSezlkwTHLV1kzFfpQqYpAB1bJSzbHLspZfDSZGtJ7_6NWWg6yaTY3gi-1eW4cq_mvtQHluMa6N1CtOHZwWeaJZX1BIUDoyDIjvnWDJzo3z3BX9MWAWSZhdGIL_nOtoU8MyNJjIR7PQ2M4H6B7-Db0UufF4I400xbuK56yMJ8F-mDTZAkbXldT-bn0XZU8SxCTuY0867A_y_knan38Obx0wGbawJd5MFMZO8eRYALcvmfEaB_bQvMviSAkgEUBpNwwz3lewMKbma9ORtLaYNphJ-fUTRWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01790095ff.mp4?token=X5-_PErT7ae0j2zehk8TjV-FdU_HqsZyMWHIN2ElarZYB2HAQiGDh-2HSezlkwTHLV1kzFfpQqYpAB1bJSzbHLspZfDSZGtJ7_6NWWg6yaTY3gi-1eW4cq_mvtQHluMa6N1CtOHZwWeaJZX1BIUDoyDIjvnWDJzo3z3BX9MWAWSZhdGIL_nOtoU8MyNJjIR7PQ2M4H6B7-Db0UufF4I400xbuK56yMJ8F-mDTZAkbXldT-bn0XZU8SxCTuY0867A_y_knan38Obx0wGbawJd5MFMZO8eRYALcvmfEaB_bQvMviSAkgEUBpNwwz3lewMKbma9ORtLaYNphJ-fUTRWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخاستن ستون‌های دود از منامه پایتخت بحرين
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://telegram.me/alonews/133979" target="_blank">📅 09:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رئیس‌جمهور برزیل: تصمیم آمریکا برای اخذ عوارض از کشتی‌های عبوری از تنگه هرمز، «دزدی دریایی» است.
🔴
ما ضمن مخالفت با حمله آمریکا به ایران، هشدار می‌دهیم که هزینه‌های این جنگ مستقیماً بر قیمت کالاهای اساسی و مواد غذایی تأثیر می‌گذارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://telegram.me/alonews/133978" target="_blank">📅 09:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133977">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1925a53a.mp4?token=VvPzkvepW6-odAzan7HHOI5mstHJwWoucjKnykxpRtcGUo6o_TmFzoYc5rE2gJms7F5SBoohSNkdUVLE0Rmvfk_R5dW2yzTHejStYTRvj9F2gaRjKhRI2oKjfjB-NE8JsjT-w90wWtDrqnEcmlOVaAT2kqTJJAFkldpkh-SYfco42Nnb08CvxzK9LUPRRlRR8_XI2hXZA8bKXwvjWr4Hq4sQll3CCfscBg-MdrJx5wz2B8m-L8G9tWPpADugm6zR8ObYs3r_sMt3H8zVoydFxavFEbJ3Ui65LSbUDO8ZBiZqeniEQvKPXzzdbsvEA5IbiSkhamjSM_fOBjssgMSqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1925a53a.mp4?token=VvPzkvepW6-odAzan7HHOI5mstHJwWoucjKnykxpRtcGUo6o_TmFzoYc5rE2gJms7F5SBoohSNkdUVLE0Rmvfk_R5dW2yzTHejStYTRvj9F2gaRjKhRI2oKjfjB-NE8JsjT-w90wWtDrqnEcmlOVaAT2kqTJJAFkldpkh-SYfco42Nnb08CvxzK9LUPRRlRR8_XI2hXZA8bKXwvjWr4Hq4sQll3CCfscBg-MdrJx5wz2B8m-L8G9tWPpADugm6zR8ObYs3r_sMt3H8zVoydFxavFEbJ3Ui65LSbUDO8ZBiZqeniEQvKPXzzdbsvEA5IbiSkhamjSM_fOBjssgMSqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ازسرگیری شهرک‌سازی‌های اسرائیل در شهرک «گانیم» در شمال سامره (منطقهٔ کرانهٔ باختری)، ۲۰ سال پس از تخلیهٔ آن
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://telegram.me/alonews/133977" target="_blank">📅 09:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133976">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سپاه: تو حملات دیشب، رادار پاتریوت، رادار کنترل هوایی ناوگان پنجم دریایی ارتش آمریکا و یک سامانه راداری اخطار اولیه c-ram منهدم شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://telegram.me/alonews/133976" target="_blank">📅 09:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133975">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3uwCKn58PiWkvgE0H0Jx0BKg0X4ZJoXzGOozEXE28cl-zCOiyhmokqR83QX3sgspSfGxPERvSV_0Oik3KkmB2xkerpo_KJPt8HuUUhqbadMCGoUkaD-HfeelX47yzlQvbE2jyyG8ozlp0m7GNlMzSj4MXQj4LM6sh-ZuIbbkzef4kJo2vL1vq-CFFoafbx06y8QeEG4bIyM6EqgHfjwT5ZEU1Vw_Wimqj7X6zxBOR0La7PlPgbZe0texT9lolAPpYi-WqNv3XbPAdx_wg9PVUOaCjmp3r0a8GjnaW0jqg8NN1KnR-MWtsS_jHKYJDD8ejpc-6emzH8hxHzKc5Vwbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۸۴.۹۶ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://telegram.me/alonews/133975" target="_blank">📅 09:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133974">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqHGGNMJTIPhxvpbqTNZph30OCrf7Mi96R0aWh83EolcFrGnZUxaLxhbQyoJ1AVbKpV8O3fpboGxEB3aSuI0GKONcVvw8L7ylpn2LzmaVgGvmPCEFYyBT_VakL1ztAW3qTaDQn6_LFoC_J6iK-JkrGO5sxWgfN4EpBM3HzAEEQxo5-ATSOM04bt-sezoLZSuMhJwYkRlPZq7NVgAxu4fYlpcHxH6Hdv9FfyeG8bCXhy4g_Qd88Eg5E2Gt5_aSIpni45Cq8wmJfH8GHxjpj5CKskKBwwf0ormS6_bn08BI_lNZxH68MtSHrsvf4VPf_xRina_vKc8seUHjdmYKlEW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جزئیات قانون مجلس برای مدیریت تنگه هرمز از زبان رئیس کمیسیون امنیت ملی
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://telegram.me/alonews/133974" target="_blank">📅 09:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133973">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfBBbxUXCoM1GWD0jPEDKDS7rrVwiKmy3vOL-7156W8i-xuuQSC1pejQrGRpaQphwz_Ut01cZFyZB0iE_GMAsQaw-r_ZDacVoBQ2S0Ta6rlTInRjSj84ebBaFqqhMIAMabTvtGgkouiU78vChcQAi26eljJ-1BMY2FFEJAK1S7j9gQQeG8hU25ooJCEr1UBbGk-COe6Zj5ruZ5lyQo6Q-WsNmtxURRlb5q4S3BvnKvOIA38pZYpA5iigH-AkOKA_7-wVeh4tkyqhjtaiOC7AieUIowDP0TGVxQCBq9TTUsI4ZCP8tZvfN6nHbQAVOP7bax5ZOpiB7np9VBIPWoyLxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
وزارت خارجه امارات: دو کشتی تجاری در گذرگاه جنوبی تنگه هرمز در آب‌های عمان هدف دو موشک قرار گرفتند/ ما حق کامل خود را برای پاسخ به این تنش‌زایی و اتخاذ تمامی اقدامات لازم برای حفاظت از سرزمین‌مان محفوظ می‌داریم
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://telegram.me/alonews/133973" target="_blank">📅 09:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133972">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176277bebb.mp4?token=uOCEj_G08C9fUQG0i5PWlBfKl-Opv0y8cXSudGn5hZcGRVCELZAf8GW116kYwB54qYwKIHy-s9zGrXDNwnEvyuf2PJLfPiHxg-wHclV9TExUkT3v7jDPdJQoRlZxNbNffSouCTCl9gf_UhyJImG72XNbRMNdAT3rmWUmrs8lk6JnpL63hpYLnRJcBPXuVjuy34rHnbkFWZqJGO_Ja7V0b1VHKtUmT8POz5X-Ewh6MY7a4kIN6WFm3rO-T4f5hG-Kp9k9Q3ky8wMYt-mAppYW55LF_JW4NbnMfdpgJEXRj114UYSYZVT6KcyDJwdyHhfAVef8NRf3hBEIzaB3mlCKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176277bebb.mp4?token=uOCEj_G08C9fUQG0i5PWlBfKl-Opv0y8cXSudGn5hZcGRVCELZAf8GW116kYwB54qYwKIHy-s9zGrXDNwnEvyuf2PJLfPiHxg-wHclV9TExUkT3v7jDPdJQoRlZxNbNffSouCTCl9gf_UhyJImG72XNbRMNdAT3rmWUmrs8lk6JnpL63hpYLnRJcBPXuVjuy34rHnbkFWZqJGO_Ja7V0b1VHKtUmT8POz5X-Ewh6MY7a4kIN6WFm3rO-T4f5hG-Kp9k9Q3ky8wMYt-mAppYW55LF_JW4NbnMfdpgJEXRj114UYSYZVT6KcyDJwdyHhfAVef8NRf3hBEIzaB3mlCKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل اولین فروند از شش فروند هواپیمای تانکر سوخترسان مدل KC-46A را از ایالات متحده دریافت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://telegram.me/alonews/133972" target="_blank">📅 08:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133971">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV1rqynS24FVKzzo9zZWo6Y0zd8GGFOMPlKEjvw41fB0OuHvy8Xf7HeYVGZyKnsBt_6YIj9oNeMOYwXXR9MFv6c9WBSGb30WZlhQI11Jsk0A6_vT1psnl6bBIJGpLv_hRKPRaIvah9e4juPM5RZrhlArgNrmedgZxZCn3kWWFilreOZMCq2oM4UsOjkLYOLNkWqcJLZ1H_Y61CZSugt56tlo4ymRVY2HWJ-7BpTxtcEg_LEW-OlF2wKnaf2iVmyCdf6ftsOba8o_sEEXt2gmvDLVa7_5PqyrTX6aTpXBrrm6mvyAjGpp-yxs7t3Kq2_ingIyAKav9g3PFvu661YaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اردن: چهار موشک شلیک‌شده از ایران را رهگیری و منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://telegram.me/alonews/133971" target="_blank">📅 08:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133970">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بلومبرگ: توقف تقریباً کامل تردد کشتی‌ها در تنگه هرمز
🔴
خبرگزاری بلومبرگ به نقل از داده‌های ردیابی کشتی‌ها گزارش داد که تردد دریایی در تنگه هرمز از ساعات اولیه بامداد امروز (سه‌شنبه) تقریباً به طور کامل متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://telegram.me/alonews/133970" target="_blank">📅 08:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133969">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e64406e83.mp4?token=dH8cJIk2JnyqOmL9cu-TIBRKOGGqNfl4NqIIXnlXQDa5L_2hNJSJiCD7RPweq9bX3lcL4-P5iknKqHsEX2Y0w6-VKgF77PAUbwN7QCPXR5XD4yNFwQuo0qW3_SKojR-9HmdD3GLT-dEG00oqqfShQvKd_dG08WNrBzFb4sJH5JdGqiEnOlvE4d9H4uPAQ54sqnYi9PpwVzRm7W22_Ru_KCdx33UlzPsMvEfS5ouV7CtRhOyu5oQjQj9oGRlHqGulHN-Or9vCBfukN0bBK6nnlgzA_r4alpP0R2z2bGqgKhMxNYxxZhROS5I3Nfg22pZ1-UV0wRNpWdYCVAgk3803Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e64406e83.mp4?token=dH8cJIk2JnyqOmL9cu-TIBRKOGGqNfl4NqIIXnlXQDa5L_2hNJSJiCD7RPweq9bX3lcL4-P5iknKqHsEX2Y0w6-VKgF77PAUbwN7QCPXR5XD4yNFwQuo0qW3_SKojR-9HmdD3GLT-dEG00oqqfShQvKd_dG08WNrBzFb4sJH5JdGqiEnOlvE4d9H4uPAQ54sqnYi9PpwVzRm7W22_Ru_KCdx33UlzPsMvEfS5ouV7CtRhOyu5oQjQj9oGRlHqGulHN-Or9vCBfukN0bBK6nnlgzA_r4alpP0R2z2bGqgKhMxNYxxZhROS5I3Nfg22pZ1-UV0wRNpWdYCVAgk3803Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات امشب آمریکا به دکل مخابراتی در بندرعباس :
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://telegram.me/alonews/133969" target="_blank">📅 02:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
انفجار در امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://telegram.me/alonews/133968" target="_blank">📅 02:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/حمله موشکی به دوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://telegram.me/alonews/133967" target="_blank">📅 02:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133966">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
اپراتور سامانتل تو برخی شهرها قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://telegram.me/alonews/133966" target="_blank">📅 02:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133965">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6378495569.mp4?token=Ky19xtEjVKigO6bQm5l7mWshh_YpPTT72Y4GYJzB1C-UaWspg1lAgoLvlIp7Al54ONov2O-FH3mJGPQ1vaVgyVF63X6Cwh09ODJOmnFFaHjC0yt9FqH9IwXjt5Yh4Mn1JLbNIOsAUI5UKC0fPR1SggoJybOlj1Ths5czDW2najkGS1qHYQchf97ZE9JHtgIFlLEgCxbCuihF99sHWUllLdOzMq-oU5rKCVLPaa8UiwB4-YHDntiow5ex5KU-ZjcYMQNcaQMlip8mgHQWhaTU499-j8C54FaX1t5xc9zPtkti1gHDglo4-f4AUhj-SK6LfXWNbO3esCKPNe-UZzz3XA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6378495569.mp4?token=Ky19xtEjVKigO6bQm5l7mWshh_YpPTT72Y4GYJzB1C-UaWspg1lAgoLvlIp7Al54ONov2O-FH3mJGPQ1vaVgyVF63X6Cwh09ODJOmnFFaHjC0yt9FqH9IwXjt5Yh4Mn1JLbNIOsAUI5UKC0fPR1SggoJybOlj1Ths5czDW2najkGS1qHYQchf97ZE9JHtgIFlLEgCxbCuihF99sHWUllLdOzMq-oU5rKCVLPaa8UiwB4-YHDntiow5ex5KU-ZjcYMQNcaQMlip8mgHQWhaTU499-j8C54FaX1t5xc9zPtkti1gHDglo4-f4AUhj-SK6LfXWNbO3esCKPNe-UZzz3XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شناورهای تندروی کلاس «گلف» سپاه پاسداران در بامداد سه‌شنبه ۲۳ تیر پس از حمله آمریکا به مواضع سپاه پاسداران در بندرگاه و دریابانی کیش، در آتش می‌سوزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://telegram.me/alonews/133965" target="_blank">📅 02:32 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
