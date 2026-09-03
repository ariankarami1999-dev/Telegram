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
<img src="https://cdn5.telesco.pe/file/UtTh4SnhwovT9HG_8sxaAXeUXHG-EsVkleVMYxtXqU-mMr7FNRbD0890UpZ4N4Sr5W_6edr04Kh3xmNnHW_egAf380jLNWETFSMeIzbyfzo8E5dkj756DxwWbMNB_lFcGY7uvwSeu3-TzoT66sovNuegEV7G5TgSnhZHZ6mYSSWzQuetTRh12KusE8PQefEeXUpRbGJtD_ZwTj_4GUnclmBnv-wwqJ_VVXdLLgRgB8xSvj1ULcuBbZXOE0Ca62s_j6I1v0JaIc-o-84QDLeuE8eP4dfIvBn5EDJv0IT0b8aoxuhgkcAaIbNwsimJOT0-q1BNhe4h3UhASRYIBDKoUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 429K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 20:53:28</div>
<hr>

<div class="tg-post" id="msg-105456">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
⚠️
دعوای خیابونی تو شیراز که یه دختر به ماشین پسرا زده بعد میخواسته در بره و ادامه داستان...
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/105456" target="_blank">📅 20:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105455">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=i9xmHxozlAZqh2ZptRSL2Q9spKGKsoGmcuLmzIbRnbpBvmM-7yD_-kutPiPA0HQJFVroVrOcSm0DECadOy8rdFLbaNnJ2updwdt01Ttr74dgWaTyhAtEShr1osV4j-j55qnuYf0gg0Z9QmUR8AWBhiSaGXYLhfH5BW3LjwkxkBAK3kQywl7n13Smo5abD3PCX2mKHyoScGW1HIvKOfbSTJJtSV4gfmwNq0jsw-ULcODR05VVPCx7ie8bY8xOXLZbr3RDOKarn0lXPE_AYZXBMdEg-iJOv_k6l1AhYdhoSKSPEEBGPQCUZsVmkcDBQzRDnWH3zfWSF5QxvygSQCqgl1IIrAU3c-baGlEP76CVpUnrbOxrNNIKa5ViS2_9cgw_xG-n9YN4CKuWTVsL1NC8SBtdIFJfD0vTvm4TuSZonqPKe9JTa8Lmjlnoio5brxm6xELRILwQGUbELlRmlYVd-Fu-VT-5ctzm-5-XQCUof2rPyvpSMb2z1GvCN7ZxdfY1rDFY0XhP0ubY9YJd0o0YHpKX9GoMu-XZhJiyjo6wrgTawDOEvJpiKO2AORXe-0flDsViGk6_wTZI8pmjG_kXzE7YgUs5KL0kDvEjtMIhf9o1lSfjh4JkoUAHPGMZTM-en5dF9bCdFg2moIhbQ7uvcnRfV98quIbq3scTeaWdNgo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=i9xmHxozlAZqh2ZptRSL2Q9spKGKsoGmcuLmzIbRnbpBvmM-7yD_-kutPiPA0HQJFVroVrOcSm0DECadOy8rdFLbaNnJ2updwdt01Ttr74dgWaTyhAtEShr1osV4j-j55qnuYf0gg0Z9QmUR8AWBhiSaGXYLhfH5BW3LjwkxkBAK3kQywl7n13Smo5abD3PCX2mKHyoScGW1HIvKOfbSTJJtSV4gfmwNq0jsw-ULcODR05VVPCx7ie8bY8xOXLZbr3RDOKarn0lXPE_AYZXBMdEg-iJOv_k6l1AhYdhoSKSPEEBGPQCUZsVmkcDBQzRDnWH3zfWSF5QxvygSQCqgl1IIrAU3c-baGlEP76CVpUnrbOxrNNIKa5ViS2_9cgw_xG-n9YN4CKuWTVsL1NC8SBtdIFJfD0vTvm4TuSZonqPKe9JTa8Lmjlnoio5brxm6xELRILwQGUbELlRmlYVd-Fu-VT-5ctzm-5-XQCUof2rPyvpSMb2z1GvCN7ZxdfY1rDFY0XhP0ubY9YJd0o0YHpKX9GoMu-XZhJiyjo6wrgTawDOEvJpiKO2AORXe-0flDsViGk6_wTZI8pmjG_kXzE7YgUs5KL0kDvEjtMIhf9o1lSfjh4JkoUAHPGMZTM-en5dF9bCdFg2moIhbQ7uvcnRfV98quIbq3scTeaWdNgo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
یه‌گل‌بخودی جدید در پریمیرلیگ ایران در بازی فجر سپاسی و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/105455" target="_blank">📅 20:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105454">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKNSAgewS1SkTyGdCjQHfoXNHjnnz9bRtiCF4Y1jRY9yJt9-fTuApdRjHj7VuhCFbDPeJ4j6N1MEMLd3lGqsizSOsIkU_RW3Lrb1btVUaqJqrTbDpsaQRCyUXLSpNGlNDnnQ62zNNJ5b3fDEGuZiA5NOt5sv5VnbW5Z9IJaBTYuk66bPZEOI6iXjO8cKy9CMSy3PTQB1jYthlYrDR0Tw-a8d2eWRM9xjkS5xli487kb7f1A7hqme0KUeVibQS6UQF54XqWhJtyltEim1DwbOc_mR-m5lBA2osHHqPscGZ_5O-_fIEmenBe-7qLfzBHBWjV-mklWHfsd6Y-zFZrmkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مارکوس یورنته پس از قهرمانی با اسپانیا در جام‌جهانی از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/105454" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105453">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESPlj93YTS_si3U_B2xc6E79htAmChtWMMjtR8uDjq4QNzD8qoFZ7kqPGyAaui3D9u7TZ7Wbdgtmp_OUd6DGs3XnAdkWB7D9ojlHsT1b74YHphmJFDQ5gbhzKWalfsTVbZ_W4mJhVsati1lDSwbxtTIMezPjGVhZ_zE0QZ9HreX1GHhJlMNVyNNFkwhZPh6lYuGu1PgQITFA1b6l8DUQw8Jh5svRa3irQTUtTYvuY6UW6yfKRNF-aNEb65qhBVA3_5vMmpY1-2AaUxbBliPde-gYDA-58xIbuI4KZVBMnPikBWgpFrkh1fFAqN_Cn8TUoohe1hfxFPi3SG1lXYaNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇸🇦
رسمی؛ گابریل مارتینلی وینگر برزیلی آرسنال با قراردادی 4 ساله به الهلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/105453" target="_blank">📅 20:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105452">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCJwUjNA0oGeYmCOMIg9K84fnLMESNcnsiag8UMhFSIBF-IL6YiYrKFVxqMPSCON-akc7KeujSixsRQc1XkJxU2cg4nv7ULaGIeSiRtEvtcDxQy4J29napbqlyq5wE3euZ7ZZWUYl3rX7KEomeHcJJP8QnLZg5LNQb1t709ZWQicPFw9gW14N4TPsQ7m9JPjiuO47Dg90iDH8pGQmmGOPVZosDr2uImWCKP8_Lb2IeIfK3zNA40CE8uqDu6MDygtadq5aE9u0UKEOhmFX7fVjhU2Aa4T1_fW7fR0q0o87i5cylQJ6Av9QHlCjzjpDXNIABtAUQF8xokR-Kd_RRAsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✍️
کوین یامگا، ستاره سابق استقلال و نساجی با جدایی از تیم الفاسی مراکش به کونگ آن هو چی مین ویتنام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/105452" target="_blank">📅 19:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105451">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8qvLQLkrHU9qeAk0CE1RGeyoHyGzC8rfjesAjvSalW8wqYMCk5D8tQkCjBUTk922jRVJ5AVwxKEQ_s0ZXOWeUbeyDM6uaPMFKOsWtXRi7HrxNrJhAPQlDsMy8zW6GQPSyvQ0GTTE8t95qHq9vTabRnrlYJi3JznVcuR6fRkDX4jZL9qggzrR0FKRIiN4XC0SP8MkZy2_jxlXZB-jZrSaDz2ridP0xCFDmwniXqEvYEDNEDlA_SBX2ILopdevcVc4iTri9RwSM0f-d4fSp4SkucJxNB0dYOOMESpsB1s29a0cNONC8l6v7s6zRmUDzugT6CBVKXQTzyKfZs0BRlIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
گرانترین نقل‌وانتقالات تاریخ فوتبال
🇫🇷
نیمار از بارسا به پاریس—  222 میلیون یورو
🇫🇷
امباپه از موناکو به پاریس — 180 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو از چلسی به سیتی— 145 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک از نیوکاسل به لیورپول - 145 میلیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/105451" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105450">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZAfxso1Hr74Zl3M8CsCBPyMSKfg2OfuABDBYztQUpcn-pmPUXIZWE24xer5I8djoaLzCgCsiShYgeUgGyJ-e-gcgzFr03eZuj8KMtJ5BEn5nNlAwZswsuB3xrS0XVFebKLC3MjDRPjpsq0Y8xPumMASVqr9H1IS62A4b0Fy-1cJJdSwuadR61vazXoLUcbv7hcZpUPpgA-5GS3lFtchv9caDtb1WbpSDdmQoyzmJ5aT-q1poz0J8C5CL0STZq0gaxlpnTGyjPYfKsomZ8wKs1WwMv-tL_Kwi9CKfDxPUAyWBatGFdFZXdgJeYhRqhR-6PBUJERWaqh5VWm6ZWk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلامی می‌تونست تو این صحنه گل برتری استقلال رو بزنه ولی یهو از نوسان قیمت دلار سردرد گرفت.
📱
«ℳ𝒪ℋ𝒢»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/Futball180TV/105450" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105449">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egHEsKxRZh6ek3hzTP3Wyr5JZRita-bWmrdIuCEGhxyASFmI7-KWkWbfhXO9WAvTigYYsxMP7rOLg4G-8_v5PtvMqWIEKRNmjFc5iG3rLKV-vVjL-0IuOsL9RFkbY3TqBNZsnGGxsTov-U4pjBAMX_zy_H62Xufsd47DlltFcisTy-DqlsopURP7GjFX9baUlKxsVwBGbKswLRq_smXRpw6U884c6PyKo_jerfVps-YkwrD1Q-cYPH9jgfmWs50M6Qi5j1xtwQUXhjCxlOT9hXiBtghblqOTO0MprGHH4NlEbARjV4mudaqpDFEJ_LRrL0VZS7ZPQQByWQJR5y4fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد خط‌حمله بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/105449" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105448">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYT2O3pdXFNcuKVS0YKnWxsOUNMUd4wDvS1CYotLvYU9no8_QT3lYvDxoKOQsEZrH50mNddoJIs28Ox3O63BSt1uyvVZA9qc93wTwVdvNRbZNLZPqlYYnYTECZaUrkyXVXYZobKojtotzojWBN65YRdTS4AgCjtIIw6Jwf-2ESrwthitf1ksNvZMgocbryx0VXARwn8mZAlvFifUtIx8Adobp9EdhKWvFil_zkK4YxTk7Am8E3qC9OaMo2Lwto2ejrDBna4w9GfeAUt88RH4HzBLY9sPJcpRKtmc_xqosNMbQWQMnhSx3ORHR5jMYC94OUqShF-ZMIN7wY-xbZ003Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
آسنسیو مدافع رئال‌مادرید از اتهام پخش کردن تصاویر لختی یک دختر ۱۹ ساله اسپانیا تبرئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/105448" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105447">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r49RZuwrCKGGquZQLBV2RCwBWcDxjDnomGXP9FpnjPiYNKnmihYiAZcRXwNKIR4DXEcAF-wS6sIxXq3JiWsxnUApGRj4rlO_5180uqy2aPyJt_e7WJ6ClELvqE0Ob40fOoSv5fMi0DN1ZSEK_KDsj9DZcVucXSaPM26BCgzmWI2GfuqoEluPmzVizoUXiiNXiKI2aXQ_T_MAquW6nklq8NE0CaFPritl1DiasgtvQpPJ2PhjSyQRID8zM6dFhLngnnqSHDntpm9UDrPLgyL24BHq5tnmnaWVxcxuPQXsk9IWQ514RlblmBA7aZNIcNijQqgodn54TehIiYY19Vb_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
😳
ترکیب منتخب ماه آگوست بارسلونا چیز ببخشید لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/105447" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105446">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=CNjjxnxFQEgeDPln4Ua103M-Eeihr80wnigvYFugihjcsTZ8uOFLI9fPQr_tcngRCmP8WsI9GHh1aCiUlyTlfOu2Bcm2Ty8Gyoh26oCznuL0vnXCtUuwoAZ2J7okPMd1OjciHsaRPQaLPtKoiRmM_mrb95vcYA96CufbATIcwtpZDAY7Wq3AINhIHDWeiywi9uOA2cL9jj0SlSTXubvjeE8rxIiAIGzyOUC6AlyMlEa5xE-UliFSWiTj9qKM6f637vGE9iFEfRIJnISW2NkuZBH--cAzT6kUn2ThLg5ssEUAhhd4YtlTlumrm3l9effGc-xN5WsLdUQTwGIPypOUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=CNjjxnxFQEgeDPln4Ua103M-Eeihr80wnigvYFugihjcsTZ8uOFLI9fPQr_tcngRCmP8WsI9GHh1aCiUlyTlfOu2Bcm2Ty8Gyoh26oCznuL0vnXCtUuwoAZ2J7okPMd1OjciHsaRPQaLPtKoiRmM_mrb95vcYA96CufbATIcwtpZDAY7Wq3AINhIHDWeiywi9uOA2cL9jj0SlSTXubvjeE8rxIiAIGzyOUC6AlyMlEa5xE-UliFSWiTj9qKM6f637vGE9iFEfRIJnISW2NkuZBH--cAzT6kUn2ThLg5ssEUAhhd4YtlTlumrm3l9effGc-xN5WsLdUQTwGIPypOUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آمریکا برای اینکه به پرسنل ناو هواپیمابر آبراهام لینکلن یه حالی بده، برای تعطیلات فرستادشون تایلند. از طرفی تایلند هم به پرسنل ناو آمریکا اعلام کرده که خدمات جنسی زیادی در پاتایا دریافت نکنند تا فساد اخلاقی در بین زنان این کشور گسترش پیدا نکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105446" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105445">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105445" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/105445" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105444">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foorSyP-BboWcpSgkmi0r9djy0q6U_8fqvf0jid5zqUOZuypunmgVT5x9GfKgsqRdF3iu_bArq9Tv0ZdvazXO9MAcY8jNDdX-XqTVoHG2fCG0k0UU3GifNo7Z2ApnPWce0nh1jQ6l7Cy5ixtDxztSFFr3C1weKqYHhvOuWAss4AArU00rHQ8K2D8qt8TRJfCAVyblz11GZBUKaYe048H7RRQ5azpX1LyxVobwpSjcq7lc-E-AFcUJyGym_o121p8sE3h0TJt2vCPlx57Ki4gq6VfIOy4zECZqNhEGIvBnbo5Q3ESmVbhy6mSAUPhUPc7fan4QdaewOxN5xLkBEMogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/Futball180TV/105444" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105438">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWDbbPMDMROjolBQb2Ig0WycATQf98eITJFlNkJ2QoqMLQR9V4XOY4l1trJsH9qY7E6Wlu8HkOf5dIaGN-2FyMcSIUwXFvR3TB1Y-YDHsIWAQwkGZ-xSVyAOgYP_739w5sFFHkUxlKA1Fcan56peMGV_arqLXHJxlyHUBcPtN0-68ZDaaVU1ou801OB1VvDmhIp7MzErJHbY4txcH2AfkcJMiXyc8WLrSt4pqjvReUgUywTBep8KxbQwsfnq8wKPaABOzXYKQKCY2XWqE6LfmGWYGCAf5yW3C7UeiZM8eLqXMj1SfTSwPu8eSh9wsXah7o9UU3dWWzDPWdtrkB0JtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2vpsah8LU1DTtro_unmqujr08E__oF_DvLm5-R6k2OeF-vPGwx1JbH18f14ybO4oGeWUatQagDjJwpujF3cus_0pB0gdGz42dgsVNbjzxy7X-kWUKq_RvBAF24gChdpC14ywkRLmTho5nyOWtbIU3HDENmwx-CDspGP-1fljE0rpsLjqb3jqyB1HD7d4DkI5IKhBTxKq7qsH9tF3R1W-hvDP17ftk24oxfWlLjcb9tJcsW98iLTkXKDvoh_AdFmqi72OtfK09OmT1maVTcqOIr-M5w5Kj0JPwwgDHU9RIA44ZuZy_jPVf7ovj4kMFBibnAU2NnlX96X26-CkTfKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSYxGpCjoPgG6_MJb_He6nGC-dCjmRPw_PtrrDOw5ajQ3olOaSpN7tRPtx8JbVmz2kczLRxCxA38VKZKQGkv5uyNjEYHbTbHxACOCNTi_xNLkEksWae2Y473JnFsWpLEv3F0pvIeP-WMJGijNBSKW1uD9zTVzgpVxoFcB5i991y3eofUpHOeICNfJsMYH-cVEurn9tKKxIgeBRUD6ALntU-27a-eNC0NTPZPLAP6kIf9pcyx8mUFih9zNc5M5BQqfk7jXH3IF34PMjk60mlS6fSiYepxFt_TEb9CeAa46oEK_lmaoyZZf4KdIIq1KbOa3DDjjNIss9B5I-U48O3lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVF_qVl6IfNnrtpe1aY7AQZ_srhWmZCQOcQMbDuQdRmtoC6MIvxR-KivoX-Z9uWmz8d4_gf19f6vMFWZ5odDR2nZYGiJ6Hp5toRYuXjv2TD7y7FRuEZydvTGPdF8MbHIHXosd9mQ08kVcXiwafSp04mW0gofmyET6Ou5suIEdrJTCtsNIL5X-hApAJlUnr9yZhqDaM4h80LSd8UTl4gGdIHDyI4LjEUR5N9ZWO83lvgUoMY6CGs7g15VXEyjk0JrWFbDMOadtsZAXCIIg2PnJZ7q4_-xhqN1HqLtwDdf13gOlL_1XcuNC17s86bjeXs7hSWzhWRatjJYxz-FH0Mcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIWDyVY2l7tDoQ1M1YRVOnieHTTwN7KLnxmPS2ha4Z-oxGMZgQEg770CnG6g7hQF2v5MhLQ2Uuv3ZuesflT8LoBOJkFYMA7fAaIIecugeNU5XpzGIXovKPnv-kbMyNfF239NgaIUR7baeGYHh1NiUWwif8ASGXS1tIbTwdSXSZQKHtD3lZbHdhe0DWHtWRZRQTyfU6VR8gce8PdJG6A3AP8-q03t7VV54mzBJfRTAWbwRnLx82PqFKPx7y9g9rSQMdFDkmDqOt8nv8SGSOvg5CsUDmn_4cyz7y8KDm_Bj_TlG_tlUia3P9Djz7eVmQb1lTGZYgZCiDqvLOFSnre87Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
هوادار بانو استقلال در دربی نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/105438" target="_blank">📅 17:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105437">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=kWxrODHZDPyHjKT4I3u1GmRo5IodfPb4JhVuulZMqzN0_t5NrjFkk4C6LJz2eIKOhcPQBf1PHTlffUfLcsuXatkoIMYWcFoW3in7DILEAPRRjWjRrNdOQwB4vN7TQUvYORwpHTA4c3yE3YWVLKbGWEggXmrxBVosHqDQyG-LaO_-pkrrjrcncqXoB11AmGGnH2y0PI7skQEYHhOjQAxqa2j8JMVVWbWrwo2ft8a2d0UnlpnOQbONUNxjFXenCkdIq-kjqvUMbiabqICvFWKrNcWPvzzRLbTEQH7rxew3xhXepUX6p2ng77roL8-A7CQBRHEskx2SzSpPxh9kPpNcCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=kWxrODHZDPyHjKT4I3u1GmRo5IodfPb4JhVuulZMqzN0_t5NrjFkk4C6LJz2eIKOhcPQBf1PHTlffUfLcsuXatkoIMYWcFoW3in7DILEAPRRjWjRrNdOQwB4vN7TQUvYORwpHTA4c3yE3YWVLKbGWEggXmrxBVosHqDQyG-LaO_-pkrrjrcncqXoB11AmGGnH2y0PI7skQEYHhOjQAxqa2j8JMVVWbWrwo2ft8a2d0UnlpnOQbONUNxjFXenCkdIq-kjqvUMbiabqICvFWKrNcWPvzzRLbTEQH7rxew3xhXepUX6p2ng77roL8-A7CQBRHEskx2SzSpPxh9kPpNcCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تلفظ نام سرمربیان ۲۰ تیم پریمیرلیگ که ویدیو بامزه و جالبی هست
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105437" target="_blank">📅 17:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105436">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=V0QoYx8f3CGU4wn9NGOmBBS2mRBf3IzGgRBYYJfH1gNObBt27VlX0avRgc4RuqlHSJfYcKcnoE2d2wpOB9R6J4g5Y78CQRRprmE7CcSYQy0Xag8kbXocBSxC3ye2gCQirqIaMkZH5EVTnVHV5EKMukCFmySmWpVd7DjXCVIm65zqBO5pZhfmtnnG5wEfq5LvaZc4eEOQpfoRYkBvQMpYzlK5xhF2mgQA8N_7n-HrnrJmejW076eqGlrv14LixpRKt73EemwUSyeJgBx2YuV2jx7AfQa8vy-_AdWQRI5p70O6R0wIZJ_HbOE4nihYihv19mrw06TpJthZ92YeIJmGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=V0QoYx8f3CGU4wn9NGOmBBS2mRBf3IzGgRBYYJfH1gNObBt27VlX0avRgc4RuqlHSJfYcKcnoE2d2wpOB9R6J4g5Y78CQRRprmE7CcSYQy0Xag8kbXocBSxC3ye2gCQirqIaMkZH5EVTnVHV5EKMukCFmySmWpVd7DjXCVIm65zqBO5pZhfmtnnG5wEfq5LvaZc4eEOQpfoRYkBvQMpYzlK5xhF2mgQA8N_7n-HrnrJmejW076eqGlrv14LixpRKt73EemwUSyeJgBx2YuV2jx7AfQa8vy-_AdWQRI5p70O6R0wIZJ_HbOE4nihYihv19mrw06TpJthZ92YeIJmGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇹
سازوکار نقل‌وانتقالات در باشگاه کومو، از زبان میروان سوراسو، رئیس باشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105436" target="_blank">📅 16:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105435">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f719399999.mp4?token=JLNi5fNFZkqHZlqbSbUXgKEQRLXUxmUqCQGErC_jiG1GiTGcv6-EKuGiFc6AOlnGb_w7k3t1cQfylBSHvFZig_gljw9IN1U1F7aXJV6uFjvlRlVM-gDKvfyWShlgz1s5epH6ObRHPJhqFf3u55RYYSbkaB4ANMN-79OWP_ubijYLwG1m8LeKi7cha8i70Ji1PZxCPYXtpY81X-SYWCd05aMXvsdetRo0ArcFrFmPowkKq6-s5a_Ck2c-I7zlUJZy7zJfRnfFDpYmXlfKED9U3E16Sb1pnbWh8lxIbXE130nqdjyUMMtZ3zKnDd59WqCUp6867gyTD6ldMj6dl7U3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f719399999.mp4?token=JLNi5fNFZkqHZlqbSbUXgKEQRLXUxmUqCQGErC_jiG1GiTGcv6-EKuGiFc6AOlnGb_w7k3t1cQfylBSHvFZig_gljw9IN1U1F7aXJV6uFjvlRlVM-gDKvfyWShlgz1s5epH6ObRHPJhqFf3u55RYYSbkaB4ANMN-79OWP_ubijYLwG1m8LeKi7cha8i70Ji1PZxCPYXtpY81X-SYWCd05aMXvsdetRo0ArcFrFmPowkKq6-s5a_Ck2c-I7zlUJZy7zJfRnfFDpYmXlfKED9U3E16Sb1pnbWh8lxIbXE130nqdjyUMMtZ3zKnDd59WqCUp6867gyTD6ldMj6dl7U3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
امیرحسین صادقی خطاب به فشنگچی: کم‌کاری کردید باختید بعد می‌گویید استقلالی‌ها دوپینگ کرده بودند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105435" target="_blank">📅 16:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=N957HKdD4ZCD2jAAdkrZTABFW2GkOL1tORGtxWM4sY6M4sdrSydFYHYlNDJVMHIEIvMI4thV6QTyS_NDtdvRDQ6Rhv8JuZSLpEjZbukWYIkR0-9s3PIrtPppeLgKoq8_Fe-a01ju9YAU7oZhS9QLtnZ8lDInvNQkqe6MEPu-5Tj4KQ3GI8x4XvjHvTxLGhWsJ4vX3IaSthSWgDrSvdsi7jTs7XZUMM9RIKmxrlXkLaG2ffOqHA-ohVVPLxdPZKj5vPrK6YDcI5VVpd7EdK0u3ubifw10QNG1WdbegeWGNBl3Fjjq7C_Pl48YFkk_CfY-K8iIefx6n52o_YHS3QoDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=N957HKdD4ZCD2jAAdkrZTABFW2GkOL1tORGtxWM4sY6M4sdrSydFYHYlNDJVMHIEIvMI4thV6QTyS_NDtdvRDQ6Rhv8JuZSLpEjZbukWYIkR0-9s3PIrtPppeLgKoq8_Fe-a01ju9YAU7oZhS9QLtnZ8lDInvNQkqe6MEPu-5Tj4KQ3GI8x4XvjHvTxLGhWsJ4vX3IaSthSWgDrSvdsi7jTs7XZUMM9RIKmxrlXkLaG2ffOqHA-ohVVPLxdPZKj5vPrK6YDcI5VVpd7EdK0u3ubifw10QNG1WdbegeWGNBl3Fjjq7C_Pl48YFkk_CfY-K8iIefx6n52o_YHS3QoDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
روایت وریا غفوری از گلی که آخرین برد استقلال در داربی‌ها را رقم زده: مسخره‌ام کردند، به خودم قول دادم گل بزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105434" target="_blank">📅 16:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=k73NqxL1GPXj5tJtI_6gFraCOXYRHAmXqXheFJittOURIEdrmAxXam1xugHSv7ArcZL4D9Gv2A_Tts6Z8dQSwk1SQKy2rbMmqMpja9DmEC_A5NNVYYwwluhsAbSGFYOJDw4vwWe8WgB_XjnL3VaJPMChjrPqJCPU7a7kAv7qy-C5R2LrORjo8UiFySg4TKOxUGOpw9d5HYvMpOfN29pdeaV-TDMyQFJ9ceEYQU8Oww98FBB1P5X-fH6qAuWL_BAXRzwwCxK0vgBRT9kjAmU769iUmR2OmAZzA18QNkQRQisRnZc46k4g0H44nyAbxw6g4Q-RiNQN35CrB13Arro7EE0gvsu8dOSmBInmhS_TsCR_90Fwm9CZ18UuM3g_opVX2g1eXldDOZgSeRvWlf5VMkuM4Kor65ckW3awBngzwIuekwrnOxOB0nzwaCJcgl_fdagfoLMl6GN8Xi54yMyhBXlmoEdBY0sDvFiDVOMIIBl5A3Ox6i72d54RduPs6DGkJf8Y-XDYe3thvBdGqYbYtvc4eAR86DAdW0qQFjy3QsNlkBKNWc7R_FcTmk3POGrq1uKxgAvJaaLKxbyJkAJUHAE3NmYYhRutOiNnlRcNp8Tsb9c-_kjLNGxES-L02GYP6qjPxZ57GBC-0yt4Y2HxbAM4yLRJSYv50Go757c-9S8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=k73NqxL1GPXj5tJtI_6gFraCOXYRHAmXqXheFJittOURIEdrmAxXam1xugHSv7ArcZL4D9Gv2A_Tts6Z8dQSwk1SQKy2rbMmqMpja9DmEC_A5NNVYYwwluhsAbSGFYOJDw4vwWe8WgB_XjnL3VaJPMChjrPqJCPU7a7kAv7qy-C5R2LrORjo8UiFySg4TKOxUGOpw9d5HYvMpOfN29pdeaV-TDMyQFJ9ceEYQU8Oww98FBB1P5X-fH6qAuWL_BAXRzwwCxK0vgBRT9kjAmU769iUmR2OmAZzA18QNkQRQisRnZc46k4g0H44nyAbxw6g4Q-RiNQN35CrB13Arro7EE0gvsu8dOSmBInmhS_TsCR_90Fwm9CZ18UuM3g_opVX2g1eXldDOZgSeRvWlf5VMkuM4Kor65ckW3awBngzwIuekwrnOxOB0nzwaCJcgl_fdagfoLMl6GN8Xi54yMyhBXlmoEdBY0sDvFiDVOMIIBl5A3Ox6i72d54RduPs6DGkJf8Y-XDYe3thvBdGqYbYtvc4eAR86DAdW0qQFjy3QsNlkBKNWc7R_FcTmk3POGrq1uKxgAvJaaLKxbyJkAJUHAE3NmYYhRutOiNnlRcNp8Tsb9c-_kjLNGxES-L02GYP6qjPxZ57GBC-0yt4Y2HxbAM4yLRJSYv50Go757c-9S8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥇
رضا قیطاسی پرچمدار ایران در بازی های جهانی عشایری به مدال طلای مس رستلینگ (چوب کشی) دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105433" target="_blank">📅 15:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105432">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=Kp_LhPZiS8e-kxVhRP4KcpVF2iExUNhPnvGapwLxuFU0hA9wdkfn66IXx18WB_ZDHXaI_USPnZV2_0Xg6UxvzNxg2kBuXQaL1nuiL_Y1QXOK2hG6BCVxfleg5IN9p5C-4TrF23i_maaKRXZ-af-GTogJWB74XxbuSAWOtqRWRgMfUMPQEk-9ioCnhiKF12_frwB4y7az1i9Cy07ug0TiQY5jGwdSz1S9Ywyyi0fBztkEPeJ8-d5UVQiXGAnqJzsl_heL0cMNT2yPxmjNVtFIFcO9y2ASjn1a2mve1j5bi6UkDTNu_AY0_gk813NRNXErNQROLpZr4x1ga7ZDm5Rh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=Kp_LhPZiS8e-kxVhRP4KcpVF2iExUNhPnvGapwLxuFU0hA9wdkfn66IXx18WB_ZDHXaI_USPnZV2_0Xg6UxvzNxg2kBuXQaL1nuiL_Y1QXOK2hG6BCVxfleg5IN9p5C-4TrF23i_maaKRXZ-af-GTogJWB74XxbuSAWOtqRWRgMfUMPQEk-9ioCnhiKF12_frwB4y7az1i9Cy07ug0TiQY5jGwdSz1S9Ywyyi0fBztkEPeJ8-d5UVQiXGAnqJzsl_heL0cMNT2yPxmjNVtFIFcO9y2ASjn1a2mve1j5bi6UkDTNu_AY0_gk813NRNXErNQROLpZr4x1ga7ZDm5Rh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
اسپویلِ بازی بارسا-اتلتیکو در این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105432" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqxghsRhAqzg11zetyzXO5x65CBLpZmftxHCV8qmXlwtP9KgUQfc4gEd8zW3mkQLKGEEUz7gov19-t6CfkO2WiCfBYHS7PMX6dN8X-cdNXLxTpiGSJK0J1efkrf51txwZVi_CPi0P_dfkrL6IcyM6PGpDJINscdhwblLRvFBMSrZuYVvk5WafU8o5RjQZP4s--yi57Qt163VVF_wdfdgFiXg95dNEWrBjkDHytpVb--7IF1W7SugkoDb-AoBv36n-EiK3-HXaW0z_XvGcAOMgZVFEg5m1dZGLmAJOTBPGfqlUVej4Vb2sHsHzLmngyvFKKXf_d4oG9VomtkN6kmmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLK2TPrvgLJtw88qFvN1CW_0g1YJyIx61U9YBQkmL_5DeilHeGImMnDJNyAlPPyhWpHIX8ioOkkX3RpNR9oH-gnNM6bNrD_4ppNYLizq2nXw-MAQBx3QPNzN_DMvD3bl86ZFcVEO7iWhDeXXzH-qVMgc4QzsOGFgTYr9imFzYkCt-fMzRCx55pYLe79hLmz7oZSPL6Jiai6ZDgxtQGBo0vmwQYJdByxWRgqf7kwHMnH5rcIh2rkJWUPUnocyYjLYFmQPAO_1LYrj9AavkGkNXy_0cq1IQo8wNIN1SoZ9qiZ-kfbP9lE7_eQDUsn_jF62NIUtUMgAPuPFc1jQoYIWEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
عیش‌ونوش لامین‌یامال و‌ زیدش در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105430" target="_blank">📅 14:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8bq9U4-5bb8P2xwJzS8xNL4KIOlo01T_0jrXqyLvM72cBu7veAK__Punp4O1KmB8D_EDc-IA5-IZqpSop7RXeY7j2iTR0jDAA0C727fKhVI20VMgsciQZpZQr-xndhWqbtBVnEQu3DCvqJeuOe6MXh1QkYgninU1TixaVSOHpjnGSu81_tE7-0t5VfvMRPZ3tIQZ2gOfDmDBElMfnDCVrpA2keFxDAvwmehu3im428B1PWqLbm1uqyCpcFyQ9Hf0jEpK7tqLeOqmF7EJzMGguRa2LZs6eGXq-D0IeOEcehbpotJfLLD0i4DZ-1N9mzgDtZGs4Hh-OMD6bnUwIoznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105429" target="_blank">📅 13:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105427">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaD8mcN9gspIRACdpReZeoLF3K3y6lyz3uSwoypkepdWE0YW6-9X2LdO2DPjKjmTxfG8Goq5kSjAo3krwawE0jW0jaISACxyyeu9X_fkU60Jq_u7nzYSjWC1Ml8rWKF1cksS8e_BQvnB-Mkd2pvkShBEIQzZlV9OEgnMCDeGAfBnXwrDTeduchgSbzPAxHGVaxdSBuO2x5nWfAPWZW3SdQeJxU33si7i6uRuaiRsm12-RT4FwQedNwOueeka9pBXNvU_iF3ZUTrokGUXLjzWJCuSFQvv6cBQb8jeO-w174EaRNoQ83CG1mOJBuyc-J1UBH6P-s2ONithmgGC3bTsPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105427" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105426">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEarT5ndKuF-Ja0RQkzDbiaILNmM6oKort0Dg8aX53yG6hbBITgVwlrYzCXu02ZGu0CKu6a9Dh4XBPyxgVfui3k5woS5paGIv2mK-8o00GfLnQm-7SQEHnxZ38QphpWALShAxS1icFF94UQak4TTwE_sXckWNtDxBbegfQEabinvsW-f4-hxZu3PrfYLgB7FL8Vzno4X355Y2MwnYViD82lm3qhqDsy9t2AvQdtPQb0XB8hgrPJq42c3iSOWDTdckEAFc7BloxCIZVu7E05mHD2HrpWQL5hFdXYnlNPVnCdkr5WicHs-znwhXGWsmJxhQLqL8yL_QrLaFWRa9TaGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!  باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105426" target="_blank">📅 13:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105425">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=sGqJePBiuuXQdy5WStRy8Gt447FPFhvdvLe_-5OcqY_Xx_ikiSBKo-PaeqIcdNNBTshN1la-6FUvgRLGhMfa3wJwMsHZ2S4XgYbXXLaqqQu5cfZODTI0unNHAq6EiJVr1Ztt1qaQSnlZsDukDOFC7T-Htb4B7Ew6-66LesFtIeRdYL2UWrzECkzYbrM1XHKzFxA4JHLG5IIg3Qc4v-DpIl6YPJAtaAO4f5SpPRVAjTl8zVAnKFkgumxKxPYIrgPwY6_HST8tn3cmcNieYgx-ZguTbLSc8SH0kWSBLGKOUEqCgLFK9ezmoFWIAuGe6xQwebazDvu8Jmxt821bksoMLScPwPKMZr13AFDo39VWpvzMxNfJ8nGYkujSx3ZsRAjoi4DJ0rBRx58L1TX5zH-w6j5MYMNfhEXQc4wIcgVXFXSvq_lokZLB6ygcMblvQdSQWb4MW63-ygWhbci209exWAsnedEP-zX7CjzDlF8zDGXwLciEgf12BiiCdG8oOFqWQIzn_qt2ocIHIS3zWCV2yYjhfyfRF9b1PZUP5A9b7LgNUw66MPWqCpItYbkznP_PkmZ1eJg6UrSZ4EvbLsK42IE9vQ0fIzpMudilSX5NhfD9xu1vSxElqCNtTnf6G3wsyBSHopmTAWAQAedOsREKCOgASwqYQEcRFEzbxFF1C6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=sGqJePBiuuXQdy5WStRy8Gt447FPFhvdvLe_-5OcqY_Xx_ikiSBKo-PaeqIcdNNBTshN1la-6FUvgRLGhMfa3wJwMsHZ2S4XgYbXXLaqqQu5cfZODTI0unNHAq6EiJVr1Ztt1qaQSnlZsDukDOFC7T-Htb4B7Ew6-66LesFtIeRdYL2UWrzECkzYbrM1XHKzFxA4JHLG5IIg3Qc4v-DpIl6YPJAtaAO4f5SpPRVAjTl8zVAnKFkgumxKxPYIrgPwY6_HST8tn3cmcNieYgx-ZguTbLSc8SH0kWSBLGKOUEqCgLFK9ezmoFWIAuGe6xQwebazDvu8Jmxt821bksoMLScPwPKMZr13AFDo39VWpvzMxNfJ8nGYkujSx3ZsRAjoi4DJ0rBRx58L1TX5zH-w6j5MYMNfhEXQc4wIcgVXFXSvq_lokZLB6ygcMblvQdSQWb4MW63-ygWhbci209exWAsnedEP-zX7CjzDlF8zDGXwLciEgf12BiiCdG8oOFqWQIzn_qt2ocIHIS3zWCV2yYjhfyfRF9b1PZUP5A9b7LgNUw66MPWqCpItYbkznP_PkmZ1eJg6UrSZ4EvbLsK42IE9vQ0fIzpMudilSX5NhfD9xu1vSxElqCNtTnf6G3wsyBSHopmTAWAQAedOsREKCOgASwqYQEcRFEzbxFF1C6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
🇮🇷
تمامی موقعیت‌های خطرناک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105425" target="_blank">📅 13:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105424">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INL4aivT5mFBm50sMlgWVPvnq-8mt4R9FzsW_K4ob0MKTW1hoGRhe__oWfu6QQyUGmrFGsel8Z9JvnxPJl7i-gcDUOonmTliWzm_P_TjyrvbBbRMftwD8jqwlyO3Ym0uMLXNzhLv44kt49WvSwpTGauJax6RgeYpAOj1B_V9qf5JuHvsEyLQUg8symVYfgNfgb0VjuZsKxBU0bGDzCmNQYHv-shQQYCkkKvzPvCfmenzpXlzszzcxj_KUCZ9x1iU803k6H7G9rss61n_ig0ZjXE4iX8ZUXR9WvWCu3HGI4MadIN40BeXHdLTd7lrji6S6OBPJQ0N77SwRl1wRsZHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105424" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105423">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105423" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105423" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1FU7ftkKT6-ScHAPXsng1skI6q4bkrvMGc2LRSPt6tJQnLyzkT_5pTExaLV1SFFAXTqbzE0tb4Q8XOBqwj4ODr3n-Q9yNrLOHf5SZ_wA6WpYBBiohBuPW3kHq87tUCiUG0EI85TC5p-HfrHBzio_s1E5HCqKEIA_YJ-kGU_qA6KIOdv9I70eJojD776kANU5vYnBIJ_oxR7xtoO-tRhF8f2zAtRqFsGhiBYfzgeLhGjiESrP6ClmigdbYBREE3EfIiB18sglt8M6mkQhcyivXo1jrQYkjprR35KN7vlEmXF_EU527YMfieRoIsbwUL2OKi-MnHlxHPXLoF_gHquPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105422" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105421">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=EYw1o8kTX1zsYZ7FkEXosxOjjkaS9FCKt5LjAWTghklM5kaXDYJ9j98qka4EoCWtu6w8gfYMYnpmv9kWhEpRfWTDujfvC0Mkd-ibGqWeK3xZBgc4XqVVPp00cpcr2wwbQgZRelmbf0nBwvonYLLn7vXmgxJ5ExD5-fwUUFM34J3UA8GeY05hjZ45qGdZexoVTCX-v2nZbTCZwL3jhYB0JSOLT1NKJJk6aTnW9Inlcyy8Y_sfEgitm8zXuA84Lm2WgFJBj4IJ2cuYklCezR8xYYknPj1V6axzByKkvJ91wph0LU1JXQUVgyl0-IN1Iw1jHtt_-oB1LL7NDha1xLpSK1M-MS-gDuD7vBsR6UtYKWDyiscvz6CcLrzRJJ1BCdSQPr--Wqfjjz_BvrnE5urNmqcqQIpXVarUVdRCc8_ia_t07eT2s4brZa4dRzHOM5Kd-8DBIzPgsjslWG6gevFgJ0UU6jiS10rnsQZthHszBtzB2vYT3cUj1GwVaLYpwwQTsMRQeWBDxYl6DY5gd8isx22tDikZsX8KWxYHLdSizYlU5ELQRa6Be5YBK_i22gXqLSEcrGvzR-2SgQRxeHpwdnvsjYUw0VzRMsK4fvER0zZaWaXDpQ3teLTs_vjYtPgQW_uq4a0nC5jzTa_MQ94uxsXJ2SzWZmyCL3U8huzPEbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=EYw1o8kTX1zsYZ7FkEXosxOjjkaS9FCKt5LjAWTghklM5kaXDYJ9j98qka4EoCWtu6w8gfYMYnpmv9kWhEpRfWTDujfvC0Mkd-ibGqWeK3xZBgc4XqVVPp00cpcr2wwbQgZRelmbf0nBwvonYLLn7vXmgxJ5ExD5-fwUUFM34J3UA8GeY05hjZ45qGdZexoVTCX-v2nZbTCZwL3jhYB0JSOLT1NKJJk6aTnW9Inlcyy8Y_sfEgitm8zXuA84Lm2WgFJBj4IJ2cuYklCezR8xYYknPj1V6axzByKkvJ91wph0LU1JXQUVgyl0-IN1Iw1jHtt_-oB1LL7NDha1xLpSK1M-MS-gDuD7vBsR6UtYKWDyiscvz6CcLrzRJJ1BCdSQPr--Wqfjjz_BvrnE5urNmqcqQIpXVarUVdRCc8_ia_t07eT2s4brZa4dRzHOM5Kd-8DBIzPgsjslWG6gevFgJ0UU6jiS10rnsQZthHszBtzB2vYT3cUj1GwVaLYpwwQTsMRQeWBDxYl6DY5gd8isx22tDikZsX8KWxYHLdSizYlU5ELQRa6Be5YBK_i22gXqLSEcrGvzR-2SgQRxeHpwdnvsjYUw0VzRMsK4fvER0zZaWaXDpQ3teLTs_vjYtPgQW_uq4a0nC5jzTa_MQ94uxsXJ2SzWZmyCL3U8huzPEbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
افشاگری همسر رشید‌مظاهری از شرایط این گلر شریف سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105421" target="_blank">📅 12:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105420">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNCMpXV3zAhBxqzDzKnqRqTexzDlMpITSHtSyFI9z7r-tMbaEDtcFShpXTM65tac4aa1_O55H8p9vHndsUACo2BscepiVE3j3DUDTkU1AXyzXPOZ0SLzFEKoG89PkU0DYChaXymU7WLKL3eMKvMo4eQGydbzrDBtbivxKuHF2ubt0-O_eCxJb1M48RHnkiLHM_yMC3gQO-CmZ5cDmHsi32nhaG9ki0ev84H2X2hq8cEqyZJWHuC-i2jHczFfhVoo5Ok4gGisMHXDrpZM9NDdM67qI87qfw_f_Rfj-CDpShNDp-7ESvJHi9jTGtznd2omH27OM5ilOuHjg_GZ7FrzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
✅
🇮🇷
پست اینستاگرامی مهدی تارتار سرمربی تیم فوتبال پرسپولیس پس از داربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105420" target="_blank">📅 12:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105419">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzmCNTeC1jkvuv_3cwS3pgFxOWoV0G5I6HNrJhIDwFGe7xdmfSqy66j0Zo0FgMJeZR3IMDSN3Tm75AlIyeynusWUzrWDRULR5JjQ9pXAjqmy4oZ9ZwZJdzjT4R2-qPSs-LceDZRDeJH5giJcHoCSgNJuJfUlDHk8o1PPDVwl2zvF1mij2UJ5B5KHwsDkaQK66pilDvX64yEamdDZ9KSVFqkwBZ-bzYRKDrQWPDQtTJs5OZ3vPVkVCzGu6nZH5gzHmZuAHYWeI-SBDthCByG-FSnBmMmLLxhR8u76k27Z2DCOVY2T2J-lvPEVPAD9PY5iR7kobKcMjQoStuEGIso7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
اعتراض تند مدیررسانه‌ای باشگاه استقلال به عدم اخراج حسین‌کنعانی‌زادگان در دو صحنه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105419" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105418">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105418" target="_blank">📅 12:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105417">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFGzwP_v2WPwz7E-7PqPrtHCEBx5t6DlkiY2WXjMzpLm-Z64hBCP5UHQNryf76oUwkaisuiCuc-DeBI7uQf-oiR5RCcYouQZLFeEVE_5bnoXH7-rAmEUJtO-2DOnuUKkePxjVyPXYno7CC5ylQ4P9nc3vIsSaWcF5oA_oNEj9Pt2D55yDaLN0X8uWoW4MhHtX1gVQKlwfVplEmbmiBh-oLLbsmAEKMhOgPgayAYQdaPRGw_rZv7ei-HLcpFl7qEGRzvxhLvBgMfcdONITx_ZjnNOm5SdxbsAODpdw4ugWotjbdfSaGloEWHztcqrf8cjoapDP7alSQDsjzy-nkt51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
محمود خردبین اسطوره پرسپولیس و دخترانش درحال تماشای بازی دیروز دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105417" target="_blank">📅 11:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105416">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=ciZcF_k9rcca4HywzAyfkQZqcQk3GCoy6-3qOi3ojNkkSh7fwoFPyqyYMjnfV9pPYS0w4sO8j9Oenvs5tdVpj04MOANH0MrFC2wHBYfTERoVL-Nm9AM3AwfsoiRh-TqbmwQHKr9MtwSWIv4YeBRgQWteUjUwO1yjPbTBEXgzGwtchS6qHOoyZvdg7g8DzNpLagKBxAmW7L9oqF-oCQpewPh9BsRc-Yjc8DiJSlXzZ655McEbAID7oTW_6pK3Xn1fLpJukqKfgvKQ3eCvlJSa0MpBD_EV6PP7aoYceXLi_oIOUude_hnHLhs1ENwC4LjRc8G2F11iJBXqDLFPB8KzrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=ciZcF_k9rcca4HywzAyfkQZqcQk3GCoy6-3qOi3ojNkkSh7fwoFPyqyYMjnfV9pPYS0w4sO8j9Oenvs5tdVpj04MOANH0MrFC2wHBYfTERoVL-Nm9AM3AwfsoiRh-TqbmwQHKr9MtwSWIv4YeBRgQWteUjUwO1yjPbTBEXgzGwtchS6qHOoyZvdg7g8DzNpLagKBxAmW7L9oqF-oCQpewPh9BsRc-Yjc8DiJSlXzZ655McEbAID7oTW_6pK3Xn1fLpJukqKfgvKQ3eCvlJSa0MpBD_EV6PP7aoYceXLi_oIOUude_hnHLhs1ENwC4LjRc8G2F11iJBXqDLFPB8KzrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105416" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105415">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=P-OsLfsA_cl_xcdOq5_fMCqJfF1O7QudTtrV5HbK_c9fbD7cXIokC6tErSs-J6LWzqkB9RJwTaojdM1NHiLwe137hn3KWBvRsO2a5w5VpTRF3dnD0KG_iipXGl4nE13RPIeRzcytPy-Zpq_TMIEX28BEkpzO7r0_49Hp-4Ma31qderX6CbynAun7dK7eHfpLzZCl9SZWbgwQ63A92R9fVCe8xNj67LCgVMV7SPNa8appQRg3o2X3fdFYfst4GN71TMzvTHF_cqmDoYbz2DJUp0h90cROmO_914K-ZmRGyKZsDnqaNOuCX4BEte6tcatr9Lra4gavJqEp-WT_2-xzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=P-OsLfsA_cl_xcdOq5_fMCqJfF1O7QudTtrV5HbK_c9fbD7cXIokC6tErSs-J6LWzqkB9RJwTaojdM1NHiLwe137hn3KWBvRsO2a5w5VpTRF3dnD0KG_iipXGl4nE13RPIeRzcytPy-Zpq_TMIEX28BEkpzO7r0_49Hp-4Ma31qderX6CbynAun7dK7eHfpLzZCl9SZWbgwQ63A92R9fVCe8xNj67LCgVMV7SPNa8appQRg3o2X3fdFYfst4GN71TMzvTHF_cqmDoYbz2DJUp0h90cROmO_914K-ZmRGyKZsDnqaNOuCX4BEte6tcatr9Lra4gavJqEp-WT_2-xzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
هواداران اسنابروک حریف دیشب بایرن یه طرح قبل بازی زدن شبیه ترن‌هوایی که خیلی پشم ریزون و جالب بود. تیمشون هم در نهایت از جام‌حذفی کنار رفت
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105415" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105414">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=SnFGQkF1dMNNGp9DXid-A90yzB0uYbewQndekdGoVOulT_CGNorhmVaseT6cITT8EoAEwGm4zHzDH1AFbq1FObeET8H0niz1Jj3-u58QEFAbMZpVcSd1A9MFA0PFW4Cu4_2q6QAej1LqJ9DmkH8uj0vztde30vPJNRTpe_TXdnPsi-1Fut42UuUKYkmc6lXzokkeP2VXUjHQCEeEPMq324Tnmh-okgIoqiTmoOtz_1v_TXjgXFhaUU_jiQVnhCKjmfBsutYrtr9d8cIvBHdEmWrLbrurUL6Ano63Rn6PyW8X2lPggAdSYKe6LiP5c_24R9Jv1hbISwqw9DIJ6BzTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=SnFGQkF1dMNNGp9DXid-A90yzB0uYbewQndekdGoVOulT_CGNorhmVaseT6cITT8EoAEwGm4zHzDH1AFbq1FObeET8H0niz1Jj3-u58QEFAbMZpVcSd1A9MFA0PFW4Cu4_2q6QAej1LqJ9DmkH8uj0vztde30vPJNRTpe_TXdnPsi-1Fut42UuUKYkmc6lXzokkeP2VXUjHQCEeEPMq324Tnmh-okgIoqiTmoOtz_1v_TXjgXFhaUU_jiQVnhCKjmfBsutYrtr9d8cIvBHdEmWrLbrurUL6Ano63Rn6PyW8X2lPggAdSYKe6LiP5c_24R9Jv1hbISwqw9DIJ6BzTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید ایگور سرگیف از تارتار بابت  تعویض شدنش در بازی مقابل استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105414" target="_blank">📅 10:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105413">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3-CvhzaWm9W9iERhpkEOooZf67tXjt3CVPPQhYJi7TH6qU3J-37i7vHxEoOUSExAcGZqft7haWRdnYR2wnPJoSU9vsrttDhbpSZZMJT2B9jsbR1mob3JZX2AbYAmlAQAAb3feNda3Cj33n9IVaQqBelK5viCC7C9e63_kBYbxKw4ES3Vow_ou3aT4L0S27uTJMJOdJx8q_TwBloEGGxKH7uVldZOIzQ36nbWCorubp2laft_xZyrGZNwrh5kX2MfBgTiCzpNlzxGkmwh-D2EC33tRU6ZFAwDmFTmukDtZZ0pMw3J9lI0lazPPk12HCYgCRyy4Q_2IUUjmDZr0FvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
✅
قرارداد کارلوس کی‌روش با تیم‌ملی غنا پس از درخشش در جام‌جهانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/105413" target="_blank">📅 10:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105412">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8I9L_VhZp6ho5ldkzoK-3lQBp7S71oVzoy9eLqReFh3fJjHmWKelPqXvGRUVaIUZejs939xsxKWe9SHuZ1BfRkbXtIG8Xom3Dnf85N2_0YifNz_ntsG6dDOnJr-j0bT7sOHOkyjsDAyP5vFtYScpVYIoP6g-KcGzUQPqPlaIB2NpOyfNK81WCnewEKGpa_S2I_tysvT6WIw2Zm0dXadM-MUcuCsEnFg9tLDHk5A-xxLidn1DbWsSeOPF5HeeF4m_bfjcP3mbcEricU5xn9vqyTJy3nPebdT2y93Rj61vU13HY3H3Qd616cgC348PtgWvJQntj1eMD6KJJgZB7r50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105412" target="_blank">📅 10:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105411">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193fef239.mp4?token=QFZgsajtTyb6RdNP0Cqn04ASLNIQbqJ4OZ1xy2nOkpYs6iQGvi0_ss7-YiD1Zar5yLt8WSzY5ZtftZBk7S0Ml0IdC9O9C2HOPWW91QLrpyYzn_CKbJXcjITZfKPTeI-D6K3EKlvhi-RNFyA7Prdw4jiSQ2he53WesP7Mdd_kYWhzA_f6L1v26OEiol_LL2PnnMiUEb1bRDFQcafn8unXC9tOOT9N_KHnVU8HJ7Y9TVS8iCJKcwPRSWwk0nRZB4fzIxrYYeXmKl7D3YCmy7gaUzS93XhTZk9hNM_Btq57KGlnxbJdTCqcIUtj5G2haqzfA4tYDrlVn0IwOPaQ5RPJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193fef239.mp4?token=QFZgsajtTyb6RdNP0Cqn04ASLNIQbqJ4OZ1xy2nOkpYs6iQGvi0_ss7-YiD1Zar5yLt8WSzY5ZtftZBk7S0Ml0IdC9O9C2HOPWW91QLrpyYzn_CKbJXcjITZfKPTeI-D6K3EKlvhi-RNFyA7Prdw4jiSQ2he53WesP7Mdd_kYWhzA_f6L1v26OEiol_LL2PnnMiUEb1bRDFQcafn8unXC9tOOT9N_KHnVU8HJ7Y9TVS8iCJKcwPRSWwk0nRZB4fzIxrYYeXmKl7D3YCmy7gaUzS93XhTZk9hNM_Btq57KGlnxbJdTCqcIUtj5G2haqzfA4tYDrlVn0IwOPaQ5RPJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105411" target="_blank">📅 09:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105410">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=v4WOsS920meNvRVDlxk8lmy8-3aWRvujloFRWjj7ukJYma4eezRsNyVJaivlCuSGBMPIjQkRnYni1ZNcSm4M-Z3EvYFfiWXjm_PxUXjLZoZzDBfKgroxXiDZ3yPlgdasGR602-s9cvJwYPDNixndxLTujFJPfgEHYfJVp9FsfC6Vf-Dtu0UeP91PJO612aG4rgf_vbfIFUrIPHT-RgoX9kW8lTtxggKEbcT5tVVpkQSU_fyn_n49VS7l2FHMze5YxQka6_UNlm3rFrzLqHQS32xPGdv-3g_RJCeL844kUh4mbFE83u5CgFp750fjEmKCYAr0lMPrJdUbccA2pBz_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=v4WOsS920meNvRVDlxk8lmy8-3aWRvujloFRWjj7ukJYma4eezRsNyVJaivlCuSGBMPIjQkRnYni1ZNcSm4M-Z3EvYFfiWXjm_PxUXjLZoZzDBfKgroxXiDZ3yPlgdasGR602-s9cvJwYPDNixndxLTujFJPfgEHYfJVp9FsfC6Vf-Dtu0UeP91PJO612aG4rgf_vbfIFUrIPHT-RgoX9kW8lTtxggKEbcT5tVVpkQSU_fyn_n49VS7l2FHMze5YxQka6_UNlm3rFrzLqHQS32xPGdv-3g_RJCeL844kUh4mbFE83u5CgFp750fjEmKCYAr0lMPrJdUbccA2pBz_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🇮🇷
🇮🇷
توصیف‌‌جالب عادل فردوسی‌پور از دربی جذاب و تماشایی پس از سال‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105410" target="_blank">📅 09:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105409">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=X2zyjsa8t_dcnk2n_Cv9bpO7R0AEU90uTS5y9NU-YM3iqi3dqfiWLbgR1JaIojIWly2pP0YUZSxthI4FmAsKQnCU7NrLnKHJTGfxY1HEJKYSi6ExLFxOu2UCRM-Aev3F5POHOak08ojJ1bXaVd33dl58wQsDNNL40aBL7BDXEb7m_MtcnIhOe1KCOAdkBCeKooGWaaNy6vumL5MAvwlchJPDBFltWKySrmIzRVD7xAbSFLx5Z28ASyf8HTbNsruv4Cp1dipB-zR6aZA4zahjP8-UO3DHWjHiw4Z-bK4si8qpC_b4WkNYGhSVbNy6Ym0fBKaECmqsiBrAEahkbPAdHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=X2zyjsa8t_dcnk2n_Cv9bpO7R0AEU90uTS5y9NU-YM3iqi3dqfiWLbgR1JaIojIWly2pP0YUZSxthI4FmAsKQnCU7NrLnKHJTGfxY1HEJKYSi6ExLFxOu2UCRM-Aev3F5POHOak08ojJ1bXaVd33dl58wQsDNNL40aBL7BDXEb7m_MtcnIhOe1KCOAdkBCeKooGWaaNy6vumL5MAvwlchJPDBFltWKySrmIzRVD7xAbSFLx5Z28ASyf8HTbNsruv4Cp1dipB-zR6aZA4zahjP8-UO3DHWjHiw4Z-bK4si8qpC_b4WkNYGhSVbNy6Ym0fBKaECmqsiBrAEahkbPAdHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105409" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105408">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603e84d100.mp4?token=kHxUYHyE343tS9Gbgzu4H8c9o_LxtIM8l2io8JQeTTyIazZ5lh2rexS9jd2NYgp_DksczAebGJuvzzO6FUTYbxCARLhkH04ViN42VfTWc-BFGmwb0KatOcoHrgfmtBimxpEXUw9kFW-awH9a-QgPgcstSV6wPAOCbXqnnJNpmz_p_eELTWPrgR98puLYHEx6dApJPRQcXxAocQ47idqrIip7VRqMJBrZcuQjmQj6toLgwgNzunqZerljz0d1q33UY-AQpfhh0YhliGQd_VNUXQQovGKDuj3Dt3ffo5LgjO0pXwbdfxw3FgLzXQtcUvRaYEdvXTPHMarFTM8KyunZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603e84d100.mp4?token=kHxUYHyE343tS9Gbgzu4H8c9o_LxtIM8l2io8JQeTTyIazZ5lh2rexS9jd2NYgp_DksczAebGJuvzzO6FUTYbxCARLhkH04ViN42VfTWc-BFGmwb0KatOcoHrgfmtBimxpEXUw9kFW-awH9a-QgPgcstSV6wPAOCbXqnnJNpmz_p_eELTWPrgR98puLYHEx6dApJPRQcXxAocQ47idqrIip7VRqMJBrZcuQjmQj6toLgwgNzunqZerljz0d1q33UY-AQpfhh0YhliGQd_VNUXQQovGKDuj3Dt3ffo5LgjO0pXwbdfxw3FgLzXQtcUvRaYEdvXTPHMarFTM8KyunZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
👍
وریا غفوری: یاسر‌آسانی جدا از فوتبال خوبش یک انسان شریف هست و در ایام حضورش در ایران برای یک فرد کم‌بضاعت خونه خریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105408" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105407" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105407" target="_blank">📅 01:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1ot0_O1ssLZWH_GfdwStpnZn3ATWPuGB-zFo9XwEjQVKR7JwTMh5k46TUR31dS9zAXbvAc9vA4w2BpNekxOuKS8PyiYB4fsS8pZiE3oFHRooQhksXV-G-LmgIRKe0o566HfHuQsl8hx4hIAY-s4_TNSZz5VsXo9YQUq_8rE7edVE5t1Jqn8L7gwQ6LfNwjFXwaiHKt0bB6L9X4JzVjDIYnAMG9lztjgKSwkomOY5sHdvtIun8k10dTTiP7BYYSUSbbVbHeF2rS8NjoEg3obBEveJBLmcRYrGn5stmxqUAhjVoNgbkcKWWUxrz_4mCIFvVX3e6uSxyGdoWV4-xp5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/105406" target="_blank">📅 01:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105405">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/105405" target="_blank">📅 00:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105404">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=FNVU25tF_hB6QFqTXfz2USl519P-B1lYN8ZBINZ9_7bf7eSvvEHkCxS2Zp4L5abDrUjqV5uu_QwWwxsBmnXZb54sF09xBWyGrmN6vMSueMEEkSU_orCi3h7dFVcW43fAVRVuzQrQ8yZcipHBi17EokSIl0EnSJU7DHz-hhAnpRkBvgfuiCbK5e4PP9S3ng-GAogElIojTnp-vTIDYM90UFR290tGG-akRV5AhKIExvi8SDCsVdt1Az148nLRpxAb_1YFJb9FCUJFvnxsz8RuKdK37kPdXqMAMrAWBibA3Tjcgb4tgCzbmU9gRtvwog9mkK2Tejnk4_9n367_jwu_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=FNVU25tF_hB6QFqTXfz2USl519P-B1lYN8ZBINZ9_7bf7eSvvEHkCxS2Zp4L5abDrUjqV5uu_QwWwxsBmnXZb54sF09xBWyGrmN6vMSueMEEkSU_orCi3h7dFVcW43fAVRVuzQrQ8yZcipHBi17EokSIl0EnSJU7DHz-hhAnpRkBvgfuiCbK5e4PP9S3ng-GAogElIojTnp-vTIDYM90UFR290tGG-akRV5AhKIExvi8SDCsVdt1Az148nLRpxAb_1YFJb9FCUJFvnxsz8RuKdK37kPdXqMAMrAWBibA3Tjcgb4tgCzbmU9gRtvwog9mkK2Tejnk4_9n367_jwu_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/105404" target="_blank">📅 00:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105403">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEvWfxm--jfuwSUvkYQkRpdV7MWp1fnyMMoayj3wSqLkI0xfSzpFhEmS4UA74I915c19hzskT-2JFzn7qD9F8zqv-rKjHcZuZTC4XjfMyQ4L06fpGsFwa5-GAdPXPSkN1u3wLgUONP1rLEwP9TkCN-B8MYjIvGtxyDDO2tyQbHwXKlf5DexotAczNZpe8fNNdq-jxswZPycCS64eAZ82fNuhuJJ1YduD2UyDZJpgYw1oDO9bGeC2yyhsXaLPRZVshrXVMR_OO3PXPDJJezZR0i9WLbuSdUXt0wj2DCVHRDeKsz7o0o6d_5Nhj4GlPMAYtNhjCR3rpTyj8wxbtDxbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👍
فدراسیون فوتبال آرژانتین برنامه‌ریزی کرده که همه بازی‌های هفته آینده مسابقات مردان و زنان توی دقیقه ۱۰ برای یک دقیقه متوقف بشه تا تماشاچی‌ها و بازیکنا لیونل مسی رو تشویق کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/105403" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105402">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447de2235.mp4?token=fPg89FGkTwWv7oJDAO3cxs5J434Xh_pEkEjRtP4yFJ4hcqxp4tZQKAgVEs8Ie5vXVbePMM7BZca-RQfpe7Xz6aOlX981DLlw0B1KI3fRtqNmly6kGh1fw5ccmOaaiC354zNqB_9Z2IqyCJnHERADpR-znXpD_3VM3xTlmtVv3YbwT6x-HtIWH5Do2tJRgp-NaTdQCIB_vB_BwK5fm1vi5Zm8mWLu7Q1tNIBv32waVPFW1iZc_IqnjWSeh6Ap_XaMwu6sPWSZ2DqLFS_U59lIopogQ9-UEPzAuoFdGYbtvdU2GP9SeXVAe4A2dl7lN3Rm4tS78MLW17bDdZlAyi4ogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447de2235.mp4?token=fPg89FGkTwWv7oJDAO3cxs5J434Xh_pEkEjRtP4yFJ4hcqxp4tZQKAgVEs8Ie5vXVbePMM7BZca-RQfpe7Xz6aOlX981DLlw0B1KI3fRtqNmly6kGh1fw5ccmOaaiC354zNqB_9Z2IqyCJnHERADpR-znXpD_3VM3xTlmtVv3YbwT6x-HtIWH5Do2tJRgp-NaTdQCIB_vB_BwK5fm1vi5Zm8mWLu7Q1tNIBv32waVPFW1iZc_IqnjWSeh6Ap_XaMwu6sPWSZ2DqLFS_U59lIopogQ9-UEPzAuoFdGYbtvdU2GP9SeXVAe4A2dl7lN3Rm4tS78MLW17bDdZlAyi4ogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇮🇷
تارتار: ارونوف؟ هیچکس از پرسپولیس بزرگتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/105402" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105401">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
‼️
🇮🇷
❤️
کنعانی زادگان: از اول بازی استقلالی‌ها موز و سنگ به سمت ما پرتاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/105401" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105400">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
📹
مارک‌کلاتنبرگ در لایو برنامه عادل فردوسی‌پور: موعود بنیادی‌فر باید حسین کنعانی‌زادگان را اخراج می‌کرد و این تنها اشتباه فاحش داور بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/105400" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105399">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
💙
سهراب بختیاری زاده: فکر می‌کنم اگر آقا مهدی (تارتار) بازی را دوباره ببیند، نظرش عوض می‌شود.
🔵
اوت دستی یکی از راهکارهای ضربه زدن به حریف است ولی ما جزو تیم‌هایی هستیم که بازیکنی نداریم بتواند اوت دستی به آن صورت در باکس حریف بیندازد.
🔵
من بازیکنانم را تحسین می‌کنم چون دو بازی را در مدت زمانی کوتاهی انجام دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/105399" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105398">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری زاده: کسانی که بازی را دیدند، از این بازی لذت بردند و از دربی‌هایی بود که حاشیه به آن شکل نداشت.
🔵
در نیمه دوم ما تغییراتی دادیم، به دلیل اینکه در نیمه اول نظم بازی را در میانه زمین به حریف داده بودیم و این موضوع را رفع کردیم.
🔵
روی یک غافلگیری گل خوردیم ولی برگشتیم و این نکته مهمی است. می‌شد گل‌های دیگری هم بزنیم.
🔵
هیچوقت درباره داوری قضاوت نکرده‌ام ولی دو هفته است که اتفاقاتی رخ می‌دهد. در بازی با فولاد دو کارت زرد اشتباه به ما دادند و امروز هم فکر می‌کنم صحنه اسلامی، پنالتی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/105398" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105397">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRCTjaTm5yzyRytfC8e60VFkzNNy5mPObtDKTpA3vzLcocvwhYHjmdTDrXEzU7Bz4cTNbQgrKWQaUbPUijmbho1zTCRDhXa-61FVvb3Eb0bNcvuZnDL8yR4oAAxVyORONjKNtcaoXx6NFiUjbS-IubEncoh9R2BL0klyFRk45taB6TwzTZBSgFjObYF5IY0Ffr1ST1u1QyqDiHiKw8AIcCnC6pe71UySLJyFeja_jtv9DLc-MIaoJbdKTsFQUEfLE1J1DPBEFEtDiGI2nIH1lPOGH1R9i1gatgI2l2AbraiZsirsWwcNtR_Cl9ttgItbLjT80GsLWdX6k0BJ4sj5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/105397" target="_blank">📅 22:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiBi4V9Lq9tL_i2NpZOUCpdBCqlzq5TPVJ3uBPICnH0c3hSCp7Bz8sUiQGELN1jkwvhGgt5_bD89a-jGcNf_Ny4MbJHPJsJLK3KAvEbZLzQh-AmYFpNzycEAV-lrlnouFinLv608tnZBUDBB6133m5LTSwgExurFk-U5qEh6RcUsv8AnpusFYF5yl-U1IGxDnk2Rg-qLGOGvNOOjwATxswXUFbpNhj4V0EnkfJ-HkkU2LMscCTcLXkbG9AInsVHnnEvsoSotSonOYuwGH32vdWd3S1RccBB67Ta1hgWTr94nnmCDdy7dkm6aHWnckNDNqSvtrelJv3_YW_7RWQTRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105396" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
‼️
⚠️
لحظه حمله کنعانی‌زادگان به عارف آقاسی که منجر به خونریزی گلوی مدافع استقلال شد و داور هم این صحنه را ندید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/105395" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
❤️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/105394" target="_blank">📅 22:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105393">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
ترامپ: برای آغاز یک حمله ویرانگر دیگر به ایران آماده‌ایم که مدت کوتاهی خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/105393" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105392">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Ph6NOd2bi16shhNYYWHKT-vLHL45JO39HXY-B5IFce2Oe1bWhDe2loXUYlQIymWE0tQgFKavFBUDZ1oeVqyuCqfKuy2jetoCC4A-9aCcAr4BEPFlNGdJy6h_62t1GnkQWTodAHuytmqcepq2xus_rQta2q1ax2YeQBnE-jw15GO__m0SchF8LvYBo5NfcWuVS631SKZnNMb07ztzATpc8vZN4JRUEuoUFAJFLqNYpfPCFktGWft8Bn_TVe1XLTsdKKz3az7oLz7lbfeA57iNq8hKHJRiYc-Jw8cvE5SEttUP7a0yPSqEfN2rNgtZ2Dt4-L7PLSY0uoc-rDa7knfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/105392" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105391">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
📊
آنالیز گل پرسپولیس به استقلال در دربی که عدم یارگیری آبی‌پوشان مشهود است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/105391" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105390">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: موقعیت های استقلال بیشتر بود و حق ما برد بود/ یکی از جذاب ترین دربی‌های چند سال اخیر را شاهد بود
سهراب تیم بسیار خوبی را جمع کرده است/ من به این تیم امیدوارم
داوری بازی؟ مهم این بود تماشاگران بازی خوبی دیدند و باید 3 امتیاز را می گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/105390" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105389">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOmjgsIU_zxz4eZoFUC0PMkxmZZz3v2W-tTuk_mK-JY9Z-k9pzquw3wOzPRc2GG8XXKK22mZ3VXG2BUt_84e6Fk_SUS99OfRx1ytxLaNYn7AVcSGzthG1Eiuv_A20hqV2R8RaF8NUqXWp4SrVymOFebMnMI0RowWFuj2MVF47fUNwMODozUPNHK66YFlqPMfX22fug61HcI8uDh_bqrYyOtwjTGRejZwHAsrnXip31meSD1EE9voEGXqvseiNwJrtznz2TF5StNWtlXNYD5QAKhziivAerejraTx6rlLI5nu-H8WZk6XHTWy8n7jFpT4jmUPIVZN7MsEDtC4xFBjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار بازی استقلال - پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/105389" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105388">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!
باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج بازی‌های مربوطه ۳ بر صفر اعلام شود.
حالا باید دید سازمان لیگ با این شکایت جنجالی چه برخوردی خواهد کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/105388" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105387">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خلاصه بازی استقلال یک پرسپولیس یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105387" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105385">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRa0XgUC4G4QXx0YtSgwpJW_kn9f3Dot9kAiW9dRHBbpEwVYmN4bN6APyNemWLilhaPUIICfD53XC1OMYQpvn8fuDMGKbAGRjtt2dSH97--qGiVk5JEzw4Q2n7oBjpD-oRYNwar5Gt1Kxu53PxYhPzK6vC9wgxf1i5PIRkUEuUFsSx4MejsS0aNt_TFLZxGsY1Xpqb1TQJ6p2P91NThzIgjYuBTJqDFGBH7uz6tlotgbOLyektuI88vsLdTCRazUMYqcrlnfNiQsIdxbaYz1zAN2w2qnn8DKwuQRaWARz17B8Q2UZGa5l9JRe4DS-jL4U2CB3Xibgzgj_qFDsvgO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
جدول لیگ‌برتر پس از پایان بازی‌ دربی! پرسپولیس در دومین بازی بزرگ خودش هم با رقبای مستقیمش موفق به برتری نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105385" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHC4AxN9ufNZUi8EVfp47GxS1Nspq0OM6JunGzGN9lf03IYSSXT1saR4Eom6E005_tD7kZQcv05z46_RtBuyPdk0Pe5c0yeHjAiqoUwaLMyWzSqL69oZ2HhffP7pQGSSn77UHRJHG7hBKx6Cw6XAMzA_vWgsPKhaYZR6b8oeeC-97g3Nv84byi7rDPD3vflYBSODi4ZPFl746VFL5r1K3OEX5PNNuHoxsnzI_iVUXAimVnlWY8_O6zG2YAwwxUK3tAiYooiC-ffhVBbofnAwJxCz6L3Uj6KosbImv-lPE_VEeR9mFIM_bcoVUlx_HAq70kWIwQ30ILK5fUQkQI4m0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105384" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuZn5ORev9FfEUhG7y5FE2YtFGpPB9sVKcJdRhgPCFcL_7yASspsSUbrj166Q0V82SDXlgOMWpWSDBH9OtlF39JwYwS0RYyxD-yX_vnJxOeau0C0yoZQ9E3QLQg-kC77IZD7-txI72IdRzllAe2f6HBIc3Ki-htS5tL7dw4PfY0lnpPP--xDspLBvAwbskUvuGxoENxYF2cep4ItP8penKNPWOwNnmPck-rret91hNKhrEnlV7stoanspzGUhardq-veSUOm0l1g_QCQuwi8Drm-upwrpjeKabmhklm_4FnBzTL2kLLpk3YBozSvX4_yPK2_QNB1IVCUREkUA7xyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105383" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=XrJdxnG5i5MMQsTl8GVtmRLyRLzniMXoo4ppTKeTwqxLvt9v7CP0HzvRALj_G8LUYS6FT0bKN2zfc5QdgNRK3TL2QP5WZvkvkygVLQ3sYhaSzmX3m2HErT6RFY448yUAYivqzHvOOswCJaePcDK_iayn4vPGtqmNhv6Bq9MEdsK3ltwJLyuwUeVHf3iOFxr_563tsH0tAT65P2x2CoJ_H9To5lwykBoiyer54ZA9XkeSKKy8mN6bkGzzla_xgFb5pwRg9IBDWUxNDW8B2Jh_kU_ezD9Pm0Bl_2WlZNwTyx1xTHtpUfl110ryutkFpDGF-Sw1sRjlb72shIY_4ncPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=XrJdxnG5i5MMQsTl8GVtmRLyRLzniMXoo4ppTKeTwqxLvt9v7CP0HzvRALj_G8LUYS6FT0bKN2zfc5QdgNRK3TL2QP5WZvkvkygVLQ3sYhaSzmX3m2HErT6RFY448yUAYivqzHvOOswCJaePcDK_iayn4vPGtqmNhv6Bq9MEdsK3ltwJLyuwUeVHf3iOFxr_563tsH0tAT65P2x2CoJ_H9To5lwykBoiyer54ZA9XkeSKKy8mN6bkGzzla_xgFb5pwRg9IBDWUxNDW8B2Jh_kU_ezD9Pm0Bl_2WlZNwTyx1xTHtpUfl110ryutkFpDGF-Sw1sRjlb72shIY_4ncPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه ای که بازیکنان پرسپولیس اعتقاد به هند داشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105382" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=KHSJzIpkK9HHYi_viH5vQTEwTLa6EYobVgFipbB08fRnunfzEbH6OcU9MhUBK2Wn3JOgzWQMBNM6QqozY3x2_mCXqeWhCJ51J6yHBHsnl_yeahfpO_VWOkFNWwE0qwQMt9yVxUQvh5QKQgJ9XOOtlbsQBA-C87akCdP9UCXAqEeMUzj1twMtbYpcmXpRNPd1dR5XfhkdOpm0b2EegOLLFiV20hnfxRzUwnXjSJbUB3_r_m1ioxJoum3mOvzCpu6lruyvn4BXlyljruSbudSNT2mmh2rLefLUeTmgYWQomXP65foUgWASFnfMgtX5Jqhzy9QTh3Skp11zyAxKDpX6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=KHSJzIpkK9HHYi_viH5vQTEwTLa6EYobVgFipbB08fRnunfzEbH6OcU9MhUBK2Wn3JOgzWQMBNM6QqozY3x2_mCXqeWhCJ51J6yHBHsnl_yeahfpO_VWOkFNWwE0qwQMt9yVxUQvh5QKQgJ9XOOtlbsQBA-C87akCdP9UCXAqEeMUzj1twMtbYpcmXpRNPd1dR5XfhkdOpm0b2EegOLLFiV20hnfxRzUwnXjSJbUB3_r_m1ioxJoum3mOvzCpu6lruyvn4BXlyljruSbudSNT2mmh2rLefLUeTmgYWQomXP65foUgWASFnfMgtX5Jqhzy9QTh3Skp11zyAxKDpX6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت علیپور خطرناک به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105381" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcBWAHBOVo2-QomORQivWiYpf2oiuNI_xSyoqofsjOVj19_ErO3jYWP7O3eP46fkRPrcy97RHv_4X-TmXpJz-hRBHwwwCCrRSXDk5q3JN9GBgcHgg_n17GHmIHj9ISTDWBcMwpRI1FQVNFNwmposU9OxMQJ3s2Nz0uf7oSfO7mvthV14c4Buc6FbKT28neaFCYn_lVjxac-g00OSdNKQcIpcgF3RtDZZdjWPSXzk0XdVtC9REFEi29BCQStPwuklSLgEOVkUcl4_d-eMFvj3ZiRgWvZQCRw2ABHUdTs_LpxUT2SH0xB-jsb57LlO-sgTfFNXm5yJ789j7PTprcHP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105380" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=bY4Fx-OMQBNt12FR6IzXqpRX4hR1aRFNMxk6BIlA7TDHVORjPr7-f7oOKwXO-qpUNtCk01PLTU0tPio7nudlR4jgpAhMmpnlbIuHwicAiCjDFOcUZOCE42QOp8xfb-7FxFt__7exUwofDY0FeM-FvRHkdRDhm_zQF_O3D-jXFjbh2bOCt7GkFugIIGjN82sejweA0c3hcwlJxAbx_QWg9W7lmAM0ZEEVt0DiqLqWIWytNwwdRXpIvQ4ZsBTq5BiUPMCdU21IV58J_1bkKzeAgXu5BRLiEfdHtkV8HYzTrxhpxg26ORl2ear4eU0HCgsFmTzXBwjCOHNrv0Ti_DL2sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=bY4Fx-OMQBNt12FR6IzXqpRX4hR1aRFNMxk6BIlA7TDHVORjPr7-f7oOKwXO-qpUNtCk01PLTU0tPio7nudlR4jgpAhMmpnlbIuHwicAiCjDFOcUZOCE42QOp8xfb-7FxFt__7exUwofDY0FeM-FvRHkdRDhm_zQF_O3D-jXFjbh2bOCt7GkFugIIGjN82sejweA0c3hcwlJxAbx_QWg9W7lmAM0ZEEVt0DiqLqWIWytNwwdRXpIvQ4ZsBTq5BiUPMCdU21IV58J_1bkKzeAgXu5BRLiEfdHtkV8HYzTrxhpxg26ORl2ear4eU0HCgsFmTzXBwjCOHNrv0Ti_DL2sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول استقلال به پرسپولیس توسط آسانی(60)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105379" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آسانییییییی</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105378" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یاسرررررررر</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105377" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">استقلال مساویووووو زددد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105376" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105375" target="_blank">📅 20:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105374">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=hBA2Gzc7MPjczwijYqzwY0HF43kMhjThEL9t6vq9LC1YtDBsJLKLUNAcGqP-lITGQl-b35-Vy5A7Iir24yhZovbJsPGZmh5pO7DmZGXQ_Ba_-G8WBvQraGvZpXZ75_P7z9-y0f2JFvhJ6iYv50-MXRfmHOfLlIKe6MK3y3PbanERAJE8Lzsjgk_YDZTt77FpnTAXxjrXmBV2UcCWUa6EisX0VfSk0EtFXT6U5YoqvCSxl8K3_a_EaGEchAqlBImycdhdCTETgCgA3i7B1aumrP49dg0WHnGh0sLjzcqDv8_SEr3BGJgef1NJ3aEhvYDFjokgXjeY9-CjvrGXsep9fk0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=hBA2Gzc7MPjczwijYqzwY0HF43kMhjThEL9t6vq9LC1YtDBsJLKLUNAcGqP-lITGQl-b35-Vy5A7Iir24yhZovbJsPGZmh5pO7DmZGXQ_Ba_-G8WBvQraGvZpXZ75_P7z9-y0f2JFvhJ6iYv50-MXRfmHOfLlIKe6MK3y3PbanERAJE8Lzsjgk_YDZTt77FpnTAXxjrXmBV2UcCWUa6EisX0VfSk0EtFXT6U5YoqvCSxl8K3_a_EaGEchAqlBImycdhdCTETgCgA3i7B1aumrP49dg0WHnGh0sLjzcqDv8_SEr3BGJgef1NJ3aEhvYDFjokgXjeY9-CjvrGXsep9fk0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ضربه خطرناک آسانی به تیرک برخورد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/105374" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=eaBV2eqs966XVAvuwjsBnQ6lfZf23Bv1NzVSfHABG7lIN2oF82Y-Is0D2Cf4PdrFxRUrDADIWyIvpzgdJ70O-4vnDHBUxzgTDcHHpnWiOqYjxkhr8wvl69h34tKhYZ4Fb8Nj89m7zcyFye8VkNPpr1TBSMPi3NMVIyWGrDOT-5Ar-lohbuUfOG9j_Aacy8yeDpXkT6eSEs1sfLMlrfxeKn_p8lYfmf-DZZpWWL_j0yekJ3MncZXaRMFkM1ydCQMLh56hKbvYnXx7YANY4S4Kq9ITb-b8zyA1tbZgmKNq60vKeQCUHvNF9PZ9g-mXFjNSZsBQksKZVE0lvL2x2Lhn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=eaBV2eqs966XVAvuwjsBnQ6lfZf23Bv1NzVSfHABG7lIN2oF82Y-Is0D2Cf4PdrFxRUrDADIWyIvpzgdJ70O-4vnDHBUxzgTDcHHpnWiOqYjxkhr8wvl69h34tKhYZ4Fb8Nj89m7zcyFye8VkNPpr1TBSMPi3NMVIyWGrDOT-5Ar-lohbuUfOG9j_Aacy8yeDpXkT6eSEs1sfLMlrfxeKn_p8lYfmf-DZZpWWL_j0yekJ3MncZXaRMFkM1ydCQMLh56hKbvYnXx7YANY4S4Kq9ITb-b8zyA1tbZgmKNq60vKeQCUHvNF9PZ9g-mXFjNSZsBQksKZVE0lvL2x2Lhn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس به استقلال توسط محمدمهدی محبی 50
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105373" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پرسپولیس زدددذذذذدذدد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105372" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105371" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105370">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=RPhOlh0Cd7l0ARSHvORcm3jDSdHKRory8qVHTRNnvJ5-yC8yGpkVtR-ag4hJEIPLnNET3A1ecakit2rYjr9z8ak5K_A78x3vqqhnM8dVDfO21XBJOpbpniHpfrWCsv3eluvP66PlO1iTLlLtaLdECQQrdqfyWD-tcjo0Y9w_UTkPemLBgjoe4OWClUBmryWYhsa7vOAZ4X65jN0almrKjtzV5piU1sKzONknuaQ6MRhzM-djkrCxM_9hE62dpEZjw-rBEmltfcL3NJcMTuv_tmMlkVb2nRfo_Fe4FU-cqGv2FesmZgChRfN5P5DKsJBPyuzBx03q-xz2qrTboaxlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=RPhOlh0Cd7l0ARSHvORcm3jDSdHKRory8qVHTRNnvJ5-yC8yGpkVtR-ag4hJEIPLnNET3A1ecakit2rYjr9z8ak5K_A78x3vqqhnM8dVDfO21XBJOpbpniHpfrWCsv3eluvP66PlO1iTLlLtaLdECQQrdqfyWD-tcjo0Y9w_UTkPemLBgjoe4OWClUBmryWYhsa7vOAZ4X65jN0almrKjtzV5piU1sKzONknuaQ6MRhzM-djkrCxM_9hE62dpEZjw-rBEmltfcL3NJcMTuv_tmMlkVb2nRfo_Fe4FU-cqGv2FesmZgChRfN5P5DKsJBPyuzBx03q-xz2qrTboaxlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار خطاب به بازیکن پرسپولیس؛ پا نشو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/105370" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105369">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=Th6-CvvyCcv6GGc-yiYtyg2o00bX7YIhWwvaLgskjDQfJjMpYGouT-AOg8BCc_2v-6Ok2z4r9wdgxSq8ePlFVxqIGFxFeD9oPrHe-ums5vCPWiiZIHWtxzA7CACKjYSpFarE7banZt2thq-YUgUYDfZmu2ULpuu5mrlwKnpWcJrTJlf0XaiWEKP-BBbx94h8lNh-jXtXzmKWtEfohKR2eQxvBfhiDh-n20AsWyOAPNe21p2M6bAoUwRSR0KRYgNTgIvf0fBpnp4DpbONUUrsNNsFzA2J5GCQr8dGS1WUMl3mgzLZbpJoYaAAGq4pDbhejGB2SxLhfS715XgwzSlXJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=Th6-CvvyCcv6GGc-yiYtyg2o00bX7YIhWwvaLgskjDQfJjMpYGouT-AOg8BCc_2v-6Ok2z4r9wdgxSq8ePlFVxqIGFxFeD9oPrHe-ums5vCPWiiZIHWtxzA7CACKjYSpFarE7banZt2thq-YUgUYDfZmu2ULpuu5mrlwKnpWcJrTJlf0XaiWEKP-BBbx94h8lNh-jXtXzmKWtEfohKR2eQxvBfhiDh-n20AsWyOAPNe21p2M6bAoUwRSR0KRYgNTgIvf0fBpnp4DpbONUUrsNNsFzA2J5GCQr8dGS1WUMl3mgzLZbpJoYaAAGq4pDbhejGB2SxLhfS715XgwzSlXJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
طرح هواداری دو تیم روی سکوهای نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105369" target="_blank">📅 20:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=R96ytiwBb3wtv_r1UIq2Pm-i1nSAP22IaIhdnPus15mgm8WSaF5xpOgImMbf-6wUEyfbJbW9r7tCftiAYux3VKQkpsasmUm3mRg0qugILsWNNbm8E8qOXz0y0Gs4CSZp8_zjT7buHfWaI-wndUDL39UVZ3_C4HzMQay_lIbGKCBo9AbG8gXAWyNI9Bbq5Zs9FlGZqDpNMLcqZClmRQmAIXYLTWezMkFrvYPiwJcO0qe56fsEoe1LbDTQU06sZz1iJ86uUHPcClmomidRXEN9Lf6hx2bPIBTKRFUHAMClqwWNeyS8-7HMTt-IS9pSzG3868MmIvym5D0wdWNgEf3T0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=R96ytiwBb3wtv_r1UIq2Pm-i1nSAP22IaIhdnPus15mgm8WSaF5xpOgImMbf-6wUEyfbJbW9r7tCftiAYux3VKQkpsasmUm3mRg0qugILsWNNbm8E8qOXz0y0Gs4CSZp8_zjT7buHfWaI-wndUDL39UVZ3_C4HzMQay_lIbGKCBo9AbG8gXAWyNI9Bbq5Zs9FlGZqDpNMLcqZClmRQmAIXYLTWezMkFrvYPiwJcO0qe56fsEoe1LbDTQU06sZz1iJ86uUHPcClmomidRXEN9Lf6hx2bPIBTKRFUHAMClqwWNeyS8-7HMTt-IS9pSzG3868MmIvym5D0wdWNgEf3T0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
موقعیت خطرناک یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105368" target="_blank">📅 20:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a811272008.mp4?token=KlyM1NunJElCEMbfd8Dvgxc4rBd2mEYh7yxtnQqqizXCPCoVtn6NVwwWjgKvM46l-kHNasLpgCuepJeRjDDLJNtoFdTl5ynRhS08wiCyRH6sUF6G4AWpCS3B_6ZYGSsFnmoIWP2iDjTx8F441aZFdBH4fOyF4m6Q64RCo7999pwS9joG_cmJqJb2HMmdp-VsSfDbgDvFtVjJl6VRihgu_-V906GDVQGvyMrO2YpFLdln22-5yNpED3TqSFheZV-NjQCMvPNSAxFeJNcEGS1-SW4kkFa7dRI6ft4NQo1dAlEBzbUrLcyJqomMf-hf1cW3R1CWV1mkNCIY3mY9ZW6dtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a811272008.mp4?token=KlyM1NunJElCEMbfd8Dvgxc4rBd2mEYh7yxtnQqqizXCPCoVtn6NVwwWjgKvM46l-kHNasLpgCuepJeRjDDLJNtoFdTl5ynRhS08wiCyRH6sUF6G4AWpCS3B_6ZYGSsFnmoIWP2iDjTx8F441aZFdBH4fOyF4m6Q64RCo7999pwS9joG_cmJqJb2HMmdp-VsSfDbgDvFtVjJl6VRihgu_-V906GDVQGvyMrO2YpFLdln22-5yNpED3TqSFheZV-NjQCMvPNSAxFeJNcEGS1-SW4kkFa7dRI6ft4NQo1dAlEBzbUrLcyJqomMf-hf1cW3R1CWV1mkNCIY3mY9ZW6dtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
فرصت عالی علی علیپور به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105367" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=GHo_ZtTY5GZ6gv5U8IFN_VUvOzVcP1d8nParMcBphYdbgf-L7idpKDlZ8dANYcLRgMRDMAU-f31cuSZ8Gk_iyad6CD3d8Cv01qcnoVdUb_TqKBX_cb6s7zYW0RhFqpaDnwBVqtC3XcyI1Y5RKWkIdr7uSRuKuCJgfNFUTHFhKMYxF_jf9b_dN51lUVLUR6LoW2UumJenEdZAdjwnwyJZ9Dz5ECyOjk4u3CTph68EPL0SkSPDtqIZ0zYGTxrv1L6jKZgKrdg9lgh5eJC7jrke_A3gW1QOaHS0ALqZ0W1PVwOQCXOzp0vlJVsN0iUKd-4VgJaHNYtm1dFskFtbhjH7Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=GHo_ZtTY5GZ6gv5U8IFN_VUvOzVcP1d8nParMcBphYdbgf-L7idpKDlZ8dANYcLRgMRDMAU-f31cuSZ8Gk_iyad6CD3d8Cv01qcnoVdUb_TqKBX_cb6s7zYW0RhFqpaDnwBVqtC3XcyI1Y5RKWkIdr7uSRuKuCJgfNFUTHFhKMYxF_jf9b_dN51lUVLUR6LoW2UumJenEdZAdjwnwyJZ9Dz5ECyOjk4u3CTph68EPL0SkSPDtqIZ0zYGTxrv1L6jKZgKrdg9lgh5eJC7jrke_A3gW1QOaHS0ALqZ0W1PVwOQCXOzp0vlJVsN0iUKd-4VgJaHNYtm1dFskFtbhjH7Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
بهروز رهبری فرد: خیلی دوست داشتم که جلالی در این بازی باشد چون نقطه قوت استقلال همان سمت است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105366" target="_blank">📅 19:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRPXeMtOTHJz4DlFgAiEUr32EjhT40x70E-r5IB_ekvH9sxdPjgL0LmdfsQyfhUSKz7e6NdTPgWOYqYFUPhE3-sLZbPtlGLXg-c52J4neB5sQPKCL6LGENBQt0hxzXFgRR2S1bz8FUquXmV8rytZFZiHLzIVTXxVH9i7XFpLIUO5sxVbGmk8yLAX7WpDhA_yu9fMs4i4MKLs_WHVc6y3qlaMe-0lWYOxsR-lxq7wL1SZ0kwssubU227z38dSXQf5s6rml-XZlqNuN64Zp_JhNfDvZW6fvRarp9IDxSiW6SJ0y5MmMYqIlv7RuYUliljReQLVKl8qb18UEXoZZOIuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
ظاهرا جدید صالح‌حردانی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105365" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=B0DvnnJkQbnxAZSofPkMtaFVBiLD0g3WuUqAUImGnC_WdLo49qmsDO5tRMbRL81cEGHekopM673O01Se8aoRjEaS81aU-I6YQT-LnKm4FD1apsPt8_6IMlkfPNQyZE812mrgglR5GPIO-M2_xVXBzlXP2GG5d2XRLsf9nwfgabae3wbAiNmVm_XSk5-yke_XVO2_htv8YOoBccsGTG9alyNVA938L8zzZcHc-CqRvX0mxRDoeq-8vgwmRC7HDbRiDZ55pQnKLNBKramlMvekw_RWUBxUGMHJtv4AfTIXAxQaveQuoA6xWR7xCBAm-zOButJKWO9CowdfbbYvEDCmpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=B0DvnnJkQbnxAZSofPkMtaFVBiLD0g3WuUqAUImGnC_WdLo49qmsDO5tRMbRL81cEGHekopM673O01Se8aoRjEaS81aU-I6YQT-LnKm4FD1apsPt8_6IMlkfPNQyZE812mrgglR5GPIO-M2_xVXBzlXP2GG5d2XRLsf9nwfgabae3wbAiNmVm_XSk5-yke_XVO2_htv8YOoBccsGTG9alyNVA938L8zzZcHc-CqRvX0mxRDoeq-8vgwmRC7HDbRiDZ55pQnKLNBKramlMvekw_RWUBxUGMHJtv4AfTIXAxQaveQuoA6xWR7xCBAm-zOButJKWO9CowdfbbYvEDCmpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😳
😳
به‌قرآن خاک کسخل‌خیزی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105364" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=lAyNQvU_mznrFtiyxjSyvThCYOhZhykQxEci2_UMY31wd4LbzR_tn1j9LulYrfh4G-tpj1O9jP9ctCKeWWyZS5Peg4PXX_Qe-WGBnXVEnxnjaI9pkjF_YyHRbMsIqqd4zSFm1G3agl9K_hodNrRfksVo72JjJkkegaLZ_oTkjxR6KfqVLH4YFRyKz6-bRSyzIzyjrDTZw6cEOcgR-uimCUF8vvGUFYzVgtwE2pE6H23KKr8PLiqSKMoVBwzmJ86msU_tYkUNR-8YBrKQFoztLiF-D5DxffH7TGPN4x0AxFdH39paPLr52nh-B_I3htvg6hLm-FZS4LxdGyzxMi4sCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=lAyNQvU_mznrFtiyxjSyvThCYOhZhykQxEci2_UMY31wd4LbzR_tn1j9LulYrfh4G-tpj1O9jP9ctCKeWWyZS5Peg4PXX_Qe-WGBnXVEnxnjaI9pkjF_YyHRbMsIqqd4zSFm1G3agl9K_hodNrRfksVo72JjJkkegaLZ_oTkjxR6KfqVLH4YFRyKz6-bRSyzIzyjrDTZw6cEOcgR-uimCUF8vvGUFYzVgtwE2pE6H23KKr8PLiqSKMoVBwzmJ86msU_tYkUNR-8YBrKQFoztLiF-D5DxffH7TGPN4x0AxFdH39paPLr52nh-B_I3htvg6hLm-FZS4LxdGyzxMi4sCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
🇮🇷
هوادار استقلال به سبک هوادار معروف غنایی در جام‌جهانی، با طلسم اژدها وارد ورزشگاه شده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105363" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105362">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=F5Kxk8AL_z68FQfb3fh6ieGSw70aEmtlwgK8Cct5znZ64KWDse-1WZOLDOqSPQqSi_QQTLItnRh4pOrmOd2dZ6yBDy1gpWn0RaKmjGRCnkFsVyWmHmNoFAgQcx_4ww_53b8CkAW8HGmzyD6qHDst8XWx9fO3fUDU0Nm99wsX_R8AtjwKBe5S8JdkOq0h-GCngUr5suwOOfzbaMLcpbVFzanjjQrpzFiuSDE1btLToZSSK0KdMyBqdAJpZ0o7z7H1s6BS7hrkWk9n-rwYVN1YNXsTk-GH1gv4hIElv0hLRsd-wa4YO_VakKFz45I2XeKVItBRNcfTShSfmy5c5d_IPFQCudC6I345GVD1BBuuk21ciyG5deR_1TexdDy7J9jjMRRMzDKLQTKqK_zrA7grIzd5vq-YHHuobXuv2NqlqjLmpSuO00kumPNHUAuKCyzWCvgA_fRrRXXIGHHlAAd1jBwouPFFxxV0YUiXai-TPnxhBu2UT6xtt_Ocmye__J291qpDVcTpqpEAtiappxO9cYdeTiSspmfuwOZGJxeNzukwbrvagpO4ZFhb-LmNyon8YdBX1-HYITffx4WFKQ1IbA-W_lqGsu9A_ZGQ2KPbMw4D1RU656jROt9Nu0PlZ7sSSekPwfaEpsoTLwbU6T7W5aZ71J3yfpjrhuw_dXKEzNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=F5Kxk8AL_z68FQfb3fh6ieGSw70aEmtlwgK8Cct5znZ64KWDse-1WZOLDOqSPQqSi_QQTLItnRh4pOrmOd2dZ6yBDy1gpWn0RaKmjGRCnkFsVyWmHmNoFAgQcx_4ww_53b8CkAW8HGmzyD6qHDst8XWx9fO3fUDU0Nm99wsX_R8AtjwKBe5S8JdkOq0h-GCngUr5suwOOfzbaMLcpbVFzanjjQrpzFiuSDE1btLToZSSK0KdMyBqdAJpZ0o7z7H1s6BS7hrkWk9n-rwYVN1YNXsTk-GH1gv4hIElv0hLRsd-wa4YO_VakKFz45I2XeKVItBRNcfTShSfmy5c5d_IPFQCudC6I345GVD1BBuuk21ciyG5deR_1TexdDy7J9jjMRRMzDKLQTKqK_zrA7grIzd5vq-YHHuobXuv2NqlqjLmpSuO00kumPNHUAuKCyzWCvgA_fRrRXXIGHHlAAd1jBwouPFFxxV0YUiXai-TPnxhBu2UT6xtt_Ocmye__J291qpDVcTpqpEAtiappxO9cYdeTiSspmfuwOZGJxeNzukwbrvagpO4ZFhb-LmNyon8YdBX1-HYITffx4WFKQ1IbA-W_lqGsu9A_ZGQ2KPbMw4D1RU656jROt9Nu0PlZ7sSSekPwfaEpsoTLwbU6T7W5aZ71J3yfpjrhuw_dXKEzNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
شباهت گل‌های این فصل دو تیم به گل‌های به یاد ماندنی داربی‌های گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105362" target="_blank">📅 18:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdICaVspJz0pJuSt-_lXaMH46ICIy1eRtjcVBHskwmBr44fIWmgXMvvolmpbCLGSbPwMr24-4Vymw_GfFPa92IiHYHK_k0jrwlG0tGaAcrysinfIrUF3_POq9aeyt0vMPrJlH-cc72lnx8vxSiM4Sf7FeNjFb0mQRDrsWBOygANgjhRqFaz3xv_2hd-m3kYyFwV8z4RdeHHubSkj7t0vVxdd6GJA8M4Gw3wsdC5iJ6hP0fiooHTtlIJ2izqPY3yLT5dFvKwKZe1-rch5sBtR8Opx850bA68OUJC_572Aj1lrDDzdh1lGl0P6iKmmC2E9uaNwFehKFVvyQ8jcWuQL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇮🇷
لیست‌کامل بازی امشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105361" target="_blank">📅 18:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105360">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=lO2FG655Fu55eud8QoO1jJyqBdnIcac8mBxVi5HzNO3zG3lFqhiAiWyTmZZUK7VIsELg5Tmc2-PNOrW6mHZVHxP_oaUoeD0l09mWA6WBgtAI50ciUCzmEflwDyvo89T39H0xDJoAsv2tm3KMNLGCMLNs3f4O-ZxYAJ12q1wYoaPLjBdOYEatm8meg6hrexh91oOr8wlb-CyNebKCE7tbj5xV1q9P9XXirDJq9TIB30LeFJOxfEbIwaSjQ71hq3pddfw65HVW1rrHkqs7xXmlcwWm2QkHqnkURNzW7Jkl_hwdtNWPUKdexT8ReIlB83g4qDeuzHJgtzDafmlHiRovdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=lO2FG655Fu55eud8QoO1jJyqBdnIcac8mBxVi5HzNO3zG3lFqhiAiWyTmZZUK7VIsELg5Tmc2-PNOrW6mHZVHxP_oaUoeD0l09mWA6WBgtAI50ciUCzmEflwDyvo89T39H0xDJoAsv2tm3KMNLGCMLNs3f4O-ZxYAJ12q1wYoaPLjBdOYEatm8meg6hrexh91oOr8wlb-CyNebKCE7tbj5xV1q9P9XXirDJq9TIB30LeFJOxfEbIwaSjQ71hq3pddfw65HVW1rrHkqs7xXmlcwWm2QkHqnkURNzW7Jkl_hwdtNWPUKdexT8ReIlB83g4qDeuzHJgtzDafmlHiRovdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🇮🇷
یاسر آسانی رو به هواداران پرسپولیس کری‌خوانی را آغاز کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105360" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105359">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=vTDUWCr0sNRVHv9ogoz8oRqZwd7UEFWARo4VqmizDQeo24t2r8DDpVlzGRzrUrU174v4oe8yqM_a73bZ-PdqZNX9LtdVdVBNxuyxbcEb7St6MvtZm-MwUTBIjvzn1m7B8ZL8izWuKaxN4AeKn9JTFYID4L78zf0ikcy_bQ-IesSJkPqxn7Q8CqCKtxEqilh1u6VcTWfuzaADUoA6PA27uMbioWwaS6oGBXHdtiHiH9rBZcQDxRgZW5E3Tb3ySVOH4NzNWG0FZuMvSik2AQftKtzVfxWs0XcEO4K2d4UNcObUWkzABk8YBDfczIQceGD3Q4-OYkRY2tsnI8xgYHAGmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=vTDUWCr0sNRVHv9ogoz8oRqZwd7UEFWARo4VqmizDQeo24t2r8DDpVlzGRzrUrU174v4oe8yqM_a73bZ-PdqZNX9LtdVdVBNxuyxbcEb7St6MvtZm-MwUTBIjvzn1m7B8ZL8izWuKaxN4AeKn9JTFYID4L78zf0ikcy_bQ-IesSJkPqxn7Q8CqCKtxEqilh1u6VcTWfuzaADUoA6PA27uMbioWwaS6oGBXHdtiHiH9rBZcQDxRgZW5E3Tb3ySVOH4NzNWG0FZuMvSik2AQftKtzVfxWs0XcEO4K2d4UNcObUWkzABk8YBDfczIQceGD3Q4-OYkRY2tsnI8xgYHAGmIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سیروس دین محمدی: قبلا اگر مساوی می شد حداقل ما همدیگر را در زمین می زدیم جذاب می شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105359" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNyV6M23Pg0kjZsGq9eItU3ruRmNXS1rMivH0u-Eff8Vov7dORfKq_OCW1mq4ScUJYzxeZT0EKC-HfzDV1AW2o_JIBu2WgKxivL7HrdxyZtVwFcJjDyY86sedHnX-24z1ueD0d77V4Cgr_ImhJX5G0MJFAGRICU3Qh-MSJD4zLYG5U8esJ7RG9vYTrJcSqV_0wnFgaok0bKtLFsfRsYR4A54Hvu4_ghbV5digPyqyyTkswMLT7wX-hdvJDAyd6v4UIpo3j-f0q0p9v-UflFa_0Zb3u6c4EozEhCgxFsfChX1JJeuxUcKcoeWwP40MUJH1MEwThbuQgJ1doI-7OeL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
مقایسه نتایج سرخابی‌ها در دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105358" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105357" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105357" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXkptLueLcRmgxRpJUNecQXG9OHF4Tf3HUrLEfyAH7E3vWRfSvrHRaoDbra4h_jtXabidubrqnkKvLdmEIaTaBK6YemQygfUf2nuFpKFVnqEzFRq-WCjnfIaQ592YJaqFVP60e2zI3ccFjymCLC2NM5MdIuN0ufBeWrYUcRBWSEL8jQ1fc14GWbDpu46ucDgKRQdlJx1KW9twDU_PFKS4qqfMOLvFxUcazzVNGFAA6xjMGiWHfMli131FBvN3_udXoI6dD3EtrkguyayL46lAyieVAPI2_CNrKFKFU8q4-CtVye4w9nfGUHv3i56NfJG8-JR6hzWIZ7IAscl3UeGig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105356" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpnTXqlaujm8ZLS9JhVExO7xZjMmv3E5Z6xHWMCm1wumtCqaC3YBMnAzwiYGukxi3MwhFBoN-1jtP4gJCST9Fu8XpSi17yrSmP0QMQ5zqnJMETMJVhQtctvVszRR1Uch3xB54TE6uhQSDbWrw7lqdegvyxWnjC4TPXPRRDoa0uet9iegcVT8Mqz8TppoHQwwZ5UpFZ7iQ0NqtXFEaiBRRLwnwnOpnjvbaVcR75NCDeSvarPKS1yDunvODizks11BMa11y9MkB81ZMJn0QLpl6KXpm41pZwgRoXHVDQm8SQhVaTTD4c7IYtxXLQpznY2sPCOzwhN9p6TDqqTKy6bK7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105355" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipUEVwxmsjpltgcs75fXQKT7eWGhBTRLLG9SQ_d-YjjaisSS64N5fBt2E5w5U4gVjjTfJ1bMIzv9VwH4Ui9tafj9UooDUAOmfDNirwWHmLzV69w1AN1GdLqjwp-6HCo7cW-2fsxGxByPMogbEkh5vFagNTEbbV_T7v2O4QinA2tMD6UN8Z0VA1M95A13r6FLoxyZ5KiJsrgTeCF9B3E7oC1sqYozKD6RL40wfz86a8gp8Jk7goRzFeQwDfyw4nOe0jF8OY6epfHfog2B02QN5DpH7sBJGMbf6BvlIwmlwu2F3zxsD8Q-7nEExoihswpb4kjAtmPRSCSupajJNAJ3xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105354" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYihNPdgn1M6TzIxAb7zHsOx0l8L-mI7JlQn1LuL-DxdK8n0Ae2AxZ81HPBi_GBbAYFfcwLeDinJynw8xkKwCg6R-TcrJ6e8Ks864fcUlet4bhzZ4ELESMO_9chP5UVr0Hrg0BzF6PZHUDK8gTB9LwpaY3IO204SJVrqYGA-xKpzyX6ck808rR9E-jNjs4TT9zAJ44vcjFuirX_U53WPMX7TWd34gRr_6fZb16E2pQN5qbgntwIwgwFTPLYEZqmqSxbWijtHWKEm4dGuK3Bmw9aUsJVFSBTKOS7I0dLWvsX6eheFmIXngrPkm176HGVaJQ7oWIDc6Sw9fkSikZ4wqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105353" target="_blank">📅 18:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvfTubKzWZWab14Xzx0f8j-xuffkA7N20yQC1jmx6enk7vOX-c4T1FPScAEjH4JYEeOZvJ24XklUbCztXy9DRdt2ZQWT0NExm8_JXh-lnpWIjFhVf0lsbgrg_4aSz7MUSoxm8a6DLbGJbJiqNilWruoofCwVeObga7_FCLBxnhYJJLOrK8Pg3jLopngcb7UOBuecogZPEhep2L6fwrponimhGZfz-LLgAqnwX8cXa_-6Vg0DpDs2jjDe61i_mlnyTJWnyDjHfoaKmIFHNO801VDT8YdeM7iPfmmlpZ_nM0MQInruQYMOmwfWXn43Hl-ezzQRcnZ5SF_TZLxYRcZYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105352" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=M-ZDZwNNQIZeSzyJ1UTk3BUh9Waa_AOsRWJXTajaya3SWpWZPmESsWePPQietAvVcvfTXoQsLtdZnb35v5F5MwyZvB1jEP4HXVgBxV76n-TDPE4ij-nHMYaTqmGQbuyaTbHhAjxZQnI-C5cbacNwucR8zW62drwUGmCsngrBh2mOKxiMMp7Co_U1Gr0_j8gr2-zt57xATQaWguT77JjWQClxDmK8KH3igmq8f4lSt-XYmERg3xW4Un3jTciSmIOnwiP1hqoQ3eP1ZlWr7zamui20E3JmFenB9buBLuvRc6c_Cb28n69mE78IX_nrZ-CaD2JLMqFKFejf4bnQWEsQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=M-ZDZwNNQIZeSzyJ1UTk3BUh9Waa_AOsRWJXTajaya3SWpWZPmESsWePPQietAvVcvfTXoQsLtdZnb35v5F5MwyZvB1jEP4HXVgBxV76n-TDPE4ij-nHMYaTqmGQbuyaTbHhAjxZQnI-C5cbacNwucR8zW62drwUGmCsngrBh2mOKxiMMp7Co_U1Gr0_j8gr2-zt57xATQaWguT77JjWQClxDmK8KH3igmq8f4lSt-XYmERg3xW4Un3jTciSmIOnwiP1hqoQ3eP1ZlWr7zamui20E3JmFenB9buBLuvRc6c_Cb28n69mE78IX_nrZ-CaD2JLMqFKFejf4bnQWEsQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
😳
ترمیم‌ناخن‌های علیپور در آستانه دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105351" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=ZO3p9omLMmS-pI535Tta2N-n9KeqcTAqlTjs8GT83ESk29mmBk4CXmZ52jJj6rOclmv8BPgMem6Delm6yxMfDB0uyZyLRsOTHlfLKWKwqxHJFnGh33GHdC7hgMjanV5HypQm1sp1pjFFBg7rWbp5BhfQqNZ1XVhOVMGCNdFfltERIEYLGXh5HApLTJCPqYnRfFlGTDDwFWG-Bo6GFsIm_WtpOtPcghaZNQq2ImhZWrcW7hMVgSy83wd7AYlfnY8Q81HCodQToQxrQyhccYY_gJF8b_TMA1H35kJubx5W0skyErx7YnqzCQhhOBLWSLTZ1iZxPjJHIkrFfMiTFkVjlw_aMqHeNcEQ2EiL7ZOiTRt-9hmtL_LKfscsNZnJ9GG5TchvG5SpQmE2XuUFiYRatc8BZLY4Cb94Ek_ZRKz-2m5OXFKcKfa-j3SCveipclcYYIFgTxQA8G6axZ6uVBHpddyt5Rpdv8zLYfuQekC3rFPJcHle5bI_6sq7xz0CIOiLV_DrYTa7H2kNRsxPsUZaXRhOau0TiBFjpOMni80IjArZIMmhyXGgQhezVnL7JvdNJCh1lwxDdo6_bj7V7iOM5NZy5SvzVyQX-hsQoWprJrunyln0r2l9WOfFfodWaxoHcDuuK5Uk3lfXmG2Jv3a_8eJ2a27qKI-L6L8_2DayTE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=ZO3p9omLMmS-pI535Tta2N-n9KeqcTAqlTjs8GT83ESk29mmBk4CXmZ52jJj6rOclmv8BPgMem6Delm6yxMfDB0uyZyLRsOTHlfLKWKwqxHJFnGh33GHdC7hgMjanV5HypQm1sp1pjFFBg7rWbp5BhfQqNZ1XVhOVMGCNdFfltERIEYLGXh5HApLTJCPqYnRfFlGTDDwFWG-Bo6GFsIm_WtpOtPcghaZNQq2ImhZWrcW7hMVgSy83wd7AYlfnY8Q81HCodQToQxrQyhccYY_gJF8b_TMA1H35kJubx5W0skyErx7YnqzCQhhOBLWSLTZ1iZxPjJHIkrFfMiTFkVjlw_aMqHeNcEQ2EiL7ZOiTRt-9hmtL_LKfscsNZnJ9GG5TchvG5SpQmE2XuUFiYRatc8BZLY4Cb94Ek_ZRKz-2m5OXFKcKfa-j3SCveipclcYYIFgTxQA8G6axZ6uVBHpddyt5Rpdv8zLYfuQekC3rFPJcHle5bI_6sq7xz0CIOiLV_DrYTa7H2kNRsxPsUZaXRhOau0TiBFjpOMni80IjArZIMmhyXGgQhezVnL7JvdNJCh1lwxDdo6_bj7V7iOM5NZy5SvzVyQX-hsQoWprJrunyln0r2l9WOfFfodWaxoHcDuuK5Uk3lfXmG2Jv3a_8eJ2a27qKI-L6L8_2DayTE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کری‌خوانی بازیکن اسبق پرسپولیس برای امیرحسین صادقی: آخرین باری که استقلال دربی را برد، دلار ۴ هزار تومان بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105350" target="_blank">📅 18:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=swMhHPvDRW-vdtB63B-QvUtpvEgpqCMfdEqrAyJIYLk0w3S3H4gw-ozqaT_MU6J3h14hGosGzGcWcRvhukwej9OCXv6qycHScLHn5C3W-XO6H_-dEIclqgUcu99uy5OX3qyvwZynDgY8RY5uFf5f85aKnzWS_kg6IktD7ybD7qqiycekXdhzZ_OF0A7-0KzhlL0Wqqbnatxh20Pp4ap-jwXl95rsDXYQ3Z6BOUnW3NG0--V7aSqr8sCVwoN_bS7t5_4KpvMpbMrf_V2ocafpe3avbmp71T5hgRNl9Tw4IoNJHkuuY0BOKkFivOtRI6drvUJL18PysO5E6Dm2fZ09QJ0uhYj7DYVU_rMf1CK_EaItTCRm3qJ0xAwcj90Gk-Nwc2ZhGkM5SQbiF6AOogFEZzNDQTO5EztOACgyPwnPS5DWQ4XpgPJvhshwi7bPTlRO1cFrKHzduh3JRbglHVm9hQdijtyyYEeUrGaYuMKBTqlnYwrFYtJMbzPkntIdfYsw15Fvi6_DgUuBXq63aiaBhsk_iyg2LGKKpKrolYSqm86XgiV3UN_AbRWxj1GWmtUOXejjhC2yYTS8QRFQXXnmu3aPshehFumgPeFq_rqYg7P2oWNYQivpXjR0E7e7z8Pccgtrx-Zxd0AIdzJZx1OeMnq813gtE9Aymk-E44LRJgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=swMhHPvDRW-vdtB63B-QvUtpvEgpqCMfdEqrAyJIYLk0w3S3H4gw-ozqaT_MU6J3h14hGosGzGcWcRvhukwej9OCXv6qycHScLHn5C3W-XO6H_-dEIclqgUcu99uy5OX3qyvwZynDgY8RY5uFf5f85aKnzWS_kg6IktD7ybD7qqiycekXdhzZ_OF0A7-0KzhlL0Wqqbnatxh20Pp4ap-jwXl95rsDXYQ3Z6BOUnW3NG0--V7aSqr8sCVwoN_bS7t5_4KpvMpbMrf_V2ocafpe3avbmp71T5hgRNl9Tw4IoNJHkuuY0BOKkFivOtRI6drvUJL18PysO5E6Dm2fZ09QJ0uhYj7DYVU_rMf1CK_EaItTCRm3qJ0xAwcj90Gk-Nwc2ZhGkM5SQbiF6AOogFEZzNDQTO5EztOACgyPwnPS5DWQ4XpgPJvhshwi7bPTlRO1cFrKHzduh3JRbglHVm9hQdijtyyYEeUrGaYuMKBTqlnYwrFYtJMbzPkntIdfYsw15Fvi6_DgUuBXq63aiaBhsk_iyg2LGKKpKrolYSqm86XgiV3UN_AbRWxj1GWmtUOXejjhC2yYTS8QRFQXXnmu3aPshehFumgPeFq_rqYg7P2oWNYQivpXjR0E7e7z8Pccgtrx-Zxd0AIdzJZx1OeMnq813gtE9Aymk-E44LRJgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار پرسپولیسی خطاب به استقلال: دربی اصلی ما با پیکانه، شما ده سال مارو نبردید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105349" target="_blank">📅 17:57 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
