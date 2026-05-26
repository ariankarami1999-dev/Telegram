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
<img src="https://cdn1.telesco.pe/file/JwZvlN3SfKHswx2Q-1V7_oRVACDxAX8LRGbYMmegLC_QvZ0leErQjXY9_sOSx9MuFcCQrBEVKpa9hakD7j4Qjuru4I2fJ7U6MEQ-3NX01uV6zz4X9exGQjWHHsIQn0y82OaxOTbt4oOm6dZyMkcMRC2dAs6xLSfQ_ZHGNvCciyTwHWJN0jwaprzX29z09-2wNAiF30qI1nPshLgCO8i5syxZ_uPykjPwAkR93Yt1LwDdqDjw8QwqcYctRU-Z6JBjJbgCL6YxWsyZtnmRdooeq96wSiOIIK_g0onhLM7wksthnHTlm6HphW0I5etxFYeuqvd6yLgWIf3ZkUDoZvBD-g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 01:19:54</div>
<hr>

<div class="tg-post" id="msg-3465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3465" target="_blank">📅 23:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">حقی که نصف و نیمه بهمون داده بودن و با فیلتر رو ازمون کامل گرفتن، بعد ۸۰ روز هم پسش دادن، به همون حالت نصف و نیمه.
شرمنده اگه یک درصد هم باعث خوشحالی من نشده این وصل شدنه. هیچی تغییر نکرده.</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/MatinSenPaii/3464" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سرعت آپلود شما هم پشت worker و کلا کلودفلر پایینه بچه‌ها؟</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3463" target="_blank">📅 21:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⚡
cfray v1.1
یه ابزار تک‌فایلی پایتونی که همه چیز رو برای مدیریت کانفیگ‌های VLESS و V2ray پشت Cloudflare یکجا جمع کرده.</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3462" target="_blank">📅 21:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینترنت برگشت، و خوشحالم که توی این مدت تونستم کنارتون باشم و توی اتصالتون به اینترنت آزاد راهنماییتون کنم
❤️
همونطور که همیشه گفتم، زحمت اصلی رو برنامه‌نویس‌های عزیز کشیدن. افرادی از جمله پترنیها با sni spoof، امین محمودی با MHR و MasterDNS، aleskxyz با پروژه‌های خفنش، iampedi و تیم خوبمون با اپ WhiteDNS، سارتو با پروژه TheFeed، سم، مارک، Samim با پروژه شیر و خورشید، و همینطور بچه‌های کامیونیتی زیرزمینی Vasl، عزیزی، امیرپارسا، ریتالین، GuardNet و... که اسم‌هاشون بی‌شماره.
می‌خوام بدونید که خیلی از افراد پشت من بودن تا بتونم آموزش‌ها رو به دستتون برسونم. و اسم خیلی‌هاشون رو نمی‌تونم ببرم. از اون عزیزی که به من صد گیگ کانفیگ داد گرفته، تا بچه‌هایی که قبل از آموزش‌ها باهاشون مشورت می‌کردم تا اشتباهی نداشته باشم و همه‌چیز بی‌نقص باشه.
همینطور از افرادی که به من دونیت کردن و من تونستم کیبورد و موس بگیرم که وضعیت بدنیم بیشتر از این اذیتم نکنه، و راحتتر بتونم تایم بیشتری رو پشت سیستم باشم.
صمیمانه از همه‌تون ممنونم
❤️
ما همه بدون چشم‌داشت کار کردیم. و هیچ منتی سر شما نیست و شما هیچ چیزی به ما مدیون نیستید.
و ما کسایی هستیم که امثال سگارو، یوسف قبادی، IRCF، وحید فرید، یـ‌بـ‌خـ و... رو دیدیم و قدم برداشتیم توی این مسیر.
هفته‌هایی بود که چند روز پشت سر هم نمی‌خوابیدیم، با درد مچ دست و کمر و چشم و تونل کارپال و وضعیت جسمانی افتضاح خیلی‌هامون ادامه دادیم؛
فقط و فقط چون به آزادی باور داشتیم.
زنده باد ایران</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3461" target="_blank">📅 21:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3460" target="_blank">📅 20:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3459">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تا فردا-پس‌فردا به احتمال زیاد روی همه‌ی اپراتورها کلودفلر رو باز میکنن. و منطقه‌ایه
مثلا اینجا حتی ایرانسل هم قطعه هنوز</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3459" target="_blank">📅 18:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3458">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستانی که همراه اول و شاتل و زیتل دارن، حالا حالاها باید بشینن تا وصل بشن</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/MatinSenPaii/3458" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmin Mahmoudi</strong></div>
<div class="tg-text">نقطه قشنگ ماجرا خارج شدن این موضوعات حتی از ایران بود، این افتخارش رو هممون بدست آوردیم، هرکسی به نحوی کمک کرد.
یکی روی توسعه کمک کرد.
یکی با ساخت ویدیو کمک کرد.
یکی با توییت زدن و معرفی توی کانالش.
یکی با استار دادن.
دوستان برای پروژه ها نرم افزار اندروید ساختن و ....
همه باهم کنار هم باعث شدیم پروژه ها خفن بشن.
همه با هم کاری کردیم که پروژه مثلا MasterDnsVPN، چندین روز بهترین پروژه زبان GO توی گیت هاب باشه.
همه با هم کاری کردیم همین پروژه 2 روز توی ترند گیت هاب باشه و اینا همشون خیلی خفنه.
توی پروژه ی MasterHttpRelayVPN، هم همه باز همین کمک هارو کردن و موفقیت های خوبی بدست آوردن.
همه با هم این کار رو کردیم، کار یک نفر نیست.
این مدت جدا از بد بودن و سختی ها، همه با هم افتخاراتی رو بدست آوردیم ...
که همه با هم باید به هم خسته نباشید بگیم
❤️
درکل همگی خسته نباشید.
امیدوارم این روز ها دیگه تکرار نشه ....
همگی عشقید و خسته نباشید، دم همگی هم گرم
❤️</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/MatinSenPaii/3457" target="_blank">📅 17:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اسکمرها و کانفیگ‌فروش‌های دزد و گرون‌فروش، هم‌اکنون:</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/MatinSenPaii/3456" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=LG5maXgm8iMFr7vdQ75suId-dK3glLL6x-y9I8zAWXrbHruT9ZB9u3SPwGb8qrmRxAV0JB10YEcNMny19uIos6MijC1ROV8WUZVmU4XBTHLRE_-X94nDwn3YIdityAKoIxzKHsWQ1uZnxamTbstGTOYYKNkTbdPxaNmmTJL-oC4FNy_xtOeHmA3tdSFnw6_i0kITOmhnPjWv1e4rY8O4m_dzVbAZzGSrTnAcMC2ql6vyjPTMtH-36ckc_LneNKrIy_IGzxuwPpjp_foRiE8LEwh1J9YQI_crBlLNdWLnJl2a08b4Zkho-0OjkUYhUQenCtPx18PVgY9fJ2Q0G9OcqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/18fbc73a71.webm?token=LG5maXgm8iMFr7vdQ75suId-dK3glLL6x-y9I8zAWXrbHruT9ZB9u3SPwGb8qrmRxAV0JB10YEcNMny19uIos6MijC1ROV8WUZVmU4XBTHLRE_-X94nDwn3YIdityAKoIxzKHsWQ1uZnxamTbstGTOYYKNkTbdPxaNmmTJL-oC4FNy_xtOeHmA3tdSFnw6_i0kITOmhnPjWv1e4rY8O4m_dzVbAZzGSrTnAcMC2ql6vyjPTMtH-36ckc_LneNKrIy_IGzxuwPpjp_foRiE8LEwh1J9YQI_crBlLNdWLnJl2a08b4Zkho-0OjkUYhUQenCtPx18PVgY9fJ2Q0G9OcqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3455" target="_blank">📅 17:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نت خونگی اوکیه
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.21.7.21:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%202</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/MatinSenPaii/3454" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3453">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قربون دستت حالا که دستور دادی اینترنت باز شه
یه دستور هم بده اونایی که کارشون رو از دست دادن برگردن سرکارشون
یه دستور بده اونایی که زندگیشون از هم پاشید برگردن سر خونه زندگیشون
یه دستور بده اونایی که سر اجاره خونه خونشون رو تخلیه کردن برگردن خونشون
اینترنت شاید برای شما یه دکمه روشن و خاموش باشه، ولی برای خیلیا نیست واینترنت زندگیشونه که با دکمه خاموش و روشن به حالت قبلی برنمی‌گرده.
✍️
Reza Jafari</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/MatinSenPaii/3453" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🍷
بازگشت همه به سوی سایفون + v2ray هست چند تا جدید که گفته بودم میزارم استفاده کنید ip جدیدا رو
✅
141.193.213.11
104.18.38.202</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3452" target="_blank">📅 16:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3451" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6rxK2hUE6aOEr808Idxh6surO5bPbySykTKAgg-cPGipy3CBQUwO65Ro6bGqQJEGM-cuUJ9Ee7A4IyD6AlXxJ2Flsuvx5QK-7Oy1hFOVBJ5DXVhocMZxdg9snYih3_CBRRmIcnvHytCL52MUiQILE28CRSGly1PESLe1d5MG9MD7Ee83c2ba_IITjmGTBVtj-B7zs3PbUO9-x_-AOYhn_gC9YQi3E7hg6L-HHinTcSOIFAcXqxRP8m-q6J7G90Y_XYp8jqG7iWDCqc90p9WWS6FbTajPiq1dp9eioR_0hCiiVS39vRNFO51LGXoGItDuYjX245LWNKAsJ26mMN4aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجدد کانکت شد</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/MatinSenPaii/3450" target="_blank">📅 16:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قطع شد
😂
چیکار دارن میکنن</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3447" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3446" target="_blank">📅 15:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.7.70:2096?encryption=none&security=tls&sni=sni.111000.indevs.in&insecure=1&allowInsecure=1&type=ws&host=sni.111000.indevs.in&path=%2F#Humanity%201</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3445" target="_blank">📅 15:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Matin SenPai
pinned «
☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB  1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید): https://t.me/MatinSenPaii/1965  2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3444" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">☠️
آموزش اتصال رایگان با آیپی تمیز کلودفلر و کانفیگ‌های BPB
1- ابتدا ویدئوی ساخت پنل رایگان BPB رو از اینجا تماشا کنید(هم با گوشی میشه هم با سیستم. از نصب دستی استفاده کنید):
https://t.me/MatinSenPaii/1965
2- سپس آموزش قرار دادن آیپی تمیز و سایر تنظیمات BPB رو از اینجا تماشا کنید:
https://t.me/MatinSenPaii/1980
3- این لیست IP رو طبق آموزش مرحله‌ی 2، توی قسمت Clean IP قرار بدید:
104.19.229.21
104.18.139.67
104.16.80.73
104.16.117.43
104.16.89.120
104.16.118.43
104.16.63.25
104.16.7.70
104.16.79.73
104.16.90.120
104.16.62.25
104.16.6.70
4- از قسمت Raw (without settings)، یا Normal، لینک ساب رو کپی و داخل کلاینت V2ray خودتون وارد و به راحتی استفاده کنید.
5- اگر دامنه
workers.dev
روی اینترنتتون فیلتر شده بود، از طریق این آموزش دامنه جدید ست کنید:
https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3443" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3442">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه کم دیگه واستون مرتب و تر تمیز میکنم آموزش‌هایی که قبلا دادم رو دسته‌بندی میکنم و می‌ذارم خدمتتون</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3442" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l1V6EHLapOX053Tml-BNZJqUC1t0eb24aJpsz0Bs2HVoFmvUK8fLQI7vfNHU0I6enb_KU0dE5AGf1pjwyzZAOXqyVn9cKqP4HOYwLZUGE4svR--9qVZ9dv106BNvCyPW-AYi0tZhAgSxST3iuWsDQudv-Lq2nsr7LP1TdWiUkvl0cOI8RbjBgeus4JfbNcS0dxI3ZxY74PJ5CBkqafbXfPeWlZHPxgVuPvD_wFJiRVVmD3_BfdnJJ5YGLoDMFZ-eNLLqtIxKLgn90I5CXh1CGZmJmaJj-unFN2kFLctXESalKeQUAs1WSlKkQCcfoEFfG1nN7L-1BHCe-GWxUl6Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/3441" target="_blank">📅 15:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">با این وضعیت، کم کم نت‌ها رو دارن آزاد می‌کنن
از اختلال و اینها گذشت دیگه</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3440" target="_blank">📅 15:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3439">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">همچنین 104.18.139.67</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3439" target="_blank">📅 15:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3438">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خود آیپی 104.19.229.21 رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3438" target="_blank">📅 15:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3437">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خود آیپی
104.19.229.21
رو توی کانفیگ‌های معمولی BPB و کلودفلرتون تست کنید. یکی سری از دوستان میگن آیپی سفید شده</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3437" target="_blank">📅 14:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3436">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UyRmXsoZnI-r2je4YAyLoD5wgZEonZXiqKOlxfGTx-WPL_9uyjEKhQ4cESZs7yuwuPyYkYw0mWcy0HIKtHNNqjy4NJpuAKwszwZI7V7HSxS-i1MISI-UhSdKvqadCWqo-FzrBTY8urzUiqMnZecq0-QA6t1Lh9PY2aRg8p5rHLgNWFAn1zWRquS8yOuxgsKj2irR0O8lh7RsVqM8vU6iznLiltC74zYK38xGjNLdxpaNxrk4wyjz0o7mdA1BUrYJWUyMaJpnOYkLCWMUw4qKh9Agc2gP8Dys9RicpU3HFOXznnrBs6DbePjWxsttcZjr1vvPqwVFoYrbmoyY1uV46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کم کم داریم توی هرم مازلو اینترنت پیشرفت می‌کنیم:) از صبح دنبال اینم که بتونم یه راه ساده و رایگان برای گیم واستون پیدا کنم، اما متأسفانه فعلا فقط تونستم با پینگ ضعیف با ترکیب سایفون گوشی، گنشین ایمپکت رو بالا بیارم و بازی کنم</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3436" target="_blank">📅 13:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3435">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نمیدونم احساس منه یا واقعا این شکلیه اما انگار اختلالی که روی پهنای باند سرورهای ایران تأثیر می‌ذاشت خیلی کم‌رنگ شده از وقتی Spoof باز شده</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3435" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3434">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قول میدم اگر فردا و پس‌فردا اسپوف همچنان وصل بود، یه سری آموزش باحال داشته باشیم ازش. همینطور یه سری آموزش راجب چیز میزای برنامه‌نویسی و ستاپ کردن IDE ها و نصب کردن آفلاین اکستنشن‌های Ai و این قبیل موضوعات چون خیلی آسون با اسپوف میتونم واستون ویدئو ضبط و آپلود کنم و کارم هزار برابر راحتتره</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3434" target="_blank">📅 03:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OrPFlA1CGSkFeNLeg5DgJc7Y3Xdjjk3ZdCBP81Pf8MkFsogIUIRNzLcU_RgPiHJbPM4Q4XcBwPnTtvM0BuWjIACejl7X63rf4Z4RvVizvWkCKNpGC7zoNPcOnkSHCTgRqms5uwS0Rr_nYQKSNPCLnTkuNsoTI7ONrOpFQ_S4h2WxzDb5Gc10-O213nqk8pxQ2heGhadfH6caVxNK1lQtyyAhF89KgsVpkWjRawRhTAGMEIM8Nf0mFrnOt5-yg9rYWDU4eI_Xe5rbiuYgn1ja9ijRmWClj4kC29dCEoM4ma6SR26PFnT0au3E2YwIp13YngKl7NWvU3foxFQWAF1I5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/grhUBbewf9lZGV_n7YYkmMbIkbSfj9Y4YrTve3vsBVREmKNFBkBbQZ28l7KFcbAgwHNbRxpejJ0UNtVRvPrMjt9kJiK8ZpUPw5D1doYTyzBLV78lADpP2cISKGYwnfRUgojceXOgx5aShlLFyeSbFmypg7PgZhvL5c_wf6ai7kj7kQgsnayKm24-CKjkWZWvMXIeOHHahA0wjWzssjm2vm-2J_B3rYomOgFahECzUorIzbDQPi3VW__-VT_dnfHX7AcSJaUB8X7q-IkKmP-tD0u9OXS6GC1lw6kkd79a51z_RbuqZXSU_YUs27Mo0huJ2bdT3AlYeeHZSI-PmIVo_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پولی که قراره آمریکا آزاد کنه: 6 میلیارد دلار
ضرر قطع 80 روزه اینترنت طبق گفته خود دولت: 6.4 میلیارد دلار</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/MatinSenPaii/3432" target="_blank">📅 02:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدای تیراندازی سنگینی که در نزدیکی بندرعباس شنیده شد، پس از آن آغاز شد که سپاه پاسداران یک شناور را در دریا هدف قرار داد و در پی آن، جنگنده‌های آمریکایی قایق‌های تندروی نیروی دریایی سپاه را در خلیج [فارس] بمباران کردند.</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3431" target="_blank">📅 02:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نمی‌خوام دلسردتون کنم اما باز شدن Spoof روی فقط و فقط یک دامنه، به معنی اقدام برای سخت‌گیری "کمتر" نیست لزوما. مسئله اینجاست که فقط و فقط
hcaptcha.com
روی sni باز شده. مابقی سایت‌هایی که وجود داشتن برای ابتدای متود، هیچکدوم باز نشدن و الان ده تاشون رو تست کردم با config.json های مختلفشون.
اگر واقعا شل‌تر شده بودش، روی اونها هم باز میشد. بیشتر اینطور به نظر میرسه که دولت الان بهش نیاز داشته که بازش کرده و هروقت هم بخواد می‌بنده.
هرچند همین متدها، هزینه‌های بسیار گزاف روی دست دولت می‌ذاره. هم برای مجددا فیلتر کردن، هم برای خود فیلتر بودن این سایت‌های ضروری.</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3430" target="_blank">📅 02:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3429" target="_blank">📅 02:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انقدر چیز میز می‌خواستیم دانلود کنیم زمان قطعی، حالا که Spoof وصل شده دیگه یادمون رفته چی می‌خواستیم بگیریم</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3428" target="_blank">📅 01:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5dtKJ1IA1Fi6YN5-Ut4EiA8NthZoAJVQT5UAD5rC0wzuWu9gjz3WueJ8raLKO8w_Ry_w6oMr1hqv3D8bI20mIzCRGdGuODq4MA3GYrnypbJv23UMPvGi19Svb7dDTm3klfJlYGu23DBKbOjFgXqtT14spw-VVkPOF0oWxb-7LvtSDCF1zNScT2vLuxwVSiSDR0KeRD8qAyLAgw4rhXOOaufyfFzLgl1mIcERDIJkD2tiFYwxQwQsPtzt_enPK0yOkVcAP2dreX7p0ptnfvp-cZlinQBv_88em_TGYYTuSghf86G5qrbI7LidnhnpAiuT_YyXzSBJfrMR9WL2bTJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aleskxyz
:
واسه sni spoofing من یه اپ با go نوشتم که به جای اون template واسه client hello که توی کد اصلی هست، از utls استفاده میکنه که میتونه رفتار مرورگرهای مختلف رو تقلید کنه.
همچنین fragment و ارسال چندباره fake sni رو هم بهش اضافه کردم.
توی تست خودم واسه لینوکس و ویندوز کار میکنه ولی نمیدونم داخل ایران هم جواب میده یا نه.
اگه sni spoofing روی نت شما جواب میده، این رو هم تست کنید، هر دو نسخه‌اش رو. ببینید کار میکنه یا نه
از firefox واسه utls استفاده کنید. خیلیا مشکلشون حل شده:
-utls firefox
توی نسخه جدید (v0.3.0) میتونید کانفیگ رو داخل فایل config.ini بنویسید و بذارید کنار فایل exe رو فایل رو run a admin کنید. نمونه محتوای فایل:
listen =
127.0.0.1:40443
connect =
104.19.229.21:443
fake-sni = hcaptcha[.]com
utls = firefox
قبل از اینکه بخواید از این روش استفاده کنید، لازمه این دو تا شرط برقرار باشه.
اول اینکه لینک زیر برای شما بدون vpn باز بشه. اگر این لینک باز شد مقدار ip رو بخونید و یادداشت کنید:
hcaptcha.com/cdn-cgi/trace
‎
بعد این لینک رو باز کنید و ببینید ip داخل ایران شما چیه:
ipmyp.ir
‎
اگه هر دو این ip ها یکی بود، این روش احتمالا برای شما کار کنه وگرنه قطعا کار نمیکنه.
https://github.com/aleskxyz/SNI-Spoofing-Go</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3427" target="_blank">📅 22:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اما تنظیمات داخلی برنامه در این نسخه بر اساس آخرین نسخه MasterDNS ساخته شده و در تست‌های اولیه، از نظر سرعت، پایداری و مصرف حجم، عملکرد بهتری نسبت به نسخه‌های قبلی نشان داده است.</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3426" target="_blank">📅 22:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaKTldgBn-OVInKOrKtkh0L9JgevkZ8pmeNMA3HIvI5ovO-HHpUdcuPe6aqPibjaYPUWR41hd8fnYzpvFJJZrnml5OsaWzAnb93uLzLcSErQ7GEnJOthLN0YixUtawn3PgX700CpBTt8ZFRzvuB_2-0_X4MbyaL26oCwN0EnYzNxLxzOCj-EtnGVIpmQfy2VKVVRRxcx7CGB-iQYyxo4ee1UYbVA9uvMYj122b_TLeMbrFI8rr1b2ArX3VJqOmANbjX1N35pM0IuYaxx6rVKMWK8cj-1zWTG1lpfhcgpVOhYfqQ2pRhBcp3cFFmBeRxzcjW-NoEvaJzNVspIM3eq618I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaKTldgBn-OVInKOrKtkh0L9JgevkZ8pmeNMA3HIvI5ovO-HHpUdcuPe6aqPibjaYPUWR41hd8fnYzpvFJJZrnml5OsaWzAnb93uLzLcSErQ7GEnJOthLN0YixUtawn3PgX700CpBTt8ZFRzvuB_2-0_X4MbyaL26oCwN0EnYzNxLxzOCj-EtnGVIpmQfy2VKVVRRxcx7CGB-iQYyxo4ee1UYbVA9uvMYj122b_TLeMbrFI8rr1b2ArX3VJqOmANbjX1N35pM0IuYaxx6rVKMWK8cj-1zWTG1lpfhcgpVOhYfqQ2pRhBcp3cFFmBeRxzcjW-NoEvaJzNVspIM3eq618I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/MatinSenPaii/3425" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">☠️
رفع مشکلات رایج SNI Spoofing و آموزش تغییر لوکیشن هر کانفیگی به آمریکا
⚡️
لینک داخلی ویدئو: https://guardts.ir/f/00871d86ad44
⭐️
توی این ویدئو قدم به قدم مشکلات رایج SNI-Spoofing رو بهتون توضیح میدم و میگم که چه شکلی میتونید با ترکیبش با سایفون و یک سری…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3424" target="_blank">📅 16:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/itWlSLeyh7wnHP2evrzY0jUgN8H1H4NBiJTUV05mBf3-747oWDVB6S5ZfptdOBIhYT-0fb470TU7-AFM6NPvEYTs5HmeCQG4GUIHF_IMhHZARYIFYnV2ownVAqnUrBElvUx--V0SVjyo1WC5Jn49-w8ZjjTej4bJ3dNIWfAsKI1BB2X9GuQPs_2XxViKmTgsipiHEmKp3szmaM5B2h1BMNXGEwB4JxVFHYby1dXdth3wp1KYwLMA0Wb2YsL0r5izukT9pCDCH3ACwzpXKqRm3sp14Qy3vBtZeoRs3D3SlaciSLN5NvY0yP8SGp9oCiXdgOGNpSGzRE3EywkcAqLYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر این ارور رو میگیرید روی دسکتاپ،
۱- چند بار تست کنید و تلاش کنید برای اتصال
۲- گزینه Parallel test رو با تمامی گزینه‌ها بزنید تا شروع کنه به گشتن
۳- اگر باز هم نشد، یک بار MasterDns رو حذف و مجددا روی سرورتون نصب کنید و با تنظیمات اولیه‌ی خودش تلاش کنید برای اتصال. اینکریپشن و اینها رو تغییر ندید ترجیحا و دقت کنید که دامنه و اتصال و دستورات رو مو به مو مثل ویدئو انجام دادید</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3423" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وقتی می‌بینم یه سایتی که پیداش کرده بودم و توی یه ویدئو معرفی کرده بودم، توی آموزش‌هایی که بقیه می‌سازن هم استفاده میشه حال می‌کنم واقعا.
وقتی می‌بینم یکی یه پروژه‌ی خوب نوشته، خیلی خوشحال می‌شم از share کردنش.
وقتی می‌بینم یکی یه ویدئوی آموزشی خوب ساخته، لذت می‌برم از به اشتراک گذاشتنش
شخصیت من اینه. و حسادت، دورویی، دزدی، بدجنسی و رفتارها و صحبت‌های ناسالم و غیرانسانی توی کامیونیتی اینترنت آزاد جایی نداره
✌️</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3422" target="_blank">📅 14:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانفیگ ترکیبی متصل با تمامی نت‌ها
😎
بزنید بترکونید
❤️
آموزش اتصال ترکیبی
👉
ویتورای+سایفون</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3421" target="_blank">📅 14:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQbpzauootgamSUJh3nkJfjp7if5fJ-94LvIwTvUZjsoOVAe5V5izIMuXVjzhe8tAuW4dxxlZEXFz62OmTbFlNafisU_w6_fAGdun58qRA_XCnGFv6B_WFJ2Dj3z2omF9bfG6y-z0Ni5UyOb-BPq2KyYeC0XL5B7l1i_KN89hMe4YFYTks0sXHBjqAciHxc09Fp_FVeTrGBEZac7HPKOMj2IXSvqjZMbd_pZGqWWsqYpL533WNjCqdDEgb8q3lymRN7DxViz3N2Xv8IeD87QQff9ejoNPLU9dkMGhIiPo2BAUxiuNvJPPSnfY-riH10TtVSul3sCZ8yOGgyp9-lySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر وصل نشد، این خبر رو هفته‌ی بعد دوباره بخونید</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3420" target="_blank">📅 13:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه. پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/MatinSenPaii/3419" target="_blank">📅 11:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برای کدنویسی با هوش مصنوعی، به شخصه دیگه Antigravity گوگل رو توصیه نمی‌کنم به خاطر rate limit بسیار پایینش که با چند مرحله تا یک هفته شما رو محدود می‌کنه. حتی برای اشتراک Pro هم صادقه این قضیه.
پیشنهادم اینه که اولا اگر در توانتون نیست هزینه بدید، دوتا کار کنید. ۱- از Codex استفاده کنید که کمپانی Open AI توسعه‌اش داده و از مدل GPT 5.3 High برای دیرتر پر شدن rate limit استفاده کنید. مثل آنتی گرویتی هم دردسر تحریم و... نداره. فقط یه vpn می‌خواید که Chatgpt رو باز کنه عملا. اپلیکیشن هم داده برای ویندوز اما به عنوان Extension VsCode هم می‌تونید نصبش کنید. و محدودیتش هم سخاوتمندانه هستش و به صورت هفتگی هم صفر میشه. کما اینکه میتونید از ایمیل‌های متفاوت استفاده کنید و یه گفتگوی یکسان رو باهاش ادامه بدید!
۲- وسط کارهاتون هم می‌تونید از خود Ai Studio و مدل Gemini Pro به همراه گزینه‌های Google search و Url context با thinking budget بالا استفاده کنید.
اگر هم می‌تونید هزینه بدید، پلن‌های پولی Claude code و یا Cursor رو تهیه کنید. به مدل‌های چینی Kimi هم نگاهی داشته باشید.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/MatinSenPaii/3418" target="_blank">📅 10:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">متاسفانه دید همه به dns، کلا dnstt و ساعتها اسکن بی‌نتیجه و دنبال ریزالور تمیز گشتن و سرعت دو سه کیلوبایتیه. نمیدونن که من با همین WhiteDNS به راحتی میرم اینستاگرام و یوتوب و تیک‌تاک و...
چیزی که بهش دقت کردم، روی اینترنت‌های متفاوت نتیجه ممکنه زمین تا آسمون فرق کنه. در حدی که یکیش تلگرام به زور لود بشه، یکیش بشه به راحتی مثل قبل از دی‌ماه رفت اینستاگرام</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3417" target="_blank">📅 07:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u2GY7ksfV_-PdkTr5eOmwNq4bYEDAxMvq6W3JhyYptu6CGbfzpoSfNtCZg9SoZi1TinpwXUXGcfio03MsTSf7ZaJ8zPPijE6UU2_6AVorl-6lf1G_fivaEjSGtAzObUpl5RnoDvwhZEOUYm9gcaoSq9ihL0imU8KplQyv4aKB-L3su210-sKeEY73lf6Lg6qlvjMra4wbhdavhRO_m9h7ufE9VqAbo74uFhLx5zyBp9rY1mt2oR5MW7EfF-Q77MDbHkJJ2jA0RPXm8BUiXmXyLasCuWmTZ-IjfTde9MNyI_DUVS2E-V9KgPI6xG_EEYdu94QB-Sw352-_3Cw9bK5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه. اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/MatinSenPaii/3416" target="_blank">📅 06:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SxMyd6ix8R6I7I-LMKde2LeyBAyL6bPjMMJLz4Uxo7AR0QVjckM43STMrp6XEiKnG4nwXVoyVNCDn-Yd-lJ-Xvl58hCDTye30i138QOWGospHpIdz47G5C_Zff0vxZPf3en-s5bhcJIdF2YA-RHd1rU2GszrBHEueWwI2iysxFJokcqkfZacPIzKXqH1eZy8VWCLiv3_Kb9wANSqpjYpV11waV1sBD4chFC3TzJGu5BJ-8i-sv_a8kFzvuv9pMNuOM0U2P2mgdcrsx5tKK08W5eYOS2Dws2k1mNiD4SkAXtg1_qt6nvuDpt9XuA3ip4HKUJTUhHJfaSUJLdWvNwGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خارج از کشور هستید، برای خانوادتون نمی‌تونید V2ray کانفیگ کنید و بفرستید چون ارتباط از داخل به خارج و خارج به داخل قطعه.
اما به راحتی می‌تونید واسشون روی سرور مستر دی ان اس نصب کنید و همه‌شون رو با WhiteDNS وصل کنید. که برای شرایط ابتدای جنگ تا به الان کاملا پاسخگو بوده. اینم آموزشش:
https://t.me/MatinSenPaii/3372</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/MatinSenPaii/3415" target="_blank">📅 04:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pczkkZFHt36gMPwwjyzrQ0JiO6LELZ61FG5WbjrHh0dbH_KWYYbkJlc7grCwwodI1f9fsDSDn4B9SYSUiJunntDu4ri6ouQU4oPLNq3ghxGIaL1I2bl_lEbJ-1WOlr0syXPe08L_yxBORtproHfoVZE-xsbJCL8FG3is0d2cNeRt6g-BcNQhOW-Qv57jQEpyd0w-S1gLpsmJ2MTG5wx7056OKDZc53bTEWWQB7fqFA8yUgB9mblaYhDbwV2GiPQCTotDPmyEK8WrnCbhAP8RkRUigLcM12Vg3tzxC2bvKyvpsOqmYmI5M6muxib0HZ-IXB58v-yCQoYwfQowrIhT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچنان SNI وصل هستش
گزارشاتی دادن بچه‌ها که براشون کانفیگا پینک میده و کار نمی‌کنه، که خب باید بگم اختلال از سمت اپراتوره. یعنی شما دو بار پشت هم پینگ بگیری، بار اول پینگ میده بار دوم پینگ نمیده‌. در این حد هستش روی بعضی اینترنت‌ها
اما خلاصه تا وصل هست، استفاده کنید</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3414" target="_blank">📅 03:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmtbgt5QJFcZu79KsobnV_-QsgFRYRXUpCVMmGpmmkmZMVCbUfsF6um8jWTHoVkKDdzfD-nS2Q1HDebmU9C0MhN_ln11hpYgmIn3gug5onYL14isMOcdrD1ksOY32hKDa85giKwF6nD_rP6NW-b0xzA3e74y-c6v3tVbK--E2aDJcmWc-B0CDzmIzYqR06qZ15g9-D6gB0tbS83QfMQiLOH5TMXxIKSLs-XB31nXSCEn61h2Grfn_8iQ6XWXh3pfCwOW8NxDU0MshgI-3Y3_BTazCFcqvCJqXAQEgEdPGI2Tv-DjB2J4jF_8oCdDD5vPNETSmqGY-101YVfNQhjuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی آدما انقدر خودخواه و بی‌شعورن که انتظار دارن کل کار و زندگیت رو ول کنی، و تک تک ۱۵۰۰ تا پیامی که روزانه می‌گیری رو بشینی جواب بدی.</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3413" target="_blank">📅 03:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3412" target="_blank">📅 21:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">برای SNI SPOOFING روی Mac می‌تونید از پروژه‌ی خوب Cloak استفاده کنید:
https://github.com/g3ntrix/Cloak</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/MatinSenPaii/3411" target="_blank">📅 20:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گویا پولی که از صرافی‌های ایرانی میاد رو بلوکه می‌کنه کلا. حتی از Trust wallet هم ممکنه این بلا سرش بیاد. ترجیحا از این سایت نگیرید اصلا</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3410" target="_blank">📅 20:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/MatinSenPaii/3409" target="_blank">📅 19:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3407">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3407" target="_blank">📅 19:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3406">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">زبان‌های مختلف برنامه‌نویسی، هر کدوم قاعده و قانون خودشون رو دارن و به درد یه جایی می‌خورن، اما یکی از پارامترهایی که می‌تونیم اونها رو بر اساسش مقایسه کنیم، «کامپایلری» بودن یا «مُفَسِّری» بودن(از تفسیر میاد) اون زبان هستش.
۱- زبان کامپایلری (Compiled) چیه؟
توی این زبان‌ها، قبل از اینکه برنامه اجرا بشه، کل کد به زبان ماشین(کد باینری) تبدیل می‌شه. این کار توسط کامپایلر انجام می‌شه. این که ماهیت کامپایلر چی هستش، بماند.
مزایا:
۱- سرعت اجرای خیلی بالا
۲- اکثر خطاها قبل از اجرای خود نرم‌افزار پیدا می‌شن (Compile-time error)
۳- پرفرمنس بهتر
﻿
معایب:
- باینری تولید شده معمولاً فقط روی یه سیستم‌عامل و معماری خاص (مثلاً Windows x64) اجرا می‌شه. و برای پشتیبانی از پلتفرم‌های مختلف باید کراس‌کامپایل کنیم که پیچیده هست و دردسرهای خودش رو داره.
۲- تغییر کد و تست دوباره سخته (باید دوباره کامپایل بشه)
مثال‌های معروف:
زبان C --> سیستم‌عامل، بازی‌سازی
زبان C++ --> بازی‌سازی (با انجین Unreal Engine)، نرم‌افزارهای سنگین
زبان Rust --> سیستم‌های امن(به خاطر مموری سیفتی) و سریع (در حال رشد و توی هایپ شدید)
زبان Go(گولَنگ) --> بک‌اندهای Scalable(مقیاس‌پذیر)، میکروسرویس‌ها
زبان Swift --> اپلیکیشن‌های مک و iOS
۲. زبان مفسری (Interpreted) چیه؟
کد خط به خط، موقع اجرا ترجمه و اجرا می‌شه. نیازی به کامپایل قبلی نداره.
مزایا:
۱- توسعه‌ی نسبتاً سریع‌تر (تغییر رو میدی، فوری اجرا می‌کنی)
۲- یه سری به عنوان مزایا می‌گن خوندن کد راحت‌تره که من قبول ندارم اصلا
۳- در کل Portablity بهتری دارن. هرچند شما عموما مجبوری سورس کد رو کامل تحویل بدی چون نرم‌افزارت همونه!
معایب:
۱- سرعت اجرای پایین‌تر (چون هر بار باید ترجمه بشه)
۲- مصرف منابع بیشتر
۳- خطاهای سینتکس و DataType، معمولاً زمان اجرا (Runtime) تشخیص داده می‌شن، در حالی که توی زبان‌های کامپایلری، خیلی از این خطاها زمان کامپایل گرفته می‌شن. این موضوع برای پروژه‌هایی که با این زبان‌ها نوشته شدن، باعث می‌شه دیباگینگ پیچیده‌تر بشه.
مثال‌های معروف:
زبان Python --> هوش مصنوعی، مهندسی داده، اسکریپت‌نویسی(ابزارهای قدرتمندی داره)، وب (Django/FastAPI)
زبان JavaScript --> فرانت‌اند وب (بک‌اند با Node.js و فرانت)
زبان Ruby --> وب (Ruby on Rails)
زبان PHP --> وب (WordPress و لاراول)
(هرچند جاوااسکریپت و php رو دیگه نمیشه کاملا مفسری دونست. به خاطر JIT Compilation که بعدا توضیح می‌دم)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3406" target="_blank">📅 19:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3405">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4659a46672.webm?token=V18tPNBkomj6DeUg-qU8EqYGaNkwFOhW5DWkOzpxkND3oXZnOoMugMHw3i8yYttdSKZv4e6qKyaY2iOoJAmLt-lZrwiuwlUbtvJsKbgPXKxDrNRdKQPWredcvukCHxWcZn8UwP_yHmKkTVpFmZmqB9gS1Gk60fG_lQ0Wf9RN6B9rki4dmdEqLNCG4uhF90MH7L4VR0c2D93Z_tjJoZ2pWzGUsRSsuReNB0UN3lMExofmR904Hm4EuTB7OdxTLKHjPsgCdMM6n4tsVUqRuG9xEyOjEczexxY81g_qsL6tnA_sOjbTNgyhw_L9OSg0t2izhm5dVrjo_Y7r5HOHPFX3KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4659a46672.webm?token=V18tPNBkomj6DeUg-qU8EqYGaNkwFOhW5DWkOzpxkND3oXZnOoMugMHw3i8yYttdSKZv4e6qKyaY2iOoJAmLt-lZrwiuwlUbtvJsKbgPXKxDrNRdKQPWredcvukCHxWcZn8UwP_yHmKkTVpFmZmqB9gS1Gk60fG_lQ0Wf9RN6B9rki4dmdEqLNCG4uhF90MH7L4VR0c2D93Z_tjJoZ2pWzGUsRSsuReNB0UN3lMExofmR904Hm4EuTB7OdxTLKHjPsgCdMM6n4tsVUqRuG9xEyOjEczexxY81g_qsL6tnA_sOjbTNgyhw_L9OSg0t2izhm5dVrjo_Y7r5HOHPFX3KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/MatinSenPaii/3405" target="_blank">📅 15:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3404">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">⭐️
کمی مرتب کردن مطالب برای دسترسی به اینترنت آزاد با SNI-Spoof:
1- آموزش پایه:
https://t.me/MatinSenPaii/2627
2- آموزش پایه رو که دیدید، بفرمایید از این json استفاده کنید:
https://t.me/MatinSenPaii/3168
3- و کانفیگ‌های این پست:
https://t.me/MatinSenPaii/3183
ترجیحا با ایرانسل یا سامانتل
4- سؤالات متداول راجب این متود:
https://t.me/MatinSenPaii/3189
و تبریک میگم! شما به اینترنت آزاد دسترسی دارید.</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/MatinSenPaii/3404" target="_blank">📅 14:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اسپوف روی یه سری از اپراتورها برگشت. هرچند با وضعیت دیروز، و گزارش یک سری از دوستان توییتر، اختلال شدیدی انداختن و در تلاشن برای یه سری CDNها بدون اینکه مردم بتونن تانل بزنن، دسترسی خارج باز کنن. که احتمالا سر همینه این وضعیت:
{
"LISTEN_HOST": "
0.0.0.0
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
104.19.229.21
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
hcaptcha.com
"
}
﻿</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/MatinSenPaii/3403" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">توی دایرکت چنل یکی داره میگه شیر و خورشید جدیده زیر پنج ثانیه وصل میشه، یکی میگه دو ساعت هم شده و وصل نشده.
به نظرم باید بذارید حالت هواپیما و با rangeهای متفاوت تست کنید. انقدر زیاد منتظر موندن هم دیگه فایده‌ای نداره.</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/MatinSenPaii/3402" target="_blank">📅 14:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3400">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیم ساعت تا یک ساعت شنیدم بچه‌ها گذاشتن تا وصل شده.
اما طبق گفته‌ی برنامه‌نویس پروژه، خوبیش اینه که بعد از اون دیگه نیازی نیست انقدر منتظر بمونید و به همون آیپی تمیزی که برای شما پیدا کرده وصل میشه
خلاصه که اگر گوشی بیکار دارید، بذاریدش سر کار</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3400" target="_blank">📅 12:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3399">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.24.apk</div>
  <div class="tg-doc-extra">25 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3399" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3399" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3395">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکلاینت شیر و خورشید</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FRNCjFaKuxIOZwqThWszPS7SxOdlGow6bpNANe7kymZAvg-dCVj6ci1eOrSPF_1aOW9YMUTUHOV1kRSu7-WxSvJylXXgV3LFo4u-r7OG1tymtjmcq7UgLZU0xedFyR7eqarmjE8U-J60S8grZQrNbSvyqsw5yW_IN-qXYhxNssdP2wZkVDltKeKZrYqyhj5TzAes0saShMVbBW0aojEZfYHkc-YcSfcW985xgy8uzMM805B3HuZlVW11a455SOY3nT2L5PJOPUGCNfT5jfvktDofA5RLT2Fg6NcmB4uMM6aBdU0VY5bKR6uI97epB2aplCvzVwjocSF34pCsU80lsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rVk8Fo_GywAUvMGMMgEcx4p31ppVQxp8m5Qz36nRZOFS2aNQH3jh6ynxEDEzqp7gvbYAWDJseviNCE0eKhf9SkFZvA-_UkvHjd38Pd4HTZh7-RAGV8XWB3UZ826nOuH629jtRco4hz-yjQGo2x09ipTtwPcPTOE0waXm1l_lydoVL7jITok3Xn6trTBpXDt5Xj2Zmia42SWpM1LH6K1NjINfgD3h3WTBy2CWdE5v1ZcmG805fdk-VdQlsM2-_3feYaJcBATGZyYiu9LbFoj_zJjt7_gzmX9qmDlBYeKikRxI25x9tU-EBmdY3b1mgJy6HuL_0q32QFG9xlKmoxs4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RgzM1ZaC767jH8c8vLoFuqEx-tCxnwZlU6g5L6GfxdjXqOVgaVioV_14s-lC17rtzLtfzFiPoQ_E0Yq_wFR4bRmizh-kY8ceU9_P1UpdXHFuABrnsfv5K_7uLj1_3zECpujUdTAISLT4jE8S-jwDCIvLYaDUeMAQ1k8Ta37FlN_4MVPbiZjy5UfMQ7ja7RrmaqD6wi9k7TEkslIz1BsMsYg9zwOYGpV7ogI_e3bHZM68nfZ9o00UouTobLoN4ZubJcvVtLvHlojcKV_mnSVlhvhWC4q_UMCwTYWxDHbZolIo1QkM1VodfV_FwplaUBoWiHyIRDMHTAYTUXwGcyTUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W1zd1zhAzuhlOLgcDtQGVyzC01z6OFaZudSmrcSuaAaw89CPZrsxq7Gn3xdf0nMtCJTy5I8il-tj719SF1KEwus_mlb1TUwvSulwsXKmbp5qmfxTBCsWFKomupQs4ksmUMBWTQgo_ESCjvMpb5gqimZi-s4dHRjZ-RFNv_iIF5sCM31i2zd64yxHgery5SvbjNJhnZCh5Nrzpw6VD1HvzC2aKhW4QNWovkaJ9SLQA8_cBAFm3M3Y_TVndNW6PbTtdVHvcJGrG-aKISBUhXvaieGjGdPNyLm4Ka4jXLFSMj2qprpbeLEJalktuF1Ks_QqXgouMP4SJQS5OPzjceQxow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید کلاینت شیر و خورشید 2026.05.24:
- آپدیت Beast Mode برای درست کار کردن روی CDN Fronting
- اضافه شدن اسکنر ای‌پی. برنامه لیست خیلی بزرگی از ای‌پی های ممکن را داره٬ پس اگر در اتصال مشکلی دارید پیشنهاد میکنم تنظیمات قدیمی ای‌پی ها و SNI رو از قسمت settings برنامه حذف کنید (خالی باشه)‌ و اجازه بدید برنامه خودش کار رو انجام بده. دقت کنید ممکن هست بار اول خیلی طول بکشه٬ حتی چند ساعت!
- اضافه شدن پروتکل های بیشتری که با CDN Fronting کار میکنند. احتمال اتصالتون و سرعت باید یکمی بهتر باشه الان
- قابلیت غیر فعال کردن سایتی که زمان اتصال٬ سایفون باز میکنه!
- قابلیت تنظیم پورت مورد نظر خودتون برای LAN Proxy ها.
- قابلیت تنظیم username و password مورد نظر خودتون برای LAN Proxy ها. این تنظیم دلخواه است و اگر تنظیم کنید فقط با این username و password در شبکه خانگی میتونن به شما وصل بشوند.
- آپدیت شدن هسته سایفون
میتونید از اینجا دانلود و نصب کنید و ممنون میشم اگه به اشتراک بگذارید که تعداد بیشتری ببینند:
https://github.com/shirokhorshid/shirokhorshid-android/releases/tag/v2026.05.24-a3b91cf</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3395" target="_blank">📅 10:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3392">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iCM9SqPZbmLWrIUFtrKAl2DL446e6tY0S9GWdWbJmag4I9mTzqobBdfTNuoBLJTvptJMjoxTYOYI-vZ9wd0sMCk5JSnaIOFEocP8wb0Tt0KcIZXmrEZJg-AUP6jKnYOITy6JziaxHo8XN5xoMs2XnVtoVoqCLJeC9KwotreDTYIi_AVk0GR9MFbEFx2bsXyTbDP1bCPv9a5N3Lifvr_MMzDQgLjHzeo9kmTNBwWT_hGmzjHg9exAcn6crunCwiNdxcMkql6IjFrsNcPKj1PiGE41J6W8fN_2zYtLTGVSa4FBFPMR1c_vg2dlIUpCf3P1Diz_OBlnMzCh_S57PkEfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو: https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو: https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/3392" target="_blank">📅 09:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3391">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه همراهان عزیز
ویدیو آموزش ساخت سرور شخصی که متین عزیز تهیه کردند دقیق همه مسایل رو ‌توضیح‌ میده.
تنها‌ نکته‌ای که باید اشاره کنم، متین از ترمینال برای وارد کردن دستورات و نصب MasterDNS استفاده کرده.
من پیشنهاد میکنم برای راحتی کار شما، بعد از خرید دامنه و اتصال DNS از ربات
@WhiteDNS_installer_bot
استفاده کنید.
اگر از این‌ ربات استفاده کنید، فقط با پروکسی کردن تلگرام‌ میتونید سرور خودتون رو مدیریت کنید و در شرایط بحرانی فقط از طریق تلگرام همه چیز رو مدیریت بکنید.
ممنون
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3391" target="_blank">📅 09:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3390">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اما تا ۵۰-۶۰ گیگ روزانه نباید موردی داشته باشه. سرور رایگان هم خواستید از سرورهای کانال مسیر سفید می‌تونید استفاده کنید ولی خب تفاوت سرعت رو توضیح دادم توی ویدئو که به چه شکلی هستش:
https://t.me/Masir_Sefid</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/3390" target="_blank">📅 08:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvH073OBPWbPbzrAe3bdweSwr2qjlQ5KrhxthVsu4LMqoJviOTt8y-NQTsUKqDlJoUYZeArPmTORc_kTQO1XqLHIuCmvN_VYF5sddIGcdwv6nyvymZPF8m-Prcdy1I78ld4CQ7P8paRIgqvqkp64g1ewJUrHo0fkastjSFZf_zMw0f1gvd30TgiBB49jkLy7a_6XaJ7AYD2ozjyidXPK56ezH8XQXxIJvhSJEX6q45r2GxbwxKtV9ax-rEjkx6HPoob2Njz2wqmzDfECy4MlJyIl7jcUN2aVZoRvv-mLAxU5Yh3UFCfrMzpDOIzHaKiMQArM0_1Fu2NZJ0sYGpUH3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ حجم دقیقی وجود نداره عزیزان. اما از چند ده گیگ متفاوته تا ترابایت حتی
گاهی اوقات فیلتر شدنه کاملا شانسیه متاسفانه</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3389" target="_blank">📅 08:02 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3387">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ProxifierSetup.exe</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3387" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این هم پروکسیفایر و یه لیست از Activision Key های مادام‌العمرش (برای مک و ویندوز)</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3387" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3382">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه Universal اندروید لینک داخلی:
https://up.theazizi.ir/download.php?t=e8a7a62516394e4aecbd26ca36dbb113e0aa</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3382" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta3-linux-amd64.deb</div>
  <div class="tg-doc-extra">17.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه ویندوز X64 لینک داخلی:
https://up.theazizi.ir/download.php?t=4b31fefbad0c08f180216f8e4c1eecc316d7
نسخه لینوکس amd64 Debian لینک داخلی:
https://up.theazizi.ir/download.php?t=bb6cfd1d86d4ed7a1826a4850b901ed46c58
نسخه مک amd64 لینک داخلی:
https://up.theazizi.ir/download.php?t=acbf869993172d51c2286fc812931ef48fd4</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/MatinSenPaii/3374" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Master-White-DNS-@MatinSenPaii.zip</div>
  <div class="tg-doc-extra">25.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3373" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">حاوی فایل دستورات سرور
فایل لینک تمامی سایت‌ها
فایل 5800 ریزالور جمع‌آوری شده توسط بنده از سرتاسر تلگرام
لینک داخلی:
https://up.theazizi.ir/download.php?t=b9162802b5da63cf5b39b02133170f4ad2bf</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3373" target="_blank">📅 03:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">☠️
آموزش کامل راه اندازی MasterDNS و استفاده از WhiteDNS ویندوز و اندروید
⚡️
لینک داخلی ویدئو:
https://up.theazizi.ir/download.php?t=7c97d6d4997fe6ad02da91e2b5381ff779e6
⚡️
فایل‌های استفاده شده در ویدئو:
https://t.me/MatinSenPaii/3373
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- خرید دامنه و سرور ارزان با کریپتو(+آموزش)
2- تانل کردن ترمینال با Proxifier و ssh زدن با خود ترمینال
3- تنظیم دامنه در کلودفلر و راه‌اندازی ساده‌ی سرور MasterDNS
4- استفاده از سرور MasterDNS در کلاینت های ویندوز و اندروید WhiteDNS
5- توضیح استفاده از Parallel Testing در WhiteDNS
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به خریداری یک عدد سرور لینوکسی و دامنه داره(مجموعا 5 دلار نزدیک به 800 هزار تومان) کافی برای اتصال نزدیک به 5 نفر
کانال مستر دی ان اس:
1-
https://t.me/masterdnsvpn
گروهشون:
2-
https://t.me/MasterDnsVPNGroup
کانال وایت دی ان اس:
1-
https://t.me/whitedns
گروهشون:
2-
https://t.me/whitedns_group
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/MatinSenPaii/3372" target="_blank">📅 03:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UCUt5tADdd6db443Zx6oZPfaPS2EOt4JUAawePLeoeZegyuV0lvT6HkSbRbBdBuEbXGlw1vbMpskLvAbG_em2Nv2AqYSmapd-K_rWsuE77vUzm22hkQSYeleRPg8iG5NvmbLlHpnWdjTgnCbxIRYHGi1EN-ZOKs3K3dEmlSjsdGClm20CoaOzI1RTdupOyjCjWY9Fl1eXlW6NDApXH5bYUSZTXF6Gkp8JeUmigdbEJlbZFt7OSXS21MfuLoYDGGnoZPdOlKaUmLHCJdWtHSy77O-fIXSJnHuktUl9_dcDLfOUaSwoAI-td2oIuvYp0dPulZz6jKqnnbCu9OQf1qfbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدرام وقتی
یه پروژه جدید
میزنه و مردم میریزن سرش هی سؤال میپرسن ازش:</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/MatinSenPaii/3352" target="_blank">📅 22:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3351">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آموزش بعد از یک ساعت و نیم تایم نفس‌گیر تموم شد ضبطش(خودش شاید اخرش نیم ساعت بشه اما مشکلات فنی‌ای پیش اومد اواسطش که متأسفانه باعث شد طول بکشه اما در عوض خیلی کامل و جامع شد)
نیم ساعت دیگه میرم برای ادیت، تا ۲-۳ صبح ایشالا حاضر میشه
با تشکر از همه‌ی بچه‌های گل تیم وایت دی‌ان‌اس و مستر دی‌ان‌اس</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3351" target="_blank">📅 22:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3350">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">Matin SenPai
pinned «
ببینید همراه اول میتونید وصل بشید؟  {   "LISTEN_HOST": "127.0.0.1",   "LISTEN_PORT": 40443,   "CONNECT_IP": "85.9.112.219",    "CONNECT_PORT": 443,   "FAKE_SNI": "www.hcaptcha.com" }
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3350" target="_blank">📅 19:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3349">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqJVptADd6pO-3ZiNOBn6JaT6Amhi9i5K2SAGKludjOhYOYIDejg78NQATaz17-g_NYc7Ub6gZfAXunES0lbY7ibDv7GIwDwmSeqH2yOOV8ZCjb6G5U5u2RvLSwsAYJ_lTdsnpxy1C9tUlRwHjNIJ22ibCZeTQgPa-L_JN8oE2dc20Vvdg8J_gOyB3TjFfR2sL4x38eaM7h05n8ImFiJo3ZdFaRxDromyNg5krQ-H2xw6g35h65Imiew7n1pCHHMASKEE-VacETa6G4yCeFMtXOkR9DTBhhm621fCXp9-VIH_wKAcalIowbv-B3LWT86ewVlZYJmr-04ivkbLYS0SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متد مستر دی‌ان‌اس که توی WhiteDNS ازش استفاده می‌کنیم، مبتنی بر DNS و برای شرایطی که گوگل هم قطع هستش. لطفا انتظارتون رو ازش بالا نبرید در حد دانلود و پینگ پایین و...
بهش به چشم برادر ارتقا یافته‌ی dnstt نگاه کنید. که نیازی نیست در به در دنبال تک تک ریزالور بگردید واسش.
و یک متد اضطراری هستش هرچی نباشه. شاید بهترین کارت و برگ برنده‌ی اضطراری ما باشه، اما همچنان اضطراریه.
برای شرایط الآن، شاید Goose یا Skirk یا Mhr برای شما بهتر جواب بده. به این دقت کنید لطفا. Dns برای خاموشیِ مطلقه.
پینگ و سرعتش نوسان داره، اما مقابل خاموشی‌ای که هفته‌ی اول جنگ تجربه کردیم؟
بهشته عملا.</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3349" target="_blank">📅 18:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3347">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BiiEQ11BQ6bnmeUBtASFIEzAF9g8OmF3BJXVQ1Rgl-ovdijPtDnEycqpFNpS7rbMBGua5YNEyDNAqI805IS2IqCRnxOm5uWE-vrGIGKbxGKsNlca4jv3e7tn7w9ApmiumQ_6MS-8PyjCRvEfw0f2m0U6qvHimi973vA96aOjgg8rdcFAjMj4v-7Sp6XN0vnzxSbJWJpvJWgsuy6r1ztVmDsJmqcirJvApsLhaMm5pc2QtQwb72ADqdsynOrxbUD6VjMXShEo15UqLjl8ib-BHB7TwkfnZkG0ZYaJCKYJw-iHqIaNBOPKIE5tjrOs0bdK4HFXBGJ82uYpZ-Y7iQ68-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ECiEm5CkhElEzeJ31OatOBg8rxmr_5UD8H0lGl3LaBI5m6fpatfBeagnf6VT_BX7BAD7t-INhYR7VB6CbvMZ7qaLYrz7lyG44AwMtcwmtbSDD9Uwi07aQxDCuPY7kbz4sS3OagwfF0ClImy5gg7IjszCJH7UohQbVpTkvrwR4dQU_mOxn5wMknT2SpLA7b3lPFWfg59hVEnN_e7tt_R2n5PJAMe8NLt4Y_s3WZT9ERnpOOQzvaLviVRERa0aSudl1QksNiV5HZhtFNOfhWpPTiHNlvjwm8KiPKA5hFmuMj335OO-LMhjoci2egcEpBNsQ5D92ApFz9oanZO5dSyetA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حدودا ۳۰ به ۷۰ انگار وصله توی یه سری مناطق
هم همراه اول شنیدم هم ایرانسل</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3347" target="_blank">📅 18:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3346">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V3-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">7.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3346" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 40 تایی کانفیگ‌های ویژه‌ی متد SNI-Spoof که از سرتاسر تلگرام جمع‌آوری شده و همه هم پینگ میدن</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3346" target="_blank">📅 18:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3345">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ببینید همراه اول میتونید وصل بشید؟
{
"LISTEN_HOST": "
127.0.0.1
",
"LISTEN_PORT": 40443,
"CONNECT_IP": "
85.9.112.219
",
"CONNECT_PORT": 443,
"FAKE_SNI": "
www.hcaptcha.com
"
}</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/MatinSenPaii/3345" target="_blank">📅 18:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3343">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UfxWdM9XeeGgV7Z1kvjhqm82xl98eG1Rp1Anlgh6n2qbEjlkSAV_RmGVCnXlID7ykhlUEpKcAfJjgas495GniC_s36QTmk6KmHtpKM6SE1ZiJXjgdzgDk2MhEp7Kf6mUIrhPkJy9M0chdbyT1pbQFDKoGVyPS-Vm1oaMr5dMYxgi2nciGaZK86FWUSM4GnUTYh1MoFQ0-gwbmlfR4H-mj55u8MrbVtzUfnjEtMeQpYwCAjhXY7ykf_xWChZ9QRRgkMjwJwh723auy1i3DhtDac3364075ZcQZ8BjvftbgBpJWU1vbh6OFCN7wrSVbH3_gITVovqUbN7PhGf--N6j8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت خوب برای خرید سرور با رمز ارز بهتون معرفی میکنم که قیمتش حدودا فکر کنم 4 دلار بیفته با کارمزد و اینها، و میگم که چه شکلی با صرافی‌ها کار کنید و از طریق چه ارزی بخرید.
منتها نکته‌ی مهم اینه که تصور شما اشتباهه از بسته بودن دیجیتال اوشن.
دوست من الان همه چیز بسته‌ست. همه چیز
و اگر چیزی باز بود که دیگه از DNS استفاده نمیکردیم.
پس بله، شما اگر VPS بیکار داشته باشید، میتونید این رو ستاپ کنید. دوستان خارج از کشور هم میتونن واستون ستاپ کنن طبق آموزش اگر که حوصله کنن. هرچند برای تعداد بالای 255 تا، قوی‌ترین سرور هم جوابگو نیست که خب این رو هم مجددا توضیح میدم که چه کار کنید. فلگ شدن دامنه هم توسط کلودفلر و هم توسط DPI ایران رو هم همینطور</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3343" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3342">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/li27N-s0jDY0EHhshcSNWNYLQeyFsVdfOCaUjiLa17VzhvV2ao1wyWVYxBNIEu1TNC5H9gDjv9saI_t-WycEKoNFlJpYDtFaAm5SNeFKHevMwH3uR_pmQyktT2CtVx2ZrEZq8trNySHSxq3ng939tlB1MuFd8PkRrr10SYXCgneaq_XpxGRZkeY0Ee8GVWndUV_MfOWSZTCoSXIoI-FMW-9P6U47DNbHsdWkKDsvx1CU0QehXUaIUByNQaqhy0o-24tOmfesDuIFld93bjB3FyKmUFWhhnPHUbemrV-k93_oqLIrwV7V7PVMuHwYJmbTb3YrKsxbvx_TtNCnrMM5ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصلا آموزش "برای" سرور شخصی هستش. و برای ios هم تنظیمات به همین شکله چیز متفاوتی نداره. خودم آیفونی ندارم که بشه روش یاد داد متاسفانه اما طبق آموزش پیش برید، همین مسیره</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/MatinSenPaii/3342" target="_blank">📅 16:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3341">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YeIU4_rYXU9LHh_9CFC4eKZGFwcMpxhRIu52laagen3KRA-Hj_O9KaUB8XoGQVaQ0GjYLkQinpzzGT46Ciu7ZxV3VqIsBVraiF7rhwKa2aeJlqmyvFM2ZCQlOCsGm7iyrT5XYhYbWXFwqwSr5crwetxazQqjgulLJRUd8vNaXa-E634Fi-XpcPN2lQj_ef5zuSudP2LXbiY2rJ-5aAPIcWYtg-7hvDQpTerybr91UXAEa-8-1EGE-PtDcES0LKW_Q2eysIw5keEOU_BQF5B27f4CJY0s0WE8tMeSAMF7XEh1zo8ModlYVWtrM3ZKbpR0th3a4vwqDmIvNDAbjsIWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ترفند جذب مخاطب نیست واقعا:)) بلکه هیجان خودم از متدیه که به شدت خفنه و میتونه ما رو نجات بده توی شرایط خاموشی مطلق
خیلیا پرسیدن که چطوری داری این سرعت رو میگیری؟ مگه میشه اصلا؟
بله میشه و توی ویدئویی  که تا شب می‌ذارمش 2-3 تا علتی که باعث میشده شما سرعت خوبی نگیرید و کندی تجربه کنید رو بهتون میگم</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/MatinSenPaii/3341" target="_blank">📅 16:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3340">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=idoQ8AEL3YejEiZZjD8xVMs6vCo4cSj2szskucS3iBvbBxX-MnNN4f_sxafpKsFWVgZA1ScQ-bryGDTF0TSHxQHh-3gHV5HzNRdL95OrXaR8LjsGz23pH3GVnLDE1oudoLU2wtDYug9RhyIj3ai0TYpmnqDEwmqgHQyO4uwRZ1nMtHL1wWWr-pxHapIUHTjv_L-apbWVCnp-Jz1uXLdtU5Sug3DTGAMIV8mbrtWpPGICKKtdVlMSMhQyX5AcYSTltwvTxvcPOa1gvK8sZgzppMRuQ82u46NDIHMtNHj-k3WgcrTDMOBxCS1AjvqTQNR35GtSo-xUirf1LJio0s9dEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ebddd60447.mp4?token=idoQ8AEL3YejEiZZjD8xVMs6vCo4cSj2szskucS3iBvbBxX-MnNN4f_sxafpKsFWVgZA1ScQ-bryGDTF0TSHxQHh-3gHV5HzNRdL95OrXaR8LjsGz23pH3GVnLDE1oudoLU2wtDYug9RhyIj3ai0TYpmnqDEwmqgHQyO4uwRZ1nMtHL1wWWr-pxHapIUHTjv_L-apbWVCnp-Jz1uXLdtU5Sug3DTGAMIV8mbrtWpPGICKKtdVlMSMhQyX5AcYSTltwvTxvcPOa1gvK8sZgzppMRuQ82u46NDIHMtNHj-k3WgcrTDMOBxCS1AjvqTQNR35GtSo-xUirf1LJio0s9dEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حقیقتا به نظرم سرعت Master+White برای شرایطی که جنگ بود و هیچ چیزی جز DNS و کانفیگ گیگی خدا تومن کار نمیکرد، مقابل مابقی روش‌های DNS مثل Dnstt و slipstream خیلی خیلی بهتره. کما اینکه نیازی نیست در به در دنبال ریزالور بگردید به اون صورت. نیاز به اسکن و... هم که ندارید</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/3340" target="_blank">📅 16:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3339">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uxgB__cuMwnfRnLm24hH9v3T9HVVAZlSFf_zo2uifaVtu6xlZNeDLxZte87HQIziGSDPuX-7i88X2zsTsln3ktaVRpKm1aDUumMFifuCB0VwrCCWtJ1cEI9iiAAXn0RStja5C6iCTLAMv0orZ00vmLnRrUZ4VrtGAnJHAbfSavo3R2ic90oK4TPwEoYJ-88_e1iTWQJwI98xGEbcy8hCeJQVccyMZ_2YL3_S2qy4K-F2e3xNtS215kgCZuYS5vOOHkTD7id3Hu7Wv1eupOXMIubUPjUHssIr67jriX9PWjGBCRTBa16sutCUQOcq7KyWorUsakBP-HJHELq9no5O4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نزدیک به یک ساعته وصلم، کلا 100 مگ رفته
اینم برای اونایی که از ورژنای قدیمی میترسیدن که یهو دو دقیقه 200 مگ میرفت</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/MatinSenPaii/3339" target="_blank">📅 15:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3338">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از MHR و Goose relay واقعا لذت‌بخش تره</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/3338" target="_blank">📅 15:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3337">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این عکس‌ها و پست و همه چیز رو هم دارم الان با همین متد ارسال میکنم</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3337" target="_blank">📅 15:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3336">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.   با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم  به شدت ساده‌ست و بچه‌های تیم…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3336" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3334">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AfXEKwSUk8kcTyim9yPY8nAjWHQ6r9L-vW06KtSlty6-R_6Mu5K3KjUUc_v8LMXGxfAGrLchDKZ24ym-0gG8Ov1VrI_dwmHu5sO1KhwLDtFwDhIRSJyXc06VtEGb3rd3TEpDR7u8s7zR1LHIodB7m3bLLRMrFAhJqxTaDyLQ7v7VWUpcizO2skMBxcUVs_hKlHXUaGo3LntjEi5cZJg7VRxCiOcGFbdhA9APoodJksnhj6qPCdh78Sj1qJweUMbxw-psk7ezhBuO_oODtChh_PpSjAHaRIEcFj4XQ1JNOsg1gOlrjzOjYKzSedQne1R5_8EiJoG8DkncPT4nNp0kEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IrPJ3Sk6i7lQbFdcbuaGDZEFs19VCuNOQqAYDc6u1iZSa09ua9SqNGBmaCV68QAB-o67cfpaznfODQZsLI7uQqsW6w2RzDNuAkQOVm6jK65ebpo19I5zhlF-MbSOgk9lY6M7Jp5341an0fiooCjV2HA9Cg3nEJepaxtk0j4fZOBLnjmpSB5trcTmhzpl8c_Iu-3BPNGdspvW_eDcLN14t285a6h1gSVrvLUePl_P3iaKttckTFPTvSfITJTSeUH2wZHfBKiZaXNu6johzFlbdkMXpWpF5KDoEk1eL7ykPzoKjxifqVnbHG0kMAJkVOIVpmGp6i8XkrWitR53jVzavw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب دوستان، باید بهتون بگم که WhiteDNS روی سرور شخصی خداست.
با MasterDNS ستاپ کردم. که خیلی خفن تر از Storm بهم پرفرمنس داد
تمام تنظیماتش رو هم ویدئو میگیرم و بهتون یاد میدم. به همراه یه لیست 6 هزارتایی ریزالور که جمع‌آوری کردم
به شدت ساده‌ست و بچه‌های تیم در تلاش هستن ساده‌ترش هم بکنن واستون
سرعت دانلود تقریبا 500 کیلوبایت بر ثانیه. بیشتر هم میشه بسته به نت و ریزالور
اینستا راحت باز میکنه
توییتر همه چی به راحتی لود میشه
و مصرف حجم مثل ورژن‌های قبل اصلا بالا نیست</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/3334" target="_blank">📅 15:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3333">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید: https://www.youtube.com/watch?v=tzjVg4O6dVs  چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3333" target="_blank">📅 15:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3332">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آموزش Goose Relay رو می‌تونید از اینجا ببینید:
https://www.youtube.com/watch?v=tzjVg4O6dVs
چیزی که دیدم، روی اینترنت‌های متفاوت از بد تا خیلی عالی جوابگو بوده</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/MatinSenPaii/3332" target="_blank">📅 15:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3331" target="_blank">📅 13:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dktvs2B4MtSTV9C4LNHOsuS4FuwGACgoFNIx7SgL0PHNL9X5l5rIJY-vsuL3zX6kSnFhtpy7U-GpNEPMujer3tzYD2m6I5LfRcAIeGW16_3B1VM437WM-Cll4PxrtKU8iSYEa6w0kOdmwI5XeJR1irwXPnhacMAqz4XtbPYDAWzy9ekZ08uTDX1zZCCU13muZkB2j7K5Roi5C4JpAiavq55vU1Z_YAE1f4c4e9094QF6GnSKejbJSvynIqQV4R5VgBK1ouo3LAII-stuTQg2ozL8dk3DRU0fy8K1VfWwt-fmA_OkD8vYOa6AlglIwLfmuD35EXt91Qd6YgT0dDbSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح  hcaptcha.com  46.38.137.156 81.12.32.136  امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/3330" target="_blank">📅 11:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UdtWaZzAdGQLOQVHGO-fXR7Y7w7yB-z-YjuKgSy7MN1It-fvp49PXcthhq8aSHFNbUT9rxtPh7y3a6B3pIKJQPbz4t8UoTjL64dYSBZeSsdbcjz2_mHIL_nrMwL4q_6Ge69I8EygEkBMMbyt6-Nsdgpgg6S5Ku6wQ14WMZbbI_hHaqe0QZLzxuQcomSbibXV5YN-1JmXAia7UjJGVdy7NI_0q16Ka9w4NBeFLnmN4xEhNxrMb5q5wyxP3-3qAJq4qPHvbwWCSN5fteYIC4GhCMbmGSIRJdFOG7F4dtZRIEPndKP6VYdbybMxEHjgmrk0SaK9HPxR_M9Mmu6JFFCFoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر خاطرتون باشه دی‌ماه حدودا دو هفته میگفتن فردا وصل میشه، این هفته وصل میشه، پس‌فردا وصل میشه، آخرشم تک و توک روی یه سری اینترنتای خاص آیپی‌های کلودفلر رو باز کردن و بعدش هم من Paqet رو یاد دادم و ادامه‌ی ماجرا
برای همین خیلی دل نبندید به این صحبتای صد من یه غاز</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3329" target="_blank">📅 11:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مجددا آموزش share کردن اینترنت از شیر و خورشید بر روی تمامی دستگاه ها(باید به یه اینترنت وصل باشن)</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3328" target="_blank">📅 11:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e4zQpeU2PBhe5t5dAoAsfMwrN2uiNU3cB8Q2DMOSHF5WXSc2IU_2Dw0n3V4UlqFalcRzwoRxj9vJYMAJxbdToz9waw0NI4sndyU8S3JV9RmbDGMunE8OH0CFmxUsWF7fTqHBJyBIWKBLabD_PADDS6nv7w4Wn5DBR4LRNY7EtkstRtGy9lidN645odOWlH-gUwdXHL79UQgvXMksjq0Mue6vuIi0DmBieFyaQ6j_sWudJv4lodcOptT6hY75TdErULz2w3yDlvD0g1U57JokhqjxtzDmHhf31weklN-A0wZzZIdkGjHv7o6z3xTKvCRy1KuOP9T-cyfuPDNiXu6pdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح  hcaptcha.com  46.38.137.156 81.12.32.136  امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3327" target="_blank">📅 11:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک سری از دوستان روی مخابرات و اینترنت‌های خونگی دارن با SNI-Spoof وصل میشن مجددا. زیاد دیدم از صبح
hcaptcha.com
46.38.137.156
81.12.32.136
امتحانش ضرری نداره</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3326" target="_blank">📅 11:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">150 مگابایت همراه اول مصرف کردم با VPN، بسته‌ی اینترنتم نزدیک به 1 گیگ مصرف شد
چه خبره؟؟؟ ضریب زدین روی نت بین‌الملل یا آب قاطیشه؟!</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3325" target="_blank">📅 11:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IqWAJiIrODR9t27BoMoAd_2H_z-sn2rbTZMxMr6mlXK-aRrnZOkawoTib5WJdn9LOmbcW45y3T5UqkPjOaTQUyGZsTQxIFzGUpxYr8vC0xLgCK5Jak_UdYISZg_UhfYBhG3ZVdNXe2J3b_hhW2IHzrSi4dNXuFuTeIVaTUWydzuCPz-NiSzFlhDmP3rlkt6yEej4avbLfgGGWUNFy7VViNdgcvO-mnB1B_ESAHKKW3qoJ6cShTV8Ci64f9ZUo2TwOsexFEAzFd6awIV44XreCgoSPOognJq2zzR-Fq-5kWsn-JPgCxe-X0Hlef06DoZT0FwHIpY7NeKmWnB3O8TOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده از نانو بنانا و Veo گوگل برای تولید تصویر و ویدئو با هوش مصنوعی، رایگان و با اینترنت ملی:
⚡️
پیش‌نیاز: ابتدا متد رایگان و کم دردسر MITM( https://t.me/MatinSenPaii/3151 ) رو برای خودتون ستاپ کنید.  1- سپس وارد وبسایت vids.google.com بشید.
❗️
نکته‌ی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3324" target="_blank">📅 10:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3321">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IK_Ax0Nrx2dpjEiRVww1BaFJee-OUSMaRTdxynQ8qwzIEn_ExDjQ-QTA3U3xhP6ej-5T2LA_rteVSKuIdA8EfeNiO4iYFBBaFgd85atSApTtlXt3YFzd9ZhvHdDdZIsMCWTsiZD42vdfzuHomNLZD4oHaLsBQ6rlsi8fxvVFZ0-6Dp1t3-pr_J08jg8-1xf7mG8IwRaaIXWuo7gLrP50sLTTtEYptrgTIK0uoGX4OE4WxiCIUwo5PwgbhpH8dw7peYFQMFqi3965A96yVHnQKADeeMVMLlziCOQ6FogyooB8E7si6tVZyp9C9-ibufaiCvUkdQ9BiM8rkGcWljp3sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LoudE5V8tFi10OI79654MJR6a0LRFd0E6YolS5R9JKCnMC5iRBVRb4Fv5uuSkGhU9Y8teXLPGuERjseOC5alW3dX7xLbJmlzbSrnW8w3pSWBmQsqoA_WaSyAD7KQMvAoegyPOtHyjF9d3re1iN936d5aXctB6E6mcvQtdnhJRf70aVVqYDw4CfurM3tPg7Vidc3M0r9OW5ySN2RbcO-4m3vSNTs7_pQR71eyvajJD0GULa78fzXF-_Q1cLypDUJDt7e5pDHDnPAZv_C6LgToHY08JTOFYOcpInbc24hTNN-eaKFejJMZypFo1MuINEalyy--7HLDXRH-Zlmt_2D2mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ratQPvVUfN7fp1vrkFJYuy86bTnWFO6PTmgKGdgrFH_JLDTHeGKbrsG_vvf5ZM4rzmZZ0RDJcTF2X6V07pEF-d_FI3fFzoT1Vgo8F-HJohm2-rLUH7HY2g2n45578mD1rV_CWvp7dDMyo_Gtz6s4I1T3UHy666ZSvzx-MFdwG7lfHXmxgZ8WMnuHSxUpZbliIpMys68tf7QjGpMOXFv-e3LqV23qYtVbJMq6i8BlOA5lWro2mzNX0keSJzzvOWa79LPGXrckHF3esg0Mjd3IedJypiHRwHmmYr_yba9MJcMC3n6rvmOSYYRQxVR4Z0xkztitVL_-CccfowNpdzJ8xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده از نانو بنانا و Veo گوگل برای تولید تصویر و ویدئو با هوش مصنوعی، رایگان و با اینترنت ملی:
⚡️
پیش‌نیاز: ابتدا متد رایگان و کم دردسر MITM(
https://t.me/MatinSenPaii/3151
) رو برای خودتون ستاپ کنید.
1- سپس وارد وبسایت
vids.google.com
بشید.
❗️
نکته‌ی مهم: اگر با گوشی وارد می‌شید حتما روی Desktop Mode بذارید تا لود بشه.
2- برای تصویر از قسمت image استفاده کنید.
3- برای ویدئو از قسمت Veo استفاده کنید.
4- اگر برای ساخت ویدئو با سقف روزانه مواجه شدید از اکانت‌های دیگه‌ی جمیلتون استفاده کنید.
❗️
نکته: در صورتی که در بار اول تصویر و یا ویدیو جنریتش تموم شد و چیزی نمایش نداد مجدد صفحه رو رفرش کنید و مجدد پرامپت وارد کنید و مجدد جنریت کنید، بعدش درست میشه و نمایش میده.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/MatinSenPaii/3321" target="_blank">📅 10:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3320">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/MatinSenPaii/3320" target="_blank">📅 09:39 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
