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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 13:34:21</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5kloEkNE3Aqp_GkHC0CF3nULWslK3YXfEB7NxUBmZYFK1_c3_8lv17Gsox_Rj-2R0p9QBgcyqogVIStB6NaLL0aWn-_ofcvpWEVsv6J8hse_3x5A3gqRo1O3ZaAIfzrJfrxebHvnrPXuT2bulG2GwcKrSSfV10X26oLfY9GPkKBIvYGgebrcRx-iALsg457VNe1wL-NFygUcI0BycLVpwd9kdQMkRcTc7C1RCn9KR6WUEBSFIogXCmMyFxjPTuR68cQL8Wa7Pr7xsqOjTJK3ZRVfteOJnW9GxdT5TyPe16GhBV1_raaiAizYZBOMy6mkWt8-8Kp80Qw6yWtK_ABVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 273 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 501 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 637 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 663 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 608 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 680 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 814 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gm1LBkdtzv-0Mta4GzzkUCd5AFDuqzDluKOelOOeeSSfqKQwbNRkGAaabKJz20g8Ay8dLwWL5iSudejSfmSnVYrv7WLsAvEi7jJ_dTZ-91-Flnz8Y0NrriPJoOeYcrhIBPgvFoafKREGd9NRsA5dhauwI6YseQHnZwSTnkVQqaeaBU8I_4e_cPMrtJM4I7fPl_iT_bISA8IqtMoQSSyRqrHEOOXb0PWhOBPMBNtotrZCeDfEyCXdCdxhkKy4RaqQipJvbnxQ_m6AfL2W5f60FRXjmVDjb9PxxHQP8ZHvFBVPrIPQPtrLK-t3E0nEzBew87U-C1Kk9wdPnDzJnnX0aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 962 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnIaKkkFgvaqCnT1q8je8W9Sw6puFoS2DLCEgMtEf40sEPeT7b3MOY8e00aPSCC2blYLPLhYLxEm7oY4_uaggW9IOjwagN_ApSfKZoz0C89m4WdKpTFncOdcoJNRrk55-ZReJwftOZlwIPHILSgyL661R9_uXjGTgJn1o4PyvsGqxTqdJXG1C2POKAxVpioqUG18HUcPwe0bjg0DdU1w3CxXeQFv7k8UNdW4dBze2XiU0JCCha1l9lOtCgeYaNLgdv_MqDW4C6NKzW_-vVQjfgN5wyzS5TXHc11od0PvXM7QeQy-FJ18mEh8hV-n1rKN72lpYce5a_7VRo2o4Wl-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gswjEbC0Crhty0I9FU4SExVkRpVo3b1uellEU5qraSrVoz6vKKF6hztQpZ-FY0aqerB_pWV4fiORzw1CM5FrgfxL9PP-fn1SiYS67Ax_bCrGFlbxNl7qdfZKg6pZnyBNbwsqFmRLWZ2mD58zYnuJWkO8d606DsTulXnvlHR5Rjo9yKUFZDM3_P5c15rkMZhnVO-0BdshTN3fgAiFP8M4b5oqKJhRFmB6w1rFZH09Ed0SLK97zuMJC1hXQL5v4KqQrDy75Hqep-HLXdDV2Nhpdpbn2byMg0DqGD2I2fJNqEoQZvupq8BCOsoXks0xqB4ShgkX2yARyvlDQyEaKrVNOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thiKZnA8hTxeOFAGJGpbDlVIK_JFtNsJYMLlr_ieutt8AtlpU5D3OHagB8Sm-Mns34e7IJKi3ZtzxZmuJTJYIYMYre8m5Ydts7HzKYQXZl1IXtoulWgQGEZ_oapUFZkdO3EwYouRLWdN3PfDFJt3ajZEEJ-lJTbvJCdXTgeRl6dWh-NbkyPQR3G0bpUQkQrXWB-YgNJsePEZj2lxtSVcYh1hEgW8jtnwHS8T63G8DXXjCJj724C0lCh7GjahVrNCdOJd3xn3H-WeAW5mJmWQw49-7WohNIs9f0N8JlRR4dK4STiJ9M61U1NxIbn3OwjcwlfVY9IskNUCnCRhBKpemw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z57m7AHrWWaEfjj-c2yn3UcURNivmfcvhM0dO8pf-kg2m13_7qs3C5yKS16P4vz9ThCFIwGgGCtSNAbQygAKRj6JC81ST2ciC2mxMOaCC70PK-WpjS8Yq-OpnjvCditdao3p5TyYx2mwL5s9-35Mn0Yaxm1FuTe-xa3tr40sHdC8U1WZH4jrFE7fYvKqG3WGcP1H4zEkzMHYYyOzEtRBsgABDTBLWCplFGp-7jZugJXqTymR21si3uDRuzjy837Nje3gfyT0MczxcPwnOMFe8LIKn4FG4wjcUdVFmnxalymY7PGXCUtA0WjxtqF-zWk5vsqWGuY3NULqfJXiEhuEYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1dmwNWEMqF0odSLJ-HaT_2LpqYklJ8Lyszs17bmc4fCUI_l2bz3Q2dDNcCL0CcAJGxJ05jzYpHGpoTOL3WMUAjQHn9B6-N3PMyozx4Sf9iJF1-AeaFn8fR4jovZD_VJxpX8BR01XacW-fwT60kGQSlHgSI1gLXAmOSAZ_MYnl4F_cYBl9GzpUzx_XWuWHta6_3FjOXp8iioUTF5yDhoqTkiVv7PKTKQeAeqTrwS1nmwyMCyyN7l-soLOdMx43_AEPVyKH7Bh2abV7wkUEw5ywdHeSr8foKKM9lKjOoiQEk4w4E584h1_alWCaIVMQKgCbEcJOMFANc3dJZ2VJsRVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8ibtoUulbMWjk5gGmRD2_6mjxhAiDFNlFc76VPEWh2qXaPcNspDVCH0w0rhZg7n1ZTDeHGC0CLj_9QTl-BtLmCKU1G4Wp3yyY2pdAGFLkCtSrHZP5hSZ2TARVrMu4_QjRJtbQr0Wk2Lk4BYkKpvugfPqkJwVtDn80YcXwTjHVpPtcYuAmI5lVa1DKBlmJx7FEbj0hoVclyvXsqANG8JIYl8nRVk4dbaSPKnCLo98mtvxYd7cChnYvOGAiX1xZZYd3xtug9qVA_Zio6yGvS_fgxGctlQlCv_8vqQR0EoZgB1wSlJ7PI4c6Wc_oB67iiT-XtS65CgGyPj2fDzJyinIA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRn0d3HX_KFIn4w7m90FRS4ZLCiVAgvgVLbT3lQ-BRFFhYSyNSgRrMobe6Qr2Z3XRF333Ho1G0vgDSLTerNnrgthZR4qO4pisVgsLwUQuuSnl5nzlc0H8oMN8S0NCQ23C8aNiZ0XaktSHoyCQJ99vDXiqOMxeKwj19B_BrQxELIt2xmwTWOPPnO1B7otV-PcldXrgXbGL7p0HiNc9xwWcBThwP0w4PCHMod3q9rp9-PCkIibc0GaRkLlhCgHGakl0fRGAccBxMlRJ-LBIYqvJZnS2bYIzmsLcHPZQ7rxkCAreIJcgxwEoQj7U5irTwalXtl0bH6xRrY97ki3wi8ynA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgdlU8bhNMYM5V2eKe2g5LOt3Yc4IUjghwR9M4lq0ilFa9tYh0daRLM2tybLuqDutZwPip2L_yoV8XTxW4QQtu7FNtzFhfrHHnfVJASxRRa5neOqrw-BYWlTFTZcMIysLtsL4FMeNNRkNNbUIL_BSF0fTkdLPfgGaUeteA73gAIBzC26VAHD9PFO0cvR1Lb41I-9h_29g-4iOgAhHZG-np2JAWyHFldNGu3GChHI_C0WwEC9L65S2L5_TJKZPGqhx4l3d8grPrvSiaRXijuVApwd4EVn5FkdTHm0GDkusCyodYq63OHow_RWTlP-6nIlyaHv4KEJtHHcODSPJYQvmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gvu6zxFSgkrnHmjA3KvbE2pf1GwBxhnafno_ibEuAHrHUVg5PYn8ZcVagqQvzeSvbxptww2Wz7sAhw-kppkE6GYV4j5c8pqfvpcWC60ZQ-P3DOXfsGPAlP8Mqlsn1iXbqb6nDH9cyVmK2_JYOnBO2LFjOBRrNNHOtcPwtfXVknBv68UsM9-KI_0pjD8K28dtEMvNvEwntDOVAmUQLBIKc9mZCaJNwAxJi4mn7G3beLHDvhYaNH-gJ4ih-k-11HlagiHUs5fKxGBTXIP1Dqo6OcfZwt_d0iNhpG32Gi3IvVvF3FsgVFOI6bXeQAXhZkdfpZdvo-Bffh6_w5cADKK08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYNbDF7VL_yItvaf411iufUtO5AglCWdxfABhFO3ijcoP4nI3_m_Ta4ZY3tOSEwFSVPUKiYpYLIpDW9kJGa_4V4lB9HOTZto3HCTRRM2XpbKJnvv6BLzCvN0k4miJ8WZbDfBZn0wfspeIs4KB70v5CJ47kw9cpdJr-3WPRd3dg2SpVSEpufqfBZsto07fDVTD3gD_n5adVphaKBJ0WXLUAMhRu-sAMPHJRictAOJgl5L_xv0lcswuGM2IlaQF1PL7_0BqQyeWhGbnn0NM2lcgPLQfXz7ciqDegGFWLG1PSBfMQv2camw5dANdlNozBHiqg1doMgMalZy3_EIixabOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZAYJkVyfazVaeYthWmkjepgzaCdqJa3O6WQ-oo2scuF9zWdET6IPZYQVoO97D64vWMEKHkRRqESBz5FP_3fwJ-y2MJSQ6K24wckQEv_n3XsWwaKvjCZD6EcrOs8LtfrYPbiMeF1EjVmWSDJ7mtLXMSy050jSrnb_3cNXDPHYRvS4qgQ8fmFLFLc4gzegIF9KTJs0S0N2wV2aIKTAyIBOHFXPQIel8yVtl8BL8tQwVUP66zdceLSAgg1JJu3z2wOwq2rKztMHpV7___bUmaBOI4RLexSyXNBejZlpSSM_Akjqe-DKqxm87lPaKLSFno1Chdmi0nbOyP93GqpVczDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a8CN6ACaUVFEo1uA10WkJAwTQQ1EZHGYMPRnJluDMBX8A5sgohaNujK_FAghvs2hmYwG__eCOoBKszVvfFdVAaXdb-AZO_iN8HAhj6M82IetSd9KNDaD3IjQHrLZE0WdbOcKxEHSeQqph_0GPjEiPa3lB5kNHkdhG4Rzs0W1O4fXZTOVj5fWn9ArwaM8hxWGO-_6hgmBxxTn1ZNCvLvAYoywuBi3COwPsMnNZoqz5QCCyIrBHY04fChZUsJmvm_e5fdvS9DU2uFN1w5HTfQx-Dvpjeu86XjzdLEqc3MlHDOsqEOIoFKynwE3vGXq0sr04WxIcvtWsxl-BpcJezuceA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFvssLStVEKzPEVWKV2sWs5bi8CGyV1IyZAY5pCmriQFkY5Q3RsZXADm0RCLtneeDGYZ07qI83egtVQYNMk5HD-df4yk0wlFq8EKfqy-K61RZyoRg6iMavobzOrssXMNeqO4iScgzwsSimowlrfNPGrinMjee2-xTRnTaSKF9GXYC_CIQBJN-iU8zAmM1Fcyaxha13EAqf4s4Rc4Olngz0_EBFtrTqj7vPXmzVZH6Cdfb0GPGYAOhA0rq2Y3Z923-4qxsOw1cAsQn_gdMTvyogTkJIb_NQtySUAeSvmI8oiq_sgXOKdO_4JASjSopgumZWTExb8f4JiRAzG53gZj5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=WhLrVznKOplHiH3CKSVi0Z_yx38UuJW9CgVaJ2Fof5Y8OTfIrc1UqWxyljFE50IJKEd8G7omQN3igatSCREMJOpmhzrbxD019899KzLPyhFQaY3LGOi8pBAS17hlkpsAJ8RSLmeuqnts9rnaDwi25hhA8GEghqQBzseGrAGfUtweUQ234RPtcB7Yg-SavBHbocz3yql_1WkWTWGZB1Mxe7nwEjsMILWSl-rGXMArUsAI1YvsHwjj2spnRFnYH1TNlGQD8RacKKiBko1Jk6js3a1PV_G5RJmuMpVWBku8D_lfRzxS0TOvvQptl3Ni5LbKBAIdO7f8G5J9wadJwKnFfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=WhLrVznKOplHiH3CKSVi0Z_yx38UuJW9CgVaJ2Fof5Y8OTfIrc1UqWxyljFE50IJKEd8G7omQN3igatSCREMJOpmhzrbxD019899KzLPyhFQaY3LGOi8pBAS17hlkpsAJ8RSLmeuqnts9rnaDwi25hhA8GEghqQBzseGrAGfUtweUQ234RPtcB7Yg-SavBHbocz3yql_1WkWTWGZB1Mxe7nwEjsMILWSl-rGXMArUsAI1YvsHwjj2spnRFnYH1TNlGQD8RacKKiBko1Jk6js3a1PV_G5RJmuMpVWBku8D_lfRzxS0TOvvQptl3Ni5LbKBAIdO7f8G5J9wadJwKnFfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2i8pRX0Lq42TfBb4aQZAH4ZamgqcPhK_Wivvu0FOznMXW4ch2zEDpCtMVvcPl6eIkw0JhKTfVisklTLJoAlJS9tk5GhwQxyosyHRWjrdFFqxT4hIfL-J9vPu4r-y_BZGVCU4DC27TPZo6f7RaKUJHG9p5aPuvTdvT7fiHvfTEhlt_UgVUw92gE43wixTarlIQxgQLdO67M86DY4qQk-Uews6jGZ-0Rp_5cgl6BnJpW1Od-jOdkpXbPtP56_EHd5orlbqtqPP9X7slyXqp_WCPt_67U91hUM8vQa-j8dil6_5i3uKtOsDrn3HyM_bUAqrQchdPNS-oceMxUblyrZJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEIQ6VXFEFxaYG5HMvGwmFkIBzAtCLuzywwYLrVjiMvnFtNmFpecAscIpgiHzzoyNJLSknLUIR4qbrIt3d4y0GVpo3tQtV0MtvM8TQA2vs-p7bHDo0nKQZTSIHjA36KYzIN1wdlOXf2RBac5dCHay7jX5VdgSM4HLFEoQp-jE1SOBC982ZwIaGhwgHQSXzAJ-1vqtmfb3-_TzNEllJu3sFj1Xv9aSCmD37JO0fgEuhYlQSsQcNcgebc2uF2Hx7VgCRQ5WILaIRo_oSD2jDFbifx9dIMpXl5e0jj5vgc5Uu4cO2TBjld291galQ5xZ_XDuDKiz8rj1v5a-3-sFJpsIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWjrpcsU3RSWys2c7i334ukdFyB8B1KaJw_3MUiOiKQlhQF9-5bhSqvWBdDpiQ6F2LePems4MzJEA1NJFnhC2b8cKXc74Y7UEBMsHxH8AH-H9J6VIguVyvtXAO2lqxUOt_ICs4apV7JlhRquYM7-14iEMrhZWpdVz9TDKJJNWwx7lToFlN1aOVRU2VfTs_U5vXrEuIgkoFkwk9dSkdUHkjIp9-XIpvTb14cswCNfxs2iBvxW-C3wVSDPjd2Mauq_-FtrZE7sYfUNcVJUmu23B99sCIO3Ba9HSR6GEn6BJEgwl66QOt5kZhu8Ple5JXMTRxKS_0xUmBoiVLEN01FurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i26NRwukGH_nnzkw-2y2XSqpCkU74NQGFy1VfX69BmA-VIs2qhU9PmC04b4jOETB-GlwO9uMSqIsq_Ys1QonIp25aFIDSOLEp2JFHWwdpoiraadfQT7-OK6bcpY1vvMptGDr01Rg0BQ1Pjcdj0pt8mvjxfP7hBuXXr3Q3CeI5LO2B1rYaZUMg6n5m8_U2EdZHYzJnSCJRMkCAvj0CgI7MP-9csLLfliNAGsbW-A02lwJJBpGlWCQrmn25LSXCDmk_suWRXJpYUJiX9u9zI2pt_km6tHpdyBJiKW6RMuP2v_LZmXb7A07tIPz6wmT5hgzzM3P5zZdNnV_mTGJRF9deA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvurZLyXAkarOO6T6kmI0S02JeCd63mAAEOCVmiBbCqzznptQ2BHdXRQBP03MQk7_Q25OtuAr11f-5BYAkxsmxpiFX1mlAHNpGaGSUiD5oNG5TR2i4ogHgQ_J2I7QBWOIgeCZCp5rIBMbaOWLsXwnbUJi8_NBXn5VXGvcSoXTesb7RZhppqjXyLpjOtI6VjBJ3QlAfsPDQ5crF1qpkqHqEaNdisc1HOhTar1bbZifFxnagYhsCQabIlU0WimZDvDxkKQ8RLKI18vSITTrLlXm7HwQFwoaOuDKHyLVLgS1vcExvDNR3MKR-tD9gbxkzUfFgjJYD-ZC4_8kBORfnDLqQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvNvXJJSshJ4Rcw0OnX51ZS2HJzC63BuP5AwBExft1xD69qeZCSsg5awpuNyzoVM8J8va9xofae_VYQCxr2HpU0I8umP4aO_ONkDbE5AZNxNuFODSEvEXOICNIRcZIbG3C1T6y_QtQUVRo6DfWPxF9wsi5Vepq03WQef7gg9JpjqBwFPBVJUYTpoNz_Ih2kSo-qDsP0NYgeSnEQjZqo37_xtG530OAsy63Dz6HasV69KSi2Tg0u3ukU92Irt-5vFjc5FZ-9paheeGwbX7uSAdPPVWR8ejb9A5p_7ROh8HNs4NdAMgllVK-XjPDyboS2nKEsFmeDA3O-YnwfL_ugBlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPESEPiDOg_cBeLDD4dwmDDReftYMuN-NdDgFjOBlLP6fefI1JT_4KAN2Egqx_DFMWtlkMb3hI95fSIFwhXK4WX5vUVU8gMQlOZ5onFpMOYGJ9edB9z-rnfRRaVX8RWvcUXwHUS_P2ecJCFwukg0_N9Y3l44l2vozookhatzpxM4GpG5lovDQPJ0f1fwfnLRYNI2HQXXtJ74ggO5cy7xdAM58waSPdd28TZAinM17mjZGyoD8EjccHQac9V16cWrd6VEA-6kxGYBJfAOzdhA0NEhfxkdNCqoqo9TbRgHwzVGm6XHALzx0JMVO_gckRiL254a0JTCMJnWjN8t9SgzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HU5LEd32maBi708qQ582yoWm3ajQxkhElIwe5gm_YSF9DA0R8nsbkvXtE5L_fG2eUwHtxSa_BH1DXrIqh2u2gcXSTNt4W30NUr_KbV7WLJUJ78YVYCg69xhZTH7kAona8YHd3ApGv78mRJFil7eOMygj8uNWv29w-s4pE-u-75D0VjVdy6xX3WDdd2SwUSJ9ZY44CDMqnkhyhtq-EubTtIvKaOQe2xlmEkj9SuD4hkn1Gsb0eF42quKuscKX35-HoxfpTxpyM82ASBSis8xZfmwfnrYZMfc42ieTNiBLvDaaVQ2M1NydGy_QuQpI6V8kleXIDGgvuWYeMT_IGSHvzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0Ir2IPpi_1zl2HwT6tt16t45RDQrhcjy6ARwgSh6SpzNCGygdLNOUoselcBIThmrJ3BUumbzHTmgVo945H_r0gKLDOKR7ndNdN1EKtoWur1a7e-2bclp_SAV_34Yukznz8o5jaiGdNtBwTYuEXEMXRfhVZemdft2pz27xkcnSfmTdfzcQQguRCr8_ZVTI5XatkDlqoQ7PGBPOsXpFKxpHe-sjKpHYAdPyZPkSuTaBCF2QW22qo4Lg7Vgghsh5YUeFr3PQnsP5AEkaa7WV4Y9bVF9F5mcvHwVqWtxllaCZaJgdu9qdZ2kpgOfvUwbk76yZmL2UUiauK3TGbx4jK0GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3z_18Q3orcb4e-ijqUKtogWtLbVVT378O1pJx1molhX28bTMQBbQ9g8OrXruhwr3lJRnNU0jX8t7pKoWYgi2WFtdgUm60hrgwBor3yU8blKUSzPSj6cLZl3DrgQ2u5HmLB70dtcCh2hBF8RN6km5-OP8zcVAgZXVaP-28-O-xF-oLW0hTO4DyU2aSQOo0hFXjVj4fopB-WWvIDxQJ3kzGQDWH58hr5sJ3nHNxHuBTj9oQ7m2tgL6RES8ft9121X7nCTvZ23twCeImOCCzn56Ywky9Wy8Hj-P0pAxEOlYQCWSgEhtjYZzbDyKOiJYzRr7ANy6UXRi-vDBZdAtY_NEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTLUg3cc7FqfMj1I3lglYY8ruXKTH_2JzcPXJAIXt04KyZ5zbGmtgHYWEIcULJORf1-qxyMEMVAmZlOrIIPCLed9hcpN4MsGp7Qcu7djGg5n4CAMX24TGD-Kyk-Ks82GtEMQs5rEQFm5LEtQ4nN1ZISqVQ5HbOYQlq1nOQ9VbuitHxd1UOhCMaggwVr5XA5bMYTvOnS1s-glIDJ9TZ5GkX1cyWAGJXrzLp380iETOlz4JwxLJOE1_8zmTqRKNYsIApiP-C7_1RyGOQBr7VxhHK41_89Ov75ZX6IpxCM-HZ-R6XIJjuQxUYEen4JZv8CGJHR5DPWYVnfK_aiqU3ZBiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzprI01yRlVXbp1Eb0V-LKNhdXkP3G6ZFDNoQdAeeI6U2uYicKexCeFgGrJkzYfCJpNQKCnSWQJa_srCkWbHRT4Sg5v51URUjlyJC9cJLtUaIEWw_5Jc9FwHUOgOdr-dxeCcMWQj9fFfsE-SHG7iHR2GYtt5jZBQ3t_5OlM3faIDRwB_Y94NslD20NfBISncG45vjnA5KW5F9wprlOud4Au3JbkKMEmP07TmdYdmjT195OZ_OG2dLTH-HZfzI5pXcnWzTux_BZ6iunT5Km1Sn2JPVZYWhFjWccJkWg2IBUuJD5efi6k6HpfnRT5CTq0XEUgiKgPgL0HUrqYG54hO4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBQLOcd_bfM9iZFERGkQwYOLPgfRwRFuTEHKkuy_UcV9kWb5S956M_Ouq9wGc1dlfDbhtRsqoZGZga0b3cGa2fcijxf-6Z0mcdqdCgkJwx0hoFQvLUmU-OTFHnR3k4ZNYzKBqQ8Bx8CBx3mG3OglWUPP53o5dHu5B1BXigALIJYIE_qphZq2nCT2Mmh8pWlVHlQb9IyE59jd2k4OuhzWE7HYsTyZqUqeAY5VIModh6EQ1PiRChVRT7Y2RgGY8QhzaFKKuOjE-vJjwJ2qShTTrDqjreTvPbzWzZQxbBQ9i5Scc0RUpKUjiwd2yUsmAsALGkv-ppErs9eiODC0cQeNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTphkQZ2OXBsGm86ZEIv4aRkHRBqnBLx3w7DZZ95NRBVZmOmyUQimZEIm0JLAulPq7Mf1Y30D5BZlVn-47dKNyN4qvj3-wa8CsLwnHZVL58A7B8C4rWOqJ01cQlwQshUSoL7013CLM71NyAOxAkmGLDJpg8ejkNVEB4mGex230HJMCkltEtHmFDRVE2Th34IdZq82pRsVMGXi0Wcsmp5cGFeqkz_0jjb1w67Ni9di20a3wa1KWhyHVB3tuc9hpUfz9hOCju5YdNAu8aiW7cUAK_1h__mHdSNtxj1BcdB7WKVcQDNx1_lQX6dYCXieoDUBxHNrEmjGwJhVcVaYvcR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_lfuOV6uVw0T7kihG1zszB5LU3WRNP7ZQop9IoO1P79bkcT74Dzvefmhn95rysiWKvDP3rWUtOc3XT2YUGPtEZSnOuOMU-hRZH3gm-QFzoTFgYybiVZNI42nD2MGzroE931HvezP-eDzcOWtxwtwy5QoaOvYOwSstlcym4zY5qFsN-UyBju04ahKXO5ZWqP9IoLt0F46Uhxe-jeRIdhsqiKF45nFZZzXGugbUz1NH3EecNh7a4uIy5eSfGp1trGkMcvtLGFGN7a02obsWUS34ZqFNAbSMXYC-9fk7dopWcSllOfRSjsmxD6Y8xeOkgwUPK7TweQC-UEvMEPNiaNmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ml9kVT4MQhR9pIFkZYmLrI6MYPH_EStlsj0zduwutOKQ8BItVKqfwMmZvN0wzKvDzRt45-9aF7RiqQzArdpZKBgXyQPDcP8rzVdH7xNO4oaOJm4rJqG4AsNYW2j-mwdMFf-uqUmjjDwXt0o3x7UAfWmua38hOmMP0vylB8QvAG5VWjg2g_UlWF3I9q6h1U0HGAoJsfyHuuhX_zEmQrGFownEbGd7_ddr3gxhEpSvagtY48axh0o--VJEfa3QHl8vuZlJ-jWAwCucjC7sZknvJd5ai7ucIAYvG2UDkyFBIGHMnvR2-oPwJPE9gfQsbvfV9KueJWT0lsRe9e6KUZyJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVNik002-0iNdNvS_GPLhjHDhuYNYwzrwe3GCDA-eVVI-IceYfzls4WVf4Z4iGX1dLtGwU6SMQxiTIvSCcmfFQTVZ3dQj2yBAXDJvly8TS4utz5aG0HOf4U6-HIW-D65MtYxojxUi4JGWpfWesZm8V_kaOk2O9iuef0G6Qx76TXKJCjh_O0MoShxK6nXtQv6iTgp1WpK4Prabsrati3u3GQWgEEG7WsYSOhEJEh6fRYqKI7dUNoQqz3IEe9Ab_PrdUzr_ly2nUs4EXC8ucfAMACMjrF9p3V_Sd6gaHx82F3g8QgmPCfWV8VfNQXPdPrEVQz5GxyH5HH-GChDyCORRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPPEKgKYBNeOz1uecenZGnJN7of7W2P5ZOtDiNI0ALirqjGIrBDM1cUAdTSRMCwOGpfTOjndt-M5HhEQPGZg03PwJKSWCP64gfDGNdo5EQ8sEr44j6Njo47NU-caqqz0LZoDsNEPRuNYnmYHrbf0c_HT712mvWWaYpR3ur-RORUfnNZmMJI0SIVRHdo4qn9Am52u0PKRj9WX2w1_tXGhPpjXj75xMzJ1eB0o_El1bzpWrNUdqco73vGedq4IgitY0_Pon6C-s-xmw8TVThhBC8yiStZF1hHjMMBVAax-1NoDkgfB5cI9DegwfdiAba0UGTk845bqIu1pECmBF9BVXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGC4icmjl5ptxxKPlwY8eMgku2jENXhUhAIS_a3jhvSiqea8QyXlu5u8CxkkMxCDeRGaiIzCr7k--YKY5xBkriSu_TUFUkiBeHwkeKJU-jdWny3bQkZMCT-Z7X5D41dHZEdGhXaRVuHCYt_FW0wfeZ3k79iMTfedhb-KLsGG55U6pRTMpdZmX73xoP3KQFc7FMkJ-MPiyVRX2wTr2hIfzXfaYZhlz3GC_mcza5F_pnKApoKj-Bs1IyNk3oMLvN0a4ohizmZTV3o1q6hANNiyWaAWl72d3Uxdi4NRdPh8udJ2BfP8YbqtlRd8aqa4xTEiJf3BjA6vc2JyT0fdz4K18w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUY7EZs4ZFP9mmZxHsLc4q66UVQuqS0xaaic_eXirTwGetmnr3VEhb0Ybf3xdhBwBAGaYtmso_GvRgPg7avY3K0ufkRafVvrL7gT2Av81wgV5eCIoW5MgOEaqDYCOCuelIOf0km1Gx1HsSBb73VnFe3kYZ5CQ7yqkgZNvBajPRwncs6zcKTGjFZKUPrzeq9Sr7thi8D4C6oR6JsZb2Fj2BTXWQYlUuUG6rlF3kj7nyPLGxmnu6l2_jyU7QUcyPEG6sMEsdaybLwivCMTBMmK1KS_tyzuEv28L2bTQEQzUVz3IVnHiFx5NgPAgoXO4Y0EjeIaUfmgaJGCjBHhnl4Z7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-GuSxL2okP57PURmUq1aOPldxetnJbmztJ9ITTD1c5kkpopZjuR91EQURy-w2Gn5LRPvRz_sR9sQMjrmzOESguKaELGRMGnx1GKVW1P9BOR31MymkK2UpMKwSb9jR60DSdcc1CJaZG9O6Vm6UmMabU4UAOTgA5fLbnJNnUtPGl_eCJYfuKVbDMGdo9fZdLZ7SnEs_vynT_GJi_NQE_37I3CTMBDOLLhSOdSU6DLVJowLqo1dFNKUB4S-9cLEbp262tV9kookOdNdJk9aIoi09ed6IpO2HQeRlPXulV0NyFY0QbCtUg_9hnkwK35PL8KkLkLSwSOWqzIuXTCE0r2wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT_3Z1Ks_40CZN1TGCShhlvhi2kruMwqtbvrA7qqylSnGI-vR66dgQfkz7_B5rqMkfxSysi24rxsh1sivJbNH7DkXeM6mcznGGAnSMpV--3DzSyDQvv0anlKaHiYzf-_wx9x0CYes3ntDi9N4Tc-dsFlS6xuznDsRtblv8g6MgMMbos4HkOoNPjoHY9ZbM7sSe1BwKNGkIz0VBYPdj5HebeHlgE1aB0Kl82Wjw_3n5ElKDzD4IPpLzLeeSlPhyJG7OGm19ttRVgHeQH2Wolo5Mgl5K5S-o7XgXgqhTwPCt7NUquGlBwA-Anyr3YOMaLDt9iTHnDfTas8CAU6jpEYmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fsixeqftbm4lt1iT-j3406Gj6iSLlXWuLzoreolDePkx7VpTGfXCY1qlSQUJgl_QXXR0LqWUNxSJ2oIkAtzKQOOhlar5nLqge6ZgeDHM2b0GWzlB68b6EZmfSR98kISH1i5EofEP-ntM2_5q39GbdT427F9LW_0GOV0i_tjB9c2oa7xOkTq_21AU5q5eN2x5jqzJD33hbtvaVNub3ykDU3QJVMYunM8n2KJeo3goAzLuWMFNJfR7MeFMeL7zpXHOjMLNPEejQNimA-poyoMp6vJ0tGMSA_jW9T4j9H5Jc3tl6V5lRfMRHc4-mjpfOksNmB8HCg2syg35ewSKKpla1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQtOr-dewpY11pJzZHm362OtMBQN0e2ZpphD4q3Cq_9rL5i_N8LyIsLBAjtgwY4ND0fpgH3msCj9BSIzWxZjAQN5dKh3IFgVV4CiZ1pK1KzbLaTtpC-v9Ltg57gyvMjAkI1V-DeML-G2HsYK0nwBwkniTInzckDnTIdrvEPphuylIafFJxFJAeLeVY2bTn0nC2kgXssRHeHlO1npdQeLXUqF5Wvqa7gDyw8lBpB8KXBfszB-ODB_dCRDtszzaDW53D2guN6I2XrqkU9sNo3HdTkz_8_7hC3dUIMTKQ6Q1IgPsP0QJzM23L6kcBCd0eRtIbsqlrTupo0fpd_UHX63SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/acv1xwBqWigJGeGNNEOPbNljRUbho8wTKVQJPHzFf_ejbYfHUINFl8kIqdJmC2hO4FOKfd-hT5-OPHFLZsk5oL3dwCEbm5ZN5h0vyRsFPKdbwctwrE7qKKNsfkJuo-hN1_BgrP6xPDdV2tkuzNuS0evnlb24XjOhlZA9E1ooH4TmBQ93rjnRBvyV-8WZmiOqDxuzbzxI_CADDObp2t9Lne1cA09wFTm-BmzgTLCa0hSnZlbuhzn7xiJO5MUYaltABMha-cJ2PPFU8ftVS4Vqw--3_N91aQuQ0TPjdXOHo5RoRLtYTY2inUNzcaLqzhVyi1E_Zd9vtmpwlLRQ48gboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KXSK-xJWSCDt8kFzhk5mGdaT7PeU8EITCT1_mXz6_xl1Xr-3jiO85ccR1huQbEJtADZT3HufRVg62KnHcEPK947yE6OI6c3_-qJFl1JtKuoJrfc8RCNavCzEdB3gcMcoeukHFXXZMPHpdeTHTGPH_72IFXj6zXWX55XAPrMXwKruXrOCj1x4f1i6uQPD-2xoBA_Qcy-77nFPhrYEdECxSdm7UjkE5IoLMNFlUWpcddvgBw2lXh7sOICNmjRf_7duCRjNA2OV6A7Om6pd2AzjLAYvSmJCsHiQEQhHvKr6Xvs8EMyNvpF4-Ml8ugvxnrJ5wc2HIpTurJ7EAN2xtal_Dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qD31gz2eJbbMKdTYoak7I48-Fpm56AMA_XiDZHUUZVx9LBv1qll5P1dHLTzm_kzMYF0l_GREaRRCUetliiSRwg8uDTxSlmTu3F6FYlMTQwczmlkZ6d2EnFRFZXqx3bA8q7DLGlB7EUQs8Ot4poqepxIX0Z6eT1uKF0pDBfhdJIje1qjdHqhW24cXzAoFVAn6t2J4xo4ck-6TG0IgLfI63WrCeSN09mWkNpeOL6wTS8_1W4iO_XsmHOGeDZ5pjIHGlsWBmo3nViNhXu3BOYmvYAdZ3T_YxHrkNG0fRCkfsDB_kMK1rhnkYy6o60ZDAK9rTb-GHPoNuruzom0-VF2cUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTrfSHWxV0t7fu29h9yqnsLQEhC2be4rYUC6cSTr2kkGYtqWRFRdvPK_qVhD53WjMLwtFbkZnxKV6OTt07apdnqbDkT00L5XOeB_yKejDEEDvls7bi2SeTGE-GgXwI1ZN5RVKertF8hRdrMa3H6yvr_t0SFWxDQP-1-N_HrAROm4xkwbsFvF2TtkCIZA9NK54jco5mjsq360DYJ70yUd8jZYutZ-9QLsLw6Ybl_b6gj5ytEKHr0fGRWk79PRsCL5GTJ14W5m_1NUfNZf0XPw16Uu9x3PGeq_T71alfX7JToSu9BmqsLI7P-IHVgeMQLm1xOIPbIfrNAh8I_h_Ymlow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvZMCdQvniJ0xwqsgdCknA79S85hnv2P1_b77TL9iv5xaPZLP5Cqsh9ZM-r1pgBTdSVdC2fGff5IXw0KfT8jD6kbgVUV-luPTO9A_qFaAezX1kipZ7Iygsz1oOaDTZES7BH7fu-OBEEWHOfozUnfmr01f7UOKwM_53O1VMz9ttAN4MDiHMcnAb5Xbp5kFnBnaPeRaE-xn_Bbcl82Utjukcnxxw7gJRCrg6T8x8ysc_0tCHpQ3Jxo7Z9NqiuzEsALvmSVzDGP1y46r_ebz4rHMrdqpLs_AZ0zO4W6SmQGyAztKMYQLWsivon2tzoU3CKN5zSV0oCAn-t2Hoh1o1G1oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzcjyGNKvH1tPvp-jHFsVs6mUhXgczXh_S5F0_pIQ04p7w5a2GhMmUGSbedh_f7JRaQIRrGBSGPorGylJ1QVRUcxKKloFyofCOXgykg8eecvDq4Kh1S0tTL-pNd4gKzKDrWlVco42LCiTeeW5al3lpAGbBgDDSKflcHZcueWJaRCuTkjJxARXOKdbGdD0ml_d4nSyn1-E7mjwcTjAQdH_JzQAvqFORN6oeaWrdCsD9gjWnB1tcO5P7DePyl079Swh04efLddXxo2k6WE4TWGzXcllNs9Co2Mj5OTO-thlDica2ezs6yej8q9RPalYVOekWWBiptdZcynmWZw4LNSmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCsxGbHJ18yEPcZyyGAJaWhZVuss_z70xqWzGciKoGU7G4Hm9CCQhpN2MHKMAskhDgtEDoC-5cDEqXZYfEy3Dc597p_l6AwXM19vOCYmXzolsPT3RGY5rAiYIeNqZxcbvCraXwj4ALlJ6lE8P8dFA7rBahwt1IFRyKtkuDerKdAe9RdH60kzU2DVM-himXN5QTV7Yza3TI3KvgZlKHmQ933WcQvJSqfd1xW2nudSN_h4MUBTY91y6N3yb9eI6Ryje8sPgp4Ch6D2sbN1bdm-KoamdXM4T8t75wcHrwlTZXCiwRc2ACTcejmWEHrzN9pFvEmiCqXkgYHrKqvvHzs4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHy_I8kLUpCaoe86MGPM-zopFp8xxtflFrQuoHYBIChbLSeUWCDvqtvkD35pKA40uFyZmhHPua1Je-_WLIPaL1LdOVIB0ieFXtex5wc-czVq19U1G4dXNE_PLAAk-GtqCAFUfgt18U4wKnzMfFTTfa-GKYK8FQk_PE2Qc_fgWCgS6Yr-g03NJBR4gw3yE1GESWlemsc7eepPp_kc0NJGSJLAqCoI8_HzIjPdZlOYr9EVWxtL5XzuvrcQ5zxoxZiAGKrGLfO7fDaE3ttxLXChV1TpzOPQQsrAsW5QA9Y6J_XQaA2OOxUefxkB2CTo0t6sGtUHLf4NRn5k7gbv1-LLHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdUSKifHW_mlHMIW9yhkERYJsJIG_7idWqljUFCnTcli_Vdg8pqJunTmekO0a6pwaUZRIyEFj38fqgHXaci6zX1deC6qSRtMWriga47CZNfIYdWQDjWG4Ay6Z94iwQFGyr04ZCNde_78qirwHMtIql26E_KJL578ESPhck02JdgWV0S2gcKOS_WJ5czEPXP3Af7M3ltYdh8g3FJC3GOaQnJytHIYhRL-rmMGxVtiIp9zW9lmGvDIW03dsXyS5_7umPEmJDXGAGwFisRqeMMPAMG-3jmIbwJyRBmFKrlFj0Eta0F6qvMrwzc-xlOXDQ3_bxHkaEvv7wKZzFsPAS4O0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-4cz9a5zh8slxhgie5dUKLd1rXdbeILOtvs7vLCSZc8pYK_drNvmCM9uumkXvKbdRLkem9exsQosxtwLy1_CDau8_fyHtfjIdPqAbfgIijmBfOPQolDGa41bE8S2fGGOBCWSKHDzqbazu7vAWnqXEHUQk3PFAfLyQR6xwd-lsM0l-5e8CQgg4MdXRBWetpan-BCIdzRC0C1UwyiqZJXQEb3OJaP9OHFrYK0-wi-i7f0qihOCUzHKhSJ4-a7vl_b7uykHSN0ksxt0MKSNNNmGcKTKUs4oCdq9fyJrUVPVOCElVks-HccPajdY9VCVH4ocDTF9ZvLxm0jBYctgmXBsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbqCD1_WVqeyniQ6FwIv7ccSmk_TVnFGP9xp0zPDQJS9jXYM2Nv0GRmUOIY_Nppx_QO7tmL3Hsp1revxWGiBr2ZzbTIgIy542r6whC5KWinQdH_2hUV-S9Yn1T4qqMHeyIdKsLYN7m3zcCXOtjlC97-4EErKFOZVmyFIURCdA-rmBFML_fLAXlKC9oBIx2IAzIAf_s09Z7XUloKRRcQyf0149oHUkePG7g3N0DRMZ_sR_zycaYgum_N-1H5kDK2_UGZSnirsq9SlOv9GxoP6a37vGQ1XfykV1_jQ4Ac-9HAGVtybzYsNU86aOt9KgFhDrmnOr7NzIsfQLZe69rrHmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AT09Sec8oZDhBpYfIbjgh1c12gCiMv_rRRvNIz9uJWme1U-evHjcrwQv8zgLRmHoCBpt-WvJqMaXs2WGZmVCXaE39_yGk0g7nQzlreo2wGAIVb4fcCeLHlmc3alzEClAbka4vym_Knk1t5PECXufIjzjOULK4ID5poMGyYhRdtJvku1t47OXuqZIY58ROYRzivPTUaqQJCPgBneBQAxvwtMj6citg3XF9lunoFaDBpIdM-RbGbwSaT1aHDJPzgG2SWPmvzO-WXpQzjEyHq19gSS4du_JiqIP3w2u0wiJILcBcFTcOMzxrDL31JFSt0EmKmTcpwLT4RdFjABRrsCzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-nwLqmzDk_tgqUPn1t9w6ciqq4IoQ5CzuSa53uXG4UWwl7OzyOY8ttYe81IUGWIwNOp1yD-auCpTqfQRnRpUDAbM-rsQaCBjJvRLSoIEWZvtUlNsGA1HGwBi27HPP26kUYlgJ3niWpE0rf_2I3Ei6SJhFaMhaqEXwkj--fZABMWpsOy9sXsaS-mEXfNrIp7dHQob8KQTJ2JA55sGsCQfW4OrsmwsQFRIgIn2xG3H8o5nbC3dW-9F_skJwQGCAioq7Lp_vmBBJRa9XH1k5rxoypuWCS9BkmJMHQz0d2s4LfjHUv8PxGeZ7dnkbKzZIi6U-t2JlAvSbrT2KIej9VAuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAYyaLzxFAMdUVwef4GoCPydFOMlbaOxICUImqDKCN_nxKeGU5nosQzuN5x8dRt6W1Irppy5ykpjOtdPTDcjF82CN4_uX_BuGUx2HCoJ2NGZHYlxXZfSwr8g2-Tp1__Zq6QWMU1vQ5BO3JymWvDgTRJ5keHYKcoPmx1Y3Oq4CSkRWxQrKLTuSVDdwibxSWChLJ2Y925YmWtfLjMya_S6o9ZoNzlwjwIlv4xgeYvcXT7TfqgnjqJNqe4xh53txtNWn2pv7OIvA5HQBdMXYGwVFaIsKSGZKzCdWLgobVVQfd4b55xQS7cRlY5jb4KO6Qlt5d0cEIUrY0Q2bavSFQie0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJGtAN6_QMbMqpHRFlhvh68R2Ss-GD__BHhl6H0Y_idrkWEc5Ypuev__HGAfGBugH09KIS8Wj_NyABXjufQhy06Bq9kkI2wOOgzntUz4F6d5tOfvDyCwvRLZXI2u2_7aqfBEh95FuHTceJyyoU6CdomAgwxvqb6J5ayY5OEmoJkzT_mWPMahBYLbsBXTw4KOtAcowtTPW2mVhQw83coceuqDpXtFrjoUDAoK7UpKUAOPFzjc79GdqbmcDxW9300e1CjkZA8v7_tCp3HR46HbhfsSuyZNBa9NPfXZlhdSDrf5FmaWynJL-VX5N1D_M4ytjCXSEtVx33StRKDuGPkukQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaMad2ROaJ5sMbCoHQPftPAAewEmHsCIiX1bwuAH_WUwOfsp3hy6pfD0xfHFK_sY2FVs9--rDqgMq32NWYR4Hco9iVAeduW2482PUMEA8b2I-zF7rPQcwTWDYVYxmYPV8JNHN7hxpGe05SnmpSaRnPlAeZ0te8lKc5Nzzc9b7Ei7-gEc2lxzEoSTrHKzXf83nBbtGxanC3gBO0DO07CkqTzy-TrODXBpZZxCp-BrztsLNrDKwe354rJ8YwABCTHbfU-KRoO7I4dkKHMU6UjIFgMj6MSpnyxwOCTPwJDKVfeU0Q2KWi3XXjINt9mBbLCaYqKJG4IOt4w-yHxxZ3vUcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOv09L5gKf8g3m5Cpp74GcSIwhUqNLdu82L94kZmMh3ALE2MWIuSl4sVYg7OsNc8WCbQbRiiutYRKvKjT-vy7uJgCMecIAxU8qjN9_2kRSO33mkMLXPxVXhUNmwjUuu-EcQaT4pT8GcrJNeohFMiuI9CdyKBw-cqzWHqkvm7rc3HtlAYyljpf2sRQ2Q4tPTn1EipPpTZSGCCNx9935cTWYxxVzZEVbtudNYNx8cAeVkrhkTJcgrs1bXRkOXwskuViYWW2OGDW8gjwHFj5Z9XQTldSD_4twS1u1aHrGyaxH6D9-jjqEVIzegmNRadvYdNt9R5avIf5BrVxleCfGLvHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQvtFJiRQXqIyZW3N2aREpCwjKv-3JBlXDDzGvgMZqi6441PaXdlJMqQPnJZ3UzxMiCIvgWmDG2uInetH0P4FDPWf2xPmrFpCvaZNnYWfd0XcHk6QAzuL2Z2ZYkhT7x4m9xq0Cx02fMuAWAy-bYQ1MVnoss3lRo5ceEGKw_lLMsZ5FXa-PVL0RlOdEe1O9cEEP0BED6e-JJOqjyoX9m7TZSOBSQvKKERR60J7ko8ISR-8mt0XEbfWQhizeTtuuUhMiuqMa5ag-PPsK_ToHBDZbE5NOVu280fQn41SFYgdCT7rOIUjeL-cFzrRY53bOj5H7Vo4EfGPXK0-_1kB_yfew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2MG0liKZR74MasfdJ5D0JhMgpXkzgkkOZP8fWpLEsBlGL8hlGgdUYaPHOqxeEmTLGdmNGoGRQpy7z0sgHP9lagYCFBkCKeYGnuQhvd3hi4-IG4JjsRJIQI3CLQy46bGYatAAN8UvW7bP_cgP2nRHvI7YlC2CduYz5hWAk7BR0kK3E7stDRqS4Ba7fHqH_0BJzDvhsV4g4DDS5izDNHD2GHlSlc5fNDiYGPpXvBW4FdBuescTgm1IIf2GxlTDtaEBi-p8bvkUIM5CkFNW5IzRQC3V_n-PWG8_LO5UN0LOpfMIXbDusMTEMNeP7XJ6ZRjuZaMSFGqyaQL0M9S9APn2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMqDj3CiO2tD7j6cqMpYAHvCs073mYj9vbLx6KWvwUwSiuGT_4g3RAFIW5-KpfbroJa2d3vlxOSNGvwUuJy9e-OiWbhxeTd4prEMZN2du5h27LGSB51M5yRkXJVers2UzPRBPfJQICIPiZbvNm46Kt4mn9mHwm6Bx3IUU_gTV129_vAfjwRDF92Q5O0BbzjQKsONzZ_oXoKqfvq8DMcVtSI13okDfVObl9HPrt1LyS9KU_sIa2CU6bbHaymeYv2b_TZMhLSZtUtbxOXELLhnx42pVYJt0YVYCKvshA42bfhs0P40h9neCTgv0IlDuBMHJb-NcyOeQAXtTYislEMzXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDVB6X1HDynj39Va2hbU4BgFKzbAUtyS0gGPKtEObuFWEiXEZxKUCE8roxD56qR5-yaGPVxDMIvmKJ5m3oBr7jmWUpFUJ0QgJsKZV450jDhep32-arDt1YCRYaq2nhUwyvUTn35bLPYg3xOufmPcek1WM4axCD8WJvsQCS48uvPFSMSjEZB2y0Q3SKt39y4_quUAs0CcMZWM3VkuecMlIh-k4POxDaim_N0ELeisely6vHLJ64q-kKwIJcAnzHwkkxERYMwTPJobFULI86v4cJ3ChUHdRN4hU8Ue_hc6WLG3JIXDXccSQR3CbvxtgYIMMA6K3JdJRuC0CSfkTj848Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOmAhIKPshMM2MM-Nq_3V7uyHO8mFvrDxBHwkhZuUMuoSljio5tjlBFkiVmeLhOVqu8_46Tb9YEtdCm8Qn4bjUl05WnaVY5aEuAUus5uzVr0qCnbJfO66WUOVIRPheviYVwtjdwGTleTFCgWLclgD6NiLichjeFObr1TwF676lk6fj8wZ9Irekwv2Y0U9kXaRxxq0i-o4pJOdPgjO0j_4W7w-t4HMPJQLjT_TeCwWjdmQNiKkH6Ep6s1jgkq5XH2yvEDLlF04FwRzUezDpFXZ30xShpFxF0pjVtXVflS364LnA-dqEhq_k-QqAE6OZGBd_W_GT8QZdXgbOTxk3B9Lw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=s52hmDZqz_caitjDgNbs3BlFzMx3mgqMeVjOFHQqu8WszkPxsvUTUPxSNkOkIa6rzcWmrXekfGrAPpSi-puWyVrG7JH5wgOHTGkVKg5LPn8030w1fiKgxcJGz8WyA5dHZxf8gEzYO5_Wj-r7Kx4s04V1PXNnMW0uEsFejO9C4nf2rjGYs2IAX9h1ZBtayrHH02GBcLM0rOxUVfLDsie7RBRW4VoPJKOASRhGTL5y4vblD3tQafovSnR0eOZRq3a_ezvHhnMEHE8I9knrDfxc3cpilIeQ-lJ9NC7Z6PqXtJRMWjaugFn7DvGln8hNmv29Cj5MoswTlFl9OcwccAp6HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=s52hmDZqz_caitjDgNbs3BlFzMx3mgqMeVjOFHQqu8WszkPxsvUTUPxSNkOkIa6rzcWmrXekfGrAPpSi-puWyVrG7JH5wgOHTGkVKg5LPn8030w1fiKgxcJGz8WyA5dHZxf8gEzYO5_Wj-r7Kx4s04V1PXNnMW0uEsFejO9C4nf2rjGYs2IAX9h1ZBtayrHH02GBcLM0rOxUVfLDsie7RBRW4VoPJKOASRhGTL5y4vblD3tQafovSnR0eOZRq3a_ezvHhnMEHE8I9knrDfxc3cpilIeQ-lJ9NC7Z6PqXtJRMWjaugFn7DvGln8hNmv29Cj5MoswTlFl9OcwccAp6HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LACY-HHNjkqi4_scnt-sVTLHh78uOTJthAaIX99ROPfmBXqNqO6EYajJ02J1wsh0FXDkH-tT2WSMFXixGV2L5pzxLUv-bmHIEiQ6_XlxsCMxXOS3V0NTCWjGLoRNSs5KXAFA2Gufk7JCi2wk4czwIlTZ4UmW4ViGhM9OvFaVQUfNWuGLPGuUQ35KNFyz5ucYT5k14KHb1W6S1-wNS17nOtweZwzA7eFthrn0zfY5-o4Gl39SRv-UmTNMgmxOAJjYELOJjnHWFE04UqZdLTYALKa6iANgCbe4BE-C90kWx6mWcNlvlNOaik_dbdMS1KE2s2yuP5SA2Xfn0wJRzO4r4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW1q4N8UPBBDnpo-f5MpatOrJiEJrnxwJIo_khuvXGT60qj-3sk7nuyvrDxTm05I5_eVfJ-a6SokLvlrTC-rEp6G3ZNj49WtMV9F2Zr5uOxjs9hlEYAOhNQ4-z21Vienoma-KKhp8N5izhCquc3c253NNzw3KsT6HAm1d9r3V44TtBJQblhg5iSa5Yyku_tf1SOn6d_KXLGUumDb0qEuotCw2BTiZpDJ5jRmKX0j3LkSUul98rEC3gLwjmbD-QmZQp4VbqkTF8JyIl2DkatCfU7v057NV9cyCTF09-UlaFrjEb7_8IBcwRi4Qodtfr3hfKBCiVEH0IYKHemdkQov6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZYTCTSBC3m7o9CWYNkp77RdYs9gKR_K6aBVNQIbin6kUL_1NLhWbhV1kbH9RRfBlbwJkkDOPKCKjgtVCl9KpXh2ZE8tkolpIag7OMFfaBJhhM0sarii_9gRi8qk71ys0J6WDGmTwpTUyH_O0gHnpmROtBn8bPEU9UZn6i3kdctcLDWZCsDLlKFWxqHOx5183VxENPFZqWiR3mi3j-YeC6kGNxDm7n4-3oqUg5tcowZleWAArRuiR3oCYqvdud6zxuGsoXEkjLjrbo6O3mw7g6v6XajggNIpbcOhSYLzYPE1Qib8tCIJFS92ojEa_edNVBKQgiTWIh-j9vi3OQghGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NV6OgYRMelc9_uHncUFQgr1wV2M5bRvJi8CXXCtIH0m3D1Kum5pBHj9iS9aCAOGVBTRdVVNqvv0jZ_M0amPHjPi_RSiZeEe7REuUWJYcjyttTOnF0X-a1kFJ8UpmSQO2t5sLKQksGXcVI4p61iuQibf71h0IWwRBLVda5oQkku3lbAPUUQUW_AQgMS9bp8Ot9i475NlDua5zKnhj1-SQIwlk-FBCTtnxvM2AxFNFEE6WAWPwoNchesyaX2OGojbs6jHqdqf1QPL2L86ecliBdpT3oL_j5nJf32gh8TGoGnFeMBrVfPtREuGjjg_6uX_6YsDhYtPgFigaVar3TreVyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MioTHo3TtB5Mppoj9a-bDLu29AIQfyz_BmHD-dUV7F1DNZYFQletPViOlgRfWiH9xbUVaw7kzPl1RA62b5JR8BaBvH7_W-VFp93ArUlfJ_RZ9XWIp8Dyyf9w8RIe29qLCe0byMQ4vK4e6IYQx5SlrcoVfd04PMRUnoGW0VvSBXpwR7q584Zd8NXbvfXmoo9qRi_NetdqhMpzpeZ7avHGQBLiP1TJlxV6etMKV7uTI10S7AMyM0IRNSvN1PcfrnMjGkw5y9IXcOkaDtNDS8hfGr_Rnz18A0cdrt9JTKY5sOmbOz1Ry9pEkh0bipM3oe07q359-qBoV0DEcf2LM9DwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fw_IIioXlsboQwCDbXWqKRLC5dp-TNh-UP24tkY4WHXqYGiMWNGCHsIDF2thyKDz0xhjSOov0F5AtoAwWS24nrkBfIA5afvKh6A_hujagklEG_Gya5Dg2ib4xxlcX0bnozLwSN1wak_D84vmxK5in2iWt6zA0gSfmdrlnX6BGcD_wWAUr2SA9gzMr_c62Sx0Yx53mPeuJfvpysHhSFHrwVeuLbOFVE1jkJ6B3RJVuRHOQPSuo4vT73O3ZgmvSINmYmuTp117-utj6l52XM9Kz0-D8V5JybrE5TD6fBzdfaV_5FJTMUV-4yYs8jn_4g2tajkPDIXfEpB7yhSKJ5ds8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GaKDVDBFmqNbhy8s0Co4tzinZ1IH0LINue32AQrk4W7TXtBMn4X3h6_P--mONMg8AfusUneEeyu-6la-NN68Fpu3jvlgk-lz3Fjwhp-ZPezNT5aVmQr5cIdWiVWCtj-S6gFSwh5nqvY22K99pdllwfMmRi-s_o5Az_tGtA5-_G8iVBsNb23m_SGouVZ-b7bvvTjLKGXcGyUWO3O_YOKUg4-Z2y3LZ8GGs_PIWqFdeHvXJQpBtlwEMMyQNrja4AL1Op133iH8msjfNSinn8Nd7Ybm4tid8a83sQNjtsvwT6OOFrMx_EcZeGA7_7iDrOD9jwRTjoiSNzQZx4dNQOZQkg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=fQZHNfWGMTiPCJ9Y1uNJxowHTR4YX29hM_4yNN7tKi82jTzOznJ52T2ZfUlgsXKmY2UpCSYFSsckfOvVjkPqCpwZ2s03km72llvIhTTIO7ntXQOlEFolKLXVfxZgSa8kn2gmLSDTlor9QZ9iI2Sh6bcGi6auRxw30QUD773jfhBqkrK5vc5mgszj9C-3Zn1jghp4X6hEcCEk45nI_APFJfYyB8wSqRoRO5E3dNAlEqOr4U-1Ic5ta8-1BdJpS-KlH1-ekxOreeOtln0gFbVXHW77Z3fSlstWoUug8a95onDRje4AuEQwGb1F5lzkCpiKyT85PqAsiZn--HI_xmKcoqVRLpfkTkbt3Lejog8oi4gR8cy9raMPrHR4YTnYLgivqJLKMHZx2vSlHmX2z5aPowgBTpbbD3FgKNhjV5pU7jU8RrGuzY-ClaqOW7PEEXIysMEQKfQcXohZcpFqmvKeEgnqosyTQooqCanxQEB7Z7MaGYulj1ygEFHH6-TzFs6UMcCbU4zg_3vamcAPYxK7sgUa22w2soY37m9zfY5vb20sYVh9aUsD3F0US4rmf1stdOSxSd93j-63dgdFd-8yrD8Gudp0OC1LHnpi9wA4jJCfBz_fJvqjEA0q6wbo3vfBZxc65Q087o39GtAqsSc1jCwvpKWllIS1uw_ifjmkcY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=fQZHNfWGMTiPCJ9Y1uNJxowHTR4YX29hM_4yNN7tKi82jTzOznJ52T2ZfUlgsXKmY2UpCSYFSsckfOvVjkPqCpwZ2s03km72llvIhTTIO7ntXQOlEFolKLXVfxZgSa8kn2gmLSDTlor9QZ9iI2Sh6bcGi6auRxw30QUD773jfhBqkrK5vc5mgszj9C-3Zn1jghp4X6hEcCEk45nI_APFJfYyB8wSqRoRO5E3dNAlEqOr4U-1Ic5ta8-1BdJpS-KlH1-ekxOreeOtln0gFbVXHW77Z3fSlstWoUug8a95onDRje4AuEQwGb1F5lzkCpiKyT85PqAsiZn--HI_xmKcoqVRLpfkTkbt3Lejog8oi4gR8cy9raMPrHR4YTnYLgivqJLKMHZx2vSlHmX2z5aPowgBTpbbD3FgKNhjV5pU7jU8RrGuzY-ClaqOW7PEEXIysMEQKfQcXohZcpFqmvKeEgnqosyTQooqCanxQEB7Z7MaGYulj1ygEFHH6-TzFs6UMcCbU4zg_3vamcAPYxK7sgUa22w2soY37m9zfY5vb20sYVh9aUsD3F0US4rmf1stdOSxSd93j-63dgdFd-8yrD8Gudp0OC1LHnpi9wA4jJCfBz_fJvqjEA0q6wbo3vfBZxc65Q087o39GtAqsSc1jCwvpKWllIS1uw_ifjmkcY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdTUKtxuYJZvUYV5ExcamWU-2YIqIADS2oj6KadNwq0xTRiHOL7eMPmMg-FNf4ItJuujBbku3f3kpGEOZJHcWG_UfxbOnfBtXTUpw4qgoln8Tlm4LBM5KtHN-iRc3peHL8U-zqsLKiAySJR19Nw9z7foLJUx-PBPP59D6t6ez4DHAphz9e7_EEofJ1echmXpGSzWqmNsIC0ZbGfmyQhVeZ2UzC7_IJNoInZvYQAFZKw0GiQ06XHrOdPWIg_9WXq9r3CucO3i8dGr2HjCoGJO2QPaUnZOENM-Uij-pQOofPbGL1MO5GLNEpn4wsbdgW_SVL0D56-c4fTZK7ozDtCnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFT08qcbTDw2jmDjvOeYx7_mQ5yAOyVzHEF8XvjZPPf8vSrC1VFLUYdbRDpbIPzj3Sk-W4Ijll3UChIKBl7GbnqIfPew_l0SET-YSjBxbOF0FzvjeGymB3JjV1eL76K4yLokgAMOMjkHbyBqbr_ZsDVQlHbA8-1DgzJT2plGoZesNsnd8z7cdMsJAEv2qdFcvDkexaerPPCCzxUYYt-wp10XnFQynr3aLPi1lif20x6QA5nKqwEwzwPnMRRX_GSXap4ZxT906fdv9bBX4J1e33gRVZv-j2VDYCtyomraBTsVX0zpvX4KADgMq7Wje2HairvRCliE8c1B0hBKzzJnGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0bQsBNRuw1FXKG83aVD984O6sYqTElh2GjYaM1xRSCGBrePld1SZAUCsC3k7uAq6Dj5Xd1gxaRPhnyGTA-bVhLnwdh1R2ByYUjBHzcZ4UJOIrDNavqL11AJDxIdHJQ4B-SzzNvHeFG6byePdZd2f6SvYVJ-AaWwmw_1I7ZL3g9UELRbuFjZ3jK1SMpFi1-bSeGzMotCUlDsijHLCR9u-KY2FgJlMS2XM1HcrMp5XzsqOxyYnh1oIo_8RCm8SvSw2r__avrZPWBdkK35js2PlddcSkCftk4gFx5T5GAiOU-YIltXBza2xL2s9XlA3B0l6zuRCsFh92gfV-s01UVpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwSfTwv-n6Nj6ZZteGf3njAPpclXsSeytY_T0rsmZr_m5fzep_IoKafbcV4N31stoMJsq1zc0PASvdorsK3-I_NhziSQbaBFcnBrcfg5uyyOn08PDNN5yUFmuwPBeXMJGMIRBeOnB9nQ5R_yX0os_BvNApj-Y0UsMaO6WsyeisKQxbdyG1Z_YBj4VOvULwXXoza7bdHESPhVbUmbAlUeBUv5LrxaJsv9Qr4b-KTbsXjZW_XSNEBFPuIOm096BUG-0jYtaXz1y-534JvV5hz228KI46l_H24yzdKZakN2QivLaAoZR2iVnWwX5uiKqiB9n5kWAmcfC2OsQDFbSPf6Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rffPdrB6zGTa77ixwL-i5adSX84RiJRoJTG5zeaehRb72X1iBbl-RbUoj2EeCe19SmDLI7lAZH0NqCmUWcBokFPdRmRpoHex8Phikn8z78bcXZAXUrzLE8Y2GnWs2ESuTCdcafDa8WIxoXsrsqNePuHOjoNZY12x2S68kGCIgZrlAHBxaeu1_t-30sr4xrkKWLMM4588WA7-DkNaJzpFHLdHZl8Qs3I1nJC84d6leHazjsItIwacrsKICrfNPdtQ4tmfE2HoYt7lxM6d4aawMf1Gn25qhZXEAkTal_nS7judJfNanrdj6YQ1w7x0XonVNkfAAX3rCK5FRL07E4RT9A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Z3V_zL5Gy06_ObEavC95tGl_TeKgh84NZKlpnkUpfxKpzGu4tlsxsaAGEe5wKASyHiGqc3zhKtagKvU1Ay91wSkl1WxXU5Arucy4IMN3l5wD3HI53wS9LuT6rT-afI32LicP-kVUiDoTXAD7wwY1_QudqVjUv50Qy8-hvpJRXsJZJdupxWS75GF2O_ULpk1vy9MFT7F16i1Q8mueY1L-LVt6QvSzako4yDhMTuG1CFIs4aEBFYU3vxrTFVADhjnau1ekuFEsxz_8sFIo1KPvMCudPkwzzVZZ0suXLAC2ECI74bFMVxzhnVLaqXJ-D9pdIDMiJbED2cP8MQbIL_zXIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0Z3V_zL5Gy06_ObEavC95tGl_TeKgh84NZKlpnkUpfxKpzGu4tlsxsaAGEe5wKASyHiGqc3zhKtagKvU1Ay91wSkl1WxXU5Arucy4IMN3l5wD3HI53wS9LuT6rT-afI32LicP-kVUiDoTXAD7wwY1_QudqVjUv50Qy8-hvpJRXsJZJdupxWS75GF2O_ULpk1vy9MFT7F16i1Q8mueY1L-LVt6QvSzako4yDhMTuG1CFIs4aEBFYU3vxrTFVADhjnau1ekuFEsxz_8sFIo1KPvMCudPkwzzVZZ0suXLAC2ECI74bFMVxzhnVLaqXJ-D9pdIDMiJbED2cP8MQbIL_zXIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFAzFZNImmrkF7rdvwouWjGsT5qlIlhz2DzifP3QvceVrlkSsI0kX_8dhtwcS2Gy18i4lPokiW85UfQCQAWpEivpLLbMTFXNZ3j2eR9_Ug8zaIZvbx4GUMJbZVcVmJLqeB5UfelCH37xvgRbjJsxYN_wNQ0DmYr28LHW_GA1mho03SqoegOSC-o9rKwF-qvTl5A6G4Ulkhs8QDjkQ8adbg09wOsOWIhGbfWzMJjXZ6_VqQ_YKpwdXJ_psxh3gzI3Bo1zo6pGpoMgm8j-Dxy6zzMFWimcz-HpZDrpDT8PW0O5_dSsPEy6FGEiCyW_oR_4vSqUk-BGqE3TKwsyY5Arlg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwkwtwDz0VcSd3CHHE7llLEZYsS1Z4-L2E5C_g2IRnqkSZsnjPlFn9vRTVyx5AzkHpHgZK7oThzuyfthMAxzqpwu2dF_UvURipRzrZQf1i11Mt7LkmaKgVPcpmnd7Y2BMPTQfR4AiUa_S4PJrVP-HX4vOJR3Nl3EQeadyaGoYt6JAA3RWnSVd4SigmBocecdQxers1OI_gHcVVBxAqiqjWuWSDlXyqSagD2ANu7ifkst-pk8oOqXfhyIOoXC1-jCzTIZ9t5Pz-yrGEABqdazp_ABmQpyLkFJAZvjZksiRDRA-8J_0Osckq9pSepkNJ20VLLOTWBwfLVAMTDSkXh6_w.jpg" alt="photo" loading="lazy"/></div>
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
