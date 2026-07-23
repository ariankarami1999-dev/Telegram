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
<img src="https://cdn4.telesco.pe/file/drVgZTvAC9RJxc242KpFiBczDNIezyEaUb7Vlum5STS5orbOJcm8Q0f-laJij_rgSXad3eOcJn18v5xoIa8P6iIcVkpqsb334QEb3Q5-iAxWo6Ae7e0kPqtMW5_E6XN0jKh9WHjeCaoDdgkZgRRy-CRkcAydTYApZ4SdfUkEk5yhhckHALsuy1LShWHObaTDqs69LZdu0_nmMOSWjGETADIjSR5EPZKvxiBwrQ4KjZna44JjIQskbnAFlP8wpR1UQOId_q9OFdwEZKy8hchMpOXIcmFWn6DGdxFz6d6RUuQhasGZGNZnyWog5im2WjvmvTLnGyDfmUMibz1zSfrDdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 01:27:42</div>
<hr>

<div class="tg-post" id="msg-136570">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136570" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 392 · <a href="https://t.me/SorkhTimes/136570" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136569">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOyLskX6gkohgrb190DwxnTDZPX72Inm40HDfWaHGhcHduQNG9smQpoDcfut6MoSJ0i-QU5eV5U-HNeBhQ0s4U2dGR_kPm2uuTjd9NjYB3kYTrtzsUdKwD_y4K6IO1DDRYLhuER93bXaERCSZ6jaz1xWFf5btIl9tnb5_f9WFAGfjFfVAUCx8bPNUlNibtStZJnroUOzIhEasxpskWPjw-P0t4LtEML7eMW8MIHruMLXP_OQwrPiDVOM3IaMH7kL5gLWRff35fnglI-MtxxwRcHUQucMDt3013Nw8RPjb39rL7djsAzjQxqAs3KGwMh5mfNJf2QBxPoyoGBhOdVaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هر
چهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
Ⓜ️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 363 · <a href="https://t.me/SorkhTimes/136569" target="_blank">📅 01:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🔴
فووووری از تسنیم
✅
مشکل سربازی بیرانوند دیگ قابل حل نیست و امسال یا باید بره ملوان یا فجر سپاسی
😂
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/136568" target="_blank">📅 00:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136567">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/136567" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">💢
کاظمیان + رفیعی میرن گل‌گهر پوریا لطیفی فر میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/136566" target="_blank">📅 23:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136565">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
شوک به استقلال: آسانی فسخ کرد!
🔴
یاسر آسانی با ارسال نامه‌ای رسمی به باشگاه استقلال، به دلیل پرداخت نشدن مطالبات فصل گذشته و پیش‌پرداخت قرارداد فصل جدید، فسخ یک‌طرفه قرارداد خود را اعلام کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/136565" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136564">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❗️
❗️
زارع به اردوی پرسپولیس اضافه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/136564" target="_blank">📅 23:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136563">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JT-3ippX2Vbf5bGesPSZh3ezEYRcRLep8RAHGMQ507ynHbjKdE5ioiydH1R1e0OcSQIca2R1wODdWgifbksUJBjtxH0xqLYlIeI4nza9a4u_r6IbqO86mArAqRZcF2r6hOX5pWSpCQgxqbPh6mRJ4flrm3d01XA7mVFF4GxwpH5gLaUnxw1H2q4hV7g-pDlHKf8F9SpeUNfbx2Wl41ccx4iuwJfvypJsC4OIfjOK1SZ_fJ3Uyqv_iA6sDloDPG8UTCXuKg92Jatm3B60UyZgqfCwz4FaLK2ZBsT3bnmBoXO_XkPwKRRN4zZxtJbQyimpmjbw2pEdHLLgQRuSVaLUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
پرسپولیسی‌ها نخستین جلسه تمرینی خود در اردوی ارزروم را در سالن وزنه‌ پیگیری کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/136563" target="_blank">📅 23:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136562">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/136562" target="_blank">📅 23:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136561">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
✅
رضایتنامه‌ی قربانی خیلی سنگینه و کنسله/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/136561" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
رفیعی خودش قراردادش رو با پرسپولیس فسخ کرده و حالا دستش بازه هر تیمی خواست بره. احتمالاً هم راهی گل‌گهر یا شمس‌آذر می‌شه و اخباری جاش به پرسپولیس میاد.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/136560" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/136559" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/136558" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/136557" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA-KnQTwQ-FW45qnbRjZGa_aucW-bWfmbubjwmDm7Qut_AQXGoKegYfqtYMS0dhJaQV4sRqnF4a3kt8RHqbd_q9zqBd_M3bHzwafD4L0f40odHMEzk0J0kHsufTNNtDcN2hl5mKwNy_eqDA9yYXxRUdPkLXWdoJy6LbMLBWDB17SWui7VLF1u8jaSGofSFjnA586tyK8B0i96W-1-i0B7ONlzE650V2mS08vTxI7UbGqhobH42VqtyqeRFiiUmZvV3t5Hmqz_MlZkYidgLTUXj10QGtBgtJ2-kVoIMIHkghw0gPBLiCYtOSRQJubYMyKoZBEPb_uFYmvW1eUvXwuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/136556" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/136555" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
مرتضی و کاظمیان با تیم به ترکیه نرفتن و جداییشون تقریباً قطعیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/136554" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/136553" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136552">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
جدیدترین آپدیت اندروید اپلیکیشن 1XBET
🍏
برای آموزش ثبت نام مخصوص کاربران ios اینجا را بخوانید.
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
بدون فیلترشکن
از اپلیکیشن استفاده کنید</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136552" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136551">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCJ9h8otFpJfFGNZuhnw_AR-svOaTDAuOqT15OtGgCHfyHAYVKtwTHEnoC5s5-9GyJbT2YfymQ9hymujbhQnaBh_qGxeo4m5yQZ_nUp87zP9dLUMrSYOJ0Yo33n2wWM6BJnSo0Ao9zQkKyTX6gJSmW8dlijf3_4UeKcb3cXj4jWp_rJPtPIBWlTQ4dxwIpSKjqH-xZ_qGcrbPIIAnUJEr9-evyR__U5FxSNRdWMcY670yJTBQOvp4hwn7bEH0-yTwr--fXawM8De2VyRPRJfVR2wU0isUCZ-RJAPiw9Xfd5UbNNpBFKsMQJPtOaBAcU3PTkuJRBPZOl3JsxhsLUxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
شما هم به خانواده
1XBET
بپیوندید
1️⃣
🏁
جام جهانی تمام شد... اما هیجان فوتبال ادامه دارد!
⚽️
🔥
🎁
پلیر ها پس از 5، 10، 15، 20، 25 و 30 روز متوالی، پروموکد Freebet دریافت خواهند کرد که تا 7 روز اعتبار دارد
🔔
آموزش ثبت نام و واریز
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🛑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/136551" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136550" target="_blank">📅 20:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136549" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1w0NSHRza-53HRMHMIIJcmR3sb2UWVLLJaqIMDdNTNy4kPhS8wQrePd33O65HuiFZxML4EM6TZulW-eygZUiHIW2Rt0TaC3avngOWa1dVFGXs4o7NldElxWU0Nc7gv9t-7dG3Ui9j_tiO54g9FG9P9R1eisA6YO7KeDGx9ja6vrtDZRUvMRr2zpSKzxhkQTe8rNQeaxqqh7Q2i1NYMtrMqv6eF3Q630E25_bsA4fyPn84DqVK-2SDQLpw-UsYwT7s5Rnrz3aR1bY-1xKAbTz7D6MUziCjyht_lYNETxq1zdMCzhTmoctQN-8pb9m8DasStsyyx4U3feDrOefR3rpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136548" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/136547" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136546" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_C1r2cRguRy-pXzbUu9Z9WsRckZl_GflSNO5N-0C7vUa8cfm09kZ-PGYirfI9qJm2U2ZcSTVwT4DYPw0Bzw4YvG9WxmUurm6DuqI_umDTo_9eXrtGazYtBY1HRCzQ6lM-8lZhYAH0qYsIQNswKT9gAJGu7TvXdjSNZcaosiVJxxOTj5OzzpQEPXZXRXvzDmwTU7PtUIV2wB6tYjgIwTRewxt4f3xvOiUV9iW0q61F6kr1U5D9FTit6d0NEnPta4fANyN6EuWXbStyyTJt2NT2AJC9wZWcqdfQJ5mTOvdyxDejkGEE-lWFSwR5LGojJSulbMFBBdTRiRp3KHw4Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیپور تنها بازمانده نسل طلایی برانکو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136545" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=Y11cOZXbEpkiuntUla8lffCiOP-YGKX8pIziYD505AN4e3nvIstZKpJlM3rrXaJNdjDBOIESufb811VJAxrFSt7PsGTbvlBYWXZ-5vCrNojYpXcNaDjziBgKIGZzFfTnuCSHtDpUN22RXDtBcV3PRTfhVe8iXIK-N6prZT1k8cpVHdHnM40zQsTRlJoWZqSJN-hTCzqJ1fhMkoj1JNgfCoGJV-GBoXt9bDMzVxYHUi7fwMfUKRsPFDXJbfWgxp7ruohuTN3GkrPanAtzsWSrWdzxUrIDg2B6tBH9lzZPn3-yqRwC-0Nn5xTWknqsfqyoE72DPsIHFq2N2jh9M2g8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=Y11cOZXbEpkiuntUla8lffCiOP-YGKX8pIziYD505AN4e3nvIstZKpJlM3rrXaJNdjDBOIESufb811VJAxrFSt7PsGTbvlBYWXZ-5vCrNojYpXcNaDjziBgKIGZzFfTnuCSHtDpUN22RXDtBcV3PRTfhVe8iXIK-N6prZT1k8cpVHdHnM40zQsTRlJoWZqSJN-hTCzqJ1fhMkoj1JNgfCoGJV-GBoXt9bDMzVxYHUi7fwMfUKRsPFDXJbfWgxp7ruohuTN3GkrPanAtzsWSrWdzxUrIDg2B6tBH9lzZPn3-yqRwC-0Nn5xTWknqsfqyoE72DPsIHFq2N2jh9M2g8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
استوک صورتی با کیسه فسخ کرد
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/136544" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_aFjZBo5ow1d4T4-Umj7RB4zOHKLHeH9kVYxmIZk1TsMR-nBnqOIq1Zf03pvOX1UcK1_GfMujRQvGtYJbVu9vBW7AFIibfKZJlJL4apIg76fF0G3lIOuMY27kOlL7JzRkBAawGOi4M1T7VyJQaYigJaisNOuXwr5putPsUIOpnwWaCXUb5suv_3kle83xfCqZtRA_uFiDaOqFZkoCeqAkA9JFMranl61ymszF3ZN6jHbFxZz8hvZvUXXfrMYHPgb6rjY1i7aTnZXH0UnpASiPZWAfBiteYEyU7gx_PG-6W8LbSLt04EGG4JDya7tqMlb-cu3eBlggAO4nGTlF8nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از تمرینات خبر رسیده پویا اسمی کاپیتان ۱۶ ساله تیم نوجوانان یکی از خوب های پرسپولیس بوده
🚨
این بازیکن در این سن با این فیزیک و قد مناسب شدیدا آینده داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136543" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPwTDtBCdzV4wuBbkYBThoV0fjdNB7hAEtEJ8JmSkVyB6ZrkWlRmnU1C2V9l3Jve7WYZaP1Mr-7FdlkVLfNjafKubJgWmkoD95DL8GrzPAqUyx6tFU1PsLsm2I69k06DGGlTUoEPv3PIWo2kCP-rjUJ7sHRQbXacGtmB0KGhGHDvYO_HRoTHmi4I-L5WvGIPbVdevHWFmhuwgyzQpkOSUosxmGQuK_nA2diITinsgmw51Z1z_bDgS25e8d3mApqrX_J6bkMmyCInipxjJ21_MFrqlF0uhX1RrAfSlFFOzqaNd4tcym-CkjPIxdeBoiTytJj0m2U7yMgEcmjm3TS8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136542" target="_blank">📅 17:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/136541" target="_blank">📅 17:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136540">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbgT8NKlDPVJcgKi0ps2f7cRQbGMB5FVn0FKZYoeiz_VYOYmhf41bTLYQKvNIGgQDtFCBQWYLdHNjBEkcadpaRkbAG4yRrQc6I0QG2Z_d06ruVJTA4p_ycvRq2FVHpmPvwcN9EQ-eNS0bfTpIog6g8QKD26lpYRbEL6ldbTOZm6AWIbsmER35vhmUNhnoVLf0_SyKozE0p6aGHNVxnukeuohmyfQiAmiupHL3PYFrrnCeQJnz3AWxsa8lA_-XnbDrJz1CQdSll0KDV55K3WMLn37sVdAMFwrpHqswR6wePOIJw50qSSqEtZKijHDWsWKVcjbO4coq9SXNg8gtAg0JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم رفت ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136540" target="_blank">📅 17:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136539">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=kv12tGhL9Sf5yiVJXfip4sSbOyPqaK3dRVG203zxqdG7jyuGx-NjINvnFu9a1clTRf6jHVGcdsvCw0BOMFOxsL7_YCnW2D7lKIyU3SUsNKjHhNQ9KW6o2xvYsWyay-EzkOhBFHLO7fRJq7FSV8Bz-L1J_BjEXAttSx33P8O4zW0Wn17WhO55nNMBggu0ayMN9mur0Es9m2tyOiUhX4ctmgCvFFclUN_r3rTeW92jO4l8vaKVUu4wxm4SerQRAl8b780OvSk_gnzWEK-2TK1L8t_bfhjiTXm6vVhwBaQmVZeHkHH98EBVDqX2dKIxFYubxMkobZIbU6PZWb1_49ri7WxoG_jb1NXYy3y6pfZBaWiO-USEmVDqfOQPGl8MPpLg-M38wz3CBfh4x8_WXUnkBigXDabZbtDibjoJtW1kwD_2e_AdoYvdpNnzhbeSQQzcjXH20kyWCwnFy7SGWcNVLYhwZoyMoJ6DGDo1eb-v59x_ioWrymj_6BshMoUik09PUDeXSo39TCdnvIBR5_Bni4Sds7Iox1z9u1Cr1iU9o9rzBqSEbxGlcaDWKfhsVBx-5WGnWD6FZ4QhkTzQNOPub6TmG77dHc1T0rdRyVaEenaIRo1X5BIuRM6mNs91DgcHMpbwk1xHJ-4UC-PAMlKGOfb6-X_L2OqHqT0nCjcj_Ik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=kv12tGhL9Sf5yiVJXfip4sSbOyPqaK3dRVG203zxqdG7jyuGx-NjINvnFu9a1clTRf6jHVGcdsvCw0BOMFOxsL7_YCnW2D7lKIyU3SUsNKjHhNQ9KW6o2xvYsWyay-EzkOhBFHLO7fRJq7FSV8Bz-L1J_BjEXAttSx33P8O4zW0Wn17WhO55nNMBggu0ayMN9mur0Es9m2tyOiUhX4ctmgCvFFclUN_r3rTeW92jO4l8vaKVUu4wxm4SerQRAl8b780OvSk_gnzWEK-2TK1L8t_bfhjiTXm6vVhwBaQmVZeHkHH98EBVDqX2dKIxFYubxMkobZIbU6PZWb1_49ri7WxoG_jb1NXYy3y6pfZBaWiO-USEmVDqfOQPGl8MPpLg-M38wz3CBfh4x8_WXUnkBigXDabZbtDibjoJtW1kwD_2e_AdoYvdpNnzhbeSQQzcjXH20kyWCwnFy7SGWcNVLYhwZoyMoJ6DGDo1eb-v59x_ioWrymj_6BshMoUik09PUDeXSo39TCdnvIBR5_Bni4Sds7Iox1z9u1Cr1iU9o9rzBqSEbxGlcaDWKfhsVBx-5WGnWD6FZ4QhkTzQNOPub6TmG77dHc1T0rdRyVaEenaIRo1X5BIuRM6mNs91DgcHMpbwk1xHJ-4UC-PAMlKGOfb6-X_L2OqHqT0nCjcj_Ik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علی علیپور: از آقای قلعه‌نویی تشکر می‌کنم که شانس حضور در جام‌جهانی را به من داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136539" target="_blank">📅 15:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/136538" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO-eivx8u_ByB3OFMs4iPb566Cpf8R4svgh-_IFyCYEugHI9OdHXTdByVI3M2h5Owq1mziiRUc-_h6z7-0yYuP-ZCTOIKrdIk7SaL2dTHINeSwOB7xAiAtCQOUaFLIWodCs2_bmDCUMBP7EtxxlRvu5x3EY5uptuy4JQFlKD4gGtXFG3cDyDW82iOyv74GGwv-GH2b_3iivnw8drs9c0WcsLBH4oz6Is9K16XdXjcJBF5qyGk5EmM3fCJp5SOjfqz5q7YMXry7nz7nSjpMnlA8I7fmWBFAARXwcAsrQhH-SbBxnep4dyoKWNPvX39zKui7btjqo1A9k1vw8tnTc6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پرسپولیس امروز برای برگزاری تو این کمپ زیبا و
اردوی ۱۲ روزه راهی ترکیه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136537" target="_blank">📅 14:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/136536" target="_blank">📅 14:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه:  دانیال ایری و کسری طاهری از نساجی به پرسپولیس پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/136535" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136534" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/136533" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
با نظر مهدی تارتار ، محمدحسین کنعانی زادگان به عنوان کاپیتان اول پرسپولیس انتخاب شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136532" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136531">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136531" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
پرسپولیس انتخاب کاپیتان را به تارتار سپرده؛ احتمالاً رقابت بین علیپور و کنعانی است.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136530" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/136529" target="_blank">📅 10:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwmN80CzaMS4qvCFnv_oeZLd9nGBuXI49jN7UMAD-ncXnrsYG3XCpNDtTIpVFfKdXM2IqkcRTvDJ56E21dRgO42oqbgWJnMbNYSl39IC9TNDIbP3pMn9V3iZypodNCqKqlbSdve1xoK1swUHIpCpRQyF4apVOeCmjrWG9DvNlrsjC9tODiF8AhAaBA6uqQDxz0rPb9AcBEklfLugY6yL5tVF2pkAlEvVI1AXoLo5PBcVT_3bj1lDE3YlnkmB9tBPAaqbEQtVz2FpGK3um_iXf-YBFDgQGswgVKAbuTCLpJE_125nSzO2Fuaic8hy3eyfT7N9Jj7JmchIY9-9DxLQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خط دفاعو ببین پسرر
...شیر پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136528" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g5iLjTo-zLh3LNOAi7jEiVE740naHkctospRrCBWzCRz8rst5WLRyGpdxl4zV9jU4OkoShQId-UduWZrdGTO-mkuftFQYmpkTwmuHxJDrjbkU23Yzhv_TCXuSvowOr7LCI5OaPfX4bxh0JyEXhLK02VQPR6Y50WooHYZVjvTd-r_GReez9_YrhopmOMvHngxUkBHm-avqxg_XrOd9AVZTpR6Qp4xu1ZRKNSU04-PObLVbUVrdBHLGogD_0ABS1Hc7CyZYP61-FjJI3ChjO_9DIpxLEqhyntTAPPgghlSwbY3cEJWtgxHP4t8eWsRdzQaoOJhbQA5j-rxhiner9j05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باراک راوید خبرنگار آکسیوس: یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
❗️
پ.ن بیچاره مردم که دودش فقط تو چشم مردم می‌ره این جنگ ها و حملات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136527" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQqJbCxkikcLRN2T-v58OWxNLhmaKmOUQ6EB4kzJDv9birVHL3lVNGGtdl_-HzbKAFKWde6sRvMoWtXkGALew3mb54UJrvSW7TLsmL5DcoIOoxBE1G2F3_pNvfN2_n5zRzePj7zcZQsnQKn_DYf3iHfM3r6BzVlJcLdlfdcL6QUMCCwzCfrgC0HS1kKkN19zw9jHnufJagqaCcfbMdMHOWFAKYSGG9GR7WnEhZVmBQTqv2TLR0_KPABN_ktuQqzrwfcHn4HLdhHtSAdz1-x21f_409em3kX1D673-x-KK1HhOxqpQYyUQC5susKfo4CvY38R09wwRnKylZ3aFx-eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136526" target="_blank">📅 09:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
کسری طاهری و دانیال ایری طی 48 ساعت آینده قراردادشان را با پرسپولیس امضا خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136525" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136524" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136523" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXsVSSJCD-dz2OZ5I9WcPqTu_6X4OFbjGE0bXud6SugHt4DGVxldkO0E2HYe23kAU2iOMOPsYYLTw03d_YZkKr7JDzEVf6LxjXtivY2Qr2LBGM0yg6Js2oUseIpQO7y4tplgHXHiESpMQPnoEa_8TnJXnG9MFARxNtcfCzi2iWMWXQFq4E8aSrNo25NWR-QliGR6vuo4gI1ItOEekhSas3LfuqfQmMJ4tMy3I2uLajeUnagOf6ZO3CPYJWY1MMvPhMkegcPWHfnnpNunsOde0731W_hGhjA_SPC4tpegQSZ5OS17DBopNvGMjXrPcTO5Y8d87Bdp_2R_q1JDC-tRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136522" target="_blank">📅 08:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136521">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136521" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136521" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDDunwhQ8-GttSW5hSI-rVz4mNOun0Ru7AC6O5DSD8pe92LCPxiv_tF3AmNh4Ak8a8kUeyhbAaffsRovHKe7l_4O4ZOFX-8VW9nNDFIVywff5mJ55axE-dmYlAL5WmMTSTBl6JhymvYoN3_cw598DlUe0Qm4Mh23GIFeQnHVyoSFLpE2qmiA92Ik014dwd6GZ6n3AtRbWLpFFNgOkBHvTPnCRcM0p-cSbclHZ8J3kmxAWXO0PNTbi9ZqPnXO-WVRbV-JkcfUGFL2IF73-5CbqGVnMP34kj_OX0GZrvzxV5wXa7EojT-RDPqM7vy-hzfCdH5jNQEygAwbHkFqNxiSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136520" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4a-Iu3LYP_0T2QRyLeZkNbwegHuzgTWyXTMU3Yl9NHdWRlS4Je49kV35CicKs96Knq-3i3wotvcMYSYowRXjQYvqv_OGUOJu638pmZVVCgo72vv-KgbEITHYsugcESTIgrIO1SnroKvWoineRtpLNbk9Npf9mry138ibzHAINIzyITo4sUjBFJpYVZOYzZwNeRz9MT9zl6B6zU5wobW0NZUF4RagjLcsXGaz2mymvAHhIPBkdLcCBId7gpJIvnVj9Ck7P8Y-ZIE44jjWZ6jJu2yUgScdf7qh69VgV3gZ-VB2atqnitnr01eiBriOcdx3yMXObSvLD7O6SGlV5tYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
درگذشت قهرمان جوان ژیمناستیک‌ تهران
🔻
محمدصدرا رحیم‌زاده ورزشکار ۱۸ ساله و از قهرمانان ژیمناستیک استان تهران که هفته گذشته در حین تمرین دچار سانحه شده بود، دار فانی را وداع گفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136519" target="_blank">📅 01:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/136518" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/136517" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136516" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/136515" target="_blank">📅 00:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/136514" target="_blank">📅 00:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136513">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/136513" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
دیروز در بازی با خیبر، جلالی مصدوم شد و از بی دفاع چپی جای خودشو به دنیل گرا داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/136512" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
یک مقام رسمی باشگاه پرسپولیس خبر امضای قرارداد دو ساله با اخباری که وایرال هم شده را تایید نکرد.
🔴
وی در گفت و گو با قرمزانلاین درباره اینکه گفته می شود مذاکرات امیدوار کننده بوده و توافق اولیه حاصل شده گفت؛قراردادی امضا نشده است.بیشتر نمی توانم فعلا توضیح…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/136511" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/136510" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
✅
پرسپولیس با محمدرضا اخباری به توافق رسیده و اگه اتفاق خاصی نیفته، امروز رسماً ازش به‌عنوان دروازه‌بان جدید تیم رونمایی می‌کنه.///فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/136509" target="_blank">📅 23:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🔴
باشگاه پرسپولیس در آستانه توافق نهایی برای جذب دانیال ایری و کسری طاهری است.
✍️
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136508" target="_blank">📅 23:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/136507" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/136506" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxFTKntRwky4jZ5j1lJElJtXO2iRsgN1b7eVKdHWri4PQOGdLrlW_JMe0ctgalJOS2PeMn69bmm5iphIsxljz2T89P9aQ5jHUTA5dFerVYxbTePp2gMKwr_i4vx5IUtj-ITbOGawH-SdGXdQ6ANxdhnX5Ub0XhRIahpKLlOjg4q09nhmzMCmU7IKARuEET5e8zNV6cHtoD1GB9-eHDjBz1Uaxuq8dfafG8O8vXtF1HPmiRvn6oTblZG9Q7LL6IcgP2I31gYUg9bl7I2cooLRrnUHMsoQmqeKEGtFncqdqNqJVwO4eh-s0Ej0V-NbyIGQQu0_Hn2U0UzeDkHs-cwgXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136505" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136504" target="_blank">📅 20:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
پورعلی گنجی هنوز با پرسپولیس برای جدایی به توافق نرسیده است
🔹
گفته میشه این بازیکن زیر بار کم کردن قراردادش نمیره و کل پولش می خواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/136503" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136502" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
تکمیلی :فرهیختگان: استعلام از فیفا اومده و مشکلی برای انتقال نیست و احتمالاً هردو قرضی رایگان تا نیم فصل + بند خرید با تیم راهی ترکیه میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/136501" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neB6NIquyKn9bQ0ZBmgrFTcFxhspCqyNEfEHuD6FDULhaF1LT5vvQqze4liGHpZp0wKbaZB-mfPuwZbv57eRTyAF6KSYKxdOU-sDkNosFZUkDhviya6TjmIByntc7y9shTUFC0aYvbLcHkt-0hM262QNr1_8yq7RyTk_aotnXVX8-Bgk6gwVmsnnQkKWeERY6yIRgPa6E1A7ZkQzZ4hmLMGwQSgnTVcNSUEX_N9SNdZfGEIwqAzItYJD2FVDWh3CNTpN0O-L1Rx0yCCG6CO-hpCpnc2dGwz5WC88HiAgXVJ6Hni4hdhKjSPIN06MLngrM7obGel0fchPetR7H4pICw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طاهرخانی:
❌
میلاد زکی‌پور با ارسال پیغام‌هایی به بعضی از افراد خواهان پیوستن به پرسپولیس شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136500" target="_blank">📅 20:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136499" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5bDjy9KVMT42yczzVbVXHRoJeaE_YRywXCVEyULhZThVu18fGZ9_wuqn_0JbOhP2lTT0oYWjygqWklAZL_rAJiGevaJZnj69kT6b7wq8LpmIhYyrgnDPMSJjrZCJzDjuocQkjqVC4FqGno9nd3w6VOehz8L7RgCqtcXt2bNYZSYwIQF751jfe6ggWMxf_-_sTbigBLNl6cTY64g9J6-FnPoD1576IrY4AmzNIwna7TNq3dzu16GEqS746-PBKjrESgsFpyMXbJVHDOGIsaayynErVZ_0HABZyr2x0eR68eJysqMgdXk-r3pK-scb7GIsSM-JvqUntQB6M3PdvX9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@ARON_TIP @ARON_TIP
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136498" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
❗️
به این ترتیب با وجود رد شکایت باشگاه پرسپولیس، همچنان موضوع اصلی پرونده محرومیت 4 ماهه بیرانوند به قوت خود باقی است و این دروازه‌بان در شکایت به دادگاه CAS خواستار لغو محرومیت و جریمه مالی خود شده است.
🔴
🔴
شنیده می‌شود هنوز علیرضا بیرانوند در موضوع شکایت…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136497" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
🚨
خبرگزاری تسنیم: عادل فردوسی‌پور نباید از علیرضا فغانی که از رضا پهلوی حمایت کرده، تو برنامه خودش دعوت می‌کرد و همین باعث قطع برنامه‌اش شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136496" target="_blank">📅 19:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/136495" target="_blank">📅 19:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
پرسپولیس فعلا با احتیاط داره از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نمیده، چون دیرتر از بقیه بازیکنان به تمرینات اضافه شده
❌
❌
کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدومیت های پی در پی نداشته باشه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136494" target="_blank">📅 18:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=qGjh-4w8fnSuoCBAPXCdLFD61wzNuVkN6olrX8XzO_UBfX0GFjnnFGrE94EVPPIMniWMeNjtEouJ1rLHWrObCATLXzwzMZNIPlDUGIRsmHRfUktIgYqU0NEv-b9vxLXwtZIoIOZNIrPm56g3j-QGUOtURCAOhSdI-4Ws8-DQFjD9Sq-q_YmwJEflC8v8Kf5vRt9ij6Sdk4PKwqdIM5Ux0PuUr2IpQiQYRfmKrliZQl0eIJw0hoTITvvZ9xWtB4c2iW_lZL5LjWURSmTrbCLexkhTm1jjR7kZ0omyV-99avvSD231jh18W4X12bIHUQLExY4K7di7Wq2acAL9RSXIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=qGjh-4w8fnSuoCBAPXCdLFD61wzNuVkN6olrX8XzO_UBfX0GFjnnFGrE94EVPPIMniWMeNjtEouJ1rLHWrObCATLXzwzMZNIPlDUGIRsmHRfUktIgYqU0NEv-b9vxLXwtZIoIOZNIrPm56g3j-QGUOtURCAOhSdI-4Ws8-DQFjD9Sq-q_YmwJEflC8v8Kf5vRt9ij6Sdk4PKwqdIM5Ux0PuUr2IpQiQYRfmKrliZQl0eIJw0hoTITvvZ9xWtB4c2iW_lZL5LjWURSmTrbCLexkhTm1jjR7kZ0omyV-99avvSD231jh18W4X12bIHUQLExY4K7di7Wq2acAL9RSXIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136493" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
#فووووووووووری
🔴
پرسپولیس در آستانه جذب دانیال ایری و کسری طاهری
🚨
پرسپولیس از فیفا استعلام گرفت و فیفا اعلام کرد مشکلی برای عقد قرارداد وجود ندارد
📰
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136492" target="_blank">📅 18:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136491" target="_blank">📅 18:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
🔴
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136490" target="_blank">📅 18:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
ویدیو باشگاه پرسپولیس برای خداحافظی و تشکر از کمال کامیابی نیا
❤️
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136489" target="_blank">📅 18:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136488" target="_blank">📅 17:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
🔴
تیم فوتبال پرسپولیس فردا برای برپایی اردوی تدارکاتی ارزوم ترکیه عازم خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136487" target="_blank">📅 17:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فووری/منابع عبری: ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/136486" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136484">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
ترامپ:ما اصلاً کارمان با ایران تمام نشده است
🔻
ما در حال حاضر قصد ترک خاورمیانه را نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136484" target="_blank">📅 16:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136483">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136483" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
دیدار تدارکاتی پرسپولیس با نتیجه دو بر صفر به پایان رسید و پرسپولیسی ها با پیروزی به ترکیه خواهند رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/136482" target="_blank">📅 16:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136481">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136481" target="_blank">📅 16:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
فووووووری؛ با اعلام کاس، شکایت پرسپولیس از علیرضا بیرانوند رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136480" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
شکایت پرسپولیس از بیرانوند و تراکتور رد شد
⏺
دادگاه عالی ورزش (CAS) اعلام کرد شکایت پرسپولیس علیه علیرضا بیرانوند و تراکتور به‌دلیل عدم پرداخت به‌موقع هزینه دادرسی رد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/136479" target="_blank">📅 15:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136478">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
ارونوف تحت شدیدترین محافظت پزشکی
🔴
🔴
پرسپولیس فعلاً خیلی با احتیاط از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نداد. چون دیرتر از بقیه به تمرینات اضافه شده، کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدوم نشه.…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136478" target="_blank">📅 15:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
بی تفاوتی علی دایی درباره استوری بیرانوند؛ فقط سکوت
🔴
🔴
علی دایی صراحتا به دوستان نزدیکان خود گفته است که قصد ندارد جواب علیرضا بیرانوند را بدهد چرا که اصلا او را در حد خود نمی‌داند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136477" target="_blank">📅 15:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136476" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136475" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
امروز ساعت 18:45 دیدار پلی‌آف مابین صنعت نفت و مس رفسنجان برگذار خواهد شد تا هجدهمین نماینده لیگ برتر در فصل آینده مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136474" target="_blank">📅 14:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=Gb85329nm4eYf56smeGKEPF3Wp8Xt4QvhKXH_QYDRI_uOj8GizHXBUt37JKisZf7uHb9T21XQh--ekVWmhb_pd3w_HI5mVMBOrJEupruCzuR7wQ_AtazFd97joPfPkWdvRiMYWnBHvGI7P7Md9Y5mnswU1mGshWfdWwYd8EfEZF-s2SFoqbmS5932clG4FmRgTWADscsaZN1HTe7UnvxrNEfe8JALNZkB-TMr8yNA6D5Yp5QBFPW5D4RaKTHz-ZM24sZbQ0z8s2-CGvgCofE4-1DxJXJUEb3i40O4IH2WKfC3eFohZW63SvHtn8E3El8uSJ5Gs4CUmQ_Yf5Pwg1Wdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=Gb85329nm4eYf56smeGKEPF3Wp8Xt4QvhKXH_QYDRI_uOj8GizHXBUt37JKisZf7uHb9T21XQh--ekVWmhb_pd3w_HI5mVMBOrJEupruCzuR7wQ_AtazFd97joPfPkWdvRiMYWnBHvGI7P7Md9Y5mnswU1mGshWfdWwYd8EfEZF-s2SFoqbmS5932clG4FmRgTWADscsaZN1HTe7UnvxrNEfe8JALNZkB-TMr8yNA6D5Yp5QBFPW5D4RaKTHz-ZM24sZbQ0z8s2-CGvgCofE4-1DxJXJUEb3i40O4IH2WKfC3eFohZW63SvHtn8E3El8uSJ5Gs4CUmQ_Yf5Pwg1Wdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136473" target="_blank">📅 14:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136472" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136471" target="_blank">📅 14:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136470" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136470" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
