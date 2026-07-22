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
<img src="https://cdn4.telesco.pe/file/DGuTU-AmW67wLSqyIDJBbm3N1Yt4345HJCPahSokEtGFL2nxz_nFxcuQXC-snOYwJGdCjrU_2dX7F7EJQn2RrftnuCmwwQcY6MwdD2d5mekoj-XLSw2oUVVxpteKCXj5HPLVI2inDzVXggJ0RFHHTS5jEaZkimS5TUxizHP1AQ6Pvza9kXKvJSN601ICXyzY6JsJ2I_GYDRbRxm2cqARdVcKb4W61OmWgBfWavYEb6RZ7J8adOIjw--tY6MAyBW3fuKS_9LokFTky5YjEQ2sg6poWWpaHrjql-ctA1DARqhB_kmloUNF1pYWTtDky2rErLtEZh-zqB0qT5ptF0b3dg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 11:22:12</div>
<hr>

<div class="tg-post" id="msg-136580">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7b2d9cceb.mp4?token=eqO1jO7NQP1-FbE8sjx6IOl9ZVAF1aJ4sQceVrDYTfbbgLLGppaEb9qpxMFWXMiXBRvW_zgSDNmvnMbPX6aYa7XAP1aCG6O8xpmIn_klTThKZCWOh4RFES0EcASK78Aix7qyEFMzdbnkBAoJtqHsoLOht1-8zRoVtChZemNJHjjkNQRCpg6JX14JAO2sNnS50KbMHFDiSADzavALnaYhIr9-SG8H_EA-ekEfGvHD6pCqnSrAG7xY-7Dhuprw2dbfmCf2gSAmfT_cptI8nmFkxJugx6KU7WKLFLrTiLmUDf63M1OFtpAo1Ax4Mt_llnsqpr975b28Cs_wc34rbV_Bog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7b2d9cceb.mp4?token=eqO1jO7NQP1-FbE8sjx6IOl9ZVAF1aJ4sQceVrDYTfbbgLLGppaEb9qpxMFWXMiXBRvW_zgSDNmvnMbPX6aYa7XAP1aCG6O8xpmIn_klTThKZCWOh4RFES0EcASK78Aix7qyEFMzdbnkBAoJtqHsoLOht1-8zRoVtChZemNJHjjkNQRCpg6JX14JAO2sNnS50KbMHFDiSADzavALnaYhIr9-SG8H_EA-ekEfGvHD6pCqnSrAG7xY-7Dhuprw2dbfmCf2gSAmfT_cptI8nmFkxJugx6KU7WKLFLrTiLmUDf63M1OFtpAo1Ax4Mt_llnsqpr975b28Cs_wc34rbV_Bog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور جان کندی: «آیا ما توانایی نابود کردن هر آنچه را که در زیر کوه کلنگ (Pickaxe Mountain) قرار دارد، داریم؟»
🔴
پیت هگست: «سناتور، بخش زیادی از توانمندی‌های ما محرمانه است. اما اگر در این دنیا کسی بتواند به هر نقطه‌ای روی این کره خاکی که خدا آفریده دسترسی پیدا کند، آن نیرو، ارتش ایالات متحده است؛ قدرتمندترین ارتش جهان. همه‌چیز به گزینه‌ها و موازنه میان هزینه‌ها و منافع بستگی دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/alonews/136580" target="_blank">📅 11:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136579">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
انفجارهایی شهر العقبه در اردن را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/136579" target="_blank">📅 11:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136578">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqnUb5bC0p2Gae4aHuBSpJM90Odj0Sgg1qz1j-vMQz_bbRP-fUTHEUv7C4HihJSiS9Szp_vToyRLsv022gsOlP25IBdiSwiSWRKbU8nWc4yokwnz_LLTmwqzUzwFxvfDZrW1cHGLycVxSjhnGNz0mG4qRblridwy0w0c941Oq_Pr0EW_qyibhNvJMFCWy7ROKScfpXC9h_mdeq4Vju3u55WMuXVqcw9rPz9HDCJ3MMi6tySOCRXBn9VHcAUEHfEOsbCFbDhMLRKK_6RU83b6mw6I77Q7g11lw_eR8WMB7M6mPlhPIxY25-v3vwyp9PzanpDiL9Bb9lcnb9TqPc_uzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رد دو موشک بالستیک در آسمان تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/136578" target="_blank">📅 11:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136577">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
رئیس پلیس راه استان قزوین: مأموران پلیس راه استان قزوین یک دستگاه تریلی حامل ۴۰ تن بار که توسط نوجوانی ۱۵ ساله هدایت می‌شد، شناسایی و توقیف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/136577" target="_blank">📅 11:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136576">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کرمانشاه رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/136576" target="_blank">📅 11:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136575">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
کرمانشاه رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/136575" target="_blank">📅 11:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136574">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: مسائل قانونی و شرعی گواهینامه بانوان حل شده است؛ مقدمات آن در حال انجام است و به زودی شاهد اجرای این قانون خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/136574" target="_blank">📅 10:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136573">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ستاد عالی آزمون‌های وزارت آموزش و پرورش: امتحانات نهایی پایه‌های یازدهم و دوازدهم از فردا طبق برنامه برگزار میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/136573" target="_blank">📅 10:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136572">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">طلا بخریم؟ نخریم؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/136572" target="_blank">📅 10:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136571">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش: ساختمان‌های اسکان و رفاهی و انبار تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات پهپادی قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/136571" target="_blank">📅 10:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136570">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZGhyNs8uKG5WfW0njiAA_2fIvtB6dD509NqBChgid3E0p7UkBdVQx_E-TuMnF3LLnD_RLYt8HDN6jqwJ2Fu7S366rhgyVnrRRFx7QlwWOZfuTCtiaAY8eHJOTPTPbgWP9SRNZftbUHuZIKv9xN8bm8VrszLfeHFbl-pfjYIdNXwb1ybSBTH0tqNfq2agGwDj9mPUGQh4gbKpk5q__bqVzjDsagPUrtrXspBG0umjA5Q3CwKJj9pRoNQv_v142l3evE-_Wo-bMZlE9q-5wwfEdme-V2N3mhmO4rMPXIt3lCOebNl5V4ITOXs_ureHBAYcW6vt3raPiJoP8QPsY3j5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری یحیی گل‌محمدی در حمایت از عادل فردوسی‌پور
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/136570" target="_blank">📅 10:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136569">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c927f960c7.mp4?token=K4iOFilGEio_lhccpp_ZN6NDlG4zWJJ9KTHAwHWJ81-yadqrvlBXWWWreeUQagIHyFmboOv9jm-zw6MoYp47LQyay-Imp8SSlzzeo94Vjfq7gYEdsBxZb55TSEXksiD0FL_jleshdtEx59UGPvo99dcELAdCS5o3stJpxfBhaAAXXmefjaCVfzkMVABXnYS7H0Q0BcLjacmvwgPZU9MZ86YWzPJOZ9heMVUjb8OcnM1FEQdOdKk2H3nNzCh3TkpVEyuv_rwztepR-VrnlmORr9wdlGb0c_wEbHCWziUEhJK3d4BwCTMdmZClCXwn6zDPAQWdosGSMN-LonwyhJflCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c927f960c7.mp4?token=K4iOFilGEio_lhccpp_ZN6NDlG4zWJJ9KTHAwHWJ81-yadqrvlBXWWWreeUQagIHyFmboOv9jm-zw6MoYp47LQyay-Imp8SSlzzeo94Vjfq7gYEdsBxZb55TSEXksiD0FL_jleshdtEx59UGPvo99dcELAdCS5o3stJpxfBhaAAXXmefjaCVfzkMVABXnYS7H0Q0BcLjacmvwgPZU9MZ86YWzPJOZ9heMVUjb8OcnM1FEQdOdKk2H3nNzCh3TkpVEyuv_rwztepR-VrnlmORr9wdlGb0c_wEbHCWziUEhJK3d4BwCTMdmZClCXwn6zDPAQWdosGSMN-LonwyhJflCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای تهاجمی اوکراین صبح امروز دومین مرکز توزیع و انبار شرکت بزرگ تجارت الکترونیک روسیه، wildberries، را در شهر نِوینومیسک هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/136569" target="_blank">📅 10:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136568">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
صدای انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/136568" target="_blank">📅 10:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3yG0gIr1Yr-Y7NNi5pbZE7tCcXCQwhE9t3lAA-35AjrB8bYj3zMkI9HvTVkG6E-77Db-bgurLLK4te_z1DPv10e7YY5wfJ-zivUMH96U3DUDFbGDsn21eKmaqlfQc0PBhJxDhKomkQ8ysLmCmboONDZAkySjgiggp80y9FbkNP_9J9KJfnw6A5KfnEEA2ZeodLhjC7W2vdu9zl-Du7lpUZOmVmqu1zO2WkFNgtYUJfi1BJ0jW_kM5RS2tFAbqG60-cEgXlT9kymoDZjK1umPRHcZRb5ifXPrf6u2dr7wf5pDZrFYPjZZDs7ZWO6bSD27WAp-ifFnre7QE8iM9FE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۹۳ دلار رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/136567" target="_blank">📅 10:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
شرکت هواپیمایی هند بار دیگر آغاز مجدد پروازهای مستقیم خود میان تل‌آویو و دهلی نو را به تعویق انداخت و تاریخ جدید آن را تا اول اکتبر ۲۰۲۶ (۱۰ مهر ۱۴۰۵) اعلام کرد.
🔴
این شرکت دلیل اصلی این تأخیر را «ادامهٔ نااطمینانی‌های امنیتی» در منطقه عنوان کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/136566" target="_blank">📅 10:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rqw49vlzUwBQAIwF053D_xt5A8WkwmowRkAn3X6lGsTQAo-SNo5ieoENWlO100lW51ykrjutCvvycRW1iHLlQT0JsbOtqipthCZ1dAsW8vIIWngvEcVpL_ZZ9gVH9WoNOY_47M9cRRNpHLtOJHf-TACfkz3y-pUS_9MdFG9xZnetSm22A_SVhRgRicFuLSQ9mNKQY1RbKpwoiYkEnq_q75e2jjDwd_VvI9zS9_EVl2C2sjJnIvfnWYDzopr3QvvvoOZXv4MHAuEC92_ngfftztR_Wn_mFraJyIKFbKMKRvKYu7_zqGbdjuWip18bkL9RRfNOZX_GJTRMIdip_tEqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پنتاگون اعلام کرد که سروان آنجل ایس رامبرساد، یک سرباز آمریکایی، کشته شده است. این سرباز پیش از این به عنوان مفقود شده گزارش شده بود، پس از حمله‌ای که نیروهای ایرانی به یک پایگاه نظامی در اردن انجام دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/136565" target="_blank">📅 10:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBCZiaCLiGjsMku8rEksSEUXox5LIThMu2rMdGF7dEAQn0AAszulTZgVjXDUVWBPmxmY52t1H_Uj8RYAvLNEFDNGsvf1EQ6DSdWGUtpJ37GlTvd73nD5_BQAOeIddguC_rEDAbEU90cRRQh0AJrMbkWnxVfWxHYtppx6blXxpXZjoqkHmeXe8lJy9AEFTCbCFzCCZY2GTrEPnvMYrwutPsmUq-pfPXjBG1eePGdF5ZDJFrkojRp8E5EiSyccOJzVcq6Ie2RLdzk7-ywUBiOe6FAAE3tIgJiVESbJgbkuuN9nifcD3GMK7dqwHLlU8pS5lH9uw5fgWUPIIscogKuXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnLHE2HC1Lv2Y-M7s5rGwum9apt9DgPEEBSCljd2mmpSMXPqARRtE6cSAmjPMmK3a9zYSAaQ8ZQOtpJtU985TQVfqqcMLc39JgVnyj5xiWH9D8qtncOEUh8PR-ilCN0STP78zfHonJBnpUskj__MyhQIJI-Hm0uneLVM5YfldRXHZmXGonQxNxCHWv_T6DbD8klzLbZIKDIBHXPVPVuA1mz6hAV36T5xJG80DFGE2JBhgE6ghGV0QrM3jTarog3rQi8g_nhTL3T94HR9gMltVL7xid81OZLV15iiyGF70c3l3zKOuhwtZM6Y18gtfjD59WBN96dqX9Ut9zCwym9ZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kgegl2ChGkbI4NCCoe1Kk076I4Bsel7Pg0TyWieyuzF1jiIXzysfPpuuVUEloy80Y9W3YdmyT9VQ5QsWeL5zFNTDFFuRQGRmfAZINXpC0TJWlEKLXohb05tGejaXaHavVZW3c6rmKS7bmCKQL0aBjRx3rNdAHDojVRxsDJzbHJNQvp3V-fMGXT8ZWPZf3_jznmwpLnl_pRcafkbW1g2rM3xBHWy_dWPdS5g1RtOGHB5K4bSlAItmTEYPS71yCGzwhqHh6ROFj3Wr3WYh3RGIy7mTzyKRg2NnJ3DiC0c5MSZ-eSadf6lenyDz0xsSM929vSy41kO6yg33852_3tXlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKAghcrYdLZqWp-ZdaCDLpGo4fhv-JPS6K964_nvjTKoIwnnaSfq9FvqAbhzyGipwaagCZgS3zsqNpCORODTXb-FlJG7_9GZ-y-Gs3itPxu4ys0ZSaVr6EFUe-GTMDyOu-XapmS-6pkbgyNLeATIPvkJwUb-CFCEldLvPSf_2_IzHLLoyKR0i2-AtAEEMSyc17K6FZljHww7m31XjQbnmwJRxzb8SmHru_bW_v18MC4gtTktF8PXWJiU7Ufx7xQX7rbBlYNmMTzAUSrpIGWYjHbVq4LvL3oMWePeXSrLTJgAP3bP0hPTSD6v6Y0bSyX8qciXPuIG50-qY_SSPfshwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwDJCu9XZ9LrvqN5WIw4NIfu9hSS_GbLd1sbovM6_BRoXts6XejFUEw0peNSSwyVcPZxv293t1dl4pYxYB0VjSKtC5wPCWWdiMwMfFTLiHTQDJ9hl4GVxncirsRtlQQHzkyszgbq6kPc8sSZREgxXT0Rkxb2mfLH6KFVfV4PWVmFj0n3LSgwkfL9E3Olof55dXamjdJC4MTAVj80KQ4du-USt-TLcf9rmwdB7-wNOeq9TgBOPIWNw0qzJmrAy8XC5BRKSQr_v8hkreIXYHIH9vuaewV06Ma4nUOh56_te2DxccIH6zmURYM2uVf9uLWQViDYpI-Bw_eL3Gbl2LPIxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از دیدار دیروز ژوزف عون رئیس‌جمهور لبنان و دونالد ترامپ که نشان میدهد این دیدار خیلی دوستانه بود و دوطرف از این ملاقات رضایت کامل را داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/136560" target="_blank">📅 10:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebb0efc2d.mp4?token=NQAC1zzjGwDmE_SbdK2qUEATGmFD4aVYcLg7D9sXV0IzF6qaVeRWDuJGK8nbiybz2vsJC5U5JPDyXg9tbRedZon8XCAtmGg-w-V0dwxBsqVXqFQlvwjEUC8jtWuy7NadywRKckJkdVELkpM5FMmGTsBEpUo7svF7SViQuyPa9oOif4Qf4RdTbhDD-wSRowLc-ob9_6Uy-pjMuayojxr9-rNMhn398bxJvFX8T_Vrm-KFVTKoHfXkMr9bEReo9B7uM04CZOarHjOYlOtJixoI88aziYLHy-d3QDzW35mX6pbrYYjNK6-aSKGK0lND5JcNLd1yGGi-1uGyaSiaemPz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebb0efc2d.mp4?token=NQAC1zzjGwDmE_SbdK2qUEATGmFD4aVYcLg7D9sXV0IzF6qaVeRWDuJGK8nbiybz2vsJC5U5JPDyXg9tbRedZon8XCAtmGg-w-V0dwxBsqVXqFQlvwjEUC8jtWuy7NadywRKckJkdVELkpM5FMmGTsBEpUo7svF7SViQuyPa9oOif4Qf4RdTbhDD-wSRowLc-ob9_6Uy-pjMuayojxr9-rNMhn398bxJvFX8T_Vrm-KFVTKoHfXkMr9bEReo9B7uM04CZOarHjOYlOtJixoI88aziYLHy-d3QDzW35mX6pbrYYjNK6-aSKGK0lND5JcNLd1yGGi-1uGyaSiaemPz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم سنتکام از حمله ارتش آمریکا به چند قایق در سواحل ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/136559" target="_blank">📅 09:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
شبکه CNN گزارش داد که لاشه هواپیمای «پن‌ام ۵۲۶A» (Clipper Endeavor) پس از ۷۴ سال در بستر اقیانوس اطلس، در نزدیکی سواحل پورتوریکو، کشف شده است. این هواپیما در سال ۱۹۵۲ سقوط کرد و تمامی ۵۲ سرنشین آن جان باختند. این سانحه به‌عنوان یکی از نقاط عطف صنعت هوانوردی شناخته می‌شود و زمینه‌ساز اجباری شدن آموزش‌های ایمنی پیش از پرواز و بهبود دستورالعمل‌های اضطراری در پروازهای تجاری شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/136558" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZJCKGdp6hiUhyM3EhfcMGLgbX6BzjuNdtIkopYXyeLM90mt7YLJQsaCkSDngO-YQKOtnInPS7s5L5oeC1vdob_6m2Kx6HApWojRAZBdz2DTumqMG_9SbLbNSElbSBzeQlxm-r2J2_KlnB0J7SHeees-OUgnv_hGsoxMiqII9SoFNREjtvFou4-g5ZtZKOZdxnaTLr9z2n5avLydBAEbUu71wI5xUKnh3s-1Y3xx6HErF0UQvRnx1d22A-sdRosnPLBz2w-hv3etS739yyLs5i0k0iZD66ISuyexM_VdXS6BT6bcdH3SGRaMu6RMRnljGv_Hc7FjvsfXqnf_cxGs8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برآوردهای گلدمن ساکس نشان می‌دهد صادرات نفت منطقه به‌تدریج در حال کاهش وابستگی به تنگه هرمز است.
🔴
بر اساس این برآورد، در مقایسه با آغاز جنگ، روزانه حدود ۵ میلیون بشکه نفت بیشتر از طریق خطوط لوله و مسیرهای جایگزین منتقل می‌شود؛ روندی که نشان می‌دهد بخشی از صادرات نفت، تنگه هرمز را دور زده و از مسیرهای زمینی به بازارهای جهانی می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/136557" target="_blank">📅 09:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پست جدید دفتر شهرداری نیویورک: زهران ممدانی، شهردار نیویورک در این ویدیو تاکید میکند که نتانیاهو جنایتکار جنگیه و بمب های اسراییلی با پول های امریکایی ساخته می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/136556" target="_blank">📅 09:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ادارات هامون، زابل و نیمروز امروز ۲ ساعت زودتر تعطیل می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/136555" target="_blank">📅 09:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
روزنامه اصولگرا:  برای مقابله با جنگ زمینی احتمالی با امریکا، آموزش نظامی را شروع کنید.
🔴
لشکر جانفدایان را سازماندهی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/136554" target="_blank">📅 09:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma0YLkfbtUpKya5q0cwN_vdgH6rlfX1Ll2Oa9aU9uwOnzmUYPSfT5njEnTVw1z7r5KIZarHH-xSJ8C1lE-YK-3swah5s670BWCOlATobvjl5nrjksxkNMnkluWhVlLthkBZrng4AXxVrTfM03zY1m7TCvmiwg9A5_p9t_iEeNMD_eg2jsZF0X91w2NzWGOeiK1T9d1Gok6t8LWLYJlGgeDR2rbx5v3NykLTePIqYH8klKQJQP3Zo9DqNNmUED8aBzvXScY8WsIkL8upNI8W-3T8HebdBsaWjEx04jB9K319bK3kCFfnE_Il9tWxf4hynIArNORrht6vJICvWjDHJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نقشه حملات دیشب آمریکا به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/136553" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136552">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29c9d9b51a.mp4?token=UF99OPSG6UegS4ZGKPC-s66u2buRsAwbQGuYODRC2AFgj_dscJO5v-UcApFC7UOEk1o0zscSmWv2_Ix5L6bH13XwQp01noInRPP5SiNPp8WEIJWtTicWZeBs6IqtnPVeZZVdZUi7SapDhI_JZqUD4m1b9Od4gzqjBbLMzSzx8J1vfbOxXRWf_ftZ5O3i_g2bssaLbOGS1SyBmX9FdDZDUZE0geB1vggqwwLi5n2H_LD3vDGzbPGjLXVxmM97zBgjdmKhpsyQCSlpH_-cuQPy6VPLyNyzOy1N-L_5S-TqaiC5GE4v5jwy9vHuuclk9gwyUs0ufvds7ZeNGNM5R_pEkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29c9d9b51a.mp4?token=UF99OPSG6UegS4ZGKPC-s66u2buRsAwbQGuYODRC2AFgj_dscJO5v-UcApFC7UOEk1o0zscSmWv2_Ix5L6bH13XwQp01noInRPP5SiNPp8WEIJWtTicWZeBs6IqtnPVeZZVdZUi7SapDhI_JZqUD4m1b9Od4gzqjBbLMzSzx8J1vfbOxXRWf_ftZ5O3i_g2bssaLbOGS1SyBmX9FdDZDUZE0geB1vggqwwLi5n2H_LD3vDGzbPGjLXVxmM97zBgjdmKhpsyQCSlpH_-cuQPy6VPLyNyzOy1N-L_5S-TqaiC5GE4v5jwy9vHuuclk9gwyUs0ufvds7ZeNGNM5R_pEkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید دفتر شهرداری نیویورک: زهران ممدانی، شهردار نیویورک در این ویدیو تاکید میکند که نتانیاهو جنایتکار جنگیه و بمب های اسراییلی با پول های امریکایی ساخته می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/136552" target="_blank">📅 09:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136551">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خبرگزاری سی‌بی‌اس: هزینه واقعی جنگ در ایران بسیار بیشتر از مبلغی است که وزیر جنگ، بیت هیگز، اعلام کرده بود، یعنی 37.5 میلیارد دلار. این تخمین، هزینه‌هایی مانند ساخت و سازهای نظامی و تعمیرات پایگاه‌های آمریکایی که در اثر حملات ایران در طول جنگ آسیب دیده‌اند را شامل نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/136551" target="_blank">📅 08:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136550">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835169113c.mp4?token=EWYy8s4Y86THTG7uYkE3z70t4Ygi8iq01k-8NWcJ9A6qOXOE0-6SvosQ5yayW8JaCEOZ--6AWZp6qJEhsb0VI5OcqjurjNQ45YZm5GJRaEHlfueN067Dgfrlg2Cd6KcdVVsZg6uZH8TbLyTEvHy0Q86Bxw4WBfaM8qUgGp16EwP9TPVYhc2DBhEEekRzBEPX5EeYqLSEMzFToe7DHAtrSopova6JX_E3NoFdf6q5xe7oMkgrWPnHBO6U7zYnbixEEuLXetUAYHO8wNOtPhlCiAht0yzYZuAz-OQpThLUlGd1Ey2VssB-f6f6R9FDu1xYXU_WPW2WpXsCmKXS8KRS9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835169113c.mp4?token=EWYy8s4Y86THTG7uYkE3z70t4Ygi8iq01k-8NWcJ9A6qOXOE0-6SvosQ5yayW8JaCEOZ--6AWZp6qJEhsb0VI5OcqjurjNQ45YZm5GJRaEHlfueN067Dgfrlg2Cd6KcdVVsZg6uZH8TbLyTEvHy0Q86Bxw4WBfaM8qUgGp16EwP9TPVYhc2DBhEEekRzBEPX5EeYqLSEMzFToe7DHAtrSopova6JX_E3NoFdf6q5xe7oMkgrWPnHBO6U7zYnbixEEuLXetUAYHO8wNOtPhlCiAht0yzYZuAz-OQpThLUlGd1Ey2VssB-f6f6R9FDu1xYXU_WPW2WpXsCmKXS8KRS9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور دموکرات، جان فتِرمن، درمورد قصد ممدانی شهردار نیویورک برای بازداشت نتانیاهو: او یک جوک تمام‌عیار است، هیچ اختیاری برای بازداشت نتانیاهو ندارد.
شما شهردار هستید، آقای [ممدانی].
زباله جمع کنید، چند گودال در جاده را تعمیر کنید، راه حلی برای مشکل مسکن در شهر خود پیدا کنید.
🔴
شما اصلاً در جایگاهی که فکر می‌کنید نیستید
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/136550" target="_blank">📅 08:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نشریه «وال استریت ژورنال» بامداد چهارشنبه به نقل از مقام‌های آمریکایی نوشت که ترامپ توافقنامه همکاری هسته‌ای غیرنظامی با عربستان سعودی به مدت ۳۰ سال و ارزش ده‌ها میلیارد دلار را امضا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/136549" target="_blank">📅 08:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpSKUusXqLax1h6ImI221GKwBrGz-PrTmuX_NSuf2HdBLKrp-Mtjg6VQhXm1zq88CuQPu5R9l1J1BwRqcC-WYG6rlj8Kx0puT3lN_Rbq-cnFB87OFy8rXmoD8k5JZCOcskU_eiLBQo2A5gOAykQ7B34GRWMwiqmbda63QcB3dc59mk1BwIH7fQz06kr_iLibZmsGbfx-n8ex5tzPKoDLJ1XiFoXBcDrwULQ3TDzn2-3DEKA8so1mvnPqFxDHx0HeNI1eISTzL0UJSDmJUxgurgWS8sk6Vfhv7WrCneNKwkkXpGEG7nMBpwcljfhCU5sDE4MPAG1ULjgRWrlnzOqd4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعداد بیشتری از هواپیماهای آمریکایی مدل KC-135R/T که وظیفه سوخت‌رسانی هوایی را دارند، به سمت پایگاه‌های اسرائیلی در حال حرکت هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/136548" target="_blank">📅 08:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار در نهاوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/136547" target="_blank">📅 03:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
انفجار در آبدانان
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/136546" target="_blank">📅 03:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
انفجار در ابهر زنجان
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/136545" target="_blank">📅 03:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
انفجار در الیگودرز لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/136544" target="_blank">📅 03:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سایت اتمی طالقان ۲ زو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/136543" target="_blank">📅 03:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
پدافند تاسیسات نظامی پارچین در شرق تهران شدیدا درحال فعالیته
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/136542" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پدافند تاسیسات نظامی پارچین در شرق تهران شدیدا درحال فعالیته
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/136541" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جنگنده از آسمان قزوین رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/alonews/136538" target="_blank">📅 03:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3f23e865.mp4?token=N61KQxWuptSCRHqYtViNXT_KnCF5rGJirMm9xqzyAlxD7ihMhxTG5o5DqqoqpiP1F87bbInHn_jsTU-M4zX29Y0zyMxtocAzMQnol-SD_F1H9ttXvkH89k93PV2i9Rb0FQdB5dQsYnu70G9M6pu3YiNpMZLElEZRB2hlrgX3UulsvLUtWg9c75N09GTrIZYxTnBqAAhUHXs6IiaYI3jRvHTuN910ImQ-3fRZJJPUgPW00AUa1IUB8jyOM17FYDqZwu-C4RItqcbGTmQHUYhXT-Z_f_JkWT6mwBzg0Pg0ALkpdGcScRhj0sePijC5zQFlq6zrWYO7u7CrkAhKtJii2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3f23e865.mp4?token=N61KQxWuptSCRHqYtViNXT_KnCF5rGJirMm9xqzyAlxD7ihMhxTG5o5DqqoqpiP1F87bbInHn_jsTU-M4zX29Y0zyMxtocAzMQnol-SD_F1H9ttXvkH89k93PV2i9Rb0FQdB5dQsYnu70G9M6pu3YiNpMZLElEZRB2hlrgX3UulsvLUtWg9c75N09GTrIZYxTnBqAAhUHXs6IiaYI3jRvHTuN910ImQ-3fRZJJPUgPW00AUa1IUB8jyOM17FYDqZwu-C4RItqcbGTmQHUYhXT-Z_f_JkWT6mwBzg0Pg0ALkpdGcScRhj0sePijC5zQFlq6zrWYO7u7CrkAhKtJii2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/alonews/136537" target="_blank">📅 03:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
خوش چشم: آمریکا توان حمله به تهران رو نداره برای همین داره جنوب رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/alonews/136536" target="_blank">📅 03:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دقایقی قبل آمریکا نقطه‌ای در شهرستان کنگاور استان کرمانشاه را مورد حمله موشکی خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/alonews/136535" target="_blank">📅 03:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پدافند کرج هم فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/alonews/136534" target="_blank">📅 03:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b55cc12d69.mp4?token=gviYY_gK99dzwuGMBQj3Cxq7My2xuDZP1aGJbz946cOlgCdcGKBM-NAOKuzuDcoHnWAy89XKlFsWGPIgyB-2Ii_lSZlYFuFtJ289QFCE_wvmxP7c8h-DlJhxjzp2X0eMPdYnp6jr8Ekzzl3FDoavLoau3uq8hB2pdRrdLd9jA3pH1-eQgXJwGvKDbiR3exDLcDZ36KhP0AtiS3BUfcDKKg3e3lU_ddNhdVIlaeK651gxHAXIy1Rn3WcGvxzpH3pZI9cJ1ElWfUTAvavSVzO-nqT61UNfGS1otctHOpnXIxPi-BJMWTOG-7jCH8by9g5AtkVxefJnWd2kSJaVObZMyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b55cc12d69.mp4?token=gviYY_gK99dzwuGMBQj3Cxq7My2xuDZP1aGJbz946cOlgCdcGKBM-NAOKuzuDcoHnWAy89XKlFsWGPIgyB-2Ii_lSZlYFuFtJ289QFCE_wvmxP7c8h-DlJhxjzp2X0eMPdYnp6jr8Ekzzl3FDoavLoau3uq8hB2pdRrdLd9jA3pH1-eQgXJwGvKDbiR3exDLcDZ36KhP0AtiS3BUfcDKKg3e3lU_ddNhdVIlaeK651gxHAXIy1Rn3WcGvxzpH3pZI9cJ1ElWfUTAvavSVzO-nqT61UNfGS1otctHOpnXIxPi-BJMWTOG-7jCH8by9g5AtkVxefJnWd2kSJaVObZMyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت شدید پدافند در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/136533" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
انفجار مجدد در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/alonews/136532" target="_blank">📅 03:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فووووری/پدافند تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/136530" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b2530c00.mp4?token=MxbrCXxInQsF7cYi3Gu9fWEs127ikYOBZjFpHht4wli8Yr7JQQb6sv-R0Sjg23529sbf8uQVJEVVhOL5jDk5kqOLj-emB6UjZo6fC4FdDhj1BHGjYvYA4nT-htFIr3MZ6tmAiUtIomezPug4p_LWvFQfTyrc9ED_KHPNFir3201nYtvlhtSWY-MViiSPukr_m05qYKx4CSqXa3BmpM135yeFlIJJmbKU3pjPkucmtKhhfgdq018cP1AeE81vHOL7c_0iNV_iE0Pu3lYxsm4166-XUkH1mz6YYmT6G_ZnyAO0i8leDTXe5l5MoY3hKgLlvfQRHZ2T9T-TccDE39gnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b2530c00.mp4?token=MxbrCXxInQsF7cYi3Gu9fWEs127ikYOBZjFpHht4wli8Yr7JQQb6sv-R0Sjg23529sbf8uQVJEVVhOL5jDk5kqOLj-emB6UjZo6fC4FdDhj1BHGjYvYA4nT-htFIr3MZ6tmAiUtIomezPug4p_LWvFQfTyrc9ED_KHPNFir3201nYtvlhtSWY-MViiSPukr_m05qYKx4CSqXa3BmpM135yeFlIJJmbKU3pjPkucmtKhhfgdq018cP1AeE81vHOL7c_0iNV_iE0Pu3lYxsm4166-XUkH1mz6YYmT6G_ZnyAO0i8leDTXe5l5MoY3hKgLlvfQRHZ2T9T-TccDE39gnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات امشب تبریز :
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/136529" target="_blank">📅 02:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
بوشهر رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/136528" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
همزمان جنوب و شمال غرب زیر حملات سنگینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/136527" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
چندین انفجار سنگین در تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/alonews/136526" target="_blank">📅 02:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/136525" target="_blank">📅 02:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
انفجار در امیدیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/136524" target="_blank">📅 02:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/136523" target="_blank">📅 02:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/alonews/136522" target="_blank">📅 02:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/alonews/136520" target="_blank">📅 02:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تهرانیا تایید؟
👍
👎</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/alonews/136519" target="_blank">📅 02:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/انفجار در نارمک تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/alonews/136518" target="_blank">📅 02:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWsBvTtqe2iQn3VWCqhZqOut74Yhz4wH_MWsOsmJRnu7NM_GZquu5JgDOc_VRCKIea_uY7p_07vk5-6fdr6K0a7theLGZWuqxgca6EYyPhHsihkvqyPwA4XckHfQn1bHi3ykA5fhQnljnKhwEvQS9GOzH4r13mGPV7FujspSUiffrO_W22uNzMoI7IWPd_nPHNpuRSzGU8jS4mbVxPzQcrI50l29MTBcfVi948s8hjnIM65GAfwT2P-XVKXgx2gC-VSKfkYsvjwDC8PA5xt8dnzik5MYhUgA-c7HEqL5OgUnINwRLQnX1eDwwFdHshmlWgWtwbHTWMP1J2TVL6jOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک پست:
ترامپ، می‌خواهد اینفانتینو (رئیس فیفا)، دبیرکل بعدی سازمان‌ملل متحد شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/alonews/136517" target="_blank">📅 02:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
خبرنگار:
آیا فکر می‌کنید ایران با تهدید به بستن یا تحت تأثیر قرار دادن تنگه هرمز، تلاش دارد بر انتخابات میان‌دوره‌ای آمریکا تأثیر بگذارد؟
🔴
ترامپ: «
احتمالاً
. اما آنها هیچ تأثیری بر من نخواهند داشت. من فقط کاری را انجام خواهم داد که درست است. من به این موضوع با این دید نگاه نمی‌کنم که "اوه، ما در آستانه انتخابات هستیم." فکر می‌کنم مردم بسیار تحت تأثیر قرار گرفته‌اند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/136516" target="_blank">📅 01:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">استوری دنیا جهانبخت از حضور در مراسم عزاداری.  وقتش شد یادی کنیم از ..... زدن دنیا خانوم جهانبخت برای تتلو
😂
😂
😂
◀️
◀️
مشاهده فیلم</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/alonews/136515" target="_blank">📅 01:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
انفجار در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/136514" target="_blank">📅 01:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvHbkLTvKVraKTdWHuJpQPvmdyabOuqtkTOQ0Gu2edc6fknHSXF_HyzTsZ4c52SoPZPsDKTWDq1-m4lmSI3Vu30I5sr6mUfv9lrLUsK9aFBLJshaQnrkb1uvabWoIKGwyQF8NJqvTfH5-6WyUovvK18l75LG94c_tTzQm9KPbgRG0zHO1rySg4oZlh2U5AuXra16JYDet_m-0c2KksiSHEoeFlFL4d6_yHhDrvHNi2bXdZBqKurN5D0GZTJDcFHCKyplM96EculrHGA3LvVQuzxxGeYuF4mTrTjn7ZVN4cyvvJgogtAD2zzcDAMQhjrH07ofak6kCs0dcECnyqiygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور قالیباف: دیپلماسی به پایان رسید، جنگ بن بست شکن است
🔴
هیچ ایده راهبردی وجود ندارد، احتمال حمله متجاوزانه دشمن به کوه کلنگ(تاسیسات صالحین) نطنز در ساعات و روزهای آینده وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/136512" target="_blank">📅 01:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">طلا بخریم؟ نخریم؟</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/136511" target="_blank">📅 01:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
به کویت حمله شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/alonews/136510" target="_blank">📅 01:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aed34ebad0.mp4?token=UFhCoCf6scwt3AQilSCqlgrbYUmPOOtFkgAZS5LVZ3qE75uWdADBxGCgAf4HxPi2vc57iC7cc9bqe5rKLo1ZzqMuxdOgzgOYEjS1plYyaQYcrPOe2DfzgARgCCC-VKgni9dUv5wUEzEMWp8jv6_a4kZ9W9kMAgL5c0jeEgtSoXLx8QQt8F_w2gX6tbgxDju-ZYs11HWajuNx3EqlqFb9MwYgY6a2SMVqMsmdK3d1otRXAUhTFHXvaKpJgk5m3A7w_HAb-r_COrHO3Y-Xi_LitKncoKyNeWSkclWIeg3t3AICfgSOiZMxXPvsj0jvXHrKx-9VcX_abHHJgpuwdrGj1jn0AR7-kOHi1AYKfOL38oEyp9uXSgNdDMyDqlByt2L_5fSxz5JBw2l0WUqE99EcKE5yuhBqOONIh5hSYWUFcf00BcOIIavPmZ0th3SAbY37FOyp7ICEhsE9HS7BfT1KcDVe7hHdNV2MPFefqpMq8LuEvX9QUKP0oLTtGVj2jP71nhewXxGLSwi3jHXqqTEswlvjIEuaM1k5PB4RZEWa_N42XohqGRm4eEiebrN04xyvkk2NkrxDpPLVlZ_HwBRq66-pcPZq9cG0ThnKZFLcHSH-V07Qn3ATes_3oihJsx1FF_uMmrWzINHaLsVOmbkUkhIZB-2eqDHZq8iiNC-oaGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aed34ebad0.mp4?token=UFhCoCf6scwt3AQilSCqlgrbYUmPOOtFkgAZS5LVZ3qE75uWdADBxGCgAf4HxPi2vc57iC7cc9bqe5rKLo1ZzqMuxdOgzgOYEjS1plYyaQYcrPOe2DfzgARgCCC-VKgni9dUv5wUEzEMWp8jv6_a4kZ9W9kMAgL5c0jeEgtSoXLx8QQt8F_w2gX6tbgxDju-ZYs11HWajuNx3EqlqFb9MwYgY6a2SMVqMsmdK3d1otRXAUhTFHXvaKpJgk5m3A7w_HAb-r_COrHO3Y-Xi_LitKncoKyNeWSkclWIeg3t3AICfgSOiZMxXPvsj0jvXHrKx-9VcX_abHHJgpuwdrGj1jn0AR7-kOHi1AYKfOL38oEyp9uXSgNdDMyDqlByt2L_5fSxz5JBw2l0WUqE99EcKE5yuhBqOONIh5hSYWUFcf00BcOIIavPmZ0th3SAbY37FOyp7ICEhsE9HS7BfT1KcDVe7hHdNV2MPFefqpMq8LuEvX9QUKP0oLTtGVj2jP71nhewXxGLSwi3jHXqqTEswlvjIEuaM1k5PB4RZEWa_N42XohqGRm4eEiebrN04xyvkk2NkrxDpPLVlZ_HwBRq66-pcPZq9cG0ThnKZFLcHSH-V07Qn3ATes_3oihJsx1FF_uMmrWzINHaLsVOmbkUkhIZB-2eqDHZq8iiNC-oaGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست : من دنبال بمباران بی‌حساب نیستم
- می‌خوام بمب مناسب، در زمان مناسب استفاده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/alonews/136509" target="_blank">📅 01:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O71v94k5NuUlcHWa8mtpd1xem9NRaPcS7r7oRUs7gYsVWKJFZ5XElfV-HUDQA21aHc2QF0931X44AE7dWgroCKJG1z3ok6BAJOhLRBwhgc-87ywZC0WNq18CcVMN4JmZrozTvr2HkpPO9X8fRqvA6qmRWV31eYigRMRbPygpveD3_efQ4ygRspqCR-7bVI4oO0O-A0oXvlyw4AwJvjeakpBGRUZGkCQy7BzGgXysUCQ5AS1AdlUJ6DeRoNUprosudFQvNsESsWP4wdc0kTodMoVqNL6oamVqHxXULqpVBpjocuyBKB3UkoUEkJRUmcU28IB1TFS6cPxNFkAZPn5Dpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تاسیسات اتمی کوه کلنگ با هزینه ساخت Nمیلیارد دلاری که بزودی نابود میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/alonews/136508" target="_blank">📅 00:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967f594caa.mp4?token=htNojYV1GtP0mOKBBfyROfhGHTTHJb5gRT_qnA0uT2AL_tVCm9zA5jI6k_Dph1VK6oUcEgDV59uWkecZe2A3JoMZ52VB1lVfQ0nfWLPoo8VKcEQx5VBaFfJQ3aTEBQuUB7pUe0TD23KmkkECWgRt1EpWYl7D0KApRRU38ev-PNJ0Sas8NjpsP2otBTV2Nei73rkAcWA8DQR9W-gB9wXNESPaFbOIK6nWENKQW-56w4DcPLLqkm71xD_0aiP5yxbwRpROPWH0ZSV0XkA8zhl69EFHxE34aBQnzvMBWl7S1O_6pTV0F2N8vWY66kpLtc0af65dF_wshzNdxoYBTp7CWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967f594caa.mp4?token=htNojYV1GtP0mOKBBfyROfhGHTTHJb5gRT_qnA0uT2AL_tVCm9zA5jI6k_Dph1VK6oUcEgDV59uWkecZe2A3JoMZ52VB1lVfQ0nfWLPoo8VKcEQx5VBaFfJQ3aTEBQuUB7pUe0TD23KmkkECWgRt1EpWYl7D0KApRRU38ev-PNJ0Sas8NjpsP2otBTV2Nei73rkAcWA8DQR9W-gB9wXNESPaFbOIK6nWENKQW-56w4DcPLLqkm71xD_0aiP5yxbwRpROPWH0ZSV0XkA8zhl69EFHxE34aBQnzvMBWl7S1O_6pTV0F2N8vWY66kpLtc0af65dF_wshzNdxoYBTp7CWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست: ما این جنگو شروع نکردیم، ایران 47 سال پیش این جنگو شروع کرد
🔴
پ.ن: ایران‌ نه! یه مشت عقب افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/alonews/136507" target="_blank">📅 00:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
هگست :
- ما دیگه وارد جنگ‌های احمقانه نمی‌شیم و دنبال تغییر حکومت ایران هم نبودیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/alonews/136506" target="_blank">📅 00:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
بیانیه قرارگاه خاتم‌الانبیا:
آمریکای جنایتکار مراکز هسته ای و حساس ایران اسلامی را تهدید به حمله نموده است
اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله ای بشود، آن را به عنوان توسعه جنگ در منطقه می دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/136505" target="_blank">📅 00:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💢
فوووری/۵۰ هواپیما سوخت رسان آمریکایی در اسراییل مستقر شدند
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/136504" target="_blank">📅 00:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwM0n920otYpHMGm38kcB61dVRmICw-7u8TT7SFxKiSDxzbvFUga-oNbY301ANBZ2yxfr63-TGgj748su5QTYTdZ9nxx5cuxJhv-cNIG6i_7donUPZ5X3IkGOBDsXPpN3sBaFnhhiMOL0bRtEqNu-EcbqIqhQ5LIt7kkqWMJv4fYZcQ2LCerJrRmf63LQ_UUhCvpE9vezSHRGaCz7PWpsAuUF3uEgJoGFVnr-uJG70B5_gDHZ1EGEHdpBGfZBZGBekAMmfrznEAhfLnA8s4y7utGetqGfeK7uNlj98byo4PGFSb-MwCz8YDwogFr9zAzyhm_9DEdM2qWlYraGRM2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: آمریکا توان حمله به تهران رو نداره برای همین داره جنوب رو میزنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/136503" target="_blank">📅 00:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس: دولت پذیرفته است که فعلاً هیچ‌گونه اصلاح قیمتی در حوزه بنزین انجام نشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/alonews/136502" target="_blank">📅 00:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDqTR35M3tg6lO2x7a27eOkMSRPn0YgnjN6eJYlwWzRRgR3-G0Evdj2GlcxmkpWxwyFCjjIAuvssusD5Eywy3PmyqZkTZe8piDVjUcxIMCr74YTH_Q2pbU6xnAXpZofEoTHJgi7xnhm3VYlZ4Ev3REmzPx2He_UgzDbGlceFfiw1qX679zigsTm-fdHbQQ2Fhd3w0NhfVgbIn-L8uJndqEYJK4wb7jRlC5RHsvZm2tZ8L2NaKEbUcXR_exg54zULUEUpaQTmevjpujdIrO8I6w5PP6dY7UpJ3rG7Z5CaH8n77JWywujBKItCoQtww6gzKqlWC-WO2MPnYWztOWfUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۶ فروند هواپیمای KC-135R/T Stratotanker نیروی هوایی ایالات متحده بر فراز اسرائیل و اردن در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/136501" target="_blank">📅 00:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: روسیه و چین در سطوح مختلف به برخی از فعالیت‌های ایران کمک می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/alonews/136500" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: روسیه و چین در سطوح مختلف به برخی از فعالیت‌های ایران کمک می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/alonews/136499" target="_blank">📅 00:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ff20b1bd.mp4?token=kjEjTMTiEPReNn5SnaFqSOz_qIaIJEfWiXbIpanqCpz5mic-tPZUqXFFrsFT_iYdaytUkNr1YN-J-4oOuGnKHPZLsoMp70ThcHxpxJKMckv7iOEqitJNBybvTqZfSNFsN7HELZBjywDb50SQc_ced9eUNO27LYYqNSvtNiXMPjKE_jfVbkP09mrz6VlQKVFXvoJIFfNMRC5FdWa79-Y3Ir8JOL-Sa74VNxPF8vdyJdxOXGiX2nen7Dp19uP2u5FxSsY59sI1263yMtopVNNyugojLXZioKJw-bihwL3bwcTHnKYTyoeggA2Ist4GeuDX9mXhtFclOCWdLkkVXaZToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ff20b1bd.mp4?token=kjEjTMTiEPReNn5SnaFqSOz_qIaIJEfWiXbIpanqCpz5mic-tPZUqXFFrsFT_iYdaytUkNr1YN-J-4oOuGnKHPZLsoMp70ThcHxpxJKMckv7iOEqitJNBybvTqZfSNFsN7HELZBjywDb50SQc_ced9eUNO27LYYqNSvtNiXMPjKE_jfVbkP09mrz6VlQKVFXvoJIFfNMRC5FdWa79-Y3Ir8JOL-Sa74VNxPF8vdyJdxOXGiX2nen7Dp19uP2u5FxSsY59sI1263yMtopVNNyugojLXZioKJw-bihwL3bwcTHnKYTyoeggA2Ist4GeuDX9mXhtFclOCWdLkkVXaZToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آه مردم ایران بد یقه جمهوری اسلامی رو گرفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/136498" target="_blank">📅 00:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953ccf337f.mp4?token=DEGlQO2VnCZydkrDJgfslJacHUACYqEQlKnUTsUdwwgsrB-waAqJ1jFiyaF222AINHH-ttGB3PUP_4fTUmv7iQwcBjci6Nt4cmmJHp7ueQW1UFdUWeKf_a9g3uowim9ejr3sdrpaHQPfce0i6i9RVFtJ1A123z1ryTK1NwFQ9JJq8y7UnCXdTRwNWvN2Ee6V8H-nCGM8-BukVCCGF1AoFxkgTwgvQvDJZek7BHyVa_e6r8Ut-tQ-kSikav3GQNDg8wPkXRnNS_JqdUKOREF9__9IHapXEZDW-5edtu51ajppC04apQJG5jel3vS8PFeGBAuoXOQZCRJOSFBiS6M6TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953ccf337f.mp4?token=DEGlQO2VnCZydkrDJgfslJacHUACYqEQlKnUTsUdwwgsrB-waAqJ1jFiyaF222AINHH-ttGB3PUP_4fTUmv7iQwcBjci6Nt4cmmJHp7ueQW1UFdUWeKf_a9g3uowim9ejr3sdrpaHQPfce0i6i9RVFtJ1A123z1ryTK1NwFQ9JJq8y7UnCXdTRwNWvN2Ee6V8H-nCGM8-BukVCCGF1AoFxkgTwgvQvDJZek7BHyVa_e6r8Ut-tQ-kSikav3GQNDg8wPkXRnNS_JqdUKOREF9__9IHapXEZDW-5edtu51ajppC04apQJG5jel3vS8PFeGBAuoXOQZCRJOSFBiS6M6TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معترضان ضدجنگ در جلسهٔ سنا، سخنان پیت هگست را قطع کردند، آنها می‌گویند: «بمباران کودکان در ایران و فلسطین را متوقف کنید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/136497" target="_blank">📅 23:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/136496" target="_blank">📅 23:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76819af5e7.mp4?token=QtENzswrRdsGMzpzH4Ctg6PHg56QTyZeH5HrR8pn0A6goiP2mjpLTwVI_qmA83yTSHpJONwlALxQG1Z9nMIRKzMk3Tn7zYXWUUYRuH472ERLFpVzBhTr7AtQC-nt0zZLMcBznq0-om43njVoccJcAGhar6848bK-7Ek0Yt5dbKMi7Da2b8u6jv9LzBtQzI2dJOtckF9mGnTCpBBzZ0eFnd4PSV6NYMvKD6U_TiJpLXTaxfU6qazQMKpN7GW03c7DjYoQEtM1f85xhzbRMWUTz-iNiQmt_7KigQWg-CBHSlTSav6YR0hYdtV2inXQVmuVDSdkq5KQ9of0MStb_wZ_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76819af5e7.mp4?token=QtENzswrRdsGMzpzH4Ctg6PHg56QTyZeH5HrR8pn0A6goiP2mjpLTwVI_qmA83yTSHpJONwlALxQG1Z9nMIRKzMk3Tn7zYXWUUYRuH472ERLFpVzBhTr7AtQC-nt0zZLMcBznq0-om43njVoccJcAGhar6848bK-7Ek0Yt5dbKMi7Da2b8u6jv9LzBtQzI2dJOtckF9mGnTCpBBzZ0eFnd4PSV6NYMvKD6U_TiJpLXTaxfU6qazQMKpN7GW03c7DjYoQEtM1f85xhzbRMWUTz-iNiQmt_7KigQWg-CBHSlTSav6YR0hYdtV2inXQVmuVDSdkq5KQ9of0MStb_wZ_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست: ما باید دونالد ترامپ رو بخاطر شجاعتش تحسین کنیم
🔴
اون نمیزاره گروه های افراطی اسلامی به سلاح هسته ای دست پیدا کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/alonews/136495" target="_blank">📅 23:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما در حال حاضر محاصره‌ای مؤثر علیه تمام کشتی‌ها و بنادر ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/136494" target="_blank">📅 23:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-2LgnMZBaaLEfu5ISeD4lAemUdXk2rBrHq35E8FRAABvsAKj6HeAaa0oAt2OrpjwRcFQokXCndd9OwNzWm0cAwVEli_N-zb_dv08RRToq7pJdehpzbZfF82ym1YhKsmHdmhFRt0JojwxBYCGLXHfSR6B_hCT5hHOee5D32gXrlZ6-5YYncsPOqCM61BimUwVDWJn_NUBFihf4HnBPlVnIEOZvHqxtQxrNg-vhPUJ8_YH49V05U0LHwZ1rjejd8PaD7QaL5mwO-SI9hCDsWoZa4GPBV1njAPeJGNmy3t9Y1g6qkSfwZdPstNcO455TjxCknpKFtdGOt1n3MRviSfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲۷ درصد نفت جهان از تنگه هرمز، ۱۱ درصد از کانال سوئز و ۱۱ درصد از تنگه باب‌المندب عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/alonews/136493" target="_blank">📅 23:39 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/atvFK_kWTtlnfDh8kJIayreunHiXGhELeoOwdhnK2VDp4FV_rqv4tXwXbuIm8JZlHIF03qf-_za8o89FlB3_4GZH0WxsI1XjK4YXPJ3kis-U0cZxS53bdVJtDcXTRJavNCV7oU0yWJiX_tVZDdDy3ZTxXOQOhMKO4h2ZgzO9OlquZV5y1yf-fX7piaiEov3S8J1llkgDxln71iFNEV-qGrXjMt8rFKsYMdNWEnx96UK28g3T2nc_GH3UsPtt-47KvSxgTzA9dB940ODBeYqHq0kI71lgj_wr6ZJgl7dbE2wCKO5MeXv5lmsXKqeT5F_CUoMUE6ILIuOMxATx42P3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای E-3B Sentry AWACS آمریکا در آسمان عربستان سعودی
🔴
سعودی‌ها بارها مشارکت در حملات به ایران را تکذیب کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/alonews/136492" target="_blank">📅 23:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
هگست : جنگ در ایران برای آمریکا حدود ۳۷.۵ میلیارد دلار هزینه داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/136491" target="_blank">📅 23:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRzJGsKvbl1U66cHtf6HQVO7BueERNRSCotx5sLDjeuUoFheh9FNsGtJEf4p-EInqPJAeDegTarAQxOvpjPmuvjwTDSvhQvcO-zmR9VwL9ElOa-FCx_vmfxU77SzZcgYSJ4dnh3i2E1Yl8_kxP5vzfoCzntU03MOsmxJTG8Pmmr7knf59tLULBrgMjxcX1MaJ7VjbdtUKS9KHAq3eL8iQYzJbVRkaAJ1IqFUDZxZ8Qfk722suM6DVW19L2hx5nInq7RoraoWont-UESCbiJcw-Eo-VSOcZOsCzeWCcV8HGPitRev8_MTzjL2HzmH1_74Zd6ccGP-hVuCVpWZBqvlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
🔴
جنگ در افغانستان: ۲۰ سال، ۲۰۰۰ کشته.
🔴
جنگ در عراق: ۹ سال، ۴۶۰۰ کشته.
🔴
جنگ در ویتنام: ۱۹ سال و ۵ ماه، ۵۸۲۲۰ کشته.
🔴
جنگ کره: ۳ سال و ۱ ماه، ۳۶۵۷۴ کشته.
🔴
جنگ در ونزوئلا: ۱ روز، ۰ کشته.
🔴
درگیری نظامی در ایران: ۴ ماه، ۱۸ کشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/136490" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29916de006.mp4?token=H357Iu0z5kp14kPnF-w6Nm0UOACgIDrSQA65O37LyxI-sLDoNwJuiqWYC7V1NVxrBxpo2-iUdKSiQnG15yCqagGqVSCHBk7ICBi-yazs3JHLMaSw3_2T396Em2BjUorl2HDONOW0xNpd7whMKFL4lo8CnGRNRCB40brsUU-SEZs2YkOHu74fWlYYQhygg4-YJn3GGqsg9EtW1We-_ZEAh-66N-up--wvRz3zGtY3mV1tbLNbMvGJXoXDwWyqf6V9xzAmt-vf7bWd6rhLj0dT0a_r4jU5phC0m-FYVLg4RP4IgOu83X1npkQA19K4RcV6p5iemLHN4oman9sqUu2V_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29916de006.mp4?token=H357Iu0z5kp14kPnF-w6Nm0UOACgIDrSQA65O37LyxI-sLDoNwJuiqWYC7V1NVxrBxpo2-iUdKSiQnG15yCqagGqVSCHBk7ICBi-yazs3JHLMaSw3_2T396Em2BjUorl2HDONOW0xNpd7whMKFL4lo8CnGRNRCB40brsUU-SEZs2YkOHu74fWlYYQhygg4-YJn3GGqsg9EtW1We-_ZEAh-66N-up--wvRz3zGtY3mV1tbLNbMvGJXoXDwWyqf6V9xzAmt-vf7bWd6rhLj0dT0a_r4jU5phC0m-FYVLg4RP4IgOu83X1npkQA19K4RcV6p5iemLHN4oman9sqUu2V_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ:
ایران از نظر نظامی در ضعیف‌ترین نقطه‌ای قرار دارد که تا به حال داشته است.
🔴
من اذعان می‌کنم که آن‌ها همچنان از قابلیت‌هایی برخوردارند، بدون شک، اما میزان خساراتی که ما در طول این مجموعه عملیات به آن‌ها وارد کرده‌ایم، آن‌ها را در بدترین شرایطی قرار داده است که تا به حال تجربه کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/136489" target="_blank">📅 23:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/695fafa7f7.mp4?token=k8eA0_8GKNUCvlMzv5f2p6BG4WtrAHUQC9klwZIJtteiVHx-q5AuSVlV5ctFIuT8W4r1UABaLrMYRpbDLLJQpyudYA6FWzprUnl5Pci30KYFuE66pS0sNqNvG-L-tlUGTiDuWNX0vj97D2zfjPFZGkDK-577AC0dhkYgpY-bqpPkv9YNH-2Opprz3FOYFM6uOJM01MDZvYyAPsjNsNQD6a45KHwWhW_AXjCQ8_diPgt_nPnIWFc4bZ_Hy0sRCVFy6yhEuNzWTzdBJXt7bricaVReCyhUPokEasCP8LwE6wdpPhMGlPRMsenwk21Bl8iyxouSMIMPBwYOvxIo6-iXSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/695fafa7f7.mp4?token=k8eA0_8GKNUCvlMzv5f2p6BG4WtrAHUQC9klwZIJtteiVHx-q5AuSVlV5ctFIuT8W4r1UABaLrMYRpbDLLJQpyudYA6FWzprUnl5Pci30KYFuE66pS0sNqNvG-L-tlUGTiDuWNX0vj97D2zfjPFZGkDK-577AC0dhkYgpY-bqpPkv9YNH-2Opprz3FOYFM6uOJM01MDZvYyAPsjNsNQD6a45KHwWhW_AXjCQ8_diPgt_nPnIWFc4bZ_Hy0sRCVFy6yhEuNzWTzdBJXt7bricaVReCyhUPokEasCP8LwE6wdpPhMGlPRMsenwk21Bl8iyxouSMIMPBwYOvxIo6-iXSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگ‌ست، وزیر جنگ: پنتاگون دیگر توسط کارمندان دولتی اداره نمی‌شود؛ بلکه توسط نظامیان باتجربه و مدیران برجسته کسب‌وکار اداره می‌شود که این بخش را مانند یک شرکت اداره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/136488" target="_blank">📅 23:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136487">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بحرین: هدف حمله جمهوری اسلامی به منامه سفارت اسرائیل بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/alonews/136487" target="_blank">📅 23:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136486">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / خبرگزاری کان اسرائیل: نیروهای احمد الشرع، رئیس جمهور سوریه، در حال آمادگی برای حمله به حزب الله لبنان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/alonews/136486" target="_blank">📅 23:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136485">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvLz1kUwLsID-_eShgRlyIP3vbriLOx9JVPu8bfNWHYVgKxAPRNdhbu-I9Bbpu4UO2I9St0TNktPlOHoVwk9OaQ3hcfwFx8MxI7vLREvEWACHS45rCBN6V1hSR4u4g87Iw4Zq28RK6YV7L4OdiqPmgZpzxqpnYiRtPAUEGAe97BZQIEtPhueXZDVnd_UGXhgAfj1Sh97RB4u-fGEN2tazZvBNRodr1BbrjcMOlfa6VLLs64darQ2OPr9ScdNwlJ15qRcn1bj8BxXIvnEwK-XlAwz1VmYMMxxykrwcTkLYHf_FEKS0BCwQ97GhKsi-QlkgF3SBLY426i82JkuXhUdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: پرواز مستقیم شرکت‌های هواپیمایی آمریکا به لبنان از سر گرفته می‌شود
🔴
دونالد ترامپ اعلام کرد: «به دولت خود دستور داده‌ام که به همه شرکت‌های هواپیمایی آمریکایی اجازه دهد پروازهای مستقیم به لبنان را برقرار کنند تا شهروندان آمریکایی بتوانند به‌راحتی از این سرزمین زیبا دیدن کنند.»
🔴
او در ادامه ابراز امیدواری کرد که سایر کشورها نیز تصمیم مشابهی اتخاذ کنند و در پایان گفت: «از سفرتان لذت ببرید!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/136485" target="_blank">📅 23:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136484">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
منابع ایتایی: در صورت حمله به کوه کلنگ، ایران تاسیسات اتمی در نیوجرسی را هدف قرار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/136484" target="_blank">📅 23:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136483">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_yd9zJ2Ia0uKGQkLtNE1bzE8PDEcZoSV2_LxYoIU4TCa-0tQifO8J19_YkB4TmdrSE11sQCONFJpjbyLvssVzy6OSrWYi5tHCfbF33eZQIDagDnkW76nWbYiNZYwQisz0hLaFvoH0-lBlRMz15KhR4hGB69JZExD8KCErTCHixqkvF_gQhqltmqwDsG8toaq6kjIWkGQ-HdnGTTux_5gcgg4HGo4T8zJ2gMTBTNEiupgep4im23lFpaCtk5pWCgG_5tSdLyJAC9qBA0zSGsSYtUac0-A2wK1wtbjhzTZ9BXgf3IFV8tGKA7xw9sIoO1jfVNrgAeM4POUCLwlJ7fwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بعد از دیدار با رئیس جمهور لبنان، دستورالعملی صادر کردم که به موجب آن، به تمام شرکت‌های هواپیمایی آمریکایی اجازه داده می‌شود تا پروازهای مستقیم به لبنان داشته باشند تا مردم آمریکا از این سرزمین زیبا دیدن کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/136483" target="_blank">📅 23:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136482">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سپاه مدعی از کار انداختن چند رادار تاکتیکی در کویت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/136482" target="_blank">📅 23:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQueWfRIKg6-pe2oX-mZVFzA1OXPUlfssl1yAADaPiRp1fBbKwRQOw4IKd9IYM5aAZ305V_RsAnhFYfeaf4CT_pLwLI4916ZYzWJZyt32PTcUQA951XyLNmNUtom2UVcYFsLNvAFZkb1dXQbyUNxFyOlggdilMLVwxD4hWxnXG7L_Im2-O19wEzBi0QLSbZScyA_b_YcPBZ1wdptkWMiaD7h_BAZtxHT3JfK_00TPC-tmaH_cLWyYo0TLrgO-B5Vig1d-rtzdTtiHq3z970ElrN7RTGN96rwY21XTnXRnHVfTIE2_-vwrSHEQZWFnQUVNHMt722iDFdHLnuMWs_U5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/alonews/136480" target="_blank">📅 22:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/alonews/136479" target="_blank">📅 22:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / نخست وزیر جدید بریتانیا با استفاده از خاک بریتانیا توسط آمریکا برای انجام حملات هوایی به ایران با استفاده از بمب‌افکن‌ها، موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/alonews/136478" target="_blank">📅 22:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
برخی منابع ادعا کردند که امشب آمریکا به کوه کلنگ حمله خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/alonews/136477" target="_blank">📅 22:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/گزارش‌ها از پروازها تانکرهای سوخت رسان اسرائیلی برای اولین بار از زمان پایان جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/alonews/136476" target="_blank">📅 22:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سپاه پاسداران، بلغارستان، یکی از اعضای ناتو را تهدید کرد و گفت در صورت اجازه بلغارستان به آمریکا برای انجام عملیات علیه ایران، این کشور را شریک جرم آمریکا دانسته و اقدامات لازم را انجام خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/alonews/136474" target="_blank">📅 22:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری / ادعای کانال ۱۴ اسرائیل: پرزیدنت ترامپ، گسترش دامنه عملیات علیه ایران را پس از حملات اخیر، اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/alonews/136473" target="_blank">📅 22:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کویت سفیر ایران را احضار کرد
🔴
وزارت امور خارجه کویت : نفتکش «کیفان» عصر دوشنبه هنگام عبور از تنگه هرمز هدف قرار گرفته و در پی این حادثه چند نفر از خدمه آن زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/alonews/136472" target="_blank">📅 22:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvMGLJJjvy-m2oHE0K-pQ4jI8FZA2LWBAS7s7zIyVAJL9xeZWN9Ag3DMavLcykzk44bWdzx0ARgMZzvkRhn3xNNEf4KScY7HLATHbZJpKELyNilABPDhkpSSoX3iAMmF_GuZqGzUXz-kplocT_tCglRpet6eUvd7R0OGnAJ18FDp0sqcxORAnMM2Vjbm78hz1mDAeeFOMY3eohTcQgBfaRn06rQVJvze6G4Pvwz-V4Q3oa0iokqfV3qbckdHyW2TlHGY53KGg2zveHqs3Lt0VZVGZ6q7xkDUAxtvgdTrX8UJ9biaHIJRmuiPy6rtxvci9k8_JqHu5plXC3RiC3uvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش i24NEWS می‌گوید که OpenAI در حال گسترش فعالیت‌های خود به اسرائیل از طریق ایجاد حضور در توسعه کسب‌وکار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/136471" target="_blank">📅 22:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcx9uiDS0D7jD1kQN7QXbwT0IiTbkJwzlURErOwTjFi_LD9AwgiiIEbaVKVn5j0Dd4XGZWYYKk1iAG-uDHpxgLICYhkZeedkhezvuVAfJJsoqyK7E8cLRN0MV3RXfk0Cz27szxpOLl81fqdm0f7WKc0TXTsW-WpGQddQeCoeQfJebre6ngnaGAOq5-dHaymy6XDD5KyDVLAKKipu41yJGMUB6hnA3zMNfjVZUi9-MPbKFKQ2xsiDUgxPWi3hg8K6xH5pMl3KTP7BFe9psTFDxdBMOvu7yOgYxoopwohKSN-TLxo6oRBIAtNYynb8_HzyOsuQtMlxXgc1Jhv0gA_fkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲ تانکر سوخت رسان آمریکا از رومانی به سمت خاورمیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/136470" target="_blank">📅 22:09 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
