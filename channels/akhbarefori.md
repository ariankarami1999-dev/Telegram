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
<img src="https://cdn4.telesco.pe/file/GoxK92jFV1TD4kSacUT0namVFn_4mZHzbld4AdeZRTyZUvQK3LX8-qrXbdECKfsvB8KxpghfmuK2m5h9R5A5dAqdT4tcQtdUrUuXqOnhzmTZSeT3GzPjn_0UO6DKWkILbfUlaPbtww67hdjGMpe7EeYQByyydbTSLOqRtqGxxXEzzgprf5DK1mJm6pUI0NlsdXNX2H22kIiMsD401o0VH8il0UBaDjBFSWLNpXjKy-MfUr9K7tXgFOcL8PUcDufH8xGSWGtGtVpCjhLWNxmfHqezdOjrLn8eFO8IuqsFTmRt9kLMzxr3m-OAjt4xkG_PK6-huLK-8CkZr_AXKZ3o9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.16M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 22:44:58</div>
<hr>

<div class="tg-post" id="msg-665122">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOjFxBHxM_uKCERe3yVe1sctzC7J72vKKLY9WSQl26NiruXhFSyLODCCVNCIbEvwfD_-O1Cp1q2czF6Ql0zaSxBEPqZRmTdAqHZz6npoA-EwzdJi6X5bAEugmpa1K_zUHXug6xZGoX0muM-ECMDMfg4-AsaIqpGxAHqPnXyqmjoUUyLVzpgUsRKU7D3dKKI6lr9SQJJVmog1DF8dYg5FkMnVbi820p95VSlPSTbaDDxb-uUPk-_fQ7B2LbUsyY1qaBJdiz0fsSOnhfo_7LMTlIoSg2AZEx_iEgfyFZsAZ4W008iLaEfN9Sc98nRqbuSgv5e2fm5f8cZ1HwSFdyn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه کج
🔹
تنگه هرمز امروز فقط یک آبراه نیست، مهم‌ترین برگ برنده ایران در معادلات منطقه‌ای و مذاکرات با آمریکاست. به همین دلیل، تلاش برخی بازیگران برای سپردن مدیریت یا امنیت این گذرگاه به طرف‌های دیگر، صرفاً یک اقدام دریایی نیست، بلکه تلاشی برای تضعیف اهرم راهبردی تهران است. در این میان، استفاده از ظرفیت عمان یا ایجاد شکاف میان تهران و مسقط نیز می‌تواند بخشی از همین سناریو باشد، زیرا هر اختلافی میان دو همسایه، مسیر اجرای طرح‌های ضدایرانی را هموارتر می‌کند. واقعیت این است که امنیت پایدار تنگه هرمز با حذف ایران به دست نمی‌آید. راهی که بر نادیده گرفتن نقش تهران و ایجاد شکاف میان همسایگان بنا شود، همان راه کجی است که سرانجامی جز بن‌بست نخواهد داشت.
🔹
هفتصدوهشتادوهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/665122" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665121">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
مروری بر سیره حکمرانی قائد شهید انقلاب؛
«به یاد اویی که ما را صاحب‌خانه می‌دانست»
🔹
بزرگ‌ترین تفاوت رهبری با خیلی از مسئولان، در یک کلمه خلاصه می‌شد: «باور به مردم». در سال‌هایی که خیلی از پشت‌میزنشین‌ها تصور می‌کردند حکمرانی یعنی نوشتن بخشنامه‌های پیچیده و جلسات طولانی، او دقیقاً در نقطه مقابل ایستاد و بارها خط بطلان کشید روی این تفکر که «مردم متوجه پیچیدگی امور نمی‌شوند و باید کار را به مسئولین سپرد.»
🔹
او اقتصاد و فرهنگ را زمانی موفق می‌دانست که کلیدش دست خود مردم باشد، نه در انحصار حلقه‌های بسته مدیریتی. او معتقد بود در یک نظام اسلامی، مسئولان چیزی جز خدمتگزار مردم نیستند و مشروعیتشان به میزان گره‌گشایی از کار مردم بستگی دارد. در منطق او، نقد منصفانه و جریان دائمی نظارت مردم بر کارآمدی مسئولین، نه یک تهدید برای امنیت ملی، بلکه تضمین‌کننده‌ی سلامت نظام بود.
🔹
رهبری که می‌شناختیم، تا آخرین روزهای حیاتش به ما یادآوری کرد که هیچ حکومتی بدون تکیه بر آگاهی و حضور مردم، عاقبت‌به‌خیر نخواهد شد.
🔹
میوه و ثمره‌ی این نگاه او به مردم، خود را در روزهای سخت ابتلا نشان داد؛ آنجا که این باور او، به «بعثت مردم در جنگ» ختم شد و همین حضور بی‌دریغ آحاد مردم در میدان بود که سپر بلای کشور شد و ثبات و امنیت کشور را حفظ کرد. از همین روست که امروز، خط‌کش سنجش هر مدیری در نظام اسلامی، میزان وفاداری او به این میراث بزرگ است.
شیخ محسن رمضانی
دبیر نهضت مردمی بعثت خون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/665121" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665120">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9174733cfd.mp4?token=PxQpLOJ1a4isBdai3f3Fh_9RsgsU-aw8XKgEOsnmxII1gwOhG9hR3y4APRwdUFvpDze7VjVPISRzlGS8wt9fQUkZCaxKOKDJtdTeMkjllohXst5jOKlwLX_oSlUrFscw4vz50A-VV25lCjMkTCaMUlosekhwjNLoYKEmzNC-hljTnMItNL0d6yYT2HpYpe0SuAfM_rZCbSbxVatvsccQRuZ6BIBhlajzOFtSohyFuA8SwsmivqGs-RW6hs2Bocf7NPNvp59ulT4KAa-MbHpc0uaWpTYRu_C_YnMABnN_jBAipX0_NHBbyQNP4jC73rw407_SV1E7wqgRoWPkzm-K9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9174733cfd.mp4?token=PxQpLOJ1a4isBdai3f3Fh_9RsgsU-aw8XKgEOsnmxII1gwOhG9hR3y4APRwdUFvpDze7VjVPISRzlGS8wt9fQUkZCaxKOKDJtdTeMkjllohXst5jOKlwLX_oSlUrFscw4vz50A-VV25lCjMkTCaMUlosekhwjNLoYKEmzNC-hljTnMItNL0d6yYT2HpYpe0SuAfM_rZCbSbxVatvsccQRuZ6BIBhlajzOFtSohyFuA8SwsmivqGs-RW6hs2Bocf7NPNvp59ulT4KAa-MbHpc0uaWpTYRu_C_YnMABnN_jBAipX0_NHBbyQNP4jC73rw407_SV1E7wqgRoWPkzm-K9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدصادق شهبازی، دبیر سابق جنبش عدالت‌خواه دانشجویی: پسر پیغمبر رو وسط تهران زدن، باید انتقام خون رهبر رو بگیریم، رهبر رو با درهم و دینار معاوضه نمی‌کنیم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/665120" target="_blank">📅 22:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
‌
قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔹
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها و شهدا در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/akhbarefori/665119" target="_blank">📅 22:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7178bd3b8.mp4?token=uagIDhQpfp75ASqWTJQFSp3iwOkFQNSC3j2T3LM0Bgnjo2Lzrbyaun0phG-E3ESt_CzXfSy0Pp9ZoBQ6mtPr9upI3QktGo2Aahg1cq-E7zN-0rs6F4fJ3iUhfJ2fQxnMRgZ6wtIpCh5W4y04bL8JSZ39fLgbEuVsJune-IPYER3e0jJM9KGMV1W-Vysow808-WLAcplv8RktGjSXqE9D-xiJzIQP8EogRsMS4JGdUwOOkGMnhTbpfrE37lePi40Xo_-sChiBro8pIldzBxYcB1fAd8U9z6krlPFnVGmt1GIT8f4CL9CeLwpnEDySdiYYS4gYyikB97yjlCc3Z9VMJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7178bd3b8.mp4?token=uagIDhQpfp75ASqWTJQFSp3iwOkFQNSC3j2T3LM0Bgnjo2Lzrbyaun0phG-E3ESt_CzXfSy0Pp9ZoBQ6mtPr9upI3QktGo2Aahg1cq-E7zN-0rs6F4fJ3iUhfJ2fQxnMRgZ6wtIpCh5W4y04bL8JSZ39fLgbEuVsJune-IPYER3e0jJM9KGMV1W-Vysow808-WLAcplv8RktGjSXqE9D-xiJzIQP8EogRsMS4JGdUwOOkGMnhTbpfrE37lePi40Xo_-sChiBro8pIldzBxYcB1fAd8U9z6krlPFnVGmt1GIT8f4CL9CeLwpnEDySdiYYS4gYyikB97yjlCc3Z9VMJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از روزی که محاصره دریایی برداشته شده تا امروز بیش از ۴۰ میلیون بشکه نفت صادر کردیم
🔹
ببینید حزب‌الله و شیخ نعیم قاسم نسبت به تفاهم‌نامه چه موضعی دارند و برخی دوستان ما در داخل چه موضعی دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/akhbarefori/665118" target="_blank">📅 22:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665117">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=ZNnD1YuIb6Nl5SNYk42CZUzMjT-3ihLo0QYSdmj8RMwevv3xNfl-39FIdqELz0IP0nw9uX25CzXV_JGCQUysVaQaYZSJJ05UTRkeCstZGh1bB3K3H88O_jAkESss5qlduSWLLZhbPnRisPYCrrO0d2F0QbKG0GqFFNnvjL0jhK7xWthhaT9Y4OAL-Z23Zx11yJHh521f3EQ3zUULhR0HWQ__njeYJDJc7CjiLJ0mIDbJ9IMTQ7c9fe-zWDS8RWEWp2DQdVSE6ERzwYEj93zFp0UmS2Od4uiwj_3In30EaSak4XHIjO0pFsIgH95ckcDnArK0uwzaiydHBf_iwNdShqDelZHKFkkqDkpFYw9MIE656iXDHheg-lq6GhxD6ZWq3sShZrNyJLl6KXJIxY7k05lBqafNZc7WNXzABxBXJa0p1jVtIRi7gEYG-kFYyq_YdCBYLBZ2V5S4F-bG4e3kgkC47Ut-twLOecD1lNBT_yHx6vuv4rh760_ewEOUzCugW-vwzwtfO2IFbSiIw07N2AZ4i1ghc8d37Zf4TjjBUEMFBEeEdrt9XkRE0lGgqlLoVMGQdy_c_oLeUbc18g5StwhHC5zAbbr1uqlRtiWXlgQXe6A9mnztj8Uh8niIHG_odzlaaw4plDcYa8jGn9VIonkXNX8m0ggenmsBjKfO_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0f902f8b.mp4?token=ZNnD1YuIb6Nl5SNYk42CZUzMjT-3ihLo0QYSdmj8RMwevv3xNfl-39FIdqELz0IP0nw9uX25CzXV_JGCQUysVaQaYZSJJ05UTRkeCstZGh1bB3K3H88O_jAkESss5qlduSWLLZhbPnRisPYCrrO0d2F0QbKG0GqFFNnvjL0jhK7xWthhaT9Y4OAL-Z23Zx11yJHh521f3EQ3zUULhR0HWQ__njeYJDJc7CjiLJ0mIDbJ9IMTQ7c9fe-zWDS8RWEWp2DQdVSE6ERzwYEj93zFp0UmS2Od4uiwj_3In30EaSak4XHIjO0pFsIgH95ckcDnArK0uwzaiydHBf_iwNdShqDelZHKFkkqDkpFYw9MIE656iXDHheg-lq6GhxD6ZWq3sShZrNyJLl6KXJIxY7k05lBqafNZc7WNXzABxBXJa0p1jVtIRi7gEYG-kFYyq_YdCBYLBZ2V5S4F-bG4e3kgkC47Ut-twLOecD1lNBT_yHx6vuv4rh760_ewEOUzCugW-vwzwtfO2IFbSiIw07N2AZ4i1ghc8d37Zf4TjjBUEMFBEeEdrt9XkRE0lGgqlLoVMGQdy_c_oLeUbc18g5StwhHC5zAbbr1uqlRtiWXlgQXe6A9mnztj8Uh8niIHG_odzlaaw4plDcYa8jGn9VIonkXNX8m0ggenmsBjKfO_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میثاقی: به مردم توصیه می‌کنم در ایام جام جهانی روی مسابقات فوتبال شرط‌بندی نکنید چون پول خود را از دست می‌دهید / در فوتبال چیزی قابل پیش‌بینی نیست و نمونه آن برد اکوادور مقابل آلمان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/akhbarefori/665117" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665116">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBtngLzNbwJdUK18lPvs0PFXSNwZLcbX6wIOKZJwFsjdlfB-aSGFzyrop_vbmgbhF5hUdnZNOLzztR0bae_J8rzRcpldklflrSShChxdLIXylgbMafW-A9HTtSvlqDz0LRCwSaj1r6QbmRWMC42pFNwz9vme8OT3d5-QjIAHWVAVFJoSJj4KsPbybVKc-ccY_2RpTUTzt4EjGHlmwNBJitATVRH05VRatLr5n53M05lJm4WFXCto4A0RTAjazikagbRzkp7rE7VFzs4gJZBMybVuGT5tFS0DjUH84sJhBQOg__D8Yfqn-wjcSXaaXuUZPLMKyXw9aljWTqIMb24qFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در شکوه بدرقه‌ی رهبر شهید،
کالکشن جدید تیشرت‌های مشکی قرار آماده سفارش شد.
طراحی‌های خاص، چاپ باکیفیت و جنس نخ پنبه؛
قیمت اصلی: ۱,۴۵۰,۰۰۰ تومان
قیمت با تخفیف: ۱,۱۰۰,۰۰۰ تومان
برای سفارش پیام بدید:
@gharar_order
مشاهده محصولات:
@ghararshop</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/665116" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665115">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
قالیباف: اقدامات روبیو در کشورهای خلیج فارس علیه یادداشت تفاهم و برای تحریک کردن این کشورها بود/ تفاهم‌نامه ما استقلال لبنان را حفظ می‌کند  قالیباف، رییس هیئت مذاکره‌کننده:
🔹
تا ۵ بند تفاهم را نهایی نکنیم اصلا به مرحله بعدی و اجرای بقیه بندهای تفاهم نخواهیم…</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/665115" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665114">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
♦️
قالیباف: رژیم صهیونیستی به‌شدت با تفاهم‌نامه مخالف است و همه تلاشش این بود که تا می‌تواند آن را به‌هم بزند
🔹
تفاهم‌نامه سند شکست آمریکا و اسرائیل است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/akhbarefori/665114" target="_blank">📅 22:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665113">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای روزنامه آمریکایی: پنتاگون در حال آماده‌سازی برای اعزام نیروی زمینی به لبنان است
واشنگتن‌پست:
🔹
پنتاگون در حال برنامه‌ریزی برای اعزام نیروهای زمینی به لبنان و اراضی اشغالی جهت نظارت بر اجرای توافق اخیر (خلع سلاح حزب‌الله) است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/665113" target="_blank">📅 22:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665112">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
مذاکرات ما فقط تا زمان امضای یادداشت تفاهم بود  رئیس هیئت مذاکره‌کننده:
🔹
الان هیچ مذاکره‌ای نداریم؛ سفر به سوئیس هم برای گفت و گو درباره اجرای بندهای ۵ گانه بود. در گفت و گوها ما نتایج مذاکرات قبلی را پیگیری می کنیم تا محقق شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/665112" target="_blank">📅 22:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665111">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac4e8a59f.mp4?token=sD1dKg-xdFluXceqbJ6536CxCyphYaevYI8ZLKq6WiOTaYNDmqzInUdSZpzRgbU-mDVdj4XdrODgw0HGCzeXCmKtE4UPNgfRCjQ5vf3Bw1rBswoxymQsY7VuwhJVYaAtz6jSNly6_KSodxGDxjWSMFDMwUj_pF_7z8h2vaTT8HAqMncul6uK-UkrXeSsLppyo2Nm9OZYoABvZX817E-A6dlJHe6ZSm50TFXH5vO1w5QCRwjPTGIGWAjxCiouIfRhtkxP6H_edEfuppb1EUg_hqntIDVt03_rr8AiLkvKszQR5KNNbQA_iKLpRgwkgJhCLK21RpYC7up4XRR1E790PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac4e8a59f.mp4?token=sD1dKg-xdFluXceqbJ6536CxCyphYaevYI8ZLKq6WiOTaYNDmqzInUdSZpzRgbU-mDVdj4XdrODgw0HGCzeXCmKtE4UPNgfRCjQ5vf3Bw1rBswoxymQsY7VuwhJVYaAtz6jSNly6_KSodxGDxjWSMFDMwUj_pF_7z8h2vaTT8HAqMncul6uK-UkrXeSsLppyo2Nm9OZYoABvZX817E-A6dlJHe6ZSm50TFXH5vO1w5QCRwjPTGIGWAjxCiouIfRhtkxP6H_edEfuppb1EUg_hqntIDVt03_rr8AiLkvKszQR5KNNbQA_iKLpRgwkgJhCLK21RpYC7up4XRR1E790PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم نروژ به ساحل عاج توسط هالند
۸۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/665111" target="_blank">📅 22:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665110">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01faa4075.mp4?token=qF_boXcxamZjYd8txpgUBgscLwUoX7Nn9zFbU1xgKjGgbdBbgqzxW13khOMxWZCbt8K9bbCG-KmqZaHf0FwLfE94XBiXJliRRUiEmq2LT6BepMwKttfVSaJw5L6aPXBj5b_bl4tqBvPfhdpsFvPSFKHKPUJi7h54YTfF_6WRu4QA9fQMibBsTbDpnuciLk7TwVvq3vtT-d27O6WxNpz-ntLO1dVi4dfZNaQl0d0OCe52vXGUd57fic7ejAblwvUuL0HGBD2NoZQ347Gvt66aSJS5CdhGz7s_I52F0vnSvV7_ZG1RU1bXzJANe2GCkSkrWsWfcV9usAXLlK1o5e3olQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01faa4075.mp4?token=qF_boXcxamZjYd8txpgUBgscLwUoX7Nn9zFbU1xgKjGgbdBbgqzxW13khOMxWZCbt8K9bbCG-KmqZaHf0FwLfE94XBiXJliRRUiEmq2LT6BepMwKttfVSaJw5L6aPXBj5b_bl4tqBvPfhdpsFvPSFKHKPUJi7h54YTfF_6WRu4QA9fQMibBsTbDpnuciLk7TwVvq3vtT-d27O6WxNpz-ntLO1dVi4dfZNaQl0d0OCe52vXGUd57fic7ejAblwvUuL0HGBD2NoZQ347Gvt66aSJS5CdhGz7s_I52F0vnSvV7_ZG1RU1bXzJANe2GCkSkrWsWfcV9usAXLlK1o5e3olQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس مجلس: اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم؛ اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش‌بس می‌دانیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/665110" target="_blank">📅 22:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665109">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=qqylR6tZm2dQl0V4h91Oo0eQ04eozfqpU-yvlMcyJxnaF2jwmcGa1GLO3PI2hq3c0PEgJeu3AERjPcAA2B8b4YvMDtbp58DFrSBJmx7urYILb48W3Drx1TZTENqymGj6WC6pRFQG0vLh8SzFsIvfK_2DiZDnKrUgQWTNCcqR5IXfPFhi6HjTIR0raoOkBctfKg-QbtKrBcVYNr2wFOIsAf1fOEmhGIg5aN5ZGWc2ct9xDHz2dv6vXZ3ESNBteG9tTIqu3ZjPSXAk0es7NfPHqGLlC3b8gxs95Z-Dm1lDPJO93Ty9vaB_qamcscP5tmMzQOI6t5oNS0yQr2JjLnanWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=qqylR6tZm2dQl0V4h91Oo0eQ04eozfqpU-yvlMcyJxnaF2jwmcGa1GLO3PI2hq3c0PEgJeu3AERjPcAA2B8b4YvMDtbp58DFrSBJmx7urYILb48W3Drx1TZTENqymGj6WC6pRFQG0vLh8SzFsIvfK_2DiZDnKrUgQWTNCcqR5IXfPFhi6HjTIR0raoOkBctfKg-QbtKrBcVYNr2wFOIsAf1fOEmhGIg5aN5ZGWc2ct9xDHz2dv6vXZ3ESNBteG9tTIqu3ZjPSXAk0es7NfPHqGLlC3b8gxs95Z-Dm1lDPJO93Ty9vaB_qamcscP5tmMzQOI6t5oNS0yQr2JjLnanWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس مجلس: اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم
؛
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش‌بس می‌دانیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/665109" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665108">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72bae72ea8.mp4?token=QfuG0fae51GGS8LNkpI0SMIdcx5uteMkp1w5G98sjQ52JuXzrG4XL7-Glz4cOzCz1pzaliWXWIDo1Ec3dIzpBGV-q3GCnOpMyrY5RkNfjlA9wtuCdFMXmfISflsX_BSiZEXg9fBRQs3kPyAQnBnExon3NAm_F5PtQ6J8QY_sieWTUUjrLYgLDLH36EikHr_huG2pTomHbSNbVAvN7bt42MVTtjnztiqIVOaY7NBLkX-89zdSL1tMDW7QMtN7diq4Py7Wlfr-mCkQCkN9M70d80xbUEWVldxrFUuEvQnNvwx1KhqEMXLFfCg9nWG5A6aeuHw-6iends2RqIgwc76Xrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72bae72ea8.mp4?token=QfuG0fae51GGS8LNkpI0SMIdcx5uteMkp1w5G98sjQ52JuXzrG4XL7-Glz4cOzCz1pzaliWXWIDo1Ec3dIzpBGV-q3GCnOpMyrY5RkNfjlA9wtuCdFMXmfISflsX_BSiZEXg9fBRQs3kPyAQnBnExon3NAm_F5PtQ6J8QY_sieWTUUjrLYgLDLH36EikHr_huG2pTomHbSNbVAvN7bt42MVTtjnztiqIVOaY7NBLkX-89zdSL1tMDW7QMtN7diq4Py7Wlfr-mCkQCkN9M70d80xbUEWVldxrFUuEvQnNvwx1KhqEMXLFfCg9nWG5A6aeuHw-6iends2RqIgwc76Xrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: جنگ تحمیلی سوم یک جنگ همه‌جانبه علیه کشورمان بود؛ تعهد آمریکا برای پایان جنگ در لبنان یک پیروزی بسیار بزرگ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/665108" target="_blank">📅 22:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665107">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkDneAmMfW2stPcGsWSW_GuLb1Mjdbl1BpEd1gJdaVdrtZ2Z807uIlUYi9L527crlWTZKPTOXNqxtyASvz6tn4dAUgs0GyDdYbXHOuHjseDkE3_fSX_vctwOgPG7MjYRTgxgvXwfdUY_vc5y4jPUe-9hB7z076F2WURES07WM2oQP23tBaOG7MKNA0mxL_kSCb34mswZro9vf_YuPoiJ1rGlx6fSbg8OobFmGI9cPNeOdAwycBW6yPvMsOWLILK22JJ6JFOSteiunIRMdAkzoOBPpV_PEGLqLSegn2Oovvf6bSuq5cLXZh-GubPdpn9siKqO273NjC1kBXDlJbDGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقام این آدم از شهید کمتر نیست!
🔹
امام علی(ع) می‌فرماید پاداش انسان عفیفی که با وجود توان گناه، خویشتن‌داری می‌کند، کمتر از مجاهد شهید نیست؛ بلکه چون یکی از فرشتگان خدا است. این سخن نشان‌دهنده عظمت اخلاق، عفت نفس و مهار شهوت در اسلام است. نمونه روشن آن،…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/665107" target="_blank">📅 22:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتاپ تورز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f234qoh26QSvfJDnm4kzGjgyvCkoOUblRWvAxf_lOTeH5cSjeayL-fESDRlZTRqa12bfOouBKcBIMF8hSPUxkN5hfKyY6pavw_l5JI8xaTp5p7tbCYMbTerv7aFNQsDPrC3GWzjGhn9VRB5Yy_f0Vq_prMIgRivtdasFnwp-pbVgHDAlzueA3USVAPt2R7eNOIGxyQBaFYUFM9ucghHGvtcDPbstPy9PCuBrroZg7tSqZ67pGwVzwi_mhJd9BxIlLmtzZrRTHHtMYVNQwhcc7FO0cFnhD_Q7ai3pINsHcphO2CMws8ZhRhr0RB3Drl06Emmj9tH6fk2X8KKMSjKyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آغاز فروش پروازهای هواپیمایی سروش
📍
در مسیر تهران - کیش - تهران
✈️
ایرباس پهن پیکر A300-600
🗓
از پنجشنبه ۱۱ تیرماه
خرید آنلاین از :
www.Booking.ir
📞
+98 21 8586</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/665106" target="_blank">📅 22:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665105">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=t8FAWAMoAm3TWEwCASAfJEDCH7dhkOBbmCxFXLGAWXaPy0plc2nmatooPpBv1hMo1_ranclJ43G-Ffd9ESEA2yHJhJrLMEpoJYH1zdgctG5_U5B5-DyPZgFRmX5I1LA9fiEdAskxvLDb5zNh-a9sDui8vlUa7_I5DZuW-Z0GBi6bRPKUUnpS0UOC0EkbeHIGUcrQ2F_Y3qFPLcBOChP3mQYFTwrYJEK_F4gJNIf5jh9Znvj3hwZvj7GhckuK05yXrEACR-b_E46crJm0b_oLZlOuP9WS8OTML4i7lCKt-AOsBLiRd7PCM9I-RDpIAn5Tj4S2izNiGA3awLAtUM1i5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=t8FAWAMoAm3TWEwCASAfJEDCH7dhkOBbmCxFXLGAWXaPy0plc2nmatooPpBv1hMo1_ranclJ43G-Ffd9ESEA2yHJhJrLMEpoJYH1zdgctG5_U5B5-DyPZgFRmX5I1LA9fiEdAskxvLDb5zNh-a9sDui8vlUa7_I5DZuW-Z0GBi6bRPKUUnpS0UOC0EkbeHIGUcrQ2F_Y3qFPLcBOChP3mQYFTwrYJEK_F4gJNIf5jh9Znvj3hwZvj7GhckuK05yXrEACR-b_E46crJm0b_oLZlOuP9WS8OTML4i7lCKt-AOsBLiRd7PCM9I-RDpIAn5Tj4S2izNiGA3awLAtUM1i5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: اعلام پایان جنگ و رفع محاصره دریایی از نتایج مهم تفاهم‌نامه بود
محمدباقر قالیباف:
🔹
دو اتفاق مهم پس از امضای تفاهم‌نامه در شامگاه ۲۴ خرداد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود. او افزود ایران در حال پیگیری گفت‌وگوها برای تحقق ماده ۱۳ تفاهم‌نامه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/665105" target="_blank">📅 22:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665104">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b154b416.mp4?token=cDZyMvTDnpEevqE2KOlppVF43luNSgR9TtqpumMMIp3ToeC2F0tEnGKbrAoupbOEpL4m-NRPgSl3Yyt2ZmcjsPBUfctGcMX_fE69nQOz0kRgSpU8EGINzDqjoHlhC1B1Va3QZJSwR-bX-6lW7olmQmt4kWKa2tN_XEPe-OfYgwS9iecIHb2aHxjkUYgziWTCFiuScOjOYLQfOGn14UDZxMOfitd9noxkp9MRFE5Z7VdyByzAAwgC756vJ3JIW2ZoHRHPPle2-vPB3b9sbvrspfp0gANqpgSV9Jxy5pT0mJReDt4KEW-MzpX1uLqwnRzShJrNvqnMTddzy8ubffAq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b154b416.mp4?token=cDZyMvTDnpEevqE2KOlppVF43luNSgR9TtqpumMMIp3ToeC2F0tEnGKbrAoupbOEpL4m-NRPgSl3Yyt2ZmcjsPBUfctGcMX_fE69nQOz0kRgSpU8EGINzDqjoHlhC1B1Va3QZJSwR-bX-6lW7olmQmt4kWKa2tN_XEPe-OfYgwS9iecIHb2aHxjkUYgziWTCFiuScOjOYLQfOGn14UDZxMOfitd9noxkp9MRFE5Z7VdyByzAAwgC756vJ3JIW2ZoHRHPPle2-vPB3b9sbvrspfp0gANqpgSV9Jxy5pT0mJReDt4KEW-MzpX1uLqwnRzShJrNvqnMTddzy8ubffAq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل تساوی ساحل عاج به نروژ توسط آماد دیالو در دقیقه ۷۲
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/665104" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665103">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stFbzxo2NdiIrEw1CM4S2BlwdLo8JBJidfocsDSykXeIMP3qP3rt1lI8fioI6EYe3yzsEi6JgTKLlM_c424SCY0Ce9b4rhJ4loFUGYT17IdsE8sK7u2erW8bLCK1FkoGoBP5D1GZOyHYn02bHKeV2TUf4gS9nyvr9Zv25kQ5zYmcA_4Ui7AsFE218dCTLGigc2iGqSDlxkKT3By1j-b2Cat84gyMeNwCAcuvSP3lzCQ4XzSJVGL-k2xZ5qhCcq0zslcuiLlNPsi585JkDeMqb66jMbQReNSELcectW1BZFbX0yz-RVRicWrRgpub7EHH1dqfz7oJqzVYUlxVtvl2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طعنه ترامپ به چینی‌ها بعد از رای دیوان عالی آمریکا به دادن تابعیت از طریق ولادت در خاک این کشور
ترامپ:
🔹
من می‌خواهم رئیس‌جمهور شی و کشور بزرگ چین را به خاطر پیروزی بزرگ آن‌ها در تابعیت تولد تبریک بگویم!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/665103" target="_blank">📅 22:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCxlrWQ6zgVDo9y-RhcWLcp-xStXu4OgsUVjawmn2KxiB2SKEZdDq1zZQsDf1EKePTHW-dza8VhQIpV_YNxqUgjVwKjT5aHNQ3eor9Cy10tfZHDVsoYJdd8Ny_q1CQaEH7ogff4YP9hWxBm35QhbKFWPWsPjfknOoCLKAMw8M7i23ERajZyetfszgCY5GBc0bA4pAbD7Srlf5wxrp0cXzBiW4S8lnHL4j6oeyk1Nt8XsNPkLyKJINPE4mp9bhp4qHPFaynZ_06x9wrbdoRXl1PL_T0JpRqbewrjeNceOVxeB3xcNahvbYsz81iI__NtBlScYRvUaY0OmHphzXZVdTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aq6trZlPIhRt9X8Fbf45kpl9e6F8faDg_BVuHcQM9vagAN3R_4JyMBvFddF29To2hjfZk-I81RGs2gKM7JeGM0qmC4keTcYH8yKjhQ3ufPiUGkv2aYV7VDAWTlgNhz1WULM5zZCPT8X2awPEeyIt7eiIrK4g_gzZ2958lWq-a84ngkH4dLQPVyA60-IRMn6vHftxdf1vtmr9uTt0c1OX7PoNdH7OLEykOX_WCVUiwQ7ZMrdXnFIVmSKFAmBSwfrsRBzxfLW6ZbK_TnmPm_MsI7slUdX4ltiTvKVkEzFvByMJRftBuNLFQ9a86OScJEcxyw3qZJYvZkyxcTZCJ4SC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EO8-Wdg4FUzaEKdnlPYrQlb-Ck8W8jtV1hvT4UpyfxJTAb9N1wxtsTPVnDpVK7YMyReBIisHYJ7XJNMshp66bgFrkpWZjsUzk-yW8eKPfh4FBk65FAdpJDU7-ooZUYt18gsaG57O0KYHE4Z6iB3AY0UTZjogNZyvvsOj8eYmUloL4fNLRCUvDpJysV3jaLTgr9hmSr8Lk-WczhC1h9BbR6fWsPzk3A8Zzlgo7WHp76c7LRZYa2ZACD-oLCQaLDW8K6fAYtlY18Qjb4J3t_MaffNvv7Yw-7DqVRgP_vBPNmETn_XVsAhhKJ7NevUGwPZ8Ei3YSepbCSWUdfQ31Dc_CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tELq5bVhMtVDDMyn296b9IfBsgqH1x4lO7rG8kWvQTE3X-NImlwU4gKawSBJzYjs92Z3jOBx85QGhtFRvNYZUYCYOFlvzpQax2sMI3zWg_s8RKqSbASc8CVlgbOowm8IojedOotgEzKRVaNyJLHqHlth0klHVlWIjL6oVI71UjFG7hb41EHoBEi3sUI5bQWqGA8qoplkLMb6aMvH0CAdwdxcO19m8cJzC5BEzLDihmio7-XfP45AJlJnRUHg3lAXIdtedRNP_DAX5bVfEpyYxDTPyQ8_uXS23R0W7VRu8pAm-YrVnHQKKYCD91s8YyauHp-qmgSPSMUPhGqLZJPEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hx_mQF7wj9mKY9SZs0dzrlexfWUv70ce7un96ETS-nyM9pgILwuA3PbtW0FiyefQPYJ61mTQ2c6oEqL-xn-fxd2kqY5vpN3v7owSoXPhuZ_8YXIeKAcdtjyy5UjQa8IgnlZ5fXN5minpBlBrTsU_zwlnhjZr8l2Fadc-lW2HEtNA828o0fH9exVyLJynnmwCWhnwBtt04mzAEtrJaCQNOsPZh1q-chPEXXhhwBaVMjihAs2nZX9wrO5-TBMv7v3Ve5UByUPaWVHH-cw6LH7T2xK74_6NfWhr2EJJN_t2CuINdDffgCz3SkGT7cSKBx25avywzHZBOn-Aw80vZ6ichA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgiTCg-nzO7LFvVu8mJvvhI6k1e__WqM8HfaoWB8DnzAPfqH8ftB4sv6Cy8oFv9r8ymGF1GlWcv05e3kKLD4K3SVY2K4MgbSYfsiGFYfv02f2wBos6mqUPxhwVtD_VTqwuoQkf3-JlsI_oXuZkGXPDlLES8_Jgzas0tlYDrYSybTSWbiP2lml6tJ9Pp4QA_0E2Xxs9ji5jqdl7qnmh11NaJ4JHdMqq7bpVSrr7Jos7WFtgtNiOoL_R2UrAPxO1gTW6RMExemJirTFhl0VLZCVF2-QfvT-pJtN0FXjDIIf5VYcllXpEo3BJT5wldnwiDeXAkkW2Flv7QaSrelaCqqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERRmd9YAuwUJjbfrO3ujG2xne6nlPEcFTqGr1KNcQby_12mz-7Xfb8IFsRKZri14ljCxXvIFGSN3Mgr8nsnwnN9-DBvKNzw-NYnruAu7lKWadroL_qsDeh30SzlhOw-DNByCvKMREZLwXAqYwmRDYUBa-CyJWObo-x8g9TlQFdI4PNSGxbw0_sU9zhd4TTGvojJ7aPZmJpns2Z5aEV0bFfaIL6LX0QkvTXlWBb9KQsqOL6SNeyPwt141IC9QSvcjuFNqal0SA7wVjLOYDE2MzW8YSYoqSP6B84a_rHKrYXXrI2F3GT84vLpdgL2Gw2MGle9_JrxC79mTm5zlf-KtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBHHtUB16Ww-Pnb2XtjyNt-5KZLXMKhyAedngLrfYAMWosmvT-Z37CJgkQ5wiRmSXZ41Fljoj-HTGB5gef0t-TKMM3OclKRmWCVLOyb0vzBdQnGVTJ1NMgaTp1WlZJNcLtMBvlTf9J11FD6k6VvhtxQSPXAqaHbUQM1nHrUegaMyPpzNu7p8VTXtHLcAluT_7CMKiwdrhTF_8gcuyAMfvB2oeHcwrpTBW2MuwDkma0ngbHNn5YtheMGQYdbbx6zNWE6W7MIHekcwtjO2qg08j_vB8Ri0E6nJM7xpUEX0teeLKt1MNlx3n2AcMJoJLMK9urqq0Mx3mFBJ7eLNPCMyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fW9-WW4lcWVM9ZkcFO0vE8C9_q_ZEPxilJykDwMm92SW4u4LFiAxs_iRiNyfTYoEhPuHdk_l2ysjP4Fi41f_Y5XpLq0mo6JXqQKy71SMmGvbbecHeUAXspnC9IBE-3xR9kRusgd7ZEvGiEh2wUid9o7GwTUei6vAyetZw5r7zDEBeg7hU2kDo9SM2fFix5Bp38fhxOTNrDgILJ72AHFGjz827QaYvEEfRoUMd3PbEtY_OXRuwa6TsvHfCgQOLb83JxZBc_AvZuVsd7UhGXTvT-t4CfOifn2EyBLKG1W6i2bmZjNdo9nJN_l7RVv03UGY-at9CmDF5dMQrXRs31nVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AMezVThGS7APVqWGpnzzRuYCGo9O4A45cPcOBbVJaw1JQVPyu_u5ukbIvmOz7dAeXL5m0TOWbFoR5nJ50jYq_R4lBjMTPbuLVDgMtD7iR0gc_oH20WFV9g6OQ_v2Q8tNcl8CJ6UNCB6159rZix3VcWH5UsT3wNTN-TFa3vBwkQ6Cw_m1QQcAHc3TjcyX04hyhNfk1_VgQaa9HVD0WKcV1col5XdytkbQI1E7XLjyXzHQAZ9CT1ki_TBYzpolm_HkIkiZRKJ0NpRka2hdbYGwF0gNodVxLEO985eprqK4KmFvyN_S7LJyjGZV7TL2wN_vhJfwfXkt_xyr9o29WRQqaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از اختلال اخیر در بانک‌های کشور
🔸
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/665093" target="_blank">📅 22:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رژیم صهیونیستی باز هم آتش‌بس را در جنوب لبنان نقض کرد
🔹
منابع خبری ز اجرای یک عملیات انفجاری توسط ارتش متجاوز صهیونیستی در شهرک بیت‌یاحون در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/665092" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66378b9292.mp4?token=Za9xq56-BtyInlA_N1Z4lOnaoVWwSnVKcqYbyNp3eADgJvprGiyHPI_XVSOmxvjzSlONzSQYs7yCDuYpj3q5vrhsXIYYqEgX22ZLobQMi0lAu96AsmrMhieDp66wyilh_l0psu0feKIVjA1hAg2zSE5nuV8wC4A06RSEbuwzrBpYs-XDCJCHk_wxi_7egcufsKvDLhW3vprdTTfE-Gt5kvfiyAGxix0uFUdhsmRLBRre7mJ6NQ4eZsi4t_ZYNkcINSxAyx4UVENtO8nzM2yXlqgSxiyBUe2CluvhlP69vlmL9YuOVVHZGld4-966N4AVDhdNK8e0GJNkL9JFABpX-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66378b9292.mp4?token=Za9xq56-BtyInlA_N1Z4lOnaoVWwSnVKcqYbyNp3eADgJvprGiyHPI_XVSOmxvjzSlONzSQYs7yCDuYpj3q5vrhsXIYYqEgX22ZLobQMi0lAu96AsmrMhieDp66wyilh_l0psu0feKIVjA1hAg2zSE5nuV8wC4A06RSEbuwzrBpYs-XDCJCHk_wxi_7egcufsKvDLhW3vprdTTfE-Gt5kvfiyAGxix0uFUdhsmRLBRre7mJ6NQ4eZsi4t_ZYNkcINSxAyx4UVENtO8nzM2yXlqgSxiyBUe2CluvhlP69vlmL9YuOVVHZGld4-966N4AVDhdNK8e0GJNkL9JFABpX-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین روند آماده سازی مصلی تهران برای تشییع باشکوه رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/665087" target="_blank">📅 21:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665061">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تکذیب دفن امانتی پیکر «رهبر شهید» در حرم حضرت معصومه(س)
🔹
مسئولان آستان مقدس حضرت فاطمه معصومه(س) خبر منتشرشده در برخی کانال‌های فضای مجازی درباره دفن موقت پیکر «رهبر شهید» در این حرم را رد کردند و اعلام کردند این ادعا از اساس نادرست است.
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/665061" target="_blank">📅 21:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665060">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRCMioB_EYvokirMlsaDTj0L_zKEyyb78GI8QQbRYbTxi906WM0hHUQBC9gGkZI90TXRMkUGbWbZffjcu898AWsM6A58ZNGf_oVWHIdweBavL6uClnP4_25aS9pDmgY7XTiBtmt9mtV7Ute2HjkeXi821PemuTIJMKlExh-YOPShnisg5ly3uRtV0I_p6sQSMkrO8dQOvTy9xPa85F9sYE6pGnB-eV1jBlzEyWH_1W0oepYOXijZAD4mEQA3TeQ_aE_KPLrS2tz3NtI-or59KSGFhuIS-ORUFRtIs5sKDlSxkFlgMuTygRCL8THdAp7UaDOdH--6g7ipmpmPI7TbVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت‌های رویایی ۶ سال پیش یک رستوران در شمال تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/665060" target="_blank">📅 21:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پرداخت یک‌میلیون دلار پاداش به قلعه‌نویی پیش از جام‌جهانی
یک مقام آگاه در فدراسیون فوتبال:
🔹
امیر قلعه‌نویی معادل ریالی یک‌میلیون دلار پاداش حضور تیم ملی در جام‌جهانی را پیش از این رقابت‌ها به‌طور کامل دریافت کرده است. این مبلغ با هدف تقویت روحیه کادر فنی و بازیکنان پرداخت شد، اما تیم ملی بدون پیروزی از مرحله گروهی حذف شد.
🔹
با وجود این نتایج، مهدی تاج بر ادامه همکاری با سرمربی تیم ملی تأکید دارد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/665049" target="_blank">📅 21:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czPPekjoAtLAxeo9ylmZ_jgf3tc3yEwKRYt8kLvXYSYKjU18K7y308JeFsqu5hNYS_Puko25AIiuG4VC3_43-TP0BBGF4GPrqbKAEcgKWIfoTAboWRG95qkDMZT_EyaNlRoVn6suD05XPKHcNtuPh5QXMcy4CrVFJQJx7SirsC40eaeoiI1vUMnYHDZ7aiw28zY-07aTUbzsmYjZb2fCyXnv2EbjcXdzlYSq1Lu_-m-i7z1jt_J8J7O5EEU8PfKBnTWiQeRb4UDupMSPAkKXJpR_KxSQdO44RSzyF2hX4lMm7Aizp2M8m6OmJ3CCf5ITT0FlL4WURja7c_6zmn1wWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی سریال: خرس ۲۰۲۲-۲۰۲۶  | The Bear
🔹
ژانر: کمدی-درام، آشپزی
🔹
امتیاز (IMDb): ۸.۵
🔹
خلاصه: کارمی، سرآشپز جوان و نابغه پس از مرگ برادرش به زادگاهش برمی‌گردد تا رستوران کوچک خانوادگی را نجات دهد. «خرس» روایتی پرتنش، نفس‌گیر و واقع‌گرایانه از آشپزی، خانواده،…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/665048" target="_blank">📅 21:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665047">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bdb2e333.mp4?token=YiBDKtEho0hpBs574-_wy8DrLOj8EOxhdUUI9zugsABjRflCpDIUfJUBHojmY6sh4_wi_d-JOvH45rtKF0uL7DSgtQrkWlvPP8EpZnUb6-QkBQUdqeblVsJ59XXKkQr7uAkM1wci88SomlLg_BYg7kI2y1rF2RpttuVSH9igE7rDuqzQXqEKxyWd82FQ6X0m1pYe0O6CPBYXzqNssqfdshjZoMqhEJCJf9dqODoA1tqfXca_78aqYsCjepHDvqZ1LsBWEQKuhwqcjDOSsXdyuKec0hXEwfsn5y1PtW25z72VRyY4NLjVbbAeTG0x9hjoEMiwSVIxaoCvFNyiPk427g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bdb2e333.mp4?token=YiBDKtEho0hpBs574-_wy8DrLOj8EOxhdUUI9zugsABjRflCpDIUfJUBHojmY6sh4_wi_d-JOvH45rtKF0uL7DSgtQrkWlvPP8EpZnUb6-QkBQUdqeblVsJ59XXKkQr7uAkM1wci88SomlLg_BYg7kI2y1rF2RpttuVSH9igE7rDuqzQXqEKxyWd82FQ6X0m1pYe0O6CPBYXzqNssqfdshjZoMqhEJCJf9dqODoA1tqfXca_78aqYsCjepHDvqZ1LsBWEQKuhwqcjDOSsXdyuKec0hXEwfsn5y1PtW25z72VRyY4NLjVbbAeTG0x9hjoEMiwSVIxaoCvFNyiPk427g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات تازه از مدرسه میناب
🔹
تصاویری از حادثه مدرسه میناب حاکی از وارد شدن آسیب‌های حرارتی شدید و سوختگی‌های گسترده به قربانیان است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/665047" target="_blank">📅 21:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665046">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLoCLXG2rJdKoTlLuk4GxkMsQOx28JVIyhQRXMHQb5_In20mbAUy8AeXVW0eLqIl_i7n-QgP6cAL1qorF-MSkZtM6zaewzRd_DooViMcLytu0KfKn1_iQrYMMvPX7XqbeMim5oiWYc8s99Sndasg6C_cxLp5wlUTn65_I8yUmcKJTsXjtf3_iPhlQfTLH5dyZ0ErmsIIrU1bXFOxloUiJ9ix17z2rs6iK4yG5m0J2PpW2FY8kNpyHKAL-EszNqQQ4SukC21MH34sAZ5ENkGkWY06gLUe4Qzw34azOR6KCPVplbk7TAfT5rXWpOZTlOf_Tk038teiPYtMVnygyC4bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر امنیت داخلی آمریکا: پس از حذف ایران از جام جهانی رقصیدم   نشریه اتلتیک:
🔹
مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/665046" target="_blank">📅 21:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zb6tx6Wd_THq6RcF18i2FxKDTpdHRxS-GbpkSm4t_S-8DZF965fW05K8ek0X5HopdIFiPpjoDZRTLmhHzISaTYDAFg2a2aGIwpmChj2S1CB9WHuv6qN2AhriDBXXOqvYEpqzJGvohVibwICg58DGIxgx0DuW0LNWiHqUi9KmXNEd0TJ5MM3jy35NcHocI6INgSGTwccKPlPRmSINY9uJC3xKJyWDgdqsGNWhzsf-8ChJryPH6bR1dfS-jIbSro9qXuSTxrcjYNjX5oL2UadcHFAW9Aj5TjAGib7AJdV-iDR26ygunnM9IpI85Vha8GoDpuvOEOTtywFRYdil3rETew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
عضو بات صرافی دیجیتال کبرین شو و تا ۵۰ میلیون جایزه ببر!
بات کبرین چه امکاناتی داره:
✅
واچ‌لیست و قیمت لحظه‌ای ارزها
✅
دستیار هوشمند
✅
رصد فرصت‌های ترید
همین حالا دکمهٔ عضویت رو بزن و شانس‌ات رو امتحان کن
👇🏻
👇🏻
@kebrin_bot
@kebrin_bot
@kebrin_bot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/665045" target="_blank">📅 21:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خطوط 4 رقمی و 5 رقمی کسب و کارها با یک تغییر بزرگ
❗
با اعلام روابط عمومی شرکت رسپینا، امکان دریافت خطوط ۴ و ۵ رقمی دوطرفه بصورت انحصاری توسط این شرکت با برند نکسفون (Nexfon) برای کسب‌وکارها ارائه می‌شود.
🌐
جزئیات بیشتر و ثبت درخواست:
https://zaya.io/nexfon-info
0219222</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/665044" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvvGTykQj3ZtpbohTZ4WZF4CuN37WiRDEI7Nf0C06Uwi68MMVijUW2d2CvR4qoXPeW-_oKrS6fJKT5Rm3CsbLoKR60hPrCKUeX1aM-OpjXkvV4mo4mj2ejbvwnygCFn0l5WLnSMeE-is8PAfP7B8em3uwMNgYrBZ64bhdUQ-8pqG7i-KvRiQqPjz7pelmBuY5fUBlPqzJCy3D2_zexAI0uNt8UaNH1lobrpWnPDwHxOW_RrM0-JvmG_wLc4LbEY0H2if6JnJj5qEoyGa7OfBRH3WdpIIOjYdO4VQhCa1ZBGIETnRneZemjycZLbJBZ09K5FJB_25PISjVd4z5OK76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از تابوت آماده شده برای پیکر رهبر شهید و خانواده ایشان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/665043" target="_blank">📅 21:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avs5GtrqV38ZUUe1PImkPt9FswAaHJSn1-hAPG5_y1EDH1KPASvMExOAwgvw9JAuLeBEdyNZolBQK7WDdVEslmB15shiWMObHcCYWBWjpy4f_0i5F55f_fuS4ucPG1aOvmXVFkTGAlpcAJsjQVGPN-O8eEtyiGPnLbZAdErzFdXfMIiREZ4Jb1PVeyR0GFaLLRAoyoSRKyR7IVw7EE59an7ktY1TmzjyKcX0gl_9cyH-OINM_bgS_oVyyDoUWcb005lCJ8Aqh2K9RjDWJavE20MEi5NOzo1_WaVryOgZ-B8WLCu1kfdR9GlAT6nBL2ieeeyjL9DOKWqPKE7-0eLCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممنوعیت صادرات محصولات شیمیایی، پلیمری و پتروشیمی رفع شد
🔹
این تصمیم درحالی اتفاق می‌افتد که طبق گفته کارشناسان در داخل کشور دچار کمبود مواد پتروشیمی هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/665042" target="_blank">📅 21:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8001621dc.mp4?token=lyafu6RBeg_ARrQBTW9_AH8hhhloCPIICjk7E__DCYQCJejGQ35czi-WFa0nmn8CtGm8607tnWBWSbNJ8bkkLUX3BVlYNAOo4vrXt4fnC70ZocU0UoSTSDLvJk9-fTLc7kejwhdCuVHszFT8mh_tj5n4WPXCjsUlVSa4qSH3FXOSXoiDM09jhAWwF_rUp5NnRQKcqjHlPBRkyyGQ1cIDH7MmYS4Y5S5i5BKy80_kqNEjLob3SY3z2Zs2Fwy4kLq7RlWGcNP1YthZU3l3VRcpCLNhWYaKI2K5y1asovYvqQTzD6UfY4xWsnkhfGcJ9XUHmflt4hFU1GYH02zlfAN_fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8001621dc.mp4?token=lyafu6RBeg_ARrQBTW9_AH8hhhloCPIICjk7E__DCYQCJejGQ35czi-WFa0nmn8CtGm8607tnWBWSbNJ8bkkLUX3BVlYNAOo4vrXt4fnC70ZocU0UoSTSDLvJk9-fTLc7kejwhdCuVHszFT8mh_tj5n4WPXCjsUlVSa4qSH3FXOSXoiDM09jhAWwF_rUp5NnRQKcqjHlPBRkyyGQ1cIDH7MmYS4Y5S5i5BKy80_kqNEjLob3SY3z2Zs2Fwy4kLq7RlWGcNP1YthZU3l3VRcpCLNhWYaKI2K5y1asovYvqQTzD6UfY4xWsnkhfGcJ9XUHmflt4hFU1GYH02zlfAN_fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول نروژ به ساحل عاج توسط آنتونیو نوسا ۳۹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/665041" target="_blank">📅 21:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
تانکر ترکرز: صادرات نفت ایران به ۵۰ میلیون بشکه رسید
مؤسسه «تانکر ترکرز»:
🔹
ایران از زمان رفع تحریم‌های آمریکا طی دو هفته گذشته، ۵۰ میلیون بشکه نفت خام صادر کرده؛ رقمی معادل روزانه ۱.۶۶ میلیون بشکه.
🔹
این در حالی است که بسیاری از کشورهای منطقه هنوز به سطح صادرات پیش از جنگ بازنگشته‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/665040" target="_blank">📅 21:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3SBJBD8rasvWSIwoO-P8dbtmHVweGI4dLSYEtrabKC3lyPL054KO0C0CrmT93Ngwl_JeppODspUhFqRQmz8_Omr4Mnye3jUyVtchEACxb-q8nf4AxDg2iQCaS2pgNPO4LJe19GZ3CNeZpmY3D4ePDpTe-oZ454EmeMw57ako5dr2zD9zG9TaysaADAzI0GTwL19zNjqHfOPhwm226x9z4n8OclVZnBLYoE5ibZYvzOpEj5uVokiEO-r1WWBRfzwSc_C2XmeQ9zVl3VYs7sS47bsxj2ZIptRVh9TGQCghkqu0LMNeh8J5HNcaTgnHDXuYMuiOAT_Ek-gwToiUNBfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی برق می‌رود، زندگی از جریان می‌ایستد
🔹
قطعی برق فقط خاموش شدن چراغ‌ها نیست؛ از اختلال در کسب‌وکار، آموزش، خدمات و ارتباطات گرفته تا مشکلات برای بیماران، سالمندان و خانواده‌ها است. #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/665039" target="_blank">📅 21:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665038">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b96a0955.mp4?token=d5jSDunaADwwoUJNGTdtBdqOBsPSw5z4rgK4TouPMVYoEHp5PBuZQSopLpL0lTztcvokfrnsBCYz-kMemrl8p-N8aECVFCo5lg9vqIErWWbgQepUsxI17wYMn6PvGDTA0G0KgDQZt64jAdbbCpZyNnGsCpgiTopsCc-eLog-RvUh-uYtARiSOaCLFX4PL7kG0lCysQmPDRW6OAH6QtGADdYwlP8gNmRYvqfDApJ_YcMxsowecVw_sVwqU0M8bQZKLlOIBN7cul81O6eGVXLMvdIp2Ri7EHF-qZ01yJRZR2QOXYQKrjIjKQRCxtQUnVJniVXFKIXLfPZHE-rrbtXxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b96a0955.mp4?token=d5jSDunaADwwoUJNGTdtBdqOBsPSw5z4rgK4TouPMVYoEHp5PBuZQSopLpL0lTztcvokfrnsBCYz-kMemrl8p-N8aECVFCo5lg9vqIErWWbgQepUsxI17wYMn6PvGDTA0G0KgDQZt64jAdbbCpZyNnGsCpgiTopsCc-eLog-RvUh-uYtARiSOaCLFX4PL7kG0lCysQmPDRW6OAH6QtGADdYwlP8gNmRYvqfDApJ_YcMxsowecVw_sVwqU0M8bQZKLlOIBN7cul81O6eGVXLMvdIp2Ri7EHF-qZ01yJRZR2QOXYQKrjIjKQRCxtQUnVJniVXFKIXLfPZHE-rrbtXxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همزمان با افزایش شمار قربانیان زلزله در ونزوئلا، تابوت‌ها یکی پس از دیگری به لاگوایرا می‌رسند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/665038" target="_blank">📅 20:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665037">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e2e722a.mp4?token=YBWtdJtGvR8HxaMVuRZtmofpM20JFn7fIrUOCVInRgdkRf0PsLz912zf2DjtlZm1zCiQbsdu-_y1vIqFnVZdRL7ZJMkJ_fEHKJvak-0e37c_-1vVc5dtMtWzJPWASkgSV3S3hcYwcqpMTRC0qmWF_QRpDc7aPAWtvgqk9lHoJ0k2WulGpooRGmvovufQ1reRc5XHb8768kr8oQqOO5dqC0bWEOIZgISWk8Z2dk-J8zY42f64mpkXJhK_XH49GQpOUHOxsjg8xcxwmdEyJ14Iz7bwin7TNEFGxC37amMr1VtPiuzHcQ3CALKgHimxM-47_09RujtTjnRU2prchB06dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e2e722a.mp4?token=YBWtdJtGvR8HxaMVuRZtmofpM20JFn7fIrUOCVInRgdkRf0PsLz912zf2DjtlZm1zCiQbsdu-_y1vIqFnVZdRL7ZJMkJ_fEHKJvak-0e37c_-1vVc5dtMtWzJPWASkgSV3S3hcYwcqpMTRC0qmWF_QRpDc7aPAWtvgqk9lHoJ0k2WulGpooRGmvovufQ1reRc5XHb8768kr8oQqOO5dqC0bWEOIZgISWk8Z2dk-J8zY42f64mpkXJhK_XH49GQpOUHOxsjg8xcxwmdEyJ14Iz7bwin7TNEFGxC37amMr1VtPiuzHcQ3CALKgHimxM-47_09RujtTjnRU2prchB06dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌‌ای از منطقه مجدل زون در جنوب لبنان که توسط رژیم صهیونسیتی نابود شده‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/665037" target="_blank">📅 20:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315cce5c2a.mp4?token=fwNI28Wps6_sFLJ5drC32B3NplibUJ8dC2GeUiTFmxnuetES0Vb2tpkfUfaT8MX1NNDuzwpPZY3fmVmxfr9ETCsVoCWWPSK5XI-z5RVHIzGgu_ntc5_05zog7yquQnkDJnZ6QHgNG9MIer4xvLYcqehavNCwXDCAeDGTrkum5EI2ithOZIUcCFgDD4PWuu7qkLC3IqWOuC_JEV2-FoRKOXgi4B9p30jQZpPGQDmiIwqNF4BtngVhcUCh-Iu3O5iDtUjhj1HCK8AMa-i1aL4uDntLBGIRALv2Hbz2j9n76p5V_UoYOgXE038eYgPB3XYlLdLksBcpWwr1_W-MGEvyaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315cce5c2a.mp4?token=fwNI28Wps6_sFLJ5drC32B3NplibUJ8dC2GeUiTFmxnuetES0Vb2tpkfUfaT8MX1NNDuzwpPZY3fmVmxfr9ETCsVoCWWPSK5XI-z5RVHIzGgu_ntc5_05zog7yquQnkDJnZ6QHgNG9MIer4xvLYcqehavNCwXDCAeDGTrkum5EI2ithOZIUcCFgDD4PWuu7qkLC3IqWOuC_JEV2-FoRKOXgi4B9p30jQZpPGQDmiIwqNF4BtngVhcUCh-Iu3O5iDtUjhj1HCK8AMa-i1aL4uDntLBGIRALv2Hbz2j9n76p5V_UoYOgXE038eYgPB3XYlLdLksBcpWwr1_W-MGEvyaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور غیرمنتظره لیونل مسی در تیزر تبلیغاتی فصل جدید «مرد عنکبوتی»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/665036" target="_blank">📅 20:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک ایران عزاست...
🔹
از هر کوچه و هر نگاه، یک بغض برخاسته است... همه آمده‌اند تا با اشک، بدرقه‌ای عاشقانه را برای رهبرِ شهیدشان به جا آورند
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/665035" target="_blank">📅 20:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
هزینه جنگ با ایران برای هر آمریکایی ۱۰۰۰ دلار فاکتور شد
سی‌بی‌اس‌نیوز:
🔹
افزایش قیمت بنزین (۳۰۰ دلار)، رشد هزینه مواد غذایی (۲۰۰ دلار)، هزینه‌های نظامی (۲۵۰ دلار)، افزایش نرخ بهره و هزینه‌های استقراض (۱۵۰ دلار) و گرانی بلیت هواپیما (۱۰۰ دلار) مهم‌ترین عوامل این افزایش هستند.
🔹
همچنین برآورد دانشگاه براون نشان می‌دهد هزینه بنزین و گازوئیل به‌تنهایی ۴۸۶ دلار به ازای هر خانوار افزایش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/665034" target="_blank">📅 20:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f2110fe3.mp4?token=u4hwu4quFlG7BcT3VLdRhL1JoJYi4kzHWbSnEOGafGD6uJFQXwiVtyi29JoBEMASiGAEYw18YuCwq-TFPdZXy5lQsBot2M3yvztpoi7BAhXSoj4AdtFDkml0Kus6jsBT2DHPNLak4k8EoaWGBsnxETWQtwmYWjjOx402MYMCeV6BtxwUiRsBD-P4Hqc60sAgb3re86_R1IK9ch2n3VQ_m4UG2ZweXExDtpLWr0ACfhGOzfXaKkhBTezENc8juqCRGzxa-uJKcHps0rgDs9WYAU0n0BFc48ToAhLQXdkfzpFXgKvBudfxGkjdbKyEjeNps3Rt-uIkFcyZcatT5UKSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f2110fe3.mp4?token=u4hwu4quFlG7BcT3VLdRhL1JoJYi4kzHWbSnEOGafGD6uJFQXwiVtyi29JoBEMASiGAEYw18YuCwq-TFPdZXy5lQsBot2M3yvztpoi7BAhXSoj4AdtFDkml0Kus6jsBT2DHPNLak4k8EoaWGBsnxETWQtwmYWjjOx402MYMCeV6BtxwUiRsBD-P4Hqc60sAgb3re86_R1IK9ch2n3VQ_m4UG2ZweXExDtpLWr0ACfhGOzfXaKkhBTezENc8juqCRGzxa-uJKcHps0rgDs9WYAU0n0BFc48ToAhLQXdkfzpFXgKvBudfxGkjdbKyEjeNps3Rt-uIkFcyZcatT5UKSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت برفی ‌ارتفاعات سبلان، اردبیل
🇮🇷
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665033" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffouYGivSVKyA-IbHUYMYbTwUtcJIVg3Adu8TwNU20n7Tm7bNhFh_bZ3GtXFCd3kvmj2y2f7nKftNRM9Tj_Sq_1GO1IgQekEr0NmSJY4D9lunJb1MRRXzrkEcc9S5LH93JxFLkNK51ctbtk1Rg4JomCptfqImS2pdLVKJC-xJ3Em_U9qEfoucCRdIqfiWxskyHO4Mw1oqeJS4s8NZKEMrDq9LtKfinM7L4dYcNUPszfpOO8iuR5zlsgnkj171-IlLzHHz8ns3jQJ3K3R8RCM6o8XCs-sWFo3xRgVrROD7paAMN3OO-wBHejK9amxuEmYfN6eDYy7AmuW4z5d06frfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا به دنبال الگوی مک‌دونالد برای ساخت موشک است | پشت پرده کارخانه مخفی موشک‌های ارزان آمریکا
🔹
ساختمانی کوتاه و ساده در شمال شرقی ایالت ویرجینیا، در نگاه اول هیچ نشانی از یک مرکز راهبردی نظامی ندارد؛ اما درون آن، ردیف‌هایی از موشک‌ها روی میزهای کار قرار گرفته‌اند تا تکنسین‌های جوان آن‌ها را برای جنگ احتمالی بعدی آمریکا آماده کنند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3226643</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/665032" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665030">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پیام‌های متعدد مردم به برنامه شهروند مدار: چرا مسئولین ترمز گرانی محصولات بی‌کیفیت ایران‌خودرو را نمی‌کشند؟/
مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665030" target="_blank">📅 20:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‌
♦️
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665029" target="_blank">📅 20:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
توقف تردد در تنگه هرمز؛ انتظار IMO برای مجوز ایران
🔹
سازمان بین‌المللی دریانوردی (IMO) در پی حمله اخیر به یک نفت‌کش، عملیات خروج کشتی‌ها از تنگه هرمز را متوقف کرد و ازسرگیری تردد را منوط به تصمیم رسمی ایران دانست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665028" target="_blank">📅 20:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e871f5e508.mp4?token=QpP4tct_YeRN_iZFFcWjv8kOfjkTFz9NZFPmYHOkgjvUW72PvBP4VfbcNz2QyHgK0NOc9u8t_DSnq7BoePzqFWzKolKI52vlzzJWb1KDsGo81gxV2zuuNvDtPEqHruOFmK5gfCwCljPyWC4uW-Ut10vbcz3pDq3l5OS9abnGWFRIomcZtCF1OrKUknKndExs0k27GrlgljVh2S2Drngdpf75h9m52wZ8ni1K7e4MtQJjJX5sfXU_tTlmEKs8_8eAg0K_RxSls0EWpVSZyhc9q0PjcbeTP97CFif8IG4fyM2NesTn2pdDFeJPaaFdDcIPcDEN3kDUElu-2BWt0a1Nhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e871f5e508.mp4?token=QpP4tct_YeRN_iZFFcWjv8kOfjkTFz9NZFPmYHOkgjvUW72PvBP4VfbcNz2QyHgK0NOc9u8t_DSnq7BoePzqFWzKolKI52vlzzJWb1KDsGo81gxV2zuuNvDtPEqHruOFmK5gfCwCljPyWC4uW-Ut10vbcz3pDq3l5OS9abnGWFRIomcZtCF1OrKUknKndExs0k27GrlgljVh2S2Drngdpf75h9m52wZ8ni1K7e4MtQJjJX5sfXU_tTlmEKs8_8eAg0K_RxSls0EWpVSZyhc9q0PjcbeTP97CFif8IG4fyM2NesTn2pdDFeJPaaFdDcIPcDEN3kDUElu-2BWt0a1Nhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین روند آماده سازی مصلی تهران برای تشییع باشکوه رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/665027" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665025">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETVnm0g1lHMgO7GWl63Odd6IgyyQmCGf8yR4NdBNhycwobZtR60u_1Df9z58b4Af6E7iaHgI501bQXMAn9mKfsE-hzXBZbU-6WWWj3GsHZmxiaP4x2RoPGMGH4WfRU57K1GASDiD5imFaYmlgHJ1Uyrf-KBNQnwJwjurnjhGj8b13rTdjJDr0mhkAAskK1e32Yi9QEIIP0LN4obLoZYZfkKa1Hez3IPiYOn0giO8YRKw9F-N0ynE08O9Gsw_B9uDv8HfhFZn_KaIRVWAfewv3Bql4Z1q6zDHW05DYa7YsgN7suhTWbr9HtzGde-ES_8MfEaw8sQQnwLcCenpSkfIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxXSfU1FjLeTHb8bz1SBjiB5zBm_izZxwybX6gVhUQ6oAMLr3xBMV6rW5DtSBcA3UcMuhfXpU7GerrgaWCiF4yaHjCDQSdWwuQgHkT9Ef4k4A6FFRCUU7dmGhdgH3hzc_IG6li1Q3KOFirVNk2XLYDhbmEbiPwPx18aPaU8CHExwCfUK7wVFxGJAybDZKTVJk3vofUXs9NbBIeqLnJyRySPEEryT8OxafaWusWBws8GyJjPnSgxA_r2cXXarLAAbWIwPC_Pl14cP-A8EeqMuf6JB5ZdfXBEzCCfJwpzowff88jTcAJhwt6HorKFq33ux9_kx7_mVTg0MD5P-ZSP8ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آیا دموکراسی از ثروت مهم‌تر است؟ این کتاب پاسخ می‌دهد
🔹
اگر فکر می‌کنید نفت، موقعیت جغرافیایی یا فرهنگ، سرنوشت کشورها را تعیین می‌کند، این کتاب شما را غافلگیر خواهد کرد. «چرا ملت‌ها شکست می‌خورند» با مثال‌هایی از سراسر جهان، پاسخی جسورانه می‌دهد: تفاوت را نه جغرافیا، بلکه کیفیت نهادها و حکمرانی رقم می‌زند.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/665025" target="_blank">📅 20:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665024">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
هشدار چین: آتش‌بس بین ایران و آمریکا شکننده است
شینهوا:
🔹
وانگ یی، وزیر خارجه چین در دیدار با شاهزاده فیصل بن فرحان، وزیر خارجه عربستان گفت که آتش‌بس بین ایران و آمریکا همچنان شکننده است.
🔹
او افزود صحبت کردن بهتر از جنگیدن است و گفتگو بهتر از رویارویی است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/665024" target="_blank">📅 20:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
اعزام هیئت کارشناسی ایران به دوحه برای پیگیری تفاهم‌نامه
🔹
سخنگوی وزارت خارجه از اعزام هیئت کارشناسی ایران به سرپرستی «غریب‌آبادی» به قطر خبر داد؛ این سفر با هدف پیگیری اجرای تفاهم‌نامه و مذاکره با طرف قطری انجام شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/665023" target="_blank">📅 20:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اعزام هیئت کارشناسی ایران به دوحه برای پیگیری تفاهم‌نامه
🔹
سخنگوی وزارت خارجه از اعزام هیئت کارشناسی ایران به سرپرستی «غریب‌آبادی» به قطر خبر داد؛ این سفر با هدف پیگیری اجرای تفاهم‌نامه و مذاکره با طرف قطری انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/665022" target="_blank">📅 20:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxv4zluwz71pnQrFts7XlrtjH97fLvABvFT-XueZdp0KyXzMnJRnlitZxT9Yym2ZJwg-wPpI00KnIGFbaj4pzAMDSCT4G1YmWbsF60YPhtyQLXXFSZeTPEpqPjMrJit3e50T8F1fnc61whZ_dXPhDTXhM61WzPfMpW9gUX0FhrosLB4khFBlR_zyV8BgGWvNoTlJtJH7iXJJhM5gsQHq_XVS-trGFXvyY9-kOjDt7ZJY4GpPLBtxQwhuClExsda0XPya_MGreOy7fLT6lXpBBGeUTirihrzmWmE20H5wV-pU21XR3UFd8qP1orIve0NfgsfyvP-Ej5fWK8vs4zSjdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ این سؤال را مردم می‌خواهند...
🔹
قطعی برق در نقاط مختلف کشور، این سؤال را برای بسیاری از شهروندان ایجاد کرده است: #برق_مردم_کجاست؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/665021" target="_blank">📅 20:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5804af890a.mp4?token=mfgKRAbgimeZmDbl5aRHCU6yzyusWtMEkKJKvb-db__k7OYYLCBPC1ty3xTafnvsLSLa-5YISDmj0gS-vKGKtizKK22hhxz3pi2Sgsd9XBEWLTLPTI56dqMCX59k6-D5fH5vPpGeAMNpLuI8YtQx7oioUMTq_fiIfC6SRNM-rPbSvoHb4Cw-k7lC9n2ESWi-rMOpXeS3EEVU4SDE-uLkegLivtRZLo_BnZnVbCFvzJJAVJ0rDsrlCh2r8HWTQgddzSudehM3ysXmhk7nsIFE4MYLRf4Y7a283hPMTQXcI0qLo4pHGKS6Ez1meLSiqJvgpte2zRd3uSQX1RXg4AG4Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5804af890a.mp4?token=mfgKRAbgimeZmDbl5aRHCU6yzyusWtMEkKJKvb-db__k7OYYLCBPC1ty3xTafnvsLSLa-5YISDmj0gS-vKGKtizKK22hhxz3pi2Sgsd9XBEWLTLPTI56dqMCX59k6-D5fH5vPpGeAMNpLuI8YtQx7oioUMTq_fiIfC6SRNM-rPbSvoHb4Cw-k7lC9n2ESWi-rMOpXeS3EEVU4SDE-uLkegLivtRZLo_BnZnVbCFvzJJAVJ0rDsrlCh2r8HWTQgddzSudehM3ysXmhk7nsIFE4MYLRf4Y7a283hPMTQXcI0qLo4pHGKS6Ez1meLSiqJvgpte2zRd3uSQX1RXg4AG4Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کرم کله‌مرده؛ قاتل زنبورها و آفت سیب‌زمینی
🔹
این حشره (African death’s head hawkmoth) در دو مرحله زیستی مخرب است؛ لاروهای آن آفت سیب‌زمینی محسوب می‌شوند و پروانه‌های بالغ با نفوذ به کندوها، دشمن خطرناک زنبورهای عسل هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/665020" target="_blank">📅 19:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b730f0bc.mp4?token=WzMEQD5Dv6ej57euhAnzWchDwBYrBTFH6Wk33Waw5XS9mvkAI4NV5PPEw5sm9uh8DE1DEA2-47ShAlBvpr9SK_sJ44S_S3WjZW9nkzYGyQL9rmOhRMAcQry7XnamkVLIeq-g19mF-75WAmHbQbRoOlNZRHcJXo_i0uE6rLqc2xEMXSKo32WBKbJ88-ecYE8_Ai7RgVJi8S3xbF8Ty_H2BUU57sAuuFsGbBL7TO9WL8imXYo6s-q7KtQ2ajq3MLTQC8R-mP3C6PBwWI8KipYHx_2-FG298nHD1JwD459B-ek3g-vN7ZdtmHb7jYCgHgZXcDiaST_2bJTFAw_GqCAmwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b730f0bc.mp4?token=WzMEQD5Dv6ej57euhAnzWchDwBYrBTFH6Wk33Waw5XS9mvkAI4NV5PPEw5sm9uh8DE1DEA2-47ShAlBvpr9SK_sJ44S_S3WjZW9nkzYGyQL9rmOhRMAcQry7XnamkVLIeq-g19mF-75WAmHbQbRoOlNZRHcJXo_i0uE6rLqc2xEMXSKo32WBKbJ88-ecYE8_Ai7RgVJi8S3xbF8Ty_H2BUU57sAuuFsGbBL7TO9WL8imXYo6s-q7KtQ2ajq3MLTQC8R-mP3C6PBwWI8KipYHx_2-FG298nHD1JwD459B-ek3g-vN7ZdtmHb7jYCgHgZXcDiaST_2bJTFAw_GqCAmwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میانجی مرموز بین ایران و آمریکا؛ علی ذوادی کیست؟
🔹
اسمش را شاید هرگز نشنیده باشید؛ نه مصاحبه‌ای، نه صفحه‌ای در شبکه‌های اجتماعی و نه حتی تصویری پررنگ در رسانه‌ها. اما گفته می‌شود یکی از حساس‌ترین مذاکرات ایران و آمریکا، با رفت‌وآمدهای او پیش رفته است.
🔹
مردی که گفته می‌شود در ۱۰ روز، چهار بار به تهران سفر کرد، ۱۷ ساعت پای میز مذاکره نشست و حتی نامش از زبان ترامپ شنیده شد. علی ذوادی کیست و چرا همه او را «میانجی مرموز» می‌نامند؟
در این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/665019" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25bb3b338.mp4?token=tOpAk17CpcHA5q8ak5fJP3oKSISmFCuYalWEkMQd5oY4omnejCjURKdWGlukBxbAebPRUHw2MnhQjGGP95rKtR65Ct9eQcKXQWp4uS3EpsU55bINwIMHx6nWOIPmFZwSXx126QrEce_YXwu7g-E3C8XB5yUhAHWqVAiTtSDbhh9t81V-fIKmy-oIm0jLq5R4pUrZqOlTv1ZYHksDkIZpA2KGXjtiT5R_IhXvfEFBJpwyjNECIvjQKzxUUYxK4KIXkbLeRmbD2WiHNhIlbVXVERa1Bcsg63g9-svX0NV7ilCG_tC2pghRSSryW3a9xzxdr6kubG23mIaKcR9zXZ3qTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25bb3b338.mp4?token=tOpAk17CpcHA5q8ak5fJP3oKSISmFCuYalWEkMQd5oY4omnejCjURKdWGlukBxbAebPRUHw2MnhQjGGP95rKtR65Ct9eQcKXQWp4uS3EpsU55bINwIMHx6nWOIPmFZwSXx126QrEce_YXwu7g-E3C8XB5yUhAHWqVAiTtSDbhh9t81V-fIKmy-oIm0jLq5R4pUrZqOlTv1ZYHksDkIZpA2KGXjtiT5R_IhXvfEFBJpwyjNECIvjQKzxUUYxK4KIXkbLeRmbD2WiHNhIlbVXVERa1Bcsg63g9-svX0NV7ilCG_tC2pghRSSryW3a9xzxdr6kubG23mIaKcR9zXZ3qTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری
از
آماده‌سازی‌ها برای مراسم تشییع رهبری؛ اینجا همه‌چیز مهیای آغاز یک مراسم تاریخی است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665012" target="_blank">📅 19:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ریزش سنگین مخاطبان رضا پهلوی؛ ۶۰۰ هزار آنفالو و سقوط ۷۳ درصدی لایک‌ها
🔹
صفحه اینستاگرام رضا پهلوی طی بیش از ۱۰۰ روز گذشته با ریزش قابل‌ توجه مخاطبان روبه‌رو شده، به‌ طوری‌ که حدود ۶۰۰ هزار نفر او را آنفالو کرده‌اند.
🔹
بر اساس داده‌های تحلیل شبکه‌های اجتماعی مجازی، میانگین لایک پست‌های او از حدود ۶۹۷ هزار پیش از آغاز جنگ به ۱۸۹ هزار در روزهای اخیر کاهش یافته که افتی ۷۳ درصدی را نشان می‌دهد.
🔹
هم‌زمان با بازگشایی اینترنت در اوایل خرداد، روند ریزش فالوورها شدت گرفته و بیش از ۱۷۰ هزار نفر در این مقطع صفحه او را ترک کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/665011" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umgOPxkG9UXug7AcirV04uXenP5oBRSCwL7FJ72LM2MWfFq1hovBQ7D-WwC3AucfTyXd2P_CtYYQxeENDQjhtrvDNIhvqasfqV-yPGYWm7WYg0yk1a8ljyxmC6wwl8HIo7EAV0L2Rzczr8yehpLu1p4Dr4MTZfng5DdCjrQyXU5FCKRZ1fLsNFeiFSGzxCZPyhMkPMGtgh_fS-2b7c-4TF2ukUSy5XpL1EMEgLmO9A4Psk8ffghNVk9HeGvOky94mPt-LGRw40lMTmkwMXIzyv3xsJl3ASeLatTbxvp-DwgnfsDL-P56ih0cDupVD3uiH83HpM3wFoRBCj7bogCS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: تشییع رهبر شهیدمان، پایان بغض تاریخی تشییع‌های مظلومانه شیعه است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/665010" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای نتانیاهو کودک‌کش: ما جنوب لبنان را ترک نخواهیم کرد تا زمانی که خطر برطرف شود؛ تا زمانی که حزب الله مسلح وجود داشته باشد و ما را تهدید کند، ما اینجا خواهیم ماند
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665009" target="_blank">📅 19:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfZM7eepI96QcF9igOa8W4U2y41PyzG8PjvYbOSV3XBayCkz6MvRa1NwqoWqCYuhJTypGS4Jgm-Q81LrflUfwxhX05qEOuQQFMCkJwoI_z3m7CPichHAe512tUUAxS1634GcOvvN92TNmO2VnVSaMNL7Xniavkd8cKtVQoDCjrLmTP6KP9Re5rboW7ENFZcB1V2MOZfuNjNqmYdjsaLHG7Y7yhbvE2Rh7wGJUPbEscCQtlcpCFDngfEwMve51IX8npUh1nr02BHcemGJ4OkhlpWpaI0iCd7Cq59tc3j6fRcdK8U9RaSMAmZrwn1ev7oXIrCyeoPqM1h1v3dBDCVl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دشت شقایق دماوند
🇮🇷
#ایران_زیبا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/665008" target="_blank">📅 19:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665007">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe298db09.mp4?token=gIcrgtlBhguwddb0l1QcSOwzwOVp5-3Us0ZcQXfis16xGJsyoPdh7avmYe26kpjR0mc8KZJXH0MDqrx2yvlzcrLbyaP3vV1WICO8zndUTrMDVnW6xy6v-ZRT7sjZcARUpEKycEGRQpV8oeTy1sw3FYokZHBdAA1glOBgdrYoVCa4LJfkoFPobckxJ5M69jzxXAoQDcsckryJTkO8KGBCo54YIQLvt3AXE7TABH9TPjRugGHUX3XvUe0KYOtD20j3BRdXnmiDhUeHc8O-jf1OuNnxTBYMOMJRpBEemN7QqHENijK3c6E71B9ILjHT_urmn4PLHLyfCVMguana-MNH8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe298db09.mp4?token=gIcrgtlBhguwddb0l1QcSOwzwOVp5-3Us0ZcQXfis16xGJsyoPdh7avmYe26kpjR0mc8KZJXH0MDqrx2yvlzcrLbyaP3vV1WICO8zndUTrMDVnW6xy6v-ZRT7sjZcARUpEKycEGRQpV8oeTy1sw3FYokZHBdAA1glOBgdrYoVCa4LJfkoFPobckxJ5M69jzxXAoQDcsckryJTkO8KGBCo54YIQLvt3AXE7TABH9TPjRugGHUX3XvUe0KYOtD20j3BRdXnmiDhUeHc8O-jf1OuNnxTBYMOMJRpBEemN7QqHENijK3c6E71B9ILjHT_urmn4PLHLyfCVMguana-MNH8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما درباره جنگ ایران: وضعیت پس از میلیاردها دلار هزینه جنگ، بدتر شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/665007" target="_blank">📅 19:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665006">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
نتانیاهوی خبیث، دقایقی پیش، از عون و سلام، چاکران درگاه ترامپ در بیروت، اینطور تشکر کرد: از دولت لبنان بابت شجاعتی که نشان داد، تشکر می‌کنم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/665006" target="_blank">📅 19:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتانیاهو: مهم‌ترین کاری که در لبنان انجام دادیم، ایجاد یک منطقه حائل است.
🔹
سازمان همکاری اسلامی خواستار توقف حملات اسرائیل به سوریه شد.
🔹
امارات ممنوعیت سفر شهروندانش به لبنان را لغو کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/665005" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e683e35d7d.mp4?token=JsogNc4M-cmz4Hx80OKrPdzCORH6iLSsDVrUXTXyFtnHI3jI4BGFQSjH6GDZaVAhXWkM9wkaJlkuFKrDVT7SDcTC9V0V_-nzNyKFvp3diD5TBNB_Z64qLw30lvJqwMVb42VL_QoQCQ4NXnkrc82qaI1OXKdR9jom-COTHpnTNHgeQCuPwgoBN8hQhtR1MhFS1pWeN2AMgW7j4-MmlKCYlB3nwmOnWi5fZqP9JU2yztR4onmhp9rsQsEdgc0SWRrHNbbh_SsoSwcGwibYR8Vji0I8sG0n4BavQTwk6-_7mjKAG7PrDySwtFbertq7xEiP9dE4v28ZcZvvezi2b0IAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e683e35d7d.mp4?token=JsogNc4M-cmz4Hx80OKrPdzCORH6iLSsDVrUXTXyFtnHI3jI4BGFQSjH6GDZaVAhXWkM9wkaJlkuFKrDVT7SDcTC9V0V_-nzNyKFvp3diD5TBNB_Z64qLw30lvJqwMVb42VL_QoQCQ4NXnkrc82qaI1OXKdR9jom-COTHpnTNHgeQCuPwgoBN8hQhtR1MhFS1pWeN2AMgW7j4-MmlKCYlB3nwmOnWi5fZqP9JU2yztR4onmhp9rsQsEdgc0SWRrHNbbh_SsoSwcGwibYR8Vji0I8sG0n4BavQTwk6-_7mjKAG7PrDySwtFbertq7xEiP9dE4v28ZcZvvezi2b0IAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کتک زدن شهروندان مغرب از سوی پلیس هلند
🔹
پلیس هلند در حال کتک زدن و دستگیری شهروندان مغرب است که بعد از پیروزی بر تیم ملی فوتبال هلند به خیابان‌ها آمدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/665004" target="_blank">📅 19:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665003">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usTrg0NBVf51NGauuTGPA6Ue01EMa5n3czv9IGWoGgzJZ-8QCjRcGoE89FXDD2qq1b4vKwiufpl1U_hhYjuNzMvubBIlEy6zEqqUWn8NsoBTPruNChi2bAiNwSnyYwrUAdWHwW5_gzyBmD-U1t1AR-_68yzB8LZMC27r6rtI0pR4Dcr93g1sszgLuffpYYlX5d3DJT--I0Gaes4hYfVK4P9bKY8a4zIZEerQskNKA7-nkne9xmAHQArkoQltvb25DjF2j40iWE4d9dyJhGQrbIdtXURgTIuSPJTjyJfkBaQbV_cFJfOCzh70dDbNM58MUhfdTin37HcNdP3vso6-qg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665003" target="_blank">📅 19:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وزارت خزانه‌داری آمریکا: مؤسسات مالی وابسته به حزب‌الله، از جمله بنیاد قرض‌الحسنه و مقامات ارشد آن، به فهرست تروریسم اضافه شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/665002" target="_blank">📅 18:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اقتصاد ایران وارد فاز رکود تورمی شد
🔹
جدیدترین آمارهای اقتصادی نشان می‌دهد اقتصاد ایران در زمستان ۱۴۰۴ با وقوع جنگ وارد فاز رکودی شده است.
🔹
رشد اقتصادی با نفت و بدون نفت با ثبت رشد منفی ۲.۲ درصد، وارد فاز رکودی شد. همزمان، تداوم رشد نقدینگی و پایه پولی، سیگنال‌های تورمی را تقویت کرده و از تشدید رکود تورمی حکایت دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/665001" target="_blank">📅 18:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ابطال
فرمان اجرایی ترامپ از سوی دیوان عالی آمریکا
آسوشیتدپرس:
🔹
دیوان عالی آمریکا بار دیگر تأیید کرد که هر کسی در خاک آمریکا متولد شود، شهروند این کشور محسوب می‌شود.
🔹
به این ترتیب، فرمان اجرایی دونالد ترامپ که می‌گفت فرزندان افرادی که به‌طور غیرقانونی یا موقت در آمریکا به سر می‌برند، شهروندی دریافت نمی‌کنند، باطل اعلام شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/665000" target="_blank">📅 18:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=BGcQqM53CskJ5h9awjnWhcehu-8031v-ikKlrIkr6mk0Kcs6luRK2Tc59HfAkeKcjuL0iR3zXT5PH13CTR9eh6MqIt4_RVkSK3R-LDsqO355FOqtbIl220o_TSASU5AechaSqBfUgN6OHZYkQTnB5F3V2aEpwJ070L5z0txC4etivvxTL7Y0AP3UWUb6hvZhSbC7ZXWSDA1VR4LlH2AEcqR3qUCQwd4ge_Ca-ISOOnSZ1v9TyFDoFuFJAvYaxzlLtNHuxkoTRyiKJD49kHgVEb6uQajuLN6FqgLJsyshzIz92A3rztJEHG9oVUIUvUIFSCNl2g_442tYvsRd1O_QRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6721e5386c.mp4?token=BGcQqM53CskJ5h9awjnWhcehu-8031v-ikKlrIkr6mk0Kcs6luRK2Tc59HfAkeKcjuL0iR3zXT5PH13CTR9eh6MqIt4_RVkSK3R-LDsqO355FOqtbIl220o_TSASU5AechaSqBfUgN6OHZYkQTnB5F3V2aEpwJ070L5z0txC4etivvxTL7Y0AP3UWUb6hvZhSbC7ZXWSDA1VR4LlH2AEcqR3qUCQwd4ge_Ca-ISOOnSZ1v9TyFDoFuFJAvYaxzlLtNHuxkoTRyiKJD49kHgVEb6uQajuLN6FqgLJsyshzIz92A3rztJEHG9oVUIUvUIFSCNl2g_442tYvsRd1O_QRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار حوزۀ مقاومت: مسافتی ۳ برابر غزه در لبنان اشغال و غیرقابل سکونت شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/664999" target="_blank">📅 18:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664998">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjgrE0yVQGLWb1i0S5SEMnh4UjAasaVHPFbLN9Mf2gGtAI6dwQg4jrBV1satsd-2GMFXtoKAftqIavMNJHBNN0L3HcgPEOzvguDIU2jLk6BQiM0pBftHBUfMDYinkxy_WRY5jo9vYtwqvp5QLgOBdXPjjXff7V6j8KKlSmvr9y0LYQdu9TerMuKeyLk0tL_VlL0GuzZykiqWRSL-czGPO0DEcDI6RR5uz1dEHb4QBztCGTHFFewq5-SbKE6l-qpjqa16k46z_3-22Me7e5jaiBnP42AW4xs9WTEAUPpAXc-3sXf2J89-KGIwL_NQoVS89B8WfrOPz2fH0gd6faf5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
▪️
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/664998" target="_blank">📅 18:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664997">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh_SfnzcM3-T_V4jbaYq1WLWK5pV9SCnSkg-U1MlNf5kbB76NzaQ8iu7ZO17EzxVWOadXfRXuxTRlhRSLejNBeK47cfAfiPV8DLlKrWYJSiQ889J8F7EPQ902yiEP2Xc7OefiPwZ5Zms5YCgdjEbCi3kNm0Z4jYxtF6avXQhtZOflHNbDdq-MDubpxAlXp-XFcomJpTbABSAUc6YQ18_QeX8faqj2m4ck7TZqWb7EFlDd-BoDVxNmNyOtrkeSC_-ym6GQHRynSvjVDagCctW5ssHAfxZYnBQw6SVALYIKX-yJIlFS2y-cmbKe4SA_laBAjL2fxq2gOh4JUQLsuNHzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز حساب، فراموش نمی‌شود
🔹
ورق‌های تاریخ دیر یا زود ورق می‌خورند و هیچ تصمیمی بدون قضاوت زمان باقی نمی‌ماند. مطالبه مردم عدالت است.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/664997" target="_blank">📅 18:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664996">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu5IirX9BdLhJ4LMHlEoTuP1dI6YTmv-7tYtTymW-Y4X5wKgNUFtfxcqUez06S6OEKlha9yPAx7y1XLOQWozvij8kChu4XshlSAaw1ICpep8PGYd2ZvM8V9q_g6f6crvmFIDFSKPzAwsj6484RD-2kad4Ws4Mr9Rz6_jy14SuHbeSo_mcG2PPD04-Qz68QIj3H0_Cntd9go3FDP28pfz1iE3OUdpLjg6MCkpVWZI_9iCsZ9pPOLlNe03s2_ZlwzHdBEbDrKsNVU6q1Aznl4Ic2EErLi8fJGRzi7dlZ_uR6ocE8ZA9t3cHDCXTFcb7-E2og5GbkPrctCC2CZBZIVDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی آمریکا به یک هواپیمای مسافربری شلیک کرد
🔹
۱۲ تیر ۱۳۶۷، پرواز مسافربری ۶۵۵ ایران‌ایر که در مسیر عادی بندرعباس به دبی در حال پرواز بود، بر فراز خلیج فارس با شلیک دو موشک از ناو آمریکایی «یواس‌اس وینسنس» سرنگون شد. در این حادثه، هر ۲۹۰ سرنشین هواپیما، از جمله ۶۶ کودک، جان خود را از دست دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/664996" target="_blank">📅 18:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664995">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFZH2DGzRF2sehSMpCIXpjwkXV_8ULyYjuDwa1I5YifLSi2n-RfODwUtUNI-rD1L-L37WNn2MLptRiB02fDtUaYBcDg6R75U0VNXEcky0TdcTtlxkmnsthPTydRe6qYhnCIPkxY4E-h-dXN8eHueE1r_VcZveCjqpkXneRuTOjXacRBVfCQef4-sQ07LMVi-BEIXlC0bx8RFCuCgG0CZYr-qDMoc8wPggQDBuyf_2Cul8BoXMt06s7MTo0fD4eTIbuZEqQFXi4l9u2UmINVO3m1oC0tfFcObMz9Vnkqpn36DV2AJBJ-OFNLJ8e4f_bvJg4VT7qbm5eiDZtr7bkvjtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">٪۴۳ ترجیح می‌دهند در برابر بی‌عدالتی اداری سکوت کنند
🔸
در این نظرسنجی بیش از ۲۵ هزار نفر شرکت کردند که سهم روبیکا ۵۷، بله حدود ۲۹ و تلگرام ۱۴ درصد بوده است.
🔸
بیش از ۴۳ درصد از شرکت‌کنندگان گفته‌اند اگر در فرآیندهای اداری احساس کنند حقوقشان رعایت نشده است، ترجیح می‌دهند برای اینکه کارشان دچار مشکل نشود، موضوع را پیگیری نکنند.
🔸
حدود ۲۶ درصد از آن‌ها به دلیل آگاهی از حقوق خود، موضوع را پیگیری می‌کنند و ۱۸ درصد نیز به علت پیچیدگی و سختی روند، تنها تا حدی پیگیر می‌شوند.
@amarfact</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/664995" target="_blank">📅 18:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664994">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9GJe9-qBFvauN6ubD0yi5q69cc3X6xhFSHU15YuqqhjgDBZW8rL4lbzNBNULmDOFX74yfZV1tDbVrVGTzuZ4lrd1MkAzEXtIZ7W2Ojzcxm1MNB58H8WvLY8qTM709wHRrdBrYvlQjwKHLuy6g5JpHgzGGnqsblxPf_b5qPveYlftfGjiolyvdsrxz19orQNvKehYYZAozPOWQW40KvPJ0loVvT9THDCNvnYBliVLzPYDFdj2I556gWdQYBHZ3XCyQKzcAtrBq5kU8fu-xDJZpjDqkk5rGYnz9FoqHOgU8bPZPJrqw1U1jTySq-s3z7zTBCTCbV7WZQUz6-UzNyw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷ میراث مکتوب رهبر شهید
#بدرقه_یار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/664994" target="_blank">📅 18:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e60e87d6.mp4?token=Or1Y5MvwwEbLihxiVv8mC1Ui-9ZS3t3Mo3CyBI6m85xcEV96kqh9_fhXQHwtOpcqvG1RyQxBypT274lzxMaqqJ3h95WKZ21gglB5lTZ1fcQQ1i64eW-lVuP2ZlHqSeeqN54P21MZmyin-RomNhodIKvlYa4Jhj4lWsEFLaZPmKhYVwC6MwqBy3DstvcOeO6RH_zJ1xfKACz4Lz4J7Rdk6oo6x5T4vyw7-pRV3LJG0J28WQ1YziyJVJP52wY1IV-1w9mPTZqAqXMbB6lMKbANV-zgyGLhgona6ocfT3ZteFkpXEfwIByCnXufmGoCANzCJQGbotu9vTTWg2DilwPSdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e60e87d6.mp4?token=Or1Y5MvwwEbLihxiVv8mC1Ui-9ZS3t3Mo3CyBI6m85xcEV96kqh9_fhXQHwtOpcqvG1RyQxBypT274lzxMaqqJ3h95WKZ21gglB5lTZ1fcQQ1i64eW-lVuP2ZlHqSeeqN54P21MZmyin-RomNhodIKvlYa4Jhj4lWsEFLaZPmKhYVwC6MwqBy3DstvcOeO6RH_zJ1xfKACz4Lz4J7Rdk6oo6x5T4vyw7-pRV3LJG0J28WQ1YziyJVJP52wY1IV-1w9mPTZqAqXMbB6lMKbANV-zgyGLhgona6ocfT3ZteFkpXEfwIByCnXufmGoCANzCJQGbotu9vTTWg2DilwPSdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺️
بسیج عمومی ناوگان سوخت‌رسانی برای خدمات‌رسانی در آئین تشییع رهبر شهید انقلاب
محمدصادق عظیمی‌فر، معاون وزیر نفت و مدیرعامل شرکت ملی پالایش و پخش فرآورده‌های نفتی از بسیج عمومی ناوگان سوخت‌رسانی برای خدمات‌رسانی در آئین تشییع رهبر شهید انقلاب خبر داد و تأکید کرد:
🔹
۱۷ هزار ناوگان حمل‌ونقل سوخت و ۶۰ دستگاه سوخت‌رسان سیار آماده سوخت‌رسانی مطلوب به مسافران و میهمانان این مراسم هستند.
🔹
تدارکات لازم برای سوخت‌رسانی پایدار انجام شده و ادامه دارد.
🔹
تواید فرآورده در پالایشگاه‌ها با حداکثر ظرفیت و ذخیره‌سازی در مراکز تجمع جمعیت به میزان کافی انجام شده است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/664993" target="_blank">📅 18:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664992">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcN5A1-ac_S5C3K29ViOFMfIHZGso-sJq3GkBczeux_B8geXRaE1_kHVeaIdoNvE6MGA9fqBi5FW2fvhOO7HP2lz9wTUS8k8uKCZI6V7Mkcmg1aLD5WF44xZUZpDuQ8zI6vFim8JRzdxf7SrjwNMv-zcd5W-OeO_CCHr_WO6NKi0KiNOXSAtedc3-Wt__cl6kA4l7VGq-zucvqkHXnlAG5H42oIe0HaCvv5KER-ajRPxLNMYvePIAmy_-GiFDdkThNqHly5Gs6cuV_I02OTQuYg0Nro-kE86DKOlPSI15TjVwJ9B8_bSxTcWs-krgXVzl7AhvrwsmAFbgcmXplxCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مامان‌وباباها، رقبا شروع کردن و وقت خیلی کمه؛ اگه می‌خوای فرزندتون عقب نمونه و کنکور 1406 رو با رتبه‌ای که آرزوش رو داره و داری تموم کنه، دیگه فرصتی برای تعلل نیست!
🎯
فول پکیج کنکور 1406 کلاسینو
شامل:
🔸
دوره جامع
🔸
دوره آمادگی امتحان نهایی
🔸
آزمون‌های آزمایشی (برای سنجش دقیق سطح و رتبه فرزندتون نسبت به سایر داوطلبان کشور)
🔸
همایش جمع‌بندی
همه‌ اینا فقط با 15 میلیون تومان!
از تابستون 1405 تا روز کنکور 1406، یه لحظه هم فرزندتون رو تنها نمی‌گذاریم.
💳
خبر خوب: کل هزینه به‌صورت اقساطی قابل پرداخته!
همین الان وارد سایت کلاسینو شو و ثبت‌نام فرزندت رو نهایی کن:
wwwclassinocom</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/664992" target="_blank">📅 18:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664991">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad19fb633.mp4?token=SESBBNYViXYJ08W8qgdBWu3Vkeu3RHnLJeNiJP9TE--avRzCc7lqg7poCsrXRbrvSk_QGFwTA10CNuYEO6ufMNntHdiJvJ_gbBGl2XqqASHOg4CSwodZexq64nU-k68lxblwC8xbDwwTXUxg1H9Fbn3qQwIsDAx7OkM96VkENYI0SZrSdybcNVqPPjuDTy_Ao2hh8nX-NLTkO3QPwI7GxfWQOW2eN3d86QxZxcrE3m6cdLi0TrLcYpyqstL9bxWYi2bLb9TwxcYf5G0A4Rr8PQgsZx43IuAs4wmxfvnCXpk1sdwZwUa77WCvIAHkU-d7n4LX8bFVSXoWrJy7qIJgoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad19fb633.mp4?token=SESBBNYViXYJ08W8qgdBWu3Vkeu3RHnLJeNiJP9TE--avRzCc7lqg7poCsrXRbrvSk_QGFwTA10CNuYEO6ufMNntHdiJvJ_gbBGl2XqqASHOg4CSwodZexq64nU-k68lxblwC8xbDwwTXUxg1H9Fbn3qQwIsDAx7OkM96VkENYI0SZrSdybcNVqPPjuDTy_Ao2hh8nX-NLTkO3QPwI7GxfWQOW2eN3d86QxZxcrE3m6cdLi0TrLcYpyqstL9bxWYi2bLb9TwxcYf5G0A4Rr8PQgsZx43IuAs4wmxfvnCXpk1sdwZwUa77WCvIAHkU-d7n4LX8bFVSXoWrJy7qIJgoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروش خیابانی مردم پاریس در حمایت از مردم فلسطین
🔹
در ادامه واکنش‌های جهانی به فجایع نوار غزه، شهروندان پاریسی با برگزاری یک راهپیمایی گسترده، ضمن اعلام همبستگی با مردم فلسطین، وضعیت انسانی در غزه را به شدت محکوم کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/664991" target="_blank">📅 18:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664990">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=e409YFlvTzefcbpwzZF9Mgnyb0rCHjlLdAZaMFk-q549LqHVatGkoP4LL2nMeVnMKLYMov1WkH-R_-Sn5vbbPoP4Oi3wHXPp7gQj1vhVnJMlk9kb85iVMDPjNx82KD2Uovt5aDDWPn_QZNDhlXL5ZxJQ0-AvU5mVzbiWBaCH3Eo1f518VMF941nu2-3a-ohX70fQ8rJOp5f03nuWVWhY7H2759h3wPv9LQjhVJiLK1CB5YCjn5IVDbqerQMHHbawvhpXVM1pXZtjpXbbStfq5ah9BsddzwY_KOdF3yNO7Wh0FgMwpBZ9kdo4ZCUvhaKorMCjGlHsRnDxlag6r7MsGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d0f8bf94.mp4?token=e409YFlvTzefcbpwzZF9Mgnyb0rCHjlLdAZaMFk-q549LqHVatGkoP4LL2nMeVnMKLYMov1WkH-R_-Sn5vbbPoP4Oi3wHXPp7gQj1vhVnJMlk9kb85iVMDPjNx82KD2Uovt5aDDWPn_QZNDhlXL5ZxJQ0-AvU5mVzbiWBaCH3Eo1f518VMF941nu2-3a-ohX70fQ8rJOp5f03nuWVWhY7H2759h3wPv9LQjhVJiLK1CB5YCjn5IVDbqerQMHHbawvhpXVM1pXZtjpXbbStfq5ah9BsddzwY_KOdF3yNO7Wh0FgMwpBZ9kdo4ZCUvhaKorMCjGlHsRnDxlag6r7MsGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار حوزۀ مقاومت: ۵ هزار لبنانی در جنگ اخیر شهید شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/664990" target="_blank">📅 18:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664989">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
منابع العربیه: ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد.
🔹
ادعای وزیر خزانه داری آمریکا: چین همچنان تنها خریدار نفت ایران است.
🔹
چین خواستار حفظ روند مذاکرات میان ایران و آمریکا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/664989" target="_blank">📅 18:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664988">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY8tn5z6w6WJT3qenKsemrH2_G1m8WtpMGXUSXV9Epm3hGC7xOewkA3NcH8mTnziiYoJk5ywpMwQTyVycGt5HCr2-XMx_Ej9rkZTlSvmij_UYUw-k0MwW0qnDBnO80LuQoPdEQw-MxVy5m7MIxtyxT4gVgsbEKo6-msc-Hje7dx6EkaxtkVAvxX35PAl4MZhsTzzL3-Dl3LvkcqzkkgN4PQroW6C6KCwH80HNpneOAEqYjAnrJ9goEm5NXSBF5XlDiZEW48SNLHFY39I6Eda9_HmiEUEW4q81D9AN4CpySZ3NRdswY1izfutOMZINxFgHlHWbmU6w0f4pDbUvq4ovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخستین خلبان زن ایرانی را بشناسید!
🔹
عفت تجارتچی، نخستین زن خلبان ایران بود. او پس از تأسیس باشگاه هواپیمایی در سال ۱۳۱۸، نخستین زن ایرانی شد که در دوره‌های رسمی خلبانی ثبت‌نام کرد، گواهینامه خلبانی گرفت و نخستین پرواز مستقل خود را انجام داد. تجارتچی پیش…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/664988" target="_blank">📅 18:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664987">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
بازداشت شهروند آمریکایی در قدس اشغالی به اتهام همکاری با ایران
🔹
رسانه‌‌‌های صهیونیستی گزارش دادند سازمان امنیت داخلی رژیم صهیونیتسی (شاباک)، یک مرد حدود ۲۰ ساله با تابعیت آمریکا را در پی اتهامات مربوط به فعالیت‌های جاسوسی برای ایران بازداشت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/664987" target="_blank">📅 17:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
خبرنگار شبکهٔ المنار گزارش داد که توپخانهٔ ارتش رژیم صهیونیستی شهرک بیت یاحون را در جنوب لبنان هدف گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/664986" target="_blank">📅 17:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
♦️
نیویورک تایمز به نقل از دبیرکل سازمان بین‌المللی دریانوردی: امکان ایجاد صندوقی برای پرداخت‌های داوطلبانه برای تنگه هرمز وجود دارد
🔹
گفتگوهایی با مقامات عمانی درباره مدیریت تنگه هرمز انجام شد.
🔹
گفتگوها درباره هرمز با هدف یافتن راهکارهایی برای بحران پس از جنگ انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/664985" target="_blank">📅 17:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21eeb708c5.mp4?token=Fe6wpa7FjU7AD5cJgYbAaGHXvJkk8SVKYz9VBcdNpPSLBMXovFhSecwP03GB8GSMyuyUQZaHmxvF4nZufvczD1IxGqzCyMZ9jqGI43Ljgxh9cgPGovMyr_M6r6paqmc8Ib1xXX_hOqetoG3kPpBTPKjSffDoHKoOsJFCAjk5RG2BJET23qq-Yzn4kTYQc93owtsrD3qnKb8UqnxzNL_wTi_-ge7EyL7lK0TZpfy3c8_C4n_AWoUO9N1F0pQ-l583WPOBWWov3JrxYoSPY0j4xlgm5sR4naxRE6BKJEAjhXPq1YkPrjvS4AmL8f1luq_xWcYe1IhR1_-h0Z_FuEUSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21eeb708c5.mp4?token=Fe6wpa7FjU7AD5cJgYbAaGHXvJkk8SVKYz9VBcdNpPSLBMXovFhSecwP03GB8GSMyuyUQZaHmxvF4nZufvczD1IxGqzCyMZ9jqGI43Ljgxh9cgPGovMyr_M6r6paqmc8Ib1xXX_hOqetoG3kPpBTPKjSffDoHKoOsJFCAjk5RG2BJET23qq-Yzn4kTYQc93owtsrD3qnKb8UqnxzNL_wTi_-ge7EyL7lK0TZpfy3c8_C4n_AWoUO9N1F0pQ-l583WPOBWWov3JrxYoSPY0j4xlgm5sR4naxRE6BKJEAjhXPq1YkPrjvS4AmL8f1luq_xWcYe1IhR1_-h0Z_FuEUSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«شاه‌بوف» بزرگ‌ترین جغد ایرانی در قاب دوربین محیط‌بانان آبیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/664984" target="_blank">📅 17:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664983">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzi6YXMOKh5AcKkUtGrobqifjGDWf4VAKvbrqHsBP0f8yRvW4AURFRfXZqNdHq4rSChaxRLCLxTlpQ7t9-E1Q3xRFL80jDLOa3g5YyhtQyc9VwQqYgyAAd35vfzpF-xA-HgTcfqsCePmKW--eOhzrFfYqKDqOjV_AUnS6f1fn5BUVKgbtxjXI3ZFZB6DFAjoFikugclA0-zpwXVwBbbF-2E4lRkgtO8Z45Zl2YQGqQAIyGUXAl7gDjItCO3z_R1hVhXmBXI0k2lkxUS64yN9U2Zn7x_kQJu6MTXBw1Ur_q-k-tmVyZDQhgnKVhikhVG4zTOXvJMlsVnGgQISSWsRzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرنا متن خبر درباره رای سعید جلیلی درباره توافق با آمریکا را تغییر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664983" target="_blank">📅 17:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664982">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
با ورود سازمان بازرسی به پرونده‌های بزرگی نظیر «چای دبش» چندین هزار میلیارد از حقوق بیت‌المال بازگشت.
🔹
پیکر فرزاد جمشیدی فردا در قطعه هنرمندان به خاک سپرده می‌شود.
🔹
رئیس‌جمهور گرجستان در مراسم تشییع پیکر رهبر شهید ایران شرکت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/664982" target="_blank">📅 17:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e5ccb5800.mp4?token=mB0cVbd9y2QcaFigiYgiMhfIAs0JWVupkDqEVgjM9snB0qxaWvSV141JEJjwxwdARJ69DgtMMpIMaEfixIgWsck_gLQvKGPgX20NZsRat4ndYzrBAcC1dXlaX9XIQVaDkqgeN49pfb_X28_Q1l3-X_95u9Z6PuVspRNaD8cn_Cb8nua6HO9lgUkIZRSkWXAwt4NN1Cl1AO1I8byPFvtlgyH10yzc8fHv9TbU1aknjHDROoBZFa2HSe2cozUQg9H5Rqy1TADi4ywbaxphQs9chZPBZuU32CCZcRgRlT8M6wK9Mzk66XgGuE2-WmDkrXdKnwUPNFPHS_UEcE3mHiysiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e5ccb5800.mp4?token=mB0cVbd9y2QcaFigiYgiMhfIAs0JWVupkDqEVgjM9snB0qxaWvSV141JEJjwxwdARJ69DgtMMpIMaEfixIgWsck_gLQvKGPgX20NZsRat4ndYzrBAcC1dXlaX9XIQVaDkqgeN49pfb_X28_Q1l3-X_95u9Z6PuVspRNaD8cn_Cb8nua6HO9lgUkIZRSkWXAwt4NN1Cl1AO1I8byPFvtlgyH10yzc8fHv9TbU1aknjHDROoBZFa2HSe2cozUQg9H5Rqy1TADi4ywbaxphQs9chZPBZuU32CCZcRgRlT8M6wK9Mzk66XgGuE2-WmDkrXdKnwUPNFPHS_UEcE3mHiysiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات گسترده به شیعیان روستایی در حمص توسط عناصر وابسته به الجولانی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/664981" target="_blank">📅 17:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664980">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b656067582.mp4?token=SEIzp6UTGWGdX7jgLwzKLVhWngSkH7iUhONa0HSMH6tVHMNh8_obbVL-FljLYTfCkq9A8voWDCQmwMlwHEA3WjBFc8_muikZAU8qoJjK-3Krx0hOjk9yW1r4HzIEN2u_r6EXQLgrK0vLzjQFMIPn3dMBbC-zGQVOM5Nle2KDOb-Sie1CUw4bu107q_ErRlml4n7hFW4kj45zLZZXVqX2UF64kElYFpJ4VioM2iGiZSDxADhH0Kicumr9ak2gUCIwUTVXqOcCtoPkz-37nnHTFAaP4vP6l5-2pTHINtMmrUsgg1aqiCTcJM2EJvqZ6zy3BfnkUFeGVPYhKMz0TWzvhlH9GBp7qe1EluHExf6vmOChreHQ1UR5-oRrjnXKf1jY2bidGptoYQe5TEKBhFQAKBiAOa9Q9XmQYNUWfrUsj8Q6BTtyks1aNyoX_jZf4v0hdAwyrFfNhWwiIRfuMHlwwfdUWru2aLcLTQjAwqYVnPoT0TMhKSe1jRD2v8nf61XTH_KyLsdQKb807dlbAoBiCpUiByeArmhCqY0aDpIwYdccGzRKeAtUUvHEYwVHaYlqJYRjkfQsfIACJlPEYMjur-0cGNg5961hDCJYFNI_aVFSOYJCVT9Gf2Tz7WmKaZo7re1pU-UjZA4kRySFL9JAmNKAk-x2OxnyBBTrcvuUsOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b656067582.mp4?token=SEIzp6UTGWGdX7jgLwzKLVhWngSkH7iUhONa0HSMH6tVHMNh8_obbVL-FljLYTfCkq9A8voWDCQmwMlwHEA3WjBFc8_muikZAU8qoJjK-3Krx0hOjk9yW1r4HzIEN2u_r6EXQLgrK0vLzjQFMIPn3dMBbC-zGQVOM5Nle2KDOb-Sie1CUw4bu107q_ErRlml4n7hFW4kj45zLZZXVqX2UF64kElYFpJ4VioM2iGiZSDxADhH0Kicumr9ak2gUCIwUTVXqOcCtoPkz-37nnHTFAaP4vP6l5-2pTHINtMmrUsgg1aqiCTcJM2EJvqZ6zy3BfnkUFeGVPYhKMz0TWzvhlH9GBp7qe1EluHExf6vmOChreHQ1UR5-oRrjnXKf1jY2bidGptoYQe5TEKBhFQAKBiAOa9Q9XmQYNUWfrUsj8Q6BTtyks1aNyoX_jZf4v0hdAwyrFfNhWwiIRfuMHlwwfdUWru2aLcLTQjAwqYVnPoT0TMhKSe1jRD2v8nf61XTH_KyLsdQKb807dlbAoBiCpUiByeArmhCqY0aDpIwYdccGzRKeAtUUvHEYwVHaYlqJYRjkfQsfIACJlPEYMjur-0cGNg5961hDCJYFNI_aVFSOYJCVT9Gf2Tz7WmKaZo7re1pU-UjZA4kRySFL9JAmNKAk-x2OxnyBBTrcvuUsOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار فیلمی از حضور رهبر شهید در حرم امام رضا (ع) برای نخستین بار - سال ۱۳۶۴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/664980" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664979">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
انهدام تیم تروریستی در مرزهای شمال‌غرب
🔹
قرارگاه حمزه سیدالشهدا(ع) از انهدام یک تیم ۶ نفره از عناصر گروهک‌های معاند در ارتفاعات میان مهاباد و پیرانشهر خبر داد؛ در این عملیات چهار جسد به‌همراه سلاح و تجهیزات کشف شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/664979" target="_blank">📅 17:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664978">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIxjZHn6VtmWsBTIqzXdYq8WFRuGS0VbB94lOK3Nm1aEFdavUZKjGuuz-GflK0OzCuNFvmj_lS8kCpT3sBw3-7OOIpXNnlqOIDeqKLq3s5ND12byEhWNviDQMU0KUJaYQ0rc8oh8lh-gl4t8kxnSyesJrfLtimfJ2-fqH0kH7yXG16ehpSC5ficjcJPsfMxiZ8OQx67vRfycQjQWgUKFfTaGBkKcy4E5vsP7FKmLGKOwi-uzCobQt43dQ-ObdZ5Yky8tOkseuQpdxf0DL16ji6m5zqdiAJZ-TCM8O-FyK0jnP4xvaMGP7K7fzHUrvXuIN1VZBn2ZkyqAXqLpNuIiWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشتی‌ها از تنگه هرمز فرار کردند!
نیویورک‌تایمز:
🔹
کشتی‌ها پس از چهار روز حملات توسط ایران و آمریکا و افزایش خطر از تنگه هرمز عقب‌نشینی کردند. طبق داده‌های کپلر، با وجود خطرات آخر هفته، ۲۲ کشتی روز یکشنبه از تنگه عبور کردند که نسبت به ۳۸ کشتی در روز شنبه کاهش یافته است. روز چهارشنبه نیز، ۷۴ کشتی عبور کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/664978" target="_blank">📅 17:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اختلال گسترده GPS در کشور؛ تهران بیشتر از شهرهای دیگر تحت تاثیر است
🔹
طی روزهای گذشته بسیاری از کاربران، به ویژه در شهر تهران، گزارش‌های متعددی از اختلال گسترده GPS داده‌اند. بررسی‌های دیجیاتو نیز این مسئله را تأیید می‌کند.
🔹
روابط عمومی مسیریاب «نشان» این اختلال‌ها را تایید کرد و گفت: «اختلال GPS طی سه روز اخیر شدت گرفته است. این اختلال‌ها به‌ویژه در شهر تهران بیشتر دیده می‌شود.»/ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/664976" target="_blank">📅 17:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4a5d2d004.mp4?token=CeSP--xIIOM5Qo62nwsyBz2h01qOQXkfae7f7XaVQta1nrhDUEVIXWCSk6DvLkubZzojZhTxXAyipMs9WiQD7gb2u1Pcp6mDmXyv4PXHs9Rx1BdP1CxtjQeVf5YpzBNqeCEkvTnL-76ijCfyzoMwhUeool1fKATu8yFIZp_S-jBTsIJDQ3X_rKBJil-XUkWL1OEmAU6BMa6La2z8Pdf4G_Es_3OAY9SIvkVpnqR9nomD8sCBzizUYvtM43qFaBQteUA1Br7CWgoeZp8c1Ve9hVQk6gQRBm3pSmZ98RlXitfu179NmOyFx6I9TjwDTh0gHtYnP5ADwph6l5kDwenTWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4a5d2d004.mp4?token=CeSP--xIIOM5Qo62nwsyBz2h01qOQXkfae7f7XaVQta1nrhDUEVIXWCSk6DvLkubZzojZhTxXAyipMs9WiQD7gb2u1Pcp6mDmXyv4PXHs9Rx1BdP1CxtjQeVf5YpzBNqeCEkvTnL-76ijCfyzoMwhUeool1fKATu8yFIZp_S-jBTsIJDQ3X_rKBJil-XUkWL1OEmAU6BMa6La2z8Pdf4G_Es_3OAY9SIvkVpnqR9nomD8sCBzizUYvtM43qFaBQteUA1Br7CWgoeZp8c1Ve9hVQk6gQRBm3pSmZ98RlXitfu179NmOyFx6I9TjwDTh0gHtYnP5ADwph6l5kDwenTWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامۀ انفجارهای سریالی خودروها در اراضی اشغالی
🔹
کانال ۱۲ رژیم صهیونیستی گزارش داد خودرویی در حیفا منفجر شده و صدای انفجار در سراسر منطقه شنیده شد.
🔹
تاکنون علت انفجار اعلام نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/664975" target="_blank">📅 17:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664973">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3gJXTIAPp2hipYRVz0LKZZPIyIsd76DeN6InVkhHpV3f41M6T4IWlrqYP7bXAlTm-Jsk5LOIpW6L1qWR88gcFePPBs5ptSlcCSPxLyYe7F7wPcsO8Wt8-GImPDGW6WJaYrBr4_eLu2EwkLA5KmpgqaSuR7_4Ef4TfxE0oG3BO3p7MFhxnb-9egfbR7qebb0s40R7bw3SxOE1ABx1IqbmUsrIAitVt5pwOcoUcIhw0QlzMjUcXZdtlN7aqFmvqyPw3hMsG1-E1Gw2xWx8NftCiUGEKNcc36jYIGyIzLpKDBqVjzfLthstskPC7MTChLcfIWu63qVRZ_X39Sycag0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ردپای کربنی سفرهای رئیس فیفا زیر ذره‌بین
🔹
از زمان آغاز جام جهانی، جیانی اینفانتینو، رئیس فیفا، برای تماشای ۲۵ بازی در ۱۶ شهر مختلف سفر کرده است.
🔹
او در این مدت با هواپیمای شخصی خود بیش از ۵۰ هزار کیلومتر پرواز کرده است.
🔹
گفته می‌شود این پروازها به اندازه آلودگی کربنی سالانه ۷۸ نفر گازهای گلخانه‌ای تولید کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/664973" target="_blank">📅 17:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664971">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a561da02c.mp4?token=JbdYUDp73xkoLjuloS6j89G0lPCjcAMs-RbTIAEgiRYa8Rfz1rSxzS5__X2CewvWeQYfZUXedd1Oe2ZDbpDAdKB5loMoEP1MQV7Le-wxQdMjzdT6PuO-fZNDIv3DrYnBLXDRcVpeSxH4zCi0fxTts_Q95tAJRSW2sAUS7YikJcUO6LMWt0YSUpvCo6iU0-DzTTOl-pSPqHW16j_cfYd47m6Yh6yYie_dcuBhg5KpsTC4jU66oGNpFfdCHwJdEAWr5bB2zrwlUVToGmGxPxTuqXVF2AxuJJSTww7bU2uf3g_nnv83THTt7mxUEuOwtw-NK7kn69ytRnctEbMNwkHe4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a561da02c.mp4?token=JbdYUDp73xkoLjuloS6j89G0lPCjcAMs-RbTIAEgiRYa8Rfz1rSxzS5__X2CewvWeQYfZUXedd1Oe2ZDbpDAdKB5loMoEP1MQV7Le-wxQdMjzdT6PuO-fZNDIv3DrYnBLXDRcVpeSxH4zCi0fxTts_Q95tAJRSW2sAUS7YikJcUO6LMWt0YSUpvCo6iU0-DzTTOl-pSPqHW16j_cfYd47m6Yh6yYie_dcuBhg5KpsTC4jU66oGNpFfdCHwJdEAWr5bB2zrwlUVToGmGxPxTuqXVF2AxuJJSTww7bU2uf3g_nnv83THTt7mxUEuOwtw-NK7kn69ytRnctEbMNwkHe4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه در پاسخ به سوال خبرنگار خبرفوری: همه ارکان نظام در جریان تصمیم‌گیری‌های مربوط به جنگ و صلح و مذاکرات قرار دارند
سخنگوی وزارت امور خارجه در پاسخ به سوال خبرنگار خبرفوری در مورد برخی انتقادها از هیئت مذاکره‌کننده ایرانی و برخی شعارها و اعتراضات در تجمع‌های خیابانی:
🔹
ما جامعه‌ای چندصدایی داریم و طبیعی است که همه مردم ما تحولات را هوشمندانه و با دقت رصد بکنند و دغدغه امنیت ملی و منافع ملی داشته باشند.
🔹
همه ارکان نظام در جریان تصمیم‌گیری‌های مربوط به جنگ و صلح و مربوط به مذاکرات و گفتگوهایی که برای وضعیت فعلی و آتی کشور بسیار اساسی است، قرار دارند. این‌طور نیست که یک وزارتخانه یا یک دستگاه خاص به تنهایی تصمیمی را اتخاذ بکند. حتماً هر تصمیمی با توجه به سنجش معایب و مزایایش اتخاذ می‌شود و وزارت خارجه در نهایت موظف به اجرای دستورالعمل‌هایی است که از سوی نهادهای بالادستی، از جمله شورای عالی امنیت ملی، به آن ابلاغ می‌شود.
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/664971" target="_blank">📅 17:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbGvxgTO_IJvJaVea0FPLi0mVNa7kOAmaFIBxOkKCjUj8y1vuv7UCXFgUZGRM4kJdBt4088JtljMGPgtjt5x5xTT8SJYgKXWoj8NMrLHAdsoQfJw23ZHV6PKbK7Kj-cUyHMAxW7cIZI-HmJEVM_RAJI3Karu4o_6ji27_EYZXQRczuFkLByVuPYhHNlHPZtgMcI4-XcDP18rrVeQcwH2c1J7cvkV04TLvqHfejLi4wef7l7LOmSLMhvqMu8Fy0sLkgUbNQJt2KAJ65n5RW1uIC_4pDSKCNAf-47gKDr4Cyho9jXC-FeLigu3OeXrc4PCIruBamgmCdqguUQyR2vEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیماری لوپوس؛ وقتی سیستم ایمنی به جای محافظت، به بدن حمله می‌کند
🧐
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/664969" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlZojn-PZG4ZChQ9ucKXbiXtaWWj6NZVKC2hiYWb-ZSdA83p_3jynOkABiJyW3UDrS6P2JAhlo-MJmhuyhcceAG_P-QbtedSpMOUiHDvsJ0ueFeoq5xBZZCgc6DUcsXSEEBJveFV1WowQn742vHX0Y7shvjdjujf5XVVm6UUvqxZnPlAb-6qChwd-m13sZRdr315gOI_x6aHcIrsvq6GinBh7kbzJOdo0h-TmYsV8i_Wj-Wr-bvOHC_2jmB5YAtfBq_J9H4C1tR03cBPRXD27WMTPVEgrzKZiU-CbUXNsMaokzirFX1Kr88ZjVBuJ22-KI_08N2KpRzO7GtKOvKvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از ماه، پل‌خواجو و زاینده‌رود
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/664968" target="_blank">📅 16:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBcu4gAYsXKMOVzqlFPZf-B6AwKf4T8U6qho5FsoNdLm4hyvaBtyvnM3-TgH1LxXZjsi8bJm5PsRGVOXTODVDxtph2CxCCSVp0xg71CSWOzVe7ei0yuCaFCFm9p-jSQCbln6kB__d2rGrqZlLbkkhrkYh9Nqv6FzkfeOr8-JXyv2TLzbH-3DrGM78AwK7GSxkYjpXvW0zJU6HXSlNxJcwG9LzM1QGUzXE6c36SjOEJuIrOT4sl-rnR8lPQMa9ungfFnDrYtxqV2xq4xwDrdZ0XJINAbXokzvOrNQ0K0qopG1Nv3yYAYIA0JLpQDcdqrYzh529PBl7pNHGGKD_DJ5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آنچه مسلّم است گریبان جنایتکاران را بایستی گرفت و آنان را به سزای اَعمال مجرمانه‌شان رساند
۷/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/664967" target="_blank">📅 16:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-UlsObVarh2xOlamZQuNg-P5b8OQ8sS1C3Rz-gs4nSCkIl036_Mxd7Rcyn_K2RAojZwmabOqfRiseUy9vDkxfzS7tUvt18ILbO9yDvpwl9C_Rjg4EiHDORgXdo2eCdSgpY_dVRA3HBELhFjvHiOJVA5_FpxRJpYbzyhvShRj9MfuCrs26YtFBidtfN7olD0sAi3jb7UUMREk1388zXtNn2bSoaEctOUC2Yea3ImSMYsz3BfQQx2e1oF7FNB-4N68b2444a1OAG_s9fFscANXjMt73wxrdzKmaAsIOikfYZ7bFXVGFlrk9qrg9dHYwRWLC04HAhw2AWJPl4XeTgBEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مالی کودک از خانه شروع می‌شود #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/664966" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
پرواز مشکوک جنگنده‌ها از ورشو به مقصد تل‌آویو و انحراف آن‌ها به قبرس
🔹
گزارش‌های خبری از یک عملیات هوایی غیرعادی خبر می‌دهند که در آن جنگنده‌ها از مسیر پروازی خود منحرف شده و به سمت قبرس تغییر مسیر داده‌اند. جنگنده‌هایی از ورشو به سمت فرودگاه بین‌المللی بن‌گوریون اعزام شده بودند.
🔹
طبق گزارش‌های اولیه، این هواپیماهای جنگی در جریان پرواز، مسیر خود را تغییر داده و به سمت قبرس هدایت شده‌اند. این حادثه با توجه به ماهیت نظامی پرواز، ابعاد و دلایل دقیق آن هنوز به طور کامل مشخص نشده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/664965" target="_blank">📅 16:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2SwPbmGgMTcW9yPE1eqlvSwDjM6QgqoS2RbMX5PY7TSaeSMW_SxqzV_0nCg-8-4_tQvb8mhyrLFJ1aB8w0AEpgTGgf1gOpBTdeDY5Jm57mUWcTE-22O06shcYe9iFfbqQxA7prdUi2FK9Nso5vhe0jH3qiul8KoTbGpvVPwIqn4QhtbZOUJm3rfxgu0oKV3CpmlHMR-Xk8jRNtaeLKJuemnOogHY48KDs0buJPl42cmHJnLh0B85GqXlnK-jLOwx486lRUXgpm-w_iXcBCXtJ8yuI1JDIbgEapk7JYfeh3c0hQ9mm0DgCeeP-eQFXpC0gNE92ksRaqwaHQzGmDq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جایگزین‌های ساده برای کاهش مصرف پلاستیک
🔹
استفاده از محصولات چندبار مصرف، یکی از مؤثرترین راهکارها برای کاهش زباله‌های پلاستیکی و حفاظت از محیط‌زیست است.  شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/664964" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-664963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fb403db1.mp4?token=tMXUO9u2nHetPoNtvO2T1Sumn04pyfdIIhIhxgyu7QLjUPPxR7rM6bagCFpm1FulGLQ9dAEiatuf-0vH16SDrxo8U90KJLbE6N1GgA6Jgjhp30T9mogFNhjpV3M64qfh-P-ztht1dOrLjBiffCV2DUghy8hrHSy9J-rHOq8DIdAUPW6eGWfApVLhFSXra1MsjjPyn-En_D2g73HeB6q9aniyEzvzj64CllyXXuSGtxbVHbgZvXsCbtB_vpRAzurF3UuOSqoIPGdCT6pCXvcbQDfxy_KuKTl8tGbYxFQ0vY2jWkmYnT6O9x6BOrh2hzQw86Udlf_WhaWVKInBhky2LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fb403db1.mp4?token=tMXUO9u2nHetPoNtvO2T1Sumn04pyfdIIhIhxgyu7QLjUPPxR7rM6bagCFpm1FulGLQ9dAEiatuf-0vH16SDrxo8U90KJLbE6N1GgA6Jgjhp30T9mogFNhjpV3M64qfh-P-ztht1dOrLjBiffCV2DUghy8hrHSy9J-rHOq8DIdAUPW6eGWfApVLhFSXra1MsjjPyn-En_D2g73HeB6q9aniyEzvzj64CllyXXuSGtxbVHbgZvXsCbtB_vpRAzurF3UuOSqoIPGdCT6pCXvcbQDfxy_KuKTl8tGbYxFQ0vY2jWkmYnT6O9x6BOrh2hzQw86Udlf_WhaWVKInBhky2LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش اسرائیل یک شبکه تونل ۱۶ کیلومتری حماس را با سیمان مسدود کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/664963" target="_blank">📅 16:32 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
