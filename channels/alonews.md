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
<img src="https://cdn4.telesco.pe/file/QtJj4gA4RFpnucMxrw2sYGix7DgdUfZPkgyatjoxIMexLBCafxxHFCP6ewiYKyLIjbf0iEbJR-4lU6WmBWP9iM1ZgShfMdc0sT6coH_zZfcQt20ASAKdppOyCzLlO1gxzSn5dnzitNBIHim7BakKHEDX-m3XmrITCLNR9keYAfyIzB6SuQuTGXu924sOgf4YBjXQXMGu9FFmdlPE_8q78x8EBeAHP7LaWxAtrepZ4UZ_byy197x_gZi4tNtPo4q9PQti-0y5RFoozpOfEfluA3-ame-6FPO0CtlbnFV14edw4Kolbt1LNpRvx5ugI_mbiH-ZbwmkJsPWkcUcq87PNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 981K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 08:27:04</div>
<hr>

<div class="tg-post" id="msg-127531">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اکسیوس:
برخی در واشنگتن معتقدند حتی اگر توافق اجرایی شود،
نتانیاهو ممکن است بازهم بتواند نقش یک اخلالگر را ایفا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/127531" target="_blank">📅 03:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127527">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtaRIsLy0-bjvoH-6dHpT4Dujth_zgluhgtAzNi3GjIHeuk1abXkRgjyB0kaqx309hCkYU4Qz1l8GvgakoMkEpFE7hYFNONSEdS1uoQ5h8vR0rrTlw0HZYGy-JhM-oyBCgmwT04RMg5J2twZZYZiWSJuq7SJQMFzlKnRy9TzB74hhhNBpjyLM6hx1JxjrC-XoICQIf_X9gTySgLbCMyOEuTbAGGA5RNlJIswudBTJoNpt5mwPEMoKE0tzaEx7sObV2ugd6Z2cRgSpIJWJSti_EiGYgbdDfK8ndLiQpF9W5618_dokuGTOywCdNysOs64MCTA5JEJUnkwEYJ2AwRmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار در تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/127527" target="_blank">📅 03:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127526">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
فیلد مارشال محسن‌رضایی: آمریکا با آزادسازی ۲۴ میلیارد دلار از دارایی‌هامون موافقت کرده؛ اما ترامپ نمیخواد اونو علنی کنه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/127526" target="_blank">📅 02:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127525">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=hErGu0ZNpp4L4fdhuFNl7nw7UpmDFc02dr1d1CkPQWMrRD12g09sMYf3YVRDL7GYn1FHHgG3vHaTQpFSQLYJVWhieNmHSxOtWNKNowwJX3OgWvFcinSkkfFzGabMA66G-bi4ubG5YCCvRJGLl5dKu04jOa1GUTzwss4fFSOgSJLRqi_Tp0-42kvMKxwzqwywDxnEn9MqL57JZWLFaVcRf8halNZL_ozaAhkuTLjTF11jyDdZXJq-oprRbhLNcL930lr_1EifzXaDxEbCZRvz4i9KNq18o__lx4Z574NtlMVtwsVjoTm1i5E7C9akx6RE1eP8aGZcDPHx-JfvYC_nsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=hErGu0ZNpp4L4fdhuFNl7nw7UpmDFc02dr1d1CkPQWMrRD12g09sMYf3YVRDL7GYn1FHHgG3vHaTQpFSQLYJVWhieNmHSxOtWNKNowwJX3OgWvFcinSkkfFzGabMA66G-bi4ubG5YCCvRJGLl5dKu04jOa1GUTzwss4fFSOgSJLRqi_Tp0-42kvMKxwzqwywDxnEn9MqL57JZWLFaVcRf8halNZL_ozaAhkuTLjTF11jyDdZXJq-oprRbhLNcL930lr_1EifzXaDxEbCZRvz4i9KNq18o__lx4Z574NtlMVtwsVjoTm1i5E7C9akx6RE1eP8aGZcDPHx-JfvYC_nsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم قلعه‌نویی
@AloSport</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/127525" target="_blank">📅 01:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127524">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آکسیوس: به نظر میرسد نتانیاهو در جریان تماس تلفنی با ترامپ متوجه شده که نمیتواند مانع از انعقاد توافق با ایران شود‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/127524" target="_blank">📅 01:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127523">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=OJ3ZoeU2UpfOk2NlKNxINVJXE3jBuF-2a6jCxfmY5bdR3CUMaicqn0CQOiwKeZRzGDPLqA2aHrKE2Xu8UtMGb3tv3D8dBIht6l2wVBnEwEy_SiMj058DyaqRC-B5urq5kfmcT4VhVZE2GEN_MeSu1pfyjuwke7gvuWxrdX12JDYhkV8a_V98MBbm1HS9cN1ji_b75zIxvBWjB14-kXYqhZstJNaDMA8arKxuxhvYI6QT2wxtj2KbKP5WdLzojAuNPxcxJCuy0cXLJFgsjVEJrcyXaFXWiW9OPsyBcLrT2KnKB-J4PqHycDeWlOHjM_0UKT8QbyT3bJ7GsZhZoT9mgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=OJ3ZoeU2UpfOk2NlKNxINVJXE3jBuF-2a6jCxfmY5bdR3CUMaicqn0CQOiwKeZRzGDPLqA2aHrKE2Xu8UtMGb3tv3D8dBIht6l2wVBnEwEy_SiMj058DyaqRC-B5urq5kfmcT4VhVZE2GEN_MeSu1pfyjuwke7gvuWxrdX12JDYhkV8a_V98MBbm1HS9cN1ji_b75zIxvBWjB14-kXYqhZstJNaDMA8arKxuxhvYI6QT2wxtj2KbKP5WdLzojAuNPxcxJCuy0cXLJFgsjVEJrcyXaFXWiW9OPsyBcLrT2KnKB-J4PqHycDeWlOHjM_0UKT8QbyT3bJ7GsZhZoT9mgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیوه جدید لب گرفتن و بوسیدن همدیگه توی فیلمای ایرانی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127523" target="_blank">📅 01:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127522">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
امارات گزارش‌های مبنی بر انتقال میلیاردها دلار به ایران از جمله پرداخت ۳ میلیارد دلاری ادعایی را رد کرده و اعلام کرده است که هیچ دارایی مسدود شده ایران آزاد، انتقال یا پردازش نشده است و این اتهامات را نادرست و غیرقابل اثبات می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/127522" target="_blank">📅 01:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127521">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
استانداری هرمزگان: صدای انفجاری که دقایقی پیش تو بندر سیریک شنیده شد، بخاطر شلیک هشدار به کشتی‌های متخلف تو تنگه هرمز بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/127521" target="_blank">📅 01:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127520">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ukI6SC4Ml5Lkbg-S4cc1yavTywLP4wM5WDenPePhovLIFPyD7NuicRi55le10WVlE8K7tHfxxyWS0Ol_zTWEjIPTazhlkRAoV3Q2l6OeXg7Ygss0t_En0L3O5xLdQrsuxlfesI-A579xIRUl352FOZG4p0I2UqF_eWpXve8eYafIDg99vse-q8TQbNt4IX0Z6nYO-ww4H3QdKpd1kLxNS5VDzf_q05iWs0mmcIwyAZ9_wPOYqzOW8jS0mW1Zsm01bq-dvgW6bWoVrIRNZVhNwyMBXmfmk6q3nHIeAeSGhnUH1dXlcLqxOrSP9YntMv0zQcxtJrzX_u_FaEM9QjpvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله شدید تندروها به قالیباف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/127520" target="_blank">📅 00:49 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127519">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اعتراف عروس و معشوقه به قتل شوهر؛ راز گم شدن کیارش پس از دو سال فاش شد
🔴
دو سال پس از گزارش پدر کیارش مبنی بر ناپدید شدن پسرش، فیلمی از قرار مخفیانه عروس خانواده (ملینا) با مردی غریبه، راز این پرونده را فاش کرد.
🔴
پلیس هر دو را بازداشت و آنها بلافاصله به قتل کیارش با همدستی یکدیگر اعتراف کردند.
🔴
ملینا گفت که با همدستی بهروز (مرد مورد نظر)، شوهرش را به قتل رسانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/127519" target="_blank">📅 00:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127517">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d5B2OFw3qLtF003xfRZwv9ebg4FrX2GheJN2jX1TWaP8qVHOzeJ-OppDtzF8wSKTWbDV4QqmuI5n-kOpWXsxGcb3XbCypxWiZdg2I1aTHoVqcYlvroqiVNIEixJZ5AmRupv-mZibCYifzBPBvvOo6sf0LyGFdlv193kaSLi4woIxk9mv2zOMxzZqp7DnJCkyjz1vJqBbr2iTxxy4bMyqyv6FV3TSoToe8Uty9oOgmbksc32mB9eVBUdTOinUa3K_Ur4ll_QZbDx4MIa1S_5Twrwit1tnXZyuo5KqOV4u-o4CCpimofjKNItYEqXCzqRpvTUZlR29gtpvnKl14ictHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nug7m73iXYVD8esuA1FJrDxN0GIjlEndAP0KpkPgjNjkpu1Fh8SyC0t7fwtJZLVsGEetGoBaws8S4h9Yk7ASLCcca2bSDsvxbQRWmylVXWKffBZf_E2135Fp0kXPHXUO6kdlAfJRzt3nSI40K25_duxEGdNnthfW3LK2SyAY4jVq0mmea79haCnGODWgnW29kHdlv_EWKXBM1-eFxgTiNNuoOKjhSSUa61yc_JQJEDm8jozK7IFJpJ63Tx2PIh1Gp1nuZIMgpgDwukU6uSiKvESbotHDWd-cCpj1FJTelsTPkYhOjrxiblcdpjsdm9g2gsnCuS_nfmwu5mkoWq-xuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری جدید از ابوطالب حسینی که خود را شبیه یکی از وحید جلیلی، قائم مقام صدا و سیما در آورده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/127517" target="_blank">📅 00:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127516">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJziwxIayMcyVR8Zsbt76kuzAgaa0-c5wySMs9_prCfMsEtyqQYmGsJU1RqmfsqAlqOYjiyP4i98d5y-S1TxswMBTH82ijdBPmIsy9k4tH1JjNklQQEym1-HlcjOFpCtY90Lagsxj_QglK_OHAehOvH7NMLjns6yv7Wui8cP8CMC4D6JZLhJF_sm8Y3UUMpVqjBMKgxKSzHA9sWl_b50aJmB2dsdrkAyF2qGMRyBaYiYhhwAwp7nM7yC7PifUdWStWtFnCYV4mvmo8dGwcnAiDBwRkwGm5XWnnayUlLQd9kWWs9gHohO1NS3Qa7_69POVK2LKAmv_HCxHbXMEgTFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش فعالیت نیروی هوایی آمریکا (USAF) بر فراز خلیج فارس و عربستان سعودی
۵ فروند هواپیمای سوخت‌رسان نیروی هوایی آمریکا اکنون بر فراز خلیج فارس و عربستان سعودی در حال پرواز هستند
۱ فروند هواپیمای هشدار زودهنگام و کنترل E-3B Sentry (آواکس) نیروی هوایی آمریکا در حال پرواز بر فراز شرق عربستان سعودی است
۱ فروند هواپیمای شناسایی و شنود سیگنالی RC-135W Rivet Joint نیروی هوایی آمریکا در حال فعالیت بر فراز خلیج فارس است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/127516" target="_blank">📅 00:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127515">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127515" target="_blank">📅 00:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127514">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrluUNtRcJyAuFEFwU9CUsrGvkEogTL_xozeSCXC6n10SA9zqGmeh-1lC41_TTBZV1Es2kypN2iOtkO_Uc4EAPlZoiw2xHALq-UgDSsNpimCgu6rGv0g_i6yIBon386aR9WzJ_5pVLTu-2Q2862P8xhVYPpujY7FJ4VKCA_w2jRNgifQOruV05WigOovyOjffx_PBle3laNHudXB97i7cOfoNbL5ors5G3wIRHjkFPQugdpGmHXXFNQSV51UHiXqW2zMYJohAwY-ONcCw137haDBNiEA7nNwY87UBgI8d4HvCiU2tA6zrFUpYKO1OwB95jWreAXI0oJTA12q5PUUeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای جنگ الکترونیک RC-135W و یک سوخت رسان آمریکایی در نزدیکی ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/127514" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127513">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d4473eba.mp4?token=shKt4ShZwln8Gi47468wJlBpJji6T7vZotuomD0zMT_RrRwRMjLua1GdoK2jWp026mNdLuv8PawSeezjagRfKFnZ8JW72dksLdN-a8oNHaXUj47M8J4xkFEby2m2Jg6uETIPe9YX-aCup1ozgS7zEGTkhUZSKM7dktjRpm7avMfmEVHeX98rPpa_78a5cYg5lr0ewjA6PHhEZ-6m3RzZt3r2cG9OvpQbdEYlJmkThK2--rvvAA8q-lPDkVGqapGvfOjfrh3CvoMM3V4siukjPHzax8NS05LyYcSc3g5UFqGyYsKH9wx6Rrm3eC91xZPPGF_fUC76nLpAwYTe408DEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d4473eba.mp4?token=shKt4ShZwln8Gi47468wJlBpJji6T7vZotuomD0zMT_RrRwRMjLua1GdoK2jWp026mNdLuv8PawSeezjagRfKFnZ8JW72dksLdN-a8oNHaXUj47M8J4xkFEby2m2Jg6uETIPe9YX-aCup1ozgS7zEGTkhUZSKM7dktjRpm7avMfmEVHeX98rPpa_78a5cYg5lr0ewjA6PHhEZ-6m3RzZt3r2cG9OvpQbdEYlJmkThK2--rvvAA8q-lPDkVGqapGvfOjfrh3CvoMM3V4siukjPHzax8NS05LyYcSc3g5UFqGyYsKH9wx6Rrm3eC91xZPPGF_fUC76nLpAwYTe408DEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: جمهوری اسلامی رهبرشو کشتن، ۵۲ مقامشو ترور کردن، بعد کشوندنش سر میز و گفتن حالت بتمرگ و امضا کن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127513" target="_blank">📅 00:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127512">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
صدای انفجار در قشم و سیریک
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/127512" target="_blank">📅 00:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127511">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
صدای انفجار در قشم و سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/127511" target="_blank">📅 00:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127510">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فاینشنال تایمز: اورانیوم غنی شده ایران، نابود خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/127510" target="_blank">📅 00:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127509">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عراقچی: یادداشت تفاهم کمتر از ۲ صفحه است و کلمه‌به‌کلمه آن بارها بالاپایین شده و وزارت خارجه با نهایت دقت تمام موارد خواسته شده را لحاظ کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/127509" target="_blank">📅 00:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127508">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6363935340.mp4?token=UXJHDj0Nw6odq6wzd_jMDgXkaqGJPMrKFIHEojvWRy1IJd2ZZV82vgR-KFrTCo7g6isLbvrmxKJtBNgcjyP5b2mG6LVLRQ_2slVAkS6fb4P1mNAMpq0dkNML9IiVSmku6TopE3ibKfU-fexkkqRDs9QTRMGCccyyFsQwFKnXFaoEr7Bj5a7bzd9724UKt50iN7eZs0g-UKYuMSfvJ16OFgj6JZ4eE_jRyaarMreo-YMJvjdDAJFrOgu6O1fjm_PAHoLrFtltMq-TfPQDMsJOQFGgMFTgoZnUAtBqQdU7t-ATzvapceQuW_A2esAyQsl-m3qLi0Bnup8ozX3Vwosb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6363935340.mp4?token=UXJHDj0Nw6odq6wzd_jMDgXkaqGJPMrKFIHEojvWRy1IJd2ZZV82vgR-KFrTCo7g6isLbvrmxKJtBNgcjyP5b2mG6LVLRQ_2slVAkS6fb4P1mNAMpq0dkNML9IiVSmku6TopE3ibKfU-fexkkqRDs9QTRMGCccyyFsQwFKnXFaoEr7Bj5a7bzd9724UKt50iN7eZs0g-UKYuMSfvJ16OFgj6JZ4eE_jRyaarMreo-YMJvjdDAJFrOgu6O1fjm_PAHoLrFtltMq-TfPQDMsJOQFGgMFTgoZnUAtBqQdU7t-ATzvapceQuW_A2esAyQsl-m3qLi0Bnup8ozX3Vwosb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن این ویدیو باعث شده ترامپ توافق رو قبول کنه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/127508" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127507">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گفت و گوی امیر قطر با ترامپ درباره پیشرفت مذاکرات بین آمریکا و ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/127507" target="_blank">📅 00:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127506">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvArhLeJAYBZ3l5j2QD9KicjFWv_DI8czY82xa91dmWxGtCu1vXTwkYHe73eAD6nULcZcfE3pv1s2qdDYN2vb85TNWATYObG8O0gWA1VoHr_v8BgJQeS-l9HM5O5e268jF-GAY6XSPeHqqy73vJ7gNqmIxhQh103K0o_wvD3nG5oDT2i7hi-LiVCLD4lQ9jpVOGNJgxBrvcchBnd7KZ-wXjrWVzym76ieRzVs8uo33BpToQgXsckMDJXHG1IxHbrsvPRr3bvbqBy6lX0srypCrwTCviNZjtogf9nKzTxU7YFG-213mfA-fMYGptXKVJftD3nTENyddPyiPyF_3WiBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: توافقی که با پخت و پز بانیان توافق ننگین برجام باشد حتما خسارت محض است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/127506" target="_blank">📅 23:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127505">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رئیس‌جمهور کوبا: قوانین اقتصادی را عوض می‌کنیم تا سرمایه جذب کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127505" target="_blank">📅 23:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127504">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d6d94579.mp4?token=oHJ0soQj2TFLQbhwIXjUifFQ00CGZRR0CdLNnwKpVnqdbdvbje9QqkbqtHjnF5QpdPoXynWLEs91qN1nNWMkrIaRVqiNGNxH5fL-KyTu_8ICtjNTFzY5vploSoF_iIWxwKug7V_a6cnOIz_3yPhTN51YA-U3FVM0Szmss08vjzbVYLXT-gsi_wytY62gL2F6XlVb6kWYqmJUEjG5Mojyf9C6K_1bTKGPpaTeqVIIJ60w6-agtm_k6pycKLlZq5Q-GqAw2H9aJc6_UF59V5d8BN7QwjdCsDmRzoeci5ylrpemr-j6tzjPu2-FV46sFcZ2Ro4hoPpoICS2pcfAOFjUEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d6d94579.mp4?token=oHJ0soQj2TFLQbhwIXjUifFQ00CGZRR0CdLNnwKpVnqdbdvbje9QqkbqtHjnF5QpdPoXynWLEs91qN1nNWMkrIaRVqiNGNxH5fL-KyTu_8ICtjNTFzY5vploSoF_iIWxwKug7V_a6cnOIz_3yPhTN51YA-U3FVM0Szmss08vjzbVYLXT-gsi_wytY62gL2F6XlVb6kWYqmJUEjG5Mojyf9C6K_1bTKGPpaTeqVIIJ60w6-agtm_k6pycKLlZq5Q-GqAw2H9aJc6_UF59V5d8BN7QwjdCsDmRzoeci5ylrpemr-j6tzjPu2-FV46sFcZ2Ro4hoPpoICS2pcfAOFjUEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داگ بورگوم، وزیر کشور ایالات متحده:
کالیفرنیا به نفتی که از تنگه هرمز می‌آمد وابسته بود.
🔴
آنها قیمت بالای بنزین خواهند داشت. می‌توانید از گاوین نیوزوم و مجلس قانون‌گذاری ایالتشان برای سیاست‌هایی که وضع کرده‌اند تشکر کنید. این موضوع هیچ ربطی به تنگه هرمز ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/127504" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127503">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
تتر بعد از اظهارات عراقچی درباره احتمال امضای یادداشت تفاهم، به ۱۷۳ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/127503" target="_blank">📅 23:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127502">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
عراقچی : شمشیر ما همیشه بر فراز تنگه هرمز خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/127502" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127501">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / عراقچی اعلام کرد: احتمال امضای تفاهم در چند روز آینده وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/127501" target="_blank">📅 23:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
عراقچی: فکر می‌کنم نتیجهٔ تفاهم برای منافع ملی ایران خوب باشد و دستاوردهای میدانی را تثبیت کند.
‌
🔴
علت جنگ این بود که ما در مذاکرات از منافع‌ ملی‌مان کوتاه نیامدیم و مقاومت کردیم
🔴
دشمن آنچه که در جنگ به‌دست نیاورده را در مذاکره به‌دست نخواهد آورد.
‌
🔴
یکی از مقامات آمریکایی به‌تازگی گفته که ما تازه فهمیدیم که ایرانی‌ها با بقیه فرق دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/127500" target="_blank">📅 23:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عراقچی: تفاهم در صورت نهایی‌شدن به‌صورت دیجیتالی و از راه دور امضا خواهد شد و سپس اعلام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/127499" target="_blank">📅 23:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127498">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عراقچی: اگر آخرین مرحله مذاکرات انجام شود تفاهم از راه دور به امضای دو طرف می‌رسد و اعلام خواهد شد
🔴
ممکن است در چند روز آینده اتفاق بیفتد.
🔴
رسانه‌ها فضا را مشوش نکنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/127498" target="_blank">📅 23:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عراقچی: یادداشت تفاهم کمتر از ۲ صفحه است و کلمه‌به‌کلمه آن بارها بالاپایین شده و وزارت خارجه با نهایت دقت تمام موارد خواسته شده را لحاظ کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/127497" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
عراقچی: شورای عالی امنیت ملی اشراف کامل بر مذاکرات دارد، بارها موضوع در جلسات مورد بررسی قرار گرفته است
🔴
کمیته‌ای شامل تعدادی از اعضای شورای عالی امنیت ملی بر مذاکرات نظارت می‌کنند و هر جا لازم باشد به شورای عالی امنیت ملی گزارش می‌دهند
🔴
موافقین و مخالفینی در میان اعضای شورای عالی امنیت ملی نسبت به متن هست اما نهایتاً به صورت جمعی تصمیم‌گیری خواهد شد و پس از تصمیم‌گیری ابلاغ می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/127496" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عراقچی: ممکن است 60 روز مذاکره تمدید شود و ماه ها ادامه داشته باشد. ممکن است تمدید نشود و دیگر مذاکرات را ادامه ندهیم. باید ببینیم بعد از 60 روز با  چه فضایی مواجه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/127495" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnAsQjyWnYv-KHR4UENkccXEGB23OwRovJYXMP8bXbCIWg8xNy1F0WCx7egiFlTs6m4XyQIauEPymAriROJJoHRTXCv47dazE7fslhSENzDxs8RMiSJcruOmRrUHNGuWxVce4MZF2yIvXbrBDHNmKdnpjZz4JlcP61krjtOmANmqnPo90yXM9ZzpxHtWt2njWHfoZsh7hV0zk_emJtfYOg7H3AKwzIr4vA0AlD5lqQ1ccvQwlO-SOJShmzdiTe9AaW308HBrNdSCIAhCa7dzob90EeJ0eNtEV1He5FVcX40yYYrAuAHsYW5l9eE0PV-ROESVzDD66HZ8Z3SHTQLauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/127494" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
‌عراقچی:  از نظر ما تنها شیوهٔ بررسی مواد غنی‌شده، رقیق‌سازی آن در داخل ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/127493" target="_blank">📅 23:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127492">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
عراقچی: محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود
🔴
دارایی‌های مسدود شده طبق یادداشت تفاهم اگر امضا شود، آزاد خواهد شد
🔴
هیچ‌یک از دارایی‌های ما نمی‌تواند مجددا مسدود بماند
🔴
برای جبران خسارت ایران طرح بازسازی در نظر گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/127492" target="_blank">📅 23:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127491">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
عراقچی: به‌زودی ایران و عمان بیانیه مشترکی در مورد اداره تنگه هرمز منتشر خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127491" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127490">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عراقچی: طبق قوانین بین‌الملل گرفتن عوارض از تنگهٔ هرمز امکان‌پذیر نیست اما هزینهٔ خدمات دریافت خواهد شد و این در مذاکرات تثبیت خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127490" target="_blank">📅 23:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127489">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
عراقچی: در مورد آزادسازی پول های بلوکه شده ایران بعد از امضای یادداشت تفاهم صحبت خواهم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/127489" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127488">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
عراقچی: هزینه خدمات برای تنگه هرمز گرفته می‌شود و دیگر این خدمات رایگان نخواهد بود
🔴
این امر مهم تثبیت شده است که هزینه باید پرداخت شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/127488" target="_blank">📅 23:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127487">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
عراقچی: اگر طرف مقابل ظرف ۶۰ روز به تعهدات خود ذیل یادداشت تفاهم عمل نکند، مذاکرات در مورد مسائل باقی مانده ادامه نخواهد یافت.
🔴
احتمالا بزودی برنامه مشترکی با عمان درباره مدیریت تنگه هرمز اعلام خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/127487" target="_blank">📅 23:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127486">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
عراقچی: اسرائیل باید از لبنان عقب‌نشینی کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/127486" target="_blank">📅 23:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127485">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سید عباس عراقچی: اسرائیل دشمن این توافقه و درتلاشه خرابش کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/127485" target="_blank">📅 23:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127484">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عراقچی: مقامات غربی میگویند باورمان نمیشد ایران سرسختانه مقاومت کند
🔴
این مقاومت در وهله اول مرهون جانفشانی نیروهای مسلح است و همه ما مدیون نیروهای مسلح و شهدا هستیم.
🔴
عامل دوم مقاومت ایران، حضور مردم مبعوث در میدان بود.
🔴
رسانه‌های ایران و صداوسیما نقش مهمی ایفا کردند.
🔴
از همه اینها کوچکتر، دیپلماسی بود که سعی کردیم صدای ایرانیان باشیم و دفاع کنیم از مردم ایران و یار نیروهای مسلح باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/127484" target="_blank">📅 23:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127483">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عراقچی: نتیجهٔ تفاهم یک یادداشت ۱۴ ماده‌ای است و وقتی نهایی شد تک‌تک آن را به مردم می‌گوییم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/127483" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127482">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgkp9rbA6QzfTQVZzIqRHItUnGTn-6wvHxof-EkW86RrkUJzOBPsSBffz3IlIa-YDk9RfG73swE0t-mVkTe7swWL_7UFcnpGL1fcjkZWVwmPHIPsEKFc_cn9iwVB6NWri2VmCI-9Mc-bbwMzIgfWsmpUHFJRHGbLWLCITWCVxRv9gmw-2DUTb8MMxj5iF3ZRRQdLsP20bvDdLxFDNMWMKO0ua8CAWmzcwFGuvKVpRmDDtcIi6HhTZYIqQ5jQntih2P9lQx_DY3HzcO5XNSWJ987FGEOhMqnSbSN1DmbbO6w_H7xASvy8cWBO01GOETF9A-hX4sXAtal-I7S7FDN69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: تعهداتی که داده شده باید حفظ شود. نه اگر و نه اما و نه بهانه‌ای. برای معامله نزدیک پیش رو، راه دیگری وجود ندارد.
🔴
هر چه بکاری، همان را درو می‌کنی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/127482" target="_blank">📅 22:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127481">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
عراقچی: دشمن تصور می‌کرد که بعد از جنگ ۱۲ روزه، در جنگ ۴۰ روزه می‌تواند ایران را تسلیم کند اما با مقاومت جانانهٔ مردم و نیروهای مسلح ایران مواجه شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/127481" target="_blank">📅 22:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127480">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گفتگوی تلویزیونی عراقچی در صدا سیما آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/127480" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFXlg0Yp8R2-booSphdlKRJIODecwYHErAi3n12NnoMGm3kxWvCcQUDfUK-1FVWR2rbfwrTudjESpBMZ1pNdbJ2oa5m0gdnUt33DU4O4b1INX2uermmFV_7gQct-uSz0QuN5cj0WLbCu-3pdczhAhH88Mhic4cA0XSw5ANAzhCTjgTKlzVhNK1P_15Vg1AyEmVBnl01pkeZwEz_dAU3cTT72RUO9LkuYo5F_K6Sf7hxu3ocD23gSE_Hf6zSBI_mWj9NwaVQ_nocazixyBaJ-fvmCbRF72DtIxUvYT_s4jcoqS8Yc-K4gSW-cDTUlkuBiqkg_dLBdqG_VAcR6fur8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر هواپیمای Boeing 737-7JZ BBJ A6-RJF در آسمان تهران که حامل ۳ میلیارد دلار بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/127479" target="_blank">📅 22:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127478">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تسنیم/ حزب‌الله: لبنان نیز شامل آتش بس میان ایران و آمریکا است
🔴
«حسین الحاج حسن» نماینده فراکسیون حزب‌الله:بر اساس آنچه از سوی مقامات ایرانی به روشنی به ما ابلاغ شده، لبنان نیز شامل آتش بس است.
🔴
بر اساس آنچه مقامات ایرانی به ما ابلاغ کرده اند، اسرائیل از خاک لبنان بر اساس این توافق عقب نشینی خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/127478" target="_blank">📅 22:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127477">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
ارتش آمریکا: اعمال محاصره دریایی علیه بنادر ایران با قاطعیت ادامه خواهد یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/127477" target="_blank">📅 22:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127476">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2k78G0BwRBEJTsie_jGPdMuiP1VNisRWQwuUKzfXqqFydiBs5g9apIcAUgubt4X1FPDpTvLCw0DyZZ6bKNN6yXuePUJhanl_MbC1CcgbsOL7c_ejIdFdX8dhBaV_iBpGcYXNWhzdr8GUcRAeBRNM0W-iq-8img9grNr0aA0Rebskb8dFl8FePrAKTSkFjRYd6G8ohMd-LQQaAmtMQwvIJ3gbrr44JwjX6iGfbX71h7UCXuQ73PhPomRT3ZdJ1qTVghhWUSuw8xPD827o-I0uMu4y7RpE-NE8K4T05fXRF3AW5F8r6mA6PRYdfF2b0qJJtUBtUZvq8jEtpJS9MCkow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی بزرگراه صیاد تهران یه مرده حین رانندگی
دید عه زنش داره بهش خیانت میکنه
با ماشین از روش رد شد و به راهش ادامه داد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/127476" target="_blank">📅 22:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127475">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
توافق بشه یا نشه چه فرقی به حال مردم میکنه؟ هیچی
🤔
مردم فقط یه چیز میخوان و اونم خودشون بدست میارن. ظلم پایدار نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127475" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
عراقچی، وزیر امور خارجه در برنامه گفتگوی ویژه خبری امشب ۲۲ خرداد ۱۴۰۵ در شبکه خبر حضور خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/127474" target="_blank">📅 22:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127473">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرگزاری فرانسه: سوئیس پیشنهاد میزبانی مذاکرات ایران و آمریکا را داده است
🔴
وزارت خارجه سوئیس پیشنهاد کرده است میزبان توافق احتمالی میان ایران وآمریکا باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127473" target="_blank">📅 22:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127472">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988e3b12cd.mp4?token=uPze1NOqdCiJJrecllfwcMBieaumVUlNlum5E_g2fjtnke4VOXxuyKZFsleXYReK0NUckLYMobXOT7FpK21G15YqFG96qQFKRc5_3lzDLZ7ciTPqv_Ba4AlHDZzEPNogcl8psOxTdN3xjjRKBaeckKfJc3IAy15Nlfz9YhomWXMUHcI43bO_z1HvBreALGJv2LFg9HctUDIw2Mko5L7RWly7fzKX48V2Tt1_reWD_-3OvUfqjgEkYrddwISUz2sJBD_khLEO6D85HTb5RT32qWhvdumHXlf6kiLqOScFrjgaoJi1kyQfdkoqDmbkaNysXfhqdbKIkAy18eCz5LQiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988e3b12cd.mp4?token=uPze1NOqdCiJJrecllfwcMBieaumVUlNlum5E_g2fjtnke4VOXxuyKZFsleXYReK0NUckLYMobXOT7FpK21G15YqFG96qQFKRc5_3lzDLZ7ciTPqv_Ba4AlHDZzEPNogcl8psOxTdN3xjjRKBaeckKfJc3IAy15Nlfz9YhomWXMUHcI43bO_z1HvBreALGJv2LFg9HctUDIw2Mko5L7RWly7fzKX48V2Tt1_reWD_-3OvUfqjgEkYrddwISUz2sJBD_khLEO6D85HTb5RT32qWhvdumHXlf6kiLqOScFrjgaoJi1kyQfdkoqDmbkaNysXfhqdbKIkAy18eCz5LQiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از سایت راداری رادار هشدار زود هنگام AR-327 در کوه دخان بحرین که انهدام رادار را توسط سپاه نشان میدهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127472" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127471">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رویترز از قول دو منبع دیگر، مقدار پولی که قرار است از سوی امارات آزاد شود را ۲۰ میلیارد دلار دانست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/127471" target="_blank">📅 22:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127470">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / رویترز : قراره امارات چند میلیارد دلار از پول‌های ایران رو آزاد کنه
🔴
یه بخشی از اون، به مبلغ ۳ میلیارد دلار قبلاً پرداخت شده
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/127470" target="_blank">📅 22:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127469">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
گردشگری دریایی در مازندران به‌دلیل وزش باد شدید و مواج شدن دریا تا اطلاع بعدی ممنوع اعلام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/127469" target="_blank">📅 21:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127468">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / رویترز : قراره امارات چند میلیارد دلار از پول‌های ایران رو آزاد کنه
🔴
یه بخشی از اون، به مبلغ ۳ میلیارد دلار قبلاً پرداخت شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/127468" target="_blank">📅 21:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127467">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / سازمان ملل: از روند مذاکرات دلگرم شدیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/127467" target="_blank">📅 21:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127466">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مقام ارشد آمریکایی: به خط پایان نرسیده‌ایم اما بسیار نزدیک شده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/127466" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127465">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ایرنا: یک منبع آگاه به خبرنگار ایرنا گفت که سناتور «محمد اسحاق دار» معاون نخست وزیر و وزیر امور خارجه پاکستان در ادامه پیشبرد روند میانجی‌گری بین جمهوری اسلامی ایران و آمریکا، امشب عازم ژنو سوئیس می شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/127465" target="_blank">📅 21:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5071b9c1.mp4?token=EKneFWnI98r2-AlsSz2IDjgFNc6TURs-fZ8XolMeXklWfr5baMnwp595Cr6kgZTzWBtREX1lQNTAPkIwXY61CzZ9AS7TFPcq-2wbQJtfEfThK53B4e3gYLhOiGrMXFYOReB6jUy2ZnN1hVOXZevcR_40f4bh4mJbaKT-Ga-xXQeakLRg3cUeRqd0RHpg3nX0CWROLV8CXoEuysZ6lDHW1EKj0sXqkSeaRMcDBTWdv6Z1uBQwuh_DIJZKvK8DCUgzXMVnTNJQt1pVL0QLdRI5EUx6r6IwMw6m4tXtxq1TWLE571EZAsFfj1TB8V5-3jdLZiSjOIOdd1KrTfzqiiwH-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5071b9c1.mp4?token=EKneFWnI98r2-AlsSz2IDjgFNc6TURs-fZ8XolMeXklWfr5baMnwp595Cr6kgZTzWBtREX1lQNTAPkIwXY61CzZ9AS7TFPcq-2wbQJtfEfThK53B4e3gYLhOiGrMXFYOReB6jUy2ZnN1hVOXZevcR_40f4bh4mJbaKT-Ga-xXQeakLRg3cUeRqd0RHpg3nX0CWROLV8CXoEuysZ6lDHW1EKj0sXqkSeaRMcDBTWdv6Z1uBQwuh_DIJZKvK8DCUgzXMVnTNJQt1pVL0QLdRI5EUx6r6IwMw6m4tXtxq1TWLE571EZAsFfj1TB8V5-3jdLZiSjOIOdd1KrTfzqiiwH-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا، ماک کارنی،خطاب به مکرون
:
ما بیش از متحد هستیم. ما بخشی از یک خانواده هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/127463" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / الحدث: وزیر خارجه پاکستان امشب عازم ژنو می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/127462" target="_blank">📅 21:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در مورد متن تفاهم ما در مراحل جمع‌بندی در داخل هستیم
🔴
همین الان جلسهٔ نهادهای ذی‌ربط درحال برگزاری است
🔴
هیچ‌کدام از گمانه‌زنی‌ها دربارۀ متن تفاهمات را نمی‌توانم تایید کنم
🔴
اینکه دربارۀ جزئیات روند دیپلماتیک نمی‌توان صحبت کرد به معنای نامحرم‌بودن مردم نیست.
🔴
در مورد زمان و مکان امضای تفاهم نمی‌توان نظر داد و باید اول منتظر بمانیم تصمیم نهایی در داخل گرفته شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/127461" target="_blank">📅 21:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
یک مقام آمریکایی به خبرگزاری فرانسه: توافق با ایران شامل لبنان نیز می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/127460" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
یک مقام آمریکایی به رویترز : نمی‌توان تاریخ مشخصی برای امضای توافق ایران ارائه داد
🔴
فکر می‌کنم داریم به تعیین تاریخ و محل امضا نزدیک می‌شیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127459" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز:  توافق‌نامه ایران اهداف اصلی ایالات متحده را محقق می‌کند.
🔴
توافق‌نامه تنگه هرمز را دوباره باز می‌کند.
🔴
ایالات متحده مواد هسته‌ای غنی‌شده را دریافت خواهد کرد.
﻿
🔴
توافق با ایران شامل یک رژیم بازرسی است
🔴
اگر ایران پایبند باشد، از نظر اقتصادی پاداش داده خواهد شد.
🔴
مزایا برای ایران تنها در صورتی محقق می‌شود که واقعاً تعهدات خود را اجرا کنند
🔴
منابع تخمین می‌زنند که احتمال امضای توافق‌نامه ایران بین ۸۰ تا ۸۵ درصد است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/127458" target="_blank">📅 20:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/آکسیوس: ترامپ به نتانیاهو اطلاع داد که زمان پایان دادن به جنگ با ایران فرا رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/127457" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NITCAUYcljY_8XAIdao_C_JcYhy8q0SNL2N5eai_SxbHhgE-h1AvyRLOalangZMnh6Y-2dw97F-LuVMrtEG2zuBjVytUuWWryVYWsIU8P_iJl7JJngFt-U6UjgRkYuYQGiYfCNiZ99Qm6IkoMgs8dpIAPLbg59bkF5KL5a7J9bs7YEreoBQfc6_GrepCCmhfzRPzGO1irfiG0Y7r9HcWlCo4r7xWqFF46mhQPMjhzJxw8cpuM4SiFLQZimYpEp7GkOjOUeT4U5BwUHAhmOSj26kvQOblZw82DmK_tsyTs3ig83o7a_TNo7Wh3T4uv3eFR4RyrnnkKVOhChQJPzmwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در سال 2049: ایرانی‌ها هر لحظه ممکن است توافقی را امضا کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/127456" target="_blank">📅 20:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
باراک راوید(اکسیوس) : رئیس‌جمهور ترامپ در یک تماس کوتاه به من گفت که پست عراقچی، وزیر خارجه ایران، را «بسیار مثبت» ارزیابی کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/127455" target="_blank">📅 20:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/ آکسیوس به نقل از ترامپ: ایران به‌طور محرمانه بابت ارائه اطلاعات نادرست در مورد توافق عذرخواهی کرد.
🔴
من همچنان بر این باورم که توافق ممکن است تا پایان هفته یا روز دوشنبه امضا شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/127454" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/ثابتی، نماینده مجلس: طبق اطلاعات به دست آمده متن یادداشت تفاهم نامه احتمالی بدتر از برجام است، چنین توافقی نه گشایش اقتصادی می‌آورد و نه جلوی جنگ را میگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/127453" target="_blank">📅 20:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127452">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
برخی از رسانه های لبنانی اعلام کردند که ارتش اسرائیل درحال تلاش برای ورود به شهر نبطیه در جنوب این کشور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/127452" target="_blank">📅 20:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127451">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfJf-sNILHYvH43qKIJg7QCu5WJSiBVmJemQ8PjMmjn-CWh5_L9OVL-Gl4PvfpfVTGjLYuAHKR8731K3N9P3N4hKcLhJ92OC00xbkL-vh5KNvuby63x1zCF8mP9H7raBtYFVNZyYL73hcGN5CYCnfTIXqpRHDIWIG_ypkPKyh8AodqgHNaCA0JUt_wPLzt61R90ymsP-rEXNJwIqmI7Tgah3k5GrWcu7eI9EnZ7yErtHHWBNvlYj96eIXtr4pExL6i6b-j7E5pWF020oKAYzL5oiS1f8lED6giaxntc5DDF347AeAKKIk_t8rWl8-kOwlSKGit14Lxeb_OVsFXVcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گروسی: اولویت ما راستی آزمایی کامل از توانمندی‌های هسته‌ای ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127451" target="_blank">📅 20:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127450">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عزیمت پاپ لئوی چهاردهم، رهبر کاتولیک‌های جهان ازاسپانیا در پایان سفر یک‌هفته‌ای، به دلیل نقص فنی در هواپیما به تأخیر افتاد
🔴
پاپ به سلامت از هواپیما خارج شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/127450" target="_blank">📅 20:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127449">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR0Gz1PraFTs1YN8TYq8fCReRMvUEdah4BORoEdvMvWSgtvy0RerrZf-LuK9ZZRtVPp6rdOCiw7xO86HnuYLZ5N_nZO48NQ9xu2meuoApLP3MOp5Rc5TBYBygfrDMu_ajb9u_CSEx3z0JX5EbvZNSSzVRgIlW7b0sTYtOnL9F4wJmd5e5WujpPCIr2xJQnSkUvJuwD8yftkJsaHryrlIxBLoeb3RapPQO2lrPy3X226EElT4jBrjOiR7C-Lo3wlVkFxCr-TFxbsvkSQfdsp9hIqL4M2h3MkTsvFc14Fv5IRJDP7F1vTmr4PKw1pWoXxvbvZEWJhp2CXpTS_2QkoLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به شهر النبطیه در جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127449" target="_blank">📅 20:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127448">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4978ed4fb.mp4?token=H2xB---aiygTLelr7ek6AiPXssYiUcUHLLY5No4_dNnbpJ1oAGE-q6myM5ZuluO7ArAlQMBFPovbDGqkjvL-k9tsMcnQFEDgIfZipzYNAZgfFawHnBsNvZ5gUs9KK85JNIvAqsgnuoGVpn2IMmNYHyxncWwKRcLGEooXCJX7MQvRHJG12gEjdLJBgaRQnfdb6fXCLJSIZ2J5zrn_e_7GyFsaEf3FH74VGteyZ9SjiNlICO5LWujvp-1eyXVClbmHHr5kVQL-B3F1aAMvXBQByW7tJP8VY3stGi5e95Vf3rtTYovaUhaPngFlGEwj7mveJ0iSU80nMT4EPafNRgyZAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4978ed4fb.mp4?token=H2xB---aiygTLelr7ek6AiPXssYiUcUHLLY5No4_dNnbpJ1oAGE-q6myM5ZuluO7ArAlQMBFPovbDGqkjvL-k9tsMcnQFEDgIfZipzYNAZgfFawHnBsNvZ5gUs9KK85JNIvAqsgnuoGVpn2IMmNYHyxncWwKRcLGEooXCJX7MQvRHJG12gEjdLJBgaRQnfdb6fXCLJSIZ2J5zrn_e_7GyFsaEf3FH74VGteyZ9SjiNlICO5LWujvp-1eyXVClbmHHr5kVQL-B3F1aAMvXBQByW7tJP8VY3stGi5e95Vf3rtTYovaUhaPngFlGEwj7mveJ0iSU80nMT4EPafNRgyZAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافق کنید جواب اینو کی میخواد بده؟
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/127448" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127447">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یک مقام اسرائیلی به روزنامه یدیعوت آحارونوت: ترامپ ما را فریب داد و توافقی که قرار است به‌زودی حاصل شود، بسیار بد به نظر می‌رسد و اصولی را که هنگام آغاز جنگ با ایران درباره آن‌ها صحبت کرده بودیم، برآورده نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/127447" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127446">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c291502e6.mp4?token=GK7TSxBf9WVGRxirxD-mRYbjMBT5OaAV6pnYq5QR9kDWbJUzvPoMfua-r5Cto9NRc4_u8eFxafJiyC1Ldwm2LQNGZoUPBUfAYmW7ul2rk9vpDNwk9X9fZALUEs-NOCBlqqFh45hBwMZCl4QjJ3fq3Ct9rJpe8KvqwowL9pyNdBtrseMj-4stAtrIQDqSsjHGTRBLPScs-rJOLfTT1sx6mXsJeDSQXj987yrz5Sn7K0_rARgmdbjESllpT6wUGcNnkxENd_oJsZT94tISJLVz4xvPxxOwNzRYbNbavkxEqHbUyOgp7umf0jYJ66uxoWviTjj_M2uLZ6sLOTBsnTbo9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c291502e6.mp4?token=GK7TSxBf9WVGRxirxD-mRYbjMBT5OaAV6pnYq5QR9kDWbJUzvPoMfua-r5Cto9NRc4_u8eFxafJiyC1Ldwm2LQNGZoUPBUfAYmW7ul2rk9vpDNwk9X9fZALUEs-NOCBlqqFh45hBwMZCl4QjJ3fq3Ct9rJpe8KvqwowL9pyNdBtrseMj-4stAtrIQDqSsjHGTRBLPScs-rJOLfTT1sx6mXsJeDSQXj987yrz5Sn7K0_rARgmdbjESllpT6wUGcNnkxENd_oJsZT94tISJLVz4xvPxxOwNzRYbNbavkxEqHbUyOgp7umf0jYJ66uxoWviTjj_M2uLZ6sLOTBsnTbo9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حادثه تیراندازی در میدلند تگزاس
🔴
برابر گزارش‌ها در این تیراندازی چندین نفر زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/127446" target="_blank">📅 19:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127445">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: رئیس‌جمهور ترامپ در حال حاضر به سمت توافقی با ایران پیش می‌رود که از دیدگاه منافع آمریکا، از جمله منافع مشترک با اسرائیل—برای جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای—است و ما انتظار داریم او این اصل و اصول اضافی در حوزه موشک‌ها و نمایندگان نیابتی را حفظ کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/127445" target="_blank">📅 19:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1ujqLdm0o3rRawp-4e0kxFwO4EhbViR837PPbbB6Gm_YVifbSWxIeqhPpfSbTdzy_CY55TkQQlJqqYiQBArR49jwTriuzhaHEipsHOEPMsrnpoORh_cVE9mX4DK9kfct3cR5tF_ujCM19wccB0jSRA-jYDn-NW78CMaqRkSYXbvmcvGzNppm0RBUk3mi31-IhRoPM_vMnoX4LyGUNkVYEg9_rrbC3dx5xlAJP_I3DuGkNR5GSvu6L9XZjKWxElTBnJ8HEfDdtv-K9uiJQuVtgPLgvHiH2zpXUX3XaQsbZGhlzUEdJ_mfVTKryQdo4PdZWsVWcFxoY_F3b2kcLImEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / نخست‌وزیر پاکستان، شہباز شریف:
در میانه تلاش‌های شدید میانجی‌گری پاکستان، ما کاملاً از کمپین مداوم اطلاعات نادرستی که توسط کسانی که می‌خواهند توافق صلح را خراب کنند، آگاهیم.
🔴
با کنار گذاشتن سر و صدا، می‌توانیم تأیید کنیم که متن نهایی و توافق شده توافق صلح به دست آمده است و پاکستان اکنون به طور نزدیک با هر دو طرف برای نهایی کردن مراحل بعدی همکاری می‌کند.
🔴
صلح هرگز به این نزدیکی نبوده است که اکنون هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/127444" target="_blank">📅 19:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال 13 اسرائیل: ایران می‌تواند هفته‌های طولانی به سوی اسرائیل، موشک شلیک کند!
🔴
ایران هنوز هزاران موشک بالستیک و شاید حتی خیلی بیشتر در اختیار دارد که می‌توانند به اسرائیل برسند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/127443" target="_blank">📅 19:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سنتکام: به گشت‌زنی‌های خود در آب‌های سرزمینی برای اجرای محاصره دریایی علیه ایران ادامه می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/127442" target="_blank">📅 19:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127441">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc5aef8f6.mp4?token=f5aWa1tkiNZxgc1BXNSwwVuZ3zYD156dGnfccloC8aeFlHJAOSLPRmGBe6WQoMYNSghlwLMzdG4lN7ieaofX7XRvRlTnM5ImBmGzgrDGEXlp2xAhVhsJngSmGL4RgoqENVJCMsd4sL6S4lQs3V0-nMGRTGlMsuUH1pPkW0k7Ei_jjKakX7gw9jTgA1a0WVaMuj0aYRTfJ7R3JYG1gJG45sSGZ7FCmQFjE2dxBWm1_m90h5J0c9EdFjacD2vHv9kcGBbdioBZmSQtCRA5T5cX-L951gOuZPcYQaBdzWpdGeUMh7uaWW11tsOBE8HX1dePV1HRLuP9zWs43jKFi3mukYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc5aef8f6.mp4?token=f5aWa1tkiNZxgc1BXNSwwVuZ3zYD156dGnfccloC8aeFlHJAOSLPRmGBe6WQoMYNSghlwLMzdG4lN7ieaofX7XRvRlTnM5ImBmGzgrDGEXlp2xAhVhsJngSmGL4RgoqENVJCMsd4sL6S4lQs3V0-nMGRTGlMsuUH1pPkW0k7Ei_jjKakX7gw9jTgA1a0WVaMuj0aYRTfJ7R3JYG1gJG45sSGZ7FCmQFjE2dxBWm1_m90h5J0c9EdFjacD2vHv9kcGBbdioBZmSQtCRA5T5cX-L951gOuZPcYQaBdzWpdGeUMh7uaWW11tsOBE8HX1dePV1HRLuP9zWs43jKFi3mukYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل به منطقه
تفاحتا
تو لُبنان حملهِ کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127441" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127440">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63455018a4.mp4?token=fb4Z1rq_woW-CJREXhdyji4bvs3-wxGeNTTxthA8lmuD8u6EzODU_fFCYt42ei1HCBDt5l0KONIivuiU4izpmvzJDjliVx48jkdXdTByRY5Ls3v4D2F0qqIr0mBejZa0Oza2SwSGx7NZ9-OLF8YzoDsDGES8Uw8pZ2InmMnEx-0-zj8d_viKTdeJY1Ikt6eljuq8M3SaNO-3yaSnxPN1OvUVkfu4GItB4rFpfyVmspAgZ1cGx8d-PERklZICu05PSXbfwDxfz5vKN4xnLVSJ3R1YVNqa6cNkqI5LDBySJBSxSOwHYLsdntcliDateV3JgQozwg0GmoHhLOiphV6yJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63455018a4.mp4?token=fb4Z1rq_woW-CJREXhdyji4bvs3-wxGeNTTxthA8lmuD8u6EzODU_fFCYt42ei1HCBDt5l0KONIivuiU4izpmvzJDjliVx48jkdXdTByRY5Ls3v4D2F0qqIr0mBejZa0Oza2SwSGx7NZ9-OLF8YzoDsDGES8Uw8pZ2InmMnEx-0-zj8d_viKTdeJY1Ikt6eljuq8M3SaNO-3yaSnxPN1OvUVkfu4GItB4rFpfyVmspAgZ1cGx8d-PERklZICu05PSXbfwDxfz5vKN4xnLVSJ3R1YVNqa6cNkqI5LDBySJBSxSOwHYLsdntcliDateV3JgQozwg0GmoHhLOiphV6yJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد FPV اوکراینی باعث ریزش زمین شد و سربازی روسی را زنده دفن کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/127440" target="_blank">📅 19:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127439">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5mY51Bgh4p8t4RLZKNcshTh9psEAOZWD6zKhRv-QgDYCxiWmU-T_DM12ZEzFcpEWE96rpcQAL5ABTlHcIK57q6YLcFrePO7n9ovcxiwR5-RB0lE-SzzIeJCxVpkJUG3hW2-U3l-sChRgMqXDWz4JZDvh_O_bSqspNaWhg_xtmCnNJn1V4Fint8dpZtDd0mF4fC4zlmOt5DS0hvOxPFhEBQZ-mBetz9rUR4t5bGcNe8SPsmXsoESyqY0flQDUXACZESTvUuzskYnAB0XedMEmiomAoqTkjku71eGod1vIaKGzAYkmoRd6WBx6F8Ss5EGFasuwJhyuvccWXAYVBQnCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمود نبویان در واکنش به توافق احتمالی:  وقتی خرش از پل گذشت، برمی‌گردد و به ریش شما می‌خندد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/127439" target="_blank">📅 19:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127438">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jURtBX91-8-BmkQZ3j3L6bBb_T3SX2kj8nGEEOkXI7OJ6XYEYCM8EHx3IK8JeDTiPS9cB08sz12ClwfD8Xq8YdtUiYFgTkaQDaF6sKw5oMvIm7jplCeEAR6DRPsvuYjJ-_nt8hi4InizD0SjSGjS9FiQLGqcdH-IqgtG_yolUC9GHQaub2VuHPjESXBRHgqFkxux0smTOiGaUBdF33CS7iuItD3K_BCvksafMRgb3_m9OWjJoD_lnbCfdJCz5ckByg7aDfoBqsiG9Kc-5v0eG-xTi_VmQ5_G9YHSEMFYyc8n3v1agBlBj-VEkDLxlwdW2e8j_HEKonyz5oEHu1ONvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ترامپ توئیت عراقچی را بازنشر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/127438" target="_blank">📅 19:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6036168b0a.mp4?token=OUEb-_AcNfUR1WDZnFMRXugP1op7h2b5Sn0ypEziLmv7wwbs5pDTZvxp_PBVL_4WVbn3tehRhMFOzsUeSdg__ttLbG8lfVqgvJDHHOdjuqWsePdEYNMGdZfwF9geNQQheX9QrqNpnIWZXoa_TOxHEdum2ar-HzF2BVGqUrBe4m46Hu2fc97v1IWkvREmta6YLMQX2Kb0gdzcTUB9TWLaYZMj2ck75vqOgSWE263aTZx7SiItDakViv21rkLJEnBluTLVS79hdOlH3FSZOGjtspiGlfuPSXj4SdaPdLDznWrdMNHwim-7bVxNM04mzBdmxHwvK6iCp3Fob9Dixfoo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6036168b0a.mp4?token=OUEb-_AcNfUR1WDZnFMRXugP1op7h2b5Sn0ypEziLmv7wwbs5pDTZvxp_PBVL_4WVbn3tehRhMFOzsUeSdg__ttLbG8lfVqgvJDHHOdjuqWsePdEYNMGdZfwF9geNQQheX9QrqNpnIWZXoa_TOxHEdum2ar-HzF2BVGqUrBe4m46Hu2fc97v1IWkvREmta6YLMQX2Kb0gdzcTUB9TWLaYZMj2ck75vqOgSWE263aTZx7SiItDakViv21rkLJEnBluTLVS79hdOlH3FSZOGjtspiGlfuPSXj4SdaPdLDznWrdMNHwim-7bVxNM04mzBdmxHwvK6iCp3Fob9Dixfoo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حملهِ به روستای اَلسَرفَند تو جنوب لُبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/127436" target="_blank">📅 19:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری/العربیه به نقل از یک منبع دیپلماتیک: آمریکا و ایران آمادگی خود را برای امضای توافق به میانجی‌ها اعلام کرده‌اند
🔴
دولت ترامپ در حال برنامه‌ریزی برای برگزاری مراسم امضا در ژنو، احتمالاً در این آخر هفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/127435" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شبکه ای‌بی‌سی به نقل از یک مقام آمریکایی: پیش‌نویس توافق مورد موافقت سطوح بالای نظام ایران قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127434" target="_blank">📅 19:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سید عباس عراقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.
🔴
در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127433" target="_blank">📅 18:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6UJD7G2tnLL2-v01srTRvVpGW0MWj0Jm9OvtxeR1IAGKfaRlibrBOVAt5sa129TFwpk3AU0lX52znOniydXVAwCPHt33qfbYvmKqjB7msAIVHGWsLEF9AD2aIS10O2Jbzz8SPbaQElz3VzoFCyxxP6DqSgW90WRfk4lP4m2kFNs7XqmWTjhq8N0g-jeJLBtVWSY3jaPBBXW_1_HueqOizoGhNW0Qhj9hA4k8MH1vVspL3CfA5_e1n_TtynFGriqdVILkaHAo0sYdwZSGleYIrUTuBpwT53i9ptP4vZK54RVd2wsP2Auwc4YrKkmKNdtnzpuDocdvaUZGzQRkgZMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو حمله هوایی اسرائیلی به شهر صرافند در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/127432" target="_blank">📅 18:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سناتور لیندزی گراهام: ایدهٔ یک صندوق بازسازی ۳۰۰ میلیارد دلاری، با توجه به اینکه چه کسی در ایران مسئول است، به نظر بی‌توجه می‌آید.
🔴
این مانند طرح مارشال برای آلمان است در حالی که نازی‌ها هنوز در قدرت هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127431" target="_blank">📅 18:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0JawyejPMzGhRMPXPs0duK76jJN30HEEBjScJ9vmRirP1zsTz_U58pjP01tl6Vj1f7f_cVs-ES6ln7QlOHSuXF6rgLBSTjA0ZyuO3_p_hSPp59wsG9R1zBDeqES01V52grYnVnlrKFHrQXKsvWeEwlIO0B9hUiOlsKWMcTqvg1cOOSClz5zrwsUfWUkeeOkJEVBzhy3VfjZ1ot24ysHQ5urnK9FR1FFKwSHfaj9HKvwewqK24okD08TBNvAHbJP5-VE5Rnm1mhIQtqAEUORtJONz5i_MQgHF-OC_4Hbbso-4kl7w54LFiZUywN67BkPYFuEm9nUVIXbxP63Ef46hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جی‌دی ونس: اولاً، ایرانیان هیچ وجه نقدی دریافت نمی‌کنند و هیچ وجهی صرفاً برای امضای یک توافق یا حضور در یک جلسه آزاد نمی‌شود. این توافق به گونه‌ای طراحی شده است که نگرانی‌های ایالات متحده و متحدانش اولویت داشته باشد، و اگر جمهوری اسلامی ایران تعهدات خود را انجام دهد، فواید اقتصادی به آن‌ها و کل منطقه سرازیر خواهد شد.
🔴
این توافق پتانسیل بازسازی منطقه و منجر شدن به صلح پایدار را دارد.
🔴
چند مورد عجیب را در گزارش‌های چند ساعت گذشته متوجه شده‌ام. اولاً، افرادی که (به درستی) ماه پیش می‌گفتند دونالد ترامپ یک رئیس‌جمهور تاریخی است، اکنون بر اساس گزارش‌های رسانه‌ای تایید نشده یک توافق را نقد می‌کنند. ثانیاً، افرادی که می‌گویند به کلمه‌ای که توسط سپاه پاسداران انقلاب اسلامی گفته شده اعتماد نکنید، ظاهراً به پست‌های شبکه‌های اجتماعی ناشناس با منبع ناشناس باور دارند.
🔴
رئیس‌جمهور قرار است به هر روشی که باشد، نتیجه خوبی برای ما به دست آورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127430" target="_blank">📅 18:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127429">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738cca7c3a.mp4?token=lLsTeJOq_iujM3VtScH9Dh6UOvqRT26iCJet4JYOgZs8NWqFWo8IWYyLWZfGi4gvfHdKOcWSnMaVBTenvaY2aNOl4ODDVFJ1Ies2OblgRcUUE_IPLs0TG-DKGYX2oM4hmlqLKv4fRnc0aSvqqGepZLMgQCXGYmrcHJH3VnAY9u_0YSnvy9NY_tpFu23cuKYSmY0qpQBew0ZLswVzax_QDPRIK-EittyAD9nxxL2zaPGV469l3WtjqbHlm29eQx8iD5OFzLNx7M-Dx4HEUrvqoWMUarNgw1UF4lRrdrNQNJsNV9xSOl9UpejqopjhvZe_zamPWkH4KigjQLqorpgVp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738cca7c3a.mp4?token=lLsTeJOq_iujM3VtScH9Dh6UOvqRT26iCJet4JYOgZs8NWqFWo8IWYyLWZfGi4gvfHdKOcWSnMaVBTenvaY2aNOl4ODDVFJ1Ies2OblgRcUUE_IPLs0TG-DKGYX2oM4hmlqLKv4fRnc0aSvqqGepZLMgQCXGYmrcHJH3VnAY9u_0YSnvy9NY_tpFu23cuKYSmY0qpQBew0ZLswVzax_QDPRIK-EittyAD9nxxL2zaPGV469l3WtjqbHlm29eQx8iD5OFzLNx7M-Dx4HEUrvqoWMUarNgw1UF4lRrdrNQNJsNV9xSOl9UpejqopjhvZe_zamPWkH4KigjQLqorpgVp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
الشهبیه، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/127429" target="_blank">📅 18:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127428">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یسرائیل کاتس، وزیر دفاع اسرائیل:
«اسرائیل باید توانایی اقدام مستقل برای جلوگیری از دستیابی ایران به سلاح هسته‌ای را حفظ کند و به همین منظور به ارتش دستور آماده‌سازی داده شده است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/127428" target="_blank">📅 18:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127427">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-bsQ1EXXe--c0H914jE3cXVIlF58vRBWpnxNSQwRzS2rBcaczaOYeZ5uI1tay7sNz3gbOu2sZJMWbkzbP7UGuja1o6rn7kWNILUFWQVLrKuoaiGW5IQQWJR63uvqMdlMIRBPdOaf7RUoHRnKAcxCJ4xLl3XLrQXV-bsNTATgAXB2u92vpUOMoJ8rPEiepzQmc_NED3wkvamHPkJxocI-rO4lXDQoN-TQX8WV3fUtEYsHr0RZwJO9e64cqC0QCD5flW_L9y3MwUFgLtU48z-ZoHhT9xIWty-lU36nEzI9h1HzeUtZYqJSgeCLZDIAZIYJ-ZQvxVo6_c-a2wYWHmHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید عباس عراقچی، وزیر خارجه: حفظ یادداشت تفاهم اسلام‌آباد هرگز به این اندازه نزدیک نبوده است. تا زمان نهایی شدن آن، رسانه‌ها باید از ورود به حدس و گمان درباره محتوای آن خودداری کنند.
🔴
در راستای رویکرد مسئولانه و شفاف ما، تمام جزئیات در زمان مناسب با عموم مردم به اشتراک گذاشته خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/127427" target="_blank">📅 18:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127426">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پزشکیان : باید فرهنگ مصرف بهینه را به یک گفتمان ملی تبدیل کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/127426" target="_blank">📅 18:26 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
