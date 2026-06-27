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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 20:29:13</div>
<hr>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUf_cmzLhvi-LfLU1vm63U24P0wzrkH-B7ybda6nxyK6EZ982RI3NWb5QjPzXz65nILDye0ObiFwnoEcwryXHFbm_2Hh-l-E1v8yuWj7VoOeTiE-H8KdV5qfqVKuUirZ0l80YBDTrHJ8kmx3qu_ySlsDbArsMqDS-E0gNoO1TIIf_cSC2oRvfD6L6CwOXJ_n1ViNvIAr_5OW-N2qtqvpFQbWnlW5FSzGeAal1w05qitCF-fqrs-1G0H2VXfb-R5xJ6Gtb0Jst3g2ngq-pkQVU2kJQplazPdsu8DoCP6f0T8Q2wAf8xD7bto68hrrpUzmnUHZRwe99x6OTOVuDYawSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf1fT1baBfZeBAaqurmo0eM0StgsZmlKGfoTXoK8JPswP8WiUMwlssOvMZp8EFz4WRnpfXiJlTILJPEBOxJIO746b0TVlGGGE7vGwbHLEK9dPrTospJva6MCa_m9rNG0uCAKDhuUjqmoi6TmEn3S7CIsjRVANye03pT67-ubxJSwzt6XWyv0rUBR2gncjI_HWeg4RbrA7EAsexnX-frZAOTshYR8TiuUc76L8YSGQOpvnhYXae5SH8vbDQ721mJ7WWe-swW7n_gK_6ahYgGtv-B0787NW6-f7zVl_5CBEnD7tzWToAh-r5qE4kRr5t7cXWRy76F0TCtBm6uLFZljow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlU--fywcKBQougDMHneCF8p1u9upW9z71z0NpI51l-Q1AKKJbYYj6AmtkfOQARua7IFaUN8xBBOrjKqS9krY_3lNYissD-isN8ne6X9bGOC0qRfxuSzqPZnCLcZE9szX4SjmptZXbX6ODQwOJLcLGN_pOeHfcAQIuQJ7O7arMisNYv4NLlsjedxaeZvSlRIZ0Ff7ei0jFjpaGxBL06JBbB9WQqDFDDzsfUVFEdYFTetG0EQ9QDk8XdMifPITKFAb7gMG6UFPcq-X__dre1yavqFS0QOavptwiRpiDoDjKyG6UD5SocWnd-OAduBVNrFTGyC936e1z-C2At8k4JDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0SGpEhvj3pA0QjvJPwWQtSdljBzk7o0mIgcNackYvZN_ANBNL0EiZZjMStPUmhl1vD5iWaK04KywXSI9KiQgdLJZLndo8mtMg774j4eUWlfq6xR44IPLIDfCtwNmTyx1jga4ewv3I4iCZy0gkkUfOHr0hSWQY0UD5kSn5KbG7ko-B2OwGobMWzNif47JRaIBhDOyCHHx4aNp9b_s17nr4daPnSLDXg8zPRJ1ZqQsYAFUbAhp0cSmQSzgJ_qsVxz02oGOZFISFbJoB84ZSMLnpzNB2aqdWuqb32vg_m3krA1ZSvL14RVCuFjGIr3cmeLYiQhYJuOBc7i1ehDXyed_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24471">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24471" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzddh3S9A0gKM9d_5xrvTtgPkOhFIhW0NqkuqckpUDx5oA3yCSEPa-O4xU-uM_jJDZvFKjX00pQ_PF5cq5JhA-nTaqazCLPuAqieV8RWPdavUYsyi2lL5MwL_tax_OjEJlTerGEQwYbrvgcioCHRpu4IRmL3T9VtDMpGoO01PpIVXxPED7GtD2VgLv3XtS81mt3OiawRZsUdSGbmnGIznNujeQqQAjECF0vI--9qu-K9DkLlPgXdlBM3MLmceT5HZAty5g31G2v6EIDrA_f6VcG9XulXlYg4QxPVe2KPE_neHp9TgoqHKotV28JudU-kvRjzoxHLUBTSEljC0lUtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTJPecoUXtUKZFl5nT0gP0Hr5Yi3GNSfXuOIM_onkA3mrYjGZxghDJTNt2jJNRG45QYlNATnVTQ_4o7OVhW5BAe8zvjWUW_OnWBd8JP2udf1VV73CLF_aL9jJPQSqCgpyo2NtRtUDjIwAkEZ7PohhGEwsfXhPYm0AHuKMVXzFkvcXA7rOtL5fEFCM0J1QFSdRXGE0aROjDe9vo35J7yeaxIHKRjKuZI7La8moL3LkONYXSxvWTRPGcCKZWAndSX17g6R0IMCRavVS_0VL9SgMSZNkpRPkIGUv4-QMlXudaMWkj1OdmY7ApgUIRVMPhpOFWfI7UXvUH6UCzwwYHA-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbnnzt24GrTjoQjNMmcP-AAzOvgGfvU4zUeRcBsKlNdm7BrxToj5kfV7REotrF_W3_Nysd2TtqYDg9fOyTTeOTkPLBe6udTfsxDVtF9vpoI-n8m4p5j-UKJd-ZGTgR9IpD1WTrCUxxBXtxmU4vx3Lsu2VwRgSDJaHREkWkSZfvpj3czoLTm15aIe4xWOrPvEW8aDcIHB7GmFrRjrG2kOHbokg-x53NC6S5xhpz9UNV1dxvtn0aD0xtgocQLCsw8IaX2oI8BBXEwrd13tNLmnAmK5-jQRPIiLV4eWzDwAsqGA4y9Eu5fXYBOyAHkwoJAJKxPuNoyeUreSTtT5RvBjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsGMifHXJV_0ZrtRNJ3rbkAmZr-ngSeE1zOuxU6vfNOkW-cV1L8hzjqf5rPBGwb1I1Kg4B_JjC1qoms47XPbNjhWsN2qYaPIKJvO0ClmpinhSWxlDlZtNz7zzmzWxG8wotI2kwcdNvJkO1zbOhw1nqu_hNkPbUbQrqRS2Cp7z4p8H8Nq6Uai96T_W1yqhmP-T3viTkFWQRQ6xVcEXoOv_Xlv0CSLw6h3UE3ZFDJWOG1nAEjUQo2EQmEvi4q2LgJxrFHEU6F8hujtwSfa7OYXmYpxjN5kS-c_pdH1EHVqGe0Q5jr0rlLZW73GClosOgXoEeyvSphlMbF4e0H4l_Qfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7vx4BE_YWhYp-qqyioLFeqUj8GgJCHUy_YzzeyIdlxCl3ZsQEV7kMmCvlU-K-XEcszK6uiWeAdEVQ50SZFZ8Op7L-NZmOp2pOQvYSFd7RytCABrnmpJjHXskgXj6NTlcxeU6Up9moMsLme2tJDn2qJ23L7-x6dImAl-cTR-H69wGspkiwrS43T9L20EYvogwCTN2j9Rb1ylInsvN22EN4j5YvVAg3imdOZqqbbWHTtCeI0rkQXniQUme5F5P2z-hmpT7NbAnIzwOMIlN8yIxcZAiQCIWCKEeM_uwRQM6lD3baFHYAqer08ZEvFO0C-fgchhbIzUUWh0RJ_AS8HA1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKk7FD0gwumuwarwtXGYgoh-OyNcOKDM8CVOzSJDGtIqzSnznYLTVgNrbfAIcapfBSHqiQi35ojy1ZiSEy3IgwF-WMJdBaLtdHlw1IMysazewyfqibwOY0UGK8jsh8kXKmZmkwBVn-6cEUSTlByqtDtNcedPmkO_OmIfWq5d74jH6QQzmkI2cvT2lBl9e2hkfU-3ung5oIWuKbfccGnVQSC-ngi6ASblBZXwT1t76rEi3P92hjPv-uCR4GJvSqDjrwSvo2fRfnPCeNdsdWBVn0GuMgVwhu0FEmhCb6Jp_E7YkcYu2YUhghYtck3G20Nvqai5d8AbULWV3tB-UOfB2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZhQR8zLAb06zPZjceI6rn8cGlFMcY-LZLJPltvns64eMiLa6cZOySGqzhnpcVOIazMSexACUAzWV2ZWdoKqMkxxXVWUlFUUNH3v1fy-nlZqZUYPd9wN9rnhlyuz32sKPJtRo13ZUnEeg0NIQ2NSLoY3jhCR4qHuATqxjJo0icH_YoBgpsXv4OZ_Wly7TAtdsy5EPTEdGa3Yl3FKxCBxrR7bA5c8T8khcIH0-lkkYDabrZfvLsOC5AauDWRmA8fzDziE2J9WLx7tTcr36JaV--P-JdYrbGYpdEV5szLCCBz1Iv3iK8caxnb_0o3pJiob2KIkx13_0UQ17YecLuxRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNTX46FQeGlwsJtCe-1cxbVYYqrDvHmc3yjZe87upnD-_IKDz2SGhP4QucuhxOlBXklAEk3EqxDX-2svTlJU0cOmMK1zhRKBCaPb4JgkbNWH-OmVGRPYbXuUinbCayZeUCnK8bVC_K4nLepn7LvTenlOkfkDAXYwjCv7N7CeMRbYU5lJDcBv2I7xqio9q-a0IF6xfgithKiklkPQxbFGBYU8SSp-sySonC4RZfdrOaRTrsZR8Jhh599zcnVjb-YfpkmUONpFHgK803u3B85Ll7zbjHdfpsgPqYEkrytbaRoduYclDvCpHhxA25BSdxH9F2zEjG_I2020TpQK40pc4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVr-5_FidoL4XTdfSURIEHAXtTbSbYGj8vYv6t_GoZp_7gMwTQJXVYiPSxEZcbrq-jbhENGZIy5hf8G20fG0gPC2KcwcVDcdMMErpgeBkLvAZkIFJMRZCaC8noID7lGl4F2Bplws1M2Suq4w-WpBbrLKKQ2k2eePiAEsB4KrYIdSkMJp7mgDIk5t6WHg-3VM5yH3-0ekTfmH9o_W081bKKjVoaJR2yb6bf_hRgUnkOm8V2PpEEoSQsDoXtf0p4VvBaKEh--QUJ7Gf4jkpWB0_3GEOr6eADylQDzJaUFAYLkq7mrFFAoJOnPf7OXkl5Fp6o1p6Pr_A4G6lHqnf2833g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l41HJhKF6LnPSmcNwFJ0-rOUKYZeABfHDFoJU0PB_j7rtVEV3v0LOsO4i8QKgXh7w1UEf7iMsh0dkvRU-xxkT8roY7kNQTMtRCOji51F6qpPXjz8b2-5cjI4Q3whTGaaGnRIc0uq15nzmwTj4Feh64ALoDvwIjNMngYBL46X68FhbhanNC7A__jMMxwlFOPJJTzMaphNBv2MzTWOM1MreHMSk5j7vWLBWUfv5qAmq2j07rho0EsH29QIRpXCn3f_QvTaPSjFeiWenM9sc6v8yynv1FxrcYzzXMqUZwPhF3WUipJEx9q6hTVY1Q-1lh0yKi5Gm_pDs9iRCyQrVqZy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVsEgcskMcZjVj4q8HerJRkiras4qcDmPj9NS5Wuxl4XtF1ntM7LskFvl7VzCoGnLm9OyPyl85igB6qjwfWfgxnSOCdIDz9d1wK7NDMVi5zZdGDq-B99lTGA3UXcBadsSbjnyMEm1xqudoLOV9UvSE4NxyNp02ZGWPqHYQ3lny7UmvWcFpSPGYZ6DlCkxK7cpY9tKbPQ-3IkJ9Z482kenuXrfK1XMRlDsM-q2ZdDij0asSKIy51v-cGtg4P7Ihf5oZnieZzKAKmWDhNbwCOSGiBZt5_Xd2xP8ouToYQwM86PSpAKJ2B31mi8VeLIiPFfcuTQw6WfaWe0W01fmzGPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKotvAyThv_HllSAbqttsMMmp-72c1rYtbO3eKRQAetFET1urGJyJ3z5s1zbx0CtdApNmtMYYXGOrsK7DbJUU7QCsqwQCFk-qi5xi8DFbyDmagO-R75h1-Ww8OcH0oad0dZQfJzTQzTuZs4QepweFIbIG55uMjHaXF1rbBGZyAcXNkyYbqFC-EgOkk_oOBpfgmGrOwA0gy2xypcX-0U7_yvtWPPOJL3vg2GhOGHHNdT1SsgiOOXfdi4YBFy6cNdEo94cfsMZZkdpTu4R5k4SFoHHAekWLOre1K7EwKjWBQmUnpUHnuf9nRMN9LzkxdkrSEjrB05lhOIMV0WgVMDUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR9mMzi5qSaLMF9PdUiTmG2xTlr02eF5B7kbAd7v_XtQQDGFCtYlRd2EPz_KKSj9cC2oZZth7PnxvbVpQmq6hE5I9bifZCDPEQIbhuAxvgC5OKsVAaDQS-pPmuwjPZux_rc8NR1sxMwvLVzxteuKtCUlfLrRnRuef-l4xOM0ScSoWRx9Xvfb7P3WXjX0Eu3baH4x7nJYF_-OzogmCbCbgZ47oPmOlAJqNIOvIJ0bHaCNKBmBMudIL-LDLWALk0TjHoG4wakxxw_Ehf27x962ImXTqpmzPnZFZ-lL2kKHvnebMOOaNgElLVmRChhoDLU2e36msKycDuoLkugad64REg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GciaDBWBF8yKnGLqJ0LEDxlHCMu228rqShXe6QDcvos5CIXZEzHnIPhaVdoxk5v3DywkYpEqPXZGq_2QXWHSzBsZWdjL6u0v2Ie4EcGH1gJGOl2vYWQ0OspvGEPJvOUdt5MMLToQPGl5FGB5U3Yq0otx2sA_3cdZu95h6tRk4E7jhAJEJ3s3PRcVI8xdNDayBQwhV6Yjcbmp-Ad6bR45kpCN1t1gOd5zYh3cdwKUETqQ83t85dR1KyEgR9-uJEfwjA36u1IWMtr-sBn5TVIaqUmy1GJONHQVBf1-_sY_MJ3ViuV38_-UfILweKAiFg5psaDdvskhB-dJGXbPVfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvd_VYhXptc6rOMRBFaERu_fG2iTvM7R1mFSGNDrt1ttj7yGai7mPoS62P6k2qz1swxBUPTkiCVvoSiUeE7nZe1StlK_b-JMJH0aNbLhcLm0PnDJQZDiVEYl2ToR5BZSw6dQUd9p275fTlT6w8snfz1E9a4008s0Y9j8dI9C87xdrRZRg9oboTgn5XJx8seVjFvEeqlMH93Ugsk5TeRjzf8qyq46fvWvXVA7fLXDTkXjczz9rC54maXVc0r_AVWQzmzbGR__ThNa01EDBibsHZb79H_LpQBZCLzxqqj3RP0XMqJPWyT_GVFyRU5ZpWg0-Vi7Hatr_cQYoI8hXNr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12f2BdpS4D4FkCGuYkAIfXHRJC9WUdjZKHfM1OjuenfhIFNf72freQns5J31A53MrKpTLr8ZIMH8aUEsy6nqH8uBLLNsOPAVOPPpOuCGrRYuP2ik9622Xv6rrOMH2Ei4c2KwKAEjpCIWHN6WWVub7zAPGmChcUQZ3XzUFvTDENKFcyrPlM1BIEIxrnRXc0mbrDuhTnDIqYpCrxIJl19tKVATRLzNyxsjO1ZLsfdw5yoYGflEAeMqmuzSTayNpJZKfPfoWBFtoZS6V_jkld-x8nbRXOm_t4wKaRNZSJeiw9_bv8pgtTb8NFLSeqbT9DTepXb1s2pB-s5HeMMcrGlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3E-Kdeu0E2Q-6-Kem5by-oYJkpfHjSG-LJaer3-APo-SlW49Y5Jr1mawNFKcYjsXHSMz69a-nPs78uAdQL9wQ8paLsVobxtWsgXKLCJtpLviInOEQVZ05dBnuuBta13jarnmPo9YoySDLHF052EMIXYxRgahIg2sE2XOVedzXrqKY1eghzbtxY4JBMBTdYWrNXDBQIbyfdZJE2EAlQcFyMwD8uyosyFD4GR0tFiEMvpNSgjHlFJ8MWuLv0p7KZkmEyNAeSWC809CN25y5D-EHl0UY9Ge_i3Kz3LSw566NMlsQ7B_4hH9ObSlERQX5JkcvgydPARSltdxdvVPcJCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ_5g2ixKZw4-8x-XIv7RGdxWZNLdD7lMBzIzCuVC-jv8GR4Z0nOxqK-09vzgrGVOgdVdGfLbnE0cknKEfZEXMdG2wyKtSwY7ZEAufXeSleMweQdnWMk2bpCe33dHFnBWuJ6Rq72UqkAidw0-XF3LfIujQ1cHTVv73M8K2ULQwRt0AlE5usAGtvl3D63gtyTW9yEMuZ96bSs9wIHFjBl91KjOg-pktXxVDMpEfs4l4dfE1f6POUMaUdeLsKmarDiAdVeX5Y5zvj2ahTWssB9oCiTuZ-W4laxuwNlFIqKHSQVJ8NBcLxhGmkPXbVkyodqAlcmhKO8658BqvpTf8nmLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVVDoaQPmRqRtN06sfGihaNh7m2gFjpB5opUMKBS1v6UkUclVDj2JI9-NzjRWDuUN6vf8qHwW0fpGVJtizpZET1LnXAoIFRtxKRMpokHmMft9sfeamZ58HU-7q8zcI04HuWjy0JTcPlHhgCQGLgnA-1VN-yKxaBvr074Grn4HiJ1FQgg5E7IAvqXVlKYWosFnLXQqP1si6twxTfJgmdJlL8Ex_aro6ntogBUZc_SCymRv34fQ1J5TArGhEUZrKoW3b3C8U4BuT7X1HZLvhC1BKPd2U1hw2X41b80n3ATy3GgqM4WcqTZGU9MfMVkugXKXAQRWMxlgD2cE52Mtsd3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O46wgAR0xW0vzSvVLUdJEaAnJPEnEgku6uhFYuE9uGn79smareeFeVPKh159rboZH-bAmJNxPUPK1ZV-ixMZClrbzIojxmeQPlDFPNQ-2JuIU-uD6yfBQAb9L8qTUr3LD9fVuZVrVoqfctxv3sojVSxdotrG6AG6lJyUjfEyoNP0IYOr4wN_V5DvYjCRg4-qHjAeqWJQAOeT5MgRHBrUNkaobysT5-w6_8h9Smf9_SqgV2ThQa43N0ZI45wkhRC-iZcR3FXbOavZgwuZwh-l2TNxIamaApjRN_i_7YaGMNiuJRgAIEcsiCug0qGLexe5vOCI6ys-V3g84qkNxVPpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJ3CSipW_5EQwYSTHwdEth6X3MVlP2s_vdy6_cLXH1mKf0pB2rbzfTUyzaXkaiMYZ9LEo67edTfFSa7etk34KiolLNHEpss6dYibjKDvuwNeI3QNUA7wyf-hYvtIUQgRgAXeIoJpFN5daL2i84iFPxs5J9Cs3rjfUShHBAToU8bMPZT7UXQnsDR7vyQzCsGhZ6Zafsut5BWQE80rF7lN4IW_T9NDfM_bx9g0rzrRO9CsdOWfmD71HyNRJLxZhdGvldWCaFkZBTHbO-QgdMeivtbmBc3ckGKPbBBjkEWjfAYBJE9rWGp-Rn5aXvFh5MD9fMm8rUrJBhs793ZN0uRyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ceWgYAl_FH6_5utkCLCi8drLcC-3sLuiQeC6KZAAYcXavAAgt0riJet1v-QWTqFCXY5lJSeVlcy6qMcqN6PtyvkNIyuWk3DKXHTmAVPtGUSBi47sC-nYW_6mKNeW9NkKbDS8oZDH4lYJcmhRVRIornX6B_JVijvKJwXF8Hg3y745vj5MzqC6QlN08FNRNqQAQx9QhUchBh1dLyssX5yejMVvXdDGwZ4BO1FY1S0NLkwCoiRABEUVpLVVsTIQUtWTGzWQv_Pa7LJSyDurQE1wLW87H0ODuGSq1oQalEgikO_TKJjTlC_9jwYDTt4hLmZWjBInah5E2tpF6ecDSu0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewyrcWge_7hvfETEIZg29KgBqMPdQ3f0rjjfFCC7ymHd-np-sN8EVRcQgp635fqJvGSMmPm_xLSJC-enweLui_B0KrgR_w8oBhJD4Ce_XK7tSqmDTV_Y4pqRRMg_GbMi1khVtEKIOz14LH_5wuHxQqOhlWGe7zn3dakpMNa_46RdWeksxLdfUsCSp62W46LPO1RJfUP8qy7TYUbrdPNTVBgIeoUsUSIEPXi9eT8oEZHxYtvK0aZzIvE_2PXMM5m0i8V7eagdDyWBblsqUZO9OXCYjIskWqvzu6rnwornQnaby3O90_uWExgoJRakNgTmctAl2tKYYDnnCUdMulBr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbNXvKSMndwdFnkJJiBqDpOLZX0fcXuogjMxaSHl547gQWkycyWfra8VLF7WAm1er62BOWC144Eiq505rQ0Bt2jrAi_RLdPfBEtdsCWQ-DWLJoH_9Kl7vnpwcCPIPP-WTw1RYAE6ok8SzrLvSZOf3-Uw9xHNBu96c64jGI2MQFbJOqPsH2YjU6CopqBrrSwH6l2e43O4UAJK_vqvSbClBl-EVJJ_2eru_RjVyUFDbcYb1dq0ushBqx2dOHy6T__BdQAgVfS6iLNOJogK61sfIq3kL3BumNpPioJrsBXt0PcUzzkSLvFV_hyVuL0K6MvhyT5hXrtUMn87lR31l0o0dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vn4vDyux5gVvwL13rfoLZPO9ZXL9X4s9v0RO65SbUj9FglX23ewFPCSR2sjjO5xOnBTi83AaefWIHu5lz3uk_LRa2IE10cBbQ__RUKmsYZNrINWL6j0Jg1xh3wQCIAMttX6uQObHrceXxST6QuWAUsQFZo4LPUdvjSbUyYvLLVtp3SAHcNVJ__Kesc5ipzxOFCGzx8yMSZKu8H_qNsokInVbHEBPzqNyeaXXkmYF4lSHOIbq8PdD1Ra0_GHSm_BJVy14GrZtol1ymrgKQuiuITOochDCJdDQtBBDxcsPqarH1S9b6TFHs-FWRhcGnvU2_TpzyGHpk7TUXMoVUXZ2Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Exgvtv8C0U25Q4G205F_sOnNUBdZzcQnfSoRUPEGCQ1KMc8dOM4_jMsYIGP5yyhotUcP1-uZapOJ_A9USjuKBPubF2pwN7qOLXdoyfL6ga9GatQNONy9AM3LcALlYLChbCqLBFS9-B6zNmuLaaPWAbvmBRTh6mr6vrGXzsn9j5xU_r2oI3pyNlywjrYewHFn_o2_NjA6Eh4CFqftaY8FkTSvsTwNhxb8bI2ciUW6rYElNF_aEmb0IIj5OcX816XF850P5obx2FeFRBB2hSOXKaFkLMyUB4uQbGV315tD4wl8he3-ZisiTsifpWHuXtf-CQ6BTB1wrH6dgawp3jTvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjTH4lAS_MZm1ghiMkdw8DKjiWiJVXQ-RnAWYEZ3fn4D0O78WfFUhFHk4A-DEVua70gdD7La9hEhaRV8drZmHjN9U8FoU8zmg36dSL4ToAl6WmjrmSR-zoRFJbJxGUfwuR4SoHXiklBMDkrKOdknJDTJgProBS25jTpkgJV7vrTNH9ZuxZGO8qgyJiOX4LeWciYskw_fI3j_5pcBYENIwsNCGrUH2qnNDLj6rwG8u2WEfXyc7nSjYnvySAi_96KuUQsWh6vSWrdlRxQyjSru2ZqUUta-c3BZ0y5EhEhuYuimdy7xrQEfleFQyz7-x3LFrKdvkFx6dsF7Lo52dSlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-1Q6GaMmRaShQT3Z14BE8hzXJwN3dvvc9VC5hwCaxEXTQdUzJo_d0yve5DODwWOOCnZypbiYYhfEXNo8LYj2g8Fe-uk5CdU3H_jEl2OZm-K2dBFsZA-vB3wim3e5SZzxGuxkaV5PRRgsElR0JurpvnDv_wBz889_guxosrKwJF12iTHrmV_mfx3BJ0m0rv9qhu5LpcNhJbySO636V7PnDa-sBkphqZH6TMNVhrJEs1Ig-jLbrTW_JSwFghvqKBiOp8ppiGYKclk9yOujYc_ld0dwNUWFR47DxxNYbmlgWnDONYBRt4jjnakAY7Fqdu2xSazehBss7nC_8taXY0hbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjyW20CH_9k6oYDIG4npGhj4H5m39dsPS6TEKeXtlaDg3AmNn2c_ODBI322PhayjXV_hi_8RyM5VIb1yp9rssdIcXtA_nS6KbcpB1L6ncl7lvLUkkujBfCCl-UocchSCo6TaBgzc08WOUTshD1Ndr0bGFKvc72Wz5g-M9KamWbSAgRh5DpUpAs-WHhhStPvhb1oUhwL0OktcdG7k1B-Iweht_m5roPg_F90_ebVBowDR5HrGre1WWA3pd4E4KofQmwe5Zv9KazZni9NOuMYNNCsh6WeVUZTUTwx5JNfXFd_b7RRTglMDAYPPx1JgoBP6fvBUmGiIoLsMCkL3PdBv5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8RLyOLzCktzjK8oqEnNtXdjXVe1UnRd7XKc5avgnBJCZ0LcaAsX5mWxiejsHr-KXFweBgdFXum0AyMGbSjbwpgCMz1PuxZqw6SJ9Jnd3nsazPGl3XAO6ql8wA_EC8Ab5EDov15kQ5SP4_q0wdfM8CMy5Lo5QrUGmVL-jGORiE5HInZsD7Xr_Y_3_NXCExDX7O3gqSEveIRH5Qd7Pfi9BEKJPUPWp6NbG06pjWakhSA_8R-JpPqCnHSz6nFpM3Eyghb93QI_zaM6kRv_S5ei6EeGD9mzKyRY1JiD4NkUvsnG7xie4BJKKONfLgf5pnzB2k9k5ZYAvAnH0EmeMT8KVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ9-el9gZLjteZigJAGb8mF2bZl4-EN2soCz6qUZX7tCD8QlpfI95_uIN6RAckF9cBYen5COc66y8dN3u6-FwAd9KVhNZ7UzZsDEQORbzXcHlpJOSnqYbV4ctjx1IBgwRbkGL-OhjuRN4VFYSdXIy84BnecbfiMitEyVhhuE8kX1nw-lXR7G4jkAMWMlwNUH8b74X9oxq6aGzzKvPKvdr4-w7Dld0bIOV4Ho-sMYF_rB6apF_t59mpAxB2H0oBwHY-YGtUq6BC5vg-a63ve4vVP3EgTv7oeRl1ozJ5Rz18-_ypnpr5Dj0f0iZoUq6vKHKkI80UazEZPH84GcTUZZmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=cXvVbjkY1ex4MOP6qKcc8-DdtRB2gQviqtAxYw_Df1cwcsTirr09MqxB3BG7SP0tgNLmuaB7urhwr7yt5L8zhL_QyNj2tiP78Jykslt3-tSIKxskjNQvgOqqISaomOhDjaqLcIEbxhYciFSl07YYlutXXEm9zrhQtSFK5EJwDq6xkVEYQYITHn1DrUxl6uZOJvkd4X4ZWWG7W1Wp6Tx43Yxl8-aVgnO8tjgHkdJx5adCVhUmkP7hau6q7QUfpjvp_R7Mitq0PFd3g8KzGFdq7qnQajKg-8g_uucWQV0xEiyhKLLSTQZDlqZekna-qdlAKjUUEdlnsP1hZEEsSNrLYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=cXvVbjkY1ex4MOP6qKcc8-DdtRB2gQviqtAxYw_Df1cwcsTirr09MqxB3BG7SP0tgNLmuaB7urhwr7yt5L8zhL_QyNj2tiP78Jykslt3-tSIKxskjNQvgOqqISaomOhDjaqLcIEbxhYciFSl07YYlutXXEm9zrhQtSFK5EJwDq6xkVEYQYITHn1DrUxl6uZOJvkd4X4ZWWG7W1Wp6Tx43Yxl8-aVgnO8tjgHkdJx5adCVhUmkP7hau6q7QUfpjvp_R7Mitq0PFd3g8KzGFdq7qnQajKg-8g_uucWQV0xEiyhKLLSTQZDlqZekna-qdlAKjUUEdlnsP1hZEEsSNrLYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKRvqFU5Us4hoiCR6-hh83E4d03idk81CshF4PR9xuVdDGkE1UpdL-Y9-y4PVqPQn6o7lsKyJypQPJS5cwX7FY9rQYUEbaUGI5vqQUacZToZIRpwTt2QRHpIKNkizcWIyfMyAr74bdkhTj9Afcq3l5l1JmelkYsfY6Dl7KHSUZIwDTwxbxPsPx7TC1MtAD_cbv6KkcEwexYT9LT6pd_FWFxh4xudDXdzHh8giTBOTj8NHnQlnA1-aaMHhcjElh-vYAdQb7D6T5HtT6aZKtd7NXX9QG-YjMExl708n7GEjazj-2EyuWow4LD9XVcwqyxYPbYmoExlPPY6ieOJOiBrFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUFDRTJ1UqqDiU0Jhz6A-NGGpnyoBhNdiiA7sEkKQ3kw9MXdbP_yAbxSEZVm35cIrP9V32dUoHjDqoJbDJUJGrBghf-DDLQ94v6RZtyOuyVNWmIxK_JaI_rw0dbtpJcmBE_xtIPj3B8WTTEIA_irPDv3qsGAJ7GitttQHogqweL_MBY_InEOMEWbv3Eugxn48O-hKXnnLt6eRFZgBwJ0ZN9v6PGqZw_CkEl8X0Emv0deKHS0MkJ4mwpYewEzoewoPRFVPrdB783AHjgtjm_Tg8P0cL5-qbNc-L_TDDRGJKFemkmPYz81A_3F-ebHoD3tBnLtDb2W4c-I_1h1D70wEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=A69NuYIvH8jm2xM9BAOsTIg1EcJw1CcKyABqqqrIPKOURRlmWvvdGEgg-g_BeUjLLMF9r8uRXP_3-jDpZ_rIQtM8NZfg2e-MjSWGCRdajJnuz4CIQmVu9gU3yi1NzSGtN-bEtlZVekdvPBzh4L_QjX-LImVioNY7rNMRQ6C9fHP-ehIiRyeggjamNbJOSvZ7cRb23jFIWWOJxaNt3CN1vngV2omZptuBQyyR9bmNzP5LDITA2kj-pCCc-iTkHxSIT8Y2IEnpU8riFBCV20Q1zTwUjPe-6e3ITZVREo7sr8mss-Vv6xmd8uCWvQ1NDIaosedH6bBsMQE-YqSb0bpXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=A69NuYIvH8jm2xM9BAOsTIg1EcJw1CcKyABqqqrIPKOURRlmWvvdGEgg-g_BeUjLLMF9r8uRXP_3-jDpZ_rIQtM8NZfg2e-MjSWGCRdajJnuz4CIQmVu9gU3yi1NzSGtN-bEtlZVekdvPBzh4L_QjX-LImVioNY7rNMRQ6C9fHP-ehIiRyeggjamNbJOSvZ7cRb23jFIWWOJxaNt3CN1vngV2omZptuBQyyR9bmNzP5LDITA2kj-pCCc-iTkHxSIT8Y2IEnpU8riFBCV20Q1zTwUjPe-6e3ITZVREo7sr8mss-Vv6xmd8uCWvQ1NDIaosedH6bBsMQE-YqSb0bpXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3k4AmPnqyjHnMF67TR9sLD5pZLm22MZy8qk8Qe9leXtY2piCmh3yR-OHwnb9s27NrpG9frQd7w47jRyKSD4_yfihFxzWQCudZ6MP6FoX2jGeZNvbnNW_hTTSZkr2Ho09heVU49CHA7IZTBbDJPDpYehcAmePcmU2SgjpSO6IEj138bZII1Ghbv--fbLGjzSdeCmWIw-bPmP4tcjmrHpd0FHvkCLf5doBHkfb90itUGIJIhdA-VPGMqx0DOTBRfmEG9LIZw3UnZV54fEGQ0hduqvHXyTEZyf6VPtMGrne1qRVwVU3YMxFadEiyL3CZGrYG6xW2xcxvBGcaU_D33s-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7xTmByV3EjJK82NM-sn5xwzoq44kiP1cIQz50jYOMZwHTjKzr9cXehv7BZOB7kh_6Nju_edGY9PJvBYke_iqLUSBIaud2HQZAbQInsh2R-6Y70-MFsmUwqTKxPA-2VQi2SseJKVMWmI9PgMB9Z6daTHFYuNZu_8_A36an_tupDQ6T3ub66u8aKy-g1EQWO2CSY7DppOPXzOW5fgLD32R-I83uvU9iOiiYHhOyMKXoZEce-t2ivy4zGJOuo3ljvgqVb814i5I5OCqFyXp1D2AcV0SpDsuIy85ohfaPqxCtPGZSGtv7Z_mKScmOGfKQei4d5iR27GYxQC36v0aktqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toEFxQp-FWWtsfrINmvbfyeIfziADgtm4wccvKoVwMUl7B-ph5PVOLm5i0IoA7dJFRj-poP6raco8msEKlR_zfX5MgWol_quaYXtBQ15MMfT2DhDaoM8zub-l8n7YXuI3A4qG2sOWUUZtOre32r5D0p79xZvDKfkw1-Z-am0LBy_ySpP0VRilg_XlAciJUcgeaxBNrFZ90mlKIkcLCCnQu9R5LkZbDQenBiVgX3yoh5JYuag6lHIVJChhyeqfKrbE4OH_MuQdGR8PPr3usqDueyHGSFnbIOOfcjKNNFznyIXkKim7ZceLv_gvxEAnIQR5Ow8FAYJDldwPZ1Y-NGL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmBH3Xs4KaZnaBZgRzvDO0Ag1UtVc77Z_LL0JyVrd1N_fUrU2SwTMkPjRgQABpXN6UNGTMlcRgN4i8zBRir0lB-A9zktYBU992nIt0IV_2iEkYpSLLj7x1P1jiLKcE-UTR8qxLvMJL7L-SPBHE7es9gTno-1sKM0iqSYxh8NNjIIVHHAETgbajKBGN0D6jFmSwTfGI46HJNfKo1ve7cmomerWgG3N_niFdHImhmTfCQvd6JPP56YcbJtzSSDals-I0Xp1IS57BJYKsEMCQ_CHCUAJBB99XWkT7h6-M4szH_UNEHF-EhZfKwQmmRzIoVUV5i50PLEEWXNpZVTQPBHLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS6n388599A6RPTuW3ogE0r5halU2-WfF9r4M74cuv70YrvEVo9wLtaLm3pstdMWJYnh9kGlnbymrJWBa9Db75Z9-Q2Q6tP5LLO7NzinPEAKjF4eb8QXpb50Mq5gjPt-j3_rXR67PUQ0H8Nf9rVfwR2UM36O7SVqyVaCWnIWD60B0QXm4yigVCtbTiso5Ht0qvVWxvqPsj9bhG7QI_h8hQhOt3YDlZZ2C6QyGnOUpsBzmxDMHRrq0rI1CXwJA77DsYZ-Rl6V2jyfKYkhMtgLGNk_A7iCD5GoUptq81NgWRYFcFrr-TJD3HKZZKT6k5LJa79ktYAcDWYp0PkoKOKwhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_nb1tynV_B_o2XoxOIv1svfy2YrliHl9IV50Vl6gvHz7oQM2bWUswWUryYuRvw0Is-UVgcIkKwg7s5Lrwr1z-bRuGLupAx60qJgnM-XLTF-Egkn-OPTog1Owp3y86OQYb68E5_i7pQ1cNaXmviuf9YKE4SvXw_QrJqADEw6atsjF4zY2SJUlJkuGZdoH0yRZVPWe_RESw2oTHMuwKqE_GMcEqzvTE7F7cvk67lgxtRG4ZfJNAhFhXOa9tmKKi0RnjD3dqhdlSBs3J_OGdEhNkYFhp3WsP2JoScoQ7bltXg0L2YocqrSRvk2eogtLVeS9nYGLjS9Kk9iq9YlcG2C-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYC4H5Riz0_jrOHfNVtg1bhh2iAaEetVQzLyQQZ_Ky6uPxBk7Sr1BOrhK6pmAITjt6lH1TgP1SwEMJUccWEbyuJjMntTLH2HTLNyOIISgbTdM9MY8LL_SjZdU_lYbyEb0oJ3y4lFeIMO0Y7xzG249iaEKsuhY807pTJVE8PBl6u7l5sNat0eSx6vAWa_OoJYUXNWd3mC-2B9Y8J_Z-Wms5gfZkklVRgOL1NnX_Fo5Ub-dT78KvHJpJUWa1sXTQb2Gg_3BQsPz3w8buktIjsUSF_QzyNJfHsUUZz6y-t6KWY8w4yjPxfdn17Kh-4dkSehoKzXyt2QNRklDR7b0xPgAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNb8l2-mGgnyl8HcWzew7nf_d18dIvw3wY2oopZZH27zMJeLBzqPJDh1nZgyZA-zkfazHT0XUG3Qg4vhc7wGcP5D-pyVLm-pykYuzkpXRn7TahSssdzVI4uIpiY0eI82KllPoefAdfP2IyqYa8dUIbZSxdEKjXH7gApGgZi9C4iedG3D3z3bqeBvbS2LMtQGnewGDMq31O5bvoQle_hK3CD-kN4rmlsFweN2zej-BVFVDknofV58BnvaSGsvRfg6ZBCvImDTaUbMGh0K5wNifXo4DbaLHiKTbs4b-YQztVzs1RLCe1zp1XZVLdUDfxyYyzghWNRYbKAJjEBDxFDPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2cWiG0zKWMEc0_2ae9AbJSgHX5r7tr5WSB9ukdc7ZW4W9yaOfaSTqJoby7CH9W_8Ip4Mc9UYzfUmchiYerMkRxDaGWSgvib5sytlCT-aAucrls_5pWvAw588ARBO-bVRYpMCjSN3Sq6k_tmO5OIIZrzpcq2qsKcUlD4fxXtVmX2SUuKBO_K4mtqNiClV33fqlbO_fj7RbEQINA7h6hMQuIxlqidyPixJPuJzLQ4NEa14vI5rwVj2Dv1en4oJ3DNfrHnHBSUU1y-NIY4w44MYU5v0Zu1EK3j3FAuIjY0zN5fdFoa8ussyP9j97n8sz5eWjn1RpM0SKlcgBh0i4TdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7hy5v6Ad8EyueIf6h2s3p9RSreIyTNkX0pSsBS3dxxD1gfiwCoFZ_SFE6KokLYkla6cLdbFvRGUvON5YuM_cOoI9fu-JpULwfR7aAVQUOWHyND4fY4fyuxfaKzU05NOtc521MMEtPbXI6bpAtfy0O79O3j1MruOM6h9au3Ed2bN2Jr0VoOzaiFh72JUOIAJ3pQFwWjTZxhyWyiIdd72Z0alhc85YST6tWmRaXPRwNdXSZa7RMkczmgytU8LyMiYiwjKZ2jdma5gn-UFWgwTj-W3uiQ0QVafzGjhHcWomaZpYojO1faNoE54d6edPl2x7Fki-kwxJambvtSiL2pqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMvhpja_ZUY8JFGjzDcPSg1JSi8zNThr_oJuyW3hMO1Mv86KgoP7AVvQaw2XzHhUcQ3wACHc95rcqTICHBi9_M9h_VPT5hNJfFCdgHcxC0O2RDq5RsyoruKokrZJAv3sFJq6xDV_Lk1QX2YuFtbHogSL-lsrLL1EdfUuu_1zF4YcaDMpYZmcgcm1yEmsieCN4fvkTv5S56GKaFq914XXDSW87WMT3cskm1v6v7lNEtoFyHyh5hxkmqwFeSgAe01bus94j8KTnPh60vbIVrcMoumRXD641ZDYA5fX5hVqfrDr0QYFj0N8ZINmdl_0-z0IgOWtcfExEoIFX8DJLDyQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=bM_FLqlhqxSOnFQl1wqUy8UmpGKdOWS0T-TlqCtFKIoIb4golsAM_FE6wU4GFc_qveshrwVNBc7fN_ihXPMcOs9FJc-3KaFm6pY0I6_lv6pTWA876lKnA_nAxMi3sKCkAMXuh8aTgVDS_Bef2mHNzX-EmpE02Ven2AQ5evNv27BKkSWo050Ys06iF-7osE4tArJDeXwag4p-_pcVflianZMeltnCsKVR19NWCz_-zLcmAycW4Zs6OTD0qeiLe1ytpqVBDOIdLDzx6gdmDRL5Ibe8Y0_wFjKptPwFGROaOYl0WWXGM3RRscT3WwLWH5mRn_wn7n9mFQjR_h6EnMXkCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=bM_FLqlhqxSOnFQl1wqUy8UmpGKdOWS0T-TlqCtFKIoIb4golsAM_FE6wU4GFc_qveshrwVNBc7fN_ihXPMcOs9FJc-3KaFm6pY0I6_lv6pTWA876lKnA_nAxMi3sKCkAMXuh8aTgVDS_Bef2mHNzX-EmpE02Ven2AQ5evNv27BKkSWo050Ys06iF-7osE4tArJDeXwag4p-_pcVflianZMeltnCsKVR19NWCz_-zLcmAycW4Zs6OTD0qeiLe1ytpqVBDOIdLDzx6gdmDRL5Ibe8Y0_wFjKptPwFGROaOYl0WWXGM3RRscT3WwLWH5mRn_wn7n9mFQjR_h6EnMXkCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juAXcj7VYdMt1pZalXg9zbF1helI01a3IgOyidCS2s8Khn0B1tD-hszYgSAcw8zY_ZpcOP-NKwimU1MBMzwl-h7sj0S-lCanHKycb_67zFSiw6I2siBqPqc0ouIB-hlMblM5doIVRhV7WzkFbiAnjjzTubpRug75op-q3SaGGexKWffd9Vmj5NyxaabatAOZpidB9XprAQvEDQrF5_LrN6WTAy_w-Us5MLc1CcA4uozgSGSL8CSl4i7beZ9yt6yK7DxYG03eiJuKfs6QKNfLr3vSJhsFcpbc5OckTE5UZ0ZYICN4WwGEJw5j42ZU7L5FK47jacAvOb_d2IVQmloLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=mh9TcGEGg8fPitL4-ZBOVFOF64Gry89ovTGbrZF9xaRWUho4dzdooDRfqxK9iN19a7OcTMHcDOSreapM8oB3UUFQcUyqACQM7KHXiU-_LAW9k9JpWFDcuVRlXiIVzn9mj5SoghKfhEc9x-lPy-8bqXx_NrqxObVyNAQM1yec2A_KmEnRqmJ1STytvnZeokM78Qvxf-vtLcJhJPFa-VvBDLxSMpO1PGaT1IjuzDZ7801b5XmTuR_YdNITm6bke9pQBarQneqZK8US706cBGBoJui6lo9LiZ6UnvpgNqUmRPw7kSgw300pTkw57b4nOHPo4qm8F5e5_iwjx71E5u_1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=mh9TcGEGg8fPitL4-ZBOVFOF64Gry89ovTGbrZF9xaRWUho4dzdooDRfqxK9iN19a7OcTMHcDOSreapM8oB3UUFQcUyqACQM7KHXiU-_LAW9k9JpWFDcuVRlXiIVzn9mj5SoghKfhEc9x-lPy-8bqXx_NrqxObVyNAQM1yec2A_KmEnRqmJ1STytvnZeokM78Qvxf-vtLcJhJPFa-VvBDLxSMpO1PGaT1IjuzDZ7801b5XmTuR_YdNITm6bke9pQBarQneqZK8US706cBGBoJui6lo9LiZ6UnvpgNqUmRPw7kSgw300pTkw57b4nOHPo4qm8F5e5_iwjx71E5u_1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=Agx7H_pivrLxNn2VXahv_6KOsBzbP-rWuFDWp4tRSHUXgD79rXl9RlKiaJNm66lk3VuTKvdx73zX9S7D-_nULcTqBr9QHFbpiitKltf-1MqNd5wfLegNl4PleqlpQFzcndUu5SqamfYLRSV9FBFpWYR9inemNhJtilDNhrn_ai4RroFS_Brcf4SITvkQTRmuSkVl6TtBIPPcW6UipRyzTMfU9UMSfJPzo9-miNCKH87afbRvIjTi06BjiODJXdb2t9bXGv8d7dbak8qPc98ZfbDpK-_G5EwA4GPQQ1Tx6hTNY3-y8yh5ByJHiW76kD0SUEtADyOYhjwVQ6-SbuClGba9d23saczzHtjPCF2ZVPGXlhmc8toitbzjllbMkVuXx3ctkdgfMXfxIj6SkQd03GSUoxYZgLpJNhOrAhIFvO4c4ShzTVMOreSkVXVxSthqzD2Iw1ZvIeZSLdTP2tM6NMg-BpqJZIR9cwRSaHO8UgESf55UCwshaDcsa4QysPFLLgufxDJNEs9k9BNKwndFgmEoYs6U4imI5aQIrxx0rvpOo-wXlLypoHnJMJnV7zH60ZzyoIpm_PnLRkR1NsfycB4eIhw8yDlvkauz5DN2HY9ExGFnIRbYyiqnsEEXqOtK_6Zu9O3RITAyFHH7YWkDfiUc1jaq2IZb2_7wF_6U8MU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=Agx7H_pivrLxNn2VXahv_6KOsBzbP-rWuFDWp4tRSHUXgD79rXl9RlKiaJNm66lk3VuTKvdx73zX9S7D-_nULcTqBr9QHFbpiitKltf-1MqNd5wfLegNl4PleqlpQFzcndUu5SqamfYLRSV9FBFpWYR9inemNhJtilDNhrn_ai4RroFS_Brcf4SITvkQTRmuSkVl6TtBIPPcW6UipRyzTMfU9UMSfJPzo9-miNCKH87afbRvIjTi06BjiODJXdb2t9bXGv8d7dbak8qPc98ZfbDpK-_G5EwA4GPQQ1Tx6hTNY3-y8yh5ByJHiW76kD0SUEtADyOYhjwVQ6-SbuClGba9d23saczzHtjPCF2ZVPGXlhmc8toitbzjllbMkVuXx3ctkdgfMXfxIj6SkQd03GSUoxYZgLpJNhOrAhIFvO4c4ShzTVMOreSkVXVxSthqzD2Iw1ZvIeZSLdTP2tM6NMg-BpqJZIR9cwRSaHO8UgESf55UCwshaDcsa4QysPFLLgufxDJNEs9k9BNKwndFgmEoYs6U4imI5aQIrxx0rvpOo-wXlLypoHnJMJnV7zH60ZzyoIpm_PnLRkR1NsfycB4eIhw8yDlvkauz5DN2HY9ExGFnIRbYyiqnsEEXqOtK_6Zu9O3RITAyFHH7YWkDfiUc1jaq2IZb2_7wF_6U8MU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=uWoWgUZCs_UGhWmkraI7yUCD-MxV2IlKkshXxeBMPtYnVarWVCxPDnPv2mFgj3XtfClZAlWz2UokgsErI-PbMd29AfqrMuO3rzfFmm23MKYNNryvziCpa2DDbfQbyEdTUdim8TUMt1roQO5q-4XSDelT3C1h5KsfmxZuZ1IVJyihcNnb0scobkAlNUlY12jx6YeYgk0P7wlnr7fz_drIDatnl-ljXcMCtRorLW3qHgHnrLaPk9k9vy-_1-98JmxO-OJCWxkhj4GP2-boZwgXRqAQ_XjB46WyFK9iyvVeDEqhACnXbgOcROk0ufrI-3tYhxIdX1duaiBPGNKZXyCjaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=uWoWgUZCs_UGhWmkraI7yUCD-MxV2IlKkshXxeBMPtYnVarWVCxPDnPv2mFgj3XtfClZAlWz2UokgsErI-PbMd29AfqrMuO3rzfFmm23MKYNNryvziCpa2DDbfQbyEdTUdim8TUMt1roQO5q-4XSDelT3C1h5KsfmxZuZ1IVJyihcNnb0scobkAlNUlY12jx6YeYgk0P7wlnr7fz_drIDatnl-ljXcMCtRorLW3qHgHnrLaPk9k9vy-_1-98JmxO-OJCWxkhj4GP2-boZwgXRqAQ_XjB46WyFK9iyvVeDEqhACnXbgOcROk0ufrI-3tYhxIdX1duaiBPGNKZXyCjaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=S3YRAgFqc48hz26fZ_YRR_XF689s7IcFQLy590-afx0glxhO-dRO9vWSEh3_unxMvxnLRPAEgJcMERksjv0p7gTqrES8R1fWpjiib0ng5NvLikjV9AZ9G8bPeMVvh_qAXCyJN4xQVggNTvSeQkrDjmjwL9DF1F0w3roWmXTWiVGv9eFGlyO8p-Ur1SXb3JTZcgEbwNLF6FT_dLpNyilpGVGKXUri2RhhWAYDEOWv1yysqh0_4N2MZTukc1uPCz6DOt-5bRvM72p4HtFHEQ4d6AvZzdDrzLlBHvPaQ_Fjq1e37RUWTdiDNcjgGqQTmWuDgpALQ1WV6xXSpYOroo1pYBsOH2Vogv-eRyvgKgAbtvCxJ7rs_Dg3kdjTlyh1h7LvJxaCZTF0Oi6s7lDFVhkHMhSAwt7s9aGVdwwHVlEQVa5QVhXbncgdnoAhIlf1kuLwtNouXQ7Hhgu86JieQQRXspaOvqNc7g4qmrOdUep2wBQxBq8asH98ywunefYkxTu-j7a9S-qGlw-qcQ0kaSygiPkFcT8-iITbGzm_fNRHFUqxX80d3_y7ws_M-K_Eg9qdutqj9j2mL3Uhs3_kSm-VgdskC8LLmf2ZsylsUuTADSI8hKH8JY3__gxwJjbFqrMYLzCDEF7YqdqqVvP_zHctCsRctSn_hMBjsd9OR3lpvfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=S3YRAgFqc48hz26fZ_YRR_XF689s7IcFQLy590-afx0glxhO-dRO9vWSEh3_unxMvxnLRPAEgJcMERksjv0p7gTqrES8R1fWpjiib0ng5NvLikjV9AZ9G8bPeMVvh_qAXCyJN4xQVggNTvSeQkrDjmjwL9DF1F0w3roWmXTWiVGv9eFGlyO8p-Ur1SXb3JTZcgEbwNLF6FT_dLpNyilpGVGKXUri2RhhWAYDEOWv1yysqh0_4N2MZTukc1uPCz6DOt-5bRvM72p4HtFHEQ4d6AvZzdDrzLlBHvPaQ_Fjq1e37RUWTdiDNcjgGqQTmWuDgpALQ1WV6xXSpYOroo1pYBsOH2Vogv-eRyvgKgAbtvCxJ7rs_Dg3kdjTlyh1h7LvJxaCZTF0Oi6s7lDFVhkHMhSAwt7s9aGVdwwHVlEQVa5QVhXbncgdnoAhIlf1kuLwtNouXQ7Hhgu86JieQQRXspaOvqNc7g4qmrOdUep2wBQxBq8asH98ywunefYkxTu-j7a9S-qGlw-qcQ0kaSygiPkFcT8-iITbGzm_fNRHFUqxX80d3_y7ws_M-K_Eg9qdutqj9j2mL3Uhs3_kSm-VgdskC8LLmf2ZsylsUuTADSI8hKH8JY3__gxwJjbFqrMYLzCDEF7YqdqqVvP_zHctCsRctSn_hMBjsd9OR3lpvfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2nh-XQtFQ3czZ9k5M3prsfB0ssAfv712B4DsOlylZPil5vibm5YCxH9-yRQsvitsLLsNAiLLRmnQDys1kWjwjUoU9oiGqULUiqenqFHGt4fWJinE_HdBM0LxN5u01KY4s5UH3smdj7-gbKxKbUCc2TUR5sHZSuBi5lSskhg0oruu7kQs23tVSJSkJwU9YAB2xuW4R34S91qOjSq3ehV4X4xsiO8d_iWpP0EYpWp3TAbFnpgnDTO-Hg13mDplxjmecRYfxNER7hFxkANNZBcOkcFafzakiSiLILD1ayO9H_9hqbc8oJTFGqzxYzMNeS-lp6ki70sBJWKedWaian8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=M1EUr0vgZnLVdq02yMwtQQ4yuyxQrssNWQiu-S1YdmbCiw1WTmM7JLoMMdKW5tN3Vh09rQvFmXQw9x2cVpiolbdwE77iCP-IHz5rBmNDPffYMAfKNW8WhjowixqblwiVuxEiKbnXvooPlGVApzfhgNsHCQCCGi_D2818QX7OuaczlQfqQ4iq_L66ZHBXw6yj6LsWQ1K9QNDI1jdaJE8_zDQwJ495yuAr4phwZ2NX4T8B9-imFPrhkXwckvuCL9LJZuzAxKQYb6vRlP19JccGHlU8uRc9bW4tdvFrj9er-l3Gl4GvYnbqOtoJcPXC55hZHLS2h1MauBEJ9e3JhButO1nVdD_MGZJyOFItcHB0CP_qZjX2nLqFMh0xj52ody3cAccc2iaRorCWn54vBlsbbels6MMUlegZcsgpoLFH4AsIc1QoEHR_dk92sXPP5QTaEfIc_OaRGGtu3rXLmjROo7nQwSASZqoUp41MoPNGjYA6obkRAnuMTXzXkPPxiK_YwWitDXfRt9Z07Qe0C6U3FXlWOHH-mwM24U5O1ktJoqWkbzd23gZLxS_5YLF0BFcJcu-Gv5vRVCcXzgnqc1XhZTIXC73kQ33JSqHdcBakm7F4AgrSx0u_OL-U0IyjZasgsbGzHOpxAAw0Gq5UvefFRRbcXdOkWYA44EYpliZDVr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=M1EUr0vgZnLVdq02yMwtQQ4yuyxQrssNWQiu-S1YdmbCiw1WTmM7JLoMMdKW5tN3Vh09rQvFmXQw9x2cVpiolbdwE77iCP-IHz5rBmNDPffYMAfKNW8WhjowixqblwiVuxEiKbnXvooPlGVApzfhgNsHCQCCGi_D2818QX7OuaczlQfqQ4iq_L66ZHBXw6yj6LsWQ1K9QNDI1jdaJE8_zDQwJ495yuAr4phwZ2NX4T8B9-imFPrhkXwckvuCL9LJZuzAxKQYb6vRlP19JccGHlU8uRc9bW4tdvFrj9er-l3Gl4GvYnbqOtoJcPXC55hZHLS2h1MauBEJ9e3JhButO1nVdD_MGZJyOFItcHB0CP_qZjX2nLqFMh0xj52ody3cAccc2iaRorCWn54vBlsbbels6MMUlegZcsgpoLFH4AsIc1QoEHR_dk92sXPP5QTaEfIc_OaRGGtu3rXLmjROo7nQwSASZqoUp41MoPNGjYA6obkRAnuMTXzXkPPxiK_YwWitDXfRt9Z07Qe0C6U3FXlWOHH-mwM24U5O1ktJoqWkbzd23gZLxS_5YLF0BFcJcu-Gv5vRVCcXzgnqc1XhZTIXC73kQ33JSqHdcBakm7F4AgrSx0u_OL-U0IyjZasgsbGzHOpxAAw0Gq5UvefFRRbcXdOkWYA44EYpliZDVr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT-NeSeJLv0Rc8pSKdQKmEM9LIT3WdY2DADDeoq7iwcyB9W_KvHrq-fDjLXnbg2HdD3fL75jacMtMsNsTwYpqiiMMTkHwMxZUpu9rG7gq-ALYMEBjT_je2NsODYLibXCHIPrwcTxl31YmEIVgCN562UleTZRVjnYVui-n7Fdn46W6Fl955_OwSvagP2O5eQVgaKqLEqTuSPePweQv-IlpEQR6NhRTxZFpyDtGx_bM3suLqyqR96H6gjej5pX2gXC09P8ZZ393Lrgkl7fqZ-HhDjNqnXdQ_81t2IGoHA55z2B781PaG0pdzBT2Sd0MPPS7nX2nFUQUe_pRsJj0RLWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coq52j-qst9rSQv5SMy6yJCZipV3kR7Wtv90x64HPx6puxRPcGKmj3JujmJbKgzn3IdGY_KosVvqN1EV00R_pobfBhRN-DMjzFnUBZVSj6QxcSgqbRCV4KsJmtmmW6Ykdx3xFy5LK_9HoKtDYOCRtX8YlI9-ksfM9kmGzLGYF7j4eLPY67GZ6qBOXsPhauXwSXdeAA1eL-rt3oatUSU553mdrogA_4B9ycgFrgIJKzmGkS9oTDkUW5pnxtkeuYx_gyNJLM_JcbULcYOFFXYDd0cgQwQ6A_bGx0QPdCg623Iq7m3ttK0Y642TeDfuZgn-h4Yh5DM1xlg4aBzCcRPsPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZfZ0LvrP_kKdm_awnEPohca81E1q-XCEIBE41E6zYl-DfS56ZeJpe937qCu02OM7p1JA4TycGlbUyGlZOfJoyJiSAwJI8vZUvXarhbdVtrM56_vqLYR1UwLrYIe7tWDf6ZHVH8BsOX_4jcchfghYUOBFGrM9TgApqN2xYFSpnIdsfhQBmLgeQZOk9KtGO9kdoFVFfQlB4f_ALJSmyHDDJln-sAePFnc1wHZ4-ZsZTZLKiRd5NsodNJ2LWfkU-mXVr9RFzIaDKlSRJpMalOXXy9SYNHS4QwciJlWAJFaM2Ymtdy-0SrDLHkh8y0Hwaq8cjrhi6gKGOlrxqhYs1wmbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FY7EvdJva64H7_g8ADAWusJE7xFVY_fXOz0FBgjBfEl2MYA4errLKiGDHqtkOz8-TwSoGBr9LIgmAZ3MHV-Ua2Y4Ceu1QeTVis0leZwYWpHB9zUiH4LkyAppWEkE0Ne3bgoLQWiRpTey1ZPDrtbOCu4oDYskTiL701fWcSS9isBPILWQYki7-QyPJhgh--2dYpFpt2IOwh07BbGGjZYTX4W7E_VFXY0-UpGridN5B5XONUjzk1rwafOSqpVibl2oCUoRacNw3Na3Rb6AXuFXIW8y3kNsmn_iudlBbRUKfMsvDPuQ7XbshwifsTWLz9olbFLERm4n04XD0KM3gOMvpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHMzm7_TEE09JlV29oLL0EaP3ew3EwlUUq1_xsDbaoFC-m6uWUB-DfhlVlavf6oQd5528c475UGOIcQOk0dsrfF4aHNK1BImm0386SO5ZERdbhRK2UDIOLVtG5KUbzaFea_1zvJvFw3f5XBJbU-YOxqPUrUgXuwXlw4wGVMg5Ih57XvgMfY6RXQZ9wOwY9neT1bFNzJgYlFHVwm2uziSX6Z6G3E5mybKgyQcU9e4HCDx3hlv9ZKgfnh7THF8veThNGF3IvDCpeg5ps9mjxKCq8iZO4ksyd8fqs56pUO0fviws5b8XGcf-u9umOKVtgwqFVO_vrzLCDw-p-tOKZE6MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyhr0058CxX69AkE7MKEhTgJ9YSIJrpYkxl30GruW-aCHys9a4bd5Fylfzi259IFjKerqtrzP4CQxDHw4ga_sQo0HTXy5ekA4hXB6ikdlXeXTeZLN2KmujejBJonatGhhGKaPNvIiXe4jt0-uc4whYQ4_2UsZsIdyWfY46JvXjJtH8Rt6Mk3p4X0vdyxRmqfa_ItBvgkRh3PpRpUH4jm-LEoJim34A128Z7ZaonBv15hajSpdjbYewdJfR2rD7Kmgh3Wc67xwKTwf61POuhdKU4_cGa0cdPh4CF2UnxCwrapAUhpp6-BzUNUa897GnMk7d65HBcOldZfOnrJWavkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIQfBylu5tbWbSwTx-uY2AqyN0sNzn0lCUVSCcbOPBiQ5YqqtjQxDeBMGXIhBhKUh3cfMnLxigXezj0pjOFamf1lBvo7j3-JscSKjg6vslJZjpa5ncB92TVBGDto88JrQY6BmrN5SHwa9WaGi7bG5oE5FK2MaC7ED9ddvId4b8o7ZoYSRPtUyFBM78tkLMtybxxzJirtJyK2XQjezch62293ucRSnRpqShNdlAkE9WOPSLALvJYwaUGezJaT6jsUlssHsapBT5TcUN4xAASQtby7rBe_Vj69NouvPvWFh2KDx9vxKI52Db1XN-HwmbK4fZTIt7k-iA84e4RT7r0JNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcvjvRNk23BIItUp3ldj-DwCA_BVP3iAwK5JtmXTDviqNP_eYjL1YNswflHmHbYwVrOMUXbOG8xxApNno1G0P4erzRUmznN0Z6561U8HjGLuabPzvgAYFnXCXPW5JOgYQooVVjkc-pOdcEh-D7mGKIbFEpUIMxxup2nqjgAQfiAgGsLwTzxOB8ujeIEMD0zhsuNuJgpHMeGII6c0YrsqS6sAO_wjWp2F1KdyQZ8dwRCbYgXckB51gkMbM2BJKzeClOnDjU6_cw27ANL9KsfX_9XgMPz0GN7ZvRGrTERD5v7FBDHGh2ZeP9X8yDT-Yy-5QyHwrQ2Cv__R9aaXPSyVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBFcwBAMs1rN7SBdzGAEL2YhamYCAA_sJjijBODrddiZ5-SDgONkPdQwLLKBuPLE_rdIhIliiNRg-mDyrVF9tZieTD29oMnC4Ru4w0JytQkQ8592sHBkLbJ1-mpnCNT_t_zcJzUryB9_NhGkpiqq58RBED5AfMk3riP0L1D93bd-EpTeowGzFBJusT_l9VUjxK71z1UWxsX11DXV1A37cMa8GxkWCsW-uda5myj05IFAIptaBVFntI-eJ5Wp-mkSt86miCn7Q63UrPS1dRGRfiTb6SC5iQ6OVAe0_FUTey2FM100BV97H4Skf6N7p-5OxCMWsmX2Sh1HL3znodBh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPRM4yJl6a7zzPuuE6hbG2m1XHgNyVyCjlS-GTJsUFABddmDgbJzJZeVH6SnJGJz5GUl3cVAX-lRVe4RiZDAlM_62jQdlbUkYmR6zh5SPwZTU1ebOZpmMFrak3zq-xjHCErgXWe-WMj6eyU_XzQioycCIfT9XUhW8GWE_lPrWlBBEYqsbFjETPhpBT8pssGESdwBuDLhY3oQSFgNl4OXEEmV6yqN1w87OWx5kTcg9zg9wCFBIR7KYuXySCqmRRBFVH9OCdgCFw-O0DoFAUuajwm7qjYohQOPVL4tFlTc2v6odtegkHHiLsbplidZBDitmuldilanb39lQtVhZrzZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXkO4k4bLZ197Yb_WASRGvaM9ZePgeBlD-BQ6N_d8tIElT_5XT6hXZbIcbEX5opPs9AH36lzR4sGoyV4bdSjwg56ia5YTeDQlXyod0YO1TLF-Tz1hoXkreCwcmab83QGyM8CppoS_d-KfXBOFyKKUZY5QUinRm0gQ2MEn9j-ArRaZNVELRTSNceL6928s7Z7MsEySfcq9FZphdMCv3w_k3O6QxMWmn-Mv3ROM7dNGnrGOG5irvZcMR2nMKOv5ERcLGwTMpZtX-gPA7xv_maq0-B6TZfco02CM-o8Weh3C-hgKppDD5_UvcrPO5oNzpqye6QiL3smcrHTW3FQ4zFPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSYLjK7yxaMU9kmA9KnVEPbse8L64qOWDpeFA0f42s2jxl6pcQCPXp9WnLn3Mhfb6lVWxtz2pVFyWE4lLLfUh_yu_TLzsRHmTHbSZOeWslftpvK1ZmWnf-8_itfNUP36rYg_vv6d_zItH3K_N9h7Q0_yhpMHTyzPoRw0UFbUNbXmSioZNyXzrKpSbB3eHcpLZdXQnQaRLKGonAjM177dtpXKA-TBG3dxjUfz6g4liCcSZkmpFkBj61gou_7imtxt7-k4Z_8DSNsyeNVy6gDTAESwiP3Az7KeUddQHEDMXQnrCrBszvyx40aqQou5xPIMiNj3HYhTvfWDpZruiIqdAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXLTbFkfw5JiMjxEBLUyD9zViQrTlm9N-bWB6fpor_VX2jh5s0mkHmApFFI1wjrE6l7H7jvz4NEcA6_sIEcnOjXaFWMwbuJGYy8uri8COcZv4OR2MWUKVWBIAUutHt7xEL16lsiN7m2ShG3UNlIsqaFGPC5W5HVf8k4bkMmqxxbBKY4b2swbTr3qBa6QMS8-inrn9agoDGHsl2GZxHcVXh9dNl5kF7zSrk5qpBp8yiTRIcydgBFCCflAZY0oQ5bK6sk7XpL2O2IGyUTwJD_bS_VWZmCG1Z-sOQHJ9jfBd3XyE7cMtj3CmHUWBf0KAWQHulXIBKf-4cPsPIeAsYhTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR3sKWsPs_PpvhVma2cWG7yLWboyxrZ0ryOMJQyQjx5upb5mGSnLkutTA-G-wgWWjNZJIGZOb4P5N35FPjndJROs0t6Bf4RjMjyFurBB8zvWGQqIV-O30mFEgfd8WBkGc46VmPDrpwialt2DrzIoanz51Le8YXirJoMol2Px1R1s94zupowZ-V07HOSZzHQnZnIhzY6I6GkUXtRo4QFTbIjEukUlXi6dbbyUHAPiHw6NAD_EH201KIdZJQKzxyI9uvEHjC7SkUUeFBsFZYUyjTcP1_8BXc6krTtTtWgG4Od9aXvCVhX7pra5dKx-WQcTK6VB2NP1yJhw_YIUio_35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coh0PCJGWtZ6xHGxitgc9DlpNrV74W4hi8Le2VoWX88TpsxFqsarVYp2on5WamOkUxNJLeuX7y5U1a9SteA6UUtONzyGF0KQir70sjpu2UbWQEKa4nWhY3vf-qgN5FnCUJ0iolhXvz87_fHX-0ZdwNhIw56lWWay8IELF2SVyU2KOYsVm9QIB4tvfYzd6ti9bDx2c1-IBezCgx0UcMjBeakZRtFbmsOozEVwXiJJGFxDRwqFQhcJiwRh9hp93R8YBUK8zkk1WzNwvqu9x1SfaG04ygBOqAlG-kjAfm98ud9Kg9UpzzZmAE-5UjgMNO8OmZ1AlO5PbmGLxRjjkCnYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqs9x81HorBPV-vep5QU_r-oXerPyPTUUCVxVLSg6x9oXCOWJG8s_tbLRRDS3lUN9F04wY_bnHl9Q2UB5YlaplDdp4fFINx8U-KqcUhSUaHmszqGBPESZjD_Bec842cexQYPi_mpeQp74vrtcEOams_NIPwdFuuRp_rQexD5zIJLApNagVWgdRTJcczsFx11FQy1vev3wnTHRUVcDVp-m6pFqlWsaVzBhDT4QQmxouSBIX785PY8tt-wxJgm6Hrj4SauuhVzGEx88ry6N8iRSzroZBy0vBpLlL6P8PpiConSmO9EbzzoKmr9-ggVhTtUE1L3PPuTStbjkYSjIFxk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=PMik3hZCYGb2WlA9TMaNp0SorOeLALcqRtrxY8G-NMwWH0-QPPLga3nPaOHu5D4jfRq2FRhVfINwNHFJDqrmVkh49xwXvPOThFqxRfKJ-aCywuXsBbz5pyC08UToYW39vPF_4zU_Iz121YvRcJLOkQXvQ1tcabS5u2TMI96-eqwqeIaWmyx81v7wkMnfB1BMtz0mp197pXmBD-wUU9fm6n4NBgyL6e4F_mOBRfyjsH9K26T2Z__nJjLLEki14bvMYCeoSTHgBf-pwqAoe-QSfC3mvfg9u-krAZQwCgAvJPFxjMdRbnfzgGim1u_L0xiFUgmMkU7fuz_46A7IVuFpxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=PMik3hZCYGb2WlA9TMaNp0SorOeLALcqRtrxY8G-NMwWH0-QPPLga3nPaOHu5D4jfRq2FRhVfINwNHFJDqrmVkh49xwXvPOThFqxRfKJ-aCywuXsBbz5pyC08UToYW39vPF_4zU_Iz121YvRcJLOkQXvQ1tcabS5u2TMI96-eqwqeIaWmyx81v7wkMnfB1BMtz0mp197pXmBD-wUU9fm6n4NBgyL6e4F_mOBRfyjsH9K26T2Z__nJjLLEki14bvMYCeoSTHgBf-pwqAoe-QSfC3mvfg9u-krAZQwCgAvJPFxjMdRbnfzgGim1u_L0xiFUgmMkU7fuz_46A7IVuFpxjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuipqruVHlR1vIXTq6TIwhtO2fiZQ_9Wzmc5ESZTJgLc2UY51zen_--vS88bg-2VerVwrdr8z8ez3V7AdfKNgj2HF8EQoqH6q19TVH7_urB2gqth2bwrsXmxEvMKJcxzPjAj3Lyqkr1HDtdiWzmS7whsgpsTaquhUrIoswyv-pMSRm2PWoOwnY3W7U8dD8hJkILsE3CsYEg2oav0ycNJpth0o902GyOvxzS_kCVWdL-0GoB7l55uYwrYuvkZmrgaOmi3B75xnvxk_VEkywkI399eX19ni24iBCQKR4zw5QOUWXJeJek359ZRzCjti-SiY_khp5cByK6wiAaTgAwMmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuPo5V7jq2FKPkP5qP9qDgVjURQPLXXjae5lBQncKUVBXqj-JcZLIVI-gHv0nD8_sxjk3XpNmd8nTgRJUY1DNYNFPBFOII8kZ_hMvvOFhkS9ebs2ZbjnNnsO8KCgwzc12nBKRIdmhZuUHlYBB0I4RZLblcUM61iHo7MvcZsAvZoZuB30fMSk9ZWzMw5Ta8T__YNNWMf0upNGGqeP1Isr2qMd3hMf3sKLgP5siJ0i8r6xA6iiURGrLi0bJVG1LuiXVgDF8ut0LFxp_h6agLYBGcPmuOHZJFg0NWmq_1dcl9cQYhzdP9_fNAi8AtHXM0bJsUx7QFRCmF_aK3R7UQ4nTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8tEb4b5PpWxVo5EOOKi65JX9kPmuxeZsyAT0TjO30dgd1vOIHXDgKW1z3YVFii0PEqHZTcOi8xh6w7kKNPonfACgJ4-MdmaY4_q-wcLT_Qyeia5Y37LPT9NIoW_mwVUgFTM-k2DmVuRgHGZkBdFGegN0kRdgxtlM0kgiTcw0Mo1IChsBMfcqjTk0xZ1FZRv0IHmpnD8zv0PUYYE2JBIkWN-n4UHYZZFYBTJdQqynj1gy-1tkHuc-bzDv_dTt3RmZNQVqul_je-fF4VxGi-_va2rvh-m8E2DRERgLegS4qV_4pjhqt4Ox54d8M7Qd8FAYpti1TACXfhw2lFTc64Blg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4dfAkUqBSrYE6Oz5Zp4C2zXJrlvU9_ZEc31pwRyHmTo8FFJbZh6vsYva5BwI6hkzlwwe0kQ-oW1HM5ZMB8sUM-DPYwj5OiBVuFbpDAHIQXJwVM2W5v_TKxyp9Z-7H84NSv4lAEstTswADuUc2hy93B-23ECYG1xWFQY-bzu6h176_mr-PI7TCli-iTR8dznrKVcB-WB9CklMDWlS-Vr6sBDFGAAd_tbH1_XsVihWcdxYJn-KfxDzlunblIhiEmFe3OrtQGKhvp2Y9L0hhDqA8iTtZH-4hkn3vHctAR50xe32VNN_xQ-L5A-iU7VrgBFPjgaYm1-u0s6Mq2fAEl6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=LtU8hdrKbc9N5zHySfkH0D4GgyOdjuHoy2BTh2GNs7kE1j2roM4uxJMBeFu2_q8gbmbAhscQ1INJ7eoleDfoTsrkaAydcSGHUTk2hndPefpjNhZx6JySCwRKYOpQCicIUNvvoadcCmwKG0FKpKbkuknoOXYkBZJ5tJlTGwXYyU1K1549QxP-cpiKabyOvQM7oM16hiSfUU2AlDz04uGwTkaTB9NXeh57zykhXL_1iZ6iPZK77LEk9tU_nXdxlBxXw33rqPLk8aH5EkPMznvJimkI4SDldskXGR81uIQPf-GUySirxLGI47Gbnpfiv72Zx77g0R19pnVvGPFLFn4ZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=LtU8hdrKbc9N5zHySfkH0D4GgyOdjuHoy2BTh2GNs7kE1j2roM4uxJMBeFu2_q8gbmbAhscQ1INJ7eoleDfoTsrkaAydcSGHUTk2hndPefpjNhZx6JySCwRKYOpQCicIUNvvoadcCmwKG0FKpKbkuknoOXYkBZJ5tJlTGwXYyU1K1549QxP-cpiKabyOvQM7oM16hiSfUU2AlDz04uGwTkaTB9NXeh57zykhXL_1iZ6iPZK77LEk9tU_nXdxlBxXw33rqPLk8aH5EkPMznvJimkI4SDldskXGR81uIQPf-GUySirxLGI47Gbnpfiv72Zx77g0R19pnVvGPFLFn4ZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=mgLxjppx-PyeYBlcMym4Wu14_VB7N7BfSWMJgoMeJj8T23P-INC1psAP5mIFIt7knxG08a4SmiM9_vR1EQu50DjpShBTsiLN5M8l_PaIY9aaZooXFNG312e8ri7Yhnwa_CwDUy8FCTEHHRIWHCIxOVK5sHcooiIM-es-P4fyB0287uU9oYhpSavKYAR4-eU1IS9B_3XW5osvin2udkXEwLbInPowgt5hcd2JR9Y_Iy7RtvOruH7h9s4ZQ4KBMpJKwZGd1jnMMoDCP3Q566aKvUHozb-ke-JkNi6ALW2m3IJgR8z9knP90m2FBJTMamWVMzs_PCACocQlZwKBkZ7HyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=mgLxjppx-PyeYBlcMym4Wu14_VB7N7BfSWMJgoMeJj8T23P-INC1psAP5mIFIt7knxG08a4SmiM9_vR1EQu50DjpShBTsiLN5M8l_PaIY9aaZooXFNG312e8ri7Yhnwa_CwDUy8FCTEHHRIWHCIxOVK5sHcooiIM-es-P4fyB0287uU9oYhpSavKYAR4-eU1IS9B_3XW5osvin2udkXEwLbInPowgt5hcd2JR9Y_Iy7RtvOruH7h9s4ZQ4KBMpJKwZGd1jnMMoDCP3Q566aKvUHozb-ke-JkNi6ALW2m3IJgR8z9knP90m2FBJTMamWVMzs_PCACocQlZwKBkZ7HyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2mx0t_wNCv9jhmulAKoMVXPrLApAgtMgWkLuwAP_2pK4g13kNv4jcHzKpJs27pQv0kl5z1N4mF-3zt98gDRi1CcLeCg2MHKqomxNNx746IA1a4nqnBrJG7bOQB54TYC2jNSfCXqlhnyF1vhPEUgi-pT--vAStfy-mKoTzDIFwaIU2gB5b0rUE0RkSpTRRaAALVomcxj87WqH228IMn3xyW7BbjaRhmiyFl5wPay-deqYdiuIqYLwFhrRgba4n0OTCKoC_NTrcBZ0hyZDC1ruTq55BAsiSdwHlGfN_Px12KdS8lKewkhI2ZQVy_Xr1uNF4VF0gJ6QWwS05JEoNgrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ghEioPLqxGQzJ7EzaIBp-US6LUvPVEln1YcNPfjKaErEMbQbJRS8Bih1QW_Ayp-9u1cvtFFgu7gzvQzcmkUdZ8rza5vInvpmHY7S-IoPoqOjhwHjNsIdFOkQP0k0v1CUi98OUeRQ4itLzReqEUaXmXniJlpPlpRkQfuRCWiz3IOk0vM0da6A04jSETOBhvBf-r9Qa7Kj39CegA9BHBOoy00AAQA7lO_ecHPXbxSySvyBtGmUeTTw0ZFLJjrHhDjeEov9ixBQ6rCjx0isiEUhmYVeg_clnOm8UZ_cu4Xrfmugt84jVuok7p7gh3G-bclpTq1b0N88Me9uswxABSOwTA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCBqkvs98eqc7lXrz-uvMy6qu9z9pw7qVUmZKjIHNaiF6ZCmvfAdeRTjHBELKW6aV3RZDqLnQoKGpsSsEt_FNKBsTZhn9I_CCjWfEk5bS_mGDtY-xj_cepsUcCkQr0POFWAq4u0byewJi6HGWWKL54AVoD_It7fJPxfwUXUb0uRiFT2z8cwTcM_I_I3r14AzJfChaG1aJBbQ85l6S72j5Gc7MJoC-alnnMxPfy7Ebw_sbVdfrHgWiPrnNkLV-0iZFUB8XZcXTZOHlzQeDN0FHvWKZDHPCrMIG139Wyp9wfAAD5OKnJJoJu_96rXnbAuNFa3nKpmN5KCAh7iXTUeaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=pYojvPmUR5lnPSCJsGhcIeihNvDW_ARqdlSXl06Sjqh8uqgsuPW_LTXm0bDFcVMYbwV8bmYsRna1l2uqKyob0EedYy5hiyZoZwI0NeQGrj-k-FILJFt0ShvX88sqeivoyaAmZLTFDdJVnWOt2UzvunPn1XuSLuphL8ZtiYkWkYGs4GZG-ejcXUt6VX8O8iCrpF2Vf3yBqq-4cb8oguNB4ePiHe1FILSdeiKNQ2GwjKK8fb-Sj1NxG03it6XtLT9NG5txwC-bCTiDL78kJRwd1-M7yxIcQNQRdXB3pW21lYWgpefjDtC52cLs2E1DD7kJXN0cg4bEC1PZLneacHrBTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=pYojvPmUR5lnPSCJsGhcIeihNvDW_ARqdlSXl06Sjqh8uqgsuPW_LTXm0bDFcVMYbwV8bmYsRna1l2uqKyob0EedYy5hiyZoZwI0NeQGrj-k-FILJFt0ShvX88sqeivoyaAmZLTFDdJVnWOt2UzvunPn1XuSLuphL8ZtiYkWkYGs4GZG-ejcXUt6VX8O8iCrpF2Vf3yBqq-4cb8oguNB4ePiHe1FILSdeiKNQ2GwjKK8fb-Sj1NxG03it6XtLT9NG5txwC-bCTiDL78kJRwd1-M7yxIcQNQRdXB3pW21lYWgpefjDtC52cLs2E1DD7kJXN0cg4bEC1PZLneacHrBTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=W0hOiASAQCi3RpI8dmPMtFqX77LPDVOLbat0-EdIjg-Irung_PoN6u33YJgH9yqD6DjW--MaS9mFzq3Wsqqf5FOr21fRhffHp5poF8w66KjOMABDNIcLPWd9P3AkCoUVi6ad1_hnHov4HBwzWgC8VqTnjY5NeotSPSeUTvh9JlnCgW9wgp-rXv32dgXmPwBd4eXWwdnA6BGncCZwJCp-1EEQOFyeIw4JcCFMn5ea3Z01bIBeq1qumU8CYfg3s6q4ROmu3v_hnKicY1gKOr7l-xCkKpjarQ5hhhYG53mN4nmFx7tBw51XM-Ahe2k4WUEKfXjS1nZGlRBlS32a6_lJyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=W0hOiASAQCi3RpI8dmPMtFqX77LPDVOLbat0-EdIjg-Irung_PoN6u33YJgH9yqD6DjW--MaS9mFzq3Wsqqf5FOr21fRhffHp5poF8w66KjOMABDNIcLPWd9P3AkCoUVi6ad1_hnHov4HBwzWgC8VqTnjY5NeotSPSeUTvh9JlnCgW9wgp-rXv32dgXmPwBd4eXWwdnA6BGncCZwJCp-1EEQOFyeIw4JcCFMn5ea3Z01bIBeq1qumU8CYfg3s6q4ROmu3v_hnKicY1gKOr7l-xCkKpjarQ5hhhYG53mN4nmFx7tBw51XM-Ahe2k4WUEKfXjS1nZGlRBlS32a6_lJyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaeyIK-yS1vm9MQoNMC0xRKpAAeDe1iEc-HgAn7liyvoFF9igYPtRwji8_AHswONB5CqW2we9D2JaEdnrrHCsuN-e_-3yjMVLDwqlj8mnsxUwYGL4xCC9-qbBeinJLFjEXL76jJBjJZOOp-_meoWMW-43w1VhdnjuZUucypzJ531yeyrHqfSbMvdA8NT54I00LJ0WlurEJW9wKp8ZqocyKzeortoGx6cJJ8dowXKFSOd3ULzgPZptGpm9EPaw9qHTH2GvToHSyDfEux0-1RyewPSTvaAegwvMc0ez4Dpwm1izIIwHkqBkQHnuwT2DXgaF8dBpQeJ4SlVuUJFusqdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L37q72lkQDIxhfeIGZZovzfCdn1DqJZL3HOPyRV6LIFr7gnVecNCyEf7-w2fRnYDejFnYDWKps-JA5eN0mH-4n2_ZNG3gi4NDQgYXkPIeDF_Q_cWoJONSvqqA68fxudn61tznvaKda_VcHvUVEDso7OX7J7V8bbU-hDOCtNQQU-c3QYrajkpIVAWQv5JmO4LD8GYnUUbGefsB7UiqHCAjVLupxBeSsRZjrUB65_LukVOkXcerKLpluCF_DnxF71jR4c86xeL06JvEV5uFIgrgttl8ndElcxfhut9nbY3zqFGS6gkJXwGT7mK9NGXlsH0g4e8BpkBpmV1aCU8Bt85MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYhq4yjMEFNHKbhK9JSQSp_f9WN1mUrTZp1dGMlInHsuNAzVxcQQPv25Tqh6-UCsSaUJnq-irUlzAA9W6V92lW9V4wkn0hXr0dcOwGL2HfsgfEnx2u6DP2dNZrhZr3vLkWlnUEyCw32vDWkO7nCtE5u4w1_RP4gsgNV-BeJshFSiUZmgwwuLmsWpdcFsZUx_pI5zyUiDD8HMFva5z6nRTrQaPdXqFjvwYRGIOPLu8QHAek_j0z5fH-XWZpNvfRwM6PYgrCZxmmY32btRGwwfeoBgc_QJPhKjvFRuGWiEDjj0uI7IaZgbKd2aFm36aw548e3PbL6rnPY_Ao5Y_3J0yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD7lBpdnizjbrTZgGwbIdHlBl19vQtO5lXI4UJMc1mviTTfcI_6NevF_GIxbGb8_x3JHSHyUE0IegD08SLe2eAbQiVYuP2Y2WL7agagMitUCsM8ToAXe1H2UJV1Uv99ff8H-h4RyUFy0RGPQB4JLewoH0TiLM2HKLcLsGv5pjEc6xtl59L_Aqu_atDkkWH5lCH3WY3MwxIgb83-RQq7F39DQfB0EgqyLLR7o4Yj2fXxXDE7Q1wBxi7HFT_gIt5ZR0Til7rdWheQC_S5KEqdTldQ4X_28GjtkuYUn5enraQqejBU7_OZ3ZShAUtWpzhgbJBJsrYAzn4KupPrLEqL2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
