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
<img src="https://cdn4.telesco.pe/file/FMfvbt8os8L0QgRgY3r1RJZqUjhGSrWgSJIFxwunHPHgHwT4GhS5eZeBCUuSJT8ZITdXW6o6K5dvNVcIVaxJFvMgvBYRuO2ZF1MLjTSVikVKfaMsReDPEO4GZyMfMTaXU6f40t3eZbqMn8Vvboax_KscTAcKq8Gq16pS9MwMBIwi64xlpjX81dlz58Jpm0qSKBaXHYTWDisQN0WI8u8Qgwgvi0owv1DRDPeIBsgrkFXh7sEeJmRdWvwTqysolLkOk2NLKgZ20-iXpex03qudmuS_NrD4fi2UHHX5LmU-vKV6mhONBL9CEQyeLc1rnJnABfCMpnNMxpFQyIuhJKBSgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 04:34:56</div>
<hr>

<div class="tg-post" id="msg-140090">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmNNXsIwDMZSXYUPri4u_wWZY93WAIe_GSUPCnNzB0Wr6l81yQkITQMHBm-Mmo9fIzoT7FuQz70Sf-t250Nr-YvWxlD5qoVpMjtUwygeb3SGbKowqpbTVZOSQb6d0TBUh5cK6suKFkpBYpbcuD2mdtTmBq8LIjXbvw28Zeba3JK5igF50LXqpPeAj-2SfPnNoEN7vmL3CjMtA89HeeFfNHjS-CfbvzWR5MxlL2Un1GSrQ0gUilVM5c-9wgfVbVGLSpK0zaCZ1HZtbeluCyPYhqAmVj4cWCLS9JR6SlMmUcOtH0m0xl_kNlcnxfvQWltc9hxck12e9ag2F6Ux8W2tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فردا شبِ پرهیجان فوتبال؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین داستان فرق می‌کنه
🔥
⚡️
⚽️
فردا ترکیبی از بازی‌های کم‌ریسک و چند تقابل جذاب برای دنبال‌کردن دارد؛ الهلال روی کاغذ شانس اول برابر الغرافه است و رئال مادرید هم مقابل الچه دست بالاتر را دارد، اما ارزش اصلی در بازی‌های نزدیک‌تر دیده می‌شود. لیورپول با تاتنهام می‌تواند از نظر ریتم و موقعیت‌سازی دیدنی باشد، در حالی که آرسنال مقابل ایپسویچ و فیورنتینا برابر پیزا با توجه به شرایط بازی، گزینه‌های قابل‌توجهی برای بررسی هستند. در مجموع، شب شلوغی پیش روست؛ جایی که تفاوت بین «انتخاب روی کاغذ» و «انتخاب با تحلیل» می‌تواند تعیین‌کننده باشد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/140090" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140089">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
حداقل میذاشتین یه سال از حماسه ۷ تایی شدنتون بگذره بعد کری میخوندین نخبه های لعنتی، هر وقت رسیدین فینال آسیا میتونین کری بخونین هفتایی های جوگیر
✔️
✔️
کیسه‌کشا هفته اول آسیا: بریم واسه ستاره سوم
✔️
✔️
کیسه‌کشا بعد حذف: عشق فقط فوتبال اروپا
😂
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SorkhTimes/140089" target="_blank">📅 00:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140088">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk_wqyZEhshrrVkpQO3oJUB4KybweLJFKieR336Nm5EzMzgGrtTp17y2xR6a5-Kor-QrWrV1mfUwV5VkCp_B6ZRvEnZ6eU4tx6BrPA6t-plXfpc4EwFA-7rOgzhe2rjUDkf7LRpu0IzalO9Uzi9wGla3Agin6SQEzeWOaEmAi3FY9Th0k9emDZGib3W1WMz3c10eZm7SCqiQN5HP7RYzr_8rvl5saoEttDShQ84T043nkoxJedI0CCpyjYwnePFrjUhaSBLALlpvzm6VeSQOH6rU7rYLBEuZULX01bCI_BvzR3jTZy3k5M8KeLlKnbv2jplB5hfVYR9-jz4WyBleMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اگه برد تو بازی اول لیگ نخبگان تضمینی برای موفقیت بود که تیم جواد نکونام در فصل آخرش تو استقلال که بازی اول سه هیچ الغرافه رو برد هم ۳ گانه داخلی میزد هم تو آسیا نتیجه میگرفت ولی خب اون سال اخرش هشتم شدید
🔴
اتفاقا جوگیر شدن شون بعد یه برد تو آسیا میتونه به نفع ما باشه و اون اعتماد به نفس کاذبی که بهشون تزریق میشه کار دستشون میده ، حالا خوبه بازی اول بود و هنوز بازی با تیمای اماراتی مثل الوصل و شباب و بقیه مونده حالا که انقدر خوشحالی میکنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/140088" target="_blank">📅 00:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140087">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v4rGCcOPtcyA8PtC0qG-SSGmYl8PIhDqzM1zUdlOh5zlkEvqo6oMi-X5bnJdJ0PJn2R3r1X8MdZa4CngGz363rs756MGjgRZkPW9dUoHBXMmVLqVK6gy9gM4EUVabqhuK9JLBD-jQP03ViRh5SxcjIK1cUqPbjqU_hGaoVThhpUbXa0U6BKSeb1mjb5NQ8dhHrN7BjNdUeWwfanTvQOehW72iRbBjCQUNOWsp2JCY2UCBzCbNjRoKLqUWLKwSw5GOOmwMqZtHGhW3B3FGl7YR8e67DClEg3WYyeTDLbtwcT97Bu5gCaCz07Uk41xscSY2UhreQzTvAtj0l7vV1w6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس با اختلاف بهترین تیم ایران در آسیا طی ۲۰ سال اخیر
❌
علاوه بر دو فینال آسیا و سه نیمه نهایی از نظر مجموع امتیاز هم عملکرد بهتری از بقیه تیم های ایرانی داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/140087" target="_blank">📅 00:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140086">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/140086" target="_blank">📅 00:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140085">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQqWi17OcUMCiL2HTv95OZ7teM6ULcrqI5cHuZPyKGV0wMnAJ2SeioAuKumefnlNkVI9exqbayJctqrqXaTyST2aArA4BfRIV4nEWwb-ySUyi0hbIGXGX8dknbY8EVoIjXgszW8MsEt8L9gzbyH-0AwXU3au-NlwvA1DAk13wDzdW7x_BN_pgF224CBuHugprB-ysT-XU7PIJ9RgI_WPc1umWD_znMYz-Pi_cPLz_ru9jL4Rlv4LZWXG2saf3sjKTdSjvtEyPr6qhJBlAn4wcmuH7ZFU4aU9gIgE5gNVgpK632j89CwAXOdiskF3NZeXfdhO4Zh4JbZku5DCWz4nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/140085" target="_blank">📅 00:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140084">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SorkhTimes/140084" target="_blank">📅 00:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140083">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
السد هم از آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/140083" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140082">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/140082" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140081">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/140081" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140080">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/140080" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140079">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✔️
باور کنید پیکان هم این تیم السد و میبرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/140079" target="_blank">📅 23:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140078">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/140078" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/140077" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O2nPRXd4LMRwLCuPqIikvWPWMFm-HsLsQTDw_5CK7ONuEEFDZXnYhXbT1WGTWX3yk3cSeljCVOSismNPZLweiYXz5Dlqs43Lyjodh-uTWMC2gi2a8Xydl7xclLu-smu1-0DkcTr2od89tzcWf8oTuYsXcTHJG0G4whxbBlv677NmqVe-LBbv42Jp_QcbhVSQy8ziroKDKGn2X68kyamJ-TjTK6N5jAU3cQmpqMizrQPY3z70Eqs8UwMAb0l1gSx5comL8eQH-E0tUiCQIKaUKO7_jBnrN9X7YbXlNMzWsM4AekUkBBF_xYiTghc4ET_NgcD7dYJ_2Qe3QCYy6Z2KzCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O2nPRXd4LMRwLCuPqIikvWPWMFm-HsLsQTDw_5CK7ONuEEFDZXnYhXbT1WGTWX3yk3cSeljCVOSismNPZLweiYXz5Dlqs43Lyjodh-uTWMC2gi2a8Xydl7xclLu-smu1-0DkcTr2od89tzcWf8oTuYsXcTHJG0G4whxbBlv677NmqVe-LBbv42Jp_QcbhVSQy8ziroKDKGn2X68kyamJ-TjTK6N5jAU3cQmpqMizrQPY3z70Eqs8UwMAb0l1gSx5comL8eQH-E0tUiCQIKaUKO7_jBnrN9X7YbXlNMzWsM4AekUkBBF_xYiTghc4ET_NgcD7dYJ_2Qe3QCYy6Z2KzCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید دستمزد بیشتر بگیرد؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/140076" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/140075" target="_blank">📅 23:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/140074" target="_blank">📅 23:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⬅
➡️
⬅
➡️
پرسپولیس در آستانه خرید امتیاز بعثت کرمانشاه و تشکیل «پرسپولیس ب» در لیگ یک قرار گرفته؛ توافقات دو باشگاه خوب پیش رفته و احتمال نهایی شدن این انتقال در روزهای آینده بالاست.
⬅
⬅
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/140073" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140072">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/140072" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
حامد کاویانپور به پرسپولیس بازگشت
🔹
حامد کاویانپور، ستاره سابق پرسپولیس، به عنوان مدیر فنی آکادمی و مسئول بخش استعدادیابی در این باشگاه مشغول به فعالیت شد.
🔹
کاویانپور این سالها مدیر تیم های پایه پیکان بوده که از موفق ترین اکادمی های تهران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/140071" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140068">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/140068" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140067">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/140067" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140066">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIN0pUGLXF9ALGK3GwAfoJj345u1af1b6xIrfVvKJccN70gpq4A85xkRV7Fm8Gtip5eHPEu-2AQ4VLI_Dmevg9l-Pm54kIFLXffUY2W_pLg93Ncld-J24_o_yjW_OFJdP2nfhF0Sqc6DvQ3LfzS1oIBpSRX2KyTnZioIdcJwdr4dem2s-_7sfHfGrIlaw3oVEutNAdMzL8YuRUNej3Wy0YHBGPAEspJWX9jalrFTfEvKEi3-1AiPh18JENu5lvLVpAvXwhDBeZLC-IC6ih4Cs4h35G86H7rZaZqsa61TTEZgdi_tNRf-9YGqLl6uCa1mnWuQKs-qLRPSUHpBDPG4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟧
🟧
کیسه گل اول و زد به السد
🔴
گزارشگر میگه غول آسیا گل زد
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/140066" target="_blank">📅 22:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140065">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/140065" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140064">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/140064" target="_blank">📅 21:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/140063" target="_blank">📅 21:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140062">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140062" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140061">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
ترکیب السد برابر استقلال.
✔️
سعد الشیب، الساندرو رومانیولی، یوسف الحناچ، محمد الوعد، پدرو میگل، محمد منایی، روبرتو فیرمینو، کلودینیهو، آگوستین سوریا، اکرم عفیف، حسن الهیدوس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140061" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140060">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
عملکرد مثلث هجومی السد در ۴ هفته اخیر
✔️
اکرم عفیف: ۵ گل، ۴ پاس گل
✔️
روبرتو فیرمینو: ۴ گل، ۲ پاس گل
✔️
کلودینیهو: ۳ گل، ۱ پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/140060" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140059">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwOiU2KCCzFZKuzURGVRZZcPihTzqlRbOHklUyvfJ3XScEbLlJdZSU_rLNUvaJ4Bfiw94XwZrCBDhYdQ_PcwmDBPsTyy2EFSYpBXTD0JKc3hgqeTLdGqXgepeZs3kEQK2ag62eNDbCCKhr2qRLoTo_LkoByTvtf9OTI6V8VXfOQmpAP9uJR4jqzPtGiKLje-nykZsVQ1t_G0h5aNXo_V0H4eNKR5g-959dOqZ1nKyd3r3z3v3Je-ilEWz8ZAReihleRRaUgcQSiSiDozQ8ExmL9ASTg39aIkgnBdaSE-fqE62DNU6UkB23otR7G9q4ONJNfu1T7vbibOkJcekZgnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
آزادی 10 زندانی توسط مهاجم استقلال
❌
باشگاه استقلال اعلام کرد سعید سحرخیزان،  10 زندانی جرایم نقدی غیرعمدی را آزاد کرد و آنها را به آغوش خانواده‌های خود بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/140059" target="_blank">📅 21:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140058">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/140058" target="_blank">📅 21:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140057">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/140057" target="_blank">📅 21:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140056">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/140056" target="_blank">📅 21:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140055">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRLXlWsfTjf7vMyd_ZuNiV25QqRTQ63IAgAkQo3kYAfABbE_O7Ktk3jhrG4SQ7E9glXh0oEqHHfER9nCFZ0WfzZm1MOX_Sypbl-PHXXkXWW8uLZeTSwLsuoETujNFNM9kczB_tcDQfnlkSrTEx0Xsxq-GZWKfsM2dpR8croJU6YQCCAQIQucRpgALtjBYSfNRdYZYi6ifJiG1t8oUgZfyI27KU-1T3FhBLsOOQ_y8eXQsahKXh2RAo8QcDW6RmvoOxQ848rPupe1wlb_2STVSXr9atrr8ztkGAyB4Jcw2z-l-32O6O9SUOptlSZhgAxw_xOs5DoyhN5u7ovjqDqHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/140055" target="_blank">📅 21:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=F7C-0wqunaI-6AGWxCWV4UBtzl-QiZJiV94gcQ91gC9P1UMboXlQEOjjPlunyeK8H3jZ3hZivbIB9WvDcZoW1gm7TFPE7KiXf1eEPdtdE6g6KX8M_xkhMrbvTV1MD9-w0r0bpIYfBSpr7dgK06VgW_cfBF9-xgEcpKRmGxQxTTElDUMIc7dD_we_EXT1u28541-bYYEwnueBClsxHCzma3uEdibQ0tgwz1qQSZWlA3cQnoS8oEqL8GpwyI8rs21s0MJubjntzwG3V1k4cG6Nci43F525ZTyRwM6bz4u5XH-9d3KTVwSMOhKtnngxSk_3D_uyow70TcqhKgj_ZvjAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=F7C-0wqunaI-6AGWxCWV4UBtzl-QiZJiV94gcQ91gC9P1UMboXlQEOjjPlunyeK8H3jZ3hZivbIB9WvDcZoW1gm7TFPE7KiXf1eEPdtdE6g6KX8M_xkhMrbvTV1MD9-w0r0bpIYfBSpr7dgK06VgW_cfBF9-xgEcpKRmGxQxTTElDUMIc7dD_we_EXT1u28541-bYYEwnueBClsxHCzma3uEdibQ0tgwz1qQSZWlA3cQnoS8oEqL8GpwyI8rs21s0MJubjntzwG3V1k4cG6Nci43F525ZTyRwM6bz4u5XH-9d3KTVwSMOhKtnngxSk_3D_uyow70TcqhKgj_ZvjAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/140054" target="_blank">📅 21:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/140053" target="_blank">📅 20:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=IOPBU-4S76bvqpDshsSdpMhATluMQo-R3292Zclxsmosoa8vePp6VNwClzsWpuCQJ9lmK9LVvNXshrRM8nZBhFLpf52DlEz7XC8U8whfvKx_fign6Q2SAUzNIM5qnTxw_CKapVkeq-TbgCrjn6-QYzIDTsSlEd8tDOxRx1uk-ixX_q2RTi-F30tmi2_T0v0JQQOhEBqf7UzJV5xGIOqlmuCduECBmc8g1tbgRpQO2iC1b4hwFIWQIEE8_8Q9wmwHvZ-R3wfnJn5mrh6FQF1_W2LbDN-uAGAOo7cg78MUDtxfh76PVEOQhIi17uzNFLW0itc7tBK1RtDrAEuFkf5dyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=IOPBU-4S76bvqpDshsSdpMhATluMQo-R3292Zclxsmosoa8vePp6VNwClzsWpuCQJ9lmK9LVvNXshrRM8nZBhFLpf52DlEz7XC8U8whfvKx_fign6Q2SAUzNIM5qnTxw_CKapVkeq-TbgCrjn6-QYzIDTsSlEd8tDOxRx1uk-ixX_q2RTi-F30tmi2_T0v0JQQOhEBqf7UzJV5xGIOqlmuCduECBmc8g1tbgRpQO2iC1b4hwFIWQIEE8_8Q9wmwHvZ-R3wfnJn5mrh6FQF1_W2LbDN-uAGAOo7cg78MUDtxfh76PVEOQhIi17uzNFLW0itc7tBK1RtDrAEuFkf5dyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140052" target="_blank">📅 20:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5804386d73.mp4?token=HMwcpgi9hmbOGItVWbodWo_4RGjtjpkvdpwMoslcO4r2RbpqPhIacakeiKEqlCPhJkL3PZASIPRqjlqFpGGBv0C0L1fEffLtoBvCLJHICBADX8_pi6aTCKGiwbln9FVSSIks6ArtCbEUn9TbCzc1v1HnJEuiz_DtRY_vlKWlq-LLQalwsM9N_Kd0dYCzagr5-1uDTdULM3Oax6ixB5piT70s4wvnz8Vw4x58nSzN-Xkvz9-1FCUPXhbsnMO_QR7snHq5G153ZK0gYkECZFdejqoHK7L3cEhEAO00SGOn0WohUA9MZODoXEzPcrbpqLBHIl_qzCIkhRF0azQOZFnCqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5804386d73.mp4?token=HMwcpgi9hmbOGItVWbodWo_4RGjtjpkvdpwMoslcO4r2RbpqPhIacakeiKEqlCPhJkL3PZASIPRqjlqFpGGBv0C0L1fEffLtoBvCLJHICBADX8_pi6aTCKGiwbln9FVSSIks6ArtCbEUn9TbCzc1v1HnJEuiz_DtRY_vlKWlq-LLQalwsM9N_Kd0dYCzagr5-1uDTdULM3Oax6ixB5piT70s4wvnz8Vw4x58nSzN-Xkvz9-1FCUPXhbsnMO_QR7snHq5G153ZK0gYkECZFdejqoHK7L3cEhEAO00SGOn0WohUA9MZODoXEzPcrbpqLBHIl_qzCIkhRF0azQOZFnCqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول شباب الاهلی به ترتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140051" target="_blank">📅 20:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPFaTe18O0cxZzc8LgUEUWKf7pD-U2xbPmfaMKQIpk5QPrlg727p0RFo2t5cv2DdBNE5MDar6gc2tY9MglhP7e20fSt355w6ZRVi4_BHzRS6-aGLB7cmzC9XF4jOT5EN0iqBDNfDJixLFS79oPUVbzamFDrRmu0pGs3AFgqWe6MXSKLCgy4egi7H3Syfp8A5oGCsPToloNC6juvfRtk2X10n7SF4uwl28TDIBBNCp7kZVRe8s7m9FPTbqEOnpJDni89SxEQ4hIz5uxm285Ux-zc5CkfCVBVRL8EoFQ-gCdNGHs1FPmg6OO4vYH4nzOwxnSfufwU93VbRsB0_8MsVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
Esteghlal -
⚪️
AL Sadd
⏰
Tonight 21:45
🏟
Basra International Stadium
🟣
استقلال با تکیه بر ساختار دفاعی منسجم و روند بدون شکست اخیر، احتمالاً بازی را محتاطانه و کنترل‌شده آغاز می‌کند.
السد در نقطه مقابل با ۴ برد متوالی و خط حمله‌ای بسیار آماده وارد میدان شده و روی انتقال سریع می‌تواند استقلال را تحت فشار بگذارد.
با توجه به کیفیت هجومی السد و رویکرد محافظه‌کارانه استقلال، بازی نزدیک و کم‌ریسکی در نیمه‌اول محتمل است؛ اما نیمه دوم می‌تواند کاملاً متفاوت شود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/140050" target="_blank">📅 20:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=MbSDKPbZJP8IWekS2g9H7rvxjd9bOYHt6u8mZZUSRyQrpesVDRTyzTHOhGY2Pw_WRf87TpVS2ad0XQBJafr5hBollHvnWgvzcmknMoTzbXfSqf2A8VC6Irpk9lK5nnguwDjfOT9kq7hDX-Gc9P9Xfpg6kBIW_ZEARDg1-IJRTju1IAiKrb57q9uleiP7DBiywl1_H-OHnCZX93i76wBGfj4_0zv-iz7-QUOxgPG44b_jBYxSoBXnb1JnYPn7WtPkrKG6_C0KQjxRHUrzexvKDcSgqjtZP1JfkH5vMKX2ZfjjIcQ9Z8Y_ZtHr6rt08ndHa0w5uuwT0dT_YzC-55jYOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=MbSDKPbZJP8IWekS2g9H7rvxjd9bOYHt6u8mZZUSRyQrpesVDRTyzTHOhGY2Pw_WRf87TpVS2ad0XQBJafr5hBollHvnWgvzcmknMoTzbXfSqf2A8VC6Irpk9lK5nnguwDjfOT9kq7hDX-Gc9P9Xfpg6kBIW_ZEARDg1-IJRTju1IAiKrb57q9uleiP7DBiywl1_H-OHnCZX93i76wBGfj4_0zv-iz7-QUOxgPG44b_jBYxSoBXnb1JnYPn7WtPkrKG6_C0KQjxRHUrzexvKDcSgqjtZP1JfkH5vMKX2ZfjjIcQ9Z8Y_ZtHr6rt08ndHa0w5uuwT0dT_YzC-55jYOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
گل مردود سردار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/140049" target="_blank">📅 19:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140048">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
ترکیب شباب الاهلی مقابل تراکتور با حضور فیکس سردار آزمون و سعید عزت‌اللهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/140048" target="_blank">📅 19:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXKH4iP9ZHKmFgw-x9Qa9Om1MmgF9ga28BP-E0rzVjm_2vo9vb1nfvl7W7pGNJZO1Ys--H5QCWe_oUI4inaZjF13ahoHP5rY7knOchFpMvNYfhR4oPtsj5TlIk6CGnOygMw1dmR0WtH806mVt-byTNRzvfEO6MDSJGmIgNlrCAaq9V_1f_1msBGUFLBWacprb5wqwwPPggI7hUCjUTLvj4eqtzf3g43V527Ld1A0Xn8XHH4SIfdN9Zo2tClfzvmTiqjPK1k5bgS5ABoKqJxxgvd8Enet0kNABIehdw5ybOTB4fNyRXQAXDiDSajCFlmEU3L-as9HOvRlRFISJlIddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
علی علیپور با وجود اینکه پرسپولیس یک بازی کمتر انجام داده، همچنان صدر جدول موثرترین بازیکنان لیگ رو در اختیار داره.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140047" target="_blank">📅 18:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140046">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140046" target="_blank">📅 18:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140045">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140045" target="_blank">📅 17:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140044">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
پایان زودهنگام حضور گل‌محمدی در عراق
❌
ادعای مجری شبکه الرابعه عراق: یک خبر اختصاصی داریم که با توجه به باخت شب گذشته باشگاه دهوک تصمیم به قطع همکاری با یحیی گل‌محمدی گرفته است.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140044" target="_blank">📅 16:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140042">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
🔻
دهوک عراق با هدایت آقا یحیی گل‌محمدی در هفته هفتم لیگ این کشور متحمل شکست شد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140042" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140041">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✔️
✔️
شایعات: حسین کنعانی، حسین ابرقویی، امیرحسین محمودی و ابوالفضل جلالی در دیدار دوستانه امروز پرسپولیس از ناحیه زانو مصدوم شد.
❌
ظاهراً کیفیت بد چمن باعث این مصدومیت‌های عجیب شده است…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140041" target="_blank">📅 15:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140040">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140040" target="_blank">📅 15:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140039">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🔴
❤️
ورزش سه: دلیل بانداژ دست امیرحسین محمودی تکل او مقابل ذوب‌آهن است که باعث آسیب جزئی این ستاره‌ی جوان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140039" target="_blank">📅 14:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140038">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqYgmJwy0J79193Q_17bV_PJaRCwOV06poNbjzKpsXiWVzM3E6HBYH6-hSLJNSuaW9cYk9GA-G9fFevyatPzGtSdixUUjOfO3CiVrkobGzBas1saF-QlSn9ku_6Tx-whnhi8t3PBwJhPc-bvgfVLIb23JEo3H9kvuYNqbUxQfRcvcLFyPZJUvdwUyJLx1fqyX3bama25NBXUYG3k-JXD9KnBHW1-SZBmheulX7dpo9SsuJp3b5agf2Rrru37qxEQG7Xk_l01XptT7Z0e3XaiAKE7nhpMpbHFm5Op51YX6RKJaGQGt90saknMGCXNjqdywSDwrj7vwSiZmWCENt9f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
استقلال در آزمون بزرگ آسیایی؛ سدِ السد مقابل آبی‌ها!
[
استقلال
🔵
🆚
⚪️
السد
]
⚽️
استقلال برای گرفتن امتیاز مقابل السد باید اول بازی را کنترل کند و در انتقال‌ها کم‌اشتباه باشد. السد با مالکیت و کیفیت فنی بالایش می‌تواند خطرناک باشد، اما استقلال هم در ضدحملات فرصت‌های خوبی خواهد داشت. در مجموع، بازی نزدیک و تاکتیکی به نظر می‌رسد و جزئیات می‌تواند سرنوشت مسابقه را تعیین کند.
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
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140038" target="_blank">📅 14:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140037">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
🔴
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140037" target="_blank">📅 13:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140036">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140036" target="_blank">📅 13:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140035">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
فووووووووووووری از ورزش سه
🎙
🎙
علیرضا بیرانوند از اول آبان به طور قطعی و صد در صدی سرباز محسوب میشه و دیگه نمیتونه برای تراکتورسازی تبریز بازی کنه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
〰️</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140035" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
تیکدری‌ جای جلالی را گرفت!
🗣
🗣
مصدومیت ابوالفضل جلالی می‌توانست برای تارتار دردسرساز شود، اما مهدی تیکدری‌نژاد با عملکرد خوب در پست دفاع چپ حسابی جایش را پر کرده.
🗣
🗣
تیکدری در ۴ بازی اخیر فیکس بوده و پرسپولیس در ۲ بازی اخیر کلین‌شیت کرده. حالا با این عملکرد،…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140034" target="_blank">📅 11:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140033" target="_blank">📅 11:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140032">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140032" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
😁
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140030" target="_blank">📅 11:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_bwC0Ky2a1nNLE7Ctv4C5VRfWZiqpgY10EqkjYKdnvYz7m94_rpRH0MV0r_DTQGIHP4a8UaS-dQbtPkKVs7QWUx8Byg48CnjADKqfGvlP4mK6yKlPFGyljVp9icJ2bFvzSKLWTvpbSr3bqlKCu250_Y4dXLH3dpIXuJJdvfKsLbyuRrFUWYpH9WHc_vEO5Szy-yvV7DajOg9j34m1bB5thdKHbdw9iHifLn1GoIpQzgIIuQFd5DxUoxtKyNPQfE32O8C_r54csnahJPTnVnPn0_rvR1wsK3OcQkO9MFZomrrDZ4sSJIZXzaEBWFvDrzQ1K-XkBmdMwBnd12QALfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/140029" target="_blank">📅 11:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
پرسپولیس برای خرید امتیاز و راه‌اندازی تیم «ب» با بعثت کرمانشاه و فرد البرز مذاکره کرده؛ قیمت پیشنهادی این دو تیم هم به‌ترتیب 120 و 125 میلیارد تومان اعلام شده. احتمالاً تا امروز یا فردا تکلیف نهایی خرید امتیاز مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140028" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140027">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140027" target="_blank">📅 09:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA9R6pQuipj87Aau46ydLX5xIuOvpLltcT4L3YEU9WdtKcZzmkUHtPB-db3vMbWmwbVgfvIXhQghtEpZl3RV-DUQEaJvtof6Mp1ZchsaGaX0rRDBX85X301e2ovUKBN5wwL97x5JYyOQ4n1hZqvkVq5hRiaX_7iMLuN1_hV5iq2Ibg5FcioMbaFMzwGduz9n3VwiYZGImqQRVfzeg7dHjXVHuwNcDmRVAgyu-uoi39Uql93nS9BHDOlMG_-soW0Kw-hcO4p2GqLWMhjYaGn1y-9BZA14vezowO7l0mLtvoUllF66tZzRKEvZFiCojStvESR9sa24vwvLf82bHkKgYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140026" target="_blank">📅 09:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6VsZJkD86xRVkq1BGbnEfpSeX-RjWCtWsKo4BXi8xVH6ZvZgAEa4Irf5bOY7oRchm95JVwj8qGGtA7DC2ieRV-XqKHngQLuJIE82qG_NmXstpS5T81d-Rn8bHVYPiNlULicUyFBQYyjdA3ggFDriA54Hi1av_3Wgk00PHi8VeSTuHjiFfm9uyZEdu9Wrz8KHFqFEJ3IMWs7Bwh2-cHDT3T_lwFOdNHXD6Pr3QNVDdOn-pfUnRFZ_2U20oel0IgaURN9xkYepa8IHN313Z-53RiYU6nPyFExgW4mOV3L0tlqpIyKwKsgVrOBOnf9eg7-5rC6lbNFIFREoj4HRaouig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140025" target="_blank">📅 01:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140024" target="_blank">📅 00:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
تیم دهوک عراق با مربیگری یحیی گل‌محمدی سرانجام بعد از ۵ هفته به اولین برد خودش دست یافت.
🇮🇶
در این مسابقه، دهوک که میزبان هم بود تا دقیقه ۷۳ یک بر صفر از نیرو هوایی عقب بود اما با دو گل ایگور برزیلی در دقیقه ۷۴ و ۹۰ به برتری جذابی رسید.
🇰🇬
دهوک با ۷…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140023" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🗞
علیرضا بیرانوند ۶ روز پیش دفترچه سربازی شو پست کرده.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140022" target="_blank">📅 00:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
فارس :
⚪️
اگه بیرانوند مهرماه دفترچه اعزام بگیره شاید بتونه با تمدید تو دو یا سه بازه تا نیم فصلو تراکتور بمونه
🗣
ولی اگه امکان تمدید تاریخ اعزام نباشه یا باید تا نیم فصل بدون تیم بمونه یا بره دسته یک و برای نیروی زمینی بازی کنه تا نقل و انتقالات زمستانی…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140021" target="_blank">📅 00:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140020">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140020" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=m56MK2KMKxWTYw5fAEyLnnqGdijxJ5DVusv5aYfy77Dn5iX6F_InbAyOe1OpOJbpBRCX6Ul6fHRS8kYVorh0D_X6eN5HihYOQZCVT8nXQJSo51YlCk96ClcHuFBaRYpbEywvRuVI24qajmPmvSoYE3rSBzhCyPYQyCxLBryzPvqVtWzglTjeVIjVSL4HWIU2bY1cGFaQ8_zeUgZE1AUWDnElWJV1Jm5CWPh3YpZcFLnb2wVWqBbfDOsWG9zAHbOecMtB6UXS689VITnsKt81YygS5n6js16c95c0-dx9jy9guRZnQ6u5DlTM36dcCl62aSovZfujBX8ftXs9XsXFjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30d045eab.mp4?token=m56MK2KMKxWTYw5fAEyLnnqGdijxJ5DVusv5aYfy77Dn5iX6F_InbAyOe1OpOJbpBRCX6Ul6fHRS8kYVorh0D_X6eN5HihYOQZCVT8nXQJSo51YlCk96ClcHuFBaRYpbEywvRuVI24qajmPmvSoYE3rSBzhCyPYQyCxLBryzPvqVtWzglTjeVIjVSL4HWIU2bY1cGFaQ8_zeUgZE1AUWDnElWJV1Jm5CWPh3YpZcFLnb2wVWqBbfDOsWG9zAHbOecMtB6UXS689VITnsKt81YygS5n6js16c95c0-dx9jy9guRZnQ6u5DlTM36dcCl62aSovZfujBX8ftXs9XsXFjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140019" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=icck3zceUeRc67rpZAhM7DX-jhYItvLpQMb2oT4nLulcJjtP3Pi7sMDTs8zN9h67UfuC1SO8cR2X3V9zHXSIfJ8P-ZYmqY4fC0yWSG2_UyDagBjua1txw9OG2zrydRsakHukLCo1ENQoMMFa5Li4Ig88B0TeevKbCsFbtyj5v6_d5W2wKL5u6Su3Mokl3M1kxJx2i0ikiRo8yg5vaHuuwIeTsICmjpOqiJYjwcGNUswXYJOL3F9vsLV8lqFni1B6NodrMYstVgYLGgDwSAo8UMLvTPc-WnXBT3XtPg4gj3KDXRsx8fpHTL91WxMZuYsUUXNDJV1uJsr1hhlCsAFF3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e82ae3f4.mp4?token=icck3zceUeRc67rpZAhM7DX-jhYItvLpQMb2oT4nLulcJjtP3Pi7sMDTs8zN9h67UfuC1SO8cR2X3V9zHXSIfJ8P-ZYmqY4fC0yWSG2_UyDagBjua1txw9OG2zrydRsakHukLCo1ENQoMMFa5Li4Ig88B0TeevKbCsFbtyj5v6_d5W2wKL5u6Su3Mokl3M1kxJx2i0ikiRo8yg5vaHuuwIeTsICmjpOqiJYjwcGNUswXYJOL3F9vsLV8lqFni1B6NodrMYstVgYLGgDwSAo8UMLvTPc-WnXBT3XtPg4gj3KDXRsx8fpHTL91WxMZuYsUUXNDJV1uJsr1hhlCsAFF3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خدابنده لو: ارونوف به من گفت در ایران فقط دوست دارم برای پرسپولیس بازی کنم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140018" target="_blank">📅 22:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=Oheu9DfftJU9li1O22uprKxCsuJJglsoQyV3L3EHqc7pzpwpIIUPkOSj4f2Sqcwqmj_y07mMttlM1X0sqNZxShldGOjNH6Mu1GGcrKe_PaeZsFK00s8HhecPvIDlYJEZEcV-sdle-nMbrP9DSdxe5_jeLDW4oIV8TlxPey9sepUDHvMKP_yfsaMZszx-vXvqmTH1gafeNFsCZbGUzfPCA1sjTw26TO6LqyEm8P8_DY59vzJQ01ZAYvN05j17DyfWRNY712w-8yB-uohJMLh-Nrn2nocWBLJf_WnIZqVNz0cq4Dlfmn4NnU8U8AWBlGs8A5y8fKquLcyirSgPBljJuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e23b00c48.mp4?token=Oheu9DfftJU9li1O22uprKxCsuJJglsoQyV3L3EHqc7pzpwpIIUPkOSj4f2Sqcwqmj_y07mMttlM1X0sqNZxShldGOjNH6Mu1GGcrKe_PaeZsFK00s8HhecPvIDlYJEZEcV-sdle-nMbrP9DSdxe5_jeLDW4oIV8TlxPey9sepUDHvMKP_yfsaMZszx-vXvqmTH1gafeNFsCZbGUzfPCA1sjTw26TO6LqyEm8P8_DY59vzJQ01ZAYvN05j17DyfWRNY712w-8yB-uohJMLh-Nrn2nocWBLJf_WnIZqVNz0cq4Dlfmn4NnU8U8AWBlGs8A5y8fKquLcyirSgPBljJuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
کنایه تیکدری هافبک پرسپولیس به شرایط ورزشگاه آزادی: قول داده اند آزادی را تا 10،15 سال بعد آماده کنند!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140017" target="_blank">📅 22:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f06355658.mp4?token=jFSUwH3Nk3J_3MuBLpu5oozriKteTmg-s5PyO8_03cn15UJi_hbQ8QY-bF3yFTeo2EGlkU4dky9zhe0zTxyo7FQV30x1PmzrOeEMzkbg-Xiw4mztlW9OVBcTz8sr3rUPgm81xDIIw26n41d1jum4kmon_BOCAM6qfR3DHx7b_0v77vhoK7WTpPFNxXsTsf43Lfl_aDy9-7mx4N1hNITLgxQduSyas89o1Yenos15eBdaMuArSjbdiT2V-rhBjdGy3EZAQwSvd9gg1YjXAu9M3ACVGfi4vPpk9s8fNS0EX65KZWHma63GIlmEQIb_1kQMIlrecXdpLUJXld61HaQ0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f06355658.mp4?token=jFSUwH3Nk3J_3MuBLpu5oozriKteTmg-s5PyO8_03cn15UJi_hbQ8QY-bF3yFTeo2EGlkU4dky9zhe0zTxyo7FQV30x1PmzrOeEMzkbg-Xiw4mztlW9OVBcTz8sr3rUPgm81xDIIw26n41d1jum4kmon_BOCAM6qfR3DHx7b_0v77vhoK7WTpPFNxXsTsf43Lfl_aDy9-7mx4N1hNITLgxQduSyas89o1Yenos15eBdaMuArSjbdiT2V-rhBjdGy3EZAQwSvd9gg1YjXAu9M3ACVGfi4vPpk9s8fNS0EX65KZWHma63GIlmEQIb_1kQMIlrecXdpLUJXld61HaQ0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
خدابنده لو هافبک پرسپولیس: امسال متحد شده ایم که هم در لیگ برتر و هم جام حذفی نتیجه بگیریم و هواداران را شاد کنیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140016" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140015">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ff628214.mp4?token=qEl9hVmRDZ-IEyRCX1fnMA5DnBJ-5ldrKNSi4XJHSq3iJ5NrV5Cm5HIjo58PO3fx6GhzoZeEr9G8G3GMeaJWXEpXf08uDKJJPEfyEFKQB6QLcw4stdJaqn5vvrqeBlJsSS-2RuCAHfibv7n4XgKAop_SY4-_5lKPrsUks41LCdNUq0c8K5iJiWtYklj7oV2P3c0Z4gFfA5KP4dCXcrEBlGyfYVC28RDTjhyZRnvB37Z5oj8175LngpTD3Gz7XZ2lItj36ub0LajwE1w5aDXxISxEN6X5h9Ji2L7fzXIlkkZCE5wl0zBY70bwTeC6dH4aYWEARknvyc19OTLvaZymVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ff628214.mp4?token=qEl9hVmRDZ-IEyRCX1fnMA5DnBJ-5ldrKNSi4XJHSq3iJ5NrV5Cm5HIjo58PO3fx6GhzoZeEr9G8G3GMeaJWXEpXf08uDKJJPEfyEFKQB6QLcw4stdJaqn5vvrqeBlJsSS-2RuCAHfibv7n4XgKAop_SY4-_5lKPrsUks41LCdNUq0c8K5iJiWtYklj7oV2P3c0Z4gFfA5KP4dCXcrEBlGyfYVC28RDTjhyZRnvB37Z5oj8175LngpTD3Gz7XZ2lItj36ub0LajwE1w5aDXxISxEN6X5h9Ji2L7fzXIlkkZCE5wl0zBY70bwTeC6dH4aYWEARknvyc19OTLvaZymVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس: از اردوی ترکیه به بعد ترجیح دادیم بیشتر کار کنیم و عملکردمان را نشان دهیم تا اینکه در فضای مجازی باشیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/140015" target="_blank">📅 22:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e456b94978.mp4?token=ZsxI2AL_2mcOFUgScBz0fhkHCP_fzOgmzgnVZH7SlAkijoNlHwS4DhGotrOID6U0ToodTLATJKugqbgraYXXqt0HblwbnEwcHpDgGFfNCTzkW9k7a0n0TPJbPan6QUBFYWrt5vQ5QaXUIrgmDKR2Ep6vrISxAjgjIpcJ614b5rDKcSWVIuKyKz7Qo_juZCx_v9YqKYTnxU9dyE4eXJ0R-tGYxr6ZtOFRilI-AhUTUeHbr-2YtW0eQ5QMICLAHaRnxxDqjCIhM3DX_2sVLe7XE8A4LM_gy8BcwDLoulyFaY4atYCzOe9GLuyqGp23v6dSRfIpeIC0tuHh-K9X795bmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e456b94978.mp4?token=ZsxI2AL_2mcOFUgScBz0fhkHCP_fzOgmzgnVZH7SlAkijoNlHwS4DhGotrOID6U0ToodTLATJKugqbgraYXXqt0HblwbnEwcHpDgGFfNCTzkW9k7a0n0TPJbPan6QUBFYWrt5vQ5QaXUIrgmDKR2Ep6vrISxAjgjIpcJ614b5rDKcSWVIuKyKz7Qo_juZCx_v9YqKYTnxU9dyE4eXJ0R-tGYxr6ZtOFRilI-AhUTUeHbr-2YtW0eQ5QMICLAHaRnxxDqjCIhM3DX_2sVLe7XE8A4LM_gy8BcwDLoulyFaY4atYCzOe9GLuyqGp23v6dSRfIpeIC0tuHh-K9X795bmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
خدابنده لو هافبک پرسپولیس:
🔄
🔄
تا روزی که هواداران و باشگاه مرا بخواهد در پرسپولیس می مانم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140014" target="_blank">📅 22:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=TyiIhMW1liFRVp2UfGz-Samo8lYckXU53E8g1u0f-iYegHUT1P9bIjwApBphQdE1HtjTji4QNQ2JNyUs_gk-FiEm9K-AfSOUnmMjXfEGupoeEPLFbEnxtFASQh2MpuWp1EXeySKH1f60G25--TW__r9cj29uJ8yeN0S-XuZFq3IYIpMiE14JBuEOYt2aTLMu6qKarnPxJedSSVkKLAuKvF0pC1YyQnRua4C5Rqsqs9Pp2Nm2BgeN3tehU2Gg92eufU-GHFCvgCsSae7TsqQn0UOHDTrlTW5MjO2uOjWuW5kj2UChRqp6riIU6z33XFg6sWCVAkM9EviAAALLNixFEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98087f79b6.mp4?token=TyiIhMW1liFRVp2UfGz-Samo8lYckXU53E8g1u0f-iYegHUT1P9bIjwApBphQdE1HtjTji4QNQ2JNyUs_gk-FiEm9K-AfSOUnmMjXfEGupoeEPLFbEnxtFASQh2MpuWp1EXeySKH1f60G25--TW__r9cj29uJ8yeN0S-XuZFq3IYIpMiE14JBuEOYt2aTLMu6qKarnPxJedSSVkKLAuKvF0pC1YyQnRua4C5Rqsqs9Pp2Nm2BgeN3tehU2Gg92eufU-GHFCvgCsSae7TsqQn0UOHDTrlTW5MjO2uOjWuW5kj2UChRqp6riIU6z33XFg6sWCVAkM9EviAAALLNixFEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مهدی تیکدری بازیکن پرسپولیس:
✔️
امسال یک تیم گردن کلفت داریم و نظر همه  هم همین است که امسال حقمان قهرمانی در لیگ است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140013" target="_blank">📅 22:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=kUx4bSjV9WYeP7PS5QIbCxeGpponJ6lBuwIn4JWqRjAAIKI9RdjHp4RwOkRhYsL06Lra5syHUo-ZVCm-GSJtbTCS7xGmEeUVyZ5eQ_LKiS97Wm6g1VWLhXNZiFtv9PLejgWHlU189vcsROOZwhTvDITDCMWkmmJX95gtuqzx3x9x773uSxZOjcN0Q8u_6XVHAJnb74vscm_xS32Tslm7HoijC3U29jjz-4bDtgWd-CyUBzKBSkWkzn1NgJghrd7fnJd6VfSrTXHjEF9J2SeQDx4lLYQHilIFnlTvKWcWnd4nCDH8V2K7T4mSJ0N-A6_4sIiMOtRNmZHdIpxiYGIC8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9eb4ad0d3.mp4?token=kUx4bSjV9WYeP7PS5QIbCxeGpponJ6lBuwIn4JWqRjAAIKI9RdjHp4RwOkRhYsL06Lra5syHUo-ZVCm-GSJtbTCS7xGmEeUVyZ5eQ_LKiS97Wm6g1VWLhXNZiFtv9PLejgWHlU189vcsROOZwhTvDITDCMWkmmJX95gtuqzx3x9x773uSxZOjcN0Q8u_6XVHAJnb74vscm_xS32Tslm7HoijC3U29jjz-4bDtgWd-CyUBzKBSkWkzn1NgJghrd7fnJd6VfSrTXHjEF9J2SeQDx4lLYQHilIFnlTvKWcWnd4nCDH8V2K7T4mSJ0N-A6_4sIiMOtRNmZHdIpxiYGIC8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بازگشا سخنگوی پرسپولیس: دنیل گرا در هر تیمی که قبل از آمدن به پرسپولیس بوده است کاپیتان آن تیم بوده و بازیکن بسیار پخته و باشخصیتی است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140012" target="_blank">📅 22:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5221c79f.mp4?token=Qcp87m4LOAwbXwQFSPO1JsHIvQrMxYAVyrF_RotvRagyN9ux5XVbtt-mKrcB_0dGMqNPdgdOTFq0Md70zpLJB3N3OlTH8t2JWgsFFfdZuh6jqvrt1wORGzAQdIb4HKD0ad8Ff4vsAp26U9npyfNw9iob3CvZGPTn844GwR682krYLdOY8WrExhRL2ES2kzQOQy524yHWvONy99bK2D3Z6oBIlxK2-UIAxY6jk9rR09DhdTOVdOsMJALJD4Hj55NkGLuVj0GtVzFmG6RnC2Ndpn-_NsrEYbp2Bs00u87kVwGjYmzhyuig3rKHPz4nepIIIE8tvu_HBtyOft35xczLWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5221c79f.mp4?token=Qcp87m4LOAwbXwQFSPO1JsHIvQrMxYAVyrF_RotvRagyN9ux5XVbtt-mKrcB_0dGMqNPdgdOTFq0Md70zpLJB3N3OlTH8t2JWgsFFfdZuh6jqvrt1wORGzAQdIb4HKD0ad8Ff4vsAp26U9npyfNw9iob3CvZGPTn844GwR682krYLdOY8WrExhRL2ES2kzQOQy524yHWvONy99bK2D3Z6oBIlxK2-UIAxY6jk9rR09DhdTOVdOsMJALJD4Hj55NkGLuVj0GtVzFmG6RnC2Ndpn-_NsrEYbp2Bs00u87kVwGjYmzhyuig3rKHPz4nepIIIE8tvu_HBtyOft35xczLWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
بازگشا سخنگوی پرسپولیس: ما باید تعطیلات فیفادی را با صدرنشینی لیگ شروع می کردیم اما نخواستند که به این شکل شود
💢
پاسخ سازمان لیگ را ندادیم و به جای آن رفتیم به فکر آماده سازی تیم خودمان شدیم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140011" target="_blank">📅 22:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140010">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=oxCq217afq9mtH9g1oUBs7ezaRN-6QyqdVifl8UUovmuwqvMFRzPtadsX-TBZ7lGx7pq6B-HQmZacb0coE-rMfC0BQLTP6Vb-hpe3tnNYWLykvK6pxlH8I_1_eBzfeeCmXSOThhjKgpa84At5YL2vpmp2ABS0n4re-DYRmQ3C83G2X9iC8ZmHvrTZP2uFSEuil0cBjroY9oW-d47riajF2UP5AbCi4tHmT-PQF5emdJHRJxTLK-DJctwosNZdw7AzOc0azQUhjAxPBSBd4RbrNzUyjOlOk5ccr226fZuSEem_eLMP91z6zaQ5787g2KVWNJ0d2wz2WH_9y5Q4tru5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=oxCq217afq9mtH9g1oUBs7ezaRN-6QyqdVifl8UUovmuwqvMFRzPtadsX-TBZ7lGx7pq6B-HQmZacb0coE-rMfC0BQLTP6Vb-hpe3tnNYWLykvK6pxlH8I_1_eBzfeeCmXSOThhjKgpa84At5YL2vpmp2ABS0n4re-DYRmQ3C83G2X9iC8ZmHvrTZP2uFSEuil0cBjroY9oW-d47riajF2UP5AbCi4tHmT-PQF5emdJHRJxTLK-DJctwosNZdw7AzOc0azQUhjAxPBSBd4RbrNzUyjOlOk5ccr226fZuSEem_eLMP91z6zaQ5787g2KVWNJ0d2wz2WH_9y5Q4tru5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
بازگشا سخنگوی پرسپولیس: با احترام به وحید هاشمیان، تعداد مصاحبه های او از تعداد دفعاتی که روی نیمکت پرسپولیس نشسته است بیشتر شده است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140010" target="_blank">📅 22:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✔️
✔️
نماینده محمد عمری ستاره 25 ساله‌تیم‌پرسپولیس این بازیکن رو الشارجه امارات و لخ‌پوزنان پیشنهاد داده تا درصورت موافقت کادرفنی هرکدوم‌ از این دو تیم با عمری قرارداد امضا کنند. عمری علاقمند به لژیونرشدن در نیم‌فصله.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140009" target="_blank">📅 21:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🔴
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140008" target="_blank">📅 21:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
اورونوف در دیدار امروز نمایش قابل قبولی داشت، در این بازی یک پاس گل ارسال کرد و یک بار نیز تیرک دروازه حریف را به لرزه درآورد.
✔️
✔️
این بازیکن در طول دقایق حضور در میدان چند بار با حرکات تکنیکی و نفوذ از جناحین برای پرسپولیس موقعیت خلق کرد و از استاندارد…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140007" target="_blank">📅 21:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tqkf61EgNo4nx3iYlK9TB6ilCsoUgCTifP3aY2TxwnTPcpPmgJMn-WEaokd-QbYxuLlIaXRqFR34CZzsedRc7TYHA5O8_uuKShkb9Ek-H1R5ybPklt1fe0fW5_vrTHwTyqeNf8JntJTwaUhWGHO_RSzitoOKm2k8X_8d2A1qdKD3v2LooTdy6ErLkNsGgYYbtseFEbhvQP3c5od_DZ8t2HeFdD8BXLPpWDHWTMJDmJnBuaafluJRWZ4RnbTADRDjUT-tTUt5-6TXXxJysLmpvFi93SmB0dwK5hJXRlDQzsFJephLB5E1jpUcvxrzeCpyekoNW31_T1OIGfjXE4ghHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
برانکو ایوانکوویچ، مربی کروات که اکنون به عنوان مدیر فنی تیم ملی امارات فعالیت می‌کند، با حضور در اردوی تراکتور در دبی، با سید حجت کریمی، مدیرعامل باشگاه، جواد نکونام، سرمربی تیم، و جمعی از بازیکنان دیدار و گفت‌وگو کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140006" target="_blank">📅 20:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140005" target="_blank">📅 20:56 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140004" target="_blank">📅 20:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🏅
❤️
فووری از رسانه داریو ازبکستان: باشگاه تراکتور به دنبال جذب اوستون ارونوف وینگر ازبک تیم پرسپولیس در نقل انتقالات نیم فصل است
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140003" target="_blank">📅 20:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140002">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7y91wHGWL1EK6fclFeBnlzcRmBi8VzawIRbcbhkOEqJcB3ha6QaFbC56cePbar82F4VDULzonTPvpOjxOimvWtwhmaihCJlS5L4YYMyT4mXCgHvj2vZhNbrYpVVrT39-rtQc_Jo8MelQ46law3Kz69Q-cdICJ6mFEl9uQZmACdZrZHR6dImMGgb-XuHHB-lV6qM39zoO-3gizDjcdfLe6rq07QMAJa2dp_si0NO7RxZUbzArCpB9-X1ClcId0Ap3EQrG94ax_PJsIOwb0tZJqN4vU6q94FTFtGI7beO_pwj5LkZspqToDSRFfImgyjbiIcj55FFCw_UpA8AgaEGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جدال نزدیک و نفس‌گیر؛ برست و پاریس برای یک برد ارزشمند امشب به میدان می‌روند!
[
برست
🔴
🆚
🔵
پاری‌سن‌ژرمن
]
⚽️
بازی برای هر دو تیم از نظر امتیازی مهم است و انتظار می‌رود محتاطانه شروع شود. پاریس روی مالکیت و کیفیت هجومی حساب می‌کند، اما برست در انتقال‌ها می‌تواند خطرناک باشد. با توجه به سبک دو تیم، تقابل نزدیک و کم‌فاصله‌ای می‌تواند شکل بگیرد.
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
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140002" target="_blank">📅 19:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140001">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140001" target="_blank">📅 19:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140000">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN1FDTTDtDJ8_INT-wF2nl0k6RhvceBnlo1osxKha1g6OSuhCdmfv_NAPxucGqUKVjc6dGeOUh3m8HaXdoZ14fZc36j3McyJeCZYQ1bthU_qQ-Z8_X7I0P7Kb80MGHwKLB6RzSTwW5UfB6dkLO6T_pH6ZkiGKAy_vNsUAtUW1pcLDldXmoT-yNHDXgERS86MoOEHg_oGrmZruvjH4aye1L3H6inDgGlHpSFiYy28tKEEki-Fg-TDB8bnNUa9OuFCYWjcTmvb7aU5QnFA8Gh6ITTbEVFJQp6HqvmQwqhVb6IDvnvaKz_TdI5Sx--TPyswl-I4uCuW0dtwadEvD7zBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
بیرانوند سرباز شد
😂
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140000" target="_blank">📅 18:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139999">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139999" target="_blank">📅 18:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139998">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=dUUCodRfplb2_G1L3NvCzlREOqTXa4R_a9tIXGuQ1DFLCTwxmW7s-uVt4RkE4JLi4G71VQah7PrWQDMJiVq4GlrMjzi_73UXF5-xWFuYhRgoPFjYuC-zKfsdcTFQgsiWEsUrXi1KN9T5bzQnpaZaf-ga_7zODzCFxm8vjQaChIc1wJH25IclcOSu-VX65QOjFk_gMTDu5l11hudCSa52l0eeeX_RDPu-pMt-kO0Q5DMLAAEncNncKL7Inozk0bpAqex4_2wv__4vwocvfNTo9GtFDnt8brY0kNARX_v8kUkZygBba_XuT3CbS0YpeDiAnfRk27QeRE0Atx87PDIbjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af9bbd8729.mp4?token=dUUCodRfplb2_G1L3NvCzlREOqTXa4R_a9tIXGuQ1DFLCTwxmW7s-uVt4RkE4JLi4G71VQah7PrWQDMJiVq4GlrMjzi_73UXF5-xWFuYhRgoPFjYuC-zKfsdcTFQgsiWEsUrXi1KN9T5bzQnpaZaf-ga_7zODzCFxm8vjQaChIc1wJH25IclcOSu-VX65QOjFk_gMTDu5l11hudCSa52l0eeeX_RDPu-pMt-kO0Q5DMLAAEncNncKL7Inozk0bpAqex4_2wv__4vwocvfNTo9GtFDnt8brY0kNARX_v8kUkZygBba_XuT3CbS0YpeDiAnfRk27QeRE0Atx87PDIbjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمیشود و از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139998" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139997">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139997" target="_blank">📅 18:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139996">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139996" target="_blank">📅 18:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139995">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
تو 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/139995" target="_blank">📅 18:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139994">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ynEBSn_On1-FFwTEuNJ7lXZOHoOBzp6536KPuEjAr2Z2Ehf2kieBEWGz6lC0fCqIhoTfdJLC_sv2HpvMBZYP4NHW8Q4IFXr7wjSNxL-ELzWpgF6PwkTz2aT5u4RLnzSJesr2OctJOh5VWl-DOQJv5CryGgjmXPX2ghPwQnutsdKWXKJtj7oiYsfeO0ASpGhBB1K-biURAs3LrNRy_janR4YJDCrEXh9Otiaf6GcnzfUyUx1UkncoHyfZz7K-AmE8ryiOdwZKNmGUPA6ibi1XR_p1891o0y2wD0Sw4gm09D3A9noMHSCSde6hz1H-l-GtrLcUnInTRu7HfuVDLCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
باشگاه پرسپولیس در دیداری دوستانه با نتیجه 4-0 تیم شهید قندی یزد رو شکست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139994" target="_blank">📅 18:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139993">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🗣
#یادآوری
✔️
✔️
هتریک بیفوما مقابل بارسا‌، گل‌هاش یکی‌از یکی قشنگ‌تره و خلاقیتش رو به‌رخ میکشه
✔️
✔️
وقتی تو سن ٣۴ سالگی جلو ملوان استارت شصت‌متری میزنه یا اون پاس‌گل جلو اس‌خوزستان میده از سر فوتبال‌ بلدیشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139993" target="_blank">📅 16:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139992">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
حضور هانی نوروزی پسر زنده یاد هادی نوروزی، کاپیتان فقید پرسپولیس در تمرین تیم دهه شصت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139992" target="_blank">📅 16:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139991">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
فارس: محسن نامجو با هماهنگی به ایران برگشت، احتمالا شادمهر عقیلی هم به کشور برمیگرده و حتی کنسرت هم میذاره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139991" target="_blank">📅 16:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139990">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139990" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139989">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
دو ست و فعلا باختیم و واقعا زورمون به ژاپن نمی‌رسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139989" target="_blank">📅 15:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139988">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
میثاقی:
✔️
مهرداد محمدی یه چیزی گفت شش ماه محروم شد اما خداداد چهار ماه؛ ساکت الهامی هم شش ماه محروم شد!
✔️
یکی از دوستان حقوقی گفت شکایت قضایی این موضوع چهار ماه زندان دارد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139988" target="_blank">📅 15:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139987">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRpa6ODlz5aIL3l69Zg5Ov-CFWXv6kDHbrEPyo1jMsy27WMehER7LW288Vg75TaxEgWxijxu8CWC8yJze0_emOVB13t2IX2PAyNyuROGCEBRZzqAi4_D8ZqnQga6o_YRtdNooAd1bEN6ogqdNbtitZiVCYj7nDFW90QwDP_TcGXfBniiX4i1UzPKNZNM1-W3XV9dOPeT5-pXeFcyrLcVZG-wam-u1a6vksYNwhkftBXb8Uzd5qx-uzjKmD8ZGGFXAfQ51pQP-SWZld-09VNWbbMlA47o2k9V2CiSnoRiv7ieDfuy3pITm91ZmkQ2O2H9WQ6jBGlQkKj7ThLyC5SdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
پس از آنکه محسن خلیلی در ابتدا اعلام کرد: «جام حذفی برگزار نشود بهتر است»، حالا پیمان حدادی برای چندمین بار خواهان برگزاری این مسابقات شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139987" target="_blank">📅 15:20 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
