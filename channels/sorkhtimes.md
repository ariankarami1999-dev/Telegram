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
<img src="https://cdn4.telesco.pe/file/O-t1YSIPhP7zsgQaoqFWtpnbuxTGgDnmpuBfgh-HapyjnoG83LkaXzmEabjW2c8nNKzDWtsCZJmji8ReQ5mF9v0zPneLGDcozCvG8xhbJDF2YINzCVmRQymJKxKvV14FgufuVsafoGMdmkqrlW9phKGUxfplZKulpccrUcMFbkp7aiuewpTs6HDDlhyn1fFpBwt0V1NVMZjz1Fq4aHrn-KCOPmtNg4Dy6ph9NtNN9XjN8II5z6gLQnl8yMSGCHr3so8VBacfNnh3gC0Hlqt2a30nPEWdT_Vl2QNiCEBIQLMAgfr-eJevd-v9M3W6ZvkowatQsrNDBDOjr-PufcjSJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 22:19:07</div>
<hr>

<div class="tg-post" id="msg-137825">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tEi9OUGhN4x4G2C0MprnQXLwX8Hk8x6WD57zDQCmf6Yu52XEdynCwyvVWz8XwRymO6TbP_uz0yTiYHJZqaSY8SntcGsZYIMVpHQFxM33WSu6ukBxXWHkCsagqwSsTmkL_Pnt3QGQuUzichaFb44791aszHgw0odzF9rPw8DWz-l3LLfpP3_I4JMP8Lf8xhlSeFQKC6PPjCnGSrKxij_vsqJ1uPRS6SXNHvXJ-DXtF7R7B2WrYTpqhdRCureFSdbHVYAu2mBKESJN2QPhEdAfWgLe7IEiD0TC-Se0W1afj5eMGrtz--43VdF-kXI6EJmqaY30szQEDpFZhSAQHy8pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یا الله بسم الله اسماعیل کارتال ...
🔥
❌
پ.ن چه تیمی داره حاج اسماعیل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SorkhTimes/137825" target="_blank">📅 22:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137824">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
مهدی تارتار هفته گذشته یک دفاع چپ خارجی به باشگاه معرفی کرد و اعلام کرد قرارداد بیفوما و گرا فسخ بشه اما مدیران باشگاه پرسپولیس به این نتیجه رسیدن هم بیفوما و هم گرا بمونن
👀
‼️
📰
قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/SorkhTimes/137824" target="_blank">📅 22:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137823">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWLOwAQJTwd0OPr0_0mdaZtyh6LVAT0OWgjPJOgyk_5CNeciYsqzg7ad-X7WofS9Mn84QFBSRoR6kpurNg_8YTbG52K8fl8faE_BF0u-cVpwqhLAhN3vVVPF28rTpT564KX5fb9QtjzPYXtVNhpRVvPNv5oV1sUpb9QqT0TJstEiN2FU9ogmO7WZnssV87kyX7xHp02HmlId0KM-b3_9N5_0rmDjNFIsgkm7hEIrGwqwhNFK3awh6LDs5Pde8-9BqeyvcGimja3hict0dQwekcSMGyhYncpl69S2GCsUPvvYiSnwS-xane3xx06NI7NYA6VHGod3DxujqZ8ty-GNSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
🤡
نرینی یه وقت سلطان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/137823" target="_blank">📅 22:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137822">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چراغی جان با تمام احترامی برات به خواطر رزومه این چند سالته قائلم ولی هوادار تصمیم میگیره تیم چه نیازی داره و تصمیش رو عملی می‌کنه  زمان ثابت می‌کنه  جلوی فشار هوادارو نمیتونی بگیری عزیز</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/SorkhTimes/137822" target="_blank">📅 22:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137821">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirmahdi</strong></div>
<div class="tg-text">چراغی جان با تمام احترامی برات به خواطر رزومه این چند سالته قائلم
ولی هوادار تصمیم میگیره تیم چه نیازی داره و تصمیش رو عملی می‌کنه
زمان ثابت می‌کنه
جلوی فشار هوادارو نمیتونی بگیری عزیز</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/137821" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137820">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🙂
🤩
ایری امروز داشت میرفت اون تیمه ولی یهو پرزیدنت حدادی و احمدی سر کیسه رو شل کردن…بسوزززززید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/137820" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137819">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
❌
حدادی یه قربانی فقط همین ...تمومش کن دکتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/137819" target="_blank">📅 22:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137818">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🤝
🤝
🤝
قربانی رو بیار و بهترین پنجره تابستونی تاریخ رو به نام خودت ثبت کن دکتر پیمان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/137818" target="_blank">📅 21:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137816">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
❌
تراکتور و سپاهان با زدن نامه ای به فدراسیون فوتبال تهدید کردن که حق ندارید جام قهرمانی رو به استقلال بدید چون شرایط جدول لیگ پارسال خیلی نزدیک به هم بوده؛ در این صورت ازتون شکایت میکنیم./ آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/137816" target="_blank">📅 21:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137815">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⚡️
⚡️
دقایقی پیش جلسه مهم پیمان حدادی و شهاب زندی برگزار شد و طرفین به توافق نهایی رسیدند/ایسنا و فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/137815" target="_blank">📅 21:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137814">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔄
🔄
فوووووووری
✔️
مهدی تاج: ورزشگاه آزادی نیم فصل دوم در اختیار پرسپولیس و استقلال است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/137814" target="_blank">📅 21:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137813">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/137813" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137812">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UizzsszcpUnMqUKjmJYi2PUGIn9HpUVYvgHIJTCZ4bm_tzqxG6TXgNxP2hyTyQeTOjoaglfboRITVy5bnfpkkHABOoqcrMSuZwG3WpbL9OHksQfVZv4dZhY0uUHS0ILDuEjyKGRMcuR_2RYsyn4jrp4TXo0CNXaAjtX-c57DLRHB6k8g-lRxzo8gP4UZjR_OqB3q71CeeBfm6YvhP561DgaZsoQ8cdPreW5lYlj7UYfQiu-b0EYLkDPZ--MzBLjzOlJC9bfsb0Ix8H9KKEGIu4h4TDK4XAjIQRsr0K61OWj769OH44byWxXgH3ohbZMtRRUrRJjkyw4IZxBctuapYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوووووووووووووووری
❤️
دانیال ایری با عقد‌ قراردادی رسما و شرعا به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/137812" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137811">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
🚨
قدوسی : قرارداد دانیال ایری فردا امضا میشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس   @SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/137811" target="_blank">📅 21:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137810">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3j8lkEuZHudGIteN_puWosE3C1oLGLfhqtI45ARIDs5OwwyKhVd3y-g-NiSxcyyv0uLr9o3xQH-ZZsk6xI4TBV28tK6398nzbzIyCF3BKvzTPSbW-i2rXbEa16QZlzpMtUwwUqRja27UFBwo74ANcdkehbL06MRz9qg1RnKR0V-oEGTeyICw9B-paCMBXoz7SJCFjESs7U-8pDi94fvV_imkm4gbG9QvWAMJ9I5JmKlSIyx8K7DfMOIrgrHRaQlXsVpjsENb_qvVtAXC1-H2cDhah1xp0NsjCcaUlIMSwmOhnL2hAvyOy8iZu27l78DnSRYYC9jDhp5zeEVsZp7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بازگشت سرخپوشان به تمرینات بعد از یک روز استراحت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/137810" target="_blank">📅 20:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137809">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc676823cb.mp4?token=o2fIbXQ0pSsnIClP259f1w1tobwf3ozJve7QBwTiV0geIA_aBZ-AoKWvNw0-dsFuYWYjRvBrUA8EcWFr50Ok7_bPa7Qt2i09wgRXNIhhrEG9qrmmUtkRVlse8XXybSTZWFP2chJ8s5aIG8H1uqKH8C2OiDa5y8oGdOh4eV04BqN12VIwVJcvrj4FwKSjPbwru4C38s-YCSLl8fTAbbWZ2pwbfC89A7s2snvSB_jQ8mfNxwsw0N-5OCUVMjV-5DK9O1d1IUbHI4-JgBunOwJogck3EZ4ylX8vSMr5hEUPshQBoGMPAMeKxSg6lbCvQ-y5SDpe83j19MIiiXt1QeDMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc676823cb.mp4?token=o2fIbXQ0pSsnIClP259f1w1tobwf3ozJve7QBwTiV0geIA_aBZ-AoKWvNw0-dsFuYWYjRvBrUA8EcWFr50Ok7_bPa7Qt2i09wgRXNIhhrEG9qrmmUtkRVlse8XXybSTZWFP2chJ8s5aIG8H1uqKH8C2OiDa5y8oGdOh4eV04BqN12VIwVJcvrj4FwKSjPbwru4C38s-YCSLl8fTAbbWZ2pwbfC89A7s2snvSB_jQ8mfNxwsw0N-5OCUVMjV-5DK9O1d1IUbHI4-JgBunOwJogck3EZ4ylX8vSMr5hEUPshQBoGMPAMeKxSg6lbCvQ-y5SDpe83j19MIiiXt1QeDMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
پاختاکور ازبکستان 3 بر 0 الحسین قهرمان اردن رو برد و به لیگ نخبگان صعود کرد! بشار رسن، هافبک سابق پرسپولیس یک گل زد و یک پاس گل داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/137809" target="_blank">📅 20:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137808">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jn-HMyhH82GXlaS9YVfRckZCFcckhGHPi36kBOivXaXJQPRvh6xRx8qNfvTihWNFoy-TVq8jjkX_qurflF8QLkaBcwZm5CnGUUMMh4jvxjDZKJTIEh4Ak-19loYnyaFFLbuTMIRBg1wVE03dlhD-qwZWPNTm0LDFu6fySC9GA4b658b1M5a7pAo7iqryuvx6YFAQ17R49ZCMvLf_RJdszzg57t2vHKLpsZiAXlsPFpXP6gJCMa5mfPLuiWeyCcCeU41Cdg_CZtLtS9nQuLfyr96CWsTwa9xFjsrqCXMHSjhoWAF6r5NElYwvuqqZQ24K_iuSqUNcZKvRINdtiHNLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لیون برای جبران؛ اسپارتا برای حفظ برتری!
🔴
LYON -
⚫️
Sparta Perague
⚽️
لیون در خانه به دنبال جبران شکست ۲-۱ بازی رفت است و از همان ابتدا باید فشار بالایی روی دروازه اسپارتا وارد کند.
اسپارتا با برتری بازی رفت دست بالا را دارد، اما حفظ نتیجه مقابل فشار هواداران لیون کار ساده‌ای نخواهد بود.
انتظار می‌رود بازی از دقایق ابتدایی تهاجمی شود و هرچه زمان می‌گذرد، ریسک‌پذیری لیون بیشتر شود.
یک شب سرنوشت‌ساز در لیون؛ جایی که یک گل می‌تواند تمام معادلات صعود را عوض کند.
📌
در وینکوبت ثبت‌نام کن و با ۱۰٪ بونوس اولین واریز دیدار امشب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/137808" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137807">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔜
🤩
سکوت حدادی معنای خاصی دارد! منتظر خبر خاص یکشنبه باشید
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/137807" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137806">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
بیفوما هم موندنی شد و خارجی جدیدی جذب نمیشه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/137806" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137805">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
✔️
✔️
پیوستن رامین رضاییان به پرسپولیس شرعا و رسما کنسل شد
✔️
آنا
🥈
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/137805" target="_blank">📅 20:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137804">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">⏺
تفاهم نامه سه جانبه پرسپولیس و نساجی برای جذب دانیال ایری فردا امضا خواهد شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/137804" target="_blank">📅 19:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137803">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/137803" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137802">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
✔️
ورزش سه :توافقات انجام شد و دانیال ایری به زودی پیراهن پرسپولیس را برتن خواهد کرد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/137802" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137801">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
قدوسی : باشگاه نساجی به پرسپولیس‌ تخفیف داده و مذاکرات پایانی در حال برگزاری هست  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/137801" target="_blank">📅 18:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137800">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
گرا باز هم زیر بار فسخ کردن نرفت و چون ۸۰ درصد مبلغ قراردادشو خواسته باشگاه نگهش میداره/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/137800" target="_blank">📅 18:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137799">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
مرتضی پورعلی گنجی با عقد قراردادی به پاختاکور ازبکستان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/137799" target="_blank">📅 18:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137798">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
گرا باز هم زیر بار فسخ کردن نرفت و چون ۸۰ درصد مبلغ قراردادشو خواسته باشگاه نگهش میداره/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/137798" target="_blank">📅 18:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137797">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💢
💢
💢
غیررسمی: دنیل گرا در پرسپولیس ماندنی شد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/137797" target="_blank">📅 18:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137796">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✔️
✔️
✔️
جدایی دنیل گرا از پرسپولیس جدی شده.
🗣
🗣
باشگاه دنبال فسخ قراردادشه، ولی چون قراردادش بالاست، نمی‌خواد ضرر مالی زیادی بده. احتمالاً یکی‌دو روز آینده تکلیفش مشخص می‌شه و اگه مشکل قرارداد حل بشه، قبل از شروع فصل جدا می‌شه.
✔️
فارس  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/137796" target="_blank">📅 18:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137795">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
مدیران نساجی بعد از درخواست خود دانیال ایری به پرسپولیس تخفیف 20 میلیاردی دادن و مذاکرات فعلا در جریان هستش!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/137795" target="_blank">📅 17:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efb264822.mp4?token=KsX2zlNbVb0R7CcEzH_qE-MADxP60Kf_IKbEEJ-MRxxGAQ1u2gpI9CuAi9kWzVMxj395sz5uo3Mv9H_QXfuzKKJdWi-eHrF1tg72YqQcQB5MzGmh26nw-Xz_zuUJxReyrf1Z9V2KNJ73qZ2QelXbb8-ZxiFXMPDZdOyOplkUF7_ORjbKh_8kZ4Z4Pvurem9Yt619iGZ8v4PLL7peQ1JiHR60nKaezUfzWJ4ubVdJzYE1wHPZ_nmV6Tqc1Uc5opZ5yZAGQYh7ZoAIyaPb6KJMKlVNATySQD4wisMi8FxLcDcD0vCTJsgXGWC_SDBEwST1_jrST2B-YyF4zaxo3GJSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efb264822.mp4?token=KsX2zlNbVb0R7CcEzH_qE-MADxP60Kf_IKbEEJ-MRxxGAQ1u2gpI9CuAi9kWzVMxj395sz5uo3Mv9H_QXfuzKKJdWi-eHrF1tg72YqQcQB5MzGmh26nw-Xz_zuUJxReyrf1Z9V2KNJ73qZ2QelXbb8-ZxiFXMPDZdOyOplkUF7_ORjbKh_8kZ4Z4Pvurem9Yt619iGZ8v4PLL7peQ1JiHR60nKaezUfzWJ4ubVdJzYE1wHPZ_nmV6Tqc1Uc5opZ5yZAGQYh7ZoAIyaPb6KJMKlVNATySQD4wisMi8FxLcDcD0vCTJsgXGWC_SDBEwST1_jrST2B-YyF4zaxo3GJSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
tik tak...
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/137794" target="_blank">📅 16:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137793">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
این چهره احد میرزایی کارشناس شورای شهر تبریز بوده و یکی از نفوذی‌های زنوزیه
🔴
امثال این افراد هیچوقت به درد پرسپولیس نمیخورن و هواداران برای رفتن اینا ثانیه‌شماری می‌کنن
🔴
همین آدم روی انتقال قربانی هم به شدت داره سنگ اندازی می‌کنه.  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137793" target="_blank">📅 16:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137792">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⚡️
⚡️
دقایقی پیش جلسه مهم پیمان حدادی و شهاب زندی برگزار شد و طرفین به توافق نهایی رسیدند/ایسنا و فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/137792" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137791">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
این چهره احد میرزایی کارشناس شورای شهر تبریز بوده و یکی از نفوذی‌های زنوزیه
🔴
امثال این افراد هیچوقت به درد پرسپولیس نمیخورن و هواداران برای رفتن اینا ثانیه‌شماری می‌کنن
🔴
همین آدم روی انتقال قربانی هم به شدت داره سنگ اندازی می‌کنه.  «سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/137791" target="_blank">📅 16:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137790">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phlgMuGnlclSgPyMtE2N0rHaD-EzBJdAaaSZElJYjuvD8PxkXJLHQPmgRuIaYXlO9RgwgowCDBWAFvRvmIs5pMKxq4EUQeABtO6_uB2qfe0h8hIEaSXPXHYuOOeag-Rf_ygv19yHTNOoeOtaxki-rPdflBTsVHYdGnRkDUlanAFHfy5ZwzhWPxWGd4WPaDHiLdy5bh19YPkmtDzT_U9P4KBbddNxsJzr4Brji4bd4gAGgdOq0zfRIlGnEWpz2RvrS1jOWC_vkv2TxSHcmXLdOZBHQZFc0Csklc7U8GzZhpQX0-KdoJ-v1SAcWMxRFK13Y9hYnbrPv-zYwq2su-g16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این چهره احد میرزایی کارشناس شورای شهر تبریز بوده و یکی از نفوذی‌های زنوزیه
🔴
امثال این افراد هیچوقت به درد
پرسپولیس
نمیخورن و هواداران برای رفتن اینا ثانیه‌شماری می‌کنن
🔴
همین آدم روی انتقال
قربانی
هم به شدت داره سنگ اندازی می‌کنه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/137790" target="_blank">📅 16:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137789">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
❌
#فوری
🔄
باشگاه پرسپولیس برای صدور رضایتنامه دانیال ایری با نساجی به توافق رسید.
✍️
ایسنا   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/137789" target="_blank">📅 16:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137788">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚡️
⚡️
ایری به پرسپولیس پیوست / فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137788" target="_blank">📅 16:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137787">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
کسری طاهری، مهاجم نساجی که با حواشی زیادی به این تیم آمد، در بازی‌های دوستانه عملکرد خوبی نداشته و مجتبی حسینی از عملکرد او راضی نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/137787" target="_blank">📅 16:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137786">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
تارتار همچنان روی موضع خودشه و میگه نیازی به رامین نداریم/فوتبالی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/137786" target="_blank">📅 16:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137785">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
توافق نهایی پرسپولیس و نساجی برای انتقال دانیال ایری
❌
❌
دو باشگاه پرسپولیس و نساجی بر سر انتقال دانیال ایری به توافق رسیده‌اند و نساجی پس از دریافت مبلغ مورد توافق، رضایت‌نامه این مدافع جوان را صادر خواهد کرد.
❌
ایری به دیدار نخست پرسپولیس مقابل شمس‌آذر…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/137785" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137784">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
🚨
🚨
فوووووووووووووری آنا
✔️
پرسپولیس و نساجی امروز به توافقات برای انتقال دانیال ایری رسیدند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/137784" target="_blank">📅 16:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137783">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🤝
🤝
🤝
🤝
🤝
🤝
🤝
🤝</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/137783" target="_blank">📅 15:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🤝
🤝
🤝
🤝
🤝
🤝
🤝
🤝</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/137782" target="_blank">📅 15:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
محرومیت مدیر بیشرف ترتر بخشیده شد
⚪️
محرومیت یک جلسه‌ای افغانی ترترزاده با رأی کمیته استیناف بخشیده شده است و مدیر تیم تراکتور منعی برای همراهی تیمش در هفته نخست لیگ برتر ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/137781" target="_blank">📅 14:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
چه ترکیبی بشه.با حضور نکونام و خداداد بیرانوند و شجاع
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137780" target="_blank">📅 14:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/137779" target="_blank">📅 13:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/137778" target="_blank">📅 13:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
فووووووری | خبرآنلاین
✔️
✔️
تراکتور مذاکرات با رامین رضاییان رو آغاز کرد!
✔️
✔️
در صورت پیوستن رامین به تراکتور، صادق محرمی از این تیم جدا میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/137777" target="_blank">📅 13:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137776" target="_blank">📅 13:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">💢
💢
💢
💢
عجیب اما واقعی؛ گویا مدیران پرسپولیس هرطور شده می‌خوان فسخ دنیل گرا رو انجام بدن و با همکاری هوشنگ سعادتی رامین رضاییان رو به پرسپولیس بیارن.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137775" target="_blank">📅 11:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
فووووووری | خبرآنلاین
✔️
✔️
تراکتور مذاکرات با رامین رضاییان رو آغاز کرد!
✔️
✔️
در صورت پیوستن رامین به تراکتور، صادق محرمی از این تیم جدا میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137774" target="_blank">📅 11:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
مدیران نساجی بعد از درخواست خود دانیال ایری به پرسپولیس تخفیف 20 میلیاردی دادن و مذاکرات فعلا در جریان هستش!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137773" target="_blank">📅 11:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
❌
مرتضی پورعلی گنجی با عقد قراردادی به پاختاکور ازبکستان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137772" target="_blank">📅 11:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
پرسپولیس باید ۶٪ مبلغ قرارداد بازیکنارو پرداخت کنه تا کارت بازی‌شون صادر بشه.اگه امروز پرداخت انجام بشه، همه بازیکنای لیست برای بازی با شمس‌آذر مجوز بازی دارن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/137771" target="_blank">📅 11:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
❌
اسامی داوران هفته‌اول پریمیرلیگ ایران
😀
استقلال - مس‌شهربابک/موعود بنیادی‌فر
😀
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
😀
تراکتور - پیکان/کوپال ناظمی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137770" target="_blank">📅 11:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🟥
‼️
😄
دیشب رامین رضاییان وسط برنامه بلند شد دکمه لباسش رو باز کرد که بگه ببینید همه لباس و شلوار من برند ایرانی هست. ساعت هم ندارم. میثاقی هم گفت خوبه دیگه دکمه جای دیگه رو باز نکن.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137769" target="_blank">📅 11:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✔️
✔️
✔️
✔️
‏  رسوایی اخلاقی رئیس فیفا فاش شد  ‏
✅
طبق گزارش یک نشریه انگلیسی، رئیس فیفا در زمان حضور در یوفا برای مدت ۵ سال با این زن رابطه غیراخلاقی داشته و از سمتش سوء استفاده کرده است.  ‏
✅
پیش از این اینفانتینو ابتدا به خاطر زد و بند با ترامپ پروندهٔ سنگین…</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/137768" target="_blank">📅 11:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5721545f.mp4?token=mc5EBc1r88f8Bk2_DKBk8qCLXpig3zu2Bhs-axFwlTc3qN7IhsDA29oJegr55RT871IKzTjCIzQMHIJ8ehr126wbrvXCzuoqHHLDc3CzETqz-mZxvBGsZRqsDuKm1KlE7rvKR3V3ymQGBSXigZIwK3mmn9fP1fKpnBUiJ6ChbbeNewNfgcFzJDkSz6u7paoH61foqiDE2oNx6K89mqzJYeibNLEcj9PTdpnOFQCFJSChVP8hnBsm5LfVnmzkhhkkDbaR1DqPMN-RR0ngm8VmT8gRJfXzdAffNNx43Kx4HVQ2OLD-qF5uPz5jWwjVvQeT2fBL_VB4aje00LUFeLk0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5721545f.mp4?token=mc5EBc1r88f8Bk2_DKBk8qCLXpig3zu2Bhs-axFwlTc3qN7IhsDA29oJegr55RT871IKzTjCIzQMHIJ8ehr126wbrvXCzuoqHHLDc3CzETqz-mZxvBGsZRqsDuKm1KlE7rvKR3V3ymQGBSXigZIwK3mmn9fP1fKpnBUiJ6ChbbeNewNfgcFzJDkSz6u7paoH61foqiDE2oNx6K89mqzJYeibNLEcj9PTdpnOFQCFJSChVP8hnBsm5LfVnmzkhhkkDbaR1DqPMN-RR0ngm8VmT8gRJfXzdAffNNx43Kx4HVQ2OLD-qF5uPz5jWwjVvQeT2fBL_VB4aje00LUFeLk0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
‼️
😄
دیشب رامین رضاییان وسط برنامه بلند شد دکمه لباسش رو باز کرد که بگه ببینید همه لباس و شلوار من برند ایرانی هست. ساعت هم ندارم. میثاقی هم گفت خوبه دیگه دکمه جای دیگه رو باز نکن.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137767" target="_blank">📅 09:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
بازی های پرسپولیس در 3 هفته ابتدایی
🗓
شنبه ۲۴ مرداد
⚽️
شمس آذر قزوین - پرسپولیس
⏳
ساعت : ۱۹:۳۰
🏟
ورزشگاه : سردار آزادگان قزوین
🗓
چهارشنبه ۲۸ مرداد
⚽️
پرسپولیس - استقلال خوزستان
⏳
ساعت : ۱۹:۳۰
🏟
ورزشگاه : متعاقباً اعلام می شود
🗓
دوشنبه ۲ شهریور
⚽️
تراکتور تبریز…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137766" target="_blank">📅 09:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137765">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
هزینه‌ی جذب ایری با دستمزد یک فصلش حدود ۳۰۰ میلیارده/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137765" target="_blank">📅 09:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137764">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
❌
فووووووووووووری
🚨
ورزش سه: با انتقال دانیال ایری به پرسپولیس، انتقال حسین ابرقویی به سپاهان درحال نهایی شدن است
😐
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/137764" target="_blank">📅 09:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137763">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚡️
هلدینگ در این مدت 500 هزار دلار به چیواله وکیل ایتالیایی پرداخت کرده بود که هفته‌ای یه بار به تاجرنیا اعلام میکرد خیالتون راحت پنجره باشگاه باز خواهد شد.
😁
😁
😁
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137763" target="_blank">📅 08:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137762">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWIzwjyp7bi84Q-N2rJOREWgTxmNHmQ06Tu10q7g0VHv6kK3Y3UvN1ArnKOGwUuDupUidwHa_leudEtGLLRnyuo61mymO7kAsG-Sspj0k3USN1RZDy4qQsx-Uz5hGCtJDl0EGTwZcpSIgl26UbbdwPLUINZGHa1mK5yhJ3eSEYYoqaY6aYIInSw1tG41c-LJps_z8gAEckDiq4PZJ8JH8Ov1aOLvogtCH9pEdXtxjO8TyhHdPL4OLFcPXMOGS1OsKilu7D-f8jwV0QmdCG3FSOvISveiNYyarWkL8ZKPR2UJVCLNjla6MTVjNcbmoZencaaor00GZmAd1fcbfHrTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبحتون بخیر ارتش سرخ
🚩
✨
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137762" target="_blank">📅 08:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRWromiEOSErLQyLzcvjWuh-iotnAiZdN0e6eQeu8yaTXfufNhXYDojEer2rVyF3HHpvIbdx0x6pHoGuK2pUdA3aObgSDr4JxegyWHmlaUvAXjzykHChqyAZFb9BlNNRgKnZV-tqTVs0GvkN06DVaiL_3bBrodnF6lRVn98UOEJZ1n40q493v1jtv5dJtKzHFgB2n24j4lHOYYgKFMkXC_-1wz-ACcB7vPjWcb-1b4jAVCE36_aDLmIKxbHRWu1g7nirmr3aL40MjRWUMo-MwDNiryOYcKknAtDoULfCNFlApDTW9rQWtxf2wwyaNJtBJxrA7LrRHShAJGdSvtxvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
چهار نبرد، چهار داستان متفاوت!
🇪🇺
فرداشب اروپا شاهد تقابل‌هایی نزدیک و پرهیجان است؛ جایی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند.
لیون و المپیاکوس از گزینه‌های قابل‌اعتمادتر هستند، اما بازی‌های دیگر پتانسیل غافلگیری بالایی دارند.
شروعی محتاطانه و نیمه‌ای دومِ تهاجمی‌تر؛ جایی که احتمال باز شدن بازی‌ها بیشتر می‌شود.
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
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
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/137761" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSJLk6WWHk3dNHnFAeVfF6IIZfQ4dMNusg7ccsXunOfLllNezOOinRZHKmwJGlyp8_52JYDtyTX44IIcmQhrzvPqj9oF513F9tS1EsusAPl45U2YyRkhwjNulYflgDBhgUTwdak7-GJwIas5YkRFcB4hRmxSa2o1hHpjkCwQuPVevysCC-yPir5yn2G65YZpqq_SPQcAiiicx-csZL1JtYt8kiq60ibA4eviKkn6t7eml1edqd_1z-8adQJUAAVh_I-hvKMknslUo1se_dE3RZheCJzSobi03EiQBr_5_YnRoy0IExe32YLAx4yvskkhvspPG4nVupYuPyBViUnTPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شبتون بخیر سرخدلان
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137760" target="_blank">📅 01:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
رامین رضاییان مذاکرات وکیلش رو با مدیریت پرسپولیس تایید کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137759" target="_blank">📅 01:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/137758" target="_blank">📅 01:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/137757" target="_blank">📅 01:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137755">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
رامین : آقا محمد حال مردم خوب نیست جدی من خجالت میکشم اصلا راجع به مبلغ قرارداد اینجا حرف بزنم، از مسئولان میخوام کمک کنید حال مردم خوب بشه و با فوتبال آشتی کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137755" target="_blank">📅 01:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137754">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🗣
🗣
🗣
رامین رضاییان یقه باز اومده بود شبکه سه و بعد 2 دقیقه تذکر گرفت که تحریک کننده هست و یقشو بست
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137754" target="_blank">📅 01:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137753">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9uCdVWBB1SgjHBjADxMOijpNxxm4zZWUe4kWgt4Wf029tnli3lo-l_-mPD1ZilZVoZl2xj_49VlwIGfpJcDQQgpqyYCI82mL2akOjQ4EML5WM46GN9wbxPeAQGty5yeIGc-YZbBX2UeSQgGrxlVpxAoP0P_5C8tbneepu8G3I204ju-5I4xk-5sLPWGcatakdyPb6kVqBgwNoD2qkLgU_pI7E_fveaqWpvAquWdlSCC-JEO5VPHeLOyq2h3lC4z1m4-x6X2RFQb16oIXCniSIYn7eymXx7vADrNXsUUDmrtITf-ChCqujyW7yA-BgQW16xIcrlIFarfl7UymxYb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
🗣
رامین رضاییان یقه باز اومده بود شبکه سه و بعد 2 دقیقه تذکر گرفت که تحریک کننده هست و یقشو بست
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137753" target="_blank">📅 01:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137752">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/281745dbc1.mp4?token=ob2coMVlRS0FZ7xKVmJk7Vi9WRha7jbISlpg9TROdJecrTUoBevXfPGHwQ1wntOsC80T-n_gXXaOqcppzK8o_fz_HzBmcsQ6PGok6QJn239m0WooTgfSKR18EACCmGfkDEgEcPlnCMRn7Vlhv2RovE_r2bb6XSiNeaFXGnLb2ZkpV6owyW_3nW85ETj6D9GxKKplgHWFJLNT-ng4CymU0Vbsn-hq6_XqPqdJd10R6bwuQOTgIS6fF4xUaTHLLzpby42DIwUeOKeiS4TxX8IHEbvev6LkyR4_A8LAQx_rsfSzLEo28SKmdGA0cmrfVjRG1o78UKxGmpcirihSnQ5amA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/281745dbc1.mp4?token=ob2coMVlRS0FZ7xKVmJk7Vi9WRha7jbISlpg9TROdJecrTUoBevXfPGHwQ1wntOsC80T-n_gXXaOqcppzK8o_fz_HzBmcsQ6PGok6QJn239m0WooTgfSKR18EACCmGfkDEgEcPlnCMRn7Vlhv2RovE_r2bb6XSiNeaFXGnLb2ZkpV6owyW_3nW85ETj6D9GxKKplgHWFJLNT-ng4CymU0Vbsn-hq6_XqPqdJd10R6bwuQOTgIS6fF4xUaTHLLzpby42DIwUeOKeiS4TxX8IHEbvev6LkyR4_A8LAQx_rsfSzLEo28SKmdGA0cmrfVjRG1o78UKxGmpcirihSnQ5amA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رامین رضاییان: ما پرواز زمینی می‌رفتیم
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137752" target="_blank">📅 01:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137751">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=NOvtxbT6BF0pddo8F3-AxeenoecMrZDZwGZaWUxlsRQphiVxp-hZnC05ZT-JigYCROyY_weS3KZZnnFT_i9xfNHCgT0vXxxcanRRYYaa1_nC5b2JbNFSVQcH6YPuCPrBuYqJQ1GevwlKN7_hKSlZd0gPyB9_Ev4R-QaaMVMs20ynw81BR-OqTyB_HR_5qo9DoOdsB30R6AmwdTxKj9wMwX8IaeMIMF4Bq_JGxGcgN2T5XffImw1ctAPgkhnQnc3DE3hVfPMTPkgCFkAzA9X5lCLLzJOkxGrDvWd4JV5VnUTPkdc3fvnLYj6z3ReOYiDaUEuqDlUpD67BAx54CB7y2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=NOvtxbT6BF0pddo8F3-AxeenoecMrZDZwGZaWUxlsRQphiVxp-hZnC05ZT-JigYCROyY_weS3KZZnnFT_i9xfNHCgT0vXxxcanRRYYaa1_nC5b2JbNFSVQcH6YPuCPrBuYqJQ1GevwlKN7_hKSlZd0gPyB9_Ev4R-QaaMVMs20ynw81BR-OqTyB_HR_5qo9DoOdsB30R6AmwdTxKj9wMwX8IaeMIMF4Bq_JGxGcgN2T5XffImw1ctAPgkhnQnc3DE3hVfPMTPkgCFkAzA9X5lCLLzJOkxGrDvWd4JV5VnUTPkdc3fvnLYj6z3ReOYiDaUEuqDlUpD67BAx54CB7y2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡️
رضاییان : ساپینتو منو تمرین راه نمیداد
همش تو کوچه خیابان میدویدم :)))
😁
😁
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137751" target="_blank">📅 01:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137750">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
باشگاه الوحده امارات در حال بررسی پیشنهادات تراکتور و پرسپولیس برای جذب محمد قربانی است و پرسپولیس شانس بیشتری دارد.    «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137750" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
هزینه‌ی جذب ایری با دستمزد یک فصلش حدود ۳۰۰ میلیارده/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/SorkhTimes/137749" target="_blank">📅 00:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/137748" target="_blank">📅 00:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
شنیده میشه که سعادتی ایجنت رامین که رفاقت صمیمانه ای با خلیلی داره قصد داره رامین و به پرسپولیس برگردونه !
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137747" target="_blank">📅 00:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
استقلال دیگه منتظر رامین رضاییان نمی‌مونه
💢
هوشنگ سعادتی امروز با حدادی درمورد رامین رضاییان جلسه داشته ولی نتیجه‌اش نامعلومه ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137746" target="_blank">📅 00:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
رامین رضاییان: دوست دارم تو هیاهو فوتبال ایران بمونم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/137745" target="_blank">📅 00:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
رامین رضاییان: با افتخار تو پرسپولیس بودم و لوگوی این تیم رو بوسیدم، من می‌خواستم بمونم ولی اونا منو نخواستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137744" target="_blank">📅 00:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
رامین رضاییان: من پیشینه ام پرسپولیسه و پرسپولیسیم و تو استقلال یه مهمون بودم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137743" target="_blank">📅 00:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
رامین اومد فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137742" target="_blank">📅 00:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137741">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
فوری
❌
مهدی تاج: لیگ برتر با حضور تماشاگر آغاز خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137741" target="_blank">📅 23:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137740">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
💢
💢
💢
باشگاه برای توجیح نیاوردن ایری و طاهری قصد داره هوادارا رو با رامین سوپرایز کنه...
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/137740" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137739">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
تاج: هنوز هم معتقدم گل شجاع خلیل‌زاده به مصر درست بود
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/137739" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137738">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
سعید مهری : برای جلالی آرزوی موفقیت دارم؛ بازیکن پرحاشیه‌ای نبوده و به نظرم حتما موفق می‌شود و توانایی فوق العاده داره و هواداران پرسپولیس با آغوش باز او‌ را می‌پذیرند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/137738" target="_blank">📅 23:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137737">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
علی بازگشا سخنگوی باشگاه پرسپولیس:
⌛️
قطعا به زودی سه بازیکن جذب خواهیم کرد
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137737" target="_blank">📅 23:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137736">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚡️
⚡️
مهدی تاج، رئیس فدراسیون فوتبال: تلاش‌ می‌کنیم تا فصل آینده بازی‌ها با تماشاگر برگزار شود/ تمام بازی‌های لیگ با VAR برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137736" target="_blank">📅 23:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137735">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔄
🔄
بازگشا :در ساعات آینده یا چند روز آینده  خبراییه جدیدی هست که باشگاه اطلاع رسانی میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137735" target="_blank">📅 22:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137734">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137734" target="_blank">📅 22:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137733">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn3S_LAYpWAXKPksGqCfr1KJBy3zP6rfepshRsL0y45DbW6QpHblyzYT8oJiURU2yOKVTd2L3xCJTsiQzzqxNF2op0ihHzAWOZPA-Oygx0kb5u6JomGgRbuzGtTPeYRgFLf20OCu9c7ObfnJA8hjcv2qLBHyRCqeUX4FDuT3Whk30j3_A5h64jaUlXCh8EfzHxw0CRtIUXNiZqq1VBMq6A9APoYLwqZbSUH4OqDlT8vK3BeFqvnZXpuidxXMVgTtayLg6wT-wjjBwcvEtwsaq27Spb20ItcfH2kRDesLnZROAWRBmskK48c_CQjFyACXmgMVYsF2U4gl9b4Mp3AY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/137733" target="_blank">📅 22:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137732">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/137732" target="_blank">📅 22:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137731">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
سازمان لیگ باید با این تخلفات اشکار برخورد قاطع کند.اسانی هم فسخ کرده.فسخ فسخ است ولو به فیفا یا فدراسیون اعلام نشده باشد‌.تاجرنیا هم این فسخ را تایید کرده است.مدرک بالاتر از این؟
🔴
🔴
کارشناسان با تایید افشاگری های #قرمزانلاین گفته اند استقلال نمی تواند…</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/137731" target="_blank">📅 22:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137730">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
حجت موتوری: سرباز بودن علیرضا بیرانوند؟ فعلا مشمول نیست و هواداران نگران نباشند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137730" target="_blank">📅 22:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137729">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/137729" target="_blank">📅 21:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137728">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❤️
عادل فردوسی پور: هر پلتفرمی برای حضور مهموناش چند میلیارد هزینه میکنه ولی من افتخار میکنم که سلاطین فوتبال ایران علی آقا دایی و کریم خان باقری فقط با یک تماس من به برنامم اومدند، به هیچ مهمانی حتی یک ریال ندادم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/137728" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137727">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⚫️
⚫️
فرهیختگان :تارتار هیچ نظری روی دنیل گرا نداره و گفته باید جدا بشه ولی محسن خلیلی مانع جدایی دنیل گرا هستش تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/137727" target="_blank">📅 21:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137726">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
استوری دیگر قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/137726" target="_blank">📅 21:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137725">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpLfQFNcLweoaKlZFn2cE6Fra_gQF4i4fpNIqz5fJfMZn3a-g6WHVayPErkPsUS0kdyLDvAIGmVD4MHK1Zh_qdsFtVpqw5O-PVBA98kF9G53akYfGqoNJme-gQrQoLveaerIzADWkeP0kZW1fl5zgdMb19-uUey_xpLgrovyFLCQ2EfSW8Rrcn2Apu8w93z_DUzAyzKyHIJb7PZWivuxZd5XTtDDVkMUcnnJdijyCyHOvMQ4MFqa72t6ZWI_Sevn0Dr2wzyPgcZnnCvNJov2hNOt21weqFikwVwrEuBOFNhFnNXQvL1x-inOFfubnEhl24pPlf9f3dL0z_k0ByS56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
استوری قدوسی  پ.ن منظورش رامینه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/137725" target="_blank">📅 21:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137724">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXOkB_UmEV3f9fXnRHI2CmwXkYk4oxWCtonWAJMJIoPRrNXhjc2ZiFXGIxq3SZX0k__EiKR8UyMXqwQc-0AkYr-GjBs7x5h4w4fBDO3Xk3YapMkB_JvR1ShDMWuifAcnqEmgRAujry-Jvyxk_irGktqMW4BqlNCv69OoKpof91s_awX0MkSaeHjAuSaPtYhtM4-JL1Qp0Mnn78aC0veY06I21LNGw1mKCTcDd2Jup4mpYUA7-_P-36zgaEkCINEDMUqgsfOLmUkiyKS-FO4uye-powmaZMhSuUksSQfko8VyDJDwfyuhGNFQRQI28fiskRX1vxhwA_sbwAlQXN_Lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
رامین رضاییان که هیچ تیمی گردن نگرفتش امشب با کمک میثاقی میاد فوتبال برتر تا از سگ دو زدن هاش تو اسپانیا تعریف ‌کنه که شاید یه تیمی گردن بگیرش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/137724" target="_blank">📅 21:09 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
