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
<img src="https://cdn4.telesco.pe/file/uCVdvWSDkQODwAOmJb-g6QbP0m0HQFHmxtnM6sCoAA1bxKjjXG_8093pOXGRdESjfMyLPAkoII7rPicFnG47zm36b6gTLarRFlm7iR5yWABDvznaYOVpu5x_2nTR7zftdIO_xuuoC9laJM3mOXa2x8OTVsEzVlGQrz9GH2BIHJqNZVik2dmKNHlfJVHVgaRW6hY75H45lXh8Hl4g8M_M6WfKJOiJDxBsPAqLQrHDiXRW-MbYiHNJxKlXia4hr2FnVxOZwKqOPZzSsJ4Lr8qaTxiRe-l7WQZbVjGgcXNGS0zLQIlpAP7H6gqRk7Unwn4JBx_9Neo7Vg-G9UIlXGBBPA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 979K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
<hr>

<div class="tg-post" id="msg-127982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
تسنیم: لغو پروازهای غرب کشور تا اطلاع ثانوی
🔴
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است
🔴
پیگیری‌ها نشان می‌دهد تاکنون نوتام (اطلاعیه هوانوردی) رسمی در این خصوص صادر نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/127982" target="_blank">📅 22:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو به ترامپ
نه
گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/127981" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFjvpphii4keeirmuKwZShicVCX3fohBjw35pYhQDGf1V_uMBokm0PzSXhWdzvqB1ONyq5wLekZnHgg1mEkZ6z1jZBxeB4-uv-4h0ynSRsujRfjz4Qt0YUYxfs6jZcNSb7sUgMoNHNu4Rwo1TaqDgmJQ2fZz-o-OmWxAb07RcV_yBEPbt68WuJlZCyFh_Gfa7AKwFxGGfbsAoDq2_JuvzStKxxY4bK8lCD08IGau5Kz7aWd-EZNpzCXLPYjouYPTBYLxSFieuaGNfYYg84wmDkU9TQ6ALmX5ps_1NQetoX0YBRJ1TnyB1UuvuqL3Z0ppaniyiEXYAYjH0HBPjNp46g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک‌وتنها گیر بیاورند
🔴
مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را برهم خواهد زد، بچرخ تا بچرخیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/127980" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
طبق اخبار رسانه ایی که درحال پخش است، بنظر می‌رسد ایران و اسرائیل درخواست خویشتن‌داری از جانب آمریکا را رد کرده و آماده درگیری احتمالی می‌شوند. باید منتظر ماند و دید که چه خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/127979" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یمن: نتانیاهو بدون چراغ سبز آمریکا، دست به حماقت نمی‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/127978" target="_blank">📅 22:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJCAZDALVGAtAAYDIIBZMcWTG4EKlZdICEiKRci6WADOHtlS1zLp4zm-lUA4sidJgO2zkGDwe2XMm_V8QSSR4lc7qM8D22bwkB0DF_WrYGneFNwdXrqyTerHr63V5f24YUflSk7iT4RkmMzs7ahOriyV73o9cJvFkzu4rD98YlUZ9KQNmkguQo2umdJgswgAb3jQ3PB4y_UnR4q6sO2Yl6qOdmT3DvN5b9POlY3HBioVsWS4O2_HZ_DjWPSGTV3Ybox1Gg25DB6skHpuO7EKHeFjRDAryRPNFpvkrHueHtpP0iSFnMXhHK7Ta0o9fadUGEhnfoLefmIkXPM6tQPlrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نظر فضای هوایی ایران بسته شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127977" target="_blank">📅 21:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ از نخست‌وزیر اسرائیل نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌نشینی نیروهای ارتش اسرائیل نماید، اما نتانیاهو هر دو درخواست را رد کرده است، طبق گزارش وای نت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127976" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
یک منبع غربی به کانال ۱۲ اسرائیل گفت که ایران هنوز در حال بررسی پیشنهاد رئیس‌جمهور ترامپ است که شامل پول برای عدم پاسخ به حمله اسرائیل در بیروت می‌باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127975" target="_blank">📅 21:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کانال ۱۲ عبری:ایران درخواست ترامپ را رد کرد و تأکید کرد: به بمباران بیروت پاسخ خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127974" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وزیر علوم: از 13 تا 20 تیرماه هیچ آزمونی در کشور برگزار نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127973" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارونوت: ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/127972" target="_blank">📅 21:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127971">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
یارون آبراهام خبرنگار اسرائیلی: ارزیابی اسرائیل این است که ترامپ به زودی امتیازی به ایران خواهد داد، در ازای عدم انتقام‌گیری ایران بابت حمله اسرائیل به ضاحیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/127971" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127970">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش فرانسه: ناو شارل دوگل در خاورمیانه می‌ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/127970" target="_blank">📅 21:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127969">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59cf18c21.mp4?token=k3-1wcpM3nbOPJ9YYocATqeMVnOtFBZjAoLkHh-M3WeNffWabFKg10ZnAxXd_EhwCFjtrghtd-RVVtIueaTb8Ck2nda9bN-ePFxihOM1OkuvPua-3Pg5-mgraZPP0u63k0IUOsrW2JilompawzYEs-w_YECzdf7B_e6jk7w8p6tzIyBmVDmOBByd4gVOTl5LfHsh7S8r-U0YTwVjdFU84P8GarGLUv4tdx61IQ8X7T1oaMPT-xSc12UahywxjAwGWmEnv1ljDtFB-iooNCwaAzDGFjD2VF5Nm3epNgK13VGjtIMyaQa1qG_IP0yYZLcROvLkfa2cYswAVyOK3BhSRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59cf18c21.mp4?token=k3-1wcpM3nbOPJ9YYocATqeMVnOtFBZjAoLkHh-M3WeNffWabFKg10ZnAxXd_EhwCFjtrghtd-RVVtIueaTb8Ck2nda9bN-ePFxihOM1OkuvPua-3Pg5-mgraZPP0u63k0IUOsrW2JilompawzYEs-w_YECzdf7B_e6jk7w8p6tzIyBmVDmOBByd4gVOTl5LfHsh7S8r-U0YTwVjdFU84P8GarGLUv4tdx61IQ8X7T1oaMPT-xSc12UahywxjAwGWmEnv1ljDtFB-iooNCwaAzDGFjD2VF5Nm3epNgK13VGjtIMyaQa1qG_IP0yYZLcROvLkfa2cYswAVyOK3BhSRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درخواست اعدام عراقچی توسط تجمع کنندگان تندرو:
🔴
عراقچی بی غیرت اعدام باید گردد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/127969" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127968">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فووری/ دبیر شورای‌ عالی امنیت ملی:
پاسخ ایران به اسرائیل در راه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/127968" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127967">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سنتکام : مسیر ۱۴۲ تا کشتی تجاری که تغییر دادیم؛ ۹ تا کشتی که همکاری نکردن رو متوقف یا از کار انداختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/127967" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127966">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
کانال ۱۲عبری: مقامات اسرائیلی ارزیابی می‌کنند که  ترامپ به زودی پیشنهادی به ایران ارائه خواهد داد تا در ازای اجتناب از واکنش به حمله بیروت، امتیازی بدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/127966" target="_blank">📅 21:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127965">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
طبق گزارشات اختلال هر ۴ بانک که مورد حمله سایبری قرار گرفته بودند، رفع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/127965" target="_blank">📅 20:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127964">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اسرائیل سطح هشدار را افزایش داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/127964" target="_blank">📅 20:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127963">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
دو سرباز ارتش اسرائیل در جنوب لبنان بر اثر آتش حزب‌الله زخمی شدند — یکی با جراحات متوسط و دیگری با جراحات خفیف — گزارش کانال ۱۴
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/127963" target="_blank">📅 20:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127962">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سخنگوی فدراسیون فوتبال: روادید تیم ملی ایران در آمریکا ساعتی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/127962" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127961">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
لارنس نورمن خبرنگار وال استریت ژورنال: در عرض دو هفته، ترامپ از این موضع که «لبنان از موضوع ایران جداست» به این موضع رسیده که «لبنان مرتبط است اما اسرائیل حق پاسخگویی دارد» و بعد به این موضع که «لبنان مرتبط است ولی من فکر نمی‌کنم اسرائیل حق پاسخگویی داشته باشد چون باید توافق را منعقد کنیم»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127961" target="_blank">📅 20:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127960">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbvfarZulYnMP-sf8cFvf_oRGC00041o0RBWZinC11BKFGCT0AAdbMEqj32EnE3ChVd5ABsdGk2TlKgaR9Nl_2aA9r55a9p6XtMxm1AhCza-kUctbsGTvymkoqdnMj7EyY1cxmZD4fLZ5Y22MUwJi_Ss3nUPMMJ6NN_WfZ4u8xKN2bFdJ6UCUsf9OEoVHaoVrEmqXTHE3OgzUBJVzJJ8eFVySeQuP2Fg7zx05xrZpdA7OgEph4APZXOng3c9LDgJmvj_MJmjvhoQr4cAvbLaeJSZmV29KHhxgkmDS4Gdpo3PHY6Ueumrm2xjPC8RXjKENPUqkCxZipfvAQRvmocWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خضریان، نماینده مجلس: ارتباط واتساپی عراقچی با ویتکاف باید کاملاً قطع شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127960" target="_blank">📅 20:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127959">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / الحدث : هئیت قطری هم اکنون به سمت اسلام آباد در حرکت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127959" target="_blank">📅 20:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127958">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سفیر امریکا در سازمان ملل،مایک والتز: ایرانی‌ها مذاکره‌کنندگانی فوق‌العاده سرسخت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127958" target="_blank">📅 20:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127957">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سرلشکر عبداللهی: فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127957" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127956">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ به اکسیوس: توافق به نفع اسرائیل خواهد بود زیرا مانع از دستیابی ایران به سلاح هسته‌ای می‌شود و این کشور را ملزم به از بین بردن مواد هسته‌ای می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127956" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127955">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKpV8G300tig1RQQD6VpU0hFjokkPf412CtJNb7k1t-kAE1f1auFk3rv3BbUdgKLzTV_Y8IbKod46HGF3y5HGomutB62EglvazTzfX7EeghOpDu0hwB-rzciSRTMmmmHNkgRmH5Cie-9jc80Pd5mIMyXgSlqnz07RQMafmDC3MqzDu7M48H6447pGA6IamrTfhRpnUxSFOF6NUtRcUDh8QnsEx4nM0oNKvch79jy3zyaWqPTlSlAzMhiJnTisOlEyLfRSyREhomxVK_ScIfy7BD4DpuRFKyA6gukWagm89CXV8uMpewVwwxu4qBTa-IaVi9cIPKLwGdlZa3dX7Cf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل توسط جبهه مقاومت قطعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127955" target="_blank">📅 20:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127954">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZgNLidj0XwMaYxF8CCrtPzLWNI8vARocozmggnB3bCfKhcEuUlqgHPciwF8ZaxziIheGO1NXDYQ0OLcEzAFaQA_GaLxA_HM1kXjaNdz8TWPreyhTFcKYPyeJbNb2cTRGTb9M2R7eRkQEsa6jijtDFZej6pVqFP_d_8e8vLvqb0zBwT7iSTn6Ge6rM17kbm4tl039N9KdFdq5udCNN7JMu9TnGGwoTH4ifOikgGVXxMOMj62bvfprd9yrHC83FuGUP_CHFinxy2_cPoZg-qYr8SyknH9Dov4KY21i4MVTriBKmwTaHHKqfvvv3w9YsaZDNqbfcu0u9MRxefOFeXMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت داخلی اسرائیل، بن گویر :
آقای نخست‌وزیر، قوی باش و نترس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127954" target="_blank">📅 20:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127953">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: طبق برآورد ارتش، ایران به حمله در ضاحیه بیروت پاسخ نخواهد داد.دو جنگنده چهار بمب دقیق را در حمله به ضاحیه رها کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127953" target="_blank">📅 20:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127951">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز:  اگر توافق امشب امضا شود، فوراً دستور لغو محاصره دریایی ایران را خواهم داد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127951" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127950">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز:
اگر توافق امشب امضا شود، فوراً دستور لغو محاصره دریایی ایران را خواهم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127950" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127949">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ترامپ درمورد حمله اسرائیل به بیروت: واقعا من را عصبانی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127949" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127948">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
پزشکیان: من پیش‌تر هم گفته‌ام و امروز مجدداً تأکید می‌کنم که متأسفم کشورهای همسایه در معرض پیامدهای اقدامات نظامی قرار گرفته‌اند.
🔴
البته عملیات ما به پایگاه‌های آمریکا در خاک این کشورها هدف قرار داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127948" target="_blank">📅 19:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127947">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ می‌گوید از ایران خواهد خواست که در پی حملات اسرائیل به لبنان، با حملات موشکی پاسخ ندهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/127947" target="_blank">📅 19:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127946">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ پس از حمله به لبنان با نتانیاهو تماس گرفت و به او گفت: «داری چیکار می‌کنی؟!»
🔴
ترامپ به نتانیاهو گفت که هیچ حمله دیگری به لبنان انجام ندهد و هشدار داد که این حملات می‌تواند توافق را به خطر بیندازد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/127946" target="_blank">📅 19:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127945">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ پس از حمله به لبنان با نتانیاهو تماس گرفت و به او گفت: «داری چیکار می‌کنی؟!»
🔴
ترامپ به نتانیاهو گفت که هیچ حمله دیگری به لبنان انجام ندهد و هشدار داد که این حملات می‌تواند توافق را به خطر بیندازد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127945" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127944">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ به اکسیوس : ما قرار بود امروز صبح این توافق رو امضا کنیم و حمله اسرائیل به بیروت این کار رو به تأخیر انداخت
🔴
فکر می‌کنم امضا هنوز امروز کو چند ساعت آینده انجام شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127944" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127939">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کرملین: ترامپ در گفتگوی خود با پوتین، تمایل خود را برای اعمال نفوذ بر کی‌یف و شرکای اروپایی واشنگتن ابراز داشت.
🔴
پوتین و ترامپ توافق کردند که استیو ویتکاف و جرد کوشنر در آینده نزدیک دوباره به روسیه سفر کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/127939" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127937">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یه اسپویل کنم؟ جبهه منحوس پایداری بزودی دیلیت میشه. خبر دارم که میگم
😉
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127937" target="_blank">📅 19:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127936">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری/گزارشات تایید نشده از برکناری سعید جلیلی از شعام و جایگزینی باقری کنی با وی حکایت دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/127936" target="_blank">📅 19:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127935">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
فارن افرز: داشتن سلاح هسته‌ای دیگر برای جلوگیری از حملات نظامی دردناک توسط دشمنان کافی نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/127935" target="_blank">📅 19:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127934">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
پوتین با ترامپ صحبت کرد و تولد ۸۰ سالگیش رو تبریک گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127934" target="_blank">📅 19:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127933">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر بازشدن پناهگاه‌ها در سراسر کشور اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127933" target="_blank">📅 19:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127932">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس اخیر با رئیس‌جمهور ترامپ گفت که اسرائیل با عقب‌نشینی کامل از جنوب لبنان، از جمله پنج نقطه‌ای که در حال حاضر توسط نیروهای دفاعی اسرائیل (IDF) در اختیار است، موافقت نخواهد کرد، طبق گزارش معاریو.
🔴
نتانیاهو همچنین عقب‌نشینی از خاک سوریه را که اسرائیل از زمان سقوط بشار اسد اشغال کرده است، رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/127932" target="_blank">📅 19:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127931">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به نقل از منابع: جلسه امروز کابینه امنیتی به دلیل نگرانی از شلیک موشک از سوی ایران در یک پناهگاه مستحکم برگزار خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127931" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
طبق گزارش منتشر شده کانال ۱۲ جلسه کابینه اسرائیل در امنیتی ترین مقر اسرائیل برگزار شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127930" target="_blank">📅 19:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMAC0kZLwGleNrGTAnqeb-Dus4AfgxNkpxudsriw-XM_tP87kzFGy-V8VTSAeo2wBCEiR9Ed_aJAfQxECPMDyIoDSLKoiMVE295Fz0yuxjUoedlkUlxTGYjaVrNgtwDuJdfE0y35NPu8hZvkhWsh9AWgTbueM-ESAXu8PyO73Rmgw0IIxW5cjVXJgUI4h6gf-Tumka7tSRGQvgAajrRR4dYl018XN3cAk71eJ49N7Vlhe2WQ8q561adegaTuY3xBLZlsTj9jKE6GhzGMkCNZnQc5PqVY43293q8s-1J9-fVcbKYnZLb7Lz-8nFCXyJBlM74k48A5kWD-i157mzJF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سید مجید موسوی
:
گوش به فرمان ولایت باشید و از هر کلامی که اتحاد مقدس شما را به خطر می‌اندازد دوری نمایید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/127929" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا به شدت به ایران فشار میاورد که پاسخی ندهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127928" target="_blank">📅 19:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127927">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کابینه امنیتی اسرائیل امشب در مکانی مخفی تشکیل جلسه خواهد داد به گزارش یدیعوت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/127927" target="_blank">📅 19:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127923">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShaFDWDTA1zfdbkp9tCwTjfDqK_pOhtwvDoPIhqQeWLkpbsAaEP-R01Df6uBzBGNPlZfyMOECRodt0JJARawY8j3Iv6FLbwwhY-jJ6Rrt8cA9NL0p0JtUiiX_xrxFnL7tRHneKB4UklIKEi4GpTbKhPy8_XS1R3k2KxGOsCF90rZdWj4m3cxnyZOdM9B6aTv_IqqWiTsrfmnrc_Eg8S9gETEkmISJKKGkBGZebUYNpPn6rhfvS7GVk8PTcdDDqUyGiCgVbyvtaFGpnkq6u1WtEbTSSxmdSXO1mek-bHewGaAkmIfztBlW-yPmwWejDm3pghHHXSkks7I2ULLIIglyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VR1H7cvoX2tM2kXbrTWT1eb8tfhLy785-J1bWboXXWMTfdhTd3YUjl3y7Ch_Z722zDcJuMGFrwNGhSoJtHnp9tJBp-GgnolPNBNPkkNb1UzEIsxkJjNLMpsAuaiZ08NYtNVE_mNzNwtpBtnelCf7-vjPj_fo1ZzUf7UNVzRK__AXvesK5eZckt01D_UTPEK4R_Z8olY0FHyt7sQACYumGWFQnjPnA5OH-P64tIeLgm5XJROjse-97QNuuHsToYGOn6UIXK9ppcT48fPsKbmnlhlnucNY7rB0ooGl9lxLb2zcbTExO0ypMSBAf5Iq3dduKEHLxb4JiVbzck9v87qSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAoR2ZDAKDPBBaafN36t4QQncq8nNf5Km59ODNmqN99C530dyR8Vxl7fvbx0wMRbO3vhHsM0OLBMDGZSHB5k_WrrlPl74X-rcjzqlz3T3fdMAEd5g6JUOJB1sxwHS7l-255NE3dI0Ux47F8ddmAEBu-AiNyyEXGV20Y1R1uDK0DkpmXJmT8I_rkb6DwA83sPimIUJQUsnMpgcUYV66ZSeOfJnkQgIBsOUVeK5xaRJpY2lMk5kex9j-RF0Xs5l9vPDxiALmQ5EKODVQSK25tRorgaDof35M8rUZO7R3lJBHAdXnrXzMZs91PvJTR0HRLqH4qnEdodhau87U-FZHA1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKzNBnAM87SygzlHm7NhbhGH2-ZVUN-ugMIUprT23GdpKIY67Oi4CEp4BxPhY0YMVFZZVVpZ_MmjlsBqFc-NvlslA8hqHpVqCdlGWUnugF328igQyCdiy1XIkyj-bmiYYeOQ_k_Jd-56LXF-LHQDY_4HRsVeB_ye_vXV8TflyJd04bQiTlvbhOoyPWzGDhmdiuIrq9L9RpPvlj51rtql4hWndqTc2uTcZGw6BOSNGlso-nYUHyY25NQOoPhINgT2kWMKTng7ucHsni0xwxzc9_MMs8IOxB3sJgtUuaYtg59wLwhNkqRxKwswaVNk1gM6AeKt8voyxg1w1q2jhSN9pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی خود در جنوب لبنان ادامه می‌دهند، از جمله در شوکین، المنصوری و کفر صیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127923" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127922">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۴ اسرائیل، ایالات متحده در حال حاضر از طریق واسطه‌های مختلف تلاش می‌کند تا از هرگونه حمله احتمالی ایران به خاک اسرائیل جلوگیری کند.
🔴
پیامی که اسرائیل در پاسخ منتقل کرد: «اگر ایرانی‌ها به ما حمله کنند، ما به شدت و سریع پاسخ خواهیم داد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/127922" target="_blank">📅 19:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127920">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNj9ylxOxKzwLwHgn7ZqPi00EKws1LXoIKvRAIhHcMjnrjZEORUHPkhU264jBk1G01usR-yDEqYm9YvGk9CaidHJ3uv1wmtrnQS7UN4lNMXGuJuhGW-YXXL1UzAPNlgDm8XEh6DHZSaS50BZFqD2S006tPV0Y0l_Sy8A531JUdg6Te4aC-NiY-A5wRr2aAipTh41J75P3pC60ZSCf8sJwyv4iLs7x3iAofxPszgSaVtVAOiyQSxW0EzTztnp4g_B0zjYMeSQ59QwXdFqunL_B4XNfpxtvXq9pDRlbzKIpf5tHWU4W4LWbJv-4l9i0aJg8DXDTmVCjaWvaJwT_x0IdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMjhvsinhpFq_tywnCDJqjPqA-v4ZZ3cGZx4qzZpuCeVXCognrojH_8q7BzDjIzBTuuhjFSLEmJkCutVfofmTVlGGAShLLGq8xlWtM_c6WKczuYQi8vaQ53zT2OxIEYsYaPaGVGQNeGCcy9z1hmTqhvkthA4V7TowEyIJpIw8X0fpMLzQvzZ8MLoOF-ELGum_DH2EGxZzrfsOAWK4dM1wmNdMSrGGfENAhboYeOunBjk9GwEkE1m7AYDeAhykEnBB7_gsUlM86Vbi1T95lY-3fCat3uK8M3XxmTk7LrrW8a9_DOPPYSu34S7-a3R3qsIHZQvMeiCjcWdbei8cw84DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل به ساختمانی در تبنین، جنوب لبنان، دقایقی پیش هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/127920" target="_blank">📅 19:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127919">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از یک مقام آمریکایی: حمله اسرائیل به ضاحیه، تلاشی آشکار برای نابودی توافق است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127919" target="_blank">📅 19:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127918">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پزشکیان: درحالی که برخی افراد بدون آنکه آثار تورم و دشواری‌های اقتصادی را در زندگی خود لمس کنند، صرفاً به بیان شعارها و دیدگاه‌هایی می‌پردازند که هزینه‌ای برای آنان ندارد و از سوی دیگر زندگی‌های مرفه دارند و تورم به معیشت آنان لطمه نمی‌زند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127918" target="_blank">📅 19:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127917">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
واکنش پزشکیان به شایعات پیرامون استعفای وی: بنده شخصاً برای کار و تلاش و خدمتگزاری به مردم کشور هیچ تردیدی به خود راه نداده‌ام
🔴
اگر به پیش از انتخابات هم بازگردیم و این باور را داشته باشم که با آمدنم می‌توانم گره‌ای از مشکلات کشور و مردم باز کنم، قطعاً بازهم خواهم آمد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127917" target="_blank">📅 19:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127916">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/ارتش دفاعی اسرائیل گزارش داد که موشک‌های بیشتری از حزب‌الله در خاک اسرائیل، درست در جنوب مرز لبنان-اسرائیل، اصابت کرده‌اند.
🔴
اسرائیل وعده داده بود که به ازای هر حمله حزب‌الله به شمال اسرائیل، بیروت را هدف قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127916" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127915">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW6iLLNa-qxUo9Zeshxrku4ulbF36PajprtVprctxhKtxkkuUcf_RYyF51p45TCa0KTH9EadZDZM6S1tMq5zhzP_ESHpRoqDhHpj9NPii1b0-MI1Tj-74jIgwyQJAJ5ZT1qyjJIwKEyPsJfFdabn9WnoVtHY748W4IVi4OuWYqxYcUsur8ireKmVv2XIZejd2x9iCHIYJTYkvOypFDo_jMwGadjkVzCBf9qN__Sq0HseNhQVIcj70RoRNo-eLyLTGxwRRq8L5QHvv9GitwQ3VkBuhx9rutEvOG5DSsGgWp8he38UR2oGNdvALkq4C97GXNFUelks_R9scUFhw6bhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس به یک همه‌پرسی که قصد داشت جمعیت این کشور را تا سال ۲۰۵۰ به ۱۰ میلیون نفر محدود کند، رای منفی داد.
🔴
نتایج مقدماتی نشان داد که ۵۵ درصد به این پیشنهاد رای مخالف دادند و ۴۵ درصد آن را حمایت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127915" target="_blank">📅 18:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127914">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رسانه‌های عبری اعلام کردند در پی نفوذ پهپادی از جنوب لبنان، آژیرهای هشدار در شهرک اسرائیل‌نشین «عرب العرامشه» در منطقه الجلیل غربی به صدا درآمده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127914" target="_blank">📅 18:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
پزشکیان: هیچ فرد یا جریانی نباید خود را فراتر از سازوکارهای رسمی تصمیم‌گیری بداند
🔴
شورای عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127913" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127912">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
معاون رئیس‌جمهور JD Vance درباره ترامپ: من فکر می‌کنم رئیس‌جمهور ترامپ در سلامت کامل است. می‌دانید، شما می‌بینید که مردم در رسانه‌ها دائماً درباره این موضوع صحبت می‌کنند. حدس می‌زنم این فقط چیزی است که رسانه‌ها قرار است درباره‌اش صحبت کنند.
🔴
اما از آنچه من دیده‌ام، من واقعاً هرگز یک بار هم به خودم فکر نکرده‌ام که او استقامت یا انرژی لازم برای انجام این کار را ندارد.
🔴
اگر چیزی باشد، او استقامت و انرژی بیشتری نسبت به بسیاری از افراد کابینه دارد که ۳۰ سال از او جوان‌تر هستند.
🔴
و فکر می‌کنم این چیز خوبی است چون شما می‌خواهید رئیس‌جمهوری داشته باشید که قادر باشد هر روز آن سختی‌ها را تحمل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127912" target="_blank">📅 18:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پزشکیان: تصمیم‌گیری درباره جنگ و مذاکره بر عهده رهبری و شورای عالی امنیت ملی است
🔴
همه جریان‌ها باید خود را ملزم به تبعیت از تصمیمات مبتنی بر نظر رهبر عالیقدر انقلاب بدانند.
🔴
برای بنده، حفظ وحدت و انسجام جامعه از هر موضوع دیگری اهمیت بیشتری دارد. در بسیاری از موارد، با وجود امکان طرح برخی دیدگاه‌ها و مواضع، ترجیح داده‌ام از بیان آنها خودداری شود تا مبادا کوچک‌ترین آسیبی به انسجام ملی و همبستگی اجتماعی کشور وارد شود.
🔴
امروز بزرگ‌ترین چالش ما، تلاش برخی برای ایجاد گسست و شکاف در درون جامعه است؛ موضوعی که دشمن نیز دقیقاً در انتظار آن است. کسانی که خود را مدافع ولایت و رهبری می‌دانند، بیش از دیگران باید به سیاست‌ها، چارچوب‌ها و تصمیمات رسمی کشور پایبند باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127911" target="_blank">📅 18:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127910">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
پزشکیان: آنچه گاها در رسانه ملی درباره جنگ و مذاکره مطرح می‌شود، لزوماً بازتاب‌دهنده دیدگاه شورای عالی امنیت ملی، شورای عالی دفاع یا حتی رهنمودهای رهبر معظم انقلاب نیست؛ در حالی که انتظار می‌رود رسانه ملی منعکس‌کننده سیاست‌ها و رویکردهای مراجع رسمی تصمیم‌گیری کشور باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/127910" target="_blank">📅 18:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127909">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
طبق گفته مقامات چینی: یک شهروند آمریکایی به نام مین زین، طبق ادعاهای جاسوسی در چین دستگیر شد.
🔴
سخنگوی وزارت خارجه چین، لین جیان، گفت که مین زین «به طور قانونی تحت اقدامات اجباری کیفری» قرار گرفته است به دلیل سوءظن در انجام فعالیت‌های جاسوسی که امنیت ملی چین را تهدید می‌کند.
🔴
مقامات چینی جزئیات بیشتری درباره ادعاها یا تحقیقات ارائه نکردند، اما گفتند که کنسولگری عمومی ایالات متحده در گوانگژو از این پرونده مطلع شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/127909" target="_blank">📅 18:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127908">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: واشنگتن گزینه نظامی را در طول ۶۰ روز مذاکرات حفظ خواهد کرد و تا زمانی که لازم باشد فشار بر ایران را ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127908" target="_blank">📅 18:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127907">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea33d2833.mp4?token=vq3XBJ3Ym1qpDUvYi6sLd5PPn1tBPINuqWZCFN0j-b11bkktZCiezvPGS9MiUQFWyLdO-JR3aKSjkNPkqnScIoKqqugLNeN4KC8NHxG0kyJnXsLFeoWYY5zWQZtMF9sorbHwXPjg_WIGynvgPclMMNjVMGJjKxYbBN0m4iz6TI4_J9JOFc_cZem9i9W6b69jze9GIMhASXmZeQQNQse3SV2fjRWvQZZ_-fdvtRb4ZKZeDqorZ5ZHQld16MVCqvWRahd-vb_UaRJZ_WsuyISN1Dj_UWiVV2ItuXM-hh10TdQZd7VUhZfF-_HrFaupP4S4aQ3VoH4r0h_KEYTcffiI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea33d2833.mp4?token=vq3XBJ3Ym1qpDUvYi6sLd5PPn1tBPINuqWZCFN0j-b11bkktZCiezvPGS9MiUQFWyLdO-JR3aKSjkNPkqnScIoKqqugLNeN4KC8NHxG0kyJnXsLFeoWYY5zWQZtMF9sorbHwXPjg_WIGynvgPclMMNjVMGJjKxYbBN0m4iz6TI4_J9JOFc_cZem9i9W6b69jze9GIMhASXmZeQQNQse3SV2fjRWvQZZ_-fdvtRb4ZKZeDqorZ5ZHQld16MVCqvWRahd-vb_UaRJZ_WsuyISN1Dj_UWiVV2ItuXM-hh10TdQZd7VUhZfF-_HrFaupP4S4aQ3VoH4r0h_KEYTcffiI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِست : پروژه آزادی هیچ‌وقت متوقف نشده؛ ما تا حالا ۱۲۵ میلیون بشکه نفت رو از تنگه عبور دادیم، ایران هم هیچ کاری نتونست بکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127907" target="_blank">📅 18:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127906">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
هگست درباره توافق ایران: تا جایی که می‌دانم، ما در مسیر امضای توافق هستیم. مسئله این است که کی، نه اینکه آیا.
🔴
اسرائیل در پاسخ به حزب‌الله بسیار محتاط است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127906" target="_blank">📅 18:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127905">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZpLTSRLKUFNT9jQI2j1UwnQW2Wk6xIe3ybmSMBht0hfjiZyiQ1B-Ck1BIXQNq8wP1FO4qR2ucqD2u4w_XThLPW7UDjrOWb1xVJzbaOcDMtS2qn0l-u82dJQNwqHq8oDWzkd1unQrgjRyz3oJZbq3rWhJjKUWLkb6nDTnvf6zdPWQyFija1cUie2oMju1i2BOOhnkrU6wz9NrHXnTFwyb3t9WWxBUn73xSRiEtYBGvpoYXHgqCdFxILFL_yioGbQZj_1CKLCT83s7dGFZuQeurY3upImTc_HzF-OvjZv1XzmDQdzfWYBRbBSZ1uUPTj52IaW2gdGd6r9ROqTvV78UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین، زلنسکی، و رئیس‌جمهور ترامپ امروز تماس تلفنی داشتند که در آن زلنسکی تولد ترامپ را تبریک گفت، طبق گزارش RBC-اوکراین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127905" target="_blank">📅 18:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127904">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98c3eb0c0.mp4?token=pl9vWrwx1ew6E_LCmSPvTRebiK-mxWf2UWTeg2G4V251QNWwgqlwLeDl7__ucTJXflIixscu6Gclp12L3kgEgZr1NGZHQyy-Cja6nznNaT272JWIt5ZN9lYRGVQCGp_2SbmwIF_rv8jUbCYVKA2MXz0miaCZ8Rh66pK8lI478tPf3-7EkmRqOwZ6ItG0C_7DX0LLGnAFEO4ROgMS7UZsCkhyaFUa34p6UVmJi1UMUInzdTU-5VUnl7YiKRj-YIIzJcba-jK19f3MqP47DMjhPAnGeTx1GK00Jhz-8QeynbmmGH8Bupf9f9FAnsWaCrX4636rkvvdfNNfjpFg7zZEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98c3eb0c0.mp4?token=pl9vWrwx1ew6E_LCmSPvTRebiK-mxWf2UWTeg2G4V251QNWwgqlwLeDl7__ucTJXflIixscu6Gclp12L3kgEgZr1NGZHQyy-Cja6nznNaT272JWIt5ZN9lYRGVQCGp_2SbmwIF_rv8jUbCYVKA2MXz0miaCZ8Rh66pK8lI478tPf3-7EkmRqOwZ6ItG0C_7DX0LLGnAFEO4ROgMS7UZsCkhyaFUa34p6UVmJi1UMUInzdTU-5VUnl7YiKRj-YIIzJcba-jK19f3MqP47DMjhPAnGeTx1GK00Jhz-8QeynbmmGH8Bupf9f9FAnsWaCrX4636rkvvdfNNfjpFg7zZEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنان: اما الان با آن ذخایر سلاح‌ها مشکلی وجود دارد؟
🔴
پیت هگستث: خیر، چنین چیزی نیست. این داستانی ساختگی است که رسانه‌ها می‌خواهند آن را پخش کنند. ذخایر ما عالی هستند و فقط قوی‌تر می‌شوند.
🔴
برنان: شما در مقابل کنگره در این باره شهادت داده‌اید.
🔴
هگستث: لازم نیست برایم آنچه را که شهادت داده‌ام دوباره بخوانید... من حدس زدم که برخی مهمات زمان بیشتری نسبت به بقیه می‌برند. ما بیشتر از همیشه در حال ساخت هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127904" target="_blank">📅 18:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127903">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67802ef8f8.mp4?token=LQGNX5xgaX7zrD0KRZGaBtF__JsnhLuMuR8C6L_B9vnmR5Gn7Jk3gbcI2qjxbLBMB8EYtMgG1rOu-gQ5bWYkYEGkdezyMEpNIN5elNdqv0AZMwIhl06sneQKOrVTB9Fv3DYgNvcsWCRTtVPbhlypwiCoKPE8Ak5da8tMPpRTVVSbGVN5we3uoYBW7tC1QlVpjR90cnOYEFUwyhG5mHZmBjZv-XALYtwOLpyJaTMVxYWG6IaMbI2lVzgrFcgVtAhGnMOEnaZ0ayfBYk86Pv-QDvWwNxLQVO8RG7n1zsaInYgBBTf_aqKS4ZCkFAi5PSy2lKS_-q0yW6Bepx68mHlZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67802ef8f8.mp4?token=LQGNX5xgaX7zrD0KRZGaBtF__JsnhLuMuR8C6L_B9vnmR5Gn7Jk3gbcI2qjxbLBMB8EYtMgG1rOu-gQ5bWYkYEGkdezyMEpNIN5elNdqv0AZMwIhl06sneQKOrVTB9Fv3DYgNvcsWCRTtVPbhlypwiCoKPE8Ak5da8tMPpRTVVSbGVN5we3uoYBW7tC1QlVpjR90cnOYEFUwyhG5mHZmBjZv-XALYtwOLpyJaTMVxYWG6IaMbI2lVzgrFcgVtAhGnMOEnaZ0ayfBYk86Pv-QDvWwNxLQVO8RG7n1zsaInYgBBTf_aqKS4ZCkFAi5PSy2lKS_-q0yW6Bepx68mHlZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برنان: با توجه به اینکه ارتش آمریکا همین حالا این عملیات را در ونزوئلا انجام داده است، آیا آمریکایی‌ها باید بفهمند که آمریکا همچنان از نظر نظامی در آنجا حضور خواهد داشت؟ آیا باید انتظار عملیات مشابهی در جاهایی مانند اکوادور و گواتمالا را داشته باشند؟
🔴
پیت هگست: بله، باید اینطور باشد. این یک تقویت شگفت‌انگیز از «دکترین دونرو» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127903" target="_blank">📅 18:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127902">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e835a4772c.mp4?token=JtT5zQm9ERAUB1h84lBgroBlkgk3uZpHw8jXUkPC5heFTBpiZWAPLLnJFsrE6GIR8diuFYkSOyPeei9MRttrHmGiM-IvXAPUlyyDYMXSddhe9gpw1g1SI67pROVv_Mrkj9CSHWAHQu3fZHQst_j7EjFVvKYAPs2XiSuxkHw36D4WbyweTLoWfOt5nDP03JAYakLEN9e_zUpftQ8qYY1R8_t-mzb7pHIF1QrnV91A44xGGSooaNSEaZOz2YVZ9Fb3akrslXmXJWQkffZpj6CfpBXc2VivgWF9T1yreSim7BXM-HnHGH3KEglTMVHTkGlz5kEfhiV1UWJ5DZVS29fOTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e835a4772c.mp4?token=JtT5zQm9ERAUB1h84lBgroBlkgk3uZpHw8jXUkPC5heFTBpiZWAPLLnJFsrE6GIR8diuFYkSOyPeei9MRttrHmGiM-IvXAPUlyyDYMXSddhe9gpw1g1SI67pROVv_Mrkj9CSHWAHQu3fZHQst_j7EjFVvKYAPs2XiSuxkHw36D4WbyweTLoWfOt5nDP03JAYakLEN9e_zUpftQ8qYY1R8_t-mzb7pHIF1QrnV91A44xGGSooaNSEaZOz2YVZ9Fb3akrslXmXJWQkffZpj6CfpBXc2VivgWF9T1yreSim7BXM-HnHGH3KEglTMVHTkGlz5kEfhiV1UWJ5DZVS29fOTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: به خاطر دوراندیشی رئیس‌جمهور ترامپ، ما در داخل کشور به استقلال انرژی دست یافته‌ایم.
🔴
برنان: قیمت انرژی در حال حاضر نسبتاً بالاست، بنابراین نمی‌دانم این استقلال چقدر به مردم در پمپ بنزین کمک می‌کند.
🔴
هگستث: قیمت‌ها در حال کاهش است و شما این را دیده‌اید. هه هه هه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/127902" target="_blank">📅 18:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127901">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3db14adb.mp4?token=tsZB8WJFVREOezmgWeisUJ_Tf50LxcqlVAu8fzZRdlEzTibZwSxYlGrN9sOaLNobRLgeyxRSVf50GTF38R2EKlWiTVbXFFOgju2DNAtZr64_gIZw2LXRN8am6phQvjuEQjWc01l6GxlqBo4Fgxb_LlsYNrqurzNRoNC9cnU17x5z9DiLEF6Wij_NvuL_K_jegzevVjTdejOF-Apkx-hhMxcMLcBiCiAlmGvG1BSQK1fOMPKvxvnW8FB0R2gNffV17obZ0rycpfZCCuTtsc04T7N3043aBgGTmYvd45_71e5ZQ1xvnaoLRzd155AsaXUWwDehJ79WyZu7QjlxBcgnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3db14adb.mp4?token=tsZB8WJFVREOezmgWeisUJ_Tf50LxcqlVAu8fzZRdlEzTibZwSxYlGrN9sOaLNobRLgeyxRSVf50GTF38R2EKlWiTVbXFFOgju2DNAtZr64_gIZw2LXRN8am6phQvjuEQjWc01l6GxlqBo4Fgxb_LlsYNrqurzNRoNC9cnU17x5z9DiLEF6Wij_NvuL_K_jegzevVjTdejOF-Apkx-hhMxcMLcBiCiAlmGvG1BSQK1fOMPKvxvnW8FB0R2gNffV17obZ0rycpfZCCuTtsc04T7N3043aBgGTmYvd45_71e5ZQ1xvnaoLRzd155AsaXUWwDehJ79WyZu7QjlxBcgnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: این قدرت رئیس‌جمهور ترامپ بود که ایران را به این توافق واداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/127901" target="_blank">📅 18:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127900">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852e5d3abd.mp4?token=pufhHWsCjHKt3ujAcbqCdmO11A7EdiaOXS354J_TdZx4E6jPQftVF1Ao3A-iDYysm6dgeWgV2j7eZ_9-aZywBXqyivYV5TNCfFbY_HRGqjyumnXLySN8C6_kNeRUCEWY5IXfBFDhLktpL2qa2vh3dPZ85KmzJXoFJqFRYStXSLC7RvFd-OKILdehnves6JTryACTNJr_vamB5wkuaIUMn6TQF9BQAhiDzY0VMTUTW3I4nOgYGBo6bCv9HJ6WNfArJXHlU0eHYK_kbYQwHblGy-XUzBLoEf-SZfP14pgIyxAdZShjZmAl50DO8uFbn4wo9OXQkVh9NQlg6Utdp1UZwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852e5d3abd.mp4?token=pufhHWsCjHKt3ujAcbqCdmO11A7EdiaOXS354J_TdZx4E6jPQftVF1Ao3A-iDYysm6dgeWgV2j7eZ_9-aZywBXqyivYV5TNCfFbY_HRGqjyumnXLySN8C6_kNeRUCEWY5IXfBFDhLktpL2qa2vh3dPZ85KmzJXoFJqFRYStXSLC7RvFd-OKILdehnves6JTryACTNJr_vamB5wkuaIUMn6TQF9BQAhiDzY0VMTUTW3I4nOgYGBo6bCv9HJ6WNfArJXHlU0eHYK_kbYQwHblGy-XUzBLoEf-SZfP14pgIyxAdZShjZmAl50DO8uFbn4wo9OXQkVh9NQlg6Utdp1UZwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: ایران نمی‌تواند قابلیت‌های خود را در اطراف تنگه ببیند و درک کند، به‌ویژه در چند شب گذشته که برای آن‌ها بسیار ویرانگر بود از نظر توانایی‌شان در فهمیدن آنچه در تنگه می‌گذرد.
🔴
وقتی این توافق امضا شود، انتظار ما این است که ایران شلیک پهپاد به کشتی‌های تجاری را متوقف کند.
🔴
برنان: آن‌ها همین کار را جمعه گذشته انجام دادند. یک پهپاد هفته گذشته با یک هلیکوپتر آپاچی برخورد کرد. آن‌ها هنوز توانایی آسیب رساندن به دوستان و شرکای ما را دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/127900" target="_blank">📅 18:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127899">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf1af4a34.mp4?token=NTf8b0RQrDjJLTPC3-DjkX_dsIo8s14Od9bNg1nZ0JIe2OUeA7U0RAQJ0iR3dk9cOz7cu9qQZyon1mmGvf5nVvF1RYAZ75fpEkDCDddjYqSCXy-UsStD6XmXGTb0yGa8tbGvzvZCWfOE2YMzoO78b_zrwg92up1k1_lp1vxyAHnXwKnEpe_nmR0sP8oti6NxiZtKINt8Tyn63y3W_2u3SyW8dOzoCg3gxfgVsYcEfzmDX5lNvAWKZqMpv789bDEZyFAJw15O-xT5A_AcYRZsE1BSKDEs3uS26WF1ds0vxt8xGglyUBSlqer7p8F6dW0Qrhx6xoTx31arNDiXLdXEsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf1af4a34.mp4?token=NTf8b0RQrDjJLTPC3-DjkX_dsIo8s14Od9bNg1nZ0JIe2OUeA7U0RAQJ0iR3dk9cOz7cu9qQZyon1mmGvf5nVvF1RYAZ75fpEkDCDddjYqSCXy-UsStD6XmXGTb0yGa8tbGvzvZCWfOE2YMzoO78b_zrwg92up1k1_lp1vxyAHnXwKnEpe_nmR0sP8oti6NxiZtKINt8Tyn63y3W_2u3SyW8dOzoCg3gxfgVsYcEfzmDX5lNvAWKZqMpv789bDEZyFAJw15O-xT5A_AcYRZsE1BSKDEs3uS26WF1ds0vxt8xGglyUBSlqer7p8F6dW0Qrhx6xoTx31arNDiXLdXEsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگِستِ : ما کل این مدت کنترل تنگه‌ها رو دستمون داشتیم
🔴
مجری : پس چرا دارید باهاشون مذاکره می‌کنید که دوباره بازش کنن؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/127899" target="_blank">📅 18:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127898">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGxBROaSd_JFd82pxWGlFEL0T2Ka4zllF53L4Fm4k7RD2_6Mx3ERCYay-gazCgjNSGZdH0txS6yQauM2OLFeJzAexfnG8QxewbPoygHx-c4h7obmFpCeh9Fn6BirWkPrweRKP5IKRjcgZ-9E87mNZVSKNElSwBvcaUffJPDAe9Y2YfI9jKoeKtvGc7AP7PP6FSyvuvUJobh0NwmXyQIBIlPGPQXge2_Ib2UQayeGK1jQn3WSl5gklogkwPg848AajknaznJ5wmhhxv9Qa9TkMnpDFrjrBM0IRap8gx595aPfXXIqSs__mu-Mldyo2K1QamIdbnXVvyDzzXWWlHum8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
ترامپ: حمله صبح امروز به بیروت نباید اتفاق می افتاد، به ویژه در روز خاصی که ما به توافق صلح با ایران بسیار نزدیک هستیم.
🔴
اسرائیل حق دارد از خود دفاع کند، اما حمله ای که به آن پاسخ داد بسیار کوچک و بی معنی بود، کسی آسیب ندید، مجروح یا کشته نشد و نباید این روند مهم را مختل کند.
🔴
دیگر نباید در هیچ کجای لبنان حملاتی از سوی اسرائیل انجام شود، اما همچنین نباید از سوی هیچ طرف دیگری از جمله حزب الله علیه اسرائیل حمله شود.
🔴
این می تواند آغاز یک صلح طولانی و زیبا باشد - بیایید آن را منفجر نکنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/127898" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127897">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1126f6794e.mp4?token=lMA23SWv88--wfceEYqK_ZdnuangkZdpOl3OnBXyk4YW6Gba6SSxEiGpZTv1cZGYeQ5yB8swzg0543lZNCavCDtZ0oeVnJIuZHbmf623XM8MZOQggoaWimuQ17twlXhfd6PHA3q176a7KM5lXX87q13TsoxzgcsHlB2RFMbZ4BMfBDW8bRNFTRVHRJwhUJNG37mP-tyxGJb04UrSV2kG0KIGcrGUGG-PVt2P8uj5Z4AMWK8s07zWvSLmNUk1ahZkbI3SFtZEY2RihtatzpXCExg7lHrNUHHtNkHGmrwymqL3VS-wfP4wWayjNztYxSxrJwdGCFVCM_sKI-5dBIz5hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1126f6794e.mp4?token=lMA23SWv88--wfceEYqK_ZdnuangkZdpOl3OnBXyk4YW6Gba6SSxEiGpZTv1cZGYeQ5yB8swzg0543lZNCavCDtZ0oeVnJIuZHbmf623XM8MZOQggoaWimuQ17twlXhfd6PHA3q176a7KM5lXX87q13TsoxzgcsHlB2RFMbZ4BMfBDW8bRNFTRVHRJwhUJNG37mP-tyxGJb04UrSV2kG0KIGcrGUGG-PVt2P8uj5Z4AMWK8s07zWvSLmNUk1ahZkbI3SFtZEY2RihtatzpXCExg7lHrNUHHtNkHGmrwymqL3VS-wfP4wWayjNztYxSxrJwdGCFVCM_sKI-5dBIz5hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر جنگ، هگِستِ : برخلاف اوباما، رئیس‌جمهور ترامپ تو این چیزا باهوشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/127897" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127896">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb30e70b3.mp4?token=ftc2R1zZXh31aR2s0WUlZLUBcfPQZzcr6-48xJhVg3uXPionMWiOc7tNIIbm4hf48VCWPvWXLbQFqmEO-D9WWog9DeRiNbKtpsa2VKjSnXlsW1rteVb7YY7Vph2K8d3Zb6sbTcjdk5DdcXaCpQBx-O00G3UXQiQlZhcbSMoqVboEINzUuKuyZ_YIt7qGAAmKKlFFDrcvF7nkAjaCPaTzf4fW66XV3WS2OJad8d6kiUWvKCoXlKJ0ROq-l2wQZNkqpwxTR-RLIbPZDG0VMALlQxqulV0xDTmBLObtpp-mrDiOo2QUYntvR80tRq5Al04JM3VOweKD3IiuNzN_6BY8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb30e70b3.mp4?token=ftc2R1zZXh31aR2s0WUlZLUBcfPQZzcr6-48xJhVg3uXPionMWiOc7tNIIbm4hf48VCWPvWXLbQFqmEO-D9WWog9DeRiNbKtpsa2VKjSnXlsW1rteVb7YY7Vph2K8d3Zb6sbTcjdk5DdcXaCpQBx-O00G3UXQiQlZhcbSMoqVboEINzUuKuyZ_YIt7qGAAmKKlFFDrcvF7nkAjaCPaTzf4fW66XV3WS2OJad8d6kiUWvKCoXlKJ0ROq-l2wQZNkqpwxTR-RLIbPZDG0VMALlQxqulV0xDTmBLObtpp-mrDiOo2QUYntvR80tRq5Al04JM3VOweKD3IiuNzN_6BY8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران:
من فکر می‌کنم رئیس‌جمهور ترامپ هم همین‌طور است. فکر می‌کنم هر دوی ما عموماً نسبت به درگیری‌های نظامی خارجی شکاک هستیم.
🔴
اما اساساً، این به این معنا نیست که هرگز نمی‌توان از نیروی نظامی استفاده کرد، و من فکر می‌کنم هدف اینجا جلوگیری از داشتن سلاح هسته‌ای توسط ایرانی‌ها است—ما در رسیدن به این هدف موفق خواهیم بود—و وقتی موفق شویم، این نتیجه‌ای بسیار خوب برای مردم آمریکا خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/127896" target="_blank">📅 18:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127895">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
هم دفنش نکردن
🔴
هم ۱۰۰ شب تو خیابونا عروسی گرفتن
🔴
هم با قاتلش توافق کردن
🤔
هرچه از حرام زاده بودن عرزشی ها گفته بشه کمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/127895" target="_blank">📅 18:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127894">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مقام ارشد اسرائیلی به کان:
حمله ایران اکنون قریب‌الوقوع به نظر می‌رسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/127894" target="_blank">📅 18:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127893">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هگست وزیر جنگ آمریکا: من انتظار ندارم که حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران شود. اگر ایران می‌خواهد این موضوع ادامه پیدا کند، باید حزب‌الله را مهار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/127893" target="_blank">📅 18:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127892">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6c0f0321.mp4?token=EqtEKpChLfyfCIiKVeIuQXxOVCd4sgizHgCPb0VFtceJv3kg57eDpT4bid6Qt3hv5Hn26dMf12EESrGKLPt-05SlG4aSqhBzX-g3WUGvvixVL_NPC5V1RAccJ1gEYvS_rhfpmeyLZBVGj9A_01Eo_gj6jBgfzgbZnB7YimqyI208enfySeS66XTEdmScyspcsjh8zetMN4GltOGI1jmvY8TBKKmrFw4s9mmNY1f4l4y9t3ZmprfsWvnau8XJlOWxRDK2-qXH-yXMLyyqDQvOgqOlxNZa-p-W_nYQTtq3VhaUvrbZ6uEb8vo_dk-d-WINQpYkxLSV6m9f54YZfNU8sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6c0f0321.mp4?token=EqtEKpChLfyfCIiKVeIuQXxOVCd4sgizHgCPb0VFtceJv3kg57eDpT4bid6Qt3hv5Hn26dMf12EESrGKLPt-05SlG4aSqhBzX-g3WUGvvixVL_NPC5V1RAccJ1gEYvS_rhfpmeyLZBVGj9A_01Eo_gj6jBgfzgbZnB7YimqyI208enfySeS66XTEdmScyspcsjh8zetMN4GltOGI1jmvY8TBKKmrFw4s9mmNY1f4l4y9t3ZmprfsWvnau8XJlOWxRDK2-qXH-yXMLyyqDQvOgqOlxNZa-p-W_nYQTtq3VhaUvrbZ6uEb8vo_dk-d-WINQpYkxLSV6m9f54YZfNU8sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، نماینده دولت آمریکا در سازمان ملل با اطمینان اعلام کرد که امروز توافق میان ایران و آمریکا امضا خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127892" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127891">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مهاجرانی، سخنگوی دولت:تصمیم‌گیری درباره تفاهم احتمالی با آمریکا در سطح «نظام و حاکمیت» انجام می‌شه و حمله به مذاکره‌کنندگان، حمله به یک «تصمیم ملیه».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/127891" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127890">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edV84_3o6K6Lqd-pYk9BImb7oAc3aTGPkmgtgZz_unbxUW9VBSlchz-qSlT6zHpBcdS-QFs2zGtVxCr63BO6f9zDWjn4MdHwUwGMNjOwbfhS13uAin5puInIqzNYkxCeD88beC9QQlfwKg6Nk9ZIbLImuHI6BwsjZKJm75gLdxZp3qtmJhyAbKpQq4-srxHjt2q7_vpBkRtcejWRuW-xNtMeDn2YEdl3kmLE-_Mh1lZz3eMAkhC2U-AuePDhIHZwXibo2VrZYvph8N27b_BgpAiB4k3FJBmeZA-q-bojWmigloJzk6mRf5j-azg32k1bQhF3wFpMnRYr86exavx33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده درحال اعزام به تجمع پایداری‌ها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/127890" target="_blank">📅 18:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127889">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4897b39440.mp4?token=HbIO7imkpr0Q3hxKeFicKs0lwfw-p1Yy3FOL4MoRBDe6ccIhq-YlsJJu58A-O_0r228S1SmWzhY8m0z0Gy84klcsqlbSa7A3k66JRfJbq_9GtNFatpN95aL4WD0tctgyNA2pJxXh2do_frTWX9U0vB5-Su56l-tEkswtbUMxpnG11PBKpl26NjdIWWTcmA5q--Z_eYjH-AE44wOnq2e-VtE6NQ5AOeBP8srTEBoCUrDPmY2zQMmquWPCbYM6eGuO14XgI-Ji51CKztpmG_BdrLUzu5Eigt0EXAh5_yF_osJihpgb6fBvu9vANnu8DP_hLCvTUrf8ItQP1gw97rRFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4897b39440.mp4?token=HbIO7imkpr0Q3hxKeFicKs0lwfw-p1Yy3FOL4MoRBDe6ccIhq-YlsJJu58A-O_0r228S1SmWzhY8m0z0Gy84klcsqlbSa7A3k66JRfJbq_9GtNFatpN95aL4WD0tctgyNA2pJxXh2do_frTWX9U0vB5-Su56l-tEkswtbUMxpnG11PBKpl26NjdIWWTcmA5q--Z_eYjH-AE44wOnq2e-VtE6NQ5AOeBP8srTEBoCUrDPmY2zQMmquWPCbYM6eGuO14XgI-Ji51CKztpmG_BdrLUzu5Eigt0EXAh5_yF_osJihpgb6fBvu9vANnu8DP_hLCvTUrf8ItQP1gw97rRFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلیپی از یه حامی حکومت:
آقای عراقچی شما گوه میخوری وقتی رهبر چیزی نگفته حرف از مذاکره میزنی.
اگه می‌خواین مذاکره کنین اول باید خون منو بریزین، خون آقامون هنوز خشک نشده، بیجا میکنی مذاکره کردی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/127889" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127888">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: ما برای احتمال شلیک به خاک اسرائیل در ساعات آینده آماده می‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/127888" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127887">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کانال 15 اسرائیل:
تمام سامانه های پدافندی در اسرائیل به حالت آماده باش کامل درآمدند و در انتظار پرتاب موشک قریب‌الوقوع از سمت ایران می‌باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/127887" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127886">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کانال 14 اسرائیل:
اسرائیل ارزیابی میکنه که ایران در واکنش به حمله در حومه جنوبی بیروت، حمله موشکی به خاک اسرائیل انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/127886" target="_blank">📅 17:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127885">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4ke6bRyit4zySsM_j35rotxhtIes6HEcx_hcXbgfECHMoE5R_KB103_L3NyAeRlhIvJPUtKCs7OJeYeJS5NakTQtTTYm2vu7xdRZ6OH_-OAReepXXK7xb3jkHsKhvqk7t3d2gWcWpY4Nz1zvwM0mxmFAuwE-X3_7ZC6iZvh3xmaqLm-b8fdhvQdBhYBm-7_hp4CaBm_HBt8lpJ98bn4Wukbv3vVWPGdh2eHjXvXpUC5IHM3dss09C8Fu0KajYq0nQoT6tJ09SVjaWs-GkdpGrGTAnAav9rJ24-w05vp1NVH50V0LIrh1vQtvmFroQl6dSL5mWk-OENHVps-SM7utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/127885" target="_blank">📅 17:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127884">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arVRmMQfyetj_rINgQFpt3eF6zkUF7q7ShGbbCX-74POuWJ-1Igiqpg36hO4Tz_uzH9I-27W32Pvx6icVe9J5oU3WQ_sX_kkFhxGpiCFi35INlllZDNuWM5CPF-7EcA1zS-SyEQbFLbmaO_L8jmawi4CbdZBKD9ByqT3OgCHWPcUIRAYMEHmwEXcHyrwCJmLzWrq8UrzGY13BMH8yuB_DXDL5KPYI44-E64sz9bVIDAJyc3aA3uktnOpmGVmsmS53mKR5l53rvX6ifUXMaB_8amsQ8FXI-94gzzENiW5CYIfaWYQMrw7JbKp4_6te6jGxfP-ZJJ_eQuxYQYdH8nyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره:
بر اساس آنچه چند روز پیش نوشتم، و با توجه به ابعاد تازه لبنان، افزایش مخالفت‌ها در داخل ایران با توافق، تردیدهای مداوم در مورد تعهد واشنگتن به تعهداتش، تغییر مواضع دونالد ترامپ هر روز و اصرار اسرائیل بر شرایط غیرممکن خود، هرگونه توافقی بین واشنگتن و تهران بیشتر شبیه یک سراب است.
🔴
در دوردست‌ها به نظر می‌رسد و نشان می‌دهد که رسیدن به آن فقط مسئله زمان است. سپس محو می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/127884" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127882">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
تتر هم اکنون 173000تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/127882" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127881">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
الحدث به نقل از منابع:
علی الحاج، فرمانده حزب‌الله، در حمله هوایی اسرائیل به حومه بیروت ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127881" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127880">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJN7fTNj6_LrXIxSZqfHGoqjJe0wcRCiNpCVO_iwYoIV6bjXX1v322DvCHlS3o7Kr3PuLxJ3jB2vTGAOHKl2rXxZlyFm1XkPWFgCeq5e3G4QI2Ni3vHR_ryJjA3n0KCSNOJUYdUrj_b1Txdd9XAic04bzzl7kRGYcGmKb9mVjRKec_BauN2BHURfUG-Aowb08jbq5Xh5BwFN2Z-QJv7Hgicv17nqduTQsUASL_CNjp5jZIUtcRLd0itDNzuGRI8zpMzEw_M7fa6OQ0KK3XQOUBs74lWba1IWCu7mnzBzN2IGjdWLOqCI49-oJ4oyo6WbKz2LZxrlOhYlDv-pxPV4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل: هدف حمله نعیم قاسم نبود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/127880" target="_blank">📅 16:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127879">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/127879" target="_blank">📅 16:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127878">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی: https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی: @exovpn_dl</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/127878" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127877">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJpfX3NkWBA4fC2ve-FabP80YoGtVn1xsw5I6TUVctPhE5_VjS_eHKeRVzhKqh5T2ZWmBLnEGwjWwYPB_khfjWDlkrWoSXGw1Nrv6PCJCq1TBncrj7AqewgpjztIPFdA1tr2Gz5ZHk_wtp6N_1UI6JONVLUkC0OT-QfB80GytF0lSAbBaX-VH04ZYgTZ11prQCIE27mB4FiKwAYCQ9O_-Z29UNL1kOi4DJzUWNkAXTxqXIHZqubk_Sbbyt2bmWZL3aYqS5nCdG2Zk2ibyzyhdOdWepFpFjYTog7njiyUbBbnAfnLhp15Oym2P277B0kCLK5SDgtLjsf0SHFlrWgRoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Exo VPN | سریع، پایدار و بدون تبلیغات
✅
اتصال سریع و پایدار
✅
سرورهای متعدد جهانی
✅
حفظ حریم خصوصی
✅
کاملاً رایگان و بدون تبلیغات
📌
دانلود از گوگل پلی:
https://play.google.com/store/apps/details?id=exo.vpn.app
📣
کانال رسمی:
@exovpn_dl</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/127877" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f5b803eb5.mp4?token=qIFEcSF0uDvQuSd9weFiyjwr_IBx_fMI41KqUQ_J558hHBBsyoki86trafRQEka0Sv0y9tScpfxvTDyWuFtlXhFVkDtBNg5vhbLWIDi5mF_EfNZIcVcLhHeLP1zSuevWKC_ywbNJY_MHDyYyxYPXp8U15hoY1Hlf6ui3evZwaK0IQwwY-hT9_Y4hpAdaqTOAsnDOFeBCZ9ng0JAOtMbnT15AUgmiCT0jAEBug3R8lXy3HaOjnpqzwFvTQ6hcO8HUv5_YYgHVrnZEIOHmhetJUJPpKicVWgsXun8wegRzmIkwn8ixQQiTHhewAh1DqhOZdo-_Ki90XCW4-f-MeYD3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f5b803eb5.mp4?token=qIFEcSF0uDvQuSd9weFiyjwr_IBx_fMI41KqUQ_J558hHBBsyoki86trafRQEka0Sv0y9tScpfxvTDyWuFtlXhFVkDtBNg5vhbLWIDi5mF_EfNZIcVcLhHeLP1zSuevWKC_ywbNJY_MHDyYyxYPXp8U15hoY1Hlf6ui3evZwaK0IQwwY-hT9_Y4hpAdaqTOAsnDOFeBCZ9ng0JAOtMbnT15AUgmiCT0jAEBug3R8lXy3HaOjnpqzwFvTQ6hcO8HUv5_YYgHVrnZEIOHmhetJUJPpKicVWgsXun8wegRzmIkwn8ixQQiTHhewAh1DqhOZdo-_Ki90XCW4-f-MeYD3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو دیده نشده از هوچی گری دیشب تندروها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/127876" target="_blank">📅 16:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127875">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70115bf6a8.mp4?token=f-6AG2gaf4Mf7Zf3kBoLjhX7XuOAesr3Ii3pTzho7hNgBcyA9DA7Xl_YTpwVWxyO5EEBv52EyiTKjkE87dtCn29vUNjLPifbVFKUF5P95bvETbCsItg5AUzAw7WIX0T8yr7OfdXKYEBz2yFhbRKJ3g2E7yEBkNMffJYGMbDMmFAy2FWomt851VUDXIqVShmVzc0kElTX322A0ZXGSzoXW8SmfR-A5MkicVsgTJPWlcIBpHh3VCGOV0LG8-vXKn_Vy0xsNCpBDAmbx504SB4gF1SiLme1Qt2P1N8vc85vsdc1rrl2xG3roeaRX1v-u3-u7vuE5Rf1_FDT41qjWBaziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70115bf6a8.mp4?token=f-6AG2gaf4Mf7Zf3kBoLjhX7XuOAesr3Ii3pTzho7hNgBcyA9DA7Xl_YTpwVWxyO5EEBv52EyiTKjkE87dtCn29vUNjLPifbVFKUF5P95bvETbCsItg5AUzAw7WIX0T8yr7OfdXKYEBz2yFhbRKJ3g2E7yEBkNMffJYGMbDMmFAy2FWomt851VUDXIqVShmVzc0kElTX322A0ZXGSzoXW8SmfR-A5MkicVsgTJPWlcIBpHh3VCGOV0LG8-vXKn_Vy0xsNCpBDAmbx504SB4gF1SiLme1Qt2P1N8vc85vsdc1rrl2xG3roeaRX1v-u3-u7vuE5Rf1_FDT41qjWBaziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تولد ترامپ
/
حرکات نمایشی موتوکراس در چمن جنوبی کاخ سفید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/127875" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127873">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrlFZYps6lGAaExTXYvFLrQnErns84Nn1VK80scC-0KCl2V5H6m5ja-LbBDv-PZHg64AGg36UC5_mRSBIRfJhlfYbhiG1rJ1lHFk5tG6YGobr0Grg0rKnilhfQJwj41FYzOprjL9qo8qmssw3KOwNBV51nETqMrx-gXKLJYHsNXWo-xYkpPn2fvN-zG71Q0ZWsI0M7Ic6Q-DwBR3I5HwBnv9JRsT4UOLKLsaFEhd-ZoW45GPdLPXVxPTGc0BHAvxFhgVbgZej8_KziaT1zew7JfuHaqtw2Z0to9z3-B05Ne-6U9AryGAIgbe1JOuWlNIoX8X1dzCB60Ad8cmo6BpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BtFPz5RgIzu_BTIfxR7adYSse7SvTDjkVbYN1ypTZjPbkdGfFKnFStICqz65TRkxHv2uUGqgfYwFwT1h7U5hayyz6XpEHnvguSp-4XTSnvTw48zDoSronW-dVSjQUjHUkQm3DvwtvOYlkomK9tquyD4Mw6gTvT_ogDJaWFmX8xx9K9syIJVcz-3W6XsTaEI4dG-zkIuMilt_AWZaGmMjpYGkA4hpWyZ9XFCGhPPxPenMzIZUcwB9KfeQTBavER2JZn5L-uNoKJ6aeEmqCVraZXAQqp9uFIYzMN1K5_dBbxWSqBM7Mp3AgeMu59DOdmRNKlBJFCHtOayxCFHM58dE4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نتانیاهو ابتدا تصویر حمله به بیروت را منتشر کرد و در پست بعد تولد ترامپ را تبریک گفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127873" target="_blank">📅 16:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127872">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rk_0s3evC2TtKu7YJfFL9kOQ24-zmpqFnLxmhI-gk1kX-8ftM3ridNPE3SWVpDtDzFSHmMTm_xQXR_cYPQRV9r_fMpo-LoLjAFfdgTlfSnvtQUVCu_DgZvlUmzRtq3Z9rgGpk0pIbwFjuQrdSCAUQFafW1Km_0PvHFQNyrYTLrmDuEdQXGOvyns61iCaE_MPF76V-mJ-mcutkWmGIi6UnhJfZauddOHdDZ0GylR8XRdBwbE5jiKl-uhX9GwURf7z1vU_NqK4bgxAyhgM46eiVukzJtfjcIGbP03sKOuMtR80BQ3FYBrgnxHBmW19DSO7w91L_2Bxb352aObYAml75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات به لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/127872" target="_blank">📅 16:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-127871">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قرارگاه خاتم: پاسخ کوبنده میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/127871" target="_blank">📅 16:15 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
