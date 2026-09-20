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
<img src="https://cdn4.telesco.pe/file/nt0QD6r4PMY3f9C8KgJSoDVGyCNedM2O3oaS8GUg_FCunRK_2YTmprsmGLK-zY_Tpb4H9Z-KsQPaVua3X7aob48tq1AwA_YdlSPVHz1Dt11NNmJG4V2TwQMSGEvaM0cM_WKedHFwfh5_8gS6IHj6sJjxK5Sf0U1ws20mp2Uk-zjag_jF0cITtqLzFXhTyC2ciUjmKwQDf7Cs4FH9iYyGWgQkPZv1XkLYxN4J7OciVehMzDz1RnAi-zooXMLnlMz7aQfIskXozYiA6Tr_dysKM2DZOanfi0F_12wKH1Wy5hyOgAex_-PuHAKzdSOaC1_mjl_7YnhnQFsFz0RCAGEudA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-140325">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd1-Iqw9QV36oSfmDw59MB9EbdV3qzDzNFG2-8Ps8UcC8ZXVB3iaJ6PnMo6unvZPihPzaHye4sZ3spT-YkmLcHXE4m1enq0ZWn08mV1piQ3Pk0qEj_kSyqVG5z-DYjd3WxS1RP8XLr-rTehR9_03Dhn6R3Pxo3ax6nznWakQ7-D85XpgaW4L3Wpmcd5RnlqBKVhOpGyrKsZQ9ystwY2W9CjA6sCADo_hZwsXS4X9nDdYrjtJxoS8SUADNAAetcYVrqCOTT0fBG7nTZNLS_yXfsLDlg138B2RamuEbTESQxXAfYXTeHOFzrMX6UHMHRJHebXTnfQBe3mNg25YdiZlew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
پیمان حدادی با حضور در ورزشگاه درفشی‌فر ضمن بررسی شرایط آکادمی، با بازیکنان و کادر فنی تیم‌های امید و جوانان دیدار کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 141 · <a href="https://t.me/SorkhTimes/140325" target="_blank">📅 21:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140324">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
✅
تصمیم پرسپولیس درباره اورونوف
✔️
✔️
پرسپولیس فعلاً هیچ برنامه‌ای برای جدایی اورونوف نداره و این بازیکن همچنان در برنامه‌های باشگاه و کادرفنی قرار داره.
✔️
✔️
شایعه انتقالش به تراکتور به‌خاطر نیمکت‌نشینی تأیید نشده و حتی اگر در آینده بحث فروشش مطرح بشه،…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/140324" target="_blank">📅 20:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140323">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/140323" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140322">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
ادعای خبرورزشی :
❌
تراکتور به دنبال جذب قرضی اورونوف از پرسپولیس
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/140322" target="_blank">📅 19:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140321">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEtwTFdxdlxG3xym4XTJmz9jEMTRJGDmt43YM_MuGcRapLuOewLGtBUaMbwFvewhYxNj0ZS6ieb7i6KLOtCZ8BZDHi4-Je7PtOZu_TN21L2udVi1pQq1zP16nmtmxW_nKERHm7aPFKVffF1Q4iDyeN07cznGeTBxjUJFgJBbydWopjJQq3GOuGm4BZDqaJAc0FO8YyqnD4oDIwqMU-sSSe8CWXHrmbphf9X2_jOZC3rEo2e27Dflh7R-fxqLZ_xtRAfw2zuH3hyBxzSElqjvMJEz5ZMR4isC0VdKaTfjWLNZj_D3PEV7ihMPFJ_yVgUEzdlxANWwSNyR64IHVXIjFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
گزارش تصویری از تمرین امروز تیم ملی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SorkhTimes/140321" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140320">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbqgqlBu-wPP-wZyceEQYr3Hm_IWJH1_r-l0rgkc0Y5P4mmu3SjGx-in_Ptk9SOZwBhLGlyurrSU-ojxx6l9KsTiw5_271mcQkE49y4A04GnYRie5lObGxIqqupHE4qvB2MmJNWdfTrmA0I4ypOArXaUuEBV-2s7Ei-yYwBy3Z-d8mRyY2toCpOJtzh81Z6maEVF_vwSoEepgZSUlEvL7oRQYBq6uSKn9H5ow2wSEWDTxCioQg0ew2nXVCCF9yKulMbzIaRyGwpj0Mm1pj5bMh42Uqm8TW0H3hxjaYDBv9O7rW_yNq0GZjGOIOl-8MRHf1UuZ_PZT6epEZDWO9hGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/140320" target="_blank">📅 18:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140319">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✖️
✖️
✖️
🇺🇸
ترامپ به فاکس‌نیوز:
❌
من می‌خوام با مقامات ایرانی
🇮🇷
مذاکره کنم، ولی چالشی که الان باهاش روبه‌رو هستم اینه که اونا مثل موش تو سوراخ‌هاشون قایم شدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/140319" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140318">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/140318" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140317">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
فووووووری ...شنیده ها
🔴
قرارداد استون اورونوف با پرسپولیس با دستمزدی ۲.۲ میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/140317" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140316">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
رسانه های مملکت گفتن آمریکا مجوز لازم رو از چند کشور منطقه برای شروع دوباره جنگ علیه ایران رو دریافت کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140316" target="_blank">📅 17:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140315">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/140315" target="_blank">📅 15:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140314">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140314" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140313">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
⭕️
⭕️
فوری/کانال 13 اسرائیل گفته آمریکا و اسرائیل تو تدارک حمله سنگین به ایرانن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/140313" target="_blank">📅 15:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140312">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fa29145b.mp4?token=DTF1gMgSVfRPpIrg6ZIwFKO0NxkJLyjxQY0Xx_Tv5jj-1xdLiKxeaxPbV8Y7yTeHtiVu4w2pDT6s8dZ_wPM86w70xTUnLyJoj6Iu4Bx2FqeUY_7lHAMRqFOSvrnpdbom3FclAV052HUy1skn0DcAzh0URiN7gl9GPxgxQXRyZ1l9CyMF1FlMp7hsw6XVXQlSkydtmvY6OY5mi90jwwFF5cFn3UxVj6MqQXoNzgVSEdw_24ytul8UNL4SBjDVOc1pbGRrSqe9fgMTU2HMbuAHupHisqmS1iJjOdr9Soko03WC9kGflJV7LLeeZQQR2I3jmGvhDavfd7SW2f7yMQUk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
| فوری از برنا:
⚪️
❌
ظاهراً عباس کهریزی از ناحیه رباط صلیبی مصدوم شده
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140312" target="_blank">📅 15:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140311">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
ورزش سه:
🔄
🔄
علیپور و خدابنده لو به خاطر عملکرد خوبی که تو 6 هفته ابتدایی داشتن، در لیست قلعه نویی برای جام ملت های آسیا قرار دارن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140311" target="_blank">📅 14:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140310">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drmUpS-ARIcc0V4h3swJH9UiQNA6rTM3iYGCH68N68KVbhccgHClni6CspAe3sJ_JOiG0YlS41xjgj6669cicce5qbSjbVCa1UzuU6kdNImyCBUjwOM9P9y_I082lE_57NYpGY7YUtCH8GwgSBxq-r77ptmBxNwt7HKXyM688RWpOrf6BEtUoS6qeiIh-qIp9xyUjfIQDiwqg4itmMq2rwSWP05jH1KCSuqIoBU6sDIBDQO-y-heMtGyONmdtrqMhp1j7bFCADlKW-bWHArprcvFP2eXSixkXFQz_nrrw9BNcv8ULMYwkY4JRBSOnwRxO4FVIlEQRWuxIEZXc3hfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مادرید در انتظار یک شب داغ؛ اتلتیکو یا رئال، کدام‌یک حرف آخر را می‌زند؟
[
اتلتیکومادرید
🔴
🆚
⚪️
رئال‌مادرید
]
⚽️
اتلتیکو با بازی فیزیکی و فشار در میانه میدان می‌تونه ریتم رئال رو مختل کنه. رئال اما در انتقال سریع و خلق موقعیت از کناره‌ها، تهدید جدی‌تری برای خط دفاعیه. دربی مادرید معمولاً پرتنشه و استفاده از کوچک‌ترین موقعیت‌ها می‌تونه سرنوشت بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/140310" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140309">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
اوستون اورونوف و ایگور سرگیف از پرسپولیس به اردوی تیم ملی فوتبال ازبکستان دعوت شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140309" target="_blank">📅 14:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140308">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
✔️
#تکمیلی؛ فرهاد مجیدی سرمربی سابق استقلال ضمن تشکر از حدادیان‌مالک‌نساجی آفر این باشگاه رو کرده و اعلام کرده در ایران تنها حاضر است سرمربی استقلال و تیم ملی ایران شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/140308" target="_blank">📅 14:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140307">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">😰
مدیران نساجی دارن با فرهاد مجیدی مذاکره میکنن تا این سرمربی جانشین مجتبی حسینی بشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/140307" target="_blank">📅 14:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140306">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdPvNrkQ0TYrIrKVNn06NanZNVy6HgJ24L_6hFxg0bq2lXcxOgXz0Ih2VnpMMfmkysLyfrHeTGfx1Nfo7UYq6vZwzX9nlpmU4iRQf9cQSRLPOe3DGdivqj4avzvb_ZTZZO3HpjlGO4fRE3p-2kFiMBA_cctAYHs0TuqHMNaqQf1ohCqrBJgzLfyF5NgAY9QjK265Ta5jKSEtVPitPx4-hyRUi9wtUyQ9oIwVWOROPaUsVPJVIJCU-i0ECMxEaqfnrFdPc9pDOU8Y69hdXhFKLRe_jLEcUNiFV6IdkwE0fw6lmK3acln2aMQTEZZoXF5pyjJznW9fs6taPDljFPdGlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیرضا جهانبخش قصد دارد در پرسپولیس به فوتبالش پایان بدهد
✍️
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140306" target="_blank">📅 11:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140305">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqUD2ndD7sFwSXOgEzcznV7mqKZARVxgGgTqz8K1O3JVXYDNsDiCgorvvbXwT2eCf-2rTAZKeElFvS7V65AdQAjwJovWCkGaGOKJDfcymdHwEmjZE4XFwZsvNn4iR1Ceylq-u06jGsEEuLvMMixdUKZUxxx6sWhUfgFsZ5rg9gR6Nh8Aw-zpJh-4ERleHV-YjYQnu0tQ1fl9b9JY2hPo_44GZLDbpp7w9wLxjGXLSxen2TC15Vd9UVg7k34wAlVqiJJTGqc8TbKTtBiAiZ-Yj_QfxkEhV72GVfpx9f-z7O8WZTgzN5ewHzQvvvN5YvWKZ5rUm6_5JAgLuzXr0xlUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140305" target="_blank">📅 11:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140304">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZCCa6YmageUjgQ11s9uKPYfRPCKq52xIJph_INt9SIJ3p9F3nFoO2z6X5ZKzQgeSlja1FJzB6kXLE_KMfdqpGF9zYsmFYbFsg0pF-XJ_i1Kyve6dhbTXXanUYB2_pTaeXU6ppVtllccK6-xGlUUUUIG0D5XsB0jNcxmQiiTSEspWdvwNx8cURbafEWxwBM_An06FDOwP4riDAOJ5A7LyoXKZE3sUoub9Sy6ZBeXc1zwSOU_DvfYis4QmnFsmhH3EUTUfoWWbZ2DSpNtoCxt-ZghJcdbGt2Wp15CE1ALsE7qu5qR2lHKn9hLXaUgXUjXHIj4iQ8XnCBb2ZDaUbyNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
✅
امیرحسین محمودی بعد از اتمام فیفادی برای تمدید قراردادش به باشگاه میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/140304" target="_blank">📅 11:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140303">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">⚪️
مهدی مهدوی کیا: مجاهد خذیراوی به حقش در این فوتبال نرسید/ حیف شد و واقعا سوخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140303" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140302">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
اعزام علیرضا بیرانوند به خدمت برای یک مهر به دلیل بررسی پرونده کمیسیون پزشکی او، به تعویق افتاده و او میانه مهر به کمیسیون پزشکی می‌رود و در صورت رد شدن درخواست پزشکی، از ماه آبان راهی فجر سپاسی می‌شود.
❌
حالا خوبه این گفته بود سر تعظیم فرود میارم برای…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/140302" target="_blank">📅 09:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
ترکیب تیم امید ایران مقابل چین
✅
✅
محمد خلیفه، دانیال ایری، امین حزباوی، فرزین معامله‌گری، ابوالفضل کوهی، امیرمحمد رزاقی‌نیا، اسماعیل قلی‌زاده، عباس کهریزی، مبین دهقان، امیرحسین حسین‌زاده و پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140301" target="_blank">📅 09:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140300">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140300" target="_blank">📅 07:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140299">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">■
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
🔵
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140299" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140298">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7qv9MokZpGj6Ih7pwmBePtjHssBeeuVEi4ZyUS_bPnq4CqfC2TFt0MQ6fMds0B2rD0O1YMXB3mKTU8Ro-FDtJRcpx4-F4MAA56nbnRF1YCFwFhZ7YCs_VzcMciUL8o1h7X9lTCMwcADh6sHQ336sNWbafQ_5pkXjjhr7pKTEjFAj8i8vdEkWw34shPZHcobL6HgeY61BKSiwFBnpIXMzHYFEySzTaRQJqE7-oqaVMMEwnWCslJ4ju_xtpNs_PoXVo61mBZawyR9xllKdOlc__xCwSpZWuBEQy0M52FFaVtTx0O4wtQIFp6vspQOQM5BuyUfXkldoj9dINAQ2pfuTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم ملی امیدمون‌ امروز صبح ساعت 8:30 به مصاف چین خواهد رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140298" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140297">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
باشگاه نساجی مازندران کسری طاهری رو با 703 هزار دلار خریده و با 863 هزار دلار به سپاهان فروخته!
❌
❌
قطعااااا این انتقال پل محسوب میشه و باشگاه سپاهان تا نیم فصل حق استفاده از کسری طاهری رو نداره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140297" target="_blank">📅 00:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140296">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
❌
دوگزارشگردیگر نیز با صداوسیما قطع همکاری کردند؛ نیما تاجیک و سعید زلفی دو گزارشگر مطرح، خوش صدا و با سابقه تلویزیون بعد از قطع همکاری باصداوسیما به پلتفرم نماوا اسپورت پیوستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140296" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140295">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140295" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140294">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140294" target="_blank">📅 23:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140293">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140293" target="_blank">📅 23:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140292">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHeF9Lpknido5yebaO7DwZVt9TvoqEi5sJZUq79x7PlQ5YTaPNK9d8pWho-Cxt2jh-flq9y8d5hu1cfTd4Azcgi7p-28NFZ6KzJKEQJUsZJeGSZ_zCcGPo9FZ5BDmvMujUta2IP27y_1nylbdqeesXzUk79eMjhSzGf9El8qpc62Pt2pNZGrdmo4FmikudILr9Zyc86Mu74ulvy6Zx0MZ-caOmOZJ-fVT88YDH2sPd3a5COa_O-0DOUwE13Qg3OeAIIks_RJl23gONtfEAM9gp8xfOGTLEuzrUNe6EaiRp-r1uJn1C8e8e37WOpYQ6TOPuf6zGtKk5xRTLbX0O4EFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گزینه جایگزینی یحیی در دهوک مشخص شد
❌
باشگاه دهوک به دنبال توافق با گل‌محمدی برای جدایی است و رسانه عراقی «روداو» این موضوع را تأیید کرده است. مسعود میرال، سرمربی سوئدی، گزینه اصلی دهوک برای جایگزینی یحیی گل‌محمدی معرفی شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140292" target="_blank">📅 22:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140291">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=eKhTf0KGpZwH3XA6qAIL5x5Ymwyub1g5q--o_XyYQpZhkb6BE5zVl9xwFYbo0PS5ZjrpNJ_oBhDMJw8tg9rm5NQjCawqi9wxe6WLlBLpxUgoWSt8eEltfQk9fpDXl3kUuPdIr9jeHRL-exCRxJNExKNXURvvurSEBhPVct3KXaO4ovGEnCb6U38H4I1vZ5dl8DUuTj6-9Jvo4RM9ZtEXsj-qM-PqxzpO1Svzatgs6RLWkx5zJLOMcD1fzdsmQwc7JKVlGQGsJ_wfPHSQY2c74D5A5hFqmnGxobzTjI7egXgDZxZmCXABeZIvnVmmPImA12pZLPoH3_cXuBBwud61Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d7cf776d5.mp4?token=eKhTf0KGpZwH3XA6qAIL5x5Ymwyub1g5q--o_XyYQpZhkb6BE5zVl9xwFYbo0PS5ZjrpNJ_oBhDMJw8tg9rm5NQjCawqi9wxe6WLlBLpxUgoWSt8eEltfQk9fpDXl3kUuPdIr9jeHRL-exCRxJNExKNXURvvurSEBhPVct3KXaO4ovGEnCb6U38H4I1vZ5dl8DUuTj6-9Jvo4RM9ZtEXsj-qM-PqxzpO1Svzatgs6RLWkx5zJLOMcD1fzdsmQwc7JKVlGQGsJ_wfPHSQY2c74D5A5hFqmnGxobzTjI7egXgDZxZmCXABeZIvnVmmPImA12pZLPoH3_cXuBBwud61Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
مرتضی پورعلی‌گنجی تو بازی امروز تیمش دقیقه ۹ اینجوری ساق‌پا بازیکن حریف رو قلم کرد و خورد کرد و اخراج شد
❌
بعدش جالبه اعتراض میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140291" target="_blank">📅 21:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140290">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG4EKl7Z0ZATDRQU76OgtOrjn0Vd3jdMht3SqN-qLp2jioBExuqg_uQTlH4ngV9FblAOCMekRJvipFAoExYEWxc9d0b64AtHsIzjSTDXtTsKq-x-RIz03u5tBzyjHzmFNpIssxh5m0wDaXdSLH5GN9NJEbbjCN_buQG16mJZ_5p5oAUz_sDX6IvU2oK6mw0zAJxbLTSEU1DNGDaJaH5_OBBn1WluD0peIEEn4jKTspBYdA8nOgeN0EdmLcTYbpLVxttaHdcTCFW34tjElLF2lIX5hPKq9icBfaX7SJkz8a33z0qgwJXGwNcbP7qadNE9BoXc0vc3oZ3lytKJU8MW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140290" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140289">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140289" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140288">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔄
🔄
محمدرضا احمدی از صدا و سیما به طور کامل حذف شد و حافظ کاظم زاده مجری فوتبال برتر شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140288" target="_blank">📅 21:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
بشار رسن پست مربوط به بازگشتش به پرسپولیس را لایک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140287" target="_blank">📅 21:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
❌
❌
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140286" target="_blank">📅 20:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6gGz_uLLRfIFc2fY7EP1HUOQX2Qu1sKBges6Pntu9bCy0Cdav68xhY6s-YlnfQtGX_ewygCovBlScM4GzbmckkJue0QZp-oROa51d2MQPCRDJqbg2-2VhD6NhBjO-4n0sKxWJv6YAFPbAJOQXqQlZtQVwm5fXtRfalh7kj8e7m3wOjrjc5SARn2aEz_Tn4MljjJ34z2PrrqYupFuRh19GIC6Md6nP-xcFcFsZl0k5XCOkxRW5ZzuxvCIUfvV0a4QxqfCVsH8q4q4YIdwLSfuAaKx7imPMDDnlBgETLyDwHVxL9xsETLupUBe46MuKl2hpiBe-qH9ysxY8AjerOdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزگاری سیدجلال حسینی با وجود اختلاف قدی بیش از ۱۰ سانتی متری که با کیروش استنلی داشت با پرشی فوق العاده سرزنی کرد و رکورد فوق العاده ای از خود به جا گذاشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140285" target="_blank">📅 20:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
با معاینه پزشکی بیرانوند موافقت شده و اعزامش دو ماه عقب افتاد رسما میره تا نیم فصل
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140284" target="_blank">📅 20:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140283">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA3vIGpMJ6IWAw10XDc455Vrw0PUOjMmF0SvxH6o4leJt0F2EVtNYOoDZiMx2W0GVK7McattOMms3XUCghuLpNBZ992ZadVV9y-PHaDeGpKxZShSaTQx_xTnKid--vP9K2eqcGQuL-4_qkKnSCaGxCI6vLaZEzrsBY7PdAIdRW2kTtBYp7Y5HADefsThjH60UD174hD8B0IDObRbUJFsfYTFxvMsozC9-xEP5YMkP8kcRNgwqjffc8UvPXC3sPJzwujGJSafo-OYqYRsC3zcTQ5XWl7zZETFQwbwsp9_uxJSpjgGuYQ7vsIP_Iu608DugZjE_4CsBVMoaMFx4blI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نبرد آندلوس با کاتالان‌ها؛ سویا سد راه بارسا!
[
سویا
🔴
🆚
🔵
بارسلونا
]
⚽️
سویا با اتکا به بازی مستقیم و فضای هواداری، می‌تواند کار را برای بارسا سخت کند. بارسا از نظر مالکیت و کیفیت فنی دست بالاتر را دارد، اما مقابل فشار سویا باید کم‌اشتباه باشد. تقابل دو سبک متفاوت؛ جایی که مدیریت فضا و استفاده از موقعیت‌ها می‌تواند تعیین‌کننده شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140283" target="_blank">📅 20:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140282">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3xXfsd6kZYt6jFt9T5sigDS2tMndA_756Y6ZbmPFP1U9E5KgxSp8fIBq4KhKBbc5DE6Uod6V0k7opFGY-m7TtJzdTqBa_YHTZ092cw75Ycg2Aug45WJ6lpUE6EPAGqSv9kA9FfNjxK88EMsvWIg9_BPtOE8MgQ2Hh-s07fbahvWA9nqZN9xoFTI-6eONGBSui8yhiXtDNkYaQ33xf6jbxuFuS7vJglSjS6XXu5DZrGnzWXKGEhfuRR2JkLjw_uAcsgnKcjeXPjvNGqaAs_3BjRer8qjnZ_p_Gww2g-PI0gO_YysceMaenYmR39JLOHGSk8yCoa9CCgwVv-p0ahN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرینات امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140282" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140281">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ad9lSVcXuXDfuh4-RjYOxP3-1WKju0Dp3kam9E876MQJKZKxJVc6nR-N-1Iv08hCST067cswtVZvvzaQruK3-gg0q71nxwdNOx3pOb07UVuFCHYnS7yvr0ncPI_2srue0otcHM1FpFnOKkbgVs8oeafjE6R66uZ23wGp7BAXq8ARwZoYHXennckA1C-JB5I0PuFNOO2q5Vu2rAlsBfuoogEwaK_cEAQCzkezpQV9JqlUUq1mMq6VvtGwzbi7_ZwIDyNCrVGUg7yoyfU0bJ0RAbP-ZqLdekru9yP_kATr7KfM56KWSjY9C-tD39RDQ9_RtR_ub1quzkugon75YcX4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
بازگشت سرخ‌ها به تمرینات
⏺
تمرینات پرسپولیس پس از 5 روز استراحت امروز با حضور 15 بازیکن از سر گرفته شد.
🔻
ملی‌پوشان و بازیکنان خارجی تیم غایب تمرین بودند.همچنین حسین کنعانی؛علی علیپور؛محمد عمری؛حسین ابرقویی و امیرحسین طاهری به دلیل مصدومیت زیر نظر کادر پزشکی تمرین کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/140281" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140280">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESETVgqQFdJtIclDpj8p1bvwSp2yiTaImxBz74lqg6gwRF6XyIlayCUVAohwuUkjWQp1rCERs_KnpHkxhCR_Ivr0aVUGH7UHtLvSdoW0-wbv6Po7uUY_jxOTy-iKt7bGewt0XfnowqSqwMungKrniv2s1skrZvoeb0kUP7R2ShWc7kGlAS_p3bYcv7DBpGcIfpyIBig8uWATv5cuGBMgnaC5K2V1WxKo3Mo9NtSe3_VClDWoiGMkqqYcj3F1ENW3OMZXIRCmVeCC_2K0xL3GFiBktiopGDeMlKwFfaNaN53FJZ2nzC2400700H9IfJposSQcxWy3zIIKsDCORIMi1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووری شایعات
🔴
🔁
🇮🇷
ایگور سرگیف پایان فصل از پرسپولیس جدا خواهد شد و مهدی طارمی به پرسپولیس باز خواهد گشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140280" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140279">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227e813e97.mp4?token=U0_peo8X3wY19ku3cMgDYZdmeRXkIITqWdU2o0uBxVtBGcuK0VAkHsqZ_a7GY8HxQDFYsoLGJ6Xukfj5i5u9P-l2ejvJ_wZmbLCea5Us3yQBJdXG9NsXj50gjADbP43PywgWPfOGKLYg947MHRqYa_-iFDUgZ3cPntWhVAVBwri21Dv0URBm_QNCDrzhlkBwetYfoBtYER3K_cuMrPrkzQra5lFHcxSA_ueXjJT5H0B0YVt_BH1Mv40-zGk5fD24eS98uAwZ1TRSfREoqHnYCA3NcJtbHNfCWu1BxmDKSDIjf1E1MD9tIBTn-NSmuAzGP_ZetsYhMBlLpPEkVE5jLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227e813e97.mp4?token=U0_peo8X3wY19ku3cMgDYZdmeRXkIITqWdU2o0uBxVtBGcuK0VAkHsqZ_a7GY8HxQDFYsoLGJ6Xukfj5i5u9P-l2ejvJ_wZmbLCea5Us3yQBJdXG9NsXj50gjADbP43PywgWPfOGKLYg947MHRqYa_-iFDUgZ3cPntWhVAVBwri21Dv0URBm_QNCDrzhlkBwetYfoBtYER3K_cuMrPrkzQra5lFHcxSA_ueXjJT5H0B0YVt_BH1Mv40-zGk5fD24eS98uAwZ1TRSfREoqHnYCA3NcJtbHNfCWu1BxmDKSDIjf1E1MD9tIBTn-NSmuAzGP_ZetsYhMBlLpPEkVE5jLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
گلزنی احمدنور در دیدار امشب کلبا مقابل خورفکان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/140279" target="_blank">📅 20:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140278">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMAsRRW6VrwVV_3X3bvndBoAaYcDmKHEBFu7Ai3mM1QdBlFcLIK8QrSXeJAw0kRXq7ahfOuujCaaLaWT4PkIP1MyME5Pqdz6C2dVffdqCCLWqyy4KDXIt9Wc4YC2RirgipmVU5bDIt0z6NjVDKy2LNWHCWbi3GsiZVsSyD9f5-I1eMY69iSH6n9YJQyXevfEuLakE2W_RylsQE8RBNgQ2xHjlY7vpBYQmb9AB2yiozOaJLCU3Mqpiy8eeMmLSx0GiLbm9ysxI26Tl_rrRU9-UjBAOn-fxKix4gt9mAOuX4tL5EFsNUykjC3pfZG4G190gSYXCQGHYNZq7HBOGWI9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
با درخواست علیرضا بیرانوند مبنی بر انجام معاینات پزشکی موافقت شده و او برای بررسی‌های بیشتر به بیمارستان معرفی شده است. این اقدام باعث تعویق موقت زمان اعزام او (که قرار بود اول مهر باشد) شده است. اکنون مشخص نیست که اگر او موفق به اخذ تاییدیه وضعیت پزشکی…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140278" target="_blank">📅 17:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140277">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140277" target="_blank">📅 17:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140276">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140276" target="_blank">📅 17:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140275">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
بازیهای دوستانه ما تو فیفادی:
✅
پرسپولیس
🆚
گل‌گهر
❌
پرسپولیس
🆚
چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140275" target="_blank">📅 17:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140274">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
✔️
پیام صادقیان خطاب به امیرحسین محمودی:
✅
بهش گفتم سرت تو فوتبال باشه و فقط به تمرین فکر کن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140274" target="_blank">📅 17:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140273">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
بیرانوند قصد دارد پیش از رفتن به فجر سپاسی، قراردادش را با تراکتور فسخ کند تا مشکلی بابت چند ماه باقی‌مانده قراردادش نداشته باشد. با توجه به بسته شدن پنجره نقل‌وانتقالات لیگ برتر، بیرانوند از ابتدای نیم فصل دوم می‌تواند برای فجر سپاسی شیراز به میدان برود.…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140273" target="_blank">📅 17:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140272">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cu_KYdk6oXRHjTrBVN46aQiKz2sigF7HsCPakmOgqYnRV9nmzHQhbSTyfRoUH6e41QAjkLPsEXuIpcLtmzz_r-AnvWS-sFfPirfnDz03oETh55u8MdvksNXcpxDfyFFmiP2yTGMulF9WDCOq0hgrd5WfAjY14jDCskRY8OQL4iGFAnyDLyuFcwnSh0yFFnpd22AGjQdfguQljGZTQkE8-X9f_ZX-P-Ai6l4vCSevoapY6S-s9Jh0hnuaYQL0X2dGKIFwMfD3HT3x6UlvqWgScnMrxD7tPw737gvzdXfNuyIKdlk9ZDvB-CkAsZ2KDgJaICZVW8dGbQgefhs4y39e2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
ROMA -
🔵
INTER
⏰
Tonight 19:30
🏟
Stadio Olimpico
🔵
رم در خانه با تکیه بر مالکیت و فشار هواداران، دنبال کنترل ریتم بازی است؛ اما اینتر برای تغییر جریان مسابقه فقط به مالکیت نیاز ندارد. نبرد اصلی در میانه میدان و انتقال‌های سریع رقم می‌خورد؛ جایی که کوچک‌ترین اشتباه می‌تواند ورق را برگرداند. یک بازی نزدیک و تاکتیکی که احتمالاً تا لحظات پایانی، نتیجه‌اش باز بماند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140272" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140271">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc94830254.mp4?token=RgJcc82xZ2n4W_WZiFr4IbmBr4bo9OIhgdizetMKH34G4IOY6WhnkWCeWzTSqfQoCobvZKRX2Xe9JhMUy2SNw14RwpxyjiCcO2Oow_kUqI3Y-sMGxBYjPlSHiPF_X2XE0SVS1PBnygvC4Fl2A0LJSxTpOyGLp0rWSQBEn2kI2P8EHBPXfhgAN7FbDKG2nkXvA6UJltcVKGcUtpCCgHCjaBK7-_MPvpqtIbx-wKspnlv2wLviPZuMTPVI4k6kmeTtrMT4si585BjdssH56mCvWMdLXdxclLxt8o7W_YbLAK4PgHWIjaEAMK323_-Kw5BhEFSMnW86M9w0FkgV7O8a9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc94830254.mp4?token=RgJcc82xZ2n4W_WZiFr4IbmBr4bo9OIhgdizetMKH34G4IOY6WhnkWCeWzTSqfQoCobvZKRX2Xe9JhMUy2SNw14RwpxyjiCcO2Oow_kUqI3Y-sMGxBYjPlSHiPF_X2XE0SVS1PBnygvC4Fl2A0LJSxTpOyGLp0rWSQBEn2kI2P8EHBPXfhgAN7FbDKG2nkXvA6UJltcVKGcUtpCCgHCjaBK7-_MPvpqtIbx-wKspnlv2wLviPZuMTPVI4k6kmeTtrMT4si585BjdssH56mCvWMdLXdxclLxt8o7W_YbLAK4PgHWIjaEAMK323_-Kw5BhEFSMnW86M9w0FkgV7O8a9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حمید مطهری سرمربی فولاد: پرسپولیس تا الان نتایج خوبی گرفته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/140271" target="_blank">📅 16:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140270">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140270" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140269">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
💢
💢
✔️
✔️
مدیران باشگاه پرسپولیس هفته گذشته‌ مذاکرات برای تمدید قرارداد پنج ستاره آغاز کردند
❌
پیام نیازمند
❌
محمدحسین کنعانی زادگان
❌
تیوی بیفوما
❌
اوستن اورنوف
❌
ایگور سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140269" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140268">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
قراره در فاصله تعطیلی لیگ، برنامه آماده‌سازی پرسپولیس با برگزاری ۲ یا ۳ بازی دوستانه دنبال بشه تا سرخپوشان از شرایط مسابقه دور نشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140268" target="_blank">📅 16:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140267">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kfg1xDJtpwcJxaGuZqGNxofIcggxzQ74BHZLyXNv3b_B21kNwadDb9U-0RYi6TVjH3OJ5Yh_aGQy35KuEzQCnGj2ANBIbDFw4qhSEWr-dEpPyrRredLoChzywhOt4cVt8SvlJW2RNAYmlAc91LN1xNQsODZNqi50ltUeQenbT-52X6zJSDKAj2LMH_pIZ77UE1nv7nPorCoOzxIMwUNlryoT-ZDUfZGKbhPCtNMxldDqectQL5U48shLdD2hQcH9wdRspojon_EacOtCO9-BXnT-6nQ5M2Hlq-Q7_Fn0jIKhX-DtcP5J4KDwXBDnsX4GcESCjcXT1UQIH7Jr26R7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تیتر روزنامه‌ گل درخصوص دعوت شجاع خلیل‌زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140267" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140266">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✔️
✔️
میلاد محمدی در آستانه دیپورت از لیگ بلاروس!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140266" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140265">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
فرهیختگان:
❌
مدیران پرسپولیس معتقدند که مدرک کافی برای پیگیری شکایت یاسر آسانی در CAS را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140265" target="_blank">📅 14:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140264">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
فووووووووری
❌
پیمان حدادی با درخواست مالی امیر حسین محمودی برای تمدید قرارداد با پرسپولیس در صورت گنجاندن بند 1.8 میلیون دلاری موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140264" target="_blank">📅 13:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140263">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
❌
🗞
فوتبال۳۶۰:  بشار برای برگشتن به پرسپولیس پالس مثبت نشون داده.تارتار تأیید بده برگشتش قطعیه
✔️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140263" target="_blank">📅 13:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140262">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
آغاز تمرینات پرسپولیس از یکشنبه در تهران
✔️
✔️
تمرینات پرسپولیس پس از چند روز تعطیلی از روز یکشنبه ۲۹ شهریور در تهران از سر گرفته خواهد شد.
✔️
✔️
برخلاف برخی شایعات درباره احتمال برگزاری اردوی خارج از تهران، مهدی تارتار در شرایط فعلی برنامه‌ای برای برپایی…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140262" target="_blank">📅 13:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140261">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052167cdae.mp4?token=p3TRy9w5PljD7biGPySco_Ix7BfUhtSwxrvYuiVkJatLPLdm2KtlgsyaSBXyblJbmTljFKDnMZOO7gXxuKu3730MzZCfvIlOXZw0NqEDHfimccZ0gt-BAQbOU9HScrJU08sgsdoZ1mhSpdJgvCn4hXcNvEBJTJtm6mYiR87XtXTZyP76PBM8HUEz5Fy-7zZBbXNfQOkGg-CcJBuxSuJTshNOnRCw59ACJ5QxUAK08OBRr9MDoBMu9jGPerphvWaIoKeNeotdmHoCmwkzPeIoJcTcSyYwzK06xOL9EZALaMstJ0i4zqPT6JrZvskASzTeEKNqN3WGYsqg7ksEq8iZXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052167cdae.mp4?token=p3TRy9w5PljD7biGPySco_Ix7BfUhtSwxrvYuiVkJatLPLdm2KtlgsyaSBXyblJbmTljFKDnMZOO7gXxuKu3730MzZCfvIlOXZw0NqEDHfimccZ0gt-BAQbOU9HScrJU08sgsdoZ1mhSpdJgvCn4hXcNvEBJTJtm6mYiR87XtXTZyP76PBM8HUEz5Fy-7zZBbXNfQOkGg-CcJBuxSuJTshNOnRCw59ACJ5QxUAK08OBRr9MDoBMu9jGPerphvWaIoKeNeotdmHoCmwkzPeIoJcTcSyYwzK06xOL9EZALaMstJ0i4zqPT6JrZvskASzTeEKNqN3WGYsqg7ksEq8iZXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
آغاز مراسم افتتاحیه بازی‌های آسیایی ۲۰۲۶ در ناگویا
❌
مراسم افتتاحیه بیستمین دوره بازی‌های آسیایی در ورزشگاه میزوهو شهر ناگویا ژاپن آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140261" target="_blank">📅 13:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140260">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140260" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140259">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg8ETSAbWhyFeh6oLUj3B6m4lJoOcI1GHPuQrciExJjUVP8wRQqU4TkxSjuaSizZ6zM8E2ilNl76zqEx3yovoML3tYCqchWl5RdgJ0V3VljXlFAs-UE8xQLuSLHgLL5XMRX0YgPelb7m61Q4g1KBJjq1gjIkse_OBA673Ng2rANui9_2gpHcxX_I5Ahbis_RKME6i8w-zfytGq7TQwKUa1UxB4X1hkSvh04f4PnyunZky0oEcbmC3Lq5u-th93_k_6RECJP25kduFefBe1vTvqNkSC0stiwTB_eUHWRNiflN-Bg3A892jj-JEroRbTFDczuGO5TGzdMqwvTz3u_Xmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⏳
۴ گزینه‌ی جانشینی مجتبی حسینی روی نیمکت نساجی
🔴
در صورت قطعی شدن جدایی مجتبی حسینی از نساجی، سعید دقیقی، سعید الهویی، محمود فکری و جلال امیدیان گزینه‌های جانشینی حسینی خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140259" target="_blank">📅 11:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140258">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140258" target="_blank">📅 10:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140257">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140257" target="_blank">📅 10:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140256">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl5274eqw7ETwFv1v-y4lBO0bVFBlINf-CeZ6y4ra-K4H3vJlnDCWgZKewsy_Gy34wdSG6bKGBzAMivCx_D23aztfiuMtKa-0O0IWHzR7FxiYn6s2Erpc8C_rdmU7SKsBhdYlNsQxoAZSiDI0dA_5UZEJhY4F5viLWUA6yl-GRpf8OBANGS148R_jQPIsh_9WoslKx5_4Ke6-RWWkLXU9YZ9U4_u6SCOOgx_1CFqAgvWm3h_UWlVpsRUe8vdrQAay-wF3urOZulG91YBpeYWP8Op3bAT-dCpGGMu9Otuwp62XwY9duC-NGbXqoSc-U5xDzbM0Q0nKU4s5-u9lP8K_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140256" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140255">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3GU9-g_dU8bBbKlZu8BjkYpW5sP6bbBR5XsU-n9tB1WzuPkTbqZs5Xcbz-cDNYF-3vPd3cHaam45YgFr341JZt5-aIlSNa-_X-pMLHoYCqvye5Pe5UAGZjg3Go-EbH4d3mlUBnYR0TvbVWOuEt1g4jAoXy6WDaNMnQVLw6JtSlhvQ5ma15mw_FKbHGlA9p4ePbLPnKsVQXkEs2HKz2DYz2YphKquL39HuGT3PF6Xhk313aQvvsixKkbQrNYFmG54HDpfIMgrbTy9IPwBIfHrw34561bAsKNc6NjvApJ80DsYkIlHDEPl2xvqfSN2niujMGjsKR0qF5tqhPqNEYS4dyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3GU9-g_dU8bBbKlZu8BjkYpW5sP6bbBR5XsU-n9tB1WzuPkTbqZs5Xcbz-cDNYF-3vPd3cHaam45YgFr341JZt5-aIlSNa-_X-pMLHoYCqvye5Pe5UAGZjg3Go-EbH4d3mlUBnYR0TvbVWOuEt1g4jAoXy6WDaNMnQVLw6JtSlhvQ5ma15mw_FKbHGlA9p4ePbLPnKsVQXkEs2HKz2DYz2YphKquL39HuGT3PF6Xhk313aQvvsixKkbQrNYFmG54HDpfIMgrbTy9IPwBIfHrw34561bAsKNc6NjvApJ80DsYkIlHDEPl2xvqfSN2niujMGjsKR0qF5tqhPqNEYS4dyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/140255" target="_blank">📅 01:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140254">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
میلاد محمدی که تو تیم جدیدش حسابی ریده گفته میخوام برگردم پرسپولیس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140254" target="_blank">📅 00:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140253">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
❌
پست خداحافظی میلاد محمدی از پرسپولیس
✔️
✔️
امروز با قلبی پر از احساس، از خانواده‌ای خداحافظی می‌کنم که همیشه بخشی از وجودم خواهد ماند. از هم‌ تیمی‌های عزیزم بابت تمام لحظه‌های فراموش‌نشدنی، و از هواداران پرشوری که در هر شرایطی کنارم بودند، از صمیم قلب سپاسگزارم.تا…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140253" target="_blank">📅 00:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140252">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
تعطیلی ۲۵ روزۀ لیگ برتر
🗣
🗣
لیگ برتر حدود ۲۵ روز تعطیل خواهد بود. بخشی از این تعطیلی نسبتاً طولانی به دلیل همکاری باشگاه‌ها با تیم ملی امید است و بخش دیگر نیز مربوط به روزهای فیفاست که از ۳۰ شهریور تا ۱۴ مهر است.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140252" target="_blank">📅 00:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140251">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
⭕️
پرسپولیس مهدی تارتار در این فصل ۴ برد ، یک مساوی و یک باخت داشته ؛ ۱۲ گل زده و ۳ گل دریافت کرده امید گل تیم تارتار ۱۲/۲۷ بوده که با این امید گل موفق شدیم ۱۲ گل بزنیم و امید گل مواجه شده ما ۳/۲۴ بوده و از ۳ گلی که دریافت کردیم دو گل روی اشتباهات فردی بوده…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/140251" target="_blank">📅 00:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140250">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=WPNAfLe8M5kqL7NNMC2busjVaWuJ-d0shPGItB7Ep_CqOfTwdiSsoYpF74Pkiw0aJAkFPISwYOtqhuNmkeAbm9NMFGUzQRD_4OiLzOjuy-64WdX9J8kGLsgo1AYoCZs3jtCyC_DOhIFu-1UrN_Qy5Opy1t7dDrpJZLeY63jliPZoq9zEVwTUy4FXlC8dTlXq67A46TuSzbpV2DJ7BdhaOhRBeOyI_J6WYCDq6G-D_pv62q_m7QIZzi-3XNTbUBRTz6zyO-AiW5zOk94F8tpzVMhHQJq2i4MjZ0h4xhTujUw-dO9nlKZ0dEd2i2N13az16a-jZw0nkr-yzxbBRWgjrafLnA9n1GrzBCCkI_66v2OfCJh1fSRxYmVw8W0pg3uHLpbRnCPS4FXRfKQ_0OIQFk_LZQsNBlOkvkJP7QfxDgWC0tqtzWIbX-Vpz-fMZ75ETG58jl7tAk5wWt39QbobtS2C4cmZZojOxlTJEDshAMkX4F6CYFo507Uqs6VsIU-JjDzU5-4A5BnsL6XodCB5s1HGV6uW_Ai5HUBg0LwivzCOiPohyoUzc80zw7saBaHDqEW6dmfWI3nIgAVl9YkYF5H_-HPu46WIkUVHuzLw42Zs0WKdyKNBpbhorFi2B1IkCZSszTV37jPcLewYCW1RNfEm0si8IsD_BSXYJOveaLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629b3f4d1.mp4?token=WPNAfLe8M5kqL7NNMC2busjVaWuJ-d0shPGItB7Ep_CqOfTwdiSsoYpF74Pkiw0aJAkFPISwYOtqhuNmkeAbm9NMFGUzQRD_4OiLzOjuy-64WdX9J8kGLsgo1AYoCZs3jtCyC_DOhIFu-1UrN_Qy5Opy1t7dDrpJZLeY63jliPZoq9zEVwTUy4FXlC8dTlXq67A46TuSzbpV2DJ7BdhaOhRBeOyI_J6WYCDq6G-D_pv62q_m7QIZzi-3XNTbUBRTz6zyO-AiW5zOk94F8tpzVMhHQJq2i4MjZ0h4xhTujUw-dO9nlKZ0dEd2i2N13az16a-jZw0nkr-yzxbBRWgjrafLnA9n1GrzBCCkI_66v2OfCJh1fSRxYmVw8W0pg3uHLpbRnCPS4FXRfKQ_0OIQFk_LZQsNBlOkvkJP7QfxDgWC0tqtzWIbX-Vpz-fMZ75ETG58jl7tAk5wWt39QbobtS2C4cmZZojOxlTJEDshAMkX4F6CYFo507Uqs6VsIU-JjDzU5-4A5BnsL6XodCB5s1HGV6uW_Ai5HUBg0LwivzCOiPohyoUzc80zw7saBaHDqEW6dmfWI3nIgAVl9YkYF5H_-HPu46WIkUVHuzLw42Zs0WKdyKNBpbhorFi2B1IkCZSszTV37jPcLewYCW1RNfEm0si8IsD_BSXYJOveaLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشته کریمی، ستاره‌ی سال‌های اخیرِ فوتسال ایران، امروز اولین بازی خودشو در قامت فوتبالیست، برای تیم فوتبال پرسپولیس انجام داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140250" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140249">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140249" target="_blank">📅 23:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140248">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140248" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140247">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le5v2PRcB0V36dfA2-d-zPT5XXPn_gpMqi-0VVhuf25YWJeoCFQC48ki5uFERa6Wi6zMDfQrdmDidXIR6jwbBy2ON_cHd3ibE6NkiBJZkquY2AP4ipRbxXDRiZicSEQkgcyMvwpVyWEY2d0mcbXo2VLGqTRj9WXpJ8PcaC3DgyhikidGRWPEAETCn58uiJ5F4uPfb341i3qT6jkmO9MMRafqTJQellBvisE0L_aaqwCq-IUf283LnYSOmf2w5PvDedWeG8jG7IBXPchFBhF1Rg2lQW0Zxd9Ajq3te6-oGYDZG76aSiNHPadL6z1AwOBuOuqSocIf0brUo9cpJTQ7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
اینم تو یه دنیای دیگه‌ست
😂
⚡️
آخه اسکول، تو این گرما این چه لباسیه؟!
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140247" target="_blank">📅 23:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140246">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
❌
اوستون اورونوف به مدیر برنامه ش گفته آینده ی فوتبالیش رو میخاد در پرسپولیس بمونه و با مدیران پرسپولیس برای تمدید قرارداد سازش کنه تا قراردادش مجددا تمدید بکنه
😀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140246" target="_blank">📅 23:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140245">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
هوشنگ‌ نصیرزاده‌ کارشناس حقوقی فوتبال به پیمان‌ حدادی‌ مدیر عامل‌ تیم پرسپولیس اعلام کرده که قرار داد یاسر آسانی با استقلال قانونیه و 150 هزار دلار هزینه حق دادرسی به CAS پرداخت نکنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140245" target="_blank">📅 21:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140244">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140244" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140243">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140243" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140242">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140242" target="_blank">📅 21:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140241">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqM29_aa_kvRGyySixUkaKnSD-QqgC6J0gjSVbtngGh5EPjGi60l_NPmPet8a_rA5Mq8abLVgYUiM0ydAxq6Ak0jTKdJUIwhpE9tajGXStKxEOQmI_uPfON17a-byQHS71OMAu3vxh2aVgUmxhih6Vmvs8vpJIaZJJldX0Phpv4iHV4D_PWx6TNmDx2U6rsqstZ-WP16IZfIKGgDFlTUfUgLs2ClJwoIk2eF2RIUPlmy5kWsNC4eLiX1HFQAqWRt_UIhFjl6sq-RXWiqtyDZ6p12jhZiGstw9thlIzE9u48eV-jSdSn76KYkFCTlFqlRNv_mNhNnqMWQZM_2Ovo1Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
عکس تیمی بانوان‌ پرسپولیس در فصل جدید
♥️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140241" target="_blank">📅 21:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM5awiHxsK_GTgRUO_b_M9oKqUJrff1sW-jFhkX_iRkT4P1U_pe-tkh4dp0H2BaksZwhjbXxDFWU5v3eRU52ZY1qBvxr_pE65NJZsRHFs_b-WkaBr6QI0MMjSVvjSjUzZfpv1pd2jGeUUgCgzErWTzU1nYYrOl34RHSSlKnVReOlrGyvxKVyCvx_eQkz4T10FquMi5oIfH3ru3WoyA2gdbbPQCoHALA5i8B05MQ6HOJmHjR8mgIjttnnnRZwT7GhUed1UvGZgXknl3IlTBsBDQXqwu7nSc2y_xpCtIYE1vDcSUEvphQ7GG42qtKW6zFIdrNPOeM8oUGYZGgxVhTraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Brentford -
🔵
Chelsea
⏰
Tonight 22:30
🏟
Gtech Community
🟣
برنتفورد مقابل چلسی؛ جدالی که برنتفورد با فشار و بازی مستقیم می‌تواند برای آبی‌ها دردسرساز شود. چلسی از نظر کیفیت فردی دست بالاتر را دارد، اما در بازی‌های خارج از خانه باید مقابل انتقال‌های سریع برنتفورد مراقب باشد. با توجه به سبک دو تیم، انتظار دیداری نزدیک و موقعیت‌ساز از هر دو طرف می‌رود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد سایت شو و دیدارهای امشب لیگ اروپا رو پیش‌بینی‌ کن:
👇
🟣
Wincobet.com
🟣
Wincobet.com
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140240" target="_blank">📅 20:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
تست های پزشکی تیم بانوان  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140239" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140238">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=jugjvzKbQmMc_yGs8R3coqL_MYnU4Tbq_CEtpPbrNuiSo-zqDaRX2ihfLlGiTsfpFpwEcxPHWVHDwTxCY8q9Mmqgl1kAetSKWR0piPllvozjFnNTdW8B9W3gPtL-8vlWy3_ldDibnPCQ7NAleLSxQJjdzo4nta3IArCluf43xYb_gGbx1ca_BOiFdwi4BfKF_JmbF77RPLkKaERPneWRHf170b85Zl7gWXdZDgggs-pzj5rObmh3yP03DPpAOlnvvQB4u3Y9EN6I6q_VRiilyO64fsW-v1ryFHaCPjZ7TvKPugtGe-GyVpHiNe9SD6YtC8oVzB8ijK3RVYgYXPOQAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cece536c8a.mp4?token=jugjvzKbQmMc_yGs8R3coqL_MYnU4Tbq_CEtpPbrNuiSo-zqDaRX2ihfLlGiTsfpFpwEcxPHWVHDwTxCY8q9Mmqgl1kAetSKWR0piPllvozjFnNTdW8B9W3gPtL-8vlWy3_ldDibnPCQ7NAleLSxQJjdzo4nta3IArCluf43xYb_gGbx1ca_BOiFdwi4BfKF_JmbF77RPLkKaERPneWRHf170b85Zl7gWXdZDgggs-pzj5rObmh3yP03DPpAOlnvvQB4u3Y9EN6I6q_VRiilyO64fsW-v1ryFHaCPjZ7TvKPugtGe-GyVpHiNe9SD6YtC8oVzB8ijK3RVYgYXPOQAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امید عالیشاه
؛ به جای عزیزانی که اخلاق را در ورزش رعایت نکردند، دچار شرم نیابتی شدم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140238" target="_blank">📅 17:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
عباس کهریزی، آلترناتیو محمد عمری در پرسپولیس!
✔️
✔️
طبق شنیده‌ها مهدی تارتار سرمربی پرسپولیس اعلام کرده درصورت جدایی محمد عمری از پرسپولیس، مدیران این تیم تمام تلاش خود را برای جذب عباس کهریزی وینگر 21 ساله آلومینیوم اراک بگذراند. کهریزی از استقلال و سپاهان…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140237" target="_blank">📅 17:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXpAHwqa_c0gzP-WqM0i4gpNbL4KYWLr7NaWFbKxV-dVkDEARnfihy4ljthjizT6vuighIMBKOi2rLzCeSNq6VB6RammsR_iRI4yiTiHbSXJEkv69RP1pGbf0S-pia7e-je5S-R6zD1bNrQOGnxpxbjMhLsLPqknlP2HxWTCXqvmYz35cLGFAtJ4mE2D-B5L4xyianXFz0jheVpI8TqBPcX16StFZ--VfCTNlT5NW6qUlF3_cIIRoAcEE96r5q4y-RTs6jR1CTQXgyIg0ERpPXyJx1QIJ6nvmUpAD6DP2ARkxh-Es2ZRtnaqFxCD1uPp3RHY3DDGFQZT08Vzmho72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
یکسال پیش در چنین شبی رقم خورد
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/140236" target="_blank">📅 15:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140235">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=WEFQqt3V79vgKqYdiOyIi5JXCLkmHDkChz49E1Z9TJ1hcIR6MVwdWft42n_DNb8-m8XpOMrGMmJ3zidTdd3l3R50TpODafuAzt5GnpV33WwOghM6mamdbKYI9wm66xGUNT5GVD7n3cjUwSYo_d5JAGnulqtYgX8srv4OIn_ph4DSQdhGtaqddiiV9veyhlLj87QI_-9dPUffyGBgnXnRpkYsh4z5B9XhMAXvY_Lpljenw19rWrbMRznuKLhvIjVHkw1KQYgOE44q5BoQuLMi20DG8EQ-FFIZVH3Ow24LhvOkEw1uQIzen5rv2k3FnJW3bkfiA2bbrTbk_dMQaljfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fed8f5a1.mp4?token=WEFQqt3V79vgKqYdiOyIi5JXCLkmHDkChz49E1Z9TJ1hcIR6MVwdWft42n_DNb8-m8XpOMrGMmJ3zidTdd3l3R50TpODafuAzt5GnpV33WwOghM6mamdbKYI9wm66xGUNT5GVD7n3cjUwSYo_d5JAGnulqtYgX8srv4OIn_ph4DSQdhGtaqddiiV9veyhlLj87QI_-9dPUffyGBgnXnRpkYsh4z5B9XhMAXvY_Lpljenw19rWrbMRznuKLhvIjVHkw1KQYgOE44q5BoQuLMi20DG8EQ-FFIZVH3Ow24LhvOkEw1uQIzen5rv2k3FnJW3bkfiA2bbrTbk_dMQaljfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل تیکدری تو بازی دوستانه مقابل شهید قندی یزد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140235" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140234">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=OSQ9e2R7EToOHBurti1GNILbKfHRCB71T3_ICgSuJmSEuMDM49mB5dz0fd9ufPw-T5n4EsNTUyZx5t3Z_pP7k1KsoOhozq5Uixh3wZjwFiS2txbt8w5TChkj1Trs83Xvz1ACy64tDJ8ApvgXz_LLHELacutKL4mzea-ba3k90JFHuXwQTZYIUPoJGi2SHZC-_KZ3HwlUi1WtXX6pXR0FoFoEC0IPmtpx7NGl8avP8HlWNms7XgSOugulbtU_0PZA_4FbmmLW_oy7Ndy2tVmwCd51Fg9eNBIwt6Q7qDGQtDCMHIgb3kOA9IQYHpSx28D9jhWUwLcPw4cAj2RXoiwSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4d62123b.mp4?token=OSQ9e2R7EToOHBurti1GNILbKfHRCB71T3_ICgSuJmSEuMDM49mB5dz0fd9ufPw-T5n4EsNTUyZx5t3Z_pP7k1KsoOhozq5Uixh3wZjwFiS2txbt8w5TChkj1Trs83Xvz1ACy64tDJ8ApvgXz_LLHELacutKL4mzea-ba3k90JFHuXwQTZYIUPoJGi2SHZC-_KZ3HwlUi1WtXX6pXR0FoFoEC0IPmtpx7NGl8avP8HlWNms7XgSOugulbtU_0PZA_4FbmmLW_oy7Ndy2tVmwCd51Fg9eNBIwt6Q7qDGQtDCMHIgb3kOA9IQYHpSx28D9jhWUwLcPw4cAj2RXoiwSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
.</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/140234" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140233">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
محمد خدابنده لو درحالی به تیم ملی دعوت نشد که در 6 هفته ابتدایی لیگ دوبار در ترکیب منتخب هفته قرار گرفت
✔️
✔️
همچنین این بازیکن با نمره متوسط 7.37 یازدهمین بازیکن برتر لیگ از این نظر بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140233" target="_blank">📅 14:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140232">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140232" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzdniqdahHm6MzNIdpePPzC6C4dE10lv90ZLSegHY4l-M_73QeGI-N9_-4QkH4B98bP7aG6F12e1KlbuisafEn8dA2_B1SSclreLXiULSCHM2lk1SdV5czRjRWfgzdM5NR_6fHvGEXcbBkbgPx9wEefiySg_vk8aHPBCuh7KPjTLW2FDBNFd795o314y3crVY6i_G__X5XGISHpvCtVo9H27a2LV9gcETAR8H6O9k16vAxKb04_oAEGXYe5T3-XRIHg4HwdnBnS4FrhJx2CXWaUGebLcvX1YFqlfoM6NI3jWfvK0BjwOpbTb_L4n9SbqucvxoA-deMCg5Q9QcB81MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تا 3 هفته دیگه قرار نیست این تیمو ببینیم
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140231" target="_blank">📅 13:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140230" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/140229" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140228" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140227">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
پشت پرده عدم دعوت کاپیتان‌های پرسپوليس
👀
غیبت کنعانی و علیپور در جمع نفرات اعلام شده لیست تیم ملی سوال‌برانگیز شد اما ظاهرا کنعانی از ناحیه مینیسک و علیپور از ناحیه زانو دچار آسیب شدند و حداقل دو هفته دیگر به تمرینات پرفشار خواهند رسید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140227" target="_blank">📅 13:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140226">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKPF5YeXu9k4abiNzjTugcYPK-j0FvgAwju0S98ai2KQvsRM3T674zPJzHN478geiIBEdujDZhzld5-lGGGLv3cgqOXhjbwO3UW6wkvPxof38Q8f6augFpvvYMjpbWwB-DYPunayGtBAyd1dKJ__yqenNp-5EUGVR0p41bHPqBzLdqFzG_3trCgVuIni-fBwAPnDPQOm3IdcN-_bPRWDbHRC6uSnRsZ8e3_S_JgtEwq2n7CA85D_zBokjgO62xnROGtPZtKAbGzCMFHdGflCVqRt1xVCbMsZH7GEKu3Ss_9FYLjj2JATAz8Fr9-PaVLnvGBh1kUDy3GY26Q-EbsmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن در خانه؛ جایی برای لغزش مقابل یونیون نیست!
[
بایرن‌مونیخ
🔴
🆚
🔴
یونیون‌برلین
]
⚽️
بایرن‌مونیخ با مالکیت و فشار بالا، احتمالاً از همان ابتدا بازی را در زمین یونیون دنبال می‌کند. یونیون برای دوام آوردن، روی فشردگی دفاعی و ضدحملات حساب خواهد کرد و فضای کمی به بایرن می‌دهد. با این حال، کیفیت هجومی بایرن می‌تواند در طول بازی اختلاف را رقم بزند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140226" target="_blank">📅 12:44 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
