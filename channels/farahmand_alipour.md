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
<img src="https://cdn4.telesco.pe/file/QSw9dBg0fNu8S-6JmttgUDdGuFxL7M3uG6DKa-xcgyQMWQle8tgz3hdXa13Bk3euXhgpQ2yRrTO1xrGC3lKtmvv_kWNIyN99ZPt8LRkX7Hzsh4JQzVi98GKwHu0lKOyBAHHjdArhxUs9J59hmC7PgQ85y3TH3jEGnh9Xvx_lrb7gSucDp44sr6Me1w0G1HPqPIz3vfsEpIM_HUQkhkTha46GLvTw1jUZEWjFf4e1DiXjdorxuwEAHIQSG4dfKeeLtjGBjEhpxTqLnlzvXw1Vi1qIvTReG1i__LpIrArZm2uZiRRrYK0y7rII3cz7W4dSeS5TS_6PK5qgSslXwLLBbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 10:53:40</div>
<hr>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fRAXIJKZv4KooSKMnjVYJEX2ecRRAgiTDqDqgz2hrrnnbYvPeORkoARUQpiPZq1vGEtgEUhW3ZfJtGNUcy0xA_r5ftFgWIEE2snb3IniYN34LsdSl6uQCugk_1xNZq_ia-9ppSfL_X0cNyyX63eIEHr7w5MD_3-IdybrW81UZysUXPFM_50S5YqvdOxE1QhD9duXh6a9ecweaTXlewTh8krw6d78SHxsvPocVeRNTI8ZzBc7lzjQqyDTMqgHJCx21L4TX_ekoPCHP1a6dIDiXYzQE1vD-SV3Ax65G1vXVAuiP9-CTRCy2qeQra4et65ZUkNdUVeeOhBYwmpRTE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMi18clNUoQI1ROilnVuhi32ajlU8RgdgqhOEhHt60flc9ZY2wXQmZthYuNlr-hjsMq7BN5Q3gAIIwJxEWIeCS_Dl6ZQ9CeJBwoiEbBOLuP5rRA53oIwsG7Cd8-4fQKdB-lQMjln3EtnELnl4kQ5RHnYLPtQ3wDt_COloMFz32Iwu_4IIVv3mWr7o39k03U3IE2O-EeGhtT5oqhWuEA-JiNopo5QLopK9RaQ8-iXDzZSuk6NFy2C4iHUaD4zVqdiRpz45nfD90VL4m95ZZ2qAEorGMcnTzUtVrTjcVpmDVazcko0p0UH2CF-p-AYH8xLq7K69wnB7F9XrNpHr40DIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADmX6iy2saQtxdvvsqd3kWqS5sNsuVF0gZKmMCZODe4HJFbWL19Cd4_G-jI0TtpsrKpk-a_e7M0m1QKos0dbgu-aHVgGXujTtvZctEQLpAED9zB4RfLoE-tuS2IxBOQaGJtCraV1_qbUlAtBzjRW-NCR-rP8ZYQakKmHcuuxBxZk0TmI24e7y1Lsi7fFewNLufWr6q3IiTTni_KEAITXmzbOwmaey8P4vqJjDV6XDbd4MgZCjVNBTm-LCPO3BVfvSiTU0qvEyeCovxJ0H8Ik4JZ1ZLkn_bs2KW5qSCJqTgJM67g6rKBjePGW0hP70R3iu-_R7hT_h9raHogjNLYOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99gftpphTHyhkJ9xPEhGIPwVC0jf9TJz4vpgFHdB19oMbse0KS57Tgn3LMR_kzuT1begK0CcZgmKvFs41FUCl2_yMjnrP8B7UXYYwtduRw8u0o2zHhwSRX9bTl-s97kuEeBRrTeMwrbJFY5I-vuIzEbsaNNy_t4HArigrw2YLZBVTiQSUqoYNY27TKv46lB9ExDH9_M2gCHvnMSUMJTMiqceCfNL-dzixu7k3OSDXgGdaPLWxlNlYtJZwhtFP3n7PC482FANbvHknDB1YuMakdmcSLvwzrSXVVEf8-sdmXxT1gTvOtCPLnYzQeEPMq_xakCZmGWssWsWkkSaqGcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1UyKuzIY7cfOnUVQ9UM2fscDXF8kkklybWltOYW-tvjOpmGj0MUxVcClkAgePVl_U6NboCYtl7jSMN3vpQR0CXHAsMdFamgOvI79hU3OAEZPcI7-UyF05SC_qKwRGD50DPsimKhC0sT0rM1WmpCqLQkGzKu7TDZyRtQNnv6RCsslC2DlTlLJxPEi7_P59rvGu6rYKen9l1VonOZve3_6GjRK8SHB3VJH3NNi1kc1okAWg_3eSm2fAFoD9bD6WhykHvE0Cn1n2BLCDH3B64BOU9jiUi5GGyXGOAJUUavGhAIdn9PHSN3HREaBhFUBsYZfJEHlYTC3mqWXO-wY2J4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=Ds7v7nuI_vXaSB3vMD_DvzvT1VVQzPrgU4RvLu3Cswj3hZZ4z6SFTxXkfIVXWWB4MYqal0sNdgrcY8oUfSSBuaZErCZk77au4DJPuOTvIWUDXpZ2l6nIGULi9xS8vISh3bJMNgVi16fR0dokLijrxziNSbLRolEKpEgpPvVdaQB9w9aGjuNE8EcgpdWKplRGloFlyPuLW0EC3nr30t8My_O-G4HbwShNyV415cCoZiABwB1-zItkFxWe2zantWryBTjtQarP-w4ZKaULk_2-qtxbjtMIIi2g86LwaeUlA_mpLDvj0CrSrwzIERj6wpsX9sA8xzWxQdU0xUTGQAfj1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=Ds7v7nuI_vXaSB3vMD_DvzvT1VVQzPrgU4RvLu3Cswj3hZZ4z6SFTxXkfIVXWWB4MYqal0sNdgrcY8oUfSSBuaZErCZk77au4DJPuOTvIWUDXpZ2l6nIGULi9xS8vISh3bJMNgVi16fR0dokLijrxziNSbLRolEKpEgpPvVdaQB9w9aGjuNE8EcgpdWKplRGloFlyPuLW0EC3nr30t8My_O-G4HbwShNyV415cCoZiABwB1-zItkFxWe2zantWryBTjtQarP-w4ZKaULk_2-qtxbjtMIIi2g86LwaeUlA_mpLDvj0CrSrwzIERj6wpsX9sA8xzWxQdU0xUTGQAfj1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clzQnuBVQiCufGySCrFOH6gs1_PI1Tz_UmVg9ED245YEwKlIAvNTpA5s5GTthKfWytFaEQl4YZqvtoJuakV5tlR8KlEX97JYJ0aZ_r6sLoZQyFP7MjdJVcxa_Sjo9vuZdrwACsVSf56x1KJsM6d0IiLIJmvOYGLXR1ykYljq0Q06-MCzCV_iGePwxsxA7t4qrrflglb_yjtpUcw6pd40wknt_cTWzeRlWLbdx7gJc5QEDvM5svHBA8hEuyfS1MokgMrvy-oPIrv2nUbhSBCTcKigVanubQkVXKoEa0cDa2XPv6VndHB279yubEw8jvHzpogcTPo-BgwMPaTetC0jog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGF3RByOIpIUgJDIy5SxGzOweFSa9ha1gWyL_6Cte5jOo9y2E619PekR5CzGCF_S4C_iWX-_W5sIjnxtZLTDOK9d-vjVoSwpBQxIRSRkyerPu8Ap556dmF64R_pqeF8OaygDm8LxJNfjh8MUiKSzHlISvghNP2KgauHP1zZcAisqA-yaEh7O9Y7aHMmEinxvq0xwnQY4lDOkloveDJMrx8bZUDyFDzfkkkmxOPXlJVZ0Qffc8LpRdTSd2bM_lDcoY7ltgyHF0kkjkNpZsrM2PgAliOl4QHO-Z88NoAz75VkxvRqSwuq-MUVcF752nsmWYjCzUqTtISlPgeXsRsi4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne5VXs8_ybH8mf6UEBsxaL2pYoMWWo5IrH0pMm18xD9Vorjb6QWPkECZY1QmKo4CCGABwVqMLk19yHMx1f26k974K46bNvbaW1z6g_Hwtfjww_ISMeynlsnMnnbinnA5NV4yB2fq982lgO8hEk82HiUQo_rfnY7MGq_FX0_gUud8XvbyztW6v5YbwbIOgCULdDItWJQPgdnox8jSrMU4GzOJPqd0ILtdxcBMrAkuJZZYCvrBdl7ukcCztg-6nZxWGPTiPAuJeNjcOY94XZ47WxJXT7DaRkeVU6ZjgX3brljYIftAM-L8nK_NaHA7M1zCTiMCLCvMZlEltk4PqhYiEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2gEVfDNi2P5xJPA2jdHSxi6kPrADS7Rw0FjMf8Kw_jBsIr1zpJ3AzY9Mp-KGll5pSEg6ZRRorBXzaShFb8dVFPOHgayUIEZHRdePB5biqWNgNXqN8BVEoJYw5XZSekqnMaR--rXvpZBflwZQ5xu5Wr71jK37mCHqjJC4yjRaUQ48vjDHTHEYq8jZsa5tjPubm_7HfyIZMryLotBz3jdMcx0bcbnpX5-G4yehipWpWgMmsu6HTlJ7vI-4BLJFbQ3KFi0HHGRc2EJeg5wWaK8TVWCZhpzNizbR6QEWS4OxsWkOjjOn3X5VRxnr3_WnVOclNKVcxe5z-kAyQKSo-vk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwC7TAZJlunCtK7VV5CO0I5e7Y3xNZmUI9ShIjftae5OXsKmR2ZDbu8p9cfSrrgc9W1JTtroX-QUO-DRzIdjM9A-MQH1Dkuh1sVfozyONKe7u6Qr3PEVfCbkyZ6xZDn6Xl5HKkVywzqR1ACxE7I-cdCzJ9l80cFXkkQm2r8r2dhTpMPHbVIi2Olv7taonAEhQ4ptEkuqaTtgPInc4GOYcCvxKOsh0bpANQW3JHv2EQCxviE74J59qLxqcSdmAPt_aVzUWwZ_Bo-atREhoGSCKrui-v9-VlO7gNQ9-xbHxxXeuwdwgGvSDNiASk7G1RCS5plCH7AssB_YDoFPN0omQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtNN94X5yB1UGhnDqA847MX2mi2Y4reogDTATFTWGaBqBSk17-GDyP1I0t6AMnw0qpvv5i4-nd4PCBTAiPFetlvStBQYodthjQiiYq8mkHVoCG44RYPL6mQ9MbIbmS8VrGp95VOaOXgiFbE8DcmTw5w_R4scgtBSlCTFWklIiz8O8eoSehRHdfYSsaDbvA7lAkF6Mn176AvhRooHIgU5PuQ01HjJPPTw7BL83NuZi7vbAeUdsjTlZODn-gw1T0OEj5qW6clCL10XSvGJGOgTLYUkluEYD350-g24AmWy4YqHLxC70ffCOVxml4ILIRwb7OMq-IKU4bFMsF7S4aQZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abOmcSonfvgHDaZgdiFfKmXK_p5jujQwOf7n717xwTg3FQJMKLhXzOmX4hCNLsAMzLvimqg-K9tHPmXaUXUtG5e7RdTamOM2JMTT0vzzMhlUmgOhVx-1aI8wM7uSJOxjnt-kH_Iyk5Fkz-cVaPUTfKwxqZZnJ91YfUrIXlZTm9aFvicmfrZEN-AXOmmcD4yMpTyuFqsOP7vs_p43gNbHj382WZ5M56dnHokC1I1LXN-EQeNK0X8lFM5M8M834DhpF8cNVYNIYp2hi3oEk7GJxNB1IhGpYl9zLt2WMyhPOb8o_CbV3b7SBH8cdRvlIEfI7K_u_R63mpEKfZ9VZcFVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYBbvIfdfaJhnTrB9hn6VuDXRGW0byzjmc-SRd6bYs_6sNUNlAUfX3A-QdK3k_BDYmBCR6U4CRXUw3R-iBYzjCUZYcq4_wwzUdbBmftB5kqBH0efzjx-U5yNYJg_oGqzJLtVHuAk1hs3eI_fIXL9fHhx-QRfr8pZCQN45k6hiHZrylXlJybXZ_cnfvlMlXYr0QWzKsjkEoQkcjVXQ2KYXt6bzfQiMte0jFQaEgGVmnqn7jFBHnuUpQROEfV05F4Gj_lrBU6wybwx-64LH54eWWUcespUKTwW4zIifWH8uH2F5vSxiLNhnKlob2Ir8MrUuhZCZwlp-5LlKJy2lWegJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPjsvmrGJ3LVPTE68NXw-lKn9COWjkYlf2mzy8g9J834Q6s2pbSxsnSPFJhnRwlVQkeOK6vaapMCNadZCWnlFIL5_2cy2GWWrOobn_zDfTJU1BlisgzNAm-z9_GQOeVIV5muh54W_PgDv-hPBXaKdmLaGT5Aw6DZ2SJ-U1Wo7oQKzAVMqE1jVhzPE3Orvdhn7oNuvX4ybgWPc-jjKlNT2CBPgeZlyBKdjKYBJyeBl9-L8tPixPa51ZXK1y0mAy2BiAkTioGEWKhoK9mDFYTbwLhWMEvjWLTAVRZIE-ypYlspxM53w7LYuXfAd5uu3VjrYcCMw2wSFSjHEs5VbILK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEiRrGdAkXqoezYBCQ8UqG1cnwvGEYmuDzGX3fIXukjGIGY15IlY4t1eueVfqR9a0N8XYr2k9VVpyz6UI1QnCHo_UjjvunxYFBQxzBeRCQGSGaJOanL3zzLm3Z9ZW6sErhT-Z6BmXqha4juvNaHkS_2rQaSkNVzy--9UDEXASSIrhcVsoIVuhhSkmEyF-E0K4Qj2EVTkiM4JcUBLjlbaI5dQmzN_1Yw7Hi3QLfoKIL9Q9RMWSe8iqJ4VHxMz5P02uFGEcPVOL5Ie7RbvnF59bx7OJJEtWRbZbRMhkhH5z-IhYM8gwzlV4rUXmDWlmW2qROKqAn4n_2Ge5Ax14tsruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=qpO_kXrCuYMvP_SgSrChpeJUeQ5_CRPVpTXlKYhfm9Z2Vy5x83N4VW1FpR44tLGH6UBaKNf4AvQkcghB5ZxJ-3862Ul8jxWUdv62EvRaytaG4awFNQekX0vbn6wCEz_0IqIv3_WBZZZe8CHP11BDfkWkwei8tgwCHmEqjbymf7nUq32PJ2eMvi3SFzZKg4_ZsxqsFH1Qrn4FWCUMzhiv6HnUzWCs3_aYL3nS57kENkbbuuWZBcwAYktvurZPsH6lJWXWv8co7etCnMFfglHUfInoIK_qxc0kkXv1hADIunnRcby0LsYTxBEKK1T8p75HIwwfOMcFvXYyhNz3mIe-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=qpO_kXrCuYMvP_SgSrChpeJUeQ5_CRPVpTXlKYhfm9Z2Vy5x83N4VW1FpR44tLGH6UBaKNf4AvQkcghB5ZxJ-3862Ul8jxWUdv62EvRaytaG4awFNQekX0vbn6wCEz_0IqIv3_WBZZZe8CHP11BDfkWkwei8tgwCHmEqjbymf7nUq32PJ2eMvi3SFzZKg4_ZsxqsFH1Qrn4FWCUMzhiv6HnUzWCs3_aYL3nS57kENkbbuuWZBcwAYktvurZPsH6lJWXWv8co7etCnMFfglHUfInoIK_qxc0kkXv1hADIunnRcby0LsYTxBEKK1T8p75HIwwfOMcFvXYyhNz3mIe-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJrKTHsWCAOC8HgpPeI3zkGxmjEGui0ySAGltCKfla99tuLHZxEEvjvUkJujOPIEH5LziAH8whEfA7HsswhTeDS7NJF7X1MVyX2Ov19nKpWyA-CSy8KcuZanfzypHgu5oSYjh4JjO5cmHaIbK_7ltQEhS1XE4I-0k2smiTX2zjcOBPS4ECoCTzIdrSMGy7CRKjnogypZq5FRpYIiDtdIWnsswLtl1YXVQ7BeSCG3aNkgkoHBclDRunn84aJsD-sAI-QSJh5bsTsXRJ0FahNY86V91w7fUJvWk-up6No1WuBmatHjEjMSslSuTOUmLPyRNV_t7NnThXl5BUqMBxmsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_yjt4l3iPOdv_AWwfHUIQ8MyHqDoN1T5VNWQIfIb28bvHSHQ7T2vdTPQB7MnV9ijtbGkGybiGugXpzzIyaugPTtykiXmvdVFJUMjevx2WAEQ_sW9ED6QAVJtn8CJYKR6QFRcLVeP-K6Txa2vfFBUks55FiOjxLVFdpjsdJOxRwjrYaL43JBPbZS8Azr2p2s4Et0V5OPYbRWy1IcxAVp18gJ22x_EGRze8zAuvmaPD8j5SLFUyrIMKMaqSErnJY59EDGb_8JBbAkVHyPUZgCYZVS-sYabwIS1QyJwE16vC-MuOWxsfnxUCUFk6oJRpb_eAWGMVPHCv7Q33-oonKWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=k8Yw8kBNqIb9MC3_o-rC8u28iLxKmWg1sgH0Z8Cp0KmxW6RU18OQoGgHq0-LYy6CzOi0F4L9PTkgYe7PpfE59OAWumS8bBz0nygfcjhUOFUwug-HJnSVYwnzwtBahm_R_XU-0GPcEcdavVeuveSvWSFfWDroO1SbDO_IEWmK4asZyq1Vlk8RwXNTjSO7XwYxWQVzi_O6GbKF9yXFyTo4KB8Fmx0J-z7LJH_6ITpLSeVLSFob_0dK1p0AZ8W3wd2SnRTXDmclvWHPnmq7M5178MpvqdekSgfdSXu9sRpGcLoteQzIv1mHkvAWWoGE-stwKKYfkr4DGFW85Z6tyoQiOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=k8Yw8kBNqIb9MC3_o-rC8u28iLxKmWg1sgH0Z8Cp0KmxW6RU18OQoGgHq0-LYy6CzOi0F4L9PTkgYe7PpfE59OAWumS8bBz0nygfcjhUOFUwug-HJnSVYwnzwtBahm_R_XU-0GPcEcdavVeuveSvWSFfWDroO1SbDO_IEWmK4asZyq1Vlk8RwXNTjSO7XwYxWQVzi_O6GbKF9yXFyTo4KB8Fmx0J-z7LJH_6ITpLSeVLSFob_0dK1p0AZ8W3wd2SnRTXDmclvWHPnmq7M5178MpvqdekSgfdSXu9sRpGcLoteQzIv1mHkvAWWoGE-stwKKYfkr4DGFW85Z6tyoQiOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvINTLguEhLMojoFjzKQdqnAjrLK0fCF2pqTwBq8QJO0DqtJDDsb6PbkUfxCzUv62g60XQ5N5qvntR79lAHc64Da4ATh0Yo5kRxZyUjHRDPzc_M1gug-N19PfLvnmXSaM3k6zpGVKeMX5yerTDLDJemiAyRuOf6oe8jQy8H1rTr9q1rThgL6YQ5QA5B-ArRTKkWcsZ_j2BaHk-VevPIcj8i4W5PJXRIO5lP-YgBNYB8yd0d0cPqJ74iLZgoM9v-SaWG5Zdk2Oy13Grl7Uq0Rw3jWTdeqjKeejfHzJrlF2tHiaoZib4AYrEixo0RWtKrfIy3Ywxi9c4I1WgYhUvJTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMU2o1LQMv1uMPPVgnLKROzFuQisy34vJBelPnsYxVdA-upkRBnyIGcPE-N35KYXGt-DQolLz6zOaZllDxNBQYHu1ttw0dAlxjIz6n2a2IY4Yv6h-savFhUQt6IHeVgsGsjQWBLNzArDtSlT6mnVGNsmsRNtw4k-hDsPwrXRbSJYtIMZvvp_OM4wvqOlf75Ec3Z3lFXE0EfD1sJiEbPge0OXbYwmgS5tMaZsjJlaAct-maT9PcYfAyqYlW-yPY0k54S48PG-hq4veNJLgh2qQ7ahzB4efksUkGFkNnH0VYFZwiQyp-rS41GMPBsohjxmjld3ZJs-IvnTM6KSoK2acw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=ECMKMRa0ul0qj4SbmEY9JFhx1Kq-yjNAZKwpJZdY9lMBufNC_fJof3alnxqswUWVFUhYCTLP1BSQ097yrguTuJKrjxqQ1iYIeT5YaO-C3XevYsmBTNAEtnQvRza1b8w9aYrJrmfl9_7weOSGPNJCjJtGV561bU0icUVbyVidbxfmnTAuoULYQxuQuEOMAtEoCUHZSN5Dqp_v13zjLlikZZYa337v-QA5I3Tay8WsbcRuadVKU3rRfm69FczCQGXcg47ooIl9DAf2_j9nAsDngR7TDNZe6PO6jhnlHq1iBCDYh0x7OOt1Fago4r5hbxWKnjXElyWEpQoECXIdMLOyOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=ECMKMRa0ul0qj4SbmEY9JFhx1Kq-yjNAZKwpJZdY9lMBufNC_fJof3alnxqswUWVFUhYCTLP1BSQ097yrguTuJKrjxqQ1iYIeT5YaO-C3XevYsmBTNAEtnQvRza1b8w9aYrJrmfl9_7weOSGPNJCjJtGV561bU0icUVbyVidbxfmnTAuoULYQxuQuEOMAtEoCUHZSN5Dqp_v13zjLlikZZYa337v-QA5I3Tay8WsbcRuadVKU3rRfm69FczCQGXcg47ooIl9DAf2_j9nAsDngR7TDNZe6PO6jhnlHq1iBCDYh0x7OOt1Fago4r5hbxWKnjXElyWEpQoECXIdMLOyOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDJdPoGTYeLjEbBdyNhDYVB6xNzv-S_EcyJoKuJsxjqefhEoy7B7olugytCvTuOH0Jlj75RMA-LRtdk_gKgQo74CCaTH1E8RtAuu_eGKQ1AE77ICGu_8pk44H31y8PVqRyMhePYxuj4lE4t4C_m2oan3ZlZPGrVCKqeuU5l-uhso06nfyA8_N6a5-HIfxwA_DxG2S30K0vFQHsQ4BTHlbT48iDJOWTE6lN4_ovwrDuD89iY-RVJ7j2n48ZefojqmSZs9U2m3gXvEhb4GFGpVbRYtME0yqGlnENwifkU-BuZgMY6UejlWHBiW5TKY1G3ebqjpuKqDUC2Yt-EoO7tQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c8bFaAV1aotsqIOulII386NpHPiNokegl16m6GTsD5RllIYewzixP49sWKpU_fW8ZfI8QUXoBJT-mjMNNNp-9qBTQrxJRDG2Eu7YtOQFcpQDn3hTzBN876BKjuIylMrPDHpUi-cNGSHO3wr7I94iiipfogFuCRnei0x7kFRLoAe2eSVestwP0pnDzy9CLnzOZ1xdK6SUZ4PnyDCQGbKiNGOHdiZUTq5vbg7B3hODzu2ug0eOPHrLco3FdNTHAJQMZHk7d_eQRa4nLhFP5DOc82oynQTjLpKY8bgyN3VdDjC_TOK_VBhVwwM9MRbaOhPBiJ9Cpk2SaH3MmYFU2DxxmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=LESBY1kqAX7Qruff98ivQ8CMgKVoZb6f1bbcAkjbtTH3wwjL2T4ulhNfR6Hj7HtDDZermx9AFnFLy_ONa8C3-Aig-2yuIfNvUsaDiAeu0aNoMglAN5k4IcAuwB-_TZliJnSSibZSnANxVBhVCp6gNz5hr8kcusZ9fItiUsqvhkWRiW5I7990dzGepz_2_h81vy8HjuMt3Q-7jjbK9UOlyAapXt5KF8ozMz86S62aQtBzB2OipeLlthAOfuq7thMwLXH06YEzZ_-c4NxSvReRnm-7JVNhwIrRlZUKzYMcN2iJEEdyg9FdHywjMfsJHKa1r9M2XZRGx4YhCoMohLSMSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=LESBY1kqAX7Qruff98ivQ8CMgKVoZb6f1bbcAkjbtTH3wwjL2T4ulhNfR6Hj7HtDDZermx9AFnFLy_ONa8C3-Aig-2yuIfNvUsaDiAeu0aNoMglAN5k4IcAuwB-_TZliJnSSibZSnANxVBhVCp6gNz5hr8kcusZ9fItiUsqvhkWRiW5I7990dzGepz_2_h81vy8HjuMt3Q-7jjbK9UOlyAapXt5KF8ozMz86S62aQtBzB2OipeLlthAOfuq7thMwLXH06YEzZ_-c4NxSvReRnm-7JVNhwIrRlZUKzYMcN2iJEEdyg9FdHywjMfsJHKa1r9M2XZRGx4YhCoMohLSMSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQUoLyAe9oE4hJDeYD-eluugXBRsMt6xxpB6a2PlxEstSl0GPFjpVwySot_UpMau0EKo9B8W7HnVmLNV3N8eiZqzUsJ5iDTiAuA4Qqvnb4YNBNNteW7UNVVSDKv6CSwefy_29udojCkl5uSq8EwZLDGjFZPQWsAPAhBH3bs79YGvK7_yg4t69qKB25gXv-byN2c761AP3P9-qCI-4dM3ImcE3rxMR8HyifcouMLzBmyJjoXoyjJeOWv1D4t_tILMgqci4SmkTC9l6GDJGxjTesABixgVV6mqnEUcyNJvaqQo_1-Orsngewx75WdvtVz8JA-auRT7O2jgAiqS187FDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7mLUcJCcY03-b6vacvciES8SFlX414Gklp4-Dhutupv4ccgc2MwP2nvANddsSxCOwREUtG9yUe8FynIs17woYkGZbP2-dsW84isJM013Ih0LJ9bu6DFzGH-4ygZRpfHFBliYqBDnutXLOIgeqhJ7eh3O5HoKLSn3lQtEv83oLJL_Ro2rs2qgvF4gOk2bZZW-WVtWr2KuPAMz-ZwWVqqq3qkSaqpPpV5MYENfNifYDKdSzszhoGGczA3KYEQfUb-0qUn7-0OM_8nqdb8xRtfOW6myU9CQLmvyO-TRPlOKA8wV49mC5LvmSv-H1oW3eDoarNzaHNyw0VXCWAGCo_qJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaeZqJ4N2kzFriTPRX4SuqRkwa4BsFyvkPhwXtBh7STZ2C2FYLR2B2JNgZYrwPkJ3J_vqDHWmCpXpDmKAQluk5YVka-KQn8PenKqYBs84iKuh1Vh7BgZvrjHweM1E2JkiWzhtevjTw0_Pq3ap46I9GiXD49NIDpsBqeFZo1oQGtGbnzN_UkQQYseS0IWgvoJE9vfN_au3CwmevNgTJFET9MxWugOj62wjdUEarNDFyVx2VRLkUBP9y2xXA6U07BNbGaZ1wWVfSNqEXznhlsag9iZedAGbfeF1Hn45fJR0HLBuwtX3fketTQkww7hnzzWhzjSgWnEQ4-uYENRO_vmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ru7pkn9FnI1IMHB87B5-j1L7zzL_PEuAAC9FG0rgelNdNxAlQ0aTpIhbP7nQWvhCyykRY0aVfCSLD6uUojV3dhaMkqH1hAlXJ6fKDqnt4nf0qmKQ_7JY1mTb-Re_-En1jrJAJFrFnfphZNoSR6hDkl4sc1GT_KHDCfbAaV-HeTlsilj33RdRbM0ukUkOnJhJ7LITAsGQSRa3hUacp9tvfBPJkiqGp1NfrWXgYvGgMyek5dsesaUotedk-TO7GMzGcPYxRjsbSZcunoJCb4rQxLcYCNd7VjwLUYc7NIhzPS3_f5KVnSSdY3X1AezYRiPGq54nejlKRDtvgXybI3GYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2MenczY5kAExdWdS0Kz61pA2hrqXNAccZqJRmquiGhyc6VAlBZqJwAGKIZ_qvZcbI8T1YabTG5UqNszyIEhB7ysjv3pAIJbLiLdLrb0TADO_xjTsZwKjUy4TNP0ru3smSuB88ls-7zzCltysb6JC1noO5sCe7x4tQ9JHKdtVBqwFyKN_yl1ZnkKIX9eKpksIfK3GenEhoozMEKw7h4TEa2Im3rq8Y6NUGcRDM2dndD6wioB8aMeO_cGNn47Rx7Tgh8jzQGeciX7n0k0c25-L6dbqyz-njcUoshFPSGAKSDsSN4x8ll4H9X9RD3CoDBXJJEA9qH7D1zyhdunAIyYHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQjlROSPIdDhqQ0aKPdUw7cfiVB7yQq8Wnd2HccPW-ioH8p9oQ795JsNx6hZJ3L1-gWADFLM6zh2APNrM-j-DSXU96ksb14GeaxNIAOKlQM9S3tnV0zNUSUYNwL_wykhSF6moug9Tb972gvLNwkjfXsUhJ-XGYlET_ruQf_XwPn2bGgfnrV77GmmAkCz3zmvj2FB7g4tCnjwDQPOCMdvC2EErWfAdteYpF0nYDeaUwvacCHWrZFDdn8qzfIeT2cI-qaG7pZsE64mufW5oXRfkx-WK-xOxBj6JF5zJ0CQoTZ1dr29po37QdvDILTt_VFepTahlGX934WgaWxLaMnSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9Dtb9yW7Q5pDzo7mIl2We4aBEm4_R9XL4eg75Z3Fy_uzMrg_ntNf8bBqX0scZYXfN-2efrqhxJh6q-Q0kO16UBFJdhH7JFtLDR84R-_NBP1-vzzEkGH0Nk6A1mlSVZB3bGdCJm_XgZeuG1g-bj6sd1hvuTqjY0tuzhZWm_-JQlylL-b2_vVGroX7WOPct_sPwNmF7jLEXT7DU_QKzVw5PDJOcY8eOOInOFt9USjRURh-KUEpBNUWMgP1i5cIlYbu5q42xXj5CTGMy7Q16ZVf_8eDCxB9vxLhbceLw7ZFTD29oNPmL6-Heixr6ORB6neBTFhzf0mM5n2hAuWgjvUeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9onFxYpxqD1Yv654pIV4Dl2RflzSQYSOHMxqlbel_DYvFPzW7c9kaN90FR2SmdF_tZzzLJecPDwaZ5IcmPdF2pJ0kNYifgLf14m-VgOl2mGPIyDS7q84aJDskjuOUWiZbI0xml2i0wV-XOl12kBOiiVQrFAW-2AGkVTTm3BeIFk4RiwbMucQFF3Wymj8B68ZCyxmmqsAL-wTHU2yuGoRswFC7UywJDPkC1PJDflV-0fa6Owpsbcv3_TZmX0bi7F--7RR8_LpWA17_whORDmazHtFp1gGMUv0WFvaSBCFd42A1ateahT6I002lr30X9sG2hqclf27FTEu_Vivdr-Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=rv7nOgfih93xTQAxQsNPia2eI7ZdEkGIFt7pfpl-bKRBTKsQoCEA1ZdIuXUlw6vwQB3DyUcf_Cd09VBUBMzaS1LizPg1p7BPCHsQj-BsrAVNbC6r3DngaONGcPJ-j5zggxQl5VFPHDn08LF8NacicBE7_hZOiBfZnvPm6lw2UHzQGwtAONwlGwjw4VekD5TxKcJ0hH-idU7yZqe6gwxF2v2PfkPHvmOmaBF8Md7AavjXUPBIK5XQJgslM9juic_DIcyf5hb6qO6_7P7TFkxLxq1sNqhuqv3AKYUAn3tqNXUG24PjtflPgUyezW4np1EZhdzSK8Zl_l-yI_csWfNthw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=rv7nOgfih93xTQAxQsNPia2eI7ZdEkGIFt7pfpl-bKRBTKsQoCEA1ZdIuXUlw6vwQB3DyUcf_Cd09VBUBMzaS1LizPg1p7BPCHsQj-BsrAVNbC6r3DngaONGcPJ-j5zggxQl5VFPHDn08LF8NacicBE7_hZOiBfZnvPm6lw2UHzQGwtAONwlGwjw4VekD5TxKcJ0hH-idU7yZqe6gwxF2v2PfkPHvmOmaBF8Md7AavjXUPBIK5XQJgslM9juic_DIcyf5hb6qO6_7P7TFkxLxq1sNqhuqv3AKYUAn3tqNXUG24PjtflPgUyezW4np1EZhdzSK8Zl_l-yI_csWfNthw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله سنگین دقایقی پیش اسرائیل
به جنوب لبنان،  بخشی از هدف این حملات
پیام اسرائیل به جمهوری اسلامی است
که قادر نیست با اسرائیل معادله‌ای تازه
در خصوص لبنان ایجاد کند.
جمهوری اسلامی با حملات دیشب و بیانیه پایانی امروز حملاتش، میخواست این معادله تازه را ایجاد کند که حمله به حز‌بالله لبنان مساوی است با حمله به اسرائیل.
اسرائیل این معادله را نمی‌پذیرد،
در برابر حمله به ج‌ا به اسرائیل به ج‌ا حمله می‌کند و در لبنان هم از ج‌ا حساب نمی‌برد.
گروه حزب‌الله چند روز پیش آتش‌بس حاصل شده میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5421" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPrH8wXmw7knitD7_PxjwZ0tEM1RaYQNgA89L_Xnfmp-ViX7R4QSUF714YiHjPzM8GuhJSV6bjzXfUWL7KnWyBJrBLgOaWlx5D0mhKl6k9ALMb3I5mbWFTxFDqY72fLA19QICHEDvVJYT0flQ7V8OjeznQT0M3bKeqxNgqjpfWW5mUlLV5T7gUpBGsIoK3Y3I-SPjPqRACVNEbRj2ieznwCW-Yzt3xcd2dzMM0FEtbunCE8x5FL9OCYNNhlcuRUqUHTMIYxom1QU0NCAu-4a2cm-0VbUgGqdweY13y4zhiIdMHlFtVkjVaxk_waxjBqc25qHjinPoP9AV3UmB6SckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=Ko7PoOi98r8Dfap9KcxDlrfPkYPIGFy7wuJQCBHrPeS3t0D0GDhM_BMaYq3vW1kkDN6s14Ej_08OANdqiCHdj1EB_EtW0R4igPyYqS3BosBxk78sk2UoZ3lglrQndb-8PqbWkLaDG6kLUCE95JRY0Pl6hMgWqBhfu9r3JIHmElCzv3_rQKQZJEY8cjJ4kQHghdeFxCHO3MJ-fh3nBIm-0dGaZP9wPlIyHHwZmfv6olDQ4QtYxLXxvBilGgGoXXbFRevvZYnlUN_J2n4E_Fb2tYAok35fVAljPKyciVVuT9GOSb4bVv9qrXSJ42eeoL2h61Y0sUh8eEqoLBKvJQjWyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=Ko7PoOi98r8Dfap9KcxDlrfPkYPIGFy7wuJQCBHrPeS3t0D0GDhM_BMaYq3vW1kkDN6s14Ej_08OANdqiCHdj1EB_EtW0R4igPyYqS3BosBxk78sk2UoZ3lglrQndb-8PqbWkLaDG6kLUCE95JRY0Pl6hMgWqBhfu9r3JIHmElCzv3_rQKQZJEY8cjJ4kQHghdeFxCHO3MJ-fh3nBIm-0dGaZP9wPlIyHHwZmfv6olDQ4QtYxLXxvBilGgGoXXbFRevvZYnlUN_J2n4E_Fb2tYAok35fVAljPKyciVVuT9GOSb4bVv9qrXSJ42eeoL2h61Y0sUh8eEqoLBKvJQjWyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=Gt6fgYAf56jv-VDEr5Fg7m0_tN6dKovZVefHMoWRl813u5v2NMXHP5FRhw9WVRIIxPU4LZB0iJA0_Uf19nkV_fhYfAUNLOoKXkdJt-x-NsVoaKSXP7ewGsnSXg92-bYK1vS6BqbVEWvv1MCx0P9kUK0gAprtTH-kyQRooXDZCNwgrbN6QMvOVIanljDSKuwH5JGea9_8xGhHPIByUssw-oOjWe8jjEAjBybp4D3ZGmifF8WNEnHRCaNC5pArukI6LFG0m1UMXi8Enif8KciRbmsgvbHV4KriSY3SxPs7DDlz8t-veGtfMI_mitSu0O0nluxOp3arRpHntOABxF0Bvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=Gt6fgYAf56jv-VDEr5Fg7m0_tN6dKovZVefHMoWRl813u5v2NMXHP5FRhw9WVRIIxPU4LZB0iJA0_Uf19nkV_fhYfAUNLOoKXkdJt-x-NsVoaKSXP7ewGsnSXg92-bYK1vS6BqbVEWvv1MCx0P9kUK0gAprtTH-kyQRooXDZCNwgrbN6QMvOVIanljDSKuwH5JGea9_8xGhHPIByUssw-oOjWe8jjEAjBybp4D3ZGmifF8WNEnHRCaNC5pArukI6LFG0m1UMXi8Enif8KciRbmsgvbHV4KriSY3SxPs7DDlz8t-veGtfMI_mitSu0O0nluxOp3arRpHntOABxF0Bvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=h3oModKE-_8JGHGIZipz3E1P4vHw1htAdpzWSLGJjBhDQGEEvNsVTCEfh9hOfnQC_QsKM3FFZZAVvs_Le_fMI46r8-NDWHe-lqZ3gdDcHJd6M4CUqtRhXjwhSb_sx1Zfp4BgaGiMUWaJ36mlH0GvjpHZrTaly4AQD3NPbJYELc82s4mqVpeAOQE1ggHzyBinbS6AQnUZ1o9tRs1dz2fgN5AMs4I5ZKzxQ_JNStNjgYkMMXIthad81UTk0jPGOaDaATiXyNrMJpgoUHzf2ttAIOod0RxwhF0vHsiv1jyO7BSnMXPO-5aJiMwlJso-RHQIhw7W2DAbpkKF7L5Zv0vAQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=h3oModKE-_8JGHGIZipz3E1P4vHw1htAdpzWSLGJjBhDQGEEvNsVTCEfh9hOfnQC_QsKM3FFZZAVvs_Le_fMI46r8-NDWHe-lqZ3gdDcHJd6M4CUqtRhXjwhSb_sx1Zfp4BgaGiMUWaJ36mlH0GvjpHZrTaly4AQD3NPbJYELc82s4mqVpeAOQE1ggHzyBinbS6AQnUZ1o9tRs1dz2fgN5AMs4I5ZKzxQ_JNStNjgYkMMXIthad81UTk0jPGOaDaATiXyNrMJpgoUHzf2ttAIOod0RxwhF0vHsiv1jyO7BSnMXPO-5aJiMwlJso-RHQIhw7W2DAbpkKF7L5Zv0vAQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u-96WkOLjrWj48HDFxJd-aVg8kNh9TcJccisVHeFMTCRnmX5MwuFby2sokKq6dgDmJnszWK5h_bjwMLYLuZF5V_bKige6k9n2SN2Y6QqHUv89k8lVCpfsZ-RjLIBaCD2Yxmsnl_epy7U164Thbc9b_dDgjsw8XPftK7osBCH6efLkGtkD-jtrqNkFOUJ6naVViuuz_1NxJpL3lQ3OBtRBWm_q5YF-BExOD1mu4RLGtboNu47erI8okBcLNDYy3YUKEYpLH1ghWbxFxEd5dvWbCkikHZIkIG0C0FgVuoc42H5DmLTAJiVHoF4xYoChrK_DvcgBkUpZVvYKqVS_3sx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4wcsiFHu7PgqWKl-ZMOHlZ4d2RwuUVrF31zI4yHTk7f84ESVJLkhR-08HcNiMSGZXYRwDXIK6ZYdrlUpD6y-lrwV_7DftI-q26F0bk9nEYya2jX5rdDy19R4vwgJLpzepa1dCnguV-S34SLPXk2d0bCcZKngtnuCijOtdE277wAQ9j31ccY1tYL7g4gRaeUQyxx96nywLd2PkFCm69L-wUdf-IQZCdD2DYmb3LAxZVljDiqa_CIGhLs8YHYKD6wXZFY_hCBFM3BV-bCusDE9nUXvNuN20aHIF_1wQGypzbe-MFk42A6KOjGljq-s4Pi-h3RyfeYoDyvguhMyCfQCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=r0IgKL5c6sLSrN2ByWFxrfPgbNhKadj8T77xou7T3oNWEYFp5O9-TIu4yimUaIYgUVKorpqgBZsBFwcGxXt4LYAkYfironGZLTmL6b5ZfUiyLxzwSfenWxndKRN64AvkmGZPyheBF-fhuly7VQj0OoOHQFKOLnht23FkUPfRKxlqhQMgj2l5F4d_Wbi8U-Ya04GfefOEUt2zMYv6ndmHN_KA6-wBw74NBkbYcbjRAaQrR7hbeU6ATQ_EWN1G2_pyIorDDEiolD90ppuJ5Se76dzycCHKPQ4YkGMY6aReSxvIaHUyq0dHcq3dHZv8oqid0dXIrwbws39OJIFnA4SpBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=r0IgKL5c6sLSrN2ByWFxrfPgbNhKadj8T77xou7T3oNWEYFp5O9-TIu4yimUaIYgUVKorpqgBZsBFwcGxXt4LYAkYfironGZLTmL6b5ZfUiyLxzwSfenWxndKRN64AvkmGZPyheBF-fhuly7VQj0OoOHQFKOLnht23FkUPfRKxlqhQMgj2l5F4d_Wbi8U-Ya04GfefOEUt2zMYv6ndmHN_KA6-wBw74NBkbYcbjRAaQrR7hbeU6ATQ_EWN1G2_pyIorDDEiolD90ppuJ5Se76dzycCHKPQ4YkGMY6aReSxvIaHUyq0dHcq3dHZv8oqid0dXIrwbws39OJIFnA4SpBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=l0OCA8VMfejUGkNL7Jrbwg1IvGq683vTa-EMYjOehYPSL3wI7fkkfshn_dpS--saBxkaCmOwBCkYInibprvlAgjMh0Qumxos-LOSBB3Zdn1nfkPunU8v1_09q_frRcqH0maT2cqdITku4d5TY38CY4x2iWRkLyGhpKBsKGL2GVbU_b3YhORLH_qQ4l1hZS-qVy-PCj25J5vmHKFFzAaySOMQ_nxEEqebMCM3OHLN71-jUv5xPduSj4k1KIWFKj8ZfWmd18aNnmHVPS41D_I1a2ig18V1LFthCk3Mct3e7LsjzCwd7Z4XGySHgOIGJVVj48zM8uMfqhsZBeBK-EjX8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=l0OCA8VMfejUGkNL7Jrbwg1IvGq683vTa-EMYjOehYPSL3wI7fkkfshn_dpS--saBxkaCmOwBCkYInibprvlAgjMh0Qumxos-LOSBB3Zdn1nfkPunU8v1_09q_frRcqH0maT2cqdITku4d5TY38CY4x2iWRkLyGhpKBsKGL2GVbU_b3YhORLH_qQ4l1hZS-qVy-PCj25J5vmHKFFzAaySOMQ_nxEEqebMCM3OHLN71-jUv5xPduSj4k1KIWFKj8ZfWmd18aNnmHVPS41D_I1a2ig18V1LFthCk3Mct3e7LsjzCwd7Z4XGySHgOIGJVVj48zM8uMfqhsZBeBK-EjX8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyFesB-jxva-dAb6S1JFKuxfZt2GUfp25sXQX5Pu6Y0MwpQP6uJqZOD9LyDhj1QI9xjTOjBGmdYTovzTPSEUYTrGXzeHB17iqIl7CjpIxS-BdpRLc_F30rCf4yjwdDVhBT7ebpKpoe2pAGkdMcahyJ9C9fAPYh7ZyMaxYcrVMJ5wfmA-qIMTkzDRNgOKPWt_DEVOr7pMxm2-IlXuP_S2VRonkW5yTwRzYXwfSCQKxlJEjinN6AnMnMIB_knue58oiN8jWXdIN3fSIbiXCTfuGCoLv4lJ7qw_wPlSp5G8W-wNLd5XgSv_i5xg7Kl_Nq93iHyl2blOOYxwRrVMHPf6cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=BEJi9xXWc4XWqxRYK1Y957LoWXj6bHCa7eTaKC-FTr35rtP2UwUAesyR5nGW7JzAGhvBI1P6q42mE0KOjPws2_jDWkTIk0h88O6W_ohkVExC0SmC15KV8hqdLaagaa7aIF701nroB-xJzibDsCqy6yGe1ZKTMSqOsoMcD-cUW2CHWhT5TLuHxiHNGkwCLP4LedpvCDImA5XCaagyXS1feBM8I5vsQw9eFopsIx8jPSx1s4QAJpg4samKFc1NtH2KQ3ivt6d6sDZ2-dY_xCPu-o18262rEwO2FdBB7EoJ45N1UJnnPkcrW_-U9AyVBQNU-jYnKcb91cnIrzBEcyg35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=BEJi9xXWc4XWqxRYK1Y957LoWXj6bHCa7eTaKC-FTr35rtP2UwUAesyR5nGW7JzAGhvBI1P6q42mE0KOjPws2_jDWkTIk0h88O6W_ohkVExC0SmC15KV8hqdLaagaa7aIF701nroB-xJzibDsCqy6yGe1ZKTMSqOsoMcD-cUW2CHWhT5TLuHxiHNGkwCLP4LedpvCDImA5XCaagyXS1feBM8I5vsQw9eFopsIx8jPSx1s4QAJpg4samKFc1NtH2KQ3ivt6d6sDZ2-dY_xCPu-o18262rEwO2FdBB7EoJ45N1UJnnPkcrW_-U9AyVBQNU-jYnKcb91cnIrzBEcyg35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYMTNCrRVdwj4-R1ysNRYAOQpEWJb2BJGgwCJOIhDV3e9CV8tOiROKESbFyTCHYt3AljtKriJSP6qL_3Z_-hZvpZykb_T5ysBe1fsCy_c1zQ9A-tKnvl2-2rjDS-cwvUZkXJqxfcIwXgIBQCBtgpKgC5EhkKzlrmVq9cMM61kX4A_bd7hvD72ajy09ncojYJ2GOKC4kIiRv8gAieMe5JqBNAy4TmZWMk6mL0RDOzYc949adBqTZIAC9n575ar1W6DaR86-9F5lq4u6F5bGQ-Xx28geC5t5xooiiLaMNaZrtd1Xx4Q3xwpeXUyLkbIcOiuM4GgfBs7Ou3HELltb6Oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBx0EUUq0698i7PY7N3T-tec9I2yCAvolHnOjgqOMoCbIVvc4aP-68S-j3pSSvD_HVLKTAFdWaKvsRxbaUf3LqenxMY_fbCRr9LgYYDa5hamvAVtf4Q1V7LBDpogqGOelSVzkh4xW70lekl8xeVzWuDinohxcZINBS-8s803ylyMNamY-4m1jEsof6e8lXj-UpjRPfO4BfoWF2GtIP14tYT-SvB1cTZujU8izSQ3xBgYEuYPrLKiodaZbBMUTaUZz_BJu2c-o3GNtjTRYOT494riCGTCllyDFxigeAgRQ60362sAZacQHm4riM87aasxSlMhkLSTp4ltCn8tJl0Vtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.
دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین شاه ایران است،
امضا کنند
که :« جز تخم نیکی سپهد نکشت!»
متنی که در اون نوشته شده بود :
«نگوید سخن جز به داد و خطیر
نباشد به پیمان او بر، زحیر»
(هیچ فردی به خاطر فرمان‌ها و تصمیم‌های  او دچار آسیبی نمی‌شود!)
در واقع ضحاک به این بسنده نمیکنه که
خب زور دارم، پس سرکوب میکنم و حکومت،  بلکه احساس نیاز پیدا میکنه به فریب  افکار عمومی  و فریب ایرانیان!
برای همین دست به تهیه این «شهادت نامه» میزنه.
و از روی ترس، همه بزرگان ایرانی هم صف می‌کشند و گواهی میدن که او بهترینه! عادل‌ترینه!
که با این شهادت‌نامه، دشمنان ضحاک به عنوان دشمنان یک شاه ایران‌دوست و خیرخواه و عادل معرفی می‌شدند!
کاوه اما این بازی را بهم زد! یک تنه! تنها! طومار را پاره می‌کند و به ایرانیان نشان می‌دهد که رنج ایران از ضحاک است و آن دو ماری که بر دوش دارد!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDoQyxCNKASI09EZkkiCbKydHIUFgyVAry6AikkNZjxRO4dWEZKIL0r8JcxzNH1EI8Z3Bc-wRCPYENGq1Z5_WJvPdbMfKemcdZ39WtaQwGX4Bnzs6x1eMnJ6-TgqzRRwazkwKkUdnRKNPlj3d2moqgqsSqORdECwu_OymmU30JwNXx6HAl5E1cnSMGaCTWp5bYHdIUraiH9MjUdZsrIOfBIwZDJTPEH0JwSZ32ccD1KMi32Mf9ItaBGWKvM9X86BcfmEBphM1UHtjKjJzXD7EjdE9MYKBfdQ0OPPT8ecwMKlhtP8HE3oQ-VLer1r1E35xXKuuxx_QHME28YPuVsCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صداهای انفجار در تهران و اصفهان
🚨
حمله به دانشگاه هوا - فضای سپاه پاسداران در تهران.
🚨
گزارش‌هایی از حمله به یک ایستگاه متعلق به بسیج در کبود آهنگ همدان
🚨
جمهوری اسلامی در پاسخ به حمله اسرائیل به پتروشیمی ماهشهر : صنایع انرژی کشورهای منطقه (کشورهای مسلمان عربی!) رو هدف قرار میدیم!
تصویر : حمله امروز اسرائیل به تهران</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5399" target="_blank">📅 11:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5398">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exQ6kqW_ETB0q0xdhnqqESndHT4FP1IfM12Q6HzJcUUeCBQv0D3rqL-gLV7mNMSvC9sGj5ermVBzEuiKg5cfw18xHQEgpaEwyJaGfrluR_g4rPapQGsUyEJVU1FNclFwOBxAms2Yxbx17aJ_KuJevn1I0gtzmLd9dc1YcBR2aUVGuZUa_DIDriZRuZTA1fkBX184TVQrqUGcG2s_KOEg65LhEwcyAmY-pTAfdBuXAvOQctXHOXvzu6yXZZgP3BRTBGWileQ_BS71zIm5GTE3IDQv9oB65Z7F1b6dI7b83ZSfMB4m-4Kzp0wUSlPAgI9HkNeld8f5HvOP7UoBzs3CsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی برای عمیق کردن دشمنی بین مردم ایران و اسرائیل این بحث «پوریم» رو به شدت تقویت کرد.
۱- پوریم اساسا افسانه است و داستان!
هیچ واقعیتی نداره!
۲- حتی اگه واقعیت داشته باشه :
یک وزیر ایرانی به نام هامون تصمیم گرفت یهودیان ساکن ایران رو قتل عام کنه،
ملکه ایران متوجه داستان شد، قضیه رو به شاه ایران گفت، شاه ایران هم با عاملان این طرح و با هامون برخورد کرد و سرکوبشون کرد!
حامیان جمهوری اسلامی حالا اومدن میگن : ما میخواستیم یهودیان
رو قتل عام کنیم، چرا ملکه رفته لو داده و چرا شاه ایران دستور برخورد  با عوامل طرح و هامون داده! عقلشون هیمنقدره!!
خب شکر خوردید خواستید قتل عام کنید که شکست خوردید!
کی دستور برخورد با هامون داد؟ شاه ایران!
۳- این داستان اساسا افسانه است !</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جمهوری اسلامی از دیشب تبدیل به نیروی نیابتی حزب‌الله شد.
وقتی جمهوری اسلامی در خوزستان ، تهران و کرمانشاه جنگید تا ضاحیهِ بیروت بیروت آسیب نبیند.
مقامات ارشد جمهوری اسلامی بارها و به صراحت گفتند که نیروهای «نیابتی» را ساختند تا آنها سد دفاع از جمهوری اسلامی باشند،
مثلا خامنه‌ای سال ۹۴ گفت :« اگر اینها مبارزه نمی‌کردند، این دشمن می‌آمد داخل کشور... اگر جلویش گرفته نمی‌شد، ما باید اینجا در کرمانشاه و همدان و بقیه استان‌ها با اینها می‌جنگیدیم و جلوی اینها را می‌گرفتیم.»
یا قاسم سلیمانی گفت : جمهوری اسلامی امروز در سراسر منطقه دارای عمق راهبردی است. این عمق راهبردی نه برای کشورگشایی، بلکه برای ایجاد یک سد استوار در برابر استکبار است تا دست آن‌ها به مرزهای ما نرسد.»
یحیی رحیم صفوی : «خط دفاعی ما به جنوب لبنان و مرزهای رژیم صهیونیستی منتقل شده است. این توانمندی مانع از آن می‌شود که دشمنان به فکر تعرض به خاک ایران بیفتند.»
دیشب اما جمهوری اسلامی تبدیل به نیروی نیابتی حزب‌الله شد!
داستان بر عکس شد!
جمهوری اسلامی دیشب در خوزستان و تهران و کرمانشاه و تبریز درگیر شد، تا دست اسرائیل را از ضاحیه بیروت و حزب‌الله دور کند!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5394" target="_blank">📅 09:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=u4L8x24jT7EFPP19SXqO36nA7LtaijPx3A4j59MTdUBwHJ0XL7RGvbo7V1qrXF0nW97KB3nS7EqwxWJhJZ27PC2u01qHbF6ICcDpWRV7dcrsstbHh1gswuQ_KQfnsePBZQHaSASIkkxrMmPNFDHvB3c4TiOrxWLuUGzslook9N8qsNv3QtjAAlIYuD3UluNq5HL1Wbn4-fDigWYEAcn7OE3eZiIIkPOoUB5XJIxM60vOKOx4xvgOqrD1RMNKWskyVKvz6DT4HpP4FibDOXd8vNVWeHsXjKa1KW_qk63Q2blS1bJg3h_3jfXoyi4u7F0V_zGAUsV-6iJ2o5sJoDnXtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=u4L8x24jT7EFPP19SXqO36nA7LtaijPx3A4j59MTdUBwHJ0XL7RGvbo7V1qrXF0nW97KB3nS7EqwxWJhJZ27PC2u01qHbF6ICcDpWRV7dcrsstbHh1gswuQ_KQfnsePBZQHaSASIkkxrMmPNFDHvB3c4TiOrxWLuUGzslook9N8qsNv3QtjAAlIYuD3UluNq5HL1Wbn4-fDigWYEAcn7OE3eZiIIkPOoUB5XJIxM60vOKOx4xvgOqrD1RMNKWskyVKvz6DT4HpP4FibDOXd8vNVWeHsXjKa1KW_qk63Q2blS1bJg3h_3jfXoyi4u7F0V_zGAUsV-6iJ2o5sJoDnXtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=Rs6iAukeY9tL3OVNtRGBGzw4nr5Hej9YFRafvcbUW85ax2s3LC40DBBI1P7rUtzFqg28__RW_qegI5ftNWr1KhdVGSj0UmKTGlSYRUiWN8R7PnrCpRMuOdEKosaeKmOAVmVQGX_oWhuCJdiFSlT3XnZt1RndB0bXnuQxazJ6c79v1DPs-tV3-JY_psGvgnvuRm956117PKr84ZiBI4eWB9e1L4sBO4ZS_PNQiEGj_-SwwAcFZTSmYI6O0tAKkQfc0Myli_n_w6h28q1UYmeaQBJ-BCok2ikrCypvMAUrh3-ri-AFIhJg7OEClt4KYRU7J7fnIeF5hYP3tcUZRCErFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=Rs6iAukeY9tL3OVNtRGBGzw4nr5Hej9YFRafvcbUW85ax2s3LC40DBBI1P7rUtzFqg28__RW_qegI5ftNWr1KhdVGSj0UmKTGlSYRUiWN8R7PnrCpRMuOdEKosaeKmOAVmVQGX_oWhuCJdiFSlT3XnZt1RndB0bXnuQxazJ6c79v1DPs-tV3-JY_psGvgnvuRm956117PKr84ZiBI4eWB9e1L4sBO4ZS_PNQiEGj_-SwwAcFZTSmYI6O0tAKkQfc0Myli_n_w6h28q1UYmeaQBJ-BCok2ikrCypvMAUrh3-ri-AFIhJg7OEClt4KYRU7J7fnIeF5hYP3tcUZRCErFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCWZoHTbCuOH3154FcfLQOSuToiL0R0Q0fodZUXMWaruKORhzv-uXUStr2kqtOoQZbszbCThjhk-Qii3ugi4_X5Cys0sycNrDO-yJByTN19NJ3AH6Ckvl1ggslmpuNuvQTucevvrWhi-yiBpB0JCnAyJhn62vY2ydYl5cdSrS6iSXbGSWUCPIqzLS1jvMvWIglGfvzrtNOSTbrSzwpXN0KVfI5yREurA6qdn-Nt82OKg9XwsWa_XlWo0FzvO96kHtELMJRH3ljdhZgBysz835J-ej-xLNxYyzOUwmhbAq2ehRu6tK29lyaDwK2WqALQd5_V5C5I4SA8agizE7FGloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
سپاه : اسرائیل شب گذشته به چند سایت راداری در سه نقطه کشور حمله کرده است.
🚨
سپاه : دقایقی پیش حمله به مراکز مهم‌اسرائیلی چون پایگاه هوایی نواتیم را آغاز کردیم.
چند توضیح :
🔺
سایت‌های راداری که اسرائیل به آنها حمله کرده کار شناسایی و مقابله با جنگنده‌های اسرائیلی را انجام می‌دهند که اسرائیل به آنها حمله کرده
🔺
سطح ضربه‌های دیشب اسرائیل به نظر میرسد کنترل شده بود. با توجه به مخالفت ترامپ با پاسخ دهی اسرائیل.
اما به نظر میرسد سطح درگیری و ضربات امروز افزایش یابد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5389" target="_blank">📅 08:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1yNzw2O-hibtEgkXo88pTBpebrAGtlpSWk9d3SDc8GD_0zqHCsR7DLMV7Qh-Vl-eX3FzfPMGnxtUIhh0-e21tv53CEx9wFwU8H7J4CFAIrB33jblUbQ5eRG38SYqq8Ha3UV6lFzZiy4BowbmZMNiZfxp4mxKAveHaWuKUhDY1SiWNslnHxk8bs4V3_coIp32VDTkUvfJDXDQUQ3z44hbJgVwwudoF_RV0ilsgWWKyWY8GVRejEePFrYeOhPJ94YNlwJ-rgmASY5HALrrb5Uy_7t0BF0HcgxBhMqJNKMPSPKTdUOmKfvWkIiDKMdoUREF54q7mfvt9yehL_l1jH_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسرائیل ارسال هرگونه کمکی به غزه را قطع کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5383" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
