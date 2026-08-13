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
<img src="https://cdn4.telesco.pe/file/JnD4FpKP6RkHAVy2jSvlN67E1sV3MadOIrwXHe85QaKX7q7bSXUjy15wVVIiSGBUb7LuI4sy60XT9pOzx80W4bBLmexS36nshkVsyHHIQsjrevv2vXlZHnURuvInzAiup4AW1Y-K-rJk9Xwf4ckNr2yI7PlQWoCe3vyXM4y2yeyCfIKEd3e2PDTAsBlH5hXQDZY4fpSY6aXK_cW_cltUtm0vreX0nqd6sR2X0ByoHkkrzVhAl2dFHTI_89WOgN5tUfNendZNp29xg4bEZrlPwrUonJy7M5nAmruvmJLAtjPrtfSQFPl-cjwwmDmvArXW3jHy3B5iAyEYs00mt-fcTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 15:09:36</div>
<hr>

<div class="tg-post" id="msg-141491">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
پاکستان: مهلت ۶۰ روزه مذاکرات ایران و آمریکا قابل تمدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/141491" target="_blank">📅 15:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اوکراین: ما مجتمع گازپروم در باشقیرستان روسیه، بزرگترین مجتمع پتروشیمی را هدف قرار دادیم
🔴
ستاد کل ارتش اوکراین: مجتمع صنعتی گازپروم توسط پهپادها در فاصله ۱۳۰۰ کیلومتری داخل خاک روسیه هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/alonews/141490" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
🔴
کنعانی مدیرکل حفاظت محیط زیست مازندران: تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/141489" target="_blank">📅 14:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
🔴
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/141488" target="_blank">📅 14:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ناو آبی‌خاکی از رده خارج‌شده USS Peleliu (LHA-5) با وزنی نزدیک به ۴۰ هزار تن در جریان رزمایش RIMPAC 2026 و در آب‌های هاوایی، در یک تمرین نظامی به‌عنوان هدف مورد اصابت تسلیحات مختلف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/141487" target="_blank">📅 14:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت دفاع ترکیه اعلام کرد که بر اساس توافق مکه، رزمایش‌های نظامی مشترکی را با عربستان و پاکستان برگزار خواهد کرد.
🔴
این وزارتخانه همچنین تاکید کرد که توافق با عربستان و پاکستان بر تولید مشترک صنایع دفاعی متمرکز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/141486" target="_blank">📅 14:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
🔴
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/141485" target="_blank">📅 14:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ادعای یاهونیوز: امارات میلیاردها دلار از دارایی‌های بلوکه‌شده ایران را آزاد کرد
🔴
پایگاه یاهونیوز با استناد به برخی منابع رسانه‌ای مدعی شده که امارات متحده عربی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران، از جمله محموله‌های طلا را آزاد کرده است.
🔴
یاهونیوز نوشته روز پنجشنبه بعد از انتشار گزارش‌هایی درباره اینکه امارات متحده عربی دارایی‌های بلوکه‌شده ایران در بانک‌های اماراتی را آزاد کرده است، قیمت نفت کاهش یافت.
🔴
بر اساس گزارش رسانه «هرمز لتر» (The Hormuz Letter) و سایر منابع در شبکه اجتماعی ایکس از جمله دارایی‌های آزادشده ۱.۵ تن طلا بوده است.
🔴
برخی منابع، این اقدام را سومین جابه‌جایی از این دست توصیف کرده‌اند. ادعاهای قبلی در گزارش ماه ژوئن خبرگزاری رویترز حاکی از آن بود که امارات با آزادسازی ۱۰ تا ۲۰ میلیارد دلار موافقت کرده و بیش از ۳ میلیارد دلار آن در میان جنگ آمریکا و ایران تحویل داده شده است.
🔴
با این حال، وزارت امور خارجه امارات در آن زمان این گزارش‌ها را تکذیب و اعلام کرد: «هیچ‌گونه دارایی بلوکه‌شده ایرانی از طریق امارات آزاد، منتقل یا تسهیل نشده است.»
🔴
مقامات آمریکایی نیز ادعاهای مربوط به توافق‌های جانبی یا آزادسازی وجوه ایران را رد کردند.
🔴
گزارش‌های اخیر نیز تا تاریخ ۱۳ اوت هنوز توسط ایران، امارات یا آمریکا تایید نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/141484" target="_blank">📅 14:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYWxWfDOSyj3c7wqkMQKN2bBoij0JU8yzYe3E48lih4csNJPInz25HDYvfCNeIfIn8N5sQ4lsHP9gWFJKTxq5mtajEwNpjZd_as-oWoc2A47zj2Hbdxusk1ADpBQRlqzHSoBa0z_4XBETeXfWq5206wPQ-_WrbCJVUH6tnXbPIb78KJbZm_Wtq4-1-ZY2uNHPI2zGHCN2xbPLf5qNCjKz7mE57ThqRlWYIrU909a_9bYgOLwqz5KyEihx4FMfWz4OYCcOqZlqt9voAtbo-Hghr77kebzBPUab6WqqWoTF5viwnIJJgrYYTClhDibDnwFHEG8wrmzz8XBa1evcpgV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=KXKKPIiv88iCgf7Zmcyp6N1OyAyrmxkgYjxe444b4q1VuGmwEVK7ye00rn_2uwzScNCbJoxI1kdVRN74OZCrZsYwuZGM8XZHBhsaYLP6yX8uispcT9vkZm_mfYcpJyZ6lmPEJiEo3EFS_qOQrtpFx8xINvs1VkL04lvJ7EsOj-3h5D8qPBCB0SfZCW1xjISxW8qpLiGXumiiVhAdckAh4Z0FkT-N-JqTCZeo0NpxezSq28lCK3J9P4HnNWAS7BqvjAs6WYxQwmdpU49gqwtp6NGeLD4DH_lWiB6Qf1bht8ti42GK-jQH6IVhOqcHDmvnNqnZ0oJAGzstUjPKx4YzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=KXKKPIiv88iCgf7Zmcyp6N1OyAyrmxkgYjxe444b4q1VuGmwEVK7ye00rn_2uwzScNCbJoxI1kdVRN74OZCrZsYwuZGM8XZHBhsaYLP6yX8uispcT9vkZm_mfYcpJyZ6lmPEJiEo3EFS_qOQrtpFx8xINvs1VkL04lvJ7EsOj-3h5D8qPBCB0SfZCW1xjISxW8qpLiGXumiiVhAdckAh4Z0FkT-N-JqTCZeo0NpxezSq28lCK3J9P4HnNWAS7BqvjAs6WYxQwmdpU49gqwtp6NGeLD4DH_lWiB6Qf1bht8ti42GK-jQH6IVhOqcHDmvnNqnZ0oJAGzstUjPKx4YzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل درحال حمله به زون، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/141482" target="_blank">📅 14:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141481">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
عضو کمیسیون انرژی مجلس: هزینه تولید و واردات بنزین به ۵۰ هزار تومان رسیده و من صحبت هایی از هزینه بنزین ۷۰ هزار تومانی هم شنیده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/141481" target="_blank">📅 14:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
🔴
کنعانی مدیرکل حفاظت محیط زیست مازندران: تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/141480" target="_blank">📅 14:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
خبرگزاری اینترفکس اعلام کرد یک مقام نظامی روس در انفجاری در کریمه کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141479" target="_blank">📅 14:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
قیمت آتی نفت برنت با ۴۲ سنت یا ۰.۴۷ درصد کاهش، به ۸۸ دلار و ۵۶ سنت در هر بشکه رسید و بخشی از رشد حاصل شده در ۶ روز معامله گذشته را از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/141478" target="_blank">📅 14:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
الجزیره: بحران تنگه هرمز، بازارهای آلومینیوم را با تنش بیشتری مواجه کرده، قیمت‌ها به بالاترین سطح در ۷ هفته اخیر رسیده و ذخایر جهانی به سطوح تاریخی کاهش یافته
🔴
این وضعیت ناشی از نگرانی‌ها از اختلال در تأمین‌ آلومینیوم و پیامدهای آن بر صنایع خودرو، هوانوردی و ساخت‌ و ساز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141477" target="_blank">📅 14:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba390ce5a.mp4?token=kG1XQrCIeIuy_uJvfF0ATitkp-i0iiMfqQ60_m2yNGCXnhe2QMZ0Oq0_6LQA1B8d6H7cU0kZDE2I1TBvBPLd2_XVWQz3xW357cxwFWMymHHM6T3zREzpvJLupFdY5cua5R_RAqp9NjLLeVhzOa0WsRUDcPNRzPRRUOk4gZZbGwNG3uWFIG07ngFQzIq9UxHCHhbe3eE8XmUrtVayVXXxbNF9hxlwT7fkbLwt2fAroZrNbIT7Sm-LoDC1NxoIedGJ3uWc-LvdRp2Sy-bEBRsbj-JZ60k7vJmqIetUkio2zWsHYs94HS2skQsiSyICiGCF4J854plSEt-jxHyXu8HW95_1K_DWtDsQmabPCpbpZuqFlzW33fcff00vIJyyBBrUvKYlGfw5T1-tDPkt5ZUdcgGFNu7DSkGrV96_KjzBx7znBQ8QDN9BrY9fFWsr5yME26J8Ev27irvhiV-A7TpIydFzJNEovU1TqkS21CV-DpHG19Qp8RYI_Gfaeagk5_3lPFRw5qf9nIuVdKs93cFauHfUTKb4Eo0iDSrjnIfXiUiMU8tRw3Jp5qP-I2SW0Hxq3zq3y47gw47BtPUM4NXiCEcYvqliQ4dvRtHWchscHB84eoEQ6mdpY2auKOKYm0n3YTkqP835xX9ErbIKG8WcEjO8YZrl9QBFKl91UbV6kNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba390ce5a.mp4?token=kG1XQrCIeIuy_uJvfF0ATitkp-i0iiMfqQ60_m2yNGCXnhe2QMZ0Oq0_6LQA1B8d6H7cU0kZDE2I1TBvBPLd2_XVWQz3xW357cxwFWMymHHM6T3zREzpvJLupFdY5cua5R_RAqp9NjLLeVhzOa0WsRUDcPNRzPRRUOk4gZZbGwNG3uWFIG07ngFQzIq9UxHCHhbe3eE8XmUrtVayVXXxbNF9hxlwT7fkbLwt2fAroZrNbIT7Sm-LoDC1NxoIedGJ3uWc-LvdRp2Sy-bEBRsbj-JZ60k7vJmqIetUkio2zWsHYs94HS2skQsiSyICiGCF4J854plSEt-jxHyXu8HW95_1K_DWtDsQmabPCpbpZuqFlzW33fcff00vIJyyBBrUvKYlGfw5T1-tDPkt5ZUdcgGFNu7DSkGrV96_KjzBx7znBQ8QDN9BrY9fFWsr5yME26J8Ev27irvhiV-A7TpIydFzJNEovU1TqkS21CV-DpHG19Qp8RYI_Gfaeagk5_3lPFRw5qf9nIuVdKs93cFauHfUTKb4Eo0iDSrjnIfXiUiMU8tRw3Jp5qP-I2SW0Hxq3zq3y47gw47BtPUM4NXiCEcYvqliQ4dvRtHWchscHB84eoEQ6mdpY2auKOKYm0n3YTkqP835xX9ErbIKG8WcEjO8YZrl9QBFKl91UbV6kNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود نیلی: امسال رکورد تاریخی رکود تورمی را در ایران تجربه خواهیم کرد!
🔴
با خروج آمریکا از برجام ۱۰.۵ میلیون نفر به زیر خط فقر مردم اضافه شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/141476" target="_blank">📅 14:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/141475" target="_blank">📅 13:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f465758dd.mp4?token=c0u5f6Qgh1CnrXeVcoeTXeXq7BvIApflCiWFtIJFnq1E2dszj-WTgJ0pjPS5HoXqUcQ7coqiaSjqWFNeapibAt3lMu4Fammk8-3JvuynxaMLMPCva1hcQwprwxVtjj9QBtXrjOKkOJE-YVoWhIIbqzRWBOPqW-DHWnub_A3NNtO8j5XIZtfJ2AyJCaBsoaV0F5jtKL9cHPcz_-1c0bqw90udyZf5Lu4aLbpLzH3Hoia1ZIhNzVoMeJ_xjIwBtWBOpG8Q2SJPhPEc85ssbvp_TBueDrV1BoTXWx7YFaQpnPgi5kr2DRcRR7nOojeE4ugn_CMUm-oqQERiR9O0mDedoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f465758dd.mp4?token=c0u5f6Qgh1CnrXeVcoeTXeXq7BvIApflCiWFtIJFnq1E2dszj-WTgJ0pjPS5HoXqUcQ7coqiaSjqWFNeapibAt3lMu4Fammk8-3JvuynxaMLMPCva1hcQwprwxVtjj9QBtXrjOKkOJE-YVoWhIIbqzRWBOPqW-DHWnub_A3NNtO8j5XIZtfJ2AyJCaBsoaV0F5jtKL9cHPcz_-1c0bqw90udyZf5Lu4aLbpLzH3Hoia1ZIhNzVoMeJ_xjIwBtWBOpG8Q2SJPhPEc85ssbvp_TBueDrV1BoTXWx7YFaQpnPgi5kr2DRcRR7nOojeE4ugn_CMUm-oqQERiR9O0mDedoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه قایق ایرانی رفته تو تنگه هرمز برای ماهگیری که یهو هلیکوپتر آمریکایی میوفته دنبالشون، واکنششون خداست
بنده خداها اصلا جرئت نمیکنن نگاش کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141473" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141472">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2g9nxwRdUojksoytjCzbGSjfrfENtd-Sx5mb42zUs2Nt4Rdn-PI0sofj1wGcvegmVbxPvQg_uzw5CTj9HlcE-rXdLuMaA7PiTrj8mCBYEbsbrx2glXkdNSeqL9oGcLSrOxgz9HnVzLNR7TxbKuf2Ilvtp13EaQ3HDRz9ESOsadcIiDgtyzGHc-2iCPEr-RAfEtZnRJcaRAXUcPcjq_nnDXSr0_sDj9v3OFKD6PEEdxxUwda0mtuo5dUnQkOLM3lSnD5xUO_Hg1ELl4gRKwHy89owViTi_4141EDs3LO1beqtZVOLMf2707XsWEAw6Db34k0Swk6HHQQ6ipKrZyZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز یک هواپیمای باری ایرانی از فرودگاه تیانجین چین به تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141472" target="_blank">📅 13:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgCc-fA0ngyqTHB6wQU_dcSqx1LHIUcxt1NxlMhVM6OcpOzk7EGWWi8RmzC836ZbF8L8af7gpkscbCzDB4T3M6m_mP4Ktr-I7laUDVOdYR2a5enbFG_N9fggs7UYRCdVRUzuQLGacMEt5Fgd71DvuNBWgJ03MYjCjm19CAN2M_P-1ZO_NeDW3tqy6GMTp1anlNMH-YwCApjwzc5viRB5tmw3u15U4hCMWknUYGg1Wjr6JKhVo3aVU25Oh1iNjSZgImu36taZYxVeZRhTTXHuatUg3CZYW70ViC2iFnRhkYuC5y2W8DUGuNRA1NBYuAs4NLuZzC40M67T_M6EVTUiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مردم ایران با میانگین درآمد ماهیانه ۸۵ دلار در در بین کشورهایی که پایین ترین دستمزد ماهیانه رو میگیرن رتبه ی سوم رو بدست آوردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141471" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزارت دفاع ترکیه:
توافقنامه مکه با هدف ایجاد روابط پایدار بین ترکیه، عربستان سعودی و پاکستان امضا شد. ما به دنبال انجام رزمایش‌های نظامی مشترک با متحدان خود تحت این توافق‌نامه هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141470" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbmIOEPSKBtrDPYgyHsAzBMZM3Fe0pi2dIvfy0CHpSN4rcZDq6gOk0TZj1HrkZrRVjcG4GDRiS9wSoVWv_9436czPJYpd32rkATvYPQpejpGdlqQWWyx0DaOMyx7Bmt3w1yfHwtbg2VZ3wP5-A9wlJJholaAX1d8xdhnwjfl2LZHcnilVcXTquMEJZu3OvVZMlq0MufzLQirJ18x2Axz2FizUQxc0yJIuyHuGPBCAjJ6mawkvqD17T_AAHuV-vUxCb14nv5YBJlxbbXyJv6bvIaTODovFzey8KTVJ5bSJyPh1TZ8K0YUd1N4iCbdQgqG3SHPrSRiCxjRyO32omgjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=Aw-11VuX-YXOFVa_anbIOOPrqLvDftpeoNQQCDV7tVQ5cURnGJVLJkGXztF79rMEoeb8UiJSW_NqBWHn9Oj5Vf9QpygG07KVazDem9dvD9wtHD2vlWFHocns9DIQIKNjHGtg1Vm2Tpjmwi9NQZqJ02ALpJa8dO2rRsF2tSY1EFlTn-Bw5W-EOiCSlgwCy3nHHTka04E4VKU6DjeHbkJrPwDBBDGQ9ZN9MUc5XrHMdLKh5gMw3GxqlN0EF0LPQq5xdfcOT-HhB80Sue3E4WgnkaDrvh2Z0LaugrPlvMuc7XNbdb5qqNm-ez_lxqTvDkuuvbc-9jO1su3jogt19k-Z9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=Aw-11VuX-YXOFVa_anbIOOPrqLvDftpeoNQQCDV7tVQ5cURnGJVLJkGXztF79rMEoeb8UiJSW_NqBWHn9Oj5Vf9QpygG07KVazDem9dvD9wtHD2vlWFHocns9DIQIKNjHGtg1Vm2Tpjmwi9NQZqJ02ALpJa8dO2rRsF2tSY1EFlTn-Bw5W-EOiCSlgwCy3nHHTka04E4VKU6DjeHbkJrPwDBBDGQ9ZN9MUc5XrHMdLKh5gMw3GxqlN0EF0LPQq5xdfcOT-HhB80Sue3E4WgnkaDrvh2Z0LaugrPlvMuc7XNbdb5qqNm-ez_lxqTvDkuuvbc-9jO1su3jogt19k-Z9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل درحال حمله به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141468" target="_blank">📅 13:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141467">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
👈
انجمن تهویه مطبوع: مردم بخاطر گرانی و نداشتن پول کولر رفتن سمت خرید پنکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/141467" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141466">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نشریه فارن افرز نوشت: «آمریکا ذخایر تسلیحاتی خود را در منطقه از دست می‌دهد. ورود به جنگ برای واشنگتن آسان است، اما هزینه‌های پنهان اقتصادی و کاهش توان مهار چین و روسیه، روند افول آمریکا را تسریع کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141466" target="_blank">📅 12:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141465">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgHaR5tXw-p8hq0k2T100VNNn6PzxrWhPO0BQjKHjuxJa8NtEOlhaPxZGD8f3T9KxyR53w75JcmaIvipCRaST1hAtHKeFa9ewOiKOOV9F7YW2Tb-RZnpkIQLk1k75o5UAIh9gnCL2VEDvafI9DKT_eJEmg0zy5O3LwQQrokIuR-8dRqAJxVTvuMiI5_6xgGEwThQZ9WSsarG9ksc-yrW5yjukDhe7DyXWcB8UqdgqU9JULY0Iohp3idtQ-KHL9g0p1VADTH5gm5s93BpcJ3_0NBLbv7xWVqhvHSR3-dKRdPYAlohhwAVFwYREkneqRg60epQwueHAYeD2KSE7MQ-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عضو کمیسیون انرژی مجلس:  طرح گران سازی بنزین از اول شهریور طرح مشترک سازمان برنامه و وزارت نفت است ربطی به سازمان بهینه‌سازی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141465" target="_blank">📅 12:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141463">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=q-wy0AYRuwLDegre8oAd9ZDv-5QkRKIjQiO1Wn71gE_qyf0YuS2HdKkWBsgQ7q_vP7iWE5pYYqfRkXdlQ4j6ne4TQvO5usFQs1vKgKYizlwKQc7w_aoGar7QkkGODCzHI-y95V0xrOJ9c0Gzuze_HCgO6z5i3dx3f7Tl3jopNnGf9JI4YD2EjCj6NXhcmndL7t2YXepIEmZ_fUSwo1n4mqNAN_3YTxVoDYn6UKx3zptM38tvW9NtSlbrIu89EgVYqvSLy1DoPEB33cmonJv0dFRm91fADsj3fc37Ot2T6HIHUn_tA1XKADsqEKF80h7Rk0n7-8Qe10e2w58OphkLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=q-wy0AYRuwLDegre8oAd9ZDv-5QkRKIjQiO1Wn71gE_qyf0YuS2HdKkWBsgQ7q_vP7iWE5pYYqfRkXdlQ4j6ne4TQvO5usFQs1vKgKYizlwKQc7w_aoGar7QkkGODCzHI-y95V0xrOJ9c0Gzuze_HCgO6z5i3dx3f7Tl3jopNnGf9JI4YD2EjCj6NXhcmndL7t2YXepIEmZ_fUSwo1n4mqNAN_3YTxVoDYn6UKx3zptM38tvW9NtSlbrIu89EgVYqvSLy1DoPEB33cmonJv0dFRm91fADsj3fc37Ot2T6HIHUn_tA1XKADsqEKF80h7Rk0n7-8Qe10e2w58OphkLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری متفاوت از خورشیدگرفتگی از داخل یک جنگنده و یک ایرباس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/141463" target="_blank">📅 12:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141462">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزارت خارجه: لفاظی‌های نتانیاهو درباره تعلق همیشگی بلندی‌های جولان سوریه به اسرائیل و نفی فلسطین را به شدت محکوم می‌کنیم
🔴
او در جایگاهی نیست که راجع به تشکیل دولت مستقل فلسطینی اظهار نظر کند
🔴
موضوع فلسطین همچنان مهمترین مساله انسانی و اخلاقی دنیای معاصر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/141462" target="_blank">📅 12:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141461">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57340e99a3.mp4?token=btWrf1sBp-Lxz6BqGfP0E3Db6bQbrkoBhK3eo76eOvEsRUay7kTaJ6ONFII7NaUvXw96OoYhZCQP9J_pNpfkH8kAjnTkkyyOVTjJStFvRtwpUhX18R4dTSIj7kwVRt3MGQ6Au_7od37vJiXPq2dU83L3jysoJ1Tt9EKjbAYpheaGfsTvg9t119F41V3LM03Fr5knieqpt1ZN5k_jzT6SwH3kXCiIHZm625bRbzI6NbBu9tT7kXRwnwH6As_Qp5puqplIVfQDdHO4uX1TNPHQPlsX8-u4vSOAqRC3qhBCGwbZ-BlZpDOI7I--v1I6mZKuFg0ZnDZCKunXbyl6zeUn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57340e99a3.mp4?token=btWrf1sBp-Lxz6BqGfP0E3Db6bQbrkoBhK3eo76eOvEsRUay7kTaJ6ONFII7NaUvXw96OoYhZCQP9J_pNpfkH8kAjnTkkyyOVTjJStFvRtwpUhX18R4dTSIj7kwVRt3MGQ6Au_7od37vJiXPq2dU83L3jysoJ1Tt9EKjbAYpheaGfsTvg9t119F41V3LM03Fr5knieqpt1ZN5k_jzT6SwH3kXCiIHZm625bRbzI6NbBu9tT7kXRwnwH6As_Qp5puqplIVfQDdHO4uX1TNPHQPlsX8-u4vSOAqRC3qhBCGwbZ-BlZpDOI7I--v1I6mZKuFg0ZnDZCKunXbyl6zeUn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک عضو کمیسیون امنیت ملی در پارلمان ایران تأکید کرد:تنگه هرمز تنها در صورتی باز خواهد شد که ایالات متحده به شرایط تعیین‌شده پایبند باشد. مذاکرات بین ایران و عمان به هیچ وجه به معنای باز شدن تنگه هرمز نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141461" target="_blank">📅 12:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141460">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYinOH5mcLAv1IA6sORccD8ZnwtCVPcvpRraQ4w3mS9mYaWlPWlAAhFrPGxWGBukyRsm7f9zpkxLR6CpuUtws5VD27APfikKr_ibssyuk5uajx_YRE7yNq-rCWL6DtrbZLu1g5pZe2TMgkOvjTKEQCf2FudAcXyQwTVoydbLgDwQqA4R18aJqn6tMSnJZ-wxGfgme4l7-qCPa2Xr3HZX1rFSAY_RmqlDAxgrQf4YQPSqDHC8ftnqHxMygvKGmHkSnxyVyEcW9nXxbETZn75T7lHRdfqXuI5fbf6lDMlEhgOAxTrrygFHSoXf1ffmv2RajQ76duu0GTnEWLUhZp6pZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای باری متعلق به ایران، در حال خروج از فرودگاه تیان‌جین در چین به سمت پایتخت ایران، تهران، مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141460" target="_blank">📅 12:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141459">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa62e58cf.mp4?token=ZJ-asZu1ZjmkJQxmCWNvLpyZA1VOWpGPbam-AyE2NhjxZn2PuzuDLV_pofgfpKuJ6dkO5s_TMCal_0dHPHEIiVLScMMIE1pRCV2wm5bgsFUdZlVPe9GYJEAxU7I12QEg86XC0dm5s_57kj9yxNO3UsNGbm4qBFB_0m2zEvNTyIV6J1pdljuiJ6L3VOEiapYg6BiP_jz3NttohB-un3OPgv1B7zcJo2DQt7ijWbk8Zp7OPE7tiZwHHAsBBW9kW8mi0kVfxC0ScMa5L3ct3HdpZVtuduSiLlOwwPlqK3zsE2FYd72-xINUlKNPIqTX_kQRug8sFsAhsW06ldRfaZNprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa62e58cf.mp4?token=ZJ-asZu1ZjmkJQxmCWNvLpyZA1VOWpGPbam-AyE2NhjxZn2PuzuDLV_pofgfpKuJ6dkO5s_TMCal_0dHPHEIiVLScMMIE1pRCV2wm5bgsFUdZlVPe9GYJEAxU7I12QEg86XC0dm5s_57kj9yxNO3UsNGbm4qBFB_0m2zEvNTyIV6J1pdljuiJ6L3VOEiapYg6BiP_jz3NttohB-un3OPgv1B7zcJo2DQt7ijWbk8Zp7OPE7tiZwHHAsBBW9kW8mi0kVfxC0ScMa5L3ct3HdpZVtuduSiLlOwwPlqK3zsE2FYd72-xINUlKNPIqTX_kQRug8sFsAhsW06ldRfaZNprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
ویدئویی پربازدید از پرش اسکیت‌باز اسپانیایی از میانه تصویر خورشگید گرفتگی
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141459" target="_blank">📅 12:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141458">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
بر اساس اعلام معاون وزیر نیرو پیش‌بینی می‌شود محدودیت‌های تأمین برق ظرف سه تا چهار هفته آینده و حتی زودتر برطرف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/141458" target="_blank">📅 12:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141457">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfCNkGn_cItT3FxuJWphhde6ZSxPO0dWQnJsmzOMRABcNAIzeZK6E6V4Rh7MYDBR8wY2UMCuk_YvLi43KgDhCIGn2xShI9Q_eCVRfX-7s5Oh5v2lLMMtSucQo7K3oPQz5a0eMSVlKQOyIRoAeoj_HhN2BtHELS2Z6ouidyZrNtSK1yZ8Rg4GrYajMBkbkqSumoRLBWwF0RxSmyGr9H7MhoEYMab-RIzO-pqWRW2wnQKIoT46x35mwS8s3PhbLYfoo_tBh-XOLJaxQo1Wuii-y7YXUKRyPK3l7dVPN8swEi136kz99Uc-Jzvr8DC-XQeSq8VU5cseyGb-Ix50n_6DAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
مردم من کنارتونم نمیزارم بنزین گرون بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141457" target="_blank">📅 12:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141456">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
مقامات آمریکایی اعلام کردند ارتش این کشور در مسیر خروج کامل نیروهایش از عراق تا ۳۰ سپتامبر قرار دارد؛ اقدامی که به حضور نظامی آمریکا در این کشور از زمان حمله سال ۲۰۰۳ پایان می‌دهد.
🔴
مقام‌های عراقی می‌گویند روند خروج نیروها و تجهیزات از اربیل نیز حدود سه هفته پیش آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/141456" target="_blank">📅 12:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141455">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
الجزیره: تمدید دوره ۶۰ روزه آتش‌بس میان ایران و آمریکا دیگر کارایی ندارد
🔴
تمدید دوره ۶۰ روزه آتش‌بس میان ایران و آمریکا دیگر کارایی ندارد، زیرا ما با چندین موضوع فراتر از پرونده هسته‌ای روبه‌رو هستیم.
🔴
مذاکرات ممکن است طولانی شود، به ویژه اینکه در ماه‌های گذشته سخت‌گیری از سوی ترامپ و ایرانیان افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/141455" target="_blank">📅 12:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141454">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=aNOpyjBz4W-HY2IM-Xd6WlMb3xisz7PZQJRkeX-Tv4bIdBzXnQrlMGxJEwzuho1bGGYbOdWp3dtkAwFvWNPFXND137dxqZDw8JUqT49iQ_FCw74uDz9xng8U_eTv1b19NfJeya8bHh-xYOUtEjmig2Mleoao4oc1W3rBbf1Q0FTBr9LDwthtMk3iRR9kyVlOcXFdeTb_sbFRlN54IeCwKJBOQg_MZjNthFLKbOasz_aVYN0KnbBv_Odhcj2cgQCbwsiOVT-o1nNy5hVthVLQxdEZW5vMpmAUwy6h1qDqFr1yVTr70kK0sSUXa5r-KlrwLfyUwvDMOEoGAmO9OTlMhov4Pmf2XX1Od1hZkTI2BTOgPFZXUdHOour14nsTBg7104Gn4eiAR9PNZZqHoOn26SyM7WgNKWbumbz97PRiC9y7QKtEBga-nje3iKqFdDun1aNWinOpRuPQuTEFiOf9i9Qx3Eb4RdGorw1Gf7TdbV5Ye-RqmhS_O8zAZEVCO9DA3vB0yAPhEcSrmU9w0cyE74lzjVSDaX6pMx6bT8l-mAGU72kkN0xK45HSZxOl-3fMS0VTUqz_QTybIgPt5hEM4BcPf3izZ5_xaeedmm5zxaSROI_TR4llLlp1VP9CwbfJ-XwAdTmvjTvgCoKbUgWNReFCPAZu8eku9gdCalrHFzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8cb1de271.mp4?token=aNOpyjBz4W-HY2IM-Xd6WlMb3xisz7PZQJRkeX-Tv4bIdBzXnQrlMGxJEwzuho1bGGYbOdWp3dtkAwFvWNPFXND137dxqZDw8JUqT49iQ_FCw74uDz9xng8U_eTv1b19NfJeya8bHh-xYOUtEjmig2Mleoao4oc1W3rBbf1Q0FTBr9LDwthtMk3iRR9kyVlOcXFdeTb_sbFRlN54IeCwKJBOQg_MZjNthFLKbOasz_aVYN0KnbBv_Odhcj2cgQCbwsiOVT-o1nNy5hVthVLQxdEZW5vMpmAUwy6h1qDqFr1yVTr70kK0sSUXa5r-KlrwLfyUwvDMOEoGAmO9OTlMhov4Pmf2XX1Od1hZkTI2BTOgPFZXUdHOour14nsTBg7104Gn4eiAR9PNZZqHoOn26SyM7WgNKWbumbz97PRiC9y7QKtEBga-nje3iKqFdDun1aNWinOpRuPQuTEFiOf9i9Qx3Eb4RdGorw1Gf7TdbV5Ye-RqmhS_O8zAZEVCO9DA3vB0yAPhEcSrmU9w0cyE74lzjVSDaX6pMx6bT8l-mAGU72kkN0xK45HSZxOl-3fMS0VTUqz_QTybIgPt5hEM4BcPf3izZ5_xaeedmm5zxaSROI_TR4llLlp1VP9CwbfJ-XwAdTmvjTvgCoKbUgWNReFCPAZu8eku9gdCalrHFzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر جدید از آلودگی نفتی سواحل قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/141454" target="_blank">📅 12:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141453">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی مشهد:  حریق در اتاق برق یک مجتمع تجاری-اقامتی در خیابان شیرازی مشهد با سرعت و هماهنگی مناسب تیم‌های اطفا و نجات مهار شد و حدود ۲۰۰ نفر از ساکنان و مراجعان این مجتمع به‌سلامت به بیرون منتقل شدند.
🔴
این حادثه هیچ گونه مصدومیت در پی نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141453" target="_blank">📅 11:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141452">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtIzsr1IIDfgRdb6SYbyXzyeDWtFVhouv4nYl3nEsiloh0M66Io5s1hBi818pw2Zc5k_i4pXtztlUQR90tnAP7Izknrbuuc5V3dcSRZyXRFahgfBuPY_3iFDM_ElxH3xafWzbi9D_2T5RO7U9dLLbueYxvz4wdXYp99_GEpPQynh89w83m3spohgvL752SIyQXeEZiFsTmuUifVnXieCjJAYJ9IH8qi9LkKO0CG0tBfFDTMpXL3Nte88q212FfjTqI7IKEoNM8XrV0-PoLbuko-vwnLiDU3X0FBByOnrGu8UQZUg6jP-5mOLGkrxonGHdHV5y2WyS2juA7ykeYJnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: آمریکا در قبال تنگه هرمز، مرتکب اشتباه محاسباتی بزرگی شده است
‏
🔴
آمریکا مدت‌هاست که به دلیل ضعف اطلاعاتی، دچار اشتباهات محاسباتی مکرر می‌شود. جنگ علیه ایران نمونه‌ای روشن از آن است. اکنون نیز در قبال تنگهٔ هرمز، مرتکب اشتباه محاسباتی حتی بزرگ‌تری شده است.
‏
🔴
بدتر از اخبار جعلی، اطلاعات جعلی است. مراقب باشید.
‏
🔴
الله بزرگ است، بزرگ‌تر از هر قدرتی بر روی زمین. ما بر الله توکل داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/141452" target="_blank">📅 11:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141451">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msl9Sw0pn0OlFd00K2cfE3r6VADkZXl1reCR2tFLU1Yhb0cDuWYxa16U3zCE4bYhhs9Rrml65QyT7eqACWTozJdHpP8MHzIzstohrpMi8HxCt6iPirmkRwNb89epe03UZ9K23K6n504B2D6gX5ce4NUtJBHOubovGer5fkPdOMuoaz7QFGbXuXjelWZ6OOgQ-Hdjv1UpsBy2zdb8AkwS4OYCzergXtmL6W3zE64m_jhwAU95crOr0HLQddkiostZe1qOsQtPF42aqPIrzjNx-9f8xwq_w4IUF9ucyqmyXDvqPLPaa0IUFgNg695vjrvKBpUbxIXSWpLEHVyK8LTnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یورونیوز: نفت متعلق به کشتی تحریم‌شده «کارولین بژنگی» که به روسیه وابسته است، به سواحل عمان رسیده است. این کشتی که نزدیک به یک میلیون بشکه نفت حمل می‌کرد، در ماه ژوئن در نزدیکی جزیره قبیلیه منفجر شد و روی صخره نشست. مقامات گزارش داده‌اند که آلودگی در راس مدراکه رخ داده و جزیره مسیره را تهدید می‌کند؛ نشت نفت بیش از ۶۰۰ کیلومتر مربع را در بر گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141451" target="_blank">📅 11:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141450">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d7922013.mp4?token=ejV33beWrLqCRP8HMGyxuYP_HemxcJgRtSOUG33TDfPW_hQuGZHUZ5Cd_cuN2g3gNr_g6gaZmHLmKfHbbUdIMjxdPMkYcT84XRDeGgDOFbKx7oJ6LJ44ZdbcC2b5lFOCOSX23MNyYN8ygZXH0Cbn-bV5Q8ZTF1_xVq5LxS2x62gUmNdYaxWQz3o6jPMcpWyKMNgx8T7PKobWB9SWQ4IUFv_7ZXCEip5eZ0sJgIPyTAUYynGXprUzfV8Djp7T2XyRsDWue3r9oDJf3JvWcYZyckqJXoRHS4d12rgM5-EBx5S9yDEVUiDJ_H_kH026SzCjJTQBjFR7Rr1ZmP7d5yXScw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d7922013.mp4?token=ejV33beWrLqCRP8HMGyxuYP_HemxcJgRtSOUG33TDfPW_hQuGZHUZ5Cd_cuN2g3gNr_g6gaZmHLmKfHbbUdIMjxdPMkYcT84XRDeGgDOFbKx7oJ6LJ44ZdbcC2b5lFOCOSX23MNyYN8ygZXH0Cbn-bV5Q8ZTF1_xVq5LxS2x62gUmNdYaxWQz3o6jPMcpWyKMNgx8T7PKobWB9SWQ4IUFv_7ZXCEip5eZ0sJgIPyTAUYynGXprUzfV8Djp7T2XyRsDWue3r9oDJf3JvWcYZyckqJXoRHS4d12rgM5-EBx5S9yDEVUiDJ_H_kH026SzCjJTQBjFR7Rr1ZmP7d5yXScw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کافه مذهبی با آپشن‌های فوق العاده توی تهران راه اندازی شده:
اینجا آمریکانو نداریم، فلسطینو داریم
نوشیدنی‌های خارجی مثل کوکاکولا حرامه.
موقع اذان، توی محوطه کافه میتونین نماز جماعت بخونین.
پرسنل قبل از پخت و سرو غذا و نوشیدنی، حتما باید وضو داشته باشن.
کافه، نزدیک مزار شهداست و میتونین دیتِ خودتون رو اونجا ادامه بدین.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/141450" target="_blank">📅 11:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141449">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141449" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141448">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای زمین حین خورشید گرفتگی اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141448" target="_blank">📅 11:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141447">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ny0p6QLTEmZDIbxJMEIpuNnaGxtk2bOPXoZuhlq20qMiPLZKRi6BOVOJEpKa-6xFDoNW4RQZkmhWie-H_O6CVvbGAGrqJAbc9l1Z8SZeWOvMX43BUrJ9zqlIUrg9ShN9ptPeQphNmBCuRmScdfMnEIe63kNUJyyrREGQCwDlrKC1xygbixFRJZDXhyHFrXuAaGwCcgdbcSWKD-PDoFNBayZCcNq3l_PLW0heHi0QwdCD1eSRvpkT-VLntAhsChAKRJ_EjQh61IdRHB3ynXPJa1gM3qLJ1IA0de8eug71QAVioi6klF5A2Fa9jjT0nW23ENSZwsTOwZohUEO9rKFKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کلمبیا رسماً به ائتلاف مقابله با کارتل‌های مواد مخدر قاره آمریکا پیوست.
🔴
این تصمیم پس از دیدار پیت هگست، وزیر جنگ آمریکا، با وزیر دفاع کلمبیا در پاناماسیتی گرفته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141447" target="_blank">📅 11:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141446">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2711d095b9.mp4?token=nJHxoo6GJWoIxkcMvyIYxvtAdel-EVbfKJYWFFdeDG3tyKPTMs4PLOwc3BBMeC6Gzo8irvFhrY5um6rXleXb-YtYUPmIFfxiuwEscHsSsGAYnTFNpQjFxbPjzlRSwyDgoVLTqJjEsBBAzXckfFvNMvRY0b5QlYwviMF58kYFSlNsunrlll5k4zSuC07yyT7P03uwMgYim-AF4_jVFreadfBbY22zRjWrXVWU64raIVQCeJ3Fwlap348cZt3W9ClHFDgPh2KH-7yeWY-p5-USfEvbru-Tz9U3uccD6WwlAbzwhZ_hQIEu0P310PSo7yex5gdGugGVmzKdVmH44g8sSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2711d095b9.mp4?token=nJHxoo6GJWoIxkcMvyIYxvtAdel-EVbfKJYWFFdeDG3tyKPTMs4PLOwc3BBMeC6Gzo8irvFhrY5um6rXleXb-YtYUPmIFfxiuwEscHsSsGAYnTFNpQjFxbPjzlRSwyDgoVLTqJjEsBBAzXckfFvNMvRY0b5QlYwviMF58kYFSlNsunrlll5k4zSuC07yyT7P03uwMgYim-AF4_jVFreadfBbY22zRjWrXVWU64raIVQCeJ3Fwlap348cZt3W9ClHFDgPh2KH-7yeWY-p5-USfEvbru-Tz9U3uccD6WwlAbzwhZ_hQIEu0P310PSo7yex5gdGugGVmzKdVmH44g8sSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
👈
عضو هیئت رئیسه مجلس : ما حریف مافیا خودرو نیستیم استیضاح وزیر هم چاره‌ساز نیست
🔴
محمد رشیدی عضو هیات رئیسه مجلس در گفت‌وگو با رسانه تصویری «آن»: با وجود سال‌ها قانون‌گذاری برای ساماندهی بازار و آزادسازی واردات خودرو، موانع و تعرفه‌های سنگین همچنان مردم را مجبور به خرید خودروهای داخلی بی‌کیفیت و گران کرده است.
🔴
ما حدود هفت سال برای اصلاح این وضعیت تلاش کردیم، اما صراحتاً اعلام می‌کنیم که حریف مافیای خودرو نشدیم؛ حتی استیضاح وزیر صمت هم در گذشته نتیجه‌ای در این زمینه نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141446" target="_blank">📅 11:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141445">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DznwD4N0n56nZy4kqa3NzGuBxhJEvnhDpOw7LA5pgm3fisCojAu57MDPYAxL9_1gxXNjUVI-1EaGJZifIBOLlESCtKSVyrhxOzEoY8T9xBBVlaGV2qau1QbvbyWQaabgN_ZVzGqsL6evWqVsdyNoHZH1m-I7rUPqidzfyuoTLQaTDihKQemf04c8FDr5mE0paSVdOUukqeqjnwu8c-HcBtM8pdWoz-_nnpPWzWxhuw10V4z9IbjLg1CvDqGux9-8OBAtVoSSFhs53BA4yE1qwUbZXry-PP7lqEuovl7slsmMARRNYQVxRgwwRjNGfzticksI9ybvvsVKGNPtmYes_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتورهای دموکرات خواستار تحقیق درباره وضعیت ناو هواپیمابر آبراهام لینکلن شدند.
🔴
پس از گزارش‌هایی مبنی بر وخامت اوضاع تا حدی که چند ملوان اقدام به پریدن به دریا کرده‌اند، سناتور ریچارد بلومنتال نامه‌ای به پیت هگست نوشت و نگرانی خود را ابراز کرد. سناتور روبن گایگو نیز خواستار بازدید رسمی هیئت دوحزبی سنا از این ناو شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141445" target="_blank">📅 11:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141444">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
فرشاد مومنی، اقتصاددان: ابرتورم در ایران رخ داده و وارد مرحله فلاکت شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141444" target="_blank">📅 11:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141443">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff225435fc.mp4?token=VnSxKCAvmDKJzPiZjEDL5VPUbNb7IahKQuK2QwsC1WoDiSk4Ahl-F0-U3WpaaZnWwFD2ihoaLzycwGp1_ce5lfhk90cdUisYj3r8r_7wJI3aSOIf3FH2u1hQHs7UndpyKjI949CBuqe1tJsv5_PhrUoHVlf05Zurtc15X5MSYQFBCJ73DBis4KgLqCLALw1E8HbGeMrvjrQPFC0a1L41uk8VHSK75JdZyS5lToZjjor9TrLEG3XMLLx936MJzJs-ZIy99NQo7Bix8H-A3BgXg2ur4pzqdGBFg6FD5udFA_8iUcbRa4IaK-Fpv6f-QimKRHv67EFOGxaGd5nuaLecGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff225435fc.mp4?token=VnSxKCAvmDKJzPiZjEDL5VPUbNb7IahKQuK2QwsC1WoDiSk4Ahl-F0-U3WpaaZnWwFD2ihoaLzycwGp1_ce5lfhk90cdUisYj3r8r_7wJI3aSOIf3FH2u1hQHs7UndpyKjI949CBuqe1tJsv5_PhrUoHVlf05Zurtc15X5MSYQFBCJ73DBis4KgLqCLALw1E8HbGeMrvjrQPFC0a1L41uk8VHSK75JdZyS5lToZjjor9TrLEG3XMLLx936MJzJs-ZIy99NQo7Bix8H-A3BgXg2ur4pzqdGBFg6FD5udFA_8iUcbRa4IaK-Fpv6f-QimKRHv67EFOGxaGd5nuaLecGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
لحظه‌ی خورشید گرفتگی کامل در تاراگونا، اسپانیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141443" target="_blank">📅 11:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MwIwUOu_ZWuiFyOKW_fnmOArvwHzuvA0T7yu8_FaskH1gaiv7IOfFogLH9aI26NoZf62mYOiajyXePDhDnS9v4qUbT50oMdVhcq7QY2Qz8mPnLOOPcOX-FKoZ5PY9ilo11_xioEdYZEit8PN2PHT83Fl4G0_hZ1xVLKcGcToI8LtABazDxIqvMXuX_QrS7AktfQXs8nw3NLL9JDuxgYsE_I1j7WKeuUPIBh-D7k4qtydhsuew360PVBFnQDPHH3uRCsYgTVgRGQ0lLIHgiqqiSAIkvy1krP5KoIa6J2PGgb8_WJGn0-1SngmWIT93LWFQMidOoPesKa2sQd2w4XkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0vaaRA7aHQ04SPHSmZA3sBsCAoAbmSptmQW_k-atvmzlkPuWrLIOmutTzJeAMWGN1a4ZEj0JNWluwR_6I73T6mDM5NLtQTU0-UvMVwSRx9yTgh2R8DHuzqlMkUdTDH6o7iKTEJ10CSiqlxHBuyAVlL_AqoML7qmAK8n4uV1oRdnA77x5XHZSumx8ah6zLwulQPU9_9VkkOYrjktvGCCABS9wHPuj9DyBbeFYILetG_j121uP2wu9VASIgCbriiXvU46yE0CrfeZPwDuPaaLbRNS49Md0oLKAXR0fOkl1abBeU32qBl3skMlOqUq_qzLAIYYEu4Ma_umACY3QZReDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAMmxw4kVivwQ1Y0Omb1oZIOk3H6-fSLtgeDX7vMLDpN6x6owPo076xhg6AQ3X9qdCHNEhZ4JWQ9lQuwQX6Rvx0Sy2-1kUinMn8tx-8jCT8EQZzY52xYAlYEsuIlwHz_dzPQDBl3fZM8oULKB93CiizUd0Ph1xgkWduGePX1czoerCTUxqwAM77CcxngNa-OwJsOFhMCaiNEhya8toR8QOsQTB1TcE9H7kJ3LnndZZZxx04OXdKY7STW_l-AJSppDFZTL47ciDP1p8E9zGYBBoOmw92Y57c9_Gtr2UMyxenKybc2oxbzZhUadNEI2lk5ar4PR-R4EEnT9kugag6EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbiLZAzqbAcflJLyIdYMuVv9F8rTRLI6Q0o2HYwvDWGG7cmMfOjb2VUrg10OEPi__HawrsCDP5kLgqNlelaRpvj1HDMtq1hd025FDW_T0iv8uiPO7OjYmxWiXNptPFtl51ttJb_AJk9WuHzip4ZalZ93E4730KrUkThyBb76CUE6Uj3sxIk2RsJZ9pqcsa-S6rOr_pZ3KWG5edGLDYE3GwNIiSx3dzXDPjMo-40RSJ2MkZspGU5Vx8qPH3pCMoxsJJgFuINux5jTMvQ4iitwLM5OT3iQKotqjBwvrjKWen6nvl9-zHI2u8UzMttfvoTUZmsh-qgfc46nU7TGH4g7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KScl5IgNBX0nTpP22FjbT1INOQKPonqEia49aiI_8E2tvrlrPXlNCcdbE_Uw2Oz0By34xJ6V7JlT3925Z8hFrFshHKIhLOAUU3pqIe40U5yaeL-f1lPk5-VH2gydl393cfV7XRlVbET5V28ypbweF-jfBVGiR5BX3ZXQLNGN5TOvbHRN3GPZygIzTmFNgC2TOsTx2AytyhptLFJoXbgl8_wCMN25uTreJWd_lbohJNivpPts9qfSw_m7-xTqULKFejPSgJgJ7cMiUo0HeYADbo_pxJBMYtZT4rrGGsnU3ZqSaYS3o_lvl_42US_kddSuEOROSLObjqRYPvOze5IrRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از خسارت به تأسیسات ذخیره و بارگیری غلات در نووروسیسک پس از حملات شب گذشته اوکراین حکایت دارد.
🔴
همچنین، یک نفتکش در تأسیسات انتقال و بارگیری نفت نیز هدف حمله قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/141438" target="_blank">📅 10:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏
👈
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141437" target="_blank">📅 10:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141436">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7nMd1gvXARKkrcbXxZYrOmGlt34KzIuqyrdVjB9_YW2gRC3_d8r_IjFix1gxaYZp5HDrjuTD9JxaGUL7EbW2DblID70ztXPJ3tZJjBRl_mdGB_HihTYYJmB74eyM9v323R_lQl46c1p4-Y-MfMo25-QYtq_C0aeSFwSwy-33rvRI1iiHHGYdBtczxfaQ47Ekh6UrX5YyUmuJRlopQwRj4yhrLnFMGcaX-7bqSmILoNzcccPiUdCdxqIB1mjsI4oqI24WAfYDxvSA0vDlBlwyXUhhvVNODkm3Lk2pxxtOPKyGSAP8-xSYfKR60vns4eAuvQlSiRCtN7_5aa1tKkmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست: همه گزینه‌ها درباره کوبا، از جمله اقدام نظامی، روی میز است
🔴
پیت هگست، وزیر دفاع آمریکا، با اشاره به قدرت نظامی این کشور گفت: «هیچ‌کس دوستی بهتر از آمریکا و دشمنی بدتر از آمریکا نخواهد داشت. بهتر است با ما درگیر نشوید، اما وقتی مشکلی پیش می‌آید، ما نخستین کسانی هستیم که وارد عمل می‌شویم.»
🔴
هگست همچنین درباره تحولات ونزوئلا مدعی شد: «قرار بود سامانه‌های پدافند هوایی روسیه از کاراکاس دفاع کنند، اما کار نکردند. محافظان کوبایی نیز قرار بود از مادورو دفاع کنند، اما نتوانستند.»
🔴
او افزود: «اکنون شاهد اخراج کوبایی‌ها و روس‌ها از ونزوئلا هستیم.»
🔴
وزیر دفاع آمریکا در ادامه درباره کوبا هشدار داد: «همه گزینه‌ها، از جمله اقدام نظامی، درباره کوبا روی میز است. آن‌ها قطعاً حریف ما نیستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141436" target="_blank">📅 10:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141435">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت دفاع روسیه: سامانه‌های پدافند هوایی ما شب گذشته 362 پهپاد اوکراینی را در مناطق مختلف کشور سرنگون کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/141435" target="_blank">📅 10:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141434">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
‏فرماندار جاسک : احتمال شنیدن صدای انفجار کنترل شده مهمات  در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141434" target="_blank">📅 10:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141433">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
به گزارش برخی منابع عبری: امارات ۱.۵ تن طلا که از اموال بلوکه شده ایران بوده رو اورده تحویل داده تهران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141433" target="_blank">📅 10:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141432">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شرکت امنیت دریایی امبری: عملیات نجات یک نفتکش آسیب دیده در سواحل عمان
🔴
شرکت امنیت دریایی امبری اعلام کرد: ما در عملیات نجات یک نفتکش آسیب دیده در سواحل عمان مشارکت داریم و کشتی‌های نجات در مسیر رسیدن به محل حادثه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141432" target="_blank">📅 10:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141431">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
نقص امنیتی در پل ارتباطی میان XRP Ledger و بلاکچین Coreum باعث شد مهاجم با ثبت تراکنش‌های بدون پشتوانه به‌عنوان سپرده معتبر، حدود ۲۰۰ هزار توکن XRP از ذخایر پروژه خارج کند.
🔴
تیم توسعه‌دهنده اعلام کرده کد آسیب‌پذیر شناسایی و اصلاح شده است. این سرقت طی ۹۷ دقیقه انجام شده و موضوع نیز به مرکز رسیدگی به جرایم اینترنتی FBI گزارش شده است.
🔴
یک خطای نرم‌افزاری کوچک، برای مهاجم به در خروجی یک خزانه دیجیتال تبدیل شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141431" target="_blank">📅 10:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141430">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_QbSBUbBElBsLqi0MNb8fKUfWo57iewUU4atloOqPHhL_eb5zMTdt3YojRU-zSbbY0MqboMaqzzvP_GvzEToBQkUkMtn_cjg2KJjLHns0LuecA7multfj9OTMeWQ8-a8YNF60a92J54l_ZNCNet1jtJ63YpnP_Ci4Uybs_HWiwGA5zfxn4rGzO8xXkFYo-55LVifLIMaZwkmIWofl6IQQeNjVU1a1BK8LoYIeMAgo93KYkKmW-shJHR0k6QCmNqu7YEHirp0Y--4AltoBOFV_Q-PjebX5W_Vz6c3_H4RPgaDzSeCLoyIPsz4ufkBsfAup_1VnvBXToUbvbnwO2QNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصویر روز ناسا؛ خورشیدگرفتگی کامل در اسپانیا
‏
🔴
۱۲ آگوست ۲۰۲۶
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141430" target="_blank">📅 10:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141429">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17fcfa2fa.mp4?token=Z7zqaMde4lIgjsU1bHXYkNUXm7XQlQ8gkIMnMtXs521tBFv_jK4TvEYR_4t9PNXykw5wxuWIrbwqbtZ3sR9J3v2aAr1qbH-1MHB-2RzlpCS5eBtGv3h9ev6b868civJY49svbnwooX-h3jPgQR8-pccb-8mr7Bvi6vt9TA3pIpXGqW_2R4wc9MFdTxHfhutr5naMrUNBvj3dEn7BsA8n3R1jWN-ePTBZaa6op1I5v3iuscHtStNS8YRpgyVPEIXZ9qqy_L7yMGRmUFEwurHAqb4w2FY526mgl408HZHIwm4Mkn7gKANNh2sou_9uQNPfXgKvKVsTqLPMycyH36O8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17fcfa2fa.mp4?token=Z7zqaMde4lIgjsU1bHXYkNUXm7XQlQ8gkIMnMtXs521tBFv_jK4TvEYR_4t9PNXykw5wxuWIrbwqbtZ3sR9J3v2aAr1qbH-1MHB-2RzlpCS5eBtGv3h9ev6b868civJY49svbnwooX-h3jPgQR8-pccb-8mr7Bvi6vt9TA3pIpXGqW_2R4wc9MFdTxHfhutr5naMrUNBvj3dEn7BsA8n3R1jWN-ePTBZaa6op1I5v3iuscHtStNS8YRpgyVPEIXZ9qqy_L7yMGRmUFEwurHAqb4w2FY526mgl408HZHIwm4Mkn7gKANNh2sou_9uQNPfXgKvKVsTqLPMycyH36O8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمان و عربستان سعودی اخیراً «کریدور سبز امن» را راه‌اندازی کردند که این دو کشور را از طریق الربع الخالی به هم متصل می‌کند.
🔴
این مسیر شامل حدود ۵۶۴ کیلومتر بزرگراه در سمت عربستان است که با هزینه‌ای حدود ۵۳۳ میلیون دلار ساخته شده و برای کاهش هزینه‌های حمل‌ونقل، تسریع ترانزیت کالا و ارائه یک جایگزین زمینی که گلوگاه‌های دریایی کلیدی را دور بزند، طراحی شده است.
🔴
پروژه بیش از ۳.۳ میلیون ساعت کاری برای تکمیل نیاز داشت و حدود ۷۵۰ دستگاه سنگین که به‌طور خاص برای شرایط سخت الربع الخالی انتخاب شده بودند، در آن مشارکت داشتند.
🔴
ساخت این پروژه نیازمند حذف حدود ۱۵۰ میلیون متر مکعب شن، پهن کردن ۱۲ میلیون متر مکعب مصالح محافظت‌کننده از شن و استفاده از حدود یک میلیون متر مکعب آسفالت بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141429" target="_blank">📅 09:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141428">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
واشنگتن پست: تحلیلگران سیا «اعتماد کمی» به اطلاعات اسرائیل در مورد توطئه ادعایی ایران برای ترور ترامپ در ترکیه داشتند، اطلاعاتی که سرویس مخفی را بر آن داشت تا یک عملیات امنیتی فوق‌العاده برای پنهان کردن خروج رئیس جمهور از کشور انجام دهد.
🔴
یک مقام آمریکایی گفت که گزارش‌های مربوط به تهدید جان ترامپ «از اسرائیل سرچشمه گرفته است، نه ایالات متحده، و اعتبار کمی دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141428" target="_blank">📅 09:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdb171b134.mp4?token=TeIutK9BmQ1WbtFBe4lNI8vjkIO83fIQk_tRe04Ymqe6cnHX_BOtvx7lFztadzwLeHVhKB_9ojgVdAgenlDvzuntBIjX4u3k9IaZDDcj7KtsV7QS-qJR3Sg2JWPTwLVp97G7XCXKtoLJ4DoFDLSls_w8XwEojzZU90wzELT6IX6DjlZ_tcV1bm7XokR8_6Hdu97vdIqf9vTDkJ8UDuvAUu5HTKb8Ic8K6ywCEMmdGgp09vFZw6FcKCoQorQ1vJKH5xP7s8e5RpUBXnEjyK2yItzb9xobhV1Vf6OuT9jVf4ICbQ_PynAOLVJ_WJfD4wjdSiIdt7LkL_Kr-g95RdAZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdb171b134.mp4?token=TeIutK9BmQ1WbtFBe4lNI8vjkIO83fIQk_tRe04Ymqe6cnHX_BOtvx7lFztadzwLeHVhKB_9ojgVdAgenlDvzuntBIjX4u3k9IaZDDcj7KtsV7QS-qJR3Sg2JWPTwLVp97G7XCXKtoLJ4DoFDLSls_w8XwEojzZU90wzELT6IX6DjlZ_tcV1bm7XokR8_6Hdu97vdIqf9vTDkJ8UDuvAUu5HTKb8Ic8K6ywCEMmdGgp09vFZw6FcKCoQorQ1vJKH5xP7s8e5RpUBXnEjyK2yItzb9xobhV1Vf6OuT9jVf4ICbQ_PynAOLVJ_WJfD4wjdSiIdt7LkL_Kr-g95RdAZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه ایران، اسماعیل بقایی، گفت که حفاظت‌های زیست‌محیطی باید بخش جدایی‌ناپذیر هر چارچوب آینده‌ای باشند که تنگه هرمز را اداره می‌کند، با استناد به آلودگی‌های نفتی اخیر در سواحل جزیره قشم.
🔴
بقایی گفت که شواهد اولیه نشان می‌دهد که یک کشتی باری خارجی منبع این نشت بوده است و آلودگی در سه مکان ساحلی و در بخش‌هایی از آب‌های اطراف شناسایی شده است.
🔴
او گفت که دهه‌ها آلودگی و فعالیت‌های نظامی باعث خسارات زیست‌محیطی به ارزش تریلیون‌ها دلار به مناطق ساحلی ایران شده است و استدلال کرد که تمام طرف‌هایی که از حمل‌ونقل دریایی از طریق تنگه هرمز سود می‌برند، مسئولیت قانونی و اخلاقی دارند تا به تعمیر و جبران خسارات وارد شده کمک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/141426" target="_blank">📅 09:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj4jYU_4JX7vdvR2c3axM06Rq1A3b2eZad209-UFXhqXgYyvuS3s6TADYETEDUS0PaH2n9Lgyk70S5Xl7LHqCpYIIRx1EW5egqiZmguJRM8zNNqpNflPdnuBHEGBwCYUM4qFRTs4fCjqoctv5LNg9gN4OHJBaMWVTiEBF6hdRr3BfcmdwiipO1r5Wu8Qq5clTGEXtteKUGOxxVW2T2rMtJcdwD7bho6Ce1Dka8FVmweoBv2G3jeT983IjUUwPiHHaOGpFL3thIJl-H8UUznkHcJil-b0xzuiK7IxiaBx7um-4ymY0LI2PTBdqOyl9ctrz0d2IPtLCzK1B-Lt06_SZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مرد ۹۹ ساله ایتالیایی نامه‌های عاشقانه قدیمی را در یک کشو پیدا کرد که نشان می‌داد همسرش در دهه ۱۹۴۰ رابطه‌ای خارج از ازدواج داشته است.
🔴
او درخواست طلاق داد و به این ترتیب پس از ۷۷ سال زندگی مشترک، به عنوان پیرترین زوج تاریخ به طور قانونی از هم جدا شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141425" target="_blank">📅 09:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA2f-24nT_ssg8G-XqOyOi29QjiERuUq5bQVZEZO2xJOFk19RALOZxnWn6fzctCNNv9UTa3jRbPvQwWmA3jZm36lXFhj-JUW7OsLnwdCrd-_TnbKowHRrfCSXalfl7BtCJZKjzsMOyaSVsYIyn1ZOH372HZrJEFLu6wvA8o93X9wrlVsXP7rIEuQIiF2YSBd02_RH6dEUMeoXd5MbiaKdKJSl1-ox_7N15i5W9PWIO_Q-smBJtICFH2f8EaFuViInaNuYBzUGxffxlw1lFSIJBPJj8UjLqHQjLGpwd1B8OYfvNhhtPXgwoWFLPCr0nUFGgst394SiP4GLvsOAI10uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت حمل و نقل مصر:کشتی "تهامه" (TIHAMA) که مورد هدف قرار گرفت، در سواحل یمن قرار داشت. این کشتی قبلاً هرگز وارد بنادر مصر نشده بود و در مسیر سفر به مصر قرار نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141424" target="_blank">📅 09:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141423">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsBuFSw4rY39-NYTbQe05aLMvC3zKsnyxpPsb4_nGmjERnRx8TEZemGf0hpWB4NkHX2jbxh0tUdeguOtWAI3-53Ayyv6l99neNrpAtPOYQrI5Xsf1vwSieTEmwzQk8J0ywsxYX7l2JNq2HoH_-hQguEHFdDWuqXVJoO3aZ4llPmSITxfrth3TVq5sSxdWZ4cPldPnrFukRQEOIOjdHCbypLbxvfN_L4kxC0kuNZTO9AgqukI5chXZYMdkmj2xY33uOhE-2gqWCQQqJhlPDSBYrbVUwCeoxjtTNzOWUUiROD9gPEs9SjQ7dQ5WtXKBg2e7KCPYdFTyfnaiOWn5pCkaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آلتمن مدیرعامل OpenAi:احتمالا تا 6 ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
🔴
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
🔴
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/141423" target="_blank">📅 09:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141422">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1mn-67bwFOyWRSX8mlvL5tEMNTlBiVc9RYGAstmgV3JDHShwSpjzkbcYZMhW2YEBM63xy2EWcEGKupcv_DGgjjn5Yt_jLRdiakhv8vBEKEDivxUHi8uWRizOLDM5L-i8yWQZiHNB1-4x-R6QfEFd_OVpZELrZnY6BSQcI5NzcDoT8nyxGYqsTLzktn35XJ5YKkXW8XJ5ejMU2DsXZyT1HlmU-H-TfGn0gE7pdiPpCWi1h1Cv46z3vfdD6Fr0yKfikvpcJ8iblk0OxyfWS2L8jBBIQbWvXO2Hz_lkaVaUTgahlOhcbS9LJlDu66ydBenl0NQNPOEz17wYZBuMtRVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلتفرم ایکس حساب یحیی سریع، سخنگوی حوثی‌ها، را مسدود کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/141422" target="_blank">📅 09:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141421">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
الجزیره: قیمت نفت ۱ دلار و ۲۹ سنت یا ۱.۵ درصد در هر بشکه کاهش یافت و به ۸۷.۶۹ دلار رسید
🔴
این کاهش پس از آن رخ داد که به دلیل جنگ علیه ایران، پیش‌بینی‌ها برای تقاضای جهانی نفت در سال ۲۰۲۶ کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/141421" target="_blank">📅 09:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/po3twxY7K4FB3yRCShkeYQ2kCzWdRwyMlgzGGB4jSE4apXLmUukP6cIwid3ClE47rN-1ROvAQkoGh2nQnzhT0P3JxuLCRg27WUrJ3YUOJzDKYeDP7QBiuwbD1MpvbmyPGxg2YPGVU6KeF7ZETKJ8qZHy5LRlYOC6WJzrpNr3avLDc8r58ZxxFBqv5Jvrgftvdg6q_YeKSmuB4f0eBy91yLnEdCqxWIOp5H6cQ9lSdrQFl7wKPFAziQJelv0iY9c-NvCQEXpDv5tV_dONabI8P_mfyzVgjkg929KRj-pxtGdKmGFV0Ih1lJMJnHq-nXkxB3SDHPSKnTR8CgCuU2PZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ReZckfzGEbtGtRQpSv7mbPKhvAwUYt6mIYtDedKY7RlCJ0EjCE28xz4g410Hx0Z2CqS-fpAg9MI2TclJyKoXHKfCnw3Bn2pfIRDqDdJK2SRd15vF2T3W1vYCDjN23OKSIp38lY3GyXhsOhh1E3iQQN1OSeL43vZRWWz4KtObK9Uauw9JIZTRQRDXS_p4EN5jscTylemio63ewnUHGMMXACkTIXy6ZR5RcUF6SmXA-EyTViCCU8kxiLIZ7GWAYfssgzvNgRX5ZKNud8GZMQIdg0KgchQ3zDEdchmQqVKRfDKVWZ6e3s5D_jEwJr7JlAuaCaYDeiWfnKADTcF9aynXbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=f4i6ErK-7RLQmKFAH5wQVqahkcvDXVfehkgyQVWsSWXoHXJ_DRcubmU2R75Lo-xTqCIhuna7LrVzTuF_iUI1GKDgi6C35Oj2d8akIvWZFs1lYYK5CflOqQ4OYVCiE3Sn_g50gmjQw1PflQBA1gBE6W-8s-THSxkde9C__4F1irYLGYmRDLzpsi2_C36Rx_n9r7faWYyd0gMkM7FWsqY1_AX129Ik8xa0EAoiUwbXxwNXi7GrPq9RUXdn6z-2ILgQcyRC-5uBkwse3hvnu0TrubUWUFTXkfM1kIOBmI0uErOtJy0hPV1DpfbcjEOCggDxwVhFIh_OX38RyCKAYdZnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8342b1a3.mp4?token=f4i6ErK-7RLQmKFAH5wQVqahkcvDXVfehkgyQVWsSWXoHXJ_DRcubmU2R75Lo-xTqCIhuna7LrVzTuF_iUI1GKDgi6C35Oj2d8akIvWZFs1lYYK5CflOqQ4OYVCiE3Sn_g50gmjQw1PflQBA1gBE6W-8s-THSxkde9C__4F1irYLGYmRDLzpsi2_C36Rx_n9r7faWYyd0gMkM7FWsqY1_AX129Ik8xa0EAoiUwbXxwNXi7GrPq9RUXdn6z-2ILgQcyRC-5uBkwse3hvnu0TrubUWUFTXkfM1kIOBmI0uErOtJy0hPV1DpfbcjEOCggDxwVhFIh_OX38RyCKAYdZnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی زیبای خورشید گرفتگی کاملی که امروز در اسپانیا و آلمان رخ داد :
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/141418" target="_blank">📅 02:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی مجلس:
دشمن قصد حمله زمینی از مسیرهای غرب کشور، خارک و قشم را داشت که با واکنش یگان‌های نظامی و نیروهای مردمی، این نقشه در نطفه خفه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/141417" target="_blank">📅 02:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141415">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UR01sAU1uoX3Jg1sL0Z5rn0RaOAjI_OMB6FrDDq5d0QeIKGZ4tt-mXwtQcbyQPG5wWHvDH_zymJN0-jPHG621ByT5k4wlb7ej2DvMVCQnx7GtBGy0k1OL9zf1dXa3gjfjguSfcg191lHbI3R3oiZWYYoFHUkjLWDdMtRI2r3izeYvRiq3cbikWepxwjgI04aQ_5bvXTOaMq4VXWrw8nQ0g7a4xbLl0hV7bsSBk4z2wnhL1SoOyUxU3pNkZP7nILFGjkj9xsnaioTCeZnt6bVRPOBNyCynDNPhZprA49J6OagBBFWmJ3aKK_5QlHR5HqXScOh0B87xLdJj0yHLOyW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfh5VeCVL32ozQYOvVSxTknEgcfgu4B-BtKn7V9Z1jCn43k9jw9ydhRIP_Ymc2AD_zrk-iyMS_x84t4qYmOB4nA28YFyrSNxYsNvEwwHoYBPOOMSS10QM781MGvLIndgYAm7Mnmctwts6tRorpLlmFEZaGmSLFyHF1IJEBIFYN9Bgau0fw9Xts2IKfXdNj8vuuILT7srL75DuZzCL7HzLkb6CRbWfbk0pEU34eCwyJmRP27sx8HPDXNhgGGf9OGX5mlpDgC6l64XJ56MfWW2ykRcXyr20Zv_sTUQgFbnrazOubkPr99Dk-xLQxhKHdriNJtTH1GpDlT-PfFn8i6Dhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ رفته تماشای بازی‌های پاتریوتس؛
بازیکنا هم دخترای نوجوان بودن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/141415" target="_blank">📅 02:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141414">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
دخترا حواستون باشه تنهایی شب بیرون نرید، تو این ویدیو ۴ تا حرومزاده تو اصفهان دور یه دختر رو گرفتن و دارن اذیتش میکنن.  @TitrDaily</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/141414" target="_blank">📅 01:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141413">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZmEeZbQQMqshFUNVUwDNfL6eYKRbrLDvCA2GPsnNHMLSMM61juzvks6yKjELTbhPUx2QNZOnw-U5hBg46uAz1a3vqxPliH9hTrV3nyZ3VBltOb5lqYl-ikKBPp0lUXaFUVbBASGBNBATpTjeGukvfCePxGDIEi4lX835x35tF3YZH827CgQVI2645GlGeR1hkX4KzM693Y3YsAby-gBVL7DaEt87qPWAtjaE-ZyaJ0AzycXtJBULlFtovzBV8bz024zPXbh2Adly9g5tQq7MNwwr2PdXmtwoWmz0MRtUbsWW59eQnGE9rOgK-JBdRwpxRn0hy75i8WDV4RuevJCn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری جدید از فرمانده نیروی دریایی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/141413" target="_blank">📅 01:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141412">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJLzXMiFZ34a8r6RmIB9_u8eFIAKLmQGqzC78QFN7F7xB8WFs2XpdcAiW478xZBI1CuRn46FmaEMS3iXdWTDxOq3AEuO7kMmwYsEdYxjkLClGdLI5fnBv5aWEM2j4dh2ad6ov2hjq25RXrJ8A3Q1gp-o0YVJa7ylkcEwjOpn-dxobxjD7ZkvG8KNS6HmRghd3mjAmAqxmhAJlaGfEX48xUfxDTw1f257q2QpOMAkGomFi2W58uA4RGOmlVD57eOxTTQhQ7RpF1yS9z1L_w11zs97zSUOQT7MN4CIF-ORSyFliicaie7rEIV4aHk9Jn9agmXAzQWRndNN9o0YouoePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری هندی شبکه خبر: باید تا هروقت که نیازه بجنگیم اگر چندسال هم بشه مشکلی نیست و مردم راضین
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/141412" target="_blank">📅 01:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141411">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2686734c.mp4?token=mlOoROdQkhsiKTPS1Lbm5Cw0UEesjUuw-KGvtdX--aZoOgRrpZItJ5KQZbMrGDOEaZLXKfURLpl9T5Lz3bb4evSoyXV1pddFrDNRuDL1n09ih3I9gm4-mNllSXT6JDnd5C5sV06heO4kTOuVE4or5ry5KSh-1UBRUr1K2nGbXWb5xbvUhdg3wj4qYLqk-Xe5EBQo1_hWHNhzL9duPs2Vxh1jiV6RQ4QJJwQdhNJga0_8aQ5l-mF9xQ_GJtVfQYHnfnWgtM-zqoEmYhLW0HVS8H7EyV3go56AtgYbIAXLbrpxU7OOg6aoljXr9amwfkGdTf51ap7pvHPYGTnj3SC5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2686734c.mp4?token=mlOoROdQkhsiKTPS1Lbm5Cw0UEesjUuw-KGvtdX--aZoOgRrpZItJ5KQZbMrGDOEaZLXKfURLpl9T5Lz3bb4evSoyXV1pddFrDNRuDL1n09ih3I9gm4-mNllSXT6JDnd5C5sV06heO4kTOuVE4or5ry5KSh-1UBRUr1K2nGbXWb5xbvUhdg3wj4qYLqk-Xe5EBQo1_hWHNhzL9duPs2Vxh1jiV6RQ4QJJwQdhNJga0_8aQ5l-mF9xQ_GJtVfQYHnfnWgtM-zqoEmYhLW0HVS8H7EyV3go56AtgYbIAXLbrpxU7OOg6aoljXr9amwfkGdTf51ap7pvHPYGTnj3SC5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یالانچی
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/141411" target="_blank">📅 01:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141410">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
علی قلهکی: طرح دولت برای افزایش نرخ بنزین تا چند روز گذشته متفاوت از طرح اعلامی امروز و مبلغ ۸۷.۲۰۰ تومانی در کرمان است که البته همین هم متوقف شد و دولت اصطلاحا عقب نشست/امیدوارم از «آبانِ ۹۸» درسِ عبرت گرفته باشیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/141410" target="_blank">📅 01:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141409">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/141409" target="_blank">📅 01:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141408">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed091c1703.mp4?token=QC18nd2IcAt4lovBrKDa1H7ESbsDVulU8bUbMNZdPti8hRTdGYg9Mqury0yr45tCK688L9Gu-lYQUEwff1957K6K9rqNnEyXZ0qRIw3qANuE28-WPSPsi-ZaD0SKgdE0wI1-r0uLFVPKqo-NwJM67zsg5cB8Ns3iQmew1yiIWc6Dz7uQGrq8_T0iwJANOAD2zaHKpN3SGH7ryg692VYJP-6h2Ld7sLXpr52T-aYJhnASx4qSIAkg6L05MvDm-n8cFLQhOeagCt93fADcIjBBer_D9EsUd3n43v5gOwPT9lcHUCriPqKq-fsR5R1NgfHyMsfNdbRg5FusdUjfD9XI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed091c1703.mp4?token=QC18nd2IcAt4lovBrKDa1H7ESbsDVulU8bUbMNZdPti8hRTdGYg9Mqury0yr45tCK688L9Gu-lYQUEwff1957K6K9rqNnEyXZ0qRIw3qANuE28-WPSPsi-ZaD0SKgdE0wI1-r0uLFVPKqo-NwJM67zsg5cB8Ns3iQmew1yiIWc6Dz7uQGrq8_T0iwJANOAD2zaHKpN3SGH7ryg692VYJP-6h2Ld7sLXpr52T-aYJhnASx4qSIAkg6L05MvDm-n8cFLQhOeagCt93fADcIjBBer_D9EsUd3n43v5gOwPT9lcHUCriPqKq-fsR5R1NgfHyMsfNdbRg5FusdUjfD9XI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دکتر موسی غنی نژاد:
«یک ایدئولوژی التقاطی مارکسیستی و اسلامی، در دهه ۴۰ شروع شد، در دهه ۵۰ تکمیل شد و در ۵۷ به پیروزی رسید؛ که "پیشرفت مادی" را مذموم و غربزدگی می‌دانست و ضد توسعه بودند. حال همان انقلابیون اکنون در راس حکومت هستند و مانع گفتار و گفتمان توسعه و مانع پیشرفت کشور هستند...»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/141408" target="_blank">📅 01:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141407">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/141407" target="_blank">📅 01:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141406">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
دادستان اردبیل:
بی حجابی مشکل اصلی کشور هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/141406" target="_blank">📅 01:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b5aac12.mp4?token=bedjN70u9K2Xj-zRydS8jd4_FiMT6VFI3BtjVceSexJQSQEN0FM_iqWHpdFTGv_5Wn17xuPOKdfpS42uWTQCRO3gdWoIvGoMs3GV0Z6GKT4UHs7DJB0spKWhaMdT-yXqI8rrA51NYuDv5HoKVLFOM9enpV8uaqcPKxx2eHmj2brSqpdt6OmyJvJryuLAsyceKukGjqrMDhUMcYJYzg-sM-oQA8Q87Q-UPGhLbLgtKulc7VrwaCF_zOKI75CluTnEL1eLND6KlnRx2hJRseUR9-BHmoOgOe-7vmgggtVqnfyCCbXkKqD6c1Rw7ee1A37a3jei59DBJd9Mqps_XUG09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b5aac12.mp4?token=bedjN70u9K2Xj-zRydS8jd4_FiMT6VFI3BtjVceSexJQSQEN0FM_iqWHpdFTGv_5Wn17xuPOKdfpS42uWTQCRO3gdWoIvGoMs3GV0Z6GKT4UHs7DJB0spKWhaMdT-yXqI8rrA51NYuDv5HoKVLFOM9enpV8uaqcPKxx2eHmj2brSqpdt6OmyJvJryuLAsyceKukGjqrMDhUMcYJYzg-sM-oQA8Q87Q-UPGhLbLgtKulc7VrwaCF_zOKI75CluTnEL1eLND6KlnRx2hJRseUR9-BHmoOgOe-7vmgggtVqnfyCCbXkKqD6c1Rw7ee1A37a3jei59DBJd9Mqps_XUG09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
یک نفر بخاطر لایک کردن پست پهلوی و کامنت گذاشتن بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/141405" target="_blank">📅 00:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141404">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
فارس: عرضه بنزین با نرخ آزاد پالایشگاهی توی کرمان فعلاً متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/141404" target="_blank">📅 00:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فارس: عرضه بنزین با نرخ آزاد پالایشگاهی توی کرمان فعلاً متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/141403" target="_blank">📅 00:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141402">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: آمریکا کنترل کامل هرمز رو در اختیار داره - فکر می‌کنم همین کنترل رو حفظ کنیم! محاصره دریایی ما رو همه «دیوار فولادی» صدا می‌زنن و ایران هیچ کاری از دستش برنمیاد  - ایران دیگه نیروی دریایی و نیروی هوایی نداره، نیروهاش حقوق نمی‌گیرن  - سپاه هم نابود…</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/141402" target="_blank">📅 00:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141401">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
حمزه صفوی: اشتباه کردیم که مسئله‌مان حفظ بشار اسد شد!
🔴
تهدیدهای بی‌اثر انجام دادیم و باعث شد باقی تهدیدهایمان پوچ به نظر برسد
🔴
در ماجرای تسخیر سفارت آمریکا؛ ایران قواعد بین‌المللی را شکسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/141401" target="_blank">📅 00:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141400">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
تعدادی از صرافی‌ها مدتی است که از تسویه برداشت‌های مشتریانشان امتناع می‌کنند، در حالی که دارایی‌هایشان بلوکه نیست.
🔴
زنگ خطر کلاهبرداری بزرگ از سوی مردمی که دارایی‌هایشان را در صرافی‌های ایرانی نگهداری می‌کنند، نزدیک است.
🤔
این موضوع را جدی بگیرید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/141400" target="_blank">📅 00:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141399">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b87629e01e.mp4?token=TYQbvf1EuuixVVbMwrhFgXI9eetWEZZjuwrVHjuNeQ2PNi0wgHUISCGoCLSEbcvvJaEv4z4nFBYivdnwrs71Blcdp2dJ7kA22FNA9GGn5EJbHtddbTAaA-sbV2-neRjiIgXufNzgTchCDugFQUhd6TbDw7DZB2tkKV3v76Rf_Xs-Mj5wdot515mWy5_sAIbfr_6nr1bGMlxRRmKE76lI5rlreB5nBCKLUCpnNnOvH2UPNi2tz-9jt51i16-1Op2NR_OMwnGvk5gJVdPTRdjeVT7fiREz51po69awL97Et75BqdJJ0tUCrT_KUyDwLktQJAktmrYjvpagqCS87ZdHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b87629e01e.mp4?token=TYQbvf1EuuixVVbMwrhFgXI9eetWEZZjuwrVHjuNeQ2PNi0wgHUISCGoCLSEbcvvJaEv4z4nFBYivdnwrs71Blcdp2dJ7kA22FNA9GGn5EJbHtddbTAaA-sbV2-neRjiIgXufNzgTchCDugFQUhd6TbDw7DZB2tkKV3v76Rf_Xs-Mj5wdot515mWy5_sAIbfr_6nr1bGMlxRRmKE76lI5rlreB5nBCKLUCpnNnOvH2UPNi2tz-9jt51i16-1Op2NR_OMwnGvk5gJVdPTRdjeVT7fiREz51po69awL97Et75BqdJJ0tUCrT_KUyDwLktQJAktmrYjvpagqCS87ZdHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کاری که حکومت با مردم میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/141399" target="_blank">📅 00:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
از عجایب دنیا اینه که تو کشوری که از وفور نفت، سواحلش نفتی شده، صف بنزین تشکیل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/141397" target="_blank">📅 00:12 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
معاون امور استانداری کرمان گفت از بامداد روز پنجشنب نرخ بنزین بدون یارانه ۸۷۲۰۰ تومان به ازای هر لیتر در کرمان خواهد بود
🔴
پ.ن: بزودی هم تو کل کشور لیتری ۸۷هزار
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/141396" target="_blank">📅 00:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POZ54Rg_qTzMryxvUHfWQiTP-GYn0LTlQOF6zkJNm89VJ-QJudZT_3eqQWGZWSmc5tpDMBihVuyu9TJw5H49l0AtxZ-h3nPV8GNFGoHQfxhWRpzhpT5v3tBIkxGPgsjE8BqdF0rz2DWcR3eQF4JLq5tNrfQPBRxiqHWs7xIEz5zYGXxZ_YR03Rs4Uh7Bm7rPiGXmoWhrf5CubMVn7rz-YpUMCuFGNQO28cTZSkGZLyR2BgjqhULbX8DiJ8vWiMHpVqQUQm2IfS_sKH29yy0BDoOplX66EJs7D7jnj3jQWCtcBRXQ8yyje-NosohpAsAcxOJ6HIZS27nTdM-MRUUA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: اسرائیل و لبنان توافق کردند
/
چهار کشور ناظر بر خلع سلاح حزب‌الله می‌شوند
🔴
رویترز گزارش داده اسرائیل و لبنان بر سر فهرستی از کشورها برای نظارت بر روند خلع سلاح حزب‌الله به توافق رسیده‌اند؛ انگلیس، ایتالیا، سوئیس و اندونزی در این فهرست قرار دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/141395" target="_blank">📅 00:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
جنبش النجبا، از گروه های شبه نظامیان حشدالشعبی، از تحویل سلاح های خود به دولت عراق خودداری کرد و از این دستور سرپیچی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/141394" target="_blank">📅 23:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141393">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ میگفت تورم ایران ۳۰۰درصده انگار راسته
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/141393" target="_blank">📅 23:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141392">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
تنگه هرمز تنگه مردم ایران رو گشاد کرد
🔴
تنها کسی که از ناامنی این تنگه آسیب دید مردم ایرانن
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/alonews/141392" target="_blank">📅 23:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141391">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8e_iuCDPsltuTKLP0NwCUKvuG5mRjxMlzP0ptT7u46s9Z_0gt8pEXVYataR4M8J3t8rwOWDBQMDawr1MEtVVDNQkmzOQX3_75n-1iiQLLIGqhlLRmYvfs8mzCGv18eE5rsxjx8ny_q7HMqaC5kc9eo9VjnfzxHZduAlrMGJvjTK8gMjfV171uyHtGms6ggSsNCRdDNnEIssclXyt-xbGYa7djCpB-jd-M58-ZCED19L-9WiISJjMxpeaj-Yd4JIwzBX1kE4NQbzGRQ0t9pdZiseHZiONvIue6P6q6gZcbqU7P0B-J0asWQkz3ZZY3F-2oxKyFzzZ_Q0vgs4Axt-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط گروه هکری عدل علی تصاویر برهنه و منشوری مسیح علینژاد رو منتشر کرد
😐
😐
😐
😐
😐
🚨
مشاهده فوری عکس‌ها</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/141391" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141390">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سلیمی، عضو مجلس: ارزش تنگه هرمز بیشتر از بمب هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/141390" target="_blank">📅 23:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbQ8HdbbHvCG5rDgPYjOx07T7z8dwSJWlhMxznW8M_Libi3Cz8icwwWxlFWgx2gp8mnTr1G92fLWV_KLkpMUeWCU2dRxsxdBa-gro_QOlCTKpQpnmdDW70KKNMLoPtNSCu6iTrMIRkEWZUAiiZa8AFxljhwYmsuomQrXnQ1WNuRc4Sk1YHSk5cqnJC8XhxGO8Nr3rOgyJc57TaaLXJw5eBU9JPWEam5cqZEpw1XRA4ILzDaK-JZPj3YCzwo7F3mFebCGmlCGRDE-Frl9FWgG62pzs_Fhh0PISYkvI6102lEr5fDPEsWCSKhPJE9PFP4KPzlvaw8Ss1OxPqHqLK6yKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد سامتینگ
(
قالیباف) فروردین ماه خطاب به مردم آمریکا :
دلتان برای قیمت فعلی بنزین تنگ می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/141389" target="_blank">📅 23:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97c70c4eb8.mp4?token=OutyBfpOaHNrYdutROGoYbDHXhGp0wZ1K2FRpz18xvL9bpkfGu9uLXgM1ob3BxVzVHs3hcm1YGQrrxBMrTF72nmqXooP3WYHgUscF-ytzDrfBiVCm31nA-GUhpV2evR_MITWGoS1r68oiON7vNF1bNYSmNQxDMzORUdeqaoZq-Eq79sh6DWIWXnhVuepquAFTnvEYYPWh3DEWN7mjvTop9O8fhDIGfA-hdg7TdlyI-xyAj0A-raY00XkzRR5K8hwMFj0IA9GduDo2MLxSbA7IGKbD999bIucoed7mEJ7xUGVb6eBhkyvIcdC4hVsp2USYeZ7L93zLGUFzTpggzRvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97c70c4eb8.mp4?token=OutyBfpOaHNrYdutROGoYbDHXhGp0wZ1K2FRpz18xvL9bpkfGu9uLXgM1ob3BxVzVHs3hcm1YGQrrxBMrTF72nmqXooP3WYHgUscF-ytzDrfBiVCm31nA-GUhpV2evR_MITWGoS1r68oiON7vNF1bNYSmNQxDMzORUdeqaoZq-Eq79sh6DWIWXnhVuepquAFTnvEYYPWh3DEWN7mjvTop9O8fhDIGfA-hdg7TdlyI-xyAj0A-raY00XkzRR5K8hwMFj0IA9GduDo2MLxSbA7IGKbD999bIucoed7mEJ7xUGVb6eBhkyvIcdC4hVsp2USYeZ7L93zLGUFzTpggzRvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف پارسال: بنزین ۶۰ هزار تومانی برای سال آینده صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/141388" target="_blank">📅 23:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhRxCxoJ4rmhnjLUxcKjm4C8-BBjwWUBHYqdLRYS3b9utiWqo5KNo1v6tIPBCLD6pL9rqvhh1aMq-5-W-LZ3Fq50XUuJTiSgAGhNZ9bJp3pcQatiUsOrb66UFHjvDOPOrH3Z_7J7KyA0W1wFErrbnnnQufZsDGiRr2AGSGt_ELYTi8QFGXSGLGM0tKK5_tJG8Lo5Z-q8ybqjg7IjuU_P6GTZq0mkHd8STbmOY9M8L-59LESvOhrR8mlbDR8ZRe1-7ErlMaBDIksKyGDrj5LfOdfUtciCO-OvEA_62j6sWGu89ahvf8W9gMiuRXrR2np_7wOt2BZy4VOurZ-fzwOCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ اعلام کرد که کارولین لیویت، سخنگوی کاخ سفید، در پایان ماه آگوست از سمت خود استعفا خواهد داد تا وقت بیشتری را با فرزندان و خانواده‌اش بگذراند.
🔴
ترامپ گفت که لیویت همچنان به عنوان یکی از مشاوران برجسته و یک چهره تأثیرگذار در حزب جمهوری‌خواه، در فعالیت‌های انتخاباتی این حزب برای انتخابات میان‌دوره‌ای مشارکت خواهد داشت.
🔴
او از لیویت به عنوان یکی از اعضای کلیدی تیم خود از سال ۲۰۱۸ تقدیر کرد و او را یکی از بهترین سخنگوهای تاریخ کاخ سفید توصیف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/141387" target="_blank">📅 23:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94e5e813.mp4?token=W4ca4ryH6s3SyHHPZy810Y_2hHKEnBu-d251ePueF5ifAcGC17Z_GWhM5ibtUwxz-WrRQjgvXK3R_QFqw0ej7gvZcQnLDG_FPvFylAmGvLYyb3dlq6UMIhRFERmI1xflJM-TECNRKQk0zd_QCQlUHW4sQAxiwn0qPL2g33MO_o-Qwo5KR8MugFfDqsdMrtZtIRDR_vY8zGrDouF7G8g1jesp2cL1QaXIfKkeXvzvcU3EbC5pPJsu2JGW3jvvwT03xQkXg30LvZv9kmctRsBhvHDW1EDwCvwDnm5ktAeIpOwgKxWnpFaxWZijzh2qnvzx-8KmewX05x0tD4dge67vUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94e5e813.mp4?token=W4ca4ryH6s3SyHHPZy810Y_2hHKEnBu-d251ePueF5ifAcGC17Z_GWhM5ibtUwxz-WrRQjgvXK3R_QFqw0ej7gvZcQnLDG_FPvFylAmGvLYyb3dlq6UMIhRFERmI1xflJM-TECNRKQk0zd_QCQlUHW4sQAxiwn0qPL2g33MO_o-Qwo5KR8MugFfDqsdMrtZtIRDR_vY8zGrDouF7G8g1jesp2cL1QaXIfKkeXvzvcU3EbC5pPJsu2JGW3jvvwT03xQkXg30LvZv9kmctRsBhvHDW1EDwCvwDnm5ktAeIpOwgKxWnpFaxWZijzh2qnvzx-8KmewX05x0tD4dge67vUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنزین گرون شده ایرانیا چیکار میکنن؟
ایرانیا:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/141386" target="_blank">📅 23:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141385">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
تو آمریکا بنزین ۰.۵ سنت گرون میشه
صدا و سیما: فروپاشی آمریکا نزدیکه
👈
تو ایران بنزین ۱۰برابر میشه
🔴
صدا و سیما: به قله نزدیکیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/141385" target="_blank">📅 23:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بانک‌های پرخطر VS بانک های کم‌خطر   مطالبی که اینجا می‌نویسم رایگانه؛ اگه فکر می‌کنید به درد کسی می‌خوره، برای دوستاتون هم بفرستید تا استفاده کنن.
✍🏻
آموزش خرید انس جهانی طلا بدون واسطه از صرافی خارجی
✔️
@mahaneconomy</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/141384" target="_blank">📅 23:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f753625931.mp4?token=hd-T_gMghVA17N8mTcwkqo0F5w9zlOatKNTmfJj9q3TmJ9HmwIGMYX4G8xY9UbTNpg6v6yFVl0B3ftyNtOIr6MluFotUwjmaYyzOpwkp-9md3pAZpZoTLzq9fJoL-jUSvB7Hg6kHRb17jQL4_RUTkV7UZJ3a758oPLN2tNS4PX96RNayGqqIbj_dYcjjBPhJuJdhmxuVxJu2WzyIfR35W77-dPnVoGr-M8nKjSty86vJNInwHbtIGCTHZcI5fPSDx8_4_8lsFali9ui42Eordkn1WRa0DM8rDnB0Bu9EZKJ7nu8735kLAgQ6BidCHKTc0GHlw3quQFXFEY47cN23Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f753625931.mp4?token=hd-T_gMghVA17N8mTcwkqo0F5w9zlOatKNTmfJj9q3TmJ9HmwIGMYX4G8xY9UbTNpg6v6yFVl0B3ftyNtOIr6MluFotUwjmaYyzOpwkp-9md3pAZpZoTLzq9fJoL-jUSvB7Hg6kHRb17jQL4_RUTkV7UZJ3a758oPLN2tNS4PX96RNayGqqIbj_dYcjjBPhJuJdhmxuVxJu2WzyIfR35W77-dPnVoGr-M8nKjSty86vJNInwHbtIGCTHZcI5fPSDx8_4_8lsFali9ui42Eordkn1WRa0DM8rDnB0Bu9EZKJ7nu8735kLAgQ6BidCHKTc0GHlw3quQFXFEY47cN23Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی‌زاده شیشه‌ای: افزایش قیمت بنزین در آمریکا ممکن است آمریکایی‌ها را بی‌خانمان کند و آن‌ها را مجبور کند خودروهای خود را بفروشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/141383" target="_blank">📅 22:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تو آمریکا بنزین ۵سِنت گرون میشه، قالیباف و ... توئیت میزنن که لذت ببرید و اولشه و ما بردیم. اینجا یهو ۱۰برابر میشه هیچی به هیچی</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/141382" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxAvb2Kwa9J-wTSoPKkhAW8oV4jVgi6AF3Adwav2OwZ2_u8XykfphUget_G7s0m_SbYOwmWehWf4KKfyLLWn5VBQVWZ4yIR92ljJJcBw2Zod8GZ1VwW-OnA4rWfETV_57hxUBEMrONZPvPy3beBmhOQxCuwWj0KbtlpU-RWob_yOeThNW9j29uhNxRxXmD-xtuuQixHSdkQeNX4dBlipmvWM6FDVTItZfcJeXdEz1Hqdsq9nWTda6vP-kLIJ0W_aSheSAaq63IlDMDyRyw7td3A7EEseJeCvj88LBzCZ48Bre7mRqeIB5hND8y0Ys0HR5ZhLBthZXqXWAme7AJdLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام اعلام کرد که نیروهای آمریکایی مسیر حرکت ۵۹ کشتی تجاری را تغییر داده‌اند، ۳ فروند از آن‌ها را غیرفعال کرده‌اند و ۲ فروند دیگر را بازرسی کرده‌اند تا از رعایت مقررات مربوط به تحریم‌های اعمال‌شده بر بنادر ایران اطمینان حاصل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/141381" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شما توی ظاهر فقط می‌خونی بنزین گرون شد، اما چه اتفاقی میفته؟ هزینه اسنپ و تاکسی چند برابر میشه. هزینه باربری کالا که از تولید کننده به مغازه میرسه افزایش پیدا میکنه و در نهایت جنس هم گرون میشه. افزایش هزینه حمل بار، وانت و مصالح ساختمونی. افزایش هزینه ارسال…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/141379" target="_blank">📅 22:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0947d4c92.mp4?token=f5dfHFy84uJLYtM3qwrMK6rY2L_hbGRVTyayiDumK3Y0X9VvmfG1dYV5fn4BaANuHxZvr7ekZXV-yk0LnYsoyNkaBya2jF4Pa0NaypLD1lGtvZwDTXSilWNFqmAdb7Z00oF6yd1vw-orDvU3TJe_wYk0PT_-mUl00hb4lGQAFTeVbuhull4aVNK3rSoxRCLy57uI4cdn6lg7WOXxvfTjiuUk1HToQJB6mN_v4JRLm5aQ-9gAMnWprvJAt0s-kyJd_xw15tJbqFpa7BprQA5nHICRpmbsdw38uE-Lpy-qJQBJ0Rxa1LSgz1LT2Tw9W5SEuZfQJulP5GqtMi-h028aAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0947d4c92.mp4?token=f5dfHFy84uJLYtM3qwrMK6rY2L_hbGRVTyayiDumK3Y0X9VvmfG1dYV5fn4BaANuHxZvr7ekZXV-yk0LnYsoyNkaBya2jF4Pa0NaypLD1lGtvZwDTXSilWNFqmAdb7Z00oF6yd1vw-orDvU3TJe_wYk0PT_-mUl00hb4lGQAFTeVbuhull4aVNK3rSoxRCLy57uI4cdn6lg7WOXxvfTjiuUk1HToQJB6mN_v4JRLm5aQ-9gAMnWprvJAt0s-kyJd_xw15tJbqFpa7BprQA5nHICRpmbsdw38uE-Lpy-qJQBJ0Rxa1LSgz1LT2Tw9W5SEuZfQJulP5GqtMi-h028aAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شما توی ظاهر فقط می‌خونی بنزین گرون شد، اما چه اتفاقی میفته؟ هزینه اسنپ و تاکسی چند برابر میشه. هزینه باربری کالا که از تولید کننده به مغازه میرسه افزایش پیدا میکنه و در نهایت جنس هم گرون میشه. افزایش هزینه حمل بار، وانت و مصالح ساختمونی. افزایش هزینه ارسال…</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/141378" target="_blank">📅 22:46 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
