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
<img src="https://cdn4.telesco.pe/file/koodlvyLFsB98w4LTMLm4g3MYPYW9NiNGxEE04oRSltRWCdgrxxlFQdb4czpJbu1TT4YDuPtXYJkkuMLvZdR3lThlHNMC76p-TL5Dn2LHUBMYBfdlcIZUvursf0Js7tSM_994se-ol2z_20vngoJoKs89KUMXTxLE4MHCpzFsiHcVP3VaAQgph2gbMFV36TWpNprHMz5zUCepCEjqazbfSUWZBoOjv-YuNNZqDS9fuAW5w2rFzoOWdZcfb1ZPLwR_GrZpMIf5uqZF7GQYxrICaIrURDbIBbibrrDB-rbyp5-SYslPYIrVEM_F4HTDTxqPBZ_tbeJlmYHysGOKAJFuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 09:42:44</div>
<hr>

<div class="tg-post" id="msg-139794">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✔️
دکتر حقیقت: ما کارمونو بلدیم نگران نباشید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 646 · <a href="https://t.me/SorkhTimes/139794" target="_blank">📅 09:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139793">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=UQvFjPy6PWQVx2YDRGkM84y8ZuiDnaf_pch62Aiw5idQbl4GIToUJikPreQxJe8EnXli2_QEmDgnuAdRn3W1fDbvQOEyzULD_BRq8lHhP7MqisvgZ3lewqd67zuTl3h7o1rhbDCmja8TpmJ3WOg4XwTyfD2n146-hBqtKQmEXOXRSGm8CYKAMvzHBYAw1qEpt189NTgEP_mHMhze7mcRJqURl4XR9ulO-fX4bLIwWexpdG4yJ98vY1JPu8TxmprwCChOdmF8haYJ1sR_bu1rYw2odkC4gn2wNlrhNB-_B5m5NEJTvFqMhrjC6kNhqiZy3fOANMpUPVo9RfhlDNz5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6dd97ad3.mp4?token=UQvFjPy6PWQVx2YDRGkM84y8ZuiDnaf_pch62Aiw5idQbl4GIToUJikPreQxJe8EnXli2_QEmDgnuAdRn3W1fDbvQOEyzULD_BRq8lHhP7MqisvgZ3lewqd67zuTl3h7o1rhbDCmja8TpmJ3WOg4XwTyfD2n146-hBqtKQmEXOXRSGm8CYKAMvzHBYAw1qEpt189NTgEP_mHMhze7mcRJqURl4XR9ulO-fX4bLIwWexpdG4yJ98vY1JPu8TxmprwCChOdmF8haYJ1sR_bu1rYw2odkC4gn2wNlrhNB-_B5m5NEJTvFqMhrjC6kNhqiZy3fOANMpUPVo9RfhlDNz5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🔴
دو گل پارس جنوبی به پرسپولیس در دیدار تدارکاتی دیروز.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/139793" target="_blank">📅 09:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139792">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
سلام صبح همتون به خیر و شادی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/139792" target="_blank">📅 09:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139791">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR-AajLv4TppZ6DmY--0udn0SxkohvLGCLyOnBUJQX_TKFS1gcP9hGjkaNKuP-CHEF-ZxIe1HBPAmC6whCg8-CxgW4Q3JNBPEH_Be3mLAqIt-ArdMK0Djro4XaJ_DcmZmf4Oq_c-7Vlw64wqEKN6bs7xygDRoAAGivCPRPpoS3wrIaylKX5E8u-HFZYNMOm0vuELDYah7G-tAMTeFom39cSlKfVakK6WHq4Aqo5WrPyoAa4HhMnvFRLR2wcQytugLR75x8ucy9LBXA6wFlK-qisYmbzql4N1hmfQoBM0z_gpeUfysGxo7_zEBvOunv_J4C8n1k_Ofd-en6Rvfil89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نبرد قدرت و تکنیک؛ در یواس اوپن
🎾
Ben Shelton -
🎾
Alcaraz
🎾
آلکاراز از نظر کیفیت رالی، تنوع ضربات و توانایی تغییر ریتم برتری محسوسی دارد؛ در مقابل، شلتون با سرویس‌های قدرتمند و بازی تهاجمی می‌تواند فشار زیادی ایجاد کند. اگر آلکاراز روی سرویس شلتون موقعیت بریک بسازد و وارد رالی‌های طولانی شود، کنترل بازی بیشتر در اختیار او خواهد بود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و با ۱۰٪ بونوس اولین واریز پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/139791" target="_blank">📅 01:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139790">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
زارع: جلوی خیبر نیستم ولی تلاش می‌کنم بازی بعدی باشم  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/139790" target="_blank">📅 00:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
زارع : حالم خوبه به زودی برمیگردم،  نفهمیدم چیشد پام به شیار های حموم گیر کرد و بغل پام پاره شد و بخیه خورده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/139789" target="_blank">📅 00:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139788">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/139788" target="_blank">📅 00:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139787" target="_blank">📅 23:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
شرط سنگین گرا برای جدایی از پرسپولیس
✔️
✔️
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از این بازیکن در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
✔️
✔️
دراین‌بین گرا برای جدایی از پرسپولیس خواهان دریافت…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/139786" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
بازی رئال مادرید و اینتر هم شروع شده که رئال  دو گل زده تو سی دقیقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/139785" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139784" target="_blank">📅 22:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXUFnqnNnHxJJGCA58yXSDjB9YDU3nj-wHn7gnB6tVstOe-2sSz9zoyCAlwBNnSLvdH4KjKe2pdVyrwoxDG0x0hruOz9tYcw3XAjIuxJ01xXpkCeKSsG-2MeXMQR4VRVeBh38bdaTxLWFs31Ipabv1oHxMwmhZCBtFHnBrb-hcSXb5u2ka4YRvdSN4Rog3lS_R-1qKJ_hgoOtbhD32yDRQuDDENvK8RTOXgnAsVLpny_eo87izeeDFJ8kv5tfIAvUzircP1ABCRPGNFilEfGHJaYdnst56NlX9qN035y6Z438Mx_82cucLW0xAdG5ikd05fn6LxrmoMMNBgisNCL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139783" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLgVa0Nj_0D2jA0NXbXLWbUnId-hhbAEwOKHtI5KasQPk8aFsEm_rxsadpYiwQBD8FHEMx0mE6pda7ElRz949TnE3yyIvkFmQyyZDMDaHYCcB4bNo9hJH8kfj6DD4kFwQoamwnDyeNhnbxqBoz_H_I03ZJlrH9vuDGnK6VD6Rbe8okj41oLteSWTrg4F5fyY403f9SCSdu9lyhD9ixTpoQsNyZ1Mqn2zpRr1RM5RIIP12jcUcYC6dVDfND7rsEzsorzgffz9olzMI9SOvV7MvS95sX4HKQgTxeTrzADFqhAhJjJ541y4MSapDnrsle-1JjwavAXedUGfqQwluL1kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139782" target="_blank">📅 22:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
فووووووری
🔄
با اعلام سازمان لیگ؛ فصل گذشته هیچ  قهرمانی نداشت و یه موز به استقلال رسید
😅
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/139781" target="_blank">📅 22:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139780">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: پارگی نسبت بزرگ بود اما سعی میکنیم به بازی خیبر برسد حالش هم عالی بود تقریبا بیست دقیقه پیش مرخص شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139780" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139779" target="_blank">📅 21:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139778">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lnm-ZvgAQq-Vt2IbvL65FfE_7LzdZBeyzTzLujoRzGhV1hIHDpuZ8kgCkWRqZHDlgSh4bup_V7lMqkVPH7KYyXQqRar-EFZdmtAZbGUsZMoy9Rbij3VyCHLjZrh1D11YrFOwXQIgvykrdcv3YFMhXfrJkhyJ_fjLRLAKYpWmPP1C1RQiRFG-z7u8MFrQxRxRSF1pYn612oOk9m6JdzKKTuCjL8XbfuFjkKiXb9R2EwU6HNF6yvL-TETOHWep92XuMj3cGJucmNgWY3qYxH5Rn9DmO2zzTDMrlb6GWTJtb62iFa9RwYKg0YbznuR2sm4XP02BBEpbN-IxsLVgNPSEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
💢
پاسپورت ۱۲ پرسپولیسی دریافت شد
💢
پاسپورت ۱۲ بازیکن پرسپولیس برای انجام امور مربوط به تیم ملی دریافت شده. نیازمند، کنعانی‌زادگان، ایری، زارع، لطیفی‌فر، محبی، علی علیپور و محمودی، هشت بازیکنی هستند که نام آنها در میان نفرات موردنظر قرار دارد.
💢
همچنین احتمال حضور محمد خدابنده‌لو و مهدی تیکدری در این جمع مطرح است، اما نام دو بازیکن دیگر هنوز مشخص نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139778" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139777">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/139777" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139776">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139776" target="_blank">📅 21:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139775">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acWNX29u4trm79IsWi3qDl2JagXQODWvYSNOC4Cfc7I-KA_ybF58a6lyttuW1bn_4g8VpMyjsQhWbDIV7UgS9f-sjuICdaOMWtOMotdcU7KJiEtfYTruu-8PrEV2HDMuL8mrjbf-peWjy69GVEoQpYBHMP3jQ1CelFbij8YscSwQ_3LdJ-ARrqUiRXq9Iyb5n8LB1wUGBe41L_Zf2lvj8sVxIUYUJfzwOoI2_2AzpJLEg_D53s8zRV_5RyNkTY70LMkng9ZPMKe-goa9PPze5ttkcvGxswB06_bvUXYv0IVy1qtHQ_O1SilFB7MP7YWAXD4QgY_PFNtfiYy5p2Rh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تارتار به ابرقویی آماده باش داده تا با تمرکز و آمادگی لازم برای بازی با خیبرخرم آباد آماده بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139775" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139774">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PFYnWkcURelLpB3vGAdRSnDL5M2ySUGUEEMteSSiYBr4bINUkDCbgMBsRFIPbNpddiT9IliPt7hu2j999r4gqXf-xru8Wgrp8RdFEcIQrZ9D95mwU3Yp-86eV3ufN7mAi-evycNMQV08dtzZa3h3eMQ9VZ4OIiv1UKI_au9a3xPn0bJfnhl-uNW2qJx9dHDlGmIpS_Qgprb9AMdNl1TyRZPSELe798oDSEyn6KreG_xfLke2_mA-JTpKVqbgPH-uiO3N2dxTMvcQOkBIuWCicD9feqkmDelABSRvMncoWqkK5SfDr-BchJ12gz9xguS_vSoc7x75_ZjPRpn3Utp1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و فرصت‌دادن دوباره به پوریا، شاهد درخشش دوباره این بازیکن باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139774" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139773">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAcQhwCMkN5f7TcUlm_XuRpJyYi0JPSjkRmSX1pnD0v1ypiqQ6ljTgZ0XHyv61Ly3kHet4EdKQVxZjT4CN9d4DqeXtJce8THD0eUJ7plPsV0sSi1ruC22Q760s2d0LiNAkpF-CP5ZkRtK5fqOeJPvwE60rMd6iygesmMqUFO2Z24_rAV7-J0WvrvclvYDzaXzGwk-I8Kp_A0QgpB5w20PGXbg0VLXx_ZU98IOQDW2c1vkZnwDtjlyruqVgO1ArwxznEUVHYgpI8pnRLI99q-JhLt45epVNZPHH_1sn0dLxKOrAc9Wkc95GdqP9KnKTIQsg-uGnpw73msOPaPQmiaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری بازی دوستانه پرسپولیس - پارس جنوبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139773" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139772">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
با توجه به مصدومیت محمدمهدی زارع و غیبت احتمالی او در بازی بعدی، ممکن است پرسپولیس با حضور دانیال ایری در تیم ملی امید مخالفت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139772" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139771">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPNn1c1pPOejTPHzIEhnlYE7IihnkJg1s7-oG0NgbvzyrtXiSMZSX26ZtHiOSsM11eLygm8WcXCsbvKQMxBGO1c5wwrTjsZAy-Tpl67hKkMUeID1tww2ajzTxjmFg2zDJ0t9OsF9GN0gpCqqh7fRhXCHFGJQb7ksEqvB3rK0CwvRcJsTsjt2wK4Qi4LrNjPJYmrTMhC0PwBEr56hmqsVpC1VDtSz2wjiy8UkMXLiaU7QhaCLHi1QBKqZK6eu-LLVlrUUfH4-U9tSj7j-vF06By24OTyyGc-EgApjHgfP9AGfyGNIWKnX-GIahrSjhvf0Xiu9UgCC1vpsivQ34wRWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شب‌های باشکوه اروپا در راه است!
جایی که رویاها، ستاره‌ها و جاه‌طلبی‌ها
برای فتح بزرگ‌ترین جام قاره به هم می‌رسند
.
⚪️
RealMadrid -
🔵
Inter
⏰
Tonight 22:30
🏟
Bernabèu
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
⚽️
برنابئو در انتظار یک شبِ کهکشانی
رئال و اینتر؛ کدام تیم پیروز خواهد بود؟
فرصت رو از دست نده و همین حالا وارد وینکوبت شو و پیش‌بینی خودتو ثبت کن.
🔗
لینک بدون فیلتر وینکوبت:
👇
🟣
wngd3co.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139771" target="_blank">📅 20:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139770">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139770" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139769">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139769" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139768" target="_blank">📅 19:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🤥
🤥
دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139767" target="_blank">📅 18:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
بازیکنان دعوت شده به اردو  تیم ملی بزرگسالان از نگاه ورزش سه
✔️
پیام نیازمند
✔️
محمدمهدی زارع
✔️
محمدحسین کنعانی زادگان
✔️
مهدی تیکدری
✔️
محمد خدابنده لو
✔️
محمدمهدی محبی
✔️
علی علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139766" target="_blank">📅 18:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139765">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139765" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUl4TqMyVxu8MF92cwyqlqpvZiOYBu_IsEDodKr2rAoAroUWSTRgt5e4UiFHYVaQtxdafqXdRwPX_EncDijOhruWkr8Anvv3Mk5HwAWgtkDx4vVQmDwwzar8C7IBI-S6qDtjanTWD-2aEdKVkJ2vbURJt0rPYIuIIpA20arRGpF6ACQdN8UMvRbI_zXKppXbvW0acwR0qkzWXMfrYdzgsqng3TQUDAlxqvmMcPA0dATrrJB9WaLJ8FJrW9VmPN3NZ8cCRi-be52e-gIalDVLwiy7pTAx8YyknwSfvLnpeLC7CvKC9bdWwtLUyMnL7CgzcXv1NpBACtCaH_x5GaAO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139764" target="_blank">📅 15:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMjbA3Fy_NYh4UUGiOQT0zRBIZBkfYoVes2s8wNvyYDg-3-gwwG2oN7uAqErhMIPoXM3hZaD3BwYNbJZISFzTrebBcyOIPmk-X10H0nSOHSee4co-U2l5uMddOOcRKnjCs7KBMF6yJR1ET60_stLKDNyuj_jqUHQI-f7ITcbalV0ts-YZs2ym98_gcpQcxiBfZzKhDvq4SC4iP8ZdvbcWF6lqcg8mDVdnVGkil-4lN4rjwdlYpsHhxWCKcMQ4Ou9JNdjlEEYWLyLkSmVPTj28ej3Fm5ty1q4OsE2GKw7fawzvy-RFVko0zP7jI77Lp6DrOH3zds1JYb9Nv-CSARJdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139763" target="_blank">📅 15:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7ifI-G8Q74PuxLVi6ui4YM0oc_r5tueM_8CqbuFvW_ABdYgqbxhcUZWjcb82VrasXdGKAoO9gaXkm2ES366EPsdzzTVwYFlP3CewAQM98vtDbKqC4aDvrmR18qBwpo75M4F6GRSHr8eA4aTBNnpQl1NXLDJIfym4_g3LIUpjvcA9MnS3rA0ETyORn4H32E3Z6JLmBzoYCkZeLRQN7Qk3hd8oI_bC1doG94_rtmPLJ2W2rNZzwKa9k3fPlii7tK0hpVjSFT05l0YVxzQobCmjw3t9sgsqiC4GsE31k_BeS3ZPT9DgrL7ZIpUvA8_JzkF98chVKrwaHSV7lFGvNIOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🔴
میرور: فوتبال سرژ اوریه به پایین ترین سطح کریرش رسیده و می‌خواد در لیگ دسته هفتم فرانسه در تیم محلاتی مونتینی-آن-گوئله بازی کنه و انتقال اوریه به دلیل تاخیر در ارائه مدارک از سوی فدراسیون فوتبال ایران به تعویق افتاده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139761" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139760" target="_blank">📅 14:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/139759" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❤️
❤️
بیفوما که به تیم ملی کنگو دعوت شده بود دعوتو رد کرده و گفته تیم ملی من پرسپولیسه و به تیم ملی نمی‌رم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139758" target="_blank">📅 13:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139757" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2FsqLXzCjyKrziXD8WC5ehB5dbhWb93LZDepPD4asL2eH_lk60Nx4bbQsh_2YOZV8nxjngogaTRbeyOg8vvH_p7JDT_btAUYXFkYdfIp-BYtWp_Z0a57s8oY9snDseqpMEu51_e3JezIcrdFjVTnWceIRKi81FPtayUUFl-0OIwGJRkl9ezAfnMEW_xjaQarZjtysfPL8tDay9Yvv-c7ejewMypmAKfQsmBLpMxiGjRpn7OzuYPfmg34nwogNVxwah1hey-5NOg5n59PVMQUeVgj_USFNbm1jfUo2GXITlR5gTHjtG1SyfnWpZs9oVDez6U9ZDjwtivwLBIS11JeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئال و اینتر؛ دو غول، برای یک شب بزرگ
⚽️
رئال با تجربه و کیفیت فردی بالاتر، اما اینتر با دفاع منسجم و ضدحملات خطرناک؛ دوئلی که می‌تواند تا آخرین دقیقه نزدیک بماند.
[
رئال‌مادرید
⚪️
🆚
🔵
اینترمیلان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139756" target="_blank">📅 12:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139755">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139755" target="_blank">📅 12:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139754">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139754" target="_blank">📅 11:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139753">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139753" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139752">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz44KYSM7vh6KMAtgEUCBS3GlpF3pxfCVnJnuwGGFO01WHDG9YrZQNjHEf7wYjv3f2XGdd3Sugl1PvaxQeoXChvRw7sFEoXgZJx1aip74PGXykqopVEleXoREsKVyqJy-eYL2cTzf_vBX2GYb7ysUiU4f-5hmucxjopsbmKy9uwIz-YCfX7glKhvaWs6nQ1rU0ZGBfrlfvPNKQT8asizG-L1LBz5zklCe0bgtzYcs41ePJO7yITizyVvVuiKyKORYyhGwstMgntnfe-4-IEYuWhsnaKyEmynR_C28m4-HmwGWckV_Z1Myu8qpGgCgx613z0kxF0UkNFBl5T0eOrJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ایری در پاسخ به یک هوادار: تا روزی که جبران نکنم، شرمنده شما هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139752" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139751">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139751" target="_blank">📅 09:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139750">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139750" target="_blank">📅 09:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139749">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BW7X023IptCDJSHHu8J30J1hSnQ1ZGTOK6EokIzn4zm72-Itd7OSxsvF5DpqS7s7JQiU2fFH4SIYwLmMQTJk6zt0zQZXIj3DnNhEioM9Y95IV9xGZK8evd1Lbl_NTEPHSUh2Qq3KXe8IbWyG5OXex1OsMkzM5APgWRJtDC8DjuPuapjpijiVHgVT1ln8ZKuClvd5btcFy5_MU-V1QpxdHOqi3v3x9Gp3SpbqGkcpIz5a6Et83MBxR0A18K9O6WNwpmzXs_RuiU4E-E5dR4bFS55bl0f0Oe-iq0OoJ-Vde-3HqXjJ9GYinkDc2K4R9_jDVeEeNAF4SvQB8B8mRqwOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139749" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139748">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و اومدیم دوم جدول و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139748" target="_blank">📅 09:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139747">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKsAFwUmAfgqsS6yDQk6gx346q-GGPQwgB85_DnPC9JyJ--jljjnvDSPKEIKMn4nfC-mXj28_LYHT2hPr8xDCaT5glFPO42ncC7m_Z54waeT1OhDlTNf7xxEXFF0MItX09favoN61MifeeGiz4iiJTMvmmZhTc3dmQgtQ2MnjClBs35_6GfAuoOjZQkNcc4VQOiUG7QtMOryPPk5j2c7Cc1qJ50XJO5C459ohuNsCHIvWAH7QQTCDUdjzG___WwGq_B25thxzJnnwrgm13f6L_99cElfM37GxU5OlgeG9mw3v2kujacAGAkTweCATR1LaDuzJZG4ztPolidDo8m9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال جذاب در یواس اوپن
🔥
[
الکساندر زورف
🆚
لوسیانو داردری
]
⏰
بامداد سه‌شنبه ساعت
۰۳:۴۰
🎾
زورف با سرویس قدرتمند و تجربه بیشتر، شانس اول پیروزی است.
داردری با سبک جنگنده خود اگر ریتم بگیرد، می‌تواند زورف را به دردسر بیندازد.
با این حال، روی هاردکورت کفه ترازو همچنان به سود زورف است.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139747" target="_blank">📅 01:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139746">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
✔️
پیراهن پرسپولیس را بپوشید و به تیم ملی برگردید
✔️
در دو سال اخیر گولسیانی ، گندوز ، باکیچ و بیفوما از پرسپولیس به تیم های ملی خود راه یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139746" target="_blank">📅 01:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139745">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139745" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139744">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139744" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139743">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=N-c2iBEQmt8c6AjqcIc0BE2bjOx0pMTSC34t-mIQQwoSO-T792BWa2ijSCiouN8izOjXL13t8ityzYMb0fdyq_gBhmhopelbm9H2iAkH4sjpKMRAlWjL7H3P9oGf_ePz1_1CXtBWXbHqZy3sE5L7GEBy-_NntC6bzPe5Qk4jH6yDxCdd-eWVEPGvSez3tQdbSpZMlzesWbmCogTdpBxJANT1K5GoRuK6PSq_4nMT5_lWCBm0b8ef2-EbyKmENoB4HjKnbvwALRe1BoqTUEUw2ml-nqW9Oir1WpuTBK8ddYJ2y9dKAt7cNfkQMcnwPv9y_piObUzm0bZLRprxxJFzkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=N-c2iBEQmt8c6AjqcIc0BE2bjOx0pMTSC34t-mIQQwoSO-T792BWa2ijSCiouN8izOjXL13t8ityzYMb0fdyq_gBhmhopelbm9H2iAkH4sjpKMRAlWjL7H3P9oGf_ePz1_1CXtBWXbHqZy3sE5L7GEBy-_NntC6bzPe5Qk4jH6yDxCdd-eWVEPGvSez3tQdbSpZMlzesWbmCogTdpBxJANT1K5GoRuK6PSq_4nMT5_lWCBm0b8ef2-EbyKmENoB4HjKnbvwALRe1BoqTUEUw2ml-nqW9Oir1WpuTBK8ddYJ2y9dKAt7cNfkQMcnwPv9y_piObUzm0bZLRprxxJFzkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139743" target="_blank">📅 00:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139742">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=fwI8wJHOHN7CPzcl5IjAZt7_X_zKNR_Yk0TR4qbWdAHv4_P4F7IfrLUSRC_OZv1yGkCscSxhfyFhoqFoDHFvrVXTvg_rpDDJyEojmFeaBClLHiWAaoEJlX4emdC62xTv-jGg2-Lv-M9rEU4vQ2TsfTt_ds8ke3Qriw3FmQ54afAzeqHg5nlxyT97gzKnkuM6hgWX3JaIkI0TNcFJg2o2LUjTPY1m-HR6cEUFtFnH5VD7YpwM_l-9vx9N_Z0JFgpWbyYVVuN9hdIFTtxkUBOiJJdHXOWRQeXvhBt6h1cKlivaDi_ly0T7Rlbm2rcfvjgATVBUjs7mD542Ls4Dhh_gwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=fwI8wJHOHN7CPzcl5IjAZt7_X_zKNR_Yk0TR4qbWdAHv4_P4F7IfrLUSRC_OZv1yGkCscSxhfyFhoqFoDHFvrVXTvg_rpDDJyEojmFeaBClLHiWAaoEJlX4emdC62xTv-jGg2-Lv-M9rEU4vQ2TsfTt_ds8ke3Qriw3FmQ54afAzeqHg5nlxyT97gzKnkuM6hgWX3JaIkI0TNcFJg2o2LUjTPY1m-HR6cEUFtFnH5VD7YpwM_l-9vx9N_Z0JFgpWbyYVVuN9hdIFTtxkUBOiJJdHXOWRQeXvhBt6h1cKlivaDi_ly0T7Rlbm2rcfvjgATVBUjs7mD542Ls4Dhh_gwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
حجت موتوری: ویس های فحاشی خداداد را دوستان اول دادند به شبکه های معاند، اول آنها پخش کردند
🤣
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139742" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139741">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139741" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139740">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139740" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=ZkwND8appWHZMDhDAB3BIaABiXyUjhvzVBMIbo0Q69T39BGH4vfwafRk1-1_uVvwv8b2KS0GBoJhcC8Yk2DxZe1GzF-l6ype5LdT9vOKQuJ-6mbTjoaWyV12Ej6cqylE22OqlPA1r3mKO0ALHypiKkaoru_vLQwKMClDHXTQdUz8oKHaUelOQfPCUEpCYmcowt6ZZ2NBlIuk9-CPC6xGoEuJC3xEcgT_DYK4I3ym4360rj-HMrJGHR5pmqCfphhkA7g0bpXgyeROWmxRTKXwp0LhBI8a-YzE-UDJfzrlvgwN76F1i1Zu9xbyhelEv3HzTmcJmTBdF__ukxBQCNXU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=ZkwND8appWHZMDhDAB3BIaABiXyUjhvzVBMIbo0Q69T39BGH4vfwafRk1-1_uVvwv8b2KS0GBoJhcC8Yk2DxZe1GzF-l6ype5LdT9vOKQuJ-6mbTjoaWyV12Ej6cqylE22OqlPA1r3mKO0ALHypiKkaoru_vLQwKMClDHXTQdUz8oKHaUelOQfPCUEpCYmcowt6ZZ2NBlIuk9-CPC6xGoEuJC3xEcgT_DYK4I3ym4360rj-HMrJGHR5pmqCfphhkA7g0bpXgyeROWmxRTKXwp0LhBI8a-YzE-UDJfzrlvgwN76F1i1Zu9xbyhelEv3HzTmcJmTBdF__ukxBQCNXU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139739" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
تارتار سرمربی پرسولیس: هوادار دوست دارد تیمش هجومی بازی کند/ قبلا هم گفتم اینجا پرسپولیس است و هواداران بازی زیبا و هجومی را دوست دارند
✔️
✔️
واقعا یک تیم کامل داریم و بازیکنان دارند روز به روز بهتر می شوند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139738" target="_blank">📅 23:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139737" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139736">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139736" target="_blank">📅 23:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139735">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139735" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139734">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk4p3JQy4fIw2VP9MdCcQSdPLqtaNtWsRSlVowswsZ_EY7thIAOmjlAiMhe00jRgxnGJY-fthH3mfGBpfoURKBiD1UukhPfHVyMbQUurWp7KyO9YE77gizvABV2todYp-M_6oa3u9VF2S0jOBjhKKrRUo5GXCxDrigblzoazw9mpjLNKZphJAGHpt01WiwQf0uWgQ1KLRBZSlyXhUOQgUtb8x1mLMw_LhA9LGKnTz2QdJT9wRyrmEpujxN5Vo2qOub-ICfcGy4L0iANKOJtmmOKAh1pe8_gTBgBie6ST2w2Z9k9n7AeT0ZYryMl-3xIvhFBWBOQ1PjaPxCmrn7N2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
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
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/SorkhTimes/139734" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139733">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqFnc2t8eDiLD3EyL0lo598yuat1Kh3rBlkcaSaYYwENhKohLyOGTQWEQqiD0e1cK0UeYN3TB4aM0IxdhtSv1JMGqI3_S1BqFMrZ1MJXeK7TCR41J56NuuheiVsjRXGG4j6z_zpJThtwK3SdmW3StVavmlVLofUo0E6P7btenok8L6br340xp6kTdctSj9B5YoS0u7ptVCudGGkechbaqWHyPXmq93z9SjTBbnrMrDEZalla8EuulOlkgf6T-T1_6xA2b5bYV8WOOjpsk9lUmQftiMS-mPd-wJLCz0WJJqSsXKdUpIyYj-qTX9nx-OOxN2Z-xv2afA2GHTISIuMgOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج هفته ششم و جدول لیگ برتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139733" target="_blank">📅 22:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139732">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139732" target="_blank">📅 22:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139731">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139731" target="_blank">📅 22:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139730">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139730" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139729">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139729" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139728">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
تارتار: فشارها علیه پرسپولیس؟ هواداران ما امسال اتحاد خوبی دارند و تا زمانی که این اتحاد باشد ما آسیب نمی‌بینیم
✔️
✔️
کری‌خوانی نماینده‌های تبریز؟ فوتبال از سیاست جدا هست و درباره فوتبال، فوتبالی‌ها باید نظر بدهند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139728" target="_blank">📅 21:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139727">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
❌
تارتار: در روزی که خوب نبودیم بردیم
❌
❌
سرمربی پرسپولیس در روزی که خیلی خوب نبودیم اما بازی را با پیروزی پشت سرگذاشتیم/ چمن ورزشگاه شهر قدس خیلی خوب نبود امیدوارم این چمن را درست کنند چون امروز واقعا خوب نبود
❌
❌
واقعا جای سوال دارد که چرا کیفیت چمن افت کرده…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139727" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139726">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
کنایه حدادی به خداداد عزیزی : در این خصوص نمی توانم حرف بزنم اما فقط به آقای خلیلی جنگجوی و با ادب خودمان خسته نباشید می گویم. این نتایجی که می گیریم او هم تاثیر گذار است و در کنار خط در نهایت ادب با جنگندگی حق تیم را پیگیری می کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139726" target="_blank">📅 21:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139725">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139725" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139723">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
🤩
دکتر پیمان حدادی، مدیرعامل پرسپولیس:
❌
امیدواریم روند پیروزی‌ها ادامه‌دار باشد. طبیعی است که از بزرگ‌ترین و پرافتخارترین تیم ایران، انتظارات بالایی وجود داشته باشد.
❌
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139723" target="_blank">📅 21:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139722">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139722" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139721">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=L8THVjqXg3bmXMefM95gO_DCMHI2SResC-JCL0Hmm_1ML6Z-oJub1huGL0p4tqwbTwiXN9EexXrJX8QC5EFprN5jIfBJBdr7XXxbLGhdDCTclRXJrxyG10VUVhNr3w4RN5Ar2KDF2lqDa-uzWy_ftzW7AttX3HytkhfOIU3JLv9r668assl_i8DrwnOVjr3VhjZFNUM0UVh21PXNmiRg5yWjDj-Js1C31iBvJVstoBNr4pPvsWuTTHpsuLBXgcN9IzNPliENa2ZqRPWF3zhETr4r33jTRfIM7VLXv7371lim5wSjLFgrVL3e0YBkNuwnR982k6ybm1h1hqEgmkLXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=L8THVjqXg3bmXMefM95gO_DCMHI2SResC-JCL0Hmm_1ML6Z-oJub1huGL0p4tqwbTwiXN9EexXrJX8QC5EFprN5jIfBJBdr7XXxbLGhdDCTclRXJrxyG10VUVhNr3w4RN5Ar2KDF2lqDa-uzWy_ftzW7AttX3HytkhfOIU3JLv9r668assl_i8DrwnOVjr3VhjZFNUM0UVh21PXNmiRg5yWjDj-Js1C31iBvJVstoBNr4pPvsWuTTHpsuLBXgcN9IzNPliENa2ZqRPWF3zhETr4r33jTRfIM7VLXv7371lim5wSjLFgrVL3e0YBkNuwnR982k6ybm1h1hqEgmkLXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
واکنش جالب هوادار تیم به عملکرد پرسپولیس: بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل میزنیم 3 تا به رئال!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139721" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139720">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=js0YMo629mmn89xowQ95jkXnHhuLFVMw0F1w_gVgCt_TtZFfhD5voCHWaC_hcmENCrviKizZbN51vKZc5oi6nJsfzqxkENQ7066a1FtoUOTGpe48JdnKQMqHtCntPhiYykBMi9giScmrBBFUqiU7OpZOhN0twbnwBMRIz_ulOwRXK-CHV3pYYsSHb5BhmcnNDDnCZ-9_VVzKqNG1kll9g1PPvLCarJJ4eH4rrwra2FExrb5Pd-bdNMxVKUVgcP2amUj2j3bifR8vDVkrmkhrCznFLvFvPytq8c9qkw8KUiQBhUVCPWJvFSRoxgw0ZJJlYV0EoXet9NwzdFs_9VUu6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=js0YMo629mmn89xowQ95jkXnHhuLFVMw0F1w_gVgCt_TtZFfhD5voCHWaC_hcmENCrviKizZbN51vKZc5oi6nJsfzqxkENQ7066a1FtoUOTGpe48JdnKQMqHtCntPhiYykBMi9giScmrBBFUqiU7OpZOhN0twbnwBMRIz_ulOwRXK-CHV3pYYsSHb5BhmcnNDDnCZ-9_VVzKqNG1kll9g1PPvLCarJJ4eH4rrwra2FExrb5Pd-bdNMxVKUVgcP2amUj2j3bifR8vDVkrmkhrCznFLvFvPytq8c9qkw8KUiQBhUVCPWJvFSRoxgw0ZJJlYV0EoXet9NwzdFs_9VUu6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139720" target="_blank">📅 21:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139719">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRuqIYusGqxIylTdDCdA65IzU6i8q9QiFv94r1dkdugXCrT7GMKhi2l1D2N-QNLViRAro2WRxtgV2gz1X3j9M0aLyZDhv4fNqYr3rMoex1CHg2SwBRSAMpOuSVpudtrBHUTN-Ab47KES4RsyCO-CW2lkR8eIx5r6fnrliMl5XASR17zeuza2kPDf4P8B4V5wQHFRPTknTKJBpsCJ15rSsl0hIA9eeBM--kmgqSFGoeBNGdo5YmXDfrGxj6-iIaKKxiL9OhxN5MXch7K3cQDDS4P7LHkkFSV_3IzWBEUKm0DXrzGuJ_uzB2DmBqwyieRFrVFnCra-Kgej06xli5uVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
علیپور تاثیرگذارترین بازیکن کل لیگ تا هفته ششم
✔️
6 بازی، 3 گل، 3 پاس گل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139719" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139718">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139718" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139717">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=rHcEdbFnzvFb9FSggB8F1oQ45dwPKT6StQsSdmkKS4pDSeG3YDXOw6U0lmAax_iByIUECZs6tbT8RbFJ0y3iKuN4Q8pxVtxfGmEeLThlMt1WDBQ40EzaXs5REt9l7tjxwCEzZOPbu8rjuJOfLAF2IEGLrEfHIMx4CiuxBtZOnChIUTOrx-UYS7eSLL-II43zIiU4ktsoPaB-6gDQrB_UdSOcr4a_j8RrkkxGiwGgXGLH5mrm-Cac1bBmlGSBdndpXW05icpMx0a7j45pS3JrtXXNz5X0MzCi1hOjNAlr7Xnp5eXSyxla1PlIjpXFKN_rFNvbK_i2XiH9KMYtysnjdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=rHcEdbFnzvFb9FSggB8F1oQ45dwPKT6StQsSdmkKS4pDSeG3YDXOw6U0lmAax_iByIUECZs6tbT8RbFJ0y3iKuN4Q8pxVtxfGmEeLThlMt1WDBQ40EzaXs5REt9l7tjxwCEzZOPbu8rjuJOfLAF2IEGLrEfHIMx4CiuxBtZOnChIUTOrx-UYS7eSLL-II43zIiU4ktsoPaB-6gDQrB_UdSOcr4a_j8RrkkxGiwGgXGLH5mrm-Cac1bBmlGSBdndpXW05icpMx0a7j45pS3JrtXXNz5X0MzCi1hOjNAlr7Xnp5eXSyxla1PlIjpXFKN_rFNvbK_i2XiH9KMYtysnjdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139717" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139716" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139715" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
گل اول و توسط علیپور زدیم با اینکه نیمه اول خوب نبودیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139714" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139713" target="_blank">📅 20:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139712" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139711" target="_blank">📅 20:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
این بازی و بچه ها با سه امتیاز بازی و ترک کنن برای بازی بعدی بعد از مدت ها یک هفته تایم و استراحت داریم ...و بازی بعدی یکشنبه هفته بعدی با خیبره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139709" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139708" target="_blank">📅 19:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139707">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139707" target="_blank">📅 19:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🏅
پایان نیمه اول
🏅
پرسپولیس
1️⃣
_
🏅
ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
0️⃣</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139706" target="_blank">📅 19:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1Xxhy0V-WX6oxmngOlSO5rM5hJqczIs7OeNyMw9iqLSo6W3mGH34T0CMEUXMpB2t-Zh2Fnz4p1iyHHdJAZFYgJMNo8XtEQM_IPlIA2Vvogwa7DCU7yoIBpiyIa-IFIhh8IwPR0Qqy9vIzNhZ6A1xMmLZ1Cj-p8RpwPfhEXY48ICeIJcVNOe1Bo7jH3joSovEmIAYX0o8Lblp5-v_jXX5E_LzkklqMjMHGuMxh66e1Y46EpAhKIJ09jtizRuh3ZWgIrjeAAblkucqYYMBj-uaUdfYiAr1H7XkHDZq7jDplICX0c6APAjlNZp17rAFAKd9R1kQ5MuluoW4i3ODQ46839-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1Xxhy0V-WX6oxmngOlSO5rM5hJqczIs7OeNyMw9iqLSo6W3mGH34T0CMEUXMpB2t-Zh2Fnz4p1iyHHdJAZFYgJMNo8XtEQM_IPlIA2Vvogwa7DCU7yoIBpiyIa-IFIhh8IwPR0Qqy9vIzNhZ6A1xMmLZ1Cj-p8RpwPfhEXY48ICeIJcVNOe1Bo7jH3joSovEmIAYX0o8Lblp5-v_jXX5E_LzkklqMjMHGuMxh66e1Y46EpAhKIJ09jtizRuh3ZWgIrjeAAblkucqYYMBj-uaUdfYiAr1H7XkHDZq7jDplICX0c6APAjlNZp17rAFAKd9R1kQ5MuluoW4i3ODQ46839-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139705" target="_blank">📅 19:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139704" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/139703" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
بریم برای بازی شش امتیازی ..امیدوارم مثل بازی های گذشته از دیدن فوتبال پرسپولیس لذت ببریم ...الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139702" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2tgP492ARUcDUwgDqflzS6gTtgV_Z-eEXjI_7qXMl1tZY1DUd-SWHnOz5Bq4bQlTLW1emL_RSUuqBV26F79-fZsUoXfZprDrLR3C5EWhkNYYqrnjGYqklMcCOGwTO5i9b7b9t_LZdpP9G9oRu1oHfrpRYsMXpVH-2JOC2eNcPEwsfGt07JprlXqT9lhYs4rJYZl2NBy5FsvbfPuBUhMB-40wde3Z5d4hB8PFvOfFLBta9BAUtphIOwKjtoKkMQNpW1jiS5n3gO689hOompH1LpMc2OjCF4e36kQo2uQKgtaSKu79H-jfJ-ohMyfp02tdSawtfY-cI2oAeAnX5jwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
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
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/139701" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/139700" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
هوادار پرسپولیس درباره جنجال امید عالیشاه و خداداد عزیزی
❌
❌
آقای خداداد عزیزی به قول سیدجلال ما پرسپولیسی‌ها هیچ چیزی از یادمان نمی‌رود. خدا نکند که ما پرسپولیسی‌ها با تو رودررو شویم؛ می‌توانی از بیرانوند بپرسی. مثل خودت با تو رفتار می‌کنیم. کل افتخارات…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139699" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
✔️
صحبت‌های هوادار پرسپولیس درباره اتفاقات بازی تراکتور- گل گهر و حواشی ایجاد شده میان عالیشاه و خداداد عزیزی!
❌
❌
از کمیته انضباطی سخت می‌خواهیم برای یک بار هم که شده رای درست بدهد.‌امروز نشان می‌دهیم که هیچ کسی حق توهین به عالیشاه را ندارد. امید عالیشاه…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139698" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139697" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
ترکیب بازی امروز همینه و تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139696" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139695">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=kGCtqJlJlgCqXGoZ9vkzxEgvzMfHoTAslOun4ph1k1PTqilM7uItF6wx-az-l0hFxBJ2ChdqZWFCsFTDl_cqGUgmn2t5hEaRToDW1w9NjpCujqRObCFIeM1RNckPtH5Ig1BHLwHxsgyfBEdkR7ZK8qvi9j1lIuy4vJ3Dm8-zmr2XC2qmp_WsuH9N-_RR7yVJVOafPsTJqJ_yunjKLh_GFXHxbelJlp-ASmnoDCGE72B0eOVu8_4oLGA8wTyL0J-2k6Ca9GguH08eKo1z2BnIXONa-P5qFRi5SQuRIA75SM2UooqCNrPgiVtuaMPnLbsZPIMSxd5pdGK2tnl0JPcotA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=kGCtqJlJlgCqXGoZ9vkzxEgvzMfHoTAslOun4ph1k1PTqilM7uItF6wx-az-l0hFxBJ2ChdqZWFCsFTDl_cqGUgmn2t5hEaRToDW1w9NjpCujqRObCFIeM1RNckPtH5Ig1BHLwHxsgyfBEdkR7ZK8qvi9j1lIuy4vJ3Dm8-zmr2XC2qmp_WsuH9N-_RR7yVJVOafPsTJqJ_yunjKLh_GFXHxbelJlp-ASmnoDCGE72B0eOVu8_4oLGA8wTyL0J-2k6Ca9GguH08eKo1z2BnIXONa-P5qFRi5SQuRIA75SM2UooqCNrPgiVtuaMPnLbsZPIMSxd5pdGK2tnl0JPcotA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139695" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
✔️
نیمکت
✔️
امیر رضا رفیعی
✔️
ایری
✔️
ابرقویی
✔️
جلالی
✔️
باکیچ
✔️
لطیفی فر
✔️
یاسین
✔️
صادقی
✔️
محمودی
✔️
بیفوما
✔️
شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139694" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139693" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0dWqW6B_Vcr6hB3hCKdlvuNEU7_jdSyqZDqRL4gTNs-7E6kfAIAMelLOls1OccjXCiu6NwEuQlL8hp-9QNjXQqwH2_cf-fiEMFyVP7s8Lu2yGrilSnC-xAcNWZj9r1oHkU-7MOYh7W-iIJFN8LD6vmfRlxBo08rSSc1nxa3g1IN_-G6IwbNcsVuY5IhxKgj-pN0eKFhOFDNLs1iUmo2MojsVTLQqtSBTZSINWr8tjk-PpoVghNzq4FGt5AlyRifZNLYhWgBiVcudYB0-xMPRctARBPk4QfPZwYKJ0qfKNgZO-Uh_9L9g9fhGL-DmccdYW4fOoGbemB1EQGKG8xQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139692" target="_blank">📅 18:01 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
