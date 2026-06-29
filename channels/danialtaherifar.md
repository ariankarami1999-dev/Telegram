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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZlLgP9I65eMDmHEgPdyl0vaTEjdw49nyvIJ8w1UOlE2dhUsGcKqaK_GpMb2N3SFYsfAodWaGiBeUHBtmnft_S9MlMmHrZehIxHaAU3kdbioob2n4zVnKhKyJsP2NljiK4oGbf6pfbjGdO0YM0KfWpco8rcFS2ozWA8tomFV_rHCUlj7BOFkEDlGsUFHpOs3A61_mAoYlC2UoSYbWkc38fY4G151nlRg7rPR9D9VcUTjUdZu0frbVeyNzmh79CtPo0LvXtkiDf0Ruzeuqd5A6LDN266robH6N7AYacpFfdTnl_PLyzWbk308rsDpHmdDgj6mADkkigoj3pa46Ugwyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q32KBrvsuOaQH6U_goAzaanidw1jgE2CC4sMFATE6v5ihL18wcTaMgq05JivbAo6_KM5BM3ScGXDN4bXDzhNREVbo-WFFzK7TgljwGQtX_mkEAQOPLCwWyT2h3Ku6pyb0ouwzYH1bqKZTQfn93GOBzNF7GpQNh8n6hq63VDNv85rBZdnZ4RGu8S2ZD6bNkO28t5mTxQgTFsS3ZbxrCE77U7eTcC0rSY_ZebYFfYyX92XVOGt45Zw6AHEpgD_v34x0gbigl80B5NqHbVrXzGmtzddY0JcxahwYHbSSd91hi8keVRROcCuT7KJ6I_k2UsMZIME0ClEYZTSNTXqGeT_uw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BWWH_pQyctHf6dLvQlkSTjdIa-RN0KnpuVqO7NvPrzk3CVWMFQc576nhHPgQbIW9k-eUNXM-dky_gyMZBgalptzAhJn9nS0xeJj-2zgHVzItzLxlZcJsVh-1Q9Aq0zcXjn-TEV2TAU8_GC7oM7Bnps5ACqwG8dMJHFD_vHfWJWcwxzPcG1ZGwYr1uLs0bfKkSuMHSxXB50lOse7zZlL5qzO4EbmEeoA9WODPof-99QcrT1dUDUwIv_JqXenJn6FV3himXIOJOxr5e4gya45MeYu6pInXs4-eaNZLC6cqy7S9s8OdmzdFIiLqgUE5CX9U4gzALPMWqTtPVwSTDWBe4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqxN5i_M07sqzVKlLqn2XIPuXUF4WRfGqBzRdeZQ1oTC2hvUWrKXeDelQPab0OX1DnczMQ-QAopXYrXJVCxPSflYsV-OJw3QzptC_V28dENUjakazXPvXuaDgEfK9_9MOKstP0x6t8WSq8Ag15vrVDjdi7wRoen183J0gm7MCGGCHOXszBvcK675X7I4KT3ir0QifbeIrESGlSX0BpOHjZNm2FBKr_EiQX-9HZHmtzlYUvlMtgvjCMvJHNtNF1QDO_iZuJzHDqqcn5hR27tukNNxs0PrzfBE2kW-9m2BMSmi0EUGefyt81771HnfyNKfntpEQx6Bsqss5IZrfnpkJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3AG9YVIpt3WFtLwBZN2-rlnE7yXjLA-UYfgrzYVsbu1HqtTeha8dAhhIOKTck2w0lSo7X7gdNWlQKCsnPG2e_QLwi5LVvOAl0WS2XRZyu-KNLHYulOkmQGMK-zKeRf2OWgd9Umhc5oD1xx8A3nWgLz8yoredJZBu6GiwLcvVi_70uFGChWGfp5MrnWbP4Q1RE9cLeS_7OnTShr0F-wUcMqer0cidghe07QPuiFJ0wSkBMVuOAtEwe1rQvJz-6Ey_VnTm-ldZl0i6auHKSaGUa7Rj8v_nkciYFhL2VtPFxdTRdzmTSUvKmTB_crTparPSW3g3sExQ4l8LTjgTwdErA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JX8HZk1tmmafebKWQQY8EH5vZIF7kn-KKqLzdCYLCdZKgKeq7-8k_jSinwMgjWRuW9XnBRgyU6H4-UmyPOd8pE-VoxQNZySN0UlaYcnC1B2Hkj7ZCJ4PM5Z_fip_bFfeOZx8KUvWDt98nBmvveXrztjwu8UFgNGIr5eWZKeYOPzFvTPX9ogSs_PWjWXzrP_xOBK2_660ALKsMk7nvP9dgX80YQ-SYgoB4ZU5LDBur1AUUp85NLxCLbVXMvbu1wF8NdhKag5oRhL18ojuBbqX8Kwzm9oGP7Bu7Qm89uJIM6GcGW0QiVHE0e8OWM9TWI30jQmWwCLX3hrogfG5PONHcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIo0hnC6oq0VYmG7LLON8ySx9y_HcFE487n13lu9uAtHuANVM-qJi5HEvgQU-JHBtcuC_trGkKeDTDj-UnYglqnVK9dYIt12Api9yAAMZGwEusB8c5b1L0Eb3rPBq4PU5gak0yaEl3VHUOxZMxFRwPfze59rcOiP-YJEMYcZQrnVAEkkYxYIRlPpmmjeKAF81HEtANCfE_dgETi8IC7EnpiW209UdNYETcZyMP1COL58WRuYPSep1AvfI8DBCW2F2tNVg4KXQ465CfrFMrUGdVDpPIlyXABX_yn8VLgIBQaCBCxMkNIPagyS-xK7sEs0jU418uYkOISmM_ezL-_oKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8iXulR1feE7yVtce4EnX-xJ3jHmfFzV58YcZqisWt6MxKquR1Bkgwk27FPRl6NG6X0fNhpG7TUw3Cc468QOPa1NI34OR9gtRx66mhKLlS4nTtikvzg5OUzaOb47ZKexzKNz5ijSpKU-nTRHDO0Wxn1ESoi5P0_yUVKG_s3oC2-_Ur5Hhn9v-lvfSMp-JIDTbs6Tx4dY8niQosRQ97NuuA10d0UEf9hpoBT5Dw32GzJ1uYvgo5puY2vUZiDlqiE7AsPlJBZ0FOxgxbfMfg2RV1wZsrUnk7Mp8oOc7PzcmWs3PhjUKoxjaEYMhB7j_M79huNy4TQjDPNztB9_9l-HEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUhyu9XcGckauX4P93n5qaoXqX5IDV4V6YVZyNxA-TaGQWN_noASC-x3aSZJIfKtF4l31S4fggir2PHAVVnThYezFKnk-QJ7wFoyklai9xnda_wPT3U5ceDkAboLFEfsRJuike8k1jPNIfxQ4_cil6bzzez2bB0hcD4uOIpOeXlzs2Onx8f9f97RLrE_mkveCWq-T0q8CdJ9WPOC3moxeP0itEY5eapvw02ESnUj-7sEtjWuq8VkyYCzPzjE10DQS7AKrm0gRfTw-PWYiTAcz9UFNP8uHonwIX5KQJOdzuSt1N28xvRxO8l1RUTVPfyuKp4CrWyM1A5FDJLRVAu5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q5vl9_bRbw8zYFTwQYRfDjWYqCpBm3v_qKhlHk7w1yiv1SJaMe5ig_uA22AQU19n_CR7eLV8PLLsm9E56AdmthXFmbImLXyudVldhtab5BHSPlCeNRODs_zKr3h4XfryGZOddwmkyB0VzTnC4Y5vTNU6jkkBNK4x5nJDH8oOGpROsY1Gyoi5RNh0xJNC7EipARY5s9On356XUd0cynJ3zzAPe-AkHVrpu4yYITwtE6qPbRUufXhCYzQ8UYJ1dKB20JsbRNnxBPi4TN2n4veNV1zGeMXVufnx_NOlpu6MutbCxPNtcwrrVn8zgEsPikBjQk4X-g27YDoADduAaH9ojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RoT2XqUrb78ROpfQx3st-0QpLZyRieG0N4nbpGlfHiL8vdPLBSQso3a1XHXOAfJ55GvIU4CAm7Xdsy-kf1Qz2Xfjxh43oNqDq2BaNb4mCcAh2AUMfOCPLfEPSPTTBAShHSMpt1KALZoKt31R9MmI6NAncz50KpZB-WaPD1_ZgYMTFzPWTyHX4p0tWE2JHentXuMu1q3DS6KlFSzDvE7fimxM0RYoSBM6M55AQilgN0L1hf3BoBwVSTc9lY4J-eqPYazfT0vVTAM8ebmkDj1YY0km1N5-euZaJngRuoOkIBtkuLip38V77wamDUto7orcreL0rz4_mTcG6sU0TcdVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sO4AGkPd2qRgsUmzq1kKclUMS2STMQ6wMOK4h9PqPlJmHYGamNARi1oIhPX7azQUuMkE6SeSoVBV19Pw3Mf0wEcj6nHWd02funZO5CsSuibiJsUxvCejk-n-X-V3zVlZbN_mKxD3GdZm9a68ahYxvLccmjOuil1h93AQ13_9joxpTbzfIPbyAMRf_HiL3dEEsi26wXd_cY_N_wEMFdk8HXocaIPQ7AOlBzpp6--KR2pWIcz_e_11fpn1TRvQ0t0iZuREst-s1TUpjHeKjFpotKKz8c7egfiMUnpUO-NM3NHWRLDx4ufQZfigzl0YIEVfyNXqZrC0WdZKCZMDcFdCig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4Osl3pdXj87v65D5sY8ZoSTXKyNpuJGF3bb5tl2llpy4wBRuVjMp9Qk0Ywa2Jh1CL2G6uJfVgVmsEWHpn1byU4BlKKVEGMADpdTnoQJyjQYQ-4pntIBD-8A1x7z-OBV9mphxssaF1TgBcBlfcwrkUo7VLOfSnk_fOUO4XIiPMyePyKOW0YqHCttL1bazq6ClvLZ1UeO_8NW_2Lz-kdYLOvKxUsW_023y7cIDzxi9qRVgN8DrC8PWfl93ltrSpFF3v621mgZo153e_ha6M9geci1f2p3f1ESaNN72AKN3RSdjV_qBbyW8AwKkG1VxRNSHm2jdtHJntH97YJdXjyfKA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=PhzWCAfa-tgbqUV1nQ8Fbg-7Wb0RDgPriqJfx9vHcgd4pYQDyJqVSmUu_63cAeUj2p9Wj-3gBMdit7Mti_C8PBlB99fnTl-u8aFXJEXlUX07MRFvLzIlodkQEuQt7xWZ0z_oiUTUNYugOT7M_sEt0lIaDTuGP6FsBvcx6YT8phwcGW6aWWISGOJf5_CAk3SKu8Z24M0w14R0isZxzPM455fvTuXkv6KgMf1kXDIMbbZRsb__XJs_F0oPqR88mz-sjTEldqMNmjgfTVYq0D3GPJx6RvcdpinQKuMTQo16lvWDtg1MwV4WmYzDi0vzyUGul_Q3dO-TQ1L4imgskkpWzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=PhzWCAfa-tgbqUV1nQ8Fbg-7Wb0RDgPriqJfx9vHcgd4pYQDyJqVSmUu_63cAeUj2p9Wj-3gBMdit7Mti_C8PBlB99fnTl-u8aFXJEXlUX07MRFvLzIlodkQEuQt7xWZ0z_oiUTUNYugOT7M_sEt0lIaDTuGP6FsBvcx6YT8phwcGW6aWWISGOJf5_CAk3SKu8Z24M0w14R0isZxzPM455fvTuXkv6KgMf1kXDIMbbZRsb__XJs_F0oPqR88mz-sjTEldqMNmjgfTVYq0D3GPJx6RvcdpinQKuMTQo16lvWDtg1MwV4WmYzDi0vzyUGul_Q3dO-TQ1L4imgskkpWzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N40e6z7DkIo611B8hGpmxJ_bacGecetpGdXIqYohH28yY8r_7ebf4ueFdYIjkEMCVsCJkAVmtQ_vd32AS2aKWcxNbXjDJj2ALZMoJTomiAlPmZlt8gyqgafVX-eBMrDZt3IeZe7z9MEg_fw2JJ4umax5JEgNgWtIJsr54KDuQLqIH_6WAIlSe0d-GmppPwLgsuFE_Epyn2Pszoti7w1lP_iGJGVN1k73JgMnPpw--VE3brAQQVWlGTqsMydQ7gOdrmZl-S4COBjbNBp9XSixnWPOa-a1iBukiJ5CI6GN_08u4CGRV_8DfnL5IthRht5d7oy7gER24ETA6gc2Q900qA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4jd170qL0VDth66au6WD0koVMHyEOzKOtv9aFV3wKeXzVi-1Cmqt13pFBeoOuF1XZenis1lLPiox1MI-fgTEpv5mHoOlXylQH15lievpCZyclFwj0jV5TT1MXUrz1abuV3BePrTI57YdXoaEOo6Fy2U3jCUswSMBQo7Zyf39H6kktWh9Nsq6kgQB9uwGNf0-DTcdk7zI7bfWiN1gchVwwknwZlMhRBmWpF2wBlz4fOlQI2p8DtElkxF-azS7OO2JTjpsaVmqyxlmAbj-I0GnkWWhHN76NcCzETpo24h_sDca3_YyKbDsv-SdSRxlD4YGDkwdCO9PNw0-Q0IjqAIHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HsCFJUhzuMxInNx51sFJ8UDGmgrkUqzvOCWG1elfIGyG8daHAq7NZCDP52x5G57Gc2SguoUYedDZOrp9jYBGtc1eKe6YReHOTDFU2_vbxX-e8Y2xALxdTqglAXeloiNe33MQiU_dLv5ET0AMRpP5Zhv_N5QNthTzUEmK87onXiZcn15ETcD8nRXn7dkk1xg9zdeMdnzCruPjiYIzZi5sNL5lyTvWag4f_OU8jkGg7eBKvns8DbCaS0iGhWbqPHZSn7IM2oRnhSFoJIKKBTsZSxhNVpxzpMGGgZBc97OTNWR2T8P5phSZBw-WDc3tGPb3WMRUP6rySL1c8O_L6x8aDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeG3Vrj-hWzMDGK5ej6qrvysYjcY1O6iZmM0zqwFip-P0xTjW9OOEHJtRLyD4yl1cq_hCDont8iQZNdSCkVaHmTNXW73vgyJD_rWW4_8FZ0C90Nt8SgQiUz8EiDPVDDgNKBqucAra108TzNBqjUZKDXosrsAnkIqmuE5BVTVssUvozjQbRKi9nm5efydi6A_S2dsZWge0DUdF-qRUHxwKksbAvqkcwebHhr3i_VTmxkaM6A-u_GJerlpUqmYfOs9m3lv2huMXguCuT-V5PnasrHUCDiuBObWUzTWtKakVCO2WOVEG08OhPeub7AkY1k9oBNrbHfpBOAItcBngrAJCg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQlx1eG1aDQYSHYRSff5H0AHGZby2WRgwfeq0uPAXgVTVlZtYYsmFQpkFlnE0VAxF4K8HX2IiQbii8cqboj5mH1gInUjvue3gu6AsTqvZ31FjDd2SXosjilvjp2x2Ih_wfWYZCUq_kWZHa2wV96Lsnbpgqt086WRLtTTm-WijdbaDMflBquJZtFn5h714fyk4G7QGVzzfG46VDuug_6fJ1129Uo78ok3s7XKnb1XXDinnXyNv63szqd4Xq3xD08IHa7fO3s5kOGZkze-bEY0q9C25eh4E-moR6NxExHaNJxO3KrFGgtwML-Wz7DDkvz-kVqJRhgs1aAvvS6AtPfuPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iizngaLLCJRJOzvCwjE2DmPMjm9I_1p8H6nqt7ILe1SosJzQsaQtPqJjraLeyLGQtk_NuL6qmX7SF9If-n53JcHm93YZPYPdnJ1ILdrI0fKl_Wi6L96IALnw7zrvPKx1W7qOb6Z-2UE6N-havkhfEtwWuMRyeM1qdZdm4EB814bISvfLM8w0ceSzbHQYxR0psJZeNfTcLN7j8DL8_XO0uePDz1JaPYikuNqnCoDBDZBnBQ3S3r0Srp8h0jlDVF8OGYeUOM02sLQcJE3Fm3GE9YnsG3L1St1ilDmDhI8lyUKbQodm8xMdPFPMox47_WfD6s23iW-9DjsC5r0PpvY3aQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PPg8uTtovJcIc057lYg059FJplKDYJmg3TYfPbEkwBk-6STP16HjlNDUUsmuTsX8c_vHToOuiPoxhKB6JvcxPLvlMt0Vw3DwoLfw3ISbRdjL8mx2_E31iCii0KmFgfLsDXfy1BE37eQCp9ZsUWq3TMlVUerK_xIDLh1SpCBd1VRXwpU2WzQDMgG_udqNipTaO7Ux_JDaTAgBXB1yEvsYtB6DwZJK4BLfxrBKyMm1ZQukLSVjW7XRH8Ys0cUIH0HK6FSKeW4Nb2LAdczB8OR60L4-4p33kEwB1uY89ZMmDrHqlrxoLTToo736ArtS07gn9M1e7vyXsvSaqIFqR7tkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGfyQGF-WTJTk4XDIOCX_9RenCccccm-oBxscneDu94w_OHcNqHljPRslB7U5qSE2ng0AdbhxiFAdhvnsAh8QtpfClgGpG04B04ehmpuwUIRTuNPlAv1breEaCsR_fZznPXYEIBULXMDvd1NbzQur9A-psIo_j_D9lwuVpLns5-iIUqnbxf4UtGSvXRJrw5MJvHIHoAH6ZrPV0x87ekfPbgaWRseOgXnaWq9jsDskVNSdzMUCxA8ExW2D_2Lg0n9EgK8E5zEbnzvRDhWBFXVSI5eViAFgeZcAuOIRHW5KReuqDjDQBOjZ_uzkBXuNhtAaMeDS_PT99T6eoPyy-6DDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlHxtcW214dzTIQ1goDMLxM7OQnqe1F3ESWdW9h3NqnmYDM4dopt6FdzTrn-EdGgTQuKv4_GPp1hSgBAWh--aMckArcYJy1Rgoq5OdlLlF6Sdm5tP_BR_Jmx4UjyWSNyNHsj63SZma_uyz9d3omMw_TpMvrcq4eHdzvriKNnTGyt_syJ57AD5YrWxcjPavTycCkBe8v9cbhg7-47v1SNW8SSugVFqRINU794gamsB3xIaugRJ15EBvGb9qovB9AZlOws3J-uuKWv0TKXxBkSXsLN2B1aVJ1zfaXL2lXOXwj7yBsChlLDVl6_GXSnf6i2Luum7xL4iBK6sHhDvmfzFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGSmuPAHLtnxwiW1cffbdVpL1Ep5bLbnfTmKFjjFe7stcIXT6Eh1PcPYW-FqoEgkRHVSHw-PHL5QkIdwQGUQJoq0uhN6AsWa8TMHzNmhEZso3UH4r-x2XZuaRQHe2oMTy3Qm2RtO-NEB5dWRLyuEGn_829CYC54fMqG819UXmcc_mErwXop-mVsRz3poZgNHOPzA47bZ2dNcqyqYp8kMj52Z8qbCij3_C-W8e_b6sHu9ts6jtPgQTwO1O2NjQiE2Gni5p47XWm9kVr8qcxtymKdVuri-I99MI8HJ1TRDBrq4FBvfKtM2AoTCaFF3A21OxozK259zxpGdaAqHFur0Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_PV9Ggay8BDi57iM0EKi4f8NOlCuo33J0Z_2Bw_w0BFNyod6guAmkdFbz6h2f5CJjvIIB-UhpOv5Df34m6JxbRxiXxNvFOn-6wwBL5dKkGCAFr4XQD5iuGZiyjyvSHpY6L93F_4md_EKxQfndzS-MSwrWQxmu67UKBb_ovmo3-pvncA6uE5NyBry4La-X_FmGZV2k38RMsvZGGYXmU7ngM1Jdrm9c8UkE54lNjIqra2vHEDPkK5Jv_GamWO440iPnys_XSnEul-r0d4PN7cYJBcBkxs6jb8PeLj2_V2tUyy7Rk56R74yo3472J7zgjlhHva45ObMQHGYyRQrqCB0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoWIyx9DprKuz4i-q9BHNBUohXTDSA7Dt_h3gC3qhTUJOSTDjOfFymcLPLI2Bfem4Dviia1pzgb1X9Ko2BRBvLz-UPmrpmi7BEKnFIJ2g6V9qjQ59A7_FqOR-rR_1yECz-ObJGVElLGXmtHdF1nuJ3HOARZ-zRgmx79zwpRnmxPqj6Ku4NLngzJfhZkvxZuHdB_Y_P7iuDs6C2Ube6uR_WY2oybXYIIkt0IyXzayVdkXRsYTapO2OoqxD7BwCWWvWGmQK204CnobE_RJbytr7NScMAkv4wCeuUAjg_lNXeCIJyDL_OJw8r6u-RUd4teHAqvCsZTmemdhwQMb3f6ARw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-Q_7zzGQk8I5IBoDhhP9mvx0Rz6DjKaMFB4i42iym8xnCqfD_EN09rDTSfSYLwONez3Ovz1N6HtvttvIdcByOqQQE8u7isFEc4uVPQ6vAtqZGFHQTtk_MFqiiaMlzKWsPvUVsoEyT9TvVHHEW9JStXWg_MRxg44h62wW0INH_hWzCgnmQ_eLs_2-YRVdHSySiMALnsoZ_kSFLYNLDnP4IlJOYftUPLt6Z0DVCS5LV56z-hihEGnfLafrSwSE3dcIo_keDgNQZmYRdASGpIYwoXTUV-23hRUKfGmWXRxDuWYNYLgbeIbVokDofoohQpl4JuAPy8O8GNRWHIy_fRGwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3RBergMnIQlkszYoC_3ksVPQlJNlLqaTmIQEgGKSbeD68N_dUBy6_ZrlTZv8_PLJcD6ptuZ3Bjp7FTJ9bzY3tqrtpgwaEz1hbgaM3qXvV_NQ9x3ZrPFEOh9So1ou8vSwihlg3tnM1hvzp5-LWfcznjOytf3bIucOrTzToeuzLNGUZ1zp1ff7TKyKu9RyEqr5vE0tXYNvj1zDJfs-jYQwixWsAGnBfJKPDjSOexvWSmfI-kY3zlHAHgP_wcQ6ofrjA5kjYj2SytjdqxKOOb9LjTrxwNkDh9q1Rt3dXJUT4GGzTD9tsm7HauMUfEXA7la3pXxBYY4fzC1ilvXMeqLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7h_-1tCrEqKHuwTIrd7FQamEK8Bw7VrrEhIt9Hi_G0iOmdlPCkEJ299kdoTiBNwdDk2hXd2tPerGbn8qo4oaLxc0FDR7aToaY-HMd7Sp3iRtwvscZYXQbZRU6930YL846WZa0asDYJUKWzpwY_-4sK6GRAbnhD7hh2tPxCyG8fhj-7-447Ut9QjrTf2NdFDwRrFEa_3PLJ_v29NZwx7Je6erx0ewiiEGU7UTkl6yPWfkuKNaKxJgW8NH2HNJiOt49fTF2Y3RLw1x52q3Yh4jWvbsQvbBF8tGQ8pB_g_s-qpUb6LiOHuwxWVSi2_c1-uxiQX_UU-7TwHxmnHGH0GcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DziOXdBWj-IiZmt9qlBLPYN90U7oFKJ318uRq0ztgbyWLV2qf1NmGSXoGdOlcxPHwdM_qhr4BLJe8mdu8ASdfLfS-XvCJVse6o6QNiW8H0j38TXCJe6XpgRUXA7WWh4l8AaCk3z6ITlR4gIh7QCZtMMpnsu8Vqlwwz4hmy4JRhalW9eTQ8MxDj7cHVIoMH-KTTBuRsdlC4ciP2aV-S3Vhod0jDTOfuMBAvreSLzfHoQSdu0xcP2FUEO3zmhWpjDt2bmSofN9vC2LHej1fu-UDSfXii0MowZElo6UJVhhFyevm_VAJUePsakdcLmnNKQYtyk3s4H43nJZ4QNiyw42TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_EMYHJALaG900SKN_Wev3KvahVQAtmFKrtVMnrWjsumJhammIE8o7U1u_wrXZ12EuicovpgroJnzbEY4OpGzX6jG8iqSdNP_a5vAgYiQyKG2d6bXKi_rK9yDtHVcOxkZ_6RWasMq21t6MeSgy4XCePJCWweOn9n43ofFEuvbhdVds8kRRmodZYVo4ClNNUMS6VNNZhw6t6mWApfOTPHiXhC88SR-VnUpkzYSis0ocY2WvqWW3wEKykUrtCZ5poTIn7oMienKRIHYLpGWFcGgAdidRD4uIuQutA5NvVFy_N6M9Olfw-CO8bN7Dk1uPFbfvepXQ7i7T_UkaCXbT9B3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6a2oyT-Rvl_gSoujUrCHyjcmA2oIlhfv8TNYE06AfP20EIQIO1aQ9-s81UlhD91DOoYWOPtCHarhpbNBkAE_IjYTQuCmaJDpto1bqdJUela7eVajeZ8YBfOgcXEyYc7DxVfaqhSlFsi9PI2xuMFC4nhGXZgTGQG6HpGfj_nYBUNPMWloqn3CBmvR9IWZCantAW2UER6mtVRUXpCItIyjgcHxd7xLpPVU2KN2LGamoLdK0ZLHDhq_TMOQLtE6Zfy52RuINDHKq_iD0syMT-SgX7QK7SxPNmw38nKuYjqWPpLIA7ES8pISZqc1BX_xCIn9j8nld6oSI97CK_5RfSA8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjdTWkYzU-W-WuQkOt7eqGqx4h6in3WbVP0SPeiAMsrLTenhkAtybR6pmkazdWUlzHxehZ1OWPHGx4J9-8pxbRDQ2jDoLU-krHGGuDMGKR7WLYXILqLrDWzaU6xdkPoSK78Ha_P0DQ9yjBpEtx2-Xkymk7jVSyTUjNTO885UxiVxEdgrYFmM9vH2gdyadFUei6gTim7pPuAUkWF0JpvrrTQvE4AO5UmG0rGPp1IBduaIaMor9_RpBwOaF6sDrtjm1T2DOuLHXZnJFXS8HUhWm_vPO6DlsRQ2dq9XrK5SePN2Z9XGFj8eh594k6sBwiMaSsXcyNh6Tsje3_nnKJ5r7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH8DPBD7FKOHJxy9mw0tIPr2wk9XS5Qgp6GZYePCPZ8SYHgd4mKciPc_NjTcpxZiczNZpskFtTRdAUv4SYgVU8QhFiXNKLIdgFPIh79lJYnpPyk2PJIj596qYVgna79E8PLW6fbwSciXdHrAKx_SZRyXx-9_N0G1cq2M9RdbinCWsgxTRvLKo5oAJOnhd0CG-Bg56SyMo7NZuJ_v0X4YWBGucWiOW1ioX7gEENhuP1YQr1mTl3UOyQQP4pOiyEU_S0VAbOCgOf6NCd3kv5JUQVihrrg-wlejOZNSY5clHiGujIUpVVXwY4_lbQRvige_oTMtOg0Ijr5rJo4u91QfEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFqQTSl3uIGW2d8tj98TkRBrf5mrrNrS7K_YwIoqy2msTJ-5IMPPRqyiiFzFGfW0iXAURXNDJZJn_0V3J75WrhBw_B0kT8sgqkVYxBN1TzuZqYfVSdKnDd39a8L3dBMedyEKHqBNed2qD2N6ikbD7bawdaUD5ZYeliz8SepP2_2VE39I79GefVB2qnj1bV-X5QVkrFn9UHLS7wIzE24z4-s8MbKMs-vvw28ylftK-3P-AYZuDdCNYHU2Qb_0GxIaH26WtQtysiJB04JDqJyp39YY15wwT7Mbp9lEHCMA4TtvIXWRgx6PnZhO9Sux_gr-8zUxwaTAH6TPR9h0eWXpmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPZzs_eJLIOR8S6LuBROKnPjFRMb0M5Ek44v92zIjMZ0ZiMynxx_mWpDFQL3Y3QGokPtKiK010957-t6K7WsVwiOysUQ8A0EL0KpZP8vTLrYRSqhfcUqMoeYCq3rUkfcY7UYC2fDFibX32LIphrdjsK69tv8zjylRNCpqdtb0O9oTgdXl1NptAFGIh81YyK7AzepDKNHTRvj-ty58NNqcmV5IHi7-9yCJ6UqAhPe37i-1KRNdbDw35PQTEuccsTO3ikyy6p0y1KM_VF2MLTtunYTj90erJRK5F8GJ4f9dh_r_csT8OdJ_oUsHKEM2Zoc-3OEzBOCO3U3S6Y9b0yhrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdeROBEuQPXhRACFu5iTui2H6Cox4Piz3StjPw-sHtawq2UUNaktDMESFfHHA80w0_uqKmz7-Xb4ZyfWMp3HBjNgBJP8Dbisx1qDRVmJbzZYsIPBMsf0jFsRs5BPhQzZxJRVzw1ky5sqwb3peWD27gopiTmEzHKJfxf1BmBcUbxK7HdsBi1niANORpiZ6lXv8UgmYkuL4L8sdEibfDiW4bqvQrLQ9DZVJGMM03yPKr8gGaxlg5Gr-G2fzakhBShvrqtX92CCVWWDQuonKk7CvS-FvG7FGMhRZf-yHSGEfnKFke9RJyWGqPq1yfvQMgQUxODMv5H_OiBjJhAtLS_f_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDGdW9hNvvBHWgsBig_r-dZCQOrdJ48HeqjhHbopgoFH7KeVJ4UqRZ6GPxK2U33hgGPOU--DZ6mXnZ5_KGj1AVDp6qkfycOAKPoGY--aH1kWjNa27mE0rWBWBTH8HOF6uq9CgnodEK0v0EzVPC5q-peAYPBToEY4ZGOYrkHaSdimIWBmmql6GJo-CUuGwaVaC1RHPqfqXASY-Ya_8qF567cTVznC7izdjV3dcExeci38s2-KXyD0dogKtHezTyLs9guMYhiYbnK350mTw1W1-eREP6UpzTqlNHeRdaZ0vxFqeblQ1GshdgnOlfPSa7rj42xFY_2tIN89Bc0JUv3n0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBTnN1H-ewz_cqN7UeXMPJjZqnhgiPmxvxdRpj3Hc3bNleglBVjMNB1obDdJUK4ouKDdQ9Wlt7LN2lj14c0mtgG0v9-fcE5HoSOXGX0N2wQMqPNmsf8jXEXaky-vx-3Gc8lQ_4HPAvAy9g5av1NNVPdT1EGPC9jqZ0qBqBEyT5cuuLM9vlrjPpjN5sEg1ZAXKUjENqZInMqF6CzJcIvFtJFrJs_gElKXp20aqH9zKMRK-kwH5LmfKPTXAT68UNF3KzNSC_osfYIflh65quSbGWmjVSQhbInxP_BaIhpWP9EJ62cuSu3gFCyIEJ04OqZT3Hobon0-qAFM7Nh9pktSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sf_P-g1cNX0DusgIEaGqCNwFy9S7C0WixkY6Q66AqPCgAOGMpYXiKLYgf0xnwUCLDRHOXIm7H9Y1B6lgqYP481EWmOgivKT6sA2oFjZO6CFGBm4wKLLwnG6wO_SBSJhC2unlfZ3NYPTsP41k3zHLagwcI8YPKPYo0dWJMS7_y0WY7Tz96msNjIUFxs7vIllqepSCe3Ycf-nP2WmpJJiOXDRo68ZfgagRNa7XeObjBfFCXjZgiu0KYNGqCRdejQU2mfuGhheO41XA6DP-r-Edo-TAIRX4vzbpOueFPAwqjctj35UQWxJwVsWBg-uD_flmv-WN-A5aZsjmKW5Ucrno3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG7NyKZYNfkIjxsuSHxBQ7XcYIRa-x9VUQl4SSeQml6pvlS22qHSfEhivPO6Mz_kWtUflWWEto3o2Ed3RvlKFHFQ4evpIxH8Cgj5XcsVy0cE1pOAWYF8g0BMv1nw4ivrzIlR60fJiHV8Y01ZWkZg24y9EZj7R6gEGy8rPe05FEUMza_ZvFBQli2zrv8YG6dGVhQLE3F_WGFdMh9b4m-tQmQm10Kt2wldl8CWJl9LyJNSnIqQjHI1c9061pTXg0OKYi-HIHjdOEPcW4QTZvr9QAId1cGUTCTmlBbdSguzIU7xvPnpRJgRfYEQi3aUTBL9KGSuC5or-e8pgYtz0G1z3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC-pqhUOd2zDL3zc418tueVr9fHzUNtP5B1wzj4goXZZ3VLVwKxeBu_aMpXvHR4wAr6nGUadnpts4GGpagJoR3t7UOHNEIqKgGR2ZfPgNzKCbpGyGLylxGAxtDPt8nYH3leKJeiAEJeilm18tGj4vJzjsawZDUdPFpGT_hWeWk2KSnhui22MdU4c9q_sqK5t8QYTb0gZ0cjOq3gDQaWdCoDQGIiQKzo6TM88Z2isnssogEiU8g5sEiOBAmf8GtVhi-atd4K7mgHfU9lkntuW5J461ibsLLfpioeQfgUvzIsHBE3CYByz5PykK5ikWZ5OYKZmS2F9eSqizc_5hRHF9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVpyrismtkiI2HJqS3xPVnFHANc4jJV0TmdIubgJ86VLGcoIfgIHm9u3x2rQDyBH_zNWpirXDXNt--nu3kC5RZUVx5ACKvLbA236gG2JrOaq6EAsy22ijRYRbQyLfMHNLHlkB6cHlIVHihSP-WaH9Ou5lViXHzelvlk-zJlpimNy3mLSj-pMeRhm4GxH63yNWC022GjN9X93pxKuozF_LIWgFxWtm6404SBqiDXJq6zB3JDy4sqWobBtVzQlHONNKdBxgFJXqhzMFU_ZDaFwYkSvzrfDOFocgHpDt5I-6RHcgLaXlUvPtkvYWhVRTX15e2hbh4UCBc8_z7kzDZOdKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khoa6wELUrFk6Bi-620GsGNJzduMVsJED1dxZivn70lzRYaSE32kCAxmjWb7hmwI55TR7_kWBoQu9zOJ-0PZpcd5ZPF3tGoIpb8ZRxRARmkEtoIJOY76JoGvP9gejGbpv9CEDFBC1oAF7wziaLeBaOuDS_Io8N5Jk0EWlqDBGfBOnq_vYUGPZxLGct75tm_8Vo67GPFswehgxyLJ6F3q5-YLaKwyqz5qa_U3kjJV0DCiLJkwUvTfhmu4s_ukiUuttkbp3FsUaRkchKpngcjrPXBCINhvEl6Yx-hnpk7Jcl3lbV0mCTWbNw3tLnX2kFz-Q3mPM0gwk_qsKcEOjf-pIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFnb9Fm1FEj2RseQxYJI72pXOqQSkanch6wtYNEWyW0IihXQxmmyTT-DijOh8CFC55wyugXwKOIXSQQdOmoVkM-6CDk26dYJ4Y2fXFTksTAdmAb2CieJHJKMExpn9jaegPyqapHZ9d64NFs0U_C08BxqS_RGipf53Lq7oknDrVl5SN8K33u3fPb7ZXEiKyA5mbMcgXFid0gn8s5A9dsMRItaLzxNpMvQn-9zontgAEKndGt_frg4ZXvDne1vp2S_ZjmnHrWDdJvYaZ4Y3se8tZR4L_0wkRZesdrbvqFkgRBs8ixvxXJPWVZLCt8s-oAxjatGeGc_AdR9TNgcjAZnCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5v8ry8tnv-K8v0cvfKwpnnwFBfmtQqGnq3FuCeF3Z5GOp9rptwD7WMP35ejdGtD7nVY174z5JXRIoOsM9KNFap7aXCepycPoBfV6Y6_tt-JqNGj_YAL5Gm5fBlbxKDoYGHZ3bN3-H0c6c_kTyi-ItLxDxp9uOeYXn0EnFsweHswbMU24Vqd4vbStF_kq3bC-3tG2GBFieGBbhhwCv0OPXC19r68ZNG0Rh--9JiZ9l1aKuTmx9rLTv2l0a4B9xnyJo7R7QB2NGFLAxIzWPkE7Xnbck90fTuAT0Mh_yQtVMq0obLvEntrOEH40ULqPXSNkKSbFJCsycVnOVCFl_s_ew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XcCP61sBRJAXXmw0GPHBPtiHL0lDnIY-4C0I2_XYuFM_Oim_R4SJ3cWw0qQUTFZau_Jxz0uLYMg4RGPP4laywrbwHlEMQGJjNmhlP1oo8ulOoF-vDv1gMc0GAWz9nyxj2XzuHS-_8z4n_ox97gFNaoW1C8iPF3PMp23RAjNVShsAADEPCKpzO21_hWXRDi-n2Ar0kH54q8rUTiIq-9K-J4FnhZ-MCHcEGNxg8ifD9gur8TEZC9fufuLxIt65iSf_Y2hnZE8_6MSsEaU5xGxALfW2UtklOSn3xQu5AeqWUMbP-GI0m4v7W0CG88QFdozC_jJZOaQNCubpivPTDnmEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqcT19k9kNVo-krwq8D3PrkOFQDJ8b5EbiFNZfV5y1bYq-BJIcsIk2DCle8cW_79TsKMGLl44SiSoXqfpoIeFA6p4uhnkULl7QsBOHsAYlta5breUthqiJKZkjSzvBIfxdqg9Mq3KvSLSlCzY8ioRdX9BPlHTsrj7zM9qqB2Vs0mrOLQ3h7y4OSFPBwZRfTYYmj8RDjDRVsi-p4kx8VwigCXGwCnDcuIeWOg62etTRdClK1UoahjQCbFBqE9a-zeIQA2ZLWoSh9_Es8YvCsKtGpmQdiORbjf7tqM8d0DM2fBYpeUCVPvCJQK4dvwESl6oySBW2ppoJT2iKPwny1Idw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO17LDJ-UwpLnbYejjxljrslEovj4GUgkM2lPV5CBL9ZDI9bB0XrUN0jkRk9mt3k5sVcwm8kG48PefJCa04Ur9vOL3V2C4nWl-niTdiyCNRB4VBlNQANbxQQ6vguSDIKH1u6k3wcKxHJtmn9-lekBAhmSjxDeqVbelN1FXyKddCRdC3xPS3ouqz0C1VoH4xb9-uCy9_Q9w9XIDJQvfMKUOvzOr4O7bLv9ZhgMHAIn0nOfveniVD0FERkx2HYRkqQPOPudWUUZvADKmhqvuU9Mb1OD0ujQw-fEALdLFutYviu5slIADlLbH-iZ4CWPEHek_c-sg9ce8gMXIo6Ckhsmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGpzZfSQ8SJFlsy4gEvVCdGQ-MEHO594rsMghCufp6oqr0hyoAq9vHYXFQBVMnYhbQ4SKNuZKjy9IZBA_u7YyW_e_E-fRjYkZtwG0Z1F8aOWubW64PSHJgUCqjhmLuBU5vXRo6Rzyz1hgUR0aIIU4L-uVm-SBCxBeZg470sgH1CKmmuKkoj1WVC7j2F36lUU1bQuqYPGDG03xXnfHb6mR8Kj0ILgpeYwPccaOG6z9oNhDYg9YKGyHg53Xy-YBvlINJPEo4dibXmpf5yFEHkbNDJ8L6fKKsbB-5Fhikfyk1tK_xPUHFSQJ3k_6BrexVZ-CsyKgM7v4FoGwkfEZgSTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2MJ8rPc-6bFhx9A68uCGbymUhjF5M9nO6xQ2msMgRb_8N_gIRSgv_fKWL7BlGwqWJZjC0ehjWEeOAfps7RKjDuQLOSqVLjw85Jf9iKqP1psuXeLwBCzC9rsalG1-Ktgt4o8TrY3cSVple80xtLLqiHRpGez95Adhkd6PjiBqEmws4lVAW02mqZCJDHLfWQ-a8NS7g_tE8Ckb-89c2apJ0_VhlezOTZwO1ScjGeFZ6d559a3gB2Wxy1XOuSOV-9LO4AR37p_zG2fOd8f8y5sAwPCbm_9ha-2ChMvxypE75xh8ojS6NsfQrf33blxL3gq51Mn7lf6JAKifV3x_WsOGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT2vfIyyDrvX7bNi9RwP4oKkPIOjuemRdF_bG0cNp29chHNtERtd6LIGC2nAlQsf4S4DDqu-ISDtRmgB9NBk4Yqhbaw9-kRGgHpn0qvaDhKUivzlhzOO7sBkpwGfZktP4H75X0y1FPXn4mhnv_jIi8yEEMISELVNoezyt6BNgLOlEaM_tA50Pcwvx6HUfr7dkFsx-wPvBUGMA5qiP0O_SgIhvT52tNG1I5l_SvsTscMnFCvhgiUkKkIPF7KO9_m429zGG5ZF62fOahu09Ss9msw-CoDXILf2xB-pDj0yNtBBZqi14683lJ3iDM39gEzbZSQ7A5g7yXtFdnjJciA7zQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssxFwXr0vb5zMh9RG_u7zgLC0anVg8bHbVfDRCflsyIcjKTeKFayaRoK0qS8BFGm2dpBHr-ydUAi-ILDDoEjtXO-QXX9qnrnCtGhIbqWw0VifTcIA2ekNrru2sdU9EZbkoIDni4xFo7_n0FR9xHWnXmBa41XNrYi644dpk2z96GJn6DwODPJ63LnWf0xDoIOFbL5pjLovh8tjL4ifFxJfxKZgHuT5eR1bxY4oyN7lMSBQK-Uvq7tHuwgNSfXXKl04CNA1VwtJBYDRFD6iVsNgrRoFSIY4l-mw_eSoHRf3b6OJQbuNogYanXFQ_hy7CYTC7aoizlaI-zP6cj1WJe2bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exW4LbUUYWAbDKA3OrwDvZZmF0Ssf4-hriAmW7awHOG6hMXdtKUUYRRFHpQ4vHeZHXWmygF5yLaofFUxe0vryygdAZ8kuUH3_YQ5wXO6Q8Nf-yEDgy9XjCkQXD9hBWTZgEVCBSM8mVCNSWPb-bi6bO4tohtBS6XITF1GgthaEIcTeIx3zv8rwLTesC0EgSZbDDHVgSoQeLjbs56TfNBXU3gE2Oo8D1OQCIVT_-G4CLe895AfyGXLOmi2DBd89ol25t9uozIVhaChyHKEFQAxY4ns4Gs7MUIWvYBK3GTKCAhbbnHXeRf9-cIzC1YKMAgFj17Ff-xGjieHy4BKWh9THg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mqj-K5Lk4awKBK5roW6_7kAvekwaqv1G2MFpLV9AYlXKllnRJBmrnk1b19VPfdeiBooSZP1Cu5NojhiRqxTeC9I01dIZn_KaSWxIb2lWPAH1BpnuHcuqG73Uwr66pP0fP1VjirkOUIE6umhgy9feYntSFjCleke9bARM0UvJEe48dFZXjtEWS2akwzQH2ejS04rSlhThFYeEdwxEOd84_VjsQXmAoYaPzEibnzc2VOwbX93UgGUHMuxA5HrlQTouzXZ4T44MluDEDPJXitAO5RZmy8osF-LYKNXaKjAALNwH4u2JEG1rwA5x541I3NzqzIMDw95kBKVQ4wGs3OnWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhbpVCSNETiqqSPLg4TyUurIRWMFwx5u_FhUMsAyJKGapQ4KP9Xqbu8lKw246px6n7Aof3jbd490c6rgldsOhgQdr6crSVKYcWxFETBdboP0hy-lp4FPyWYVpUlraP2qLrF3GTIFg868CGDSDtOuWjWcKzQw2FSPU48yoQaBL5A9QNVfZlrbtL5hS8d2cNcubrlEZ9EJ-2bxLrwLT6xU55xcZ0e4TlvlRRVYqFyw43alKmwNglvIc-RJZAtmo0yxqazXL-vz0seLbtCLpysq9UB--08ph4jDJ95KmkUQuxEx7kHYckszelcoFtExog_6jfMzTf0x-SqM2XpdL3y1cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfCwNBIEKFgF5_SdcMfjvcfhxUalExiSF-3Af6IT1tYqzU8pxNxwMCQbUF_6N4sSXP8fEv9aaI5u2CEECjILL_fviijH15OcqoxC2xHWmwr1oMSa9h1E1nAm-xnwR2VhENnJZVHGW1iyUa7KcYnNbk4g2S3jWuvdf8NT95w3VM_K5ALALmZGi1hCxPbDRO_h3R6wXv2RadjeDWZE7PEBZk5QIF_FiDszOPWeLcfCWbHQCvWC20AsVSZ_Hn43CpplWx4Vtk223A6e3UvIO4osquchP_xX2ygfAKuGRRaMvfCYZqmlQt4Vuj4v_84Gop2xZI-KQsoh5ch6Bnv-EMTMWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPprZ8VgLjHcnAGEiaZxVsbGpFior2D_s_6IN8WB98dhlUuk_zBAjIulCQhOGvYSTMX_2JOiamRYDvpBtdW-Lg6xbAojgLa0iLL_NFEKdaxTovHTCOTTS-bixfDiaCeDPCboVa5X12h-rGBE3jrT97anm2Lv1r-mEeX5bRVhq7qhRoYA_EBazArijOp3Wccvg-6LgSMjNPbb_QgdgLrsivikgBhdP7fSIc8gXhtII37XN9kapWGgL1tVm43o45owflM0i5ax01T8Ng0zhyBzYqaaC17Kk3lCUwCyW5QQSGcWotoZIzVLmVENhAGM3SpO5UCFDwG_jg-cCyflyUacvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcdI212RxSDI0n5TKxP7UK_NGeNzBlxvN4pG2ArqHq4Jjj79aPPFGRneFUVonBmpYvV0pzT4GCCWKT3Msu53tlZVY4W-9Od3Nogjpf2Wf05sPJ9J_moZ_cz7-m33rES9muV66yWDJgBOvyfwdU6NLQLCg5Sfmd6pzDjLtHlUPMNLUmg-bgJiQ1Wep95_z5AqXRBJ0_gc1hb3-WThbf1euWFLaRkUgIz14ulFlmHj5XCE0wTMnWlEBCHz7rKrfHpJH5zQJYU6AwWhSmC9x5YpnrblKLaN_69NtmHoBwqNPqovylY3o7VEf8kbAnEgmT8uzOezkm9URwCyWe9GDXR2pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3MWWOogmk1fO9i-9cVHJS0e7SKiKTyWV1dMlzX89BQ5aS0Q0WQ6oLxbh0nG0T0XZuPSmTjACmtu5Vpz7a-1zW-CjpwJCEfXhZzzTmWCzdOhMwk8I7UkMVBZXELSZa0Lm8fYqliGi9TToYT9BOEAllt14hB7aDM--7jFeTv7_mW225sQGvaEiw08SuNmnofXh9pfjq-v16Y5sAwJtwV16wpJFvo3qtV-QuEiNS5WYn3PtkOTaTDCQzFl9-gGx607IH5-9o7kWcXc60z8-8Miz3bYDKTzhTrr6zcwVMUJ4iX3sf5TU9nwUS1qNWZg7Lvt9jI8qcpUYxePfQPRqMZIww.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=SIW9BaJYsu3k-zvnQ2ksCEAKTvtaIDuwH9rkpMv0i1lnqc_69LihXJmw437AkZUCCl4hwHWuD7MlrL1Uzfm-VSJgn87C3yoW7lGk3gpMtmrJNABJwrrnsi0F1f-jIl9kYd23wFj-pWiDI__kBawqAgxdSkNvqkYorsYjEQ6VSJ6AT5LP2x-s8CcxBCViFq0UcS94WTSgmCg4P9MZfkZVbtXmvdPKmLM0dpzoXM4GBiShzQ1qPVIo15-Agqqm80MoX_7HLXPp_v2WIXUt_SKK13YVy4XIfPkAagOCLZqHrUS1clzv9MNhI4LKVx0GX4XV36BGi5igRm4IIBYIJOFEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=SIW9BaJYsu3k-zvnQ2ksCEAKTvtaIDuwH9rkpMv0i1lnqc_69LihXJmw437AkZUCCl4hwHWuD7MlrL1Uzfm-VSJgn87C3yoW7lGk3gpMtmrJNABJwrrnsi0F1f-jIl9kYd23wFj-pWiDI__kBawqAgxdSkNvqkYorsYjEQ6VSJ6AT5LP2x-s8CcxBCViFq0UcS94WTSgmCg4P9MZfkZVbtXmvdPKmLM0dpzoXM4GBiShzQ1qPVIo15-Agqqm80MoX_7HLXPp_v2WIXUt_SKK13YVy4XIfPkAagOCLZqHrUS1clzv9MNhI4LKVx0GX4XV36BGi5igRm4IIBYIJOFEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6J3ai9ZCR-KaWV8lzh2t6jcXinijXMocTwUNTWvF5EK0bOz61gXbjjDqv-pX-YiL4_hKHn23zJMj9lJfJaCQktT4FEk6QfSLqNjpbn5m6KeoFazooh_kKbMVr3bmy1z1huUjsnVw-lyr67bbQbzxR7HpeVomeF5gZfjj8KSz89PToObJP-WPaM16eGxJu7IAAxJDy3gcNdeisGiDXspTO11vJVg-1LznxMU9JV9SEjgwHB-yz1Ajto9R6psOQmiFm7S51X0pRbEGmObIKGna0Q6XknxBf0EjVMGp9Ddn2tr7hk3VH1wfsqhqubYo7C79p5dW7gSpRq2kPXDsDO5NQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcf6u_zvjt4TTs5KNwlO98thYmCUtv5BAKtpeDP6Ubh8a8tZ1HBNX4IcBv_Dt-eC2mf62kBnIWks4FSTl3YBa5pW6qZLr3u6cN82q51Eu65jON5QR7GEiC98NYwrfk1sALw2PcbQ40yq_ons1ajAE5EiL0twV065VpMRGK2nqnjy7zSnxXByxpjLen5oKsFmdlyLORnLzM60AnKyci3ucUm1ri3pan0McemwFkudGpmnoV03NMe5X0hsvR4RQPc6UspjFM_Y_DIHrwwvlv5yvmaJbpRrZiFDAcWnnw-7_brab9Lj4A1gkeBHWi8u1jme2MbnsR9kVLxQFAmpDypqDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxJRhh4xRNvbOgtPo6Dsca0pLaoEKssmpTJEuwz3Xx8POl7Ct6rguyv5AGaBcRgbR-Kmo1v28MYM586kHAW_8HXeqaPsLPlflDVEsd5vDTeo2G7I8HQfPfUvZ7yeJ0ynSMsLTTysCpx4Y4pfg90kCzDDh6PAslpEYQqHXRccS9-WI4Q99VdpeXYDK8vNlDs2Z9bFDaY1OCMnQ-2LxMc7FJKbsdvpUBvq5nqSk5Wav_eq2vd-xCo8biw18QPSH5IPjleVb2uViwRb89ot6VCJh5urvmmITHGGV1_scjvL-uUK5N6VxEf72Yk91eW2Xo0zUWM1L3cCfAH3Kgc7ygRqCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9yYdpSGf7oopJiqljXjuSwadZ-JgH927nWkzR4X_6gs2ONwQsrlHbK517sNvR8bIci7gl4NdNh0-6OB3QMk8LhER3_KoxMfjjczqn9d2JXZ75BmcGIQuymZCcFMo69ShbxCijz7_U2odONM9uXReDbvGadN1xKeycUuCcfw43fGaelLHhezG9tCPIUfY-4MNilv7MFLmo5PDAwJZ-gdpcnRPKOeV6m0QlqnccN4iZM7jG5_8frNfzP1_XgAHH3fpgHJ55JzceNm6HcIRt1zsfjBVf3ohaWw9k5r1tX_cLXaDFmIDv_m7lR0TwWBxBPHSAm4iUp0e6WA32sa42_tpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOkkEXoxC7v-LHegg36ElBJ0neNEWIaAjTeQqxfAVQGRSmAHiChw2WoTeYDFtmfMGup2JHrTVgK3gr1HCekQxX6oYnS_sf58UyGr8O59329VHNv8uqL9aVrFscX3xD2S77LhKQ4lA0jGB6xTnQ9tIuUFXTE_RBOhQdv2E_GYG5P3v9_mD04izt_5GNXKhtOR7utH3jMEwYAscandFOjIeEG6wnjjTzq-EBkFzpY2af85Yue2AkayjN471UbbKN5GDEGKObzdWgCEPxgTsiXIFYFbWJSWuV-T8W_GZ0eG16pkfElV3rVPyJZQhkzbgksdKyWqc7duyD2006lzJJMmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiBnryxVKGEqyNDs9MKRc_aVsWV2sfzdLNnBmM0KED3f0PJ51DJvbRuNcoe2KFBVHASn6d1QNnIZG8_S42iiZoLCuwOV2u4r5SJrI05wm7-pvYvSH5vj3PTl82vtaLZgCQe5A-0zIT62QQ_PO725OSFhPnBhD8vQ2U5VUFG6i7zj5-zUuibUKWnqs3yrR8cR1ceFtA00zVVB3STEBqQ0Zl-y3ej1Pi2C5DnmpYL_shbIXacoQZmNe4_Z77b8DI3GSG7JqSWRi3na_x4RdXeN0hStqqgCc_38biOFeAX4Sh9OfRqL3B6PfCiGLkjbmkh55m6GHj7PU083SsEg3Auprg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ep1-MTyvHGkBdzups4lHaWU7SL0d6QAgqu02GDVATSsSffC92kb-PTW2j-tyVRu4dNHW4BBcWhSD-zAvD7TF8vbIywjkigExNITn4fkCdgWKQXMZGUJon7TeIYX3-m4NS7HamGuPHwDmdZaCqEBSL_MD1MapgtjcyF-TqLUsTElFCe3OtTOGARtkRsi4zE35T-2-DkHEby-p7KBIN1ciwuAQTM4PH-u_V2l2Uqq-TPp93cG5XcQyqy_opmO_EpDCg1qqAqYz5bCyRg8zBjMY4F1M6MCQLa1NnV-DXQofD8alpnHBU_J90t7gz60FNYk0dpRNx-z1kazNg_-RjPuf-w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Qhtt20Ma79WmChfIzQZ6wsEtoYySXJbqE5Lz1CIhFMkbvE59jFACY2sSq1GvjEximxGxcwVQFu7zvMDTACB4N8tpVw17ghx8b3pCOU0k-0wBRuwPzuKh7MOzdbmq2DMqtFocMGhWCTvlFmsCVmeqrOuhNUaXdLzbIJfGbKE6dt4UBY_cstNB-EAKjTx1d5fUtot8-zugZmhs85dSDroqx1tJPBN3FBWUCjLEwq52zBzf7W2JMeQtjDE4eQmnJsyVzzJk38p7--2RS-aVsYL5ptsyF5xU3Me70Ef0xXBrubblW-jkFZNNXRMy7OWoVfMYQ0o2iIqSjDVveJn4hJfiYVtnZKLZDZX1_1GBlPKky0AjmclvfgmYKYjRZSnyVTAPLiL9lhsbIqnCLnd351a1zyeneKXOTxBrpj6I-0RP8A12K6l0STxplgsW3_wNFcV7FftRhHrehL_IFemzX3pjgczvIaTE1Up-BqETfo_4bVM4524yx3r3HpKkB18XVs07XtCbuSjFKXMPkkxDGfkrRYb4ZVs91D3hFHYRFeeUWGWPZC4U_CJZaVjs_oQwToN8Uduiy3Q3FCcSjI8dArwPts1zlwIGG9CC4uPTDaQ716FolE2FFy3OHUsB8VBM9INyqWtzZef7OuwSVXZs9pkokq8jypc9t8GdJ782pDF5dXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Qhtt20Ma79WmChfIzQZ6wsEtoYySXJbqE5Lz1CIhFMkbvE59jFACY2sSq1GvjEximxGxcwVQFu7zvMDTACB4N8tpVw17ghx8b3pCOU0k-0wBRuwPzuKh7MOzdbmq2DMqtFocMGhWCTvlFmsCVmeqrOuhNUaXdLzbIJfGbKE6dt4UBY_cstNB-EAKjTx1d5fUtot8-zugZmhs85dSDroqx1tJPBN3FBWUCjLEwq52zBzf7W2JMeQtjDE4eQmnJsyVzzJk38p7--2RS-aVsYL5ptsyF5xU3Me70Ef0xXBrubblW-jkFZNNXRMy7OWoVfMYQ0o2iIqSjDVveJn4hJfiYVtnZKLZDZX1_1GBlPKky0AjmclvfgmYKYjRZSnyVTAPLiL9lhsbIqnCLnd351a1zyeneKXOTxBrpj6I-0RP8A12K6l0STxplgsW3_wNFcV7FftRhHrehL_IFemzX3pjgczvIaTE1Up-BqETfo_4bVM4524yx3r3HpKkB18XVs07XtCbuSjFKXMPkkxDGfkrRYb4ZVs91D3hFHYRFeeUWGWPZC4U_CJZaVjs_oQwToN8Uduiy3Q3FCcSjI8dArwPts1zlwIGG9CC4uPTDaQ716FolE2FFy3OHUsB8VBM9INyqWtzZef7OuwSVXZs9pkokq8jypc9t8GdJ782pDF5dXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBxcj4okk6lwRvzrUtxdjK49jCPT5Fb8uK5n_Aawe7iy49h5zvk1vWt3oID13eDtiIe5ZRGVyRfR1Yyt-4Z_aXvVlbsLvzb2yUfXMp3jFLEvyOh5GLVF5htmci3m7ZqkGXRhgnnMtSWULkAbb8rJnny_TQnIL43CdIWR1ZBsGNllLZcGSVZ8Svi7sxLzvjm2Uq8SObPQrsPP7wMWgCoAkwPqu7eYV4e9HX92i8rrOCoqyp5JTu3c-sC8c1TGdrZngcQDwFiWhCwWu2TNQGDHXfOmpLIo2MNoztBOM9iKCUsJb1Ypej8HLhEWrpa8FnO0niNdz-Y4dflaQ236mmWBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSlIYiG76zpohmhCwaLB7nMLjU6CIMwxyLUqD1Go6mAbi95CbN4fFf9QCzL4XA-2UXJzKMDuNKniYiflUCFWF_vD5JN_4bz9zLnOWsFhlA6Vm5PFjJ63cnLJP7tBbxwAxTp44AVAnaNjJRJnnDLa0JHX8K8Tw7qKaegdrvu6ZivMJ0D9yZjrqsNUCCcKmLKZ0iQFG6IYrT62SfxWEZ3QVvc158cJI9ebGVj5XV_WVzUggG7dbfftpBEWQ-uLvL9DAsV_7OnnnYcohDsHtYYIINtdW3apHOXJQYCJA_CEi_dk9OHa9DCY8pVIrPL_5yRV1FtJKxakZpKgzzC_D2pr7A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWFnjyK4Sdn_v5GHegJxpZcrqljLgQXgn23n2sVhafuQaYz-_8pzmVdvMfoIHo0zz8gmQ1p2CfTWLx3agpcUmWjwP_P9oBqQKinQvz1ez-LqvUcc_uW-ATC2raQw5J10IxX9ncWkJAkW0muJnxJM0WxUvJEpJAYS6KlX97UnmMyqUHCMGLkWtwn10YbcGi-_ACvMgF5hPNVWTmU4yROOx8UF6Z8mopRoH4_nPEoybZECDVPtnrn8_E5gCFL6ivlHNncAXE9V-EreQAEcPOV0DWzYkaHctC4EF0GORZwH112Lfsin8rXy8GTwyon2dmQKROC1MKdn27UQUlOM1a-rgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvG47inRwiaZ9D0GcdRfiN239BApkdIyuLsQvhiLDL-urxzxotWBLNNtGh57crA5qeGXjpu2kSn6Ui0Bmr62hwm7u5K2EB00qAZwH1tvFUGfa3r9mkbcFbJvMABkfFMHB7XH8fYm2l1BzGta8N1OxLlT4z1wDyOeU-ft5lyvlfO4lwrarXAJBRl4odz38HZ_RqgbxmodCrnTz4RFjxCPceCBpzWDEpW4NFMmxTPOVwdh9BkRx_717a8jSt17z-1t9MWptTmYKxUY_n2VrwUxKZR58MamcUOk9EBH4FkQA0IM0WuygSdQHqY_7dwPrqfrrRqkQIMPFZghcnfeU7Esgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AyX2kPIm87rXK77W-NRfM8YnR28t0KJFdOFaJlQxxTTa0gs5_CqMeAWVPxOQWgM5w8EuKoxwaBRXyNp_aahOGHzKdB8AumDjsyTlGzvliGIPt7PM_vXZOdIUJqLRw7pP8Hs-HS9MskuiyPDBf1yRd4NcEhotXmN8sUQaLpBBMyAhwV4cHmjV7Ej74k6wcX_rhOFcq4rlE_ZTJr2A9TK23xYYpDfzbmA6eoxEUkk0ILkMKpqyRwV-SlKra1N64Y7o2yiS1nqvSimQw07FpdtKvodtqo1NilSEofYYbYLLhq5yzqpvW-pBFThLU-mQ34ikWYbOFx2FHqLV6rRSzRUtKQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0U3mdl3ZLPvdyxYAOLK7NA2-4vur-mlkgv7sK9dOLrDjL_eV-Ue0f6eEHuMlt6rul_PO8WKNGIsSOGhNvkP_Sp9MtRm_6iiIq55T60vyLVv4m6-BgV_aJrC2_5pZ82r1xyWPQoCMOOaIlNqORrw_uRc0NkdaP6iNC7NuMn-4pfT95ii10yUSZDVjJk_rduWYrJpPVR_ipr1QdjJBi7Wz2uh_p6rgDnsxCXTw6KKFpiwFsDN4U2j2O-1ruRSSfbgU__W2gU5yjK7zuc5N38LqZj7LEUT-TlDJPGQjAzYgnOsILSENELW--kYyL8zeEjUelmhAGJiLc1cAMYEV9sboxr4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0U3mdl3ZLPvdyxYAOLK7NA2-4vur-mlkgv7sK9dOLrDjL_eV-Ue0f6eEHuMlt6rul_PO8WKNGIsSOGhNvkP_Sp9MtRm_6iiIq55T60vyLVv4m6-BgV_aJrC2_5pZ82r1xyWPQoCMOOaIlNqORrw_uRc0NkdaP6iNC7NuMn-4pfT95ii10yUSZDVjJk_rduWYrJpPVR_ipr1QdjJBi7Wz2uh_p6rgDnsxCXTw6KKFpiwFsDN4U2j2O-1ruRSSfbgU__W2gU5yjK7zuc5N38LqZj7LEUT-TlDJPGQjAzYgnOsILSENELW--kYyL8zeEjUelmhAGJiLc1cAMYEV9sboxr4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOoufgGjGreg13PYfE67o_fQNEc76TztVW4ahWZvdBgM3NVRCJtE-YMW76F58_ki2U9ae4lwRGxxXz5VB8P-7cn3Mi3YtbdzbLDSRxshfKbm9tRKx8y6s55N_46-6m3z4Qvp7SFGNEho6bfsyIZNdg7dApmPQSezTvOH9MkM8y-iia0A0HjtuysDT3pQimX5dU-wU8oIQQjjV67E5_972aGQ5pgJEpepbVfdYVOwqNw997QnJcaOYN0-BwR82zQpyJv5gyiwrTG8jIyijdvgF8enZac1D96vMI4OiWEtRGMHU2bh7rH2ObdDszj5OT8zztcmWgktQeQ1n0xDRH0abg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I483Dt1K-DViujdmwu48sY5z1xKtgtkP3CRNyaFRGC8pfNaasxfDhdA04gNIHGcLBbQCVL9eHpRs9IK9m4MPplnYW8Hdk-TDgOxE-tjYh5e-3ke4oFe3JlQB6vokRUqyy8OhiQ8drmgFSj8k3uH4nZvZ5SwNvKvEi24YrffgInqwSkFtu8Sqy-ttVgNcbs75gzWBvlxGNKprecPTTC8J4OqsDdlkxZahQPJUGEqZA5eQQf1LMk5CNA2B4J2YfpA6e0yHsFzVWQ90KKf85-xPetVJcf5a8V9tmU9ISU_DenVvOcOc9f_V1ri_TyvasadXy1fqzbrlKLQXz-E8gQrcIw.jpg" alt="photo" loading="lazy"/></div>
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
