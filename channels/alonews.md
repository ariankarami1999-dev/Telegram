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
<img src="https://cdn4.telesco.pe/file/Vcl_DXfJZACJRC5jQ6xLhznzx1jK7veoIfzVbTYvnpOze2Ha_x0NulLIftYAaZRgK0BVOMAjuaoKd_TQWPek1usBELzMhqt7QsU3xcFPRTv4rIeiRw6AcUQWmRiftMrA6gPMCwV_B7s-21gM5z7tc6yvhWd8AYk1s8yxSekhYdKxW-2f1oP1nNDx1WwaofvCs71dZWbO4SIxFaX4pO7Oi-sXadCGaTpo3r-gO9Nd_t2L1P97r6L5Sa4-QpsEGyCfeDxGpr73N7uCshRstMgkC981RMl4fdQ8szJp9ZM3c3kXZzJsHbl0FY1UkLAlvItK8pbwflfBWx8gu1kB1XF0Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 18:07:08</div>
<hr>

<div class="tg-post" id="msg-122590">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
قیمت جدید لبنیات:
🔴
شیر نایلونی: ۸۴ هزار تومان
🔴
شیر بطری: ۹۸ هزار تومان
🔴
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔴
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/122590" target="_blank">📅 18:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122589">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5HxAD9Vljk8Ncus3pwsriU28g91UH6o0ooQgAvvQj09fF2YBLkLKnHJAJxYU_xW0TSn42IooLoTfZR7GmTyejfme2YTu4UxpHRb8c4gCWSerIC-UhgHV4N0hC4YTiXLBmEbQA0YYnxIsL7ftJUzdqcWPQdoIIhCOStlHPjxhRFjr0GnuwKIwB_M9CVQsr9pFVW1OJ6K8GqiPUx7eGKv_4BNCFLW_sLmaqYVdeKEh2-RwWlhduoAprhLHGwln7yRzEf12XSLjNQmJNUqtaKN7FoRTDvzlclOJl2a0yLxfEVWTJcjTXoYnSgvr0IsCAJjKz9ECrWB1UtGoGoKxG8ESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال: مذاکرات ایران رو بحث برنامه هسته‌ای و رفع تحریم‌ها به بن بست رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/alonews/122589" target="_blank">📅 17:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122588">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
المیادین: هیئت ایرانی به ریاست قالیباف امشب به تهران باز می‌گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/alonews/122588" target="_blank">📅 17:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122584">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7c408a3d.mp4?token=mIGe2bDkW1541Xai9-GOfn36LAHO7coMvmuI5VMlFnbJ0MAoiFZMdHLOMVePOS-fvm_VlTt_syF0wKiqvmfPmOQHAOrUP1m0qaPDbOrgm3D1zhywGhSRQ3MvzGNshbgnVVS8ElwU6WDr5vxRbUHU97KRGhg9Hl803Ia9zMffs26bBZmug1a1vtXNYbt8EjbIkQij7jGejHuoR3rZl268t8fRQixZgEfWwQ85Ta8RuqGVKT-sqV118xj-Cp4Kns85gXnl8fpVFLj2o_LfZ2J6x14YW7zucZasimT6h2BQ0YP7fBKK5j5tbqz8Wll8FM-4lc8smczZ-_Jyhx9ZOIrYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7c408a3d.mp4?token=mIGe2bDkW1541Xai9-GOfn36LAHO7coMvmuI5VMlFnbJ0MAoiFZMdHLOMVePOS-fvm_VlTt_syF0wKiqvmfPmOQHAOrUP1m0qaPDbOrgm3D1zhywGhSRQ3MvzGNshbgnVVS8ElwU6WDr5vxRbUHU97KRGhg9Hl803Ia9zMffs26bBZmug1a1vtXNYbt8EjbIkQij7jGejHuoR3rZl268t8fRQixZgEfWwQ85Ta8RuqGVKT-sqV118xj-Cp4Kns85gXnl8fpVFLj2o_LfZ2J6x14YW7zucZasimT6h2BQ0YP7fBKK5j5tbqz8Wll8FM-4lc8smczZ-_Jyhx9ZOIrYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز - حمله‌های شدیدِ ارتش اسرائیل به جنوب لبنان انجام شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/alonews/122584" target="_blank">📅 17:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122583">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
رویترز همچنین گزارش می‌دهد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفتگوهای خصوصی با نزدیکان خود گفته است که اسرائیل توانایی کمی برای تأثیرگذاری بر تصمیم‌گیری‌های رئیس‌جمهور ترامپ در مورد ایران دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/alonews/122583" target="_blank">📅 17:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122582">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf973f0a89.mp4?token=BwFcwwpmTsCHWUHMn5mFP6-LmJR3x8PHGDYhBn5LxkPIPi8rhIZ0Sh7BAuwtG8PGL0kBGiY92BpXlnaX-_qWdDg52bUazFo091Lr2Bh_MW_ZhlQ8KkM0gatTJDqA7r_CQyH9KCzbajQpk4LonF7nmTXIu-KC5mzZixkFGnO7ppUSvP3-z1nefxqhRPapLbaFy6HLmrW4GcnmE8fc67mYQw0P3JTBIlvJydJF1z5mp0tZ4YWnMTEsfVRsElgJILmWZ8SEbU9YIrLZ_mHJjuhBiAjsmM8r0zlGu9uWq_Ri4zUnt4I1-FmmU7Xphd_OyQULBdIj4D5wb3ka8fsz4Bm1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf973f0a89.mp4?token=BwFcwwpmTsCHWUHMn5mFP6-LmJR3x8PHGDYhBn5LxkPIPi8rhIZ0Sh7BAuwtG8PGL0kBGiY92BpXlnaX-_qWdDg52bUazFo091Lr2Bh_MW_ZhlQ8KkM0gatTJDqA7r_CQyH9KCzbajQpk4LonF7nmTXIu-KC5mzZixkFGnO7ppUSvP3-z1nefxqhRPapLbaFy6HLmrW4GcnmE8fc67mYQw0P3JTBIlvJydJF1z5mp0tZ4YWnMTEsfVRsElgJILmWZ8SEbU9YIrLZ_mHJjuhBiAjsmM8r0zlGu9uWq_Ri4zUnt4I1-FmmU7Xphd_OyQULBdIj4D5wb3ka8fsz4Bm1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای باری نظامی آمریکایی در راه غرب آسیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/alonews/122582" target="_blank">📅 17:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122581">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان، روز دوشنبه به وانگ یی، وزیر امور خارجه چین گفت که توافقی بین آمریکا و ایران در مورد تنش‌های جاری نزدیک به حصول است.
🔴
در دیدارشان در پکن، منیر آخرین تحولات را به وانگ گزارش داد.
🔴
منیر گفت که پاکستان حاضر است به تمام تلاش خود ادامه دهد و امیدوار است که چین نیز به ایفای نقش خود در این روند ادامه دهد.
🔴
وانگ یی با اشاره به اینکه پاکستان میانجی‌گری واجد شرایط و مورد اعتماد همه طرف‌ها است، گفت که چین از تلاش‌های این کشور قدردانی کرده و از آنها حمایت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/alonews/122581" target="_blank">📅 17:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbBG7Cx9eoeXZcSM0POQbFRRzPZ6vlCnzW-bew0ooY5f-iwiOSZjQ7CtjciMJdTgZX68Mb94plKiRZPdyz2cs6_dAHMYBZBdWHxF5nqS5NofVtPZJho9LUcWdZZAMjBQIWTiJSh0qjwjfCVmlWSvDvwnlXd2VvCcsz48u8s1-44eoT-0kYPL6To3rodT_i1g8wnfMlBA-C7Iy-EHU2JEeBvD_yGK13jftW3-LjIg-ABVnZdN_O1hvmkih9CYcjbriqbIkaRN5epdFZitOc-jLE9F5KKUvnBxOkzg8XQJw9oYB2PWnZxLC4dr7-zCJkA8qdWYGjJxh6VRkQswtIu1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل هشدار تخلیه برای دو ساختمان در منطقه عباسیه صور، جنوب لبنان صادر کرده و ادعا می‌کند که این‌ها «تاسیسات وابسته به حزب‌الله» هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/alonews/122580" target="_blank">📅 17:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر نفت: باید عرضه بنزین کشور را بطور خاص مدیریت کنیم و در تلاشیم تا تاسیسات آسیب‌دیده به سرعت به مدار تولید بازگردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/alonews/122579" target="_blank">📅 17:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل لحظاتی پیش موجی از حملات هوایی شدیدی را در نبطیه در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/alonews/122578" target="_blank">📅 17:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122577">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / هشدار  روسیه: اتباع خارجی خاک کی‌یف را ترک کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/alonews/122577" target="_blank">📅 17:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122576">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان: ما آماده‌ایم به دنیا این اطمینان را بدهیم که بدنبال سلاح هسته‌ای و ناآرامی در منطقه نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/alonews/122576" target="_blank">📅 17:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122575">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAumzpED9sAsge1uIwy55Jw19m-bpZRSF0M2MYk1u6cYZqPgB_Cpkm45ezEVr6g-um8NTxGl3cq5jnHHwRWQTRIjxsfUSCTmTLBDNPVY5Q1jvmSDjvCIhXeITrgVb7bepXKjdyw9zy5IA96sdgCYzBG7S073JDKtlXmPtLFx7bz6_831qIwTWDUknQqnFVI2XxwHAKuuyj7zx-IHWluSyCr252M0CHqQOzM3r2j3uGa_wiFdJCrwqq8Kz_W8O6qoHNjAW7gWG_k-pGAk1wkb4-kwrb2zs1ifTfDLxDnNrkrsTgAX-wN_D50DSj6aEElNjVBKC8C6bCAHuAqQ2nQN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
امروز فقط با گیگی
159
تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات:
@manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه مشکل:
@Niiiiiimaaaaa
عضو کانال بشید کد تخفیف ده درصدی هم بردارید
😁
✈️
https://t.me/+iDE5AfsFulQ1YTg0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/122575" target="_blank">📅 17:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122574">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPTjQyUNhufZS2t2irBSdoEUgq5nV-M10jp-S4ziKYU27-PIYoPhBirNDHBmYqsj6tiLPaB8KhQ1_qWJASJ8Ug-wK80sGj2wLR6d1OhnhT8BbW7sLZgoFRElZl9x9NqrWjeug1GzTUczTtwSrPDbggBGXy8OKelSI9YcUKuHcpRpZqu8TpzlCBkwWzKWizQWjH-57bZ_Yc9YGkWxFvHE4pL3a58qgok3y_PsGR71709dVl_Cns-X-NTY07iVSj_utOhbQp-OVx2BJEq_uoaG0RLp9bZRTTXo13ms4eSiTEmlrBrRvjrAYNScjHu38i_HUxyGuO1K2S0mfP3FRb1TCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو شارل دوگل فرانسه، و یه اسکورتش، ۵۰ مایلی شرق بندر
Salalah
عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/122574" target="_blank">📅 17:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122573">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزارت خارجه ایران اعلام کرد که جمهوری اسلامی، اسرائیل را «یک موجودیت اشغالگر و غیرقانونی» میداند و هرگز آن را به رسمیت نخواهد شناخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/122573" target="_blank">📅 17:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122572">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
عصر دوشنبه، صدای فعالیت پدافند در جزیره قشم  از سوی ساکنان محلی گزارش شده است.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها مشخص نیست و هنوز هیچ‌یک از نهادهای رسمی درباره علت وقوع این صداها اظهارنظر نکرده‌اند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/122572" target="_blank">📅 16:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122571">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeaQRy8ectr8ARHre9BHy5geAXjG3qjxoZ-es5xR7sNjE3e1XqPU1YzODG_nTqHak14D06PKAvmX9N_cCIPiSreJgMycbsGAj1Nf0O9L0vbxhNqR7zuYyikkUFZ5swqFM3_Thz3DrNxX48m4nac_TVsSmNI47PFY7UjsH14VAI0iipbw7XvojyoIErcwWPyze1dSn6mjiuRhaQFBXiC8b5MA7LhALak485-INM6QjcHEDAS0AaBN6r3ua-hT7upO79Kt_K-fm-lfTqzbXNROHHnTydP2cIQqh9iR_25fuT1S3ctD-ARdbM7adDixkRsLwUnxegC80DQMLV2Sx8HPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز /  انتخابات هیئت‌رئیسۀ مجلس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/122571" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122570">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNqOo_YmPpqVeQp3_jxaaXqdbZ-heP79VAw8D6ryldnk01bLUeO3SIZ-vU52ykWVvdK3t9RRkmEAx9E1D5WaC07pjf4wFBE8d96LrLEWCxpfKD0WgzzQEcAWMWrfjO5bIKEVIt5pNCK7nCsI8Oa39Q3QFzOPx2mUdi2uENipAW3aq5BijdtIXnfIkoVqCkdeA8Xrc8ZKwRSz4Gyk0VQOdiHcltkaonTwWoLF-Gt6ESLw177zMqnC6U3Y7LF3p4OOQaWb9gLjVqc3YoBS5Me5sV3HX-wAMhXN9oh6nePmrGYQR8Ywa5ELzvcq7Tgl9ayccgbH8Y8TFz53vKZ28cWwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دمای هوای تهران برای جمعه به ۴۰ درجه خواهد رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/122570" target="_blank">📅 16:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122569">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
نماینده حزب‌الله: لبنان بخشی از هرگونه توافق احتمالی بین ایران و آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/122569" target="_blank">📅 16:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122568">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
به گفته شمس الواعظین عضو شورای اطلاع‌رسانی دولت، اختلاف در رقم و زمان آزادی اموال بلوکه‌شده ایران وجود دارد که با حل آن، امشب یا فردا شب تحول امیدوارکننده رخ می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/122568" target="_blank">📅 16:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122566">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS64sYOHn23Hqxr5RGDCV4b2BUEpuco75UxLAwgJzuEHdQYWjOsKMSwKErbdEgeksmt0o9zv7yo9ozUtcfqI6y4hAjEYyeblUsV73kznZjTKvpEhLXOpdIRXhDxGkkxgAHeJnxWymX8-WpAUcVF3JKrOACNumBqt8gRApVzzg2zaclC6VtYUGKmgTLsgN0J2NBVRa3XpNJDMBzPhJzU2YPKCv2a9qNXCvkhTXnJmPx3uHuav4n2L1Xvmb804VavC6k7D3dclxZwzXsS_IMhtCj5cpaA5h0yO1GCNqnxfydvpSsCDSGoeWa0No6Ry7ykCAsRqClBskdOGvecPdxbJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOQtyR91Zs7EU14da7NTThDW7-kNcceLKOL-3aNEuhKqqxMg8TNO6KkRxFFLd-rxtcViMZZkLbOSY_e7Mvq8vowdE3t2VUHGht5_XLbXVkM5VYKJ1RYyNNPDY1KFmTjV-iZTGATCt-ZP-N8FvWPUXjPChsK4_ipPHEwM6qtZ_LUDyzNOZrDyU7-Taqzs6t4_3ooBKmxAogUeO8vBlzKB9I66ii_l48b-rrXctIQfv0IyhIhC0dYYIaOEFJ5ISsBlEockUXxDjHUdXWPuO5ZyNQi_TwkK6n_dgjBe3nRiurfGPWIArT83E9A7OLDGRWXSsz3ea1ywSaRQa-nH9VFDow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شهر سلطانیه در جنوب لبنان پس از حملات هوایی اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/122566" target="_blank">📅 16:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122565">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عصر دوشنبه، صدای فعالیت پدافند در جزیره قشم  از سوی ساکنان محلی گزارش شده است.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها مشخص نیست و هنوز هیچ‌یک از نهادهای رسمی درباره علت وقوع این صداها اظهارنظر نکرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/122565" target="_blank">📅 16:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122564">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk5FNd5tNqWQjKRudNYKnXP9KpLe2YBy5GwfkC8ixyU7bJNSN-92HyATOGloU6DQerGaPj9W6D7RvrJvUp3aN14Dwu4mV1spwMC5HgGD2nTukPfX3AeB5nQ8w7JvD8Zd5BjdIUGV8JKxGALiIG0Bt8HPD5rWNk2HzaF8yljBuVMloHdIRZ4O94y4afTztLXZ3pEkTCXd78FqyEC-Vn6CQeezfQWUXYekfodoPzg0YRtirU7PMUN3YTB2kpiS8hY-xaqnvuvMj0uHJWHvnoEpIlyx-tcSEmcCi-WQOpPJY8PWxrB-yJnL64dx1zDvEZbm-m2r00KVMRgC5b_4-QnEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست:  ترامپ از تأثیرگذاران راست‌گرا و چهره‌های رسانه‌ای مرتبط با اردوگاه MAGA برای توضیح کلیات توافق با تهران و جلوگیری از شورش سیاسی در پایه محافظه‌کار رئیس‌جمهور استفاده می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/122564" target="_blank">📅 16:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122563">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpFhEhsSoVowVBacyYK1WAHQGstUAm8yuwyB-5NxYwMN-QAyfB0Z0xMb5ck_iP7QpbJbFQai54OZNvhmIoJ9uf3PVbyRaeI-imIfQPXj9oGczakSwst1VTiHaww2879FPi_FBZWNjceQLV6hGsErfmKn_5QYKk0Y1NrYTI5zw_riL9xgxPGQ50kxJ6DGGB_D2rOWamG_AAbWKc8ib0Q-EZvmB9-72XgwU00gKkGOPhGqeZG6829BdLYoyMTqEGTzDt5H6vWDKWca3f1OoqXMC_OfBYxpvqgtRdIff1msydutPGG_GjJxmNLXsO676cyBkn4DHqtXJ2wYUpXSTQDHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است!
🔴
این فقط یک توافق بزرگ برای همه خواهد بود یا اصلاً توافقی نخواهد بود — بازگشت به جبهه نبرد و تیراندازی، اما بزرگ‌تر و قوی‌تر از هر زمان قبل — و هیچ‌کس آن را نمی‌خواهد!
🔴
من اعلام کردم که پس از تمام کارهایی که ایالات متحده انجام داده تا سعی کند این پازل بسیار پیچیده را کنار هم بچیند، باید الزامی باشد که تمام این کشورها، حداقل، همزمان به توافق‌نامه‌های ابراهیم بپیوندند.
🔴
ممکن است یکی یا دو کشور دلیل داشته باشند که این کار را نکنند و این پذیرفته خواهد شد، اما اکثریت باید آماده، مایل و قادر باشند که این تسویه حساب با ایران را به رویدادی بسیار تاریخی‌تر تبدیل کنند تا آن چیزی که در غیر این صورت خواهد بود.
🔴
در صحبت با بسیاری از رهبران بزرگ ذکر شده در بالا، آن‌ها افتخار خواهند کرد، به محض اینکه سند ما امضا شود، که جمهوری اسلامی ایران به عنوان بخشی از توافق‌نامه‌های ابراهیم حضور داشته باشد. وای، این واقعاً چیزی خاص خواهد بود!
🔴
من به صورت الزامی درخواست می‌کنم که تمام کشورها فوراً توافق‌نامه‌های ابراهیم را امضا کنند و اگر ایران توافق‌نامه خود را با من، به عنوان رئیس‌جمهور ایالات متحده آمریکا، امضا کند، افتخاری خواهد بود که آن‌ها نیز بخشی از این ائتلاف بی‌نظیر جهانی باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122563" target="_blank">📅 16:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122562">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73ffdc524.mp4?token=PV4ReXSdx-p6JibcH43M8VeAX6J5vCBNDy5KayoS_DROCEZWY-0tjITfo1mY0CDqfeLsn8NOvw69UHpzoQHUn5lVyq6priSHTJSArvWO9WiLxA1-beD_brELrJRgy9umtWNAIZ8CPM7rTCJCfzNPzDgzOw6BckptP-A68R61aIvGn43lmMXnNTtw1TjH84cob0g8nhdVqUVFCgTgOwLduQT_Udb5FtxKf4LTehBAZA28A1t7SgZlYn6OSQZilktOkf6vy07YtsE7GFSei8szAiEQhTQzqp5BXowQ1_Z_-c5TOKVHzax6XpNNCfdQZ07fE92NSirlgB4acVnUiHWpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73ffdc524.mp4?token=PV4ReXSdx-p6JibcH43M8VeAX6J5vCBNDy5KayoS_DROCEZWY-0tjITfo1mY0CDqfeLsn8NOvw69UHpzoQHUn5lVyq6priSHTJSArvWO9WiLxA1-beD_brELrJRgy9umtWNAIZ8CPM7rTCJCfzNPzDgzOw6BckptP-A68R61aIvGn43lmMXnNTtw1TjH84cob0g8nhdVqUVFCgTgOwLduQT_Udb5FtxKf4LTehBAZA28A1t7SgZlYn6OSQZilktOkf6vy07YtsE7GFSei8szAiEQhTQzqp5BXowQ1_Z_-c5TOKVHzax6XpNNCfdQZ07fE92NSirlgB4acVnUiHWpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور چین شی جین‌پینگ به نخست‌وزیر پاکستان شریف: از زمان برقراری روابط دیپلماتیک ۷۵ سال پیش، چین و پاکستان یکدیگر را درک کرده‌اند، به یکدیگر اعتماد کرده‌اند و از یکدیگر حمایت کرده‌اند و دوستی سنتی شکست‌ناپذیری را شکل داده‌اند.
🔴
علی‌رغم تغییرات بین‌المللی، چین همواره روابط با پاکستان را در دیپلماسی همسایگی خود در اولویت قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122562" target="_blank">📅 16:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122561">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933f4064df.mp4?token=fuU3k6UIU_zHDDpibLkQws31ya9Ox3_6znHPk0k3OvL8i7yRpQSjrG7j0drnuHsFFuZmOH9hNOb_ll-yDrEmGT8WEou2EE-D6ZnEInlpIZP8v87xRvbaOMBq4lsWZV6HkeAvPGS-qWDfq1-fXL7lIacVcC0-_5G7B8bRi6i5K9w2ZfLEwuMJbWRJuEAeP9hrHLz4jCiZiompV-Nk1fdfetU2y2kb3eE5wwHWQbJQ29f9rrVHi-844wxrX9gvGPhatjjc2Igv8lCwcpfqnmlDHihzc7vtDDN553VXbLcyvw1Sf2St1_O-C4mQ4H5g8ks-ayIhyCe7R3rt991okOteiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933f4064df.mp4?token=fuU3k6UIU_zHDDpibLkQws31ya9Ox3_6znHPk0k3OvL8i7yRpQSjrG7j0drnuHsFFuZmOH9hNOb_ll-yDrEmGT8WEou2EE-D6ZnEInlpIZP8v87xRvbaOMBq4lsWZV6HkeAvPGS-qWDfq1-fXL7lIacVcC0-_5G7B8bRi6i5K9w2ZfLEwuMJbWRJuEAeP9hrHLz4jCiZiompV-Nk1fdfetU2y2kb3eE5wwHWQbJQ29f9rrVHi-844wxrX9gvGPhatjjc2Igv8lCwcpfqnmlDHihzc7vtDDN553VXbLcyvw1Sf2St1_O-C4mQ4H5g8ks-ayIhyCe7R3rt991okOteiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین‌پینگ، رئیس‌جمهور چین
:
فیلد مارشال منیر، می‌دانم که شما تازه برای تلاش‌های مثبت در میانجی‌گری برای صلح از ایران بازگشته‌اید.
🔴
ما نقش سازنده پاکستان را تقدیر می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/122561" target="_blank">📅 16:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6Mm1rhSk3hmd8sIPXodZXkG9bxIaiZOwEsXMU8wJYXjgwxdD0BrKF5Cw4mlU5_JZNAZic7lrrarPlyPvc9sqtKThmf6pwaenfm6zbxownDCtqzAR5UQ_lbHBxdkJeJ-YMZUhIVJwDsFGWC-UDWQmW-0rnFJfcFoOnGWGLQobYR2mcKK3slpRbVEzk-MnA0z80Ro6J_v9pgQQ0GOSTZwOM73wBgYMlJSmolQjr6ZxcjMWmLoewZ8K88McORUHc811RHdfZrdbUdbfLaSl2qdwsxBdj7K0wwKmnFEKEdkfXiocX3NfcGbOnEe_1S4CoI6xW0K0y1qaiAkolvlaAu3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srkXPAK7lwC2_V8gVj0z1pqfJVXji6UI_2dvm5_lPL9IfrHwsElvzP0h7Yq_BWTOMzX8GmtgfwmlGRoKbmJSth5ehNmaNvRdd3YlnOvJkfJihMb2L7BnH4YL-1UiY1aE8oH-B_PDcIEVYehmizwS7zoeOb9MZJT8Npu4UeF9eHd42WjHyNO3X2nNsxUfLaMsmUTKb5m09oVp_J1HBovUyR1U1wpmvoqRms_wPJeougOY3WywmCigNroqIalc9k2VHzvaFiro49CMTdzLp6LVEc99Zi8QPp9RRYmNAfuue3rVZVJsuwOLlAgasphfSW0xcuTC8Io2ZonF_hYVCWhODQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل دو هشدار تخلیه برای ساختمان‌هایی در برج الشمالی، منطقه صور، جنوب لبنان صادر کرده است.
🔴
ارتش اسرائیل ادعا می‌کند که این ساختمان‌ها توسط حزب‌الله استفاده می‌شوند..
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/122559" target="_blank">📅 15:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
خبرگزاری مهر: محمد باقر قالیباف با امیر قطر دیدار خواهد کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/122558" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ به مجری فاکس‌نیوز: هرگز پول نقد به ایران نمی‌دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/122557" target="_blank">📅 15:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRmMk64Le2Z1NNwNxFWa0X5W7l_FsfXd1LFwbK5mJBSlouueQqpvlW1l-NOWTTqZgtkw3yJpMIg4h97PSm-pL61QFDo8tEcylUoeE5bFP7Baq-X5gScbPAEZpQ-OMBybcYIhvJr7A1xTh-8yU_fMCQ8Ws59Gw5i-fKFDdyXTUUyuYByVbfNO6K6Nm1kHEd-leNJrNzen8XOlu1oFoD3FcgT7mSj9jXIexsHsB6VE40_PRrjytdNSU9GESX6kxSnQHW0YPp7kOTK3SMjpsgXkKnbrDh5kPenL3r66GW2aykVV814r1FwBWR_jwLWJlgDbls28xMoILGT3JmddfkXk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست:  رهبری چین ممکن است محاسبه کند که همکاری معنادار با واشنگتن در مورد ایران، انعطاف‌پذیری متقابل آمریکایی را در مورد هدف ملی اصلی پکن شایسته می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/122556" target="_blank">📅 15:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
«اتاق بازرگانی ایران و پاکستان، یک نهاد تجاری خصوصی دوجانبه که منافع تجاری ایران و پاکستان را نمایندگی می کند، امارات متحده عربی را متهم کرده است که فعالانه مانع ادغام ایران در کریدور اقتصادی چین-پاکستان از تبدیل شدن به یک کریدور اقتصادی پورتدارو پاکستان (CPEC) در دو کشور است دبی." - فارس نیوز.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/122555" target="_blank">📅 15:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
تسنیم خبر سفر قالیباف و عراقچی به قطر را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/122554" target="_blank">📅 15:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCjyn1EDTa8IBbuNF_0_0hQLdAQnFY3UMas4jcs-AU12RAZ2vQiuv-xZ3FsXlK0mg7zaU48wUegh4ZJ8-NBkbgoiXyHzzVbbFSejcfSEqjbKWbOtTOtpTPwc-TilBIfzPpmC1pyKHdMNim0hWmWA8BJMkLotTDBIYRjFEhbD56RXot2pVxFLkYVxgh7OzIKTdEVjcm5-xeYxodUrpMM__5PDESOV6rNtf8jFN3EVpOf48EvPXHQfa5sXJpto4Pq72tUxKoIDiUQ-SdODIoHZ9ASfAaLLkYOgwUhe8POOsEn3oe3gREjTeEETAJZHMvIp98E9pO0UgyyHOzaHJnbLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل هشدار تخلیه برای ساختمانی در اردوگاه پناهندگان فلسطینی رشدیه در نزدیکی شهر صور در جنوب لبنان صادر کرده است و ادعا می‌کند که این ساختمان توسط حزب‌الله استفاده می‌شود.
🔴
از ساکنان خواسته شده حداقل ۳۰۰ متر از این ساختمان فاصله بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122553" target="_blank">📅 15:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رئیس مجلس ایران، قالیباف، و وزیر امور خارجه عراقچی امروز زودتر به دوحه، قطر، رسیدند برای گفتگو درباره تلاش‌های دیپلماتیک جاری برای پایان دادن به درگیری، طبق گزارش فاکس نیوز
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/122552" target="_blank">📅 15:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIVYoik9Ql-2T4XH9k_vvxcfvJAG0EYQ0QJ-5XTDg3wik53d1pKAkRsH28SSB7lgN93pwKtWBLhzQwvPWW-76Dt6YdJnx-7qxEtamtm_gU6ZOA0cVFtROmE0hmA3NGyafBsZLtedDOCgXuelOmNI0LIrVRTCilGSx-pTnc9PTpUFvib43DcSR7XCzU2AruW3u2QthoHT47-Uw1sCY2irWX9rDr8LccofEMnmJnESRfx65tx3XybGn6Rb1RD2w4mO14lyDwlVGm_9XkUmqkH0IrNULvdSN5_jegVY0D9LlmmMJSMXVRiKDrTfwjaQBeB4TQD2GKKM-7UgATxbh2E-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مسجد ابوذر در بلوار ابوذر ،اتوبان محلاتی؛
آموزش کار با اسلحه.
🤔
جمهوری اسلامی از چه خطری این روزها وحشت کرده ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/122551" target="_blank">📅 15:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwUlhMBs4tQAvQIoM-_vpqpqRaAJ3WgUA_AatQarqd1upkPBLFgoHgyEyp3JJ856w6-tYR7TSnr5CC-imrldAQfeq-U9PV6XbyEuHJWAsiiRFEkERpO_WeDL2IllZs9fzXGzZobhFpVXjk19SEfMkI1nW_Q1egRV6BAroBwbW_4WvWRl6qCHmTX4odotzce5yWFS7LAH1N3pQutpNg0IzeZZ97FwDD04XL7RZHOnn8f7rgPjnZe-YZ5xrYrmJXRbl0Wr4q3j3W1G69EXtW2gp-J6zh-pHmZQ5kwCw4JLuRIavkoZ4H8ZANS0X_OQelX7pg9-SRZeYdcStpRbBnr1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنان حمله‌های ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/122550" target="_blank">📅 15:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
دو مقام اسرائیلی به رویترز: نتانیاهو به نزدیکان خود می‌گوید که هیچ تأثیری بر تصمیمات ترامپ ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/122549" target="_blank">📅 15:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122547">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEeq8B4f-YNTxV_jIw07x7azVL3oJqtWBnIVuZIZd7NIRVWMEi2KeV01JNxR9dSjpYXt9pGD9qeGumMQ30NB6ToAt3fFztEaj25h-HqcowAL6AFBIMmtnOMiXN7uqeOZTVyCFIJuxlIZ7btpdZS9F2GxFLSI9gqw3aH1s1UN2mFiDBmF8eQpXtQ3LqLnjdzVsVC-aQ6vqztf5sloFt45BUI15exFAdrnLRtcNGNS3UhBVFFzEGQnlIVfVbZVv4AGkKFyzv1WT_g_XOwm21M_wa8rqhEndhMdSDYPiqr5ISJznIOdK0IcmfRn9HWdJBmMUTaSJfYx-P71n2gBS3PIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527cd39d33.mp4?token=lO5srp13qyvIpzIFokVfwfgExazcFw8uhGRGDCGDioPfrD4qK8tcwW-uMHLCTzcX8iFyooieUkRO7nIPW94QYS2IPn4KaWz2wJuPC02G8KnbqlIrUlLgZaPjCb-YGwvatV1UZiELAblv1_1Fp2visGgx6MfVgcfIKmkFODoQYs6J8gQqvCIgKMNfp3fl0rqHpWirn0yjShggHc-8dhZOwW1-ACcYvHWOtNv6vFMM9fk4On9C4boCHN_fdRs1UV629eUQ0E_x-wwJhit1lJp7pYxHMhrJqrFfcvBPkRMZbUXeA8h-P0iblrIGWZ8I2CHmlQNeankJ_lAE10S21wxaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527cd39d33.mp4?token=lO5srp13qyvIpzIFokVfwfgExazcFw8uhGRGDCGDioPfrD4qK8tcwW-uMHLCTzcX8iFyooieUkRO7nIPW94QYS2IPn4KaWz2wJuPC02G8KnbqlIrUlLgZaPjCb-YGwvatV1UZiELAblv1_1Fp2visGgx6MfVgcfIKmkFODoQYs6J8gQqvCIgKMNfp3fl0rqHpWirn0yjShggHc-8dhZOwW1-ACcYvHWOtNv6vFMM9fk4On9C4boCHN_fdRs1UV629eUQ0E_x-wwJhit1lJp7pYxHMhrJqrFfcvBPkRMZbUXeA8h-P0iblrIGWZ8I2CHmlQNeankJ_lAE10S21wxaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تخریب در قانا و نبطیه در جنوب لبنان پس از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122547" target="_blank">📅 15:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122546">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۲ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122546" target="_blank">📅 15:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122545">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رئیس مجلس ایران، قالیباف، و وزیر امور خارجه عراقچی امروز زودتر به دوحه، قطر، رسیدند برای گفتگو درباره تلاش‌های دیپلماتیک جاری برای پایان دادن به درگیری، طبق گزارش فاکس نیوز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/122545" target="_blank">📅 15:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122544">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عوستاد خوش‌چشم: علت منصرف‌شدن ترامپ از حملهٔ دوباره به ایران، ۲ عملیات پیش‌دستانهٔ منتسب به ایران بود نه درخواست عرب‌ها!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/122544" target="_blank">📅 15:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122543">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ادعای واشنگتن پست به نقل از یک منبع:
بازگشایی تنگه به صورت مرحله‌ای خواهد بود.
🔴
در مرحله اول، آمریکا ۱۲ میلیارد دلار از دارایی‌های بلوکه‌شده ایران را آزاد می‌کند، مین‌روبی در تنگه آغاز می‌شود و محاصره آمریکا برداشته می‌شود.
🔴
تفاهم‌نامه شامل توافق هسته‌ای نیست، فقط تعهدی برای مذاکره بعدی درباره مسئله هسته‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122543" target="_blank">📅 14:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2b6f9bc3.mp4?token=ERYrENRTSQk9KEQfN8s20NyiVRlR_eFwTjB22gZNATblDnB7uM5H-nKFXswFAxHvyCQkLFuUhDqSQKVVF24UOuJbHC_TLWXB5aCoTu3auWQsJ6-fB7gAukb0BYpeFu3Yb5lVe2gD_cL468-qthH88iRvsY4-_JbcXlaudGuwx67hrvH3pdq19DeBVNvEqx65mGrD7G0UiCBommojCjtbPOuQ-fJIV78lPWcdENK14flvEwj2LfIQpNmXeDu5Jx_-RGloKq_8UorJHgpREDoYjZR2svlqYNIRJ2ZXansV_hpXECs1f6kDgudRR1qfij71r0INyD8Ve1TUpn4-ZADqmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2b6f9bc3.mp4?token=ERYrENRTSQk9KEQfN8s20NyiVRlR_eFwTjB22gZNATblDnB7uM5H-nKFXswFAxHvyCQkLFuUhDqSQKVVF24UOuJbHC_TLWXB5aCoTu3auWQsJ6-fB7gAukb0BYpeFu3Yb5lVe2gD_cL468-qthH88iRvsY4-_JbcXlaudGuwx67hrvH3pdq19DeBVNvEqx65mGrD7G0UiCBommojCjtbPOuQ-fJIV78lPWcdENK14flvEwj2LfIQpNmXeDu5Jx_-RGloKq_8UorJHgpREDoYjZR2svlqYNIRJ2ZXansV_hpXECs1f6kDgudRR1qfij71r0INyD8Ve1TUpn4-ZADqmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد حزب‌الله امروز صبح به سقف ساختمانی در متولا، شمال اسرائیل، حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122540" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLt1fGi8kkwjwYJ59OSVxDgBNU_bOJWnuv2IYC8NE-xGx-0Yx1qRnm4Wo2IhjuIqOffg7B6_SECuVeN-StG0Iqrtka2O5GPXRI-7d2TkzCaXFudN-UeG4iVooJSqJzpyKbscqq47wZia43cvrK-XrdeE76Dy4gz01hFGwS8DubtkUiv7OeCysL5Geda9czhoCdbirBku2dFYkLNzVKx5N0FxHPlcOG-dw2ttHItEaDU8VXp3CIqYFh2mNjodrbb99EyxRHxGr5O8N0dzaUDdbHc6rC6Z9dFV_0CAivWJJ6k7jXbaJL4MZCc0PegubeAw8Vs7IDSyqr0yxAcqg85Vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۷.۸۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/122539" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122538">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaG86VCOcVhWJmKpOkWe9Oh8MS3iZU_S-_7MLxbX83vS1m-dCPqYkkAlKoocVAP9p9pG8Q3W9mSYji1HAxejlNzwFA-du45js5jedSC0U7EGO67od9QvDKo1qW6G857TT9zkmlmIsiD9b8l1pUjU1m3QetBXN6_yMqdJsMeW8FdgiNjAafSw6dNufrVl0zddBnfMNvC_T6WZBibq-BGm1N9FIQXJ9pgo-yvvvDoe57dNYmmX0docnhf3WJh1Lw_00Vp2Xw94qjlC3rjnUdGA8uqc9zrj0yo_93A2GliyhiF9n4vhD5Hx5buVnfUc2df3I7wlgxleUBcAFzwca2lX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیئت‌های چینی و پاکستانی در تالار بزرگ خلق در پکن دیدار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122538" target="_blank">📅 14:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122537">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZeRmNXyMa9Lej5CZKiDre2fKQ6BXhwXXPXNbbamFb0yz9zJ_uW0uZAoJCC754QtKcgFn_qNZ3mVpLtF0U6SbNKeDTtWEX3Veg3wLXUOn-3GO7dwLB_1_RS1DrFZrjdj04L07OXqmJBsq5O7cJ9V9w5entX-E-u83uew38MA75Uex2DWiyUvMtNN2bIwzvcbmuYSs3DyVDzLnY_VTQ7vsxZK6wVNcoYf9od68FndtCid1yAukkN5odb3X25PasAvW34n4u4dlBdqa4HlkwsEDNlrX_UbAfMirZSxWVc-S3BcPg4dkuTiaR_YipStqQAC2pYNEjfxcOXEMaercT2CWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: دموکرات‌ها سیاست‌های بد و نامزدهای بدی دارند. غیر از این، آن‌ها عملکرد نسبتاً خوبی دارند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/122537" target="_blank">📅 14:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122536">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDA8WROzE2agn7xvO5nHo-rcsTyGEWjDD2OS9SYMZv9ae6Y5JdAkC-vznkXkJoA_kTdfLtXhTvOq9vtfG4wKcB5tC35Zf_jVT2pDnfPwq6k7VltfB4vSwylRPOKJgaeQsi4LbW3v4U7EzuCEhxAlSpvYrhH4FD7bW1v7IQNFpIpWndWEqU1g3lf9bjrGl6duS34sRb0JZcndp3YcPC8kP_vhj5o9UO19J9vwzhAYD0y2MeYBXv7_dibGTVhHapkjJZmUpcPHl8FA-8z1LkVygrVGgKDOPe2n90YMlN9sAJW9V6nXTTbU9HiEqfrwWlKuS8uu1N9bG6MNYNCQLBnB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
روز یادبود مبارک به همه، از جمله دموکرات‌هایی که به ارتش ما و تمام موفقیت‌های عظیمی که در سال گذشته داشته است بی‌احترامی می‌کنند.
🔴
خداوند کسانی را که بالاترین فداکاری را کرده‌اند، برکت دهد. من همه شما را دوست دارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122536" target="_blank">📅 14:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122535">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان در دیدار با رئیس جمهور چین گفت: پیشرفت قابل توجهی در مذاکرات ایران و آمریکا حاصل شده و اوضاع در مسیر درست پیش می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122535" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122534">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
دبیر کنگره موبایل ایران: برآورد خسارت روزانه ۵۰۰ میلیون دلاری به اقتصاد دیجیتال ایران در پی قطعی اینترنت و اختلال در زنجیره تأمین موبایل، با خطر لغو ۶۰ هزار شغل و توقف واردات در فروردین و اردیبهشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122534" target="_blank">📅 14:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122533">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / منابع پاکستانی به خبرگزاری آناتولی گفتند که آمریکا و ایران می‌توانند طی همین هفته، «یک پیمان موقت برای پایان دادن به جنگ امضا کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122533" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122532">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سازمان توسعه تجارت ایران، ثبت سفارش واردات انبه را تا اطلاع ثانوی ممنوع کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122532" target="_blank">📅 14:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122531">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
یک دیپلمات ارشد ایرانی به خبرگزاری ایسنا گفت: اگر آمریکا به تعهدات خود در چارچوب یادداشت تفاهم احتمالی عمل کند - مسئله هسته‌ای و ذخایر اورانیوم غنی‌شده پس از ۶۰ روز در ازای رفع تحریم‌ها علیه ایران و آزادسازی دارایی‌های مسدود شده ایرانی مورد بحث قرار خواهد گرفت. مدیریت عبور در تنگه هرمز یک مسئله ایرانی-عمانی است که تهران با عمان درباره آن گفتگو کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122531" target="_blank">📅 14:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122530">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: چیزهایی هست که از اول هم با ایران در موردشان مذاکره نشده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/122530" target="_blank">📅 14:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122529">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-v6eaSor75t8Q7grTvCFbx-o18v31R0YiTzXxID4q_F70Agh0naU6vYTaZZueJ8tNzgvcoaLNdbB1WDLYirMLfaNYljDIC6zOZWYAQGVsTYpmrq3YpAOfDolqKyAaiBcipfnHMU7OJKAgGhDemlKQlLnCWg1cMoVdI-lGwBZDtfEbgvi4i5Hc7CjW3CAkarHRCtm0oI2ylEPWxjXyL0sj2B87kHRHV_C_6HyTQ0uZVa36ivYnbcTHfpY2LSpGGCl3NWXUEHOtCO-BVih5AUEWcpZaQJlgwHwqBIdEadmq-RwpQviWsRVF4ZnHWG6YemvPouRIhQFhF9m1VyMJahSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122529" target="_blank">📅 14:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122528">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNJtUHIXmBVe95SeWvYc1bSWUy-hnIaMA3mgNx42BW_fdaFHonDu5K7s91oWtnK9VjzSWGdggcKbAljtPb_mrfyMvuv6IWu51BeqMJ06dxwlme3-QrTACy1fiIGFYfU9E_38a8dV0TWJZtFq2r01wPDpckqW7EN2_h4EZISs5CmMZ2WpAeQ1vOZ2lPAO2HlVKl5-v9ncoyqa5O1XGBOAibjLARyVA-xdf4KROpc50vvrDbot8agrYl_Xlustn8Z9Fv89iXmrSdiB8KVYwCKIrSl0TpSvwwgCxVNhzjXMtxX6_8Xr70vOxpcsyvZnKkj4pBpW9nosysUXcAZ8xs7v5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری
Financial Juice
به نقل از ترامپ : یا یه توافق خفن و واقعی با ایران می‌بندیم، یا اصلاً توافقی در کار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122528" target="_blank">📅 14:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122527">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل، ایتامار بن-گویر: نتانیاهو باید دستش را محکم روی میز ترامپ بکوبد و به او بگوید که ما به جنگ بازمی‌گردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122527" target="_blank">📅 13:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122526">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVW5280jwFmKQ7NwOZypOGFtlhAg83keAw3GuRbtMbSSi1YwETlk9MISwtTJW8zW1mAUDlLAGFUzpqDr9yzUyT_9KEBtd1fCzdiLGIxxicUzk_aTdrYT10w6BB_sqmt3ceYPKWJ3KDxxpg6Zu774z2R3DZGKs6xsIHkuVowPS4A1_lXD0_XPm0YWJDWXQcoxZs_sEI7JBDKKL5N9czizer9UsOqXWAD_nhX9BN0KLNc1qKrXail7ToznQhRR_hnfLPV0hGYpv382wAIj_El4c3smTbsNY7anZdWI6EXf5sseuKrfwdVLW-QFtktyT5jJB1GkhQd6iEEhruR0H5JtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ درباره ایران
🔴
ترامپ : به همه دموکرات‌های احمق، جمهوری‌خواهانِ فقط به‌نام، و ابلهانی که هیچ‌چیز از معامله‌ای که با ایران دارم انجام می‌دهم نمی‌دانند، می‌خندم.
🔴
معامله با ایران یا بزرگ و پرمعنا خواهد بود، یا اصلاً معامله‌ای در کار نخواهد بود.
🔴
این معامله دقیقاً نقطه‌ی مقابل فاجعه‌ی برجام خواهد بود که توسط دولت شکست‌خورده اوباما مذاکره شد؛ برجام مسیری مستقیم و آشکار به سوی سلاح هسته‌ای برای ایران بود.
🔴
نه، من اهل چنین معامله‌هایی نیستم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122526" target="_blank">📅 13:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122525">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی مجتمع گاز پارس جنوبی:
صبح امروز در عملیات آواربرداری پالایشگاه ششم پارس جنوبی، یک حادثه رخ داد که ۶ نفر از کارکنان شرکت پیمانکار مصدوم شدند.
🔴
۳ نفر سرپایی مداوا و ۳ نفر دیگر برای بررسی‌های بیشتر به بیمارستان عسلویه منتقل شدند.
🔴
علت حادثه در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122525" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122524">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL7q2ZFgO9PNCw27Hqg_ciRYqFze6RsQ2jF3oQUIaKVLyZe5AdsIun0DTnDsM8ru5cN9uSmaO5SmioF_4xICzBBalBZw1540AJWiNqFRfmCiNyh5aS1Kjj-v6tjIRL403XeshFNX2Dw0GFmkpHhpmhrfmvcNNVLvyK4zOnAOHN3oxtCW1vDNOoOUZwhAP7hK2cdJywcjPh5RACBsYQBup0Ne6z8A-7O-EFK8IAni2xfYf2Ww4HgHTzmCerI1qK0aErJmxGDsC2CHDCmmFmNLdX5TK-oOzPZ3x66sWeaiVPpBMQ-JysRX6VV5DaIawm4p-BtV9Dgi6xHgKjJGBcnXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۸۳ هزار واحدی شاخص بورس پس از پایان معاملات امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122524" target="_blank">📅 13:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122523">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری/ بازگشایی اینترنت بین الملل مصوب شد ‌
🔴
ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد. ‌
🔴
این مصوبه برای رییس جمهور ارسال…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/122523" target="_blank">📅 13:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122522">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
شاخص کل بورس با رشد 83 هزار واحدی در پایان معاملات امروز به 3 میلیون و 993 هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/122522" target="_blank">📅 13:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122521">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c2bad0b5.mp4?token=IjB_Z1_Cdw8OBCghKFpHWxF1YBsRPCzl1yHP5riXYf7fAytukCIHFOyp4YviySrdP9ocXMdLgc4tuRoOIKASOfnOdHehT0lSuk8sEgk3xmQBUePhpgw3STNW0aXCkePQdlKORkQEiGG3o5WLr28ozPN8NZBVaM5WGyPnsEZ09RA8_HLMTgKpFxjCQRQEYC0Av1-GfmuHzlzPUAwa17o-u6QcD3dXgTETXPV3i5KOSD1OCVzSuBGanj_36O9zFFnCjdZk4rwvLSrKoqPhO9h2jpAmhrEHRGNHO33wVCe8qEJ_yzombzg2ohicv-2kZ9NsmVpCXOA2Rg0hGId5FDBxjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c2bad0b5.mp4?token=IjB_Z1_Cdw8OBCghKFpHWxF1YBsRPCzl1yHP5riXYf7fAytukCIHFOyp4YviySrdP9ocXMdLgc4tuRoOIKASOfnOdHehT0lSuk8sEgk3xmQBUePhpgw3STNW0aXCkePQdlKORkQEiGG3o5WLr28ozPN8NZBVaM5WGyPnsEZ09RA8_HLMTgKpFxjCQRQEYC0Av1-GfmuHzlzPUAwa17o-u6QcD3dXgTETXPV3i5KOSD1OCVzSuBGanj_36O9zFFnCjdZk4rwvLSrKoqPhO9h2jpAmhrEHRGNHO33wVCe8qEJ_yzombzg2ohicv-2kZ9NsmVpCXOA2Rg0hGId5FDBxjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد خوش‌چشم، تحلیلگر مسائل راهبردی : تا پولای بلوکه‌شدهٔ ایران آزاد نشه، فعلاً خبری از هیچ توافق اولیه‌ای با آمریکا نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/122521" target="_blank">📅 13:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122520">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4yMSOCafh6tkFcdUq9VgcOcsHolB-Kx6TB6IIzmm7RS6tKxYQHsUEMwU8ekdgVEluim-uKwDsPMq9NRcu5uHxlIx8gmn_FEpuWZHRVPur2r1wtGMkTFMNcZ3u5XqYS9r4I8nr08-08l4qQH80cnO9cy9f2hCuXcPlaTf97NHY1gc5qwIX3byQMUnue5Xu61VLCSFc3iSYmxX2LnVwDaz3YfFz5a0wafCB76QUlDhcMvCXDZDs3PHZwOxtbcV7dkbo1u3kBAwtj2lKa_kh-jgMYnbDftY7Y0IsaNu4Qc-jwQKlCyvkrINQV2D6krqhKBH4p-Paewdn5kXJhLNo7e2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آونر ویلان، مقام ارشد دفاعی سابق و کارشناس هسته‌ای ایران، هشدار داد که بهترین توافقی که ایالات متحده و ایران می‌توانند در مورد مسئله هسته‌ای به آن دست یابند، ممکن است شبیه برنامه جامع اقدام مشترک (برجام) باشد که در دوران دولت اوباما حاصل شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/122520" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پزشکیان: تسلیم زیاده‌خواهی‌های دشمن نمی‌شویم/ حقوق ملت ایران باید به صورت کامل استیفا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122519" target="_blank">📅 13:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
هاآرتص: افسران ارشد در نهاد امنیتی اسرائیل از توافق احتمالی بین تهران و واشنگتن هراس دارند
🔴
آنها هشدار می‌دهند که منافع امنیتی اسرائیل در طول مذاکرات لحاظ نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/122518" target="_blank">📅 12:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122517">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvvmdwWj2oHwfl44EVgPtzPyShKtKN212Yimts_THBZPatuMhPsdVY1ilrIkeo49U0nLO-Mwe30bx_9etr9MX4E341XIzU6VD1JNTwPGgjLp7-9OdyGaa2gdCUc3zSg7OhlW-Y16R3urPK9TronsyspVOL6ityd-cIMOIQ5kpkvHCk3Q2A--rUlF6kZQBlx0QPsUQwB83zmtL1_Ftie6In4C8FP-kyZ5AXkPA0Xa1PMx6xHc-Txm4ru0kTC0XsTbSSpNDvicIyMXHETyWCwHhmDIFp48T8DbOIgfNp4003tuILQmEVuAv5ty9Q_FMmX3dhSgLX-f7H9EoA053-PKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظرسنجی جدید نشان می‌دهد که تردید گسترده‌ای درباره آمادگی دفاعی آلمان وجود دارد، گزارش DW.
🔴
این نظرسنجی نشان داد که تنها ۱۷٪ از آلمانی‌ها معتقدند که بوندس‌ور می‌تواند به طور کافی از کشور دفاع کند، در حالی که ۷۲٪ گفتند که به آمادگی نظامی شک دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122517" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122516">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCN4_UwNwLViu95Ath-n6vDZ8m3kEoNuqxYKLpQXg2_NgeNmuEmfmZAP0hrt_3s2fDwtlxn70jZbicQcoLq9iT-Q1MTwQbgZ4uFnvN3AlIuZlc2_JCj21wOtBGDWWu3JTFHotA674CGdqM2yKaObl61YSMe4FqAzf5z9SXzSmEZVH_gzqUOk3cDrPFnRBVBi6eqmPwvq8XAa0qmPxGMoZN8IIp6u6X4b7SohY7y7HKoshDtezZLc1R7oGTP1SJo0vmQCyNt1wltKQ2KWzpYQh06BQxCGkzWHj8wKCMGqXA5h2mISbixnvgFDJKbM1YTONALcG6whkxkZDlJPijFrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، بزالل سموتریچ: برای هر پهپاد انفجاری حزب‌الله، باید ۱۰ ساختمان در بیروت فرو بریزد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122516" target="_blank">📅 12:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122515">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f45a5fac.mp4?token=ZuS56hIDwU00dIXTMv6HMSKOXwgFt_pIVqTUldjCXUbAFEUo_9IBgon3UP7MJ9KH7-uE823UMmMlzSCYdcOa8-ZQDiRo8mRDDfboEhmI-jXX1kkt3M67SEmKFaCsdJSo9F6sAK79ChOYYrIfVYpZdVxYlnqoEjLctS_88MFWh74gNHmkFrQakuD4K08lyjqN42mEMTxPE8iatYiMxTTIMtTMZsQjt-hcFz6ZbnB_sYMW4bwYjlTi-hAm8PcDqKnj_CaKUk1K75-wHsz1HKq1NVtf--dXxTbp2yDO8aERgHJ5bCEUFN5zr0JWodagZG1tIMWnjFvGQy6kHMDG2kiaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f45a5fac.mp4?token=ZuS56hIDwU00dIXTMv6HMSKOXwgFt_pIVqTUldjCXUbAFEUo_9IBgon3UP7MJ9KH7-uE823UMmMlzSCYdcOa8-ZQDiRo8mRDDfboEhmI-jXX1kkt3M67SEmKFaCsdJSo9F6sAK79ChOYYrIfVYpZdVxYlnqoEjLctS_88MFWh74gNHmkFrQakuD4K08lyjqN42mEMTxPE8iatYiMxTTIMtTMZsQjt-hcFz6ZbnB_sYMW4bwYjlTi-hAm8PcDqKnj_CaKUk1K75-wHsz1HKq1NVtf--dXxTbp2yDO8aERgHJ5bCEUFN5zr0JWodagZG1tIMWnjFvGQy6kHMDG2kiaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو تو پاسخ به سوالی درباره نگرانی هند از نقش پاکستان به‌عنوان میانجی بین آمریکا و ایران : هند همیشه نگران گروه‌های تروریستی مسلحیه که از خاک پاکستان فعالیت می‌کنن و هند رو هدف قرار میدن، این نگرانی همیشگی اوناست
🔴
اما درباره نقشی که پاکستان به‌عنوان میانجی و تسهیل‌کننده تو موضوع ایران داشت، اصلاً مطرح نشد و فکر نمی‌کنم هند مشکلی با اون داشته باشه
🔴
اختلاف هند با پاکستان یه موضوع جداگونه‌ست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122515" target="_blank">📅 12:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری/ بازگشایی اینترنت بین الملل مصوب شد
‌
🔴
ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد.
‌
🔴
این مصوبه برای رییس جمهور ارسال شد و در صورت تایید رئیس جمهور جهت اجرا برای وزارت ارتباطات ارسال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122514" target="_blank">📅 12:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عبدالناصر همتی برای پیگیری آزادسازی منابع ارزی ایران راهی قطر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122513" target="_blank">📅 12:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122508">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEn_8ZHoaKTJEuyS76_hquilKhzipxeXCp_WSy3Q8wVm-_gHgMvAUcPsms6WlxKTdKM_2Pard_onhEcJI19uBgnYGGvswfFsjtjQ28ydx8AuDJyTntXlTvVdEKUkxj5x6xSgdO3uPH78ALL07XGgD8MrhDtMnT0L8exFlsPNPysnpHtzc2TkSH3K20LVXCkZFuuo2HSNWDn45vLDT5kOK9zwNhL54yZWrdTyRFMVzSSmO-84JsQmW1-1dA9xodBAtU6GbZvzBhPjjn7nlhKZzZwdzkwRQ0ZhYSUtieA_d7H0vnpyNLptK3P3Snp7vRstIDEm9tG8LO9QtMQhC8WebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohXDvQiuHSdxo7wrNeKHXWDRhwECKa12nzKs8kAUViRy6_yQZB7dBfNThnyialbtDcKuoqXhIyHY76BtfwcvQeWum7gjz1Dj3dkMsJTfk67D758kU2NKp_RYacC5azdqZHTRsjfAmDhxh5Fu-v7KCZ4OveH5lEB77JHkgCmnbw9I_8iHgOPm4NEWPiiXOUGT9c_kEcWxjXRHypiabM8HFSSY-z0li-cfVAxwsdfVYnfpjLBgCymR9IcmzeRM3rHn_HiOP-ZBxfOB7ZWP-rW3CG0aEN0Y8qGLYAS91mNGbD1omoF8i9yHSiBB1--KgXniM89EvGrbZFnzkrFhz8tG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lwoo5l2roPOjF4QmxiUsAVmQrXsO5xdt3Nf2zPKcZp6T2aHyM466q6LvAYGW_6QfPldKty4WRnxlKQwz5sUGDdZtpPrAjbVZtHexYI1U7Y0kgwuVVp29WJFsAS6t5DEHu7_iEhjq6pQU7lAOaqsLVFV1WdFJ-CkfsbOP7aiDxYCm0CX6x_u3pOU8MzwZqaKj9TsD7GB90EJvwboHk7fdcA0Dmc-zknyOtAMIv2m7XZl132Y_zJyxDMHPrKsTZ3lcDHSGRAbjj2ythzBQXJLwWgSMFH7_-tgnFJs7glfis0o6IlJ1_IaXIi7uM7rlwBBIk4BL1YhKgTB31SNln6XjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSQwfHbr3T4CNujPbXbpOMI54JTBYxoP4SZqCNOIoqlTYJZDZYqvc5z6anhkgnVHBtoZls1jKzfnuqRAFOiTHTLI0y4NKr4lBIoWOGu7EnteQymAv1LtckEJN7dE_GFAC2SrvH-Y4VTjd3wV32QG3G9XUOGeamRmT1Uo-94C5qA7VjiSIIgexGhl7kD_daMhY1jd9EaSVnZlpOMaQaufbBtlgLDUxlVc74qvLyPWkZmGWUbRxBpItGyanGO7nuFqhxRN_2ne7EADMs7goxxP-dCbxOKNnfys8kVSgWIjqa5Y4NmH1d0VTIVqSpAaAJ93d5vWW3Si4IdZemq3yRiQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipQx-WJ7rPe982XSkL8tya9_-K3Fgiiwt_idezcuO7D4gZ0x1eOqRHq4lcgsgFEqQysHLALJVTuSgjg__0_yQbi_WItdZ4S9mBLyPswSqkbkeRNTj1CYWMqwb5rAsN6SwMyrYUyPAGAo5U6pfV9-movuBu-mbN2s2YYGVuJx_gmK4v6a0c2WTkVk0uRHJldek_lL4Wl0Vn31EcDnpklMrg9CyzFz3fmjAtW4p_ZL1rvvskNX3IdTwta8-2GKKnHeOprvdaprTObdTlb4nGLOaKu8s_O4v2T4VHnHoTZGb88JxTtPItH6pFmVUwb5iPPYTwxFE1rd8FsFguM3T1RQww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی را در چندین شهر جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122508" target="_blank">📅 12:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122507">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=qmU4ql_0q7IHy4stfuZPrl-QfqrrGPyqU6kxXVun6m3BziNwMlbrLFZIuERlFmHX1hXGgjzjUKASQgh-p1WRJD93y1WtwOd1M1h6tJTD8gxcmYL_QKDrnBnrJQyqJmrhcdDWf5dafR5KWzJYJCbRZz5szOzKqbaQ5X8_TAynhL-PP2-YBv0307BhS7-aY_kN9Ycd03bXZYzN9jTxWo_9TmIsZqcUsjE3NFWJAkxIBIJ82vUBpgQX4uHaMly08khRp64MEJAZoR4sU_ohCNhO1AuQLHUWJ_UvGfD1kbYTF6D8QEpecx2q-dqsbevD7C63cBMR57w98KnvwRLBLIotCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=qmU4ql_0q7IHy4stfuZPrl-QfqrrGPyqU6kxXVun6m3BziNwMlbrLFZIuERlFmHX1hXGgjzjUKASQgh-p1WRJD93y1WtwOd1M1h6tJTD8gxcmYL_QKDrnBnrJQyqJmrhcdDWf5dafR5KWzJYJCbRZz5szOzKqbaQ5X8_TAynhL-PP2-YBv0307BhS7-aY_kN9Ycd03bXZYzN9jTxWo_9TmIsZqcUsjE3NFWJAkxIBIJ82vUBpgQX4uHaMly08khRp64MEJAZoR4sU_ohCNhO1AuQLHUWJ_UvGfD1kbYTF6D8QEpecx2q-dqsbevD7C63cBMR57w98KnvwRLBLIotCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
🔴
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم
🔴
ولی ترجیح ما توافق خوبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122507" target="_blank">📅 12:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122506">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2989a06ab.mp4?token=bvDCeWclK0IeP-t0rGKECOu0zyWXp5YsWV7EQECmxx6BJYSSuISRPijYTh3pq8YY0xsiQfLIp8GF15iCj1Iwlk-e_R0yL2SpM7259kkqrUS5cYSofzL9zKHgB2k0kufKPgtTmFGcUGUTscVF9gmfdMNaW83WSdbFF5u3WsFLUDAfNmm8qVNV0sxDysf-6g3kY6gh0za73TLNlTr-NCeRsW6pCoBZgDDgWKQXFrbhvO6hEjlLA_DpnQTQJojwhpduAsdATzyr9j5wEJK32UMxMKWsRN1WsKPGYG0zFol0yJdkLGiVPVTaw-mIJ4kP9PibYGqBDBKoAfTci2z5Z9mIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2989a06ab.mp4?token=bvDCeWclK0IeP-t0rGKECOu0zyWXp5YsWV7EQECmxx6BJYSSuISRPijYTh3pq8YY0xsiQfLIp8GF15iCj1Iwlk-e_R0yL2SpM7259kkqrUS5cYSofzL9zKHgB2k0kufKPgtTmFGcUGUTscVF9gmfdMNaW83WSdbFF5u3WsFLUDAfNmm8qVNV0sxDysf-6g3kY6gh0za73TLNlTr-NCeRsW6pCoBZgDDgWKQXFrbhvO6hEjlLA_DpnQTQJojwhpduAsdATzyr9j5wEJK32UMxMKWsRN1WsKPGYG0zFol0yJdkLGiVPVTaw-mIJ4kP9PibYGqBDBKoAfTci2z5Z9mIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه آمریکا، مارکو روبیو : هنوز همه‌چیز در حال پیشرفته، همون‌طور که گفتم فکر می‌کردیم شاید دیشب خبرهایی داشته باشیم
🔴
الان چیزی روی میز هست که به‌نظرم پیشنهاد محکمیه
🔴
درباره باز شدن تنگه‌ها، باز نگه داشتن مسیر عبور کشتی‌ها و ورود به مذاکرات واقعی، جدی و زمان‌دار درباره مسائل هسته‌ای امیدواریم بشه به نتیجه رسوندش.
🔴
این طرح تو خلیج فارس حمایت زیادی داره، داخل آمریکا هم حمایت میشه و تقریباً هر کشوری که در جریانش قرار گرفته فهمیده که این فقط یه پیشنهاد منطقی نیست، بلکه برای دنیا هم کار درستی محسوب میشه.
🔴
همون‌طور که رئیس‌جمهور گفت، عجله‌ای نداره و قرار نیست توافق بدی امضا کنه. باید ببینیم چی پیش میاد
🔴
ما قبل از بررسی هر گزینه دیگه‌ای، به دیپلماسی هر فرصتی برای موفق شدن می‌دیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122506" target="_blank">📅 12:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122505">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
منابع خبری گزارش دادند که «بنیامین نتانیاهو»، نخست‌ وزیر اسراییل، فردا نشست کابینه امنیتی را برگزار می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122505" target="_blank">📅 12:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122504">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ایران در دفاع از خود هیچ گزینه‌ای را منتفی نمی‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122504" target="_blank">📅 12:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122503">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985125f801.mp4?token=SOZSSLWk4JynkWufm4ix_oYB19Jl7HHxJTNThC2cb5qQlVm5vGusGNlL45Au4GJvpxg22F71RJZu3ayTuX_gO2ZJQ8AYM7OXB7tJvRyDhqvDoayLw9gBeGC1tqu3Sb0qp4rkP1KADvYDhZ7HxIYBmmyZfl5To5SzqeUf2ows_eUcjHVmJ097SPs5YBKQCgnDC8pABYc113hjji4Io41POy2Gm7_pxPb9fjingQSN8Aj91WMJVrgZIc1gOMRWFa-FPyiNLZrrWwkiuLUV_l8z8lCsXcG9U3xkA_UMb7RsXK9yaH2yiTHaWdjuioigxVBwwZ_q81ZQt_mXwuMpWJYaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985125f801.mp4?token=SOZSSLWk4JynkWufm4ix_oYB19Jl7HHxJTNThC2cb5qQlVm5vGusGNlL45Au4GJvpxg22F71RJZu3ayTuX_gO2ZJQ8AYM7OXB7tJvRyDhqvDoayLw9gBeGC1tqu3Sb0qp4rkP1KADvYDhZ7HxIYBmmyZfl5To5SzqeUf2ows_eUcjHVmJ097SPs5YBKQCgnDC8pABYc113hjji4Io41POy2Gm7_pxPb9fjingQSN8Aj91WMJVrgZIc1gOMRWFa-FPyiNLZrrWwkiuLUV_l8z8lCsXcG9U3xkA_UMb7RsXK9yaH2yiTHaWdjuioigxVBwwZ_q81ZQt_mXwuMpWJYaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین
:
در جهان تنها یک چین وجود دارد.
🔴
تایوان بخش جدایی‌ناپذیر از قلمرو چین است
🔴
ما از طرف آلمان می‌خواهیم که اصل چین واحد را حفظ کند و ارسال سیگنال‌های نادرست به نیروهای جدایی‌طلب استقلال تایوان را متوقف نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122503" target="_blank">📅 12:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122502">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بقایی: برای تنگه هرمز عوارض نمی‌گیریم؛ هزینه‌های دریافتی صرفاً بابت خدمات ناوبری و حفاظت از محیط زیست است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/122502" target="_blank">📅 12:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122501">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، در شبکه تلویزیونی ایندیا تودی: اگر مذاکرات شکست بخورد تقصیر ایالات متحده یا متحدان ما در منطقه خلیج فارس نیست. ۱۰۰ درصد تقصیر ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122501" target="_blank">📅 12:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122500">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه: اسلام‌آباد اصرار دارد که پکن نقش ضامن را در هر توافقی بین آمریکا و ایران ایفا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/122500" target="_blank">📅 12:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122499">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بقایی: چین و روسیه نقش سازنده و مثبتی در تحولات منطقه ای ایفا کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122499" target="_blank">📅 12:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122498">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم: سامانه‌های جدید پدافندی به کار می‌گیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122498" target="_blank">📅 12:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122497">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بعد از ۲۳ سال، یک خانم (سمیه رفیعی نماینده تهران) عضو هیئت‌رئیسۀ مجلس شد
از مجلس هفتم تاکنون خانمی در جایگاه هیئت‌رئیسه حضور نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122497" target="_blank">📅 12:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122496">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCMuf_xtYpdbz9dWtvCbzYtjIK_87zid1XeYCCKF6x_YS_rFlzF_wczcYanBkvizWhtU1qtFKcT2W-3hIy9zntyBXmHMLd9NLIwNjFOsUH5Fkd3y8VWrwAzPeXxw17kRmPvO6IUr7vupehNm0BTrqH45t2p6wF7JQ4uQnUdYBceJfcWTnMbfA6nNofj85gV8hLkTy-iXsxmP19wOzEV-YD8ySTsoYIjoNrRMwrkC0kZktJMBsAWK4wQ8mURZjFmQedVIrEYAEtagCIeBltDrbQcFx4hCJ8xicZGDRpYV5pZMhOVYNGRh9NSfO5eDSgV8xgnMxKOJVtI741DXQISexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس:  اکنون روز ۸۷ام متوالی قطعی اینترنت ایران است که بیش از ۲۰۶۴ ساعت ادامه داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/alonews/122496" target="_blank">📅 12:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
بقایی: حتما بخشی از پول‌های ما خرج موشک و پهپاد می‌شود.
🔴
اگر چنین نمی‌کردیم دشمنان ما می‌توانستند به مطامع‌شان برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122495" target="_blank">📅 11:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: اینکه ما به نتیجه‌ای در بخش بزرگی از موضوعات مورد بحث رسیده‌ایم، درست است.
🔴
با این حال، اینکه بگوییم این به معنای قریب‌الوقوع بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.
🔴
سیاست‌گذاری و تصمیم‌گیری در ایالات متحده دچار نوعی تردید نهادی شده است.
🔴
تغییرات مکرر در مواضع — در عرض چند ساعت با دیدگاه‌های مختلف، اغلب متناقض و متضاد مواجه می‌شوید.
🔴
این روند هر مذاکره‌ای را مختل می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122494" target="_blank">📅 11:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تمرکز مذاکرات بر خاتمه جنگ است و در این مرحله درباره جزئیات موضوع هسته‌ای صحبتی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/122493" target="_blank">📅 11:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122492">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بقایی: سفر آقای عراقچی به نیویورک به علت مشکل روادید منتفی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122492" target="_blank">📅 11:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122491">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: فعلا سفر هیئت ایرانی به پاکستان برنامه ریزی نشده است
🔴
موضوعات شکلی، فرع بر اصل موضوع و محتوا است. ما الان متمرکز بر روند مذاکرات هستیم. اینکه بعداً به چه شکلی تفاهم اعلام شود یا امضا شود، یک موضوعی است که خب فرصت هست برای تصمیم‌گیری درباره آن در آینده.
🔴
اینکه هیئت‌ها باز سفری داشته باشند به تهران یا متقابل، بله ممکن است؛ اگر لازم شود چنین کاری انجام خواهد شد. ولی در شرایط فعلی، ما برنامه‌ای برای سفر به پاکستان یا سفر هیئت پاکستانی به ایران فعلاً چیزی را برنامه‌ریزی نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122491" target="_blank">📅 11:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122490">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: امیر قطر سفری به تهران نداشت
🔴
معاون دبیر شورای امنیت ملی قطر به ایران سفر کرد آن هم در چارچوب مساعی جمیله و تلاش‌های قطر برای کمک به پیشبرد تفاهمی که به میانجیگری پاکستان در حال انجام است.
🔴
میانجی رسمی بین ایران و آمریکا، پاکستان است و برخی کشورها نقش مثبتی در این روند داشتند برای کمک به حل موضوعات.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122490" target="_blank">📅 11:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122489">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
قسمت دارک ماجرا این بود که «منادی» خودش عضو هیئت نظارت بر رفتار نمایندگانه که وظیفه‌شون رسیدگی به رانت و فساد نماینده‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122489" target="_blank">📅 11:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122488">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXniPoaUKRRyYQQejGaspeQArJURk01rr6i_rG78KUWVEHV8GYt_r7wA4-YuEvzNX-bqP8KrgcoCXhkQa7zAgeoxIX4Ted6Id2NpVtRtNZvTWGKKW5JCG0D0NykSj3QtzsOXGMe_eP_FX5k-ohc841JpqJiu3iHJ0wGou7Iozso8RZsUVHbNIsz0YitpshqFH6q3lZ3iibAXJjZRZZvvCzFoky8s_Axsu9lrs9XfwA6P-TvuT7svxi8Gv3Y1y-WKXysPt_Tff2jg1p3HSVRV8BL317Ai4oMvVcJ7uPoyOxqxc_ZAee33fKMcF8LLOyADshonMHuRjmU86l5KSmU11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کودتای رهبر بولشویک‌ها در مجلس جواب نداد
🔴
حمید رسایی سعی داشت انتخابات مجلس رو تحریم کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122488" target="_blank">📅 11:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122487">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
👈
تعداد آرای انتخابات هیئت‌رئیسه اعلام شد
🔴
محمدباقر قالیباف: ۲۳۵ رای
🔴
محمدتقی نقد علی: ۲۹
🔴
عثمان سالاری: ۷
🔴
رای سفید: ۵
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122487" target="_blank">📅 11:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiQc9kZomRgaigeknVx_wyUhSqOZ4T3Y-y9X0EzMRS1pBGebqK01v0cVeiTFuJufly_q4VWxB_mr_vAOXplspAYgETe6vQZcSDFoIjaQETX7I3PWKI0ahpLvi6-7vxb6LWgXeTU93KIsPFsBt7g_WzzlCLwJUiINYUyaGVnZfTjO0tNC0BmAZbb4bvci5G_QX1_1r_6ga4mx6GmFMhrE_bsujFJY3zLXD61iMlmm539hJ3iwMZb8bwGPf4cIWhans4AVWSn331GrgbhiyUDeDuBXGscqA1eeabMJhFD7coKVugTWL4FfJKUqMTqkG5gfy0Lry9-VoZn1MgX5R5IHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXKcEZlJlPpI25YlwB3-Kxvf-VQyJQ60CHSh_LXF8xtteW4kH_tC2iVAr1dDk9AiC5OsXo2WgkOSg6h3wLUwpEEtPL_78CAnK7BxdS4HFSmNcOk5OlY11d3Fyg0ILjQf-S9KO5RfB3J9_blcWuL9C-pM-0Oli8G6TuPpXNo7gXMEtQMMzFmEG6ppBN9gFKq1ELsyaNExrRsXJ9MPE_dBZ9rMLznctBDsGag1KrgwuATRSP8M1soge8O4Zpm3bK1drq8zDL2SKhv5b8G0SA_09FjpmsWHeT9tDxtz5-cWSulVLz9DneCWDXlQjIZta_lOmTun_1cn7wrSXns-j4YE3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خب منادی نماینده فاسد و پست تبریز که به نماینده‌ها وعده خونه داده بود تا بهش رای بدن، رای نیاورد و میتونه به عنوان یه نماینده ساده به فسادش ادامه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122485" target="_blank">📅 11:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
👈
تعداد آرای انتخابات هیئت‌رئیسه اعلام شد
🔴
محمدباقر قالیباف: ۲۳۵ رای
🔴
محمدتقی نقد علی: ۲۹
🔴
عثمان سالاری: ۷
🔴
رای سفید: ۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122484" target="_blank">📅 11:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122483">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مشاور وزیر قطع ارتباطات از احتمال دسترسی و اتصال به اینترنت بین‌المللی در هفته آینده خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122483" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122482">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: این تحولات که در چند روز اخیر خبری شد، نتیجه چند هفته گفتگو از طریق میانجی پاکستانی است.
🔴
برخی کشورهای دیگر نیز در این مدت نقش داشتند. بنابراین اینکه در زمینه بسیاری از موضوعات مورد گفتگو ما به جمع‌بندی رسیده‌ایم، امر درستی است، اما اینکه بگوییم این به معنای امضای یک توافق قریب‌الوقوع است، کسی نمی‌تواند چنین ادعایی بکند.
🔴
تغییرات مکرر مواضع مقامات آمریکایی را شاهد هستیم. این روند هر گفتگویی را دچار اشکال می‌کند. با این حال، ما همانطور که در میدان نبرد با اقتدار عمل کردیم، در عرصه دیپلماسی نیز با چشمان باز و با در نظر داشتن تجارب پیشین برای صیانت از منافع ملی ایران کوشش خواهیم کرد.
🔴
کارهای مهمتری از پاسخ دادن به توییت های طرف مقابل داریم.
🔴
قرار نیست سبک و روش دشمن را کپی برداری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122482" target="_blank">📅 10:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122481">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تمرکز مذاکرات بر خاتمه جنگ است و در این مرحله درباره جزئیات موضوع هسته‌ای صحبتی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/122481" target="_blank">📅 10:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122480">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الجزیره: میانجی کلیدی آمریکا و ایران، به همراه نخست وزیر پاکستان از چین دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/122480" target="_blank">📅 10:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122479">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/637c252247.mp4?token=pmUnXoC_ghEB7IuS_3OsfOMnj2vyipMk8dNU2bTfEmWuKr8lhFFfxK7sQyxkPEcpT0riMTpRj565DsK_QiBwOdFf0rHfuxVO3-YSzmoCyCr8FYmYjTQAtp-BMROwgmjoqwtl5kjz381X8_VXKnyi8U4sWJj5ho9CCQeILZO5AoEpAKfQvEFZka5LwkuHyg0pSEWYTqXSn8blam_Ax4EsTwGXzhNHPEi5QxUyEJVlvxW_W8aQ0VK2nyNm6NrcV17fG-XfRLkpQkLO1mNgNsuRCpr1mbrTDpe0d5QUYbcZE3hRqR4diVEVLpuXEYUikn7hx5IoUqd_wdeuWQWxu_D2ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/637c252247.mp4?token=pmUnXoC_ghEB7IuS_3OsfOMnj2vyipMk8dNU2bTfEmWuKr8lhFFfxK7sQyxkPEcpT0riMTpRj565DsK_QiBwOdFf0rHfuxVO3-YSzmoCyCr8FYmYjTQAtp-BMROwgmjoqwtl5kjz381X8_VXKnyi8U4sWJj5ho9CCQeILZO5AoEpAKfQvEFZka5LwkuHyg0pSEWYTqXSn8blam_Ax4EsTwGXzhNHPEi5QxUyEJVlvxW_W8aQ0VK2nyNm6NrcV17fG-XfRLkpQkLO1mNgNsuRCpr1mbrTDpe0d5QUYbcZE3hRqR4diVEVLpuXEYUikn7hx5IoUqd_wdeuWQWxu_D2ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از تیرباران مواضع حشدالشعبی در موصل عراق توسط A-10
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122479" target="_blank">📅 10:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122478">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpcJ8S5-VxhrI4UG_pmFRIniDJaPc1b_S6Ybcr2xpiLjuKp4eMd3MOOFrAd68wRFSVQ91YFIxil6WGR8DZpxKwBKu9xpUk9OIiwKtxNB0iWVdRc_o2ptMFMBybdKnQ851LQ7k70ASFjtgV4LcDo75uemTyXnszjLb73ckSGgcThrAwcmVClbEJ_FSJ_w7x4up61ch_Y9Gz1K3N5cIxQWKVgGu-f7abT3IYcNADV8Mqe5meL7k6983dVFieZxbqJiqhlPI9xl_7xifl9f2lEM9Ih82sBdjVjOxEJIk2-u-RWfBvRvxbyKgea2w2KugccHOuRnM7d_F4FrQlqD5g145w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل از کشته شدن یک سرباز در لبنان خبر داد: گروهبان نهورای لایزر، ۱۹ ساله.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122478" target="_blank">📅 10:32 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
