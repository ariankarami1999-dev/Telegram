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
<img src="https://cdn4.telesco.pe/file/pMrgRbT3mgH68o5QK7N0rlCkGX5a4mxeDZgpZSTs5zhOn-cUoLRMrvPpUd9tNWuu6r_LgEF7J0yYGPo_8LZb7jbn9RztzGPE9P3LCFPzVzgHkIwxbxe3Dv5xlnHjT1p0gGWcoSPO-MaFd1KH4FqeM6j9usksFrIAKCn56KIBdMQTJAhJ-ddmfH78cBlrbjJSsbNVPBTZIo3UhRk5GUol17a9uI-NTX3-Ooi9UOZf2MZPPAeDm-4eyEJi-KVEhtOfrF2VoKqvvFsWgtW5grP26lwakyuRO5QD3D4Yi3HV_VOL4kYA2qWsdq_AbV5CPoPlsXSlaJ1MpvpI7rhj1pUsNQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 507K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 04:24:08</div>
<hr>

<div class="tg-post" id="msg-29853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29853" target="_blank">📅 02:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=kiX87__m3doVE42jSGJi0WI9VAUuErxZxNfp8dETTy32ZouY3vuNRRx9HtDZzJLSVJpHfb0K9Ttbtfycw96iNlYnYOnQ5QRBRlMXJy3HTJS9Sj3ocAd_UPaQR979YqH7679IpjAvNOQUjb3HR9VP21B_xjnkemRCwoxAm5si2SmG0jYMN-7XUulAdLAsIE-3iEXkwGzhPcMZOQCwUyvDTtMbgJbhuHYn5Tp2SiPFsBmtSxe3bKODoP6NUZF3PDXFgfFfT2xaoietlYE4dVJBVGgKiBRJgqcVYyeYetZRXmGbiaj0OBS1gAVLPX72QOWn95LcZwzgTAUk9b0jjwQCXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛ صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/29852" target="_blank">📅 01:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29850">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBdJGP1Wfq1vmsMHEZIYOaDeJmZD2sLOsgUXKLbGGMHEw0RGHG4BWtf3AVDw3K4tTBJQZE4FRx46DWFsdRAsYfdj1AIE6SgawgbMxsdYpytO_lw4LnMgDdQ4oOmZz-W5zg0M4POHp3-VUkH9N8d3wxMHfwWQ9POvWPohWMnSUEFDVmQ8N-yRImIHM4oAUAK8iCTkNy-8i9cAABFnYoV6iifagN7z1GO7yQ9HCv5z1-T0wazRPinUJLMkoWAgFoEsU73ZT3wcLVzAaOkUha7d5Wx-RdbG3e8Fo8QldTaGWCLav1sHWXkaohfeD-JzzOf26zpOcDysJZE3-fbO-pQ1TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ از دوئل یونایتدی‌ها با تیم آماده برایتون تا جدال بارساییا با تیم تازه وارد لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/29850" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29849">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeoIi57ehT8BpiOSLCOXU3wGISM52GrXYlyCbzFax3WzZ3nEs1lglW6fEm1HA0wJzFNpPIo5oXUt7EyzZqSIcm-qLAXvCeCrru4bzaauxec8Lpq9mKdlw0zDLB6tYkD1zKV3-GOPggmG8lwVibvQ3oEn07VVVKmq1I8UXutyEyx81ryfvqi_J3iRAq3-QM9dvG_c49lq7GPfEEcx72hl3afMJsEJta5kSO1FezQt2sqzeIj-oZY4RyA8twPFkSPtMnqfSn2RSHMnqCjx7KkLm4sUpa_cZP57v7HfTipXp51MIeHPsFpeGXMz_KTbThFZ5x441RWrnJeLl9B57rb3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
رستگاری‌رئالی‌هاباگل اسپی و پیروزی غیرمنتظره العین در جدال با یاران رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/29849" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyF_zQI9V84-3lDeAMkPUssu2bG5ZArJRQDl3cWU7sR_TLfi_crl3khADLs27S1T3C4hpLKjD3bJ_scLwomgD1xjsb4HlF6MBdE7h0LSHDuVBnu5SprDyAov9KQJ93UpjQCg3_Tazsg9uO7HXtHzvhbZrwl6sRMzncY1an3kMBGj-R-sqUDOxmogxptEfqR6564_B_e4oXK_nTnXLUVpaOKSHY3vkaF2Z3fkRiZcOpQLPk1XYLgcuOlLWCIn0U4Uo1xhJefNFTIiZiIDcISGViqdEL2HBbdt1WPILQV8TdSpFeMOR-dEHBho8V1tBoy587JTfwux8dal-KmQR4uizA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💎
🤩
روزهیجان کازینوبا
🤩
🤩
🤩
بانس
شنبه،دوشنبه،چهارشنبه وجمعه
🔔
ویژه پروایدر Playson
🎮
بیش از هزاران بازی محبوب اسلات
🆕
متدهای پرداختی ریالی و دلاری اتوماتیک
💵
🤩
🤩
🤩
بانس جبران خسارت بازی‌های کازینو
🧬
ورود به دنیای کازینو با هدیه‌ای ویژه
همین حالا ثبت‌ نام کنید و برای
🤩
واریز اول از بانس خوش‌آمدگویی کازینویی تاسقف
🤩
🤩
🤩
میلیون ریال بهره‌مند شوید
🔝
فرصت‌های جذاب در انتظار شماست
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
P24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/persiana_Soccer/29847" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCimgnv-UdOjxeBCN1JCFGQPM7mcMtng3yzhwqGaeTg8RbbrnOqyq4WG1dZPuvtmoVUu1mbF0NovfOETSA5apfLXgbDEnG_BfwB52MK60B91Dql36ebKPcl8PI2RZs7eCK9nuA76rSkWdWYMGEvg9k2XJrFMZ3Eyn7tNIV6kwWbKEfiYdk-WHTmsrNhdJ6CV4uXqc06ZEXctvCUA9HwhGa8R9EK_0SdY7s_bflgKli_Nmz_5Z01RBHM9Rx2QETwnqw5o3qqt-g-12HfFNaes278P2RsJHycIU65gngai9DHhc4OEjTuWjyHJSbhmCQIACd5ZDLLr2aM9vgIkvnVXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ مهدی تارتار سرمربی پرسپولیس امشب موافقت خود را باجذب بشار رسن هافبک عراقی 29 ساله پاختاکور ازبکستان به‌مدیرعامل‌سرخ‌ها اعلام‌کرده. بدین ترتیب پیمان حدادی بزودی مذاکرات رسمی خود را با ستاره سابق پرسپولیس برای بازگشت…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/29846" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw57bTXuAjElbw1gDPF-xO8GSiS_2_jZ2qgGon4aiRO87oDahMxVp8iOh6UXxxrEsPYlM-tJKAuTajpPPA34B9inkjG-4PK8rRUREMWwzlO2Z1C76F-mGYG-U_uzrz9N9R69A9qqXa3N5_TXwOzJo53ahBFtDQGyPLyiqSVPdTUw0BzgMBLqWBm9PDyMWfOrlmVbivIws-RTGbM-8M9nK28xEjq73EzHjL0aFrBws-P8MnMnkmfZO0F0pSeo6eZ563IhuTlWYW9Da07QI3csCwc88lEYY5IiIIN0wcbwyqmoc241LE6naoNXLFqTyOHmMwpsjz8QDZECjoAQkBhu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس تا اواسط هفته‌آینده پاسخ نهایی خود درخصوص جذب احتمالی بشار رسن هافبک‌ عراقی در نیم‌فصل خواهد داد. پاسخ تارتار مثبت باشد بشار رسن به پرسپولیس بازخواهدگشت و مارکوباکیچ و دنیل‌گرا جدامیشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/29845" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_02RzcWOdTTAeDb1Cx_t-DaeLb1GiuUcP72CyfiyH1a6yPbjK_d3lQW5wY4-LGQyPXe4hS0psZJbNH_16EdcJw9H8CNtnM-TlOOpzdsL4F0ZMQ3SJ0eNUgb8V2CHLolKiGfhsWEtMPrszLZNSP6kgvOJagpUlBCmROMmBttB5mY6HV_sUtYlIAbn_wklHLVbx733VbbZnG2mtQzBfPOVjGQXAilOqPcn0aRyA1z_TcQy8YlkBJoegd54dvfRQjHIUtlQvaBL_iPAbheGEgX0ILmeT5wKMzFclYDG1ffbf8PWA1JCngdOHWS-cVl6G1jtwRy6932MAaf8rc5-wWpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/29844" target="_blank">📅 00:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L68F1F5JF6moj64ueQiw7_99oqa6BJ3LqL5mWTnghco3sfjk-v9XtkcsIJ91Jf4sEZSIPJnVjy7kw7GGNch6a9yIlSE1FCClJtUycpkFobarmAdbRhmF_1Vao3MYfNFQ0KtGsuLURfy7wjI5-X7rltNg7h_TcGDENTGfxL45CZpTgA-2p80jrX2SvmAZNEmF6SuoUDoDXph_KpNgFPG2Pxfk6T_lwV45k7sJ0prIeUOTKU1d3UwbyxYf_fWM4_opwnWR3O0OWBoLPWlDCUYkuC2Q8EVDlVptxA1pgmqOsstQ5w8nyIF1RjX-gCZvGU0jZSCCP7c2NHpS7dZIWzx2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/29842" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29840">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHVRRl-wM629S_BG_8PynuMAox2cbPgHVfaGg1NR8UA0hhZdDfyyBN2YPQSh5PyCEDZtHUpjHeD_k5cunnYyD6o-lFdEPcFO82M0GoJwZMT-2SbmYE0kWGyHVFM3euHE1LEjqfGcddTv9Jxugoty9VRupjFzq97mUqP40a9U7-fI3GLTzbrkZDNx2InTVFGph6OrdAdc0SoBcUPrPOEFY1L5vI7o4V3nqIK8NpFeMySu83pCw_xj5e-lt0PQvXM_AXdedia3HjhyWbMocHbx-_Gn4U-xa8jaw4gHZcgQAg32fccxY7wwPlLlwbXDdVcUIXFhL6roshMuLhwv44NwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auEbOyAwVUake6hHYQg4XStpQWvIYCGhVGPTov0LSnjaX-gVh0kA4wfNfZgT5b_R9KNQ4ZRIKmcfn4hHqNzQ0bh8yTsBx96hdc6qR8hZdsA3Pn5g-psSPK1NWVefMJ5FLzWUmnHS6v5pjU4ab3qpUsnZDkJyGkyLktTQObOTm5CZbWlX-zEounTO5-OpXNKbuPdJHBGOjVJgLzz6xXwqGl6p5aqfehv7sTHiP4jG3BSw_3mx-ejTqGJOqknvOGoxm90ipPibGNTWEfijC2hyvVmA9HcW5SPa-s5jIALleH3i_Yx8UmFeiZ-C1ud6E1UlSmJIuH8DaPhVxWeXkn2lkw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛
صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/29840" target="_blank">📅 00:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29839">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqvu3uKK6JT4TvlJISi-XktZeXtzB8SznIqBgCrGXZmPk6AmwRY-4gefUx1wKq_HzYgOo1SRLH_Upw40gGp-1h9ESnAzp06jq5zH0reAxfejbrlOjnSdPKOCI2_0CxjTGIQjibto-KqxenqHDq_ZuYmQEMeTgEJ2Tp8VGoK3OaPVleXuZSLwqULOKW17C1lb_bCepBbP0wM95ubddapkGM9ypy0jOcBGMUlzUJA4F16SFCwFZb9p5kCp6KQjm1vvSzI45QTQu4rEnda34EeciMyNRvWva01UCWSc47spMrb12whQIGUam11vZOcKHMni3uoL-mvCLA3OPt96ibKtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/29839" target="_blank">📅 00:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29838">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T5Wr8zXnIFsI_aUQghsyOcTOICHgqn_YyaqqtFkk8JWiRvaDalEvxKubIa_BDamdGImsLh3GJkq5J897npVRcot93tPTe8OFL4SkdJTDdvh6w7_MfEtcAzpwIG1mTXSgzt2affXOV4BrqxAmxMYHQH7A88mO5PkiLBttribBPmRJJ11tNyhWcOpIl5j2xyx7KbGy2pmhCitZLRIK3knx2Uoy--P7pOzpndfgTcssShpTnZ2IF9xdB5ozlIuHhS9ndzfJPnvdlA64VrNLD_0Yw_ewDzIlFIR0GmsYw4UOu9_nenHZs6rAKdsuj8ssgfoPXnF_GTYPAuwKyST5GqU1xJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=nEshzW8nCHauffLtHciL3ISpSIDUN0lm80KeSR1AkNHEueBtaCBVFFr4ZXzlVyVBebOjv0hNq5tHDRj-IIpER8SVqxBnEr3jXCr-dN21_GqlYi2tOf41QiHoTRJP7UeQd48qJX3H2TVJ38IqrLV6OI3h4SjEzgTgOlJL4fDX9y-nfttm6ls1ZOKwd4OYN_VEcSiUL7R8BmkWMCs6Ifkh5_sfonNAf46CO9mdI7xsrrZUX3dvtSI88MrI6JQ5W0uCD368MSxM1FLpBHM8Yop5cDppFamFNvmcp1Crib5fO_toV7obOF2I0CEEMiIPT98O_KKdehW9ZRWthwz7fZl0T5Wr8zXnIFsI_aUQghsyOcTOICHgqn_YyaqqtFkk8JWiRvaDalEvxKubIa_BDamdGImsLh3GJkq5J897npVRcot93tPTe8OFL4SkdJTDdvh6w7_MfEtcAzpwIG1mTXSgzt2affXOV4BrqxAmxMYHQH7A88mO5PkiLBttribBPmRJJ11tNyhWcOpIl5j2xyx7KbGy2pmhCitZLRIK3knx2Uoy--P7pOzpndfgTcssShpTnZ2IF9xdB5ozlIuHhS9ndzfJPnvdlA64VrNLD_0Yw_ewDzIlFIR0GmsYw4UOu9_nenHZs6rAKdsuj8ssgfoPXnF_GTYPAuwKyST5GqU1xJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه‌برنامه‌اینترنتی شب گذشته لیگ نخبگان؛
محمود فکری کارشناس‌بازی بود. مجریان برنامه 500 بار "حاج محمود" او رو صدا زدند اونم کیف میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/29838" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29837">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5vk123rSQBrqWjpFt5cjs21JVG8E77z6oTY7-9QBETAcQehfS8MBtHOsnXfQ-2KUduvlAN2B-um4uXFuU-cu4NOY08-5qH7CMrDd2iyB764f4mDVw5Sx_VdLSqC7B62Q7Q81IQjyN8sRH_fqwxMphAb8Atk1-Cbo7mrvZKmqs_qLj-qkxPTrxtmfQyV6IfjQwwgg4fY58-iw0K5mfjUfTa5Hhsa35C1oD3XMx2nUULCdE0UBo5wdoKIFrO1aNrl_QE9JE2YG4YPpyyKW8UH_QUTcuh92Ik1KANYqpzkqCrfqa9wvBcrw8SIVrOAjF-CRhh5s6k3grPqU_4Rfn_AFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رونالدو امشب‌توبازی با‌العین اعصاب نداشت، مدافع العین هم خودش رو چسپوند بهش اونم این حرکت رو روش پیاده کرد. 4 تا زدین ولکن دیگه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/29837" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29836">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h-JMvii-CtokTdQntHbB5nien3fvoWukgp8aoXsaxBRW-wbBn3HSlCsO7T_XzjkE-tl0Y6Le2uSRlaDaRrsjslBZL4zYPbsM6evgEfj7sUzEQqbiJiY7U0vj6BCdckFZN2Si1i1G4e6zu0wubg0bfmNsuGwP0Gwd9gIcTWCpSDC65BSyp7YBKlXgdoPsTKLbmVfRNVpNqMsANGVgrp18APU1yX93JGvqvlsXT3mDCFRGoLUhbwNU0cHTkDpsCY_mpUGf-sAdjgDE8EqzzyAatfQlOYIMUAX1E-8bHO4kNyIjeq7e9WO_Uc8yNcA6ka0fWDujBq7zcbxypOUhIcce8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h-JMvii-CtokTdQntHbB5nien3fvoWukgp8aoXsaxBRW-wbBn3HSlCsO7T_XzjkE-tl0Y6Le2uSRlaDaRrsjslBZL4zYPbsM6evgEfj7sUzEQqbiJiY7U0vj6BCdckFZN2Si1i1G4e6zu0wubg0bfmNsuGwP0Gwd9gIcTWCpSDC65BSyp7YBKlXgdoPsTKLbmVfRNVpNqMsANGVgrp18APU1yX93JGvqvlsXT3mDCFRGoLUhbwNU0cHTkDpsCY_mpUGf-sAdjgDE8EqzzyAatfQlOYIMUAX1E-8bHO4kNyIjeq7e9WO_Uc8yNcA6ka0fWDujBq7zcbxypOUhIcce8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/29836" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29835">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=GEYd0SI8k6nUlVwbAExMV5taZN8TLnmbuuqkp3B5KbmQsmcYVMqwXnRs_9OvriciEYGY-hMn_XE1ZLVdm86Yp1sECRswYLxO7s0fCeMeDodM0CgC0zEYwlN8aS00dLmEoaHqR7R3nAFC-3tdQxYS2SKCWb_AGYlRqK868qoGtiAx7BFY4w4A6q49EktWStfGjPPR2PUusQcYGmp3Flxm-e5muhfgkOj-tBbnJw_J_99xBYJhzsfw55n75C06cXsHIxql1Aj7GkMBkhe3El9Uz_Cqqwjr_c1EyCEwAqfSnq0fzRgdgHbWiZNWvbiB4_rfrsv9OZB1WFT45zhfWLOo56j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=GEYd0SI8k6nUlVwbAExMV5taZN8TLnmbuuqkp3B5KbmQsmcYVMqwXnRs_9OvriciEYGY-hMn_XE1ZLVdm86Yp1sECRswYLxO7s0fCeMeDodM0CgC0zEYwlN8aS00dLmEoaHqR7R3nAFC-3tdQxYS2SKCWb_AGYlRqK868qoGtiAx7BFY4w4A6q49EktWStfGjPPR2PUusQcYGmp3Flxm-e5muhfgkOj-tBbnJw_J_99xBYJhzsfw55n75C06cXsHIxql1Aj7GkMBkhe3El9Uz_Cqqwjr_c1EyCEwAqfSnq0fzRgdgHbWiZNWvbiB4_rfrsv9OZB1WFT45zhfWLOo56j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
توضیحات‌مهدی‌زارع ستاره‌جوان پرسپولیس درباره مصدومیت‌عجیبش؛ دیروز  پزشک پرسپولیس خبر داد پای مهدی زارع در تمرین ریکاوری امروز طی برخورد با یک جسم تیز پاره شد که بخیه زدیم. زارع امروز خودش در استروی نوشته پای چپش به شیار تخلیه آب گیر کرده و اصلا هم جدی نیست.…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/29835" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29834">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=VGZooCC4DyoOHstc-kG5QWDZGLTEOJFgZ_xUXjodeTA_NSasdhzGu8d9CBHSxyldWHCTeAoWuV6qI1-iyPXb8sSK3BPL9mvvoYPFYyKFpyC5sz5DovUjORtcG8BP1VQTJuyagfy3gwbEniqWc_5RrUdz-hrf9T4hpp1fNm2i_S5lWMkimCr0xwbX7HqBMTykv2kZtxGJSA_Av2qVyMsJ66fVEWn65KliRjNZLjErLv___hehLwHBL0PRXNALS35ZKoYDlbPRhmB74JytVC9aaM51coAx_to_GqSlkVyHtyl-_35HMux5RUMry-A18eivfO04p6LsbF-AKUx5Q0fUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29834" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29833">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=PGCTHdkU6apsmgyX18_5WTqOBUpDBa4hos5w-8bho6XF1DyOGvHHxQj0XsPdfpVq0zQ7wiOcxqEJX1P7A0XnI3G0_74XsbRER9DPq6OXce6wZBxokZKt41BRDiUTNGWbLTqW_RUOToWfWPd80XTm_6y6RyVD4y-V6FpHl7Pb6X4lAW3wV3cSlZh0foT6tOivn6udrqp8kyjnZVLhK00yeNnpOn1AbiKsyp_5q3iaybtDUMEAdBV-cwNz7mgYuwmA7s7b2KXjJ7H3K9iXNDduFxssk9x1o7D4H0BwfuZhtcLO-8RiaUju8qZ5X3Ch7zPC1JwxqToPU5-Kgx_PlLqVuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=PGCTHdkU6apsmgyX18_5WTqOBUpDBa4hos5w-8bho6XF1DyOGvHHxQj0XsPdfpVq0zQ7wiOcxqEJX1P7A0XnI3G0_74XsbRER9DPq6OXce6wZBxokZKt41BRDiUTNGWbLTqW_RUOToWfWPd80XTm_6y6RyVD4y-V6FpHl7Pb6X4lAW3wV3cSlZh0foT6tOivn6udrqp8kyjnZVLhK00yeNnpOn1AbiKsyp_5q3iaybtDUMEAdBV-cwNz7mgYuwmA7s7b2KXjJ7H3K9iXNDduFxssk9x1o7D4H0BwfuZhtcLO-8RiaUju8qZ5X3Ch7zPC1JwxqToPU5-Kgx_PlLqVuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
درهفته‌اول‌لیگ‌نخبگان‌آسیا؛ العینی‌ها بادرخشش خیره کننده برادران رحیمی توانستند با نتیجه پر گل چهار برصفر یاران کریس رونالدو رو شکست بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/29833" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29832">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRbDTt8IuJ_so9vT1xj1_uSTsxyoE6JNX0CU0EffJvhacqnddblClaiUW2z71tJGPoHZZjgH4zczCWCdvXszVul6QfNtXUesz5woESnOaZHN7zs10PfCOj6C_7nHML_RyEqtK9buvGkaxQg0jPCMWUluYnD_ul00S3euZ-sEgxz4ss6j47xHwcQ8h7wmAOxNCLNVT8chb3HX4YP9SX68A5JQqZImEt5e5eJBLHWc8egkfnh7DbVLUqTKj3YXuzWvbON1unMQrigZT71kB1i7BFZNgsPxhR-R53Ilydxh6CRPpWV62LGSUlWCSwEFIVAP3IQQ7aRQinpCgS0894djOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29832" target="_blank">📅 22:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29831">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3q3t5gFp1i0N_TONPZ19BQh3NRPrQfeV_SRCnzFzzOjxOvlhRswHApMbNWW3UzkeDmQ-8Tg354aBOOZ-Mja3PFO-NT0aBb21FExO36ZQ6AI5CzlI9J6n5t5wvSv6LzqLGR_Eawht_zyC6YD3DuZerbM-ga_e5vxyNvi-WhEIM93WFg_UdcrnkRyKidNtE53y9VZt1AgaKal44g09RV_UZe4nMMo5NhEOdFFkDnDnjKq3j3uqdDLkZY0W4RAAvJAroyXp0HtaGA4w6_F87NnUyEdK9o2mQ-5O7fBkfD1XDId691psEWgNthHAvZAde7DMNKkEHZzERoWm56NkSOljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29831" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29830">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-ZvH2PgOfeJnYJiQZUmYgHhxkwQFpQhQiruTRpd62xs8ZYPVUavdlz0CuDwd-InyetJiKwG1WWwXLYlr5qIbDJb5uTPMEIwnIijUY_LwLK-8D_X4P9gNQ6iV0iCy2w5XwMspYwAkBGpGgkMHWkbStCW30dbwe86_KK6Bb89wTiEjGEa_PUdPjq64r51JA8W_RDM8VcoCYm-cQcJ_XZ-fa9FLwxsHv8xWLyoPlArmsV2IOAR0CZtT35H3W0oTdX2mxiY40q3QGgZqq2CRF-7vGIxdzXpYFVXV1Ed3Bb2Ih7ZCb2rVJUL8yQ2RSArj41Rb8p11HqGS2GcHyZyJ2RTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛
شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام
در سایت میتونید مسابقه بازی
رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/29830" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29829">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvroLRreFCTf6QJvevhvMU8jOr1gwBddhpi-ZsDL3Wee_dR4Ri2QtpFXFf8U-aBMyFjddk0ItDDl6aa9tUvZkGEI_k5FZ8krs2lvFEa8JMxkj6xFxf6m3TY-horxc5OGOS-3zq42IItMMGq0KR2CL9A1U2AhZTMlUOIIhp96--1brp9RSRBR_HhIdFy8oUuIEsU_2Vo8Qyvyqi9eHy2VVRaru5dml9SuL59MyJpBwg86qtD75tB2OFTNJpXARcDiYygtHD_3ly1FUKbn5zzrdp32kH1tWuj3LaILiU3QQC1bHMFAGqFxgFPGCMVLh380bcIuhCAkxypim0EXB8yk8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇨🇴
#تقویم؛دقیقا 11 سال‌پیش درچنین روزی؛ خامس رودریگز فوق‌ستاره‌کلمبیا این گل فوق العاده تماشایی رو در جام جهانی 2014 به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29829" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29828">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29828" target="_blank">📅 21:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29827">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=ImuTia9bklseH29ptesWo2QeJpfQU9lLMTB8ITAYuK8rTcEuhmMdTDQd4-z2UEwp4-T-RjlYWdOcx8c0I_vjeiWT03EJUlLg2z5vqObWLNSXDpOhfWDnBrVD5Saqn8-uSNiFuBQhx3gNMmg4umRwOBYWg9wOPUd9OeGQqjGjm245b_1e3cKV4P1bmbGtU6UOEN11J6u4GQRlTrsVTeTxqrTVuua-mS7EjgqJrmfU8xLbN2OxVHT5liuEKX0dGGcIxVeeyRV2iyyBwa7_1-PTOyvlI1c7pgl6PQ5S4XWYL3WSoLJ5nFukiC--geppjf9UFOc9bpnpEL1WJ_PmjUCiXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=ImuTia9bklseH29ptesWo2QeJpfQU9lLMTB8ITAYuK8rTcEuhmMdTDQd4-z2UEwp4-T-RjlYWdOcx8c0I_vjeiWT03EJUlLg2z5vqObWLNSXDpOhfWDnBrVD5Saqn8-uSNiFuBQhx3gNMmg4umRwOBYWg9wOPUd9OeGQqjGjm245b_1e3cKV4P1bmbGtU6UOEN11J6u4GQRlTrsVTeTxqrTVuua-mS7EjgqJrmfU8xLbN2OxVHT5liuEKX0dGGcIxVeeyRV2iyyBwa7_1-PTOyvlI1c7pgl6PQ5S4XWYL3WSoLJ5nFukiC--geppjf9UFOc9bpnpEL1WJ_PmjUCiXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای‌ایلان‌ماسک:
گوشی‌های هوشمند امروزی تا پنج الی شش سال دیگر کانل ناپدید میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29827" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29826">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_jViPPuef1s9R7j2Ez4xKpgU76kJxhMgflfqDI_sYdjNJXe-99XQxyOmdZH1Tw_Mh8C2pfnad0LMN8xhb_s6GUZ25RnwnwxuUUiFCroMb3ByXO0kCyLgcgLAgP7YLhSFiHFUYSh6q1jEkGt3Rss93gYn_DDZ2F2JEu7ywFaH3KlYx37arBebAvko4FiddtK41Ri8YbHyMRB-YITpQFKOy7gnFIHPN3Auccrim6SFmKSywO72MUXYitwfp6XfyxMh2VU65cqenMAjYh4235LEx6mNR5O1xz3knxRO6u7dWP9EiBfeuu9wO_lpEo13wjlEEQvp37jkq1Ts9BsYe333w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29826" target="_blank">📅 20:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29825">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXbX8auptH-YVzH_hlZzAFQqRDxoQmqTQpjMpOYKpJaw-goU7cW5Oz0tyHh9P5UNGKfKc1Rq_PGTLHxv_lhkVlWr5OZIqdX_sIe7-XWStjHbVTkYh7FmDtk7rjRYdyPvpIOjmJoq_3Bq9HSQDFaGwVyUwF7kfbYTWkVJppJ03wKrWAqfJKuE2RWnmwyEbABQymo6y8f-VL9f0BidN3xVRKVU6U6uohTfX4MCCJCB8UYnaLYVllaGEEseVnPgT8OwAOEI73yt9tECBoXkR0IIm_LqHH1Tlogdtp4_Iee9mRvgy7khHur1etEvx7_SoVrbCCNEb380SGh4FtpGyXZ2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
رودری ستاره30ساله‌جدید بارسلونا:
رد کردن پیشنهادباشگاه‌رئال‌مادرید اصلا برام آسان نبود. بله‌ابتدا درآستانه‌پیوستن به رئال مادرید قرار داشتم اما بعدِصحبت‌هایی‌که با دکو و هانسی فلیک داشتم تصمیم گرفتم به پیشنهاد رئال مادرید پاسخ منفی بدهد و با باشگاه بارسلونا قرارداد امضا کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29825" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29824">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de2283857.mp4?token=L8tU3y7aq9enCunRpJWj24Bgk5n7Kx88xSILYhYlDk1ox2JEwuH0Ry7OGJBXU4CAdSxG4iN5nk6OqpowR69mGKWvfOTPT-AvHQah_myXKsVHnryfXRoijeS3WQshx1qKcjDPSMwDpMq8c6ipkimBNtmncm5CGKnbo49VRLACZ62bavc0GLH6OF9SQXiLFJ2NlS_kCSpz7VAVnoFkRhAIhs5tvErEqPBTopLwHAlYBcu4tCJYBahAprBTMZIA0ON-gi7XuXfgh7_9aKbEUQ2cYbA6LV_lFRZqMJ4nhbMqo3as6nkjvboA8Y4gmYi8JXZ65rxNFi5xWfRUPV1CdkimbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de2283857.mp4?token=L8tU3y7aq9enCunRpJWj24Bgk5n7Kx88xSILYhYlDk1ox2JEwuH0Ry7OGJBXU4CAdSxG4iN5nk6OqpowR69mGKWvfOTPT-AvHQah_myXKsVHnryfXRoijeS3WQshx1qKcjDPSMwDpMq8c6ipkimBNtmncm5CGKnbo49VRLACZ62bavc0GLH6OF9SQXiLFJ2NlS_kCSpz7VAVnoFkRhAIhs5tvErEqPBTopLwHAlYBcu4tCJYBahAprBTMZIA0ON-gi7XuXfgh7_9aKbEUQ2cYbA6LV_lFRZqMJ4nhbMqo3as6nkjvboA8Y4gmYi8JXZ65rxNFi5xWfRUPV1CdkimbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی‌از عملکرد خیره کننده جیجی گابریل ستاره 15 ساله تیم منچستریونایتد در فصل گذشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29824" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29823">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLg4Sx2WuGVPDL4ZhAACjCcs985un_6A0NkjfLpOtH5GmyTJJBU8bqI3dSpr0-1z3iC5i4tgSWWhg9JdpEr2M7hhxH9ZYPl__BAaiwp11R_oHf04inX1EEWv5XWPo7ZafH2Fpc2CfX9dlNaYw62idkKSM-sgFP5Byupruh5p5KajegVSbDorKg8PX7-BGwbQBXeMl-gSY8qpa3iHR9m5J_77-b3PH_TPiNj_0EZZFQCrxxBRLU16kP7vN3txrvO14fcG-Dgwv58t3wpp0f02wC2aze8KluMQi8Xl2ihmyg584vmNKot5XRMjYGwoWPRSKWwSjTEHJdJ4_MH1oamcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق به ثبت 27 گل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29823" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29822">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGs9GBOy-UFEPuScC5Ks8KpGAL2yBay44i4zTj-JFrBhI9OnusGVBpK2mRURuZU6TuRec-255X607tYKVAOVEklqHO707fHbpfUT01NYaKJ-iVBp7wfVFwbCG82BoqvqghDIs_jXoQPEs-mLexIwd-EEmUpYZxTCMy5238qvHB7jJ8jAuNr4dJXGEpQU_K4-nKAReVileHw-IIErHl2YffVp3wAb6_GXe93Wij-nRsj5_Pe8FCNRQT-6SX_-FGbDBBWdRCtL4iUEsDYZ6S-tr6nYfXLGynjEzeuOfZ3AOiFUY10DGZ6hT3A6K0aBimie0fsaSCi0bEJfmJha9U41Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29822" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29821">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8dtSNYSh4IsRQdhLQ111RnFYyg9GhaZYvNo3AVgKmWiE5tQfLnepltQ0IwiTJqs5Ku9VWBh_uEEWtBCay4f5xeScPyTD5CYJM4UOEtLcFKZQeIzp0tMT30qbS9HUnIPgvuEaB7WjlBJuvMBiB4fxOvF8dcIl9C_AlB-zB8c3nBUMMHfvCQRF4GIrPbSwzWxwPd7G4vkKj3NKUm7xdBRzNTvU0RqHwbKKJEqptq8y0txPIWmXd9hJO8WQS4PQqnDJCV9q8t_GByEUiM27MaoHy5QtyiIzdIcnf2r2kOPKBh2qMXUJClg25ImYS62ykVYHRPvYQ1B9nPG0gLj_m7UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/29821" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29820">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29820" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29819">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_YagaCaOk3TeDMQHCNLxw7eTQyZJboSICWZ-eOTmxhvZ-LkedkmuWposG3BXqpjovC4XJlARqc148pGk6bdSdHD12e-3i9vQ0uwNPOzj4uwftdJ7SeyklEQ1J9qbyL2qgc8biUg-bgksQ3HJCI0gKlWO3ivKMox4r4Qe3gqRhP5OY2tO42gh3sHRCiVm6TtrhqB8JmbnbF2nm13qsGWLFIwolJs7emN8UN-F48txzpE-YA4wkjFPdzOM7BnK7HmyEUvqRtYkvd3GnCEIb93PiqVoWYoiHJi9NLYOHx4850qYRq49Mg05UPGEk0tlEuJOfVn9H3YrOgMFfBsECyXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
الچه
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29819" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29818">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3gZbnWyDOvmF2hW86_9cw3Zbs4ztmafpYnQwPUfKSauOWk50Q6_yh_rjPAfqGeSaJq3cGpjvOjp0UAMGBiVjx1X53fbskpNdpXtbTorTD3pwd7jP0s7-9grvMiimQGlwHdl2U21JAWWjm1SPLUDBT-5_G-4fIRF-OQKdB83f-b0wq3166POdlp3nCZNJju8CEpr6AlnxPVb4haqSa8fvpHrp0jQlhVcJOLF6FhaqT1HnnRlkLWbBoJj0rD5AtUTVsOzl2s7rjrUImLLaaai31uUuKnkrkoPUMopVy7qiZDPcvTiSpY8BFG3_xwsjYE0wFRRRiSfLHx5AnM2JFAb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29818" target="_blank">📅 19:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29817">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmFIWl8Q27AlHsjJmSPy2KSN-R-4CpFA8sM5PtZD6gGd1xRUN_t98LIS_wctd67mw96VCHEYS9_nDKCttsSSeZgmt2-sTpXxEgky3avE-RhHbAcw5WpgZAQ47-6fMxzh8H4e8ETX9173QQXE59RQ7blaETqwX_VX8qu1D0MvKk10eVA-1mb5C6AzwywOJYyQ_km6_P_xlP9SdBhue2aArgXWV38610T9I8giW8JCT0jJ2iErJ0ctYvIaClmUbKHfIyrS0v_onPgR0b6-0fH_5OPM4blGm3IlLwmYGVodFEodGOXPBxK44TPBOWnmjPmihjvb1MSCphS5qoqIx2AE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29817" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29816">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf-egeZeABpSkupE6yRcV0ZiIwJZEssD4ovQxPEW1_0Oj0J2TNUHw_vHhHcbHPkBbG-DlUs85SpwZ2zpr4QtlugDRd7Cg8_vJqO5FeY8D4HyhTCXjCK-7rjSgnict9jInVC9Bw7modJyvCMx5svlMXtRYlQrsUmIvEoCjIGOScciUYmrUEC7sZF0iX2ab3sXfZ1CQQhjRvpwYI1UPlUhC_oS8_zyIWByWvJ9UqS72xFnKHZha6kNA88N-47OXYc_n7GZ0PAcv8_Awzfn9Q9AgG17KquUa6qZdDJYiZ_3FE0xSlKni_e3US3RkezdFWvKmQq8avtefnF5Nf8_b8s6yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29816" target="_blank">📅 18:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29815">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9Nn8IB3Uj1FoghQFPJlLhNiqaBoAuWjKKBL4k_EcheMywyAGMRH6GuBLxfoAX9776-MaZyY8nlT8ZN2MdSLv0m6JE0FRN0onUC2R5UCQ6amYbigxuuiYfbaeQ3pqOZwitf25n629Oth8K5S-WLkyXOxHr7MFfI2HsofZWJ_rv7dcYdCFxnaZxSKdAAB8yZj2kcMhJwqciOb1PymlKcWOXsxcBAZXjuVmgmXbIHlcQqxr0XBy7O0L4zOm9_A2h0arCxEKBKLWA1kn9UQanyAkehYV0mXOsBFrP1TKxm7QLSKQId054P8yC5754zyf1k29rAxx0IOOieUlAihwGo5vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29815" target="_blank">📅 17:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29814">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlMzHRvFCmKN-HaQcw52B5JXFUBheHk77rhCYxnoDJusxp3HU7ol-q67CiHkI36CBgc7FZMdcXLt-mXX1JCojy6mw9FcieicBXSHsedMwpepGutYQK--tns3FbpUl6x3yRsdChCUBV0UxNfEfcnKfdP4QS7EoHoMe6EhUnnDa6DOcjnY_obkatvEKZ8FIe2RSeCN7wVfrKBWg2F4kbc4wyQWYjKoIHP9s8S73yCEyYYtncQZNzj8fcss_0OgW-A-0WnFAWFyqd80CYAaLT_4EUBZeSfqW4IijuXjTO6ZJe0eNOXkUipcTs6H1lT36yfWIdxaSBVt75MA25EsEwt4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29814" target="_blank">📅 17:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29813">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okyr2B6VBTDObiVBxbI9sbf57YVWJJGeYTCj1KqcYXTnJc0Vay9vZPggXVxv8EVLqZJ5gh6x4Aj7dKVsnm3xdRp7sjPjMzoSmNwSe-EF17fQUjDZ_Xfx_L92v7vNXUtTCSTRD46pX6vOuhx0JbMAV27RV8zX3kidpUzdJP4HlXPrLk1Zxdi4bxKDVMaGWOI7ByYAVj7pXhkre2ifWneY9FD2CyZLRzwAD6SLA4FZh1ZTXNtDcUxceygUgOWjl39lme88xh9GLKs4CpyNh8lF5RYyOxfmZFjChPeMKVkLdY5HOwKL2fVcU6EINrlt5d4Mrptm_sUhvHt5zAQiBQh5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمپین تبلیغاتی جدید سیدنی سوئینی برای پلتفرم Novig هیت زیادی ازسمت ورزشکارهای زن گرفته اونا میگن این کارهای بانو ورزش زنان رو جنسیتی میکنه و اینجور به نظر میاد که تنها استفاده زنا از ورزش این حرکتای سکسیه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29813" target="_blank">📅 17:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29812">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djYmHS87O8eQmpyt4Bnb38aVDeicOVcX53hgaOWY7n7QcBCi1-s_xTElybShbVNkxMI75fTX0oPBbZ2cx4yQd_9jo7cDUTAS004mOxvIFyAcIOJVX3NZVxDe6BmRwRQjU6Mttl_9kraz8AHf33QZogpki4h5YZbGk-HdbSV-IplzJJR_QhrW-yH8qdChHPuvHw3-ublqHfYxUiOi89WRcu5nTJLVNB7JE0UFDs9c_rN0fILHnfqG_WvQCUAEPg5Hic3eCqsb60gGf7KfxML8jCPNVah8W2pZ9K2H7zONjb-7e7Oa57PWs7CMsja5sdU38Z0j2wI6zUEFJS5asTusvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای تیم امید ایران در مرحله گروهی بازی‌های آسیایی ناگویا 2026؛ فردا اولین بازیمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29812" target="_blank">📅 17:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29811">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsTvD1_JavbiI3vMnnSO3VK1l2Ib9fbJk40AinlmC23jIeJC7pXhKPE1vxDwYRR-Dl-oWCwik1xGlGeuijDcoCe-JBtpxdMk9EcYwn_EiDskAnYkD_K76AF5D7CtZBpOSiOq0xnuHwN9sftG8aHCNdMGzNu82QEfZgOj_i--zwP5KgIspYQXhDnLDgLU1nSvPFiaXMRzgVTbzoMksjLB-Oky4-UOsJP4SbysbBdbsEzU5Na9Ap9wM6O20c69ptFJqLkB2Zn3EI-WzAgU3rT_RIWPRQdZriYPAUWdZVSLroEONk73ao2ZYOhgqjmB25MqZ92YLiezd-sZBmByWlCNGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ویدیویی‌زیبابه‌بهانه خداحافظی مانوئل نویر 40 ساله از بازی‌های ملی. نویر گفته دو سال دیگه کلا از دنیای مستطیل سبز برای همیشه خداحافظی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29811" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29810">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQFxB-RwN4sqe7BRpyYp_QXsk4M-uCwbWmQO8nhD0FDvBPsXX53E5Sju2k5FCxQiZtwSOUWOj-3gEynnCGBwNldjQ4RDiMsoyIUHnG0iiz5qINYHcuq1u0SySv_nblbqY2_rHm0XA-NZb-phog9X3pbUTebeXDvD4WRpT6ZYmmzVVRUj1DMaFKJ3zS8eX66Mj5DGxe7moZDoJyIQG_zTcs6CDFt4dHgUKGaAUXI1fD42i0VZJaEkIpVbPJojxrLTc1MLaWTv-wP_51xJ6UmttOauv1KDBfAqpzJrzG5fOq6onoNojG3w568ojvvTOY633UBzV2lBVJ39rv98RKHqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29810" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29809">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJJfE-C0qsRKaH9CpqyiSJ2eykZRV76-rfL4Qc028DgUdNfGVhHMrzg_cxDOJyhmiRjo4zKqBpivnWP6CgI9gfklpsemusFnIHRzOHc6tUoSMhQv--Q0UdCUOfPG9S5EYykdWVO0FylGQASEAZs2Yk2GcTSZXUBzOPSd-j_idUmJduXpyoo2TjvAmTwVWBlOqSJC96Cr2fqpYRAf3Q8y9jzH-92MRc_4JBJ1MRVaThVqAXYSIUSVU1drDH7ZtY3ZINN8bNVMVVBeEsh6BSvamHjYZQxgh2RhdPHNgrtDpE7s0yg1jTL5Vuu2AVC3Fs9I0_KsiK2VOZnJgjEWg4HfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29809" target="_blank">📅 16:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29808">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep-dV8se2CvvubQQhQ9ub_2-8-43sleOJVvqgPc5Dow9AyCxC4RcndWkIiQavTz2V65UgnvEPm1iWtDzD6tuf5B4rKsFow76CzoBFu_GtQMGNTOngx8oHlDjhfLQJ0hjmjjcrCmeBn0Vyv2JA6NfFnUCKBV767ldAPecxBwBTy3DgRgE5MVStrPqIxfEKWsVKvne8W1Ke2vml2j4NKlEI7bNiSUD6sBbv_XLrqzTeSjAR0UCMZ5W1fUkvxic-YuvPgfxLPttZygIH8u_88kzJOdPzXoU6zag5wVb3aBdF0RuGcfdpTqFPakThQgmIEVN9u28vJsMFioJCSzb3zlvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ در قرارداد شهاب زاهدی با باشگاه جوهور دارالتعظیم بند فسخ 150 هزار دلاری گنجانده شده است. هر باشگاه لیگ برتری که شهاب زاهدی رو برای نیم فصل بخواهند باید 150 هزار به باشگاه مالزیایی پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29808" target="_blank">📅 15:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrUDIQUyXDRK3yVLrW73iIp0zjA_BAWQ1BFeCkRft2_viZHhf7Y4h1wm2YyMvWyM-GuUsRCMujZgbBaZZihTVDFi8OBI4ugGTHDc9kI7eHqDZR9AkjuGO7V_ogSngPP_RJMjAFnKI0pic6gCLa3qv4jA1gJiyl3s9tLL8ADKLA4Zl29Yl4BDMvzpkgTPCRai_wudYg9tdc-Ny0liylt9By5jTQTjH__JF0KhyuB6dwOXqhO97QX8hcJ_pwQ-FVJKwerskNREqm1TX9-R3QoZ1-cEPgvxbtcsXgUqyNFY2-u9xsCbdlQRm_TXWQ9Z5hlfPspyNMhvC6-gRAzvNzPM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAZUuudk51XK-HZlQRPedNCk6zRDZItPQlAHrvIj02C9uv_eGG9lwb8ide3o1hijov556zIYQ4wIrnFw77M6BldG48tBBklEMRru1LDBAeVa2psFGQPehmY9IxGMzqT-68v7w0EFmx-utn6rEH9yh0PuRQhi4fkvF3LYtEGrjwvuwJDy9LhpvZ4lgFbQPJfiq0K87aby09eiIVpCi7jwePO7j-9hq0_Rr4qhFlKMPrW40VXmC3S4fOWN7kOREXDOXAiBGJu8Njclk-cAcaZv6pQ9OywklAvYMgIUaCqXwQbL1icT6YQPlEiUQalli-QqFpAjHQG9f6yrCxfJwZ2Aiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29805">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdv7NG0fsc_QnztDr4SZkqPO9vW7cjBdFDYdN5T5-z5U_4C5oYQDAcwkJ8qbtyXto4EfVaqdKyqCj3beLB-WartrHygEryO2f8Yo-m7F8qcrnYCg7U4MiKAiNNhqfH2WKlNVHOlBprb4PhoHc2-F9JRwodtbJocqCYVx3HY_ciPj9bJ20U2w0loif32h7REl3eOGBt5a6pWrHdfwIbN6w2ux7iY4Xi9o4wLlykWazE9P8ZuKX7lMMZHeHK6q64WYha0xFiQL7VWu5XZt_tOy2fo2OBqt9g7DKn-GtuebQ63AfJQKpNFMQKDwR7tlkPPt8hcos6h553nqvUT-cB1MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امیرنوری‌بازیگرسینماچندروزپیش در مصاحبه‌‌ای گفته بود که خیلی پولدارم از هفت سالگی فیلم بازی کردم و اولین خونه ام رو تو پانزده سالگی خریدم.
‼️
خلاصه‌کلی از اتفاقات مثبت زندگیش گفت. بنده خدا فکر کنم چشم‌ خورد دیشب‌ تصادف شدید کرده الان بستریه. زندگی‌خودتون رو رسانه ای نکنید لطفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29805" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29804">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-Yd84dbHesu2I6mzpFGOzq8w_f_VKC_h1QuX9GOMsOLOVoqt5nemaElvhDO22Psjb3f05cmsmJwKKE9dAjyauQIg8timxbF4NX9DfhSFSVYGmGvN8oedlV64EuTcJ01ZsG8RVZY5fSU_0yrFq36YgmDnsTJfxKN_TTuf_VNO1LmBLfWuOnU0fAi6dbwayonUa6k9ZSV_A63UDVvCk_QX4pRcK10cQgBrZLf8tFINNFwPBadt_gBiEMeQA6Ss5K3kLwYnb7voQZoPMUKkY9w7mH42mPEJzzRsMWaSvhPb9BxXmX4I-Lffm_Tl9SkgfMSfR_Ym7CqxEFgBMwx4y-8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سسک‌فابرگاس سرمربی‌جوان‌وموفق کومو در گفتگو با گاتزتا گفته در وهله اول اولویت فابرگاس موفقیت کومو دراین‌ فصله اما اگه درپایان فصل رئال مادرید به او پیشنهاد بدهد باعث افتخار ماست که با باشگاه رئال مادرید کار کنیم و سسک به اونجا برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29804" target="_blank">📅 13:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29803">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Q93cZKcJPg3x9cRijGHsdiD9HdSWJMOnElM8iLqW40RqNQbkbqOIkHhS6nmW11G-Mg0TSfEzhYuR55ZmT4Qg9tE5qMVStow8uZOR13PPUGHSUxgYTjc7FRIhChyjFtWr7WlESVMgbHxcqK4Pq91qsyykrXRG5Tzbrmz4UNAUoG-xoDqbCGNtpyZgTmz_pL6Yvc-yfNj_qi2ZbuY1EVRguOMonK8LKVX38epJ2n92KNSeSAqK4-u2131egrDchQdSbRpoL15TAZeaXYVqsae0LaABDWaG0LUFdqN-XvPDE--2WqKc-vMGhjd_bCAgd1MmXjnslt6qfbHxLgZYdF0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29803" target="_blank">📅 13:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzUe_SaQdWSH2cWrW9HvWl62BnyF3Y07NpQNSaY4dg63Nfg1VU_m4NFqTRVqyFvjcEP-PipZmX6ErAc7Myo8bANBJY8fMUTwglZZ8bQMHfxxoJkgmczkmdKIVHOr911BYYLuz5WRRnrKUCto2s9rWRQtQEIUFZjrSOej7rRugY-of4G3iDXDtfqCAgLKVu92EroIKsPx6k6PmZGPmF2K1QzGrv8ruvThy5QxEAt1N1dqlq3jtMwOr29tUOUZPHevBjPZLeqjTh6naFiSX0pr5OzmgFCLsKIi__74Th4MV_TxFUKI9qzrtql0PFicYZLMcsKuUxUevTTVC8aL83Igow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دراتفاقی‌جالب‌وبی‌نظیر؛
در هفته چهارم رقابت های لیگ جزیره؛ لیدز یونایتد تنها تیم میزبان بود که موفق به کسب سه امتیاز شیرین مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29802" target="_blank">📅 13:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecWs-CQvvDIdBwU47UpCBXi8VGy3u-0Z3RWJk2c0lFGw3_zWllQ9NNdm_UozBgvcsli47McUZOc7dMfnm_iA-uC22CvZxMTjKuSfiUN-ZKw3WVuY-NFmN8Pd89s2UIcNS-6kBsg_OWu5ZQ7lXDGS6lqMTvl8q6yrfS89WlCcSTzCdEzwqXV2Ga8d0bSBOoOOC13W6-KTElKu_yAfzebV9Wb8wMczcpZGM2Hi2wJwLfoRVb7ygAf6AS8ANvURCrfhBARkoeOgRN1IrVYBSEKOrvLoAmAxFVIH5K-7AEKgwyG-zs5vIXv9ePEMvyNABfCAy2rRUbpuTbLf2cIlcABAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29801" target="_blank">📅 13:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdYXPqOTu6AtI30H3ADGFmaK_qU5mdSka2txBGlMJYcVAbmztaRfH9DkmQI9Kl3GNRnATMGmbL4Z3Q92MPXzDMtRrbOnwF3Gp9eETkDx158zGK2B5hFG15PAE-laRvAaRcvs-cxQaSBr-8XBMSz02v0uzLHnIOhEKdbkQty6_KkSsvbkZz7W_PvPzzBfV02Q1oP-lHDVrPdLfg06VTPGB0M-beeZeAT7g1tEQuRuS1LjwM1meAQR13IUz-jg5IOJwNpwMW0VnIixrOju--Jq1ARbdL8enFqsibjVWcz7fnHfO4MNvaVPPtT6DNmNEngI37MexaHTSAxxExINB2U70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های علی قلی‌زاده امشب به محسن خلیلی گفته درنیم فصل با پرداخت 700 هزار دلار به لخ‌پوزنان میتونه موافقت مدیریت این باشگاه رو برای صادر کردن رضایت‌نامه علی قلی زاده بگیرد. خلیلی قراره با حدادی و بانک شهر در میان بگذارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29800" target="_blank">📅 12:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYCCaViVBIKPEPOW2W9GrCsB5aSwy2QQigpdsvKeca5g95JVnQEuyteuOv7lTkKdPk2psAxNSG8H_E2uqOhpM7b3nCZ-ATrJPKhjMfSmMhAPPOD1WOh_S-2wbqdAYiex0qiaDtixdL-44iYWgMq-1YTn1UYQf7vzc5cRtvmoFWyYNi6hMF5sORs9TwReZj4UU-LlH0uRapCQKzJcgNKiLSLcVNfLnJ5a7GOqjRPZj6D75y8j_pgMS9CohHcNEQfeDJDJd3754xrNwPpr382kQ6CBsGxxJwutokqG5b1MeOoeOWr_IhULStgNoqHchx1h3Thc3NQgasjE1FvFtHYZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درخواست‌عجیب‌وغریب علیرضا بیرانوند از سازمان نظام‌وظیفه: مریض هستم یه ماه سربازی ام رو بندازین عقب که بتونم برای تراکتور بازی کنم!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29799" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZRQUi-htMzmbghZt5lViinWnq2nunpJUEFQZJbMEXnNfjkF9-Au_YoqnANq6Xywm_XdbND4qhb3NOZmMfYO9NHgEyF9VGGjI1tdlFkm8397G_IKCqwaD0LkmlL7ySO1zJKubaY5ObE5x10TKLSvk1I99GsRBqewqDH-7nbBhJ09GjY68rmZRt1dPfK-nZxE6D7tA9WgYjD-VDcKtYONWmvmTpq2BhJpb5aQqNbPBNUWYP2RaD7Gr8R90gTD0IWZcqE50riEneWW0cJv7CLmJTuW6UNWRRpNlAu2IMO6fggT4EqYAn8ZQsZfM9Op6HvDvmMEWDjHvH_ZsF2iLNrO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29798" target="_blank">📅 12:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vE5P8hWoGMM6pdQLiv8ntdhqsNyDpCxn5tD_ocIJjbBWZdO-977H9iUxNaFj-_wtaDQ3f0cs6fMMjEuslzCDs6KdS31uGd8r7YeQHv-tcLuAY96Jzr_qKJepiEIfuMtmj6jOx3UvLQXNbdN_NVTueV1Ju5eCBXROIL1PJHyaut1juQFaYYg29cpWUYP93-L8QeDjCe6jteLejO-NOmOtx87COqDHfIDT67EjLAEua_fdrDK4MkZ-CgEXDocMhKYhcWbG02bGtNvY0K6gS8rgUktaYJe_zQvMEzLtNpTWNFRRsiGaeKa4P4QB9CDQtzqi8d0ZB35DaVgGOhge81XjsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYeHlMBFp_e21pe54rERuTmrj5fut893VudgvpqoFmDMiyChgviDcC9dors3qFq1kmg3QC2i2v9u2OwmHIX9c3IR7xwMs4jpCL5T5r39GsDXqI38eEo2zI-IoBnIx4Mg7R62RnCNDG71YkpzGVlhnZjgFq2sH_FZII3zdR5-YhunO-qZ8x3gPHygMUTuDs8N_B5nKKK8xV6DPMX2u3ctmYRY8WxX2yvcgNwjM6b1PYqvrF663SpYgHwIIeW2l8DKtkrjHbmLWQURDwVR4MGdBl5jULnT0bPhNK3PmsWrIviPCa_G0KqOPyt4jyC4H6fd9nLPvawQC4JCoUaT5NE1og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
تمام قهرمانان رقابت‌ های لیگ قهرمانان آسیا از ابتدا تاکنون؛ الهلال‌پرافتخارترین تیم قاره کهن. نکته جالب این که تیم الاهلی تا همین دو سال پیش هیچ افتخاری نداشت اما درست هزینه کرد و عین باقلوا دوتا قهرمانی شیرین در این مسابقات بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29796" target="_blank">📅 11:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29795">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPYWIzRZ0Qhckvu4yC9C6Ib3Yj87MjQ7jb4NoDC4Hjr7yw97a2fOoZg65y9N6lA580epZ414VFjue8zpEx4jI3zSQBTJlYSXuEQ4K9Wo6wAOs6UKnX5GH80yNRXrqUyJD_eAnmCUicDvK4_XHr7uvDjYPPt2ENKsX9Bz6biVwg_J0PdJPfckcsIQYFr5OYq-mi-5ggSrTd2sVyQDTazUhdfWoPepg4eNLrg_5_uk5P0dzTYvCLgTaSFHXogFZaGm9HKhH41KoVjy-0q5wrH2JoVfrxnCCPGPYBSh28nB_8H7dOsZz5Isyrf3wY78L5n4bhVWXw1rJtb_hXwRfoQtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابیو آبرئو تا پایان نیمه اول بازی امروز بیجینگ گوان درسوپرلیگ‌چین؛ موفق به به ثبت سه گل شده که‌یکی‌ش داور بازی مردود اعلام کرد. نمره آبرئو در این بازی تا پایان نیمه اول 9.1 ثبت شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29795" target="_blank">📅 11:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj6IDE-6MiBUggWk4RWlR7GVTcrquHUKtmgfO_nJ--GsMaWDR2wtrtrjtmjZniiki86fcy2DncJHJdXZFM3McgOEPQyJS0gOea3gQrGun8rmngQlDuYfbfbo2nAuVbDpQrLB0A_xoNSbXtClpVqcRagOYUpXkE2FTGqWDgJUxJdQyVthJBJcufjM8YsJD8hJeU66wdGznZf7lANUxsasMicxZ5TePaPGBJT8cWKk4_gZ2FQmjzlguBoOmpVOxGn1w5PlYlxGclpQl7aGE3VMNnu1Q3i9PueFmw7FG9bRhOVpajjRzPucC7WldkPGJvHpYbKFJgja0LWcgZqKw6mEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29794" target="_blank">📅 11:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dal86uCYI8nr1-M4Bn96tJaaH6RuqSjaruyLuP1Mtmy8ju6Gz13pfvUQRftVpXLA-GzVpprP5eLINj4MUOFvcIcu2Kdw-6hfKWg97Xmt6stBTtJ58inLBJ5_FAa5pAFA7IWXeFaITkTSJ7PTkjOcz8rFhKqVAz30H-n7qGbJE_KfBp4LmdRTDrWPDLbv2wL1BL9QEMsdsRr37Lw08x2Cyxikxorvkkat-6i2S_NHchgBdX4zv0KC7YDq9aXFX6nSv0Ovu4WNUNwOxvB6dqioupLHJqoYsh25Kn1kqs0_u9wiXM3h9HP4fbojPywAvStWtVTeCMQcR4VVgAS4n4dgjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29793" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29792" target="_blank">📅 11:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29790">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc2q9K62souzViM5k9s4qGUJ3_oyUP6HzNQdzL3RqwNk6-6Bt5c0POb1EgP9LudRAo6W47FeUaaAc4OBZrW_U2Divg9hhmaamdG9WTaekXhS_osg_DrOl4flZ8BTq3WITP251sN7o17L4nWUzP2u38PDwn9WCaKPE3Ngs5jAFnae0UNXdNqtkehJ-DR_A1iymYRGOMDX87VwdXq_AbJyzQAWAKVZpusuOgwNxkzYRNFkka_G8at0ZfQfTMDn8ZDgCe0auNrYF7pImUSxA2y78PLrp9wWheENkQ_BLWFCTx4nFwCJXaC_hcwViGWja5J2dPuuElDmIeVAYRubnKkC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29790" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29789">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxKBzthMNjB4Qi9LC1aSasnjarcnDREB9b8hlllcFO2B3qJBt7UOK1IAD1MIGQwjUhP4UO0KcP59E-sReGEtyzpYtceMv96NgUMEpRrkJ1bH7zGqzLOaqfE9pxqHSkPBpxJTK9LCDOVZlItbbgVPDl1tMa0oFYvNpp5feXNKLfSfQESdVxLy5XooBIUXW2NALUTgTipkuVuZgPOp8xq1e7HHajf4JBNqBVzqiwXuMXhCpyuV_GsJiOYX9tBPIq6yp9G93FAQ3OwKNNtuJJhQ3leEYjAiHsk8jTphfnmCeSmPtsbp8-uQLgT4dsxZGazGtJ7SgDGBoWrcW41e5y5KEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌کادرپزشکی‌تیم استقلال؛ مصدومیت یاسر آسانی جزئی بوده و او مشکلی‌برای همراهی‌آبی‌ها در بازی روز دوشنبه مقابل السد قطر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29789" target="_blank">📅 10:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29788">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltEmSh2G30Mu49W2eG4BzhgnPRtlJ4bmKRvNnh7i5hEcjaR8GhRM0KmRZmlcblQE0jy3M0VHQrQg8OYws5KxHGfeP8MtOhCCPxd2BMonVFrRWk6aNJtZYC8JijWjR5VUddR8CRMJ08GSE31oH547qNGNRav6JJz8IrRGlfHVB-pj5WfrpjHB1r9COy7gulxS45fEo9gb_TdSzJMSpjsW3ZgRMo8aAOf3mge6J6Dn3PeIHmRo8ZVqkPBxhJaWtrAXmAbxzB-11dWQDyCUuy5S60aMkeqIxRlFue0HKGO47LIaH8mD9tn4rwOqoMURmg9Hmqoh1pskdnKRE4cMVnMgWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودیگو گومز ستاره پرتغالی ولورهمپتون در کنار دوس‌دخترش؛ پارتنرش‌به‌حدی گومز رو دوست داره که تموم بازی‌ها برای حمایت از استادیوم میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29788" target="_blank">📅 10:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29787">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=KmCZLPWqRSSVxMFiy_7-CdwL9AK7eAa9ZLkbY4Vofb6Ie7NJmuG4A4wYqHasDhwz-24Ya5ZJ42WmH2frSdAgEpnQMo_bTDoM7Pc0H2WYvE1IO5K8Nv7DEnzd8EKlvXXlGRiZYAiQbvNotduMmp5D3ujN6thcZzyr0kOvJKstRz57-6z0nRS-d4FBiW-YEusKVmUKH18Q555KJXFpGV78fzRxZtZnX13MyALHq6n3N_VNNJxNhqp8SzbOPfny37SUO1y1QJQzTOu1l2Gq4cClMlg2naTMaNT_eGf6O4Rzk62_K71vduEZ83JGRH0sUB7EenXcrvFOdpZV4hTP_NZY4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a34b5427c1.mp4?token=KmCZLPWqRSSVxMFiy_7-CdwL9AK7eAa9ZLkbY4Vofb6Ie7NJmuG4A4wYqHasDhwz-24Ya5ZJ42WmH2frSdAgEpnQMo_bTDoM7Pc0H2WYvE1IO5K8Nv7DEnzd8EKlvXXlGRiZYAiQbvNotduMmp5D3ujN6thcZzyr0kOvJKstRz57-6z0nRS-d4FBiW-YEusKVmUKH18Q555KJXFpGV78fzRxZtZnX13MyALHq6n3N_VNNJxNhqp8SzbOPfny37SUO1y1QJQzTOu1l2Gq4cClMlg2naTMaNT_eGf6O4Rzk62_K71vduEZ83JGRH0sUB7EenXcrvFOdpZV4hTP_NZY4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/29787" target="_blank">📅 10:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29786">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5bokmgI__iqMBKYdBlm3y1AkqW4mxoIRZaSdfYkOLWTZ35E7u6m886Dt8acP2djH_vtx2ay0vHuifBWUvelYnDI4f7rBj1728POjHVwEgOAyG2B-efMHPVbRI0gBPNLRsiSxYIuzaqgn6vA_e1oybX-WzCs28FiPldplwnRv5zjefYqxzhSTApISkos5etk-_Ve4_aTPGytToS2byAV7495k0WAnK5LSBYCq5eOw9YxLMIxPCNhjD1-yH27duXZ0G0Ie7aMCgDTpHh71opFN4dF6tAIPhbjgzeFhrQE9KL8dj6IUT8X8WutnAUL1MQRIbC9Cx0yBCQOCKt_042HPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/persiana_Soccer/29786" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29784">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilR88zVHFYDzTyL_Yzf10PlBUQ-I-mnw-yX2UKsl3X3WrZKm7Y55DNNqRyOybfP9zbmo8YcCnEICVHpeRZvSvKvXERdNCApxcK-LOoytvdc1iLN_haYWONaBGZqXWX50MMjY_B626GykldfKTtkJvFBT5hHgRFxPNUfoynTcD7s4RILI7A1pQHjNymoWkTNrVWPJQxiMFoNebtavvHYAP8TXtDMlNglGHXGAwaT6rFR1h4sGE6xnxmykrpyQ-Twy4tdc5GxV-di7Bj5RqkkzzJryCIKzFddQe-s5Yzo7U9zb3VeT09CojPhSgt3PLm-T5oQJJvg9HSMq6xAp2figXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/persiana_Soccer/29784" target="_blank">📅 01:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29783">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp31UKBFribHQa78XP1MM_TC1AQUq-C7QzRHKcM2EzBNwWbcbZsWEnpLq4akiT0oltXwJONR1imMLNUZ3TrbDeIcQiYugllss_OoAc2fF5VjECx5CSjd72OH2-RlHYnjPiRx-raL-_r6fV7tLAk14X2fns2FVxQwlqMrbIPVGBYqKN80vAh-gmTnrMVPHnMSnKVaOj0k8Tcf5JrEI2Iw36U_C2ox90XaDIXYSnmtV2OWxXdFKcAkvK2tpXozYBTZ653JLtv3mIs29H-LWQv6XvZtnsjMTtUZOSYAuEP0LOUK2LPrQOJJ6fzMrEsuGXEs_J0TTUjOqaqKvLniCFdMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مهدی تارتار سرمربی پرسپولیس‌امروز درحاشیه‌دیدار دوستانه سرخپوشان جلسه‌ای‌کوتاه‌بااوستون اورونوف برگزار کرده و به او گفته که درادامه فصل‌بیشتر از قبل به‌او بازی خواهد داد و مشکلی با ماندن او در تیم پرسپولیس ندارد.
🔴
گفتنی‌ است‌ که علاقه…</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/29783" target="_blank">📅 01:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29782">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWyzWAngF4E3VRAPqk1PmkDL_7Zcs5ve8b48G7XgBejcL2UzTMqmH6SGEiWIZmemn2vU8NUPpCMGBKh8jEBshp-uqnTB3hJCZhCXvFfHMbO-kWrPqRwYMMGcM4SAqt9Rd8rhuxgh5ad8VfbMry1j2Pp7ffQCVIA9maXRmpeC4HIVXQvdC28eEdVzZHKd79p5KDKUNkseoxZDXXI6glWGuJ_ZIKcUs59zZGbTzgfohLuGPJ_59O4rPF9jgBGlY4-kfITWyEGiwahch1dKNj46RMGS3Ufv1CoL1yzac_gB_Ir2Qykv16HBxmMCjQU3tFK4Xr3Y5uFc4uCUXb9kJEz7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ تقابل‌لیورپولیها با شاگردان دی‌زربی در کارابائوکاپ و مصاف رئال مادرید با الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/29782" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29781">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0uB6_hUKAyrc31umnwPzByZ6or7MI8Ly-_7UbTvo6awHjZX62Ey12nqIo9BnniwbSLwJG1o9KCbyGIxtCxHDBKqUNWmDwZFe3BukZFE11FeXWZ6CVcW3XUfZXa9B_vJxoMepDWSEgwM3DbtFDgX7dDrNGb9c0XTQgT9AuRL7ofQu4d_oQUnK6ginFOJRDwIp339A7iIhGSlkXDAO8aMXnX1hxtat16n-wJZH1ZTXmQXuphz_2_UgbeBY0iDa8dHJTqAoPGCBgzExxk48qSSNB41x3ZXaxXQismT-dWY5j2Z3y64p2dLriU8RrC9kJe5NIbF88k-f_TLXUDEVZTQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرد شاهکار استقلال برابر قهرمان قطر تاصدرنشینی‌یاران دیبالا در سری‌آ ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/29781" target="_blank">📅 01:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29779">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VIpNmhoJE7sdW61ckzqXwcu_7JdbljkdLVB441fV_w41ziZWouxn4QTiQLHsaAopTDGrfkCPNh_5R4OykpPgMNS9XxO8q7ICjEdsfXaiZ-15o-zABLwoy9p5vY2dpY0M0I1obINCVksKX3DMiId5NeWVGCOdYvQJQfWYx-JtT3I1AKcy9dxVcTZAbK7vhuj22HT-82-NhHkSUBZU74TU3pFrWx_lph0y1GWcTZQYQCtOt_-dqlwd6VO3GqX6t8d3-3xWtdNYhRZPN-CNIWZsIg_PjVa4fCbM2_dWBsqRYX8lQZyya9DKCRyogLIxjhPh-H35d8ffxuR6SoWIPMO_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیربرنامه‌های علی قلی زاده که رفاقت نزدیکی که با محسن خلیلی داره با توجه به چراغ سبز علی قلی زاده به پیوستن به پرسپولیس قصد داره این بازیکن رو در نیم فصل به پرسپولیس بیاره و صحبت‌های اولیه شروع شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/persiana_Soccer/29779" target="_blank">📅 01:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29778">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCY8LkflslenX4thrWy6Ff49T8sIcrUw1A2_K6Qrym1lo1SLVNnMh8GsG87pWXs3p-7SvqDOuO0uVA-a3du6cmCwk3F_gleYRNP8ryIspTFNwEdFLQ4168gJ3gWTZkjExrVIb_vwV3Ulai4fdsNvqC_9gJfF19AOfnlVvlq6MmohVDlXCO8YMjoXoIpRdu6kNsrnC5dMVBFTFrhblSz4ZxKtd_P177cl7AYcldLjAB4aJyMOS2wNIKlNbKzrYAY-62Rxif6_I-b9ey9zzi5C3Hneu9jyjL8YVeOxiOXZHGyhZbKt9avsRn3pGuwvih5YRlzKboL8R05AbXZMSRMSmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ بشار رسن از طریق‌مدیربرنامه‌خود به‌مدیران تیم پاختاکور گفته ابتدا میخواد تکلیف نهایی‌‌اش با مدیران باشگاه پرسپولیس مشخص شود. درصورتی‌که با این تیم به توافق نرسد قراردادش رو باتیم ازبکی تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/persiana_Soccer/29778" target="_blank">📅 01:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29777">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3x8swRMTk81YIBvpzDmCH9txqKsirsZdXlxkvKO-KDmd0ZmOuIYI_AkYuhfNh80nIAX-CCpGIxNVboX0LDuyWkC_k_CzQA39j39pnaDh70UZVa_WDiGCLxyCtO_Stilj_59iuRTS7Ee-2BA1XFBtNGkCXlwtKGRSOqy8Xe_O6E1Tn5IBaLE0ASPfeRb5FgfGwxgJ4Sb54DSJ4nJ3EckbMEgGh17dcKD4BjlVdehkF-qTDLUJDw9aaFF1X_QxGzgPg3A9WnyrHVToe_xKDQ4UtC2cpznT6AInRkyMT0gqbfUtFOU5RnX64T7FNKnu2_79bck2x_WMa3V1gRYwTjdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/persiana_Soccer/29777" target="_blank">📅 00:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29776">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM7xGaztTRHIx6u9JalWJRa0xWfHc1AEcLLZzWZVM4guqdABR3IqaPdUi6_mZNf69Sjx3k6TiZ7npzhOr4kcGOJTPGCGvhXd3lX3bikyaNGBgQNud7J3lrwJhl4NRejRcGQGo0zjGSA--TAry9qVL5hgjuv9imPPDKgNhmc4cey8nskhhx7D0CnvsJMT5DIDCifktt5XlH5aI6AmAfva_yLe0tjZ3siLTmkZ_ir-V17ud3Pnt6mCG-YBFEUM7_ltiRie2yk_aQMWm19xWcfhMU611WtBN2CnwyuXh6HgnbGebMMvEsY-KNEELZ1iq9ejQQIPfM9Br6v-YAt-pUW0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال‌ میخواد درروزهای آتی با پرداخت 800هزاردلار به‌فابیو کاریله پرونده او ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/persiana_Soccer/29776" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29775">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiMeAyn4oT63qqMGtpqufFvf4370LBhLyndTPGFP_SrSBJi1rObEqUJggQijgeJyy4xx5d3SUXnOPZxPkCoFxCu6YWLQ18ISCvkySYSgoW29hCw85yXKO05ywUq_7VCg7l8FfCnN2pC9kkAyjgx9ANwIZKMkgMNwbxtQVyzhAEhWxKR4hKuAiJoUh20LfUgAffhOsxmHuQVeUqd1e7HzetAebIowSZzTvIFpQwiBpoaWrER-8R9WqZERwTSomqxVi3QxSGX9DwbJAp8MTGdQgs3sjZ8QH44D7dFol5prhenASPe4EI0kZylocYn6TIi60p-mIRmTG5u6cnu70-GNgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم سری‌آ؛ آاس رم گاسپرینی با دو گل سه‌امتیازارزشمند رو از تورینوگرفت‌و با چهار پیروزی پیاپی درصدرجدول ایستاد. شاگردان سسک فابرگاس هم دو بر یک ازسد پارماگذشت و با10 امتیاز در رتبه دوم جدول رده بندی سری‌آ ایتالیا قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/29775" target="_blank">📅 00:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29774">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsDvLCyYwZlYckXLX1OLiKV5htREMAGnsqiiDhdjXp7bQHXrDnNzggOyEq7LXoimPuXeOVv_VWO2j4gvaTITHAr8coNpMf8keTtQbeDPyYNp6hygKn10AnM5dzqmDB8cESzWTHaLsaBtzT5yE9cW2E7YnizhRqnydy-RoPO8ti49JtxIbiySzeOCv3loW2Eg48u2FYffz1sj77mgzrNhdc3zQJyL9LFdTfr7cj3VvC2SGiCpesM-w2AS_o-fzRwJ8bbqxuOothtKVbVtItNc1wieUjrjipRhYEwJ9DooHkHfKkUHADzF9Du1iKuNSMS9eQcapk6Duq3RHHqn6RUuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/29774" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29773">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAsB-lZQKMAZ7mk-NojzJtUm4zp9JxaVS8ksibxBSIjFXO50Mx5o0CgFBiUqVlPJY9TBoLJUUptmOWv1FG1Gp44hJIHf5L9W4G-_uJtxTRlpLrC4Zf3XDLPi-pM1FSVY-UR813pXqOkBAQtb-KBE73rHgOSMvK6lr21k_FP-w8bGurPdsGmvGmbBSKe7ZQOAVQ92MexsyBH4TTJ799GCOv8bd-asNt4HX_Gu-LmrQungbmx0-SV4x5xpEb1hoP0HxU_b-_zHxoSg8koK-xLHDLX50DsJxVjaJ8ZqUJpv_L7j5BVcCC9PIluYu9MMTXeQ7iYOCbfEa8v23-2GUMGZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/29773" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29772">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFPE98BlIKVHNzjtHPOuegopAgaYlWPtfrlJAWvr5lqlSHIaBR2_UyH3Eu3-jlRR_GN91AhYEarCSFcucd5eR0AhBD0uVqaxtHUeRZxVDjO23_nA5Nav1yDfAthr9iKRIh6ZQm8-0iE6cOjodS5VHKF1SloOB9PpcjSiNi-R388yzyhl4f7j3ko5-1Xp-U2LwKK89dJV5tu_p4AVBTdhue5iCe2DTHfMCxBqp0F4lhsgT5DN3m-tA7SR5urIPrhAkB-Xk4gRMMBRRyfZJ8oaznTyJW41nHYIntfgIdW0awL8rjT_0qiwig7nN6R6hah3MhS0u5tcrqJeVaVICbdmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ نخبگان|دشت سه امتیازی ارزشمند شاگردان بختیاری‌زاده درگام‌اول لیگ نخبگان در شب درخشش‌خیره‌کننده‌یاسر آسانی؛ السد قطر بعد از پنج مسابقه بالاخره طعم شکست رو چشید و تحقیر شد.
🔵
استقلال ایران
3️⃣
-
0️⃣
السد قطر
⚫️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/29772" target="_blank">📅 23:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29771">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Elxm9xYJkAH4kz03Svg8BIPitYMwi4S6v9V9PLJqjm_IE1BTlLUbXEHom3nVo_LNWUHbUT3ItLcUOiuhy-lcX0vAS4Ka-tB2D-cS8WV4v1Efl-MZoWCqRR-MkP1xLo12wz4LyNPksZ8wCOJfCAvn8Nw-m9NZkf1B2-RVt8dXek1pGgIV-PvuIft8-lkq8TYHgLHW16DByRco4_I21gm9X_xthyeU0pv3YpSUfiZ80Ok5jHY-O5HbVmH_c-TGM6CFKKMVlHLH0Z1_PrtKitVqvujtZPXJ4WkL5Y6xryt1g3Yu0o3Yr3bzZ-rrRft0krz0Iv7SvBbvbOnecjtjZz7HoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/29771" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29770">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=ruUUl-vCkUxjOXMM-M3j8Q2YgA7iC4fmI04Sy__lp1xNsBVu1tHOYoVweEIKPAYvQl-K4BB45Nwh7bKcsnp3Tkq4cRPaoa9WEEUlSdbo7FOjWDDWjZZfNgxJJ66ihlDcN9QkKF55CXN3wu9FTbQtJJIwFFnd4351aoFhMFB7_zY10JY1R2aID0Jzz-bAbvhSfTQpa-IAXrrj8U0aIchwLOSYHo4ZxZ-gvajnULrYB_HM8xq47BQS-uRJuYISjYNGF6mP392IP9x2HxawMFHNl005zfJvtUf-pHTC1o3mvhozIWBajQKjSLFhn2Lfz4fYKJAbJRqlUUxtH7Fe_UYE9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e46b6c177.mp4?token=ruUUl-vCkUxjOXMM-M3j8Q2YgA7iC4fmI04Sy__lp1xNsBVu1tHOYoVweEIKPAYvQl-K4BB45Nwh7bKcsnp3Tkq4cRPaoa9WEEUlSdbo7FOjWDDWjZZfNgxJJ66ihlDcN9QkKF55CXN3wu9FTbQtJJIwFFnd4351aoFhMFB7_zY10JY1R2aID0Jzz-bAbvhSfTQpa-IAXrrj8U0aIchwLOSYHo4ZxZ-gvajnULrYB_HM8xq47BQS-uRJuYISjYNGF6mP392IP9x2HxawMFHNl005zfJvtUf-pHTC1o3mvhozIWBajQKjSLFhn2Lfz4fYKJAbJRqlUUxtH7Fe_UYE9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارشگر بازی استقلال
🆚
السد: بله داور آفساید اعلام کرد، مشخص بود توپ به دست بازیکن خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/29770" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29769">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2JuG8289UzEXUKnuXs57FpgnjhkxAdjuKUKwqzWnSk8GcS-no_0GzJheEXcsrGIGduGldyGdr41qsGh6p4hZkPwvYYmFKVyu0AwMJGWNTrTdX8MXF8IbMFkzM3fD7_xSFEySFO7_JlPL_H-sI-jwWAeUAFEOrK9VcFEX2FBIcE5JxfXfNdgbx3HzXNiR5XcleRd_O-kJCegyr5RUgnmea2_c_0eJ4_4ffTJewlBR31CLId1xgnhRUtLQ9FE0qfiWNirMNhPJysO-fsopM-M6ogWlGNv9jW0tv17lxkq9MhZUj4qwYRhNXTJx4LP6uov9OLy17GIKy1QdCn1yJ7EdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
اظهارات‌ جالب لامین یامال ستاره بارسلونا درباره توپ طلا: "فکر می‌کنم امسال من لیاقتش رو داشته باشم، بخاطر چیزهایی که بردم. چون از نظر من، من و امباپه دو تا از بهترین‌های دنیا هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/29769" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29768">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=EBfJNhSl4a9VTcYbwDI0b3obyDRFOGYkQxQP9a-UcILKPMLK7IF2AAL6FEZNmMo35nrBwN8-0CeuwyuFf-qlfhxHXP3crfzvSoLIX27vSZejxGSieAMb_z51nMUbKjSiYOmanPh3R9xy9aInpErplx-ZUrHufd2mj0LQIhNT1TPUQhEJz5ydvKh2ONcVIla-VpmbnWg9BowI3VOFakoMoYxef1zsdSMDh-HVWdYGLvJyZVE0hkH9Z2gjcWV72jux9smMQt9pItlNuO73bjUl32PNdFpLAj4e5Pf4lJaTwTHSUc2Jz4OZYi2ywPBc_rtD1IFfc10oU5N9RV7GbuCywIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a29f0c126c.mp4?token=EBfJNhSl4a9VTcYbwDI0b3obyDRFOGYkQxQP9a-UcILKPMLK7IF2AAL6FEZNmMo35nrBwN8-0CeuwyuFf-qlfhxHXP3crfzvSoLIX27vSZejxGSieAMb_z51nMUbKjSiYOmanPh3R9xy9aInpErplx-ZUrHufd2mj0LQIhNT1TPUQhEJz5ydvKh2ONcVIla-VpmbnWg9BowI3VOFakoMoYxef1zsdSMDh-HVWdYGLvJyZVE0hkH9Z2gjcWV72jux9smMQt9pItlNuO73bjUl32PNdFpLAj4e5Pf4lJaTwTHSUc2Jz4OZYi2ywPBc_rtD1IFfc10oU5N9RV7GbuCywIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
روی‌سماجت‌کاپیتان‌‌آبی‌ها؛گل‌دوم استقلال به السد توسط سحر خیزان روی پاس آسانی دقیقه 47
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29768" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29767">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=XdLdovytJuLs3aXQtMFrAcQ8tJ5HggqGPOXFZl1yzG6MGkQnKHPtN__MBHZDyTFToWF2lc8NnwLN6R12vt85AiWSKIjmIX885O2RcF-BoyGOLi_8cw_nn16A0bHFrbpPV9TCRVjBHn-qwn_vf-0jRBSwBeywoq1cSsRma5fA4YsxZkVTnUsXrOiP2yHwz_Mp0OpLUQ1JsIqchy5LSXICHMsNc5n0-9lIAQFPgmqCnZ7bn_tnUHAlwO3ha_tFkpTr-3XI-dkRRpMH9sbmIu6BIJ-_5XxiCJp7gXTg4ZX2zkFw9lHuTrOLUxLCBSPhLYWR6I7t05tMfwVDh9xP4ZIoJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb15dcf87.mp4?token=XdLdovytJuLs3aXQtMFrAcQ8tJ5HggqGPOXFZl1yzG6MGkQnKHPtN__MBHZDyTFToWF2lc8NnwLN6R12vt85AiWSKIjmIX885O2RcF-BoyGOLi_8cw_nn16A0bHFrbpPV9TCRVjBHn-qwn_vf-0jRBSwBeywoq1cSsRma5fA4YsxZkVTnUsXrOiP2yHwz_Mp0OpLUQ1JsIqchy5LSXICHMsNc5n0-9lIAQFPgmqCnZ7bn_tnUHAlwO3ha_tFkpTr-3XI-dkRRpMH9sbmIu6BIJ-_5XxiCJp7gXTg4ZX2zkFw9lHuTrOLUxLCBSPhLYWR6I7t05tMfwVDh9xP4ZIoJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/29767" target="_blank">📅 22:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29766">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OifBEOxm7J-2PBCqoAuIM_5y9XdxIXoUkhYgAl5R4Ip3hrh6uqPfBYT8l1GzZYG2c0QEYLKKhl-YeEIeZQ279Z27CFPWrnnPTX5HKxa67lrMIXsjpjbogYzJSpIJhO_l0D_C5BB6pCQ5yMxj8_9JJksbSJKhTyYJGhG_oRqc9aWyZQrYa83EIsWvQs1M3truAstnTnGKAVd8oOMTDQRsvgRsXu58_qGCkPFPvROazcU8GhO38IJSixPnM2mW5YIEutMzyoTr8_JNYpyXd-9LqKtaDH1INu1uyPzJm4QV-4-nb2YAAXqvYMvvVy9iJGIhpOTnSkc4CQ_J0BVrgYqUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شلیک‌محکم‌ستاره‌آلبانیایی؛ گل اول استقلال به السد قطر توسط یاسر آسانی در دقیقه 9 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/29766" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29765">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVRD6nzLfNPaIjEQiNHSFm7IUp6a2U56LIm0TmGlgHLLSg1CasEPendIz6Nxv9DpLPIDwafVN3sNb1OAhv1BJ8f9x74JwwQLps4SqYBfAiP8SWk88_kubTsm7x864tmtFwH_X_YPT8m2ux3yrtFPoobGjtQwIUup0Wm60JtMhXaq-tkmTLFAdnNHiyjI5TwQ8A6FUhVAhGntLrv21hJQzYZc3NnSb9kF1ssAu5une4d0zWiOiJVumG1JIuUFxwyD-DFuoU_Fhij0TIzZYa3blbv8BdD_LUgDjn8H9y3Nl1Gtg1nkAAATyDlQ0SBsbxiSYIt71rK3RBc4blXRpiELrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/29765" target="_blank">📅 22:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29764">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=AAhmH016BAIQhhA-nKKfGsOM39kfNBpO5Lumq4-5kaiz-r8L0tJ1u3JN6lGIi1H5QtX1FT99W5GaDthkKgimV77MbsqcJWDwhIX4DXjwqZK8j_paLcM0b6oPdYhb3ZiI35EQWU-R7R7dDaCGe6IvZZbz1MT7LmAhEETeAL1koI8P8XT7bsF0F0_wSpGV_RlG0G1BD2JvbU2VLLc622aUIvPv9n7ZdFyrlG9bZHXOUmNQ9nQhTXpL6fz93gc09JwIG7Nopovr4GIDXDcTMmNTTOu2x8VI2ZrFxgiWn0fky6XzTQoKFFSZdZIemIHAEbXhUvmw6vLlX24UbzYCAL-wSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8d6d38b2.mp4?token=AAhmH016BAIQhhA-nKKfGsOM39kfNBpO5Lumq4-5kaiz-r8L0tJ1u3JN6lGIi1H5QtX1FT99W5GaDthkKgimV77MbsqcJWDwhIX4DXjwqZK8j_paLcM0b6oPdYhb3ZiI35EQWU-R7R7dDaCGe6IvZZbz1MT7LmAhEETeAL1koI8P8XT7bsF0F0_wSpGV_RlG0G1BD2JvbU2VLLc622aUIvPv9n7ZdFyrlG9bZHXOUmNQ9nQhTXpL6fz93gc09JwIG7Nopovr4GIDXDcTMmNTTOu2x8VI2ZrFxgiWn0fky6XzTQoKFFSZdZIemIHAEbXhUvmw6vLlX24UbzYCAL-wSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم السد قطر در هفته اول لیگ نخبگان اسیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29764" target="_blank">📅 21:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29763">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3SEaow01uef4zAQaDw7jX_79uneDMoLKe5CK8QdhJAVrapvPQ_SUP0c3thuvxxgqICfAxILYiWlrCyfWSxaOUwlT_gCXT6N7WPXYUAdQqeqLA56EAuXQ_VAhxxXgPbn5ZIqSkGMN_4thN7F6isHQHYOFVwnGy_UuXHPu-WCWrXUfV_4LAjDEVO2osSApsQfksVMn_fHWSF2QpLMoZWQ77Ys-nI7dpVdL0MSDLXo0Rz3bws8KCrrn1qGsyTAOXLzT7dBWVu7hgjSicU86Qn06-DwZ1YKOEgN735dnJRdlA71L4dvAc4QlMaQFX-vfEARDnQ3yn0ef3b_hoP8jVP8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل اول شباب الاهلی به تراکتور توسط یوری سزار در دقیقه 22 روی پاس زیرکانه سردار آزمون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29763" target="_blank">📅 21:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29762">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=YQfO9BE2V6Xl94prl3WS_9og6CQQD45-T7xqgP4KYeCLbtH-v0uSi4nsPeVMGH3NS5OuxTNSImxbJwpQArqUCTVtVI1xojL5bleyOGTVz8UGMMhCrYuMQAoba0j7OF5TxqOX0kesZd_qTgNGC820KLmpen0Pl7Zmxh6TSpCdbN_Qx3I5y44QrPqtKQRlBuyZHUmQMSRSF6RX6JzeIYNiIRGnQboujGzLxB2J4lxsJnOtRUXo2CHV9elvQ9394mVJvWl09MdnzcZPOVIS53ionbBx2xAkGrFDmXzVpRv_BTEtci3rTC-odWfz-x4BEICBcwLijtTC5HM_uYXTH5ZVMG7Koolkz8gXFwwaLoFi58wihUExXdO95Pc2sjsgDPJQR4-1SFhGt1ejLiidxSqGoPATrZKe3haV_jpZmxyVKXBXhPcDnB34-MZdsQczrg76gy3VJoxdi5eIpd1qyuCOUHr00bjDlk-taUhB86VEEI8peVWQKeka-mp-AraIC3RQuaOgS4vhJuQQHGdMHlRPV0jadt8_MQ-EN8ot9IKj_yuKuz4RcGzGyEHD9CxZpbhC51HWzBswjTfaG9BDfpNefjb6M88F4h2g3x95-3SzqPYiADXYxij9ckaEa6K8krIyVt5_zAmYEc9tG8nQc-yAEEdvsdbEWazhcP9jk9ATqjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d18cb084.mp4?token=YQfO9BE2V6Xl94prl3WS_9og6CQQD45-T7xqgP4KYeCLbtH-v0uSi4nsPeVMGH3NS5OuxTNSImxbJwpQArqUCTVtVI1xojL5bleyOGTVz8UGMMhCrYuMQAoba0j7OF5TxqOX0kesZd_qTgNGC820KLmpen0Pl7Zmxh6TSpCdbN_Qx3I5y44QrPqtKQRlBuyZHUmQMSRSF6RX6JzeIYNiIRGnQboujGzLxB2J4lxsJnOtRUXo2CHV9elvQ9394mVJvWl09MdnzcZPOVIS53ionbBx2xAkGrFDmXzVpRv_BTEtci3rTC-odWfz-x4BEICBcwLijtTC5HM_uYXTH5ZVMG7Koolkz8gXFwwaLoFi58wihUExXdO95Pc2sjsgDPJQR4-1SFhGt1ejLiidxSqGoPATrZKe3haV_jpZmxyVKXBXhPcDnB34-MZdsQczrg76gy3VJoxdi5eIpd1qyuCOUHr00bjDlk-taUhB86VEEI8peVWQKeka-mp-AraIC3RQuaOgS4vhJuQQHGdMHlRPV0jadt8_MQ-EN8ot9IKj_yuKuz4RcGzGyEHD9CxZpbhC51HWzBswjTfaG9BDfpNefjb6M88F4h2g3x95-3SzqPYiADXYxij9ckaEa6K8krIyVt5_zAmYEc9tG8nQc-yAEEdvsdbEWazhcP9jk9ATqjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
باشگاه دورتموند با انتشار سوپرگل دیدنی و فوق العاده فیلکس کلو اِنمکا در بازی این هفته با پادربورن مدعی شده باید جایزه پوشکاش 2026 به او برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29762" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29761">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0DsXywjHBn5k8Svh3JV-ptSDLg9m9Mg3szz1BHKUr1VCUun_JrzefQfS07923_yZkhQNqfSlBAuc793YZKZAN4Q1_Z3C86NeOngWGwIeKGIecnlEPPFXIdGyB0e33CBPzB9luvlKyFuw-G9wOjtxm4tQwm4fb2DjTWaYHP7SayeYLqOp6Ukj0GCwSVJw7Uj6PMnZpoyNNMAIjQ0mMBOfeGA_2u75K1LvrbME72MIXQzdFsgedBJOAY-fudfSwmDnTjYlODRqwVSZVuKw4Wkj9RRoLNHHwP70MavY7OOcmjvwEGpTJJu0VuvUowMuWp6COZ-Oju3fVLmo28cLmSACQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29761" target="_blank">📅 20:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29760">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_IWRRMJFasyANCSpQ-bQVAWMj6xQsYj1TqJ3YoydL_Sdw0ngo3SoV1tEQr3PVslW7uDYmKo7f3CQmJEaSgliEVULv1PONGtWQZAa3QzTXLWQVmkRePPHqvdaBTVeGrwdTTfMYQWh7sY9-zIvMvUm7TuD_s2eM4ICgaR4O4mV47xiYFmvyoX1hmh3CnrdF8JASBj6oeAp02T7XLIe9IN_u7h3u1ioNv0suIh8SAqYOPCiSUIGflyZBWayJp_xabHHiTh6ny1wGTPbAHw6_fTiXQFUQ-OZSeKUwtXw5gX_IiKtrwx5wZ3ENs-_EvhwKIsS4j_iFZJNfR9yUmpVUYn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌نخبگان؛ ترکیب استقلال برای دیدار امشب مقابل السد؛ ساعت 21:45 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29760" target="_blank">📅 20:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29759">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCWuKMbpcY06X3WJZ1kATvR9RP-tjC2I5QknVhwigKxxwIh-KR7J5cauIzDwz-gM7joZ5-LZhjhPU4V4naQJs7RPFHld_BaBLIlK17hwlfCwKiOjuzetqonrOb1rC4gsvAQaOAyFgAkpr5M-LF1mLgwcZQ8PwHrE-KWwEzetHxHxdvXLIUGoLwnD7rd10TvZ_V_XJRG9_ngxMCCYBLpD7EhbntxAFq-42XH47XekBFuWtv50buC2MdwezeuEoGn_MEB1P8_w0Wo_ayGJX30py_A06hnMWa-rKi65BM9aWJAOlE64WG7hX8GYRN7XzeBpHKraU4qwSGamc6GM7ne82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔵
شماتیک ترکیب احتمالی استقلال برای دیدار امروز مقابل السد قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29759" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29758">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kol6ApazXbQT3TEIkMMFAgaP0asvq8eQVL5qBJsSeVt9IEJziaH6d0S30pBhMjcG8KK1h9jZBcYeOuhbWoYcdjSxZIx9enuuSC7ykN6K3_rNmx2jHFUazt87qbx1kVGgbN2VQ5yhVYwbbxP8p4-pzNFk3FNsoKzpR8eJbaUo_Sch3j0t_9MxfKREbJ_tcpte6CiO3QlMxPOYvzanW9bw4dquOpa-RNArylu3fj8h58dLUFVqi1v0nyxZMmH75DogLd4MDxWi3ljOxuBaiImkov4mSTCVcayQUMuu0CuNKBan4GQh5Dfi_kUPvaTbHK1hZXUvXWLe6kIU2LrrJKvXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سوال خبرنگار از بلینگهام:
هنوز هم گواهینامه رانندگی نداری‌نه؟ جود بلینگهام: نه ولی به کسی نگی ها. من هنوز راننده‌شخصی میگیرم، الانم کسیو ندارم باید ببینم همیلتون بعد فرمول یک چیکارست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29758" target="_blank">📅 20:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29757">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=TINVn2xSjpNFfBPxpdVS9sIMsODoCaeF4CMEIchOjOCPqEblcvRyI0H0Oj6mX3VN-WdWwpQnByRfHRe_kuh8W9WcyObfPKLjdstQOaw-smYM6B0YQp4A3AdZjm8dagOD6swYL9h_BbNlTPAOriz4HAeCmW5C5PiEE66-8uwOP85WdJqztqu8HboF6JhKmLJXzIwUcwBBjgNqrWcG6V0K70dRjC-jTzN_sEo2tzd-5F56SGGSupFK_grxbbTUH0zEw0-owBpOz_MAS64vJF1GgihdTCgZJbyt4e7Sr99cR-yrfuAJwSccuXW00uSXkoIq9n9o27c-oksR2-RuxYMuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de12818fd.mp4?token=TINVn2xSjpNFfBPxpdVS9sIMsODoCaeF4CMEIchOjOCPqEblcvRyI0H0Oj6mX3VN-WdWwpQnByRfHRe_kuh8W9WcyObfPKLjdstQOaw-smYM6B0YQp4A3AdZjm8dagOD6swYL9h_BbNlTPAOriz4HAeCmW5C5PiEE66-8uwOP85WdJqztqu8HboF6JhKmLJXzIwUcwBBjgNqrWcG6V0K70dRjC-jTzN_sEo2tzd-5F56SGGSupFK_grxbbTUH0zEw0-owBpOz_MAS64vJF1GgihdTCgZJbyt4e7Sr99cR-yrfuAJwSccuXW00uSXkoIq9n9o27c-oksR2-RuxYMuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ضربه‌سرمحکم‌سردار آزمون‌در دقیقه 7 مسابقه که وارد دروازه تراکتورشد اماآفساید بدرستی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29757" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29756">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90deefc883.mp4?token=qb8zIitrwJbYz4Mr8M5_uci7Ym27HGvYmA_WKJvkpKb0zCawsvKDlnGwZV4nkS1OtWoRf75gXLHeSpsC3Lv0hbPdcrxq2Q6ZMpnQqDaBcrj-JChkhA07Gd4BP41XMiRwOWDi27_I23HgCs6boUysTp4W31SVjtwaOUSZiRN5oAkWvJi_0LIEOYUoXVTSB7FznUTxPMKLlVB5UR7bs5QdStc13O8YoXsmZ83EBLevPtntEBjkLl99caqEI6dak8WPyMMncWE-PdOKhLvFJ-OSBJfkv0dgbus-8mIW8WBaVrSGcvH1-BLuAnhWmXRl0w077AGKk_bPABOiSlX2ny1PVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90deefc883.mp4?token=qb8zIitrwJbYz4Mr8M5_uci7Ym27HGvYmA_WKJvkpKb0zCawsvKDlnGwZV4nkS1OtWoRf75gXLHeSpsC3Lv0hbPdcrxq2Q6ZMpnQqDaBcrj-JChkhA07Gd4BP41XMiRwOWDi27_I23HgCs6boUysTp4W31SVjtwaOUSZiRN5oAkWvJi_0LIEOYUoXVTSB7FznUTxPMKLlVB5UR7bs5QdStc13O8YoXsmZ83EBLevPtntEBjkLl99caqEI6dak8WPyMMncWE-PdOKhLvFJ-OSBJfkv0dgbus-8mIW8WBaVrSGcvH1-BLuAnhWmXRl0w077AGKk_bPABOiSlX2ny1PVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ایشون خبرنگار باشگاه شباب‌الاهلی هستن که پیش از مسابقه امروز با سردار مصاحبه کرده و بهش گفته مطمئن هستم امشب دو گل به تراکتور میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29756" target="_blank">📅 19:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29755">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoZZ6ozu6LtGzbm-NblL85BINcmT4vDzcSgnmj_2NImwycceghUNEyQp2CocynhWqvy10Ky1yB1Fim37nZ2-nJit8v-DLao0NCStZ0TLpFJ92NghY1O39C6elgyU_aunUKIWZuXhBUBm5wojAYGT9eTB19hc0EKWFyDzXGjpNZCLX6Z0d_vOYQchhm4LUqMSq7lTBviDOdLdLKE3WwrKHX-9n4Zli_oqqtQAAXFwuPpjn1Ya8g2XQX1w0RbkMZXL0QZ2yz6vVGgUEpBhSvyIIG7VMWOvvtfeJt1aZkV6SRsJNXcW9yIEV6umZIrpJXItMkQP247ksLZy6DrjrxcXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29755" target="_blank">📅 19:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29754">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXdLb5mZzNQYLpzazOBm0NnRxm2hNNyyp7ACPzsJXsdSmL83QQYfeOvG0TculTpP9KD-baigWqYq62TfX41D05ADDv0KJtFxi1iMBs_x6cxqrseMKt5x9ak-D-mtexfaY2Ny6r4WQ2pPUL_LBtv9G_nrdfXyuSd9mGmw6r3X0sQ163aAdBqJwmJyIhrZmxZICXaKN9uvAJVDzI8AOtbxBHjtT9SkLhvlhMRmxJuD_34G3XNfNVUPEJn1OlfCo2jQiXxlFR1uBT0_N9MsuWU2Uszlbwg6J6wt37_qQe-FfYdqsH5Vs-KLEewnQ5Mop6p3yjSHgoz_FLcYO3Z4-FDBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فلیپ کوتینیو فوق‌ستاره‌برزیلی سابق لیورپول و بارسا با عقد قراردادی دو ساله به سانتوس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29754" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n40tNZlGDhfv2kzZiro16GqxawI2EWgvImsUhdYTb_r6lO4alI9R9E7zo5ObHvZ7qfDQ-167pIpZ5Ki9PgX4ubcpZDUelwggPTyljBEkmO5pU6Q-UVRtBZhQ_R0cUlmLeJyXsit5pApacJpi-kLGRtaM5MmtDQ-m0YAFiS9UT9An7feAQOqUyh94bHdDyFZh_IyU_Dr2e4YXaA_KlYgB2m58WAUFECd9cZzhQk7zqy0a4pQDG33i8MEMNOgcKC5isC8yJA-JMIPc1XgHafg7Z8Z9XSFBZpE9l60kHzdgD3IJD5iokSTByzjaQBtTHwi1qKqkxZhoU2xU3qIKgKsKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛
مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29753" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29752">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSFW8Y21ZbmxxfBDuy5FRG-30rGQXJpKOWs1XqkekJuDN3GsRVfCuh9i_S14M3ozYJviIQ7gQnVdVBeWX9ro-nJFfk2X1e7HV4JYpQymqJA3sNqsFxsppTq5F-C6-NZtb0k83ypAMbGZ9APGk5ZMa1v7GOUARYunVzGmc2tpcZOuuiTmdAOVec1HzG9WzQ1T23mlUBxO-w5QCWlxWhAxFghW4bcCpcYpeHvIUToMqWhTHpoGe6EulMKI_lvFoDUpuQkCy5n56z8l9zJo9VZRjwM7xNNlJ6EHFgGXRkKHr52kEsJQx_I9zGiY8xJrg4WqZQvrPXRm7F1uyEzVqlSAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌چهارم‌لیگ‌جزیره؛ منچستریونایتدِ مایکل کرک دراولترافورد مقابل‌منچسترسیتی ده‌نفره یک‌ بر صفر بازی رو واگذارکرد؛ تک‌ گل این دیدار رو ارلینگ هالند برای سیتیزن‌ ها به ثمر رساند. سوپر سیو پشم ریزون دوناروما در دقیقه 90+6 مسابقه رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29752" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29751">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dObyV3maz3dKwKjcMjfiVpiJMwM6cq4-qJgpJPMF3V-_UDB49FmGxdSU6t2hSyp925l005BhQEJYGaRoh8NaBb7LS08kyDF8JxrdbGAG9mNNI7_80wSTugUoneL4J-y_ET_30byUn6SWmNlbAKuVU4NKdyM7BOHvx4FJrJno55-9Nu6Og8VzgvdDYGGn3jmK531AntS0Bu62MQosOnsxNQeAh_Am8drntm1l12XxYSMVTopNlEr3SKib_4N7p9w5rFG7eE45NN4VNhsCxwlmPjddasVSSJxNGnpmH1wF5dV89WqSz0KDv-Eyf4FTSU3PVh-NrABfL60H64GhcKxHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🤝
دوستان خود را به پین باهیس دعوت کنید و
🤩
🤩
🤩
واریزی دوست دعوت شده پاداش بکیرید
🤩
برای دعوت دوستان خود در پین باهیس بعد از واریزی دوست دعوت شده به پشتیبانی وصل شوید و همزمان با دوست دعوت شده و برای  واریزی شخص دعوت شده پاداش  بکیرید
🤩
برای آزاد سازی فری بت دریافتی میباست یک بار فری بت را با ضریب 2 به بالا کردش دربیاورید و سود حاصل از فری بت را برداشت نمایید
💬
برای اطلاعات بیشتر با پشتیبانی زنده سایت در ارتباط باشید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g23
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29751" target="_blank">📅 19:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29750">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ3daKqtTAc32au8wZ1x3wDuj50YqAzMk4opr2Q6aKOHfRt05YJQmSFGESIA4k_PL1d6yE9VHU9Vep4Ury9nIQEOtrcLnUMNH6W-PZ0RLdW7vXuzIToDOiQMPCVvCJWYxJGIER5JteqkvdQZjiDItHYjyTQfFqfxoUi-sCUPrbQaJkAvmqeb1VCjOQpyJn_VBDx2Bc9eQMtq0198r9CUn7EXOsmp8gz5tbqRKj3twiXCe7MHJrmw8LwxHPXrFNtWa2mjc8kNmXwHbRATEkeYUh9hyiEW8y5yReZOYCAD8nAXGbANYGNGryLkAx3A0VjKYSWYNmlVv_yFvYRwK4tgug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29750" target="_blank">📅 18:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29748">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYotYfQZUVy4z-XHd-RXeyFXyoyxrgSuvRPODA000A4wzf7XZUEAL3-Az5vlMy3Mn38H40_A9i83R6RE9tGTgT1CuRBySCP5AkhrDaO84J3QYsUYUGDloKzsBuWT_Ex_JwpVg4HsQVKEVbI032PnfkTIwlqetVnssUlDWGZQ4ZVu2tunnKLctl95pTTKQtBsLiWkgfXOLUEdRtOgVF9FBV7IIP5mcUtzmJI5lqfzol3KJCnjzh4X6B1JRvdgl2fLL3GjcYrY_G42GPArmsniMNIBJPRpAGQh3r8DWVq1ibDq21scrcvdq99GNiJ4I6590qbg95J1r2XB4BSj9Hz3ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlHdRwqA_PCCSpxI5RURqum28kILrn3yTQ6XbOJnYpPx1BdE-RIch8Oaubi0vfx4s14UkidcSAyweOv8Pey-paylkRtIPJ2EI5OyK7QT230QSK77xBAlGgJbN55T8CAui985HJntW9DdD6V5MiqwkRaBHlLBAh-EvocRvLHJsi4e-TnA6vuoJ6WSEUbcGIoKULckiEG_sH1bEAKI13cBjGNS4myPi--7z0SZ3froeSnOG_dUJvUrXjaKGAPRLljw9J4fnyZd5UXa_m9XBr92HmurwvVpsgPm2eo038HQoCwjbktpWZOy1ECPZ22pKZ20a6NCjLKB2FFGjwcRnws-Uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
هفته اول لیگ نخبگان آسیا
؛ ترکیب دو تیم شباب الاهلی امارات
🆚
تراکتور؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29748" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29747">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgGjAiP2Qhqm09UQg7JccbsafHXDienA_nb23oZd2dfBln3m-58Klb7GyhvFvOvUBE799V67Y16BG7IRtKawJSQuwmo467N3x_9iGLbjkIKjaCFiD4taUEO2WmLrIy-sv0KePKqLLZEBRC5-L_J89w8auRNnkqYFfZsbW9Ix8s59tyhsTG0DrsEqok3_mwtPOmOB0wV44Y--KWMri9Qc8niIQR_mT_w_9JznHK79GaORMxumOy0qw3yO5HutzbCQJdo_3RyoIH8xROzN5OCp8f_Tjn4XeUfgr4Kbw6klTFPX5eBR0J4WrKetTOGYXP1TseDwTkek1lT7JnGJDJkTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از زمانیکه
؛نامزد ویکتور بونیفیس قبل از مراسم عروسی‌وقتی‌‌فهمیدبازیکن تمام اموالش را به نام مادرش‌زده سریعا تصمیم به جدایی از بازیکن گرفت. دختره این امید رو داشت که بعداز ازدواج و باطلاق از او ۵۰ درصد از دارایی او رو صاحب شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29747" target="_blank">📅 18:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29745">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adae707100.mp4?token=nuR4sRaSYSrOGqOMSxWQJ8Dx5MZugIf_HEentBULibcrxRUAE7osIa_3zlPsrZGsPomVnvd72tBTe8AmZJfazWzHkfWRwVROvcScorr903cJ5N664sefVcM2M5ookTRyhtgUl4R1KxU15V9Bb79a66DhD-6XV3U2IeiHFC-9H6pe94yDYcpHZ7Gg7jKY0_wA41pr3RokBVxK5GVbp6DXwFeSN1hl7YsTC2usa54K-ffmeLePiroVHl_Jpm1572k39GUpazP225SdfqRXcdpclzlO41T_9aIsM9dF3rTL7s1QQK8stPmoetbM7_v_iaYQ0aVTN7DN_QaiGhMZTdVUTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adae707100.mp4?token=nuR4sRaSYSrOGqOMSxWQJ8Dx5MZugIf_HEentBULibcrxRUAE7osIa_3zlPsrZGsPomVnvd72tBTe8AmZJfazWzHkfWRwVROvcScorr903cJ5N664sefVcM2M5ookTRyhtgUl4R1KxU15V9Bb79a66DhD-6XV3U2IeiHFC-9H6pe94yDYcpHZ7Gg7jKY0_wA41pr3RokBVxK5GVbp6DXwFeSN1hl7YsTC2usa54K-ffmeLePiroVHl_Jpm1572k39GUpazP225SdfqRXcdpclzlO41T_9aIsM9dF3rTL7s1QQK8stPmoetbM7_v_iaYQ0aVTN7DN_QaiGhMZTdVUTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله‌ تند و عجیب یک‌آخوند روی آنتن زنده صدا و سیمای‌ جمهوری‌ اسلامی خطاب به لاله مرزبان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29745" target="_blank">📅 17:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29744">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN0yYXZtHa9DK81i_GERq0v81WfxkeCgcozvHjYhNnJacV91BxnOLZfrrDODgOme_Vi-S0jb9Lid2j3HmcRdubh0Ab-is3Ibj__DwzillOQ8TLX54EZXaagyAbOJQKQGb5jgWg0TUc0IwjlNeTZTZmxPuiwJ-9xXwa1m5TSjDrH-C7Z0q1zUDFN9rraYY_KSbSHWBWW2aabVqu9rJ-PoEOQ7MAN5yTcPwRI4-kadMZzsDm0Q19gQ7aYdoKT49aWU1FfPx3oVmrRH1NQOyFSHOO-_hI2b8hZBpFVkXHse9VkarBkN2LloyNHl1uz969PqWCx6_uOvHlDp_hThkg23OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29744" target="_blank">📅 17:24 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
