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
<img src="https://cdn4.telesco.pe/file/WUabFCjN78Ahm67FF5ERSi94Hp-kuOWL2qJgFn6S09eAhwQtmLVpXwv8VVNn7SbmS2z2OjSHSrGY_TWOiSwOrwVIj2mAty9LVSQW1SzLFOK46OFmJfLNT5HXFI_doymEOy8b06FBBWlxXpROFoi3LNWaKjlP3ygwBt9mb2dPVyAuXUnZYjnNpHLi99qTHuU7xfiaFHaTuqSXTrMohumRZWVp0iONcB--aOB3KAnVbj6q5ae22grAk6cA3MhgSchiHOGNYGWmEzT74XTbTbLT2BG_mu_Ldk5af646g2a-sHSxoiNgUC7z54VxGuhcwEXBLkYbnTTfpfVvkrbLC5ZaiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-133581">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
رئیس جمهور: بیش از ۹۰ درصد اعضای شعام با توافق با آمریکا همراهی کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 731 · <a href="https://t.me/SorkhTimes/133581" target="_blank">📅 18:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133580">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
❤️
#فوری | نیویورک تایمز:
🔸
محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/SorkhTimes/133580" target="_blank">📅 18:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133579">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
🔴
خداداد عزیزی با حضور در باشگاه پرسپولیس قرارداد شو امضا کرد و رسماً سرپرست پرسپولیس شد / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 977 · <a href="https://t.me/SorkhTimes/133579" target="_blank">📅 17:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133578">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
اتفاق خاصی نیوفته خداداد طی روزای آینده با قرارداد مالی خوبی پرسپولیسی میشه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/133578" target="_blank">📅 17:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133577">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
❗️
خبرگزاری فوتبالی :
🔴
🔴
اوسمار به مدیران پرسپولیس اعلام کرده برای شرکت در تورنمنت سه جانبه به ایران برگشته و برای ادامه‌ی همکاری در فصل بعد باید فکر کنه و از خانواده‌اش مشورت بگیره.
🔴
🔴
باشگاه هم به خاطر این که فصل بعد در صورت نیومدن اوسمار به مشکل نخورن؛…</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/133577" target="_blank">📅 16:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133576">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
✅
اوسمار به مدیرای گفته برای فصل بعد باید فکر کنه و با خانوادش مشورت کنه و باشگاه به صورت موازی مذاکره با یه گزینه‌ی داخلی و دو گزینه‌ی خارجی رو پیگیری میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133576" target="_blank">📅 14:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133575">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1962b1668b.mp4?token=aNjRyjdG0rKx1QtbhBb0u1sEzJa5k9mQxAZHdvbp_wkD8ixWFzzweTW5-RzhcgReA2CAzzJzc5-SUZ725p8hDGiC4qVicDuUQP7Yoc3WXmEVNBFMBg5rcWmJ9uhz7XkI9XOOKb3wVAf6TrPEplqX5wgI9-N_ASVW6-hxa6NLkYZHskU-wW1Nuq98MmM1eHB4ZLd4m8e0z4mWKVcNIMR2JRkUWHeZfLW-5b3nSqGOr-sQeZwtq35hBqzl-QONc0Hw5mNFPZ1ZdKEoK1DlN27fyLv2dMrj739iI__sD5SpZrCUHAGnqsQIqxQ6EO_L6mj7gko0me-RkGmfiw8u27E5Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1962b1668b.mp4?token=aNjRyjdG0rKx1QtbhBb0u1sEzJa5k9mQxAZHdvbp_wkD8ixWFzzweTW5-RzhcgReA2CAzzJzc5-SUZ725p8hDGiC4qVicDuUQP7Yoc3WXmEVNBFMBg5rcWmJ9uhz7XkI9XOOKb3wVAf6TrPEplqX5wgI9-N_ASVW6-hxa6NLkYZHskU-wW1Nuq98MmM1eHB4ZLd4m8e0z4mWKVcNIMR2JRkUWHeZfLW-5b3nSqGOr-sQeZwtq35hBqzl-QONc0Hw5mNFPZ1ZdKEoK1DlN27fyLv2dMrj739iI__sD5SpZrCUHAGnqsQIqxQ6EO_L6mj7gko0me-RkGmfiw8u27E5Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇮🇷
ایران آماده و مصمم برای آغاز دیدارهایش در جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/133575" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133574">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
تاجرنیا: شنیده‌ام پرسپولیس در بحث اسپانسر، قراردادی دارد که باید در لیگ نخبگان باشد
◻️
به تلاش‌های باشگاه پرسپولیس احترام می‌گذارم ولی برخی اقدامات تنش و مشکلات را بیشتر می‌کند و حتی باعث می‌شود انرژی نمایندگان ایران در آسیا، در آستانه شروع این مسابقات گرفته…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/133574" target="_blank">📅 13:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133573">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
درحالی که چند روزی از شروع تمرینات پرسپولیس می‌گذرد، محمدحسین صادقی همچنان در تمرینات غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/133573" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgbDK0lOd3_fEHNCRmikeeN-cKKxxkmqxmCDYYWqUIn0tvWrdAwJDFl2Qw2hXSVUFIo_ukhcv8OcVeFYWpspk-nKTPNTBkfpqJTak09v2zq_KejxM_wk4DoJyzzMDKOF74HqhcABO0WDT_SqQZ3aZhbhTGOawtlgQUacyA7Dep5tDqa113BzBPtSs9R4gog-pj4J_ZziDmYN1jFErK1gW5YMvm_jrdkvjGa_w2Y7VI8xwFOme-L1vr6cO2OJVG9NkO-x_IKtI-08635F-b4iJmobbVGfnu9V7lqxMm-th_oGF27OTheTv8PVnr3ektmoETItLPWu8rejO5mvfQpH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
درحالی که چند روزی از شروع تمرینات پرسپولیس می‌گذرد، محمدحسین صادقی همچنان در تمرینات غایب است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/133572" target="_blank">📅 13:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSaz6RPTqI3g1qSs7Lcg9zFWEdlWV_1jnql7r58n9PaZiDa-SlowhOftZXD0VnKEkWVhUX5NOGHE_xjwNQRL45bIkHwqlRn9UuMmw2BlvpMILG7KkzZoYiLgSPLpxA4uypS-K3QKqdTvdNn4yeMWK_l_WBbEkwv5khu5c_B2jTjBGbv4SS99t4wmig72aZHP9N2urDnSVJuaMm3nsK2my2RMFlrwFkGTFB-ybm2AuoUxgLFydGx--VpakRyxYIPaOCF3d5kTx1cVPYQ7hqyFinHZ8w6SA4x_3gfCA_2iA4Ezeua66HkQYgCI6zZDUJw61hj_XeqQI5OF6FavcnPFkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه H جام‌جهانی ۲۰۲۶
[
اسپانیا
🇪🇸
🆚
🇨🇻
کیپ‌ورد
]
⏰
دوشنبه ساعت ۱۹:۳۰
🏟
استادیوم مرسدس‌بنز
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
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/133571" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
خداداد عزیزی پیگیر امور نقل و انتقالاتی پرسپولیس شده / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/133570" target="_blank">📅 13:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📊
📊
جی‌دی‌ونس: برای شرکت در مراسم توافق میرم ژنو!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/133569" target="_blank">📅 13:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
امیرحسین محمودی امروز صبح برای تیم ملی مقابل تیم جوانان تیخوانا به میدون رفت و موفق شد یک پاس گل بده
🔴
علی علیپور هم موفق شده دبل کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SorkhTimes/133568" target="_blank">📅 13:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‼️
مهدی ترابی: در گذشته زیاد آهنگای تتلو گوش میدادم و تتلیتی بودم، اسطوره ورزشیم علی دایی هستند
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/133567" target="_blank">📅 13:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwwtzYPgK17Z9_dzor362LtYnKrYypJbvcTlLImQsGQUNsXDRILDocTAq8sfsbeUZe2JoMsJ_QDn7Zl17rLe8Artp0RABgq8PaoC7eeVJzqVVV6MXIQB1nXnTxIY53_PYu8HUCYRIGhcP4HZSgizcz0VOWU8xYT2vTwHsDtKlSXp6j04KzqTWz3Xsl_ghu4ALowUY1y_VO30IjJKcEpNMwiw36C4oEhQWnObWMJ51WFEXI4s9K7HEyPooxb06wktZeFjkilqyqU7uvTuKm-j5Yq6uYw_tJDDl4zrrrhdCbC-xvyJPScuckp9A281iyvPMtIZj_UCKjpH2lIYYYlWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر به صورت رسمی برگزاری سه‌جانبه انتخابی نماینده آسیایی را پذیرفت.
‼️
اسفندیارپور قبلا اعلام کرده بود که گل‌گهر انصراف می‌دهد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/133566" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🤍
امیر قلعه‌نویی:
می‌دانیم که ایرانیان زیادی در دهه‌های اخیر در لس‌آنجلس حضور دارند و امیدواریم که در بازی فردا در ورزشگاه به ما انرژی بدهند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/133565" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
براساس گزارش نیویورک‌تایمز؛
کاروان تیم ایران با ۱۰۰ افسر امنیتی و پهپادهای پیشرفته از این کاروان مراقبت شد که تقریباً ۲ برابر اسکورت تیم‌های دیگر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/133564" target="_blank">📅 13:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
محمد سیانکی گزارشگر صدا و سیما جمهوری اسلامی راهی آمریکا شده و قرار است هر سه بازی تیم ملی را در جام جهانی گزارش کند
🫥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/133563" target="_blank">📅 13:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQkVp7WOWkLQWLC1yXldaP4QRK_L5fsHKL5ZKuff-d-RDHy5rZGGgxLO9dlNS0QWUhxSkOWIqV8H1Xycv4HYe8I8eBZkx1PnYqih8oDuQIA1wfsAJe7MxlAgHnNzRSY9EYWoqjXLB8obZJhPlyy6J5wCJjKInAQP8t8fVt7LM9LZNtR8wjRHsFKw8_W4MIVaQBmWYP_2a5tdjoqkmqTUPd_TNe1ebwKMSI4cNWuYAEt3jzyQOZvTTYj6XFsOcs11HHN-dwbjfwkhMjy9oQOA6einUyvSwJ_KVUYkRG_5MpZ63eULRDMnVYdwJLq6E0Ss3vzgoZc3As1LSdG65zXB0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
راوی ماندگار مستند ناصر حجازی درگذشت
🔴
بهروز رضوی یکی از اساتید هنر دوبله و گویندگان فراموش نشدنی رادیو و تلویزیون ساعاتی پیش چشم از جهان فرو بست و درگذشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/133562" target="_blank">📅 13:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
خداداد عزیزی پیگیر امور نقل و انتقالاتی پرسپولیس شده / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/133561" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
اوسمار به مدیرای گفته برای فصل بعد باید فکر کنه و با خانوادش مشورت کنه و باشگاه به صورت موازی مذاکره با یه گزینه‌ی داخلی و دو گزینه‌ی خارجی رو پیگیری میکنه/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133560" target="_blank">📅 11:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljDu-7Vth6ZkhOER4r02-6SSMmCvcFqoDjeWJK6cNxA2wAJ1eYmRuU3_L25w5MCHvXk5ybF2e6J7BBJUmRfjtFNXpPxY63gJDbwCyMTlWIhu43iOIJjMheJ_Y7wA-kjwFV0MjF-C82uf7OX7UX-lGSmJ7OfF5rdL5J395XTzHNVxl238xCqdWizhBZg-NkqDQc99ZjKBwiguY9oiMVKHNMaGQZdCG8Uic07TXmGRJp51sz6Ltfd6RzNSUVm3LGvKiLSkZPy-0_dGACgIzg60S7CgMGvGLP8deUYhqRfS8mN1yte_9NAZ1ojSu6UCfb5X-EIyI6MXxg67pP4wtiAhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
رده‌بندی تیم‌های لیگ ملت‌های والیبال 2026 در پایان هفته نخست
🔴
ایران در رتبه پانزدهم جدول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/133559" target="_blank">📅 11:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
❤️
امشب ساعت 4:30 صبح بازی ایران مقابل نیوزیلند برگذار میشه
🔸
بیدارید یا خواب؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/133558" target="_blank">📅 11:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133557" target="_blank">📅 11:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133556">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">#جام_جهانی
😀
کنداکتور آنلاین جام جهانی فوتبال امروز و بامداد فردا:
😀
اسپانیا
🆚
کیپ ورد
🇨🇻
⏱
ساعت ۱۹:۳۰
🇧🇪
بلژیک
🆚
مصر
🇪🇬
⏱
ساعت ۲۲:۳۰
🇺🇾
اروگوئه
🆚
عربستان
🇸🇦
⏱
ساعت ۱:۳۰
🇮🇷
ایران
🆚
نیوزلند
🇳🇿
⏱
ساعت ۴:۳۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/133556" target="_blank">📅 10:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇷
⚽️
🎙
امیر قلعه نویی سرمربی تیم ملی: برخی بدون مطالعه می گویند جام جهانی با ۴۸ تیم آسان تر شده است اما به نظر من اتفاقا سخت تر هم شده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133554" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
اقا کریم از بازگشت اوسمار خیلی خوشحاله چون دیگه بهش فشار نمیارن که سرمربی بشو/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/133553" target="_blank">📅 09:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⁉️
⁉️
حضور عزیزی در پرسپولیس قطعی است؛ آغاز فعالیت‌های سرپرست جدید در امور نقل‌وانتقالاتی
🕯
حضور خداداد عزیزی در پرسپولیس قطعی شده است و حتی او پیگیر برخی امورات مربوط به تیم و نقل و انتقالات نیز است.
📊
📊
عزیزی خانه خود در تهران را حدود ۱۰ روز پیش در جلسه که…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133552" target="_blank">📅 09:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
فوتبالی: چند بازیکن پرسپولیس به کریم باقری گفتن خودت مربی شو ولی اقا کریم گفته نه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/133551" target="_blank">📅 09:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
🔴
کسری طاهری:   •
⚡️
میخوام امسال قرضی برگردم لیگ ایران  •
⚡️
با پرسپولیس و استقلال مذاکره داشتم.  •
⚡️
طی چند روز آینده تصمیمم رو میگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133550" target="_blank">📅 09:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c82165294.mp4?token=VmO8lPBKi-y8jRMeVOy2GSaJC5QYKYSbRZdUXkwVb1q_6Pq5j4g7ZODVfLbUzl1ODnD0m0zPQQ5ocTUEUz6kAhy-lXcH19ipd9LksZ4O1CSvs4xHXUgRqZKmJlK9H5uAa1ne84IyapvYOUSaNCmQO8E2QffK79ALMUjj-xWNvQgXYwfVetyslJbS4iupVD6u6V5Gvn8HX_GZt3M192MaObMRYIy0lvD7Wz2EQg1yX4zwTsAK1gYSZ7aHzgy51OKzSkda67KlT90ajYtkA9-ZnaKL3KeCg1iygnG2IlvI-lHcyjRmS0UN94cE86dDVm5uiouiHqMokecb_y1veYBEIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c82165294.mp4?token=VmO8lPBKi-y8jRMeVOy2GSaJC5QYKYSbRZdUXkwVb1q_6Pq5j4g7ZODVfLbUzl1ODnD0m0zPQQ5ocTUEUz6kAhy-lXcH19ipd9LksZ4O1CSvs4xHXUgRqZKmJlK9H5uAa1ne84IyapvYOUSaNCmQO8E2QffK79ALMUjj-xWNvQgXYwfVetyslJbS4iupVD6u6V5Gvn8HX_GZt3M192MaObMRYIy0lvD7Wz2EQg1yX4zwTsAK1gYSZ7aHzgy51OKzSkda67KlT90ajYtkA9-ZnaKL3KeCg1iygnG2IlvI-lHcyjRmS0UN94cE86dDVm5uiouiHqMokecb_y1veYBEIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⚽️
بازدید بازیکنان ایران از ورزشگاه سوفای، میزبان دیدار با نیوزیلند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133549" target="_blank">📅 09:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
نیویورک تایمز به نقل از مقام‌های ایرانی گزارش داد که محمدباقر قالیباف و عباس عراقچی برای امضای توافق راهی ژنو خواهند شد.
❌
به گفته این مقامات، ایران عمداً تا پس از نیمه‌شب به وقت محلی صبر کرد تا امضای توافق با سالروز تولد دونالد ترامپ هم‌زمان نشود
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133548" target="_blank">📅 08:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133547" target="_blank">📅 08:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
#فوری | یدیعوت آحارونوت:
🔻
نتانیاهو با درخواست ترامپ برای آتش‌‌بس و عقب‌نشینی از لبنان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SorkhTimes/133546" target="_blank">📅 08:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW56hF3P1OW6NmObpcWC_9_2Qt62GXwW7bcoXyOliuYyO8dysT7-TQgl-CouZW-KDUrbNQT2b3yg_cGfx_y2gSqWCvfkdrn-NpTb2lqYMjvPfrQsUBXTY4pG13t_g7soD6-Oy65keveAajFcWFz1i2nOuzVCYdrPNgJTrReKLc2K95dnSpKyv6lRRUa4n1A8UATKgMD5EgaVO6yQf-N_MKKYemXEWmrTrlFUgYl9z5kcQC2iw14N2ulnlrNEmvSc1KHdB5sBIsJHhGPkx-o3PBcCxOrL5IBrlL5Oe6r7zs4Yr4h0g-i1ptLI_Ndb8W3OCp9y2w8G1oPofAxvDEh6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه F جام‌جهانی ۲۰۲۶
[
سوئد
🇸🇪
🆚
🇹🇳
تونس
]
⏰
بامداد دوشنبه ساعت ۰۵:۳۰
🏟
استادیوم مونتری
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
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/133545" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
نتایج شب گذشته جام جهانی 2026:
🇶🇦
قطر ۱ - ۱ سوئیس
🇨🇭
🇧🇷
برزیل ۱ - ۱ مراکش
🇲🇦
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند ۱ - ۰ هائیتی
🇭🇹
🇦🇺
استرالیا ۲ - ۰ ترکیه
🇹🇷
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/133544" target="_blank">📅 01:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133543" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
منابع حکومتی: بعد از هشدار قالیباف، ترامپ ترسید و محاصره رو یکجا برداشت، برای همین انتقام حمله به لبنان رو ول کردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133542" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
✅
#فوری | کانال 12 اسرائیل:
🔻
ایران پیشنهاد ترامپ برای ارائه بودجه اضافی در ازای عدم واکنش به اسرائیل را رد کرده است، و حمله به اسرائیل را قطعی اعلام کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133541" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133540" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133539">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GTUnqnSnHaPLCANeyDKzWxlrABYgnSNX6VN1L4y66rNVpNPxbUigcAMiDjQIOZSP1sAWJMHZtsddZujYN7mkpQkdm9BZFJKwSNjr_tRpdnhDv7k9R19ytSQGofsgZWoa5LaXHseOQdJ890-4DNeotio9iSbAlnzzdPYKC1E2ey2aawqcCYixYJAxTo5d9yq3hcbqVf5zasJrw7tkkMcmMcHZwYnw1yXW5b0GiNVAbTMCOcm6w_Wh_PjpNi-zk-X_qFF8FqPWna5M9L6MJaRAgIrpr9uBYkioIDhAiPITm5HgDM6ucJxAPNdQehIbuEXZ4IVtky2se0IZeXfBA5qErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری
| ترامپ: توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می گویم!
🔻
بدینوسیله به طور کامل مجوز بازگشایی آزادانه تنگه هرمز و در عین حال لغو فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔻
کشتی های جهان، موتورهای خود را روشن کنید. بگذار روغن جاری شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133539" target="_blank">📅 01:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133538">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
❤️
فووووووووووری/توافق رسمی شد
⭕️
⭕️
پایان جنگ اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133538" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ: من علاقه ای به تغییر رژیم در ایران نداشته و ندارم. تحریم های ایران طبق توافق برداشته می شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133537" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❤️
🇮🇷
فوری/ترامپ: امضای توافق احتمالا توسط خودم انجام خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133536" target="_blank">📅 00:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❤️
ترامپ به وال‌استریت ژورنال: بزودی یه بیانیه راجب توافق با ایران میدم
❗️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133535" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133534">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❤️
🇮🇷
توافق میان ایران و امریکا امضا شد!
❤️
توییت وزیر کشور پاکستان: الله اکبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/133534" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133533">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❤️
🇮🇷
توافق میان ایران و امریکا امضا شد!
❤️
توییت وزیر کشور پاکستان: الله اکبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133533" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133532">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRJhjtYOthK5JI_P-U7l8oY0Jmptkz_EoiBnmJp7uNBHvrRN18Fhv0b9_zVGLw56ZJMzU_5q8mqcZPqWi11zP1McNmnAdBuL_qFZMjDcdszmViFXHvWyc1iLjfX_xslZwggiDSZEEnESDRvQc0FQyd-YXV_3UdMuFEnNX3QCKPZrC572t2KX3vuIOJTY_p42msI0MjRyezVEk16yyCe1vLjV4in_GWss-Sf_gg6Fn7zI4IINnExTUAwZGer7P7kg8VKKG_ZMO0PcTy26PRe-kU5FqfM-dyAMVmi0mXDxPWctU_wQo99sCaRdZnLwfdtcPSmvM8wYlekKdqSIDyO1Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
🇮🇷
توافق میان ایران و امریکا امضا شد!
❤️
توییت وزیر کشور پاکستان: الله اکبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/133532" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133531">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
خداداد عزیزی پیگیر امور نقل و انتقالاتی پرسپولیس شده / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133531" target="_blank">📅 00:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133530">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
❗️
فرهیختگان: لیست خرید پرسپولیس شامل طاهری، یوسفی، لیموچی، زارع، محبی، نوراللهی، مغانلو، ایری و اون یکی محبی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133530" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133529">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_Drs0NiXr04s6vKJcOzkXJonzjMOA6MM7Tk1wuNjmFpcMxhQL6kvSPbIaTiv87ADUi7MM3z0oKoukBMPiYnRPl5Sy7oDxUhY0W_gt2JpGavMPf0IRkUpqVIrMrzQSFpHOvOMUSuzlBsp9esvHVXczz3WKT-0myVwSiUG-GrMMS9vB3G_CUn0TeOrJLQJAnCEFGZER_LJc5s7pI61VprwSAWawZqKpxKmkJaCWHavaJQKzO31exF-ZjjmLCHnNkkIEq9t6n2t9BU8_qTRT9qGtdmEMDnV2xnSadmGk24-Ll12HKnrDOoCANKFM0NXeITACeeAJ20X90MQVUvWzqPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ترامپ: ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133529" target="_blank">📅 00:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133528">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
یک منبع امنیتی اسرائیلی گفته است که نخست‌وزیر بنیامین نتانیاهو انتظار داشت حمله به بیروت باعث تشدید تنش‌ها و به شکست کشاندن دیپلماسی شود، اما مذاکرات با وجود این حادثه ادامه یافته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/133528" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133527">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
#فوری | یدیعوت آحارونوت:
🔻
نتانیاهو با درخواست ترامپ برای آتش‌‌بس و عقب‌نشینی از لبنان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/133527" target="_blank">📅 00:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133526">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
سینا اسدبیگی در لیست‌ اولیه‌ بازیکنان‌ مدنظر اوسمار ویرا قرار ندارد اما مدیریت باشگاه قصد دارد درصورتیکه با احمدنوراللهی یا محمدقربانی قرارداد امضا نکند سینا اسد بیگی رو بار دیگر به جمع سرخپوشان بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133526" target="_blank">📅 23:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133525">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUuEGTmMNUSYLOMvPSjXBA6nkuVQeFEzirQyfMfIcC0P7xU_6E-oD94_6k1yDOGIS_ZNvTF3q8ShSswsqMSkodqCtKSUJvdrTJpRNvhVFWewR8HhGCoL35XT4kdEACQwdwIIANmPLvedC9GNAhq5FqW8k0M0VtMIYdA7tWjZQO8xthPf02FApqHrtHLQt6smBOjbWMZpi-eCm5PxaAavh-1tVWBVNlKMz71BOC39Rb0hK3f2_uTO2wQ2fDtNFuGtwPAwvWDGXnTuo4r7oX5tkyUA0d9lLoLMYscWvbGvXZxGejICgtqaneOxSPnfUw8iWTzlytcu49_0a0FXuA523w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
این وسط دلم برای هواداری کیسه میسوزه که با هر گل آلمان یاد یه بازی و یه خاطرات خاصی افتادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133525" target="_blank">📅 23:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133524">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
فووووووووری
🔴
مدیران ارشد بانک شهر با اسکوچیچ وارد مذاکره شدن و اسکوچیچ برای یه فصل دو میلیون دلار خواسته / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133524" target="_blank">📅 23:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133523">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
فووووووووری
🔴
مدیران ارشد بانک شهر با اسکوچیچ وارد مذاکره شدن و اسکوچیچ برای یه فصل دو میلیون دلار خواسته / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133523" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133522">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
بانک شهر هنوز موضع خودشو برای ادامه‌ی‌ همکاری با اوسمار اعلام نکرده و ممکنه اسکوچیچ گزینه‌ی اصلی بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133522" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133521">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_otbE-Bmwsw7rMWjvjIfD0t6NEg3W1_TCR0sFfemqgF-VIevA5fDDQSNWg3X9HhG2ulAu9Wcaj9rhqVBPD76BocB5d5Nbohn95YJorv34eBsnIq7k3-F3jk7Q3vmHiQAjLV8Wl45biPyi6b1w9xT2qYCke7rB0B5eKk1vPsEyg3HAC-kaOth0nqvyHVLT2LGy7BfoPcDhz4T7jOdfydtTNCm8yrSMTlaR0dedt4FsKmH0bvWyeFgf1RxAWMFIuNJErOW2b216VNcg_t5pqhYvoL_g0A4paeINmigJevIxfHVoHJ2BIENdHBLe-AMDt3vI6c0Q3V7P5AFy_oP5kzcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇮🇷
برای بازی مقابل نیوزلند، ملی‌پوشان فوتبال با پرواز چارتر راهی آمریکا شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133521" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133520">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
آلمان تیم مظلومی گیر آورده .. ششمی هم زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/133520" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133519">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
ترامپ:
🔻
به نتانیاهو زنگ زدم و گفتم: «تو چه غلطی داری می‌کنی؟»
🔻
ترامپ:
🔻
به نتانیاهو گفتم حملات دیگری به حزب‌الله نکن.
🔻
چرا نتانیاهو باید چنین حمله مزخرفی را انجام می‌داد؟ من خیلی عصبانی شدم. بهش فهموندم.
🔻
او اصلاً قضاوت درستی نداره. من این رو…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/133519" target="_blank">📅 22:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133518">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
آلمان دومی هم زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133518" target="_blank">📅 22:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133517">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
اختلال هر ۴ بانک که مورد حمله سایبری قرار گرفته بودند، رفع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133517" target="_blank">📅 22:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133516">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRXfhHLD7-3O_N9qNrotRUBuWa_M-iShb2vFXWxMEy7Q_R47e2DfkBgLOuBdGPVQXbdrAY38Aw0aKTvVUHQdRd1RnvoftSyCXIipjf19wRgA2Mmdkj2qNPrAWP_ZjfGw_3gf4KvUGucqwzDBoVSVPR46teCSU2Z7wfwBOxj3bfbZF1UzF_tCr0DGcyg8G5zk2BQ_Ga90-Ut_gG9DC8rWPEkXCzROM7YwZsRQQlxbXxZzTWWBtCVjcLcBnS6qDSF4728Oyj_ZtMMKJGM8At-_kD9FZVBU8Re76b7BOdpy4AL_agt5wYbhBSElhS9gGH1PhOwpV2r0VUHz_4-bYjxJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زیرنویس شبکه خبر خبر از حمله به اسراییل میده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/133516" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133515">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
یحیی گل‌محمدی: فکر نمی‌کردم لوکادیا روزی در جام جهانی مقابل آلمان بازی کند/ او یک بازیکن حرفه‌ای بود/ از روزی که در تمرینات حاضر شد مربیان از نوع تمرینات‌ش راضی بودند/انگیزه زیادی از خودش نشان داد/ لوکادیا یک مهاجم شش‌دانگ در محوطه جریمه بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133515" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133514">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
پیمان حدادی تو یه حرکت پشم ریزون یه نامه زده به تاج نامه زده و مدارک تخلفات دو باشگاه استقلال ‌و چادرملو در صدور مجوز حرفه ای رو برای تاج فرستاده و گفته اگه اقدام نکنید به afc شکایت میکنه!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/133514" target="_blank">📅 21:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133513">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
یارون آبراهام خبرنگار اسرائیلی: ارزیابی اسرائیل این است که ترامپ به زودی امتیازی به ایران خواهد داد، در ازای عدم انتقام‌گیری ایران بابت حمله اسرائیل به ضاحیه.
✅
جزئیات نامشخص است، اما تلاش‌های پشت پرده در جریان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133513" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133512">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcUvhTnnOOZMKLG_Ca6-MmWeEZG8-ik5KenInDFdZco_APQhErio-oKEOP0WdD0ryXc3CCSyXUuJDilEvZU6kQNTnV6CnMJp5gdFlB3dDV9N1rfb9xvVdibSr8HPgDKMXX-4YlIKBpHPpK7i-i4XH1OIRgQmtUdRMiH6jDW3Y4P_KdIJCzrY7mswqzZAjqO2-u1SeYti_ioVtSLMXp_GBXvfgmcWMF7fFP3SDCZKBIwEV8yqWxdxLbpCjFXiozekVd3drjJCZBf3qHlxAYhl1rOiNkagIDiIBtgwOKR-8pqnuDdRpo-7Ff-vNzJVn52eAlLeupo5j9bEU1O7hKXOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/133512" target="_blank">📅 21:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133511">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvqVzBmTcdSqkykJUgIEClEWtNHfIFl8XZ516vXpVYc8Q0kriuYoG-7v5fnm5UpmS8DoSQRbWz7F0JHr1O7DSaxUJcNPmDgeYT1RqhlSDseykzAUa0U3Ofa0a0i8_oU-9U4SfnA39176chqCvTIXgAzv5no4H3YOraJRDC43dhAgtZCj55ZX1PCzRvH3H6u2UK6sT0cqsOHni8_C3g60i_BuVCCpDAiwrSHDDJKxgVnPMf2efUepCHUJFU7kW7-Cp3LPSGfPxn6qVhuoFXOiC1e3BFi9g4cjMN-nhoFph0o-b91w7vefTFmefYEyMujBr3aKV3NdvGzXGClmDkOgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های امشب جام‌جهانی رو با ۱۰ درصد بونوس اولین واریز پیش‌بینی کنید!
🟠
Netherlands -
🔵
Japan
⚫️
جام‌جهانی گروه F
⏰
یکشنبه ساعت ۲۳:۳۰
🏟
استادیوم ای‌تی‌اندتی
📌
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
📌
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133511" target="_blank">📅 21:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133510">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
رسانه دشمن:طرح آمریکایی: ترامپ به ایرانی‌ها به‌خاطر پاسخ ندادن با شلیک به «اسرائیل» پاداش خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/133510" target="_blank">📅 21:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133509">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✅
گللللل مساوی کوراسائو به آلمان با تاثیرگزاری لوکادیا که مفت از دستش دادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/133509" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133508">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8cba0bad.mp4?token=Yhtj44SFFNirlYb9puJXB30a115Fm3vroo3YNUnkAztCV5um-IqOdw-vJD9mcMntK53TRMeuht1lBpH39o8Lal4VRAh4diq6DbK4OKXEOhCxGnKI5FhPNopAeciiO5XSaAnNMl3jf3Rgz7xPhIvT-dfo-__vGn_up7pOLhuWhww382MH6n2aF_uKG3aWtifG03MVpINOl3OXhXN6_jntXTzotX5nHscffeasNsqvNcyPx5ai-GvvOowrsH-uL982ZOjbscwn19dyyGvrZKzL3JdB04ZY4bJs2YoC6j1zIIYXY81nUVkwpwRxo4nPM8CWNHP6ZAeolaF2VDWhpWd4vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8cba0bad.mp4?token=Yhtj44SFFNirlYb9puJXB30a115Fm3vroo3YNUnkAztCV5um-IqOdw-vJD9mcMntK53TRMeuht1lBpH39o8Lal4VRAh4diq6DbK4OKXEOhCxGnKI5FhPNopAeciiO5XSaAnNMl3jf3Rgz7xPhIvT-dfo-__vGn_up7pOLhuWhww382MH6n2aF_uKG3aWtifG03MVpINOl3OXhXN6_jntXTzotX5nHscffeasNsqvNcyPx5ai-GvvOowrsH-uL982ZOjbscwn19dyyGvrZKzL3JdB04ZY4bJs2YoC6j1zIIYXY81nUVkwpwRxo4nPM8CWNHP6ZAeolaF2VDWhpWd4vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گللللل مساوی کوراسائو به آلمان
با تاثیرگزاری لوکادیا که مفت از دستش دادیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133508" target="_blank">📅 21:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133507">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
ترامپ به کانال ۱۲ اسرائیل: از ایران می‌خوام موشک به اسرائیل شلیک نکنه. این توافق در ساعات آینده امضا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133507" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133506">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
ایلنا: مسعود محبی مدافع خیبر اولین خرید پرسپولیسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/133506" target="_blank">📅 20:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133505">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🔴
پشت پرده حضور احتمالی خداداد در پرسپولیس
🔴
🔴
سهامدار پرسپولیس دنبال اینه یه اسم مطرح رو بیاره کنار تیم. تو چند جلسه ۵ گزینه مطرح شده، ولی بیشتر از همه روی خداداد عزیزی نظر دارن.
🔴
🔴
میگن چون عزیزی تو تراکتور تونسته تیم رو منظم و یکدست کنه، بعضیا معتقدن می‌تونه…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133505" target="_blank">📅 20:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133504">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D82F-9FXvOl2xD7b2BMOB0X_O4KUw5qbLX7kIhw8r-ju8k5f8kF440IOAlfsKxBzRaWkBrS6ogozeOLYKTlRDVm5-5397NtbYGiOhcgQsCEj76jFNNMxvdMkvltJEs__mewihtZerQV1EbBI1rkJAf8xqIkD_ApZ4D73zitfEIL4s7TfI2UU0zQltsYqgAzQVjZHbU2TWz_PGN3SncAspgfWvoVnR-oDdgM70CMqjC4lfZjhqF5xzLlJu5JqzKbQ1_sGfUrzLKG6Dwlu9yxo-VnXW1BtpeY55ZGyDJMAD5lWnxuTNb4wXlOh4nJdlaM88PoB7jZ6Oc3YU9gPqTJzbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
یورگن لوکادیا مقابل آلمان فیکسه
🇩🇪
آلمان - کوراسائو
🇨🇼
|
⌛
20:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/133504" target="_blank">📅 20:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133503">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
✅
یورگن لوکادیا مقابل آلمان فیکسه
🇩🇪
آلمان - کوراسائو
🇨🇼
|
⌛
20:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133503" target="_blank">📅 20:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133502">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
ترامپ به فاکس نیوز: اگر توافق امشب امضا شه فورا دستور لغو محاصره دریایی ایران رو میدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133502" target="_blank">📅 20:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133501">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
ترامپ به کانال ۱۲ اسرائیل: از ایران می‌خوام موشک به اسرائیل شلیک نکنه. این توافق در ساعات آینده امضا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/133501" target="_blank">📅 20:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133500">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
🇺🇸
ترامپ به اکسیوس:  قرار بود صبح قرارداد را امضا کنیم. حمله در ضاحیه این کار را به تأخیر انداخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/133500" target="_blank">📅 20:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133499">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
ترامپ:
🔻
به نتانیاهو زنگ زدم و گفتم: «تو چه غلطی داری می‌کنی؟»
🔻
ترامپ:
🔻
به نتانیاهو گفتم حملات دیگری به حزب‌الله نکن.
🔻
چرا نتانیاهو باید چنین حمله مزخرفی را انجام می‌داد؟ من خیلی عصبانی شدم. بهش فهموندم.
🔻
او اصلاً قضاوت درستی نداره. من این رو…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133499" target="_blank">📅 20:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133498">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
ترامپ به فاکس نیوز: توافق ظرف دو تا سه ساعت نهایی می‌شود.
✅
حزب الله به ناکجا آباد اسرائیل حمله کرده بود و هیچکس آسیب ندید ولی اسرائیل در جواب به بیروت حمله‌ی بزرگی کرد و این مرا به شدت عصبانی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/133498" target="_blank">📅 20:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133497">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
فوری / ترامپ: حمله صبح امروز به بیروت نباید اتفاق می افتاد، به ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
🔴
اسرائیل حق دارد از خود دفاع کند، اما حمله ای که به آن پاسخ داد بسیار کوچک و بی معنی بود، کسی آسیب ندید، مجروح یا کشته نشد و نباید…</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/133497" target="_blank">📅 20:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133496">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfrxeI3Nm_XTigzX04KY4PaLz7YPcaeG2jw1BZrfOV_yt3LOPRNkgKH5nxR9KWpSYM5NMrMJ_GlfSpXksDDJYyLhzc5OPr3QXA6b4Gx6KCpZZ1QwU9i-QLFeIHdhGu0giOEgDGErNrnr70MYKDhyjbIusYo8wHWYcfzEgrrzhdIpAU8HgFAMcwoXZ8rMGEP05k6HITLy8mAwvZAPxy_tRgSinfqvRj3NOOC95iAUv94UEL1cWbjC6EElB-WpkXRiKwh_khCL_kwytdEE9WHR0x5ErccDYlYYZnrYjrrMFrxFswJzrom3plu6YQA8XAGJNd_7wV2r8Aqk4-_80DRxcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اوسمار ویرا و تولدو به تهران رسیدند
🔻
با ورود سرمربی برزیلی به تهران، تیم فوتبال پرسپولیس، تمرینات خود برای حضور در بازیهای انتخابی سهمیه آسیایی را زیر نظر مستقیم سرمربی برزیلی انجام خواهد داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/133496" target="_blank">📅 18:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133495">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
اسفندیارپور مدیرعامل باشگاه گل گهر:
🔴
قرارداد مهدی تارتار فردا تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133495" target="_blank">📅 18:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133494">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
با توجه به تاخیر چند ساعته در پرواز اوسمار ویرا سرمربی تیم فوتبال پرسپولیس و دیر رسیدن وی به تهران، امکان حضور او در تمرین امروز وجود ندارد و بنابراین باز بودن تمرین امروز پرسپولیس برای خبرنگاران لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/133494" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133493">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
تو روزی که ایران و آمریکا قرار هست توافق الکترونیکی امضا کنن، اسرائیل دقایقی پیش به ضاحیه بیروت حمله کرد که خط قرمز ایرانه   توافق پر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/133493" target="_blank">📅 18:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133492">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
تو روزی که ایران و آمریکا قرار هست توافق الکترونیکی امضا کنن، اسرائیل دقایقی پیش به ضاحیه بیروت حمله کرد که خط قرمز ایرانه   توافق پر؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/133492" target="_blank">📅 18:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133491">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
محمد باقر قالیباف درباره حمله اسرائیل به بیروت :
✅
آمریکا یا نمیخواد یا اصلا زورش رو نداره که به اسرائیل چیزی بگه؛ با این کارها نمی‌تونید از ما امتیاز بگیرید ، اگه اوضاع قراره اينجوری باشه که اصلا دیگه باهاتون حرف نمی‌زنیم.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/133491" target="_blank">📅 18:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133490">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
پایان بازی | هفته اول لیگ ملت های والیبال روز سوم
🇮🇷
ایران
3️⃣
×
0️⃣
آرژانتین
🇦🇷
🇮🇷
25 | 25 | 25
🇦🇷
23 | 19 | 23
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133490" target="_blank">📅 17:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133489">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8ZpAIpEV9VAz77fqRDoNcr85h-qA76TYBaEcJ0DFcDaaI1GQby1RNfDyNyd7mE1OkqU01wt8GxsXI3eq3RH0E1tCaujty34cSgShSrm-HOWBV9lsMd5PrI052w6gUxmGnX0r8mxvoxJG_gZz3kLpB-LbIgZlsWdNxWG97hvJ1R_uqnzPOPjJ3rHLs8gKoyJEHq_e6HKgvAUaMRFkdElfXqg_VZFKRDCg51uN6SUCAu-qMaxlDO1kF7lhHGDHTH56vloEmQgQ1YsC148LTY2cIB3b4zCkvB3_7w-v9X9xmkf4uVfXFB8EuGbpK4He-ARK-HmTVGuPT7fBthhA2E1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
مهدی ترابی : رفتنم از پرسپولیس به العربی بزرگترین اشتباه زندگیم بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/133489" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDwg2NFwdoiD-c9bzl3NWK1vuY2O-mGYKrmbVDYoNU1RORS9GPxoev-TikA-5i5DUpuiEteirlTrFmwfvxLhCC9Zi9DzKz4MT1Enug43a6gLuUIzg6S9NHAaUHI3UezyMpb3sS_jR7HBMEOabBZqmM6ONARtZKCbdtnR1WffqqyUA6AvJDSfbDDPNs0foQomXsEkz6_noHZvtdNZlqV8M_aLPjt_4Bn8fsxxOMhINn2PayOhs70TmY9KEbjrCTFGo-FcbO0RGPdgh8G5wY8JKcuUT9DECEWJ3AGfNbbASdXfpmBV0lb7UfYoWtWpvQ3zT-fWq8A9Ai9br-GkEjLAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مدیران باشگاه پرسپولیس برای تقویت خط دفاعی خود به دنبال عقد قرارداد با علی نعمتی هستد و مذاکرات خودشان را با این بازیکن آغاز کرده‌اند/ ورزش سه
😕
😐
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/133488" target="_blank">📅 16:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133487">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
محمد باقر قالیباف درباره حمله اسرائیل به بیروت :
✅
آمریکا یا نمیخواد یا اصلا زورش رو نداره که به اسرائیل چیزی بگه؛ با این کارها نمی‌تونید از ما امتیاز بگیرید ، اگه اوضاع قراره اينجوری باشه که اصلا دیگه باهاتون حرف نمی‌زنیم.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133487" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133486">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
اوسمار ویرا بامداد امروز وارد تهران شد و تمرین امروز پرسپولیس با حضور او و خبرنگاران برگزار می‌شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/133486" target="_blank">📅 16:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hK_rJdd5gJT9Vq5tUHtFQeAL-GZd70OsfcOn3l0HxorLfyiEzV0ATjn0pJdxYF9W784Me0npwUHzapabBEPa-_7vLI3Um030GMfadVa34Dp1gn5vbUgTfa_2yDaHyVpI-lqbeN54vHaWiWWyhEmv-VKLupElFgI8A48OtW5BfiYEuZIX3CfAgFdmMgwLinigcmNlRry6QhgJLoAXn7gHJCHfdnxH-Ru72sa2HikyxFsLje2kXOz5guBoA3P0T4T_cxbXn-fW9VGafxqiI8iQGlEZbRq33K4NU6WGZyn_yQlRZNs0XWy5ZaCyqFDJfVbnpibvvjXCToDCRJ_bFtCeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قالیباف درباره حمله اسرائیل به بیروت :
✅
آمریکا یا نمیخواد یا اصلا زورش رو نداره که به اسرائیل چیزی بگه؛ با این کارها نمی‌تونید از ما امتیاز بگیرید ، اگه اوضاع قراره اينجوری باشه که اصلا دیگه باهاتون حرف نمی‌زنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/133485" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133484">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
شایعه داغ نقل و انتقالات!
🔴
یحیی گل‌محمدی، سرمربی دهوک، با سروش رفیعی تماس گرفته و از او خواسته برای فصل آینده رقابت‌ها به لیگ برتر عراق برود و اینبار در باشگاه دهوک شاگردش شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/133484" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133483">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWjGN-une2zzZnFB8jft9iFX1aExg-y7oGh4ZOPVMbsiok7bV7s0nA9kcJszCv13a2LsernuKgMRPKVetjJRfSGUw-YYK93zF6PoBWifp4I-BqZ-lPTk8PTDZCEXwUTPHmTdoy1ZgwqTFERrEsZ80xi_NBABnE6VJUIaA7THi1UM4GtUt50WwB9ia2qXEfMjy7fOybctyXrX2gFt1Xag5txP--sE_W6kvrZVcgTKFffh_7Qfk3PV4-DrROU37tA9f95YgJAZZ0oMwONN8T4CdB--_Vj5SdAXDEMfhW5PH9CzlkUVnmxBN0Ro60PhASZEeddsSQeeHOnfSxJ3By1N5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
فراخوان بزرگ طراحی کیت رسمی باشگاه پرسپولیس
🔴
باشگاه پرسپولیس از تمامی طراحان، هنرمندان و هواداران خلاق دعوت می‌کند ایده‌ها و طرح‌های خود را برای طراحی کیت رسمی پرسپولیس در فصل ۱۴۰۶-۱۴۰۵ ارائه کنند و در خلق پیراهنی که نماد هویت، افتخار و تاریخ پرسپولیس خواهد بود، مشارکت داشته باشند.
🔴
این فرصت، بستری برای نمایش خلاقیت و همراهی با باشگاه در طراحی پیراهنی است که بر تن پرسپولیس در رقابت‌های فصل آینده خواهد نشست.
🔴
مهلت ارسال آثار: تا ۳۱ خرداد ۱۴۰۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/133483" target="_blank">📅 16:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133482">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
بابایی مدیرعامل چادرملو: پرسپولیس با گل‌گهر بازی کند، نه با ما
🔴
اگر رأی کمیته استیناف به سود ما صادر نشود، باید حکم دستور موقت بگیریم و پرونده را در دادگاه حکمیت ورزش (CAS) دنبال کنیم.
🔴
به این مدل تورنمنت‌ها اعتراض داریم، اما راه آسیایی شدن همین است…</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/133482" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133481">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
برخلاف شایعات مطرح شده وحید امیری قصدی برای بازگشت به پرسپولیس نداره/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/133481" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
