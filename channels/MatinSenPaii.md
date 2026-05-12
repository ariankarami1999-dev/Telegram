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
<img src="https://cdn1.telesco.pe/file/SpLgu4RKB5tI7CbirrDpwVnZErEv4T70iYfjNS8mmSK50p7kthXsjE1Kx7bhokWxU88T22gSQN5x3ayIpHlKL7KAYeCy7hLJWcMslsLISh0CBeWXoHe4r5u5xwsbufBKb5OXDrkugbyWx41rnmAP446ry38QFrvB4EDakQDoFk7iHbKSEhxSa5WDUlS92cBuItOMSsY1T5efzvsTp7a0jc97XyocLwNvrSibI0ESlzhx1ZLplEpyrJWCOJRv0lBAfnndGpa8-eTTtCwHHJG5ylEnSs_v-93en0fTAqZLdSwEY92nmZJ1KFo7lK5bOBrqrDcx3KlfmR7tfkPm5TahSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 94.6K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 یوتوبر انیمه و مانگا(الان کمی شبکه؟!) - برنامه‌نویسِ ایده‌های باحال•YouTube:http://www.youtube.com/@Matin_SenPai•AniList:https://anilist.co/user/MatinSenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 23:24:47</div>
<hr>

<div class="tg-post" id="msg-3026">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2Rdc10OpjFpD1sUd7zDrcDgGMjeiCmC_jHINq3whd03qbxQ8wEf48nnKnA7Di7U6mXE2J21Hqe4oUhT6dcA9rzeAoJhcn59B1g08aaoQCp_2wDSrwZNSefgJamXA-G_nN5wD5g8Zl8a538uzKK59B7631lLHO_NAO5Y06ZFMqkpAF5GFWv_N-36_Io_yctqZN0pxFU4p-8zp_-fQAc-goDasBkppDTJS3ALQnqxS7yJ9AItjQlKgo_UNTDs6iS7keLIjxnlCgCM5_YU_2LhmMLLpoRhQFL61AFsWIBzM-UkzCMuWYISk6vM7vZIss8uVYYnpxrzCSiEowHpiBTCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرفی نمیمونه.من خجالت میکشم که هموطن اینام!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/MatinSenPaii/3026" target="_blank">📅 23:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3022">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/MatinSenPaii/3022" target="_blank">📅 23:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره. اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/3021" target="_blank">📅 21:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تجربه و علم نشون داده شخصی که تجربه‌ی توجه زیاد رسانه‌ای نداره، و مطلبی رو آموزش میده یا توییتی می‌زنه و اون مطلب وایرال می‌شه، مغزش عملا دوپامین رو با هویت اشتباه میگیره.
اینجا مغز فکر میکنه که خب لابد «من خاصم»، نه اینکه «محتوایی که گذاشتم خوب بود. مردم صرفا این محتوا رو دوست داشتن، نه اینکه شخصِ من رو دوست داشته باشن.»
و اینجاست که مغز ما رو به بی‌راهه میکشه.
متأسفانه عموماً از اون لحظه، شخص دیگه حرف‌هاش رو برای بیان نمیگه، بلکه برای حفظ اون حس میگه. و همونجاست که گم میشه و مسیر رو کلا گم میکنه.
به خاطر همین هم هستش خیلی از افرادی که این روزها وایرال میشن، بعدش چیزهایی میگن که ممکنه ازشون بدتون بیاد. توی فرهنگ عامیانه، می‌گن طرف جنبه‌ی شهرت نداشت؛ ولی واقعیت علمیش چیزی بود که خدمتتون گفتم.
اگر وایرال شدید، خواه ناخواه دوپامین کار خودشو میکنه و حس خوبی دریافت می‌کنید اما مدام حواستون به این نکته باشه(همونطور که منِ متین حواسم هست) که این صرفا یک عدده و من تغییری نکردم.
پیروز باشید
✍️
Amir Mokhtari
با کمی تغییر از سمت من</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/3020" target="_blank">📅 18:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2ECugSztoQbRzSk7h0B_AVUl5EolzQ9AejL3n6fHRbQwhGLHhhgt7GfCDPWJ7q564L4-vakBC2bB80Y9oW20vCvZ-ksKRlMrJ0KYHCm5XcXnO0HmcW1Q2PcAwayDo8Z_r8-juqQsmO5AreV65ahv8FV9DoXrR6uyHmdo6K6H4udi8DGjjyiqIK_6qmT-Rbuxr21WILrN6qvlNXdAgB3JfE2RRfprsyw5lONC7LBrdPKUK3gXTAc3iLWQmXI_TOZ7xD56k2AcfxXOFHYdWL2y9kZ6lZf3gOK_jv4Qou-xjrM5FmA-pFZlBDmMrulP863xLlFutWMyjo69stZCVDlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IRCF | اینترنت آزاد برای همه (Twitter/X)
🍷
اپ متن‌باز و
#رایگان
TunnelX برای زمانی ساخته شده که کاربر نمیخواد تمام ترافیک در سیستم‌عامل ویندوز از VPN عبور کنه. با این برنامه میشه فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگه رو وارد تانل کرد و بقیه ترافیک سیستم رو روی اینترنت عادی نگه داشت.
لینک پروژه:
⚡️
http://github.com/MaxiFan/TunnelX/releases/latest
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/3019" target="_blank">📅 17:24 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8PDEYOXFOjlkYcjM1MaqTacPd86HJrjL1TBtTSMnqs4ny9YxfEpzJDoxoD0GiWXhSwE_8hHxdDiOKuHNzV2D5b7_-KoVgIe_AGcpDakE78h2D4bp4l52zlCa9dFFnUPm4_HIhfRefpq6TwgHv5RZwbYqq24ym1INNAOg1KoXXT8T_pKwZAHagS5TXCev-p0bzGMGghbxnZUuLxmP6to1B5X3lFoT4k8r4A8uyYvt0ylPqC8ylCR0Nc4MOA9CkA0PXj-twdMGhradTyttRe9x8FURdT2xkR3uvPsMQAFRINUYNj288rp1USCoRmYIoB8d__kAtqejAjT4XTFDZNWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/MatinSenPaii/3018" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3013">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3013" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/3013" target="_blank">📅 17:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lMaO8gOgRrK-2rwbhAhF_qNoN3xsPmM5A7SXbx_F4eIY7Bbl1Y7-VtHW4BU0H-zTrxUjfvcSJEnKqew68lFjYpYjMR4Lti225qua3TioZfIq3W_UBfwP1ZQEVqUlRSfo1M6R1ufm2tAl2dlXVykBrB-O6mA65ZQ8wipt19Ye7cUmAnJgDYILLzfziSj-5bC5qBr4EAm5sca9TM81_xoF7epTzD8dF92VsnQibrOQ4PNE-LqZazDnIGfsr0i-2f_DhkVmhnoPU7ARBV227sxU88aeRhyJdsGoLmwDyZREpJb0vydNrwD42-lij4QY7CblyUm6LJVAxYMwjEurZZ9dVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YS0BpoeoA_g3sMpBPmg5zn2XUT3uTQtcqmXnvPTcyvPJTUETSoCnrfspGibygZYezBgBT-zKRbP6dOCAc9UiZxOL7HyTZwSLHfg1ZG7LEkFsLaJQZprHVecvcpqauGfUj_DaKGsMHG9tt0cHUDDy0cdjTapnObN422mQfbwm9-uw5uZZ5TR4MH1V4fCddobDFxrdNS1Z1IY0GMcd7cQigb1k7aBbv6Amfo1EuOx01cPa6yyh6PVZxyAhmcYoHZBYHWpeo86vaQfzdAxjLF0DEGzujpVsrtHQkS8qkvj5NumoX0xAgQ97W0UxapHZm_juEaM8EFD79JgVb0Ppk1yplw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به زودی یه آموزش بر پایه‌ی DNS داریم. یک دونه رایگان بدون سرور، یکی با سرور.
به همراه آموزش پیدا کردن ریزالور
با تشکر از بچه‌های تیممون، WhiteDNS
(توی این عکس با سرور رایگان وصلم)</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/3011" target="_blank">📅 23:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">من تازه دیدم که یک نفر امروز صبح 500 دلار دونیت کرده به wallet های روی پروفایل توییترم. و هر کس که بوده، واقعا ازش ممنونم
❤️
کمک بسیار بزرگی به ادامه‌ی فعالیت و همینطور دلگرمی هست برای من توی شرایطی که درآمد یوتوب قابل برداشت نیست و شرایط اقتصادی داغونه. اگر…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/3010" target="_blank">📅 23:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پول پارو کردنی در کار نیست. این پول‌هایی که دارن می‌گیرن بیشتر واسه جبران ضرر و damage control هست که بتونن یه مدت بیشتر قطع نگه دارن.</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3007" target="_blank">📅 09:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فیبر نوری مخابرات کلادفلر وایت لیست شده ظاهرا.. امیدوارم بازش کنن ناموسا بریم دنبال زندگیمون</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/MatinSenPaii/3006" target="_blank">📅 09:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3005">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromfarzad</strong></div>
<div class="tg-text">متأسفانه همه راهها رو معنای واقعی کلمه بستن (غیر از mhr که اونم نصف و نیمه و داغونه) وشما به هر نحوی بخوای به نت بیرون دسترسی داشته باشی باید هزینه زیاد بکنی ، یا بری نت پرو گیگی ۴۰ هزار تومنی بخری یا وی پی ان گیگی ۱۵۰ تومنی مثلا یا بری سرور بگیری cdn بخری وdns بخری و .... بازم هزینه گیگی بالا میوفته ته همشونم پولش تو جیب خود دولت و سپاهه همه ی اینا</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3005" target="_blank">📅 09:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آقا من نمیدونم این چه وضعیتی هست که درست شده توی این کشور !
هر چی میاد میگن پاپلیک نشه ! شما متوجه هستین مردم بیشتر از 60 روزه با این قطعی نت مشکل توی زندگی ش پیش اومده ؟!</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/3004" target="_blank">📅 08:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رفقا من متد‌های حال حاضر رو میدونم. بله میدونم که CDN آروان چطوریه داستانش
منتها برام معقول نیست آموزش دادنش. نه هزینه‌ای که باید واسه‌ی CDN داد منطقیه و نه پابلیک بودنش. اینم احساسی که بهش دارم مثل Shecan هستش. یه Back-Door توسط خود حکومت که خب دست خودشونه.
مثل گوگل نیست که بهشون فشار بیاد که باز نگهش دارن. اگر اشتباه میکنم من رو متقاعد کنید</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3003" target="_blank">📅 08:29 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromペコリーヌ</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pq4scYDISBmbtAmiTD7YxMxagOtqiVe-abrwSfsZIB3hO0DM8ChZaVnrS9s_qgOla0mVoEJRF8rzmTyOv7_sq01SZkZuXAAf2vVDvEsx_I0izAcoxSgiIMQC9NyJolUiJ0lbIMTeU4EUlIP2R2tNqrL_tlQkAtUV9y5PMd55OWMkKnq_8N7KnmFPtlw3YhqMHr-xJOZPTxCFqd7HZaMlVQ8tTWyWtM9nEuO6j3IQLhd1BEJx60VuXdhVnQYieMqKZF-4wqtqCQyjZAR06A95gw-tIQQCXtVw1CESXgnt4FKb8ZQjikxrBcANxGvGGSRJYUK0zaSdcdpf0rkGo_iFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/R5BsXUjmnklH9bwwToDd1CVGWaqsGJ4of_yQUePnZoKeTfdv3GkNj0BulUkqCB0KcrVS4XrU8rPFzAanoEKoXag5RV-Ajr73qbeM4ciBis8AYxX6U3wxSNgtyOL5_hHSwbM3pWnJmsKtO910ofv5MMTLA8Z3vphY5YOMXQXJflRp1CHys9keYRNvM9mZu2ZFMmAExtzqEfHGNzzjmoqal_ue0kPB04auFocXea1xqQbEsvDaHP1dnmtw8R3MyuhAEGN8sW7QDPdMaMFsv9nR-DWkmQLY80569HLvVBiKzM_ExTCqJarTKgljiq1UNKuinS8LDJaNOHqkWNyCzyYZ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واسه ۸ گیگ اکانت رو بستن ؟!</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3001" target="_blank">📅 20:48 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینا رو سرور ایرانی شکن فعال کردن روش vpn زدن و کانفیک میفروشن، طرف در عرض چند روز یک ترا ترافیک رد کرده مشخصه مشکوک و پیگیر میشن</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/MatinSenPaii/3000" target="_blank">📅 20:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نقره ای دارم یه ماهه استفاده میکنم راضیم چرت و پرت هست این</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/2999" target="_blank">📅 19:28 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OOGFBiiKKUTT9s54V6nwuGzI99QzpXYFEtsQT6Jd869dpwBhuvjUea4fzTCKE9fCylsMIw9YKKHTD7eOlVSL_QIdYrTDY-6nmmYH6cLzcP7KWuh6Ii3sePLkHAT-ZeIjsmotu0y7uGTtJB4O47E8Pnu2eLMtL7ecgL09F1O4FHDKOfsE9HRIv43-87ozj49CrCNABliNelvM4pde5sDGWKwH3mpNAciQ_WW9PBG6nJnZhSJJz75oeq1lWjqUiyZJTQl2bIdseP1XUYMO2aww0cFhxBoy65QBNN3bI-Q7W8q_vBkghWsmrFXGeITROQwz79rwMr6HrOKZX_PvTDjYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول به "شکن" و امثالهم هم ندید. یادآوری کنم که چند هفته پیش، به مدت دو سه روز chatgpt روش باز شد و ملت کلی اشتراک خریدن و روش کانفیگ ساختن و باز مسدود شد. پول مردم هم رفت سطل آشغال</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/2998" target="_blank">📅 19:12 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">من این تایم 70 روزه رو خودم 5-6 روزشو قطعِ قطع بودم. اما با اینکه توسط چندنفر بهم آشنا و پارتی از زیرساخت معرفی شد(از فعالیت من هم خبر نداشتن و سر آشنایی بود صرفا) باز قبول نکردم همچین چیزی رو و توی تاریکی و قطعیِ کامل در حالی که لپ تاپم بیست-سی ساعت بود داشت dns اسکن میکرد به دی‌ماه فکر می‌کردم. اگر چند روزی دیدید که من نیستم، بدونید قطع بودن رو ترجیح دادم و یا Dns رو هم بستن عزیزان. کسب و کارها یا نابود شدن یا رو به نابودی هست. هر روز کلی پیام دریافت میکنم که من تدوینگر/هانتر/دیزاینر/فری‌لنسر/برنامه‌نویس/... بودم خرج زن و بچه میدم و تمام درآمدم از اینترنت بوده و لطفا یه متد معرفی کن بتونم وصل بشم و من باید با شرمندگی این جواب دردناک رو بدم که هیچ راه معمولی‌ای وجود نداره برای وصل شدن با سرعت قبل.
اما چه کاری میشه کرد! جز نگه داشتن امید و صبر.</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/2997" target="_blank">📅 21:17 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سوخی با همچین موضوعاتی چیز درستی نیست</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/2996" target="_blank">📅 21:07 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">آهنگ (هفتاد روز که من از تو خبر ندارم) ایرانی</div>
  <div class="tg-doc-extra">•(Ali....Amin)•</div>
</div>
<a href="https://t.me/MatinSenPaii/2995" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مردم ایران خطاب به اینترنت
01:00
🫩🫩🫩</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/2995" target="_blank">📅 20:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آمریکا هم عجیبه
ما داریم زجر میکشیم از نت اونا هم اسنادشون رو منتشر کردن راجب یوفو و بشقاب پرنده
https://www.war.gov/UFO/</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/2994" target="_blank">📅 20:02 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد Advanced Settings شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup:…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/2992" target="_blank">📅 17:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5TMN6z8ubHJEIc3L5ICMFWfD_2G-N7tjhjzPZvaS1zIGWj4r_WAE-ES3J8kx2efl4XWQYTY_bG6MW5ZewxjB_sZDA1jCeuCk0dPiBBYj1p260zKiTMNd-iElvJmsg8FCD5r8IXJM1x1y4rnLO1S7dcsIlPV9wMP7Mguk2rhuWdWP48xDUO4MZVRR2zexy85KF6_mIvJjeTYNzYcweyKbhvbjZh2Dk9p1G4ynDxkP6CDnwNkrcFOmDMUIu8907DXGJRxbzgVFZPFrOlDo2VDZyPXOA33kJkiTnFaJ3TgVvS-Icf-JStFDtMae9c49j2kDid0y9c9sLiepBOh_zKDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/MatinSenPaii/2991" target="_blank">📅 17:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">thefeed-android-v0.17.4-arm64-v8a.apk</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/2990" target="_blank">📅 16:40 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">thefeed-android-v0.17.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/2989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
thefeed-android-v0.17.4-arm64-v8a.apk
📊
Size: 8.9 MB
🔐
SHA256:
466659489e5429db20710d85241012002aec644cb739220338b9dd6aef186fe8
نسخه جدید TheFeed (v0.17.4)
🚀
🟧
تغیرات بخش اصلی
:
🔸
نسخه IOS بصورت ipa در دسترس هست، اگر بلدید خودتون ساین کنید و تست کنید بهم خبر بدید که چطور بود (دارم تلاش میکنم بزارمش روی تست فلایت تا همه بتونن نصب کنن)
📱
🔸
برنامه زمان اجرای اول زبان رو میپرسه
🗣️
🔸
فیلد جستجو فقط با یوزرنیم جستجو میکرد، الان با اسم کانال هم جستجو میکنه
🔍
🔸
زمانی که اسکرول کنید مثل تلگرام تاریخ پست رو بالاش نشون میده
📅
🔸
اضافه شدن بخش حمایت مالی
❤️
🟦
تغیرات بخش کانال های دلخواه
(TeleMirror):
🔹
دکمه نمایش پست های بیشتر به بالای اولین پیام اضافه شده تا بتونید میام های قدیمی تر رو هم لود کنید و ببینید
👀
🔹
قابلیت باز کردن عکس ها
🖼️
🔹
قابلیت تغیر سایز فونت
📝
🔹
نشان دادن ای دی پیام ها
🔢
🔹
رفع مشکل نمایش فایل تکراری
🗑️
🔹
دکمه برای پریدن به اخرین پیام
⏩
کانال اصلیم:
@networkti
کانال کانفیگ:
@thefeedconfig
لینک دانلود نسخه جدید برای تمام سیستم‌عامل‌ها از داخل ایران (با گیتهاب):
https://github.com/sartoopjj/thefeed-files/archive/refs/heads/main.zip
📥</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/MatinSenPaii/2989" target="_blank">📅 16:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به نظرم اولین اقدام دولت این خواهد بود که یه لگد میزنه به Google و ما، و MHR قطع میشه</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/2988" target="_blank">📅 01:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این کار «زدن و گردن نگرفتن» واقعا رو اعصاب‌ترین بخش جنگه
کی اینو بهتون یاد داد اصلا</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/2987" target="_blank">📅 23:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-344eQ9Pgqp56Ykakd5G3Y4gFxfTv6GcNLCPkQOQA_gapeIJBdfGUYNxvHGkKgKa6SoMxQyrEkuFo29dk-iBRr7hh5hoE3N-vUW1VrzA2DZIyiz3Flh4d--HAJCbU4KhYgLlkTkXwnoBEJJ7bXa1DwSVG-bWdPJnw8Clze7bbDnmQzFnYKnvXHIkiGuBuge__rs_E7bPSb0ACEEX3NMgkdcSaLKw_ksHoiaCaoemJcjM8qObIOYR5UkEx4HlKoV5L8iIAK625Vbyp-mUnwkfmteJqIW7j3P5-g1vLvRpHYxIVyv3nQ04J-bCQf1-F-kqN3Q3BJk5thSgGfNr5lGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچه سریعتر اکانت مایکروسافت ویندوزتون رو از مایکروسافت به Local تغییر بدید تا این بلا سرتون نیاد. همینطور علاوه بر پین کد، پسوورد هم تنظیم کنید و راه‌های دیگه‌ی لاگین.
من دو بار به این مشکل خوردم و متأسفانه تنها راهی که پیش بردم این بود که از طریق Advanced Troubleshooting رفتم و ویندوز رو دوباره نصب کردم(فقط اپ‌های روی درایو C پاک میشن و بقیه درایو‌ها و همینطور پوشه دانلودهاتون سر جاش میمونن)
اینجا یه ضربه‌ی وحشتناک خوردم و اونم این بودش که مجددا بعد از چند روز قفل شد و روز از نو روزی از نو. که فهمیدم راه حلش اینه:
1- تغییر اکانت مایکروسافت روی ویندوز به Local account
2- حذف پین کد(که بکاپش ایمیل مایکروسافت هست) و اد کردن password یا یه راه لاگین دیگه. بعدش مجددا میتونید پین کد هم اضافه کنید
الان سه هفته اینهاست که به مشکل نخوردم دیگه</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/MatinSenPaii/2986" target="_blank">📅 22:44 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bgBVCB9gvJC-9hL4CYG3RNsSpWt7BLEbJHubVznA549I9ZXmHkoq59wMLppesh23VGMZNnLDeUKxsZ0IzhGgLuOmGVsg-ezPnx8fhY1amsqqiXK7Z6mCWqn4Lyyt460udwFQAFjJu7TdhACCfaWBsdLXzMonVovzqi8wBNBLH6sCMUXguzCwK7ewKG3J7rBmnj1yck5oOr3QFnaNTDNOOhsRZ0j8VSwTdJ3eWqZppv-gx_2aq_h5GYbQgiaT17jDjGH4ROZXtaYLR2KkMIK46CPsJ-TDz9fYnJ81RVhFBkQswSRDO9BUaieLS9tRY0ZZrgcnUxxzLi-UiL0w3sNotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان فرمودن که با این ریپو: https://github.com/ThisIsDara/mhr-cfw-go تونستن مشکل کامنت‌ها و ارور restricted رو برطرف کنن</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/2985" target="_blank">📅 21:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه سریا برمیدارن Deployment id هایی که من توی ویدئو استفاده میکنم رو می‌زنن و استفاده می‌کنن
😂
من عادت ندارم اصلا پاک کنم چیزیو. و اشکالی هم نداره. فقط کلودفلرم و گوگل اسکریپتمو ترکونده بودین هرچی اکانت روش آموزش دادم
😂</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/2984" target="_blank">📅 21:17 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j7aL10h39XekHDv_OUCD1uGi4WcPMWkDyuVFRo3j7zy7swdI6DPcI5ZlQXThB_I--Pfqx-rVgw5dbmshwIDYieOsZjGYNV1HhrUFaMvH5gkQ4AVZz3Df2vM6Jsnz8p0J1d-mlqfxWekV279VjfrPL_FUabrhbXcJr99ce8ZeP2hcXgDF_VXWz6DFAzqd4Rw_Yvy5OjLmNl-wt40nrDNSYVhC_1FAhqSbTAG9XuvCwsPFkwEkLN804mlFr_avT6iqFhbQmlwEMqW1F9K4GpXRe_uKw9KJ9q-XHVfzQzfJieu1x-Cf_MaMptjJj7c6lECZZpNwVX8_9I7Pm1q7b_Bb7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان فرمودن که با این ریپو:
https://github.com/ThisIsDara/mhr-cfw-go
تونستن مشکل کامنت‌ها و ارور restricted رو برطرف کنن</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/MatinSenPaii/2983" target="_blank">📅 21:06 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">قوانین مسخره ios که نه
خارج از ایران اصلا نیازی نیست mhr بزنن</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/2982" target="_blank">📅 20:51 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اندروید نداریم</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/2981" target="_blank">📅 20:45 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود: https://t.me/MatinSenPaii/2969  لینک پروژه اصلی: https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/2980" target="_blank">📅 20:43 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">می‌دونستین یه نوع اعتیاد هم داریم به اسم اعتیاد اطلاعاتی؟
شما ممکنه ساعت ها با هوش مصنوعی چت کنید و خسته نشید و ولعتون بیشتر بشه برای چت کردن باهاش، یا اینکه یه نصفه روز توی صفحات ویکی پدیا بچرخید و مدام اطلاعات مفید بخونید با این فکر که آره دارم چیزای مفید یاد می‌گیرم، اما این کار شاید ظاهرش به اعتیاد نخوره اما جالب اینجاست چون دوپامین پسیو (دوپامینی که بدون سختی داده بشه) می‌ده و هیچ سودی هم نداره دقیقا خود اعتیاده. فرمول خاصی هم برای ترک کردنش وجود نداره اما مثل همه اعتیاد ها میشه با سختی کشیدن ترکش کرد برای مثال یه کتاب (فقط حتما یک موضوع واحد باشه) رو بخونید دقت کنید فقط موضوعش واحد باشه.
یادتون باشه هرچقدر هم درباره چیز ها در طول روز بخونید اگه اخر شب نتونید 3 خط دربارش بنویسید اون چیز هیچ وقت به آیندنتون کمک نمیکنه و بیشتر جنبه سرگرمی داره.
@Linuxor</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/2979" target="_blank">📅 16:19 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💬
یه سری مطالب از Repo سازنده‌ی MHR واستون قرار میدم(مربوط به این روش: https://t.me/MatinSenPaii/2785) :  اول از همه دقت داشته باشید که به روز ترین نسخه‌ی code.gs رو حتما از گیتهاب پروژه گرفته باشید: https://github.com/masterking32/MasterHttpRelayVPN/blob/…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/2978" target="_blank">📅 15:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ولی من دقت کردم نه کسی پین نگاه میکنه نه سوالشو سرچ میکنه تو گروه فقط میپرسن پشت هم</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/2977" target="_blank">📅 04:14 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">به نظرم تریدرا الان باید به جای دوره‌ی آموزشی، دوره‌ی تحلیل رفتاری ترامپ رو ببینن</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/2976" target="_blank">📅 01:35 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL4Jyw0pLJ9RAvFRR9xJx3XJEHSD_mIltHPrz14C-jnOh5yeNlZ7vv5CUg19qUZrWTYTti0gWTCfnfqbvwtHjqPLgtxy2kLvjA-7w5xtmYYncYva6fyN_JSmFXNuPGMwn0_YE4Vr0NQIpOX-1zDrZql7xvDK7HWWp9mIfTEsdCAmlchuOzLcpLnYREiUGjKIGxV018xKdz9oTZFtmDvDze4PdzHnkNKHE__Sw-XNiq07cF-wrIPzyDEIdp_yj_0Aq7d2t9I8AF0IjHfSG-bdSF9qwm3xvpx9ILLXRVYlAK299xfktbvwRK4MtIOoM3KGvIcZvX5dzKsqpkc1l8ihuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
دانلود با اینترنت ملی از یوتوب و تورنت و هرجای دیگه!
پروژه AzuDL - GC2GD یه ابزار کاربردیه برای دانلود فایل‌ها از طریق Google Colab و ذخیره مستقیم اونها روی Google Drive
با استفاده از این ابزار می‌تونید لینک‌های مختلف رو داخل Colab اجرا کنید و فایل نهایی رو مستقیم داخل گوگل درایو تحویل بگیرید؛ سپس با متود MHR فایل نهایی رو دریافت کنید.
🖥
قابلیت‌های اصلی پروژه شامل دانلود لینک مستقیم، دانلود ویدیو و پلی‌لیست یوتوب، استخراج فایل Mp3 و... هستش
💡
ویدیوی آموزشی پروژه AzuDL -
GC2GD
سورس پروژه:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
✉️
@MatinSenPaii</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/2975" target="_blank">📅 01:23 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/2974" target="_blank">📅 01:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لینک های داخلی اموزش و برنامه
📥
mhrv-rs-android-universal-v1.9.14 39.2 MB
📥
mhrv-rs-android-arm64-v8a-v1.9.14 18.1 MB
📥
mhrv-rs-android-armeabi-v7a-v1.9.14 15.8 MB
📥
ویدیو اموزش ساخت متد MHR نت داخلی 18.3 MB
📽️
﻿</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/2973" target="_blank">📅 01:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-text">لینک های داخلی اموزش و برنامه
📥
mhrv-rs-android-universal-v1.9.14
39.2 MB
📥
mhrv-rs-android-arm64-v8a-v1.9.14
18.1 MB
📥
mhrv-rs-android-armeabi-v7a-v1.9.14
15.8 MB
📥
ویدیو اموزش ساخت متد MHR نت داخلی
18.3 MB
📽️
﻿</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/MatinSenPaii/2972" target="_blank">📅 01:11 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⏱
لینک فایل‌های apk با نت داخلی:  https://guardnet.ir/f/8785ed32c47c (متاسفانه فقط آرمبی ۷ هست باید اون یکی رو هم بذارم)
⏱
لینک دانلود ویدئو: https://guardnet.ir/f/c5321e5300d0</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/2971" target="_blank">📅 19:11 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یعنی انقدری که سر آپلود و سرعت آپلود توی سایت داخلی اعصابم خورد شد سر تمام  فرآیند ضبط و ادیت و آپلود روی یوتوب و  تلگرام ویدئو اعصابم خورد نشد. بهتره تایپ نکنم دیگه چون اصلا کلمات خوبی به ذهنم نمیرسه</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/2970" target="_blank">📅 19:04 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⏱
لینک فایل‌های apk با نت داخلی:
https://guardnet.ir/f/8785ed32c47c
(متاسفانه فقط آرمبی ۷ هست باید اون یکی رو هم بذارم)
⏱
لینک دانلود ویدئو:
https://guardnet.ir/f/c5321e5300d0</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/2969" target="_blank">📅 18:59 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود:
https://t.me/MatinSenPaii/2969
لینک پروژه اصلی:
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد با گوشی بسازین، به علاوه‌ی آموزش یه کوچولو کاهش مصرف ریکوئست‌ها(به نظرم دیپلویمنت بیشتر بسازید راحتتره)
🚀
لینک‌های دانلود با نت داخلی:
https://t.me/MatinSenPaii/2969
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/MatinSenPaii/2968" target="_blank">📅 18:58 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">Mhr cfw با ترموکس رو بذار لطفا</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/2967" target="_blank">📅 18:03 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">باو از MHR و این داستانا بکشین بیرون تاوقتی ورسل و نتلیفای هست :)</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/MatinSenPaii/2966" target="_blank">📅 18:01 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آموزش بعدی روش ساخت MHR کاملا با گوشی هست بدون نیاز به لپ تاپ و مشغول آپلودش هستم
متشکرم از دوستان عزیزی که کانفیگ رسوندن به دست من
داخلی هم واستون آپلود میکنم صد البته</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/2965" target="_blank">📅 17:56 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک نفر 47 دلار دونیت کرد. ممنونم ازت هر کس که بودی
❤️
کمک‌های شما حمایت و دلگرمی بزرگیه اما دلیل فعالیت من نیست. کار من همیشه بدون چشم‌داشت بوده و هست</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/2964" target="_blank">📅 20:32 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سؤال: چرا قیمت کانفیگ‌فروش‌ها پایین اومده یهو؟
جواب: 1- تعداد زیادی از کانفیگ‌فروش‌های حال حاضر، زرنگی کردن به حساب خودشون و اومدن از سیمکارت‌های پرو و سفید استفاده می‌کنن، و تا می‌تونن می‌فروشن.
2- همینطور یک تعدادی هم از متدهای خاصی که رندوم واسشون جواب داده استفاده میکنن(به طور مثال یه range آیپی وایت شده سرور ایران اینا هم جزوشون بوده یا استفاده از Shecan)
3- استفاده از اینترنت طبقاتی شرکت‌ها، سازمان‌ها و یا دانشگاه‌ها و اساتید.
4- دلایل دیگه‌ای هم هستن که یا من نمیدونم یا حضور ذهن ندارم.
به خاطر همین قیمت کانفیگ پایین اومده. منتها من پایداری زیادی درونشون نمیبینم. اگر جایی ارزون دیدید که اوکی بود هم، کم کم بخرید. یهو نرید 50 گیگ بخرید</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/2963" target="_blank">📅 16:22 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(مایلز گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbG-X_37ecleeR-dB4fquutYZKRPs79at4SUnnSSYbLy9N89rAXVD2n-y5nZnfekP2Ns7i3GffECOBiqrrx1eo1U3zI1njjFPyZ35WQNu036KdKHdS26UCrZywv1bVu39OcvsQZOBgQlGnRNB8PsU86i_Mm3L3xjQcWS2_0LGsAlDh49XAD3sHRv-TpSnugRltVSS0fpfyFFBcDLPLP6w7A7KQuqGeZ0JxIEpe2LAk7P0F3OpqASMk_6VVX5_uiAVwtIwXI26exsQYS_B-cnjHZKsU2EqqsGa5vhzoZwldf_D1z1u_mrfxRfEwU_nlf_4XZOXLRNs22l4qaSh9Gw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍷
اپ TeleMirror یه تلاش آزمایشی برای دریافت آخرین مطالب کانال
#تلگرام
خودم و سایر کانال‌های موردنظر در شرایط محدودیت شدید اینترنته، که سعی می‌کنه با چند روش مختلف پست‌ها رو بگیره و نمایش بده.
این برنامه
#رایگان
و متن‌بازه و فعلا می‌تونه برای دنبال کردن اخبار تلگرامی بدون نیاز به فیلترشکن، یه گزینه موقت و کاربردی واسه دسکتاپ باشه.
لینک پروژه:
⚡️
http://github.com/ircfspace/teleMirror/releases/latest
(پخت و پز عشق ircf)
@ircfspace
💎
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/2962" target="_blank">📅 21:25 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حملات آخرالزمانی اسرائیل به جنوب لبنان</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/2961" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دی ان اس هاتونو آماده کنید</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/MatinSenPaii/2960" target="_blank">📅 18:43 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خب فکر کنم دوباره جنگ شد؟</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/2959" target="_blank">📅 18:43 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/2958" target="_blank">📅 17:17 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اینا که این پایین میاد و خیلی ممبر دارن بازم کلاهبردارن؟</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/2957" target="_blank">📅 17:15 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGc1HCLmVvAEFwRdOpI66E-xtfEvHxy1p7OnFYNlqEToI95_NjdUzzZ80LYxte-l5q2oDf4jgGTi5_W9CCWzf-vPnfSdh-NeVAinIeVfgKA6i8uUJGRKucj7ozjbgtycuM72CzUSryUwMXGC4cJVlQUNlUECp2-zGJvPJZ4o4cquUGUMd5RdDyecK76Hv0b37rd1ONDxm4jC0z2vh3rCld-F_RmXeewhBLMt4VE4IfM44B5ZhleNeJ3rYf7BJUb9uZMQR0GPKRn5oID4f7NVRW4mkuSJhcinJKZ494pJet2_9QrYZq7lwZiJdgNe2jAt_8bVZjvLIVFn5y4_qbvU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تبلیغات هم مال کانال من نیست. اعصابم خورد میشه با یه ذره Ton تبلیغ میزنن این زیر اونوقت من باید چندین هزارتا Boost بخرم تا تبلیغات رو غیرفعال کنم</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/2956" target="_blank">📅 17:10 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شرایط نت و محدودیت‌ها رو درحال حاضر نمیشه پیش‌بینی کرد. همونطور که میدونید با کوچکترین حرکتی همه‌چیز محدود میشه..
اما به محض اینکه یکم شرایط استیبل بشه، پیگیر کلاه‌بردار ها و کسایی که تو این وضعیت بد جای کمک و کنار مردم بودن ازشون دزدی کردن و زخم تازه ای روی زخم‌هاشون بودن خواهیم بود.</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/2955" target="_blank">📅 16:57 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من با این لیست وصل هستم خودم روی همراه اول و سیمکارت شاتل
185.161.112.38
194.225.152.10
217.218.155.155
185.20.163.4
78.157.42.101
31.24.234.37
31.7.78.205
80.75.14.102
185.255.89.57
2.188.21.138
2.188.21.58
2.189.44.68
185.110.244.150
2.189.44.98
2.188.21.62
2.188.21.70
80.210.40.55
85.185.163.4
2.189.44.66
2.188.21.46
2.189.44.84
2.189.44.82
2.189.44.86
2.189.44.85
2.189.44.83
80.210.40.53
2.188.21.146
172.64.32.0
108.162.192.0
78.39.234.230
173.245.58.0
2.188.21.78
2.189.44.44
185.20.163.2
194.60.210.66
217.218.127.127
2.188.21.130
31.24.200.4
2.185.239.138
5.145.112.39
85.185.85.6
217.219.132.88
178.22.122.100
194.36.174.1
185.53.143.3
80.191.209.105
78.157.42.100
213.176.123.5
185.55.226.26</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/MatinSenPaii/2954" target="_blank">📅 11:45 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گویا یک پروژه‌ی دیگه نوشته شده واسه‌ی Vercel
که تشخیصش سختتره توسط سایت
اما من به دلایلی که قبلا گفتم آموزش نمیدم چون از نظرم به درد نمی‌خوره. مردم نه میتونن راحت اکانت بسازن داخلش، نه اعتباری به وایت موندنش هست، نه اعتباری به بن نشدن اکانت. توصیه‌ی اکیدم هم اینه که اکانت Vercel Pro نخرید. اما باز هم اگر علاقه‌مند بودید،
این خود پروژه هست:
https://github.com/B3hnamR/XHTTPRelayECO
این هم آموزش متنیش:
https://github.com/B3hnamR/XHTTPRelayECO/blob/master/Anti-Ban-Tutorial.md</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/MatinSenPaii/2953" target="_blank">📅 11:31 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitends-beta3-arm64-v8a-debug.apk</div>
  <div class="tg-doc-extra">22.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/2948" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/2948" target="_blank">📅 10:14 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2947">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نسخه‌ی بتای 3 منتشر شد. دوستان از سرورهای دیگه‌ی storm توی چنل استفاده کنید. خود سرورهای built-in سرعتشون یه کوچولو پایین اومده</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/2947" target="_blank">📅 09:40 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxhKMvGv6-sGWzOR2xKHIZeafkVeW0NqPGP0ocpATcW9HEL54KghHyMGvR8qhpAHbbZVqAXZxJQbf26wFlGMpvb78UjbHNQgG6q7_D2vLIgfcgIaMSQbvSzHpISWQHaJlD_8y-pqEGIi2sGC_ooOQNYUZE40LMwLmDetqDmOoMdzVbCkKJlKU0FYUNHmIat3R7H87EBM-dEccR-VJVd6qptIb0sNF6NrVBcdIuyc1wTbOnD860Hvbo1dHSoO5gd8jaUQiluFDewDY6RUiMDhyFD5Uze8_JbPERkHJdS_WkCq08N6-k5ktZt08xi8dJJcRX1MzyptC0_SVPXr16rUCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N32lnCvhN7WYJNcOOGgzQX80RLIZa6vRNmqZZH1kW-gNx2acoscYg4upB4CkGQONVUwE5os9XvnutCtUg5mBi9kyMGXDVr_fImahmrWlvJQ4iZIeHqLo7CIfIhfgmbAxILOIdMCDBaum6VrQXC7no92dROEp54V-_5kfFP7h2sJbGoJkdLFUq1LNYXNZKLySJdwgsk7Oeqq8GYEItcBp80c6lE940X0U1D9KxNQTwj9oE5bBB2fgzXTC4ZjaGiXS2SEKRwSMD_Exm6g6xqtDwn7E1EpCanSOyZZPfg8cunJziU43Q6-3yJ22_0PZVyKftfVHtvFbpxU2rKpt3SSByA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
دانلود سرور داخلی
https://uplod.ir/gce7505a78tl/WhiteDNS-Beta3.zip.htm
https://guardnet.ir/f/whitednsB-3share
در این نسخه تغییرات زیادی روی ظاهر، پایداری و مدیریت کانفیگ انجام شده:
✅
طراحی اپلیکیشن کامل بازطراحی شده و حالا ظاهر جدید، ساده‌تر، مرتب‌تر و دارک دارد
✅
دارک مود و رنگ‌بندی جدید برای خوانایی بهتر اضافه شده
✅
امکان ساخت چند پروفایل کانکشن اضافه شده
✅
امکان ساخت چند پروفایل ریزالور اضافه شده
✅
انتخاب پروفایل کانکشن و پروفایل ریزالور ساده‌تر شده
✅
لاگ‌ها جدا شدند و حالا خواناتر نمایش داده می‌شوند
✅
امکان کپی و خروجی گرفتن از لاگ‌ها اضافه شده تا اگر مشکلی داشتید راحت‌تر برای ما ارسال کنید
✅
دکمه Reset to Default برای برگرداندن تنظیمات پیشرفته به حالت پیش‌فرض اضافه شده
✅
تنظیمات اضافه و گیج‌کننده تا حد ممکن مرتب و حذف شدند
✅
دسترسی Battery Optimization اضافه شده تا اتصال در پس‌زمینه پایدارتر بماند
✅
باگ کرش کردن اپلیکیشن بعد از Disconnect مخصوصا در حالت Full VPN برطرف شده
✅
نسخه جدید بهینه‌تر شده و لاگ‌ها فقط آخرین موارد مهم را نگه می‌دارند تا روی عملکرد اپلیکیشن فشار نیاورد
✅
حالت Proxy Mode به عنوان گزینه پیش‌فرض قرار داده شده چون عملکرد بهتر و پایدارتری دارد
پیشنهاد ما این است که اگر امکانش را دارید از Proxy Mode استفاده کنید. حالت Full VPN هنوز برای تست وجود دارد، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است سرعت و پایداری پایین‌تری داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/2945" target="_blank">📅 09:39 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💬
یه سری مطالب از Repo سازنده‌ی MHR واستون قرار میدم(مربوط به این روش:
https://t.me/MatinSenPaii/2785
) :
اول از همه دقت داشته باشید که به روز ترین نسخه‌ی
code.gs
رو حتما از گیتهاب پروژه گرفته باشید:
https://github.com/masterking32/MasterHttpRelayVPN/blob/python_testing/apps_script/Code.gs
✅
1- برای اسکن سریعترین IP گوگل، این دستور رو اجرا کنید:
python main.py --scan
و بعدش توی config.json، آیپی پیدا شده رو توی بخش
google_ip
قرار بدید اونی که پینگ کمتری از همه داره.
✅
2- گوگل و یوتیوب باز می‌شن، ولی ویدئوها پخش نمی‌شن و سایت‌های دیگه هم باز نمی‌شن:
الف) محدودیت روزانه 20کا ریکوئست شما تموم شده. تا فردا صبر کنید ساعت 10:30 صبح
ب) deployment شما مشکل داره و باید مجددا روی همون اکانت گوگلتون پروژه رو دیپلوی کنید
ج) اکانت شما فلگ شده و باید با جیمیل دیگه‌ای دیپلوی کنید بالکل پروژه رو روی یه جیمیل دیگه دیپلوی کنید
✅
3- ارورهایی از جمله certificate error و ... به خاطر نصب نبودن سرتیفیکیت هستن. ویدئو رو با دقت ببینید و سرتیفیکیت‌ها رو نصب کنید
✅
4-  خطای unauthorized: مقدار auth_key و AUTH_KEY باید یکسان باشه از سمت گوگل و فایل شما
✅
5- ارور timeout آیپی گوگل فیلتره واستون(به سؤال 1 مراجعه کنید)
✅
6-  سرعت کم: سازنده گفته که استفاده از چندین deployment_id و چندین اکانت گوگل، این مشکل رو حل میکنه</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/MatinSenPaii/2944" target="_blank">📅 20:13 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دیروز به گوشم رسید یکی متد نامحدود خریده بوده 2 میلیون تومن
وقتی که خریده
طرف گفته خب حالا متد رو الان واست میفرستم
پست‌های کانال من راجب MHR رو واسش فوروارد کرده:)))
مراقب باشید اینجوری اسکم نشید دوستان. هر متد عمومی‌ای که باز بشه من و بقیه‌ی بچه‌های کامیونیتی اعلام میکنیم.</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/2943" target="_blank">📅 19:36 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">❌
پولت رو بده نیازمند، سودش بیشتره تا بخوای شکن بخری! من شکن حرفه‌ای خریدم، اگر اون پول رو میدادم غذا برای گربه‌ها میخریدم، بهشت رو واسه خودم خریده بودم! نمیدونم چرا اینقدر شکن رو بولد میکنن! البته به قول متین: «شکن چند وقت پیش هم اومد خودش رو بولد کرد و مردم حمله کردن اکانت خریدن تا روی chat gpt کانفیگ بسازن، بعد که فروخت، چت جی‌پی‌تی رو بست!» اکثر این‌هایی که تبلیغ شکن میکنن بازاریابِ همین دزدان و قوادان هستن! که مردم برن بخرن بعد قطع کنن! تهشم بگن: «اختلال از سمت زیرساخت هست و ما تابع قوانین کشور هستیم» یعنی پولت رو نمیدیم و بهت هم میخندیم!</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/2942" target="_blank">📅 19:23 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">توی این سایتِ خودِ گوگل، می‌تونید از مدل هوش مصنوعی نانوبنانا 2 و Pro برای تولید تصویر، به رایگان استفاده کنید. تبلیغات و credit و ... هم نداره امکاناتش هم حتی از اکانت Pro جمنای برای تولید عکس بیشتره: https://labs.google/fx/tools/flow</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/2941" target="_blank">📅 18:38 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2940">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Go1mYrGXHoUBXhDJuFgdu85bfQZCVxXvCTKehMqKJTBwgpXhSv2QIA_HE4wgBs-CZ2yyfBrBfmOY169dTulgxxG3NXaybVG-zY_oI4cRWpgJ1L1dYFwbIxO1no0C0GB8HQVk1gXzyki12kEoA22VSW0eUgCa6mwSuDYAsHtiKZ1aO_gWvXE45LcJHgsxyEStb6dHT_FIBNNNvWgZM3gqXG9qDI2xEqVRDEn_VzUq_JOt7VSCX9H3tbp_-hXdvcCxrRjlxMocS5_Jo1RdXqBKJJrxhh2ZUfnBgMbAhZacWAcMB6kjvLg-3aXXfl2FolYsgbIIjeuWqxaZdHOSqqCX5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این سایتِ خودِ گوگل، می‌تونید از مدل هوش مصنوعی نانوبنانا 2 و Pro برای تولید تصویر، به رایگان استفاده کنید. تبلیغات و credit و ... هم نداره امکاناتش هم حتی از اکانت Pro جمنای برای تولید عکس بیشتره:
https://labs.google/fx/tools/flow</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/2940" target="_blank">📅 18:31 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2939">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">من وپن دارم ولی خب جمنای اینا نمیتونم باز کنم
کاریش  کرد؟
ارور میده</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/2939" target="_blank">📅 16:17 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نمیدونم چقدر به دردتون می‌خوره توی این شرایط اما من می‌تونم آموزش دور زدن تحریم‌های Google Antigravity و کلا ai agent ها برای برنامه‌نویسی(با کانفیگ‌های غیررایگان طبیعتا. چون ایرانی تشخیص میده ما رو) بذارم واستون. اگر آموزشی هست که به دردتون میخوره و نیاز دارید بهش هم می‌تونید باز بگید این زیر، اگر دیدم مناسبه یا تخصصش رو دارم ضبط می‌کنم</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/2938" target="_blank">📅 16:14 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J5DoYZGaD4o9MS_Tp8UsBELSXOvW7bnJ1JmZH0ys7tbxLjg9xxisaWga1xWILmrp-ey1ZilKDhu_O6oKwD15BGxMB1TzWqhsUJjDDBrFMgzvBsl0gFHmhO9BnTpORZ8rGdyut4Koo6cibc8LDK2o9fq98ECRy4kwE-bKif_GoAOmrQGZbtQimT0j6VE7L_HYyIo4GaKLXI84nsbF4MQ3alk6Gtjm_CmoJ5_1r-IeZeHFjj5PSNUcv4FaM4hgCwrOqfA6SnkU8KM8QxKPhGBZHWvHjDalJ8NVLQ0eQSkFvm8sB7_F2B1Ti4WyCXbl_qpn5crZNJhbYJpDJrrpLDtsPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدرد نمیخوره
بدرد اتصال ضعیف میخوره من نیاز شدید به یوتوب دارم</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/2937" target="_blank">📅 14:50 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پدرام گفتش که یه نسخه‌ِی دیگه هم میده که بتونید سرور خودتون رو واردش کنید</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/2936" target="_blank">📅 14:36 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2935">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اپ کلوز سورس هستش طبیعتا ولی من امنیتش رو تضمین میکنم.</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/2935" target="_blank">📅 14:07 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پدرام شاهکار منتشر کرده. تست کنید
منطق اینه:
سرورها به صورت رمزنگاری شده نگهداری میشن، شما دیگه نیازی به سرور ستاپ کردن ندارید.
فقط dns ریزالور تمیز که میتونید با اسکنر پیدا کنید(قبلا توی کانال گذاشتم اما با اسلیپ نت هم میتونید)
و Dns رو میزنید، کانکت میشید و استفاده می‌کنید به راحتی</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/2934" target="_blank">📅 14:07 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS.apk</div>
  <div class="tg-doc-extra">22.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/2933" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخه تست همگانی کلاینت VPN وایت‌دی‌ان‌اس منتشر شد
🔽
لینک دانلود سرور داخلی  https://uplod.ir/i7zea22zumur/WhiteDNS.zip.htm   در این نسخه از WhiteDNS، هسته ارتباطی روی StormDNS ساخته شده و ما تا جای ممکن آن را برای شبکه‌های محدود، ناپایدار و پر اختلال بهینه…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/MatinSenPaii/2933" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2932">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_I_6kE3CPsOsFPRFbkByS5eSIkFtpVlFtrwWxQ7hwYPB42Tl-p1kP50GDVbcal2T1nrNsttnRk88PrLIFbhXqweFnTn-EW3FURX4NxF7SvVZddKLONwsbAE17gdsf5-UxvJOMQ_lqIOEdT5oISkFc5GeLjzJiWMUKWRTu6zdGSBjG8mhJ3sBuQbHfNA6RCH8Q-n7LQke3MJ6PICLzyQSfKd_O39ru8wB1jFs0CSNqXh6s0q3r-3KgwhyIH2qpf_HHPchinfxzWHMbLMpD3c_wAaoW19CNzu50IXvIOwinuIoMWkOxK1H6MgvewAG__pl4uz5SSPWQzYeiZ1PbeJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه تست همگانی کلاینت VPN وایت‌دی‌ان‌اس منتشر شد
🔽
لینک دانلود سرور داخلی
https://uplod.ir/i7zea22zumur/WhiteDNS.zip.htm
در این نسخه از WhiteDNS، هسته ارتباطی روی StormDNS ساخته شده و ما تا جای ممکن آن را برای شبکه‌های محدود، ناپایدار و پر اختلال بهینه کرده‌ایم.
برای اتصال، نیازی به وارد کردن سرور، کلید یا تنظیمات پیچیده ندارید. فقط کافی است Resolverهای خودتان را وارد کنید یا از لیست آماده داخل برنامه استفاده کنید. اپلیکیشن Resolverها را تست می‌کند، مسیرهای سالم را پیدا می‌کند و سپس به صورت خودکار اتصال را برقرار می‌کند.
قابلیت‌های فعلی:
✅
اتصال Full System VPN برای کل گوشی
✅
حالت Proxy Only برای استفاده دستی
✅
استفاده از چندین سرور داخلی WhiteDNS
✅
تست خودکار Resolverها قبل از اتصال
✅
امکان استفاده از لیست آماده Resolverها
✅
تنظیمات پیشرفته MTU برای شبکه‌های سخت‌تر
✅
نمایش سرعت دانلود، آپلود و مصرف کل دیتا
✅
لاگ اتصال برای بررسی خطاها و وضعیت کانکشن
✅
بدون نیاز به وارد کردن کلید یا دامنه توسط کاربر
اگر روی اینترنت شما اتصال سخت برقرار می‌شود، می‌توانید مقادیر MTU را تغییر دهید تا مسیرهای بیشتری شناسایی شوند و اتصال پایدارتر شود.
⚠️
این اپلیکیشن هنوز نسخه تست اولیه است.
ممکن است روی بعضی دستگاه‌ها یا بعضی اپراتورها نیاز به تنظیمات بیشتر داشته باشد.
لطفاً تست کنید و نتیجه، خطاها و پیشنهادهای خودتان را برای ما بفرستید تا نسخه‌های بعدی سریع‌تر و پایدارتر شوند.
Powered by WhiteDNS
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/2932" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">از ساعتی پیش دیتاسنتر های حوزه هاستینگ مخصوصا ایپی های وایت  دچار قطعی شده اند ، معلوم نیست دقیقا چه خبره
اپدیت :
سرویس cdn های ایرانی هم قطع شدند</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/2930" target="_blank">📅 13:39 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تو با این حرفت داری میگی همه دزدن و سوادی ندارن!</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/2929" target="_blank">📅 12:01 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">پول به "شکن" و امثالهم هم ندید. یادآوری کنم که چند هفته پیش، به مدت دو سه روز chatgpt روش باز شد و ملت کلی اشتراک خریدن و روش کانفیگ ساختن و باز مسدود شد. پول مردم هم رفت سطل آشغال</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/2928" target="_blank">📅 11:57 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">متین خدایی بگو چرا گفتی خفن تر شده چیش تغییر کرده</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/2927" target="_blank">📅 11:55 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کسی تونست اوکی بشه آموزششو بزاره</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/2926" target="_blank">📅 11:54 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نسخه‌ی جدید https://github.com/therealaleph/MasterHttpRelayVPN-RUST رو حتما امتحان کنید. خیلی خفن‌تر شده و میتونید روی اندروید هم وصل بشید(اما با ip ایران خودتون)</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/2925" target="_blank">📅 11:53 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2924">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نسخه‌ی جدید https://github.com/therealaleph/MasterHttpRelayVPN-RUST رو حتما امتحان کنید. خیلی خفن‌تر شده و میتونید روی اندروید هم وصل بشید(اما با ip ایران خودتون)</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/2924" target="_blank">📅 11:44 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نسخه‌ی جدید
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
رو حتما امتحان کنید.
خیلی خفن‌تر شده
و میتونید روی اندروید هم وصل بشید(اما با ip ایران خودتون)</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/2923" target="_blank">📅 11:43 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2922">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🗣️
سوالات رایج شما راجع به متد MHR-CFW :
1.
متد بار اول پینگ داد بارهای بعد نداد
🔺
ممکنه مشکل از پایتون یا تموم شدم ریکوئست‌هاتون باشه. باید لاگ cmd رو چک کنید
2.
راجع به نصب سرایفیکیت روی ایفون لطف کنید روش mhrcfw که بتونیم نت لپ تاپ رو روی گوشی هم داشته باشیم
🔺
راجع به آیفون پیام
این دوستمون
رو بخونید
3.
من بدون هیچ مشکلی وصلم همه چی کار میکنه وقتی  میخوام اینستا لاگین کنم همش چک باکس نات ربات میاد هرجوری تکمیل کنم دوباره میاد
🔺
بخاطر آیپی کلودفلر هست، اگر از قبل لاگین نباشید تو اینستا نمیتونید کاریش کنید
5.
سرعت خیلی ضعیف نسبت به mhr
درحدی که صفحه گوگل هم به سختی میاره
🔺
دوباره دیپلوی کنید
7.
برای من پینگ نمیده و وصل نمیشه
🔺
حتی اگر اکانتتون مسدود شده باشه هم باید پینگ بده، یا یجایی از کد رو اشتباه زدین یا کتابخونه‌هاتون درست نصب نشده
❗
درنهایت، سوالاتی که بهش پاسخ داده نشده توی ویدیو توضیحش هست، لطفا یکبار ویدیو رو کامل ببینید و به جزئیات در هر مرحله توجه کنید
لینک این پست رو سیو کنید؛ اگر به سوال جدیدی پاسخ داده بشه توی همین پست گذاشته میشه</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/2922" target="_blank">📅 17:38 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2921">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKeeling Gunner</strong></div>
<div class="tg-text">- وقتی دیپلوی کردین بهتون یک لینک میده، حتما روی آن کلیک کنید تا باز بشه، اگر ازتون پرمیژن خواست بدین. اگر بوک مارک کنید و گاها بهش سر بزنید هم بهتره.
- در گوگل درایو sign in کنید و پرمیژن بدین.
- یوتیوب را با مرورگری برید که به گوگل sign in کرده.
- حتما مطمئن بشین که سرتیفیکیت نصب باشه (هرچند برای من در اندروید نصبه اما بازم کار نمیکنه)</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/2921" target="_blank">📅 02:02 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2920">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">من این مشکلو دارم که میام طبق ویدیو نت رو share کنم روی گوشیم با اینکه لاگ میندازه تو ترمینال ولی چیزی باز نمیشه و تغییر نمیکنه تو گوشی فقط انگار وصل میشه
🙁
تو pc راحت و با سرعت وصله</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/2920" target="_blank">📅 01:58 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2919">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یکی از بچه‌ها
این رو گفته بودش. چک کنید و نتیجه رو بهم بگید:
دوستانی که مشکل 502 دارن راه حلش اینه:
برید داخل فایل کانفیگ (نه config example پشت سیستم نیستم اسم دقیقش رو یادم نیست) و مقدار auth_key رو درست وارد کنین، همونی رو وارد کنین که توی کانفیگ که توی گوگل اسکریپت وارد کردین.
ظاهرا cmd موقع گرفتن دیتای اولیه مقدار auth_key رو درست نمیذاره، اینو بعدا باید به سازنده بگیم درستش کنه. کسایی که اپ terminal نصب دارن مثل متین به این مشکل نمیخورن.</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/MatinSenPaii/2919" target="_blank">📅 01:55 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2918">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اپ بدون ارور هم ران میشه
اما هیچی باز نمیشه</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/2918" target="_blank">📅 22:23 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2917">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">☠️
آموزش جامع ساخت فیلترشکن شخصی رایگان با گوگل و کلودفلر، متد MHR-CFW  لینک پروژه‌ی اصلی: https://github.com/denuitt1/mhr-cfw  توی این ویدئو قدم به قدم از پایه‌ای ترین نقطه شروع میکنیم و متد mhr-cfw رو پیاده‌سازیش میکنیم
⭐️
آموزش کامل نصب پایتون و پیش‌نیاز‌ها…</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/2917" target="_blank">📅 21:39 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2916">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B5Iw6uGafNZlmv4QCWr_b59T34oz9Mz8YQZk5y0FAXJ_WaJsj6J6KZkNv2Y63qGHLiBMP6Bk6E_F7CPqgflgqiZLBMbjiqhA5fVfWBJmLvU6RfqjILtxSQadTI3p3_6GgekQSR5m2LdJUFhi3RokLwi5a9DUH5xLXMClxR1sE-EjO4HyOV0BTe-aZ7btlYfH1QfRuxlBGAPR2x2PkDUjNCx7RUyh6lCRFx7JXokvOpTGupXb1HW6fbahfrOXO-Eviftr9ASip4Ll3jnnMQi4tGrSaph6t2QnkHCkgw1AHTBAhuP98klcu3hR1fx4sDkcHdbEyqrU9zFOHI-NxZG-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">11 عدد IP وایت، پشت Cloudfront آمازون</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/2916" target="_blank">📅 17:22 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2915">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">طولانی‌ترین ویدئوی کانال شد واقعا اعصاب و انرژی و حوصله برد ازم. تمام تلاشم رو کردم جوری توضیح بدم که اگر یکی بود حتی cmd رو یه بار هم باز نکرده بود بتونه انجام بده. با تشکر از تمام دوستانی که برای آپلود ویدئو کانفیگ و برای نت داخلی هاست در اختیارم گذاشتن
❤️</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/MatinSenPaii/2915" target="_blank">📅 04:36 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوستان من اینو روی code.gs از یه ریپازتوری دیگه وصل کردم و اصلا به کلودفلرم وصل نیست ولی داره کار میکنه کلودفلر چیکار میکنه دقیقا؟</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/2914" target="_blank">📅 04:32 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QCk49aR8Eq3nOYwpstN-eqYeluQKH0oo3iahBk4Uh9og0y8r9zicu6T-0imDM2EAvDGD6-puq5SMmflzjXx_4OrRBlAQDLG609ypJUCsf20Q_ISkxjEZP7CiuPG0kVZsDuCEcVlor4SzMqEY559PaOdij2QeP1gRrDqA_yZpx8sngh70IdNLwye_7732v0yBMim5ozY48suyYcWq0Yw5xrfJ1f_Aa_NgisRUbkZa594UQ72iaroS04NgO0-YjR9SceuA-UZRnCG8TaitB8WKItUztQ0inHiaDrozN_nMbU_kILJFFDiQWV1WAfRFvzJTSzcDARu4-ECCOnzIzT4HJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش جامع ساخت فیلترشکن شخصی رایگان با گوگل و کلودفلر، متد MHR-CFW  لینک پروژه‌ی اصلی: https://github.com/denuitt1/mhr-cfw  توی این ویدئو قدم به قدم از پایه‌ای ترین نقطه شروع میکنیم و متد mhr-cfw رو پیاده‌سازیش میکنیم
⭐️
آموزش کامل نصب پایتون و پیش‌نیاز‌ها…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/2913" target="_blank">📅 04:31 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">mhr-cfw-2.0.0.zip</div>
  <div class="tg-doc-extra">75.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/2912" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک پروژه‌ی اصلی:
github.com/denuitt1/mhr-cfw
لینک سایت گوگل اسکریپت:
script.google.com
لینک سایت کلودفلر:
dash.cloudflare.com
لینک سایت پایتون:
python.org</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/MatinSenPaii/2912" target="_blank">📅 04:12 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">☠️
آموزش جامع ساخت فیلترشکن شخصی رایگان با گوگل و کلودفلر، متد MHR-CFW
لینک پروژه‌ی اصلی:
https://github.com/denuitt1/mhr-cfw
توی این ویدئو قدم به قدم از پایه‌ای ترین نقطه شروع میکنیم و متد mhr-cfw رو پیاده‌سازیش میکنیم
⭐️
آموزش کامل نصب پایتون و پیش‌نیاز‌ها به علاوه اکانت گوگل اسکریپت و کلودفلر
⭐️
آموزش استفاده از انواع هوش مصنوعی‌ها از جمله Gemini
⭐️
توضیح ارور 502 و مشکل لود نشدن ویدئوی یوتوب
🚀
لینک‌های دانلود با نت داخلی:
https://nc.thearthur.ir/s/YaCp4zAzepHJKi2
دانلود ویدئو با کیفیت اصلی(400 مگابایت)
https://nc.thearthur.ir/s/oPg4gAqtFd8zBFd
فایل پروژه
https://nc.thearthur.ir/s/xJdfE6BeYEQA4s5
فایل نرم‌افزار V2rayN دسکتاپ، ویندوز 64 بیت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/MatinSenPaii/2911" target="_blank">📅 04:12 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YaTiZoyoCEQzchcelOf7vNTaGTUwacGJCNb_fGgm5nVGWD0jlUaIZOIrTGm53X66SDDalJgnjZCABlH90eH93zPJRO8tTf62Z3lKgM98Z9zMKA9ggxbDgRZwVQdSDlomZ2XpACjisk6DAtB51_yQ3hrgojAXfoMsW9INh4HFrKlRSH01E_lzESDnjxO_mlTUGZ8gYNpSCkriMA8OBSLQIHP9gbSLW8NnfSwpGXWEI_u9KBVjlS6Mr9kWNCbyJupENOyCLqowjzbddlH99DHNEAZLPnUmGYXfcj3Kmjs6PSPVqrX8eDNc-Bi2Gg_EGssyLxx9UEUgglTu30fobOdWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، روش لود کردن جمنای رو هم واستون پیدا کردم:) که به ارور Unusual traffic گوگل نخورین</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/MatinSenPaii/2910" target="_blank">📅 01:21 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2909">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه دور کامل از صفر آموزش نصب پایتون هم می‌ذارم واستون</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/MatinSenPaii/2909" target="_blank">📅 01:10 · 11 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
