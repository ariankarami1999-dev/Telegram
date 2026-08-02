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
<img src="https://cdn4.telesco.pe/file/Te6BxeCKFwqY6rRnwaLYkHo30qZe_quKPBTpaxSbJ5ptDhmWltvG98-XKl9BXiU13LyLd4sd9Mz2t-YtVGjvBjHBfgAGpQAn5iELkzr5sOoslWoai2yOAbO84xWWXQs5MkBeI5MtkJOSLz1rn0PMrjT6Fz-7gGoZQI7KqybmvtVfRJtqfNPx7-37vGjA-3YntnZuJNTkX-_4-oWYTLDTXpYdvPIulAZ_kRLs7HsTqZC-zS0tNYQnaDSRps9bLKo7AoScJl0FsMxFYQp0wpYGYA5aMgDIBK8zxtiGeJ5baUL_Ksivgkdjm-HKiGYcX2QWPxMAGbVgWH5EHebjLOQOaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 04:34:06</div>
<hr>

<div class="tg-post" id="msg-137180">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQCCtnqI5r7rojzO8vuHzlLT5gQ7Ja_FC5pJv7sVCiLRMt7Qy8OV3oLETti0t-mQovuMdyEGn2eKwCCA2xLhZmiHt3xD2iYAgMjEqliN2qZc8KmoAf2ncbe2rBKMcU-AfHII96sDIG3QavjMQJFR2Wxj7NKpG5qNyuo0Swceh_wfmAUCqy1PUJfykIP43m4DTVJ5hUuWK3UvbtLnbaItCTzhOoaKjr4byM9yyP7AW0Z8B6HiligSXizcXWpJ5luOAKoFjLggEDgpGALrSaNCfTyqgkzrMHEndv_ES-znT_rlDDRsgudDF3CL39l3NBKrv4F0euuh1UVpY3BJQAhJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فینال غول‌ها؛ جدال لهستان و آمریکا برای تاج قهرمانی لیگ ملت‌ها!
🔴
فینال لیگ ملت‌های والیبال ۲۰۲۶ بین لهستان و آمریکا، تقابل دو تیمی است که با نمایش‌های کم‌اشتباه و سرویس‌های قدرتمند به دیدار پایانی رسیده‌اند. لهستان با برتری قاطع مقابل آمریکا در مرحله مقدماتی از نظر روحی دست بالا را دارد، اما آمریکا پس از حذف ژاپن نشان داده در بازی‌های بزرگ توانایی تغییر روند مسابقه را دارد. انتظار می‌رود کیفیت دریافت اول و عملکرد مهاجمان در توپ‌های حساس، تعیین‌کننده قهرمان این نبرد جذاب باشد.
🏐
اوج هیجان همراه با وینکوبت، یکشنبه ساعت ۱۵:۰۰ دوتیم لهستان
🇵🇱
-
🇺🇸
آمریکا به مصاف یکدیگر می‌روند.
🔗
برای پیش‌بینی دیدار فینال لیگ‌ملت‌های والیبال با بیشترین آپشن، همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/SorkhTimes/137180" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137179">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
✔️
مدیران باشگاه پرسپولیس موفق شدن‌ با اقدام جدید‌ خود به توافق با باشگاه فولاد‌ برای جذب ابوالفضل رزاق پور نزدیک شوند/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/137179" target="_blank">📅 00:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137178">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ٫ اینترنت سراسری قطع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/137178" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137177">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/137177" target="_blank">📅 00:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137176">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
🔹
فوری از ورزش سه: خرید پایانی پرسپولیس مشخص شد؛ ابوالفضل رزاق پور و دانیال ایری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/137176" target="_blank">📅 00:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137175">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
🔹
فوری از ورزش سه: خرید پایانی پرسپولیس مشخص شد؛ ابوالفضل رزاق پور و دانیال ایری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/137175" target="_blank">📅 00:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137174">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/137174" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137173">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/137173" target="_blank">📅 00:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137172">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/137172" target="_blank">📅 23:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137171">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
❌
شاید مرتضی یک فصل دیگر ماندگار شود....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/137171" target="_blank">📅 23:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137170">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_s_Ro-olZNk8dfswpL5e_B6cS7SMsecpR4Q01KW0EgCbsWZS_Lju-hsoHbLrIj8ZsjXYvjYBeimFM9eE2Hzpz32I4NJHqkqxM9hkgfkUDB3HbKof4hj2Lc62L7SdfWC2lyKVuIXT2fVqtANRAmj6dILvdYzYypsXtm0pOAFHewOvU5tBjqVsO2g_V7S76p7GnGw8OaSXqaWsyMjThx_0sDR-VddLhi5J0Z3Vy7BWTuDR3o8IwzsQHHsFTPcsGJjIj22DqsSeHdbOuN8KDFssigzjP6vZyLBy0nDOc9kDSOUhwy0wK23R_Uw9TaU7_GMVIlu7uiI3EaZLCE-kThMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
علیرضا اشرف به عنوان مدیر رسانه‌ای جدید تیم فوتبال پرسپولیس منصوب شد و بار دیگر به جمع سرخپوشان برگشت
💛
✍️
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/137170" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137169">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔄
🔄
🔄
حسین‌نژاد نمیاد پرسپولیس/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/137169" target="_blank">📅 22:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137168">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
⚠️
باشگاه فردا میخواد برای رزاق پور نامه بزنه و پیشنهاد معاوضه بیفوما و 80 میلیارد پول در ازای جذب این بازیکن رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/137168" target="_blank">📅 22:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137167">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚡️
⚡️
علی بازگشا: پورعلی‌گنجی فعلاً بازیکن پرسپولیس است، اما درباره آینده‌اش هنوز تصمیم نهایی گرفته نشده؛ باشگاه هم سیاست جوان‌گرایی را دنبال می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/137167" target="_blank">📅 22:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137166">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
علی بازگشا: پیگیر شرایط دانیال ایری هستیم
⁉️
در مورد شرایط دانیال ایری از فیفا استعلام گرفتیم. دومین نامه خودمان را به فیفا زدیم تا استعلام بگیریم. فعلا نمی‌خواهم جواب استعلام اول را بگویم تا جواب استعلام دوم هم به دست ما برسد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/137166" target="_blank">📅 22:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137165">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
🔴
🔴
🔴
دانیال ایری مدافع تیم فوتبال نساجی در آستانه عقد قرارداد با باشگاه پرسپولیس قرار گرفته است…
⏳
😀
البته ذکر شده که این قرارداد به صورت قرضی است و سپس اعلام شده باشگاه پرسپولیس میتواند با پرداخت مبلغی این قرارداد را دائمی کند…
🗣
🗣
شرطی در قرارداد نوشته شده…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/137165" target="_blank">📅 22:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137164">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/137164" target="_blank">📅 22:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137163">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
❌
پیمان حدادی: نهایتا یک الی دو خرید دیگر داریم بیشتر نداریم که طی روز های آتی به ما اضافه خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/137163" target="_blank">📅 22:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137162">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/137162" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137161">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
محمد ربیعی هم  در تراکتور ابقا شد.و خبری از اوسمار نیست
🔴
قرارداد ربیعی بند تمدید داشته که در پی توافق با باشگاه تراکتور فعال شد.
🔴
تراکتور نیم نگاهی به اوسمار و طغرل ساغلام داشت و شرایط و وضعیت انها را بررسی کرده بود اما پیشنهاد ارائه شده جدی نبود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/137161" target="_blank">📅 22:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137160">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
ترامپ: هر کشوری جای ایران بود تا الان تسلیم شده بود اما اونا نشدن، من اونا رو تحسین می‌کنم. شجاع و سرسخت هستن ولی خب تهش تسلیم میشن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/137160" target="_blank">📅 22:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137159">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">📎
📎
تصویری از جلسه امروز پیمان حدادی و مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/137159" target="_blank">📅 22:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137158">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
❌
فوری از ورزش سه: دانیال ایری این هفته با توافق جدید دو باشگاه نساجی و پرسپولیس سرخ پوش میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/137158" target="_blank">📅 21:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137157">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
#فوری | سی‌بی‌اس نیوز و به نقل از مقام‌های ارشد آمریکایی:
🔻
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است؛ اقدامی که شامل برق تمامی غیرنظامیان نیز خواهد شد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137157" target="_blank">📅 21:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137156">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzLo8gHRXmT6FR-U2R6vzqBEoo1nqKlE3qIhQpHo9aivSjkD1-x9t6qvXZ3uGCEawr6lBkGcltnAfk4g8Peoe-gw9DfAmernE85uLwbWQQOcYl3HVa2z5VGAsNgEgI5VUk10R_3w7WGdTbMNd81WRHmlZABXyuS-1V3iCnKZ9gvRMH83HRfIl0gf6GrtI4NzxQZTZwyBoTign_1bEoc9M7EhpGI9yS5mWsk-yxDsa4ZBfF99Y36o391Ra1xbQzrwBaCRk5Oyymb0Mz0mCZrMEbgt9ckgzH9eR4ODgA0YPKjE84pSxnJ1QrMlC3Bg7ObWEuBII8kWrA3EFp-P5EdoHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
گفته میشه ورزشگاه آریوی اسلامشهر هم به گزینه میزبانی تیم‌ های تهرانی اضافه شده
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/137156" target="_blank">📅 21:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137155">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⚠️
⚠️
فوووووووووووووووووری
⚠️
⚠️
صحبت های جدیدی درباره باز شدن پرونده انتقال احتمالی دانیال ایری به پرسپولیس مطرح شده و گفته می‌شود این بازیکن ممکن است در این هفته با توافق مجدد بین پرسپولیس و نساجی به جمع قرمزپوشان بپیوندد.
🗞
ورزش سه
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/137155" target="_blank">📅 21:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137154">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
✅
با بازگشت مهدی ترابی به تمرینات تراکتور، پروفایل وی در ترانسفرمارکت به‌حالت اولیه بازگشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/137154" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137153">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه: سیزده سال از عمرم رو با عشق به پیراهن پرسپولیس زندگی کردم. با کوله‌باری از خاطره میرم. برای همه شما آرزوی بهترین‌ها رو میکنم. کسب قهرمانی ها و کاپیتانی پرسپولیس، همیشه در جانم زنده خواهند ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/137153" target="_blank">📅 20:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137152">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16152d790d.mp4?token=O24RZbXmfn6_a6Rc7DLKpXVQLFcMv-22F99KNpHLmMEW5-j3yd3tIcWNN22GURxxrMlA7rgI54KFEefNWO91w3Ye57fE7O0VDRflH4CBTQAelT6nAAdCpXQ7Hp29vrfuAQzqcT2tijKSQfEuKY5m4jwLrdCPq-NOk2Qlpkl8UoNAL-gpKrG9zNrUSEuDf3brlA9DsLNdOPadRtboSC8DB7HSX-s8Zo494-3gQGA0wx5ETgIxYkl1Ab0EdjoZhMXwnzWhHfGGYWOeK5Pqo7qU1plbYL5A63thg5xa0Gxw0iCgVcZWQjliJDyYHevt430v2j0pSdCp7LjuSlJ3FMEBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16152d790d.mp4?token=O24RZbXmfn6_a6Rc7DLKpXVQLFcMv-22F99KNpHLmMEW5-j3yd3tIcWNN22GURxxrMlA7rgI54KFEefNWO91w3Ye57fE7O0VDRflH4CBTQAelT6nAAdCpXQ7Hp29vrfuAQzqcT2tijKSQfEuKY5m4jwLrdCPq-NOk2Qlpkl8UoNAL-gpKrG9zNrUSEuDf3brlA9DsLNdOPadRtboSC8DB7HSX-s8Zo494-3gQGA0wx5ETgIxYkl1Ab0EdjoZhMXwnzWhHfGGYWOeK5Pqo7qU1plbYL5A63thg5xa0Gxw0iCgVcZWQjliJDyYHevt430v2j0pSdCp7LjuSlJ3FMEBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
🔥
امروز تو یه بازی فوق‌العاده حساس ژاپن بلاخره باخت و امریکا به فینال لیگ ملت‌های والیبال جهان صعود کرد
🇯🇵
ژاپن
2⃣
-
3⃣
آمریکا
🇺🇸
🇺🇲
USA= 25 | 23 | 20 | 25 | 15
🇯🇵
JPN= 19 | 25 | 25 | 19 | 13
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/137152" target="_blank">📅 20:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137151">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzpInDuG3tIEPCvSderuUFdp_MRW0vL82JghG-B0XKwqpA8JhbF1MsI2bSTdBQytnhDdX0G1hFIi9iTJOX19kektoVvEi3A7QkcoJgqxiWbnsp5eyYk0uDzcHqVPBn0gSinLrZCLMGZ1WlNzncyem9-LF00dDSIlO2yd8KtFyfNElJW91x1RZHY-MmYuE4dlP4WbcMC3EaQ5L3jA3ZsWOl2fQbFacAEZESopslNQogGSdVjNkrHxz353mIax0v7jip6Z8vJvCxkKr-ZToLqzvmxTY12_8ck6pl3L-WbVa60ImYk5QuvZuJXD9fWG-7WSGLCmyMER-CykudIdXROzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇
⬇
⬇
با‌ارزش ترین تیم‌های ایرانی:
•
پرسپولیس: ۱۶.۵۰ میلیون یورو
• تراکتور: ۱۴.۳۰ میلیون یورو
• استقلال: ۱۴ میلیون یورو
• سپاهان: ۱۲.۸۵ میلیون یورو
• نساجی: ۷.۶۳ میلیون یورو
•  خیبر: ۶.۳۰ میلیون یورو
• گل‌گهر: ۵.۹۳ میلیون یورو
• فولاد: ۵.۸۸ میلیون یورو
•  ذوب‌آهن: ۵.۲۵ میلیون یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/137151" target="_blank">📅 20:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137150">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJXjSO5vK086Ia3H4J94I6yCG8P5yozXJCeSCMgXAFfFTBasadlK2OBroRk-s5w5IX2Si_KdxbJyveRB6OkijAbsvM9tpc2WKZNEoSbhFQ50D5CVEzoa9Qj_bd_v_ELtxDgPJZW7mj10moEHxaOuapCmXVKqPgNlAVFDquW9AABEETZxdx1XJlOAJm7HtP1MKIV3GT2u_HGh_r8tLbdbLow5ykag6KA5Z4KEal7QW4wGdhI5vzLklcVqScRpcQ8MLDkPh5crlYj28z0AQqmXfDiO8VgPtI-9BuhXV5uG0OHfQJHSuA3zSiWNjYUcNKGpQvpB5VJLJgta5slf3-VHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
دوئل تمام‌آمریکایی؛ فریتز به‌دنبال اثبات برتری مقابل ناکاشیمای آماده
🎾
Nakashima -
🎾
Taylor Fritz
🎾
تقابل تیلور فریتز و براندون ناکاشیما، نبرد دو تنیس‌باز آمریکایی با سبک بازی تهاجمی و سرویس‌های قدرتمند است. فریتز با تجربه بیشتر در رقابت‌های بزرگ و عملکرد باثبات‌تر، روی کاغذ شانس بالاتری برای پیروزی دارد، اما ناکاشیما با بازی کم‌اشتباه و ضربات دقیق از خط انتهایی می‌تواند کار را برای هموطنش دشوار کند. اگر مسابقه به رالی‌های طولانی کشیده شود، شاهد دیداری نزدیک و باکیفیت خواهیم بود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/137150" target="_blank">📅 20:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137149">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
استقلال دیگه منتظر رامین رضاییان نمی‌مونه
💢
هوشنگ سعادتی امروز با حدادی درمورد رامین رضاییان جلسه داشته ولی نتیجه‌اش نامعلومه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/137149" target="_blank">📅 20:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137148">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn1bYwUT6EU8p1Jn_wDRJcySQE5ClhF8Rje3k-zgo1-c53pvxfJHD3LFs6cYYrJiGqIyxqd_wTLzlsZ8FOgZF1WXAJo6VrOvX1DOb8h8S3l6Zabpg5Lo03SArP_KkX-f7BKgVONt8Cog5HvRfjYfNE_1uCb05NZrrrqt4n3wRa0AxogPnXY-y8SHBWLxFYEWOv0zSN_8AldfI3i7wDQoRC53tl3CZcxzRLKAJUCz2MRiFWNitUi_abewKiiX5nxS7CrORFe9mPvHcx4LGrK-x4CJ9hYWHrAxzjoMLJg0dRZKSPJdbRDpSLlNQ9YKdJ-tZcH5nln6ckjl5g6AE4AjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📎
📎
تصویری از جلسه امروز پیمان حدادی و مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137148" target="_blank">📅 18:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137147">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
کاروان پرسپولیس دوشنبه‌ شب به تهران برمیگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137147" target="_blank">📅 18:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137146">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQPpFTr7-ioy37rNDzX0f3yFL-g90oNYKvWAPTuihbm02iN2Mb_lRa4gYawyvDp3nKlOwTHpXQbh6nucrhOzNNrhkk6OcB0P13vYMaiyAb8T7hmsZH7zc9QTqLSVqDOm7CZ8YVllYfClPzz2ch_DaZHPUVc-L_PwUcLc__DFSm1GLSZsA2rege2Y7WYwZIoCsj5_piDbiZACWN97d5X-cr8aENufaVaXfrxWOkQrnyrrJ0UByeFudr4VwvR4C9kmio2M1Kop1RAHjfoKHlXJeA6oZ8NXsQnGrY-MaBlLCi-u4yPGi1oXO-LUCDpP3NIjnwkFquiQiUiXThivNNw04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاروان پرسپولیس دوشنبه‌ شب به تهران برمیگرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137146" target="_blank">📅 18:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137145">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔉
دانیال مرادی رئیس دپارتمان داوری فدراسیون فوتبال: تمام ورزشگاه‌هایی که در فصل جدید میزبان مسابقات خواهند بود به طور کامل به پوشش VAR مجهز خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/137145" target="_blank">📅 18:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137144">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
❌
بازگشت اسانی به استقلال و خلیفه به الومینیوم تخلف محض است
🔴
🔴
هر تیمی که با الومینیوم و استقلال بازی کرد بلافاصله شکایت کند.
⚪️
⚪️
همانطور که پیش بینی کردیم می گویند خلیفه به الومینبوم بازگشته و این تخلف است چون استقلال او را معارفه هم کرد و نمی تواند خلیفه…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137144" target="_blank">📅 16:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137143">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/137143" target="_blank">📅 16:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137142">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
ورزش سه: تیوی بیفوما تا این لحظه نتوانسته خودش را به تارتار ثابت کند و در نزدیکی درب خروجی باشگاه قرار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137142" target="_blank">📅 16:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137141">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
محمد خلیفه، گلر جوان و ملی‌پوش آلومینیوم به استقلال پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137141" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137140">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137140" target="_blank">📅 15:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137139">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6Gxen3RmaHrp9AFZT9tMQLXjOu6h0xSKoRA5l05G_sP2tMScnN_OJG-TzKDddpJD-zYx724arV3NWl53nnykGRG_MVBytTVB5OuqYYiEf4lTNCZpY2UgmHilcv3DfpKW4SoH0lzr0nXFXMmmog8Tk3Pa2b_aX6FlSMASNwV4vy7F7d22SWCX1cir1G4ongbxekx7gvlVGWOAlisZrkAIUWemCa1eL5rC0H008_szhJeA0UR9s1yX3vD5cWUX0bMrRgvMsxhFvAMxUT5sXDbteqFfhLmh6NWnwSfddT2ylYEeCaIRwQVBV1PwKaDMytjjk6I8YzHS_BuAkPI2UaNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قدوس در لیست خرید پرسپولیس نیست
❌
🔴
برخلاف برخی گمانه‌زنی‌ها درباره مذاکرات و پیگیری‌های پرسپولیس برای جذب سامان قدوس، این باشگاه علاقه‌ای به جذب هافبک الاتحاد کلبا ندارد و نام او در فهرست نقل‌وانتقالاتی سرخ‌پوشان جایی ندارد.
🤩
خبرگزاری آنا
🥈
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137139" target="_blank">📅 15:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137138">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
آنا : پرسپولیس برای جذب ایری دوباره از فیفا استعلام گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137138" target="_blank">📅 14:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137137">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
پرسپولیس برای جذب ایری دوباره اقدام کرد
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137137" target="_blank">📅 14:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137136">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
⚠️
باشگاه فردا میخواد برای رزاق پور نامه بزنه و پیشنهاد معاوضه بیفوما و 80 میلیارد پول در ازای جذب این بازیکن رو بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137136" target="_blank">📅 14:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137135">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
خبرورزشی : شنیده‌ها حاکی از آن است که با توجه به عملکرد نه‌چندان امیدوارکننده ابرقویی و همچنین منتفی شدن انتقال دانیال ایری، احتمال دارد کادر فنی در تصمیم خود تجدیدنظر کند و پورعلی‌گنجی در پرسپولیس ماندنی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/137135" target="_blank">📅 14:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137134">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGMNZgKOGbcSZahmTuQbkL8aalgh0j36WENV0kjzkifdn6vpCxB6U4ZHkjgO_BEiSogOIM7nghLuD-rtRlM0gy9gsWi68tgbI-GnNuD6xjAK54lXjSAM21xEsan7AVX26RexPTRNmhdtnrIpJbscg2mf6ZqEKSJHdVbdnPYFampX3-tcFcSU_LOGoiY9a_105A4_E1cqwHrqSnLttXx8gbGId4xvTlnwY4_H39D4FDJg_gpXEQ_ipxE1tucbG_Pjsu-xK1DvTfFKbrUAL_Dn4gVxGafxIOOyRBPeTIvEmNt7XV63kTUjvXVjWYHt_GFLipZdkJDAv6oqVlGqGKmSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
آخرین ایستگاه تا فینال؛ هیجان نیمه‌نهایی لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
شنبه ساعت ۱۵:۰۰
[
ژاپن
🇯🇵
🆚
🇺🇸
آمریکا
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137134" target="_blank">📅 13:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137133">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
شهاب زندی مدیرعامل نساجی:  با استقلال درحال مذاکره‌ایم، با توجه به بسته بودن پنجره شون اگه بر سر مباحث مالی به توافق برسیم این دو بازیکن آینده‌دار نیم‌فصل راهی استقلال میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137133" target="_blank">📅 11:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137132">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCiCUuCA2-bvVhTlY7pRkE7LBPUmffB9jXUelcrhSgDfQlXChu5HaWBx0K89xkutgW9SJjLjPkcVDgIWXKv1Doqg8WblVcsDorBxeOVQq9FTPpcNvUr5PIa_Dj2JB5AhCevC6e0OA9pHOzS_EUiy1PTixgOf9w8jum_m2Q_cZ0rnSCwagwee1LkUbic6QLNdRaR325ZBRK7MlSPtfFxKlaLUXIZB881Iy_zdVXikpXGFo7TXrOuqBpkQq4P-O1t7bnLE1YYKNq45GF2RxElT8pdqAy3fkQxvO0CuCZLX0rUIalhDY1Sjj3CIQsDyoUnqobXRlFJKCjCMEjdaNSM1wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز: بمبی که دو روز قبل بر روی یک خانه در قشم پرتاب شده است حامل یک تن ماده منفجره بوده است
‼️
پ.ن خدا لعنتتون کنه ..با مردم چی کار میکنید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137132" target="_blank">📅 11:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137131">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⬅
یکی از نزدیکان مهدی طارمی پیشنهاد پرسپولیس رو به طارمی تایید کرد اما اعلام کرد طارمی به ایران برنمی‌گرده/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137131" target="_blank">📅 11:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137130">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137130" target="_blank">📅 11:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137129">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
🔴
تارتار هنوز اعتقادی به دنیل گرا ندارد و دوباره به او بازی نداد، اما چون پرسپولیس برای جذبش هزینه زیادی کرده و قراردادش هم سنگین است، این مدافع مجارستانی فعلاً حاضر نیست قراردادش را فسخ کند. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137129" target="_blank">📅 11:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137128">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🫥
🫥
علوی سخنگوی فدراسیون فوتبال: برگزاری لیگ برتر بدون حضور تماشاگران؟ این موضوع در جلسات در حال بررسی است ولی لیگ با تماشاگر قشنگ است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137128" target="_blank">📅 09:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137127">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه: سیزده سال از عمرم رو با عشق به پیراهن پرسپولیس زندگی کردم. با کوله‌باری از خاطره میرم. برای همه شما آرزوی بهترین‌ها رو میکنم. کسب قهرمانی ها و کاپیتانی پرسپولیس، همیشه در جانم زنده خواهند ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137127" target="_blank">📅 09:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137126">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
خداحافظی امید عالیشاه با هواداران پس از 13 سال حضور در پرسپولیس؛
✔️
آرزویم این بود روزی که می روم شرمنده شما نباشم
🔴
🔴
خرم آن نغمه که مردم بسپارند به یاد....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/137126" target="_blank">📅 08:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137125">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxNNRQX-iougKS_oUcJwzkpBxI0wgTqRHBb-y0clI6nDDJopXngd435J8eDpwKiZ3fYjDU9-fugsU_tkrVPae9oyWKN3syjj0JJMw7biBj8URtoOItC4-0HpQA7hKAGHP4EsS9MGIfnKyXUflo_x2EvLJrLE8Q1iXH4Jwls1N18jdYbmGjGQa9wy06j-9tvxp1g5Sxm_EXLfWaBB1epbZeNh9f3TKSwYsh0mmk6lkX21LwdgKU_eUmzGoZX8wujTcNBh56od-SFsIXMFqAk8MW3E4ceL6MAYk8KNyLX_p4GmrC8OP0Gc00gnhOkJhsMYco5HeJ57nCgqk68FufkJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137125" target="_blank">📅 08:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137124">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsQUqnFodtabYba10YV7HaKWZ6mi-QRq4pOaMd5TEqzgDAkESuaRYMb_vPanhOcqYEtlWv5Z2-frE9g8Ye6yRKbBwm2Cb8lTLCPM364017xi-_Aer9m-ywYtWhh-If1u14wbpB-LDuUpR-RIWhlHDcJ-ZxCtopEHLx25_2fz8jADIJ-YdOM66_7vqzVroETFXMc87XbihJ1EdTOn4tJ4oH134tPewW7mTPjCygQSOyGw8h9aLW3AnLUZ9yoLVT0a5Xdq_IsxqJYOgAcbLUwzY3tfP2VoTpGQ6ffNP5U0cwvtgdXXA2G0xFbANiXkBa8IlX-hS2zJVoF91wvJBsfezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏐
آخرین ایستگاه تا فینال؛ هیجان نیمه‌نهایی لیگ ملت‌های والیبال همراه با
اسپورت نود
🏐
شنبه ساعت ۱۰:۳۰
[
لهستان
🇵🇱
🆚
🇸🇮
اسلوونی
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137124" target="_blank">📅 02:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137123">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔽
🔽
کانال ۱۲ اسرائیل: شماره معکوس حملات به ایران آغاز شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/137123" target="_blank">📅 02:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137122">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
ترامپ: هر کشوری جای ایران بود تا الان تسلیم شده بود اما اونا نشدن، من اونا رو تحسین می‌کنم. شجاع و سرسخت هستن ولی خب تهش تسلیم میشن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137122" target="_blank">📅 02:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137121">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
❌
❌
شاید مرتضی یک فصل دیگر ماندگار شود....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137121" target="_blank">📅 00:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137120">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACiJrgYEbB6FwNk8Z4zlfh-mzNBTVKTTqVIjEmxQTDOl0wCW6TEYDdkidGpK0gFtr5Sv8QFEUCVoqEE2kq-KM8Ad6buBkgvyw0uOPKvdRldwc33HNu5eCsKVsHkFVEH_w9kTk0MAoCNXw16KdEVk8ybeKjkUOuRujWFTRrygcb3G_szQ_vj545EdKbP0jdZ5putjF8cSAZpPoEvqWWzgzF5wnOlZHcAGXZJ3xgkbqu-eRrM52Pja75bOn8ESUIXXpU2y18q7ScbpZ-Th2uIzMrpA6GOmhfWrRjb37LVgWb0x6_PqXr11CS_o1SPXxOW5Kqvt-t8uIBf3f7sFd-QhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گفته میشه آخرین رقیب دوستانه پرسپولیس در ترکیه این باشگاهه:
✅
7 تا بازیکن خارجی داره با اینکه لیگ دسته اول ترکیه هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137120" target="_blank">📅 00:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137119">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
فرهیختگان: همایی فر عملکرد خیلی خوبی جلو آلانیا داشته ولی تارتار همچنان خواهان رزاق پور هستش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137119" target="_blank">📅 23:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137118">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
باشگاه پرسپولیس خبر داد: امید عالیشاه با توافق دوجانبه از پرسپولیس جدا شد
❌
باشگاه ضمن قدرددانی از فسخ توافقی خبر داد و برای او و سرلک آرزوی موفقیت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/SorkhTimes/137118" target="_blank">📅 23:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137117">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
❌
براساس قانون جدید سازمان لیگ مبنی بر اینکه تیم های حاضر در لیگ فقط 4 سهمیه خارجی میتونن داشته باشن پرسپولیس در حال حاضر 5 بازیکن خارجی فعال در تیم داره باید با یکی شون خداحافظی کنه که قانون جدید سازمان لیگ اجرا بشه
✅
دنیل گرا
✅
مارکو باکیچ
✅
تیوی بیفوما…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/SorkhTimes/137117" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137116" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔄
🔄
دربی افتاد هفته پنجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137115" target="_blank">📅 22:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137114">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!  نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/SorkhTimes/137114" target="_blank">📅 21:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137113">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
اورونوف که به عنوان بازیکن تعویضی به زمین اومده بود با دریبل دو نفر پاس گل را به علیپور داد تا او دروازه خالی را باز کند و به عنوان گلزن بازی لقب بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137113" target="_blank">📅 21:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137112">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🗣
🗣
🗣
شنیده ها حاکی از آن است که دنیل گرا ، تیوی بیفوما و حسین ابرقویی بعد از اردوی ترکیه در لیست مازاد تارتار قرار خواهند گرفت مگر اینکه در ترکیه اتفاقی دیگری رخ دهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137112" target="_blank">📅 21:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137111">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی
✅
✅
منتظر یه خرید خوب باشید......
⚡️
⚡️
این همون خریدی هستش که خلیلی ازش حرف زد و گفت داره قطعی میشه و هوادار پسنده.....نامش آشناست......
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/137111" target="_blank">📅 21:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137110">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚡️
⚡️
فوری/ دونالد ترامپ: در پاسخ به حملاتی که سپاه پاسداران به اردن کرده، ما ایران را به شدت مورد حمله قرار خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137110" target="_blank">📅 21:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137109">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
فرهیختگان: همایی فر عملکرد خیلی خوبی جلو آلانیا داشته ولی تارتار همچنان خواهان رزاق پور هستش.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/SorkhTimes/137109" target="_blank">📅 21:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137108">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا همایی‌فر دفاع چپ ۲۰ ساله آکادمی پرسپولیس تو هر دو بازی دوستانه مقابل پیرامیدز و آلانیااسپور فیکس بود و تو بازی امروز هم ۹۰ دقیقه کامل به میدان رفت
✔️
✔️
با مصدومیت جلالی و جدایی محمدی همایی‌فر فرصت بازی پیدا کرد و میتونه پدیده این فصل پرسپولیسی‌ها…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137108" target="_blank">📅 21:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137107">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhf_fsI6RVaMYZLHHOudDGZD9sAfOyFp9GJpz6ibq2yTOyB8oaVu5NF_jy7R7eVzzdO1F65LMwEYOgvyL1oUlGZ3Zkm3sf0i2duC3gIaTW2kbtABraqPIoq3tvGaKaml0k-YsGS_byGRzyuMYQZ2ZeaQzmg7gzJlaV23OWkF-giswwVB4EGQjzbyVFKWSxCR6NteLMfilU4IRocxMisihoPuC_fWjBkSyeByCBBsOYRnXripHxOi77Ff2awgmx0YH55Ez3LQkaaG7p-YiIB_LPcd4B7bjz5qgbNjKrZmLI2uX7DXoecTbdEye8yx6qqWjner0DZc95KS-eqdHwZbbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
نبرد نسل‌ها؛ جودار جوان در برابر تجربه و کلاس موستی، جودار در آزمونی سخت در مقابل موستی!
🎾
رقابت رافائل جودار
🇪🇸
-
🇮🇹
لورنزو موستی رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137107" target="_blank">📅 20:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137106">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls_GEWxEg3Ub8AOcEMizYRoHGldch55gZh0fXpZrKtAp5Vc46sG32hMxenOcKoKeu_n5vbbZkcL902ta4XVifSW098KR12jnNgSP47WG7RnFS50Z3A1soBDB2C6PI-FENZpQHxvWlAGS1_7YeOhJkN3_ZJkE_vpy4s0nUFJlQPTL3dwGcKq7DNk-21Gk1WN60cLh85jgxgi2tEEYeWrdMqB6OjBIDu2H8nQshGdthbjv_4TFw5DWIDQ-1pI-FxSPuH7zEBMikGmvP2gR9RpI38lvC5fiUjYWfx90rO1vQG3YtTHLF4d0b6XKpLU5PubpyEncR4jGFvdKzwpfLxZ8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
بازیکن آزاد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137106" target="_blank">📅 18:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137105">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgDcuSmmp8Eme07lOSM6RVTs9wS7XCjHKJOZ5OBlBoozBW_714a0kcoKTK10dZMS-BuHKRd5Y6A5os4NTxxPc_I8DJv9wmaKhOiNBgSmavxG3OxBvDfgAEVKIMDaSLzh6s4ZdIV4nlSdGzT1HLRDKThfIf2HhbfOJjfV16GmX0xijVxLRmW9hZFzGRNk5_XoaIbDM93ne-t20OefDQ8Da9rkwTDy6x_FdfsyBEOULod7kGhXwojD-FnGmd3zXlOh7HYI61Z8GfLCK9cabX_YUVwus2TvzTDeF-VS40ved96L_LuoDKNppSB3Ea4V8_ObcUXRdz68mFdwsZ4F7OS5CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌀
🌀
آمادگی بدنی فوق العاده پوریا شهرآبادی
🤌
🔥
⚠️
پ.ن عضلات پارو ببین فقط
😳
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137105" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137104">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
15 روز تا اولین بازی پرسپولیس ورژن تارتار در لیگ برتر مونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/137104" target="_blank">📅 17:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7kwSb7NJeyQP89IGO84_X1Do4IF9ppcIDCf0XRqTjDrbNE9-3JHKjLJH8-lCxx0JExyiIqR3nK975zU_ClG4Cuz0U6HF43Gn-8tPy-BD09Us-pmTfJna7YCUakuDusTx3b1nPUBdkUyAGDm9wnIn4tpA1yTz6gQC3OsiMyHJCZTtdgQwgsjpzE3hA_cE-Jrkjo51Yuh6ogwFdUe1GjncQry5ifps4CXiGFf42E2dJLPD1madeeivyrBcwXXLstud4DERXX2qlFehezfi3qVsWExYVRNFe7IS__NzOlGURZm1zuqPdAv1qhA_qNimju5C_aSYSMqEiF0F031Il4LrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
👤
ایسنا: سامان قدوس در لیست نقل و انتقالات پرسپولیس حضور دارد و گزینه جانشینی رضا شکاری محسوب میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137103" target="_blank">📅 17:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgpNwmaXe0V6EJoToMqBP_d0oJrf3s7lWMA8HzKESYp5hRo4jC2-r1EdgVJ7enK7PRNrDaOeuzF3mOqiO0oe4lKJkwiWG1AJN8mXxFZJ8zVHS8noay-gmEKdgxWI61LYyL_rxR9Ywb80V6URMgjW7zwDswryj6iSEa2OCVg8AW4Ya3KbNO2wwvk1C8_eCNY7ghwAma3164lTpTGZthPPTCEHydtPYJ3wzVKtf-t-8sqnjy3SBjbvibrjUTfHEkvzVPl0MCZdSlzStauyasA_r-Lugj5eeMWOIubLV7Ygpvu6U9NfQiyMOG9mdJHyepiAY2xWdKcce523op9p0dLT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
تمرینی با انگیزه‌ای مضاعف سرخپوشان در اردوی ارزروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137102" target="_blank">📅 17:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137101">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQyRS7syoOVQVHzirfTTp4SpAiJKzUegRiHvTA6RBziDq2SiWjXMxBbYbYTCI8vjmQb2fLEznCcfPvnHmTmhntJXaFabvh8AYCTHzgmqxsiTxqJTeJMcRyfoXKKV-tthSmw_dFnVSrT5yfhXCGEcBUH4OhsrX5IWCkdHt_iTo3-AWgJ-xiB5NfNt2lqkzcV0B5_mMkvJrqUdi6rFkDBX3qLYUg9o5BEuA8l6R0OxMurYickpGChqVMHHCrM5yVRNch4HXIjp3dNQci5OxN79P0aC0k6rFffd6wRZJ6mE8XoBzGIsdDmLpnM8AbVghFHC8SDysQFYIsQH6fegi54YQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
❤️
امیررضا رفیعی به اردوی پرسپولیس در ترکیه اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137101" target="_blank">📅 17:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137100">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
تارتار نه از جلالی و نه از عیدی راضی نیست و دفاع چپ و راست میخواد
☹️
☹️
☹️
///فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/137100" target="_blank">📅 16:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137099">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
ترافیک مهاجمان در پرسپولیس؛ سرگیف مهاجم اول تارتار
❌
پرسپولیس برای فصل پیش رو به نظر ترافیک زیادی در خط حمله خود خواهد داشت در حالی که فصل پیش در این پست با کمبود بازیکن مواجه بود تا در نهایت ایگور سرگیف در نیم فصل سرخپوش شد.
❌
هم اکنون علی علیپور، پوریا…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/137099" target="_blank">📅 16:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137098">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnOCEYgwfcmbCnXKFwVpPKNIbS0Y8tJSdryRj3JntxkyT7lY2Yfs6CO4dQWm1vytk5xbK402YlF_AaFkl6m2JWQyEmSHf2GriFptItB2oAdRmZcMPLtCnin269FzuTo52jrgPNH4kNxC4wVydcqZ48_-3oJAoJdV-dHhHyXBt14dxYuN6KIocWiY_X0g3cBcLTT6RBOHsA-1uWtTw4iUToJXZ3yT1aP-fI-4PLpqnQ8jdcxWd0xib425Rnw--rCigkbZs8DOcBfM4Wh-U1SXiiLl1UZpN6Jfx6iZqBN0eS-igHB4R9Ryv6B2kjK3jRAx-z7aitynEKrrisRrzTOw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽
👀
‼️
محمد عمری ۵ فصل پرسپولیس بوده ۴ تا شماره پیراهن عوض کرده!
۸۰ ، ۷۷ ، ۲۱ ، ۷
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/SorkhTimes/137098" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137097">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
شایعات؛ رامین رضاییان تمایل داره به پرسپولیس بیاد و تارتار هم بهش علاقه منده!  نظرات؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/SorkhTimes/137097" target="_blank">📅 14:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137096">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
❌
❌
#فوووووووووری   |#ادعای_روزنامه_هفت_صبح
❌
مبلغ رضایت‌نامه محمدجواد حسین‌نژاد، ستاره دینامو ماخاچ‌قلعه، به ۲ میلیون دلار کاهش پیدا کرده است.
🔄
هر دو باشگاه پرسپولیس و استقلال برای جذب این هافبک ملی‌پوش وارد عمل شده‌اند و رقابت برای جذب او همچنان ادامه…</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/137096" target="_blank">📅 14:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137095">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
رکوردداران حضور در دربی به عنوان سرمربی
▫️
علی پروین: 25
▫️
منصور پورحیدری: 18
▫️
زدراکو رایکوف: 15
▫️
امیر قلعه‌نویی: 14
▫️
یحیی گل‌محمدی: 11
▫️
پرویز مظلومی: 8
▫️
برانکو ایوانکوویچ: 8
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/SorkhTimes/137095" target="_blank">📅 14:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137094">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFJCC5ievHnEsBdGeNrSiQwMFNTDk1pNQCVQxhIGw7qSYuBvUzr1yaBZtp7Xc3kpR46gHN39GEbjElGzXY5JV3GXAhdmdUoavFl4JOqpwQtUs9IemO-cD2zGgt9k-KsRZ5e0ZkIJBEFa58yQWvo-D2f8RUc8CwKf0izWtpvgRmo74Y3E9EcKNixTzbIS4E98ZJNjtGkjSxn1Xt0QUB04HIlmQU0f5IoL9x65ZOtQemRsaaShxo15AJOojD8-Y3xR74-xqGEixRIEKCT-qnHTX3YofFAxBhc4yY1odB7WmJ5laCKWhJV7DYJAgcNU4UKWcR2gqAtWd4jvbpjlLzzmswsE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=vrzcuD3UkT4aaO4fBTzRBrY_IKxcjI0_bNeblunZ29BKfH6Kezv6LRbOX3erBkdbcczqVW5cgqGi09pY7qAHW-T2R-Dw9EqgFpO18BDnCBtsPaJo9N6MfS28yny7BpgOmNkU5xbpGeMcdexdHauQRNdDYin7WwJPW6twJ7HAO0lK9MIvBP-OTWZBVi8FOFN6PK7UC_sVmyeqwo1lPLnVqTMfp54sm4-422CCh8inO_KqQSf8AXlpOfEhPFFp4GAwR-TNGsqngd_SXxRHo1k3I1M8CTP--IN7i63TivOFNX9catNB627XrtIqJF8wjIuKq4UiZkXyhP5RxtmyMsBYFJCC5ievHnEsBdGeNrSiQwMFNTDk1pNQCVQxhIGw7qSYuBvUzr1yaBZtp7Xc3kpR46gHN39GEbjElGzXY5JV3GXAhdmdUoavFl4JOqpwQtUs9IemO-cD2zGgt9k-KsRZ5e0ZkIJBEFa58yQWvo-D2f8RUc8CwKf0izWtpvgRmo74Y3E9EcKNixTzbIS4E98ZJNjtGkjSxn1Xt0QUB04HIlmQU0f5IoL9x65ZOtQemRsaaShxo15AJOojD8-Y3xR74-xqGEixRIEKCT-qnHTX3YofFAxBhc4yY1odB7WmJ5laCKWhJV7DYJAgcNU4UKWcR2gqAtWd4jvbpjlLzzmswsE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
@Wincobet_bot</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/SorkhTimes/137094" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137093">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
دکتر عزیزی دست به کار شد
🔴
خداداد : میخوایم حسین نژاد رو بیاریم ایران!  پ.ن مبلغ فسخ و شنیدن شاخ درآوردن
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/137093" target="_blank">📅 13:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137092">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
طبق شنیده‌ ها؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ علاقمندسنگالی به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/SorkhTimes/137092" target="_blank">📅 13:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137091">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
فوووووووری از ورزش سه
🔴
خبر شرکت هلیلیویچ در تمرینات پرسپولیس شایعه ست و مدیران باشگاه این خبر رو تایید نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/SorkhTimes/137091" target="_blank">📅 13:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137090">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
طبق شنیده‌ ها؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ علاقمندسنگالی به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/SorkhTimes/137090" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137089">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
🔻
🔻
علوی سخنگوی فدراسیون فوتبال: با جزئیات مقصر اشتباهات معرفی سهیمه سوم ایران به آسیا را به زودی اعلام می کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/SorkhTimes/137089" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137088">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🫥
🫥
علوی سخنگوی فدراسیون فوتبال: برگزاری لیگ برتر بدون حضور تماشاگران؟ این موضوع در جلسات در حال بررسی است ولی لیگ با تماشاگر قشنگ است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/137088" target="_blank">📅 11:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137087">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
✅
✅
بابایی مدیرعامل چادرملو:فدراسیون فوتبال باید خسارت سنگین به باشگاه چادرملو پرداخت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/137087" target="_blank">📅 11:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137086">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
علیرضا بابایی، مدیرعامل باشگاه چادرملو: متاسفانه طبق آخرین شنیده‌ها برخلاف پیش‌بینی‌های قبلی، کنفدراسیون فوتبال آسیا با درخواست فدراسیون ایران برای جابجایی نام چادرملو با گل گهر مخالفت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137086" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137085">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
#شایعات
‼️
3 هفته اول لیگ بدون تماشاگر برگزار می‌شود!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137085" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137084">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
گزینه خارجی جدید مهدی تارتار؛ پرسپولیس سراغ مدافع شاغل در روسیه رفت
❌
❌
باشگاه پرسپولیس مذاکرات اولیه برای جذب عثمان اندونگ، مدافع ۲۶ ساله باشگاه اخمت گروژنی روسیه را آغاز کرده است، اندونگ دو سال پیش تحت نظر تارتار در گل گهر خوش درخشیده بود
❌
❌
گفته می‌شود…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/137084" target="_blank">📅 11:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137083">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
❌
❌
حریفان پرسپولیس در نیم فصل اول:
✔️
هفته اول: شمس‌آذر
✔️
هفته دوم: اس‌خوزستان
✔️
هفته سوم: تراکتور
✔️
هفته چهارم: ملوان
✔️
هفته پنجم: استقلال(میهمانیم)
✔️
هفته ششم: ذوب‌آهن
✔️
هفته هفتم: خیبر
✔️
هفته هشتم: صنعت نفت
✔️
هفته نهم: مس شهر بابک
✔️
هفته دهم: فولاد…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137083" target="_blank">📅 10:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137082">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
حمید استیلی: هیچ جوری نمی‌تونید علی دایی رو حذف کنید
💢
برای چی باید درباره گرانی‌ها و وضعیت اقتصادی ایران سکوت کنیم؟
💢
مگر می‌شه سردار آزمون رو به همین راحتی کنار بذارید؟
💢
بین مردم و بازیکن‌های تیم ملی فاصله افتاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137082" target="_blank">📅 10:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137081">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
❌
حضور مسعود محبی در روسیه منتفی شد/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137081" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
