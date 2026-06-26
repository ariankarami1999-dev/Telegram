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
<img src="https://cdn4.telesco.pe/file/mswG9WrXWmyTnlM6inCcPUKERp5ISVy92UpEIGokcO7d9ep0KC2Bv11jJR6yxU_ahekZsIwnuek-wTbXb7JdQ2pG9eSluC8jf6ruPfLvJuKTcb_bjPfjE5FTkaUgj-M18QKmfglEOfbMEzcj_9pNuq7MhCOVj4uDfd2VMmcXhOTxHslKBmsmWGKFhDQ-XriC864glkL8FNu-5bnMVJneGSY7Rrz8evabqStrRSaKLfGzlgxpj26BxFxDjyHEVqcY_ZPgqguK6lUhi-IE57oXsgvkq1-vC7h9p8a66zfna5byc7f6sf0_pMGkyEhqYTVq5p2eju-m3f9dy1Z64W4-Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 00:32:49</div>
<hr>

<div class="tg-post" id="msg-663639">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
حمله ضدانقلاب به ایست‌وبازرسی بانه با ۲ شهید و ۵ مجروح
🔹
در حمله امشب افراد مسلح ضدانقلاب به ایست‌وبازرسی در شهرستان بانه، ۲ نفر از نیروهای انتظامی به شهادت رسیدند و ۵ نفر دیگر مجروح شدند.
🔹
جزئیات بیشتر از ابعاد این حمله و هویت عاملان آن در دست بررسی است و به‌محض تکمیل اطلاعات، اعلام خواهد شد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/akhbarefori/663639" target="_blank">📅 00:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663638">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔹
سنتکام: ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/663638" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663637">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔹
لبنانی‌ها به خیابان آمدند
🔹
همزمان با چارچوب توافق میان دولت لبنان و رژیم صهیونیستی با میانجیگری آمریکا، هزاران نفر از مردم لبنان در ضاحیه جنوبی بیروت در محکومیت این توافق تظاهرات کردند و آن را گامی در مسیر عادی‌سازی روابط با رژیم صهیونیستی دانستند.
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/663637" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663636">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خبرفوری
pinned «
🔹
آتش بس نقض شد  به گزارش خبرنگار صداوسیما در سیریک:
🔹
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
🔹
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
🔹
حدود ۵ ساعت پیش چند شلیک اخطار از…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/663636" target="_blank">📅 00:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663635">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔹
سنتکام به صورت رسمی حمله به اهدافی در ایران را تایید کرد  فرماندهی تروریستی مرکزی آمریکا:
🔹
ایالات متحده در پاسخ به حمله‌ای که یک کشتی تجاری را هدف قرار داده بود، ضرباتی علیه ایران انجام داد.
🔹
هواپیماهای ما حملاتی را انجام دادند که سایت‌های ذخیره‌سازی موشک…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/663635" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663634">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5bf923a1.mp4?token=YCLRNI26zlGrh2vJ6-u2ozSrATphp-oGS38pdktE5e0mSGiH9QE2hI_J20UfaekBvi67S-VvIVk8Ne1PBevNBjkL8oZ80RkA7D35OgLG89a3jEmG8JDJaCPxOQsfnC7EXFeAQPgsr7wyYhH9BU7PDsnv-pL61-QichIYrtc4B17QtuqlCWg42DlAO4Tp2lKeUWjTGGlf1N9UYHIP_ae8jBOq9UlTnVfClv-wUnNALrAseehhPZOgvfEGGyeTxGbIbILgLVZuhfatmVgOgFH2-0RHyXYq00Na9kWKE2NL5peN332D6hBFENFh7yQIoP8g6wlwRv2xgE_hOHGQaQ5NYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5bf923a1.mp4?token=YCLRNI26zlGrh2vJ6-u2ozSrATphp-oGS38pdktE5e0mSGiH9QE2hI_J20UfaekBvi67S-VvIVk8Ne1PBevNBjkL8oZ80RkA7D35OgLG89a3jEmG8JDJaCPxOQsfnC7EXFeAQPgsr7wyYhH9BU7PDsnv-pL61-QichIYrtc4B17QtuqlCWg42DlAO4Tp2lKeUWjTGGlf1N9UYHIP_ae8jBOq9UlTnVfClv-wUnNALrAseehhPZOgvfEGGyeTxGbIbILgLVZuhfatmVgOgFH2-0RHyXYq00Na9kWKE2NL5peN332D6hBFENFh7yQIoP8g6wlwRv2xgE_hOHGQaQ5NYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اعلام رسمی توافق چارچوبی دولت لبنان و رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/663634" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnX2dNY9enoCy6_W5cKX2-mUJzgWSKVfFRuuilJHW75aikKTFaPevZc7q3re5NqgA_cmIBsggdMNFsBAWx_qpaQHoyIGSIHm-PUuZtFalrQ4ZQXEcDWp73FZnWQD8NrI4BQWVP0t59JtN6b-U1Ekf3r_nnapO3kxudctJdbLCsdK6xPdPuOq8c2muP_WDY_qqypWiTVDs_bJWtSHe7hUGon4eGBZn46YDigDqDnTtia4IYQQF5qsQBvFYD9wG40DWRw_Y1nvR6ZMeHEvVyRD-VtVvtDxAZLhxewDETViiCoV6vsEdQzqEJzTwiPd_vHl4dNG_FJcCXnwf1YPIgFEOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سنتکام به صورت رسمی حمله به اهدافی در ایران را تایید کرد
فرماندهی تروریستی مرکزی آمریکا:
🔹
ایالات متحده در پاسخ به حمله‌ای که یک کشتی تجاری را هدف قرار داده بود، ضرباتی علیه ایران انجام داد.
🔹
هواپیماهای ما حملاتی را انجام دادند که سایت‌های ذخیره‌سازی موشک و پهپادهای ایرانی و مواضع راداری ساحلی را هدف قرار داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/663632" target="_blank">📅 00:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔹
آکسیوس مدعی شد: ارتش آمریکا حملاتی علیه ایران در نزدیکی تنگه هرمز انجام داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/663631" target="_blank">📅 00:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
خبرنگار: شما گفتید ایران آتش‌بس را نقض کرده است. آیا با پیامدی روبه‌رو خواهد شد؟
🔹
ترامپ: خواهید فهمید.
🔹
خبرنگار: آیا همچنان معتقدید آتش‌بس برقرار است؟
🔹
ترامپ: از این خوشم نیامد که آن‌ها دیروز چهار موشک به سمت یک کشتی شلیک کردند. ما سه تا از آن‌ها را ساقط…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/663630" target="_blank">📅 00:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpmh7VlBBQuKVl5X94etInsB3GplyWAwM1GfZv5hKn76Sh0wIriQ_491OepMbf-YkuRorZRILytnMIqnUJooUuUX03aCEYaBVR_J1zgQJhcmYmqc0GQNoOWB229FRkmrTkus3iEc1TL98eDWg2czJZ3cekadTiRQkJVs7fOkBVpO9NZmLDincz4VmCD04H_tovAUod-EhDfSSVJxY-94cXZK-H4DwaRi1OHnx8wGkQRiOaz5PV_0QjX7PvKaZJtORQsMypTf0-CcaF1LVjnEaxNTX_1_fhSIbrUtkedP1lt-NCpBiW4U5ApA7ot1E-Ar17Js26mpZYJRSPagnHvEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/663629" target="_blank">📅 00:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/663628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/663628" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/663627" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/663627" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
محسن رضایی: رهبر انقلاب در سلامت کامل هستند
🔹
سازمان‌های حفاظتی و امنیتی، در پی شهادت حضرت آیت‌الله سیدعلی خامنه‌ای، محدودیت‌هایی اعمال کرده‌اند.
🔹
رهبر معظم انقلاب مسائل راهبردی و منافع ملی کشور را حتما نظارت می‌کنند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/663626" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
الحدث: سخنان نتانیاهو با آنچه در پیش‌نویس چارچوب توافق پیشنهادی آمده، در تعارض است   الحدث به نقل از منابع سیاسی لبنانی:
🔹
اظهارات نتانیاهو فراتر از مفاد پیش‌نویس چارچوب توافق پیشنهادی بوده است.
🔹
«چارچوب توافق» با اسرائیل به‌صراحت از «استقرار مجدد مرحله‌ای»…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/663625" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663623">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66c2c5f5d2.mp4?token=cKKxz4ULtqIg-nl9tBEFx-IMlRWXUG5QMj6G6MTYeo6ns0TFLMDCiZu8Su2i-PbpXAs--VA10_U8ZsNxMin8q8i3rjYqHkcCNzJn4mHbyH_UWJtEzVBWbZAFTG1ynakPJ2TqO8Ga0CgfAFIch7y7f0xOeUuqFD3lM_lgppYGMaeW1khWlarpSq51jmEqnk2R1VkfQdlrL8w10Gy-_AWxHhncw4XrIQHmauxMBlmkzRsqcAvfApe-Z8Z3C23L10fENXZVUDi24q71b7mn0Gw7maniVbPGUmaUa1VhA2gKUINkOSb_pykrQqDViPjoGE6J7l28Re7Mf-MX7KcRqGmziA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66c2c5f5d2.mp4?token=cKKxz4ULtqIg-nl9tBEFx-IMlRWXUG5QMj6G6MTYeo6ns0TFLMDCiZu8Su2i-PbpXAs--VA10_U8ZsNxMin8q8i3rjYqHkcCNzJn4mHbyH_UWJtEzVBWbZAFTG1ynakPJ2TqO8Ga0CgfAFIch7y7f0xOeUuqFD3lM_lgppYGMaeW1khWlarpSq51jmEqnk2R1VkfQdlrL8w10Gy-_AWxHhncw4XrIQHmauxMBlmkzRsqcAvfApe-Z8Z3C23L10fENXZVUDi24q71b7mn0Gw7maniVbPGUmaUa1VhA2gKUINkOSb_pykrQqDViPjoGE6J7l28Re7Mf-MX7KcRqGmziA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ جنایتکار ادعای خود درباره شلیک پهپاد به کشتی در تنگه هرمز را تکرار کرد  رئیس جمهور تروریست آمریکا:
🔹
ما هنوز یک مبارزه با ایران داریم. آن‌ها چهار پهپاد به سوی کشتی در حال عبور در تنگه هرمز شلیک کردند. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/663623" target="_blank">📅 23:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663622">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
صداوسیما: دقایقی قبل شنیده شدن صدای انفجار در طاهرویه سیریک
🔹
منشأ صدا هنوز مشخص نمی‌باشد. اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/663622" target="_blank">📅 23:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663621">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmqCZGzj6SresqEVQWd2iEMTHRmykKQlSRodakGfb9u7dgvulvARtFmGQR3q3vkirKo28WTlgvh0XHDpJ20BZj8yDH2BTPLnLTYOGMMrtlHqqnerKe9iZuG3OBtz8Tm_digsNYX4rVqy5LV_mZZPqW2J-9tBGr_U34m_vAZIJV9lvWEZGMAWOfIcGF9rIsLzD7DNDGAp9cnLPZsrTaihxzsms_47wTJYB-QXkcOOcVRotOm3iCPsEwRtMxQvGhejzGpKEoHFKn6Bg2HdU9BO9_BumUfWErLe2Nik-Ftwxm-ZZ1i5Kp8mLSCOjtpCh-nQ_CGBTuZafsNVE8hte_8OWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_دوم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید بزرگوار علیرضا جعفری  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/663621" target="_blank">📅 23:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های کردستان، قزوین، فارس، سمنان، گلستان، یزد، مرکزی، خوزستان، کرمان، مازنداران و زنجان فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند کرد.
🔹
تیم…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/663620" target="_blank">📅 23:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663619">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQqUbDK5aBC3vAZUOgLWilcuXEYIge6sJCf1BVU-7ZRU6QH8_TWoaXoyRYIdLAtDgovypS6UsIPZeT34paONqJnD4a1jrbzhpCSjEF__3k9G4tzpBbYtdrx1SrQw0VFiU5Z9zfEc7_ZZ8AyYkDE5699QmbeBbKDw61JWoZnzG35jiyJdXhq5uGBxSzEMnLb7dwFrj4gjRC84w9PXQL_S1l_kfXpmirEOaLK8yK0RfSdnNfmsXiG3TpdLmg4g1oefM0tThRQ7F45ppmfWAaXu29l8yUsb1fZjfYy4EUSvb5DWaRlNgBT6nUYqnwmRJcwxUynKI7Pz3z12D-kfygFsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تخته آخرین جلسه فنی تیم ملی فوتبال ایران پیش از دیدار برابر مصر؛ «امروز تنها قدم نخواهیم زد؛ میلیون‌ها ایرانی، روح کودکان میناب و روح ماکان کنار ما قدم برمی‌دارند، حالا نوبت ماست، برای ایران. یا زینب (س)»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/663619" target="_blank">📅 23:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b1a67169.mp4?token=MRjxefuw0egUZvxIsYDFfhGvnH7e8rjYKecSzt5O7YNYijK0Iwve9Ecdh2dz5aPTKLK1fYrosrpJIZyh24TKskfcBxQoRZ5sohzvZygNkRBEL51d4quH0Iq27YSK_xCK6nkhHF3RtzkL-eJRyyoytWSJGTPr8wBFSi9yUr8D3upwxA5DzY6A6YSz_AvLz62qTDo8n9H9OrFf7tbWHBPaVCIBLflqPd1ofe69KMA4pn9Ws-UBEA5thgCScfiDOTKy_S4ufBKQ4fD1ZwuEd2RfXk7LtFBbQtIjKi3nvWlBR4LOdfmwy0HpTgPOtdRo0JJdG_jfvi4tzh_NO8b6h0QJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b1a67169.mp4?token=MRjxefuw0egUZvxIsYDFfhGvnH7e8rjYKecSzt5O7YNYijK0Iwve9Ecdh2dz5aPTKLK1fYrosrpJIZyh24TKskfcBxQoRZ5sohzvZygNkRBEL51d4quH0Iq27YSK_xCK6nkhHF3RtzkL-eJRyyoytWSJGTPr8wBFSi9yUr8D3upwxA5DzY6A6YSz_AvLz62qTDo8n9H9OrFf7tbWHBPaVCIBLflqPd1ofe69KMA4pn9Ws-UBEA5thgCScfiDOTKy_S4ufBKQ4fD1ZwuEd2RfXk7LtFBbQtIjKi3nvWlBR4LOdfmwy0HpTgPOtdRo0JJdG_jfvi4tzh_NO8b6h0QJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول چادرملو به پرسپولیس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/663618" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632179967.mp4?token=BbzHUz3BIVmG6dIrT_Lz7sg8y_vD9Qnrx1aTCxC2kaQcfIg5FBw9w868nP5RNBNOABGtLWDNcBKGFIDux1qEhOBn5aXXfdAZpmMTaMWjY8vKITEuvclGjWv0MKuMCJ2RjJPxjMRQg7J6Igq8C2MKka6kt9Iw60E4f8MnY-Nv-dEsG4UzuFMoGnrRttp44WduPj1AOJJ94AkF9NG2TFHQVaiQCbA7EhixPxKt63Vei0AUhu8naRYjizYUHnA0XcwlVFEoT2S8ZeCERqjDxDQXiEo57v-LCd_hff9yxa9VhrmOaYXhPr5s6pDyeKKOerEe5Dl_DukTU1X_OXsFQc9jpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632179967.mp4?token=BbzHUz3BIVmG6dIrT_Lz7sg8y_vD9Qnrx1aTCxC2kaQcfIg5FBw9w868nP5RNBNOABGtLWDNcBKGFIDux1qEhOBn5aXXfdAZpmMTaMWjY8vKITEuvclGjWv0MKuMCJ2RjJPxjMRQg7J6Igq8C2MKka6kt9Iw60E4f8MnY-Nv-dEsG4UzuFMoGnrRttp44WduPj1AOJJ94AkF9NG2TFHQVaiQCbA7EhixPxKt63Vei0AUhu8naRYjizYUHnA0XcwlVFEoT2S8ZeCERqjDxDQXiEo57v-LCd_hff9yxa9VhrmOaYXhPr5s6pDyeKKOerEe5Dl_DukTU1X_OXsFQc9jpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
هتلی عجیب در عربستان که روی آب ساخته شده
!
🏝
🔹
هتل شبارا یک استراحتگاه فوق لوکس ۷۳ اتاقی است که در جزیره خالی از سکنه شیبارا واقع شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/663617" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔹
ممنوعیت استفاده کاربران زبر ۱۶ سال از شبکه‌های اجتماعی پرریسک در اندونزی
وزیر ارتباطات و امور دیجیتال اندونزی:
🔹
تیک‌تاک ۴.۱ میلیون و یوتیوب حدود ۶۰۰ هزار حساب را مسدود کرده‌اند و دولت انتظار دارد سایر پلتفرم‌ها نیز همین مسیر را دنبال کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/663616" target="_blank">📅 23:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109ad3478d.mp4?token=BtGigCaTxUSUZukBiIX4B1_P0lL3qBK77DPA_bThMcGlBn-Egnst0FnwofmpioPpGv4tFYSV03EUSZ-g_-lgGEuSDYOO2IFLxhFkNzQLXHMgYI3UA6nW1BB7SeEGvGqaBqeWEWY6aDkM37jWyx7MCN_egzjs5cyEqmIPrPeepPu4xR0aqOKWZZtwHLHs4TJfff2z0d8lMt0LsJ5FJUW1hUSXNIu6JTRg-9aJ_x-P_qPboppMqMlbRT3L46M8dw6YYO5xRasvucnAedZBZJ_m9lOUxG8_ZruDhPFuxf2TsDj5LuMo1KHsduFZ1Fk11fZbrh09nSAg_hf3DAJNikydWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109ad3478d.mp4?token=BtGigCaTxUSUZukBiIX4B1_P0lL3qBK77DPA_bThMcGlBn-Egnst0FnwofmpioPpGv4tFYSV03EUSZ-g_-lgGEuSDYOO2IFLxhFkNzQLXHMgYI3UA6nW1BB7SeEGvGqaBqeWEWY6aDkM37jWyx7MCN_egzjs5cyEqmIPrPeepPu4xR0aqOKWZZtwHLHs4TJfff2z0d8lMt0LsJ5FJUW1hUSXNIu6JTRg-9aJ_x-P_qPboppMqMlbRT3L46M8dw6YYO5xRasvucnAedZBZJ_m9lOUxG8_ZruDhPFuxf2TsDj5LuMo1KHsduFZ1Fk11fZbrh09nSAg_hf3DAJNikydWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل سوم فرانسه به نروژ توسط دمبله
🇳🇴
1️⃣
🏆
3️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/663615" target="_blank">📅 23:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔹
ترامپ جنایتکار: هفته پیش یک توافق تاریخی با ایران امضا کردیم که هیچ رئیس جمهوری قادر به انجام آن نبود!  رئیس جمهور تروریست آمریکا:
🔹
ایران هیچ توان دریایی و هوایی‌ای ندارد.
🔹
اخبار دروغ مانند نیویورک تایمز می‌گویند ایران قوی‌تر شده است.
📲
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/663614" target="_blank">📅 23:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4812728452.mp4?token=cILu1pzN_iJb8UAMqeAJ4J7NiJfaxZOAtI84JqTC9sKjd5UyEPz32suj2T2TQ-qsu3DZ-8kI_b2VY6o05Rpc5vbvskOJA3jEbBp2PRkqkA5mDR-vJSAmPjmLOg8HIedNZr0xfxSxDlJia2RGxhDDvNVg6-DbMeEA82vuufQawUo3zpiH9x62b0xMEpHlroHoPWzBxJvFTYdCkBrzSGnREujDY9nHlpOf56zIPZmBSDwH4TFxFm8Mmth_2wYCJVO6t2pzYCP3BcCirs-7US7in8lHWiUpCeYTyeUB-yCm8QAFKUnWzxvhhi_4fqzYEs95gn8LNv6l0jz96lLmhOG0sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4812728452.mp4?token=cILu1pzN_iJb8UAMqeAJ4J7NiJfaxZOAtI84JqTC9sKjd5UyEPz32suj2T2TQ-qsu3DZ-8kI_b2VY6o05Rpc5vbvskOJA3jEbBp2PRkqkA5mDR-vJSAmPjmLOg8HIedNZr0xfxSxDlJia2RGxhDDvNVg6-DbMeEA82vuufQawUo3zpiH9x62b0xMEpHlroHoPWzBxJvFTYdCkBrzSGnREujDY9nHlpOf56zIPZmBSDwH4TFxFm8Mmth_2wYCJVO6t2pzYCP3BcCirs-7US7in8lHWiUpCeYTyeUB-yCm8QAFKUnWzxvhhi_4fqzYEs95gn8LNv6l0jz96lLmhOG0sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
لاریجانی: اگر دشمن به ایران حمله کند جنگ منطقه‌ای ادامه پیدا می‌کند
کارشناس ارشد مسائل بین‌الملل:
🔹
ما با کشورهای منطقه مشکلی نداریم ولی همه باید بدانند که اگر علیه کشور اقدامی انجام شود جنگ منطقه‌ای ادامه پیدا می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/663613" target="_blank">📅 22:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663604">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUZ5dXw8-8Nw58O-jluPMkH-qlH4xqSU8wEUzpv8bAVHA92836eZLSIoAlp8Yw6DZ2alZELlXEQIbfYO6pxoLK4ARIuS20NzYHrYjBu5Lige-9g1JMJW3DoiMih_j4SVvKXpb_xrxKDfjJ8jCo6ajbEbU7fvdykzogXEq3otob6jF2wucP-lj1WFq_2Yhc96k9OMGhcexj2xSI3ZX5KLpyQXdD8lHwpex0BIAHdyrUZ-S5EuWTqL8rHOPTEY2nURaoqm3M5zKqKzBmyuMauep6QO1xBVYuLaZUbV_V4S4spIQz9_OxARWXjH2FxsLVATUnewL-ZSwrlZe89kZZ-DbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKGrEDVO1D1QJIGjoc42TbN0nAYrH0iwnaFD4VScIg7EmBvUBs3VdH7ElO71Eou6UTjzUf2ky6mN4ElNPmCzh-0qePM_wny6ilRbOw1Tel-X-w1fiCYMBThusWC5lyq0p6kQnzEypgQjuVpLi58yUMtAXlmq4CjpvKSo31jl49uT99B9pOXrs1nM9Fx-xBGayhnA6nmUAQ3YiHRbvidLbPBpYpOgOKHr3GmJywlChkkeujjcBeFl3G1JuRKUpaDIVerMAjYOHRp0FAF8IjUMQBItxor9bajwbnbB3Ca0tD_woigKiGbU2esFwwC5IBZEADFuD4UI8c3uQIPTh8FXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnaU_k5ctdLU2hL-eLesXA-xIVuUjTC27LmMbVRwZsgUOjQ4xSJYLb5_qwheqTZbZuXWj1-X6THvGLncffAF85ENjmTYzjZekeliYVR7jeGHG-Gk02lAssmjiWAq1zJU5WErr5ilu-14xG80VL9tgTR954opmn_kv143OaU6LNsfNbd5Sa2IUMSAh__X-DNBIH69AoHRCloYnQXRr_kb2AroQwgaTAOhQwvI_68RKGOgOFeVFp6AqOyR5zhXWiaWdJpU8RBRjkipw-LFzcORr3Y4GPoW0ziygRcN_FXT7DmPEMWVTQJsvrpw_rB1vok46P3IeZTtTE1j3wXmVU6fIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzdL6WmLAZIWaPebsbgzDfmznTLiTednofreblPhypjSolK_S5cNdOl0J-RqRR15mwe5Hwf_0u7JFQSrIMeiOztmLBXKeDRNAbdVuXNFoolO_W_y2kg5kW4dLIXS96F4ggBQQvzqhFj1VplCG-ZOIDJMIHH9u29E4eNkxIoUkrIQHTXzqH6NQ0R3sgHaOBMbt3WkF6QBE-QOLdxnWcf5jtTZbXr_wY5Iig94h-QsewUB-7GIimSlebv_tvVhqid81P_1V52GvZApmyGxxxLLpQDFwteuM110wwYMimloyaTZK2c_AF61oCyk7w7yzEi2vPMwpCNxMyOBNyRTy--sog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI534rfu35kI31iGJl38esLCXpT5oXBP3J067A2W4DCupTvkOEvpq0D5atP1azRVH_fOfRA16xqOiZLiAx_11R9TOaZ7w81b8RG7T5LxUHg5GdKn0uy-0HYP3zwWTn6gTAqg0206tiYkfw7Ggsd5OQRIE1mRZbxHOU_N7KRJpSW66c2dsgyetF4LOnAEy8K36UOxQNikYSb6up6U_lMgg5gYHHGa6JuaptfusRtedKFZIsSZnHFwUD9BSnOu8DISvXsyruyG3t4UFAtrrwOpXvif0nIyQ5-S9dNx8S0xYtLzubxoPCau3ybLDX_o12KvJIgAet-jY8khZErLhgt1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIKE3rhWpBl3cRjX8Y_OR-vfLwE3s8mxMLTnv9qzK38GdMZPgRKceso8CBhhjOA58b1qPBnVnQ1-lkIv-a3inxaCf1X53dwYLgUvAZvNcSFWw2lUkpDMplfpcghDgdFXJ7wZO7j_gybsYhrZcP66a0cn3cp9Pgg_hO2tNzWt4z-AaO_PdMP4MCfU7YolErSe7uKX9ua7cMsmJFMm3pjQDoPw5iAen7ZeOT7l4WyydBFuiHC0s6UWfOh4fNrSqmXN4Re43f4vEMgaN8fJoDUTpx2vZaSQjJeBUKQlxN7iVjelFpvwvmWWcrw3Bko9eS6oslEijiphp-sutpdc0VM9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rop77K5g9BMBWAcjk3QKNI904jfmI3iAlOzTesXVyb-goW_ndzmP7iZNBQwb_l1m32vqxKhaXMicplfA3lVvl_OmsvfkeK2z2vchyf_4bM5aheh0h3bheHQRPDHXx5YvEMP-4W3WsWT3ZeS_ppjZ6oanBPfFBcNO4VcHM02xc7voEB-ZL5aBp3gMjZWTSJAA8sRa42-TwI6zINtFYQyvRm5cwHGDy1LqXYgWehXitWBtvGWIRjU-7_pBVQDJwYNAnSLmsQejPmMLL1ywWDIWkJkrjml9sHPB0MLUvcBkLtJ4XHCMbQIflQWuBN3ZSmtE2O6qRhM3so6g6qbcDhVIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9nlbPtYFd0E3YDZnmCLwk7CWk_omZbLdMHsqSgvmo0fZtYeh0pP4v87TbA5MQoU7pIsmS9QS8WI82i6rbI_wT3PKNnaFpYWxDn1XyrYVYNHgI3IjVHpD4UpcoRQkjNjaNyfgzAMYi7-uG_hj1w2ajuxoG29ZNc2iaBPOiiywGOhyKcWp00zwE7hzxizTD8zMUtUKASwFhFDC5wTBfkSv4qn7q3Wx2VnxyukX6zmxp4O3QoTQd36WlMxdHJwG21QyCumDxmn5LIb8hbR1Yk7KC0HesYW2SH88VpwVmhQy0BefkzSVcQZzQdik3IKQwtiqu2Tuvz1iBq4jpO6C4Fwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hx-VJm6nyE4tJZa68oGCWA6bN4TNJqGGiRi-Sgr1Sfo0UjGa1OcnWbWIs72uBFoMxQK6r5wNpiXJ6se44stc3kvssM-tAvWKrKbub4HWkpNBeH0odtwaPWUeOsw9cNwK-MCjp_VxnmRpW5LE0TJREar_f18OUyBpJhq5vocQBb9MOhsD19qUBvkUPqHxL9m1NKWIOy6qALqNfYwsECdFf0N7yVBRcFsar_vYSBF1sEvJE70_Vl9vn4fpdS2ukZaswqYg6nF6XXo1OKZDSeIqp0LJHRk6MPTlPaivwKDgQQ94wMh5higEiYMM_DXxZXJwLCDSNkraWs6NEVMgklwG0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
این روزها،
#همدلی
فقط یک واژه نیست؛ حضوری‌ست از دل‌هایی که برای محبت اهل‌بیت علیهم‌السلام در کنار
#هیات_قرار
ایستاده‌اند.
💫
هر قدمی که برداشته می‌شود، حاصل همراهی مردمی‌ست که بی‌ادعا، شریک این مسیر خیر هستند و چراغ این راه را روشن نگه داشته‌اند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/663604" target="_blank">📅 22:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663603">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6875a7557.mp4?token=MtBWNqXw_IEhHRNyR7Is2Kc-_BqKgO7Fa7baJJ8PE2cxaR8M0lU0ztWxDe_gcZDYIKtEFEkU6a8h_2rC54y2NF3GKzDNNxRuCxanZU4wQtaPnjtABqOhMF-KnkyfBW4AfoEWaPXosjFgA1sgYLhkQWHBanUhie-AngaFMUhL3YCbOmJvtgt1cQfbtNihpQRs39P3Fs85p1QPX-MXMksjoPgj2X6QYuxKs8JL-mmIST5S5MKguknCKjTYzivdKRV2kokCCTg37LHUkp_e9tBzJkHDA3exYYLyi3Qn62ekwi2Cd7ZuTY5EaVPLWnTi9uj5oe5ThY0y02fFI1OJMUY-Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6875a7557.mp4?token=MtBWNqXw_IEhHRNyR7Is2Kc-_BqKgO7Fa7baJJ8PE2cxaR8M0lU0ztWxDe_gcZDYIKtEFEkU6a8h_2rC54y2NF3GKzDNNxRuCxanZU4wQtaPnjtABqOhMF-KnkyfBW4AfoEWaPXosjFgA1sgYLhkQWHBanUhie-AngaFMUhL3YCbOmJvtgt1cQfbtNihpQRs39P3Fs85p1QPX-MXMksjoPgj2X6QYuxKs8JL-mmIST5S5MKguknCKjTYzivdKRV2kokCCTg37LHUkp_e9tBzJkHDA3exYYLyi3Qn62ekwi2Cd7ZuTY5EaVPLWnTi9uj5oe5ThY0y02fFI1OJMUY-Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ، اروپا را به اعمال تعرفه ۱۰۰ درصدی تهدید کرد
🔹
رئیس‌جمهور آمریکا تهدید کرد کشورهای اروپایی که بر شرکت‌های آمریکایی ارائه‌دهنده خدمات دیجیتال مالیات وضع کنند، با تعرفه ۱۰۰ درصدی آمریکا مواجه خواهند شد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/663603" target="_blank">📅 22:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663602">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4a64d6f1.mp4?token=U-L-jRULh0oRDTbPfJ6CP8BktYgFnZ_PrHPYzVR64q-X23L2WS_aJvdYKm1AX4RbQN5ruXuGFqe0ybOakinueUfbj6wny9DuxQtj_FiGbcOQn-vAVul6FVZAsk1-Gr2s5kR7PERPcZVsHVRAY85hOkermgSjrW017d6bBmU1rjfA8TRovZipYboNt2K9lCMxp_E_I1maYi-Se3fqsJUSm6lz3w_BTNUgJVoNzT_WhNuUJs-zea9w2zQ_nULO2Q9A2Xc18W-FFA-Doxk_PK4AVAfsP-4rstLZnUU6SHnWF1TLgNz6lGC0o2MvoDFaiPmjhN7ipwcpMnxHSVLEwmKMDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4a64d6f1.mp4?token=U-L-jRULh0oRDTbPfJ6CP8BktYgFnZ_PrHPYzVR64q-X23L2WS_aJvdYKm1AX4RbQN5ruXuGFqe0ybOakinueUfbj6wny9DuxQtj_FiGbcOQn-vAVul6FVZAsk1-Gr2s5kR7PERPcZVsHVRAY85hOkermgSjrW017d6bBmU1rjfA8TRovZipYboNt2K9lCMxp_E_I1maYi-Se3fqsJUSm6lz3w_BTNUgJVoNzT_WhNuUJs-zea9w2zQ_nULO2Q9A2Xc18W-FFA-Doxk_PK4AVAfsP-4rstLZnUU6SHnWF1TLgNz6lGC0o2MvoDFaiPmjhN7ipwcpMnxHSVLEwmKMDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول نروژ به فرانسه توسط آسگارد در دقیقه ۲۱
⬛️
🇳🇴
1️⃣
🏆
2️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/663602" target="_blank">📅 22:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bdf9eeef2.mp4?token=SkHPlGMGosvPNqNO1Ar2KeZpSqo73cNoGs7uzgVPncVPK6i1Wg1AElk92bwPHyqTA6Icdcfn8ZDQjBjhD7vOiPc2z93mdt2KKSlTBYhO9lTtXBZ-eNykxCECmWm_2wSETjMWAkOcwxK_B7rILPp8-MOHI5-nOioAcSBdmOyA4-yNzbu7hHN7u9bMygxNHXNfHnDAg4hlB0-ulPl7aIx_otN_ngT9EZLzfPvkJYt5VV8fvBQrLXuWEJlh9H4KhaB-yBStN8GAN7ZFA0aFGDqDTw9AZ-rm9eBhXBC1HC7pjtB6K4OxWfEV5zfEqC7a5IdaZlOeLkUl-eQanp2TLXe7ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bdf9eeef2.mp4?token=SkHPlGMGosvPNqNO1Ar2KeZpSqo73cNoGs7uzgVPncVPK6i1Wg1AElk92bwPHyqTA6Icdcfn8ZDQjBjhD7vOiPc2z93mdt2KKSlTBYhO9lTtXBZ-eNykxCECmWm_2wSETjMWAkOcwxK_B7rILPp8-MOHI5-nOioAcSBdmOyA4-yNzbu7hHN7u9bMygxNHXNfHnDAg4hlB0-ulPl7aIx_otN_ngT9EZLzfPvkJYt5VV8fvBQrLXuWEJlh9H4KhaB-yBStN8GAN7ZFA0aFGDqDTw9AZ-rm9eBhXBC1HC7pjtB6K4OxWfEV5zfEqC7a5IdaZlOeLkUl-eQanp2TLXe7ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم فرانسه به نروژ توسط دمبله
⬛️
🇳🇴
0️⃣
🏆
2️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/663601" target="_blank">📅 22:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔹
نتانیاهو توافق تحمیل شده بر دولت لبنان را دستاورد بزرگ خواند  نتانیاهو:
🔹
اسرائیل تا زمان خلع سلاح حزب‌ الله در منطقه امنیتی باقی خواهد ماند. به ارتش لبنان اجازه خواهیم داد تا کنترل دو منطقه آزمایشی در جنوب لبنان را به دست بگیرد.  #Demon
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/663600" target="_blank">📅 22:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a0e43c80.mp4?token=rIK2d16UmnU-wbN2OCxtcWzaqIAm1yDdO2EBi0TVea8AsFRq9p3o573XlHZrwRrCAilZ6iL-WwCyhCXCciAzMD-9NgD3aGhkvFJ-aSO2Dg9PZi8VCw5FR9uIIwW4aGkIG3uBefpxYNqLYlU_K9Tf4II4TGK9PWWzr0R1-jQpJM-j5xf74yNfVucCfb4BqNHRc3kYkT1KeGxh4WkkiDZjQxIf38Ql3zBa3CM93vnB8XUgd0gqrEfXPVkRf2SiY6KZm3dcG53I6kg92qgLxKwt3f3nSAqCDeIeMw_sOx8ypVi3kIq7IfoaI5vt9FOe1C9G_nwiLv4k6Ku5XunOJN6pRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a0e43c80.mp4?token=rIK2d16UmnU-wbN2OCxtcWzaqIAm1yDdO2EBi0TVea8AsFRq9p3o573XlHZrwRrCAilZ6iL-WwCyhCXCciAzMD-9NgD3aGhkvFJ-aSO2Dg9PZi8VCw5FR9uIIwW4aGkIG3uBefpxYNqLYlU_K9Tf4II4TGK9PWWzr0R1-jQpJM-j5xf74yNfVucCfb4BqNHRc3kYkT1KeGxh4WkkiDZjQxIf38Ql3zBa3CM93vnB8XUgd0gqrEfXPVkRf2SiY6KZm3dcG53I6kg92qgLxKwt3f3nSAqCDeIeMw_sOx8ypVi3kIq7IfoaI5vt9FOe1C9G_nwiLv4k6Ku5XunOJN6pRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
سیلاب تابستانی در مرند
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/663599" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a5b8fd72.mp4?token=u4UI8HEXqZCp112RgisCdVdekiA-wjx64krd7-5Wvc-edmrlmFkFOcsz1n5XyCntuSSxv59_bEqnWfNfXSPcbVO0bjpvJg72ctz7qBZj_uKhDwFAwPssfuLdi4pGbSiaPjLAgRmLWYrOiYrxE_3nBER9ZDgHZT0JuW5ZOhDIiSu5VqN6bSrnxFfkdJcw1YWK4nKi20wRzN-wXmI5Fk9YaIIbgbMBtDvFjKkzV4q1TqHwtNDuew7YRH5BaldTHza0p0GfejTk7v2yvhTKOP2yGhiky-N9cRu-KSpzHVpt3nnd4X_HgK_X34-674BRFkxun94GvU6rX4PC9DxmlVb7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a5b8fd72.mp4?token=u4UI8HEXqZCp112RgisCdVdekiA-wjx64krd7-5Wvc-edmrlmFkFOcsz1n5XyCntuSSxv59_bEqnWfNfXSPcbVO0bjpvJg72ctz7qBZj_uKhDwFAwPssfuLdi4pGbSiaPjLAgRmLWYrOiYrxE_3nBER9ZDgHZT0JuW5ZOhDIiSu5VqN6bSrnxFfkdJcw1YWK4nKi20wRzN-wXmI5Fk9YaIIbgbMBtDvFjKkzV4q1TqHwtNDuew7YRH5BaldTHza0p0GfejTk7v2yvhTKOP2yGhiky-N9cRu-KSpzHVpt3nnd4X_HgK_X34-674BRFkxun94GvU6rX4PC9DxmlVb7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تابستان داغ از راه رسیده؛ با دیدن این فیلم دلیل واقعی استفاده از ضدآفتاب‌ رو متوجه میشی
☀️
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/663598" target="_blank">📅 22:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/140d694557.mp4?token=XXBkxDIdLcHDqdM8p3Esy3Z8fJMlHz79sZYuW9lD_dSse-2lz_NvoN-4aWl2zBqUQJGPXK81fZfhH0yBlRN0eiVtFv8VexEvmDyyONXuwANjhhJSXfVDxDuA02ulb-eJmow66WwIURtN7OMzXMRxhSbQrcHm-8XMlOikdYL-8C4QV9KLly8sT8ahvwiZVUFw7uufcdfbpMsRq_rYRInl4L7Fv5YfUCvnl19Pt3xDXDwhXdmVo9EUxrW7W-h-TpX6H3Xgcw45wYpBVyrwAwWcAShPK6Z0dxg-RzY3H97IDnDGnczvJWLyoUBmqhCNol1mseqbOIAaOh3BTJmKGXf3BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/140d694557.mp4?token=XXBkxDIdLcHDqdM8p3Esy3Z8fJMlHz79sZYuW9lD_dSse-2lz_NvoN-4aWl2zBqUQJGPXK81fZfhH0yBlRN0eiVtFv8VexEvmDyyONXuwANjhhJSXfVDxDuA02ulb-eJmow66WwIURtN7OMzXMRxhSbQrcHm-8XMlOikdYL-8C4QV9KLly8sT8ahvwiZVUFw7uufcdfbpMsRq_rYRInl4L7Fv5YfUCvnl19Pt3xDXDwhXdmVo9EUxrW7W-h-TpX6H3Xgcw45wYpBVyrwAwWcAShPK6Z0dxg-RzY3H97IDnDGnczvJWLyoUBmqhCNol1mseqbOIAaOh3BTJmKGXf3BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول فرانسه به نروژ توسط دمبله
⬛️
🇳🇴
0️⃣
🏆
1️⃣
🇫🇷
⬛️
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/663597" target="_blank">📅 22:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663596">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWjTw7NkFZfkDBD2ooHA_h4PiVqItvui-ooCr11D_PsoMD3R90ERRz4PQLydcqnzViEIfOcilU5KUAMtYy3U5eYEedNsZ8XKv14cezCqtswdOJSrh1WQu1srr97az0reJt9FViWKZsIbTj6IWb4PSeSUYkKl_WO8hwv0_VA1lCc3w2n2hxpLv5UB9d6dvW8iYMlVAPK8jBVnPCXgypHxXEyNjsDB5U94bDNNezcxzm6jx0d5Aon7B5_aSu4W3UyJRbuLM86yrWqf3J7Dv9n7bhQJ7Ry5YFUG2pxyP7NVRYyy-hQIER3HGCiNtUDFvpjmjGQ4q9aVvxeztR6maSS5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
انتقاد صریح پرستویی از مزدک میرزایی
🔹
پرویز پرستویی با انتشار یادداشتی در اینستاگرام، نسبت به استفاده از پرچمی غیر از پرچم رسمی ایران در برنامه جام جهانی ۲۰۲۶ اعتراض کرد و این اقدام را بی‌احترامی به تیم ملی و مردم ایران دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/663596" target="_blank">📅 22:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/emNP-tqLKJZO2neerdRV3-39hG59dtmbDci_Q0FiPsLFvYMI0ddLA5Qg3l3_y8nTe6fdhv4o_HgFKeyDuIQv3PsptxJRpmlkK7cWUu318ssh98myXcR6hr1HmoeuPngiy0jc9Ry18Mrmwn_8fWb9A2tfET6idyrXR2ddIYZoxdBd3UnUZNU7FdnK84ND0F5QiyVsKv6xxxoTQdb8x2j96w-gQPjIaxkQNJQbZ2C81KalFP4YRHT-2Jrc6qeuwKQfDQUqu8s6KIP7vavAf83IhUoFtHAcxCncVctK3-FI_hiZmDPnnwpEYpXKpDXmXRC7B8S-zk-wSEWeT4NgTMlFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGS0AfHPaIx9xKqM50DCDyYfg8FXP9cA80yCowO8RKGWvIeVBxpdsCU0mS9qMJeaK2ywgZwVNYVwhIlKAgLGytDskg3hoXDreAihJm9V5D6HZOaCQ48Dp2S0tNRDNJnZIPuDUkpyvfJZQaMTXeZIZpGvWGT52z6_Gr6wUfaetmXxW4tSZI1-IgfuKA7uy6TUAN8BKyZWdzo_pTRr69NK8gJKZFyO-FROoZWjfWrSdKRLIC45K4ziS0oWWkcZ1Zk5jKpvEAMYArhl_aWqItQFQWGqJ2ST9GpN6UFh9Pt9TQareOMnAb8vv7F32omBH-Z6OYyZdVgs6Pt94U0SWOxYmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
نمایش اقتدار امت حزب‌الله در بیروت؛ امروز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/663594" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔹
گل اول چادرملو به پرسپولیس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/663593" target="_blank">📅 22:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5bb2666b.mp4?token=ic9qf3lFCES07iHo9JCIr-pYHw4D4n9Glsy85CrDEnJEPAygLQiqn1Bj8W-D2q11H-zKFQAAHk4ptI744aUttWxtwHBLS_DIAJLOsy9c2gjO5VtGJPoAeVJJY-yxV4mmOk5_BbCqQfcY9rgVjXwjqMRg1glDdlcDODvS_DfULlkzBROOwVQ76kUNmJeiu8xT5Z7zBqleKQjWArCWA0vE3vlWL_-I_Kr9W6UIOA9ligW0Wy4F5mmkCofKFG7ALynqIPSSe46dwuOiREGJfE3JUV7Qzg4C60GVv4DhMdGhxNKHkpvPw05jplTsyrRtvyN2zpA5hAhwfE3CgSjUnye6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5bb2666b.mp4?token=ic9qf3lFCES07iHo9JCIr-pYHw4D4n9Glsy85CrDEnJEPAygLQiqn1Bj8W-D2q11H-zKFQAAHk4ptI744aUttWxtwHBLS_DIAJLOsy9c2gjO5VtGJPoAeVJJY-yxV4mmOk5_BbCqQfcY9rgVjXwjqMRg1glDdlcDODvS_DfULlkzBROOwVQ76kUNmJeiu8xT5Z7zBqleKQjWArCWA0vE3vlWL_-I_Kr9W6UIOA9ligW0Wy4F5mmkCofKFG7ALynqIPSSe46dwuOiREGJfE3JUV7Qzg4C60GVv4DhMdGhxNKHkpvPw05jplTsyrRtvyN2zpA5hAhwfE3CgSjUnye6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
هواداران اکوادور با تانک، صعود تیم‌شان را جشن گرفتند
!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/663592" target="_blank">📅 22:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae0fb97ef.mp4?token=c8OnIAA0gLK78Qrc7EEiy6e_FFSIlDXjU0PEk_GahLrdC9yHknp52nevgMofecJxSyXrL4gaz0cEhyiXssMsa9wntn9ry0yJHjqBpH7yJOErK5CfHCrVql7-LK00HpHensZDwcWgGlqtgJefFGRvHkf57MdY0RgZUPplaoWv2AwjEcKO3vR0vKQuu7N6MEYHzJ1Y25OA6Kc3HZAksG24j8BgFjmtpe0vihAsjN5En53v_tDwnyp20Wa4RczuLxsw03iTao5rv3VxBD9d-e9pehq-n5Dfb2NAXtTv0G2QE9PK-VfU81NWliLfrOWCptDCeWps6uTNMV2UoRCfygpwVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae0fb97ef.mp4?token=c8OnIAA0gLK78Qrc7EEiy6e_FFSIlDXjU0PEk_GahLrdC9yHknp52nevgMofecJxSyXrL4gaz0cEhyiXssMsa9wntn9ry0yJHjqBpH7yJOErK5CfHCrVql7-LK00HpHensZDwcWgGlqtgJefFGRvHkf57MdY0RgZUPplaoWv2AwjEcKO3vR0vKQuu7N6MEYHzJ1Y25OA6Kc3HZAksG24j8BgFjmtpe0vihAsjN5En53v_tDwnyp20Wa4RczuLxsw03iTao5rv3VxBD9d-e9pehq-n5Dfb2NAXtTv0G2QE9PK-VfU81NWliLfrOWCptDCeWps6uTNMV2UoRCfygpwVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدئوی فدراسیون فوتبال برای بازی سرنوشت‌ساز فردا مقابل مصر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/663591" target="_blank">📅 22:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663590">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnypfWxXY0oYNI1qxdesLL70uxgVKupekskOXl2I0cD9ZergFuVl0bLEOU1g0OGOpao4Vob-QYBYdA2_LnHuS0mpkAvZJigUNGLL_NwRVUMpQ6pvmqSfFIV-G8B16HdKzp2q6fNRbeyxcn2U9kuFcmsMJqNyQOCCbiTOgrcJDEII7butrOeXmCjSl3FRGwgydSzPVWWRidhneTLTK-1XLJcEG6uhP_M-Ww8iijIufsWJQSBrekYwvT4rD5ylHu10lfPK29uZ9_boCD6xfESWBsjofgx_azQXAIhbT72FJ-q1pCu2XRzZOmKJFggS9rUXOJmwLU8krZ4U0bew3cnNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
انگشتر جاسوسی KGB با دوربین مخفی؛ شاهکاری که سال ۱۹۶۵ ساخته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/663590" target="_blank">📅 22:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663589">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔹
ترامپ: دین در حال رونق گرفتن است   دونالد ترامپ:
🔹
دین دوباره رونق گرفته است، دین واقعاً در حال اوج گرفتن است. اگر دین یک سهم بورسی بود، همهٔ ما بسیار ثروتمند می‌شدیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/663589" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663588">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjdbAZwxQWqN-pmQsW-TCzOox16EA3ybxqr57KfvSMFturFBLumAIn5NO2n1JPUCVextzv49HZO8pI4I8hu9gC21O5NYQFAkG8ZLgHDu9IzRpQFCb477AaZOEgsJeecJkmGGOCDlTp4lotC9JEqennPsM_KC9tkmcFvMXJqlcJRfVfDmW0eoCSQYsPVi35M7k-YVboHnnO-nclPM7USTg-YPYJLNkxHa8kUgVsOTKagB1Gfmj5JZEGXXQEKm1vMQJWv6c3DBY66JI9_6Tzh2q46m0RkjZH0EsmrAvbyK_iCeCTm2L9qkKMTJKhz6l-QuXJFMQ-nuJB2OTApMrCeuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
از این چیزی که فک می‌کنی بهت نزدیک تریم
#WillPayThePrice
#خونخواهی
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/663588" target="_blank">📅 22:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
محسن رضایی: دولت آمریکا رویکردش را در قبال ایران اصلاح کند
🔹
دولت آمریکا و مقامات آن بدانند  که ملت ایران یک ملت بزرگ تاریخی است.
🔹
ایران با هیچ تهدیدی از صحنه بیرون نخواهد رفت و از حقوق خود دفاع می‌کند.
🔹
دولت آمریکا مسیر غلطی که آمده را باید برگردد و راه جدیدی در پیش بگیرد./صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/663587" target="_blank">📅 22:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663586">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lttU0cGu4u81N0n1IMsk_q3v2stc-5fsUQ6C02-miHRIz2wLTeQHkUWHxUxbTGQTbppt-QV2GfslvKoxw9kv_Sv0epu3aTFLxefuRWtT0zh3N14o3Cd5X32J9R8hdJja9JCrR_4D4stT1bdyWNnMIyWKhGgydRdr3w35by51kZyPEReUgnuQV6tRu0JSfRCWAdOQSsqx5Kyh0OtA0n9VV_3EhG6zU-WKyWuna6tV2aulW3ObrkAjV86z93pFPISEsEkbtiKLM7fsfkcjEt0zKeLZqmhQCw7vp5nCosahSReodErw2oWqWMFitEOpQi93Tviape9Rb_qRAmaBgIQUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
‏
مارک لوین: امارات به اطرافش نگاه کرده و به این نتیجه رسیده که جمهوری اسلامی جایی نمی‌رود و کشور ما آمریکا هم دیگر قصد هیچ اقدام نظامی جدی‌ای ندارد، برای همین دارد به ایران نزدیک‌تر می‌شود و با آن مدارا می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663586" target="_blank">📅 22:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHiqQPWwwLYPYHqolSu3W9VnfxM3tnlfEM3038aI-TOUCCR3KGmkzjjTWYKirEfzVZcJ3SUsorsLNJheroUzUJM5Q10iosHFjvLQuO36ZoPOyjCcQeO_WbFHRLBPf3jleSvb-rtvPZizhRmjfkP7RMaVQZL9tkDIFRnJvKooVgennPkDu-wmT-PIqu4Q1bKruq9bd43bwSxUTyWnYqJI-vsYe9qifm0D2eXL0cHNI2Kuv8gjfVOcEzpDYI2kXcHt0xVN4Sflz9sPZjwG3TJUHLwfIKkoiUUDpsGujBlhSlNxOc3k9DGROFFbhlyaaElCxCWoG5nQfelZywopMTh2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چراغ‌های رو داشبورد ماشین دقیقا چی میگن؟
🚘
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/663585" target="_blank">📅 22:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3339b8b4b6.mp4?token=EVdZGH_RoqN25pq2V3ndyqRXZR79ZrwZv2RvaGm9mi-O4URobSpYZF3oyH3NuGRVVye8KRGJTWkN1fSzF_rCot8W1Aw24lNleBHVRPIic8Q7hbRcdTUj-HKw1ChNZkq-9WI1-wzqG_e58X6X2O6dlnyKsoekhZgvdpq0MvYsFfN7tSZaqfTX4xvI13f7wr2-I0IJmfJxQidyXvISPXBlBvwsRt_ITkGXADaDajOFDe-Cz0B-zTvVTjg-n0sJ5OmlGmxAM6rsMk4s6FDEYkNBGMOeBznzB4NBEG_3ZYqvtVlXAuJp4LykHjvCXfvU07fRISLvVjfuLPzqaJG6heT6Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3339b8b4b6.mp4?token=EVdZGH_RoqN25pq2V3ndyqRXZR79ZrwZv2RvaGm9mi-O4URobSpYZF3oyH3NuGRVVye8KRGJTWkN1fSzF_rCot8W1Aw24lNleBHVRPIic8Q7hbRcdTUj-HKw1ChNZkq-9WI1-wzqG_e58X6X2O6dlnyKsoekhZgvdpq0MvYsFfN7tSZaqfTX4xvI13f7wr2-I0IJmfJxQidyXvISPXBlBvwsRt_ITkGXADaDajOFDe-Cz0B-zTvVTjg-n0sJ5OmlGmxAM6rsMk4s6FDEYkNBGMOeBznzB4NBEG_3ZYqvtVlXAuJp4LykHjvCXfvU07fRISLvVjfuLPzqaJG6heT6Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاندار کردستان به وعده خود عمل کرد؛ واگذاری منزل ملکی به خواهران آسیب‌دیده سنندجی
🔹
استاندار کردستان که حدود یک ماه پیش وعده تأمین یک واحد مسکونی ملکی برای دو خواهر آسیب‌دیده سنندجی را داده بود، امروز (جمعه) به وعده خود عمل کرد و کلید، برگه واگذاری منزل به‌همراه تمامی تجهیزات مورد نیاز زندگی را به آنان تحویل داد.
🔹
به گزارش روابط عمومی استانداری کردستان، پس از تعیین تکلیف حضانت و سرپرستی این دو خواهر از سوی مراجع قضایی، آنان در این منزل سکونت خواهند یافت.
🔹
واگذاری این واحد مسکونی با هدف حمایت از این دو خواهر و فراهم کردن زمینه آغاز زندگی در محیطی امن، آرام و با ثبات انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/663584" target="_blank">📅 22:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663583">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔹
اعلام رسمی توافق چارچوبی دولت لبنان و رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/663583" target="_blank">📅 22:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663582">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGZXXrXKmugsT7X0a8cKRAzumWX11iCmdDo_PrKqqerYDNbuxKvjcD7h5XDtZbvEB6TECoSY2U2g24mx-mmtzTqXZcjDCWdTCnwd1vG0hCqiRgb4JBEXql9JMMGEtKuwIv3L1bP8vTSbiZcY8I4aeECQMiQOwbCPflJDfAQive0dJWRI8RMQ5sBDCdHQrTWj1inWtyUH72cCJLjNW3ubafsX01Id-IsgVaO4IJ6jNpzxA30l2R42vlCfvTLd40O7dMen72_3MowNiV4z-IaFgog6Ks3u6-eTfj2M6jH3xBzZgIloU1d2D6r82fbDkRNQ7TX54-l7SoYS7ZN9Gh1vCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کمپانى انگلیسى بستنى ساخته که در شب مى درخشد
✨
🍦
🔹
در ساخت این بستنى علاوه بر عروس دریایى از پروتئین‌های فعال کلسیم استفاده شده که در اثر لیس زدن آن از خود نور ساطع می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/663582" target="_blank">📅 21:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663581">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0286efbe23.mp4?token=hvCdFRrx9DJJR2PvJiWda-gNcWfPQD8rChkQQTmRlgU1lyvrAvPMIHg8AyfDxoKea7axx1lArg0HzfF11wGO2jDiGEilNj1P13OFCwtk2x3qpuOI1L72qDNJSeLlnYhAoF-hWxQIqzn2THPO6DECn33Qkqx6BcNX5DXeIW7kIE9IsO3EzhW3xnoXQN9984X7A0XhB6tuS7PdlU00sl9O8aJk5wZwOr8EHVc8X_C2I3wv_xbVY87OKqDil7kZ4FKiTEgM6KncJqixL_rTq5GtCWtVgCN1HUvt1NMB1BlPkZn6pgWEQeVn6Grv7lEHFsbx7s6thCJ5pLLpqQGHh4jd2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0286efbe23.mp4?token=hvCdFRrx9DJJR2PvJiWda-gNcWfPQD8rChkQQTmRlgU1lyvrAvPMIHg8AyfDxoKea7axx1lArg0HzfF11wGO2jDiGEilNj1P13OFCwtk2x3qpuOI1L72qDNJSeLlnYhAoF-hWxQIqzn2THPO6DECn33Qkqx6BcNX5DXeIW7kIE9IsO3EzhW3xnoXQN9984X7A0XhB6tuS7PdlU00sl9O8aJk5wZwOr8EHVc8X_C2I3wv_xbVY87OKqDil7kZ4FKiTEgM6KncJqixL_rTq5GtCWtVgCN1HUvt1NMB1BlPkZn6pgWEQeVn6Grv7lEHFsbx7s6thCJ5pLLpqQGHh4jd2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول پرسپولیس به چادرملو
🔹
محمدامین کاظمیان ۲۵'
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/663581" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663580">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjyqxUlQjFqmG56iY6oGIcdQeBdGLVPfzYs5mWOuzcJYWPal7MGqUPNQB9i-RkSZYQNYfizGmuRuGemhyaqSMOCdBbzT1nm6_3JH4PtAC_aqwYbWaR_7WNRMrIGOctiHSmy2GHbg6p7PBuAHv-KtWHnlq1CbLUhhmZOKXKdEq3OEtOwBcHUP7jZQw99kIrdNk5gt6gDUi7UTpp1Yy0V2xcu4PuJAPFTB4NyNy1OXiFIhyAh47jHS4MklXMI5VooAWmEdx-evE5GCcIlFLXdJWemIGcPywWooGiXCMEXGOaqS9iLpPdwsQZfzs536EFFXHZtb9BOdsv1nuRNmkfYz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
همه خدمات بانک صادرات ایران در بسترهای حضوری و غیرحضوری برقرار شد/شعب شنبه و یکشنبه تا ساعت ۱۷ خدمت‌رسانی می‌کنند
🔹
با تلاش شبانه‌روزی متخصصان بانک صادرات ایران، اختلال موقت در سامانه‌های این بانک به‌طور کامل برطرف شد و تمامی خدمات بانکی در بسترهای حضوری و غیرحضوری از سر گرفته شد. همچنین شعب بانک صادرات ایران در روزهای شنبه و یکشنبه تا ساعت ۱۷ آماده ارائه خدمات به مشتریان خواهند بود.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، بلافاصله پس از بروز اختلال در برخی خدمات بانکی، اقدامات فنی با اولویت‌بندی دقیق و متناسب با نیازهای مشتریان آغاز شد و هم‌اکنون تمامی سامانه‌ها در وضعیت پایدار قرار دارند. مشتریان می‌توانند بدون محدودیت از تمامی خدمات بانکی این بانک استفاده کنند.
🔹
بانک صادرات ایران ضمن عذرخواهی صمیمانه از مردم شریف ایران بابت وقفه پیش‌آمده در خدمت‌رسانی، از همراهی، شکیبایی و اعتماد ارزشمند مشتریان قدردانی می‌کند.
🔹
این بانک در پایان ضمن تاکید بر لزوم  تقویت و توسعه زیرساخت‌های فنی، از عملیاتی شدن مجموعه‌ای از اقدامات پیشگیرانه با هدف جلوگیری از تکرار چنین مواردی خبر داد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/663580" target="_blank">📅 21:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663579">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ad6c9024d.mp4?token=odHs6IZD0rANYBA0MlazwlOkdBuRK8BnTO8dUQlArOQX_D9GWzXJaqZWZjXcRBCyLqEMV2hpZ6tsFyEZDfZPB6o04xkleamS0c-5C0WPOkCvin05GuBrgRO__vTqcitTPmzlxSeuG-uil9Moqs_vXCeweFUlt55T2D3KE70QGzs5VmEVrpvqCDUpM8gfrDG01sQC-9MtUQJLDQB9rckld7I5dBzuylp5Ie1TVVjQpZU74sN-wwdI9VOj4Zt43Aw4o-6hL6GV2UuNDvVqMULUEXwKE9NI9vwVjywQVJhRvoh8Zn8zgJ45DwAwcbCgI-O-_dGtnd7L5Eohm6ynjVHc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ad6c9024d.mp4?token=odHs6IZD0rANYBA0MlazwlOkdBuRK8BnTO8dUQlArOQX_D9GWzXJaqZWZjXcRBCyLqEMV2hpZ6tsFyEZDfZPB6o04xkleamS0c-5C0WPOkCvin05GuBrgRO__vTqcitTPmzlxSeuG-uil9Moqs_vXCeweFUlt55T2D3KE70QGzs5VmEVrpvqCDUpM8gfrDG01sQC-9MtUQJLDQB9rckld7I5dBzuylp5Ie1TVVjQpZU74sN-wwdI9VOj4Zt43Aw4o-6hL6GV2UuNDvVqMULUEXwKE9NI9vwVjywQVJhRvoh8Zn8zgJ45DwAwcbCgI-O-_dGtnd7L5Eohm6ynjVHc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: دین در حال رونق گرفتن است
دونالد ترامپ:
🔹
دین دوباره رونق گرفته است، دین واقعاً در حال اوج گرفتن است. اگر دین یک سهم بورسی بود، همهٔ ما بسیار ثروتمند می‌شدیم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/663579" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663578">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ-QOubcZRnh-867vS2KVv_afH3Ted-1hqFgGswyFQsFVWhxTzNZK9x5QqpGmQUJQixjeMWpBe_6k_StQFhtPD7ySSGvPAz82orMpcnfuKpquyYu7vKIttrj2Yk-8MfA3NfSkKp3dAwB8imOXKuR8YOGLg0jey3QZhQoNjst5KZojQY967vm_oYPPWfJNpljSkiI23xXkxKs157cwtfm8hQ0Dbd0vTDeQPTdcDFxiBEsyq3_mQ3o8jp0joXuddmZXvZHCgv-5mmCBOcI-QEu2NmHKNhNqmuLNF74-j_zvhA344xNxkYnUUC7qWvJ7TwH-VSqJDyvsa1tG0NdjF-drQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیر صعودی تعداد بازی‌ها در ادوار مختلف جام جهانی؛ از ۱۹۳۰ تا امروز
🔹
جام جهانی ۲۰۲۶ با برگزاری ۱۰۴ مسابقه به میزبانی مشترک سه کشور، شلوغ‌ترین و بزرگ‌ترین دوره در تاریخ فیفا محسوب می‌شود.
🔹
تعداد بازی‌ها از نخستین دوره در سال ۱۹۳۰ با تنها ۱۸ مسابقه، روندی صعودی داشته و در دوره‌های طولانی (از ۱۹۹۸ تا ۲۰۲۲) روی عدد ۶۴ مسابقه ثابت مانده بود.
🔹
حجم کل مسابقات برگزار شده در جام جهانی ۲۰۲۶، بیش از ۵.۷ برابر نخستین دوره این رقابت‌ها در اروگوئه است.
@amarfact</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/663578" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663577">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_a6DXaw6cg9BMerDRwmOsaVAW7EKujjg2gur9uzvduPkLoBR1TcQPlJKe1QDXoB-hwY2ejm5kuTHdo8rBU7H9aBHqVrPdJrTdKEl-J3sGy_r-CHUg4_4vXgFvpSwrCI9W0Si6owGqO21s7AiyWmrWYEY2JTQ-euhyfI-4RzlJFpAkUPe9DoXcR4LIKlLAJ1kjcsMIOxq8ENnqJ4x3zV7Wid8NuWyXVioitaFEH9Ecxzx7nJl99P5bN_AEkp79Cx6aQDMX0R1hzgdD6T-7xdolq4ZuczQ4SnoLFZlEOO8qqh2NxVCaJiddBBRBTcl3S3hs6X4n_Wes6HgqDjV7DIvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
نتانیاهو توافق تحمیل شده بر دولت لبنان را دستاورد بزرگ خواند
نتانیاهو:
🔹
اسرائیل تا زمان خلع سلاح حزب‌ الله در منطقه امنیتی باقی خواهد ماند. به ارتش لبنان اجازه خواهیم داد تا کنترل دو منطقه آزمایشی در جنوب لبنان را به دست بگیرد.
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/663577" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663576">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔹
اعلام رسمی توافق چارچوبی دولت لبنان و رژیم صهیونیستی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663576" target="_blank">📅 21:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663575">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
آخرین وضعیت شبکه بانکی: خدمات کارت‌به‌کارت پایدار شد، اختلال خدمات آنلاین برخی بانک‌ها ادامه دارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/663575" target="_blank">📅 21:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663574">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346118b0f2.mp4?token=E9uFQfbbUy61KeHW10oHwqn72aDSHWzRBShVltres4j33-oZPwQrr4Ax886KWwOK5fFZWW7QuK-CGqNNcMO51AsVleH37Yewz8uh-C4iqmEOAzFcG_pQHF72NZQwk4pSrm6uzCt3YVDHrwXEKQV106l_aTEka5qeTRWMa6LLCBKVB8cu5m8Buw3K7AegG8WbVrJD76_--DPLC38zEzTJ2NHNnK8mCnRojsu23YiK4I6pA-3xCXq7QhxUBRe7eks_lCJn1HFNXKwKKelI-7p_0TTKOSOs52kC5YMznsQ4G70KiBLqf1GavVeAuJN-uMnFiv2DIUr2AAlfVeNZcF37og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346118b0f2.mp4?token=E9uFQfbbUy61KeHW10oHwqn72aDSHWzRBShVltres4j33-oZPwQrr4Ax886KWwOK5fFZWW7QuK-CGqNNcMO51AsVleH37Yewz8uh-C4iqmEOAzFcG_pQHF72NZQwk4pSrm6uzCt3YVDHrwXEKQV106l_aTEka5qeTRWMa6LLCBKVB8cu5m8Buw3K7AegG8WbVrJD76_--DPLC38zEzTJ2NHNnK8mCnRojsu23YiK4I6pA-3xCXq7QhxUBRe7eks_lCJn1HFNXKwKKelI-7p_0TTKOSOs52kC5YMznsQ4G70KiBLqf1GavVeAuJN-uMnFiv2DIUr2AAlfVeNZcF37og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
دمنوش‌های گیاهی که می‌توانند به شما در زمان سرماخوردگی کمک کنند
🤒
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/663574" target="_blank">📅 21:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663565">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAZEJxT6GSIEGs2KJBz_O648yrqJxyY6G93asF8ec-eIkTkdPh_lOeMkx09mx94-Pz9uYd2l-mKnTktGlhZZexC1MyzboUnDa7eXQ6FVax1GRHHlY-KGoXwDRYEej6ftZ8hnSO9JAhE_rsIk2POBvaekRklYu7OBXjkpOLVHPr3SfPzLgbU-tuPUjenVVbi3qEfu0OKUcFZSahkLL2MklmO_z_GOCPxragQl7-TrfbkkJO047ld4JM45EeK_xaCAn5sbg4S1gzQO3nwhTgqRF5tUf-F7vQ6kwbAL3URABmFTDIsUnF4xzDHdfcddCyeHqMjDhQ3FIdIA2TXLF9-Inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8nDJdAC8Qp-JHxu6Y9p4_m6FCJ6f6bRr_LLwQauZf3AvKQOEbl6puVg1sU5-dhZOg2X7fZui-AmKkyjL5uVo-G_bhBMc_cue5zcx6vyqcuZ3ZStThpBrkCih1WrJX-I31bfZP_nJvWHjRv1iOmyg3_G3my6R1fvxiZeZEimbkoUtoudSNX8XOTfYKpKuSuFKsGFn6mf7i8F2eA361b-94Zr1qiJNDLHjkttPGZUvHDPYU5RprW3rsy0CrSRbQ-b3rUhgmfZ-IitCOsJ9mOOyldhL7IXwG59Rv-cXOGEsT6vbdHyu9A70ToNs4z29SK6NWAOn5ArCMtlBnZqyrbiCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZ5DDkKZpJSq3FLmb3ahD058AeXseFKasIO75SV84qEcwKOGwNznbjb1HsBiEXwq2cJ_6WTnbDiKL5q0pPxh_JYnqQc9NnTiaYH_5QyrCw2xY3xNkmKasJtgXXoUxOp-4ykn3cj4uadmEUi2Bt9drJvN0mFWpr-YXczfgUy5QE0yFtDf79FToxHKaKxxUv3aCo65un2saAXiEQjejhCAdGtfjqlcHV6Z0q488EYSAAxwIkX53I_aZbSWubjUhhABB1fFIruMd0JAtBCCLXburBM1IfC1Sts5T_T0naWr3c6dZ2xCf6J3kKu-mmgjQrnmuGp19PymgCcZxcDHA-eBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIknGimJh0Fm4eDqj4NQmosZaRpD7qiyKSl5kc8IIwMheRl3PM-4OWqlkLTjWLaW3wQBWbAck3ULOL18J3utM9eAa8kJwY7XpIdVPFpAlG36KzzqFLcF5IaLHpbW3epxTmEJCv80lGS21myNSPstOhQO0nh9NGebcWavIitb9KNULARGWMCOIeab9eq2vyTe9orWkZOuceRAa_iLFAwSeYGJJ2CtscrLa1Eg2UiUf2s97WhU0k9-KPPjaafPPxUNfrm9wzSsazQ_X2m5mWi7gkLM9cUgxFAD7JDk2khVYu2gnkJq6HE6T_4SAL4qiCdEXnzqM5OMUqx9RoLqk2EiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpeRfvKBXAZtaI0rVqTen_mbn72FQ3bErwotM1vnhuNZaTV2rWMnrzV1XK0Kqz8EekCWbki4AUYOZmVNDgFYRq8Sg1NZDxvSZpOqXcp4tfNY9lEEKI2d2KT3bdHDCX-0C-pbVn59v0A7B_92oszmld_L4YnVj1TJOFQ4LI3pIGADdslJF-JYfCj6opJ_JahQbWSDZYrjfocRmNso2sqyUavG6KM5guE8cWalLyoVD-bOMi6_m9TC5T1xi5iwcQ9Pu2ea7uwT22pQy7Nd-ndtCRxBeaV-ndcxUpVqrzYcPcb74fy1oaj17J10u8Ee4gZLNA7CjA8C8XEfoR2cj8kslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVdO5efCN4-3yCb3Nh-958JGPdgvqSL3qo4Rboi-rdF7obFc9L8fzhbl4MNk916GRXM6LggSM9CDq80Dp3xve4rP7d4Hbq1hGYCzyHuGFALrWEDZsbMCfE-K74gAET-vqwgBZ9FvXFWVvrVKboX0oxISSoTHKju1CHTx0mfuKIgPbphljFik3CzTEw7DxsKb70405_inXPr1rJvccAP7XWEnsJ-y7rLmkLdJaknTGTYyvPnGN8DXjIHn0vFzxUFtp2PL5DBqrKwxQNm5xKpfQEiPB5KTMpzRNHgr5CuI59vJ1EFdy9_37l2XbV8s53aKIPWLvJVUvIFQtLjUw07q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVdLYROmehi50DilKkQ8sMxJvxLlUAoCBq2P4MZV6CEE1vxxBBtGRWWdnvnXQBfSXFwVRsFZdRdD6Xg1ZCNk-lFuJ1DMdKRPamMmZpBwbyQKau6OKYtaJo8NAxjDs1uka7_DJxCqc2RcK2YKevpyepLI8kp7dLcj6EdLb_4eGQ0qnXju_m1FcEK85BpCZ-sJfNFilpIQj-X89Lmje6GJmUjzcoJhsvbkQYiKXtlwQO7dj6O0M5iY94meWhgd_upfdC3Cf5d3dpiZIB0JEeTfC7OV6-GCOuaMDE-FMHv1y_XFAK2EC8h95MWTqqQ900tHl2ubzD6u9VL1gHNEueRd8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h0u_d0ZPGissBD8Te_fvIs6vNMReEGalGmi-jUH8edDaRFl1dMomTZlnzP3HA5x0dUJm-Wv3QggproNLBuBczDPh37rO_IIQNbZhjmB5JFW2IEQbziqohrf7UTuiDA29FKGWes0jEhAN_5h_09YMCk9U10DsymKxnh-nF6e9DD7WelG9FcbkqTLHEypuB5LKqlOBvHDQtVdE_xko13B1tnsTRiA_ApM4Fbz_Ogkbqt79O6YgqX2PJwYdn7N61PtxtLDWwrhVT0F3k620IxGPIeiI2cc3Dr8tg-7733PRZ55RM9pwDrohJoPGi4aZKv5N8fIjilkDIqEi56vh0VzP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S26tbGuT19k4eb_qSKAjaAD1q9vFdBjW-WR6CRY4SWW-R8haMi84CzpT_BweDOqyMlPVGXGBJe69RtJl-3Gttu3V5j7EBildU4knVaKnfNzXdVTbbWmDvXGDnggJKskBD9M0FH5cdm4BW3N2wLWcueTPAjpaCR5VZKhW5lUYm27PUHI6hCY9aNCAiVnt7P1er6sk3JwCaf2tF2Hm68V-17EtFUHd39RIQ_fHts1Z2uj1MywLBAjmECsdljnwvhjSZ39NaAI705pcAlpLvpAraLxSULpdRA_pmZLCtx4xTdPXbFcJSuq1_P42AlY99lsX8eViOnmySEv9nigQ_KxE5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خادم حسینی
🔹
همراهان عزیز خبرفوری؛ اینجا جلوه‌ای از عشق به سیدالشهداست؛ تصاویری از موکب‌ها و ایستگاه‌های صلواتی که به همت شما برپا شده‌اند.
🔸
عکس های خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/663565" target="_blank">📅 21:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663564">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eghv4lq5MNjT-n5ReSLEk7sXkKYaX_X9aBgkrcs_zAXVrgDhuuOO-4gY01GfVPYWh4p9gFvYVbFVTAp9R183Wr33k4TtpfiooUZdYM0MaefMS9QkJZ1Y9KSX6gzwvxzctO3P1OKzpXUFuPy07_P_dBYngpRkSbou8OYQmXjTkn_SFcs9X_gC5TD7zg5yN6CPhsOeZWK3xn203GuY10jLou0ksigRUsc1NRCIocgqI05rsaIa7ElhEIP1Gtryj98nOPbUG6oWKN9miviOWD5oKgedMCz84W_ZNlzY_t-RCv2LghL-3lttf9imBgqg4mkmDM7DekbL9Vk8QuFhynwU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ادعای روبیو وزیر خارجهٔ آمریکا: لبنان و اسرائیل به توافق چارچوبی دست یافتند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/663564" target="_blank">📅 21:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663563">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa59379808.mp4?token=VbDPu8opevw38C-E2jM7GxwlaCKC4Y-hBF9sICeurhWyXSd1Ki2h1O6yVzvn6-8fSIQutVe8B_sJ7Ef43KXmTA1PO44UybdnyCBlLwTTMCgaKaxNZnBRFUIsDjDjbSTg_riDZHc2wqP1e_tYzwi4IuxLBs2s1dGpnl8Yc18oUtFB-yFk49g-NtfZ_VTar37_jskRcZqhQR2291c8yzPXL9gQTGenPLb_u9hJJIH2aVljspWW8S0Xudtyg1LcexaY3eGHGPUc_Qg2rKM-VXkHRDnfcTpmul6AzwMX3yTUmKtKfEFd5bXtqlnoj24KumwjOnpTbvuySG9VCwJkPP0GHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa59379808.mp4?token=VbDPu8opevw38C-E2jM7GxwlaCKC4Y-hBF9sICeurhWyXSd1Ki2h1O6yVzvn6-8fSIQutVe8B_sJ7Ef43KXmTA1PO44UybdnyCBlLwTTMCgaKaxNZnBRFUIsDjDjbSTg_riDZHc2wqP1e_tYzwi4IuxLBs2s1dGpnl8Yc18oUtFB-yFk49g-NtfZ_VTar37_jskRcZqhQR2291c8yzPXL9gQTGenPLb_u9hJJIH2aVljspWW8S0Xudtyg1LcexaY3eGHGPUc_Qg2rKM-VXkHRDnfcTpmul6AzwMX3yTUmKtKfEFd5bXtqlnoj24KumwjOnpTbvuySG9VCwJkPP0GHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بازتاب نماز خواندن بازیکنان غنا در حاشیه جام‌جهانی؛ ایمانی که فراموش نمی‌شود
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/663563" target="_blank">📅 21:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663562">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔹
پایان ست چهارم | والیبال ایران ژاپن  ایران ۲ ژاپن ۲
🇯🇵
۲۵ | ۲۵ | ۲۰ | ۲۳
🇮🇷
۱۹ | ۱۹ | ۲۵ | ۲۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/663562" target="_blank">📅 21:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663561">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔹
الجزیره: لبنان و اسرائیل به چارچوب کلی توافق رسیدند  الجزیره:
🔹
لبنان و اسرائیل پس از پنج دور مذاکره بر سر یک چارچوب کلی به توافق رسیده‌اند و قرار است این سند به‌زودی امضا شود.
🔹
به گفته یک منبع لبنانی، طرفین همچنین درباره آغاز عقب‌نشینی مرحله‌ای نیروهای اسرائیلی…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/663561" target="_blank">📅 21:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663560">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔹
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/663560" target="_blank">📅 21:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663559">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069b6e36fc.mp4?token=VYDFV9Rsvk5qRd_Njwg7uitq-KU9fEmLWlHBJfcsJaIJmmIUIyqDFl0rFKz_pKc7E-Bib8ur538WKpad_2qXPapYtCxvgycRZ_5Bmg4omn_zRfskTKdGQyAnZ4Yuxf2j-hIA1gq9dMw1v3o77OgVTv9iHqmcVXfjPk7SwYdrrLnnLC79fq-C9e1p_srijik9q1sQ3egj9F2JCUSsUaDkoDsaW3htqO_rf8rdrMQPzv93c0MQnYyly7x6mpFyMTU1RRD3bP6Y4cvLImqFULC1sxGOVDUajkDB2D54wnqBZshy-g9orvMiW5g8frw925K5qNPzcJBHksTE3rDI7alvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069b6e36fc.mp4?token=VYDFV9Rsvk5qRd_Njwg7uitq-KU9fEmLWlHBJfcsJaIJmmIUIyqDFl0rFKz_pKc7E-Bib8ur538WKpad_2qXPapYtCxvgycRZ_5Bmg4omn_zRfskTKdGQyAnZ4Yuxf2j-hIA1gq9dMw1v3o77OgVTv9iHqmcVXfjPk7SwYdrrLnnLC79fq-C9e1p_srijik9q1sQ3egj9F2JCUSsUaDkoDsaW3htqO_rf8rdrMQPzv93c0MQnYyly7x6mpFyMTU1RRD3bP6Y4cvLImqFULC1sxGOVDUajkDB2D54wnqBZshy-g9orvMiW5g8frw925K5qNPzcJBHksTE3rDI7alvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گل اول پرسپولیس به چادرملو
🔹
محمدامین کاظمیان ۲۵'
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/663559" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663558">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47b979a35.mp4?token=JFanLHB-jnUHwPn0gqKae0AuuW4ZtkM3BvOuNx7DhpnphDLHdDeTNuu0dd2TQGeRHOTstTd0WBBbPygZQXjQHepJRbJMSRFqOpLlS05ws95irkwaMVo3m1GTGXak0A6g9CtmzXG5MVBPLZD2baRAUf_BYKkZuXx3nPabiDEaF308RksZqvr4Sww3tInNi4MZQPBtLr78KE3Q6H5z04uXB0u7d-CX5YhXt3wY_Gp1vhHAcQeJXGtWi8ASyFiERM6mPWv7fRcuOAvr6HRzEK885P3V8TbLcck-5OG7NNAIwTrqF62UkL8t4XmT68xCdzoWM6Il9ia85HcoVwOzyNdZWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47b979a35.mp4?token=JFanLHB-jnUHwPn0gqKae0AuuW4ZtkM3BvOuNx7DhpnphDLHdDeTNuu0dd2TQGeRHOTstTd0WBBbPygZQXjQHepJRbJMSRFqOpLlS05ws95irkwaMVo3m1GTGXak0A6g9CtmzXG5MVBPLZD2baRAUf_BYKkZuXx3nPabiDEaF308RksZqvr4Sww3tInNi4MZQPBtLr78KE3Q6H5z04uXB0u7d-CX5YhXt3wY_Gp1vhHAcQeJXGtWi8ASyFiERM6mPWv7fRcuOAvr6HRzEK885P3V8TbLcck-5OG7NNAIwTrqF62UkL8t4XmT68xCdzoWM6Il9ia85HcoVwOzyNdZWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حالت هواپیما قبل از خواب؛ احتیاطی ساده برای کاهش امواج
🔹
حالت هواپیما ارتباطات بی‌سیم گوشی را غیرفعال می‌کند و میزان ارسال و دریافت سیگنال‌های رادیویی را کاهش می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663558" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663557">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFHgJydKNm8wLilQ5HdnGRnak4-abKxqzNmeJjsllV2L7TmMk0b2KU38W09DXXuDxXo4khBgfGsZMWgVhGRgo2bn_gd6FKqrFvK7po38gtpvgtbRoX-FDlKx1URUSlxg4EpV_-2ASw6wE0KFshdWPsvfw1wybYqLSRjSzKKt_iv-1RTIltMD5qpa5otv_WSkcMtQK6vnPMOTF6e4KSv3rq3XV75Bm3xYJqMZscZgnW7sDCwhprdyUSxyhwEmesmGNciWgF8NpVnZ7OpiOVfmyZzEigVyTotFS-HaYAxvmPy-fd0Y1G4F_jj9Ys7WdJp_z9dcYMa9EW8ZO-qvRI5caw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن فتحی عضو کمیسیون اجتماعی مجلس در واکنش به بیانیه تجمع مقابل مجلس: درکتان میکنم اما تهدید به تجمع مقابل مجلس به ضرر نظام و دشمن شادکن است
🔹
تهدید حدود ۵۰ نماینده به تجمع مقابل مجلس در مخالفت با تصمیم نهادهای ذی‌ربط پیرامون برگزار نشدن صحن علنی، به ضرر نظام و دشمن شادکن است و مصداق اقدام علیه امنیت ملی خواهد بود.
این روش برای نمایندگان انقلابی مناسب نیست و مشابه این رفتارها را تنها از برخی نمایندگان مجلس ششم دیدیم.
🔹
از جزییات پیگیری‌ها و نامه‌نگاری‌های دکتر قالیباف رییس مجلس برای هماهنگی مقدمات برگزاری جلسات حضوری آگاهم. راه‌حل مشکلات کشور، عقلانیت و اعتماد به یکدیگر است./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/663557" target="_blank">📅 21:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663556">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7AhoBM8IoMLVQXgIBHxU25BHTz8ptqHQfBuTfTtM30CU9jCCKPPwvPVYTNejetcTR-szCgT4H08SP9rqs4gMpO-fmsZCnK2GdyAxyz-1AjyDUQ_I-OZl_ss3vynHbAWOsBnWKCHs0NL4qGi1yXJv4PfDvj5QfVf0op7-1VT-VB6n1SQVUVIxWRWi44bvxPZ3JkwfPjugzdZ-0yvzInONyx8mmZh8_DxlXgvDKeP97z3v3PJpyWyYkxKY_NwPxGLAd7BRUmbGNx8O3oLZDCPtAXc0EDaNQkgqFLTLNbcpSj_vQiCxPL2PZC_NEX3THOdaDrSQHXpTq8_a9_gI5L8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مفقود شدن بیش از ۲۱ هزار نفر در زلزله‌های ونزوئلا
🔹
در پی وقوع زمین‌لرزه‌های ویرانگر در ونزوئلا، گزارش‌های اولیه از ناپدید شدن بیش از ۲۱ هزار نفر حکایت دارد. عملیات جست‌وجو برای یافتن مفقودشدگان این حادثه همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/663556" target="_blank">📅 20:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663555">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌
🔹
پایان ست سوم | والیبال ایران و ژاپن  ژاپن ۲ -  ایران ۱
🇯🇵
۲۵ | ۲۵ | ۲۰ |
🇮🇷
۱۹ | ۱۹ | ۲۵ |
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/663555" target="_blank">📅 20:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663554">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dskneu5r6KDg8dieFVx2PWniMkLvwbl3RRTKo-NafDqFixp8Lnuy8hxkg02r-qKv-DJZi2Y28VG1TbYYRiBMflQyUeekXt_OhkRe1D8kOOQbXwYdiDZzriFAYes8XY5wc6SjNKSSEjdVqbVO7_lDYDKAJg1nblbVg7E9F8PjTQv2aSs7y4KDK6mZD6s7W-Bgiy0RrNSnpi7HL0whxmvuQIxmJ6YfxsxDp1_jHFfassFcsJkqgSnGvV3nmKGPRzineu55xf1xBM6e_8FgqGDdh43mwMZLSL0WSc_XoRsScgNWEKs-phn1N-HQotukteQ02hAlSOKTtfITCwWBV7o0Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عکس کمتر دیده شده از داریوش مهرجویی، خسرو شکیبایی و جکی چان در حاشیه نمایش فیلم «هامون» در فستیوال فیلم توکیو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/663554" target="_blank">📅 20:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663553">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
خبرنگار آکسیوس از امضای توافق بین اسرائیل و دولت لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/663553" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663552">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a899637c4.mp4?token=guYr6ws5KRzwU3BeNDH-lWAkKQVmdgD9KMU6qiTAHOaCv-JtAUBVWT-47YQ5CCfDRSeAkiqTd4fxVjk17PhPDJE-EOX5Of15lymvu9X9fg86OEIgoaYISycFAiJIX6UjMspZXMcc470sZlMcSH-I5YM7qmCN6qK6fU5uZgAZh_S6KVNJQil3fIGVmNIOWl0SVCV8Lvp1S-CYJCBkIeRO9nh_lhMG_knm-Spkn2CzAP1rLYOLtaUPya9IoGF5hyBejGBOya1jgY_CWzIJ_z3nPavoO9GV3rF1-YXZX8ph-IcnYY_pm00D_eQCITYV6ERliQ7Fz521inC6DYcan_BZnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a899637c4.mp4?token=guYr6ws5KRzwU3BeNDH-lWAkKQVmdgD9KMU6qiTAHOaCv-JtAUBVWT-47YQ5CCfDRSeAkiqTd4fxVjk17PhPDJE-EOX5Of15lymvu9X9fg86OEIgoaYISycFAiJIX6UjMspZXMcc470sZlMcSH-I5YM7qmCN6qK6fU5uZgAZh_S6KVNJQil3fIGVmNIOWl0SVCV8Lvp1S-CYJCBkIeRO9nh_lhMG_knm-Spkn2CzAP1rLYOLtaUPya9IoGF5hyBejGBOya1jgY_CWzIJ_z3nPavoO9GV3rF1-YXZX8ph-IcnYY_pm00D_eQCITYV6ERliQ7Fz521inC6DYcan_BZnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحنه‌ای جالب از تقابل کفش کوهنورد و دمپایی فروشنده دوره‌گرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663552" target="_blank">📅 20:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663551">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfa562drFtfNpneBCZKLNdBPz24ys1-2vF7TCKuEt-abITZxUlPfRLKYT0-3RQz2hI_OOqlqFZNwif65qC3oHonRF0-RZtmwu_vle5Y3AiNxBoe3XEFrAF26pYwZR5eZTxZspJ4dCMhnLQV0W1KDG-oTWzPklPK1NfbWJXgf-WxHB36m0hwiT8o0NN_IJ_vPdEe7R8GJiJuGAX2mR6TsWL6vGRCxhI9F1iQWOfXEaNu77yyOTKE0WKMvSpj8D_3zTUJVaKRsmKm9FYYhHEDKRYQKop7uUfO4pnCJqMxgvXCb8ji8xzEAUOo_B5_9tVZ_EqeCBl7vp9WV30HERLJnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
خبرنگار آکسیوس از امضای توافق بین اسرائیل و دولت لبنان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663551" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663550">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
پایان ست دوم | والیبال ایران و ژاپن  ایران صفر _ ژاپن ۲
🇮🇷
۱۹ | ۱۹
🇯🇵
۲۵ |۲۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/663550" target="_blank">📅 20:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663549">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a710aedc.mp4?token=TxNfs8K6KeEpT9wozxx-AStbWOK9sfbxFk4lAyybSPcqDQtRyOkhlI21lqd09tFKAu3RJLktJpx4lGhcOH-fzJnJsf2q1rTJ-aGhNG_-FJDyXafsFA7GzIhJNIjZMiChmZdFbezVfA3Y7BvSNaOhFkm_r1nnKPmNbnAd5B_lhy5XtCrUS4JSurS2noRHCEfChFhFhv0Ah2EvndBa5zj2tj4k6ZOfNrrhIdlLnBrjSHyDoGXACUm1y3M0kb1aEfk20Yy9Y44yrETEdBsSNoXASY0RGoRIEy-3LCds2m3Isn1c5JXnKf2zrgs_Ffad-eB1ris_G9RXfoUyyCiSSmZ3ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a710aedc.mp4?token=TxNfs8K6KeEpT9wozxx-AStbWOK9sfbxFk4lAyybSPcqDQtRyOkhlI21lqd09tFKAu3RJLktJpx4lGhcOH-fzJnJsf2q1rTJ-aGhNG_-FJDyXafsFA7GzIhJNIjZMiChmZdFbezVfA3Y7BvSNaOhFkm_r1nnKPmNbnAd5B_lhy5XtCrUS4JSurS2noRHCEfChFhFhv0Ah2EvndBa5zj2tj4k6ZOfNrrhIdlLnBrjSHyDoGXACUm1y3M0kb1aEfk20Yy9Y44yrETEdBsSNoXASY0RGoRIEy-3LCds2m3Isn1c5JXnKf2zrgs_Ffad-eB1ris_G9RXfoUyyCiSSmZ3ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گروسی: اجرای توافق مستلزم دسترسی و بازرسی آژانس در ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/663549" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663547">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4Se911q861nkHEKYvgnJ1VJr4_ISTSr-S57NiPBqqc9lXFKimqtVw1dOevMghNMFjSRa0jZx7KCnovSsGNb7o-VZ5cwwVTaYRP4jQy5u1oy37t2CeaGKDcNQu9PdeYLNdgDzbfYwgXfv753ODpDNUt9dzOKTgBdDFDzFIHuMbDNawEElpKEeyWa6qGrThFLr7Ygqy2i7gV0H3Q9MDHEVM7QhLcdMcC3qhBuCwOfnPbU_9wFpzKIKUBDzkrP18yXJEapxSrMFEQqfWxRekBAheD92MKeD72lhctskRJinEdCpveCzc7YcURV5w_MMfU_eMW5gOudkDxRRTmlTfo7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j75u2vpfRlnK8o2zH7ajBVPLbYEdKkIy-uKwHs6yRHVHqnNpQX4lNkBSLYdYj4frbh2ZsazvoJZSp2q8DgwD5elxm2dmRwT05zgeQDIMxUQCh_1J556onZcot5Ga-ByR_UxsWUrwpK96WRxTTFy2CNyktHlieh5Qvxym66-0oU7DaaZEiRm3w2MC8bTkfTx47lpAJQykeAogc4NILWYq9Jl2lzYiSMNYy0wBFLXOQNJWCnwsCz2aE6MRgF8NXmqoxZtgqk4XeLsKKythO_SyrR-MOFSYpSLKeHsGmXubQECYNPZNl4Ex1Ji484RU_TlnsGDpEToaj1igXNZi_8d9Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصویری پربازدید از ساخت یک هتل در جوار ارگ کریم‌خان
🔹
ساخت و سازی که اعتراض حامیان میراث فرهنگی شیراز را به همراه داشته!
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/663547" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663546">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234209cb14.mp4?token=kDiVdTl4KCW7deaCcJciONwCFHmhpQHADYIh5BR2Wkxgyban63YJ1mvtDX8lEE78B1gbx9Si7IT1EQbsbTWLN-eUgDCMvSJIaH3WeW8uA5qUUy7xv73ZxqGGBybfarWk9mYLZtWzByFhjPP_teUnzdxkmaijaVz_YwbjkVMiwwvZVhTyPjZpc5t155xVw4KM0Qmlq1ISjsaY3rKpa-EyL97safJR0GsMVPt8g--S-q36NsQMFJNBjp0UZACBF15_aBeS3gE7xG04a4pmxsINV4YiCDABLufzvawl9oTJfYdKZrATGn74B_H9883VrbrMrrDdOOTYaVU-BatDyyO9RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234209cb14.mp4?token=kDiVdTl4KCW7deaCcJciONwCFHmhpQHADYIh5BR2Wkxgyban63YJ1mvtDX8lEE78B1gbx9Si7IT1EQbsbTWLN-eUgDCMvSJIaH3WeW8uA5qUUy7xv73ZxqGGBybfarWk9mYLZtWzByFhjPP_teUnzdxkmaijaVz_YwbjkVMiwwvZVhTyPjZpc5t155xVw4KM0Qmlq1ISjsaY3rKpa-EyL97safJR0GsMVPt8g--S-q36NsQMFJNBjp0UZACBF15_aBeS3gE7xG04a4pmxsINV4YiCDABLufzvawl9oTJfYdKZrATGn74B_H9883VrbrMrrDdOOTYaVU-BatDyyO9RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قربان‌زاده، عضو اقتصادی هیئت مذاکراتی: چرا پذیرفتیم که به مدت ۶۰ روز هزینه‌ای برای عبور کشتی‌ها از تنگه هرمز دریافت نکنیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/663546" target="_blank">📅 20:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rr4FQFbToAuz1WImzR8l7i5EPPERfY_TZICDV9VyQIY1aVplBMTYHuHTdyfkz9Y0hg97Iqxzx0ABae_L8nmTZGHFLkdkYbUAj6e5jy0_oxUy_K9MqMcG1Adp2qKJ-hg2BAL00r6dSGwPnvvlfe1LGik517Jb9NTIfNwBPtkd02hSSXWZT642YEd6xuIbbQFrXBCqJNONoQRRjswh_ObBuas7UsuB3yNXLcHLUPryKlCYyhAPcBO0TE8NUW_ADfqB8vX3BL1Voj7UY4XCv4t3iIe9TCozuiEp-_J5MOuU8O1rwH_cBUQIaNCwpwbEGnvzzPjvLsYwAX5mVoaHLWrjeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سردار محبی، سخنگوی سپاه: تنگه هرمز سرزمین ایران است و هیچ ارتباطی با آمریکا ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/663545" target="_blank">📅 20:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaQFjCPi_CjBa0cSfnB3lcTZIJILPZnFypA1dpwjjXDrI4cD7bVLuqyauOURdVz2JTfrt7maGaZ0BpRQZTu6YHN73VhRMInnYZd4f6DEkbx1UFQSo8a9eywAcGewMaZd4C1iVm1OsXK1MaQ2v1NMdzTpTkwjgaiB0a0dKj2Z4eu-D2Sgivx-LkflAZD7v2a5Y2lCeeFSAOgCZBb-tORbI2z3V1ZfE_-kDNBPBzw-Cc6h9NsobJOS0KBjmWTBLDSKXtkYyHkq7Dirxwbeeb6B7gPPldGtT-Nz4wPmAGFsYJGVEyVx9k_67C-cPz5n0eWesmM_ahtxLcsZIUFPod8PmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هشدار رئیس کمیسیون امنیت ملی به سران شورای همکاری خلیج‌فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/663544" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIaeSTJYF28YDNg3sdDgbQq9Cb-gx1m9C8FciCu0TKnVqbmALZkzn10fWwK2R_n2SrXn3P0TjevZcDK-20tEf8wXlOiWkiVB-cWUa_OgwdZ9nFngq0YFrlbR41tB4knrdJH5LO7h96DU5tCZK3KCxH6C-qbHd0yVYV7PBqDP2s82zQt1ewLPa1zIrPWGM0AbPbSX0JyJN-NJ1lAwqQnPq3AN4BsB0qBWleugGSJdbmJFBRU1og8PPq1nv_bUUnYsVwyJocmXFD9SZM4vAYEZWukFkTHT2ItOmsxuF5QimPbiIP_sYcPalaDztTsH-qiftbw53q9lbXBX5QnyqMSVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
روابط عمومی نیروی هوافضای سپاه پاسداران انقلاب اسلامی پیام منتسب به سردار سیدمجید موسوی را تکذیب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/663542" target="_blank">📅 19:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btSWxmgV4_uLmL2v6p8fJ9Xz1RbtIUw52mRjIf4ahdVw1AJfH1-_anDjD3JYFwlbMBl4sNozLXxvEfUFfXkWiZbd39Ce2JbIn1sjxwGR4EkDmE2bXMOCDOr4VOKsI23qwa7WBlIPOIi1OeaaIVUEzcqF774kJn3v3fP71AFDaapuGZrnG2oow8FptrJKKQcgGUSnXmrMrr_HyRqhJso_ScQGUL0ByT5_D-lj10D11E-Xhn4MkU8_VGX6Dw7oB7bPKOokuLPBFpg3FuTXMIWZbysFd2eevIuuQqQh0rDGqzl0WA0Fz3C3BFsCca_JxLMf5SwZBOyQos20_Onuu_hDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPHHyeIyosHHgLbofJdGdadn8Zn2UQFnPTJ7BgaCsudI-5oJX5N0l8oOCIpMyEYITfm-v1vSVOZS5HoAEMW3I0s2qK9JVh0kU0tpW7xYavg964tqIu4x3ESDotSxW7MkZ0RkSzGWWXqCfXh0ZBvXzlQkYymAJb4oM1e6ff10sY57come3u_6MepuI-u4LyPciwfbF8n-9gVYO1QYANDEO4tgIvRLiuA78AN1lpMu4Z5uffExsXjf-kpkdw2BlWMDW-dOaP0ubEdGSLE0fDtci3_-rDi1ftas7qIhq6yxORnKSMrUpcPW1KJU7Nsb4PGzm5fofpQCDtc7G2cD5xGiCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
رقیب کره‌ای آیس آمریکانو؛ آیس بلک سزامی لاته چیه؟
🧋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/663540" target="_blank">📅 19:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663539">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔹
پایان ست اول | والیبال ایران و ژاپن  ایران صفر _ ژاپن ۱
🇮🇷
۱۹
🇯🇵
۲۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/663539" target="_blank">📅 19:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663538">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa5c97e84.mp4?token=sTPu2vfxPtsbE3iPRemJl3MJU8RBBZxADmsk1UyRfuX3wg4Yks7deWrd2iO868MHdZG_4FvEJwWmuMjegEBuzm6xYs_HxU2deYCzwgQY_gAcBAFnn5qEmy868s-lFFzZI-6Iy39X4U08nF3OgiEkZOIyuUl7ny8_ODSUpxSILcHjBY2v0q4hQ6qth4Wk3JAvTmB6KqWbJ_iWxLxtWQyUHBHCijYTl2tfgO3fItWQb86tJmuzoMJgJSZSHBBhscpAUFhkQFte2e7NMu32TdWsc27Lbyq87P3Xcs9y1OxH47rwQ2jJhx5zcZU1-XMPDER2uouUHFT3qGP02dFuTbvq0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa5c97e84.mp4?token=sTPu2vfxPtsbE3iPRemJl3MJU8RBBZxADmsk1UyRfuX3wg4Yks7deWrd2iO868MHdZG_4FvEJwWmuMjegEBuzm6xYs_HxU2deYCzwgQY_gAcBAFnn5qEmy868s-lFFzZI-6Iy39X4U08nF3OgiEkZOIyuUl7ny8_ODSUpxSILcHjBY2v0q4hQ6qth4Wk3JAvTmB6KqWbJ_iWxLxtWQyUHBHCijYTl2tfgO3fItWQb86tJmuzoMJgJSZSHBBhscpAUFhkQFte2e7NMu32TdWsc27Lbyq87P3Xcs9y1OxH47rwQ2jJhx5zcZU1-XMPDER2uouUHFT3qGP02dFuTbvq0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای ایران
🔹
در آستانه دومین بازی تیم ملی فوتبال ایران، مخاطبان خبرفوری از گوشه گوشه ایران با لهجه های زیبای شهرهایشان  ویس هایی از جنس عشق و انرژی در حمایت از ملی پوشانمان ارسال کردند.
🔹
این ویدئو،  بخشی از صداهای پر مهر شما همراهان خبر فوری است.
🔸
الوفوری را دنبال کنید
👇
#برای_ایران
‌
@Alo_fori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/663538" target="_blank">📅 19:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663537">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReVbTcR6_X94QqKKwx2ZlKYnerc6SMOX9bx_rjhazZtriuY-VTl4k3pm9KvoLKV0VVT8mFvI1ETE5p0RXUbMAPQyCU_F6PqAkENunH3ftGME3W37LMf4jw5RaXqgndo_0rFK5FCZ8lcIvFOMURoYVebu5NkEAkIJvFIfxQVxTixOWutZg3sLbrE8_nJTqZN5cUBMzk_qIOJVr0i3AWUiMfcDUyYhmLaDO5HlsCdRZji2y875A8e8wofsilyDxPzFIiSE61AfFYG05TBoZKWgSyU17GTOdsMtEmefpHNloAJySl-XDRJ0PJRPkcAV3jD-_f6zXqdGFfNS5OTDbA9CYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ادعای ترامپ قمارباز درباره نقض آتش بس ازسوی ایران
دونالد ترامپ:
🔹
ایران دست‌کم چهار پهپاد انتحاری به سمت کشتی‌ها در تنگه هرمز شلیک کرده؛ یکی از این پهپادها به عرشه یک کشتی باری خسارت وارد کرده و سه پهپاد دیگر توسط نیروهای آمریکایی سرنگون شده‌اند.
🔹
این اقدام نقض احمقانه توافق آتش‌بس است./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/663537" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663535">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3NpUGTLb4SChG5DkuRvMwY6o2ibExg7z1EJx56XqrjC5I_aoNTk_DUv1NByBNbzZji_kxW0pdl1HzLlNU7eGe_5YwJ_jSuBAFf2AefpBkZUYTlZFRdvOEQdHn7XQ8rGvzH5jcEjtoLyn6MImAA_0Ol_SJilWlrFkuA0dBjiuFHigNouAQ81-iYlGgqptatqM0WyDEhkpCkpEW-sO6OKWuodEwiv1tQhC3z_tROhJsVCnWnE46N-p222uNZrgYEYvd6VIpMChKAG43rww8CMN_fJZ27BjSPLlHumUrCHgUcjSYD_ipx7HAZNfWyo-FTdYNB4abLfojkWbILeTBON1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpS54vi-ab1fX0x6XWeVU6qfC-yoap9Y_6dwSrmUhQ3QzUDhSyeqFvM11JWwUv6WyX32CkRIfjixAmaTz9Q_Hb0vdTA5Km3AVq0my4Ys4Ui4AR14NpTRBIgLHUiqb27Rd30nHRunTjoTfRZT72DWWZ_jsGlMV2PJ1IIsBFpBFOxfq0m0dcmlsCxibPGGeeDfLuZNJbIH_M_kfCpyajOKqFOqnQ7tnEyiSjNPV-Zbb6KJs9_t78NHNfItC4gDP7a2BKs9kY2IPbzWYsteO3iGoqMbf0ILIZRnS3Zbs4A1ZDtokPeOSzV5x3aE3Tc1lBrTjlDUHjraSa3HAFtyiCtPsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برج هواشناسی بوشهر؛ قبل و بعد جنگ
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/663535" target="_blank">📅 19:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663534">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suazLNmVj15siWIepcFFK4F633bFNx3gy9CtBL5hlD8jcCyR2sJQu3XZ8f8pMuLAeE7gMbhC1Fz2vpR6heGRipJ255YL2EamqLeVE_R_4sz9xemSkTyPPc2O-JEgQ-G2HscjJy4xfvkIRWfbF07VK7OTkl8spnANWe_GT-2MQfanEInzn7fm2xm7wiDB7EQEheKWrl-cx2eR_xJ1UDIVdiWpNU-7nja1NGyYVSg0iSKnQVJPmg2H593Uju219d-F0-hkaZfjonPHy1SCt7UPABf_bYZ2Ed2VrCrIfoXjqOSOGlJWBrusdHO_tkRXq5xzXoitmUHn9UTKiMMBkNCf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
والتر بلومبرگ، تحلیلگر آمریکایی: عمان به اروپایی‌ها گفته عبور از تنگه هرمز مستلزم پرداخت هزینه خدمات است
🔹
عمان به متحدان اروپایی گفته کشتی‌هایی که از تنگه هرمز عبور می‌کنند بایستی برای ارائه خدماتی مانند کمک دریانوردی و کنترل آلودگی هزینه پرداخت کنند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/663534" target="_blank">📅 19:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663533">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcrBZgYp8vBpfsGEhpJf7PSPQ4Eaw4Xauv4EcPie1MJgXOWllxyJayeLAeMRGjAHbBAg-jUc4U2-aVMkNlMt8Ki8Vur8-gUZEUgCcAFFPe7WxD5nOPKhJRDp3kMdsos6fHLvCm_y_D6fUBxmEOsQKtL4Ee7wbROcBLwMFuXQnLHNyAhMEwbQAY2CK5sVVARy1WxIdemT6cE0vBUPDBsTBcrZyWfGGsPKJq_uNdwzAJFolX7-IrifVD8UOFEm49H7jsetfA0-i-HN_D48hm4N4f41NuRk6TaKv2qHmfedqI4GFJYFfvp1ArUmEjTNvL05AZnFL7ydcYPt5RZ-CprYqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵
مشکل گوارشی که نباید نادیده بگیرید
🔹
مشکلات گوارشی همیشه با دل‌درد شروع نمی‌شوند؛ گاهی خستگی، مشکلات پوستی، نفخ یا حتی مه‌مغزی می‌توانند نشانه‌ای از اختلالات گوارشی باشند.
🔹
اگر این علائم را به‌صورت مداوم تجربه می‌کنید، بهتر است به‌جای نادیده گرفتن آن‌ها، علت اصلی را بررسی و با پزشک مشورت کنید.
@amarfact</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/663533" target="_blank">📅 19:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663532">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2e5da6e1.mp4?token=fPbXL1RIdgTCTNKdN0May2cE8hp1hjpUCQ7GGdDypZlFjiySHbwJqv_hiB1eLOZoelwYQH0_kmqyud-51MaH0OhKEi3FVWF3isCwmsRIIgc9SctwNBeCTo_cb2IL2xwuGcxtlAt0NnFQxPUwpowfBP10ZxW5cVsSFiY7xQSrUbyTHuAL_afUe2bzsVNiVGbxsMntjorXkg_a6Ha_d3Lk_6mNxu7CzSfOCb4A4lfb1vy8KJ18eIrZLDcYce9l4iEtYzD1NPzWIkkFNS4DudhS7xoGkPdLVxb11K8twmmKZ4IBe4ZFZX7io7I18j5n1AuHSU7I-sCE-_Bf2SiDuFDr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2e5da6e1.mp4?token=fPbXL1RIdgTCTNKdN0May2cE8hp1hjpUCQ7GGdDypZlFjiySHbwJqv_hiB1eLOZoelwYQH0_kmqyud-51MaH0OhKEi3FVWF3isCwmsRIIgc9SctwNBeCTo_cb2IL2xwuGcxtlAt0NnFQxPUwpowfBP10ZxW5cVsSFiY7xQSrUbyTHuAL_afUe2bzsVNiVGbxsMntjorXkg_a6Ha_d3Lk_6mNxu7CzSfOCb4A4lfb1vy8KJ18eIrZLDcYce9l4iEtYzD1NPzWIkkFNS4DudhS7xoGkPdLVxb11K8twmmKZ4IBe4ZFZX7io7I18j5n1AuHSU7I-sCE-_Bf2SiDuFDr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حسن رحیم‌پور ازغدی: تُف بر روزگاری که رهبر ما را شهید کردند و ما از صلح با آمریکا حرف بزنیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/663532" target="_blank">📅 19:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663531">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6DB3IpmmRMgBH6vQ21TftkN4AotzTSGDYZCYhheoUU47SZFklVmVH1LhFxJ7cAEm9Sw44yzLGrKBemoo7djx38jsE-eK-oCEpvAhWOMyoqa8R_85T8B61q3SiEFLDtS8RQm1xSq2px7JXFIRN1LxEO_WbNKnw61wEODQE5LlrjPspF3L3GFgEw2JPwRhT3e6GD1HRE4YeB32AhKDgH2z8htrv1w-1AKSW7svbxyOxmp9ToErx4N9m6Ao0nS4fSzIZtuJR3LrzQYn0yDu5xFN_SasK5KxCjiZ_nCNs8wu9hUobFu_r-lTf3-NqXBMk1yG6Pi4kjyLkSniMKCvp4sUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
همه خدمات بانک صادرات ایران در بسترهای حضوری و غیرحضوری برقرار شد/شعب شنبه و یکشنبه تا ساعت ۱۷ خدمت‌رسانی می‌کنند
🔹
با تلاش شبانه‌روزی متخصصان بانک صادرات ایران، اختلال موقت در سامانه‌های این بانک به‌طور کامل برطرف شد و تمامی خدمات بانکی در بسترهای حضوری و غیرحضوری از سر گرفته شد. همچنین شعب بانک صادرات ایران در روزهای شنبه و یکشنبه تا ساعت ۱۷ آماده ارائه خدمات به مشتریان خواهند بود.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، بلافاصله پس از بروز اختلال در برخی خدمات بانکی، اقدامات فنی با اولویت‌بندی دقیق و متناسب با نیازهای مشتریان آغاز شد و هم‌اکنون تمامی سامانه‌ها در وضعیت پایدار قرار دارند. مشتریان می‌توانند بدون محدودیت از تمامی خدمات بانکی این بانک استفاده کنند.
🔹
بانک صادرات ایران ضمن عذرخواهی صمیمانه از مردم شریف ایران بابت وقفه پیش‌آمده در خدمت‌رسانی، از همراهی، شکیبایی و اعتماد ارزشمند مشتریان قدردانی می‌کند.
🔹
این بانک در پایان ضمن تاکید بر لزوم  تقویت و توسعه زیرساخت‌های فنی، از عملیاتی شدن مجموعه‌ای از اقدامات پیشگیرانه با هدف جلوگیری از تکرار چنین مواردی خبر داد.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/663531" target="_blank">📅 19:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663530">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ca0158cd18.mp4?token=eTryZDqa8Fg6o7letFQZjvseG37Ktt1Q6Sb6D8wsUlczGJDvgXd8Kz_QpYrPhW242pG_ut5wWijUdhB9UJYxbfoU4z6DznIahtl33Qtg0rus4MuMaVLre9EJx7Gm9P6M-VlX51HWdWz_8ErB94EabUlcb8mTkSlnqfu9bh7o1YSZCIpH8JgxeFN9olEyB3WH2uCfBV5LyRdvTjQSFAq_mU94tvaj0OnbKQEssrcLtP_WcGv3896vQJXXBIfvdxCAnVGSsY0M3AS3Rm9rvMJ1-oGyELzy3X5kmvhsQoiVpTe7Fz0EXT1q4uTWEWodYfY-tolbnJo_OOyuuIW4CoaoEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ca0158cd18.mp4?token=eTryZDqa8Fg6o7letFQZjvseG37Ktt1Q6Sb6D8wsUlczGJDvgXd8Kz_QpYrPhW242pG_ut5wWijUdhB9UJYxbfoU4z6DznIahtl33Qtg0rus4MuMaVLre9EJx7Gm9P6M-VlX51HWdWz_8ErB94EabUlcb8mTkSlnqfu9bh7o1YSZCIpH8JgxeFN9olEyB3WH2uCfBV5LyRdvTjQSFAq_mU94tvaj0OnbKQEssrcLtP_WcGv3896vQJXXBIfvdxCAnVGSsY0M3AS3Rm9rvMJ1-oGyELzy3X5kmvhsQoiVpTe7Fz0EXT1q4uTWEWodYfY-tolbnJo_OOyuuIW4CoaoEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جدید حاج حسین یکتا که موجب واکنش‌های فراوان در فضای مجازی شد: علی‌الاصول یعنی ما نباید اجازه بدهیم دیگر جام زهری به خمینی داده بشه/ وقتی ترامپ فاسد اهل فحشا به مقامات ما توهین می‌کند باید محکم تو دهنش بزنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/663530" target="_blank">📅 19:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663529">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoqXV-B_iXTMUj-jVPnqycATyKcmcHO8vfoUkXQqGSnXF7XpGmm_L-UgXsMrOIcjEnVbWcXCOlFjvHdJLV535o9tVrYCYaUPR5yBYBUh69Mw0cVvgiIspztS0SH_wuFvwmU8ecC85Y-MwulGfOYFQWpLfSBYkdPvToNY8xZ-v-kc_Zt06f04riV2puDh5UPXnD60C5Q1-XUozda8JYG9C8UbEiAmDGSK-yD6u86yd7__NlJa1kbI8dOv_4PzZnxgCtIVgobA4St6KSXudBFowaF7VV6ulFPHx5iFGVvwhLbSeEHcLNOHMKSMf3vbZseP2dzy4IA8h1QdotW7nPvX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/663529" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663528">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔹
پایان ست اول | والیبال ایران و ژاپن
ایران صفر _ ژاپن ۱
🇮🇷
۱۹
🇯🇵
۲۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/663528" target="_blank">📅 19:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663527">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4VH8vgQkfnnCR8rsuViACvfueML9xqwmQ8zlQbGVaxjCBcwZDqUznuyICmAxQSPNW2plGy-JTv7F7bKRpxoVURvi03zCaqCFfUpIngL_8ndz3IVIwoI4AwV7xGPxsLrzoBSkm878uUtVuK3CCKZoDjx8g1KZ58Bb-EfJyNXK9c6z5cfTPr1iyFIz8eD46VZSXb7o44-p7xP7gFSyLEiFYDqWizu63ff6EXrCTLSUH4MovkEzTungGkDlPXi7AygLyPLCP4zmRPl0YPPCEK7PodXFZI2YTWjYsuuAB48TJTHXelofK5dQ1Eri-pziWmtMdtR2C2bfSvZCUmhvrJtlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کالکشن جدید ورساچه مورد توجه کاربران قرار گرفت
🔹
برخی کاربران فضای مجازی می‌گویند مدل‌های جدید کفش ورساچه بیشتر شبیه کفش‌های قدیمی  بابابزرگ‌هاست
😁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/663527" target="_blank">📅 18:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663526">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ادعای العربیه: دور بعدی مذاکرات آمریکا و ایران در تاریخ ۲۸ و ۲۹ ژوئن در سوئیس برگزار خواهد شد
🔹
دور بعدی مذاکرات آمریکا و ایران فنی و در سطح کارشناسان و با حضور میانجی‌گران خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/663526" target="_blank">📅 18:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLg45zsS-rl6cRIh7XeB-TcKxceWIQjVIo841o-84q6HyJdWU1CXT07pmCpyBjHxyZdEbXdycIlij0i79dTQ_VNxdE308GETgPglyJCrY6ggVcedb65vQEQMBpfPCYXBI1QpF6LyzonBp5JvRDQ0iMMc3WY6P5S7OIMAfDnqLiQBc92gw2bGM-fZVV580IcO1V1DFSqM2mxKzlbxRn8SU00RcUVvdq0vUa53kRNatbavvrp_HmYiAxF160NZBvEiChl5TUw4o7_d8sH36jgA9VrVewtY9sV783-waF4WitwSU1lz_UqD0iCS7EXo1GZHppyVssCfjVQSU385pAXq8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تعرفه‌های گمرکی مناطق ازاد اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/663524" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fN7HulHmX0vpWrDJRzKVfHRkQQdnISM5g0m4EzhyrUbynWYDT1d_ThLYezK27LGN2L7DzmgOG_oebkGC5B7kR1JQF5M0-MMWEq_Ns6-_RGhks4jjIalL5ZzSzS4zh7l9Ttp3v4gaCljFSeMO1ymoygvQMo-OgcZuWyvBePIlrFN7oPJVRfUh4dmfQ-IfOXrAdDocpn8XWfwcJWeaKpxqDIMVqlkLpJZuJt75NPsqOoxhhXzaBK0-5nwhaE4C0zFjrjaz7KTbv3skBsa20WNvCPa6jQiHAv9zS7wOvonlYD8hjE8k30--ZH_RyDp8W3CHh1OTr5k9HHSkX9sZ1BwyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LkYSwEY49r8XgFf1YmMdqWnNUdh5ZZ4CDcrXJn7VkFtVDKMau4RXWet-1F8G-QpQcRP_XyNQ4o9W-M3EjdbuPvI95y_HWhQfN-wDnmt6kMVkKEJnXcCigquw_GMB1xHSGYYV68XFiJxaeYNZt_wz28SAb0N7RKFiHs_RpW2wju9xRS3ez9pRILroY2F13U6Lx-6GIP8C7Pmskx0WeGDldLM443OWGd9PjzdRT4z5WkUWOSw7mGurIeXqIbFDYLmijVqqFfC3nDIqJ2EtTlQ9tq-fiZU5mrpDZuZguH5YTe2Y-nOvsKLSlUoWSwELlgJxJmIUnIXW_7hiTSE3thDADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwc3FVKCPemAlv4da7S-TSu_Qy3SI3rV0b97dyMHDWE2X6khsZfAaQGBt2gabh86IbnaukvZUVIj_7cykgB0yk6Vwpxjyd_CZsSRD45wEv6PIybOeneWD8ATMmox0D600fTXF0_4TEASRtTui9uXuWIgW3Uu9Zh6rwWEjqjlyDP0EWEHG17rdThq5sVsrfGqbxovnFjL59RwZ-OVmObrdtnOiAYVzBZnpWebQNnH-qp7L62AGt51VU8VVQyNmiP1r_wePU4jLKIZxdkhE8qhzpWsjtTBeTOxwOTJAWCqx-sqqYo-nvBlnvdyOEapy5NeZDev4bDuKwXCG33Xc5AXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vnRGOJNCvd2pPG5e6dlSMP23aXBHjuk54GJb5I4vEnHYBhXpSzMsrG-cKyqOryN5TUlqyM18L3ZcOpxoD9T2eSi4B5GM3MPO5aBksaG3BjCj5vBrQMXpQoC-wQYcj8smFtFwc9kuvFgDxbK-6bUtuKpC5VmIVQV3qTyb-u03SNj67YKRl_HbyFjvrbss9ThoLc0Or6xcBhR_LHUjIuVW-FSwmxMo9934uUZYS9aTJECUmMsSQnNAeiGPFyPCjX3sgayIc4GRCTegj_jDJD3YUgQfQ_ilk4s-D-jPFz8G_e1zEO12NhK4AUKYmCTb0o34fWD8nmyHrqCcUmRzndpCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRo7cSRx6g4pFqFdjEezDudl06-tZbwCgjlIlXaicdou4ATZBrnOV246bV4Xxn4Hr3FTyDKwFJZe55Zwu8WPPMc4UI0IouLYepqMgXU6qoisoYoPj01-Z9KnMvrwsaLdzDypzSqUAaLO2IHZyWnzSGqoEimZ_5EQjRZK_g_s6FK2WHsqD45Gva8x2IDzO5tSSQJSV0ooBEYAqGRkh7GlZmDB4QbwMlclaKKXKM_4NtuWxj_2wYXQbA6dn_beuTBt9bZVZzq9jf2O0DM_9bAnqn55K6qaEPLYwVLRWIuOUvQjsrkpkhXnBuVXUD3lbl1rgwXxrVWfOzgNi5cw9hq2kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
تصاویر هوایی از مراسم عزدارای ركضة طويريج در کربلای معلی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/663519" target="_blank">📅 18:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663516">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjGaH8D3TXZaRTZo-Af1TNHXYg0BnwqRtXjli4cum9O8ybXANPuA-cqa17hmZ5tTWhPWmwmiSY3_Jsch7sht7NxOd7oo91AJawE0x1aiJTiBCt7sGzMDfVA1VDUJHscy-0u4gpGSnmb3068WVTqj3u1hupC1wT0utn5PFT-RXLOB7YqP8-AFPo0LhSHGkfKklP3E4v0LV4orvgw4YAeAwgmNnRTNLmwLLjaCmJ8NLsQFpx5ozWS2TWZ8BXrv28iAqpPwHLR9ZyADpTEPwNmCvXJ5vG7kl-5W3fY4r5pkUoGdYu3aIS6y3AiqpSDLrkYVrD5Qk1mOjAaveuigSDahIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCQC72QPRoXebjuOY7Cw1uHXeurj639RG-K4l5FWBbP3Wt4lC2n2Bb5Rw_5YLgNkRDpyOFL-s500_BDHjjxnDD3v1yfUISNLfhf1KY94O40D7fZE8E-4Te1tE_QolHgVap7C3_DJl8Cd6WgidHxenRZVu1ri9O1ehPbotTuyxQNI92pPvPInXcV9OqQLZKaKx1AqQNNpISA-Pmot8X3JyBAcb9DUh095JC3cTaY-UwmZusxiuRNdrvAkSLOQKyslulxmD7v-D0l2rN4sK0rnbCeGYZMRn29S8ovsFgcMs5c3M63wTawTe36NW9zRcteqzg6kEC2e11X64rxOB_DFRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8XHQZFG7U6iV96aQmuCP_moGehjQUhkLcqjzuZ2sL15OUsN04Qsx00xmBCAx4hKeO4hLb9NIGycZukeevOZjJto2seQJhsezXXO8dKJPzMwP5QKhh1h2DJGJbiefNX6EGTuNgT0eGpnScfiwsVqe6lXCXOaCOR86rF6c24YbVj1T6u3XkztvLTaHGOd1IRcaILtewxtciTaaSGOWR-A5FEw5ur1xF6UWHTw6XbL6oPuEgF7h2raLdujEKYw3z1A5P-lM1PLWD5fmpMyPNJRyFQ7X5W5JK25F17OhPBcxIf8hmLVfQzdS9hgUGNdYCY8HGfiBllpjbjFN91HVIl9Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور رئیس‌جمهور در مراسم درخت‌کاری اسلام‌آباد با واکنش طنز کاربران همراه شد
🔹
بعضی از کاربران با اشاره به پشتکار وی نوشتند که اگر نخست‌وزیر پاکستان مانع نمی‌شد، پزشکیان تمام اسلام‌آباد را بیل می‌زد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/663516" target="_blank">📅 18:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663514">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
خدمات کارتی بانک ملی از ۲۲:۳۰ تا ۲۴ در دسترس نخواهد بود
بانک ملی:
🔹
در راستای به‌روزرسانی، ارتقای زیرساخت‌ها و افزایش پایداری برخی سامانه‌های بانکی، خدمات مبتنی بر کارت بانک ملی ایران امروز جمعه ۵ تیرماه ۱۴۰۵ به‌صورت موقت از ساعت ۲۲:۳۰ تا ۲۴:۰۰ در دسترس نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/663514" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee97d789f.mp4?token=GavInZF7XJc_3pgl3RvHLnz3Hu4kYs8AhzZFdiYoWN6s2vSLSaY12Gaje1Wcdk-qM5gbSP0F2w4DXaQMVIA_Q2QkC79i3zo9lzJIV1V6tFeHWbMxNmtj7zLUus2MgK7rP_DhuQKqkA-bKvUi6QeN7FNr-ongIzzcuyiHF3iYR5CbD173NnY8dV4gQOp3mwPirWESDkJajG_nDk9hHwjn1iusOvScr3pFDflGnEoUqVpWq4U4CJdDYeu1kulkVl6xF2_K2LFuJ-9PTt8OZ46CFdJhl-kjQbJ5LrhsjPul_myi12EOOVrqQBtaITqOof1tSIpxsmr7kSAG8D9WOY_ceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee97d789f.mp4?token=GavInZF7XJc_3pgl3RvHLnz3Hu4kYs8AhzZFdiYoWN6s2vSLSaY12Gaje1Wcdk-qM5gbSP0F2w4DXaQMVIA_Q2QkC79i3zo9lzJIV1V6tFeHWbMxNmtj7zLUus2MgK7rP_DhuQKqkA-bKvUi6QeN7FNr-ongIzzcuyiHF3iYR5CbD173NnY8dV4gQOp3mwPirWESDkJajG_nDk9hHwjn1iusOvScr3pFDflGnEoUqVpWq4U4CJdDYeu1kulkVl6xF2_K2LFuJ-9PTt8OZ46CFdJhl-kjQbJ5LrhsjPul_myi12EOOVrqQBtaITqOof1tSIpxsmr7kSAG8D9WOY_ceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
سینماهای 4DX در ژاپن
🔹
در سالن‌های 4DX، هنگام نمایش صحنه‌هایی مثل طوفان و سونامی، با پاشش آب، حرکت صندلی، باد، مه، بو و نور، حس فیلم برای تماشاگر واقعی‌تر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/663512" target="_blank">📅 18:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyuSx-PtPRp1bkJ-cYyNLrzgxGRRyC5xJ_kz4R0d2dJH5-inHGnUqxpR1MSTKJ7eaJoOFgT-fcxdAbOkouHGa47S19h1KIfVvZz6x5DtMfbvRPSci2jnPZ4NsUTbaZexFEC65MEKFFDujMw3Z_ztwo3s9mkIKzJ3hh_2Z9wOEifsqQqjF3BGQM5dRY2yQRDwLWSi7zvBKRnIFn0JgU22auh5XzrvWG9h3P5q8NEWnTDZlYk7tSjAwn-NaRo6TnBXAmV8QLtMFTnOa_cbIT-blom_3i48CxTpKO6BAHB9VWdaUYzlM23tPlA-hMWzqBME77jTkrXea_K8NpNA_vcm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663511" target="_blank">📅 18:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
بازی ایران ـ مصر فعالیت ادارات در برخی استان‌ها را به تأخیر انداخت
🔹
با اعلام استانداری‌ها تاکنون، ادارات استان‌های کردستان، قزوین، فارس، سمنان، گلستان، یزد، مرکزی، خوزستان، کرمان، مازنداران و زنجان فردا با حداقل ۲ ساعت تاخیر شروع به‌کار خواهند کرد.
🔹
تیم ملی کشورمان ۶:۳۰ صبح شنبه در مرحلۀ گروهی جام‌جهانی فوتبال به مصاف مصر خواهد رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/663510" target="_blank">📅 18:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663507">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSXUUYk1SfRmf1KlB8PNv3UlrZFLTqqoN9hAMEBLUyoMoGAmmYzShV6lFFIeFUgzBra8UIRpdkvUDBFqbEzPIIE6RnKPvn3xM6hIKrT0jmLvYSiK-zY6NnH2BrnjMYJIB_pZK3W1aMsVHK9B_RxFfeJo3vgnmxPHulUuOKaCn5Q3tn3pJewJJgTnXGigowvDl-EhtXY6R5D3vRrYO00ym3fm5GMGkdFLjPaQXwglYQM0XWsaZFsRYM3gSIcYKwX75Hi7U5yCVH3OIvfTFJHHdifHAEt_VEd4xHUHJ9l_iAv95QZ4ne2OILhNTxFXZ1jTbzSGQvZQrxJaFxTnUY9LGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUkh9v_saz8msBT5Q_OEZfajS_NGvVnlSeyxJ3UBgtyZd1kjdzgfgFg7K-knqUP0VLzXvbja0kLEDLq2ghuTTO4f98a2gIkLs79YlSIAH8BwnCo-gv6Lvj6LLqcVX2Y5G1UAcAJQ-7Qgb2xP-T56NKfpQaREtOWj0--Y2ZHcszpY6kw8xN78ddZKXmGwTRN4A6tgkMr79sndf8MlBELCiDsEsnTyCmLmVRSoS8S1I-SQyZe-xd4MBt1E0skSmnFcMscO9Dig5ds1V7KppqC2SKYM-fCmEh0N9pJz4DJGZzXKY5DAqbE_KkkxIyDnU0QvftW-HZhuAEImiMMIZStSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oY1EGut6F4bdK7wsuE7GUsnhoKeYicKgReo2A0igX6vCHqH_Th1R_CblQXw6VMwSlomQGesx4plp53niVR-U4F1OCz66rMhHe3w-07MssHy0lREqPq7OGh1W4PhKpDwOB552Ndmyv8FzgxG_Qjs-_aJGmHBmoQI-hNfV_fnn_I13bMU1kfD6yj9SXQIlQNtQPDDMko_1HHmB_h1oqlMcCe3jRlblIQYTxEDTn7JdzXqGSWeiqdEVrLatAN5_UbYsxbqDnb4b7QbOxoMyqhS8NxQRVAash-DXB9R8AJ3fBJ6NRm4k_aOG97rz3wQLrXgEOLL0VPLyolIAst1cIAzSrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور مهدی کروبی در حرم امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/663507" target="_blank">📅 18:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-663497">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7V_08iUw0bhuFc5xltYRTFxZge8rpCVHk00I5V4MMAZNpbuQXVCjN3-9NbHsuVnUzxQkSSVAvrrwgsNlU9-LGCgmRhh6J4V1Aa0-dzBR1mNzD9fVQkHL3ZO70h2lP4GQpi_qU6IVSJviEPQST-SvtakUIQEqQAwXT5zQvO7tK3BobY6P67H76mwsbFVUSQo_jjeDVeKk5MxwR6Ojc5X_LcljXkqI0TDXLJLkwiyu4bt-a3COz84LqP7sdQBGCSvLY2C6rgobRBgyEqq5IGCB3cwSHUqVaIkS2rCxWr_04b83z83zPguzXw95N-H7ePoekDl1FItnfUSky4z_vBtWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZ3SNrjW6aIGjR4PLudD6HIQaIFdu8j_Hmedm0FKGdEKr7jx03lT7sExFSsN402O_25bpAkiDNJui-E9UkCk_mCW5DvFIvYwEL5alR8AssIecOMR9BroqnVPFdITOMHpdafUr6sFT133eV0xiZVRC7uiv_VXt5fkzff9j1w4VfLVdKuUi1LJVnTWnV1NtbW26orzf9LqlrM0GadEZTgGi6EnleaoAQQTHcJEg_W11-aJBRHKFl6vn9awbG6yYZ6ekt7_0-KvtLjFEWnKTEQEwF7BEa8qJP5R0FSQq1iJDsdVOp4L3fiioSw6YJId_-rZ6ygioI_g6PNX-7lDOCkN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9hESdNLbUP-jlIyK3nWh7z5Pq8UYOA9rcQHKKHnW6nPGtRQEYZlVGTfwIx7fjz9vPLGeKh-Uip1Ud0QeQNiC-QZiTxSTRH3fjeDV3HObxQJTmN2C-6Fd7Z7JHFFKguHUI-2wh2wuIEXobQq9PKgblwXbjeG1EBkT6v40Eu46A7m2JmRCrHE_ekVa4DheXZ_oK0N3ScsUjewptssbNHLq-Oao_sNAKEX46DlPJ6QeDkuwC4eKFv5vslDZnhCsYa_G4ztcitufGF-0g3p3AYGpDiplLdRx6d6ngAIQMn_zsz7cV52BIoM6JHuzmT30o5dV8o1ROZMZ0jCyfIDnyhCag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdE_MYga_PnUNib0Sm5nA4V3ZqFe_B_9p0bl9lvV3XguLdBOqPiQ0p2ygwrCD6_LVhFvTD7q_TO6EFBWDtnYLXfktKPALSjBPrPXIoEtHxr4NJUe1YoRakIWPdv4JOY7JDfyscAASzjWvpjWhIEmghb4HjhcIgzVFZXuwNzS9ZN8Mzp2inwe1cDJbEnfJRTl5sstR6SDbTzIAvDLECAqjEJWQu5wqYVijBrHtbQfbGgCXiIZZlODz4bARj7I8IRRvmPJKYC6k9cfYTo6h-NFmWx7gr0ocV_b3DiSbRgvHNolVw_8ccJm765whChL9ouifbpEQyYShtWLTdWLW4QLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7yDNqvHiGMjs9GH0sokPJ2ZKpSlk4L6xdq8kT2aUaBg5k6drqfhvk_i95FKUHL6AhCQD5nIJjuj2NF4Hx09lRQACwy4ocMmqgOrVnSZVQ7izAEIy8EXe9dop0SsP9QIHsL5xdkpBGSgIm9P-jTaFO4yJXvDjftmFviuNF_ZaSZhWS7P2gqq3xUX2SXEDaho1kahL_zHFZn8y9naQswFmO5rS3we7MHlE0_2lAsCG9dDJz4bBEz4fMevBYWJQr8lWIbfjSqh-28JLHNffwUqMnJccAP_6oSOmyhHljQrXAaTNhjAd0M3Mn5L0Ve8-Cd8PebR1gH72lc1bhXrY9nPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqrzBgfPHdKAfnbNzQ66bUiDBuvPYPK9Ofg42_Q7aKdbNcRnZMmgrX72Q7-cnBki63hWpUYGlpxzh5KNH7X-HoNm3b3MJ2ljddCgIoPIfWEkhwCkywEmQrbWpi590yDPJHTCIOZNnQPIM__69zrRUQuqDI9SDMn0WrOGt6LsfzCI6_Xu6lwKuWlWRtYLbCN_a_eSw7i41evJFdJEeUw65yf4_jLMsIwGDKaIkGM1Nt-w1elx9vQ5uPYI5b58yrFDdBJOIXWwpIeOtxDpxFYsKJ0lXI1EUruvCsfIaNhhdZQ0QdowQR7RYKtmUkFmhTb56fR8vGZiMBJ3evdzGVV8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdp0DMC_W4t_sE1R_t8mMpJLtOrpUP7KEhNj6Jes-5KtV3ld8zm3IQdF1vrk8MmkgbcaFVjpKA9DJorhPMUGQKH2gqb_X3petNqem9aPyUqXN9UMOhFGe7KsXAEcZt66RimLtKePtCONxe83wU9ZXh--0mUaB9pYVlpN1GCssEEp3aKuCP-aLzcYansNeDRzUTBrsG21wouJ6IGw3DzjtMae5wNQItQ4PHPWaGrFTYQrL07MRsRWMQuBAPxDFc0DBzIIPBCwaJOnTN2HHAOuGXTVTddsIEy3epHJvN1xtNCFBeWDv1KTYLHyBvor6mjHp-2aKiZZSTKE7EEgnMqWBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmi-kutsgfjMk9HqtI4umSPQx8xDAfNlXCMA1ShvUiodowaQ2IR8ttTypR3Mo5NdzyRafgp2I_vp7hn042ONkx7rmJnQmkVqlMu2KrvNxcbVZo-1jhiBweX-EH1YbpvFHABI4Le3LxuicOXXXHKF1m5TMkiZHuYshmZ0sLdOjLobb7zNaR_vjqsClfuil-EQ56EyHIzVyxyGs6_vH2tUHn1kWllfhdcKjbmyOFA00A21tast4wQ-MFrF4Aw5T_AX5qtJbJw9tHnSfhkv12jtc6smdc8Z6JQkMOXLiIpSSsO-JrwNT-MiOaFYD1UoaR6ITzb1FwA9G85nMGRTfr3aqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuks0JJdEhM7ht1mRhrsUOgc5rbhgFkx8T3quJp5da57H4Itk7ZtnnLdG9A77cxy1oJNGCN3aXnM66_HRqwj-dQkEyvd9oF9fBwm1dkN6oMc7hYIK6C9gd1WoMeq1uKSWNTMenVtSB4rTaiuQy-0aNLjLSnPMCSJ53s8KwZy24lrmsesHzx7gacDj5BvbgNPpVjTlXsfv9R_1iOuCrrdCHfu1ErXLOhPC5PXhXpBX5p1VxrIXMIS6rrW8J3fwNgwP4tHprZ1a9g4HdEtaGceQ8kdBx9AyFZdEnFd3yjhYzgBeHy9U1qVOMEPf1E4yc7qDS1u54RXAMomwPwwsB0M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYlRymn2GiWGsfAPYeGOEHsEpBwwZdaS_KjbdN_imVz9t9FWTLW_c-SRhLmRpuzyt9dXJXkwJM6a7VMBCa1gVcYhB7AlLlcKLP-hR3EtxM3oQKB_rgEDdat7cximsCPvmQonJ65gg0nTE3IZq1k6Pt3C3_PINEPrl6Heua70ygS_NoyqioTxzo-6R_MOK6nW6a2ci6HZnasfbZsqlw5o7fQL09qZ6PYaUIMSSuGC1gdwIH6-KB4dpsdXAN8xX8yKi0X5YMyy90FHK6KoaCHNB7ov6ewJbQGEhL0lhyAm2lmhoCocvyEOSVS4sLrNWxtrt604WrwojVFPE3fo7wnBjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برگزاری ویژه‌برنامه‌ محرم برای کودکان در مرکز شیعی بنت جبیل آمریکا
🔹
مرکز فرهنگی Bint Jebail Cultural Center در شهر دیربورن آمریکا، همزمان با ماه محرم، با برگزاری برنامه‌های متنوع برای کودکان، نوجوانان و خانواده‌ها، مفاهیم عاشورا را از طریق قصه‌گویی، بازی، کاردستی، نقاشی و آموزش ارزش‌های اخلاقی به نسل جدید منتقل می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/663497" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
