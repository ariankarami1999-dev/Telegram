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
<img src="https://cdn4.telesco.pe/file/gGqzAfwT_q-OmEUkRMRaUVE7hAV667MKtdi4Z_LS0S4J-0J-gmPaKcgHIVEbI2mmtcJa1KjHQ2W9JH6gwvCuARQt1UN0kBclRMU3u6fRZ-SyT6_XV3N-ojir149mFMr9BWPaQITHvI8b0NZfUT0GJO6Jd3Cd2omQdh9aeq_jTDvQfNySwCy2zaVbWqVe4Pz01Kr_9MxECGJp88YJibIeux4FTF0F3RvNieljWeQorObpFmbTsvzFz6L39rrUWqakfYdSk6l1eFdRbzP9wWmfVlYV55T1dzgA7_5iSJeScCETehwJpRh0NzFpWiiCpiEsX7NiErNIvOTP78kSKctPiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 17:54:16</div>
<hr>

<div class="tg-post" id="msg-675494">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سردار رادان: توصیه داریم زائران مرز خسروی را در اولویت قرار دهند
.
🔹
رئیس پلیس راه مازندران: جاده هراز تا ۲۰ مرداد شب‌ها مسدود است.
🔹
سی‌بی‌اس: آمریکایی‌ها جنگ با ایران را سخت و فرسایشی می‌دانند و نسبت به آن ناامید هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/akhbarefori/675494" target="_blank">📅 17:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675493">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای العربیه به نقل از یک منبع آگاه: ایران به پاکستان تأکید کرده است که آمادگی دارد مذاکرات را در ژنو، دوحه یا اسلام‌آباد ادامه دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/675493" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675492">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153e794733.mp4?token=htsF0AoA8yPLe_2mY_OUOZAPkKzs3ULPrpjnCBM4grwsvkwPEEmuBHX8SQe0PvyxJGLIygXt4cOQjNW5zillkpgdHggRi0fQjYHmB6zFSWlSNaJNjYz6CyU2nc4AvZnYoz6Ps2mQts56EIwH8MzRIn8-KOdxgvNdMy0LP38lRNC6vxLynDz5KxVf6uZ3etFmFZpcMlHYCv7CDtP02i74Nk52Qlpgnqgu-df-AndwFkrjxr06xpy5gF4-CewIBVcVdXv_jEdcNZZTvkqI5qwupJmPLU82iT9vut9YvRFFRNuFhwGRU5pzQ0M__-ImUqARxz9jV9mXkF96Vt-UJacC_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153e794733.mp4?token=htsF0AoA8yPLe_2mY_OUOZAPkKzs3ULPrpjnCBM4grwsvkwPEEmuBHX8SQe0PvyxJGLIygXt4cOQjNW5zillkpgdHggRi0fQjYHmB6zFSWlSNaJNjYz6CyU2nc4AvZnYoz6Ps2mQts56EIwH8MzRIn8-KOdxgvNdMy0LP38lRNC6vxLynDz5KxVf6uZ3etFmFZpcMlHYCv7CDtP02i74Nk52Qlpgnqgu-df-AndwFkrjxr06xpy5gF4-CewIBVcVdXv_jEdcNZZTvkqI5qwupJmPLU82iT9vut9YvRFFRNuFhwGRU5pzQ0M__-ImUqARxz9jV9mXkF96Vt-UJacC_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نون پنیر سبزی با شکلی خاص
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/675492" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=Nv0dfZELgW3Lw1ScaXnJ67Q6mnPNPPkAbGFb0qfXTnEP18rQFcAAe1gI5jBabM8HHlhXCbZy68MEx2kAaq8BZDg4HMvHLTnt3l5UQy2BvnV6iAaLKKfzVwTd-0dWRfiMvzt38WAJ9eHwfDyy0XsJV3zKh73uDG8Q9_ItxMvLp6PGf7wEdcCRBFYfOQIoG1e2r0LHJ-5Fi7OvvL6Mu1RA6_3o0Cu8Ktpz_PRGOmwcrNW4m75xMBT9BtcFVZtDOqPABqeAjW22dElVI4gKR7KJtRvTYwL8quHhEpX8HVyZaADvsSZug5I94w0GghCwu1msS80vZEf1qL5izpXPZoZgag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a84e97bfb4.mp4?token=Nv0dfZELgW3Lw1ScaXnJ67Q6mnPNPPkAbGFb0qfXTnEP18rQFcAAe1gI5jBabM8HHlhXCbZy68MEx2kAaq8BZDg4HMvHLTnt3l5UQy2BvnV6iAaLKKfzVwTd-0dWRfiMvzt38WAJ9eHwfDyy0XsJV3zKh73uDG8Q9_ItxMvLp6PGf7wEdcCRBFYfOQIoG1e2r0LHJ-5Fi7OvvL6Mu1RA6_3o0Cu8Ktpz_PRGOmwcrNW4m75xMBT9BtcFVZtDOqPABqeAjW22dElVI4gKR7KJtRvTYwL8quHhEpX8HVyZaADvsSZug5I94w0GghCwu1msS80vZEf1qL5izpXPZoZgag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک شب به‌یادماندنی برای بچه‌ها؛ دعوت احسان مهدی به «سر سفره خدا» در محرم شهر
🔹
اگر به دنبال یک برنامه متفاوت برای فرزندانتان هستید، «محرم شهر» هر شب تا اربعین در میدان آزادی با بخش‌های متنوع و ویژه کودکان و خانواده‌ها میزبان شهروندان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/675491" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قتل خانوادگی در قزوین؛ پدر و پسر به اتهام قتل مادر و دختر ۸ ساله بازداشت شدند
پلیس قزوین:
🔹
مردی ۴۵ ساله به همراه پسر ۱۷ ساله‌اش به اتهام قتل همسر و دختر ۸ ساله خانواده بازداشت شده‌اند.
🔹
متهم ابتدا ماجرا را سرقت عنوان کرده بود، اما پس از بررسی تناقض‌ها، به قتل همسرش بر سر اختلافات خانوادگی و قتل دخترش به‌دلیل شاهد بودن در جنایت اعتراف کرد؛ هر دو متهم با دستور قضایی روانه زندان شدند.
#اخبار_قزوین
در فضای مجازی
👇
@akhbarghazvin</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/675490" target="_blank">📅 17:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d069bb518e.mp4?token=vvctKUXKkKfVscBayT5hOvLCXy7A1gMrhuNwkFAV1fN4NO6O4lVzavbkhJXPzj7GqW245IGJ9zsDejV51PeEJurSSRGyRlQJ_h4kHfmacQiDSzON_2lA26lgLdgqyRhFJ_aML7zTHXGuDW9WOiKuYkyhj1Xr_V6fvjST-DzNQykgtZYMjcnODBM3C4eYMFsUy8XmUIU5rSdIxQQZMQRe2epKNfW5CuMhb4hho_H6TYF0rpyn7gcU_UsVcq7sDpQRyNWbhBik8xtgUsPBOYtF6dApyVU3VWZR-8Sufo3r01hXetdl_GhfRasg_y4QxR-FJzAZmB2q_ExL57OLr_dafTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d069bb518e.mp4?token=vvctKUXKkKfVscBayT5hOvLCXy7A1gMrhuNwkFAV1fN4NO6O4lVzavbkhJXPzj7GqW245IGJ9zsDejV51PeEJurSSRGyRlQJ_h4kHfmacQiDSzON_2lA26lgLdgqyRhFJ_aML7zTHXGuDW9WOiKuYkyhj1Xr_V6fvjST-DzNQykgtZYMjcnODBM3C4eYMFsUy8XmUIU5rSdIxQQZMQRe2epKNfW5CuMhb4hho_H6TYF0rpyn7gcU_UsVcq7sDpQRyNWbhBik8xtgUsPBOYtF6dApyVU3VWZR-8Sufo3r01hXetdl_GhfRasg_y4QxR-FJzAZmB2q_ExL57OLr_dafTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحبا به صاحبان پهپادها
🔹
خوش‌آمدگویی موکب‌دار عراقی به زائران ایرانی؛ عراقی‌ها امسال بیشتر از هر سالی مشتاق استقبال و خدمت‌رسانی به زائران ایرانی هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675489" target="_blank">📅 17:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTfN7XEASneaz_NE1yvTqPnFi3LIRfJKUVfLdBR8HG49XghMthzFsCduevtqUMfSpN_DONcBWUYDEaOjMXEdqeyHpjN7IT8z7tOJYCZvcb9_qET7FSz2PPV1WfZApDrWNuyiEHC5OXaK0gEFJNXR_0pJPUHq7idSHk85NxnoqwEE2QGbTI9-J4HIst0K0zw-sOzZiryG-EIywojo5-vXgqZLTeKQVOG5GJu57rrv6EQxJhqtZ5JlagYO07YSkMyf45FkbdLs2-IRg17LyZ_KH88ThKrUq1Yz3zjBR4yWjJhg8uhXKpHUrsow2HV3Hl9Yn23FbB5jqHqpa1onLQTpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای الحدث: ایران مذاکرات را متوقف نکرده، بلکه تعلیق کرده است  الحدث به نقل از یک منبع بلندپایه:
🔹
ایران به مسئولان پاکستانی اعلام کرده که از مذاکرات خارج نشده، بلکه آن را به تعلیق درآورده است؛ بر اساس این ادعا، تهران خواستار ازسرگیری مذاکرات درباره تنگه…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/675488" target="_blank">📅 17:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675487">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHpQRPqhfzJNeH9rd-uE7tibujOQxFdMZ8ptWmFxyixKJUyraqPFmjr34OUn4a_pnOUjRh0xYW2ksMKa7phbN9z4sLe5LgEYVhr0Yo0HlfQ0_niKHK8NT67ZFl0od2Iz2EeebkMTyvmRkAGHevPCarUD681I4fN-1gUsTj12edd_5dKtfhDHIDlTeO-Mf5bLXbuzia3c0fAJ1ItmLsFeqe5JT5Jrsxe5wMslf-W2B3A74IO8OLCYMRana0-wuRqcylCGPJOxkH6a99vMOjTbYZP0_1FQSgfCx_KyrDj3eCzIjftlhcG4XGrkt_yGJciEPlFWNGHfGl9wDtJozIbyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باج‌خواهی طلایی برای زایمان؛ سکه طلا شرط جدید برخی پزشکان
🔹
یک سلبریتی‌پزشک فعال در فضای مجازی، علاوه بر دریافت هزینه‌های مصوب ۷۰ تا ۱۰۰ میلیون تومانی در بیمارستان‌های خصوصی، شرط انجام زایمان را دریافت یک سکه طلا یک‌گرمی به عنوان زیرمیزی قرار داده است.
🔹
با وجود فراهم بودن بستر شکایت، بیماران به دلیل حساسیت شرایط جراحی کمتر اقدام به ثبت گزارش می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/675487" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675486">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اژه‌ای: برخورد با مجرم و مفسد هزینه دارد؛ باید زمینه‌های جرم و فساد را از بین برد.
🔹
ادعای سفیر آمریکا در سازمان ملل: ترامپ به دیپلماسی با ایران فرصت داده است.
🔹
نماینده روسیه در وین: درگیری ایران و آمریکا راه حل نظامی ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/675486" target="_blank">📅 17:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675485">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c18874268.mp4?token=Ahm9HlppvxGLDxj1irxioAEwIzxwdx3KyB9b7q5UBMqhrEWdvTqs2PQpaRcKmh0iJCCIs1DzDK54yB9av5YR9Gauh4_oEFP-_khW4eYcSxaJtegl9XCIUB1WZXyhoipc8tjTW8j21z2izM9EOgGUA7c1oOlxrCGG7TYfxf4YRQKrKSmyxVRFTnF1z3zd6thbw_dksfw6W0KOtX9FcLpQwn1w2xrDN2i9rswgTeBvYka_rk9hVLvPReetQreYH0S-2seuNp7To0Ki3sKvbfppFoCRouWQjjk6-6SHbm1L6XCW3ZaJWUo_3P1Nqy2jMfeKF6DAds50Fui8wfCT_fEqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c18874268.mp4?token=Ahm9HlppvxGLDxj1irxioAEwIzxwdx3KyB9b7q5UBMqhrEWdvTqs2PQpaRcKmh0iJCCIs1DzDK54yB9av5YR9Gauh4_oEFP-_khW4eYcSxaJtegl9XCIUB1WZXyhoipc8tjTW8j21z2izM9EOgGUA7c1oOlxrCGG7TYfxf4YRQKrKSmyxVRFTnF1z3zd6thbw_dksfw6W0KOtX9FcLpQwn1w2xrDN2i9rswgTeBvYka_rk9hVLvPReetQreYH0S-2seuNp7To0Ki3sKvbfppFoCRouWQjjk6-6SHbm1L6XCW3ZaJWUo_3P1Nqy2jMfeKF6DAds50Fui8wfCT_fEqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنتونی جاشوآ بوکسور سرشناس بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه دیشب خود برابر کریستین پرنگا، با آهنگ ایرانی وارد سالن شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/675485" target="_blank">📅 17:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675484">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد برکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEXBTbLmDGYgLkaGD67M5TJHal7HZNTNC9s63VzhnTNZllBXxhhSaMnvwAE8IZ96EJTv2vYgXeUaPpBjeYrCq2j1pvto_OCdukxrlLr5ajGqj-vZNTxBuULT8uD5HMgRi9hWJTMM17tRf3FrvnDnNxrs_CKGu7iwhjgxmz637zWKODOjmJy9W_i80BDsPQhv_NLEAOcO0vTsvlulOsVGsqsFYQvK7dVCvWNUtyaxCQn63AP-ACPjpf8pPkdJ49KzhCzruXUDEzNUFUplFSSDp-eBtfNy7qPC8zgo5QGIp2cvkTScMmDUz-xkhiFK6wCvjM-MZ_wtANmumwsqTpcKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📞
مشاوره درمانی ۴۰۳۰ با تماس رایگان از عراق برای زوار اربعین
🔸
سوالی درباره مسائل پزشکی یا درمانی در مسیر اربعین داری؟
🔹
سامانه ۴۰۳۰ به صورت رایگان و ۲۴ ساعته آماده پاسخگویی
🔹
مشاوره رایگان در زمینه‌ سلامت، تغذیه، لیست داروهای ممنوعه و معرفی نزدیک‌ترین موکب درمانی
فقط با شماره گیری 4030 بدون نیاز به پیش شماره از عراق
یا با شماره گیری *4030# (ستاره چهل‌سی مربع)
@bonyad_barkat</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/675484" target="_blank">📅 17:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای الحدث: ایران مذاکرات را متوقف نکرده، بلکه تعلیق کرده است
الحدث به نقل از یک منبع بلندپایه:
🔹
ایران به مسئولان پاکستانی اعلام کرده که از مذاکرات خارج نشده، بلکه آن را به تعلیق درآورده است؛ بر اساس این ادعا، تهران خواستار ازسرگیری مذاکرات درباره تنگه هرمز، سپس آزادسازی دارایی‌های مسدودشده و بعد رسیدگی به پرونده هسته‌ای است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/675482" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
کوچک‌ترین زائر اربعین امسال ۱۳ روزه و مسن‌ترین ۱۱۰ ساله است
رئیس سازمان حج و زیارت کشور:
🔹
تاکنون بیش از دو میلیون نفر در سامانه سماح ثبت‌نام کرده‌اند که حدود ۵۸ درصد آنان را آقایان و ۴۲ درصد را بانوان تشکیل می‌دهند.
🔹
استان‌های تهران، خراسان رضوی و خوزستان بیشترین میزان ثبت‌نام را داشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/675481" target="_blank">📅 17:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90be754f92.mp4?token=Sr4kHhZLzskcQ6_38Z35ImpVDb7uoKlAV7NYJiWpQRqyLi4zylx-nHknelhLyVmCvTV1oF2lv-rm_cEnd6UFV1b8lqARVDgwG0MLVX3HmI25fozhvHhSaq9owPGoNl1qd_G7ZuM5Wl_vUOfJ1_l4oQTc0Se86wWo6VP4N3Mo8e3qm_YPRn8IbXqVmWm3wMaHmaVRK_j0Jgg9Iexl8Pa8uB1Sj3O6CC0OvE9PHIICAy8bIP6flDrCoa0Bfqu94AzqQP4LqdjRIismIbDmsxDQ-9TDq9ULh7El0BAUFtYMDJDtxcRz4nhshkWpjLkzoHXbFP3QlGa9iSepovrHgOiipz74KH-WU2J3eefYNEbA_ttcj6d3J_P7amyrKkHRqVPp5N1JGO0PLPI9Tn2bM3d--_pAKTs1kAoC5o8QGUVhVSsOHUe4b98K8rjPBghYzNTKhNusnY9NvZXLbOLBg-oO_Z5nxHTmVF4u8CcUP93iD1ofBt-LrUflB6K-2kny0YYQj0_kNd-d6m7bWnelB6O1-cnucyzWjraTdRO3PXXr6vbxLAOkLWyAjONO1dZev-Q4A9g7MvbZAcMy_Bl8ZB1pjtNUh_wzjOc7m3ato2b1neQHQ3fOkkXHP8fTAENLhBfIe4n5q9ySsRXuX-1vbzomV4lpkXKApya2R8yQDUZU1Rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90be754f92.mp4?token=Sr4kHhZLzskcQ6_38Z35ImpVDb7uoKlAV7NYJiWpQRqyLi4zylx-nHknelhLyVmCvTV1oF2lv-rm_cEnd6UFV1b8lqARVDgwG0MLVX3HmI25fozhvHhSaq9owPGoNl1qd_G7ZuM5Wl_vUOfJ1_l4oQTc0Se86wWo6VP4N3Mo8e3qm_YPRn8IbXqVmWm3wMaHmaVRK_j0Jgg9Iexl8Pa8uB1Sj3O6CC0OvE9PHIICAy8bIP6flDrCoa0Bfqu94AzqQP4LqdjRIismIbDmsxDQ-9TDq9ULh7El0BAUFtYMDJDtxcRz4nhshkWpjLkzoHXbFP3QlGa9iSepovrHgOiipz74KH-WU2J3eefYNEbA_ttcj6d3J_P7amyrKkHRqVPp5N1JGO0PLPI9Tn2bM3d--_pAKTs1kAoC5o8QGUVhVSsOHUe4b98K8rjPBghYzNTKhNusnY9NvZXLbOLBg-oO_Z5nxHTmVF4u8CcUP93iD1ofBt-LrUflB6K-2kny0YYQj0_kNd-d6m7bWnelB6O1-cnucyzWjraTdRO3PXXr6vbxLAOkLWyAjONO1dZev-Q4A9g7MvbZAcMy_Bl8ZB1pjtNUh_wzjOc7m3ato2b1neQHQ3fOkkXHP8fTAENLhBfIe4n5q9ySsRXuX-1vbzomV4lpkXKApya2R8yQDUZU1Rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روضه‌خوانی سید مجید بنی‌فاطمه در منزل زنده یاد اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/675480" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqUYM6k-Ts24uKw0Qrc-gKNaMmDAFdGNCe0fOFilr3E8JgB8fRLHsTNdYMgEa4MItdrHyN0nTVaS9vlQyF3sX3_60_CV_WsU06BBjXiS5e3tGoiR-6yD6iR2LpW2nVEBbP7Iua9Xm9ARqbG-5sl8YyK6XexwEGPz1Grx3V9jTkVgb6_enHvNCnBHO6ABtJW4Zl0fggL-DKC_ntdiQQLNpN4--B0EwIkDgZkGeRykPy8N03EpE33YY8agGbiZEoobo3BrQ7O_hhsGegukbgNiVCrvbFw3QqqefoM3Tq_2bDSIkeDItqrDNSwbFFTkZ2pmXQ-cLXG6w0-3hmaaYBqy3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/inMY0-yucXsK71fK-shBPc1al0OOE5aZkxWh1YlNn7KEO9g-Kbi6WWTpGA05i9NmdOQEo6Ih9PacP3ipwod4qf-uam_VcRqEcW5KovNikcraaloRhiVv95slsnSt8ZaCWuVVlZ2zcqZQbIfqz41f-LNTJlH06_d6Rq1D2URvUL2n4inQKuG2SsVg0WINs96hFU_B0VOhsUpblsEkmpcFp4zZd7VH7YlHpDkTzFpwzimX9VtNoAYKZst32MIIRAH-gcQykJE4xaQ0C1ry39C4WMFVXu0kPK82WMUPepfu5Gx8lBlNLNXvZwUL8aVGE0wPljLImU3GoxTQNjTIsI0HSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNAfocusmt_Gq_YryRkbmf5kfxECFqKaMlr6ZBME9G-W6_GgIyCYdgSq92GYoHT-dfwR-X-z2E6OJPqUwgMh6whg2mcKaGa-XQbeyh7VWOse0zyE9NwnvylvNg5dc188UD3JH_B6N_60dpDUsdGDeVq6mXHl8RYYT5NmqfPmWgz1nvraIEKrQrKiEPyTEKaHkpubznfOlDoKgXEzFf33mLfj49qwg71FTdgiJdpYuITKGPzpVelx5-yUsiKFzHHGm7HX7UFMGayNta2jGz-fNysDpWSjWfCx7FQUAl1ZD-kxzHmY5vv5fuWQkLRKQy5h1NGxIRJp94PNo2rFDXgFFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازیکنان ایران در جمع بهترین‌های جام جهانی
وبسایت Sofascore به بررسی عملکرد بهترین بازیکنان جام جهانی پرداخته که در بین آنها نام ۳ بازیکن ایرانی هم دیده می‌شود که هرکدام در پست خودشان درخشیدند.
🔹
علیرضا بیرانوند برابر بلژیک: سومین گلر برتر جام
🔹
رامین رضائیان برابر نیوزیلند: بهترین دفاع راست جام
🔹
شجاع خلیل‌زاده برابر بلژیک: چهارمین دفاع وسط برتر جام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/675476" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
از میدان آزادی تا کربلا با پرچم «یالثارات الحسین» به نیابت رهبر شهید ایران
🔹
مصطفی زیبایی‌نژاد مدیر کل فرهنگی شهرداری تهران: امسال با پرچم‌های «یا لثارات الحسین» میادین شهر تهران و به نیابت و خونخواهی رهبر شهید ایران در اربعین و آیین جاماندگان شرکت خواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/675475" target="_blank">📅 16:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQJR69hxBLau3p7Lu6geUUxuy2debICLYuho_u1sJUhPFt3eXxNtOblXpjn3ZnFh3KN10vW9Yq28eUa5kq-ea8gBaRws4tZ9IsNmSYEymr0VVez5N1ofkK21XYRHQ9nnD64CStQh2n5uwCuyh9_5CcO1FJVHQl2yXLGpQK15ZAQoooEJSPlERFYxFAxfGKpMd4mB69hL6j4oaMN90nvu19IQoOCcuX6JMSm0gRkIuaDW95oBmmLtnF9VdJNMA0WYVrSLm6Viy5AQdh573mGfCB_7muNwjuHCjBWLP08dS9bAoZh7Fdcy1fELR-E3mUFr7Rp8LybwNzPqkhZR6YiylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نسل جدید هوش مصنوعی OpenAI معرفی شد؛ GPT-5.6 با سه مدل Sol، Terra و Luna  سه مدل مختلف معرفی شده:
🔹
Sol → قوی‌ترین و دقیق‌ترین نسخه
🔹
Terra → تعادل بین سرعت و قدرت
🔹
Luna → سریع‌تر و اقتصادی‌تر
🔹
عملکرد بهتر در کارهای تخصصی مثل، برنامه‌نویسی، تحلیل‌های پیچیده،…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/675474" target="_blank">📅 16:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ef1d20ad.mp4?token=a52T1UKO8oLkWjqUF34kYMM_XcX5gUA-iE6W-R-p5Uj4EoBVY8Kedkp19LBzvXWig52fbM3jSnTmokIUKDcgove9xJkBPtK8aPWbALb1MPTuBCnjY_yvTVtjdACcKEnoHkphSqsCyNw_z3Ej4oKsSW-mG803TBiQ7AxeaGWMYroepSEiE42vzvx1uMBYdiVtlMRiRKlvZNM2xaTIXqUXW6eYyh2jE0dRT0VZY7_QDsL6-c-HHEk7Gvf8GCb-rrd9mF4zNPYDsBuTK9o_uHqz5YIDLXGyzQ3DI8oAT-YsSw-jdnlvc_245TxlN4gOZUXFG8XOofAWb-PDUA4PolJ94g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ef1d20ad.mp4?token=a52T1UKO8oLkWjqUF34kYMM_XcX5gUA-iE6W-R-p5Uj4EoBVY8Kedkp19LBzvXWig52fbM3jSnTmokIUKDcgove9xJkBPtK8aPWbALb1MPTuBCnjY_yvTVtjdACcKEnoHkphSqsCyNw_z3Ej4oKsSW-mG803TBiQ7AxeaGWMYroepSEiE42vzvx1uMBYdiVtlMRiRKlvZNM2xaTIXqUXW6eYyh2jE0dRT0VZY7_QDsL6-c-HHEk7Gvf8GCb-rrd9mF4zNPYDsBuTK9o_uHqz5YIDLXGyzQ3DI8oAT-YsSw-jdnlvc_245TxlN4gOZUXFG8XOofAWb-PDUA4PolJ94g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروهک‌های ضدانقلاب را در نطفه خفه می‌کنیم   سردار محبی سخنگوی سپاه:
🔹
ما از نقشه دشمن غافل نیستیم. اینطور نیست که سرگرم تنگه هرمز باشیم و از بقیه توطئه‌ها غفلت کنیم.
🔹
دشمن می خواهد گروهک‌های ضدانقلاب، منافقین و سلطنت‌طلبها را مجدداً سازماندهی کند و کاری شبیه…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/675473" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b48e83b.mp4?token=CETsBEPlSkTmWtHVNvFDtjsZNfxL0_csIoDGoTOMTX-3Glhe9dmVbdbeQhVnSL9eyUwcFfeVAl6VTc-vhKnBVQ3FtcXivXdoFfQgrW6omHu3qJeNCB3aneMcsEfeuqEX2D65YgDDsKL3LQ_afb1Jq4YN6QjL9oqVm-sEZx4Kpy6gMD6_uYdD5Kyh6D-yLvW_o_H6scUsjmZJW-uhIYTa8kWzRjfrSPQlKRuRWChyi33TGcajYPqqGxGdeOC-JkMFfImOuKecVAi-6_wl8y_C8CUWz3pRCZelBV_SXYCq2v96MNlRabQas71WWMeB6iEBIY3JHIXyDA77DX2FuJhuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b48e83b.mp4?token=CETsBEPlSkTmWtHVNvFDtjsZNfxL0_csIoDGoTOMTX-3Glhe9dmVbdbeQhVnSL9eyUwcFfeVAl6VTc-vhKnBVQ3FtcXivXdoFfQgrW6omHu3qJeNCB3aneMcsEfeuqEX2D65YgDDsKL3LQ_afb1Jq4YN6QjL9oqVm-sEZx4Kpy6gMD6_uYdD5Kyh6D-yLvW_o_H6scUsjmZJW-uhIYTa8kWzRjfrSPQlKRuRWChyi33TGcajYPqqGxGdeOC-JkMFfImOuKecVAi-6_wl8y_C8CUWz3pRCZelBV_SXYCq2v96MNlRabQas71WWMeB6iEBIY3JHIXyDA77DX2FuJhuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نکات مهم درباره ساعت و نحوه ی مصرف مکمل‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/675472" target="_blank">📅 16:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675468">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WWsKcdPu7MeD01p7IF3qc71mP2LdIOvmzLgL-ZLg3AgB8Tkit1fVMe06KcjiWNbc6L5p4Z5wxhwRMh96Zdah7eWIrozqSFYfWRh2MR24ZVO-9IKyPak3fct3E0aFN261wVwuD6IMzd24o3e-ilbrN9vS0sbHsYag1kEsQWfwJWUVuOeXmAzuLyQwb5jT_YypRAjWwu7Y4kcR8O7_clKYsO_vH1E4raRVfmiEC-KApUi0ED85GEH4GhDp3G-EiSeK-1XB68VTzy7y9N4rwkNDdQTTXWWQQavd0hc2qsEjsFMRQno09gkHHyc1W-fdA2Uj-kF3VJiTBM7JVJw_txUBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRHo6DXH9DVVI2vxr6S3wElGkkK-8Xu0Nv_33Bnb7cuJptHxJC4bCFx_anS-GLIr5XIpmhPPQRu6eucA8G1qjHEcYnNIO3885XsOE44jZKdH5zeqjMPV5iNkQQDidA-bIEBwWIPo5FAZjEYa9dmwbO8tqJGcdPOAfPkq_RNkuD8mQGEFjcnSMzSpq_c_kgCiQ-kGUYWLchMgzugi5Cz1qI55ff1uyyum89cugwq27077-zBtR__VSjfByr_iiqfseevVFh7v3rOKVFI_6kLDvaFUlbR2b8x7BgLw0uMuPS5gzsXriFcdhqxgVaM8wCmfQFSmHHxl_sQS1tOCNr-MgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjucbtFrQTnrStnwwFJ-sp3VauzHhEVippv6BGW3JocU8WxcgXyKcSROzIciq6v8mV21PncddDYV1GAFutXNKt9rYCp7M8HqCTEM9jqmJdNlywj6lCOzZxAmgswcSxFms1_7EFcRdndE8_qPyyeZzTd5uS0tXu3M6J2IvNRFvWXApHPK3ltn9eYMU3GhC-n8k3MqUg3EYazYrQ2vEPSbfO9kSbWyape2_hBSW08cR6zMSQGynYC3s4GVGKnm6S2n6IfKOyCYPYarPkaqxnXpv8m-zxUtz45_PeDUIsfQEtsY_iN_0spooBQ-ci4bb7yZgf7eQLOaQ0BdKMJlq3L6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tjs1gdYnhGhWl1Glaa5QtpySx__NDvacfE-N3-2Osrqcm2Pryv9rdxJQf87pSMD7K8Ui5juExMr3o-edenQnEq6PDejOG1ie-DzbyL3o6I1KSxbR9pLXpI_NDU1shHUhav-ygKeF-kkLFBA6eQhmNrKkdmPDTA7TGMWIwAAJ-DTreL21DnvXoLTR8uSWshwJmyUULUThw4WiSw2aWa1Gw2FwfyqTbF7r0dhqxAJenwa9wpHQOeuk5hO4uIcCy3X5WfNXZfdI5eMfil8aJf1RhWjjRbY9MCk55XH3ZT4M4l8413MDHFc0n5eE0Mvdd33R22JRK5eDI8gvr3ts-8Ma-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
با چند اقدام ساده در مصرف برق، می‌توان به پایداری شبکه و تأمین روشنایی پایدار کشور کمک کرد.
🔸
استفاده از لامپ‌های LED و کم‌مصرف
🔸
خاموش کردن کامل وسایل برقی پس از استفاده
🔸
خاموش کردن چراغ اتاق‌های خالی
🔸
استفاده از نور طبیعی در طول روز
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/675468" target="_blank">📅 16:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675467">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd000ed14.mp4?token=dVw7u0fTb9ePnecX1uOHJGRXTVLAqv1yS-Y8D2nmvzTZ1p-rqcgLd95I2wrjtBC-6RnE1G8ukyT9_cnImSaDkbyVQfBgi21bOQYPd_em2gV8U3KVXB96ru10TpuEB4FmESp4jlyq5GxruZqf0uCylcW6pZrxtARQNahWjsHI8z-eRBRLjqkJ_StmxQxKzti_n1fvs_fQYvr2cwc25PSs6daoNn5WgrojCtD-BOv9QjblL_FwWc7QqlLWoW7YxPHGnxadK41ZHkUKT8tmYjHKwZBUE9hDcTKdiKYcZgqDGhJbslOOhfIfp6IY5FehqsXyLedRlXUW_3SJtbJRzF04wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd000ed14.mp4?token=dVw7u0fTb9ePnecX1uOHJGRXTVLAqv1yS-Y8D2nmvzTZ1p-rqcgLd95I2wrjtBC-6RnE1G8ukyT9_cnImSaDkbyVQfBgi21bOQYPd_em2gV8U3KVXB96ru10TpuEB4FmESp4jlyq5GxruZqf0uCylcW6pZrxtARQNahWjsHI8z-eRBRLjqkJ_StmxQxKzti_n1fvs_fQYvr2cwc25PSs6daoNn5WgrojCtD-BOv9QjblL_FwWc7QqlLWoW7YxPHGnxadK41ZHkUKT8tmYjHKwZBUE9hDcTKdiKYcZgqDGhJbslOOhfIfp6IY5FehqsXyLedRlXUW_3SJtbJRzF04wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام شهید صیاد شیرازی به این روزهای ما: بنده امروز با صراحت کلام حجت را با شما تمام می‌کنم، نتیجه تفرقه فقط باعث می‌شود در برابر دشمن شکست بخوریم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/675467" target="_blank">📅 16:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675466">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naqME7FeN4hVz0F_2mx60xrhDsRn2-jep3wYyc5hvaj1EZVsceI9GdwcoAtJgnA1rwYYdJA7hYPP3Wx1t3av-t-6-NGNSKcA7h3F89MyRkiQsgrtuWH-l7qKZvzf3-MaYCEb0D2ezPy7hfcwYZZkylJWVgUWrfcU_mNGxl64Lt-KHkQ3FK6f0_lDQ5hDaJF__Cyc-n455L40oTfgkWAx1ZRgApSrHrvTmCJevTFrJkG90B4Qzu6DNQlM2Ss7QZ8leLR_2KwooMxhpyS1BmaClanL0NvjoXxrDpq99FPdLxEe10tqfyC2dY6mbq46SjzA0ZBkhQzSoBBvQifWUNsERg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرباز سابق نیروی دریایی ایالات متحده:
۳۰۰ نوزاد در گورهای کم‌عمق در غزه پیدا شدند، در حالی که دست‌هایشان از پشت بسته شده بود و زنده‌به‌گور شده بودند. این خبر در هیچ روزنامه آمریکایی تیتر نشده و حتی در کنگره هم مطرح نشده. همین یک موضوع به‌تنهایی نشان می‌دهد که این کشور تا چه حد سقوط کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/675466" target="_blank">📅 16:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675465">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1gk1XsUofSIKuXX2EeyUl4q01vXPpTyT1ETsm_Ko4shLgxEGUp5m8NbIu-LUegFHu8Ik7fmMpDk5-PTsCa_bhGVSOUM3Gl9DGWd2lqyTMsWxLWYSpE8FFk-x9LaaXj7xALx9Dqbf0ilIDVyT-yGp5KGTclWoiWARBcPe8WrngdkT8ItDEwRbduOfY8BTzN1dVp6evQMz-ZDGdVy8vydDAE2TCexIGpYbl9GfcTts3YP98PXZCrz_v0j-FS7sZrLPRP8VzXCh_Efwjca3wL8OLvnKFOAbe3vhVRbQYQkRpb36g-JwjmZPC5rMBOitdso1Sr-ViorvKyhO7m8w9XzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای رونالدو حتی ماشین هم بخشی از استایلشه!
🔹
کری رونالدو با بوگاتی ست با ساعت چند میلیون دلاری‌اش!
🔹
وقتی جیکوب آرابو از ساعت خاصش با رنگ کهربایی-نارنجی گفت، رونالدو فقط یک جمله جواب داد:
«بوگاتیم رو آوردم؛ دقیقاً هم‌رنگ همینه.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/675465" target="_blank">📅 16:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675464">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
گروهک‌های ضدانقلاب را در نطفه خفه می‌کنیم
سردار محبی سخنگوی سپاه:
🔹
ما از نقشه دشمن غافل نیستیم. اینطور نیست که سرگرم تنگه هرمز باشیم و از بقیه توطئه‌ها غفلت کنیم.
🔹
دشمن می خواهد گروهک‌های ضدانقلاب، منافقین و سلطنت‌طلبها را مجدداً سازماندهی کند و کاری شبیه اتفاقات دی ماه را دوباره رقم بزند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/675464" target="_blank">📅 16:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675463">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUT-CuGTHvXKMukYN1c5PEkpbPIMi7talvMcJWqubqLjZme6nWJMrTam7h7Ss5mylPicS-ROGnFt__gfWRSYHG1Gi0GURaJxwXXuHPT9hfGurhSd3_5enbQAGqY9Fu3QY2T1Tk5K-8wdakTW7XGCWAXnh1_oB08R5nkl1mDUexgmLd5ztMdEK6mQIDbsUf-bEHK-U3JZmxkNnLcb2Ul7YuJ8gERUndVOG2A_Gl6hLUSLqstwE0mAjZH6uzRHNA-mtNG5tVq8ZiX5LqJde6gNla6G0r0L7iTMwCcdqNqqa9rq8vMjcXBZBIvArv4-fXGm8IBP1rPLhULmqfYMi5pLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رایحه‌هایی که سرحالت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/675463" target="_blank">📅 16:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8869df45.mp4?token=Vjj0FQOZg7YSX3D0ScrXXS7jMmEWuAv-CWvaPMFZ1VUOILccPQlq-WkxSGjTNzmMQx-hzhIcqMgVhNQwEl89tEJzabpRYU3xanVcbEDQ4Phx3DqCx-ISQc20KNYrtQsg87qWm-10mDxpPYSSDNiEcCdh4YpYIPwAkKS7Kjf_ZXf34mHhUvE2ohl0_fB6uVDqrUy3Hwv-C-wUIBzRyE0RgjtqvkgKVmF0DIALls6b2yixP-xEDsHnzeErvdFNwDL5f7dhU5gQV8eKZg7pNmrNtc_dPbrx6YdsBTcQXMCEHF3lOG7ENUi7B9e7tNyXVXOmQwkP3LyZ9j0vASPckvXjPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8869df45.mp4?token=Vjj0FQOZg7YSX3D0ScrXXS7jMmEWuAv-CWvaPMFZ1VUOILccPQlq-WkxSGjTNzmMQx-hzhIcqMgVhNQwEl89tEJzabpRYU3xanVcbEDQ4Phx3DqCx-ISQc20KNYrtQsg87qWm-10mDxpPYSSDNiEcCdh4YpYIPwAkKS7Kjf_ZXf34mHhUvE2ohl0_fB6uVDqrUy3Hwv-C-wUIBzRyE0RgjtqvkgKVmF0DIALls6b2yixP-xEDsHnzeErvdFNwDL5f7dhU5gQV8eKZg7pNmrNtc_dPbrx6YdsBTcQXMCEHF3lOG7ENUi7B9e7tNyXVXOmQwkP3LyZ9j0vASPckvXjPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک پست مدعی شد که کی‌یف آماده واگذاری ۲۰ درصد از خاک اوکراین در قالب طرح صلح است
ترامپ در جمع خبرنگاران:
🔹
طی ۳ روز آتی، جزئیات کامل را به شما ارائه می‌کنم. اما ما دیدارهای خوبی درباره اوکراین و روسیه داشته‌ایم که باید دید اوضاع چطور پیش می‌ رود./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/675462" target="_blank">📅 16:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82abca7c11.mp4?token=L40rOaR0Dprnm1ULeovUg7jStXJ4kdz7Ofwja0BG_7NWSDPIUaPVL8CBLd6vhYn5AqggT23H3tJ78XXKCbknqGhKf3tk8BMmAHN4TvJlqSRy2isXz82dgPaD216jZZTl9NfKxlaLtvF6M4MEi7NOwCwhQn0Zl_U7x0CbkcR_kAkKI5ksrwFWrgUny1-Sb23bl5EwP8ZSp78olCJpYL91Rce8K0gp92zUw4YpQDY7fS3N29NA4ERHUZcDTJ6C_aNwnuAwaYWOEsucF5iTd1s6OEtWV439gsDrwpuy3ft1bHcMDugAsquYq54uzdV2HhdLnGD7kPXilCJ9mro0w_UUCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82abca7c11.mp4?token=L40rOaR0Dprnm1ULeovUg7jStXJ4kdz7Ofwja0BG_7NWSDPIUaPVL8CBLd6vhYn5AqggT23H3tJ78XXKCbknqGhKf3tk8BMmAHN4TvJlqSRy2isXz82dgPaD216jZZTl9NfKxlaLtvF6M4MEi7NOwCwhQn0Zl_U7x0CbkcR_kAkKI5ksrwFWrgUny1-Sb23bl5EwP8ZSp78olCJpYL91Rce8K0gp92zUw4YpQDY7fS3N29NA4ERHUZcDTJ6C_aNwnuAwaYWOEsucF5iTd1s6OEtWV439gsDrwpuy3ft1bHcMDugAsquYq54uzdV2HhdLnGD7kPXilCJ9mro0w_UUCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه از تصرف شهر شیفتشینکو خبر داد
🔹
وزارت دفاع روسیه تصاویری از آزادسازی شهر شیفتشینکو در جمهوری خلق دونتسک منتشر کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/675461" target="_blank">📅 16:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10915659e.mp4?token=Zk-jPepjOYkND13lzkSDS1MqtjRPZ_yK5muEOg1MGgcTyz8P7L69RzQVyEISZimt3HFkuojk10L5W6gABmvv7DmaLsmY9fR4kg2ccbR_uCNz31HSQwemxTYilZbshCqhVR1jZibRz4VII-pp9sbFKxVXhLGd81C3Eg8DE5Ae_gb6hNj8yOyPrKFitQFC1Q15ueKDYdhF3mwVySmPxjdokE-o37bznf3u5AO0CfD12CNkHdu8TALoowijIr8zk3WgRnRJd0JdkP7EF6Hn5Ltn1NaD7fSkVAu_5vQUTzu4l-j8RyR4EgjqBd9a8OBHBaaVq4A3iuZJwyGRobC8l9wE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10915659e.mp4?token=Zk-jPepjOYkND13lzkSDS1MqtjRPZ_yK5muEOg1MGgcTyz8P7L69RzQVyEISZimt3HFkuojk10L5W6gABmvv7DmaLsmY9fR4kg2ccbR_uCNz31HSQwemxTYilZbshCqhVR1jZibRz4VII-pp9sbFKxVXhLGd81C3Eg8DE5Ae_gb6hNj8yOyPrKFitQFC1Q15ueKDYdhF3mwVySmPxjdokE-o37bznf3u5AO0CfD12CNkHdu8TALoowijIr8zk3WgRnRJd0JdkP7EF6Hn5Ltn1NaD7fSkVAu_5vQUTzu4l-j8RyR4EgjqBd9a8OBHBaaVq4A3iuZJwyGRobC8l9wE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: دود غلیظی مناطق وسیعی در اطراف پالایشگاه نفت شهر جازان در عربستان سعودی را فراگرفته‌است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/675460" target="_blank">📅 16:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
۳ محصول جدید لبنی یارانه‌دار شد
🔹
کارگروه امنیت غذایی ۳ محصول جدید شامل شیر بطری یک‌لیتری ۲.۵ درصد چربی، شیر نایلونی ۹۰۰ گرمی ۲.۵ درصد چربی و ماست دبه‌ای ۲ کیلوگرمی ۲.۵ درصد چربی را به فهرست کالاهای یارانۀ لبنیات اضافه کرد.
🔹
با این تصمیم، تعداد اقلام لبنی یارانه‌ای از ۴ به ۷ قلم افزایش یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/675459" target="_blank">📅 16:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmiYyaSnZpSJmqv08voGp4_EwQmfX9AuKg_6waraWzUV0zgMVPkv2_5NiQ-bXPp_6wY5-43cMcJuBAM9kVhPcPIQRgtLcsmRt67mJCRvG_8DjnZy20mg_es8PmqdPdsNHpVgir2JkZB5R3_tQnXhPQ0vTqQdDZKfF-1Mr7MYBk_VdIsYD4dY8D8OOWbNubeIo4XNBNeNBAK1a8lFlOWa4Jf-beRpaGuxnWRvMTa7yiWSPZvgjSIVl3e3DyOpDXZKvmDQg2REHgyKDMKSexiE5YdNc2CCBqnSEbnBu187VYtESVZlqPf6py8XIUxvLz-6N1cAijKMlbZ56RRfy5vI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMlF74LnRUNivg6sTuG-sI4IgH0gxTwlX4-2Z3DMah-j5MbmgbqYKF1_KoLi8d61iwtjcjLqX9VqlpvrhFdPOx8mRtXSQEgDEsdb3XTZdV6cubOLwbw_jVc5ZEVrJlCGZ0PaPFD_KAFrGdmRaI4vkWY9I4NVXKHg4iQ3-ixVDfiq0H_fVbW2a3QmO3rQaoDp7Kpelt-xHxyoyn0Cd9ha_Zc-UBjF8uViezo4IYgtBWoHxkExq3MoYq5TLFdptD_F_cgPi2yfeUY0pmEtbBZrvKcWfy28ipGo0dIxwlDSn0YN7MTzlJXHxshOo8zRCu4T_kP3jCxxV4KRb7koeqe47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVn7timNigmdI-jj8DgA1arXTbi5tTNj_YcNANh6XAK1QTQlipjIYsPcX1hp_pZoN4AwDSSOuUmNo94g5YD-1xJ8XsPQO4rXVty8szS44pt4F8uo7T1A4jISxTHZnrk2-J-FNkxoNlLZGpOHrLxd5ZJYVqFQGjC3S-jCh-cHLjP3lBg83U9orUVVNwFzvKtnT8_fBkNSVW0CvAaIxgV3gK-dtgZqMKi6RiynPP82EYowcrMQmoGEendQtUmYpw3QHvW_PA9dfvwtbrPqgWyhYi-zJxVxYMRp3F4VG_l-aCbYPJcbBkeOvB8fTYJHN8NUkhosDH3UN2R7rBn_z_guwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JZRmYo9ZULI30ati-bR0JK50t9I-yUS942BfU1tvAKJu9453wBY3Whd98ebbmK56eeJLVUvRYU1SuvRTHbr8npk1lBDQU5zuRtsy1nX55sCFJsj7eGkjuENDMXzjIIhBCDRbyaDbLGjuXF4OmDeLWqiC_f_COrGsxtDqfpx45MybTH-2ll27D9pXiV5N2reGxP0nDwKqXzI4GlHZHb1QWnADqAZeqZMxFHvTRTh1HvwOHhvTOn8_6ElKufNIF-yFhmif-W0odUIuOIvAoEcAYAO1JUl7vsqxTz2Q4QNiVG4wteeU7qIWLLL9SHN0Hj1YzwKXcl_wxAu0PzUtRlQKBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فهرست خسارات اعلام‌شده آمریکا در پاسخ ایران
🔹
به گفته سخنگوی سپاه، در پاسخ به تجاوز آمریکا، طیف گسترده‌ای از مراکز فرماندهی، سامانه‌های پدافندی، زیرساخت‌های نظامی و تجهیزات راهبردی این کشور هدف قرار گرفت.
🔹
این عملیات، فراتر از انهدام تجهیزات، توان فرماندهی، پشتیبانی و آمادگی عملیاتی آمریکا را در منطقه زیر ضربه برد و آسیب‌پذیری زیرساخت‌های نظامی آن را نمایان کرد.
🔹
به نظر می‌رسد خسارات در ۱۵ روز اخیر به پایگاه‌های آمریکا از مجموع خسارات به منافع آمریکا و اسرائیل در جنگ‌های قبلی بیشتر و دقیق‌تر ارزیابی می‌شود. این موضوع، به‌روزرسانی و تقویت قدرت آفندی (موشکی و پهپادی) را در دوره آتش‌بس نشان می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/675454" target="_blank">📅 16:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXmMSPcRZHFKl5Jc26gz_5bSj4QxU2DIqqjgU9EPUfadFpV4HyoQXARruuBJVJCTk8Kr6LAXzNWJZb7BvZCYwlc0o8NQgLh-ecE_fEyV-Ejt17GpuA8HBuvN7m6GM60QVqEarvynjJ20FjoCFCljrOzS9eELn-jb6uVNzdetDGSe5JOg5XIqbWwjaGrNLysAtu0sUN36yOgBYatDyn_wdgv8BTuWDEgFhw9vpwlW7921My1W-IfnVAlZ4JDZpFD0km0aL1FbKOUBlzS270xVO27aNJGa7Uf1bVx1uzPDN5s0S9uL730pcWPuE_InvbhBhVwzI-oxSBInaVEi7Nmj1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0sGNKGNh4TyZBmwoCMGPb2ZUYMrL3EV1oANLbAkjQldzHUQ1vR7N-VNXezgORWFHXrDwcAHPizGbhhpCJkkNIH9UnrtAL7cyEU6oLL3wRrUXKNVGaDRIDF5GttAJ4KH1iH5ZLnX9ck_Fx5xWoQjF1t2mkmGiG_g_2NqnuUIHsQf39iqJHXMWAhsRV6EDqID7W74FHMe82bK4yBi_V3Ry82W6BYKVRGOa8prFZQVgS5GWqBytGmtsuvb9rIPf-KtZ9pnnDByUK1xTHBDHa84AQuODQbnPjNOvV0A91v5Ompei9PQFB1D9kGxcQ9FyiPBK1uNqS9rmDXarYSko14XqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4EQdOSvQ7tab6qmMYx-uzJzapRup129yYmv1oX4bIoSmnJUcO2l1_k_EHyWdVW8TXT4gXupKbmp3j_EvWuki5UvH01-77P7hhU8uJ3MzSFc8WojNOONG-phnByv7wbqAXf2lIJJ8-ACHQIBHjxjorxr7-BzTFGoZkY8cD6q1JfbAg3ZZUsARBA5OLuII8H0AYJLYWadUAwsqLNv24nlCwMGXIRFFhkQ1-TdohHK2EUMrFRuYJrs0xtftZ32nadVCTM54f6M0WrBj00jikaSi1XbpdDOIvyDaUhHOFBT9XgXLzjt2kwiugJWy4Q0uVV7NwI_6FJ7tgN3kU1KYJv8Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر با حقوق ۲۰میلیونی قسط داری، این ویدئو رو ببین تا تو خرج کردن کم نیاری #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/675451" target="_blank">📅 16:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
کویت توافق همکاری دفاعی با پاکستان را تصویب کرد
🔹
اقدامی که به گزارش رسانه‌های پاکستانی، گامی مهم در تقویت روابط نظامی و امنیتی بین دو کشور به شمار می‌رود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/675450" target="_blank">📅 15:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675449">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eea40c5e8d.mp4?token=tK5q0UDrU9Pf0CRhNrJjRvcKMpjL6vpDcucEttfKGbg8YyzRaJFS29t3KN8ntxBt4OxSKkCO5IkcnBy8DeWW_ZZZsnZplA3pYqqGpYB17v9yqOpByDg8S0-P3MOPqHXq-9XDwemmKxRF3P1F0G1ogKtY2-el4tD6EkDjYH2_RwGoTB3npA2ZqHovV6TTm7JcR5XJEyeSJE5Lop1axCjMRar8USGt0DbeLZVf6IY-olJ2Fzj9XmmyzDJ_n5PiEH6bVgSXdav1iic_xP1XZXxiLNpiBw9Umzj2t3TiAK9NU7kx8Qk6QrHmky_Ut_pyC4gYSTSIPCD5Y1m9mXOIclWARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eea40c5e8d.mp4?token=tK5q0UDrU9Pf0CRhNrJjRvcKMpjL6vpDcucEttfKGbg8YyzRaJFS29t3KN8ntxBt4OxSKkCO5IkcnBy8DeWW_ZZZsnZplA3pYqqGpYB17v9yqOpByDg8S0-P3MOPqHXq-9XDwemmKxRF3P1F0G1ogKtY2-el4tD6EkDjYH2_RwGoTB3npA2ZqHovV6TTm7JcR5XJEyeSJE5Lop1axCjMRar8USGt0DbeLZVf6IY-olJ2Fzj9XmmyzDJ_n5PiEH6bVgSXdav1iic_xP1XZXxiLNpiBw9Umzj2t3TiAK9NU7kx8Qk6QrHmky_Ut_pyC4gYSTSIPCD5Y1m9mXOIclWARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری خاص از نقش‌های اکبر عبدی در دست مردم مقابل تالار وحدت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/675449" target="_blank">📅 15:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675448">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pj2CP1xgz8wnYwqFycaoZz54nYKMG3iYqawQ9IMmq6OUHWwI2vo9WV0q6ap22Z8rj25oR4PFX9UGKvfTeEQsTLUWCE6jFjlTVwEpos090k-sw1Z5v2mNcQPgYP9dfpvNNnClSRnGX0BGHsckCLVSyJdxIDlwX306kEXSISFDerjQFbnJJHCAvFyYhNLBz2bJYnjnoeL6XkHs0QELXufQiWSkZMnKzqoyCQNF0f_wN5q4GC9xKodFks8uKcEsyEqg2t8VP1VulqZA9MnxUNMkRYdCSbiWQyTkhI8j5PLZs-IdAC_Fh76LWvOWRwVt4oFqk1BuK7NUAFoEZUOUArVTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر این روزها فروشنده‌ طلا هستید، حواس‌تون به این نکات باشه که سرتون کلاه نره!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/675448" target="_blank">📅 15:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675447">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG5RIyO2PK8LDKQ3njyLjM-FTQ81AJb3FNJUj_gJ8vjedypjL84B189k7h1Abs4Et8x_QNSG7LLy8-1ojxyOObLtEoEOfIrDKf5nmm62gIB3ebGfFCzw43hSLbmmRAEmHW4hxVq2EWH6R1IJysjjN7-QGZW8xlIOqRl-O5CIpLDGIx1Etoh21RxsQffWQivIzyP1VqaeHr92gLD3fzn-rcFpd1g4cALfuFG5Fw4IcJe3-QawMpWbdZVTqOIRrI2faxGIghGpRd282xFxUSDqZmQCMRgP2BG_oYj2SpiPqzmRNXUx4oeg2U_MIFJP28YnWIEpOqZO3ZGR-GqH67TGKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقابل شبکه‌های تجاری ایران با تحریم‌های آمریکا
🔹
به گزارش رویترز، واشنگتن در ادامه جنگ اقتصادی خود، شبکه‌ای از شرکت‌ها و کشتی‌های حمل‌ونقل کالایی را برای اختلال در صادرات نفت ایران هدف قرار داده تا زیرساخت‌های مالی صادرات نفت ایران را مختل کند؛ شبکه‌ای که آن را تهدیدی برای «امنیت ملی» خود می‌داند.
🔹
با این حال، اشاره این نهاد آمریکایی به توانمندی شبکه مذکور در «دور زدن تحریم‌ها و توسعه تجارت جهانی»، نشان می‌دهد کارزار فشار علیه اقتصاد روزمره مردم، به سد ساختارهای انعطاف‌پذیر برخورد کرده است. تقابلی که ثابت می‌کند تهران در برابر محدودیت‌ها منفعل نمانده و مسیرهای جایگزینی برای حفظ شریان‌های تجاری خود ساخته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/675447" target="_blank">📅 15:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675446">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
انفجار نفتکش متخلف در تنگه هرمز
یک منبع آگاه اظهار داشت:
🔹
ساعتی پیش یک نفتکش متخلف در تنگه هرمز که از مسیر مشخص شده توسط جمهوری اسلامی ایران خارج شده بود، بعد از برخورد با مین دریایی منفجر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/675446" target="_blank">📅 15:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i53tOKjhnNrsG2FZlNZHFCwBUu7c37Th2tB4-2bBLkWzRvgLeTxfnV3s3NQA8jxGwsJek9tweTTwYcGQBfCuX8LFx-jGr_ZHCrrfkn2wsUBZXTd23j6Foo-bAsW04SwXP_X6uHxsJAbz7LTW7PnvpP_jwMUapUgvbKpSdnwfyJdAXwNE5NalGCdBzpiwKnroOOldaaoCb_2AZEzBBPQxL6h-sGu36mUp6bmrr2rNMcdY7HSxQpjg15S8XJpaIKMdYHPxrWjxoDhoWYP4CbOgCu1eBN3UjRQnbnShUSWzmb4GBZelDUTT8OhSE_HH9IgkWqWFbVtI7uff1UI4eTUJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzWrn9KbGuzYXhLpjrsPf7RTMxuXCD_ntYXdrYCe_L-VXXhZJ7SpMDzGmGZuTgWzOArl1TierwGUIKz4bVdjZKLkv40nHbaqxjA4LCUCNuLHVpQSZA3St4a_bPbegg3a7MC4fWTiIh-ABpqexcObqUMj2bOCRV8gythdJOU3-nfG7ZJXzGd7qe76kaSGrOGNKg1LHlRlVDFFYZHGrEmupswcty4XB9OjOghtlnC_XLSWY_fZe9MhlY1KtQdZG09GrrzbqWameTD00xKCqqaUvfEMBKpJ15RJuI9Mvoh_TuXRtv56pQ9AS9lCmEdRuEuli0SM8gwSEaEZkJLmC4uvUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سی‌امین اثر ایران با عنوان «دژ الموت و استحکامات دفاعی وابسته به آن» در فهرست میراث جهانی یونسکو ثبت شد
🔹
سی‌امین اثر ایران با عنوان «دژ الموت و استحکامات دفاعی وابسته به آن» در فهرست میراث جهانی یونسکو ثبت شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/675444" target="_blank">📅 15:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnqSF45xbCGLZNKFbhv7N7w57ZysnrGd1DlJVlh7JYENK4tDTTk89k-fWmAId5dNp-Qx-Wzw-xH7uQa-WqbMnq102bkbZGS5NTgoug7TEfW2SV7TB64yqZuDR9N3Vr5WusoUWNsuX6vRQaw0nPg5CdIhFFVwxqE7IhR07LiftV0VOlIZObtNMiO8zYar7P1YUQOJPY91sHrWGFsaaXPL_9i_sn103vKsHRKN0cQRnhs9mtTfvyOaIU58lU5JH_22IfWvEChApJm-Aj0KI6flcynqg3C5c-x9AVjXFYGPXhJW1asp3kU65Dr2a1f01O9zlywCENASRUzfUv0M6MrJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری خاص از نقش‌های اکبر عبدی در دست مردم مقابل تالار وحدت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/675443" target="_blank">📅 15:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363c16074a.mp4?token=txIk_vKkUOVk-W7mXduXsspiNfOoM7TOxdafuq6gSrXQxiei4EbvWf3lpeZGa_00swKTaqH8XeTt2AgqTs8KmVGWVZNHEFWKw68Kbzt5xmrw2RMxvTzbsMn_o1-Y_3S47yM7qMarMsjCWWOnIyfjRtNTO3e-idX_BV72J-l3mQEitKsr3rY-wc5P0dLWQggMWn9qY-R-WPKHt9kw3Ehno0zFgaz7pxGx4L8IRkLwByV7feJxwGRde18Fj7etN4_h3zc35LOY4oqh9WVX3lvFqh7jwnYmoxHEZE9sgNlhIZRwVwWYGGUCAkrsit345_La3iooBxEDGBHsA7UYa-52wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363c16074a.mp4?token=txIk_vKkUOVk-W7mXduXsspiNfOoM7TOxdafuq6gSrXQxiei4EbvWf3lpeZGa_00swKTaqH8XeTt2AgqTs8KmVGWVZNHEFWKw68Kbzt5xmrw2RMxvTzbsMn_o1-Y_3S47yM7qMarMsjCWWOnIyfjRtNTO3e-idX_BV72J-l3mQEitKsr3rY-wc5P0dLWQggMWn9qY-R-WPKHt9kw3Ehno0zFgaz7pxGx4L8IRkLwByV7feJxwGRde18Fj7etN4_h3zc35LOY4oqh9WVX3lvFqh7jwnYmoxHEZE9sgNlhIZRwVwWYGGUCAkrsit345_La3iooBxEDGBHsA7UYa-52wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه صدها هزار نفر در جنوب چین به دلیل طوفان
🔹
پس از اینکه "هشدار قرمز" به دلیل نزدیک شدن طوفان اعلام شد حدود ۳۴۰هزار نفر در جنوب کشور خانه هایشان را تخلیه کردند. همچنین، فعالیت‌های عملی، خدمات راه‌آهن و پروازها به حالت تعلیق درآمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/675442" target="_blank">📅 15:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ملی‌گرایان خارج‌نشین به جنوب بیایند، قول می‌دهم کسی با آنها کاری نداشته باشد
مرتضی محمودی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
شایعات درباره اعزام جان‌فداها به جنوب، عملیات روانی رسانه‌های ضد انقلاب است و نیازی به حضور آنان نیست اما در صورت لزوم این نیروها با آمادگی کامل وارد میدان خواهند شد.
🔹
از مدعیان ملی‌گرایی خارج از کشور که با رسانه‌های خارجی همکاری دارند می‌خواهیم به جای عملیات روانی برای دفاع از سرزمین ایران به مرزهای جنوبی بیایند و بار دفاع از کشور را به دوش بکشند و من قول می‌دهم کسی از داخل به آن‌ها کاری نداشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/675441" target="_blank">📅 15:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675439">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8aWQmCrPqKWLmmtIqodT9F5oGmzdDZClpon1oNgqgDXYNLb_0N5McvuLqRl0I86Xk-jE9E4VRYtaOrh8ZXD7CtkhHGN-Aelmtmq-aANM4bLXPh72hlltE2hCbgjI0V5a0rYHb7g4-P8wngzfBdN-SUOvERdb8FN2QEIUhPKPnyECnEdDWeKVUeL7oHVPiWc9wzjr8hmkFZb0mAMvMifDy85r8EWaIMtl6V-4tePfzzWJ4JIHu5Ph_RNQiBItBCNBfgKYwV9kJZYC5JNX3y9DppNrmJ0iWOqHh-JPr2khnhX4C3SiKitkvN-5bTlt7dCTy3LtMphAqnImPiTyEDDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
فرصت استثنایی سرمایه گذاری در   اراضی شمال کشور
📍
آدرس: ‌شهرستان بابل ملاکلا روبروی پارک بانوان
📐
مساحت 31280 دارای سند
💰
قیمت‌ کل : ۱۰۵ میلیارد تومان
💰
شرایط پرداخت اقساطی ( ۳۰ درصد نقد الباقی دو قسط ۶ ماهه)
📅
زمان ارائه پیشنهاد: ۲۱ الی ۲۴ تیر ماه ۱۴۰۵
جهت مشاهده اطلاعات تکمیلی و‌ دیگر قطعات قابل واگذاری به سایت املاک و اراضی آستان قدس مراجعه نمایید.
🌐
آدرس سایت:
https://amlak.razavi.ir/panel/auctions/#auctions
📞
شماره تماس:
051-91008003
#زمین
#مزایده</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/675439" target="_blank">📅 15:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvl7u0JL0Dn5lXAYFInzVYXbX6F_ufKZ3jS_keXEkpLcsuq4eYFB39qUF_WPEhtgFqYyyqZWGWagqZP4zaZnDzijKhENSt0s0xV_SFUJ_c1FFIDDrem2WnmPSzuQ8NWGuvbgSEU1f3C5nXqEKfQPrgRjs7k4RA3fLq9AbUR2-FuAyVT73835nS5g_0_tZMpQh72ah74QtUFJBhN51zmyNSB0lKxhy01GwlmO1P3hdJ9JBcxCw522g5znSO1rvkcagsuK5UEXGYPHH1lwFthv9yoFNPnbxHJ8ImDMRmsKHRb8aOhSsZ8zp1iZSfvXxGjEnuVJgqTFXGXKf1IyEGbSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سرمایه‌ای، فرصتی برای خرید طلا
🟢
صندوق طلای «رز ترنج» امکان سرمایه‌گذاری آنلاین در بازار طلا را با حداقل ۱۰۰ هزار تومان و بدون دغدغه نگهداری، سرقت و تشخیص اصالت فراهم می‌کند. همچنین برخلاف خرید طلای فیزیکی، اجرت ساخت و مالیات خرید ندارد.
🟢
بخش اصلی دارایی‌های صندوق از گواهی سپرده شمش و سکه طلا تشکیل شده و پشتوانه فیزیکی آن‌ها در انبارهای مورد تأیید بورس کالا نگهداری می‌شود.
▫️
خرید از ساعت ۱۱:۴۵ تا ۱۷:۰۰ و با جست‌وجوی نماد «رز ترنج» در تمام کارگزاری‌ها امکان‌پذیر است.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/675436" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
نتانیاهو: با ترامپ درباره ایران گفتگو خواهم کرد
🔹
نخست‌وزیر رژیم صهیونیستی از برنامه خود برای سفر به واشنگتن و گفت‌وگو با رئیس‌جمهور آمریکا درباره ایران خبر داد و هم‌زمان اعلام کرد که این رژیم آمادگی دارد دامنه اقدامات خود در کرانه باختری را گسترش دهد.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/675435" target="_blank">📅 15:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پژوهش بزرگ محققان: دغدغه مالی مداوم می‌تواند مغز شما را زودتر پیر کند
🔹
تحقیق جدید نشان می‌دهد که نگرانی مداوم درباره اجاره‌خانه، قبض و هزینه‌های زندگی می‌تواند ساختار فیزیکی مغز را تغییر دهد.
🔹
این مطالعه گسترده و چنددهه‌ای نشان می‌دهد که استرس و مشکلات مالی مداوم در دوران جوانی و میان‌سالی می‌تواند به روند پیری مغز سرعت ببخشد و خطر ابتلا به زوال عقل و آلزایمر را افزایش دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/675434" target="_blank">📅 14:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQBhPGvNJaSHLf1q2fCdUQxmYkTe5uj4Rx5P93S9IbuU3g3r58qrrqf9k9GgSrWBmUJP5-x4DxPGdOda-Qf8CHNXmtlBTKVTBQiScEwFMLCD7R_L2Oxn4jfFQ5atUYWRyNAp-RTdGo-tLVFdHcGh4p-E9wBhVZuX8aY7RWadCBAK666otwIAcJHy4PTB5I6aGR7KRcaOP8Xw7ZIDOiP1qFA5KGARNcVsTe_-SRTqbnXvYHWqK7rRXXVKTy_7szEJ9c8cW3qR-CqlNjJCgckKA5WNgWp3XRkheibz9YnEtHuZdEiOKZ0TbR2cseS8QY4VJ1UdA_RT6ucPm7m_Pqtxlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
زیارت به نیابت رهبر شهید
◾️
همین حالا با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲، شانس خود را برای ۱۰۰۱ سفر کربلا امتحان کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/675433" target="_blank">📅 14:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dc35f548.mp4?token=o2OgC-V9uCJPVZX9PttaAvsXtOnUCmZ3QkNUBV-qxjxhYAgwigbBPdhwNdGFN1mtCnEgbXJt_UIf7PnGqWJzA4d4PLddBpIu-IX6b_ohKb7nKzDWaj_qUGxFz-DUtL-7x_OVG7LHuLwN3Uyoa-mLR6HXfNYFg0hZmS1sYOpQX391KPv8wDBKKtQ4G5P0vC-09FxipmQ4Nuu-mYcF-isTw5NBwgkSJ2iJYB3eEfkcn6DPMOlZ47NXwvH6RsZXeYg3-a_0XhPHxKusHsq2wmw9zT8xShhRS1QDWvXjD5U3JRbpRN8wEXGBfMJMjX19_TLZ4Tmyf65O-V34myL7CZNF4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dc35f548.mp4?token=o2OgC-V9uCJPVZX9PttaAvsXtOnUCmZ3QkNUBV-qxjxhYAgwigbBPdhwNdGFN1mtCnEgbXJt_UIf7PnGqWJzA4d4PLddBpIu-IX6b_ohKb7nKzDWaj_qUGxFz-DUtL-7x_OVG7LHuLwN3Uyoa-mLR6HXfNYFg0hZmS1sYOpQX391KPv8wDBKKtQ4G5P0vC-09FxipmQ4Nuu-mYcF-isTw5NBwgkSJ2iJYB3eEfkcn6DPMOlZ47NXwvH6RsZXeYg3-a_0XhPHxKusHsq2wmw9zT8xShhRS1QDWvXjD5U3JRbpRN8wEXGBfMJMjX19_TLZ4Tmyf65O-V34myL7CZNF4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوای خانه را اهل خانه حل می‌کنند؛ بیرون از این خانه، کسی دلسوز ما نیست #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/675432" target="_blank">📅 14:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675431">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04731b9058.mp4?token=WgPoIa60sI8kd5lEyE3Zvbcm1JTqcNJnrzPCVr4ZXwP24tWVeGEaGKpvY-LMTEblfMxoJMLIHUROkuOEyPFaYHE9VtR8Gi0DAyzyHmw2WcM4tmwg2K-6FLmxvjoyfD_m0Sk8ld8CmYnkAIZTrtBdN_GzS6BbMsHOlLLeFb7qVevBwUeWSxLfGV3xJnjO2KYTBnlQtaM7mRazsFxi9DMdaMwno2fEuswejUj2_hUoQ6CIKOBdV5qnEQPiuAz8aeFTAwfeDV2gktpeSKMW_-KECOtXj4xsqxlhNf5hVimMMJAT5EF4v0c4_Nml62S1EHo-E4EAoqHKUhfSrL6dWgoCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04731b9058.mp4?token=WgPoIa60sI8kd5lEyE3Zvbcm1JTqcNJnrzPCVr4ZXwP24tWVeGEaGKpvY-LMTEblfMxoJMLIHUROkuOEyPFaYHE9VtR8Gi0DAyzyHmw2WcM4tmwg2K-6FLmxvjoyfD_m0Sk8ld8CmYnkAIZTrtBdN_GzS6BbMsHOlLLeFb7qVevBwUeWSxLfGV3xJnjO2KYTBnlQtaM7mRazsFxi9DMdaMwno2fEuswejUj2_hUoQ6CIKOBdV5qnEQPiuAz8aeFTAwfeDV2gktpeSKMW_-KECOtXj4xsqxlhNf5hVimMMJAT5EF4v0c4_Nml62S1EHo-E4EAoqHKUhfSrL6dWgoCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف‌قراردادن کشتی ترکیه‌ای توسط روسیه
🔹
یک کشتی باری تحت مدیریت یک شرکت ترکیه‌ای در نزدیکی منطقهٔ اودسا در سواحل دریای سیاه اوکراین هدف حملهٔ یک پهپاد روسی قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/675431" target="_blank">📅 14:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27a6d3475.mp4?token=TpDFfkfBwYDhHxc58IfJckh-4gBDZQ5uiLCd67JQAfVSI9mudODUhcSC_05Icp7pqjKTpUzy7xj3V0VN9vTEz_-UACBdqtR1U158yVAh_oYxfSQhT7ZxlXIWVaxezM9AuGpRC_aDlv6UUclDR6p1QZFwiPOuj_Y-bPxCwJ1cZFc0W4kWKKYcgKrekXPit3PZSr9NbZWzNr9ZHHTR-I5X7PSJYclN-9Q4-of8eFAfY9e3r9HAD3vXEmhYyjaFetW1WXrU-bFiacItwKuQ0eN-ezMAW2uD6CrBaBytvwGxOQSmBD4f9hx-yfkpJ6CRnDivaYzGlnPsDqtylEtVlnMgYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27a6d3475.mp4?token=TpDFfkfBwYDhHxc58IfJckh-4gBDZQ5uiLCd67JQAfVSI9mudODUhcSC_05Icp7pqjKTpUzy7xj3V0VN9vTEz_-UACBdqtR1U158yVAh_oYxfSQhT7ZxlXIWVaxezM9AuGpRC_aDlv6UUclDR6p1QZFwiPOuj_Y-bPxCwJ1cZFc0W4kWKKYcgKrekXPit3PZSr9NbZWzNr9ZHHTR-I5X7PSJYclN-9Q4-of8eFAfY9e3r9HAD3vXEmhYyjaFetW1WXrU-bFiacItwKuQ0eN-ezMAW2uD6CrBaBytvwGxOQSmBD4f9hx-yfkpJ6CRnDivaYzGlnPsDqtylEtVlnMgYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات همبستگی با مردم غزه درمیلان ایتالیا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/675430" target="_blank">📅 14:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تردد بیش از یک میلیون و دویست هزار زائر از مرزهای اربعینی
سردار منتظرالمهدی، سخنگوی پلیس:
🔹
در بازه زمانی ۱۰ روزه از آغاز ماه صفر تاکنون، شاهد عزیمت ۹۳۰ هزار زائر به کشور عراق بوده‌ایم که این حجم از عبور با مدیریت دقیق و انضباط کامل همراه بوده است.
🔹
از این تعداد، ۷۵۰ هزار زائر ایرانی و ۱۸۰ هزار تبعه خارجی، مرزهای کشور را به مقصد عتبات عالیات ترک کرده‌اند.
🔹
در همین بازه، شاهد بازگشت ۲۰۰ هزار زائر ایرانی و ۸۵ هزار تبعه خارجی به کشور هستیم که نشان‌دهنده الگوی صحیح توزیع سفر در مسیر بازگشت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/675429" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675428">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خسارت شدید به ۴۰ تا ۷۰ درصد کشت پاییزه گندم در جنوب کشور
هاشم خنفری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
کاهش بارندگی و گرمای شدید تا ۵۳ درجه در جنوب کشور خسارت سنگینی به کشاورزی وارد کرده است و به طور کلی بین ۴۰ تا ۷۰ درصد کشت‌های پاییزه گندم در مناطق جنوبی با خسارت مواجه شده‌اند.
🔹
باران دیرهنگام و همزمان با تلقیح خوشه‌های خرما باعث ریزش محصول شده و شوری آب تالاب‌ها نیز آسیب را تشدید کرده است. تالاب‌ها به دلیل کاهش شدید آب و افزایش دما با بحران روبه‌رو است و این موضوع سرمایه اقتصادی منطقه جنوب را تهدید می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/675428" target="_blank">📅 14:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
فرزندآوری بعد از ۴۰ سالگی در آمریکا بیشتر از دوران جوانی شده است
🔹
آمارها نشان می‌دهد در آمریکا، تعداد زنانی که بعد از ۴۰ سالگی بچه‌دار می‌شوند، حالا از تعداد مادران جوان بیشتر شده است.
🔹
بسیاری از افراد ترجیح می‌دهند ابتدا درس و کار خود را به سرانجام برسانند، از نظر مالی شرایط بهتری پیدا کنند و سپس برای بچه‌دار شدن تصمیم بگیرند. همچنین پیشرفت روش‌های درمان ناباروری باعث شده زنان بیشتری بتوانند در سنین بالاتر باردار شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/675424" target="_blank">📅 14:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک توسعه صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4IK4S_bWgYaMH-R1FiCdLifUn9F874NuDJWoivDLnizIW9DAU-XSXJRBPd6Zx6cfrlJNgOMnCoOi2nGjPzMTgsHQnVWOZf1uLjasd6YYY3OIV5pauOktGezkyrwCLoPIS1RnNFXblnGYHX4kkNnApLWpPN6qqjTHKJ32XXzfDrbjyH72q0vMyvKTksVqoIDK-iakbXkt2XlRV-rMRSBMjbFuGAlnMy1Y9930fTH1nz54X6mToocFFven891e5DRYdTHn7-ryzzvn62t4wK1vpxDkGbhwpQfR7ZEdmoGFaoNetCV348VI-tzgyiWUQ8U4amuMzaWnIoGNfoXWpFoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">↗️
افزایش
حمایت از تولید در بانک توسعه صادرات ایران
🟢
بانک توسعه صادرات ایران در راستای افزایش حمایت از تولید و تقویت بنگاه‌های اقتصادی، عملکرد موفقی را در سه ماه نخست سال ۱۴۰۵ به ثبت رساند
🔹
گشایش اعتبارات اسنادی داخلی این بانک در سه ماهه نخست امسال نسبت به مدت مشابه سال قبل ۲۰ درصد رشد کرد.
🔹
این بانک در سه ماه اول امسال موفق به گشایش اعتبار اسنادی داخلی به مبلغ ۵۶ هزار و ۶۲۷ میلیارد ریال شد.
🔹
این رقم در مدت مشابه سال ۱۴۰۴ معادل ۴۷ هزار و ۱۰۰ میلیارد ریال بوده است.
✅
این رشد نشان‌دهنده عزم جدی بانک توسعه صادرات ایران برای گسترش خدمت‌رسانی به تجار، بازرگانان و فعالان حوزه تولید است.
🔗
مشروح خبر
🟢
سایت
|
تلگرام
|
بله
|
روبیکا
|
اینستاگرام
|
آپارات</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/675423" target="_blank">📅 14:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8b32939c2.mp4?token=YXC7AapY2iX0EZmwb7YbC0e2dHlUpGmEZfsKNZZKGPIUpcjqZPvIJz7taNbZaDDl4wF3_QuVH0zRBI3XRZx0TzFFuCGth9RmLlDkZ7HWV3RUAn0oWjCLN2tiQgNcXy-ii1GkMVvadqi8omJdo6Li7Ys72g1M7dLQ_PWHnODYeOPr_d5JhTarqm1FA7U-HzOA9CYpYsiLRihZpLd0vItvJPlHRNppCngsQSBKt97WcfFF7QhJgda4oawZJTY8V-ChrYGEyRvGJBevCvDXRWg_UI8BOqhv0AhfPAQ1nD9vbpup88xmYX3EDyofGnb78JQkxya2rxuFHqjc9wkFryqupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8b32939c2.mp4?token=YXC7AapY2iX0EZmwb7YbC0e2dHlUpGmEZfsKNZZKGPIUpcjqZPvIJz7taNbZaDDl4wF3_QuVH0zRBI3XRZx0TzFFuCGth9RmLlDkZ7HWV3RUAn0oWjCLN2tiQgNcXy-ii1GkMVvadqi8omJdo6Li7Ys72g1M7dLQ_PWHnODYeOPr_d5JhTarqm1FA7U-HzOA9CYpYsiLRihZpLd0vItvJPlHRNppCngsQSBKt97WcfFF7QhJgda4oawZJTY8V-ChrYGEyRvGJBevCvDXRWg_UI8BOqhv0AhfPAQ1nD9vbpup88xmYX3EDyofGnb78JQkxya2rxuFHqjc9wkFryqupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی متفاوت از طبیعت بکرِ ییلاقاتِ تالشِ گیلان
ییلاق ناوان، روستای مَکَش
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/675422" target="_blank">📅 14:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
خبرگزاری آناتولی: پاکستان و قطر تبادل پیام‌ها میان آمریکا و ایران را تشدید کرده‌اند
🔹
میانجی‌ها آتش‌بسی دو هفته‌ای را پیشنهاد می‌کند؛ واشنگتن و تهران در صورت موافقت، بلافاصله مذاکرات را از سر می‌گیرند و آتش‌بس در جنوب لبنان در صدر دستور کار قرار خواهد گرفت/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/675421" target="_blank">📅 14:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1c74d1fa.mp4?token=H9J8W326wg3QzRnsFMFLnl4f_MzvYm41l6L2NQG1LaubYLXLuS5N4AdoduIyHp75ByW3QqevP0fCZIaeoZliDnjX7atYLPk_qDfXvyv18CTmBKmRwMetnokAzmWv7h8gtQAZlNa_UPivMQvUxzARBmaJn-tTbmlX_mhu7jZLP1rlxBuv4ucB-ctJFtH4IvuHO84OVRbfPPUw16a9KrhKZPOaROS6iJXiv1UnaRoVrPSJoXRumSdYbD5oTTHeIV7gH8LtyM5p_7DpwLaToRhYHq0LCzcGXuo0quhTB0BOS_HaRpWwiC8IHdT4DJeScIeHBlIFLvJzJj8lclwClaZzEpuDhr90PtHaCDqejRriE5pHZtg_FCLUzlU2ap4unx2woBImGo_CZbaS908ZRi7Gz2nlOG9f4oeffSPVIp0FC6RQCvqrb3taPpBGFyIe4M3-2DDRrZcGli7LskTxWs-uS514Ee1bIjwe0bSQUHijiQpHhDMpUraFPg4w1ek7c2JpD_3HckXwROgO8DE2D-57gV51Zq75Dybbxxo-I6rP3PinSJixr4Mh4gi8KXlhZrC3lG4-YfOM3vwFAXfKiEIBW2iX55RO--OzVJ3qEWEXmfWA90mCpYuFi2G-VfbWRtoQDiiU3PKsiA819hEKzFFaUX_Jm4qLbUQ9AOEUjTeRo68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1c74d1fa.mp4?token=H9J8W326wg3QzRnsFMFLnl4f_MzvYm41l6L2NQG1LaubYLXLuS5N4AdoduIyHp75ByW3QqevP0fCZIaeoZliDnjX7atYLPk_qDfXvyv18CTmBKmRwMetnokAzmWv7h8gtQAZlNa_UPivMQvUxzARBmaJn-tTbmlX_mhu7jZLP1rlxBuv4ucB-ctJFtH4IvuHO84OVRbfPPUw16a9KrhKZPOaROS6iJXiv1UnaRoVrPSJoXRumSdYbD5oTTHeIV7gH8LtyM5p_7DpwLaToRhYHq0LCzcGXuo0quhTB0BOS_HaRpWwiC8IHdT4DJeScIeHBlIFLvJzJj8lclwClaZzEpuDhr90PtHaCDqejRriE5pHZtg_FCLUzlU2ap4unx2woBImGo_CZbaS908ZRi7Gz2nlOG9f4oeffSPVIp0FC6RQCvqrb3taPpBGFyIe4M3-2DDRrZcGli7LskTxWs-uS514Ee1bIjwe0bSQUHijiQpHhDMpUraFPg4w1ek7c2JpD_3HckXwROgO8DE2D-57gV51Zq75Dybbxxo-I6rP3PinSJixr4Mh4gi8KXlhZrC3lG4-YfOM3vwFAXfKiEIBW2iX55RO--OzVJ3qEWEXmfWA90mCpYuFi2G-VfbWRtoQDiiU3PKsiA819hEKzFFaUX_Jm4qLbUQ9AOEUjTeRo68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاروان کشتی‌های متوقف‌شده در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/675420" target="_blank">📅 14:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a995cdd107.mp4?token=eMA1L-xOcbp0sOJv9khq6iVO0vL064snST1ZxAsBc35pqiN8tLin5_Fg-cHA1s4-Yn-MP3LKaNcoPrFnI-4voaE7HKjTQo7h-XWI4uBsBgyQ2v3HJiNiqLfkW2-e2Rg2RfE563Y8X8RSapbZFfDcUn7ascvS2xFvu7jmNuxsZxTWQhiCsGMkfWihZ5R2zzOrR7duurE8ZQSxH85WqAZ_xS5068XUWU_DeIFAAHF8Ltpnm8jFnQgOAeKuKS8zzUqofOtihCK4QXoRSQPTiHeclzwSyKTy8iRGANBqiErlfonCpqvIU6mRbgPcMnw4prFFpZU80I2Vjc2JiPivgYxYB4Yqyprk9uFoBZD37We1pl0AwlX-xN3S0TC5LxrcURZ6uCPHxTDakJZqAYXL8wk4IJyGNgqUFEk7oo3h9LwesuhDJzQ5_KnlLlHXGXZMt27yQJDJLqHVTSI-0jw-8i3DI5VdL8sLFT7ZANng_EMdLZzv7o7Fxf3Y47SD4zpDERQxyngAbpqavgxDFXvQWdsL6XnNpVT_3AMukoXVL01yWegD_4FJ3dsKm14kVgCne_K1ZleEoFzZGjzWADSMIfvAzlMHg-4ShYYFoKxyZLHrwiscwMFuOgAis0OCRNfCIe0Rvu89UVn6mpX5w8zhNKUuyb5R_725G0h19zPef3uZ75Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a995cdd107.mp4?token=eMA1L-xOcbp0sOJv9khq6iVO0vL064snST1ZxAsBc35pqiN8tLin5_Fg-cHA1s4-Yn-MP3LKaNcoPrFnI-4voaE7HKjTQo7h-XWI4uBsBgyQ2v3HJiNiqLfkW2-e2Rg2RfE563Y8X8RSapbZFfDcUn7ascvS2xFvu7jmNuxsZxTWQhiCsGMkfWihZ5R2zzOrR7duurE8ZQSxH85WqAZ_xS5068XUWU_DeIFAAHF8Ltpnm8jFnQgOAeKuKS8zzUqofOtihCK4QXoRSQPTiHeclzwSyKTy8iRGANBqiErlfonCpqvIU6mRbgPcMnw4prFFpZU80I2Vjc2JiPivgYxYB4Yqyprk9uFoBZD37We1pl0AwlX-xN3S0TC5LxrcURZ6uCPHxTDakJZqAYXL8wk4IJyGNgqUFEk7oo3h9LwesuhDJzQ5_KnlLlHXGXZMt27yQJDJLqHVTSI-0jw-8i3DI5VdL8sLFT7ZANng_EMdLZzv7o7Fxf3Y47SD4zpDERQxyngAbpqavgxDFXvQWdsL6XnNpVT_3AMukoXVL01yWegD_4FJ3dsKm14kVgCne_K1ZleEoFzZGjzWADSMIfvAzlMHg-4ShYYFoKxyZLHrwiscwMFuOgAis0OCRNfCIe0Rvu89UVn6mpX5w8zhNKUuyb5R_725G0h19zPef3uZ75Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت سیزدهم از فصل پنجم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ خانم نرجس اربابی که بعد از ورود به دنیای برزخی در کنار یک همراه، شاهد نگرانی خانواده و همسرش می‌شود و به تکرار، رفتن کامل و مرگ حتمی را طلب می‌کند و ۷ روز متوالی از آب روانی که توسط بانویی به ایشان داده می‌شود، می‌نوشد و در این میان شاهد عذاب افرادی که مال حلال و حرام را رعایت نکرده و همچنین دوخته شدن دهان افراد بد دهن را درک و مشاهده می‌کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نرجس اربابی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/675419" target="_blank">📅 14:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675418">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8884c8a3.mp4?token=lybra3h9ZAqsIlJt6iPu_xvb0EhXL24ONZIWk_hcxIzN8Io4pY-xY-NcEZniDdWGuw52kG9DcnkIuOuCPUfK7IOwb00xuoAUGZSNRDtf6Iv5aCFo_EnEufeWoEqMSOF8q-ChPtqh943qPIq7S337u4ldkc3fOJos3825cXmg8ZsCF01ON8IB03AGnPpJjxSvTHgt9RAqHGr77vcBzfMrvQ1gxKhglhHPSzfDXg3Z6TpNBWiZNIhWx-QqQMME8zK2eI04bah0FKbr8cQo_KdXdp6LNwDNtlP1hJnAiOxUo2xEyecjYhahiP_-R2hQo-9wl77jHdO_9INRHAhs97rGc1TdRVXEIKIdaJrSMR4JjWO5eMti98DB_ytZe9DDEEHU5ADzn_hcD33DLlXZStIN8JYtMigkgMmq251UcL2plj21Nk5vBAVt3E4jw6VZM-WTg0bbtE_pDw6_BL6qnnRigqefJuvTejoIe0kXVdeIMR_fNw_1V0hFH-8IG2ngcfl9M-2WbM7RJ7mfeDTVfRY1UAlHtT_uJx_sV_IVr9jz6QHmkoR3r4EJT6LfKwlXGx084aibRNUO6SkZcsNqh7mbXJfQmkYG1O7OveJxYHr4sAmXAnOb2Tpc3t7LeJPjA1aRU2sXG0AFxY4YXI5I7JFNwVfOOGPOEpOuz4MEZc2zXJk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8884c8a3.mp4?token=lybra3h9ZAqsIlJt6iPu_xvb0EhXL24ONZIWk_hcxIzN8Io4pY-xY-NcEZniDdWGuw52kG9DcnkIuOuCPUfK7IOwb00xuoAUGZSNRDtf6Iv5aCFo_EnEufeWoEqMSOF8q-ChPtqh943qPIq7S337u4ldkc3fOJos3825cXmg8ZsCF01ON8IB03AGnPpJjxSvTHgt9RAqHGr77vcBzfMrvQ1gxKhglhHPSzfDXg3Z6TpNBWiZNIhWx-QqQMME8zK2eI04bah0FKbr8cQo_KdXdp6LNwDNtlP1hJnAiOxUo2xEyecjYhahiP_-R2hQo-9wl77jHdO_9INRHAhs97rGc1TdRVXEIKIdaJrSMR4JjWO5eMti98DB_ytZe9DDEEHU5ADzn_hcD33DLlXZStIN8JYtMigkgMmq251UcL2plj21Nk5vBAVt3E4jw6VZM-WTg0bbtE_pDw6_BL6qnnRigqefJuvTejoIe0kXVdeIMR_fNw_1V0hFH-8IG2ngcfl9M-2WbM7RJ7mfeDTVfRY1UAlHtT_uJx_sV_IVr9jz6QHmkoR3r4EJT6LfKwlXGx084aibRNUO6SkZcsNqh7mbXJfQmkYG1O7OveJxYHr4sAmXAnOb2Tpc3t7LeJPjA1aRU2sXG0AFxY4YXI5I7JFNwVfOOGPOEpOuz4MEZc2zXJk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روی این پل، دو ایرانی به شهادت رسیدند
🔹
حضور خبرنگار خبرفوری روی پل رودان به بندرعباس که توسط آمریکا مورد حمله قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/675418" target="_blank">📅 14:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675417">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
دستور تازه شورای رقابت به خودروسازان/ شفاف‌سازی قراردادها الزامی شد
🔹
شورای رقابت طی نامه‌ای به خودروسازان خواستار رعایت شفافیت در عرضه خودروسازان هنگام انعقاد قرارداد شد و تاکید کرد که مراتب عدم شمولیت مصوبه ۴۷۳ درخصوص قراردادهای مشارکت در تولید، در فراخوان‌های صادره و قراردادهای تنظیمی قید شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/675417" target="_blank">📅 14:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675416">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af46fd431.mp4?token=t8EayKdJfqmYu-1JMD1qirOltZIK1RY0cB3egm4w3NvlvWQKdbiStVwSOwbwNdh7v10DLZqjy6auSwRwYUhpPkfxygagGiW8gY_F_5YM-ujQ4XJxXEvo4Vwf9rwaaGFrPvYK83AirmWccikYogAjJ8oeFY-YDs4UeMGNBJ1vJ9ozXFSzJHwS-176JcbDIqPx6uWR9mwBybuqe7XVJBO5xDjCsD8rsLhpyBuuFSiAL-X_PJaMGyIS_c8SeaT9s6OoQB6RxL208RCRaDLq-nd2gYqkaz_KzSCMhjFVoyRpzPxNI4h2nyOs-lFx0U8QLaw8gTrLMQRnWJD1oAlCYNGBWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af46fd431.mp4?token=t8EayKdJfqmYu-1JMD1qirOltZIK1RY0cB3egm4w3NvlvWQKdbiStVwSOwbwNdh7v10DLZqjy6auSwRwYUhpPkfxygagGiW8gY_F_5YM-ujQ4XJxXEvo4Vwf9rwaaGFrPvYK83AirmWccikYogAjJ8oeFY-YDs4UeMGNBJ1vJ9ozXFSzJHwS-176JcbDIqPx6uWR9mwBybuqe7XVJBO5xDjCsD8rsLhpyBuuFSiAL-X_PJaMGyIS_c8SeaT9s6OoQB6RxL208RCRaDLq-nd2gYqkaz_KzSCMhjFVoyRpzPxNI4h2nyOs-lFx0U8QLaw8gTrLMQRnWJD1oAlCYNGBWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
قطعی برق؟ نذار گوشی‌ات خاموش بشه!
این روزها با قطعی‌های برق، داشتن یه پاوربانک دیگه یه وسیله لوکس نیست، یه ضرورته!
🔋
پاوربانک شیائومی با ظرفیت واقعی 5000 میلی‌آمپر، همیشه خیالت رو از بابت شارژ گوشی و گجت‌هات راحت می‌کنه.
✅
ظرفیت واقعی ۵۰۰۰ میلی‌آمپر (یه همراه مطمئن برای شارژ روزانه)
✅
نمایشگر LED دقیق (دیگه نگران خالی شدن ناگهانی نباش!)
✅
ایمن و مطمئن (مجهز به مدار محافظ در برابر نوسان برق)
✅
خوش‌دست و جیبی (وزن سبک و طراحی شیک)
✅
مناسب برای شارژ گوشی، هندزفری، ساعت هوشمند و سایر دستگاه‌ها
قیمت قبل: 1,998,000 تومان
❌
🔥
قیمت ویژه: 1,598,000 تومان
✅
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
📦
با توجه به قطعی‌های مکرر برق، این پاوربانک می‌تونه همیشه یه منبع انرژی مطمئن کنار دستت باشه. فرصت تخفیف رو از دست نده!
https://memarket24.ir/product/brief/60476/180124/</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/675416" target="_blank">📅 14:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqDvxCI5i4nfCdMOMInre9L7LESg2gKqoXcOrF0nOrgvDIi6wkfhE6emxrHdoUtNHTOotxowKDC66egOqEOhjexEf4mbxz0vTqw5CzR3xMCnP-C4k5nqFd95H0pWz71wETJR29t888hRgceYS0MuSwDjsPJ3UeBT03Mh-fJSMF2YSdjgrZNE2wDy9SSC4SLjL46c7Kcl7VlhzyL7qYv9GHp3oViMDvNYetA8yv8M2hQio_PVpwslQafCRZV-LBVYp8_szcqAk6w2rRkRUkboKAWRkN537NiDQGGdUs8qk6a982P9j0DE1VN7VKWimdKqCV6fQmRdQcrqjBuncQUZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDC4Zf1UFn7DSTjSH2vE1h98wVEme-0Ge9JIzROvZdRhp5U81r1wmLUSRlpF6d5PFTdt9O26IBmTe0Z3nQjnXgmyBTNzDcqkGOeTiJreqqvH5311mghpagYvq1ESoLN3k7LWJpEOe5K1U6IF8mr4SwxVRF3ZtuD_azxWGRHvZ7IPd1QRM-WXhxs6PdRLIVm7SoPvjxrhtXrlTFCgDUj47y3SIm43Qc97hUHdRZIgQrPksCWFyKAjhCSjMFwhDfFUVKyJKg9EnoO69AqcITs09Hy8-EHJWiU0T_1xt9RSH-ejGxQfXbJjnp1qZuCSTllUeuWxOYXYhqcokA2x-eD66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t07unvZ7Sa3djr1twPKtDVjp3ZpZckn0bbNdzRMi6hta-5zQ16X5CQNzoPUMOeLZH57xHN1jgfrpvG0zZL5w7pi_ao-lCVpk768GKxixSxSYrk7r9vzAm1sVbOVk8gdnD00J2kx4fx2MJzVVKAhPAr8k-gMUwTIVyVhafkfpiz8JkHUM7KO59WT-s9Y8R3IL4hBZ1P8Vig-JVhb6KAcBk-oP65RpggcgsP9DoL8IUxRQCKbz4KgAfZ0vMzSvoi-IR77rSh67A20bi9ogOFyiLzT3zQDCcBYUgJ68jmesns1k6gQJf8zE7gLHL6M4pNV_vQLovWQ3S7w5T-WM10WWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qv5fR15xZ79Ieiza5ARDqwzRHIRUk4fj9CNYvQ9WEffNWlX6xTUJiPR--hOYmimAxMEeW9cqNlfiweiQ2zFQYIBx8sbZDAkih7O4GpIbVjIStRHgIklQ9TrdDxLZJl8bifSDsqbicQLNu1t3gvnNvBlSbRmyJGdwOm7AL7EVJbfKgsS3No-dxmzsgnpoLP0BWBM52GK3i-345BKPTFYPlPf-eU4t0CKMnWVtGdys9u3OLODRNmhR-XTxv9RsXImiu94HlFxJy8zVdHcaNGUWYzl0m_64ZeTOelprSMa-l6QUiwPO3SuvuiCESQpKZlMqkaVBv_GmCk3DtFwHLl6SYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEGfgSbwBP4R8CH-9wixFHTMYJYt_gEamsdyL2Z4WIqLrxj3_wWuJJw8bG7SIdq0HoHo1CBoOc-BjASKA-G0sPSU585XND7GrlLR5BYjOAjqBxYl9nTdQcVC2kXXbF-3It88M30ZYThqbsPi5ferraDH8vxLGgWPW9vNKhSrFnLrcJ3EZ8-1pkDXQ-k_YnDOnQNnqaQ0tpysN4Q61qoT76BVF0MCcXPmzHcnLwcBNIvShIFt9hjyGIdEobCuVh-cLpJQmrR-fErc6d3RqREX83YETUM7D05qR6iw6x2hVyi5qzHeldSKHukYB0rNtzY3XdgCsWf-Zp6XuL-2-BtTCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از مسجد الرحمه در جنوب نابلس که توسط صهیونیست‌ها به آتش‌ کشیده شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/675411" target="_blank">📅 14:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75623e9328.mp4?token=DTr1glOhMsUUXmvpxuq8LggAL9_SbwF8EfYaJlop22pMrtYX1Fdyk94a-4MJjGhBMrA2bB6U1fgdu2tSlVki0ge_uS4uIznBmeD8MIbYa-hfvc8cCe4F9r60XVb1bKzJJ1Q-QFMSP78iAYZw8-IOkn6z14F767WIrtBS5LylshiSDdSFBblKQiqwjkP_z0dBi-kPZv43bDKtEPa2-NHAdi8V9Bur1MdGbSOSjqQJ8HDpRDZPHYhJqXeRhELbhK2L8QfAh59YIC9T8VzZJcBQ3_yCFCi_K74kCeLm_VJo5XRgYdVCp2FqRCuka7B64Y7E_hoeZnh1_tbd-7QBnlwDQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75623e9328.mp4?token=DTr1glOhMsUUXmvpxuq8LggAL9_SbwF8EfYaJlop22pMrtYX1Fdyk94a-4MJjGhBMrA2bB6U1fgdu2tSlVki0ge_uS4uIznBmeD8MIbYa-hfvc8cCe4F9r60XVb1bKzJJ1Q-QFMSP78iAYZw8-IOkn6z14F767WIrtBS5LylshiSDdSFBblKQiqwjkP_z0dBi-kPZv43bDKtEPa2-NHAdi8V9Bur1MdGbSOSjqQJ8HDpRDZPHYhJqXeRhELbhK2L8QfAh59YIC9T8VzZJcBQ3_yCFCi_K74kCeLm_VJo5XRgYdVCp2FqRCuka7B64Y7E_hoeZnh1_tbd-7QBnlwDQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت اشک و گریه‌ هاش این بود که می‌گفت از امام حسین(ع) خجالت می‌کشیم که فقط با آب میتونیم از زوارش پذیرایی کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/675410" target="_blank">📅 13:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077e4d4ba3.mp4?token=aEGDcvb11vaPnRqHAXf4Dpi6SSWLfiy-xV6Rabx3Rw40g4uBJ_E5KkqiWNvVvW6osiRPw7Xka-iilqViQXQraYq3UhQTY6MzFfpazDxc4P-Ie5ojGlVFQGF-usx2C4t12m8W2hE7H6wAhBp2g_NWpDC4s2UT1W0B9TfTd-xq6b3k28-WH7Ktnq0xIYoDCbz_FVbXhS9OwXWf7ZAkSn_BAQJees9PCOf6fm7uFTFr2Mg4n2Bv3wwfQXa0vyxxhpIpf4-01T66wOthJC0PaQGxQBoRWcauN2I_Vq7fBpEHKrVpwTvLCieodAT3LJikeyDDBLrLV8IudI3BeFAg-av-cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077e4d4ba3.mp4?token=aEGDcvb11vaPnRqHAXf4Dpi6SSWLfiy-xV6Rabx3Rw40g4uBJ_E5KkqiWNvVvW6osiRPw7Xka-iilqViQXQraYq3UhQTY6MzFfpazDxc4P-Ie5ojGlVFQGF-usx2C4t12m8W2hE7H6wAhBp2g_NWpDC4s2UT1W0B9TfTd-xq6b3k28-WH7Ktnq0xIYoDCbz_FVbXhS9OwXWf7ZAkSn_BAQJees9PCOf6fm7uFTFr2Mg4n2Bv3wwfQXa0vyxxhpIpf4-01T66wOthJC0PaQGxQBoRWcauN2I_Vq7fBpEHKrVpwTvLCieodAT3LJikeyDDBLrLV8IudI3BeFAg-av-cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسر بایدن خطاب به ترامپ: چرا انقدر عوضی هستی؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/675409" target="_blank">📅 13:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lrs7E0HgnbG6WTRaH9PWDR0aTkdx1KBt522kCEMJykcEhjPQHGVjQDugb1hVVwuoz44GFJbJhoGBSrg4GEjV6IeO1ExuFHk1rjy6mf_lGUl26I4yz_tKIkphz3FA3lM7LoULqE0kCgY02t-kcIIngjiV6TUdl1dVMLjicXLCw9qLy6SqZnHv2w_hsraSFWwS8fkQKOSpTt6Ut9ETgopT9mqgyonLUozmEMOzBwqRpNhys2SvWu9vqaHXNonHQSEXdsBtuaT-MNVfm64m3XRrKkYLTPJLKXG6owKnyS_ergqYUU6azEBNq_8Uw-rHgDrr0vsCj4b_U4bmv3uJHE7YAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZspfMHRvkf1WRw8FAn3RFBzNQWS5JjftMKbg1XMkDmKIK4Sfa8LsvZfbKqe7x66_5dXVvodekLspsZ_Ibop6T9bwIrYkVsGvUkbwlWbU445tQIxh5Hedob6XEm52ccSgy8nBCOT4VSWRljJouG3_JVFFgfs-UNZi2TZY57CJGqPISRsKbkItBTwz4XFnG9w6y3omSzeD1DpMnx2X-fviFbfFh187R0vabTma6DU3JUaG20CVQwmGf5pO-IPpbZrMmdUzOx0_uuCG_BuvE_kukz5eXiBIEaYtmwMjXML55MX0iYxemQ_3rE7cHuTn7kTLCK7a-iNtf0J9G6UDX0x9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZDrOCOXfPe7zoRWLp6tQsp-6zpovgv9ZCh3xKWWcDNwcQSRRNf0q4t7prXSUhM0uk2tWXFT8WxBxm1lgIjwyHvxy5m3REMvwesgxWQ2caPfgpItDKSIQ2dGax0yCiUE8mcNZnLzUpkkF2T05b5pzm9RRBB008BO7eiyvEYhEYbAoOAX90nzknR5pZe_0T1Rg80GavDFP6t3VdJ6R5BkamK0K4AM1QcbRNytz6AljENkd1Skj4KMCGHlP1_OPomXb7FtbxOXjssVrrC6kI8Tk0MbQAYfO25DfsT3i9HbHRqNADuZLLsm2CiOkbE2Y5xlsfpIYmr3y2b2sxyuOgKIPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بلیت قطارهای اربعین چند؟
🔹
مشاهدات حاکی از این است که بلیت قطار برخی از مسیرهای پر تردد در ایام اربعین همچون مسیرهای تهران - کرمانشاه و تهران - خرمشهر بسته به نوع قطار از ۷۰۰ هزار تومان تا سه میلیون و ۱۶۰ هزار تومان عرضه می‌شود.
🔹
براین اساس، قیمت بلیت تهران - کرمانشاه برای قطار سه ستاره چهار تخته ۷۵۳ هزار و ۹۵۰ تومان، شش تخته ۷۰۳ هزار و ۳۵ تومان، قطار تهران - خرمشهر چهار ستاره چهار تخته یک میلیون و ۵۱۰ هزار تومان.
🔹
قیمت بلیت قطار پنج ستاره تهران - کرمانشاه نیز دو میلیون و ۳۰۰ هزار تومان و تهران - خرمشهر سه میلیون و ۱۶۰ تومان تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/675406" target="_blank">📅 13:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675401">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/If6KkaJZzrO5dHbfZZLt5-UOxUdqg5LxEyfZVKrdj0HYQrKh2MMqk-f7907Sucb0wCqeuhtlm30zG0Rl2vvHOAXqKeqaCHA7AkcVUmz8j22I0tllySofNAQWMnK6b1Fq7M1ppPim471ox91ZKXGZ9z-9PenCHB8nNc8T8DY9Ff5Oo3dy7bQ5v1bDZ6AdQSPizZGuC_dsEqcPYoqR2MEfy_XaF-54PkPRbMcphaD051k26MPHAdpu-VLZ9QNxmEUdKWXq3csm-mhqxKzb7ZfFVxRuR6wyd6Fk2o2_t6pLZ5f90AYRqOHhglIAhEMWZpfCTa5dYERfGvna2sFsOlGruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rp6mdGitLRSbkkzFAhiriLA_Fsm5Aynen_HeQFewOdHUujWlSILzRfqzD7q1tqSiDTcgnBrwU7vrMJ6wR975aSOw9SBKnmXyxqjrvZygpuRhzZxEYcIpqHfe0td8wNL7Gtgl905K5HJjsiEnyzCxoKTpm28matyhi66WLhwitSxfmp3D41jwwBsnNX1rO3dLjgFIMi34NvOamp9rZ8T-mQqmNLy3v0yoFkM_p5QzfEXx8cZx9SJnjYffLUTau6QvBrcMgR3rNZ3BxHiNWQC6nynSIqpIzF9_WnxOsMOnttvza0C7JwK-ftzpvNmucRwWXgWjjs3g1hLxbEH8GDFbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/orVQTWHiOMWIEVuXcFeUkkzOiLNL0C-GYIUVuYxeZVXUh2ZdbEWv7WimTzLCxdH9K4YWR5q-uTSOk3rRyuevYf0DsXkMMBdw_0DHbA9FAFYttBT1WpyKEh64p28Zi3H_a0hShWLownKIo7e9mzFOWfyTnUel8IqSyzRWmYfJnwqzS-YuwZipI4pT7yHcmAWWL2NEkHkFpkBM6uM4D0joP4TBOi12nVj5MzUsaiZkIdTptNjXahetIhd_wV6ESxLMxC5dtbVOAJ8mVsO2sTXYZzBd_jug1uQQM5HTDexxEdcR4zTzj7T6LWwEnHYWmaLv6KlLoFnD5byCXI8nvDDhPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گونی‌های اسکناس در بغداد/ کشف ۲۷ میلیارد دینار عراقی در پرونده معاون وزیر نفت عراق
🔹
بر اساس اعلام دستگاه قضایی عراق، ۲۷ میلیارد دینار عراقی در جریان تحقیقات مربوط به پرونده الجمیلی و افراد مرتبط با او کشف شده است.
🔹
بخشی از وجوه در اختیار افراد دیگر قرار داشت و بخش دیگری در مکان‌های مخفی از جمله داخل دیوار برخی منازل نگهداری می‌شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/675401" target="_blank">📅 13:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675400">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4G2Iw-s1NzVVPmDQNRk6-M4keT6CWueHPvf0Jn3XSgc_cutP7O-ooMk_8y6FpHAIs8qBvlWwpJCPk6XRtxk6zuCuVCIZ2GKL18sU5Pocx_CbzDG-4EA2IoewVlwCxzqqympqLvywc61OelJFs5_lEfVhgkqa3Wj-jpn8Kp675RgmXHBXndPqbgP5cykZK-KQPavEjw-w5qDKby-1ErFweJMq64r2dm81lsmK_6cKb-cpDRUOJlNYyKLhCm954m3RWzpvYTTEWcZ6ksBCGgQh9E56DaAxyVVddcxLKWyuslTInLay3hTeiI_D9zoan3YNS_ar9xgThHmw6tNATIvYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفندی ساده برای دیرتر رسیدن موز
🔹
اگر قسمت بالای موزها (ساقه‌ای که همه موزها به هم وصل هستند) را با یک تکه پلاستیک بپوشانید، ممکن است موزها چند روز بیشتر تازه بمانند.
🔹
دلیلش این است که موز از همین قسمت گازی به نام اتیلن آزاد می‌کند؛ گازی که باعث زودتر رسیدن میوه می‌شود. پوشاندن ساقه، انتشار این گاز را تا حدی کاهش می‌دهد و روند رسیدن موز را کمی کندتر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/675400" target="_blank">📅 13:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675392">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arOjLfw3vwJ_glCxMly-w05KiYyY2gvs60SCz5HMd9kiEnlfsZz0vHs5HtgftmeN1iLRFA6uwUG8agIg5ZECYEXdsPqw21DnIkC1xBtKaQcR8eFt2NsI_UP7ftk1kIAFYr9LCL8mqgN_y-AzChkj-gs5kmCXM6WpgxkwZk76ZPGfp-WFRkcluENKigBk-qvv5z5e70JCq1j1fdo-e4afh3vRgJewSYq0zRB7OCQpMIMGUXnaQzsnNVYhZQhaQLkh_ZkN8wvj0WQ3OvKtGwLnwxUgTVAgCBxgzEthNKk9UOW8u63QDX94X16w1HabrqP9fsXMjhwx3WqNgK1usd_EoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_zhSyezgA6_PsZJ2atGRMLg6ckAAljhanShjw_wWTAHIxbc0UxuNMXHxAEHcPLF_9kFZHHbyrPt321T7y3kqi9tetsK7kW0_YN0Pw8eaLoY_qph5LlL-vamWaKuwGqxx0tNslc2UK3364N9OXIkX98lSt_p8seYpnYCnDrFq_JOnuidYz1cAD1QQBV5reTrXQkb416-SkZJnasBqWcxA2FYTJ7KHh_1eTtIk-EyQSGRqObFftltgTlKFK3f2M6xUL2jYmVPdU9_2K9g7J_eyWb2_giyPLMaO9dTq7g3FuxERpYBgid7FH2lSHqYctlkjveQsmcEXDfEH0NEVT55XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xp0QqgC0y2iH_u-aw5WYyB3Pb8RsgaJRTR32B9p6NgAXE-knKzfLqyhEIDB0GTAgigArbGjn9cH2DFe-zF6LtFaEDR1ufpCKfXUS-7scEs8xiD0ozgZk2fYAfAnCmQK-dm6IGezNLyzr6VK83-eSeprVF2pp8YMjC67K-Pn5kN0fXEhqGM34pzYO4Dev_oQ9sUolhBnqpacyp6dMxvCH5YWTCMDZzBT3xRYIJA_WARYe2bQpERX-ZR0CFPIYqQTkjeODd83VYJITDEv2et8AJbQHFO6wU8nKKmbbLpCXuJjFKH8sR2oglccGRiwIpyiU8L89Z1tkjHhTJ0C624oCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubIDtp4K71Rh2DnEIYAQPveCPjfA1eQzfRyQEh8L1e0vXR5RTWc1PUw1PqwY99JKJgIq3Kf1t7XEsVuc5xLs7EA5UoqmoITY1kYOTG_hyzYWTTnK-y01FMkcEU0pW5RrJMrbtCh-u_OT6g8dWb4__OTEC4uOZr2UhM5oTkRLSqxK-WdZCcrFdZJm1ZF5NaSi5kpdIBuGpIujC-05zRCf5laLpXG5nKZpgiE7twZGQvfuoh-Z96NX3G1yHnOsTz35rQBuizBnwKKEmjhb4BFwqujUjwH2h0tgKGF5jGT_TK48ZPEEn6DqyKCSz6js7iogJ97wuvsRpTVVuQ_bpzdbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ve5ydn9n6ky3zEv6yMD2r4HOBfZpVa4n0VPXkohUYWyqzhT_iRG5C254VlCW0QF9BKNMrLR4E9L3PYi1gmG_JG06pxAImAtRfwXhnEBFE52hKvTb8-VlHtOZX9so5h0MU4Tt1SdJzMz2hWCtiWNdEFMUFJBWnmNsQWnTPhjSiF4Xa9ByaaaKYTlccZ4zQsmr27_Wp6fqkw667zzLw6N79QUF3lHs0jWOCXfY8RnWVk0G2T9FluJOtVsEUtQ6QjD8LOBGuFKxIABEV7X491G79_fJ-cvg9KDBXWS29lRuHBHxwgGeyxe6ThgEDyh7xvyMYX3KlZTY7iFwOiCj2wQZqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مقدار دقیق مواد برای ۵ تا ۱۰۰ نفر؛ دیگه نه کم میاری نه اضافه می‌مونه
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/675392" target="_blank">📅 13:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675391">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
آشنایی با خدمات مرکز داوری اتاق بازرگانی تهران
🔺
حل اختلاف قراردادهای تجاری از طریق مرکز داوری اتاق بازرگانی تهران نسبت به دادگاه و محاکم قضایی، مزیت‌هایی از قبیل کم‌هزینه بودن، یک‌مرحله‌ای و رسیدگی سریع‌تر و کاملاً تخصصی را دارد، ضمن اینکه محرمانگی پرونده اختلاف نیز کاملاً حفظ می‌شود.
👈
سایت اتاق بازرگانی تهران:
https://news.tccim.ir/
👈
صفحه اینستاگرام:
https://www.instagram.com/tccima/</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/675391" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675390">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
چالش تفاوت قیمت‌ها در بازار لاستیک
🔸
تفاوت قیمت لاستیک در بازار، یکی از دغدغه‌های مصرف‌کنندگان هنگام خرید این کالای ضروری است. بررسی قیمت‌ها در برخی فروشگاه‌های سطح شهر و تعدادی از فروشگاه‌های اینترنتی نشان می‌دهد که بعضی محصولات با قیمتی بالاتر از نرخ مصوب (۳۰ تا ۵۰ درصد) عرضه می‌شوند؛ موضوعی که دسترسی به قیمت شفاف و فروشنده معتبر را برای خریداران مهم‌تر می‌کند.
🔸
برای نمونه، در یکی از محصولات بررسی‌شده، قیمت مصوب یک جفت لاستیک سایز  ۱۸۵/۶۵/R۱۴ از یک برند پرفروش حدود ۷.۵ میلیون تومان است؛ درحالی‌که قیمت همان محصول با مشخصات یکسان، در برخی فروشگاه‌های عرضه لاستیک و فروشگاه‌های اینترنتی تا حدود ۱۱ میلیون تومان نیز مشاهده شده است.
🔸
تپسی‌گاراژ با هدف ایجاد تجربه‌ای شفاف‌تر و مطمئن‌تر در خرید لاستیک، امکان مشاهده قیمت محصولات و خرید لاستیک‌های موجود با نرخ مصوب را فراهم کرده است. کاربران همچنین می‌توانند لاستیک موردنظر خود را به‌صورت اقساطی تهیه کرده و برای دریافت خدمات تعویض به اتوسرویس‌های منتخب مراجعه کنند.
🔸
برای مشاهده قیمت‌ها و خرید لاستیک با قیمت مصوب و اقساطی به
لینک
زیر مراجعه کنید.
https://tapsi.link/rh2g6</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/675390" target="_blank">📅 13:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675389">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPxoS2oeOD8E7i9G_3oForWXJo5Z89wjWAFZxy2v7TuCmtjaOTvY5VC6oESYnD9DcFZUr3FaRTS8MqvZIEN-co_NgpSHrgVyCP46QK-pt_e6w4-AaVqxSvD2GiwS7Foe6uDvLevJ3Drifl4KzycfIGGfo8qASDeCfENYnhOAOzPKzt8FMLNKrcpJybngMw70cDTh97-N9f1z2jxVKKY5AXQUnV8LqhJYak3x9ncKkI9lZLmmDoiPOG6ag9Mv3ORLXtbfWJczxLQklgHz3GJBz4XxJBp9hkgwqkTCUM4kkRO5raYiceWKNI89G3aGZo5nvrPqQV_Y_pGnKES6Ye5Kyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۴ مرداد ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
امروز قیمت دلار در بازار آزاد با کاهش نرخ به ۱۸۷ هزار تومان رسید.
🔹
همزمان بازار سکه نیز نزولی بود؛ به‌طوری‌که سکه بهار آزادی با افت حدود ۴ میلیون تومانی به ۱۷۵ میلیون و ۸۳۵ هزار تومان رسید.
🔹
بازار طلا هم در مسیر نزولی باقی ماند و هر گرم طلای ۱۸ عیار، روی رقم ۱۷ میلیون و ۹۷۲ هزار تومان ایستاد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/675389" target="_blank">📅 12:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675388">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879cc5a64a.mp4?token=WUcjVoyVmcH747nUJdu_We4wPzNcIf7Sp6l_bRYH6c7tAsN0MFcbUjUeCNPLvsTvHd2qKjtVcQQ9K2Bo2FLKAplfMKYbDthxPg4VSk8SdODaBaHZKEsDR4cj1Vwv_Rj03qAu8i5TEWNgHo7LR78w_GZ5JrmOwt2d4FrIldq7ikPeBKdFRAmRJ83i8qHWKyq92kDL6Bc8Ypt4MP7iA5tuWluonaYSFeKrWz2VG9G7kM7_JuibQSRQMrwGFEXsdMbdhpnFZhAcTCsVu_f8P6SZrzoPLOH7t_RoPHkULx9-mznkSGW49C3sSAzUB4h0FAqGzJiu257hynmCPW2OTnyjfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879cc5a64a.mp4?token=WUcjVoyVmcH747nUJdu_We4wPzNcIf7Sp6l_bRYH6c7tAsN0MFcbUjUeCNPLvsTvHd2qKjtVcQQ9K2Bo2FLKAplfMKYbDthxPg4VSk8SdODaBaHZKEsDR4cj1Vwv_Rj03qAu8i5TEWNgHo7LR78w_GZ5JrmOwt2d4FrIldq7ikPeBKdFRAmRJ83i8qHWKyq92kDL6Bc8Ypt4MP7iA5tuWluonaYSFeKrWz2VG9G7kM7_JuibQSRQMrwGFEXsdMbdhpnFZhAcTCsVu_f8P6SZrzoPLOH7t_RoPHkULx9-mznkSGW49C3sSAzUB4h0FAqGzJiu257hynmCPW2OTnyjfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور امریکایی: هیچ تهدید هسته‌ای قریب‌الوقوعی از سوی ایران وجود نداشت؛ ترامپ آمریکا را ناامن‌تر کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/675388" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675386">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aad00d00c.mp4?token=b1XTqxbo6JCHqDNFVxfiX6Z7O6qM188386UECGMcY4J8XvnPrZ6qG3u72OFflbp-sVBbgIoNpFO4LkPOqJpded2AokupqYK-Q4sNAB2DerAlcWPyQs485X8E1F-62xPeIBki_OGlG9U3yuV6HIznvyj3924NQt7pMl1z9d9B2Izh_PUvjBJWMS0Vw0Fk1j3iiuWaRFGEyhAWppomXsrLzFXtMSQHWkZa3oomgJCcmrKS5Dx3GeMpkCQVo0rV0xEL9TWy1qyhRTxcDz09Y0dU2Xb97B-Ymnjurz1MG0uRinoj6_u31jdAC68iId-STmd8OUHJ86XBzgafzR-T7i67ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aad00d00c.mp4?token=b1XTqxbo6JCHqDNFVxfiX6Z7O6qM188386UECGMcY4J8XvnPrZ6qG3u72OFflbp-sVBbgIoNpFO4LkPOqJpded2AokupqYK-Q4sNAB2DerAlcWPyQs485X8E1F-62xPeIBki_OGlG9U3yuV6HIznvyj3924NQt7pMl1z9d9B2Izh_PUvjBJWMS0Vw0Fk1j3iiuWaRFGEyhAWppomXsrLzFXtMSQHWkZa3oomgJCcmrKS5Dx3GeMpkCQVo0rV0xEL9TWy1qyhRTxcDz09Y0dU2Xb97B-Ymnjurz1MG0uRinoj6_u31jdAC68iId-STmd8OUHJ86XBzgafzR-T7i67ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکبر عبدی، هنرمند تکرار نشدنی سینما ایران
🔹
گفتگوی خبرفوری با مسعود ده‌نمکی و احمد مهران‌فر در مراسم تشییع اکبر عبدی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/675386" target="_blank">📅 12:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675381">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایرانی‌‌ها روزی ۷ هزار تن مرغ می‌خورند
مهدی یوسف‌خانی، دبیر انجمن کشتارگاه صنعتی و صادرکنندگان طیور ایران در
#گفتگو
با خبرفوری:
🔹
به دلیل بالا بودن عرضه و پایین بودن تقاضا، حدود یک ماه است که مرغ زیر قیمت به فروش می‌رسد. پس از گذراندن دوره ۵۰ روزه، حدودا از ۱۵ تا ۲۰ مرداد مرغ با قیمت تمام‌ شده کمتری به بازار عرضه می‌شود.
🔹
میانگین سرانه مصرف روزانه مرغ در کشور حدود ۷ هزار تن است. فعلا صادرات مرغ نداریم و به واردات بی‌نیاز هستیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/675381" target="_blank">📅 12:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675379">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d154d7226.mp4?token=TceW2Wdx0J0tro-LiVYAxUEAy57UlbCATmsCdD3k7Sxci8uZ5A6dU95xcpk9aimkHe60Wy25t8f0M0ARwWwUerJ-sMglkSi0ItVE8yj2jmOhTXjl0ozfnRa7hAYwCx5O_S2ysnlGhYiSNmNMR9MMzm5UsuCm0RQX7Bp2-av6oHi-0By2MVCZ0xsNpE9e3f_vjfnY3cbblnQIh0qWLkSjeZVXTakwLHbVj3H1E2VU3v0BTNN4Rrobggw2Aj7DesixZPKhG1ZoA85U01rQT1yIqWFcnazOpWxU9PYY4WWPc8GVzNy9Jzxzy1DGCyEvS87d1boeWZW_gn2sXMeY3wz8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d154d7226.mp4?token=TceW2Wdx0J0tro-LiVYAxUEAy57UlbCATmsCdD3k7Sxci8uZ5A6dU95xcpk9aimkHe60Wy25t8f0M0ARwWwUerJ-sMglkSi0ItVE8yj2jmOhTXjl0ozfnRa7hAYwCx5O_S2ysnlGhYiSNmNMR9MMzm5UsuCm0RQX7Bp2-av6oHi-0By2MVCZ0xsNpE9e3f_vjfnY3cbblnQIh0qWLkSjeZVXTakwLHbVj3H1E2VU3v0BTNN4Rrobggw2Aj7DesixZPKhG1ZoA85U01rQT1yIqWFcnazOpWxU9PYY4WWPc8GVzNy9Jzxzy1DGCyEvS87d1boeWZW_gn2sXMeY3wz8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داروهای روانپزشکی رو باید تا آخر عمر مصرف کرد؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/675379" target="_blank">📅 12:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675378">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsD2kxtQtb3tjukJoaTFwG1DmnBZYNs5QAehSR0IJZ5IURYuZwhk51x80J91dB8SHj0hgFVJilXUbwUYujEpFfFo1WDhR7bOE2yNLr_tf6aizGaiXw8bF7mWWmXWI8Hu5OlVJpEc5BW4aDEZ99GpXK1MBg_zKpIKygPI_DWShRtNm5T1_4EZkFvwP3eN1r0UD0MFqsBqlbWUwhbIdYS8PMx_X3McN1h-hraTHonyYal_AQ1up_Tw4yUFRU15wEPKohG6w1LdvFEMN8yQVMcKpmlBytyB9LEbsFy0XudxI4yNWVA4bvcwKlk6W4GUBpf5dHWBiVu5BU9Wg0m2IYX8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
برسد به دست زائران اربعین
تمام خدمات مورد نیاز شما در یک اپلیکیشن جمع شده است:
🔹
بسته‌های ویژه و پرتخفیف رومینگ (اینترنت و مکالمه)
🔹
بیمه رایگان تلفن همراه
🔹
تامین ارز زیارتی
🔹
استعلام گذرنامه
🔹
خدمات سلامت آنلاین و...
📱
همه در نسخه جدید اپلیکیشن «همراه من»
برای مشاهده تمامی خدمات دیجیتال و خرید مستقیم کلیک کنید:
https://www.mci.ir/-4I2DXIW
https://www.mci.ir/-4I2DXIW</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/675378" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675376">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
وزیر آموزش و پرورش: سال تحصیلی جدید حضوری آغاز می‌شود
🔹
وزیر آموزش و پرورش شایعه مجازی شدن سال تحصیلی آینده را تکذیب کرد و گفت برنامه دولت و آموزش و پرورش، آغاز حضوری مدارس در سال تحصیلی جدید است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/675376" target="_blank">📅 11:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675374">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
توصیه‌های وزارت بهداشت به زائران اربعین
فرهادی، رییس مرکز سلامت محیط و کار وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
باتوجه به تابش شدید آفتاب که حاوی اشعه ماورای‌بنفش است، به زائرین اربعین توصیه می‌شود دو ساعت قبل و بعدازظهر حدالامکان زیر نور آفتاب نباشند و ساعات استراحت خود را در این زمان تنظیم کنند.
🔹
در ساعات اوج آفتاب حتما هر دو ساعت یکبار از ضدآفتاب با SPF بالای ۳۰، لباس حفاظتی و ترجیحا روشن که تمام قسمت‌های بدن را بپوشاند، کلاه لبه‌دار و عینک آفتابی استفاده کنند. همچنین خوردن مایعات، به‌خصوص آب و یخ، از گرمازدگی و اثرات سوء اشعه ماورای‌بنفش جلوگیری می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/675374" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
فهرست خسارات بسیار سنگین آمریکا در پی حملات ایران منتشر شد  سردار محبی سخنگوی سپاه پاسداران:  طی ۱۵ روز (از ۱۷ تیر تا ۳۱ تیر) آمار خسارات وارده به شرح زیر است
🔹
در حوزه راداری و پدافندی:  ۷ مرکز فرماندهی و کنترل  ۳ سامانه ارتباط ماهواره‌ای  ۶ رادار پدافندی…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/675372" target="_blank">📅 11:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675370">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تیزر/ مروری بر مجمع سالیانه «وتجارت»
🔹
تیزر اختصاصی شهر بورس از مجمع سالیانه
#وتجارت
.</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/675370" target="_blank">📅 11:07 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675367">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5a04d09fa.mp4?token=pQ0bcbD-ZAm8wZtVhGZZBovSs8vNFg7r1lOds78NOoLQWkJRWu1QCn9KX-k_5yPHF58fGG-Gu3jjTkirncOig3OnXtEeHLkKEYjWS8QT_w001xxvUVV368zkqkRXfwDSxTjBPb6Of_c8Rvg33mnABJrpbf1TmWhXtcCfH0bxRVRJNteqqpH5Vr_dQRCds4pfaOMNCic2S9CmY2xWJzmHfP0Pnai4o7-W3hckg_S-t9_tsEibGE7ViZAxlu4-c23-BS4wcNZ5GtVnam4e5mfEJAcPU9cSIqpedQRTXeu82MbqNXtHkuhsiCH6K1f9o7FaqGSfBD_f8vxe8HoCtbd2Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5a04d09fa.mp4?token=pQ0bcbD-ZAm8wZtVhGZZBovSs8vNFg7r1lOds78NOoLQWkJRWu1QCn9KX-k_5yPHF58fGG-Gu3jjTkirncOig3OnXtEeHLkKEYjWS8QT_w001xxvUVV368zkqkRXfwDSxTjBPb6Of_c8Rvg33mnABJrpbf1TmWhXtcCfH0bxRVRJNteqqpH5Vr_dQRCds4pfaOMNCic2S9CmY2xWJzmHfP0Pnai4o7-W3hckg_S-t9_tsEibGE7ViZAxlu4-c23-BS4wcNZ5GtVnam4e5mfEJAcPU9cSIqpedQRTXeu82MbqNXtHkuhsiCH6K1f9o7FaqGSfBD_f8vxe8HoCtbd2Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های هنرمندان در مورد اکبر عبدی
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/675367" target="_blank">📅 11:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4a1a32e2.mp4?token=HeygKgpq_aMInyNlPPJB9LoHGnHHhrjy_QlOnpgjqVYMFVMRmOgnkGsSs8CMr4_J_czN6nHvHdHB5ZfDtdzyk1DcRo0EKnjgNDWuj9c897M9LefCcFFCPNEO8IQY_GccbTYi13ss_Lrmy3kaiS0utNmq94tnkDDjEHOwVcCLxj8h87npffmCF5Rvy2l-yUNDkW95hIbVmMxJ1iVZ5XgAm8wnsean19YOg-0UqZ9B0ND44oQWv01PiSB8ng6cJUwIKZdGdUGhlDqRRBU393jYYNASGG2xKzd5EEXOJtvacJxxcS4klDwuvar-a-WhTQ50kCP3ltA18viqbIJhdsLvNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4a1a32e2.mp4?token=HeygKgpq_aMInyNlPPJB9LoHGnHHhrjy_QlOnpgjqVYMFVMRmOgnkGsSs8CMr4_J_czN6nHvHdHB5ZfDtdzyk1DcRo0EKnjgNDWuj9c897M9LefCcFFCPNEO8IQY_GccbTYi13ss_Lrmy3kaiS0utNmq94tnkDDjEHOwVcCLxj8h87npffmCF5Rvy2l-yUNDkW95hIbVmMxJ1iVZ5XgAm8wnsean19YOg-0UqZ9B0ND44oQWv01PiSB8ng6cJUwIKZdGdUGhlDqRRBU393jYYNASGG2xKzd5EEXOJtvacJxxcS4klDwuvar-a-WhTQ50kCP3ltA18viqbIJhdsLvNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های علیرضا خمسه در مراسم وداع با پیکر اکبر عبدی  علیرضا خمسه:
🔹
دیشب در منزل اکبر عبدی، انگار سکانسی از یک فیلم تازه بود؛ باوری که سخت در ذهن یک بازیگر می‌گنجد. بدرود مرد شریف، بدرود رفیق./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/675365" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675363">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
صحبت‌های علیرضا خمسه در مراسم وداع با پیکر اکبر عبدی
علیرضا خمسه:
🔹
دیشب در منزل اکبر عبدی، انگار سکانسی از یک فیلم تازه بود؛ باوری که سخت در ذهن یک بازیگر می‌گنجد. بدرود مرد شریف، بدرود رفیق./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/675363" target="_blank">📅 10:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675361">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
اظهارات عجیب طلبه‌ رزم‌پوش: برخی برای معافیت سربازی وارد حوزه می‌شوند و بعضی هم فکر می‌کنند آنجا بخوربخور است! اما...
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/675361" target="_blank">📅 10:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675358">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95c1cd2ef.mp4?token=ghOuUZFDCr_HUGecYgqf2sHUuJWNWC0f5tw3taXiTNHs4Bv7TCcROStdRhtz4S_rFcWiZmsmJ6FTaGIvdv004A7ytsvClfYPHySTNHU2n3dY2MF04zinx5Y2xG601gd6xx6EbBiqtvepzpG4OM6AKtkquIZARUXG7s3SQ6D2sSMrVKH6oElac-6oB9Ho_qRl86ImCcOjitIdp-NyGSx55KdcefszuXWfagRpi_42r7z_8hH_FKQKhjxqnvQdERtvfd9nqzPjooKF_smsIW8KnjsX6aO8we7H2SFdc4aQQWC-mNIDM0iSvQ-mR1AGZNxXB_nnp9MNzro8sVK4LPaGTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95c1cd2ef.mp4?token=ghOuUZFDCr_HUGecYgqf2sHUuJWNWC0f5tw3taXiTNHs4Bv7TCcROStdRhtz4S_rFcWiZmsmJ6FTaGIvdv004A7ytsvClfYPHySTNHU2n3dY2MF04zinx5Y2xG601gd6xx6EbBiqtvepzpG4OM6AKtkquIZARUXG7s3SQ6D2sSMrVKH6oElac-6oB9Ho_qRl86ImCcOjitIdp-NyGSx55KdcefszuXWfagRpi_42r7z_8hH_FKQKhjxqnvQdERtvfd9nqzPjooKF_smsIW8KnjsX6aO8we7H2SFdc4aQQWC-mNIDM0iSvQ-mR1AGZNxXB_nnp9MNzro8sVK4LPaGTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر مرحوم اکبر عبدی: از این‌ به بعد هم راه او را ادامه دهید؛ ما کمدین‌های خوبی داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/675358" target="_blank">📅 10:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C66TEd_azc0VENVHGyOMwxXHdqdqQouqWo08njYvfL0z3DVZJmUXH2qKxKpibh8ERUNOguNYgbR3ChA6EFWL3n6ySxvL6lEL_mxnHzzkfx7sjeXtYkMgfDb_1rAvs46H1nwCVZx3P9q2C1Eeasf_fHahgSuyMxQkCXdoZetN3HXvnQF7r3EaNOZdx-vO8SKMvXBfHt1ZP_0Okwj4Ei8WOgHOZby_YzELXQ_OCKafJ9l4L89jbQcTB_opWt5Y1A4gcFvLJAUdoRMUfsJGg1FiJYSNYnj21vGZIiBBG1NMw67IIw2b12Dp_8TTVor3IZQhml_aa4ZJTg8Uwyml00wFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EESgiFctGeHNmw_QAYnj3BlbM7W7ONabZNN8LTNxtTfSW5s56XazVVBVshB3oh0dtbATIvczUqXOuVu917c-lJvWbLTHjMdS4b65R-xldXkiX84_S3QiZK-7gSVfIRuuPB1s2s04HLso7ZC9NM-Z2FO7avap5jIoSiYJUzu-TWspcbLUeAP1nXfoTuU3ywG33DTjslApNqHHj3DJkW72fGswiHqtCljk31hMWLnR7iowPYk_soop5LUB87jHr4gqp0odnHyjvn2qnajobvtXadag-HUi78IcvNC8iDXPvahgCuPFMfFfP8TRnUxTSoEZRgLYROhZ3v6s02j0im7jXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
برند معروف گوچی از پوشک جدیدش برای بچه ها با قیمت ۸۸ میلیون رونمایی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/675356" target="_blank">📅 10:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675347">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLz_c1MCUrmXBxwCvoVgh0_rnwvXeyX0LuiCy1zIAgQHSm1MsbDNjXlk3r3D8OJRDw4gyC_yCVUbdbH3xTT7EZkgyP6YR8PEcUnRmCl2d8VBQI9m8i0JzzhIjAcuqwDIx_NPH5r70k2XDQgCIhIWGsZ57pciBsE1R3DkRTqDme3TM7iwDfr8QCOAHxNwzg9CeeYkdA-25SfqC2RnzAlxgnVUEfL8QHQQ4SfgEBn4ox2K0sxXQ1HDpLKcbP4Ixu3V2ObuA-9CCMR_TENRSl8i8te15t2QJlYqd_GMi-04SM2E7zAkyKvtVEPjzHt44fo5tjSAK6p8JhHOjKcuEhXKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWkrD0eMUBGdDsnHd6leWSBVLMAm9Dx7c9Ubag7DWFkFpm8tcSg1rab0bmZOM_bxt0hDw69KoRZc4ArfTxEeM1Fa3X-bsEUp7MEs7fS24IXYTXnbiXDZUJyq8url-WHbextwC0Gtmsja7uMfu1fwGGFs3l4vFZbDfzfgiQpViD91RmgDFpy8FswzbFh5WUkzyNAO_Gz2U7VoGV8SkstDD9jVrf9D4k3icQthR0iHJmhsO9E3FDT-ny8trekhMUnNeEWGJUSdDbJMpVyXFP9YmtAtwnfb_K5EapiKmEkLmjh6Yl5hq4epvTmy5Enog6CW6jA7f0LwADLnR0-gdFmj9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U_TEuoNMHNjVK4fjyEJy9Zlc6GtGmkCLeQLFfIrZx6lpzbh_gubmW5GVDBscH0QZ7a4yEmx59jacTtWLbRc-121ByKd01114R5u2eB8Y_Ae9zjHMqlx98RjsyVIrUbS9hitSDfbDNMTGGLHvn1NeBlZG9pZDd5--NAbGegBY3ciYwbi2ihu76KlcalILY04TGFl-N-I0ce4W4aVIv71LRIOUpAJBXiWyxOsJdsjTbfVogDawp9OM2gvZEAY_WO0lPTZWkEV35jZm_80hFeXiMZ4MMBYdQQKVCSweBp1iYufXZXlGlmKfcVE-xVAhG0k8stHosR2sQANxFEYVrd6B0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXNqD5tvtP53WjlgY0gGWKjc50V5kwwA98LJ_w47LJnBrT9ZlvSaegJViUlvLldHnsjvHmhh-teQ9qY0DiqxRgJDnovFIQ1sB7GFeRs6YDE6opiOYl2dCBthEY8UBmLQ7C1KrSpsVnj6kn2HSVShDFplN7znX-9gUcwScwUBd0bnkXi4u8ljW8-xEnXQQbSP2jOZMKUzF_tRgB-5iuRdt41MP-xsX30jCtxc9fCN68of-86hTzsnwCa7_aeV43QXrEQIs-WkZuOSlmjHk31e4xTiTxyFdVFMF7zElcy6b64OT970CYXgVa04vZK81NvUXGjNCRuQwOk7-nRMCyvIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0clBrscCnJObmicLc1ZbmGtHm-MSlRQiK3MxhuOr2XVlBbUmgQ12M1bkM__3piOa9t07eWP28b8J18Ip4kpnfDqceK_0FEh4i4L-wti7GM5FjSVwr2ZXW1GEZdl6WzB_ehwW_3c1agqJCdkP_Uf6eFRGVam3vSg5TIjY4e6wyFy-B8TkQZpH9voKInKN8O6z6hZmzpKk2l-08lznH-BtUTWegEpyLtWwYeX6DbtgxdUE0GKOjso7xxBxqLNsGYXBIG_OWk3-ljL0DDwEKONAVgZkepPxexbkBp6-q6FKv3X8NpqIEYip3hToj8NPS7MaFfA3a68wcGvT-dRHK0QQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkeG3RDYQmOvK1NaCA650PreTf000O0P2EWme_KW-Un3wnHMbjlwhzJHINj0cQ5SDVeMTte-4HCOwp0QkjpmWhvyoK_7XoI0s0TbhfsIEd9WpN5qIFN-SjkhvpGxptGmmWIRy64iiwTu-b9kIzhePtu0XGneUaOFHL8ZfyygjhEVPkdvZEh05nbdAJd2jMP9Rso9JZZ1YYFWge0p6cbPpCYVsi_T4rrwhTAOsIxG9Fo5nacOGGNxINOKcq63Gd52nQ7PVpvfx3TWFhh27oE1oZIg5btDTdWe5CsAhfSU9uwPcCrde8LYvHqoLrEByyN1REWIeREwUpH0yXfBeu4SgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4DcwIlFCz1Tw3_EhdRRqGjbS_GpBc7k3gmntIZk6XDcGqCtSKXjpYKdl7ej--Skv66yiGXEm7wPglCMEEC1EEtY_apwUNjSGgmrB5b6sR2iAgKwlOtqqdcgTi6fD_b2oicYlqE9L7rIlv8jc_JRGgEknaK8_h4mN7E03jYD0mIaywo9Lpenj5w6HAmTXOTKkOh_Y__aiNSfKrxKW3cmNdB9rT11oQOypaMJXHHZdAri8h99RY7eMjowzOiyoYOMOngzg0K2PrtlLI3vB4dr5_YiaDMYMGZd2UxwbyWC0vWBcVXnPDezg9fllEdzwP53TD5Ip_jC1RMO512u4ahvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSWqU-CF8eHQ7Ptb-VucU6ERzKDUcmxnb4NDViQyP9031KyZdEMu1Iy6q2cb16bwp2soUwQ7Mh4rwPqQSKSY93dM8mP33yArG25Hk9bWis3neU6JgTX3XzbLDVoDunOJMFSetdoT-W47A9ru5RjMjnUcrv8e5i_dTYPjJuDG6Sjn8MlC61Vdw5TxiQKysOeyGi6vWaA77VstbkY2HXzudGOA4aHubS-Ia4yAAABPAdRIUAHIKMGvryHpjfNda8Dj8wjWcnMR1WwRviiP8vP9dlHPlZsFa0lI5QlVwRipk4EGIQpAmk3hCEr4trOGYvjXmPcVGZKR0v3EvosfrzPgDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLuQvUC_g0iv187-Z5Nys69R4nE_CQU36UXKZpNXwGuVQFuhFF6IRp3ZyH-RZ5PxToq4CR9hJHMQgyCyggXRrS4MdSS9x1POyII9b5NE8G__BJBSMRB9aLZhDNjDvzj5j9at_Y5RSS7Lg2XrXaHSVwkPUjifQjxU1LuWYkQgoW8Q79ZSRimWkVsutdG7AHAuMUnSQ7yawoq4pfMzFFeYH_KQtW-i6D4hZ126ORtH66Yo128AgRiZ9BnViz13aVWCshMxqaQCydSnB2BiGvutT9CTCerHmx1VFrp5hT2w_mTzvyyl-9ymPyCh93M7J0ksuX3k6PI18nKYCTsXieQ69Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گزارش تصویری محفل شعر شاعران و نویسندگان ایرانی در اربعین به نیابت از رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/675347" target="_blank">📅 10:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675345">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQBmdeHwDXWi0HUnnSljxgSpkXV22UWI3KEW9VjWsBGr0oibedIym1Hok3W18Dd0SSH-Aj-rIHBifgYP3_NDFaDHL8kDDNaBcdnZxs6hsOxCX-HVxj9-_tO-Lwwdptnd9TfutND5_ZtrJ6GFuN1CwzcOhE0soRSv-XwOd9C8FGd1bNcjqAqbG5yabyxujh0EHpXWFaDj8xwhsdhYWJCybeZD_QairNfth27FzKhsUOA8UCMTND9NUfWboQ6-Hk2LZlPp-Y8U4k_sfx8Yjpf-1t3DeJM_cZToERrFIQu2qNYeNfW4btLsxtu2J4Q4aynlVoJvOU9iN6k5RswzV5qi3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd934ca97.mp4?token=p3z2N7UkpvcBZGpRkhkUsxHsSBlnyOR2R-DF2b9vZoDl4cFsXSH_e2o0taaWW9sCh_SrcHYX47hd3y5d3zvYnH69_cwfJly_cRWVtfUdnIg8V0FmvQCUug2CMIksh4PDgZ4J6tnKlwXTebtdxR6y5-uXQ3xA_awM9YgzR1kxq1RfDZF8zfaMTMdWgEmL1pZKcxK9mDtPZQNTdphFdPzJcZhHobGI7QpZ8Xn-zAl2IXK_wnCppctiu8WKvgeJ6vhhHj5aAd3xA42jlsdhpsi2h1-NHvaildIDYoPZ0Uzphz8bzMta1fb4nweCzW-itDH4HldE4nDxgLMboB-AiW8WpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd934ca97.mp4?token=p3z2N7UkpvcBZGpRkhkUsxHsSBlnyOR2R-DF2b9vZoDl4cFsXSH_e2o0taaWW9sCh_SrcHYX47hd3y5d3zvYnH69_cwfJly_cRWVtfUdnIg8V0FmvQCUug2CMIksh4PDgZ4J6tnKlwXTebtdxR6y5-uXQ3xA_awM9YgzR1kxq1RfDZF8zfaMTMdWgEmL1pZKcxK9mDtPZQNTdphFdPzJcZhHobGI7QpZ8Xn-zAl2IXK_wnCppctiu8WKvgeJ6vhhHj5aAd3xA42jlsdhpsi2h1-NHvaildIDYoPZ0Uzphz8bzMta1fb4nweCzW-itDH4HldE4nDxgLMboB-AiW8WpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از هنرمندان حاضر در مراسم تشییع پیکر اکبر عبدی بازیگر سینما و تلویزیون
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/675345" target="_blank">📅 10:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675342">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLqiHp2iNd1ZQpUXJ4xod9tDCw8K1ITNsxfLXXf4CpBa0c7CtlU0s_lvT-AnwMl2X-AtWWi4kkcU5597vqTKXzaWuz4JygF_Bo3RO90-DIKwxfisE_ndkP6RFqPGDrfUgTuCviDx8nqZhUXtTgapqWrzLbMo3xXPHCNS-FpXVlkadlQ0Ok0rZUvffMgos3MdmlghmQ2QwLgekODMgg4SvMdF76bcxo_45844fQsIZG-331B2o7No14G6NN1DuWzuryfpxguz7Nt7qFUH5GS5H9M32TWiXCn4-ycafnzdmCYU02Wb4tjmz71OT_jICa5ubkX35gmhbwuy_FOdZ_2_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omtoQrIcjiWx3WNP1Q5_HLSdqpk-CCvhgkAPCpjaookp4OtrqQYRBQHejfE-efQdPWiFt8xIRonfN7FUohrzcaSNDhd7XVmwkY1BRJg784paxsygzTH0qimlDPKzZ5TyCwQtCsoW90mFAH-waY2d0SvoxlYdT74upHiw0xlCGu5QHFPQOHehL4_h_DqNOuk0xFu15yLnxC4ocDU2kBwT76MPEsKNqVnUqqOp5ym9-iYdHFq5RDKHyc9HtRxlosH-CsCTdLjNeLZ3VnuM3_UITLXniRXIp-y61vVMX3hOHK-i6Igpprhl_Db9BO7Uz0HF_QgPwheEBkhV67HAwJbFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MVAEMfzFT1WwoK7gT0O1wE7EuUVGVaqfdUPnUqpmu4OqyhXE1jgfsgOTMYrqBREJJ1TZpNFnFQURkKjGV7UnRSHOt4kgnU2n7Ux-SY8VrO2L04EsrvXJ7TSI9sTZVGCYHh28hKBJ4Nxomg2cDnCw3xGPy5FDv7YLVheABIczdjQ0lN24aIbxl7ZnYeEUCxhrYkSpOY4QHtXhBcVJi80A3C7SW5wID0l2RP6ydDiRRWx84s9-h9mLbFCyaEfyW_0nyAMgIm-dzCaZMtxCZWCEuLOcIaT31y2HkWmN-U-zzOLyoW1Htjwm2DM5Oc1CjvI3y50jLtYcCOpPUBh6GEI3Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بنادر کویت و عربستان خالی شدند
🔹
تصاویر ماهواره‌ای نشان می‌دهد بنادر کویت و عربستان کاملاً خالی شده‌اند. یمن تأسیسات نفتی عربستان را بمباران کرد و نفتکش‌ها گریختند. مقرهای آمریکا در کویت نیز هدف حملات ایران بوده است. از زمان لغو تفاهم‌نامه، کشتی‌ها به‌تدریج کاهش یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/675342" target="_blank">📅 10:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675339">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd39b62ba.mp4?token=iUm3cB0TbobsMSkhj_Kg3TTVFvdTbJM7MpET9Rzu_NW3vAPZe5ESbRFsYdRFVbg3J8DfS3J5RN5iE1msZZF43bSMVNRI0HJblrf6e-oZH_BhnVtNA3VEhPXvat_r37Lv1yB-NSFnNer904cIDrdTu9hoM1aSAt27eOssyGkMQb9UVdEMFDy0rXMIqrnRbC8A2ZoCcIO6nTOgI7qRfhxgk3yF-DRFF8-FImEZ-scRIS_i4rYtVi0pRRTnnz2kpeCdb-YshNpoD6Dx7YY8fIIRs5SI-qdl-gCpBO-25TMiaWh0IYyhp_Ptx5IKpQwzghHtMoEvFaUOrisd3fo8TpIdKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd39b62ba.mp4?token=iUm3cB0TbobsMSkhj_Kg3TTVFvdTbJM7MpET9Rzu_NW3vAPZe5ESbRFsYdRFVbg3J8DfS3J5RN5iE1msZZF43bSMVNRI0HJblrf6e-oZH_BhnVtNA3VEhPXvat_r37Lv1yB-NSFnNer904cIDrdTu9hoM1aSAt27eOssyGkMQb9UVdEMFDy0rXMIqrnRbC8A2ZoCcIO6nTOgI7qRfhxgk3yF-DRFF8-FImEZ-scRIS_i4rYtVi0pRRTnnz2kpeCdb-YshNpoD6Dx7YY8fIIRs5SI-qdl-gCpBO-25TMiaWh0IYyhp_Ptx5IKpQwzghHtMoEvFaUOrisd3fo8TpIdKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوکوسبزی رو به سبک تبریزی‌ها درست کن و از طعمش لذت ببر
😍
موادلازم:
🔹
تره ۲۵۰ گرم
🔹
تخم مرغ ۳ عدد درشت
🔹
آرد ۲ قاشق‌غذاخوری
🔹
نمک، فلفل، زردچوبه، پودرسیر و پودر پیاز
🔹
گردو و زرشک
🔹
روغن باید داغ‌ِداغ باشد #اشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/675339" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675338">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb7c984de.mp4?token=S8MQ5N6Vi_-IH41F5yVngOkDTFSZiEUT4orp6Iz9s96KnFGvvLWEImPAhy27tokdygIg1N-dKBQ7BtuFWpRCHubWamNVP8dYn_v2Ws9ud4dhzCUUoSBxonobJxT7fe7NcuC4C_A5FHTQvSuJpwJcMuEXL6nt4CvVliM3XvHQSkEsAvFDZN5_JyfojVGJsUjxogA3qfmXOnVbPOeOPDcqrwp_NfiV5oBfr55BG41C0S2uYELtdQ--Ea8U8NYwpK7ZMBREFVj18f7qerVd25txzFMUBSBdJqwScdUoAMTsoYtV4DxowkQ6GQqDi2TbtQabDVSoIVTh47-yMtwAir6COg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb7c984de.mp4?token=S8MQ5N6Vi_-IH41F5yVngOkDTFSZiEUT4orp6Iz9s96KnFGvvLWEImPAhy27tokdygIg1N-dKBQ7BtuFWpRCHubWamNVP8dYn_v2Ws9ud4dhzCUUoSBxonobJxT7fe7NcuC4C_A5FHTQvSuJpwJcMuEXL6nt4CvVliM3XvHQSkEsAvFDZN5_JyfojVGJsUjxogA3qfmXOnVbPOeOPDcqrwp_NfiV5oBfr55BG41C0S2uYELtdQ--Ea8U8NYwpK7ZMBREFVj18f7qerVd25txzFMUBSBdJqwScdUoAMTsoYtV4DxowkQ6GQqDi2TbtQabDVSoIVTh47-yMtwAir6COg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شاعر «میدان با تو، خیابان با ما» از خلق این اثر حماسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/675338" target="_blank">📅 10:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675337">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74fc712a0b.mp4?token=dUAzisFAVqM523oCd2KbvqmNxZvjPTGIahYkHFV6eDfjcjsNOSFdOyIfFGL3yZlR_Bba5QS8sDM3LfEcbveEThHDfMp6uTh2dYFmT8ZxogB30UWOaYnOlsAw6z4B3dNJsC_QzpuGUGkZ6CnBfIC9iLAYfY6L0DdzvsyTMEPo7SGVCZn2Ve9T4VPqJw53BIBKsLh1yb-eUXxP5GFWlmH32Q9CIXAmgFshNiO6W7bHb-0GP5f98WksNGVyBsBmB7W83OUmjVc4iRQquXFsP0O0AOrHo68yTCRzcLECIP0l2HVSUNuGvw1pzBEpbAwxPlEyYQ-LSpLbJroo1m9BLsO2NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74fc712a0b.mp4?token=dUAzisFAVqM523oCd2KbvqmNxZvjPTGIahYkHFV6eDfjcjsNOSFdOyIfFGL3yZlR_Bba5QS8sDM3LfEcbveEThHDfMp6uTh2dYFmT8ZxogB30UWOaYnOlsAw6z4B3dNJsC_QzpuGUGkZ6CnBfIC9iLAYfY6L0DdzvsyTMEPo7SGVCZn2Ve9T4VPqJw53BIBKsLh1yb-eUXxP5GFWlmH32Q9CIXAmgFshNiO6W7bHb-0GP5f98WksNGVyBsBmB7W83OUmjVc4iRQquXFsP0O0AOrHo68yTCRzcLECIP0l2HVSUNuGvw1pzBEpbAwxPlEyYQ-LSpLbJroo1m9BLsO2NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین تصاویر از تشییع پیکر اکبر عبدی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/675337" target="_blank">📅 10:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675336">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
فینال جام یوفا، ۱۹۸۹| گرم‌کردن افسانه‌ای مارادونا؛ شاید زیباترین قاب تاریخ فوتبال
🔹
هنوز بازی شروع نشده بود، اما مارادونا با چند لمس توپ و با آهنگ Life is Life، خاطره‌ای ساخت که از نتیجه مسابقه هم ماندگارتر شد.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/675336" target="_blank">📅 09:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675335">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
شیطان زرد مدعی شد: توقف موقت حملات به معنای عقب‌نشینی نیست و در صورت شکست مذاکرات حملات به ایران خیلی سریع آغاز می شود
/ ایلنا
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/675335" target="_blank">📅 09:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675333">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719dbea7f0.mp4?token=eOFjWImiccV0p0SDnIbN4TkHP0wbLObUzUqLNvth8IJp4-jGgjIfSt19bEDzTow8xfkLGUmXsGmZqC17R93sQU5qB5MkY2jTD6MU9GlJkoZSlk_qss3nsC0IDOyBuHRH42-xp-EDmpxh-1d1Bcfhu2jSr_WPq7SUBgFvDVQ3qqRmeZ5vg1SWmGBuSOx4KY6olu8A2s-eMM-2de01Yf-nyWpG3341V9gE0t3lrzPQ6Wqepat1X9UIIZ1qMjqb3NpT3ZgtkooTW5uKZqimCbeZpVlKttzyo836SKTYAXeelwcetBH0BUeL0jeNuPhjzgGo_V7gB87j27QRFsy2h81ftw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719dbea7f0.mp4?token=eOFjWImiccV0p0SDnIbN4TkHP0wbLObUzUqLNvth8IJp4-jGgjIfSt19bEDzTow8xfkLGUmXsGmZqC17R93sQU5qB5MkY2jTD6MU9GlJkoZSlk_qss3nsC0IDOyBuHRH42-xp-EDmpxh-1d1Bcfhu2jSr_WPq7SUBgFvDVQ3qqRmeZ5vg1SWmGBuSOx4KY6olu8A2s-eMM-2de01Yf-nyWpG3341V9gE0t3lrzPQ6Wqepat1X9UIIZ1qMjqb3NpT3ZgtkooTW5uKZqimCbeZpVlKttzyo836SKTYAXeelwcetBH0BUeL0jeNuPhjzgGo_V7gB87j27QRFsy2h81ftw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکر اکبر عبدی ساعت ۹:۳۰ صبح روز یکشنبه، چهارم مرداد از مقابل تالار وحدت تشییع و در قطعه هنرمندان به خاک سپرده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/675333" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675332">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b220fadc5.mp4?token=hrRkQCfbZdaf4GLEWBUp7U5YdyA6-ch1bL5hHR23j7x9dCYhql51uoxMTq_a7W7AI-QCv5iOfyEbvaE8-ohqsk8qEkFMZtOCLbDz1RzofxExKSPoZGMKKPA3at-rwKynJ3765wvbJ67USIDB9JBU_LHOkQgn3vI9Xg9SfRTYn9ThBIH7_VB8eLY3DJpJmTPpBWcVA5eGFAnQxwesy7KP7M101c6nAPRQu1AiE1qyY9oh4EVwC7SUyHUdxeQYvOtdA63Fyh42AsFV6fPScb8mFXD5hNl6jgPerOEwPY0n7akdgUKva2JzvxKwF8PIMqF_Hmqoz_GwqwsWo5j0d6cdX1cGuyiwG4j2u3fKq0fcpARPMfLsmw6qSGku3R81p2d6pKkPMW16E2TFlbqKvPeONPr9XOUO4WhRs5pgT6otvEc7bgodk5QX7KFWeKiwX9h-KFNpheFXmtrEx2R5u2dtiffIAL0bafN5d8tovQb7n15My-IJmKhtCd8nnU1EY6H0766_xaVQ1iJgY7ST3UfClRbkmC_dWM61sx6qdZnJNoQOD58f0gzSO8C_eaSDsx1zdxIq3oUt-LSreSPwgCbV4Chtp4t-DlxFKUdPVM1g4oBvqYpqU4xlpKtw9hcJgvmJIv8Zfq6HEIpPkgCMSFZifHIC4zQW3l4KKmzYPk6_J68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b220fadc5.mp4?token=hrRkQCfbZdaf4GLEWBUp7U5YdyA6-ch1bL5hHR23j7x9dCYhql51uoxMTq_a7W7AI-QCv5iOfyEbvaE8-ohqsk8qEkFMZtOCLbDz1RzofxExKSPoZGMKKPA3at-rwKynJ3765wvbJ67USIDB9JBU_LHOkQgn3vI9Xg9SfRTYn9ThBIH7_VB8eLY3DJpJmTPpBWcVA5eGFAnQxwesy7KP7M101c6nAPRQu1AiE1qyY9oh4EVwC7SUyHUdxeQYvOtdA63Fyh42AsFV6fPScb8mFXD5hNl6jgPerOEwPY0n7akdgUKva2JzvxKwF8PIMqF_Hmqoz_GwqwsWo5j0d6cdX1cGuyiwG4j2u3fKq0fcpARPMfLsmw6qSGku3R81p2d6pKkPMW16E2TFlbqKvPeONPr9XOUO4WhRs5pgT6otvEc7bgodk5QX7KFWeKiwX9h-KFNpheFXmtrEx2R5u2dtiffIAL0bafN5d8tovQb7n15My-IJmKhtCd8nnU1EY6H0766_xaVQ1iJgY7ST3UfClRbkmC_dWM61sx6qdZnJNoQOD58f0gzSO8C_eaSDsx1zdxIq3oUt-LSreSPwgCbV4Chtp4t-DlxFKUdPVM1g4oBvqYpqU4xlpKtw9hcJgvmJIv8Zfq6HEIpPkgCMSFZifHIC4zQW3l4KKmzYPk6_J68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناریوهای احتمالیِ آمریکا در مقابل ایران!
اکرمی‌نیا: ما برای هرکدام از این سناریوهای محتمل آمادگی لازم داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/675332" target="_blank">📅 09:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675328">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1756a5af24.mp4?token=jke1B6H41ExBK460zKtxgZEm8VE1hrzgU7VRWksChUAOJkVL66l0CqXqP0cv_MjpJvHsC0RuzTmFAqJnZLQgnP9yw5Er31yx7N3RQgDyfFTeM1JDzITbsQAwERowt-8CFYODPEfbdhBR8MMQWfcdxeqA2Y4yDbvrjyDiuc9VSzUnmst3w_WJYlwEyNJLx6_0FXw48U52rhNkE_6-JCirb01OoLAE0gnxXD3qY-dzUR23MlF8gGfyck7u2gGu2m_kYW1pR63ojz1s0YFSUUi39YuWJFFNWAckKVuQLInbxk9ylL1GYipaNS6YZPAMDqiDXkIHmbOGJsKXt1dExKcUboc29bu0jNEIIPTqG3RzFD0J4VMOmbtFbDyY3wf4E2cgUCt6klBoZJZG-km4_ZO49cJlHuAM1ipV3Jy-7TK6hv7CuO3RxYUZcm5pI2jgzH9aIrvMX8kPgxgnR5Fm-8HiGadDjihB9MF0IjsP-dldmADwkdg5DNeq7c52TUvL0_24A3uCZwCKM7NDSxIVmhuYGFp_UxCZpiMXjtgUcTMX5HW9gi1SNytOEmjDaLx9bIsIpy-zbEHWuWSbZbYrsfjO8g3EnBkT0u1LtKjKDMJlFuhtarHBbXavHhEg_xLdxGeM_DF__jaGdxsO5rRbdT7Kmf1P_eTrltgmdXNlGkgzUKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1756a5af24.mp4?token=jke1B6H41ExBK460zKtxgZEm8VE1hrzgU7VRWksChUAOJkVL66l0CqXqP0cv_MjpJvHsC0RuzTmFAqJnZLQgnP9yw5Er31yx7N3RQgDyfFTeM1JDzITbsQAwERowt-8CFYODPEfbdhBR8MMQWfcdxeqA2Y4yDbvrjyDiuc9VSzUnmst3w_WJYlwEyNJLx6_0FXw48U52rhNkE_6-JCirb01OoLAE0gnxXD3qY-dzUR23MlF8gGfyck7u2gGu2m_kYW1pR63ojz1s0YFSUUi39YuWJFFNWAckKVuQLInbxk9ylL1GYipaNS6YZPAMDqiDXkIHmbOGJsKXt1dExKcUboc29bu0jNEIIPTqG3RzFD0J4VMOmbtFbDyY3wf4E2cgUCt6klBoZJZG-km4_ZO49cJlHuAM1ipV3Jy-7TK6hv7CuO3RxYUZcm5pI2jgzH9aIrvMX8kPgxgnR5Fm-8HiGadDjihB9MF0IjsP-dldmADwkdg5DNeq7c52TUvL0_24A3uCZwCKM7NDSxIVmhuYGFp_UxCZpiMXjtgUcTMX5HW9gi1SNytOEmjDaLx9bIsIpy-zbEHWuWSbZbYrsfjO8g3EnBkT0u1LtKjKDMJlFuhtarHBbXavHhEg_xLdxGeM_DF__jaGdxsO5rRbdT7Kmf1P_eTrltgmdXNlGkgzUKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان ضدجاسوسی آمریکا در خدمت کدام رژیم است؟
افشاگری جان کریاکو، افسر سابق سازمان CIA و تحلیگر سیاسی:
🔹
سازمان سیا کاملا برای اسرائیل کار می‌کند و افرادی مثل مایک پمپئو در رأس آن است که از صهیونیست‌های سرسخت به‌شمار می‌رود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/675328" target="_blank">📅 09:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_JIJWvj7UMgL2JuQmSFF_ez5RDLtX4pCTGcOSrwuhSLnIg-jJRSQ3ZyWrY6FRqS5Japj7ABuIFeHNtup9OFTeCb8_eFkaQkXUsVhF2sa63TS_wsydIj5_GkYUdxornQojbZG9hHgSNCLdcPurr2JzVKHAtnCggbu76BQPyK_29W7uEYOR0zLZidezxotac0Gmq6UpbWbeamgVKevJDU-Ze79luVNx0j_bMllpBvVqDGbV8sasn27uov20F_6IGqzX1bKpdXmO89847_WCVhtOjRXc-IXKp7iq1Dyf0hNs6eadPj02sSVhQ0VaCaGD4k5CBdk3JmntCx9GXqy7faHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دارندگان سند تک‌برگ زرد بخوانند؛ آیا باید سند خود را تعویض کنند؟
سخنگوی سازمان ثبت اسناد و املاک کشور:
🔹
اسناد تک‌برگ زرد نیازی به تعویض ندارند و معتبر هستند.
🔹
تنها اسناد سبزرنگ صادرشده پس از ۳ تیر ۱۴۰۳ مشمول قانون الزام به ثبت رسمی معاملات اموال غیرمنقول هستند./ میزان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/675326" target="_blank">📅 09:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84fcb8b82c.mp4?token=QZtTrzTXxVqIZ9Tv1PxqXMQjR7LdxEWSoYIO_sJImZh8QpHDQ2-5kNSCIdejAhCFlxJvlNmZkGHioi4E0gs-uWHxk_W3sOCxdDFbjntMjHmXj5Wu-ZMCeXHSqyE7tHwKaJ_mJ-lk9aIaC20qWd5SCkpN66mobRXT7Ybb3t413sgtp50LZfEIubiBqAW_zDis7rT6lLlnlXq9LfIKJ1gBsFud1zzNKw-rXZnLb9qvF2DZoDMzUmj1u0CA8de-r7MO2wV9ShTOpO_1Fy4C6p9BxWUQXc5E5SsJH5n4kMukJtuKsJcl2LwRkCIRkvR1ooTZAiRd1KZfpHcgllQaHenttg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84fcb8b82c.mp4?token=QZtTrzTXxVqIZ9Tv1PxqXMQjR7LdxEWSoYIO_sJImZh8QpHDQ2-5kNSCIdejAhCFlxJvlNmZkGHioi4E0gs-uWHxk_W3sOCxdDFbjntMjHmXj5Wu-ZMCeXHSqyE7tHwKaJ_mJ-lk9aIaC20qWd5SCkpN66mobRXT7Ybb3t413sgtp50LZfEIubiBqAW_zDis7rT6lLlnlXq9LfIKJ1gBsFud1zzNKw-rXZnLb9qvF2DZoDMzUmj1u0CA8de-r7MO2wV9ShTOpO_1Fy4C6p9BxWUQXc5E5SsJH5n4kMukJtuKsJcl2LwRkCIRkvR1ooTZAiRd1KZfpHcgllQaHenttg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین اشتباه والدین با یک گوشی شروع می‌شود!
🔹
گوشی همیشه مشکل نیست؛ مشکل وقتی شروع می‌شود که برای هر گریه، بی‌حوصلگی یا ناراحتی، اولین راه‌حل باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/675325" target="_blank">📅 08:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675323">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLTSGm8D0Rns3d98PkW149UMeImvefR7Xn1ObKl6wIwuqVddD_DQ0f6AodjpWJCdnidvFmuJz4tdFxBPNfcQCyQoirlkGSjBf0v7dOwImZVQb3dMBPcoSIZhOxDtlFQFlJItR-6EIhzAmflwolebN84fPmTIIN98L9N-k3Nc1MmpbybAlrP7-AkkHVLJhQQI3qV4cofQKwpXM0l3MrRT7als1bXKEx0xUnXOBb3XclAdOZ5_a-NEdsLMlNY3f-OdU8xDdE-eWBrOH2UumM2vsf9rKmRrzAyNfb9sXnYjVfUW6d7fLEY_rZtfDdOBL8mAlrGLJMyCzpOOu3dTI2BpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین عکس ثبت‌شده از سطح مریخ ۵۰ ساله شد
🔹
پنجاه سال پیش در چنین هفته‌ای، کاوشگر وایکینگ ۱ ناسا با فرود موفق روی مریخ، اولین عکس تاریخ از سطح این سیاره را ثبت کرد. این تصویر که چند دقیقه پس از فرود گرفته شد، نخستین نمای مستقیم بشریت از سطح یک سیاره دیگر بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/675323" target="_blank">📅 08:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675320">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZaWSaIcFzBujhvZQc3bjsd22mOw8aCylLYoMtB8Axw7pU5POyUGrBAn3dxPajIbABmqQN_2bdmBjod9CwrRmQUl6k_AjOfP9CPoj2CJ6k4k5me_12ttCKW3qjlcFCGy4hp5_VkhrmEKHg1ISRm1a7iScKeIgqGbv9mHtdRBNVV8_zzJ8AZhVWaxH19CpxRNXJ40ikFR9_VL2-JazoyyBkC4cxbKRzWWhecsuQYZj4rLfYSi8xAYJFnPRUl7rttbp7unaLzQBhM9rrZRsD-aLWUwOUkO0ytAGSl7-fdtW9NcPT2BBGXWi8e68waXpGvdWW4Y2KU0ijnLCIf_ENnvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محاصره دریایی ایران همچنان ادامه دارد
🔹
محاصره دریایی و مزاحمت برای نفتکش‌های ایران ادامه دارد و شب گذشته یک نفتکش دیگر در مسیر خروج از آب‌های ایران متوقف شد.
🔹
همزمان، یمن به آرامکو و پایانه نفتی ینبع حمله کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/675320" target="_blank">📅 08:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-675319">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ec9d1cd3.mp4?token=l3078TwGMhwnw_M23z1TwkGbItDJl7OZKmEUEnAclH-ryeYNquq0cjfKCeIkEvBpyW9mpW4ESNdQbx3cwAV465KB7GtpSlGkESqekGExLuIdndg_6WbpgcsxJLD9N7F0M1HeNeHgMhSC7717LBSJaR2OUj_poI73WGstLGhdBCcK2K2L0wGNg8HbK3CNLBXQQL1S5szLRsk0bPKtNdnuKWbI5aHWbOJXrCElf8gatoiiwXH7ExLji0kl6Mxgfuuo98QWcXYfBFhfRqsgmiQE-oxsLWKVo97lmnDDw2Op6sfQ7vX5VA5CrPXVZoz0gpD_7rfc6VQLAtpoFqozcveKAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ec9d1cd3.mp4?token=l3078TwGMhwnw_M23z1TwkGbItDJl7OZKmEUEnAclH-ryeYNquq0cjfKCeIkEvBpyW9mpW4ESNdQbx3cwAV465KB7GtpSlGkESqekGExLuIdndg_6WbpgcsxJLD9N7F0M1HeNeHgMhSC7717LBSJaR2OUj_poI73WGstLGhdBCcK2K2L0wGNg8HbK3CNLBXQQL1S5szLRsk0bPKtNdnuKWbI5aHWbOJXrCElf8gatoiiwXH7ExLji0kl6Mxgfuuo98QWcXYfBFhfRqsgmiQE-oxsLWKVo97lmnDDw2Op6sfQ7vX5VA5CrPXVZoz0gpD_7rfc6VQLAtpoFqozcveKAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه فرم زانوهات طبیعی نیست، فقط با ۵ دقیقه تمرین در روز اصلاحش کن! #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/675319" target="_blank">📅 08:15 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
