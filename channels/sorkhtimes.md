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
<img src="https://cdn4.telesco.pe/file/ID3_q2p6PrbMjL_nJ4i_HpG1ccxFQSVW5Qgh4g_SVTCAHK7r9k0kVYPoJ-1kwjwRfp4QC4VQObZwOj3RYI_0MmycLeBPAHIj-s4J5nje0NBjflVRYMFAl3zbeAxjpaiGvFLGa7cjEUKgGarXV06UN72u0drwSF16Ag6HHyBprP4idf5-CAVY675GXRy070juQ1ax2NiMcjxUi8nTEuZ9HEAXcyau_qKSnSa868Q3b0ljGnY7Kmj-1ZTGtwTtig-u1KpW9QFAJf_6LhU36Fw33rTd3UzIiQVk2rZDA4CRH7vdVgPk41aq3QBhEXe0SgoP-1mqOb4QeSKVJN6vkVrJVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 01:44:01</div>
<hr>

<div class="tg-post" id="msg-138753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">7️⃣
وقت چرخشه! | SCARABTEMPLE
🎰
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
💰
شارژ بیشتر؟ اسپین بیشتر!
🎁
هر چرخش، شانس دریافت جوایز نقدی
⚡️
اسپین‌های بیشتر، فرصت‌های بیشتر برای کشف جوایز بازی
😳
👾
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/138753" target="_blank">📅 01:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138752">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❤️
❤️
❤️
سهیمه خرید لیگ برتری پرسپولیس در نقل و انتقالات
⏺
1_مهدی تیکدری نژاد
⏺
2_سید مجید عیدی
⏺
3_محمد مهدی زارع
⏺
4_سید ابوالفضل جلالی
⏺
5_پویا پورعلی
⏺
6_محمد مهدی محبی
⏺
7_دانیال ایری
⏺
8_ خالی...
🌏
سهیمه بازیکنان آزاد فیفا:
⏺
1_خالی…
⏺
2_خالی…
⏺
3_خالی……</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/138752" target="_blank">📅 00:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138751">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
‼️
فووووووووووووری
🚨
ورزش سه: سردار زاهدی بار دیگر در ارتباط با ما اعلام کرد علیرضا بیرانوند سرباز شده و از مهر ماه ( یکماه دیگر ) باید به خدمت مقدس سربازی اعزام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/138751" target="_blank">📅 00:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138750">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
ورزش‌سه:
🔴
الوحده به خاطرات تغییراتی که باید تو لیستش بده تمایل جدی به فروش قربانی داره و بعد باخت امشبش این اتفاق قطعی شده
💣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/138750" target="_blank">📅 00:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138749">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
ترامپ درباره ایران:
🔻
به نظرم این جنگ به‌زودی پایان خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/138749" target="_blank">📅 00:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138748">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/SorkhTimes/138748" target="_blank">📅 00:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138747">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
یکی از سایت های اماراتی گفته قربانی با قراردادی ۱.۱ میلیون دلاری و سه ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/SorkhTimes/138747" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138746">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22323c2ffc.mp4?token=B0jNzx29hCIhQ5ZxaFsXPd61k9i-Ba4LGp6z6xUIgqog_VznLkXfwo0SJ-QVVdKQicY-5KIPfQJmQD5Tf9U55wxqcgLE7HFlnXaUEZnOiODmp6zLlachlx37O2QweU9heFiTz7pRp7OveG41INAM2kWiDd87pB-CQC2s9vA6lQftwNyrPui9sMEq_NOnSkmjhhbt_5fqi2PifdXqGyYLAf5AomaCYB97bB2tscRuNWlu3nMEAQGvVObaUO43Zc8cdWssIV5nreccMlrdiuSmfy-nnHYjU0ITPjN4WvB24ZR7kijAWPOMP3q2_vu2HQ8OF2c15lVVpT7I9nMsO-i9yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22323c2ffc.mp4?token=B0jNzx29hCIhQ5ZxaFsXPd61k9i-Ba4LGp6z6xUIgqog_VznLkXfwo0SJ-QVVdKQicY-5KIPfQJmQD5Tf9U55wxqcgLE7HFlnXaUEZnOiODmp6zLlachlx37O2QweU9heFiTz7pRp7OveG41INAM2kWiDd87pB-CQC2s9vA6lQftwNyrPui9sMEq_NOnSkmjhhbt_5fqi2PifdXqGyYLAf5AomaCYB97bB2tscRuNWlu3nMEAQGvVObaUO43Zc8cdWssIV5nreccMlrdiuSmfy-nnHYjU0ITPjN4WvB24ZR7kijAWPOMP3q2_vu2HQ8OF2c15lVVpT7I9nMsO-i9yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
محمد تقوی، در آنالیز فنی بازی پرسپولیس - استقلال خوزستان گفت:
❌
❌
«در فاز حمله، همیشه ۶ بازیکن پرسپولیس شرکت داشتند. اما جدا از شیوه هجومی بازی با توپ پرسپولیس، بازی بدون توپ این تیم، غافلگیرکننده بود.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/138746" target="_blank">📅 00:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138745">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRjJKWgf67RSW-w8_yWOCSZD0L2TIceAywcYluYqBFhGYrO0KrnJNS8pCjLgEqhMKHIN5fi-skUZ4vcbakL9FfIWnLri-ZUUjfQpa4cBYp4Ye3jEi2DqIoXyScGQLJ-b5BXEveJy41rQYYEJN1FAxyP-wTWVBTMpqkoibDki6CxiL_CnE52aAZ4E8rda6AfozgfyNNa_w3JOnYw_xU3DbKXhRdIyXHfe0pI_WD0-VBwpO71oGKJlyJNrNzbo6vdeQgj_ognkcZiFdoPqqmZ_bN1PBBG-Aan0qdiyqeEzZR2zOyJ7HAvZH0YXfsd46ZTjWz1bXQ7daFPu7baMmDM-kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
مهدی تارتار قصد دارد ترکیبی هجومی در بازی پرسپولیس و تراکتور استفاده کند و ممکن است یک سورپرایز هم در این بازی داشته باشد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/138745" target="_blank">📅 23:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138744">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/138744" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138743">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/138743" target="_blank">📅 23:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138742">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/138742" target="_blank">📅 22:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138741">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
روی اشتباه محمد قربانی و بازیکن دیگه الوحده پنالتی رخ داد والنصر گلش کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/138741" target="_blank">📅 22:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138740">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🟧
🟧
🟧
دیدار پرسپولیس و تراکتور قطعا بدون تماشاگر برگزار می شود
🔻
حجت الله بهمنی سخنگوی سازمان  لیگ اعلام کرد هر دو دیدار رفت و برگشت پرسپولیس مقابل تراکتور قطعا در این فصل بدون تماشاگر برگزار می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/138740" target="_blank">📅 22:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138739">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
حالا شانس ما یا گل میزنه یا میشه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138739" target="_blank">📅 21:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138738">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
❌
فوری از عطا حسینی فرد نزدیک به تراکتور:
✅
هاشم نژاد و ترابی به بازی پرسپولیس نخواهند رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138738" target="_blank">📅 20:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
🇦🇪
محمد قربانی در ترکیب فیکس تیم الوحده
🗣
پ.ن شاید سرکاریم خبر نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138737" target="_blank">📅 20:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138736">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
یکی از سایت های اماراتی گفته قربانی با قراردادی ۱.۱ میلیون دلاری و سه ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138736" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138735">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138735" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138734">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozCFPQ6WB_Air0_i-zmwotTROLNHpfcCJItYt7JSMpl7t695L4LcnI9nbtk8xx78U6Kbxo6QO3sVy4v9tRt_UOxkeaq4vkwNB3qdihxKravFZNaPaaZc390JTYgx9IHhhi_yn5q-DFoOFAj6Avh57oIOvhpdSMAO-8vQp1DQmlPZ-Ym3WaCQyBO5PNcCpbICuQLTs-PIgVKjjKwN78Bx5b4cVP2Mbn7MaqohsQ6wQeW8NwzpairgGaqQ7QrQPs9hXC9xdRH77VTRdPFX3BlughhceEcyUylo1gDjBUQNs7eGAjyqKm0NZ6B5OAXdr8RYf4wEBnEulCpoYF6rEn2Bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه بازی Scarab Temple
7️⃣
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنید.
در عکس فوق شرایط دریافت چرخش این بونوس ویژه توضیح داده شده! هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138734" target="_blank">📅 20:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138733">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
✔️
تارتار به حدادی گفته یه دفاع‌چپ از بین امیر جعفری و رزاق‌پور باید جذب شه/تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138733" target="_blank">📅 18:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138732">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6rP_qi2wLidQRFe6jinN7Goy-dBjCoTevf5X8qeDKgGc2IJPc1zxJVXMdLVj7n8UzpSjtpIdd4_u3CgGVgpLWiQIv8sterAeUv3TCdFQceEf2BCXjsxXc9zBnhQnQxu9WQWMZnbAYFY6DDOUuT8Irslk_zxWtH3HwJa-aKYHG7OHpCTN9JTKoPikaDY3M9sxBfyXzlbUrSwAwlmZxp7SdIoMnN3KNAE0Pjm4BHtaxc4cxppOqeG7tIdtMFyRYd8ASfqPN8E7TXNtf5AVXt_3EMmyc2i_9T8R8JF_ishGNn94imDHRRMRRVX7zA-m1bZFKYQbegxWf6bkRE0N8i5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚽️
✔️
پیام نیازمند با 3 تا سیو موقعیت و ثبت کلین شیت بهترین دروازه‌بان هفته اول لیگ شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138732" target="_blank">📅 18:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
بعد از مصدومیت ابوالفضل جلالی، امیر جعفری، مدافع چپ گل‌گهر دوباره گزینه باشگاه پرسپولیس شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138731" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/138730" target="_blank">📅 18:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa96SNCL_NwPYeN9P_6ravFdre7DYnfN4gAAM6OJ-n_hakUw7dMemqdmnX8ClDFWRLQ2fcXdQQR4QI6W63YNZlIaErjtqDAq81UHB0AVc-9MYNnCcbvgS1yMepdPD-bVdMi4cunumSKH9j_aoHF1uGpQyd64U4dHcVzwkUIO2m4hdnDWL9Z80bN2hyPnjod_fHj5tfPe5Yf03y1gPfY-L5LSOicauvKH2qsVuMel1hBUJm6a7gzh6GMPXfC9VyqKSNQaL24y4ZTcywp1GIvD-DGXN5nnnYtBsvQrUnV_GLSIuPz7PZzRINcyaKeQYDFiU467hUt4NC25-4Cw7xeIgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138729" target="_blank">📅 16:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/138728" target="_blank">📅 16:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138727">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
بعداز مهدی ترابی ، مهدی هاشم‌ نژاد بازیکن تراکتور هم بدلیل مصدومیت دیدار با پرسپولیس و سپاهان را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138727" target="_blank">📅 16:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138726">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
❌
تسنیم به نقل از سردار زاهدی معاون نظام وظیفه گفته که بیرانوند در لیست تیم امید نیست و از ۱ مهر سرباز میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138726" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138725">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
ورزش سه:
🔴
سه سهمیه بزرگسالان برای علیرضا کوشکی، حسین‌زاده و هاشم‌نژاد اختصاص داده شده نه بیرانوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138725" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138724">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔄
🔄
فووووری: چون نام بیرانوند در فهرسته ارسالی اولیه وجود نداشته در فهرست نهایی ام نمی‌تواند باشد و نمیتواند به عنوان سهمیه بزرگسالان همراه تیم امید باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138724" target="_blank">📅 15:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138723">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaEwzXhMlamr0PfaVa1T3wnm1fZ_bk-_2rpJoYxSjUYNRh_IWzGGlRjDPUVvGeaEi6LPVOHx4nTRMmfsjDKsBSrEOdKG_XgXKT7kKAy-l9mQCDLppYvVxiefRdmU-FWyZBUuykwgg_rDixhs5q40gpbS5SyScSpbJXQtF90MMauX4rnRAC-C-SnZAd08OvNnnUFJVzXqcu4EvX6Ip8om8V1PbPB1jO-bpM4k-MYzZlMKldssGMPsSu20F7kvX3hvLl48qJWeH9n_PrXJ0RHVrRqwzXOm4EY0nuRLMG5psFOFbS0cw1wpeuUAqQ-shlmJkq9zPgXsKNffkB1d7KlCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری از تسنیم
❤️
ابولفضل جلالی مدافع چپ پرسپولیس دیدار مقابل تراکتور و ملوان بندر انزلی رو به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/SorkhTimes/138723" target="_blank">📅 13:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138722">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
✅
فقط تا چهارشنبه پنجره نقل و انتقالاتی بازه و تکلیف قربانی باید معلوم بشه.بعد از چهارشنبه دیگه فقط میشه بازیکن آزاد گرفت   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138722" target="_blank">📅 13:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138721">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
‼️
‼️
موافقت فولاد با معاوضه بیفوما و رزاق پور؟فعلا خبری نیست.قبلا فولاد حاضر نشد در ازای رضایتنامه رزاق پور علاوه بر بیفوما ۸۰ میلیارد هم پول بگیرد.
❌
❌
پرسپولیس همچنان مصر به جذب رزاق پور است و راهکارها را مطرح می کند./قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138721" target="_blank">📅 13:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138720">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9646c2be6.mp4?token=iabLgptnihjmKWJrl_Q8HAORvkJitYT-ijZXw-KcHJTn0qhAkS2iP-Yt9XI72QANh2mfuGmN0U3D4U54YsiEl_JuSfEA7PB3GpE5iJt3ETfkCKE3-Bmq3lmbB8InlYz8aMQLZXG-sweM_o4V6-oof8TAgvsfSobmrliTAKfm_lF_eB5YwwOcsPtCVac1icMfqSQIuDoFoYeLNL6Fj6KM2vI2rrVxwg6Ae8KV3Mphn2CiR4D99wamUeEUQS1rWkzsA-2wJC6nY1ZzLNuMpnuhz3LF2gl59hUgiYO7eXcZOpEcYZdZriDbWXGXVGsqqEKj18w3vkReJa45-4Ut_fwDig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9646c2be6.mp4?token=iabLgptnihjmKWJrl_Q8HAORvkJitYT-ijZXw-KcHJTn0qhAkS2iP-Yt9XI72QANh2mfuGmN0U3D4U54YsiEl_JuSfEA7PB3GpE5iJt3ETfkCKE3-Bmq3lmbB8InlYz8aMQLZXG-sweM_o4V6-oof8TAgvsfSobmrliTAKfm_lF_eB5YwwOcsPtCVac1icMfqSQIuDoFoYeLNL6Fj6KM2vI2rrVxwg6Ae8KV3Mphn2CiR4D99wamUeEUQS1rWkzsA-2wJC6nY1ZzLNuMpnuhz3LF2gl59hUgiYO7eXcZOpEcYZdZriDbWXGXVGsqqEKj18w3vkReJa45-4Ut_fwDig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تیم
❤️‍🔥
❤️
✔️
پ.ن جونم به این همدلی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138720" target="_blank">📅 13:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138719">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی بازی با تراکتور و ملوان را از دست داد. وضعیت مبهم برای دربی
❌
❌
ابوالفضل جلالی، مدافع تیم فوتبال پرسپولیس، به دلیل مصدومیت از ناحیه کشاله ران، چند روزی از میادین دور خواهد بود. طبق بررسی‌های انجام‌شده، این بازیکن برای بازگشت به میادین به…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138719" target="_blank">📅 13:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138718">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
دستمزد طارمی در امارات آب رفت.
🔻
سایت threads امروز(جمعه) از دستمزد مهدی طارمی در لیگ امارات پرده برداشت و نوشت: مهاجم ایرانی در الوصل قرار است سالیانه 800 هزار دلار دریافت کند. دستمزد مهاجم ایرانی در الوصل در مقایسه با المپیاکوس(سالیانه 2.2 میلیون دلار)…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138718" target="_blank">📅 13:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138717">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
✅
⏳
10 روز تا پایان پنجره نقل‌وانتقالات تابستانی فوتبال ایران باقی مانده است.
❌
❌
پس از بسته‌شدن پنجره، باشگاه‌ها تنها امکان جذب حداکثر 3 بازیکن آزاد را خواهند داشت. بنابراین روزهای پایانی می‌تواند برای تکمیل فهرست تیم‌ها بسیار تعیین‌کننده باشد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138717" target="_blank">📅 13:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSSNckYMF_pRbNGqzLoyNVrL8LwVwBTKaW0iMsHWTUdOEow6-YxO5FxWopAsD3mJtF78x-j11iSpYW8nIsmjQktC4gpZ_XWMrxlnbe5l1LPXN94aY5JFg3pP4ROCQJHab4Kb1DVRNquEQ8PNc6HnjO4-oReglM6KGKolDyKzpM3JiDoEVEplAIDXkbP996BtHtwblnZdBTuoHQMO7G_A2Gr-QO8uvAKUuVMs-uJoxInf67OK7KBnlez0rKVg9dB2ImegQj4ac1n5YTRqrsAiDPJtGaUYgJ6kDB9T1XyiC9piGbB2PIVEq--d-h0TLKQSBJWmwlp3tN0SzJDRit8tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرزین معامله‌گری، بازیکن پرسپولیس برای گذراندن سربازی به ملوان پیوست.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138716" target="_blank">📅 13:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8_Ip1VIxTd_Q56aAgKKx-PhFNiCq8ZrUgjwX3U6VI5t1FEv5MAs9m1M-pKmwVAu1PRJC83WunFFc2f0-ybtrOWgAQ3LTbLZ6C_WziIqbNXP3OP3ePdjhj3MyyR5BELftOvtpBOown4xS225U-3ls5H20AP_BIue9fB9cQESwYWKr4HV4_IWHgqCaAy9qm6ai_jM8CZD76xOPV4hSqw6XZz1mauGTNfIiDuxrjzxZTWek-Q0E2gzJ13llq5OIeZqTjocGcfg5CFtaVW2snsdOSFzx2i3AVeIaVS2mYKBF0C1nFP21NSfqiLWQ6VuNaNSNOADIA_MrpcbW9HQLgLqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آنا: 20 درصد از قرارداد بازیکنان پرسپولیس واریز شد، و قراره 20 درصد قرارداد بازیکنان خارجی هم بزودی واریز بشه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/138715" target="_blank">📅 13:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdvIwQOGYm_337f1nhXfUQBQLZzZxgkTKQBQa9YCmyj3s5GJafiHH9qmA66tdWYJJv6P94H6bNDa9nCa1wQvzTHfN0_1U3nrX66ouYCKm5qRvwI7lj76asoM73roTLdDg1WnJIEMG0op0O8roqo-Flxu92lkwVcNVcbjJC1QBVxC7qwdY1se-R4ChvCXQNzX5jCozfFl_GnlxWvMednMhA0KOo8I04pPob_jnDwIp2FUjN6-Ob_eKE-ejGp_fwlDi6kYVjhUfj4bwuRt-NEl_yUlN4S7PEY9Er0xVnBdxo7UfbnNsQiRPWEXOPerqN7hIrFlLX_fMGMoaY09xaZ9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دستمزد طارمی در امارات آب رفت.
🔻
سایت threads امروز(جمعه) از دستمزد مهدی طارمی در لیگ امارات پرده برداشت و نوشت: مهاجم ایرانی در الوصل قرار است سالیانه 800 هزار دلار دریافت کند. دستمزد مهاجم ایرانی در الوصل در مقایسه با المپیاکوس(سالیانه 2.2 میلیون دلار) یک سوم شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/138714" target="_blank">📅 13:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
✅
در صورت نرسیدن جلالی به بازی با تراکتور ابرقویی گزینه دفاع چپ در مقابل تراکتور خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/138713" target="_blank">📅 13:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsCAwcuXHGimKMt356IRIpiZJ0sKDl9yCUuWEFKvzNagrU88izHuG2zdU29A2KyrDzahPUQiJS3Twna2RFjrQT1et0Gx1IBZkVT3tAh1PZ2kaPxtNCy2-aCQ9yBSxSM7O_Ly8v9hwkBKmx5PmR0oHYx7n9GgVlAb-9usNbZSE0XB4ORD3oSlMY5gaPMOzPjd0pztngvnRteFD-yYZczK1dmAIBc0S1ZKlyfyksEnicN_yJB8HoUhjWrrbGVDbATn73fynWM0m7oZvWqr7j0vCnW46dsf1MzdO4F7xvXxlxyEvRGAZum0qGCcIDmcEwhBHLSMnc3Isk49f4ImG04jRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شروع فصل با یک چالش تازه برای توپچی‌ها؛ آرسنال در هفته اول به مصاف کاونتری می‌رود!
آیا شاگردان آرتتا فصل را مقتدرانه آغاز می‌کنند یا کاونتری غافلگیری بزرگ هفته را رقم می‌زند؟
⚽️
پریمیرلیگ انگلیس
[
آرسنال
⚽️
🆚
⚽️
کاونتری
]
⏰
جمعه ساعت ۲۲:۳۰
🏟
استادیوم امارات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138712" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/138711" target="_blank">📅 12:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
فوری | سردار زاهدی، معاون نظام وظیفه عمومی:
❌
علیرضا بیرانوند از مهرماه 1405 سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/138710" target="_blank">📅 12:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
فوری | سردار زاهدی، معاون نظام وظیفه عمومی:
❌
علیرضا بیرانوند از مهرماه 1405 سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138709" target="_blank">📅 12:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138708" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138707" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
🎙
میثاقی:
🔴
جلالی بهم گفت حدود ۱۰ ۱۲ روز نیاز به زمان دارم تا یه میادین برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/138706" target="_blank">📅 11:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138705" target="_blank">📅 10:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0oBcMa1xT60zJZSBCsnQ88txU9e6KUtlHc87axDlmP7Ur_XKrb6C5qsNiBk7fiLspn1_wc28_KCSrLZdmKtf70AE5A-8clqmLWLw-OddGjoU1y8as8QPTdMfvp1wd9GNLL58oaoBjZHXPWutlwUezE_L6y-PsJ8yG1zHJYoR-DEA9Acg50nrwI_Qu1R-5EbiXfbPhXx3zgCFdxsb1C3T6hltEqEKDPMcDT7H-E-uGTW_tPgRdoDt4rprysvClGcIIgBee0wY5xjFZIYPBenQ_9734DFjYNlrBlWV1b0_5aPTT-aiAxjBfV8Nm7CavqIqvNSCIUPXLcphRv6NBG9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138704" target="_blank">📅 10:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138703">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس در دیداری دوستانه با گل‌های امیرحسین محمودی، مهدی تیکدری، پوریا شهرآبادی و محمدحسین صادقی، 4 بر 2 آریو اسلامشهر را شکست داد.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138703" target="_blank">📅 10:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138702">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
🔻
🔻
میثاقی: احتمال داره حسین زاده و بیرانوند به همراه تیم ملی امید راهی بازیای ناگویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138702" target="_blank">📅 08:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138701">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
❌
باشگاه پرسپولیس برای جلوگیری از جاسوسی ارتباط تیم با هوادار متمول خارج‌نشین رو قطع کرده اما هنوز به بهانه‌های مختلف مثل اسکان برای بازیکنای جوون با تیم در ارتباطه
🔴
🔴
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138701" target="_blank">📅 08:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138700">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRox6VcMeUEX8XbnXhV3sFfU9XBuuPhQZmo3AK_iovMcsO9ykBcOCff1uBOUK2CNL22FnLseSUsNrSRKwbPoIzGJJATdIVLGBHVagWAyFHmRiFTV1UguvFYXE_qdvO2ia0riUfvRouL0d43MUKQ4AkCZJwkoWaMyE5fjnolLDAOzl1ZB5hVA727AarduxXP3qVDNqbHvQc0WMSJSiC30LckSgOPQKHbBvcGxLiFc7qlOfI32JYQnZXxgFwO8y7XLKoBteHJ2haIFpK9ienH7zXaL_8TUdpmlwVewDZJJRrEFcZPF0r-37LJzYBvgk0tHmYQ86U2jwynz8jFT4M5jTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138700" target="_blank">📅 08:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138699">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">7️⃣
وقت چرخشه! | SCARAB
TEMPLE
🎰
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
💰
شارژ بیشتر؟ اسپین بیشتر!
🎁
هر چرخش، شانس دریافت جوایز نقدی
⚡️
اسپین‌های بیشتر، فرصت‌های بیشتر برای کشف جوایز بازی
😳
👾
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138699" target="_blank">📅 02:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138698">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس، پرسپولیس فصل آینده در لیگ یک تیم داری خواهد کرد و اگر مشکل خاصی پیش نیاد بزودی امتیاز فولاد نوین به پرسپولیس منتقل میشه؛ در صورت نهایی شدن انتقال امتیاز فولاد نوین…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138698" target="_blank">📅 02:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138697">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🏆
🏆
دربی تهران رسماً در استادیوم نقش جهان برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138697" target="_blank">📅 01:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138696">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
حدادی: دوران بازیکن سالاری و دخالت هوادار متمول در پرسپولیس تمام شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138696" target="_blank">📅 01:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138695">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚡️
مدیر برنامه آسانی: نامه فسخ دستکاری شده است
🔹
مدیر برنامه یاسر آسانی، هافبک استقلال، انتشار نامه فسخ قرارداد این بازیکن را تکذیب کرد و مدعی شد نامه منتشرشده با هوش مصنوعی دستکاری شده است.
🔹
رسانه‌های مختلف امروز نامه‌ای منتسب به فسخ قرارداد یاسر آسانی با…</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/SorkhTimes/138695" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138694">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/SorkhTimes/138694" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138693">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/SorkhTimes/138693" target="_blank">📅 00:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138692">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
🔴
🔴
پیگیری کردم؛ ابوالفضل جلالی احتمالا به دلیل مصدومیت بازی‌های حساس پرسپولیس مقابل تراکتور ، ملوان و استقلال را از دست بدهد. در واقع یک ماه دور از میادین.
🟫
🟫
🟫
البته خبر پارگی رباط صلیبی صحت نداره چون زانوی جلالی نچرخیده که رباط بده و خودش هم با پای خودش بدون…</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/SorkhTimes/138692" target="_blank">📅 00:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138691">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✖️
✖️
احتمال معاوضه بیفوما با رزاق‌پور وجود داره.
🔴
تارتار تاکید ویژه داره رزاق‌پور جذب بشه. البته تارتار فعلا در قبال رد کردن بیفوما پاسخی نداده.
🔴
ولی درخواست فولاد همینه. بیفوما رو بدید رزاق‌پور رو ببرید.
🎤
سپهر خرمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/138691" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138690">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138690" target="_blank">📅 00:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138689">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138689" target="_blank">📅 00:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138688">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚜
علیرضا بیرانوند در تلاش برای حضور در تیم ملی امید ایران برای ۳ سهمیه بزرگسالان میباشد تا با کسب مقام احتمالی در مسابقات آسیایی از خدمت سربازی معاف شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138688" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138687">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/138687" target="_blank">📅 23:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138686">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🟧
🟧
🟧
دیدار پرسپولیس و تراکتور قطعا بدون تماشاگر برگزار می شود
🔻
حجت الله بهمنی سخنگوی سازمان  لیگ اعلام کرد هر دو دیدار رفت و برگشت پرسپولیس مقابل تراکتور قطعا در این فصل بدون تماشاگر برگزار می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138686" target="_blank">📅 23:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138685">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
❌
حساس‌ترین بازی هفته سوم لیگ برتر پشت‌ درهای بسته باید برگزار شود؛در شرایطی که براساس رای فروردین 1404 کمیته انضباطی و تائید استیناف تمام دیدارهای تراکتور و پرسپولیس مقابل هم در مسابقات لیگ برتر جام حذفی و در دو فصل 1405_1404 و 1406_1405 باید بدون حضور تماشاگر…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/138685" target="_blank">📅 23:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138684">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un50eICkP8u2AG41PA0bpHdAOUiXcMo46-yocOZUITG0h4fw_duDeETvIhl2kTSy6vSGobFjJPqEkPD4mPWbbJgVgM-y8JKZ8YOaLnuT_8ngheHbi3XiWcZmvX7uKgrADJ4nAWOrrh357FZWL3H-FyyjfRK-UGr3Cpjkls4wrr7MH2w0bo5bn4rsXtWvPT-v42B_HuKI8xh9quxo7XVbsesjVTz5J4CMOqPO9OtlwbZGQQdexq3_PpJpF3za3wvE2Xumqaw74tX1K7FWA0Nm2g6WUq-CaP1uJuWMgSk5OX9UBYQmtBVTh_tVK67Ph5t5xvYG1b1c8_gaaCXx3LgMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138684" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138683">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8400611245.mp4?token=OckMbx7WDdJCkmIV_1bItVMYQLzx0FXEt2nS4tOTe7YBCBV4URQNp5RYSGDTlwNeritrQ5ez9VBRHqHb9-Ga5yUrtpxc3NLtpWRokS15mdy8OZ8e94xUDMqqAU4dy4utgflk5c6QkaY_qNkZ3Qw-PIJHFP3D-P4G3oE2RyjaFd625i5ncYuwItnzdhGNQpd2ldOhFBsvEFjYr4Whc82w-AsoSzXD2tRBq5x918qxB-Ah8UCSPO2QSOA5j_RCuTaaPQ1NEOdWrSxIychov5h7gjzsPIHor3NHsMUjwUTvLU-hQ3geEUGHlJ90ipQOatZZ3UyAnbvX-vPFZKd1CMfThw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8400611245.mp4?token=OckMbx7WDdJCkmIV_1bItVMYQLzx0FXEt2nS4tOTe7YBCBV4URQNp5RYSGDTlwNeritrQ5ez9VBRHqHb9-Ga5yUrtpxc3NLtpWRokS15mdy8OZ8e94xUDMqqAU4dy4utgflk5c6QkaY_qNkZ3Qw-PIJHFP3D-P4G3oE2RyjaFd625i5ncYuwItnzdhGNQpd2ldOhFBsvEFjYr4Whc82w-AsoSzXD2tRBq5x918qxB-Ah8UCSPO2QSOA5j_RCuTaaPQ1NEOdWrSxIychov5h7gjzsPIHor3NHsMUjwUTvLU-hQ3geEUGHlJ90ipQOatZZ3UyAnbvX-vPFZKd1CMfThw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازگشا سخنگوی باشگاه پرسپولیس: فکر نمی کنم محمد قربانی را باشگاهش بفروشد/ پرونده هیچ بازیکنی را برای جذبش نمی بندیم ولی در خصوص این بازیکن با توجه به مبلغ قراردادش اصلا وارد جزئیات برای این انتقال نشده ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138683" target="_blank">📅 22:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚽️
🔻
بازگشا: شیر ما برگرفته از هخامنشیان و نماد باشگاه ماست، اما شیر استقلال و نمی‌دونم از کجا اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138681" target="_blank">📅 22:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138680">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🚀
آف ویژه سرویس نامحدود
🚀
1‌کاربره فقط و فقط 600T
2 کاربره فقط و فقط 700T
3 کاربره فقط و فقط 800T
ثبت سفارش و پشتیبانی:
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138680" target="_blank">📅 21:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138679">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
🔻
🔻
طبق شنیده ها فولاد در آخرین جواب به پیشنهاد پرسپولیس خواستار معاوضه بیفوما با رزاق پور شده.
❌
همه چیز به نظر تارتار بستگی داره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138679" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138678">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
💢
💢
باشگاه میخواد یکی دو بازیکن جوون رو وارد معامله با فولاد کنه تا با قرض دادن این بازیکن ها و مبلغی پول رزاق پور رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138678" target="_blank">📅 20:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138677">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/138677" target="_blank">📅 20:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138676">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pzahw5Eb2dte6OkYlnKDli97OTQqwZ5sD2nbr3wj6E5GEO90b_Jhnsyx2ZmRd-gSQwFNlObzOwRqyDSPBj7-YiLoj1bKiebAWiHlD6b1sjQYIMwwz-ICPT1R1q6hnVcSrGBzGUVJl2q9PN1MEb7KgaLBUnMiw3mvzv1HMbzu8JE13-F-YOdxLwvOZFoaCzkoYMksB54ZWM8FlGP8FP85gyTfnk4nsohJ6D5863FIIuQfROvl9c2zKyxDR656H1u_pI5-xVAwUA7khNbHQi_Il7mbwvcJ5wp23BJqxTwcalnOAx6wPEvlFI5_nMzDkLrO10l8nRmUhBo9JsChK3sldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
فوری ؛ یکی از مدیران الوحده امارات در گفتگویی با رسانه الریاضیه این کشور اعلام کرد که رقم رضایت‌نامه محمد قربانی برای فروش این بازیکن به‌ دو تیم بزرگ ایرانی و خارجی رقم 1.1 میلیون دلار است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138676" target="_blank">📅 20:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138675">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnyEhjToA-MSXkae4TZyQR-5j5DOdDzvPzNR8w6S6fOFxkCvv9jNOlPDJ6KuzxXkmmNznY6yPlTDPdJjwGwmKNqNkgzxbp-arvFMXt2As04TaeVB_0vf2RXryM15nNg1XBnZzPzJo9vGOfQrEqr9hlzayh0gk9F2EszKN1t1gEYAtf0L-RspmM44cpUGBlJuTQablRwjFRVZaqO0bbSn47ssWIaqs0rv9vScpJRFsgTHW-yjtK3DWGbsXiNl7hIB0ACteFmZx_IFoGtwbdvETbwfc1KrJYolicf_GFOnujuJ77JnHB6HaMC7KxRsnn7h80wBXAFJenXsb4tdh5Uyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138675" target="_blank">📅 20:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138674">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=rTnv6VMzGGHCcm8E09oqdSG4NDczi8cMM3EpFe-ZWCf0xL_xY1CGz_QXBPmHywjIMOxmqptI4DvXSqb0aukrIV73J8hoyrmppDmJT8-py71XptwnpYqm-UQGXE2SYnbKn3MJ_i-O0ATQXMdlov7fshHQFIdi5O_FJ8DSDv8nXGMJuzf9-ko6316yr6ONywzwYgZwb4q6WCATdiHH-yq0drQxR8qpdwZPf2Zff6t0j6aykPhIRIxBZSsZnSU4Wp3GeIMq83Bp2AJcIrS9paj-Uj1k4t3n7mm_nTlX4_1Dg34-q0rvFITs186yFOPW2ezDLhfit-ZRsD9dVf0qn36VlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=rTnv6VMzGGHCcm8E09oqdSG4NDczi8cMM3EpFe-ZWCf0xL_xY1CGz_QXBPmHywjIMOxmqptI4DvXSqb0aukrIV73J8hoyrmppDmJT8-py71XptwnpYqm-UQGXE2SYnbKn3MJ_i-O0ATQXMdlov7fshHQFIdi5O_FJ8DSDv8nXGMJuzf9-ko6316yr6ONywzwYgZwb4q6WCATdiHH-yq0drQxR8qpdwZPf2Zff6t0j6aykPhIRIxBZSsZnSU4Wp3GeIMq83Bp2AJcIrS9paj-Uj1k4t3n7mm_nTlX4_1Dg34-q0rvFITs186yFOPW2ezDLhfit-ZRsD9dVf0qn36VlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
🏅
این شاهکارو از دوربین باشگاه هم ببینید
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
❤️
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138674" target="_blank">📅 20:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138673">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAbs5E2eK-8ZFCvCo_UXgtO3hmbjBw1EpN6NP_ns81KL-FNurWEAmpEkuZl7VnZbTxNqDFSAVwyleQcAE9Pvrl_fMQgc5c6dsXpWFc9vUDKiL428xCjbHhcLqLn_R2xkmHPHVnlHsfXLmvMyOyfNvDQj8aGVdEY7vQ4xPQmDElj6Tvvlq9uuJE3BInOfr0nSeAO7TUcD5oVfqm5pbpB2K_JFhepUvUSc8A6_hOBcG8_TtTWIfto3f7RBYMdlThVKIQTV_eHP4xUiZHD8Wbbj6HkEwa7IuqMScNM88TByli8BvdI3VXjsyVSiC3Ztfns4tG_dcU6ipSs6e7LRWxtrKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه بازی Scarab Temple
7️⃣
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنید.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/138673" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138672">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔔
⭕️
احمد العتابیه، رئیس نقل و انتقالات باشگاه الوحده، در مصاحبه اختصاصی با رادیو ورزشی دبی تأیید کرد که محمد قربانی، هافبک ایرانی، در آستانه جدایی از این تیم است و خاطرنشان کرد که دو باشگاه ایرانی علاقه جدی خود را برای جذب این بازیکن در پنجره نقل و انتقالات جاری نشان داده‌اند.
❌
العتابیه اعلام کرد: ما مکاتبات رسمی از دو باشگاه بزرگ ایران برای امضای قرارداد با محمد قربانی دریافت کردیم و این بازیکن در صورت توافق نهایی این باشگاه‌ها با مدیریت الوحده، پذیرای یک تجربه جدید است.
❌
العتابیه فاش کرد که ارزش غرامت مورد نیاز برای جدایی این بازیکن ۱.۱ میلیون دلار (معادل ۴.۰۴ میلیون درهم امارات) است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138672" target="_blank">📅 19:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138671">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138671" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138670">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
✔️
فووووووووووووری
🚨
مهدی طارمی برای عقد قرارداد با الوصل امارات راهی دبی شد
😳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/138670" target="_blank">📅 17:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138669">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔄
🔄
🔄
فدریکو پاستورلو؛مدیر برنامه طارمی:
🔻
جدایی‌ مهدی‌ طارمی‌ از باشگاه المپیاکوس قطعی شده است.
🔻
درحال برسی پیشنهادات هستیم و به‌زودی تیم جدید طارمی رو معرفی خواهیم کرد.
🔻
مهدی یک آفر از لیگ ایران نیز دریافت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138669" target="_blank">📅 17:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138668">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0ViWknjvVc0r5Y2zHCjxm3VeoZbHXaVaIQElneuEpBNRkMfb84QOKIQC4SJKc8329mBRNyyRDYBq_Xk_13jBId2AseL8AmLLW13vp_97VbPPRis-Mto0qIIRD83QaPrGrq45KxOcZbElzdczsEDdarf5ewixbAALyrW4WEKiBcj6N5MpJn8GwzPsAxgbg9yt_Rq_4I1rmWLvTWr-pdkGTrA6rVOCvpx0V-xwDtR8vc5swvV0_iQQgT3P1sjwjQXMgOem5rFJjjn3Z0N-Mv6WoOQEbXUj6s2QmTsc0VpOyt7iV-YvfKTrJgHKZStyKUjE0CRj2LMHIDhSLSt0wCy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
شایعات: الوحده امارات با فروش محمد قربانی موافقت کرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/SorkhTimes/138668" target="_blank">📅 17:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138667">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
ایشون بازم نخ داد
👀
🚨
کامنت محمد قربانی برای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138667" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138666">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇪
یکی‌ از خبرنگاران نزدیک به باشگاه الوحده مدعی شده که محمد قربانی با عقد قراردادی سه ساله به یک تیم ایرانی پیوسته.
⏺
اما اسمی از تیم مقصد نبرده و گفته این قرارداد به زودی رسمی میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138666" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138665">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💢
💢
💢
💢
مدیریت بانک شهر صبح امروز به وعده‌اش عمل‌کرد و 800 هزار دلار بودجه برای جذب محمد قربانی دراختیار مدیریت پرسپولیس قرار داد.
❗
❗
مدیربرنامه‌های‌محمدقربانی  به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/138665" target="_blank">📅 17:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138664">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/138664" target="_blank">📅 16:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138663">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwFmR9N0FPz7-mec-nM_HLau7QY4NN0Jjx9wPVNkbqzqlgnLufSkCFJ_qED8yhf5Nt0RblvD4q7ifS4MxY4m_MQKHGE2PJI2t6gjxD3TkocjV_6cP9EO7tyiPlhuJ2b1Pb4Li2I8Mhg1LpkManrxGD9It8lEuPoNR3o3c6QlOj4ZpkyLpu5YTuwrdMBEUdth-VsjB57Fw-2bDolTmLiu65IjQnk3020PAYrTsnpy9MO76s6eklxg3bTJzw_tzmL69EyO4sypE1JVSHHpjE5_TgatSpUdPhAvGqdMFRLtRCaJV7C1MeLEfk0fzO73QzRXw_flwW_irwS4DwMWPKQlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138663" target="_blank">📅 16:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138662">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
تارتار: چون جلالی از قبل هم مصدومیت داشت، وقتی نتیجه ۲ بر صفر بود ترجیح دادیم ریسک نکنیم و او را تعویض کنیم.‌ما در پست او همایی‌فر را هم داریم که از جوانان خوب است اما نیاز داریم در این پست تقویت بشویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138662" target="_blank">📅 15:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138661">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
✅
مشاور قالیباف اعلام کرد: با تصمیم سران قوا، گرانی بنزین منتفی شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138661" target="_blank">📅 15:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138660">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c71PlzohQ2enLhMJOSmBF4t9aKulLe70_qAvP63AyFoSateLdTvT8xo6-f6SyUj3QM5ut0j9mFW5WRkuyz1V0SQKCZL0mjFhfeBHapeIoHNMWKhRywfowjIfCrgcDeKu-AkQ82ZVFO-0N_IA44gFKQVxR7s-a5HX1m8HmSkFFHPNPNL5b119w1YSEcBXbzHSVYC07dIvJaNawBqJ2pqgZlVrr4H-ql3WUppzPhZU7_oNwPCeS-Itl_6UZ6hY7Wuqyy0T_QGbjuTtbCqZFFMTT3NqhmdO5-u0NLUNJMe2-0QGWCzzfbMJBcgux6n19y9dAcQjMDdpksv8ppsHoWiYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/138660" target="_blank">📅 15:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki3pFa0S6HA7_AFqVELXfjsv67_ORUkKcSKVZFiIkblx9bU9-jrUyjjDX4iI9EdRtH63OWGkFVP0KHh_XfY7g8jdQZmOipCB6cSmvSvl6DZ3uAvUdw6cRzUQJztLdl_sY0Ww74N0Ad5ThyqMCkez3NSYp_Iw535EyR3HTU71MKwZra9VTLjvujhnypJ4jt9-sfDUz2UF44ATUqdAi5IrEEaZzTbEOhfcHz_p2idqa1hnxBXJC0aQt3o6Qa_jJtAQyoxQSDPaToOFatgtuS5IstH5bPJ4xUBakOMLDswHLMXCJg28v7uplglE3LzZJ-LIYreIKFSF2uLDN62AEO0zPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید عیدی با خلق 4 موقعیت مسلم گلزنی خلاق ترین بازیکن پرسپولیس در این بازی بود
🟧
یک پاس گل به علیپور
🟧
یک ارسال دقیق برای جلالی
🟧
یک ارسال دقیق قبل از گل مملی
🟧
یک پاس پشت دفاع تک به تک برای علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138659" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇪
یکی‌ از خبرنگاران نزدیک به باشگاه الوحده مدعی شده که محمد قربانی با عقد قراردادی سه ساله به یک تیم ایرانی پیوسته.
⏺
اما اسمی از تیم مقصد نبرده و گفته این قرارداد به زودی رسمی میشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/138658" target="_blank">📅 13:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
پنج بازیکن برتر پرسپولیس در بازی دیشب :
⏺
علی علیپور 8.45
⏺
ایگور سرگیف 7.83
⏺
محمد خدابنده لو 7.72
⏺
پویا پورعلی 7.68
⏺
محمد مهدی محبی 7.41
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138657" target="_blank">📅 13:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
فووووووووری
🔄
🔄
شنیده میشه حسین ابرقویی مجددا درخواست جدایی داده و گفته میخواد جایی باشه شانس ملی پوش شدن داشته باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138656" target="_blank">📅 13:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
✔️
پنج بازیکن برتر پرسپولیس در بازی دیشب :
⏺
علی علیپور 8.45
⏺
ایگور سرگیف 7.83
⏺
محمد خدابنده لو 7.72
⏺
پویا پورعلی 7.68
⏺
محمد مهدی محبی 7.41
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138655" target="_blank">📅 13:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWBQ_svxDhzJ-MeZ9AnYZ3Yb_QdZY1W-llS_9q3gtW7AYzZL_jklhgYvkR7-36nUitH3Q7bS43yMZdlrofgLwkoZORyUZemUBugRP7vggibLEnP8VXm1ZjvPL0F0DhBjyR-uWBpwMqy_Qf4GvgafCBfKi3tVA1UIi5GghTm1gpDGII1OsfO9GWpsoNJ--jYmGrnter8ebhfIt52K6uSNEunDitbaVSGcC7dvZVUUB-Q1-dsX4nNc87QNMKyZKh62PVC8TVgCSv6g0J6im_HLx47tGlQs7ALL-a5POypkpfLEqEZw5kGGsH5OCmGglj5Cf_8AtKl26TPTpQfH6wnagw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
️ بونوس اختصاصی چرخش رایگان بازی Scarap Temple
💰
کاربران اسپورت نود می‌توانند از همین حالا، با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
💸
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138654" target="_blank">📅 13:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">⭕️
⭕️
⭕️
😰
😰
شانس
🚨
🇮🇷
🇸🇦
رسمی؛ استقلال و تراکتور با خوش شانسی تمام به تیم‌های عربستانی نخوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138653" target="_blank">📅 12:52 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
