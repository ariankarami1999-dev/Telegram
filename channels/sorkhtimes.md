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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 13:28:15</div>
<hr>

<div class="tg-post" id="msg-138718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
دستمزد طارمی در امارات آب رفت.
🔻
سایت threads امروز(جمعه) از دستمزد مهدی طارمی در لیگ امارات پرده برداشت و نوشت: مهاجم ایرانی در الوصل قرار است سالیانه 800 هزار دلار دریافت کند. دستمزد مهاجم ایرانی در الوصل در مقایسه با المپیاکوس(سالیانه 2.2 میلیون دلار)…</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/138718" target="_blank">📅 13:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
✅
⏳
10 روز تا پایان پنجره نقل‌وانتقالات تابستانی فوتبال ایران باقی مانده است.
❌
❌
پس از بسته‌شدن پنجره، باشگاه‌ها تنها امکان جذب حداکثر 3 بازیکن آزاد را خواهند داشت. بنابراین روزهای پایانی می‌تواند برای تکمیل فهرست تیم‌ها بسیار تعیین‌کننده باشد.  «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 305 · <a href="https://t.me/SorkhTimes/138717" target="_blank">📅 13:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSSNckYMF_pRbNGqzLoyNVrL8LwVwBTKaW0iMsHWTUdOEow6-YxO5FxWopAsD3mJtF78x-j11iSpYW8nIsmjQktC4gpZ_XWMrxlnbe5l1LPXN94aY5JFg3pP4ROCQJHab4Kb1DVRNquEQ8PNc6HnjO4-oReglM6KGKolDyKzpM3JiDoEVEplAIDXkbP996BtHtwblnZdBTuoHQMO7G_A2Gr-QO8uvAKUuVMs-uJoxInf67OK7KBnlez0rKVg9dB2ImegQj4ac1n5YTRqrsAiDPJtGaUYgJ6kDB9T1XyiC9piGbB2PIVEq--d-h0TLKQSBJWmwlp3tN0SzJDRit8tfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
فرزین معامله‌گری، بازیکن پرسپولیس برای گذراندن سربازی به ملوان پیوست.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 699 · <a href="https://t.me/SorkhTimes/138716" target="_blank">📅 13:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8_Ip1VIxTd_Q56aAgKKx-PhFNiCq8ZrUgjwX3U6VI5t1FEv5MAs9m1M-pKmwVAu1PRJC83WunFFc2f0-ybtrOWgAQ3LTbLZ6C_WziIqbNXP3OP3ePdjhj3MyyR5BELftOvtpBOown4xS225U-3ls5H20AP_BIue9fB9cQESwYWKr4HV4_IWHgqCaAy9qm6ai_jM8CZD76xOPV4hSqw6XZz1mauGTNfIiDuxrjzxZTWek-Q0E2gzJ13llq5OIeZqTjocGcfg5CFtaVW2snsdOSFzx2i3AVeIaVS2mYKBF0C1nFP21NSfqiLWQ6VuNaNSNOADIA_MrpcbW9HQLgLqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آنا: 20 درصد از قرارداد بازیکنان پرسپولیس واریز شد، و قراره 20 درصد قرارداد بازیکنان خارجی هم بزودی واریز بشه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/SorkhTimes/138715" target="_blank">📅 13:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdvIwQOGYm_337f1nhXfUQBQLZzZxgkTKQBQa9YCmyj3s5GJafiHH9qmA66tdWYJJv6P94H6bNDa9nCa1wQvzTHfN0_1U3nrX66ouYCKm5qRvwI7lj76asoM73roTLdDg1WnJIEMG0op0O8roqo-Flxu92lkwVcNVcbjJC1QBVxC7qwdY1se-R4ChvCXQNzX5jCozfFl_GnlxWvMednMhA0KOo8I04pPob_jnDwIp2FUjN6-Ob_eKE-ejGp_fwlDi6kYVjhUfj4bwuRt-NEl_yUlN4S7PEY9Er0xVnBdxo7UfbnNsQiRPWEXOPerqN7hIrFlLX_fMGMoaY09xaZ9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دستمزد طارمی در امارات آب رفت.
🔻
سایت threads امروز(جمعه) از دستمزد مهدی طارمی در لیگ امارات پرده برداشت و نوشت: مهاجم ایرانی در الوصل قرار است سالیانه 800 هزار دلار دریافت کند. دستمزد مهاجم ایرانی در الوصل در مقایسه با المپیاکوس(سالیانه 2.2 میلیون دلار) یک سوم شده است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/138714" target="_blank">📅 13:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
✅
در صورت نرسیدن جلالی به بازی با تراکتور ابرقویی گزینه دفاع چپ در مقابل تراکتور خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/138713" target="_blank">📅 13:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138712">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/138712" target="_blank">📅 13:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/138711" target="_blank">📅 12:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
فوری | سردار زاهدی، معاون نظام وظیفه عمومی:
❌
علیرضا بیرانوند از مهرماه 1405 سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/138710" target="_blank">📅 12:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
فوری | سردار زاهدی، معاون نظام وظیفه عمومی:
❌
علیرضا بیرانوند از مهرماه 1405 سرباز خواهد شد و دیگر امکان بازی برای تراکتور را نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/138709" target="_blank">📅 12:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/138708" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/138707" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138706">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/138706" target="_blank">📅 11:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/138705" target="_blank">📅 10:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0oBcMa1xT60zJZSBCsnQ88txU9e6KUtlHc87axDlmP7Ur_XKrb6C5qsNiBk7fiLspn1_wc28_KCSrLZdmKtf70AE5A-8clqmLWLw-OddGjoU1y8as8QPTdMfvp1wd9GNLL58oaoBjZHXPWutlwUezE_L6y-PsJ8yG1zHJYoR-DEA9Acg50nrwI_Qu1R-5EbiXfbPhXx3zgCFdxsb1C3T6hltEqEKDPMcDT7H-E-uGTW_tPgRdoDt4rprysvClGcIIgBee0wY5xjFZIYPBenQ_9734DFjYNlrBlWV1b0_5aPTT-aiAxjBfV8Nm7CavqIqvNSCIUPXLcphRv6NBG9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/138704" target="_blank">📅 10:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس در دیداری دوستانه با گل‌های امیرحسین محمودی، مهدی تیکدری، پوریا شهرآبادی و محمدحسین صادقی، 4 بر 2 آریو اسلامشهر را شکست داد.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/138703" target="_blank">📅 10:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔻
🔻
🔻
میثاقی: احتمال داره حسین زاده و بیرانوند به همراه تیم ملی امید راهی بازیای ناگویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/138702" target="_blank">📅 08:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138701">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/138701" target="_blank">📅 08:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138700">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/138700" target="_blank">📅 08:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138699">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/138699" target="_blank">📅 02:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس، پرسپولیس فصل آینده در لیگ یک تیم داری خواهد کرد و اگر مشکل خاصی پیش نیاد بزودی امتیاز فولاد نوین به پرسپولیس منتقل میشه؛ در صورت نهایی شدن انتقال امتیاز فولاد نوین…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/138698" target="_blank">📅 02:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏆
🏆
دربی تهران رسماً در استادیوم نقش جهان برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138697" target="_blank">📅 01:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
حدادی: دوران بازیکن سالاری و دخالت هوادار متمول در پرسپولیس تمام شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/138696" target="_blank">📅 01:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⚡️
مدیر برنامه آسانی: نامه فسخ دستکاری شده است
🔹
مدیر برنامه یاسر آسانی، هافبک استقلال، انتشار نامه فسخ قرارداد این بازیکن را تکذیب کرد و مدعی شد نامه منتشرشده با هوش مصنوعی دستکاری شده است.
🔹
رسانه‌های مختلف امروز نامه‌ای منتسب به فسخ قرارداد یاسر آسانی با…</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138695" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138694" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/138693" target="_blank">📅 00:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
🔴
🔴
پیگیری کردم؛ ابوالفضل جلالی احتمالا به دلیل مصدومیت بازی‌های حساس پرسپولیس مقابل تراکتور ، ملوان و استقلال را از دست بدهد. در واقع یک ماه دور از میادین.
🟫
🟫
🟫
البته خبر پارگی رباط صلیبی صحت نداره چون زانوی جلالی نچرخیده که رباط بده و خودش هم با پای خودش بدون…</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138692" target="_blank">📅 00:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✖️
✖️
احتمال معاوضه بیفوما با رزاق‌پور وجود داره.
🔴
تارتار تاکید ویژه داره رزاق‌پور جذب بشه. البته تارتار فعلا در قبال رد کردن بیفوما پاسخی نداده.
🔴
ولی درخواست فولاد همینه. بیفوما رو بدید رزاق‌پور رو ببرید.
🎤
سپهر خرمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138691" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
رسمی؛ با اعلام سازمان لیگ دربی پایتخت برای اولین‌بار قرار است در اصفهان و ورزشگاه نقش جهان برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138690" target="_blank">📅 00:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138689" target="_blank">📅 00:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚜
علیرضا بیرانوند در تلاش برای حضور در تیم ملی امید ایران برای ۳ سهمیه بزرگسالان میباشد تا با کسب مقام احتمالی در مسابقات آسیایی از خدمت سربازی معاف شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138688" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🟫
🟫
🟫
بهمنی: استقلال به عنوان میزبان دربی، نود درصد گنجایش ورزشگاه را در اختیار خواهد داشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138687" target="_blank">📅 23:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🟧
🟧
🟧
دیدار پرسپولیس و تراکتور قطعا بدون تماشاگر برگزار می شود
🔻
حجت الله بهمنی سخنگوی سازمان  لیگ اعلام کرد هر دو دیدار رفت و برگشت پرسپولیس مقابل تراکتور قطعا در این فصل بدون تماشاگر برگزار می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/138686" target="_blank">📅 23:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
حساس‌ترین بازی هفته سوم لیگ برتر پشت‌ درهای بسته باید برگزار شود؛در شرایطی که براساس رای فروردین 1404 کمیته انضباطی و تائید استیناف تمام دیدارهای تراکتور و پرسپولیس مقابل هم در مسابقات لیگ برتر جام حذفی و در دو فصل 1405_1404 و 1406_1405 باید بدون حضور تماشاگر…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138685" target="_blank">📅 23:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxI7Nn_EvwKByt1c90AXysGWEfUn25BSieJml0MM33UlAe2RwP7tzLSM3lpJC6eVNeLEkJh7ToSaknucmsWILOiExV3QohTvXSFqFHqwelIU4Zq5yxnBmxtiVJJK3D_9-NU3gmu_pgRgAduRkNSlEZvbcT1mtmZCWcrEN7XuxBWw6ffujDLl8Vdh54qZSmi50q7X6eRhyI8ag28HPBFUxCE2S4n1rks9HQvap2oq6-y72iDjFFxG0BzB5-JM80T0aK6jdcC7VYvC5n2A9DNBTiOgin2vYJyuw5DjcZ7ZZ1hxHHzBQENJikkb0nHwbpwdFb2IW_IbU7gZstPPv67Fdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ایسنا: هر تیمی که 1.1 میلیون دلار به الوحده بده رضایت نامه محمد قربانی برای اون تیم صادر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138684" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8400611245.mp4?token=mvfT9evUxA4DaD0lbz68ANW4zqjc_E11FAV-yqRuZuzyWGGx1JEwqat6sOxILaT0n7fp3k3wWB7vjcVayuCEo3fstanYUx0wpGcIOsOX5op8X6GIyT1t0QISVxxs4Bjmz53fdyg53hjLEtrENVFby4C-IKNtFWLRGUR_k-qT6kzxoRTbv7KM_XYMo2XTadUIXDQ2OKFtiaWJnwf6YuMyzjb9GYmvOlKFyap4mK3_kxIVgF2OLoglawgG0QYrlyY6pnbDhzDHoST3o-RMVWgPa9ZdikI_W_rGKbDKxQIN-86Z7bpTamcEzQPjWg85wYr07ooAFRGo0xyXiBKpz2mSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8400611245.mp4?token=mvfT9evUxA4DaD0lbz68ANW4zqjc_E11FAV-yqRuZuzyWGGx1JEwqat6sOxILaT0n7fp3k3wWB7vjcVayuCEo3fstanYUx0wpGcIOsOX5op8X6GIyT1t0QISVxxs4Bjmz53fdyg53hjLEtrENVFby4C-IKNtFWLRGUR_k-qT6kzxoRTbv7KM_XYMo2XTadUIXDQ2OKFtiaWJnwf6YuMyzjb9GYmvOlKFyap4mK3_kxIVgF2OLoglawgG0QYrlyY6pnbDhzDHoST3o-RMVWgPa9ZdikI_W_rGKbDKxQIN-86Z7bpTamcEzQPjWg85wYr07ooAFRGo0xyXiBKpz2mSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بازگشا سخنگوی باشگاه پرسپولیس: فکر نمی کنم محمد قربانی را باشگاهش بفروشد/ پرونده هیچ بازیکنی را برای جذبش نمی بندیم ولی در خصوص این بازیکن با توجه به مبلغ قراردادش اصلا وارد جزئیات برای این انتقال نشده ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138683" target="_blank">📅 22:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138681">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚽️
🔻
بازگشا: شیر ما برگرفته از هخامنشیان و نماد باشگاه ماست، اما شیر استقلال و نمی‌دونم از کجا اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138681" target="_blank">📅 22:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138680">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🚀
آف ویژه سرویس نامحدود
🚀
1‌کاربره فقط و فقط 600T
2 کاربره فقط و فقط 700T
3 کاربره فقط و فقط 800T
ثبت سفارش و پشتیبانی:
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138680" target="_blank">📅 21:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138679">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
🔻
🔻
طبق شنیده ها فولاد در آخرین جواب به پیشنهاد پرسپولیس خواستار معاوضه بیفوما با رزاق پور شده.
❌
همه چیز به نظر تارتار بستگی داره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138679" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138678">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💢
💢
💢
باشگاه میخواد یکی دو بازیکن جوون رو وارد معامله با فولاد کنه تا با قرض دادن این بازیکن ها و مبلغی پول رزاق پور رو جذب کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138678" target="_blank">📅 20:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138677">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138677" target="_blank">📅 20:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138676">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5FoAAg8PW4O6PGkGyHM8oTLGahzIFoFWG5N9oXBzY1uD70TeFMkMjRUv9EER06u9gnodwjgd67v_YyIeAEAI9FM_3VhpsNUnbVxkXFeSGZ3E9NVE2yC5SbtQ-EZ3N19gp5HYoJBBYBRaW3O2PHEvwPUgfm6QtHQ-lB8ILZPg8N7407uyvsvmm7FBTe6whuNz8nq_I2eWY9eCR9FsUJUq5EiZo6ALUA7I8DFGTPenFNBFlsF8UMRl5aIwRr2vk8WKmyhzPjeTh0yc7pYd_wv0vntSuAUN-xgVW82-j1CZbB4lUCzYEgHUtYVI-NvoEGq8ynSuMHX0SCyrol_vUfhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
فوری ؛ یکی از مدیران الوحده امارات در گفتگویی با رسانه الریاضیه این کشور اعلام کرد که رقم رضایت‌نامه محمد قربانی برای فروش این بازیکن به‌ دو تیم بزرگ ایرانی و خارجی رقم 1.1 میلیون دلار است.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/138676" target="_blank">📅 20:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138675">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3BbX7QGgcivW5YUReW8CknSzBElUrylIkllbNnLYgGRAfwVip-sVl1EsK8oQQ5sld9H1LliYT8jB65oSdd98e1b3Ssg7XSrnhGyhxvuDx5k3Dp7u7K7cJruwT8NUfAbzPG8JIeD7H29fhkCRruSPa-cVT2wEtHIzMUZ5FBaMgaXgWa8K3QEvtlmMP_hsNKpbw7yp-X4F1eawRkxDLSmO14HsIradwZa6CT3L2IIcgd0fF4CROtGoN8BJxbzKojkuQ19vnK-UKl2BC5FdSr0CVDWve3fpiH0vgtr-EwAG_JWXkqMkmCf9Z8crjXKoLi4mD__g6cR_3v-gCZiwTo-qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
قابی از دیدار تدارکاتی پرسپولیس - آریو اسلامشهر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138675" target="_blank">📅 20:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138674">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=qN4nOFzxJ3RjxTtwaf5ZN6oQFyM4HfQFmGo4VKJeEam36cGCrBAE1suFJr1-XDjEXTkR2uNW6ue7D8ldTZaFSBLTiBRURMEF2xSO_0kREUjn98zG3FzIILahmO8idAccNpo0yEDhZtCkJLTEPP7XwjNXAuUDM8kZiMBQcqfUpjrDb3Kr5nsm9RdREbmOr2_vPrOmo-BC0bJKUivZ2pMjqf3sozYdIg9JIGXru6Z41MQ1TfGuVv0o68A0cezz3taz123o8sNFZwbfsn4JdkWSV7lY7adJMHnkFUapXJzuZaxtdyZJx7XQNJ9bC10HWNVmndMXfs5LZarhALQrKZPNMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5bbffc124.mp4?token=qN4nOFzxJ3RjxTtwaf5ZN6oQFyM4HfQFmGo4VKJeEam36cGCrBAE1suFJr1-XDjEXTkR2uNW6ue7D8ldTZaFSBLTiBRURMEF2xSO_0kREUjn98zG3FzIILahmO8idAccNpo0yEDhZtCkJLTEPP7XwjNXAuUDM8kZiMBQcqfUpjrDb3Kr5nsm9RdREbmOr2_vPrOmo-BC0bJKUivZ2pMjqf3sozYdIg9JIGXru6Z41MQ1TfGuVv0o68A0cezz3taz123o8sNFZwbfsn4JdkWSV7lY7adJMHnkFUapXJzuZaxtdyZJx7XQNJ9bC10HWNVmndMXfs5LZarhALQrKZPNMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
🏅
این شاهکارو از دوربین باشگاه هم ببینید
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
❤️
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138674" target="_blank">📅 20:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138673">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTghdpDzTQT2py5AU9gXZlXPLOxhHBiEeaKK1qNSqx23N1CSA5_0yYkvvL_P7sLfFOGBmWGNsdasST3CahbwIOkrhHhbrNEyd81_6rciZ4pkbIzs5ZNMa-mDOw2fRCKZnjgCA6AaI7LtQ3LxEHiDl7K2wuBpOJCwNWxfQBwwPGSnhiCS0KBJ0oQrlxhFc0TJCcNJJudTSc2Vx-JuoAvB2fdHJJNTD6Le4hqHImGbnBVK3WhfPe6D_Hd0muW5Pk7xdMG_CoQzspIShKm0iS8VPSssbala8aaruaR70tsJSiAu7fU8JCu1JNuFNzrjh3RzLLO7VKouD5kVUPK53HYfiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138673" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138672">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138672" target="_blank">📅 19:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138671">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/138671" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138670">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/138670" target="_blank">📅 17:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138669">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/138669" target="_blank">📅 17:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138668">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6RhVWu-k4OGTPHGjsoiskxarsuC4v6AUQZTypP1hr4PaqWZ1HtbLvdVlSJE--6QEpL6VhkJC3yPOYni1zPQH0GzypENpfFp8xvF26Y_-47mmSq3ta0C7T6jDxgesbbvygyUKpd4XAWa0EbEJ44PELS7qpkqB11AaraxgOdE1eD-VqeRfzoqoBmZeUC6gQcd0r4eeVG3VYouKVcC2qRC7spVO_ijjjJEaMjZrHdLVpBfpZRwBJiOHZJM1bjT3R5GJ-6CagEBVyBlG14MEgOEAB5u42p6XhGUW9i70_JNPWDuI9lzEg_PIwD8XkSJYpyZm1weFgtUxvrjE4M9dXmeRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 7K · <a href="https://t.me/SorkhTimes/138668" target="_blank">📅 17:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138667">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138667" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138666">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/138666" target="_blank">📅 17:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138665">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">💢
💢
💢
💢
مدیریت بانک شهر صبح امروز به وعده‌اش عمل‌کرد و 800 هزار دلار بودجه برای جذب محمد قربانی دراختیار مدیریت پرسپولیس قرار داد.
❗
❗
مدیربرنامه‌های‌محمدقربانی  به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت…</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/138665" target="_blank">📅 17:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138664">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
وضعیت مدافع چپ پرسپولیس بزودی مشخص خواهد شد
✔️
ابوالفضل جلالی مدافع چپ سرخپوشان که در روز گذشته دچار مصدومیت شد قرار است طی امروز فردا تستهای پزشکی خود را آغاز کند تا درصورت عدم مشکل به ترکیب پرسپولیس مقابل تراکتور در هفته سوم لیگ برتر بازگردد.   «سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138664" target="_blank">📅 16:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138663">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0QqQswPKtGdCy1fJ_SEDDQW8qDzhAsdN0rgVGqj0Oa8nPMksdmYI_2MZ1S81CamAha9D0i_jek0hZ54tzeUwesBkZeFhnefAHhRTPleFE53ZH_DA-4rHLeX-Z5lTaHe7vKrlrl9IcTH0bCNKsmjxfxA-tsKYrAhZIi3S2Aw2BTgwJcpkPjmwIthZELTmtFgd6tLYVmpaMdXLrGJTUle-NlMVcb1V7oZYnv8YHYl00cEfOPTxMkHRHE5tdOoTowdTss-6gpWU2tBcTfP-Fz0UyvZ4vtS6d4hezHg3UpbUzr8_Hm0TrTnDjPJXQWnxI9LghGdUjvbyI1V0anO96Q0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138663" target="_blank">📅 16:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138662">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
تارتار: چون جلالی از قبل هم مصدومیت داشت، وقتی نتیجه ۲ بر صفر بود ترجیح دادیم ریسک نکنیم و او را تعویض کنیم.‌ما در پست او همایی‌فر را هم داریم که از جوانان خوب است اما نیاز داریم در این پست تقویت بشویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138662" target="_blank">📅 15:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138661">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
✅
مشاور قالیباف اعلام کرد: با تصمیم سران قوا، گرانی بنزین منتفی شد..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138661" target="_blank">📅 15:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138660">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQDZAYpm_omVrMXHNN0w5xY1OufN71TEgEkEYhho4yJ7nCJX8dQKHTOquCQhTawAjBo4Pyb5MzqvhMPuQR3xr5U2egukAkS1N5juBZ8e29RWDSvP3AjdWrRjY-mwSlJWvlNRfet6y27GsXLkQWakiBy9kQNfAEH99QgsiiID7iGEYc-aZdgLrVXZSOke27VOHlkt3NhmOX1GrhYM12GeZNROrtalIOPjwC6UIbumjVCq6tQ7HpIZq7z_qZeUYwJasu8vuqylFuxIBx2GzExWsGzPQNQhu4R64OZNrKBK9OqSjvAF74O8Be5rMijICo7uuDn_rOws33NsCKrKrWBCSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/138660" target="_blank">📅 15:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKZk4iohsj7i8yVPZq-DD0AG6ivfAG52GbaoZe2b93LJkOL0bcd_UUtwV6sFse-Ro9OGWSMkiVlXA5mV-tPQNwBjz1qEhiF2amVn_ML5i0L0oqOf9ExMQCK99Vr2Dy15o9UKQw1VCNIeCHfKU8qMyQp3yp7ADu-2y4sIRIOqn1gL4U3SY0syvzLT3-SEReVFYb1WFFFDddFWfAXxnhSGbbnmTBDbG7DlHXWRdg_5JITx5_lqiSRFMaGPJW6m6EB2JINCKnD7yYEBWv1mnx0wQtQmyGgjXwOLa4UslhcH6N9IXEah5jxmMvQNuAQPphwFf35pD88Lt4ZfqNuWzpvxqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/138659" target="_blank">📅 13:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138658">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138658" target="_blank">📅 13:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138657">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/138657" target="_blank">📅 13:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138656">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138656" target="_blank">📅 13:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138655">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/138655" target="_blank">📅 13:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138654">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138654" target="_blank">📅 13:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138653">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138653" target="_blank">📅 12:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138652">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
✔️
عبدی: بیفوما اگرچه فصل گذشته فصل خوبی را پشت سر نگذاشت، اما در فصل جاری از نظر کیفیت فوتبال و میزان ازخودگذشتگی، من را شگفت‌زده کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138652" target="_blank">📅 12:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138651">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
❌
نیمکت
✔️
امیر رضا رفیعی
✔️
ایری
✔️
تیکدری
✔️
شه‍رآبادی
✔️
بیفوما
✔️
محمودی
✔️
اورونوف
✔️
همایی فر
✔️
سلمانی
✔️
باکیچ
✔️
لطیفی فر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/138651" target="_blank">📅 12:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138650">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLIiQjm81QuRS0GZH5R63lVluu-m7JweClP7c4RC4AFYenKkGAAkh1UgCg2rPiyXMM1OScv_67JlR76kUpJCb6usDeKh9zavCpX9_r53yITnBhk6x2oZG7aHjCeUgSbYlUQ1lRy4R1cFZoXvxnfp5Fx9zxAInXLhmSKOny_0ufNhwdjQoxtd01ktkFBM_KsvBrxf790N1Peu2zRUYfwokr4yN2Z8n2dOHbyMYJ3WdD0md7TUOYW-_TUxhKy4QwRm9VZU_Dw0wC71ZQSFMWOygQC8hdtOWJVZJ-A4YEF6FwSMrpEuBkgoCmZ1Y6q3zx5EabukMGg3ev1sz85ODWE_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
❤️
برخلاف برخی شایعات مطرح‌شده، اوستون اورونوف در جشن پیروزی کنار هواداران حضور داشت و در شادی آن‌ها سهیم شد؛ او پس از پایان جشن، راهی رختکن شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138650" target="_blank">📅 10:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138649">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XawtsrO87V49zVZ4M560STv-qAbhvSGbpxgQPZYHw5MZkqoBFd2nA62cwk8UKQQ2Bxvyjjr5rdAXEZYnudIVCnldG5HWpUQgg9J0HoHLpr7mQ-U_IIp6UKFdl_PcLqbPOGhcV2rOD62ju3DSXPJhz5sEFCFvJ-no7QYjO2VQW11lCplFZ4IiBRo3a8lktnSb1T0x2Zu4QQtgINikFKuDfCEei1E5CsXt5nLPA_SWUUoUL_PqrS3V2WmzK-vjGhwFRcgYxxtF2E5X58qCrRCwcHiWuhQolaKQDHUm1J8Vsq7z2IL94HxskMV1YZH-AXWEBwSSISE_AWh31momR58r1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
هفته‌سوم لیگ‌برتر فوتبال
✔️
پرسپولیس
🆚
تراکتور
✔️
🗓
تاریخ دوشنبه ۲ شهریور
⏰
ساعت ۱۸:۳۰
🏟
میزبان ورزشگاه تبریز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/138649" target="_blank">📅 10:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚽️
🔻
بازگشا: شیر ما برگرفته از هخامنشیان و نماد باشگاه ماست، اما شیر استقلال و نمی‌دونم از کجا اومده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138648" target="_blank">📅 10:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
علی علیپور با دو پاس گل و یک گل بهترین بازیکن بازی امشب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138647" target="_blank">📅 09:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIoVIsuxjm7zw0qSPm072eAQXLbtI1hUv2j6ULXbpUY4-9l9xhaEjQel9vL03urOf7RXsgxBLp7y_Prg-RglgtV6IDb3x4-KbOJlxe_Jfk_HcEoutB6kGvfRfYEYELQs1zJ8_zXkY_HB4SGqdiRsfGvtoXCEhZ76AyrmKfAVg7nSS2M_M8fIfA-zL5nIERtO0Mh_6FoR2NKGjZgbu3NJoPd4_SaVJ-mvQ-9APblk4OtFfDdZ552zgg4aYm-NKD_J6lVobkIO6D21S3_3tZ2DApTOjEF3EmNBwSRs4do-7tUtPeL1vssonsdlhtiXysqdH6Jud11HOQ2rx3MjHpX35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارک کلاتنبرگ: گل استقلال خوزستان به پرسپولیس صددرصد آفساید بود چون مهاجم جلوی دفع توپ مدافع از روی خط رو گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/138646" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138645">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
حسن اکرمی داور بازی پرسپولیس و استقلال خوزستان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138645" target="_blank">📅 09:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIaX4LBvQwZU3bj37LMGc15HSeJe8nEDnpuEsvlNSryHVQZoQT11TvvvRmIDr1peRarhTPpYl3AbyiqX3SGA81HCF3GXBk0ZyFZ_ue-h3liNKc-5N7hW9m0MhdvalmAySolel9GQBjzTW34BDla-rVEhXdQBOoL6Yf82BuN0TBkfYDdn0_aj4ygStX_zHnVf8y2TzdQYv5b9cwSf44fGSyGFqFkcDWCy4mxmIP8J2QsrngDQS1Tg3bpUrfZbj0lIQjpNE3SOATli2uor7O_nPrH8uVudtJPIx4UCpro9bViMZR_UjJjyN6dTfRjAyYY-BqKHSwq6NdtavaZ_APwQ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر خط رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/138644" target="_blank">📅 08:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/138643" target="_blank">📅 08:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">➕
دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
➕
اسپورت‌نود کار رو از طریق ربات مینی‌اپ ساده و راحت کرده، به‌راحتی میتونید پیش‌بینی مسابقات ورزشی و بازی‌های کازینو رو انجام بدید!
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138642" target="_blank">📅 03:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8ef11ffd0a.mp4?token=khP_q4r4HvnbsrB-rXUkptGerqR741kcbD85IBUkaAWCgzf56wONjQW8XBkfuua--rRIXsSeFhi3XUQHOcGj69CjcT14JjHXkXNQr6j_zQbXyWsOq4x0mWQBaK-8d0UPhKhxTWSki6QhZo6V9Gj1lBe8YQbOLf3L0jFEsicsAvwGJMbuRrmXfMzGa19-mS-8y8ws3DH4__KYC76C5DmVA9xx5SE5gj_URjgFeyuCyyeXuztQ9MrU83UMOzPe0eOHtUjASGAES48adHVMyRdiC3PITnVoEXmFnkVVKGvi7UYDPV6EoGPtzVKkeD6uieoTGQmD79FHhgvyP0LRF-t36g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8ef11ffd0a.mp4?token=khP_q4r4HvnbsrB-rXUkptGerqR741kcbD85IBUkaAWCgzf56wONjQW8XBkfuua--rRIXsSeFhi3XUQHOcGj69CjcT14JjHXkXNQr6j_zQbXyWsOq4x0mWQBaK-8d0UPhKhxTWSki6QhZo6V9Gj1lBe8YQbOLf3L0jFEsicsAvwGJMbuRrmXfMzGa19-mS-8y8ws3DH4__KYC76C5DmVA9xx5SE5gj_URjgFeyuCyyeXuztQ9MrU83UMOzPe0eOHtUjASGAES48adHVMyRdiC3PITnVoEXmFnkVVKGvi7UYDPV6EoGPtzVKkeD6uieoTGQmD79FHhgvyP0LRF-t36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس در پایان بازی با نظافت سکوهای ورزشگاه، کار قابل تحسینی انجام دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138641" target="_blank">📅 00:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138640">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8nSaQ1Ym2Sp5k6XRINhj-y9Gu1tCDfwuyDwJiQrYFLx1Xomfa0662YMisiM7Nf-4MmuOPQBapKN0z2iDDQGDXTdJGZKB8VodCU3PARlMg26A9CApDC5tCTSv9yzm3vcFltg96GYO59l9zKUdZd7r7wRz-QzzFyq2njAQYg4nL94OcmQNIiTj__g05NhqE3xImGc8yt11K1rDmgx_YFslqI0ZmIRKUpLQgj6clPbvlLlelzyscwHc2NyHCS_tt1g7d84PjkMjsj4p7EDRAJXn9YoD46fbCwBBfISpZIDjh0lBFbz7sliTUBSnaCDrzDT_jS-s16QPtFxXMDTCgmquA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💯
میانگین سنی بازیکنان تیم(ترکیب اصلی و تعویضی) در بازی امشب 27٫81 بوده!
✅
تیوی بیفوما با 34 سال مسن ترین و پوریا شهرآبادی با 20 سال سن جوان ترین بازیکن امشب پرسپولیس بودند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138640" target="_blank">📅 00:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
دردسر شیرین تارتار؛ ۴ مدافع برای ۲ جایگاه
‼️
⬇
⬇
⬇
با اضافه شدن دانیال ایری، تارتار حالا کنعانی، زارع، ابرقویی و ایری را برای قلب دفاع در اختیار دارد. زوج کنعانی و زارع در هفته اول خوب ظاهر شدند، اما حالا رقابت برای ترکیب اصلی جدی‌تر می‌شود؛ مخصوصاً با توجه…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138639" target="_blank">📅 00:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
#فووری
❌
طبق شنیده ها, حمیدرضا گرشاسبی برای صدور رضایت نامه ابوالفضل رزاق پور با مبلغ 120 میلیارد تومن رضایت داده و تنها موافقت حمید مطهری مانده تا این بازیکن پرسپولیسی شود
❌
❌
البته بعید است مطهری راضی شود مگر آنکه....
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/SorkhTimes/138638" target="_blank">📅 00:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obaJObN6O9l4siGSPfGcBBelJJwPxK5bKPQYIETVp16MVSr_dHPsd4n0ET1SadkCiUv3R2q87oYIiqRQNfgcNooFKOVp38G3v95FeIhIQkXE7-9ShQG0NvVnR-ecC_LZQdqj8q_BOkJ3PI4K6AZkxWmuz64D_Hxi9zTOveYOyAyDBPsMcWalwixDiFGwnETNKXDs9smsV8iInNf_vd5YMrL2-79oCkWQvz9i0HI1om6djBsrrmAqHmzhGNPak8yV5L4o4M85JxH7Dz57f-E0-hGyjJUx3gU_198Qyo5oLImV3f4suVNr-qoHTxQ8lQrw-_JO3wuHPB3YXnYTFkRrTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
صحنه‌ای که کرک و پر ابوالفضل جلالی از پرش محمدمهدی زارع بعداز گل محمد خدا بنده‌لو ریخت
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/SorkhTimes/138637" target="_blank">📅 00:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
📱
استوری محمودی کنار بیفوما  بیفوما: عشق منی محموش ؛ فدا بازی
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/SorkhTimes/138636" target="_blank">📅 00:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384e0a5eb3.mp4?token=iKTUEE92VLdKZ6nRVECQDYVrWoie6gVMQmZa50Y3shhUp7j4epSxL3bxF95FBnMUHkY-QqR07YHg_EdhChyrgx2HbZYU2kmW6NDDFgaCSpU1nD7VNsoSmF65Kt6sb8SW43BCfkpGRbugC4elfFdjYLtq2yzCOF2l25dolwYcRRQoDauAuKIjRPi4dqQcyzQRIAggTAlEuemZ_ghB1F8JT3a0eABJPADlhY77-b7MljEyFZPxWmC9SxWqF5xK57-MCS2J95_i4WJNOFgiEmo3Ejgt0V8yOM76Q2TSPJAf6xqmy_N7FoEONOrFDPUb3y5w6UMfwzhbHsfaN_9-BmOnCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384e0a5eb3.mp4?token=iKTUEE92VLdKZ6nRVECQDYVrWoie6gVMQmZa50Y3shhUp7j4epSxL3bxF95FBnMUHkY-QqR07YHg_EdhChyrgx2HbZYU2kmW6NDDFgaCSpU1nD7VNsoSmF65Kt6sb8SW43BCfkpGRbugC4elfFdjYLtq2yzCOF2l25dolwYcRRQoDauAuKIjRPi4dqQcyzQRIAggTAlEuemZ_ghB1F8JT3a0eABJPADlhY77-b7MljEyFZPxWmC9SxWqF5xK57-MCS2J95_i4WJNOFgiEmo3Ejgt0V8yOM76Q2TSPJAf6xqmy_N7FoEONOrFDPUb3y5w6UMfwzhbHsfaN_9-BmOnCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
📱
استوری محمودی کنار بیفوما
بیفوما: عشق منی محموش ؛ فدا بازی
😂
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/SorkhTimes/138635" target="_blank">📅 00:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
در یک پست باید تقویت شویم
❌
از مدیریت باشگاه تشکر می کنم و از آنها می خواهم در پستی که مشکل داریم بازیکن جذب کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138634" target="_blank">📅 00:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2_larp7NVrw9lUiUCwce6CAOVi5eDQYNZwz6d_QEBVhloGuNbZjmycTr4GZIvHC1SegqXdwCHA_j12dFFgtUxEDv4vmUe8YGCzffcdFqrDVWS-PcXMbi4hWyv3TBuVU1rt-NURtaTIhU3DvJWuDXthiE1F_dUh1PecG0Hy6h44jL9_lxrqzSbUZSC2e4pHNbizui77WL_P_wxV4COV15rGgmjYVnpBUaWQ2BNzHo7dw8eddJ9uoPFVWOVBVrNL9ZzMBSEDKlGyQH2Vx69AomK1DRAV_yveKOB21soaJtkcxx5DQouWLIH9kGSyQdyM2hZKaEIQh4CJT2zyMzTaPsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور با دو پاس گل و یک گل بهترین بازیکن بازی امشب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/SorkhTimes/138633" target="_blank">📅 23:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGUudjYerSBuYbcvFsa1uu97ma3EcoTNsdLFqWWaMa16u1H18n26sfhbXvQuOPYEPyxOKkAjSA6OBNqBbQqGfoIF8JFGzc-PZFdQGfGTVq-joK-v5zq3YVmotqhZ0EkvbqEW0L0xyx5tFYcLBfka97GLUcuIrQQTkKsDaguFHTntygfsPeJzJLwJlv1aHjBK6Ptw6jyrFgAa3tpNb-yDsPL3uHScLRjlkr3HApqysrGuBr03TdMw1f7S20nN-9sknpQMb8SGqQTP7Vdy092oTa1snGPjgzK1S3ubI-bQ1TIds_qV9xYFfE-xzbdOOPuI8Ou_nPRKq3Q2lbXsVn-4XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
علی علیپور، مجید عیدی و ایگور سرگیف با نمرات 8.8، 8.4 و 8.0 بهترین بازیکنان دیدار امشب دو تیم پرسپولیس
🆚
استقلال خوزستان بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138632" target="_blank">📅 23:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
بهترین بیفومای دو فصل اخیر بوده .عالی بودی پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/138631" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
♦️
ممنوع المصاحبه ای بازیکنان؟ در این مورد من مطلع نیستم و باید بدانم ماجرا چیست. چنین چیزی با من هماهنگ نشده و این بحث مربوط به مدیر رسانه است.‌باید به هواداران تبریک بگویم و امروز سنگ تمام گذاشتند
♦️
اینکه نیمه اول در تایم زود…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/SorkhTimes/138630" target="_blank">📅 23:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
تارتار: چون جلالی از قبل هم مصدومیت داشت، وقتی نتیجه ۲ بر صفر بود ترجیح دادیم ریسک نکنیم و او را تعویض کنیم.‌ما در پست او همایی‌فر را هم داریم که از جوانان خوب است اما نیاز داریم در این پست تقویت بشویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138629" target="_blank">📅 23:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b3360c20.mp4?token=vFmiERF2ZuRzJVrm33Fi3cUyXjyNxg_bs4flg5ZNWer1Mmqg2NpTsUBJVHbkvQQ0hXGj7qLzj4_0HQdj70uomtXu501y07METoecbT-Sed6IYsARCxWRk2EBltZ0skCeOlX6Q_8zt0oOP47ntmyDq6kzmNHUk3lJTa6edOqoFBSZJlw_nkGzxXsy_T1mUPkEFtYg2VObbhvueWGBzljx7peD4C_XvuJjgQv0ed4rXFnDBpAQB7Jo5aS1xcCaP-OyLeoSd7JjfBlFVqwmMHhe9w7_fPYWnd7ZUUQqDdLF-V89v2G8hEA2yvhhODZi4X048PeWmSoAYyna35geLy2lHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b3360c20.mp4?token=vFmiERF2ZuRzJVrm33Fi3cUyXjyNxg_bs4flg5ZNWer1Mmqg2NpTsUBJVHbkvQQ0hXGj7qLzj4_0HQdj70uomtXu501y07METoecbT-Sed6IYsARCxWRk2EBltZ0skCeOlX6Q_8zt0oOP47ntmyDq6kzmNHUk3lJTa6edOqoFBSZJlw_nkGzxXsy_T1mUPkEFtYg2VObbhvueWGBzljx7peD4C_XvuJjgQv0ed4rXFnDBpAQB7Jo5aS1xcCaP-OyLeoSd7JjfBlFVqwmMHhe9w7_fPYWnd7ZUUQqDdLF-V89v2G8hEA2yvhhODZi4X048PeWmSoAYyna35geLy2lHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
پوریاشهرآبادی؛مهاجم پرسپولیس:
🔻
امسال تیم یکدل است.
🔻
همه بچه‌ها جان خود را برای این لباس می گذارند.
🔻
تیم ما لیاقت قهرمانی دارد.
🔻
پوشیدن پیراهن پرسپولیس آرزوی هر بازیکنی است.
🔻
مهم نیست چه کسی گل می‌زند و مهم بردن تیم است.
🔻
بوسیدن لوگو؟!این عشق بچگی است.
🔻
رقابت در خط حمله نیست و رفاقت داریم.
🔻
تارتار پرسپولیس را متحول کرده است.
🔻
در مورد وضعیت تیم امید و باشگاه نمی دانم و آنها باید حل و فصل کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/138628" target="_blank">📅 22:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb8538e6b.mp4?token=oghOdsYHDp9yQgYhTVg8JCaobYZ9uk1I-DcKtwvHTU35_qVIoNB7KPs4CVlf29vxlelO_B_AQNvyVAWRVDJKQB4oq8L5NXDomXJizPjpzWLjCHcX9Nu3jiCe41AZ7nWSfCVcXzJZNEKPYBUeLAdwKCDHoXZpFmgD0vtrFi5SQ0XTT8e6YOqO8qWmAomkC89vhiFN_VlSJH8Zu-I_F2X6nzuyhz90GGUriowOxSbTz-IfjR4BweUBDn9FiX6FLeL-mRsVRynEhdOIjOuQ7jSQqNUxidRrv14BT9fqPI2V51Tcuq1CiqN2rJ74AoIu4E7N1Qjq-qZ6SSFEgqbBpgE-Njfr7aXBDuguzX-oM3uCrhoaV0Ez9UjuwM8K5X2XFrZcfqwOx9qBq745H4ZxOimiidTu9TiUhipZAacueNvshKLBDYORx6gmDC-56xEJaISeJL6H6cAKyJL9imd9axYgDQPvP-tuqMZAmIq9GDkA2qxmjt8n8ngApDAY_yMhGiUdU8W5p4fi7E5BtVmqXmqDPIYRGVAlWiRN9BfYZ8OD1P3XEx_wdE73PASsGPem5lp71BZpOCz49ehsd-ncalH81FkXPzDMSqNdXwBhzYFfhDPmq-xD67WRtbyn1CyTeMNxIT73gMUUgaxD1YRyfels2mA8ZtYfYzP4Y4xpiLRoOyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb8538e6b.mp4?token=oghOdsYHDp9yQgYhTVg8JCaobYZ9uk1I-DcKtwvHTU35_qVIoNB7KPs4CVlf29vxlelO_B_AQNvyVAWRVDJKQB4oq8L5NXDomXJizPjpzWLjCHcX9Nu3jiCe41AZ7nWSfCVcXzJZNEKPYBUeLAdwKCDHoXZpFmgD0vtrFi5SQ0XTT8e6YOqO8qWmAomkC89vhiFN_VlSJH8Zu-I_F2X6nzuyhz90GGUriowOxSbTz-IfjR4BweUBDn9FiX6FLeL-mRsVRynEhdOIjOuQ7jSQqNUxidRrv14BT9fqPI2V51Tcuq1CiqN2rJ74AoIu4E7N1Qjq-qZ6SSFEgqbBpgE-Njfr7aXBDuguzX-oM3uCrhoaV0Ez9UjuwM8K5X2XFrZcfqwOx9qBq745H4ZxOimiidTu9TiUhipZAacueNvshKLBDYORx6gmDC-56xEJaISeJL6H6cAKyJL9imd9axYgDQPvP-tuqMZAmIq9GDkA2qxmjt8n8ngApDAY_yMhGiUdU8W5p4fi7E5BtVmqXmqDPIYRGVAlWiRN9BfYZ8OD1P3XEx_wdE73PASsGPem5lp71BZpOCz49ehsd-ncalH81FkXPzDMSqNdXwBhzYFfhDPmq-xD67WRtbyn1CyTeMNxIT73gMUUgaxD1YRyfels2mA8ZtYfYzP4Y4xpiLRoOyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
♦️
ممنوع المصاحبه ای بازیکنان؟ در این مورد من مطلع نیستم و باید بدانم ماجرا چیست. چنین چیزی با من هماهنگ نشده و این بحث مربوط به مدیر رسانه است.‌باید به هواداران تبریک بگویم و امروز سنگ تمام گذاشتند
♦️
اینکه نیمه اول در تایم زود به گل می رسند جای خوشحالی دارد. یک گلایه ای هم از داوری داریم که امروز تمرکز داور در 20 دقیقه آخر از بین رفته بود. خطای روی عیدی و توپی که به دست مدافع استقلال خوزستان خورد نیازمند دقت بیشتری بود. همه بازی های پرسپولیس سنگین است و داور باید دقت بیشتری داشته باشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/138627" target="_blank">📅 22:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0042859545.mp4?token=Ofb5CXWtkccsGhlU5ydp-AZlbeRvSxQu7S_MRjQoQn1xlfZJFerIXhHRFwoHWecpPYcGCXnbXCaLW0mkJX8iWL4T617OSWKe2Vdrqf4Etej7fTPSqIYOhnlbL02RcwkWstj4y_oWvIEOC42ldcLp8-wLBv9qKv318no0a4nOcfuNjyDo8ZkkYGdLx-MUT12WYCyRP1frwAfuTZvroCrC1Ub75i4cB5t5pFke1thIJdc9HPi2AP49Ts2HIaLMyEanHRwk2iM01ynL0bvFu5FrNES4d7D93kOxyodY-vcEmNy04CxruQ5yy4M0UompI-HQQY9Ci7DUxvEr3f2dB0bN3Tf3-irm92YX5CrZEZHx7-9QCQpFfVZ4AGo2aBL-3fPMOUcVsZeG-y-LmlyiT9M7wr4fDF4xhc5nCXA3SbwHhcOscwEl8QuI_xyTRg8ULKG7ZpL4cDtWVmh69j1sjF3fQkIalXCDXWBRtycp6ZtPCZa6uOxNOxE0PVUyddqmBb4_kWNpuuS-7O3mXV40T6mZrQbp8rFlubB5BgGDTtwy1UQRgBDLbTlVRIzDe0HcTaKEzsVXQe-NYVf9oVIbJYNq3TL2DyYQypb_WK8yoYMwxAdysKlCT6jZRY8ARzJJjDaqGu3wSJp9f1eSgUSCrF0UcPCHzl8gb6RClXSYuS3PezE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0042859545.mp4?token=Ofb5CXWtkccsGhlU5ydp-AZlbeRvSxQu7S_MRjQoQn1xlfZJFerIXhHRFwoHWecpPYcGCXnbXCaLW0mkJX8iWL4T617OSWKe2Vdrqf4Etej7fTPSqIYOhnlbL02RcwkWstj4y_oWvIEOC42ldcLp8-wLBv9qKv318no0a4nOcfuNjyDo8ZkkYGdLx-MUT12WYCyRP1frwAfuTZvroCrC1Ub75i4cB5t5pFke1thIJdc9HPi2AP49Ts2HIaLMyEanHRwk2iM01ynL0bvFu5FrNES4d7D93kOxyodY-vcEmNy04CxruQ5yy4M0UompI-HQQY9Ci7DUxvEr3f2dB0bN3Tf3-irm92YX5CrZEZHx7-9QCQpFfVZ4AGo2aBL-3fPMOUcVsZeG-y-LmlyiT9M7wr4fDF4xhc5nCXA3SbwHhcOscwEl8QuI_xyTRg8ULKG7ZpL4cDtWVmh69j1sjF3fQkIalXCDXWBRtycp6ZtPCZa6uOxNOxE0PVUyddqmBb4_kWNpuuS-7O3mXV40T6mZrQbp8rFlubB5BgGDTtwy1UQRgBDLbTlVRIzDe0HcTaKEzsVXQe-NYVf9oVIbJYNq3TL2DyYQypb_WK8yoYMwxAdysKlCT6jZRY8ARzJJjDaqGu3wSJp9f1eSgUSCrF0UcPCHzl8gb6RClXSYuS3PezE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
محمد حسین کنعانی زادگان، کاپیتان پرسپولیس:
❌
❌
من به تک تک استقلال خوزستانی ها افتخار می کنم و بعد از بازی به رختکن آنها رفتم.‌بازی تراکتور و درخواست برای حضور تماشاگر؟ فعلا بگذارید این بازی را بگذرانیم و بعد کارهای لازم را انجام می دهیم
❌
❌
ناراحتی اورونوف؟ اصلا چنین چیزی نبود، در تیمی مثل پرسپولیس بازیکنی بازی نکند طبیعی است که ناراحت شود.‌هر چه آقای تارتار تصمیم بگیرد همان می شود و تابع هستیم. گلزن تیم فرق نمی کند، من دوست دارم تا آخر فصل گل نزنم اما پرسپولیس قهرمان شود.‌خوشحالی من حرکت موزون نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138626" target="_blank">📅 22:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mpgfm97_eCa_rzl_ns-bADAXDiI5uwIhu7aSo1pmCSbuyU87M3BLXONYtkQx4igmJ7oeZWEYqEKvXpAlh5gVWhNgcRAyfQ9mtLEBASKva3DN_VULAz9xZ3FxU1gflDl0MPNaKJIXdj_1yK7Ggo0EZsEtyXVStFK-YTczWGbxXFi1h0rVZy0r4qHBLCEgSHuycTOiB278A1mwNu6Y5ELI-uiha4Am3RE20VB9PGO_UuNGuyCuHF9l_AzMx-q_vcxAncmV6ijYKZvI9G2dVJueHHOhEXq0oWhz1dwxAfO-Q3DCFqWfqoQEMlcDY4mHpukkDS0hqhJNu7OOFuexhmpp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول لیگ برتر پس از پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138625" target="_blank">📅 22:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
مهدی تارتار، سرمربی پرسپولیس:
❌
گلی که خوردیم از شیرینی برد ما کم کرد
✔️
✔️
دوست دارم هم خط دفاع و هم گلرمان جزو بهترین ها باشند
✔️
✔️
از جلو خوب فشار به تیم ها وارد می کنیم
✔️
✔️
به جز نیازمند درون دروازه رفیعی را داریم که خوب کار می کند
✔️
✔️
دلم سوخت که…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/138624" target="_blank">📅 22:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138623">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✖️
✖️
مهدی تارتار، سرمربی پرسپولیس: بازی با تراکتور و درخواست برای تماشاگر؟ فعلا می‌خواهیم امشب از برد خود لذت ببریم
❌
از داوری امروز توقع بیشتری داشتیم! در صحنه‌ای که علیپور به سرگیف پاس می‌دهد مدافع حریف توپ را با دست می‌گیرد!
❌
داور می‌توانست برای ما پنالتی…</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138623" target="_blank">📅 22:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138622">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یکی از نکات مهم اینه که فصلهای پیش جلوی تیمهای ته جدولی امتیاز از دست میدادیم</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138622" target="_blank">📅 22:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138621">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">یکی از نکات مهم اینه که فصلهای پیش جلوی تیمهای ته جدولی امتیاز از دست میدادیم</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138621" target="_blank">📅 22:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138620">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
✔️
✔️
هدف ما از اول این بوده همه بازی ها را ببریم. هواداران پرسپولیس این شکل بازی را دوست دارند. بر اساس فلسفه هوادار خواسته های خود را جلو می بریم.‌در یک پست باید تقویت شویم .از مدیریت باشگاه تشکر می کنم و از آنها می خواهم…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/138620" target="_blank">📅 22:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138618">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/138618" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138617">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
مهدی تارتار، سرمربی پرسپولیس:
❌
باید از هواداران تشکر کنم که در برد امروز سهیم هستند.از بازیکنانم کمال تشکر را دارم که از دقیقه یک فوق العاده بودند. نشان دادند امسال می توانند کارهای بزرگی کنند.استقلال خوزستان کادر و بازیکنان جوان و خوبی دارند
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/138617" target="_blank">📅 22:26 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
