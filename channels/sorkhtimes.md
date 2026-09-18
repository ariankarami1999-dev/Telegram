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
<img src="https://cdn4.telesco.pe/file/JSIMW_Twgzkc6ypIkmj6G6eAmiafQqoZvB7tY_e5S14VYcwsls0aqYLfNdScWjmMSNhNMyjz0X_6QUwb-7Wq4cP_I54OS23C-v3Pepog9G-JbwKgBTlCi5xj8lm9hjXaVNRbKEOyuA8xx4lVZJ9qWQPe7n4OnRxKC-_Ql0NlQxb0xs5IY9cdKeNeSaJGIzj2dhbqcKk8-Du_iuSy0T_Qo4wpr1vXrYCUJIzPrcSABmY4Vwpcz70dGj_o3V6XrtjVcpc8-H71Lasl68cCDnnHWIuzcGGLNcxsxKQIBSOH-ab6HkaJ7rJw1eyrgVsI5CdczGTgGce1e2c2rMHqQgxA2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 05:52:39</div>
<hr>

<div class="tg-post" id="msg-140214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دنبال راه‌حلی برای ورود به سایت بدون دردسر میگردی؟!
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
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/140214" target="_blank">📅 01:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👤
⚽️
فارس: مهدی تارتار، جاسوس پرسپولیس که محمد یوسفی هوادار متمول بوده رو از تیم کامل گذاشته کنار؛ بخاطر همین ترکیب دیگه لو نمیره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/140213" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
🇮🇷
محسن خلیلی خبر مذاکره مدیریت باشگاه تراکتور با اوستون اورونوف رو تکذیب کرد و اعلام کرد این بازیکن هییییچ آفری ندارد و در جمع شاگردان مهدی تارتار موندنی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/140212" target="_blank">📅 00:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgS7t8qSKW92EgT5NwPNzsiXdemc0TDpStNtQyTcthLQAousFBeHvUYPw4krzYGc3l26aCaZk4A8VjdBLgBt-zPqmsS2eahAsf2lHQi1A2EsWkdsKj2lFK7KVl5TXoqgDqUbal0IRoC4u-j3AJZG9E__7Lj3tV4Zw3Ztdy6pDB081G76NXB0PxZ-Ea66yn5xkc0lZRu6QaBscl2PGL0c4PmIqfuvb-osKjqfMWoBF2dxbNC133TI7jYTkhy9NSWF1g78PLBifnRdGFPhlYK_8gfuQNC75CO7v4o1erWPfzhqUE1FGtQ4WiTMGa4WYg5G2J8vaS5bgt9xgXLmM36sDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💢
💢
💢
باشگاه پرسپولیس میخواد در پایان جام ملت‌های آسیا برانکو ایوانکوویچ‌ سرمربی‌ سابق سرخپوشان رو بعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/140211" target="_blank">📅 00:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
🔻
🔻
توضیحات #تکمیلی در مورد پرونده اموال توقیفی باشگاه؛ از صندلی چرخ دار گرفته تا پرینتر و آب سردکن
🔻
🔻
🔻
در دوره علی اکبر طاهری شرکت امین سیمای کیش(۳۰۹۰) اسپانسر پرسپولیس میشه و به جز اون چصه حق اسپانسری که به هزار مکافات به پرسپولیس پرداخت می‌کنند با همکاری…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/140210" target="_blank">📅 00:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140209">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/140209" target="_blank">📅 23:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140208">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=JPU2qWhsTeBaYQplGS7Cgnw0bKTC4VNBCUZGt76FCWXfMQgIHvOzpsjE_okty9oEn8gu4_7z5cuIYOghBU9nsAscL04dDXbZffKRjttsWHMltYZL2kezoYLR7thn-OwH4Juc-eOpdjj3aPSV3WM8uq-fpQQZ6_5JJzbTaFSaA12-lYwUcozwDBFPrEYz64eDIBbkEDRxH4PdiOz7PksAe0Fr-tpdzgdLgO9uIZ7cwGxm-x-sOarJRY_Sjnt8pYDuYy-lDXTi7FvMuBVV8Kc9-1a1uhTSkAX5JDlZbyYl4nU4jlrNtt-5tq9hw0fb8lPUIt4CS56ERHvjz0_dlbL0jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79b8e0878.mp4?token=JPU2qWhsTeBaYQplGS7Cgnw0bKTC4VNBCUZGt76FCWXfMQgIHvOzpsjE_okty9oEn8gu4_7z5cuIYOghBU9nsAscL04dDXbZffKRjttsWHMltYZL2kezoYLR7thn-OwH4Juc-eOpdjj3aPSV3WM8uq-fpQQZ6_5JJzbTaFSaA12-lYwUcozwDBFPrEYz64eDIBbkEDRxH4PdiOz7PksAe0Fr-tpdzgdLgO9uIZ7cwGxm-x-sOarJRY_Sjnt8pYDuYy-lDXTi7FvMuBVV8Kc9-1a1uhTSkAX5JDlZbyYl4nU4jlrNtt-5tq9hw0fb8lPUIt4CS56ERHvjz0_dlbL0jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/140208" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140207">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/140207" target="_blank">📅 22:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140206">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
✔️
کیسه که محمد خلیفه رو خریده بود بدلیل بسته بودن پنجره اش ، این بازیکن دوباره به آلومینیوم برگشت
😅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140206" target="_blank">📅 21:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140205">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/140205" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140204">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtBtqR_TgKlqL-lLkvwCQXMarzitSBpY_VIYi73uygs06MAFl0X1hB16Z8DBue9F28_ZHdYwRz2salyvL7fwpvVMZfGQZfKCqRyd4bdZdfTuE7MfhaTofyTL9k80UH-gUQR4M-0WfqDede6jf5lxfKdIVP4MNk6s4w6VNraiheOn_fZLvx0JFdfwwfC2jqxmeRoCvbZ88PYYcK8XXHPzmD08Cw7TdUv2dL0w7AONdePQzB8oxptc_ajFbwy-99yVT6eaWuQS6GiVToY5Q_YcjWta3S-G3pokBb_gZPjKfeTw1J9G9TwDuB4vAkk9pdUusqvNw1rNcF3KjEc5f4kglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری تسنیم: علیرضا بیرانوند در پایان فصل به تیم کیسه خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/140204" target="_blank">📅 21:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140203">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
ترامپ :
❌
ممکن است مجبور شویم عملیات نظامی گسترده علیه ایران را از سر بگیریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140203" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140202">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=SykwPOKREXyi8ozAn1xOfNxf1pb5yzgcJQdoWcVDFH--_X3N_yYQkOYoJQuaRRRRoAelxgnMotGyT4r6-e12L7StN1Y64ryi85zX41Mj1XL0TT2XeZqNQzQ4klG8qb4RF0MhINSaZseVQ4GeTMYpcnFS8_Ut4Z9_2jt0oonBv-oBNg24VCBQro2gPDVNj90fZ_uETMI8CjG4ezGLMtYZr6M7zcfGO9QkWFvK4VkO0bXHqlrK5TySgTl1SY5yDvNjCx2c2N5f8QnGLLY03lRHAtS1Yn5Bns5DAuuSJFIfZFm6wAdKhw8Zit5nnxzesjCabdHlDFAHg5E9TnqZ7_m5GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fab4451f6.mp4?token=SykwPOKREXyi8ozAn1xOfNxf1pb5yzgcJQdoWcVDFH--_X3N_yYQkOYoJQuaRRRRoAelxgnMotGyT4r6-e12L7StN1Y64ryi85zX41Mj1XL0TT2XeZqNQzQ4klG8qb4RF0MhINSaZseVQ4GeTMYpcnFS8_Ut4Z9_2jt0oonBv-oBNg24VCBQro2gPDVNj90fZ_uETMI8CjG4ezGLMtYZr6M7zcfGO9QkWFvK4VkO0bXHqlrK5TySgTl1SY5yDvNjCx2c2N5f8QnGLLY03lRHAtS1Yn5Bns5DAuuSJFIfZFm6wAdKhw8Zit5nnxzesjCabdHlDFAHg5E9TnqZ7_m5GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🟥
هشت سال پیش در چنین روزی؛ پرسپولیس با یک کامبک تاریخی 3 بر 1 الدحیل قطر را شکست داد و به نیمه نهایی لیگ قهرمانان آسیا صعود کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140202" target="_blank">📅 21:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140201">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
شجاع خلیل‌زاده، احسان حاج‌صفی چرا باید به تیم ملی دعوت شوند نسل این ها گذشته است
‼️
🔴
مهدی لیموچی افت کرده و میلاد سورگی که به نام جوان گرایی به تیم ملی دعوت شدند عملکردشان در حد فیکس بازی کردن در تیمشان نیست
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140201" target="_blank">📅 21:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140200">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
#فوری | ترامپ: هر اتفاقی ممکن است بیفتد
🔻
تصمیم بزرگی در پیش دارم؛ آیا می‌خواهم وارد عمل شوم و آنها را نابود کنم یا نه؟ این تصمیم بزرگی است
🔻
به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140200" target="_blank">📅 21:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140199">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0ZXofgs6TcZeXkdBwxZYBh2rQ7SAbg03LJch0Dd_ttg05HcPF5nt1jeTRYnGZy4hxvFchHZu-xplVaeu-AJ5XhyKVXxIqdxW29fERumy7cNgcNBBRXMaQmhcbRnTFDwkeBeeUyPeeZfhfXlCZaXxk8v2O6Oc0zpzAnRIWlcseDfvj1v97-cS3x6KdU5pJ-0vgScHk95w6xjo5j8gulX9BVRGYxZPIASlPxS2ZR6ZQaQbQI2k_GlKS8j2za8VuZPxgyS9it2EEvg_IvdcYrFLyA8l2FG0uoI7lkw5VEeZE5qgcFPWVyttVTRe6lC6g5oAzM4OtMm_FYvgoyglysl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
❌
❌
❌
در اقدامی عجیب علیرضا اشرف مدیر رسانه‌ای پرسپولیس اشتباهی عکس لخت خودش و پسرشو فرستاد توچنل‌رسمی پرسپولیس و زود پاکش کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/140199" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140198">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔄
🔄
علیرضا اشرف، مدیر رسانه‌ای پرسپولیس: خوشبختانه آسیب دیدگی ابوالفضل جلالی جدی نیست و با استراحت و ریکاوری مناسب، به بازی بعدی میرسه  سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@Sorkhtimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140198" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140197">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
ترامپ ویدئویی منتشر کرده که تو پایانش بخشی از سخنرانیش تو زمان شروع حملات مشترک آمریکا و اسرائیل به ایران آورده شده: «خطاب به مردم بزرگ و سرافراز ایران، امشب می‌گویم که ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140197" target="_blank">📅 20:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140196">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
پرسپولیس قصد داره قرارداد امیرحسین محمودی رو با بند فسخ ۱.۸ میلیون یورویی تمدید کنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140196" target="_blank">📅 19:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140195">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
سازمان نظام وظیفه به علیرضا جهانبخش اعلام کرده که معافیت‌تحصیلی‌اش رو به‌پایان است و باید تا اواخر آذر ماه تکلیف خود را روشن کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140195" target="_blank">📅 19:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140194">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB1DV-EppOpCYW2AKZgEgueZ_woHpG_gF0nbMNMWLICYQAxgvk0Qa0NSo0wJY8DON9Q4r7R0c-fjJq8y_q6iWhyAms_iX4ycrgFRMacZ1J4CCETIzBLVNFpre5BR52GM5w7ESZbiFDDuRf26d9AE7D9C57CTObp2tLQU8yEB21jSoocWZFKjDNWcKCrVLwIBjD0VLxtKocwuSIUvtGCWOAV22g30OAtRlnN-fvcoV5zQn3mKFAZPB-O8cTWxtzVqb-W4Xgx1js8E9zrjOWDS23PTx72dx7-vXiJBhqcEBqyWL_jUSteriVJH7Vj6OywuI8kC9YyaeMsQ38GDwq2p9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیتی و نوریچ؛ شبِ امتحان برای سیتیزن‌ها، با یک حریف که چیزی برای از دست دادن ندارد.
[
منچسترسیتی
🔵
🆚
🟢
نوریچ‌سیتی
]
⚽️
سیتی با مالکیت و گردش سریع توپ، از همان ابتدا برای کنترل بازی جلو می‌کشد. نوریچ احتمالاً با دفاع فشرده و ضدحملات به دنبال ایجاد خطر خواهد بود. اختلاف کیفیت دو تیم به سود سیتی است، اما باز کردن خط دفاعی نوریچ چالش اصلی بازی خواهد بود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
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
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140194" target="_blank">📅 19:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140193">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140193" target="_blank">📅 17:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140192">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140192" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140191">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
❌
مراقبت از پوریا شهرآبادی از دست ایجنت‌ها جزو اولویت‌های اصلی باشگاه در ادامه فصل باید باشه. پس از درخشش این بازیکن در بازی امروز و احتمالا ادامه تورنمنت آسیایی، اسم پوریا بیشتر سر زبون‌ها میفته و مدیریت رفتار و دقایق بازی کردن این ستاره جوان، جزو مهمترین…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140191" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140190">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140190" target="_blank">📅 16:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140189">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حدادی اعلام کرد شکایت را به دادگاه بین‌المللی CAS می‌برد و ولکن ماجرا نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140189" target="_blank">📅 16:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140188">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
شکایت پرسپولیس از آسانی رد شد
✅
با اعلام کمیته انضباطی، شکایت پرسپولیس از استقلال بابت حضور یاسر آسانی در داربی رد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140188" target="_blank">📅 14:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140187">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140187" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140186">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140186" target="_blank">📅 14:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140185">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140185" target="_blank">📅 14:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140184">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
خط خوردگان بزرگ لیست
😀
محمدحسین کنعانی‌زاگان
😀
روزبه چشمی
😀
شهریار مغانلو
😀
هادی حبیبی‌نژاد
😀
علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140184" target="_blank">📅 14:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140183">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
اورونوف به همراه برادرش که چند روزی کنارش بود، دیروز ایران رو ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140183" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140182">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
دعوت نشدن علیپور و کنعانی زادگان واقعا عجیب بنظر میرسه.....  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140182" target="_blank">📅 11:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140181">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
✅
علی قلی زاده: من از ته قلبم پرسپولیسی هستم و دوست دارم برای این تیم بازی کنم
❌
❌
اینکه به جام ملت‌های آسیا برسم یا نه بستگی به شرایط ریکاوری زانو دارد/ حضور من در جام ملت‌های آسیا نشدنی نیست و باید منتظر باشم
❌
❌
فعلا فقط دو ماه از مصدومیتم گذشته.خدا را…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140181" target="_blank">📅 11:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140180">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140180" target="_blank">📅 11:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
✔️
فووووری؛ با اعلام امیر قلعه‌نویی علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی عیدی، امید نورافکن، مهدی لیموچی،…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140179" target="_blank">📅 11:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140178" target="_blank">📅 11:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ9utubfO9Vbw4PTk_iFLja-jVRWnqQtx1B2XS8axVKYSGBoCxrGy02toJ1e_p0LFXjeKQbeOTy1NsDM4h496VJVZQy8Ajcw_hrKUY_8bmuihTtLUDmMg3n4_K3eMI49Bx56TVXwMWe8UHgmWk806O7EAn3cwexbo9S2WCicM9oWi1pf_vwDBQ0hg74iub77Re1_cjAaS4BIcsZA9YmSTcxkDv3TVSYQ3RGCq_mrPxWKWf1aM_KeWabR44XpMwnCPfFSqZo214a1tlJklXV3Oad3LN873wruksmeYNonI18R_PKvBDP0e-OAYXeX3JW0RaCNpzgR4eJoFhwHKP_KPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
Juventus -
⚫️
Nijmegen
⏰
Tonight 22:30
🏟
Allianz Stadium
🟠
یوونتوس بعد از شکست پرگل مقابل ساسولو، در شروع اروپایی به دنبال بازگشت به مسیر برد است و فشار بیشتری روی خط حمله خواهد داشت. نایمخن با فوتبال تهاجمی و پرس مداوم وارد بازی می‌شود؛ بنابراین یووه در کنار مالکیت، باید مراقب فضاهای پشت خط میانی باشد. با توجه به شرایط دو تیم، انتظار می‌رود یوونتوس بازی را کنترل کند اما نایمخن می‌تواند در انتقال‌ها دردسرساز شود.
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
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140177" target="_blank">📅 11:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140176">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔥
⚽️
رکورد جالب پوریا شهرآبادی؛ شروعی درخشان در پرسپولیس!
🔴
پوریا شهرآبادی در حالی که تنها ۲۰ سال سن داره، تبدیل شده به دومین گلزن جوان تاریخ باشگاه که در کمترین زمان ممکن به ۲ گل می‌رسد.یعنی شهرآبادی برای زدن ۲ گل، حتی به اندازه‌ی دو بازی کامل هم در زمین نبوده…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140176" target="_blank">📅 09:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140175">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✔️
✔️
رسانه هفت ورزشی:
✔️
پیشنهاد نخست لوسیل قطر که خوب هم بوده به محمد عمری ارائه شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140175" target="_blank">📅 09:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140174">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140174" target="_blank">📅 09:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxvFZUFjy-dErWH1x1GzCApFHVlQUV1H4WHEfqSMm8S_brnKkI2vJReo0AoRKKLj_nHcUB5_U-naSnHV_LE8QLxxML3F9Q51QEQebsjkfInOdX4NrA77Zs_JIv4YuYc9hgKrzwHw8uugfolOwj2PqZOGwVi62T5K83nuPOTA6ZzBuFKM5-Xx5bmVnwmY3UbYhYQqo6n8AUBv6kqk_SE7OxCZV9JmAX3HPqdZ0gaV0P-IcT74iRVwArdMAyb3lmpEZYBXaTdHPuNDVxdlDVw9LgsWbJMALZGt-CbBxBWGX1O2hSMx6ehEtRBwQD2LTFxYDLFb7ZXSjY4M6AvwQiVMwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدودا ۳ هفته دیگه تا دیدن دوباره بازیهای پرسپولیس مونده و عجیب چشم انتظار دیدن دوباره عشقیم..‌.
❤️‍🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140173" target="_blank">📅 08:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8euJ_xJrwbFORDE2t7yDk1xYbq2tE0LraDH96ObpdKgOGdhdOLWvLk3Akaw5xfMr4lkcTVOEWaofF_ypq3ApFMPjyX4M9j_lw4YQhmXno5rwK5J4ixkid24fSz_vF7zc13RPNDV2xufesytxSXio9i5xbhlaNOk8S1eJqhXb-16VCnZOxzkqg0i6SqTZOMf7dGe_hb7VT_lIZQp3GV0x-WSRob6LoCblJAyVPrV-p-0Mbn4aBU6yuJeJHXu09ZZ5GwasHb9OwUdZ3MvxdMocZZZm4gr97aV4ZZuSzKQEPPIq3LAhd35puq_m397XDoTdxhDtUhbu3Zza7sjvAa2CA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140172" target="_blank">📅 08:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140171">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=WGNSn7eTs60wPAqvs8Xn6FHRvp4B0rBUOjgyIj3bhRDL1YU4tm86BSe_DinEKY8tCLT0brZ6aM-WAmjEGt_cj5EOFf2JSNhsD-dVPFoDxiHmBbJUgycybrNr0rDaBoEI23Qh4eqGkbgVMnitY5tueN3nMLNtfLDAKHnol246z9Oke9Ko4m7Qm2gS1HasF4T-o6H5k55m-EAStvBaHy4JTA6iDyZ1z-0TKrEfK1gKxVWAnH2-x5FS81tF64tr8_Bou1EOADSwxEPSl2WQsQaUEAXSuo7zjfz-AKIvwIaWvy93_JKUn_5W4gjcmV3cjVfXhubTUQZwwnggBWLaHuzY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ae93144a3.mp4?token=WGNSn7eTs60wPAqvs8Xn6FHRvp4B0rBUOjgyIj3bhRDL1YU4tm86BSe_DinEKY8tCLT0brZ6aM-WAmjEGt_cj5EOFf2JSNhsD-dVPFoDxiHmBbJUgycybrNr0rDaBoEI23Qh4eqGkbgVMnitY5tueN3nMLNtfLDAKHnol246z9Oke9Ko4m7Qm2gS1HasF4T-o6H5k55m-EAStvBaHy4JTA6iDyZ1z-0TKrEfK1gKxVWAnH2-x5FS81tF64tr8_Bou1EOADSwxEPSl2WQsQaUEAXSuo7zjfz-AKIvwIaWvy93_JKUn_5W4gjcmV3cjVfXhubTUQZwwnggBWLaHuzY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
آموزش ثبت‌نام و ورود به سایت وینکوبت از طریق ربات تلگرام
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140171" target="_blank">📅 01:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140170">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140170" target="_blank">📅 22:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140169">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
❌
#فرهیختگان؛ مذاکرات با ۵ بازیکن برای تمدید قرارداد آغاز شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140169" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140168">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
❌
مدیریت پرسپولیس در حال انجام کارهای تمدید قرارداد ۲ساله سید پیام نیازمند، است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140168" target="_blank">📅 22:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140167">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
❌
❌
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140167" target="_blank">📅 22:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
👤
مدیرعامل فجر:
📍
انتقال علی بیرو به تیم ما قطعی شد
❌
چون پنجره نقل و انتقالاتی بستس تا نیم فصل باید بشینه سکو
😃
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/140166" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2-gr6TqYPLjKny9FABC3SnQMF_oE0cw1NA6xXRb_4V4iWJPiFqIt-i6n1K6g_-gckYUOD-y300iiwg6Bn890KqtYE3OUzP0GbcTbNWdV3F3kBQyy4xWpVhA8m-ecubHm6Sd2WXBwzt9CEV6H-BtKaDtmupuoQu_zHexmKADXkmAq4nXbgE7xxszNQ_Qe5Qn84HOmcde8JJhCos5HTDeefRWt3BdhwOB0MxVrr5DG5SN0lXLYg7_lExhG9eBJCXbI7ycYRzKEP4aBEQfAwOrLRz5tFEvt6Nam5Wy-hT9nOCJDMfgXh9DjdJOnx58EPuUqWWi2hI5nrjeli5bHshb4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/140165" target="_blank">📅 21:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140164">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
❌
❌
باشگاه پرسپولیس کارهای تمدید قرارداد ستارگان خود را آغاز کرده و امیدوار است بتواند آنها را حفظ کند/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140164" target="_blank">📅 20:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140163">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
❌
مدیرعامل باشگاه فجر سپاسی؛ انتقال علیرضا بیرانوند دروازه‌بان تیم تراکتور به فجر سپاسی قطعی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140163" target="_blank">📅 20:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140162">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlZTZKCyGBHyv0hTDT38_ZvSabiMfCscwCTAmwTF9LlQOydRkr_55zQUQGje5xFpODBnK6CtEdqw_E6vlaVA14Vnk1_8o1ShiUbNbTz9s3ov1DkcIE4ad7SacZJPWJ1LDC4ZuDeZOJvKpCfcJ5t4RG1hiTiuHl7vfg7VwMC0N84BZEPiANcx1qo4iEMAFGX9xhfdNdKE40E5JvgVOEys-gEtWyr5yfCurKb6sIMVPFuSIBRSVmeCF00wa8aUhDuMFKdwOM6OGY7Cwz-9kV6hnrXt6Jsj5W8fpsiycLHx4dLk0sAzMhJp5D6_m0j71DHwBMBNh6neb3PXvTZQGqLkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سن‌سیرو امشب شاهد تقابل دو تیم بزرگ اروپایی است؛ میلان و بنفیکا در دیداری که می‌تواند از همان دقایق اول با فشار و درگیری زیادی دنبال شود.
[
🔴
AC Milan
Vs
🔴
Benfica
]
⚽️
میلان روی بازی در عرض و نفوذ از کناره‌ها حساب می‌کند و بنفیکا هم با جابه‌جایی سریع بازیکنانش می‌تواند فضاهایی میان خطوط پیدا کند. اگر پرتغالی‌ها بتوانند از پرس میلان عبور کنند، ضدحملاتشان می‌تواند جدی باشد؛ در طرف مقابل، حفظ توپ و صبر در ساخت حمله برای روسونری اهمیت زیادی خواهد داشت.
🟢
امشب چه کسی برنده این نبرد اروپایی خواهد بود؟
📌
میلان و بنفیکا را با وینکوبت دنبال کنید؛ همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140162" target="_blank">📅 20:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140161">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140161" target="_blank">📅 20:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140160">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
النصر هم به طور عجیبی سه گل خورده از العین ..خدا به داد کیسه برسه با این العین   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140160" target="_blank">📅 20:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140159">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140159" target="_blank">📅 18:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140158">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140158" target="_blank">📅 18:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
رسانه های عراقی: بشار رسن دنبال اینه برگرده به پرسپولیس
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140156" target="_blank">📅 18:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">💢
عابدینی مدیرعامل سابق باشگاه پرسپولیس: ‌چوب لای چرخ مدیران پرسپولیس نکنید، برخی بیرون از باشگاه پرسپولیس چوب لای چرخ مدیران این باشگاه می‌گذارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140155" target="_blank">📅 18:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140154" target="_blank">📅 18:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140153">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✔️
✔️
در جلسه امروز تارتار با حدادی، سرمربی پرسپولیس تأکید ویژه ای به جذب ابوذر صفرزاده کرده و از ساعتی پیش جلسات نهایی برای جذب این بازیکن آغاز شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140153" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
شنیده ها: تراکتور نیم‌ فصل برای جذب حسین ابرقویی وارد میشه!
✔️
✔️
گفته میشه تراکتوری‌ها ابرقویی رو زیر نظر دارن و احتمال اقدام برای جذبش در نیم‌فصل وجود داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140152" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
❌
حسین ابرقویی مدافع میانی29ساله پرسپولیس چند پیشنهاد لیگ برتری دریافت کرده و قصد داره توافقی از جمع شاگردان مهدی تارتار جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/140151" target="_blank">📅 15:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140150">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0xzHG8dq-rmqcdsd_2QdPq-eGeA9LKyiqOQqUhv8xtnqyhqjvy5h5PdIjYv2i8RnFcHzEntaeA3yIUqq960eafXGDVyQUpLZgpz7USiG7mQxp7-aFUf94KwoliWIPbJsbfBp42PJGQmzffZQLiyF9jLus9VlXBXnOdAhYwMEh2vmChVGYahpuPtsORjvj3g7Db0UvH4-DGev8u37RyM7cfptKGjDF7sy9uG6UXujWYxDO-lzcahk8c_c14YbJzheh_8b5ifDxWti9lz6GitpIvr79F-G4thGABmclR2yp05fFRcPj4FgnfxrEfSuFe0iuueFi55Wh7MUw-S5Gd5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❤️
ایشون بعد از اردو ترکیه که مصدوم شد حتی تو یک تمرین تیم شرکت نکرده و حتی نمیدونیم مصدومیت‌ش دقیقا چی هست و داره چی کار می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140150" target="_blank">📅 14:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuVpR-VNHHpyjNQiz2N0AW3_QeUVQkPNFdSDvRmYjDpDCI5ps8gZCylunO9rkGsL4USWPbozuHL5NtjopiVx1oy_y40g9VUeNVgFAuG2r5Sd56141aP2C8Dqi5-SFO5ikjnwCzBcqlkabJ0AbX5y3FoBauZmfeP_5CaBK0uDNNmFfmiTtTUHMu76i1Hmu7iZYehmu54flE7wktr22uC4iP5cj5ONwb6NaiA_4e-5ysQK_pk8EQ34njEaeM0lofPSfxV_d08devP4GCIwPw9UxwQqBahCtzbj-fP0raeDTE4EG8wdvkyjkoEAgHC6piKxZMXtW6bilQXksVmT1UUH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گفته میشود باشگاه پرسپولیس دیگر برنامه‌ای برای خرید امتیاز تیم لیگ یکی ندارد و به دنبال خرید تیم لیگ دویی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140149" target="_blank">📅 14:46 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140148" target="_blank">📅 14:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct4mhwssw29B8bNc13yQ7TxJ5r-4TqV9A8YYr2StocxmlX2hYP3ULntuFn2qXaGkc7BSZ-b07X59NTzC1aozp9gXN3t2TkrkOdD6a7-sZqW0C9QcqS8o-UINmqxqqrfLYafqWWsG2KXdGCTOVyoYuMaqaf9hyUJ3wTQOxaLdl_ltUfjrDLUZdnBrv258VHINnCY-5pcOleTY-ZfRjykFPyd1WZqK4h65o_dJXTgGY3ISWG_HOVO_JD4KSJ1XRdYpUHNkbAnAO8ezJLZeLcyrc1Go8bnbk4hgB9NeInAfafiilkTQkozCTyKKWH1t6QuBpLp_AYQTZj09w2zKrZrKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چندین بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
امشب کنداکتور با چند تقابل جذاب از لالیگا، لیگ برتر و اروپا سنگین شده؛ از جدال اتلتیکو با اوساسونا تا میلان مقابل بنفیكا و منچستریونایتد با برایتون.
بارسلونا و لورکوزن روی کاغذ شرایط متفاوتی دارند، اما بازی‌هایی مثل میلان و بنفیكا و همچنین اندرلخت با لیون می‌توانند معادلات متفاوتی بسازند.
شبی پر از بازی‌های قابل بررسی؛ جایی که انتخاب درست، بیشتر از اسم تیم‌ها به جزئیات مسابقه بستگی دارد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140147" target="_blank">📅 13:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TimrK9U0LWXWYC0LGOPvw-LqkyPvWtXvOnfAMHfypAKhtcgqUnl_y5NI-jMBlOcVOZDgRtvWcLrUf3oz6J_3mOiYh7SuEKOZwBbPO4vOrw_TgJSaqcQ47IMk_h8SyepP9BvnfNsFDNDOxqXulYIrJHfsU-iL31g3bof_aI-H9TbFV5fzI9RC4X_fRjJlIARh0DoFOsTRyP26X7PrRQWg2lGXd7ChVIVCOe8g9UoJSkanUQl1Mu8q5RIavT3GCCBcBp1DhdUi59_zimNLrxpujq3HGFXWuW0bZ1v7b1o1LjEZEPqVdOwAxMYc65hGcZQ_zScgO8qlTASIzLJQsSd09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140146" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKLsYJpDEUik4vT3rWPE3JSo4IYsqnjXsZtszY9D3rQfLG6m1oa98vYBZaP8icwKBMKgCvnm8QD8Sh8t58xJJcOHgHK2KdQc_uxA8kjNG5KQhb1SsigT48UCZ5WmWDpYdEUa_7SbdrN4wT0HtYlZQe62kSpUOAgdY0QmIRDHdnWmJH_3fa03Yu9rIu-B0-_vUzfEWUGjuoBmtTUfRRcGJHUX1sP485ghh5My4-AEplBKdnUiOek-AzjCKRmKkvaUNRiu_0BHBp11PkJFUsbg0uVEsaB7imCi0HDSO02zTQFLRQDMUtpNbjFVERzslntWBA7pwhffUyHGW-1fhG5BcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با پنجره ی بسته و کلی مصدوم و محروم و فقط با ۱۲/۱۳ بازیکن با علوان زاده ای که الان خدا میدونه کجاست و ادام همتی که بنگاهی شده رفتیم فینال آسیا.
✔️
✔️
با برد جلوی السد برای کی کری میخونید بدبختا؟ اخرین افتخارتون تو اسیا کوپا امجدیه بوده که چند تا تیم محلی رو بردید سماور گرفتید . حد و ظرفیت شما همینه پنجرتون بسته ست ولی بازم تیمتون پر ستارست با برد السد میخواید برید پای سهراب بختیاری زاده رو ببوسید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/140145" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140144" target="_blank">📅 11:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=vCYL4WJe4AhjABTF7eqgsuPHcfSmxiHEh1MqJBeTTbjPafMmvSyBS8-aGR2a0R6wXHw_e9wuFCDUhxGv8DP3Ex9V3lVpV2EsLBHqUPQoN8ARqoK0a6tdZubB9BtYDxO2rL6KAyqJ11KZiaDoiyUfRG6q7_5YZUjaYrlPvq6IWtH7qNsYZRUDUYTkcJhFYvIP3BpJf7MxiFy9PZ4ZktgL15lndN8Ugxoy1EZ_xxUBsfvZbOksxZkqHwcHsXB2LB03si5mZgw2jeKy3csJ85SZNBPMbaTDB_iP5bW4nfss16Jafln__7aRY9L2gFo7FrTTMpYjKa7NoaZbut6oiv4cNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=vCYL4WJe4AhjABTF7eqgsuPHcfSmxiHEh1MqJBeTTbjPafMmvSyBS8-aGR2a0R6wXHw_e9wuFCDUhxGv8DP3Ex9V3lVpV2EsLBHqUPQoN8ARqoK0a6tdZubB9BtYDxO2rL6KAyqJ11KZiaDoiyUfRG6q7_5YZUjaYrlPvq6IWtH7qNsYZRUDUYTkcJhFYvIP3BpJf7MxiFy9PZ4ZktgL15lndN8Ugxoy1EZ_xxUBsfvZbOksxZkqHwcHsXB2LB03si5mZgw2jeKy3csJ85SZNBPMbaTDB_iP5bW4nfss16Jafln__7aRY9L2gFo7FrTTMpYjKa7NoaZbut6oiv4cNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم ایران به امارات توسط مزرعه(89)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140143" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=GA9JF_l36l2EVK7oTFAHCPC2ZFTP_EHvJvg4-LzLbItKhNjHBk-BSq1YS0juR-YHSWyCQYCEV4Qfu4oO_KIgeC1AEU7BMmviS90GyouqKR22Y4O3qXvod_dfAFfIUbg5r3F0Lpb4OhHlIxv46yS9jukFSsPNqBPzzTpGywxb_kFxghhfWPvoQwm4NBluyQw7Vc_HZf66XXqhWV19wbJGnOjDpSUYsj1DAFb0Ua9wwEJHgg06qK-cocF0hOaTSxTaF94_AlZxQNzVwA1LFVkIdMJk0aZvcXf53_lD-cs0tzlwlmV8BR0p1S-y4a36qkhOvEjEwvUOMXDnzMkdPtlo5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=GA9JF_l36l2EVK7oTFAHCPC2ZFTP_EHvJvg4-LzLbItKhNjHBk-BSq1YS0juR-YHSWyCQYCEV4Qfu4oO_KIgeC1AEU7BMmviS90GyouqKR22Y4O3qXvod_dfAFfIUbg5r3F0Lpb4OhHlIxv46yS9jukFSsPNqBPzzTpGywxb_kFxghhfWPvoQwm4NBluyQw7Vc_HZf66XXqhWV19wbJGnOjDpSUYsj1DAFb0Ua9wwEJHgg06qK-cocF0hOaTSxTaF94_AlZxQNzVwA1LFVkIdMJk0aZvcXf53_lD-cs0tzlwlmV8BR0p1S-y4a36qkhOvEjEwvUOMXDnzMkdPtlo5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل دوم ایران به امارات توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140142" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5qwJkJo0vACdLB4UMu1ySgCDx2Kp4BC44AhGIeTkrBJ7JqFZFE-lKioV2ZMRFHwE9WPTwJGhtjj3KVBB7QsFfFdVcTxBjKDnnvVwdBsBVoGKv4rEnvwlhYsmSmHqnx4jmbzT1pdNIHabCBOwK7xUn0tozmZ9OZoPHjMiAvtyaOT8rGlymip35nS1EXv9m-NLsgaFKkLw0UZ4sR3UUHhgJs2H_6GCzceneK-juyGmeYbPAs1qKbP2eEnbHzxW8f6zO1tP1g5vaRcCjcgJ1Rd0znCt7F3K2yT3jVqkR7Du9korr-U37mHGgrm1xNnHD8ni-RNpkmZlm0B7q6V2BfY56Rk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=cZYxeQPCds39kDpsW0-zQwWNm6NSp_-6rqddyKVKN1qf7jeK5Mzi_uFoOVyA_M5WGQkzDR4J4riOkwR1JuxAnAGdGG-mU47wHzeRmkxzUICbNYHBDr5SyxWbX2DJIbDoOzTlhli-6u1K7L4-VDW-p0CT97DNju7Imso0jzQvxXiCdwD9UTXdlZs5zE_Dty2FCPx-6Bx8_DoBC4fDF0eH5_INjH-MgBdRFrtu2iwes3owNJAteiLdOJimL_mBcM6HEiKCNRcWJo4tg8P9SvoqwQvT1Ae1fjO5V61WEcQOwZEDOsiVNPUV9BwTFm5zs9I2Rf4BLdwF6T67s7Mt2poF5qwJkJo0vACdLB4UMu1ySgCDx2Kp4BC44AhGIeTkrBJ7JqFZFE-lKioV2ZMRFHwE9WPTwJGhtjj3KVBB7QsFfFdVcTxBjKDnnvVwdBsBVoGKv4rEnvwlhYsmSmHqnx4jmbzT1pdNIHabCBOwK7xUn0tozmZ9OZoPHjMiAvtyaOT8rGlymip35nS1EXv9m-NLsgaFKkLw0UZ4sR3UUHhgJs2H_6GCzceneK-juyGmeYbPAs1qKbP2eEnbHzxW8f6zO1tP1g5vaRcCjcgJ1Rd0znCt7F3K2yT3jVqkR7Du9korr-U37mHGgrm1xNnHD8ni-RNpkmZlm0B7q6V2BfY56Rk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول ایران به امارات توسط شهرآبادی(49)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140141" target="_blank">📅 10:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140140" target="_blank">📅 10:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl0dEdg5CShjVr1GYTi8fY_gZQJY9qD7wHnsDZc6dbkJQijGjkiX9uLrc86dlU_xYpLpC1M7eXVjr0ChYe3Tc3FBVMCxi9DsOKyGbP3OzvSjwaTXEnxcyXGxDTUTRb-YKxSRsOPMjynNkKsU-8jjEiIhAhKr5VKbGcn4Znr1VKlANwr60l38sJyKdNYWKPFrbORwqUt_kERYWsir1C244OGbW17N6U4xlHRKXjX1Yrwq7zo-Io-uoxLwaNgkYHpqKYmWK4dp6rz95TqDsSFcMNn7kPll_PIxZxqxPOUYRxrdzCJrK4KcHx5h-i0pmx8rsp3hyMQ-FaWEBgjZb1tpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/140139" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCiGNOqNjNiuw0FNL6jtLhcj-ftRH3SZ6JFFhmwHbb7zb5k0NSzo8A3BimELRi6SxXVVPGbNzgRyEJgnDDDj1qyNONkl0kE5zgxQ54NgThRW6DUp8Gh1s8Fz6_JokRI6KbURWGFxp0R8QxHNQTYwlbApNAe7-5SaRM7XvHkBIjaxqp-nTBydUbTMPd3LbtUXx0FUbTSka4GvNE9i97pBlacfNk_3qKtBbgu7w53tg5Pp2sMDwPU1MhzEnAAlK6swfauotZeJ7DEiBgbcO49vGGjrlJIKQiOUd6zLMXCseVvidWWhkx0akSCpDNGHryNhnsAJv0HqilNkK989V3DhOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140138" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IwIqHhaXt7lzrDqjfaSX0DdxdCh6bE_r7FQJ9pJ5fWcMopQ_jy25o0aK8nBLsK41HXUY7PR4PVYcvxMXo25hZxATtifq8oqsevYVXzJXFfgi3Qf1Kqm_RSUSfWTLsIh7246f6ZSK2dgSKef5JSGsqPGyjLqGWOzRekOt_-apKGnK0tCQbpkw7BXanDWjYjF38Csn6g_HGIyZQslq1Rs8qhRSy_Lv9J_QMrD_Zt_BLsAYSIkqq7C6c3fqOPY5lJN0ldssxXd3KufrJTi62ckehB4FwRBatFFvB4El-dklSQqsUFaCJxQSV7CuWuqsUNbDclswZ3GJ1ny-FZxN_TmaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140137" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/140136" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140135">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7D3JiQrbpU3hSLser_qXFjUDcTdP2Ra6UW4PvWECnCYw15daS5p34K91y2fX-nVmNajICTQ0bWtQhnING7V9DDZzJYCNzq_IKDMwnbuF61amhP8cvg0Xs5rzVS9doKWJPN7pPkQftPI0_nmKFOtkYXLRDWQ_GwFDjsbkG2HuePVpEql69dyFGyx1xD053tJpUdDrsrBFn6WZd4SnWUX7lGgk8R0GfOLk1rJvq7fdPMhk1Ahqqx8zXUWqwPUvL52Rrm9eCKuyo51NXsk7RE4cJs9glRLYtjQn1WQk_-Zvkm3erydPobNuUToc_MWowjQtO215yie8Heuml34AJE0rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/140135" target="_blank">📅 00:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140134">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=ib5YQUoRl_FEVgHhQWaLxnZYi9upyzbDyBXehpdI0n9j3ZparbYQvuYTXhZbNzPUPCSU7vFDsTGVHYk4izqlpxhxqW2VndA5hIwz05-3kpm3nlHkIrv-Nvjvu5hJc1Yq01EPefmsCCyVnZ9DyP4eiskM2VLweEw_PVpgv6iGtoCNysWFDI6uHuGbtGChuTYCUtGl_GePsuX7CQCN_Zit7KnJsetHTx-P89ZT2RRKlSwwC26p5Jg_iqWc0k-W6jMa077zQ47H-FFk6EkiCLtlmeTaL_5PGVAuSynXRMzWxWFDYSNxPgmyDjKWdB17flj8-HCLRRKqJ9NhM9ep2v7tdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=ib5YQUoRl_FEVgHhQWaLxnZYi9upyzbDyBXehpdI0n9j3ZparbYQvuYTXhZbNzPUPCSU7vFDsTGVHYk4izqlpxhxqW2VndA5hIwz05-3kpm3nlHkIrv-Nvjvu5hJc1Yq01EPefmsCCyVnZ9DyP4eiskM2VLweEw_PVpgv6iGtoCNysWFDI6uHuGbtGChuTYCUtGl_GePsuX7CQCN_Zit7KnJsetHTx-P89ZT2RRKlSwwC26p5Jg_iqWc0k-W6jMa077zQ47H-FFk6EkiCLtlmeTaL_5PGVAuSynXRMzWxWFDYSNxPgmyDjKWdB17flj8-HCLRRKqJ9NhM9ep2v7tdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
پویا پورعلی، پسر خاله حسن یزدانی است
آیا می‌دانستید؟/ ورود همزمانشان به کشتی و راهی که در نهایت جدا شد؛ خانواده یزدانی و پورعلی همه پرسپولیسی، به جز پدر استقلالی پویا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140134" target="_blank">📅 23:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=Q3kiGzr2F9p1fqbhFoGTPGzoF1vO5AVmesHOG7V0xe0HMNMZ-A5roU7vrg_DAgz3Cl8Eo3RnQLj-eVHaLzI6SDz2iwTUGUTahcTe6bvbfUmOwdc2GUn-1yms3USXYxmQija9-v7pQUvPpJe8yIRuBeG96fCvgnEBhHLs9KR00V7SYYy_3Taxwpvyfd_pTfFJxA-3o4QEjLh6fVw85KlBe9o7CwJVTCTtx1CGZx6hn3INVw8AleIOA7QppvpkdWuN631Mzby6sHnIfHyRIZMm52zlRJKe8Mz1t49BiCNJYyx_YspmRdNT5mH9eZprRlW8lH6Y-DqxKHW6cIVr6zk1Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=Q3kiGzr2F9p1fqbhFoGTPGzoF1vO5AVmesHOG7V0xe0HMNMZ-A5roU7vrg_DAgz3Cl8Eo3RnQLj-eVHaLzI6SDz2iwTUGUTahcTe6bvbfUmOwdc2GUn-1yms3USXYxmQija9-v7pQUvPpJe8yIRuBeG96fCvgnEBhHLs9KR00V7SYYy_3Taxwpvyfd_pTfFJxA-3o4QEjLh6fVw85KlBe9o7CwJVTCTtx1CGZx6hn3INVw8AleIOA7QppvpkdWuN631Mzby6sHnIfHyRIZMm52zlRJKe8Mz1t49BiCNJYyx_YspmRdNT5mH9eZprRlW8lH6Y-DqxKHW6cIVr6zk1Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/140133" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=bDdbqheSrsPzrSCj4ZZyWpX9K_lXoLTpI5Cc63_9be5SwxHg720--miWJNzdk_Lywg8WvivtoOKX_-wDlZOOjib5Dw-xL7nG-8yNCGGFyaSEYzXqvavn-k7AGDLyhNXWHJ6S6iPbKEfa1wnYGnBsCG1shbfco3CtZq2bEfXP3jE_Fw0Xg8-taupb-F95ilpKbk3cZvKfFub3jxgvUXDYscKfOYhROS6slqgS6Z-YeeJId7HHAWdFrT3os13ugsf0AbaUhWXu2LsjTeueRtu_J6KRII9qu4zJb2ll-fGK2n9s11O52OaSxmOelik3degs662PqLn7gElPVXbKFPJtrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=bDdbqheSrsPzrSCj4ZZyWpX9K_lXoLTpI5Cc63_9be5SwxHg720--miWJNzdk_Lywg8WvivtoOKX_-wDlZOOjib5Dw-xL7nG-8yNCGGFyaSEYzXqvavn-k7AGDLyhNXWHJ6S6iPbKEfa1wnYGnBsCG1shbfco3CtZq2bEfXP3jE_Fw0Xg8-taupb-F95ilpKbk3cZvKfFub3jxgvUXDYscKfOYhROS6slqgS6Z-YeeJId7HHAWdFrT3os13ugsf0AbaUhWXu2LsjTeueRtu_J6KRII9qu4zJb2ll-fGK2n9s11O52OaSxmOelik3degs662PqLn7gElPVXbKFPJtrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
💛
🎙
واکنش عادل فردوسی‌پور به اسم‌های روی پیراهن بعضی از بازیکنای استقلال در بازی با السد: مگه خونه خاله‌ست که هرکی هر اسمی خواست بزند؟ یکی نوشته گودی، یکی دیگه اسم پسرش رو زده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140132" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=NG9jsyBGCnSaGc9Ayfelq3ahA4hqTCBLYeUJzA1D_JyWnMscPmUNrSyJk25cc4FUSB20CoCcc09naRtMdPhpA_-PcnN6nowgOf2VkCBEiKr_gTeCXS_Sius-iKn_g6GXnmuNYGj3TtE4KI5gHmPpY2WtiAWzR21_-ns98JTMyJ0umzR7T2OXW-EENvwi2D50pctIKXUOUg8I8kMGs4kVHXI_Nwf7cBpp6_988DdmvuF6j7PTFTQJiK7bBY4L3ss-PpGXyvZc4lyeehoFbVdd-kDjGeofcp8z82QsfSppdRkaIpNuo761eqzWPCCfj2FbDlnkLGovXVvFxX1sDEL9Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=NG9jsyBGCnSaGc9Ayfelq3ahA4hqTCBLYeUJzA1D_JyWnMscPmUNrSyJk25cc4FUSB20CoCcc09naRtMdPhpA_-PcnN6nowgOf2VkCBEiKr_gTeCXS_Sius-iKn_g6GXnmuNYGj3TtE4KI5gHmPpY2WtiAWzR21_-ns98JTMyJ0umzR7T2OXW-EENvwi2D50pctIKXUOUg8I8kMGs4kVHXI_Nwf7cBpp6_988DdmvuF6j7PTFTQJiK7bBY4L3ss-PpGXyvZc4lyeehoFbVdd-kDjGeofcp8z82QsfSppdRkaIpNuo761eqzWPCCfj2FbDlnkLGovXVvFxX1sDEL9Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محمدمهدی محبی : این همه هوادار داریم ولی چمن نداریم، شما کیفیت بازی اورونوف رو میخواین ببینین باید بازیش جلوی مصر رو نگاه کنین، بنده خدا تو این چمن نمیتونه دریبل کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140131" target="_blank">📅 23:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
پورعلی: الگوم آقا کریمه و هیچکس هیچوقت به سطح آقا کریم نمیرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140130" target="_blank">📅 23:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❤️
پورعلی : من به مهرداد میناوند قول دادم یک روزی شماره ۱۱ دایی کمال رو بپوشم و انشالله در آینده می‌پوشم ، می‌خوایم قهرمان بشیم و آخر فصل جام رو به روح آقا مهرداد تقدیم کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140129" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I0wFRFfzGPtleHrPbG7UYrVT8ssX4RWPwer5FUnsuIcu22zIAJKUqjlNxO69rkMG2wPJaYavKAehg0zQZYw8ktYBup1-qK79ueQnAF-9tJ9qhiNVvIWZ-s_iZCKnIC-djETOGF_JhyrMyje1Xp7Vcdi2Yz41bJ_FhKc46qDvkF-GcY2nCVJ07_1ziowEupBNAU-VjGUNanpap1J7ghO1Hh6k5bz6zXReHSSMJpTeS52hbgJdh7N2Ics3zJUvD3qQ7v3Qla9IQiAfj4GogkUNOLBMK-KwdIQRWHwdVfkcG38uTa3ygix7I6J7mOBTKh6631ICWBprnmZBqVUsJC_-Q2-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I0wFRFfzGPtleHrPbG7UYrVT8ssX4RWPwer5FUnsuIcu22zIAJKUqjlNxO69rkMG2wPJaYavKAehg0zQZYw8ktYBup1-qK79ueQnAF-9tJ9qhiNVvIWZ-s_iZCKnIC-djETOGF_JhyrMyje1Xp7Vcdi2Yz41bJ_FhKc46qDvkF-GcY2nCVJ07_1ziowEupBNAU-VjGUNanpap1J7ghO1Hh6k5bz6zXReHSSMJpTeS52hbgJdh7N2Ics3zJUvD3qQ7v3Qla9IQiAfj4GogkUNOLBMK-KwdIQRWHwdVfkcG38uTa3ygix7I6J7mOBTKh6631ICWBprnmZBqVUsJC_-Q2-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140128" target="_blank">📅 23:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">📹
همه‌چیز از مصدومیت زارع، زیر دوش و در حضور پویا پورعلی شروع شد...
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140127" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
پورعلی:
✔️
حاج مهدی یروز سجاد(پسر تارتار) رو اورد و یجوری باهاش رفتار می‌کرد که انگار نه انگار که پسرشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140126" target="_blank">📅 23:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
پورعلی:
🔻
من نزدیک ۳ بار میخواستم بیام پرسپولیس یبار نیم فصل ملوان که بودم و بار دوم که از تراکتور میخواستم برم گل‌گهر قراردادم رو بسته بودم با پرسپولیس و فشار هواداری نذاشت که بیام.
✔️
من و حاج مهدی رابطه خیلی نزدیکی باهم داریم و رابطه پدر پسری داریم…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140125" target="_blank">📅 23:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140124" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz0rHJO0kZRsr-PYdUHuoXTV-Pk3yPQ7yj-gHoqinBbtnvzAGITT4qyh7eArGbnV9qX0bG8oOLVVy2bK1G_uHSBbza7LtgLRto-PJRonyYe8kZtxMdeB5FxC0Ac7XYi7H89AngB8WyTQHZQDi8o47riqOgZHW0XzIpm9znR8MukJnphN5Hy9c3Wbwv-X6Ldi_8hPQ1PvGwQpsJKIo6xV7iuo1B-3kRgRKJdPvC9GH9LKvcssUP17yJHnvK7BNSz0-auK0U2giOHvqLozWg8NQsmt3kSWDOzLy69yBJntfvpXUX84uUTpe0nmJxKKMs-eiud_VBNUiAR0zfCMUu802g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر استقلال عالی مینوازد
😂
✔️
اسماعیل بن ناصر هافبک فعلی الغرافه (که سابقه عضویت در آرسنال و میلان داره) مقابل الهلال اخراج شد و بازی با کیسه رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140123" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140122" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXHyRqjohdyQlAm_ns9Q3fo_tVGgmZtMW68evPQSYaDNG5aJ0DIfh2AqVuu6KTN1L2-ffiwm7SMkvGGeEueNhWvheL88l_iWcDY2pQGswh82UFN1rxQ-j1n17lrEVFCmJ546KxwCjsy5Ufk3nqHaAXiVH-Ndt0iZSYTL0nVl9wxb9-GphbuTnv3-rDDVUvUBe2L8xKwaMV-0AqRyBHuLgzioOSsenq9lWL9C-c__UorsCcn6hA9atAVb2XmcpA_G10tdl6OhSyXvCvM0nsW8WaghoGz8R_-okhl9Vdvl7CODGLEmQgs7VYbA4Qxo02RdpRA0Ldfz8XFml0X28cegIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جام اتحادیه؛ لیورپول و تاتنهام، نبردی برای بقا در مسیر جام
🏆
🔥
[
لیورپول
🔴
🆚
⚪️
تاتنهام
]
⚽️
لیورپول و تاتنهام در جام اتحادیه؛ جدالی حذفی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند. کفه ترازو کمی به سمت لیورپول است، اما تاتنهام می‌تواند با ضدحملات خطرساز شود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
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
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140121" target="_blank">📅 22:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvfkrv_S7YZwJSEMLN2x4lS02HBvyRlxMH1IAGDOsiaQo_wLCojpXtVmbK6f8BZDsZN-feOCs_azwb8A5F39X0vgPCA_h45iaeihPjmuKHQ6PA93iwKQ2dB8gcuzKUOY0UwV-Dko3J6mMdZdyoKkiuEwNYLqB5jPijL-e__E-RYH6GfQtIEFvEeBFo-ybi4Wd2qqrsh0DU4IDNd5EqBdqWsswZwTbQYepWt4uhMYa3imu14Ar5Te-Bh7PPYp_S6kh_EWpXNbc-O6nEBZ1Ay2lUSVAUFjQS_btSQgXperfVUXSBkfupzvCN5N-M6YYhdNDrFrvp5wOQ8I_FcoDomxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی
امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :
پ.ن تارتار به شدت راضیه از یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140120" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
الجزیره امارات با مالکوم ؛ کولیبالی و تالیسکا و بیست بازیکن خارجی دیگه با گلگهر هیچ گوهی نخوردو مساوی شدن!
❌
پ.ن تیم‌های عربی زاییدن امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140119" target="_blank">📅 21:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD5GpTM6_1ywh7PCO3FcQnRaejxwitlV9ObXa6upt2koNfEh40nGajlr-AUP7A-7gLx6NGXZCJzo1AP4rgyPlnhXI3wSjCjHQ6r1k5WsJo2WS0LvbnRHwUfJO5V0QnTpTCjKtXHYqYxitXrLrLfyDX5lW4PMGODlnCLkwmqY7PL-TqyLstlfKwIr3qW82bjR3M_cdojcJxLyot0ysjl9jJf6q3tu5iRp-AuySQCAXPS85UlFa0dYW0yuyCsoJxN1nhb_d228zUDBuYbOl0ljwu8n2I88Ifh_HRZ-JY8fUkI7JhmBgykfBGaFdGUkJ9BJhGOb4KcxtkPW2GTCvMcPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140118" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt1rnoDidHY4dWBt7XlTGMjQ5TmRJbI0qJuzQTOnidGQz9JCDcCPMNRJSfb010WiV7J0jVzs6xEjrQGJ-9uBQk3yeLxPeu2Q8pUkFasXSWTyv8J-rxtaeWru0tZHSzQ4Z9HlGKOawPsI6G0Y3blyOz7q9lcqYAjmOpDuUcvFUs-ox_TL129xWXLs_ZnhN6behJKLXIKcu1zmM3VUSyji13iprtE5GTEn0wJEawTMezvL3jIdLOgR_5Zj5M9XtngbsLZJzchAc67tQZzw9TRX_sC_jk_BiEWRh-3kXvEcuqSUdLliCJI9uSfr_JfZ4dbe1bsEvaG9dzyh6aUdCIus3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایران ورزشی: تکلیف دنیل گرا همچنان مشخص نیست و باشگاه هم پاسخ روشنی نمی‌دهد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140117" target="_blank">📅 21:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140116" target="_blank">📅 20:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
تیما عربی انگار ریدن اونطرف الاهلی که 2 ساله پشت سر هم داره قهرمان میشه دقیقه 90 تونسته به پاختاکور گل بزنه و 1 بر 1 کنه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/140115" target="_blank">📅 19:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/140114" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
