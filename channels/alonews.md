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
<img src="https://cdn4.telesco.pe/file/muQNAevQnzCpyE6TwLUaFcwc77yvDswawaAvRoEzAL3HdtvFRZScQv13OhImWgsuf5x0mwx-UzPHflXzdcvU8nPHxIIWyMd2SG96HhcbUDIYKAedV1F1PpoAZd3Tm88smepCgW_NMPlxOo7KV1pjtDvQ9nZQbGB5ehnxS909mhc2Kq72TtqHLMnpt9CvMAPJLsAagcqsHsbpswbcjUZ9w0yRBZP98hn01ev_RVhD6fWZO5F2eYK7azai4gWO_TYkQtNRMh_yNta26tRTLNxNE0CeOr67MEFXL67RA8Av3R_QDN-UhhjZeJyhDh2Rcws2L6OGgmRPm54QcY4dWRAIwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 22:18:40</div>
<hr>

<div class="tg-post" id="msg-136166">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ارتش اردن : ۳ موشک شلیک‌شده از ایران رو رهگیری کردیم</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/136166" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136165">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تعداد سوخت رسانهای آمریکایی در اسرائیل به عدد 90 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/136165" target="_blank">📅 22:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136164">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزیر راه: بازسازی سالن مسافری فرودگاه بوشهر به‌زودی آغاز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/136164" target="_blank">📅 22:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136163">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
اطلاعیه جدید آموزش‌وپرورش درباه امتحانات نهایی
🔴
آموزش‌وپرورش: بر اساس تصمیم ستاد عالی آزمون‌ها، امتحانات نهایی پایه یازدهم تمامی رشته‌های تحصیلی، در روز چهارشنبه ۳۱ تیر ۱۴۰۵ در همه استان‌های کشور، به جز استان هرمزگان، مطابق برنامه ابلاغی برگزار خواهد شد.
🔴
امتحانات نهایی پایه دوازدهم در روز پنجشنبه، یکم مرداد ۱۴۰۵ در تمامی استان‌های کشور، از جمله در استان هرمزگان مطابق برنامه برگزار می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/136163" target="_blank">📅 22:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136162">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
طبق گزارش i24NEWS با استناد به یک منبع امنیتی اسرائیلی: ایالات متحده در حال آماده‌سازی مرحله بعدی از کمپین نظامی خود علیه جمهوری اسلامی در روزهای آینده است و افزود که طرح‌های عملیاتی نهایی شده‌اند و در انتظار تایید رئیس‌جمهور ترامپ هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/136162" target="_blank">📅 21:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136161">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
پرس‌تی‌وی: گزارش‌هایی از انفجارهای شدید در پایگاه‌های نظامی آمریکا در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136161" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136160">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شهردار نیویورک، ممدانی : نتانیاهو حکم بازداشت داره اگه وارد نیویورک بشه، باید طبق قانون، برخورد بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136160" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136159">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=GmmMWuB1rmya6n8YHtLpaxY3BlVo8EfgvH9_m8WPbro6C4LO1d5JUPlgBv-joYOW_dhQcdxblfAFMeIB2XCtV49D9W02DE6YlLWpRHwCoAzUK6rEX-zr8ZalmS-PTLyJdWgCsOtzRQQE-fEDQLTp3-VlcWfSblUwTMM7QnRboq6rtF84biVXUezOOF0-jk6l9bq8IOFz_atRqJwsK6QQwkGabb266mwb8j9XKETtuavVzqCNWTlry_6XTZeaox3dfDSAsFLzMlpHtl306RF1ZAd3wEvQNvAq808I4u85pf837b9pYcpdfIkY4kAavTMzxyEdSckSsdzdLCxk_WyzZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bbc33d8c.mp4?token=GmmMWuB1rmya6n8YHtLpaxY3BlVo8EfgvH9_m8WPbro6C4LO1d5JUPlgBv-joYOW_dhQcdxblfAFMeIB2XCtV49D9W02DE6YlLWpRHwCoAzUK6rEX-zr8ZalmS-PTLyJdWgCsOtzRQQE-fEDQLTp3-VlcWfSblUwTMM7QnRboq6rtF84biVXUezOOF0-jk6l9bq8IOFz_atRqJwsK6QQwkGabb266mwb8j9XKETtuavVzqCNWTlry_6XTZeaox3dfDSAsFLzMlpHtl306RF1ZAd3wEvQNvAq808I4u85pf837b9pYcpdfIkY4kAavTMzxyEdSckSsdzdLCxk_WyzZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت سامانه‌ی پدافندی پاتریوت در اطراف پایگاه هوایی الازرق اردن جهت دفع حملات موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136159" target="_blank">📅 21:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136158">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه اسرائیلی کان: ترامپ به اسرائیل دستور داده است که در هیچ رویارویی نظامی با ایران شرکت نکند، مگر اینکه خود تهران ابتدا به هدف قرار دادن اسرائیل اقدام کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/136158" target="_blank">📅 21:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136157">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تحلیل نیویورک‌تایمز: ایران و آمریکا به لحظه «بیدار باش» رسیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/136157" target="_blank">📅 21:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136156">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
هم اکنون وضعیت در اردن عادی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136156" target="_blank">📅 21:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136155">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=MKL__vvG4OfYNQlNWKGBf_M-Zf9mwHXBOlav30ukDBTR9IJhlblDGgiA2gWDz8rWVUQoHaWeKKZGMoC0ZNWuUVyEp1HtR3nli6V5MecHqm9ORrN2Qd0LAqOAfFRsxYLiHegCjt4vH6nqXgWmq4Zxef9VjNuagiILhB3n5lJAdnfT6Rw0cY6B49tkAJrlNQsGKGpJHVwLsXf7vZ0Yj75Z1EEN29nhPcwKLfTHhVi0BjDvG7UaPqy9QYfivvM_9sRp-VhdfOx8SEQCgYAvv-qQQpyvMLeSPcSXLkgz7p6ULqqWZaCh2gg46Lfmv5vap4fO5BV0NcvEV67QPUO60FTQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da7dc70f.mp4?token=MKL__vvG4OfYNQlNWKGBf_M-Zf9mwHXBOlav30ukDBTR9IJhlblDGgiA2gWDz8rWVUQoHaWeKKZGMoC0ZNWuUVyEp1HtR3nli6V5MecHqm9ORrN2Qd0LAqOAfFRsxYLiHegCjt4vH6nqXgWmq4Zxef9VjNuagiILhB3n5lJAdnfT6Rw0cY6B49tkAJrlNQsGKGpJHVwLsXf7vZ0Yj75Z1EEN29nhPcwKLfTHhVi0BjDvG7UaPqy9QYfivvM_9sRp-VhdfOx8SEQCgYAvv-qQQpyvMLeSPcSXLkgz7p6ULqqWZaCh2gg46Lfmv5vap4fO5BV0NcvEV67QPUO60FTQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکت پهپاد شاهد به سمت پایگاه آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/136155" target="_blank">📅 21:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136154">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ded62ba49.mp4?token=ViGTIRKm58JTj2z8wvO7-el2yzM-8qNGEduXzooik9Qlb7jfAvdWiRVPrqMlCUftfyghA2JBINhODvUHrwlnyQZQa15GJ-V3ZMEzmU3D7Oefwj6-YbSr6LADJ2wt_t1uRTOAQJoowQQKXMw6EHFdUvZlRnYucXSXlgmXg4BQplChl_LY8xmebIv8eY9sAEyNIO9erdpVsN2eKxQC9c537aEWSkWBjVyNNKsvfUpbsIp9-ddLBAvktJixII6MfZ2zBP4m884MZkzSbVPUre56wcHGKOLnq7IBq9n-jbzRywy191FpPAjVIxtVzGsJL1ioO-oXlAHTq4xhql1uzALxyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ded62ba49.mp4?token=ViGTIRKm58JTj2z8wvO7-el2yzM-8qNGEduXzooik9Qlb7jfAvdWiRVPrqMlCUftfyghA2JBINhODvUHrwlnyQZQa15GJ-V3ZMEzmU3D7Oefwj6-YbSr6LADJ2wt_t1uRTOAQJoowQQKXMw6EHFdUvZlRnYucXSXlgmXg4BQplChl_LY8xmebIv8eY9sAEyNIO9erdpVsN2eKxQC9c537aEWSkWBjVyNNKsvfUpbsIp9-ddLBAvktJixII6MfZ2zBP4m884MZkzSbVPUre56wcHGKOLnq7IBq9n-jbzRywy191FpPAjVIxtVzGsJL1ioO-oXlAHTq4xhql1uzALxyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک
های رهگیر بر فراز آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136154" target="_blank">📅 21:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136153">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5d359683.mp4?token=bQ_QVgI0QhM78iH0Iw_7B-RPzCR_X99s4Mxzhq-2QtddSGnaqMen_8vk7r8xwPgAciTT4LPmWwRPBt7G4q_dmT9GBUDqjD1yBpquro1-IWxSZEkaGVlTbnKcuVwRPtj-H1zwS-2PuWI0X2169F58yVyh-gHOWzNXxCqX5J9_92jm9bU76kZmXVGWip-RClgmcpIbcQH19Qajg4_KtPnwmQs0XxuHeJn9ZwUEPfvwP0EtsEc3KKA2PcDOmL6NCEQZwKAJOeY6xNFlJNci-kr22ENgFnLtuOmrmp57-FYLWtScJCXKmk_BHc5J6Rhw34VVGaFONPwXOLwh6f3phui7yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5d359683.mp4?token=bQ_QVgI0QhM78iH0Iw_7B-RPzCR_X99s4Mxzhq-2QtddSGnaqMen_8vk7r8xwPgAciTT4LPmWwRPBt7G4q_dmT9GBUDqjD1yBpquro1-IWxSZEkaGVlTbnKcuVwRPtj-H1zwS-2PuWI0X2169F58yVyh-gHOWzNXxCqX5J9_92jm9bU76kZmXVGWip-RClgmcpIbcQH19Qajg4_KtPnwmQs0XxuHeJn9ZwUEPfvwP0EtsEc3KKA2PcDOmL6NCEQZwKAJOeY6xNFlJNci-kr22ENgFnLtuOmrmp57-FYLWtScJCXKmk_BHc5J6Rhw34VVGaFONPwXOLwh6f3phui7yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
امان پایتخت اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/136153" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
انفجارهایی نیز در اربیل، کردستان عراق رخ داد. ممکن است برخی از موشک‌ها به سمت اربیل هدف‌گذاری شده باشند، یا این یک حمله پهپادی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136152" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
حداقل یک چهارم از موشک‌های بالستیک توسط سیستم‌های دفاعی MIM-104 Patriot در آسمان فرودگاه بین‌المللی پادشاه حسین، واقع در شهر عقبه، اردن، مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136151" target="_blank">📅 21:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78558531db.mp4?token=iZhTPqTp8sjbX0WfwdKtQXRt1W3oyCC26lRAFRIjDMc24yQQi8CvJnTNB9PgtfjFq6H7Z-IJPE68NqORuFylrtKGqc-inTbL5Q6TJJ6t398xHfRVPwtqExsmIz0oohY27ituoRiPsmJQqTqiUlfz2S-7L0odYgi3ByIue7umtj9Z12yp0lAwDvQ7yYxbYE-rHwf0DQIJcdzfP601KHHdxIu1t_6U0KTEAxCslnHLBbZ8nhw2Gl5tq7LHzmXi87_l2FjNZcjSubRrvyVoLv53Rzkn78r3s3jAVCMuwea5kKUYbQ1OM9BW3S6V-6GMPm3DDznf0LVbsVH_En0PP-tNiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78558531db.mp4?token=iZhTPqTp8sjbX0WfwdKtQXRt1W3oyCC26lRAFRIjDMc24yQQi8CvJnTNB9PgtfjFq6H7Z-IJPE68NqORuFylrtKGqc-inTbL5Q6TJJ6t398xHfRVPwtqExsmIz0oohY27ituoRiPsmJQqTqiUlfz2S-7L0odYgi3ByIue7umtj9Z12yp0lAwDvQ7yYxbYE-rHwf0DQIJcdzfP601KHHdxIu1t_6U0KTEAxCslnHLBbZ8nhw2Gl5tq7LHzmXi87_l2FjNZcjSubRrvyVoLv53Rzkn78r3s3jAVCMuwea5kKUYbQ1OM9BW3S6V-6GMPm3DDznf0LVbsVH_En0PP-tNiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آژیرها در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136150" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندر ایلات
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/136149" target="_blank">📅 21:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
آژیر ها در اردن به صدا درآمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/136148" target="_blank">📅 21:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/136147" target="_blank">📅 21:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گزارش شلیک موشک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136146" target="_blank">📅 21:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136145">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تبریز هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136145" target="_blank">📅 21:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
صدای انفجار در آسمان اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/136144" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4EQBnSuQUvoKmJdDBxNsyZaYNaz3RCt49pTJzlPRXL5g9U2pCown-kmTsgB2GZdrYwefxyzSevldJSDzVWenOFJUY6fMNBssrtw1bFOibVvLn-wmivqBNQ5Wz2MZWKxiOKO8U9nBaWzQRkm1_3-rFAbwWSbdAPChos8Vhsd9e3sG55s3JTF-FO6mxU35Mu_CYZ-Wj2q2E9FLFZD2fAl4Jc8X8NRCesKpTXuYIFyooNenhTL2sEA9NHLrXH0uQS_-P58KiSiN6MI8qISYPtv18HBPJyIs3Fk4ROS30vEzbCDdgYianfqjaj-0C0-_sH-70fJrucixHiGXj2uwXuBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تبریز هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136143" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/136142" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136141" target="_blank">📅 21:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/136140" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کارولین لویت، سخنگوی کاخ سفید گفت که ترامپ در مراسم انتقال نظامیان کشته‌شده آمریکا به پایگاه  هوایی دوور که عصر سه‌شنبه به وقت محلی برگزار می‌شود، حضور خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136139" target="_blank">📅 21:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رویترز: حملات هوایی اسرائیل در تاریخ ۷ و ۹ مارس (۱۷ و ۱۹ اسفند) به دست‌کم ۱۱ محوطهٔ تاریخی ایران آسیب وارد کرده است که  ارزیابی‌های یونسکو، شامل میدان نقش‌جهان و کاخ چهلستون در اصفهان می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136138" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تعداد سوخت رسانهای آمریکایی در اسرائیل به عدد 90 فروند رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/136137" target="_blank">📅 21:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136136" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ایالات متحده در روزهای آینده، مرحله بعدی عملیات نظامی خود علیه ایران را آغاز خواهد کرد - به نقل از یک منبع امنیتی اسرائیلی توسط شبکه i24NEWS
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136135" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نماینده اردن: نظامیان آمریکایی برای گردش به اردن آمده بودند!
🔴
پس از کشته‌شدن ۲ نظامی آمریکایی، علی الخلایله، نماینده پارلمان اردن گفت: نظامیان آمریکایی به‌صورت اتفاقی و هنگام گشت‌وگذار همراه یک چوپان در صحرای اردن، بر اثر اصابت ترکش موشک کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136134" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
افراد نزدیک به ترامپ از او می‌خواهند که پیشنهاد قطر برای آتش‌بس ۱۰ روزه را بپذیرد
🔴
ایالات متحده آتش‌بس را رد نمی‌کند، اما می‌خواهد که مدت بیشتری ادامه داشته باشد و ملاحظات بیشتری در مورد تنگه هرمز وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136133" target="_blank">📅 21:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136132">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری /  تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136132" target="_blank">📅 21:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136131">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baac3e6178.mp4?token=r57VOpXzfo0pM1Eb8v07akjughu0diMwGG1a6MxKMYAjMmAnFq07KgtzcSs6dgubu8TEYZaI_fkFaRI2xp0cxIRonCr5QuApBMWR8jTvGi69hI46jodaJpCLegGhdtP--QxZ77qMUn08cedan7nKlPGEH3ko0cExskfyLOPcdnfFILM8_9ZNZpIvIXbFGA_VdYpNNR3ulIcHwB-tnnY8I5VkQj5cQgm2fe1hztbdxOYXVaSiqy-58wUoMynd1S0-Xmdufr2dcqo-Ov-n1K4nF21PH3GwFx7rNqWPsfFjxP4OsSjZeJDjZB2Bx7m4uLGFaCj8Lnsmb-DzvfJ9u-gUKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baac3e6178.mp4?token=r57VOpXzfo0pM1Eb8v07akjughu0diMwGG1a6MxKMYAjMmAnFq07KgtzcSs6dgubu8TEYZaI_fkFaRI2xp0cxIRonCr5QuApBMWR8jTvGi69hI46jodaJpCLegGhdtP--QxZ77qMUn08cedan7nKlPGEH3ko0cExskfyLOPcdnfFILM8_9ZNZpIvIXbFGA_VdYpNNR3ulIcHwB-tnnY8I5VkQj5cQgm2fe1hztbdxOYXVaSiqy-58wUoMynd1S0-Xmdufr2dcqo-Ov-n1K4nF21PH3GwFx7rNqWPsfFjxP4OsSjZeJDjZB2Bx7m4uLGFaCj8Lnsmb-DzvfJ9u-gUKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجریای صدا و سیما و دایی یکتا مثلا اومدن برن جنوب و بگن شجاعیم، بلند شدن رفتن بهمنشیر که ۱۲۰۰کیلومتر با بندرعباس فاصله داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136131" target="_blank">📅 21:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136130">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYPW706Mbbt5GH1YjZ9ATLjK5asNLB2sDVPQH4w3PAq34IvqTdfJEkzZPJ8WM94guMQUQaCkADBUUsUhtWfGv9dfyhvP78JuzEgkeSqfrtVH3SGfBWxn5ci7g5dJ5rYXMmRSxVCWV7VJA1Msacaz4o4eWysSfo5ECPxl96ieY6Y8NmvQc_Bhb5NBqMUNPEwyPb6ndedd-yxPoF5Sbwrt1B6oaGFNu1xz4xCbndSi90kX1DJtWxIOnCnTfx3eSXv7XhA1EzNMXXRk4CATysoAd8olrURDbz24MXzy8-_A78oEivfv2572c-epms6cda6d_LMRukiX2zZj1A39VFcYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو: ایران پول کم نداره، مشکل اینه که پولاش جای دیگه خرج میشه.
به
گفته اون، هر پولی که ایران از فروش نفت یا رفع تحریم‌ها به دست میاره، به‌جای اینکه خرج آبادانی کشور بشه، صرف حمایت از حزب‌الله و حماس میشه؛ در حالی که می‌تونه برای ساختن و بهتر شدن خود ایران هزینه بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136130" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136129">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سازمان ملل متحد خواستار «کاهش فوری تنش» در غرب آسیا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/136129" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136128">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-uojnF4-4xn3khtNoykxE8b2G_AyfM5mmdG0AYX8_uxZuNODq9d1qfXjNh54h4cML5aLbRvM2qjVAJqTw_bWHe93b2db0J21CK3qNRPER0DbzNzPrEPXGcXmk5DkYOjOVL6KwzHqwLBeAYEal6mkztX6ek9-9rznEgf_ETAZlBkCtQeQ8PqyMtDtjzZKz9ClaxhU_ktoE9lq4ImyA809mo7E4DHvB50G7QWUw417UTTm_xp9By9uidto9Afd7WtYGNSbwK123Fly18D6sxwCviXcaskM-445xikFcve-xXOtX-rd5mHQ1F4BnDkXXWSO6cSY87pL8TC3ynuURcXkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقوع حادثه امنیتی در سواحل عمان
🔴
کشتی دوم هنگام تلاش برای عبور از تنگه هرمز هدف موشک قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136128" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136127">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
پزشکیان: موضع‌گیری‌های احساسی نباید ما را از رسیدن به اهداف دور کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136127" target="_blank">📅 21:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136126">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزارت امور خارجه چین: ما با حملاتی که هدف آن تأسیسات غیرنظامی در کشورهای خلیج فارس است، مخالفت می‌کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136126" target="_blank">📅 20:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136125">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک مقام دولتی افغانستان به الجزیره گفت که در اثر سیل در استان نورستان، 20 نفر کشته، 80 نفر زخمی و بیش از 100 نفر مفقود شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136125" target="_blank">📅 20:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136124">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مدیرعامل شرکت توزیع نیروی برق تهران بزرگ: به ازای هر یک درجه افزایش دما، بیش از ۲۵۰ مگاوات به بار مصرف استان تهران اضافه می‌شود که معادل مصرف برق ۲۵۰ هزار خانوار است.
🔴
پنج هفته سخت را پیش رو داریم و امیدواریم با هماهنگی و همکاری مردم بتوانیم این پنج هفته را با کمترین محدودیت پشت سر بگذاریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/136124" target="_blank">📅 20:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc6dbhIJc2oj9rxkXRpEYhDfbUUBtU-18Np7Cdv06uh_Xmj8rlfEfdjJ1f67BGwdBCYvcvKm7bUU4YwbhNOg2gJrxu4TTvZLaI2kqxoJilacttFeCvYjwXYhQZo6U-o6kSvwV9S3zVLVaMyBQWEZm5C4h2-bU7hqIkbsiqftwCxU6GsWnmy4lfYdu4U23LKop6fBCsdJJ6a4c2sPM8efjUSthBPuENt4JfdqZummR_8FnzsI8Gnk21cI15MVsHcvawciYi3TAX3K7gKSzHLhdajepu3Oe08SpmqgIIVb-vcCkpPtJo6U11RYQ4URw4RoCCCTwclaDMUSrMjS9EXXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در بازه زمانی ۹ روزه آغاز دور جدید درگیری ها میان امریکا و ایران، قیمت نفت برنت از ۷۰ به ۹۰ دلار رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/136123" target="_blank">📅 20:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
روسیه: آماده کمک به حل مسالمت‌آمیز اختلافات بین ایالات متحده و ایران هستیم
🔴
خوشحال خواهیم شد که بستری برای گفت‌ وگوی کشورهای عربی و تهران فراهم کنیم، اما قصد نداریم خودمان را به آنها تحمیل کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136122" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
استدلال این هم وطن کاملا درسته که میگه سرباز آمریکایی سگش شرف دارد به کل جمهوری اسلامی و طرفداراش
🤔
هرچی از حرام زاده بودن طرفدارهای جمهوری اسلامی بگیم کم گفتیم.</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/136121" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: اسرائیل سطح آماده‌باش را به بالاترین حد افزایش داده و نهادهای امنیتی خود را برای مرحله‌ای جدید از تشدید تنش آماده می‌کنند. همزمان، مقامات امنیتی اذعان دارند که تصمیم نهایی درباره روند تحولات، به تصمیم دونالد ترامپ بستگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136120" target="_blank">📅 20:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTlF78GtiIY1sOnwOLlrr2dqCi9kvO-sOsJzdVc6MY0Mn-KVVH37ww7VSOPa4VlgbOirr-K4D1wBRt25wzpcEmqISUavI-c3_5BlrsY-CLWLhaYPcBnEu8saq9pefRh4ijn40Xm18VE5spa-a_1_Va55zlLR0ewhv9J1EWv-buR6g0CDZlpQ9ZugNo-6ZnyUOHCwUWRTL8sD3SJG1_QLBcNAsehlAqBfAQxgC8Og9G5o0fpPEYjljKpcj1umkasEnj2dvwG90Iuta9pVmpDqItkCJ-Y42NxmZIp9Ebgl9dnhS276d8o26XvMUD8B9VeUfd23jl5mgo_S7tbERfdBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک سیستم دفاع هوایی کوتاه برد به نام FK-2000 که توسط چین تولید شده است، در یک منطقه ساحلی در بحرین مشاهده شده است.
🔴
این موضوع بسیار غیرمعمول است، زیرا هیچ سابقه رسمی مبنی بر استقرار این سیستم توسط بحرین وجود ندارد. امارات متحده عربی تنها کشور در خلیج فارس است که به طور رسمی از این سیستم استفاده می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136119" target="_blank">📅 20:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNkdswi6vNLxEo4pKgaN9Qq6Q19yK6VAifPUOTTUUhn1EjSa0hNoZbYKub5rVAQdvaIZMifz4S2eljhh6P-sBD0vFA3FosN-EuFAKtN61_Pe0akUo3tCS15fzIlVHgukiTfj9olicsLGjLUEPT3kjZHynTiiKXattQoCiOb4yYnYj3iJvGEegFlPfcVhCP1I_mCa_j_HI41ri3e-59Kgft3czIpotWdqQdaCzaXJEqTUqjJsEMrpFzYoDvgXGpjkg1xzEte1Nf3KJsS99YDstxrfVVsO0PS-mozKrMyElfyCLDV5DF27BbJJ86RNriAJzmWtH3nw-9zitkC5xfqFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هگست، وزیر جنگ آمریکا پست ترامپ رو تو صفحه ایکس خودش گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136118" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / خبرگزاری عراقی نایا:
ایران آماده حمله زمینی به کویت شده و هر لحظه شاید حمله کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136117" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b3c25773.mp4?token=YqLEPmTncBbCrk9Lu63sHdFfx8wy7fp0w9zsDib3y22OMt9JqAJCqS_4HimePMxVNHzh-oTQnuSjO0J_fTx8LjiB9fqnQ6LGLaTMcjQKTdfkx0H6JRT9FzGDX-ArdTEbVUA2gOTMhFLBNUhrdnW8R47N1LVgw8ZmWfXYF3qUTLlNkhJershN3INGZvnOAdE9kcGCJp88kvT0-TI36kyNjPjYfqSgB2g7O2dG2GR0K_dMqAkQII-CajMvWpGv6GGReLMVh_fWc1a7Kc-zF7OnEj1BsuEFiXxXboeaorau_DfGuS00Y75uKIbQi4xRH5vZMGeJ0Uq2b_flwghtYFDc2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b3c25773.mp4?token=YqLEPmTncBbCrk9Lu63sHdFfx8wy7fp0w9zsDib3y22OMt9JqAJCqS_4HimePMxVNHzh-oTQnuSjO0J_fTx8LjiB9fqnQ6LGLaTMcjQKTdfkx0H6JRT9FzGDX-ArdTEbVUA2gOTMhFLBNUhrdnW8R47N1LVgw8ZmWfXYF3qUTLlNkhJershN3INGZvnOAdE9kcGCJp88kvT0-TI36kyNjPjYfqSgB2g7O2dG2GR0K_dMqAkQII-CajMvWpGv6GGReLMVh_fWc1a7Kc-zF7OnEj1BsuEFiXxXboeaorau_DfGuS00Y75uKIbQi4xRH5vZMGeJ0Uq2b_flwghtYFDc2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری /
تجهیزات نظامی ایرانی از خوزستان به سمت مرزهای کویت در حرکت است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136116" target="_blank">📅 20:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: جلسه کابینه امنیتی و سیاسی اسرائیل درباره ایران با حضور تمامی فرماندهان و رؤسای نهادهای امنیتی آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136115" target="_blank">📅 20:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYN-uuKbOxskyDU3LD0EI_Z_cqpG7ERyj2inVbIf0MYRadMjXB1ZL4T8eyraTNK9rXrc1jORMXT_NU4832gQL7Sc3WV4I62NpqS3nWKaL25xL_NGZMU-8GeYuq__59PZToi7xzMwd8hAnGD0y5Fz28rrSHk3oqp3q5AyRqkWQuxSd7P8kUD8igT12Gh3ZzocCXjrTUSdJJInQuPrnCCcOykuUtOpR8uLirb_IpeZ41djRlKvyLtMF2PPI8bhqsd9UVJ1hwsgFKCxmpGo1T-4_6t0urbMjGaelioynh0ZIb2S4BRWFcTtn_vtNGUA11LToPxOD7llAdnX5Ypf49b_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، از طریق شبکه Truth Social: نتانیاهو به هیچ وجه، تحت هیچ شرایطی، در ایالات متحده آمریکا دستگیر نخواهد شد.
🔴
او در حال مبارزه با جمهوری اسلامی ایران است، کشوری که اخیراً ۵۲۰۰۰ معترض بی‌گناه را به قتل رساند و در طول ۴۷ سال گذشته، سربازان آمریکایی و دیگران را به قتل رسانده است.
🔴
تنها کسانی که باید دستگیر شوند، افرادی هستند که ایران را به این گرداب بی‌سابقه مرگ و ویرانی سوق دادند، چیزی که سال‌ها پیش، توسط روسای جمهور پیشین، باید به آن رسیدگی می‌شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136114" target="_blank">📅 20:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136113">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وزیر کشور پاکستان: امیدوارم وزیر کشور ایران خبرهای خوشی به همراه داشته باشد
🔴
محسن نقوی، وزیر کشور پاکستان با استقبال از اسکندر مؤمنی، وزیر کشور ایران و هیئت همراه، نسبت به این سفر ابراز خوش‌بینی کرد.
🔴
او گفت که امیدوار است وزیر ایرانی «خبرهای خوشی» به همراه داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136113" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136112">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پوتین رئیس‌جمهور روسیه فرمانی را امضا کرد که بر اساس آن مقررات ورود بدون روادید شهروندان چین را تا پایان سال ۲۰۲۷ میلادی (دی‌ماه ۱۴۰۶) تمدید می‌کند.
🔴
عبارت تا ۳۱ دسامبر ۲۰۲۷ جایگزین عبارتی در فرمان قبلی شد که تا ۱۴ سپتامبر ۲۰۲۶ میلادی (۲۳ شهریور ۱۴۰۵) مجوز ورود بدون روادید شهروندان چینی را صادر می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136112" target="_blank">📅 20:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136111">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnWy-vlWUHZvG5Y6AmzJ1aU2y6jeOVbtKT9vZATQ2ebPyntBnSGcHhdutiQFymOrM8FwXU3zLAw1_YLCv1xD44aiTohn_X7sTEg2XvaVjH4ZcBNObOablHUiiAh_WsxLJ6mXKFpzAZBIXlRMRjUOgSqpA3kcmOZzOSEZ19pxxUkeJ_jGC222Ho135XPTimgaL1-ty7VsLtgQKHM1jcsvHKF_UVCoXAJGI3wGx5s7GbeyRqj6QVMYcC3QX84aOlb7prO2RA6V2tPoCYOUStyjNTk_cy2aWs2E4WoypNMgkfBq-cp5TZwtFBr_vqxZdTmt9mHF1fj9MmNYIz4SuFe59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
🔴
این دستورالعمل به پیتر هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136111" target="_blank">📅 20:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136110">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
تعلیق پروازهای ایرفرانس به منطقه
🔴
این شرکت هواپیمایی اعلام کرد که پروازها به ریاض و از ریاض تا ۲۵ ژوئیه و خدمات به دبی و از دبی تا ۲۸ ژوئیه را به حالت تعلیق درآورده است
🔴
همچنین تعلیق پروازها به بیروت و از بیروت را تا ۲ اوت تمدید کرد، این پروازها از اول مارس به حالت تعلیق درآمده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136110" target="_blank">📅 20:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روسیه: اوکراین به دنبال بی‌ثبات کردن بازارهای جهانی نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136108" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqpDSxohTgDB2RK0pP0CpxVFSsszXuFgE3r9sGO_xf5hrOScIeCDWZpKZbak6_VHxsBtjhwMVh9kFnkrYWsceWBkz6hojG7w1nV4q-Vm1Ag1kMddNc8Z6n50jbZnrIr_quf3AYMaYLSlBA5U1I7DhTc0r2sd1T5OXnlPq9JWLmRVlHnKxi05C3PUOBUFsqCfavoP546tun3R1ETWi4IPXpdCEqkv-Ig6gBXkPMQJRwCxdeD0Xr8jvbPliI_OFGnWvgGVbqq39Z-I-Cr_dZyLzANobmfsNW_dyRAFYSrV_ENQvripqGSgXoqCWqcBWK6aYS21E70F7g40ceNv8T6TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی منابع: تصاویر ماهواره ای تایید می کند که سپاه به پایگاه "برج 22" ایالات متحده در شرق اردن در مرز سوریه حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136107" target="_blank">📅 20:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نیویورک‌تایمز: «اردن» به کانون تازه رویارویی نظامی ایران و آمریکا تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/136106" target="_blank">📅 20:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
یان برمر تحلیلگر و مدیر موسسه تحلیل ریسک اوراسیا گروپ:ایالات متحده می‌تواند تنگه را با هزینه‌ها و پیامدهایی برای همگان محاصره کند، اما بدون یک توافق نمی‌تواند تنگه را باز نگه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/136105" target="_blank">📅 20:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca576a26d.mp4?token=ijMYw44HqhgDLjNHZD0EdiI5K1UifwJyC1fmSP17tAYV8dVq-2wqSCv_xVYpSMQUIZtepSLF_RuZXNCPXZjI9He4bQC5RBiniiaweQDMMCo9RUkkpvOvpjwOurPvpcSmBexYaKX2TqWc-_JhsRdKGzvfE73aAt_PVuQBaQqDIOYe81ZiQ2C0mCgDJgsXXp8oTqAQr-VojALQj5XgMGES8aLI0bfXeIAB3TPvkaIZQ6Q7LqyIFfp_jBn7MEhnM92cBwqJ9wVr3ITHcPclCDMx7HrVkGokmAPi4DWTHZO0uj1SDYds-YFhdIO5veMRnys_TUerC8lOVsX91ZmvtwOg1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca576a26d.mp4?token=ijMYw44HqhgDLjNHZD0EdiI5K1UifwJyC1fmSP17tAYV8dVq-2wqSCv_xVYpSMQUIZtepSLF_RuZXNCPXZjI9He4bQC5RBiniiaweQDMMCo9RUkkpvOvpjwOurPvpcSmBexYaKX2TqWc-_JhsRdKGzvfE73aAt_PVuQBaQqDIOYe81ZiQ2C0mCgDJgsXXp8oTqAQr-VojALQj5XgMGES8aLI0bfXeIAB3TPvkaIZQ6Q7LqyIFfp_jBn7MEhnM92cBwqJ9wVr3ITHcPclCDMx7HrVkGokmAPi4DWTHZO0uj1SDYds-YFhdIO5veMRnys_TUerC8lOVsX91ZmvtwOg1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداسیما: چندروز پیش این ما بودیم که آتش‌بس رو نقض کردیم و آمریکا بعدش به سیریک حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136104" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گزارش اولیه از وقوع یک حادثه دریایی در سواحل امارات
🔴
برخی منابع از وقوع حادثه‌ای برای یک شناور در آب‌های نزدیک سواحل امارات متحده عربی خبر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136103" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d906443db.mp4?token=SaSSJTnvbBS4LwITkPFlmKoFaIGlWQ_I_IVzZ3F24U24gVuvh3WP09RHSo1zTnjJwzaHy-qLBmYJXwZU1COqwfkQhoDXQmn31OMLqXcfTMhk6Hc3_B1flCSFONnnoxQRC7-niAZ_MMWOz6kvsJQ2E3OPRTGmCw1shwIaaS2NjjlxqW8TsqyQw6OiTncqDFa8n7lK71EGwVM_D3nGJjyAi0-JfZgVUGyQt-ZxrBTkw7T1gPo5pas-uDabtej-99NhV4sZFQUzznXxi8qesz7mtC_VG1GUGThV2EPOynvISF3zXLuY0YRIBY7MxU8UeWke3wNlJPEnG9SG2IYE49J1OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d906443db.mp4?token=SaSSJTnvbBS4LwITkPFlmKoFaIGlWQ_I_IVzZ3F24U24gVuvh3WP09RHSo1zTnjJwzaHy-qLBmYJXwZU1COqwfkQhoDXQmn31OMLqXcfTMhk6Hc3_B1flCSFONnnoxQRC7-niAZ_MMWOz6kvsJQ2E3OPRTGmCw1shwIaaS2NjjlxqW8TsqyQw6OiTncqDFa8n7lK71EGwVM_D3nGJjyAi0-JfZgVUGyQt-ZxrBTkw7T1gPo5pas-uDabtej-99NhV4sZFQUzznXxi8qesz7mtC_VG1GUGThV2EPOynvISF3zXLuY0YRIBY7MxU8UeWke3wNlJPEnG9SG2IYE49J1OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد انتحاری مدل "گران-4" متعلق به روسیه امروز به یک قطار اوکراینی در نزدیکی ایستگاه راه آهن سولنویه در منطقه زاپوریژیا حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/136102" target="_blank">📅 20:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136101">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
ما رو از جنگ نترسونید. ما جنگ رو به چشم دیدیم. تو شهر و محله‌های خودمون. تو ۱۸ و ۱۹ و ۲۰ و ۲۱ دیماه.
🔴
تو کدوم جنگی اینطور رگبار مسلسل رو به سمت مردم بی‌دفاع میگیرند؟ کدوم دشمنی بجز جمهوری اسلامی ممکنه اینطور مردممون رو قتل‌عام کنه؟!
💔
صداها رو گوش کنید. رگبارها کلاشینکف است. تک‌صداها قناصه. با هر کدوم از اون گلوله‌ها مغز و قلب یک جوان ایرانی را متلاشی کردند.
🤔
ما ملت ایران یک دشمن داریم و اونم جمهوری اسلامیه به همراه طرفدارهای حرام زاده اش. دشمن دیگه‌ای نداریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136101" target="_blank">📅 20:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136100">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش اولیه از وقوع یک حادثه دریایی در سواحل امارات
🔴
برخی منابع از وقوع حادثه‌ای برای یک شناور در آب‌های نزدیک سواحل امارات متحده عربی خبر داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/136100" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136099">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdjSUNPjxeAHtBi7cxnVK6TAkALMwwSokbEe5DiVblMRf88Uepxku-1AdyiseUUNgN5yPXbgUhUgSUOASzc5t0mKf99IPgW4PI5aoKYIJGrisiN1uhptyZksqINsN-859eP-wTpBqu7ntKiQxEEm56rdwkkMIOvFK8FyySxq9xqW2gpkFBRIfXBM8ip93kK7MqYvVEuCWYaPGfLxr_S_wyDvp92IhSY81KMjyyQT4wm1ilgKCMbAn6XJ4u0249Ow3WuvS024D_8kXd80T09R_KI8cA1caalbXN-yg8v4MJxjhFsXGCgBHM5qbEuxWDllsobsh9eFYRJphCIDLhBQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دمای ثبت شده در شهر های ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136099" target="_blank">📅 20:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136098">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
توانیر: بین ۷۰۰ تا ۸۰۰ هزار ماینر غیرمجاز کشف نشده وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/136098" target="_blank">📅 19:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136097">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
گزارش اولیه از هدف‌قرارگرفتن یک کارخانه در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136097" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136096">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
گزارش اولیه از هدف‌قرارگرفتن یک کارخانه در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136096" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136095">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuxgLRSofXKEqMr4lsfwXNILDQnFxA8gzkjlWvbm3MYh8nzh1g89wrI8zdlPkRuAiIJ1LyS2lHxv-zk3zvTn1drQFeefU5BpAnu91SFcGnNK2-ng0hrqAmfzqdVHqZMQPssyyCAT5W1DG9aLuyH0frwRyciBq4nZFJQq26RZR0ZI5QmoCgEhiG7lVDJPGK_E407wfVPsjSfa2qEJXzFfYWIbCcd1qsOqupHmimcFRyBQ8Gbedzwgz9DpvYGHGA4xMxjoVik9AEMYXxrU3HPgCaZ5IdEB1bQxmztyhs0H1e8UKEuoD1ycBvTaFuBfqd52JMslAyv38guu0UZmcSMkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ دستگیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/136095" target="_blank">📅 19:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136094">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد که نیروهای آمریکایی مسیر حرکت ۷ فروند کشتی تجاری را تغییر داده و یک فروند دیگر را از کار انداخته‌اند، از زمانی که این کشور محاصره بنادر ایران را از سر گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136094" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136093">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFWJk3ACWC6uiXaua3KacaXvI-9ipebYGKeRq-UB_5XBHeDBGNvH7IVZF4o7kXQE1CGhKBIOlBvamDRrvjfrI81gwyUAK3N8pnykwiU-9wDFPV75kesmYASujbfKNH2tkHwPADW0gVRplyryUL--BxfheDkj483tsiRLfvoVC_KmuCSDjs90DyKfR31eFaqOzx90dyJuweLSqoX9bCuRRvH3P8EOzUp-BwIlNgpiQr-iIbfmxTHNxWiR6GU2OxbJJSYBMEEXWXYtEY5_0Mqdsgw8bU-Ytl1LIE1OnMcUWPYU2kbJ_DOgS18SyDDNWaSkiT5ylxxHWSI6ji_x_4Cvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید: آمریکایی‌ها با قاطعیت از توافق صلح ایران حمایت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/136093" target="_blank">📅 19:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136092">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: میانجی‌های جنگ آمریکا و ایران در تلاش برای پیشبرد آتش‌بس جدید
🔴
قدرت‌های منطقه‌ای با نگرانی از افزایش خسارت‌های اقتصادی و خطر تشدید درگیری‌ها، در تلاش‌اند زمینه دستیابی به یک آتش‌بس جدید را فراهم کنند، اما همچنان با چالش همراه کردن طرف‌های درگیر با این روند روبه‌رو هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136092" target="_blank">📅 19:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136091">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / صدای انفجار در سیریک و غرب شیراز شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/136091" target="_blank">📅 19:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136090">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وضعیت در بحرین عادی است. موشک‌های بالستیک مورد هدف قرار گرفتند و منهدم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136090" target="_blank">📅 19:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136089">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7b5813d2dc.mp4?token=pjmY0YS2rIByGQhSUpVOvJ5hIt6rZcH6zp_6XXsNm4_OtpmDrlFNraL8OUv3tLGy755SjXwbCSm1a-RDUZbvfxzlH4eu4UI4djgTR_W8b7g2-d0DaWcooRmYFRrniw3OkWluzj7sI-lOuzIeAO_3-2owyoA66mg1FgApURDgSbwZsXtZKIhEC7c4jgl9L66Z6TbzvK3kygTQg6cH9hrUyKz4aq6uIiLjjbmb5Rp1STRV3LRip89P-_NGXiGngs5YhcV48Ht1dhdnNY0I00Z7MF084AADKdQQs-Rm2_fza9lS0ObUxLX8Tzddo9kW6WtBJBAEX-r3AgzF0AsGNFsqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7b5813d2dc.mp4?token=pjmY0YS2rIByGQhSUpVOvJ5hIt6rZcH6zp_6XXsNm4_OtpmDrlFNraL8OUv3tLGy755SjXwbCSm1a-RDUZbvfxzlH4eu4UI4djgTR_W8b7g2-d0DaWcooRmYFRrniw3OkWluzj7sI-lOuzIeAO_3-2owyoA66mg1FgApURDgSbwZsXtZKIhEC7c4jgl9L66Z6TbzvK3kygTQg6cH9hrUyKz4aq6uIiLjjbmb5Rp1STRV3LRip89P-_NGXiGngs5YhcV48Ht1dhdnNY0I00Z7MF084AADKdQQs-Rm2_fza9lS0ObUxLX8Tzddo9kW6WtBJBAEX-r3AgzF0AsGNFsqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای دریایی انصارالله، یک پیام رادیویی با فرکانس بسیار بالا (VHF) برای کشتی‌هایی که در مسیر به عربستان سعودی قرار دارند، ارسال کرده و به آن‌ها هشدار داده است که مسیر خود را تغییر دهند، در غیر این صورت ممکن است هدف قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/136089" target="_blank">📅 19:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136088">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
احتمال تاثیرگذاری در بحرین. ممکن است یک برخورد رخ دهد یا یک رهگیری در ارتفاع پایین صورت گیرد. این موضوع در حال بررسی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136088" target="_blank">📅 19:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136087">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رئیس سازمان آتش‌نشانی و خدمات ایمنی شهرداری بندرعباس از جان‌باختن ۶ نفر در پی وقوع آتش‌سوزی یک منزل مسکونی در محله اسلام‌آباد این شهر خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136087" target="_blank">📅 19:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2b37b047.mp4?token=TJw1iO_Yax2cijDexUcn_ZDX9oQe1pT1Qs9AjL5PCpbP58Ysp_DVvCJyfPnKS348i4Hv9LSw42miB9RW2BqE3Sn6rk-onDUp2pE04Zbe6Js_mQ-tv8u9xOcLkOsjoZpXkiFkfDDAYbSlwWvlyk91-PisZxt6MkdXIVRTGrzECu92X0XDAcpVFNQOdD0ezBisGF_lGOigF_PRpIy7lJdt2dq_KBAY0GD8e1Gj5Zo6QWRMWtZSrvIRUC5IjSqvbFvE2S3fEAJJXi2W6-ZazHwm-06GvAmN1uGmEUN7ei4iO_KcBedXUDCEY8XmgGdDfHp1LfVEgufzFJ8NcCGwBHzlLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2b37b047.mp4?token=TJw1iO_Yax2cijDexUcn_ZDX9oQe1pT1Qs9AjL5PCpbP58Ysp_DVvCJyfPnKS348i4Hv9LSw42miB9RW2BqE3Sn6rk-onDUp2pE04Zbe6Js_mQ-tv8u9xOcLkOsjoZpXkiFkfDDAYbSlwWvlyk91-PisZxt6MkdXIVRTGrzECu92X0XDAcpVFNQOdD0ezBisGF_lGOigF_PRpIy7lJdt2dq_KBAY0GD8e1Gj5Zo6QWRMWtZSrvIRUC5IjSqvbFvE2S3fEAJJXi2W6-ZazHwm-06GvAmN1uGmEUN7ei4iO_KcBedXUDCEY8XmgGdDfHp1LfVEgufzFJ8NcCGwBHzlLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی‌ از شلیک موشک بالستیک از لار فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136086" target="_blank">📅 19:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اسکندر مومنی» وزیر کشور به دعوت همتای پاکستانی خود و با هدف پیشبرد همکاری‌های دوجانبه وارد اسلام‌آباد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136085" target="_blank">📅 19:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/beRZ_kNON8eNjpA6GVWaW7pmtQ6IRMQ6l8SHdfI2VHmBuw5C-t5Cd5QVi7JObZUKV1j7SoLLaV05TudZG8HwRJVDZvL8qQxtIsrjMM9LpqTQP7v-pFnxY9w8f8r_oAU6hq46JMG6RLNzBKtgUmTINdlamZL1hgx6KnYi-1n98qvEZAlocNJhUjG_N6-i13jziuvAyvib_grOm_Rr7Li3lgsMU9OMzdlyVETuk-vGCt3owOVRga7HIg9wvaWp6T6LaLqgy6gNpPa6RPvfp61iPITKHJK2Mp4DIebMqITGkBHLQjWgheF04Zkk-vT9BAjtAAPM52NrrRSEK-Rg1emHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک موشک بالستیک از شهر لار، استان فارس، به سمت بحرین شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136084" target="_blank">📅 19:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آژیر های هشدار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136083" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
آژیر های هشدار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136082" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b09189c2.mp4?token=B4sWECbny9pJUKvfQsd7wnDGOdae-FZzizpfJDHPtC5lhBI5cC28c93mOMicERSrseTJn56aLXNLlDmzAliS5ZZCYG-NL-OxyYf3C--rDoSIia-RIYrnOhB_d5rebUjYmPl7kQXcdBsPDCYH9V1b36Y2Hu1VmBOKDABAA3AbdIVCasgQoKz-wnxH_vnpzXE2n8yEFaqj9q6TpM6pp6LdxRgK5qo1W8hGVCd-nzKFHPxdBvkPA6NkI5er0ylxrtjFpadvO_VcghvA9PJV28wyssTBBNovovAwjj633ucuS1oVGvxzDUtskY4mpao2QZCt5iY4DU2prVhjWqewgnAs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b09189c2.mp4?token=B4sWECbny9pJUKvfQsd7wnDGOdae-FZzizpfJDHPtC5lhBI5cC28c93mOMicERSrseTJn56aLXNLlDmzAliS5ZZCYG-NL-OxyYf3C--rDoSIia-RIYrnOhB_d5rebUjYmPl7kQXcdBsPDCYH9V1b36Y2Hu1VmBOKDABAA3AbdIVCasgQoKz-wnxH_vnpzXE2n8yEFaqj9q6TpM6pp6LdxRgK5qo1W8hGVCd-nzKFHPxdBvkPA6NkI5er0ylxrtjFpadvO_VcghvA9PJV28wyssTBBNovovAwjj633ucuS1oVGvxzDUtskY4mpao2QZCt5iY4DU2prVhjWqewgnAs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: ایران یک هفته پیش قرار بود بیانیه‌ای صادر کند مبنی بر اینکه تنگه هرمز باز شده و دیگر به کشتیرانی حمله نخواهد کرد. اما به جای این کار، به سه کشتی حمله کردند.
🔴
رفتار آن‌ها باید تغییر کند تا رفتار ما تغییر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136081" target="_blank">📅 19:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ژان-نوئل باروت، وزیر اروپا و امور خارجه فرانسه، اعلام کرد که روز یکشنبه شب، دو کارمند سفارت فرانسه در ایران بازداشت و به مدت چند ساعت بازجویی شدند، و یکی از این کارمندان مورد ضرب و شتم قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136080" target="_blank">📅 19:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878063c52a.mp4?token=jq4wv2xc00lbJCsxVhljF4Cz5bridSsQPxuTtA3W1v8SgGtkAb8kTLpzvyrdpBz_ZlKpas9-xCDX8vuFzEUna3sUBKGZQas48yckpBSBKUMyMSX8JHsLUVv0a9PPjZm2_bPB95-XL-uY_XJYEKa7j5h3LkGGp6n_jNFJXKHVbk-ad6xnyls73jt9ZGSsmU3nC8hKwB_Xr4rLZ8hXdjOPOh3MPvqJDlBVmG7L_mz3XxXRsKlGJIh0jwctuJvtqiNTSWWx9sbFuPb6TtOpT6hjfAgNNAWPeiP1y1kLEbHqPpyC9DrwHSs3BERpRKfQvyf7FnxgVD3n1eIO_vrHBkOW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878063c52a.mp4?token=jq4wv2xc00lbJCsxVhljF4Cz5bridSsQPxuTtA3W1v8SgGtkAb8kTLpzvyrdpBz_ZlKpas9-xCDX8vuFzEUna3sUBKGZQas48yckpBSBKUMyMSX8JHsLUVv0a9PPjZm2_bPB95-XL-uY_XJYEKa7j5h3LkGGp6n_jNFJXKHVbk-ad6xnyls73jt9ZGSsmU3nC8hKwB_Xr4rLZ8hXdjOPOh3MPvqJDlBVmG7L_mz3XxXRsKlGJIh0jwctuJvtqiNTSWWx9sbFuPb6TtOpT6hjfAgNNAWPeiP1y1kLEbHqPpyC9DrwHSs3BERpRKfQvyf7FnxgVD3n1eIO_vrHBkOW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما منتشر کرد: تشکیل زنجیره انسانی ده‌ها هزار هرمزگانی در نوار ساحلی استان هرمزگان و جزایر ایرانی و اعلام آمادگی برای دفاع از تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136079" target="_blank">📅 19:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E85zTiUOA50APvYfVNHJtJOvsfmoo9jgplYKc-ydQ56_iEMZgXxKTCa6BQFPh9gAciFmONuueqB8HpIE-xfik_CncKvnzWkBwY1uqvpS7o_0oMoVeCZxqgUBO8kdDNrAe-8p2lLt4bJ6IQFoLsPo4hPzuW-c4TsWqIv2troK3D4Jdq1GCEbqB9xie9anEV46xtvlbgACL_yD0cC_FSDL3pswC0wN8xApuh8wq8UXNDkqZeitwLlCTql3rF4sJFfq3c3IOo5EQhfI50bVdir0Fc0Zz9uTqXimI7LV8-vyTV64Xbiu9QBz7t9zp58UCOMHo4_icATTD3jDRzytSgK3uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت هواپیمای عراقچی به سمت پاکستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/136078" target="_blank">📅 19:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRYIpw3cw5IiMEl0E5ODgNZmdket3za-tGPYOuxZocUyzztCDdITjfwfI8NOeswdGVP-cxndbmWGrNLzcn-yx_oES2NUIpn_ushmc930oxtf5CCW8c2txMZzz29JcsAsQYRtrC2PfHTa7EKsmA6Xbxq15IIXk1rIR-dcQa_HSqMg5_xcmCn3V38_5S11mu4PK4JvJ9uahA_mYB5QJOYq6uRmoINt041Ii7izR1xEW85RQdA2yANLEhUzNil_tFH6MMIeGaPO4PD_xmt_boPUsN3gw4wQxGpLe8uEt25oaglPLNGuSXAxZMuScdf6Ak9hYPVv4HcmmPTVj-8IhWmoCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاتریوت یک موشک بالستیک سپاه را برفراز بحرین رهگیری کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136077" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2pcvFyC51Aqj6M3WBznu4PFbuCNXC2HWvvek2iGhwvChhUGUtVyKbDQjo98p0j0zQdMjhLBB_Vaz47KhpOkfr5KOtQj6dYuATrkRGk4tAy94eAzhmONDWFS-uISIoZkbsYBiqHk6VxCJpVQUKwVFkLjzLetPm59veeWK7euJZe8RslV5E5gK4zIOYOyyDlDxmrrr_FO80oHom4mLVuXfaPUEiP2oUV0be5oGzHYtgt-zc1UOA7madFCIog_Bxh9ZBqsqq8e1xbCmhR6kRx2Re3vpMubaaCM3GQFbscuy859olU01haa9HWJHgusZ7GaUOn_ITWteER63jfQg_xYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
⚽️
رتبه‌بندی جدید ۱۰ تیم برتر فیفا پس از پایان مسابقات جام جهانی.
@AloSport</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/136076" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defffab074.mp4?token=kIBgylHh8zU7CVq3GXk7fSPPkcbS8xN3upjiMXcJLdzGDKFVYNTlzA9DDr3ldoEHUuNx8hDlOy2_Rb4r0QS7mueT2kZPZLkoUJGC2aognDxjpnmL0omdwEPqDCK3EAv2Z9P4UwFyFhOxKvCq4UCLLXwlKudJ74hKE0kMadugGqLa_RgB27b6jJopjHmXGfA3Kg-VAazMSmQ2-1xRrVmQmXC0nzPXj-WzIj7Xssc7Z4qn6wOwcjvQZg5YuLSfpB3ISA9ffx6SJmvUbIqpG6PowoLS2L7wes3zcb1X2Vi545u8SpWFf9RGfLWrt_PBwg2KWpuSMCEi7qvy27674ome8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defffab074.mp4?token=kIBgylHh8zU7CVq3GXk7fSPPkcbS8xN3upjiMXcJLdzGDKFVYNTlzA9DDr3ldoEHUuNx8hDlOy2_Rb4r0QS7mueT2kZPZLkoUJGC2aognDxjpnmL0omdwEPqDCK3EAv2Z9P4UwFyFhOxKvCq4UCLLXwlKudJ74hKE0kMadugGqLa_RgB27b6jJopjHmXGfA3Kg-VAazMSmQ2-1xRrVmQmXC0nzPXj-WzIj7Xssc7Z4qn6wOwcjvQZg5YuLSfpB3ISA9ffx6SJmvUbIqpG6PowoLS2L7wes3zcb1X2Vi545u8SpWFf9RGfLWrt_PBwg2KWpuSMCEi7qvy27674ome8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سلاخی کردن جوان ایرانی توسط حرام زاده های طرفدار حکومت تو بندرعباس رو ما فراموش نکردیم
🤔
سگ آمریکا شرف داره به شما حرام زاده ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136075" target="_blank">📅 18:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرنگار الحدث: پیشنهاد جدید توافق میان آمریکا و ایران شامل توقف خصومت‌هاست
🔴
پیشنهاد جدید توافق میان آمریکا و ایران شامل اجرای تفاهم‌نامه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/136074" target="_blank">📅 18:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136073">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d3c1d446.mp4?token=Bm3G9Wrcg5peSFlDV83gRjM2VqfWNtayUt1RE5-Rm9xdwhO6Y_zbZ3k9iqjrW3hwMWpJKKyFqctOBoL_n2qdlasUXm-nY2k8XH3oxHZrh8jYhpS7kVNX3ExTRATmXApBpE2EUeT6c3Ih7t8h55AN-XzbYFngxZxeKB7FaexQKUMYYRVX9UT6oyEih1PqbDWB9NU9fpoKKP4SzjOahCabpKuS_VIG6yHFEHANFrRuUFyhuSSvmNK8txiPoKJ0YK7B4BwzpEJRFlYclDmPkub0XyfWUo-bQX29gc1fkzt6WAiuSpvepi6s0aIVuEHrHCJsWIc5d-R7yXq825j9VUkKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d3c1d446.mp4?token=Bm3G9Wrcg5peSFlDV83gRjM2VqfWNtayUt1RE5-Rm9xdwhO6Y_zbZ3k9iqjrW3hwMWpJKKyFqctOBoL_n2qdlasUXm-nY2k8XH3oxHZrh8jYhpS7kVNX3ExTRATmXApBpE2EUeT6c3Ih7t8h55AN-XzbYFngxZxeKB7FaexQKUMYYRVX9UT6oyEih1PqbDWB9NU9fpoKKP4SzjOahCabpKuS_VIG6yHFEHANFrRuUFyhuSSvmNK8txiPoKJ0YK7B4BwzpEJRFlYclDmPkub0XyfWUo-bQX29gc1fkzt6WAiuSpvepi6s0aIVuEHrHCJsWIc5d-R7yXq825j9VUkKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرمربی نایب‌قهرمان ده نفره جهان اینگونه با گریه از مردم کشورش عذرخواهی کرد، مثل بعضی‌ها از حذف در گروهی جام جهانی دستاورد نساخت و پیشنهاد مجسمه سازی نداد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/136073" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136072">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxax57wR9ZEg67CZfFK3Q01o10GhCxc_GzDII_1llcoD_f7aVxgcEQVnLT_HZ3A4Y-WgR6n6qCd1pfxvXp95h29vetLslVHea17Y0vqnZJ0OspE1stp0LfWpIX8RMuTsNZDwEqfYquQUzRgL-cG4KvHbIFQoZa3QwDfMgodX68QNe1UTYYbwF6oDnYAjpVpRbJhHYDYkpLihhac78gN_R9PRPQJ1ymuG2GlgKm-ES87OZlJZ7-yAUt2RS7oqlco1tQ9gyt1zyYMp4-P7OViWp8dbUFekhjZOCL_-GTY0LdwF9cNpHpC-v8ZymKkHMKr_YFS8DWw5rlhQTwZZ8jvW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرکت هواپیمای عراقچی به سمت پاکستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/136072" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5o1cxNIKxf0lbLJQSX4fB9mXJWiszoH52UH_CLD6TntdBeZbken_OO-64R5PoDALCZb2QCC24QrleA6BP0XN1J77EWMuwrJrarFA2rQFfwLblEgYxqIX8IxwN960hgGiZ0nM4yDmnU0kIeQToyrWh533vZuMgbmuSstz6-y8KcbauXVIpH1AX3kYyCETl2KTuE7oeUf2h0adzoCSUhdSlh3oeqvrUttHscmOvi9wIkWWvqPpUXvq1AnAPkIjTLyqqQJBXaE3tfKaUIR9XbRNxKkmM9IGyVRKZngF3i7Ox5Ho0l_hpll7JiBEDEOOEOGLV5rhJQjToPPjPyKZ2I6aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ یه عکس دوتایی با لیندسی گراهام پست کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/136071" target="_blank">📅 18:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
یک مقام اسرائیلی به خبرگزاری Axios گفت که عقب‌نشینی نیروهای دفاعی اسرائیل از مناطق آزمایشی در جنوب لبنان از روز سه‌شنبه آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/136070" target="_blank">📅 18:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
فارس: دولت با ناترازی جدی بنزین روبه‌روست و گرفتن تصمیم دشوار اقتصادی طبیعی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/136069" target="_blank">📅 18:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
صدای انفجارهای مهیب در جزیره ستره بحرین شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136068" target="_blank">📅 18:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfRiXpaBLS4HEDlG6_1-XrqlAeAQ_6EA8eKLOX4lLOpdeA_BJb_lF8Ob20amEX-mlaQq4YV_WsW5hub6khwcqGkPF7e6cw5LJJg8nFx-uKlxYPWwnseGYCXSSK-mcxD8ec54fqjfusKl-YtR2iFJz-RkYwZyAjBxSH-1XkYpPScmUdA4pco88R944vnT1dMT7diFpAYWFPzpBKS8VSHvLXDuWLQRemFLbus015ixqno8yVVqp3AQz4ysKySB7jmWW_1rr3NX6PziTDDoYrgnLpHDjUxUMDhBpC0hqNdwh0JVa3R5BpBfV9t91zD2v64Yrmkd22uszM1Jx72_liicoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمون شیراز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136067" target="_blank">📅 18:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
العربیه: دوباره آژیرهای خطر در بحرین به صدا درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/136066" target="_blank">📅 18:31 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
