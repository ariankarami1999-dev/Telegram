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
<img src="https://cdn4.telesco.pe/file/fCTAvFmpGhIiDlGKyMLZf_I6ZNZU6_lrgFlDmDO06hhkU7ZSRONIF3hQTVywJjNRy4cC7XLETBShSqnJW5XZDMUeZ40qx8gnfnvwQIeZ0GYSbC2cHfBZk7h-3sfVlKAwvuJMD_64Jn9T99ohgEDSYStewm_QKbMY8Jf1xWevoXn1Myg_gBEmsbk70NTbxbjddQsNrcH2dloMQYoVqaxXtaDRC1NDn3LHLTq8ZnH2U-xUx5ABqnDBxUG64TmcxBIQmnSkIMUm2K3uNqhhVXLNvz_NgKXTVJCv_lkOm9XtMtO6dUvUCk9S0dKW2bv98ychhkoD-EfCKAqhuK3nktKSww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6fRAXIJKZv4KooSKMnjVYJEX2ecRRAgiTDqDqgz2hrrnnbYvPeORkoARUQpiPZq1vGEtgEUhW3ZfJtGNUcy0xA_r5ftFgWIEE2snb3IniYN34LsdSl6uQCugk_1xNZq_ia-9ppSfL_X0cNyyX63eIEHr7w5MD_3-IdybrW81UZysUXPFM_50S5YqvdOxE1QhD9duXh6a9ecweaTXlewTh8krw6d78SHxsvPocVeRNTI8ZzBc7lzjQqyDTMqgHJCx21L4TX_ekoPCHP1a6dIDiXYzQE1vD-SV3Ax65G1vXVAuiP9-CTRCy2qeQra4et65ZUkNdUVeeOhBYwmpRTE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=PZJyMxz6ZNz4g0UCntr8Hhmgk4yJPbUI-LZrXEEX69GG3mwIMAMn4oMDHGF-iefR2Qi1gKncNLiW4M-1SXC3Kk6Aj_nxhzsudO5wnvUcR8I4witI2Pdg_au_C6JIuuxGONZHlj1XJ-mYeV1Y4-udHNjKDifvhKv8zYAWA3UcAXF5O8enXi9eoGgetgl8gHnOltyQIDjAzdR8mND5O4GZ55GnL-eNHzugAWzZ1B4Ie3pcG5AGG_CkdCi-JR1J4qzcIN-aaaSNAyaLDwEdL8iggMW-LcB7fw4UYRp759OAccy8_QmqYUM1h4a12f8FOm_gvJUnAWIi6VKy4hxU0nnGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMi18clNUoQI1ROilnVuhi32ajlU8RgdgqhOEhHt60flc9ZY2wXQmZthYuNlr-hjsMq7BN5Q3gAIIwJxEWIeCS_Dl6ZQ9CeJBwoiEbBOLuP5rRA53oIwsG7Cd8-4fQKdB-lQMjln3EtnELnl4kQ5RHnYLPtQ3wDt_COloMFz32Iwu_4IIVv3mWr7o39k03U3IE2O-EeGhtT5oqhWuEA-JiNopo5QLopK9RaQ8-iXDzZSuk6NFy2C4iHUaD4zVqdiRpz45nfD90VL4m95ZZ2qAEorGMcnTzUtVrTjcVpmDVazcko0p0UH2CF-p-AYH8xLq7K69wnB7F9XrNpHr40DIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADmX6iy2saQtxdvvsqd3kWqS5sNsuVF0gZKmMCZODe4HJFbWL19Cd4_G-jI0TtpsrKpk-a_e7M0m1QKos0dbgu-aHVgGXujTtvZctEQLpAED9zB4RfLoE-tuS2IxBOQaGJtCraV1_qbUlAtBzjRW-NCR-rP8ZYQakKmHcuuxBxZk0TmI24e7y1Lsi7fFewNLufWr6q3IiTTni_KEAITXmzbOwmaey8P4vqJjDV6XDbd4MgZCjVNBTm-LCPO3BVfvSiTU0qvEyeCovxJ0H8Ik4JZ1ZLkn_bs2KW5qSCJqTgJM67g6rKBjePGW0hP70R3iu-_R7hT_h9raHogjNLYOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j99gftpphTHyhkJ9xPEhGIPwVC0jf9TJz4vpgFHdB19oMbse0KS57Tgn3LMR_kzuT1begK0CcZgmKvFs41FUCl2_yMjnrP8B7UXYYwtduRw8u0o2zHhwSRX9bTl-s97kuEeBRrTeMwrbJFY5I-vuIzEbsaNNy_t4HArigrw2YLZBVTiQSUqoYNY27TKv46lB9ExDH9_M2gCHvnMSUMJTMiqceCfNL-dzixu7k3OSDXgGdaPLWxlNlYtJZwhtFP3n7PC482FANbvHknDB1YuMakdmcSLvwzrSXVVEf8-sdmXxT1gTvOtCPLnYzQeEPMq_xakCZmGWssWsWkkSaqGcOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=m4ZMadD-1kjwwDFtu6iqOXgqmDm7hqXR7enFVrO_Q4EO6x8szeJTUxHWQYXRNyk5d68QmxwttjbLdATowITusPdLyJRw_N9VPGJ2Yr430SinR4z8ij4-kbw5btk7PbdF3YRX8b4wSp0p_ybfdS3ayV4y5HQz00EGAJD5pHX24FMaFKEJd_qv8Kxqkxapy1SMjHqYj2VwOYuhMXzVUeDyHJ8uw84Pkh_BlHKAaTZgR_0b-BnOCKBO7L4fRhxmgJagwn7eFAIugzYK0mMKMQCc-H0aOVo7p5Z5Oc1zKgEbViuOKTz3aTwR98O5HR7SLa5oWkPTbyBUBbhakrcdxQvbZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=m4ZMadD-1kjwwDFtu6iqOXgqmDm7hqXR7enFVrO_Q4EO6x8szeJTUxHWQYXRNyk5d68QmxwttjbLdATowITusPdLyJRw_N9VPGJ2Yr430SinR4z8ij4-kbw5btk7PbdF3YRX8b4wSp0p_ybfdS3ayV4y5HQz00EGAJD5pHX24FMaFKEJd_qv8Kxqkxapy1SMjHqYj2VwOYuhMXzVUeDyHJ8uw84Pkh_BlHKAaTZgR_0b-BnOCKBO7L4fRhxmgJagwn7eFAIugzYK0mMKMQCc-H0aOVo7p5Z5Oc1zKgEbViuOKTz3aTwR98O5HR7SLa5oWkPTbyBUBbhakrcdxQvbZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnGMVbSm61suwzWvztA8xkb9UZAmbevGwixy8HxmgihbUalSZUIYEUu7_8QagyqtFozqK60GajQl29IH-NVo7-GJCh7SGhd2S2q5E0_xUu_flUHGSK8_bkbh12-7Gl_9LOuIKFPYYwQ5SS0b6kXYb0KzhhouXGDGbZKZOezGoEVHAtdxiqTKQ7Bf4KrL5Yep8bzLPjDEw7hJQJK6coYQFsOO0Wr_GIeThEIavNGdbXJZWQSG0XijftSjZTmPXBV4xrb4BeonE8hUGoNNvFouSzfPuCPkAEbqWN-3b73Tem_6WRZ7gsGSPOxIq3WrFgYJ3jq-mDcb0B-ziDEyYTxavg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCzwanwE3FBm_uj3gtucpyNlSjAZZw4h1Ov5h_-YE0nTFPTIxRXkP5m6Es4PPEEObA2LPgV9Zknz4uQxxxrEGjjnjBinyOKBiLEm-I2DBGOvOsJziXGPBEi3D7hm567uZRugC_f7iYAZrNzO-n9llbd9RARnrhdCwir32P0q0lIKLRXnbSAm2BkRu0X-ny6nHdRKxgFOB5ePGbUgVMqykrBoWnaTnIIPL1UtLOo_7kHJiL2OwjmUFpXtUl5ohRnWtax3vY2gnKW9tgSIF-YHLCbAfbgtayjulo4lIpOk4lvvenYUq6uw5Eht6F0VfNzv9LNOL11pu1bzUFWzo4UNVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewGZHoz265X__eD6yrc2Jg2mNbTuxQckVfQ2XTT2EsiQmwrFkle5a_AdFnTY2gbf0tKBoI2xjHMOb01vulk4GI2p-mzlC8RsraWborXAzI_Wj69q8QMo2s6bNqETj0rRKupIJ3fy9oNtxTehcQ79o28c13CWAkyNIadOEKtmtD7hKN6M2FQfUThUTwGPE3SJg1z9G1aI-LIiRGu97RVKBMrJkaJUDr2k9XTdeJRO3LYwppCdC4GNE4X1-W25wJPDi-wsbi0_dIQIB3ZJfeTIfrnxsns91Qo2IR180IWmp3A1khGBLjwEKjYOQihCqK0G9MHxK1RT7fDkMZSqqbMCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-CAKKVwsbJZO3rjlTGb2m8ffBrmHY7YR1kcllkHUEhQQU_46rBQFtkFjdeB0Fpe_CPfrK_LptJFipS6K9Liizwxt0PVFZHPZXxwVPcI4mD_hqow9GmXCWRJfE56NfGf9T9g6BpKra0j-YqX26nh6r7aceN6dLfyhNAtFMCkleXtsucfyGvFQKQp_6GcylCSdwpR-Kb3I6HUrB7rfDJcxzLf9cfvK7RJaUjQhQlXpTx4HYs4JG-lOVyGC1tdjXP0TRZ5LRYbdf-yz5K1zU35KKlnpYdiKl-RcONuC1QfsQd_nA2gONIpVi9ACuVOlBge-91zLRGlrD16SfwG7Q37rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UABvy8cfUOqsyDmP1d1OlgRnLkYaXUv9tVp46_fyfOj7g-D741nqNjWJNCyt6_D-hvnfUWfG2QDlde28v8gOWthrJj9iJGbc0z9rBeViH39aP48OT6jk9P-dNq8lGvoBPHggR9P-745zTsRfurCHSTf_7ai3pMnNkoYT8R84KYtMNrogQGTXyeKBqeHm1wTRUtDt1Ito1h9sd3VL_u_Gxtr4EKx9k6rAY3HlMZVySr8D1MYP8yhVGvToRBLL8LzvVX7uB1aVDsfJDdNOKDf7yFhuji4T7NvwW1yrCpRXqRAnKrPfIDwjAq0iABYkX7lHbe8Ac2su46Mdb8yN-RIB3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUuIXq_qf5SyBCf2j0W9MYEe8F1WnHN9LxPZoxfgF_sUQzRo9BLFBnwXwIcRzAK1ltZIkeTmYMRFSVqEZZt0xh6G-1gq54MRtLlcW_dP7r-sGzSW3MqbZFCR3fvn1VWLWfHRE1b-jmwb_PrdiuB4prQac4ZvCqJ8g1szL9XQGvNEvoDddoySbrgj5SLmy7_n0gSFZBvc1P3IGSF5SVVb1nhRp89QkZbk1hYABlfKznwnshqgZxPFkL2_VZeWAtBTYC9lCBvjtYw4APJwZDX5Bx07CVtt-invJtgYoP8kMpryN5Fv18FwaowDLkp6-5_M5ZC5o806JUvElLBAdTlqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWu9pwDOYr-HiZlLO-62cYvBUFBilxLpgZRbdppyum0ZOsBmTq_dldOneuyXf4p4TcJuC4zVBnrIp_8DPwvl_zqywRJDOYsStkpCPo2cTUL2Hb-PA2-fLWtaMrItcy5pT7zc2vZsrFdd9UGKo0ohk2FqN0hWZvRTnizdbii9E64DqaO1_uYOWjJS3x25NyZubVSZ1eUs_5R0Ahy5dOZH0mlJ7rMKzd2X5K9k21pWl8Tbx8wCQFoI6Fy4xk7rDOlmZHN1KM3ewR_GqRjzorT-4JJA0qPkjWn3RgcF_O8_LLxlEeKqM5-RPc5NYoc67qSLm5ppuHZONQ9SeYmHcpTcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh7ZuevdbI_ZCS5TqfN-iKsuJEQepLQabz390wTEi8s_gjS9vOl7IIC18NS9FzpkHkJy-OBDOVHZl6jAHYPnVMUsrQ1h4tLX8b7LnOoTq6wmcrMFBlwt-5GHZThJTtqUq_I549c1jwr2Czk_HyFQ5Uurm35FLkTmzZEoLmcgIbIwB41auxD9Qddzqg2BzVoPHZx14kEvfs1FOFUN6tEgQd1Jhb_7HtHO8nZGCnAE9_-da_gbjQi-YNvV6kovq8VYiS8qceKjm-kzx-owA3jWiyfHXEHPiqqIRuMBHNPUyJxobuFrSI8HGHqDvI5OPDMnDm8fhHELivcRXX2520lL2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thGhdwfGtQphWRAtBCD6Opm_6vQ1BdRAkNULGk1qnb6jger5dswVucCjWDe51Fyv3vObWwXHXsf78yj9uBE7tc1_yqYFr_oLJG7bpY_KTwP2ff8RaGZ3D_rkfqyasdj8uJKt2EbjyVQeOd2XOfpMZxzk818cgxzhamzMmOfYGy1ze31tQgLU-6E1mS-qOiG7iIcTWMuX48xTRRWR-ruj_HLI4G7PTQtEKqCntw2_16tgeTsITvtiLX36c9J09Itp-y3nEQFGG12EKZtabphm9mgse8eXW0JYBREwm-k8ZdrLc9c-lV63fBTAk-w944k6VwKBMw4FFDoSjVRd9Q57fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-GPQ8e1V7eTv8bAv8X6lWlT4qzKIjfTvPmdyqeJSrM3Wc6cbfmhzWHo9oHlUhbqZRG60QXE8qiQD5mOWwb_FK2EODLMi9KQkKKLNHzML1AtsAMKZEAVGctdR3tB2JDMVAtUa1kyRvXD5F5QBDTV-knwswA6sISBJNpzm4bt6MFiR-lf37lGoPqU2I1IIICdUBr7irIokpAGf9-hCc_63Y_0fkonm-eKFdCqNmcW6wE3EdFE2KYO0ni9fjk5RcZn91gfoH2PcIHQTQ3qFZ2ZFBcwE9jqmAG22xDqir9BCgcVZkfT6LeGIangdnIeiz7P6dSHm6vARFwSyKUxw6GuFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=YjXIcHzcXTAuWZhEaPePtWjMgHcKmbXfRBf4_vvrN0ngJKxVnQgt2yEm4le3qFTkXLOOjcK0t-RY0RzV80TAVg3__46banq2O2BMSQFMQFmtD4v5ntRD39HjlCgDaWfY30V714jMMwCJ3T3pUbYrlA4lMNSheJ6l7ALp6TxNn9nnhP4y4X-vM03EFFqyuzs6Fl07nBAvY3KNMOMd2P0UL9wg-I_R6KdCjbqemaU1o7HRk_d4TZUVwqoL91ilyI8vEcfmDs3RpsAs8pgxHRbCekyT5r4MjOqwOKeTR0ZIoitjWHUbrLOJ5APSnog1gzW8IcQg2-OGAwt7GrMi5eM5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=YjXIcHzcXTAuWZhEaPePtWjMgHcKmbXfRBf4_vvrN0ngJKxVnQgt2yEm4le3qFTkXLOOjcK0t-RY0RzV80TAVg3__46banq2O2BMSQFMQFmtD4v5ntRD39HjlCgDaWfY30V714jMMwCJ3T3pUbYrlA4lMNSheJ6l7ALp6TxNn9nnhP4y4X-vM03EFFqyuzs6Fl07nBAvY3KNMOMd2P0UL9wg-I_R6KdCjbqemaU1o7HRk_d4TZUVwqoL91ilyI8vEcfmDs3RpsAs8pgxHRbCekyT5r4MjOqwOKeTR0ZIoitjWHUbrLOJ5APSnog1gzW8IcQg2-OGAwt7GrMi5eM5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK8oUzRVqLdirtn15Kc1Ll25vK4CFl_bzNc1_f6PGV-Dnckl0ljMXX2ixuoLBj8vYby4pLlxer3LnQLdq7jLtPtqGLlaEPcFBihf8wOCzlvQhOKztBjQeplci7UBlmyWW0EwR7T5Qk-uSQvws2KyFyVr9zr7pvgNnD9Jxa_Wh8pdCpP7Zan3QCOcp7fzp3WqS5ydUHFvbis7uSPEj2cdDFdnGN4r6KFZNBpwcz-dnZl2X-OJ-EfNOX_WfC4A79yddkGRxgNoD4QBWRZlIj7w8h7hdaGpzU8Wwwt_4lZkvqq6oYeE6etMEr0bB__ZrKfik2lQ-OgewZV9UuuCup9E3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1McTXhmZIHhjKk4CZ_VT7ICaGy_65o6F5mUZETxb-SSwvTHgEsIAtSkMQ9KNf3PvnzcbJtdws7m_g76DHUMAFkfMnfWpLWFzUQDX_6hkO_Y3nwDpdB0EgkoHnJCQcbkODy4km1eqYiyFV9wHP3q5nozOP_VdGHxHwcU3pooQSoWfb8ddDNdW_DKwf6-g2j9WPpgllXdHe1wJyVztwnaI4V4Ubn-nNG9GjnaWEt1QN1impcYjfY8AqXuDDzrJJNPEyLGvdHv7bYbAVWxsiHNxby24TC_O6G5seZz-oDsgm0MDq6D6PHxcvBSTfdjV2246GiUntrnaGKYbTK8o7XWuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Gwkw3L8qzsp9OpcAsK8T-S9QJeJI1HIoe4JZEtzd_O9hNkj_aThj9-rwrkwfCHwfh63NEJZd0Z6njAcSR7HCubNxkCyc8k8QzrcltgxtnWDdX0DcDavyeGQmaxt3H4lXH6K7SXxbV4b8CjF4bnFXoekTquOsoddz7-qkUZW78Dvbqa6lMqS2p8r7UeNtKKOKeM660qWPf4bV9_kbJerS47QuyBVrp5pAHZ38PD4el5eaorMSxhBcT5P137UPDHdKq6EgWl6kh-KTG4nfk12bUgEhgSoCAjRzdHw4-qyTWy_4wmF5sn8YHU-PHfzQbNLG8-oSW186cD_G9lDiXGViFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=Gwkw3L8qzsp9OpcAsK8T-S9QJeJI1HIoe4JZEtzd_O9hNkj_aThj9-rwrkwfCHwfh63NEJZd0Z6njAcSR7HCubNxkCyc8k8QzrcltgxtnWDdX0DcDavyeGQmaxt3H4lXH6K7SXxbV4b8CjF4bnFXoekTquOsoddz7-qkUZW78Dvbqa6lMqS2p8r7UeNtKKOKeM660qWPf4bV9_kbJerS47QuyBVrp5pAHZ38PD4el5eaorMSxhBcT5P137UPDHdKq6EgWl6kh-KTG4nfk12bUgEhgSoCAjRzdHw4-qyTWy_4wmF5sn8YHU-PHfzQbNLG8-oSW186cD_G9lDiXGViFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqy2PjNjYU0Q4IPED5MbkHgi1UQ4bcR3-oNZIq0Ujv45E2hJaEBWTEOyIaEA-29SEm7ZPv0SWAUfkqvVCmKqF_JmN8kheNjGIbZfzcD2MTo-GX9VGHj2A2h6YV35Oo-Vo_fwBCKClvFgA5idwK7gBc2Gq6RqSkIfDIEE3YQ6kx6N1_ifIYxGVDSuD4VfznQcVctif313Q9dx2lZBID9Ih9S8CtgudrV9rAJU1ZigCspktDNvwwdIeZP_idJ7igO2Jaq92TWbjiJQA1xW9lVgS5EBKs2nB8j4m0ySxcwoKEJNgcsWHcR8SYxqoWdnCA4S_TxyWXq9d4s5zWt4HUE_-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbF_wojsE3HvoiJsArI0dKz864jDC2X1z2V8fP7wuJlkOF6DT-U6Vz5natss02XOifrvTe3k08-dT5bBIjBGWygoQLelaGZCJZC7vwT4K-vIb3HAxjPUb7tTPewH_m9sqAIMY3GdnC5V7iZb2_YdvEchL7rbvH4TvPxWDMShC2sZEWtLimZKrHSoVsnNIG97M-47VeyEaxii88g20aN3dRnMycjeQCdgenqdCxa-q_L1ELLprOS45EOkaokUUtOhe0C0yh4xElnYakPqrOVg98ED7oAa8ufS02F8i_rTBQ6MEewL11dBFmm3hq4AxURZinQ9pDdYPg0IiwxnoO7HpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=oCxSonkOZ0MX4p_vjFX1pO6lf_HINwN1HOY2eiE-gxXogYh4qPcISICco8XMSF7fa1aa0bjTmY0AoITIh-azjLu-5kr835eDEe3-JzqxjrgAXtP_a7D3sViXOtejdTJEso4R8hmF477XiD2bmJN8wHKVPcwRhrfMhtN_wrduUVesTjjxyxUlqyf63ogDsRxeJK0fP5xUhHELEBPlksDTixsSzdhKP_94jHQ-DWtkIu74nBv5XV3Ycs5QgpzmDE4InMWPeqRVxgdf4bxdLcn-yq7XJdTxHxnhNj_IZ6h8G-QrcfU4JA4KeKzepKb0VS7hXs9bUmZi8byKGZHH9JDyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=oCxSonkOZ0MX4p_vjFX1pO6lf_HINwN1HOY2eiE-gxXogYh4qPcISICco8XMSF7fa1aa0bjTmY0AoITIh-azjLu-5kr835eDEe3-JzqxjrgAXtP_a7D3sViXOtejdTJEso4R8hmF477XiD2bmJN8wHKVPcwRhrfMhtN_wrduUVesTjjxyxUlqyf63ogDsRxeJK0fP5xUhHELEBPlksDTixsSzdhKP_94jHQ-DWtkIu74nBv5XV3Ycs5QgpzmDE4InMWPeqRVxgdf4bxdLcn-yq7XJdTxHxnhNj_IZ6h8G-QrcfU4JA4KeKzepKb0VS7hXs9bUmZi8byKGZHH9JDyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgq-2C8TeHMRelznqvppP71Ke2joL8RdEYBkB-GGlCltcxY0nCyW9XtFghogpwv3OhdGYULjC8tRv6iS63q9dVez1993IYKG1l7v4D6raDq-6QuhYU1kyxx0wOPiIUWltWByb_7iuPRebWNqQxPG3c6hNxdp45XPg57DkQEc_do7Q1BG76Eyf_-2ZXiMRJrs4YA0ZLd0PTftVpvAxewvVdcG4nP1CAbYT2BtgibbbMBwln5x-6UNBXwTWRKocPpiRBOBszVs19Ril3h5inv71lDP0azccbDrlMv0eSgmEps37n6X0zL8_btfuZN17yA6Ewd36WQGiQejD2pnhRw6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpPq2jJp5jWh8AHIu8G3uTTv9EnnJvrpXidVSjj96DB4gNOywn0n7YfYUIfPuPgPytSkFvOV9wglLGSsZl-0MlC3Oc68qB2CA288OHXf_hiMBHYsrm31wPlInNnaKl3_eNl2BQF3Xz_rJDoZUESSUfRhlFbcwzHfPIlpqDeojAVzciuz7EdwU4jfbAnsqWMacryGxEwH-UprPyyJqklrv_uaKQzzkd2vmHVT4rKem3T0aOrc8Yrf-ddhyHPbvStWBxPkycAJczVqy4QBKCaFJgL2l2jYvXAUM9XfLtaoCeQPlHQ4xeODSSVpz84bpsu4FGKEC6KiR64L6IwZlUrYIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=S7CiAb_HEzxD__AaMFi2YoUdJyM1W0IMHMFBNLVYhiVyDlEyRPfPOs51MqW2l00FEDotV6-xqXXWqWpns6_p2COmMJAG4U6di4Ku6GGaoCq1GQDd2l0Fjo_8v2e3fC_NZwY57PhzRfLkjT1K4V6QxUx573G38RgNmHWPh_gX5yjaZ8VKm1tWZHs7ix7TzHHHQ1hnB09BnLfoqk8Jrsi2cmCGewyXGv7rzRhLSBe-O303SCfFnJBBV2462ETZQxZc82khZBjCs4XTRPjmH0NVowsh6VlqqVGAjhh73zX4cmKF6dLjbW7kzgq9Z2XFpMcYrHVe9HycU86PI5RJzngZDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=S7CiAb_HEzxD__AaMFi2YoUdJyM1W0IMHMFBNLVYhiVyDlEyRPfPOs51MqW2l00FEDotV6-xqXXWqWpns6_p2COmMJAG4U6di4Ku6GGaoCq1GQDd2l0Fjo_8v2e3fC_NZwY57PhzRfLkjT1K4V6QxUx573G38RgNmHWPh_gX5yjaZ8VKm1tWZHs7ix7TzHHHQ1hnB09BnLfoqk8Jrsi2cmCGewyXGv7rzRhLSBe-O303SCfFnJBBV2462ETZQxZc82khZBjCs4XTRPjmH0NVowsh6VlqqVGAjhh73zX4cmKF6dLjbW7kzgq9Z2XFpMcYrHVe9HycU86PI5RJzngZDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3KivRsUnel1FV_aax_8-ggvquysYhDu7o_TStAzu-Lo4uQDEIaVljQPBY1mfGzIWJ8offsTea4CBzkPvTeUzQwZh13Y5A7H7gwxTuynf1dzpj3ENG3Ksn8XZ7f9QKvEvPZjAcqG0_uS2GfCjJ1Q34WPqlb0uXhdHpabFmeBYbbYpeyyOl2Dpe5XTrd1hGcn2LAuTWCdqhWwdtL-tAXEOF3_P2tJkedFl_cwhi2mB2i-df2wV2Ih23b2aBXd5wN6cZgsQhJujWpJTYy8-X0bHYwmz8X27I7yxbj4rBKMCXKc656hiSX27TB0HwfkQwKafaJbqTJasrE4B9f5boObqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حالا چرا قرآن اصرار داره که بنی‌اسرائیل با جنگ وارد سرزمین مقدس بشه؟  خود قرآن هیچ جا به صراحت نگفته.  اساسا داستان‌های توراتی - انجیلی رو قرآن عموما اشاره وار گفته،  چون مسلمانان از طریق تورات و انجیل با داستان‌ها آشنا بودند.  شبه‌جزیره عربستان پر بود از…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5433" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">میزان درگیری میان خدا و موسی از یک طرف و قوم بنی‌اسرائیل از طرف دیگه بر سر اینکه حاضر نیستند با جنگ و….. وارد «سرزمین مقدس» وعده داده شده، بشن،  تا اونجایی بالا میگیره که در آیه ۲۶  خدا بهشون میگه حالا که نمیرید مبارزه کنید تا ۴۰ سال بهتون اجازه نمیدم که وارد…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5432" target="_blank">📅 09:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBILEEwQuhd9d71LMoWTJU24Y2JifIuFgd0Z1vO3L2OohBlFYv97Pg0hA3ELP6hdEvHjZUmEy8SvI1XJzIJorlYSytPjNBbQR8mA_pqjzOrhNxk6t7KHMjne8-RPwznm-SYAZcSaD7bAl4yK4zSYmELjTETYjeyZbJ6fg8YPW1lvmG7B5RYeq6JiWbN6NCddB36Bk74sXoDjsdsEcASwKoHau0bER7I05KcLxB4L8IXi0klRVUdCOM1r3olsLwjhCmlOESEFsBkpJ9q-n99OdxCRp4tKFOElvORiNumRASLl_uwfcjocOISzWRa1lQ78vXkIHq3HmAqGCkfcg_jv7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5431" target="_blank">📅 09:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuKgKkKspaRJY8Dt0ZVq3kTMLZ99rj5czq6e16O53uR2MIuTO7lO4SvM15jrvl_roGfy93F8HsuShLaTSLt7-MVP8rcCHdG1pfNQJiQkMEI-5dd-4tt7RxU7yroBI3qq9Zljqxrv_rMJ8FTgvS3_bt2WyllLR9oIcLD9sPKIz8x8ixXKqwaF2dQFMJJzO_YHWNTXFXlWjk2pCf8cm-F2W7jMjYfviNvohBHKY5xOn64yj_xEZL-Qxo96b7_Tw2VPks69e3mK4bSXhD8sY49LwifDhdPbZADzOEPgG9Z8mgDbrrsSkSd5r7m2fFpVS6TJksy8oHWNawOAM6-147KpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین آیه ۲۱ سوره مائده موسی به قوم بنی‌اسرائیل چی میگه؟  «کتب الله لکم»!  خداوند برای شما مقرر کرده!  نوشته! سند زده!  و میگه برید و از اونجا هم بیرون نزنید!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5430" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5429" target="_blank">📅 09:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5427">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5D2RB9jdyZyynw2wRCrPpq5_G7EVujItYuQOJOyruz5NJYAKEWdbQ8ULyoqrDhb068vVZO2zuAeU1LzsnYWfiuxL7m0_gzAmI3FzyKZ1Cxy_qVazbAaKeDvbOs8MygzILO0w-vKv8lWS4WPRjz6CGkCTlanRAuq_GXNA2wI-ca50rctsdCTzC9lXD47z1hFM3aers7YOw07ffc7OK28PDIoY48zVKc34nHYyBn10BAQnFL4WkCjQTtPx-G6CFIALI136w1-OTJShjneKqHNp0VLXkJTq8I6MnT4g07e0-UKbO9RB56w9v5yq8XkKsWNdb-nY7uT2N5V0XX9nP-O_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mxbkQhIB30gS6njgCdlvsASCpi-Noco-zEKVJpwydkNJm4Fp_ysYh-udbUWW1ZwfKvyMMNTnBbKUGslBM7sbZ-1Pz-u-jhAhhD9Ytn_C95S_rpOknP1zA9zS9XMnE_x2S8tJnVBPp4uOQtluvA4snlQziZ0vMt0UCmWIrPPNiXZdNYUrkkWqh3RgG0LDq998SCPFn_DTCqFYzXCcYbTGBx7ZCF45xYe3xZBoqCE7eF9MtxjOXX2CfI_712tlFsAwtYbXtdLUUOt0gtcoy10L_RmPXukp0WsS97_WCAVZ7aExT3e8gXEucYazuhbM7DyjWFxAAluxklMuw-Me9-h8WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در قرآن در آیه ۲۱ سوره مائده
موسی خطاب به قوم بنی‌‌اسرائیل میگه :
ای قوم! وارد سرزمین مقدس (کنعان - فلسطین) بشید و عقب گرد نکنید که زیانکار خواهید شد!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5427" target="_blank">📅 09:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
حمله پهپادی حزب الله لبنان به شمال اسرائیل.
🚨
حملات پهپادی حوثی‌ها به جنوب اسرائیل (ایلات)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5426" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl37g190-sSH5jZc6jiJ-ZAlFvMZx0PAaT_fE0WorjjVMW528g2wTEkhjt8SWwXUNpw-nyy0ltsLl9aV1tXPIZAiiTS2nN4dtWgiGmAfNxxl9Cy-W6OtZeUtB8m92Rm3vjcUeFLJoRd4r4RE2U7WvX6jJDhe0AzptcrG68wlXtRRoCNiNHoqc1BQnVysUGISLe9oG2hBt6qKSao1uO3Fc12M081q2QQl3coXUvvvmrMlbnxxtpF4PlLVfWVsHGloI6dNsbO0xeKbtlhe3jbIpXlRdrQVyZ3J6xSZEDTXnH5Nd4Tkeod5WL2SOzxXiNHkFUFeMQ7-hHXQUsSwYjJoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5425" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWCn7k9xY3rJiPFLgbuopN4u8--oKzEvv6LaVkc4XLLNmWMpy7hQfV5cuUYJJGKclZ06DzEURjvAePl2XSidfbeytlQqlFkJKYi1WeCCp7XEhIvJl3t3QSyHfSixSVnpJfNHzcD4Qv8cOA85OdZwdW-HlZ2wbrGeHZaBWSMtORF6aQstNkSp6pY0vtfnKNwkEwBGel_Dmy54Xp2ywLxJK2DyevzSzf1IKYVfOyb0DnxGJFWwcL2BzxMbfPmMoC4PzMuuCROpak_93SaoBzSSi2LLFhFzLB7Glgv-k_DPkbveJjNyZvoh1DR-89A1xvabNvDyNlaRJJ84BgULEr315g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ۱۲ روزه ، ۲۳ خرداد شروع شد
و دیگه داره یکساله میشه
یکسال اولش که با شکست دشمن همراه بود
ببینیم بقیه‌اش چی میشه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5424" target="_blank">📅 22:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏قالیباف:« آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
آمریکا دنبال آتش‌بس است ‌‌و نه گفتگو.»
پس : میشه نتیجه گرفت که جمهوری اسلامی برای خروج از محاصره دریایی در چند روز آینده دست به اقدامی بزنه.
گرچه حملات امروز عصر اسرائیل به لبنان نشون داد حملات دیشب ج‌ا هم نتونست وضعیت رو در لبنان عوض کنه، فقط یک پتروشیمی رو در ماهشهر از کار انداخت!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5423" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0AvIQ3__zaeqIXsVdSHy4Chu3L_dtfghgGh7-ddgpfP1YrhpCRI3czRSllIKFq3l0DZPG01qV_vweGPJlCOMfA44D-hjsj4IaNlbHD0HJZJMc93KzCFhzAcjorfKpT8Cq6SFwPUr1NzcB45LkaM0VHsCuDGWuBz36N6sTc8D2xJy7OkXjgEZVdnMu189DY18g_0Q6EnRcVAqizL7ON952X9fbkvC-zgzTdj2wnJuoBd-sGM1eOxb-XdP285POVQ1yysjq9YC1wxZlwfRQFL0k0KPdyZd2StONttVQANsutbEQ_AzH-QpJxgr7VEdz8zqOPd-oxATmej_yWIWwO6gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی حدود ۶۰ روزه که نمی‌تونه نفت بفروشه و  زیر فشار بسیار سنگینه
دولت ترامپ اما همزمان به اشکال مختلف اجازه نمیده قیمت نفت در بازار جهانی بسیار بالا بره.
امروز با وقوع جنگ نفت به ۹۵ دلار رسید که با مداخلات ترامپ به پایان رسید و نفت به ۹۱ دلار برگشت. که میانگین قیمت این سه چهار هفته اخیره.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5422" target="_blank">📅 20:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=Ss3jrxhvdSQyVIhGLwgp_cK9AC9kI-NEWwrUjwyz7EdCJKVmyILBbp0lWGgRWQ2Iw4AjziV6TszZ_PiHzXoG0vvkBYjoWQzBKDm35gwzSg_ALPjivvjREZAEvsGKavDFypx1uSrAXDFG7oQuVBcx09OBRXpMTjHCBxGVsjJAhp48b8DL9K4E0L_JU-xm2JlVgBivFs7zcxPJvAx3y9Adl7Ea9ockWYtWz85FPbMZK61AX0cUe8jlbjfvYO9B5MrQCxoDGJwnvTMnSGZFDWif3Y0HyRctdA2dh7vxAELID2EraKKxoNzR_kvQHu6sovb36CqIf8HcF6CWh9bjCy0CzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3dcbb79c.mp4?token=Ss3jrxhvdSQyVIhGLwgp_cK9AC9kI-NEWwrUjwyz7EdCJKVmyILBbp0lWGgRWQ2Iw4AjziV6TszZ_PiHzXoG0vvkBYjoWQzBKDm35gwzSg_ALPjivvjREZAEvsGKavDFypx1uSrAXDFG7oQuVBcx09OBRXpMTjHCBxGVsjJAhp48b8DL9K4E0L_JU-xm2JlVgBivFs7zcxPJvAx3y9Adl7Ea9ockWYtWz85FPbMZK61AX0cUe8jlbjfvYO9B5MrQCxoDGJwnvTMnSGZFDWif3Y0HyRctdA2dh7vxAELID2EraKKxoNzR_kvQHu6sovb36CqIf8HcF6CWh9bjCy0CzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏نتانیاهو: در ۲۴ ساعت گذشته، ایران و حزب‌الله سعی کردند معادله جدیدی را به ما تحمیل کنند.
این معادله غیرقابل پذیرش است.
قاطعانه حق خود را برای پاسخ حملات محفوظ می‌داریک.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5420" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXRZpsmhMQjkPykVnM795i0PK3kwCCkw2o6rYCtHhgNppUxsdW-_6AcnKU3v2n3Th_6Zhtt-OjpSR8yNr9In3x-XuBNaCWl32CXRwtsn14_C-421eKKAwWDQYEQmlSR9nCqcTnOH6uYsRWJrNk9Fdo_YoWetQ8tFzzNYBhQVZKIrExHHRE3bwnMms73tRPFhUYylztng0C3lNrWwP2NiHks7oGR7Uf4Voyiv9K603JIZhaleh6VEbN0cI7gYIM-Fdab8et7shG-lRoDSaWEVwKk9hT8tHGku2kD724IOZ5wphLS54bUF3Y_xOMdcwlhfACTasWfBd1-6z9tVeztYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5419" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5418">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=avsHn0zk4RDiIs4tLqmSc-edi7WzDduNRt3DDnXDFFuuP9lH9MCzOBrOqsnGlwDmHIkMEBB18MFDNxQhXZTy797BjQbP3vRW3_VBU4QDQnAGKtN4SAnbOt5qtYcKfsr0zQiOojEnlx36UBZQVCkM5QkQb6edA5jTx47yxYnokxnZRXYvnup6Q91mb7LCw13XjpNzKsp_d15ChUWWg9CXsjw74J8q3bc8JoyOQnEyHq6mMOb-im_AUbgqPLh7m_0ZoFO3D_GTY8C4D2ojL_wUqeLDb2xQ2FyWWyzkvitHK_l7_6E2wC9RZjKXJW8hlb_OW6Nh9ViXJUOnFkuCGmG51g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e85051dba.mp4?token=avsHn0zk4RDiIs4tLqmSc-edi7WzDduNRt3DDnXDFFuuP9lH9MCzOBrOqsnGlwDmHIkMEBB18MFDNxQhXZTy797BjQbP3vRW3_VBU4QDQnAGKtN4SAnbOt5qtYcKfsr0zQiOojEnlx36UBZQVCkM5QkQb6edA5jTx47yxYnokxnZRXYvnup6Q91mb7LCw13XjpNzKsp_d15ChUWWg9CXsjw74J8q3bc8JoyOQnEyHq6mMOb-im_AUbgqPLh7m_0ZoFO3D_GTY8C4D2ojL_wUqeLDb2xQ2FyWWyzkvitHK_l7_6E2wC9RZjKXJW8hlb_OW6Nh9ViXJUOnFkuCGmG51g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ : همین الان زنگ میزنم به نتانیاهو تا بهش بگم که به حملات جمهوری اسلامی پاسخی نده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5418" target="_blank">📅 16:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=T9VQxL4FtpnmZyFvJiV9y4pp9q9uYyytf0YLWw6OPmMm5sMwSea9TJQDSw_1GRaNishxbP3418aNtqa2iPj4SxlU2nj5r-nn5nXlZopR6hPRpMwNn63Iq5YKmuDWF5Zs7KU7H5S3LYeaFzRMTgdrcq4oD6nqlCQPxoP0OR7IdWrPm8kekXHpG1_TCqoV8iwEVhpUP6acFs6P1PDtKN8VkBgL9mE1yPaqV017fBgxp4URArW6tJJ2j9xIantqI5vnsD8mVqi0-9H7m-GNlIsQ_uyFjz0Z_0C0tcSOKEzGjXNPWxB01pbiNGnc_ex2lTqf1tUPW-QszpDdI5HLG9AwvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6629addd3b.mp4?token=T9VQxL4FtpnmZyFvJiV9y4pp9q9uYyytf0YLWw6OPmMm5sMwSea9TJQDSw_1GRaNishxbP3418aNtqa2iPj4SxlU2nj5r-nn5nXlZopR6hPRpMwNn63Iq5YKmuDWF5Zs7KU7H5S3LYeaFzRMTgdrcq4oD6nqlCQPxoP0OR7IdWrPm8kekXHpG1_TCqoV8iwEVhpUP6acFs6P1PDtKN8VkBgL9mE1yPaqV017fBgxp4URArW6tJJ2j9xIantqI5vnsD8mVqi0-9H7m-GNlIsQ_uyFjz0Z_0C0tcSOKEzGjXNPWxB01pbiNGnc_ex2lTqf1tUPW-QszpDdI5HLG9AwvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید
این ویدئو رو خودشون پخش کردن !
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5417" target="_blank">📅 16:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5416">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اورژانس : ۱۴ نفر در حملات اسرائیل به ماهشهر زخمی شدند.
لغو تمام پروازها در سراسر کشور تا اطلاع ثانوی</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5416" target="_blank">📅 16:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5415">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=XvJI5b5fNLdmExz9TvvxwvHplIo778yrMfi_8363o_lYB9KQ0H8dYiK80jjKYHa0913w6lilkysDtmzeeBWV_CZBlboGh7zqBinrcfe-aoHYKhvo7T4_OLgMzUPZ81l6ZwvPtAA_AzEyklXDVRMgTyGpq8Fapj_P2-x8HMDk4iE3smW1K4-smHHYy0bSH9iEpsDiip-2MZhKECMO9IP-oOW0TOeilDmeoiNLsjN2-hUSL7Kyg720joi6yxlYnYGP5jrUTf244im71AysGgntDzw3osRTZp_42a9_MJqexw1LFVslVKtZHtUYkYly6h5frGS81xH51LHNXaKvzCb7lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee24d14acc.mp4?token=XvJI5b5fNLdmExz9TvvxwvHplIo778yrMfi_8363o_lYB9KQ0H8dYiK80jjKYHa0913w6lilkysDtmzeeBWV_CZBlboGh7zqBinrcfe-aoHYKhvo7T4_OLgMzUPZ81l6ZwvPtAA_AzEyklXDVRMgTyGpq8Fapj_P2-x8HMDk4iE3smW1K4-smHHYy0bSH9iEpsDiip-2MZhKECMO9IP-oOW0TOeilDmeoiNLsjN2-hUSL7Kyg720joi6yxlYnYGP5jrUTf244im71AysGgntDzw3osRTZp_42a9_MJqexw1LFVslVKtZHtUYkYly6h5frGS81xH51LHNXaKvzCb7lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در حال بمباران جنوب لبنان
- برج الشمالی - حومه صور</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5415" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OZmOhCODxSvLL3N5LsRBzNiXUFnAuh8cydxPKH78YGQsoH5fK-mFRYz6iZ4u_SpPf9Ub5_vfPTkb6k1kkk9APJB9-y6M5tHqNV0qEdyTJjdoH1JhwA7BesG5jcGlv1z3Repgt2JKxnzFI48vRpoizOwGWj5iGcqX8LFkcg3Jw7zcMD_iFxdwO_SK62-BTEuEl0fXL2gJt9_ahnP9H24-WDaGmGcNEGeYqJaVTi7BBigLlynh9KUt8AkkvvfHUfB1Plpfvnx9V0ovFTgJbgQ0tLIfhM-K_E-reCX0v624sEHR-DTtVjZqPlUEd7r_ubBBw4CdZcaKnthPHvFQFUIR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xy8GUeFYDy-ma6m2KoM9dv77k58FLwu4csoVqSnHMoOPgShlnA4Ph6JZd3d2vFgmeVsZQne5jldsPs3l3G1hh94JlM3MThzKVjqikujefg59GSRskOp-1IlZKnKCdgRi2vZieHsurmDlE44UBPK0MGQBTYORRwT2sNkmjFeMQ3vRFSR73Iu4YZImPi7AFcDW55NyEq1VMs4Oi846IRj3bJz29ruQfqwdRgx2pnhP-ELDWDYUu_FOWO-OaBmQ4WC-ltG9HX4weOuH3QWK2UvanYo5hw2hKPfcEPupw3fuGGfYMy5Ol9ZCUCD-G-UQSgYjjCopwQJqBncUuIkVnWHrrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسرائیل، دیگه به «جنوب لبنان» و به «ضاحیه» حمله نکنه،  یعنی موفق شده معادله‌ای تازه رو ایجاد کنه.  جمهوری اسلامی هم گفته اگه اسرائیل به جنوب لبنان و یا ضاحیه حمله کنه، سخت‌تر حمله میکنه.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5413" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:  «پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5412" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336071990a.mp4?token=CA92GkzW8FBaQPYrOZ5fNCZ7BQg4ZIgcvBqmsTsBtQvthILyRT4to5JIMpXOLNHGDgSrAn8fy1Q_9DmbSIFMD7ByXrHExUHEzBGztBq1vPFax2NUap8DprKKwur73lLijQoluNY0srSuovMq-XSWxOqKNww3G8qmn8DBq8fdRFVAfjj1xY7Wp-d3qAsdS39h4sJpn27MK0wGZR4wX8gUh9mSlWV_vVL82d37R89Fw43goQl7Zk7lWlyl8bZC2Eh6OVCUFELtrkAyrhuJC_6ITraQgjB3NBU2jmYW-2Fg6ARBqD7dceP1BvcOhcakbganWQUjuBTpbCm6nOOcz9hvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336071990a.mp4?token=CA92GkzW8FBaQPYrOZ5fNCZ7BQg4ZIgcvBqmsTsBtQvthILyRT4to5JIMpXOLNHGDgSrAn8fy1Q_9DmbSIFMD7ByXrHExUHEzBGztBq1vPFax2NUap8DprKKwur73lLijQoluNY0srSuovMq-XSWxOqKNww3G8qmn8DBq8fdRFVAfjj1xY7Wp-d3qAsdS39h4sJpn27MK0wGZR4wX8gUh9mSlWV_vVL82d37R89Fw43goQl7Zk7lWlyl8bZC2Eh6OVCUFELtrkAyrhuJC_6ITraQgjB3NBU2jmYW-2Fg6ARBqD7dceP1BvcOhcakbganWQUjuBTpbCm6nOOcz9hvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله به یکی از پدافندهای همایی غرب کشور توسط اسرائیل.
این انفجارهای پشت سر هم مربوط به موشک‌های این سامانه است که یکی پس از دیگری منفجر می‌شوند.
این سامانه پدافندی قرار بود از آسمان کشور دفاع کن (با شلیک موشک)
ولی اسرائیل بهش حمله کرد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5411" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپاه یکطرفه این آتش‌بس و توقف جنگ رو اعلام کرد. نه به درخواست کشور ثالثی، نه با رسیدن به هدفی و…
این می‌تونه ضعیف جمهوری اسلامی تلقی بشه.
احتمالا برخی‌ها در حکومت ترمز سپاه رو کشیدن</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5410" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
‏قرارگاه خاتم‌:
«پاسخی دردناک به اسرائیل داده شد و توقف عملیات اعلام می‌گردد! اما تاکید می‌شود که در صورت تداوم تجاوزات، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.»</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5409" target="_blank">📅 14:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=aemehLPLXRWZl6IVIFTyhFi0TBxQ5ojmcNw383AcKHfnUxjTocR6UflpsP_QY-qFlvpuQy3A-47A9sYqot5IleiCT9KDZUis9e10_ZlJvX9iS-GipjdHolvMCnemRHK4vYVwxh3vuQcn_6sWJwRSt0xbXvT_DXVns9_cukFt2drvqNRRVtGdL7CNNhpg6UG59ClJaeU6BF0mLQoziE2GEDNmAEmC7p5d0YHmogmE68VwMHtrxlrgFH_Ivbpdg7r56v2AO6orUzkH1rz7FulRG0Oef1TW_IkYFTjxayz4akA_L0lPcJduvRVTejE8NFrJfIlj_UbdfIgSC2E6Gh8Arw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7deb2f31d.mp4?token=aemehLPLXRWZl6IVIFTyhFi0TBxQ5ojmcNw383AcKHfnUxjTocR6UflpsP_QY-qFlvpuQy3A-47A9sYqot5IleiCT9KDZUis9e10_ZlJvX9iS-GipjdHolvMCnemRHK4vYVwxh3vuQcn_6sWJwRSt0xbXvT_DXVns9_cukFt2drvqNRRVtGdL7CNNhpg6UG59ClJaeU6BF0mLQoziE2GEDNmAEmC7p5d0YHmogmE68VwMHtrxlrgFH_Ivbpdg7r56v2AO6orUzkH1rz7FulRG0Oef1TW_IkYFTjxayz4akA_L0lPcJduvRVTejE8NFrJfIlj_UbdfIgSC2E6Gh8Arw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله به یک نفتکش هندی در سواحل عمان!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5408" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">چرا ترامپ چنین مواضعی میگیره؟
در پایان جنگ ۴۰ روزه، آمریکا دست به تحریم دریایی جمهوری اسلامی زد و مانع فروش نفت شد.  موضوعی که فشار سهمگین روی جمهوری اسلامی وارد کرده.
همزمان اسرائیل حملات خود در لبنان را افزایش داد و بخش بزرگی از مناطق شیعه‌نشین را گرفت و جمهوری اسلامی را تحت فشار سنگینی برای پاسخ دادن قرار داد.
این بار، حمله اسرائیل به جمهوری ضلع سوم فشار است!
ترامپ میخواد به جمهوری اسلامی بگه : اختیار اسرائیل چندان دست من نیست، اما اگه بیایی و با من توافق کنی، اون وقت جلوی اسرائیل رو هم میگیرم!  تحریم دریایی رو هم برمیدارم! فروش نفت هم آزاد میشه.
اما اگه قضایا بخواد بدتر پیش بره، خودم هم میام سراغت!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5407" target="_blank">📅 13:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5406">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNbr2oz73O2h5K-Z3Lbwvkc6idx2T5Cia-TDWvvm3ZSvOKrAO7zXm1LzYd_1CZv71N0Oek2XM5OspGUtdhB7L99osnArtzC3nRUhokYiTr53zMuawKHMwF67sjpIZfbLg_UhSA63ZY1sNucNJFvhDZO3eZcHxwzWmnF74mZJ_Ji9bQqsF09VWsfp0MMFdABcLNKWi04IdwATSwZp6mcyduDejjE9Y2lL9a7iRkOMfzKMKQmJITMUp0Z5tXabmECAGI8bYK27OkjuadgmxCekfSdeeXMhr_94EmF9mG4WP2SrKtEVe3Sj_qAKFbwwkRpqFm5gus3GUFwMXxE3ZKy49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5406" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=WuwlpnMJ65uuZQc5aHsm7ZfcaRY54sYDqxbkY2fvYk3ltmFxAzMaXENAOk28bD3X5KUQrfbWlOs8WO0wQgr5_0YVWbRXeKaKltintyaYf0pQj3GZCggB7PqfvMnZoe1p5ucHfbMOJNZfSFrY1Jz4FgkEoalvulr9fK4XkELSy2Ihzpt-P_jC4Cq5v3-irPV9ms5BgSNK6_psT2panUBDzMfgfiRzrWR6_HgYGSl3sPw041t9F6gH3CN7rCqBFbD8tl8amt-WgMS-1mNmjHee2POVw9OHTP-ig4wTj-QTWBDWQLWKXZGvEXMOWh7cf0SqoVBZzmUVS9sEbFoHZzlOyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7503cf1.mp4?token=WuwlpnMJ65uuZQc5aHsm7ZfcaRY54sYDqxbkY2fvYk3ltmFxAzMaXENAOk28bD3X5KUQrfbWlOs8WO0wQgr5_0YVWbRXeKaKltintyaYf0pQj3GZCggB7PqfvMnZoe1p5ucHfbMOJNZfSFrY1Jz4FgkEoalvulr9fK4XkELSy2Ihzpt-P_jC4Cq5v3-irPV9ms5BgSNK6_psT2panUBDzMfgfiRzrWR6_HgYGSl3sPw041t9F6gH3CN7rCqBFbD8tl8amt-WgMS-1mNmjHee2POVw9OHTP-ig4wTj-QTWBDWQLWKXZGvEXMOWh7cf0SqoVBZzmUVS9sEbFoHZzlOyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط یکی از موشک‌های جمهوری اسلامی حوالی شهر فلسطینی «اریحا»
دفعه قبل موشک به یک روستای فلسطینی  زدند و
۵ زن فلسطینی کشته شدند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5405" target="_blank">📅 13:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
در جریان حملات اسرائیل، حداقل به دو سایت پتروشیمی حمله شد که هر دو استراتژیک محسوب می‌شوند:
پتروشیمی کارون در ماهشهر و
پتروشیمی سلمان فارسی ماهشهر</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5404" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPVIra-ZeVQBSGumi6r4McaJu5-tIRQiBwwsxET0WLbjPr_zlfXmU5BoMm3SM8MwUiCQtN85VkQvbAJdrO6LnYV_DZcOYmnnuoGxd7COLT6xqFFj47vV3KUrz8MBLub58Aa47w7VIrf9bV91oXE_xr6VkpQs5L_Tg3N88ikExq3hl-SyZ2nFUy9I58THR3w_d2WQV72PAT7l-1dccnZYaUiTfO2UwxBiFwjUnCeSL16rS_P6r7HiNqHR9P29Z9_N0FdOURqE9bD4HaexVVXepECoy9zO89c3NIZ7Hmjn8YmMyhdK3S52BLuWW8YreTHaWPvlv51pJnFSF3xxgzckqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ : اسرائیل و ایران باید سریعا حملات خود را متوقف کنند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5403" target="_blank">📅 13:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">در جایی از داستان شاهنامه «ضحاک» ، که نماد پلیدی است و هر روز جوانان ایران را به قتل میرساند، برای فریب افکار عمومی دست به یک پروپاگاندای بزرگ میزنه.     دستور میده همه بزرگان ایران زمین متنی رو امضا کنن که بر اساس اون اعتراف کنند که ضحاک بهترین و عادل‌ترین…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5402" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XsBpLV0Gtl8cKA-qJPMVZI6Ok-2-1U70OurGG5W9ZgR9XLOPJ76IDuhKQirD4zYGUHHRj_ci8We2i1oueoWl_4XffxVV96zF5EwF1bY_knnu9taFZZVSPlNr94ZjIDaZwcUdDUZdwlITog8KecZpnrVctWH_11FXGdhBAV4TdNJcZpLg53mAE5ZXDSWReoSzWTuTDpCUUxH1x8y9JWTyfuNmeAJ6rBWXnjs_eyOnns0dUkngq3F_mOHfr9h_FpTtpiww8sf-IdlABHVuGC1ughZHxIxbBR-1XFLniXWB49_PsZhv5DFyKAaxoLE-KOTyNsKXu5ryb_ub199KmjTR1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5401" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
انفجار در غرب و جنوب تهران
🚨
انفجار در فرودگاه شیراز
🚨
انفجار در کرج</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5400" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc73pBd7Xw19SFbBlrYtxwWr_pqUmvBbJcdYnoTUOTmccw0z2ydPSKr6di4ZOgpI9ER4skpFv4ohNf4e9Mo-iRNGIC3GjEdG-keeHrF55OGmtw6ZVhPtLbubOP7-9jPiWVV0MvAS_QDlg_97bix0DFnJqClg6rJPIgFOoSgxI3Lq3FL6VrZGS-gsln-NmTeecyxSIo3FCIEtQSF3zo7oeW5jnshMGBaBPQXkTll8qq7xaTcSmuQ9fSgnVWQ9-I6Xn-qjc7OzdFY9p_OfijI8fhgHk3JAdpT79y6uC3mK5RiZzR0aN8uy7YAMRJBSfXm3-nY7YfqB_wE_PWx-l13VBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vij2gYvzaDZ391cogU8rrtfQdp-BDikQ4YCsZb0Aire5qpKrLsJlhRxWYwhmfXF5-8L_-7GmFZFKSPBkubTBan0-331ILjsSWh6aNPsuTMAzfqt569O0aRtprYlJZVEgQn4V9gPAkz-_7muAmxpY9UKaUHmsZiMn32QL5aCqXpQK_rRBW1gMuFF20kb0tE12mNdjWDY4EoHRZNMaRYjRBiYXWjGNhq1_mQPh_3_niRlQrrErs3gi2I-ruiyTWJ8GD6vb9kLbwg4eGGacw6L-I2lq0YeOiOiJ0PD_uyl6kiuVaOd0fGEwyUvCvfsko1hHZBoEaZM-3FtEALP69c31YQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5398" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">۴ موشک جمهوری اسلامی به سمت حیفا و ۲ موشک به سمت تل‌آویو شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5397" target="_blank">📅 10:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5396" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
آغاز دور تازه‌ای از حملات نیروی هوایی اسرائیل به ایران.
🔺
حوثی‌ها : با موشک به اسرائیل حمله کردیم. دریای سرخ بر کشتی‌های اسرائیلی بسته است.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5395" target="_blank">📅 09:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=ZRYBs5K81BaFwMfrRaZzeGuvMwvSXIXH9YbwSPMRnC_1FR-KaFzpe7dQcs_ke46PO2BPqSTt_DPNiE56uZxKaryG4bqzyYARtuKKdpstA_zj88CnOINi4bnjaV6b5onYqUnIvsjGmLK6i_S8GdangnscSlSL2tbNNeXFKavn3aKsat2w1MLWmRcFk--_ZSGEhBLT_ghPJAfsFK1cF1T5ALa4KcaxSctqfxtR1t6EM4hHZOOdUvsWS3p2cUDCHiaB7reFK0-fe8v-rVxWrt82PeFui5QnA67hVRuiVfMBZ_tiuNp6rQ8CMkQifacHpXGfZyx5dMgjSlSo9F0YXqojMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258de5db5b.mp4?token=ZRYBs5K81BaFwMfrRaZzeGuvMwvSXIXH9YbwSPMRnC_1FR-KaFzpe7dQcs_ke46PO2BPqSTt_DPNiE56uZxKaryG4bqzyYARtuKKdpstA_zj88CnOINi4bnjaV6b5onYqUnIvsjGmLK6i_S8GdangnscSlSL2tbNNeXFKavn3aKsat2w1MLWmRcFk--_ZSGEhBLT_ghPJAfsFK1cF1T5ALa4KcaxSctqfxtR1t6EM4hHZOOdUvsWS3p2cUDCHiaB7reFK0-fe8v-rVxWrt82PeFui5QnA67hVRuiVfMBZ_tiuNp6rQ8CMkQifacHpXGfZyx5dMgjSlSo9F0YXqojMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی  جمهوری اسلامی به اسرائیل و  واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5393" target="_blank">📅 09:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔺
وزیر کشور پاکستان صبح امروز تهران را ترک کرد.
با پیامی که مهم توصیف شده بود، از سوی رئیس ستاد ارتش پاکستان و نخست وزیر پاکستان، دو روز پیش وارد تهران شده بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5392" target="_blank">📅 09:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=DKoBkJZLVArMcU8xytEYeMDmkylVQ4pVTgoib2IsYOOkXnEFJFLits_rTKlKcnXMvHh_N2Z5dWmgQ8yLh6qxRitBWbfBDieELs4-sSRJbxt0NrHs5PRsGMe1VP3OhCgVsUvraIKxbO1G-LsB4-GglKqrnKG1I-oC_LwZ1aJK0DCvZQZ-trna5yu719N45T3t-l406miwDMV22RbyCNVIz86-Mp-KbSdksLFsMSYq_1T9YG8gTi4bM_-m51zIWU7FZ43Y2-dhApGG5nXJQ8wuLbdK1NgPfNZshiWE1wXIHRyuKCzMPVLBvvRmai2owcbC4tDzvP-KXnc6S8qIDdrtbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24ce7a16e2.mp4?token=DKoBkJZLVArMcU8xytEYeMDmkylVQ4pVTgoib2IsYOOkXnEFJFLits_rTKlKcnXMvHh_N2Z5dWmgQ8yLh6qxRitBWbfBDieELs4-sSRJbxt0NrHs5PRsGMe1VP3OhCgVsUvraIKxbO1G-LsB4-GglKqrnKG1I-oC_LwZ1aJK0DCvZQZ-trna5yu719N45T3t-l406miwDMV22RbyCNVIz86-Mp-KbSdksLFsMSYq_1T9YG8gTi4bM_-m51zIWU7FZ43Y2-dhApGG5nXJQ8wuLbdK1NgPfNZshiWE1wXIHRyuKCzMPVLBvvRmai2owcbC4tDzvP-KXnc6S8qIDdrtbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - لحظه اعلام خبر حمله موشکی
جمهوری اسلامی به اسرائیل و
واکنش مخالفان جنگ! حامیان خارج نشین‌ اینها
میان توی تلویزیون‌ها میگن دیاسپورای ایرانی عامل جنگه!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5391" target="_blank">📅 09:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvdZyHtcZ3wgY5eHeX6-DXFw1m_aCHJlPII_nQ-0-F7MTmiDhIbeX5VRtRzD7A8mLTRbMy-dnd0Z9YczCwqy5GfRupwtGXmG9oWwxiEucktFuts9zhMhLSbWumzfm6-rzbeT0gug5wzkfQSNn8e3ehiJ9dHCVK_MlgVJYBhgLr6PvLL3HNii0Ym_WybfXD4afdPqsZKhldmW-cxqB4T3IKpFFUmekp8AT8hfkYi78k0hXALfT0gjJliPK8-QqGzmRoiP9VlXmoUgUyJglcIF0QtLi9--3A0iI6e0CUw_pYFNh8jK5vGhvf9xNgYwaVG1kjuNHluCkZW81jVbE33N9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاریجانی هم صبح زود از اون دنیا توییت زد که غم ویرانی ایران رو نداریم!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5390" target="_blank">📅 08:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX9WWYbe5xcNsFS8NQiLGFvgokvAVp7WIVWfKBD09Hrrx9-OHaJgpvXwhDyY2_mc3_lBZ9K_A7uGtJh02Hwe24sh590M4oUh6B49SfX-cmNdhMEtiPVRgp8T-xqkfsMBOSpN0X_fcTnedhwKgv-szh1cA57b69m5aGLyfrGayK-Kf1Clae-yqCW3k2E_HF8mgOB_VLTCJ_hiqQ6DZt00UeCVW7_gGyk37g-EfAJXUtqZULb8e9x-Syh6NYfPDkn_B85mwZtntep9EB9p_Xa-QpyjXyMBH44VgAnLf8FXxabQ9c1OeAKE3S2gDmesy95lFQZEzSF98QYMkBjmADVq2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5388" target="_blank">📅 08:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
خبرگزاری‌های داخلی : اسرائیل شب گذشته به «پتروشیمی کارون» در ماهشهر حمله کرد و این تاسیسات خسارت دیدند.
🚨
اسرائیل دیشب به فرودگاه مهرآباد نیز حمله کرد.
🚨
جمهوری اسلامی دقایقی پیش موجی تازه از موشک‌ها را به سمت اسرائیل شلیک کرد و اسرائیل در حال آمادگی برای موج جدید حملات است.
🔺
کابینه امنیتی اسراییل تا ساعاتی دیگر برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5387" target="_blank">📅 08:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تاکنون : حمله به تهران، تبریز، ارومیه و کرمانشاه گزارش شده است.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5386" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل رسما حملات اسرائیل به مناطقی در غرب و مرکز ایران را تایید کرد.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/5385" target="_blank">📅 04:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای انفجارهای مهیب در تهران ، کرج و اصفهان.
کانال ۱۴ اسرائیل؛ آغاز حملات اسرائیل در ایران</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5384" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
