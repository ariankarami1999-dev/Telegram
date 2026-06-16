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
<img src="https://cdn4.telesco.pe/file/hxGTR6gecU4w7fW4D2v93s3rQ7zn-fNhTJqiDUJSXGZNoRFtSJ0MHK-UXQd00YZzDi5IWGK6kS3vvJGzbrwVsRxgYYrWn_ZuC3pc5AsGoKCRjfM0_SperiC3hQmRNQ88Aolv7tcJOWvcyboi4UXhrJP353bX-1aEYi6Ew5qHqS56l5B-25gPRpiy7uwEa_JEWNTTczzfdosOnSkgyGm0ZUNL1Sp74zLIF99ziKy-Zu07v_6Ep1fZGF1f00cIx7gGYxAcMSFR_HBoKvDzOwvfvMkMPhd-dzHL-aMs4HLIwsR0Kth1z65q4gdN7QP6pcENgNUUURXKEWUfYktIkadACQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 9.68K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 🚀آرشیوتلمرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 06:23:54</div>
<hr>

<div class="tg-post" id="msg-6404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">علی تاج رو میذاشتی جای دروازه و دفاع خیلی بهتر عمل میکرد
⚪️
@ArchiveTell
| $aDrA</div>
<div class="tg-footer">👁️ 493 · <a href="https://t.me/archivetell/6404" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🛢
نفت خام:
81.5$
|
دلار: 159,050 تومان
🕰
بروزرسانی - 26 خرداد 1405 - 03:04
🪙
قیمت لحظه ای رمز ارزهای پرمخاطب:
🟢
BTC:
$66,152.52
(+1.00%)
🟢
ETH:
$1,786.95
(+3.76%)
🟢
BNB:
$615.87
(+0.07%)
🟢
XRP:
$1.24
(+4.98%)
🟢
SOL:
$73.79
(+4.37%)
🔴
TRX:
$0.32
(-0.41%)
🔴
DOGE:
$0.09
(-0.86%)
🔴
ADA:
$0.18
(-0.05%)
🟢
PAXG (Gold):
$4,304.90
(+0.65%)
🚮
قیمت ارزهای تلگرامی:
🔴
TON:
$1.71
(-2.06%)
🔴
NOT:
$0.000448
(-7.03%)
🔴
DOGS:
$0.000044
(-1.64%)
🔴
HMSTR:
$0.000158
(-6.08%)
🟢
EVAA:
$1.258452
(+88.39%)
🟢
X:
$0.000012
(+3.86%)
🟢
MAJOR:
$0.035791
(+2.66%)
🔴
PX:
$0.017240
(-0.23%)
🔴
STON:
$0.578778
(-0.88%)
🟢
REDO:
$0.077989
(+10.89%)
🔴
UTYA:
$0.019192
(-7.00%)
🔴
DUST:
$0.000175
(-2.63%)
🟢
TONNEL:
$0.627903
(+4.80%)
🟢
FISH:
$0.005469
(+1.74%)
🟡
قیمت طلا و نقره:
🌍
انس طلا (دلار):
4,335.20$
🌍
انس نقره (دلار):
70.01$
💰
طلا ۱۸ عیار (هر گرم):
16,296,900
تومان
💰
طلا ۲۴ عیار (هر گرم):
21,729,000
تومان
🥇
سکه گرمی:
25,500,000
تومان
🥇
ربع سکه:
47,620,000
تومان
🥇
نیم سکه:
85,960,000
تومان
🥇
سکه بهار آزادی:
163,625,000
تومان
🥇
سکه امامی:
167,010,000
تومان
🥈
گرم نقره ۹۹۹:
377,140
تومان
🛢
قیمت نفت:
🇺🇸
نفت WTI (تگزاس):
81.5$
(+1%)
🇬🇧
نفت Brent (برنت):
83.7$
(+0%)
#دلار
#طلا
#نفت
🫀
نبض بازار در دستان شماست...
‌</div>
<div class="tg-footer">👁️ 740 · <a href="https://t.me/archivetell/6403" target="_blank">📅 03:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">https://ren-6zrx.onrender.com/sub/CHAT</div>
<div class="tg-footer">👁️ 722 · <a href="https://t.me/archivetell/6402" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAssa</strong></div>
<div class="tg-text">بچه ها شرمنده یه خبر باید بدم بهتون
من تحقیقاتم از سایت render بر اساس هوش مصنوعی بود الان شخصا سایت و قوانین رو چک کردم
مثل اینکه bandwidth رو ۵ گیگ میده اما پروژه اولی خودم تا ۲۵ گیگ مصرف بعد ساسپند کرد البته این هم بگم من کانفیگ پخش کرده بودم و تقریبا سه روزه داره دست به دست می‌چرخه با کاربر بالا
الان هم کد بهینه تر شده کمتر گیره
خلاصه که شرمنده بازم درباره اطلاعات من احمق برای اطمینان هم از جمنای هم از Claude هم پرسیدم
😑
💔
البته اگر قبلاً ورسل زده باشین میدونین که اون سقف زیاد مهم نیست و اگر شخصی مصرف کنید و ترافیک عجیب رد ندین کم کم برای شما تا ۴۰ گیگ میره بعد ساسپند می‌کنه
ورسل به اون بزرگی با هابیش ۳۰۰ گیگ رد دادم حالا این رندر که چیزی نیس
😂
بگم که ریلوی سقفش همون ۷۰ گیگه
و اینکه اگر ساسپند شدین فوقش با ایمیل فیک ثبت نام کنید و یکی دیگه بسازید بیشتر از ۵ دقیقه کار نداره
بازم عذر میخوام باید شخصا تحقیق میکردم</div>
<div class="tg-footer">👁️ 896 · <a href="https://t.me/archivetell/6401" target="_blank">📅 02:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzIEF5uxmVT6w6jmnnusFbQ3oxDWoU13ypadYGBZe3iioKppjOtqOIGaYrcjemHoYVX0gHaGe2xitKTC0qUbGOPiNnALfG0tM-l07JiboyxTA0WmouNZlr292plyAD7trJRvhcdnC7IanmepzOeHDbmCvyVBrdbHcu48DWBaytmpmWPEPt7wRtxA2jT4u_hJwhCpiDuDR1kcR26HNs3oQ3GC6N8fxxL_Bh7c6MVNVBdrK9wnIW31MPCAWBPpNax9IsakPJVprJGBjH_dwUPohsemJXegps7JWzSGA_U3HE-87Kc_E6m-SwpPrYSi52P8_st5oNMvJjfAtwZ0GidRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/archivetell/6400" target="_blank">📅 01:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حجم: نامحدود
زمان:x
vless://9bdd3d97-27e0-40bb-ba2f-c89cbe970318@naroto.96s.ir:80?mode=auto&path=%2Fobito&security=reality&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A%221000000%22%2C%22scMinPostsIntervalMs%22%3A%2230%22%2C%22xPaddingBytes%22%3A%22100-1000%22%7D&pbk=y_WO1jyTc3ROz1aF_FbuIranHlEbjg4jNhXiBuSnqFU&host=naroto.96s.ir&fp=chrome&spx=%2FgWP01C5SFWa4ZX1&type=xhttp&sni=www.yahoo.com&sid=25b6e1e9e80f#Obito</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/archivetell/6399" target="_blank">📅 00:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حجم : نامحدود
زمان : تا فردا صب
متصل روی همه اپراتور ها
✅
vless://b5730518-4cc5-4922-bd0b-8c0f3da190a6@65.109.191.83:8443?type=ws&path=%2Ftest&host=play.google.com&security=none#%D8%AA%D8%B3%D8%AA</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/archivetell/6398" target="_blank">📅 23:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087fb590da.mp4?token=EiyH2ogH-b_1maQ9J7gMO55jBxyhp4nNOcfK03YmreMdDHyCaOVr03VhPY3yNMYdHZINAempno4Wg7DfFmOOPMiRMgy5vjp26R_N7qJWlWb0YBSU2cUDvt4jk4PClVfVSt6lsNPLr_Gl4-UaiXJHn6yRlxQHXVyB_KGbfq7Mvngd88QM7szPLSBqNDw8fYup_uFCbYsiyIHarziRNHnsM3Gt6RI0dwRv8UAbN1NwcohhtZCJhKyBVjChMJ7r6StweRzF60aq90YWT06-jARvPCJn1pYxmY8hjxY93b_hnJ_uvkhtePzmeztUi1g9IYwBLnRdcFJAwKN5ubs5okdSaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087fb590da.mp4?token=EiyH2ogH-b_1maQ9J7gMO55jBxyhp4nNOcfK03YmreMdDHyCaOVr03VhPY3yNMYdHZINAempno4Wg7DfFmOOPMiRMgy5vjp26R_N7qJWlWb0YBSU2cUDvt4jk4PClVfVSt6lsNPLr_Gl4-UaiXJHn6yRlxQHXVyB_KGbfq7Mvngd88QM7szPLSBqNDw8fYup_uFCbYsiyIHarziRNHnsM3Gt6RI0dwRv8UAbN1NwcohhtZCJhKyBVjChMJ7r6StweRzF60aq90YWT06-jARvPCJn1pYxmY8hjxY93b_hnJ_uvkhtePzmeztUi1g9IYwBLnRdcFJAwKN5ubs5okdSaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک پروژه متن‌باز جذاب برای ساخت ارائه با کمک هوش مصنوعی!
دیگه لازم نیست ساعت‌ها برای ساخت اسلاید وقت بذارید؛ این ابزار رو می‌تونید روی سیستم خودتون اجرا کنید و با هر مدل هوش مصنوعی دلخواه، پرزنت حرفه‌ای بسازید.
✨
ویژگی‌ها:
🔹
پشتیبانی از OpenAI، Gemini، Claude، Ollama و مدل‌های دیگه
🔹
ساخت ارائه از روی متن، فایل و اسناد
🔹
قالب‌ها و تم‌های قابل شخصی‌سازی
🔹
اجرای کامل روی سیستم شخصی
🔹
رایگان و متن‌باز
🎓
مناسب دانشجوها، مدرس‌ها، پژوهشگرها و هر کسی که زیاد ارائه می‌سازه.
🔗
Github
#OpenSource
#AI
#Presentation
#Productivity
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/archivetell/6397" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حجم : 1 ترا
زمان : نامحدود
متصل روی همه اپراتور ها
✅
vless://3b71df7e-c358-442f-91bf-4ba658223173@138.124.88.172:443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#1%D8%AA%D8%B1%D8%A7</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/archivetell/6396" target="_blank">📅 19:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌍
افزونه Local Translator
؛
افزونه‌ای متن‌باز برای ترجمه صفحات وب بدون ارسال داده‌ها به سرورهای خارجی.
💡
اگر دنبال جایگزینی سبک و خصوصی برای مترجم‌های آنلاین هستید، ارزش امتحان کردن را دارد.
🔹
ترجمه کامل صفحات یا بخش‌های انتخابی متن
🔹
استفاده از Translation API داخلی Chrome
🔹
حفظ حریم خصوصی؛ پردازش روی دستگاه کاربر
🔹
دو حالت نمایش: جایگزینی متن یا نمایش ترجمه زیر متن اصلی
🔹
ذخیره خودکار تنظیمات و فعال‌سازی خودکار
📎
GitHub
#Chrome
#Translation
#Privacy
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/archivetell/6395" target="_blank">📅 19:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEN73MCNmvPRVl-ygIzmj6IV3YcxDEbNEZbmiwbO8KuLEQn50Hp5Wq7XGw4EET7OME6IYLrCHj81BTRH9oKvBawGfLSsa38az91MczFUWjrlZBfk1TPk3mNEIBLsDfWsQC9HJIeLe8CS0FIx-jYwpighfLGFfpN9ig-ne8GJN2ROfgue_VuqtZlSfSz3VEzFHiPM6LlWNnrkEczyQT7yvmmJS0HF9ioA_Ntx8HZF-94Ya9RGIhfd8Np24_4yzgU542901W9NexS1-JvPMQlG8gKoU8KCahyMQKUuFC89gQSKQI7I1gw_BwGtANL4Pw-lsdHQausLKFotitxcnom6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با افزونه SkipBait میتونید ویدیوهای یوتیوب رو سریع خلاصه کنید و دقیق‌تر داخل محتوا بگردید
🎬
✨
قابلیت‌ها:
•
🔹
خلاصه‌سازی سریع ویدیوهای YouTube
•
⚡
جستجو داخل زیرنویس‌ها و متن ویدیو
•
🤖
پرسش‌وپاسخ با هوش مصنوعی درباره محتوای ویدیو
•
🌐
پشتیبانی از جستجوی وب برای اطلاعات تکمیلی
🔗
لینک
#AI
#ChromeExtension
#YouTube
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/archivetell/6394" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارش‌های تازه از پیش‌نویس توافق آمریکا و ایران
🇺🇸
طبق گزارش Reuters، پیش‌نویس یک تفاهم‌نامه موقت میان آمریکا و ایران روی چند محور اصلی می‌چرخد: توقف درگیری‌ها، بازگشایی تنگه هرمز، کاهش فشارهای نفتی و آزادسازی بخشی از دارایی‌های مسدودشده ایران. همچنین قرار است درباره پرونده هسته‌ای یک بازه ۶۰ روزه برای مذاکره باز شود.
📌
با این حال، Reuters تأکید کرده که این توافق هنوز نهایی نشده و بعضی جزئیات، از جمله رقم دارایی‌های آزادشده و شکل دقیق رفع تحریم‌ها، در گزارش‌های مختلف متفاوت آمده است.
⚠️
فعلاً باید این خبر را در حد پیش‌نویس و گزارش رسانه‌ای دید، نه توافق قطعی.
#Iran
#US
#MiddleEast
#Reuters
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6393" target="_blank">📅 12:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
احتمال بازگشت Claude Fable 5؟
بر اساس گزارش برخی رسانه‌ها، کمپانی Anthropic تیمی از کارشناسان خود را برای مذاکره با مقامات آمریکایی به واشنگتن فرستاده تا محدودیت‌های اعمال‌شده روی مدل Claude Fable 5 را کاهش دهد.
📌
گفته می‌شود این محدودیت‌ها پس از نگرانی‌های امنیتی و گزارش‌هایی درباره روش‌های Jailbreak و دور زدن مکانیزم‌های حفاظتی مدل اعمال شده‌اند. برخی منابع نیز مدعی‌اند که امکان عبور از بخشی از محدودیت‌های امنیتی Claude Fable 5، یکی از دلایل اصلی این تصمیم بوده است.
🔹
هنوز هیچ جدول زمانی رسمی برای رفع محدودیت‌ها منتشر نشده است.
🔹
در صورت توافق، احتمال دارد مدل با لایه‌های امنیتی و محدودیت‌های بیشتری دوباره در دسترس قرار بگیرد.
🔹
کمپانی Anthropic تاکنون جزئیات کاملی درباره آینده این مدل منتشر نکرده است.
⚠️
فعلاً تمام این موارد در حد گزارش‌های رسانه‌ای است و باید منتظر اطلاعیه‌های رسمی از سوی Anthropic و نهادهای آمریکایی ماند.
#Anthropic
#Claude
#AI
#LLM
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6392" target="_blank">📅 12:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A4TJx_LKKgfHazaBY4XvHrqb0hW_D8hA8CYoF5i5LIqjGLhx5T4stUGAuoJFS4Jqd2zJZx4BZoKiHkkRXu3ic6X6YIo9k4KOIwpP6zc-05cK020wzVlnWT8dXrUHCWoeLq80oPhx-DjIK68yg6TizgdbZVRx9oPnV87_pt-3j32-ic7fliavnXHpRptyKQOg0LCmEWJR8xMwSk3qYcd6sXYKkIce2sRqTzxXwvjOOmvDhIATb1igiMbFoUK431I0yFJmocEEtelRHGrTns4P5zG058wYalk7o-rqq4pzwG9MxI2tNGMBgGIPPXsML1peL-Ao_sK5x2vhgEuAL9GpoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت Ponytail هوش مصنوعی را از نوشتن کدهای طولانی نجات می‌دهد
☠
این مهارت عامل‌های هوش مصنوعی را از نوشتن کدهای طولانی و بی‌فایده نجات می‌دهد و به جای ۵۰۰ خط کد، عامل می‌تواند فقط ۵ خط بنویسد.
با Cursor، Windsurf، Cline، Copilot، Antigravity، OpenCode و Claude Code کار می‌کند.
https://github.com/DietrichGebert/ponytail
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/archivetell/6391" target="_blank">📅 11:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">زمان : تا ۱۰ شب
حجم : نامحدود
متصل روی همه اپراتور ها
✅
vless://0634f8e3-96ea-48de-87b0-3fc747894692@138.124.88.172:8443?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#%D9%86%D8%A7%D9%85%D8%AD%D8%AF%D9%88%D8%AF</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6390" target="_blank">📅 10:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دسترسی روزانه به سریع‌ترین آی‌پی‌های تمیز جهانی با قابلیت جستجو و تست زنده اتصال
▪️
@nahanproxyipbot
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6389" target="_blank">📅 05:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین: آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6388" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
آلمان
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 21/30
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/archivetell/6387" target="_blank">📅 02:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgjpwXnqQXqpUtRTpRh_EO_Ggv54-47jxcwrr1sbdZOqahMb82nH-7teM2mf_OhTkf485FlK0EJwfnZ2Z_xWFAb9S1BVtw-jkazIsBDWTdPkj5xDd_ad_6KE1jYi16IUaqntxDI2esdLnC4-B-rkl3yDofIDHFsw7gcGuWopC3kVNe5ny-9Xa5wzBLqm0zpUhjzHi_DqnrnmUJtKDPqn35CStjwHVbPfMHNSZS2OW6nPzKdu-nufwG3P6VIgIeG4sP_eN-L-XFiHYx9NXSkP623ltWEvPuBMDX__CYqXAc4OYaZiZVa3dlew0yojH20lRXixqcTeImgAe_D_nqYXCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
مدل جدید
GLM 5.2
از چین معرفی شد
توسعه‌دهندگان چینی نسخه جدید GLM 5.2 را منتشر کرده‌اند؛ مدلی که به‌گفته برخی بنچمارک‌ها عملکرد بسیار قدرتمندی در استدلال و کدنویسی دارد و توجه جامعه AI را جلب کرده است.
✨
نکات مهم:
🔹
عملکرد رقابتی در تست‌های Reasoning و Agent
🔹
هزینه API بسیار پایین‌تر نسبت به برخی مدل‌های مطرح بازار
🔹
مناسب برای کدنویسی، اتوماسیون و وظایف طولانی‌مدت
🔹
دسترسی رایگان از طریق محیط توسعه Zcode
﻿
📊
برخی گزارش‌ها نشان می‌دهند GLM 5.2 در چند بنچمارک حتی از بعضی مدل‌های پرچمدار فعلی نیز عملکرد بهتری داشته، هرچند نتایج واقعی بسته به نوع استفاده متفاوت خواهد بود.
🇨🇳
رقابت بین مدل‌های چینی و شرکت‌هایی مانند OpenAI و Anthropic هر روز جدی‌تر می‌شود و GLM 5.2 یکی از جدیدترین نمونه‌های این رقابت است.
🔗
ورود
#AI
#GLM52
#LLM
#OpenSource
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6386" target="_blank">📅 01:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6384">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">زمان : نامحدود
حجم : نامحدود
متصل روی همه اپرتور ها
✅
متوقف شد
❌
vless://7ddb01ec-279c-49e3-bda1-86155ff14046@77.73.233.129:13237?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#Test</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6384" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚀
ساخت VPN شخصی (VLESS) کاملاً رایگان و بدون نیاز به سرور (VPS)!
اگر دنبال راهی هستید که بدون پرداخت هزینه‌های سنگین برای خرید سرور مجازی (VPS)، یک کانفیگ VLESS اختصاصی با پنل مدیریت حرفه‌ای داشته باشید، پروژه
REN Gateway
دقیقاً همان چیزی است که نیاز دارید.
این اسکریپت که توسط یکی از توسعه‌دهندگان چنل(AssA7778) نوشته شده، به شما اجازه می‌دهد پنل و تونل خود را مستقیماً روی هاست‌های رایگان
Render
راه‌اندازی کنید.
📌
ویژگی‌های جذاب این پروژه:
کاملاً رایگان:
نیازی به خرید سرور یا دامنه ندارید.
پنل مدیریت حرفه‌ای:
دارای داشبورد برای مشاهده مصرف، ساخت لینک‌های VLESS متعدد و تعیین حجم مصرفی (مثلاً ۱ گیگابایت برای هر کاربر).
ضد خاموشی:
دارای سیستم Keep-alive داخلی که هر ۱۰ دقیقه پینگ می‌فرستد تا سرور رایگان شما در رندر خاموش نشود.
پشتیبانی کامل از V2rayNG و NekoBox.
رابط کاربری دو زبانه (فارسی/انگلیسی) و حالت تاریک/روشن.
🛠
آموزش سریع راه‌اندازی در ۵ دقیقه:
۱. وارد لینک گیت‌هاب پروژه (در انتهای پست) شوید و روی دکمه
Fork
کلیک کنید تا پروژه به اکانت گیت‌هاب خودتان منتقل شود.
۲. وارد سایت
Render.com
شوید و با اکانت گیت‌هاب خود لاگین کنید.
۳. از داشبورد رندر، روی
New
و سپس
Web Service
کلیک کنید و مخزنی که فورک کردید را انتخاب کنید.
۴. در صفحه تنظیمات این موارد را وارد کنید:
Region:
حتماً روی
Frankfurt (Germany)
تنظیم کنید تا پینگ بهتری بگیرید.
Build Command:
pip install -r requirements.txt
Start Command:
python main.py
۵. روی
Deploy
کلیک کنید و ۲ تا ۳ دقیقه صبر کنید تا آدرس پنل به شما داده شود (مثلاً
your-app.onrender.com
).
🔐
اطلاعات ورود به پنل:
آدرس ورود:
your-app.onrender.com/login
رمز عبور پیش‌فرض:
admin
(حتماً بعد از ورود از بخش Security تغییرش بدید).
حالا به راحتی روی گزینه Add کلیک کنید، حجم تعیین کنید و لینک VLESS اختصاصی خودتان را کپی کنید!
📥
لینک پروژه در گیت‌هاب
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/archivetell/6383" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎁
دریافت اعتبار رایگان API برای مدل‌های هوش مصنوعی
سرویس AeroLink در حال ارائه اعتبار رایگان API برای استفاده از مدل‌های مختلف از جمله Claude، GPT و سایر مدل‌هاست.
💰
اعتبار اولیه:
🔹
ثبت‌نام عادی: 35 دلار
🔹
از طریق لینک دعوت: تا 50 دلار اعتبار
⚡
محدودیت استفاده:
🔸
حداکثر 10 دلار مصرف هر 5 ساعت
🔸
حداکثر 70 دلار مصرف در هفته
📌
مراحل:
1️⃣
ثبت‌نام در سرویس
2️⃣
ورود به پنل و ساخت API Key از بخش
New API Key
3️⃣
شروع استفاده از مدل‌ها
🤖
لیست مدل‌های پشتیبانی‌شده
🌐
ثبت‌نام
⚠️
قبل از استفاده، شرایط سرویس و تاریخ انقضای اعتبار را بررسی کنید.
#API
#Claude
#GPT
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6382" target="_blank">📅 21:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">https://ez-d0de9f.gmailam.workers.dev/feed/archivetell
اختصاصی ۵۰۰ گیگ ۹۰ روزه
لینک سابو کپی کنین بزنین تو کلاینتتون
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6381" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRtiuQzOWbgr-BQRVq1XjPeliTlJWMX3Wo_6cc4xTDTBCY1BD9nxZCfCQeMAFN8x5cIhKJLm-pn6DO2-hrp2JUPYEj3_QQIn6GSiwIvG-qPyAu8yE-ORVZDv-7Jyu5Pm1T-7JFBNlo8zFPxg7ie3c1-cIHiZbh9UlkxIr0_E1dYxe87q_jQPZTPLScAY0TuKPP4cN3gzR91d17B2wAPXTs12h7D4BtMUQb2zEniqBzNrxz2oWqkj5zz2dJ5BlINp2vwnB2wsAJnFCZjBsAuB0eDR_led0KMp-zZCU_jpBFfm7u63iLYmrgSaifzS53ICNY-SRUIih8bin410aHEHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
OpenRouter قابلیت جدید
Model Fusion
را معرفی کرد
حالا به‌جای تکیه بر یک مدل، چند مدل هوش مصنوعی به‌صورت همزمان روی یک درخواست کار می‌کنند و در نهایت بهترین بخش‌های پاسخ آن‌ها با هم ترکیب می‌شود.
🤖
برای مثال می‌توان GPT-5.5 و Claude Opus را به‌صورت موازی روی یک سؤال اجرا کرد و یک پاسخ نهایی و بهینه دریافت کرد.
✨
نتیجه؟
🔹
پاسخ‌های دقیق‌تر
🔹
تحلیل‌های عمیق‌تر
🔹
عملکرد بهتر در برنامه‌نویسی و مسائل پیچیده
در واقع Model Fusion شبیه یک «اتاق فکر از چند هوش مصنوعی» است که روی یک مسئله همکاری می‌کنند.
🔗
قابل آزمایش در OpenRouter
#AI
#OpenRouter
#LLM
#GPT
#Claude
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/archivetell/6380" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
100GB
🧭
شرط: حداقل 1 دعوت
👥
دریافت‌کنندگان: 43/64
💾
حجم: مخزن
⏰
اعتبار: مخزن
🟢
فعال - در حال توزیع</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6379" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">زمان : نامحدود
حجم : 50 گیگ
متصل روی همه اپرتور ها
✅
vless://11cd9b14-7128-4887-acac-2ab549d26664@77.73.233.129:46024?type=ws&encryption=none&path=%2Ftest&host=play.google.com&security=none#50%DA%AF%DB%8C%DA%AF</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6378" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAUzjrF6O2tned5SGMHvmjP2av3NHgi8sWUaXX3Qt2ALBJOt1KbwyH71d92mXXJFIwhKsYIvD2IyjyyhX8ZD6GgqV8EkahFAavUogmECObOAEg0iZhnE7SHwFtKOBVRMQQiXq4JJivlcfIonBaH8JvNogGDNo1vIzIVi0XMlsXXPdFl_f35RXNW0oG9UdnXrxsp9DXGK_6kw8yNMcIQzzjltkiEkYGnJRt9f2MlNA2UrU9uuo7LSeXkItdyo7IOq3QE1b-gZKrj7OSh-Js7WkxyWBz9YQK9lQukban-fCsWvOlrCl8MHxfp6W0OG5ig2Cj2PVgNiMKgSRpwSA6Tqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ملانیا امشب، سر باز کردن کادوهای ترامپ:
_ مستر قالیباف: 400 کیلوگرم اورانیوم.
+ روبیو، ونس و ویتکاف(با ریتم) : چرا زحمت کشیدین ؟ ...
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6376" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتیجه نهایی
🔥</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6374" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA4DL9cYq7t3TN0bnYctpb8dL6ZOWA5HPNH8J-Y4Uv-XXTveCp5Ju9a1uLRm0iKNXyDemzynOE_C4dgRyYwi_5CscM7F7OHUQXRUuZsMyCl_o2D6ZdU8M5PFSlHR2Qv2JtqyRCnYvT0w2YIVz3CX4dkCZcR3XuIZVNz1CbPZAKMqxBoO7bg4Uj1pp4SbsB84_tT-QYpV4bQSDFLrmN1l4w3xR8Q6ehh7CkC9qJvl4qMEq6PdOAiwimjoNMT_-lY14agTkYC5_f3z228eWgq1TOwGnQ6pLKOz6cAGewYcytfbP6c8R4jAV81473fRJMRvJ8qlyvgnuCk5CW77QnUMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6373" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6372" target="_blank">📅 14:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه…</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6370" target="_blank">📅 14:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6369">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
چالش Human vs. AI
🤖
فکر می‌کنی قلم و احساس تو در ترجمه از هوش مصنوعی بهتره؟ وقتشه ثابتش کنی!
😎
متن زیر (که یکی از معروف‌ترین شروع‌های تاریخ ادبیاته) رو در نظر بگیرید. می‌خوایم ببینیم کی می‌تونه روان‌ترین، دقیق‌ترین و ادبی‌ترین ترجمه فارسی رو براش بنویسه که هوش مصنوعی هم جلوش کم بیاره!
📖
متن چالش:
"Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people’s hats off—then, I account it high time to get to sea as soon as I can."
🎁
جایزه ویژه:
۱۰۰ گیگ کانفیگ اختصاصی با آی‌پی ثابت آمریکا
🇺🇸
برای کسی که ترجمه‌اش یک سر و گردن از ترجمه ماشینی (AI) بالاتر باشه!
*(نکته: اگر تعداد ترجمه‌های شاهکار و برنده‌ها زیاد باشه، جایزه رو به قید قرعه به یکی از بهترین‌ها تقدیم می‌کنیم).*
⏳
مهلت ارسال:
فقط تا ساعت
۲:۴۰
فرصت دارید.
👇
نحوه شرکت:
معطل نکنید و ترجمه‌هاتون رو همین الان
زیر همین پست کامنت کنید.
ببینیم چه می‌کنید!
🔥
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/archivetell/6369" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6368">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWjoZyFEnjrQwLq7HGuvfXeRTrHtyZ5pyIopwTIV5kBVxg423Mj1cvMrbzczNWlnVqwwrxsk1VtOansq66mg29578Dm2Vry5lR0MScW7_fzfCBksgCwUxuHh46EjF5AS0pncE8QQ4qSQgQ99GXCs3g9YX5QTyhcLVzn-Oub5rxQNHP5TpHeDRJFBaz64fLl6Erq5ueQThC53KSpPLr7j-FkYkyB5j0dkkzKAAJSr9klBnazhyYHddIipldOmpcv5_MHPQmHiOdLo-spMpOuq9A26Z9Lkn5pB-hk3By-67xmx6Z7drxJbHY087nMAyv2u-S8p-WkXtM5-e5Iv-F7otw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن» یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/archivetell/6368" target="_blank">📅 11:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6367">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQmGXwN0i0VCKNkl1pczI3irL5uo3SV-2ic35qlIiOblWXx-cpYQhvQfxCVGgTD0tWtENrdxTJ2sBYucrOu_tuNrk6pgsq42vAGNJddXmsZRimHX-acIw4hmAemSR4OVI6SdtjUUicvEBF0MxjcpE3LdpnvOduCQ5kG3DC_Hc8AsYaNWJVv9wA9KqTUs95Ylm-ioDcR5gUwEwvPwatxnRQNz8t1PxA7LqSI_HuhLImIA6QLzUR21JullDXaJiB_Vs7sQzHZQIc_mH6oNpK3LHqUhKzoqjW9tfI5zTRlzUjIxF4DTmfjuEhB-2yW4hY2xnr7OIBEgb6HAg6dueb0xmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر چیزی را به‌طور تمیز حذف کنید
✨
فقط نگویید «این را حذف کن»
یک پرامپت بهتر به هوش مصنوعی می‌گوید چه چیزی را حذف کند و پس‌زمینه بعد از آن چگونه باید به نظر برسد
🪄
Remove [what you want removed] from the image. Fill the empty area naturally so it looks like it was never there. Match the background, lighting, shadows, and colors. Keep everything else the same.
#Chatgpt
#Gemini
#PromptEngineering
#PhotoEditing
#AITools
#Design
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6367" target="_blank">📅 11:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZyNr97IzbughO4LuJ9Q9T9n3H6qXrTPlHYMunZMxZtzLO837q7g3JmFxsrrLzLQ8NSIxvYmajYAhKQfW_w718IvSvJ4zxTF4786FTHkSWVAfDM0j2bnAoPiEuuQtHOAdzhiNgdswI5ybkLDnWICUrBg5WgK2a56SYJY3RSWu3-UDA99B9_IqqpiaOEW8je0IE5QFO8EewTuV399apldAfrAKfgpmErNcoo0f_cINZ-QGX4F8gnmu230rJhdb1ByPocr4dsq8m3Th1uROJ9E_S0YGOKbKTSDu87fzEDylCBMxwTNO9OunpbWhkBqZz7weQOt4V-Bee9CFoq8WDaPEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت تصویر با FLUX.1‑Dev، بدون ثبت‌نام و نامحدود
🎨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6366" target="_blank">📅 09:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viGFMofjQfkkt97hO6emI9g55XqgHn358aCvkWMKVUBSvLgjHgoU9HuJBiiSgpGjs1KKUS5BQv1YbdNcuWm5IKur3P7OjiTnDFjIfoOeqpq3Aq5Bd_4aYGUqLP4R1851m3YcUYc14WJBHCzWuo5IDJt1WMuTvwsjYRjZcaGvIDZ5Y0OZSci7praiWwZ1eiZif_BX5M2NykUitGYGD_XWZzIrUUMFC9UP_H4zwfIfSSbapjHOvNzTQ7SHS0DK_obMpiDM5dVpnrGhSWAwa-TkAMweZWoiRDM8NlepkQ9g-xdXaSy7QkZ7keb-6tKqGesFiPiJIM-2cWXXaIRI-b59mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
روزانه 6 گیگ کانفیگ رایگان
🟠
پنل BPB کلودفلر
🔹
با جیمیل لاگین کنید
https://dash.cloudflare.com
💻
در ویندوز نرم افزار BPB Wizard رو دانلود و باز کنید
https://github.com/bia-pain-bache/BPB-Wizard/releases/latest/download/BPB-Wizard-windows-amd64.zip
🔹
عدد 1 رو تایپ کنید و اینتر بزنید (اجازه لاگین در کلود بهش بدید)
🔸
لاگین که شد بیاید تو پنجره برنامه گزینه 1 رو بزنید و ورکر بسازید
🔹
تمام سوالات رو بدون تغییر اینتر بزنید و آخرش y رو تایپ کنید
🔸
پنل که باز شد رمز دلخواه ثبت کنید و لاگین کنید
🔺
تنظیمات پنل
Common
:
ipv6 رو خاموش کنید
VLESS - Trojan:
- در بخش
⚙️
Protocols تیک گزینه Trojan رو حذف کنید
- در بخش
🔓
non-TLS Ports تیک عدد 80 رو بزنید
✅
بیاید پایین و گزینه Apply رو بزنید
🌐
دریافت کانفیگ ها در بخش Subscriptions :
- گزینه Raw (without settings) رو بزنید و دکمه کپی رو بزنید
- لینک ساب رو در v2ray وارد کنید (میتونید لینک رو باز کنید در مرورگر و کانفیگ هارو کپی کنید)
🔵
@ArchiveTell
|
#Mz</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6365" target="_blank">📅 05:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4Y_xM2btHcL8oA06SzfCiRQtWSiFlriIPFr8D_8LiZ_s2pyI92ZB6ePvqm10oBKELO4dO5Wl--1ge6ORZJuslFktVayvxfF4MvvxmWf-j47C0n_y7HRwUSlaG6diRSsmjlCU2LpX_gVv5Gj8CSJGzVw-BUJnQYPm-7ffiYR7c6G0fzgkwPLbw0r359DzjxfJ3TAr7Zn46oPPaf00JK4JAJTrpZqWHVHRJvADSXb8EXssk0Vwje27wuFcopdSH2rJG7WXwak5J7sly81GUAItlAXrSrK-rf8Ipkef7PoTX__KD9HDoyeYtzyH0_5TiEX9Rx3qP2nLetEJjQY5cwe2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😬
کاربران Gemini از محدودیت‌های جدید گوگل شاکی‌اند!
ظاهراً گوگل بی‌سروصدا سیستم سهمیه Gemini رو تغییر داده و حالا حتی بعضی درخواست‌های متنی ساده هم بخش بزرگی از سهمیه روزانه رو مصرف می‌کنن.
😶
🎥
بعضی کاربران می‌گن ساخت یک ویدئو می‌تونه کل سهمیه روز رو با یک پرامپت تموم کنه!
👀
«جاش وودوارد» مدیر محصول Gemini بعد از موج انتقادها گفته تیمش در حال بررسی ماجراست و احتمالاً تغییراتی اعمال می‌شه.
📌
اگر این چند روز حس کردید سهمیه Gemini زودتر از همیشه تموم می‌شه، احتمالاً تنها نیستید!
#Gemini
#Google
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6364" target="_blank">📅 03:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6362">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=OwctFIfmp7cxNy6e_SS4Ks7Lz_rnTAMPappjJJXVlQ4rWNQKf0fNbsEjIq_s9fm9aBuyKvp436h8KioAcQcrGtgxQdwkf1mLA1gCbYO9Yf8VE07QTB-oco7dSS2FfIzDPg06ORhZkJhFWxxE80wRk_uSpDfITWdcBflJ2yHM4TRP2b7QdHsMR7y7FkckCuHfIkp9wY9hPESe7DSqBHVDKW5uvKdKpt_6l9uqSdjFapWjNoaj-orv0U_UJBR_B2uK0Rwpa1u0sYKZo4HMN0S3SF0Q1Q8lpnIWoui4tE1DKsILY9sZmJWO6-H0cnQI9v6_fUoKUQki55E0nqkz7buEaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e67893cc6.mp4?token=OwctFIfmp7cxNy6e_SS4Ks7Lz_rnTAMPappjJJXVlQ4rWNQKf0fNbsEjIq_s9fm9aBuyKvp436h8KioAcQcrGtgxQdwkf1mLA1gCbYO9Yf8VE07QTB-oco7dSS2FfIzDPg06ORhZkJhFWxxE80wRk_uSpDfITWdcBflJ2yHM4TRP2b7QdHsMR7y7FkckCuHfIkp9wY9hPESe7DSqBHVDKW5uvKdKpt_6l9uqSdjFapWjNoaj-orv0U_UJBR_B2uK0Rwpa1u0sYKZo4HMN0S3SF0Q1Q8lpnIWoui4tE1DKsILY9sZmJWO6-H0cnQI9v6_fUoKUQki55E0nqkz7buEaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">WhatLetterAI
تصویر را به متن تبدیل می‌کند و به هر زبانی که بخواهید پاسخ می‌دهد!
📸
🤖
✨
قابلیت‌ها:
•
🔹
تشخیص متن از بیش از ۱۰۰ زبان
•
⚡
استخراج متن از تصویر و پاسخ‌گویی هوشمند به سؤالات محتوا
•
🛠️
دریافت خروجی به زبان فارسی یا زبانی که انتخاب کنید
•
📦
پلن رایگان با محدودیت ماهانه برای ترجمه و پردازش متن
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/archivetell/6362" target="_blank">📅 20:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCksRyp8GlgcpUwM_ke9fjUUBJEtQpNH35Q1O2uf7WZDGY6IWGaPaERT0_ZUFZFA1yajDuhfg-6W0NFXefzPXq7DFmg-c_3Ci1BHj7W-Swd9UUwlkYYqhpIBAjY18qow3ZrgHtuWjQTnzorRC6ZMMGwDLGOt6f6IdjU6mnvmGk7NKnokut1b_okGnGg8Pm4MEqt9J4IP72QSIyxL78WRA0UQPPeGftoQN22fkHHhU5m_ukDyd1VOO8eU3homfRZZ8rUesisJgq2c49AMddrmMnDVx0Mz6yY5HAfufmVfQJjfkFb26Vrr_3tpB1LbqgJPBPu8AoB1niXfEtAG5K-ofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تولید رایگان تصویر هوش مصنوعی
🔹
بدون نیاز به ورود
🔹
خروجی سریع و بدون واترمارک
✨
🔗
لینک
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6360" target="_blank">📅 19:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6358">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaawfQ1reGTmsUMgAS83sAmUOzEeESqJJ1XEcrSOtJjTyHaNlevwoxuUR-1C7X91X9e6dfq50zzhl-QzNs31ROiDOlpa-ftX-M6VyOfjstdiOIcndm94aSlZ_QOpOfbb59sDkugDt1EBZAklRitilfjfhFiUM7Ds5Bdj404Wr-b-SWJ6ATk9ltMTbpcuWjctpPw83o-90WHkn8bv-QEZLvZYTanLL7G6annKw49QaLbHGMnalsv9Sb0hzHVzFhMuXrQwI-RZKHEBQBfAb-W3BmRxAf3h33aySlZfw3uA2eaIyspB2buTdmA9-odKPZXqOF4nJWohMcnoNAs1pAotFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=nh64XlAnxa03Eeo8puyUoYHkKSUYQ8gCfZwy6IUMb9mQk9Bszt96kV9_xR0_KBBM-d2CxbVUx7Re9LN7qGkEjwGmLFRkkosm4MaHvVwujCse7fGX4_tvgxRSmPewGzKuR6YpGECJvKtRBBs5YBJCrot77JA5ZxY7BIW_B4Flv6N1pXc7hW_jZiOHaG3S6H0hYocC2fiKrNU7CVKMbAwt3P0cweOtPZaQlEVsf6o1RF4F9gF1NFWvHR-8TMTkWppJjrfh_8DCZ2rOmKnvWTOwpeIjfuqZe3f2erfh80Apiv48ALX0c6oA3udhFMKC-fM5PHkTYgGrtrZRmAuZlnNZGxg4Y__F69NyA94ZrqlZ1X4otfkc2oKFCNiOBTPwgG_HIxT5wPtP_5S2Rm4sEmxvESqIceinH2f9MrHYP6hRq8yN59NMJ6Z4QbdYpg7CWjTrfgQky72xncUDs6c81MIEUi--ghqxdEan0yT8Lj7kYOVIUcvxRL9Q_TzDdKlw6Lm3xMsKMY0g6itcZtKmHOeiIMXZiM_E9OLecHshJbFSf-xJ8HXAZN1EHNslVO8QgYusUCyyp4HfYYcUNJKhCHBPuBpnAakJ4htgVKmAAHb183hvRreCZ8SLoVGs5uwUhe1ieVW449AbSqAOFQJqfXXEUNi2S8zwliPPCYT-RVAsmUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7dbd572b.mp4?token=nh64XlAnxa03Eeo8puyUoYHkKSUYQ8gCfZwy6IUMb9mQk9Bszt96kV9_xR0_KBBM-d2CxbVUx7Re9LN7qGkEjwGmLFRkkosm4MaHvVwujCse7fGX4_tvgxRSmPewGzKuR6YpGECJvKtRBBs5YBJCrot77JA5ZxY7BIW_B4Flv6N1pXc7hW_jZiOHaG3S6H0hYocC2fiKrNU7CVKMbAwt3P0cweOtPZaQlEVsf6o1RF4F9gF1NFWvHR-8TMTkWppJjrfh_8DCZ2rOmKnvWTOwpeIjfuqZe3f2erfh80Apiv48ALX0c6oA3udhFMKC-fM5PHkTYgGrtrZRmAuZlnNZGxg4Y__F69NyA94ZrqlZ1X4otfkc2oKFCNiOBTPwgG_HIxT5wPtP_5S2Rm4sEmxvESqIceinH2f9MrHYP6hRq8yN59NMJ6Z4QbdYpg7CWjTrfgQky72xncUDs6c81MIEUi--ghqxdEan0yT8Lj7kYOVIUcvxRL9Q_TzDdKlw6Lm3xMsKMY0g6itcZtKmHOeiIMXZiM_E9OLecHshJbFSf-xJ8HXAZN1EHNslVO8QgYusUCyyp4HfYYcUNJKhCHBPuBpnAakJ4htgVKmAAHb183hvRreCZ8SLoVGs5uwUhe1ieVW449AbSqAOFQJqfXXEUNi2S8zwliPPCYT-RVAsmUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎵
LoFi‑Engine
ساخت رایگان موسیقی LoFi برای خلق فضای کاری دلپذیر!
✨
قابلیت‌ها:
•
🔹
تولید محلی قطعات منحصر به‌فرد LoFi
•
⚡️
صداهای طبیعت (باران، باد، دریا، پرندگان)
•
🛠
تنظیم تصویر و طراحی فضای کاری به دلخواه
•
⌨️
پشتیبانی از کلیدهای میانبر برای کنترل سریع
•
📦
کارکرد آفلاین، بدون نیاز به فضای ابری یا اشتراک
•
💻
اوپن سورس، سازگار با ویندوز، لینوکس و macOS
🔗
لینک
#OpenSource
#AI
#Music
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6358" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پخش زنده لیگ ملت های والیبال (مردان و زنان) بدون سانسور
🏆
https://www.persianagroup.tv/live.html?ch=sport3
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6357" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59055631c.mp4?token=e83Ozolk2T7s0XQd9GzPQ-bKYj4xGropAFyXi3gYwZJRUsjXayHn0f2JbcMPacsErSx_cGARG6oYOuBp6jk-mzLUddRbcBoBpB7lKklbS3ab_DoV_PgGNhOtSPcPYLrMndrSI1mTi0WtKisqAa3Eq2V1g2FR590ZJvd5PLwuaLjbhKyJSRnTzxtgY67N5-M1hG1G0ZPdbUfDUPTqQ8GdhXUk0h7WxNndPIqoZpf48xdTeG8zcylJ_lVCysyBq80mCjOm9Hi0eHMY0e68QsGJjQyOErMLO-jAtXJ1Xsa6AxoU8qcT-AT3p1NAtfe1Y5XA0arvU8gtH1a_VBf4eVvVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59055631c.mp4?token=e83Ozolk2T7s0XQd9GzPQ-bKYj4xGropAFyXi3gYwZJRUsjXayHn0f2JbcMPacsErSx_cGARG6oYOuBp6jk-mzLUddRbcBoBpB7lKklbS3ab_DoV_PgGNhOtSPcPYLrMndrSI1mTi0WtKisqAa3Eq2V1g2FR590ZJvd5PLwuaLjbhKyJSRnTzxtgY67N5-M1hG1G0ZPdbUfDUPTqQ8GdhXUk0h7WxNndPIqoZpf48xdTeG8zcylJ_lVCysyBq80mCjOm9Hi0eHMY0e68QsGJjQyOErMLO-jAtXJ1Xsa6AxoU8qcT-AT3p1NAtfe1Y5XA0arvU8gtH1a_VBf4eVvVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Runway
با چند کلیک، عکس ثابت را به انیمیشن تبدیل می‌کند، رایگان!
🎞️
✨
قابلیت‌ها:
•
🔹
پشتیبانی از تمام فرمت‌های رایج تصویر (JPG, PNG, TIFF…)
•
⚡
افزودن جزئیات گمشده توسط هوش مصنوعی
•
🛠️
تنظیم سرعت و طول ویدیو به‌صورت دلخواه
•
📦
خروجی MP4/WEBM با کیفیت بالا، آماده انتشار در شبکه‌های اجتماعی
🔗
لینک:
https://runwayml.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6356" target="_blank">📅 16:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/archivetell/6355" target="_blank">📅 14:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">uk-new_domains.txt</div>
  <div class="tg-doc-extra">21.8 MB</div>
</div>
<a href="https://t.me/archivetell/6351" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیپی کلودفلر
آمریکا انگلیس آلمان
با این آموزش اسکن کنید
https://t.me/archivetell/5657</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/archivetell/6351" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">با توجه به رنجی که اسکن می کنید هر کدوم ای پی یه کشور رو بهتون میده مثلا این ای پی رو اگه بزارید فرانسه هست:
141.193.213.10
یا این آلمان:
173.245.58.55</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/archivetell/6350" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Cloudflare Germany
🇩🇪
103.21.244.0/22
103.22.200.0/22
103.31.4.0/22
104.16.0.0/13
104.24.0.0/14
108.162.192.0/18
131.0.72.0/22
141.101.64.0/18
162.158.0.0/15
172.64.0.0/13
173.245.48.0/20
188.114.96.0/20
190.93.240.0/20
197.234.240.0/22
198.41.128.0/17</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/archivetell/6349" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">Cloudflare ranges
74.115.51.0/24
23.227.38.0/23
185.158.133.0/24
216.198.54.0/24
212.104.128.0/24
216.24.57.0/24
66.235.200.0/24
198.202.211.0/24
103.133.1.0/24
199.60.103.0/24
63.141.128.0/24
137.66.28.0/24
137.66.28.116
185.133.35.0/24
208.103.161.0/24
185.148.106.0/24
209.94.90.0/24
160.153.0.0/24
199.34.228.0/24
160.153.0.0/24
198.41.223.0/24</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/archivetell/6348" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvr6tKtXmcWb-YdgpKrH3w3E7DoUDbCDYCh8eoE_NP0es7hcE0AeMprzEvk746DyTpgyCenO9AUlr2HdWBtozh0EaIlmF9Xnnzv0Z6vNkgtNxBcNeHEF3HsVnqQcj9jqjI_YDz-lZCsZ2THltbhbhRYOLS6Es1zZCJSEv27OXy4MJFxsaFJAh9VDOmIUywMk4JkF7RwGDGPtJZQw2xgPTwfdqUgJRA5cWquiTVUSANffqX00A8ItWiYkFaUdqr-hXjqXKMgRFG2RdFuidl9WcOPrWZhYg2qroEZ6K2OSHVfNIg-ZIfIhfKhPlnrVKEVNuCj2DSqDB5Y5eOv2OczEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکن ای پی کلودفلر 2
نتایج این اسکنر معتبر نیست یعنی ممکنه پیدا کنه بزارید تو کانفیگ بازم کار نکنه
بدون vpn وارد این سایت بشین اگه باز نمیشه واستون از یه
اسکنر دیگه
استفاده کنید
https://cdn-scanner-pro.vercel.app/
لیست رنج کلودفلر که پایین میدم اد کنید و اسکن کنید.
هر کدوم که سبز شد بزارید تو کانفیگای کلودفلر
با پورت 443 تست کنید</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/archivetell/6347" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSd9qJRDhQsFpSjK_2t0k7j8RweHoov-7jKEL9znq1iIL3Vc6ejaaQHbNQwz5PdZjA5epNKkHjvUO8gad7b2qrxfxj0fDd3xJey3c4v--3FENjzj1zHKPy1ONNlZkDfpGuqMYcvLXZKSKK77P76JVgnCteqyST2oYbssXTNRsOWkP2cX7EXJmoIz0gyxQ4RjgUX5tv-8X8GMrXXB8mhmyzNjAHraRUX5EIkoSXgXJFIzSDyPovYqUkzuXaYXAaqv7X8DJDVu9megFvHByZbP_gsnDJOyT5583wksDzoiYQOEm8q5L40F_mQNw-VsXkX0eyN10gZN7j37hgnqySGJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم کانفیگایی که میده</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/archivetell/6346" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJlOdnqwQ_Z4LfmmbBRuKuURMPTk1ql2mlJoPk5vn31edP2eymgb68-mpCtBYxDOIMPjcI2Q8vDrAZNV3cOHoeLGY6FTc-UUQzaGI34vADyacHFbobeZ94yziL8XQk9-HQKA2oSe3wHn1LeW-aSr-asM_VAyJiCTUIHvbgGmY9oOVAumpHG95vZ7rpWRWzIIblnbsXPzJnmtfbUJHca8V765rCAKmgifqmNOFLXZibeGljXomWIwPVA72ycRZkm2c30CbbgNLBN1MJ53XE45qQWlzRsDoKuPyvhVNAkFpcqoUrvuS5uYMAd7elUwY79wO9o6Pyx3X8Cwg255X3j0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyqNUeoeM30GTrDWdZaRaUloVeFXB2XvPBzOm6J0FGKRpeqp9Vq1WkvXiYG1oHnZ4PfM_RFVN3A0ltwsYC9koncEWPWCHxuwnsyqXoFhyLhoWqoiOrzojBwyXN8xUD5D5V-l1ggL8z66oEEGhDZFkp1PFNE_Cgm7lMzjyekph0az123E0xOM83SIkg4SEr6BXo8uv6p_4BVMCcW2bODt_HQyEk1Cnt6E-20ExS0C4YxrKh10jhMiWnpYfWsuwktyzD7BDpistNJpgM1C7a3DyvyrE_gwfLduNAyJw0WHNOJVnlBZzDXBPFMGAHBM1MdFB8Ow__S5tOcMv3A6F4SseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8F13BG5f7qIWiiERmkcRqrxm37IIq88jbit7UHU1pH60kDdQfVdADUQSf0XyDGWO60ZTm0u0bk0PGGBiZvc3o6v43YcICGWlkjry5Op9YG1ajF-YS9oUKsNdQ8ucdPzY7pw0Z6zmZ6-XGhZFMYUqtwV_YHUYNPqn7dH3kR7mQejWj3PM8bTUhmpS_XjHKLQn5QECVT43obwsWEHYmSan4yuAaRmiokP4spmnGmGmxb7scbHxvb5IPGFivIYXEgXqDUa1lF6p7GxD4_CBhPevLdnvqIk2Yv1HsoVo4eE7ya7_X6Tis2ZE88rYGVAdT_F7lbrgUKMvvagajP4etz02g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">7. به صفحه اصلی ورکری که ساختید برگردید و بزنید روی پیجی که ساختین تا باز بشه
این صفحه nginx که اومد یعنی اوکیه اگه ارور 1101 گرفتین یعنی اکانتتون بن شده باید یه اکانت جدید کلودفلیر بسازید
به اخر نوار ادرس یه admin اضافه کنید تا پنل باز بشه و پسورد رو وارد کنید و لینک سابی که میده رو کپی کنید و داخل ویتوری وارد کنید.
کانفیگایی که میده اگه پینگ نداد نیاز به ای پی تمیز کلود فلیر دارید.
مثلا این رو با پورت 443 وارد یکی از کانفیگا بکنید تا وصل بشه
188.114.97.6</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/archivetell/6343" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8iKi-ImsBRzIUlbG8BktCRdhLQoIQtGLG2D-X08sTWikt-IwebLiOmVzs3vezjtZWnQK1XnKQCbZ3pO-xiGdo4mc1tl3KyKRyl0d7XKZiXHuDD1iSzepLoGj82b7UdUJD6u_WGswVIsC6Y1URmuGcCkW4rHTB4y7F-0r4ClqAt3vf_q7VFEJlRF82yDk40-RxJHFl-8optU_byh-S3rBJUWlNUJ1s4Dz5ZXD4fSIDKXBB0yGb2ovJmlECsftAfNEktEgk2aVojwTLGaWgIyest-tT8sr1-XZvMPwGMSWiICxyWjfO_TYxFo93RyH_m0Eksd_KH7JJsl0VVyhawMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6. بعد پوشه رو بکشید تو این صفحه و بزنید deploy site
تمام</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/archivetell/6342" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cT1ZdqLfQoRsTs6RDZntj6Dqea4RXwDjsGGk0EmlOl5sWFFP8YlZKlLaaLQqcg5U05bL5WbdxqCF7eMkg7tpWSqb7wOgWbKre4-qfdnEoxgbEAAyHltb5JnxQDQaj6pNkg33LjOgS-Ie-s9WdjBFW6tn9lZI-KhK4OtGA0fe0944CY2FYweFt8vr3WaFLMfudv5sFtkay9475_faFz6v1MbhhvXyPJ4DugoBCNanwo2lhmIDss1eW-SZ5rqXSB7_BXcV7uyFMoCU4wqlzzjgSnkuirSifMB6PN3muKOP5_JX7g9Jhm2lajyf5b6S54TZtOhL8rdFapcNlaRZLhtmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5. از بالای صحفه بزنید روی create deployment
حالا می گه پروژه رو اینجا درگ کنید
برید به این صفحه و فایل زیپ رو دانلود و اکسترکت کنید و اسم پوشه رو ۱۰۰ ٪ تغییر بدین به اسم غیر vpn
https://github.com/cmliu/edgetunnel</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/archivetell/6341" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab1gGuT5IqqJmhg4bLq3ogRYuQ_s5o6UzeGkZOgBw-r82Chom8vjNkoy4gjo3dpkRFLulF5TVHlhx-HCoAKMgDHWPdDqHnU9-hP4iStj2H86YifHNabFWvZfsMgt3HygxFHkoo_JygBFfgCBTlC8-XqWPiR9v6d35cQ7-43rUKmM7plbUiibNnFnxIOoYQKqzQhJtWUlUlfNUQ3JZ9rrR82oaForOfbnkkolQdDSVer-cp2nZCxG_72B_vlbg9DI71dTSs_085LXCHNbKiKD0oENdNoeXi96BQv0F_1frnZeRFvoo3WZaZr8fMl76qLZ0n_pr7Ps9iooFIXeCEUmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4. بزنید روی bindings و بعد اد بزنید و از منو kv namespace رو انتخاب کنید و مقدار زیر رو وارد کنید:(حروف بزرگ)
variable name:
KV
KV namespace:
همون kv که مرحله قبل ساختین و سیو رو بزنید
از بالای صفحه بزنید روی دکمه آبی رنگ create deployment</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/archivetell/6340" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou1s0ihk0zj4BIzzL-Zf3LTvG9MXDhzTw-H3Afr0Q0CsbU3d7L_rJiS1VEydEi0soWQybkgRqxoiuNgfjDcXKsv3jLjQM7vSkyoFz_aGFiLXfshh0_TBA_k773uEYQVPr7guJmcFaSaysIq1QY1Dz3nLdU-M4X-oKzRz2JtvD5q20MlriK3CjjOXgDSpGtmkI9lzU4XnBYDSH9q9dV6WPwKXcLENre6qsgOOLdRPHyJpBzNP1SKUN7XqmWU1ejIWUvVnwA2IUucUq4FbRexk8t8A9QU7IcLCYgiHyfuwKKNdt7akhJNO6Kt6RyU4DP1Bd2lYGwsyU1bB5Eo1Mj8h2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">3. برگردید به worker & pages و پروژه ای رو که ساختید انتخاب کنید و به قسمت setting پروزه برید
قسمت variable and secrets اد بزنید و این مقدار رو وارد کنید:(حروف بزرگ)
variable name:
ADMIN
Value:
یک پسورد دلخواه عددی مثلا 123456</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/archivetell/6339" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRVbvtXrp3zxMPpx8yLUSERwJwZb6ifU7pMpOooongwcMwkg8KuaUB2YQbj3fDl0n5QdwwQI5TF4vQHlE3lo8W-5W7mnh6IHC5Hwj6ujMThriwQfiAZom9b4PHz-PzoIH1ALu5tRGK5TlmDefaT01SDBuSLaDvo6E4XdC75YVhf9R8A9W9bSelF258RiHgzR0kqCQa4PccHPjvCs4j41me9PW688u4jJu_yaiOwD-KBp0PUCrRchjmJEfR3LQ-HJSwSO5iH-7RCqv_cMcDNzkBBDof6pq-7G8hAR-AUPflG4FTJBzdztUYQd4AkxKW_ntFJTT9PUUKHhF3iYBWJmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">2. به این مسیر برید:
Storage & database - workers KV - create instance -
یک اسم انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/archivetell/6338" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtwPS4250T9eEb4gXQgt2WTtFcJDSieS_ZDpy2c-hOQSmyZD8x6wdtyBbwr0uiVPLLCugC7ca53GzKPQK5Wc2yuiukwoGH6ena9Srh0s6JwaIAFYsAEvJK7v09TVrBs2zdSho9CMMeIMjGodKi_5tUpur5fz3slYxv-w08xHAQ6b9JAZowTH6FEs4xcN_EujwH1GJA_Vgg3lZoyVrxUoZJiH3e3K8yK7z2kbEHtQKO-8CwdHCDye7yqPAGxy5Cvp9nOPFifCNPe-b22NaSf8AxZwKQN2W5MQnf9-N486YTzB95QdrZQ8Z3syzLoiF_2CCJvCAm-FJUqFB2vZ8lI_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1. ساخت پنل edge tunnel v2ray vpn
به داشبود کلودفلر برید:
https://dash.cloudflare.com
به این مسبر برید و یک پیج بسازید:
worker & pages - create application - get started - Drag and drop your files - get started
یک نام انتخاب کنید که هیچ ربطی به vpn نداشته باشد و بزنید روی create project</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/archivetell/6337" target="_blank">📅 13:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6336">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQBxabkXJtdf05zp14FVhuZ3nEPGSUM0U8DUmRVv_z603_vf3Z-4YPjEViy0cng21Qtg-bs3D3_rmLI_azw52CQY-Am5_HjwCqc0tA76eYCExq-3cmo8fOoopyDpG70SOQvhQbDeANuDxxgatioYvZeBUre-hZE2itFTTsQxdDatHkgqc4L2AG3ZFWhcKuVJVm0WGHwcBxJn866OwP6sN8jXMTl02DBJ0WjCXPCnVg0YrqSP_9uSH3v59umtQrmpsTqe1gN3Ar1ilGa5E5lu_MHYCC2UnXzZMhleO8pcizJK5-XqOndfKFmDVkRTdi2pNFMAOXYNND07V2uhIN9ERA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای من اگه خواستین ثبت نام کنید  https://ai.prox.us.ci/sign-up?aff=iYva</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/archivetell/6336" target="_blank">📅 12:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=MyrHL7sttp1Fms7qUsJsONsiV68k8MfyPZX47apVMm4IJAyx6rpCyg3IL8XAJUeKyll9LNGk9aY6M-jwUUMGvg-bIePWUJoXbHf2XbGy9CvAd7xOt-f_wWI-MNsA1LW4QLTSN21_dQb5yq8iq39Y0H-iMF_ksecQhJ4e1gC93y0n-Zz8r0uJ0JPwlQFnzQ0gYi01VI0vI-kkENHCN7co_EQp-Xbur4_o6MdRjozZg4j5Ky9nxTxS6YR6P3besfNIW8P7pbRCauqz9wv3iNNO5Bz6TEXdAb5UEcxiKwoSxkrQ41jq4KzgpUelT8xRwpZgSRlVh-zgqQlLw8MvjmhvcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7020a91df0.mp4?token=MyrHL7sttp1Fms7qUsJsONsiV68k8MfyPZX47apVMm4IJAyx6rpCyg3IL8XAJUeKyll9LNGk9aY6M-jwUUMGvg-bIePWUJoXbHf2XbGy9CvAd7xOt-f_wWI-MNsA1LW4QLTSN21_dQb5yq8iq39Y0H-iMF_ksecQhJ4e1gC93y0n-Zz8r0uJ0JPwlQFnzQ0gYi01VI0vI-kkENHCN7co_EQp-Xbur4_o6MdRjozZg4j5Ky9nxTxS6YR6P3besfNIW8P7pbRCauqz9wv3iNNO5Bz6TEXdAb5UEcxiKwoSxkrQ41jq4KzgpUelT8xRwpZgSRlVh-zgqQlLw8MvjmhvcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
- لینک سایت در مرحله اول  - لینک سایت در مرحله دوم  #GPT5 #AI #API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/archivetell/6335" target="_blank">📅 12:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enc0hLmOPCDp_LntLDOGuzJ2ABRdUEzThPSqflKUTyDicp4B2mxiIKRwgQD4xkeVRW2_EcWe1468AgMEVCEXB5Ngm8eA0L77vSLfQstStgbFdUU1g_65N9aPkNnNS5RhAnKaxBG4sMSZ6CeFvw21QSGJqnA8DHCegqEQ6JXCaZpe0xLWsDMVJJxlTtoeIAejC3Tct6oqICtmr2IbLTGYdSyBG7GRhvteYS8zm-t1iai-9M8GIKAdvuX-DPASGjPNL_5SOjupg89x33CTn2VgUH9S-Dcnt1irrlSWKUs2rM67CbtwhozO8GaXOH7W16zJk7mg0P5VU7mCD_pG8sMeHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 گیگ اینترنت رایگان همراه اول
تو برنامه همراه من وارد بخش زمین بازی بشید
به تب پیش‌بینی برید و یک بازی رو پیش‌بینی کنید ، بسته به صورت خودکار براتون فعال میشه
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6334" target="_blank">📅 11:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duqiYD6fik0NMpE4U_HrRf3OUxsK5u-4ENQOfB31lu4lc60XHnMOJfijA29BZTqa5OmssCM1w4o2OZ6xB36SLbzrfGyM9XGeXefIntiQwOuvoplN2X9w0xiZF0AEGmhMIw0acMatxNuOYFgCpozSILfFUomrxim6ln-0Ewqriz4zc_mAHCWu4la5SbsIrUrVPObXawfgFZitaCPkY73N5_uV-iulZBS1YmgF9sh7lureusFEEA1lKSXX1v-blkFpLyQeF1eEaeo4e9ub_cOzDBaORuZBhRaFtkmnzeD4q5CQCWy4LRz8dhWGiixlurpvSGMZECANLmQ-z8pLEFNBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دریافت API رایگان GPT 5.5، کاملاً ساده و با اجرای قطعی!
🌟
این فرصت استثنایی را از دست ندهید
⚡️
-
لینک سایت در مرحله اول
-
لینک سایت در مرحله دوم
#GPT5
#AI
#API
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6333" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmDva6biqyc3MHpmjc5PoWCE3QoqXzXpK27w7e0IfhPi1Njz8xmC0F-tbMBZ_gED41ICPEtPLx0tGLRG5WlK6HUrZLu6hqXh7tjDHXNdd-45dXaRkP0caH0etpocf-12wWFsvrq-Nlpjn0hOeU1UBcyxx8sC1sOAM5uCp9r4nuR7oRv192vNadalDLD_AD9S-Vs2uAszgNDTSJOAbjEhhFao-oNn1Pcbt5ovUp3McIgAYDDYHzMOR0NeUuY0c7eqSwgM1MB0N-SvRab2FqKoeTO1Qt0O_bemfYyLpZFgNF5prBj6Xtv5kmC_D_bpKktrZtf7iQzXia34GykW5R29UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی تلگرام
🔥
بدون vpn وارد سایت بشید..
https://proxybolt.link/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/archivetell/6332" target="_blank">📅 09:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSSHV0pwi9o6ceYFMd0znSdcKIyvtciLd2C4fme2Tlj6n_Bv9XmT6WGEK6-_QtbGKhByfGG5Hvx3HzXBUrC0TefdPJVzhXEmU0nd9VcJTuV6U5j3qbv4ZBjEiOcsePSw8wiEUhN0L-LtZMksXsSjgBo7XvqxVGBka-ft5oQvtp8xLsDfY4yO4-L1L6U5UfgtcRDgbpvWgYL15oHPE8MlDsgDg65c5atQWcQ19AVDxv_uZfO6mrbb3851ZiPEI4YsMyaPUZcihTy_6MRrg6l6PqXKsrpC0FgV2IQTTEUnOOFoTOkAooOMjh73IhLq5-l-p9GlNEL2vJplOUnx7j1N_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت بازسازی عکس‌های قدیمی بدون از دست دادن حس نوستالژیک
📸
Repair physical damage on this vintage photo: remove scratches, creases, stains, and tears. Restore faded colors, rebuild missing details naturally, and keep the original grain, lighting, softness, and period aesthetic. Do not modernize the photo, oversharpen it, change faces, or make it look AI-generated.
#ChatGPT
#Prompts
#AI
#PhotoEditing
#Gemini
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/archivetell/6331" target="_blank">📅 08:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6df494956.mp4?token=W4ZdyLeLQGBSkAWEAWtOFVg7-VkHoLuw29lwwudniUdlMyezDRSA6nE90BuwxY64aeNfIXH_OwQlrA1T6EMAfZnBLq0iKwmcRHkY8xvLVbqClEA0BM6dCGz6eq0Y529SCKE_OHVlpHM6AsoJMbKLOgKr1E_pMv4tvPTIemoLmR2dFK5iMhRYV5EvnzmPHV5B6w-GSVf9Hl2PqjsYYQUFjeD3OZyrtFYh0n_0KupiC_UFw4K76-0WrIrF6Eji-knjGkeQYOIe0uvcFhUaTILRKZYEHRS0-3xbIHDZhSznb2ev3YNDOnt5ONEhl8S8pncsrZI4ghzSmf20TUVKR8sCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6df494956.mp4?token=W4ZdyLeLQGBSkAWEAWtOFVg7-VkHoLuw29lwwudniUdlMyezDRSA6nE90BuwxY64aeNfIXH_OwQlrA1T6EMAfZnBLq0iKwmcRHkY8xvLVbqClEA0BM6dCGz6eq0Y529SCKE_OHVlpHM6AsoJMbKLOgKr1E_pMv4tvPTIemoLmR2dFK5iMhRYV5EvnzmPHV5B6w-GSVf9Hl2PqjsYYQUFjeD3OZyrtFYh0n_0KupiC_UFw4K76-0WrIrF6Eji-knjGkeQYOIe0uvcFhUaTILRKZYEHRS0-3xbIHDZhSznb2ev3YNDOnt5ONEhl8S8pncsrZI4ghzSmf20TUVKR8sCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
ClaimCircle
با یک کلیک، خبرهای جعلی را شناسایی کنید
✨
قابلیت‌ها:
•
🔹
تشخیص خودکار متن، پست یا تصویر فقط با کشیدن دایره
•
⚡
تجزیه و تحلیل لحظه‌ای محتوا و نمایش نتیجه در همان صفحه
•
🛡️
حفظ حریم‌خصوصی: پردازش در مرورگر، بدون ارسال داده به سرورهای خارجی
•
📚
پشتیبانی از چندین منبع اعتبارسنجی برای نتایج دقیق
🔗
لینک:
https://chromewebstore.google.com/detail/claimcircle/ominadfbilailbklmclcmdbpmckckdad
#claimcircle
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6330" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها…</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6329" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHQKeKQO0cwOpfhOJxo86z9ELsbpz7xoO_f8PORBSC0pxP2BMtzgn9rOZr8GY8-blVrM9UDARUnc1XcVHJB5zJIz_oft4VYj_kVV4ZMziDiueC7OIyp0VgBOYIuGyvZoRSbxLrX99a2-ArktI_IH2jI09E7y9W_L3cLjT5-8t68LT9bb6SChKo2jspoQXPbqfW0ObzxcPLDcIsu968rc5cSGXPtKpky1N0tw1TATn2MCluE1T0DvspXpBDP7kTfy_gM8YbjoHzfcXQ7BglpEJta-Ogj6OXnLyx1eBaDMWn8SD0jc1yNDnoaXEqc1PNkJBi6M-3AgUIwENGVfBucZmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پخش FLAC با کیفیت lossless بدون محدودیت!
✨
قابلیت‌ها:
•
🔹
دسترسی به کاتالوگ گسترده موسیقی از تمام ژانرها
•
⚡
دانلود همزمان چندین ترک با سرعت بالا
•
🛠️
ذخیره فایل‌ها با وضوح اصلی بدون فشرده‌سازی مجدد
•
📦
پخش مستقیم بدون نیاز به سرویس‌های استریمینگ
🔗
لینک:
https://flac.music.hi.cn/
#Music
#Flac
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/archivetell/6328" target="_blank">📅 21:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
🔗
قابلیت AI Agnet در گروه
🔸️
ادمین باید از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات طبق اتمسفر گپ صحبت میکند
🔮
قابلیت خودمونی بودن در گروه
🔸️
ادمین از پنل استارت ربات در گروه به بخش تنظیمات برود و قابلیت را خاموش یا روشن کند
🔹️
با این قابلیت ربات بی سانسور و صمیمی جواب می‌دهد
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/archivetell/6327" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ArchiveVPN | کانفیگ رایگان
📝
کمپین:
50GB
🧭
شرط دریافت: حداقل 1 دعوت
👥
کاربران دریافت کننده: 50 / 50
💾
حجم تخصیص یافته: بر اساس تنظیمات دستی/مخزن
⏰
مدت اعتبار: بر اساس تنظیمات دستی/مخزن
🔴
وضعیت: غیرفعال / پایان‌یافته</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/archivetell/6326" target="_blank">📅 18:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hW0Keg4E1da_dG3eNyoybz2ISVKDBCaE54RHA7RJGSSQp1s1eo_pB3tvuooEeTUZ-U2G8KyVMAaHkEpIzl_9aRyE9JA_Pr2QDGFlCZFcL0X0-sgbUUOdB4q9K2HDdgduiBAcELAhCLXi6VuPJ8uHcNLRKDMNeOWkxp2mR3XbszXkBWjI3c2L_jERytKUfwsADj-r3-0o45qwH5c9wE-CqXcoYAVAGr3C0OHS2V9EJOaoib_K7GmoqT7kC8T321rjlV8kp2SCGUnNINNwacmnC3rrb4h5HG3NYZfnzWCj6vCsvn4lalAAaW6sHoySKSlhUEWpOnh4VAx30P45ChUFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید انیمیشن کوتاه از متن + عکس فقط با یک کلیک!
🎬
✨
✨
قابلیت‌ها:
•
🔹
حفظ ثبات شخصیت در تمام صحنه‌ها
•
⚡
پیوند صحنه‌های طولانی بدون قطع
•
🛠️
دوبله چندزبانه برای مخاطبان بین‌المللی
•
📦
رابط کاربری ساده و سریع
🔗
https://aianimation.video
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/archivetell/6325" target="_blank">📅 17:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M60mT1S9zBASQMPPYKYcF1gbwe5weJRUy8CVHOzd7Udz5FPZPrGCWviwuakAIEvc4t1UA1x8RLPqV3AkHskX3iYrLAx6VVeKwGMTrMyRqPEILWui_efglKXoocbotjEammBfs2lvftdJOIS0rg3FZAQxklvYuY_ZyZUdNxdmdMz1vyzJpCZRA1WmgOIcZ5LEJE-jPXcdG41T08nc4zRn5duk9V3Bp1Y1CqNe83At0vuxc4sgDLxlqdRWjISnpeTeghS-pY1TpPxE7CcD4kyOATfYobJ_idZPNJBoSM9Bpa8X6BD7o1BNvwdhi_Yrdc-Atrc4V_9Q_invgmoMmtsQCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تولید آهنگ فقط با توصیف متنی!
🎶
✨
✨
قابلیت‌ها:
•
🔹
نوشتن شعر، ملودی و تنظیم خودکار
•
⚡
ساخت موسیقی پس‌زمینه بدون حق کپی‌رایت
•
📦
خروجی با کیفیت حرفه‌ای
🔗
https://memotune.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/archivetell/6324" target="_blank">📅 16:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxm1FbsBVLxUrMmHyU1i8z74dNzV-GQ7qIjZzW8Hq0ZYvHESSvpRQbXwDUvwkfXJwokEz50xzzljsfww0UAySwUFjMn0NsXMZkH0ddH6WeGelHpwIAiHf6GndiHX40lSWD85DtLkSx7m6UGGv3iRvMU8XOVsmnZLf9AoS2GHluTDOwJiZ7wB9QBhnhlg_3nbZi3WgDO2dshOCD3c_c4i3dYOHG9k19juBk6gCbkPXrjqh2RY9gTiyO9VtxrpXDhnLrvqY6E7G9OvHsm_QJuz6Jgt-nbs6HHmxq5kajfHZZF4RYaKzkPczRi6c6ahfksZ5V-6BG7N819wxsbxgyQQlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ویرایش تصویر آنلاین با هوش مصنوعی، بدون واترمارک و بدون نیاز به دانش طراحی!
🎨
🖼️
✨
قابلیت‌ها:
•
🔹
انتقال سبک و رنگ‌آمیزی عکس‌های قدیمی
•
⚡
برش تصویر و حذف پس‌زمینه با یک کلیک
•
🛠️
افزایش کیفیت و ویرایش دسته‌ای سریع
•
📦
خروجی با کیفیت بالا در مرورگر
🔗
https://stylizeimage.com
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/archivetell/6323" target="_blank">📅 16:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=sYJAY5nzHYdnucDIPdb3oYS1FhG_R7gOT-D-y2tMDfmlcmReRrrfY7xz8YrEMa-FSNEGbHUwMpQUrv7NlyBUKdk9ynYrXufd9OtAYf9U1zwZoTU938OlY0qjLo2QuyYzzX8xFBsPFSpVpehBchc2RbD4sa1sfVpv-SoIzpmPhtdmh1bxl2oTOm3W5Pwje_YXgJmkE-3FHSlF5rO6KdVv5cf-1afEj9MbBRVedGBEHdfMka4TxdSxAYFqz-Wu2BxOgLy8cPQ_k9Kyfaz5kLV0Y0udK9pSGsX_TxlPHlouB_3kwXSsRfX6LR8UByz5n9VYSxS-HLE3N8ygfcthEY-QfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dbc365d49.mp4?token=sYJAY5nzHYdnucDIPdb3oYS1FhG_R7gOT-D-y2tMDfmlcmReRrrfY7xz8YrEMa-FSNEGbHUwMpQUrv7NlyBUKdk9ynYrXufd9OtAYf9U1zwZoTU938OlY0qjLo2QuyYzzX8xFBsPFSpVpehBchc2RbD4sa1sfVpv-SoIzpmPhtdmh1bxl2oTOm3W5Pwje_YXgJmkE-3FHSlF5rO6KdVv5cf-1afEj9MbBRVedGBEHdfMka4TxdSxAYFqz-Wu2BxOgLy8cPQ_k9Kyfaz5kLV0Y0udK9pSGsX_TxlPHlouB_3kwXSsRfX6LR8UByz5n9VYSxS-HLE3N8ygfcthEY-QfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه GlifAI، سبک هر تصویر را با یک کلیک کپی می‌کند!
🎨
🖱️
✨
قابلیت‌ها:
•
🔹
کلیک راست → “Glif it” → دریافت نسخه‌ای با سبک مشابه
•
⚡
بازتولید هوش مصنوعی سبک نقاشی، عکس یا صحنه فیلم
•
🛠️
حفظ جزئیات قابل تشخیص در خروجی
•
📦
کاملاً رایگان
🔗
https://chrome.google.com/webstore/detail/glif-style-hunter/abfbooehhdjcgmbmcpkcebcmpfnlingo
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/archivetell/6322" target="_blank">📅 15:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDbZrjiX9uhxYvghk_CS1l76wwztoRdrNF0YfjTAoEMyTSQ9GOx71ftFUNSVwjMxp0vJzr7JFkxyAnAfXNWOnMNRvn-7p3pjjPHrlVhz4VYdFJSRQWPH68jt_R_Ld1I4ko1BI1oiu855oKkV1LsTADUpYCRJGMzjajudTmi1RT4DmBIYT06lHwBUsjwmUY_N_kewk_8pz4DqNrUJTMZRDveB6QtV2ySUvZ0mY2dkUfdPxrkHCmAllIUS4o9OI8AcO9--gUNw1ou78FYQC6jdh_Ud4LPaiQ5R2QIpRcx-vYdZ8h78EYuWLJIJ3jwfIDZyOYS5t712lfPq318M95v3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنریت موزیک رایگان
🎧
https://www.musiccreator.ai/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/archivetell/6321" target="_blank">📅 14:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGFWify1P31iePA75CvRIGOuRigJ04qOD2D6wyMKoLyNhweKueeKbz8SH3HGRJiOo9ps4Qd5k4QVLQFDo86d-hsLQ6Qz3mDVyQ55TbkgKhDooBwnt14iOmafeu2veiLdTOFzmn7U2E6sSEmlyqmituZwnz3w5e_Ahf-NgHVD6J2NnuLWm1fdwEG4CdE78VR0mZDqWGnDn0lAglO1R8afCm2W_32ucZqaQTn0lNrrV4rzMZBzTkAIzzFoNimaxyIvGM2aKVbCUVigG5ziOpFVG8fTlB85O94obRYHLGWGEqm0n45tAeai64Fs0RbYurW3EoDZirHuN9arbzVFrTvRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSbd7QeVKFUnyiImDyYHM9zTo4J3HjyEqrpLMtqeoURNcU0801PiwhaUzlkLMqv-I__BEF0noYvqiAxYTldBTQIUtxZdEk1s7bNXWApoSBwXDmsTX4rDuFq8ROAiYFF2appwvGObRPDka6ezyDFMc6Y0KcifpJcm5HI9CshCpIDXoKf-66K96GrnwH29_CKHDZNRJpW6KUx9vqn2GfAVJKZ5KMi27_maRyI52pmHSjhMPq0m7FwK7cYhTWbuBQffvez5XHetpnqRlnCY8Q9ZWWFbn5lm8zq3eYVXXXfIgaEsoq9BSfjRhJXOq4mxyDoaxPuWJ-ih0q3B-ZYdOUQceQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/archivetell/6319" target="_blank">📅 13:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد
شرکت Anthropic به‌تازگی مدل جدید
Claude Fable 5
را معرفی کرده؛ اولین مدل عمومی از کلاس جدید
Mythos
که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:
• عملکرد بسیار قوی در برنامه‌نویسی، تحلیل، تحقیق و اتوماسیون
• توانایی مدیریت پروژه‌های چندمرحله‌ای و بلندمدت
• پشتیبانی از وظایف پیچیده مهندسی نرم‌افزار و مهاجرت کدهای بزرگ
• استفاده از مکانیزم‌های ایمنی ویژه برای حوزه‌های حساس مانند امنیت سایبری و زیست‌شناسی
📌
طبق اعلام Anthropic، مدل Fable 5 تا 22 ژوئن در برخی پلن‌های اشتراکی در دسترس است و پس از آن استفاده از آن نیازمند اعتبار مصرفی خواهد بود.
این مدل به‌عنوان قدرتمندترین مدل عمومی Anthropic معرفی شده و تمرکز ویژه‌ای روی وظایف طولانی، استدلال پیشرفته و توسعه نرم‌افزار دارد.
با لینک زیر ۵ دلار اعتبار
🎁
نیاز به شماره مجازی
⚠️
(ایران رو چک نکردم ببینم داره یا نه
😂
)
🔗
https://v0.app/ref/94OS6T
🔵
@ArchiveTell
| Bachelor
⚡️
#Anthropic
#ClaudeFable5
#AI
#ArtificialIntelligence
#ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/archivetell/6318" target="_blank">📅 13:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
عزیزان با توجه به اینکه جام‌جهانی و لیگ ملت‌های والیبال (مردان و زنان) در حال برگزاریه  و با توجه به جست‌وجوهایی که صورت گرفته هیچ شبکه‌ای به صورت کامل از تمام تورنمنت‌ها پشتیبانی نمیکنه
🏆
به همین منظور تیم ما یک بات کاملا رایگان آماده کرده که تمامی شبکه‌ها رو یک جا در اختیار کاربر میده و دیگه لازم نیست درگیر دردسرهای مختلف بشید
🛠️
✨
✅
این بات به شبکه‌های ورزشی محدود نمیشه و حدود ۶۰ هزار شبکه فیلم،سریال،اخبار  و.. را نیز پشتیبانی می‌کنه
آیدی بات:
@Bear_Tvbot
🐻
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/archivetell/6317" target="_blank">📅 12:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqPDYOqmYmSUZ83hqHSRclwGl5gfHJSHttmE10E5EyhKgpOE79dwRX8i0mDTKoceZ3-_XStG5LC9AzQpnCCLD3Nfh4SfrJSUiga4vvxfCIjFCufKAFdQYLUi-KAStPmbnAppxJZ6jiQEd6VRkgFIwKWn6Df_b8fRybnkvx12abrgTLCcCC00Zv78wUnOWJtPO1ZdP9x_NGYjtE9vU0C4mW5PGtnPeTQ435qIebwIXFDDf6aIGDlKV-UIa5WzKDsUEnyrJfvd0t5MT1-lOrWo0_jh8Dw_xdJAOAs68hufzh_o798vxrxLkmnxhIZaBCGy30Y3CfJIMcqu0KqJsNhCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مدل‌های پیشرفته‌ AI به‌صورت رایگان در Notion!
•
🔹
Claude Opus 4.8
•
⚡
Gemini 3.1 Pro
•
🛠️
GPT‑5.5
•
📦
DeepSeek V4
🔗
لینک:
https://app.notion.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/archivetell/6316" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1yyl5kn9hJjkurIkLa95OYagzWLb66OXWyB0rEUHkb2Vmk4oPumyDPlelUgI42x6vf9Cx41io-b66-v0MxRRMbp9KktMv90A1sJZzLxg5V_T_J8wxSlEVaaB0Nz-hMyBSGuGlDF22Nny22opS3Z5-IFRWC99gWZGKKs5YVI06uPD2HkeIgmR0_PmFEOzCMZu2Zb2uhH4bJXfP_Tz-Yc9RVu08ZttvcO_nBkwuTumy0LVJm5seanD3svYPPOD7gWSxJ0epwv3qQHedQB8jYrMAQCjC4gb4fH9OI8tj7uALjgejskEiSJa3I33DzM5lolvZaFtaQD-6z4KKaZ0RwN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VejCT85P9sN_A_sjfo9HHHmKlRsEG2woR5RoxIXbFW_3DcZ6E8h_38JdzdTEYafrJC1kDZoJIw4G5GFpteTFdyjFj5WmsmNH3_LBEjqGaby7UjY-c58s_VUbspwh7Vlknml7NCwtJA3KxCFUTwzsGjgum-ak_r1iKi1hXtcUu-gdwPXsqjS_fZgACEYdVFwdIEDSOtYbWWGwJspZ6cWsJy6SYXyzZ9dFs3NPI1lISQaQu0SWCYrm_vQmQK7rhGJalSkPYXDwdH-hh4DHuyBrBA3qAQpkJCSlUIYcHAFAHt2Gkr6AF0R-FRMWg9sMkdUcz3CLMxjYFE4Ep60LJhvztw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=jxfIxDzA3xfmFJmaNnZKsQCgGzGQybP_2AVHPow8_pp7HDl9J88HZWdwXIUcoVfiwhYmG5aCbdAyyZA7JRbnAl2LAYehQSCpFbWjaBIBdC7jpFDJ8qDue4SJD15QAaldL0YMPhfIagjzwnJinnMFa5BZJynNA94HZGSJ57StAcdOVbffDtsZB9viRWGwZVlHt0LvbkhVw9X_FM8_rajVz7CYsGRwvG5uR2GttniJl94d0yTIJkDS1QjODrlA-9PkF9QgyM_2qJ7BozZRu_U46lQCMk8KkRUvfkAbIqFTTZ_Q7sE5J_0T_sk30nRqQvqW8gD01q4AXaMgGMe7bX6oAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0889cae7d.mp4?token=jxfIxDzA3xfmFJmaNnZKsQCgGzGQybP_2AVHPow8_pp7HDl9J88HZWdwXIUcoVfiwhYmG5aCbdAyyZA7JRbnAl2LAYehQSCpFbWjaBIBdC7jpFDJ8qDue4SJD15QAaldL0YMPhfIagjzwnJinnMFa5BZJynNA94HZGSJ57StAcdOVbffDtsZB9viRWGwZVlHt0LvbkhVw9X_FM8_rajVz7CYsGRwvG5uR2GttniJl94d0yTIJkDS1QjODrlA-9PkF9QgyM_2qJ7BozZRu_U46lQCMk8KkRUvfkAbIqFTTZ_Q7sE5J_0T_sk30nRqQvqW8gD01q4AXaMgGMe7bX6oAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
تلگرام به‌روزرسانی شد: پشتیبانی کامل از Markdown و امکانات جدید
✨
قابلیت‌ها:
•
📱
دسترسی در تمام ساعت‌های اندرویدی
•
📝
قالب‌بندی نامحدود برای ربات‌ها (حداکثر ۳۲۷۶۸ کاراکتر)
•
🤖
ربات‌های هوش مصنوعی می‌توانند درخواست‌های عضویت در گروه‌ها را پردازش کنند
•
📊
امکان افزودن لینک به گزینه‌های نظرسنجی
•
🌐
باز کردن سریع لینک‌ها در مرورگر پیش‌فرض
#Telegram
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/archivetell/6311" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRdZ_m7o8E5eZafbtH38l1tw5clkZil5lIjZ1USwvlf5njq5gPzw_E9PwiJKK2QpTDWhm1lWlGF5Nx95CatkBYhT-rdsbORTm-FziM_6U1r2vN0-PcKr0azgWSkR3q2r8e0WAYl_6phs7Ne8xxBUdLIYKxgF3DwBRCPqZjsabOyIv8m-L57QayIjEu2rzYYgz8jM6Bzs8LCvv-DGXOvkW2-COm4z5sN_CwK3S4OBDSY6oPGVfGVKe-GqF2h9HpfrJPK8dC69n12S6lt6Sc4DgdRaCALSsNKTVsutX6Iz9s6j1zGJRHMpQlCebwDThPqwlthUcCkocs3IPuaJ-zkFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
MemeDepot
کتابخانه‌ای بزرگ از میم‌ها و گیف‌ها برای استفاده در شبکه‌های اجتماعی
✨
قابلیت‌ها:
•
🔹
جستجوی پیشرفته بر پایه دسته‌بندی و محبوبیت
•
⚡
فید و برچسب‌های خودکار برای میم‌های روز
•
🛠️
دانلود بدون واترمارک و ثبت‌نام
•
📦
به‌روزرسانی مداوم محتوا
🔗
لینک:
https://memedepot.com/
#Meme
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/archivetell/6310" target="_blank">📅 11:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔥
دامنه رایگان 1 ساله!
اگه دنبال یه دامنه رایگان هستی، از سایت زیر می‌تونی کاملاً رایگان برای 1 سال دامنه بگیری:
https://domain.stackryze.com/
✅
قابل اضافه کردن به Cloudflare
✅
امکان ست کردن نیم‌سرور دلخواه
✅
مناسب سایت، پنل و انواع پروژه‌ها
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/archivetell/6308" target="_blank">📅 02:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCT_Q8LI61KDbI5I4-aj_BsPu1wRtlOSSdRB41M7-U-jSqK7w9v2x73XkWF7xSbLC-hUVy071wNy1NCN8E7mr3qOfvFEdPsMMuAhLB1Z9N7Da0o8uUUTArViqcQLTlOaKvLOD1pMPXuFxk5F02fll64XjYvDoLrWk_6oezYGaMaHcsqX0z4xac8C4X3oKE3qvdRIVbbitxKBe8B43A3J9B18pMX02aNS79rkHVZwwE66x_cz122t43URoaJw72vqOrB6a5LoGHuX7PId9KQ6tYQDqMVzQjgS59NKjTa9EOslc39aIm-3iYD3aCQ1Y_3GMZZhBMttAmZ-eFLJW_K_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕵️‍♂️
CloakBrowser | مرورگر ضد شناسایی برای اتوماسیون
مرورگر
CloakBrowser
یک مرورگر مبتنی بر Chromium است که برای کاهش شناسایی ابزارهای اتوماسیون طراحی شده و تلاش می‌کند وب‌سایت‌ها آن را مانند یک کاربر عادی تشخیص دهند.
✨
ویژگی‌ها:
• مبتنی بر Chromium با تغییرات در سطح کد منبع
• سازگار با Playwright و Puppeteer
• قابلیت اجرا روی سیستم محلی، Docker و سرور
• مناسب برای تست، اسکرپینگ و اتوماسیون وب
• کاهش احتمال شناسایی توسط سیستم‌های ضدربات
⚠️
توجه:
هیچ ابزاری تضمین نمی‌کند که همیشه از تمام مکانیزم‌های ضدبات عبور کند. استفاده از چنین پروژه‌هایی باید مطابق قوانین، شرایط استفاده سرویس‌ها و ملاحظات اخلاقی انجام شود.
🔗
GitHub: CloakBrowser
#OpenSource
#Chromium
#Playwright
#Puppeteer
#Automation
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/archivetell/6307" target="_blank">📅 01:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):  Aistudio.google.com  @ArchiveTell</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/archivetell/6306" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مرحله یک طهلیل من به واقعیت پیوست
😝</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/archivetell/6305" target="_blank">📅 23:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrRqh9_odRh9oqKPeTpqkMoOT7CirQPZUPGcLv3ZmUB1LVoj6OeNM82avZ5_vz5Mrf31tmM0rGACZ13K8eCwgPFfEZP7X23Cq2lCBY7Ymh5Wrs6hIJ1R0tkHPeKuMk3RnSSU7FNgkSaxOhDy-XzrIo_JNop09uhumlwji8SXza3bNSFIjCY3ZsOemn_ONuf2ksuqgBXHcJP4IpMKDICtnxswTNu5B03rbXgWJkFUWWVoZtI9Vh9bxY5_kIl2w-XVntN1bNFoWJPVeAff77cs--F01LZr8vvGvnPbtBdmGo_LYpXvmV3n5KgrJ-tMyxAdTb2Am3fqJH3PpoSKRM6vVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به تمامی مدل های پولی گوگل(Gemini 3.5):
Aistudio.google.com
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/archivetell/6304" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک تهلیل فوق العاده جالب از آینده ایران
👇
https://tahleel.netlify.app    بخونید نظرتونو بگید    @ArchiveTell</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/archivetell/6303" target="_blank">📅 23:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📢
جدیدترین قابلیت‌های
ربات وگا
را معرفی می‌کنیم:
📚
حل سوالات درسی در پیوی
🔸️
در بخش سرویس های هوشمند
🔹
امکان ارسال عکس سوال
🔹
جستجو در منابع آنلاین
📝
خلاصه خودکار موضوعات گروه
🔹
هر شب ساعت 21:30 ارسال شدن خلاصه مهم‌ترین مباحث در تمامی گروه ها
🌐
بهبود سیستم جستجوی وب
🔹
نتایج بسیار دقیق‌تر و معتبرتر
🔹
دسترسی به اطلاعات به‌روز تر
📰
آخرین اخبار هوشمند
🔹
هر ۸ ساعت بروزرسانی می‌شود
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
⚡️
Vega Bot
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/archivetell/6302" target="_blank">📅 22:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II69ZcLErJDa6Baav6jue7Y0rTww1u7bUgKD9XgsTp8D_9rSPsLr61hB7KcRmC8RkSiM0Dizg4dQPezQsbGz3VOobiDA93aDvlhpOm4b0VBN5LhPzM_FPZqEj-HLniYXhKTQrs8ZQkURBHknD6kdErk4g6Twedu8WAYLp-Ca7160rOhWPq38xe3hiFoS1A-3L8U1u4pITpc1a1PstUfcVWLFLOALWEFaeW2NlKCiwM80fEWq4HrLLfP3Pj3Dy-_69pm0rYKsYeAM7P_CY-_4WBRpBgZc1v_QUUpv9DVz0sbkHlpgrDUEPWzD8zH7bLx8nXbtN7o91dsiTxOmztsfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
OpenAI برای برخی کاربران API Credits رایگان ارائه می‌کند
اگر از APIهای OpenAI استفاده می‌کنید، می‌توانید با فعال کردن اشتراک‌گذاری داده‌ها برای بهبود مدل‌ها، به سهمیه و اعتبار رایگان دسترسی پیدا کنید.
📌
مزایا:
• سهمیه روزانه برای GPT-5.5 و مدل‌های Mini
• اعتبار رایگان API برای حساب‌های واجد شرایط
• دسترسی مقرون‌به‌صرفه‌تر به مدل‌های هوش مصنوعی
⚠️
توجه:
با فعال‌سازی این گزینه، بخشی از داده‌های ارسالی شما ممکن است برای آموزش و بهبود مدل‌ها استفاده شود. برای پروژه‌های حساس یا حاوی اطلاعات محرمانه، قبل از فعال‌سازی شرایط را به‌دقت بررسی کنید.
مسیر فعال‌سازی:
OpenAI Platform → Data Controls → Sharing
#OpenAI
#API
#AI
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6299" target="_blank">📅 22:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/archivetell/6298" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=Gxu-4TG6QarN5C1KeG2bVgvPKDbCXkOnuj79r2jHkFdvzgVWxhn7scSR4CcSf3ZkzNhx8RqPbLfDrecz45Q72UO4a8f2R3xfpV7JwdnBtSjkVjlttioV-maaIw6EWEpsc25fNGIDdRr9ahhe3yy-QDTPhwQU46junEjk125sd_7g1J72FTdMTyBLmGDMggG2nbo-acCsr4wIASINEwT3_zO1PUnS20ZfaK43p985HS0_VqDel49tm30XUdpuSo2o8R93PDDqLMzu3SsfCxLZrvQlgeqvwe3fpOrSHvb7TeNtAT1J7zddfSl7lFFgEJAKrVAPrEsGEoCuhyugdX-j4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253323d5d.mp4?token=Gxu-4TG6QarN5C1KeG2bVgvPKDbCXkOnuj79r2jHkFdvzgVWxhn7scSR4CcSf3ZkzNhx8RqPbLfDrecz45Q72UO4a8f2R3xfpV7JwdnBtSjkVjlttioV-maaIw6EWEpsc25fNGIDdRr9ahhe3yy-QDTPhwQU46junEjk125sd_7g1J72FTdMTyBLmGDMggG2nbo-acCsr4wIASINEwT3_zO1PUnS20ZfaK43p985HS0_VqDel49tm30XUdpuSo2o8R93PDDqLMzu3SsfCxLZrvQlgeqvwe3fpOrSHvb7TeNtAT1J7zddfSl7lFFgEJAKrVAPrEsGEoCuhyugdX-j4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی ۱۹۷۸ ایران، فقط یک تیم فوتبال نبود؛ نماد غرور، اتحاد و جسارت یک ملت بود نسلی که برای اولین‌بار نام ایران را در جام جهانی طنین‌انداز کرد و نشان داد که می‌توان در برابر بزرگان ایستاد.
از ملبورن تا آرژانتین، از صعود تاریخی تا تساوی مقابل اسکاتلند، این تیم برای همیشه در قلب تاریخ فوتبال ایران جاودانه شد
❤️
یادگاری از دورانی که فوتبال، فراتر از بازی بود، یک رؤیای ملی
✨
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/archivetell/6297" target="_blank">📅 20:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jN5rVVGzIJvR8369f8tRdoryVSdLwGJaWWeO49uvBIuCnFRGcygXd91H8XGFgkoDDi5tKzsS2b7KWeGiXehyNlJnbdskyJNaJR1IyfvEoK--yycRHvTmxII_ruuJIPhJIXxBH5kJkY28aPGPLuZSfFxvXW8jz3uqnv45Q2T8TXq4H-Zg_H66-nt0_ot4HQI5hSqtbUwIqptaSOFmm_RN2edwHDr6TSc9gBu2hih1G-rJA5ba8Et7W8HS9k3hgaecXawa-aBteozEhOstrXpQgKGyF_dJYklWzyTtE9J63Y6jdRQmjie97j7JWYx-lzxRshSn8z6rw7tBBj1bUhY-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
RuView
با استفاده از سیگنال‌های وای فای، بدون دوربین یا حسگر، موقعیت و علائم حیاتی افراد را حتی پشت دیوارها تشخیص می‌دهد!
✨
قابلیت‌ها:
•
🔹
ردیابی ۱۷ نقطه از بدن انسان
•
⚡
خواندن تنفس (۶‑۳۰ نفس/دقیقه)
•
🛠️
اندازه‌گیری ضربان قلب از راه دور (۴۰‑۱۲۰ bpm)
•
📦
دیدن افراد تا ۵ متر پشت موانع و ردیابی همزمان چند نفر
🔗
لینک:
https://github.com/ruvnet/RuView
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/archivetell/6296" target="_blank">📅 19:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگه میخواید به سرورتون وصل بشید ولی مشکل وی پی ان و این چیزا دارید و روی cmd و ترمینال و این چیزا وی پی ان سیستمتون کار نمیکنه میتونید از ssh آنلاین تو خود گوگل کروم استفاده کنید.
https://webssh.webhorizon.net/
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/archivetell/6295" target="_blank">📅 19:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌐
Javid Mask | ابزار افزایش حریم خصوصی برای کاربران استارلینک
اگر از استارلینک استفاده می‌کنید و به دنبال راهی برای مدیریت بهتر ترافیک شبکه، فیلتر کردن دامنه‌های ناخواسته و افزایش حریم خصوصی هستید، پروژه متن‌باز
Javid Mask
می‌تواند گزینه جالبی باشد.
✨
امکانات اصلی:
• محافظت از حریم خصوصی و کاهش نشت اطلاعات شبکه
• فیلتر کردن دامنه‌ها و وب‌سایت‌های ناخواسته
• راه‌اندازی ساده روی سیستم‌های لینوکسی
• پشتیبانی از Raspberry Pi (از جمله Raspberry Pi 5)
• دریافت به‌روزرسانی‌های جدید از طریق پروژه متن‌باز
📋
پیش‌نیازها:
• سیستم‌عامل Linux
• حداقل ۵۱۲ مگابایت رم
• حدود ۱۰۰ مگابایت فضای خالی
⚙️
راه‌اندازی:
1️⃣
سورس پروژه را دریافت کنید:
git clone https://github.com/rowdy-ff/javid-mask.git
cd javid-mask
2️⃣
فایل‌ها را بررسی و دستورات نصب موجود در پروژه را اجرا کنید.
3️⃣
پس از نصب، تنظیمات موردنیاز را اعمال کرده و دامنه‌های دلخواه خود را برای فیلتر یا مدیریت شبکه مشخص کنید.
💡
این پروژه بیشتر برای کاربران استارلینک در ایران طراحی شده و هدف آن بهبود کنترل شبکه و افزایش حریم خصوصی است.
⭐
متن‌باز و رایگان
🔗
GitHub: rowdy-ff/javid-mask
#Starlink
#Privacy
#Linux
#OpenSource
#ArchiveTell
⚠️
قبل از پیاده سازی و نصب، لطفا کد منبع رو بررسی کنید.
چنل ما هیچ تعهدی در قبال این پروژه ندارد.
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/archivetell/6293" target="_blank">📅 17:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTm6ym1lYjXRvf4rbj9m8xPK25jOe5jIOPIuQxiTA7Vy5l4nIr5osx8WEhUQWNq0ZvDZgG-qYVWFt7MHExVKUdvUQRp9dm6DFZtOY92NpaHLpeLuJPxpuuKnXLA4vcRuQHABXXACmNT_YkAz-vLlSK5lFDvp89MJlThEjFcOKiW0N10ed0Jo3ZlqKX8uwNUCrB3rSeLLQ8zW0yljNBPd1F_yHtxt7pVbai6xCmZmcWrU_9DLzwMCfsba-uolOdueTtbQtISwWpAsSujTodLUcxJGD57CG2c-K7mfmzrRCOzcDn_y7osn0tR6aF2tqrHp5gb76mDc9QK9jKPmInJHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v98xi_IgxdH61dJi1vt6zLqABe2v9iSkmwbTWfFX_gHmQIoCe5v4KJoNnMl_j61SUocxPSsj1fOKKMPyLHTfzJx7jzV9smn0qWZkKgEBd3J6haNmX4ZmjUeWKZEWHCErWz1uxU_6sYuoXv9twLRAanf1Mf3SdxBiVQelq3If-S_4Af2epun5HQRHAB2WqnZTudgz53zEqSmvDLJNlMMuX9O6UhGLXeKt8MNXyIoNGF2VTxJUrF_hBBEQn6OOYO99hBCv_-fUX5Mj_11UAUz3XhVOkcEDbFevq1W03wG8vYSuyBJ4RK3nyrxwnt3PRHxxGoAMl0iz1Bo7XMDYO0rKcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-cdfsF9GA-NJoI7kvMBqLpstkqb0XqFhsjdl8snBEG6K0_dQvq4F5Q0epNV27D9SHCJg2LywDbnCJalX73U8Z0oOSYggF_SXg_Wx1wIQeMMJxj1RgN686P_sCmcjKyviWOJA4fE7jGXQV0dub0sKNIA9EMCZGcItpmKHSOX3HJR2OZAIUbfw_lyDoZiOKl929NjN1uNWlCRA8Ju0k0MTnyr0jIUjg4MkFwxHMIXfmGPd-IstSecfYD-ddN1c918sg3LeoRz4SxMeV0LI2Vr1lV9zEUEHqDFdHN-G56TRHNJslx-Xx2M0TOOuKYbgzPqqK4MtUcM74Ulre6FFMr9zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
شیائومی MiMo Code: مدل جدید هوش مصنوعی برای برنامه‌نویسان، با هدف پیشی گرفتن از Claude Code.
✨
قابلیت‌ها:
•
🔹
کار با پروژه‌های میلیون‌ها خط کد بدون محدودیت
•
⚡
پردازش مخازن بزرگ بدون از دست دادن داده‌ها
•
🛠️
آموزش مجدد مدل در حین کار روی پروژه
•
📦
تمام این‌ها به‌صورت رایگان و متن‌باز
🔗
لینک:
https://mimo.xiaomi.com/coder
#OpenSource
#Xiaomi
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6290" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54834411b8.mp4?token=KE7cGFtXXfrgxULYha5ZfKC9bE5XcDM_mvFexs0Rh0kDBgCwvOlNi07V2nL4336DSrlX9d6UbpnkcrHptckTPpMXU7Hoj8iA-7hxJQ7Zu8s-DRE30Ms2cwN9TSCTOBUxDevjIKRXe5UfPYceU0VQJzC5fdn4q4udE7txCZm_s0m-Lgerm6yOAVWhTFlMJqP_m7jAKBEbQHoK19ZN6shXX5PucaxxzBmykGVAahdOqJ6WLL2MWLOYjlxMWvo9lqngv5CaM8BYkKcnY8p5taBooAq0d4lmhXdss7SdIJgB4mqWIFjY91jQzRCJe_AXUBzmeWh696ZI0aksd2VPMzgzNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54834411b8.mp4?token=KE7cGFtXXfrgxULYha5ZfKC9bE5XcDM_mvFexs0Rh0kDBgCwvOlNi07V2nL4336DSrlX9d6UbpnkcrHptckTPpMXU7Hoj8iA-7hxJQ7Zu8s-DRE30Ms2cwN9TSCTOBUxDevjIKRXe5UfPYceU0VQJzC5fdn4q4udE7txCZm_s0m-Lgerm6yOAVWhTFlMJqP_m7jAKBEbQHoK19ZN6shXX5PucaxxzBmykGVAahdOqJ6WLL2MWLOYjlxMWvo9lqngv5CaM8BYkKcnY8p5taBooAq0d4lmhXdss7SdIJgB4mqWIFjY91jQzRCJe_AXUBzmeWh696ZI0aksd2VPMzgzNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
Every‑PDF
ویرایشگر رایگان PDF با پردازش محلی و بدون ارسال به فضای ابری
✨
قابلیت‌ها:
•
🔹
افزودن متن، امضا، تصویر و واترمارک
•
⚡
تقسیم، ادغام و تغییر ترتیب صفحات
•
🛠️
رمزگذاری
•
📦
کار با فایل‌های بزرگ به‌سرعت
🔗
لینک:
https://github.com/DDULDDUCK/every-pdf
#OpenSource
#PDF
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/archivetell/6289" target="_blank">📅 16:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📊
خلاصه یک سال فعالیت گیت‌هاب در چند ثانیه!
توسعه‌دهنده‌ای با نام
PankajKumardev
ابزار جالبی به نام
GitStory
ساخته که فعالیت‌های سالانه کاربران GitHub را به شکل کارت‌های آماری و قابل اشتراک‌گذاری نمایش می‌دهد.
🔹
کافی است نام کاربری GitHub را وارد کنید.
🔹
سرویس اطلاعات عمومی پروفایل را جمع‌آوری می‌کند.
🔹
سپس آمارهایی مثل تعداد کامیت‌ها، ریپازیتوری‌ها، مشارکت‌ها و فعالیت‌های سالانه را در قالب کارت‌های گرافیکی نمایش می‌دهد.
﻿
💡
اگر توسعه‌دهنده هستید یا می‌خواهید نگاهی سریع به عملکرد یک سال گذشته خود در گیت‌هاب داشته باشید، GitStory ابزار جالبی برای بررسی و اشتراک‌گذاری دستاوردهایتان است.
https://github.com/pankajkumardev/gitstory-2025
#GitHub
#Developers
#OpenSource
#Tools
#ArchiveTell
🔵
@ArchiveTell
| Bachelor
⚡️</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/archivetell/6288" target="_blank">📅 14:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚀
دریافت ۲۵۰ دلار کریدیت رایگان برای API
اگر دنبال دسترسی رایگان به مدل‌های زیر هستید، می‌تونید با Agent Router API Key اختصاصی بگیرید
👇
🖋️
Claude Opus 4.6
🧠
Deepseek v4 pro
⚡
GLM 5.1
📌
مراحل فعال‌سازی:
1⃣
وارد سایت
Agent Router
شوید
2️⃣
اگر سایت به زبان چینی بود، از بالا سمت راست
🔝
زبان را به English تغییر دهید
🇺🇸
3️⃣
روی Sign up بزنید و با حساب GitHub وارد شوید
🐱
4️⃣
وارد بخش API KEYS شوید
🔑
5️⃣
یک API Key جدید بسازید
➕
6️⃣
طبق راهنمای این سایت، از کلید ساخته‌شده برای اتصال API استفاده کنید
⚙️
💡
با این API می‌توانید:
🤖
ربات تلگرام بسازید
🌐
وب‌سایت طراحی کنید
⚡
ابزارهای اتوماسیون ایجاد کنید
💻
پروژه‌های هوش مصنوعی توسعه دهید
🔥
فرصت عالی برای تست مدل‌ها بدون پرداخت هزینه
💰
﻿
@Archivetell
✨</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/archivetell/6287" target="_blank">📅 12:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⚡️
سیم کارت رایگان همراه اول به خاطر جام جهانی (کد تخفیف + پست رایگان)
CUPSIM26
هر کد ملی تا ۳ تا میتونه بگیره (همه رو تو یک سبد بذارید)
لینک خرید
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/archivetell/6286" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=DnclSc8qFm6eCGpDFj4OdjzWHfAu5Jyi4O-S05tvtLl-z9YIO18mD2MFKTV8-jT-vyz-ih1imVhtGInAdPdpeBjGoNlqGvamx8Pks7kLG2yYAixkqPtNDOVJ7gkKNybX9Dp0YBMkgLhklKNgmiNYLdRF8Jv1Ydlp1ctA21p0G0iJA5OZzT2HihRIaSwkv1HLEkktsFioXAbSxdAunUjZD5ND_8O--7GGrlgVhHoeUhlvzaAsmdedqnj1wQuGAh-p9zL8Arg0tjuJn82z-QZ7BSouNVTKKgPxjQU-D_rG7P8kRkX0dl_yZr6bw3zbf5McRWhk9Xef1xqOjPPfOAvRPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6bb99e167.mp4?token=DnclSc8qFm6eCGpDFj4OdjzWHfAu5Jyi4O-S05tvtLl-z9YIO18mD2MFKTV8-jT-vyz-ih1imVhtGInAdPdpeBjGoNlqGvamx8Pks7kLG2yYAixkqPtNDOVJ7gkKNybX9Dp0YBMkgLhklKNgmiNYLdRF8Jv1Ydlp1ctA21p0G0iJA5OZzT2HihRIaSwkv1HLEkktsFioXAbSxdAunUjZD5ND_8O--7GGrlgVhHoeUhlvzaAsmdedqnj1wQuGAh-p9zL8Arg0tjuJn82z-QZ7BSouNVTKKgPxjQU-D_rG7P8kRkX0dl_yZr6bw3zbf5McRWhk9Xef1xqOjPPfOAvRPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
OpenAI
تا ۵۰ هزار دلار اعتبار رایگان API میده!
🎉
•
🔹
۲۵۰ هزار توکن در روز برای GPT-5.5
•
⚡️
۲.۵ میلیون توکن در روز برای مینی‌مدل‌ها
•
🛠️
تا ۱۰ میلیون توکن در روز در سطوح ۳ تا ۵
•
💥
در عوض، داده‌های شما برای آموزش مدل‌ها استفاده خواهد شد.
📦
این ویژگی برای همه فعال نمی‌شود، اما ارزش امتحان کردن دارد — وارد OpenAI Platform شوید، Data Controls را باز کنید و به بخش Sharing بروید.
🔗
لینک:
https://platform.openai.com/
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/archivetell/6285" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co5I8HkNHmrvlsAnZUcTxmuG-ha6MLCbw8-pPxf4FTHNPC1NSuJZhEMyEjgEPB4B2ESoc7ZyNhHW5Q3InWpG5YDhYx4X2_O_wDZaDypnDl_Y2PI12-Nm1_HN47nc90ycbjpz0VRpp3i0SeTcx-yR0SnGpPvKNO09oBqCtj8HlKfex3Oqiv7CwnRCCzF4HBocs-V87_WHWei-UsgBVnNAR8MFvqCjaTt9FONjCJ4EoqMnIi-XRz0qoeXNBdrrpb4HAWRBiXeoR2QOngHkYp9_Y_xhqVnS8CrgNtePeAviTBf_X9schlFVlo3AlLSSKny0j_nbGUWSN21LdpmyCpFoEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
BrowseryTools
مرورگر خود را به یک جعبه‌ابزار قدرتمند تبدیل کنید! 136 ابزار رایگان برای فایل، رسانه و هوش مصنوعی، همه در سمت کلاینت.
✨
قابلیت‌ها:
•
🔹
ویرایش تصویر و ویدئو بدون نصب
•
⚡
مبدل‌های فایل سریع و آنلاین
•
🛠️
ابزارهای توسعه‌دهنده با Next.js + TypeScript
•
📦
هوش مصنوعی محلی: رونویسی، ترجمه، حذف پس‌زمینه با Transformers.js
•
🌐
متن‌باز و قابل میزبانی مستقل
🔗
لینک:
https://github.com/aghyad97/browserytools
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/archivetell/6284" target="_blank">📅 10:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=Ol4F-4ux1Vib5vmAY3P7h3DKS6g4OE4JU8t3PorwI0ZAZ4RIpXOmLp6Rj0knQ2ws8K0y3638m5fZiNNUT8mdiOt6BH8BmHjAjsxtAwzZ8iV_qMri6dR73A6RqoQEuvgiYh_ujyYkt5cMCBMzefxLl-R3TDv1TTPilt1H5DqrbtV8Fhp-ef_LYyrRr8WC4xoYIyavqmlM-5JH9B4iA7drdTtQpqkgPOybnYPKsRZzghqMMgo70ZwiW07eZcVGK0c5wW3gpQ85l84AIBDkTIM6aXmsByJxgk35Vq6WNA10Qxr87Q49lopxn_N3MwfbH3-eRoTXgInl4tm6XIu_KwLr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59619c8a4a.mp4?token=Ol4F-4ux1Vib5vmAY3P7h3DKS6g4OE4JU8t3PorwI0ZAZ4RIpXOmLp6Rj0knQ2ws8K0y3638m5fZiNNUT8mdiOt6BH8BmHjAjsxtAwzZ8iV_qMri6dR73A6RqoQEuvgiYh_ujyYkt5cMCBMzefxLl-R3TDv1TTPilt1H5DqrbtV8Fhp-ef_LYyrRr8WC4xoYIyavqmlM-5JH9B4iA7drdTtQpqkgPOybnYPKsRZzghqMMgo70ZwiW07eZcVGK0c5wW3gpQ85l84AIBDkTIM6aXmsByJxgk35Vq6WNA10Qxr87Q49lopxn_N3MwfbH3-eRoTXgInl4tm6XIu_KwLr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
افزونه ImageToPrompt تصویر شما را در چند ثانیه تحلیل می‌کنه و یک پرامپت آماده برای مدل‌های تولید تصویر می‌سازه.
✨
قابلیت‌ها:
•
🔹
تشخیص سبک، اشیاء، نورپردازی و ترکیب‌بندی
•
⚡
تولید پرامپت دقیق برای Stable Diffusion، DALL‑E و …
•
🛠️
بدون نیاز به ثبت‌نام یا حساب کاربری
🔗
لینک:
https://chromewebstore.google.com/detail/ImageToPrompt/pgabcjhpgdcgbflabemecpficpknnpfn
#OpenSource
#AI
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/archivetell/6283" target="_blank">📅 09:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP4HtIPDDrrSUhGghkl3SVy2gVrofum8PKLGMupjRc3JQD5xpDLbmvHB0qvuq8XWBle7qsQTup8wiEWGJcfK-k_U5QDHMpaCqeApJtG48-lFrw767NCRuzc_v9JPCFFLc5gwsT77Q2-g4yFMXtW8EjqQmYnQV40LFKaPMgUR2xh391N9ssXBdOyw2LhFB9oM83PjFEkT1RiMmNR5gsuMqBqwR7Rw-jJXmxhIQO4BXl3l62WLGmms5sPuiTz14VU6VmQunArS_G6GbjRTQs6Vy0CR4cyr9FBnnMlzc3oLEDFIFRTekLDgewhROMCRPGzPmZElYQafH_yXmjWgSYAPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتقال فایل سریع و پایدار بین دستگاه‌ها با قابلیت ادامه‌دادن پس از قطع
✨
قابلیت‌ها:
•
🔹
انتقال همزمان بین چند دستگاه
•
⚡
ادامه‌دادن خودکار پس از قطع ارتباط
•
🛠️
سازگاری با شبکه‌های پیچیده و متغیر
•
📦
انتقال تطبیقی برای بهینه‌سازی سرعت
🔗
https://shrimpsend.com
دانلود فایل مخصوص ویندوز ، مک و اندروید :
https://github.com/shrimpsend/shrimpsend/releases
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/archivetell/6282" target="_blank">📅 08:41 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
