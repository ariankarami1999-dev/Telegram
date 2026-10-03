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
<img src="https://cdn4.telesco.pe/file/mO5IzfKLgXNTU3Afdx1zJjQbAbzOvCqh3Dp0VHaIhMrXmeEeAQSMYlRTveZv6i8Nrp1IyWx0vgRmcVfbsTbgBgti6ZZH0YE0d6KL1GoTedKDsPmAHg07QA4XJ5G0bBSq3_JrQtnx2HyzhZBosx6GkbqQLp-ZOKN3hFepKaSEdahwYicqHHaXKOEZYXOSWjGpIWPb8HFKLEPiSYbyH-5YyZOzQQU0TQ7upTgYOVkd4betpLW62LWJf_E7aN1fiqeSvuzB8utcSl_5VsV21iycjEq-0MhUxWg33J7Lw64A0P3FOJEcXurpnu5XtT80t7cXIhbfjnn5VY5xyh5t8uz3xQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-150704">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دیشب در کمپ دیوید، ترامپ و کابینش جلسه محرمانه‌ای داشتن و آکسیوس گزارش میده که دست‌کم تصمیماتی گرفته شده.
🔴
موضوع مورد بحث این جلسه، ایران و یمن بوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/alonews/150704" target="_blank">📅 12:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150703">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abPPaXyeNGgGcDsaqGmr2aMlbW5NvNTwnQ2Qc7UXzaNWkkYcTw5LVmaw9KJ8bv_VoYSkkebwK6wD_chuHIr5d98gbA9oFntc6IiGxzgY3_mlLgszh1a8JqnhS_-Ip2aHOLWuXJJXVKN3uguzi6z-GJ0seyq7VRv04OxW32ii92s6qI-T4kcqSqKFE8yDqa_CrFW1hYHZZp4KD_p9Dcai1ULpSZ3kFHEUX92WPnJ4ibIURuT8QoYBn9Rp0WSod3L-xiW3MYqOo_FmyKX6DWy0vT8P7EuG4WdOjZYF1Hj8rsLEbW93V0d8jxXgKFjxc3HkqisUPJEbafCVDsijWqx4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از پارک جنگلی چیتگر در سال ۱۳۷۸ و ۱۴۰۵
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/150703" target="_blank">📅 12:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150702">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffde0cb90c.mp4?token=nTgJUIRUMFkQT7MHBeiFV_Qn8X_EK12OeOfZb9gtUM5sOHnrULbFNyHJy2Pe1LVhxib852Smig7b5vnH2-leWtS7PQJmLQ6cv1E_EZfhk4dEiMvc_cb5TNF662C3nSFLMFHOuZucoWshUI7kwhVmeizLunhI637kKFA4UClVnYxpZYk_zwf5C7Ip4q6DDGYhr0wxT3WmSo9wNHLYUF1NJzlveliYPx1-AzXv0sbwlqTkpiQ30mUDM1cgq6dKFV7lBrCYP4T8V0gJd952Lmqo9CFETVUG24Oselg8wwbm9Srf5D_VxQzD6R4Cq2YG8BQnd9PEJdaY-Ut8Yt6_8CGu5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffde0cb90c.mp4?token=nTgJUIRUMFkQT7MHBeiFV_Qn8X_EK12OeOfZb9gtUM5sOHnrULbFNyHJy2Pe1LVhxib852Smig7b5vnH2-leWtS7PQJmLQ6cv1E_EZfhk4dEiMvc_cb5TNF662C3nSFLMFHOuZucoWshUI7kwhVmeizLunhI637kKFA4UClVnYxpZYk_zwf5C7Ip4q6DDGYhr0wxT3WmSo9wNHLYUF1NJzlveliYPx1-AzXv0sbwlqTkpiQ30mUDM1cgq6dKFV7lBrCYP4T8V0gJd952Lmqo9CFETVUG24Oselg8wwbm9Srf5D_VxQzD6R4Cq2YG8BQnd9PEJdaY-Ut8Yt6_8CGu5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ریاض عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/150702" target="_blank">📅 12:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150698">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4829d2be.mp4?token=KeKvu4HtVRoZAXCXh1j6m3uIKSK2qAjEPiz3vcxvFKgDLW4avc5clnVfFpLAO6SPsTgYItAAjUe-j47SxJKCbHKo6Oi9VRzHQg_i6BvmBZ3vJijglSV3wjdY3DnL4Zb3L6zQWnhflg6gYIBxfKMdywgzc6gs1M68801YROj8B1Q6uMw3b5wdgqtQ7b87i6z_iSrh--SB7Cpa2zuRHQVgSYVUQBLf-WhJ_WnP9dg2xIsxj1cLHE0ERaStOwkpWLVNxOBGf6DoLEyespOEo63NZFeKfyIGCctN41sl4lA7ylJhzwjz4lQQBCKJGyJ6-dTIfO62ZyquFiB0pYMjkzyjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4829d2be.mp4?token=KeKvu4HtVRoZAXCXh1j6m3uIKSK2qAjEPiz3vcxvFKgDLW4avc5clnVfFpLAO6SPsTgYItAAjUe-j47SxJKCbHKo6Oi9VRzHQg_i6BvmBZ3vJijglSV3wjdY3DnL4Zb3L6zQWnhflg6gYIBxfKMdywgzc6gs1M68801YROj8B1Q6uMw3b5wdgqtQ7b87i6z_iSrh--SB7Cpa2zuRHQVgSYVUQBLf-WhJ_WnP9dg2xIsxj1cLHE0ERaStOwkpWLVNxOBGf6DoLEyespOEo63NZFeKfyIGCctN41sl4lA7ylJhzwjz4lQQBCKJGyJ6-dTIfO62ZyquFiB0pYMjkzyjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات دانش‌آموزان در فرانسه:
🔴
۶۲۵ نفر بازداشت شده‌اند
🔴
۸۳ مأمور پلیس مورد حمله قرار گرفته‌اند
🔴
۳۲ معلم زخمی شده‌اند
🔴
صدها مدرسه به آتش کشیده شده‌اند
🔴
خودروها و کلیساها به آتش کشیده شده‌اند
🔴
دانشجویان آفریقای شمالی‌تبار و دانشجویان چپ افراطی علیه دولت فرانسه اعلام جنگ کرده‌اند
🔴
تا کنون کسی کشته نشده !
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/150698" target="_blank">📅 12:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150697">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUwOlkdWzRAnxKt9-cEJnsw9nPdW0PDJYj_0gfd6k0j6z-ccGq2s2peJAZlnwXa0lJXUdOzf-4bMrOrqs8ljyLzkZqVLQybuGn44hSP1aixeRwr3sENMKn-_rISqkB0M9pTao7KHLrZkbFd00uGJ5G2_Fmau6w_ioKIKjehIa9y6OncPf9a1UoxyaptC4ZRCY9qOrWIp9nMk-mIhDjXXpExdAGlypvyC6VCZ6utcjaB8fAz1y5GoewixnqHzrC2GIuiUxYF6SlWDavLRUWBoqqNiPgj83tmSuYxLV31TI80tng2whspcXTFhOx7FK_jSezPSIQg7aU2TGzzU3qilPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکم شهریور 1405 همین ۴۰ روز پیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/150697" target="_blank">📅 12:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150696">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هر  یک دلار 267,200 تومان شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/150696" target="_blank">📅 12:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150695">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJqXQc6zQzuiu9zOZXePi3hpBAg8bVrLJ4c3CPG9yJaPejYEcS-3aIbzr76BNsx_ynwpuHDG_l97w10f4scpPJxKCRiz4XT1YD3F_N74nYzQBBHAA9XLxJUhYNN5aDLgoL_TgceaRP1eL8Oj7TtR895ezwHJ8Uue2kiLBFHACUPuspncCvmCRnzQmjBmVjtLuFXu_QPKYxtvutjgRpyGawB6CUHfUxG8gRDN4QtJCtBmzFBvs828Ck3Ec3XNfsebFV9r7nFJPn3pbDk6BpiIwi24DIIZtCNRLx8xyDadEGZd1oGbw-6NvFDeNBHwcfn5U7dvs6A2zg8eFuXf8xIVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری وایرال شده از رژه جان فداها در اصفهان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/150695" target="_blank">📅 12:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150694">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
تعویق رأی‌گیری سنا درباره توافق هسته‌ای ترامپ و عربستان
🔴
سناتورهای آمریکایی اعلام کردند رأی‌گیری درباره توافق‌نامه همکاری هسته‌ای غیرنظامی دولت دونالد ترامپ با عربستان سعودی، پس از برگزاری انتخابات میان‌دوره‌ای و حداکثر تا ۱۳ دسامبر انجام خواهد شد.
🔴
این تصمیم در پی ابراز نگرانی برخی نمایندگان- به‌ویژه دموکرات‌ها- درباره خطرات اشاعه سلاح‌های هسته‌ای و احتمال شکل‌گیری مسابقه تسلیحاتی در خاورمیانه اتخاذ شده است.
🔴
این رأی‌گیری به کنگره اجازه می‌دهد تا پیامدهای انتقال فناوری‌های هسته‌ای آمریکا به عربستان را بررسی کرده و موضع رسمی خود را اعلام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/150694" target="_blank">📅 12:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150693">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
👈
تیراندازی در مقابل دادگستری مهاباد
‏
🔴
خبرگزاری صدا و سیما: دقایقی پیش حادثه تیراندازی در مقابل ساختمان دادگستری شهرستان مهاباد رخ داد؛ حادثه‌ای که در پی بروز مشاجره لفظی میان چند زن، با ورود مردی مسلح به سلاح کمری و شلیک گلوله همراه شد
‏
🔴
در جریان این درگیری لفظی، مردی که یک قبضه سلاح کمری در دست داشت، به سمت زنان نزدیک شد و اقدام به تیراندازی کرد. جزئیات دقیق چگونگی وقوع حادثه و ابعاد آن تاکنون مشخص نشده است
‏
🔴
اطلاعاتی درباره شمار مصدومان یا تلفات احتمالی، وضعیت جسمانی افراد حاضر در صحنه و همچنین هویت فرد تیرانداز منتشر نشده است. همچنین علت اصلی مشاجره و انگیزه احتمالی تیراندازی همچنان در هاله‌ای از ابهام قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/150693" target="_blank">📅 11:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150692">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b5ad2c555e.mp4?token=lRuzpqAWDPlUl8h3Rbwe2xoTi41sX8uPEnCGHIHNRMA7-OX-ZeJqgssBSwzjxoxro-5_OlrGuZ0QzL7P2jQOMeJ8tTRyxfUDuGekFbLtpPDji5-EJ6GkKZPNswPKtkKYWw3TlC28bkmm_-S1KwVqBqlvezGAPq3SyMFDvevxSfJpdGxbd25SUwiToTKqDFkhuaqG0Z1tvecVHzqPwuRp2V2LfrCSdeLlBv-Lur026Gg7AETRbOvpsirV73D4byhsz0hoFMSSdqqW_m0aYi2h-6udSzPur0bhSPhDIurzg0N7Iy6A5RQ94eaQd1oiGcfx3nB_3WXoPKj-PaKxGVu8LB7oM9ipSmaLqL1VYVk_ZBRVMdAj3STZPRhRDGqSJFS0n3l802Q7NLlUlnzAwJBO99IvgNnZZht5FH96p-wn2z1VJIw4xwLfuTBPhV4sqd0m2sXuCKSqYNbzZPWQeZ7g9UyQVcDIwTsQLNCo3vCA-FOJ6VrURLEPyqn0rx2axZ3jFHiz_fKRKpEjXgPiwR-3AfgWisr-AE4pBcqi6UWzS7yCaGDdjysWroEm9l8GGXIVYscKMCZbosr-ftvRKlgy9U2_rV5NPj2p-AvHGX3m4rnWkZQ66TdeXH5enMUeimjisMIOVTnY__Xs4JUo9e4WxDKN3Xxfj9EZUikyqE77K-c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b5ad2c555e.mp4?token=lRuzpqAWDPlUl8h3Rbwe2xoTi41sX8uPEnCGHIHNRMA7-OX-ZeJqgssBSwzjxoxro-5_OlrGuZ0QzL7P2jQOMeJ8tTRyxfUDuGekFbLtpPDji5-EJ6GkKZPNswPKtkKYWw3TlC28bkmm_-S1KwVqBqlvezGAPq3SyMFDvevxSfJpdGxbd25SUwiToTKqDFkhuaqG0Z1tvecVHzqPwuRp2V2LfrCSdeLlBv-Lur026Gg7AETRbOvpsirV73D4byhsz0hoFMSSdqqW_m0aYi2h-6udSzPur0bhSPhDIurzg0N7Iy6A5RQ94eaQd1oiGcfx3nB_3WXoPKj-PaKxGVu8LB7oM9ipSmaLqL1VYVk_ZBRVMdAj3STZPRhRDGqSJFS0n3l802Q7NLlUlnzAwJBO99IvgNnZZht5FH96p-wn2z1VJIw4xwLfuTBPhV4sqd0m2sXuCKSqYNbzZPWQeZ7g9UyQVcDIwTsQLNCo3vCA-FOJ6VrURLEPyqn0rx2axZ3jFHiz_fKRKpEjXgPiwR-3AfgWisr-AE4pBcqi6UWzS7yCaGDdjysWroEm9l8GGXIVYscKMCZbosr-ftvRKlgy9U2_rV5NPj2p-AvHGX3m4rnWkZQ66TdeXH5enMUeimjisMIOVTnY__Xs4JUo9e4WxDKN3Xxfj9EZUikyqE77K-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، می‌گوید قیمت بالای نفت هزینه کوچکی در ازای هسته‌ای‌زدایی ایران است
🔴
«۴۰ درصد. اما درباره نفت یادتان باشد، شما دارید هزینه‌ای می‌پردازید، اما این هزینه بسیار ناچیزی در مقایسه با چیزی است که اگر این افراد به یک سلاح هسته‌ای دست پیدا می‌کردند و از آن علیه موبیل، آلاباما استفاده می‌کردند، باید می‌پرداختید.
🔴
خب، چنین چیزی اتفاق نخواهد افتاد. و ما حمایت فوق‌العاده‌ای داشته‌ایم؛ واقعاً حمایت بسیار خوبی داشته‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/150692" target="_blank">📅 11:52 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150691">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رئیس سازمان سنجش : نتایج کارشناسی ارشد اواخر مهر اعلام می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/150691" target="_blank">📅 11:37 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150690">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb3de2fd69.mp4?token=eytkRHf5jVkvvNgipZyy56X20PKwXpJU-FUkKFt9NtBvA0KaMRxqwvBSpCwXvyl1o0aLPGq3Uc8_3hERmYkbl4hgmqx-bkbNg66sHB69o8gJ7jmQvmTvpY1XGNfXWzimHcH257-IFx00HoSCZQDzF8pJeLD6tUVxgQGlSQWJmhsJUlnBxL1uQRVZeptxQv88qeavM-FFDbujvx3HgdwUAo8Vlt8hgjjFCdv86OEe7mp1VQ6AdMsXFTpeUHrDWNd7ZW73x1lfPVq2ywOfIQA9wbDF58tTsoaJfiOhuZGRMdZuc3HZgGlsIJXXLGfi-Y3ytzY9w_KW2sXdw4_sLeL3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb3de2fd69.mp4?token=eytkRHf5jVkvvNgipZyy56X20PKwXpJU-FUkKFt9NtBvA0KaMRxqwvBSpCwXvyl1o0aLPGq3Uc8_3hERmYkbl4hgmqx-bkbNg66sHB69o8gJ7jmQvmTvpY1XGNfXWzimHcH257-IFx00HoSCZQDzF8pJeLD6tUVxgQGlSQWJmhsJUlnBxL1uQRVZeptxQv88qeavM-FFDbujvx3HgdwUAo8Vlt8hgjjFCdv86OEe7mp1VQ6AdMsXFTpeUHrDWNd7ZW73x1lfPVq2ywOfIQA9wbDF58tTsoaJfiOhuZGRMdZuc3HZgGlsIJXXLGfi-Y3ytzY9w_KW2sXdw4_sLeL3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر جدید از تداوم آتش سوزی در پالایشگاه آرامکوی ریاض درپی هدف قرار گرفتن با موشک‌های یمنی
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150690" target="_blank">📅 11:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150689">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
مجری صدا سیما: اگه به رهنمودهای آیت الله العظمی امام حاج سید مجتبی خامنه‌ای دامه برکاته گوش بدیم مشکلات حل میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150689" target="_blank">📅 11:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150688">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هم اکنون ،شلیک چندین موشک از صنعا،یمن
✅
@AloNewd</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/150688" target="_blank">📅 11:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150687">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
دادستان کل امارات: کمک خلبان پرواز فلای دبی قصد انجام اقدام تروریستی را داشت
🔴
دادستان کل امارات: تحقیقات پیرامون حادثه پرواز فلای ‌دبی نشان داد که کمک ‌خلبان قصد انجام یک عملیات تروریستی را داشته است.
🔴
طبق نتیجه تحقیقات کمک‌ خلبان هواپیمای فلای ‌دبی در حین پرواز شروع به اجرای نقشه خود کرد و با استفاده از تبر اضطراری به خلبان در داخل کابین حمله کرد. تحقیقات برای روشن شدن تمامی ابعاد و جزئیات حادثه فلای ‌دبی ادامه دارد.
🔴
پیش از این مقامات ارشد اطلاعاتی و انتظامی اعلام کردند کمک‌خلبان هواپیمای فلای‌دبی که متهم است روز چهارشنبه به کاپیتان حمله کرده و قصد داشته پروازی به مقصد اسرائیل را ساقط کند، تبعه عمان است؛ فردی که پیش‌تر به دلیل شناسایی به عنوان یک تهدید امنیتی، از سوی شرکت «عمان‌ایر» از پرواز تعلیق شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150687" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150686">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd1ac59b80.mp4?token=LS2GItuNcGOca2Clqi1-RbG1QqYuvIW6YI6R8XBb3cnx2kYb2WDIO6FqcZbgDFGZQO3DLLuzAPQ2_74pkbFGwjLxFwWy6_JuJuLhykAwpp8BBkxq5B1AAo5zWcsI4d9zbm51Cwa2Qv5rAkH1_AjnKjjRWvXkOOMgZ-Rx-GwjxKAX-LdfvBm7oFgMKWV7pZCFiQjbhg9EsxNkKMZY4b3z9RZr_63QwG4aXmxgHFufrs6rVWcc5cCyTk3qjHDGca_M5zs_j66RtN44c9NsjLFTAQQy1lJ3jDkrPZonkDcNrIAKmX0KqGQrjniU9FakhCcx_ZVtOCeZZXFP-XETqumF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd1ac59b80.mp4?token=LS2GItuNcGOca2Clqi1-RbG1QqYuvIW6YI6R8XBb3cnx2kYb2WDIO6FqcZbgDFGZQO3DLLuzAPQ2_74pkbFGwjLxFwWy6_JuJuLhykAwpp8BBkxq5B1AAo5zWcsI4d9zbm51Cwa2Qv5rAkH1_AjnKjjRWvXkOOMgZ-Rx-GwjxKAX-LdfvBm7oFgMKWV7pZCFiQjbhg9EsxNkKMZY4b3z9RZr_63QwG4aXmxgHFufrs6rVWcc5cCyTk3qjHDGca_M5zs_j66RtN44c9NsjLFTAQQy1lJ3jDkrPZonkDcNrIAKmX0KqGQrjniU9FakhCcx_ZVtOCeZZXFP-XETqumF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رسایی چندسال قبل: زندان اوین هتله
🔴
هتل خوش بگذره
❤️
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150686" target="_blank">📅 11:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150685">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKI9O3iWF_iG_zChz2xNZgJLS7WAU8Qotqb0r7kKoHec_3nrYLExrW_g1maHWtIcxGW8d_wltD1CZ8HjLGbz2eOZdMv72M9BmAfmAot1_fBgKu4pET4qgXkGCKncs_nM3uOR2f8xivw9a7CAjDtDYOA6PBzZ6P2Dj851ulLxBWk60xK0NqQtbfeIbABMucNg8VNhva8jmceIfyAardRiykoJGHqvz9pPadt-q-MqSOXzFUQ0tyPcP5_w3n2ZDfr2mPdEYdDtiSCJ9zn6P24lkv6RMo4UmZLIJQT-igGo8eqazz1Xln6vBdcMVYdyIzCGYPgjoJrMGTeKCVTm97kUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین تصویر از کمک‌خلبان فلای‌دبی پس از مهار او منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150685" target="_blank">📅 11:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150683">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G__61qWSFx5kgs6kZmGe0N1FJ-14HRSFpWzqF4QbHvQ__AlMZBLfrp85_tNmUC1UF8GNETELMdxmaqTpb8u6e5uiYFcLVKUPbQ07f775wL49JmPsgdDKznNQjboLfgLHeAWF8a3JE-w-tuvxS1ieGYfrEMbMM01jAxuNoC5tJj_ChuoYFNVv0UJDqqUsTRuBA5-5CBrRBi9ihRbU8XgU96o7UVINeBDFh5s5UqE9DnaNVnZ7AqbhVIafY9oGAA3GkfKCRINjj8t0MtURXwKXHGg1XSYedrwHAbjEbei-SapmTdu9pHiunIknm0mcszS822Dj3cVWQ_qpbA1puQu19A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdXA5ye3kY6L62jitSP28w4oKiqXvTAUe7mfcRzyN7JhrAbYoMKRm2YA17O7tAywRFJSZAdc8nkSbDcccj21WMyP1xKD3YRijpx5rae75gyGbMQZnetM1BCyWA_76oSU9t7dKYkbx36OrginopOkiUWpHc8SBcRH7jsnEQultled2-2cjWp04bFi2KQrGCkCPZlWExba9WRK868ZcnYh6ayWoW0RSpDfnXtKQCB9prgGG0tdGIVYuHg_ylcrA4mbD3t3TBye9wvpYgcCYo943HDCQV2R33W4MMyMhxgHXowFDTTJaXlCDw-QPWRN2U-46d6UMahFAmn-UKx4OoNxqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اسامی نفرات برتر آزمون سراسری اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150683" target="_blank">📅 11:00 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150682">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/معین خواننده مطرح اعلام کرد بزودی به ایران بازخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150682" target="_blank">📅 10:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150681">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
توقف پروازها در فرودگاه ملک خالد ریاض همزمان با انفجار در عسیر عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150681" target="_blank">📅 10:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150680">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
طلاگرمی 26,012,881
🔴
تتر[USDT] 265,300
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150680" target="_blank">📅 10:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150679">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhbcGLwOndj1vikgQLbMkFbIt1SL-P_gCDFEWofPiyHFfFOav2MrF5bREd9jDjTuMZ9Z9YcgNNpC7MVRYWldmkuuTPtloKZcAJzD_BfFymz7Bu8pIDT_2HQAxKSNHGlY6XFlM_7VlG5QzkBtsmMsaAQx9T7JisEs9-2zC3wVnblORcNcC9foHaShxiLTkjfYcwyv1Vw0b8ciG7_1kaY5cdU8QSkKw4fL9v3tXK8Rdc28Ov1_xSpX7zEVv5Tk_2HkgSjTEiJvrisRcWi3AEpCF2pxlLprhiCQSrK8hf2CNBOrLi4lkxRfHIkbePQqLXyKH7bLxEzef2T2ONRYgzBWHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آمریکایی: ترامپ بعد از انتخابات به ایران حمله زمینی میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150679" target="_blank">📅 10:49 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150678">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbsOF4c8tTK64_pjcVqItKIq7eeZRMRY5wmcEciEqkuVS86WeCLQRChYTpSVR1WHZBWVYrQJlgN9siAsheR5jTUBqLBB6P63JOkf0vWDKc6jxPQp4K12v50It6mkOk7lg3r4Yeu-PaAsgVSMxDmvnTKsoUpZmfZV_Xx68TT7QgsnmORMHN0FYh_FdpuyIfmQ_rpJsb-dLilGZ9kC0xMu7STXM9ZcmzB8VT_Ma59uICTzGQ-Ly6eSPSayX92LetwGkt3sos9Ojv-tbFFiupInsopkK4-iDNLp7IberEe-xTDg3RCc_Kh3iDIfKryDmTAgauNu2xh8hYuGiZf-UxbJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقائی بدون اینکه خندش بگیره خشونت پلیس فرانسه علیه معترضان رو محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150678" target="_blank">📅 10:42 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150676">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S2lDqIEx9x488lzuyDCmK45eetb4eSBuyjKybyzzcxwBBtgw8d9_eNRSPgDwk4HnDGg1CiZk5XaA8u9ppw5y8LCD0wHZ2glfg-zh3b4VX_9uWPq9xX7IiVE8D2NHC-CTLsL2xvGBNIVI9Kd3cSwNOsSAKmBglE12_MJdjvWtSRcq_b6MHjbYLIfXHCribbMqD8Obgm5l0Zemol-4gfkqPdQzcEPA35xNg087B_YuSgRzXs_IOOIiH9esmB_9dQvZsi44jVmgPzBDnXrzMMugHpJP6GwKXoyfZUPd5Hzy0q3lQCRWtnaZbWT6h_KhCGUjOcIfi8UMuMSk0hPyJZYITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=AasXGMGmZR0yvtM_SPW8cW7HB1cYsS8_7y8W31aPOzK57HYrTe03Vo--OGKBVphKUWOqZmtmSGvfKGPvA4DSak-E9Rjsc0qKgUOeOmD11zX7X9vjuO7KsXcMWjnB3BruoLiV21DpCRjKYWcZlSrTgiBrHyo8PhyfW50bXns4Wf8RdtkK4327VxfXdMKglksu2m31UShKtdXmqt1QmiPOEJJ9SXFWG4vvnUO49McjGcYkS6sTGBQb1AyFCbwEybNixHpt_xl6pXmdUPXlYqmhTpsCc5XjcbUULK5tLkBxsW6myLquMTOVevERhGJGnSZKCNhhPgW5v-wwahpQlM2FIw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc83c2d7b4.mp4?token=AasXGMGmZR0yvtM_SPW8cW7HB1cYsS8_7y8W31aPOzK57HYrTe03Vo--OGKBVphKUWOqZmtmSGvfKGPvA4DSak-E9Rjsc0qKgUOeOmD11zX7X9vjuO7KsXcMWjnB3BruoLiV21DpCRjKYWcZlSrTgiBrHyo8PhyfW50bXns4Wf8RdtkK4327VxfXdMKglksu2m31UShKtdXmqt1QmiPOEJJ9SXFWG4vvnUO49McjGcYkS6sTGBQb1AyFCbwEybNixHpt_xl6pXmdUPXlYqmhTpsCc5XjcbUULK5tLkBxsW6myLquMTOVevERhGJGnSZKCNhhPgW5v-wwahpQlM2FIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی ایالات متحده (SOUTHCOM) تصاویری از فعالیت شناورهای سطحی بدون سرنشین Saronic Corsair نیروی دریایی آمریکا در پایگاه دریایی گوانتانامو، کوبا منتشر کرده است.
🔴
همچنین SOUTHCOM اعلام کرده است که پایگاه دریایی گوانتانامو میزبان یک مرکز آموزشی برای شناورهای بدون سرنشین و خودمختار خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/150676" target="_blank">📅 10:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150673">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f36095dc2.mp4?token=IBbtSfxlos_0F8umDT5yqtApKkws01gPjvLTK6lDV2f0PeO_kdKxPRetusd8H8EYf2Jo1A-m8Spy3VgcUfwRttw7wLn6KCgxKlP57f-I0e8VGNRqFcwALZzVhfomEonJ91gYbjCV8w2bcJptrm1mcOqLI68k6NjedDX3fdRhKO2wTCmyMqfeLWXI5sqMcnbd3GO5tz1zRf2okG319NysZyf-jAZ3LZv8ozntCZY-qUZQhDxylR8NOEXUcaMsDSImSjUgkbvibAjZEVILn5TQvXQqOR3zOchvBOQ7GJS8KiQkTjHN1WO-sEpPE776TnFEkqTB5QmHmNx3eZxRlNdjzixahCFgEZGI2ATaIhnblrjzVKUE-kQcs8wBM3q5T67WdiiaA1dYELPsmHg9BhkjxmCBLKOQgy2uGRm1m0a-ZBysfNTUfCFWVcDpDh3I5s5t34lQWfo-tkgUHFoN-VBlUtzwh_zxPEiBf8ChT35RmEOQkoqgKzvCn19Rx2ztqdagVM869rucUs9yRs_OLeESX8U4900h1ADA2KWOESk1DLO_EvxdNRRBaBy75DXT-T4MJW9q13WBVREZAUgP0dPTEJNB8SOwSv4CzfQIwcoPbncwzFwv89wDSXPnWToMUOR9fnMDz9nyD3FtVwmMo3E-xVDoW2zXXiQXwThz_ZxmAiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f36095dc2.mp4?token=IBbtSfxlos_0F8umDT5yqtApKkws01gPjvLTK6lDV2f0PeO_kdKxPRetusd8H8EYf2Jo1A-m8Spy3VgcUfwRttw7wLn6KCgxKlP57f-I0e8VGNRqFcwALZzVhfomEonJ91gYbjCV8w2bcJptrm1mcOqLI68k6NjedDX3fdRhKO2wTCmyMqfeLWXI5sqMcnbd3GO5tz1zRf2okG319NysZyf-jAZ3LZv8ozntCZY-qUZQhDxylR8NOEXUcaMsDSImSjUgkbvibAjZEVILn5TQvXQqOR3zOchvBOQ7GJS8KiQkTjHN1WO-sEpPE776TnFEkqTB5QmHmNx3eZxRlNdjzixahCFgEZGI2ATaIhnblrjzVKUE-kQcs8wBM3q5T67WdiiaA1dYELPsmHg9BhkjxmCBLKOQgy2uGRm1m0a-ZBysfNTUfCFWVcDpDh3I5s5t34lQWfo-tkgUHFoN-VBlUtzwh_zxPEiBf8ChT35RmEOQkoqgKzvCn19Rx2ztqdagVM869rucUs9yRs_OLeESX8U4900h1ADA2KWOESk1DLO_EvxdNRRBaBy75DXT-T4MJW9q13WBVREZAUgP0dPTEJNB8SOwSv4CzfQIwcoPbncwzFwv89wDSXPnWToMUOR9fnMDz9nyD3FtVwmMo3E-xVDoW2zXXiQXwThz_ZxmAiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراضات تو فرانسه  همینجور داره بیشتر و وسیع‌تر میشه؛ از درگیری با لباس‌ شخصی‌ها و پلیس، تا حمله به ماشین پلیس تو روز روشن و حمله به یه لباس فروشی و غارت لباس‌هاش !
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/150673" target="_blank">📅 10:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150672">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85d3a8a0d8.mp4?token=o8e_2eQbpzbkoqwGiHFkYQzYSIi-NlcNslpbb91Xjr_8NM-ZDLeQE_onC7KiQsK8TuqSAFaWzj59V95eICvZEDSAIwzGdtYGjXCkC9dhE3xeJcawbBBXUhVGiyuSyVmj4qOjSd3nnPgQKn01e5Cn67bmPfBkU3YfpMxHq4ck3Zh6qPjXCLqSW0Xs3AzibjrrxouUIaetygREMN61dWHE5MTvZf_domWLiS0d93HBfHIiDJn8pbxTKLiBnKxhFDlfK1BryEAB8geTfQ6jw1-L37RRBexWjHMSyu92eOFYIeExJSwaKaD-kcVEm8cF2FgN6bSgCQNw4K3L8ltfSNuRMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85d3a8a0d8.mp4?token=o8e_2eQbpzbkoqwGiHFkYQzYSIi-NlcNslpbb91Xjr_8NM-ZDLeQE_onC7KiQsK8TuqSAFaWzj59V95eICvZEDSAIwzGdtYGjXCkC9dhE3xeJcawbBBXUhVGiyuSyVmj4qOjSd3nnPgQKn01e5Cn67bmPfBkU3YfpMxHq4ck3Zh6qPjXCLqSW0Xs3AzibjrrxouUIaetygREMN61dWHE5MTvZf_domWLiS0d93HBfHIiDJn8pbxTKLiBnKxhFDlfK1BryEAB8geTfQ6jw1-L37RRBexWjHMSyu92eOFYIeExJSwaKaD-kcVEm8cF2FgN6bSgCQNw4K3L8ltfSNuRMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از پالایشگاه ریاض، متعلق به شرکت نفتی آرامکو، به هوا برخاسته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150672" target="_blank">📅 10:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150671">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb79ecbf18.mp4?token=V3xqsEsRXKc2t8drnMCxocnitEbcsi-oUT5BsF3YaRV8MXUZLFT3_jBax6nDBEdTAlK2juHZ2aVPEDG2ifmBoNC-2Tfj6SNx0VXeuZJEQnePNNJEOZWne3iBG9m8emuMpR2opq5LDgaWo8EfZX8h5_wA94yfMcgomZaBu-EKp6TOB3hCbw2E3ayf3Ey-85hCNVIwXfEHJK_iTT4PPELGCl9WP9i88xV7k7IFLMXTPXxBYPLPTZd13Dotpw0ek49PYK33MjDWDlOQXqqn_mxnU-bhhN21oc1DiNjPCOfAqUdhPlZmij-qOCoNF0028CmwEOf1VClguwC6f6lMW8c8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb79ecbf18.mp4?token=V3xqsEsRXKc2t8drnMCxocnitEbcsi-oUT5BsF3YaRV8MXUZLFT3_jBax6nDBEdTAlK2juHZ2aVPEDG2ifmBoNC-2Tfj6SNx0VXeuZJEQnePNNJEOZWne3iBG9m8emuMpR2opq5LDgaWo8EfZX8h5_wA94yfMcgomZaBu-EKp6TOB3hCbw2E3ayf3Ey-85hCNVIwXfEHJK_iTT4PPELGCl9WP9i88xV7k7IFLMXTPXxBYPLPTZd13Dotpw0ek49PYK33MjDWDlOQXqqn_mxnU-bhhN21oc1DiNjPCOfAqUdhPlZmij-qOCoNF0028CmwEOf1VClguwC6f6lMW8c8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: نمی‌دونیم با کی مذاکره کنیم
‏
🔴
کسی در ایران نیست که با او مذاکره کنیم. هیچ‌کس نمی‌خواهد رئیس باشد.
‏
🔴
می‌گویم: با چه کسی در ایران صحبت کنم؟ در می‌زنم: تق‌تق؟ هیچ‌کس خانه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/150671" target="_blank">📅 10:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150670">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
گودرزی، هیات رئیسه مجلس : دشمن بدونه ملت ایران به کمال نترسیدن از مرگ رسیدن و هزینه جنگ رو کمتر از تسلیم میدونن و ما برای جنگ بعدی برگ‌های رو نشده داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/150670" target="_blank">📅 09:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150669">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آکسیوس: ایران و آمریکا مدام حرف می‌زنند؛ اما حرف هم را نمی‌فهمند
🔴
باراک راوید در آکسیوس نوشت تهران و واشنگتن هر دو از ترجیح دیپلماسی می‌گویند، اما توافق از همیشه دورتر است؛ طی ۱۸ ماه گذشته دو دور مذاکره شکست خورده و هر دو بار به جنگ منتهی شده و تفاهم‌نامه ژوئن نیز تنها چند روز دوام آورده است.
🔴
به نوشته آکسیوس، مشکل فقط مفاد توافق نیست؛ ترامپ به‌دنبال توافقی سریع و قابل‌اجراست، در حالی که ایران مذاکره را فرایندی طولانی‌تر می‌بیند و خواهان تضمین و دریافت امتیاز پیش از اقدام است.
🔴
این گزارش «بی‌اعتمادی مطلق» را هسته اصلی بن‌بست می‌داند؛ تهران آمریکا را به حمله در میانه مذاکرات متهم می‌کند و واشنگتن نیز می‌گوید ایران پس از تفاهم ژوئن آن را نقض کرده است.
🔴
آکسیوس می‌نویسد اختلاف بر سر این است که چه کسی اول امتیاز بدهد و چه تضمینی برای پایبندی طرف مقابل وجود دارد؛ شکافی که هر دور دیپلماسی را دوباره به تهدید، تحریم و خطر جنگ می‌رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/150669" target="_blank">📅 09:48 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150668">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeHKMrnouDKld76pE9Py6P3csDGzWwzqFEkUOOzB5ErPcyyrnCFE9eYw-NiMGn9OlOtZCeiQVMggsSHv2OlgbdXEX3dFY23jTKoXumwgflvwFcQHDGGtRGiQ6_JX6qRlergDQ09n4nKVoEZhJ-zkxwJ93dkdwy_0tAVgWQZxoBCAQSLsojPQ823ClXxFhi-bS8neARaYM5az7-nPJIHjqdqDMi3anWqGYFP4h2BVhvFRo6KmdkilGv46rMfL9cdLG4slhbRE7kUKponNALcb0VByshcSlxfw9ge6G9KvmHTrNOciSA0uPPcCxI5L1CBPxPt1WJgxB-ovjPxkusxp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین تصویر از کمک‌خلبان فلای‌دبی پس از مهار او منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/150668" target="_blank">📅 09:34 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150667">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
گزارش استیضاح وزیر کار به هیئت رئیسه مجلس رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/150667" target="_blank">📅 09:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150666">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f398c56e.mp4?token=LCOYSKKtpOPdA8eq7LW9orXoKW6JQLaTlqbWOCJp0ESljRuBxU29dZvpnn7DEg1LFtuS52wdvuzVJJRCOT2alAArXtWKydZNNWwVG1wMYD7yLPCJxWZHfyCntVnnQzZK2A-OmBHGcuntc1aK5icxa7L8f-dR3ISQ9U2VdwuAyXCXlFpBU27GyF2duqk5ucjdhibLGHXL-g02sXQ3E123MfQ0yrpyLAbkSudnVaAzucFNH3PtEZAt5-jUTVyTuCC1-a1IQ9qFj_0Khbx1P2Awuc-EFzigbYY3gP0kSZABNBkoT1v1kEIOmJWTn_tSa337y4kWDrECN6_freA2jp8RIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f398c56e.mp4?token=LCOYSKKtpOPdA8eq7LW9orXoKW6JQLaTlqbWOCJp0ESljRuBxU29dZvpnn7DEg1LFtuS52wdvuzVJJRCOT2alAArXtWKydZNNWwVG1wMYD7yLPCJxWZHfyCntVnnQzZK2A-OmBHGcuntc1aK5icxa7L8f-dR3ISQ9U2VdwuAyXCXlFpBU27GyF2duqk5ucjdhibLGHXL-g02sXQ3E123MfQ0yrpyLAbkSudnVaAzucFNH3PtEZAt5-jUTVyTuCC1-a1IQ9qFj_0Khbx1P2Awuc-EFzigbYY3gP0kSZABNBkoT1v1kEIOmJWTn_tSa337y4kWDrECN6_freA2jp8RIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «ایران برای ریاست‌جمهوری انتخابات دور دوم برگزار کرد، اما هیچ‌کس در آن شرکت نکرد. همه می‌گفتند: «من این را نمی‌خواهم.»»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/150666" target="_blank">📅 09:25 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150665">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d072f8ec59.mp4?token=NgjHItl_xn4pAbvruGHOp0hDy8TI0B9XT27btFC60brZD7SeP_UxJJNLtCULwVAGLmtmY19o56GlOj6lvvoIaCfehSD5pm5W6e1VV0q1mLgZFYfCUlkjU8D67GvzcKMJqJ-WoyuYITR4fGtzCAKUbnwayHpJfqYvzlY9LmH6u-j_ZtstYmcX_jKcX3RBVbaXkVsAp4DkNAx3h2cgVjZ_gT8Mro791DqdR39NIdxBs6RNP-cpEpycRQIxn_L38auOGcIrczxHL3uGyAiK0T0s5vM3CqjUF144yrEe2O7SpBONw-THNzPjzhOlmNbQrod0LbC655R-TXljupEAQEb4rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d072f8ec59.mp4?token=NgjHItl_xn4pAbvruGHOp0hDy8TI0B9XT27btFC60brZD7SeP_UxJJNLtCULwVAGLmtmY19o56GlOj6lvvoIaCfehSD5pm5W6e1VV0q1mLgZFYfCUlkjU8D67GvzcKMJqJ-WoyuYITR4fGtzCAKUbnwayHpJfqYvzlY9LmH6u-j_ZtstYmcX_jKcX3RBVbaXkVsAp4DkNAx3h2cgVjZ_gT8Mro791DqdR39NIdxBs6RNP-cpEpycRQIxn_L38auOGcIrczxHL3uGyAiK0T0s5vM3CqjUF144yrEe2O7SpBONw-THNzPjzhOlmNbQrod0LbC655R-TXljupEAQEb4rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: گروهی را دیدم به نام “همجنس‌گرایان حامی فلسطین”. خب بیایید یک روز آن‌ها را برای مذاکره به آنجا بفرستیم.
🔴
دیگر هرگز آن‌ها را نخواهید دید. آنجا کارهایی با آنها انجام می‌دهند که باورتان نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/150665" target="_blank">📅 09:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150664">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
یک نفتکش حامل نفت خام در تاریخ ۲ اکتبر و در فاصله حدود ۴ مایل دریایی از سواحل عمان، هدف یک پرتابه ناشناس قرار گرفت
🔴
تمامی اعضای خدمه در سلامت هستند و تاکنون هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/150664" target="_blank">📅 09:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150663">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وال استریت ژورنال:
عمان در گذشته به دلیل نگرانی از پذیرش خلبان عمانیِ حادثه فلای‌دبی به ایدئولوژی‌های افراطی، به خلبان عمانی ممنوعیت پرواز داده بود، این در حالی است که طبق گفته منابع آگاه، شرکت فلای‌ دبی او را استخدام کرد و به او اجازه داد خط هوایی شرکت را به تل‌آویب اداره کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/150663" target="_blank">📅 07:36 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150662">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj5MI4qgPn8x0EKiaOs-aLjPsSXSi6Y8muGlUmLHhFzAAh-akuvVRp22uMQ6mBFHNWSwHPGS3pnY5C4MbJnnxx8l9gaepRV3yDCwmkBKGZw6PT2faBglNgv2k-yTjEmFhky9C96acWBrg024IELqQ6F78ank50gw-tW0WkLAp_CnTc_o76uFltbp-juY-GLlAZjGpqxasdgSH_E7yyebl6SA2QNH2HIrIb5Ws6iV2yPWnM_Le2jJktLCBCD_idTxX9hzwDQVMBQIyjYfEfGJfgSvn6agYoT6w7OHTyWuXN7Iahr3etfYCLE6-zzCbPKsQEpAlg3BeOU4cWpbbbAVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس بریتانیا
: دو فرد ایرانی به طرح‌ریزی برای اقدام تروریستی علیه جامعه یهودیان در منچستر متهم شدند.
🔴
سلام احمدیان، ۳۶ ساله
🔴
رحمان صالحی، ۳۴ ساله
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150662" target="_blank">📅 07:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150661">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5-H-hd-QGtL_Nkrhm3dXzhzg554BBg6mgRaTbNkdmVXJmx_rKrNcH2ZWA5EBrQL7i75o7cvU4v5xwdPQ2fAFbnJaeHxBN3-v1_jLRwKBXGIuXfXjnRg8Xb3j3FQLkBwgX1UHMKUJXgAAIh6-eRit8G_pBnBOe2_bKo-_-X1BKd-g_RsSoLdm4zXCM_KNAT8eID8yLEe0ZNa5XbAthCyACCGGD4zwH7_PT-e8FExF2zvSkfkmTb0qv0TET3qSt4BJnKt0Aekz8OpYXK71R_Akw8_ShpGLMwaUBcpOx_IOdRLhS-kaWZVHwi44v46rGRwSLhcC4SR1F8jyAXy8cgVoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
قیمتارو شکوندیم!
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
مولتی هوشمند
لیت
|
۳۰٪ تخفیف
۳۵+ لوکیشن • ۱۳۰+ لینک پرسرعت • IP ثابت
▶️
یوتوب
و
ساندکلاد
بدون تبلیغات
🔥
فیلیمو، فیلم‌نت و نماوا رایگان
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کد تخفیف
:
LIT200K
اول رایگان تست کن، بعد انتخاب کن.
🔥
ربات تست رایگان و کانفیگ:
@
litvpn_bot
❤️
ربات مخصوص
همکاران
:
@litpanel_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/150661" target="_blank">📅 01:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150660">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYeIrpsbhE-Dzj9eWU-qpJbAqof9S05SzVZ5uFBzFwTHHOyEPfreIgUlQzw60vjgkF872rZ3sDYbUMTHgxNfolA6ve04Ifhfns1vWHFyC_-djDVB8UjXPI8Z2PbDB-UScAG5md5XZ27bTMzxTcDyWs4p5RP9JQ5_QVK9fJ-9z-XMCgXGujBG9xQ43lFcouuciq-m0SPB9zAGlKIEmqbV9Nj-WOTPPz5AbCoKsz3tbIUmnG-gM_80sfMgRI-dVIIXGGncrsXwU_7jtASyPy-EMUOKLvpUXkhfMA3g9vee2egNecKA64q8bqWCTXzcwlYLny83T2AI2051VPqRKNqvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: رقابت سنگینی بین ایران و آمریکا سر ابرقدرتی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/150660" target="_blank">📅 01:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150659">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh0enwkGteTRXqYNApPvrekoWGr8ivM-TpvYwYkHERRVKDi64J7RiOj6vPey7D6bCzDKxr5wnRX6RoLxIXbio5c-0zxLd2FOdwTFRRFpLfJbGU5lq0VxxADh3KvPtwNbHLjWiWjP1czE9mXbUaPjdljy5Qbv2J4CoTPW5FLAqld-aW1yGxgdbhOa02T_64k5M_8wixPSZEdSWaHtjndZPbupbxeVGJu27B7juKaK2l9UQbJscMRp1lNUazDCpL-32-endOMtRoSJ1UCAbRVqIZgQ_QgZXF74WJofhSkE5GdYnfC5C98bL3VCyzwr69fUcECoZ9tqz44LS9f-cLPtwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سایت رسمی استارلینک نحوه عملکرد استارلینک موبایل رو توضیح داده و گفته ماهواره‌ها بعنوان دکل عمل میکنن و هیچ نیازی به دکل زمینی یا تجهیزات اضافه نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/150659" target="_blank">📅 01:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150658">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nitXKnffdoNJTJdMpeBf1_2ZpH_RAGIncqX01vGWtOfvMBcxh-oKxFVmI8hSADwTMtu0h8au48ugA-TEwIGY-tEKb4-LK3Xz9lxgTF4TZkHkCqlDu6z6rd5VlakqhuI3EsOppShd2KCVUVMvukOopvdRtBEju3WBvSatIp_FkSOt611tBphjpck-YA-Fye4A2EsTsMRgU8bQWoSHezDSiyQlU0teTCbRe5tIHuNvC-g8Gn-rAT_6XvajKfStqkIGfaUuxwcerKrghpp8w-oQX54KcJ31GpapLol62-z1qPGB0kB5CUUdcjdgzgej8Z6-RS_ZgjCKfONnv__CzeOMlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور فیلد مارشال: ‏آرایش‌ها و آمادگی‌ها برای رسیدن به لحظه تصمیم در حال انجام است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/150658" target="_blank">📅 00:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150657">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0eda5713.mp4?token=jdR__FETobKRVnR4-XpyMaDdwxpCvGQEzfvjep939_lUm37XvjxfY4z6jzvXtEIO6LWoCJoRY-4cIRLYqC6dOJsZqVcidnqiEcrOVl3rqIykwdMpd9IG5KBBe9tAJgXl1_P6yY_OuBN8fA7eioE8smhijZvkMiI80AdtN4zSsD3uGaUIVUM9-ha1m0ENL4Fh2svmbKHNAHXQD0Ucsrmkpm2cGPKQUjBjv_axSFv557FYLGaBMu5QfBSmjDd8ARqy4dbryz5nTH4mtKDs2Y6tPU9ZmJ8ifur5pJ4TMqxSYhXXw9mGawETaRsh2R9W-sVDacDwMtDscDhwnsyjKrHxIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0eda5713.mp4?token=jdR__FETobKRVnR4-XpyMaDdwxpCvGQEzfvjep939_lUm37XvjxfY4z6jzvXtEIO6LWoCJoRY-4cIRLYqC6dOJsZqVcidnqiEcrOVl3rqIykwdMpd9IG5KBBe9tAJgXl1_P6yY_OuBN8fA7eioE8smhijZvkMiI80AdtN4zSsD3uGaUIVUM9-ha1m0ENL4Fh2svmbKHNAHXQD0Ucsrmkpm2cGPKQUjBjv_axSFv557FYLGaBMu5QfBSmjDd8ARqy4dbryz5nTH4mtKDs2Y6tPU9ZmJ8ifur5pJ4TMqxSYhXXw9mGawETaRsh2R9W-sVDacDwMtDscDhwnsyjKrHxIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس تلویزیون:‌ حتی اگر بمب اتم بخوریم باز هم تسلیم نمیشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/150657" target="_blank">📅 00:33 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150656">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d0d925a5.mp4?token=ELHS3zv87jLwm9u61xACB1mPYOym8jcuhixZxiezjDLfqkX0SGTEEJiiVeDNyEdGTSe5jambkTVY5CJtTV3jvQ4-ylxfZfvFapTBvNNQ8OtdojqoprIIc-OPH1cJtUCg56d-NhbI0ndghMId1T6h8tTZsZ8PKEtkdoBY1_KhxuhSnXPWaYWCnOEvLV1WlHMUPZgPqSKU2QIIfLUHpiQR-qFZe8RJXywfO0XCat9Jhf1dXFNfgVmiJPZ_eQsKEJAPWBBwqdJAmqzNE0FaQmLu0U-HMsLel9MlFr7oAB_LY5w_Rzvkng5zM9t_X2w8on3K81MNQYxYhuru529KRNzMIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d0d925a5.mp4?token=ELHS3zv87jLwm9u61xACB1mPYOym8jcuhixZxiezjDLfqkX0SGTEEJiiVeDNyEdGTSe5jambkTVY5CJtTV3jvQ4-ylxfZfvFapTBvNNQ8OtdojqoprIIc-OPH1cJtUCg56d-NhbI0ndghMId1T6h8tTZsZ8PKEtkdoBY1_KhxuhSnXPWaYWCnOEvLV1WlHMUPZgPqSKU2QIIfLUHpiQR-qFZe8RJXywfO0XCat9Jhf1dXFNfgVmiJPZ_eQsKEJAPWBBwqdJAmqzNE0FaQmLu0U-HMsLel9MlFr7oAB_LY5w_Rzvkng5zM9t_X2w8on3K81MNQYxYhuru529KRNzMIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اینجوریمو نگاه نکنید من همرو دوست دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/150656" target="_blank">📅 00:27 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150653">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20b902b1bd.mp4?token=SGWVMOSWBl-OZ217HeliPXTT9BBRszIkrazFEu7AWXHEcj6Pdq3YlB-58t6f5xU6TjwPjpIosOqHt8_0OTIrKKPTUdjhQm_QofAvOTQdw9WCtAEeNCo588sQFm5elm5B3JRFOwxP695h-pGWcPUZE-_AcVlr19wzyFPuLJQ3OtOT-3sxOtB9R1zXe0bzT1ow9tqF7aOCogyMTYekaUlhIoDiqBxMck0t4YWx2jIBfM3wZNMOmI8iBSbtSLOXZzn9xoh5hMzsTjrt8TLK01wep4JkBNMqi3oJPEwOPiDDcquOrdO8ZZ2Qzawffc2cBLrInfaSl75WfyhFA0BEu1lPCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20b902b1bd.mp4?token=SGWVMOSWBl-OZ217HeliPXTT9BBRszIkrazFEu7AWXHEcj6Pdq3YlB-58t6f5xU6TjwPjpIosOqHt8_0OTIrKKPTUdjhQm_QofAvOTQdw9WCtAEeNCo588sQFm5elm5B3JRFOwxP695h-pGWcPUZE-_AcVlr19wzyFPuLJQ3OtOT-3sxOtB9R1zXe0bzT1ow9tqF7aOCogyMTYekaUlhIoDiqBxMck0t4YWx2jIBfM3wZNMOmI8iBSbtSLOXZzn9xoh5hMzsTjrt8TLK01wep4JkBNMqi3oJPEwOPiDDcquOrdO8ZZ2Qzawffc2cBLrInfaSl75WfyhFA0BEu1lPCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش کصشر و بی ربط فرمانده کل پدافند غیرعامل کشور به بستن ساعت هوشمند
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/alonews/150653" target="_blank">📅 00:19 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150651">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=YNSxgPq0iLGKSWgBld7z3h0BWHK9kdLIdolcA4THcsWaD8zIUCvrn9SN4o12DYoGo-LOdSj6xTNnrhsKasgT9W7RrDdd246TzlHEvEx5e5KEuXQy4uNLhA9NIeAeBWDdGgwBwK2HhXSiUrhUVH6ii7HM1OrPFflV-dYjSyrP2RvJl4vWs6PxZEMWy7GGcRK8lE_5f3k5FxNdVBmFoAe8PmUtZZd5oQICC9iO_O6Qh82H69p2fMRNDubg6VCqxfueTbQwAzYSmOS9RJgXfS-gzj80t0yU0nThkqQozDK38sCpI04tPVTBRrr56WP6mq8NZWFZW_ScJX3_ffN-jTWCkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b49a7f3128.mp4?token=YNSxgPq0iLGKSWgBld7z3h0BWHK9kdLIdolcA4THcsWaD8zIUCvrn9SN4o12DYoGo-LOdSj6xTNnrhsKasgT9W7RrDdd246TzlHEvEx5e5KEuXQy4uNLhA9NIeAeBWDdGgwBwK2HhXSiUrhUVH6ii7HM1OrPFflV-dYjSyrP2RvJl4vWs6PxZEMWy7GGcRK8lE_5f3k5FxNdVBmFoAe8PmUtZZd5oQICC9iO_O6Qh82H69p2fMRNDubg6VCqxfueTbQwAzYSmOS9RJgXfS-gzj80t0yU0nThkqQozDK38sCpI04tPVTBRrr56WP6mq8NZWFZW_ScJX3_ffN-jTWCkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : قدم بعدیت در مورد ایران چیه؟
🔴
ترامپ: خب، اگه اینو بهت بگم به اونوقت تو یه خبر مهم بدست میاری، درسته ؟پس نمیگم اما خواهید دید که چه خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/150651" target="_blank">📅 00:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150650">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ: اروپا بیشتر از اکثر کشورها به دیزل وابسته است و سهم قابل توجهی داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/alonews/150650" target="_blank">📅 23:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150649">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / خبرگزاری فرانسه: پلیس بریتانیا دو ایرانی را به برنامه‌ریزی برای انجام یک اقدام علیه جامعه یهودیان در منچستر متهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/150649" target="_blank">📅 23:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150648">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دونالد ترامپ درباره ترکیه: من عاشق ترکیه‌ام. همیشه رئیس‌جمهور اردوغان را خوشحال خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/alonews/150648" target="_blank">📅 23:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150647">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بلومبرگ: ف‌بی‌آی و گارد ساحلی آمریکا در حال بررسی حمله سایبری به یک ابرنفتکش در نزدیکی سواحل تگزاس هستند.
🔴
هنوز مشخص نیست هکرها چه مدت به این سیستم دسترسی داشته‌اند و با استفاده از آن قادر به کنترل چه بخش‌هایی از کشتی بوده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/150647" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150646">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: ما روابط بسیار خوبی با اروپا داریم و آنها آماده همکاری هستند، زیرا حجم زیادی از سوخت دیزل در اختیار دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/alonews/150646" target="_blank">📅 23:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150645">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ: مسئله إيران به زودی حل خواهد شد و قیمت نفت کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/150645" target="_blank">📅 23:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150644">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ترامپ: به محض اینکه جنگ با إيران به پایان برسد، قیمت نفت به سطحی پایین‌تر از سطح قبل از جنگ، و احتمالاً حتی پایین‌تر از آن، کاهش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/150644" target="_blank">📅 23:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150643">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ: اروپا مقادیر زیادی دیزل دارد و سهم قابل توجهی در بازار جهانی و همچنین ایالات متحده خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/150643" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ: ایران در شرایط دشواری قرار دارد.
🔴
ایران در وضعیت خوبی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150642" target="_blank">📅 23:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150641">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b51715eb64.mp4?token=jrJqUcBIeZtfw3_URFQ3UeGET2HFcVrhbJHpFY9iRUlhyKnkEkX2sd0nPcP6O6xyrIj4sSDsgubfxoPRXxwEyYuMEFsXfvH-Va35agkGvXVHUcarv5vM_e3MZY2dtqQ3Yra-MOeQ8yA1Ow5FseCMlUyDhh0MgZORDJcoUmxHfh_8yL4ArapoFme3m9LDsh30joCLCks1wzosTrneuUk7tVe_cuOk3VjTqsUaMJb2ah_whp1bt0oQssClO7HIsKy7BayKdiA8FBV-oJuf87ZlLMcI-jO2Gv7pqC2AvgL3XMEE_fWr5laLFoDQ_r5OJjg3VrrfgbaW_vRq9ni8FtfUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b51715eb64.mp4?token=jrJqUcBIeZtfw3_URFQ3UeGET2HFcVrhbJHpFY9iRUlhyKnkEkX2sd0nPcP6O6xyrIj4sSDsgubfxoPRXxwEyYuMEFsXfvH-Va35agkGvXVHUcarv5vM_e3MZY2dtqQ3Yra-MOeQ8yA1Ow5FseCMlUyDhh0MgZORDJcoUmxHfh_8yL4ArapoFme3m9LDsh30joCLCks1wzosTrneuUk7tVe_cuOk3VjTqsUaMJb2ah_whp1bt0oQssClO7HIsKy7BayKdiA8FBV-oJuf87ZlLMcI-jO2Gv7pqC2AvgL3XMEE_fWr5laLFoDQ_r5OJjg3VrrfgbaW_vRq9ni8FtfUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موج کودتای صهیونی در فرانسه به دانشگاه‌ها نیز رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/150641" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150640">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
کارشناس صداوسیما: افزایش قیمت ارز و دلار ناشی از هیجانات بازاره و قیمت واقعیش این نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/150640" target="_blank">📅 23:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150639">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ایهود باراک :  نتانیاهو برای عقب‌انداختن انتخابات، زمینه جنگ تازه را فراهم می‌کند
🔴
ایهود باراک، نخست‌وزیر پیشین اسرائیل، مدعی شد بنیامین نتانیاهو در حال فراهم‌کردن زمینه ورود به جنگی تازه است.
🔴
به گفته باراک، چنین جنگی می‌تواند به تعویق برگزاری انتخابات منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/150639" target="_blank">📅 23:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150638">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOWC6Ih94oohBpNlpXHR9NCMwq9-lhLFYiyDWuzSZ1P-OWL7DKseWgcSBFCXSZ7LwI1tncl26Helhh1Hgm3vRUgiLuYlFlq90eIbn-BnbZ-75g6oqe1Omn_A2QkSfIGnUfiVg0o-oTVrFcUSGrUq1YqLNtLWsymfshwcFSGQnYJd3K2A5oKFuRcwl_ziQKcFqGGbievsTq715wDsyGp3FgILgUIVjz3gPww5Oma4_KV91FuQSJyLAardncAirewAbV9HHQKcUXC1c-MjfFvxscfrXa_kPzEn-RLiM7SMY3yTqi7wV_oK8vouY0bRYtD__QDrgQeY4_wLerEtuA1MHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آمریکایی: بنا به گزارش مقامات آمریکایی، ترامپ پس از انتخابات میان‌دوره‌ای در حال بررسی «اعزام نیرو» به ایران است، زیرا احساس می‌کند «چیزی برای از دست دادن ندارد»
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/150638" target="_blank">📅 23:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150637">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pktCtAIKXwYbTpe8acDd5ce3Zv83GAmNI7k5teDiNn4HfbwJO4KRgc96fvsWm9s17KVblE1GO0P2oHy4XuiE7O-y4r5bz9ZP3YiTmk4N8rZUPoXlbaBjfC4f63Fbs5dxpb2G_acRKgz8B5XJ4Skmtpz_8XUgR3JxThOSTvnorHaKvAebZzGCRoYRn1kgphobuS4agk-TjkB9DhVUyCiSKmE1QFW2d64ojHa_xv8aHwVnuAt53kAv3oTDwfExV5VZNQ09Y3iD6sEz4yffbi6TRKua1M-j81Cz25hvYOCyr-gG25KWZYAK9XflAe8sZuaBfVhQpEXTjrWXyLuMFoSLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در تجمعات شبانه امت معکوس مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/150637" target="_blank">📅 22:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150636">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8uqx5yZpyNTShTnlewd2ww89TpRN7vLevXr7f_fp9CRugQyskJ_lJSFyUSH4GgHmf9aM5mOiIwx1YFxepB3f3j_fPO8fqnPxxRzFR3ExbwbrDwYWNvsJ-MqP06_wDUiZgnzsjCXnN6S3Uonj1VKYxnglRBrfuFsh1k3ZMx5XNG40Ae0M8hvZ5yo_CZT2NRD63BGccjy1t6mIleAzsCkl_d1504ClwCVaDQOJY9mQqGvbWldOsZ2BYXxen2y41YfMyKcgF_VtwS4P5QjjXkp7Uy7o-vVg5YEok0mmYH8XB8VWcVokFpuMsPsWZvgCiJchEkPOHNYUwUP0tLJwi3IAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت ترافیک هوایی در فرودگاه ریاض اکنون متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/150636" target="_blank">📅 22:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150635">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رویترز: مقام‌های اسرائیلی قرار است از کمک‌خلبان پرواز فلای‌دوبی بازجویی کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/150635" target="_blank">📅 22:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150634">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
طبق گزارش وال استریت ژورنال، سازمان هوانوردی فدرال (FAA) اعلام کرده است که نقص نرم‌افزاری جدیدی که بر هواپیماهای بوئینگ 737 MAX تأثیر می‌گذارد، خطری برای ایمنی پرواز ایجاد نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/150634" target="_blank">📅 22:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150633">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
فارس: ترامپ به دنبال انجام کودتایی دیگه در ایرانه ولی الان خیابون‌ها دیگه دست تروریست‌ها نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/150633" target="_blank">📅 22:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150632">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بیانیه جدید آمریکا و تروئیکای اروپایی
‏
🔴
آمریکا، انگلیس، فرانسه و آلمان با صدور بیانیه‌ای اعلام کردند متعهد به جلوگیری از تأمین هرگونه مواد یا فناوری برای ایران هستند که ممکن است در فعالیت‌های هسته‌ای مورد استفاده قرار گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/150632" target="_blank">📅 22:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150631">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qduw32hOsej-rSNh2c9SQTFhEl1iuyQmMfDVCkI9LRYZBy2l3Fqm4YQj4SMcT88H5FKNoH3Nn-2JxMXSerzpPKRNfjN62I762hD846CGJi-0hoS2bMcz59Bqd4wLAOgTX0DBD0pdI1e2Or-2rMpXCeY7nbfwXmJrY6dZ6gsRZfzZH4V43TBl6mzw8mBnBtQC8exmK7cf0USTBPnLKz7AWeBKxrRGvYfS-N5QekThdD0443ocPCf3Tykc1S4odaD3pv7fHYLhD6dKXdfe3rQSbmosTw7PUyXXs1YGzs5nobpzHWoyyq6tjj7xnZliHVdRrbsrgfAdRM7mG7vJJUAsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایتالیا اخطاریه‌ای در مورد سفر به اریتره برای شهروندان این کشور صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/alonews/150631" target="_blank">📅 22:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150630">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آسوشیتدپرس: شواهدی از ارتباط ایران با پرواز فلای‌دوبی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/150630" target="_blank">📅 21:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150629">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز: عربستان سعودی بیش از 100 هزار نیروی نظامی را برای حمله تمام عیار به حوثی ها بسیج می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/150629" target="_blank">📅 21:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150628">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKzW4XsysN0B0nOFLfSbfivD__d7u3rr3rtkwWBsv1tmn0UAq8y1JTy4GB6kL2w7eBl8e5TWtY64VjYEuqj-MNPBu2GI-27lk6eRUh1wroH4UmdR0ZTHBrqWXIDujU4fsWbM7wcXMY3aJu4Hca11rYgD6qIjuQSB5qb9hdZAQjJ8M39bUegz8_ezbNedja0CNg4CsbJA6NvDAipyTKzftY4fo5PlKb1LPAi_Q3D5Q0qLzkuqs986U0wesWGmEIdz68osVOPYhEczgqpJhjn9EQ7XqZ3PpkF_GuH5WxgRbMN5AsHYOQBr7A83XdEy1JTHFiCtirqbRjAYoffrfztvjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/معین خواننده مطرح اعلام کرد بزودی به ایران بازخواهد گشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/150628" target="_blank">📅 21:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150627">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=ZZK-g8G-95Fwx8-2f2auOBPwL2VWdtYjU9BvogrKiOkCBYl0ZUa_hgBenw_j7mRFzuhxNtIDa9sv3TqyoEJjAjJkGqPbkW7HJReFOgDjlgsl4TKE7xqMiym8XJauIL8wJ3MFEQAcqAI4TJIwg-QlMtWN2rk7JjnC5SH6Mw3LWu31X-R9WADZqfhmmZXZGFFBs7DXtRkDQtbljWX7PPbZ3_HjPBrkiTHrlqUXmEsRAtGo81LjWaEyxNLpw1vUd2bBR6mJaIExl1CopkePN1PHhUUyCDSQL2ht2xEPvcQiAcnFXavwELxR4fWFm4yMds8_J0q8NQng452AO1ce4jMfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e221ca09.mp4?token=ZZK-g8G-95Fwx8-2f2auOBPwL2VWdtYjU9BvogrKiOkCBYl0ZUa_hgBenw_j7mRFzuhxNtIDa9sv3TqyoEJjAjJkGqPbkW7HJReFOgDjlgsl4TKE7xqMiym8XJauIL8wJ3MFEQAcqAI4TJIwg-QlMtWN2rk7JjnC5SH6Mw3LWu31X-R9WADZqfhmmZXZGFFBs7DXtRkDQtbljWX7PPbZ3_HjPBrkiTHrlqUXmEsRAtGo81LjWaEyxNLpw1vUd2bBR6mJaIExl1CopkePN1PHhUUyCDSQL2ht2xEPvcQiAcnFXavwELxR4fWFm4yMds8_J0q8NQng452AO1ce4jMfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/150627" target="_blank">📅 21:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150626">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6527247c0.mp4?token=aO8h5TZ3-R8lS69wxZSw5S45YXtnwLUUSt8VslwsugnO7hjqzhGutwC4fIiVvvpeqE65jQCPnQ2W9FxNm4t5H8KULjWw9yLSMBXqlz45Io7hSfTV9DLcORxqvBTLv1NIxUZeWexESw0NQwifMhweJd2V_IOmat8k55DrE3-B0QrSU2yGZ3gzeNIwGKQyf3c_xp6QaJCw3oWI_VSgtk3m327s7VMuVpNGhQ_96V5kEOj6x4uE22EtBaDmb-N0W77q_vjD-GKSfr7l-obVSGBXEBtrB-2D3YoMzLcToUPoVDQFy0abhmpYglYT1RqmCYe_o8zGcQd6D5o33f2F476ztUsbSAGuI7V7dSF2ftasWparOFuTrqxyB1_wavw8kLIS372D-saRdvjd0STzGZJ7oJ6uc6LxIZbRvAv2CU1g2g0PBmDBcJtVbpmSD-RujegF7C1DoRv9UCFuSHfOLi2E010s1uAJAvtiisMW7-qV7Drd0MWRT4B1e3ZK0Gy1KRTDmJpMtnJas3OX77eCZ_NH4b-Ltf8zE4V8e7Fr2rab3CSsVpUE1h8BQngNPWjjBw9lE_Oysv5OssQuVE_6qKWTABeiGBLl78Ctp52j_SL6I1VfuWjYqxSDJz74mwW126gqKHv54y3JsyyuWMlAT-3MRERBeMohYzVLiRsdW2B554w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6527247c0.mp4?token=aO8h5TZ3-R8lS69wxZSw5S45YXtnwLUUSt8VslwsugnO7hjqzhGutwC4fIiVvvpeqE65jQCPnQ2W9FxNm4t5H8KULjWw9yLSMBXqlz45Io7hSfTV9DLcORxqvBTLv1NIxUZeWexESw0NQwifMhweJd2V_IOmat8k55DrE3-B0QrSU2yGZ3gzeNIwGKQyf3c_xp6QaJCw3oWI_VSgtk3m327s7VMuVpNGhQ_96V5kEOj6x4uE22EtBaDmb-N0W77q_vjD-GKSfr7l-obVSGBXEBtrB-2D3YoMzLcToUPoVDQFy0abhmpYglYT1RqmCYe_o8zGcQd6D5o33f2F476ztUsbSAGuI7V7dSF2ftasWparOFuTrqxyB1_wavw8kLIS372D-saRdvjd0STzGZJ7oJ6uc6LxIZbRvAv2CU1g2g0PBmDBcJtVbpmSD-RujegF7C1DoRv9UCFuSHfOLi2E010s1uAJAvtiisMW7-qV7Drd0MWRT4B1e3ZK0Gy1KRTDmJpMtnJas3OX77eCZ_NH4b-Ltf8zE4V8e7Fr2rab3CSsVpUE1h8BQngNPWjjBw9lE_Oysv5OssQuVE_6qKWTABeiGBLl78Ctp52j_SL6I1VfuWjYqxSDJz74mwW126gqKHv54y3JsyyuWMlAT-3MRERBeMohYzVLiRsdW2B554w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مکرون: آمار بشکه‌های نفتی که امروز از تنگه هرمز خارج می‌شوند، در روزهای اخیر بهبود یافته است و اکنون، در مجموعِ مسیر هرمز و مسیر یَنبُع به دریای سرخ، کمی بیش از سه‌چهارمِ حجم صادراتیِ پیش از جنگ در حال صادر شدن است.
🔴
اوضاع در حال بازگشایی است، همه با عزمی جدی در حال اقدام هستند و ما از احیای آزادی کشتیرانی حمایت می‌کنیم‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/alonews/150626" target="_blank">📅 21:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150625">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a60b7a2.mp4?token=KfFhdIHlD6N4Wi1W-GO2kJLnyC_3LDAviSouHeHUHuCBomCfQHHsXYM4HTJKishKICbSO2ArGLKxieMtyf2NjAjBTx7OCwopbI_TrAVUA-C6tk4QqRLacdFUwBtMxxbyHoIz3nRxwhuOKVKgpI-aX9pg0XRQdkUa89Gg9BJWmZP_fnoCYIVz_4X45qtH0IDGDctwzRJgJUIY3SVTqXMtgeg7lSu2pSAySVBsLMt6UR_cU0ycViUJAZDDGG6NJfZNbt3f7NfXrzKGxmDU-r_0P9PKABFZOpdEG3-tF3TvsQQhd7wyUIdrebO4djO4g9jj6tWQPYxU_FvOJ08mTdfIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a60b7a2.mp4?token=KfFhdIHlD6N4Wi1W-GO2kJLnyC_3LDAviSouHeHUHuCBomCfQHHsXYM4HTJKishKICbSO2ArGLKxieMtyf2NjAjBTx7OCwopbI_TrAVUA-C6tk4QqRLacdFUwBtMxxbyHoIz3nRxwhuOKVKgpI-aX9pg0XRQdkUa89Gg9BJWmZP_fnoCYIVz_4X45qtH0IDGDctwzRJgJUIY3SVTqXMtgeg7lSu2pSAySVBsLMt6UR_cU0ycViUJAZDDGG6NJfZNbt3f7NfXrzKGxmDU-r_0P9PKABFZOpdEG3-tF3TvsQQhd7wyUIdrebO4djO4g9jj6tWQPYxU_FvOJ08mTdfIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: ناو آمریکایی آنچنان از ترس موشک ما فرار کرد که چند هواپیمایش تو دریا افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/150625" target="_blank">📅 21:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150624">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز: عربستان سعودی برای یک حمله زمینی تمام عیار به حوثی های یمن در هفته های آینده آماده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/alonews/150624" target="_blank">📅 21:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150623">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز: عربستان سعودی برای یک حمله زمینی تمام عیار به حوثی های یمن در هفته های آینده آماده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/150623" target="_blank">📅 20:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150622">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رویترز : ایالات متحده یک آزمایش انفجاری شیمیایی غیرهسته‌ای زیرزمینی در سایت امنیت ملی نوادا انجام داد تا تشخیص انفجارهای هسته‌ای کم‌بازده را بهبود بخشد.
🔴
این آزمایش بر شناسایی انفجارهای «جداشده» (Decoupled) متمرکز بود که شناسایی آن‌ها از طریق پایش لرزه‌ای دشوارتر است. واشینگتن چین را متهم کرده است که چنین آزمایش مخفیانه ای را در سال ۲۰۲۰ انجام داده است، ادعایی که پکن آن را رد می‌کند.
🔴
داده‌های حاصل از این آزمایش برای بهبود مدل‌های علمی و الگوریتم‌های تشخیص انفجار هسته‌ای استفاده خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/150622" target="_blank">📅 20:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150621">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: نمی‌خواهیم درباره احتمال دست داشتن ایران در حادثه هواپیمای فلای‌دبی، پیش از پایان تحقیقات اظهارنظر کنیم
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/150621" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150620">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRXKExQ2nAtSGdYWAck-wY5aIWcP5UfVfXd0oU3gHEI8xikVoEZ99ue_FMmDFpA7C7BeQEC6UZKNxzr-j0vUbwL2TWZTKsuPOrsLjb5xE9wfMYNXDkt_BVHeVBLNvoVQhU3qmzR6HG2IJt7agdfaMIbvZ_GPAlBUWIPCUMpb3M9d-1xK-wAW3Hjr2yU2B2Vk8YF8XNu-H4c52C3RNWZbgbDMxgJFJm86MO6-aHhQm5g882CYOgvjHY-hsNR9KpRKsAGK2cWLpUhZYhkWT3np7eIBAV1moGSFdqap9bHdJwnEhVOXkyBWUYxC49YwXhfCzHNlYiYuwdwFOTQGsEJHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مغازه در بازار سنندج
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/150620" target="_blank">📅 20:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150619">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
المیادین: ارتش یمن کنترل رشته‌کوه راهبردی راسن در استان تعز را به دست گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/150619" target="_blank">📅 20:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150618">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLDmFA2aopBPaf6e6NajU8FTJ_uAs-t_bHNdgeyEfDwdzdt0AgtBciJgt1ThrB00mO6qiiftluBeBUct8g2Bag-5qdoij8ayrp0H9FuPuwg9KzZQenZtAhU1C17CmymWYj5ShnyQ6MYgDPbDGkr2zA_WQO_ZjkFe75ZXxFTzIwAgU_zr6lx8nimpJwAiknnIJ5NUvprB9oUmMvsD1YyfBzuhoDylPDnho3ZD6RAmlAb-73Uduh8b8IqnJND5GcmhxQ0_GXlleI6H_8cW0F9E0uEBn1te78ygNcwuRfAf2ic8U7YFrEm8KuDvv-z6ilGKBrC3IglrJIW9JWJt6GoUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکانت مشاور قالیباف: تازه ترین اطلاعات نشان می دهد عربستان و امارات نقش جدی در به بن بست رسیدن مذاکرات 10 روز گذشته ایران و امریکا داشته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/150618" target="_blank">📅 20:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150617">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بریتانیا: تحریم‌های هسته‌ای سازمان ملل علیه ایران همچنان پابرجاست
🔴
بریتانیا می‌گوید با وجود پایان فعالیت هیئت کارشناسان سازمان ملل درباره ایران، تحریم‌های مرتبط با برنامه هسته‌ای همچنان برای همه کشورهای عضو الزام‌آور است.
🔴
لندن همچنین ایران را به «همکاری ناکافی با آژانس» متهم کرد و گفت پایان مأموریت هیئت کارشناسان، نظارت بر اجرای تحریم‌ها و تلاش برای دور زدن آن‌ها را دشوارتر می‌کند.
🔴
نماینده بریتانیا در سازمان ملل نیز مدعی شد ایران بیش از ۴۰۰ کیلوگرم اورانیوم با غنای ۶۰ درصد در اختیار دارد و آژانس قادر به تأیید میزان و محل این ذخایر نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/150617" target="_blank">📅 20:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نیرو زمینی سپاه : با جعبه مهمات‌های آمریکایی برای سربازاشون تابوت ساختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/150616" target="_blank">📅 20:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150615">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: نمی‌خواهیم درباره احتمال دست داشتن ایران در حادثه هواپیمای فلای‌دبی، پیش از پایان تحقیقات اظهارنظر کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/150615" target="_blank">📅 19:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
رئیس مرکز ارتباطات مجلس: مجلس نه تنها هفت ماه بلکه یک روز هم تعطیل نبوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/150614" target="_blank">📅 19:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150613">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgiS3QBNqp1vMOT7A3WY0tNXdqdcXhEvqiFAGMKSoI3QwOgEqswzz4zF_lzzgE84_JwASMNYm6mKPCTb4p4MxXlNyBMqX15rU0prHvkv8yUq7i94nC6vRfWTJOIXsMOy9-epJqlR14eruQjSqaRGkpbcnoraiDhpWVcPYinw9jZXec5O2gCj3goiideHANckm0dW36m7z_6JRM6JcX8cdqgLMCBzGHShzDUH8FAc4dzQi2PfxPqGXcFcrihWukdmI_E7rcZHz3bNeFZlCERydoeTK_1SSinboYW9wcWtlXf6jcOKkCWtBoq9OaJXoc4kl4UQRCnau8mjviC-HT7_dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: تنها شخص دلسوز و راست گوی مجلس الان تو زندونه (رسایی)
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/150613" target="_blank">📅 19:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150612">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
طبق گفته مقامات غربی و منطقه‌ای، عربستان سعودی برنامه‌ریزی می‌کند تا به حوثی‌ها حمله کند تا کنترل تنگه باب‌المندب را از دست آن‌ها بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/alonews/150612" target="_blank">📅 19:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150611">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دیدار فؤاد حسین وزیر خارجه عراق با وزیر خزانه‌داری آمریکا؛ ایران و خلع سلاح گروه‌های مسلح محور گفت‌وگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/150611" target="_blank">📅 19:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150610">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش هنگام خروج از تنگه هرمز بر اثر اصابت یک پرتابه ناشناس آسیب دید.
🔴
این حادثه باعث وقوع آتش‌سوزی محدود و قطع برق در داخل کشتی شد.
🔴
آتش‌سوزی مهار شده و کشتی به مسیر خود ادامه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/150610" target="_blank">📅 19:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150609">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وکیل: الناز شاکر دوست به یک سال حبس تعزیری و محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد
🔴
پ.ن : الناز شاکردوست به علت انتشار استوری حمایتی از وقایع ۱۸ و ۱۹ دی به یکسال حبس تعزیری و دوسال محرومیت بازیگری، محکوم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/150609" target="_blank">📅 19:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150608">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بیانیه دولت عراق: برای انجام روزانه ۴۰ پرواز از مبدأ و به مقصد فرودگاه نجف توسط شرکت‌های هواپیمایی ایرانی، به‌جز ماهان، معافیت دریافت کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/150608" target="_blank">📅 19:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150607">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر خارجه عراق: بغداد آماده میانجیگری میان آمریکا و ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/150607" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150606">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ظریف: روس‌ها نه فرشته نجات ایران هستند و نه دشمن، «شریک ارزان» شرق نشویم
🔴
محمدجواد ظریف: «ایران نباید تمام تخم‌مرغ‌های سیاست خارجی‌اش را در سبد یک قدرت بگذارد.»
🔴
«چین و روسیه باید انتخاب راهبردی ایران باشند، نه نتیجه ناچاری و بسته بودن راه‌های غرب.»
🔴
«وابستگی یک‌طرفه، قدرت چانه‌زنی ایران را کاهش می‌دهد و کشور را به «شریک ارزان» تبدیل می‌کند.»
🔴
«روس‌ها نه فرشته نجات ایران هستند و نه دشمن؛ مسکو هم مثل هر قدرت دیگری منافع خودش را دنبال می‌کند.»
🔴
«ایران زمانی در برابر شرق قدرت چانه‌زنی دارد که گزینه‌های متنوع سیاسی و اقتصادی در اختیار داشته باشد.»
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/150606" target="_blank">📅 18:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150605">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nrdl1qJc0zORT0Z1aO51WpR_So3gE1m4BXMFyVOmD_KaP2gQgfopqVfGKIj1hrNAb2B_FCXJVenyne198PuyITMHToT_e94h4xpHX3tCy79VTjuD9dICAfMXgOtXlEnvvaXP1esRb2Zu3dBSDpjAbhEv6ite6wzAmbdJt1tEmPrM2Er2nicbkvWX9yhaOWeIW4GzNtygh9QO8yeaSr1oDJGEcf0a6uWNg4Ri6T5iGwBkK3NNFgVFl7Vt58bv1AxmSRoH6g-P4zKsj7OfBuOzdArP66V8XY7JCLeI7VM9qb3tt8UKz-Q7F0hrK8r1u8fmA-ACOzSJ5WiDtPsoVTlsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: ترامپ متوهمه و تو عالم خودش خیال میکنه پیروز شده اما واقعا برعکسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/150605" target="_blank">📅 18:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150604">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnttKbbEf-msLIidQbO7DdtAVA1gTGxxFXbn81PC4tUsdpbYV5K6cFyPDKAtJoRq_eSq3249aR9-axFSM_WMHrx_WxrVI9HiKd9lmemzMGjivfNPgo5FaHNYYcY7IMCohOxaNRM48uXYuHP3JwU3OFFrtgzymtcTfGjF_90ikgljJ86dHb9EzN7SsBfRq1L-zrDlrWYYs5NkQs9W6MNxJZIfDMtNEAe6nYCDKQNw6yauXCfT2Uzjj4U2Z7L20uAirBRWtivU6f_YLn-Le1okZe6QEc9f4FZ0d_9gjR5o7etlBSdq_F3l-_sQ7YlGr6y2CalfpAAKE-qiGJVaYfrUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امضاهای کارزار درخواست ابطال اعتبارنامه رسایی از ۷ هزار گذشت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/150604" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150603">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خانعلی زاده: عراقچی آن‌قدر در نیویورک ماند تا نهایتا با دستور مارکو روبیو، او را اخراج کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/150603" target="_blank">📅 18:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150602">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
مدیرعامل فلای دبی: به درخواست مقامات، پروازهای خود به تل آویو را موقتاً تا اطلاع ثانوی به حالت تعلیق درآورده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/150602" target="_blank">📅 18:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
مکرون: گروه 7 قصد دارد ظرف چهار ماه تا 100 میلیون بشکه گازوئیل و نفت خام آزاد کند.
🔴
گروه 7: در 20 روز اول، عرضه گازوئیل از سوی این گروه و شرکایش به میزان زیاد و زودهنگام افزایش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/150601" target="_blank">📅 18:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
آکسیوس: دیپلماسی ایران و آمریکا همچنان در بن‌بست است
🔴
به گزارش آکسیوس، مذاکرات ایران و آمریکا همچنان با بن‌بست روبه‌روست. بر اساس این گزارش، ترامپ به‌دنبال دستیابی سریع به یک توافق گسترده است، در حالی که ایران مذاکرات آهسته‌تر، غیرمستقیم و توافق‌های محدودتر را ترجیح می‌دهد.
🔴
آکسیوس می‌گوید بی‌اعتمادی میان دو طرف پس از اتهام‌های متقابل درباره نقض تفاهمات قبلی افزایش یافته و فشارهای داخلی نیز مواضع دو طرف را سخت‌تر کرده است
🔴
طبق این گزارش، ترامپ نیز نسبت به امکان دستیابی به توافقی پایدار با ایران تردید بیشتری پیدا کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/150600" target="_blank">📅 18:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njkn7ZDsqMITkX1kUX-Q0yY0ND3v1parsV7sAfnD0Yx-MRHyuols1S2Xu8ytU_wupE3Ozp1MSiy9Tl_DgATn5_JMGcTOhktYodzL4QR3rGg2M7GkfOxA502Br0gTL-GRrpIia4acYSYmRrT-ezMxiauD4MXGKDlPgVrX1WZzkrOmakj3BqFRjdrPx702a7y0CLbqDBi2z4c6yx3ovL1u_xj7qEdW-dxCvNPV0MvltwjSKBPox25PrUNRc-2LtNDYGgAUdShWTTUNyCCRSTlJQVv_LrDrLggFFi3zbpltGQMRE5c_94Ehm6PCn2cxMfsfeWqoO5w6DCVyci19-_0SyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از تسلط بر منطقه بنی محمد، حوثی ها به سمت الزعازع در شهرستان الشمایتین در استان تعز پیشروی می‌کنند و بیش از پیش به التربه، آخرین مسیر تدارکاتی بین تعز و عدن، نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150599" target="_blank">📅 18:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHnbcrurtZ7eXB0RfDftuzRZXwkfmIMMzqLsQHkYDqDCZaQ2Mc-qFKD-0zqSODYWIHxJj3SNEy3ZZ9J0OfuvmHu7Zg8k6U27sv_j8F9NmdvYNMZjjeO89l38Hhli3Pn0lEsyBhhqkbpj-KKtdAWgTiI2bgRwcBKv8PIIj76HQctRib8gEbdtfKYPEmyX-cQZHU-KyN8WsE0DVMcVHC3IUJ8z9NzV2EDEJBOH8TljaWkwU-viaeS7xhb8hb51IKq_2E6ZbP3uVABy5dJYmyl1cZgSuYsjR1IqXGQPkDoYsODGpw2Sm7zcPehdByuJKRxW9MOe7kpwexo4RbC6t8NEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۹۸ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/150598" target="_blank">📅 18:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=h29J8EqODXNibcCn_uBiZGLLREntGN2MfQd-UhYmhJK3UkaJet1W9MXcMcvhnkrc2X9YL7N0K3S6vL7911m_M-OjFW1bolqXHoH08rdZCcNRpEHn9qb1Enm0vsRFc9zdp0cSX3t_BeVdgOG45Cn6uHLL7owG-0W3MAZI93LYIdg02pjhB_Cq36ZgQem87lUuf-Rgsajyk_uMxnshDUNcCnOuGmT2LW_RUttENlLtPZn0hZ8QhgnIM_GWYXN-HRajQYDhn8TQokF4s8IEbXUwzelc6aeGLtJIAp87tC4oD4ZyuieluoU4w7Tt0t9o-ttEhrJENKgzPgJdrTlW4AuFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4df7e241a.mp4?token=h29J8EqODXNibcCn_uBiZGLLREntGN2MfQd-UhYmhJK3UkaJet1W9MXcMcvhnkrc2X9YL7N0K3S6vL7911m_M-OjFW1bolqXHoH08rdZCcNRpEHn9qb1Enm0vsRFc9zdp0cSX3t_BeVdgOG45Cn6uHLL7owG-0W3MAZI93LYIdg02pjhB_Cq36ZgQem87lUuf-Rgsajyk_uMxnshDUNcCnOuGmT2LW_RUttENlLtPZn0hZ8QhgnIM_GWYXN-HRajQYDhn8TQokF4s8IEbXUwzelc6aeGLtJIAp87tC4oD4ZyuieluoU4w7Tt0t9o-ttEhrJENKgzPgJdrTlW4AuFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه اخوند تو تجمعات شبانه: در پیروزی ما توی جنگ و ابرقدرتی ایران تو کل عالم شکی نیست؛ الان دعوا فقط سر میزان ابرقدرتی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/150597" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری / ترامپ: «اروپا همین حالا موافقت کرده است که مقدار عظیمی از ذخایر انباشته گازوئیل خود را آزاد کند.
🔴
این فرایند فوراً آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/150596" target="_blank">📅 17:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سپاه : آماده‌ایم به هرگونه تهدید یا حمله، فوری و شدیدتر از عملیات وعده صادق ۲ پاسخ بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/150595" target="_blank">📅 17:34 · 10 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
