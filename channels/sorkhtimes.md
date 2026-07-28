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
<img src="https://cdn4.telesco.pe/file/gdnT9a2Km1EtncIAXjVOnE6Lc0Ze9DqLecu7qYnCJq-PKi2RzFoEVunvyIwdly1cOkQRqutN85nT5l-ZCFs3Z1yLK5iCkwvdiMBCLdsphUX8fPx-f2ORJxMUuogRZ5icsqPUqCGO-VpzbcjhYQgugMFup_SoEQLz5XPfEjp4m8vdUR6ToyDoYD19W26lZH_sAwQknm3DiKNF2GVmocG2hqjG0wOGpQQFK84RDI-QXtjMwgIvlrIM8CfeILo4qF4ok_cGiuNCisxnhjkVc-3nnwMrMMmtJOIdU84VaSl7eZJS2wjlxUBanT4LgyWljta08O9vOHQRliKp-JALWb1l0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-136907">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBTs29QpglaegitKvLCo2pDoz_t9Om_7HpL2fLCfntpfdSy97-MQvdZ41hXnds8UC2PW1G7KyLXtOCVTWfovOrfIYXHncEIcClk6lLklduBHgu8fl4EmaSLf61dAFY5z2htq1A5zp0o4T4wIorpEEyXC5UicbKUTmkty-m_WrNwpcW6tBtqUFqd53JaIeT-gV0BNtUTx4dj9L3XDD20W0mf572gioRNLpjOiGBDZHdkh5zPmcsiYPTBN_paqGYdzZCYIFndWOoN0HLnMyARpJo6dFzy9ewlVWIRZnFwTgpBevHgJRnf4KZk3ev002UxEG7okNtUXZFl4ep-jTs1V7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➕
دسترسی سریع و مستقیم به اسپورت‌نود
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
-
مزیت روش ورود از طریق ربات:
👇
• ورود مستقیم به سایت
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/SorkhTimes/136907" target="_blank">📅 13:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136906">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQ9LAgBydbrAtcTSsvNVLPbRx27qeeU98143jFfomfLSgC0mfJdPR6CTCHUxv63XuIUPzXDO8lykUY3FM58wuw0lZtAh5axeppTbVbEAiRnJvlkLBgyYjHjyxf7-nkKf8l48P_s8NdzEUlRcAi_Rh6hv7b0Z_-SHHzNPEenGMPXVReDabmj0ld9vWBsVf766Fsuyt6re9q_jT3tC6T8GfjvqRVDf_yGeHrZE3SGfG0PYp5w683zs29Yben0YrFwODWCmgMxcQlkU-hpaINgBrQ4lQEyBnxLf_cEO_D0ZpgnoNBM_mi9_1BI6jPAKP4fN38kEwpzeLCDHXOpJm1yhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
زین الدین زیدان  رسما سرمربی تیم ملی فرانسه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/136906" target="_blank">📅 13:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVeZsfL0d8KW0D-t6i_GnFoJbfsqzEkrTk0x_bMpK8I0mBrfQtj00s-KmIY8U2iz2187-1QT9vVvIwTDqF-Mnb88vVYglaFDhDwCaDBmxKMuh_odxWgIC8uc4Zix420Ytm2GOJFy3SBir34ReXauKKSp9XDmA4VXbDWKZW3WofTfAfjEh-7YKhdUzUU1wbndWLT_n_bK7I-3csPwN7TVRJXFTTfVhJEG3TtGP_C4OAnx-nIyDlUX0BF1QXB-iVIF0-LaIbuDDNxDLTZOp7aW3CVzjBA-DI9x589yBNGHvXbNyMUFq6GG6UOEeHMpcoF9XRbTOab-Hk0WKDwRucu8qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🤩
باکیچ؛ مهره محبوب تارتار، خاطرات ربیع‌خواه برای سرخپوشان تکرار خواهد شد؟!
➕
مارکو باکیچ در تمرینات اخیر تیم پرسپولیس عملکرد موثری را به همراه داشته و تبدیل به یکی از مهره های دوست داشتنی مهدی تارتار شده
➕
در زمان برانکو نیز محسن ربیع‌خواه مهره محبوب این مربی بود حالا بنظر میرسد بار دیگر قرار است این خاطره برای پرسپولیسیها تکرار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/136905" target="_blank">📅 13:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/136904" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136902">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
معامله گری که سرباز شده و برای دفاع چپ فقط ی جلالی و داریم و خلاص که اونم مصدوم شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/136902" target="_blank">📅 12:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136901">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/136901" target="_blank">📅 11:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136900">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/136900" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136899">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/136899" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136898">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/136898" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136897">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/136897" target="_blank">📅 10:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136896">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG0zo9U-6fOALuMCibCLUN_ePRG2qXZrBXz9YBiQMWCfSmG4_Xla0sSAU-DcD05l3SctIRYukZeUL4XXRgaHSyToyG4lw28dGmQPx9DwX4NrpXUXP11oRhNGVX5N5xtHmV-KCnbFcyCLfTu3S9g_NAocsos4apQrYgQivbBSiydq-hQmyecrJt4oPr16gepeRU7_F3t492E0ULgPS8qysMaz1w4o0zdjE_QNzu_uOvIOGTbmIEPCnlrSf99fpe-a0L0r6Et-EqV2VrLniZNuG-qyDZ4pynkToDA8HzcTbpKTGeXecFmGQ1KOyZ-O_ILYyIQIjeyOHeHv3X6qFCqV6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی
؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136896" target="_blank">📅 10:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136895">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o41Dehhp9b_NEHM03-1J-DOsPj-SWRs9WzE92Y7WvMIL48iD1AR23TWXq62zieQefQ9lYXwN2Fnr-3ptOkAVrrnLx4oPStqYS1KeiojcVlE61boMxRoXZILfO7fJdKOKePT2aIj0B6SIi2z5Dtj7C4hvaRDqoSDyMTxMW0dLRvYLO0bqaVQyzdZAeOpapXEl_A41KD8cEAHz81rMVsQ8u67fAKFS2JPDE7LTImso3U2etnyTccato0xMg_pGPk7BJ7iETPatF7fC1V50fDVVUepJLwyzXi0a0JXx1lFTURsRnUzJjP0k34ihLl4C52gxQ0B0OhLp5tHqNAxC3hCOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پرسپولیس و الاتحاد کلبا به توافق رسیدند و محمدمهدی محبی بزودی با قراردادی ۳ ساله پرسپولیسی می‌شود
/تسنیم
🤝
🤝
🤝
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/136895" target="_blank">📅 10:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136894">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IhLSZx93SYJIvJKCmAMs0vjaeDzOHBHQdyzwyzdfHy2YnkQwv1qPAeKh0g8ErvC3ZiJCq3wF4iL_durtuATTLEc3s_jv_A1MwWllC6ufRYlSJu0bptablKqnk9hKUxB0iWRbjBeTF6rG9jj867Os-uUSlbXknZhBxUS2bV99h2ZGnYlT8PcA1baU_qqoke7GYBILOYhAmSTCIRzTISO7UZZjMHp0TorOxTir2cCzv8iXstYwWeLAkOfB2lK3Prj6Q2WntTa7Nx5TTvmKCrLIsoIPy3dijNk9O6IGS3sIM5qPe1arWc85Q1JQ2VeJ5egEh_8vfiFOKdB3LCpGyd4H8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💢
💢
مذاکرات پرسپولیس با احمد گوهری آغاز شده در صورت توافق احتمالا تا پایان هفته این بازیکن راهی ترکیه خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/136894" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RirSKy5n6f7NreQNrHnDkAxFdEXnFWB8fkiiOMdKt5vbQK_WrWs6JcfqfhtMAcw4XI2oCZ9_6kwYJpyq1pkPIpqju-_rLyjkqkubFdwxRv72CKhUCdxLo5ZhyZT2h-dOV6SKVlmzmcFZr2Shn79Jp7XpmzXuS3VEKS85Wki0LPOTTwZn8LAMFv2L6T0eP0irEuMxX_GPD84eLAKUbwcvEjTYtAuN5f6BXicRk2ClxGejymEe6KcpFFKE-6_1VoWyFzq-3YtSJZEeGcmqLFqvlInYYbfDzOdfV3jNJwVTfX1v8moCsuzKDJ2X9bSYB2TL0z1HHh0NF9XbTnKba9BJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووری؛ طبق شنیده ها استعلام باشگاه از وکیل خارجی برای جذب کسری طاهری و دانیال ایری امروز میرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/136893" target="_blank">📅 10:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
🔴
علیرضا بیرانوند در پایان شهریور 1405 یعنی حدود 2 ماه دیگر سرباز است و دیگر مجوز بازی در لیگ برتر را ندارد؛ مگر اینکه راهی یک تیم نظامی شود.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/136892" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136891">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
فوری | انتقال ایری و طاهری منتفی شد
🚨
طبق گزارش تسنیم، انتقال دانیال ایری و کسری طاهری به پرسپولیس منتفی شده و این دو بازیکن فصل آینده به جمع سرخ‌پوشان اضافه نخواهند شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/136891" target="_blank">📅 09:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136890">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/136890" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
یعقوب کافو هم به تمرینات برگشت
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/136889" target="_blank">📅 09:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⁉️
⁉️
فردا شش‌ مرداد حوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/136888" target="_blank">📅 09:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔄
⚪️
🔄
#فووووری
🔴
باشگاه استعلام گرفته و فرهان جعفری تا دی ماه قطعا سرباز هست و نیم فصل قابل دسترس میشه / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/136887" target="_blank">📅 09:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBmY5ix3ViReVhMbRkBCV-e5KLQaEPIv1ExxIKgcP-DX_A41b_zjWx8zP74lNPQN2eFJOmGRss8GwbrumBDZj7dOB9JY-1NBDM9UtKSMwq1nW1dBbOpyF3--aQR3otFv06Yp4peDz_qs9bGrRm-rOPhYwZPYj61gNx2YngM6ulqrGxenKx72nk7W5Zd4Nqqh5GY4v14kDo6_Cr5V-K3sutQbr5Up_Qo5ziLtPTxfKxW_eqLT_CoV_KYL71q5ERQz3v5Q-VbNM0xPSouf2a6-N3HFjDEAE_-lerAwr8Ou5659nP58rrnod2SgO3qY_twh5C_njqHSjCJp4p0n0oa8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/136886" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHHyjWxaxQLimjlyNId9Lh7cvfOYe6naHO3g1mkeh-e3I_NVn2-VqseephsDe-b_kEUc3E6h9Utfoqrc8wWKcdDzzHxn75MUJgbdST1mMS879QjezaAxa34uvrrFuLvtY3fNmf9FIeg1JDLyIFnrSsxxwKvoMFAruvbcqKEPI9UEQxXNoBKTKhVuW1RWZT0sRxHCdESnBLXyUbByqN02kO_EkdrAm6FvbqnGNpbFBJ5M9GElkp-vbHNdj28bTdilE-72TtuQ0Zdtc94y_rMKQ5xVXj6ANiZQpzlTobJuP1eve-ndpPK-Npc3cNbCwylzOL2MVYgknKuxtm132nLH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
⚡️
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/136885" target="_blank">📅 01:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/136884" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136883" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔄
لطیفی‌فر فردا به ترکیه میره تا به اردوی پرسپولیس اضافه بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/136882" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136881" target="_blank">📅 00:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔄
🔄
تیوی بیفوما در پرسپولیس ماندنی شد؟!
🔴
🔴
مهدی تارتار اخیرا در تمرینات پرسپولیس از عملکرد بیفوما رضایت داشت و به مدیران این تیم نیز عملکرد بیفوما را گزارش داده بود.  با توجه به عملکرد بیفوما در دیدار روز گذشته سرخپوشان برابر پیرامیدز مصر بعید نیست که این بازیکن…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136880" target="_blank">📅 00:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df2772DZc0R0bJOTFpnqjJSpF0zSCaRWbOCWhHg0ITd6aZ45UlPqohYFJnLd4sqmYDSoIxqVa6KwFcrLHPEUwBLGqnxTSY2T4MHxPgyiWbLmCtQrPhsVUaNRiQSr9OayZDCz_Dqk6jW-7vUxrkRu1-SzJk924dzuq3h9j4qEn5drGV3kTmMIK3bQ-4ryJRlkTye1R2rTFOhBnLaNa0eNouQFfI-dwFmRGXRtaG-53nqPKRbbWS76l6_2XvNazy8-s1zskhlko2GafEmx_AcC4ppDW3B_a1WJMXUWWWmAVNim2GUFKqrWpp-NSVsDasv0r-TEXqIX0Zi2Uzg_mhapUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گویا رامین رضاییان به خواسته 200 میلیارد برای
هر فصل خودش رسید و در استقلال موندنی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136879" target="_blank">📅 00:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚠️
⚠️
قدوسی و حقیری: مدیران باشگاه دارن فشار میارن که گرا بمونه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136878" target="_blank">📅 00:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
قرعه‌کشی لیگ برتر ایران فردا انجام خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136877" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZJ1Qn3XCM_-gJHSU0m2OeDcZ-jZE4qnZUuZ4TaogmV6vySfK963JmN7pXTxDg6C2XQqbfVOOn-B4bnK73cOWp2zrvmqQ8ZWR74ut91K7DhGp7Z9jxlFxFWlfAMJo6vxm3qoyCLHUnux1JvKbwihmlqp7CeSmunl6D8c2YRiVWODLIbBYnQOrVS__MGmonOg1ewwfpU9qxW-gzm6mUc9UrP5B2f4npCSOAU4ZuKBy-aayO9icmhwb44IJBeDwgYuYxk7BGGqttCEGrBXCyJ3C78XrFhD4_f9pKEvBl420fX3K6y7Viqd0_YBpFV1loors0tTsOy7wRH7zZVY5on4OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136876" target="_blank">📅 23:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند  #ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136875" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136874" target="_blank">📅 23:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwg6RX_4SFXdPuIZZOEP_FfTo4Bpc52k-Hc4Zp9rAyIiR9fci8hjFHbayF0W5zzUZbjMGXTKvR5FUPATopbQ-BMBBDKJX7qTcVU09oFpzw01P_5UC6PA4Ej0o_HOchJ1T2iUsI3OPO-j_BRKneQ30a30sjbBPoBgYINhvdzIVYfLc01nagnOMf5ekuLtvromdwPUTLSbVau2rmpQr5j3CL7nhEv-uKtNzeqoEtOLTjUq1JrPLAKoa8MIjC-O6g3yzZ7D92keKDEyWpIrZCNokaKW7IvU3bGhcCFytmXI0DWW-II_LhD-nAC4FQKinrPhZ_1rMGvbRPfZ5ymcteBBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استوری حسین قهار خبرنگار حوزه پرسپولیس در مورد ایری و طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136873" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
گرا در بازی دوستانه غایب بوده و احتمالاً با نظر تارتار جدا میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/136872" target="_blank">📅 23:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-A6nfZgQBz2oPpEw8WnJXRHO1QIwNYxy_jNUc8sPVLXNOiKOp4Cz7LUICPJxaHXN4Suqiy0RKKjlq0t3fVfji24i_JBurbil2ILW0sfYBzIwdHgEgJIgAdz_bRw-1a8G3jAGadaYL0eD-U4N7mVEldWCKKxoFjNS8PvemfqoPVB18HViBNXB2pz9OXhcom9IE3STYdqWkCfIX2Bi2dpfagygDX33lg5Qz3jkHOl7HZ8u2e7wrXLD_iuuKJdW7BB8iKlIGSkGQe2z8yE7EqQ3SDD0KYIDN3Ai-AN3X8slaFu6lh1dDUtxkxbfcxay8Xig4k5v_VKGqfEpO6i9VK0-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌀
🌀
باگناما از گل گهر جدا شد، نیاد پرسپولیس صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136871" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=Ih3bRvDcikk976W2BLijM_F9ib7QlQ9BSl_v87I5HX3-k8vIvbmtIE5F9FVA4-k49VwIDehbEuhGWud9BgHt40qPJi6ea4lHn6GCtiydI1pqcw-vWOhoStwRoQdtmIjHgbbE9GMUfZ4H3NTvBw3rIDPlMmrKEOEpD6SSDW-ElAYHFJJx7fEu5zJWn_Ai2N8BnxenBtyyc4oJmTaq409BbVSqhNITu1_EPnEe1fBjJtX3-gYActge5ph0TW_dpgjkWavRSV1xshgNxvcxkxwICNxSw5vzvzUKtkov-gYZ7Rt6MNKdGFVf3ypWGNjrhIaHkZ4YWuIGcFExKgOxlQgiqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=Ih3bRvDcikk976W2BLijM_F9ib7QlQ9BSl_v87I5HX3-k8vIvbmtIE5F9FVA4-k49VwIDehbEuhGWud9BgHt40qPJi6ea4lHn6GCtiydI1pqcw-vWOhoStwRoQdtmIjHgbbE9GMUfZ4H3NTvBw3rIDPlMmrKEOEpD6SSDW-ElAYHFJJx7fEu5zJWn_Ai2N8BnxenBtyyc4oJmTaq409BbVSqhNITu1_EPnEe1fBjJtX3-gYActge5ph0TW_dpgjkWavRSV1xshgNxvcxkxwICNxSw5vzvzUKtkov-gYZ7Rt6MNKdGFVf3ypWGNjrhIaHkZ4YWuIGcFExKgOxlQgiqIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند
#ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/136870" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚠️
⚠️
باشگاه برای بازگشت امیررضا رفیعی امروز مذاکراتی داشته….!
🌀
چرا مازاد شد که الان…
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/136869" target="_blank">📅 23:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136868" target="_blank">📅 23:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahrooooookh Abbasi</strong></div>
<div class="tg-text">منطقیه این عدله و تفصیرتون کاملا
👍
ک پرسپولیس تو پست محمدقربانی الان بازیکن نیاز نداره،چون باکیچ،مملی و دوتا پوریا هامون ک تازه از گل گهر گرفتیم کافی هستن و بلاخره یجاهایی هم مربی این حقو داره ک با اون بازیکن هایی ک خودش میشناسه و خریده بازی کنه چون اینجور بازیکن هایی ک مورد علاقه سرمربي هستن و با نظر وتاکید خودش جذب میشن بخاطر اون رابطه ایی ک بینشونه یجورایی برای اون سرمربی جون میدن و تو زمین براش کم نمیزارن...ولی الان ک قربانی با این تفاصیل جذب نشد اینو هم باید بگیم ک تو پست ۱۰و پشت سر مهاجم حتما یکی مثل محبی،ترابی،هاشم نژادو...باید از نون شب واجب تر و جذب شه</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136867" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
🔴
روزنامه گل چاپ فردا:
😀
مهدی طارمی بین لیگ برزیل یا پرسپولیس به زودی تصمیم گیری میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136866" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
‼️
شماره 8 مرتضی پورعلی گنجی رسماً به مهدی تیکدری رسید تا جدایی مدافع میانی قرمزها قطعی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/136865" target="_blank">📅 23:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
فارس: تارتار از عملکرد گرا و بیفوما تو تمرینات تیم راضیه و احتمالا این دو بازیکن فصل آینده تو پرسپولیس بمونن. ( شما بخون نتونستن یا اجازه ندادن این دوتا برن..)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136864" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
🏅
آقای هوادار ۸۰ درصد نفراتی که تو لیست اول تارتار بودن جذب شدن و تمام نفراتی که از گل گهر میخاست، لطفا از الان بهونه دست کادرفنی ندید، آقای تارتار طاهری رو نمیخاست و گفته بود حد المکان ایری رو جذب کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136863" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#شفاف_سازی
⛔️
در خصوص محمد قربانی خیلی هوادارا میگن بخاطر اینکه تراکتور تقویت نشه ما باید جذبش میکردیم، اما بودن خدابنده لو،باکیچ،پورعلی و لطیفی فر به هیچ وجه قابل توجیه نیست جذب قربانی
🔴
البته باشگاه قبل از جذب پورعلی و لطیفی فر برای محمد قربانی نامه زده بود اما همون ابتدا کنسل شد، یکی از عللش این بود که ایجنتش منصور عظیمیه دست راست زنوزی و اجازه این انتقال رو نداد،قربانی از دو باشگاه دیگه ایرانی هم پیشنهاد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136862" target="_blank">📅 22:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
اعلام ساعت قرعه‌کشی لیگ برتر
🔴
🔴
مراسم قرعه کشی لیگ برتر جام خلیج فارس فصل ۱۴۰۵-۱۴۰۶ ساعت ۱۶ روز سه شنبه ۶ مرداد در سالن همایش های بین المللی هتل المپیک تهران و با حضور مدیران فدراسیون فوتبال، سازمان لیگ و نمایندگان ۱۸ باشگاه حاضر در این رقابت ها و اهالی…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/136861" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein</strong></div>
<div class="tg-text">این نکته رو بگیم ک درویش با همین مدیر فاسد سر فخریان عجب دزدی کردن غیر عادل هیچ کسی حرف نزد</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/136860" target="_blank">📅 22:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
📌
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام عضو هئیت مدیره باشگاه پرسپولیس
⭕
باشگاه پرسپولیس برای جذب دانیال ایری و کسری طاهری به صورت رسمی از سازمان لیگ و فیفا استعلام گرفته تا در صورت نبود هرگونه مانع قانونی، قرارداد این دو بازیکن را نهایی…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136859" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/136858" target="_blank">📅 22:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
فدراسیون فوتبال و شخص مهدی تاج به دنبال تمدید قرارداد بلندمدت با امیر قلعه‌نویی هستند! هیات رییسه با این تصمیم مخالف است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136856" target="_blank">📅 22:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🤩
#تایمز_توئیت
❌
هر روز برای من مطالبی تحت عنوان افشاگری از مدیران باشگاه میفرستن که بیشتر شبیه فیلمنامه هاست
⁉️
وقتی هر روز یه روایت جدید از نقل‌وانتقالات میاد، آدم نمی‌دونه مدیرعامل کیه، سرمربی کیه، دلال کیه، خبرنگار کیه، منبع آگاه کیه!
❌
یه عده میگن فلانی توافق کرده، یه عده میگن نه، یکی میگه پول نیست، اون یکی میگه پول هست ولی نمی‌دن، یکی میگه لج کرده، یکی میگه اصلاً از اول قرار نبوده!
❌
باشگاه رو انگار گروهی دارن با ریموت کنترل می‌کنن؛ هر دکمه دست یکیه، فقط دکمه «اعلام خبر قطعی» خراب شده!
❌
خلاصه تا وقتی هیچ سند و خبر رسمی‌ای منتشر نشده، این مدل روایت‌ها بیشتر شبیه فیلمنامه‌ست تا خبر. ولی خب برای جذب فالور و دعوا راه انداختن، ظاهراً از هر نقل‌وانتقالی جذاب‌تره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136853" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">➕
بعد پنج سال به این نتیجه رسیدم حداقل نصف هوادار هامون متعصب،ناآگاه،هیجانی،و تو دنیای موازی هستن و اغلب دنبال کری خوندن و دلقک بازی
➕
هیچ فهم و درکی از فوتبال حرفه ای ندارن و چشم گوششون به دهن چهارتا از خدا بی خبر بچه ساله که گوشی گرفتن دستشون میگن لنگش کنید، هوادار واقعی پرسپولیس رو سکوعه که لب دهن نیستن اونی که تو گرما و سرما از تیمش حمایت میکنه و بالا پایین این تیمو دیده و به مسائل اشراف کامل داره، یه عده فقط لب دهن مجازی هستن و ساخته شدن تو زمین رقبا بازی کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136851" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🫦
کونده رفته به ایجنت ایری و طاهری گفته به بازیکن هاتون بگید استوری بزارن… شما که پول نداشتید گوه خوردید این دوتا رو خریدید به امید اینکه این وسط یه پولی گیرتون بیاد ولی فعلا کیر خر دستتون داده بانک شهر… به قران خود بازیکن ها هم ذی نفع بودن وگرنه هیچ کصخولی…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136850" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136848" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/136847" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136846" target="_blank">📅 21:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQqwpbUe8kaPKfxx0vyogBHtnfN7dJq7q9f9jdFNNFaZ66HXATb0nXqIY5f9wvcGz4yqhP3hdotDDWq5EeT2OS-aoNEWiVLB9q4Si1hQ1QqLC5aRwfStT8N7FLSfzb7zZ0V4lSl9js5kjEKxCJ8S56tD9eQS5H0z6ZprvODGP2c_UxYRNO8U0PvtErB4uS66WZpTWo6GW99KJmtfRk5q1XAvdZCaj6GM9lvC7D012-KSw67TvGF6NeBvegPgUiO10fdmB82XbfDjZmQ3pjxP6afRz0kl1ySBNnhWQDDRqxZZ03iWE67gOxOkAsrrNiiti7EArZth2yqF2u9zoDxPxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری رومیخواهند یاکه خیر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136845" target="_blank">📅 21:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
✖️
✖️
آنا: یاسر آسانی به سرنوشت دیدیه اندونگ دچار شد و تحت هیچ شرایطی نمیتونه تا نیم فصل برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136844" target="_blank">📅 21:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMCcsdi4vg4NF5apH6kuxuzehpdN6aBoZCKvWDIkn0y7KZZrJwOTSKVrp9OKrF37oaz9F4ZKPGfYbZ_Zffu3wPy0uhX8ZkA4FtnSbd4zO9YYnUJFtZhoKN_XKfIzpHARYjPy7ezpO3LqaPpe_5jAKHxi6dc1UsU7MOUFDcEx4SlfFA1cEVS4s6HT_-5qZpTaINiMD7ubjMEtXX-GNEzWAlVp_KE20s4AZ7RmgeSXRg8ldLACRpOzfdEeLhnwWUqxCX2VLJQCCODcSqsr2NCS28mZ3_H3HJaRQSmcOf6crtLAquC4gGkUF3eu_v7g07js76nNxPhtZ1RRsJuPro_2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136843" target="_blank">📅 20:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136842" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/136841" target="_blank">📅 20:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
❌
❌
#فوری | ترامپ:
🔻
برای دیدار با مقامات ایران به توافق رسیدیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136840" target="_blank">📅 20:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136839">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136839" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136838" target="_blank">📅 19:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136837">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136837" target="_blank">📅 19:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
🔴
پرسپولیس برای جذب فرهان جعفری از نظام وظیفه استعلام گرفته و اگه مشکلی نداشته باشه میاد پیش خودمون/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136836" target="_blank">📅 19:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136835">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🎶
🎶
🎶
صادق محرمی طی روز های آینده از تراکتور تبریز به صورت رسمی جدا خواهد شد و احتمالا به پرسپولیس بازخواهد گشت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136835" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">همه چی رو کنار هم میزاری میبینی کسری طاهری و دانیال ایری و مدیرعامل نساجی و دلال این بازیکنا در کنار بنگاه دلالی ورزش سه دستشون تو یه کاسه هس و دارن آخرین زورشون رو میزنن برای تیغ زدن باشگاه صب ورزش سه خبر میده کنسل شدن الان بازیکنا خیلی یهویی با دستور دلال هایشان استوری مشترک میزارن هوادار هم که خدارو شکر سوار موج میشه</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136834" target="_blank">📅 18:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136833" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭕
هرکسی از ننش قهر کرده گوشی دست گرفته کانال هواداری زده هر کصشری میخان میزنن، اون حروم زاده ها اگر میخاستم بیان پرسپولیس چرا رفتن نساجی؟! صدرصد هم خود بازیکن هم ایجنتشون با زندی بستن
‼️
یکم عقل تون به کار بندازید خداوکلی چرا هرکس هر کصشری میگه طوطی وار تکرار…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136832" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136831" target="_blank">📅 18:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل نمیکنه شروع میکنه کوبیدن باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136830" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Js5_AfAjKhy1GW25T4eLnq2VDB8eixxF9_M3NogbTevP2L51AHqnU8G9qaN4u-D0OQsTQKcPqNEJDPitvMtWq0IpHYqCG3rAgUINGqFDSoauxlUYyA7DqKdVcW_cJMBugOrjrWtwPc41tgXO1-Xs3cWrM-IlpAFABXm626oUoWI_utNAqgyiNGhSuD6CK8pBEy1-zuBolNBuzmlQpAbUw9jrcB9EwPKyN_xnK_BV1HJWLpP1Yol40gO0Km05iT1RQ5xFas-GWzkyXZialoEr1PKk3CVPox9x4JcxKl1iYd4EsqbOZ23cQeTBHp_f_xVF0vMxGNr9JA1VFuqohT5xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند اصلا دانشجوی دکتری نیست
🔺️
رئیس مرکز ورزش و تربیت بدنی دانشگاه آزاد گفت آخرین مدرک بیرانوند، کارشناسی ارشد است و او حتی دانشجوی دکتری هم نیست.
🔺️
پیش از این بیرانوند در تاریخ ۵ خرداد ١۴٠۴ و در برنامه فوتبال برتر ادعا کرده بود که دانشجوی دکتری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136829" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/136828" target="_blank">📅 18:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136827">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔄
🔄
ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم و این شرایط برای خودمان نیز آسان نیست؛
🔴
🔴
ما نیز میخواهیم هرچه زودتر تکلیفمان مشخص شود تا به فوتبال و آینده خود برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136827" target="_blank">📅 18:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136826">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIiwqzgcH54NI5I4RJx5oeV-1ssKVY--TqpRNQOX9K_wsd1XmHx_Y4g93BDBPh3xYJoBvLQmoE_5RRjOoxYDfi4aRdeiqr-DjDSDFQdh9uK6sd3x7XQu3pO8U1E1JJtmywVNIZs5Qp_YCcDjtfjqExotoyT5MkR-N9Bwxz6_ay6JUZOIMMb9I4FwefgdmivAu3FVgm25KInqjSw-YNEpBOCsnCdc0gN2FSTqQk21KxkHV19byorBiXVRIY50JkjbHKXWGP_6IkPsTrR8RdlhihE4d9LaMAI3mjjMBWU7IoB4C1s14mTuerQj6p-WTW2TIfJsdODRZDjyFy9Vfzunmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
آغاز یک روز پرفشار و همراه با انگیزه سرخپوشان در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136826" target="_blank">📅 18:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136825">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔄
🔄
استوری مشترک کسری طاهری و دانیال ایری برای هواداران؛ ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/136825" target="_blank">📅 18:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136824">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/136824" target="_blank">📅 18:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136823">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/136823" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136822">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136822" target="_blank">📅 17:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136821">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚪️
⚪️
⚪️
انتقال کسری طاهری به پرسپولیس فعلاً نه قطعیه، نه منتفی. سرخ‌ها علاوه بر دردسرهای قانونی مربوط به قانون «پل»، بابت مصدومیت رباط صلیبی قبلی این بازیکن هم نگرانن. پرسپولیس تأکید کرده بیشتر از ۷۵۰ هزار دلار برای طاهری هزینه نمی‌کنه و تا وقتی از نظر حقوقی…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136821" target="_blank">📅 17:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136820">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136820" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136819">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
پرسپولیس و تراکتورسازی پشت پرده توافق کردن که پرسپولیس بیخیال قربانی بشه و تراکتور هم بیخیال محبی تا باشگاه های اماراتی بازار گرمی نکنن و مبلغ رضایت نامه رو نبرن بالا
😐
/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136819" target="_blank">📅 17:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136818">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136818" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136817">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
محمد قربانی: پرسپولیس و تراکتور مرا میخواهند/ مبلغ رضایتنامه‌ ام ۲۰۰ تا ۳۰۰ میلیارد است
🔴
🔴
بهتر بود نام تیم نیاورم، اما حالا که سئوال میکنید، میگویم. هم پرسپولیس و هم تراکتور با من و باشگاه الوحده مذاکره کرده‌ اند و در نهایت باید ببینیم ظرف روزهای آینده…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136817" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136816">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136816" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136815">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136815" target="_blank">📅 17:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136814">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی اعلام کرده یک مقام از باشگاه منتفی شدن دانیال ایری و کسری طاهری رو رد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136814" target="_blank">📅 15:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136813">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136813" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136812">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136812" target="_blank">📅 15:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136811">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/136811" target="_blank">📅 15:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136810">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKMdE8i8htKeFkE1OCn54L2ECcg-4aWBPeyEOJJ_3CaU4-7BH-bPnKfk0xlkTEjyUbcdIbgwGV6zzGib_bRloDMJFqoWF5xDarPdyw9n-XGqkpSaWAOj_bL27ISCuwY06vls3I-fQvyd4vukcCzfNhwpU28j08dVWLZDOIlb2CxznvYPc0knTwcIwpMEi62_OJ83VGNIpyCB2TnKg-SNdtOyeWILnIZpobFroNP6Z6OMdErwQhbvfAT3dJ9uC8NCUinI5wfYyXgzCKDtuy2XDXl1aoNz2fKbN2nU_irpa2NdtDEGZt40O_yHT2TVRS9iF10XJ_v8yoaNLf6D5gLYWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاظمیان به گل‌گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136810" target="_blank">📅 15:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/136809" target="_blank">📅 15:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136808" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136807" target="_blank">📅 15:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3bb8sOqQfHbZgHZlLoxEIZFjMaVfWnw6YTBiJLNM-pl85rMWqLzNvEAGHLJREkymcBp0DWw4AhLLzyLQcmYEv16cBw67nR7UFkVXQbNzyAvxFeUb-HYIk37_S3FG-DLgH15VNvz70iLFEiW4A42N6_OjcJM_Qq1_QPh_fr1wPAD706OXLwk7qJMgGN4clfvv6GKzK3VTClt7GUoKzOkUBHuoOFs3guwL4xRqE8Q8tQCNFC_pLtMet5Jsbz_56YhCKik_A3XBcXL1gP9YmtK59t8zocUrNu3pJekjFbxvZMKeHOtWSIWJxgVycOj7b6cVl9JUFXZ1xGyKjUabRDOZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136806" target="_blank">📅 14:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
❌
باشگاه نساجی گفته از اقدام پیمان حدادی به شدت ناراحت شده و میخواهد دانیال ایری و کسری طاهری را به باشگاه های دیگری بفروشد
😀
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136805" target="_blank">📅 14:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136804" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136803" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136802">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه تراکتور پاسخ هایجک محبی رو به پرسپولیس داد و محمد قربانی تا ۷۲ ساعت دیگر تراکتوری میشه/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136802" target="_blank">📅 13:54 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
