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
<img src="https://cdn5.telesco.pe/file/nEo9_qyHk4y-qkv4wdwRuZNyycILKwknw8fXXCAlnEROtOZNuwVSajMkaAF-9tRvZFfjB1MPVySuDtHW4vnw8Px9D0XpZHFfTEMdpJW1CUv0hDYjAXGqFk-19JvLL2nyRWsbqTSDfV7q_JZw_DhDXcaRMqs7Q57Q7FzYo-ZWT9CRP-3lz_fXT_tYcidu7WgygFzI_0xG9ISafolMsHW5a2eG-Jte8xLTQmTDi1VAUG-KdbmRhieQpmVWhwjOd6WnHFMEBdseRbwbMEEtSKMGr6vQgi272qIORfysR000zof2UCgW1lTS5PyT9OiEE2GV98K5bHaBJSlNzmtAr4sunA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 473K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 01:06:13</div>
<hr>

<div class="tg-post" id="msg-103521">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
🎬
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
هایلایت بازی امشب PSG
😀
-
😃
استون ویلا با گزارش آرش اسدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/103521" target="_blank">📅 01:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103520">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D85UmFnbP5qPRVT318VqtaAeMq1B8Y56mFJhVaRN-eC8RLonLz1HqfYLDQSn3eOI21VttCyEksBNNZ8kNpHlADtoYMl4T-fV27Z79Fl85Jkf-YgI6zrUc67MthKyx96tgDaA5pk5V1vRtqp_IFg3xd0LiYfd-Yfl0os_s4bKSrmSn66Dc-L36zwyWyQT-qDiiomTchlxkqJnjebW14Mf0YSbcVcwDYlbCDpwjW072koQrj4LQ08s1sAHYXNrTrZD0rSvFJC6yTOCF8fqJ_2UQQa_xJVHg3asjAtNWqr8A47dukpHjfrvGVE-ymOmvRUVpmpiE7_KUlYWn2e-LJ4BSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
از اسکای اسپورت :
⚽️
منچسترسیتی بیش از ۷۰ میلیون یورو برای رودری می‌خواد. سیتی ترجیح میده رودری را برای آخرین سال قراردادش حفظ کنه.
❌
هیچ‌کدام از طرفین در تلاش نیستند این انتقال را مهندسی، تحریک یا به اجبار انجام دهند. سیتی راضی و آسوده است و رودری هم راضی و آسوده است.
✅
در نهایت همه‌چیز به این بستگی دارد که آیا بارسلونا می‌تواند رقمی را که سیتی حاضر به پذیرش آن است تامین کند یا نه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/103520" target="_blank">📅 01:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103519">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrPkNKOjQTYlbjP1lRk493Ecp5Kw7Tan6Vq11VpECsMZZUHc74aoao2CCq3PKl_SWiSmDpnPcrEOJbf5S0aPPYwMKXhqkfLniYfkAmKBaXfHmQKJf4wNYu-busMgiRl9QJ-TodllZlg9QBr_jrZCNbEWunoTL9L5sgM2o5FhlTUtJ6ywRLcezoUjCR6T7ina1xVQ9gzZ_umgWts8jvOL5qfd-oH_DP7S2_cbeumiakCJ4WMfiiH5Q2LgS7zq4AeatT6WpX7Wvad-D0KTRhiv0qspof5JdtRJXL5gWdpQ5Dtdcgw7itqH3HJ36J3vyAg7OC7clZOrtS_MYNwIc39usA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
رئال‌مادرید امشب در بازی مقابل لاکرونیا با تک‌گل براهیم‌دیاز به برتری دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/103519" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103518">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/103518" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103517">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=AUSejolOxY8fzRaC6pBlBjZdKBAa9_hcMgSAarHJ7nwjlp3NP4y5udgQHNDPPuXPEcJBy6aCRgb7dqbQjmZS2OtJ7i3uftGV39Osc2dewSqPARKCClisExbDhAVSUNpmFFJ51FquxXVpsFFYpbpgwfTsp7EBU410ECxGhRL44j-F0ZNtB4HiuC5zUT5HGrHyX60WXg5AJt4LphFM6f33FqDKdE65i3J6KX8HS6Ar1NDJqs0HLu9TadtfCl9QtaXxVWxZ3DXV6PGkX4nqJ9h1QfVn2IdnUZAghZ5I0cSd_hvjuIvAeK0bdfFUNZNBRAb9B8-w6H7IM3ZPW1plheeoEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=AUSejolOxY8fzRaC6pBlBjZdKBAa9_hcMgSAarHJ7nwjlp3NP4y5udgQHNDPPuXPEcJBy6aCRgb7dqbQjmZS2OtJ7i3uftGV39Osc2dewSqPARKCClisExbDhAVSUNpmFFJ51FquxXVpsFFYpbpgwfTsp7EBU410ECxGhRL44j-F0ZNtB4HiuC5zUT5HGrHyX60WXg5AJt4LphFM6f33FqDKdE65i3J6KX8HS6Ar1NDJqs0HLu9TadtfCl9QtaXxVWxZ3DXV6PGkX4nqJ9h1QfVn2IdnUZAghZ5I0cSd_hvjuIvAeK0bdfFUNZNBRAb9B8-w6H7IM3ZPW1plheeoEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a21
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/103517" target="_blank">📅 01:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از استانداری کرمان:
با تماس‌های برقرار شده با مسئولان مرتبط،
فعلا
عرضه بنزین با قیمت لیتری ۸۸ هزار تومان متوقف شده و مثل روال قبل بدون تغییر عرضه بنزین در استان انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/103516" target="_blank">📅 00:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103515">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idmBWvV7EXmlfAV_Bu_5iq0zC8ubEU_FEPS6Kb0uFBekib_NhpSp0sLTPtprf0Hc8VnwUyoWL-_XsCfKJFcO2nYyAdtL14-1M5Jsc5IPKOPW6IUZcRDIsY3ajGJx8CVtAMKLmSC-KtQv7ASV_HzZCjxslMl1msuhKMGw5WlIniH-Uh4LWQa_ckRYOObr31PAnApwp25Nx9Q1fnN32DZ8V3a9IWKbzbOfiw3fzILuuNylsu1Ku1twg-zVMvrDifbvwh9YQ9SvKSDp-RsgWfS3b35je7dDERwxXwQtgfp3prI9c2McOMt8yohE9c_KBZ_j2VcoA06liUhbjkBOF6S_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
#فوووووری
از اسکای اسپورت :
🇪🇸
بارسلونا به منچسترسیتی اطلاع داده که آماده است پیشنهاد خود برای جذب رودری را به ۷۰ میلیون یورو افزایش دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/103515" target="_blank">📅 00:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103514">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eU9NYoVIxKMFuCiUfbNi38YXGAfpMFq0Ojric5th7tau-i9jomc-1s5gcKpPC7oEJQ-iProcrzmkNYo8SM945upURhw0kPFSSz6Xok2eK49RDqlCFIjWzEqILEj044CtRHVN2mF4Y9_QZWtexGV4AEyBfHh3DS58jkRsQwuVbNrzGt17smWABUN31BbWXjXP7PwNhBESFwhpc8X7g1H-etCsyJuNSZxhTmZ3gb7xROFQIOb6vbN3fI0EfXaHTp1z4zRSJqXz65DoQCqgvz-UJ117CyS4nWkOcgkzb3vlKOGXmiLU1tlv1kvH9Foyo5ei4MWF3hBBHjj90feJZMK7Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🤕
یکی واقعا تو بخت اونای‌امری ریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/103514" target="_blank">📅 00:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103513">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7mct6y0-L23Nbnhs8RlIS3Bzq480CvvXQQg-7is7UJKgXA64GCFDKcTZNcEkNvZqRXJcRdbchEAwNm2LqVFshxIsYQf_RfKTF8Jhv6x_-CRC9nGrSF07x70dh3JYhrSDt9Fw-8ayLIgom1YNyPAAPQW0YBnkBZN-veyD74xPM2yXHhJ43lJ2O02Ywb-BkP3B7_A6oaXw-B0pNVh9eWBSIY5sP46xTybyh_0dpHoTbz2AdEyUps5g-o7Ncvvb8yvaeYFS1r6aeBc9Ons1Gcc3F-LU9QbkUGyECY_fmjwl2uRz2Nt18ynQosZI5LzS8F-i7EFyarJHWPHc3NOk-I28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
فقط چهار بازیکن در فینال لیگ قهرمانان اروپا و فینال سوپرجام اروپا گلزنی کرده‌اند، در حالی که سنشان کمتر از بیست و دو سال بوده است:
‏
🇳🇱
1973: جانی‌رپ، باشگاه آژاکس
‏
🇳🇱
1996: پاتریک کلایورت، باشگاه آژاکس
‏
🇪🇸
2017: مارکو آسنسیو، باشگاه رئال مادرید
‏
🇫🇷
2026: دزیره دوئه، باشگاه پاری‌سن‌ژرمن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/103513" target="_blank">📅 00:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103512">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWlSoebSctCP1qIDhz7Vw1pFmFo-CM2XkBUOJ3rtaPAl3un1sIzuQ61li9PIzi6UuKcQGSYuRuhxLXg84ia9U4DbxkaLTamH2OSmFxPpmjQmslsJtQRLQY7pGzVCd4ExCSAHSBY7pKvd2bJ9La9uIXYWzW4EjU-AbVjuUUtqLBhhnLuCnsesxcqmTSoqMkyoPAS7VbOU4zJ4Ctdo_NhlflrT5uCj65FUREOWhFKT9P-Kzbow9NBrRDzHMcKWvkRpjqKm0BOp1iplt5k_Co3A45ii-PkHY5MhHpH8D3nAmLNM9uesDrhY84S64JwdC33V_PoXoqJ3q9eX4xmm76VLRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🔥
🔥
🔥
🏆
فقط سه تیم در تاریخ، عنوان قهرمانی سوپرجام اروپا را در دو دوره متوالی به دست آورده‌اند:
🇮🇹
میلان.
🇪🇸
رئال مادرید
🇫🇷
پاری‌سن‌ژرمن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/Futball180TV/103512" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103511">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgZoNhEWYpux227-M2ZHeIBxQMjtnXIFI8q5wO8XFGAJIGDelkmkYcC7v1GlF-KS1s0H-cPHeaI7xWljvt1XpESuhLREj9zEOYSKxFFBETbpuX02jUbq97sRfWuwL7kWxUDc6Zo9V3XqoFZsdFq__Zz0cGcu5cMPh-cjhq4YSc0rfgAFb9bZluygE8AsUptzAf4QwOJ_eQ2Zu1rtMY2VcI5e8tJpiliwmqMLUt9FHrzoFhiZmJmRBT8iUZnnA7neBpxg-KL1PpxEq40CCyjbLz9t7GpMjb5yGKWB0-8kWH7rPFNiwkm66AUkxJiFsXAtEZiJptwSNYCXOS7ilZbFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🤯
افتخارات پرتعداد مارکینیوش کاپیتان برزیلی و مدافع پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/Futball180TV/103511" target="_blank">📅 00:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103510">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzlOjt7iciSCcdJpOBVesPsOzpTPn2wLvoc9O0LpbiNZvEy9PCdQaJ6BS0muGg_M77Xp9dZ7TcyIzw7IOh6lW6_Iy6zjautB_ixkbf5CIpsOi9iGaQ-uc8Bma40V2FsZJ38S8g80tzDjGagvVz-wcof4jAGBQH6Xt-wS7VRvZ0aCzURWz1UpCz39_ElqQ8tfP8n7L6AypWEzoA9YikzFguaZ2RXs_uBdjtc9RiVEnbJVe22sNLKmUzvCfLoFtlBMSb8ndibpaMK_kt48JJwPi1rFZdW-W22RMfaC3zo1w3UXPy0-n9dPZNZ7Pa2rHmZd3zJTdgPGxu_1ZqEyqcGUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇫🇷
پرافتخارترین سرمربیان تاریخ پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/Futball180TV/103510" target="_blank">📅 00:30 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPXLq9zSqkpfxq-a0dv0igAOJfG3RXi5-913fYAnKuDTUp-NMj1gI4RoAmhV3Sp-UW5XBirpjq7-Mfj022w4PtA0_IkTcESI0xxpiN7_BgxEqTeGuqJvoxI4kKFUh7DWSQG-aeykf91uXQi2QOvqk4Vn64mglJFCYhlFgNT4nMl6EoLZctIGQSZk1aLZ0-em2nuEUkEwqIsc-PyldukDS0jb9ojvIzsxv1UfBGUmzzGLEwkRmoZqsAFVz4BkpdDmW9n-N18iyL766XkQ_69E9pmRLGJ7fxJsHIyfvBNg4HwGh9asQHOYTC0wLvNJGHqARdhtM25VSOJUKLw4gw3SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
پایان‌بازی سوپرکاپ فوتبال اروپا؛ پاری‌سن‌ژرمن درحال یکه‌تازی در اروپا؛ انریکه با کمک خط حمله وحشی خود موفق به دبل در سوپرجام شد؛ دستان امری بازهم به کاپ‌قهرمانی نرسید
🇫🇷
پاری‌سن‌ژرمن
😀
-
😃
استون‌ویلا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/Futball180TV/103509" target="_blank">📅 00:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvis4rh8Hlt4GflwsfCmYqhgyXNv3YHfOyx-QkSGbXUcvgEN-DJitWuKYmb7FExK1ZQRssdRJ4Wfy2K0dl8OHeChxRXLRGn-J3OdWLyqVU6d80dfTLtVewNrC5E8I51TuMgwYP0sax0qbGfgBFAVscDNIPmiOdChaQtQ4sNgm98yL_L8_7ul3EY3C81R_4pvPTytOpLIMv7uryqkdD26-OzwMJj4__7QCMNvFs3Y5dKrk87B1hYfpI1aQEYug9pL5bpCgvrF5eSaJCwAsBrwSPPGfJmY7G5gf5OA9lu3tvGus857-oFqQwqi0njS8u0CHYvALiiqWGN3AZ5xOepdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
پایان‌بازی سوپرکاپ فوتبال اروپا؛
پاری‌سن‌ژرمن درحال یکه‌تازی در اروپا؛ انریکه با کمک خط حمله وحشی خود موفق به دبل در سوپرجام شد؛ دستان امری بازهم به کاپ‌قهرمانی نرسید
🇫🇷
پاری‌سن‌ژرمن
😀
-
😃
استون‌ویلا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/Futball180TV/103508" target="_blank">📅 00:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5497970611.mp4?token=Xe_a8ZtdcevWfXNPG_VLQBKvGn3zS_8uqc0XpN68uHPog0eTdbedxRRdtWD7NOkbEn5f0-MSQIIOs7bOt_5GCeRZZSI_VUozyGVvqryMBXP68hxak27TMPPMyJxwZ1jDY6YB9dqDMACTKvJ_junp_xH46xT0gaUQhnrRIm-kRhhRg9h7LIeit6QopcgOfq_s6VeUctXJCV72QDApx3Mor66FPwYM0SiXUS9zi8BDiJrBImN3LA1i_rfqFjwLPsoMkgFiuC-ZKk4_RUv2sUsl3KRyhem9SrTd4bKuZfRJxCRymDr7aUiGemdQXunplEv8nZb4_afbHh9CUlDPNrh4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5497970611.mp4?token=Xe_a8ZtdcevWfXNPG_VLQBKvGn3zS_8uqc0XpN68uHPog0eTdbedxRRdtWD7NOkbEn5f0-MSQIIOs7bOt_5GCeRZZSI_VUozyGVvqryMBXP68hxak27TMPPMyJxwZ1jDY6YB9dqDMACTKvJ_junp_xH46xT0gaUQhnrRIm-kRhhRg9h7LIeit6QopcgOfq_s6VeUctXJCV72QDApx3Mor66FPwYM0SiXUS9zi8BDiJrBImN3LA1i_rfqFjwLPsoMkgFiuC-ZKk4_RUv2sUsl3KRyhem9SrTd4bKuZfRJxCRymDr7aUiGemdQXunplEv8nZb4_afbHh9CUlDPNrh4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
✅
رئال‌مادرید امشب در بازی مقابل لاکرونیا با تک‌گل براهیم‌دیاز به برتری دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/103507" target="_blank">📅 00:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو و اورنشیتن:
🔺
چلسی تا روز جمعه ساعت ۱۷ به وقت لندن به تیم‌های خواهان انزو فرناندز فرصت داده که پیشنهاد خودشون رو برای خرید این بازیکن ارائه بدن و حداقل رقم ۱۲۰ میلیون پوندی میخوان. پس از این تاریخ دیگه این بازیکن برای فروش نیست…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/103506" target="_blank">📅 00:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBwSz2-zBmzDqU6hMWmFbEsEwi6akt2nOe53DEpVGBn8IgzE7UcrW4q20ujboV5HVU6xXc2iy7Q5vxbfZIkOMwAZ6IvnlTkyHlWf6VKropEkNmwNeo6rDw4R1e71mMJEcsQTUBipv7lZ7jA27oFb-buQRZ3PsbdbVsewXejgE2diDWw167dpowX8sE-ICPK60eVjST6wdtp53oUXq_lESBDxVeDIMNBa46NwdbIQ07g_TQ5cqiLujId-4BAi99vox0WNOO4pJnhKLRYAKQBx-1cdSZ-OudvV9BuiWGKZw1tgFdM_HtA_GLWP-jOAr0YZBmYifegcFG3rhaSIY5ZEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو و اورنشیتن:
🔺
چلسی تا روز جمعه ساعت ۱۷ به وقت لندن به تیم‌های خواهان انزو فرناندز فرصت داده که پیشنهاد خودشون رو برای خرید این بازیکن ارائه بدن و حداقل رقم ۱۲۰ میلیون پوندی میخوان. پس از این تاریخ دیگه این بازیکن برای فروش نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/103505" target="_blank">📅 00:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38009c3d9d.mp4?token=PlrYBAglnBn5vTaRjEdhXtoKDQ-4UhWCGvuM3B8lHzG5g07ghLMmOkbmbVaEG1Z9-aBdiByE9aBG5hMPANbkQAL6hPpqA9kMH1sCv3PbPD3HlVt4EMMQyOx7C2nW1Z37zVlyRE_4bBHQjpAukcp0R3Q4ELG2HSe4lcabZmwh3neJ18v_3LMXGiO-EQUR7JydFCvrqA7k8uBoJjSl94tesubYei0IDFbNIz2HITgjicFOFmDBvJB2sB3ZRgFhiXs6g0GBbawsnZRAZyIe2Ao8KdvTiWTwJ2ZWRRqgZRPzFNtakjSx3scR7X4MqPtTwwZd82Kd9MBuoC5mY8Mr3iAkqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38009c3d9d.mp4?token=PlrYBAglnBn5vTaRjEdhXtoKDQ-4UhWCGvuM3B8lHzG5g07ghLMmOkbmbVaEG1Z9-aBdiByE9aBG5hMPANbkQAL6hPpqA9kMH1sCv3PbPD3HlVt4EMMQyOx7C2nW1Z37zVlyRE_4bBHQjpAukcp0R3Q4ELG2HSe4lcabZmwh3neJ18v_3LMXGiO-EQUR7JydFCvrqA7k8uBoJjSl94tesubYei0IDFbNIz2HITgjicFOFmDBvJB2sB3ZRgFhiXs6g0GBbawsnZRAZyIe2Ao8KdvTiWTwJ2ZWRRqgZRPzFNtakjSx3scR7X4MqPtTwwZd82Kd9MBuoC5mY8Mr3iAkqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
😱
لکه‌های نفتی بزرگ در سواحل قشم تنگه هرمز
🔻
با تداوم محاصره دریایی، مخازن ذخیره‌سازی نفت ایران به‌طور کامل پر شده و ایران دیگر امکان ذخیره‌سازی نفت ندارد و به ناچار نفت مازاد خود را به دریا می ریزد. این خبر تایید شده و مقامات جزایر ایران درحال اجرای طرح پاکسازی سواحل از لکه‌های نفتی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103504" target="_blank">📅 00:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29b02952ec.mp4?token=UCokJcvDS1yKu9wvdbSiv0YxRGKqK3KrQ_qQjWRQ_FJJvWVfe0qjjbbexlwW9A3dVnvTMa7Y_WVuXj56r0XXCeo19cMi56oQE1FRvCea-DC0R930ZeGXsZhAg7lWHJb9o_rMz9D8ruPy4tUgU3vSioJeH7lx9CtkGLHDuHsIuU2FGuCPcL0JLpT1-mBvwPMvqhFkDZFKTH6Dgcb6Zgx0DF8wjUJtSQppDDUGAdiOqUuLkC-2nubiTEdsm_6MLtTcORhtzQB6ZakLJyAchL4QDZxEJFUkf1OGVTH596pwjkSv2v5APlb6Q6RD6rxTaKU68AAQ0Kx7-gTk4kBqjgr-27E9V8-PftNVso9bBMEvwqHr05TfjlyiWOi8iV7trNUxcJqRpYiD4PgSSjsMRnEHOjLrffLviq2qo1d3vI7K9vMJqNw1CBE5HrJwQ94gQdMV3VqFz1Lx-9wyBPNZq9MNRTqjjSS9jnHKzE9youALcIKyvIXdb9ay0ClfSSX_sDh3rF7-bUoHMAAFAOSHSyASnZg8Bdd7lGOeDNsln1R-Steag21QIIbEqL2PJ8VQi3QPRlFfYMrarCqfsdS0YduarRdGTrKgz6M6pH1vrjoOhdSF8LvXDfcTfKSFRQp5KPb4vVSdIHnd-3CB28dAhgCdNKczB9h3NpJ3CN042z8orqc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29b02952ec.mp4?token=UCokJcvDS1yKu9wvdbSiv0YxRGKqK3KrQ_qQjWRQ_FJJvWVfe0qjjbbexlwW9A3dVnvTMa7Y_WVuXj56r0XXCeo19cMi56oQE1FRvCea-DC0R930ZeGXsZhAg7lWHJb9o_rMz9D8ruPy4tUgU3vSioJeH7lx9CtkGLHDuHsIuU2FGuCPcL0JLpT1-mBvwPMvqhFkDZFKTH6Dgcb6Zgx0DF8wjUJtSQppDDUGAdiOqUuLkC-2nubiTEdsm_6MLtTcORhtzQB6ZakLJyAchL4QDZxEJFUkf1OGVTH596pwjkSv2v5APlb6Q6RD6rxTaKU68AAQ0Kx7-gTk4kBqjgr-27E9V8-PftNVso9bBMEvwqHr05TfjlyiWOi8iV7trNUxcJqRpYiD4PgSSjsMRnEHOjLrffLviq2qo1d3vI7K9vMJqNw1CBE5HrJwQ94gQdMV3VqFz1Lx-9wyBPNZq9MNRTqjjSS9jnHKzE9youALcIKyvIXdb9ay0ClfSSX_sDh3rF7-bUoHMAAFAOSHSyASnZg8Bdd7lGOeDNsln1R-Steag21QIIbEqL2PJ8VQi3QPRlFfYMrarCqfsdS0YduarRdGTrKgz6M6pH1vrjoOhdSF8LvXDfcTfKSFRQp5KPb4vVSdIHnd-3CB28dAhgCdNKczB9h3NpJ3CN042z8orqc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇫🇷
گل‌دوم پاری‌سن‌ژرمن توسط دزیره‌دوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103503" target="_blank">📅 23:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103502">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5rxFRsuHu9eUixCx_BljNTsTaW9hcyX7y43a4sei6kL7h53TmMiX8GANXYIeeAsg8C1unvVt7-qSGLkCzYHnwq7oufPsemqXOjPzJ4CBUeeowVb1Sgd-XkxYjmVEGGjEqgfGOudzgJvvbWsBPSdFpsE2LB-uuxUIXKRWkqNbKvI0ZWScuNNfKy3iB1jFv7O81325nRc3h_ejETD7etfpGQYBpeHE7BYdStDrIrX9dwvrC-eYGzk54PczRPFZi-C7BveKG6gVI2mT-ThhW93-FTNcLNlj0k61qz0AngR01FPcnaZnvx7hlSJgPoVHdrZR9KAw5u63ihQ_g7mlOE0Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🗞
فابریزیو رومانو: کریستین رومرو به اتلتیکومادرید مبلغ 40 میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/103502" target="_blank">📅 23:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNWKh0Xa2d8T8UotTFU37yQ2lr0eEZMY-9F6Ey8xIhf0d9PWAXTmnFKMglPj2WkImCthaWmeb7qdgG8ms57vizU06S6wpAZU8iqrVOlY2rXjSUxUU_8L383iNxI0sIXYdeLMo0DSWRMz_yg-9s72q8b6iLEV_KROm7_9Id3Rn_bD4pyuymjI6afgEB1e8PDTkS-JZydVItuFmlEx5tdhaMrFb6lxxDwZePZfUSnVXxHl6qMTalay-e_zxtW0xGbXa-zZOHUCqblW3DJCkMn4esesC3-JgsOBY5SMoatfcSFmDgerfnI5KL2oMwa1h5_7hHvNNFcIUharn5B_AryWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
🇦🇪
امارات متحده عربی ساعاتی‌ پیش ۱.۵ تن طلا از دارایی‌های ایران به مبلغ حدود ۲۱۰ میلیون دلار رو در تهران تحویل مقامات مربوطه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103501" target="_blank">📅 23:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103500">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ojDJUQ7CBgjIjK4Birr0nXWlrNEcijUJN4roIJvltS4iQwyfGms_agB35mfJt01d-BMMJu0FNpkj2ajciJ7hKDsbonzmU9nzMOTrqVoyyf7ZSVIXlT7dhvi-lc3oqJPto7P0wOywB8dvxEXzWBZ4ErizZYD_MdXkNoLWS9uI6QfKJXKootD8VZEAzr4Z43z9lgBTxlxh-XMQTe4jK68cLIlJZIKBoP4P5uQjGPevZ1q5-h59Vnz67bWUwkq4G_LMBUZ6iFNZUzwzjZpig7LYXbm-ZS9xX2huu76U2ip2ELxCCYJDGLVG8Gh6hd21W51bdqUUrlwX8uuQh41IgF-0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
✅
تصویر دیدنی و فوق‌العاده از خورشید گرفتگی کامل ساعاتی‌پیش در ایسلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/103500" target="_blank">📅 23:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_j2H3tlxX5NNq7Toz5kUFj23rRYaaIej-lmNAZxuLE2F67Tu1uICHUwEaNGXdpW3pgSGmZXtjRQsttkyUvalVw-oaxEnJzeP_X50HpEfeFIIEZ4ne9qOkvUtprNXwL5-NAdVYB7pE065DgJ0SM6h1YE_7P8pksGT2FiL7kEJ9kEKyU204Dm0zTDWZECe8AIshrXrKJS-Fh1k-nRfgkOJmFaee0R8xTqNdymhx5sDquWHoKXx3OFYEW6c_mTPoe3NVekvY26W9NHykkmW6_tGIoyn2ALouV762nNLJyZrX0KHMaxa9ujVwHVm5Y2KdGIypYxbmYeSM6YbxlqIqTRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🇬🇪
📊
کوارتسخلیا اولین بازیکنی در تاریخ است که هم در فینال لیگ قهرمانان اروپا، هم در فینال جام‌جهانی باشگاه‌ها و هم در فینال سوپرجام اروپا گل‌زده است.
🥶
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/103499" target="_blank">📅 23:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103498">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZJwlNi7Ke6kI4dQoO5xJHeVp5T23u1MgPMM1njmKWZd-9QQEKzoZo_JYI4aA8SUuYonauf5INkKImQ2dX4fODeWHpmz_wm3UjJMiB-bwm_RKYGVknp81EMr3s1ICfKc8sTcjgfq2lUMWzJpSrd2avIfQOsi5YjZ0UzX_LdqVZbXl7933cKDGQ-vzv2IjfoNCaUubh4JTKOwI6KQ97ahr5JY9ZVCJKpCZeFlrvcvzSW6mY1ZzDS4tEapW0WdvHfrFUniQmvQKHnD2WVB-8b3TlK_TRvtCS64B-tLGGn5Iilp7htixF_8DTCeh6LTmdPPyOw-SFmrgrbgzv5d5nkvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🤯
🏆
#رسمیییییی
؛ ماجو با گلزنی در بازی امشب، با ۱۷ سال و ۲۱۲ روز تا جوان‌ترین بازیکن گلزن تاریخ رقابت سوپرجام فوتبال اروپا تبدیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103498" target="_blank">📅 23:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103497">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8d89b14cf.mp4?token=s0pvLqaUjG4Fil9TLvJorl-nQthOIK3KdeHsym2Hh-rtc9kGjVmFPEA0mMuCmja8ROfVuqiWclriDSNRnPl67XzCgVKhsCQ7hz_uDncCb_0PLarWdR5XGwpEESVl7pSj0V7Hbhkv9uorRj_9gHi1RRAD3cAB0TXMuVz4b2DrOQ7GpJDVzpVdj8BWYANxLRmeMdJzs37NylAaYJIK6ZbUShA1eK56onAyxNgxBQGbbjGxrX2QjYO-oi1hyOx-KItYg7MVlu6-W57TAp24ZflVrU3kfALmmWPVKiT5JJnp5qyHoho8x_LFjnKYEV9U7rG5gUJwpDMiJkHkMPcRys5fDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8d89b14cf.mp4?token=s0pvLqaUjG4Fil9TLvJorl-nQthOIK3KdeHsym2Hh-rtc9kGjVmFPEA0mMuCmja8ROfVuqiWclriDSNRnPl67XzCgVKhsCQ7hz_uDncCb_0PLarWdR5XGwpEESVl7pSj0V7Hbhkv9uorRj_9gHi1RRAD3cAB0TXMuVz4b2DrOQ7GpJDVzpVdj8BWYANxLRmeMdJzs37NylAaYJIK6ZbUShA1eK56onAyxNgxBQGbbjGxrX2QjYO-oi1hyOx-KItYg7MVlu6-W57TAp24ZflVrU3kfALmmWPVKiT5JJnp5qyHoho8x_LFjnKYEV9U7rG5gUJwpDMiJkHkMPcRys5fDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول استون ویلا به پاریس توسط ماجو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103497" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103496">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگگلگلگلگلگل مساوی استون‌ویلا</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103496" target="_blank">📅 23:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103495">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fba6f1f51.mp4?token=GU5aMuSYoMn8NEAZIzBgVlH_PWZPpYN7sbsYfQCKnTC6QDWrDPHN3Z_OpZTE33gxmi0LTHKoCNtY8yVty2G-Cfr4Ty8MbdAxDJb5iyFxmFtZt3MqvkvGaJ53HOXQEHhzXjvVzme01nWMcpE81GpHXCB6h_WMUGyOBJgoZwqERu5DqmbfZC8Xw7U-HKX9gRpZhKUC7hCJS-taOcKNHxaKX1lprIOKy3DTS3_24KewljQzGJcpkcCsfYos97rckyyxBD7KSET-uZSmXuleGWPVNvcfnOUFKn0TTO4qNeVscPN-NSQ6ag2bVWBqCrkIVpGIfTeGGoNKg1Qy3xJmO2SR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fba6f1f51.mp4?token=GU5aMuSYoMn8NEAZIzBgVlH_PWZPpYN7sbsYfQCKnTC6QDWrDPHN3Z_OpZTE33gxmi0LTHKoCNtY8yVty2G-Cfr4Ty8MbdAxDJb5iyFxmFtZt3MqvkvGaJ53HOXQEHhzXjvVzme01nWMcpE81GpHXCB6h_WMUGyOBJgoZwqERu5DqmbfZC8Xw7U-HKX9gRpZhKUC7hCJS-taOcKNHxaKX1lprIOKy3DTS3_24KewljQzGJcpkcCsfYos97rckyyxBD7KSET-uZSmXuleGWPVNvcfnOUFKn0TTO4qNeVscPN-NSQ6ag2bVWBqCrkIVpGIfTeGGoNKg1Qy3xJmO2SR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇫🇷
گل اول و دیدنی پاری سن ژرمن به استون ویلا توسط خویچا کواراتسخلیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103495" target="_blank">📅 22:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103494">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di73kRqaVMY_J038MqV9Bx7amyfCKQ99FAE0Vz2Xjjc5nKMr4-2o_TZQE9kzN-38jbnduEPlQkAKG2V8M0sHnRzlGQSZlSr1sdwi2wPzQZV9KOr2WiXzIPNk-ff6_l_VS1SYdlr4xYFD1BilPEYcjsD4Pp8lndSrVhhg9doXSvonHmP3QHSNmiw5Ri7zZWrSXNYDYc97HSFjV8dq-Pu86ReEuBCy5CSVLhFuzLN4w2erYw-h37FWi0MzOkqLjOfy48vK3IPTIz_EVCYXtoH_4djI61TNmrI4W0_EqfRlkjVMDqJMHv5tVb-j44yvq6wnqPWDHKFZOs2VGPlAYy8xuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
رسمی: ژاوی هرناندز به عنوان سرمربی جدید تیم ملی هلند تا سال 2030 انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103494" target="_blank">📅 22:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103493">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jey5WT3WqhWVSKYgogg9oTGMKJj16pchCw5kFVCs5OozynDzyF7iyNBunccgEwq9aHOdZs_-sL8OWQt6hebwTtnt2DHvHiCwMJzoP1xNXWxuG7iwigcTt_YZOTpCLWNfWabf6GpdUEi8oCkCYkqsAhvokiziBc9k6c7b2XB3ImyCL-fw3WTr3MDIXZDyP5DGt_xEuGLwTuIIj0q7qfjFwLbAxsl_IoKSxWeyMejGGuQRt6xdSufauRtpA4Vd1MlWFA0IFQk1TZLnK91Jcu7b7oafEj7N-SBvFeJ74N-0OKa1b0LFhVQIEtrQbww7OPoKwrWhODvz3NaGYquw6XGTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اسکواد پشم‌ریزون فنرباغچه تحت هدایت کارتال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103493" target="_blank">📅 22:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103492">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d270719e48.mp4?token=RjcNYsz7oKfdlVDIz0K29HAu30-yQ933wEY_NWQ2CdD6h-2NWdvp-abfRkd1TqH0XhsTB7AG2z6xI-xSwoBxxBPzzERMY556KT_YzUAncdfg0iacdWv2HLcdiIiWG_d44JpfEukIlD7KhIeXCD2oZ3F7CalceRQmEPptgi2uPP0fY2sf1JURjfcdGRv2tpbPN89AyGu0oDtD2uLAk38bq6Qlc0tYlyf5mUpTv-4-DRt57h7I5hoAZ7q00Icn4tYa032V-NofRsZdHnSqrLwuA5Z2gUktdVkgVUVlDgBHgzUM_Bl28FE9t-pSalp41HiJW96Cm3g8mEYLhgknBFU5zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d270719e48.mp4?token=RjcNYsz7oKfdlVDIz0K29HAu30-yQ933wEY_NWQ2CdD6h-2NWdvp-abfRkd1TqH0XhsTB7AG2z6xI-xSwoBxxBPzzERMY556KT_YzUAncdfg0iacdWv2HLcdiIiWG_d44JpfEukIlD7KhIeXCD2oZ3F7CalceRQmEPptgi2uPP0fY2sf1JURjfcdGRv2tpbPN89AyGu0oDtD2uLAk38bq6Qlc0tYlyf5mUpTv-4-DRt57h7I5hoAZ7q00Icn4tYa032V-NofRsZdHnSqrLwuA5Z2gUktdVkgVUVlDgBHgzUM_Bl28FE9t-pSalp41HiJW96Cm3g8mEYLhgknBFU5zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🤩
عمر آرتان داور سومالی که توسط ترامپ از قضاوت در جام‌جهانی محروم شده بود، داور بازی امشب سوپرکاپ اروپا هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103492" target="_blank">📅 21:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEDdI6GGcp4dZrjix5k_JC8ISpdFfrKfrEN4EVdG1LdjyNJDDuXFOo1eLwUXviviFMStkfZHUQJfY8cTvYTWD9_14YScrLMQBjtac6fMAxWunBg6E7TwCB0swr6m-65DFQTjrmzj1WTW7vgQkJ5kgmCUp-e0r00IYnr17i1H3LDZQyCP-izw2JourCMp1PK2YCuwW751EN7Xdamt4gXeAIZ7fvpzjoD49j9O5FnRtUJCkZWAWSY8NsdcvU8EajvoxTTuztnZlaaBCsnNaE7kKf9wTVllTghG7UOqkCANfsFhh6FR6DOnxpOK3MG9yMwjk-nDby4boyDr2_3x1GbsrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
سوپرکاپ فوتبال اروپا؛ ترکیب دو تیم پاری‌سن‌ژرمن و استون‌ویلا؛ 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103491" target="_blank">📅 21:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD2mwIID1ds894S4p7lb1Ebc2DiD-C6OtvbafPi1r4TwPeWh7VcHHuICPqPqkaODjcBSsjVEGKci_VCq5wlm6VWWkfCJeW1miz2hrmTkpQrkBLiaU3Yrel6aBuMX5GF_YKnShE8eJgxYQ5aSOh52slGaFEjWXgE3Oawo6ZXWauGDBc16pkHoBikPGEO-1oxNqAM1h3wb5R-TeSsW4s-x5H8gdr-geZteE4FC8Y7tchQ1d1EN0wo1XAYx-zUEguwkFScQZYOHV5XcQ9Lm4zNB6o-iynG5d0zWUya-rn4XKLecP1eziU58SlMDBdh_yh71QPuWU2qMjolfVwrP7VSDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/103490" target="_blank">📅 21:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rc2yBs0D9yVZKCjuZtzR7t5NpyMPh7OziA082K3VI3SqTzd7QAv8_Ws_7S4NpMHu-cxy6r8K1r559ifzF8i38DXEaVqb5AXnZWFPAA7ZsiETtf-U6ETJ2n4tIVCHvmZm3W8myVeWon4KV0vYN6SkQWmVKFovtTwKyYElau9ave5bnJ_93Gm1SMBJFCtqrPvaS7xEVy5NUy46N0ogRUDYU4Z4loXKoOTEYEMzOI9Q6GMXS7P7gWzyreOUHL0sTksIoKopryk6EZ8WtPnu3g9LQw2lZTWA-q3eXnG5mqApfX6VVNqudUmVI8G6ynjouyVUzupPAc8my3nLbE60GAKt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PlH1lNe7Y5v8k40ZXLOijgzNvduNtOLAV2Wrfo8p7jbo187CDr2_hV6Mj1mQdTpw5_Z8BtxkBaO-XqRXxUCVVmsY1_ruQsX_5tR2XBw63Cq6zQckd0V3A5Xft0T0dmSVuUfReokRdbdwQi_pF6XUjJH4rH0MEFYlN6S-NWWhKsrC62n-aJQYNBO--Fu7ONWcOsQtD2oCkzInx1xDJmWM8B6j9xV4mp2FV1mSQQlSxcrJmJ6BaIFUFj8QGzoNCm5_lgQEcUgqTnnKHqV5JCrw6ygT74_whtlDV-EJW3loKs8MfP83ONVM_CrDcj3H_0YFSzacAqNiErCcNzMfFDaioA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هواداران پاری‌سن‌ژرمن در محل برگزاری بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103488" target="_blank">📅 21:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzOno87y0IrMxCDAaFk419B1LNUNk5b-rRbfW5hjXUnuqJGhhpvmQsLaWiTMnQR0bGH4JHHFzwPh1fDmY5Yf4jCqzW7zkoSTrrRWsS57xPwGZBal0tRvoB6MSngZjSEQsC-hjEUoDMY8006j87pcqnTJC5pbQOY9eTSIY4_jxoCFjByIWMY_7ELqbIloaxIS52B4y_XzTr2rRcUaSJAcKDJs_oA2PtBeIEFcTufRc-J4WeFjDY31aFHfGylUURJPMUt0w8TJyfV9sOYYQti_GBODTKdPDVWKn8NNM8WFaTXOmxkRpZv0kPczbtGV7X7fsIG9V13vD7mk7z0YxVNnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آمریکای جنوبی Core: تو اتوبوس تیم سائوپائولو نزدیک 90 کیلو ماری جوانا پیدا کردن، اتوبوس توقیف شده و یه چند نفری رو هم دستگیر شدن تا نتیجه نهایی تحقیقات مشخص بشه.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103487" target="_blank">📅 20:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZk83Mcwz5PCO0Gh2W1oiFShTT9K123RkjFgA3YcgGlaoXTktVpXa4ivzZW97NA0OoFqNvWkzYJetdc0Eo1_4X8je1NAc1O8gQWuB1D-vXAuUkxLuaTv6exiIH3wKYnSFFH9NvjDZAoiQbsbCwYJgYONKgji51YElbeza9KGcX549Oc5JTQVk_ApOgNL5RsfD-WV-D521Lze8W00CHUuhuelvzLQKcS7rz_PJr0oN4ZlZo5_p0eUZ04XjBvlHh0jM0GGZWPRRhD6zIg3L7q4PgZU-jKR7doRZmAyRSE9VS-19xOXrhh3KEDqFuQ0XnQ22Kwg9JX5jaCeVVdXyyUVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تو چنین روزی در سال 2023 هری کین به بایرن مونیخ پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103486" target="_blank">📅 20:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnELesRZg7I48FUJPxFacjjRqFSkSTb7aFSO3pnw0ilkNss-Bu5mz4uYZ6Gv5Lm7-9dRAM-E9pN8prxQxYLAp8CgJbna5i3IENNw-T6XBhU0U_ZsBjCs07qjBdAsq7wziC2UNQB-3zDj-WDtA318it8TM4B1oWMxw3F3RpLAAmJO1KmjmAKy0h038re0ZArYXVOOisvTHXuSyyNWbanw0badCktJZCpjh2ScXulrgQeNR53yPG7hccXhrS4W2rnFyD-1IwMcsUw3JmRiryBKSyyIFhnVNi69zJKxAjsDX0g3RJMjs8OEN_ra8l5aZRaUcRHuSpbU2tVUwKlN1YClaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s20V_TeVvby7vlMxWVHjw14cn6EPTHT5q5w58Rdt7CFihJ6pSazlaUl81JeMbBduSiUYm7Aj7k5a0FKx6qml0QnwXb5QxlYdJvcCvqqAU6ItpG69TFvCc6V2xKahS3u7zM1kzXADk5sNBwaudmzN_tjxVqAy5FJKEbCspNR87eCzioD654qfSuKikXOlL6mB1FuC31Zu2203BcZvRcsjdVvPKeUUxCT3ci6L6RYzJe0z9dP7-5MP6YyXD6aSQnOviXrC0WktzciDn9rAI9XHxIdgtxxgxG9jyKFMVzqJQeaJkw49khO6R_d_vB3Pc8DbHSf_zaMSCUZNem-uwRBeiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
مارسلو درباره اینکه آیا حاضر است ۵ قهرمانی لیگ قهرمانان اروپا را با یک قهرمانی جام جهانی برای برزیل عوض کند، گفت:
سؤال خیلی خوبیه و کاملا صادقانه میگم؛ بله، این کار رو می‌کنم. قهرمانی در ۵ لیگ قهرمانان با رئال مادرید دستاورد فوق‌العاده‌ایه، اما قهرمانی در جام جهانی با پیراهن برزیل برای هر بازیکن برزیلی یه حس کاملا متفاوت داره. اگه مجبور باشم یکی رو انتخاب کنم، بدون شک ۵ قهرمانی لیگ قهرمانان رو با یک جام جهانی برای برزیل عوض میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103484" target="_blank">📅 20:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQUci9mJh8D07Uq4bgNRhjIiK3HNf2FE5LgXInh44-QGNuLPnhE0-e9mZUEflemCubfEDHvMn9yURTjVYwhl3MX7hQhrks5nVZ6cLrZ_DSqnUL8QQ16MIIlnvrqh6f7LVwMtiPbnEXly3NXrJZEhukuc3AslNes_J6e6L6cUr2Us5eMMELvS0xOVoDcKkoSlwAQFfGyuAOg5KyMZj9UZ1tSMowGE8_kNVV8oGD6rrgFJehAocerFehgULAnATkFeG9cXwkB87JLgTHF0CxTA-Nw-pP2-uSrxvVyr4oupoeGZgCxPccAYsfOHBIrquWyLevRAECUH1O-kzuPf79yIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار دوستانه پیش فصل
🔵
دپورتیوو لاکرونیا
🆚
رئال مادرید
⚪️
فکر می‌کنی مورینیو ترکیب اصلی رو می‌فرسته یا بازیکنای جوان‌تر رو امتحان می‌کنه؟
⏰
ساعت ۲۲:۳۰
🎁
هدیه اولین واریز، ۱۰۰٪ بونوس رایگان
همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ
Betegram
بهره‌مند شوید.
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/103483" target="_blank">📅 20:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMGVEmkrBemRPfo9FkGYR4ZbB19hADm-XTgtYBRn5ieY4kHsFAaNeHKGDhvxKe3uyPY7iJsChW1z3KCWASY1BAXnbTc6dFGRDn_h7BOvSNOIyLIwStcntk2RP3fr7EQ9UXOD6byXzaKRYjSzuGnSrl42SNo1T1QfHGpAX3g2jQUgGVwvw3QACaNbp0DPoL7JydMhjjkiicZpz8p0kBoCRpG2z5e99gkna_JKhs74oaMjr_w0Mbukiwyb8R-Ho6DoFVqeDnTym8FGXOoLJSaHgyQ3CY2eoXdjVdcYV4RQaxggwXaEllVOI-EZq19PE_ix17_E9YZYh3jjt40N0NcodQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
خریدهای این تابستون چلسی در یک نگاه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103482" target="_blank">📅 20:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnkYWnnKRoRdAqgff4f3jyKha8184a-wCavca7VcN_TwjLvyMwnXxuAKTqnE_-V6UeD4kfJDFHXwZs_sYQAwJymHFcEvAl6LdTw3wxBv1lIPnrmV4VXaZkZ9wapCiwRm2Lsms5S-pVUpm_z1aT9Dmm--Fx-LnRUXq86QNXF9Vgf2GOOmMGsH2otlWWiQqjbJwUYkMXk62BjKh1jB2LSIQBmwIGWsM8H25YKWRg99ZPw4dH8cX4qCeRkNTL525LG1jPAdYskcRu_I8uczp0rAMWzEqoLFdY4wiJp0qBpb7xO736-MX4LqbCaWhahx_vWJWNVfDqfEJ1fiPxc_EnK1aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
🔻
عملکرد امری و انریکه در تاریخ مسابقه سوپر جام اروپا
⚽️
امری: ۳ فینال سوپر جام اروپا = ۰ جام.
⚽️
انریکه: ۲ فینال سوپر جام اروپا = ۲ جام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103481" target="_blank">📅 19:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IZGi5oEJH7gNz3KA1-yRuOnUFjOjlS50Cia8YZBx_wdd2fXn9oIYpSbcvZ8w4w7ci5-cs4aGsgN83tb8vRBrcEuLfg3a9ejWiFRHOdOLYQFazX5uii5q4KZLk5VXjJcbmsGYkitsaevHJLLrlKG9DjmFyLcPP425C5ZGAkyXPYT7-2B46pK-sn_SrgCoaSRSag7WfMmCPcN5Mlw5CEiks0VFhYm8k4dvucNoHRrB8kesKIZq5cPZlcA0jjx1WVRChNvKZPYzMfv86GmdgiRPvMHa03QeL6-uszw2MxdcGSyNUYrsx_oyI0mLFf-CrTtHU-dRhoWGc2rtCMYbYDHrxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UbzJFaGVWTB3QAWnyw8919D8x3gEuEfsbuPvWtmWjprJ7MdVuV5xDUzkOboWINz1lkn70BRZ2tTwCi8gGnHy5a3QoGgFn8mkgqKzsr3rthR61IPPbGZM0M34ZQt7eH4UU85g8Q2Hs5gngll8qziGmBHwXjStusbjGFq6vt3wkTwt2msy7iBXVf8wlWdgVJCxt-n6Y3Bjj1rUPtSL6v9oGiVR01s2QRrLSfLI_Ar20ehv_Rf_aZjjHiUVIk0Arrh4Iy_wUyvP_VgrvVgDbSR0jUcp-VGTFpuGaer3tWiVFW-i8n9gQ16dvMbCQ1FufBfkG3s3SFYqFbW4eE0yX4cg1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اوله گونار سولشر درباره از دست رفتن فرصت جذب ارلینگ هالند توسط منچستریونایتد:
تابستون قبل از اینکه سرمربی یونایتد بشم، به باشگاه زنگ زدم و گفتم: این پسر رو حتما بگیرید؛ فوق‌العاده‌ست. ولی قبول نکردن. بعدش که هالند به سالزبورگ رفت، دوباره همون موقع بهشون گفتم: بخریدش. اون موقع سه چهار ماه بود بازی نکرده بود و هیچ باشگاهی حاضر نبود اون مبلغ رو براش بده.
قیمت؟ فقط ۲۰ میلیون یورو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103479" target="_blank">📅 19:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttC4CvB5bvqZUr6VeX48R2qlz9DcsGOsj2udtcTmmyXin7KEyqizYGbZ_S2F64Iy9__30wX-O5iRYbJQy0nVYLGhRzEa99VnwrBYqeoOs_UJu6v11XwHRsTQV3y_Nh4VZwqtonPK3g8U8GA6hIyXZZFGqnQTxymFh6k3cfpstI_-jkgalpfIbJIN9IrztyJMlgvaiDo7NEYZAr3xDxSbrxi39odXjOg8DGAwuudHzRcK22qx6jEc51CsVj7BYVERS_Blu8BP-gjXK6WpQ8cj2WCVddnRV8QgXRXaIjZcFhK-QvKK4G_rG024fXHuY4QGfPC-f8CxrpNmDfrZJNtSkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
اعلام شماره پیراهن بازیکنان استقلال در فصل‌آینده؛ شماره ۱۰ به ماشاریپوف رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103478" target="_blank">📅 19:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-djh_R8PL6EqOGcnT21pMnBSEI__Ma_ikW8WrhQqRxThrzLT98NzcysrjU4fuo-tlGdUWJ5dOSNc_912vGT4Hov2LsGvPpEqZrBa6dy0o7XN2tZmeJXua0a6VBAl6XRobUnf95e_dAHAuWWDbnbld9DLiEZ7DnyoG9IAAib-IXkWdj3mR8fKSFvzzWBsgExIR9LVu_ZW1vpU-cuNWu-_7lwtEoTbUUPR8UwevxmaU5AeXjrWjnWhRkWLwI8R5LsAFnAaFoT0S5j-WQr5jPryYOi5wsvqpQ2BND8R2_tSUGfnvm3WFWwbxpOPrxO8ogH5gCyswobdgcMpJ1HFdiBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
باشگاه‌های لیگ ترکیه همچنان دارن به خرید بازیکنای بزرگ ادامه میدن:
🔵
روملو لوکالو به فنرباغچه پیوست.
⚫️
دوشان ولاهوویچ به بشیکتاش پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/103477" target="_blank">📅 19:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103474">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S48sGLOR1O5Q7LjCA1TEeBziw_MpreCIOHAZ4X36AYIE3-KxI1_zjSRCKmGNmsyS6-mwMcpol9AWV8Ukw2TV9lOx7IYerY9NxvoMx2V9CSJ8w60JZeDpGT5u2lBq3zngNg-8f1mJQtDNbryCL_Yz3Iz2b2d0MxnwyXaVvsiUvxuiVG-7x5LreEbQhB6EQ3j6oCDbYv2AEnPvo6r_xuc9xjY7ZirqRNxcL_C1b0AJ-m8g7YUx3tDTmuadt3v4mYHKkZHPS_FOwTpeIemovpitfTpRvGb3lezmU64xzwuGmk601ir7xsqSlc94y21hMFb6mQ7ZV8oUa-6hmz3EoZ7ZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFD_No4Qg8LJky-y7f4L4l3iOt1O4lLgPtT8m8-uXzOPFhLmHFhr-vprOt1EgxJaBmmob_Tzyi-MCI7lY7rn-uIvdQQ6yYaS8IZdEUZ4mrLQ2t3WkVnlinCDiLVJLJCrf3pMYkr1qJEStpWWKIUv24Rufu78dscHzkWK6pTNirAlNkOLC8BQoZlwoOM6YG0J_QpgKpG7U19fe3tjeNSDhlx1Qk6S58d_0U_BwlsxNWK3-87Dxs1QDXiWgoTMFp4iHHXFmfHgQoMuGYUmXR2aEts0AUhIkC4vIR_XW9Hd51dgwf1CjfoPd_hl_If2uZSlloxEnOUCSJ-OPEF7ssuegg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
‼️
باشگاه‌های لیگ ترکیه همچنان دارن به خرید بازیکنای بزرگ ادامه میدن:
🔵
روملو لوکالو به فنرباغچه پیوست.
⚫️
دوشان ولاهوویچ به بشیکتاش پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103474" target="_blank">📅 19:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103473">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30210b96aa.mp4?token=fi0ESYyZn6MuaEQIerwU1jF_4dwoleJiTdTXIPD2f3hLNI3oK8HhyvCRhyH0ISIoslRlRI4CVYIJgX8CrENRQLjpaYlv7sEDI-qhA_hpHO3YXMwVFQ5dK9Cefecna9iRdQBxm6mHbRw3ceWFECB-HWGYRbQci7fi-ZDQnepeB1KJeUc5g5laNn_DVLH3CZLqftFxmi7gc3YXCuViyDqmz8iMWm95b1Lj9eaIOh0_0UWFgMuJiKMTCQB8qPzxO8uyRJNuoSGnez_bS2cORPMq1kSL1pmGExy030lNDFPi03_5x0giBiGNbHBI2iVAK6zY6CZAPADu7u9YCkaszzSJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30210b96aa.mp4?token=fi0ESYyZn6MuaEQIerwU1jF_4dwoleJiTdTXIPD2f3hLNI3oK8HhyvCRhyH0ISIoslRlRI4CVYIJgX8CrENRQLjpaYlv7sEDI-qhA_hpHO3YXMwVFQ5dK9Cefecna9iRdQBxm6mHbRw3ceWFECB-HWGYRbQci7fi-ZDQnepeB1KJeUc5g5laNn_DVLH3CZLqftFxmi7gc3YXCuViyDqmz8iMWm95b1Lj9eaIOh0_0UWFgMuJiKMTCQB8qPzxO8uyRJNuoSGnez_bS2cORPMq1kSL1pmGExy030lNDFPi03_5x0giBiGNbHBI2iVAK6zY6CZAPADu7u9YCkaszzSJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمی هنرنمایی از رونالدینیو تو پاریس ببینیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/103473" target="_blank">📅 19:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103472">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7767f0d57a.mp4?token=dm8MsTfLA_Iz3WYeRoO_fxbijXMDMRYROthpLwM5ZgjWCbaylGR88ZulhVeqVQEVncruXRe06TWAXMW1-F18y3Fd5-hL_aa1mneUbFmHvBYdHHn-QjqeR9SBsBcW6me--4juHfHiu78JkHZ2Rc9syGcOu_nZgzWwRx58eR79V-TIKfsbvFmoe7WYHhZVIHl6m__3nJiCtMUf7H_dGD817ODovtD4FLQADFPfj_yFakqro-ahs7frwaVtLtV_Gukcm-VJoJGd-3FAmNLUbnQ0L1KpRV_3daIeSog0hMMbhX7LY7NJKhUR5cyOI90mF22x9FCw7WCivDkFSbiKe8yWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7767f0d57a.mp4?token=dm8MsTfLA_Iz3WYeRoO_fxbijXMDMRYROthpLwM5ZgjWCbaylGR88ZulhVeqVQEVncruXRe06TWAXMW1-F18y3Fd5-hL_aa1mneUbFmHvBYdHHn-QjqeR9SBsBcW6me--4juHfHiu78JkHZ2Rc9syGcOu_nZgzWwRx58eR79V-TIKfsbvFmoe7WYHhZVIHl6m__3nJiCtMUf7H_dGD817ODovtD4FLQADFPfj_yFakqro-ahs7frwaVtLtV_Gukcm-VJoJGd-3FAmNLUbnQ0L1KpRV_3daIeSog0hMMbhX7LY7NJKhUR5cyOI90mF22x9FCw7WCivDkFSbiKe8yWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🚑
⚠️
پشمامممم از مصدومیت فوق‌کیری و عجیب در یک بازی‌ دیشب از لیگ لیبرتادورس آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/103472" target="_blank">📅 19:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103471">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b0dc101.mp4?token=Ybu6o8X4oUxO2RYcNUoOTPN_ntMvYW384K2OiIlKLa3TgQg8gGWVy971N_K6su-nkq3mmhezvT49OG3AsKpJOihx0_q0BhtN-ewy1TRuDBXqdd8KD8ZKhv8NZWsFexFWc3w4zYmU33LwZQPDxuQhUkM7ZBZCnIwcJPxdZeNy8fXX6BEjzz0bYxhf61jHxd7PsyQxzU7R81VI_fnKIuUGGgZOaubYBa0FXbmRWIY9SksrFpXPRiSV5lWm8S55NYk_sklYjzfb-OkZS2QmDsloNJBpeAAkKoN5pvktoRZunD1cLv25AOZq_D5bb6ARgH1O7voiCWPJNsxopHsqTljoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b0dc101.mp4?token=Ybu6o8X4oUxO2RYcNUoOTPN_ntMvYW384K2OiIlKLa3TgQg8gGWVy971N_K6su-nkq3mmhezvT49OG3AsKpJOihx0_q0BhtN-ewy1TRuDBXqdd8KD8ZKhv8NZWsFexFWc3w4zYmU33LwZQPDxuQhUkM7ZBZCnIwcJPxdZeNy8fXX6BEjzz0bYxhf61jHxd7PsyQxzU7R81VI_fnKIuUGGgZOaubYBa0FXbmRWIY9SksrFpXPRiSV5lWm8S55NYk_sklYjzfb-OkZS2QmDsloNJBpeAAkKoN5pvktoRZunD1cLv25AOZq_D5bb6ARgH1O7voiCWPJNsxopHsqTljoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل محمدصلاح در تمرینات ترابوزان‌اسپور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103471" target="_blank">📅 19:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103470">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVeqI8q0PvyILxdHAwO44DPcDr39XTB8bH1_NFYzE8T-t4BBov6nb5Wthv2TOdhk4CMpxiPbOtlub4ON821_-X6lFlMa46_S4evxXlwBawXJLw5vRsAj0_BlGGLDWpo2dTirPYoNea0yXUnVkTI8AHHMQAD2M6FCT7f2rhjsKsKnNuVlJfSIf8MUhqcAMePxTlKkU46B72ouAtXWa6dHTut1lQIcz2KEct9DtQ4YMYpZUZJVomq7wi8DZNcEonpNTzIlFycPkLV7tVGV5Sfe7LPBuGDr3EFT6DjF89yTyQMstdRdxLKG1YTYkRe0gVa5g4UtWLxTb1xUdGUHPZiRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⁉️
ایجنت کونده امروز تو شهرک ورزشی بارسلونا بوده؛ پریمیرلیگ در کمین است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103470" target="_blank">📅 18:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103469">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd45c75847.mp4?token=KBwBwYdYm3wvc34fzKFbACqlEnH5nNyer0VECqh70uYXiHm2SewE9BhEcJVqUgDnZYTGcbSaDqTYxsY3WXNZPDO2rjil-FrerFqOg8Rlph8JFC3QEeUY6S4MmE0WiqjGsWKhHjPutVZB5rXBoBAbYcfq8JeuZd-Kk_hXKoJty2aK1_Ksp_xiBQjV-byqPhTVm3FpdKzR-8dE_iw_X88JTx3OZARJuaog5gYGWc4wyQ6eThhCBJgmJsuKH5aNT0XQOgDwIrnazD-rGs5Nc9C0NwRdYQeUDIrjSoO3aiK7ObkJmyhwbR33VVRDdYYkapaErRmmkEG81w1W998Kd1f9qkcsvjqcdqiFzv4OYcQyfQSV_pnvEfHrZZoV62gVBCC3LtjQal7dLlLgcc2BrVZeprB7qWJ6xRg6X_s2xDRiU1ZfvEc95rBmeAXjDk-TK2PxJjd6YJ2NnfDoHhSSNm322qFhzj2BAjW_s_8lXXJQizai8cyG2YZ2_2YVxgRdmrmGcCIM_n6a5y42E_ivkDhl1hEiT8_1Atu1uGrON6o0Lnp4_kCdOYSsHwAQ_Q06xMYcNlgHwJbq8JgJEMkg8SFzTa_nACK6L95toTni26B_NruLmGbzk-Y7cmxnmeS022xP8EsNRYPErsdvqz9vaDoVBjprKiUJxawraaAQkZZDwTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd45c75847.mp4?token=KBwBwYdYm3wvc34fzKFbACqlEnH5nNyer0VECqh70uYXiHm2SewE9BhEcJVqUgDnZYTGcbSaDqTYxsY3WXNZPDO2rjil-FrerFqOg8Rlph8JFC3QEeUY6S4MmE0WiqjGsWKhHjPutVZB5rXBoBAbYcfq8JeuZd-Kk_hXKoJty2aK1_Ksp_xiBQjV-byqPhTVm3FpdKzR-8dE_iw_X88JTx3OZARJuaog5gYGWc4wyQ6eThhCBJgmJsuKH5aNT0XQOgDwIrnazD-rGs5Nc9C0NwRdYQeUDIrjSoO3aiK7ObkJmyhwbR33VVRDdYYkapaErRmmkEG81w1W998Kd1f9qkcsvjqcdqiFzv4OYcQyfQSV_pnvEfHrZZoV62gVBCC3LtjQal7dLlLgcc2BrVZeprB7qWJ6xRg6X_s2xDRiU1ZfvEc95rBmeAXjDk-TK2PxJjd6YJ2NnfDoHhSSNm322qFhzj2BAjW_s_8lXXJQizai8cyG2YZ2_2YVxgRdmrmGcCIM_n6a5y42E_ivkDhl1hEiT8_1Atu1uGrON6o0Lnp4_kCdOYSsHwAQ_Q06xMYcNlgHwJbq8JgJEMkg8SFzTa_nACK6L95toTni26B_NruLmGbzk-Y7cmxnmeS022xP8EsNRYPErsdvqz9vaDoVBjprKiUJxawraaAQkZZDwTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎙
⚽️
لوئیس انریکه: فوتبال اسپانیا یک دهه است که در بالاترین سطح قرار دارد؛ مسیری که لوئیس آراگونس برای نخستین بار پیش روی ما گشود و البته بارسلونای پپ گواردیولا و حضور تعداد زیادی از بازیکنان اسپانیایی در این تیم نیز نقش مؤثری در آن داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103469" target="_blank">📅 18:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103468">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcIrSkrUA2caG5EnnEHvEmsYkQfWK_Dn-O-ZZIjID1eEVBBxtkcF161vhBXsrFpqyIgZxb2ogX3PMxZ6TnG6dLL5Kpeh7Y46JM-gAuOGogzmFbyLf-TBNOSzwMAP6wq_G52Q--y9lpYzTttGwblWz1hQZ-oKbUmrDRfF7yA1p9URt6fcG_b_VL3TpT_nt61JTaNUWs8SCr-NjZuRYR4DRIMaITubyDPiER343LSW17EQrt-8A7epSzUyd8UN6dT_-T7Lm2ajxHHtn7oluf6KTRccvelpflT4QUPB4zhwF2k20kqss77YykHHrSejxBxBci8ICrS_KjUk3RU8RwhWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رسانه ESPN برداشته عکس واقعی دست‌های کریس و جورجینا رو ادیت زده و پیر و سیاه نشون داده که این خیلی مورد توجه قرار گرفته :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103468" target="_blank">📅 18:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103467">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e531436fd.mp4?token=JheHa1D3D1GSdHm5BaCLeyFDLk7AjcuM75fnt9m71GrTwmuaR1jkQ6KyGGwcmJ7u2UmvD-CP5k4Ki9jaGwf9W-p5whN2637h0_JVeMd8qHIrzQnO76qyl_NVw72C82aPbuM-MmA3hgEQiv-w2BvVh52thl-bldn5SUUXXZN7v5zRFy0pZyKknbclAlghKcVxtDqFkT72LLW8JCDFie0B32dr3V25540cBGljikuhmo6ZenZhh1cz5txuqMIPpe0IHrqfTZgOeR1hXacel0CXvE164NxDUlHU21pQHZ7O5Pqau60h7-Ia1VWOqmcBXIaiVso__1OxkhHEDY6BidUXrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e531436fd.mp4?token=JheHa1D3D1GSdHm5BaCLeyFDLk7AjcuM75fnt9m71GrTwmuaR1jkQ6KyGGwcmJ7u2UmvD-CP5k4Ki9jaGwf9W-p5whN2637h0_JVeMd8qHIrzQnO76qyl_NVw72C82aPbuM-MmA3hgEQiv-w2BvVh52thl-bldn5SUUXXZN7v5zRFy0pZyKknbclAlghKcVxtDqFkT72LLW8JCDFie0B32dr3V25540cBGljikuhmo6ZenZhh1cz5txuqMIPpe0IHrqfTZgOeR1hXacel0CXvE164NxDUlHU21pQHZ7O5Pqau60h7-Ia1VWOqmcBXIaiVso__1OxkhHEDY6BidUXrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
گارناچو در آخرین تمرین استون‌ویلا پیش از بازی امشب مقابل پاری‌سن‌ژرمن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103467" target="_blank">📅 18:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103466">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103466" target="_blank">📅 18:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103465">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6vOWUPxEtsBm-xy5iJQe_A_kUtVQRqCy5EMULI-n4m7rx05pKpQWqxUTMn48CMy2d1VLcmLaQkMuPc73_XSCluTPx2FHVbiQvRNyqyOwBXir9Z5LDc1dI_9j-BWyabH9UMN2WnwZoutNTcMtSoUx8ypoABth7rphLzKOU78QdIRJS_nk-8_-9eMykEU-TRCCF0LOB0SuNFDIN6fKLCefwwkwVSNokW-I21sKteHOaxCQ3m2YOpBG6nP-KWbrATW1Z_PYw0tNO7JwoPKftZ-la7_Pj53o7EfCL4GEaac6_VNZZFRhH9ExvgSZWEmjN2IvyAtMgjugc9N0ou4l7EjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
g21
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103465" target="_blank">📅 18:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103464">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5acc84a7.mp4?token=r1XPTObInGO-JRJdgGtgjL3oBR5WWLyDNkNfriprYP3zrHQZ6Rz-UNrVFKPEgBkGTLQAUoREOPMoMrztx1FHiNdu63Pu26XhbNCrxWgEevgS0zV-mlT5XEjuNLfWCu3JMHsdQmTpOz3EG4LwTkNFi452L5jNDphul0No2D9TK0XGfBAZq-k4xyMx1TEh1k4JO8Mz7YF9e5AXVm1SyySMMdUPdPdbPej6Jbn8N_-oS65Lh0K0Q4rh1htGr2tS5Jr1zgSRnceh4zE3RmgkVFNJt_WCEKGAyDBSmB-VeLHiQev6aIuW3zshUru6CebkldCnwmaPGAOZp_99eipLOckLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5acc84a7.mp4?token=r1XPTObInGO-JRJdgGtgjL3oBR5WWLyDNkNfriprYP3zrHQZ6Rz-UNrVFKPEgBkGTLQAUoREOPMoMrztx1FHiNdu63Pu26XhbNCrxWgEevgS0zV-mlT5XEjuNLfWCu3JMHsdQmTpOz3EG4LwTkNFi452L5jNDphul0No2D9TK0XGfBAZq-k4xyMx1TEh1k4JO8Mz7YF9e5AXVm1SyySMMdUPdPdbPej6Jbn8N_-oS65Lh0K0Q4rh1htGr2tS5Jr1zgSRnceh4zE3RmgkVFNJt_WCEKGAyDBSmB-VeLHiQev6aIuW3zshUru6CebkldCnwmaPGAOZp_99eipLOckLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
حرکات عجیب و جنجالی مجری صداوسیما وسط برنامه زنده؛ رد داده بود قشنگ
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103464" target="_blank">📅 18:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103463">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de251cf467.mp4?token=FxAGE02nLa5RmJPIGnzDvBemIt9kelxSLgrP4WLeL_vfph5SXNyNjrxF9ih1brG94uZne1pn0g32YezSpOe0GOClAA_pt4ZoXbIqOkekXSXxfovTyrswvo7RNOkWUpU1-2DMIwesB7y14mOWhVapa6vs7J0LX7WH_lRcaqr3om6sAei0JIr4oiZ06SFSjYqqqsWGurClqqhvdL0Y7JNKLgQpzr2mpqEErYb6fRYKqDHjl7GZDn2iwoUNJOjNF5hRyDgqZ6vYXCfpelNqdSaJG_9Sczcy_A67H6J3Ce-kQ9ZvPOyf7Zyk2Fe77FvscceeC8niBlk0nUo78vgCgn43aAnLGH7jtUKDmZ6X_fxIPt6rc-mGFtneLHy2WDy90JaQoLNZdkMW8knVpvtelqJCCDfR1YNgsKwGbPBIkuMbgbrJFoZO4Hdr3TlrXOAFoLBdPl9_GXIw7k3b4wJHzl5ZImjcz9TLHsC9_aesAFL9p2clguAL7KwZy4JuchohMp1wMyAKLhgCmk4TksaDd93k3dLLNWPa8Ps-Ex8MZ2OMPzQnAkT8bv8sECT_JY2h8LZuN9qxGyteqgRhT1KyE6gwg-dtqu4hpjs99BWLyxkP2mjDsOPcpd_cq364xMTlBkz6xRB0RxprkZHsqM8AINkC_m55OQ48NGrOLfHxATG_KuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de251cf467.mp4?token=FxAGE02nLa5RmJPIGnzDvBemIt9kelxSLgrP4WLeL_vfph5SXNyNjrxF9ih1brG94uZne1pn0g32YezSpOe0GOClAA_pt4ZoXbIqOkekXSXxfovTyrswvo7RNOkWUpU1-2DMIwesB7y14mOWhVapa6vs7J0LX7WH_lRcaqr3om6sAei0JIr4oiZ06SFSjYqqqsWGurClqqhvdL0Y7JNKLgQpzr2mpqEErYb6fRYKqDHjl7GZDn2iwoUNJOjNF5hRyDgqZ6vYXCfpelNqdSaJG_9Sczcy_A67H6J3Ce-kQ9ZvPOyf7Zyk2Fe77FvscceeC8niBlk0nUo78vgCgn43aAnLGH7jtUKDmZ6X_fxIPt6rc-mGFtneLHy2WDy90JaQoLNZdkMW8knVpvtelqJCCDfR1YNgsKwGbPBIkuMbgbrJFoZO4Hdr3TlrXOAFoLBdPl9_GXIw7k3b4wJHzl5ZImjcz9TLHsC9_aesAFL9p2clguAL7KwZy4JuchohMp1wMyAKLhgCmk4TksaDd93k3dLLNWPa8Ps-Ex8MZ2OMPzQnAkT8bv8sECT_JY2h8LZuN9qxGyteqgRhT1KyE6gwg-dtqu4hpjs99BWLyxkP2mjDsOPcpd_cq364xMTlBkz6xRB0RxprkZHsqM8AINkC_m55OQ48NGrOLfHxATG_KuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📆
در چنین روزی، در سال 2003، باشگاه منچستر یونایتد با پسری به نام کریستیانو رونالدو قرارداد بست. و بقیه ماجرا رو تاریخ نوشت..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103463" target="_blank">📅 18:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103462">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXBpe-L9Qz79z1FOv_BeoBVhthGz_svSGGOw8Zz9ESYQMnIx9dxKl6dv2Ol1Z6cRRXwDgqYFZj4s4BTXFUbvZohSKXHKZH0xAJRCuiI7PyQwN01fifv64H1CXjrUeVTprEUFmFNbvxaQO5aTrXaF4jLeE4u1KgWN7ufZGhgJVIclYfiOlcVHPQecU2_4TysomA2W8qHn8YT3pzpVEXR0azup1Bnot0GB3ueC2pNTRRrdHZIaIGkP3zU1qcbOw1Uegc1MWe59xJdKqaB-N10mHeL9PIl5XGkInl10I7yUxb19YOffjYFAyL2mJkFiln30kNqYc0Ae_EOeQ_IXrM91-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه دو تیم ژوزه مورینیو در رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103462" target="_blank">📅 17:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103461">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b308ef230f.mp4?token=le0tgxt09DHdvlidp4uQmOuU6s7Pfq997CJPmi1rP6VdsoanoGaTv5jcgjh1_McTDFtjrtb_SPirkg2ro8VR-_SFqXWD9FqaY7m-2ua8GAQFm4ki89cTmne0RWr_szeawUD1oKsyZZ0T0vflqtR69L_shJUsxiiNwqOdZjPWRT7mlVt6Fc1UCF_gbJuW_iLlt1pg6fhbMkWSBbCgqYunryrVHN0DMWhRh1ewExdMucSO9GhMEiVY9t9WpiNpfkSCzHCEMltjpwunZipZdmbjrPBZ7oH4HK1CWLGllTLyI_iqUOGO_BYRBVjqjNb06a0MQdMmMjuqzK-em36A7_b9LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b308ef230f.mp4?token=le0tgxt09DHdvlidp4uQmOuU6s7Pfq997CJPmi1rP6VdsoanoGaTv5jcgjh1_McTDFtjrtb_SPirkg2ro8VR-_SFqXWD9FqaY7m-2ua8GAQFm4ki89cTmne0RWr_szeawUD1oKsyZZ0T0vflqtR69L_shJUsxiiNwqOdZjPWRT7mlVt6Fc1UCF_gbJuW_iLlt1pg6fhbMkWSBbCgqYunryrVHN0DMWhRh1ewExdMucSO9GhMEiVY9t9WpiNpfkSCzHCEMltjpwunZipZdmbjrPBZ7oH4HK1CWLGllTLyI_iqUOGO_BYRBVjqjNb06a0MQdMmMjuqzK-em36A7_b9LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همیشه اخلاق رو تو ورزش سرلوحه قرار بدید
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103461" target="_blank">📅 17:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103460">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBwE-czU5oYw7nujG-hTaWFIYCRuUJpnGqFxoZv4s5g1BIy-dQic2BFj63nyej8ns7_V5pjJMJsPpzrkr2yHVXvS5Q4BmTcShohPvF9WOT8TRo01HA4Q6s9UAJXYoqcysbMipCc9B3vcOEyPUDJAMmoFEHFC9Re8eWnz5HKltAPucEV4bcaM4D-3RmldW99Szn3FSk78liAFZtvlUVnjkshauS-glVQ3b1uIPI5eVfqFRUObA48iSr-wHWvnHjHx4dILU__-u_mlo20gR5KSEKT-zKwy_UiRXIcLfPRfFq4kOGYqRq36XXA9Y42C4LbxdiDk43MLWkGg7_BxvalNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو: جد اسپنس از تاتنهام به اینتر میلان پیوست.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103460" target="_blank">📅 17:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103459">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42b3af2b9.mp4?token=QrT3rmFO5C_k3hhvLCknR-9dEyOAFwRalwEI1lDGWu4KD13KLy_iRBHN-cRwgN6o2NnHNZIrrEbUempMLpX3K3Tsv7ltF9JNWx14uRvQNIYCqAFEIq4ii592B7RQ2SLFVXsxlefibMEgMLS7XnkPbMEOGCFLhx-0HCl6F9qu-J7P_gS_pQSIhThYZ751bVR4LUdo-mz5OCMJ8CeEKlVK1wbpViRj9TcnMf4w3GhwFYnnOgYfQLEaXdPLNAcz6mai8SGGJUTK7cJFxMcrXuEW1xLr61c0a5Mf56IAho-DdDhfGZoA_oscWEbQx3C9S6XupJhjb2WlOaxJPVyrG0c7jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42b3af2b9.mp4?token=QrT3rmFO5C_k3hhvLCknR-9dEyOAFwRalwEI1lDGWu4KD13KLy_iRBHN-cRwgN6o2NnHNZIrrEbUempMLpX3K3Tsv7ltF9JNWx14uRvQNIYCqAFEIq4ii592B7RQ2SLFVXsxlefibMEgMLS7XnkPbMEOGCFLhx-0HCl6F9qu-J7P_gS_pQSIhThYZ751bVR4LUdo-mz5OCMJ8CeEKlVK1wbpViRj9TcnMf4w3GhwFYnnOgYfQLEaXdPLNAcz6mai8SGGJUTK7cJFxMcrXuEW1xLr61c0a5Mf56IAho-DdDhfGZoA_oscWEbQx3C9S6XupJhjb2WlOaxJPVyrG0c7jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
استفن‌کری اسطوره بسکتبال امریکا و فناش
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103459" target="_blank">📅 17:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103458">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e09EGPOpNALmZB-ZV050JhQfsUJkSgGDzhg-gfesgJdnTDdGMbzhJe_XV-UEHHk5t51C8exoAHeFokFRfvk7k-ODKZWTraOQp8U8xAl6LhpN7L08G4rqYgvEy-1QefVlaMIQmpbKkeUZG23tH6YXk9vJalQVTYoaE6iR7Ik30JxQcle4F6VbIW13X-MMpXCpKXyiZkSpxlyzlsK34eHIo53uV5dk9dN0bU1YBiiuYjpyU3iJvXrai0Xa69pHEJbLEE_GVIoy3UAAE2YNW9jtFcczYn70Fg9n8yXHUBgyP0MyWBohNBQzdoxv1mSFgs0MbXnva346kCAFj8GXYLMQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت کریستیانو رونالدو برای مسی: لئو، در این دوران سخت، تو و خانواده‌ات را عمیقاً در آغوش می‌گیرم. به تو قدرت فراوان می‌دهم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103458" target="_blank">📅 17:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103457">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKIMMND9TJXXRPsP8xruKlG8cQy0_cV0cC3hmu37L-rjoSC1m4sSUH9jKhfdZt4lOuezOT65P6XiGTsfg8Qqdvzxyp9Lt3P1IbDNdc4CId5I8MZO8EsrGIqqd1RiXMnETYTtSsMmJhIp4d4tTI0IXLRBEL5RNpc58buqjtJacHfW6SuFe56JNXG3C2uwwM9OR95hu7gumDF_ZATNHKYbYqvd0-MR2P8NQzPPJ11H5x4mKAJVqWjZkpGCqbkyaCSzlw3_v4nmLvDodupU4Z9J3YWZjN2T4jdt74JMgaQ3W01RX5ID-8RX67b8tz1W0KLhDwbczkS5SqtovdHj3V1ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📷
⚽️
بخشی از پست احساسی لیونل مسی خطاب به پدر مرحومش:  نمی‌دونم بدون تو چطوری باید ادامه بدم؛ تمام زندگی من فوتبال بود و الان واقعاً شک دارم که بتونم خیلی دیگه ادامه بدم یا نه؛ تو از همون اول کنارم بودی؛ تو پدر، دوست و مدیر برنامه‌های من بودی؛ با اینکه گاهی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103457" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103456">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48116d0ce.mp4?token=DIlqguUXZIf8IS5U-oVA8EhAEZ-X8nuX-7P9dQd_UbDP-I-VjAjdAasfu95qaJB-oKtrc-HW_7tsCFHOOA1IBIA7x0nabUpdlEeoHfHMAId77fEZ5o3uOP7nXN4m0He7Q4OnPMYBPwHK93dyMX-h2UiimIfhNmKR89lkEca5BBFyvkDN83smpFhELF9n1z5MUQynW87n60CshVb2GXWZxjUFtjow8lSgnSZpYFu6hYBLf4-4ynX32W0Scq0A-foSQP8mHvSuzxK7R_rFAywuIrH8ChtvLWNl-4vaUi43FXbLiSAIJhTOAKNXJ-FXDvqk88K7kOZFNYH_1Wnyv3SMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48116d0ce.mp4?token=DIlqguUXZIf8IS5U-oVA8EhAEZ-X8nuX-7P9dQd_UbDP-I-VjAjdAasfu95qaJB-oKtrc-HW_7tsCFHOOA1IBIA7x0nabUpdlEeoHfHMAId77fEZ5o3uOP7nXN4m0He7Q4OnPMYBPwHK93dyMX-h2UiimIfhNmKR89lkEca5BBFyvkDN83smpFhELF9n1z5MUQynW87n60CshVb2GXWZxjUFtjow8lSgnSZpYFu6hYBLf4-4ynX32W0Scq0A-foSQP8mHvSuzxK7R_rFAywuIrH8ChtvLWNl-4vaUi43FXbLiSAIJhTOAKNXJ-FXDvqk88K7kOZFNYH_1Wnyv3SMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
روایت‌ قدیمی و شنیدنی ژوزه‌مورینیو از شکست مقابل‌بایرن‌مونیخ تو نیمه‌نهایی چمپیونزلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/103456" target="_blank">📅 16:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103455">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nch9XcLqFNHd8naPmzasEAgw0LIEsSeR23lSbAuapNUxRzapF7xYzgWViyZCNnNZv18EAtQx6DmVSfvy_6rOn63TokDyL8O7DazQPIXx4Oky6NYNH3yaKu0wGVZV7rIQkPZq3EB28zw3Q893ust6XvbWHyGmhXYDan6aGDOgONjKPCSAAE7iUJfjeRoZrTfRJk4aFXZyhmxaDU-58Sx326u1q3C-qWhqeS8UgsFfobcoASjsPWo1tYYARgu2weBUnIIW99r9MftynMKQG64e0TiKbteskx3rcjFsydazVntsUl9AGYcYqCUdBDO5BMrAAPyuEyMPNDuyLS9Mc9Dugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📷
⚽️
بخشی از پست احساسی لیونل مسی خطاب به پدر مرحومش:
نمی‌دونم بدون تو چطوری باید ادامه بدم؛ تمام زندگی من فوتبال بود و الان واقعاً شک دارم که بتونم خیلی دیگه ادامه بدم یا نه؛ تو از همون اول کنارم بودی؛ تو پدر، دوست و مدیر برنامه‌های من بودی؛ با اینکه گاهی با هم بحث می‌کردیم، اما همیشه حق با تو بود؛ خیلی دلم برات تنگ می‌شه، اما همیشه در تربیت بچه‌هام حضور خواهی داشت؛ ممنون برای همه چیز، دوستت دارم پدر
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103455" target="_blank">📅 16:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103454">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e1915bb6.mp4?token=gd50LWeOC2Ex3MIu142iWqu3EwPDpmhhmWxlU9JN--lTtqjqpbo5xTAJgv9dhUExa-Ld_NjcP98dReelgL4faclGz-k4jKZr6wuAzYdv1pqlbIikL--hFqptN9C5HYrQQLmQ7AGirTjjtAPWrjnqJ1gqrWLxwyR5jTCQcJNgLZnkTQENOtivaMLnNO--Vat_bMrZKQf9COMVSb4bB3CZUEO2OmaCvFFaWrXBwD6zgJcPP_Qn77Qj1gVK6gDQQB2P9wddKD8JehGJsQRBGuxaSkA6DCkYqRd7dcJ6fVJKiZBpTD51eqxML70VuD12kP95pS9gkyqrelzGB0B4GtdHoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e1915bb6.mp4?token=gd50LWeOC2Ex3MIu142iWqu3EwPDpmhhmWxlU9JN--lTtqjqpbo5xTAJgv9dhUExa-Ld_NjcP98dReelgL4faclGz-k4jKZr6wuAzYdv1pqlbIikL--hFqptN9C5HYrQQLmQ7AGirTjjtAPWrjnqJ1gqrWLxwyR5jTCQcJNgLZnkTQENOtivaMLnNO--Vat_bMrZKQf9COMVSb4bB3CZUEO2OmaCvFFaWrXBwD6zgJcPP_Qn77Qj1gVK6gDQQB2P9wddKD8JehGJsQRBGuxaSkA6DCkYqRd7dcJ6fVJKiZBpTD51eqxML70VuD12kP95pS9gkyqrelzGB0B4GtdHoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورزش کشتی در بخش بانوان
🔥
😅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103454" target="_blank">📅 16:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q8bgnc8W0WGrhzmRT87OrcrnDzEqfnovbeQdCKzxA-0_s9BfilpROe4kPcYSrWT_D_QtO2jHjMDsAA4OG6rSMagNuN8d0qZ3ZVlutNtARDW7HYFgLm4XcenLroEiHdthD88ONBhJD5BjYj9hXC1vDz8ch1Z_RuGPF3YQ6X_XOfNriSX8d7y-FvuO_k1569rioo6kLS99Jvw6dvo4aFZz9MFAe0eJJYDYAA9vKHiT7AhZzCLdP3vYIkfnpooxRwRzC6W1wlJrwkY80GNNdquhLZExg-sEh3PcXEXakiQeXCUsnmoDvC8els8KcXX3zPmJdq4d-SISjziBm-TLNw1nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/He0xV3tNsX4k5NczZxlb7nFIpObIvwHwEqV8R4myBLTJlzkUKSCy5uVSjAKsGpNbSHT6BZu3oLkTWeXeqDnzh4Hx9yD4AanxNyYMe0zZPq-RDUQ3Xwj5YK4Bta7eMwBhbQ3OF166--DuqEwjtsnqS5qw4cZd5pADcS8kPFl-aZTzwpg7wDkwo6UclYTVP2upnx1qV6max2yDbo7TPLb4xEMqezkNMlFsOQvVwS-PvzE2tkf8SDoDLmXBehlSJVjx46sItTdbWVhnyuC9eKLVzTbjyAQXpkj0EGHnjeX5mm5l0RCCnQwgF9mvD4ms65aqlRuQGSwbQ0Hck0EJWL1Z0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😃
😃
میلیتائو چرا داره خودشو شبیه شخصیت کراش میکنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/103452" target="_blank">📅 16:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3653017ea0.mp4?token=P8H42N-V_vntJdOygUz07PDyXIy6QH97kwKdIwTep_wRggWdAB_oRKWcK7EBqgLBX-9czW4ixB415QshMDaPhQ6wF5XxUmqo7wxA779HzumCSYcsYduZ7_0DtKn-21Lz1f_zOf5ecgHU8yAIBrFRzEGrgmEsy-IUmHFrNflaHL4tYRbssiFdEtzUjOZNnGZV5_XoC4qxqol9a0PjOuPcrHQa_sSG_3Z4INoWdUu926E6QMWGlTsCgqCKZNEdnRksm6yK_EnuZyMSxlryg8zIBVZlq9sznnRiw0qmX5CnSj6oBqHYunKPccaXqey2GpwbX_U10k3Cb_HnIs1ZVLw1LnUCPSOT2VgDjmBBG54YwByqiVFwPUe75Sg3hQR8T9P3PZXuXhPKo9L_lQIq3dwVio0G4hsblMzWs_DrqF1hg2D4Nv51s-s-lVel-Ev3EZhNC3FsJmzVehbput4AQvKwdqQvAPj1EYKUbFxN8vWU7GZLdRNReEVsBwlWrA42i69Vxfdr1rCS7iLDYdvUXis99-uvSq-aun301deKYsFoRlDXx3K6-w76Pw8X7pzeURfNzZKFNqHjYcUOPdcM7j8BJDj1gw1Id2CFW6n6bO-hRMXpvkYNgJzDvE2zo2aeK0Fg-xkTY14Z-CexVnqZcUwYXIc1AkD82ERTp3g7ds511hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3653017ea0.mp4?token=P8H42N-V_vntJdOygUz07PDyXIy6QH97kwKdIwTep_wRggWdAB_oRKWcK7EBqgLBX-9czW4ixB415QshMDaPhQ6wF5XxUmqo7wxA779HzumCSYcsYduZ7_0DtKn-21Lz1f_zOf5ecgHU8yAIBrFRzEGrgmEsy-IUmHFrNflaHL4tYRbssiFdEtzUjOZNnGZV5_XoC4qxqol9a0PjOuPcrHQa_sSG_3Z4INoWdUu926E6QMWGlTsCgqCKZNEdnRksm6yK_EnuZyMSxlryg8zIBVZlq9sznnRiw0qmX5CnSj6oBqHYunKPccaXqey2GpwbX_U10k3Cb_HnIs1ZVLw1LnUCPSOT2VgDjmBBG54YwByqiVFwPUe75Sg3hQR8T9P3PZXuXhPKo9L_lQIq3dwVio0G4hsblMzWs_DrqF1hg2D4Nv51s-s-lVel-Ev3EZhNC3FsJmzVehbput4AQvKwdqQvAPj1EYKUbFxN8vWU7GZLdRNReEVsBwlWrA42i69Vxfdr1rCS7iLDYdvUXis99-uvSq-aun301deKYsFoRlDXx3K6-w76Pw8X7pzeURfNzZKFNqHjYcUOPdcM7j8BJDj1gw1Id2CFW6n6bO-hRMXpvkYNgJzDvE2zo2aeK0Fg-xkTY14Z-CexVnqZcUwYXIc1AkD82ERTp3g7ds511hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فوتبال در هوای بارانی در کشور هند
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103451" target="_blank">📅 16:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103449">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a91054b37.mp4?token=Dn9SwONU2gBL5ZobcHHKHLobDN_IfcWzT5JEv8_BDoaC04WlftnUBV6kzOfrcuh4qMvtL131xUIubn_3ENeEUa7YIpyW-hcRbz_DnYrsF31HexxXby87395a0GuzKcjkc_4dFkP2cE7Jo7QN6gpKLxbe0ufLKh38yMQlibiGybdKZ3PA76hKSTsk1Ecsq83zsP3YmvMsAttfJJetQKWMrFRFiZu3wmeRaS-fvoCQgW88LC7dkxOZKUsS_dAtx9qef5cOLNfUE2q5G1WTeD55jXMILELjRZvp9_30E4Cm0n6gp_EjOkIhYuUAP16QOwne9NYh15zIlFk5hDWG70U_BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a91054b37.mp4?token=Dn9SwONU2gBL5ZobcHHKHLobDN_IfcWzT5JEv8_BDoaC04WlftnUBV6kzOfrcuh4qMvtL131xUIubn_3ENeEUa7YIpyW-hcRbz_DnYrsF31HexxXby87395a0GuzKcjkc_4dFkP2cE7Jo7QN6gpKLxbe0ufLKh38yMQlibiGybdKZ3PA76hKSTsk1Ecsq83zsP3YmvMsAttfJJetQKWMrFRFiZu3wmeRaS-fvoCQgW88LC7dkxOZKUsS_dAtx9qef5cOLNfUE2q5G1WTeD55jXMILELjRZvp9_30E4Cm0n6gp_EjOkIhYuUAP16QOwne9NYh15zIlFk5hDWG70U_BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
یه یارویی به اسم «پدرو» فلج مغزی داشت و آرزوش شرکت تو مسابقات سنگین IRONMAN بود. برادرش «میگل» تصمیم می‌گیره با تجهیزات خاص، پدرو رو توی تمام مسیر مسابقه که شامل شنا، دوچرخه‌سواری و ماراتن بود همراه خودش بکشه تا رؤیاشو واقعی کنه؛ حرکتی که به پروژه «برادران آهنین» معروف شد تا هم به بقیه امید بده و هم ثابت کنه بزرگ‌ترین پیروزی، مسیر قشنگیه که دونفری طی میشه.‌.‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103449" target="_blank">📅 15:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103448">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X951I_-k7d_ckjWo73xcG5uicmjwH3q1Milwn2L0447ISjOOJcCNupbDGAYvDOryu46He_CE56DLPDb0B3tN0G7fUqJ8rhml7m9_wwnO4D7tRyq8fprZo7rBUQiFpTT4VbxcHGqZSmM3S3F1dqQ4o5S6Ne1OQ40yvvcY0AVOvV_ePRbYVzsa4WijUKt3dBPPz4FDzfQ458bxVRXmZaYY4pSuMqhKT62-DqEd2MxQMd6OuSP4k0vexPWw8S_7-JU_X2qyVeTguU9_LuQ_alH9_2gPxSmXaOwHebqJQKfK3waHmdo1rB3Y2KxqMUmw7lP9KO0Mju7-URX4U4pACuQm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
•
پنج باشگاهی که بیشترین درآمد رو از فروش بازیکن تو بازار نقل و انتقالات این فصل داشتن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103448" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a4a8150c.mp4?token=JA-Bk8WJtAexUKM3rNyfijCsuWLSg5mr1UydJhtae0ig5S4HNJsCjYIBkXhcn2vetOV8d2fYbA6y6eKPK1SAzz0xVsrIAuk2AYgTui9wDJbNYJbYxvmBHiIqrnArE1PnHLVGXZlcCpT_QBQHOJoJ3MNaMBkoINJhJbNpXDQfOwblLkuBZXgLZTTy8FsoaI5dYQ-2EADc7M846F1pLovV4Qqc2m9sCNQCKrUyFBKpAC1tvGTBzvR3m4JzcSdYxfJMCZOr01hJkb2hOoNA4ReneYpDG-49rFf68JPORPpshYt26gntmIm1TtNDL4hqDvq2pIkXgF-s_WLt4bS50F2UKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a4a8150c.mp4?token=JA-Bk8WJtAexUKM3rNyfijCsuWLSg5mr1UydJhtae0ig5S4HNJsCjYIBkXhcn2vetOV8d2fYbA6y6eKPK1SAzz0xVsrIAuk2AYgTui9wDJbNYJbYxvmBHiIqrnArE1PnHLVGXZlcCpT_QBQHOJoJ3MNaMBkoINJhJbNpXDQfOwblLkuBZXgLZTTy8FsoaI5dYQ-2EADc7M846F1pLovV4Qqc2m9sCNQCKrUyFBKpAC1tvGTBzvR3m4JzcSdYxfJMCZOr01hJkb2hOoNA4ReneYpDG-49rFf68JPORPpshYt26gntmIm1TtNDL4hqDvq2pIkXgF-s_WLt4bS50F2UKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
رویایی روز و شب بارسایی‌ها‌در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103447" target="_blank">📅 15:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103446">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7IFeWOYAoBJNZxG4VBxc0tRwko2vnGyTtzXdAvadnJenWFciz8OFcB4zsyH6vOPC_nUM-KnIOLsBEgi9zpR5xI500OFtt6Xkr2tftEghwYYYLelNrdimwkU07OotGV-IMQ3YKDJJ_lx5Uq4oIaVrxazy2R3j00fXWFpHabJFwTlktiWacW1WrWs4fB-dBn4D9JO3vxVFtMk-5xZGPhqMgTWt47pkc_TrlpGZvMprSY7FM83bnwN_sd-Afso126OiiKZaIZ_59BFuVkZND9jXkNDzof2Jnun_VYazttKdGrQDuZW1KqC4LaPlZc34Q3N0-oMNVNTkCtLExJiy35IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
پیشنهاد جدید بارسلونا برای جذب رودری به دست مدیران سیتی رسید؛ 60 میلیون یورو ثابت + آپشن
🔺
مدیران منچسترسیتی باز هم بیشتر از 60 میلیون یورو میخوان اما دکو داره مذاکره می‌کنه که به توافق برسن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103446" target="_blank">📅 14:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103445">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186aaefcf2.mp4?token=eQvFM77_BTvcfnoWj_i5dE2HZaYYkRLXuv6TTB5YUbL3kTv1z8nNHW3p4ha9OyDsNJp0bY9AeOlyadmMOs-FwDsILlkrkfq0_HoTTa1TkaUYtms-SuGuNINyBHaq0uEV2KSe42-IlRkVfw-L2E3O6p1UH_oamvpyW-Hq1PUQznCMF-rp_iSfS3zI1caDc89a5WysN11rXGkS5DbiQcJGsqLsnGfkQa462nW3LbffQX7LnqFL5df7hRriAY3SILEV79FSnmkn6P_jTEmJm759Xy1mnTxhVk6Y2Dg8t4oYC7tx5jkZirB4WZ081_-nyrs7QWgOZ_WuniE2zYXzl33McqsE135JK9Vt2w39nSIPbKriHo92gHnOHZPHGhhHktKToow2j4dvCxHriwRLJsqQw_p5oDE4rjFe84zmmf0HjyqQpuNcQIaOAjFroykRhDocpoSWgSOCN11DxA1t2FD3TzUKvL4vKnKG21RsfQ2QCMvNWHSFEFUvx3KJGmrAWWwelOnoVviIviHv7fuUGHnVHLtu8e5JqO2Kw-8bMx9RpHntKYd9WxdbRywF7WXDXlXnoVX5VJf1f9sFxP0qfoJZ_WFsIAwxcX0tMbPLNsTZh17RDd43Irror-Azt6aLBt9WP3JEnMXja4Tc9RASlVgHiwKUVenxggtC-1gMo7myt34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186aaefcf2.mp4?token=eQvFM77_BTvcfnoWj_i5dE2HZaYYkRLXuv6TTB5YUbL3kTv1z8nNHW3p4ha9OyDsNJp0bY9AeOlyadmMOs-FwDsILlkrkfq0_HoTTa1TkaUYtms-SuGuNINyBHaq0uEV2KSe42-IlRkVfw-L2E3O6p1UH_oamvpyW-Hq1PUQznCMF-rp_iSfS3zI1caDc89a5WysN11rXGkS5DbiQcJGsqLsnGfkQa462nW3LbffQX7LnqFL5df7hRriAY3SILEV79FSnmkn6P_jTEmJm759Xy1mnTxhVk6Y2Dg8t4oYC7tx5jkZirB4WZ081_-nyrs7QWgOZ_WuniE2zYXzl33McqsE135JK9Vt2w39nSIPbKriHo92gHnOHZPHGhhHktKToow2j4dvCxHriwRLJsqQw_p5oDE4rjFe84zmmf0HjyqQpuNcQIaOAjFroykRhDocpoSWgSOCN11DxA1t2FD3TzUKvL4vKnKG21RsfQ2QCMvNWHSFEFUvx3KJGmrAWWwelOnoVviIviHv7fuUGHnVHLtu8e5JqO2Kw-8bMx9RpHntKYd9WxdbRywF7WXDXlXnoVX5VJf1f9sFxP0qfoJZ_WFsIAwxcX0tMbPLNsTZh17RDd43Irror-Azt6aLBt9WP3JEnMXja4Tc9RASlVgHiwKUVenxggtC-1gMo7myt34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
لحظاتی ناب با اسطوره زین‌الدین زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103445" target="_blank">📅 14:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103444">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d1d4d2c8.mp4?token=lvBRETZpE40h-7pzmq1Qva_8IYxcQ-kgGjyjND8u6zoRZrA9fQSzed7UJhX6hza2BQ23-9lnwTtwP9yJCL0He05E8YOXUIDyHMprywPFLhSiLTSu_fF6paxuq8rPcnRMLKaho7LtV7v2EIYDiJFnNh6YOslhoxnw236_Tx58EnKGJCzD0HXSiI1D0Yj4T8_kJHbtqVxbFDoWWZUtRCWexArMbOZ5hGLLN1_4Y57Xj9RBxnedonZdA2oWP6FYlD6w4PgIfv5Fa8Wrq-JWwoEB3wKIfIo_glUZSaXiAVHyQtY-jc36MazB1Enp_PrUs7I9xw5ljbkbdzYCZkbZhkZghA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d1d4d2c8.mp4?token=lvBRETZpE40h-7pzmq1Qva_8IYxcQ-kgGjyjND8u6zoRZrA9fQSzed7UJhX6hza2BQ23-9lnwTtwP9yJCL0He05E8YOXUIDyHMprywPFLhSiLTSu_fF6paxuq8rPcnRMLKaho7LtV7v2EIYDiJFnNh6YOslhoxnw236_Tx58EnKGJCzD0HXSiI1D0Yj4T8_kJHbtqVxbFDoWWZUtRCWexArMbOZ5hGLLN1_4Y57Xj9RBxnedonZdA2oWP6FYlD6w4PgIfv5Fa8Wrq-JWwoEB3wKIfIo_glUZSaXiAVHyQtY-jc36MazB1Enp_PrUs7I9xw5ljbkbdzYCZkbZhkZghA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
دل‌هارو ببریم به سمت دوستان فوتبال‌باز قدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103444" target="_blank">📅 14:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103443">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fba285851.mp4?token=UHpGNDZoQ_3H6F2N5lX3pEvQiNA84jE6v8n1WR_PpdlNl0rsu4KHiDXJyU0kro7F_DSNZBc9Bm5WWZ3-ycu2jcE0E4JALZdVvZXQMwtl6R3_0vpZKfSSY12DCwLxs20juVKWLNmygSezswusDeBS7xWCVwtUEIfHXRRpg-ZVuc2ajATaOXts2QC1g2eeATVLBvZRJEHRJ-2gLykgDOB6Z7XxaJoxMAHrDchokpeDrFjFV4IR30fS7nDPAmn1WgFqWM17NmdgOTaGp3GuY1OuyoYPqiUywQVdwF3dZGdrRVGmG-btoR3-ZL-hoegT3eIIGavzg1_ac6f_EVFhfD5KfzssS-yiXO5hsEYguMXhiYylyxyPUB335RqKa4D0v59j6qtrUjAetb5Wrub2cY4_ofM147XDpKs_v5vIPDVncNPFqzg9ofOXzLla-N4sUbS_7t-CvQZwT42IDkqAhNfa4ytRxL0PENV47SAPUMhcZHpupFeydIx-rxCSmeCmfqAyDhY71ukoZjGNv0cWlQ0StuvwP3bAG7-lQdC5TsCcYAnROvE_bErp9xUhqM16Mlo0rQLOHQWcSGKPVFaPmGsxuPHSq5cCKSFJH20qMgbnORpwiK2MQcY3aMPVbqeoys4zSM-36T51X6_PsqGimwRQTCbmTiFtViZgkL7a2jXIvv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fba285851.mp4?token=UHpGNDZoQ_3H6F2N5lX3pEvQiNA84jE6v8n1WR_PpdlNl0rsu4KHiDXJyU0kro7F_DSNZBc9Bm5WWZ3-ycu2jcE0E4JALZdVvZXQMwtl6R3_0vpZKfSSY12DCwLxs20juVKWLNmygSezswusDeBS7xWCVwtUEIfHXRRpg-ZVuc2ajATaOXts2QC1g2eeATVLBvZRJEHRJ-2gLykgDOB6Z7XxaJoxMAHrDchokpeDrFjFV4IR30fS7nDPAmn1WgFqWM17NmdgOTaGp3GuY1OuyoYPqiUywQVdwF3dZGdrRVGmG-btoR3-ZL-hoegT3eIIGavzg1_ac6f_EVFhfD5KfzssS-yiXO5hsEYguMXhiYylyxyPUB335RqKa4D0v59j6qtrUjAetb5Wrub2cY4_ofM147XDpKs_v5vIPDVncNPFqzg9ofOXzLla-N4sUbS_7t-CvQZwT42IDkqAhNfa4ytRxL0PENV47SAPUMhcZHpupFeydIx-rxCSmeCmfqAyDhY71ukoZjGNv0cWlQ0StuvwP3bAG7-lQdC5TsCcYAnROvE_bErp9xUhqM16Mlo0rQLOHQWcSGKPVFaPmGsxuPHSq5cCKSFJH20qMgbnORpwiK2MQcY3aMPVbqeoys4zSM-36T51X6_PsqGimwRQTCbmTiFtViZgkL7a2jXIvv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚽️
چالش‌جذاب و دیدنی تمرینات لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103443" target="_blank">📅 13:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103442">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOVbDxsxFAwhgDQU6dh9v1ZTbbpnLdZ9dQwU3Sf6320iF_SqB4QHjBcPkZKuOI40c5-j3P57AVZP067-w6S9a8iJFVsu0_5XGjeKWq8SUrRq_i5wMn4kVYjDgNamDNWA_pSCMjg60XybYiZFOkNOWK7c3GfBSJQjSviB2s8WkxOnobc3djP-pQ-_IOuWL_amaeQRN3SciRYaRGHDdh_ecUOwce0Xf_LlhBYpHJm7Ga-fC8VFTgcafdgLksDX2j2tSGCyw6wTgO2jDrGJM7zuoJ-8sVqYowmvawHBrWsFGjiyxWMtA4afwSeWuwb7U_Uxrnt4ZHvhb1AH1eh4PRiyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
مودریچ و کارواخال، پرافتخارترین بازیکنان در رقابت‌های سوپرجام اروپا با کسب ۵ عنوان قهرمانی.
🚨
📊
🏆
کواچیچ، با کسب سه عنوان قهرمانی از سه باشگاه مختلف، رکورددار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103442" target="_blank">📅 13:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103441">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc3b0e5a8.mp4?token=hj-CnmPBeRfbkQSiaz5crrKDWKSMo-kpSryMGcx7rzp80CEYljiiCrhpNGfjNw-7hh6-IQWfSZZwJYALeemJrkeZaM28EZHc5VvUzFRjO68IqErnffasOBRHGFuN7wybYFlYfNQXQEQJI-yStN_iQZ1J1kKLA9cbYbdU8SXh4aWjEci_puWkknUYywXyan0-eeOitZCuhVclwTi6Hw-5r_8H3cWCbSMJM_TcsiW8GPqlJPBr5Ho_8Dk5trISrLJklz9pWSVWJWOGJvcpI48_huPG0yRJ7BcvBBriaF64XGkos7cXP9IVa005owgDFju30fuCLAphUuTxsLjWhiLExQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc3b0e5a8.mp4?token=hj-CnmPBeRfbkQSiaz5crrKDWKSMo-kpSryMGcx7rzp80CEYljiiCrhpNGfjNw-7hh6-IQWfSZZwJYALeemJrkeZaM28EZHc5VvUzFRjO68IqErnffasOBRHGFuN7wybYFlYfNQXQEQJI-yStN_iQZ1J1kKLA9cbYbdU8SXh4aWjEci_puWkknUYywXyan0-eeOitZCuhVclwTi6Hw-5r_8H3cWCbSMJM_TcsiW8GPqlJPBr5Ho_8Dk5trISrLJklz9pWSVWJWOGJvcpI48_huPG0yRJ7BcvBBriaF64XGkos7cXP9IVa005owgDFju30fuCLAphUuTxsLjWhiLExQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
💸
وقتی استاد فیروز کریمی بیشترین دستمزدی که در فوتبال گرفته رو لو میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/103441" target="_blank">📅 13:10 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103440">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79bf3a3f4d.mp4?token=ZllDaVjz8YlkkaPb1rufhhsQcBhbpub1RR6xcrlF8OrKAvBskWSmW6LdT4XVZX23Cdvrh5ZeWyx5znjyFoy4KErjKC63Dk-NTNJn5FS0G8aKrBRa_LVcI1--XoMqlHCHn1vLZ8035ZFjryB-uNr4puXphH-qV9gKDJhmhRsgCW5ou9y-rbEqq0GJoPqaf3EkvfqKEKUgnJAlyrFko8Yy5_JnjFCdXdsfHfrvB9Q7Dpg6OObtiYNB-ypfjV3So7OFMNuo9jZAvlb8vIlwseG6eYm9bpYgyNcH_BiIfclLEEnbHFX4Vk_Bk8qLZLwaqlyjGeCsR8zky7OMTMtHnEJZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79bf3a3f4d.mp4?token=ZllDaVjz8YlkkaPb1rufhhsQcBhbpub1RR6xcrlF8OrKAvBskWSmW6LdT4XVZX23Cdvrh5ZeWyx5znjyFoy4KErjKC63Dk-NTNJn5FS0G8aKrBRa_LVcI1--XoMqlHCHn1vLZ8035ZFjryB-uNr4puXphH-qV9gKDJhmhRsgCW5ou9y-rbEqq0GJoPqaf3EkvfqKEKUgnJAlyrFko8Yy5_JnjFCdXdsfHfrvB9Q7Dpg6OObtiYNB-ypfjV3So7OFMNuo9jZAvlb8vIlwseG6eYm9bpYgyNcH_BiIfclLEEnbHFX4Vk_Bk8qLZLwaqlyjGeCsR8zky7OMTMtHnEJZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
✅
بواتنگ از خاطراتش در بارسلونا و استعداد بی نظیر مسی میگه...
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/103440" target="_blank">📅 12:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103439">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUYS7pfaHSmA9s55TybZv7270XbCNC345NVXuQy6Rdhszg3iJdxFdiN4VQNUXvvrfz2BF8JWUvPX9J2ZMgJT289EK8Dhnh87bEv-W696RVjT6T2Cvr2637UcTTwGshGBTXGdUt4Q8iDG1SS8cC13H6L4ciLeqzwHmfB6fHQG2OAHXn8wgg46zQq--g2Cefha5syyfZNmIzrn11EVMIZBBLyT2tBOQ5PDguAu-CRxSSTtWZ9WvjOfNBo7fzojyLRk6y9gSX1tRKPw-C16DEGydrA6VL_sPP2fe3PXaE6akAg-Ca6fx5aY7LCaC8gY3Jc1CZuRiSJzD_3h_-JzbtJOyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇮🇹
🗞
رومانو: دو باشگاه اینتر و لاتزیو درحال مذاکره نهایی برای جابه‌جایی داوید فراتسی هستند. رقم پیشنهادی لاتزیو ۱۵ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103439" target="_blank">📅 12:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103438">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/531604864b.mp4?token=REFX26g8WM8HScE_169m9YQpNjj4VGUQ2l6kGIR1cdEvPwxqLr13CEjI6vYTbPKuWFjf9-4pMP2WmBG6UVeXZChd6iURgKmJx4SQjr-OICHX6G_UIopZvEhj8Y9OacWxvIxroZagcmaD-E44RE8OLclywBS4OP2g3SwTPrdFk3_NhApwC4ihF5SZM0vMNX_w1XMLGWfVLqw76x9EPsm5Nhs6t-mdf6GTbfEWncFZ8Fc5CyFeBevw-6P_2LnDlAn-_o-wtSa7xgVF_mhYaw31cySFzy30fZJA32tuSPsjVtB0Ko-C0W9SgqzEoDUv4sNxw2H1FX9WQfHkldMM43pkhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/531604864b.mp4?token=REFX26g8WM8HScE_169m9YQpNjj4VGUQ2l6kGIR1cdEvPwxqLr13CEjI6vYTbPKuWFjf9-4pMP2WmBG6UVeXZChd6iURgKmJx4SQjr-OICHX6G_UIopZvEhj8Y9OacWxvIxroZagcmaD-E44RE8OLclywBS4OP2g3SwTPrdFk3_NhApwC4ihF5SZM0vMNX_w1XMLGWfVLqw76x9EPsm5Nhs6t-mdf6GTbfEWncFZ8Fc5CyFeBevw-6P_2LnDlAn-_o-wtSa7xgVF_mhYaw31cySFzy30fZJA32tuSPsjVtB0Ko-C0W9SgqzEoDUv4sNxw2H1FX9WQfHkldMM43pkhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان بزرگ
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103438" target="_blank">📅 12:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103437">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHVnJ1GgZLSKz7gB96UEA61lcWRS8n7SsrM_gbn59sdVw7uCuJInITBGn0UC3HydcAnf8conSUaUeo2ToaBwxGB97IOZP5MZMVggnZ37FSC92NgeqNvaXpr5EzB8pV7QrIMfun7JbfUS8IP9IvTmIh9VApBSeVqazuFRlWnt56j0Gq75EQVO1gYQRcyCKAMQvV6-2cOwvrZ2gCTytvI1cMB89t8JwXygQXfNM_yig2dwh60lIzq12C3Y1lQ1lTbAHW-U4MAj_9esb9SN2glTZX2IL4xJxznXwZimElIEob3oGi6b-YrwP2RDM0J9S8gnGwjfvbPg6eHlvBmFNNgyOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
#فوووووری
و
#رسمیییییی
؛
🇹🇷
روملو لوکاکو با عقد قراردادی به فنرباغچه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103437" target="_blank">📅 12:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103435">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZUkuYZEWONV46xhwXx90j_C4-fY4eW-34upcw9J383ZUDK-Hw2XJXN5bmWi5aoqIxpNn9V0EP9BmPmuQro7s5iHbfqo5imOAGULhYyAwkr6Fj8r6I1GhdNiBl8sIUeT60RrNZmQSSlUQ9gVHQqG5JaV1SVbp2GFZaNkJCiK2vDp0px7Q7RiCZP2XGH6N0OyN9HitkbTAzAQsTTJ7DZrTBe10Uex1KqYCCnDhF2Z1ZTpmxqKU7nfrSuAjzunsbMOPxPu13Bw1PSQMsEljjaZYnaatjtQbO7yyQJoQh9W0wlRHgaWubKOjhFNCkKhDsSn7CQgryctYxvGImgHGQ0huA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEOTBJAAAib5GwjdVZydyUrRf44vwCTahYd6gUz2yW9x6EZm9-S_7zqYJYdUUkutb18XUtJz5gaX0XdL6ZkaGJl7UOQyIOEtQMkUKu1e_9eddo7Teh7Mxx7zDMN9mz9RjHM_5k0GI4pptNUjf1HUQKGOwcMPO-F2gymVsJpO6WJMQ6TQbDbSO4DqdAw9HWbSxH9bIOnLoBAF2SdfioOuMzEXsvQR-pDUbkY-VizMGYmd-3AyQR9QMgSBQApeyldde9WYuhT9YwFaVp_UC5ztgPCWtH9Kp1XcbIanyDs6ih49upNyT8CDuUMUJ0yzDIF-WzRs5J-NfWP5XWmIAE1gNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
تمرینات امروز اتلتیکومادرید با حضور آلوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103435" target="_blank">📅 12:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103434">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba2ab6526.mp4?token=FwVHgexyrsMgghrVs3X43PHCd_pPuZOW66vd2Cv2dzUCLWQi_XVtpZ78ZRYAfvGjQi6NfkeK7JBH87lQ6qdCJon3j02KVGhlBhj3Q-A6YxNe7DvVXb42LoIVgcpMc3m0ANixdy594vM0U35m_03WNQs3PIPMuveVj53L_l2jlLNzVCeCV5_S-jiD2dei899_HiLQEudZasC7ciWLGiXlo4iFwLlVoDpoaMus56rSQbeSx8FLAsY8LI91lK06aOJA4ZQTaKwh6yQwX22yxLeT5cUpQkADui1UBI36MLZBAnbzbKifNysS-k4gCTnmMQUE2WX5NmiwFwPZUnhn5X09rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba2ab6526.mp4?token=FwVHgexyrsMgghrVs3X43PHCd_pPuZOW66vd2Cv2dzUCLWQi_XVtpZ78ZRYAfvGjQi6NfkeK7JBH87lQ6qdCJon3j02KVGhlBhj3Q-A6YxNe7DvVXb42LoIVgcpMc3m0ANixdy594vM0U35m_03WNQs3PIPMuveVj53L_l2jlLNzVCeCV5_S-jiD2dei899_HiLQEudZasC7ciWLGiXlo4iFwLlVoDpoaMus56rSQbeSx8FLAsY8LI91lK06aOJA4ZQTaKwh6yQwX22yxLeT5cUpQkADui1UBI36MLZBAnbzbKifNysS-k4gCTnmMQUE2WX5NmiwFwPZUnhn5X09rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم ازدواج رونالدو و جورجینا.
🎉
😍
💍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103434" target="_blank">📅 12:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103433">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aav3XhgwTNSeu7vwujwjo-w93KgtUcg5r75-0pFlTUh2kmBhrEHU_J9MlHCWkbQReNH2gkFtiPVyKETZMMz-EYbPvWxltMBfF2XSHcfyzDkRzxdSkwH0JefIfGKB3rCf-lWOAzuj9Uhz7saFMXmK6zSaA5w_EZyo_OCLYOE4-mP9S6LOeSXr1qOOPKkH5NEwEDqSpRNoFuXsVost39Q03tmMnIC2OD9pweoYboqGvndA1uF5AKf6Ro5Vrj0kRjDD3UxTSt93kw0iRix2iYUZtbPsDwSs0GPtqgv76kDy9Fq9lQK8_enibTf8d67QUVn74c49DJr4kYq2Wu4cQpazGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
❌
استوری تند روزبه‌سینکی دروازه‌بان شریف فوتبال ایران علیه رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103433" target="_blank">📅 11:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103432">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uilfk-YrW9mWl2ECOBon1nmDiAig7okE4P0uHt9xq78axI7sBbpSN_0a2-kr3sbTeyRaZuY7FO0F0kRgmJKvDLTJagrT0tW3NPb1VohJYTTAWIYb0LLeJEO8aYrem05ICk00ns01r_bCebcVC-pPa2yKSkqClWvpdP8ZjPWa8y10tdeoDZ45b5PiHo1QJkyrVpl9HVizzULgNUd7YZvsDUc1v3jBHQCGIq1T8pJjYIdzTBbb3SiMWP1YRPSVa5hdUJy2AR-vwKJK75Nm7vw1k8RVARExF0I4eX_ATmNi_XkvSvcCLEu39Rj58GUOpWqY8i6tZPedXNeOhskaDjlI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
قیمت‌بلیت بازی تیم‌های فوتبال استقلال و مس‌شهربابک ناقابل ۳۰۰ هزار تومان وجه‌رایج مملکته
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103432" target="_blank">📅 11:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103431">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpnxNHu9GOmWGeKay7UEBu9UBf0ZckQOzT8Mca5V9kl1jnSlhne8QVS93udrv7eJpJ0-rPVdN4DCGv3FXjt0PJE_WurTVIo680FoX2UmYvFQ4wPYkczeIhIQER_iSGXpa2HJ1CMF3lO5aUfZmcVDds_U31LxxygMIPKsQhi1o2urqd6C3WAAnFGjWr2y8sTfL2p285MDX4jrr1DTfRFh0yqFPpLgLWRjAL0yylbDl02BRZYFf1Dx4myw4yjOMfnGNcNN_dHWd-oZ4Y_DGzSp6d-1s1X_Cl0TEVxtmorj9vLEhepU48Kvx7KSDaC-cf45KoL46YUI-PFPleaYw-NBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
رونمایی‌رسمی از کیت‌اول قهرمان‌فوتبال آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103431" target="_blank">📅 11:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103430">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emL1tD9i5SDeaUv_6saGmTLoGWl3ZawLGtaIK1cE3br7HRxmmI0g86lFbF4UJK0525yVLm7jQi71yIC2UdrZW7-PyfrGAHN71W_v_f0KXEcrLCnQN4N1Oha5dFM8D5ohuSO1nFl1XUJ5hMy1D1yt-8pSCSR0QKlhYVJc2R5tRvPHlLEtFqB5J-fQ5feUjT5peTPmS_Xy5mNk4Gz8P9operWQCNIai6UPdLTtmRpCMQP9EXAPPT1GH0LK0WUaAY1gbEhkHICa7Vhqg6Z-PEsiAPK1JaAifU4meSa6AQ0Z758tyc48QoRCKKh-sSCnc-NsxiXRonCew4DDs0nGjjeK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
⚽️
#رسمیییییی
؛ باشگاه چلسی رسماً اعلام کرد که با پپ چاواریا از باشگاه رایو وایکانو به مبلغ 21 میلیون یورو (همراه با موارد اضافی) قرارداد امضا کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103430" target="_blank">📅 11:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103429">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWjH9KVwxvPHl95F2DxT1iM8u6Q9EqvZpUgEyj879aoWJKzfiwb47gu_Fv0XmRZ08druEM0xTcTw_SPugeBmr2lezyJ7WfVERzdH53uRw4isVKolBcuDxWHm5lfttTJ1aRVCwiyeBFzfpDcaPr9HkXSvrybbYusptpAidVCEFCP67YiflZ4kfKWNcJPWL709XW2E_JxfAlP1IxbxuKuMkg1wU48O4EH74ohFRIwQI8QX0ahgGS198b6dcsk9o3D9LbZ6teR37XNThnBiObbGrhJZUgWQI-ok9XcPXDlXxDzbKrfEOa07326mV_MBQ4plmBQRjEckQrytRmuWOf-2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📰
فابریزیو رومانو:
🇪🇸
پیشنها دوم بارسلونا برای رودری به مبلغ ۶۰ میلیون ارسال شد
🚫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سیتی ۸۰ میلیون یورو می‌خواد
💸
✅
انتظار میره روی مبلغی بین ۶۰ و ۸۰ میلیون توافق بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103429" target="_blank">📅 11:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103428">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4QJ7iQZtXf2M7fdvAxt5Fa6bSobr_IL5vCNkA6eidhjPjHUNnXECrzHeYMTJyI7mjlT5nAABNOoc9gwDDa4D_p14w3NVJtjqJNEHYmIu7zLKFUTU7maeMBHnilz4-ViYti9LiNNqDsVzzuut0SyQWQaD1H6ZnMc8ItZTa0D7YA1Vus8ZCCmzDvfP8ZXU2SRo0oeF1j21GZXH0CSBOrfvvxeqCWDlru83dwJ5tEZhDLPujOaa6oJSsB8ZjKWvmUoWQ6AxTM5i7spYz26-TmVEi2CtlGEZSKAKxdQW5otsXpyom0Cj_7HBtmXm4VvIzw9Txu2D2LxCMXMLK0vTifqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رونمایی‌رسمی از کیت‌سوم و صورتی رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103428" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103427">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103427" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✈️
اپلیکیشن MelBet
🥇
🎁
کد هدیه 100 دلاری:
Sport100
🔒
برای تعیین رمز ورود حداقل از 8 کاراکتر و حروف بزرگ و کوچک انگلیسی و اعداد انگلیسی استفاده کنید، مانند Hamid120
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103427" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103426">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ylz-pekCZih7kiaY5WUfip2oclBUtsZQEgs0jrZjxt9-lB1ShALHPgRNNwiV4b5Ey2pbfMgncsShVg4Yka19qeE1nz-G-zlw3coxB5z-gmQqeflhgG4LcYCXFIDkPIvSzpVKYoqgaHAgKkJLbNuZcrxIIRhzjAW0EOwrdSr9dA8FhA0maCtcP5p3hO6q0_wCpaM50AJbFsNYB4NvA4wb2cYMzQyc1jROwh1iW46rYN_ypQwbG-UwOGrV_tmtD3w3upKR7aDd2pipnoTTvomH7BxuvFyv2rTBrtD9FVZ3G19GezR4GwGylAug4FS_kStaq9QN-vHv8Q-yWwN8ux_9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌     ‌ ‌ ‌ ‌ ‌    ‌‌ ‌‌‌  ‌
💯
‌
فینال سوپر کاپ اروپا
💯
🆕
دیدار فوق حسااااااس
پاری‌سن ژرمن
و
استون ویلا
رو با آپشن های تخصصی در
MelBet
پیشبینی کنید!
💯
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103426" target="_blank">📅 11:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870f9db185.mp4?token=pASKbcx1dQE0VjT1_kzbSiTkxVoMsgmf7ZlrCmrHl8z8JP_HtHsJSkU28Kh0_YL-n2U7VyP94djIjw5B53VYE11Nh71A1T_jEdnE7yeyilpeldgpVhr51UCiUAlJUY2lXuVzG2sWI-wb-kTwJXh_WbeqZhRtFHeNMUDwAAqhV4GsWDyQyl-XPxMbg64VxIkrDY_e812gitJsrj6VJZDCp7I3xfzo_KiO_sMiYKLhk1zY8SXCQOTqLrMBD4iHKGEdG9uf0VDStr8I7ER-uwDKwYqi5WCnzxTfONxA1KAd3O_SRpirQ6HMxetl2bC8NHrcj00vn0S4SVI6N7A43wwFU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
😃
لو رفته از مراسم ازدواج رونالدو و جورجینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103425" target="_blank">📅 11:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6KuGbX2dg58CD8Ipk9p-54vV86QNv7cTg9mNNU4Fol9ctu9WQ9QiQF7lJi_my-aY9Pz_qIxXv4btlbYy7VFziGr-wiRarD-oXgAeK5kqH1BbGrH8-mLQoFV9SI1Vf5w6_wfTdQ_JIhnL-g7SbYOahIt0CbvYTh5RuqvQ6jIj1y2kL0F8SrfHIaGVIiTFFmAapdrS_1U_OKh6dicrEPKZy6_G7bRNquUi6bVkdem4YzbtrZFjR7ZWZcKc7bA3dxyJpes_MTO2L_E9Dsq3z-hsS_96HRWpXKcVLKtWHX-auP0KJn3kpLNPwWeudWqBu5WNVOxr82l7SRbENr6q01DmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
مقایسه افتخارات یامال و امباپه در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103424" target="_blank">📅 10:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c644437b15.mp4?token=rvCOMk0ApYNDxSrSDgeep4sWmHzILYlFKz0wDPvmML5TqFhEyVWqGVU2tacNwOupPoXc31fhp94y4EbFeYNIYHPZ0R9El-JEXA2gXVLKt8IhwStaSJ1760PbCgSUBf6xLrqCwjtPCdebl3W1Tjm_LsPu4kqutGS3cXyZ3Fk_drYGHrnQFqEtnTz7wrg03dJzIgApBtf0fRWmTkJtIC-vGbK7hN0jiNs9YnlwVJgDvk985jSgTVBZ-n1-TGSZiAHZVRyZTbMaJ4hTGkcRR4J4htEp-Hy8sBImt2c-YjfTrS1uE2GaLpg4T0GMd6XzOGRuKB7zXrvHuG7XEzuERZ2HmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🇪🇸
اولین‌حضور پدری در تمرینات بارسلونا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103423" target="_blank">📅 10:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103422">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gom1mcBYpapmKn8AeYYiRyEhrCgNZBETsiU26PY_yIrRzTAv-APx007-Gbq9v5GjG_FQOdbvBQUKzsX7I_HjRnx9ShWQEvuX_tfeoMM48UODFDLiZJU2janVUjGTPf5d0PauyPp3DOUJpNAuLs6uVoBdSbXKQpVs_bGngsUyurVrCahEb7Cy8RPWz7d5hUvXPUVJttR2CZb8nBnIsMgPJSERyZHCUW8C9E6C8cZHBd0rCXb1N4it6zZHCMuK7CqYs2WN9emTYH88e1Zq-YTlNPYdZOeaVVyXPNPW0_gm0iesDAmL4Ir14nlqMo_RcHzd7sZee-MkzAGaBs9tVvk2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
❌
جرارد رومرو: هانسی فلیک علاقه ای به اوسیمن ، ولاهوییچ یا لائوتارو نداره و فقط خولیان الوارز رو میخواد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103422" target="_blank">📅 10:13 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103421">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDmTF2Ylssby6oGHC1tvu0fu2tvnnZAKlUSOT34jM7z14ifUcMleCC2hw9E0_4iC0KPDIoTX-LBGkKWr3Vkgo0aDY8JliyfQAC62A8rWBlzdNOfAnXb3paCr0xszHtPlnvbuUZgChJ0mUwT18kQPH5WFtHvdwQdM5rWTU2ujTNqJQ8m--5Ij6E5g-YW1TcNqB36jCxWelvF31dSx0mRe5MMj4lvwIjNz8F3ppR7D52B7mnFg27OvJQ2VTrXvZ--U2IP1CSqIQGkVI7cgxWhOZIhvqsCAxeo-C1TaTzR5DzUeV2FyEYjXkHvV1Y3bXPz0gngGL2r_14EkxmWA_3RL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✅
تمامی قهرمانان سوپرجام اروپا به بهانه بازی امشب تیم‌های پاری‌سن‌ژرمن و استون‌ویلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103421" target="_blank">📅 09:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103420">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY0GsCXFv4j--HUJJ962-TNtLO7ETJR2cbqfa3VNyUz5lVV0S2YJEadEpVtJP5SgyoEDq5_NZYHFjykIznHqWlGCKwCqs6kTHFkaGE0FpMn_mwaXEIxinufAsXHPLWZcG9KyrOmiLbEGxzi_nrLlFJj-q3AHKvb6Mus20GRf0eUBFjHxQpGaT9TEyNaLF-S42Rqjhbb0dL2KBwKZUjaLpL77t10OQGan6Axu9ozIKYNAHUKeN8aaCEFHlUcHUJXg95ephvcCQjUHx0EqqpLRa4yBZRhB2cv9z8zQNJytlRo4lbsZCIt8AMWtH9Hx4BPZbRskaAt-GWLkbpAnJTTNNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اولین باری که رونالدو و جورجینا این دو مرغ عشق باهم دیده شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103420" target="_blank">📅 09:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103419">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=H1WSLL0zFPpeZOmFPIS48SQZjo_8C6ADPQvsq7W8RENy5mgyr1H3kz_pcvSZGdkgHi1C-jzUqqeNLIZ5UBMDg04-E9n453DytZBhHE7mFu8Au-FAaA3kpC5IHfkRZlYz-516VbpA2wjxXwLST157x1L7H2vP2lr97LKZ57Cm1X7e9h3zMpE11veH8Pkm3xir_7lYG7W3nPLvz0Et6I1etEOFpWEXgKQ0Xq0tYMsVKEtDuFQRcqQOnzz2Xz4aqWZmDHxByvZRgr77nK6nZmAxMwH98Hh3xctL7eMbU4GtENLHIB-qKOftA1knheU8dVmnyOFdug8udvyxo5XHf2PGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea09ff2dc9.mp4?token=H1WSLL0zFPpeZOmFPIS48SQZjo_8C6ADPQvsq7W8RENy5mgyr1H3kz_pcvSZGdkgHi1C-jzUqqeNLIZ5UBMDg04-E9n453DytZBhHE7mFu8Au-FAaA3kpC5IHfkRZlYz-516VbpA2wjxXwLST157x1L7H2vP2lr97LKZ57Cm1X7e9h3zMpE11veH8Pkm3xir_7lYG7W3nPLvz0Et6I1etEOFpWEXgKQ0Xq0tYMsVKEtDuFQRcqQOnzz2Xz4aqWZmDHxByvZRgr77nK6nZmAxMwH98Hh3xctL7eMbU4GtENLHIB-qKOftA1knheU8dVmnyOFdug8udvyxo5XHf2PGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاوووو عاوووو رامین‌رضاییان چه کوفتیه دیگه قرمساق
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/103419" target="_blank">📅 09:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103418">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZna2gX0v_AH-fScEaM505wyrLalrWFvnGonBBviMhknq4awn9Bhqspsv9TSntu-QhHbvoDEUqV1VP3j54m1SWlWYKPHAKfgPViGy1gAI4j0V6x-JJUtqPVcMuaCFxKGMRGRCGKHQDwmGFvgFOQHAtwtNCLPBCsoytT_MwPL8XZfNmZk6jbwiTs-2KsK-eI2_eaaRd-m0A98cyMasmsozysCRPt70rSJUaxolp-uETOTL0gLCFJZbzO54uSF7glA9PCV3MZ-BQsoo_hEHKBjN_g_tTAWfgw5EWXHgEUhNSdJ_DDmIh8S6PVdL2zLGcVT5BAR1mlZtFnwns4fOjgMZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: دوشان ولاهوویچ به بشیکتاش
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103418" target="_blank">📅 09:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=akoQ48m3AjDixnrhyxPAkHFzfjG-H_p8k14wCtqCf36Es1CiOKnFDE4zyjHT8nfJk5b6xvByLwY6tXKvPE_-7rQHdd1Rocnq9K412lrDNpIElwBSvqwRypG4xPAgsTIx-vsS7d10QozTV_fM05heCzUdETXnGlC0_2-9fS-FWPWYdP460t4UPHxwHTPgB2wYOR_vGb58bzVyzhoItJxgMzChTaUrcANNvqnJ0iKYb8_WWpr89i3JNl1KDGsP5FKqmlDVEEYlvYUQ9B57ABg5G3xWA5mphzts6wPsG67-lrADUc92KsFx3dBKluyk9gxXBhyyug5foCT6VH5ZUleDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcd964c7b.mp4?token=akoQ48m3AjDixnrhyxPAkHFzfjG-H_p8k14wCtqCf36Es1CiOKnFDE4zyjHT8nfJk5b6xvByLwY6tXKvPE_-7rQHdd1Rocnq9K412lrDNpIElwBSvqwRypG4xPAgsTIx-vsS7d10QozTV_fM05heCzUdETXnGlC0_2-9fS-FWPWYdP460t4UPHxwHTPgB2wYOR_vGb58bzVyzhoItJxgMzChTaUrcANNvqnJ0iKYb8_WWpr89i3JNl1KDGsP5FKqmlDVEEYlvYUQ9B57ABg5G3xWA5mphzts6wPsG67-lrADUc92KsFx3dBKluyk9gxXBhyyug5foCT6VH5ZUleDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق و احترام لیونل‌مسی و پدر فقیدش
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103417" target="_blank">📅 08:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22164b16b5.mp4?token=ANVK5zThBsj_LcJDUA35emlTB4Kpu60mb7r_k9pz-NwadKCaeRuWbrk7uF3lu_QbiGn-PxWqmbD4ZqeSkwRz2QuKUBPc-G598c017GATgqbyy0dmzyqe1Hxu2t3gxkSsGxDMBXIjgiVHStJsufMUiG304rhJwvynLwAhKQ8hHdYXdVISbXFt493q9JqR2Why8P3fvN-WFnBj01NRPGsZLNI1aK4I1ksPnUnD4mPYaVgnuZ8N1YX6P5x5MVFBY_6Bf0pepgf1_SxogIbfvN4s9xbuFl9ptGVd5f37wAzhcHH_VIfmEAcXgIYVVteUcIKAwL04Z95Ey_RC3rmQtSjxDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
یه‌ویدیو کاملا کاربردی برای دوستانی که باشگاه میرن و میخوان بدونن هر حرکت برای تقویت کدوم ناحیه از بدنشون هست. حتما ببینید و برای دوستانتون بفرستید
❤️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/103416" target="_blank">📅 01:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103415">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qT1blmqPo7kJ7jMq2yV_9e5d4Qn6cTRln8r9_oeF0SCl30ycZGX2z4ZYTDzoQSdiH6l5joHXy8Cbvi1qYWUGh_2yoYDnODRhHnxK6ygsj6RmkyAH1H-eTXZ_8Ku8YsU1zuJxO4lwS-GXvadiQ-MM17zs3BOlKKkLNalHswBba6w_lbRYvIMlOeeVa2Qb1K1NPQm6vMbniuzN8C9skMNec94EjpUEvQ-LGDJXq2NtJMe0Vm0l8ZLVlhVnQBxIF9MZVViE3gb-riCozZs1sjnQrqsQEtSGYNpq-vlKkGnLvSZOHbWPgp3Fja8qS1S22XOV-s6HsvL4ikMF3OESZALWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
رومانو: HERE WE GO فران تورس بزودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103415" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103414">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/038cd39016.mp4?token=V0OdXG6SMXmsOjB5XYQXaPycqwBdXT1nfgcLVhcMa88o_YDQp-Iz4aeH7moOECqwaa2jh0GDiauU8qOxUUhAM7w0HgOHPzuazFoQfRQ9FZt6i5wLuwXkxwTWTy-_ZWIHgkjtUdUUtGshzQHbdSsbWRZTu5UTJY9Zoyt59FaHlBZpHz5H9aBwg-uL3O-HW8RwN8-IstWGT1CCS8A00NzcxAAi9fRtLvJ_puGyp3hE9K6CWGm_PQ17zovKuTkIa0I4F7Zeln8-jZ8XFSxuuKSSr5jHbMqSWjIc4DTV2-qOfzbeGtjJcpoRREzLguaLIjaM8hkmW7sGSrO3inQlQk7vaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/038cd39016.mp4?token=V0OdXG6SMXmsOjB5XYQXaPycqwBdXT1nfgcLVhcMa88o_YDQp-Iz4aeH7moOECqwaa2jh0GDiauU8qOxUUhAM7w0HgOHPzuazFoQfRQ9FZt6i5wLuwXkxwTWTy-_ZWIHgkjtUdUUtGshzQHbdSsbWRZTu5UTJY9Zoyt59FaHlBZpHz5H9aBwg-uL3O-HW8RwN8-IstWGT1CCS8A00NzcxAAi9fRtLvJ_puGyp3hE9K6CWGm_PQ17zovKuTkIa0I4F7Zeln8-jZ8XFSxuuKSSr5jHbMqSWjIc4DTV2-qOfzbeGtjJcpoRREzLguaLIjaM8hkmW7sGSrO3inQlQk7vaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
😢
مسی وقتی می‌بینه رونالدو و جورجینا حداقل تا چهلم پدرش صبر نکردن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/103414" target="_blank">📅 01:11 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
