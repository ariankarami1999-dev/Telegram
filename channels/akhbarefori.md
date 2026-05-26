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
<img src="https://cdn4.telesco.pe/file/D2gMOXsrmo1xfjw5akw12kNWHf3xaE8zWgVu_4dPfupUkIAmstyEfMLebjTyrfoAsKb73hdchgda1okfHxYCDghPMxT0WKoZtmal-SJHlqYqBVQmH75hmFw-6tcm8mvrSMcznpzt8ATSKR0tG46ZqvXhSUZU7tWqzAM2W97JPPHyp0SdANlgab3KtbMahkADgZyTdGR_0i9hZCYYD6TqBVZT05a79yCT-YYPid855lpQdvij8uhT3PkY0_P38E3wJ7mg_H-r32AkyJL040rG2mVq33JRVkLSIQicQmcictIrctjyDYK6jvX51shVpagpgdlmTj6AZxDjVN7ma4GGRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 02:32:37</div>
<hr>

<div class="tg-post" id="msg-654261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
مقام غزه: جنگ هنوز ادامه دارد
🔹
«محمود بصل» سخنگوی اداره دفاع مدنی نوار غزه شامگاه سه‌شنبه گفت که آتش‌بسی در این باریکه وجود ندارد و اشغالگران تاکنون ۲ هزار و ۸۰۰ مرتبه آن را نقض کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/akhbarefori/654261" target="_blank">📅 02:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47e4223c92.mp4?token=YayvtvMdbQ7nXkNs9OuzmZCXtveX-SuUNd9HzOIeLm283K95LT0qlTqljaLNm94JNyTViHFJKO3vmvTLMLs2-XOXklW6EMeFrulbIrPRWPTtlWKrUBOhMn7eqEV7C_Q4vyZtYUTvgVI9LalYbn5S4lHNgvFs9bpJaaLxJPvSsOmsCV04n8qkRWjTpJS1xx9TCd3eFp8hENzJaRZPIt43NCCjbh4basOuhiqYIab_glkWS1S6n7hqZvNSgj-RjTxD2iHoc2zLyH7ZLl0iMIlli8_UpZJK6f-sexPPJkpD2aHfaK6n0M7LDMcKsdi9qnhfyn9v12zkDANjl4QGjBC4tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47e4223c92.mp4?token=YayvtvMdbQ7nXkNs9OuzmZCXtveX-SuUNd9HzOIeLm283K95LT0qlTqljaLNm94JNyTViHFJKO3vmvTLMLs2-XOXklW6EMeFrulbIrPRWPTtlWKrUBOhMn7eqEV7C_Q4vyZtYUTvgVI9LalYbn5S4lHNgvFs9bpJaaLxJPvSsOmsCV04n8qkRWjTpJS1xx9TCd3eFp8hENzJaRZPIt43NCCjbh4basOuhiqYIab_glkWS1S6n7hqZvNSgj-RjTxD2iHoc2zLyH7ZLl0iMIlli8_UpZJK6f-sexPPJkpD2aHfaK6n0M7LDMcKsdi9qnhfyn9v12zkDANjl4QGjBC4tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی شدید رژیم صهیونسیتی به شرق لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/akhbarefori/654260" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
۳۲ عملیات حزب‌الله علیه مواضع ارتش اشغالگر
🔹
مقاومت اسلامی لبنان اعلام کرد که در ۲۴ ساعت گذشته در مجموع ۳۲ عملیات پهپادی، موشکی، توپخانه‌ای و کمین علیه نظامیان، ماشین‌آلات و مواضع ارتش صهیونیستی انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/akhbarefori/654259" target="_blank">📅 01:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
وزیر دفاع یمن: نیروهای مسلح ما همچنان دست به ماشه هستند
🔹
وزیر دفاع و رئیس هیئت ستاد کل نیروهای مسلح یمن گفت که یگان‌های نظامی این کشور در بالاترین سطح آمادگی و هوشیاری قرار دارند و دست آنها روی ماشه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/654258" target="_blank">📅 01:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ویدیویی که «بیسان عوده»، خبرنگار شناخته‌شدهٔ اهل غزه، از محله الرمال، در شب عید قربان و درحالی که مشغول خریدِ عید بود، منتشر کرد و از این گفت که حمله، در یکی از شلوغ‌ترین ساعات و شلوغ‌ترین محلات غزه رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/654257" target="_blank">📅 01:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل به نقل از یک منبع امنیتی مدعی شد که ترور محمد عوده (فرمانده جدید شاخه نظامی حماس) با موفقیت انجام شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/654256" target="_blank">📅 00:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fef1a040e.mp4?token=L9HX-L3Tf5onUVnWHumW5YeOohWdfJtsvYgO5ZDKVHAUoTgutr1ovUgcpLlA4KF9fXPGa1I9vd-3kZqZ8uOAXvedcNRYCqYCWHEl-ojh1yl7n_yYZlvuF3HjfljXMR98law6sHSzFhQEAlr2ZsKBKrr_O6gkU_E2PUBoKzHvTluz9fGUJx_RQUz2ZW2QLX9pCtE_rs2qxxIE2TtnAARshR9Vz0Rh12HaHngKOdqywMPaIQE1eeedxmm6poM3q2W4_wC45Gv916Ftws2PO8UfhCriB19bwXP1t4IaFifoQgcmvtYUPvqdl7e-bHFHGeuyG4BLRGobEDLkXIUBIFlkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fef1a040e.mp4?token=L9HX-L3Tf5onUVnWHumW5YeOohWdfJtsvYgO5ZDKVHAUoTgutr1ovUgcpLlA4KF9fXPGa1I9vd-3kZqZ8uOAXvedcNRYCqYCWHEl-ojh1yl7n_yYZlvuF3HjfljXMR98law6sHSzFhQEAlr2ZsKBKrr_O6gkU_E2PUBoKzHvTluz9fGUJx_RQUz2ZW2QLX9pCtE_rs2qxxIE2TtnAARshR9Vz0Rh12HaHngKOdqywMPaIQE1eeedxmm6poM3q2W4_wC45Gv916Ftws2PO8UfhCriB19bwXP1t4IaFifoQgcmvtYUPvqdl7e-bHFHGeuyG4BLRGobEDLkXIUBIFlkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار روسیه به کشورهای حاشیه خلیج فارس درباره پیروی از آمریکا علیه ایران
🔹
«واسیلی نبنزیا» نماینده روسیه در سازمان ملل شامگاه سه‌شنبه خطاب به کشورهای عربی حاشیه خلیج فارس گفت:‌ «شما گروگان سیاست آمریکا در خاورمیانه هستید!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/654255" target="_blank">📅 00:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
حجت الاسلام قمی: بحران جمعیت و تبعات آن از نبرد نظامی هم سهمگین‌تر است
🔹
حجت الاسلام محمد قمی در صفحه شخصی خود در شبکه اجتماعی ویراستی نوشت: اگر بگوییم بحران جمعیت و تبعات آن، از نبرد نظامی هم سهمگین‌تر است، اغراق نیست. تبعاتی که شاید الان نه، ولی در آینده حتما گریبان ما را می‌گیرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/654254" target="_blank">📅 00:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be028be8c.mp4?token=OAdu8xjvn1jjNDtzo3-GPw6wVy_1D56W5ctEiIojPF30qyVk2GykRPP2V9rThej0XEqjuooU6sRsEyPWaA7veNnnWpBMUXb0Ca0bFIbGg7CAQRhZY-HlFtMAcpCtPLDJ9zC2aiNazgO-h-KTjaBm8nmhGzdSeNX_I5-O3E4AAcAZO1iVcC5xqgV33tm656bmkbIzWxNuB4pXEkR902ozoc5Qi8xKUi73rvoXbx9sCFo1yIaT_eAR68OCBYqmV5UkZdJwts0jxUACRTMToD5uVZBWksLmMC1Tnx3BbxEj5h85VfL-VnnVCIJ9zuxAkr8rQDPxXCOFaUqDX8lZaiFjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be028be8c.mp4?token=OAdu8xjvn1jjNDtzo3-GPw6wVy_1D56W5ctEiIojPF30qyVk2GykRPP2V9rThej0XEqjuooU6sRsEyPWaA7veNnnWpBMUXb0Ca0bFIbGg7CAQRhZY-HlFtMAcpCtPLDJ9zC2aiNazgO-h-KTjaBm8nmhGzdSeNX_I5-O3E4AAcAZO1iVcC5xqgV33tm656bmkbIzWxNuB4pXEkR902ozoc5Qi8xKUi73rvoXbx9sCFo1yIaT_eAR68OCBYqmV5UkZdJwts0jxUACRTMToD5uVZBWksLmMC1Tnx3BbxEj5h85VfL-VnnVCIJ9zuxAkr8rQDPxXCOFaUqDX8lZaiFjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر فرار بزدلانه نظامی اسرائیلی از ترس پهپاد حزب‌الله
🔹
کانال ۱۲ رژیم صهیونیستی تصاویر جدیدی از لحظه فرار یک نظامی صهیونیستی از ترس پهپاد حزب الله را در شهرک شومیرا در شمال فلسطین اشغالی منتشر کرد.
🔹
سکانس پربازدیدِ دیگری از فرار نظامی صهیونیست از پهپاد انتحاری حزب‌الله را از اینجا ببینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/654253" target="_blank">📅 00:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی: دیروز پس از آنکه دو شناور هدف قرار گرفته شدند، نیروی دریایی بلافاصله پاسخ داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/654252" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDcuZr5U8GChdu2ssYNcvsCTC48mSfbBU6ezyZsg_uTr9JNqbGTrIcsWZkHEXWHb5DFZpm1yVp5dLYiyj5iGoRh8kpNFPIqcdmlgSbO-NEsb9Uarzk8QgOIC1xdoac_nVOaI1jlygJYCqnKuLcJGldXqP4KmgRsfLQ8Q5SxxRKNNZ4F9_wguAXoKp7W2EPZrXRFYOwg05sUk89Io3DZJmYDWfi_9oWnF4SfXD_LLY8833A90XUXNdcBaHKJsIigGK2A8UV1T-uYeDS36ahNKDjq_uA_fYTI_cJwonBXaiTpxREKj4idthqDvbgtNvRVVw9VsUJUYJ7Fv98-OB_dplQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس یادبود شهدای خانوادهٔ قائد شهید و رهبر معظم انقلاب
◾️
شهید زهرا حداد عادل
◾️
شهید سیده بشری حسینی خامنه‌ای
◾️
شهید مصباح‌الهدی باقری
◾️
شهید زهرا محمدی گلپایگانی
🔹
پنجشنبه و جمعه ۷و۸ خرداد؛ از ساعت ۱۶ تا ۱۸
🔹
مصلای حرم حضرت عبدالعظیم حسنی(ع)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/654251" target="_blank">📅 23:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a14f65b188.mp4?token=Wt32Z1Yd-4NLlMwU-rahvS7XmpzoTCLkXSXFa6tZeSfjeAw_XvZOxVJ-46E0bws6_gdY5FuDMgYUgRJHhCanbTxYvsKSnEn8EKJrcOSQdFvx3rBiEMbBYOzM8alKGSmsodEssYMaQN7BE65E2-uhHtcgTUPBGBavjw2c_5gGvQsZTj2eQ5s7xbu3LVpj3JhAqmxvSVopyVVNW92tCZaRrYUdSNkwL1WTnhHQGMZ6Qk6cwXt5bFlNqwIdxRiXFa46x-NBG0n2hafK4XhMSCwpIF7RNG0U7jCrvm_YShfJ8-cCe_JMTIHVshsoxggWL9bYyclIg5dwuVcBC8lqHyaexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a14f65b188.mp4?token=Wt32Z1Yd-4NLlMwU-rahvS7XmpzoTCLkXSXFa6tZeSfjeAw_XvZOxVJ-46E0bws6_gdY5FuDMgYUgRJHhCanbTxYvsKSnEn8EKJrcOSQdFvx3rBiEMbBYOzM8alKGSmsodEssYMaQN7BE65E2-uhHtcgTUPBGBavjw2c_5gGvQsZTj2eQ5s7xbu3LVpj3JhAqmxvSVopyVVNW92tCZaRrYUdSNkwL1WTnhHQGMZ6Qk6cwXt5bFlNqwIdxRiXFa46x-NBG0n2hafK4XhMSCwpIF7RNG0U7jCrvm_YShfJ8-cCe_JMTIHVshsoxggWL9bYyclIg5dwuVcBC8lqHyaexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیکونهاد، عضو هیئت علمی دانشگاه شهید بهشتی: بدون مصوبه شورای عالی امنیت ملی اینترنت به حالت اول باز نمی گردد، مگر مرجع بالاتر که رهبر باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/654250" target="_blank">📅 23:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKA250qiuNi2JMfPryup6RoOp96Zb6SkoisRzHmvw8Srh6itoryiHJKSEdOqbvNB5G-CK-6Kvz3QmNdvBdcQM00S7REuR6TIRRIE-w9PGo4b0GAMMV1ARrQ4SjRrOA5l_59IIhGxhaxgseKGTmvNVR0Qfv2LtghkGdSYQ52T4uUq9hnz1Vt5SxLrN4scNFAVcRSYHpOLN6dNr9uzY6i-zJzTBZUfVGjEzI4LDb3sRt47TM0z3AqQ2Lgne278Wf2SzplpFrxmXGy8c4xslK-8YdpmEwDavQV486atVNMeI2XzgmpoMIzh0gdedvBzYPMvTop1mlsd85J_FmWwuxR21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: جهان اکنون به‌شدت محتاج توافق میان آمریکا و ایران است
🔹
بدون دستیابی به توافقی پایدار میان واشینگتن و تهران، تبعات ناشی از انسداد تنگه هرمز می‌تواند بحران‌های جهانی در زمینه‌های انرژی، غذا و هزینه‌های زندگی را عمیق‌تر کند.
🔹
اگر به سرعت توافقی پایدار حاصل نشود، پیامدهای آن به سرعت در سراسر اقتصاد جهانی گسترش خواهد یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/654249" target="_blank">📅 23:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
چین: توافق پایان جنگ ایران و‌آمریکا برای تأیید به شورای امنیت سازمان ملل ارائه خواهد شد
🔹
وانگ یی، وزیر خارجه چین گفت که پکن معتقد است توافق پایان جنگ آمریکا و اسرائیل علیه ایران باید به شورای امنیت سازمان ملل ارائه شود.
🔹
وانگ گفت پکن امیدوار است طرف‌های مربوطه بتوانند به دنبال کردن آتش‌بس متعهد بمانند.
🔹
او گفت: معتقدیم که پس از دستیابی به توافق، برای تأیید به شورای امنیت سازمان ملل ارائه خواهد شد تا مشروعیت و اقتدار داشته باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/654248" target="_blank">📅 23:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654247">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcamJVttZrBV8bd2aaGgPZwQ3EdNez0_YjSi2rB8j_kBeTgpPTNiFbsZpC2cQJ0QONDDA8IoqLyW2jEzBgtVJLsoVLT7dzJBFAInYsBrOHZJxE4lMLtFGkHQyeMXPeqlEg1qssANOoIH7vH3TkV520sFVlm-5SjYVqgS4PZ70hkMKOtLXyfHjgU4aOFuCG1MR-xKZmRJEwgU1UxQ0Y-tXawGMn2BHnGltilJZSThzUrZvsIKfW7jVq0Z5mY0ldIfkejFOei-E2JPxYfeTbUPz7u-UTl5MeE_mNlSF22XYrFKTUiwMzm0nHLJ7ChQOd4tlfEvKKdN7svz9mXVuPP8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آشفتگی در آمارهای پنتاگون از تلفات نظامیان در جنگ
🔹
تحقیقات اینترسپت نشان می‌دهد که آمار و ارقام ارائه‌شده از سوی پنتاگون درباره تلفات جنگ علیه ایران بدون ارائه هیچ توضیح مشخصی کم و زیاد شده است.
🔹
اینترسپت می‌گوید مقام‌های آمریکایی تاکنون به درخواست این رسانه درباره آشفتگی‌ها در ارائه آمارها پاسخی نداده‌اند.
🔹
این رسانه نوشته که وزارت جنگ آمریکا در حال پنهان کردن آمار نظامیان کشته و زخمی‌شده در جنگ علیه ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/654247" target="_blank">📅 23:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654246">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
علی باقری: نشست مسکو بستری برای مقابله با قلدری و زیاده‌خواهی آمریکا است
🔹
معاون دبیر شورای عالی امنیت ملی: ابتکار روسیه برای جمع کردن کشورهای مستقل خارج از چارچوب یک‌جانبه‌گرایی آمریکا، گامی برای برقراری صلح و ثبات جهانی است.
🔹
عضویت هم‌زمان ایران و روسیه در سازمان شانگهای و گروه بریکس، بستر مناسبی برای تقویت همکاری‌های سیاسی، نظامی و اقتصادی ایجاد کرده است.
🔹
هدف از این رایزنی‌ها، صیانت از امنیت کشورهای مستقل و جلوگیری از تحمیل منویات و زیاده‌خواهی‌های آمریکا بر دیگر ملت‌ها است.
🔹
دیدارهای دوجانبه در حاشیه این اجلاس، نقش کلیدی در نزدیک کردن دیدگاه‌های کشورهای مستقل و حفاظت از حاکمیت ملی آن‌ها دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/654246" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654245">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482bfde588.mp4?token=T7hKxU4NCueD9IHT4aGQQTV6TltsROSXOCrK3Uq7RQVzAVGYwgqGCx5vT9tfj_AMCo8l8atrLrOJIvdcIYYY7zLb8xiHlaPX7gJgi0WAG9jM3R7FE3iftjwMT3tKpBx9o1RNAT0AEoP-i3x4XDBBlxhbBY21a6uDftqzy9CU392Flg2xMuLB92Koq6fWXP3eB4Rd7U2W3Tm1P__jd6zKHmeBGxwornIUPV4I7cjmehB4HfPtGLHnlaYyrKxpIAtZ3zkQlTLFqI6o4CbDaSjw3XEMg2P1tFB15pDoQ7yi_S01OXqRNQvkdsnFDZqQAy9twDTabxw_OUZiygxV_XKOQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482bfde588.mp4?token=T7hKxU4NCueD9IHT4aGQQTV6TltsROSXOCrK3Uq7RQVzAVGYwgqGCx5vT9tfj_AMCo8l8atrLrOJIvdcIYYY7zLb8xiHlaPX7gJgi0WAG9jM3R7FE3iftjwMT3tKpBx9o1RNAT0AEoP-i3x4XDBBlxhbBY21a6uDftqzy9CU392Flg2xMuLB92Koq6fWXP3eB4Rd7U2W3Tm1P__jd6zKHmeBGxwornIUPV4I7cjmehB4HfPtGLHnlaYyrKxpIAtZ3zkQlTLFqI6o4CbDaSjw3XEMg2P1tFB15pDoQ7yi_S01OXqRNQvkdsnFDZqQAy9twDTabxw_OUZiygxV_XKOQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس : آزادسازی ۱۲ میلیارد دلار از شروط ابتدایی ایران در مذاکره است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/654245" target="_blank">📅 22:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654244">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a2ec2172.mp4?token=F90l-MrXhCdcE6ujKNM42dq_JXvi2Vv8ngcSsxGvIUd_wHsCZnB3il32iWpVABw4bMuIv9QmY8pxpht_nX1RwCTn1uiCzrkxR0zvIAd-sSgF5ebs8RdJLovnU6ZxjDs-KEDp3iHDR55IVUTHnO55WClsapZPA-9flbcIaf5zACE2xVJCa1YM1-KRfDsRlv6rRNjYS8QsdLJXJlNsaBFqC1xaeniaJHo7IVe5DosEuLphl_bOQQBszk-Xrfvo36iZct2PVdECPs2JD1pJqvGi4DWT-b5_3QBi_quvyzy9xUhiXMsx2zLspAVa8cpmK67Fp0WZNNGXBHRGUIcv_wvKoHltLlj_l-yU4fHp4MJQSL0OVx1v6kNqjfoAi__bFgcffmOxa3c50-FZwsDz5OAxoB7ZWwKQ1FsD0M0P5GIvLSrYiG7DPFTD2iSM6nRKQIBYrUadcTnrnqZcfv7rvfFgqrVofL894GTqDVpeSuWHROrU2ECgp_as4gQODuYnAytlyWl2Y89RudNuTvOOdRnT5CCbukbJVVkWm8pTx-JpSf2OtgnQqgGQ73KjKmgh6I2p2PH2efJ-L0bGRgSZTBJxbKIkWJRV4tdtmxJY3btwklwA-6Qv3QerC85kqvTshKTVSPWmqYA1iYaxLo595KLcKUOXIlkPVABHy_d5gB2F67E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a2ec2172.mp4?token=F90l-MrXhCdcE6ujKNM42dq_JXvi2Vv8ngcSsxGvIUd_wHsCZnB3il32iWpVABw4bMuIv9QmY8pxpht_nX1RwCTn1uiCzrkxR0zvIAd-sSgF5ebs8RdJLovnU6ZxjDs-KEDp3iHDR55IVUTHnO55WClsapZPA-9flbcIaf5zACE2xVJCa1YM1-KRfDsRlv6rRNjYS8QsdLJXJlNsaBFqC1xaeniaJHo7IVe5DosEuLphl_bOQQBszk-Xrfvo36iZct2PVdECPs2JD1pJqvGi4DWT-b5_3QBi_quvyzy9xUhiXMsx2zLspAVa8cpmK67Fp0WZNNGXBHRGUIcv_wvKoHltLlj_l-yU4fHp4MJQSL0OVx1v6kNqjfoAi__bFgcffmOxa3c50-FZwsDz5OAxoB7ZWwKQ1FsD0M0P5GIvLSrYiG7DPFTD2iSM6nRKQIBYrUadcTnrnqZcfv7rvfFgqrVofL894GTqDVpeSuWHROrU2ECgp_as4gQODuYnAytlyWl2Y89RudNuTvOOdRnT5CCbukbJVVkWm8pTx-JpSf2OtgnQqgGQ73KjKmgh6I2p2PH2efJ-L0bGRgSZTBJxbKIkWJRV4tdtmxJY3btwklwA-6Qv3QerC85kqvTshKTVSPWmqYA1iYaxLo595KLcKUOXIlkPVABHy_d5gB2F67E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بروجردی، عضو کمیسیون امنیت ملی: دیروز پس از آنکه دو شناور هدف قرار گرفته شدند، نیروی دریایی بلافاصله پاسخ داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/654244" target="_blank">📅 22:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tb5pToQyHAYpjfcOIw-4YbcOeTJUAQOI4emO5nZqhHoguBK0tw8Q98abYyobAtS-2mN0O_SIkJsrqKP3VZ4A-eBEIdOcMr-6-tafjJqln1rD8liYTvMYgoeKD0fJ3O_NG8SZqI_J973TZCXebVaInkbbU3n33fPa0_mg3qCHBMpHODSvA_NF-Hb5HfDiDPMB6zPE95AhdiLZac25wT02wG3IhamVp9MaSx-nxiUIlcgB1eG9AXb6qIGMHlIe5GxZTFIfXb8izvejwOAo0xqrpNZ2o4JzaVQYDg967k6RrscmqFLaxjOC4ky1TA5bnMbntlDWBE9QH4dmKPHWoG9t0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPgWOG1enwfM42KF-RmOMZ0W-O887X6URl4TfRffCtciB83b5QGvbci4vmu5cdZ0rtXuVRIc9PIgRQKC3iluQFNe4mCucI-xtr92X18sMbNXZxYuk2k4Zxfpv0CCt0nQkZe2_ZfDBae5SmN7nmTdBrKVH8UeMQZmAVdD8fxTOp4izSw8L01Sa8w8iIavv98ZEkvxPbdAkEC30fHRPJIssl-u9djLFmtYj9nf4wI7azojdLgDm3TElWTKeVV7_ptN5oeCcRQxTcRZQdZNL0uogIdPSqz3Er5I5lRo3b5WwU9jW7VHrt2bhaH2MOGRnbT7FzxmyTuHzDmygbUIzyA6qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXXUkkhAUnLqdMwkob1ehKO8ruAY02RfxZoH7exCLhB-QBIJ40jyOl8hGSBAxAB63fg6X5_cIYa1RqS870t_3t0-f51OMCZMxfwJsMWmNARF8e63n22ZbooCGSfyk4XkDZZHu4RXzmQjJwvOVgJeOpFrzF27YeCsyv2ngsmpQ-5CQl0rNLKucBw3FPqFkDLz5ILGU-UtN56JfvwpA7DSelwd5foFDJNdIrhMIdRgeTkjZFCW3r8V9ev7u1fFBteuURQGl7PKGnQ4jb2hcCrU7pIxJ9GtfWDv_AsFfmn9FGclySqe7bl29N69BEn2qsWIVJF-ZptGS0UMB9hvoOoleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n0w28EJj0G3WYCU0Lx5LJfFtfCS4oj-7Il8xZ-KCergUtTJ_eu_IoOE_O_VIxkppZGK9TTGsENgNa6BjcK6303_-2hbEhezVDoeiL2G32JnTLMkGmMhDEYfVARcq1kHPP4thIZgv5xIW3966kfDSmuUwrPuq2O0o1mI3DZz3V3OJU4cgcWPgzWOoo5tdreSKrIFUuQsoeA1q56_GhUwisXT5gOMB69lS6XtPhZCxURCe6HCoZc1YI_SqaeTFHKFKQ3X9GIrpcDvaDYj0g78W9iTP_skPMqvtRGhAfrBlAvmI-SD4CE07sBrym0tlWZ8z6A3mRw9YR8bep53n7MHnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PY1JJfT2ZT0VVHgyTffIpxx9nRuHQEKFEs_qVedxLSvZtzDPTjbVqTUT0OpQWLmTALB8NXC4p0AIJEqq2cOvSHNRs7TTgbv460OwkM_Hvda94AHfAgQCD8D2-lr46i4-kb59rmZxaQFKltO3DvT5Qu67Qc3ePUQym1lqd4Y_rK2ssYnn90gzzVt1SKmpCqTNmZBXMhW1vsY1-3gAzYQiZgp10pLwBUQL53AZmlXMG63a0Da2-Z_wTQZDkvW3fEYeAJ7XRpMifAnrnp5U3Bx1U9IC6-3oVks2absMnBmic3udoR_Ae-9QpJoib4ZLOP04GUulwonjB4OplAQDkh95hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CnR818ibDXJk4nSGNrJ_9H0UnzyJ9o6Vf_p3QReqj-V3m4WmqLklkhdVdmV9ScmYcT6ViJWxvEptN-UgQ4WEymu9ifYpedm976PCdIsP7v-0dX8pQdoqKAXZqK02ySxgEFnFc0jClKW-tXQf8asoTtsHDJ8hjg-fulXZ0NQrs6pXXv99zetwGIlPtqXxkAOc8GfFmIOH33resFQBQMcJ0dKcL6rdaFyxbXztjGMtPL8dnItLrh4VyVb5UW2P55ywdPHt_-N8JFaG7Dwmk-BLW4t3P4sUXD8dmq29q38xC-3BQxB_g0wvuc9HU06yVl6a33DpImWOl3E4nZ7IZ8DKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-h_1RlaQ6Go8zSb36JmYzkMygh7p6KSgaL4DjFYRnlkunNHEaRGgReok1rqQaVmsPsrOq6hNa0zvx9cP821-hl-S8pky5BXgHmZZteEzpz5iA9NN5hmVRpqLLmt-mCcBJw_SJtDkLC7_C4mdO6_qSPAy7lqmV-41rzdCKcO7_zxisDmJstvNYMYF8hPR42pR3mOac3sCjzWG7pH3iSyoDv2zSD7xtvf5fF0acx7wPZi6hWoxbZ503FcumVRN0fGii4QmXBy3zwJCogxbfbhFHmFZPwIjakg1IGM3X86m-rVL0fREGHpAMsoe_ypWXZkP0veUM8YGzk6BiQzK-69Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoOuYceBBYEfRhYzokkCqihBvjkzqUxN1-dc6_AZqKYzELBdm9lyukyBa_SlNZwv68NBjECpoLSH42cUyMUDJNufveHKLQRRbHw_7H3JytScTicOZxMuu5fYSdb4RuaVjYNPr9IsV6xeX9oGuRuMW2Q9OPrK1v9V9yoMElBZT3JgE1_3hASqxaO3HyhHEe-eWEPOgNMGf6DoIV6OWOqGuNN_wF10YgSmDvka3_OAzJUh5KKs5hs5k6W-zBe-oU3ColCJxdtRs77YSXhOayuT4OAsUDvo1jY9UsrsIZdl_PJdVbzrPh6HTyTeOJTQ7S_ouE_9FmfQXqpyI88I34Xz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YorCwZ2ER6RuFemKw5cz-qV4z4FOQyhcBPjGJPIWsYbVD-09Q4YvZfTN59HWZgKu79awHrlvRR3claQ4M2_Ec5irNEaK32MeHdJuWL3yoY5_PIZotAsfth0xY8qHuV4DSvXth5DUDllvUmN3UVxY6VngBrJBQlBk9kZLKmj-iFGJIaTl7Ok1wSlDKI68oLb56jwK2k3Ne7g-2gR_FAz3UQXbrthmIxpoxTLu2v5CXK8J9qmGQG22zqg2OgogrQHoWIGwV6sPF8S-vVhZ7jgZZnnKhnCAWnqo0dFL-5FHjUF0rxLfS9PzMSySqyomG7QUW-SL3NoFRK8MW5zz2QTXuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-I4iXKmGoKzNW6-n5LLPGf-YlfIQ_y2e6O-p0QuEXRnjlkmSH9x6BbkCxX4UsJk1_YO0Rily_6nc8lgdXUq2sjWqzn5xcD1aRB2nNyniwYvOC9bId-hD5AkQ1x8leJCrHtxRdTsy0DGOphqeP5qosTim6_GZyUptwoucjv3LECSfvWAoVLAvP_7Agx8wogbzcccSk4OyHdVTFgB5q-68OQMyslR88de4KE4J8J7C5F5oecg6zxSe9eSQ0_EsKMGNmJrLJOXGA99uqkOFjtRQJsDlWx4mHxuReH2msyRZnxSw-OT__J9ZGMWpVNaSVGJI0IerN9-viiSOf0BVxdytA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/654234" target="_blank">📅 22:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62aae35680.mp4?token=MUqWxJTirFW3egS05RAVye4ITAVnhdFaHm-MTIv6NgvRwCU9Glmvooo1SduvfnYtFbsZBGYRrATg15T8f77SNTf4NhVJq2EcZZ56C19GIcFZ2sjqN3a45Fla3jQXScNCD2Tkdsk26IBK61eJ_kQZ6-BPjpQ4dJpS5p5aS8Ii6Od8agwS2dEWbU1nhFoRtTXS-Q0-y8ug130eA0ERnjCEVfDdZtlQkib0roAxZZKuJv0Ou2Og29sVLenIKNmSnG9OC3IzvnbpSs64vdKURzK2phvBhjJmaWqX7wZnAytxJRvcpSxPUaxMywyDJwACPFtnEKywdLQBpPneRLlqoIEZyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62aae35680.mp4?token=MUqWxJTirFW3egS05RAVye4ITAVnhdFaHm-MTIv6NgvRwCU9Glmvooo1SduvfnYtFbsZBGYRrATg15T8f77SNTf4NhVJq2EcZZ56C19GIcFZ2sjqN3a45Fla3jQXScNCD2Tkdsk26IBK61eJ_kQZ6-BPjpQ4dJpS5p5aS8Ii6Od8agwS2dEWbU1nhFoRtTXS-Q0-y8ug130eA0ERnjCEVfDdZtlQkib0roAxZZKuJv0Ou2Og29sVLenIKNmSnG9OC3IzvnbpSs64vdKURzK2phvBhjJmaWqX7wZnAytxJRvcpSxPUaxMywyDJwACPFtnEKywdLQBpPneRLlqoIEZyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انهدام دوباره یک جنگنده F۳۵ توسط سپاه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/654233" target="_blank">📅 22:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe615e247e.mp4?token=FO8qpZE7xh5DXi07FZW_ySqZyRjseA6GCg_0n_VIecO-fjk0e8v6wYJHCAaex9Uc5_6yGq3Sd1i9VkuJhntUvpXSfMupK9tSlXdCsr9yS3Bv5XQpVuOQjVGct43ERZ2yUBFHE2nJwQe4FxhgDv9SBSrhhg49JEEaD0Aswk8lXsyO8u9ikefphZN7-iClf-9zTRUirL8xxtbM9WRaynS_PsARcuENtPrmYpHePqT4uqBat0QTzg-wA2TUexZ0lGGv6vwCRYwgqG7I9hAesTxsmcBzXGkzwNihvFhoFErhzj9LPyLjBqWTfru5MpsSiIFuq4q5FAXvDE4fg8xn9x6jog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe615e247e.mp4?token=FO8qpZE7xh5DXi07FZW_ySqZyRjseA6GCg_0n_VIecO-fjk0e8v6wYJHCAaex9Uc5_6yGq3Sd1i9VkuJhntUvpXSfMupK9tSlXdCsr9yS3Bv5XQpVuOQjVGct43ERZ2yUBFHE2nJwQe4FxhgDv9SBSrhhg49JEEaD0Aswk8lXsyO8u9ikefphZN7-iClf-9zTRUirL8xxtbM9WRaynS_PsARcuENtPrmYpHePqT4uqBat0QTzg-wA2TUexZ0lGGv6vwCRYwgqG7I9hAesTxsmcBzXGkzwNihvFhoFErhzj9LPyLjBqWTfru5MpsSiIFuq4q5FAXvDE4fg8xn9x6jog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش موشک امریکایی با چند هزار ترکش روی مردم ایران
🔹
روایت یک مستند ساز از جنایت آمریکا در لامرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/654232" target="_blank">📅 22:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec933080a.mp4?token=qS2yvADx2t_LRztPJMPZUuMg77X-J1lVRl_H8sgG7oFwuObnzDYZekcN8tuaDgv7LfaRbR70Mh4TzEaZxS2cKhRyQZAYxip9Ha0p2nq5xbMF4YJ076jUd0Q4cnJIphY4zhNnC_6utv8pQDQ7Uq1oczBUmwyuHp_DzpyHlVNNkgS42VROe_mbDWA-k8URPJtVqezt17Pq3RaYhRVUXiZH-fVuoMUpu352GtW-MqkxTv3atGg-vN3DXQJNgCpURUlXQVSjKpOqKP04XIhFoHud7vov-qZG6H0cTULR9-_-PbQhWOGWPeFZWhIDCRRBYcSP30LBZso38QGDIfYm3f3Up1qfEiqRXKGAE4aaRxA_GVw6ZT08c_bimzPJHS-Xnq7SpPQCSb_sZRv8QtdyXEJnRa667HhysogmAstqeHfvePlDHVQflzFo8C0O0EtEsRqDtYuQNA_7QsvSGYX-xY8UsIbOqNH6WLrC0dYOy87FHcidPuUR9Ey-jrEuPFrI2J0gxjaLIbh47fnJ3JNRC5J5kOkY-mrOz5zD7jPe_RFz_brVVxlKMVYEJ9UQ6_2alWlaIuPcto33QPwlyrytkl0JMjcs5FoAUY-RqsZ7blTuEiKvstGB09veeI0r3P4w1OELFtWhfbUTFgbFYyzReOAkGCXU6OeiqcQluCVsWPmZ_MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec933080a.mp4?token=qS2yvADx2t_LRztPJMPZUuMg77X-J1lVRl_H8sgG7oFwuObnzDYZekcN8tuaDgv7LfaRbR70Mh4TzEaZxS2cKhRyQZAYxip9Ha0p2nq5xbMF4YJ076jUd0Q4cnJIphY4zhNnC_6utv8pQDQ7Uq1oczBUmwyuHp_DzpyHlVNNkgS42VROe_mbDWA-k8URPJtVqezt17Pq3RaYhRVUXiZH-fVuoMUpu352GtW-MqkxTv3atGg-vN3DXQJNgCpURUlXQVSjKpOqKP04XIhFoHud7vov-qZG6H0cTULR9-_-PbQhWOGWPeFZWhIDCRRBYcSP30LBZso38QGDIfYm3f3Up1qfEiqRXKGAE4aaRxA_GVw6ZT08c_bimzPJHS-Xnq7SpPQCSb_sZRv8QtdyXEJnRa667HhysogmAstqeHfvePlDHVQflzFo8C0O0EtEsRqDtYuQNA_7QsvSGYX-xY8UsIbOqNH6WLrC0dYOy87FHcidPuUR9Ey-jrEuPFrI2J0gxjaLIbh47fnJ3JNRC5J5kOkY-mrOz5zD7jPe_RFz_brVVxlKMVYEJ9UQ6_2alWlaIuPcto33QPwlyrytkl0JMjcs5FoAUY-RqsZ7blTuEiKvstGB09veeI0r3P4w1OELFtWhfbUTFgbFYyzReOAkGCXU6OeiqcQluCVsWPmZ_MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاحی که هیمنه دو ارتش متجاوز را در هم کوبید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/654231" target="_blank">📅 22:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm-ItYRQ-Mci_yJTdr0XryMOBbjipmek6U6XeIdb84xDa3ttyO9Gv5IjOEcHxK-5qtLc-f6V9MN6pzh-PREURf_bvZU38fasxKPO6czcgsH32zMDMnIBvsdvtAZb2FFenwr5Jy2SmVC8nE6hTU1blu1GnPwombRARrdBFX3Wfr6ysK7oVpUWXDO9SUD9hYHuL1HVapxebREB-t_3Bwx2mO17pMQVRJxWFOsL4gj-K9HYJIf1wayDJ3CKVyf0Pj_1E0UQfCLlmYr7En8R1a1RhSia_srpD8R7-uF8i9FRFMGyYhQw2F9V8B7_ROAl0o3mHtOLnSWFGEUFQZVxmrhgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم یادبود شهدای خانواده امام شهید و رهبر معظم انقلاب اسلامی
▪️
شهيد زهرا حدادعادل
▪️
شهيد سیده‌بشری حسینی خامنه‌ای
▪️
شهید مصباح‌الهدی باقری
▪️
شهيد زهرا محمدی گلپایگانی
🗓
پنجشنبه و جمعه، هفتم و هشتم خردادماه
🕓
ساعت ۱۶ الی ۱۸
📍
مصلی حرم مطهر حضرت عبدالعظیم حسنی علیه‌السلام
از طرف خانواده‌ رهبر معظم انقلاب اسلامی
@Akhbarefori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/654230" target="_blank">📅 22:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUOU7VPuorz2Odvvf_vLcoTSWDhlpkblv-GPsAijxDeZfAHqskMzU_qvNJjzldtCXk62Xvg1mlcunXPBpFD4TwEDM08vdDK2r0ginHkr-Ci7Y-f_XyRZs3A8oXVuLG8kPLD2r4-DAJJZBLJrhga7NmAutxEDKsFBfJdMEHUOiN88tn26XSIY2AX_qeH_LRZWMCLPei1ZjlLNNgZ3iLMA1kfgWOqseskZe0DPaaqyaGCbUVbPlz9Kpx-S47TTUU9yWL7e1QCsBHQLWkJ_5qARlkBgoQDBGrEndTEKRHk2ob92Zw9_RWdcOlCwVdhEiG6V7QUi5i47OxeC_IWeJxEMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مخالفان رایگان‌شدن مترو، تهران را معطل «سلیقه شخصی» خود کرده‌اند؟
🔹
افشاگری صادقی از پشت‌پرده مخالفت‌ها با رایگان شدن مترو/ برخی اعضای شورا حتی چشم دیدن رایگان بودن دو هفته‌ای مترو را هم ندارند!
احمد صادقی با افشاگری از ناکامی طرح دوفوریتی «سروری» برای تداوم رایگان‌بودن مترو، از سلیقه‌گرایی در شورا گفت و بیان کرد:
🔹
در حالی که این طرح می‌توانست به کاهش ناترازی سوخت و آلودگی هوا کمک کند، برخی اعضا حتی حاضر نشدند با امضای خود، مسیر استمرار دو هفته ای رایگان‌بودن مترو را هموار کنند و شهر را معطل ملاحظات شخصی خود کردند.
🔹
احمد صادقی، رئیس کمیته شفافیت و عضو شورای اسلامی شهر تهران، با اشاره به پیشنهاد «دو فوریت» برای تداوم رایگان‌بودن مترو تا زمان بررسی و تصویب طرح نهایی بلیت رایگان که از سوی پرویز سروری، نایب رییس شورای شهر تهران مطرح شد، گفت: برای مطرح شدن یک طرح با قید دو فوریت در صحن شورا، امضای دو سوم اعضا لازم است. در این مورد ۱۰ نفر از اعضا طرح را امضا کرده بودند اما برای رسیدن به حد نصاب، دست‌کم به امضای ۴ عضو دیگر نیاز بود که این اتفاق نیفتاد و طرح به مرحله طرح در صحن نرسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/654229" target="_blank">📅 22:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a26889fb7.mp4?token=Gsssbxem07l7x09Q1_ni8sej3270A14A3uVhayObyDQHpSerMPVxKCEjhD18ZbspncNYrP_Ymoy4OVtvWny_WMBYxeidg5DgDeL867QM9FYrtEEPcrpDhqLKF3EvrPw06fdjsTctagyw3O-CEcoHTbBqb-aJG2yUlecR8nparKPVhbzyCPAcFMYfO3US_rlQaDzYjhZoY6tFPr-JxkIzIk3ppUv4IgH335ScshfMoo1aCHOGuJBqTDxADRo-Iv9oYWEYSYbJPFFuMDt9_hRJ9pxPUUIX_9_93saJB3v3NBH_RrizPAviqYycUH9p6YXt_UXocsS4MdW-wbRJS5n9CTug3PyZWBrS3y-QKl_TpQalIe2g2yUMgePkaqSRp36MBjo4A4WCoOqZOl8FthAZMzlW8jQcj4ukNtg-ezsIi-Ul5vwZajR5hlI0YPvMFaQEEFTIydvc6rvq6Q2RRUyLlEtwRLGV0BLzPApfCjtgSKW4HdTpHCIBshw_y_gaGG-drHvYhCTbqTxARMvTmvJmLI4bFAqoZbgs5iHdgIgIgCEn9qcU-ouQWbMxGx43LwTC_WqSpH7XcIJ2LJuN2KHatFDCNHy3foA9T2mTPLedj1WgF-K33O6sUhgdOr5-jVpwlO1TFug35O7DUpVJRaw3VUu9KwwltQZm2cK6GIdJQp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a26889fb7.mp4?token=Gsssbxem07l7x09Q1_ni8sej3270A14A3uVhayObyDQHpSerMPVxKCEjhD18ZbspncNYrP_Ymoy4OVtvWny_WMBYxeidg5DgDeL867QM9FYrtEEPcrpDhqLKF3EvrPw06fdjsTctagyw3O-CEcoHTbBqb-aJG2yUlecR8nparKPVhbzyCPAcFMYfO3US_rlQaDzYjhZoY6tFPr-JxkIzIk3ppUv4IgH335ScshfMoo1aCHOGuJBqTDxADRo-Iv9oYWEYSYbJPFFuMDt9_hRJ9pxPUUIX_9_93saJB3v3NBH_RrizPAviqYycUH9p6YXt_UXocsS4MdW-wbRJS5n9CTug3PyZWBrS3y-QKl_TpQalIe2g2yUMgePkaqSRp36MBjo4A4WCoOqZOl8FthAZMzlW8jQcj4ukNtg-ezsIi-Ul5vwZajR5hlI0YPvMFaQEEFTIydvc6rvq6Q2RRUyLlEtwRLGV0BLzPApfCjtgSKW4HdTpHCIBshw_y_gaGG-drHvYhCTbqTxARMvTmvJmLI4bFAqoZbgs5iHdgIgIgCEn9qcU-ouQWbMxGx43LwTC_WqSpH7XcIJ2LJuN2KHatFDCNHy3foA9T2mTPLedj1WgF-K33O6sUhgdOr5-jVpwlO1TFug35O7DUpVJRaw3VUu9KwwltQZm2cK6GIdJQp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوار بهداشتی شدیدا گران شده؛ چرا کسی حرفی نمی‌زند؟!
🔹
۱۵ تا ۴۹ سالگی. جمعیتی سه برابر نوزادان کشور؛ اما وقتی حرف از گرانی می‌شود، اسمی از نوار بهداشتی نیست. هر ماه حداقل ۲۶۰ هزار تومان فقط برای یک نیاز طبیعی، نه برای تفریح، نه برای تجمل، برای نوار بهداشتی.
🔹
چیزی که هیچ‌کس درباره‌اش حرف نمی‌زند، دارد جیب میلیون‌ها زن را خالی می‌کند. تورم پنهانِ قاعدگی را در ویدیو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654228" target="_blank">📅 22:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedf16d37d.mp4?token=l7-EH-R0ZgytlexKw8fxtLNJjorBha2dz5iJYNoYta1zzDF6u8k1EYvzXz9ZjTkVwCEE9BRLlEF6NHuQ_Mmdq_yRLFJcTnwwThRqoaLoZTKDd26I8GC-WVm6h5gcC39V9I91nwb58cY2coW9bnvcE5Elpn4V5vhI3wwkH4tl-Uuja32QNQQP8MxZdUmfmK2nKho9CzWzYPm5Y0wH8ebrl9vtjE2Hn6nbON8CWZr65LNVzu2Nq6Abl9bfF8Ja3ZNsLTWhqT95xjomKH8b5bv89mm77cSU88h3QYucCIn5MFpYfKUDqPVPQXYzViWQQpOJe-b0c8I06gJOs4JLoj0vxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedf16d37d.mp4?token=l7-EH-R0ZgytlexKw8fxtLNJjorBha2dz5iJYNoYta1zzDF6u8k1EYvzXz9ZjTkVwCEE9BRLlEF6NHuQ_Mmdq_yRLFJcTnwwThRqoaLoZTKDd26I8GC-WVm6h5gcC39V9I91nwb58cY2coW9bnvcE5Elpn4V5vhI3wwkH4tl-Uuja32QNQQP8MxZdUmfmK2nKho9CzWzYPm5Y0wH8ebrl9vtjE2Hn6nbON8CWZr65LNVzu2Nq6Abl9bfF8Ja3ZNsLTWhqT95xjomKH8b5bv89mm77cSU88h3QYucCIn5MFpYfKUDqPVPQXYzViWQQpOJe-b0c8I06gJOs4JLoj0vxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام پرنده بدون سرنشین MQ۹
🔹
انهدام پرنده بدون سرنشین MQ۹ دشمن متجاوز آمریکایی هنگام نقض حریم هوایی کشور در منطقه خلیج فارس در بامداد امروز مورخ ۴ خرداد ماه ۱۴۰۵ توسط سامانه نوین پدافندی هوایی نیروی هوافضای سپاه پاسداران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/654227" target="_blank">📅 22:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای رژیم صهیونیستی در ترور فرمانده جدید قسام
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی در بیانیه مشترکی مدعی شدند که ارتش این رژیم «محمد عوده»، فرمانده جدید گردان‌های قسام، شاخه نظامی حماس را در غزه هدف گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/654226" target="_blank">📅 22:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmRSuEmKQU2bTaIfwBlU1rXNa1EHypBFNtU0S-LZ4QFHGKTlob4xAtz0fRo_Nrw2g8fIdfUoYpswuvgwLH5ZcP6t6dkV75jbNqBONkxLO1_PjMj43fJgOB3Zf1Qk23-hRm_aZHOWfr8VI49RdNUzxOru7kjV7xf9KcKfFMfs3y71_e8HNvHBlFVYhlil8F8jBLOVNtDrzRXJPqjequD7p6TaGUGO-_K1RcOHzAtk4GFFfF_sG5REQnXC4m7WJV8rpJVTo3K3cNzKvMvLCdJszmuLD_hq4AIa2uMrt3NNJoJjFRgIy_C_ushdCHB51-PgPypcqIThxPMh-pplokjx_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هآرتص: اسرائیل از زمان آغاز «آتش‌بس» در غزه ۸۹۰ فلسطینی را کشته است
🔹
از زمان آغاز آتش‌بس در اکتبر، ۸۹۰ نفر از ساکنان غزه بر اثر شلیک نیروهای اسرائیلی کشته شده‌اند. ۴۲ نفر از این قربانیان، نیروهای پلیس محلی بودند که وظیفه‌ حفظ نظم و امنیت را بر عهده دارند.
🔹
شرایط طاقت‌فرسای کمپ‌های آوارگان، تراکم جمعیت شدید، فقر، گرسنگی و بمباران‌های مداوم هوایی، دریایی و زمینی اسرائیل، زمینه‌ساز بروز تنش‌ها و نزاع‌های خونین در غزه شده است.
🔹
با وجود این وضعیت بحرانی، حماس با نیروهای پلیس خود برای برقراری نظم و رسیدگی به جرایم تلاش می‌کند. با این حال، هر یک از این مأموران که در بازارهای محلی یا مراکز توزیع غذا گشت‌زنی می‌کنند، جان خود را به خطر می‌اندازند؛ چرا که ارتش اسرائیل مأموران پلیس را که نقشی حیاتی در کاهش رنج مردم دارند، به عنوان هدف نظامی تلقی می‌کند.
🔹
علاوه بر مأموران پلیس، غیرنظامیان از جمله چوپانان، رانندگان کامیون و کودکان نیز در حملات روزهای اخیر جان خود را از دست داده‌اند. از جمله در بمباران اردوگاه النصیرات، یک مرد ۳۸ ساله به همراه همسر و نوزاد یک‌ساله‌شان کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/654225" target="_blank">📅 22:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260f53d553.mp4?token=STh0BqYp1Nvef03w8lyjC7GO_UnMS0q1ooVg24uqFi4p82-eWopleLVcCzWpW9MT9rQER2kClbDr_Is0uTaXCxLn6FiymSRhO-gZ8e_OgsHWIfC_Mfn4X2jxiOmZB4Y0Vs9-w7PU4SoQ8KtE0yhLsmbr6DLOPYQFJmAND4Pn6p9jSS3rTJy3zOLyYpD_oQMpBkruuFhsvuHZ03fJpdj2dHryezlGm3HZoqh7PGtmbK7ny2Z_3oOLUEYJ_vTy-rr4qPwn54ncnna3VpAw-Y6jN-GWpFcFVWYc0Zs35oU7WwfQcl5b1p8LS1LgSROKdGXIZvPyWNikspmgddlxZiCpnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260f53d553.mp4?token=STh0BqYp1Nvef03w8lyjC7GO_UnMS0q1ooVg24uqFi4p82-eWopleLVcCzWpW9MT9rQER2kClbDr_Is0uTaXCxLn6FiymSRhO-gZ8e_OgsHWIfC_Mfn4X2jxiOmZB4Y0Vs9-w7PU4SoQ8KtE0yhLsmbr6DLOPYQFJmAND4Pn6p9jSS3rTJy3zOLyYpD_oQMpBkruuFhsvuHZ03fJpdj2dHryezlGm3HZoqh7PGtmbK7ny2Z_3oOLUEYJ_vTy-rr4qPwn54ncnna3VpAw-Y6jN-GWpFcFVWYc0Zs35oU7WwfQcl5b1p8LS1LgSROKdGXIZvPyWNikspmgddlxZiCpnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعدام خانی‌شکراب جاسوس چندجانبه و عامل ترور ناکام خاخام یهودی
🔹
غلامرضا خانی‌شکراب به جرم همکاری اطلاعاتی و جاسوسی به نفع رژیم صهیونیستی، پس از تأیید حکم در دیوان عالی کشور و طی روال قانونی، به دار مجازات آویخته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/654224" target="_blank">📅 22:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b79410cb18.mp4?token=uKXRcc4bOliHpoaD1pQsg9f4pWu3D-zOZLpIyRSVF8khPv-2MDIG0EG3gPSGVQ_-xEOrmThWsdr8N7Qkc7dCLlBvEkJ4xkJUVPkhI_oGVoKnAl71G-PMZ6SXTnRHZgfKvGKVH81jS5__4tfea9p7ZfQsctgCFd8USwp6L0svccyVPsxVgYDPiWe5lzf1ih3-ooZO4fcrH7YaPc4SSt6ZpVyrDNcQzoX6dnVmu828OSoDFFUTnrXZ8P9yE7axOMCiMldXUDbJsjZS6bfisI9RmhiW_a8wxV1T_CXWhOCynnBG5DXEwvFlhkvjBoPBNJJjvAfAAMxwsmOhqlaiioCwuHqkvLEhsNQ0CSmK2LD9YePK58-JQfuEqQ7DvgsBuDbKOjVNrTrWVWl-V2YlRQv8p7qOiRQ4oWWUQoWC9ilF-iZg6KHV0rNqV1mNXQcHENkgQxsKsFD8TlN8L-jpwkKQECapfg8N5jKhldn2z24mrJ2Yrj3XFBgM8PzHRVmUa8AzfN02-mtSSbl_CCGQ4iqddEA7229RG1_WSlR8a2JH5ZHGvOEgyhatUYh19RgSXQiPL5lF3u8QfU5pSwhdawCgON7C2RXkdoFW33Cdro7AW5d6JCC3i2ENreobdH-36QRnIqBCvWgelCdbRIaCWV4vQ7KjIACyYfHiSk-J-21M3oI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b79410cb18.mp4?token=uKXRcc4bOliHpoaD1pQsg9f4pWu3D-zOZLpIyRSVF8khPv-2MDIG0EG3gPSGVQ_-xEOrmThWsdr8N7Qkc7dCLlBvEkJ4xkJUVPkhI_oGVoKnAl71G-PMZ6SXTnRHZgfKvGKVH81jS5__4tfea9p7ZfQsctgCFd8USwp6L0svccyVPsxVgYDPiWe5lzf1ih3-ooZO4fcrH7YaPc4SSt6ZpVyrDNcQzoX6dnVmu828OSoDFFUTnrXZ8P9yE7axOMCiMldXUDbJsjZS6bfisI9RmhiW_a8wxV1T_CXWhOCynnBG5DXEwvFlhkvjBoPBNJJjvAfAAMxwsmOhqlaiioCwuHqkvLEhsNQ0CSmK2LD9YePK58-JQfuEqQ7DvgsBuDbKOjVNrTrWVWl-V2YlRQv8p7qOiRQ4oWWUQoWC9ilF-iZg6KHV0rNqV1mNXQcHENkgQxsKsFD8TlN8L-jpwkKQECapfg8N5jKhldn2z24mrJ2Yrj3XFBgM8PzHRVmUa8AzfN02-mtSSbl_CCGQ4iqddEA7229RG1_WSlR8a2JH5ZHGvOEgyhatUYh19RgSXQiPL5lF3u8QfU5pSwhdawCgON7C2RXkdoFW33Cdro7AW5d6JCC3i2ENreobdH-36QRnIqBCvWgelCdbRIaCWV4vQ7KjIACyYfHiSk-J-21M3oI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زمان به عقب بازنمی گردد و آمریکا دیگر نقطه امنی در منطقه نخواهد داست
🔹
اخبار تحلیلی ۵ خرداد، ۸۸ روز از آغاز جنگ تحمیلی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/654223" target="_blank">📅 21:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654221">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
عبور ۲۵ فروند کشتی از تنگه هرمز با هماهنگی نیروی دریایی سپاه
🔹
طی شبانه روز گذشته ۲۵ فروند کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🔹
کنترل هوشمند تنگه هرمز با اقتدار در حال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/654221" target="_blank">📅 21:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654220">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e1e88e8.mp4?token=vb2lsVJoBM5BqgFc-tvb2fsFlFbld0JXqTZsQ-M7tbTBTq2xiiYXQ6JEcvK9IYuu4SpICp_ZF7r09N4EzTt9r3AGciIoqwFEpAJXn5AQr5f9i4FVJjOoOifZXmFgkjQKiatBzdVUyVa-Y2yPsZJjhFJpgDSZcWZ1tZRbC_L6Ll7aNgoZBBgvQzmz49wmmnbiEq6X7Qc0W47rxGv04ODl4U40QpQWWkW_iL5Iwfs3ZQf9N8qE2dufw59LMhtr_9z9Rb3XEwKRP40Bo4VX1tj0qwede7bDmSp5Ev8St4jh6MvtmWTN7Sp3F6iEUnyVwZ04JivWbbla3Nh-VnRxNgFDPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e1e88e8.mp4?token=vb2lsVJoBM5BqgFc-tvb2fsFlFbld0JXqTZsQ-M7tbTBTq2xiiYXQ6JEcvK9IYuu4SpICp_ZF7r09N4EzTt9r3AGciIoqwFEpAJXn5AQr5f9i4FVJjOoOifZXmFgkjQKiatBzdVUyVa-Y2yPsZJjhFJpgDSZcWZ1tZRbC_L6Ll7aNgoZBBgvQzmz49wmmnbiEq6X7Qc0W47rxGv04ODl4U40QpQWWkW_iL5Iwfs3ZQf9N8qE2dufw59LMhtr_9z9Rb3XEwKRP40Bo4VX1tj0qwede7bDmSp5Ev8St4jh6MvtmWTN7Sp3F6iEUnyVwZ04JivWbbla3Nh-VnRxNgFDPjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزشمار اخراج نظامیان آمریکا از غرب آسیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/654220" target="_blank">📅 21:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654219">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
کیفرخواست ۲ مدیر شهری در خوزستان به اتهام فساد مالی صادر شد
🔹
دادستان مرکز استان خوزستان: اتهامات این دو مدیر شهری شامل ارتشاء، تحصیل مال از طریق نامشروع، پولشویی، رشوه و اختلاس بوده که این جرائم انتسابی به آنان به اثبات رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/654219" target="_blank">📅 21:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654218">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شورای عالی مسکن، سقف تسهیلات مسکن ملی را از ۶۵۰ میلیون به ۸۵۰ میلیون تومان افزایش داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/654218" target="_blank">📅 21:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654217">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دام زنده ۱۰ درصد گران شد
مقدسی، رئیس هیئت مدیره انجمن گاوداران ایران در ‎
#گفتگو
با خبرفوری:
🔹
با تدابیر صورت گرفته، در دوران جنگ و پساجنگ در تامین نهاده‌ها، شیر و گوشت مشکل خاصی نداشتیم. مشکلاتی بوده اما نه آن‌قدر که به تولید ضربه بزند. درحال حاضر نهاده‌های دامی در ثبات است.
🔹
جنگ همزمان با تغییر قیمت‌ها در سال نو بود و افزایش قیمت داشتیم. شیرخام حدود ۲۹ درصد و در دام زنده ۱۰ درصد افزایش قیمت داشته است. جدا از مبحث جنگ، بخشی از این افزایش قیمت‌ها به دلیل تحریم‌ها است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/654217" target="_blank">📅 21:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654210">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2mSr7k_nnybTmvcedI-SDDwId4W-QYHt3SGV4sXeHWbt9KtVwY80wLTZhQa0enA_oEsGcSHTGdGDXSpRoDqca2hzCjkXYDuqhf2-wdr-1ujZom53fP440I4nZFPHJHWVZLjbQok0hIFrTOBIZubj0lPJ5YYCIgimdNBxR1Qj4fA5G9yO_Cd7KqmacuYuLxw_XcbQTU-i48OLHZOVmKMKaCIFOhJVkKLRE7AK-JpQAtU_2f27CftRs2eUkCu-iSsEBED8NIQOBnWEQQk0JqOkNpBE2lc4SEmD9sJjcDDxOvFg3jsGUTQ7rhCC42SmAEnaep-8itDGPZ1Fj40GQcWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ma0w8qSsQ3kbHOIkgJjkOANqjVAUPiIgNMtmMuTBRziNAnh7W9fk8rsH15cOyueZp_b3H8Z3OBRnZsbk95lL775INX-hJzPZq5lacPDeNWR0xJ_vlb5h7gW9tWGo3qsletYPyCkDbXdOhfRVzS_lML4FnzflzVnhTTm7dl3zs3zoVd6zMsIpHsbIpAGMRiMoD-bbeZJ8xdvClM6OJ2rt0EUe4rJmfLIU0mg4eIx4cf_GTfsm3GqU-B1pjzSTlzmHV5weMp0z2-LmBEvhiZjSsu3p1RoQYojihSX0WbooI5ndCeFF1oKJZPaoBJc_uWGDfKnoxxJ9vZIn-GwgDWuoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mA736NZ2kK1YIoy_Isq7Wp6jyHN9wct5UBfZUjoBsJlwdSsz7IuyqPgggB5ISoqmhozYXilnaZe5DoPH2Cz16lwAITezMkis6metrlTASuPsYqEtw4IJ91PRR2KkPqB-qQ1Q47Ge7oXhDTLrnNr-cxABoOi--LdSDVAUqGjhtEqlnXk98Q44emaNYuIRu5-fUcRVJ4_0tw0heW5UW_zxxe6p5i1BGFm3L412z1EvgmQRnkcw7rzJRNGOEkdK4DpF_G2Dl7vMmiG83Um0RZZhbu3RijK9yeATKbfddYyI_UmtYDbWtWDhLGY5vGIMW3zkKL7UFDdg33FHpb1lejhT2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3fQiS3Q7M_M2eMEGyZUsQ_U1pnMECHVSR0fdSuw4AMIGiWw8w9eTQCp_W8ILZpGo2jqA1lYxelig8Lk_AGdQeziT7xkK34z8xFtSvbofzo_Priah0hkkl2QBThaFKYxYvlCMZYFU3023YbC5-WXKwel5KAFrpYj5rPC62YhKGQjDe04qDd_pOHW6iFrTgQ6uWDNKx8kZyyol3eLtGoqyIZD2MLI8nlU5ceorT0w9oiOKrYjuENQOalJIuX4ebrLbX2wSsvdzWGsVi8O9Jqz_n_kHyyM2x70XN3RC2TLovZlFFmsiXg29DTnaaoNDuvls3QIVloOsEilgujucjhRyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AvCAmeOeV5PRC0YmJfstbQD1UF9Xx4oxJsCDOiInCK4kc2eB8wkZ2-pTZnmCXQ2pYjm9CWmx2SFtDEmK8rBpnEIPPoAzkTXo1ZhBQ_nctcH6L3-FhjPM5l49L-1MuiNHBKqvnZ9ZNXI6AYkQ03mhFt2240N5J_OzTdAnSO1buWHXA8iQEf6HWvyzW5nLiRnAeuXhq1RKRHEGriQR1XQBiOZ8AfE-8XjXUTfU-LMVK1647zpvP6IBJdg8i6hE7rqoW2ZGb7gdgkU1ix0BoWoCkl8CGdbQV7WjA4uSHkjq0VAQ2H5ymS4ShYfZAWbw0kA-a9ehTTx4wmfwstjQlGvncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1XZsb-KgtLYGtSy-_nknVP965iRieWcIgEbaAT2_sPfP6Guw2ETzRfKvE8Cnvaobn7eZ-eXnt0pZ2neKBOqUo-hfoKqzypiS4l-3eH_OZiT2LehBDRPv-zQe62xVyNrxM4VN7iYIRDDfX8Q7mVoLnSh7m3Nu1umx1rtn_kHOZ_UFV0CNQGARp5lZvl1qIZDy9_roIqy-ibsBruIDx3fjoN8anCr0F2JByfN0DpwjO2NkFXnzjPCmAQnYRa9T8FZ3bx2KA2LzM52s0SeSq_RJvhMbEJg-Qf3l4yAGr46HH7Gh-54zLJG4g2IRK08Ao5p4QwDRZLlUYC8jiS758GRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xab8aNhSY2AOgGOGDg1DoJi0RkCsNT9Scor5WhCgmvh56Rl1YRL3jZyhyoekGSIN86ovriBi2HFJo38plttP8hg0t0oRHPI9iJf_aMqdCuK2iOjGCnhYkd9d7vr6GbaTSLWmwP0AWWqL2v2jbcGqXzAVbE0GZo4COyTWE5xLTK-9DPYzDgYo-F9UEOkcl8YA-sGAEKPXXQWTf8BCV3imWyrkdfAu1l4U14hsjXP3gK6CyoO_5he6kF9ZgS7dQJRglNvRHFFnYXGpJiyDgrGQkjpOX-LokVHG1VvqA2N_1TAeFjINLogHNENdDUs0R8258tD6WRE93acjuCqSR-v4wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بازدید دکتر سید جواد حسینی، رئیس سازمان بهزیستی کشور از دفتر تهران مجموعه رسانه‌ای خبرفوری
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3218110</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/654210" target="_blank">📅 21:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654209">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
اسرائیل گسترش تجاوزات در لبنان را به اطلاع دولت ترامپ رساند
🔹
کانال ۱۲ تلویزیون رژیم صهیونیستی گزارش داد اسرائیل دولت دونالد ترامپ را در جریان ماهیت و اهداف حملات جدیدش در لبنان قرار داده است.
🔹
روز گذشته مقام‌های دولت دونالد ترامپ به رژیم صهیونیستی درباره گسترش تجاوزات این رژیم در لبنان علی‌رغم آتش‌بس ادعایی اعلام‌شده چراغ سبز نشان داده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/654209" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654208">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/798f002d6c.mp4?token=J2J5DxbBjNSsHoi-eq2jEHaUwnem9jbadp7VlASa3b2TG3IYZLSfcQhFetzuoB6jG3jSm1qno5uTQPDAGhw8i4nXXhq5msQyXuq5SwUtgrlY87Lt-UdaHzUl7SfZlfmOuqoBlP36Vfsq_XvUNY4LPQp5DVa4L-MwPEFHymSVOLKqhQRLr7ruFVbMuqwhzhCpKtgMfLjOeXPx-nweq90vta-MHDJ-pgzI08q_Ocf0MW1R0zkZ8q8arx6tdcpbasWBxYeomdc0FrocIb8TGqCOwTaZ-08WNEk5rNqtCSsav__jIUJwERE7DqZZcDcuY5TSw7TVh-EaIEm0dm5HCEuGTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/798f002d6c.mp4?token=J2J5DxbBjNSsHoi-eq2jEHaUwnem9jbadp7VlASa3b2TG3IYZLSfcQhFetzuoB6jG3jSm1qno5uTQPDAGhw8i4nXXhq5msQyXuq5SwUtgrlY87Lt-UdaHzUl7SfZlfmOuqoBlP36Vfsq_XvUNY4LPQp5DVa4L-MwPEFHymSVOLKqhQRLr7ruFVbMuqwhzhCpKtgMfLjOeXPx-nweq90vta-MHDJ-pgzI08q_Ocf0MW1R0zkZ8q8arx6tdcpbasWBxYeomdc0FrocIb8TGqCOwTaZ-08WNEk5rNqtCSsav__jIUJwERE7DqZZcDcuY5TSw7TVh-EaIEm0dm5HCEuGTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار یک خودرو در حیفا
🔹
منابع عبری از آتش‌‌گرفتن و انفجار یک خودرو در منطقهٔ «اور عقیبا» در حیفا خبر می‌دهند. یک جسد از درون خودرو کشف شده و هویت او هنوز معلوم نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/654208" target="_blank">📅 21:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654207">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6LOxVrFQQnsXcktnwJp9qOyyYqvnNN_-4zlp2yN7s653T3X8BbAUYRoI3ijZLI3w2Lj08s3kny3jOnztdkD7QMNAXf5wnSP7XSTMCYS0MSrLWtmYdXRqJj0gzAVfmEHLj7Uabg2xi8WOVhJ9cf0zH47ZC69TQ91jWRvCOWjI5SiRQ0eb2_ofu_gv7aweXOU81xSqw9OkBLBmY3rfrNa42JKrXCxvtcFuG7rb28zU2ezsLh7henyNniCoMsz8u5FrJp4EHc2PBrDjt13n-VJ1fk8pG3OZ6cMpv50drJSTkBJU-GcTceaWh4HKXRLZSGyOrs8NOgXrTngiha9r6olaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب گسترده پیام حج رهبر معظم انقلاب در رسانه های بین المللی
🔹
پیام حضرت آیت‌الله «سید مجتبی خامنه‌ای» رهبر معظم انقلاب اسلامی به مناسبت برگزاری حج بازتاب گسترده ای در رسانه های بین المللی داشت.
🔹
خبرگزاری آناتولی با تیتر «مقام معظم رهبری ایران می‌گوید کشورهای خاورمیانه دگیر سپر پایگاه‌های آمریکایی نخواهند بود»، نوشت: «مقام معظم رهبری ایران روز سه‌شنبه گفت که واشنگتن دیگر نقطه امنی در منطقه نخواهد داشت.»
🔹
خبرگزاری فرانسه نیز به بازنشر موضوعات منطقه‌ای پیام امروز ایشان پرداخته و به نقل از ایشان نوشت: «مسلم است که عقربه‌های زمان به عقب بازنخواهد گشت و ملت‌ها و سرزمین‌های منطقه دیگر سپری برای پایگاه‌های آمریکا نخواهند بود.»
🔹
الجزیره در بازتاب این پیام نوشت که رهبر انقلاب اسلامی تأکید کرده‌اند آمریکا دیگر امکان ایجاد محیط امن برای حضور نظامی و استقرار پایگاه‌های خود در منطقه را نخواهد داشت. همچنین دعوت به گسترش همکاری و دوستی میان کشورهای اسلامی و ضرورت حرکت جمعی برای پیشرفت جهان اسلام از دیگر محورهایی بود که رسانه‌های قطری به آن پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/654207" target="_blank">📅 21:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654206">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اعلام آمار رسمی؛ ایران در جنگ تبلیغاتی آنلاین از آمریکا پیشی گرفت
سی‌بی‌اس:
🔹
تحقیقات نشان می‌دهد در حالی که سه ماه از درگیری نظامی ایران و آمریکا می‌گذرد، تهران در میدان نرم‌افزارانه و پروپاگاندا آنلاین موفق عمل کرده است.
🔹
بر اساس مطالعه مؤسسه گفتگوی استراتژیک، حساب‌های ایرانی در شبکه اجتماعی ایکس در ۵۰ روز پس از شروع جنگ، افزایش ۳۰ برابری بازدید و لایک را تجربه کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/654206" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654205">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تصاویری از هدف قرار گرفتن خودروی هاموی متعلق به ارتش اسرائیل در شهر بنت جبیل با ریزپرنده انتحاری ابابیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/654205" target="_blank">📅 21:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654204">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7cdda78d.mp4?token=g364YJXgMhJMd2PPwuL26W0JPONB0Pn6FetR1Vjz662znSUvpoiAimKQuA8CYefIT79568EQte-9HRYSCudbHh_F92plMpKlWG_6qRKcw9WwJZN91sHN1-Hozi0tBZ3qFvgRGtFTYYFq-lrCIOY8DqE6Ttah0IDSIyQT7mXtobOy8IopAcCNAmFcunkll_uZ19_OfSmITLENR1xITyoKfSi28MxvG7gZEXLCocMBcxzLQ3sNC2c6UwX9FvBvJA0LHvBFL3H_MhloHSCDNdaOD9ymlvJULgC--zG7zOmddFwqdjDfiWG2EDpH6PxrzaHM3XK-FwqGmbyxgBV4cYnEHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7cdda78d.mp4?token=g364YJXgMhJMd2PPwuL26W0JPONB0Pn6FetR1Vjz662znSUvpoiAimKQuA8CYefIT79568EQte-9HRYSCudbHh_F92plMpKlWG_6qRKcw9WwJZN91sHN1-Hozi0tBZ3qFvgRGtFTYYFq-lrCIOY8DqE6Ttah0IDSIyQT7mXtobOy8IopAcCNAmFcunkll_uZ19_OfSmITLENR1xITyoKfSi28MxvG7gZEXLCocMBcxzLQ3sNC2c6UwX9FvBvJA0LHvBFL3H_MhloHSCDNdaOD9ymlvJULgC--zG7zOmddFwqdjDfiWG2EDpH6PxrzaHM3XK-FwqGmbyxgBV4cYnEHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عید قربان به حقیقت ز خداوند کریم
آفتابی به شب ظلمت انسان آمد
جمله دلها چو کویری ست پر از فصل عطش
بر کویر دل ما نعمت باران آمد
🔹
عید قربان مبارک باد
🎉
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/654204" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654203">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d932c9054a.mp4?token=pxl675s5vn0fBzgITfpmEueY-UafJjRUAy4odm9x-nGdtPC8phTvWjw9Q-3ZoGApHdHAYtI-dO-qx_q6sjeTryr2SrD7P1_QDCxpSK9voA6U1CuES3NQQInDh4Rc7hgGNSdJbDrYfaprCyyYlF6Jn7CwRhxOpjof2WtrYiDzkAp3oY2763XvpqMVzrrmFIu_LBOrWWcwWSDYD_bxAAyjm7cj9JoLzNVDeS9U3EmykseENldGh3isJv_66xA9H_EPvB_b1Zl1clZGRKoM75mu_DAxV3L0W871fsSLJGfwoKLEW1FvtsbknQ9mc4ZAx6Spl3b94gndfTDAzCzQaoG2-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d932c9054a.mp4?token=pxl675s5vn0fBzgITfpmEueY-UafJjRUAy4odm9x-nGdtPC8phTvWjw9Q-3ZoGApHdHAYtI-dO-qx_q6sjeTryr2SrD7P1_QDCxpSK9voA6U1CuES3NQQInDh4Rc7hgGNSdJbDrYfaprCyyYlF6Jn7CwRhxOpjof2WtrYiDzkAp3oY2763XvpqMVzrrmFIu_LBOrWWcwWSDYD_bxAAyjm7cj9JoLzNVDeS9U3EmykseENldGh3isJv_66xA9H_EPvB_b1Zl1clZGRKoM75mu_DAxV3L0W871fsSLJGfwoKLEW1FvtsbknQ9mc4ZAx6Spl3b94gndfTDAzCzQaoG2-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات درگیری نظامی ایران و آمریکا در دو شب گذشته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/654203" target="_blank">📅 21:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654202">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaSXGx9hajuFPjIVA3MB9GNEjLpdov7mJjAkUx-4AXAZilkK8GAFq0png6IhrWN73T3sfKLeCZPm0VPHsAjCSeVC6KNOSIcP4X316fK-ncTXTn2Hwz6Ai2DFVTq8trZuTqV5Ps2e5YH-o13Tcz9k0_a4vGOWPRjj6e5ChAbA1Q3xJp1Pizn8Qmuw3zttxbWtkUWAwpLkX0TLruwazx3Dr0x9c7oeeGJWtL5xUS90m80tscgmp49poZ73ICsukRdp4OMKdpvt46Yk367DPh-BEMynUDGu4TAMxanlGgI2oZxB56YoWYZ4mozfcVs8mZNMkxJizoAgCW5F1zXcfTUr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تخفیف‌های ویژه چرم مَنطِـ آغاز شد!
تا %70 تخفیف
➕
%10 بیشتر
و 1,000,000 تومان هدیه اسنپ‌پی
برای خرید «حضوری و آنلاین»
کد: PAYSS9R
حداقل خرید ۴ میلیون تومان
مشاهده محصولات
👉
manteofficial.com
@manteofficial</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/654202" target="_blank">📅 21:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654201">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5n0nn7ceyuefUM2GqiXnNR6a2Wt1GyX7aOpb0MoySUovcjXJ7MsPcFJ1xb92AsHFCEJbDhZg_GHhsalw-vcD568J3jwFEkt7sOPXIFYjANS0uD6aAxbY4pEP40VbU5bkR7cEaqnlK7CvrLIoKFQm6FNUW6qjommYnInNwz7xsNXJcFcSIdfdvxCNGv-xUrh_Y0lHXSGSVjYoOHZ4EKly843uZkLOOkaf5yg68TC6QOtR2ZcI0YkA-GGDSABmh06NA-KiKYgMysfgBTytDdRCmptIyC8ZCrryLS232_mPyun6N-diquZan6ka1wD-nJpAlWuNQpaZwoS2Hjl1BGWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب گفتند: «سلاح الله‌اکبر»
الله‌اکبر یعنی: همان خدایی که دریا را برای موسی شکافت، هنوز زنده است
شما در یک جمله کاملش کنید:
الله‌اکبر یعنی...
پیام‌های شما در رسانه‌های خبرفوری منتشر می‌شود
شما هم در ویراستی خبرفوری کامنت بگذارید
👇🏻
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/654201" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654200">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqRYvj0JoBTZwfFz2yQjA-ax0yEo1-rEU1RPJXJZLWkPf45J3DlvMVodUu7Zfx1n56sPbPDVNLxHbHoj5scOp-FohOTMG6e4qkVpSQXxaCaXelOnnvZiUR2WJM7UZdH_a1wXCNbs9O5KIiY6e9R-sKvAOk16bELho6gLWHqt60StQR6BeOn_owH3P3np8DR7yXnU4KoCOD6bOf5rXRY81NTMuY4RNm6qGUR7m4HUv7IYlamgoUblRLGRf8QWCHbGo9Nj8EnbEX2dNRF6HEIH5o8SeoBdvjt8JBXnGua056RqblR--7xssGnfDxuDR1uTVrv9T-L5pYpobIQxCZ8V3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا کاهش چشمگیر نیروهای خود در ناتو را کلید زد
🔹
آمریکا در اقدامی بی‌سابقه طرح کاهش گسترده نیروها و تجهیزات نظامی خود در ناتو را به متحدان اروپایی اعلام کرده و از آنها خواسته است بار اصلی دفاع متعارف را تقبل کنند؛ اما همچنان نقش بازدارندگی هسته‌ای خود را در قاره سبز حفظ خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/654200" target="_blank">📅 21:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654199">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9662fd766.mp4?token=E8zYQNW_qSUTt2XnNqZUoFoZHkOC6dbfcHbjWC87sRrBRL-B_tIx0Q4rWKsOt0pXmOPEdq9gxBrMoHdMT_uK155lAQdqAwdl6Y30yCekpLcXkF8tVeOSlRbcWPW1iBJ0_a3Gq8Ml2sBb_cvUBjgFsDjXvOjWodSd8gzVutlIRcOJOlVN3D2pKJ8mnqfcc8MhuPozfM_zcnZTUaRkAvcyTS1KOVTpxjx3V6eraWuPj_-03buEc7F_FMkHFNek5cWYEDIi7cj7RGL477K4Nv_qS2YBNV-K6afXwCKlQBpwII64h-u9FX_BsVcf9h0v3-1Ux1uOo3z8qf7Epj8UqUeKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9662fd766.mp4?token=E8zYQNW_qSUTt2XnNqZUoFoZHkOC6dbfcHbjWC87sRrBRL-B_tIx0Q4rWKsOt0pXmOPEdq9gxBrMoHdMT_uK155lAQdqAwdl6Y30yCekpLcXkF8tVeOSlRbcWPW1iBJ0_a3Gq8Ml2sBb_cvUBjgFsDjXvOjWodSd8gzVutlIRcOJOlVN3D2pKJ8mnqfcc8MhuPozfM_zcnZTUaRkAvcyTS1KOVTpxjx3V6eraWuPj_-03buEc7F_FMkHFNek5cWYEDIi7cj7RGL477K4Nv_qS2YBNV-K6afXwCKlQBpwII64h-u9FX_BsVcf9h0v3-1Ux1uOo3z8qf7Epj8UqUeKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوای الله‌اکبر در سراسر کشور طنین‌انداز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/654199" target="_blank">📅 21:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654198">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ice8Rmiz62iOK_iYvYHinndPp6GZX-hdQrgZx0wLiRuy0PYZTNwFxu-MToZqP0-EgECee-7GSdnLHOUZmFzT9P5iSejq-r2g1610t7BprGuhmB2ZVE7KI0GdQa3f5R1aK0QTarVX8cZfLNvzlUz3_qeNjHyW7VDR3zpCw1qmymhUoNACxjTx57SC4troB6RXbEV6fXMHtN21bywGek7dLxPM_ThSABVQmZr6DGlE_chkdbpNXhZWdW7SirTT21XDyDTZ1bdkJ6xNJZ8rSJgEuPKvq6Wega-DI8oLnRYfaMFBl_vrNUA-_joBauluckLUE09TipB_D0iTGSNYZzUbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسئول حزب‌الله: ایران مصمم است لبنان بخشی از توافق باشد
🔹
عضو شورای سیاسی حزب‌الله تصریح کرد با وجود تلاش‌های آمریکا برای جداسازی جبهه لبنان از مذاکرات اسلام‌آباد، ایران مصمم است که این جبهه بخشی از هرگونه توافق برای پایان جنگ باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/654198" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654197">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce48cacc5c.mp4?token=Lkrfw1U8a45xrEHAOiSnkHSNj8aChZnj8wPs941b0WJW40Nuz5Ib78JC1aXfySH6AwuGJGqSiWSW9w057LqdloFwMqrTKY-3vzNapwekzkgAV9EFU41SEhoMu0O2NQN5D2TTG6zeyBvVWKf0L3HxvsXMd1myQ1Vpl6wLWEynf3O6mvNKU9wAMdSSnnVEV9S3jYezPQ487Aex1BGxc09Js2TdpjgM_D7pGDWllKMAd3dY-4xYtdCYocnIALPJKud10WIa6x3j-H9f8Z8ZjUKQ_1spI2zfMHFSu4JFP5zs3YTSND9cliHZC1oRS4gQa-eU6xmWcHgdq5L6lOAadtzU1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce48cacc5c.mp4?token=Lkrfw1U8a45xrEHAOiSnkHSNj8aChZnj8wPs941b0WJW40Nuz5Ib78JC1aXfySH6AwuGJGqSiWSW9w057LqdloFwMqrTKY-3vzNapwekzkgAV9EFU41SEhoMu0O2NQN5D2TTG6zeyBvVWKf0L3HxvsXMd1myQ1Vpl6wLWEynf3O6mvNKU9wAMdSSnnVEV9S3jYezPQ487Aex1BGxc09Js2TdpjgM_D7pGDWllKMAd3dY-4xYtdCYocnIALPJKud10WIa6x3j-H9f8Z8ZjUKQ_1spI2zfMHFSu4JFP5zs3YTSND9cliHZC1oRS4gQa-eU6xmWcHgdq5L6lOAadtzU1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سلاح الله اکبر
🔹
با سلاح الله اکبر بود که ملّت مسلمان ایران در چهل و هفت سال قبل قیام کرد، رژیم طاغوت، دیکتاتور و وابسته‌ی پهلوی را ساقط کرد، دست و پای امریکای طمع‌کار و مستکبر را از کشور بُرید و نفوذ صهیونیسم را بکلّی قطع کرد.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت برگزاری حج | ۵ خرداد ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/654197" target="_blank">📅 21:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654196">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">این زمان برخیز تا از بام‌ها
لرزه اندازیم بر اندام‌ها
🇮🇷
الله اکبر
🇮🇷
الله اکبر
🇮🇷
الله اکبر
🇮🇷
الله اکبر
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/654196" target="_blank">📅 21:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654195">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3mT-l8MKWIkV3rNM5-BASUYIsI_O9_6FQpoeGCl3kN2F41wie1nDih7SR2goRyBlCD8gd9Accnul59C_p0bgP7Tm7vsrmcAPPf8fhbvGk1_JLPVqdEZGy2TYKvzdytfSJfsQPluE10DmI0tW7Ufz6vZqcIDmX1lT38IfE_VVgcftT71W8YAQEwhg5ifOjHm7ePsGzDgXFT3oB9g5B-T2-fOGg6AFrffTz-E0MBJ-lRgtTxUZ-Fu2dN5YNZDo_-0KlaFcklkC7c_jNOknb-qs_aMwHRT23cB97pIbv37-0EIsVaSu86woSN58t_WSsi3ZO8LzdMYokhxeyG7APj6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو دستور گسترش تجاوز در لبنان را صادر کرد
🔹
بنیامین نتانیاهو نخست‌وزیر رژیم صهیونیستی امروز سه‌شنبه در نشست کابینه سیاسی و امنیتی این رژیم گفت که دستور گسترش عملیات در لبنان را صادر کرده است.
🔹
نتانیاهو در این خصوص گفت: «با دستورات من و وزیر دفاع (جنگ) و با هماهنگی رئیس ستاد کل ارتش، در حال گسترش عملیات خود در لبنان هستیم».
🔹
وی با بیان اینکه ارتش اسرائیل با نیروهای گسترده‌ای در حال انجام عملیات زمینی است،‌ مدعی شد که نظامیان رژیم، برخی مناطق را در جنوب لبنان اشغال کرده‌اند.
🔹
نخست‌وزیر اسرائیل در توجیه این تجاوزات که نقض آشکار توافق آتش‌بس است، ادعا کرد:«ما برای تقویت منطقه امنیتی در لبنان و همچنین محافظت از مناطق شمالی تلاش می‌کنیم.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/654195" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654194">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
هشدار آمریکا به اسرائیل درباره حمله به بیروت
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی گزارش داد که دولت آمریکا در پیامی صریح، مقامات تل‌آویو را از هرگونه اقدام نظامی علیه پایتخت لبنان برحذر داشته است.
🔹
آمریکا به رژیم صهیونیستی هشدار داده است که به هیچ وجه و در هیچ قالبی نباید به شهر بیروت حمله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/654194" target="_blank">📅 20:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654193">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
هشدار ایران به آمریکا: حمله به بیروت و ضاحیه مسیر مذاکرات را نابود می‌کند
🔹
غالب ابوزینب، عضو شورای سیاسی حزب‌الله: ایران از طریق واسطه‌ها به واشنگتن پیام داده است که در صورت عملی شدن تهدیدات اسرائیل علیه بیروت و ضاحیه، کل مسیر مذاکرات نابود خواهد شد.
🔹
دولت آمریکا پوشش کاملی برای تجاوزات رژیم صهیونیستی به لبنان ایجاد کرده است. ایران بر حضور لبنان در هرگونه توافق نهایی و پایان جنگ اصرار دارد.
🔹
حزب‌الله حق دموکراتیک خود می‌داند که دولت را با حرکت مردمی ساقط کند، اما هنوز به این مرحله نرسیده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/654193" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654192">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جزئیات حضور پرستارنماها در اتاق عمل یک بیمارستان!
احمد نجاتیان، رییس سازمان نظام پرستاری کشور در
#گفتگو
با خبرفوری:
🔹
در یکی از شهرستان‌ها به ما اطلاع دادند که تقریبا تمام نیروهایی که در اتاق عمل کار می‌کنند؛ اینها همکاران گروه پرستاری هستند یا از رشته‌های دیگری هستند.
🔹
ما این موضوع را به وزارت بهداشت ارایه دادیم. چون ما اجازه نداشتیم به داخل بیمارستان برویم، از وزارت بهداشت خواستیم این موضوع را بررسی کنند و گزارش را به ما بدهند.
🔹
پرستاری که در یک هیئت انتظامی حکمی گرفته و ممنوع‌الکار شده است به راحتی می‌تواند در بخش خصوصی مشغول به کار شود چون جایی نیست که این را استعلام کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/654192" target="_blank">📅 20:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654191">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vb8LPgUvCYCjomS2y-cm5QaubpTns-J86GondC9eUhAiLjjS-P2dB1cyo6FDkFXY7j5C3w7_rmszMjZ3sdV2iVVTr9uj2ypOFE7Wa6TlFJ8rl92LZLmTGwIh0YEBywLx2w0betQ-o1Ye3ux7i_NfCsbA6FBNf59Q16TjG6habcgmm-qT9G0-UbXIPyF9l43JJqTbrQ7HBpHD_Su-vjYY4SOBsIRL7HrPg89JGAAcz_Ytr9kubbja9SEpqJpMYVVo5V-n2uTETukzZCfnA1yG28wiJHwQbUFeKwyfGhumq1xhR_WQq70eBBmchwr9bmTW2MHbYrFIJ9CpWAMGyrgopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امشب ایران سراسر فریاد «الله‌اکبر» می‌شود...
🔹
در لبیک به پیام مهم رهبر معظم انقلاب اسلامی و در حمایت از وحدت ملی، جبهه مقاومت و آرمان‌های انقلاب اسلامی، از ملت بزرگ و همیشه در صحنه ایران دعوت می‌شود امشب رأس ساعت ۲۱:۰۰ در سراسر کشور، بر بام خانه‌ها، میادین و خیابان‌ها، فریاد «الله‌اکبر» سر دهند.
🔹
این ندای واحد، نمایش اقتدار ملت ایران و تجدید پیمان با راه شهیدان و ارزش‌های انقلاب اسلامی خواهد بود.
🕘
زمان: امشب ساعت ۲۱
📍
مکان: بام منازل، میادین و خیابان‌های سراسر کشور
🎥
همراهان عزیز؛ ویدئوهای خود از این همصدایی سراسری را به آیدی زیر ارسال کنید
👇
الله‌اکبر
🇮🇷
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/654191" target="_blank">📅 20:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654190">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
نگاهی به مانيفست مديريتی سيدعلی مدنی زاده
🔹
بررسی اقدامات وزیر امور اقتصادی و دارایی نشان می‌دهد نگاه دولت به «کریدورهای ارتباطی» از سطح یک پروژه حمل‌ونقل فراتر رفته و به بخشی از راهبرد کلان اقتصاد سیاسی کشور تبدیل شده است؛ جایی که کریدورها پیشران بازآرایی اقتصاد ملی و ابزار ارتقای جایگاه ژئواکونومیک ایران تعریف می‌شوند.
🔹
در دستگاه فکری سیدعلی مدنی‌زاده، توسعه کشور دیگر صرفاً از مرکز آغاز نمی‌شود، بلکه مناطق مرزی، آزاد و پیرامونی به کانون‌های جدید رشد اقتصادی تبدیل می‌شوند و کریدورها نقش «ستون فقرات» تحول اقتصادی را ایفا می‌کنند.
🔹
وزیر اقتصاد بر این باور است مزیت اصلی کریدورها زمانی ایجاد می‌شود که مسیرهای عبور کالا به «قطب‌های صنعتی و خدماتی» تبدیل شوند؛ هدف نهایی تنها افزایش عبور کامیون‌ها نیست، بلکه شکل‌گیری زنجیره‌ای از تولید، خدمات و تجارت در امتداد این مسیرهاست.
🔹
در منظومه فکری وزیر اقتصاد، مناطق آزاد تنها دروازه تجارت نیستند، بلکه می‌توانند به الگوی حکمرانی اقتصادی نوین تبدیل شوند؛ او از همین زاویه در حال مقابله با «بخشنامه‌های مزاحم» و حذف محدودیت‌های ارزی به عنوان بخشی از پروژه «آزادسازی واقعی» است./اعتماد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/654190" target="_blank">📅 19:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654188">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM4rcuuLs5PZI2ykSuKgNSZNKe0UWba2KfGQyG7f7j9sz1ANIESdASC8qxtljJrnKyw_-fb8fh5pCX4CukEFC0Cu4U9uLEk0C8MV_KReewRE0Yzt9GhwD9_H1hmTjB-sJHDlakz3H1jCysfGWdbrGj_S6xeZGausihnwEMbBBvzon06HOVok43cnDVLFPj46xta8YhW5vBad-1trhh1If3v4PgOnFWtgM8ydKElNNUQp1BF8BuKhYlcbUkvHH6tbwDLzFtd6whEzQfs-9hYe8ev_GEz3HEcfepRSYVcDYzinTnhBRTSnOa6IY5Q_Xm33No--UomI923ekNZqNawvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a942e9380.mp4?token=SilKgYuBTZ6wR3PyQvjG2DAHuS6IHy5VkzawtbQet4wHWbwhPLBXnbyfBrFAR-s-SHg7vkW55pwtc2uixCQjjJL0guXRKJHkznvaXjOJX3sG_rB7_KEbMW7cJAf3CXYUx0HI-OVWvjfs_FhbY4npqB6ML9rMZ1KEgYNDMyOvCpXBhviPvCQtI56bVVMqI2u60JRfyGA7C-AcvuLVyTz1ZYci796ZWa2LRYdw6ilTzH2nfmse0vGMgUbh6CiwOE1nTLmsTMtvoBUwQDGFB5VeC9KEVfNUaGu0TvO625w73FxOX--AC2SIj6Wf3olOeSsd0GqDiB2cmGAIELwFHFSgkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a942e9380.mp4?token=SilKgYuBTZ6wR3PyQvjG2DAHuS6IHy5VkzawtbQet4wHWbwhPLBXnbyfBrFAR-s-SHg7vkW55pwtc2uixCQjjJL0guXRKJHkznvaXjOJX3sG_rB7_KEbMW7cJAf3CXYUx0HI-OVWvjfs_FhbY4npqB6ML9rMZ1KEgYNDMyOvCpXBhviPvCQtI56bVVMqI2u60JRfyGA7C-AcvuLVyTz1ZYci796ZWa2LRYdw6ilTzH2nfmse0vGMgUbh6CiwOE1nTLmsTMtvoBUwQDGFB5VeC9KEVfNUaGu0TvO625w73FxOX--AC2SIj6Wf3olOeSsd0GqDiB2cmGAIELwFHFSgkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنایت وحشیانه رژیم صهیونیستی در غزه
🔹
ویدئو حاوی تصاویر دلخراش؛ در جریان بمباران جنوب غزه، محمد، کودک یک ماهه فلسطینی مادرش را از دست داد و پزشکان مجبور شدند به‌علت کمبود تجهیزات بیمارستانی، یک پای او را نیز قطع کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/654188" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654187">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MU0QO_ZVRemdxkEMDpeWCcO2zZJNPdruDRmALWFLdvk5bjkcD7Ik7T_iWoAQlhyLnZGK3neGkG7UrvB55SddrzqViRH_9BAUL06DDUykZw0EuS_Fb6gjNeX-VwXpOVKv2z89BNpbip-csgEoX4K5fFj2hLLIUybKs-0gHV8Wa9IYXw0LBCD45QLnDIz6114DOKaCaH0d9Pyd1nS8997VuaRQTfDvBpH9wd3IRxSgJzT-RFHJzYEQq3g4e78Ek0KVpshSUTuo34-PKufDLlAYeBEOYb0vDTk155I411Zxl56b-W5H_2xCz3QY3syoYtBx5NW1nyzRyuQ52kPKdv2Jbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورتنیکوف، رئیس سرویس اطلاعات روسیه (FSB): کشورهای غربی در تلاشند تا از تروریست‌های سوریه در جنگ علیه ایران استفاده کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/654187" target="_blank">📅 19:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654186">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5d-umv5TEqjSbyaDfFNtDsSt-6xBve903CMeZOk4LoyxtocB637_lvyxB_xneigG3bUnY3-WCVm8WIbCvVooVt--ovmhMLRM77uFKpXZKeWjvjvrc8v2lmc1A-gPkPqJS2JXWb8m2oz7SXxPgBpkQKcX8cVD92FGX7IT-EkRSuv5p-oXHUOlaC0uvvuY_ljcmSilzKq_NOKi7Cf5x9y3iIX4YleAvY-vFq9pIHYXFjkZLKHGlyzIqPCjcg-Zq2B1Hhb5XPaSx3M309LLbnDwndGjOIFItpYS44bd3E_9X-prr0NzKCoQUcxlXLpyiLNO-nk-QaPewAHsRcGtWxaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش امارات در جذب مزدوران کلمبیایی و اعزام به سودان
🔹
«ماوسی سگون»، مدیر بخش آفریقای دیدبان حقوق بشر امروز سه‌شنبه در بیانیه‌ای اعلام کرد که جذب و بکارگیری پیمانکاران نظامی خصوصی کلمبیایی، شواهد فزاینده‌ درباره حمایت نظامی امارات از شبه‌نظامیان پشتیبانی سریع را افزایش می‌دهد؛ شبه‌نظامیانی که بارها مرتکب جنایات وحشتناکی در سودان شده‌اند.
🔹
سگون افزود که صدها مزدور کلمبیایی به دست اماراتی‌ها در یک پایگاه نظامی در منطقه الظفره حدود ۲۵۰ کیلومتری (۱۵۵ مایلی) غرب ابوظبی و در یک مرکز دیگر در همین شهر قبل از اعزام به سودان برای جنگ در کنار نیروهای پشتیبانی سریع، آموزش دیده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654186" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654185">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7v9vFtwHzrEAtROvi7klscV28YVMcqqFWZzd5hfPLYpst897kOnrsXP7vLDZN_1_ahfgtFt1UXKxFhombS5m7POLIUMLCpDOUQO3F9UgFPE1yoCzzZCze8v0lWXZ2NWDEvthg1p3bifgxGnSChtT_I7r_aaehrRSxE7etr_wDBwVOrLrY2NAJe1BS4L4C0UNisGDcIllSZIVq1J0eFznMPLqcr_duTg1K93IYhwl_h4xCImOSbzXt9AFhDjjY9HN1QRYtdI_xAB23e5yVmf5ogsUvhwBbLoevvX7iMgVWiMhf7b_03EJsO81xsifWK0yrNopXdIknTssCxg02e5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان در گفت‌وگو با امیر قطر: ایران برای دستیابی به چارچوبی عزتمندانه برای پایان‌بخشی به جنگ و تنش‌های جاری در منطقه آمادگی دارد
🔹
ایران صداقت و پایبندی خود را به مسیر گفت‌وگو ثابت کرده است؛ اکنون زمان آن است که طرف مقابل نیز اراده خود را نشان داده و در مقام عمل و نظر، به تعهدات بین‌المللی پایبند باشد.
🔹
تلاش‌های جدی و کارشناسی برای جمع‌بندی نهایی اسناد و متون پیش‌رو درحال انجام است تا مسیری روشن برای ثبات فراهم شود.
🔹
امیر قطر: دولت قطر از هیچ‌گونه کوششی در مسیر برقراری صلح، امنیت و ثبات منطقه‌ای فروگذار نخواهد کرد و همچنان به نقش میانجی‌گرانه و سازنده خود ادامه می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/654185" target="_blank">📅 19:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654184">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وزارت ارتباطات: اینترنت همراه، امروز (سه‌شنبه ۵ خرداد) وصل می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/654184" target="_blank">📅 18:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654183">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qejNOv70BsS8LKab0pLJUF0zGiP9HytN-IO3vWJGxrFiSk-6R9DDqGDD9IZj8vPL43I1Sii6ipYnQmaRDW8TAeWJj1Hjm8bVmdJVH7SVzlaKytNvDiqGxMKPsH2wJQKatP0zdr5swtLwxQfhwjyhdfkVL1wS494BuC2MViIfdHNXVdD3iUB_uYiHWf1HCsQlMspmpdYIrscpzU_nz2CJVuhjbiZ8M-9merQuHbKQ4CpcYX8qUxErXtANzNHYd3VA_Ew8jQGRD60TUwvTGtJJA1VX9jnu7cWU-VVf5aXnbUeiMVQZfxlFKsbN8rzyvZ0d29rhsV0jP-0dxiddee844Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواسته‌های اصلی ایران و آمریکا در مذاکرات از نگاه سی‌ان‌ان
🔹
شبکه آمریکایی در گزارشی نوشت، ذخایر اورانیوم و غنی‌سازی ایران، دارایی‌های مسدود شده و جنگ در لبنان موضوعات اصلی هستند که هرگونه توافق یا عدم توافق میان تهران و واشنگتن را شکل می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/654183" target="_blank">📅 18:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654182">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای از سرگیری برنامه شکست‌خورده «پروژه آزادی» در تنگه هرمز
🔹
روزنامه وال‌استریت‌ژورنال مدعی شده نیروی دریایی آمریکا در اقدامی تازه، عملیات اسکورت و پشتیبانی عبور کشتی‌های تجاری از تنگه هرمز را از سر گرفته است.
🔹
این عملیات احیای برنامه موسوم به «پروژه آزادی» (Project Freedom) است که چند وقت پیش توسط ترامپ اعلام شد اما تنها پس از گذشت ۳۶ ساعت متوقف شد.
🔹
وال‌استریت‌ژورنال مدعی شده در نخستین گام از این برنامه، یک ابرنفتکش یونانی که حامل ۲ میلیون بشکه نفت خام بود، با هدایت و مراقبت نیروهای آمریکایی از مسیر تنگه هرمز در سواحل عمان عبور کرد.
🔹
مطابق این ادعا این کشتی که از اوایل ماه مارس در خلیج فارس متوقف مانده بود، اکنون مسیر خود را به سوی هند در پیش گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/654182" target="_blank">📅 18:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5a65b411.mp4?token=KKVYwe3NLlgNH4Z58eqQGW5Snh8YbQDS8vqJ6zwe7lNsBpFVzUqxMUkEyASHhHAXUUKS3yFzpxxpm7AIAeirmQ84v6nbjUUHQH7CHFo3iBlY5sDg9sgA6oVEYWVjSjvE9HHTm5BcAjVtHDhFdTVfXDv73NOhzl5nEaXl7pIp7VqHI3j52qDwFgpx4nD6Zam2TX0mxFWvc10hmm6eTjmw0pJXqnNTOOVlTvpovvtBBQ6xX_qw42h56ECBaW5LTYS7QY__Z3uf1KAT9fmAuJkTNq6ROnHerjOC269BbFken63pI0F6FlfkfRcEbQpv67nbqd9LkkXHcDy5lDJwJllQkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5a65b411.mp4?token=KKVYwe3NLlgNH4Z58eqQGW5Snh8YbQDS8vqJ6zwe7lNsBpFVzUqxMUkEyASHhHAXUUKS3yFzpxxpm7AIAeirmQ84v6nbjUUHQH7CHFo3iBlY5sDg9sgA6oVEYWVjSjvE9HHTm5BcAjVtHDhFdTVfXDv73NOhzl5nEaXl7pIp7VqHI3j52qDwFgpx4nD6Zam2TX0mxFWvc10hmm6eTjmw0pJXqnNTOOVlTvpovvtBBQ6xX_qw42h56ECBaW5LTYS7QY__Z3uf1KAT9fmAuJkTNq6ROnHerjOC269BbFken63pI0F6FlfkfRcEbQpv67nbqd9LkkXHcDy5lDJwJllQkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این همان چیزی است که اشغالگران ادعا می‌کنند یک هدف نظامی در جنوب لبنان بوده؛ از حملات اخیر در استان نبطیه در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654181" target="_blank">📅 18:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654180">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رایزنی ترامپ در کمپ‌دیوید درباره ایران
🔹
طبق ادعای «نیویورک‌پست»، دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد روز چهارشنبه در سفری نادر به اقامتگاه اختصاصی «کمپ‌دیوید» نشستی اضطراری با تمامی اعضای کابینه خود برگزار کند.
🔹
دستور کار اصلی این نشست، بررسی وضعیت جنگ با ایران و گفتگو پیرامون تحولات اخیر در این منطقه عنوان شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/654180" target="_blank">📅 18:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654179">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c7999dba.mp4?token=bxlOq0_pOWLc0M4hNpbnYrby1cZBG0vEwQBNMA3YPUv2vqGjNYCiU_pUAfRjNuKKI-L-Tz3WsoniAHRtZqLp3DXSiD2yehs7FvxuVzzS9feHK-aAbOsd3ao5XijDyJ7fBMpfEmysg8qiAV9-pwjb-7xHuRu7c5ZTbwEzoe9jPeE95Pm_AnOW7th5NztKPM-Ex6YNjzNmGhv6FLeN5ad0hTseM8bjX_BRtGefZ-kwNY-OfKaal7KNHB0HvWxUPl-d-MBBYP4vmWrkNCuXhPWmT2ap-3rZyBILXREGcv856jfjzXaweDUY_fRyQFCW0K-nVxCMg6MoQtD_YR0tXJ3-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c7999dba.mp4?token=bxlOq0_pOWLc0M4hNpbnYrby1cZBG0vEwQBNMA3YPUv2vqGjNYCiU_pUAfRjNuKKI-L-Tz3WsoniAHRtZqLp3DXSiD2yehs7FvxuVzzS9feHK-aAbOsd3ao5XijDyJ7fBMpfEmysg8qiAV9-pwjb-7xHuRu7c5ZTbwEzoe9jPeE95Pm_AnOW7th5NztKPM-Ex6YNjzNmGhv6FLeN5ad0hTseM8bjX_BRtGefZ-kwNY-OfKaal7KNHB0HvWxUPl-d-MBBYP4vmWrkNCuXhPWmT2ap-3rZyBILXREGcv856jfjzXaweDUY_fRyQFCW0K-nVxCMg6MoQtD_YR0tXJ3-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین انتظامی: از دفتر رهبری به (شهید) علی لاریجانی ماموریت داده شد تا برجام در مجلس تصویب شود؛
🔹
اصل برجام قبلش در جای دیگری تایید شده بود؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/654179" target="_blank">📅 18:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654178">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوزارت تعاون، کار و رفاه اجتماعی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2UgyCZUZxaDHNHCWerFhHxnHXzHgWqO2o3TiCWVSMw2MRGqpj_rxqaYv7hnTK4U6C2iTLdFGXTJUxnrZ7XlY3F03rTFqqNG3YqXERHbSLHBXGM3mv8GugKr4kpZZ-4v7gQ1YzsFb8k-v80XKDPiYrucDxAAiyNdyq0cvJQp8J3Lf8L9hyarnvuqnHnTnZ4bipzhEhmEwx_kEdIAMpRDoFtWEjWcQeRK98zih6sjeQ87FqGw3m0aA6zXzeMQEOlI_ViMNtIp252vmMcvD9SVoDTlHhExZG8hGTWy6PZSCW-KPuUnN9ECWBjU6wuzXOJZLTUheX-dLmmY1EYYmZjALQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تبریک وزیر کار به مناسبت انتخاب مجدد دکتر قالیباف به عنوان رئیس مجلس شورای اسلامی
وزیر کار: در ایجاد نهاد نوین «بانک زمان» مصمم هستیم
🔰
وزیر تعاون، کار و رفاه اجتماعی انتخاب مجدد دکتر قالیباف به عنوان رئیس مجلس شورای اسلامی را تبریک گفت.
🔹
در نامۀ «احمد میدری» وزیر تعاون،کار و رفاه اجتماعی ضمن تبریک انتخاب مجدد دکتر قالیباف به عنوان رئیس مجلس شورای اسلامی و آرزوی توفیق برای ایشان، در جهت پیشبرد آرمان های انقلاب اسلامی و بنیانگذار فقید (ره) و رهبری شهید (اعلی الله مقامه) و منویات مقام معظم رهبری (مدظله العالی)، بر مصمم بودن وزارت کار در ایجاد نهاد بانک زمان تاکید شده است.
🔹
در این مکاتبه، اقدامات عملی صورت‌گرفته برای پیشبرد بانک زمان به عنوان تکلیف مصرح قانونی این وزارتخانه از جمله تکمیل فاز مطالعاتی و اجرای آزمایشی آن در یکی از مناطق تهران به رئیس مجلس شورای اسلامی گزارش شده است.
🔹
همچنین «میدری» از تدوین «سند جامع تنظیم‌گری، احراز صلاحیت و صدور پروانه فعالیت اپراتورهای بانک زمان در ایران» منطبق بر مدل های پایدار اقتصاد پلتفرمی خبر داده است.
🔹
لازم به ذکر است غایت این تکلیف قانونی، ارائه خدمات « بانک زمان » ظرفیتهای مردمی، نسبت به ایجاد نهاد نوین رایگان و تهاتری به افرادی است که نیازمند حمایت یا مراقبتهای ویژه هستند تا از این رهگذر، افراد داوطلب پس از ارائه خدمات، اعتبار زمانی کسب نموده و در هنگام نیاز خود یا وابستگانشان، از حمایت متقابل شبکه محلی برخوردار گردند.
وزارت تعاون، کار و رفاه اجتماعی:
🆔
@mcls_gov_ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/654178" target="_blank">📅 17:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654177">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwid4yKD9n3tqce-yWn5k9e1WQS6858jBuARzP0KdBxV73ksmZo8ztOHySQzysLEiih6_63UUS9gD4chBKRFUUpw8UCwAAzT9NlIh8HLzfZ4Fzbts2ShDXJzpWBfT9KW1qChMmHKfxfgJtpIubZY_wqj4UgscN6asq_Qcn7GjKI6SV8-Eg0t2gw1OFDcjzixoF7xMSWb0I3EtX0FcQ65cvZQVCutU-6PYJI6UIlsLG91TXHBw7dDLqRSZcy0kBNm4xQEXkLCIHBj9UJQzjyyef0991EGhOeGvDRnMYk2YLk-dZZxe4QApHPtNEbe5M_EbywJljFHPgDVj0yY7h5jnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ شهید در حمله اسرائیل به مشغره لبنان؛ بمباران حومه سد فرعون
🔹
همزمان با تداوم حملات هوایی رژیم صهیونیستی به جنوب لبنان، وزارت بهداشت لبنان از شهادت و زخمی شدن ۲۶ غیرنظامی در حمله ددمنشانه اسرائیل به مشغره خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/654177" target="_blank">📅 17:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654176">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
معاون سازمان حفاظت محیط زیست: حدود ۸۰ درصد بحران‌های آب و محیط زیست کشور حاصل مداخلات انسانی و مدیریت نادرست منابع آب است
🔹
در حوزه آبریز تالاب جازموریان حدود ۲۲ هزار حلقه چاه وجود دارد که نزدیک به ۱۱ هزار حلقه آن غیرمجاز است و برداشت‌های بی‌رویه فشار زیادی بر منابع آبی منطقه وارد کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/654176" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654175">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e989bfbaef.mp4?token=HJ9JIbfxSNgaDy5zbeKxBmnLe6rqpntMVKLaph450FWOpfevIQPxz9EHI2j9p6gL7LBFNY8vvqD6mtlH40rQiWSs070SYJIJPQvLj3__hsPqm6Su1gvPtIW1ONx3ZRspmk9Xc8B9ttZ3LYZEUQNJa9yR1oP92ucNYHNld2j53hAq1j3RTSPt18mIIfOEiAFwNGQHOwm8IwML0BmGyVnWNRd8mnvBiNfyYHixlpIPIuEKCw3TyZsDyGj-Czm9H8lKzMsOVtycGjKYMlJCLZYeyJ68ErhIzOJxUJtvADgNxgaAxtL-WO8ZgSBs2FdHgMH7VnYYQA76bPFwCtoGuB8OcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e989bfbaef.mp4?token=HJ9JIbfxSNgaDy5zbeKxBmnLe6rqpntMVKLaph450FWOpfevIQPxz9EHI2j9p6gL7LBFNY8vvqD6mtlH40rQiWSs070SYJIJPQvLj3__hsPqm6Su1gvPtIW1ONx3ZRspmk9Xc8B9ttZ3LYZEUQNJa9yR1oP92ucNYHNld2j53hAq1j3RTSPt18mIIfOEiAFwNGQHOwm8IwML0BmGyVnWNRd8mnvBiNfyYHixlpIPIuEKCw3TyZsDyGj-Czm9H8lKzMsOVtycGjKYMlJCLZYeyJ68ErhIzOJxUJtvADgNxgaAxtL-WO8ZgSBs2FdHgMH7VnYYQA76bPFwCtoGuB8OcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملهٔ صهیونیست‌ها به نزدیکی سد قرعون در شرق لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/654175" target="_blank">📅 17:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654174">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مالکی: در قطر توافق شد که نیمی از پول‌های بلوکه شده ایران پرداخت شود
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
سفر آقای قالیباف به قطر در راستای موضوعات مذاکره، مسایل دوجانبه و موضوعات بین‌المللی است و آخرین تحولات بین‌المللی آنجا بررسی خواهد شد.
🔹
از آنجا که قطر مسئولیتی درباره پرداخت بدهی‌های ایران به عهده گرفته است، یکی از موضوعات سفر آقای عراقچی و قالیباف، موضوع بدهی جمهوری اسلامی ایران است.
🔹
طبق یکی از بندهای توافق‌نامه، قرار شده است که نیمی از پول‌های بلوکه شده که در اختیار قطر است به جمهوری اسلامی ایران داده شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/654174" target="_blank">📅 16:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654173">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال:
🔹
مقامات ایرانی و میانجی‌گران عرب گفتند:
🔹
«محمدباقر قالیباف» برای دومین روز متوالی در قطر مانده است تا درباره توافق پایان جنگ گفتگو کند.
🔹
به گفته این مقامات، قالیباف روز دوشنبه برای رفع موانع باقیمانده در طرح صلح، از جمله درخواست ایران برای آزادسازی دارایی‌های بلوکه‌شده خود و جزئیات مربوط به بازگشایی تنگه هرمز، وارد قطر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/654173" target="_blank">📅 16:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654172">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سازمان حمل‌ونقل دریایی انگلیس اعلام کرد گزارشی از انفجار در یک نفتکش در ۶۰ مایلی ساحل مسقط دریافت کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/654172" target="_blank">📅 16:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654171">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgp01D7Uv-nsoHATVreidEOONqx9nRylsVILZBGWJE98hqzC1F0BVo-Cf2A6t5Og7Iz72M0SPS-E7hLJ-HEnoMU2rsIxjsYm3ksTw7YNHmaRjJ5YrjWRLpYUUAdk2i9WAwmJ6XYejQzj2KPv2nFLb-_FoE32U6BDMZkyeigrjyH-SpYkSwjcg6gcok3AqwhX98n1QwsLcazxSpIS10x86yJ7ukZ57b3YDxbZaNgk_AVZnSRvaAxV30s8ZEGzP3tbCyPN29FnfpVZZJpnH1MJZrLgMwbIETsgvo5uE-U23jPkRH6RLAlGF-ve8Dz6BkCjzZSqs3bBMKhqsHCV1pj_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشایی اینترنت به دیتاسنترها رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/654171" target="_blank">📅 16:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654170">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a0b54080.mp4?token=nPReiJPn5TLpS5aoMzh-6IOAJxkgljU4A6n9QxiteFK4JtLIGnMWeEt3y29nzCtBFYTnWCQClU6GZXuJscZfVk_ZCDwONUAaDhr1nnGT6Hr6pkwmwIdDc7hFLgtAL594--EAzquPNZ9Df5g7kEQ2FBwPbC3VtiImlRlR7aeI06UCRKzXaxifAnEVSK_ZpfdqXzOp1TtvK9uXAiALdVXvOkzWBc4Fia_Zsp6-lC2TD4ZDDtCmvFoJvzt7bJkTNB4559cjEm7Ojzsxtf4VOgUnCBWB7Ib6f5aN4KnNXZ64DjkLaxUYe1ziF5G-0W2uOxwu13_xfAsl5048Y1BA-CLFQyK0t3oJy8WOV9uc2WC-t4zN-Q0bXKn8s_q4HRSSsLu3kt1gBNRtY0HxejzJdc6fU7ssuQ9IB5u3aukWShAp58Ncv16EQBrzFm-9oZ_uWqgQK8HqWRWDnisTcpNFMTTuZEBeAAlWmRPN7gxnucDrcI3pJrTsRGB2bu7KNPnMNiupb_ZE62gWNuoe2g_9Jtqyf6HXPZu6u0BQNR8UTCpyo9oWRD5OzLhluUqh40csH2WKWal31bsYVihrAmMhOHnjF2BEAfI7X1YGL94TOy4bK6v8mBHhMkEIqOh4BNfAcksamEDbWcOpSPS5E19kMCObUoUcowmx5VOOpkPLb8tj0Ck" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a0b54080.mp4?token=nPReiJPn5TLpS5aoMzh-6IOAJxkgljU4A6n9QxiteFK4JtLIGnMWeEt3y29nzCtBFYTnWCQClU6GZXuJscZfVk_ZCDwONUAaDhr1nnGT6Hr6pkwmwIdDc7hFLgtAL594--EAzquPNZ9Df5g7kEQ2FBwPbC3VtiImlRlR7aeI06UCRKzXaxifAnEVSK_ZpfdqXzOp1TtvK9uXAiALdVXvOkzWBc4Fia_Zsp6-lC2TD4ZDDtCmvFoJvzt7bJkTNB4559cjEm7Ojzsxtf4VOgUnCBWB7Ib6f5aN4KnNXZ64DjkLaxUYe1ziF5G-0W2uOxwu13_xfAsl5048Y1BA-CLFQyK0t3oJy8WOV9uc2WC-t4zN-Q0bXKn8s_q4HRSSsLu3kt1gBNRtY0HxejzJdc6fU7ssuQ9IB5u3aukWShAp58Ncv16EQBrzFm-9oZ_uWqgQK8HqWRWDnisTcpNFMTTuZEBeAAlWmRPN7gxnucDrcI3pJrTsRGB2bu7KNPnMNiupb_ZE62gWNuoe2g_9Jtqyf6HXPZu6u0BQNR8UTCpyo9oWRD5OzLhluUqh40csH2WKWal31bsYVihrAmMhOHnjF2BEAfI7X1YGL94TOy4bK6v8mBHhMkEIqOh4BNfAcksamEDbWcOpSPS5E19kMCObUoUcowmx5VOOpkPLb8tj0Ck" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«بیش از دو سال‌ونیم است که یک نسل‌کشی زنده را تماشا می‌کنیم»
🔹
روایت هیثم عرفات، فعال آمریکایی-فلسطینی از تجاوز، شکنجه و تحقیر اعضای کاروان جهانی «صمود» توسط ارتش رژیم صهیونسیتی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/654170" target="_blank">📅 16:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654169">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
اینترنت بین‌الملل در دسترس قرار گرفت|خط ثابت فعلا
🔹
برخی کاربران خبر دادند که اینترنت بین‌الملل در سرویس خانگی و ثابت مخابرات باز شده است؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/654169" target="_blank">📅 16:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654168">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
رایزنی امنیتی نتانیاهو و کاتس درباره ایران و لبنان
🔹
«بنیامین نتانیاهو» نخست‌ وزیر رژیم صهیونیستی و «یسرائیل کاتس» وزیر جنگ این رژیم، هم ‌اکنون در حال برگزاری رایزنی امنیتی در رابطه با تحولات جبهه لبنان و پرونده ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/654168" target="_blank">📅 15:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654167">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSvZk6HB5QtgetoYW5ci9DHuS9j3A7DGQljcQmNEJv_CJ5F5pqf0Kz04gXFCxN1Q1Ka3OFhaBswisxyH6_INIKKHOToECO9Xdrs_5y8wgMt0qaeGj2tdh2AuGCyofXijmjM4Px_zQOZgA_1FCNMR6ic01n8I3EPirWQvBHK484tIGF5EYpmzSc3Un617qBT6LGq-4Iy8Ai3vM_n6ZupJVyrNbLeATpqJt5cUZ25AoYmL1reyFIw58v_84eQWT9cwj8xknoqPcfN2kDayUaP7inDCLPIPx2rblNPsmNg1hTLMhv9ZAWUrL7rjHjISGgjH3jhSHrlNLcpxTe3o8uWY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قانونگذار ارشد روس: زلنسکی در پناهگاه است
🔹
همزمان با تشدید تنش‌ها بین روسیه و اوکراین بر سر حمله مرگبار اخیر به دانشگاه روسی، رئیس کمیته دفاعی مجلس دومای دولتی آندری کارتاپولوف می‌گوید که ولودیمیر زلنسکی در پناهگاه مخفی شده است.
🔹
کارتاپولوف اعلام کرد که حمله به دفتر ریاست جمهوری ولودیمیر زلنسکی و شورای ملی (پارلمان اوکراین)، بی‌معنی است چرا که هیچ‌کدام از آنها، مرکز تصمیم‌گیری واقعی نیستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/654167" target="_blank">📅 15:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654166">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6045f895b4.mp4?token=Zc_OvLBLH4ziKyYkwj4XGCrmxGGeug76rhMDmaIU8BHQ0P67I-I_bsbpTa9WsUbOuEFpTvE8mvwCo07XDe9KvcEffOrFiSYrnC70FLkFg1j7VdGzYzKyApY8ISf7FrJfS9o4Jk-aoQ9GTtYgw5smFSiPVYJUfq-KltUc9LLLlujGJICLccHXDEgCqqjn-ZdOs96QNT41T7R6I7WiKDTxIbLF_MMdiHCaT2WywZjOyrmroITNR4p2gQTG5Osb-QG16ED5hSSc0VkWBIjICwINvqmbFzP0mglUTxnroyRsqB3OT3CCBsLt5DSSP2Y0xAP1P4yK3b0Z-gPoHaZAEilD7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6045f895b4.mp4?token=Zc_OvLBLH4ziKyYkwj4XGCrmxGGeug76rhMDmaIU8BHQ0P67I-I_bsbpTa9WsUbOuEFpTvE8mvwCo07XDe9KvcEffOrFiSYrnC70FLkFg1j7VdGzYzKyApY8ISf7FrJfS9o4Jk-aoQ9GTtYgw5smFSiPVYJUfq-KltUc9LLLlujGJICLccHXDEgCqqjn-ZdOs96QNT41T7R6I7WiKDTxIbLF_MMdiHCaT2WywZjOyrmroITNR4p2gQTG5Osb-QG16ED5hSSc0VkWBIjICwINvqmbFzP0mglUTxnroyRsqB3OT3CCBsLt5DSSP2Y0xAP1P4yK3b0Z-gPoHaZAEilD7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توافق با ایران، حفظ وضعیت فعلی و ادامه محاصره و حملات نظامی سه گزینه دشوار برای ترامپ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654166" target="_blank">📅 15:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654165">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzdqYVgzB7M8VdoPNgU7VGUAj5Mdq95OAK3RzjO1VcuZmnFVehBDT9wHdEAGkkS1HbCgvz1dxeNM-SffEEhY_shQ92kP8Igzl7225x0D0lM0hBKbMpb_iz6eM62V_Lv0-_TeNMQpBtX0N4WFjYFu3c3_BelrO58PAAvbM4-jUV8-179PbxG6gj9EYLkVKxzjZi4YQZaEDHEasT_bs2PgjzpDX6bfc4iqEIEAgXXudHLujHE_0dFyJkqij23w5yfnSpw8R8bIFCP3Ri-u9Lxxezo8us3MahE63dwi1nQW97bR7VyyvlDqIDUebnobPdF7xzwm04NnO2csx_mV7qbdEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برق اروپا در گروی محموله‌های گاز قطر در پشت تنگهٔ هرمز
🔹
شرکت‌های اروپایی برای قطع وابستگی به روسیه، از قطر گاز طبیعی مایع (ال‌ان‌جی) می‌خریدند که با حملهٔ آمریکا و اسرائیل به ایران، صادرات قطر، یکی از بزرگ‌ترین تولیدکنندگان ال‌ان‌جی جهان متوقف شده ‌است.
🔹
حالا قطر ماه‌به‌ماه این شرایط اضطراری را که از ۱۳ اسفند ۱۴۰۴ با حملات موشکی ایران به تاسیسات راس‌لفان اعلام کرد، تمدید می‌کند که به‌معنای عدم ارسال محموله‌های گاز به شرکت‌های اروپایی نیازمند سوخت برای تولید برق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/654165" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654164">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwclS8shqd9-rKbzQAQ1kneVLFVLxcdYhFxkqeArnLmdPUTSnXiuOp1V2i2rj1F2LrmmjbKVmQZXY_84hH9UKkVRR851qX8p5sjr_kpmmeAbUa1ZOtL26ETe4hufKJXkpDR8UKAtGhfFPT5V3z96IqTW_uomSJ1zNPBnH7XF54t17hS9N46C95_j2gtJi_-JPEtmhWUs2CeiacCMCXgD5BJBTl1SdYdppW8fIwqM51Il0duXIv-Dt9Uuax7Ipv1RdH-FEkLVipmIhtws9PgoZ8bgB65FyWIOgVzLd01z33MnOq1c82w5oJenMCzjziuhpjJchVo8pZKtqFAqVcpmng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیر آراسته: از اقیانوس هند تا مدیترانه را برای دشمن جهنم می‌کنیم
🔹
جانشین رئیس گروه مشاورین نظامی فرمانده معظم کل قوا، با اشاره به گستره جنگ فرامنطقه‌ای از مدار ۱۰ درجه در اقیانوس هند تا دریای مدیترانه، گفت: چه جنگ شود و چه نشود؛ آمریکا دیگر در منطقه پایگاه نظامی نخواهد داشت.
🔹
آنچه که تاکنون انجام دادیم، همچون رزمایش بوده است؛ زیرا ما سربازان، جنگ را زمانی جنگ واقعی می‌دانیم که سینه به سینه دشمن وارد نبرد شویم.
🔹
در دفاع مقدس ما تجربیاتی بدست آوردیم که در جنگ ۱۲ روزه و جنگ رمضان به کار گرفته شد و برای مثال ساخت موشک و توپ جنگی بنا به شرایط از همان تجربیات دفاع مقدس بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/654164" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654163">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
فوری
بازگشایی اینترنت بین‌الملل ثابت شروع شد
🔹
در پی دستور رئیس جمهور به وزیر ارتباطات برای بازگشایی اینترنت بین الملل: تا ساعت ۱۵ امروز سه شنبه (۵ خردادماه) حاکی از ادامه روند بازگشایی است و توقفی در اجرای حکم رئیس جمهور صورت نگرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/654163" target="_blank">📅 15:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654162">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به تورم فعلی، مبلغ ۳۰۰ تا ۳۵۰ میلیون تومان وام ازدواج تا چه حد می‌تواند در شروع یک زندگی مشترک «گره‌گشا» باشد؟</h4>
<ul>
<li>✓ هیچ فایده‌ای ندارد</li>
<li>✓ در برابر تورم فعلی رقم پایینی است و تأثیر چندانی ندارد</li>
<li>✓ نسبتا خوب است، اما فقط بخشی از نیازهای اولیه را تأمین می‌کند</li>
<li>✓ بسیار موثر است و کمک هزینه مناسبی محسوب می‌شود</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/654162" target="_blank">📅 15:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654160">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بانک مرکزی: وام ازدواج ۳ ماهه پرداخت می‌شود
🔹
بیش از ۸۶ درصد متقاضیان وام ازدواج موفق به دریافت این تسهیلات شده‌اند
🔹
صرفاً ۱۴ درصد از این افراد در انتظار اخذ این وام هستند که با میانگین مدت سه ماه به متقاضیان پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/654160" target="_blank">📅 15:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654159">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOVbZgftAJTnO2XBFuDYjqZss80hkA01y-hT1Vf7HPwu-DeLCGfULv3ykBKe20NrEpQgk0HjHiIpFRkahhU_7ZSq07aBDUaS-8rbWs2OZ6e4cNgPm3lzykeS0h2r8uBTko_XUTQdVsRJg6v2EdDeFziLJPXF3Aw9qgM0FnobwjD3J2ddeOiVK08sBHlkjtzxoeaAD9a2-ZzBNhlN4w9SX37uK1sj6x4SKEaNgVlqKPthm8TOgpzotfC30Hh3UnR7Pglz_anJY77tcWFb7P_Y2xEGMoXM0wSZ55VZ6GBg6UaKYenvghFExBJkWOX2hgci5GvjrdwRzEqf6PXywtC6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: نقض آتش‌بس توسط آمریکا بی‌پاسخ نمی‌ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/654159" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654154">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0efaaad45.mp4?token=l3oGA7QSa0JmQPzr3lR2VGFf0Ptx15_fKztsSsYJt4iTfbZuzp8WPomw-5cBPptT14FQ0-KgpE2WPKI9ExeRY8mbAxYCeeOrDJf2WWFA0H9n9z1kvSoRSYDfPBOR4W-kDNHTUlg2FsseucD_L4BcMx0UWo8h3H9UE4nXjhHS4q94J3a0Xy33gnDbGJ9HnZdXq2USfvsb4VqCoiIAE5RU_efwNIBG-uTjja4A0wDO3bMoqlPm1fSUEtwXrq8fzf9z93coKwKLMJiNZKMFssgsyMt_pyMNue--fcrQbyNoDMddULLA0LbbDwYZCbYLmYNsJb1mYVD2ympc8fwe7m8Ywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0efaaad45.mp4?token=l3oGA7QSa0JmQPzr3lR2VGFf0Ptx15_fKztsSsYJt4iTfbZuzp8WPomw-5cBPptT14FQ0-KgpE2WPKI9ExeRY8mbAxYCeeOrDJf2WWFA0H9n9z1kvSoRSYDfPBOR4W-kDNHTUlg2FsseucD_L4BcMx0UWo8h3H9UE4nXjhHS4q94J3a0Xy33gnDbGJ9HnZdXq2USfvsb4VqCoiIAE5RU_efwNIBG-uTjja4A0wDO3bMoqlPm1fSUEtwXrq8fzf9z93coKwKLMJiNZKMFssgsyMt_pyMNue--fcrQbyNoDMddULLA0LbbDwYZCbYLmYNsJb1mYVD2ympc8fwe7m8Ywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش اسرائیل آماده یورش گسترده به لبنان می‌شود
🔹
با تشدید درگیری‌ها در جنوب لبنان، منابع اسرائیلی از احتمال بالای یورش گسترده ارتش این رژیم به مناطق گسترده‌تری در لبنان تحت عنوان عملیات ««تیرهای آتش» خبر می‌دهند.
🔹
طی ماه‌های اخیر حزب‌الله لبنان با ریزپرنده‌های انتحاری مجهز به فیبرنوری (FPV) توانسته ضربات دقیقی بر ارتش اسرائیل وارد کند؛ پهپادهایی که امکان رهگیری آن‌ها وجود ندارد و در نهایت مقامات نظامی و سیاسی اسرائیلی تصمیم گرفته‌اند به زعم توقف این حملات، دایره تهاجم به خاک لبنان را گسترش دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/654154" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654153">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c07ac5071.mp4?token=aEpGh0KbRibUprsFeZL92fu0ATE_H9bRioCMPc9SYinIHIbQl8rS1eyDjRBynCd7iTeRT1nBJQlhF2qLDpzWw6bPaQzm-R_S2wnuOfJhIpvR29nHhc2NdhlMNlhDjInmHAhebpDHC1a8RdbFfsdkmVvBvUXkFRZQZkIDsFjaWIi6SZQsaIePgMsAdOpUlq9skBD-JcMl_ryRDlS2wUbyySRIF5xx1wztOqUoV1ArrMN7n3fbvNNjGd1C88I15HzmtINSFJZ-qvxn-W-k0-V4C_m0_ra8MqghWZNgV7j-fUILvn4rb7fqvinkr9teRoLShl1anGlPT2g-AVj07fFz-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c07ac5071.mp4?token=aEpGh0KbRibUprsFeZL92fu0ATE_H9bRioCMPc9SYinIHIbQl8rS1eyDjRBynCd7iTeRT1nBJQlhF2qLDpzWw6bPaQzm-R_S2wnuOfJhIpvR29nHhc2NdhlMNlhDjInmHAhebpDHC1a8RdbFfsdkmVvBvUXkFRZQZkIDsFjaWIi6SZQsaIePgMsAdOpUlq9skBD-JcMl_ryRDlS2wUbyySRIF5xx1wztOqUoV1ArrMN7n3fbvNNjGd1C88I15HzmtINSFJZ-qvxn-W-k0-V4C_m0_ra8MqghWZNgV7j-fUILvn4rb7fqvinkr9teRoLShl1anGlPT2g-AVj07fFz-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپاد آمریکایی زیر پای آرش‌های کمانگیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/654153" target="_blank">📅 14:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654151">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شکار یک مرکاوا و یک هامر توسط حزب‌الله
🔹
حزب‌الله: یک تانک مرکاوا و یک خودروی نظامی هامر دشمن اسرائیلی در دو عملیات پهپادی صبح امروز منهدم شد.
🔹
در شهر «زوطر شرقی» نیز یک بولدوزر نظامی طعمهٔ پهپاد انتحاری شده و دو تجمع نیروهای رژیم اشغالگر هدف توپخانه و موشک‌ها قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/654151" target="_blank">📅 14:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654150">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ارتش اسرائیل دستور تخلیه نبطیه را صادر کرد
🔹
ارتش رژیم صهیونیستی با صدور هشداری دستور تخلیه نبطیه در جنوب لبنان را صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/654150" target="_blank">📅 14:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654149">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e062176e2.mp4?token=oO-1Bt4Pm7ew00fBRKJS5zuBTNZAxRR6NW1kA-n7FSEQASCiG4tYI23l6LXpSZ1uGKmcQuThqrVh-kTtNhMc97FF758Yllmv639iz15vmQBrXzQ5AC2pSql5GpmmqzU8A7_CSI_p0lIJnkOwB5X9i6THh1pvDKroNeKAOK2Z-aoHUy_PJeHjANX6Ac1BPbSztJqgMPOsqk_XDoGRoDuXq2zClj9kgkWwA-qsAzUHQR8uLGHYkwqB3FiWvALHi0-LwIunIQEo5VEJnIoDZj1DJSmJ2lIr_qXLBPm6l5tBuy69WSiA37CsU7mOzRwWTlM1sUy_oQwttIvv_NlN8D5lyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e062176e2.mp4?token=oO-1Bt4Pm7ew00fBRKJS5zuBTNZAxRR6NW1kA-n7FSEQASCiG4tYI23l6LXpSZ1uGKmcQuThqrVh-kTtNhMc97FF758Yllmv639iz15vmQBrXzQ5AC2pSql5GpmmqzU8A7_CSI_p0lIJnkOwB5X9i6THh1pvDKroNeKAOK2Z-aoHUy_PJeHjANX6Ac1BPbSztJqgMPOsqk_XDoGRoDuXq2zClj9kgkWwA-qsAzUHQR8uLGHYkwqB3FiWvALHi0-LwIunIQEo5VEJnIoDZj1DJSmJ2lIr_qXLBPm6l5tBuy69WSiA37CsU7mOzRwWTlM1sUy_oQwttIvv_NlN8D5lyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جولان صهیونیستها در مسجدالاقصی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/654149" target="_blank">📅 14:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654148">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_xxU2Gc-Bl8J2F0o1p7GCnxAuP2rEnb7H-hPJQRnvkr51NZ8tF106lf7tN3mIecnaddiHsRWw_pusYuGnlS_HgUFFr5rtOTdxW5OTeL8wHYqWIgMGUz4l07sTRp6odaJIwBfUmWo9yoylea1UWzVF-4TcyE0xvumlYv9egz7EMrTUNxDWBlAO_gJFBC4WVWKjTY_dDF9vcRiDFTwPoa4xSFrQvG95fXvxm02z82fRjmUFw-CL86hIKwmz55Ca53jdRDt8cq7MBkRa4DpwKW3aWillEHvN6Dfw5os3UZEQRlvcPVpZUOXEV5K3xVu6fmyMRUi6BJP1_NT113e8zbCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: مأموریت این ستاد تنها در پیشگیری از افزایش قیمت‌ها خلاصه نمی‌شود
🔹
معاون اول رئیس جمهور در نشست ستاد تنظیم بازار:
🔹
ایجاد نگاه جامع برای حمایت همزمان از مصرف‌کننده و تولیدکننده برای دستیابی به پایداری اقتصادی، مهم‌ترین مأموریت این ستاد است.
🔹
معاون اول رئیس جمهور با توجه به چالش گرانی، بر ضرورت ترسیم تصویری دقیق از ریشه‌های تورم تأکید کرد.
🔹
برای برنامه‌ریزی در جهت مهار گرانی، باید سهم عوامل داخلی، خارجی و اختیارهای حاکمیتی به‌درستی تفکیک شود.
🔹
عبور از مانع‌ها و دستیابی به ثبات در بازار، تنها از مسیر استفاده بهینه از منابع و ارتقای بهره‌وری در همه بخش‌ها میسر خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/654148" target="_blank">📅 14:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654147">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f434bd9b85.mp4?token=ruNVNzBS5SBPTS0taM2AzbuD031lm7-GcvHqg--wPRc9SVlfsnWv9zRlVAv_0DhZPO2sBvbHfSFhCr_lzcNIweNWBsTMJTJNNpT9uBlmahVBmvDPsFwnK8oKVzY_amWMUX_CAPqkP9WpHKqYnDT9q4bc5vGkuCuopLSAivtXQmJ8Tqg5asm1BiVpYZ4klFxs3aVDy1kWlGVmk55u9IqrxrvgxhioprhwSeddSFd4qc8gaeqetB7FzEj_ecylMS__3IDO9XjFAUOK0E2kcoA2YMa0gYNPBQ3SLwqw1115fhFty4V-FKsZYcxR3JmyfcfEAx0FwzmvXjx1ZSR38LuBRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f434bd9b85.mp4?token=ruNVNzBS5SBPTS0taM2AzbuD031lm7-GcvHqg--wPRc9SVlfsnWv9zRlVAv_0DhZPO2sBvbHfSFhCr_lzcNIweNWBsTMJTJNNpT9uBlmahVBmvDPsFwnK8oKVzY_amWMUX_CAPqkP9WpHKqYnDT9q4bc5vGkuCuopLSAivtXQmJ8Tqg5asm1BiVpYZ4klFxs3aVDy1kWlGVmk55u9IqrxrvgxhioprhwSeddSFd4qc8gaeqetB7FzEj_ecylMS__3IDO9XjFAUOK0E2kcoA2YMa0gYNPBQ3SLwqw1115fhFty4V-FKsZYcxR3JmyfcfEAx0FwzmvXjx1ZSR38LuBRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر: آمریکا در جنگ ایران شکست خورده است
🔹
نظریه‌پرداز مطرح آمریکایی جان مرشایمر، به شکست ایالات متحده در جنگ با ایران اذعان کرده و گفت که واشنگتن  «نمی‌تواند راه‌حلی برای پایان این جنگ پیدا کند».
🔹
این نظریه‌پرداز خطاب به مردم آمریکا تأکید کرده که این شکست آمریکا تبعاتی منفی به دنبال خواهد داشت که همه مردم ایالات متحده را تحت تأثیر قرار می‌دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/654147" target="_blank">📅 14:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654146">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS5U-oOVFf9pnIzwEloEhsdp5DURqYftzcra5yJ6oPnvZ8luH0CdiJMQEV-3xYAFzO7Sq0Jl7jkA4kQnTjLRIgZNDkfw9SLlnCYVAax8oAkF7X9dtL2CEsod2ODM2l8FtiJkLOD3UEyytlsdoaV70qtDEODyLn-VyhbHa-1-1R-o7CKDaBSGbcDk8zgnM3yF7b_15OOfntxnDHHOOBWk3PklCB_Blifp-X0Z60eoyV3olPNs6oVUsZzBjthJaIkhaxJxbWgJg3FUrYYB4euGC99_tO9QGSIrfgZKjjRohMU19UYGMJcwNxSPjkanOp35OySQbftU804yFq8DZW02XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چین به نقض آتش‌بس توسط آمریکا واکنش نشان داد
🔹
به دنبال ماجراجویی‌های اخیر آمریکا علیه ایران در خلیج فارس و تنگه هرمز، چین از «طرف‌های مربوطه» خواست آتش‌بس را رعایت کنند.
🔹
مائو نینگ، سخنگوی وزارت امور خارجه، در یک نشست خبری گفت: «ما از طرف‌های مربوطه می‌خواهیم که به تعهدات آتش‌بس خود عمل کنند، اختلافات را از طریق مسالمت‌آمیز حل کنند... و احیای زودهنگام صلح را ترویج دهند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/654146" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWtttpsCql-gD6pycc_DFP0uAJG-Ob9QYDMxSIsDVo9JenmgUL00DQZtmzWVA03woWWdQjdcaH952VKK6vqmNtXRPBMB76VJxYVS-O3PnNTCHRWXriHWtoi0UqBRUduddgCcLCVPAxR2p9YaFDyGL2We5jrBPiMPbs1R3Gt_HCKCv0CyTRsaNRVp5a8fmhkm4u7ZdQBNJ7OHaLSVcWtjMmcU2SE7BRT0OjCSAbNIzBtx7c0KR-x3L6cB5rke5jGVrZtA3BTw4znQPq8nx58ZAH2POGV4PYofq9uy2l40wPAOjue7-C_D1weM2cMZcPVboJ_N4rYaWIBcuNOC82-ZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از شوخی اینترنتی تا موج سیاسی؛ ظهور «حزب مردمی سوسک»!
🔹
فضای سیاسی هند نماد عجیب و غریبی پیدا کرده است: سوسک. این نماد نه نیلوفر حزب حاکم هند (بی‌جی‌پی) است و نه علامت دست حزب مخالف کنگره، بلکه «سوسک» است، موجودی سمج، منفور و به‌باور بسیاری نابودنشدنی که به‌تازگی به نمادی سیاسی، غیرمنتظره اما قابل‌همذات‌پنداری برای جوانان هندی در فضای آنلاین تبدیل شده است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3217224</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/654145" target="_blank">📅 14:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
منبع آگاه: هیچ مذاکره ای بدون دریافت پول‌های ایران امکان پذیر نیست
🔹
یک منبع نزدیک به تیم مذاکره‌کننده گفته شده آخرین اختلاف جدی میان ایران و آمریکا بر سر آغاز مذاکرات که مربوط به نحوهٔ دسترسی به منابع مسدودشدهٔ ایران بود، با میانجی‌گری و ابتکار قطر در حال برطرف‌شدن است.
🔹
براساس این گزارش، پیش‌تر آمریکا نسبت به اجرای تعهدات خود در این زمینه عقب‌نشینی کرده بود، اما ایران با پافشاری اعلام کرد «تا زمانی که پول‌های مورد توافق واریز نشده باشد، هیچ توافقی ممکن نیست». نهایتاً با رایزنی‌ها در قطر، پیشرفت‌هایی برای حل این مشکل حاصل شده است.
🔹
با این حال، تیم مذاکره‌کنندهٔ ایران با توجه به سابقه عهدشکنی آمریکا، این تفاهمات را تمام‌شده تلقی نمی‌کند و بارها اعلام داشته که «ایران برای همه گزینه‌های محتمل آماده است».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/654144" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ct12WSAVWmN-G3UhUgrMHKCYwpm93jQIdf48GxWJV0uraLct43GeIQpSoR-bhy01zL96xp3mq_vGurcu1bGg115SUc-yiHW6WhbKbiHGxAnBcih_QzwRE3Z1Jyfh0K4poevTXWr34YxsM6MSTEILfoYxbJgBsoT3D_j5cS2x0-Ndw-ifsXvWT69MwLGS1tS1g8rbtH8qUO6R51YhXo3_qjvNXBUcLCpqhDpetfBu1ML8VyygE2ZHtV858_FIMJq6exVgfQIewhIGYACcD76KFyExTyLjFuw_imLPoG5bnLaJTfAhtxe3ltir4JNFJc4nLO82XoQ8r5yUJgNx-d9l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیام الله اکبر
رهبر معظم انقلاب اسلامی در پیامی به مناسبت برگزاری حج فرمودند:
🔹
با سلاح الله اکبر بود که ملّت مسلمان ایران در چهل و هفت سال قبل قیام کرد، رژیم طاغوت، دیکتاتور و وابسته‌ی پهلوی را ساقط کرد، دست و پای امریکای طمع‌کار و مستکبر را از کشور بُرید و نفوذ صهیونیسم را بکلّی قطع کرد. ایشان خاطر نشان کردند: رژیم متزلزل صهیونی و غدّه‌ی سرطانی اسرائیل نیز به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگر ده سال قبل رهبرعظیم‌الشأن شهید قدس‌الله نفسه‌الزّکیّه، بیست‌ و پنج سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله. به همین منظور، خبرفوری طی فراخوانی از هم‌وطنان خواست امشب ساعت 21 در هرکجا که هستند، الله اکبر گویان، سلاح اقتدار را به دشمن نشان دهند.
🔹
هفتصدوشصتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/654143" target="_blank">📅 13:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5482e0431c.mp4?token=dXC_hipxjDDIft44jsckFBTk_K9XQxmr2HAeTnvh_DvzKV0Ojy43slBL9yjJhvc2D_dr1hbNpGWy1uwGH_iaHkvChIifAy-aKWrBYXS9QAW_vBkFkxU0QiGMdFJYOTUUd5xNQw5ZlXjFMzwx4QTNFxY6lLCkMURPajA7pyE1o-ObDM8k2PphbfhSm3HtsSiwe8IE-nhpPDp1c6uNENB71tyOB_JtmVOgbphBkbIYAGyJPtMtsRU5Y4ZYwaCwBuny-R5kUondTmLSMgx_wnroCrzkx8ul9MlOu7Xc3bXgS-VvapbF1KBBACynTDzzUlk3DGWFUXCnHMwIXRBY4T09dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5482e0431c.mp4?token=dXC_hipxjDDIft44jsckFBTk_K9XQxmr2HAeTnvh_DvzKV0Ojy43slBL9yjJhvc2D_dr1hbNpGWy1uwGH_iaHkvChIifAy-aKWrBYXS9QAW_vBkFkxU0QiGMdFJYOTUUd5xNQw5ZlXjFMzwx4QTNFxY6lLCkMURPajA7pyE1o-ObDM8k2PphbfhSm3HtsSiwe8IE-nhpPDp1c6uNENB71tyOB_JtmVOgbphBkbIYAGyJPtMtsRU5Y4ZYwaCwBuny-R5kUondTmLSMgx_wnroCrzkx8ul9MlOu7Xc3bXgS-VvapbF1KBBACynTDzzUlk3DGWFUXCnHMwIXRBY4T09dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزدوران و عوامل وابسته به رژیم صهیونیستی بدانند هیچ حرکت و ارتباطی از چشمان تیزبین پاسداران سازمان اطلاعات سپاه  پنهان نخواهد ماند...
🔹
پاسدارن سازمان اطلاعات سپاه با رصد شبانه‌روزی و اشراف کامل بر تحرکات شبکه‌های وابسته، این عنصر مرتبط با رسانه‌های معاند و اسرائیلی را شناسایی و در عملیاتی دقیق دستگیر کردند.
🔹
امنیت مردم، خط قرمز مدافعان ایران است؛ و هرگونه همکاری، ارسال اطلاعات یا تولید محتوا برای دشمنان این سرزمین، زیر ذره‌بین سازمان اطلاعات سپاه قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/654142" target="_blank">📅 13:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKihuWNs8Y-3DMxkDoIV3d6MQof_pIYeWdsqvdPiNlI1vOAa8DQn0lULYigOLCCz2_ndnTlhuI1LA8N8VvCil53h56FrLWxl79C0E-C2Ar1I1bsSe4GW9gvaiEJvNfOjmvfqVtdfIt3jmnUZPvBa-c-lU92Sh0ayIQbpU2hWJ4H5v2jhCYW_N59PbthCayvz__ALl8cwDE-9rlQitlu2LmIxOPKGAxUtt0OH-aiK3MLgopGJlhJ_7i85rUYYIxLPXzmOWbxGunsofrzu-YXKhD_axfussYEfzPIz9IjPasvFIHXh4f0w02cEvm5RqgF7FZ0CCrpCLi2DCPVLearWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت سرباز وظیفه در یک مرکز ایست و بازرسی عقدا در استان یزد
🔹
سرباز وظیفه محمد معراج نظری در ایست و بازرسی شهر عقدای اردکان یزد در حین انجام وظیفه به شهادت رسید.
🔹
محمد معراج نظری در حالی‌ که در مسیر پاسداری از جان و مال مردم و تأمین امنیت عمومی در ایست و بازرسی ورودی شهر عقدا مشغول به خدمت بود، با ایستادگی در برابر خطرات، جان‌عزیزش را فدای میهن و امنیت مردم کرد.
🔹
مراسم تشییع و خاکسپاری این شهید عزیز، روز گذشته در اردکان برگزار شد و مراسم یادبود این شهید هم روزهای چهارشنبه، و پنجشنبه و یکشنبه هفته آینده برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/654141" target="_blank">📅 13:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654140">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GL0boQGB72py5HYfQ6cMPF0hxeOPXT-fnweYCvCHDgHWlm12h2RRMIkFFvUdJos1EHGg0ntKxT7FSwDOKRaA50jEBH21UTJNGI6lFTl-fPLLBOymlZr_aZdjgfhX39zt5EtXzaWAMzLR79cmKto2mx4_B74mh49Cl60GJ6-8FIsbXsK0rzYjxn70Q5Yo-PlVAO3KTkBxOg6MUcgyehm7gF1vTodgrkSn-lHwcztZm9gMH-SiJiB_CsYtxyYUgCXQ_ee0GraqzdR76gMa52bDKH6qF0p5oDLYPcpVpRUxB7E4qU6ukWslqKPfTwf3zQIUFYiSUQ5rsraqD5dL_ny0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امشب ساعت ۲۱؛ ملت ایران فریاد «الله‌اکبر» سر می‌دهند
🔹
در پی پیام مهم ولی امر مسلمین جهان و تأکید بر وحدت، مقاومت و فریاد بر سر استکبارجهانی شیطان آمریکایی و حیوان دست آموزش رژیم صهیونی، از ملت بزرگ ایران عزیز دعوت می‌شود امشب رأس ساعت ۲۱:۰۰ در سراسر کشور،…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/654140" target="_blank">📅 12:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-654137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKrhn0B8G47VBbQJZcrCEYblmLTcmi-zj8i4C_UR6x8K6z9YK6sqFV0fmyHiM7RiA2JZ2pssJ3-G5Naof5GB4YL5ktA2LoE8CyyRR7B_Ra6uqwOFlrEfUvECc11b4Li1F4buhbfZUhQCT-57Ce2PWoH8jTIKTAGEHctkzCdOOnRYBnsNHwJTgRcKnAvoDpibAh2bHO_99hur6W9i2ZLZYvhKqI0QXoTDEu1u6AfRCOsjEZ-VTS03x1wleab4XmTP7vLeptFqLV25Q_Bcv4IA8y9gtqy-BCMl1d8AYiDOLbV3ySxHKxa1kYckP6j4RYfcGzcUEyZEwLM5aoWvLx8_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امشب ساعت ۲۱؛ ملت ایران فریاد «الله‌اکبر» سر می‌دهند
🔹
در پی پیام مهم ولی امر مسلمین جهان و تأکید بر وحدت، مقاومت و فریاد بر سر استکبارجهانی شیطان آمریکایی و حیوان دست آموزش رژیم صهیونی، از ملت بزرگ ایران عزیز دعوت می‌شود امشب رأس ساعت ۲۱:۰۰ در سراسر کشور، بر بام‌ها، میادین و خیابان‌ها ندای «الله‌اکبر» سر دهند.
این فریاد، پژواک وحدت ملی و اسلامی، حمایت از جبهه مقاومت و تجدید عهد با آرمان‌های انقلاب اسلامی است.
🕘
زمان: امشب ساعت ۲۱
📍
مکان: بام منازل، میادین و خیابان‌های سراسر کشور
الله‌اکبر
🇮🇷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/654137" target="_blank">📅 12:19 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
