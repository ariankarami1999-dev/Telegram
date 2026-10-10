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
<img src="https://cdn4.telesco.pe/file/rsn5PL8jX5SrPoOPSy3vfwsiGEtBLpnSTga31KVq543CMHyKAAoLV5jccpcjKXUXajWwxzZI0D7ferzTTt7vpGVrLbVU31q0My0KWOq0itmbzFPWsGySSiYpXhJG5RM4INwAYmOR4pT5KloyXCOGg5t4KOy-lPvAdzhUzVLY6DEbQJeO9nxNmuyEjppuiWEnhplw8UdrlG0tL_EyawbWxacVSpXyuOflK94QoQtycSYfiWy_M3ND-q9OfyzY8vWDSF8bmKfymwXdOcSCApR5E_NgHy4W4lUjnfRzXPeTopJSeRzztve_icMYnY8rSbLVNzaqWbjwTX3TIMZyqfFmEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-141284">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=r1H_RwZslAjye9o3xhFFEqnYyc066OyA1sBJN7f_gYREkGvZwijwsafWVcalI286xWZTgrYlMH74mv7z2jPM7LuwKuxm0lyWnugVsatcLMZv92Ceg-2F4AHiw3sXfW7lH1Q1DQpCOtMu9A2H-qNeVRc0fZWMy4xrM7fRvAeNv1K9aku52St9ec1mSIXY_BppdVPYPFymXcxxVqOeWqgvBY8GCDlbp9z9v7C9TOvsvz3uEF6CIX0zmj14TU0Kuc9zCK0mZ31t4xJ1xrcsoV78jAWPPBKOE-nC9qrYhxnceI1Gn5bE_QpoSvcVisyCX145DrX18nDykfSNnrMP9trpbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39e252ccf.mp4?token=r1H_RwZslAjye9o3xhFFEqnYyc066OyA1sBJN7f_gYREkGvZwijwsafWVcalI286xWZTgrYlMH74mv7z2jPM7LuwKuxm0lyWnugVsatcLMZv92Ceg-2F4AHiw3sXfW7lH1Q1DQpCOtMu9A2H-qNeVRc0fZWMy4xrM7fRvAeNv1K9aku52St9ec1mSIXY_BppdVPYPFymXcxxVqOeWqgvBY8GCDlbp9z9v7C9TOvsvz3uEF6CIX0zmj14TU0Kuc9zCK0mZ31t4xJ1xrcsoV78jAWPPBKOE-nC9qrYhxnceI1Gn5bE_QpoSvcVisyCX145DrX18nDykfSNnrMP9trpbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در پایان بازی پیکان و شمس آذر، رضا شکاری که پنالتی تیمش را خراب کرده بود، دل و دماغی برای خروج از زمین و رفتن به سمت رختکن نداشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 365 · <a href="https://t.me/SorkhTimes/141284" target="_blank">📅 20:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141283">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=hW33-HAdo44xRM4l977uEGBcEE-5cEgRb-QUDtdgUcGl2V9ubv2Q5R5JRD33FTppVa038UBBpBKl4T2RakiPc5ztct5ZcXJ0BW9r3e3ZttzKgO4cx1-JvL_kivDj3ntIUi3DT9gPeBWGrtO1kxM5Yt3stmX3WaNawOQ4gJRhgMku8nvers__jYkNMOLauToVNrjFE4RoWv8VdFVM3jP3T010UbgPibcj7S3nckWIhgCYOt01G2Mm_kWgdAMsUJAyyNU8xzRMeZhm3B7bjarJlr4RQLRl6FBtgMJWWO3RpgvXN2MrYsEiX7AbZQrZrsEh9pwM2JImQ72Ny_g4IVAdWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b96d408ed.mp4?token=hW33-HAdo44xRM4l977uEGBcEE-5cEgRb-QUDtdgUcGl2V9ubv2Q5R5JRD33FTppVa038UBBpBKl4T2RakiPc5ztct5ZcXJ0BW9r3e3ZttzKgO4cx1-JvL_kivDj3ntIUi3DT9gPeBWGrtO1kxM5Yt3stmX3WaNawOQ4gJRhgMku8nvers__jYkNMOLauToVNrjFE4RoWv8VdFVM3jP3T010UbgPibcj7S3nckWIhgCYOt01G2Mm_kWgdAMsUJAyyNU8xzRMeZhm3B7bjarJlr4RQLRl6FBtgMJWWO3RpgvXN2MrYsEiX7AbZQrZrsEh9pwM2JImQ72Ny_g4IVAdWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساکت الهامی به بازیکن تیمش اینطوری سیلی زد
‼️
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/SorkhTimes/141283" target="_blank">📅 20:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141282">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRzK_j_JYPyIgKVG6ucdmjdTx5i4uEHkhgp0tobOHy7yMiotqXOEwRxegF4mdx3l14q8UsehOI0JkgZaC5bfZ8zqeyR6ytwGVGz05qKV1gqTGh3fAJofkCHNY7TxCGaqcNB5114kXqcmUm72WqSXiuPMWMU4o0u3MmSlRJrGSI9ZdK1lVEQX-9qZWDLZJAmE_RUVAUNOUE7nw_ll5wxRmrRb80rO4JvITKG9hw_fnYzL9z1z9UH7U5ktg7YLa2JrClBcGSZPnG9DbmiXq1RXS_NC8OUXC9bUX2AqoJMmf9mtbWrNhPN7z3pFPdPGE6Xg_t7gU6BAjPaQwfsv-MXMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Real Madrid
🆚
🟡
Villarreal
⏰
Tonight 22:30
🏟
Estadio Bernabéu
🟠
رئال مادرید در ۷ بازی ابتدایی لالیگا ۱۸ گل زده و فقط ۸ گل دریافت کرده؛ میانگین ۲.۵۷ گل زده در هر بازی نشان‌دهنده قدرت هجومی بالای این تیم است. ویارئال نیز با ۱۳ گل زده و ۱۲ گل خورده، توان هجومی خوبی دارد اما در خط دفاع آسیب‌پذیرتر است. باتوجه به میزبانی رئال در برنابئو و اختلاف کیفیت دفاعی دو تیم، برتری رئال و احتمال گل‌زنی هر دو تیم از سناریوهای قابل بررسی این مسابقه است؛ البته پرسینگ و مالکیت بالای ویارئال می‌تواند بازی را رقابتی کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/SorkhTimes/141282" target="_blank">📅 20:53 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141281">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 856 · <a href="https://t.me/SorkhTimes/141281" target="_blank">📅 20:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141280">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
به تمام دیتاسنترها آماده باش داده شده تا در صورت وقوع جنگ٫ اینترنت سراسری قطع شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/141280" target="_blank">📅 20:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141279">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
🔴
🔴
محسن ربیع‌خواه مهمان ویژه برنامه تلویزیون باشگاه پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/141279" target="_blank">📅 19:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141278">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
پویا اسمی که در بازی دیروز برای تیم بزرگسالان پرسپولیس به میدان رفت، امروزم در بازی مقابل جوانان استقلال فیکس بازی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SorkhTimes/141278" target="_blank">📅 19:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141277">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
تیم پرسپولیس از دقایقی دیگر در دیداری دوستانه با بازیکنان ذخیره خود به مصاف فولاد هرمزگان می‌رود.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/141277" target="_blank">📅 17:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141276">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c_8jI33lRQ_tx0Fhi3S1YAjyM0lnG-3B9bkJWxz_5BpLnntJDSviNwJx31QaZLWjOgwC7LP3VmVL9QM5CRgt7aaDh-_Mhg6XAZwSPmhnJMdw06FmfAaL5t58NCaS_AVWCKXhv5T-eSga7VhRY0Zx05ZyUADwJ7SckiR2CP16uaip6kO9LqamtVv7V6KNIgIGfkKDTc_m2n9OtYRm9qmme1LLan2LvgCh9pCPhk1PdIqjPjr49wFz1ipmcUOl5UNzX30FRv4oYCVnEttu12onbLNxNwn2J13brW_TA38ismoLmUi6uAEdLI5oO1PUmfaaD33sSeIFZW_oFvKzO8DbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
#جنگ_کفتارها
🚨
محمدرضا زنوزی مالک تراکتور به تمامی ارکان باشگاه دستور داده  که هر کسی با بیرانوند در ارتباط هست فورا  قطع ارتباط کند!
🚨
به گزارش فارس امروز یکی از اقوام  بیرانوند که در مجموعه زنوزی مشغول کار بود به محل کارش راه ندادن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/141276" target="_blank">📅 17:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141275">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/141275" target="_blank">📅 17:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141274">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/141274" target="_blank">📅 17:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141273">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7P_aFNm1hEu71gokCLQsGxKxLZ9wYYLtHcEeHiaxiJtv7aYEfVVqPnkiJVhLuB3pp2oKRjrjoIdnhxl5H7aRnhiIaJTQidpWA19q8w4bGZgl4ZIwL8mtOW8Pa0WfN12Uo456Lh8vUbwke3ZlkMpphMHQU8GJXDpG1L70gvgwTIOpe9k5V1bqjz24CDK-oOPex1jAKtZBCQh8qZ1Iup_wnb_ZA6N4HJG6Ejtd3GcZRoBzwkiqHqLB2UzUTCU2bhgjYsuG00kWATsmBFnUZhrM07YCqDyqNAuK3hWljgpOrOTpqxi4pZ6IHJ42Pbq0_OAchpLmD9x7s7o-u6ETBS-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ارونوف با ۱۶ گل، دومین گلزن خارجی تاریخ پرسپولیس شد؛ فقط ۴ گل تا شکستن رکورد گولسیانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/141273" target="_blank">📅 16:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141272">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/141272" target="_blank">📅 16:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141271">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/141271" target="_blank">📅 16:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141270">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/141270" target="_blank">📅 16:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141269">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=eEsCxBUd0ZybbFmQ51YyC_Jb-JJ_GNfQ2FOYgyFdDgompiacLyPnmvXcjWq3FMEMVMaNhobIEoJxxaSgK5YrIaQzR5wNMOXoixNHJwTEBrOHRREeiJV5QiU4cpEVEiXZzqmRkkWkuIwU3Io2c_2rdIBmRHdE7EUotDJ1XksgvU6ulplthxyzui5LL8YIrA0zRLnHQeG2gQ6WwH-8XGg37F0aqw-1ZTeUX2P1YfboIp8JXE2GuztNDFlX176fOWQwX8RW5eOtJf6Tv04uUCQRk95DI466dvBfmD6Kk552aty200gFxPRua-PytApMiUa0alQ_4Yfvx7u3lMDsbJuqbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f241a3512.mp4?token=eEsCxBUd0ZybbFmQ51YyC_Jb-JJ_GNfQ2FOYgyFdDgompiacLyPnmvXcjWq3FMEMVMaNhobIEoJxxaSgK5YrIaQzR5wNMOXoixNHJwTEBrOHRREeiJV5QiU4cpEVEiXZzqmRkkWkuIwU3Io2c_2rdIBmRHdE7EUotDJ1XksgvU6ulplthxyzui5LL8YIrA0zRLnHQeG2gQ6WwH-8XGg37F0aqw-1ZTeUX2P1YfboIp8JXE2GuztNDFlX176fOWQwX8RW5eOtJf6Tv04uUCQRk95DI466dvBfmD6Kk552aty200gFxPRua-PytApMiUa0alQ_4Yfvx7u3lMDsbJuqbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
ضدحمله زیبا رو ببینید
🔥
🔥
🔥
❌
با ٣ پاسِ تک‌ضرب و پاس‌ تو عمقِ زیبای محبی به بیفوما تک‌به‌تک میشه اما حیف که این کارِ تیمی با گل تموم نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/141269" target="_blank">📅 15:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141268">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw56z-pkpPbutR-ciBQ7ldycfTjCXjWG9Z-htVta3sMaqyqtcs6rxKd0Pe4dqtLFdyXrPZcTRheAVX7GE0KbKQvzp0UyqgUyJUKFdVmpDZMMKXlHLsjr9MBCfB89WB4mjPip5xBgWE0zLoI8tnb2jRbobQkTAJgQMP8NAv6yc1RtECEwhhaEGlcaNQj4QAJ5icFbi93zIjubEHYV4-mvpgV-WWCbGTJXt_jevVHCsTPian5GB5NnX2eIyztpz-kvx27ytiR-4JAKTovwjZu8M_dcmP3adKNJ59M6EXzmRpTn3D9cmp5-GmnsFP7Zyc_fpk4MWdbx_s3-aFprK-4Kow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوووووووووری / مهر
❌
محکومیت استقلال در پرونده‌ی آسانی قطعی است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/141268" target="_blank">📅 15:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141267">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=umEPn-TFbhh70uUjjFArDc6uXPFp3NOJuYKc5FSHpVOlXWU7jP6fopH6kxwj3fe14cfizDGaGwONqPi7fQoIC7euY_Vu6_2sq8ddJIkMOapOM8bao2sCyoWvssdSVbkp6t7ClgqjkUeCIQmvoTa3yDKg3gR_YekcHIoKmMJqO0jWs8muNxs5MzW72NWjQpeliO4W7MKbmnX5-79RAEX1Fu0BJZ2nLpIrOFKDZPKh3d1-oWe2NW1xpI3gyusEjq8XfodVymnt09xx1fMMiVR_g8Dyewub75fzPHfTySDfwtjl9Fsyv3mWz4j0UJbY8Ff5tDk-zYYvdwVdmlRdvvvfCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4727e2d06d.mp4?token=umEPn-TFbhh70uUjjFArDc6uXPFp3NOJuYKc5FSHpVOlXWU7jP6fopH6kxwj3fe14cfizDGaGwONqPi7fQoIC7euY_Vu6_2sq8ddJIkMOapOM8bao2sCyoWvssdSVbkp6t7ClgqjkUeCIQmvoTa3yDKg3gR_YekcHIoKmMJqO0jWs8muNxs5MzW72NWjQpeliO4W7MKbmnX5-79RAEX1Fu0BJZ2nLpIrOFKDZPKh3d1-oWe2NW1xpI3gyusEjq8XfodVymnt09xx1fMMiVR_g8Dyewub75fzPHfTySDfwtjl9Fsyv3mWz4j0UJbY8Ff5tDk-zYYvdwVdmlRdvvvfCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیفوما و آن فرارهای همیشگی‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/141267" target="_blank">📅 15:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141266">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
گویا پویا اسمی که امروز به میدان رفت و جوانترین بازیکن تاریخ باشگاه شد یکی از بازیکنان مورد علاقه تارتار هستش و شدیدا بهش علاقه داره و بهش قول داده که بهش بازی بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/141266" target="_blank">📅 15:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141265">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
این وسط شله زرد هم فجر و شش تایی کرد ..رسول خطیبی ی تنه فجرو نابود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/141265" target="_blank">📅 15:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141264">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
فووووووری
🔴
باشگاه پرسپولیس وویس هایی از ایجنت یاسر آسانی داره که به پرسپولیس گفته آسانی بازیکن آزاد هست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/141264" target="_blank">📅 15:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141263">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOf3ez5il9TVOk2uAFc5oJJbs_V9pO4O-LM6Qk7Y6QmX_hBWeDy0mPNeHn2-2skAyc8GTcuPLNV5co25aXdRPQevPV_vs91yee_ISwEofckIdYkxsoNuWO2beq5LgH0SpT3iv3Q4yhKSMPwoQOaT216ILqEBWuf6frnhEp1yP8gJ0VVzjxlNXMlVv8xA-Vljz05ysaiE_spqSmq2fKROJLme830C59Rhb6WSCfgO1X0PADMzaWPPFblIhFn8IyIedU1GrcEjBAh_mZbrLmeJ4GuojNrfaxDSr9oDDHh1AZQEJEJ7qmyeT1-S5PlXpPS3mdSby1nDo1wox4U6BLRamw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
نبرد حیثیتی در لیگ برتر؛ شیاطین سرخ مقابل تاتنهام، جدالی برای اثبات قدرت و تثبیت جایگاه!
[
منچستریونایتد
🔴
🆚
⚪️
ت
اتنهام
]
⚽️
منچستریونایتد با تکیه بر امتیاز میزبانی و قدرت در انتقال سریع توپ، به‌دنبال ضربه‌زدن به فضای پشت خط دفاع تاتنهام است. تاتنهام با پرسینگ و بازی مستقیم می‌تواند موقعیت‌های خطرناکی خلق کند، اما فضای خالی پشت مدافعانش نقطه‌ضعف مهمی خواهد بود.
سناریوی آماری محتمل: بازی پرموقعیت با شانس گلزنی هر دو تیم؛ نتیجه نهایی تا حد زیادی به کیفیت استفاده از موقعیت‌ها بستگی دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/141263" target="_blank">📅 14:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141262">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
✅
🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مهدی تاج غیرقانونی بودن قرارداد یاسر آسانی با استقلال رو یادآوری کرد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141262" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141261">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvUJuNihIG5x9MeGf5XPDb6eyt5MRJRUXRk2ebgSt7Mcky5VKb_xhlP84vkzb4Xduur-GbKe-bDtjRMQIitKVKRXpc3rJvunPu1iPc1QULpn2izos_jOH32HczHyyOgKLRQIkRMU3gZNnACV05Y6Z4vBe-uJmrExN16JldhUaupVswwNoRcU6xuFDCU-7P1vMAMGb5ZF2Dl_8p6dxoDi0KZE02n8vst7u1kNA0CgbrV8cA-WzwbnZZLPQa3AzEftXzw5lkGA2xdau9_waN4yz4BDzITSghpZvPlQkAp0-PA3mKmrPd3weJurVXKCi9z_Lm2aC_AEgCoxOSSHHte32A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
پرسپولیس با ۱۵ گلِ زده، بهترین خط حمله لیگ برتر را در اختیار دارد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141261" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141260">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141260" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141259">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭕️
تیوی‌بیفوما وینگر33ساله پرسپولیس با نمره 7.8 بهترین‌بازیکن‌دیدار امشب‌سرخ‌ها برابر نفت شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/141259" target="_blank">📅 12:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141258">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA1RTBV5QQoMlgNlUpZ_FZ_HuaSeje0aSHBIyt1xLuAAhDKFAE1EuO-K_o9tgBejIjWFCCetfzUaQG0wewqFAQjwu3CaxOiPOowLlREiL1xBDYh-WqmssnbhkFpXYJ86ElrHlOLdr08YrhZkG404HrPdVTlx3itVjrWAPPRKyRVyZz0WTbOsaPN4seVLFS_3QVqGEJZwP0YGkYP2mOAHXmZ19UejQNCRITjet0IgZpDgoQP6VRLutbFfwbrL1Ao5-hqEHxtlIRXFJniOQj109eL7NvC9Q-L_TS8MUOKKAh_3LMkavKhE2UZFzEf9qWG87hu6Wi1fVhIEsQX6Omu9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/141258" target="_blank">📅 12:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141257">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🔴
◀️
مجوز خارج شدن امتیاز باشگاه پادیاب خلخال از استان صادر نشده و باشگاه پرسپولیس برای خرید امتیاز این باشگاه با مانع روبرو شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141257" target="_blank">📅 10:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141256">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/141256" target="_blank">📅 10:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141255">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/141255" target="_blank">📅 10:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141254">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a373367fda.mp4?token=sJE0tKBkQXg4uD_5o6A6KDlr9ZAV0BA-IgvClZp2gF6RttzMMvrwyD5hK1B2Iu29pFh2c-_DvqEGtSFROB_jio9SEFbby2G3jdGur2Rb31J2BIlbH5Ji7RTTVPzxZN6h2zBFyyfy2LgCytvVU_JxMhObpM1-a1OQnj_lgzkTfGp1y5brWivVBC0BM7Ui8SHckvql3t7e1_GTnxJrdi6WF5ApKxubwejFZKEp59Cr4fTdb1-4vgB9lxIAsKMQXWCFq1B9DtoliSkQsiWB-jVuGzAyQ4I02Q0Q9medDQLI09KQ1DzWQG_fuozIBr1UCIp1GoB6DUV62bbOrvtOWeWCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a373367fda.mp4?token=sJE0tKBkQXg4uD_5o6A6KDlr9ZAV0BA-IgvClZp2gF6RttzMMvrwyD5hK1B2Iu29pFh2c-_DvqEGtSFROB_jio9SEFbby2G3jdGur2Rb31J2BIlbH5Ji7RTTVPzxZN6h2zBFyyfy2LgCytvVU_JxMhObpM1-a1OQnj_lgzkTfGp1y5brWivVBC0BM7Ui8SHckvql3t7e1_GTnxJrdi6WF5ApKxubwejFZKEp59Cr4fTdb1-4vgB9lxIAsKMQXWCFq1B9DtoliSkQsiWB-jVuGzAyQ4I02Q0Q9medDQLI09KQ1DzWQG_fuozIBr1UCIp1GoB6DUV62bbOrvtOWeWCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آنالیز محمد تقوی از بازی پرسپولیس-صنعت‌نفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/141254" target="_blank">📅 10:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141253">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141253" target="_blank">📅 09:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141252">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141252" target="_blank">📅 09:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141251">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
پویا اسمی که متولد 1 شهریور سال 1388 میباشد به جوان ترین بازیکن پرسپولیس در تاریخ لیگ برتر با 17 سال و 1 ماه و 16 روز سن تبدیل شد.
🛍
پیش از او این رکورد در اختیار احسان خرسندی مهاجم پرورش‌یافته آکادمی پرسپولیس بود که در 29 اردیبهشت 1381 در دیدار…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/141251" target="_blank">📅 09:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141250">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141250" target="_blank">📅 09:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141249">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141249" target="_blank">📅 08:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141248">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و 16 امتیازی شدیم با یک بازی کمتر و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141248" target="_blank">📅 08:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141247">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMIeEPKHVL4ZDJ0-fswROKM1rfCdpOAPIvu7vQ7oQGT-6YuPfDoa0fMgAfYHaCAQky4FvPAZb3T06aPUMZxOmr7byxuVkSwTzDLvP1m4ynhUXCAUkaZFFHc2So316SxQeGY8McTg8xSDW0ekj2A8zQbva1xtefQYKGw0BGNaQPOmSr0IoY0L76a8V7vXF7eo7JD1CPOSliWmQNXXhsLIx7UyBtk9xBvQuZJDL4wtbXpVxi-dtqJJO86Wd0qB8ArlzB0ctLtBRLlXcW7wdUB6l9y0PvFq6AOS1dnqf3EEI7Tkh6RBuCnF9FPVcZ4Rymj9DHZpmrzEBalc0FGuisdmhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141247" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141246">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141246" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141245">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🏅
صحبت‌های جنجالی احمد گوهری درباره دلیل جدایی از پیکان: سرمربی فصل گذشته پیکان به جادوگری اعتقاد دارد!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141245" target="_blank">📅 01:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141244">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
فووووووری؛ سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکی‌اش حق خروج از کشور را ندارد و ممنوع الخروج شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/141244" target="_blank">📅 23:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141243">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
#فوری/بیرانوند با دستور نظام وظیفه ممنوع الخروج است و امروز هم مجوز تمرین نداشته.
🚨
کریمی و نکونام می دانستند بیرانوند حق خروج ندارد و برای خوشایند زنوزی اخراجش کردند.
🚨
اکنون هم می خواهند سر هواداران را گرم کنند و به رسانه ها می گویند مشکل حل شده و به…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141243" target="_blank">📅 23:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141242">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diYURjpD1D14uT0Q--CKZBa9mvKmVTilq4foL0yv9CyUZGOsgZztJi6BTRj6N3kebPx-LC29CrVHRB476nQAn8DuqKzIqUSNQ1YWMtzwi2BOiOSRp5bh97uytEv_uZHoPA1fS9Y6WYdZLzwKWKzWThbqAC9h8ZtF5POi83CAHGpVit6egmKzhTQwnOmk-o0dLvRr4p_Lhfbar_PsTXjA2P76Zl-VDf0-vBA2RVcPG2-0XUvjJ6RNvvc-rk2JqYApP_G5-xFMG_lBmCgQE5WLkAUhDTDkXW8BCwRevvviMJrWRL5Gc0JcvcZt2WkOyDViVnHShPd74dtie3Kxewoglg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوستون اورونوف با گلزنی مقابل صنعت نفت به دومین گلزن خارجی برتر تاریخ پرسپولیس تبدیل شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/141242" target="_blank">📅 23:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141241">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!  علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/141241" target="_blank">📅 23:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141240">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkQgu42Syr2XpMWMVMsGw0T0VDm9JIeMn3xJ-6e7qoHheDXPBSNFEzjaazCminb_isCUDMAHwkFzgo1hp7YC05VsXdLh8UwQbuRaRoHLuN3rs2XloblS6mwrvm0GDaMyqOVaqcymhkRlto-qK0LIDLsfjU9nZ-khn-Du1jEoDgX1_wravuNawN6wEgpxeMFVaYbkObUjHuybxH2htS6LcYY0z-qG0s4ppV24TiGpIzRnPZdis6DAZLm2FhSKfu7-biAYK-nX2r8rzHjLJKqptwv_2lbgVcfhzb8CL4x80J4pYqGga7YrOZ8P6woJ1yjLmtw5i3atcxS0tszMsraYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
❌
محمد نوری پس از شکست مقابل پرسپولیس به صورت توافقی از صنعت نفت آبادان جدا شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141240" target="_blank">📅 23:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141239">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=jxTsn8_io4g58J3oGac1ADkO7-zqlIPCpLAa7m6NdGEprr3493A-vDxrHFMOFEZdzNst0gHz39egUrLoWISpLlCOGuNNwMCPdGn07snCeJBya3wHediiUPYqHXQo8QfpdxjxvqWIDkOyqHgJZRnIJSXR8QctvJ_1w957r-TP_tuEYMKJRv8abOodDY2mrqWq13kioELnfeHDc-Y4q7LolRbm2HhvDFqny4c2Gqm54bZmZFw1IZW7uDlx_iU8nJ_4PWO-0l2pzxPTfxFY2J7zOg_mhS9PULBGW_faJRVQP7v9tbm1Bm9Ts4ahN75itEoO7QjJEma8SF1doCG5dVU0rj8WtdoG__jXy5GKrMNCovgqliSsFdXDYD3Av8ZymbBNcNHcMFr3damBzAReHUGIwsNiPHsU7wRM2za8DtNk1SzdHCOKnCvkBSWczhr0hWPicfL7rxY6fBqWNeXngEAmjYIAx4KtEJc_whlWfTxed8dO06Ar2qVc6MHgZ-4QzIKdjhsn2leoqKg50qBV89AT7H15vTXWw6GyvitMdsStJryr5_lZzZvuaqMmYrEa55m3yQ-z-CgUZd2RIJ--tSM0Xes4v1JvADSn20bA4kXdKDmfuuctzSWKaFJcljjXLrQmgeLJxGidfTNxT_OaUmfPRxfLmfC_xMUCkSSVqTQijvk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ce1b9f2c.mp4?token=jxTsn8_io4g58J3oGac1ADkO7-zqlIPCpLAa7m6NdGEprr3493A-vDxrHFMOFEZdzNst0gHz39egUrLoWISpLlCOGuNNwMCPdGn07snCeJBya3wHediiUPYqHXQo8QfpdxjxvqWIDkOyqHgJZRnIJSXR8QctvJ_1w957r-TP_tuEYMKJRv8abOodDY2mrqWq13kioELnfeHDc-Y4q7LolRbm2HhvDFqny4c2Gqm54bZmZFw1IZW7uDlx_iU8nJ_4PWO-0l2pzxPTfxFY2J7zOg_mhS9PULBGW_faJRVQP7v9tbm1Bm9Ts4ahN75itEoO7QjJEma8SF1doCG5dVU0rj8WtdoG__jXy5GKrMNCovgqliSsFdXDYD3Av8ZymbBNcNHcMFr3damBzAReHUGIwsNiPHsU7wRM2za8DtNk1SzdHCOKnCvkBSWczhr0hWPicfL7rxY6fBqWNeXngEAmjYIAx4KtEJc_whlWfTxed8dO06Ar2qVc6MHgZ-4QzIKdjhsn2leoqKg50qBV89AT7H15vTXWw6GyvitMdsStJryr5_lZzZvuaqMmYrEa55m3yQ-z-CgUZd2RIJ--tSM0Xes4v1JvADSn20bA4kXdKDmfuuctzSWKaFJcljjXLrQmgeLJxGidfTNxT_OaUmfPRxfLmfC_xMUCkSSVqTQijvk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
⚪️
⚽️
تاج: با یحیی گل‌محمدی برای هدایت تیم ملی امید به توافقاتی رسیده‌ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141239" target="_blank">📅 23:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141238">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
✅
تاج : آزادی تا 2028 باید مسقف بشه، وگرنه دیگه اجازه میزبانی نمیدن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141238" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141237">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=hMDaVQCA6LeV8ZdcZjQn2A-juz7qyVYuGk14j_3WbxVnSkZwf0LpnOSn5CAXy6x86hSjM-A--bhnSh5L1awTPPDNSUPeHzUsulJVAzshqT2h_up9_Rh3kmDu9DQ14tdy53Hvtfqayu-TDSqFa8fiMpM76u6YeXoImX641GTZSVu3O7Xx3qjRTB8_N-8vw8d10jbqgXy8mrQ9EpvTmRA7OVH0Fs2iUJl2RrCUqdX35s_DlM6YAcywyWGAwNWtBZ0lLdc136f6mBwzODpZs_laBe821ltMEJ1hxy8yshzcoND7YZTSRvRrBqMWNX7b0dDi3Q5GzI-oZRPtfLwUlya-iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fbe6664d.mp4?token=hMDaVQCA6LeV8ZdcZjQn2A-juz7qyVYuGk14j_3WbxVnSkZwf0LpnOSn5CAXy6x86hSjM-A--bhnSh5L1awTPPDNSUPeHzUsulJVAzshqT2h_up9_Rh3kmDu9DQ14tdy53Hvtfqayu-TDSqFa8fiMpM76u6YeXoImX641GTZSVu3O7Xx3qjRTB8_N-8vw8d10jbqgXy8mrQ9EpvTmRA7OVH0Fs2iUJl2RrCUqdX35s_DlM6YAcywyWGAwNWtBZ0lLdc136f6mBwzODpZs_laBe821ltMEJ1hxy8yshzcoND7YZTSRvRrBqMWNX7b0dDi3Q5GzI-oZRPtfLwUlya-iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در اتفاقی غیرمنتظره پس از پایان دیدار با صنعت نفت، تعدادی از هواداران پرسپولیس با قرار دادن موانعی از جمله لاستیک خودرو در مسیر اتوبوس این تیم، مانع از حرکت آن شدند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/141237" target="_blank">📅 23:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141236">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7CEAz0DOJKMSnIjgsvQDsPsyVQXFOFwHpCqjIqVotIo_MgdZMv9cekzVD8qjfiq5t3FamAkCcWiyNOYMLTB4BhpLolVqeddLXgPgynbodYRT-hBZaujAqNUvy8apJjny6SQggZCw0GfQ7Yzz8y7-pTzYBaoF_T-eGCde8Qy54WVQysoIt7XlOKTUi4jwHexm3Pc3hdL0jCEbifA3k8m_HMZD0_PnWimmjWeMwGIzrO6D3TSnKOtEf7slf-p3Hvkw7fCG1Ngu5AD6ttFOr5OELW-UEJ906lRrfvWsPMtf-ydq067MNJuXzc6shBuF11fb7N3Pu6msvztAFyh9biggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
منفوری بیرانوند ادامه داره
🚨
فوری؛ بیرانوند از هتل هم  اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/141236" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141235">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=VcGrjn0-pZK5Hwk7oGZNtG-y1uV8yP68L9n3NKrgzNlcgg0fazLAGEDhB_gZRzxnh0ry8qbB33QmnArX_wRA6wfT6DAoWG1LjRvViaLeBqN5WL12JXdu8sDqxgKCdXB9QDKoRzlwY_adqJE0Eo4nKga1GGFHZ29hUB6qChWd7-WU3AP7VS6b-7KxVtX3jzZM6Wq4_K8koa-DVd2FQ1C4okWY9pn3iIEqcMG5TI8ivR5TcHUrcFgHDi74Cpo7nfnLTuZArWXN_VSd4nd7kFk92_fOAVzWsM2zQhevP7pAcXCQGx0GiffIc6Uwve4gDWgwifaalMDlDTgefEauwVjnjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37a5e6308.mp4?token=VcGrjn0-pZK5Hwk7oGZNtG-y1uV8yP68L9n3NKrgzNlcgg0fazLAGEDhB_gZRzxnh0ry8qbB33QmnArX_wRA6wfT6DAoWG1LjRvViaLeBqN5WL12JXdu8sDqxgKCdXB9QDKoRzlwY_adqJE0Eo4nKga1GGFHZ29hUB6qChWd7-WU3AP7VS6b-7KxVtX3jzZM6Wq4_K8koa-DVd2FQ1C4okWY9pn3iIEqcMG5TI8ivR5TcHUrcFgHDi74Cpo7nfnLTuZArWXN_VSd4nd7kFk92_fOAVzWsM2zQhevP7pAcXCQGx0GiffIc6Uwve4gDWgwifaalMDlDTgefEauwVjnjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
❤️
فووووووووری ؛ بیرانوند رفته هتل محل اردوی بازیکنان تراکتور ولی توسط نگهبان هتل راه ندادنش و گفتند سیکتیر
😂
😂
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/141235" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141234">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=rN8_aoGKsB1ETArmVAYPWtMkTHoHUACijRv4OP7MBlaysNLt9Q2JT84Rbqrqsda1DZ4S64XaFC9sWLH7rJVOXt9h-e5820dAgDXG0mq6AYQOp1QKbQm2PHpl2iPS11kUMv6IIQDF4azpMDXkxuf5oN8bvcSbHQtlbSFZn3aS16skbwCs4xku364NoMt_FcXV8W0FDy2TFadLHyj3aK0B0Z9X_0XH-NVqJBDClpbVpWHmNt6_gMI7XlUbP_r4CJwRgI7FfGdhk2hpNAtNmpfTf17RdwuwdkCVgVF-QDyw0GOIjvpThykCdLdNf2PxNoaWsq3EtCe_vsoF7DJqzhcGNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc26b95b5.mp4?token=rN8_aoGKsB1ETArmVAYPWtMkTHoHUACijRv4OP7MBlaysNLt9Q2JT84Rbqrqsda1DZ4S64XaFC9sWLH7rJVOXt9h-e5820dAgDXG0mq6AYQOp1QKbQm2PHpl2iPS11kUMv6IIQDF4azpMDXkxuf5oN8bvcSbHQtlbSFZn3aS16skbwCs4xku364NoMt_FcXV8W0FDy2TFadLHyj3aK0B0Z9X_0XH-NVqJBDClpbVpWHmNt6_gMI7XlUbP_r4CJwRgI7FfGdhk2hpNAtNmpfTf17RdwuwdkCVgVF-QDyw0GOIjvpThykCdLdNf2PxNoaWsq3EtCe_vsoF7DJqzhcGNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اتوبوس تیم ابوالفضل جلالیو جا گذاشته تو ورزشگاه
😐
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/141234" target="_blank">📅 22:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141233">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✔️
#فوری | شنیده شدن صدای چندین انفجار در شرق بندرعباس و اطراف قشم منشا صدا مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/141233" target="_blank">📅 21:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141232">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه چیز را در این زمینه نشان می دهد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/141232" target="_blank">📅 21:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141231">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
تارتار:
🔴
به خاطر گلی که خوردیم و موقعیت‌هایی که از دست دادیم ناراحتم
🔴
از شادی هواداران پرسپولیس خوشحالم؛ آنها همیشه باید خوشحال باشند
🔴
همه بازیکنان از کیفیت چمن استادیوم شهر قدس گلایه داشتند
🔴
از مسئولین کشور می‌خواهم ورزشگاه آزادی را هرچه زودتر آماده…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/141231" target="_blank">📅 20:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141230">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de5Vx1doW_e34rQRuEtYfZz39m0moByiDOt3ms1ooF-W8St-LUrsnXQNHPqKSLakJ_zVFyiE_W3ezW0HZdqPjQdM8Rjo3sTJBRXNunIv-Nx5_v5E8Jof7GYf2uJ4DXjF3zXRVxtVVcF3DidjDgQtsJHL4J_PPYZuuJe6_sym2q0D9RTDev3FyzNCQle8Txn5BqANiKIejnAtN9gAei8BOkiTAQfYq7jLcYqr-ZgAPBryYmP6QIUMnZu8ZXJZ8wcQp2Ym0CF2spDahUXJ5jh4VGQcYM5gHK30hQN1wqCyoPf5P84kRDS4nxetFHTXskL-wir4tVt2VcZHqKZU6wxNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرخپوشان پس از کسب پیروزی، جشن خود را با هواداران تقسیم کردند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/141230" target="_blank">📅 20:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141229">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-3VDWbbu2eiW-GJJ7nVbajEPsQQVfiioyFQYKUaGhgJZFIawop_QuAa_w8-Ub1InWKPvfUKOC9D8xxUQJzqM4Yr9hJ3l_IAc9016veLXVeb2jjB8xb9NJVgZOFb_9I_5leqfz18TtMuszr0f2b8CEIBzPi--ooTkGa3KHygNloQHpfDyx_JF8h5kFtoNU3CvM0FEqF6vzu3UKtQxU4bvZIPk-HhmhASEtSVUkZYpH7NmXkBJkkQheEzQfzkviYirT5Vn9umntqh-sCb_4PxXXhRFXLC8hV3Xd0_EmfU5fS21wGf0cOJycjSVoGEqhnIAO7ff0gRXOlAm6Rkoivnyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زنبورها در کمین سه امتیاز؛ وردربرمن آماده شوک در خانه دورتموند!
🔥
⚡️
[
دورتموند
🟡
🆚
🟢
وردربرمن
]
⚽️
دورتموند با ۱۲ امتیاز و آمار ۹ گل زده و تنها ۲ گل خورده در ۴ هفته، برتری آماری محسوسی نسبت به وردربرمن دارد که ۸ گل زده و ۸ گل دریافت کرده است. دورتموند در ۷ تقابل اخیر مقابل برمن شکست نخورده و با توجه به فرم هجومی میزبان، شانس بیشتری برای تسلط بر بازی دارد.
سناریوی محتمل: برد دورتموند؛ هرچند برمن با توجه به قدرت گل‌زنی‌اش می‌تواند برای خط دفاع دورتموند دردسرساز شود.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141229" target="_blank">📅 20:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141228">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141228" target="_blank">📅 20:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141227">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🎤
🔴
علی بازگشا: اسناد کامل و جدیدی درباره پرونده آسانی به کمیته استیناف ارسال کردیم
🔹
امیدوارم این پرونده در داخل کشور حل شود/ اقدامات قانونی را در داخل کشور انجام دادیم و اسناد جدیدی خدمت کمیته استیناف ارسال کردیم/ امیدواریم این اسناد جدید و مهم که تا به حال به این ارکان ارجاع داده نشده موثر باشد و رای جدیدی دهند/ تمام تلاشمان این است که موضوع در داخل کشور حل شود چون احترام به ارکان قضایی کشور است/ نامه‌ای را روز گذشته به فدراسیون ارسال کردیم و ادله ما شفاف است/ چیزی که از فدراسیون می‌خواهیم اجرای قانون است نه مصلحت اندیشی/ قانون منع مصلحت نیست/ تاثیرگذاری یک بازیکن غیرمجاز می تواند نظم جدول را برهم بزند و به بقیه تیم‌ها ظلم‌ شود/ پاسخگوی هوادار و سهامدار باشگاه هستیم/ ما مندیت آسانی را در آن تاریخ دریافت کردیم/ باید رای قاطع و جذاب صادر شود/ کسی تماسی نگرفته که این موضوع پیگیری نشود/ اسناد مختلف از جاهای مختلف رسیده است/ اگر نتیجه دربی به نفع ما شود دیگر طبیعتا در کاس پیگیری نمی‌کنیم ولی ما درباره این موضوع صحبتی نکرده ایم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141227" target="_blank">📅 20:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
پیام نیازمند: بازیای بعد فیفادی همیشه سخته/ تا جام ملت‌ها خیلی مونده و تمام تمرکزم روی موفقیت پرسپولیسه/ کاپیتانی پرسپولیس برام افتخاره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141226" target="_blank">📅 20:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
✅
پیام نیازمند برای اولین بار در طی حضورش در پرسپولیس به عنوان کاپیتان کارش را آغاز خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141225" target="_blank">📅 20:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141224">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141224" target="_blank">📅 19:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141223">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHkE6ARvCzJqf-SA2UJ4ECRIBYKktXwnmSTMgk2_WQrFrIucKN51mGfZfCCdamTPnDKxyqSLWwgoJzaHlK9sBRNyvjfQhF9Q3UmmBzXvsGHWv-VY0Jw6yp9NRuNG8JOGDBZNPN29XppcEkWVzXDPGc_Tx9dwrQST00M_a0t7FTGnitQwebRNH3QnskDrfvqULiPkKmejjUZnWY3ff8f_gUl_NKptsn8pusAwb7N3cmpcXtgpehhpriX5bQNjbPpdmy06vD0i6NpS_gOvNNVCulGOTaHSTXDZB-HgnZ2RdyV5mgDRBS4Myzc3ghAE8lZKnFl-s8oGObPChoB37BBzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
جدول لیگ‌برتر پس از بازی‌های امروز
🚨
پرسپولیس با برد مقابل خیبر در بازی معوقه، به صدر جدول میره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/141223" target="_blank">📅 19:22 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141222">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/141222" target="_blank">📅 19:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141221">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/141221" target="_blank">📅 19:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141220">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a74657a541.mp4?token=edpXFRBr-WQMKGdl9Om9CsQgarYugOvmVLAjfs3UZulmmqK-3FnksA8ZSCeVWa0dBVr7zsoaU44CotjJ0dVLBYjam9XiscQtbv_7_ufspzLrwfgHgh4ibpJ14knTSC--DqZMH96z3rPgGyLQb6Li4gVrELwGuXvfoUtD-AUvmbhAZfX2unUiV9ZWwm45UH5w1f1swIlTkXzxQyyzdUxR1zp3mgxq5K3LrRRNWK6sxT3mVPOOFoDGAZrx-TjxhNa8VEZtMDqlj-aNR_anZcItKr4wbPhRhZIVXCUNsWLyu5X3GOcEMkEmRrvzhs99DzrnGzCNgWrAan3SkvEqnuoYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a74657a541.mp4?token=edpXFRBr-WQMKGdl9Om9CsQgarYugOvmVLAjfs3UZulmmqK-3FnksA8ZSCeVWa0dBVr7zsoaU44CotjJ0dVLBYjam9XiscQtbv_7_ufspzLrwfgHgh4ibpJ14knTSC--DqZMH96z3rPgGyLQb6Li4gVrELwGuXvfoUtD-AUvmbhAZfX2unUiV9ZWwm45UH5w1f1swIlTkXzxQyyzdUxR1zp3mgxq5K3LrRRNWK6sxT3mVPOOFoDGAZrx-TjxhNa8VEZtMDqlj-aNR_anZcItKr4wbPhRhZIVXCUNsWLyu5X3GOcEMkEmRrvzhs99DzrnGzCNgWrAan3SkvEqnuoYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
شادی ایسلندی بازیکنان پرسپولیس در کنار هواداران در ورزشگاه⠀
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/141220" target="_blank">📅 19:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141219">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس 3 - نفت آبادان 1
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141219" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141218">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
جونم جسارت تارتار ...پوریا اسمی .بازیکن محصل و مدرسه ای و آورد داخل   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/141218" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141217">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/141217" target="_blank">📅 18:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141216">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f5a2397a1.mp4?token=NIfvIpKZICDpG3jhyveQYEcVjcloQfYP2QQaXuCT96RvUcbPMCcAol8ddIWD0iYeZGeE9kp7KWNeERXYh5tXvFUasOFlTit9n4VEZjVpxy44k5jvgSzAgnuk7YVdhgnB52BcE1un24UmggXCqQX88B8wOxVFWGKHpee7yKJrOybdWf_KxImeHM6IPXZznUe0w1e7INVFyBJDstCKhVf2Mu98LQN7OdsLrNdUHBNQLPwd_IljoEgKMgjklQJ3GufwLUT1vCGRuVismHAJ2-vzzF454Pi6sLRbNhCqoRhR33SX61RGSHY6idyGw2veUo-CLF7qFL7F94qfljB4Hnbseg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f5a2397a1.mp4?token=NIfvIpKZICDpG3jhyveQYEcVjcloQfYP2QQaXuCT96RvUcbPMCcAol8ddIWD0iYeZGeE9kp7KWNeERXYh5tXvFUasOFlTit9n4VEZjVpxy44k5jvgSzAgnuk7YVdhgnB52BcE1un24UmggXCqQX88B8wOxVFWGKHpee7yKJrOybdWf_KxImeHM6IPXZznUe0w1e7INVFyBJDstCKhVf2Mu98LQN7OdsLrNdUHBNQLPwd_IljoEgKMgjklQJ3GufwLUT1vCGRuVismHAJ2-vzzF454Pi6sLRbNhCqoRhR33SX61RGSHY6idyGw2veUo-CLF7qFL7F94qfljB4Hnbseg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل سوم پرسپولیس به صنعت نفت توسط اوستون ارونوف 85
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/141216" target="_blank">📅 18:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141215">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
همون بازیکن همیشگی و تاثیر گذار ..بیفوما پنالتی گرفت و علیپور زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141215" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141214">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
گلللللل دوم توسط علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141214" target="_blank">📅 18:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141213">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a110cac30b.mp4?token=kT_yxfvl6WGb4_xHT6HpCDGj7vuyrNjw512l4wC90qGscqvMHsMkWUMO8iXT1v161V14xTSMmDbPVQPA8aP826eoeuwd3n4NABABz0pHC-gZY840wmNBAxrPUV8WQSOrSffcwZBFK-TgK3boEKOyuO4uwX-_D8z_zu3AGw7BNYtJodMh-iN94Rv5Mgews1BeB-lNh0tLebyyg4fauCSILw1vYzp-Vnn4p07LyzMBSjZ9Oo7yY2BXWIN5WJg6_KF_s4uJowTA5y41CZTX_ammoYHun-p_AgMa81ED2bX7A5qKCbXuZsAZkavm6w8FJBPmFB-iJKfNjceDWIM2LPBLm4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a110cac30b.mp4?token=kT_yxfvl6WGb4_xHT6HpCDGj7vuyrNjw512l4wC90qGscqvMHsMkWUMO8iXT1v161V14xTSMmDbPVQPA8aP826eoeuwd3n4NABABz0pHC-gZY840wmNBAxrPUV8WQSOrSffcwZBFK-TgK3boEKOyuO4uwX-_D8z_zu3AGw7BNYtJodMh-iN94Rv5Mgews1BeB-lNh0tLebyyg4fauCSILw1vYzp-Vnn4p07LyzMBSjZ9Oo7yY2BXWIN5WJg6_KF_s4uJowTA5y41CZTX_ammoYHun-p_AgMa81ED2bX7A5qKCbXuZsAZkavm6w8FJBPmFB-iJKfNjceDWIM2LPBLm4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گلللللل دوم توسط علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141213" target="_blank">📅 18:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141212">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
با تعویض اورونوف جای عمری و پورعلی جای لطیفی فر میشه اختلاف و نیمه دوم بیشتر کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141212" target="_blank">📅 18:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141211">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141211" target="_blank">📅 18:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141210">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
چشم نوازترین پرسپولیس چند سال اخیر و میبینیم ..نیمه اول و با یک گل بردیم ...تو نیمه ای که سه چهار گل و نزدیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141210" target="_blank">📅 18:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141209">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=eww6plPMXzrAD_XVSyYXfB9mfARHxlvgSh7Xf9cbp0uKRgg8eLwV50wec72FY7FrVBQ2zNMvmourT4BkCUI1EmKtJ-Bvtxho5R9iwbVLgSFOJVfE6btWJ-0-Vsw-ypdWeK8syi1b5-4vb3U0UEqYWl0wTUUCOc5FQTpVkUnDwnpcpmfATq-YCuKuFrmSzoGwLjm2SczrsLJgPh5KrTB8ixdNbMjnubGTOqPXJiiouLsvRxDyYFfs39M9nT7OB9SjYf1nsft3zY0NoF8irrlYa4OdOQoLX8X-D6hmJfM_lVEnSTv06XewYLcHX-Q402ZjXIuPfsJdOK8bIaT_PgOBNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36338a35c2.mp4?token=eww6plPMXzrAD_XVSyYXfB9mfARHxlvgSh7Xf9cbp0uKRgg8eLwV50wec72FY7FrVBQ2zNMvmourT4BkCUI1EmKtJ-Bvtxho5R9iwbVLgSFOJVfE6btWJ-0-Vsw-ypdWeK8syi1b5-4vb3U0UEqYWl0wTUUCOc5FQTpVkUnDwnpcpmfATq-YCuKuFrmSzoGwLjm2SczrsLJgPh5KrTB8ixdNbMjnubGTOqPXJiiouLsvRxDyYFfs39M9nT7OB9SjYf1nsft3zY0NoF8irrlYa4OdOQoLX8X-D6hmJfM_lVEnSTv06XewYLcHX-Q402ZjXIuPfsJdOK8bIaT_PgOBNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چقدر خوبی شما آقای نیازمند
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141209" target="_blank">📅 18:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141208">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
یک گل زدیم و سه گل نزدیم ..و همچنان پرسپولیس مثل همه بازی ها سوار بازیه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141208" target="_blank">📅 17:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141207">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گل اول و زدیم خیلی زوددد....سرگیف داد بیفوما زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141207" target="_blank">📅 17:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141206">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141206" target="_blank">📅 17:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141205">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141205" target="_blank">📅 17:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141204">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس که سه امتیازش به اندازه شش امتیاز ارزش داره ..دلمون برای پرسپولیس تنگ شده بود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141204" target="_blank">📅 16:54 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141203">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141203" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141202">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرایز اصلی روی نیمکت تیم هست
✔️
✔️
پویا اسمی ۱۶ ساله
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/141202" target="_blank">📅 16:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141201">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
نیمکت ذخیره پرسپولیس مقابل صنعت‌نفت:
❌
❌
امیررضا رفیعی، ابوالفضل جلالی، علی علیپور، پوریا شهرآبادی، امیرحسین محمودی، محمدحسین صادقی، امیرحسین طاهری، پویا اسمی، پویا پورعلی، استون اورونوف، یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141201" target="_blank">📅 16:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141200">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
ترکیب اومد ..جای جلالی تیکدری بازی می‌کنه..جای پورعلی لطیفی فر بازی می‌کنه و جای شهرابادی محمد عمری بازی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141200" target="_blank">📅 16:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141199">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=kByR4enHiAe-hkkp8SIVHH8Mp2DUaEbv9MBUQ0cH-icB08qwtDtUTl4x2v_rH0ftHGM5nIEQ--1j6IPpsIQUBHGKFXQJaVj56ZF4PicVBEmjgBuMS8PD8tejfG5pUCyFnreW_BDQgZ3JLAkueZcB6uCFBnkz2NYqA31N_4vN-PsxWF5R00YfhQYwoLnM_FP_2fc-yS9rhSaE3bjvWETTJIz9HWyWEuSyB3Zu2sR-qXhXga602imXNsoos_FQ9x3w0Q_UnJJAUo-CRU4gFDP7nmKPe-ItqNxkxH_gmWjSY4Lr-1silkBi_fo7dKD_0FkHVgw0RUj_Wof1EYJxWPKmdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c7ca0c681.mp4?token=kByR4enHiAe-hkkp8SIVHH8Mp2DUaEbv9MBUQ0cH-icB08qwtDtUTl4x2v_rH0ftHGM5nIEQ--1j6IPpsIQUBHGKFXQJaVj56ZF4PicVBEmjgBuMS8PD8tejfG5pUCyFnreW_BDQgZ3JLAkueZcB6uCFBnkz2NYqA31N_4vN-PsxWF5R00YfhQYwoLnM_FP_2fc-yS9rhSaE3bjvWETTJIz9HWyWEuSyB3Zu2sR-qXhXga602imXNsoos_FQ9x3w0Q_UnJJAUo-CRU4gFDP7nmKPe-ItqNxkxH_gmWjSY4Lr-1silkBi_fo7dKD_0FkHVgw0RUj_Wof1EYJxWPKmdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
باران در شهرقدس و حضور بانوان هوادار پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/141199" target="_blank">📅 16:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
ترکیب احتمالی پرسپولیس برای بازی با صنعت نفت
✅
حضرات/نظرات:
📺
پیام نیازمند
📺
زارع
📺
ابرقویی
📺
جلالی
📺
عیدی
📺
خدابنده لو
📺
پورعلی
📺
محبی
📺
بیفوما
📺
شهرآبادی
📺
سرگیف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/141198" target="_blank">📅 16:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🟥
ورود اعضای پرسپولیس به ورزشگاه شهدای شهرقدس
❤️
..
🚨
هوا هم مشخصه باد و بارون شدیده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/141197" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZXhJ56MVSdvfUPL3SDjifsi0ZSdT-oCnMhjkNwBZ_cXb1rzhORxWKhdFCNhXkKl3EYP8JiU60P9QoBCS7qO7e0Sa-YgTqG6g9EP9MQWOFpqU4jsInb8qJ2IpYiUuPG1dnbTVJUSKqbKaneDUIVnBncSO9a00Yo036PT_xwQXfDFu0ajUIzQNTFpNqj3OptASKO85lsHjVE_zBNDaYaNpwOQvL2Tihx-3CtZ2GE-XTnUsT37hCkyUns5aCwwssfj6Ih90idDJ3IkDhY3Ci8jMnZiBODW8aJX99xxXb4x9aL6c7dxqVZuBBZ2Y2joqnrH4nysi9uOfghky__W4Te0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نمای آنلاین استادیوم شهرقدس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/141196" target="_blank">📅 15:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141195">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
⭕️
با اعلام باشگاه تراکتور، علیرضا بیرانوند به دلیل مصاحبه بعد از بازی با استقلال از این تیم کنار گذاشته شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141195" target="_blank">📅 15:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuiQ9LL9u5iBzt0nKxCR_fCFoolZ6xxaqNF1rknICSGrN1h9MSreVdUgWGseca300L6mUihL_g2gIzecCGvG6fexLCenICJhbLLMOZtwIJmt8mRLST0gvuMe_gj6e3uic1t7nOLLR51-PPVv8ruDuDHEGqjrlr7Lg1avlrPGJvFvrcc1TZQnPTLddOgxvLQpF7mgBg6__SpMGJedaALoRqjU_1_DC1a7cW2Bp2FfRzYdU7GHq3afc6URTCfkBi6KYZllOsqsdy5_rVeY46eq1hcwrbb7wUpOZWXnVhodBacrQTFTqm9lrafKjLPkExtsv-2MECiRrlKfJjaEWlUunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج اعضای تیم از هتل به سمت ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141194" target="_blank">📅 15:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141193">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⭕️
فردا ببر و محبوب تر شو .حاج مهدی تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/141193" target="_blank">📅 15:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141192">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7JBmuZiIi1RyhtBCMdwZ2w4zENEmZIWivJHPPeH2ih-D527XmqrR44GdoUijaoj4JlK_JFRFz2TaTqkNq1r3raL27aMY6R2j0tUMnV6ynwkLpKX6amkULVHvnhiWBWOS6lXz5NXetb_cFJRSAJnmy2SJ0-luN5rz_iBiXgwAcnIlsAUQktAUsoobP2qDi7x5l7W7RTxyOKl8_HTMMF2Pe04Gtw9_VHKFkBsvYHEqEBN-SuJZkVL6T3As__lda3NfrZJo3XcFprabNEnkkdCmh10wOGkgaPtD6KNsGcY3M1DRNukEld0dxDPKeG7gDHAvavjmMKLBumfj9h8ZlekNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
علی علیپور: از پیام‌های هواداران عزیز که نگران حالم بودند متشکرم. خوشبختانه مصدومیت جزئی‌ام برطرف شده و با آماده‌سازی کامل در خدمت تیم و کادرفنی هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141192" target="_blank">📅 15:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141191">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
باشگاه تراکتور درنظر دارد تا با توجه به مصاحبه علیرضا بیرانوند، به او اجازه فسخ قرارداد و حضور در تیمی دیگر را ندهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141191" target="_blank">📅 14:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141190">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
🇮🇷
🇮🇷
به مانند بانوان ، تمام بلیط های جایگاه به فروش رسید ، دم تک تک عزیزانی که توی این شرایط اقتصادی میرن هزینه می‌کنن و مستقیم  از تیم حمایت میکنن گرم
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/141190" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141189">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141189" target="_blank">📅 14:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141188">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🙏
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141188" target="_blank">📅 14:12 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141187">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv_gkyWGd9MOVwSwOn1Tw9N1s_0_gFMzt1JujJdhlVQCFyLOIwSk0BP-kKx6-FN3MFnQix9qJAqRN5jOHtg8ozs0iuHmwk20mg_LrmydK5y1AbaAhaudgEivMKy35ckq13TG04Ld37T4peIIqaOPrW-sa5ArVcWXnfqg-SOaRW_oVvLNUOqLx-1oOdYjNapEShJYfKk_AGnYRXO3ME8v175A6EbBDiplHJ6LWca2727YD32rLKF-G-gF6-4KTRL5XZHaijfip44SWYBMX4J8oEQLF4R423epsqoi9OYF9wsVUznPRPN0dEqYHHaf7b1T8IHM_TECP_fCp1G3k1184g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت
‼️
علی علیپور در این فصل تمام گل و پاس گل های خودشو در این فصل در دیدار های خانگی و در ورزشگاه شهدای شهر قدس ثبت کرده
👀
✔️
پرسپولیس امروز در ورزشگاه شهدای شهرقدس به مصاف صنعت نفت آبادان می‌ره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/141187" target="_blank">📅 14:09 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141186">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
علیپور هنوز زانو درد داره و بازی کردنش ریسکه البته خودش میخواد که بازی کنه تا از کورس عقب نیفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/141186" target="_blank">📅 13:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141185">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
❌
❌
اگه امروز علیپور بازی نکنه و در غیاب کنعانی نیازمند کاپیتانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/141185" target="_blank">📅 13:27 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
