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
<img src="https://cdn4.telesco.pe/file/oh1p4k1ORmcpfb-T79kLjgWXoe9TxSK6oQWzn5UIE8xqDLHz21VOP6S9vCgNDRfQ9v9aABqGR0i9jItlnNwuUpcvlQxhoTc6JIS94j6mUVPBMCReeGHr0Dfz5pRCaFf5jK389NO92QUSVKyqjzVEUbmjNA5IpL7WOVUvWLjgi13xXgW0kbHeXzP2dVKywidDIrs_7H07AIAcE3qmBYGqoBJt9BcTXhGPwe1lzKjjr0ewcUSuNVDJQusRlf57FoL9Pgk73_XGBShPMlz_4kC3_rM8eowwUWZm0JFuSlE1nheC1jqKcmnro8bGTmbYroOKczuk2lcPFXHdT_5M2oWPxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.54K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSWdGJ10-rC89ljCPsLTsFTFKNru3jRger5jNqLajPYWTqAWlAEb6NwUs88T-s2DYFwgEQLdOLu-3SiPG38to4bGhnUhJgfxKFKtGoZFMzWf-0XhgDp4A8U4jQ7Yq10xxRpL2iQ8K8rmeQRTxdVBMPWvxIN7vlF0ptLP7mlikm8YF1At_vkKASezqsTtFPCLLFv-0wDfZvUszVvxF_pClRPODIvnqyLZ1vhedyxmrrdULmrlDye5OhDYr9mfVfCJOwjZw8Kmo_ci7m5M2Qs1CLROOfJO9tDKlreTj6ejcdjaMGtH8wM5zINm3RoZFl3YHoAvvAHI0o70OXguRMHhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 283 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست
دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل
Fable 5
و
Mythos 5
قطع شود.
نتیجه: آنتروپیک مجبور شد این دو مدل رو
برای همه‌ی کاربرها
غیرفعال کنه تا با دستور هماهنگ بمونه.
📌
نکات مهم:
• مدل‌های ضعیف‌تر مثل
Claude Opus 4.8
دست‌نخورده موندن و کار می‌کنن.
• دستور از طرف وزیر بازرگانی (Howard Lutnick) و دفتر BIS صادر شد.
• دلیل دولت: کشف یک تکنیک دور زدن safeguardهای Fable 5.
• آنتروپیک می‌گه این jailbreak
محدود
بوده — فقط یک قابلیت خاص امنیت سایبری Mythos رو باز می‌کرده، نه شکست کامل تمام محافظ‌ها.
یعنی عملاً قوی‌ترین مدل‌های هوش مصنوعی آنتروپیک حالا فقط در دسترس آمریکایی‌هاست.
🇺🇸
@danialtaherifar</div>
<div class="tg-footer">👁️ 507 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 626 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=rVR0sbbY_JE2f2_93jis7QUikwczNwSF4rahwsrEY5XBc_3vnaNE-35hU7A_WW9hJJj2b3ASA2XquTSuypG-cfwFyi9kvFoKmzR1awu1_RXxw_xwg9f1opYKSbudW9AiZ_ffLnr024aG8INFEvPkdb62R2Qz4l4YNMEVEKIwjFy1BiBnl5yYtBLROxXJ-H6gOikCaP3zTXbjsdA_r7X07mKF_zg36URXP9sPU5bp9pfcjDDnSrPXbz8Od87hYc0xr_aZ-y8zta0QsRL-SzexHQ7HF2L-NYCuf4iAXBaGQX3xjmOd1bDBEONka3rARdVsyhCwwEBcliQGqHZx7jEXog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=rVR0sbbY_JE2f2_93jis7QUikwczNwSF4rahwsrEY5XBc_3vnaNE-35hU7A_WW9hJJj2b3ASA2XquTSuypG-cfwFyi9kvFoKmzR1awu1_RXxw_xwg9f1opYKSbudW9AiZ_ffLnr024aG8INFEvPkdb62R2Qz4l4YNMEVEKIwjFy1BiBnl5yYtBLROxXJ-H6gOikCaP3zTXbjsdA_r7X07mKF_zg36URXP9sPU5bp9pfcjDDnSrPXbz8Od87hYc0xr_aZ-y8zta0QsRL-SzexHQ7HF2L-NYCuf4iAXBaGQX3xjmOd1bDBEONka3rARdVsyhCwwEBcliQGqHZx7jEXog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2wy2f1QBQKF4ZUz6TCsm5X4FaZkagTLKU6PmsuRMsbWMnbaAo8k_Bok9NWxgnhiG-qRmNH4Sc8VvWFNr-_a9vDjABYj3sm57NMX4j_6h7RYLRlI3PKfBe-suqyrKDScsJl3RtlthrAojRx1d1LHdi1B9L3R27TVNV4vZJBKv6jPyR0Y_oj8-PU8eXie1fUusnIupncSe7ZZ8L0SeG_wg5TmvtKPmjgLbhjpJroHEVnCQkK7xw1Z654ZUAXd4ESOI9jxpdjBq6GFADgzJBUPHynSd44UbmEY_RKST8_75jM56_EL1CE09MljsZjhcEoIZ19U0coQpiLlmdaAyNpZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm1LBkdtzv-0Mta4GzzkUCd5AFDuqzDluKOelOOeeSSfqKQwbNRkGAaabKJz20g8Ay8dLwWL5iSudejSfmSnVYrv7WLsAvEi7jJ_dTZ-91-Flnz8Y0NrriPJoOeYcrhIBPgvFoafKREGd9NRsA5dhauwI6YseQHnZwSTnkVQqaeaBU8I_4e_cPMrtJM4I7fPl_iT_bISA8IqtMoQSSyRqrHEOOXb0PWhOBPMBNtotrZCeDfEyCXdCdxhkKy4RaqQipJvbnxQ_m6AfL2W5f60FRXjmVDjb9PxxHQP8ZHvFBVPrIPQPtrLK-t3E0nEzBew87U-C1Kk9wdPnDzJnnX0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXm4-sqP_kBTcKeFYL_a2pJ3KLqc3xvulM2uqPlJYc74rHTZvQCXxqgM4t541Y9l8miu6f7zwyN1oxMCkwio8Hj0f4w1zHFCEzcS7jsCk0yAd_uLrmAkH87dM1a6uMNzdb1XpL95XGpTqu2AHbiCWvOEbX6GI310L80uPGq9CSu_iZgcCwRsxQpM5ONL6arV8goGDq1nl80iwWFsjFHWOM_6xYhWnna5BgxqJnx_Duw1I06rX7nJMoTuL1M_Ra1Bl45Rpl0B-ZmeyJewQ5sxyOLnaiaXXzEJTU1BA4rFUAHmV5mLnEJyc8b7c1NprjRPUlg6e2kEoFophSAy4q7Igg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/by7mfVH3Mq62DbX5UkwuhhYA6nTUqLNW9oqLvzguB7OX2TnH2CJq2PlZK4s2XdJ63P8hrHg8xG2Hyz9sOPU_hwJyaWBw9VVBd2L1Ih9vIa4JRW-Z3geHw-7lFQPsaQ0sB5pleaNx6TzcUjVyse2PvtmEVPk1V7QobjGo7NPPjRhDfYM56usx8TdN-SWMh6raFGauRvhj5gBmEEBcWbldifKKN-0PjKTEG4cxAgYHylpn-REaSK8c8kLosXNy7pKsxTi5WzDT4QN3_O-DgGFhuGLYvkzvfLpyCW0CbR__B4hETSl7G3AslG14hXLIrrQpn2iBRuaLLWS2CRtcG8nfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0s5ynJonfxgtV_PRGf_Hz9Ftr9ndRibxYfFmt6gjVlYuS-NrxY0boTtsrLwXaytkqOqQ65s1SqjdnFI4aGchjtoI5siOL9jV1ctHhab_URtih2qdiS1bYioOBXLVPQA3uKBcuQSinZszRRfoeiToJC4GFxy0AB7sengYXH1wtl5teJHDqUdn4ekgAV9yp77sb2lGpTIiLWku0WWW7nGZ4-IKtEZkQkyuArhTxGn3bXCIb1ajIvHx_jsn3PNtroN4o72zpopTZFPqW_a4I7yPtu9bHZMADxkajyADGjv4pEXdUVoeYRdurW5Z8qK5lxJS1MUCShF3hy7aXO14eOvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czHixWkQ8_ViC3ex0M225w2BcijttePIyQbBRRQMtFf-mdqfwq8EkHqVmOiNS9nEKGm1j8vSXUHZ4juFFfCJs0OfYipCMYQeDvhv_Liv80-8BwBz2n6DiHssg6OVcP_tmEUTlS-wljHF6LAao6FCLC7rmTykCQsKQImMx0xyExxb7lGCX-NvClr63y0_K2r_yZBW7nibAPvheNLC-ew-hj6Rs9y3KTeXJ0u7uzcFndJCdGOwiyK7E7eaZ463cgPnfTTbjoz1XMI2TwjxZCaJUIu01i1szEmo-Ag3Df8RqFtCepe_PF-BBLfVts8n-IPKT-6upKEcAEEWfv2kR_u1ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 943 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 904 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lb9wecNqpYbpLuxQn3pN8qehoZKWvUVev3AEee8UV4IIiJW6xbnCNEEybCdC8m3hd9D5akIt07HjNzblt2a-K_-5_huOJbrfrgGlrJhWOctsriX04dXeQtJ1bimCUZ096319-rTYXwDzux1CnRv-tkUwdVFhx-479Snmmtuodk0g3rH7t7Nyr0ydMParu5iTkfcd3nNKo8bTVHDYDVXkIWAS9UABXaQEWO6HI-MEtM9C5L_eKpYd0Rx4zzXZ8HlbTCGGGhi32DjRMxrz-INOZlbk8axa_IwtmZnzqADf8V2Iv_NXquB1651uMImjjwvbeS57Ie3idMPMMTOymL6Vxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tkjdc3VrxAT8VEZlqBHBujWsyAW2lwvtPD4t_6cxy1pPY96Mc5Fo87rI98xmgP-4XmS_-6Fe4Igyh0YXJL7te3RkSeEaX_EqczLvKk907QLMugqRvBwT0QZr0XQhd5CZsJWys7JfUAMDClNfVN-TKZAYeRrPFvRZzoFy0eJmPVDE7iCo22mejA1ikW0-wirTEQu6ChtYKaT1Vwd9leYy0_fQoX9PD5Fi-OKrSPX-vJYiFb7U3BgRatC2aiUUGo0Z0aHPbl78cFgD-LuNcdRah1SDyr9UJFHqKeki1dW1VUBDPrIHA4sc9T3tIVgGor6DXCEplrNSbyrLTtM8zbmrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUarb1J-PmMgBR6vW3C9grVgUnIru8vu3zvA1BqhzQYxUTFPo1PI_OQNt8WZQUFxdfCePm45sFxv33wPAZY2eSntgKVA7gxCFp7GAsIIzE_6BrPvKHFVqb1bsI5if8_d1R3Fu3ANkD_Xn1J1Q5zejDH6zJ0WVpFGcHWU58WhHxWdxme0kQl1piTACVJF5bKCZ4juNysQYYYgMx4Wd2VUv5q1ISpEXXGvJGqQdXE4RqIyM7YQFkHRRViLv3kccmWw6OgIVtSmxw0aJ_AfxyitCAr3fN5dO95cgCxb1RvwMcveuwyavqlwVbeH9dN9dprPueHkLgCftwXxdcIpGuJgkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDOeMDiC0DfgU5xHOdfwMJW2C-V949ri4OjfW0ZozuSojLYtpRPVSzMc3sqs1hHyl8tPaWO3SkuqwgvRE9u7DyF0NwJt4Y1fY54gD5oK86bDfEigLXdK85wgVZc-j5ZxSfcOd0lYUlshYBVI2BI-uzZg5BV8JZR-NwkA2fn59Aqgpl768T94wrcFmqZRFYY_2hEBLtDdhiVSGFKC0dtDaNtnwc1lPpcyqVAajKOUThaoGPxQWS0IRHtOIOacGA1aixw9vJX2JxaCKKNXdw_tfPrS4Sv2VMQK9xWWhOgVtkVBKjzQcsR-hV_z-2TNZMahbVWsK10i7IA5wAc7u_3Agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 881 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 954 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 831 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 677 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 897 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYSKOp240wtO9FP--g2EqmjtTs6ejXx512BdjhMToB1m_d08KmQxVk5kwz_l0NOMCmEfqDvKoTrCsg1D-IcS-gy2sadr_yEdvTDFqzar-NU4h80lmHjtfv5bE2z11VzZdAGZ_9uYuMufUeZ_Hc3CS-mCew08daDDxlpVIH6QY1VmhK_THcxlACfH_KWeIbizI6lIu1oUGNqrCjnrLOfkJLxej1brsfBTBzBmWNNbS7DOwdLj7IXIy10Bp5au7hSfwTZuHExg2r3pCRsp-oUHAgWcuQL0jQDRePhchHZHMixh-9RykD1_b_9v1dEzKRNO0eWcmZtbK0vgafgZW5uWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 772 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktJCzYLYTXr1OhRcDr6jj3609ZmR55nReCR-Kan1EvuksIXleaZcW7ig1TcMG5YPrDY4I2noOMNAcZL58ZJC7NlTL8M2Kk9eAhM06NBPDIpMiGGaVLZl8BsV6JT7nwTKViI5j5E8Mt85dBhBwiBokt8ampxjX8KaHadEHbLfADbVbZr1ANo-K96K0YKU5OIr4vItKDUurLFiIAbUGo_wFgsZLbl8d0PfOyimy_86j6brkRaaRlCMCWrikjb8Ct-XtliBG9pPR1GBSBcd_q1eGfhFq6xm1HGROpOK4PPGCuIV_j1JL3gbjv60lPDP7WpnDtXl55GnGVZJ52uD9_YnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 853 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 686 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gENdyO9Bu2sGHYbUs1ceOgAHTQ0iKY8QNmRRKJlj-9g-k3Km426uhtkz-fho_gpk_dy1HdSSH-kzuBYKn_vQxV7HQ9xQ86zIUgBEaa4DQzZaGFnXYLuvmDQM0YzPH266Dw2r_wgjIIJX07u9IshKdbkfTBNYvbuG_ql_6EJeQFHxcIWJ3H5P3PRwixYc_9ruAiyxo3iSFe_k7KkU755t58prI7AcCMNMVXEpgnoIZtxdflh14GFWwsw2dP4nhfL15GUAee_LGAeFTBDcCeDoHHr2wP5r1_UXX2n3QnUGn6Np0VNQvBvnjU0QeYKc8JxJteyfMuoNTJ8LsH43wOmOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 886 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLHWDujBAYIMZafBuluLqt79TpIN99Atb1nTXAj0hxWEY31H91285Ju-RVYugnpRFWpRqqptCSlYQbJis0LIppoYZBxXofDcaaouNS8NME_-dvWWB3qAeO6vKzdmIYx4eadFfC6U9haRJavltncuw5liXCHIcM9elBURrIqUYHv02ckdnUgglzruv0OyFTjw8tw-iOvSeYbclN_52aP5W5-KjEfMEsp76e64I3TXqB-CezRFzjWN5ZBl9mmtoxoV1nUjciZLsp5go8a6i81L7adnAovk3t1HkFLECfeHj4w3qbjYmCDLHuJp_vyJWU8UFfE7cZNXn1sLVMiG-nyaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ck6uX2HheeKzts65NzhrvSBocAM5iEsoPbdR5Cf7Rl40V6_Ukp9CBONDHaV-Jgh30f64tlaTZxx0Lu2-do_66obhzw_0uNbVsPdRibU5yqJDGkln2kDSRJWi7nSDs2SUxGaER8JI-R0hxbUusmdUeOSqTHFds_9Q-yqEnXR3oBYDPQ_sOS2Kd1osizx0TNxBRydjf0UOqajDWnFTjPiEFxCPZgcBJOvdoasVQKFR8ox0_x5ZjFU9H8KFmW19efeLdZCv4Y3MwjA7G6WArl1DOPXLGaW40DXUaPk7bOOCVEBzkVn2ZIgbQqiELnTeu11mWmGef2OHjz8y1fPxEC8NJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S0Cau-GfFcWkCwywZ6MTxUY2ReWZW8c4Q7203a8DZvB_e9IroYOD4-VJAN_eajyBS9xyis7BkBa11cUqD1o1ZodIETmYxndv7jxZOrYAKW1DCtgUEfhcXrvKl8InjUs3CpX3do2pkFVnzw26JNcWgmNZ155tC3n746nZw0iv7aQ3-OzMNHK7Q3PpngixFvHhZosnjAYmYefK-j6WihqJViGvXNyKTTcA1E9iQtocajFlmIvROOzRKtVkliFa_ngwAlAflx2rrGLCUvjPob_cE_Z3QQ8EdF_ncRFyPaVos7whqzfsPF9K0SzsN2H9St23l5VBRufIvsMz9on0J98TgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE8TlCGOQbJhcgxxHiNJ2LCXSc5fToFTNs6jDx4Fevd_JtjOfvlNLA7pkpqZUdj_x82OGUehROPMDTLFthO9C1pF-hWK1k2ZmvayUCVzhBCSeq96L-HvbPgia1DgcZzRmXlsTLhlGKJOjECCbOmFdJ9UgE0Hr_TR8oCCQtI5qXjq27KHzyefMBeAnTgmk2k09p0CBWUaQTH5R33CJ4thD1cgyRvz06E0PYMT9HwpbuJlx5cbxOffkxtZ10rJ5flFg6VqW8Gxy1PNbl4meoYpLshKpBRMjKVYKRZVvpgsrh6wimjSFUIuVGT8-nNl6Cq0EyD-ivPfi_6OMi1fMdV8Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUtUOJ-hSJK4ToL73wkFiTwLofHyXzOPmn2pMOe9Hm9DZi9zGITkq7ZWMMJqbIv_xhmewvie4Dbv_IqrXCCD9Qvkuy6ahXlGCOgdbLGeyBSFRxcXd_RWhMnjwqtSAoLiuz6-T8XQoD-O_YyTpImzgeBBFEZAqBmFHDLqgOn9vLZZBwgztnXgXBD6FAqwqO5zoZWxVNnXLP6CJvFBdbZQzP_OgOWHaGcZTuphCtdJ-CLZ0zu2wsXqlEto676w49xH9nmlUMbDlPpYyupYkzQBJE9psUWLycsJ8BwH55Ev_13RJW6BRK0PPZKTDgo_TiE_Pr0fw0PWzkf7mFMGuNDJHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 878 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=GbXVtORoPQ4h28zdNMhdqthFIGjd8fuV7J-5wEuuj2qhEU8uN6zBItt-aISWirmmp1I7o7CT1V-kfxJXZlJJPQ27anRm5SWgOTEnwqt6Du9Jnb-0D96XS8xBVwa7F8mOn4zNme4Om-KiaxSDq1d24kbS9NYMZaKAyR1p8fNJ2zUoC7dN4LGkD42K_R4wCp3IOA9wr2yRWiIQ5zzyd-_FkyvNwciWZL3_mOeuWb23TcSqveISD7mMj5pdpBnVtX3c7Mtyi3y-IEg7PlK79Irr2JY58RQqqpxylDY_oH28YTUW8I0xW61twot_hy6c3Sm8dU5Tle16edvsAJ3U6dQMQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=GbXVtORoPQ4h28zdNMhdqthFIGjd8fuV7J-5wEuuj2qhEU8uN6zBItt-aISWirmmp1I7o7CT1V-kfxJXZlJJPQ27anRm5SWgOTEnwqt6Du9Jnb-0D96XS8xBVwa7F8mOn4zNme4Om-KiaxSDq1d24kbS9NYMZaKAyR1p8fNJ2zUoC7dN4LGkD42K_R4wCp3IOA9wr2yRWiIQ5zzyd-_FkyvNwciWZL3_mOeuWb23TcSqveISD7mMj5pdpBnVtX3c7Mtyi3y-IEg7PlK79Irr2JY58RQqqpxylDY_oH28YTUW8I0xW61twot_hy6c3Sm8dU5Tle16edvsAJ3U6dQMQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/strJqCrjmzTzVzYpOSby50zW5R3w-23pzhUxqFeuLEFZ6GTu4C49ZgcTaRlR9_PJ1HiUz4FqQ6yOqxhloihmBhSV1_JM6kFjfRYjHDZKsw24wFmUJfiVDFuofom_pSxy33WFe1BzHBKq9aUDw7Q4z7rG_xhmhHLysDl31o_hl5npag5zXCcY44D_5gevB0HoVWUGUtCGRzPRT-wOign4Xehr19YM2Zhcz3TRcWuvpeYcUIssJJ9ytutdDqvUMzXB3R3KKoErhFKUDel7xPU8RMN28ICwq8Cf1JyEHBXlak0MiKQOA6Ek8sUJqoRyNYu3SX7yA1TxQqyF9SX4WjrzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBkCAaAavxK2RAh-fda7CMCN0sg6_kHUWsjLeAoRUt30SSOd5bhG2PCmd4aHtGXIj2cQXs2h0_vKeBlnexuUP4xx4o63RiTD-fWSBQ4Q9RArADf5Qbm6ICRTjIDE3UJOA64sXqTeYlD9FIYx7zABjk1MvHAgDNPo_3eDE4kl6NRWbiIk2jV0jgFHaECD64w6NYryqYsB1f-4YHXIrcFrotHhdTpYsBl5BQdKOxXmR0MIs99hveGufJwbW3UoDYcZUSybe1N4HS8uGLlsB60OjyeB5sCcIy_1UTX73XP8TWHew6Ig7k1CmW425rqLSggMlYaG-7TX0lUFwwCGkdQy-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 779 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLP7aPCzeApbv8WAA6XRCioyJIFksvxQ0NOaoAUElvt7lGTUsgq21sqCBaMz-sEp40SQ-1FM4Lw98gJ6OmNvtB4r0USUTrsx51WK_jPUVD5KIDjGfDhywWzJaNaVw-JqLTGPdMwX1VQbrJyYLOTCZUqfqWlyzsrRnjho5jxzWE1lw62Rbmud4pWKa7teNqdLgEVx7IRp9hF3x5CXlSK9MNMRD-Dy2VVviKNB8hmzbNAdGiYwz3FbZc2RxWaVkvP-DjmdF1k7q85CnMNAgSGoFL0hbJoNcFf8ldzhqIVBn6lrj2gGkGXWyLX0VGGxGKxy9mDEfteChPq3iE71g78Ufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbsfCthalkG7a0thpymwpwDA15un6Skr78IAD9-vYEaPLJTokMqOQddR0rN0p6RHKqYwO47V1eTsZo4OyeNn4CDi1r2LIsGY-TjnmMTMKwwXTY2YLBwkyy_6PutaenzKAfwDpmMwHZtnDWHvDltCKeWPOwTnHHbO6qoXi0uWd1HnVJXQeoAmRoTV7P3-uRiHwph1-xKto3wuzBNfqcabm_NDMWagVZ3qS8-pqgxFsHZLifAlc2e3vWv7Y96oI_P8E-Cb6vcQlhFhsGVksd_k-dHoQ16BtXxS4jnZNcRq41xseiABFOYpir76VBZgHsnsB5Iy15TH_CN3mjQX_fxOng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 800 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2eUgctdCOU17OrqNUOSbBotKO4Ij5ke2wj4aR70lwsJz6ktlIaNHFWiCyeVfWNb6vfRvkAV4k0iRhqgAnm5nZWm24hvqpbB2q0wJISuMosMxRl0BzVbbv1RjfbQYq5oJ8pjmf8-Tt5DsOerIiUllSqXAqCUr2UyVNPN05k9vAsk0aO-SXBq4fDKPTJUtpNm2TgH9RusdNX4TGPkdm2A4i3MGOnPBlfcpD5hUez_cGX8WiwKoDt-V1Ej-oNIgTllWrsJ4e_svLRjtVlKna9FLu_BRPirBZg30gD4I7i3Z3WASu9ChR42uYXv5ZhsrSipXJqBXNlnRpb565JGDCG1-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E97fkDiqAK_biIoTV4kFu5w42ZskXobbXo7e-Epk5JPLUyHjuIGjsLCY_NcUdcQGFLwc0qSrI4EAReKPgbE5R7mHLprKzHDW2QBJ_JFkf_uYDxIfqudnjSOuPjk1UqBr6PN0c8EbBtmkcqy7GwGLQlTNHrf0V5dchXczU7lI7QV1EcAlpr9Q3LyzGlb1b2B9BgE1hCNg_T8jOeX9N5XGhjPoqJOXQTM7GK8srWU4n_gR9BGZIn_Vuj1lTJfK1daJ2bwCjHckeKunWUGU5zqM4hl-pi4wwCzTMxpaP11FQZqW5ptJ5o-jkBVotYdzg4Aa_MkkUXbXj9OsIL9owsLNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 744 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0E5njHGfzd22Y9gZH6FrzgABv2g9q7z4bCBc0CcuhDI6BWLxqCCVMbMewiKOOo6IO-gZ4PgiycNaHRhuAJczQAL1yenJ2J75C-mIORxVAWdJP1IplRZDp7EDMK8dxstgA407X5As2lVY1odHXma5Sow7642iM0ueQhSitF8Ohpruc2wokn27sPb39CgEeis4HTl-lZaGIOcF2xNU_MqIZIrY2sbB31ALjxohFdJW_-xrUbgrV8OkeumR7puG6aDL52rQMgK6uWdckdZhs2M2RoZkK51AN7jPqhEP2cMw9X3Wyf00XPjMWLuvr1RsWVJXI4mL-xIjd7FiB7s1g-oBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVC4dTTeZdwC90sQMN8wQqfQNoXebxFdR-_dY6go_p0Us-Gb9l9YOweSfaoFV_dgdAQTgvVIF24p9bqC2f9Q3rkMT30g3_QsRpAF78qcj5bYEtZYI9t6fWfvYzP0L-tAZk4s4SV-XdIXEtMjAf2-yIKNPmL2P6MZ-7xCGQ_Bv4V9CB_nMqZaTq4HermjDpLRC5DajXipAxJr135bfTVLfgEfeWoPDcZ8qDRrF5Zb2jUZp--M5zX2_i4fSDQ1AFELUoxVXTPRpp_BtAnQS00gV44hktMNq_IDcJa0qiWc4fMVn_KRh9PLMAluiT2fxreoIcXoJzt9h0tK0oltTZGT1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 754 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BR7qpGCKjMTgqV8m0bJRuC-DFLWYNhieQIUlxjfpE75eVrq9yKm-7rKMr-YrYSYrIl6tWRWx3xyRmbupC9zRFfL6Mkhr9xNxUQ3hYXVNfmJka0ri6idrrQD41oYJo2zaucN4XB5rrpFP-M3qHRQcTMARb8fxKUW_eyIe1VzfUuF6rJFi4e9mpH3xvFxx4dZkMkgdgdGjKHq2Mg4-Cbu7COwP5yEg0Yv21vQSN3xSx-jalQgU4h-9x1X4SvTvlEb7lRoJXVKc4YRze2VV4AVKuzeqvPl_I5bjQF5FxngCdSpRtp26dIZcD92umt-tdVESo1mS3hY4T6PlQfhiJqfL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 812 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 720 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meebArlmHomTpjj05Xpb1d8e3vU4u7zns7SFUcfPKSYLvfDTvcjJNy9p0Cxbo89HcPLwqJhkeMihWjMKhK3r1F_oWHgvTLGpryCX6LvNrpe6xJ4rU2feiSlFiTFe-7taMjwgcfI6QF1UWWx5rID3grJUJtmJNTLuzV2qTVibOkELLYExQZ_VTaU83pAJWYKR7_9NpW5ZVdEko-WnLYJujyFPAA87nlcrVb1bOe8jLz8r8WJZX1_oCB3lMIFj0F258AtlHHb0QkGbB_knUQ08m5FR7nIYMLOgDb205-HqbrtQ8oV-rLumQG-BWw1bnx0ehsZ-jFAs1P18jlp7j7spOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 821 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPy7Yb5sE2_uB_QTok_NXaQa6TiAOQ7eKuJ1NT_7IO5mgybD3s_eaIzbyzcTLsJCNqeWQFPnoefVNThZ03xV6ha7Twk9ksPAifxwhdVQEgkrgxay-Ow3mMy1lneLHZ6wjyyCE9MYmT7_ea6NBgi6PgH3vxzOquDG9PaHsEAIHmDx6RQ8FywnQNb87Vfk8fWROWLSMj1ItgF_vgYGr_Vyvm2W286vI4FNBJ6r9eNADeVFmAho3bJRSTCMHg60pgxNqcmCjwDlLHKx95q_b2GS2RijDNme0wh_GPqc3i0ctDwIpZsJSZ8Nv3Pkhqz0TUeyhsvdqHHLZ8VeyGxbG2HQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 603 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdQ8UBrCH7GNiJE5XPeVL4V2L4uZRLj_w5_YCy0BQRJVXAc0a8pmrJWMF5UrMVdQAxE3KsqHcZe6C-Pj2sc5oVLzvRMyRzztmgnfOTK3VGsItidd1Zu7T-HWivfykRkVJ_nYjD9-un1z0mWXyaN-odCvkb_zsfLTQYhW4wdcQoyeVZVJu_UZIvOuJrwFAlsaAOkJQqM2NhGa0T_EO-am5hxXPdoO8XhZdawL6zec0Cz_JYhN4Wmz3ZIOInWHDOJUE7EZAtQXVqnO_JM37L2DrR4jLgPP3yYgjILR1umSpIAJ0aA2BH44IPz6v88TCqDrKVtoJO0tDYAhoNpB0Mv-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 696 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQiwEzaPxY9r5V9anwrN9yLCxqzAq6M8OXqM1uMI_AR6ndo878UxYHZDA4sYY5I-x6P3rUf_bPK6cGnh9zCHkPYal7FkCBiyQdr8kL5iej6wcCZnzkfph1gvkAIF1TpmVUt_dUUuXaZhWLwlGpQu8x9JMrBA_gE4WHxkalpHJ27EPyeP7uoZ3_uYVt6OJyPKDvlpQuDZ0bTTMSAHjY_c4oSJlcN8W92U8YaXeQqX267e8mYD_71thUrLnA0STzk5wiMdD-LHy5j0_Ai3A0XR643ewswYhL8PdhNVNii4YI3Qxm7SdKVqArY2-h0HQvSrCuztnx1ASJjgP_cNyuwguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1eN1vUs3gzDlyr8PfAykLbRY3uNP7kWprgobqSYm2O8OZFjspcVZMnAPaCweoEzY87fWIL7uLEdsOQcOut6rR5eM12i7ULPtGa-NdZNfymI7KDCYfkeh7SqvYSK36tlfW90CXS91Ybl3dM2mPLL4T9iJty4mTm2FgtJfKwECOUmO52KSSQSdS-iNMMAxc9dit7igZBhNpyC37ZcLKobIP9Sek02nqrnt_PM3G9h8uV7TVKHYbj5QuCW46MrU9eagiXbkres8_LA736dfXzOouPH-payPo5ASXIKojaOjASrHatgp4ZoffSj7fDjk2RAc1NksVkTgAe3_OCV-zff8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiV4KpEL4txemuKS4ppXMfRltdobefJz1yUX4LQTRjKFTeFULBN_ng1luGLgvb2wBGXtl8W8MAmLxTt4RMq56fxxidVSAQHmrs22Lz1yj-gQvv_M3lzk3EUHlSr_egyv2FCUGF49Q_vcQvqGM2cMlHceWBJBCn4K9Vlw3y6C9tdeDSyt9r03TtiFTjYD9VNiOnp-zXB0hqAnO2szWdYqlLn3r6INEcv0gXXtFMVxLhQG9EtI2GKqrItMMWLVpRrfwYFKayendFANkEc1SyIN1qLBHnXZFYE2Sm8RA-Nb7mooSZM5l5tsfVOkFQH6qyL_Wk-u57SNZG_ZCenfdJUR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/goXLGNzEkUayHvgyepQ4ii3qHjmJTm63Xw3c5Cz8KX56q2fFRB2gS2dbp3Ok3CfmoC2byWsJuwsMF_AQ2igmH1ufAkG1IXtU3O92wNTf3BQSt-s_IQa_9hUgzGT0i3Zbi9TMp1lxc9jv2VfQOfxzSw3rWDBQSzkGWWQCDaTjS0xf5pLnisP0dFW16T_ox6JpzMne_Ef5cvE8rTZ6_Rw2yVvm4ylEXbHSOrp3mnwesg3OOKzxrkqWYIYVIP59tXKv5hu5wOeu9B0mMIHLKAw3WL0BqYsSGuwnrGVzTYKCeXSBJ8a8TjnxxTWtDcT2c5tQRzf4gSKJbeK3h3uGWK5wng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMeYaYvwb14auI-bl6bz4UwAq0aEo9p1N8bfjlkCRYszG_xI_3xtEl0NrkqCZtyjmNy1DVLcMwK2UVGI2jrIoAmsXTl52j8eNr94uZIVm5tos22GkqgmxJEk5aAmDqsY9-XFecVP0KQpPmCq0EO-JYtifkWneaJfKAsfN06T7qDUC-AmJKGHQosPU6MvF483BJ4FhVnkqm3mVm4LG647egKHWIFLBfSxPImoBnQS4FPzDGt10M3IhIwcaSsvFIREBExenbITftsUvak4QUyAwudo_-Rhk98MkkZY55EeOl3fIPuVTDCaqxqJlWY-9xTJeVtxmEoxOonbWKOr2-H-eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPJzb9d0HzLkBvwk7cIRCotcuP_MxJ4KKOF78Mk48s1Zrp-jimgbQnZ54dFfvJW_gVfRerLA_XTHUbbXZ-J3aaqzIQ_q6c0UxK2eLq8jj5jxwsAzTPveQ-ddBgPQJzB6s5EGfSNh-ST0SmCYVTLrVOdvmurvsuwcchobzlXgu8wXYvM7rGGbRVrQ-7E52V6I0Arwr8eCuYEBPtd64K3f0GEMY1qHDzSzr0EPSEBUO4dVX3LG2eDwpAkS88skesDXPiA4frG-MzrAWmmxz-sA5_yTNSal7jp-M8ApaMcPqlH9Brxmqu1LfXTgJD6E1dVcGnMmV1QmtCFAXX91LqPxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 580 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrM3DWXHiAknC3__epQu396P1RtxLqWfUo4uRFr1Y6PYA8S08LkTMcAHXAWU05RTAAwo0EBltbsvnFNuBVhZiFVMqagHhNG4AGF61TNmvD42AqlfYz8PzxO0C7tQB8UDrTJq08tPvrpZS2J89nNjNPpREO2Blt1G2ADa1InAMpsBEBCeJq5UNXyXtWNJDCCQsX6PAiSkC0FyqlSB2HjV_EnfD0Jr8bRBqantVusCHmkY9ndLCBj1gQ2hlz0qUSxtbP1kR_wwexn5HOKuIum0JFhmGg-IW8eSDiX4W050ueGQUojwau-KigfWRBs7ZlbJ2CIuswHgkwPZjBL2UN9Bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 591 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3KKRFAZWUrPD3UKzbtodpI1ZZgqiLxBglK3HZvq64TAtDk3FfUPBqbiJX5n7HmvfMcGitC-QJeEuQbAuKJJupsaYSqOV6NNIPhzqQXgN4tqKpVDCaF4x5eMkvRpshuYkeFMtOEJbtZjGKH3yo3JsDU8q6YA6kJRYoDmJhMuYuaMt_PsF2be0Wl9B2OPFp_hK1iGiRS38nk8pAIJM12rdtp6-H0kpGoz1ifCAqNWL9_XJtS8Vqg-YCtVsSNUIHMuwnkU1PvsjCIooD-dGjsGuUmXYDtVEunj6lrUCER_b7LG5H6cgPcqjqahT-O0lla5LK9jc_a2oW9_NwKvqd8log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 700 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxOMDE8sRUD4KUXH6J0hzG_aMBaEO2rBopRZ9-moYb6xKiEaUl4uPfJ1AUPe9rVmVQqy7ADCNw9C6emSDnRRt-5kybDYKddhuj6M8nB8_2gMnn3ZaIqMiogS8pjJWIyXkN7Ix76yJJpd-oQ0Aot234r0pz7x3hlCnPFsz_ye5big7bCAEa2KzUQrHgyJm9b3BKeNnYRkH9WG-Opwcu3CP8cLG1ePBPlQOhjxT7xujEuiNFsW3hh_0TdKrP8Qdh-gCMlzdgxARghxDTBIyTugSjAMz4WeOSTEfTMmN_t5EuANwXHlSLEzyIXFVpfRIfBX2M1GSb2iRRwr_BuEK_M8ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 645 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnuDznTZ5Yf1dKS9nA0iDCRrmfcjpS2ec1FHgM4cDVPCef1BsoWBNV9Mjw3DTK4eDT94uXXuWpkkVr87fLxyGrskmkKVROU6hH-lxcAWqev2j2vtFWDX-7T30t97iPRMjyH2M41kX9N6lyMr4JziBZVDTc3a2X8Y95oxSLzPjTBTgmfF1tVh94EcsZguJOwygWFrmWBD0Z3Ru7z0u_mAAtP8wVp0YP0WzIf-81zGY1NUBOW_Eu8AzblPhkqfnGYKl2RnYj0vVyjCKuWpAcK40Wzv_wIEUKgScx_MYzJx19F7HmKWmEMHRfekDvAJxoJEunMsNBZhuMVsljFiWgDgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 713 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1iylW1x_iWWS3Uanb6-nHayLKq-YLv8r54MuGJj2OUuMfPHxTghG_vwO9eHVeNwRC76xk9Mym3JBkNCI68eesuICMwBE050ii2ib6_t0QxIwSyiHuxQJfK8hiJtUpVHxUml-cbD4lBB2x7-o5CKGKR5hHBanMxn8KpODDJs89yqioQF7OyW9jsAcBQhSzDyQPaibQXSgNXZYYLEdHBIcrZ7dmmjFblE9tVJWYrrtgK_cBnCF2QE6XgnCr68i4W8vYIwv-ShKvz5JHtv4VmqgSSDbwXxt-HU0ZhMpHtI1y85HTfu008X5xSQ85c5Lz2m1PHgOaiPXE-73v_vjpRW7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 611 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqWKoQQnF1ANhm_KRAD1Exvjfuc2geDM5A2mJnTr3_ICdPF-0rJEAPaeQAex31cw2N2aVDD8NT-YA8JM_8GzpGaumqyQfPHtSV_N-uiagMT5ehbpVHef4g7pGTDFa0YasWVSRnbZ3bmXs2qcyisfaAfkqXgYNnkduHUHpnxzp2zY2d1tQEdaZm7LZ63--1gqqAnmv6pRLiyl7JlnQUN2DCWHz4JSQVT42C9vb_ld_8tCoPFjXaXPqrGB-b7gkJ1Yzh4Zgb1NnBCd1rfWr3GIHZ6EZKnxx5c-4oVIxWPbjgdm6KH78E2R0Wo2G5mVrLL3mmh1Gy5zOzkxB2FfLDFhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 640 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJM_2Lcrcoa32ZDNMz81iEfWccxfeA6VEC9NBUy0uif6ouUxdB6UD46LvtJpx9Zqttax0dlkClmXfWGTDoyO47CEf5-GZ_sZI-Xa5GHowij40FyQGYxor4TDZhthySyiOEjj-vYIsQXia9umq9bfWaW52ZiwAlaqeCGM-7ICw0LBtS-Yd1NsDeG9JqEBAkOvTQHaCG6lWH4xsCGhKggubVXxS87xLqgvXaC4YOabERkcj61rjd4Zhg2rtSmIZUZhDzxapye5gV54DBrjY9NHOLDDrzqPA5DL3Wyvp9_WEWpz_GlotwUDw7Ac0vGrSpd4bEX0e18O9vsGh46xbPG9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5L44amNktGDbGx6gO_Oqj_A_YFENiqqMA1aDyGsBhF9OW1Fj-jNc0Kstg1vAY4m_QRYJA_6aJqNuDBYStyQNazxzWSNoiHaC6YCGRj2f0-g1ogmVyCB0DLGEfPCMDnx4z7PMXI5vHpi9P6cXmCYoLCLzSfUhyW_2J3_w5R7CxzoySikfrpKvKkK-BnYXjm7CtHFuBYLKp_KLdH_0AxHh4P6Y416kjon2YNuTzRnCUL_Fw2c0yZdYRQr8px4EOwYPkPgqQ8vmYxBDb2FXe41aqWW-zcw0h76_5KX53gAu1M1bSz9955AKGq7dSSswHjf-1dyll6VweESEH3op6Y-og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTfQ9vNvxKmuJaRMPl2SmASI_j5YKi420NhSMxmpz6a-oQdtrYbxxMAu1l-POzrjKKHEJ6hjVcvBZ7-UilnU4gEpZAclUfTaQteQJ1o4CxnmWFJCpmg9eY8ZIDX8ikt-ddQza30wsNwLE7kNsjM1u2WyG9_fcQMQhRNIuwEn06pAe3HqB3YcQbTHDDCRnFA7vJCltNHzsSzXS0QvfSSI-HvZxxNv-nZVnAQ6TQ_ty7szhZsMwx2d44m5d6kmHvnhGBKYNx-QjUm1QhLXhXQBNWjiBOKupuXDsZzgZTrKsol9xamulljL1od7YIyeiYW-wjUyE8_WKfODVwAxfMq-4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 544 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGsIpIm6VgJOI97ImUFxNW0iLQNZvheJb-MThNSkmojoRB5N7ysaSPQ9Vh40sXnopjSn_GcO2aHbWI88-s_cLuZQmnFeo1PT2BX6WYmwh9vRvNjxXKxEnsAaW4tvYErDamoWcEuVuR5GuooNV2ECw6KO3DwQCyNF_hFdFf7LA46X9hIGyGh67ZhbZRhcK14g_5pK4_NDXWw_ByG_nAA1fFs9fVH_B7VvCgcPNsuoiUXCOxxaVQT9bquBnOXv6KtxVBIgL453W_7JSTMDRFbeFxlCs2dMHTh7qfk9EEdJRC9EFkzry74NWtrDUnci18nnMXFMcEnpd_MlCkG4NrUuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9ZvbbA2bitFGCjAI-tkIA0VmlVzFvj2ZV14IpKO1O8aD3GViBywKLDllT_w8c3IOZcSnVUEroet0GbnXAX0HyQl7l7EJsEc8Vudqx7tdgVjTzPlMixiuUAbrKDDIRjgOo0eUHV_DFqacJ2VJI4a9uipcCdbpCqssgRuNzj8hKfnTxVRTdl8zVJ1gxM-yLgwzqdSnp_0Vc2BlMqi6F7VUP3yX3fXbU2NapViiOBZpTNebgu6PBiBbZrrELgFKkxmpxw9mS3xmYC8e0Zx-70D1KSnxO1Y9GL77bVHWJqDFkNnnQv1qBFjMc5WwMyAxrID75qocSi3TzzY24EqMcD-QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 668 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v54spfd2qaVxXf2FLcoRQZIdhp0ve4u9vB8tQJcS6f4RCS1-WSYYeY2WlftL18zX7EwyuxBoIp0pI-qAALxKnftq9rG0QjjZD_EdPpSLYvvzBGj8zm7W_oaOl5EbQqbjLWGZGAbmM3scy-2Y_vjwXGiTgV4iLJw-LnAnMFvpymTX-FGMREiiGjVGIbVAwcZashG4Gn22POI5rBgcJaLp-tDmMLeG1rFaaLZgUzC75jzWTQyYPifJowJXZLEwJXpaliBYrup7K2tM-hWDwu2TTia_qSkYHT3pLeH33nb-CTyMRkMJJ9IyM2p9Sf3YdVvYFm4vigH-VMTrQ0lesDX-uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 682 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 691 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2njgcUMtcw8k_8iFCc4Gvr3ZirdyfEb7JtvMhBN4qp0d68VHZe-qmrVDClasZLfeZIcLIIiQXeMqX4r8v7A6eLcHFJfk2eTuJpmhAcnuwdhiQARlme58Vw-4KlDOhMVbtDzh3PyBwU0YpaA5jOBQjZYDYKFAaV-03oL-PkbzRcW_Moq4vdrgEFNboblf2mUCG4h-sGwFrvEiHGLcNBK2P5EOyaxs4sv4w6OoZ_rXh8o9dNxj7cAvB1_G30KgCPC2GkWMeYXALpv9AmYqy7IBS-OQgU4pPdvSTfLBmIq-pWmmfrjlTNlBwSSRSeADZ6jgnjahr4Kl3gWF7Qmg1JbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C98T1FNHQPUKMTq4rjfhaHv5bsj8DffJ4MzBnbGvyuR_8KzJPPuQy3fa2JbcXlHgc8umFcPsWIIUFOMXlAnBf7ROdkYCDnBYW4Bq7GICGpY6qLg5i3aoAKXzlmG6YASHCCf6mRvTTXK9WVaislidD8ZxVNRxMmA8BptbFY6Re_ofvXMlE7E2Ka_yRmJm8ud5C-8BBfFrzLTQ9HkldRxvrYoajoRE-fuGHRuTnGHlElY7ww76ctu_igp5JYRNKZgv6EJUFTJBkVUvtMOYJji-9-72cykJxyF4NCB1nSpL1UpYGHkPSdBE8J1OwxH44gUaqOk1jUiOlEiENS5E99p0AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 813 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nj73RUxuqqxOPIsouSZ3zk22lwT_oGZka0o768LXkVlhQFxsxovX72XCw1Q-2Tes38AYOa17ovFuibOEt-QVD7iPmLu2mcck20LYCQCogY7RBRU2EAgI6xrfYfvhZZEQoR8WU2pqtBNuuxFRTUKCuWaTLSVhK_1THkl3KuadNf-tTFNm5iXVHcdtctRiDJ_h3NBG8zGeHPoFadzO0XKLmA-Jffm1HN9WsTcIjWiXDtAPK3-_TU1tEEPrDagS0y-m5N4Uvrh7ADr1zdCufybgrZzMK6oZnZRj5acYywAWOzZG3nPHMmkLv2NDSifUg7_uVoNHGWlJsR3Qn_A67UhGOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t68sLRVyYymOq0v9G-a_e56oC_-HsuggwLsaN-9aTpqpbTvbYiiC4dsyM4BYuoY6Nb8SUAvLULli99IsqM1xibofnrhu_8Mg1fYYqF3-jSWDxOyuWCB0PcVTHCtFwOOfQRkhXQuoE9rdnzFXIRUCLvfbMbgcj44d3a2VSVW2Z5xNZByaoQKtxawcoBAsi8NUgP7lXQxf8MX639_qGAc5ALy42CsAK-msBkEvu2ODDEGC9bQZGM4001xTmcXqQP4dV0jK4NgMtsy_06DykGm4fP7I7qn6SZ62cKOiFjTzE2Q91GV-Tqz3Xpz3ESFUhrU5Y82eISw-JffCQG__HVUSIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 805 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRXZGYgKgg9Sg5zYgI73SKoPyTy79w4tfRyxXCKUaqYQzzTxN3g8bBXxFU38qGj1P-eJv0UfGlxmtTfP2rEnRKyQmMkxSMtkMlA5HRe6qBFxvj6GRBwC6Uuy5duGZRUozveaoeWYUC9fOp445wc6bNelTxJrGLZ6tVF1aB2NWr5LbBDeDEUFtJjjZN6hQFgeKSnmuv-pfxxbDqUULGNz_JeIDrPswiyzkhvv5TUD9Xh_tgjqAINcx2htQmQ7qqVDGLDCRCmUU3TvwOPh5l7R5TjnYQKNZXi5jIzm5Y8EUpj3B36inqWVx4MfZN5fCcM0umMMRjymGiDqOurXdxPuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 586 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JNjpThlBFJMzir78Q2-lecM4oX-GdBoE-srbjGVjWM1zeRL6smRq09GwoGZeW3cLnH_Tt3INB8k0W0-__zxo8FSEQXrBelqgH4RGFsvUPqN7ngY2vDvSMBvs46tWZhoDlibwwDFTbGrl4WMjgr_KclyosVrCIzv7u8SI9Q62YFiCJTxKhq54uKP1XVd3CUoBVIDCJnBGyXkdo8c_2jhtyK2veKG3Stz-ehO7VekFtaL5TSifFIejakqz4s7aGFJ7e_JuCVO5D3mPdHBzNUaqyM6JIfaByz_gAECUKtmXh_MPRzrWeCaJ_DgTldFGH1GSIc9LwfkPst-G5E91uDjKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efedcpTs4pLJ3s_GxuDEmOawoAzlOdUgj6NpYr5rONxWGnfzm5TBWPZ0dR7X7xRUHcaqAeqWMLPczmr8Zq9KDQDfbiXavSVnoakbPRiagbApX0QZoTiUSQ3_asC3Cw5vy4R7xRvTGtcPVG3YlQa4qCGcoBAaZH2F_b5ogMcF8t2M5isOtRQeSlZTs8vWYPcfdmR9KZHglWA8F9JII_Rn4JWQk87EvnYIYk-Y1wKOhBBqxr_ORm44mVatkz0yGta0SdBl2366pfFusjVtIl9eI9yjGcfPNCYWVyjJKtcoGTLIkkjye_7uhIjho6GNrld7GimIWxadwviI_rIxL1RQgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 674 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRo4K1SQVp98VSk1bA210HxX7GKJnol74E5F0DwwyW1_gUxo7X-5kefDMATQP3L4XLuKP29sUfT5f4AL_n3sOG1c6sY_4PwgU4Zm0jwdDcRCDA5MUdKJPDneD02BFTOObLaaOpWz-wUqMN_EFHLUajJ1yDYt23FBUl3pt0zve-Gt59CwK8gRZbd0SFAnCV7C7JM90JUkXUsQq_urpSWlotoLf56onxZbHVYSQTh1U_QDnTZO3fFHEVLjkUiVeszf4g-4M1s0M6IyBEKwSeY-p5s6TV7uOHrBCbPXutc2Z7B0JqmPAoPMgnuZ8fgeQAuul3AmoNL7ze3hb9nF_SuOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 717 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWIxcOU0-NTsCuaT_mI_zL0te8yEsMDepcQelrfuQSQtfW2pqt_gGh8giTpJygvdXah18j4tX3OzYXDuFtLXgAZnnrMc3e2OlA_uHQ_eMToC961fLNHdIauKfj39XLxQWIImK3mpIcSxOZknzZhFR2UCUjIvp7fMwzynD_q43XYHthXFfhiWjFOPMFTm2wfjsRhyueCuFQ_ZlNVCf-g68Yvd8QoFY2R4DhJRy8grfIkw6to3olgS-hRVbU9e9GXGIc8w3ZZXub-iihDogt68UZLMyEmgFoSZjwEHFHuo-Jd92bHf_PbtvrlYymlryMMjdjn9fryPMGFZy-rWYEC9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abqmM0B-Ivnpfvu8hPW_gWxb8O5Q_vm_ZQOuuFGTVK-zrlxKAq5g0U5A7kaAjno4abmYZ0MTfW5vs9zAah_3fim3CoIZ6uFYVD1beEk3zFNiEu5INJU0SspcRBVm3f6vm2h0TRvlzyWAvufTaJi7QedJNwcfUOEAQb1GvYUDcg0XQU5ZmFsVtT-wJUzR5Ko-U3RW7PUpYPpkYCMVcuI4XQ6Hv-VDte4vNZn2ml2aHGMiSABTZbbvgb8e3ZsPNsQ8FFzyMGG5i3eUCnlVkHTZUpjJKicusj-9hO2GlefPQVyIkTJoBKVYKfmdpE3nloAGtW64PZ6Dn8wjrBFPLHWqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAH6-eutF1yUm503yy68Ja4kEEHKvIFqFEhoI0IMPmzSgNCJF6kTCcFteBbmLHPQVYxGcnqo0OXf-C2WKlgoOAgMf2xK5rMDUAhztam6KkWuPTmLV30ZJYI-XbxCWk0KdwaBk72-HyV-689632SzgxaZyo4hOEjqvswQYUxjXHYPeuRYteh4Smiwvg83VKoW9NkbzCjoB_szzIhMUfl47nnxo9uFyq0rmzNHLL0ZSfIxgSBAIROq9Ys-yR5zVbsX4Gy9I4q-TNs_UuGmiJGZ9Yst2lkNFG-CMOa0bSMVwEAlnLmhWk1ZhaQGO92kChKqiowfn1cCHzz72zzioVJmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDrZpM0tp-o1uvwvDsFl63qwwIoTRrFTMEVU1WowZKg_dpwCBT63WvuovixlLr812TLVWg9mvAmxZKRrrnTl-LEmX5uL1jNjcOdgBV8skvL58LovX6FptXAjesZo2zjPyQ-6eQ1MbsEWYw4c-u2uMpVIrm_fgea6fegiPF6x3MSb_CU4GQSjo9npbzBty6ZRsSzicmq7-narh1n5ReCNbbz6lnKlvGEwvA30tBxduvhKSRGuIqNg4Oeptr6Ql5HhahxQGqng7ny3ZKy_oGzhSsth_WadE4LFkDRL51K7X7nSv5qsOdWKHLbS0nm1g-azYU2JCMV3SMmEqEVfw5YmJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmuPZPuTiuT5gpX5IyqUUzLfNABdzPr1pMwBl1kAOwKqAI8VhKwSF8-7dlc8FX800CJ8Dv_hPaObj1d1-syQeXZdquAqr7qrDaT4XyUjFwAm6wAE6lfKUM3JJQQhSJmNu117CSnTpgKHkg0yIDxID-yAcLVIWaVb8HLBE4o3my34AMR9mFbfsY-CHuF3ezzhGUAaLy3AmCalJtQnet_OYlVWJijQsc2aODHRB6Og5XTsinZXEIpaw9X_hXSe4ErnyUx13RwFBAoQ9UE10II4Vz-EDv5e9QAFzzBvsAnb2DCTQslAwRg5ErumJw3tGYkvtwY0VyxSVmOpr687THPqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGusbe0Xl5c75UybizJbESojmaF6s7-nA8bxFNFKTDNN5B_9uS9FmSoJb25TtDV1_DWEkLExFikmKWmmzZxp7d6wzqgg8oZCw9xAuuDD9rOsbz8sL_uxqaS1Le12XGD8LTusaK4ldUI7LFvK3LcrUH0nRxDHIm4fBRNxBGhIVBNgEysfiEnlO3lEBlN8yfqIskMcJSdysU8e4zZV3qUeFF6tt-ioTfnrhU2aE1lfqkdkwx-0TW82dLfCj3hwYaWNnDsB8CzUB8dlcOQ_tqmIc3tMtFKSdZGCR6l94uegEQoiGF570NAiu2635qsOzfUbcN5OuQosc-PkzoCMwWcR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qdq2douyZC07XtQ1IN1u4l0jYyPqmQ8Ewt6WuF6dHG20twTIPLtxor-ZHoSxSR3_cX8EwbckDo8cBwBEUKzrcBiVcmbPtig6OsdCHGJ7EKvMSoCpA3gAcwsc-j8Lja-VmlHmn-olZFtlWIxRQt403MVCFb1Ygwuklr7Sg5pivzBW0h1ssSF8O0ALqpbi-Ni5zARRm87Mpp96f1UdMRLJZtwBtxdVNR6HvsyaRj0L0isMgXMilK5NpMoevciWRVJEveO9cHmgell5yAOhaXm3PXq95IEEtsE5HiG39MatyljgFINxY4Cil4TE_U51JVvOrFmSOJGMN3LeqnGZcvhiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 657 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1CJd2Eb_izdjIGT04QNn801hYIuO-rBbsbxK3mHdS56PfALuEbSP3WIQWAmam28kdHqy6hvaC_6VY5wcywNNZEaw3deCPXswmuL5P20qm80nCfCz_kvoI98wRFURW8qmy4u3plARs9PIzCh2YGFj3RRUFGq16OIfYdwFbEpb-S5DZiQLGB5VvGEHF49ntv4fbrolvcF4jzNBU7eXdWNgrCy_zZiOhxGMUqDZK1Pl8_F_zq8hFqMz4Synqm96NuLgqnsQR3DfZXiDiqXXnQ_m342DEi033OJp2e-PoDKVqrcU1gJ-LdJigrwmPgM6k0rgS3vFuOMuYiXQpDy1mU3IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 702 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qFm-iKCQ-kcbeCClKlnI7ljkv3adLqpHG3siWK5dX_80xRpGm3_2a63kjWkkXk1z37YyT_ggjwBFUCM-wmegxIs7RaOfQIYvO1fV1WdFpGkC6ScKG46cDxrnYcmy5PS90MHMZrl88TC8ugdkqzPNaSRxeQJVmvmyN9c7qwEYe5LzuSfwEeMOoTlrGPHzmXW5fvrTAnqJhwiyV8eL8mMs8lls6IaKFHw4DQ9z-kYM4FaL_LRXoOmT7btnlzpB824dQVpBeZs3Yqc0K0SVYzBh0SwPiE3LvyhB27jWi0czrYZ0dHByzi3_qagyDDAsbV66qPWyZX1NorJ-wG1xB1R3Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=qFm-iKCQ-kcbeCClKlnI7ljkv3adLqpHG3siWK5dX_80xRpGm3_2a63kjWkkXk1z37YyT_ggjwBFUCM-wmegxIs7RaOfQIYvO1fV1WdFpGkC6ScKG46cDxrnYcmy5PS90MHMZrl88TC8ugdkqzPNaSRxeQJVmvmyN9c7qwEYe5LzuSfwEeMOoTlrGPHzmXW5fvrTAnqJhwiyV8eL8mMs8lls6IaKFHw4DQ9z-kYM4FaL_LRXoOmT7btnlzpB824dQVpBeZs3Yqc0K0SVYzBh0SwPiE3LvyhB27jWi0czrYZ0dHByzi3_qagyDDAsbV66qPWyZX1NorJ-wG1xB1R3Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5LiQro6_3YkwTx_qlUQxtz2dmyK1k4Nct5F-MVnvik5nLbpUDzCnF4YhRYggeDk75lbSDIvwJnDsE605NXEm5czWDTEFSHwVYx-AwSuvqOFLj2ylCQ1ey8iKFfeKe7KQkVMmHHjcvK-sUz7mxGPy6C38Lerq3zgrgOd0Iuq7JrueT1G5y_0_yUIsjktlbPsZBazrFsZdXbWKb3dohLKeDe7oiQcmH7ioUIfqMnhskmgQ1gqH1iFaJHk-V1zbssmJ2iFKt-u8zZicRXRXYrERj3T-XFEarz-C9rx2k4BV2WI7VQ3z5pV6jy3A1VKjlgbJ4DbzWZfqvq4gkzapSOfcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxPx8Th8qwIXyNhpiv2WNMGKtllo8lp8s5ENGk58jx8weZ7wEVASdCMNZ6rUTaVDSk8k7AXsnW1fFWIknzmRIB69j3iUn6Qeben_aooCnKXMRSV7TND4nxH4tbd-w_PM-H3LWDcbPDRpZWoJpFAEOUi2wCDj9uUacAHLL2bCWlOkQxnGaxYdJFSjXStbJ53i2_e5IOjvMo0P-CDTxYYsD_irn5hTHdksMJXkQf0yuq3JhRynAoeDKh86-jLiZvoYZuOv4NOGjazPoflD_Vs4osq0dNE30P1YxSyDBbJNzCTsczQ_rsN5I5apiE7ojtACDTDP-j7MH76-OhjEs8eviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fb97ZGZo_FSypVv12WGXLOL8o5uuYsH3a2tKjJ5T6ZTMSlfGhWFQQrxrTAc1Sp7ioM_qsr506kY0A591_4ah2c2UpQ4WDkHBC3U1mqBuOSQqm0bWnMiDLIo1UWPSh5UriOuScPBy132xhJFjTXfQXGPuHIs8brNkzGgyiU6tHjrGdQZr3DAEQF0kKGTgEAcealASO0ijHc1i2HEcsmqkGIhNypQBjugPufsPGs3x25owHT6cAJKRmVdESpOZv_Jp0O_1yHoXCDLWxXlZLJhNsgEr_qDrOvovXFI09WUD1Vr0zhmclTXm1wfTlxaJqByNRLgYzpPVK1-qjEas4Wo9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pet-LW6eg9Q6VqJsFfr9OtKEzElqSAYZv3Wd1nox4A1giKa1m5FE3VlshMr6PKDazu6HBNHE3EYQZ2qomDou_grXKRzdzO8cISDb2kcFk5BrUA5mIIbffb3nXX95yto4E2hqGVNdh13fd5CIGlkB0jTE11YBGb85tJnINd4T-GnKH9eIosbil0Etp23fvFIEVoYO9PHIvM_0EnN8hJqWfnapKonT8wdUKEZTwecgz3PU-osuV8b71US6sNb5exNyKKUDh_i9P23mM4E53LltxZNNXkLkw9jnycLHlTqE87dGw5PKkCzJNXuitABa8LnyZrgvTNhfTrjNjctouL_chg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCNkGNq7jPJHTznNiRcA63yzRt3JuoGz7c2rsFv1Fy4o_-R2etLOqb9zsl9QV_Bok6hss6HX4EL6XNjedaNTFAGZcw_yxyXLi_V9eXKpztmEzNm9HPdYEujMI_R7lvuXZxDEMxhyYN4-_SwYWv8wSgPYZ-Z0nIyOvsJeRbNntlcswfRirP-2PYYHxUj_4rqWjCDl_0-YvDN7BoHQgwrMy1TiqEhZlHUCIeJkssDJexfe83eCtI2dhWfz_EFoB9xhuVj-yYtJRuPYs0YYtEIPLqyIqS5eEYPZtEiBicDIsEQUXLndX6NQhvLKPdqXXzRpLo4czFZU7Wz5eAGQ5sVwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6WOZzy3H7cdsABHsAagRPDfzShzSnDYwgwEcVPKLXfr2jFX9To4urhBWjt4ovSoinKMDsbXlVase--AndKhXm2RYO2hlIpFTfObTQWbbuhY73sbARyo1t9oyZ4DGAzNTNQTpSCnL8OixO48QaC8CRHlkWLRVQuBlk5a_gFq8MheOhJLikO-c-8L2YxfEEZaRtmLfGVjhnQBQt2peZQ2AhHXDrnLJeJUiV4RNcQ5HD6lF5GHQYYI9L7d9ZSxjc9vhTn2L5cR2aP0dFhiSDqS3CjxHsechQysvn9W0y5utf0CP4op6u09qydhvtQPS-NswjEsDUImhihCC5F7ucSAuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTd6aQhiIQMiJn81_cI_z4C0QQHazS5pb0ngyWiBk_jES0fGdKxAkBCn_cK1I6W-Spe1xptjKg4VE5qTF8OP-pzzCNfnKsPaYGLfjMgGLfLjZZ4IrPcWWBkGcWsPrk60_aDKMm9aKMKKr3d7fRPTAndQiiFdUebyGVf7yFxQsuvH06HBNKasusn0DUzrxpfFp8IzHyeVJUQf-2dyid_-NHEr0ho2HeqWK2Q-M3tdnkask_XE5PYVTkuNuRcXxHp2vU4KeOjVMzGcwKsuHPgy4o7X-blvkLvrlAE6uycvGj8Xc4cRC7quuC6PS4Pbqmmuh59PFBOepP8TuVImlR1_Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=krcrccq8ks6F4L0A8mK2jMUMWoBvnHcRupbaH9ou8ldXhqEY1S1AuCcFQ6vyeGhU6n1-RyuZjxMgvVTmFccn3iN5Oi5rYRKzTv7nc2__gCofe6XZrG9jGkSVC3CqNm-py4owTorkjWXFMw5-mUwrzop1iHYlSOzGFIUbRwl1yjq1J6YhmbFPg4u51n4ZDZLP0RJMVyn1EGcX1TS86V7mCJ_x-vfLvNEDZ6u__GDsl0fdOKcwoyLq0jwi_8G1TxBRZT71YVhlGrmbIxRIUAJDTiQzzLtsCyitwcCsbHAmV9VNDoTG9Jxw_yOdqrQzG7o6DyJ_7X0bW1mVVkHxzWfK0mAjVOJLumzUbKL3Bv1PF7i70HB4jx8F27-dEqxKyTaqhK--O8jjfORfmhvl31mfs5lv7ERAEXtduxmhuONmNaB4KBEcvXq-sgiYkf5YcGPIPQQRzMnMz-WoIagKL24qgG_R6Kr1MeTDNmr-c-gnJ-H9b6G3UP8oYbzwTnP3qpQXWaLX9ysDcc6pG2A0brbwYWCcCEkgbh2IIy-4nRVdnzT31pTkQmdPpgGml4w8Nudtw_eVacPXV7KBx2OpvRnI37AoYsFS5jgU_5r5MUMqF1AkhzLtSxKD-PDZVMK30cpUpAb6qmwsZKLR1ie2BVvq3yl-Ri5LFg8QHlvbo2uoaUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=krcrccq8ks6F4L0A8mK2jMUMWoBvnHcRupbaH9ou8ldXhqEY1S1AuCcFQ6vyeGhU6n1-RyuZjxMgvVTmFccn3iN5Oi5rYRKzTv7nc2__gCofe6XZrG9jGkSVC3CqNm-py4owTorkjWXFMw5-mUwrzop1iHYlSOzGFIUbRwl1yjq1J6YhmbFPg4u51n4ZDZLP0RJMVyn1EGcX1TS86V7mCJ_x-vfLvNEDZ6u__GDsl0fdOKcwoyLq0jwi_8G1TxBRZT71YVhlGrmbIxRIUAJDTiQzzLtsCyitwcCsbHAmV9VNDoTG9Jxw_yOdqrQzG7o6DyJ_7X0bW1mVVkHxzWfK0mAjVOJLumzUbKL3Bv1PF7i70HB4jx8F27-dEqxKyTaqhK--O8jjfORfmhvl31mfs5lv7ERAEXtduxmhuONmNaB4KBEcvXq-sgiYkf5YcGPIPQQRzMnMz-WoIagKL24qgG_R6Kr1MeTDNmr-c-gnJ-H9b6G3UP8oYbzwTnP3qpQXWaLX9ysDcc6pG2A0brbwYWCcCEkgbh2IIy-4nRVdnzT31pTkQmdPpgGml4w8Nudtw_eVacPXV7KBx2OpvRnI37AoYsFS5jgU_5r5MUMqF1AkhzLtSxKD-PDZVMK30cpUpAb6qmwsZKLR1ie2BVvq3yl-Ri5LFg8QHlvbo2uoaUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNSn_lRg6QQsgzySGu_nIWU_yymojYH4Ki0-5cvjtVUrQkvSDoXkRcZvZ6R0doBAhfryaWZt8rLtYyVlApJAikU51gvxLpDgRsNCvbb0ssoO0C5zPJZAtSwaHMmw6LRXgD5wagYKd9RI4oOMWozrMUnM4tEgOiidpWLgF3NYDSn31J07IKn-htYu2uMIHaBGlXZHzsP2jxGLEbmMkjNiA-jeXmMIQh_IU7XGycoUCpXBPAvXGDUFJBOWy4GZZ_SfCGm8x88NI-ThCTZyLwu4hx3rYGJt0U8UECJqsgdpFExu4I1xwB9E7FUKrDyeVVNE707ISY5VExycucWKuLJwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyNq4-TlQ3lhmQnShK4wTdda9VkVe7CSDqtGJWgr2ZAnVdCc-Gw17rvxgTwym1ZjlVw6Bw8NhtIx24Bo15R-8S3-SrSpS7kaERd65gM-MTx2Scuu1DzXCHH6kgEsg4uJ5YNyNjtUuEAny_eMVWf0f1mC-ExPbMOL69sy46UmmPE_ijsKjUAcIWO6R455hmzI6SU3p_JoYMA7E7NS4l3KM_12HRb7-2hKJlVdVubrvXTxPogVakVBwHL4zVkc2Rhmq0OlRqknW5Huu8tXgOwrmzLWNw5w5mCd3AUqLbJeSuFQMqXVfQ3CchHH5u--RcanPcpZyRnAR9H6lefMh21teg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftlxuU8AbiPDexzDKYMgCoaGeTQ0kPO5Zg3J3caJjHT7LdgihJYpjsyPxCbk1I9p5P6RKB_90QUlIYDDxxiGRfVaG2dt3817wjz20n5_z1Vn3qySQ2JsPdoie7iqpCag-XtRmR4HWL5aTK2ujzIGZSnQsipXqfVeGJFBXfACQ_ap5TwrgQAqVV3pJHVlzjvBS4r5I6TNhOznX5bju0i0LFNtkIJbKZlL34BwhgxSZE-TKU4JFUTZsojy7bk8KLAPK5sRVbEQwp531ncPb3HiJT9_zEIqXcHILEtGAnI2Tk9betq4sq0vhmbL3nynMjqYYOH5VR4t_bP4TUo6It52pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdeYbyAEU39H-nIVDRAYU73bTzszYeZicr4OOFzg8AHfSMuPW6_zHncEe9HjajW0QjJ3UF0d-oAVpOgDGCCB__f6_FNR1_dnpfcMh40-q5nhwUO4EeOKntvZTkvzpUhur6CcxCEZ4a78IUl14pdxivQiKNlUw5QC4WEodf6hvoO_Oe3x5xYikI01HIT_zZ0EOIvl9aPB-HwmBJHIQ97G1GX1wnIXLA-wN1-FryDjbsv6n_enDF12Zx5ZlqfqTDVG-r9cmv01sKGYvu26lgNKIyPQkHtfvaTXEjNUA7wkbj7BIB9_r5ENyVwBftCt4FFgb-KGKA_HE-s0JGFia9otzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7JT7S8-41_I9BnVq6jjjNAIZx7amc1zxQ5KhRxatJAud39Z_iJt3Vjf0S4IhHT5dFc6DhkEhHOXrb5FJHH9md5ZO5LVTQMRS7KZYTgwplEmxRRAw0NzpwK2Ate5se7O11xnIDPHBlAGQf6qWV7rRI9aAC8kWEbVq5J8T5qnqIzjm5UNWlvoaUDvCxX3u83Ygeuf_ZjK-eGl-76ABwM9rekg27x9MHg2Z2N-b4T6eturA6wCw6HNfDHU3DowNd0Dp-hLP37gT2ujU_iF_0etYn7IACXRX75d5oojiEqqBRueMFdvHLBc3lWXpWyE02GU9UZGXoVgtYTLNFUgihzS0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YhyWrIQF-u4OZxYuWQH3FgkhcVBXk6t1F_wqs7Bio3Ov4JyY11k_EWzrG9gMtRTtpSZjoI9d_52gDKJALX-IpYZ5sy6XDDw8kHEvLlj-uaCdA0xPfPi8WP9T3B43uy5T_2Na2NNt91Ckq1P7ycY1oZ7lKKRw2Ez2An7Y9HjIjuZGfrkxL9sbIPEtgbAPL8WpqulIjwD10bNLK68AyKUYYR18EaZV3FOZ_amN3rD7pq0hgdGCbSIlz-mQeO5U3hkvtYNcnjgVSfEA34OI0TQj9NdGQvxlCK1XTRpDvdfQSI_N1XucJNI1JWD7Uog5vfseZg8qZ9myO4LvQqaFQVjxiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0YhyWrIQF-u4OZxYuWQH3FgkhcVBXk6t1F_wqs7Bio3Ov4JyY11k_EWzrG9gMtRTtpSZjoI9d_52gDKJALX-IpYZ5sy6XDDw8kHEvLlj-uaCdA0xPfPi8WP9T3B43uy5T_2Na2NNt91Ckq1P7ycY1oZ7lKKRw2Ez2An7Y9HjIjuZGfrkxL9sbIPEtgbAPL8WpqulIjwD10bNLK68AyKUYYR18EaZV3FOZ_amN3rD7pq0hgdGCbSIlz-mQeO5U3hkvtYNcnjgVSfEA34OI0TQj9NdGQvxlCK1XTRpDvdfQSI_N1XucJNI1JWD7Uog5vfseZg8qZ9myO4LvQqaFQVjxiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClfB3J9pFjzJEAq5jeaWTccm8xOBdhoFqIPyaCHaUv99Rvqld2gJQfb77AOTbGnNpBB_dk6v9Mm6HJDjdQXa4SjEjgYyq9jOGJtgb0H9Z-2cgBhtudU4vyE7BB1q7HYv9AIWf1QUZeQL0Ydir-HV4Ilo0Scg5MIa1h8nv_5UN6d6Y5bbaZkQSU6gdFmGkyxnOw0BUoZapOPyUcev3Vp8EOdEruvoXBk3xEi5TELxz7PhD4xxN9XDxvQ6YTsEXcW-0j8TYjEJKCSD20XNl61oXp-9ogUYOxUKNw0QAjkobGbvj-YSIEW6iDHdpRr05vmLQGdjcb4SulYZMhwtYrRvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gfd9ziq2X38h2aWnSlZLbkIaIuhDRywPddWp9gj5VZTM8ge6O1Kd0FKXCijRNhCk1uDdTeg9-42Ef3Ce7YRBficfEi5NJGCs7zMg5fG6uv-YhYu_C97rfiOHpnuWofbPETUj-r3hYt9o7zCajE7RJp9FjH7o3QDqSsyoEGTbkRy9jEYyQXxltHHPuxH1Dbn3GctFrrKSdd8tCtrXJVV7fHMI4FUOHvjRNGLUI5A0-HBOF7Mh1vPPYEoSEtKJkYB6n6x4L6y5izlTrZBs_lieNC7fFH8Bw1xEyeSBa0hr830MArWSi4R_U0dB5A_UIa34L4tPVdQrheyN9R7TU_4U6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
