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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 18:01:45</div>
<hr>

<div class="tg-post" id="msg-938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5kloEkNE3Aqp_GkHC0CF3nULWslK3YXfEB7NxUBmZYFK1_c3_8lv17Gsox_Rj-2R0p9QBgcyqogVIStB6NaLL0aWn-_ofcvpWEVsv6J8hse_3x5A3gqRo1O3ZaAIfzrJfrxebHvnrPXuT2bulG2GwcKrSSfV10X26oLfY9GPkKBIvYGgebrcRx-iALsg457VNe1wL-NFygUcI0BycLVpwd9kdQMkRcTc7C1RCn9KR6WUEBSFIogXCmMyFxjPTuR68cQL8Wa7Pr7xsqOjTJK3ZRVfteOJnW9GxdT5TyPe16GhBV1_raaiAizYZBOMy6mkWt8-8Kp80Qw6yWtK_ABVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آنتروپیک دو مدل قدرتمندش رو روی غیرآمریکایی‌ها بست  دولت آمریکا با استناد به «امنیت ملی» دستور export control صادر کرد: دسترسی هر شهروند غیرآمریکایی — چه داخل، چه خارج آمریکا، حتی کارمندان خارجی خود آنتروپیک — به دو مدل Fable 5 و Mythos 5 قطع شود. نتیجه:…</div>
<div class="tg-footer">👁️ 278 · <a href="https://t.me/danialtaherifar/938" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 503 · <a href="https://t.me/danialtaherifar/937" target="_blank">📅 17:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 624 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 664 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnIaKkkFgvaqCnT1q8je8W9Sw6puFoS2DLCEgMtEf40sEPeT7b3MOY8e00aPSCC2blYLPLhYLxEm7oY4_uaggW9IOjwagN_ApSfKZoz0C89m4WdKpTFncOdcoJNRrk55-ZReJwftOZlwIPHILSgyL661R9_uXjGTgJn1o4PyvsGqxTqdJXG1C2POKAxVpioqUG18HUcPwe0bjg0DdU1w3CxXeQFv7k8UNdW4dBze2XiU0JCCha1l9lOtCgeYaNLgdv_MqDW4C6NKzW_-vVQjfgN5wyzS5TXHc11od0PvXM7QeQy-FJ18mEh8hV-n1rKN72lpYce5a_7VRo2o4Wl-mQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRfh5isCsUEyQNkTI2Fz9sOiBqMUNXs7-VkHXkwPe4E0Lk_uN3tqlWY3QdarJu1oCm6HfhFrLb6le-VWaLpEoPIPyMwK-wkTJwjBH7q7zBhL3k6vznaTyyCAr13_kDAGrl95WSxR3mRw5fl7VmfeEcH9xpcezUECsoZ-9pbj-IeLw4FYg6k0Pje68y3Tlb5TFua53O8MQ6Ji9P26tI0BntSPVa0YfBFDF2G9vqNjpROvB6wdZciDEKdVyPWN87ffNDacadjT59hEUcWENHCNyhm7LX7XDPYi4fDzsGYHKRws65kE_2CXs5u4LxmBOta9WZOUILKFVNWUjcqQIw_hJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nI3XfdHn-dT-mWvl7vfLEOb3QJdY9nrurCpy4J7eZkmeFnM9Nx1_Ld3vw59WZQNaewuvDwtLkoVA1RbSfuFPDk0Nnf-u9D1t29vlVoqmqxNnRVUNL2eLQe6zu2DBifttUHW2uDW3st5Dj7Tk_mcIvgsSqqcXQud0C_VuILvUfHRxRhPeXp5ugD_N9fYjrcRFpoe-RKvuHXNK5_vk4X_855yc3TjUoXUvKyZob_dM57JYaPqOI8DMOQpagMJu_8ueTgKqOnbol5dRXkFHHlHR5UA2XBQOvRtAzInuYKZcLqisObgrigeuaoptuwOIGwFpzL0e7kMkr6KBjeYekthdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTf8_Z802dVa4_KBvCMGUrmNOBDTWShqWRZz3eBwHw6gTRgXgL514dQcT14-AHGVT7d4ucE0_kPGz2u4KySVVh95Fv0VpI7pdE0DiaSKS0YDciqjxDBnuPfyalvYirvLDadQngsTnEwwG_w_a22ibmtYlI-eKuzaO3VeuHVIJpZ04NQXYEUUjjquNl9w2VLBS5B11Qg-eocATzYkMZRegugDiSEdpt0p2PfuMStQR2fkMrEq2ABFqiNPDSRJlql2rDt0rb-ifrcaHwQZSCX5qbnPGRxatN2iKHBWtkaNQBHgk-ZH0-3lyHkD-8ABPcI95Q2ty4lv_NothJtaERi0bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO5-r7QXEM0DWtQcZxCIdl51G0A_PmCg1IOzMwhr0W13ecqK_Wu0xSIcthAoTMQJEUnCjAOfCcPF4BCgjFD60O5MlS-Eq-nQpiPJA-Y7vcc6t1KQ95mQ-I0pYYu7eKVy8QpxdG7lTkdtmQM7tagNf6oLDAc0EVU9f9PBrVuA_DHSs8IL9pdpwGFNJaeEGqfJdQqqVlCL6ujNhvWSrwhf9BUPaN4_tncsOzdtFIdYbTGz_THmECKkfFKJvFdBxV6R_n8nZItnvc4XDhmrSpan8BCZmGeX39aZL1N2_Lp33oJL9H9StlL9Kbhx64qFpLodDB_D6O4-9EbNqzWaouqU4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDyfbkRtO1tBO2jmYjQ_MgHLwkfyb5do7ODmU-yKpbcIEUHSN6-_-trzOaP3gWDSFwcCGBLmiptpeD9yt0HwhIaaYVRrsH041JdcUwpzVAwcBTUvio6-SI6BBSFl4bTpnKmKOqoltrrqfPrFcIn_R4l17DKEaSqzccHz7DYqJrEcB2LON-kJ5hmBb3Peq0ODr9qehUWDX68eVEUUyIda0Hp0WEQs_BQvzBKysuu83UwPymA3cduhX9wuych4jiakcQF5jJEHJmn0BYJRVXygORxezdQ08BD7WByIzhdQg04aMOMrgt8B2tbH6VEF7o_u5LZazEPS5WlLKgx3EAe17g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brq_JXtYr5fzcTRzO2SBOGIcE3wY3kfg_sBcCFS25B1SVCCXKSaxL_PJlb3VW8_BzIVugUwE7HIo9xxE6TsOrYxmYroil6F6hxNTB-sNm4Wbw0LHREYQMxAiJgAtmwAI0i4VDafCxoMHeytEEKgvCg-1s5Fx9EJnt4gyJOibdp7Ez-6BnLPic_ldEDu0h-IxrNYGBdG9eneJpl2-3PnFjg2-IEMnm3otxB48OxdvTLs-_qYVJ1NTtbQQ_0s0Fdrh8tElExvCs9bWls96YX3AJ1tB6ulIgB1ZnwyISAmljo3HfynWWXHOV4mPkeQOu4qDyu9ZnVK43AbU9iheO9-oPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHZqau0J4Apzie6J_EHgPDWHoYoNpxpDV0JmQHPbMVOIh-odiwcBfd60l8x-qTmBEIPSrt45r4zO3KIt1Ng3d13nXYrgsPfcmaeYkMeLeRzo090fi13VIbgw8pJnLG2LeV6oE8zB_PRZDUMWv5Qlp4qX3-ePkVSyaHkQQfpro6aRMSv5RcVbFVmokVJjqaXT1v8rl-ZNRTNMDf9McUI8zmwU-fUJ8YR4D6_TcOX0pB5CqY4fUaSBPjDUDqZ4l4a24E3kEIwcX5UjV9n7W3KiumcNB_T5P5IaMwNuTI3RhIsA3lqByrMx6vJsFT2S_Un8n0-LWD45BtrAH3r_dpfMFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2GI4pqggMqov8BtYesqFFSDhogUia8Kcdr67ZpXbrLPnJtTV2twq_DjJGyBQogTALAr2ZVrlfDz_KrF9i4GegJGB-IndQd69jSxyhZ2R_uT7duVcG-S1-aACokMX3P46smnsWaCjF-Nv05abgA4RHngu0b0iWpjGyTWzAkuumwmSZpQEisA3U7Ft38ZdxHhGNNVbDKuNrM9Y9m9l4Uu4iRG2LDCsnbcYT2wZhkU4-WVV5lLWe9FBA8EtTXhIy05jYCBbsHr5Vkf6fJzfMBoYvAZ5OqZ-cBfOmFwnHFMwOSdEpO-t73gp5deV8VtBdTtIosgCQorJUIOa6zh7exFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLvsTZDh5h7yniywBD2j437wCMKlyDtiTtgpw43atPbazM2hQV8IN_f8lCkY6bkXtle4P0nND8OtpiimA7Ot6DvJNzoi1-EVejSEjoaSr67U3Spsv1T3QtlidsNjNRxdgmUyyrxclfPGFkqVzqjpsKGhc3Wa3rD1GiK46KmTLHMKgEUccDdd6yJK3_SaBt0dqBHLFS_livbHTgPIpZsc1jK3pvx0M1XVdehnCD7K_85-ccQJlfdi-vTUg7VhqQTAcyIjj1afdTP-IrJHGxB3eAhnwmRZxLAtj2GyKRbNfUJfYdWF3N3gTOCLLADmIuob6ReUTLgLnGmize9ZJ_WZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-Efsb5hT1BuFLdq1lXJ3rIhDp9-75NSI5kVLVcivbfNISizU-aOj0DmO774FXrstHF6u6vznbXa2oJbV_a3mKFrdSxqjmQcEKGG_XSDp6ae14r65omtAH1FGRRF-51lu-NNSzm7Q6eH0XYaBUEXSJBaJ6XMp42Ff84HTsNS3Erz4uIyVXF1NUg997efeceILZm9k3lDEfm7M6FelZyOt7rTFqLFh1dCpoCbcqzhQ51zIQwPQaC2TmQ890DOuXibxKANCMmE_ymxaV3mptN4w0BH4AMpoBSR1Ctt9PWmFvHu3-aS6K4MKZ-k44ezx8--BAG79679v0Opi6PPAS5fZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKFWyTcKVEavwdIfuqNeuyIYrUmR0OtzGG61U1XBNMHOUwiNpf9D_4STlUVe6Ha75NHut0KCD4gEpmCCSNDmRHeuG4FYbiW1av-cKmopdvph-387xCMAONgY4yWI6HIS5l25KJaG-pxtdlXGVmbBj-o8qTUPw1dlsNb8DOOgY9_6iXaYsAK95WKA1XCP07zr0JoIsKMN12NIfK2ZKsKo_XrPRv8uy-S5uuC6nKXEFeq6WkdB6oZYERDR4-sHPxBbNciy5PRIMqxm10WH6OiGKxNfWapBSliDVfJsy09wfph8PXQizErYr0KoZZTDsZvuFj5uC5IjfVlc2k54hs6xhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEh1Ppj9XbHfLdTZlaaF-YkIodlu_UaZUxKWdSeDVGZYmIj0tQnAL7FLoYgYII7lwtkK3LRBF8NUyOmJALuieRrzatCD-ypicCflxpNdjHSDajYGDy4BT9G6IuO9h7KXDh64F1vlkiDVabCkNR-ZrPiwx-ISmdhrTt3__6Wx3y9UVFWUgrS83ytmsYyh9FRC-JVIim_U-p7113-DmQdGiAbnJSm3hv3_KLaNrGqynHJIvQ-wTKRvlt9cFpG51Q5gbiO4vbH284R_lAsEofF-o3lEhQtL5rRRkbYKOmsVnXIcykIZh5x9k5nDU1OwzCyKOsxq9B_Gv70frEfcDPIxPA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=SSmr01yh1kFrpVCqCOGwQ6MavPSGk2N87wvp2z3G0ksD4QZE3WOZfsIUHdyYWpEBYEXz0iMG0HCzEml8PLIGPh5RoleSgLF-ARAfpn-ikW_nI975lAnzt4kt9HGHNuF3liSceA8OmejylUk77gpkfQsj63L2bFHYrJbLvcybUeP4B_bq0ttrRwXas8ec44hNFwQHcVV6gVfw_k6cdJl-691EiPTn9qoaGqhNqgs6MzAp_kJXWpRiQZbWo51riBpzY9-fURqsquSTWNAEZT8B3cEwvP7RIHh2eM80FXfjn52U-AWIDVRoCPtxYgdG35kmwb2UPhb7mSjAiUTz0KpyLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=SSmr01yh1kFrpVCqCOGwQ6MavPSGk2N87wvp2z3G0ksD4QZE3WOZfsIUHdyYWpEBYEXz0iMG0HCzEml8PLIGPh5RoleSgLF-ARAfpn-ikW_nI975lAnzt4kt9HGHNuF3liSceA8OmejylUk77gpkfQsj63L2bFHYrJbLvcybUeP4B_bq0ttrRwXas8ec44hNFwQHcVV6gVfw_k6cdJl-691EiPTn9qoaGqhNqgs6MzAp_kJXWpRiQZbWo51riBpzY9-fURqsquSTWNAEZT8B3cEwvP7RIHh2eM80FXfjn52U-AWIDVRoCPtxYgdG35kmwb2UPhb7mSjAiUTz0KpyLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcx9BpBbi9N_SlxLQu2x0jmMeJ05s7qdWgkLCPjyNi5b9wX8KIKs0tTKFEAoX_G2KaT_-LaclHIp-dUDfygJXvag5fqa7KDSDBEgSQwAMGvjkANVfx-XILOIqSplXT4Oh9aOpKpx1QdJqdzT5vqwka6C4tA-mOQD0mWUnPCuPijDu7A1k9OpMkzLaImK9b6tpysf4gjUTbjctOg-hfGBg0IKETTVXCojN6UKzXoPua48nZQlAUOx3SuPmHl3Nav4ArRxAWh2npP3Ej5vj1Fx6jSw7SgevcDhxXV1PcSfpOwCVMs3jNCda5t8IzOU2WqlDObVLCNRI8-tH2OqT2iD-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgvI5_k2RPDwTMkbpYYXl_uLDOCBypiQyTHbK6kg-4KVp0cJJciUPdDhM5Xya2sBg-08KkZiJB-vRZbLmw69-Wr3uXjgP2fT7q55HFF3OX14_AIuXSee_uk_MvbiaYfrUWwiIklVm888tLWKJ8BLnj9TGJHQzTF5q-qFeTgXTwZdOVq1eJ0LtAv5aasNZzkzrr4rfzFz2Z9eGEkI-LzwSfwb5paqkGK05ch2AoX5TfLFvbtI9bbo_zq1px7KgvP449JnxFMxhIVmFPVxT9yNYov4agTEG9VXMU6nRbSWrcRK3Q1htBjb4X5n3QnCkDF-FCA7EwUik79xWoRO6UiTow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAt57oWsyY7D1oa_TEyw6tj_pA6IRkhrpZvEsccJGwy-icRwu0Ffr_4Uc2HKoHByE8hEM0ZlN1IeqGTamAIJlirKcDKGNNSG8XOZ3ptkM4kFoMRtPxSUh2fPQTO85FxSMfL-Utz--utndvNVZJboieC_9ULk4vx3otltBlCArofjbBZtrg9Cfa00gbGa0gfcd0gMT6wG7EZ7-mNavNmbobIFwKR7-Rqw9yMSf94AZ5KcSkBzEcV3rxxLzE4JfvQPfu_ir16E6Ajw2gc9Gr6xHsSuEpq8rG-6yeoy6E9LJKTNhLfmYcjDk-bHHn2f7QsL8WCHkDn9gJhQXd5a15YMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_xLLozhTRSi8ZZv2GviU7048MKxvlMNqacSguVIy13QhLWcMRhOf94M-fKxijy7l7IZV4MlC5Gp8h5kBLaZm4hQ2y8C9NzniBb4v3PT2b6_Rfjr3Q-SGo7Fk497Apbka21ZI1IWgjeKCytK9gUUQMzEvloRbCyy6FciGthuVc0CTmjuZT9CIRRS7_ZxsnMA64IEugRtBEZ0iSHwQqPPFOafai6OpcYyv9FgLNEsv8_TFsYhxOsGzQue8WiYMzKfYxZac2oV_CXcGwhKUN1po5JFpVG2fvcwofS0pi5AoNL5qtdr47qv5qSQ1NLG6pNaknu7mMMVAtD_sqLzLs2pbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJ1AOcrGYkmQ2XKC1lAZWFMAEqCNq2eL8wfXfnnPBYgCCgY4YCB1YF6dIEjbUs6ayu37zQ8MY7VIDQ7dtTSbOI8szYaaQHyITSnodtz6rLta39_-_4gM9rDgG3VnwFsr_RgrWpvaEbBYkQfH3GeANsefm5ak7AIbRzAyQ8hHQz4daf844Ggkcv6POebRfcYixkGf72mUHvfXTiFcld4ekUJEMJswkdwVgV_uVLCOnD3n5NwFAiN__oepJRNcaMXL6FPr6wl3PEtz-O174cf4BzvpODhdUayryJmexJ8pg0_HxDsYqmxntHLfa5hvOEICZ9xQZmCVrKEYLDy8DBIxtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA2GEz0q1_RIzYPo4nGcaotQEFFBCVrv1mvG-iblSSe0wm28HmtzOX8V2DrPlLiOMDBrLgVO8W1_tWLF6ZuNM4yR4FHU4GCWgr-0afAHFnDCXUkdopaK3phVrfRO3s-fmmuhMsCWeB-GD1d2Cz1Q__qgsHPnpByb2Xo8yB_GLO8y3jnn-YODMvHeCV-73Hxb2UtbM49s4BfeXljnys5voeHBxXgICiLLmiOlfoPmThycXmqors4_wuBgqg5N5Ycol5Dv4iNel-XvvPxIq2l05mJ_bvN3NNo14SD-dGtfatWqgTgYUy7-7LFHiMPDKoStCwokJsM42-KTvs_H_WyVMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XaIiGf8aNsOHT9Y5PbV_P9KD5iYSubcxbLc5Z2A6RmnuSf0B3D5QqyXT3EvXLbdm4foMTrNdayrKtJVPmzVpQOV2wknZIypZjLA4iVOjqijSK-dyue4ubK3yrW3IrIbW2Z6Dq00Y2x-L0lGCeJmGi_qLcJ3-kXZd6AJHTNme0AHdNXDISw1_4rr4cwTUA2xmyPhC5X9ytgvAVpFQrAt6MmtMBigEBYRuBNd9HP9Faoe-guS-rtsw26o-S_PaBy_s5AiV01Kd-lIh3oAiR67WXYfepqJ3nAkJzV6rEDnVl7rrEBDxoH7mLLy6er1IVv-jTxpWuAB6pt5qQnK2w4MkHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCf0Dfi2DlVWN5fptrn0z-u8IlXa7W38H-hp7_ypf4Cei9ukzK9Jg0mmeFDZ5REzI7jF6EedwMDfN-6m3N9eC4taN3Noabmu0uZScJtnZxRByHmSNB6lpt9PHcNxms80HMdzRmiVTi5oe3oeBsonokzg9V1fRK79MtbiwT6m4nZE2HpDtbPcfMg5P7VAKVbXmqSDnjMgTIkm2r7sp-sJ5U-0OWLaqPqSKG9TyakEqILQAmgKzffHbXegxSzykqkQ1QfFlX3tqxwGEAETHDZrvnPc426VSc24RMZggY38WBBmHTyFzRRSRzZ9THZwZXsWfK7YYFjwd5kt89MYWNOXnw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4dagH_lFXHs9LQMFptWan3NDbyQ06fvmY0PfA6ltnNnBMSmo_kCyVJIXVylmsILNo7oCXG6sD4EcZfNFRkzi1dwUmCYdK0Xaps4uxN4WlwvOGCt9Qg1pgYXwWEpFVr1HxK2fAyJEwgVKL0XdAIXWCRF56h2nts7h6KG8KjOvKDpmWeMBB2lYCmHUdIyUrEnQkFzSXq_yefpURh0-h-M7NcEulQSO9NGfUAVgw1s_lDOOWhu0BDygN5whg9IWn0Mbe554__roq9Pu_bC8kRqrGZnqZPpwwciq5CiN3jm_VoJNANDu7Cqajnrq5hFX6mUbxG3Be2IToBhG4mOLgbv-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF0DjT91pqgpko9UeYxYjufXvaHL6OR0TP3s_bYHlGoRLxk6YHZwJlIsjlEwpGMuWFdgDDLoJljqXY1wN37EAc800s0gpfhVB7wUx0k3l6Y-AZYl5X8MqGIRMat4UOA4vMp4CO3MHQ4F0nmgjdh2ecHB9lonXJuo1h8NGCbJy-kw9cYK8qCWROCeZDJLmMbdw8p0J1O-3Bt5eN4pr7mvptmJJewfLR7wv0dsbCwDmqZLswVejSL82supyQJTA4RzG11lMblCj2Ot5yVUsxjF7M3wDAk53n6QDy9oSsJwRhwWEphCW9CpKHrxUDTtjG3fIU4d2dmFxF3MqLk1mJ3eKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIfWfzxb8RPf0MbyYmA3uvCVqebCGBHp2sTSzhClbkfqs-L43khvXFngftqsaWN2dJgK-Ly5f2PTe5gJ_2Cq7855QYOk-CQSF-RW7wUEBsJ2O3fgiDjmbHd_U0Xia2Wo0zCNX8r53DtuTBxFfXMfaDjMDZBgZ5yk2fXwrRT2ZvcefWQ3-eJC3ahlx7V-iWUJyAG1lZLsdKFzTyeMVxNH6sI01iRzEhkSuB8bbQvy4tc0cKYUu3sHKGBdJtrLw2DoBdW-YCpIRLv_3eSxls76oV7TvvyIdzhpnHD1KYyTD0fjjQvewpsk7j8FML2GcWv1K73nc6zoXy6IM5lJrbv9bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEW4yEoTFlEKtx6nS30DO6Ksg2ZP2OLSGDvkY0MFqrPcQMV46EG6grcYt5Zk5LWSd7Inkjh_Nb-UbLVN__PC_O1kTTuChoR6I8Cy8x0F1Ke6j5OkyoT1bf0L-SH3sU9bDhpkH_R5iNUM19eCmieEdy7vxTmZxdtmEgNQkgLMyoUBmM2pRd6_tdBnUYSiD_Us_2A4ov8gkmzsOEBqfumbgnPGF2VRvor0hyn7pA-SU0sBZiVp4hKf6yKqN4lRQv2QWnsRGPc8wZWC6K6G753KV9sxMNSFas53fz3-XIV_X2xn_XM_c7M42J3hLWhnmPT0URe_7NPfJfKzqSNahu5RWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dF29kdOqTL-ANeFy1WbHo3bNNSbaljid_w2naUigoQQUItGqWgkMDg8gaxBURR5Zz1P0YkfNGqQ4uC6Nrt4Rs4GP23xcuKPow-LtOEUWHy-lpUIBg6OxSavQiR8g7fjVruOB2yi0mqd_2xxDjxE2NV5GdNmHsCA61bnU2iZPchdhyS3fn2l-8hOzWt0NtKkvBGg82_FSTG-sG3aEY05JtQo3xRFhaZ3WaQ25NNTU0djeYbVn5i-ahCQAsnY93_BUl_FwO8YUOG0PT1aSL7XSZ96Wz8rmkY2bIhKWQs91VclAb7SFsi35ZFyvQA_MOj7NyI2FzZu7ThNQNWSxj9gRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQii2iT5v0UH12VulBx_OlzIMpMqT9p34YbMPsM7HcSWW8q5KqzWGhouYZX-Mj6CyR3WQoy-3UXRcJGeva4Uegx9T6S9r9pYsHPKeNmBRtMVHIQOH_vX4vnRNN0tiasV3_vrnEP6I2hh_mDk77Dg1pDeyPlZeAu2PAZyQHhffLb3BDR9B9yUyp5OerSKDhr5yNrWrWSDF7w0iwpfn7gav-vWeeRuvPlOWXDuX9fhSDvhQQUCEyN6ZmwnFpeyT9ckAXvoCqLjML73DrWQOlOzKPE9kDAZJLWhKJ_E7nm0jZ_U_HTACA4eTzSp4K7TQ-aXIEcJQRcOW74SWdZihU6Qew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9_YfjWanyCvJ1OMpwZxscabCesS60qLk0_ggxez_XXmtBNExNX3lW2dYpgJ-2HqMXjIicA1ixBuLMNGcDjKN_7w3ZZvnb35VaFO21T0uR-AEKEKNQuivzd06c8OpmSGJ2MpQCGF9iDzYrQwS6bvWy5ezrUGAy26qRqus_hpc07VcBlywnMI0yIVxxQYgyjKf3ckI3adl_6gVJqRD_R8E1FLuu_DEW74J0xcBO5Wd-n3LncPw6qDCK0YHStITDaPQ87-NG4chXB5PVXmKzvQAATD0uC-CB9DAakECVgJ6MVCpkUZ16su2kSEAGeoTGXUXRdYfSohnZN9J7bFICgPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVOejkIIjkrDIKUnFsyxtnMDPZLCz9hEOwVEGHLOexMgleUrH9MBemaEstSxMaxwQOHWSSoYWndPjRWJMCuJgoqNiA601_h3NpwwSFjy0WYzhas8yMKH5il4gFyPQGQt_ve3KHrqoEN-HhsKqmmXP7YNoNkPD-qNxnHLNdCGaMZjFxHgQ3sGk5wS8ZZ-BYcTqC_pIK2UxF1xyVy1LFTeBbqUUhSr-XqsOLxfLEdyNEDcqXhCD1-JhZWYLu8hFRCFH9pzbFxhvSF2igOb8KAYGzdU0_NjL6teZKtZL6rMdcsKCRt7XYWPzgNY8_fad8ld6oZbBCB17d4LD_V9uWhB1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1VKFLOzaWytSlIyElI1s1Yl8o6PaQWnfBStkkcoMh3idwGrWvzHjM_Vuilwq5Py6rdiZJPlayrRtvoABx59A6oT_E9-TSbIqX0cwnvoDKXcCo1kBcOTPSXhulRjFb9aPWwIp1HUTT90LZfHDS5BxH40yfEsD8d0YTsOtzDa5zPY--3jqXPhBU9-VLe4TgBpKlMoCV-tMIdgYemjyzRgdBRtorLhinM4q_4zpTYonYWLGZsfqDEsQ3BVWL3HuFHvGztxqPAIJYJCBJDXTM0roJwGCk7jbmA5Tx6qgeTvRnpPR0JHwIAWrIKZVnlf7DDO6WZtcGn1Tvb5BBzzHM8HEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 783 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YthTRhUl5a6XfiOW89oUT96l3Q2ipz2sHbQjmQNMXj_D-c5O99bLH1nTln6PeukR6SgBch8lUMJu0dt9atZdlXxjD3J5to1wJrmQKmqqgl9lEpMEiiYw1xYD7QAO36ta-_8ELooJ7GQUTHy0TgIPGEe4AA1tDYLx6DhtaNOny1CoDmt-nqZ9pSfdYr-u0-P_n58mrioJEXRXYaDBR-uNn-g9QzpeNdyWSAL4_kVSvpa9UjRjWvO6jD5rVDnqW3H5C-NrNga_dTzz9uBABads7kK6kDycKP74eKCJW_FmSefgmWsyE04tfPTlS6yjxxFNnXVgV9kayelKFIegKjSOeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmTktc1gWBBT-1M0Mxx9kHz_cRONxdFWNlq9twsqEkEe-ODn03Uupaq6NYm4F25-HELhnomDj3Hb96k7RcR9k5ywzC6ZE__CnwN73Wf8LF39yWaYkCFz-md_mhpxscie6lxf09-GeBdZzw59xRypcR_Ki8Swew_6lY5nnT3wPDuDIeBLup2BfcLV3tbepDmgL6gg3t7vMJhtWuMZ8u-pQbs4dZyG5WVMxF_fP_WT6UZ_Vht_t85KquVjZnbgPMGW4vJRkt_PPOEMeJwpbfUu5bquuY8RnudLSY2phUqEPFdVMSWHmVhWCup7TeO2sFiQQe5Stz2Y9hdMSkABywRYTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agz_Rsz5ULfucf4dY8CG5x1rOMKIJWQdtaiIHCqFPLXnqhWqV1jWW0teFVpEhKdHeF-AaRChFuYYu_wCmJ7aBaUexjfi_JHDgI4BOdhI9mzUQDPJ_jCYXAdhFwrdLU6Joq9QcONFfZFLAVAA60HM0tyhnNtMcxqBw9ojQIsS563maXKbm-_I45ldfkGXsF3L_1abO4xcU1pvdgIZxrK0PDOtFwX83m0lz_KyHAmLkJzg2m_ShSMw_LYFmE8Fhz591A2sDJ6XZeDUu-8zcyJghnoh7GFRMnh7L6erCEeNVebp8UEutLXminaqmsvENM-57FAoW3qxr7RXs2c74LgaCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqoOo74nkXtxOXUjxpvK6Ro0nPsiwmfM8Vtv9o_os_CAtoGrJDQ_W9nsV7FFIDO2rVrDhAvfVoUna89u1AWZJo-aiUuuCD8ATvw6TxYIsQEkDaa8GTQs-3ZeN1BOpFOHce3H01lzKoObpqQa5ByoyB5ofD9h5-S-wk13mXxVm-p_TJrzkrXzKf8mgtC2HUyEngUBQaAI_aZi9MAXb-TtAAfKcgz2nBjV5GYpiwui4js8B2vtXmB0zu2vFn0eD3fYAuworXtkVOvdxj5ENIy8-Z0ufrbPtaBWPomLT4hWVhAAC7bZLUODcIQMFqHdaZsDoeLzg9FakBu2e-Z44zwh3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6v97I5ZRFp7PQS6bT9HoXumFowU_dtdLk1I-dWHys6o9nXeUt0f2mhk94XoLiKS8dlB8e_kVAPhSJI769cV-YT98lsIdrQx8-gdO5R0d5ZWfvhvgI3P1mg5k9bOaPRLpDBsBzQ___i54ozbgzL2Dj-UvOqaouGzLIWxLdOFg8NZm6oc2O5KjJbdBssuvPX4yj_jtWqQNMj868jO6zzrggYVNtWY-DROzvHwmPl2P1B_6THBMNN3m3Xj3Cs8kKJRYslGsUzNxfapSJu61FTbLEM_wFE4dFoE4i0brMMjgxkcVN3CBK6p1booGlWhJAt4OAMQo92YWWlkS918XcNwAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uisonBVBCmG1cPq33Uo9R2RlfqigD8MxB2xc_zeFzlLP23erNa-ubRZK8uWCHzGnbvMz_HXgrY6ZAeSS3QrnBVrcTspy9V153Bj3w03Fw_aoToC4m7FqHA6sIzzM2HXEe6B6Z6La7Q_NgRUp90JeBWwymhWxfyWbWMGLZgDcjv8KeLBeeWM_X4VntDeZJcvRvw0p4lHZFSRlEL2afiR1hGKKymZUZuw_bV0o1of-MNFaWVYmK3c1u36eC0ioz-NZMpHir0FCCi6pfANtTfxczw1c9SOYUslPF7vffhTQMhGujrwFDclTyeRF9xCWZx0efqpdvBQ5-knt02jyEvi24w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpOzJeD2UHy0Eme61T2D5HinQvPg2sXhihML2fVgE8X_bkppWLiB3G59SUgLXaJ_ggn-0bfHDotrbv4ePFEkUKFeM4BlBKP2d2iRwEr_hsxvs6mRscWFlSW1POWFK7ReKN7drG94osCU_kwEKNQJJ7lkfXTDgx3x7gT8ff65bw0kY65bOJkXC0uHRi1ln6ZEtELMOjbRIrTHlmM0YLrZP9qUz7zZ41_Ym3QdGWyQalf8izyMaJUVjBWpwdvs7nFc8G--eALOyoHSVp8JaecPXfGKRT0V2VWrKMD4d7x8yF0PQFbEgNsmsiBrzajLDftsX8bqhzK1nU9zsRwqU6RKOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHxxMm39CMoQi41lwJOHf4kuK2r1xiAKJQ76o5N8W24HUfFU9lTQSUbyrfEEYEH-ZKkNOocZllXBO2GPQjvGScBA1AgWJkvIczxkBxFi4dT_5nXa48qkdZQUicC_etlxE4wAFzl_bxSiTF_HrxOiMkSCzzDcZXz0ocPJmph9Nie9qjJKQ0VZGyGo09sKRchjc3LP4NrH-z0ybkBM0rMmQsaDz82Ug6SXGX10nJmJOGsvbWGfd7-eMeHLTw-RGcfRyFYXcMkWP4BaP-A-1nPNM7W_GE2yGltGI10kWxomYpBko-f7R6yG08CAIq7-yJhPxd2Ypw-aJpZWWcoZs7NQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3KZqB5akW9i1aduPrRoF7BUc-PL7dxSx0c1gDkpc3TP3m6IFydqbYXdlrKl62MEsjQQGY0WqPdsgnSRCEEgQT_qKgXaJ6zquiQ6aS8EHDzbul1mlG6hyIlyyZ9vj1XSwBhuyZOrzy8XQ7JyhEMUGCD6kMX36uTkvNv9tx3TjdAaF6cYXtJXR9s8mT6PBGDh9aBj9CQTIvb-YfX778vZI2vnOrGv8eZq54zR6goTpmJyMi-utIUcDNMwcgojFs8NMl5uGyacAUGYwG8MVeM5ICdN4WsP83Jap9KsuuJSG6jzWpjJDw3vm4ERxMTGDiIVVIS3yEn0HnbFmiWjf6AcBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9pWruTvuSqXBwSF9iL7Q7Lv5Iq-_d7uvyV6doTiQ8iLh0SKNYIjueXuDFmKthN5DbRxWkhpDruPayT0MiNEaJ9-SuZqGpbyUW9crsEchsJKPEkdaRI-iP-obq9CTiI6UqmE2r_yRF2GVzCTRWiwX1gWgBM2dk6LEXZJ6SV-C3mj3WCWFPwHa8sn6r3CK5-7OO_XvPx97r1SBflYlsoSMz11pq5iMNn1ikkUWG_vEKf3RVce0KNrb6BzQ_DO0bRtqQjsSPBxiWqubnp0du0iZ7YzWMfTm_A07qzIpA-ls_luFnUmqPzM-cpYhBBif8vZHYs7nPvxMAQ5aPjzvVG2Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugv9Z2_tua1nLStpsmMPRm59ja08P2VHwx_vH4opKJQAY4ow7N_xFDK1-byvJiem4RhrtjZAKe4eT3Erp6pgzUkhwMQkUqaArTzI3nO7WK7ytKq_SWFAbblRRbh_rjzSVNgleiDki5l_4LjQ4e8WH2vafbkxLG0aj3oOhCh76rigJQ_CA8BWP_xqafoM6q73SzfZKsMbZ7GvMFzPd8bOxO0_qL-qtuvhQrAiENR3oaUucN27Hf1u8KrdVxq2vfAti7kvxb62Efsn4bcOR4HGnOcc9uo2BGDZLc573LWMk1fhkAnDPzAK3uR43AYJS8NO8Jfkj6jZHF10ZPOeXLtg3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KixdEy-Z5m2AA2tZ18yoDIjyPIVBb4W-r-Kg-YEbgO6orRRMzbNCoLPrS2pZCIZ44YkY93_-45aPmUyWYJcyoGj-xVjXIzmUkgovOLfv37hTSochOetqgX4AGNzZbE2mI9wii2ItVaxp13DtxYmMF98s9cBr5A2Z-kzPzfDnRNVbRNfMlV09SkqJohQJcPLe-Uc8UnJkAYJ57L_dU0q5tNnOH7W32_8hGDZ-X3YUSb11NNRcA2IboqGvRhhEfiuXiwmyhXQJJfcNugXVpAny92N-DnPZEMgXe3ovkguJOzckyXB6FjsbFtZAxpRrp5soxWASnBd4JRYrK52jflGAlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0KfTcxujDA0nDEJOlf4rBwT08XTbIE_jbgCmCA3-wyGw4DeYM2D-AGJdCkz8Vyq4Uh5qfHdSgxsjFkltFskN2pfhchiGGjcklaJjjaoky9LCOXVuObMMD5-MuvdG1q03S9lu-7GnGl0YfivZ8Dlh7AkkDNiN8jRN4cbBBND1d6V5V9Qfa3D1LyvP_f3Ui40eekYO-7rL74H7ZzK4b26lAP3-FWl2r67nC3u20B7ak2eCQk40vCQhroCsVnbMKPbrT3lUnFn2I2lvvNjI2FhBDjI-RzKT68wqkeU0W8dpWLdsY5zVvI3jYD3J4GCAYhlC5AJ5ClocqmAlGU29FxdLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWkwNEIjvYoQLUbPJhZCkqCZB16RxziuVnaNNUG7bh_e05lE8hMmfTEXNqKnYHzecWH5yjxz8ooK2faEZ6TiNfE87kqGFe5IGvztO1UZc4DnDBgKr1JBeXbBuNVC7VSTSz4Hlg5nRBqWmyZXq6SgMJ82jVOA2Gn-sDK876Iq027YMo1HxBsdU0pnCZgrtAX12j8YxjIAtu9tz4rX5oG8Pnismf_85LmCnffjVmTWQvNE5koniwPRDfCCQUpE7vaDOY1b0ulVH753t90XnstqI9_OewHBuLrmEr1POU3WjJm_2N4tqmw7GPit8hwGRlCR5EESuBAvWkdHZ46FsZWxhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXMxDdxeGsEyolLmW61fhfc-_UsclLuktGRudjT-kndmEEB_96YhVK-jlRSc1-bJHGoqL8uCXH1NQVFS8JCBDPIx4DC5qyVh1tSFPLAPLzA6MKfUPVAGqj4TIVI5y6n5n-7AwkyV9Bc-CoRmoZWAJA8BtBbm-pMKCoqdZ2lMX3DqoY2t8m88O_UmeRGjmohd9E3g7O04pdIXMmbN1na7I3E1EESaxpnlx2DFnYxIufN77DRlxRj1ZNKRq6sRJzkm2brRmCJcFLbK_4IiQpYzDiNcGcw1CPA0a2ibHTGrP3KSL_7aD8UXkr90cPYBT6qM01hSmVcoaADJcFBsgLAxIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veZc7yha6wKZiJwsiTsLzqIQ6eKnGrGbUIHRIUHmUrcs3uA8D_1W0toc6hTfc_aMM1EMemCE0OGidC0aPtT3bomfYBKawNqwkVhNlfSOy42W3NZ5VNtGfxoWSZnmeUvX8GHdlozjgGgtk7t5Cf4eLL-W71TrcUBo5Qhyj0b6aZcrA2Shg5_lafjXW4mlIELabnCi8Vo8QJAScdAMZsHlSKg0fH8qyVsdi9_ax8I933Uk7ehoqDu9OrlIIyo621-N908gLhBw_bWhIFo76kpMwG664U_2hIDEhMNqT_AVB06R0COSPXwPHhGCqw4LqS7OdTa6c8fHBeve8qh9hKI5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/THXS114agQajt4FTgK1MwDCZTHQFS5vPi7jkd1moFMszINj1yuwEMURb3IjQ5S68w3l6w_JspKVd2rIPcV-SjkIR_vroT6GY-Fxxcs0IycdGzLWwDEH8pYqeQeXmxGLp8iNjND94GFofS8fOkjCE5_Eklytac3N5KzvcLoeHkIKk-O6VbeVJnuJFfgFCLDTlnzIY2FSj6dY852JnK17LOqwD7VYB0kULUBtscNuKfMofxsS9rHlDc8p-kXxPfuNIa6u5y3X4DvCXIkddreAgWpu7GwxuCwbxfw_8WiFUhubyF-dSAge3z-Eb1aXKFUhcxljihVIWWfTw3IdACWSL2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Navw5HH4itCZFM58xFG3FTWVqNjnPx7vnm4kr1IC28BTAbzDzaBNixH2LBGwF_yh3yNmBGDy9Q6LfCGuJtNQjyQhnXpSux5sIRRvtxdE1886x6Y1_ji0FEV0bpyC6yLzEMc_0QS2jDAnqc3NzTjgfWBxfao-bufiW66gEBO_gYEAbtEMzrxO6fqH13VHcD9_FttIkwlRt8SZt3WGw0KDhN5octSS8mzJx6kyasdniC1trGTsREtUSv2n6n3G3Vfa_aoeU8Ugu3uHlvHkT7JNMo8leuRQzGEGbZvkAVaV6t99jGqAksRYNK_GquksaDhdLt_6ioQVUifFt9LeZpnMEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wju7MOMZMPiVHZFGUn0pd9ovFV-LRnvTIh2Epyi0lKrX02u-xW8rAc5BkCZzHEHgKK2KtyZIvB9wwVuitMnzepowzjIl00wmiuDZWNH0QEV8gLruTqbTuTgIJXcPCXnhs26JI_0OC3DyQLO1vO8Ib2DiPZJukA0DtivpPyk4S_Z8TUJdzMA3qXd7d4fG8enYkuWrLjNVSKZCpQnOJIFk0uYOsiuj52mYXUYHpd_AYunWQoYAeRGcilyUAx_jxsz2oZYqc5uFS1yQ7mq-fKicSf0QolpABQRUjxQzIDasZlpltR93I7aTr85C59VgbBuN-Peu5z-oCE7h-aogQ36sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8-rSA-e2dNPZzBkJFebBbbDHT4Y68GSq86Mrbx6uD0Z7NaaGq_5sXtxHZX4EJQEqRgKSzyVlJxTj2y6MyFOizVYXpNzMglhuwO7F_7ZIAcQOVy7yyxy_Iqvks_0CLVoQ5k0qYtXGzRhBy749BAc7uonynzPU_-DeI2hgSAfijdrZNlHXU3yzTSTP4Dw5ktLER4fOTkRldmvWLNpXdShpmHFBWycBwCKLDHrbkieL7CyOVlZrAmQlxh3cLc7d4VVsewKrpUvXYplGHE3cJsrkSraSsSoZpvCcywwXv4YkfrGs_BzxAkl4pqPxwfbkYU9xCmLgkccFdv3ZomFvARq7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdnA2mKDoPH-3VS_PdSCfKbh-COZWaBURqTmRtUWTLNhuun_kgqKHmX7TIdEbJ28bZs0l2heKdByDwD1vF0G4F3G91Q8E62Qxvu12Sm4U2FcWscXU7JMC8y-WsqMCiNXnGmqlRegD45nDbq0cnwHWGxhx-fqBxQTo4E89_FUfbM5VnYtJBmPac_JIl3E9QQ0XLROap4uUm1ElsVQyU_GOM1WZYATL3IO4GGV7B-uotjC42j1nT4f02nvO2GV_iad1xZ_w7NnQhDcJqNIKkSJ5Y1p39vQPXlAk_v32fVOILsI0e6RjBmA4bKz69J1jHsSA1II90Zi1S3SM7vpeTK6mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlRpeh9Mcb7BdQSbWTE0cjXnTVe92sxdKq-IsYvlm6FR3rQHvxIAhxmTUmOYP_MhY10Znj_LuN0lgsRWSwnmbwP5onnlHzP4h0r43H-1zOQEK5-2tQ3mlgRV_1Va3NraOXQzsqVu_i5C3-i-PJtOzB87w86zn5H11GWnK742282xJ1SgHquCZDP-VrdxU2jPR0Iij5KiVvK9zX_iQc7g6FCVTZBky2qMGhFcJE4GxlKk-i3FmJVLoqNVAFej7htJQ3w7uFCKBzzUK5tSml7EOnah-o8Lv1C9onQ39FYQ5KrAW6SPWC54hqcHRMNqOGTatAdpVcemsgbInPcssGT54Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwMjai_s-JnR10nxaQBmWcLvcSOgN3c6lnK6OLyGtHzA_WnuBgmlsMas6hMo6I0OxF6H7AGHOaic08Ha5P2WNjzOWkJ_LTJK6P-fk8MTolk8TozioEZBWmhOeml_BO-nnLZbC2MjBsc6qr3LY5ufbFCiMG-XgJpTdEA5KjW3FGJFZieniduo8QBWrAY4JSfjxrKxplGaP9HN9_TSFFxkV1rfdn7YDgkxn9E0INLbWUHUsBoJ9lKDulqcXGITcxSgt_4XYOt4tSaPB2u-dzXEGvk0WqImo-vx8rh3MkKuWp4CQTJJeaWjulDrBQrdjD3hFbL-fx0k6tI8QV0JD1H17g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyRvn1TUSyAOIA43E9tEErT9mXwl1n9cMNArBkdqUZDjIB9HVNmIWvRVYRKwDAuwg2-g4wqofDEDl8Md29MDCvqNVnakjkZrWNgNdZ_G45x_6abGzTchJsGjf-GEFI_Yk3DENmVX4PR6pTSghQyxyadxXAzyH_3hS1EN4EACsFUGl9VoyKUkQjau7IkI1jBFSsBDwBYUePRbjo4ZPfYXRHyyqjlAkjyMjQiN6l470w_nvzAkuK0YkKfgEceqj_BXB8TYcxVNOrotlhbU3yX7hyq8vUtADQR4Yjy2qRSVXtVAd6tgjskWVYAmUIOEDa6D5KwY7WNSO33n0pAJw2lT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mE5e3arIFOXCB3jVywTISzL9LqLrHMKszL-UNNKlJDLdAML3hYU7fGreCjorTbu7o67lAc7cxq1HoNgYU0cgxLJbGpTV71TUYGSg2MTNPZNrwZB_446ociQMcgBkN_0JM3RJMUV6ua0U9GCZbiP_kuTISNSgkoRRyTsHEwCDJDiiYfP8Y4wx1we7hE2--FkHwsy3q_ZGu7XsR25DlyZoR51BGVksIdu_UWrTUsi1B9ZYXi3jTvpg9q1C6bjesp6GSYDg4uweGJAhtVLLu6d8xiV0gdI9pb5hg_Z9YvLIN7bscn6A9E1wAOFn-9zulSag2GfZMHZmllgMyy9c_UN0xw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7x01QljibNkE79hUcSZxDPzfe_M8PxSilmpqiAyQlSd8hz3Il7-EpRGvuaMBk8-MbA8hKmhWCxE_yINehkBQY8iqrFZ0Fd8xMLyAi6NvecOrfi7ODjOqucnJhDhOHGtm9VAujvllSqPlW1nq-cjWHatqutLN7RQDb3SqOXMZhv36GFwelW01pVu4-4nGKREvP-OR6Aj8K_cOH4puhStsNZdmq8NLZj89G8LzNjQU9AAo7tq_JZ0oNj0eJfPQhXsB206J2YuKAakb48ffX-K7uSazVo0fw8ePHRVcCjqJ6FM0q4vC-xTq8X9dyPTpal4QQgQ5HaxEE5oVHqLjvygMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-RuuFUYs8ePZ6N1tYtpPdSeEaR9Kluu3f4LFv6c1RqXhNaun6N_4_0z0ACyz0zlkpSy8IzGObu6aHAfyawYQboB47AOhdNoWPG889F6OJFXvo5Ut6Uj0QHMYmYfsznQLf9FRoFvGbdYVUx_z5chFXDTxgeG5DKNNR5HPrKwbSPgOuhOtMIP__SVh4zWlfOyF7msnVTKUiMpIO4a-WMTKPO1Cc_VD59hVsDh2di8VfYWsSX601JgyiwbzoDODWAeWqYzrcQLCBDqPs-4OJ4b9h5Zyy7qCkYn-_MJX2Mtk_9K_PD_5h0_O5iNht--fIWVSLJDqQ3faJnyXjy9saId4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg3PTabQdpNO6CfUu6iC3dsQb46cRxHu1FwVIzF56IG4iKzEJpZ93Mbk6EkVs_LjcfCgUJ-QF6QrXF47Zob6akTbI0HlCUf3nHLfoiVDHaGtLdZxNE0wDTLfDNffUa68opk3LPRky7MNCrkOOrQyQdiNLUXYgpFFvL5UeT4FPRu75nPNrq92wtg-mLgaE_gkuptuyMp2HyLvCJ1VoDCrp1ji2yk3sM-z-GOLFaFULYK2Y6VFEcVdn-lp6MRs0IavyUPGFzJbKoyuqVGxUqzT2cqiuOM-mAkDtUd6Wm4JG_nYHBYaFmtgGxSBXWDOM71b3Vl3QlTcpdsQFrcx6Nv2_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIfC8hwDImgciXhkNs-KxrCwS8BxTZbD1Xy6V4sAaFUnCZIwFYuptkdUr-wxvHZjPyjJZ0o0Yeyqr1mJvsLrPS6h_BsSwlyhgzGYD2rTOFwzZqOp6aIf99PtN28Cp6V5wYzUH5alyd9hFuLDs0c4yfgm9EfVfG8A02NTo0k18X8qFHHegUeAZXXzR3ONcALPDjZkLmAD5hGtnJf0FzaETKAi24o1zwQNd9WPstAgWY285MUbXuFj6ZYZWlUdVF-p9A7-V0dP7iV70bFunONA5bk9Of3IyKJ783x06AuFJWMXuaFeQt40ZWhuujgiLFbY386irnVfAnRUceLyLzUUWQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=DfFe1o1oIbho8F8QxKizliBK8MeYG61Kb9GaVMLVoYg_NW2YoMphiKpdKCNiX7Dk822y4aleLHpxFP31VQqEDR0SRXmoO96FBK8YqqG62oDcO3QSvCaZ2SG7nYD6mc06hOjvtwMmpJU2YSCmxUnIU0jI_WKHPBHFIuVFnIfHNjxKZcnMhCymFY3O3nDBft_vJSDxahtyyjWCO1xHXAUzCJO45syyOXZGmCqnCTK8aYZk6KTOcGyhvRUZe6W2w18iPTEaWRi8RvIURoqV4SazdcFWj1N3GVxNSFYJjIf8-dTF6tnwyOmN4o1zf24U0OBoX9WyArAFLFj64tjvQxkfwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=DfFe1o1oIbho8F8QxKizliBK8MeYG61Kb9GaVMLVoYg_NW2YoMphiKpdKCNiX7Dk822y4aleLHpxFP31VQqEDR0SRXmoO96FBK8YqqG62oDcO3QSvCaZ2SG7nYD6mc06hOjvtwMmpJU2YSCmxUnIU0jI_WKHPBHFIuVFnIfHNjxKZcnMhCymFY3O3nDBft_vJSDxahtyyjWCO1xHXAUzCJO45syyOXZGmCqnCTK8aYZk6KTOcGyhvRUZe6W2w18iPTEaWRi8RvIURoqV4SazdcFWj1N3GVxNSFYJjIf8-dTF6tnwyOmN4o1zf24U0OBoX9WyArAFLFj64tjvQxkfwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd9fgVwGouJpkGEwSC8oppYLo7zTDvxr_1U8WRdIF8SaCH3fTGjtFzj711BEeOuZnX1uiZdyzeGNYcJgBj5BP5LjxbMz1-ceNUkN-YzgNwGDc-9AON0OFVt68i_8OntagnVy-6offmDpwvQgkGFg1Go660OtTUExik0vwmMOBZzpBTUrXsbVuWzozYQV_hpDQ6uax-0tjcERXx1vDWesMCxtPlM_evPTDf_hArfedZBr_8A33La4-CqEnwVfhDNspuVGzXlJBrYZpAET7DFBb3vXuUEES65Edat0qxnceS2raGS_0IEQEGhqwwbeYewW_8Hb7U_q0w51tPebAU7RLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXA9rhgRTA6gJo9r7af3Kl8xpmNLPaA1N987jOaCMF4NBN74HXZM9VW8THPOXKrE1fgZ_6Y10n3GULKEcSl02Vl3daf5k-i87JN3sn41MTi6GFBlMd9DfWzC7icXvnpkL0mz_-0L0tm_5RtR6Mz_xTOSKKQDEDLslWJgCe_fh4S31JmTvVJkrZZ-6tgXYydeVEBXyZOYz7HGZWW1Kg7uf78FlsCWJcPRiS1bdg2OBkbHMYXZaPOSBfeTJnBf6CZcE0pqbrjJ2TMsHJTzNciRd8z2yOcxovY_YOG3lfH_c1HcTYOR7rO3ZVZglbzlntJ44HM4k_lgRIPG5R4DRMkCew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YpYaPDJLd3Wih1DesQ6o_WP05mnF3yY9Ez6XSgZL205z9-N1Mu6XHGSvksXQ877uyZ6WtkDos7_YKJvqXNuOY8-QuAvrZqG_oXJC6YdMFJAn8Fzka9fC5Bqql77_I1L5gV7s1xWxe9f6NtMJQHmxbOgjqqNYJmb6KhGULehVeozIu_swmjVbi2onpJHKJP_wjwAmYLLW_Q6QLTFrtSlEHSw0Hs5_7dPC0IueUh7UWql8Zuh_ianVO_EtWllOMj8iIlT_HpEL1PFghKm4EK-59CtqIZoBcWqmuxNNBSvQrToCAkLMkZ8fMKWrTkBcS3nL8hWFkPTwkWPdoMyfxjVCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gi3g3kOe01KbnwchfPdSj6zQNhuxNJfLF1BB4k8DY7JSBP-xTaMBuyGDswAWVkiVJqbrdRfjCqCTbbMufXRH2CUgrYDWZRjkoUo1LJjUcUasPkDvtqUiEpOYb0Z8V0o2FBwssUCWAKoWKygTLJsK1uFa-CfvxAL0Wqs1FoOpzNM51lU2c6v1D-XLhb0fe37CseoVjXABfO0LBqKZ8wNiimk9Z5pS4qk0ZkaiLNlK3PMKryBPxncwAHXZj5Bg4JK3x14VYOqQ5EthjmmK1K-YeTNFyaQlhMa0i236n-LH7Zx_XhwMW6NyYOECVRgJT2DVXtHpgbnlzVY1r8vLpR0Gdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsNYgWjm2a1BRoYJRnErKHMjYU77BvwXLE2s7xwbIljPjFZK6aFqnwE0I_g3RhGXkINNcFI0QYNRdbjt2KC5BpFHUdwrlPuOLRq55SrXpvzi-9adgvJ3KbQXb3xTqe0Zg77dtVG_FMym9hMaDCWp_dEEnsVV9Fjw4H9-nrbamp8m0NtlM6nrNekZ934KkYRXjZTa9qPDLB8KUUI4WW3LCmEnr3qOugA0Y6ybvioASrZUk19JRcleGgRoMhLqVcn_IMS6wPUjx03wP4xQqYEJX95LBDJUK_f9ymxvCGDlKg11YWl1pTtkpBLus69mCSk92_GhTwvMylsxkCxJWSqn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hnO6bbxoCfwg6WMlLAY3WS_bGwM9kMX8F-rJrWkLJN54KCc8vGX3L4gekglP7JvwpYmNhebQjLhSRBx06j80wqzAue2xrHoVQOquQD7P_tHxebkutBmv0Pz7uYDrUpKTA0d3o9dllXhJyVnG6eyzKqWoV2iHvAhnsympcRvO9luCz3CSueXleWyz8aw6epxTzXT2twBKg6kno4Z6_slZ6terszaeFQDCaR-nzLtbPJXmCRx5xv-RmAL7vLn54wknwlbsyonIXD6MC4MZXD7MJmG3SXKUQDgjRxoC5x8a6fT4qV0dAX0v0GJGILLzn6vVPP4X6BNY7zHBndsnRMe2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEOvMleECDBCOWB7E8nhzhM-SnCUxDZx7UMCrb3hsQ8FXAD0wj4FY_SsQqk3t7ZULyVgKUyeUzE0dQB93H3Z0qtw1oAb-6i2756mcF9k1E_k1SIfOQ5sMjWmekFHqt9kUuHY7FNkFb-I2Hu95ftQNQsKgCMpsdPYSr2mihNozyI23fyQK2RlrRhQguDeXhHxqshO5fui9N9fjKRTazhL4pkqCGv35-fLymEOj8rNwTwFyAEaxlY6XpFsSmDmaptd9MVAvK2ap4LIpxM4dE2nGtf7jvI3MNTPr7jX5Zttnrdewqt_XsLSooF9rHVMZ0sdWQQkbkwYvWZkLQrIksungw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=sT6he6HiiryrzWbQckzC-85J1eo1L3889bH8gSozLhLKOHeuagAGaGpRdU7c999UZKYdmIra69a2alTCUpHEcVVzxNhLRYWPupkegSpUYwN9xlNmykzzwhtDVSuKcHnIZ7h0GsB0u_sk5R22VCoAbYCKKWCeSeQHijLN6cUDvHCp4BfWDDvl27EJDGP4oi9Q7YCdodPR1sISo6wwe9qcC1n-LKBcDSz9oV6s6x7-znBIddMMy-uJHSvzNFZDsYlXPuxhYYFaNZCz8csYTXeka9beLxbb92GqMvxNM4kCJWxQSzzHKMv2c_7t6RIJfOQ5nQpbRByXt2fFlM-AQzkXM23Imh6-2ZvG9-vrPTIhjBY8o1gCDzMGyzplKPik7FYTaHEDQ8tldnB-VVm1qKdSBx95twh1UBevg867EqwjF5No2bU4QrS-pAEQ3k1EgzKc1TAbvaN7yAf88aSixCQQ6tA4nJMux4Em2-w5kOEaZkRUdkWIYuX0iWb7nvyFEIFyjYMZwD6338FNm7mNnbubEhT0yhQegfpsGZdJ0rk4qR6wmDwl7nRQ7FI67ZvWLO3HdsAC3KHp8Q6MHW1w7LEfedFgaDGumnumYg6pKBpKIbOEVaAsYNvlnSks5HQSh7CSuqFXXV9J1h_uGW-P1jqa4zgD1QKBvez_PK6kzVXhlmM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=sT6he6HiiryrzWbQckzC-85J1eo1L3889bH8gSozLhLKOHeuagAGaGpRdU7c999UZKYdmIra69a2alTCUpHEcVVzxNhLRYWPupkegSpUYwN9xlNmykzzwhtDVSuKcHnIZ7h0GsB0u_sk5R22VCoAbYCKKWCeSeQHijLN6cUDvHCp4BfWDDvl27EJDGP4oi9Q7YCdodPR1sISo6wwe9qcC1n-LKBcDSz9oV6s6x7-znBIddMMy-uJHSvzNFZDsYlXPuxhYYFaNZCz8csYTXeka9beLxbb92GqMvxNM4kCJWxQSzzHKMv2c_7t6RIJfOQ5nQpbRByXt2fFlM-AQzkXM23Imh6-2ZvG9-vrPTIhjBY8o1gCDzMGyzplKPik7FYTaHEDQ8tldnB-VVm1qKdSBx95twh1UBevg867EqwjF5No2bU4QrS-pAEQ3k1EgzKc1TAbvaN7yAf88aSixCQQ6tA4nJMux4Em2-w5kOEaZkRUdkWIYuX0iWb7nvyFEIFyjYMZwD6338FNm7mNnbubEhT0yhQegfpsGZdJ0rk4qR6wmDwl7nRQ7FI67ZvWLO3HdsAC3KHp8Q6MHW1w7LEfedFgaDGumnumYg6pKBpKIbOEVaAsYNvlnSks5HQSh7CSuqFXXV9J1h_uGW-P1jqa4zgD1QKBvez_PK6kzVXhlmM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKwKsnrnUfvcPyfplGSroeaw0l_kFwO1u09wOayfrxk4Dj9iv_Cpi3AEJ4__9_rvTbJ19xijMDDdF5gGMyN7mOOJ2RoW96oR5JFrcYcJH0TDKpteeZKrfDOYcWiMifEii6W2OQ1b7iE0Hih3Zz8n5jSrdzf53LSAuVmu3wJeZlBQuOQheHPwUrb3AvyAydFiTI2fAYY7MEfqVadkGQu2hIfMKGsWpeeJvh5GF-QYEksxA3zpXdq0qlE_uajoOMWJg1aCkkrE68ZWTlzorgTEJgDi_0GVsH9v_KdbdKFB6TF7bCrlw_siFl5VZftarqCQCO6_0s3iMe76AZ_CzXbJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uahYTkW79XUlZSKfNU6yNnTJ_6yRA1KHgKjzAI3UOm0E3x3bpPWwwicaM-yuvmSKQbxCHOiIU6ogGr5NNWcuSCKwoYkFFHynqOXx4s8G3ch9Ds_TOZVGG59mYCpxczzRhsftvwR-DZlhE0pKH0aWHAh812Wh3ii5_BfYRyemu7pZ0m5F4pwm7Zy1nn0NR194IaBqgimhtcyUlDrxtQW9i4h8gawDqmJETq1506ShlQyl6FL8lwtfcf3rp0MoTWLnPMHVWgAt1Z3DEZPSzYZk6egoKLxJzHolBW8ClGtxCYdFHqtFZNZ_Osm2dPYmwJP6BPr2CM4iifJmZMyXFYpOtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaQeQ2uEGzliFkqAAfPNzTcKo5AJfVXdrC8YVV6vb8g_k8LX_EKQc83Zyoo26ccAlISLPukU0ZsrAkKRy1TBoChxAbSnIMFpWJAzTUTXdIX2hIZYgNgJqWB9TpfoGqOteOPDVBtdSlDTUIhgchJu8nil_WiTEhq55Y4rGTeG9yp0y_7yhoIkkCIEY-hKa-opEqu2rZScjJnqkr2lowMGo1DFVe6ATu7lbgoWhaXw5k1yL7IzHnrL7vy5lZqxxOTurHlRKSZRmyPKhZ0l5DoaeCLQfaLoS65IXkbENCg2eGkEjP_OgzEBFyh0QZmS83RiFcBwKHptnItNhAmvjItspg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDQmCt6Qh_x8jzKO_Tfa-eE1iDNyhxvzepqLybCktbdiobGKTeME3t-zzhoVCeZ6GkwHwezoZXe4nVx71thmd83LQbr4uMY2_zBpEQh7e4ynXZN2KeJNC_obFBIm6Dc3xfBXd0naRt0HsmsRPpg1Q6ITXqpQvo87QS07vLfKrb-i_UPDYELyW7kFvz8pg0ng68ZSvWQxK9QGU68EmHZTKbuJqn6XaZPcVfi9qqe2OxNgAliOtSjnJxUkhHWqIg6ZPR1KV91e5-yQMkPDlJuIya1hmVvg5KsyW9xxCpyHwvCDVRp6YwuvMVT_7m3ZtWStPKdXTP7Iv6m-ErxGhI1K-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2FWK17CxcW9HRKJWWfYe55ZmhH0-MAEaoWlR4bhUma990k0TQZwjTdHAY27MqAelWfjSHDVkUa8sqXdcez2tqtseTqQdau2VyMG2QCCrdC1kItHHbtopIjeWoH9WdR_Ms-3Bq7Qdsdk4K6tawyXOfwDYPYF6sJmKBrIgrj64UzgRZOPQPP1yWRmBddJlO1fxJvKw3rhrufIoHI6fz00ydj1M10fo7Toad7MGBQd2VvefnLr8m8AJI4f8Pj514eJgnb_kvM5Os08hl7lnD9VwOamBiXOgZMBT7TnElrfaT39uONUqIOtybaIWKUPJWPwP0P2uJ6ynu9JJiaJyYdNRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUaoBS89l3b7mXNlbjaiyCI4CGytcHgJp19XuEYWgw0Fa9WjFOlYdkoQRSN1pKGDpT_S0nAritX1Xb0FuRDRCMex9xeoJP4T9P7FVGKl2FHDZ1ROz8b0OdzB_i-zWIWe66BYYyC32b6wddo5N-q2yG3mDEaIe0rw3pVkA6VCWdVSMYQXkvR6BgoRbbH6At41bJAuWWmNp6HINk7HuNV-EhoBmOv24ve_qVMNejkCEnWZM25YiPrC5qP7GwP_avehlMVOCz1W80BAa3payZRdAPfyFS0Erz0IFRv6EwnyYoA2by2FMXMe6irBOBHKEXOK_GDZdH8G-9ezZvD9AJUUbxNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUaoBS89l3b7mXNlbjaiyCI4CGytcHgJp19XuEYWgw0Fa9WjFOlYdkoQRSN1pKGDpT_S0nAritX1Xb0FuRDRCMex9xeoJP4T9P7FVGKl2FHDZ1ROz8b0OdzB_i-zWIWe66BYYyC32b6wddo5N-q2yG3mDEaIe0rw3pVkA6VCWdVSMYQXkvR6BgoRbbH6At41bJAuWWmNp6HINk7HuNV-EhoBmOv24ve_qVMNejkCEnWZM25YiPrC5qP7GwP_avehlMVOCz1W80BAa3payZRdAPfyFS0Erz0IFRv6EwnyYoA2by2FMXMe6irBOBHKEXOK_GDZdH8G-9ezZvD9AJUUbxNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBwSh2BreVIZCAQOpCorcxE7OKHSKpmR8FA1wztHwqVVS5IApHqoUBRUVYxVqhMgVQTcukiOUMbHcu57-ze5D1cqfXOIpCf3VNvImyGc-yqmHjtDgSWylPmJG4XDh1s7VebZERsOhLZoe5wa0F2INCfK474cp9RggGCPuh6YClXnj09erpm3-PE_6Lsmx45ZyGv-2fdNd7rvybxu8K1eNJBQfdlXLGIM0R2uBDRZYd4GW4BlcVN-aSNw8XuxMknYEkWLVnABisux1io718VF1AgSD_ubL2YsSWX5DQDM4pa1b9Wvj54bgKpK3ExlpPYJnHzAkZlkb42iMklggPOlRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ge24SltxqB5v-GrTWIoOWH6ctZYzOEVNEXvkegyTBLxosbX0_tw0CTOLDArUxpYD8uGELxIfFnTUcZIqNt4sxiJv-j9g1NWrV-No7lwunA6dxqrk4z4F95dcO2nTyFfEKCBwlPJLZgH2KLmlYZZ9llQzo-uQaOxQKI50EpEb7bqyrO59aT8agjtBiOf9oVl78XDU2cGjikMf7FohG8qrWzbUkp3jBdQ40wbX5lyZw6zkEjjxHK86UqogPmG3fVMzxujMUzdDfXRadlmOvkCmRrz-KCkuSRRq6WxOB-_IrzH1oNDGXEDNQ_3O-czgX9jy5v8MKkTHsosI-qkzJjw0wg.jpg" alt="photo" loading="lazy"/></div>
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
