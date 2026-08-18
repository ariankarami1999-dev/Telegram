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
<img src="https://cdn4.telesco.pe/file/r9DCJjUXsQWFlZNITq2Wml1Tc3zWMSrOoxQvdjFardjei_j4E8GFIO7KeKH1-0DYKPs_I2eEE6ZojSTJX-I3JaZj0I_NT3L8WyrNwHvB1mCboKi0kRcD_TMniRVeaOI7p8J6y1JRswamZdDekH348UJ9UjrFWfiou_2aaavtKzOl--tKqZy4AktyA9HuVzKuS2wKX36ciReVMBO6Cqzl_QQUDKCWbn_1wtSN8mJCOEOuCqAZx6DNr903dCINRGYCYbX5pqKeuQ5bfZzKG4I2mK0u1hFthozIX11i2aqwrywDgePHDCyDd7h3yBKn8rEVtpa9jEZifo0g5wUNO79opQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 628K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 06:44:15</div>
<hr>

<div class="tg-post" id="msg-27970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqWJbrdWFOqngNw4mZZUD56vSI_kEZwDxUe1quUKxnyCZiANXY-ZfStTCYrm-rhMYxOMoLtfQhwAORk1uQqdOuDoUwCfjjkVgR55-IXMkN9WnOcCVZsYOxTmP49AfMQDODwyiUjKdniuza-9cmHdOEeMY-Wbtz78a90NzRykR7fltunk6GU0lLdNZ3JDzBx6aK7MernemSXi-ahlUqNwzL7VQMY0zYTknVjjgP-PF2P8KdoHr1sJ11lJqAk3TvmcY-diXs8U1ZeBut2JgdzixXFUqB2BVnnyd7VbAlJHdnIVxAtq1WNM3irJiGm3rA8yy4ptJGf2Ai1w9U8KlhuNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇦
امریک‌اوبامیانگ دراولین‌بازی‌خود برای دپورتیوو لاکرونیا درهفته اول لالیگا برابر الچه گلزنی کرد؛ گلی که اولین گل این تیم در لالیگا پس از 8 سال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/27970" target="_blank">📅 01:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27968">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwkQpD_RoU2nNINjpEbK44W9NKYHoBSmjMnh6WSZO9hbTDsyFVYhjr5yOdLFofRaM3-CCDCoyV71bM4Wga9ddJmsCLXttECmp9xoETyF06gKAy7C7yN__43PmnmyMft1DEnsfQdt0Huj1Pftgwdd_3Z-i_5XgAYj0AZxBLqfRp34oV1RahuMOlwrSeFT8wL1WAyBBBGyJSreYkZXW4UPLHBexiHuc8PeWGw6nKae8j_5ObteyJpt1PvtnxQQBE5mX5pRQ6Hgn8qn5RpFD-_Wwd4TYbyTeOH9NSBGxQS6xmX_PtffIJBf0w_a4cwfROfNlD-z_9Q-_t2F_h0ioBEDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از مصاف سخت آبی‌پوشان بانساجی تا دوئل تراکتور و سپاهان در نقش‌ جهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/27968" target="_blank">📅 01:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27967">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwGDCxb-9-YD2h4jXdTjNWtJfhbDfAM7ACHKUWeACvdMl9o8NC8oG5Ysgf6JLRvNAJGi8ZNrEFfO3LXO5UQlAHOAfIo6vixHGXALvbLO4jb2oFy-dRmYEpUmIJAcYJsjfoOpJTcgZ_yygFrFOIfHiv-a-ABXTcuVszM8S8Im54OjOFkRX2AarB5Msr14kkemsdiSyqiCwYpdboq4QhLWtquXdm1dfAOBGMcUKPIqRErN7bsjeDQ_FMPk4FGFva80hUHtbNd1Scxg3ZTR_z57WKwFUcebegKB9QxI68U0rrnuu-eYVT-iyxWCg7Woad2sTl44ovazYo1MyjfADp1wBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌دیروز؛
صعود بی‌دردسر و راحت شاگردان‌اینزاگی‌بادبل و درخشش‌روبن نوس پرتغالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/27967" target="_blank">📅 01:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT4lFpNdJh98g2NrfZoB5qMkkgwNn4Wl-NfK12U-6NbTv6Ew3xeyA3zeca-jbfxuqZbaxoyo7dKxi7fZ3V_PvstPRY6ZJiXBdPfHjUnKDrQKRmryZbJ59agPLNKvPnZ7LMaVaKquFhGHytb9FCwdZDr5t6UWyUykRcjV_ahIqaZ36FtWHByqDbF3aCCIhGyQ9vSEJGdDL8Io7glxVnqnh6-O4RKW7I6rNUgzgFMtB6dUPyhVVg7pE9oTrKzJv78k5B07j9BlTJ-ZERNF6p0Y8sqweHEGsQsFtzJLI3DBFFKk-__l7qnP5YlZKW1nD620AlBXTZmm0YdRFsXnCNcgGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ترکیب‌احتمالی‌استقلال برای‌دیدار فردا مقابل نساجی مازندزان در هفته دوم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/27966" target="_blank">📅 01:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUMU8ly2fVzLtMOWzsq69rGB77YqCQl_3mMdS1N-Ofmo1zniwx0z_T9S9lR3Msrx1vxUs_eOGkn2-En5PEVC5jA2IAbnYGgvKvX9_fnEuGKrPNxp_j2gssbfYSzTe5QE3L8NQDinfMmD2F8LSu-3XDrNVJeofCeNZnVCDr0NIb2eOQlvqsgz92jLDv-rFMJhicV7j6tNWJKIaL8AE4sLahGW0gEt_q19wjViZOyhqaCfmw428sbAJ0LxRn5jDwPvmSPdJM_xvNY8IdagWiXAMcnVATl5mqc0GKTxpanFDWAOLG2HRHa2k2xwFVM4fFIN-jPUYlVEyEbYCPP3YMLQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/27965" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
🇺🇾
هایلایتی‌ازعملکردخیره‌کننده رونالد آرائوخو دراولین‌بازی خود باپیراهن‌لیورپول؛ سرمربی لک لک ها گفته قطعا عملکرد درخشانی از آرائوخو در فصل جدید رقابت های لیگ انگلیس خواهید دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/27964" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhxnsoF9P8QenJoq_v9BT259d5NLui9YKj78W2S4RFPwndtNisbUd4zGL3DbQ4xiBIeHmDGh-QcTEfSBHodtuOJ888-m3FuTtGPiZpO1nDJJ9KdlTjVrRmZ5u4OrcRNCeew0RuJoBmlCG7mKT3r94QmHENnJznmBxtQVI_HE23UPEIl19KJsUYUmSJ_pM5rRdV0kNzdC1YzEVQSX_yb67cYucyyEVrGiYO8AK6Wh0HiHZzYGwiQNROlVVpsJZZFhe3VJQYVCIxqtx-rKlQy6pgXmLBRnBCh053Rvaqw1odOB-nngdsGx6I4B8Vjhp2RkfYpkWIFoHbakpmMGCqKJ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
این شبا همه از پیش بینی فوتبال دارن پول درمیارن
🔥
💖
اگه توم دوس داری فوتبال لیگ های اروپایی با یه ادم حرفه ای پیش بینی کنی و کسب درامد کنی عضو کانال بکس بت شو
💖
sa26
📣
کانال
بکس بت
برای عاشقان فوتبال چون هم فوتبال میبینی هم پیش بینی میکنی و پول در میاری
🔥
💵
‼️
توم میتونی از پیش بینی فوتبال یه پول خوب به جیب بزنی پس با متخصص این کار همراه شو
💖
💖
https://t.me/+F1CivZlkxrgzMTM0
https://t.me/+F1CivZlkxrgzMTM0</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/27963" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeMwBI_-ZmQK9U7rGCs04kv7MFgeuc1eGlul61d1TQOjY11iqTZh8eW3DOtL85Gy7zHe3cnV6TvxGDsfmpzSqzMSP0sWlAanlhnhZuLZ2dsFeLgSB-qmFBEIa7njaEH52nkEp8OesYZbhh26Or2r4fET3XZkrfZzSbDbVX51p8i0ktpufQ-e0MUkp8ZvzHp2nRaPN3JwYCz90MXzsED7g3zjbyp-gkCS29idLS6IVb-7JsUK9nlcPefgJjQw04yHpYuwlV5GS-dXaGmhviOjMqmmY6qP8Fg-KwXslEfFGJsLfp4e179o8q31ZoSyjv8NbGuG8VIwbJcr_cD5O_yqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
یه لیست دیگه از بهترین و خفن ترین نرم افزار های هوش مصنوعی برای‌کارودرامد و تولید محتوا. سعی میکنیم که در کنار اخبار فوتبال چیزهای بدرد بخورم معرفی کنیم‌. با همون گوشی دستتون راحت میشه بهترین درآمد داشت فقط کافیه اراده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/27962" target="_blank">📅 00:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Txryor--4KhzlfO3ShOPyMiAiKdtB0dq5hrTtAhGfulGtOw-ddIZ1Je-bOi1luvUPHEQEyxZyyPLGq5jELQ914Awe1cs5PAtwJjXJV9kqn-E54F2XNY-gc7ZRueN7r1CnCqsboRgIUxTgFA5zp9D6Lt87hlore_fZoyKukAS8zy8yplF1mQH3p_CmY43_nzjkRflzgbk5I9yJlwU__UgnUhzPx2JaxnNZR7Ri1TnynAJwErg3Xe9j1PON7EBgSJg3nta3MQUlo2cgYGFcT3_Ek95pFz-HWNJDr3KopzKuRLSW0l4wO93Xa-Y7_QLG1onM9LC020dwQl5V7OVFZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قرعه‌کشی لیگ‌نخبگان آسیا و لیگ قهرمانان آسیا 2 فردا سه‌شنبه 27 مرداد در هتل حیات، کوالالامپور مالزی برگزار می‌شود. قرعه کشی لیگ قهرمانان آسیا 2: ساعت9:30 صبح به وقت ایران؛ قرعه کشی لیگ نخبگان آسیا: ساعت 11:30 ظهر به وقت ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/27961" target="_blank">📅 00:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOHoq4kHhLWVPlZ3xuAtF0VaKCGwL7J5VX4TXIfWwnGBrnrCWe-pBX2YOBrYz2qSI-VQ7IJ_5tCSNIpQfJbVbhsvU6oT0uhHZEQSa8-kcz0kBSG34NiYPH-ACMCYs8N-ok7xF7ETg6QyAqYuB7p8gFEDS4KdAjmekmvZoS_4CUoESVKNRqtOxBCnPugkvLmpke3z01auttWPnt24FOaLEaUywYNiz36Ocj_z24alAF2uBftbtum1s9PdEQ8QbQjV0XBh-VzbZ43lNAH7ce-MyQ_-Yj-4nd9M9XpSqNfK0M4H31OtR_fc580howLq3tFBAplf37svLmZYHVQPuPKKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🇮🇷
استقبال‌فوق‌العاده هواداران فولاد خوزستان از رامین رضاییان خرید جدید این تیم در فرودگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/27960" target="_blank">📅 00:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpoFC-xrC1wqCbmkep7uhlNeHtwBelRkseBO8XE4AOflQrIIontT7HfF_2QtARHtBJSYlDzJk1WFlXkOa7yegNRAzyDYKt1Nh-aJlA8anHEKfnzDZzDcIgRwPYGaUJSCxe8mdXkReI4zCSTjQyfLUmcvQ-2Z2AI6e3IHBR8-voVxpvNb-rHUgFf72YgtutdTulMxrhoD2GE9yU_2fQGFS52ud4tNbw7g8H3qJuaj_d1ktlZzLx0GeBU4-ce6kR3Xiy7Opzl4f6uHbgbnpC5ME8hqfRJIsAK6AKbc0zvzFmsigJSN3DnZ7vdTldtKrzTXbT6lHubC726yAeNq6JGm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت های لیگ برتر؛ مسابقات این فصل بسیار فشرده برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/27959" target="_blank">📅 23:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ea8a6246.mp4?token=WQ2ADorczFMq4JS1cPj03xK5GR6IZLA9pdSkqvECh3pwcEorgXj55ujWpJagF_-nLFw-pXMSroYvJmvthHV0saO2GpFd3ltp1SaEF4ZB85lt4MLSrPteibxNFcN7vc3WqqkAG5A-0J9FRFIXY7gO5a9TAzdmiYst6RC1_4Xk6oIXVaxZ0oY_XZXuKK5q2eNUWQrn1QJdMPlrX4z6FQw1VfCVkv3y6LqeZkHway9Aj0l0RUz_2NvImizKceDRC_cg0ZgGEj0DrwpUPGA_FhPxkS_-D_AJyxCudV-fhrunDkTUJi-aNzljB6A7_vvxy7hoV7wSyKcxkHvjaKDBH4RR_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ea8a6246.mp4?token=WQ2ADorczFMq4JS1cPj03xK5GR6IZLA9pdSkqvECh3pwcEorgXj55ujWpJagF_-nLFw-pXMSroYvJmvthHV0saO2GpFd3ltp1SaEF4ZB85lt4MLSrPteibxNFcN7vc3WqqkAG5A-0J9FRFIXY7gO5a9TAzdmiYst6RC1_4Xk6oIXVaxZ0oY_XZXuKK5q2eNUWQrn1QJdMPlrX4z6FQw1VfCVkv3y6LqeZkHway9Aj0l0RUz_2NvImizKceDRC_cg0ZgGEj0DrwpUPGA_FhPxkS_-D_AJyxCudV-fhrunDkTUJi-aNzljB6A7_vvxy7hoV7wSyKcxkHvjaKDBH4RR_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/27958" target="_blank">📅 23:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0831d66706.mp4?token=XY8L_07i5Fe2hrlh2W3sVwzvRwhSeF40hBaJYXxyq4Pmm8abLJsW7HyFRZiH651f4BedsK7RXkMp7lHDC4X9_63aiePinGyNLmUafsSd82p-E7fLWBA3YiU0CBgPlMT_UYwG-FKLW-seiBdEXOztdbYOHXbo-8MbASZikF8llxRU-520zUHCdXRJZ1wC0rZxYxFkXZCpIKRG9aXuPFaqVrWEfpkBorRqYxULWxzIV4A24y7g1Op01ZkE7_DqUGkXIgqOg0gfiqK3e35kkSfGVB1CoP5nGjjb1g5X7H1Z6BlahyxXUIL7a8v8D2USxqLgpHm-4BGMKj8aAqH_iPlqO3Uf2o1UQwN1-ZnT4AMTQdlgS_aiCl6dr3R0yTiu2Cfw_jSxzDPINzxhwFHkiMpehzTmOsXaRPY97IPtJ6zIzfyJIZ1p-2W6wMEGc-EM0rQCv46Fmf42RhRxnbPhTquWb--N9JBCTGOzO4ZoUGsge-GEqYtuZbT2Mva68EqLvEEvuse1kOtfhXhGL11SNe4kgmZB6QQa_upJTIP1MjPVMMzUzEEU6I17lc6I_XFI-jgm-H3iEFOmFoFR3oZLp9veyawWq5MhE-ZwRzlCVOEF4Kwna7h3i-hrBR2wq3JszUP6NShQV3T8imqlkfmDF6XME6DOGHLQeMbqNvLKGuzFtdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0831d66706.mp4?token=XY8L_07i5Fe2hrlh2W3sVwzvRwhSeF40hBaJYXxyq4Pmm8abLJsW7HyFRZiH651f4BedsK7RXkMp7lHDC4X9_63aiePinGyNLmUafsSd82p-E7fLWBA3YiU0CBgPlMT_UYwG-FKLW-seiBdEXOztdbYOHXbo-8MbASZikF8llxRU-520zUHCdXRJZ1wC0rZxYxFkXZCpIKRG9aXuPFaqVrWEfpkBorRqYxULWxzIV4A24y7g1Op01ZkE7_DqUGkXIgqOg0gfiqK3e35kkSfGVB1CoP5nGjjb1g5X7H1Z6BlahyxXUIL7a8v8D2USxqLgpHm-4BGMKj8aAqH_iPlqO3Uf2o1UQwN1-ZnT4AMTQdlgS_aiCl6dr3R0yTiu2Cfw_jSxzDPINzxhwFHkiMpehzTmOsXaRPY97IPtJ6zIzfyJIZ1p-2W6wMEGc-EM0rQCv46Fmf42RhRxnbPhTquWb--N9JBCTGOzO4ZoUGsge-GEqYtuZbT2Mva68EqLvEEvuse1kOtfhXhGL11SNe4kgmZB6QQa_upJTIP1MjPVMMzUzEEU6I17lc6I_XFI-jgm-H3iEFOmFoFR3oZLp9veyawWq5MhE-ZwRzlCVOEF4Kwna7h3i-hrBR2wq3JszUP6NShQV3T8imqlkfmDF6XME6DOGHLQeMbqNvLKGuzFtdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
👤
پست جدید رامین رضاییان که هفته پیش به خاطر عکسای‌لاکچری از مردم ایران عذرخواهی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/27957" target="_blank">📅 23:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVkF3KsuqWNEx6w_qWKjWmfz5Uag_BUXLHKImvyWdG9whveNTlnxEDjSs2ntyNInpoztC_4X3NDsnpMzkfcCZmUOt4sp0XdwWWfK21gTscFF8zuZOJV2EobvKqbORVrhyi3AmhmBzyPCq2qRhbeEe7DcY3K6-DQOXiCSntrDIfa5GpPVtQdw3UfAm51diba6LprzxcTlda7lYrKOdsOGaaFSBjDOx87nCYO0c0KFXCjI5WwQ0pyNrFCI7uwY68tZmsRPWVQx957Xv8kmS-ABxY64lQ4rU14taaEkgR2ESorTxqkcqKLEy-LAD5eGEYap38qn3Fm0efA3cuoDTIkgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علاوه بر محمد رجائیان، علی تاجرنیا رئیس هیات مدیره باشگاه استقلال صحبت‌هایی با حمید سجادی وزیر سابق ورزش و جوانان و شهاب الدین عزیزی خادم داشته و این‌دو رو هم به هلدینگ خلیج‌فارس پیشنهاد داده تا از بین این سه نفر یکی بعنوان مدیرعامل جدید استقلال…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/27956" target="_blank">📅 23:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1JDyI8vwhRVNi-tK5g0_JHd2_9pPuK0aG_WML0PWh4hEsnoO4SfpLro6-Zb8ZfcPkEq3Pnj858LVzj3oNXctyLlWGmqv4JYJDbuF4sdc3JU-0TYeMa5w1ms43bWkKRKwDi-W_wDuoC4oaRnGpnNLkhbXNAgyjoEoIp9l7e7tkdL95RtnynNEkUh0a6N9DyOTi6peb4G6qeVcg7yB6_VzX15mHyBLCwJfN0M0C4AY-Bse9C1s-S81ioaA6TwAFdPSGRwfQ6meKfE5_v8DuwKNzjsi0BIPbA0Q2rTCOEV-9aExI8dmjyDmKiiOUigBlR7WkQ0VWO7GFHQQ0aT4p8TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کسری طاهری: از پیوستن به سپاهان بسیار خوشحال هستم؛ باعث‌افتخارمه که کنار بزرگانی هم چون سید حسینی حسین بازی کنم! واکنش حسینی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27955" target="_blank">📅 22:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27954">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmHyIESQ8WhkuLi-dPXFiIzlxFaIvOJQH0uAaMgraDFnbi4IFDjg-92_oW5xtNdEDNBiCn-hVajxtpog2OFeW4avfJ24twT6VZpiTf8oXhUe6rvoPt9n00YBcpRmA7ZNQ6Op1bbMtZAaLXOMsth9XpPY1O7x1O2qarQwiCpIfMgLPh5vfTin33l1VES75I1kiqSmkCWG_0sFn2D02Vm79Tvij4AlYspjNrkRnsI2zcbLtAOW2Fgwph7V5smoZrn4ZaKy5tJn5H7zuUewJD-eZlDC6h0B9nnK0PR0h7HUFXhymebzOU-OWt6pIR_6usKwQjWAr2-1vpwkey-knYwjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
پست جدید رامین رضاییان که هفته پیش به خاطر عکسای‌لاکچری از مردم ایران عذرخواهی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27954" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eelGb2Y7AT2T_Sy-PXNH_NZMajusiPHdZBC20tSZ0J5FXHINNet_MdyPqN6r6FWTn-Gxo5rkdzOcMi-WJ8Yg8r97frDQSyCKq9J9h20FTmX7y8s-QUsfOOA9dqvKIu0RshjCXSstn62OqE1BkX6DtRqqIxkQup7_hlBzmjDFR21EUQ7tpVyNrD9TV6mLJvTGmYrpMWNZC39OeJ6VRyuYojEbsRY-bTDUQZiwGYSkwYJ5Wkdfh02qlhsr6ZuS4iIHOgwLhqde9lRuZWKiNia8POEkjlSEdJ-27CwvhCZfl6AV9LMP11BYD_P4pQzpZetDX0NoKtHXUj2pjekuyTYW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری بعد از رسیدن به بارسلون: با پیوستن به بارسا بزرگ‌ترین آرزویم برآورده شد. تلاش خواهیم کرد که امسال قهرمانی UCL رو بدست بیاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27953" target="_blank">📅 22:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqbjjBGcdhmb9CbI9s1fnjOw10I36ZqVKKelB87JXJR-62cIcmk3cbskW3pXxnPx7RnSpJ7GfvLaYW11ks7HrTBKtA2VzS0NLm4_xhegqQnmREXrcxTOIfuZ1yPQFlLwK_2IPs3ed4lOpznf-wtT8D8lNyn74EEb8l9XTL1Wo39HonE9zPWBqm_j9AoVEHffFFwsamlJBoCJSr25i7hGDZm9UB1YxWw_o0SD4U44XD3UyqLEAbdv7PApN1sAQsfgpBr-FIpWK6fokRQLWIHiUjhWrsHgC8o7qXbXTg9DBAkqt-JSZ7EFGYtXU7TVvOBbVZPHHiZwiazkNAJ3DxlW3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام دیوید اورنشتاین؛ باشگاه بارسلونا برای‌ جذب رودری هرناندز 30 ساله روی هم 76.5 میلیون‌ یورو به‌ منچسترسیتی پرداخت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/27952" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27951">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koWBWbU5MMcii5L1QOMo6jYqHI5isvuEZos1y-czeCBsRPANijsJNkmDODgL-ajAAGTsnkAdD8FxbcJOv976c8BKwPQPvmrLO9-oKo8tmWpbzu9ONpEaSxsnSViNUVALnyIfvv8vI9rfN9ka6SqolyatSUurKQxUpGtDLOpZ2kaaZtkUBQoue61Lk7RrJOvQW2EQrN2njfH5qZ5PNcqkr_8pnU3gi3kg4qTA1axGsPRoeTI3-AAGDA0xkM_Uto6IqW1v4v4V8A-xCSF_HtyDVmP19VaHlVE4lls5FFGkZq9PIRKsWfyzoJ1g8L3mKbNyghfksqXxbZuKHm-hsNtgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت های لیگ برتر؛ مسابقات این فصل بسیار فشرده برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/27951" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27950">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldP5CotIxfGsvwZbCuSd4QYQJjNnBW53T2JR7-4ihgpUs-7IEWwdLVY8vi4j1c1x5yFTDPMPoBjD_khhsylmaBICh9kYikIm6sMppKFE23e9BpV1v3xzwybWIg_EEe76_taY05GYKb9BUXopySURJVCom8R1GJwhFNvD9ZTJCJI6ck8OvBTtABd052GPIwflMQtdFeL-yFOxdijhVdXshbH021lQlWYktY7sjIvpPEW-fa2vxCJNkiUJBvWXAC-XP_8ItRkzaKHuinsXOIjq24juh23lmF5V6-vOuQ63rfukarsd6GJw7Ttgh4jJb6_eGYr2TR-Cy-ZLNrdOvRnCyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی و شرط بندی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
تا 20%برگشت باخت هفتگی
🎁
10% شارژ اضافی روی شارژ دلاری
🎁
و15%و20%شارژ اضافی نقدی برای 3 واریز اول هر روز
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
g26
🎯
ادرس بدون فیلتر سایت:
✅
https://mafbet.com/fa/?btag=260368
✔️
کانال تلگرام سایت:
👑
https://t.me/+8eCDvbzSV5JlZjlk</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/27950" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZxh-ZGBg700y0-pfCf4nP_riMXAt_fCQT4Wwcbq07Subvk76z2lYxx0AG31RHTx8BXU6nWelBykApm9_e3B6N0YXzFtW0tviwoRvq7F5oONV8SpvljulY6n2BK0PZobDFXW6Sm8JZ5NAdD5nLNZteDw1NUqBVF4ZHCPOcEQfEX49Em3vweSIIheExa-QBBs0AVxM4jVafXe3RhAhwm2SzbJ9ohIVcDpPeusw-ZZmWtvCTG2SANQE2_GncUM13adxPgEPpm0iV09bIOSsuzwF9fYmuH0KY1jexfO-k2gT2Cg7QEDl4RDjDpGCwSVj8-865h1kjldGl-90SRwbZ6prA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkVeF0yc0SBwZpSE9o5LcPHJS3gtcxSzlcKj_xFDWlmnNGGtcC164QTTrWb0uGYdSFKy-5gyquixWzGnTrEMdRecOky5QEjgvvadEiNvAebNLztsljyWaY6IaFUvoT-wgUXQe-3hgkpegl5Jklaqx5v0zf-HAJ_jW-bU6UiJGnD9SYjiulvTALS62EP_8wyUZS6ApvWx2-9HOipX9LoadX04tCUJkm4rbLfNe7GVt5wYyHeEID2V89hluqTf_OwezeqYusAO6cVUpXY25Rbbw67hLn2Hz-8MdJ7X3A809yliE2O8lpdXdt37aYGJZIOU751tDtnIRa-X7Bh6r7_VZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کیلیان امباپه بعدازچندهفته خوش گذرونی با دوست دخترش با این وضعیت به تمرین رئال مادرید رفت؛ برای پارتنرت‌غذانخریدی مشتی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27948" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5XLIGo4bD8X9d5DhFHLEdYza8c9QJlQIf5D9sPG7E8IsGgaqbJwJs9CvEmc6zBlmaLsQC2uFs05eBB97P7db4kqudvR58nw6FWntdccewNBFwHQfbrFyeHVtIelF5QvQxkET7Q-ZnSWF-KG_McqmAZ8zS8gPL_5YZL3Wj9ev3ST0LDDynjIyk1_oap8fv90MRLqr72P_4VNkJep_RE69e11Y3k4gncnxnACLEdEXGAx6lZgXCVmf2HW10qgP_nbqg6fOvCmCGeGgPM2iMujNx51pJEcp5YJImUjv4QpP5OmBYELpXPP6LJAp0x3tV-3ixjQp67lEG6T1JqCZqFapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصاویری جدید از دریا بنگر دختر خانوم 20 ساله محسن بنگر کاپیتان سابق باشگاه پرسپولیس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/27947" target="_blank">📅 21:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27945">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5xw9UfQOgngXyB5n0oB_tZtjZhhApIHRWJ45Zw_AYIq0LKDLUw6bFRdw4Qrj3G_E7DdcndJ1JEmO5ie34G_UEsktwRyYC9puzGLD8CtPBsXoZK9haU4eixNA0sPj1OMte4HOKgAfj11rcWF0aBKyOfff9uYN9RRJReDVh8AJU4R3JAXn7YczyJspHlmEpWB1kXdwt6p4Yo_l5iD3LtWSkvP-xYkkH0__8-UA5dBQcDVPIze49Di9jj3xEyDkaAzoLrPMw-RsDOh06APnpdqAWgT3L4ERV0Z_erS7GThutg7_wWkm8tXFGfqR5PWUfVl_AO6QlTjIhA9w4ralxNXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtSFLSNl-fjj7l8SKPk6R1d5Ckij4dUo0Gmk-Fb3c7m3AssqsQE4dhOabGT3e-oB0v3iQc6sM931kFhe6Kz3hDpIUeyxRIeNPzSHgcKzNp-XdyNLsaxuSnmpq5pq5160fqsxoJsb-lDFGt9zhAs9Pw64ZoCLl9neWFYpasCaKh4gdxBBbreb2nmbviRrWuXIo59eIMGi3Fc4OPd87yfqCflCI2fsIvGvPaxDzkAy-v1mGI6kfBZ-8YQhild3JAh1GEuDf3iO80RfkPIU75quOE76aJ88WRoiFu-tntidEHt_90FRE6pv8k2IuSX9vHYKxtl-fsMmBP02p7vHlqxadw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
فشار بیش‌ از حد مسابقات‌ لیگ‌جزیره با شما کاری‌ میکنه‌که فیزیکت از این به این تبدبل بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/27945" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27944">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1UIlSzOCRpBTH_dNs7R2M4RWmGqYOXf0fevfESr33HldXeLxnP6C8lokDbtCKEwoN5NcDyqqdEkbQuv0EeWOn2MCp9cvmwds58pYsxZ0TtLZTKB-7aEx81idfTgc9Dw79atBgz3Jvp-h__Cn6zKHdKfiZfyWNRgyI8_YkiIxzJ9O7MvtgrvGkpHDO8krD4QBDgjZvAPBjZHjyST-UtprNWXrAilMC-D_33L5B5DiI-sJSi1n4SMIZ0_jQv2-tTKi4n__QBFJJqiRzw6hyWn1TDaKlzxc_sRiZn2_i-fMxRqIHLaAVrpdGTpNFn7QW2HuXTMtE-enNqTqWaTs3S1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه الوحده تا دوهفته پیش حاضر بود با 700 هزار دلار قربانی روبفروشه بعد تراکتور میخواست با 500 هزار تا بیاره که مخالفت کردند بعد پرسپولیس اومد گفت ماحاضریم 800 تابدیم یهو این گلی که زد و باشگاه پرسپولیس هم‌جدی‌خواستار جذبش سر این قیمت رواعلام کردند. قابل…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27944" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27943">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFot9MfvedZrpDdtmf094UvWiE-ZWhdL90Bb8KL98gH2dLismdhSRnLepHFQTQEFk26BH-CNIrA5ZtNXaQ2pspAGJrwu06PULqDD0RlOOllu53JhcgwzsNAN3ssJdl05JbiUW2GiR3cCOcz6QZPOXJTmuLP2lp3NFDzxlTFs2sn0MtsHxwBGaym2DQNpQWbB6VRMdWdhqtoWUqo1dOAgGwFp0wXI7cLCj8JePx0nY6ffDRX3vqW2rVRNecBta5ARLV5Re4IgJz6Y6GYEFgg0NqCmys5ZXdvpGRW-yxwtbcIyBJf_jopsfYWPJRFlSRD2ZZl-_JrhEHEVmjihB9vOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شش روز پیش پرشیانا
🔴
دانیال ایری مدافع 22 ساله نساجی با عقد قرار دادی 4+1 ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27943" target="_blank">📅 20:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27942">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWu5B4UZ_yyJHe7zkjENP19UQM1xupMoHjZVJ64M0xxO_VOsfXXKLFjM5X_6O68OEj4VgKQFv0DfQqzHdDyYYcAgyFV_mm7enyGUyVFZpQhXyy3smmFIyRhpfH30mG4erGI1rzjaPBDMzDClnazVIWYGG9DVJwwIMMO2pbMugI4sBJin9FZYKj9eiZzYrZYSp5FbLClrkB8HCHWjGmR6fDFEkwjJBACWY86xNaHVLnR_GHfpcRaOMgboWav35sJdDbdJex2KbppNW0xorpooa0yN774G3NR0Qw_-97jvUdMjV_ZtmpU8mdtRfekqmhCZGZlw893Hyy2hayQwr0UDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
نشریه ESPN
:
با صلاح دید هانسی فلیک؛
رافینیا دیاز ستاره‌برزیلی بارسلونا بعنوان کاپیتان اول آبی‌اناری‌ها درفصل‌جدید انتخاب شد. همچنین شماره 16 کاتالان‌ها به رودری ستاره جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27942" target="_blank">📅 20:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27940">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vxIZlPanNDRxLwfOPFDb_NF9vnssAgspZKZ5bpkTI6bRqy808t59LdlLz1Lj28lpTpDxHLQiA39Iil131dnuIYlup1dkqWW1S0dK7WldyBm7GYxyC4siYpWmOMwd1wuv2tXoIHwvJ0GJOMGqrSU9htzzTSz5IUhY36ilqrUlOJFzIqPuWjgu9vqPlQ49uRt_Q48lDL8Vl5MnaHFbJBVxCL_V9sCtQ-lkPsUO2qcMXFgL5vEW8LD9UREr12VGKbPrQXqKZVviAc9CYIdKA2zhSJpvyA3wI86hJ3KzovIQV9KvWPZ9jir-LxQDH1vOA5msUIQ58M79thrgAHg5vyyl3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNtw-a0rvUXp1eSq8sDJfO6XuaEAPZjLP6NWvwspzUdo3wo4tFNRu6tg02uE89zPJenj_0FuhlfbnWxorKmgSeuyRcLOE2h0A_i54wmBRXLXhG8rZoJsuFzPZZJh8q7fGx9K-7rZHnRxc59ELssfjfOmd6K6B6gx65zQKdm49iErparVwzKsFhEtCmpU3LtMF6Nc4NKWzawMDTepqTB243vLM8YerJw7e2Gk8CkRM9cbmsJDIF7VhcArPNVD9yb1Cet0mLGOKBklAxgtkF1sATLW6q92hXTVEMnGVCtM4tw6CVfDOO_S2kd7A6N-mbNavkhUdV_JZWHVNMzSRodWOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جالبه‌بدونید با اینکه رونالدو چند روز پیش با جورجینا ازدواج کرد و ده ساله که با اکسش کات کرده ولی هنوز عکساشو با اکسش از پیجش پاک نکرده و گذاشته‌ بمونه! شما تاریخارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27940" target="_blank">📅 20:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27939">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTmsjsjudRXckJvortHYnwG-mIv2A3z_Rd8Jru-WiMTUTjgb0tANNUZxzBgchbMkQ0LGaoeT6QlCxEzXaMAuOV01JkXMp261raZg7KtEZvtEfsJ8FrvqJMUQvZ45bCIDtSKZDsqh3l9mvWjupjRDOJUYSec6oWzFT4FdzzXKNY4Ugk3pz1k6CSIbWkgOZZChzRDY9bZHlmkAqzj2Kn-3VfV8MpRss5Jz-31fx-w4lBxumdiIgIflAftLzavDBUjYiSQxI-k9VJdTAWR9uM68CoIquh_W2_AGQmlnkidVphmG9G_DbsTRy2Om8I8nwRylQTt0yILCZTdFbG_Rc3GwVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27939" target="_blank">📅 19:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27938">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq9tllTSFqKdhdlskLGRXWWu7tChcebQ9LTkyG6Zw5UMiTwlouSxv4Og9VgqhTvcMkt7AjsenizBoo8m7TlHpGHO5uMVynIaz9yU0otBXkt1T_c9TTxR6xg1tsx--g9BS0YLfucA-yWiLa4rFXJIdq91c-JbnYvA3DW6iBt4sXI6dXUbtPUw9ff8yv-UWUvRAILXOwOAx2UUBkNdWzFwmg7SWbOQxAEn33yum4tuyqL9j-uMXr4a14mZDoEvOUpiQIIlPzUuzJmlmJV_KsKPfFkX4S1gIi2T0DkZmwhAEERAjEPAIoF8Fx5YKIQFooccSwOJVczbqesM5SbHwctsmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
درحالیکه‌اکثر خبرنگاران از پیوستن انزو فرناندز به‌تیم‌ منچسترسیتی خبرمیدهند رومانو میگه فعلا هیچ خبری نیست در ضمن سران چلسی انزو رو 140 میلیون یورو میفروشند نه 120 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27938" target="_blank">📅 19:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27937">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRXtAj6N4i7phB1e56N848j4xg54GPLb2FCf1dQYmlGULzr9C5PmKQzqeMr2qhNY5SV7HL_Ies9Nc3bZHf5uHPPM_ZHUbCnXF4NE0cp_4YHpYQX7PGnJ5czUBS_-xv5ZqXaMsuC2kiy57y07m5ZNu3kBvS2Aloa6QO5FQ9lNvpDrxCG9ZPCkBELQFvmw90LruAEn_BExpul6pPXjkmCmK2tcR5FArXgTezPZq2UQcxEkI6Ky5TY1SgzRCub4u2m8BHGrOXCl9PdGPfc8T83JoFOKLYd046M3PzTLGug6bHd1N43T5c7HhVDw5u20T0CmOmGaZHnJ-LGBQBpBwSsN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بیزنس‌به‌سبک نساجی؛ یک ماه پیش دانیال ایری و کسری‌طاهری روبا1.1میلیون یورو خریدن و الان با 1.45 میلیون یورو فروختن به دو تیم پرسپولیس و سپاهان تااین وسط‌حدود 350 هزاریورو سود کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27937" target="_blank">📅 19:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27936">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f3e1492a.mp4?token=axIwbAXwPLmwl4nWyg8HkNppiP7FUdLchLcJb3mSgpIdUPqyGbXM0zHP6KZdk2VBSkEErVLWvOJ9qLXCqKsL35KEEc5oLZRPh63AY2GBRpjlnTJDiOr8Xw4z4MlPU8K6nBvDSYHnwfNdND1MBBszAoRqs6ckBF3r-sTBJmBGROQm5-yqnrnV4XNei54FRgelOl_BmCJ76HYXrhySnCPHPiTkcb-hmXTTvillmRL9NXvIl9pNQevW3UwiU8Oe6W88dY6UPM8cwST0dTW_pbJjMmZpSDls-xzRd5djJ4wLFdIHfmD3Q6zyzaonVP4R6vaF_cJdPzq2KydYxnbHze4VObZXB2-07mJ8SwSkC5IDes1TBYVVuvAD9yJFD5GQBzfa0_kkWpMPyaCwsqd6Kg2u05H2wIjgdIupKg0gIJk1Oij33WgBjqITxf6bHesK7UjCgT0c6ca22RAimLbg7j3AP-THoGuDKMo_nQT2KwxNaV3Op-ClNDmiwTr3IBJyR0r38pP5vM0zXZ3JvpyX6hVYHqCFrzwidSyYXIBIs99xs68YqLdvq1_VydP6zogjuxAPHYSU1LxQJpNdWIEIePuGZpz4gm44TNmWP1V57EMF-7sxK18d7zCuWAoiPmouEwW8oARX6_8toV1u-w87v_3Iy2wXzNdsSlGcJ7DeLRMpIiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f3e1492a.mp4?token=axIwbAXwPLmwl4nWyg8HkNppiP7FUdLchLcJb3mSgpIdUPqyGbXM0zHP6KZdk2VBSkEErVLWvOJ9qLXCqKsL35KEEc5oLZRPh63AY2GBRpjlnTJDiOr8Xw4z4MlPU8K6nBvDSYHnwfNdND1MBBszAoRqs6ckBF3r-sTBJmBGROQm5-yqnrnV4XNei54FRgelOl_BmCJ76HYXrhySnCPHPiTkcb-hmXTTvillmRL9NXvIl9pNQevW3UwiU8Oe6W88dY6UPM8cwST0dTW_pbJjMmZpSDls-xzRd5djJ4wLFdIHfmD3Q6zyzaonVP4R6vaF_cJdPzq2KydYxnbHze4VObZXB2-07mJ8SwSkC5IDes1TBYVVuvAD9yJFD5GQBzfa0_kkWpMPyaCwsqd6Kg2u05H2wIjgdIupKg0gIJk1Oij33WgBjqITxf6bHesK7UjCgT0c6ca22RAimLbg7j3AP-THoGuDKMo_nQT2KwxNaV3Op-ClNDmiwTr3IBJyR0r38pP5vM0zXZ3JvpyX6hVYHqCFrzwidSyYXIBIs99xs68YqLdvq1_VydP6zogjuxAPHYSU1LxQJpNdWIEIePuGZpz4gm44TNmWP1V57EMF-7sxK18d7zCuWAoiPmouEwW8oARX6_8toV1u-w87v_3Iy2wXzNdsSlGcJ7DeLRMpIiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فضای مجازی به ما کمک علمی زیادی کرده. مثلا شما ده‌ثانیه‌ویدیوحرف‌زدن آدما رو ببینی میتونی راحت متوجه شی دوز مصرفشون چقدره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27936" target="_blank">📅 18:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27934">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWERPkZwoYPo0J0jEQsNKkrD5zIiY-vs7X344huhi_uozxowyVb519vqg_GwyhzEJCvJTe_z-GdHs4tsSMgnCEbn47EABBNE9Bm0k4daO0sVweTBh-FdIOLNqGNDgMTrHKndX_5tRSXX-BhJKIQjbbAQc4vEetQE6EGDKdIeIoYo4FDocTxyIzd4b36Yxaz2VMbBohkoW11YKN5k3NBLizvvW--FM7coxLVn8N71l7blq4WkijEOA_XlqrrV56cNLlc6i3B9OfuN3ulPUk0MIBfFo3ON3c702YL7DudanuwUgVJow9zDnYKajkEMzyNa_Y6_LS-oHJlGnPD7v02jJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dbw2gop0PGRPJDJ4A0g6jbr-F73lt7iYNFgxqn70kmmNofoo_q182t2y_9m5aApAD6QLkgyU3iSsJZ6EiLccdUGFpWZHteYW79u56hyXnpzOMav4hTLwZGhovp9q4Xi7kxQfP4Ux4bL9JG-dW2kJXvxKWGqQrDYHhbSE5of6BDqaZoC4J88mrZvoO3VfaDyF89tnsxzY8ojdTdZJjzQgiTPUOeiMz97CUbs10cLltDiXFK4tdP6fVbYKqEOjWTr5F7UevnHbpBUXKSmIpnvA9nMtk0M4lIfn-omP9uetwRk8oWlSRDQiCmq-rjAFSYoLkj1gJIIOTWnLRaS0B9COng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
عمق‌اسکوادبرگ‌ریزون‌ آرسنال‌وچلسی برای فصل جدید رقابت های لیگ جزیره؛ آرسنال بار دیگر از اصلی‌‌ترین مدعیان قهرمانی لیگ‌برتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27934" target="_blank">📅 17:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27933">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yoh_xlREvHmPfwlV2BOSlX0hHaoEvk0fUmjkl5m-DpzezxmPaKa2WpnoQZ4lc0yh7dhf9JJ7Yz79f1-83pDAetzBE9dcf0pLBm-50KmfzRTyxyxcyqE70BkVQD7i_mezs3L4YNSXgv9P-2ehxgFYr1P-A9tVZ5TGEWAfdCs0PlV_4rR6aijUQqwtkpXFXwPynjeWf2hRN1jXVSLN8QyFJutkv6iJHdUnNjRQDoGQTOMiyZ1pRIeROI759UboUn8QEAVAQ-JAcAMAYxfKTaZ32RwL-S9ZyFzYYb0tTUS5iXeWf79HHgMD5El-X9cW_NZzXq35PUOYdObZxpkKaybDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#تکمیلی؛ مبلغ رضایت نامه سید مجید حسینی مدافع 29 ساله سابق آبی‌ها از سوی باشگاه ترکیه ای کایسری اسپور 400 هزار دلار اعلام شده. درصورتی این رقم توسط خودِ بازیکن یااستقلالی‌ها پرداخت شود حسینی به استقلال باز خواهد گشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27933" target="_blank">📅 17:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27932">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBQSSElt4fxkUSFtbHwXA310M5APTECyaFi58mHA3VvTyEiD6TvCMAZHXy5UWwfRPGV1GeL4SwckI20ta-39Sp6ZeSjR-DJ8rWT3ovwfREzKJBUFYgKAP1urJAQzOGxIfPasJUSsAymRVTAa1ss0KOT_yECudmwci4ezYlXbBeBZAayOSGALK32PHbgmj4AvXmIbIDRIvSM2myOM8Dc0QMx_TqYu8qk45tv4ldqAilSoIZymkYJ3suFmyxMfeVopAKvEnOd9dQhSQTGcC4HP-4Zq44_VKL8bemTlEnL1nkpWDRRjKbU7nMIEUI5d3fws2tK3uxreXqDYwSjoKHj52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ بعد از اعلام رقم دقیق رضایت نامه محمد قربانی؛ مدیریت پرسپولیس از مدیربرنامه‌های قربانی خواسته تا با باشگاه الوحده امارات صحبت کنه و رقم رو بیاره رو 900 هزار دلار. سرخ‌ها آماده‌اند تا سقف 900 هزار دلار هزینه کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27932" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27931">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG1swUBXHPt20JjmKfVp1MZqs0qfdfDzSjUIUujLtsLc62qWus_bxYmBnrBNP9ocEzfqAyVBYvgtDcmi8nsa27jR4aG9vDgNO9yunob_vSgaEx5sdmQqBPBb8FX7cf22kWHeDVQmE6ztGSEiJ1pKLQ-Psed3byojYzTL7zs-xLJvMXJbbVHDh4n3bgXuP4WmlZcjqM4U-H4mW9cj_6SvZN7ru7h7_x4P4MjkavQ4lEfzpYULBN_tCq4vn_gF4AyDTBpty2IEbffMEAfUob3aNURKHIWpYIN-iBGjeKSS8bzjYGh1jyKjnp3ZmqrKd7qECnN4z8o_8c5YYcUsFwTRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال‌ایری بعداز عقدقرارداد با پرسپولیس: قراردادم چهار ساله امضا شده و شماره پیراهنم 89!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27931" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27930">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfCpzFDvJYYhavDUTo3YdRP2U6rEKT1-MbfnL-MGGmFtlUsFQHRO-6ADmW4EppdwHk2WlYjQlj1l6jEU7xy5hiqHWzAuMspT4ATlj03ebYABPXtxI7RcZNniQL5TqaJ47N4hmvPHPf7pv2rQSXEmuSXKa-zf2W-qD9iucYeo9hCh_7j5-VRhNY6dFUcPHV79EMEJt--yqeR7kp-qMkqnuicKqO8JE443-B6tjJRmrKqb725d6FZV6U1F8xq3zLGKyG9Ij2P24zR92uo_sL4hPD0FU2Y9hh4L7zgqsXPv68YYyRQ0JwALVcV_w6woefzdjdMNCVkP8MwB-T8PXu3GKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام دیوید اورنشتاین؛ باشگاه بارسلونا برای‌ جذب رودری هرناندز 30 ساله روی هم 76.5 میلیون‌ یورو به‌ منچسترسیتی پرداخت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/27930" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myolCfcoUcZ3ujtdbIHmS3OVdxct2PNBjdbPqOzRc4pXUUGIKnTv6gke4pY1qQW1AJnxHyIW1h0HRow4er43zkAwPr_6cL5aNbpyTyYznQ6ior17q1eLycXctDbiJGyCIQcV45pEW-ad59HTZFACTKY_DksdpHEH2_UiMWB3Db0sb49Bj-76PyA24KDpZHN-Ww9lexXwfL7ptSamc1NSNtQx761FRriEHn42yhdFAN5MY70PuiYXTHNrcnEBWlMGXQe5K-OUOxgQVgGEd_XHJ9IfixLcOnAOxbD0ddlYaesjqcfbkGN6ej9zaY1RDL_bb1UboUwGTe73BqNWsUW2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام حذفی عربستان
🇸🇦
الرائد
🆚
الهلال
🇸🇦
🗓
ساعت ۲۱:۳۰
🔴
انوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27929" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzTc3sjJDdsUKvys0sinOaKhZRfteA55q-o1rmKeYpNlHvXE0zGFRfRRxThF9MkDDryIWvVv4niTuHzEQI_pRv_d0Xh9kBenU2GPNWrhzrVDiS1rO2_qsLdS_ISt2pVn45jUxtiN5yFovmsXTHOjpO9XQOpI-2RcS1Ez4u3U8hl7Kc6zJ0rOmEKCXSQZMiBHKZ7MbH5--Ml5Yr3PH-IbX5MrimFagwAteO9unksX423PN_ouldFxYTLmIoJBNVzQ1azdZG8U8WEqBKPZvogsbQZO3_PAOVrA7WBhnVHIG9B-Vbo9S-pakWAcg8DFz8KL7vnMz-trO5U6u2heFPbdsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شش روز پیش پرشیانا
🔴
دانیال ایری مدافع 22 ساله نساجی با عقد قرار دادی 4+1 ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27928" target="_blank">📅 16:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIWbiX3NcSVSF5pod0k6V9DU7Xx1No09fUV5NsQ41xIiBb5KylIYGO_9dDZuehyEBIMUBLQNehNa_RoU9qVg92L-nvEhrvkPzkTxvtajDnOFA1KyczygHpIfiybBYgmNTNzYcA8lHtIIUOaC7SuYNVme2ExWT1uTpnStTv_NcATEYonxL1iNnL4R608Ay1Upm46WZpYjjnT_nwwAvWM23AvhUyqGdmXG0ysPHov_fFpQWw0JGFLufd7GAL8FyXq7O7cjHEJQFpfJWinFo5RJ_Za9ctjWf4mdNxtrfDb7eaVk7B0gbLywbau2w556L-Z9salTbAnB-GdX4ejPwsauMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌انتقالات
؛ دیگو موریرا وینگر چپ 22 ساله بلژیکی استراسبورگ باعقدقراردادی 4 ساله به میلان پیوست. موریرا فصل‌گذشته 4 گل و 7 پاس گل داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27927" target="_blank">📅 16:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27926">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdde82e9ea.mp4?token=dOfvOrIUJ_oiLsHe5dk7ldCyB7aWYDYogX8wAq5cN_VHGJx3aDfNCIEuZ9f92eZ8G8RywSeGGP363jc3j4yFt54NESSAKWyPwb6y9cOlKw6xssV71oiC1rTOA4SVEFhgHpKE3zbuDL0UfS26eW71omnsTMCBMgA4qWA2Us8YGPCuvnGszoV490GSZQ4P5ULDMfuLxxdFNxVk_F-zM1uqME1G1s75-jC4ekXHpxggOYjwXUtXAhREJM0vYhaCIWrhQIkrnHT9STEVKuCLUPUBU7F0E87U9Txagp95-AvdRHMYr_yx3F4Wi4_mvhXyPQHG_RJstJCBXsVTNDcveX2MMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdde82e9ea.mp4?token=dOfvOrIUJ_oiLsHe5dk7ldCyB7aWYDYogX8wAq5cN_VHGJx3aDfNCIEuZ9f92eZ8G8RywSeGGP363jc3j4yFt54NESSAKWyPwb6y9cOlKw6xssV71oiC1rTOA4SVEFhgHpKE3zbuDL0UfS26eW71omnsTMCBMgA4qWA2Us8YGPCuvnGszoV490GSZQ4P5ULDMfuLxxdFNxVk_F-zM1uqME1G1s75-jC4ekXHpxggOYjwXUtXAhREJM0vYhaCIWrhQIkrnHT9STEVKuCLUPUBU7F0E87U9Txagp95-AvdRHMYr_yx3F4Wi4_mvhXyPQHG_RJstJCBXsVTNDcveX2MMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی شش روز پیش پرشیانا
🔴
دانیال ایری مدافع 22 ساله نساجی با عقد قرار دادی 4+1 ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27926" target="_blank">📅 16:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27925">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNb0pPS8tsoNhpYdjC5D_G2HjT-58Pm3qDruDGRig3Cmm0n56phcWlaArDHEZ8-cVnmuoNrIAMToWPJ_jwIuyXwmUh8eKf6Wtrmg7jBhfc6SclJwRYbt7HRDfTA74Ngxoo9P0mZDkqNXLn54hNAP6u4TeB7M-B35XjDqcsQzzhHx2FQfgqZQ2uQg_PZbkMT1jydkIOX89pT73H8Kb0JtQ7jPLjGGBFsPwwcRdzJ0uoKC2fsSKDGZ4jeG_wHvXY951QBOStPvdsABCLkJH1xeSCBxLKyKKNZMNS6Sl36I8KvuK_YR3RJ7IN4tK3UrFCmBhkfeONEO4BVoRy89nnSk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
21 سال‌پیش درچنین روزی لئو مسی اولین بازی خودش برای تیم آرژانتین انجام داد؛ اما مسی تنهادو دقیقه بعد از حضورش تو زمین اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27925" target="_blank">📅 16:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27924">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2s-y_hSIfxgwcQDhvosHaSgeU1fNqiz6A8DG0Xt478pdDx79GdmewRLM-uPEPukyY_n-vnIg-DcwSGqmIrIaWYgEyWomHcDGayMQtuOP4Yokci903zcMsm5WaNVxoe16tNQyR1GVbSIL0LH4XHEWwTB1gVvsAdJxZcPyHMp4t-v0_aqEaM06mhG4vZSDkjHaDd6UhKreGiA5vLdzYf9_7hSTOjnlhFMQ4TtcGvWGg1FAYUbYfdnPmhDgBAKYF7JD0H_oXDQRXMS7Mv4sCfzE0alah0gOgW5NKT9GjAUwc7ZOehrHLComJOlwOhrI1jaXocvh7wQBjxK3IcSTaG5Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27924" target="_blank">📅 16:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27923">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d79be75e0.mp4?token=tdc99nC-CI8Y0iPpli6sfbh8XXYeTUslLs-KKY081g6yb7_8LISpm-GM5QdVMZIQuz8gOuYpaPwz0vmPbI6KCH9M4ekI4T8sSTBwQt2pZxsLyY985vjKy-NG6bG--jSxu13G31hd7rhm3N993hI8tX-8E6A7eR8LNx9JR8lgBt9P0t02sm-9gxnHwLzQtecyAYca8SFDOLcFLdKTAn7m7vH8oONeYA-T3qCDIx8y_BABGvAL1GoaVD7gsTRMe16MHnTTJqPxyKbLBo_CEINpvMa64gm3aASf4MulSARPF9ucX1t3G-YRc73qHFDUHUAaK_HM59WHsLi7ola7oXzMLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d79be75e0.mp4?token=tdc99nC-CI8Y0iPpli6sfbh8XXYeTUslLs-KKY081g6yb7_8LISpm-GM5QdVMZIQuz8gOuYpaPwz0vmPbI6KCH9M4ekI4T8sSTBwQt2pZxsLyY985vjKy-NG6bG--jSxu13G31hd7rhm3N993hI8tX-8E6A7eR8LNx9JR8lgBt9P0t02sm-9gxnHwLzQtecyAYca8SFDOLcFLdKTAn7m7vH8oONeYA-T3qCDIx8y_BABGvAL1GoaVD7gsTRMe16MHnTTJqPxyKbLBo_CEINpvMa64gm3aASf4MulSARPF9ucX1t3G-YRc73qHFDUHUAaK_HM59WHsLi7ola7oXzMLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری؛ ویس‌کامل‌صحبت‌های گوهر شاد درباره درخواست‌ هایی‌ که رامین رضاییان ازش داشته: اول گفته خودت بیاکه باهات‌سکس کنم بعدش دوتا دیگه از دوستات هم بیار که سه تایی باهم سکس کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27923" target="_blank">📅 16:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27922">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KME8r91S8kr7wY_FMOEeevw-i1V4KUIriFbwIIlM0Jct6UrjkcFp-h9fEnSyJCpCIjANigw-hsUTTILaIVax1g4dwat8NhefF3PKG95jI4C9lZTJYSZ7yqZHARBdD9c2fJ9M4uypRorDtvVBN5TKbFLnNNch3Bz8I7y6q6hGSfaDM5GDOlMZ6fRbuMLW81PGrYHBQTl3R0B26zgnj_G1YNmVyWGRVuYUoJINafLllwCa17av251A_FlRhWu_7jJ-HuDMbSHZyRBzxsCMmLe6j_3FTD9eENs8zdNyYr3thltZeYHiHPFsJthUhbw6Ycfk5b8Lmgl7FaB8bFbVcE7e9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27922" target="_blank">📅 15:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27921">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooQO_-BwMAanPiytX25cYTHizTR3gUrqJUV3qsKTKEVSoGYiAfv_c7j4UasKWQJIUpEyaGakxV55dj0B7Pu6oww1kATWs2BBLi8uja-snZXCtYGwZYZ0gKyYLxaq-9sR-EAOIGeNx1KLJuFy_rJiIfMo0xeC5TNhe2syU-KRgoFRgJLUSmZgGAp5gLSpXMETze2qbEz2c_2qpbw8Bb3d4iNzJNx4Ma4HJEYcZ7GShaQ6YAtwqdvTLVEugBP57iPCVUZS_uKet0WkZ81EfFkcitxQ0cYKrvXbhvDc7gEfC-wEnt7gBo51kskGz1zcjh5g_Q1q02pqRVqShZzMW2nudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27921" target="_blank">📅 15:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27920">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIwt5mc8jfVojEpwTYWzoE_lZI4BFxfDudNZLwRs45o_FT6Wxt_1mnIZTKodrSNl6QWKb19V-_ObXhYiDQJRkf2H9ixTVVO1b5Tz-mtDOJt22bQio9qjDT9gMCcxYi_K27fZpQkJeuyhp45MdiwI4KhXtbeUEdAuduH5u9BEkVpyd91cdxkJOZn0FyTjZwT9RSnr2brjxM3TbipyOluXsIs0YY0Iy-teux1e8CHC_33z6myb98ABdzi8pM8v-585VEAGtZVl6eWkHh1t4n6fxCJ8bQnKWLw39La76eQYA5bNUOtURaMPa0ak6XrBGT4WZ0WMrHCyUjkiQw-ilOL9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مبین دهقان هافبک دفاعی 20 ساله باشگاه الوحده بامدیریت تیم پرسپولیس برای‌پیوستن‌به‌جمع سرخ‌ها به‌توافق کامل رسیده و درصورتیکه سرخ‌ها بتوانند رضایت‌نامه اش رو از تیم اماراتی بگیرند دهقان پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27920" target="_blank">📅 14:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27919">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e92cbf4ca.mp4?token=UlYxwE3lJepdd5zmypE_gsItvhsNWJUz-u-yIB7LZPtjL7Z3R4BcVaCb6M9YWy6VJWBaVx2E4zk9IC5XBe8npBbRWjsWposiKXfqVB3NuQrdChptIAoHb5hPAwPpSXA7lOBkAqhcaS0NjL1GA8tn2_lgnuJfsbry9d15OMpt_sXHIjwFcmseO0oAwlnzy0pbb24vf17EspTOrf6c6bDAPdhqAlD5YtZxw49aETFlRW_fiAqHp5utvRx4Z0r-fNwtSsTKdOsCrIeG66ntNZvlmjShbUonj_Zz1hN9s_6t4fWaoqGvRrp3PObkyLEA26W2RLZp2JIBWfeY9v1xIbxf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e92cbf4ca.mp4?token=UlYxwE3lJepdd5zmypE_gsItvhsNWJUz-u-yIB7LZPtjL7Z3R4BcVaCb6M9YWy6VJWBaVx2E4zk9IC5XBe8npBbRWjsWposiKXfqVB3NuQrdChptIAoHb5hPAwPpSXA7lOBkAqhcaS0NjL1GA8tn2_lgnuJfsbry9d15OMpt_sXHIjwFcmseO0oAwlnzy0pbb24vf17EspTOrf6c6bDAPdhqAlD5YtZxw49aETFlRW_fiAqHp5utvRx4Z0r-fNwtSsTKdOsCrIeG66ntNZvlmjShbUonj_Zz1hN9s_6t4fWaoqGvRrp3PObkyLEA26W2RLZp2JIBWfeY9v1xIbxf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
مدیریت‌ باشگاه‌ لنس فرانسه بعد از پیروزی یک‌برصفر این‌تیم‌مقابل PSG در سوپرکاپ فرانسه؛ به هر بازیکن تیم مبلغ یک میلیون دلار پاداش داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27919" target="_blank">📅 14:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27918">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzFJ9d2zFLUDRm5eC9LJJjkgx1tcAi71UJzdvAMRgTfhit1fCqZvhSAyE4uAIwaWiSryTiu7twM9SyPAmQ9xcDodqflVmFpbTTeMNeg9oCkhARZ8M2wgTDpdmaCemxvrhEKJC1aAR_GnFk2JxndkyiTFR5m0t8wGsDiMt26aLqxu06xsNoQV7PxH5dcGE3XJtGniv4L4UVz9zv7as9CrJ4-cFC7Jya4cS6757iRxca_tAGKeq3i5BtnOZhtD6pKWH3ZwhPnKsWKiZLcCs589I_m_nIj-lx9fad5SWeah96bHf8ftqC9dk4sZD9yineARLUjth_7__ScnZS8omrLpag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عجایب نقل‌وانتقالات؛ ۱۴ خرید در ۳ ساعت!
باشگاه الرائد روز گذشته در اتفاقی عجیب، تنها طی سه ساعت از ۱۴ خرید جدید خود رونمایی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27918" target="_blank">📅 14:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27917">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6pVeg38_p9GqF3V1qKWPNdvKhXprw3K6_KHZ9lbGJCJM26I0DubRCQQHnAVuFgaFqa-Pv6Rx52Qm0PkXCixzr6PAxMriiQo3diRhj7U3K9VWd-ePJo5_kLVNLYzPp5k6AXLv5UrMPzRqyhWEbH7vYzwoj_ECLciYZFn__5w3rl3pQlC3DoQvlveVtlDSv-W5NNvtLwn7P8Gv39qJFeLuh5S8RxrmjxLM2TelKhQIVdjLEaIPJ8zKbWizyJakd9fu9r5agktFAJkUJjcddSlnanPBhl8I_iAAS0_zBv_trDf2LwZrqWSLZ4TjbGJDHmcxlKGtwemnkPZL4862MBdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27917" target="_blank">📅 14:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27916">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs4r0RGKL5knsbPzDSyo-MVLvfotBDkzMONZyCd97OIBGlE_acU9C6zf0lcBI1cP68OCcMy67YULPmHciG97PywIor5WO4lF7Zmqi4FfG5-LabgyCdgIJu6008IeCF0SrlRYrEdanAyQQRYCWvDtsragvVMGy5wgIArBhmgV-kR0SLEVHVi5awqDi5mSOPot-UiHIFOpGM1ARDEHEsINZhpGUi8D1AuWxJpuARUuAgGDzeVcynm1by4S5-vpOOenA2mRV4tynSgsSFR_Nv-39EOZsQGo3x3ufm_0qxqopmVs-umu6cvkS7ZrrArrg06tKvE4G4Z1D3vS4p3mFOZccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون و آنتونیو آدان دو بازیکن خارجی استقلال تاپایان‌هفته جاری به تهران خواهند آمد و در تمرینات استقلال برای هفته سوم حاضر خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27916" target="_blank">📅 14:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27914">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQpZSeRVBcMtdNE3IYe4pNbBzZ8iHKuSfriQ_9tAdIF_-0KjVJ9jWvqEzvlW4Jd-Xm7iVLK4HMYS0X14RMsp2mIuGnXDR83GENFB56fYR2i-Kb145-fmrwwHSqFVA9-ArcoA49Me_olBy1L977Krjh0PIaxT6EemTSRnILEyJHadPsP_smG1JttWzTQ0pL5XDLFC8PWy6yfTcjh8eoah2F-dEPCnNju10VAai5Xd-wtm-PSoog6EfaDhwvmWhSri_9yG1RbvxzjYaZ5xgVFOPUme7qoHoUEEIWPYKHXXUUCjW6cemT5htxzinw4SOuED5t_UmtE1jlHQNa5oyznAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KR_AznyaBgrWKQW0ulyLzOhLao95thcgKjbD0z-rtt9iEzIW1lgCtKUXneqfo8gLPSU9oS0s6w3p0oA53D7RIdbjFvBSC0mbCp_YXevN4J-k7AvTQeS1aCbkAAIlixNzg0yoj0VEM0NdaChsGCnuYG4tC9mZamyAUQKj3GlJgWG2DXU05ST9RKkj5p9MLUTlFXJ8jqH6LLTKCh1I2szYP-KYsa0llrM9jJGutRSkc5zhiVUSLmi19tvucDqxnPYoiwgY_G_uRhWV8X2d9x5nzE8wMQQShe3bxwrKwYwNsemTyfplSvlDFMJA3J9ZqvChfLHszIOdjw3IzaMs5qKZAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو و جورجینا رودریگز در اتاق نشیمن خانه‌شان ازدواج کردند!
🔴
هفته‌ ها بود که اینترنت پر از گمانه‌زنی بود درباره تاریخ، مکان و لیست مهمان‌ها. از جمله مهمانان مشهور شایعه‌شده از فردیناند تا ریحانا بودند. در نهایت، عروسی این زوج در یک تاریخ برگزار…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27914" target="_blank">📅 13:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27913">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q07wzpbmtioiN_PaWPIIc1vD51DOSgzNTfjFx6-XKiSgP6uJgayJu_R1iCi1vBRX_SbYzWyjUuQ6RZCzzhxc_rlLWolxEufhzD8A3wdDt078EZM2M0nIifF1BOW2Qrne_NsniAqfALsNqGTXqN3boCD0Fn3RdA4i79wUdC_aeXAr22S8oAfrm1LeC4jgQ2s2eqRcUikiM2AXqSD5R5MCTWLqVfOZqIXKgpO_FbRYdtDOXcuhCtzaTqGX8ae5S_-TLUpIRBcCEdep_ETfyFjuzVtuucbMwGxovhDnphdykGp8CuWulfsEkb0FUNqfeqChX5GU6rTl8sR0XOiqZHqXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه شباب الاهلی درتماس‌بامدیربرنامه‌های رضا غندی پور اعلام کرده که حاضره این مهاجم 20 ساله رو با رقم 500 هزار دلار به باشگاه های ایرانی بفروشد. گویا غندی پور درلیست‌مازاد باشگاه اماراتی قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27913" target="_blank">📅 13:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27912">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3tjwMl_kBOpPwfk1xcMR67ZxINukTLvyc1x3Xixft8Eosf84e5DzgSBmBJtdGLDMfhJTilJ9hV7Kfyy_IyALI-h4PNpQsULyu7-QfYtLM-Frz0g-gd5oTsm4uVBOQcFZmj8TMtEWcvV6G0JDwQsu1G88W6M_e0GDAnx4kex00QGk9xDKrd2EzYq6ts_5Y4bAq3YQFrnSNmC05cURhx8W7b9-b_vkdxeFSurIOan5LLLXI8I4qLTiDdDdGdnWvrNh9mEnRcvSX1j6YGTmMx7lzRvPNxmM-WqHAmBmdaA2rqmQOctO0M6OeXvOuicsvQarmeKIa0SgpYHDChForhr9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گوهر شاد: من‌آدم‌کثیفی‌هستم؟ کثیف اونه که جلودوربین‌ادای‌آدم‌خوبارو در میاره اما پشت دوربین دنبال تریسام زدنه. من اصلا هنوز چیز خاصی از این‌آقامنتشرنکردم اما بزودی مدارکی رومیکنم که  شخصیت واقعی ایشون برای همگان برملا شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27912" target="_blank">📅 12:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27911">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🗓
هایلایتی‌خاطره‌انگیز و تماشایی از دیدار دو تیم ایران
🆚
عراق درجام‌ملت‌های آسیا 2015 استرالیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27911" target="_blank">📅 12:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27910">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrC54ms3p9Epx4fW47k8vf3Y0EKdwNT2333HaQ_lcSbJwHl4ChrNepzH2BludufernAZNsgIAZdS2Bfiv4aGE5-LOa8ExEKcYUphFgK4I1S1Glvhyu_xpNXJpRPfA8gzWDWmZwrri3guIgr-TU1n_jMgVEHOMbvSzeSX8fQQWGRZ6-lfOczdyavzqw7FHkBBmBC0Od88g1LYfmRomu3DmWxtanA6purBmqWUNwer22fwOySbwaQXqo6M2G8_lLHBdL7JdyLBykqEA08rrk_iEt7NfFjK4MN0UWqurSIGPxtrMpgAYu6BccbYyOCgmpsq3ytfoWQCDpLSI60JUv2vFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت های لیگ برتر؛ مسابقات این فصل بسیار فشرده برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27910" target="_blank">📅 12:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27909">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXD76HZcZ7hJ7aUl3XYWRmRhzlhAxfP2VcrDq0wUygGTGHmhX1q2iQzbK99xGb5rH3CASNKgJ8eb-08xkEO0fZRalss_hW_6PdOhTR4EiZWqFPO-eXFmlM9O_irnqO0e0GI8CLB_oVK4Fec_LBj6RxPcbI_AqIxvnZH08XgCeyEDz13XCPQeQMz2mDjKpijsJUESctd4MnXNNkNUtACvdUUN5s0xwBq92YusBDnhzv-mw4_tLNPxHCXShUSQ8grXKPaxX0tnXj0SIMj6UCuIK-fqoq-G_Xaodbmry7pANRh5hcNRiKjhWhxanZL1lhKiWa-UKTPUv9tNj__MVb0ECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27909" target="_blank">📅 11:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27908">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY7q4YYhTk5SVAPdc_-YSVk8uz8lw1YqlP4isMGSLuxItdh3fDeygNnTbyWImH7_F7JDVIQiwAq4e8U_4x575Sp74rAYWihcNi0H_JARH2UzhkmynItY_oQqQNL07qjxewFuSvwAK_Br4vdLqR6qQqAiOLlwi-AoshdDPNH49iDvRGjv-1G6of2p8Aji-SV9JzspcbGwN-00vgi4oZtqTIejoYW-XDxqz8oaYpyeSpD5eFR4CjxvfCIP7qYUPW67OlIXFhaLAxKOVPjY-WI7K3Q5y0gmHEV6Dl-0JNWpmK8vyU0WDTZ2zihU1nweTGhCJq0ayXx6n1yedYHnVD-YaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
دو باشگاه استقلال و سپاهان امروز تمامی مدارک‌لازم دال برقانونی‌بودن‌قرارداد آسانی و کسری طاهری رو در اختیار فدراسیون فوتبال قرار دادند و بزودی فدراسیون در این باره بیانیه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27908" target="_blank">📅 11:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27906">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rucTI9KzjYZJKTA_66jNuYB6qwo9Oh93IRKN-2BxnZS4k4_tWuYTmShHwi-ynEvUhx_HpBorqAX6cYzCYzI9OwF2wl5TRWTu-PGILhbL9PWNGGqCrqGk4LvUwpA-ZaxAmsL_9DESFMdXFOHVzzSWuD97766V-KkfZxdDsioHKZlrsc67XlPka_k-Co2ZtGHjtiDgDVMOckaBgIgIfgpEgGiyVT4F4xFCuxPVhwrler1EtcvqSVLUgKLLrctURh7hrRxWlp54CaNgSeDRRRr7eJzquwjA1BAS2JFEhvOboJThVzrjGBX40z2w0M7cwUPo3LODiv308kNXmxU3MyR6HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27906" target="_blank">📅 11:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27905">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec510822f.mp4?token=QA7XxgamifO7jHpl5kLZYLV8HKbztcfcYCPGUIYCVB7uZMyGguevDlioHL6rSuORJUmyuHuW_HHWuu4SfqxM4b7H78ZLe0PdA9l2ZzDEkEmT61EvYbLS-7HPNhQ1WQQJeqYAAcBxNf0oPAG0fVIudTlPtj5BVTK5CM2Qp6VNrgCtqoe-ukpILv0ULSvzRfL-Voc9Y-WQ1LD9iYkvMGHPrYG2OCmd6UAxln-yxBt3UO8EcPBeHaKOedwLnJPSkbjScUDV14tEuls_HiP2sbLgevi5jO_kx4NEo5ui0Sa7XZ1q1OZnuVmnfqUcnKBK374Q87UxcZNa3pAwuLPQGvd-Byr4TuWcpN3ThAJ4AEP7S1Sh0Z8EIQy4l-r0YzmrUBkrLEhBseJ2EunL2kj_tMkFTVvEzdvQJ7zcoCryO0LVwVBh0WDPdRtifstQnit8AWXojo35kpY8W0mzYIsE_1pKBgLf7Dz7N2rEhQEdanN34Bw6IoBdu5M6827QIpYWI0d2NcqhE6cmZIFYj4duLaNHY6QODBMtGeO64hbkSx5nnO5ENe5xXtk2t1_W-V_cDi69Vf-eiuycpL1I8btmhDFjgyxzynghwrdOdon0TmNwfk7OKla76Tn_6aZQ2q-O3yLFOPNzK5pSHdxWeskyXY2NhxTrgsnYrOcmJFQvkqZoYLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec510822f.mp4?token=QA7XxgamifO7jHpl5kLZYLV8HKbztcfcYCPGUIYCVB7uZMyGguevDlioHL6rSuORJUmyuHuW_HHWuu4SfqxM4b7H78ZLe0PdA9l2ZzDEkEmT61EvYbLS-7HPNhQ1WQQJeqYAAcBxNf0oPAG0fVIudTlPtj5BVTK5CM2Qp6VNrgCtqoe-ukpILv0ULSvzRfL-Voc9Y-WQ1LD9iYkvMGHPrYG2OCmd6UAxln-yxBt3UO8EcPBeHaKOedwLnJPSkbjScUDV14tEuls_HiP2sbLgevi5jO_kx4NEo5ui0Sa7XZ1q1OZnuVmnfqUcnKBK374Q87UxcZNa3pAwuLPQGvd-Byr4TuWcpN3ThAJ4AEP7S1Sh0Z8EIQy4l-r0YzmrUBkrLEhBseJ2EunL2kj_tMkFTVvEzdvQJ7zcoCryO0LVwVBh0WDPdRtifstQnit8AWXojo35kpY8W0mzYIsE_1pKBgLf7Dz7N2rEhQEdanN34Bw6IoBdu5M6827QIpYWI0d2NcqhE6cmZIFYj4duLaNHY6QODBMtGeO64hbkSx5nnO5ENe5xXtk2t1_W-V_cDi69Vf-eiuycpL1I8btmhDFjgyxzynghwrdOdon0TmNwfk7OKla76Tn_6aZQ2q-O3yLFOPNzK5pSHdxWeskyXY2NhxTrgsnYrOcmJFQvkqZoYLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
توماس مولر که پیش‌تر از لیونل مسی به‌ عنوان الگوی فوتبالی خود یادکرده بود این بار در تمجید از کریستیانورونالدو گفت‌سطح انضباط و سبک زندگی حرفه‌ای‌او بادیگر بازیکنان‌اصلا قابل مقایسه نیست. ستاره آلمانی سابق بایرن تأکید کرد: «من هم بازیکن منظمی هستم، اما کریستیانو…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27905" target="_blank">📅 11:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27904">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac05124de.mp4?token=v47CGVSGnkKm_6HeP9J_FXCniD2YU-BqF_kn8r5Sv1cp1NYoEK9g5p97sBBCi5d5u7k5YkBTdzINovBIXxgnD03tEmtszktvjeE59uNgv4H9svvJ8oLCp14kohIuEzscQ7Mz01p_BmFdd1SWjI7xT9jb8utzqpiri0Y_fEgfy1w6j0HKwas7uq10j8flo-myhNIuSMhjDMI1_OjbRj8PdEyl0UsXNmyMroUOXrR0H8xODGJKYuNJayiALGGK6fZp0HM5NqtZyOl9q43m8VwMi_F_Ej761PWLt02bEjSJyaIo-hNSxFZRLvGtjA6UWUnKwXHwdX1ddBdp-zdzwhlDcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac05124de.mp4?token=v47CGVSGnkKm_6HeP9J_FXCniD2YU-BqF_kn8r5Sv1cp1NYoEK9g5p97sBBCi5d5u7k5YkBTdzINovBIXxgnD03tEmtszktvjeE59uNgv4H9svvJ8oLCp14kohIuEzscQ7Mz01p_BmFdd1SWjI7xT9jb8utzqpiri0Y_fEgfy1w6j0HKwas7uq10j8flo-myhNIuSMhjDMI1_OjbRj8PdEyl0UsXNmyMroUOXrR0H8xODGJKYuNJayiALGGK6fZp0HM5NqtZyOl9q43m8VwMi_F_Ej761PWLt02bEjSJyaIo-hNSxFZRLvGtjA6UWUnKwXHwdX1ddBdp-zdzwhlDcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛باشگاه پرسپولیس برای تمدید قرارداد امیرحسین محمودی ستاره جوان خود به مدت چهار فصل دیگر به توافق کامل رسید و بزودی با حضور درساختمان باشگاه قراردادش رو تمدید خواهد کرد. محمودی از باشگاه قول گرفته که شماره 10 فصل آینده پرسپولیس باشد‌.…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27904" target="_blank">📅 10:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27902">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiX2iavVv24uAPD9JDqYussyxV2exXN3pHZltME40ToRavBssZBgKs3tPdDrqvxWaRyTs9g33Xm6x2twoagTrlcZVWYvMoN-7RhBc55Qv_zNL5-vU4O5soQElm-W_4UqS4jnf33PdCxIvuVzoMhP2TnCH0P7LBPlOZQtT7Bqo_7OQ_Yn1hUYFnNTa8VikoJTl-FEXWHvtzLGDRIO64DSBUQzjkgH0U3OAtg3mW4SDpcM0UTccZJYS8sLzo7f0XWVeJnfgV3g7GJPp6BTJeud_3p6y7GgPuihdF-pzlM3SIeZYHdx7vcKH8EK2zh9K_a8TAXtSBGqbrLfpOWPVqYqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی ترابی به دلیل مصدومیت 4 الی 6 هفته دوراز میادین خواهدبود و بدین ترتیب دیدار هفته سوم با تیم پرسپولیس رو رسما از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27902" target="_blank">📅 10:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27901">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keh5gY2tVQj7WMEZZ_Q9JXzfXz1OZ7zYWA6lehc3CJ-jM02LcPjc0bG8qcAPUzqq5Ka3mSYmdatP1KYVroqyycfTzEINWHKRKZ4WmEWN0DQcoNS6gNy91YDa7L46X605gqNwtVVkKsLYjx7Hv-_nqtPKHsWixBM6KBZINvl_sJVuJaSnD4A0Igw4LGPfovMwDwyWzwhVujuA9K68TL-OqH5G-_DiZ9md4OTjjnlb6rxyjt33Z7ycoFt148rY03ahvX1sgYiqR7MkGhxNz5kYnEjhQxgZ7diW2oOoP4Oxb8JqBrW01O_hYPYix-27oXmX3gTXt-JeO3pnDQ1WNP5xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🤩
#تکمیلی؛ به دلیل درخواست 80 میلیون یورویی اسپورتینگ‌لیسبون‌برای لوئیز سوارز 28 ساله هانسی فلیک به‌سران‌بارسا گفته کلا قید جذب سوارز رو بزنید و تموم تلاشتون رو جذب آلوارز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27901" target="_blank">📅 10:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27900">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZ2hxWDI95D_QdF_yQxkNzXHpf3nbOKnD0yS-FD6PGevwoj_y0WYPBsxAgRcnnV5akNCbKGeB2NgVa2_aRtNjM9kzqch8uJVwgRmdunvZaE528XOAVP0hRIAJreDsbqu7yBoqlICOTmNXKCGRdO1FnnBfRgxy4amlfvnFykgjhTww2rVhtzOjZrcnZkElHq5HVqTwsXybU5bblnBneUZfPZEofVfqTCaaytFz02l-hAMWvZ9qG-yv8PdE1QfhnXjY6lt_uzE398CtKb9VSkhNjX3WE6_J8TLElQahCOh6YfuvHHDfFBUXb39V-gin3CFgd22mIqC2uxWZSE-GODkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
مهدی ترابی ستاره‌تراکتور از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان همچون مهران احمدی یک ماه دور از میادین خواهد بود و دیدار هفته سوم باپرسپولیس در یادگار تبریز رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27900" target="_blank">📅 10:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHUuTt952zkxPw92ACiAQLAYYO6ZLUXqEviQdcf-zG3ktftgIHtLjdGRcZ3aEACoPzAeEg5p1T5dtXZfsQSGpGeA9sBK2g17M7P36mbgrH9bn7uxSaKTQxrjXkVA7m6psvske4FK8JH-PPfEKQoEqQnwKU31PUJnnLqPHHN9dacztHYbaQEwysn6AoIA5KUn8uWLFdGUX7rJmqxTU_lc70bqrFB5hOWJ_a0Rb96mSZ2iCs7jTlsirQQkzYGGgPyecYIgj7Rom67dHn4ItpvTnqwoLAU7Bjsz37BzCJG100rLhzmV1VcPoilajoEoIeilLWTHWiD9nvIrDDmVKCkjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27898" target="_blank">📅 01:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27897">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coB9SehzHOEIm4BpfKUxUWtD3EovdkRowmlf8Imdhm1yU96CjARddh7szft4qRfd_aXIx-Ns5sUCB56_rRAZz_Tw-J1c5_dKEbdCM8eDHB-KDIvXRWh2lkww1zxhQwqE_mWf0c9kj30FeAeNNos7iabpMrysUT9ZjZOJLEo9hwK5lrubhVUqPi2ZCv4ewxYBlMxdcQH1IQaAUqgu6mll3Nxd-BFVgXmoYqe797PUNcbuEW0yJT_1EvuBJPjpENXOOLCXqhgesSrrgQKntgSgz5yltW1jm3hLQr-P0RlrvbLxFoTXvZ_Jzy4hK4IlnCIYmuQeicHrpnq3cnPJuLPPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌تنها‌‌دیدارامروز؛
بازی یاران کریم بنزما برابر الرائد درمرحله‌نخست‌رقابت‌های جام حذفی عربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27897" target="_blank">📅 01:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27896">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHgrtDBTHWUJMbmz2Ap7lK54fj1HARjCM5yWlnF9iytH40IoB11zzlA_tJCU_yOMlt-ZrvK0GMLx-4ptDU9hyLaXQtAQ0_9SwQnG4NmiVEnBUocqmgBybXR-jN0gV5tppvvn8hPq4eMFRZJiOpUc-M1gVm_LavqKiiJZM2rjZC1yghrJf_1iTdDzsL-DBWpHDfU3bi2Bol1Nwl86-9hnynmu8T994ZKUM-Fpx2IWpIpIhI7bAWOKq69d2a9_H_OrY2JzRqT38l2tAEmuOp3kNB9_4IlVFWdgF6NcO3btEJT4QqyTJhQgxa3_-Uo-KyrJIRGM1DGHQ6wJNi-MaZQKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
ازپنجمین قهرمانی آرتتا در آرسنال تابردپرگل بارسلونا و رئال مادرید در مسابقات دوستانه و از دست رفتن سوپرکاپ برای PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27896" target="_blank">📅 01:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27895">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATz44F6DKmpIM6KNzXW5ppXah8BNTyvZJEMyUu6Wil-kynLybV9Ypy8dVhZ8LUOx6vJFTNvN8jh_B78l2aD0NFxVHuXpDmpwiPWxfGy6NuN5AdmrUE31KWa4GKF0ftDF7tEQsVOT0jt3uNWA-r_hIpBF_XZeEWYwLC0_7NbTSALRhYYS7qG4tkYvDTwrF0XwfN_mB3_o4Y8crUcanT71r_K9Y3QaKjJKNAWEtTxWueSkaQDZv054m-Lz2gFcC_YCoW776bWchCMpmCXcQbQjCDooA5mZV4txjVvz1efjb0JTLoNObUIZDqWv9AcQLjS2WywxRUTeJKvyyCygctg45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بزودی باشگاه پرسپولیس جلسه‌ای توجیهی برای اوستون اورونوف ستاره ازبکی سرخ‌ ها برگزار خواهد کرد. اورونوف شب گذشته در پایان دیدار با شمس آذر درشادی بازیکنان این تیم شرکت نکرد که باعث دلخوری مهدی تارتار سرمربی این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27895" target="_blank">📅 01:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27894">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFtOVctRgXKM4eC8GkskkHf5LMSWxRMpT4btlMAXK-zYIXaqA4WkbgJGDcygPjuVPWs48LMZKAleM4P9vfwvvz0ozr4kUhsJD6MUP_s0rUov_XUwIhX5Lh1R_w7m0ybBi8gLBO62htSamgq5kzuR4QER8vjh0w6OFqWNmuknU2WQAYCiWsOAA_gbDXTdGW2UjpI13ccJedkqrfxftbBlP_puJz0ylJJ48zcKlfUlUai9MqYrMa8hOcBO3ggdJqj4k-NZYPj2MTLaRkLVjLSSZKDojcqQcLBKTR0-_rktgqCCxHcm9ohm_HQvkH1P5JtjGoMgDzbcZzkHtcMYV6RcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردین رابط وینگر سابق تیم فوتبال استقلال در کنار همسرش در تعطیلات پیش فصل رقابت‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27894" target="_blank">📅 01:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27893">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efS8teLPbWueDJkeDXi-xqIA4X5vgpJkK9bABf5ss9bFpEYsEXFzK_adcqMh8iZoIwi9cVZZ1HTSgFQh-E68uDYNTXXOQXBeAWyWE_F9GQTyPOv7DARs2iyZoxjux9lHrWRWke0074y_y1FNlZ4aVw2NwfJ86uY_oGZKeywmpmptl-bGEMvZta75fan8dnBPtyT-1iRvbmchLNzPo5woO7eenpgquAYGGV48j4Hj3B7moE8SyYd3WCBBGIOdePFK0K-9Rknra64V1hVZyKkF1QCpvYaMNmCwrw--BRko7vrbAvXEu5umdcITPxHmiqTx92Oyetk26HZk44IJ58ErBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپرجام‌فرانسه؛ شماتیک ترکیب پاریسن ژرمن برای دیدارمقابل لنس؛ساعت22:15 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27893" target="_blank">📅 00:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27892">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZlAOjd4j7THjWDqcslkq6EuA-qTq-kT-_oe8WrTI1fkFiSVewwpj6GWeJetfsYkp9wNqKp4nU_M7UZCbTp06pv4OvpT4aZq0i5RjeTXFgB7r2Ga_7Hzm8K19wm90-NvbQP37a60wP9XLWhdPO9v5VqtaDh4EpiRIktrE56PATLXUrnoo0wmded46vVwVmU7qsplkX5uN6bEhK_GxSqnroiIjMmL06W_i7of3-wlVm-zwrt1CVX3AVka9RvJIl1H2soaeS_4hxF4gnXmiXMaWf11JQKGunxS4tpKlauj9sSXCa5z4yM5YzV2QrseYdvoWUwrICWLgrasTdFRdPwOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بعداز جذب محمدصلاح؛ باشگاه ترابزون اسپور با عقد قراردادی قرضی تا پایان فصل داروین نونیز مهاجم اروگوئه‌اییه الهلال رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27892" target="_blank">📅 00:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27890">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lemN-0rNKpXbOJk1wOSQqUe_Vh2uG6iq4UI12yAdJCYUPAH1HitQzqmG5mLyPIgO2bcs2m-IY-I4HLlTTYa_-GraImDKAyk8F5znSNpoYA7hs5_aFbVhHtP7izWlNJIBZDmyPe2AKaAO_1Qf__-CdLPL9s4lwIBSpbhx-BNJWHqjYmOVpqKLqCqgEJ3qu1JxCEGAbOuemVNx7Wf9GdfPttCnEZSjYPmtrgpN6KgJjv9GmOYoKvwfcTCp__ekD_V8q9lZCCNv6WWpFmQjeijo878sHi_5rsAAfcL1keq3iq760RIJWSbob8pmohfZdMl3M2bUKpvbsbFB8VTGPe9tTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmXfcVUrRymTb7Ye7O2PxVFaE8VZ2YQ6mLRH3RKGo8LWvs0TTBmFLCsO9CWdIgMlj9v2p0CVSgMx9EY2Vk2CDk7Q7pfyWJKJf-ARAbUPRgJS0v5IEEqbJAzxxKiqMyNu0d9GoNQWUEl9onwDGCDYT2rDjpVmFgXzU5BNyQgFbPesDQewlGxkCjkv9KYcnT1R4xlQEPG-spyA8X6fBT0AynBfcBG4NfiUrzDjgVqyrOjwx3qGePG3zcmnDMIizY6UOZEoKIrcJG4jWb-q6XjATOP6M8B5Yl0TA8OAAfe3lW653XeHaqgA4dllU5Ep0FENzCaAWhPwwbkKXexeB3hpxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
مراسم‌ازدواج بسیار ساده کریستیانو رونالدو و جورجینا رودریگز پس‌از حدود ده سال دوستی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27890" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27889">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3nhF4J5AckuRvnBgcbDoSePcOq6DmkjOEsqUOm21vM7eVD3CgU_fuAKyH3iav0z_oJgcDp8BnHKLlzoIKT9frcvq152R7MqCUBy-GYCy1NI8vcGh_R4jHKBXmyaai3YoWrew-yWB7zax9WtSQv7NJWXMUGyuN4IWUn1yA7zfUzX0lwMurbdyqgz0QAc_wUjrcbJYRRmKRFzFtzf_SehvtVQbjteKngOOS7lijchrELP2W_CPHB3fFRIqK-e7RjMEjF8LTd-Rcr122ZDyVIBV_af3YfvNhOtw-qhczUSsk-zL2-ABhjO9vAbvXh04kCWehJqbVF4Y1S1YjQI5MR42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ سازمان لیگ و فدراسیون فوتبال بزودی درخصوص وضعیت یاسر آسانی در استقلال بیانیه خواهند داد تا هر هفته جو مسابقات لیگ برتر با شکایت باشگاه‌ها بهم نخورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27889" target="_blank">📅 23:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27888">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYiAawTwzCVl5IL--IiGB111gAX6S4B9sUL9VmQmQDrBUfRGrOnNOhCSdVCgjJcTz35IZgVpa5fD1gAd0NXJVKCrffTu2_3tzaR6qmwcETpuh4H4Xu7JAOfYZexew13u8O9xcfvwW6f6iisW8QvSJrk9Vd_8h0_XhOH0oCC3I4tyUFMC6dPeHo0KAM8CXhQ9bRa4T9D4VASomlHZvczRv5fqBqo05t1VujI3GraIlJwFUJ7CqBzr5gLwnA4AYH0msyKFMFimB9VWXQTke2Noxs9D2b33eTuhqBZAxKdoH5tf08ZuR_pQd_q4rTZusrJ4YKNW_zVgiiR4XPOvdv5yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
دوباشگاه ملوان انزلی و استقلال برسر انتقال ماهان بهشتی ستاره17ساله‌انزلی‌چی‌ها به‌جمع آبی‌ها درنیم فصل به توافق نهایی رسیدند. بهشتی در نیم فصل با عقد قراردادی 5 ساله آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27888" target="_blank">📅 23:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27887">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk_ufB9SS0Gy2K7Nj8J8ncmkqGuCcOgoJUWFMxbaJ0mxqatgH0f6GDlzY_PzCR08Xw--REWai8txf-OMnfeQBVdwyeZSg0__jXNj_kaBFqGYkmOqbYQROQ0rTciq7Z64nyDZqz0WqWwHMCrv2qoPNjnD5FvZTEIWmiefD8rEvd8KAq57MJjwLIK67N7raGA5Lmy6TuF4osjJUsleLEpOcw5uEF4SBjqCfhzQt0uke58bMCiQrGZSOG7lgc-azZZYGGZe4X69y36zzwEXCwCOgicjyx2T06_u4YtXDvE8towjeiuYl9maPEzbPeqwapW8DdtVnesf2DIE9sBUy1_eVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
بااعلام رومانو؛ رودری فوق ستاره اسپانیایی منچسترسیتی با قراردادی دو ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27887" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27886">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b29fc31c.mp4?token=eygPKHBPAidvC_9xKGmw0jZJbFIkNddYcPjMCCm-sU1Mm-TL8q0nvmjUq072KhSzujVDClKcrIL06t9l0zo5C5dADN8b6ojkX88Mdo6FGRkUunLYNTOp1wHovJzxS_Oq5RvHO2QEVLGf8nR661JWcf_hoxy-IyjFwOAQVmwROipl5iHb7ZLX4nWXh6PnmbInP646FvlAWD60K-CUIrosJmUw8Ie0CcaWPP2n_jXmHa4DnC2T0KwAgOX_PyxDz57bKrsP3RKHsAke1lwQY8m_dbiFW7pQDBX23RWqBL40OLDcrcPDXobgqyoBuK39VEexw4Bdbyf8h1RKGCqrDz1x3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b29fc31c.mp4?token=eygPKHBPAidvC_9xKGmw0jZJbFIkNddYcPjMCCm-sU1Mm-TL8q0nvmjUq072KhSzujVDClKcrIL06t9l0zo5C5dADN8b6ojkX88Mdo6FGRkUunLYNTOp1wHovJzxS_Oq5RvHO2QEVLGf8nR661JWcf_hoxy-IyjFwOAQVmwROipl5iHb7ZLX4nWXh6PnmbInP646FvlAWD60K-CUIrosJmUw8Ie0CcaWPP2n_jXmHa4DnC2T0KwAgOX_PyxDz57bKrsP3RKHsAke1lwQY8m_dbiFW7pQDBX23RWqBL40OLDcrcPDXobgqyoBuK39VEexw4Bdbyf8h1RKGCqrDz1x3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مراسم‌ازدواج بسیار ساده کریستیانو رونالدو و جورجینا رودریگز پس‌از حدود ده سال دوستی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27886" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MetORDxpIeykXYvm0wthxU0Dt2SIw1Y1Ip2AszWvtwIcbeCHNyggbRv0L36DvIlwED3xufWnGoyzu_JKP9bgatziuGJRkcbbHAz-Gf8q0JYUCT8ooOQn9UyrlFHGor9gEZ2PXnCxOuAcXleylruhOA-uW-iU5I3W8Ta1SCWLmCB4HZ-E0cHVYsmmbynkcuh9ozJYQ7hf0zFajoA7iMOJRGj1DtMOq8ofkem7-xtHh8J66YRItzHkuEQJyMDgNjLWpq9QOq6_6ZfEDQdrhIKxug2_biCvXt8HgPFbBHdmDv8Miua3ksVaW4ek3dpno8yWtXwyDO5gjb1vExDBoBsTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ESPN: رودری به سران من سیتی اعلام کرده که به‌هیچ‌عنوان دیگر علاقه‌ای به ماندن در این تیم ندارد و قصدداره‌راهی رئال مادرید شود. شماره رودری بعد از عقد قرارداد به رئال 18 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27884" target="_blank">📅 22:17 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScpjQHzGR7bEFgxzDCMIcaB0Q-qwPKSd-pleK-6yEriIWG-F8y1rdBokaPtyVgYvvOrpVM_sXqqr2Jj8aDQDhvy6rRN12l-c-iZtkLfeZAAe6v1y0uHhixdwBKfonK7I7VJzjvYzwFM04-M7_8QKITfTdKLLH0q6BDj9Dlj0O4HIRdOP-R-uJ0HCWWa2S9C5YLV6GfYO6RM0R1G01isGMA68W8qDUn1bgaKk4RunzSmH6UF1GbFgXanmjNMSJYRnUppP5VwGCJctK3fyU1gfPJzuY2BfYdCmTcxJ4BRmP0QPL4chZWuCiIzZleXYq-liXBBkB-yJJ_O0vWS1_vJAjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27883" target="_blank">📅 22:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbezn-GmvsRxCQEOlGqF2kSbiW8vOZONAKaZHdN-vgNW-jufofpZiUuoW_-3IE9othBx3kdIBFqfu4DfS0v_TDSYU3rEf6i6x-8mweOS10nAQ7mGCr1Oz4vFcbQkSczR8KG_OQJh_pUBjftH2QMnA5EiceW2oZ043vWx24Z1lfpBwwyxFG1j9IzkK-N5Wcf751ih4XC4f6X9WYr2vsBPFkEDZTqcYK2LJNb86Wet1wcuxC9k60UnyvPAfhSfkQEmOoOnS_hNeEV-0Jcq1aMbN5YqV68BwOJt_RnZR2d8O3fXqx2hJ7timUp-vE87l0cdvX5VoVpOB4beh__9tiqj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیروز گفتیم امروز استعلا فیفا میاد و اگه مثبت باشه باشگاه‌سپاهان از کسری‌طاهری رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27882" target="_blank">📅 21:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27881">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7uauCvwnh4yj-LY6zSEfuFqv43dXp3R5BavX34R2uWqJgW0GyrJU5erzjBq1xuxEnleozWlpMY9waMHXgfXIcJl9AxfO-6jT7xBFV24gFC5iHNSBpGrml3bLjlGEgq4bulrqSVRVjEgPbhfEZJdcbiGQ8zkQPFHXFOHNewSEJ_eC0rz22GVqX_yfNVe4oijj0dwqvFP9tbnXZDWla_umVIdImJUaBB_YfZPQ_Fz9sC0xY24zQr44szWzUsm9MUq9nlE21YEM2vpY5mXNKVA21NC7-I-0PBqmdYfYOrdkBBcBXXXimDdHENwiCE-gSJqpgoJLe6wOoA19eayRTdIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپرجام‌فرانسه
؛ شماتیک ترکیب پاریسن ژرمن برای دیدارمقابل لنس؛ساعت22:15 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27881" target="_blank">📅 21:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27880">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UIzTmhoBd0b5A0wXFAcDPPNiyVKNcLRVETcEUs206txZQdeQtE8ahNLJOUzW4Mpnyd4n68dExxA5_GpnTto3AZUhhRS3zFxa5kUvX5FUWhNF5EFRZRYV_iVofNrw5aSzogU_o8HyEROJmHBZFC7abzV_8-U89fpe3Cu8HBi844IL1x6CAx9PERJjHFIvUXHIIMpF95XX5DOGPQ2lUVJC-f7H9SgOTgx84ktIKGjui9yeVmzgT8IkiBfotjf_8DxCiRnEP0asN5DZ5tY9DR7SBM5Atft_pZzbLkjQp9nuTjMbVtupCQBSUX6tlCOfa7wd1XS2MqHeD6rjmdsp-Ert3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژائو کانسلو مدافع راست الهلال قراردادش رو با این باشگاه فسخ کرد و بزودی قرارداد سه ساله‌اش رو بعنوان بازیکن آزاد با بارسا امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27880" target="_blank">📅 20:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27879">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdri2pNIylh44bk5vsBr5mvYM3Rsb01KkZqwp6g4gSfDiQkZfx1U1ina8qrirl1f7XFCJLD_plXtkdh3AzWtcOZ6SnXxVUSWYx2cph61FL2n4xk1paayKqwFFnQZHwAJiGOgkk3SV-jFYb3o0puRrYnfBOQiM0PLXFP5ZBhr3tYRfCBB_rZwf_ucNlWb_RVDiGFZVDyX1Xn_BOnMIkD-evPlz6Ze6YM69a4tgKlKHDmFWtZWPJfOT0kLd5gLSy01MLojgBeKOut0_6xP1gbPufBOAthnJ0w53Jzi0IzITJNwSLdoaT-8lyxyafanthPOzgCEXmfRK3Q1HKUmENcHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27879" target="_blank">📅 20:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XY_Bdg7yIqhQp5OQau1PJHwUgKINPvRs4CPEHPCJ-DZ0KErZPN1cq6PhOgZGMUrsEhcXUIwO0uK8MmH6IyBZfB98jMygZLeM-7r0rfchDkvDXw5KyIb7ZF-83j8oTJX4_Rvf2qTDemKbye4AcBQZJv0qd_vyD3ZOpHSynyBky_eHFyDl7LMIsEZH2GY_pcpEM7fXz96pWYkEM1z4FLcwIwsE4HS9wPMlxf6VcqkT8RVus4axf7CgrBQ5W_4LAhaoqBsDw9ufVkMJV5_J708wTzfbGM4Ux9ZHPxN8pgVf5t7ERe_mTuCeq6SThrbbgOq6IE96Wj4058UZyOYNcKNbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5dO3MZ-caOTwE0SNqxTEhfJq6pVZmGT0A9xnQn6hFbNBavBF1EP1F-j_l_PPkqTeJhzDcVSyokFDoZt-Ov3nMS-uvEMpEZvwp-8yRQcD1LcVfd5_RH7H7AJTNNISpTXgxMtYNKX2aUOqYuIbGTEegq68h5MUe8iTozLjTQ5aOeJ-FY726X2StiEGjFDKSp_MqeNFKKl0Tx25TxZcAIr-qzqpa9uJu37x-eXy7sD0zkwvhggD81yXx-IFEUEQhJaISyVHVSWbK1s-KMQLEu-EEo1WNCOXSkTL1FFPmyqbnOXDA6SHiaNHVgI0QHXxLgzj83sGQS2NcOJQplyjA3hbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
دیدار های دوستانه پیش فصل|ترکیب دو تیم بارسا و رئال برای دیدار با بازل و شالکه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27877" target="_blank">📅 20:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27875">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBrTan1oWrnPa5dIteJe3gsHecX0rYn8PYQL1BfQiu9OCrxEnvaUn60w7ElF9FFDYCdFkwSebnNkkR26XLdiqwTkks-lh4yr78pBoqo_SAjqQhsf091QrXzYSj1kRHVSFNg5DC8tzKb9yje1RwYI980tnMBX7UVyrAOdjs9A_e3m1SiGYw-ROuYDvPKhdACVoYwSU7kOKdvj8Cv6AmGyJ1FuZXuDbluAmDFxi14yBGbBjuh1naCrO-XheDA7C38Zkx5f0UPcAn9-8lojTrXkjTjUmmc3PmtLWfi-t0Q207ydABdqxa6qLf1ELyhPkYbNxrV2zSNhRuUqBnYbzaxkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: هانسی‌فلیک‌به‌سران‌بارسا گفته اگه شرایط جذب خوالیان آلوارز فراهم نشد با لوئیز سوارز مهاجم 28 ساله اسپورتینگ قرارداد ببندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27875" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27874">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8iju5lCOxG-VwkBAf2VonUNp2feYYRZSUH0alZbC474IKMKgyXkFLXlX_uM-oao6xws02h45Gp-kzEmu8mENc86gTWqVx_0BcukULMe6wyUm7r4Ba1FC1QNPlmQqF8bmj9OyVStlcoVIgsBgZJOIcm5-T0gL1eS4DwJMWmK47yl8c0jzBhUw8vXL6g-2ScYJ-M4-DHLJvMpa-ySRnXXrIR3oJxjUhkx68vqTQa_oQteQnbEa50q9axbABXPBBCH5XbtaCmtWKYkx4OIQJOmxZ-b66_EkyrPSeER7NdqKdb2OuBNdjEX9KIVBQlrddT-6aPj4IYw0oZ2DpEjsU_Wug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ فرداپاسخ‌استعلام‌باشگاه‌سپاهان از فیفا برای کسری طاهری خواهد امد. در صورت مثبت بودن استعلام طلایی پوشان از خرید جدید خود رونمایی میکنند. قرارداد منعقد شده و طاهری بازیکن سپاهان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27874" target="_blank">📅 19:53 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27872">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASgWwixWGHSDNpNQPZ1Z7XbH3YicgZu2CopEEouUdY6cHmmsS40iuGS9eYE9WA_9P8BrzOLaxS1Ah5NMoMvk5x7SsCVvZFbQ0d2ANNvat1ERs6w5ivyAc8rVCE8tp-IauNU2QKpumeC45Ja21w3WM8ataYgYxQrPxXcbJN_OrD79EFlnaWByPzE7OilHYVLwmMyrQxmmJSX3bazpfaA_xvJ4oThoi664BR47gSjCOtgDU4jGM8Y8_Y2KUq0qtLshOrJZyrcEtCV1yQwfvPdwHZ63GS2wjgBdks2oyvvDkefNv0aEmLWH-rtuxOkix7lwqJjITAKom4UcmjUw2Jo6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27872" target="_blank">📅 19:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27871">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3YEbaK7LKk_khyVSD0pKfhk3iT_HBiwLwp7ry8ITgempbS5hv3InM08_mqye_TNNObRwzOk-RWJXzfXQd5FEbjEAl5ARCm9Y4qCb320-Jl4KuvLrUSdhDQ74nu5IJYAjSTobMlV4HdUjgy20Y2vUr_Alz7ISaSdz5uyFi2PpTDc3jxrSskVInrvsLqb81FGgJ0a7lM6d9LSWhqK_mp3UTFoj4O8sDzYcPiBI6m6UiCjMpsi76rxyq662mnFswBPBotVNXhzXfPIlCS4QD8AwLocOMlBJl17WGKFJS687XR_n-6ulEseY2cxbyid9hRqLZ9VxYLRIS706Ucd8LzwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپرکاپ انگلیس؛
قهرمانی ارزشمند توپچی ها پیش‌از شروع‌فصل با برتری قاطع مقتابل سیتیزن‌ها؛ آرتتا با بردن سوپرکاپ برای رقبا خط و نشون کشید.
🔴
آرسنال
3️⃣
-
0️⃣
منچسترسیتی
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27871" target="_blank">📅 19:29 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVu_BWLHS0mmJmpwWfm7qipVbhLeBYt_HOCP3TONFy6k3NCGfBMOogDRQhRdHlGU-fiv5JFebhg93xxhpkMPazjITDSbxJy0arPofk6fCB69BIozNktGnh4qwqRYToR5yJKlay12l8vZbyHKfVWStgPiLowdT5X2y-IpdUvsscsZDq9Rn8e9lxwd20uaNtfq44DcqwsLn4-eoYY3qNMC_CixNjkY233_U2Wmq3uzCL3_KcX7BzfhId4CVxrjK5PlEFpF7-U8Cx3NlvTdPAptgNBPgcVzTn_n198xsnf7wZAz-IlXxqxvYbMIehWykBUkBgcmwXFU-XF9EVzAndEIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه الوحده تا دوهفته پیش حاضر بود با 700 هزار دلار قربانی روبفروشه بعد تراکتور میخواست با 500 هزار تا بیاره که مخالفت کردند بعد پرسپولیس اومد گفت ماحاضریم 800 تابدیم یهو این گلی که زد و باشگاه پرسپولیس هم‌جدی‌خواستار جذبش سر این قیمت رواعلام کردند. قابل…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27870" target="_blank">📅 19:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeOEFo8UZGk6aZkSBCfCFvphnoJ6TuG56YHOZyZIgumBkAuzl3sv77nA91m918xD751FVE3p7JTGZTmAudl48PRIkNfD_nRdHtlNVEH9068YhzHa1tQIiLEGntko7yXFAEY-Sv7rb3nK8TDASUJ8QvguVkhdNJNuKuTZGdthLEdOR18gUTs8zin6WJC-AMjtaF2jXaKnnWKVl2NljAc1SqLZLRRI5sTTkRBeTsrYz9Nk1I343Sy3Gjl0GG1JohKLA1B-SSrlWkNLcissahgki7El6a3xXgYcscB7idMpcq5uvUgV1TwUDK_AaIVe4Ksz5RdiloDb9IfgRKrA14760g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#فکت
؛ باپیروزی 4 گله مقابل مس شهر بابک؛ تیم استقلال به تنها تیم لیگ‌برتری تبدیل شد که مقابل تمام تیم‌‌های حاضر در لیگ برتر به پیروزی رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27869" target="_blank">📅 18:49 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVQ90pFvyAnL4eSRNNQqaQziU0kPq6PELwUhCJkjyeLvP111CpVbvEPXkPHe0GzFbze03eSNvRSOnwcL5GmMqsfrkV3GR20elYB770Dn6v8aGo1VndXpMGbwIMtl4NSdQbJLin7bC_Vc6r7RVUm4lOCdXKtqPouL93m2Elx0cdlLLQndNfwrZ4243nPmUr-RlQr0EdLZdANDP53F-PDwfp8kFaapIRlmW-6-k0j4uFEKlEsRJGdGFmAsDbNhd8Dxq-3TehwAI8bjaXaphWS1yKtBi8NYiFdT-m2E70l9rQ94R1wvV2usBx5cJ0P5Ny3NbOgPsKQCfHJJ0-8Tyy1-1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شاگردان اسماعیل کارتال در هفته نخست سوپر لیگ ترکیه باوجود تموم ستاره‌های این تیم با نتیجه دو بر یک بازی رو به گنچلربیرلیغی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27868" target="_blank">📅 18:31 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6yoozcfMc_pv9GDrlqrql8ON_6rjvCVOplE9hz_taJA1-1y50mQAnSvei0Ntzkx4Tjftb0UJ1Mva9sKQ1s0jXe1jxpB6dne79UPrYTQk6Tjwq2AK4aL7-39u3ZqTr5jgGCwbNwXktvc33cix42EsMAO7Ug1TLHVA_cTOQp45IPwRDH8-Qb47yLDXMyYOAhPQ4gKSIuyUz9yfac9DLxd6jK4S67NcAHG5zb8oA6gevXiIUS17Ex4eIbDvfwVMrrhsgbcBEietxlTJJoSnwR9T4xkE46j_ywzQVl8CDVfkzVHWeri1bNkS4CjpfygQxAB5l05obv95GMcOewuUXQQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فوری
؛ کریستیانو رونالدو اسطوره تاریخ فوتبال:
احتمالا این‌آخرین‌سال‌حضورم درفوتبال باشه و میخوام یه‌میراث فوق‌العاده از خودم به جا بذارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27867" target="_blank">📅 18:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFKwpxt3dGJ69Vp885yi26Zbl5s6XHr6hW_cpRZeA9OSrkSqOQIPiiAWhjZe7TF1jxhr-EwbOURes7jAlgPdTzEFN0gqw2MSvVNyVpfHo4lJl1DnOaHvvzIzY93lPASzhNrGm-DVQutFKvX4BkkOTsoUFrkcIpocke2NqeaWMtVet5fPNuu9RjjaL_vuWQDqbpxLa7zNfHu7JTHCKxk9uLWNcSIJx0YKt-JCv4hVVmEKqGNpeCid6AmOcVYAIWAl9L5P-gZy9v048ZRL1mVmSBsWAd-CbRwLQGki0Ao1QH0Fm68Ire8LtLoFML1e2H2BHRnSqzbswMOlKuWgR8bnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسامی داوران هفته دوم لیگ‌برتر
؛ بیژن حیدری داور دیدار آبی‌ها شد، حس اکرمی هم داور سرخ ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27866" target="_blank">📅 17:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7cDoQ_ng-Un5fDCVK39nuFVmL-9y6ka-SM9aXBigGbOIR_KRdvY-PBq4vnIwoBZtZrSbFLt0mngK2-kRar7i2GRCsNgSlymJ5231lO9vx0Qfqv5LbvQlUaDVt-XXQqc_6Ye8lmgPb8xaWITWJ3T8AvGkOS6vlocbuoeLT0IXDqS-AafVSyexAzxeWXKMeXBlaOcbopUY1Znc8UsyTwtU3H0eRcomKtY-BbXFZXYP2tYjtwC-o1-hgv4whpitKRjGaRhYB-porlY4rYFevY2gvGJ8NxpL8HyPFcnfu57yDe4UOqgCQ05-JFelVjKP6gFvA0ykVUVM6PYpZBgWMOubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27865" target="_blank">📅 17:35 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27863">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxPRzUrFAmOm_xfqz0Uf5UKVV4Dlohvwoqox1xUhzQy8RfV0a2r-R4d0VP9oRf5Xdh9VQKVlOXytpe_0uKS8C4hnOkbuL1ohTxX00gv1X8KRJTAVIRRXrJAwTzAjcuFKdDtxiuPt1AsESC8asRSxtUgwivUMplXZARsAastcuJ92JIvOUNUbSYXmu0HpwJPxldzOExuvxgzPTRqLWu9aVem2lSONXwGPbjyuz7EOnkfQ3pekFGjnlb9KQta1QlEhBd8u7hxQua5x4f06NBMPlVf6Br3hGXrfhjpRMuZVLJOkIy90EhGVLkn0V0MifJSmRMwzwwzPnfQCTvDhhyq-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSYMFoYSwvmRckOBLh1jJi6x13rIh4EHl6qK7U6DxFEvgzLQaThzie3oEg5fPYNDZBnnsr69oWuM8sK_oK2d7DaPvXdFsHrS-tXwmDIparNKEwFCDE3C6rfoxwfhaXQKr6llZa6zqP-TL6r099fo6wVXoza6GRUGw659ewAk4OWkSjrDgMniCnXRb5hUMN8HFwvGYYy56FDO4FZHiDqx1Jzzs9A1RpoMmRirhsMogrLVjoe-SZm6CB0-2wRpoIQMDe9DaWoRwmCsHN7Dm9pzQrad543uf4d5ZsjBuQVpBwUixw6NljkrPn583R1-y0RS2OOshVC0jYv-Qo0PAYEIFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
دیدار های دوستانه پیش فصل
|ترکیب دو تیم بارسا و رئال برای دیدار با بازل و شالکه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27863" target="_blank">📅 17:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27862">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HD7ABx02vGSWiDadPVj-GqOTIxZsKcEC9QE9xYl_90GmST65d4JHcHGbo0WI-VgZu9FbOOb1rqnY4bE6aYter7aUx40G5NCrjLPAXxUS6XqoAe-R_5VxvWiKiKGtNvbJ1MmtQoKyyzuvsOgiV2t-_2daBbIVALiAQLBsNwOMARORZu9-J5J0MRI8ClrGm47huEjwDFiPPnWxQI5K3rdPRHMDzMFyl0V_taXyh9GTKUAPACCHjYvv3ZmEpDin8zaEF982HwJf0HhxChgeF8WWpaJduKYogjpESkxSQ90Lt0X2qefwdoPc8wCOEDqgVMhmFuSPmhTe4KHf4eqXa-16mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده امارات دقایقی قبل به درخواست باشگاه پرسپولیس پاسخ داد و اعلام کرد برای فروش محمد قربانی رقم 1.2 میلیون دلار تعیین کرده‌اند و حاضرند با این رقم این ستاره 25 ساله رو به باشگاه پرسپولیس بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27862" target="_blank">📅 17:13 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfNqAMVfzAZiS9AjzGnDZk_pskYnLRlI6ortdr71S-_XQ5Ys6ZZvUsMIBJrZEzIYIIYOUztN_ZvxHvaF1EkdxtRoaGXx6R1ShXLXEm7jJTjfJoz5ajpP7Mba3h11i2BRoXz0iK1LveSScb1YOWc0m71ebnskiMRStdzE0ZxniRleFCeo2WABWTdiYJSXqzD5Mo28hoULxFbyjRG7Cur5YlaZxQ13iKj8G-IWA-eUj9mO2WMLBAHK53VmNa9n2C0q9nY1fo_WgDe5Hr9aR5K1lWxXLaxWxCjl52NwDMM0ypDJGajTskwmuKQ8lEoxKGgD1OQjDlA_txYelTiVE72PKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛مدیریت تیم پرسپولیس دقایقی قبل بار ارسال ایمیلی به باشگاه الوحده امارات خواستار جذب قطعی قربانی شد و ازاماراتی ها خواستاراعلام‌رقم رضایت‌نامه قربانی شدند. ایجنت قربانی مدعیه با رقمی بین 800 هزار دلار الی یک میلیون دلار میشود قربانی…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27861" target="_blank">📅 16:54 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
تمامی گل های هفته اول لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27860" target="_blank">📅 16:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzPofncxhB3wT-kBpfbdfCErZp8iDZ1-MELtHEon_wo3Wo64KxHe_9P92eR_mmsYEP_NP68QSnjpJWD6k-6VMH6dznkTUTW7g2fQfje4yu_CNjeIPKBun410tWU7c8H0SEwUIOw_4eNmbRG9QTye7cUbo2wjJBSHD9VBA3DSu9AZGFp8t7tRvvp4VLvXYi1pUxqj1TdUAKPsq7NBTb0_k_vtKfBZnPXGudTPSM9JxsrxuNwCQ48YOkksNNPXUaMTlG2VXPq5gdAt_P-wfsc0z_wHdJpTrylSsLk_tWx9-dnNkiHWkPVcqwqmW6zMs4vxiaG9XChq4leLU5o8DqM-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری داکنر نازون مهاجم31 ساله استقلال بعد از پیروزی آبی‌ها در گام نخست؛ همانطور پیش‌تر هم گفتیم نازون به زودی به جمع آبی پوشان برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27859" target="_blank">📅 16:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27857">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34645ec54f.mp4?token=Ipg5GqQ0MAXp41vDvse1GP3WQYwFwCtbriXI95K4-rdsRuVXDgS2GSA0pA0SPq8VxqxzFPholv8DSa550VDXug9zLy_4gJazZZn430ETqqv7A0lGt6QmA2fCqHtwELh-P65Ckv4Cvf2dJMUmIKOwPGzz-5Ujn7ykHWI8mhuDwWyUvHINj03UzBV5R6KgashpHV6Iqjy7rNetaEzkXVNyXbjDbmhRmCL6kWyx-Zx55oNJ1Fq7x1FI49W5dXYYBqwmgaFeJbcagQ47uQps2qgdXC2DpghaKwiaMU6kgByQTs_Cp5_pEr9PCakrG_5pja3QOypXhCNL5uoNK9V1xCzlpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34645ec54f.mp4?token=Ipg5GqQ0MAXp41vDvse1GP3WQYwFwCtbriXI95K4-rdsRuVXDgS2GSA0pA0SPq8VxqxzFPholv8DSa550VDXug9zLy_4gJazZZn430ETqqv7A0lGt6QmA2fCqHtwELh-P65Ckv4Cvf2dJMUmIKOwPGzz-5Ujn7ykHWI8mhuDwWyUvHINj03UzBV5R6KgashpHV6Iqjy7rNetaEzkXVNyXbjDbmhRmCL6kWyx-Zx55oNJ1Fq7x1FI49W5dXYYBqwmgaFeJbcagQ47uQps2qgdXC2DpghaKwiaMU6kgByQTs_Cp5_pEr9PCakrG_5pja3QOypXhCNL5uoNK9V1xCzlpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیدر معروف باشگاه پرسپولیس شب گذشته تو قزوین خواست به سبک هواداران تیم ملی نروژ تیم رو تشویق کنه که این سم خالص رو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27857" target="_blank">📅 16:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27856">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NgS9x0_xheBMdo-ZuAQTXN2bw060SP9-X6mk15qVpcW0vDh5_cS0J7X0h2Bm0hJtls1TYUSIKHhJMPgOmbEvpGWadJcjrv_TLH-mFH_TldeC-i7ynlFEySxi6VJhSz9OtcKVdxbZ17kBckvwcL68elPm9-_I3KM3qPDgtSUcKICS_xIhJj7ZLLQlaJo3KOmVEwkSBMK1QdB-1W_kPChIrwKFY3-bE3AKemiWnfH6VWmu2dqLvqxhZjQXdstJPbyMWBFA9BKa30oRpzrgqzUbJWKB4Womp4tmh0bQlr5_8gwlP8qHIdyitdvZYLxlVdh2HX6DxHOhx6MnZ7cqUSmj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
سال1998 زیدان مشتری رستوران ایتالیایی رابرت بود. ‏زیزو اونقدرعاشق‌آشپزیش بودکه اونو به تیم‌فرانسه اورد و سالها برای تیم ملی فرانسه آشپزی می‌کرد. جام جهانی 1998، یورو 2000، جام جهانی 2002، یورو 2004؛ ‏حالاکه زیدان سرمربی تیم ملی فرانسه شده رابرت رو دوباره برای آشپزی فراخونده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27856" target="_blank">📅 15:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27854">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvfsyHrJrMqvhNpQXNNDZhShlyAiDRtp_qajHH44EQptCGRuZndjEF-REXUn6zm_WeG4BiOFcDPtglEqxJVuxmyNBfwVuN6MS-kBVrNEc2M78ZrKBI22_fppGeOoxqUqa3jFAhGHP5UE5YTq4k33q0DCm9jKvrqFlyXAWmHVvGu4do9qYN1JioI-txX_HOpf4bDyW59MNHLYJ1s-rs-GMF15Kt36a6GOJCOfwvGsja8qqcgr_M5MTfkt5x4xFnuBEpcVuO_PiXCnVGOGsZ0-yWCkm2zPxmbtVGui-vpFwW93o0lPbT5KiP51oEugt0rfSY8RnSAJR6E58u3DfL22xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3nT6lPsXm9Gz4-SANsXFp3PIKEN0AalUclB5FGLm4SBWp_BKl5DM-COxHwBGCK4-JnbutO3jfqah1mtWtmofMm-i-s591HNHxJPKPy4tnllUxo2nvOJ2UsriI7okPxbp4RX62dqVKJO-6FAhGg4QCdJP6cLjfAjJ5M1-CHkeWX5EWLVcE7UaMPEenRWoQ4YWnm3HIfB82M298Xho0CKOUtlbM9Y5ekX9k6gs0T5e_AZ8braG1_mOSblqGGqoiptJ6APaUpP0ejWcYbn_PJWwJUy7z8BzoZzaqdt41XqvtEHwETRXqZ43ryNCCK2VFVKIq4beEgTWeHTnsRmlHdtUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
توی بازی دوستانه بایرن جمال موسیالا از شدت‌گرما ازهوش‌رفت و پخش‌زمین شد. حالا استایلی که اولیسه زده بود توی بازیی ای که جمال موسیالا از شدت گرما از هوش رفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27854" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
