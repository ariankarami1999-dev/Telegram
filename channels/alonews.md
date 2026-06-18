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
<img src="https://cdn4.telesco.pe/file/ZtlW37VfZnXBGn-pDwlfbQ-QbkcxYOJrrZO8qIVSPbMekE_Mkmaz6TFb_Bk7NrtTmQBssp5kAoKY3iTAw1LvbMbtVv74rIk2GpZ7DFJmVKMZiI3hwsFiB5gVG-FThpN67aZZeqQs438s_qm-rtaQRaW9SRJ9Ukrj0VbKclcAzEbYfCJbNEomI-EuV7zduPiSOy1dTFm7_KCzL8kf8pK1Qa3VnMght3UQK58_PiVn63vdcRQ9lM-j_1A1X_BaSQtSQ-td8TUwwNwHfTlCPLQO6aSs42qk81A8vOQCWLWKZqTmB__Mvkd5UYvyn9mBbp48SW6ut3UkPCSKipNMHMd1Dw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 966K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-128844">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
🔴
مجری شبکه ۱۴ اسرائیل: ویتکاف و کوشنر یهودستیز هستند و اسرائیل را فروخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/alonews/128844" target="_blank">📅 10:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اسرائیل به حومهٔ شهرک کفرتبنیت از توابع النطبیه در جنوب لبنان حملهٔ پهپادی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/alonews/128843" target="_blank">📅 10:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128841">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29f737682a.mp4?token=TxjjrcmTZ5J0bbic1-xIwgGo_ENLrqlsyOdceBgy_F2me_DiTljYAyoP5rT31uCTQFgqoDNyeGEVUQYyTO1LYi9rEvS7o4Ev-GFXxXuS_hw8j-sZC11-avYUBPTMrG4RvNyW_V9BFVprs2ANIEW0qE7Z_FWqWqTtD-FblxlG4CkH2LVCv9i0MUp8hx-TcwE96swYyji6FetpU8oVuwUXGlTLgDDl9mQE7MEkHMQ7LNqsuuHiIHaV-mvK0XofmGIpQgJwDquIVmuunhPGOwfDyMT1m7-mQ0MX_uqgRtpG65pHzSYXlP-TMubKR0yogCHpPUEXaiSVWAoXIZcskwMJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29f737682a.mp4?token=TxjjrcmTZ5J0bbic1-xIwgGo_ENLrqlsyOdceBgy_F2me_DiTljYAyoP5rT31uCTQFgqoDNyeGEVUQYyTO1LYi9rEvS7o4Ev-GFXxXuS_hw8j-sZC11-avYUBPTMrG4RvNyW_V9BFVprs2ANIEW0qE7Z_FWqWqTtD-FblxlG4CkH2LVCv9i0MUp8hx-TcwE96swYyji6FetpU8oVuwUXGlTLgDDl9mQE7MEkHMQ7LNqsuuHiIHaV-mvK0XofmGIpQgJwDquIVmuunhPGOwfDyMT1m7-mQ0MX_uqgRtpG65pHzSYXlP-TMubKR0yogCHpPUEXaiSVWAoXIZcskwMJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسکو در دود و آتش
🔴
حمله پهپادی وسیع اوکراین به پالایشگاه مسکو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/alonews/128841" target="_blank">📅 10:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128840">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnsDwYWhKTDaG2q4kr__azc7u9bA9FzaPd6b9aKIf7Clq9ghRMbtHhkbVu0Q5wg_iXnTQLfOGyqMwssf19y0kM2Tb9iSN8rKr6QJA5tqBZvfWCEhtMTP6vRZKMRIYtgU1j9ANpuvjI70bMKNEayUrTHWNg1pqaVLf94wCCbLApTHb61svMARpvosP4XFLmy8G6zwo8IyfEaaPEI16fdoWet5Nk2EA46g6SB0Jv-6QaZud0b7LngISuOraC3TCXIxvvdzLJPrDVG2Pp_DtidcFHqqPmD804rzs3xMUJCDHmcj5HaOO8bNSmEYi075a529IeFPkVUY-wTskUMDGsJ4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردند
🔴
بسیاری از محافظه‌کارانی که از رئیس جمهور حمایت می‌کردند، نگرانند که توافق صلح به اندازه کافی برای بازدارندگی ایران کافی نباشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/128840" target="_blank">📅 10:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128839">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دولت سوئیس اعلام کرد که روز جمعه نشستی با حضور نمایندگان آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مرتبط برگزار خواهد شد تا مذاکرات مقدماتی انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/128839" target="_blank">📅 09:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128838">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVEG8YWzDf-iKcYko94aFOGJoKAUwqdbff0xr3-iO5QDbLbKSB7YujbtSA2t8kY8VXtyVSxbl450sCivdzXG5L6pjdxBMCZt3-K8a3_9uINb-rX8iPRMl8GN7Pm20WP_on4VMwRIbM73E2df78AllFz--BlRf51IO6MqUS8pvCygSXPmUXFkN9N5sliPWkuZ54NNBHjzo6-tnt7pefL2H4MlSUOFo27m9LlUjJo-dRQPeAZAqBtXJKImSdqyAy0CPQCUYNIs-Rdh8dNIkVpnCMXpUGR3kTSl29AGf5Py8A-KGCqQ13BRTjOAXs-kgjPt5pQnOE96K7QW9KQJqQdp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور بلومنتال: سنا قطعا توافق با ایران را تصویب نمی‌کند
🔴
محکومیت دو حزبی برای یک توافق ننگین عجیب نیست که شبیه «تسلیم بی‌قید و شرط» است، نه توسط ایران، آنطور که ترامپ خواسته بود، بلکه توسط آمریکا.
🔴
بیش از ۳۰۰ میلیارد دلار ثروت بادآورده، لغو تحریم‌ها، فروش نامحدود نفت، عدم بازرسی یا تأیید کامل. همه اینها به خاطر وعده‌های مبهم و غیرقابل اجرا در مورد تسلیحات هسته‌ای است که ادعای ایران برای پیروزی در برابر شیطان بزرگ را تقویت می‌کند.
🔴
هر چیزی شبیه به این توافق به محض ورود به سنا از بین خواهد رفت. برای اینکه اثر اجرایی داشته باشد، باید در اینجا تصویب شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/128838" target="_blank">📅 09:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128837">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCo9ACtRy0aAHQjbE8rnmoAThQuGU0YJpe5djTIGyuL-RxeWZ1KpovffbBwrqtopBWE1JxabHqZKfjKGIgx__kCpNnBM0ArYjRGX9mU3VuhgxyS5F-VxL94rLx5qnxNHMaRW8aveqVj6Za-V9Ukq-E5syS15D1JMSsl-LwzJs8abvcGSsjz9spYrvq_Q-e4YxQBF6TqKGxTcAfYen_pIKVfIHO4lOYbQXVkPsPoT1bz_3gY9JZTFRUnjXYgo8twDZjRZiFGsTEoI5Uv68IZkF4z-oIfpySg2d5NgIYADIlHHpdQurSt8l5wUoH3G_GXQ9tySUoPzaPWTj2ZbrdlfoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری متفاوت از ترامپ و مکرون در ورسای
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/128837" target="_blank">📅 09:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128836">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
روزنامه خراسان: مراقب باشید در مذاکرات ژنو، ترامپ یا ونس با مقامات ایرانی عکس یادگاری نگیرن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/128836" target="_blank">📅 09:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128835">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام کاخ سفید:
امضای رسمی که قرار بود در ژنو انجام شود، پس از امضا در ورسای لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/128835" target="_blank">📅 09:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128834">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
تاکر کارلسون: توافق ایران به امپراطوری آمریکا پایان داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/128834" target="_blank">📅 09:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128833">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ارتش اسرائیل: کشته شدن یک سرباز اسرائیلی در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/128833" target="_blank">📅 09:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128832">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الجزیره: موجی از خشم سیاسی واشنگتن را بر سر توافق با ایران فرا گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/128832" target="_blank">📅 09:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128831">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات جمعه ایران و آمریکا در سوئیس قطعی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/128831" target="_blank">📅 09:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نفت خام برنت ۷۸ دلار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/128830" target="_blank">📅 09:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128829">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
کانال ۱۲ عبری: افزایش نارضایتی‌ها از نتانیاهو در دولت ترامپ
🔴
برخی از اعضای کاخ سفید می‌پرسند آیا نتانیاهو خواستار طولانی‌تر شدن جنگ با ایران بوده تا موقعیت سیاسی خود را تقویت کند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/128829" target="_blank">📅 09:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ :  در گفت‌وگو با وال‌استریت ژورنال: بنیامین نتانیاهو فردی فوق‌العاده است، اما گاهی بیش از اندازه شتاب‌زده عمل می‌کند.
🔴
در برخی جنبه‌های جنگ، نتانیاهو اهداف متفاوتی را دنبال می‌کرد و اسرائیل به ایران نزدیک‌تر است و به همین دلیل در برخی ابعاد این جنگ، اهداف و ملاحظات متفاوتی داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128828" target="_blank">📅 08:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: ممکن است رسیدن به توافق نهایی با ایران بیشتر از ۶۰ روز طول بکشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128827" target="_blank">📅 08:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
شهباز شریف، نخست وزیر پاکستان: توافق تاریخی اسلام‌آباد میان ایران و آمریکا با امضای روسای جمهور لازم‌الاجرا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/128826" target="_blank">📅 08:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
واکنش مکرون به امضای تفاهم‌نامه میان ایران و آمریکا : این اقدام راه را برای صلح پایدار هموار کرده، گامی مهم در مسیر درست برای هموطنان ما است و به زودی به کاهش قیمت انرژی منجر خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/alonews/128825" target="_blank">📅 08:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee38c0f1e2.mp4?token=rQXiWS81QHlBlVWaR4cSZqcfKG9vTvz_6zLe7YYxJfrE5oOZINcMZkqqHooz6G0kXeLvQYXay_zpMYEJQBTELDtdjgDCzS1oIzqJebrfjBD59H3kwYbuvBIR8xl6p7SFUsecxrPsqk1mJMltxR3MTG2OJnJGR_nsPfoUQx6tLJIuM6LbuXTy-lezFn_XCz6vRHAJWhjAlK5lBcNfjadLXS3W9xF1DsaeG0T9pDSHRCpOk0ZgS2ek1az8fSilLK3FKsfIJwgKjlnzZc0CFhi6jjeTCK5tB-jCWAt8PyY-8aT9msbrUit7diZgGwbjay9iEuv4BRVMnSXPJ6Q6KmSYXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee38c0f1e2.mp4?token=rQXiWS81QHlBlVWaR4cSZqcfKG9vTvz_6zLe7YYxJfrE5oOZINcMZkqqHooz6G0kXeLvQYXay_zpMYEJQBTELDtdjgDCzS1oIzqJebrfjBD59H3kwYbuvBIR8xl6p7SFUsecxrPsqk1mJMltxR3MTG2OJnJGR_nsPfoUQx6tLJIuM6LbuXTy-lezFn_XCz6vRHAJWhjAlK5lBcNfjadLXS3W9xF1DsaeG0T9pDSHRCpOk0ZgS2ek1az8fSilLK3FKsfIJwgKjlnzZc0CFhi6jjeTCK5tB-jCWAt8PyY-8aT9msbrUit7diZgGwbjay9iEuv4BRVMnSXPJ6Q6KmSYXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه امضای یادداشت تفاهم از سوی ترامپ
🔴
متنی که ترامپ در این فیلم در حال امضای آن است به زبان فارسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128824" target="_blank">📅 08:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stSUKwEhqV-xz5gkSZkHUZK51KZasuXV77DKxe9R3igW8ZkieNbGotDCkb0KCe8FYibgqcsbaIFP4e1cbGmM89rn83vE5iJdb78I-Q4mf4xxIikI21DF_K1-1WF12EkfEXFzKGTuk2YNUloR1YQkYSwf4TKzT2g1wOrUHmailq3UaKbjETjaBELR7eHZ-Weg_u_bW8wy6zcEXGCyVNSZXvqbkZNX6JlxorlczHatlMiNaRdnJQ4ReeVEOeqD_w8ZqhOttlu6BCVW7Enl4SkTPrwurTiMsbKcpcxEPvv5s102UjJeiCFoL_jfhthFiSsMZx_reLw8vZks-9fx9d1aUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظۀ امضای مسعود پزشکیان، یادداشت تفاهم‌نامۀ اسلام‌آباد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128823" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7HnN2gBCUXmr4yBfl0xGKMXQt_q0qovVVpah01eY7dd-bzVFx6-_bnLkPxnHO8TTkEtEnY0X9K5ZgbQ7MbImtkGky7hRSGRzxGVipMB8vPGWHqkQcCKv0LwK882kSf-NL1ceb4pRku0Q-LFjGchfZnGZ27F13WO5rPOuF1fpV6QHmi8NWeLptia6YsSdU5ju_2K84CmKaD7vWaPcDn8NKztHmvRtt_WvR8874tid9Jekcm4F1as5yfiIszdh_SxZI8rPygcj00Z-7sieAv2Fx-XLzf12EODJ9shFQ-44DEqmqLFY1znazoOk17eAXqGc_LSrzoqOmr4EGljENn32Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
🔴
آنها باید بتوانند دفاع کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/128822" target="_blank">📅 07:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNNUBrtXAQwVtpDt6K0eDr5Vtb0mvn_pdhwl4mjhWHJfAPhU2H8l2UCHDn5jFOdU9z3b-6RBHN0TjpFjL03ZtsNR7-ZOtzzVWYmj0NpK1sUv70NwM3GIYD0HIQAXBD9fDlmlglyM0-NpghtzpVNCtGxizYzVFsMxUgJvdEplzObUkcrxAcZvVccjtecG_HvaauxwH7iT3mTdbLIn0QUHTmb3P1yGhlH1xM9QZg2EAwoBD5hFY6cCQ5cY3JZN-pHV86ch3tLEzPO0t7jTuhYGXgb5NprYV1KRH-c9HEJrtt_kQWs8IZGvbA6E4Sz6Ll_zDLj_nFdSkmEns0EysLcqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/128821" target="_blank">📅 01:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
هم اکنون ریزش شدید تتر و طلا
تتر 152000
طلا 15میلیون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/128820" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjuSe0Kt2Hy4VZppCpxooyT3NMV2jwoQdlxAPW6YVzHDLjCo2iMD2KL2h8vxKCFZ0TewQXtSCdzYn68sfn6s5Zby-vK0MWrGj46SaokWyTTskCmteXI7nXtvtFbEuPLxjiJFnAfIAskmAM-7sb6MuvdVnckUBMhoSm2lubyh5zepKnAts4-cgT-5mYg78DPssm7673DYvAugw_r2VWVUoiv-ASTwZP9PlhPn_aHGKO8_0Lap4o33phXy81IUQ4HO2-NsNAtUR2CO1JKZphs_3Dr2UDf8ddPipS1nSE4eKjLD3LdxQ-jjkEUPk6ZyPnhtD4QXfq45vLrQYTivlScHxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قاضی زاده، عضو تحریریه اینترنشنال: کجای راه را اشتباه رفتیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/128819" target="_blank">📅 01:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQzWXWzBEJSAddepGlifTe23oI4vqx2biO8i44YI8hdsTnnSwcJvgynr28I9ShwiiQ6MushXLIMHiFJIqiubvOB76t41S0O6Tu2BxruXSIE4rELo7VuuigOQK5vOG5thhX1jztPhjnUZIm657-oYEzN1AUgno6IPULduvfnv8xyJaIsPE9Z_dUJvVHfMidHl6g_JwDRaXBpRkLVzuGCK5JSPRhyMkhmTC6zjcZZYvrt0OFx1QlmCuh1qGNAiIsvoqJUNWACSor5kFszkx5hNrbdEB6_SgyzNpM9XKqegf7L_XAxuEaSF_T7PjJy62U7st5xmQ6zpjmx2oqjzMuARAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: ترامپ شخصاً یه نسخه از توافق رو توی یه مهمونی شام با مکرون تو کاخ ورسای امضا کرد و عکسِ اون توافق امضا شده رو هم برای ایران و کشورهای میانجی فرستادن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/128818" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heztpjVJzGjqiEg6mJPoig0rNG1UGbQ5rtOKHhsHcXbtjAkDTc_cl04QxitRzRr6hGUrfAQ8Vp-liJTZTlQLCzSH1vUD4PlKZr4Kq1jieY8czUss6w384Du3Pa9mEa3qPsXEEaILpsV0_vRhi5B9ZSaBgs3Ms01njgtC_3h117A7H8eqO5iO5jGcxv2HrpuA_nDULXmyTUcCNd9nY1UlAq_IcEUYon0awqAL-ED8megAhXUNmKmcZST_urjlTkjgSJxyDHNDpBl5pMs0QE0y_agjCPKggYLvq5jG81AbupLshyvvgtd_sWyL4BIYE9fGyDPUdI_2FFChh7tClYFPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندسی گراهام: انتظار بسیار بالاتری از این توافق داشتم و فعلا نظری ندارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/128817" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128816">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t646BCiGZqNtXUCe-dRHWY8OfhcZw00CkZLtXFqBZSBDPh4PX8f67CZ9vDPjLeKSTEl3yUrhpzPCuxVIdp1ybW4-0WDHTV7Y25tI6Yda0ND8Su9YK4I20lGTXxeek4b0RAHwHxESZFhi67EFQ759WX4uxCrSlmWFtcYtMhGz3hG5nSeqMTGT1BNyipHre22sVN7rWGdxYE4-BgJ_BTJpmFp5ih69jOeiHNiVD8ORf29Ib9u0VXp0fW_k6_YN7YZ7BzGbmCFPSONN-Ap3O_uIOLSsauMMxQs2H5Fncl4GjTkKI8JMGg0nkJTvEmUjSVVWe2U4eaqxST69B_xLIts83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: فاجعه‌ای بدتر از برجام رخ داده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/128816" target="_blank">📅 01:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128815">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:
قرار بود طی ۳۰ روز محاصره برداشته شود و متقابلاً ایران هم درباره تنگه هرمز این کار را انجام دهیم. اما بعد از تحولات مربوط به حمله رژیم صهیونیستی به ضاحیه و تهدیدات جدی که از سوی ایران انجام گرفت، مذاکرات فوری انجام گرفت و قرار شد آمریکا تعهداتش را فوری انجام دهد.
🔴
در رصدی که انجام شد مشخص شد کشتی‌های ما بدون مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما ‍بس از امضای این سند شروع خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/128815" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128814">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
تسنیم: متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/128814" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128813">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حسینی با یزیدی صلح یک ساعت نخواهد کرد
کسی مانند ما با مثل او بیعت نخواهد کرد</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/128813" target="_blank">📅 00:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128812">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در متن تفاهمنامه تاکید شده است که فقط منحصراً در موضوع هسته‌ای و رفع تحریم‌ها مذاکره می‌کنیم.
🔴
از زمان اجرای تفاهمنامه، که الان است، ظرف 60 روز درباره موضوع هسته‌ای و تحریم‌ها مذاکره کنیم. اگر زودتر هم مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، عدد 60 روز منطقی است  و اگر لازم باشد، این زمان تمدید می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/128812" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عرازش برید خونه‌هاتون</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/128811" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرنگار اکسیوس: دو مقام آمریکایی به من گفتند که ایالات متحده و ایران روز چهارشنبه تفاهم‌نامه پایان جنگ را به صورت الکترونیکی امضا کرده‌اند و اکنون لازم‌الاجرا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/128810" target="_blank">📅 00:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFO5HbXO4lgFmWuY1G8wNSDpkOz7M573joU1wKlp5MHS1BSbz9rDVby98fXsHohSpAEUwpUhrnAhXpCMvalHCp_PTAlA99AuEWCGcZgcQk4KnsXgwwxXTMtxqtLZxZjXWc0orCsuiSM7PXvihD-6fP8EvJT0aHTg1whwBCv40CVz_ZKai7nfMtqy_XSkG2ZMzFtjmJ4-b-8fBRMSMS5qG9xB_4QhipKFljhHn2Wp4dMlZHc7d3lpYhJn2_WzoW7Q8Pq5J9AObquVRi_NUsDFGvapTtlYIU6Ye_pwrOWg8nLFIq5yYpoaJtJtcB4NJll_qk9YaXqE-Rmj3r8KuIwhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/128809" target="_blank">📅 00:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128808">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری و رسمی/تفاهم نامه توسط ترامپ و پزشکیان امضا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/128808" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128807">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
فوری/بقایی:  الان که با شما صحبت می‌کنم احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/128807" target="_blank">📅 00:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/بقایی:
الان که با شما صحبت می‌کنم احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/128806" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128805">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=p2kHAz_NjyATW3eNBWpUCboW1ZChAIurtNIHI5zy54NdIK-htp0s9esfzhiuZdmS12aBWE0CdN8rUvOsjYkyzOlp9Qx6_KPUvzR66r_ugiwTT__ccDyrpgnnlPHyNBd-zLHODQa8jMv2vZf-XqiWVGx0CY_C0E5pN-V9fuvYBKFVTjaKQB_dxqbU2n6wQaymheWlWTf9LhViJmhhsxQa6LoztiXvofZymNtsmf_tPrvgvsSdtGP-OO-0vBwWGBMKKpgJI3hHUFnIPboRRX2pKKC04mo21-IeV8wJ3NZsmE85JO7eG7RX96YidGMY9rImEUohPKfLuLF8ZJUzB5ahPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06cd39a29.mp4?token=p2kHAz_NjyATW3eNBWpUCboW1ZChAIurtNIHI5zy54NdIK-htp0s9esfzhiuZdmS12aBWE0CdN8rUvOsjYkyzOlp9Qx6_KPUvzR66r_ugiwTT__ccDyrpgnnlPHyNBd-zLHODQa8jMv2vZf-XqiWVGx0CY_C0E5pN-V9fuvYBKFVTjaKQB_dxqbU2n6wQaymheWlWTf9LhViJmhhsxQa6LoztiXvofZymNtsmf_tPrvgvsSdtGP-OO-0vBwWGBMKKpgJI3hHUFnIPboRRX2pKKC04mo21-IeV8wJ3NZsmE85JO7eG7RX96YidGMY9rImEUohPKfLuLF8ZJUzB5ahPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/128805" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128804">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سناتور جمهوری خواه بیل کسیدی در مورد تفاهم نامه ترامپ:
ریگان در قبر در حال لرزیدن به خود است....این بدترین سیاست خارجه آمریکا در چندین دهه اخیر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/128804" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128803">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf1d3e6ee.mp4?token=b3HYtOzwwpzR4ZPBkIANU6HvacX-rzE9Yaj74ku89k4bXQoifwl5zFYPRUjQe0ZBl_UDq-sa_3ebwOeeEkU-8DEefmxZjlEcYtAkhEDWj0RUxAR2GdgM6FvkULXdfbyPp7aAxNkIPJKE8P8YjqpeBs-2rNzdCteqXSsNG6h_LCNRB1IjAeADVWCvW0zmNvoQ8AHNOk6R9YPdcdbpDJrj56ID7NYI9wkZjsLgRkNtRCKobDNVsnjRrkRlWTr15Z6D5WvaE4OV-DD0-Z-_a9--HhRTBpzTGQISLEbNA3JHus1FQqzblGDlIZrC7Eowr-gu3WQ0-nOI8eAcmn2YtxHJfIjXxKxZPMqFEf2ig-I3MrWU0BcibXyn6gsjq1vcfyhyyyuvuCaK9Jsqc7RAHvozrEq7KcSbVcKgnP2USm65_QHW9_dr2A51M13JZUV0togadV9B3ILP09zSrWZetoY8rpuj7BsFgUwvGK8NoGhNqSl4Kg0iQ7FTjIqqf-Y5FJWZ5tXXkXw7W_2m5YaMsK3443HluFuyQDC1XGalDpe794bvdBamc_n0KCmPcvw-UHNX2hXURvdp9XZJsee2pTrEsZExy3Xd91CJ2jCjSpibOycoiTN1-1jQZrmB77OkVJuk97dffRgCzxlIPEfDs_1CuNyN1mPvotc6utdHsiEGqso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf1d3e6ee.mp4?token=b3HYtOzwwpzR4ZPBkIANU6HvacX-rzE9Yaj74ku89k4bXQoifwl5zFYPRUjQe0ZBl_UDq-sa_3ebwOeeEkU-8DEefmxZjlEcYtAkhEDWj0RUxAR2GdgM6FvkULXdfbyPp7aAxNkIPJKE8P8YjqpeBs-2rNzdCteqXSsNG6h_LCNRB1IjAeADVWCvW0zmNvoQ8AHNOk6R9YPdcdbpDJrj56ID7NYI9wkZjsLgRkNtRCKobDNVsnjRrkRlWTr15Z6D5WvaE4OV-DD0-Z-_a9--HhRTBpzTGQISLEbNA3JHus1FQqzblGDlIZrC7Eowr-gu3WQ0-nOI8eAcmn2YtxHJfIjXxKxZPMqFEf2ig-I3MrWU0BcibXyn6gsjq1vcfyhyyyuvuCaK9Jsqc7RAHvozrEq7KcSbVcKgnP2USm65_QHW9_dr2A51M13JZUV0togadV9B3ILP09zSrWZetoY8rpuj7BsFgUwvGK8NoGhNqSl4Kg0iQ7FTjIqqf-Y5FJWZ5tXXkXw7W_2m5YaMsK3443HluFuyQDC1XGalDpe794bvdBamc_n0KCmPcvw-UHNX2hXURvdp9XZJsee2pTrEsZExy3Xd91CJ2jCjSpibOycoiTN1-1jQZrmB77OkVJuk97dffRgCzxlIPEfDs_1CuNyN1mPvotc6utdHsiEGqso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آسیب دیده جنگ: خونه ما موشک خورده و کامل تخریب شده اما مسئولان اصلا براشون مهم نیست و وقتی میریم پیششون نگاه هم نمیکنن مارو
🔴
الان ما آواره شدیم و چیزی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/128803" target="_blank">📅 00:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128802">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523f0d92be.mp4?token=tV51KD3zO_MZ2p3gXSqWr82-VQee_gFmm3l9KF2Yk-u4hLNh2Pi3XmtcfidZbamiyvrpb7q8ExyqeDZXPd212l3mfKTBPwNdo5I8DTFHG5a4EsyF-6-yg4vCwrBESU1jZzCpGwnbtkZyJlBBPY98jOmG0ZTonBN5uv_N5t-3bIKT8hLCBM5gH1bb3GbFUHEqWCT2slQIP8UoMstS7ktqraN3KmWESCwPG6y_JSuOkGqtbBRJflUpruoXisr8sMBnzLDDwjwht4BZm-HUKRrTK8OBOxFckwbfh2MJueZnmB3WHbDdvLA33UXZ7iZnXpgdVjO1tmpkUBRycfxbQEqhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523f0d92be.mp4?token=tV51KD3zO_MZ2p3gXSqWr82-VQee_gFmm3l9KF2Yk-u4hLNh2Pi3XmtcfidZbamiyvrpb7q8ExyqeDZXPd212l3mfKTBPwNdo5I8DTFHG5a4EsyF-6-yg4vCwrBESU1jZzCpGwnbtkZyJlBBPY98jOmG0ZTonBN5uv_N5t-3bIKT8hLCBM5gH1bb3GbFUHEqWCT2slQIP8UoMstS7ktqraN3KmWESCwPG6y_JSuOkGqtbBRJflUpruoXisr8sMBnzLDDwjwht4BZm-HUKRrTK8OBOxFckwbfh2MJueZnmB3WHbDdvLA33UXZ7iZnXpgdVjO1tmpkUBRycfxbQEqhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
با بغض: برای من کار راحتی نبود با ترامپ قاتل سردار سلیمانی مذاکره کنم / نفر دومی جز من برای مذاکره نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/128802" target="_blank">📅 00:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128801">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL1G6Sp5fOoQ0_lFLmQPzKgN-D1u0cZDZfEF0NdN4uKnqCsSXtMcmTNO65z3zzjIZ6y8YpVmtZZDERcx1MN43SMuaAN115k27rGNAe8Icjyf88wcUUf-0nlFAFg5sTaXxtFxMsY0pNE3jW8r76dk4i5RZs-X1Rww56iS0skwdJcsD9XvAwVnA2BhZDmC54LfvYTRhdAtPwmtJ7kJXjTy3Fh33-1NIBFwAij6y8D1rP3UTWk-tgG1ymA1qCJlznlLKZwo9nxnXUNzzGq2BS8B8wjoaMIWwUx0A2y0pS51c5XN2AQaeUiJawDBE7dcGK0dpIMOeNF0xw4viIUXo7c-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری میا خلیفه بازیگر مشهور لبنانی برای مهدی طارمی:
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/128801" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128799">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx_CigfYPXf32m3OFBX2-DC6h3x31WoJgXy370XSh1krUkd86oNJc0AAiJsbpuOam7A3PPhx-JZ-XGJN04995cAxF7bKQLjDxEZNeNF5xVMjerg4IjyV9ZpeLOEJP4mAoxYf9EFQuLNX_gA0l-jjMCnLLhlE4fnDykE1JFprUJpn8yHOHab9h5NzAcoikioQdpraGAfB6nfoCehDXMwgr1siBkSDS4NamwSl3WiYWKQ4mMHJUxEodTkL2VtwTv4LirYy6ZIYMs8BoW1VT0R3So1vdm6E5DdAMXnJ4SVytuwn0os3fvt8tZFwVwjNPMzjlBexj0MAa2LV3P9Kd21d0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a5eac0f85.mp4?token=iJSJN09OF0sD99-4ZHEBd78ota7ZIyBFEX9f6SEML-Chqu-mU0P35WvcabRk22jWsHNRUEF6bcw8cTVGNCzveJf8iqqKkR3zwIvJzOmCvNEgFqfkQ0yt_qIgk9wzf3JQIf5rzkm92mNyHbx3KDkjDTA2ES4iWxUbk88kHDq66NY0TjZ3IaJ4wYnzSD-IWV7gzGUB-_CgHq3yd6mfm6v-di24xgab_Sdrf543eyyv8hkv2o168g8Mwf6ZTTyxSRQcXFO0Vra6s-CPapA5edhEQ3qypP_5q41aY3qOt2SzPPXCTxjtnjgabTdl4cu9IsuOSS4IGst4y7paGAr3lETEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a5eac0f85.mp4?token=iJSJN09OF0sD99-4ZHEBd78ota7ZIyBFEX9f6SEML-Chqu-mU0P35WvcabRk22jWsHNRUEF6bcw8cTVGNCzveJf8iqqKkR3zwIvJzOmCvNEgFqfkQ0yt_qIgk9wzf3JQIf5rzkm92mNyHbx3KDkjDTA2ES4iWxUbk88kHDq66NY0TjZ3IaJ4wYnzSD-IWV7gzGUB-_CgHq3yd6mfm6v-di24xgab_Sdrf543eyyv8hkv2o168g8Mwf6ZTTyxSRQcXFO0Vra6s-CPapA5edhEQ3qypP_5q41aY3qOt2SzPPXCTxjtnjgabTdl4cu9IsuOSS4IGst4y7paGAr3lETEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جرمی کلارکسون از مستندساز های ماشینی معروف که در ایران طرفدار زیادی دارد اعلام کرد به سرطان مبتلا شده است
جرمی کلارکسون:
سرطان پروستات دارم، ده درصد از پروستاتم را برداشته اند و اگر همه چیز طبق برنامه پیش برود، در فصل ششم «مزرعه کلارکسون» می‌بینمتان. اگر نه که مشخص است مرده ام. مراقب خودتان باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/128799" target="_blank">📅 00:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/128798" target="_blank">📅 00:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128797">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXPkabK4ImFZyZSIRde24txlOnR36NP66Pk25c-q3U9QRsTKBtqdhEsFzfdU4burm4qSvnh9J1cJKj-oURurrdZwHn2k7yFrIO-IBoDysGP2iOHZm30n0E9XVKptNKJLpPJHHk57sZYydSYcpyddOFn1wk6lR_r-qoyQs3GnuYZory-0vgv7yznHL9xDL_CR0FfYUjH6SfIAIk6ZBYNSqNzm-u7X2p4bOrz1B3JobABOLHYB572LmwNOR66qFec7UZSS2XrMZfXXr6hQ5vbTLjtxoVSGb1BdXbGgGwD78IsuA1ZBwG64dxlXqxnGN-RbmW6zvfvyF7ITLm6V97vGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر کشور: ۶۰ درصد مردم ایران امیدی به بهبود آینده ندارن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128797" target="_blank">📅 00:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128796">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ebf99a2f.mp4?token=mZReQh-U_Ok_4S7p46DFAhsj3ovshkGEcrEOAjoK8Rfm5pwbzwrBX1dolih8eYHDd4SU_IEQM0DGXaPstnv40fXtWo8BLIuYSaQ-pXEmtIlGZAwRlMOcsiyGVmbGycCIbRZCS7ZK5yXcu36KMMcDqUWmP7DlKLiGsdLg9pKzWZK7o5aBTbA-s438AaqLtDdk-Zgp_KfBNpTR68nCcypnlQGDPKY3pD5lPHA3AlXC9eXe03GuJT9Owf-IGnuvPgGFSEU-GxZxnQr4DRgANIizuxb5mN_Y-nc8NQiEtppkGqlPCy6N1M2q42TKKf92W5nOq42jtlitxRXdZmQwJd5-QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ebf99a2f.mp4?token=mZReQh-U_Ok_4S7p46DFAhsj3ovshkGEcrEOAjoK8Rfm5pwbzwrBX1dolih8eYHDd4SU_IEQM0DGXaPstnv40fXtWo8BLIuYSaQ-pXEmtIlGZAwRlMOcsiyGVmbGycCIbRZCS7ZK5yXcu36KMMcDqUWmP7DlKLiGsdLg9pKzWZK7o5aBTbA-s438AaqLtDdk-Zgp_KfBNpTR68nCcypnlQGDPKY3pD5lPHA3AlXC9eXe03GuJT9Owf-IGnuvPgGFSEU-GxZxnQr4DRgANIizuxb5mN_Y-nc8NQiEtppkGqlPCy6N1M2q42TKKf92W5nOq42jtlitxRXdZmQwJd5-QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: ما میتونیم تنگه هرمز رو بر ضد آمریکا تبدیل کنیم. هیچ کس به کمک آمریکا نیومد. این موضوع که باید عوارض تردد در تنگه هرمز پرداخت بشه، تثبیت شده در تفاهم نامه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/128796" target="_blank">📅 00:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128795">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af930f2ffc.mp4?token=IRHkj28bBQKajiEIpk2JkDHMItQXiAJNQ0sZ8frjxThuyj4ewKuDqF_YOKd-FTsB6LwHIPXECMOXH3QVlifgQiKy4MCUyofPYSyBTRBSajziSLg49Yxn_jUEtaSvi_UaC9A8XoChn8voLgggi9UTgpXSjBqBjKF4o4-GKE4muI14twtqu41_mAQMG51ube892lDJ-8V0HGjDGiI-bLF99nab9xM6yENwW_IFXmWu7LryGYJ7c026kS7rV15NJ2vP3Vv8Cdy5bGFlvMhZeZlYv-ZGD1QBWNVo8hzMa1v89FSi2gr86aHDOhf35OQm8XSVZ8bbqCqrF11LosS9jp3Z6ycWIG2XCblRDq_YDX6rEZ7EvuA8D0YMnkRU6jR6lYPPma8jAET_q8ldIOk5-xY0MlIEmA14RANNhbpamM-BTtPjnvX1LDk7ilmlMv-zyCXmm-VW_RhhLBPIQlERJg9L0bj8LHG0FDkJsXzTm7EjR-yISyBKDunH0Pq5PlCEYt2FoXFlEDVITeITuVIhQwXIdujFRJ9vPZkH0Q5ucQnzq3oVyFakrZA38B6Y2jwserpKI_q9GCQZOuP9U3DUVAnqZ_faXu9K0YgKX0DpuXzA4Nr-4eH9TqNRmLpT4suHAPCZ2AEHLqRZy7j9aE3OmbvNBIJUwXhiqUhHCdcuul4CJg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af930f2ffc.mp4?token=IRHkj28bBQKajiEIpk2JkDHMItQXiAJNQ0sZ8frjxThuyj4ewKuDqF_YOKd-FTsB6LwHIPXECMOXH3QVlifgQiKy4MCUyofPYSyBTRBSajziSLg49Yxn_jUEtaSvi_UaC9A8XoChn8voLgggi9UTgpXSjBqBjKF4o4-GKE4muI14twtqu41_mAQMG51ube892lDJ-8V0HGjDGiI-bLF99nab9xM6yENwW_IFXmWu7LryGYJ7c026kS7rV15NJ2vP3Vv8Cdy5bGFlvMhZeZlYv-ZGD1QBWNVo8hzMa1v89FSi2gr86aHDOhf35OQm8XSVZ8bbqCqrF11LosS9jp3Z6ycWIG2XCblRDq_YDX6rEZ7EvuA8D0YMnkRU6jR6lYPPma8jAET_q8ldIOk5-xY0MlIEmA14RANNhbpamM-BTtPjnvX1LDk7ilmlMv-zyCXmm-VW_RhhLBPIQlERJg9L0bj8LHG0FDkJsXzTm7EjR-yISyBKDunH0Pq5PlCEYt2FoXFlEDVITeITuVIhQwXIdujFRJ9vPZkH0Q5ucQnzq3oVyFakrZA38B6Y2jwserpKI_q9GCQZOuP9U3DUVAnqZ_faXu9K0YgKX0DpuXzA4Nr-4eH9TqNRmLpT4suHAPCZ2AEHLqRZy7j9aE3OmbvNBIJUwXhiqUhHCdcuul4CJg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف: بند 6 تفاهم‌نامه 300 میلیارد دلار برای موضوع بازسازی و توسعه اقتصادی در ایران تعیین شده!
🔴
در این بند 300 میلیارد دلار تعیین شده تا در ایران سرمایه گذاری بشه که بخشی از آن صرف بازسازی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/128795" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128794">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0842a70573.mp4?token=ZgxckDtsal5UrYl85hpxY8kttE33FhGxGeU9bz796dMkewCWtzINY4TKRo9oFrLm6d16k5hx7vxMWLAmtz795HMMQbwuclQsBQfOl9aCWHuSwAVFuCEGOLX7EAE5m_Wf7F30zM7WMAt_vMC6uw8sZpgfVzX1MrdoNc3-pYzTVjfUC0IDjBGr4MqMY1EtX9ol7K1eAVKZaayjk8h0MS8ZZPZzwYiDGC3behpF1B1e-8wqMo9C6tc8XiJ8VmcfLU7lRGGqZ8ssGS8PfC5f7G6_KxgNHaCnLyr5g4O8EebrpWMAtSFQJZIOZYJokCzRWK14iu1mwAYqHA2vMD0Y5ZSUaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0842a70573.mp4?token=ZgxckDtsal5UrYl85hpxY8kttE33FhGxGeU9bz796dMkewCWtzINY4TKRo9oFrLm6d16k5hx7vxMWLAmtz795HMMQbwuclQsBQfOl9aCWHuSwAVFuCEGOLX7EAE5m_Wf7F30zM7WMAt_vMC6uw8sZpgfVzX1MrdoNc3-pYzTVjfUC0IDjBGr4MqMY1EtX9ol7K1eAVKZaayjk8h0MS8ZZPZzwYiDGC3behpF1B1e-8wqMo9C6tc8XiJ8VmcfLU7lRGGqZ8ssGS8PfC5f7G6_KxgNHaCnLyr5g4O8EebrpWMAtSFQJZIOZYJokCzRWK14iu1mwAYqHA2vMD0Y5ZSUaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، ژنرال 10 ستاره هم کماکان در حال گذراندن تمرینات آمادسازی برای قبل از مراسم برکناری خود در سمت وزارت جنگ مشاهده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/128794" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128793">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ترامپ برای شرکت در یک شام رسمی که توسط رئیس‌جمهور امانوئل مکرون و بانوی اول بریژیت مکرون برگزار شده است، به کاخ ورسای رفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/128793" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128792">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
قالیباف:
در قوانین ایران هیچ مانعی برای حضور و سرمایه‌گذاری شرکت‌های آمریکایی در داخل ایران وجود ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/128792" target="_blank">📅 00:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128791">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
کسانی که در خیابان فرزندان ایران را به گلوله بستند و شکنجه کردند، مولایشان حسین بود.</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/128791" target="_blank">📅 00:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128790">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
قالیباف: وقتی اظهارات ونس را هنگام سوار شدن به هواپیما دیدم که درباره لبنان صحبت کرده بود، پیش از پرواز و در فرودگاه توئیت زدم که تا وضعیت لبنان روشن نشود، مذاکره را آغاز نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/128790" target="_blank">📅 00:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128789">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قالیباف: برخی متون تفاهنمامه به خاطر حساسیت های حقوقی ساعات ها در موردش بحث شد.
🔴
برخی دوستان نگران بودند که آیا بعد از ۳۰ روز محاصره رفع خواهد شد؟ اما به لطف خدا طی سه روز محاصره لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/128789" target="_blank">📅 00:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128788">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
قالیباف: سازمان ملل حتی یک بیانیه که آمریکا را متجاوز اعلام کند، منتشر نکرد و لذا نمی‌پذیرند که متجاوز هستند. در دنیایی که قانون جنگل حاکم است ما باید با قدرت خود، مسائل را دنبال کنیم.
🔴
البته در تفاهم نامه بند ۶ برای این موضوع آمده که در آن از لفظ بازسازی و توسعه اقتصادی استفاده شده است.
🔴
در این بند ۳۰۰ میلیارد دلار تعیین شده تا در ایران سرمایه گذاری شود که بخشی از آن صرف بازسازی خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/128788" target="_blank">📅 23:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128787">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قالیباف: کشورهای ساحلی تنگه ها در قوانین بین المللی حقوق و وظایفی دارند از جمله این که دیگران باید هزینه خدمات شان را پرداختند کنند.
🔴
دشمنان ایران را خدا از احمق ها آفریده و باعث شدند ظرفیت بالقوه ایران در تنگه هرمز بالفعل شود.
🔴
ایران در تنگه هرمز حق حاکمیتی دارد و طبیعتا در قبال خدمات، هزینه دریافت خواهیم کرد.
🔴
پول‌های بلوکه شده ایران باید در حساب‌های ما و در اختیار بانک مرکزی قرار گیرد. خط اعتباری یعنی بانک مرکزی می‌تواند هر لحظه برای هر کس خواست، ال سی باز کند.
🔴
این را اطمینان می‌دهم که هر کجا دشمن به تعهداتش عمل نکند، سیاست ما بچرخ تا بچرخیم است اما اگر به تعهدات عمل کند ما هم عمل خواهیم کرد.
🔴
اگر دشمن بخواهد خیانت کند ما مردم میدان هستیم و فاصله من از میدان مبارزه دیپلماسی تا میدان مبارزه نظامی زیاد نیست و دست مان روی ماشه است.
🔴
به کسی که منطق را نفهمد با قدرت، منطق را تفهیم خواهیم کرد. من دیپلمات نیستم اما خوب می دانم چطور باید به آمریکا تفهیم کنم که باید چه اقدامی انجام دهد.
🔴
ایران پول‌های بلوکه شده را دریافت خواهد کرد؛ اما این به معنای این نیست که پلت پول بیاوریم. این پول اما باید در اختیار ایران باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128787" target="_blank">📅 23:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128786">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
توضیحات قالیباف در مورد فرآیند مذاکرات اسلام آباد
🔴
طی ۲۴ ساعت ۳ دور مذاکرات با متن و ۳ دور مذاکرات سه جانبه با حضور میانجی برگزار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/128786" target="_blank">📅 23:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128785">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قالیباف: اگر می‌خواستیم محاصره دریایی را با موشک بشکنیم باید جنگی بزرگتر از جنگ ۴۰ روزه رقم میزدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/128785" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128784">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
🔴
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128784" target="_blank">📅 23:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128783">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128783" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128782">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
قالیباف: ما حتما باید با عقلانیت حرکت کنیم، شعار قدرت نیست، گرهی که با دست باز می‌شود را لازم نیست با دندان باز کنیم. اگر دوبار شعار بدهیم ولی قدرت نداشته باشیم یعنی بی اعتباری و کمک به دشمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/128782" target="_blank">📅 23:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128781">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
قالیباف: بدبینی و بی اعتمادی من به آمریکا از همه بیشتر است، حتی اگر توافق نهایی باشد و آن به تایید قطعنامه شورای امنیت برسد بازهم اصلا قابل اعتماد نیست، تضمین ما قدرت ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/128781" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128780">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قالیباف: در مذاکرات به ونس گفتم ما کاملا به شما بی اعتمادیم
🔴
بند ۱۴ تفاهم نامه این است که باید به تصویب شورای امنیت برسد و تبدیل به قطعنامه شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/128780" target="_blank">📅 23:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128779">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
قالیباف: رئیس مجلس لبنان به من می‌گفت ایران مایهٔ افتخار جهان اسلام شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/128779" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128778">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
قالیباف: تو مذاکره به ترامپ اولتیماتوم دادیم
🔴
آتش‌بس رو هم آمریکا درخواست کرد و دنبال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/128778" target="_blank">📅 23:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128777">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
قالیباف: فرق مذاکرات الان با دوره‌های قبل در این است که امروز علمِ پیروزیِ میدان، پشتوانه مذاکرات است/ در مذاکره‌ به روش مبارزه وادادگی و شعارزدگی وجود ندارد
🔴
وقتی حرف از مذاکره و دیپلماسی می‌زنم، منظورم دیپلماسیِ اقتدار است.
🔴
زمان برجام هم گفتم که با مذاکره مخالف نیستم، اما تأکید کردم که با مذاکره‌ای موافقم که خودش یک شیوه مبارزه باشد.
🔴
فرق مذاکرات الان با دوره‌های قبل در این است که امروز این علمِ پیروزیِ میدان، که هم دشمنان و هم دوستان به آن اعتراف کرده‌اند، پشتوانه مذاکره است. نیروهای مسلح ما در مقابل این دشمنِ سراپا مجهز، پیروز شدند.
🔴
در مذاکره‌ای که یک روش مبارزه است، وادادگی وجود ندارد و در کنار آن، شعارزدگی هم جایی ندارد. اگر شعارها را مدام تکرار کنیم، دشمن می‌فهمد که تهدیدها توخالی است و این موضوع باعث می‌شود جسورتر و گستاخ‌تر شود.
🔴
همزمان با مذاکرات به تمام اقدامات دشمن در خلیج فارس پاسخ مناسب دادیم
🔴
در جنگ تحمیلی سوم، برای مثال اتفاقاتی که در خلیج فارس در دوران آتش‌بس رخ داد، قابل توجه است. در آن مقطع، این دشمن بود که پیگیر آتش‌بس بود و ما در ابتدا آن را نمی‌پذیرفتیم.
🔴
به هر حال، وقتی آتش‌بس اجرا شد، دیدید که دشمن اقداماتی را در خلیج فارس انجام داد و ما نیز بلافاصله واکنش نشان دادیم. آخرین نمونه آن، حادثه بالگرد آمریکایی‌ها بود. همچنین دو ناوچه دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند؛ موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
🔴
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن به پرواز درمی‌آمدند، مورد اصابت قرار گرفت. همه این اتفاقات در شرایطی رخ داد که ما همزمان در حال مذاکره نیز بودیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/128777" target="_blank">📅 23:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128776">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
🔟
ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
🔴
1️⃣
1️⃣
ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
🔴
2️⃣
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
🔴
3️⃣
1️⃣
پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
🔴
4️⃣
1️⃣
توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
(امضاء) از طرف دولت جمهوری اسلامی ایران
تاریخ
(امضاء) از طرف دولت ایالات متحده آمریکا
تاریخ
( امضاء) در حضور میانجی
از طرف دولت جمهوری اسلامی پاکستان
تاریخ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/128776" target="_blank">📅 23:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128775">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
🔴
1️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان، اعلام کرده و تعهد می‌کنند از این پس هیچ جنگ یا هیچ عملیات نظامی علیه یکدیگر آغاز نکنند و از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین کنند. توافق نهایی خاتمه دائمی جنگ در تمامی جبهه‌ها، از جمله در لبنان، و بقیه مفاد این بند را تایید خواهد کرد.
🔴
2️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌شوند که به حاکمیت و تمامیت ارضی یکدیگر احترام بگذارند و از مداخله در امور داخلی یکدیگر خودداری کنند.
🔴
3️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا به انجام مذاکرات و حصول به یک توافق نهایی در مدت حداکثر ۶۰ روز، قابل تمدید با رضایت طرفین، متعهد می‌شوند.
🔴
4️⃣
بلافاصله با امضای این یادداشت تفاهم، ایالات متحده آمریکا شروع به رفع محاصره دریایی خود و هرگونه مزاحمت یا ممانعت علیه جمهوری اسلامی ایران می‌کند، و ظرف ۳۰ روز به محاصره دریایی به طور کامل خاتمه خواهد داد. در طول این مدت، تردد کشتی‌ها متناسب با تعداد ترافیک قبل از جنگ که از سوی جمهوری اسلامی ایران برقرار می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود تا ظرف ۳۰ روز پس از توافق نهایی، نیروهای نظامی خود را از حوزه پیرامونی جمهوری اسلامی ایران خارج کند.
🔴
5 با امضای این یادداشت تفاهم، جمهوری اسلامی ایران ترتیباتی را با حداکثر تلاش خود برای عبور ایمن کشتی‌های تجاری، بدون هزینه فقط برای ۶۰ روز، از خلیج فارس به دریای عمان و بالعکس، اتخاذ خواهد کرد. تردد کشتی‌های تجاری بلافاصله آغاز، و با توجه به ضرورت رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز برقرار خواهد شد. جمهوری اسلامی ایران با سلطنت عمان برای تعیین اداره آینده و خدمات دریایی در تنگه هرمز، مطابق با حقوق بین الملل قابل اجرا و حقوق حاکمیتی کشورهای ساحلی تنگه هرمز، گفتگو خواهند کرد و با دیگر کشورهای ساحلی خلیج فارس نیز تبادل نظر می‌کنند.
🔴
6️⃣
ایالات متحده آمریکا متعهد می‌شود، با شرکای منطقه‌ای خود، برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران یک برنامه قطعی مورد توافق طرفین را با تامین حداقل ۳۰۰ میلیارد دلار ایجاد کند. سازوکار
اجرایی‌سازی این برنامه، به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. تمامی تائیدیه‌ها، اسقاطیه‌ها و مجوزهای مورد نیاز برای تراکنش‌های مالی مربوطه توسط ایالات متحده آمریکا ارائه خواهد شد.
🔴
7️⃣
ایالات متحده آمریکا متعهد می‌شود به تمامی انواع تحریم‌ها علیه جمهوری اسلامی ایران، از جمله قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، و تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه، برابر یک برنامه زمانی مورد توافق به عنوان بخشی از توافق نهایی، خاتمه دهد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوع خاتمه تحریم‌ها که در بالا ذکر شده است اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔴
8️⃣
جمهوری اسلامی ایران مجدداً تایید می‌کند که سلاح هسته‌ای تولید یا ابتیاع نخواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت کرده‌اند که وضعیت مواد غنی‌شده ذخیره شده را از طریق یک سازوکار مورد توافق طرفین و مطابق با برنامه زمانی مندرج در بند ۷، حداقل به شیوه رقیق‌سازی در محل، تحت نظارت آژانس بین‌المللی انرژی اتمی، حل و فصل کنند. دو طرف همچنین موافقت می‌کنند تا در مورد موضوع غنی‌سازی، و دیگر موضوعات مورد توافق دو طرف مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران، بر اساس یک چارچوب رضایت‌بخش که در توافق نهایی مورد موافقت قرار خواهد گرفت، بحث کنند. توافق نهایی مفاد این بند را تایید خواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوعات هسته‌ای ذکرشده در بالا اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
🔴
9️⃣
جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند که تا زمان توافق نهایی وضعیت موجود را حفظ کنند؛ جمهوری اسلامی ایران وضع موجود را در برنامه هسته‌ای خود حفظ خواهد کرد، و ایالات متحده آمریکا هیچ تحریم‌های جدیدی علیه ایران وضع نخواهد کرد و نیروهای نظامی بیشتری را در منطقه مستقر نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/128775" target="_blank">📅 23:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128774">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVqY_7U7_I9sfe3FqyErFE0iG7iGqAK5F250KOQz_sSnYxRY1qAztoIkCxa6_Cl6OQRJ_6z16VDcTfMkb6fUbexy4dMJeOeQieVQW5mNMB9wlYJJWBeCGqacfsAVqqSu5uQ1cc8ssxYi6XMHubORzukSu5OFkHobdcZ_6LMX0yZ6cLZCycckldh0AUuNnoYjfYee4ozVrZKsMd2PbVbvES52JshID3W8sxgODz37Hh-sFMLaPB9J7VDCHpqLaS8Rib9l0BMAPTvDNO9Ipcyne4iWbza5LCxSXfbbxKOFAUWBMCSvkWMqXWJx2mTXhWvMnlwu9_DAsOEVaqZ90LiZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا سیما : انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/128774" target="_blank">📅 22:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128773">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تعهد ما این است که در مدت مشخصی، ترافیک دریایی را تنگهٔ هرمز به حالت عادی برگردانیم
🔴
برای تدوین سازوکار مدیریت تنگهٔ هرمز و خدمات دریایی، ایران و عمان همکاری خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/128773" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128772">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر خارجه ایتالیا پس از تماس با عراقچی: توافق ایران و آمریکا گامی مهم برای ثبات منطقه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128772" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128771">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مدیرعامل سایپا: ما قرار نیست ماشینامونو گرون کنیم بیاید از خودمون بخرید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/128771" target="_blank">📅 22:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128770">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0daa17143.mp4?token=MIiVV0g7N4lwmPVRLQYqLsrjZvBye6Z6z_PrjeYnNLvViGvr_PMcnER2wkgXGx8WSUjl5I42pn5yxQddGpOkA-JGKOxJYWfDaix_dBUMO-dQMSTCBz1WBr5P_XdwtRTzd7s-xPu4nz5Ib0WN4yXRIOlovk_jdIR9TjyEABqjaD18kTEpVL2w0TBDql4t4z6bIgIFTqH-VWaH9cUHwdiJrv89r0tflqFE47-ujO2Rt_8ZMZs7Fa7rIjnfjzKdTdd_297gPPZ27qjyxYi7EPmXMSvBWZCgSQDXdwhCgQT7hme0Gr1z2FYiBiaoC1JiElOdrirfUGn1Z8dONgzD4HdKcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0daa17143.mp4?token=MIiVV0g7N4lwmPVRLQYqLsrjZvBye6Z6z_PrjeYnNLvViGvr_PMcnER2wkgXGx8WSUjl5I42pn5yxQddGpOkA-JGKOxJYWfDaix_dBUMO-dQMSTCBz1WBr5P_XdwtRTzd7s-xPu4nz5Ib0WN4yXRIOlovk_jdIR9TjyEABqjaD18kTEpVL2w0TBDql4t4z6bIgIFTqH-VWaH9cUHwdiJrv89r0tflqFE47-ujO2Rt_8ZMZs7Fa7rIjnfjzKdTdd_297gPPZ27qjyxYi7EPmXMSvBWZCgSQDXdwhCgQT7hme0Gr1z2FYiBiaoC1JiElOdrirfUGn1Z8dONgzD4HdKcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ با هواپیما به سمت کاخ ورسای رفت، تا مکرون شام بخوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128770" target="_blank">📅 22:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128769">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDj-_mQ2VV2OHQdCcw9uS6P3Y04fdmYVwpAFuXC4S6DMUXJU8lHWWlLlj8blQlVUlT-2oVjvNf0juZVH5k6aPKBo89erTJg4bBiuGp4lIXADm8brEfvcH0Syubz1Qo4gmYZvfRO_UNl26oikDnZcB3eBMQXBd1wpE3crmMPFOIIzB9YbBmHyWEup0aB5_t3rTbJSdiP0gUgK-SfbCPa0keraotmLCgzBCjHyRwvmK2lt6AUtOn7uTSJf6ZJUqWD0g8KYO2CpXhP9oziNVZASjZe6sn2E0tri3OQOliBGm58LIg5rWgSUQj6yCrpLkUHV6YMvaql4kiqTTJEpKTk9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور لیندسی گراهام: به نظر من امضای این تفاهم‌نامه به نفع ایالات متحده خواهد بود، زیرا تنگه هرمز شروع به بازگشایی می‌کند و درگیری‌ها با ایران متوقف می‌شود.
🔴
اینکه آیا آمریکا می‌تواند با ایران بر سر برنامه هسته‌ای و سایر مسائل به توافقی قابل قبول و قابل راستی‌آزمایی برسد یا نه، هنوز مشخص نیست، اما من تلاش برای رسیدن به چنین توافقی را کم‌هزینه می‌بینم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/128769" target="_blank">📅 21:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128768">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
وزارت خارجه ایران : ادامه اشغال جنوب لبنان توسط اسرائیل، یادداشت تفاهم را نقض می‌کند و ما اقدامات لازم را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/128768" target="_blank">📅 21:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128767">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
منبع آگاه به فارس: پیشنهاد امضای الکترونیکی تفاهم‌نامه ایران و آمریکا پیش از سفر به ژنو مطرح شده است
🔴
تا این لحظه جمهوری اسلامی موافقت خود را با این پیشنهاد اعلام نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/128767" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128766">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
معاون وزارت ارتباطات : با اشاره به تجربه قطع اینترنت در جریان جنگ اخیر کشور به سطحی از بلوغ رسیده که حتی در شرایط بحرانی و التهاب شدید نیز میتواند بدون قطع اینترنت مدیریت شود و دیگر شاهد قطع اینترنت نخواهیم بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/128766" target="_blank">📅 21:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128765">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
الجزیره به نقل از مقام کاخ سفید: ایالات متحده متعهد است که بلافاصله پس از امضای یادداشت تفاهم، معافیت‌هایی برای صادرات نفت ایران صادر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/128765" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128764">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری / بقایی: احتمال امضای تفاهمنامه توسط روسای جمهور ایران و آمریکا مطرح است
🔴
برنامه‌های ایران برای نشست ژنو تغییری نکرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/128764" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128763">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آکسیوس: طبق توافق تأیید شده، ایالات متحده و جمهوری اسلامی ایران بر موارد زیر توافق دارند:
🔴
آتش‌بس فوری و دائمی در تمام صحنه‌ها، از جمله لبنان، با تعهد به عدم انجام اقدامات نظامی یا تهدیدات بیشتر.
🔴
احترام متقابل به حاکمیت و عدم دخالت در امور داخلی.
🔴
مذاکره برای توافق نهایی ظرف ۶۰ روز (قابل تمدید با رضایت متقابل).
🔴
رفع تدریجی محاصره دریایی آمریکا ظرف ۳۰ روز و عقب‌نشینی نیروها از اطراف ایران پس از توافق نهایی.
🔴
بازسازی و حفاظت از مسیرهای حمل‌ونقل تجاری در منطقه خلیج فارس–خلیج عمان، با پاکسازی موانع و مین‌ها.
🔴
مشورت ایران با عمان و کشورهای منطقه درباره حاکمیت آینده و ترتیبات دریایی در تنگه هرمز.
🔴
تدوین طرح مشترک بازسازی اقتصادی برای ایران (حداقل ۳۰۰ میلیارد دلار).
🔴
رفع کامل تمامی تحریم‌ها (سازمان ملل، مرتبط با آژانس بین‌المللی انرژی اتمی، تحریم‌های اولیه و ثانویه آمریکا) طبق جدول زمانی توافق شده.
🔴
ایران تأکید می‌کند که سلاح هسته‌ای توسعه نخواهد داد؛ مسائل مربوط به مواد غنی‌شده و غنی‌سازی تحت نظارت آژانس بین‌المللی انرژی اتمی مدیریت خواهد شد.
🔴
حفظ وضعیت موجود تا توافق نهایی: عدم اعمال تحریم‌های جدید یا تشدید نظامی.
🔴
صدور مجوزهای آمریکا برای صادرات نفت ایران و خدمات مالی مرتبط.
🔴
آزادسازی و دسترسی کامل به دارایی‌های ایران، طبق رویه‌های توافق شده مشترک.
🔴
ایجاد مکانیزمی برای نظارت بر اجرای توافق.
🔴
توافق نهایی در چارچوب مراحل آتش‌بس مذاکره و سپس توسط شورای امنیت سازمان ملل تصویب خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/128763" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128762">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
یک مقام کاخ سفید: نشست سوئیس برای مرحله بعدی بسیار مهم خواهد بود زیرا سند کنونی نیت‌های طرفین را منعکس می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/128762" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128761">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
کاخ سفید: توافق نهایی از طریق یک قطعنامه الزام‌آور از سوی شورای امنیت سازمان ملل تصویب خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/128761" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128760">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه : در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/128760" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128759">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
یک مقام کاخ سفید: به همان اندازه که ایران به مسائل هسته‌ای پایبند باشد، تحریم‌ها علیه آن کاهش خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/128759" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm_z8W0f_6N_4YLU9ExbjGAcfM2MR_PVhf4WGMt0jK2qmrYwN18P64d_9RYvlKBYWdzgsy20WJrZVaJmei7SU8CR91GUpCH7sPw6OhjglDHn4yhFrYyz0HBuwN1Qljj6oP_NLG21da4WGJPcuTr1KgvT4QHF7kRSuE_srPfDPxK2b_3wjB7QEQ9CfjZ7x8x4UOFi022FeP3kKxXqrDBrD8l4IP4xly5LH0HdP6dz_GDhj_9Q65C5YDo-7GI_IQworSs3gwjUiXlag80LGi3XjubWgqqdzzFmrW5oDSpO73Ty_CosxzPY3VG89YnwTqvq94Ywyza6rCN47vA5MiPmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی بریتانیا گزارش می‌دهد که یک کشتی در ۱۰۵ مایل دریایی شمال شرق عدن، یمن، امروز زودتر مورد حمله قرار گرفت پس از اینکه دو قایق کوچک حامل افراد مسلح تا فاصله چهار متری نزدیک شدند و آتش گشودند.
🔴
تیم امنیتی کشتی پاسخ آتش داد، که باعث شد مهاجمان حمله را متوقف کرده و از منطقه عقب‌نشینی کنند. خدمه در امان هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/128758" target="_blank">📅 20:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / تسنیم :گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/128757" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f24117a830.mp4?token=AxEFosKuHCIiYNjq_xe1W9HnbOY23XTquOYRhmfCZWveEdIsENI01elZTgjMTGxP36VTksyqU5v1xzq5FZW0ljdvEC1OszImttlSbonhZf3tmvPKwqdhGYUHv9AZoenTN3O9g0NYBwjipOi710ouDSsQ8eNEnItNskLi4p9vK8LhhB-saHU6EYhlClUDQdeF0DM6rRZ3fbWJ-J1K1XGK39O-cHGuafEJ_sKaTggBICAk0q4_aHi6KRm-ePAfEIvA4b558LESiKCCxLEBDqvIlBLpdw6veJN8GWgVrNrlFmL--mMaMH23kWXwVLcNptBg1SIpImAKUmh6cAONAsp47ZnusTQiQikbsUBMEo1IJaVWJ4qAFnuHDDgT2XYB0alukA8LZ5HFPxIr8j6T2XDYB7ShjXLgCxYAn5Rqktc_4YHKftdP8mnK0U_934l_WDbSUNj1kw76Lmj5pvog8AVRfZRQ-HyL8aSgQ1ZHRyLfDQrgQRiqWxhqGskJxHzT8inpFEhn_jKiUt6MN0NmUFXn2665XIechwpdnyQFCfcQLuwz96_5W1ECWpMCDHEthOkf9DFEVzNF6ga90MQKt4j6cpNbyz3TQYajEVvnAkz32P_G1x15CfkLTunZH2ofAgMoltxyJaOM1LjfpsI0Y_Dsd72HUEht3lM6FkKmWbkUjrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f24117a830.mp4?token=AxEFosKuHCIiYNjq_xe1W9HnbOY23XTquOYRhmfCZWveEdIsENI01elZTgjMTGxP36VTksyqU5v1xzq5FZW0ljdvEC1OszImttlSbonhZf3tmvPKwqdhGYUHv9AZoenTN3O9g0NYBwjipOi710ouDSsQ8eNEnItNskLi4p9vK8LhhB-saHU6EYhlClUDQdeF0DM6rRZ3fbWJ-J1K1XGK39O-cHGuafEJ_sKaTggBICAk0q4_aHi6KRm-ePAfEIvA4b558LESiKCCxLEBDqvIlBLpdw6veJN8GWgVrNrlFmL--mMaMH23kWXwVLcNptBg1SIpImAKUmh6cAONAsp47ZnusTQiQikbsUBMEo1IJaVWJ4qAFnuHDDgT2XYB0alukA8LZ5HFPxIr8j6T2XDYB7ShjXLgCxYAn5Rqktc_4YHKftdP8mnK0U_934l_WDbSUNj1kw76Lmj5pvog8AVRfZRQ-HyL8aSgQ1ZHRyLfDQrgQRiqWxhqGskJxHzT8inpFEhn_jKiUt6MN0NmUFXn2665XIechwpdnyQFCfcQLuwz96_5W1ECWpMCDHEthOkf9DFEVzNF6ga90MQKt4j6cpNbyz3TQYajEVvnAkz32P_G1x15CfkLTunZH2ofAgMoltxyJaOM1LjfpsI0Y_Dsd72HUEht3lM6FkKmWbkUjrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا بخشی از این موضوع این است که معاون رئیس‌جمهور را می‌فرستید؟ اگر جواب داد، عالی است؛ شما به خاطر فرستادن او نابغه به نظر می‌رسید. و اگر جواب نداد، تقصیر معاون رئیس‌جمهور است.
🔴
ترامپ: این ایده را دوست دارم، حتماً. به این ترتیب، اگر جواب داد، من اعتبارش را می‌گیرم. اگر جواب نداد، تقصیر JD است. بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
🔴
بله، این ایده را دوست دارم. فکر می‌کنم ایده خوبی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/128756" target="_blank">📅 20:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=se8Xolnlu8GHPN5ig_gyYzqkuz1Od7eQCvIM5A4UP6XDgqD0wBJnrIvXTjo9YSnRL1hZu2hS1OiYQSwZC7U-AcRv5D3qQ-ZorD21BhtBHIIURdJQo-2ce4hyimPqarMxenDKh2iKyhsLbuWjRexbaiKbHMPd71ce4U-lPj8JPhFDt9hLA8gfv71_0Y7an_epMLQQKoJlt3xiPfulDoWdedIZnxGz-0n5ixLLnpE64m3AKhPNjCsJjA0JgD3dS1J21pj3Ddj9cJbCbnV9FtEb_mkpUyK9_Ljms4T9gvhJVkmeqsTjpnPUSreIzI_MmMkvlSUV0h2YDcycPBFfJHcGRh-yX3GYH6SFW0KqKRn4VZzxGf1KvHVglfpHGRb0MQfJ7wh-P51ItDaPwTxpPw0o6ybqviD1fcaFPT9pZ9cTnLyKVK-gp_5piyRTDr9pYEa26J8sSjINLiZ83I5TaU-RRg0b7RN2n3kFSZL1fOThuWKlogg-Io2hPlAYYqS5-XoZViuG0K1N48QzkDrqYgBK_XjS8ALfUxjdH74akmYDLkw7hmcFs5qzX1J_POSppxLi5eMbzaOH3HEZmLMdxx18x_CoK5LCk9RKQM0Jaj0_IBbG9DeQ6qt94ct6DERpz1ycztihAO-s7O6fGaUkLi8C10I3vdmKzbHzfA39oxIQ8Jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee1220f65.mp4?token=se8Xolnlu8GHPN5ig_gyYzqkuz1Od7eQCvIM5A4UP6XDgqD0wBJnrIvXTjo9YSnRL1hZu2hS1OiYQSwZC7U-AcRv5D3qQ-ZorD21BhtBHIIURdJQo-2ce4hyimPqarMxenDKh2iKyhsLbuWjRexbaiKbHMPd71ce4U-lPj8JPhFDt9hLA8gfv71_0Y7an_epMLQQKoJlt3xiPfulDoWdedIZnxGz-0n5ixLLnpE64m3AKhPNjCsJjA0JgD3dS1J21pj3Ddj9cJbCbnV9FtEb_mkpUyK9_Ljms4T9gvhJVkmeqsTjpnPUSreIzI_MmMkvlSUV0h2YDcycPBFfJHcGRh-yX3GYH6SFW0KqKRn4VZzxGf1KvHVglfpHGRb0MQfJ7wh-P51ItDaPwTxpPw0o6ybqviD1fcaFPT9pZ9cTnLyKVK-gp_5piyRTDr9pYEa26J8sSjINLiZ83I5TaU-RRg0b7RN2n3kFSZL1fOThuWKlogg-Io2hPlAYYqS5-XoZViuG0K1N48QzkDrqYgBK_XjS8ALfUxjdH74akmYDLkw7hmcFs5qzX1J_POSppxLi5eMbzaOH3HEZmLMdxx18x_CoK5LCk9RKQM0Jaj0_IBbG9DeQ6qt94ct6DERpz1ycztihAO-s7O6fGaUkLi8C10I3vdmKzbHzfA39oxIQ8Jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دووسی از فاکس: برای مراسم امضای توافق صلح ایران می مانید؟
🔴
ترامپ: شاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/128755" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: رئیس جمهور چین به دنبال کمک به حل و فصل اوضاع مربوط به ایران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/128754" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/128753" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ: به محض اینکه ایران اقدامی انجام دهد، تحریم‌ها اعمال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/128752" target="_blank">📅 20:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=q5Sp3M68cyMXSp8pNgwR7a8kiEUl1DRpdFejOcK2CUfmMlpqPwjJN8bM8tWeaaPWC6OZARB68a1Sq50LdhORc--4hCItu0fwgalmCf5Cl3mYmjvhjUDum9Tar1UqrQyUEV2Te_IOjNICapJuWE0GxIYJRaYYn81TqckASVf6H6E69gz9qKN_AH4BZhLZSgjLu6TK-AfQapTVF8dxWPted3a6AIVuu3e7SVt_oxcN7OMj2og5oyhyiQfiDHhol4tWpdjS6tIIynmcQC45lndWxfy-nQxtqDMGNQ0Fu8aP54C-Chv-iarQeuTj4oRbiOBgwl9Qju-uzpulmLT0ry6PeA33afRqwMwQAsyo40Jdtbts91OaRkAsyKQVMtzYCSj2z4EELnzDtcaJtDiMSrJ80FGuME3x4APrEGQxA1eM9WIHG6I-RKoZBt7CbtFkiENoFP3jfWLcXwQqqd8hMlEx-1GxqRzsTSZXmavQjyqQAEFchXq6zIIPmu-CRx5AW6va0fBiTWww_EUxa8-bSXKrnN4jePVtbVWVd8m3i98xKc7TFPWLLDYeN6BjiVgffObpWUTzadT01ARVXinrVW8EOIhzZauQjIFutM-q9fFHmqi6Zhrf3qhHA7f1OfmWRFDdoeqBGzN1IovJ86Vrinq9zBasMTemxxZrmSAv3X_DIaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6589ab41.mp4?token=q5Sp3M68cyMXSp8pNgwR7a8kiEUl1DRpdFejOcK2CUfmMlpqPwjJN8bM8tWeaaPWC6OZARB68a1Sq50LdhORc--4hCItu0fwgalmCf5Cl3mYmjvhjUDum9Tar1UqrQyUEV2Te_IOjNICapJuWE0GxIYJRaYYn81TqckASVf6H6E69gz9qKN_AH4BZhLZSgjLu6TK-AfQapTVF8dxWPted3a6AIVuu3e7SVt_oxcN7OMj2og5oyhyiQfiDHhol4tWpdjS6tIIynmcQC45lndWxfy-nQxtqDMGNQ0Fu8aP54C-Chv-iarQeuTj4oRbiOBgwl9Qju-uzpulmLT0ry6PeA33afRqwMwQAsyo40Jdtbts91OaRkAsyKQVMtzYCSj2z4EELnzDtcaJtDiMSrJ80FGuME3x4APrEGQxA1eM9WIHG6I-RKoZBt7CbtFkiENoFP3jfWLcXwQqqd8hMlEx-1GxqRzsTSZXmavQjyqQAEFchXq6zIIPmu-CRx5AW6va0fBiTWww_EUxa8-bSXKrnN4jePVtbVWVd8m3i98xKc7TFPWLLDYeN6BjiVgffObpWUTzadT01ARVXinrVW8EOIhzZauQjIFutM-q9fFHmqi6Zhrf3qhHA7f1OfmWRFDdoeqBGzN1IovJ86Vrinq9zBasMTemxxZrmSAv3X_DIaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره افغانستان: ممکن است تمام تجهیزات را پس بگیرم... افغانستان دارد به ما چاپلوسی می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/128751" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=T6I31azxFoUxmPNWLYg_HfLp3kjt5k60qt1ZoxV6nKsl_PsPwIf0MFShI4iQU8CTOHzrhfqnBv9k7VYsyMO3Z-bdxGl-Cx_B7-yGcwVXfxpv05w0hA4JR9yDi2FmOujatQbA_hWAuhqwNYiiWQ2NSZ07UKo5hx5jWTuyq5qW7IySMrfcl5kGvujD-jUgYKg5jCFmpMSnasT3UsWQFto-I5Y_0nRp5DTQ7N4MEDPKRSgHKKFvkuS4aKTQW2JpOGZ8qNFmN9sRPv_UfbZRh8c3Chzl3bXbWet9aLyvRhrmGePFemvtnwSSktRt_ytUogYq-5rr_G56XrdbJRkHtJUT91VGZ4J9n4jxL8fbD5__4Cf-fUi-U1SicaVAazwTeaJ8Ldevp41iIbi-Ytb9NgU-Fwcj3OwoJtivf5xGAyVw3MkvvmsHaLLP9PsspqEIcOYhPJINlayVF5dr5dg4XCFQ5rDjt39Z7pKSQx0Dw0w4YFQTb2n95Q4sCn69x9U5006MhcwDBrnNTGnrUMn7a61iCz6GtO2lnZUzwdHGVw-YXL30Z2donEam2_fKiPrfF4Z_LeffWivN4DAOO9yL97EH0isH_LU56Bhy-o5xs60XwuzYT12E5Vig2pYcKSDEnWckDDkK7WtpAyKi27YoywY3IHzLTsRxZx27chwyX8Jt1P8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74479be1f.mp4?token=T6I31azxFoUxmPNWLYg_HfLp3kjt5k60qt1ZoxV6nKsl_PsPwIf0MFShI4iQU8CTOHzrhfqnBv9k7VYsyMO3Z-bdxGl-Cx_B7-yGcwVXfxpv05w0hA4JR9yDi2FmOujatQbA_hWAuhqwNYiiWQ2NSZ07UKo5hx5jWTuyq5qW7IySMrfcl5kGvujD-jUgYKg5jCFmpMSnasT3UsWQFto-I5Y_0nRp5DTQ7N4MEDPKRSgHKKFvkuS4aKTQW2JpOGZ8qNFmN9sRPv_UfbZRh8c3Chzl3bXbWet9aLyvRhrmGePFemvtnwSSktRt_ytUogYq-5rr_G56XrdbJRkHtJUT91VGZ4J9n4jxL8fbD5__4Cf-fUi-U1SicaVAazwTeaJ8Ldevp41iIbi-Ytb9NgU-Fwcj3OwoJtivf5xGAyVw3MkvvmsHaLLP9PsspqEIcOYhPJINlayVF5dr5dg4XCFQ5rDjt39Z7pKSQx0Dw0w4YFQTb2n95Q4sCn69x9U5006MhcwDBrnNTGnrUMn7a61iCz6GtO2lnZUzwdHGVw-YXL30Z2donEam2_fKiPrfF4Z_LeffWivN4DAOO9yL97EH0isH_LU56Bhy-o5xs60XwuzYT12E5Vig2pYcKSDEnWckDDkK7WtpAyKi27YoywY3IHzLTsRxZx27chwyX8Jt1P8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به آنها می‌گویم: شما احتمالاً سومین ذخایر بزرگ نفت در جهان را دارید، به چه دلیل به سلاح هسته‌ای نیاز دارید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/128750" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ درباره ایران: آیا اجازه می‌دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/128749" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
گزارشگر:  چرا اکنون برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
🔴
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از سایر کشورها دارند.
🔴
ما احتمالاً ۸۴-۸۵٪ از موشک‌هایشان را از کار انداختیم؛ بقیه زیر زمین هستند؛ حتی نمی‌توانند آنها را بیرون بیاورند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/alonews/128748" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ktAbx9kjjgHoCWrzBVvKepQF2qApgXAuQ3ErvL_fugd92zhYCz7l3Mu4FK8zNG4cXPqUE8V6LEILNVLAML4f4kPPzWa8HgJ4yt99H4fCCr449huO13cP9SQG8RtrRYTCpxHei6hGg-alFp98sFC9UX9wXDz48PnPEINu7pt_SV82DOQXjwFYHBYqdKJkot9rxWOYe_knMwaNb8r12OZ2U5B87ieRZYcaCt8d3ZMrOKghFWAuaL2AT49bFGSXL9WTkiSE3q4EHyxOBAVzQiEuKXj77PQ-M3JvVZoShFfyS536gSuphtgMf3-8OnoSELGwXHP8ppqNkcG3q26uQg2D4D5CjKYOzZuYu8N55zGCJr6uf_kqdxz6AONgBeCdAkEkoWBCyqimSNTg0XFJp1ezhfIhNkGGTd0z33CS81EQ6LYTyowtwGnd7d9tHBF14KbeFuAScMUECm7aj9LAsun8CG7z-MQjqy9z7d_cNadRbHDxag9tA8yQE2nJs7uEx_XltedKQBobdg-btuN-8_iBd3WtJONwZsB6FRY1kcLRIs10VBVhXfPuWiEYeUMI1Kcyn0usJC6-s4pGOw1H_dFcEKgZOZb2hNHrX7BnruxjnEp8ouIqH55Slr1WbN5FRvAtjHSynCgPK33YZ6d6M0q3D2yahOzJLHiBkka8VZE7M2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0760bad7.mp4?token=ktAbx9kjjgHoCWrzBVvKepQF2qApgXAuQ3ErvL_fugd92zhYCz7l3Mu4FK8zNG4cXPqUE8V6LEILNVLAML4f4kPPzWa8HgJ4yt99H4fCCr449huO13cP9SQG8RtrRYTCpxHei6hGg-alFp98sFC9UX9wXDz48PnPEINu7pt_SV82DOQXjwFYHBYqdKJkot9rxWOYe_knMwaNb8r12OZ2U5B87ieRZYcaCt8d3ZMrOKghFWAuaL2AT49bFGSXL9WTkiSE3q4EHyxOBAVzQiEuKXj77PQ-M3JvVZoShFfyS536gSuphtgMf3-8OnoSELGwXHP8ppqNkcG3q26uQg2D4D5CjKYOzZuYu8N55zGCJr6uf_kqdxz6AONgBeCdAkEkoWBCyqimSNTg0XFJp1ezhfIhNkGGTd0z33CS81EQ6LYTyowtwGnd7d9tHBF14KbeFuAScMUECm7aj9LAsun8CG7z-MQjqy9z7d_cNadRbHDxag9tA8yQE2nJs7uEx_XltedKQBobdg-btuN-8_iBd3WtJONwZsB6FRY1kcLRIs10VBVhXfPuWiEYeUMI1Kcyn0usJC6-s4pGOw1H_dFcEKgZOZb2hNHrX7BnruxjnEp8ouIqH55Slr1WbN5FRvAtjHSynCgPK33YZ6d6M0q3D2yahOzJLHiBkka8VZE7M2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند، «سپاس خداوند را، دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است؛ ما کاملاً تسلیم می‌شویم؛ کاملاً دست می‌کشیم؛ این جنگ تمام شده است؛ ما شکست خورده‌ایم»، نیویورک تایمز و سی‌ان‌ان و چند رسانه دیگر خواهند گفت، «ایران پیروزی بزرگی کسب کرده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/128747" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ : ما یه میلیارد دلار بمب روی ایران ریختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/alonews/128746" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: حادثه مربوط به حمله به مدرسه میناب در ایران هنوز در دست بررسی است و اشتباهات در جنگ اتفاق می‌افتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/128745" target="_blank">📅 20:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=DGMOOtNvPxiSTffmoa1X6HNgMolIz8b2qIYT2skGYrFoa7XdfZiyVGL2ruqQ9-kOhul4HaY6XqHi6zlYBFt9OP1aqYDrFuMeEZ0ZbdhsCm12pkZr07YabY-usyQWMDQUgBSrWBcmBUmQexhOEKZ9SZv0Z_CxG-pCLQ_XO2aaB9KhAoXKi-NEsYLh5ollYpVitQv3gQG724gNkKJ6JS11sTpLDPGpblZiuoBXEmiKrxORyn5BgL-7JX4uEUp78PT98zLexIMbGs1fFseh0sOCqd5VYitAd4qEzt7qhmnHxOcybdIT6LQgBL03hjpAaVa_BZwpqCz7HdpvpSeXo8Z5dmFTSksBUViocQBq4DxLuCFVWXt7XNAsjHSl95TbvxzYlNWPzSh-vnsjbmz9CwYbpRRVQ9sGN6yE_Y5gBrAw5lhFMpthUEEw8klBdHtyS2xHrIG8BdWm9qK1bs9lDPESojM4vkaQmA7jZIFztbihR1KD-C9PJuwUIczhRWM8AaI7kk_qRyJPw8bcoLcktxLBPFHqn0QEeIPRsUwBeH-g2Sb6X--DMWyXjMCUqU1j0KLB1Ddb01LnsHdicq4YQbJH5upkc5hLwSinyQtPLWmFF7wlXUz31hQYSA4TnVHvabwx5mgcPAMBz1h63zGoe2PlQ82rptcFpfeELmcz5DuMDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fca7846a9d.mp4?token=DGMOOtNvPxiSTffmoa1X6HNgMolIz8b2qIYT2skGYrFoa7XdfZiyVGL2ruqQ9-kOhul4HaY6XqHi6zlYBFt9OP1aqYDrFuMeEZ0ZbdhsCm12pkZr07YabY-usyQWMDQUgBSrWBcmBUmQexhOEKZ9SZv0Z_CxG-pCLQ_XO2aaB9KhAoXKi-NEsYLh5ollYpVitQv3gQG724gNkKJ6JS11sTpLDPGpblZiuoBXEmiKrxORyn5BgL-7JX4uEUp78PT98zLexIMbGs1fFseh0sOCqd5VYitAd4qEzt7qhmnHxOcybdIT6LQgBL03hjpAaVa_BZwpqCz7HdpvpSeXo8Z5dmFTSksBUViocQBq4DxLuCFVWXt7XNAsjHSl95TbvxzYlNWPzSh-vnsjbmz9CwYbpRRVQ9sGN6yE_Y5gBrAw5lhFMpthUEEw8klBdHtyS2xHrIG8BdWm9qK1bs9lDPESojM4vkaQmA7jZIFztbihR1KD-C9PJuwUIczhRWM8AaI7kk_qRyJPw8bcoLcktxLBPFHqn0QEeIPRsUwBeH-g2Sb6X--DMWyXjMCUqU1j0KLB1Ddb01LnsHdicq4YQbJH5upkc5hLwSinyQtPLWmFF7wlXUz31hQYSA4TnVHvabwx5mgcPAMBz1h63zGoe2PlQ82rptcFpfeELmcz5DuMDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: مرد خردمندی یک بار در ژانویه ۲۰۲۰ گفت: «ایران هرگز در جنگی پیروز نشده، اما هرگز در مذاکره‌ای شکست نخورده است.»
🔴
پرزيدنت ترامپ: کی این رو گفته؟
🔴
پیتر دوسی از فاکس نیوز: دونالد ترامپ.
🔴
پرزيدنت ترامپ: آها، فکر می‌کردم می‌خواهی همین را بگویی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128744" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2OaUOKIN2DkYAHx3FBd9WtVpA0uHqj9mo1DyI-O94jwgnGi3X-EMtp6KlgLyuMY4pZ2xWmHfefZScrnhWpQcIaj62gHn8WsNc3M80DTCG2itmfakE3hnBLrl9D1Hk7Gf-q9d56rbchq5Or7ErmTJSBHNLExrlkAA_vd8xKst4KeQzh5fS91l3O8n8yrEaLca32yWONHvtYjo_J0EoAL-zvQ6KKDO5GbjMEitIyOdYU1ysWhzRV1vhaRFnti0iXY54vhEzcIYvI9kr8uA98RvHja6hboLPXa5aWwOUqghpmT9Vi5K_1_AoB-a08qCxz6Vh1KHkOKuoDiKBMzn80vUFgcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0926f88f33.mp4?token=qpYWq5B0HPaEXderQPsZITyv7mn3cxCSuEWGzQrZ1sCpXLcMjsfqS4D_XLuk_19qrgSx4SUQGSF8Q3yZJFYBkQKqDYNlDELQzXANWdElKHTjBZBGqEqSTjNoQDeclRLNXJPUcuMarwIKTtdRgRr-hfGTnEkw2DBDKCmkD-c91slPvrolCHyqyl42ka501wVhD3LOHBwBtWI1orpqOmTrtZp23IrN2l-l9HzLNyUpIoKfl6dFhJYWOxl1dj-qCUimCnSKnqOaAtmNt9nLjtkLokSNUuUgHmjqodhF-Icp0JwfdwP9Ir7kpa-Tk__7kI-z0btSILM6T58bFcADe7A2OaUOKIN2DkYAHx3FBd9WtVpA0uHqj9mo1DyI-O94jwgnGi3X-EMtp6KlgLyuMY4pZ2xWmHfefZScrnhWpQcIaj62gHn8WsNc3M80DTCG2itmfakE3hnBLrl9D1Hk7Gf-q9d56rbchq5Or7ErmTJSBHNLExrlkAA_vd8xKst4KeQzh5fS91l3O8n8yrEaLca32yWONHvtYjo_J0EoAL-zvQ6KKDO5GbjMEitIyOdYU1ysWhzRV1vhaRFnti0iXY54vhEzcIYvI9kr8uA98RvHja6hboLPXa5aWwOUqghpmT9Vi5K_1_AoB-a08qCxz6Vh1KHkOKuoDiKBMzn80vUFgcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره خنثی بودن متحدان جمهوری اسلامی ایران: می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، با او بودم و او خنثی ماند، کاملاً خنثی، و من از آن قدردانی می‌کنم.
🔴
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار خنثی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/128743" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
