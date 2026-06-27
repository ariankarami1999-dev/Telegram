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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 323K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 21:36:08</div>
<hr>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbeb7hXk3EwiMKcWbI-1bU1t0SDA_YDZkGno_dVcUFIIKD5MdAHl7yxCK3bGc24RawcCt1Y0D8MxfNfJTyVPgRwJrIvQLKbkRt4Pw4kqlAFZyllOFwMpMmXKnr2xsSHxvgQvS0YIr_4vmUbc3QOCNh53EZg51KzHx3jAKBuo0oxIqHE1U9lMToYIlm7Zh8SKCS44tt-TfjMC2-LLs6lKjZYgxHbpG5faNZeD0u7PXB5wa_DKNO9YKp1WQb6GiPs64hATGAdOLG4P9dffHW7CxcQtfVhoxSdxmmk7fGY92Q9csptDkQJEfnCJWdqiAKtUmzMUt1rIQZLl27EDxI2gHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCMS5wMKmZ0G7DK0ovXrFIyxpV13qG9HZIa1aSpySIFF5lFG9Fa2YVivArsoI9obZTbCinuCrPvcMhEjeExU6V-MsxNB51vTCZdNoTbsNQet7i52g6DHlmXXx3yedYzdUC1IlUiruoa2Q_iB1kfcXKRy2t0gQ7E8obscrvsjDAJnPxBa8S1JVd2IPIWDtcB11Qj6mI6z6tKmqeV55HbQ6iELImIy3MKvci19Zivz6qchmhHOPtV3hFHnMw9XqLcK35b_WiaB4b4au2RvKpxWKEJvMRSdL9GQgb7dRJqNG1BrgySaU91hhsa4Ew_uREeDcCtBvX4-WHeniZiFxPezTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l45UZTHVz3bJIDOieOkFmt4HLUlXFoUwhF_qGI1r-LecV-GRKnv2PYcTWUiYSp_iKSZFczPp8nRdEyRXiCb7gioXJxoeKVnrdfrssIFgSatjpV2Wh9U0PGmRXhxOmuWsr8Y7SbVeXJ5MR6DFI1kz96V1sph17OImEI2PWvmOg99yZAVnR5Dg3yjH8LsjMGym4TxT8J8x5-75kMULvuibYOeNSrSYiXbZgucr-Rus2TCGNKzG-2TRNE_QQ9du8z0-petGuF1DoDfcnP745wcCFtICrt5R-TPky9cXVGHCIQt1Yv-Tn1NO1JLi9mmghq6JB56Mnitf4wEAwkMcs4fBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkBqacVAAXT0TPLkF1a-ymhldOzxHbKgkPrRcL6StbyisgBV43Nw4uKGXECz3SPq-oxzx58l2y06PpmkugiwYF77uJLvfLIg2M4I7jROxs5Uq3otxDMbqeLRbfOQbOei9pqQLr8EnnuRA3G062EefuwuY2beSAhg68W2mXGWo50jCMP2Ziv_GP79rQF9gyBHSBMpLf4dp4aLfjipVQMF0j0BfiqXnqwXZUbZravzJYZvc3uIA4cIVClqVl3bYPBuoy-A2iqOEPFOFfT0nOOSZakqg09hAwDypKvNSaLWcQtTWzhOquE5jsSgPcuOkBu0DGFuo5iDhVHFpgpkgDGsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=sALoWcUCA2IOpkOhZ8P25XrurhU-AkEnON4p-h3MnW-HXAvlAOCSWGW_7aedBhzHFU-jvSNmANkdvAFlvErlh31t-zTBCqAVP2Mp6TNLfBZohfdgRSQRxP7iOdBcUBER78X-3WzPggZLuASc5jo1dY3CKKuPUIm42TCxR1F_Y_dJHAHKGR0v0J5BvlJry_OKbZwC65r02BLLsi2LHgMuyXa6TlvByw0CHvWbxqi4G5L1kaScPeCVnTMEuB7tHmw2xNZJC5Eb0ixrqCv5faYlSvM9fog0r8wpMFwj-ASlAVK_66TJcgOqMnRO4rotAWA0U2lVxq1VeisBfN2EJlN2vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUf_cmzLhvi-LfLU1vm63U24P0wzrkH-B7ybda6nxyK6EZ982RI3NWb5QjPzXz65nILDye0ObiFwnoEcwryXHFbm_2Hh-l-E1v8yuWj7VoOeTiE-H8KdV5qfqVKuUirZ0l80YBDTrHJ8kmx3qu_ySlsDbArsMqDS-E0gNoO1TIIf_cSC2oRvfD6L6CwOXJ_n1ViNvIAr_5OW-N2qtqvpFQbWnlW5FSzGeAal1w05qitCF-fqrs-1G0H2VXfb-R5xJ6Gtb0Jst3g2ngq-pkQVU2kJQplazPdsu8DoCP6f0T8Q2wAf8xD7bto68hrrpUzmnUHZRwe99x6OTOVuDYawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf1fT1baBfZeBAaqurmo0eM0StgsZmlKGfoTXoK8JPswP8WiUMwlssOvMZp8EFz4WRnpfXiJlTILJPEBOxJIO746b0TVlGGGE7vGwbHLEK9dPrTospJva6MCa_m9rNG0uCAKDhuUjqmoi6TmEn3S7CIsjRVANye03pT67-ubxJSwzt6XWyv0rUBR2gncjI_HWeg4RbrA7EAsexnX-frZAOTshYR8TiuUc76L8YSGQOpvnhYXae5SH8vbDQ721mJ7WWe-swW7n_gK_6ahYgGtv-B0787NW6-f7zVl_5CBEnD7tzWToAh-r5qE4kRr5t7cXWRy76F0TCtBm6uLFZljow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlU--fywcKBQougDMHneCF8p1u9upW9z71z0NpI51l-Q1AKKJbYYj6AmtkfOQARua7IFaUN8xBBOrjKqS9krY_3lNYissD-isN8ne6X9bGOC0qRfxuSzqPZnCLcZE9szX4SjmptZXbX6ODQwOJLcLGN_pOeHfcAQIuQJ7O7arMisNYv4NLlsjedxaeZvSlRIZ0Ff7ei0jFjpaGxBL06JBbB9WQqDFDDzsfUVFEdYFTetG0EQ9QDk8XdMifPITKFAb7gMG6UFPcq-X__dre1yavqFS0QOavptwiRpiDoDjKyG6UD5SocWnd-OAduBVNrFTGyC936e1z-C2At8k4JDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0SGpEhvj3pA0QjvJPwWQtSdljBzk7o0mIgcNackYvZN_ANBNL0EiZZjMStPUmhl1vD5iWaK04KywXSI9KiQgdLJZLndo8mtMg774j4eUWlfq6xR44IPLIDfCtwNmTyx1jga4ewv3I4iCZy0gkkUfOHr0hSWQY0UD5kSn5KbG7ko-B2OwGobMWzNif47JRaIBhDOyCHHx4aNp9b_s17nr4daPnSLDXg8zPRJ1ZqQsYAFUbAhp0cSmQSzgJ_qsVxz02oGOZFISFbJoB84ZSMLnpzNB2aqdWuqb32vg_m3krA1ZSvL14RVCuFjGIr3cmeLYiQhYJuOBc7i1ehDXyed_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=t97c1llWse_8seqhPTcGZ9iKvh5un0YDVK0Rk1LEThbPDTrAyEbh1IgzYgJnijVCClt1AeJo9YSHEBfayiZd7fA3rt-U8h82XDPQpDX6tOgNtUBfmebaw1P9EfRJnUdLjNKrwozV2lRQ5NR5vvITzX-xeA3vRHEfjnH5PkopSBNUC1sZd021MZGZ3dHgpIaS1DxFKz8yhypa7pWMS2T5OClmxU2zVtc6cfHAsjuyMhX4VyhkEtduyaKSjmuKIOeRW2a3r5vuGclFwdhDbKLJZEAf59ncftG-_0XdF1TstSm2f-Es4JVWQwWzmHjVBV5TAS7iE_U3aGwjd1VsmZkbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fqwCBfYfCGbQ2CNMUYa-K3lN1xZEozQ5e4T9U3TKYkLPRmoQHmD3sQqJTjhaxxthuDH3xiAUMU27qln_bTfcBPbV0WcWFIALFcsHItqT86ASRdFBptMwmSIBeIJAbbe5YOqjRXbnw0VwmS7POXV8sbmJ99J3K5rGSjQYyj3bUkXjcs6hD2rlT_mfvEb43p85eCHh3-FWtDCLPiAA8dRWFpYb8SSRcmmAs2Cv5W11Cncl3hPDnqRdi-QZt42ZDDHoLygyig2kIfKRL-geTkEJyZESm2m4ajx2tvECxNpVK6NKC7WvUdPHeBV-vUye51EBN7wLvV3w6fz8J_BqPRgvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
با لنزبت، هیجان بازیهای جام جهانی رو چندین برابر کن
🎯
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوس های روزانه مخصوص کاربران فعال لنزبت
🍀
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G6
📱
@lenzbet_official
📱
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24471" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzddh3S9A0gKM9d_5xrvTtgPkOhFIhW0NqkuqckpUDx5oA3yCSEPa-O4xU-uM_jJDZvFKjX00pQ_PF5cq5JhA-nTaqazCLPuAqieV8RWPdavUYsyi2lL5MwL_tax_OjEJlTerGEQwYbrvgcioCHRpu4IRmL3T9VtDMpGoO01PpIVXxPED7GtD2VgLv3XtS81mt3OiawRZsUdSGbmnGIznNujeQqQAjECF0vI--9qu-K9DkLlPgXdlBM3MLmceT5HZAty5g31G2v6EIDrA_f6VcG9XulXlYg4QxPVe2KPE_neHp9TgoqHKotV28JudU-kvRjzoxHLUBTSEljC0lUtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJPecoUXtUKZFl5nT0gP0Hr5Yi3GNSfXuOIM_onkA3mrYjGZxghDJTNt2jJNRG45QYlNATnVTQ_4o7OVhW5BAe8zvjWUW_OnWBd8JP2udf1VV73CLF_aL9jJPQSqCgpyo2NtRtUDjIwAkEZ7PohhGEwsfXhPYm0AHuKMVXzFkvcXA7rOtL5fEFCM0J1QFSdRXGE0aROjDe9vo35J7yeaxIHKRjKuZI7La8moL3LkONYXSxvWTRPGcCKZWAndSX17g6R0IMCRavVS_0VL9SgMSZNkpRPkIGUv4-QMlXudaMWkj1OdmY7ApgUIRVMPhpOFWfI7UXvUH6UCzwwYHA-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbnnzt24GrTjoQjNMmcP-AAzOvgGfvU4zUeRcBsKlNdm7BrxToj5kfV7REotrF_W3_Nysd2TtqYDg9fOyTTeOTkPLBe6udTfsxDVtF9vpoI-n8m4p5j-UKJd-ZGTgR9IpD1WTrCUxxBXtxmU4vx3Lsu2VwRgSDJaHREkWkSZfvpj3czoLTm15aIe4xWOrPvEW8aDcIHB7GmFrRjrG2kOHbokg-x53NC6S5xhpz9UNV1dxvtn0aD0xtgocQLCsw8IaX2oI8BBXEwrd13tNLmnAmK5-jQRPIiLV4eWzDwAsqGA4y9Eu5fXYBOyAHkwoJAJKxPuNoyeUreSTtT5RvBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsGMifHXJV_0ZrtRNJ3rbkAmZr-ngSeE1zOuxU6vfNOkW-cV1L8hzjqf5rPBGwb1I1Kg4B_JjC1qoms47XPbNjhWsN2qYaPIKJvO0ClmpinhSWxlDlZtNz7zzmzWxG8wotI2kwcdNvJkO1zbOhw1nqu_hNkPbUbQrqRS2Cp7z4p8H8Nq6Uai96T_W1yqhmP-T3viTkFWQRQ6xVcEXoOv_Xlv0CSLw6h3UE3ZFDJWOG1nAEjUQo2EQmEvi4q2LgJxrFHEU6F8hujtwSfa7OYXmYpxjN5kS-c_pdH1EHVqGe0Q5jr0rlLZW73GClosOgXoEeyvSphlMbF4e0H4l_Qfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNTX46FQeGlwsJtCe-1cxbVYYqrDvHmc3yjZe87upnD-_IKDz2SGhP4QucuhxOlBXklAEk3EqxDX-2svTlJU0cOmMK1zhRKBCaPb4JgkbNWH-OmVGRPYbXuUinbCayZeUCnK8bVC_K4nLepn7LvTenlOkfkDAXYwjCv7N7CeMRbYU5lJDcBv2I7xqio9q-a0IF6xfgithKiklkPQxbFGBYU8SSp-sySonC4RZfdrOaRTrsZR8Jhh599zcnVjb-YfpkmUONpFHgK803u3B85Ll7zbjHdfpsgPqYEkrytbaRoduYclDvCpHhxA25BSdxH9F2zEjG_I2020TpQK40pc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HNjWfMpwIuYeRpHM7VcT-ZAQc8flttrJ_SAF71c6TsTSvTmzMgeXp4fpk8mvN_WmHB6OX0BTHQbqsvnM4_ZKrnI2UVQOLkNM2DUpKhfRsLtkVnqTX-b2zGpgUIxTF85rGiy7QHeWO0zABNQ0pCJg7OL_kK-lWBxI2WkHVdcj9nhFbrbl1gBiOkEplqM1kzzbDv4V7Q-Inwoo4JXM1SzUSuojKeU6J7dqNkF84rI5oLEYRdzjWBNyD7XeZSB7X9NBxsjyS8_iPJ5Ob0qzA-Oa1Gni9EBV_BojHELVEBxGCmMVweJ9riaq2yUWEGXvHmh4zoS-8ssh_Acx-k1doy4njQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=HNjWfMpwIuYeRpHM7VcT-ZAQc8flttrJ_SAF71c6TsTSvTmzMgeXp4fpk8mvN_WmHB6OX0BTHQbqsvnM4_ZKrnI2UVQOLkNM2DUpKhfRsLtkVnqTX-b2zGpgUIxTF85rGiy7QHeWO0zABNQ0pCJg7OL_kK-lWBxI2WkHVdcj9nhFbrbl1gBiOkEplqM1kzzbDv4V7Q-Inwoo4JXM1SzUSuojKeU6J7dqNkF84rI5oLEYRdzjWBNyD7XeZSB7X9NBxsjyS8_iPJ5Ob0qzA-Oa1Gni9EBV_BojHELVEBxGCmMVweJ9riaq2yUWEGXvHmh4zoS-8ssh_Acx-k1doy4njQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=nrW_ObZrjwX29wPAKyIvWFm9nYNon0YmlRCSxPFqfkgD_8MyBlgQC9uE2CehG4hTHwgaphc-AJZYXzIHLPVprJhRHCN-kHusOryq_ug5iyXzih1DeSjp5DoBi7XBxrmrJDwB3RMhkf73Aj77rSpL6GeEDIKKy-0aL327zDNvxAVR1Nrjc1OUYFaStZBor0IKh9D96lRAJrbT21LAL-ziXom5r6-YKhZAkhwsmzoVE5ms9WwtYMIM-LuaxxedCXMaeishxN8WTm29fGaCV2Lbwl1q8LSJtIS6Ecu9z6-weW9ORxsboJyXOu27-XyNLToOZX_U6oWyn-xIhuJn7d3ON1qRLrxXPhWAbou1lxS0xWWOPM75ugPeSD0mxhm2X1SynemyYcZycjp2OCkpreaMW3xYgZbk61-o30P4P9FO6mZOiH94CauFhDy_1HMxS3VZFPaxSdvRGV14J2oEap1DQJFO1WqqxS8yoBEeIB6eTso4WXqzSbeSUFQk-ooDnIL-3l3E7jU-5NmqiZGhVu-3Yja1i1bciXwWs0MH1IKJEO8lpl7T_IWoi9wYx-kWOtft5tbgjJESnDj0ZB611CYKtTSevZ7DxUOS22_PzsYB2egfjgXpDHD5s89LTjrZkaQkDQQH8v_2HAahLi0yd7eRmKGW0HTSsv7CQUuA5h37MNM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=nrW_ObZrjwX29wPAKyIvWFm9nYNon0YmlRCSxPFqfkgD_8MyBlgQC9uE2CehG4hTHwgaphc-AJZYXzIHLPVprJhRHCN-kHusOryq_ug5iyXzih1DeSjp5DoBi7XBxrmrJDwB3RMhkf73Aj77rSpL6GeEDIKKy-0aL327zDNvxAVR1Nrjc1OUYFaStZBor0IKh9D96lRAJrbT21LAL-ziXom5r6-YKhZAkhwsmzoVE5ms9WwtYMIM-LuaxxedCXMaeishxN8WTm29fGaCV2Lbwl1q8LSJtIS6Ecu9z6-weW9ORxsboJyXOu27-XyNLToOZX_U6oWyn-xIhuJn7d3ON1qRLrxXPhWAbou1lxS0xWWOPM75ugPeSD0mxhm2X1SynemyYcZycjp2OCkpreaMW3xYgZbk61-o30P4P9FO6mZOiH94CauFhDy_1HMxS3VZFPaxSdvRGV14J2oEap1DQJFO1WqqxS8yoBEeIB6eTso4WXqzSbeSUFQk-ooDnIL-3l3E7jU-5NmqiZGhVu-3Yja1i1bciXwWs0MH1IKJEO8lpl7T_IWoi9wYx-kWOtft5tbgjJESnDj0ZB611CYKtTSevZ7DxUOS22_PzsYB2egfjgXpDHD5s89LTjrZkaQkDQQH8v_2HAahLi0yd7eRmKGW0HTSsv7CQUuA5h37MNM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=SA_4aGWbqzwwj7U3F2eqFoS5D1MhckgpYYu88AGGCTWSa3Wr6ysD2IVpo3JJfYS9MrFQxTuVRkEgvX5sDQRiLI-oGdLsP-8sgUPpu9z40V6Q64-_sPZS-UWGEfXBY6eMAfypE68wZc9bj2-XoZrL5t5nssW81XUF_8qhsjyMv999IJe5WY91_GChzIKv9sJrD0tR-C7DxbYxdMVgLfaAHk-P5NnhYsz3Wa5bSf61RBSVwAZNlEhRpW2fffG8hkrEIJZ8oLo3oAVThSYhRtr64eibsZJN93fpKwTs4D4Z8DKKEdiwrydOZ1kmQiC33lGF5ifFHnAkFCxJSvs3BzjnyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=SA_4aGWbqzwwj7U3F2eqFoS5D1MhckgpYYu88AGGCTWSa3Wr6ysD2IVpo3JJfYS9MrFQxTuVRkEgvX5sDQRiLI-oGdLsP-8sgUPpu9z40V6Q64-_sPZS-UWGEfXBY6eMAfypE68wZc9bj2-XoZrL5t5nssW81XUF_8qhsjyMv999IJe5WY91_GChzIKv9sJrD0tR-C7DxbYxdMVgLfaAHk-P5NnhYsz3Wa5bSf61RBSVwAZNlEhRpW2fffG8hkrEIJZ8oLo3oAVThSYhRtr64eibsZJN93fpKwTs4D4Z8DKKEdiwrydOZ1kmQiC33lGF5ifFHnAkFCxJSvs3BzjnyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVr-5_FidoL4XTdfSURIEHAXtTbSbYGj8vYv6t_GoZp_7gMwTQJXVYiPSxEZcbrq-jbhENGZIy5hf8G20fG0gPC2KcwcVDcdMMErpgeBkLvAZkIFJMRZCaC8noID7lGl4F2Bplws1M2Suq4w-WpBbrLKKQ2k2eePiAEsB4KrYIdSkMJp7mgDIk5t6WHg-3VM5yH3-0ekTfmH9o_W081bKKjVoaJR2yb6bf_hRgUnkOm8V2PpEEoSQsDoXtf0p4VvBaKEh--QUJ7Gf4jkpWB0_3GEOr6eADylQDzJaUFAYLkq7mrFFAoJOnPf7OXkl5Fp6o1p6Pr_A4G6lHqnf2833g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l41HJhKF6LnPSmcNwFJ0-rOUKYZeABfHDFoJU0PB_j7rtVEV3v0LOsO4i8QKgXh7w1UEf7iMsh0dkvRU-xxkT8roY7kNQTMtRCOji51F6qpPXjz8b2-5cjI4Q3whTGaaGnRIc0uq15nzmwTj4Feh64ALoDvwIjNMngYBL46X68FhbhanNC7A__jMMxwlFOPJJTzMaphNBv2MzTWOM1MreHMSk5j7vWLBWUfv5qAmq2j07rho0EsH29QIRpXCn3f_QvTaPSjFeiWenM9sc6v8yynv1FxrcYzzXMqUZwPhF3WUipJEx9q6hTVY1Q-1lh0yKi5Gm_pDs9iRCyQrVqZy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVsEgcskMcZjVj4q8HerJRkiras4qcDmPj9NS5Wuxl4XtF1ntM7LskFvl7VzCoGnLm9OyPyl85igB6qjwfWfgxnSOCdIDz9d1wK7NDMVi5zZdGDq-B99lTGA3UXcBadsSbjnyMEm1xqudoLOV9UvSE4NxyNp02ZGWPqHYQ3lny7UmvWcFpSPGYZ6DlCkxK7cpY9tKbPQ-3IkJ9Z482kenuXrfK1XMRlDsM-q2ZdDij0asSKIy51v-cGtg4P7Ihf5oZnieZzKAKmWDhNbwCOSGiBZt5_Xd2xP8ouToYQwM86PSpAKJ2B31mi8VeLIiPFfcuTQw6WfaWe0W01fmzGPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKotvAyThv_HllSAbqttsMMmp-72c1rYtbO3eKRQAetFET1urGJyJ3z5s1zbx0CtdApNmtMYYXGOrsK7DbJUU7QCsqwQCFk-qi5xi8DFbyDmagO-R75h1-Ww8OcH0oad0dZQfJzTQzTuZs4QepweFIbIG55uMjHaXF1rbBGZyAcXNkyYbqFC-EgOkk_oOBpfgmGrOwA0gy2xypcX-0U7_yvtWPPOJL3vg2GhOGHHNdT1SsgiOOXfdi4YBFy6cNdEo94cfsMZZkdpTu4R5k4SFoHHAekWLOre1K7EwKjWBQmUnpUHnuf9nRMN9LzkxdkrSEjrB05lhOIMV0WgVMDUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR9mMzi5qSaLMF9PdUiTmG2xTlr02eF5B7kbAd7v_XtQQDGFCtYlRd2EPz_KKSj9cC2oZZth7PnxvbVpQmq6hE5I9bifZCDPEQIbhuAxvgC5OKsVAaDQS-pPmuwjPZux_rc8NR1sxMwvLVzxteuKtCUlfLrRnRuef-l4xOM0ScSoWRx9Xvfb7P3WXjX0Eu3baH4x7nJYF_-OzogmCbCbgZ47oPmOlAJqNIOvIJ0bHaCNKBmBMudIL-LDLWALk0TjHoG4wakxxw_Ehf27x962ImXTqpmzPnZFZ-lL2kKHvnebMOOaNgElLVmRChhoDLU2e36msKycDuoLkugad64REg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GciaDBWBF8yKnGLqJ0LEDxlHCMu228rqShXe6QDcvos5CIXZEzHnIPhaVdoxk5v3DywkYpEqPXZGq_2QXWHSzBsZWdjL6u0v2Ie4EcGH1gJGOl2vYWQ0OspvGEPJvOUdt5MMLToQPGl5FGB5U3Yq0otx2sA_3cdZu95h6tRk4E7jhAJEJ3s3PRcVI8xdNDayBQwhV6Yjcbmp-Ad6bR45kpCN1t1gOd5zYh3cdwKUETqQ83t85dR1KyEgR9-uJEfwjA36u1IWMtr-sBn5TVIaqUmy1GJONHQVBf1-_sY_MJ3ViuV38_-UfILweKAiFg5psaDdvskhB-dJGXbPVfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvd_VYhXptc6rOMRBFaERu_fG2iTvM7R1mFSGNDrt1ttj7yGai7mPoS62P6k2qz1swxBUPTkiCVvoSiUeE7nZe1StlK_b-JMJH0aNbLhcLm0PnDJQZDiVEYl2ToR5BZSw6dQUd9p275fTlT6w8snfz1E9a4008s0Y9j8dI9C87xdrRZRg9oboTgn5XJx8seVjFvEeqlMH93Ugsk5TeRjzf8qyq46fvWvXVA7fLXDTkXjczz9rC54maXVc0r_AVWQzmzbGR__ThNa01EDBibsHZb79H_LpQBZCLzxqqj3RP0XMqJPWyT_GVFyRU5ZpWg0-Vi7Hatr_cQYoI8hXNr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12f2BdpS4D4FkCGuYkAIfXHRJC9WUdjZKHfM1OjuenfhIFNf72freQns5J31A53MrKpTLr8ZIMH8aUEsy6nqH8uBLLNsOPAVOPPpOuCGrRYuP2ik9622Xv6rrOMH2Ei4c2KwKAEjpCIWHN6WWVub7zAPGmChcUQZ3XzUFvTDENKFcyrPlM1BIEIxrnRXc0mbrDuhTnDIqYpCrxIJl19tKVATRLzNyxsjO1ZLsfdw5yoYGflEAeMqmuzSTayNpJZKfPfoWBFtoZS6V_jkld-x8nbRXOm_t4wKaRNZSJeiw9_bv8pgtTb8NFLSeqbT9DTepXb1s2pB-s5HeMMcrGlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3E-Kdeu0E2Q-6-Kem5by-oYJkpfHjSG-LJaer3-APo-SlW49Y5Jr1mawNFKcYjsXHSMz69a-nPs78uAdQL9wQ8paLsVobxtWsgXKLCJtpLviInOEQVZ05dBnuuBta13jarnmPo9YoySDLHF052EMIXYxRgahIg2sE2XOVedzXrqKY1eghzbtxY4JBMBTdYWrNXDBQIbyfdZJE2EAlQcFyMwD8uyosyFD4GR0tFiEMvpNSgjHlFJ8MWuLv0p7KZkmEyNAeSWC809CN25y5D-EHl0UY9Ge_i3Kz3LSw566NMlsQ7B_4hH9ObSlERQX5JkcvgydPARSltdxdvVPcJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ_5g2ixKZw4-8x-XIv7RGdxWZNLdD7lMBzIzCuVC-jv8GR4Z0nOxqK-09vzgrGVOgdVdGfLbnE0cknKEfZEXMdG2wyKtSwY7ZEAufXeSleMweQdnWMk2bpCe33dHFnBWuJ6Rq72UqkAidw0-XF3LfIujQ1cHTVv73M8K2ULQwRt0AlE5usAGtvl3D63gtyTW9yEMuZ96bSs9wIHFjBl91KjOg-pktXxVDMpEfs4l4dfE1f6POUMaUdeLsKmarDiAdVeX5Y5zvj2ahTWssB9oCiTuZ-W4laxuwNlFIqKHSQVJ8NBcLxhGmkPXbVkyodqAlcmhKO8658BqvpTf8nmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ufWXIkcxVCl242deZF-L8cQOdpg8fdueu6yhZc1FQje5XkLuq1J6upx3zZd1oO2nTNt1ParpbwV-_wKHGHqiH4OjB-O9lGCAsyn1WLuVLRhQQQ3Ae21CS6iPbyp6v-zT-1OinIBlLOzEK2kuspHfVGfsuOI7-jCNSZdltTt8j5Tqo9PW4GknfWdyOmLTqucjItuGBl27DNss-FLsU0QSkTEkja7VJw6Syg-Bg4JEIMWGcWXppv4XRNoXWJw1Y-mmMe-gGXkVo8-KGfCYDZOBzG4XndFfQWeXqG6yXN4uS8WRJ3NBRT93T_ZV-solShdosSydEVQhaIq-LF8IGoX2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ufWXIkcxVCl242deZF-L8cQOdpg8fdueu6yhZc1FQje5XkLuq1J6upx3zZd1oO2nTNt1ParpbwV-_wKHGHqiH4OjB-O9lGCAsyn1WLuVLRhQQQ3Ae21CS6iPbyp6v-zT-1OinIBlLOzEK2kuspHfVGfsuOI7-jCNSZdltTt8j5Tqo9PW4GknfWdyOmLTqucjItuGBl27DNss-FLsU0QSkTEkja7VJw6Syg-Bg4JEIMWGcWXppv4XRNoXWJw1Y-mmMe-gGXkVo8-KGfCYDZOBzG4XndFfQWeXqG6yXN4uS8WRJ3NBRT93T_ZV-solShdosSydEVQhaIq-LF8IGoX2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=mWVwD84Tg1iY6BHd-6PBMt0e8FJ2m5tdq8fcYlC8hZmHZi2WpQnPaY2QuYVnHm1MTs3ftTqdC-HJWkaCfbgHZC2_X7RUiGXi0unGKYSXRBXkd4qMrk9iSEPG17-1J517SZsiRbCXDEE5LJ0PB3OSO3GxESSe3eLe1UT3mZ5FGYkFbarmKfTedZNdlzaE5esmFn__3yuYh3GoscgmYabNsr4QWb7lQT74GrwRPoZCUglcx4obvG1b3ycWYrfTZ865ah6ed26ah_pqSwD4DB7eo_PArtkMzvX-t0qRDN5ylQ3k-LLp9TnVmL5EBfTHFGH26mGRBNEWD7QuHUxxN-nFQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=mWVwD84Tg1iY6BHd-6PBMt0e8FJ2m5tdq8fcYlC8hZmHZi2WpQnPaY2QuYVnHm1MTs3ftTqdC-HJWkaCfbgHZC2_X7RUiGXi0unGKYSXRBXkd4qMrk9iSEPG17-1J517SZsiRbCXDEE5LJ0PB3OSO3GxESSe3eLe1UT3mZ5FGYkFbarmKfTedZNdlzaE5esmFn__3yuYh3GoscgmYabNsr4QWb7lQT74GrwRPoZCUglcx4obvG1b3ycWYrfTZ865ah6ed26ah_pqSwD4DB7eo_PArtkMzvX-t0qRDN5ylQ3k-LLp9TnVmL5EBfTHFGH26mGRBNEWD7QuHUxxN-nFQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YViYcvOtFu9vN_-LU6-m_TTS2rHmJVkc6QBPo_-7cITD_Yf9o-KJH19q58-U5RLwIS8QW6dCL0RBTbu3HuURuOIH2c1-YGr2wuPEcUa_BkBcmT2_y9t7cscxlMBfxkwGPtcdDotguOzxIrt-oSsH-mZ3ifIn6pwcBzCYOC06Oz4rCqWSVu4z4A3PFyMfULWcQYh5CuIBvdTX6frqQ4BI8b2WPYMdXx_RHDBY65ZkNzSlRXS7UTx5BOjk43zMTZ1Av5Chk2DQh2ytxeGlrwgTEZ7TsECOsGcL2KdknKrf_9qTPoC7RgzUt4jzp7A_dlW7ywO833FjkF9FucsCvl-y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود بسایت فیلترشکن خود را خاموش کنید
.
🌐
Link
🔜
MelBet1.net
🌐
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVVDoaQPmRqRtN06sfGihaNh7m2gFjpB5opUMKBS1v6UkUclVDj2JI9-NzjRWDuUN6vf8qHwW0fpGVJtizpZET1LnXAoIFRtxKRMpokHmMft9sfeamZ58HU-7q8zcI04HuWjy0JTcPlHhgCQGLgnA-1VN-yKxaBvr074Grn4HiJ1FQgg5E7IAvqXVlKYWosFnLXQqP1si6twxTfJgmdJlL8Ex_aro6ntogBUZc_SCymRv34fQ1J5TArGhEUZrKoW3b3C8U4BuT7X1HZLvhC1BKPd2U1hw2X41b80n3ATy3GgqM4WcqTZGU9MfMVkugXKXAQRWMxlgD2cE52Mtsd3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O46wgAR0xW0vzSvVLUdJEaAnJPEnEgku6uhFYuE9uGn79smareeFeVPKh159rboZH-bAmJNxPUPK1ZV-ixMZClrbzIojxmeQPlDFPNQ-2JuIU-uD6yfBQAb9L8qTUr3LD9fVuZVrVoqfctxv3sojVSxdotrG6AG6lJyUjfEyoNP0IYOr4wN_V5DvYjCRg4-qHjAeqWJQAOeT5MgRHBrUNkaobysT5-w6_8h9Smf9_SqgV2ThQa43N0ZI45wkhRC-iZcR3FXbOavZgwuZwh-l2TNxIamaApjRN_i_7YaGMNiuJRgAIEcsiCug0qGLexe5vOCI6ys-V3g84qkNxVPpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=PwT6hbzGA4ewS9g_jQqFhSuoNiBwCXcUyaZkXXUzcY06bmmlVXd0cCTo3jo_KhuzwShTZBxuJSGompUEmcCI8vHRtrjlLJkv5EegwNF-H-a1FF1Bi-CdJHDjlR_PMUaSub2Z2H4N_FKZTCwjsArbaGbsP7VNLSoZmzAF3SjvTUD23-bZR_T9qDcWmLeG07nY3ImYpGaEXbcCuEpmKaQX7w48_yvJb5XkittHQ5FHw710HDZvxY4kZnMvHBoZKQWif3uHXFgyDHnXi309gj2hHwxy_hIyQBb0EjesVZXkIK8EkU5J7Fu_X0KmcqsP20haU3UKn_o-ABn22wKNffqEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=PwT6hbzGA4ewS9g_jQqFhSuoNiBwCXcUyaZkXXUzcY06bmmlVXd0cCTo3jo_KhuzwShTZBxuJSGompUEmcCI8vHRtrjlLJkv5EegwNF-H-a1FF1Bi-CdJHDjlR_PMUaSub2Z2H4N_FKZTCwjsArbaGbsP7VNLSoZmzAF3SjvTUD23-bZR_T9qDcWmLeG07nY3ImYpGaEXbcCuEpmKaQX7w48_yvJb5XkittHQ5FHw710HDZvxY4kZnMvHBoZKQWif3uHXFgyDHnXi309gj2hHwxy_hIyQBb0EjesVZXkIK8EkU5J7Fu_X0KmcqsP20haU3UKn_o-ABn22wKNffqEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAhKsVJHodurTsca1hB2_ifJzpjOWNDLKF5tjE2ADLwb_xSCxF1hEzaEnTgDUctyjXgyhQq4yxViSmQYcucylECp--LJzyBP56auhUCVO7XxzMQxVOlWcgbwuzhCznfMeJZQkhO7ArnWe3bmJO1PS-Cf8YMPpP8nQTu4fFxcv9U2StfYh1EANgS6sZuLaThfQOGtiza27f_3s2sELB_6BSiD9o-i8mDBjZnEKuLZcmNB1UttNfH-6_gWik0fguG0ELG83i0cAX8vm6Q8RK5AKnMPqwDKx-0_6fWSghtUHQvsquTgZ6J2V1nCbNObCt7rePJ-EPcuwahfyh1a1wua0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdmABX3XrDG1p9q8bD3X1xILJQkW-nP1seONCk_gbm8RfE5adPQM97GTHbliOJsVfLRqBN0D2DL_LglFLTFDgQKZbRKqi953_D1_E8E5z8iT1zrePe0-A2aPvtKqgMgUFjuT6SEI4G4vGtw_6U16TC7eBUCtOjRzFaNLKh5jTggKYX1lqoDYVZn55nMO6TdDHQrrt9FUjjJAkjRdHDdXq4hAxs1UilOVQP6Y77e_7jTe7jqkNOdudvZVxXH-HjWkfmaJ3i3qxpvAJc5IJJAFnNa3GihISHOGsFeT1LspE5dlAKY2xGxtNqqHM0KRB5S_X6xJuj-sEnAAFix6XdVbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqKidKKOyob6VXBvNX17qtrds8tt2ErNSVep_tywDSdw3O3Pucx1xzsDN9PWvUugMtLjX3EbY0SvkRFmt5nY-lmM9WYuAxFQwhLw_jwdnW23T0GCSPZhpwrSMsxSkCgeCBMQ6pb9SjzwIjoSqCRsgFnQHDWgqRNmq58uhN9ePQP4LU3SdM7MXpZeXBiH53OEXbZ1FW8F-NV62eoShuoMR4jA4v6zELH0FmUbPqepKZj_7gA4pXlx5c0XI1lMQQUzvh2gn-zv1n8eLCQDY0CWfA92BZRSBrrtIo1b5ks3x0RiMVxLn6l1k-FbwwzTi_HTJTatwARLGzCfJo7yuuHvPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdmIhK12seTSXfm9BW8KhEYCBK20t8M3F3bpLBcztzyYo4X5i75V6vWeOw15O8n9mWfavxSnC4BB2_G3LDSfe_EAjChAJwsi907hahKeCwCMrZCcO87XLuhqh1L6KXWZ6HrK7hSHOPWOtz6IZRXuMQrFOX2jqM9tHKb8qUWriDX51XKw_-R_x6rX0UcgpjEupEHy77j9iWZMMrfAhRnvwY1_TIWtB3SmcHdEDQ1QJIgOFRuPLYQxsctMVwoTmzuFTIU8EQ45hxGeWjovD-UJteN1BmnmwxFSoi1-wmIGWTKDZTnDnm5LL3MtmlT3y1SpCCzr4y5O_hZF2v9ettbY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uU99Skli0jVPOoK7YPrXOtmZBOzPJsp23gVXA5BK6O-RSs7Jkd7z36KZppTfJgfvpf6rHzWZIAZkMOtgvbFxiIGgAUrChdJVNVJrVrctTTu84sF6RqBMTF2nrmBaskYf5sX61xdudh9roqJy4FUty2JAdC8X0O4PrSNhN2r_nrsePAXcrVM2eCpCI0Uv-UIkoD5p99CEmD9jCnNDh1eQKjC5d8aNX4UHVZbugdUhGVEvTcZCSlJQzvQvisJBlXefwhYdcCr9EmQKSY_OqTsO1xoy-BPlD7yqUP9nFzGc_PcHy9HwSBzOfzA5oghl5z540v374Xp3kH_g3F9HK5KUoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAhDascrPaWOrMVPpX8Y9t0A02gDvOJcVDuyXLM7UHira89lZr_na8kCe1y9V8GQa84EoWW-tsAQ5Z1S6FrGDx1WrMILid24P2Zls2calgwJOYwc-Cwv_OhTVmGLk7vWYGIAplRrlJeofFTU4TsaX_2q1N8onIkbqkkwqPqbhvwjdaB4ZJpBiBmYxfP8hBqfrAKzqbdO91VoM4Y7wxfw1X-IJW6FgZUs4vea6Tz0jRqD1P8JlQysri_56Agm1sdnDsQMD2jWa1c0zfhPr2ZSWhz1KMgE_eQ4JVxNTQVgd78bX5dBYJuxKkzug5pJHENS57DNYZqEl8dsgxCXzaKFdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLmhstzzHO-DH5KfPFM9DgIYEmQiILJNLCcShjfHxRHVCTn1UGXVI9dQpKwtCI2BBOlsvfM3Hd3n4-pmmCsO6KLl4Iq56g5ddcahWPeJT4PvPhXWd63GFafP4EgdM2aMD85E4_6pL82SVBzd65b7m8b6f4-RmvPKGIRA1TCA7gbOGSLZ1G8PtO7H1nGgJwy4DlpGuUwLJ50E89W4n9LpxKhiCa-WDutcTI9j6SzerhjMKCwlQqe1GExZQ6BuKHaDfZ7N2Y65Z1Ff5g3YnUkNmzWFSZKocmXkFIw5CedQ6XXmMCVJ5WVDVXFsyfI3I-6dpTTW9Uvc1BdAEv8uHy29Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kTl5iSKqSumi7BS_Lht30Zg9KYPnVLgXe2cp_uarWNPtXI1zzuC29aHPyP42bHoTVm4-Gs1GLqQ_NY-c-QIrsgUYkX-NKP0NJDsR1-HglW8nduc9C5rKzcds8wXDhprAbaCGNk8voVlY_SJPLFKrxyMRxxEivhwTzIiaZwqCJZEXNPIVFH005NurywA3-jgjX6sb4zWWeiy2lMGI74_goJwdHL89Un_naJ5J-Prf4-J9f5W-MZZqm0xAOao63LVQVPyBUsbsYk2yWpJz6LpfS0TbwOr3gYZXkEqzJcZgz0MICQ8l4fBAdX0_ps-INHaoMgCxPR6eXAe3CQU5P7XKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szFRjtNRHA5ok-SKUQzSgQkFrWUp_sG4pQsNPKnym8wTTmrmPbNcrF_F5ZOGuSZqFeKYizXfQHjoCCufRx2hKYKe7oKptWkTbg9kok-m5i4naYpXsLOsvJ5raKB1DlevnV03Qzi_Bci_QRhcOer6fcXvBRbcc7FBrHO35TeRUHrrUPUba0tWaL9wfP0T-OMilAOe5iMEtbzjfgrnYhYVEHaL4fib99yEeD3RCoMv9GcHzWFAb9rnITKesAnp0qNuyii-y1gOOyK30I0FPdV-pDhnBvChV9wl-qlzswIZF1TxVWDjSVUup97M01RwEkU0_BBGj7LtlP2bw_TYdNo1jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra9lFiMKAHB6X0sLI_fAxTGqHmyw0QQHrKJ1WtQImvtCye8hpcnYNUr9pTUFnLFbwnuUEtRy6N1ylmzqnMbxaiR5-f4toyvb8KHtHX6JmUCYERL4a-SUySfuhP1SG-Nwaqy_OPmvHW3cYx_t49roZAKUiSe5Ahg_-tUqpqPlvmUv6fX2qT36UYDPXjbsTY5JVXq_jilON_mi1fyxNLe235HCruGggpoKpl2zHVQS_pJYWCQPOmmy0L-n3gXlVETn1NoQDKEBBG4UWHc3UFwD3H6SaVG-AJ0O78J6YXlNjDCkRFyPAPf3ktkvcreLELSU-nPrdwDX9BFEO_7Hd6KEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ74ah9slNZ_f-Yf4lo-Qp48qeTylb1YfT66JTkdvpdkYR-QGDfqhiVYK-eFdKFr6h959Np9R8Q20hXXM6MYP8FR5byh5xoApzv0m-EWF2DDq4AzCkSVLG1rZ2WHDdBHVYGNC3tZQ72AqyVxI2DE26InPvIiI4yDAc4460GxX4XLcGfUOv837Wehrvy8668rJeoJ5lh7SQiG2dDMq1WxIbCGaWHubomRBWMCtocFoK4snq4LOFffUBHVgUSq41YoKwVx-Lt-i-mHRk9Ziugv4PokKdHvHshr3F9bcdeV9R8PeexXRAOuJpWJV0dP_jxzoXiZv5IL3zbuaDBwcF0JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=eQfbUsiODsJDxof9gd1LcoixtWwsg11vRTmGIxCNXTy8TefBPRz0K0oUpWt_cQ5cNPgxTM375ltiLN-Si1hLinLPOs-2I-iOHPJRWsJ111Tq7v5XQu7gbsTh-qa7go8n660-znfuVNajpwsMxnUmUZJJ5GUYt9lSLehTl_oAXYICdXqXnEOnz5pq6eEgJkcLvN9-SKBJ7TLoaEIb4ylJaEap4lw47KQjwK_gwjUE-kbQFiLPRjVkp86zoqrJC_QwlATnrDfqcOFamiG1H5ZiC0-6H-bCb3CjgTkxuhacBP8SjVmXQoHQaff4v1a4EqF4HSgPTBmVI4a44MfDRsR6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=eQfbUsiODsJDxof9gd1LcoixtWwsg11vRTmGIxCNXTy8TefBPRz0K0oUpWt_cQ5cNPgxTM375ltiLN-Si1hLinLPOs-2I-iOHPJRWsJ111Tq7v5XQu7gbsTh-qa7go8n660-znfuVNajpwsMxnUmUZJJ5GUYt9lSLehTl_oAXYICdXqXnEOnz5pq6eEgJkcLvN9-SKBJ7TLoaEIb4ylJaEap4lw47KQjwK_gwjUE-kbQFiLPRjVkp86zoqrJC_QwlATnrDfqcOFamiG1H5ZiC0-6H-bCb3CjgTkxuhacBP8SjVmXQoHQaff4v1a4EqF4HSgPTBmVI4a44MfDRsR6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PudajAwH9VuboGKl6qC8sJoXvWJrBo-CRICVWiEU2tC9ytIyPe-NSE7Y3AN06qFG399Ab4eU5zqNqFfRtFXKcT-70uCtet6HvCb1n_0vJu4E6jrhUMB1X1rJOiCT5_yR5O_Qss66iUN8zBTbAKatByxIATgOSgrXgnBRP1vGY2uF_Xb6LK3TvPF-xXUKU16NbpZeZngu1mT_o9AYz24KK3psT4ffhJ6d6xdpTaLsoONyvceP9GR1JYLKUqVN2zoq7LeyN4mS_UxmO0mp9HvhMSovaXmjwmkV9-hnya9S-oC6v8PIhz84OHj0kQV2FEfc5GRK7qo1prZYERr8ftSwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pL0wk4EuQkMNQWOvwO8IB6_JSD7EwYWIByIQG_NoKoail1UjzLtWWjcJ2g6qGh5ooPavx6P2_Cv496jUJyDKXwjFQ5b4TQGQPsITX9k9_0D_tASP7kvbjepuZ-noV4Khzwcgeo8qg6wvcZhWOKwyU8QtDBW8vhJ8dZeI0_uldsv4kq3y4FGSvImZm-4CiLs6BSb8GGjQOYRaEECS36iwQFTUIvKI42rVs7Bmo73VF-K6R2oKUHweWeOyZf3oF7oCbrG_5_TldfTFAmmuzwS7v6tSca_2bkv-NmVYmLjM2gtsJsa_wVf1YfdwFJqaWivFFW8D1930OPdFdIuGyp0eEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=OOnWQOYNA_2wPEUs1d_PTbxJI7oyL2uAd1-49FY6JCmJnY3CEM2cmxFeBEuMLJWl5L71Mgd_2U-poPizDFc2bKd_DPGfIJ7Y1bbQOdtRz0_6Fz0fgUEkGizpSRnWCAqVymNOcwDHgUndJrQE5ozBezpoxayDpdm6fPDiTA9h0knr6X6g1aLXiZRxHadX1prJ3t9BYza03W8zxZFcKpUG1gYRuRLk7XBVsaUhHiaTEr5h1StOye78XI9KvTGU4F70oLY-e9c24yGMKWYr2uiIxNVKFmJLqPcZ4eXiyg8uXNTcFn7DMxovAohUQvkIxuabBEiMqPB-SgpDm2cxlSOW8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=OOnWQOYNA_2wPEUs1d_PTbxJI7oyL2uAd1-49FY6JCmJnY3CEM2cmxFeBEuMLJWl5L71Mgd_2U-poPizDFc2bKd_DPGfIJ7Y1bbQOdtRz0_6Fz0fgUEkGizpSRnWCAqVymNOcwDHgUndJrQE5ozBezpoxayDpdm6fPDiTA9h0knr6X6g1aLXiZRxHadX1prJ3t9BYza03W8zxZFcKpUG1gYRuRLk7XBVsaUhHiaTEr5h1StOye78XI9KvTGU4F70oLY-e9c24yGMKWYr2uiIxNVKFmJLqPcZ4eXiyg8uXNTcFn7DMxovAohUQvkIxuabBEiMqPB-SgpDm2cxlSOW8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTtmtBphJGISWOusp9dGlEnv2LPGYwCrP2YtEpw6ZWUaCntwwzS5a7RRmiEdna2BbtxRTdaHzV_n-WEFPRhEZdcGO5VLYIp4CDv-9tCIVDbBZup4Opn-I82JtlQVdgjsfUn_n1ICcMWPfC9P27kG61vk3hzYcqo2ISajzrPBLa9EYNFhATuxC6doK6SMOxnm5yRZ9NyO0GiEUFF8cuXr8uw4pMJkwciwpxRC54Fg9ba24kYSMnI7MZMF6yIO7zphY7ZF1Cw9dxIirpXrtebOlYr6rXfzqiPbazKGONppr0vYOA2wYlETd6OV7XFCMnt76FyZgTJaEuA2InH96N2XyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3hi9ypSZkV0E8ohHG2nisWtNkpf7XfLXH1ENuRwh3u0g5Ubuj6YOPW2DjRxJ3DCtp0Z1HgepqG1VhKkNcMG75BuHtXa8cbmDIZMF8NStXGMQ_sxQE2PdF9ORkcoN02MVTv0anbi7lvw5fvtOPKNU0-ZRBouFAXtiJUy6o9brDuIM3-wBQcFWPZtZg7WGe7NfUGR_Ly5_g91jRikdfZkntK9NGZKwlmbxNqVRi9qgOL0HyJAKYMoDfzxybYW_z2KjWn5HdYgBlucleDrd-e29ARpdqs5ABm6lfPGlxaV6wqgamIrM5po2DysiqkZA1ZVHG4vldLi4pjsCGQ9x9bmTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWjnTWLXOnVdxGEKMo12xRMIUBvcc7dFL_62ktsUMfk9N8CNhW74a9y_Kuqz41Q-t8MZMCEvOKRH-gXHDun5WqrM_2EJVmUQ5Pq_yOjLuGjgLqleAXMl0xOIaP2bHuNbAoTPHsPUYZWMnDMiQd0YbsX90wAdG-HBrRy7rLG7G7XWO9RPyexzy2N4kbYGzTW1BStGBBMpXRFy-l3lOsQknZ3jCa_CKQjU8Quuo8SmgNU57sqvYg39Q1WcwkcZ7aJz4Fw0E_mZPE7ZVZkybi5wKQRTrtFkDcBr3PaaFQBMMy1cFTn_hcgBoGeLxPWAAsoE4S6zSDLS49fFsFUrjHPwzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gz1vV1eoBb4Xbufjq-MPX5oR2tGseLmqxGV4J7xzIF6yf-L0SMoCxiIWBh8lu3LD7yu36-utdbqW9om3mve5OqwwRFZJ0jfERwn1xFBmYV1HCMyH4UuVFfeuKWc5VH0j79LDiEjLg3v3ai9AcGJBfuQclMKhFZsc_ArDMX6nDF2vXv7d6_NkHNy-hVElglx3wNEGk1RZS5fvkrcR_rIaCoWZ87nILW0xND2dS2MOMdmC5gq4mJQzS_7Ob9AVVLk4a4pb66I6wyUg3zqgf7hZQ_MvirUadcUiIOhEBdV94IwuTbLegUUw5tdzMAcJki5nZDnO9Bq0mVf04DVQh_XOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkvMkzrQkVx4NRRm44YFDSP6FDkp9DFWg0_ngDioLFd6m-NR_uPQ1gD99EBvyyqNk_5LPsYEsT5cUfDOGg_JEJgBcNb7FRgdsCKELnx5iZo3yvd9u8BhvTB4YPOzBBUSyss7YeK9Au0VQHhPGcgX5f1uXRowq_-Pq64FhBDadRmlSa9a1LVNTQBYv3WecDTV50N4HnOnWQFvHanCdjJKxCZtnDP3zn5lxR9r0iyOX4keUpS9pygEpCO28v1Zk9t3ex-I2QvmUduvXKqzSHofAB69dBoXBLvgI5o8sMm0BRn0fjPMqoZYrvgGWqSU2ssmVlqE5MkxuDiGb1ulq8bO2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlAMvzM0r6GXn3Zd6ehI_fX1ck6WocDty1OOC4q4cxtdBffgZVaPStfkLelwL1V80xlsRCHPf9xCKLfFsLpstfKUQDJJq6EDfVbI1zQQv0OdvB5Y_D0tBxo_tGXCCGhqIvhXD9IduziKEq3NwGRAalWkOeuo_8h9te0dU6ZJvJkDdmAXazMzfP9tJLiUiXSrKZVkPhFeI7FoguZHTjkfpxbRT4Era2BkjowNPrnVhlDUl1q2Kr7Gm7jn9hPworqU7HV6KtrDFJd33BRjZsGru-CU11x2tx2yGfUNfqYagR2LaPhUNVGflt5g3PIVuOiz9Ox_8R3ONkey73bYDevbHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGvY90jxv2MoxxAHXCseS8wfNTaRAb_Tl8bhWhM3L9bxSeHvB-5e4nNXv5u-cPH21yFaoiSToeWeBDL1WBYYE2uP_9tNcu2OFZqcUtihq9j75boVZLkgcTSVbuTvwKvsNNQc2XGyrTg0sLgI_So__p_PmCTp9mL4F8umHl3PkVo3ZFhCFIFnIdvxZa6hmHK2xAvQ64KsEoHLqsJxoiYrWmvc0aBb8D1EZMoZXqdBhlITSpEDvkhFAz1EeuNRehN3kaiq7HnuSAGYn76LCSmjpmk_GP3oki33oIngsDxLBqw-zcj5cdepDqXtalA9yUdTbDlMG3SDO0Bp0mneRN_Low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW6aG9wFpHLe_w6iuxncvwJAPvxeXia4f90ZzTHzeombxnt-5goocqlCrqebhao9Dksf-hXoUR1N-0IOs_ekg7bjHQ7YUiF7S0muSOO8auGvTNwNbVWnA2HsGFp3mai3Yb6IpBMhfxubTrGJd3dikV33-JRtOnrEEnYXtKUmRiRw4ojw4xsbZnRKNLTFF6sNNIItsqClu7mJbno1upUVxsShpiZqsuEEygg1saiVAmq-QFa8sznbuhlbeTrpdD5JfjMC97iiD7kJ-omtEw6ejlFZeg1esXWC1apCq01cm1kUuiEssQ5AB_O5uNsPyDcEWlCTjpUfcQ0d1Fn2lXvihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYLq7_gFj_2Gc6dTuUYXQUchqhOz3pqJkfNcXJOAGp2p3sEh_iGfglRXx2DwFg5Y3mmFzlh4CI3e1GplLRLaECgg_BbN7UqbOCGFE3O17tdLTx8V5HihAO-W2lDDF8-9kjoWsQI5H_gnUSD64rnrlaC-Ty4JocSG-2KWMLjCd9sLxhzxes8BUa5KFp_IBsmbaLDcOO7Zlp0nrTypUtlJ2gm1b8Zw6ktOfdP7AbpCZ7yKraO8CeL3nG5mSrRDEpx906hElp7GG1-AUCYJi3koyy1NwGQWTyNRdDdQiASOP8uV3tb7EiZscGGV143bZt_aCi0jHXmlwVcn8VWeS2Bh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBE1UvQQHvqRF141lYcs1QcWyNgkZ4YLmU3Q3YjBMWUW5zg6BWjoH5cRQ8WA3Qdd5437Aqb_wZDrk9PjwMbyVMfxpa01whhe0FnfEvU0kfiPxIc_8qI4ZsJxU9t5aEXFKdQkqvzK28pL-ZwEK2S3rpMOzKgmPXbkBR6310wsT_X0vn_Xxn7h0evIffL_pDv4OK0lBKOiXbgAt-K6HflsnyiILfiMr51EGPQCUtbwlD5CX0WqVugioFH1-8C0wGi2w3ELgtNtog7EnK-HO70mehAZdtT0DQ0hy1K91B6fx3p2pKbR9rXrPAlAg15wdlbjPzOK2r--bQL8Eb9G9iaw9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r94wrBwGLS5_ubR8e4IlBAStqt0wK7aONX6P4QcaumbmQU9BRYXLSFFDy3F-Lmnri7FleyhReX3fGbIZqNadWryZk4rFDEmtYL80nn0e97pmWKvKAcgSkXagcGKhyg5xtlJHFaUL-McM3D79GGZARa39cADfBzkS_eiSPmOm4qbhk8OvJyyh4q1LVSVf8CjIBIxkec448D5jrzFCMyWQVpaWgKcr3itvoIgPGfSTIkVNN-V2Uys9GpIM6xRAsu3vbMUxnRZaGVj4WE36O4BxoeM33EjneMCgZqzMy3vSZsD4ghZlXm-xZBiaGwWJ1aMo9TnXc0TbIhO30KlzWGmuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=hrgqNKcspKATFJib_z9WW0BZcJAhES2kCNJ4kA9AL_JK6LnS7dzl5RQKfIt-cyvwER-0If0sRMEp3LCL-y0SWLPx2IQQoLXDNtXcv6bphQFiRgUA4UriwUbIhj77sOK8m5UizXf-wB6SXvz086XTPkctBDnOk0H4BDRPlFo7qkjXSWd8Lk4Ookti03EF5-bk4FQl9WdGsm0GdPNlnubFtqfN8bo4p5I4PGOG9gjGM1ixr3JPmnP4orrUKfM9pm8NDAkWDyMXZflgaHkB-ASv7qNAMNkgT9epaGbFrau9c5gnm4n17iiBAQya5BMdze2TiZhTVD-i7TlTbso0v4OI0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=hrgqNKcspKATFJib_z9WW0BZcJAhES2kCNJ4kA9AL_JK6LnS7dzl5RQKfIt-cyvwER-0If0sRMEp3LCL-y0SWLPx2IQQoLXDNtXcv6bphQFiRgUA4UriwUbIhj77sOK8m5UizXf-wB6SXvz086XTPkctBDnOk0H4BDRPlFo7qkjXSWd8Lk4Ookti03EF5-bk4FQl9WdGsm0GdPNlnubFtqfN8bo4p5I4PGOG9gjGM1ixr3JPmnP4orrUKfM9pm8NDAkWDyMXZflgaHkB-ASv7qNAMNkgT9epaGbFrau9c5gnm4n17iiBAQya5BMdze2TiZhTVD-i7TlTbso0v4OI0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyRnInVg86PDfB4tP6_UCM1qCUHPoOh5VwcqqmVbYzP0WFbIUxzjyxQwLvbCWrSTl-CMAYGTjW0YZoZwgd60bVKbNHaqyDrj-X1wNm9_4KsUiYevmBRSuX-3fWlaWD5aG-ZvT4cipbE5YeEcm8lEuKYj-BPgUx9DM-bzhJpDWd2EY5CWa38Gl8pXGgJ8U5OLH8CeEcoUKr2XfKwNGN-OZixF_XVtZS2CkPVcLTUFVSZxgfvOsv8hWpT8KGnyDxICYUJS4YMVxPLQ2v89sR8gShg-fwS_GXnlYlyB5M6prFOCySr-RwbJSALnvYG5NSm1oecrmJaGu9vSqsNR8X74eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=P-Y_avu-c4WaKt8TX7GkgapMrgdRdZIk25TpQzBgHpZIu0li7kWyGiwoKwqOsiym-2KYqvPw5guwUiTKPnvU3RkmRBgn2qFzIsaYceZ0_dbCP6Toy18Oz7YRjorgpA57VywIIK4xpol-_bXloIaqm0XgI6TW1-oIXVbRSlx9O_5ExXuQkZYGJsggeW8VmCf16es_b92TuPqbDwy6KgEyclNwk1LiTTOd6Yk9DFhSni05ih6QOOZb5RiDwf8Gg_5yqpn0Ri73AE5LYuQWKdGmQy60rDB97NEwMTJkMsDHi76tcEEjK6u6TalcpPtf9WJnn1DUCGRFHBv3FiZQHNKuPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=P-Y_avu-c4WaKt8TX7GkgapMrgdRdZIk25TpQzBgHpZIu0li7kWyGiwoKwqOsiym-2KYqvPw5guwUiTKPnvU3RkmRBgn2qFzIsaYceZ0_dbCP6Toy18Oz7YRjorgpA57VywIIK4xpol-_bXloIaqm0XgI6TW1-oIXVbRSlx9O_5ExXuQkZYGJsggeW8VmCf16es_b92TuPqbDwy6KgEyclNwk1LiTTOd6Yk9DFhSni05ih6QOOZb5RiDwf8Gg_5yqpn0Ri73AE5LYuQWKdGmQy60rDB97NEwMTJkMsDHi76tcEEjK6u6TalcpPtf9WJnn1DUCGRFHBv3FiZQHNKuPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=K1mfWBuu4g9mSByuFR9vQtF9uOyXqiW6eilCAw1DW3vPm_IdSoDme7f1RXvWlP9tITA7pei6g04RO5hSlJ2kLzoBTAxX4rYlfnCfu230buBbkQfuYkB7P-SbuVAIdxr3SU_u-RJ4C7KywFY2-b9wLOVS7ibA3OQ19Rsb3smx8Ets237Bd-Cltnghm9OcQ_SIcR0cTt34IrbvFiQlcdg6JwW83s4Y3Y_3Y2BOkDd7rXEhdy9dK8-G-6FqiDslJ88K3-M_pcXHp52j7nmI3k3uF7U_l8QV5lSQAO_JPhbG1e8O0-wuQhv8T_Fu34aLGbHphNTO1OHVTfmnes-I64LUgJuUqhu0zPEU-RXFhzfQK1JNyxNoC16XZ3k_owRWvwVgUwN0pveamJcSsErmOJTbppqwobYztQO9u-6BvdszjDjyziAiaKULEXExp08rxshAOa2Tkf7Yb4m48GxBJ-IDaDGsjj4KaOpgEVpcVQ0wWbccxA8RRQE6lczQuS2rRzU56VYYrJCN_WYfwyPQbpDPzXJIj4B0etS_0fGaNwfi6EAhdZ8ZFwK7EUybUsqaHGzf39_y-ODHPGP2OnrD_DetMFxUtWneTwrbkfTn111lj4Z6d4_2-XQVQQbQmQj2aTMuwJBlXm4USIFXty1c6tym2HHXUIEiWRJ-X1fuRN9pUIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=K1mfWBuu4g9mSByuFR9vQtF9uOyXqiW6eilCAw1DW3vPm_IdSoDme7f1RXvWlP9tITA7pei6g04RO5hSlJ2kLzoBTAxX4rYlfnCfu230buBbkQfuYkB7P-SbuVAIdxr3SU_u-RJ4C7KywFY2-b9wLOVS7ibA3OQ19Rsb3smx8Ets237Bd-Cltnghm9OcQ_SIcR0cTt34IrbvFiQlcdg6JwW83s4Y3Y_3Y2BOkDd7rXEhdy9dK8-G-6FqiDslJ88K3-M_pcXHp52j7nmI3k3uF7U_l8QV5lSQAO_JPhbG1e8O0-wuQhv8T_Fu34aLGbHphNTO1OHVTfmnes-I64LUgJuUqhu0zPEU-RXFhzfQK1JNyxNoC16XZ3k_owRWvwVgUwN0pveamJcSsErmOJTbppqwobYztQO9u-6BvdszjDjyziAiaKULEXExp08rxshAOa2Tkf7Yb4m48GxBJ-IDaDGsjj4KaOpgEVpcVQ0wWbccxA8RRQE6lczQuS2rRzU56VYYrJCN_WYfwyPQbpDPzXJIj4B0etS_0fGaNwfi6EAhdZ8ZFwK7EUybUsqaHGzf39_y-ODHPGP2OnrD_DetMFxUtWneTwrbkfTn111lj4Z6d4_2-XQVQQbQmQj2aTMuwJBlXm4USIFXty1c6tym2HHXUIEiWRJ-X1fuRN9pUIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=h0MkCcuT_zGXO83dlOHhE7wfkGvBV4_3v5HABynOGpUeX73qEnVLbJsleQLAsdz-931bKmxOoaWf9xOGokZjOTN7VfYE2O5EgNJC4n2aPlLGdy7iZvZyPUmk_UMQ2cM88VOGxfphyZvmm49eYI2G10oGnUjFSqjKrsu3S2hiM_QTaY61lXOpflsnGXgXyY3SOOoSR-miv-sLn_iEqcqDEkVmKIpDGYkg7NU0v4xWg2CLVD92rpEHUsd70jUCfXHRiLWZrqJSYh-3fi_d8GlwOhORPVZIL5wtHupCwF8pXWDyizt4CcNd6Gj0RyqDYZnT38XDoXNV_Jidy890cAuCuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=h0MkCcuT_zGXO83dlOHhE7wfkGvBV4_3v5HABynOGpUeX73qEnVLbJsleQLAsdz-931bKmxOoaWf9xOGokZjOTN7VfYE2O5EgNJC4n2aPlLGdy7iZvZyPUmk_UMQ2cM88VOGxfphyZvmm49eYI2G10oGnUjFSqjKrsu3S2hiM_QTaY61lXOpflsnGXgXyY3SOOoSR-miv-sLn_iEqcqDEkVmKIpDGYkg7NU0v4xWg2CLVD92rpEHUsd70jUCfXHRiLWZrqJSYh-3fi_d8GlwOhORPVZIL5wtHupCwF8pXWDyizt4CcNd6Gj0RyqDYZnT38XDoXNV_Jidy890cAuCuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=MTAi4u7rLPHGVE2uEh3XagcmsIp6VQLvwKn_plzxS5T5MBK1spSfV-V7YL_BqttO7QnYw-aqi5m2mKEOkjoRVXSm_7g2JMHTK3Oc7tC40t30_AShvsQLUbuG4iQM4KB_Rg0YpG3avdMV0j5q1CQHv_cAV-pp2SyVeUeJLsHxr0mIWxnmoHfgiauCoSliTiuzJB0hcz-C7Plj993oPpQ75zwhwBBqnHxf1q5GW_lWw1kBUpxBIsmwa6PCgwKOLp2yrANH8mAm9Y0mBe2r6GJjapGYY36T1TPxFEM1kUU2GyEr6pO5v2lClOr_nbJmSkRN3ciaxo1e4WD14x01oZRzCS9U28KzX0eYfci-CrgGFG8-x2cz18Ghz7PEa9AUudnRcPdpUUzdFmQam3a-d-jTkl-HmDBfksBQ3uhGSk09BnP-_VwXPVEz-eIwklOWORsDRBzcwfh-KMc-9Bxo-haZooNMJqRhVm_z3H2UI3hbpcIZvUXJZcDYIf3WaSUUJ4l7DWwu7DX5GxF_5D-0eiMIvQw4SqtpTPfq5T5MkP1KuKwAMW5ktUZf-_QXRDsgtodh6STgdBSHee7joQZLaoMtGFvae1M5dhHQXlmFuIlh7Rje2pTKfl9VhOBjYGs9fQsfcpfRFjSdruQnJCqh87jf-XQLSoFO1Y-PhsZEm6WGyCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=MTAi4u7rLPHGVE2uEh3XagcmsIp6VQLvwKn_plzxS5T5MBK1spSfV-V7YL_BqttO7QnYw-aqi5m2mKEOkjoRVXSm_7g2JMHTK3Oc7tC40t30_AShvsQLUbuG4iQM4KB_Rg0YpG3avdMV0j5q1CQHv_cAV-pp2SyVeUeJLsHxr0mIWxnmoHfgiauCoSliTiuzJB0hcz-C7Plj993oPpQ75zwhwBBqnHxf1q5GW_lWw1kBUpxBIsmwa6PCgwKOLp2yrANH8mAm9Y0mBe2r6GJjapGYY36T1TPxFEM1kUU2GyEr6pO5v2lClOr_nbJmSkRN3ciaxo1e4WD14x01oZRzCS9U28KzX0eYfci-CrgGFG8-x2cz18Ghz7PEa9AUudnRcPdpUUzdFmQam3a-d-jTkl-HmDBfksBQ3uhGSk09BnP-_VwXPVEz-eIwklOWORsDRBzcwfh-KMc-9Bxo-haZooNMJqRhVm_z3H2UI3hbpcIZvUXJZcDYIf3WaSUUJ4l7DWwu7DX5GxF_5D-0eiMIvQw4SqtpTPfq5T5MkP1KuKwAMW5ktUZf-_QXRDsgtodh6STgdBSHee7joQZLaoMtGFvae1M5dhHQXlmFuIlh7Rje2pTKfl9VhOBjYGs9fQsfcpfRFjSdruQnJCqh87jf-XQLSoFO1Y-PhsZEm6WGyCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuCcfqlI-wfwEq2udniugrd4RF6NEs1_9ucbZ-MAC2eQabbSS9pXneJoIXRHEbrFg4qshQPoRP7ZWZSHape8RR45c7SYSOaRy45Xo2J6EpVwuXdVxnlfRYdv7A4AWINEIIpmuS23GLVdtatF5K5lQmVq1FqWZQJnFVjwFpgr5p1ML-r9F_CiCdoGc_BZv7dl6Dcii8SvL_Gt0BQZCJE5RE9h-arZkYGDUNrYQnyYrt8ObCir6byMDYxeLyA6Y7vvLMMvDgP8q4vG-aEIcxTYVssw8IxmPrCmQ_48TLd2KNj00872QbSeRlDyeWSSRzgptzjWc3Llv-f-swndfeDUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=k_aQNTMPqh8P6KZ6C-BeZbx3_QgtaLuyc5g7EiJPjmvpztrxRvVUhhZycFffkryJx1jgzFemdsfKYaqRdpLWM1otxsxTrOhjTHwLALlKQEc1s1mqd5511S-y6NC0cYfN1HgXiN33O34ketWaEotuLgldn92ekJKYK5U8HQCIaK1l9eAHZ3Q-lMJ9HeBMjNGVeSAwVgmAC-P1yAV5kgCgKRSBpHgj4L2UFKnHYxkRgTvV5JeAV6NhmjM_3koQePgvDZ0SCpcs-owF15KictLDtPlZMjF40_93-wk3hQL3ScG5fXUBsQuP0xoFJwzceKH4b8mqEw0kBwa1FkJgrWh5jh_uls0QREbVL_dfGWt7bcmdoYqEdcpYQmYK9gO-MZmXXY5lEWMexcJ5WLc9luWmLvKyPH7n9CupTu-Dfvt61S0yi4NLsJbqKbkKlNEiG9yrZoC9c4P4EHcuJtlHUO1FVeHULlMJGOgVNP-uGfA0pwwf06-vnXfqyYEsa8BgyCNzwjUZn5CaPovw7xymXh8z9-imU9GBqxW_GKdlo85mqJW7F0ajEpJOfs2jeLw0HptlhkZgHb8GJn9e-XGRyzNHQ1zv1m0Gnt9QrJFyolNEq-CFfqHCLmb3PbExnFoxx6Ns3YjhR-6DJMRTq5NbshmCMy6kdTd_OES-beJZt_HKU1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=k_aQNTMPqh8P6KZ6C-BeZbx3_QgtaLuyc5g7EiJPjmvpztrxRvVUhhZycFffkryJx1jgzFemdsfKYaqRdpLWM1otxsxTrOhjTHwLALlKQEc1s1mqd5511S-y6NC0cYfN1HgXiN33O34ketWaEotuLgldn92ekJKYK5U8HQCIaK1l9eAHZ3Q-lMJ9HeBMjNGVeSAwVgmAC-P1yAV5kgCgKRSBpHgj4L2UFKnHYxkRgTvV5JeAV6NhmjM_3koQePgvDZ0SCpcs-owF15KictLDtPlZMjF40_93-wk3hQL3ScG5fXUBsQuP0xoFJwzceKH4b8mqEw0kBwa1FkJgrWh5jh_uls0QREbVL_dfGWt7bcmdoYqEdcpYQmYK9gO-MZmXXY5lEWMexcJ5WLc9luWmLvKyPH7n9CupTu-Dfvt61S0yi4NLsJbqKbkKlNEiG9yrZoC9c4P4EHcuJtlHUO1FVeHULlMJGOgVNP-uGfA0pwwf06-vnXfqyYEsa8BgyCNzwjUZn5CaPovw7xymXh8z9-imU9GBqxW_GKdlo85mqJW7F0ajEpJOfs2jeLw0HptlhkZgHb8GJn9e-XGRyzNHQ1zv1m0Gnt9QrJFyolNEq-CFfqHCLmb3PbExnFoxx6Ns3YjhR-6DJMRTq5NbshmCMy6kdTd_OES-beJZt_HKU1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rytN7baruJdMjm_ytiAf9expKSvLlndKlv_-SXPSFNpGj7GjhrWuZxfizWBitYwzcFmtzcUPsmFlKVvUo84Sc-Xc-n-BWXDh4bb4IPel4OMGZGZu5MazqnUGaLj2wDLyKgPPt7dTet8qSXBXm2YlsK5FEWeatWzTTOYY2PvljCYrhn0TlJTfoIH8QvF-0lsfm_Gobtrm_zSoc1FOt3ZMN_nLjKoEGNLcuMF62SVRyOaCptuH6cA0vNH60wRvXeJt8X-kRf4BDaz7YcZs7sVgv62P4Cz9d2UGaYCJYnUNvh_rU-Cr_j3L-FzjL-NjcgLou6W-tbP-BSjxCzjj07lKjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHQ1NmHjY_qCdY-BUmrNaIfb3j0cShZhX-AtGNCpvKFgbJzCPq-PBhr5D4tf0v8j6ZA8fwZrIXGPZslV9b5UgJql-H4UzSIXIzXps2tOFMnF0DPfUuzgTIEhAjgChn2LzxkST1iJwsKy1XpZinaObyHVkkI6sgEtsybxCrRvTPn5k-9U-JwbjmWg4_g73al16KyllN0ZW58T1zEKp0cfzySgrUsYo_DVrMjyaXygOZVbLschfCuxPBjrrGM8ewmo3sTTQvCgrs_a1FxqykSUJlxNfiH1gT6aOiatfxp72q4W7OLaWhpkBJlCNC6ODH0Rp3bK6mQb6KooFSqIRmgdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLTjlGn4qgh-tDxPZsAytGieg0bi5jwv19DOBZvfTjlRiRb3ed0v3sK990g3VUavMXUxdMSFQ4kPBp2CJRx49LUmZ-vSD9sn5o5qUsak5Y189b5rgtiIqRtOhtRZwQBqRoxLkM1thP0qdEwzlCavFf5uqgx4-Tn1HRddiF6IkWAlKj5t4Edadf-ZNuWMW6wGXOOUjrkwgzK37XgBU5clOy0yAJtqU9wItf9vfZA1xlelc6MV0Ja-cCNwdiYmDr_Wz3XqIHJgWlQXLbnTyx4Sjn9La3RFZc-leSSSGDUl-RPY5s3ELuOs6jw1QtjvG_wmngTJ_yUXkRX4fQK8HRTnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EA3aZa5cFm2gGO4AHVc11i47T4W5c-2Tk0uvhzHefwzi8t9aRjZ1EVhDtM0hXosOv2MNXCAyNO62duxFrf1vF7xZD5AwrDuDUKb9ZSr63L1BjEuv8DMwJhaRriTfPY46bnogUiTIG9CRxvXDnke8Xkhhwb5T5mWt7GgpupSDsMKqlcIA_hsAKuRdEOiIrzPEkgDFhJl6QT8aT4ui6DHwt8VETw3iB1yddL9rYz7p2QnbruuK62ghUE6JNSdnu06bJs4Z0T4eTVpsKCJvSfkHyyUGWWLxgbRBAVKFAysIow5zf56wJwSRwpwAZRvRq72ZD9zRQyZaaEmhT7RliaHrPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIgRt23HSG7FMBymAQ2cP7t8SobB_qB2uFyoZSSI1UCdqYvEwyJ72XNe8pQBQ4Wr-DxSzQmy3oU2L5m-ht6nc0fWi314GAncmpv0aAA1XGHZPvrvb6OO0tCp5YlCTDC2iJ4Amam9ZXHxt-AJuxf923UbEA-AoLaTAH-pEKY5D2MgORLLkryzEjEup_UUM9c7Tll9p9ogTNvgREOGRVg8bFcrf3_cAIL-QIQKkDNk3Wydsa1YS6rAdum6974Rq0-WEnKv8dnEZ2q-T0NzCKME0ciyD6WXvR7LmbPn9FZdYsOLDIFTe8HVl4mpdcSPaS2USx2fHXCOq1QuUwVBOfrNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdJ0o5KbSNXLHBTMzXpHbUd2gsHXuxO2RVwTqXVu3mgFAygTv8jv4xNKAhE2LAKotzuSaHkOJQJcUQnpkne8aVRfpfP-egwWFzMeg4JC3meTHwBZOtLOmY9te2qIhrVHUa6D9C0YSSsjfptsmC4usNkhJXTRKc2AJ-rYK5DKnUtBNGgJF8YXVzwYSB0Ey5Xo-Zt-MrHzR0XQMAAHiQAt7-1Wx642uQMKP6CKkvyRoX8sgOgNHea1VhSB3ZrceznihVJ05QTbzSBKuCXOiifjp0K99Cbg7g8e-sKhIUyPp5GzatCU6RyFKQzPDi1BqhIFnCdBBJ8N1jioRbrgSUAyVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke-zLjEb4RXosQbX8dYzrG23cPdcHRoDlWv6vur6J87SN_YlL77aIXh-ZmdtxQZvOtTcL9oYQ2oF3brTJyyA0wIiHhs6xihUa47cO364tM2ZJS0Qeb4otyeVO0mVnTliOW5ywMOeQT8X6qacgEgM1mETXeE0gOxKHQbHbUl0KXkG8IyfVt64FfRzyk4qYZ4ugh-tMPRbc6gMlxcRnRAUqcR6xxecFwOC4uNUUbJ2ia_p8fCU6DkEv2CnAV18cBnJEnEryj8Jcc7AN52iFM5wKv1T67BbX-gIWDTRtb1_Dvt07z4QxcdKt0z0J5I7PTDJVdCKG4cA5aos3PZElU4sRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxeDlDtgfW4ReSBtkPCt9IzLJFWyUP6520p83_4ipRD3toh_qkND90vPvOqup6xe0XjsXizDHIecIDaBpPjo6tuzFYxPTdADpmNRHiVM053SlWlIKAw7Af4__3pRHX76Xvf40LM_ZvsZsK6O9R833YSMqTiR3lS2yHzoUlwZ79uRwjjC_GE6Jsw3Xi06E51UGO18c6K2sRtqSVVd51jRxzRyvEFXPT5I6Hf1Q-3Q2S6ClZLf_pIy1r7q-o3q6Yw1Z3i4P8Tl-HSry6PkrRXNg-T4MXYEIUblln47KSd3w0XA66GJzRc9qJZb-OsZLGtaclDPJl-Gmtwm6AKhgrAsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLUKWR3QPgDJ76UvmDutPsvXiAwY4EK9oGDRJmf6BnlP-BnxtRJfC7z1qHH29e4M8zlUGIDGG0u7AwMnsXXy1P25AtnJTgcc9M0haJeDoUW3UZ4TlHsFvrT2hqfJBgZjfWrMKJ-hm9XvYycIRY22Sd7lNugBvcYz7_SB-JJ-o_ECt3vhZphnY3iXvDPTj-N4AjhsvkVAXOc7FFYJnzsTOkLdqusSeh1k7K63e1PGIgMwOLVLR97j4J7lGbjGZENFpNaH7TVu6yGb_WaemerzYGvWgxXcuKI8RNTLrxJijHlk0FH1gCvj6B1A5r0w4bA32Ff5JOiKXrAZ6OQ8Ni9f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzGlVHNxuL4DzfvO9-NM4oJxl24vDyLgjiki_KuT739A9A6zcYcdyJl9JAOPq47lacx82RFcVsQhjPo0jzxG7dSxqXiW_TWWi2QKN5ujCwOdlikwVSZoIAR02zBVXbl7urYUaiEsEA9cLjrJxj2o-SITyLP6IlMkHimGLUgPczeRKgS3Ihq8C0k_AY8mgXDmpz4UL8jb6ra_ypw4urrYgjewPSpOu0D_bmtUnCM4OnOp3IGfsnzGDLJj6Evj7H-QxTLb1ITxsn8xB0Gb5LqFx7FB6KEmGnp-EYBNFQlTRyldv_qmo3YnIA7Fdt3gLxP3RfFoMz-yUQjnkN2sFn2zmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSlQ2l-kUFOMC_o4l6CBSGfJSP-uIRnxpvBnS9ubYnuPrbCFdrQ5f2qCu3z6Im8BTBVUtQGEpO5iLSrOL22mfdiEbZGn2cd3OsZy7y0vzrwAIn0WNyE-eWsRW_0ziyvE-tKb6qfpuNZhINw_T2cKKWyhMX89V1AlrQu4vgP1zAC3wclCeJsayacOKrnKT30kmaiD5VJKlfpcLueqwBzAggdfAXHPVnsqgcNVwUgGrziTcmI1tMzZZebULk-dk-F1YG5lVuOvkba7Q7_YB5PRpLCiqYmAOtKXvx8Nu_JlqGts27YBf0QOE5-BXeYYLxYDZeX_6NFePgO2LKVcpPVC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPOZynby_xbOJsBI6tSZvM_UOeSTpXxdmiYG3_6PlVgl99cjzzvM6gXWozMfRneaW0YZUxDzG5CwN2kvvcFkYnCaskDfHou4ddITtBnZ7-QwguYoR76R_wX9wmqgxKXuLOh4b1A1elqLVic09LlowfXsM3CkqT_Q9mIOm0rFONrv3RZW7ugn4-7UOELIeNGphiVtFIQ72DHLsRLjYsJY1ADmtK0OgOGW6UoKTgcqZa6qK-n5f6-HWPixXo8QdqoNC8t_hsLyAdZR2Aa-zpe1KbiC5M2KscAzG9tOqKfDg2qd10r9b1Qt71X3iRI_St1eRQ2i6d1W0eXTTcNVbsC6YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm9UMn52sSJ7r--7n2CBX0XGmP9_5LiN2JhlI_7VTBUBHxoLnhmB8dO5Wp-AEFvnVlpQvmsN1OPOm7IQGTWHJvxOCgJVeGomMgIdHQwNV7EFP_-G7kKppal3L-9IGy1QAV_2knWB7x8-LJURxOge_krTupH2wNo4VRL5_dDCC_1OhYUmm3nxcnM_kl-hgymNU07Mo7EfphiWWwaNdPDN4K70rk1_SpJiG3TxCx7e0LrbsiuFcQE0KV1ukTd4FJk5z8eeD2yQgxjDRsmK47M7LmwxW00CNI3gaQpRNtG1r9mjCzH5UZ6fWVx8HAwgdZICYW0cAYt4humC6tFIWzPp3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXBU61mDu_h-rgyMLX8gwd-uAinMkOqLTmzshF5idLxUGUC9YHf76pMqOf7lMsreIvmt3NtCt5JshGqLTVV2KQKcbKbLvBhjfjiv2eY3C07EwBGc-gGqyQf6ihwr6H40tc597Heb7s1zpaqtIEeDLsBwLp2NlR8DJROu7-7V3rAyqTCOUSOcQPZRiSDxvGWBEsjhcIe3RFyhvCwiyXK43fnzk3cfCXh4l3Qew3jMTT0mbUNUNVHnVWCu_QgvUSRu5lDcxoSVVc0xW2VykkxmDAnNZvIuAcNCyFC2hRQ2oYGthEBrp5QcS938A8vX-vv6dZh1SPryLb1Bzc8SgpN1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzY_fOaPy51ADVeM5YSMWHRTUPQnkHZs5TnOyB_Ui3VEKU-JadcKc_o43H79p5DO48uojIAUaG5HDYpLeApqbEGdv9rSXBNUvvu_KvfkDNhkVZ_X8N7LwEmt9oxyHLNMP-d-U4_BdozmdGIaM5jSNGcEDkkkwmaQDGh48iYifpa_Rg_S5k-rigO7sRWEi1od6pa4q8VUB6z-_rze-QO13OfkBVN1ZD11m8KezwMIQkYkIuyJNvlp8i1tW8gXYUgx182ajUQFKx9c9E00YAht9JiftuY62GZQ_52o3apr3LMWLNwUnTAS0oeUDr_TYnFL3mBOSJ1SD6K65B3erc289A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVgxybVtBHRXJIAwAxuSXSmWPaIDjgLoeOwfEQ7f8befsTSkFYuTqFMCaUwdB0SSEg9abo4taS9LDw2HVbA1oYM0Cl10bHfxS9HpEnS3W4rYdP6U7yjoOH0rmu2u2qOwLXmJp4A4476Xby69RrAeS0FQd399YBwxFaU1QqdGHX6GGPVcACyNa9oEQpHU-l8h4vBKRcy7kZbx8QAgXWRXOPs__OAjUGD4Z0VHwRWa334GgnbcPr1DbPb6hfObswlSLek44ZFYEHsyjZdcwAtcq6UgN5JJv5pAWHB7sWGhGq32Ag9Nz6d9AP98KC1Led0Yc_cT-ZGTxswoHeZmalQemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=XjV0kvaYHxFZdndobA4MMeBqsduXzWDKdsFUIB9ybW2jqTEoC1K1tZQC7bPzSYci5ufeYfy_OYmlXFSH6VA6Zyg9Ix-E7wvWS1wP8O8i-CDdOoNQsJkqeTVvjU77QoJOsULtPMmNJWknwlsqhBx73MurIbgzZ3I7sTSzP_GOOJNpkeYsDeqM1KMCtreQaj8Xo4k7r_eVhVZCbBeedoW_16206xiygYwJqHrMbHh6SiJrg6yj89bCzLlTKwTvHSqj46CPEHBiuqKTi1dtTam6nif-oqULAXySVEeOvVEkhM3c7C2u9vAOrNFFWHXvRwAIz_CVz4Hn5RcqaLoGzxG-RjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=XjV0kvaYHxFZdndobA4MMeBqsduXzWDKdsFUIB9ybW2jqTEoC1K1tZQC7bPzSYci5ufeYfy_OYmlXFSH6VA6Zyg9Ix-E7wvWS1wP8O8i-CDdOoNQsJkqeTVvjU77QoJOsULtPMmNJWknwlsqhBx73MurIbgzZ3I7sTSzP_GOOJNpkeYsDeqM1KMCtreQaj8Xo4k7r_eVhVZCbBeedoW_16206xiygYwJqHrMbHh6SiJrg6yj89bCzLlTKwTvHSqj46CPEHBiuqKTi1dtTam6nif-oqULAXySVEeOvVEkhM3c7C2u9vAOrNFFWHXvRwAIz_CVz4Hn5RcqaLoGzxG-RjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVlNe1pNSkkaKu9ccn1JcA6al3Ga0j3c8Eq2vKVTQOfrICjgszTPaP8yuD2reskg6wurC4qb528EDkWhhSJr_1XhYzDLRMr38aWKptFYbldc17FGnK5CK4X-O73QLpzNtszIOGPH0bbNT534mRH6YOIgAF68NvzLnhb8Cd6ANkQXmZiTOc3N22HPm0EFEMxFGPc2l5KUVaqzWDRcIaLmGjZSBOujrlOk-CD21cxPYXXIREx4oD-nM9G59T405vUHNJZUsWE2s1gbPnKsy9w8LvDFdOMeMO7F0Z4Mpkvuqq-5K3if6CJ3wMw0cGwJsX_zaA5UNIE922Lbc6JrpxDGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXk4FLickIf0nSc2rCyXdhQz7aPeo-iYtNZO4XrRoFb_MV94e_bRYOVR5Fp0bfhWUw7TDN9VEmu7_HWlB0VUspI8CaXxHIQdQD5lHuCyh-FGa0xuKdAwMtHJw_4jA_sep78XXz6bDKETkyB4LkF3xBWYHl_I1i3oSerJ3Uw8qDKmK6bIkrR_eB0u8mkVfL1M6UgCR2nf3can7ltVuTkjOP1GVhe3dg-ED8r51V-Q73bqlR33lbeobqmgDacT-o8J76qqAVy1nD7bs7a8zn_OaPABoCm5Jn6UaQSh8neR7qPVnV1syofbuFWDoZJ9pgyyg7TJqcaiY4MvWb16lfYTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pc60pHx6mrNPMSB9ZBSeAHx81LuByQHFdDofGm7kI4sQrsB9gKbojL3iiELsr-jYhR-rgm4CDjM4Ws_e60w_xcdLVkRj2sWyUbrx6RyUFu4aESCqz-5UJc0dTUVwWL5cAB695OHYO7nPdnq3Qt4iPI0wbqzDnG0R9afCp9ZR8TWQwT9r-gGicD9gC8UJhJLIhVhV8SVBsS6rvtNX6O9co7YcwIHCHi8i0IE63ZxcxJUW9zcNdtdlN7mwUavzilZ3DOwvXIioq4_3eBiLaeI4vn0LG6na4JabKXpw2Uv3eDepRs6VwUkzvEm1G6gn7z9IxMuazlAriH966r5Eo-Aclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD-RNEJ3FdpfnrQZBVYt2ZbBUwYFmfj3vUA6GsMk0vhXBVu0pr8lVsLoK0xYaolMy1SyUR9nj5tXZtjJQpCTG-orMDmazElT_UetIbg36GqpNb7PMPek0WKVNmmNv3f6EPp9Wvtmkz-nxJ5wktz1OJiTZ9mMzuoZUyiTWVoKlEKSzIvlRz0OvD3RemnbfpjUQgMn-SD78vWb_BJISa6LAovAZqhkUmMx0AGK5xn8J6U44C-Pd2-oQUTXjI8lCJCgECVgtiJsbkVZYz7Er5aDjeDfLgoZUx17SNQ4qhXQhkFWMUG1N5at8OV-TkF1tFoKkKoyS7C31WQLOLYg-VVU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=cgEiO_ptYwFjlF6MURsIXtAdw9Tga9ZFVx6eeqDg6S3-QzzDudIqlz9NUTi1RlY12-DB1BupCIAGA2d_FSHmFlsrE0BSZjHH96hiAiT-4MkQyxv46SVCZvzjkUHuiVA7_Ce6FE4FwCgjjGODMnhaO6U6eimfVtIaYAOfXlg2zHKJNEsCHdDSLdyzRh3n_xNp1V7_JxB8J0DYsK7z6_s-n5a_P6HYiky8StQoaKukfAC1rMW_-xJM_-6RCQVM2oqBmNRjhht-xEI7r2PsUFSOaN7-2Samh6yz0lr5xtWpJCeL__x6EIXlXJDDNH3KYJR0Omaj38QkxYz0uhy7txSJWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=cgEiO_ptYwFjlF6MURsIXtAdw9Tga9ZFVx6eeqDg6S3-QzzDudIqlz9NUTi1RlY12-DB1BupCIAGA2d_FSHmFlsrE0BSZjHH96hiAiT-4MkQyxv46SVCZvzjkUHuiVA7_Ce6FE4FwCgjjGODMnhaO6U6eimfVtIaYAOfXlg2zHKJNEsCHdDSLdyzRh3n_xNp1V7_JxB8J0DYsK7z6_s-n5a_P6HYiky8StQoaKukfAC1rMW_-xJM_-6RCQVM2oqBmNRjhht-xEI7r2PsUFSOaN7-2Samh6yz0lr5xtWpJCeL__x6EIXlXJDDNH3KYJR0Omaj38QkxYz0uhy7txSJWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=V3MKznf4e99oHASZKQbBmQx38rDdbwM6g2tDyTj6gq_D8tdzcbpW-YWps7PDN-B9ouUZALyZbVXvwE8c217IaCYSS_7fcQv5uY1UVmSSvHJcUiTiaMiePav3CNq_-zZdmlvqQin_VwiGxGakTc2MKHt7hrhK0P5dICz2A9VXUIASQcdxz-I6aCFvz3CnAHV4juKU4Pu4VldP4yI32zLS7MOVqsRdGWvnyaM6Swu2MY3ru-d6IW1Se_IdeEfhrW598m0IhXQ5qcxRwH-6IaWTl-YxaKWzKeYojVPeAmbFddswvoFenZsT0UUJtGnFfGRHimopMl4yX7bGX5GdgohrSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=V3MKznf4e99oHASZKQbBmQx38rDdbwM6g2tDyTj6gq_D8tdzcbpW-YWps7PDN-B9ouUZALyZbVXvwE8c217IaCYSS_7fcQv5uY1UVmSSvHJcUiTiaMiePav3CNq_-zZdmlvqQin_VwiGxGakTc2MKHt7hrhK0P5dICz2A9VXUIASQcdxz-I6aCFvz3CnAHV4juKU4Pu4VldP4yI32zLS7MOVqsRdGWvnyaM6Swu2MY3ru-d6IW1Se_IdeEfhrW598m0IhXQ5qcxRwH-6IaWTl-YxaKWzKeYojVPeAmbFddswvoFenZsT0UUJtGnFfGRHimopMl4yX7bGX5GdgohrSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ItHJGZ63yAFxb1_hQTqUbM2S20a-egCQBUIP4GWzRzCL1i4Yj6ukA9MsqqjnZAn1HMYtqOJaWKpgWPBsuUcPqIKXcO27qJB0zBu86N6sm1CnC9T9VIJkw8VLra08rnXR9oEgfg22vGvMCO17T7JtvtuNs6lYvDS11VXHiv_oFmBz11unhy-6hPqKE2gPGFqIZfPpviivToBrITQtzUb_u6q-IA5mAd1SmOVospaD9bkJfEvTSOWe99mU2XVxO7NlS2uJFNIZ83u-deQK8wYzxWhePRrQen4Y4BjwoY6Km3Xqf93SEZJHateFRm8EWD-sMl496aX8Zrm2XHLChF8hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h77TDfN97S__GFFPFd5ylt5qjNNXijzklqu3Bq_72y0LRIKv9d224WNeXZm4mPzxkawIg0Vxy1Ymfm-iFRnNKGHfu6YfmZ1xjhkOF10fwlbqwE22WXvNhOWq2rBz5T_rGo12MBfDb8XWIzTpPpscywFbyf_Opi9KOVDpnpa_TBdIC08cQSxgu8OI627-3JJ6lFEOMgICaz0JATDapuez3d1FC_LRdajUwrPNswqhbb54gAiReESv-ctY7On_K8Q5r4266EWFogcyO24NjD3nGRt-ccPP5a4tvz_qUVfqtpNlbuSL9bfJmK6DWuT_JuxnI9rOOEG5z81JXci7FA8uuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCBqkvs98eqc7lXrz-uvMy6qu9z9pw7qVUmZKjIHNaiF6ZCmvfAdeRTjHBELKW6aV3RZDqLnQoKGpsSsEt_FNKBsTZhn9I_CCjWfEk5bS_mGDtY-xj_cepsUcCkQr0POFWAq4u0byewJi6HGWWKL54AVoD_It7fJPxfwUXUb0uRiFT2z8cwTcM_I_I3r14AzJfChaG1aJBbQ85l6S72j5Gc7MJoC-alnnMxPfy7Ebw_sbVdfrHgWiPrnNkLV-0iZFUB8XZcXTZOHlzQeDN0FHvWKZDHPCrMIG139Wyp9wfAAD5OKnJJoJu_96rXnbAuNFa3nKpmN5KCAh7iXTUeaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=oT8D4AySQ9haVvBVi-3mJpelbuYRZnD-oKE-Q7G0aRcecVGuC_KG-y-tevNeMssyZ2NXJbz6_yxxDCAk-8mg0ARrEGzKWlnwjNBfsYMl2cbiryQ2Foe8mvtL9oRSZV4olMbRrggT_FEIfsQPbUebMhLcjsVHleBt_ik1YuuO10LAUYdg1bjo8oLB-mWhZsPASbrwfBXPr2cBkP1za2lrU4y4wKxC9qzkRb7c8573Ug5pKm0khbQ9RJK2CCM3vL8tXzAPUwlvOk_52ait_bW8TQn1Rk5BsUzI3hOd8ZTcDvL_GJw9mE4dBnVJyUDIF-eZRRKrqCFZitGa-FI6RQpnCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=oT8D4AySQ9haVvBVi-3mJpelbuYRZnD-oKE-Q7G0aRcecVGuC_KG-y-tevNeMssyZ2NXJbz6_yxxDCAk-8mg0ARrEGzKWlnwjNBfsYMl2cbiryQ2Foe8mvtL9oRSZV4olMbRrggT_FEIfsQPbUebMhLcjsVHleBt_ik1YuuO10LAUYdg1bjo8oLB-mWhZsPASbrwfBXPr2cBkP1za2lrU4y4wKxC9qzkRb7c8573Ug5pKm0khbQ9RJK2CCM3vL8tXzAPUwlvOk_52ait_bW8TQn1Rk5BsUzI3hOd8ZTcDvL_GJw9mE4dBnVJyUDIF-eZRRKrqCFZitGa-FI6RQpnCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=QtJ-6svu9jm2O6erqFb5OzUMntR8q81xq_SkPwNEhdHoZBmL5nEoALrU7gOmRvqQ7P837YZcIy5VeXbEA_ehx6j6NLzEIw7GUxXTkGz14H_jOHC70fGdJogzKlcjhCXB5ZksL5x8uza3kkoYr3CA3BWLQrauz4ZhL1TQu6Nv3ERmPvMNZUUKNLAvtaHG7foZt0JqABxWHHdcAbX4lWshnSBLLuakLTTFVtFNBM0Sv-2MqhU15kIZc6D0FL2ebVbkzlc6CcE6vrm7dcKvNyYQfuKksi6HzDmv8bInN5rqWCyNObPjqnpTUhJh9opHDyYApxL_vp5JRkzm-i9Tl8BuRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=QtJ-6svu9jm2O6erqFb5OzUMntR8q81xq_SkPwNEhdHoZBmL5nEoALrU7gOmRvqQ7P837YZcIy5VeXbEA_ehx6j6NLzEIw7GUxXTkGz14H_jOHC70fGdJogzKlcjhCXB5ZksL5x8uza3kkoYr3CA3BWLQrauz4ZhL1TQu6Nv3ERmPvMNZUUKNLAvtaHG7foZt0JqABxWHHdcAbX4lWshnSBLLuakLTTFVtFNBM0Sv-2MqhU15kIZc6D0FL2ebVbkzlc6CcE6vrm7dcKvNyYQfuKksi6HzDmv8bInN5rqWCyNObPjqnpTUhJh9opHDyYApxL_vp5JRkzm-i9Tl8BuRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
