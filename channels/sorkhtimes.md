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
<img src="https://cdn4.telesco.pe/file/NWuI8alquG1GlEggxE9JtVJiaqHI2Um2NxcJB__MF-1hqTeUBGu6ZC7BhXbRrgQ62wu0TtmtlcfGhjIQ8eKDFSGblccPbD5wopsCdAhPUgyeDFvyNdVtHn2xrHml9so6kaVDYRkz7aq97K6rB9s3juE9iZJAeiUyo8fM4hjquJt_WIq3ZXqDjoC0pPkpkRe9PyBaQtnj9uS9BgpWpUZC0kZYsSHEmfvsSkBtTfN1RA6d5mk_OYQext-hRiJnGjcAmy4x2JZM2g_0E9z9TO2FlKbQQ52xVIr0ebBDvLe0X-Wc2w3Vdluxv6N3HAFWDdhS7vR3F7I3QhzG3NoV7SASuA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 12:49:04</div>
<hr>

<div class="tg-post" id="msg-140869">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scFce4oAiFMtZ9xHaoWSA1BUF_OuQv63A2FaqROBVWadhohw3WtVJ12jr3nLvkte0kZVnqtQ6hjNDqXd6zMq-OOYLRKWsrjHOXrQB93aBRSP9dxEK8nGF-gYRlUJM632B_BAYSx2SCSW2vhKmceORZu05rA_FrXxoOECSYrXvtV6nRTNtc-CVFPq_Oxstgb3lJxUL8UfUJ6-ekOTEfZOybjTTbTHAX-eorzW80Ql-57hPPfDNbR2jRchkh4obyiTorpdXlHJq50C9IduQTAV8kpXXlnJh37Ukd77qo4QwdrALS4zt-_GkG4EoVLEUFCdESJgxqtHNcMubWOF910tZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
زمان بازگشت قلی‌زاده به میادین
◽️
بر اساس پیش‌بینی کادر پزشکی باشگاه لخ پوزنان، قلی‌زاده می‌تواند پیش از پایان سال ۲۰۲۶ و در اواسط آذرماه دوباره به میادین برگردد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/140869" target="_blank">📅 11:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140868">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKCE4RNYe81PTmC_7PxDUDwx2q4QgSxw5RrYX8d1W9_i-1SriXnXgU2LXykOaee5ARybu_9c3ENVkoIw3-aKvDpomFbaK6FvpIHxfy6_mkrThM5lSFpPc5YZiWD9qMt3JkDPZE3ICgGqofpYijq9M2Fxpgc9hz91jnvbmQcTg2Xck4ZpJz2wmEyPF1AGBnuSpx3VxG-U_S5rn1MFss5XQW_WMHbxbtkN0syuiYZh0_4nfMdSzNX7Dt4OP-QbrCEhbaY1VTYW0nECc8sOXMuJCGw_NSi8yUdGADrjdC__c34kls8LHMmFmmZLqzMgomm7pdhTX6hpgz8K3y6mC_vIBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از ورزش سه
🚨
زوج خط حمله پرسپولیس مقابل صنعت نفت آبادان رو ایگور سرگیف و پوریا شهر آبادی تشکیل خواهند داد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
﻿</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/SorkhTimes/140868" target="_blank">📅 11:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140867">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚪️
⚪️
محمدحسین صادقی امروز علاوه بر گلی که زد، عملکرد درخشانی در ترکیب پرسپولیس داشت و ممکن است در بازی‌های بعدی لیگ به او بازی بیشتری برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/140867" target="_blank">📅 09:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140866">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/140866" target="_blank">📅 09:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140865">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
✅
✅
گرا: از پرسپولیس نمی‌روم؛ از زندگی در تهران راضی‌ام
‼️
✅
✅
گرا در در گفت‌وگو با «Nemzeti Sport» درباره مصدومیتش گفت پس از مشکل کف پا و انجام MRI و تصویربرداری، شرایطش بهتر شده است. او درباره شایعه جدایی از پرسپولیس هم تأکید کرد یک سال دیگر قرارداد دارد و…</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/SorkhTimes/140865" target="_blank">📅 09:03 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140864">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-KliyALPnMNcmoOZZ7iECwhnpAtEmAtlspXRWvY-5plyQnZZbCIrSl3TjgGTn6kwkwAhhasQmBuK7AeOMrqAP8gMpntIUBtb4d4HSff_7vaCPwlQ7HtTC1t6rfIt6PCRpcejbxa2ysP74nqolvRaCO3XmfFuoLrhJwVwx0i76_IA_zyhRejDylIkQxUrE8tYhOO5y10G2NbrUvaR98cVDqf08qudHZ_EHjt2RBNe3qeZO7m7J0n4YKw1L4FfSUKf1VhsQu3IHcMjyx1C9Z23ODl3Axsfxk5BAWHE3XhRX8GY7cvuzscgH-mpqhX92LPMWQQZcC_xh3-P4QAMx8J8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/140864" target="_blank">📅 09:01 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPXs8ZY6DYVEcaBN3p3oFaY9g3hI2rW8OU7Sy4I60Vo_MwlDE1swDAn_zOfo4LVz1SiDBXq1PwwLFy65GZ3MujnsEVlwAojYTh-9A_7Rh5mF33dS5PoqMuHIoaT_zhXjy1HXxRCpn5hur26PCKYfmyoffA4ORM45ut4iNxU1W7MATFmcbUU6fUTx5Jw_tXLL8PGkz9921g7dw5pofBu5zPk5Q8CAg4ywsXtfaffhptCrFQ0m3A5amGBcbmxG7-sFrqmnvQ7abRTnc3xm9ius0uCSbUzvck1bJe5LO2m-bclebMKbhiMAYa7scA9L4RgA_ZsdG71vWhqpRNH44JtnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
CROATIA -
❤️
ENGLAND
⏰
Saturday 19:30
🏟
Stadion HNK Rijeka
🇪🇺
کرواسی برای کنترل بازی روی مالکیت و گردش توپ در میانه زمین حساب می‌کند، اما انگلیس با سرعت بالای انتقال و کیفیت نفرات هجومی می‌تواند در ضدحملات خطرناک باشد. تجربه و کنترل کرواسی در کنار قدرت هجومی انگلیس، این مسابقه را به یک نبرد نزدیک تبدیل می‌کند؛ احتمال موقعیت‌سازی برای هر دو تیم بالاست و گلزنی دو طرف سناریوی جذابی به نظر می‌رسد.
🟢
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
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
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/140863" target="_blank">📅 01:14 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
مجتبی فخریان بصورت قرضی راهی گلگهر شد تا پوریا پورعلی بصورت رایگان به پرسپولیس بپیوندد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/140862" target="_blank">📅 01:02 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140861">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
غندی پور، مهاجم ایرانی شباب الاهلی امارات، به دلیل مخالفت باشگاهش نتوانست به اردوی تیم فوتبال امید در ژاپن ملحق شود. طبق قانون با آغاز پنجره فیفادی از ۳۱ شهریور باشگاه‌ها موظف هستند بازیکنان خود را در اختیار تیم‌های ملی قرار دهند
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/140861" target="_blank">📅 00:47 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140860">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
پیشنهاد پاختاکور به مهاجم پرسپولیس؛ سرخ‌پوشان اجازه جدایی ندادند
✖️
✖️
بر اساس گزارش چمپیونات ازبکستان، باشگاه پاختاکور در نقل‌وانتقالات تابستانی مذاکراتی را برای جذب دوباره سرگیف انجام داده بود اما باشگاه پرسپولیس با جدایی این مهاجم مخالفت کرده است. …</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/140860" target="_blank">📅 00:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140859">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✔️
✔️
در نیمه نخست و در دقیقه ۳۹، شوت زمینی محکم محمد عمری را دروازه‌بان حریف دفع کرد که توپ برگشتی را محمدمهدی محبی به گل تبدیل کرد.
🔴
در نیمه دوم و در دقیقه ۶۶، حمله ترکیبی سرخپوشان با پاس شهرآبادی به محمدحسین صادقی رسید که او بعد از جا گذاشتن یک مدافع با…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/140859" target="_blank">📅 00:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140858">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✖️
✖️
بی اعتنایی عالیشاه به تارتار و حدادی
🔴
بر خلاف سیامک نعمتی که قبل بازی تدارکاتی امروز پرسپولیس و گل گهر، به سمت مدیریت و کادر فنی پرسپولیس رفت، امید عالیشاه ترجیح داد، برای احوال پرسی جلو نرود.
🔴
از اینکه باشگاه او را در لیست خروج قرار داد همچنان ناراحت…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/140858" target="_blank">📅 00:28 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140857">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
✅
ورزش سه: امید عالیشاه به باشگاه اجازه نداد امروز مراسم بدرقه و تجلیل ازش برگزار کنن و تندیس باشگاه رو هم قبول نکرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/140857" target="_blank">📅 00:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140856">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/140856" target="_blank">📅 23:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140855">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140855" target="_blank">📅 23:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140854">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/140854" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✖️
✖️
شماره ۷ رونالدو واگذار شد
🔹
پرتغالی ها خیلی زود جایگزین کریستیانو رونالدو را انتخاب کردند و رافائل لیائو شماره ۷ را برتن خواهد کرد.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140853" target="_blank">📅 23:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
بغض محمد عمری درباره شروع دوران فوتبالش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/140852" target="_blank">📅 23:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
✅
✅
🚨
فوووووووووووری
✔️
مهدی تارتار قصد داره جلو نفت با سیستم جدید‌ به میدون بره
🔴
باکیچ فیکس
🔴
محمد عمری فیکس
🔴
ابرقویی کنار زارع فیکس
🔴
شهرآبادی کنار علیپور فیکس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/140851" target="_blank">📅 23:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
پایان بازی / 3 برد از 3 بازی بدون گل خورده
❌
پرسپولیس 1 _ 0 وارش نوشهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/140850" target="_blank">📅 22:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
✔️
خبرگزاری فارس:
🗣
شادمهر عقیلی مهر میاد ایران کنسرت میزاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140849" target="_blank">📅 21:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140848" target="_blank">📅 21:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=Gia4HDZNeH0O4ALVCthDssAH0quJ34CLluH0yHyjqSix73MTFO4t54CP_JwQ8jJhFNw3GLZseYogQZaszfNHiTpfoPOU3YUgCfaWGlCVcJPnpgBrx3kSztDZWs-9CCCB7Zc66JEtNTtEo97H4BnJleV_dlfpP_cXyIV7LTNTJKixemHcCfekJTbxhgqi5F2tamVlefveEP9dLAiLKB_v0mon1j_1lV-U7Nc0fQA6woqEvhTxgebd3J5L9-uM5Hg3jfx3ebM_YQDosmPektcMGcMi5H2RRg8S5f0_MwvLU8LkUZyymdxKstnNsl209GpYfbXZpH5GbXbUFHUbrCjNmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50746a4a4d.mp4?token=Gia4HDZNeH0O4ALVCthDssAH0quJ34CLluH0yHyjqSix73MTFO4t54CP_JwQ8jJhFNw3GLZseYogQZaszfNHiTpfoPOU3YUgCfaWGlCVcJPnpgBrx3kSztDZWs-9CCCB7Zc66JEtNTtEo97H4BnJleV_dlfpP_cXyIV7LTNTJKixemHcCfekJTbxhgqi5F2tamVlefveEP9dLAiLKB_v0mon1j_1lV-U7Nc0fQA6woqEvhTxgebd3J5L9-uM5Hg3jfx3ebM_YQDosmPektcMGcMi5H2RRg8S5f0_MwvLU8LkUZyymdxKstnNsl209GpYfbXZpH5GbXbUFHUbrCjNmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووووووووووری
🏆
با اعلام علوی، سخنگوی فدراسیون فوتبال  جام حذفی این فصل برگزار نمی‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140847" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✅
✅
حاج صفی: بهانه نمی آورم اما چمن بازی با ازبکستان و روسیه خیلی بد بود. از مردم بابت پاس اشتباهی که مقابل ازبکستان دادم عذرخواهی می‌کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140846" target="_blank">📅 21:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140845" target="_blank">📅 21:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/140844" target="_blank">📅 21:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9nKLj6OsPyZ8HZKZ4svXWiw_EN7cYKYTfWnGEhSM5puMbdGA2unB0L9IfC25Ua9NH4xejGL4nfhoEHefFCwRKQYfwB-moVXpSqnG68NC21F4oJcYHwfbxFSAi8Gm_CDJIvg59dySOwpSkUM6eA08kKTy_8VP88TCH_sZiFstNhouQ821r0SCy0ffca9BG52hdWl4OvzoQXX9t7thqc1VlaPUTpKrf_nRuWLh3rYc0ylIQAHdC6oyPOvvkZNJGpX6Osq6yPlEXfeI1HpSP7najtsQqF4VzEm6F3GOb5fdtQlSOJE7FEBvbCY3Tk-s8WDON0NIBmH8erHhPMgMwvXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
FRANCE -
❤️
ITALY
⏰
Tonight 22:15
🏟
Stade de France
🇪🇺
فرانسه با دو برد ۱-۰ مقابل ترکیه و بلژیک، از نظر ساختار دفاعی و کنترل بازی شروع خوبی داشته؛ ایتالیا هم بعد از شکست برابر بلژیک با برد ۴-۱ مقابل ترکیه واکنش نشان داده است. غیبت امباپه از قدرت هجومی فرانسه کم می‌کند، اما حضور دمبله، دوئه و اولیسه همچنان تنوع زیادی در حمله ایجاد می‌کند.
با توجه به فرم اخیر دو تیم و میزبانی فرانسه، احتمال برد خروس‌ها با اختلاف نزدیک و گل پایین خیلی محتمل هست.
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
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140843" target="_blank">📅 20:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0YGGe5y03sz8tgpHoLV_-7RNWx9N09Gv_VmnpfokOgv9Vae_6JtpyzJndcmnHFW2wM8Uj-MCJF9EBhBjFVUuSSQUVUhnLcAHxeHx0BpBavCJ12o5OUq3qdHlIv0TTOLRmjpcsvLwrwBMEZdaW6ouAHAsem5Xkvv94jf2a1Z-WHf3lrB0PIrFUab2N95hjSdLxYFf9f09Mvq6Ta-0JuUnZt6u9rSFyNirbUyBLqKi10kWztf-TZtZQEjHbsMyONbxgpawGkGsdyyOmEIYbTOQ7kFhcpMUAx412jDlnmrEKP49BuRwaGEv4vdrw8rDoNr-yp8XOV9SyYnKSCuvnX-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
موبایل قاپ‌ها به حدادی هم رحم نکردند
💢
مدیرعامل پرسپولیس بعد خروج از ورزشگاه شهید کاظمی و دیدن بازی تیم بانوان در خودروی خود مشغول مکالمه بود، که یک سارق با موتور نزدیک شد و با قاپیدن گوشی همراه حدادی متواری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/140842" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIxySuNAg4blF-SbpiThqTAnG3lbLPabJUVtHW97Z2wjzAmUupzeF9E67rfGMOAvvdZpGF-0ocbN6ZANREwKzXgJDwVjvja0cd63wRryyq4Sv1sAWpi8DFzgW1IaXIaFVN4O0MAmw6NGNBIi092fzLY0im5Ex2SJT7n-Tu7RLMXRbr3OWntaDi1pSXZhYyTPUaketv3EL11IWpG0nR5uZ-hfXFeVx1LmRNafZc80B5p0PVI2sjbC85uMJwhbcYTb1zrekPCgcAae6FPIDUlqdCbkctIOQDwbz74KJFYQg3AA7NUZiPHhAJ9UIGYGUi3g3fdlW-_q7Ivb-nVN6Yx3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
کاپیتان پرسپولیس در دیدار دوستانه امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140841" target="_blank">📅 20:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول  پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140840" target="_blank">📅 18:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140839" target="_blank">📅 18:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.  #دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140838" target="_blank">📅 18:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrgtdrr9YnsVwo7Fhocj1exP7va3NN65jXJeiBbZ8vHwQCbqYVjS7jgZLNVTjgxQn3q8A5Jjs0trgV88HT5n1wDMIxFXsvOZhAoHkTYI1Kd49AKddapT-4BhL1AwbIqpEU6l9-bEXO1ebpekYGgS09QplgNcnMfZqKB6RDmDihIT9w4lJeCFdbYQ06FwNSCxqxrGgL616t-jgrbRuuEn45qB5gIroOfeEXLCXYciMfM1NzcT2iVQO1mkAgBWanGbKlvUbhvSecXdJ0Pv-zn_x1SbFQEA5BMFTumDKZfctXLPy27ZVTeYidjyjUPHjajyIJye3yIcRxdbfb5o2iv7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بُرد پرسپولیس در دیدار تدارکاتی
⚽️
⚽️
دیدار تدارکاتی پرسپولیس و گل‌گهر با برتری دو بر صفر شاگردان تارتار به پایان رسید.
⚽️
گل‌های این دیدار را محمد مهدی محبی و محمدحسین صادقی به ثمر رساندند.
#دیدار_دوستانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140837" target="_blank">📅 18:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3zHAMxSwVrlql21mHhNOKogpWC8IHUmhjrBW7CBmf9lLzhgjJci79NWlFl7oIelng3v7nNG_rr5SD3S6fxvpconMc1olmisaFsX-jochgsNxFnM7XknFnZLnY5AuMYP1D3tlv0RDzvNywVBtq7k63pOhYS2NFALv4dTKvRo3h3SK5JoUy9xehOKmOrV7M4QZAIfqB35lUQcxKfpFKKvMqbXav6_KvbTzFLNgKXwoXGQX9kS_GtEUCDTM5WSAks-qW-2T69l627-yL-f2Cy4D_2R_Nx8lsB7Wqsh7wlaBxQLZafqJY8x3yDgMEWcCNZvsRMkZChXYHWsmZ6VQmnqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😀
سخنگوی فدراسیون: قلعه‌نویی از باختن بدش میاد به خاطر همین بعد باخت جلو ازبکستان اعتصاب غذایی کرد و چیزی نخورد
🗿
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/140836" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f945d97990.mp4?token=YqiuaXNDymh-M5NABvtZ3Htnkppgrb4J5i4I0tsfiPcqUgF5J7I-HTfOdSa8gHw3i-CIQsJSof8uHg6TqmoZ7iOAsPdM0_woJQYEiYNhYSjk0e_8yNjMegdd4-X9OOgCvtiH4juWwMkd4YCT_v7v4kwfT3xWMoahpZswh8RcvCb8T9t1F_VfdmvV0BGlMLvTVprZGbrRVs-NKLAdLtzgIdokiK2Iapi0kAzZxHpTv65IMWkiciJScyu3Jx-PgbV3t59sUfX2Pb1drF9eFa0nIHHQ0JohAL8p3je6kzooO2s6L-V1sSKgjkn0SlokBKBM0LDehK5w-AGoTUwVy34SzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f945d97990.mp4?token=YqiuaXNDymh-M5NABvtZ3Htnkppgrb4J5i4I0tsfiPcqUgF5J7I-HTfOdSa8gHw3i-CIQsJSof8uHg6TqmoZ7iOAsPdM0_woJQYEiYNhYSjk0e_8yNjMegdd4-X9OOgCvtiH4juWwMkd4YCT_v7v4kwfT3xWMoahpZswh8RcvCb8T9t1F_VfdmvV0BGlMLvTVprZGbrRVs-NKLAdLtzgIdokiK2Iapi0kAzZxHpTv65IMWkiciJScyu3Jx-PgbV3t59sUfX2Pb1drF9eFa0nIHHQ0JohAL8p3je6kzooO2s6L-V1sSKgjkn0SlokBKBM0LDehK5w-AGoTUwVy34SzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔘
هفته سوم لیگ برتر بانوان / پایان نیمه اول
پرسپولیس 1 _ 0 وارش نوشهر
⚽️
زهرا قنبری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/140835" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0t-rt6_7nS5C7JJuqWUMyzER6lpeGFgIST_cpIoNx5BCaJqTz-qMHHqJGp7DEmy90VEUzDVD7sDU1-DN5t1B28fqaZX7cwUYVI0xsQyMG8G-ooMZEok4L4Yp4UQmCMZQTczJgooJamQsGP0mV6tXb8zxuciwll8ItNhYI_CEzTiCYLQeAZw3oGzQeDWhp2-_4tY4zE6PqJqzF2cOTN2hcqDFLVjfXRFuSMq0YEzr4aS2io8XCm92m9m99OjHm4A2rR32ZzlzAfEnf6PB9Uvx2-It7Fxr4v1F39N099S_MB4mVK1goYvwUxYoXbmqo7K1d5urTS6J-G5HAqRW3bulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پایان نیمه نخست دیدار تدارکاتی
✅
پرسپولیس یک ـ گل‌گهر صفر
✅
گل: محمدمهدی محبی (۳۹)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/140834" target="_blank">📅 17:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=jClV_TBb6sJQ7GeP7jv6YxGmssQ3oZPtz-zyu17cvjSkefOJNKTpTKMtQYaJs1y4S_p5xCRZe4cVi_88jHV3Ps6IH8RRivcgQ02nq___LdJWotIUEm14oiz_N_iRtRknpST1uyiycdJ66ZukKewfrppbPBVxFgBTkgT8YLE6QRYOK1dKM4hiHOHowW3cYPB5KlmvbCT7HWd3H_3p9f6fYxZr89lZNCFSZhlpebRqs1i8fUqZIBKycvONiF7WiRNJwE2gteeZJuMUlzN4y_4QDKfQuNrJrKhXJ32xFQGKmtQFEkGmIbrml2Vi1vsGmgE8w8hnd34Tu8wFU2_AbMPqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622eb15a1c.mp4?token=jClV_TBb6sJQ7GeP7jv6YxGmssQ3oZPtz-zyu17cvjSkefOJNKTpTKMtQYaJs1y4S_p5xCRZe4cVi_88jHV3Ps6IH8RRivcgQ02nq___LdJWotIUEm14oiz_N_iRtRknpST1uyiycdJ66ZukKewfrppbPBVxFgBTkgT8YLE6QRYOK1dKM4hiHOHowW3cYPB5KlmvbCT7HWd3H_3p9f6fYxZr89lZNCFSZhlpebRqs1i8fUqZIBKycvONiF7WiRNJwE2gteeZJuMUlzN4y_4QDKfQuNrJrKhXJ32xFQGKmtQFEkGmIbrml2Vi1vsGmgE8w8hnd34Tu8wFU2_AbMPqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حاشیه‌های پیش از آغاز دیدار تدارکاتی پرسپولیس ـ گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/140833" target="_blank">📅 16:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=auBBUt8yJC3kWOOSpSddLtY9GVzI8hJWL2cklF_760VhWDkpq0sDNZSitp_sZc5K5NdOj_BiqMLGCwaBq54mG7iUsXDZtm7k3Jpb7OJU8EJA1iivP69IWT3hZozeV-njeaeQy61hkR2oqB_Nh55dt_hhOqwpRiIpqhBY4o_opFSCeOUKXIwVY-OymDbkxlz0h0Apv5HCfcnYGceVy1ttLesp5Fy6gk_dVcCEBLANE9OU-1z-UdCHddf353CNQrfaa6Fnci1TvgA0z_XZQUjFXeoBdPmDvGjZp71-Oxr-QvGcW0LGKLywvw4g_onimD9sfTHAIgQjnPqMC09e9ZsDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff65ff20e2.mp4?token=auBBUt8yJC3kWOOSpSddLtY9GVzI8hJWL2cklF_760VhWDkpq0sDNZSitp_sZc5K5NdOj_BiqMLGCwaBq54mG7iUsXDZtm7k3Jpb7OJU8EJA1iivP69IWT3hZozeV-njeaeQy61hkR2oqB_Nh55dt_hhOqwpRiIpqhBY4o_opFSCeOUKXIwVY-OymDbkxlz0h0Apv5HCfcnYGceVy1ttLesp5Fy6gk_dVcCEBLANE9OU-1z-UdCHddf353CNQrfaa6Fnci1TvgA0z_XZQUjFXeoBdPmDvGjZp71-Oxr-QvGcW0LGKLywvw4g_onimD9sfTHAIgQjnPqMC09e9ZsDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شبکه سه اومد بازی جودکار ایرانو تو مسابقات آسیایی رو پخش کنه که جودکار ایرانی تو ثانیه اول بازیو باخت و حذف شد و گزارشگر اومد سلام کنه خداحافظی کرد
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140832" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140831">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi18b-7hA8cMMNK8rtr5VyPr-7ogBLIB7X16fUsCFBawl9dtoDYCWTI-S_66N28Ygd-rQ-TpGNf0g1-TXJX_A9me6MRYUZnDEzR4OzkTRDcWfeIUVexUCBIbXuM8Oa5-v16nHcaW2kChEiuIOnK6Pv7uTySUojQmTehbZCIlaQvex0yp5ljjFACVzjAdC8durvMJy-Ownnz5wKtRBSIZcQIDxN_l8COq7So-Do-lONUrOriomrhLDk2EyY9KMZ-8pF-FUuaIwO3TkgEmyj45tVFta6MR7RKdIPLvIki191EKTcnj88GWdkIgVAFiTk9ns8BxtnvJL9eRQez3Gunx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورونوف با بهره‌گیری از تعطیلات فیفادی به اوج آمادگی رسیده و اکنون با بالاترین کیفیت در اختیار مهدی تارتار است
.
😀
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140831" target="_blank">📅 15:24 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140830">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
#شایعات
✔️
هیئت مدیره پرسپولیس به سازمان لیگ اعلام کرده که در صورت اینکه نتیجه دربی 3-0 به سود پرسپولیس اعلام شود از بردن پرونده آسانی به دادگاه CAS صرف نظر می‌کند، در غیر این صورت این پرونده‌ به صورت رسمی با تمام مدارک به cas برده خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/140830" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140829">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-gzA9ZRyhBlQl61z3GV1Vhi-rkIk0CSS_lAVyY2Q8xW-qGnNyKoppfEYEEGsarrWThdKgSFRwiwA99lNWhMZvWeuZsEfOyK8mvFKuHURBnqBh77crfC6Z-rt1hNmBElEver_4jiGz-g-zxh4_XWHyrNBPYlNfaDRETCtceBslAILiOa6z7Lr4qr46hbc7MUlpBRdbfHy0n1JwK9HOdN9zHLoOsiiAYsG09DC5JxfLAefZ_yfVOvdR9NPYrE7n27hnRU3WWKuTO4GjTh8ls8liMioPQ-TZ4Z0BBEkeCzjnWSZRFbhQKJdXojGqAGVMf3KkowcrHQUz3DQ3sdADypng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
جدول مدالی لحظه‌ای بازی‌های آسیایی ناگویا
✅
ایران با 15 طلا، 17 نقره و 13 برنز تا این لحظه در رده ششم ایستاده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140829" target="_blank">📅 15:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140828">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAi1Jh-UvQuFTHQR2gJpQWsthtocSzDg2J_mzCgGWVwPUiHbW09BcLzev41jt9sZ2b2jHWshVR84adwdgSphfrdoizjGNRRmTYUmoDj1PQvjluP8_pqVv9KrxxKEKCM19T0MwkRSguWEL8dxbAQWJWGImVWAAbpxLoTM8tUDyylCYBX1W84lgg_J0ILwdBtHEGPq7ehs0-k3c5x0tNIBrY3qOeMLCvQD9w956aOKm-GIl4pFkLAW6strlDYRABsQ3Tf45Z47UilfAA25Qmi3b38VSOIk4fuCNsP3Oaa4Z-zevwbjDcpUSFd88wNTTNN7Iv1XUELDyJl6BRZWw2R3U-os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6703d31fc.mp4?token=pVQkApfXJAcynkCAUK2rXhZ495l0eLCRQM-e_20VvZJJBKmtl7ibw2_SiRPXynaHn94xYlpNPYsuP4s6HifG95zTBp2qIXnz4gL5NlUUr5QPT06ekW5CS_BQcAjGin3pTt9oT7QqnxO6VKtESvHWmw-svunn2XOKAGMYLCXqDECQIiffW8Zzy2DiN79M5q2nkShsNl2nMWw2CN50o34GtTitRRx4p4rgCVlVuOCR_2W1CQcEzMhcPprL7Pseg8OWfQSvGDuwcww0lslkTIydphSKAuaK0VYHkno_JPLu1MXdn5DqGNwXN8zsyEOjhQ9ZEIR1QcgympGjcg-8Qm9EAi1Jh-UvQuFTHQR2gJpQWsthtocSzDg2J_mzCgGWVwPUiHbW09BcLzev41jt9sZ2b2jHWshVR84adwdgSphfrdoizjGNRRmTYUmoDj1PQvjluP8_pqVv9KrxxKEKCM19T0MwkRSguWEL8dxbAQWJWGImVWAAbpxLoTM8tUDyylCYBX1W84lgg_J0ILwdBtHEGPq7ehs0-k3c5x0tNIBrY3qOeMLCvQD9w956aOKm-GIl4pFkLAW6strlDYRABsQ3Tf45Z47UilfAA25Qmi3b38VSOIk4fuCNsP3Oaa4Z-zevwbjDcpUSFd88wNTTNN7Iv1XUELDyJl6BRZWw2R3U-os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سکانس جدید از گزارشگر تکواندو براتون آوردم
😆
😆
😆
😆
✔️
کسب مدال طلا توسط ساغر مرادی در رشته تکواندو با شکست حریف ازبکستانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140828" target="_blank">📅 14:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140827">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_zMrFgXrxTEPlRCBBYfynWgQR6u_vzYqTTRTDUl016V6vnnhgRilmlz_9KG_oa9RgJDEQlN0PL1UK8dPAXmi3sKm0aHk5FDAdPuUHNkOhD6OFtEfhHu2CFWa-ep8OuQzsCXuHFzH8LPwL3McVCYZS1b2VQJDCrAzklWavzlm3KWz--wah9DBwR2GjuvNUHvOGrJlCEqGhquwp__W8Pvw2fZ3eUfy7HOXBY_J6LwgN8AyJ0dWu0tQn2OYUziVP-DKdrwod82CAAk8fy8a3x1eY5xlFlIH0FMNfC3G0aQRZ1Z9gu2zmCB_R2eWCRQQZbBKIKK1dcAegep4erjpOvk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
چهره خندان و شاداب جلالی در تمرین روز گذشته
❤️
✅
ابوالفضل جلالی مشکلی برای همراهی سرخپوشان در دیدار با صنعت نفت ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/140827" target="_blank">📅 14:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140826">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY9Rg4QOmncCPvNV2rAEEnNmOpWwGi4iaTsQAgZCuYo7tRakm2bP9Uc9G6PMx0SjqWd7Htwr-f27ixZ9kn2NcgqPpUHqjC0funUcre_erpdpASv12E1BqjY363ws6C4U9E9YsNmkoE9M3gyFO3BVul5ai5H_bQRu6yiK2E_xTMbUGFK5u8mjrvRKE1rHNfz7wLHaKtvum_xWXGbMsevJnpyk0ssnwXwgHRNq7CphLIVqVYdG7jDkvchy6JznfHZWx9ugAaSLh8_H_iElop_sQxFlwSrynhbANjFfi0k1ii1mBj2HfQKIwwNEDj6mZZHqfGJguXnczkH6ED9yl3A9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد خروس‌ها و آتزوری؛ جایی برای عقب‌نشینی نیست!
🔥
⚡️
[
فرانسه
🇫🇷
🆚
🇮🇹
ایتالیا
]
⚽️
فرانسه با وجود غیبت امباپه، از نظر عمق ترکیب و کیفیت هجومی دست بالاتری دارد؛ مخصوصاً با بازیکنانی مثل اولیسه و دوئه. ایتالیا بعد از برد پرگل مقابل ترکیه روحیه خوبی دارد و می‌تواند با بازی فشرده کار را برای فرانسه سخت کند. با توجه به فرم دو تیم، انتظار یک بازی نسبتاً نزدیک با موقعیت‌های محدود و احتمال گل در نیمه دوم منطقی است.
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
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140826" target="_blank">📅 14:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140825">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140825" target="_blank">📅 12:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140824">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
تیم والیبال ایران جلوی تیم دهه چندم اندونزی زانو زده و بازی به ست پنجم کشیده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140824" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140823">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140823" target="_blank">📅 11:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140822">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
مدیر پرسپولیس: منافع ملی؟
✔️
شکایت از آسانی را تا آخر پیگیری می‌کنیم!
✅
یکی‌از مدیران پرسپولیس مدعی شد هیچ توجهی به درخواست علی تاجرنیا ندارند و شکایت از یاسر آسانی را تا زمان رسیدن به نتیجه پیگیری خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140822" target="_blank">📅 11:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140821">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1aNWWJ2JHNz0k7VbGeNpG1ZYho64cEaA3upstIEHhvJR_2vouMnuMOSxyYRda8AJkrPPWh85exifpGpTImUKyjBaz_yoQRB5oiffCKP_fSEo_hVRICsFaFmxFz8hgKp0Zjshlrh1eCvD0LdKEGu5G2KE0oMoMKf5mBWz_WTlHAde21UPHuQ7ADapgx5-IIeHFzrxyMM7SFyA-V9DCB37Njc4U_7BA4YmtwF1e4M8j0yPGhWehfCUcarsdPy0Uj7PBLS8qGrtaGw71zlVnDvvvS6l1n-AfX97pD1-QiAgGMI2446TpdU1czQg2-UDVi_98KmJVFA18sKY_jjFYffmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
⚽️
👀
‼️
فکت عجیب ؛ مهدی طارمی در شش بازی اخیر خود در تیم ملی، نه گلی زده و نه پاس گلی ارسال کرده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140821" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140820">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
❌
علیپور شاید،کنعانی بعید است
❌
❌
مصدومیت علیپور رو به پایان است  و مهاجم گلزن پرسپولیس به‌زودی به تمرینات پرسپولیس برمی‌گردد اما احتمال غیبت کنعانی ور بازی بعدی زیاد است.
❌
❌
احتمال بازی کردن علیپور در بازی بعدی بستگی به زمان بازگشت او به تمرینات گروهی دارد…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140820" target="_blank">📅 09:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140819">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140819" target="_blank">📅 09:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140818">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6L4DvGqgvXDI4j9WVPA_rtHnzjV2f4HlFhGNcfn5wKhJSDsweAL6pMeAU9SMF5eokXOEDn6khNPyOM9slPN-6XR9tfwoizoUoIH1CQv6oz-TJDz-BcofnQKCem-dcESHJv-YzJ5LSRA2lejS8QCQjbOL-CYwWEsWNeWp-wa7l2CeKYbdBe2djZFDh2B3hB6nEGsCxiGFVzhJYuWUtOPSIikOhD0G8zA08zqPOYOLnLWJZrMsn053IjjQVfARzDTQbPCDrlrRChf9UK_cI3sF5fAkHi99eJz3XkupOcJmoLSpDZZiymxDu1zov1CJe5TVA_qotAud0eYZi_YkHYBcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امروز تیم بانوان با زنان نوشهر بازی داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140818" target="_blank">📅 09:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/140817" target="_blank">📅 09:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX2HBfxM1FYXJ-FANwo3wWMNszX7HmFtOJRwihc0V-ZUL7ohRpeb_OziQ181Twyykvcot9J7-vAkollKeYjjkPyO2TvmcZuSPYdLTxD6Ti0Me7MpJznOHTZy_Oiu9cYeX7i8yCPQz-apR8_NInJnh2czd2NyZGHMkKwIdTJV8Cb5SxCyoM2DpmP4W9EDSrg3t5IkJo6snJYoUCCKqA-OFR-8xddRBRK8x0A-fVh9c-Ae7DZ7cr9GCsSYoE7xfGG0amsDvJvRDeTqw350kOe9L42f4Y_wNTCJI9CBm0F2fv-M81UX3KBpURNvk0ToGgucJRNZq_7avUKXgnMeX6JDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یک شب پر از بازی‌های سنگین و دوئل‌های نزدیک؛ جایی که چند دیدار می‌تونن تا آخرین دقایق غیرقابل پیش‌بینی بمونن.
🔥
⚽️
از تقابل‌های پرریسک فرانسه با ایتالیا و بلژیک با ترکیه تا بازی‌های متعادل بوسنی با سوئد و مجارستان با گرجستان؛ کنداکتور فرداشب ترکیبی از مدعی‌های واضح و نبردهای کاملاً قابل پیش‌بینی‌ نبودن است. در سمت دیگر، اوکراین و لهستان روی کاغذ دست بالاتری دارند، اما فاصله‌ها آن‌قدر نیست که بازی را از قبل تمام‌شده بدانیم. ۶ بازی، یک ساعت مشترک؛ از اولین سوت تا آخرین دقیقه، شب فوتبال ادامه دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140816" target="_blank">📅 01:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLB0cI7jqx5SBeqKi8QMKtan0IDqoP8qe-uf7NKLPKEPL1OKhowrH7zcSu0GxUUwcPVj1MLjbgHXkj7uNHNbumXBve9pykwiUGJyD91SwWbPL6xQTmlF1OCKtimY4ZVZnK3EvMAJ5KJvC3hRRoB6BsDVUJFl8KoJ78hfqPy1JYai3g8MDdhhKFq68TxqtqfaSGw-QI7DM3vjdtrRaKCLk2T6IGJjMN_wVxyevaWB6I0VbcCRNYG0Uzrjg0TBfEZ5LqctjT409kQvBZPm8Opgy19fWGekdiea_cyscMWQIeqjj_qkUNC4KJdCzFgA1sUk3_8FHfBITk1uTBLMM30mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گفته میشه که پویا اسمی ۱۶ساله یکی از استعداد های جدید و درخشان پرسپولیس هستش و تارتار میخواد بهش بازی بده و مثل زارع تو گل‌گهر بهش بها بده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/140815" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJuApBbzDUPBTW93ItKDo6O5NvNtEbI7MqFk6ySuQf_yqRyc_wBi_5b9FgnOccZmaTqVc2iiXia8yxdbf_8yEn-8khArG0nmgtOHoFYuS7ccV9cfF7yc9nky1IVMeICrYTf5YsvW-UrY4b9hyp88Gf5wGvXW9F3lXdRgOUAHmeNt72WZ-R_VYTj8Tr-HvNUDcdrFH_L_GM4CfsOoqXT3pfXEa3ahGR5_8syR0fNA-__xkhvVGzJb_WOMjlBlIgmJG6lGjkl7OowQVCEQ3Q1X6_9TGR9WXlyuEmzd4fenNGFa-l4X1hOg9Kp_Io8CSGA2EBMPeILIez4sAx0iblFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
پرسپولیس فردا به مصاف گل‌گهر می‌رود
🗣
تیم فوتبال پرسپولیس در آخرین دیدار تدارکاتی خود پیش از آغاز دوباره رقابت‌های لیگ، فردا (جمعه) پشت درهای بسته به مصاف گل‌گهر سیرجان خواهد رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140814" target="_blank">📅 01:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
رامین رضاییان 2 ماه به دلیل مصدومیت از میادین دور خواهد بود.و پنج بازی آینده فولاد و از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/140813" target="_blank">📅 00:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPmrA1lyhDeVGo4Rlyuq95kytLS4gSuQeTZXoFdpLczte1k6HqclkxwcX8BTxrX_x0-8SuCzzkydV4-PkGT6j9TlifNh9q9fkoVGp0kLAJekE2xMoX1ntvLtK60F3CJY4lRNEqAs3BxEMqpWweE-KaHe2L15H8ntZw3AU6WV14aSOFoDd1lFN3aqQINUgKM7LNdjqRwESUPnx3TYWJvPi2oKrQ9imIvcV_FTnIleYnommsFRAQQAzKiAvgxtUZ1BYk997Y0b0SBJJQj2HH12VUPjccYpfRjukOsW4DO8ZnaTUNJQECd8vIttoEwDeAj8T4PPY8DHpPuUTDCmLpcoCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت ملی پوشان پرسپولیس به تمرینات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140812" target="_blank">📅 23:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/140811" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
جنجال قرارداد گرا در رسانه‌های مجارستانی
🔺
رسانه‌های مجارستانی با اشاره به غیبت گرا در ۶ بازی اول پرسپولیس، دلیلش رو مصدومیت پاشنه عنوان کردن و درباره قرارداد و دستمزدش هم نوشتن. همچنین مدعی شدن پرسپولیس دنبال پایان همکاری با این بازیکنه و اختلافی هم بر…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140810" target="_blank">📅 22:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/140809" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
❌
ادعای جنجالی حسن روشن درباره ساپینتو
⬇
حسن روشن، پیشکسوت استقلال، مدعی شد در دوران حضور ساپینتو در استقلال، اتفاقاتی در اردوهای تیم(دختر بازی) و محل اقامت او رخ داده که حاشیه‌های زیادی ایجاد کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140808" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140807">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
❌
خبرنگار: شما ایرانی‌هایی که آمریکا باهاشون در ارتباطه رو «دیوانه» خطاب می‌کنید؛ چطور میشه با آدم‌های دیوانه به توافق رسید؟
❌
❌
🇺🇸
ترامپ: شاید منفجرشون کنیم. باید بین این دو تصمیم بگیریم؛ یا منفجرشون می‌کنیم یا به توافق می‌رسیم. زمانش که برسه، تصمیم می‌گیریم.…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140807" target="_blank">📅 21:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
🟡
🔴
حسن روشن:
🤔
🤔
ساپینتو اکنون بهانه دیگری پیدا نکرده و روی داوری تمرکز کرده است. ساپینتو یک مربی درجه سه است. صریح می‌گویم روی آدان در دربی نمی‌توان حساب کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140806" target="_blank">📅 21:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
یاسر آسانی: رامین رضاییان کسی بود یک دقیقه بعد تمرین تمام اتفاقات رو لو میداد و همه میفهمیدن و ساپینتو برای همین لج کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140805" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140804">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140804" target="_blank">📅 21:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140803">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
هاشم نژاد به تمرینات تراکتور برگشت و برای بازی مقابل استقلال اماده هست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/140803" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140802">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpTM5ufOPPeBix3pFYkK1a11ELizqCTFLNCC0uuq8ENgFy-yvhFNqaaywjo2z_6Zjbbrpr7q6Cpr-CI7cHTJlN7UmBkqoN8oXOinpGLklf2PB3-isJs4FKVJoT3Ypd5fOqSf0R9ha9DNa5ucWkcurs3KlS_-RUGLEWDubmXI0EtSqNrNtzFeOWYR9zfmXF797dkRLW3YOSiT7Ox2IOljPiwO80_9IZHBAsIvsb_8CjLdGI7fGTtblht--doCmylTSnwCWD_78M8fgbmTKS6-YtpCU7cSlCdsA1Xci0Us0KxkpmBYAiDs-BsOnW3b5tHGfLn36naCpN0QvrK9rZcnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نبرد شمال و جنوب اروپا در یک جدال سنگین امشب در پارکن!
🔥
⚡️
[
دانمارک
🇩🇰
🆚
🇵🇹
پرتغال
]
⚽️
دانمارک بعد از برد ۲-۰ مقابل ولز با اعتمادبه‌نفس بیشتری وارد بازی می‌شود و در پارکن هم معمولاً تیم سختی برای حریف است؛ پرتغال اما با ۶ امتیاز صدرنشین گروه است و دو برد متوالی داشته. نکته مهم امشب غیبت کریس رونالدو است؛ او اردوی پرتغال را ترک کرده و برونو فرناندز هم با مشکل جسمانی روبه‌روست. در مقابل، دانمارک روی هویلوند، دامسگارد حساب می‌کند.
سناریوی محتمل: بازی نزدیک و پرموقعیت، با شانس گلزنی دو طرف.
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
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140802" target="_blank">📅 21:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140801">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140801" target="_blank">📅 18:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140800">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7PIxbJgHyrsQu-m7l3Oe9GufSJRVwcKNkFfqlB1Fa5mySf_WtlNJ8-N1lwL9lcKUdvnIxwiq1Il5x1H6kvlxQXNlWIqwuNd2jAyI7avAxZQs5yGsWIzE3eresW1mIamSgchI0vxTcFEQvtoa4P8VWHwsogdxN5jXSIGIojAiShMAR8u3LFqP5x2QKkCBYOCqVwaph-3SvLcLs4yhbQe_ZusFTYuUxxpwNV7EyRtCI2ig1ZHuB5EmVCN_zD4TvztKsSxw4QtzWyt7IOpM4gPB47bzvx0o6CUQ9RXAMd3rL66C4B3CSL4lfdzQ45oG6JJgAwYf5rBeFcojhrQj5w5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی علیپور دویدن را آغاز کرده و احتمال حضورش مقابل صنعت نفت وجود داره/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140800" target="_blank">📅 18:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140799">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOITnLXkuzLS4i64xad0rllYm_Fj13nrIfzDjkPzLSXwyBteqddtq2t15i-jCg2DroqWPSPEvsyMhj7x0z22vQ_9BdQ9sEFh2LWOF8wHbFwn5mBqyLkuKrI0uqwbVch2jXB2rzun4Rxlu28pqFkmhe2O2Qk2RnNl2W5P0rr5EKXcx8bCMLK8XlwhaGfwDu0I9EIxS3rukiACx6ymP_ojjQWHY8HbHqdkomprjGN05OnEEwtERkSD0n0c5-mroKV3qfvjsWzOFgP5PyqPIVun7CVv20PPmaIQqJ7Fn2kVE8wtEfryTb4gr3NthjaZimO7RIyjnqUemKBQfTpLrQcKfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
گویا بازی دوستانه سلحشوران تیم ملی برابر گینه بیسائو به دلیل محدودیت‌های پروازی لغو شده است. به این ترتیب سوژه خنده سوم این فیفادی از دست رفت!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140799" target="_blank">📅 18:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140798">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/140798" target="_blank">📅 18:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140797">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMjkfyYWnGZ9RybT5WhtIzMNygdn4R3YJLRHboxGs1pvsPd_3n3lBpXPTnUwV9st4ruu2skd-22Um1q4kI0lkLZxP1QcHzh3q_vbVxdb6b2vc9-7zet0eQHJm1nvok-wD_zVA5-bS7c3QtR4lDCIxBYidr51leexXlHHgFaqH9k3xCgfBsYHV_0MrlXLnSxDU8CPfaEmoGdHz6HMJ5r8mru7o2q2DEgZ83yytUTVLc2GoAoIvozTFbbHlcR9S3xUuAezr4k-_ZfTX6tgHTWI3GvZmTvtQW4fnNMLfdmRdlsANn-8O_2L8Czv-hJqbAHO1o6FWhHa8fEhPSoETg2Jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
ایجنت دنیس اکرت در تلاشه که این بازیکن رو فرو کنه به یکی از تیم‌های ایرانی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140797" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140796">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPsFXR9_RZ1G6qI7xrekms1QBhl9a4meOEq4PDJh2QmAToG4R5GSVn2E0WqC2qCnV4H8XiP-VBcKjvi9ndc-g2o4b06r20Ae8dK1FaWXcdthavi3SquuH0vY2IeL2H-bdg8Mdzi_J0DqFSygnCWq0Sfpig6D8jYjChCvSnU4KVmkBs1ZOZ1rLPfCFfyCqSfFMqjV3JADWiLML3patbVl-0Wj47iFql5hPUUI73RfgUqIYM5xlzsTAjSm3iYtWEsl4w9GxQ-IYcqgWV7jTC6uvQr6mQnV_EifrKAJNhLfHATvs2WG8rp3DnmZfw-MbxeQ1jyf3WBXAmlCa9uULwJRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/140796" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140795">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t87MNSoq2GeGEMOehKNF25AFL3_Y7mHDn1iV4eUYsKd8F6NQrZQlOKjewGe3WcfGbtVXcSfiCEwwWQI1bgdM3fDe_d5uPgossGqRiMjs3YsGE4OKPWBmeheMLYd63jLe9unhj2yOLNIVQlOn5N7fLuCb21sodopxXrxeRIfb1Bm4eppmG-LOgoI9iKL1FOl0hHuHv6WSvN5uu9ky030eTCSp29FWMvxfOukIzt6klds7t10OVIkE-EOkpgFKu5_1ChO99yMxHRjZg6Jqrur48HMv3xzD8gGSKX_6G7zGDGV1A3wRcjAFYxJV21rFjyyYDuEOIVFeeveZviaes5woQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیشب در بازی دوستانه بین کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردند و گفتن بقیه بازی رو وقتی انجام میدیم که فلسطین آزاد بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140795" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140794">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140794" target="_blank">📅 16:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140793">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX8FD8R-icRHVn91Ub7lHsm3VGkxou3Vw-UoCkT5972x0kAR1HJuVHkfPEFWdI1qOX_PKn3Ep-Cr4yjbFJrXWq2QjZZx3PkW1wnGPVmDBy7kIUZ3QZLFh1gc2i6VtMD9IA9_0dMOIbzZLA_a5xkAvB2t_TVq1xg2fMhgDHB1oeC8jmd1I9sDOmoEkvQIIhlPa9KzBtpibLPQurczYmgs0MBirgwZyYWBkucSoCjJf13YoKYMWkSpo0Bm4CoN3SVFlay4H-ZXyvDBtbYrPczacDobJIGnB0AZ9TWsP1KHsTyqQFrWIBnNykSv0NpT7tugD8Rt_BIVAu2QOYoCaUeLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🔴
در یازدهمین سالگرد درگذشت هادی نوروزی کاپیتان فقید پرسپولیس، یاد و خاطر این بازیکن در دیدار امید پرسپولیس و سیاه جامگان زنده نگه داشته شد.
🔺
پیراهن شماره ۲۴ هادی نوروزی در دستان هانی نوروزی فرزند هادی و بازیکن تیم امید پرسپولیس در عکس تیمی پیش از بازی.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140793" target="_blank">📅 16:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140792">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bo1ST_YWS03tODpJuNdqchY5z8R4VtOVzz_0ep4r5HjKCqy6DmaEhN60JsIbVI2tzBq6zcIxqXAefcPuql-b9pdqtF9n71FQ8x8NOLq4oJlmdk421przH-GvMkfyy27lPwH4OdLd007-y56jugrVGozXREF9MnumUijgOcd7Wv2AwYI5JCU16lRnCB5KRD1Wc2wUvLqL6uif3FE5A56TpBOrbez47SdbrOoPQU7SG0CUygQv800pZeqn6v_MX6XHSyv3b4lgKLlAFh_x9Y6vHsULrQ5uVENcyF0Op31_QMtIQpMrBw3QESbqhJwpqY4U_QJpj6GZy-lRKJYwuN5_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
Germany -
❤️
Serbia
⏰
Tonight 22:15
🏟
Allianz Arena
🇪🇺
آلمان بعد از ۱-۱ مقابل هلند و شکست ۰-۱ برابر یونان هنوز زیر نظر کلوپ به برد نرسیده و مهم‌ترین مشکلش تبدیل مالکیت و برتری میدانی به موقعیت‌های باکیفیت است. صربستان هم شرایط خوبی ندارد؛ در دو بازی ابتدایی لیگ ملت‌ها مقابل یونان و هلند شکست خورده و با صفر امتیاز قعرنشین گروه است. از نظر تاکتیکی، انتظار می‌رود صربستان عقب‌تر بازی کند و فضای کمی بین خطوط بدهد؛ خود کلوپ هم روی همین موضوع تأکید کرده و گفته شکستن دفاع فشرده برای آلمان چالش اصلی خواهد بود.
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
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140792" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140791">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭕️
⭕️
⭕️
خبرورزشی: مرغ حدادی یه پا داره بردن شکایت آسانی به Cas همین و تمام
⭕️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140791" target="_blank">📅 14:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140790">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
✅
✅
تیوی بیفوما که بدلیل مسائل سیاسی دعوت تیم ملی کنگو را رد کرده بود دقایقی پیش برای حضور در تمرینات پرسپولیس وارد ایران شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140790" target="_blank">📅 14:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140789">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
🇬🇭
کارلوس کی روش بعد از باخت خانگی ۴-۲ غنا جلو گامبیا سیکش از تیم ملی غنا زده شد و باید دنبال تیم ملی جدید بگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/140789" target="_blank">📅 13:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140788">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/140788" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140787">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🗣
سرگیف و بیفوما هردو در تمرینات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140787" target="_blank">📅 13:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140786">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
قطبی یک قدم تا بازگشت به فوتبال ایران؛ مذاکره ادامه دارد  •
✔️
✔️
مدیر برنامه افشین قطبی اعلام کرد مذاکرات با فدراسیون فوتبال ادامه دارد و دو طرف در حال توافق بر سر شروط همکاری هستند. طبق مذاکرات انجام‌شده، قطبی قرار است مدیر فنی تیم‌های پایه و سرمربی تیم امید…</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/140786" target="_blank">📅 13:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140785">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
محمد نصرتی درباره حضور دنیس اکرت در جام جهانی: آقای قلعه‌نویی، با دعوت از اکرت در حق یکسری بازیکن جوان اجحاف کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140785" target="_blank">📅 13:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140784">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
❌
هفته هشتم لیگ برتر در آستانه تعویق!
✔️
✔️
در صورت قطعی شدن برگزاری سومین دیدار دوستانه تیم ملی در فیفادی پیش‌رو و انجام این بازی در ترکیه، احتمال تعویق برخی مسابقات هفته هشتم لیگ برتر وجود دارد.
✔️
✔️
در این صورت، دیدار حساس استقلال و تراکتور نیز ممکن است…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140784" target="_blank">📅 12:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140783">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
فووووووووووووووری
❌
محمد مهدی محبی مصدوم نشده و اصلا مصدوم نیست. امیر قلعه نویی دیشب با هماهنگی قبلی برای توجیه شکست های پیاپی به محبی ستاره تیمش اعلام کرده باید تا دقیقه ۳۰ مصدوم بشه و تعویض بشه تا فشار رسانه ها کمتر بشه و این یک حربه از سوی قلعه نویی…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140783" target="_blank">📅 12:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140782">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
میلاد سورگی: از باشگاه بزرگ پرسپولیس ممنونم که باعث شد من به فوتبال معرفی شوم و به تیم ملی برسم. امیدوارم روزی به عنوان ستاره به پرسپولیس برگردم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140782" target="_blank">📅 11:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140781">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🗞
لیست بازیکنانی که قلعه‌نویی ازشون ناراضیه و شاید دیگه دعوت نکنه:
❌
محمدمهدی محبی
❌
صالح حردانی
❌
سامان فلاح
❌
احسان حاج‌صفی
❌
حسین حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140781" target="_blank">📅 09:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140780">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140780" target="_blank">📅 09:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140779">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
پیگیری‌ها از مسئولان باشگاه پرسپولیس نشان می‌دهد که هیچ پیشنهاد رسمی از سوی باشگاه‌های خارجی، چه از قطر و چه از سایر کشورها، برای جذب محمد عمری به باشگاه پرسپولیس ارائه نشده است و بحث جدایی این بازیکن صحت ندارد. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140779" target="_blank">📅 09:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140778">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
یازده سال گذشت
❌
روحت شاد؛ هادی جان 24 ابدی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140778" target="_blank">📅 09:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140777">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
❌
دراگان اسکوچیچ از طریق واسطه‌های نزدیک به فدراسیون فوتبال، برای بازگشت به نیمکت تیم ملی و هدایت مجدد ملی‌پوشان اعلام آمادگی کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140777" target="_blank">📅 09:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140776">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم./فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140776" target="_blank">📅 09:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140775">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBDdXMJ1MCRwmpOR3Mp1tv-ZnMjAtPxbvSoUvPtSfHfj8fqC4MBsOSkf3m1mX9Ri36Fu3wDYAzKePp7MoFE_PWlCkW6Bz1aXF6-e580PKCMiMUy529FvJHEfoFxaIKCzzNVvsCaeTzQ5nSJQwwjmXBGbFMu8sxCE6Ol4IZMSx8F7sMWNqnFSfzCf3FlDCLkEsWqTik7X0SBea42_-_epmsib9XhzofTwx0o8nu9W90ZPw749UezmlnJat7azwA1dQpDFCg7Q4v1adgwBizwpcxSQ8hm8Fk9xJpJe_qppxDLIXZGCVUGQ6aeqLvcbyZv-4TNSeTdaIPjCxfQR5HWINA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140775" target="_blank">📅 08:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140774">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqWS4MtMwGTeAu-wOUx3ExaEm6GlnAoowycBd0qzEuBPmgIDffzc6JkbOJKp0tXWhizC2oD7zLeK96RhaAk_yGFZuI8Iu70Ne9kfioChYkXu5GbeESCDoy5EVYpNT_5mR6m8fgTzGVGDzA5eqhaXsBup3MZd987bScXsjm7nAugfgQvi3Xxj_jHgrmwQJuY5kPEPbTElMw8fGpKUkmndisV_e_dapApuxQv5RdVUOIVGzBA6v1Ny3vRusxjf5I6kXHiqgcz8WeN-XPcBiza8ZWiDGhJ6lINlsE_vPlOeMNWJnv-ynvovE7VA-8QpYSiovm3WUeaekhWkqd7IZEumJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبِ سنگین فوتبال؛ چند تقابل با پتانسیل غافلگیری
🔥
⚡️
⚽️
ژاپن و اکوادور شروع‌کننده بازی‌های فردا؛ کنداکتور فرداشب پر از تضادِ ضریب و احتماله؛ جایی که بعضی انتخاب‌ها از همان ابتدا جهت مشخصی دارند و بعضی‌ها تا دقیقه آخر قابل پیش‌بینی نیستند. آلمان و نروژ روی کاغذ دست بالاتر را دارند؛ پرتغال، هلند و اتریش اما وارد بازی‌هایی می‌شوند که یک اتفاق می‌تواند همه‌چیز را جابه‌جا کند. فرداشب، عددها حرف می‌زنند؛ زمین تصمیم می‌گیرد.
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
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140774" target="_blank">📅 01:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140773">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
🚨
فوری/ ترامپ : به زودی اتفاقات مهمی درمورد ایران خواهد افتاد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140773" target="_blank">📅 01:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140772">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
فرهیختگان : دقیقه ۲۷ قلعه‌نویی خواسته حاج صفی بیاد تو بازی تا رکورددار تیم ملی بشه و به محبی گفته یجوری بیوفت زمین که انگار مصدوم شدی وگرنه مصدوم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140772" target="_blank">📅 00:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
تعویض زودهنگام محبی، به دلیل مصدومیت که احسان حاج صفی جای او را می‌گیرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140771" target="_blank">📅 00:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHM2o0uKLRRu5WRiMrB1BrpzHMOPjJdE2kldZQeTawydPwQolwVDis_l63ALiHTVqsnJsdSzf-JmWGR-wujKWo3U2RPOCRorHkWGTLT-Ik_0BzBW2uJHmt1P8mm0jYdUVG1ANi9P9h3RfQxpzqaZxplB6t85AIpH0lRPonGVG4hbokgcefzR8BznC7_P1g7gTMwZ2EdmOa0k6CUWlxV50ork2rt0GdhpOnxKO54PEBHrO7Z3xUm_uY4nR1bKTw4ZwdEqnRXTjk1kMUTAyld3Z1VnrXqb2wX3cmivp88sQkP_FTdYWFdUBxk5eaAfLOloZVfCo9o_cv6i9mI8fv-l2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
عالیشاه در خانه
❌
دیدار تدارکاتی روز جمعه میان پرسپولیس و گل‌گهر در ورزشگاه شهید کاظمی فرصت خوبی برای قدردانی از کاپیتان سابق پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140770" target="_blank">📅 23:57 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
