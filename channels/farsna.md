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
<img src="https://cdn4.telesco.pe/file/gLuGNg4tknGYL7og6NK0hS5jk-_dlpqX6ObhQoTld9q7NWgX3yAIRBp-FbQwLRIkNmONkvu4yGS5p4h0icQIDnxhChi83Dk3EO8CRw35CCKESxJrBXyjZdiOlgf62UHIlC9Ks4QJOK0f2si6rE7ohfElbny40EASIDnsfnuSIeah9l_lfng63VTdib7YxDgX6xcpE4RZDArXn6Y__eZuxXQs6ethw5NnUeqqwkqCQr19swEz0DgbwAiR-kaa5tv_oaVvB_tbN-Ofji_in1K7rOQ7Ii3PBscQ8oD0DAiHvO8_PAMkM7Th7nGze5rBlXXip3AA4XuhSdYfLXFFbY7zRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 12:40:42</div>
<hr>

<div class="tg-post" id="msg-454956">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IB_uTB-CdNMpe3RRyF0mt__bDzXMEcTH-yt2RoXF1A3-Q1lBfsWEC--aVpbo3ZH8FbwsNd-hmny3LEve9iAvsPS6FLFLnUVfgt9kBZEU2XadPUVw9nqI4VfOSoZQUe9jCZPoXLt4etRLUHmzbg-6Y9p3knV1LGkoo4AmW5AZEZ4ulR5Wv6SLTzViPQP5DGju25h-3fcQ9jptZwHy4KychX_9_N38O9F0_WVQKLBBJ3Hif9clPKo91PnyW2C39bfWefMloTuG-ZWqXXFe5abNpvcTd_Cp_H7RvYGcvKs6dV7Dv1vGLj-XauQyBs9CImvLPy6pZc9IXwuXtv3sCDUFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ و نیم میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با با ثبت رکورد تاریخی جدید از ۵ میلیون و ۵۰۰ هزار واحد عبور کرد. @Farsna</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/farsna/454956" target="_blank">📅 12:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454955">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9CM5Y4clqKQO_FxnJMSQqIsrweUOe0gb4iLo8POJF3xMtD8JTZRQFW7uGyUlYQpwv74efMv0yy_tT2Tednc2DBg3e3wtjYHamIP2ZBFjFewIWpmpWi86AKYYgDCIKPdGimetQJpDGh5bh7iP9M_bivyTsSZctbCDWYhLnCAYSMAcghYKx97wb-60PObaYJyTi4HMERojwrHzQ8UHb86eEu7FQZZn0_JIj9K93mORQuNKNPPWy_ICgv2hOLhmc4vOSJar6cyxvRLb7r15nNvANxvFgN2uCIlMcoxqsNOITkWecG548OQLidU3yokYFuid2ookQUHA3qzh_ZgPpHWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک نفتکش سعودی را در منطقهٔ ینبع هدف قرار دادیم
🔹
یحیی سریع: در راستای اجرای ممنوعیت تردد دریایی برای دشمن سعودی، نیروهای مسلح یمن با لطف خداوند موفق به هدف‌قرار‌دادن نفتکش سعودی «وفا» شمال دریای سرخ، مقابل منطقه «ینبع» شدند.
🔹
این…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/454955" target="_blank">📅 12:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454954">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ok2X2eHBnsIR8-9h-MEZwBFVmviPLey3IoBKXkBZEJyAlGXNRRVZDI2nCb1Fsr4sTgDDoLsqJBhMR2X76T2mfSy7yNQcWLgBzBSWD-KtP0uAm6Xo6WF66WFK-MSkza_NgmXUBsXqions3cqAToE11YBh2rMwtnfNjujdZYE1p0U1tmieneIucRDkRjoOZclWOt9maJMYAASbJpSiWQhpkpFlGU2E3liemDV1v9wePq1XvNRjRBcjYq1xFhj9wXU8DTAHRZ4EQTto4w3ibsMOZHQo7ntYNxOCHXGjnEkFXpCZm0dES02kiSTrD1p5GpdYhRcAfvxNVq9K1XwIlBQpIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی، مشاور رهبر انقلاب: نیروهای خارجی باید منطقه را ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/454954" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454953">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c3874c8b2.mp4?token=ZRMncVMW7-J9sT4z-GrSg89BmBjfnFkuFJcAQOCjeAdBsXMRKEeMGFUaYZTpFIFXYmxva0kog83tG6bMLqkiWvGZd6ERX7NLZjHE3e8nwIMML-bh8LuRNrLog3lXxDtmnQ_VDdPK0LSpzFGSNj_N3ctXQ-vo4F9e2TF2hboER_aXgW_teWDmFfGJKIV_SU8l8Fkg9MXiNWRWfFKK6t6kXvWBqv_upoOdgjn2jq940Fh7MRB7OAHs7b_ygedpQV2cX3lvffELcYyHKORV9uM_mbHDC-mZLZ7fbAO4eU0lFr2X-aiGU_1qeDG1gTMosu8o1bYhDYsHqUDuR7Kreo0S0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c3874c8b2.mp4?token=ZRMncVMW7-J9sT4z-GrSg89BmBjfnFkuFJcAQOCjeAdBsXMRKEeMGFUaYZTpFIFXYmxva0kog83tG6bMLqkiWvGZd6ERX7NLZjHE3e8nwIMML-bh8LuRNrLog3lXxDtmnQ_VDdPK0LSpzFGSNj_N3ctXQ-vo4F9e2TF2hboER_aXgW_teWDmFfGJKIV_SU8l8Fkg9MXiNWRWfFKK6t6kXvWBqv_upoOdgjn2jq940Fh7MRB7OAHs7b_ygedpQV2cX3lvffELcYyHKORV9uM_mbHDC-mZLZ7fbAO4eU0lFr2X-aiGU_1qeDG1gTMosu8o1bYhDYsHqUDuR7Kreo0S0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ معنادار هوافضای سپاه به تهدیدات آمریکایی‌ها
@Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/454953" target="_blank">📅 11:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454952">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odBEYGn0tdmdCXqu1fb5ER5W16PMa47tIJ7q6JBj5O2ToiuzyaFxiw0htfSAOhg5-SuTcrFW3U2kkrxxgEy4pNqpAd02fZEpBMsJrCzv8XO4Inim8T4sIMuxOHNApwrTiCxRDGVq0sTtfEdF-oHXGVT8i5JhRaho_-Bik_ZAV5y4CFX2VSp_heV-z9gAQyo9TGxAklZImjBdtbihWNdkp3BdabgJ4KNSSU-JrDB4-1NwV_HBJPtL-R5e4ejB3AZF7EczSNQD53lUoJxNfDpCQdtN3KgwWRM8lXsyPiYK4-7qOfb0g5kYV62JrVfapjnkGspZp-YH-GIF5UzR25lZug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید حوالهٔ ارز در مرکز مبادلهٔ ایران اعلام شد
🔹
دلار: ۱۵۴ هزار و ۴۵۱ تومان
🔹
یورو: ۱۷۸ هزار و ۵۴۲ تومان
🔹
درهم امارات: ۴۲ هزار و ۵۶ تومان
🔹
یوان چین: ۲۲,۸۸۹ تومان
🔹
روبل روسیه: ۱,۸۷۹ تومان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/farsna/454952" target="_blank">📅 11:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454951">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad9d0a8d1.mp4?token=cU6qf0_uTsNpnLNiezcdhZ-nTPHUFRvZzLaZpGbn2dwq2n3MiBgEUMkU2LmhG3Ce0i5dodMgwhKjOVRAbyv5T0OAHc8T5KrZglg6P4wTcPGIPNmzebBBWUylUJgZMrlz5gsp-NimnTdkwJ9hYZ2z1mp-z0nC8MRn5zxAC3K0SShOJ9Zqr2Ni9O2p8wgETMryGV5hBc9b-uFZXfbgVl29ZCH8LaGFa-5nWNkUGt-14aotXTg7Z8414yx488fMhGjwEUH98xQsF3TPKxYk49pseZAXeFP8MZUtsjeHMUFZJDFOhKBgF3rfwBRypqtr37MlTJTcC91SwvEYVA3k3kmyiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad9d0a8d1.mp4?token=cU6qf0_uTsNpnLNiezcdhZ-nTPHUFRvZzLaZpGbn2dwq2n3MiBgEUMkU2LmhG3Ce0i5dodMgwhKjOVRAbyv5T0OAHc8T5KrZglg6P4wTcPGIPNmzebBBWUylUJgZMrlz5gsp-NimnTdkwJ9hYZ2z1mp-z0nC8MRn5zxAC3K0SShOJ9Zqr2Ni9O2p8wgETMryGV5hBc9b-uFZXfbgVl29ZCH8LaGFa-5nWNkUGt-14aotXTg7Z8414yx488fMhGjwEUH98xQsF3TPKxYk49pseZAXeFP8MZUtsjeHMUFZJDFOhKBgF3rfwBRypqtr37MlTJTcC91SwvEYVA3k3kmyiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب: بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/454951" target="_blank">📅 11:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxRWdzRLiLOofHrBzX0B42bYH8IyX08yVmbb2OZ19RoC3FCYOmAdls_OdDnMMihxy3Fx3-lJA0wY5_nIx6DxZVjorRCeQZQlBA0UvE7EVZp9uJkKsv-0f-fM1E64kZrkGW2Wniu9j3j99nBNsx_x8KvLJkQ8giunZY7OriEYVprcA4QjZiO-tprzWWGXxnvvjOmgz9NAYk8JrLMX0LfATkropAkla7xdwbWws05pH2E27nu8DeXW0lkZ5f7EmRm_boM2eyoBbU5p1EQ6rY3CvSQ5VAMgcHl4OaAeDtp1GW-l6pMuSE2ZY9WBMwEdNUVQQI58Gx2xq9Sv-y5lip-Qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجمع هلدینگ خلیج فارس لغو شد
🔹
مجمع عادی هلدینگ خلیج فارس که بنا بود امروز هیئت‌مدیرهٔ جدید را معرفی کند، به‌دلیل آنچه عدم اعلام حضور نمایندگان سهام عدالت عنوان شد، از نصاب افتاد و لغو شد.
🔸
این درحالی‌ست که نمایندگان سهام عدالت ساعتی قبل در مجمع فوق‌العادهٔ…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/454950" target="_blank">📅 11:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سپاه: اعتراف رسانه‌های خارجی به شکست ترامپ حاصل مجاهدت رسانه‌های انقلابی در مقابله با دروغ پراکنی‌های دشمنان است
🔹
بیانیۀ سپاه پاسداران به‌مناسبت روز خبرنگار و سالروز شهادت شهید محمود صارمی: ۱۷ مرداد، یادآور مجاهدت خستگی‌ناپذیر شهید محمود صارمی و دیگر شهدای…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/454949" target="_blank">📅 11:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e2ece40d.mp4?token=G9xTa_Gh2xbXVQtAvVSL0q2o2t5ypTF9Nk-JkU8iwHLOtX6cDw0buY7_39QL1p_JGqb89bzfpCwFqf3fUxSTbd7B-DGxxUsRPPJFZuqfJIHyem7uy_qCNpYakxFvsscJkGLJFKrOZrRPk2dUgiQ8KeCzi7dlLuFrA_pcGHfmsFyAoidTvmIjmGLEIFlQaIkLv9MewatMIvMgn16yevy3p-WwEkTgGMC1cFejjkV54q80EPVnpR3Hnv35BvYpcUDofQQONaN-4_Pxw9ukN3lUdwChBsRLfy7HT0pCd0K-R_88yQa6Ji6PR37gPxVDy5M7U18u3wkehyQKWhHysAmMwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e2ece40d.mp4?token=G9xTa_Gh2xbXVQtAvVSL0q2o2t5ypTF9Nk-JkU8iwHLOtX6cDw0buY7_39QL1p_JGqb89bzfpCwFqf3fUxSTbd7B-DGxxUsRPPJFZuqfJIHyem7uy_qCNpYakxFvsscJkGLJFKrOZrRPk2dUgiQ8KeCzi7dlLuFrA_pcGHfmsFyAoidTvmIjmGLEIFlQaIkLv9MewatMIvMgn16yevy3p-WwEkTgGMC1cFejjkV54q80EPVnpR3Hnv35BvYpcUDofQQONaN-4_Pxw9ukN3lUdwChBsRLfy7HT0pCd0K-R_88yQa6Ji6PR37gPxVDy5M7U18u3wkehyQKWhHysAmMwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: رأی مصادره اموال ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
🔹
براساس رأی صادره، تمام اموال منقول و غیرمنقول ساعدی‌نیا مشمول مصادره قرار گرفته است؛ شایعات رفع پلمب برخی کافه‌های متعلق به متهم صحت ندارد.
🔹
تا زمان بررسی فرجام‌خواهی…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/454948" target="_blank">📅 11:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHMQ4vGBGzxA9466pPB8g0f06Sh0gHDTH2a23jdaP9uVkG-JaBAcQQxtGti5SAGzJc0VUSB4c-29223cLEYyn2BKucKivGVPllgIMdVFhON_uTtG3FzCmdAK_3c-5Pz2gpMEFf1q9IX0Li24qztNn0dM0v_5Y4T2b6nlreV5HPK-n2na0iPbkjrs7z70dwD6wIOvj15lO2ZEhP-YlFdWUsxpVUZFIbpZJaBY2vG-9-qpzmN3c3myX8TI8qVzCcfNEONHaQZn8XgVuZDA9Tbi7AEj5xO8XTZ6pO2xz1-EVrTt9yql_f0upHpwWtv8oUx3W5yJplJlTfgCG-WYtw7Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیهٔ وزارت خارجه به‌مناسبت بیست‌وهشتمین سالروز جنایت حمله به کنسولگری ایران در مزار شریف و شهادت دیپلمات‌های ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/454947" target="_blank">📅 11:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd3fbe409.mp4?token=je1SPUd6xbIaWqqscya8kjRO1DsbGsqET7dn6p8GaK5zQghzqJ5tt2PoidAVS4ZRGuyJZ6WNQ5u0G40zg63_FFTkhIA6LpZ7n3iCeiF4HKpaWiy7hfrqTTYfeozfThZVLiRkD6cJFNns6NkW6WfPJKXXxuI7Bc8bJJLENCKbYpwY-tpLCQTGZxxQR17mH1m05pG63ruwC9GTUVt4EjHrHvdpykTAViLtunCzaVRPipXRGg1k_Fsl8jqTsmQuqiiDsP9UFuL5HYS82qaZOqZ88JKeHygLXCastR624FI3v64dmHjPDsT4Erlv6ybWb3EORT1xQBhN5Ts768twbt0MLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd3fbe409.mp4?token=je1SPUd6xbIaWqqscya8kjRO1DsbGsqET7dn6p8GaK5zQghzqJ5tt2PoidAVS4ZRGuyJZ6WNQ5u0G40zg63_FFTkhIA6LpZ7n3iCeiF4HKpaWiy7hfrqTTYfeozfThZVLiRkD6cJFNns6NkW6WfPJKXXxuI7Bc8bJJLENCKbYpwY-tpLCQTGZxxQR17mH1m05pG63ruwC9GTUVt4EjHrHvdpykTAViLtunCzaVRPipXRGg1k_Fsl8jqTsmQuqiiDsP9UFuL5HYS82qaZOqZ88JKeHygLXCastR624FI3v64dmHjPDsT4Erlv6ybWb3EORT1xQBhN5Ts768twbt0MLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی قوه‌قضائیه: رأی مصادره اموال ساعدی‌نیا جهت فرجام‌خواهی به دیوان عالی کشور ارسال شد
🔹
براساس رأی صادره، تمام اموال منقول و غیرمنقول ساعدی‌نیا مشمول مصادره قرار گرفته است؛ شایعات رفع پلمب برخی کافه‌های متعلق به متهم صحت ندارد.
🔹
تا زمان بررسی فرجام‌خواهی و اعلام نظر نهایی دیوان عالی کشور، ساعدی‌نیا رسماً از فعالیت در حوزهٔ کافه‌داری محروم است.
@farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/454946" target="_blank">📅 11:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-Rf8cBl4DlMoeXtrWuFiLfR8v-X0H-di2XBrgi0_ScWQCbKkG6elcrpmEfKAt03ehBoyeA59g_4DK6wdYkSm3cofdEiLp9MXQ8KPmRotcwYTX3I55DtJt4GJOyRzyd9xKlHwLub5vVff0JtRHy_t-O3OgPMiDROf3Hn8jzNgCchViipRen1WUGUToGjV473Z-Eag-HyVACr-2Iic_4I-Ff-kJ5AMGIeFTy69u1JcU3LMX_u6wuqcx9qMw9aiI2JhQvTaIPQkw48PtSQOayjDS4JUN2IdXaXRb7xHApBhlJvEp5u7ekCT_Lf2k47UWrOmoWGsjSEfWw31rC-fMR4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف لاشهٔ پلنگ در پناهگاه حیات‌وحش عباس‌آباد اصفهان
🔹
در جریان پایش میدانی و بازدید از آبشخورهای پناهگاه حیات‌وحش عباس‌آباد اصفهان، لاشهٔ یک پلنگ حدودا ۵ ساله توسط محیط‌بانان کشف شد.
🔹
این پلنگ که در حین تغذیه از شکار خود تلف شده است، جهت بررسی‌های تخصصی و تعیین علت دقیق مرگ به مرکز استان منتقل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/454945" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: درپی انجام انفجار‌های کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/454944" target="_blank">📅 10:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNdI6_06ZmqJTOeSXfzeR-Ox9O2og1VJj5PvI7PmB8RfRsmZJLEz3bUILPJupl7h-3pHA9m_dHrUe8TCalMAn4rb3kVbRQsK8Xv8QT5XmKWBTAXUIgUdmJvyIcxOXk0xNZruMQGRgRTVyyRq5WyAXDUWJxfKCaO2YapJFyfP1fLj4n-DXcHD42xXPC4vK5XYM0y4HC636DcphgsUdwQqzrBWZeniXfRJZMr2Iwf7dd5NJA_OIOV7a20W4oq3Cyg5MoiY5SWPi0n67h8tZYI4xcte9MNrPFJZ1RG4JlJ0H7nEmyQOkTufYTmT3KKfC4a96bO90fmKhYe7f5flcdLrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌سوزی یک کشتی دیگر در تنگهٔ هرمز
🔹
پایش‌های ماهواره‌ای نشان می‌دهد که یک کشتی که احتمالا نفتکش است در مسیر جنوبی تنگهٔ هرمز دچار آتش‌سوزی شده است.
🔸
بامداد امروز یک آتش‌سوزی در کریدور جنوبی تنگهٔ هرمز اتفاق افتاد و یک شناور مقابله با آلودگی نفتی و اطفای حریق به‌نام «ادنوک ای‌آر۰۱» خود را به منطقهٔ حادثه رساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/454943" target="_blank">📅 10:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUmTCs9-mA5p6qCHSrc7iCbZgh8TSUp58xCB3gL0WDSI_ATYCTM8vyFNGUacl6AoG23RRcY1H5XifRP267tYeNDxT7ZLl0HtGouZYlHkzldLD-3zy8dy27_7mlpXTq5BPgK6VdrzbrTsgl-OnZRhiTrRKcq-sJR-jaf6tVibOiCVFyf88CPtEbxTkLosiqWzeGX6Sv0E1w-1sYiEDeemNRd1HkVumpPRLu0IZ0GxtUR_6TyXkoOa6d3Hib0lkao5XJdN0OhEmF4hlSrB2h7_SrzfT1sk8pERK8EM-XtdpxFERmYjPPvvF1L4cIxY2Dbltbz1wFS7BExd0RQstA1fig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاچهٔ ارومیه جان گرفت
🔹
شرکت آب منطقه‌ای آذربایجان‌شرقی: حجم آب ورودی به دریاچهٔ ارومیه از ۴.۵ میلیارد مترمکعب در سال آبی جاری عبور کرد؛ این میزان، بالاتر از حقابهٔ تعیین‌شده برای دریاچه بوده و بیانگر بهبود شرایط آبی این پهنه نسبت به سال‌های گذشته است.
🔹
استمرار این روند امیدبخش، نیازمند تداوم مدیریت علمی و رعایت دقیق الگوی مصرف است تا پایداریِ ایجادشده در تراز آبی دریاچهٔ ارومیه حفظ و تقویت شود.
عکس: عادل باخدا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/454942" target="_blank">📅 10:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCY8Tr09X168pnG5G9kcfcry1Kr6DYUYgnJ7NPIxJKoiDXgvu3oX-r7ii4srYp5AjUgHJKLu3Nj9oOtN0shGfE5uZAp-Zoykw2NeXTml316bYGeXtAPsgLkm4_9OdfcC99m-Vwd9KmgwB2-VF1EjnMOLH7SqFCqb_lfUPy6ldYCzBO7yVnPWb6NaU_WxUbVTHV-6-UBF0TF__EndqWNTpqmpEVQfwjuopz9cMkR95xy4nFz2Tap7NTha-wIvTEbez2janZ1j2-h5l-Dgzb7wvfNpsTiPBOURJbdMRnoM6g5jN6qtdT4xlyJA_Djxy4LhU7OfS__XEjIvpGlHK31jXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو برای کمک آمد
🔹
رئیس فیفا که با طناب ترامپ به چاه افتاده حالا به دنبال خروج از این چاه با کمک عامل این بحران است.
🔹
نشریۀ تلگراف نوشت: ترامپ وارد میدان شده و می‌خواهد هر چه در توان دارد برای حفظ اینفانتینو در سمت ریاست فیفا بگذارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/454941" target="_blank">📅 10:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ارتش: خبرنگاران فرماندهان نبرد رسانه‌ای با دشمن هستند
🔹
ارتش جمهوری اسلامی ایران به‌مناسبت روز خبرنگار: خبرنگاران، فرماندهان خط مقدم نبرد رسانه‌ای با دشمن به شمار می‌روند.
🔹
فرماندهانی که با ابزار قلم، تصویر و روایت، در برابر هجمه‌های سازمان‌یافتهٔ دشمنان ایستادگی می‌کنند.
🔹
خبرنگاران با روشنگری مستمر، ملت‌ها را در مسیر تشخیص حق از باطل یاری داده و زمینه‌ساز تقویت بصیرت عمومی در برابر موج‌های فریب و عملیات‌های شناختی می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/454940" target="_blank">📅 10:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEJHZetUcFI_7W_j92L_BS8PNGcxOx28Rof1OFLpy3ULZVBtn5yvW8DxosCxLKdWADtEnju0MFzzAhQoIqTtjktWeYGCJclZzpXCiBQbiFOCN4Ddj6nSh6HfaqHVcGcvA6_NSDW94RYzRRvPEcHT2C1lI2MT5bi8SlGufr7nepzQiO3f8TqR7zjrVNN2o811K6sWc82so28kEMjJfP3iBBBuYdS7nz4sAELyAoI7Ri7URuL8ChifC1sEcdDCYr6HRj7b28YJLW8L1ZfAoQBBZJopf1LHJz7MLO_g4ACwWYGRuD1QmT66x7c3U7Ncurc7fpILmMHinXYlYPmR797vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ و نیم میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با با ثبت رکورد تاریخی جدید از ۵ میلیون و ۵۰۰ هزار واحد عبور کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/454939" target="_blank">📅 09:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=Ez9BGLaWn1rNC4JmwOVwGdYIs9vMP2BQQ_UW8esU7bIOVCmz-mJZswRWc2GYDvPn-70CZ-Z-qp6H8KuhADvPQZoNaMktVr8tCmpqMXxkY_KGW1k99e9SrT9yE2JjtfNBAekaW5iFyPHRT5X95nAA5cmgE7HlTLv4fNjl8AncZ5L1OA6wN9isjQWRk0leCev5BGqqOwTa3TATYCa1i-t5_zk638KqQPhyZG9S872yQoptq4_biN_g_8ueqhEG_zztR_wrzM80QmZebNbRZYdY4iIQy5Tlgeqo6QhfV3FSHr_BFagzsS8eB_zyULQNDzOpi1E5AgYzBHZpOej-RjiKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2094e644c0.mp4?token=Ez9BGLaWn1rNC4JmwOVwGdYIs9vMP2BQQ_UW8esU7bIOVCmz-mJZswRWc2GYDvPn-70CZ-Z-qp6H8KuhADvPQZoNaMktVr8tCmpqMXxkY_KGW1k99e9SrT9yE2JjtfNBAekaW5iFyPHRT5X95nAA5cmgE7HlTLv4fNjl8AncZ5L1OA6wN9isjQWRk0leCev5BGqqOwTa3TATYCa1i-t5_zk638KqQPhyZG9S872yQoptq4_biN_g_8ueqhEG_zztR_wrzM80QmZebNbRZYdY4iIQy5Tlgeqo6QhfV3FSHr_BFagzsS8eB_zyULQNDzOpi1E5AgYzBHZpOej-RjiKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ایام عزاداری دههٔ آخر ماه صفر در حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/454938" target="_blank">📅 09:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سپاه: اعتراف رسانه‌های خارجی به شکست ترامپ حاصل مجاهدت رسانه‌های انقلابی در مقابله با دروغ پراکنی‌های دشمنان است
🔹
بیانیۀ سپاه پاسداران به‌مناسبت روز خبرنگار و سالروز شهادت شهید محمود صارمی: ۱۷ مرداد، یادآور مجاهدت خستگی‌ناپذیر شهید محمود صارمی و دیگر شهدای سرافراز خبرنگار؛ نماد تعهد و دلدادگی اصحاب رسانه به کیان انقلاب و ایران اسلامی و آرمان‌های والا و تمدن ساز آن است.
🔹
امروز، منطقه و جهان، شاهد یکی از پیچیده ترین و سرنوشت‌سازترین نبردهای تاریخی معاصر است. آمریکا و رژیم صهیونیستی در جنگ‌های دوم و سوم علیه ایران اسلامی، علی‌رغم تمام تلاش‌ها و اقدامات نظامی و عملیات رسانه‌ای، نه تنها به اهداف اعلامی و شوم ترسیم شده توسط رئیس‌جمهور پلید و متوهم آمریکا دست‌نیافته، بلکه ابعاد تازه‌ای از بن‌بست راهبردی، شکاف در صفوف متحدان غربی و هویدا شدن افول هیمنۀ آنان به تصویر کشیده شده است.
🔹
رسانه‌های جهان، با اذعان به ناکامی واشنگتن در غلبه بر جمهوری اسلامی، به وضوح از «شکست» و «تله خودساخته» ترامپ در جنگ علیه ایران سخن می‌گویند و حتی اعتراف می‌کنند که تفاهم‌نامه‌های حاصله، چیزی جز «سند تسلیم آمریکا» در برابر واقعیت‌های میدانی و قدرت مذاکراتی ایران نبوده است.
🔹
این اعترافات، بیانگر درخشش مولفه‌های اقتدار نظامی و بازدارندگی فعال کشور است؛ مولفه‌هایی که مرهون هوشمندی راهبردی، ایستادگی ملت و پشتیبانی همه‌جانبه از نیروهای مسلح، به‌ویژه سپاه پاسداران انقلاب اسلامی و نیز مجاهدت هوشمندانه و دقیق رسانه‌های انقلابی در مقابله با دروغ پراکنی‌ها و بزرگ‌نمایی‌های خصمانه دشمنان است.
🔹
در این میدان پرچالش و معنادار، دشمن با بهره‌گیری از تمامی ظرفیت‌های جنگ ترکیبی و سایبری از جمله هوش مصنوعی، در پی تحریف حقایق بوده تا میان ملت و نظام ایران فاصله بیندازد و سرمایه عظیم اجتماعی و وحدت مقدس ملی را نشانه بگیرد.
🔹
تجربۀ اغتشاشات به‌ویژه در کودتای ۱۸ و ۱۹ دی‌ماه ۱۴۰۴ به ما آموخت که ضلع رسانه‌ای فتنه، پیچیده‌ترین و حیاتی‌ترین بخش این معادله است؛ جایی که «روایت اول» از آنِ کسی خواهد بود که سریع‌تر، دقیق‌تر و هوشمندانه‌تر وارد میدان شود.
🔹
این تجرب‌ تلخ فرصتی شد تا خبرنگاران فهیم و انقلابی و رسانه‌های متعهد و زمان شناس، در جنگ تحمیلی اخیر، با تمرکز بر روایت‌سازی صحیح و بهنگام، با عملیات روانی و آفند رسانه‌ای علیه دشمن، تصاویر ماندگاری از صلابت رزمندگان، گزارش‌های صادقانه از حضور و مقاومت مردم، روایت مظلومیت شهدا و خانواده‌های آنان و بازتاب همبستگی کم‌نظیر ملت ایران، را  تولید و انتشار دهند که بخشی جدایی‌ناپذیر از تاریخ پرافتخار این برهه حساس و ارزشمند محسوب می شود.
🔹
خبرنگارانی که در جنگ تحمیلی دوم و سوم زیر آتش و در معرض تهدید، لحظه‌ای از انجام مسئولیت خود عقب ننشستند؛ آنان که در کنار نیروهای امدادی، مدافعان امنیت و مردم مقاوم حضور یافتند و حتی برخی از ایشان جان خود را در راه اطلاع‌رسانی و دفاع از حقیقت فدا کردند، شایسته بالاترین مراتب تکریم و قدردانی‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454937" target="_blank">📅 08:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWpzp0cF3XfmH5fC0GqsdWivoO6yLlUlZrqgVAM4qmpcv9Hl8mE5dNEp-B6CNyoSHHfbr4x2WGLUn9j1UqhoUCz4pFJhTxV9IiDHjLPgqWmu_ZDYNkvPNYpJ1OMCyvGX4YRvK3TwvKaGcEbW88FMAwsPAqxcAeoA8GjRoI2jTw3PNKsqoa-Y5GlorMDvUbE7Nwmd1Xw8H3F4tSF5f21X1dEIKsPlyiS8pfcf2zB_-RLU_g-erU5ApdTAYoqHeUxg-IzVgm6sXN4y7jVZ69t1s0pghla2X_oHaI4SUMqYHWztfdwszPEAV4m3zv-74haVhf1VrbclxCMkKEg9YRXyvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: خبرنگار متعهد، هم‌سنگر رزمندگان پشت لانچر است
🔹
رئیس قوه‌قضائیه در پیامی به‌مناسبت روز خبرنگار نوشت: خبرنگاران متعهد کشور در دشوارترین روزهای یک‌سال گذشته، با شجاعت و مسئولیت‌پذیری از مرزهای آگاهی عمومی و انسجام ملی پاسداری و در میدان جنگ شناختی، با خط تحریف، سیاه‌نمایی و تفرقه‌افکنی دشمن مقابله کردند.
🔹
در مقطعی که تمام دنیای کفر و استکبار، جنگی موجودیتی به ایران عزیز ما تحمیل کرده‌، عظمت کاری خبرنگاری بیش از پیش درک می‌شود.
🔹
خبرنگاری که سعی می‌کند خبرش درست و دقیق و سریع باشد و در عین حال التهاب و تشنج اجتماعی خلق نکند و امنیت روانی مردم را تثبیت کند، حقیقتاً هم‌سنگر همان رزمندگان پشت لانچر است که از تمامیت ارضی و عزت و اقتدار ایران عزیز دفاع و صیانت می‌کنند.
🔹
خبرنگار متعهد، دیده‌بان تیزبین میدان جنگ روایت‌هاست؛ او که با کلامی سدید و قلمی بصیر، خاکریزهای ذهن جامعه را در برابر تهاجم ترکیبی دشمنان استقلال و اقتدار ایران، مستحکم می‌سازد و اجازه نمی‌دهد که غبار تردید، سیمای درخشان حقانیت ایران اسلامی را مخدوش کند.
@Farsna</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/454936" target="_blank">📅 08:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزارت دفاع: ایران در میدان دفاع مقتدر خواهد ماند
🔹
وزارت دفاع و پشتیبانی نیروهای مسلح به‌مناسبت روز خبرنگار: در شرایط جنگ ترکیبی و عملیات روانی دشمن، روایت صادقانه حقیقت، مطالبه‌گری مسئولانه و صیانت از افکار عمومی، بخشی از قدرت ملی و بازدارندگی جمهوری اسلامی ایران است.
🔹
خبرنگاران، یاوران و همراهان راهبردی در شکل‌گیری گفتمان دفاع همه‌جانبه و انقلاب صنعتی دفاعی جمهوری اسلامی ایران هستند.
🔹
جمهوری اسلامی ایران، در میدان دفاع، در میدان روایت و در میدان اراده، همچنان مقتدر، هوشمند و آماده خواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/454935" target="_blank">📅 08:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRxuH2Hw1H61mgb98W7XdJUPE-r7I2etsrdC3ZJ8GFXNRUvjxrYFf4tc3vNLy6hJZDMmi-l1y43i1EX9Ee9c-CTEBQyduQB0GPtkSlITj01ENJMglHX5nII7ATGt9AKa91Zxr1f0mEk80wXxcYRezjhGXZxjkC3QbB86b9NwkQHzIA92yGredJENa3qqfQLKw-_Rz1slKXohyUYvvQlhbIPcV_K_Kf5_g95sGk4NKMdvV-_FWdjSpUHzlnr2xxUCyoR7APe4LHKPnBKPfMkN48mclwJJD6u7Q3PA93kh9oigsSkFIjZNqRPE5-Q1G-fMnX8iMKpqlIYKCbkmuL1ChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: خبرنگاران رزمندگانی هستند که سنگرشان آگاهی و سلاح‌شان حقیقت است
🔹
پیام رئیس‌مجلس به‌مناسبت ۱۷ مرداد: سرنوشت ملت‌ها علاوه‌بر آنکه در میدان آتش رقم بخورد، در میدان روایت تعیین می‌شود و میدان‌های نبرد تنها بر خاک و دریا و آسمان شکل نمی‌گیرند.
🔹
صهیونیسم و استکبار جهانی تنها شهرها را بمباران نمی‌کنند، آن‌ها حقیقت را هدف قرار داده و اعتماد ملت‌ها را نشانه گرفته‌اند و اگر روزی با گلوله به جنگ تمدن‌ها می‌رفتند، اکنون با خبر، تصویر، شایعه و تحریف به میدان آمده‌اند.
🔹
در چنین جهانی، خبرنگاران تنها مخابره‌کنندۀ اخبار نیستند؛ رزمندگانی هستند که سنگرشان آگاهی، سلاح‌شان حقیقت و مأموریت‌شان دفاع از امنیت روانی، هویت ملی و اقتدار فرهنگی یک ملت است.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/454934" target="_blank">📅 08:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یمن نفت عربستان را زمین زد
🔹
کپلر گزارش داد، صادرات نفت عربستان پس از اعلام محاصرۀ یمن از بیش از ۴ میلیون بشکه در روز، به کمتر از یک میلیون بشکه کاهش‌یافته است.
🔹
تنها راه باز صادرات نفت عربستان اکنون کانال سوئز است که سابقۀ بسته شدن دارد.
🔹
همچنین پیش‌تر اعلام شده بود که برای اولین‌بار در ۴۰ سال گذشته صادرات نفت عربستان به آمریکا صفر شده است.
🔹
طبق داده‌های کپلر پس از اعلام رسمی‌ محاصره از مسیر باب‌المندب، میزان بارگیری نفت در ینبع به‌عنوان خط دورزن تنگۀ هرمز صفر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454933" target="_blank">📅 07:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2nxUjCbbIfYs8djqzhiJnw9hrxkK9w3_1AqkIhiECQtwmpMDSDbGgtAy5t8EtruIgKor00XoFJU3rj-dLr4Macla9jOXdVnVu2gMZPHwuF-jjKcnp7XBuKzMvkTKRc582_0LedcuuMuvcL-UBjywcCUtyYExpOgt0-PSJ8UU7M7xzEnouFBsWPV02d2IDvdcN9KXZhq5lyo1b4YrZvLtUDPSj84SvBAeoSzpEKoJJmUdrPDNfmhQTv8l0_tc1mFzbNAHR9y9ns13dV1o4R6w7JhHBgUveaay0TgAg04WeLFjE7q-SJsup9j95yu73K_sXyPi5OpZ83AgPYmWDxg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ اوکراین به پالایشگاه سیزران روسیه
🔹
پالایشگاه سیزران روسیه ساعتی پیش هدف حملۀ پهپادی اوکراین قرار گرفت.
🔹
پیشتر فایننشیال تایمز گزارش داده بود که نیمی از زیرساخت پالایشی روسیه به دلیل حملات اوکراین متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454932" target="_blank">📅 07:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW1jmVZUini9eiC8yNM_6v2tjQ6fuHeTH9ffi9AjDCDnrcVZpxlHhV7tywcsetzpfn-bOlnY1CXhTyYmcXS2eOTXz82T-kKOt__e_-ZmQd1VJjRiGq5LoliPU11I39DlxvHgY1Y_ksuXQFIBEHQLprQ-6HUquqES5jIG-0sTw_xGkKvrsaQzwiUEXHTcYDWCQyNPowF9x4i2pvRtenpGZSNOEzOzniErf3ihhkxYW-isVLL7CQNveaMOKcEBrmVTyB3riakxdaB_vBN0wzFE2Z8b5YrX7nD6P3s321WsgrZZndbtGh2ohWCYZ7V26NEdDVpoU0YbJ4eZdKmS-cWdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار هواپیماها از فرودگاه جده عربستان
🔹
دقایقی پیش، هواپیماهای مسافربری به مقصد جده حاضر به فرود در این فرودگاه نشدند و از فضای هوایی جده گریختند.
🔸
تعدادی از منابع غیررسمی از حملۀ ساعاتی قبل یمن به عربستان خبر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454931" target="_blank">📅 07:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454930">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ab2e54ea.mp4?token=b5KnJ9YFySlfeBVBhiTj-QRs88DjXLwVbdy-gFvm0lef-lYpz_lZK-MVEI3pgaPi05fHOkdshTgmKC1eJ8iS5tUNc55Bgny-WeJPbY7xl1hSHVMkjqgqiO-8wC3VlIpHjdKZ65L93_tVM2abu22JSOEg8wLnT5uYftq-rhtGXEo3WmBu9IcypB_aXNfD2q1ITAueJmlmIs4P5Se7kqQILAEd1UGpK8pcBsGwrd7jXKIOH4ZZeX0mwOM-1BaVpJXer3pdoe5hkA0SCvUt41dfAWWaBJsDiSDWmQd2tVjz2eCDfDOaQ9mY2iTzBX3WKgTPCMm_A0-5IjaALsAEmTMZtymy3aK8n7OTXtrf5SFqZePE05GcBcdEN-SMSnaMdE2Kchm3DlNIFlyXQ8TJ5-Rek0LmwUVa350hOqUOwpoSIyMIhLf2LkbIR1yVjdvXSwORm5Q0TsT0Z8nuJO4PSSKJM5Fu-bi-rfDJfn2QImvuyFCnjf4gMj5NDrem5etZAw91HAWgA1Y5e8wBbmwxzkh9YE7sdgqzjQ8PCdTepGtjH2oduZR7e9wvUNkAVUEQ6OBs1oR_43cD7AbgFUZaHNGIDQuqmkGo8GPlhNd_FAKL1PFN49jU6wsGhKhY6j11HYPQ5fUArXp6MktcTg3RV_ZerPfzzLj_XmUGBMG_fwF44yo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ab2e54ea.mp4?token=b5KnJ9YFySlfeBVBhiTj-QRs88DjXLwVbdy-gFvm0lef-lYpz_lZK-MVEI3pgaPi05fHOkdshTgmKC1eJ8iS5tUNc55Bgny-WeJPbY7xl1hSHVMkjqgqiO-8wC3VlIpHjdKZ65L93_tVM2abu22JSOEg8wLnT5uYftq-rhtGXEo3WmBu9IcypB_aXNfD2q1ITAueJmlmIs4P5Se7kqQILAEd1UGpK8pcBsGwrd7jXKIOH4ZZeX0mwOM-1BaVpJXer3pdoe5hkA0SCvUt41dfAWWaBJsDiSDWmQd2tVjz2eCDfDOaQ9mY2iTzBX3WKgTPCMm_A0-5IjaALsAEmTMZtymy3aK8n7OTXtrf5SFqZePE05GcBcdEN-SMSnaMdE2Kchm3DlNIFlyXQ8TJ5-Rek0LmwUVa350hOqUOwpoSIyMIhLf2LkbIR1yVjdvXSwORm5Q0TsT0Z8nuJO4PSSKJM5Fu-bi-rfDJfn2QImvuyFCnjf4gMj5NDrem5etZAw91HAWgA1Y5e8wBbmwxzkh9YE7sdgqzjQ8PCdTepGtjH2oduZR7e9wvUNkAVUEQ6OBs1oR_43cD7AbgFUZaHNGIDQuqmkGo8GPlhNd_FAKL1PFN49jU6wsGhKhY6j11HYPQ5fUArXp6MktcTg3RV_ZerPfzzLj_XmUGBMG_fwF44yo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طوری زندگی نکن که واقعیت را نبینی
🎙
حجت‌الاسلام رمضانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454930" target="_blank">📅 05:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454929">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyKey8xHAgqKk-Nr830mFBBQtFlb_3Wg6s5tPnHeKNkLI1EO5af3qQIAJ01zAIWcgNlkNb3DI1J8qul6D4Rqi14W-hagMGUCoUgXigX65r_4Bzpglr7kCYVnYhAzV-JwwcyFMPgXQv2m0-SP6i2c2XIBG7zWggSbXpjwa8jIqLdd0XS9OSyffjuUK2_aeMis_l72wH23iJteawzgjw6jLu3ndO_gHfcg344VIgWw7nFnaGidsC2pYnZ2hzF5DRUvyQtkMzLcRNUnJx6jbw1pLGloOvBv3ldZwoLM1XYDJJEP7NNYo72-kF4PXrrEplaeKtxcna2SScgO7SKMb9NlCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۴.۶ ریشتری در گلباف کرمان
🔹
ساعت ۰۳:۰۷ بامداد، زمین‌لرزه‌ای به بزرگی ۴.۶ ریشتر حوالی شهر گلباف در استان کرمان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454929" target="_blank">📅 04:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454928">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buxAqFtt9KZehIYthIa_PSnXb-jT0GUIjbnncUKemI6ZDBMdsvOfVslXaGltUr4WIaBJg_kSq47jb4CXrCMekEXEyX6G12b4wF8U3SF21TDunvpD4PiVWNFkL0JZZUDWcuu62ND69LyF5zhWY0rVv6s3qYisY0NpdNROoDXacE4bAW4iDz4yiGx9x2RnbkrAl2EjTdAP6UONxuYv1kQEVtz5V_sy7Va0F4d47EZLLY8l8Jz6KgRuw_WuZMMbZgOC0QAmai2eROe8qvozCsSiQcpmO3e-1Ox4tU6T5SxarmBBOt-w8ll78U05GTZaLRFrZz1PxYDU7LUZAgeeaQRE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار ارشدترین ژنرال آمریکا درباره محدودیت‌های نظامی علیه ایران
🔹
شبکه سی‌ان‌ان به نقل از سه منبع آگاه گزارش داد «دان کین» رئیس ستاد مشترک ارتش آمریکا طی چند هفته گذشته در گفتگوهای خصوصی با دیگر مشاوران ارشد ترامپ صراحتاً تاکید کرده است که ایالات متحده باید «راه خروجی» از جنگ با ایران پیدا کند.
🔹
به گزارش سی‌ان‌ان او گفته گزینه‌های نظامی موجود برای تشدید منازعه می‌تواند نتیجه معکوس داشته باشد و صرفِ اتکا به نیروی هوایی نیز بعید است اهداف اعلام‌شده دونالد ترامپ را محقق سازد.
🔹
کمرنگ شدن چشم‌انداز پیروزی نظامی باعث شده کین در این دیدگاه تنها نباشد.
🔹
دو منبع آگاه تایید کرده‌اند که او نگران گزینه‌های نظامی روی میز برای تشدید درگیری است و موضوع یافتن راه خروج را با سایر اعضای کلیدی کابینه از جمله جان راتکلیف (رئیس سیا)، مارکو روبیو (وزیر امور خارجه) و جی‌دی ونس (معاون رئیس‌جمهور) در میان گذاشته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454928" target="_blank">📅 04:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454927">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ادامۀ تجاوزگری‌های رژیم صهیونیستی در جنوب لبنان
🔹
المیادین: توپخانۀ ارتش اشغالگر صهیونیستی منطقۀ علی الطاهر را هدف حملات خود قرار داد.
🔹
همچنین ارتش اشغالگر اسرائیل اقدام به یک عملیات انفجاری در شهرک «میس الجبل» نیز کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454927" target="_blank">📅 02:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454926">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb10961f.mp4?token=N9sGcyhh_vAjchSkCyoA0NGpR3pFk1Xrm17Di00L-8_dMs64Fg3EyaeYz5lApL6vj0hHKV6z2u6apkHO-ZLdFLkVgG8MfEHRYYbjbrgrdpz-m8qNbfFTdwx1HwadD85ExVSVHUlSjnwpp18A5b5KP8tGkOKC_gnTh1-yDI8ExnnoEJr8kFA3UmTegtw4fcWZ9OBEFcrFw_3rrKRNDMNAzGJ38e3IJpxUhpn9ZQdQuwc2hVHljWrRPa1novXnfN5PfC2gIRZr0bPpNXwn2rFMQAdLUiPZjkMS-gRUJuUiqObglZ_9ANLl6ueOr4AifM7NewItLa82-LLHmxEGCHkCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb10961f.mp4?token=N9sGcyhh_vAjchSkCyoA0NGpR3pFk1Xrm17Di00L-8_dMs64Fg3EyaeYz5lApL6vj0hHKV6z2u6apkHO-ZLdFLkVgG8MfEHRYYbjbrgrdpz-m8qNbfFTdwx1HwadD85ExVSVHUlSjnwpp18A5b5KP8tGkOKC_gnTh1-yDI8ExnnoEJr8kFA3UmTegtw4fcWZ9OBEFcrFw_3rrKRNDMNAzGJ38e3IJpxUhpn9ZQdQuwc2hVHljWrRPa1novXnfN5PfC2gIRZr0bPpNXwn2rFMQAdLUiPZjkMS-gRUJuUiqObglZ_9ANLl6ueOr4AifM7NewItLa82-LLHmxEGCHkCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرس‌های قهوه‌ای دوباره در اشترانکوه آفتابی شدند
🔹
تصاویر تازه‌ای که محیط‌بانان اشترانکوه هنگام گشت‌های حفاظتی ثبت کرده‌اند، دو قلاده خرس قهوه‌ای را در کنار تعدادی کل و بز وحشی نشان می‌دهد.
🔹
خرس قهوه‌ای در رأس زنجیرۀ غذایی بسیاری از زیستگاه‌های کوهستانی ایران قرار دارد. حضور این گونه معمولاً به معنای آن است که چرخۀ طبیعی منطقه هنوز از هم نپاشیده است. زیرا خرس برای ادامۀ زندگی به زیستگاهی امن، منابع غذایی متنوع و کمترین میزان مزاحمت انسانی نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/454926" target="_blank">📅 02:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454925">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca78e40b2.mp4?token=qpjHDN5altoc0bT5XfgTfhSUAmtpcwXW-XZhpuEgyEJJhNmUqJ4D-Tg0jrgT9X7_0xPapW5c039G_OWrgR7kJQ_q9oujsK9CVUj2XEmqHCsb6SwPVdNdbJmmp0LVgLKRJoitEHeRIEDCBcWCbfDXYwDbtWLTwuaji5mninelJ4YZFGyydyV_1aJYxMPlRtlVbbOJR-MJuYY9-ErQcLoOSZYHDP7ZqfHbcZCXUqY20avS4nRiG9tdiouhMz5zN01jXJnKGp7p2p7mBKopBELuJtgfbSstPHBmmr5SwAGjdfdmOP8eghVDl8gIWTWHOQFQ3F8xEdBvAO-yoKhr4kyVuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca78e40b2.mp4?token=qpjHDN5altoc0bT5XfgTfhSUAmtpcwXW-XZhpuEgyEJJhNmUqJ4D-Tg0jrgT9X7_0xPapW5c039G_OWrgR7kJQ_q9oujsK9CVUj2XEmqHCsb6SwPVdNdbJmmp0LVgLKRJoitEHeRIEDCBcWCbfDXYwDbtWLTwuaji5mninelJ4YZFGyydyV_1aJYxMPlRtlVbbOJR-MJuYY9-ErQcLoOSZYHDP7ZqfHbcZCXUqY20avS4nRiG9tdiouhMz5zN01jXJnKGp7p2p7mBKopBELuJtgfbSstPHBmmr5SwAGjdfdmOP8eghVDl8gIWTWHOQFQ3F8xEdBvAO-yoKhr4kyVuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهدی سلحشور مداح و رزمندۀ دفاع‌مقدس با حضور در میان رزمندگان مدافع خلیج‌فارس، از خط مقدم تنگۀ هرمز می‌گوید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/454925" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454924">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=oWD5e1nzwFlOi0ytRiJbySwvMBbkW7an64oD5Oz4nzAa7Qwg7KXj4VquLxil4izedg76fFCd-KRzROIq3-n7Gz4U3BYD0YQt_GZNGHK8jd-Fsl8f_koBY76jGkDj-fnK8yMiK0hPhA0Qq86n5odOwi1Cv2gKi_cDlgr67cShKV-mamw3MmekVDTU7oNfllMQ0NltRaxQ5gyxN4zVaUZywZ0G6sWibipgD8RCIRofPa-UAikx_tlgHeUmRk0FRnlAEHu6IlcHbtXG0O4J_Kvm7kYevalVWU3du8U1z7vXL1Hz6LIrXix_HFGzZv_5CeznGd9-PgBHH1Qi_p5IU18kMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c7c72b59.mp4?token=oWD5e1nzwFlOi0ytRiJbySwvMBbkW7an64oD5Oz4nzAa7Qwg7KXj4VquLxil4izedg76fFCd-KRzROIq3-n7Gz4U3BYD0YQt_GZNGHK8jd-Fsl8f_koBY76jGkDj-fnK8yMiK0hPhA0Qq86n5odOwi1Cv2gKi_cDlgr67cShKV-mamw3MmekVDTU7oNfllMQ0NltRaxQ5gyxN4zVaUZywZ0G6sWibipgD8RCIRofPa-UAikx_tlgHeUmRk0FRnlAEHu6IlcHbtXG0O4J_Kvm7kYevalVWU3du8U1z7vXL1Hz6LIrXix_HFGzZv_5CeznGd9-PgBHH1Qi_p5IU18kMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سانسورچی‌ها ناتوان از پنهان‌کردن ضربات کوبندهٔ ایران بر ارتش آمریکا
🔹
وقتی قدرت نظامی ایران و ضربات کوبندهٔ رزمندگان جان‌برکف ارتش و سپاه بر پیکرهٔ ارتش آمریکا آنقدر خسارت‌بار است که با وجود سانسورهای گسترده هم نمی‌شود پنهانش کرد. ‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/454924" target="_blank">📅 00:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454923">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
مردم فسا امشب هم برای ایران به میدان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/454923" target="_blank">📅 00:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454922">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCm29aTZZIDLxjoPs01PPuhiCiW0U6fBhLRSY7oEy6Di2pj9i1vm9meWh4XDC2iVFlWw2trapqkZCUU6NSpU79t_U0qMXnV_EPezET3TMOM0UOfcAjNvBELX7n9fxBjomYQLXPd_UkDEUmJ6dXjyxS-VVV_TdgmAKv_m4OIBgaJ1iv0dwoNjNO7XFkLz_PbirtwZH4RvSO9yFwM3qNhGLJAThMyYr_twtJ-CXSA4G5RsI53mPYBBLjZ7u-BDAPn6xCd_XHz8mVDl9r7J2dLnpl0exozK8dlUFQ4ciRgb9tk_vvuI8GrnBpXFveYL2TMXuxNbWXOn2wZZj4D9cS_Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب‌وکتاب اشتباه
🔹
امام صادق(ع) متوجه شدند مردی در میان مردم به تقوا و نیکوکاری بسیار شهرت یافته است. ایشان برای بررسی موضوع، به‌صورت ناشناس و به‌دور از چشم مردم او را زیر نظر گرفتند.
🔹
مرد وارد مغازه‌ای شد و در فرصتی مناسب، دو عدد نان دزدید. سپس وارد مغازه دیگری شد و دو عدد انار هم دزدید. امام به دنبال او رفتند تا ببینند با این مال حرام چه می‌کند. مرد به راه خود ادامه داد تا به فقیری رسید و هر دو نان و دو انار را به او بخشید.
🔹
امام صادق (ع) جلو رفتند و از او درباره این رفتار عجیب پرسیدند. مرد که امام را نمی‌شناخت گفت: «ظاهراً قرآن نخوانده‌ای! خداوند می‌فرماید هر کار نیک ده برابر ثواب دارد و هر گناه فقط یک عِقاب، من ۴ تا دزدی کردم که می‌شود ۴ گناه، اما آن‌ها را صدقه دادم که ۴۰ ثواب دارد. ۴ گناه را از ۴۰ ثواب کم کنیم، ۳۶ ثواب برای من باقی می‌ماند!»
🔹
امام صادق(ع) در پاسخ فرمودند: «تو قرآن را بد تفسیر کرده‌ای. خداوند می‌فرماید: «إِنَّما يَتَقَبَّلُ اللَّهُ مِنَ الْمُتَّقينَ» (خداوند فقط عمل پرهیزکاران را می‌پذیرد).
🔹
تو با دزدی ۴ گناه مرتکب شدی و چون مال حرام را به دیگران دادی، بدون اذن صاحبش تصرف کردی و ۴ گناه دیگر هم اضافه کردی؛ پس ۸ گناه مرتکب شدی بدون آنکه هیچ ثوابی برده باشی.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/454922" target="_blank">📅 00:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454921">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c14ff6ba.mp4?token=aD5_uspBAV7ofz90d1nqBepUeftVAiiO7cfX9TDLzDva3t2Zze63xQDT5p_j1TCoT8SzzAlSkdr8FbaaiBsqmNguDBYgVe1l9cr02Z9mltFCjN4kTRCf9YfTsX9Or2EGtoPNTiTVN4mAyk_xzphR_tl8o4mSas4kO-K53OKj3fO3NOduPNMUiFoSWgTbByZ-hyZ8dOkIp43PaACmpWLOjP9T-FKOsk4EIREdTT9HGwXXVrdRRS94YzHzVve96fMJ-BZFQc_IePAGmnhjTE2U-OX952tPic64qhxwrFiWVKVW4CDnESvKLcCvmojk1V1YBfbyRl7W-iOUE1LY8_XcnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c14ff6ba.mp4?token=aD5_uspBAV7ofz90d1nqBepUeftVAiiO7cfX9TDLzDva3t2Zze63xQDT5p_j1TCoT8SzzAlSkdr8FbaaiBsqmNguDBYgVe1l9cr02Z9mltFCjN4kTRCf9YfTsX9Or2EGtoPNTiTVN4mAyk_xzphR_tl8o4mSas4kO-K53OKj3fO3NOduPNMUiFoSWgTbByZ-hyZ8dOkIp43PaACmpWLOjP9T-FKOsk4EIREdTT9HGwXXVrdRRS94YzHzVve96fMJ-BZFQc_IePAGmnhjTE2U-OX952tPic64qhxwrFiWVKVW4CDnESvKLcCvmojk1V1YBfbyRl7W-iOUE1LY8_XcnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهرکردی‌ها با شعار خون‌خواهی به خیابان آمدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454921" target="_blank">📅 23:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454920">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM_AEpS35uD66cGAk2gOhPfa4zInV_q_oO4jAJKw0dVQIkC25t9gcTiySv-VmlbXapBxNigCs4_Ie3M2GPI_PIncvNk_w85WEnFucDjco1gp29zw-vKVlD08wYld_xjAIGmAwDSlrRt36Kq6lAKS1f513A6bYrHs_XJzCUmDIrQbTsVXDPUK5Elq4tdNQikSlCLYkn3okWgpZe5Csau1zT61wIkfF52mk055TD83hN7wOUo7djSnGFWkqMAEbImwcqQ26hVwH5oYoI92nC-2HNN7lsUhaR3rCL3d1aKrGcLrHZl-izjygQlupAFvmxdZ1w6et13wX8fdCw-qUjCApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترس از موشک یمنی نفتکش‌های سعودی را به دروغ واداشت
🔹
خبرگزاری آمریکایی بلومبرگ: برخی از نفتکش‌هایی که به سمت بنادر سعودی در دریای سرخ می‌روند به جای مقصد نهایی خود در عربستان، نام کانال سوئز یا بنادر مصر را به عنوان مقصد خود ثبت می‌کنند.
🔹
این تغییر رویه تلاشی است برای پنهان‌سازی هدف واقعی این شناورها که همان بارگیری نفت خام سعودی است و همچنین فراری از گزند حملات موشکی یمن که در واکنش به محاصره عربستان، دریای سرخ را به یکی از پرتنش‌ترین مسیرهای آبی جهان تبدیل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/454920" target="_blank">📅 23:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454919">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🎥
وفاداری کاشمری‌ها در شب ۱۶۰ بعثت مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454919" target="_blank">📅 23:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454918">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aed543861.mp4?token=XAEDSdOmWmINsMSj0glnmdT1waAJMBALHjDsjBkL0_O7oriby4w0DwQyubHhG42MpOsZ3s5hhxZDkCMCI3WW2_Uf7oNS7m-DrbXlfxYuNiRLdFfTxAVhn6Zs4M6gyykf6QMlJ6GCAbI9DPO0RwuV6p88en70M1XXamGH3zeQaGFtM24Ovupr5fAabqdvtDcnlwlRfD8LA7mfPY5_Wthf44PXVdVHDkzKBXVKq6OaGBNWRdKyjINWomXP_9m0PWsCKYtfXhgjb0hxv-vDPn2hF5LwKgWaftRd5Xb3UU3J0iTnMOz-7Oi63E1mWelee9aVBZ_aXYBcSijiqFQZ6YDi1zoN712RjVBSad6UVrD9VsiHa3s66kJfTXMF-2JoQkvlg0lHClFPVPLnuQWQdhD-gMj72dnao-TEGfUaAxmEvp0a1yVaJn9qHcoFoqrZLHeOUz53DdF8HXJTuljYMnFqbuOOnNIDyian4lCVL2aN1tBH0iQiXw9igRmkWkCyDmwkn3ZQc7MuUpVaUasg8qeClOyVKY0Du1FtexkIq_NqPDJzX5_UKBuHi8oK7rXOuhSjg6uJaF35-knD7nplgjhU-7KM66bf5ke84y0g_oajZIHR9zEm3LVF-Rmp4oxBLqlzni4wO8HUhRiWzww7ImoGXjalamV84OUogHXLDZReXR0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aed543861.mp4?token=XAEDSdOmWmINsMSj0glnmdT1waAJMBALHjDsjBkL0_O7oriby4w0DwQyubHhG42MpOsZ3s5hhxZDkCMCI3WW2_Uf7oNS7m-DrbXlfxYuNiRLdFfTxAVhn6Zs4M6gyykf6QMlJ6GCAbI9DPO0RwuV6p88en70M1XXamGH3zeQaGFtM24Ovupr5fAabqdvtDcnlwlRfD8LA7mfPY5_Wthf44PXVdVHDkzKBXVKq6OaGBNWRdKyjINWomXP_9m0PWsCKYtfXhgjb0hxv-vDPn2hF5LwKgWaftRd5Xb3UU3J0iTnMOz-7Oi63E1mWelee9aVBZ_aXYBcSijiqFQZ6YDi1zoN712RjVBSad6UVrD9VsiHa3s66kJfTXMF-2JoQkvlg0lHClFPVPLnuQWQdhD-gMj72dnao-TEGfUaAxmEvp0a1yVaJn9qHcoFoqrZLHeOUz53DdF8HXJTuljYMnFqbuOOnNIDyian4lCVL2aN1tBH0iQiXw9igRmkWkCyDmwkn3ZQc7MuUpVaUasg8qeClOyVKY0Du1FtexkIq_NqPDJzX5_UKBuHi8oK7rXOuhSjg6uJaF35-knD7nplgjhU-7KM66bf5ke84y0g_oajZIHR9zEm3LVF-Rmp4oxBLqlzni4wO8HUhRiWzww7ImoGXjalamV84OUogHXLDZReXR0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کلاته‌رودبار سمنان از ایستادن پای تنگه هرمز می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454918" target="_blank">📅 23:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454917">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5493f0e659.mp4?token=VL-vYg50qGobBL0jEBzhisZ7R6dni2v-1SK8Tn2a-M8TTH_lWmFeHpCb_YrXtcYWpwFEUWrPRCNaNNVLDCHTj0ssj-N0twARtNUMroasuJjteXK1Q19TmsksrjxOW1r74zGQHSUioCGmFkrztMEoX0FFlJT4rycWfngpV1VpfmFXgudx1fvt1IapPypoXI6nIRd2GXNAuOlO3DSlQZpIuhcA2OTZLO6u23DKr5aVfY0cZdhj9OZGH4wnn32jCfFKBkJEpB3e0ADF2_5_x1oYqIxq2W6oS-MrlGMRHw1msJT1hn0acnBNwEhAjPD2RCLe6LP4bAExEgTXW3bCsNl_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5493f0e659.mp4?token=VL-vYg50qGobBL0jEBzhisZ7R6dni2v-1SK8Tn2a-M8TTH_lWmFeHpCb_YrXtcYWpwFEUWrPRCNaNNVLDCHTj0ssj-N0twARtNUMroasuJjteXK1Q19TmsksrjxOW1r74zGQHSUioCGmFkrztMEoX0FFlJT4rycWfngpV1VpfmFXgudx1fvt1IapPypoXI6nIRd2GXNAuOlO3DSlQZpIuhcA2OTZLO6u23DKr5aVfY0cZdhj9OZGH4wnn32jCfFKBkJEpB3e0ADF2_5_x1oYqIxq2W6oS-MrlGMRHw1msJT1hn0acnBNwEhAjPD2RCLe6LP4bAExEgTXW3bCsNl_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدان برای ایران تا پای جان در خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454917" target="_blank">📅 23:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454916">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0f07184e.mp4?token=v1LB4kjmtToto988_zPHWVvubwUQHXu2u7-Bf7W6LJS_jfaWsTB9RXbWAiGubZ6jhd1L5zI_nrJJIgeEZTGmTQuVgcDLAM729u5fxPHYzpCjDIvnXs0oRkxq8UT_FnzwOHY0lFuADqKImqSeM-1tC6s4wTy1AiTV232kiASd_KQ44m1E5WVBjDIR3RMRI_DhwXitkn-idG_2eGoxDtNMeVOIYmA2ZL_OhGw80BHkqmUKLy0BHhPQQ2oJ4J4IG8XWuRiWxG2bC8W9OO3ptPAFb5kcP1J4N57WAlPpyJa2FijOsgIY-iwtYalJfops-prUUqHIXBIRPEG_h96rBs7OFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0f07184e.mp4?token=v1LB4kjmtToto988_zPHWVvubwUQHXu2u7-Bf7W6LJS_jfaWsTB9RXbWAiGubZ6jhd1L5zI_nrJJIgeEZTGmTQuVgcDLAM729u5fxPHYzpCjDIvnXs0oRkxq8UT_FnzwOHY0lFuADqKImqSeM-1tC6s4wTy1AiTV232kiASd_KQ44m1E5WVBjDIR3RMRI_DhwXitkn-idG_2eGoxDtNMeVOIYmA2ZL_OhGw80BHkqmUKLy0BHhPQQ2oJ4J4IG8XWuRiWxG2bC8W9OO3ptPAFb5kcP1J4N57WAlPpyJa2FijOsgIY-iwtYalJfops-prUUqHIXBIRPEG_h96rBs7OFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانه گرگانی‌ها به ایستگاه ۱۶۰ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454916" target="_blank">📅 23:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454915">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgEU3LdNIb00ycbQb3zXlQXbalvCv-6k0Wt70hL2ar6j5ouGxUo1g9u7ZSUT2jQJE6OJQn_bW35BG3-hAPP26TAQQeSGRjCh0GDRFPnhnCJnAHPRQnwGtm3sZgMpPd1JgJJVuk9dfOoM_NO9CVTQ_yhN3vuD4zkYFLIPHb-j7YGUhSa1SHctkUgiQnyARpUPyXi8ieavEM_rRrPQUbMk6S7V4Qtp5SUjxD5kXhMzmBV7RNizCw2TLDlJ3pIrwHPRzGy_cLYETHfsw06msWGja4ZBhq0anJXCFp5shraYLD1KZAkB7F0763Lt5bZI3AK3l0PKCWvZ2KEN3dPt2jf74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: ملت بعثت‌یافته ایران تا استیفای حقوق خود از میدان خارج نمی‌شود
🔹
ملت بعثت‌یافته ۱۶۰ روز است که علی‌رغم همه دسیسه‌های دشمن، در میدان حضور دارد؛ این ملت تمام‌قد در مقابل دشمنان ایستاده و تا استیفای حق و حقوق اساسی و مواجهه با ظلمی که دشمن بر او روا داشته از پای نخواهد نشست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454915" target="_blank">📅 23:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454914">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
خون تاکستان برای وطن و مقاومت می‌جوشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454914" target="_blank">📅 23:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454913">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G03ZtnizsgVjz6QdJHmNFhVFSt-ptkDLu6Tv4ISmOoqDGt7sl3J42qgv0vM-vhXd6foUBpltFj-FPCFzX0ReOUgppR2JkcewU4h3VQlLS3oXeBOygkrmfZ9Vdu6iAo3lX0G3pDowWN03dPzUfAadxA6jnk11Z8En62KNYzHFQUkQu3oYohCJo7AeR5NRDDMHJmdvaiQ7db2zZ8fOOvjoM9I6uNLkOVe4JMxeULaGw2jsrinabyvuelwew5dUzw7NB07NAj6Q5b_4m0r-0rqZDp9zPeZNEYuQJMcoMP1iqIdPqIck0dF_gCemwmbdBABh5J7O1pbJYGUgoL0xpsO_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق مکه؛ ائتلافی برای نجنگیدن
🔹
عربستان سعودی، پاکستان و ترکیه امروز جمعه ۱۶ مرداد در مکه سندی امضا کردند که از آن با عنوان «توافقنامه دفاع مشترک مکه» یاد می‌شود. مهم‌ترین بند این سند، بر اساس بیانیه مشترک سه کشور، «اصل دفاع جمعی» است؛ به این معنا که هرگونه حمله مسلحانه به یکی از سه عضو، حمله به هر سه تلقی خواهد شد.
🔹
اما اولويت‌ها، سازو کار تصمیم‌گیری در سه کشور، تجهیزات و خلأهای فنی در توافق، تا حدی است که هرگز فرمان نبرد مشترک صادر نخواهد شد.
بیشتر بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454913" target="_blank">📅 23:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454912">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b4eca2cdf.mp4?token=TwSAKdydJruNPXwWf0e_fOp70zEIBe2_NR1bMf6PeW30T0MQutYEhgCaeHKHiUTT3p0gBDs-_Xg-vmRZRxmLkLQqAxNNMM-KNpSw6POU93gP8NAc6fzVa9RCTvN-TnMTquiksD2o4A40NFVUOsrM_lAwLs559FaYGP1w-OJeXLwvFpveuoWCPrrwpwt9K9N7TZRgEDDVwEoZ4uBYboGjL_K2r52FmaoldLIHHl_UZ6n9rIRNs5UxlyplAl3hboyaBUMy6YOnC2twJGHA-Jh20XGEInuxBS-KPtYN0Nm-HfQp-EevgJBp-ldRsDSiLjHu5ehlrRxkbMveifslIeKRxKC-3LeaxAUFOZsPBFuC8wZNhQTHm8_5396zpma6c0cUiV-smlMWZYMfrB-Wgd5mu56qoxhD5VupecdQmqzYAkvKbyuKqB8i3ZnU5XEZJ9emuNyrxTNqG4mVRCU_KEpy1C6ArShT6Gvv4ZR2rbnjQBZbubQSSoFLsmlqmN6QL6CcRvdso3Pyw0q8v_xgrCd0HtI_C9FuDj9casSdclX93gTwWpPzUb5tia546zGZ68GgTAohNGkOlKhYPtq417PVDIpGdj0OVvR6M4kwy0PoSugx5sNGWNqpxzwSTOQMN3pu8o7rCJe4iD0L3Vf5kMSmDal95vQ7hLPQY7nTtR7klIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b4eca2cdf.mp4?token=TwSAKdydJruNPXwWf0e_fOp70zEIBe2_NR1bMf6PeW30T0MQutYEhgCaeHKHiUTT3p0gBDs-_Xg-vmRZRxmLkLQqAxNNMM-KNpSw6POU93gP8NAc6fzVa9RCTvN-TnMTquiksD2o4A40NFVUOsrM_lAwLs559FaYGP1w-OJeXLwvFpveuoWCPrrwpwt9K9N7TZRgEDDVwEoZ4uBYboGjL_K2r52FmaoldLIHHl_UZ6n9rIRNs5UxlyplAl3hboyaBUMy6YOnC2twJGHA-Jh20XGEInuxBS-KPtYN0Nm-HfQp-EevgJBp-ldRsDSiLjHu5ehlrRxkbMveifslIeKRxKC-3LeaxAUFOZsPBFuC8wZNhQTHm8_5396zpma6c0cUiV-smlMWZYMfrB-Wgd5mu56qoxhD5VupecdQmqzYAkvKbyuKqB8i3ZnU5XEZJ9emuNyrxTNqG4mVRCU_KEpy1C6ArShT6Gvv4ZR2rbnjQBZbubQSSoFLsmlqmN6QL6CcRvdso3Pyw0q8v_xgrCd0HtI_C9FuDj9casSdclX93gTwWpPzUb5tia546zGZ68GgTAohNGkOlKhYPtq417PVDIpGdj0OVvR6M4kwy0PoSugx5sNGWNqpxzwSTOQMN3pu8o7rCJe4iD0L3Vf5kMSmDal95vQ7hLPQY7nTtR7klIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی بروجردی‌ها در شب ۱۶۰: لشکر با ابهت لرستان، گوش به فرمان امام زمان(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454912" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454911">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572a4348e0.mp4?token=j0xSHqYcarGbLELLUEneP4WmvrmSRY85nlgErprl_fhAwzIrx3HEOwpMBwAw6x-xerHFOfREGA7G6khNcTcesoQjHMQlQYtk8O9gMAdmJvjGYrg31oJ7UeTkUOed0NVCfitxgHOUpID3KczrKAo5uFLHX_WS78vrmRT6_ijQQwFkhOoSJ9f9HQgs0m_Wo7pbKIOeKMK9LzcGG6qt-AHd5sFkhfU5BSofrdygl4G8yQ2x1ZRE-ab9q5fSuNE7cHci5_AxxRlHT8RgXka1pG_e8JdJbTqq3vdVVvw-dlN1LE2yKVw0lzM_8FbYUm3efno35lZ2Rkn0ieTszrgcr2VAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572a4348e0.mp4?token=j0xSHqYcarGbLELLUEneP4WmvrmSRY85nlgErprl_fhAwzIrx3HEOwpMBwAw6x-xerHFOfREGA7G6khNcTcesoQjHMQlQYtk8O9gMAdmJvjGYrg31oJ7UeTkUOed0NVCfitxgHOUpID3KczrKAo5uFLHX_WS78vrmRT6_ijQQwFkhOoSJ9f9HQgs0m_Wo7pbKIOeKMK9LzcGG6qt-AHd5sFkhfU5BSofrdygl4G8yQ2x1ZRE-ab9q5fSuNE7cHci5_AxxRlHT8RgXka1pG_e8JdJbTqq3vdVVvw-dlN1LE2yKVw0lzM_8FbYUm3efno35lZ2Rkn0ieTszrgcr2VAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با گفت‌وگو توانستیم جنگ لبنان را متوقف کنیم، محاصره را برداریم و برخی تحریم‌ها را کاهش دهیم.
🔹
عده‌ای می‌خواهند بجنگیم؛ همان چیزی که اسرائیل می‌خواهد تا ما را وادار به تسلیم کند.
🔹
ما کوتاه نخواهیم آمد و سر تعظیم فرود نخواهیم آورد. @Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454911" target="_blank">📅 23:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454910">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5abfce3af6.mp4?token=VCCY4O30Z7ha1yhCt6SEoNtqBpTGYY7mX_7SLATHyVr92Rkw_DC4a8SA7D-hEl2lM9YkkAgvnXGo51yhdPTGrkhaVcM2nSkvUX7qVvbdb4_g7BSUj7E3KjLVMeTPHhom58cHjw2ooMKH2KFnmWw1yER8W_YTgN5vWBR3P3QpGl0tQOdkfgfg2fWqZPxVBKHsTiNe8jeDxoZCSLA-JLg6sTLR7OBAp4VEC0iqyqb5vX8g236fH4rXxeXjjcexlFyaOnguruzntYZ5ghXxjQCmtic9cMPKcTTFDdPLTmOl_txcZhxfTVCp4OZY6LE5Y4Tlmnawkdd3vwsv8L2SKzcSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5abfce3af6.mp4?token=VCCY4O30Z7ha1yhCt6SEoNtqBpTGYY7mX_7SLATHyVr92Rkw_DC4a8SA7D-hEl2lM9YkkAgvnXGo51yhdPTGrkhaVcM2nSkvUX7qVvbdb4_g7BSUj7E3KjLVMeTPHhom58cHjw2ooMKH2KFnmWw1yER8W_YTgN5vWBR3P3QpGl0tQOdkfgfg2fWqZPxVBKHsTiNe8jeDxoZCSLA-JLg6sTLR7OBAp4VEC0iqyqb5vX8g236fH4rXxeXjjcexlFyaOnguruzntYZ5ghXxjQCmtic9cMPKcTTFDdPLTmOl_txcZhxfTVCp4OZY6LE5Y4Tlmnawkdd3vwsv8L2SKzcSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کلیات توافق نهایی شده بود و برای افزایش اعتبار آن، قرار بود امضای نهایی از سوی ترامپ انجام شود تا امکان عقب‌نشینی از توافق وجود نداشته باشد.
🔹
اما کمتر از ۲۴ ساعت بعد، روند مذاکرات به‌طور کامل تغییر کرد و توافق به سرانجام نرسید. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454910" target="_blank">📅 22:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454909">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d007d8a7.mp4?token=VF_-TTtC0wW0vVuBfIhQXdIZ058iF1Cq2nFy1OZ6DsPbFWboKJlN6inlplVZeeVqcHK6Ih3HFfbl-KAHGVRK-pu6sP-MdHkqRQZqcL6vAdi53_hhCFNLzxx2HkceczCb6TbWRzKMJEaXML4dgWx-f8ltcm1wdrCsEWd4NQwZFfw_w8l2f-vwlwGTUv7fsXZmL1Zmo3P9br6Ip5E0KKbDt8pF6GyU_WC3fnUwV83as4xbfE0P_cQyixfmlRUZnYQTHJxdsi5efIe6WU3mxZavmPslxUmltYHmaxab06aCAM8dr5_EdpBa8yhTvoYRZiL6GG8ENEEKKCM4rHZu0ALGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d007d8a7.mp4?token=VF_-TTtC0wW0vVuBfIhQXdIZ058iF1Cq2nFy1OZ6DsPbFWboKJlN6inlplVZeeVqcHK6Ih3HFfbl-KAHGVRK-pu6sP-MdHkqRQZqcL6vAdi53_hhCFNLzxx2HkceczCb6TbWRzKMJEaXML4dgWx-f8ltcm1wdrCsEWd4NQwZFfw_w8l2f-vwlwGTUv7fsXZmL1Zmo3P9br6Ip5E0KKbDt8pF6GyU_WC3fnUwV83as4xbfE0P_cQyixfmlRUZnYQTHJxdsi5efIe6WU3mxZavmPslxUmltYHmaxab06aCAM8dr5_EdpBa8yhTvoYRZiL6GG8ENEEKKCM4rHZu0ALGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از قالیباف خواهش کردیم که رئیس تیم مذاکره‌کننده شود
🔹
همکاری و هماهنگی میان دولت، مجلس، قوه قضائیه و نیروهای مسلح، عامل اصلی عبور از شرایط سخت بوده است.
🔹
بی‌احترامی و تفرقه، خواستۀ دشمن است و باید با همدلی و احترام با یکدیگر رفتار کنیم. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454909" target="_blank">📅 22:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454908">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825ae52635.mp4?token=gUGHxtXtAbKVwyYf2BHkUVx_lFf6dAkZiFrwBJa-gYvjFwafKOnn57HPlyi5ERoKgKsIznMiL_dbVX3j1Nz7CU9edqiRVLjIQ-au2UtMVzrWTcUtli27fNLmlUjZSA1KIg3iHXnLhIGNxjFwcNcz_5KSwO4B7jQkZHoW9BTiIPHFiDClR_MD-qzctliMes5IoHn38Sz7bJLp9q3THpLw9EohPyTqhjfG3-0e01-tZuVNt4_FqE4elDe5RF-Z-c1J8d5Yzcpm6CUuEbuPt5mI8-uTcWWrDGaKtietampeqrloSkoKPMnPhFJRy92d5zHNuVz38SFX0vGD03sgd3RQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825ae52635.mp4?token=gUGHxtXtAbKVwyYf2BHkUVx_lFf6dAkZiFrwBJa-gYvjFwafKOnn57HPlyi5ERoKgKsIznMiL_dbVX3j1Nz7CU9edqiRVLjIQ-au2UtMVzrWTcUtli27fNLmlUjZSA1KIg3iHXnLhIGNxjFwcNcz_5KSwO4B7jQkZHoW9BTiIPHFiDClR_MD-qzctliMes5IoHn38Sz7bJLp9q3THpLw9EohPyTqhjfG3-0e01-tZuVNt4_FqE4elDe5RF-Z-c1J8d5Yzcpm6CUuEbuPt5mI8-uTcWWrDGaKtietampeqrloSkoKPMnPhFJRy92d5zHNuVz38SFX0vGD03sgd3RQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هرگز استعفا نداده‌ام و نخواهم داد  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454908" target="_blank">📅 22:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454907">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf3016833.mp4?token=ugGHjwgA0XFwtAZGFlhOrzyxrz-ClFPwaFcyVkdKDgkpSS57D81bRTi8puWmY8iIPvg97bPbAwW2ovhAD2KW8e2uihHDFzUuEoJGwSJLUQ_fZ4jhWM3HWnnjh52I6icaPP2SqOVYml7prIQDei-VP473-MI6z87sQe5muj8laurb1b4Rw6sT-wTFouAFGuJTIXFy794fB6ZYIvmi8gm9vVanc4adSig5qVbgRC5cfm2BIm5m5RiUjOglX4HePDjkdReB1aUaBkWTq2ZvmGPxSnB2N4ID5ZQ7evBuBv5pNDLCZZsyG16o3D4gtSGiKEFcpGDRjfSTerWBDsHEEjof1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf3016833.mp4?token=ugGHjwgA0XFwtAZGFlhOrzyxrz-ClFPwaFcyVkdKDgkpSS57D81bRTi8puWmY8iIPvg97bPbAwW2ovhAD2KW8e2uihHDFzUuEoJGwSJLUQ_fZ4jhWM3HWnnjh52I6icaPP2SqOVYml7prIQDei-VP473-MI6z87sQe5muj8laurb1b4Rw6sT-wTFouAFGuJTIXFy794fB6ZYIvmi8gm9vVanc4adSig5qVbgRC5cfm2BIm5m5RiUjOglX4HePDjkdReB1aUaBkWTq2ZvmGPxSnB2N4ID5ZQ7evBuBv5pNDLCZZsyG16o3D4gtSGiKEFcpGDRjfSTerWBDsHEEjof1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ دولتی به اندازۀ ما در جهت سیاست‌های رهبری قدم برنداشت
🔹
اینکه عده‌ای اختلاف‌سازی کنند و القا کنند رهبری چیزی می‌گویند و دولت چیز دیگری، هم در حق رهبری جفاست و هم در حق دولت. @Fasrana</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454907" target="_blank">📅 22:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454906">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f3ea9adb1.mp4?token=RajI1-zAK574rGOLYn8M12b7AuEqz-BFzBi9qrn8YLSYGx392S-9Z-vpti-N_o7ADxRxzjnwAj_OXw_yUH486OqLG0s8t5CX69mmDCDcT9dnqtdb9OlEbAGFvT_0iJ5uIYZEb3u8MAgwX_noMKuG0OpM4e1fFOnfQGayKzuscyjYuVt55F-hw3CBTIKa0ip1Y_A7Pju9ukiU4xdnxYs3FzvlJcJ2yQoYs0kQjM-03WnJXiAFMCgBEXZGSyOGYa6hZUn7EbZJR3ZycSqqOoUuH2sxW6J1DrNpuf90422k4yOCC60AAUcz_zMp8cUJnIT815Uwlu3fFgfN3IHXrf_pyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f3ea9adb1.mp4?token=RajI1-zAK574rGOLYn8M12b7AuEqz-BFzBi9qrn8YLSYGx392S-9Z-vpti-N_o7ADxRxzjnwAj_OXw_yUH486OqLG0s8t5CX69mmDCDcT9dnqtdb9OlEbAGFvT_0iJ5uIYZEb3u8MAgwX_noMKuG0OpM4e1fFOnfQGayKzuscyjYuVt55F-hw3CBTIKa0ip1Y_A7Pju9ukiU4xdnxYs3FzvlJcJ2yQoYs0kQjM-03WnJXiAFMCgBEXZGSyOGYa6hZUn7EbZJR3ZycSqqOoUuH2sxW6J1DrNpuf90422k4yOCC60AAUcz_zMp8cUJnIT815Uwlu3fFgfN3IHXrf_pyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تفاهم‌نامه آتش‌بس با هماهنگی، تفاهم و همدلی در شورای امنیت ملی شکل گرفت
🔹
ما با نیروهای نظامی کاملاً هماهنگ هستیم و پشتیبانی از آنان را وظیفه خود می‌دانیم.
🔹
کسانی که جانشان را کف دست گرفته‌اند و از این کشور دفاع می‌کنند، مگر ممکن است میان ما و…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454906" target="_blank">📅 22:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454905">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92096f3d23.mp4?token=T1EqFAWQ6N9R0p6yjUIQDGCOtKDqWZpVSpjs8ZGGgaI8_9LF8VZcPIJ6IzvKyGnrqGwjFY9mulj4VZCvG0VC_pAiCTYJ4HvYYBd32GEcjLrZ_YkVWKLM-FMv_1XNv-__soazQn03KtdS8MMJDU72e7i4GMLO52XE_c590BMaIIWGl-D-fXFi5q6OdleCflTsa8OthRtxl3hJI62KsrK15_Q_vRxtRFfeFcpnzFec2EuZjIxkj1jI-Pb2C5aiQoiqisZAnyZ26RryG2lF2Jn4bBRw6hxEjvU5EsT-UsM5IUv0ucAjW1z0U39GG3w3nQKdVBFLGe2gEZB-joqDsgSwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92096f3d23.mp4?token=T1EqFAWQ6N9R0p6yjUIQDGCOtKDqWZpVSpjs8ZGGgaI8_9LF8VZcPIJ6IzvKyGnrqGwjFY9mulj4VZCvG0VC_pAiCTYJ4HvYYBd32GEcjLrZ_YkVWKLM-FMv_1XNv-__soazQn03KtdS8MMJDU72e7i4GMLO52XE_c590BMaIIWGl-D-fXFi5q6OdleCflTsa8OthRtxl3hJI62KsrK15_Q_vRxtRFfeFcpnzFec2EuZjIxkj1jI-Pb2C5aiQoiqisZAnyZ26RryG2lF2Jn4bBRw6hxEjvU5EsT-UsM5IUv0ucAjW1z0U39GG3w3nQKdVBFLGe2gEZB-joqDsgSwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا از سرزمین کشورهای منطقه به ما حمله می‌کند و ما باید از خود دفاع کنیم
🔹
مبدأ حمله به مدرسۀ میناب در یکی از کشورهای مسلمان بود.
🔹
دشمن از پایگاه‌های آمریکا در برخی کشورهای منطقه علیه ایران استفاده کرد و ایران ناچار به دفاع از خود شد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454905" target="_blank">📅 22:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454904">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edbd6dc5c.mp4?token=REQJ_IvbXmCvvOEpI1aD7UgiH7vVGKYf2Rp_NzGn5iXUEl61g95C6ziXhVGQsIRZUn5RNufidNyAiq-fZzaktJEsjOq2pUF6JA7R_U2I_PVlYGPFrZux29Abmcub4Kbk3PhwPjHprqzkevpYt6s2uOICVx_A4aFRAUvJSoU96JBMt4S_CE-wGklxJST4hhxrY3M89VDsRiJzf-yN6aU4rUG37pHbkQ0AxhaElLoHP0yfuQ1--5MlHFWzVwubAU2tmRXR1ezmQggB7ImITGKlm5W0Pu7XHakJ77Lc2bCXQ6Q3GFzV5HWDJa60R3nqTbnDfNcbUd_7LP9yxT6Zv3G7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edbd6dc5c.mp4?token=REQJ_IvbXmCvvOEpI1aD7UgiH7vVGKYf2Rp_NzGn5iXUEl61g95C6ziXhVGQsIRZUn5RNufidNyAiq-fZzaktJEsjOq2pUF6JA7R_U2I_PVlYGPFrZux29Abmcub4Kbk3PhwPjHprqzkevpYt6s2uOICVx_A4aFRAUvJSoU96JBMt4S_CE-wGklxJST4hhxrY3M89VDsRiJzf-yN6aU4rUG37pHbkQ0AxhaElLoHP0yfuQ1--5MlHFWzVwubAU2tmRXR1ezmQggB7ImITGKlm5W0Pu7XHakJ77Lc2bCXQ6Q3GFzV5HWDJa60R3nqTbnDfNcbUd_7LP9yxT6Zv3G7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ امتیازی در تفاهم‌نامه ندادیم
🔹
می‌گویند آمریکا به تعهداتش عمل نمی‌کند؛ تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454904" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454903">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a5fb3640.mp4?token=cLqztr4VraG38VBaD6NRpMPq10Z50N0CJR8aBumJ-j7D-XbP0-j6uDluwLTguMI5Cf5aDYfu-yFyukuhcQKyf4Hm6UGQglsnWjk2vc2YuiQlqAAocx6v94smitZsj8V2O7F5T2XAfJ1Mb8kEciRO1VD2xH9ukYlje2hlV-B110O2L7TW2OOSFxrGN_TAuH_T80Q8IM5mirneC-uAVOuUnkyXmtOLVV8KsO-sLwUyQOUJjZDzSUFMhdEDWRv2mN5sKLBhxbghyvk2NSAQmNPUvXXJxzsjbl-tBO7sB1YhI5kuxZyXyXzhy9QqxThR3YiYwoOP5KMicW5MWpdMOwRwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a5fb3640.mp4?token=cLqztr4VraG38VBaD6NRpMPq10Z50N0CJR8aBumJ-j7D-XbP0-j6uDluwLTguMI5Cf5aDYfu-yFyukuhcQKyf4Hm6UGQglsnWjk2vc2YuiQlqAAocx6v94smitZsj8V2O7F5T2XAfJ1Mb8kEciRO1VD2xH9ukYlje2hlV-B110O2L7TW2OOSFxrGN_TAuH_T80Q8IM5mirneC-uAVOuUnkyXmtOLVV8KsO-sLwUyQOUJjZDzSUFMhdEDWRv2mN5sKLBhxbghyvk2NSAQmNPUvXXJxzsjbl-tBO7sB1YhI5kuxZyXyXzhy9QqxThR3YiYwoOP5KMicW5MWpdMOwRwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ امتیازی در تفاهم‌نامه ندادیم
🔹
می‌گویند آمریکا به تعهداتش عمل نمی‌کند؛ تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454903" target="_blank">📅 22:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454902">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25623b3011.mp4?token=a_IbnyLuDDalGMDUSFsEFQ0xE3VVW9JvzkhqUwJdsQdgNsJpVwQHumr-qQaUGA8q3TUB_7dC41oEdTBaI0B6xNTi6LDu2sKTE2R8nHVcmlEez2IbSX2U7ibS4bCJK0-nm9Skyk9spohbZRF5gxgf348M2mFf81GVNsGKhJLm3R6Ky7C_47tbrBUHQuRv1c-XEF09vBh_R8e89xRSvwVNVu77IjK9g82twXRCm8kpWKK1X_paxviBtHimSMTQ4nWg2JzabISH0SzzNxvViD3VXn6qFZfPPrXDyXWHjP37pzAaXMmo_E9RmTD9-RhwbzSaqJowr_stXMOU537dSc9jZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25623b3011.mp4?token=a_IbnyLuDDalGMDUSFsEFQ0xE3VVW9JvzkhqUwJdsQdgNsJpVwQHumr-qQaUGA8q3TUB_7dC41oEdTBaI0B6xNTi6LDu2sKTE2R8nHVcmlEez2IbSX2U7ibS4bCJK0-nm9Skyk9spohbZRF5gxgf348M2mFf81GVNsGKhJLm3R6Ky7C_47tbrBUHQuRv1c-XEF09vBh_R8e89xRSvwVNVu77IjK9g82twXRCm8kpWKK1X_paxviBtHimSMTQ4nWg2JzabISH0SzzNxvViD3VXn6qFZfPPrXDyXWHjP37pzAaXMmo_E9RmTD9-RhwbzSaqJowr_stXMOU537dSc9jZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیر بار زور نمی‌رویم، اما به‌دنبال جنگ و تجاوز هم نیستیم
🔹
ایران به‌دنبال جنگ یا توسعه‌طلبی نیست و تنها از توان دفاعی و امنیت خود حفاظت می‌کند؛ اگر فشار و تهدید علیه ایران متوقف شود، دلیلی برای ادامه تنش وجود نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454902" target="_blank">📅 22:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454901">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab394bfe.mp4?token=Mko1jy5Ud7wFcuQc6e5EqyqYHhtLUcngUcZpkeieuUCIaBE_OceOCJX5bSZT2xyMOa14IkW17dEvp5HtwB_5-8PPo5_q_2DwoD1floE2MRfyrqEAWQaz4gVHzHiffB6G3nyBMNUF5J-4XuS8_THyE2zfbLl_q11oNjvFTyWksR5CZzPIDHKNRmRL0E4tkAjqCF7ljQ-yYdavUBEQAAxGvDf9zEZa5Nx63Lmk4BfM5HYXWt9TRO30twgAGazKHQmmbfoIqiTEtH8-Guy43b_9gEceXsf6eWjuFn_Bk60Rosc7ugze7EBzL9ii8M-JlUrctKhlfTU5lty7d0UxVocNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab394bfe.mp4?token=Mko1jy5Ud7wFcuQc6e5EqyqYHhtLUcngUcZpkeieuUCIaBE_OceOCJX5bSZT2xyMOa14IkW17dEvp5HtwB_5-8PPo5_q_2DwoD1floE2MRfyrqEAWQaz4gVHzHiffB6G3nyBMNUF5J-4XuS8_THyE2zfbLl_q11oNjvFTyWksR5CZzPIDHKNRmRL0E4tkAjqCF7ljQ-yYdavUBEQAAxGvDf9zEZa5Nx63Lmk4BfM5HYXWt9TRO30twgAGazKHQmmbfoIqiTEtH8-Guy43b_9gEceXsf6eWjuFn_Bk60Rosc7ugze7EBzL9ii8M-JlUrctKhlfTU5lty7d0UxVocNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: شکافی بین دولت و نیروهای مسلح نیست
🔹
دفاع جانانه نیروهای مسلح با پشتیبانی مردم و هماهنگی همه بخش‌ها، محاسبات دشمن را برهم زد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454901" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454900">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876ed831cb.mp4?token=EHtyNEQeRM9zUAsCO0E1qhvXcxEhtBXac_QaP8ICfLOGa-s9tPdvEp_mcglmfp7JumHbhbYksBW7cLUlwRq5hVNiFUVxjL8C-dRhQiDwpARYZW2HVXeQgOHdbA0kqD90Rnpzc9ZK9zy-QAtkUZl1FiN21uZtqx497p3mcDsNIUowmVX6NdczAUmsExmc9TSAj_E-R6Gzh_jBkkERjnTdpo1SQB_F9gNsPl0-uQp6OvcSbt3wPRPAzBypJ-cVhvRysQ_RWwl4eCHxEOg7BQJ53qc71uKi7CqwLBI1O9ax5hF7Ab2kQqicWrrPBw3rriE-Aq6NsaZ6o4n-p5v-wuHOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876ed831cb.mp4?token=EHtyNEQeRM9zUAsCO0E1qhvXcxEhtBXac_QaP8ICfLOGa-s9tPdvEp_mcglmfp7JumHbhbYksBW7cLUlwRq5hVNiFUVxjL8C-dRhQiDwpARYZW2HVXeQgOHdbA0kqD90Rnpzc9ZK9zy-QAtkUZl1FiN21uZtqx497p3mcDsNIUowmVX6NdczAUmsExmc9TSAj_E-R6Gzh_jBkkERjnTdpo1SQB_F9gNsPl0-uQp6OvcSbt3wPRPAzBypJ-cVhvRysQ_RWwl4eCHxEOg7BQJ53qc71uKi7CqwLBI1O9ax5hF7Ab2kQqicWrrPBw3rriE-Aq6NsaZ6o4n-p5v-wuHOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در جریان مذاکراتی که با فرانسه برای لغو اسنپ‌بک شکل گرفته بود به تفاهم رسیده بودیم اما آمریکا نگذاشت.
🔹
اروپایی‌ها اختیاری برای تصمیم‌گیری ندارند. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454900" target="_blank">📅 22:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454899">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293aa3d819.mp4?token=XE6_HUX_0Ws0WQOpWHVBGIBMOmE4sg9Qf2_RX1lLYetgNT_6n7fm1wMX93smj0MK2O1E36Kjg34sO32wY25e-2Wt-7sCSqjLooJ1A-pqtDjGK1c5uSrmqVFt9ywyiZcaTibH9t8hyjG-DKp5EXo_YLn7ruE8nfZhN3UxdebV9cWDKFZfX3_DEV6I1OtLxmb-c8Eom1THH8efYgE0CKkbF3aiq6cthsYQGM1R2KQBATFhQDYLEhvBs_eu_oHc_lPIjH_Aof84a7Vvw_0JPTf6j-2VjdajsO_Uz_gNFpQ8_1_HfJk90MIzZVEXCX8s2fX8devbH45gyJEsaCCWbjwgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293aa3d819.mp4?token=XE6_HUX_0Ws0WQOpWHVBGIBMOmE4sg9Qf2_RX1lLYetgNT_6n7fm1wMX93smj0MK2O1E36Kjg34sO32wY25e-2Wt-7sCSqjLooJ1A-pqtDjGK1c5uSrmqVFt9ywyiZcaTibH9t8hyjG-DKp5EXo_YLn7ruE8nfZhN3UxdebV9cWDKFZfX3_DEV6I1OtLxmb-c8Eom1THH8efYgE0CKkbF3aiq6cthsYQGM1R2KQBATFhQDYLEhvBs_eu_oHc_lPIjH_Aof84a7Vvw_0JPTf6j-2VjdajsO_Uz_gNFpQ8_1_HfJk90MIzZVEXCX8s2fX8devbH45gyJEsaCCWbjwgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با امر و نهی نمی‌توان جامعه را به درستی اداره کرد  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454899" target="_blank">📅 22:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454898">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cda7947ea.mp4?token=a1DBQegfcOvTrzk24vLw8BKnnzNZP31Vbl4VntSpoR51XZVNwv3qlwuAe-_KSgw4Ff9IdLsynV_LYkS0QCw-J7tIU474j5r8tG5FZ3TIQ7SXiqdvPKxn1aS4YJfEgIBTw3sb6oBFTVPI5OYVdeYSs0WyGB1DqZSwtiIB8yF-NHw3jRCr9_Ei4QAfid-WNSzoN5H-XqMd6zfzlQB1cccK3au_bCy_Asa4-D37ekEwFpCbjubJBdLdkX5QFIigCHCtUiZKB36-GfUXCVPWscgHrZL0V034A4QUn-xJ0rNVrxb9F3W1-SvYRF5OhsrNuVHw0lRHouEC2VnzOY4frVoqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cda7947ea.mp4?token=a1DBQegfcOvTrzk24vLw8BKnnzNZP31Vbl4VntSpoR51XZVNwv3qlwuAe-_KSgw4Ff9IdLsynV_LYkS0QCw-J7tIU474j5r8tG5FZ3TIQ7SXiqdvPKxn1aS4YJfEgIBTw3sb6oBFTVPI5OYVdeYSs0WyGB1DqZSwtiIB8yF-NHw3jRCr9_Ei4QAfid-WNSzoN5H-XqMd6zfzlQB1cccK3au_bCy_Asa4-D37ekEwFpCbjubJBdLdkX5QFIigCHCtUiZKB36-GfUXCVPWscgHrZL0V034A4QUn-xJ0rNVrxb9F3W1-SvYRF5OhsrNuVHw0lRHouEC2VnzOY4frVoqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: خیلی از مشکلاتمان با کشورهای همسایه را برطرف کردیم اگرچه آمریکا و رژیم صهیونیستی با توطئه و جنگ اخیر به دنبال ایجاد اختلاف بین ایران و کشورهای حاشیه خلیج فارس هستند.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454898" target="_blank">📅 22:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454897">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993ce56811.mp4?token=b0BIkwOZh7ESWUg_76mBf9fj2elYYMLPggKwUFsPYEF97zmmtmBLT2VxlygNAgUzx6gEWn_aUqbpmw1IeUmmpjvLKcSyiAtj3lADFMFRvs5BMqt-cF7hBjKMHExig-jUU5MzZGKV8cF35Lgrg4ybYp6JtC0mE6Sa-RNrJHNcnnBCQ0KSgKKjQ3TFgtWgXGLnPhB30pruDNOa3BgO_vjg6J6dnEKkyikb-RW7ku4sBKgt7JDFUlc5qt94EVx_SMqMNwgtQdSNZS7K2X7KRG8B7BHrOhYVTHG3thcN1u1pDxGJOH8VGv3Gtc-PWtvitaGYNxmR0_wghHaKzo3mPKqk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993ce56811.mp4?token=b0BIkwOZh7ESWUg_76mBf9fj2elYYMLPggKwUFsPYEF97zmmtmBLT2VxlygNAgUzx6gEWn_aUqbpmw1IeUmmpjvLKcSyiAtj3lADFMFRvs5BMqt-cF7hBjKMHExig-jUU5MzZGKV8cF35Lgrg4ybYp6JtC0mE6Sa-RNrJHNcnnBCQ0KSgKKjQ3TFgtWgXGLnPhB30pruDNOa3BgO_vjg6J6dnEKkyikb-RW7ku4sBKgt7JDFUlc5qt94EVx_SMqMNwgtQdSNZS7K2X7KRG8B7BHrOhYVTHG3thcN1u1pDxGJOH8VGv3Gtc-PWtvitaGYNxmR0_wghHaKzo3mPKqk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مساجد، مدارس، مراکز بهداشت و شهرداری‌ها پایگاه‌های عملیاتی هستند که دولت می‌تواند برای اجرای برنامه‌های خود در سراسر کشور از آن‌ها استفاده کند. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454897" target="_blank">📅 22:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454896">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d09c66ced.mp4?token=H0aFxPACBVKG-5FzcUhNtNbVNBf3aQCeqhZLjOAydiTBMhHMR0f9J4ZZSMITw8HN_AnV6-TBpbdNxy6BXHWpxtCffBcIXHJ6cYL0fZwx87eoXe1gBSIhaoRwK7KvKybg7zzPCQp70k7O1VGJ6dmdFFhTJUKHgF9HI71_yeX2xzkiG5KiFfoEj2diOFbDZI5tiX8oYc4WqprjVeLId9bquF-KUhTCkNgnVgPxJOmK6e-j2eRfNLuhAH54-tNGxWgeq9gV956V8uOw_sqXd9RIwclPD-c8nwUed9pY0JUdAufLEcvK0_ApxsgqRLEwPX4QQu2o4LbmR5fj5Q9PQyyuNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d09c66ced.mp4?token=H0aFxPACBVKG-5FzcUhNtNbVNBf3aQCeqhZLjOAydiTBMhHMR0f9J4ZZSMITw8HN_AnV6-TBpbdNxy6BXHWpxtCffBcIXHJ6cYL0fZwx87eoXe1gBSIhaoRwK7KvKybg7zzPCQp70k7O1VGJ6dmdFFhTJUKHgF9HI71_yeX2xzkiG5KiFfoEj2diOFbDZI5tiX8oYc4WqprjVeLId9bquF-KUhTCkNgnVgPxJOmK6e-j2eRfNLuhAH54-tNGxWgeq9gV956V8uOw_sqXd9RIwclPD-c8nwUed9pY0JUdAufLEcvK0_ApxsgqRLEwPX4QQu2o4LbmR5fj5Q9PQyyuNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با مشارکت خود مردم در محلات مشکلات نیازمندان را برطرف کنیم  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454896" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454895">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f4ea84f.mp4?token=P1NXQq6V_NlTXCpk_NpFYnGASziO4KSaOs4niIYoF8cwknbBuwUO9HkcCadnx_s6sghpW3Btidf4iD9SqsgLp9QNKfId-7wsm2jvgDIDTYN1-mp9j3V181hIb_lBsL5E_rIdkzZKNfSAH6RnjLkx4ioB2Ty8sX4dfSUQZWMYAHcq1CZOui9ohO3H3e4fP83ktFVvZHPBnJdAPaC00SsxPk3XboygAm-uzfCoT-NZXaA-RucviBEgPA679d3OYNO2q72h2f7QHqEVLS7qAIh5Q52KybLuGLaxLDLTUfOwVIWC5nBveadL_p7szBLWnzAzbeannQ8trBhHRx_U5roRIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f4ea84f.mp4?token=P1NXQq6V_NlTXCpk_NpFYnGASziO4KSaOs4niIYoF8cwknbBuwUO9HkcCadnx_s6sghpW3Btidf4iD9SqsgLp9QNKfId-7wsm2jvgDIDTYN1-mp9j3V181hIb_lBsL5E_rIdkzZKNfSAH6RnjLkx4ioB2Ty8sX4dfSUQZWMYAHcq1CZOui9ohO3H3e4fP83ktFVvZHPBnJdAPaC00SsxPk3XboygAm-uzfCoT-NZXaA-RucviBEgPA679d3OYNO2q72h2f7QHqEVLS7qAIh5Q52KybLuGLaxLDLTUfOwVIWC5nBveadL_p7szBLWnzAzbeannQ8trBhHRx_U5roRIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با مشارکت خود مردم در محلات مشکلات نیازمندان را برطرف کنیم
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454895" target="_blank">📅 22:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454894">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اعتراف شرکت نفت امارات: ۱۵ نفتکش‌مان منفجر شد
🔹
شرکت نفتی امارات، ادنوک فاش کرد که از ابتدای جنگ رمضان، ۱۵ کشتی این شرکت هنگام عبور از تنگه هرمز مورد حملۀ موشک و پهپاد قرار گرفته‌اند.
🔹
این شرکت تایید کرد در هفته گذشته ۳ کشتی مرتبط با این شرکت هدف قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454894" target="_blank">📅 21:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454893">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJshEFpq0ogYr7zZwbgl5UjXhj_pJKhGScy9lA41824jzh7CzbYBPQuzU0DOR9MayLYpT50JLZOokL7i1utw8cu9YIBYlH9ijK6DFuSXxmp4XskXlOrQ7mFjnRiU91MO4YcXAwgz869aeH0qw321i6q6GqJ2sAjJGCRH0bR445epd2v0e98nmCp7o2XaygMDIFrq0zrIz2iHVri75R8d-Plp8nYxgoNksbJ2dkJ6Kle1QTNtnlXDVMyuzNbrMsSf3ZqtG6XjZR1eTA82VVJWE3SOVhiAMViiSNec1texzfas1cNsBr_h6WPP59PIUM8e6mSOrFSYVxIR4vZ5G-HJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی خطاب به کشورهای همسایه: زمان آن رسیده که به خود متکی باشیم و برادری واقعی را درپیش بگیریم
🔹
نیروهای مسلح قدرتمند ایران، آمادگی، توانمندی و اقتدار خود را در برابر پیشرفته ترین نیروی نظامی جهان به اثبات رسانده‌اند.
🔹
هنگامی که مسلمانان در کنار یکدیگر متحد و یکپارچه باشند، می‌توانند در برابر هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، با قدرت و قاطعیت ایستادگی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454893" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454892">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b23c4b0f.mp4?token=YYKnkZHJ7ktIB9sN5BUI4nD3rTBW-r4D_gpKcXkxxZXe6tIco_rWx1g1fxDopMhGFd53EX78NaCRzfYkSJCPxWsFzHSBfvqzNhk9xJDdMrCcKTW2swu7QB5gOVktU73d6ImErfgw2ZDsxaqsCuhj6Gmo-RpMf18ou1HvFY2J0ApK54hFZawFLaPT7FwjGdkGk-LzKEjrxvUYJDe-ntqak05DEsZGnXPoJkj_jScQq7DyEGJQ2hiey23VRqyLHa77mhbDivcKf5lhWYnn15IexvBkx2qgLXnCn6UG3BfQTNt1gN5SuhRkhF6NMB2TZRv-EPWPV-ITvBox5NsoW3LrfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b23c4b0f.mp4?token=YYKnkZHJ7ktIB9sN5BUI4nD3rTBW-r4D_gpKcXkxxZXe6tIco_rWx1g1fxDopMhGFd53EX78NaCRzfYkSJCPxWsFzHSBfvqzNhk9xJDdMrCcKTW2swu7QB5gOVktU73d6ImErfgw2ZDsxaqsCuhj6Gmo-RpMf18ou1HvFY2J0ApK54hFZawFLaPT7FwjGdkGk-LzKEjrxvUYJDe-ntqak05DEsZGnXPoJkj_jScQq7DyEGJQ2hiey23VRqyLHa77mhbDivcKf5lhWYnn15IexvBkx2qgLXnCn6UG3BfQTNt1gN5SuhRkhF6NMB2TZRv-EPWPV-ITvBox5NsoW3LrfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۰ شب حضور فاروجی‌ها در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454892" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454891">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHJObbh5PV4x9XPltMIk3-M20YqOiNaQFuFUl0cvyvL7918D_bO3hrOHLt9sd93QhXwVLKpJIx2kHGp_V-50UQiX8lo-dqYDqIDdDRvKLhBkEORApItE4Zcez2eTgIOxq-9hRBSs831Y2m-pa7vJYpz132OOelBHSj0S1gWOutZKL1y7F1OwZ9OgNZTf5JZk_5mjjr3jbGaWlck4pKoN2bmZn3ko5PufxeNYLqe9WlvAVpRGeGPSROFbhkfYtu537jn2MQi-c3GBGDvQZJtyOUlTY4vK9w5SBFrjLHRFDSThHYbO5_pMU-xeLPKdk01WoV1tdXw0_EydS2RIHLgdow5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHJObbh5PV4x9XPltMIk3-M20YqOiNaQFuFUl0cvyvL7918D_bO3hrOHLt9sd93QhXwVLKpJIx2kHGp_V-50UQiX8lo-dqYDqIDdDRvKLhBkEORApItE4Zcez2eTgIOxq-9hRBSs831Y2m-pa7vJYpz132OOelBHSj0S1gWOutZKL1y7F1OwZ9OgNZTf5JZk_5mjjr3jbGaWlck4pKoN2bmZn3ko5PufxeNYLqe9WlvAVpRGeGPSROFbhkfYtu537jn2MQi-c3GBGDvQZJtyOUlTY4vK9w5SBFrjLHRFDSThHYbO5_pMU-xeLPKdk01WoV1tdXw0_EydS2RIHLgdow5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بازگشت یک زائر گم‌شده در سفر اربعین به ایران در برنامه پرچمدار
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454891" target="_blank">📅 21:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454890">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHNQ8olow8wQtzSflRxguDWb3_NPeJF2RteXxi0njo08_UaYUihwvTgRzQZfUqRWOzBrIrYS0qTHU0NPG9WzsNO78LgtlGylQGbYxmZK2p0o_bQChw8JZqnoR-fsRvCyZZpdjnxlM2gVRAiShkNPtMIpT4JroFviSZMcArJJOTBUVU7bESF1K9gmTlVEJnjP4FtpGCrhroHQkJa4GRSroZDglOCg6ePHMOX69UcETsv8Ndze3tChf97iojbahMcXMo_OffJdlEpWfOs3rN4tsDFyuK48TgEdH6Uig9SUsjpV7GrhquK1rDvTq-FYvzJrtg7a89NIR3b3d0Fv_DdLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت عراق به محکوم کردن تجاوزگری آمریکا و عربستان اکتفا کرد
🔹
شورای امنیت ملی عراق در نشستی اضطراری به ریاست فالح الزیدی بدون اعلام اقدامی عملی، صرفا به محکوم کردن تجاوز هوایی آمریکایی-سعودی به مقرهای الحشد الشعبی بسنده کرد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454890" target="_blank">📅 21:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454889">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e079e9fa.mp4?token=ZOzg0GEnejJGITfl50bWqzu9whtMNhnTTVqAfngGHZbVMKKiWFjouhdQ1BIejmv5pUiV3WzUZVFj0ynRFpXGW_R14EctSP0r9K4VwuYm7g0N_Bn0Pqcx09SsukyBrIo_rQu4NQuLV1KS0lfHruMZQBF1wuMzbo2BzjvZ9tmWiopzHzTgFqst_ByRC_lWlN_che5gGAfJ-WzAz5u5YkcP1wJ-pNBfre1pZvcpHwqO90nZpJnvV_A7Fd8rMu-zTjiIlB7lIO2uYnSo9T2-Y7rnFpuXNxmN1ptXUSDCCku0YFOcSRYlsySdRMiCxjmDh3s_9eyQ8PJKRG8Tv-cvoQNmiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e079e9fa.mp4?token=ZOzg0GEnejJGITfl50bWqzu9whtMNhnTTVqAfngGHZbVMKKiWFjouhdQ1BIejmv5pUiV3WzUZVFj0ynRFpXGW_R14EctSP0r9K4VwuYm7g0N_Bn0Pqcx09SsukyBrIo_rQu4NQuLV1KS0lfHruMZQBF1wuMzbo2BzjvZ9tmWiopzHzTgFqst_ByRC_lWlN_che5gGAfJ-WzAz5u5YkcP1wJ-pNBfre1pZvcpHwqO90nZpJnvV_A7Fd8rMu-zTjiIlB7lIO2uYnSo9T2-Y7rnFpuXNxmN1ptXUSDCCku0YFOcSRYlsySdRMiCxjmDh3s_9eyQ8PJKRG8Tv-cvoQNmiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رگبار باران در ارتفاعات مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454889" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454888">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">درس ماجرای مصر و «لحظۀ سوئز» برای ایران
🔹
سال ۱۹۵۶ جمال عبدالناصر رئیس‌جمهور مصر کانال سوئز را ملی اعلام کرد. این آبراه استراتژیک که خون حیاتی تجارت جهانی بود، تا آن روز توسط شرکت فرانسوی-بریتانیایی اداره می‌شد.
🔹
واکنش پاریس و لندن به عنوان ابرقدرت‌های ان زمان، تند و خشن بود و بریتانیا، فرانسه به همراه اسرائیل دست به حملۀ‌ نظامی به مصر زدند؛ هم‌زمان دارایی‌های مالی مصر در بانک‌های غربی بلوکه شد و کمک‌های خارجی، یک‌شبه قطع گردید.
🔹
با بستن کانال سوئز، مصر جنگ نهایی را برنده شد و این «لحظه سوئز» بود که در آن پایان عصر قدرت فرانسه و بریتانیا رقم خورد.
🔹
مصر گرچه امروز با واشنگتن متحد است، با اسرائیل صلح دارد و تحریمی در کار نیست اما اقتصادش همچنان در تب است و بدهی خارجی از ۱۶۰ میلیارد دلار عبور کرده است.
🔗
ماجرای آنچه بر اقتصاد مصر گذشته و انتخابی که پیش‌روی ایران است را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454888" target="_blank">📅 21:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad891b3e3b.mp4?token=sGX_U5mmM0bZzWfi6nFjLFbxZvVxAJjSkrrmGi6OOjLFzG8hRIusA6SHRKFIUz9hGzVOAkzPBrWPbPA4ty-xDwRBm76T_WD9p08OKWZQZBjWDsEjN2bH_omntjJEMUbh7A5HTN7Xk53BZQZvUcxv-vsuxzGsPUAp_uNaB0pjZMehn7R7Ql6F_D59dKHxSVKCv2EtVMaj0urqcrHfbJsP57IaEkQOwvrF2si8uoGHlWAh1Cz-oL7lTHKgwnTQXzlzgfZtng9_BJkj1or7ln7FQjGweQ9dOm23pIoj8PaCzqdojmcSbIpPGdvuzf2hMjQAHpl-IdVx4BpiwzKiddrSig6IREacQOHj4Gjszj0fBoEc9OECucoa0Btr7Udk3-HOlTcSFBMpt6o6yBz9d799QbAM-a8oiiel7J0Rk4U9QYcZcVAgW1j3AMdT-57hzwCcn2vZGuVg7K9B45RVDCUx8zQzthTCQY48s_2hVm5CNyfPW1yRQMvqZTjizkpci2tvnRg-feGliPp-KM0z6sr0NWwrRK8z67HimxY_YmkeDDC8s7SHGyP_69OUmj4mcLkSJ_Ech5bXNdbyrn7AJMv2gVSC-uJOJXIHD30G3Ph3mMj1cNUrYmwsM-enjEPRKZiHVLqH4YebmZSxg3yZDZvW9Kqi6a_rkmAKoCaIO5-e6EU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad891b3e3b.mp4?token=sGX_U5mmM0bZzWfi6nFjLFbxZvVxAJjSkrrmGi6OOjLFzG8hRIusA6SHRKFIUz9hGzVOAkzPBrWPbPA4ty-xDwRBm76T_WD9p08OKWZQZBjWDsEjN2bH_omntjJEMUbh7A5HTN7Xk53BZQZvUcxv-vsuxzGsPUAp_uNaB0pjZMehn7R7Ql6F_D59dKHxSVKCv2EtVMaj0urqcrHfbJsP57IaEkQOwvrF2si8uoGHlWAh1Cz-oL7lTHKgwnTQXzlzgfZtng9_BJkj1or7ln7FQjGweQ9dOm23pIoj8PaCzqdojmcSbIpPGdvuzf2hMjQAHpl-IdVx4BpiwzKiddrSig6IREacQOHj4Gjszj0fBoEc9OECucoa0Btr7Udk3-HOlTcSFBMpt6o6yBz9d799QbAM-a8oiiel7J0Rk4U9QYcZcVAgW1j3AMdT-57hzwCcn2vZGuVg7K9B45RVDCUx8zQzthTCQY48s_2hVm5CNyfPW1yRQMvqZTjizkpci2tvnRg-feGliPp-KM0z6sr0NWwrRK8z67HimxY_YmkeDDC8s7SHGyP_69OUmj4mcLkSJ_Ech5bXNdbyrn7AJMv2gVSC-uJOJXIHD30G3Ph3mMj1cNUrYmwsM-enjEPRKZiHVLqH4YebmZSxg3yZDZvW9Kqi6a_rkmAKoCaIO5-e6EU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفتگوی بدون تعارف با آتش‌نشان بِهشهری و فرزندش که جان یک کودک را نجات دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454887" target="_blank">📅 20:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWb919leniH6mC8KrG8y0thLsYoJPW4ay3vdIS1ZiMTBPJOWHO1ApHWr7Tf9KHrLeF2VwIC5DnTYJ3SJAoWSmvQ4YBBQzu1bfJdiKjv2wB-oLSogdMypBebq0NG49EP9719dcahzdlYm9JCoYoev-1XwRjiucVKpK9GprEwdR0HFJ1V1JKeZyRI2fq2ohW1qJgtBSN1NWos9il-syd240Tbsll6elaJ7pXkWUeE71m2QwK0cV_Ql8fU8O8sar_s3_Y6iiNNvrhP0RiUBzoTAISTRC52ztVZZHUsFo4QwEFsSXtZltVaAoXZRJ5fZV9gd17wZRoTjEy-uX2KDRVLCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
شمارش معکوس انتقام
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454886" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">عملیات جدید یمن علیه پایگاه‌های سعودی
🔹
شبکه المیادین اعلام کرد که اطلاعات اولیه حاکی از آن است که نیروهای مسلح یمن یک عملیات جدید را علیه اردوگاه‌های سعودی انجام داده‌اند.
🔹
در همین راستا، نیروهای مسلح یمن اعلام کرده‌ به زودی بیانیه‌ای در این خصوص منتشر خواهد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454885" target="_blank">📅 20:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7rlm1Lqnqe-VY-RTKMp_P0ufAs7fHbXtkDa8Qp_O19yGI6JS7zphQEgvVXZqAvgSTzOpcF4dAX_wxY_TkrrsvIsYTgZr9zXJCWwq6QYUmBeVVxHpM8arOzjwuGMopPi_L55aAAvDbiI4kURRb-qacIjxjSIOSz2FyrNgYahJYj_MZ20Bw0givvK_bp5B8eu6O1yffLz4kEwrZCMg5yjDFAD3DtEQqpZg1nfry9zgdujYXKexSqOpF3DQf049D3M4Evc29dn0K02TvRKt7Sj0S4hVkOpA5o8IWCpX-eRLOI_PUnfIDQ_b21xWyyjk1U_PIPY_i1PA93IJCSpGe7UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنایه بقایی به توهم نفتی ترامپ: اول باید واقعا پیروز شوید نه اینگه در هرمز گرفتار باشید
🔹
سخنگوی وزارت خارجه: رئیس‌جمهور آمریکا مدعی شده: «ما مقدار زیادی نفت از ونزوئلا می‌گیریم؛ میلیاردها و میلیاردها بشکه نفت؛ و همین کار را درباره جمهوری اسلامی ایران نیز انجام می‌دهیم.»
🔹
پیش از آنکه بتوانید مدعی غنایم جنگی شوید، باید واقعاً در جنگ پیروز شوید؛ نه اینکه در یک تنگه گرفتار شوید، در دستیابی به اهداف (شوم) اعلام‌شده‌تان ناکام بمانید، با کمبود تسلیحات مواجه شوید و در این مسیر اعتبار خود را نیز از دست بدهید.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454884" target="_blank">📅 20:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454882">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
مقاومت اسلامی عراق: پاسخ ما به عربستان و آمریکا قطعی است
🔹
برای حفظ امنیت زائران حضرت اباعبدالله الحسین(ع) و خادمان موکب‌ها و جلوگیری از هرگونه اخلال در مراسم اربعین، پاسخ ما به تجاوز آمریکا تا پایان این مراسم به تعویق خواهد افتاد؛ اما این پاسخ قطعی است…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454882" target="_blank">📅 20:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454881">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4iD5QV0XKPS8QaK6bapudKTCZQHq4_l3J7XQNZvpznFzVOj9hi4j71xyRP-e5Xa05wcrUPTfEwv84vhIkBtP8dVtOtDw2VWGesFcwf7tGfd5NwH84YPrWzdQKy5jPuKSMzCW0gOt3CeAMp6SBqWJGw832X6eS23kD1azbtDqFVNSla1prMW61S41e8GaAvrtGZspVQUzx4LQlCO226VW30aDAh82tUgFDnkRNzy32wO0GNjUffrgzsU7xpuuahFGkuKJdfE4c3m1E-51_z8Ii1_bowCAqoz1iR63vLhck-OGQapOARi5qcwkOhmuGsOWP4jcoWdSrjNvp8QU5zo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بازی مرکب» دیوید فینچر در نتفلیکس متوقف شد
🔹
گزارش‌ها حاکی است پروژه مورد انتظار دیوید فینچر برای ساخت نسخه انگلیسی‌زبان سریال محبوب کره‌ای «بازی مرکب» (Squid Game)، از دستور کار نتفلیکس خارج شده است.
🔹
در واپسین صحنه از فصل سوم سریال پربیننده نتفلیکس، شاهد مواجهه‌ای معنادار میان شخصیت منفی سریال «فرانت من» (با بازی لی بیونگ-هون) و زنی ناشناس از لس‌آنجلس هستیم؛ شخصیتی که با بازی کیت بلانشت ظاهر می‌شود و ظاهراً مأمور جذب شرکت‌کنندگان برای نسخه آمریکایی این بازی‌هاست.
🔹
بر اساس این گزارش، نتفلیکس احتمالاً به جای این پروژه، توسعه نسخه‌های محلی و بین‌المللی دیگری از «بازی مرکب» را در اولویت قرار داده است. نتفلیکس و نمایندگان فینچر تاکنون واکنشی رسمی به این گزارش نشان نداده‌اند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454881" target="_blank">📅 19:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454880">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزارت خارجه آمریکا از وضع تحریم‌های جدید علیه ایران خبر داد
🔹
وزارت خارجه آمریکا در بیانیه‌ای اعلام کرد اقدامات جدیدی برای قطع مبادلات مالی با ایران انجام داده است.
🔹
در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454880" target="_blank">📅 19:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454879">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2cc38f78d.mp4?token=SPk4IINUxbF5ESQ5Ycy9CxIIlMnfEvVZc76TfR3rrIWRG7-9lSNrHqM-hSNSGlzOWFQZ_CmyTBUQsGyYEFJ1TVlCIHzrog1ftA9gjmX8MRPWm3nMjIochr0fF_CbCzgN8hwlqZHke9QXDdkBaRhZG6uj5WLxR92lizqmb1RuUWIfaPXp05tHmHWY0oyFpVB6ksGiEQsvoL2sgwF6hYYiIE5lPyCRQCszKLAJg4z8tqhNvfvpi8AHh_opWhK8TVM4XjVO9CvLFxxBGXaGcf3sKwF2NlnLUkSGl0072SA5U8qBYFtM3GX2YLf3cA1ilCHsmnhcRDeBDjZZbj9YJlwJDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2cc38f78d.mp4?token=SPk4IINUxbF5ESQ5Ycy9CxIIlMnfEvVZc76TfR3rrIWRG7-9lSNrHqM-hSNSGlzOWFQZ_CmyTBUQsGyYEFJ1TVlCIHzrog1ftA9gjmX8MRPWm3nMjIochr0fF_CbCzgN8hwlqZHke9QXDdkBaRhZG6uj5WLxR92lizqmb1RuUWIfaPXp05tHmHWY0oyFpVB6ksGiEQsvoL2sgwF6hYYiIE5lPyCRQCszKLAJg4z8tqhNvfvpi8AHh_opWhK8TVM4XjVO9CvLFxxBGXaGcf3sKwF2NlnLUkSGl0072SA5U8qBYFtM3GX2YLf3cA1ilCHsmnhcRDeBDjZZbj9YJlwJDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عصر بارانی تابستان در فاروج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454879" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454878">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
تصاویر جدیدی از توقف کشتی‌ها در شمال تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454878" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454877">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJR0BA7aTwcGDaGzb5BQHygIR0j5JAn81YbVK0Wr5-hUtP1K93bNK-lyjC-ABarvva9x7jr2x2-sssmvK83lEFTjJm5S9SVT0EKRghrgn0VqKKQL5JSONLqLqXCmDmXkd2GoRegJjJx0O7S7hJkI6vJ-jn2okq8vorjDdQiEmcSyUAY_XaP7LszGcgy2_ZABip96C2g6O6zpaJhuXyvzYbY2pVj9wZ3XjeDLbR7pKMEpOGA0kaTLbZ14IrgeMXvzCRBKoegd95QBYBL3XDReS7dOX7rMBIb2GpPBOK76XNIlVvvIquAzP5cgteDS66fmh297KfF5bLg4F89nA9m0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید یمن به سرنگونی نظام حاکم بر عربستان
🔹
وزارت امور خارجۀ یمن به مسئولان عربستان سعودی هشدار داد که اگر به سیاست‌های استعماری خود ادامه دهند، باید منتظر نابودی نظام حاکم بر این کشور باشند.
🔹
یمن تأکید کرد عربستان با فعالیت‌های استعماری خود به سمت مسیر بی‌بازگشتی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454877" target="_blank">📅 19:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454876">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib1A-l8OMTWDIquJ-mTqGTpKIJ78gK6P6yf3Y1tN9Hd7LjG8PaDL0njkitkYsQkgYnOUXQ6SQz-hxC84YxDrD2M8kRruX4v3ytE34aZYDRL07z5VXo8YgmmPTiO_y7fas5A8yDiPEF5L5k5fRsqEoNgLOUJ3xCBqkkLvzt8AcOx7mUE_RoQ6m93tF4624BL48I06LuAdFuVT14Tq3jESuJiavEmf7csfU5QN4C-jGd6f3GpeATpkpP1NOWYsBl1pH5vmUVYjF9v4OULM0OvIYA7vuYz4X1DQ1CjP_8k5u1Nay67VF07GB3998TF3H1BCM0zlZ-9DmGJcK-Hpown3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقم تاریخی اجارۀ کشتی برای انتقال نفت عراق به خارج از هرمز
🔹
رویترز می‌گوید که شرکت «ریلاینس اینداستریز» هند برای اجارۀ یک ابرنفتکش برای حمل نفت خام عراق بین ۲۳ تا ۲۵ میلیون دلار به یک شرکت کره‌ای پرداخت کرده است.
🔹
پیش از جنگ، هزینه اجاره چنین نفتکشی حدود ۲ میلیون دلار بود، یعنی هزینه حمل‌ونقل از مسیر خلیج فارس اکنون ۱۲ برابر افزایش یافته است.
🔹
رویترز می‌گوید اسنادی به دستش رسیده که عراق برای ترغیب خریداران به بارگیری نفت از پایانه‌های داخل تنگه هرمز، نفت خام خود را با تخفیف ۲۵ تا ۳۰ دلار برای هر بشکه نسبت به شاخص عمان-دبی عرضه می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454876" target="_blank">📅 19:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454875">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awu6DTWRUI9YOUoxG0ldXs_6WWUWoxnIjag8Y9J0Q_2EFQHhZRhWWZEUaTvnNRQkni2OCdZjjAcmqmltBqBdi5sP0U1MHAUZSjwF-W5i6hEH_hyLOLJpKXapJ9z66DMFRxUoGLvmmOvXe9eQX1YBWu3sLETt6DB7jMUaANaVT4LuwCqyIfH3DYlxD6GWBgLxgfRZSMaWZ_kMOHiasNiXFys8VK_NOKrGZKCjJmzYPg1ZLMBilARy4_T8Phug5Q8dxD9WD2lSdLlcU-mRPMwjs7G0yF8RWfBndZOMVQ3jtBVnRHwC77eXtCIVx-NKpMBHz0_GIJTaoIQgvrWh0SW3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت نیروگاه‌های تجدیدپذیر ۴.۶ برابر شد
🔹
وزارت نیرو: ظرفیت نیروگاه‌های تجدیدپذیر کشور به ۵۸۰۰ مگاوات رسید.
🔹
این میزان که در ابتدای دولت چهاردهم ۱۲۵۰ مگاوات بود، اکنون با رشدی ۴.۶ برابری همراه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454875" target="_blank">📅 18:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454874">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سازمان سنجش: نتایج آزمون‌های ورودی مدارس سمپاد و نمونه‌دولتی اوایل هفتۀ آینده منتشر می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454874" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454873">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6sKmJhd0J4E2F3v2KQdAkZlWxsIsMg15wlo6llT5WRgc8O-OiITojcaM1gmgyHs33IvL0X6Ls55pupDBDTMzYOlxoYfg41UBYEkRE0fw3TOTATmLmV_QYlst8pIY0_xPIGnItXEhfoGYwZx_IEjqxQCU6SSaRUhUy7ESeF4KCcjGjDljKfbzQo095kM5tGxK_oOidkpBmDFZ9DUBznj7Mu_yCUquXei5L9pRA4bouhCrhwd4sRH-7g6baFOSOT8u6tgz1TXeY6ZOdCiedADfKd-NQSZG-VUe4BcEFa6AHFVfEJ1kt4dHYChYb4-TaNJmKqIlim0jWAfp3ikOfKUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ۴۳ روز تا مرگ نفتی فاصله دارد
🔹
بر اساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیرۀ‌ استراتژیک نفت ایالات متحده به کمترین میزان از سال ۱۹۸۳ رسیده است.
🔹
این ذخیره هم‌اکنون تنها معادل ۴۳ روز مصرف نفت خام این کشور است و اگر نفت جدیدی به آمریکا نرسد این کشور با کمبود نفت مواجه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454873" target="_blank">📅 18:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454872">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX7z2ACfIQi00UtdZkt5FZU8f41C4zRq-s2gRrNtDzKuXxVFDv5PQ81XSqI3rEnxh3KfyS5IwvFZL1xdnZi_n0RZZn6bJFtLcVUZaAZFmB4fr4pmxwiHHHkDSV5-df5clTf1AiHuqOMLgvaykilU_Ws9gnxFitPS3S8B8qnc4e_DljuCxg2hirnkvA4cIcUryPuRweURlf3B9gYyDtc9twj70aj59NtIL-OlJmSZb_aS9ltJYl4ottj1gPGeQtqSGiWvh323yB9nK8AZZx26HXyIELshIVmvL0PCtY87zAt7h28rOkG0sywg4JEeI4-hTnEP1V4K_JtaFrJAi8ahdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات جدید یمن علیه پایگاه‌های سعودی
🔹
شبکه المیادین اعلام کرد که اطلاعات اولیه حاکی از آن است که نیروهای مسلح یمن یک عملیات جدید را علیه اردوگاه‌های سعودی انجام داده‌اند.
🔹
در همین راستا، نیروهای مسلح یمن اعلام کرده‌ به زودی بیانیه‌ای در این خصوص منتشر خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454872" target="_blank">📅 17:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deebb7c7d7.mp4?token=dM-pLR7Q7GVdOC2VtGp3i2nvE_LReHvBHIsMum9yDhSKyjDSGmwSR7cXqpAlOfQATrf8KAxJGviub1LrVYQN7kB4YtPrsBXBeW0GC8RHPGnZA_ByN8DIsj-4ZChG0TjDh0l-gLQsx_uGU0RySlab4ZNhc4oxf9wboS0FXs_5RMl3xWp-Z6Hh43C96p6XyiIiXsmwrfhY4X-xyTNZbg3o9qv8lnKFRy1XHrMG7XBAMbSPmCoEdQmTqcNIzSuVKeuK5ZBuKnX0r98x6RiEr9e8LwS1xvCYX7sMK6gBEULwFmZH1YrwojlWYt13zN2bz8llqZDIYMlwKheRXFj2UTfE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deebb7c7d7.mp4?token=dM-pLR7Q7GVdOC2VtGp3i2nvE_LReHvBHIsMum9yDhSKyjDSGmwSR7cXqpAlOfQATrf8KAxJGviub1LrVYQN7kB4YtPrsBXBeW0GC8RHPGnZA_ByN8DIsj-4ZChG0TjDh0l-gLQsx_uGU0RySlab4ZNhc4oxf9wboS0FXs_5RMl3xWp-Z6Hh43C96p6XyiIiXsmwrfhY4X-xyTNZbg3o9qv8lnKFRy1XHrMG7XBAMbSPmCoEdQmTqcNIzSuVKeuK5ZBuKnX0r98x6RiEr9e8LwS1xvCYX7sMK6gBEULwFmZH1YrwojlWYt13zN2bz8llqZDIYMlwKheRXFj2UTfE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه نفت اسلواکی منفجر شد
🔹
انفجار در پالایشگاه نفت اسلونفت در شهر براتیسلاوا، پایتخت اسلواکی آتش‌سوزی گسترده‌ای در این تأسیسات به راه انداخته است.
🔸
در ماه‌های اخیر پالایشگاه‌ها و زیرساخت‌های انرژی در اروپا و اوراسیا هدف قرار می‌گیرند؛ از وقوع آتش‌سوزی در پالایشگاه‌هایی در اروپای شرقی تا تاسیسات بزرگ نفتی روسیه.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454871" target="_blank">📅 17:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67424e7ac.mp4?token=FGVujq2lmGLh-62ReaAnTumSlWG3Od2RjGrZ9LTxumtxYsC_ZYfZYa2iRjU1Nal1YosdwKjY-8L1FAlS4GnZAaTBpz49YuA14q6-HorRej3ZwfbVxD4h6ede8r2tW59Qthh2osnNXSYWy8WNOW2VcPEUpoFM96HabggRJq2hNumkrzRLtMCy5fP4dvfP49tr_RbJzwCr8BIS6YjNLcVy7eT-52x0WEAmV_rn4q0E5iq6e-BN3I-w8VqzaJe5KkzM6VG3P-jrylz360YT8qPzKSKJbNpQGMqlP6oss7U7EuNPMtp0R9kfbH-0cw9zV7ojRLIaqSOREPaEKbbDi6RN9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67424e7ac.mp4?token=FGVujq2lmGLh-62ReaAnTumSlWG3Od2RjGrZ9LTxumtxYsC_ZYfZYa2iRjU1Nal1YosdwKjY-8L1FAlS4GnZAaTBpz49YuA14q6-HorRej3ZwfbVxD4h6ede8r2tW59Qthh2osnNXSYWy8WNOW2VcPEUpoFM96HabggRJq2hNumkrzRLtMCy5fP4dvfP49tr_RbJzwCr8BIS6YjNLcVy7eT-52x0WEAmV_rn4q0E5iq6e-BN3I-w8VqzaJe5KkzM6VG3P-jrylz360YT8qPzKSKJbNpQGMqlP6oss7U7EuNPMtp0R9kfbH-0cw9zV7ojRLIaqSOREPaEKbbDi6RN9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از مختصات جدید تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454870" target="_blank">📅 17:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454868">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTklnj3Pq56m8zUiOELdUcE5XhJK3pCcpi1mW-IcvYfQ3zPBlpXeAZzOlZ0FWzrGxLcH7cQOX-e7MsvHz6GkVfg2CdVCxkE2GQfG6du7KsBWpSblpZrZuBOKLV5b-A5_0cnXrX4MygjEVqcuh9YEDjjE-olFA7sdPmdQ3wjOvWEMZiwo9pjAqq-zXrsnrhO81eyJ1dXQtC5vMGMKSb4iV2QWcA-o6EahXUw9NG0JUwT-ZfrPoFsQPArcofpr43Rsv6KLwA3yDmXDmy9wR81mWv6Itl1l6-lVXyoMl4AJ8LYw3O1iDuE8VdXnV96mYPhyhaVbwKDTFxjyIqWBCMh_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلارزدایی چینی‌ها با خرید تاریخی طلا
🔹
جدیدترین آمارهای رسمی دولت چین که امروز جمعه منتشر شده است، نشان می‌دهد که پکن ماه جولای ۲۰ تن طلا خریده که بیشترین میزان در سه سال گذشته است.
🔹
از ماه مارس که جنگ علیه ایران شد، خرید طلا چین هم افرایش یافته است و ماه گذشته هم ۱۵ تن طلا خرید.
🔹
یک ماه و نیم پیش بود که آمار شورای جهانی طلا نشان داد حجم طلای نهادهای دولتی بالاترین میزان در نیم‌قرن گذشته است و آمارهای بلومبرگ هم از پیشی گرفتن ذخایر طلای بانک‌های مرکزی جهان از دارایی‌های دلاری حکایت دارد.
🔹
آخرین آمار وزارت خزانه‌داری آمریکا نشان می‌دهد که دارایی‌های چین در قالب اوراق قرضه آمریکا تقریبا نصف شده است حالا پکن با این خرید از ابتدای سال ۶۰ تن به ذخایر طلای خود اضافه کرده است و حدود ۲۳۶۶ تن طلا در اختیار دارد.
https://farsnews.ir/Sadeghi/1786109079785791668</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454868" target="_blank">📅 17:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454867">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBVQ9M6obQqeUdT20HTNJtwOnPIx0SRlgC9oaGo-naugAj6upc6tY62YfU4ndIXeB0iNNs6gAIlGggg5Du-gd7Q6gwtqSFtQSidVq4Nq2oCIwadNUwgjfv8OUyUOGHUjlMKfskXsfvGMdBFqteW7oggRi0p3ZZnvoxYrg7CT0z_tt_UnA2UReMj8J35PrU7H4uM7Fg1Gi9cEh2Q3xpp1x0t_g2EHCNxOO8Z0FOHrhlj5eUjV0gy9BUunGsI6dRUkzO3W4HmF5rTWf1O9TDq7ki-x3SLklRCVPo3mxOwvDGrN7v0voMkXUgt3epSyixlfzOXVL_eH_T792wEs2RIBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش جوانان ایران در المپیاد جهانی هوش مصنوعی
🔹
اعضای تیم ملی المپیاد هوش مصنوعی ایران موفق به کسب ۲ مدال نقره و ۱ مدال برنز المپیاد جهانی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454867" target="_blank">📅 17:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454866">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byDA2GxBv44xm0KhxijyVJ9kDrsjY-jOrMZHzLzbSgWFQd-kxUA3rUoa7kaZuFTddOyK1gvIBKX1jgrThyukq1QFpgZg976bOXN7zyXeYTfrM_8VzBCDe9qtxYtkzrkIlAFcPNc0NZHTBV0Np11lxl4gfEo1hDMDjqQj6g1-hpFK12sA2aG1yGGaF9xRa4ot0HlF1-y2MJYt1RcUzb_5G1kVTQ5fW4P57JYAe2pZ4VgZTK1DGk13R2_fr6b85CEyGcxougBB_UFzgrT0EvExABx9iuo0Si4yEsnZphuIZ-_OxMTaI92N-EiB-Qk-gaoEDDjMEciG93fwjLNM_EgcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مرد سه‌هزار چهره» و حماسۀ شیرعلی‌مردان‌خان در راه تلوزیون
🔹
نقویان، رئیس سیمافیلم در گفت‌وگو با فارس گفت تولید سریال «مرد سه‌هزار چهره» به پایان رسیده و این سریال بعد از ماه صفر به پخش خواهد رسید.
🔹
این اثر مهران مدیری، حدودا ۱۵ قسمت است و در مرحلۀ تدوین قرار دارد؛ در این فصل از سریال، شخصیت شصت‌چی در موقعیت‌های مختلف قرار می‌گیرد و اتفاقاتی رقم می‌خورد.
🔹
نقویان همچنین خبر داد که فیلم‌برداری سریال «حماسۀ زاگرس» که مبارزات شیرعلی مردان‌خان بختیاریرا به تصویر می‌کشد تا پایان سال به پایان می‌رسد و پخش آن به سال آینده موکول می‌شود.
🔹
همچنین ۲ اثر پخش‌نشده از زنده‌یاد اکبر عبدی به‌نام سریال‌های «ماه‌عسل» و «سبزواران» وجود دارد که مجموعۀ ماه‌عسل پس‌از ماه صفر در کنداکتور پخش قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454866" target="_blank">📅 16:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454865">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npLVhAP7JnO3U3omFQFDputREQlE0l_HXqgCnLLI2c9hDApxhK52JuH7kJ1KgNnfr1ZTUFh_be45SBF7CNcxOjCB_mh16KlM1b9IK_Q_mjXHB6XKpRjB6nY0UlVvL-fbY4X-oKuYRvF-yrIkAU0iY-5DRhY-bnhiUlBaY7hU3e6hi1XLDVSn4W2cVAHXyXFXgWbUput_KEpcrJ32kH3ImtVo1krh5Mc4Ira9y6Afs-ubWhR1n-wj4Ru8uJLweyfqkyWHuNzcUsOhOKUMzx4yHS77NO30eF0Zr9f9ZjUtvoK077cwongUOkZ7zdFfajdvP_1267OiQA9Ro5F03WMbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان تماس‌های تبلیغاتی مزاحم در فرانسه
🔹
فرانسه برای مقابله با تماس‌های تبلیغاتی مزاحم و کلاهبرداری‌های تلفنی، قانونی تصویب کرده که طبق آن شرکت‌ها دیگر حق ندارند بدون رضایت قبلی افراد با آن‌ها تماس تبلیغاتی برقرار کنند.
🔹
براساس قانون جدید، هر شرکتی که به‌طور غیرقانونی تماس تبلیغاتی برقرار کند، ممکن است تا ۳۷۵ هزار یورو برای هر تماس جریمه شود.
🔹
دولت فرانسه اعلام کرده که حدود سه‌چهارم مردم این کشور هر هفته دست‌کم یک تماس تبلیغاتی ناخواسته دریافت می‌کنند و بسیاری از آن‌ها با تماس‌های بیشتری مواجه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/454865" target="_blank">📅 16:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454864">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0AYtcPtK3fKgKkQ_yiyFaKleF4C8TUVmLxdnXA-GOozPxNfTQp9K_LFxdQLufYQmjlDjJEsUg_WURCLxaBYwsEiWXUTgqXOMLD8SR4ShEvuuJs_T3ffesgMlgndaowfCdYkPsw1vulodMBdjrSwr2neJsfyn-zvyIoHO2nGRoUTDNm1Lr6azaA-fmAYkCnoHsNInRA7XNm8KbiHsDqAiE5hkC0rMzIY0bo3Zlw9c6ZeSkLdE-6M0jq_dzHgsiX7iPku2Bo6lWzLA5WJPDbDxiyHtCGKZ_k2PT4l7GcKYVytc1S_O-blUT-hl1laQspkeQX4B1PIIjJ3FS5MYvl8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت سقف پیام در چت‌جی‌پی‌تی حذف می‌شود
🔹
اپن‌ای‌آی اعلام کرده از هفتۀ آینده محدودیت تعداد گفت‌وگوهای متنی در چت‌جی‌پی‌تی را برای کاربران رایگان حذف می‌کند.
🔹
همچنین مدل جدید جی‌پی‌تی۵.۶ لونا جایگزین جی‌پی‌تی۵.۵ به‌عنوان مدل پیش‌فرض برای همۀ کاربران خواهد شد.
🔹
بااین‌حال، اوپن‌ای‌آی اعلام کرده محدودیت استفاده از قابلیت‌هایی مانند بارگذاری فایل، تولید تصویر، مکالمۀ صوتی و ساخت تصاویر همچنان برقرار خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454864" target="_blank">📅 16:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UH4PF6ZKjXqO0388MrzSwU_962DHO48uDwsCX4P1J9BTQVXuYAVgkFs9ewCGJfYIOzKvYQj6YJsfY98_UJz9EXLPRrKwGhLye_SM2cdnA7LPQpsuMLcGfjCkVwijNrvEAqzSTCHXSc29RmGP1yayTNeyTMGBNMwiUo8kujBN0ECnx3iKvwNvJAN_5KSELcr9mjx9hH6C2kA4AIE20a0Qiv1kHQov0ZfLb28Jtf6jIQ1M_TnojWCM8QGK_qgkspFp-HM9xsN9Qa-8Aaw2Z-_Saso6GngHKmsTUn3WsnDjobWi9Ni4W4zA6OM8OozHcYOIVvo4SPsaGqO4UowPIEiGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDhIEBGYxqLQW3NBcph_y7fufOax61ss4lAmgHkOGaAjUBEbcIArFGd8NSm8L1mth-pIKxrEWeNhtaXZXGgCfO-kRHE1TyUYDw4fpGxrtx1ku1d13uRP7o5V7p9QOt6qlyOihH_adAhfiKOC9t_DkSa6Dxx7Et_rxdPavQsiiN2yl5yWNHVF8VTRCIlusishgWELg64b3isIdhe3ZqKJBvKZIwkxFXujYoH6tjgrkcLQNYPgWJ_i_Kt-YnFpspMo39HwfTfRrta4omegieWQbYGbkheZ9TvHeiBNr9CJg3XLTKKbt5-Iz3e3h6Z-M_GF6npHvYrnNFmSriQ3h-gc1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0En9Gdkl4M2nn-Odguyou4aRbXN9MVTuG9nPxRmfcqyQ7isf45ntjrcWmXYICy4T5MPqeA2vDF9sX7immfkUUqf0wnkuOX3eA8-EEP-uuuLBm3BR0BkJ84XftUaG3zwg1C0oaq6BhN0LwodIapL48wQBTKRtPiAqTMTDvE4V-TZ0xK7TSQxkpojVbuIDHawyVcNf0y9LdCOQWWY4GSF2pPoZggIcNRdcMO39ACK-NBAOAVuK8PucBbXauQdQG_TQLExhpYgAaniXanjrzx3nCRZOJr_WGIJLTr2xj0kk2IEr9ZlfkM0MJJP5nO_Amfr8UfgxRueJ97OehQX_zSC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw_hoPEKJsiQcLX7Vx1WX7Du2JBRIhXXmUrFgozgN2MpVaF4yVMJN3uxzj7ZfZSC8DvEzJumYEyAZ_RkaQ7nMBVZXZvQfTrCkHjVxBdTzK__LLVc4sp3OkrYciWoPfO_Uxv1Ci8FrIaPMVgs4aUMX0la-RJ-mbuAYRhFBwKIMjt9i3tYgj88znLM4WMbw17IFzXPyd5usaj4cdYFMMQQZ7fs2k5dUS03Ll9s8jsNFOCWBoW8V5nqLPDoUugbc9TfGKKZEf_EtCzr6W8ah6MWPLkJzj8Wn0fgqFSugOVrry9WHFuypGmvqYlDGsXZLWKd9IwKH-wYk9548-oJgbKr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQ94Q2yURk5EsZYdma_03VCuO9Hm2AMgaMGvljqKPLU7pDSU-71KIXEMh-Izbh78ZVI7EujRLV0xEX44c8gh4I2PzNeUczXykkPxHkIwnULfdeuc-tFTnMIY9c5xYU8furnnEgdnSptfDeDvk4g0xUqqStN9Il4XmehWPeDQNX8FREqmAevsMHmP2NOXrPLIZAdA_YItlWKq3zIaE4StoZnXgtrVzpYBSe5XktOxFGKGsG4QTS65ke1tJkaIZncmjZH7dyynQnuQEKb7wagW5acLpZhUfXxrhXrWBnzWfiqVLQ_AhbPBtEIJnynaL5_utYKXVeS7_H7AgfltSCb0Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم دعای کمیل شب گذشته در حرم امیرالمومنین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454859" target="_blank">📅 16:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454858">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3l1GjjYMuQ4ddPJeK_pcqW4g1GuOJsVm9oxUeoLoCmH52Da811vvjikpmrCOFt314XzbtkYkegvnqIUntU37vpzxXZDUS9Cj3631UZ3ywt4RKnFfbeQ_vs4B0WgdsCYML4I5VbiGY57qrZm2nWW5JjAZBWvD0RobpWyDPj5T1E0KQ9tGikrSPPptsRT_NJ9nZW8dWBZmiKNUKvfY25zoIJvd7fBEn30eA_8527x1RfLEILp36wi1esFl6WjTRLSSOg5fd5oSFY20FimI7FKL18Kl9LKQLw-MK_AXtajL4znr-oBBbNJiZJCHi1JRdsCPdByC-7F3T209zec4j-GJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان عمر ۵۰ ساله دلارهای نفتی به دست ایران
🔹
ماه پیش عربستان هیچ نفتی به آمریکا نفروخته است؛ اقتصاددان آمریکایی، استیو هانکه، در واکنش به این موضوع در صفحه‌‌اش نوشته: «خداحافظ پترودلار».
🔹
پترودلار از اواخر دهه ۱۹۷۰ میلادی شکل گرفت؛ جایی که پس‌از شوک نفتی، واشنگتن و ریاض توافق کردند که عربستان نفتش را فقط با دلار بفروشد و در اوراق و دارایی‌های آمریکا سرمایه‌گذاری کند؛ این دلارها به پترودلار معروف شدند.
🔹
حالا با بسته‌بودن هر ۲ تنگۀ هرمز و باب‌المندب به‌روی نفتکش‌های سعودی پترودلار عملا کاربرد خود را از دست داده.
🔹
ازطرفی با نبود معاملۀ نفتی بین عربستان و آمریکا، ذخایر نفت آمریکا به ۳۰۴.۸ میلیون بشکه در روز رسیده که با عدد بحرانی اقتصاددان‌ها یعنی ۳۰۰ میلیون بشکه تنها حدود ۵ میلیون بشکه فاصله دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454858" target="_blank">📅 15:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454857">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMeFO_WM0g5_S9puRhxtFyv9WD1pvcitVUGMIs2Ji7IW6mDvEpUdkuUDsDJx17fFRF8qAWx2D88mnLp-ebu3x6n8kHWiVVbdu5JtPmv2B113Hbrpc7T8V_gqBbokefQjo23JqMDOJt77yIdjCd-yYk3X5MQZd-ImlLhOkpCrLwqO_QMr2JbrcqyyNsA4m__oG0dthOIU1bR6Jot3h4Zkm8FxEBYdxhYwOsv-7C7c6MopiLsAgucU2pPTMcGYpTSk3hO-e9tguveHj6S7ijyKXYwNgww5gnVaQqizjh36OiUWqUYbTA9Sy3OB7g22NBgT1E2veyh-qa1Vyl2jokEIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آدان در آستانۀ بازگشت به استقلال
⚽️
بسته‌ماندن پنجرۀ نقل‌و‌انتقالاتی استقلال و بازگشت خلیفه به آلومینیوم باعث شده تا باشگاه استقلال دوباره به سراغ دروازه‌بان اسپانیایی فصل گذشتۀ خود برود.
⚽️
طبق شنیده‌ها مذاکرات با آدان مثبت بوده و قرار است مطالبات این بازیکن نیز پرداخت شود.
⚽️
این سنگربان احتمالا در هفته پیش‌رو راهی دوبی می‌شود تا آن‌جا طلب خود از استقلال را دریافت کند و سپس برای عقد قرارداد مجدد با آبی‌پوشان راهی تهران شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454857" target="_blank">📅 15:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454856">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3b0b0091.mp4?token=r6-G5qPK5Vnq7lEI8EiqmG1nQMBAEUZJDvfFjd0RPs5nmVp4ds_B0jeKflQ1llUInOV3CWwUsxdvmU3vF6IyOGBqfgOzVEGAP6jOxlEELaN_B6I2C0dH-dvd4n8Dn15SF1jPfxchX87o_SlAWTKPnQvsVl2ASVn8_LNVZ549SREF12ADrSio2nEdJpusAIwuCgAErs4M2RuoWWvDGl4IBNR7p73GCgPEFXs_fR-TWifAzt70Yv3GHGQnw5kEZHJWl3_g8DGAFxiAXCUr5lfBCS-o5HTNWMao_sezTwuoT4fIWAq_tSoC8k09u--_xc06rVADE2YVxD94qe5o-TsTw0d-PqkV1w2RzeWUN2mIs-heMopvYgMAMr7ieCquwSEjsntekm8-ZlXuA0OMHBq6JIdwauidLfcau-m2Ap7rLGyQoxTMriNiMwDi7SkQ44w-b7bb8SkBlf1vtW_Ukcb_1_HXvMyGBvq7QHzhc_8NaN0dZ8HTYg4ZbYxUCp0_4pfOHKR5hG2Mdob15P-FjSEjFs8-ibzxRupxfKKmJ6LQv3hQUqWx3yg27zcmkzol9R7a02vu33Ch0WLj6RVbxOrgo8FX-DwdzYB4xOu1QUag4VNdgSSj1yHA162xowSk-pU72z-9vzsK_fEluRRFLnnQV9jb9ENZgfxqFggqxrf2HC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3b0b0091.mp4?token=r6-G5qPK5Vnq7lEI8EiqmG1nQMBAEUZJDvfFjd0RPs5nmVp4ds_B0jeKflQ1llUInOV3CWwUsxdvmU3vF6IyOGBqfgOzVEGAP6jOxlEELaN_B6I2C0dH-dvd4n8Dn15SF1jPfxchX87o_SlAWTKPnQvsVl2ASVn8_LNVZ549SREF12ADrSio2nEdJpusAIwuCgAErs4M2RuoWWvDGl4IBNR7p73GCgPEFXs_fR-TWifAzt70Yv3GHGQnw5kEZHJWl3_g8DGAFxiAXCUr5lfBCS-o5HTNWMao_sezTwuoT4fIWAq_tSoC8k09u--_xc06rVADE2YVxD94qe5o-TsTw0d-PqkV1w2RzeWUN2mIs-heMopvYgMAMr7ieCquwSEjsntekm8-ZlXuA0OMHBq6JIdwauidLfcau-m2Ap7rLGyQoxTMriNiMwDi7SkQ44w-b7bb8SkBlf1vtW_Ukcb_1_HXvMyGBvq7QHzhc_8NaN0dZ8HTYg4ZbYxUCp0_4pfOHKR5hG2Mdob15P-FjSEjFs8-ibzxRupxfKKmJ6LQv3hQUqWx3yg27zcmkzol9R7a02vu33Ch0WLj6RVbxOrgo8FX-DwdzYB4xOu1QUag4VNdgSSj1yHA162xowSk-pU72z-9vzsK_fEluRRFLnnQV9jb9ENZgfxqFggqxrf2HC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات هوایی سنگین روسیه به مراکز کنترل پهپادی اوکراین
🔹
وزارت دفاع روسیه اعلام کرد جنگنده‌های سوخو-۳۴ نیروی هوایی این کشور با استفاده از بمب‌های هدایت‌شونده FAB چندین حمله علیه مواضع ارتش اوکراین انجام داده‌اند.
🔹
به گفته این وزارتخانه، این حملات مراکز کنترل پهپادهای تیپ‌های عملیاتی چهارم و پانزدهم گارد ملی اوکراین در منطقه دوبرپولیه در جمهوری خلق دونتسک و همچنین تیپ ۱۰۵ دفاع سرزمینی اوکراین در منطقه براتنیتسا در استان خارکیف را هدف قرار داده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454856" target="_blank">📅 15:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454855">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e751166f.mp4?token=td9zvLa7lpbvKZkQRtvUXC1ExfPcWiXC-lDNCYyt23nPnXfRzujZoR04glLQkTWr8V6sUxAuul7p6Lq1iZlzme2IyupByFBwhirk5ZTSywbWJoyAwDj639d_xOQEypm6cLnzkmvp4O2yLTO7V41LcLN2pNXrSE5sWcpyYeWmVh1QbeeSJ3dDSlP-aIpxkrRy_mI5NUPo1kyLLysYTVwE3p92NJ3-BKaCajqTMqYepax2Ka2ATCDkVv83s3L5OtV2JN70pkhTmRqeQxYKVI3P4-vblH6FA7_oSIIk9XpfDzo88P_yQ_61WYZ7kvnSb65hAMpcxVfYBsvjKNKmdRU3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e751166f.mp4?token=td9zvLa7lpbvKZkQRtvUXC1ExfPcWiXC-lDNCYyt23nPnXfRzujZoR04glLQkTWr8V6sUxAuul7p6Lq1iZlzme2IyupByFBwhirk5ZTSywbWJoyAwDj639d_xOQEypm6cLnzkmvp4O2yLTO7V41LcLN2pNXrSE5sWcpyYeWmVh1QbeeSJ3dDSlP-aIpxkrRy_mI5NUPo1kyLLysYTVwE3p92NJ3-BKaCajqTMqYepax2Ka2ATCDkVv83s3L5OtV2JN70pkhTmRqeQxYKVI3P4-vblH6FA7_oSIIk9XpfDzo88P_yQ_61WYZ7kvnSb65hAMpcxVfYBsvjKNKmdRU3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان آرژانتینی پرچم آمریکا را پایین کشیدند
🔹
معترضان آرژانتینی در جریان تجمعی علیه لایحه «مصونیت املاک خصوصی» که پیشنهاد خاویر میلی رئیس‌جمهور این کشور بود، پرچم آمریکا را پایین کشیدند.
🔹
میلی در کشورش به دلیل داشتن دیدگاه‌های افراطی مشابه با ترامپ و وابستگی به اسرائیل، به «ترامپ آرژانتین» معروف است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454855" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454854">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edef91be97.mp4?token=heEyQPfWoR-hl1n5zempfb72a2g7mWx0DWVasE3-rbM0AaDyJO4xJOlB90dXBP5a15JMs3LVkqTZW3aHELT9JFYD0o9NE754JijGVvqLaQpF32h6MF-C7UvSnSYcwLhs3cltzKgIsptfAWkgq-A1_V3NHTSYEDKDwGGfYRhAhRnWa3t1w1KccjxPos1g8Mdlgz2uEzBh32T4BKc_OJ3aeHghmtvSQNfv720cvMB7CsjRbqJnPlPbK2-7NaAPtEB9DbNG459lK6bwM4qMHYLf574__6c6CQZCEvTlxbYO1JoGhZM6YHH11RMiYVpu0db8DJbwaIuh9XQ887lrohC1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edef91be97.mp4?token=heEyQPfWoR-hl1n5zempfb72a2g7mWx0DWVasE3-rbM0AaDyJO4xJOlB90dXBP5a15JMs3LVkqTZW3aHELT9JFYD0o9NE754JijGVvqLaQpF32h6MF-C7UvSnSYcwLhs3cltzKgIsptfAWkgq-A1_V3NHTSYEDKDwGGfYRhAhRnWa3t1w1KccjxPos1g8Mdlgz2uEzBh32T4BKc_OJ3aeHghmtvSQNfv720cvMB7CsjRbqJnPlPbK2-7NaAPtEB9DbNG459lK6bwM4qMHYLf574__6c6CQZCEvTlxbYO1JoGhZM6YHH11RMiYVpu0db8DJbwaIuh9XQ887lrohC1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج‌گیری اختلافات داخلی در اسرائیل و آمریکا با شکست پروژه‌ها علیه ایران
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/454854" target="_blank">📅 14:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bjy6Rohq4bTz9I0lyVlIU5G4ab035V_AA_3zU5ix4g3p_A0Vb--d-LItAntxjEMp5o59sk4VHbT1YZ1-fZBeajLL_hA4JRKqONy0m7oSXW_JZdB0j-EYtv_B58ft0VOG96kzQlseVy1xdzDe9Ps2_GdlKegYrmp4QpVtZPzBO5CU-5gQN0H9wSJw8oEWlSGyG8kLwQhAaUiqgU7DLmSRRYVroS5xQxE1Woi0LNwuUTSdkvYLLTETLuR5tnaIt5PGS_ZF5LL_urFzItF_YA1JnBdhPnSt_Z8qzQZeaazzrFeHJ82YnSNlQcx6LULfzXu4Ijg0vULMsZPDtXgBBMxkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfqL96dw9mbraOjsCs9pr6pIoTdzAAFWi2hApo2eS28E59YKLN-4VlfGa1xKoCeP56Uh65RsibL7aLn-_z29_0zxNm_qKIzGNxFf3jA6yVbmRk8zINtpTDfR4aPxJjPAgQsvewmaVbWWlFhItcJvswNAal6gng2NIaoiTYqZRaveEmWJwtuHyHUQks9V9Alp8O1wN6P9_LBgSNQ8prXOYsJb6horLRQXyFaNJE8mMAg33JRXRXBQlsr1SHSatcQeH9bhBWhEAzXOM2JtUP5z41VSPqi-HsZsz36v-CytsETDXv0nrvUJKQtxAcMU_70qYqK1KaQxtB9gHyq6EWDoPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه  @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/454852" target="_blank">📅 14:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454851">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148682d952.mp4?token=ZIOMqrxZm-8ebRPm8VsZKbZzH6NXyhScsJ34d4UF0quFHPfxUGmU-mfbonKOTCtyI2jGtLnlm8m9k2z-JVAJyZ2ukJIg26PMWXvBRQTd4VjzxA8tk8rdJSBoGYimSwiVz6oho8DLJdKGO-WJ58hZkRX7TMWdLcvzQAGaHSo1StxztY9kQWY9NPiu0QxjI5BeFswijAXXvH8cHV6CdPWgAQQE5_1lmE7DpvCNvDCNz1lOh_mdVInFZO3WHIDc5iHuT_35B-F0h2bl7y3LN-0dO2_ygFnCD2ke3oJZFQ2leZmBChLrHdSEduMLMr3E47Jex-nSpwVfOmU-C3jDwR8uVCv933uq2_Pj8jKzqIDOr_zNYe4Rw1TexpCt1R5taNcwcAuEYHqP7CyFAjNNl4cWVfj5Em7CIOppD3WhaEdxojm6zBIZpnotmLnQMHtH8R-vy2FV9C5y0BssKSrB57O_AsuOVYkcUu3pk0JHNygSV5NXS3UyG7J0D1yftPvg_ZJWglp3N5OHusFHGOad9oT6_k0pYg3HLPKFbPAQKKqqYDG_M5z8ddXFLupu2Fh2zqnof8h-EtwoxlbQBoJQ05PSm8GDsVxXVh5Vi8GluoKhKydi8jHX0mUFkVhcxXbERZ-3AACj1Ake5cSC3f2WVpew2mfGqgsv-xhTxLdE7E8vZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148682d952.mp4?token=ZIOMqrxZm-8ebRPm8VsZKbZzH6NXyhScsJ34d4UF0quFHPfxUGmU-mfbonKOTCtyI2jGtLnlm8m9k2z-JVAJyZ2ukJIg26PMWXvBRQTd4VjzxA8tk8rdJSBoGYimSwiVz6oho8DLJdKGO-WJ58hZkRX7TMWdLcvzQAGaHSo1StxztY9kQWY9NPiu0QxjI5BeFswijAXXvH8cHV6CdPWgAQQE5_1lmE7DpvCNvDCNz1lOh_mdVInFZO3WHIDc5iHuT_35B-F0h2bl7y3LN-0dO2_ygFnCD2ke3oJZFQ2leZmBChLrHdSEduMLMr3E47Jex-nSpwVfOmU-C3jDwR8uVCv933uq2_Pj8jKzqIDOr_zNYe4Rw1TexpCt1R5taNcwcAuEYHqP7CyFAjNNl4cWVfj5Em7CIOppD3WhaEdxojm6zBIZpnotmLnQMHtH8R-vy2FV9C5y0BssKSrB57O_AsuOVYkcUu3pk0JHNygSV5NXS3UyG7J0D1yftPvg_ZJWglp3N5OHusFHGOad9oT6_k0pYg3HLPKFbPAQKKqqYDG_M5z8ddXFLupu2Fh2zqnof8h-EtwoxlbQBoJQ05PSm8GDsVxXVh5Vi8GluoKhKydi8jHX0mUFkVhcxXbERZ-3AACj1Ake5cSC3f2WVpew2mfGqgsv-xhTxLdE7E8vZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تبادل پیام خاص میان میدان و خیابان
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454851" target="_blank">📅 14:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454850">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وزارت خارجۀ پاکستان از امضای توافق دفاعی سه‌جانبه میان ترکیه، عربستان و پاکستان خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/454850" target="_blank">📅 14:22 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
