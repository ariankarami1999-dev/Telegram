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
<img src="https://cdn4.telesco.pe/file/neqDXHuiCjcoNMmLf5_NQEMaF7HxQaXM24gNGzFxWwM04TAual-jt8djZn1gR8_hGoi1v9-AbMSuA7N8W1LXQDKZww6AJgJR3xg0BKnRl4uO7v8VFi8MvPe3ED64Gxr-9sE8bRrM1hQznjzqQfTspbcIUytlY9jDrJ60IAoZn2gyApeklGhTivmSnHSrInkFDcaC7DSOCFWyNiHqOx9NP5mCOsg31ome_ALDB8Qzi-nHB04vcyEnUKXHoNBnhW7S9Ag4-9dlsC7Dhteeob-GwhLi8bbZvOCttVWT_OSqppa0PC0VvkOsbInZ_hZkoV5_LeOQ_DkzVRKy9xWdEEOLdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 03:18:30</div>
<hr>

<div class="tg-post" id="msg-462724">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c730A4k6oKmxCGQdbyesiQTQndTZLRoRtfSUilr_jlujQ5lAMgWtDiXiP82wqgUD5AAJrL7qMsHdbJKXkfx5M7jlrPndD2s8tVWP4t8dv9wE7Wy99CJc-hkh3f1kOxs-p48BQv5eQkYI5LLXYXtCvCcZT0ZZgREncZucojcucX6mwBCcIbo_eCVedARTbNBUqrlU1Dq_bAxVl1kueNwPuqxOoaIhGwX1P_9zP46ouGypHdtpX6uNUGcRgKIQNnSTr9Kyasxf6mmwaKOv0a_2voiP3lPM80r_5rHzEOm9kDfHJT1IoVymZ7doNZAOl3huEHi428eHy7EmRT0Gkx2sAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریل‌گذاری تونل آهوران پروژۀ راه‌آهن چابهار-زاهدان، در کمتر از ۳ روز
🔹
عملیات ریل‌گذاری در تونل آهوران پروژۀ راه‌آهن چابهار-زاهدان با فعالیت سه‌شیفته و در مدت کمتر از ۳ روز توسط قرارگاه سازندگی خاتم‌الانبیاء(ص) به پایان رسید.
🔹
تکمیل ریل‌گذاری این تونل، گامی مؤثر در مسیر پیشرفت و تکمیل پروژۀ راه‌آهن راهبردی چابهار-زاهدان و توسعۀ زیرساخت‌های حمل‌ونقل ریلی کشور محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 512 · <a href="https://t.me/farsna/462724" target="_blank">📅 03:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462721">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACD9qnj7k-gI8NGmK1cUmnC7RoSs4j338ibCDLDWS9_a9aRAMNfuko2eJ7bgguQ6LFrCiXGNgOPilM7k-9bH9Yrs92DL5WZyuVp8Qyuys1beWefN3kdDh_DKEwX5-jI6fxkyEiY3sLsWr5hijfm-46Xg5Yw-f6EWOzNV-xRjAFHPgVQnTTXm3ab39LDqMbgQoXQzMJZxQLH8ikekItktwELCB0NXVOehUglFUDNL0cLk_CyzzBswLfJKQbbl9Vir-5wavoezPYAeEvjjASPlgrkN3ZVfkgm_XVOCCsbsg7HmAV-QzGAmrASQktyGBupZmG1W50DLVOmU9DZl6OuquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-ZTe550vBTxuIKgy_1KgdJDCCjFBKgdERur_MTHuriIhph_fq9LyJ3kHsAL1yFFYyBdkWJ2GgSmLZ28LKEc59vDCgHIddFiNqr8EI_3SrkxfRVtFj6olf8iXp8Y1aggyFIS39YiFwxonFIigD9EUc4X5FP-QrfowgSBJrnsLHfVxePYetPKTgtZr4d0TG8aQCL1JImI_-3ejiqZXQEL4zIxWD1kGHV-gogTVDH-pYzt-2d8MBCGtYB6waW_afF2h9kxxNdrfjFqX3UyxTGxYIDOEg_CPARJ35cgxdWnYEZ5g0C9rHJCrw90XJveOE_ZfByzmuU_VI5Kw8P-rI1F9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkP48WZSGLc8dy19Yi9-fNwm52Sf5hbL9dM9SxLauCG2qj3gin5-QiEKjtfKubvb4Hvucv-_gFuFjeGXtGGuiD4vxYobHDouLvuqNQAA8PnlQKseAWqh-urp93puvFhxqurq5_DzqYlH3sD09TzE-Xq_oftT8BbA3TbaIg3K-N5nPpC7tpDc4nek4LNHUcgJ7rAcg2PdnhqwA91RV24PGab35PM60cjYL1QMFGTxw-lDo1zjZA44WkKSO-ecbxpcKrS3Ub1Zs8mcWR2d1Ee2cTuh8p8vYfYl7Ar5b_WbfrqbZfsANwBYWeSiYX1rSBCVRvVzLEECE1lqIKheyn4RvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامۀ خروج تجهیزات ارتش آمریکا از عراق
🔹
کاربران عراقی تصاویری از کاروان نظامی ارتش آمریکا ثبت کرده‌اند که در حال حرکت به سمت اردن مشاهده شده است.
🔹
این کاروان نظامی از کردستان عراق به راه افتاده است.
🔹
ارتش تروریستی آمریکا قرار است تا ۳۰ سپتامبر به حضور ۲۳ساله خود در عراق پایان بدهد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/farsna/462721" target="_blank">📅 02:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462720">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجار در اطراف اربیل و سلیمانیۀ عراق
🔹
شبکۀ المیادین از شنیده‌شدن صدای یک انفجار در منطقۀ «مصیف» در حومۀ شهر اربیل خبر داد.
🔹
همزمان برخی منابع عراقی هم از حملۀ پهپادی به استان سلیمانیۀ عراق خبر داده‌اند.
🔹
به گفتۀ منابع عراقی، پس از شنیده‌شدن صدای انفجار در اربیل، هواپیماهای نظامی آمریکایی برای گشت‌زنی به پرواز در آمده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/farsna/462720" target="_blank">📅 02:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462719">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWZ9SNWexUBJtnCfYFAoKK-l-So-FKs8go5Lz4eHjvAH8iCM9AzP2IITjbd8l8mRm0DANPGRZl_BJyD7XMXHJKgNuBMErPk4aM-x6StiSMFy3GGNdKlpVMzgxT4ll9vkS3FDvkHUA_Iy28Ij9hGUpTvtbucB3UCExYAjZW9HKPA_GuXHadwzy5T_si-ut1WCSJSv98eMkQ90zPFHq1jEjEmWxaPcC8H0secOhl5vll8rMqKBnjlO5WXJD06x9Bt4L0Ic9-3mtBkGcLubKulxOLqBHG9WHz1A-QT2yXzsnM1q1GDj-TIQaX32fbZY5HhaBzqTkCz-s6f7tQkWkbuxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متکی: دیپلماسی هم‌تراز میدان حرکت کند، دشمن شکست می‌خورد
🔹
در شرایط فعلی، جنگ‌های محدود، ادامۀ محاصره دریایی، آتش‌بس و مذاکره، چهار مؤلفه‌ای هستند که آمریکا در قبال ایران دنبال می‌کند.
🔹
در این شرایط، عرصۀ دیپلماسی نیازمند دقت و هوشیاری است و مذاکره یا عدم مذاکره باید متناسب با شرایط و منافع کشور تعیین شود.
🔹
اگر قدرت دیپلماسی ما پابه‌پای میدان و در تراز شرایط حرکت کند، می‌توانیم در برابر دشمن موفق شویم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/farsna/462719" target="_blank">📅 02:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فعال شدن پدافند هوایی در جدۀ عربستان؛ پروازهای فرودگاه جده تعلیق شدند
🔹
منابع غیررسمی از به صدا درآمدن آژیرهای هشدار در فرودگاه شهر جدۀ عربستان سعودی و تعلیق پروازها در این فرودگاه خبر دادند.
🔹
همزمان برخی منابع از فعال شدن سامانه‌های پدافند هوایی در این شهر خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/462718" target="_blank">📅 01:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25685c3991.mp4?token=T4UFVehvMcYGTBeMDex79msszQeHRM4bbVvamOHwgznVjnlqCJnXRmIN4HneCLVHI13KWp0RIOeMSKIrtyqusdOmL7H5uRqnsuN99Em_McyPjFGjLZ6ZVntxjKay3zdZaT1rN0oamgb9OJtq9-LW_xilZwDeuZRwv_H60rXEvvKNzvsofC1kTGR6Ry2VkyXv13zpVn1T_gbqsmI-B3GQ43f23E5U6RqqgOrGZIhfT3rQy-GsJ7pEsUUNtBot6MfjRbsLrY35AR7j2lJtpE1M1eZ9Xbx43W6K7zxf7PPzdOBT2cuTLR44Aor2J86khargchlI_G9EQo3WFTUI9YF_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25685c3991.mp4?token=T4UFVehvMcYGTBeMDex79msszQeHRM4bbVvamOHwgznVjnlqCJnXRmIN4HneCLVHI13KWp0RIOeMSKIrtyqusdOmL7H5uRqnsuN99Em_McyPjFGjLZ6ZVntxjKay3zdZaT1rN0oamgb9OJtq9-LW_xilZwDeuZRwv_H60rXEvvKNzvsofC1kTGR6Ry2VkyXv13zpVn1T_gbqsmI-B3GQ43f23E5U6RqqgOrGZIhfT3rQy-GsJ7pEsUUNtBot6MfjRbsLrY35AR7j2lJtpE1M1eZ9Xbx43W6K7zxf7PPzdOBT2cuTLR44Aor2J86khargchlI_G9EQo3WFTUI9YF_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از حضور شجاعانۀ حاج قاسم سلیمانی در منطقه‌ای که ۳۶۰درجه در محاصرۀ دشمن بود
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/462717" target="_blank">📅 01:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4ucy-7gqTmxsKU8NyQoUwXZD7fz0i4JEiJF_humDB6xQg0xNEbdtCqbCSEFFx1SRIHRB5p-Wgdol1P5d1L99kiKSOpj_bA3W5tgBaZNCJ4RSiBD6gG3UaP7Pg9lGdFStp9PqULzbhzbt-RHwnLKT1PL6x28PJoW0WhV9Uo83kj5w1ksPkLVdfcTq5yxdGJK9tOijtzhSUfZfBIoIYQil20_GIqkX5ij0EL3EiPad3zqG4_71auBb_qgWkQu5ZZkmVm1iDG0A4oOs0GDiaCDbRHqsLG_2nOPhuglqaFY7_xodjb91u3wEItFzcQJxMZomaP9l-jf_AIolIy8W1eMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب دو راکتور سنگین در پتروشیمی لاوان توسط قرارگاه سازندگی خاتم‌‌الانبیاء(ص)
🔹
عملیات نصب دو راکتور سنگین در پتروشیمی لاوان با موفقیت انجام شد.
🔹
پتروشیمی لاوان به عنوان یکی از واحدهای مهم زنجیرۀ تولید محصولات پتروشیمی و مواد اولیۀ مورد نیاز صنایع پایین‌دستی، از ظرفیت قابل توجهی در تأمین نیاز صنایع داخلی و توسعۀ تولید محصولات پلیمری برخوردار است.
🔹
توسعۀ این‌گونه واحدهای صنعتی، علاوه بر تقویت زنجیرۀ تامین مواد اولیه، می‌تواند در افزایش ظرفیت تولید داخلی و توسعۀ بازارهای صادراتی نیز مؤثر باشد.
🔹
اجرای عملیات نصب تجهیزات سنگین در این مقیاس، مستلزم برخورداری از دانش فنی، تجهیزات تخصصی، برنامه‌ریزی دقیق و توانمندی در مدیریت عملیات‌های پیچیده مهندسی است.
🔸
این عملیات بیانگر ظرفیت مجموعه‌های تخصصی قرارگاه سازندگی خاتم‌الانبیاء(ص) در اجرای پروژه‌های سنگین صنعتی و نفت‌وگاز، و استفاده از توان و دانش فنی بومی در پیشبرد طرح‌های زیرساختی کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/462716" target="_blank">📅 01:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462715">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4kYKTgHReCnd0WY8kkj_Za5R_f0xqo6ZrNvGEhpw1u7IXwXhyRHeyz-C3qaHwZo_BnaLHD8goLCorHUpsZ3Imdg4tSLjvxT3YlJiPuJ8c9L-yhk-eyzoDa1yTESJ8bft1-9hP_wIaEowOROfGFLZoKRq8XG6ZJb3vNZmWog4HIgJCCm91VkvWUz6YxCeKF7qIcTrIxZiJlf7jX0yEHR7zLqTOqZLiszbfEIQp5V2JTcuhnAKpMl8zPcLpmPnHb2nnkc26nbmBkTQTqFOdCwLkkcCxelRwwevSe2hqiVi-we2o5RclXWLhgVetGQRCn9en7X6GqSfYx8LWagUZcXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزمایش نمایشی اسرائیل و یونان در مدیترانه
🔹
رسانه‌های عبری از برگزاری یک رزمایش دریایی مشترک توسط اسرائیل و یونان خبر دادند، در حالی که این رزمایش تنها شامل چهار شناور بود.
🔹
با این‌حال رسانه‌های عبری با بزرگنمایی این مانور،‌ آن را «پیامی به اردوغان» خواندند. ترکیه در سال‌های اخیر تنش‌هایی با یونان داشته و در ماه‌های اخیر، مقامات ترکیه‌ و اسرائیل بارها علیه یکدیگر موضع گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/462715" target="_blank">📅 00:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
سپاه: نفتکش متخلف با پرچم کشور توگو مورد اصابت قرار گرفت و پس از آتش‌سوزی متوقف شد
🔹
نیروی دریایی سپاه: شب گذشته نفتکش متخلف ترند با پرچم کشور توگو، با تحریک و فریب ارتش کودک‌کش آمریکا قصد عبور غیرقانونی از تنگۀ هرمز را داشت که مورد اصابت قرار گرفت و پس از آتش‌سوزی متوقف شد.
🔸
نیروی دریایی سپاه بار دیگر اخطار می‌دهد که عبور غیرقانونی از تنگۀ هرمز جز نابودی شناور متخلف نتیجه‌ای نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/462714" target="_blank">📅 00:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462710">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gz3AcR341pvocVZJw4ZpwmIH9-eJaPAJ3UNEmLZMMDsUmA3F49pYHAuVegSG5GyoOAtHSf00vsO4XpmTSOKG3yc1qO7DuCGylLbowfuFARPjTiHjdfPzZ7W0wkkRPEZ36vQx796RMSj8Dxdnm4qMkhKPtW6Ww7U03SUMer1U1OFifVIOxxxEOoM_TYwLUCTL904Hdt4iyf7XMlcAtET_xJN9d4JDKxUJDZ_qYfpjEuvANMz87fcJuaKy1VChVPFlbClJBcoMuVuAOwR-BgnQ-YMSGURoVP9186QXm_PHz5f7M3cV8Ih8lE3PIuOTmpET5nAsr8UpccTOwL3SIrogwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Viw0_Nyv8nxG-3Sj0PJXcyYQBgN2JD_NHkvDoG2LEwsd7LC8PAXIgmDvJ2YbpIzvg2kwzNVl9MCxBH1Ezu0oXOkTbxUPuP08AV5CR4rIQvnhBhnZX6stVzaA362iFxAg6kRo4WjDhiJWp-oSK3I0CxqIbVr_t0uJJBP7Uonso6QH0mxTkf4g5JtGGbPZIP3YTVfc69YirfmYjraV_PfOrgdKMlj8vXK4tpSwlNMomESs3As7yKiPHyuRqnZUaaOJLE2nup8qoC_UHRT1AYO4LMSltKuoSpzpN0yXeMajxqP5nXoFRm3DLf3gQGx8BftdQhMMmk5aFgG1m0IIyT5X6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qm420GUA3jmpN9KLfxweBCkp2q_x1glOfM91dZPfzupgQ9-ewH3_2LdLNZB6nEC8QE1jORz0lBBUmFaZtY_sAUJKXtJZQ51LcsNN0LXcxKMkdVxZ7ovDvzhSqJl-OmCznIxc6q-LS5lZ4l20emEhUssgHg5q7tfGfM741OyzLB0xQ--aSK55bFAA35aFjb6_OOJ0o6m054d0uxF3_h5h5v04bmeMZXD6Fvfj2V2RcPcd1bwR8hfoUUtGBzt_nsGSv3lcqb8x_EMGxh_siTb2BzDJ3LPwmfigMAy2O7Pq8YOUabNlMqUEJXJOoH-jxAWh-LCcVsJjD4ATz11Fe8FGuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMbCa_LCzOtMPoaboOo0vaieHl-rkg2gBIvNjRLZA4-sSoW-Q6d8GsBNmMcWW3om6bsSS3ocTvaQFXGMKlo8xlqOSoIbv4JxHgSvQmxxRmrgpA7W6QLrYBaV0r0NEChTBLOQI-tDWJVKdtAwXCH8sQTt_zp1D0fG6L3GlGo-9plQ-2kgYaXg68PVgQo1Q9PhCCyWLUc0vthLsTPaKrYdENXsiuYSm5x6ZioVemQO8936V1VvvPfmtdfRuTdjKmYIC-vKWg8Ysq37jjr6E_BkuiawZ2jo6c7nJJnGGnNPmykksU5BgqQFb286UAs0Rt23kIkq8ZkRoh7Q_2ThqSd_nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور حجت‌الاسلام محمدی گلپایگانی داماد رهبر شهید انقلاب، و پدر زهرای شهید ۱۴ ماهه در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/462710" target="_blank">📅 00:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462709">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی حومۀ شهرک‌های بنی‌حیان و طلوسه در جنوب لبنان را هدف حملۀ هوایی قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/462709" target="_blank">📅 00:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462708">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foGnK4TaklpiOvfu9L--xP5tPdPFvxU21AllVDsqLgZfnrqE1QTBHuN6MN68Towe1_4k4Bgum0TvmV97FQ2db-t3oQY4mL4tCQzMeIDMTJcXf5_fxzt25pC9pZ9zGp9Az2kclxU9I9ODgmGFRWs7NE_490u9_soppsm3K06oHoEafRJcpf6FYy5bQ4RTcRVjHQv8FprBUOPzfDrvACYbkQEZzazKfbXOST4pWKeIRzUTtCYPw8ZbPyvmSdigMTqFIEXnO_dSFWTLONrR03gxj8GafVQhAOfgOGh9FqBtJmJ8Q7KIaz0TG4HWu1Tjrxp41FhTZ9kdcCoivcjXwAGlEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما خیلی مراقب کشورهای حاشیهٔ خلیج فارس بوده‌ایم
🔹
ترامپ در مصاحبه با اکسیوس گفت که می‌خواهد از نشست سازمان ملل برای شنیدن مستقیم نظر متحدان منطقه‌ای استفاده کند.
🔹
او گفت: می‌خواهم بدانم کشورهای حاشیه خلیج فارس در چه وضعیتی هستند و اوضاع‌شان چگونه است. ما بسیار مراقب آن‌ها بوده‌ایم.
🔸
کشورهای شرکت‌کننده شامل عربستان سعودی، امارات، قطر، بحرین، کویت و عمان می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/462708" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462707">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ادامۀ تجاوز رژیم صهیونیستی به جنوب لبنان
🔹
ارتش اشغالگر رژیم صهیونیستی حومۀ شهرک‌های بنی‌حیان و طلوسه در جنوب لبنان را هدف حملۀ هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/462707" target="_blank">📅 00:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462700">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxYJsGZw4GBAAVLoLrW42KB0RbiWviZ06Ia2wjb4ImWc_4DXNnJJafdZX-duGiYCx6d7YRpbuiH1oco2FA9kXDyGTFuQw9MecomRac8FpQQW0Umq-2NQ86gs3bvYYuh5D0cte4OlnUr2parvOhxmByLWDeu5Rr-FqHFphcFFDKgz0Uhs1nMpbQ4hL1ExH6S5f4vjp3rLPghY5-jjD45hUFYKn9aCnGXJ8t804DIQSUnNk58BuR3Y7r_p17DR40hgHCT61L31ruU6C5He8EEcet42OJ44fDo3bWg9bKcPGKi0fa9Uto5jjuuw5W7ocUMlBL6R8Pq3ySxXcX3QxI5Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxTM6QuSZp4JIbiEPP7dxTMrUCp_2_NZv312lmZK3i4u_aXj0-6fvREqvegvhUnA9dZW2gE3vWDUiDF-OHYft1tfZsgxVLy_MBc9FGFEdDEL1EhgLjQsTH53K6ryKs9D_0eMag3GyzjS4Cw-V6aeXc_DJF6Aw-6rRy5Hub1G5TCWGRiHLNL9KeAmhVHgvIgt1d2lpDtSV2dSTjHgK-EVWl4f_pXqtxxGgEDwzgpOUEhqm7Ax65LoY8kaHEGWQtp0SxDAEjL5s9toXRLUnS7JR29vmUmX8ufvE35dMxUYjnOorxm5ch0iR5OmFxkMg20hBn8gi6-Rja46l7FUPwwc7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/elCCIChbcfAprzOUfmwzL-I-E16C1MzPHHvLyOVDpsjCj-YQwuQWOmYGiYEdHWVHPnagipmEm_xsHr2ghp3W9rebI5ZLLHV7Ta_48z8EmS_QfnkmdCqgMbp5l5xF1pmIggdEYAttYAn25mG2MswZO-TXAI9dhDZjDv1oDsusFZJXGKcq5e9zTD808Ifjunm1YuJ6yuYJjlawLjmDAKKD1OUs6M1aicibasG_0n28Pm8wH1B0E9_xMu6oNsC4h7v1bFUM7tNHv2WxKCmYXxyIVBqGZJEjeK1yBYZNu9dspVOF0IspASDguxwKR1vUHHMKwWd4PUc2yxxEn0_I-GFhrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JVH20lGP-IcjMiIQjUtxTs4fWe2zJ5SZ2VnHCVQASyllfYx8BfAvX4vL0zx3RENobpOF-sOJXv389OwSSFddO0NB4nEOU_D2lIzPfjv-LuH46voTwvxOpjgdKFR1FG2jCi7dx9CL_B3e_6cbdnYUnxyWOwTSol26OHBFOA3BJK28SYj5cCOCU7FQZXZeizRR6JzXHrg4vHrmxPouOvRKmXa89Hc3i8PaOuDtHEQFsgeomOpYziOA3RjbeTb9Ihw8t27p5eWJeaQYFiPzfAzh6Dy8KsE5jP224PJRaCohwmQ_yCVumUVCxPo5_2rek9jUQOSHTpDFKW757WOk2T6uGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiZN1Yp0U6HSlh18ZK_B81Dc3edogeJ3SIC6_Mu96N9Tu_fUek4jP8zlgw7G3XC2YYQPCG_u03wf0WYQSbFYA2IUlpaQQa8sKP_Yv5xOk_sM4DDZakL5Axk81CpNxRk6DudbAbhTXhyhQe_8-397rtV_EI1RN3uPzsk03BBZssw2CKfIamIUjYxYVUO1wqE2M9AvafFFqx_VpO1XfyQ8qSBkK1wjnL5tV6juFMoCa3GYEe6y_05BkDiwPleuZ48xQ6BofbQSw69CLnD0Um7WQSVq9W_nBFwUwkKj5WOcTYdPOUKGiuU-ZDbVZawBoIkUghucJlKyV34xowfBSfDUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmRCtE9SbWKK1iNpeXsEZLalCqr0prWU4dAjbJul3zEPTTZkFpkWn4I6IrsX3udUwNEGxxL_WI_66gJPTZZw2LvvuwsRbkRwrQzJCLbt4S5vWH1sg4ZZjZ1cdX_QKQYdB3Ddw7_sIfWqyjf1WEAiyRw8J9yOLkN4TksgmfsvhQzjXKZMEru3sZSVAx4Ri0tFxuljI2-Htunr5YP0qbeKYGJxMbrj87lf7PzsppV0BiFtg9ZVu0_3D7gPqug82Jlijn16kMNmbxyo4E5x-Smune3OHEXR15VEIzoacdSyXN9WkYEshiUKo_mIQ_FiJk-Zl4yIoJdGsmOrzJ70t8vIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwforE1gBvNl9E2zVHZhf7ove5yWBlVLWN14kSQ4S3gNFP9mLrVQEzCLCcnsLRlVsWnnZYyJ5lKpJ8cV6PP6bc5f6JwWLNcLXGhb0CmxOPokM26o611qI51bZ-J8Zgw39CrAQN5BWakVpT8Hq-ZyTj9bYn-eWz4s1t8BIwZW3yUpZdNg3OJULDeTyFTVHta12nsb7IOHCUB1x_t8JQRB5NznmREckLFt0ryWk1_U4YytSTMq7Rr6a8fgkzRujENjVt7IGIdHAlWxs5JBGDtCCxIPTSC4jG0ddQS_Avf6FCVx3ALpei4x4l5itCSSEydT-M1ys1paQj01_nD1IO892A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خشکناب به یاد شهریار
🔹
روستای خشکناب، زادگاه و خانه اجدادی استاد شهریار، امروز میزبان رویداد فرهنگی و ادبی «یک روز با حیدربابا» بود.
عکس:
عطا داداشی
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/462700" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462699">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqFpY8ZyADvQQ8eN-h3yOEoISX4pKhz5YqP29vwZTprThd6s3DVB-_eTRcXS1O6kVQSVFsAUJpDrIfAmhKvVWxnJH8n9OBXMiq4BviGlQYTf1xPh9_rArd47gPbYN2DJ6RiAE8mr1I-FFes2Dt9nlOj5pjwshS781b2rZkU_juvwq_r-m4szj_BqtqyeJkK88cAq41DZIpCrsO_4TwDesT-6YXCX6cAYdi-jqDS-QFAA5g_og9fdeRkt9mMd03PnfCYvQVCnZbY2dPd4W3bUgsAE_ZjJlEb65Kbo9jxm7WX2O1UbUKHziKYN4iZCzD8BO2LG9G6wNcMY9Hwr-74eFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر صفوی: هیچ جنگ تحمیلی نوین صهیونیستی یا آمریکایی، نمی‌تواند بر سپری که از بصیرت مردمی و اقتدارِ ولایی ساخته شده، برتری یابد
🔹
اتحاد مقتدرانه ۲۰۰شب حضور، میان اراده‌ٔ ملت در میادین و فرمان راهبردی رهبری، نه تنها یک پدیده بی‌نظیر تاریخی در سپهر بین‌الملل، بلکه یک واقعیت تغییردهنده در معادلات قدرت جهانی است؛ هیچ جنگ تحمیلی نوین صهیونیستی یا آمریکایی، نمی‌تواند بر سپری که از بصیرت مردمی و اقتدارِ ولایی ساخته شده، برتری یابد.
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/462699" target="_blank">📅 23:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462692">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhtxGzIdymEZLcds48OojfbrCFr39994WdVGG1WpO221kZQESwAbwgeo8NQpCHuygbwXaKL9t2FDq7KT_3ULXayvaA0XC9D5HotOxkg1BlNra-sBjgDFq2ZKoQq2ApSIdHRII4vg6j4TlTm7v96LkEi90NxY0PKY-ypyNUqFeFcwkY9VbyfoqNZPXPkoT7UyDgn7BWpa7ES9ASolyDOlT5VNbjsesEVvNzStN79lMsjKc0gvR3n45mVIpS5u_-IWBvUoU3mqKXDSBxLFMWTn-k5tN3MKVKoHyxnAs5UlJcBIedpBZChQ6r8ULCfFVkdkg5DtG8GZ7ZFycPat9-WdSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFxcHQqdfIlnDG4XPOPCTOnl_q6RDcWcMynefVUlaU8jJUOWlY9a6f6zTysaU7CDj1s5B1VBZ0iMckrKGKeJSqD0yOJijpJUzvmwSoWI0518Wsnc93An3k72PrFMJc_UmCDTQaGEC2O723zVQVysUnlQax8BMjX0uggbnNrvwMOKAYv5u8YGpW_1VBeEM5r0ncMSsaUYdg8Me635CYiURH9zxBHfTdRLPhg5tH1UlO7IB4ue2Yeky26OXbcYxHO5Gt9u7OFE9cesD33-GEeLc4qWuoUk-0VT4NspUulyFSDMvUXQHarEnCDYeZDp87bzV-2PQw0rC3omI578FLH59w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0Yy2yMSbJcaWB1_BhTcxctWRv7qE314Ear_LtYoJobD_cgyEScu4T5YSgL9XWiYHbWnEPn2QT4fCIydmzYqSVM72wb8JNY5-X8gtHzXPxBFC_Y-BaahtoK3JCu0iUC3wvE4kq8LtjqDXiPO7eL3S0JOShf5GpySinObO-X6iDja7rrbDqDb-BHZwMCOXkAJw6bh2kJ8oMz6_eS8qUu5PHNqPytTKMEOly1zxuoLTP9abR5Poy1neM1GUOIGhL-FOjiQb5kks9ZKVRwGLj6JsSR5XeWMJChqZ8F2HgeFEzObcZQi2rgETa-M4yYMGwaeEfImPBtLLM2eUNSsR7b2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ku1gWjlcKVaYhJFg0LqBID9kLaH-QuzaUX5QKzFX7UTgcEKwJILIOPqpts2lJoVoOMexhW26LUsFnAqGlD_9xHVwAHkc0rp3wSUVfsCpbKok0qZIPiYnd9KentVYrW1_pmtOkQ4RnuOlhqdmOvvjIRO3Nu_VXiAmlFQcaXGw0nELlfBEioyp4bcUYJ0kR9dJgNi_IdKrQtRlKz_jq-iJ-reYm2eoZOo1NoOXn4KzPqXgm39bazaQdkmAcKsh_oo1smUK1Hgk9V9Krvoalbisu8En0W0juS9jPgKXvEfwiE-pM3Y99ZAJTKAwf7p000wYzQjFaE6wVGo6SUNJ-D_WNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3rVSLwMLKRVIOBxwhSMLDBB8AgKwZ0vS9Aa308LQPqrOxCDpc8vDganSEGOqRBGTXXzQbpQ_VPozt8MORM-ZHdKab8RRD7tlV1B2f7UQX4SkvLiZe4fGFsN3rTNiH_OcKBNRqXF6u7M9JIBwCjt7Sh_VRIO_kGx6qskvhfSMX-IaGAOlLEVbCYO-MEWdZPNGdXaG0ABdcwrUcDvARlJWb7rrn-u-DO92UW8S8GrGsG_6YxfmbrCU3khnyeGHu3XPlIAqqCkxH0Q5ttNb6oIxkVWIWyew9tC8qA18nLikTqy_M0ZpRu59eA8b08WmZVG58TIlEgDzCK1YejHYyDa0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2Q9dObhrBNUWYQiAlA8Q7P_9FdthmxzobYX2z-QnWg4XznJJSvzGAGJPagqYFe3B4BoBfLVXa9kFJMDcn_fmaAllw5KHcG__yjSi36yma-a7rYPccsn-HKurrwcLe9CyTywkM2Co8I5kzV4o9AoA3LG2lNhVLP39b63eyMi-RZdiWwKAxjdFoJsi6U514rY3lGYT_oJY1lo00pEpsSmg8tFyn8YC2w_sVm8H3o0UjVQPPJCvTR-xaFXV0NO1MTIR1bmunV6cl0O5lE1ILHTK_Jt2IP_FC_gi61kB_m-l5cdPVdb3POhHSQXUSQVFIrbBUE-bzb9zcpsoz-39p4_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tLCN5O7j0TVNzvVB7dFAQSslZGr2ym-cajEZFN_EAD9tRQSTO2vs-6_JUJNfGNya8ki_r_ZuR2hZYJq7TuzUqP846m6Jui-Ob_z2ZPegAt_D5teHN2kePoOp7Hmw_Cpv97G8Gy9trtAzQMRaFUaMulhhRtTkLSyqKtWegP3knEYN9Pem9zCm2oHWgdlJ6SXbPA0LOWIFOhvsJljAcbDT8Y58yUtsbFExnagHgn-ug5Ty95gMf_FCExCKH9mFWf3EJQ-B1wp3qsJmo4mbUJ1zSSYbIMY6PcSJ6e-hccsiZYWXIxkvAfxaNVZm6-4HS2RHKSnnTlebpnWVDZUlvZ3XTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روز بختیاری‌های کوهرنگ در دومین کنگرهٔ ملی شهدای چهارمحال‌وبختیاری
عکس‌:
رضا کمالی دهکردی
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/462692" target="_blank">📅 23:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462691">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-QBFjVglaMmYMlK9TOjZKroNguw52ZlOvOfL0MkJ7Q0G24aN4w2JWk0PE4D-vkM4fI95UDl224fWqYCBH-Euepa2cAq5P6EbHzrpMEd7VR8195GaSxy-k0LtWa7NLENqCLNY6IDzwW1W2Bjaf3wdRfO0dcFTpOztzmBCEq2-2gzmdcHzPTiNc7p70eSX3XkrXRg0EQNUEniW6T4CVJqHGGH3BdL7q4xEG5fg5IFZTqoLsm9NX9PsSwaLbRqfTDglRXMs4F8fQQWNrkqt5Nl4HeaJ8gv50BoF9BNDgO7kOlmvTTwXke2cb44geUQm4DgpVGIRbNBEjoH-eGu4V9dBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه امنیتی در تنگه هرمز
🔹
سازمان عملیات تجارت دریایی انگلیس (UKMTO) روز پنجشنبه از وقوع یک حادثه امنیتی در نزدیکی سواحل عمان خبر داد.
🔸
طبق این بیانیه، گزارشی از یک حادثه امنیتی در تنگه هرمز در ۱۶ مایل دریایی شمال شرق خصب، عمان دریافت شده است.
🔹
طبق گزارش‌های اولیه، خدمه در سلامت هستند و در زمان این گزارش، هیچ تأثیر زیست‌محیطی تأیید نشده است.
🔸
بررسی‌ها درباره جزئیات این حادثه همچنان ادامه دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/462691" target="_blank">📅 23:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462690">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94517e21c1.mp4?token=Z8m0dU0vrglBIZP9pWUQFo77X0JngzgnXtDWVlKQ3oxOOpkRIJ6SVHidaC9BsCScJzazEl-an0UbPeiYrlbKF_em6MkBY-zMleLITzyLZHXUiKtoUyyDDMhs647Exjdx7yqzmgYT1HaWJoB_t6Kw7wjdhxMWx0NqCua7er6QAFEhA3qBIwVftrauVVcIJbLfVF7wq1HChQfO0HVdbzNyfZMaruJIru-H5trNGSQRypI7bXro4RpQJsGHKi7L7j4qByc0PgdxW03FqWCgkF6bVPUJTVvvqTqTbUE6gcsU5Qt96Lrc2ch5w2iMMv8C98ZSTTC_Q_9VpVuUwucM9s8lRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94517e21c1.mp4?token=Z8m0dU0vrglBIZP9pWUQFo77X0JngzgnXtDWVlKQ3oxOOpkRIJ6SVHidaC9BsCScJzazEl-an0UbPeiYrlbKF_em6MkBY-zMleLITzyLZHXUiKtoUyyDDMhs647Exjdx7yqzmgYT1HaWJoB_t6Kw7wjdhxMWx0NqCua7er6QAFEhA3qBIwVftrauVVcIJbLfVF7wq1HChQfO0HVdbzNyfZMaruJIru-H5trNGSQRypI7bXro4RpQJsGHKi7L7j4qByc0PgdxW03FqWCgkF6bVPUJTVvvqTqTbUE6gcsU5Qt96Lrc2ch5w2iMMv8C98ZSTTC_Q_9VpVuUwucM9s8lRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تب و تاب «میدان‌یار» در تجمعات شبانهٔ مردم گرمسار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/farsna/462690" target="_blank">📅 23:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462689">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkM46UStfv0tZLlZHqA4w-Z5QONage21HPvbZtn1keso0ZVf2b5oqlr6JuzSBW1lDR7xSBQ7zYnfriQptyJzUiQ8-dO5pJsSompdk_GuYU0tLUxjYAQboRm3dEqbjL_uvUxceMQXnv5LiBK4MbXeJde21wn7r6MKKbOfzB1yGsM3ycNmyjD13ZlWRfdnoMCbn3BbnmP6_4kybCJCgNmPhB00HgVmCwaab-zte4-uxc4THJ7V6w0aE2r_VJ3DKn-AHptDimc8SuMWIzWLfNpz37aqwSp0vGRhL9fxKgg6fMDQQYc0TyDQVB4mRg-To0lCkQvtzClpnD4CQFaQ9YhuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از لبخند ماندگار شهید مرتضی لاریجانی
🔹
جمعی از اهالی رسانه امروز با حضور در منزل شهید لاریجانی با خانوادهٔ این شهید دیدار کردند.
🔸
همسر شهید مرتضی لاریجانی در این دیدار با اشاره به خصوصیات این شهید بزرگوار گفت که نمی‌دانم آقا مرتضی هنگام شهادت چه چیزی دیده بود که اینطور لبخند به لب داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/462689" target="_blank">📅 23:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462688">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e3b781074.mp4?token=rTBFTT-59NIt6dS21yVP9rRVOrXlBwt4NoRrHAFChkrO1qVAUo1_wlw8ZOfO6z9QzmIk5J0x1ugoUxfqMA2CI9CpNl8G9RjnPfxPbzmY9CXEIp9gTdexj9xMNm05KD9U0cxfNZoeUV58jAsXWUE1HRVmEwNyptwVjAWF599UQQlxocmKjd8sZ9U3FH8QSXvGqJJ0YHGQx7gISpPPyrLY8-MTYx0EfrWcT1X8-Uoko583TZV4hbznUBUSL4jE6uzpwhDtg85NcB8dyFnlClYAYjOCoOTpUXDXvDURi22LGz_N4PGLQixSvDNloTp-ufGeMnuYNxNzKL5nzkDIkx04TK99EyxHi2SZyfiph82w-4TMiwxAi3pw6GBcy15aCf7ycSGb1_BBLZgSq-ruydbOLcXobtQuUDlrCYh_XjFWKhJSD9KgXQ7lwiTdbihqABrLA3TrZX0xifVIJk2I6Nk8sBEkhPB4XwpXSp3JQmQYbe6WN4rNWxioW3ZtaJlELHMcIQIcJN-QtCfSZr2oKLsmJBCaX8qB7wK3sP7hWdEbGlXRpmp13twOaJlE0xF6GSCEX5D_46NCL0Ks0bjuxzRr0cZ41cMztdE3HjnmetA7-BSzoqmeLd4uUVP_e5Hhz9uVUd2a9JYnLp9NOX59c3lNaN9FFF5K3SWsQwdDCpMwBCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e3b781074.mp4?token=rTBFTT-59NIt6dS21yVP9rRVOrXlBwt4NoRrHAFChkrO1qVAUo1_wlw8ZOfO6z9QzmIk5J0x1ugoUxfqMA2CI9CpNl8G9RjnPfxPbzmY9CXEIp9gTdexj9xMNm05KD9U0cxfNZoeUV58jAsXWUE1HRVmEwNyptwVjAWF599UQQlxocmKjd8sZ9U3FH8QSXvGqJJ0YHGQx7gISpPPyrLY8-MTYx0EfrWcT1X8-Uoko583TZV4hbznUBUSL4jE6uzpwhDtg85NcB8dyFnlClYAYjOCoOTpUXDXvDURi22LGz_N4PGLQixSvDNloTp-ufGeMnuYNxNzKL5nzkDIkx04TK99EyxHi2SZyfiph82w-4TMiwxAi3pw6GBcy15aCf7ycSGb1_BBLZgSq-ruydbOLcXobtQuUDlrCYh_XjFWKhJSD9KgXQ7lwiTdbihqABrLA3TrZX0xifVIJk2I6Nk8sBEkhPB4XwpXSp3JQmQYbe6WN4rNWxioW3ZtaJlELHMcIQIcJN-QtCfSZr2oKLsmJBCaX8qB7wK3sP7hWdEbGlXRpmp13twOaJlE0xF6GSCEX5D_46NCL0Ks0bjuxzRr0cZ41cMztdE3HjnmetA7-BSzoqmeLd4uUVP_e5Hhz9uVUd2a9JYnLp9NOX59c3lNaN9FFF5K3SWsQwdDCpMwBCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج حضور کاشمری‌ها در ۲۰۱ شب حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/462688" target="_blank">📅 23:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462687">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3NtaLgs4PASe0wZjye7Grjcvxjy4IsaZFuwAuoeHgLVEHr96t9c4l-Ta3PmtO1RLaJU0mWQ0EgM2JiIn9F84ngCqGYZxhEaDkuPB5Hcl7SxqhJ2bFh6fUJEYhkiT2C7u3a9px0OmPKHqSKm8SHJUHIX8XcrkTNgkrHkP-TQstaaiaa5E19HstgBGmYZ6Es5JxUpOAQHSidycyJfVi7Nawij6NiVQodlZLpTsZ73W3lKS5I-LA0G91wTi28qdKyvEJJ_ZhjV4TsJlkHW4AKnUlzA4w0f7JJRQSlMxMlHwTQ5roYuuMO3eQYIeR36eUixoX0HNeO3rg9kgJDPx3eBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: وتوی پیشنویس قطعنامهٔ غیرقانونی آمریکا توسط چین و روسیه، مانع سوء استفاده سیاسی از شورای امنیت شد
🔹
نظم تک‌قطبی که در آن یک طرف با زور و اجبار امتیازگیری می‌کرد، به پایان رسیده است.
🔹
وتوی چین و روسیه سوءاستفاده سیاسی از شورای امنیت را رد کرد و حاکمیت قانون را مجدداً تثبیت نمود.
🔹
ما باید از چندجانبه‌گرایی دفاع کنیم؛ زیرا یک‌جانبه‌گرایی در خدمت منافع هیچ‌کس نیست.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462687" target="_blank">📅 22:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462686">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
خبرهایی دربارهٔ حملات موشکی یمن به عربستان سعودی
🔹
منابع خبری گزارش دادند در این حملات، «خمیس مشیط» و «ابها» هدف قرار گرفتند.
🔹
سازمان دفاع مدنی سعودی ضمن تأیید این حملات، از فعال شدن آژیرهای خطر در ابها و خمیش مشیط خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462686" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462684">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t3QV8o5B3k-hu4Y3Rz5yZDv6jtZhvoykXAUCfvIHPa9dq3p56J_96GOU7CjWhG5HBEoT3dK4gPjM1h-VAO5juJYafNuyN_MEH5bzmw4QE69VeYsRretMGqC5XVa2GV9_OJFp3nG2OMLYS8YyCRfEEa0ypLK4J3WfdPmKyl-j0E1JdncyGxbJolQMHsWRppxYZnRRRCfFtRN-pqFrcH5Y0SKl-MdXp6GVhRu-DtcYmUBjvV5w_2hIK4HWGc08OWvsFdLzY2h0aaCUIOHL_0DXacC_zW6Aw6sXgK4WTs8P78scAx3BRzidQcigtw2zUjOSmnZXgePB97EVAKYiYjmkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrDleV5PqwprKcbkg4pKer-B-vGXFkabaRJY2fyl_brGUURwGY8zbGmanuxbLqpBwrucjxiCZ0omLCyfuIO2slDKnArlbH4PIlK4Ij_fW5wX27jBuxiYVvahXXQIAY1ib1BXbVNT-4rg9fJaIrn9uAbY8bHcGRJTrgKLIKft5k1cQU40CMOW5Ldqz4Y3wkW_GqUcgILkhMoaGRtEgxMU8HTB2MzGz3kwyGhfb_QHaohs_WAwGMntvT5FmD1F0xm085H8ql5sKw8b1jjkqBzpA6MvzkJE9aXYZuDcq-litrG0ZoriP7HJtPwkBP2EQa0UTZOxPTddeHoB0gU_3nu1Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در جریان عیادت ۲ سال پیش فرزندان رهبر شهید انقلاب از جانبازان پیجری حزب‌الله لبنان
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462684" target="_blank">📅 22:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462681">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SqjKLIGfMkV5QJWniZrIktA6BBkMpT7iR9gIQ-30c8iaf6bmgz7uLqLP03R_ndqNuoe3hqBuJ1w1jp6f_N203FTheTuGyM0UdiA1uXKcQmqKCjJx-kKYmUgQQYqdjrCpPE6OXGNM8Jp1EoFcoDY2w-e9QYljDigRpipNccgHu6Js7bB2pC1TMzh0NxMavxRDqpPqzVIZOlOlis3_z0zKnTJk7HjM8sC-noe7-qsW2vs55T8v51n52T6y-5ac2aSySZjH8Z2sHW6ZrsP4Wg1NWXkwve-4PZy_NvsvaZ3KqyoxL12JUsY2BJ6j-pNMrKAFbixoDEc3_gSZO_y6wTWf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPndTy7XTYAU4BQDKSJ8Yk3G0mOEv8l-4_dDIb7ap_jhrY4zkfzkrTVfWB7tMdpi32XX4XPmAfq-I2aduSHXREBygphF54qw7tJRZeYPWsboCAwTwPJ909cfrH87rdHnlRaBQGvWFLI2YxqNvAux-UomgEaa6IKMUaqpj8Tn6IpBmCR4fzjhpkrwydBXhTzjyh_FbmJ6vsHvWGyCJMQl2m8kaxLHIcHW8AleyLFRUku0ZtF3XvnB4mMtxo2fk7sF6QCcWb69-98qwFDght9ZRKf04JKhHHxMejjGdAJSSoUQQG--1Zu1N74eM4MbxbCQNqDMkndtyVT7hfMlpEXuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXFE_w-Hp8UJeiutBxr6U2e99o_VS0f2GfkzQnlRZlJKgZxEh0oLqpmXEuz2SVIY3WKVrOAQal0WcdRbd0TP2-iHTPyXjWMB9gZV2RyWUWFsj9apo6JFXsKHGbq9A6XCq1OTCKOrtlqNl-A40CiBboPcis-4zcKYFgm-9DhAl2Y5WpLq_wSQbTO1NTSym8oDnp4oisP3Oee3dQ60d10ojKqijpuSZlxKAsGJzjFogDV3dx2jj7GsUAUkJScvDPA5XkhE82zXla7yCORF6xRNe8P5DTsTM4Vhmn0LjG-txxiZratGViuIW6ceyC2r4_QioOIE1S0tSdY2vhLXtK2WXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌ها از سقوط اف۱۶ در آمریکا
🔹
رسانه‌های غیررسمی از سقوط جنگنده اف۱۶ آمریکایی در شمال ایالت میشیگان خبر می‌دهند.
🔸
تصاویر منتسب به این حادثه در فضای مجازی منتشر شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462681" target="_blank">📅 22:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462680">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک) اعلام کرد ۳ فرد و ۲ نهاد ایرانی، از جمله پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک بابک زنجانی را به فهرست تحریم‌های خود افزوده است.
🔸
وزارت خزانه‌داری همچنین افراد و نهادهایی از کوبا را نیز تحریم نمود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462680" target="_blank">📅 22:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462679">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyO9Dfr6zIkdt0qF0eFRFD4UX0hx1mx7DHVTCq1ExEPl2AeK23ZHP8htrsgc4K8vCkdR7yLuEBEVWZlPBTTNydbnSuyoh9-Pvlz8oaA1OD7r5JcwRFAGgirl6wf1xHoSkTUH9AxAl8KUWt80tAKjbbWB_sIbkAGeduDzY24j3Tog8eqQtsiqN3EgLKeQAJssruAy9RqryUe-6VsSA2JjzkvLOqsft14VQxGbxyCHp6HBj4klccdzka6te8kmJe5-BPh9IKBPm2s5KJd1k5_KlO21MAj6DNy-98cGpIcGQBsTn54-QI_tjZkaufAJrjSUgF0Fp-08GJMOup-E8QWgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنگنده‌های سعودی در ۲۴ ساعت گذشته، ۳۷ حملهٔ هوایی به استان‌های تعز و حجه انجام دادند که به کشته و زخمی‌شدن غیرنظامیان منجر شد
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462679" target="_blank">📅 22:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462678">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee92e48af.mp4?token=FZGgN81CNdLo_eFY2qSvlNCYJ5Ci7hY4JTUw1GPSYlZLc3ou-aIy2dLVlHh9FrsKMG0Tsc2kSfj26EtVo7qymxXDLXNUZ-oynq2oAiGv-wDzlSg44et_y11gvgNmlXzpPzmW1XSgM_OvvP_BpzI4Gp_E34XrHjZQS7HraJdVdrwWPw3RzO6GAvgkS3EHjuMtw334Dz31gY41enQLDnBVGRK3PlXIwVEyKRUPF6ehFbwjHyd7xtKptQU-HZAX-djvQDYneWLKxh0FqbIopXryMXs-0RrU27rn4GTGh77MwUkxRT5fetl6Pxj84AkBgSmgN3yRaTO_kRXvVLNzEDq1lEBNCWuVRNVLFRcBCx_TNypNMUlmqR_kpMSXTq6Odl4nFmEjPPehhjDJqeaQghDYhOS-bGq_xfRT4-GX2qASXFIgazv_q6URyNK-gy2RWrsF54p4FLnod5164B_YEByOvUCj-kIEp3pUD1tfywpFtVbuWs1-OfRBfGlvT437_wfe1n21l5_j46pUYhkxIDxxU8SrYj2jarx99DbMplb69_vcdpwaCuaVW-NTXzn63zWECExsp0LNNYTZd4j7NS_Rtwrn2LC3fT7CWB1Cqxd55XoRuhOz7-dKn4NXwdAtdLh4S9gRazkyKIcOmIdFoGyafAEq5JqmiklGbFGD5ykdi_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee92e48af.mp4?token=FZGgN81CNdLo_eFY2qSvlNCYJ5Ci7hY4JTUw1GPSYlZLc3ou-aIy2dLVlHh9FrsKMG0Tsc2kSfj26EtVo7qymxXDLXNUZ-oynq2oAiGv-wDzlSg44et_y11gvgNmlXzpPzmW1XSgM_OvvP_BpzI4Gp_E34XrHjZQS7HraJdVdrwWPw3RzO6GAvgkS3EHjuMtw334Dz31gY41enQLDnBVGRK3PlXIwVEyKRUPF6ehFbwjHyd7xtKptQU-HZAX-djvQDYneWLKxh0FqbIopXryMXs-0RrU27rn4GTGh77MwUkxRT5fetl6Pxj84AkBgSmgN3yRaTO_kRXvVLNzEDq1lEBNCWuVRNVLFRcBCx_TNypNMUlmqR_kpMSXTq6Odl4nFmEjPPehhjDJqeaQghDYhOS-bGq_xfRT4-GX2qASXFIgazv_q6URyNK-gy2RWrsF54p4FLnod5164B_YEByOvUCj-kIEp3pUD1tfywpFtVbuWs1-OfRBfGlvT437_wfe1n21l5_j46pUYhkxIDxxU8SrYj2jarx99DbMplb69_vcdpwaCuaVW-NTXzn63zWECExsp0LNNYTZd4j7NS_Rtwrn2LC3fT7CWB1Cqxd55XoRuhOz7-dKn4NXwdAtdLh4S9gRazkyKIcOmIdFoGyafAEq5JqmiklGbFGD5ykdi_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۱ شب میدان داری مردم مراغه برای وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/462678" target="_blank">📅 22:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462677">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af9bb34f.mp4?token=bzbOSkBVPogX9FeutpzdxMjj_KGy6StqQXbgxcHeAaJm8t23pyDHN3SE-lvJFkQ2t4NteosAwFtYLsIJhAzC7yQoOOhUHDZzNEhGfppZglaM81e7fWHEUgKTp6zfikF4vb2CsjPS9WVjdhjikR4Rk2yH-kqpvKmlNuT907k-9eG3MoHzsdGoyQivak4lpfbDqOjEIvnYdomIffcoH2NyNBP1Vkem9RdoGWIW0Z5OUEar2m5T6xRnFneNiDiOVRj6e6V5qdfXsqIQICjwjrS7EbmlhDbkz0dcx7ZOlBlTaJIvY2Hbuyc1NGGARkHO_cV4yylA59jxVsmd9hby_f4WpJI1g8Yf5lL-ZnPePRk0LbweBTZeGP63upwLtk3Y-Jpdbm_9NQO2jwrBU9oFcKyEsX0p5g3sRQL5OH9WsbBAEAWx2ATpWIrLYXS6pCju0zRv_ZGO71CgZxlCtD9dklUIss7V3dhGxyqeezeHgluEkdRAKc2i2v2Og_zdyw1kfvZsyrDabTjWQDLmXiTGxK4ZTXPToz1IVxduR2gL6cMeoK0t3xcmxrR7K9pM7XC_BoVXYZ1OJp4QR6hzlCqb931pRQGyHhIErzDXdN-KJ2jC3gLpDL2sSwjjePEKPVPCJznUYrgkYVNcCs0EYYaRxWHmktraKLfiPo1LfvBfrT49C4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af9bb34f.mp4?token=bzbOSkBVPogX9FeutpzdxMjj_KGy6StqQXbgxcHeAaJm8t23pyDHN3SE-lvJFkQ2t4NteosAwFtYLsIJhAzC7yQoOOhUHDZzNEhGfppZglaM81e7fWHEUgKTp6zfikF4vb2CsjPS9WVjdhjikR4Rk2yH-kqpvKmlNuT907k-9eG3MoHzsdGoyQivak4lpfbDqOjEIvnYdomIffcoH2NyNBP1Vkem9RdoGWIW0Z5OUEar2m5T6xRnFneNiDiOVRj6e6V5qdfXsqIQICjwjrS7EbmlhDbkz0dcx7ZOlBlTaJIvY2Hbuyc1NGGARkHO_cV4yylA59jxVsmd9hby_f4WpJI1g8Yf5lL-ZnPePRk0LbweBTZeGP63upwLtk3Y-Jpdbm_9NQO2jwrBU9oFcKyEsX0p5g3sRQL5OH9WsbBAEAWx2ATpWIrLYXS6pCju0zRv_ZGO71CgZxlCtD9dklUIss7V3dhGxyqeezeHgluEkdRAKc2i2v2Og_zdyw1kfvZsyrDabTjWQDLmXiTGxK4ZTXPToz1IVxduR2gL6cMeoK0t3xcmxrR7K9pM7XC_BoVXYZ1OJp4QR6hzlCqb931pRQGyHhIErzDXdN-KJ2jC3gLpDL2sSwjjePEKPVPCJznUYrgkYVNcCs0EYYaRxWHmktraKLfiPo1LfvBfrT49C4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم در میدان، نقشهٔ دشمن را ناکام گذاشت
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/462677" target="_blank">📅 22:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462676">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
چند روز پیش به درخواست دختر نوجوانم، برایش یک چادر نماز گل‌گلی و زیبا دوختم. اما به محض اینکه کار تمام شد، گفت: «نمی‌خواهم مثل زندانی‌ها باشم.» لطفاً
مجرمان را با لباس متناسب شأن خودشان به مردم نشان دهید
، نه با پوششی که نماد یکی از مقدس‌ترین اعمال دینی ماست.
🔹
بنده
متقاضی پروژه ۸۱۰۰ واحدی مسکن ملی اراک
هستم. از سال ۱۴۰۰ تاکنون برای تأمین آورده، حتی طلاهای خود را فروختم و حدود ۱۳۰ میلیون تومان واریز کردم. تا قبل از سال ۱۴۰۵ نیز برای تأمین مبالغی که راه و شهرسازی اعلام می‌کرد، ماشینم را فروختم. تمام واریزی‌های من به‌موقع و حتی زودتر از مهلت‌های اعلام‌شده انجام شده است. قرار بود این واحدها حداکثر طی دو سال و با حدود ۳۰۰ تا ۴۰۰ میلیون تومان آورده متقاضی، به‌علاوه ۳۵۰ میلیون تومان تسهیلات بانکی، تحویل داده شوند. اما
حالا صحبت از هزینه‌ای حدود ۴ میلیارد تومان است
. به خدا مستأجرم، یک فرزند دارم و دیگر توان تأمین این مبالغ را ندارم.
🔹
برای تمدید
بیمه بدنه
خودروی سمند سورن مدل ۱۴۰۱ به بیمه ایران مراجعه کردم. گفتند باید پوشش «جبران زیان وارده به خودروهای نامتعارف» را هم به بیمه‌نامه اضافه کنم. وقتی گفتم خودرو من سمند سورن است و خودروی لوکس یا نامتعارفی نیست، پاسخ دادند طبق قانون
چون ارزش خودرو بیش از یک میلیارد تومان شده، نامتعارف محسوب می‌شود
. سؤال ما این است که چرا باید خودرویی مانند سمند سورن به‌دلیل افزایش قیمت خودرو، نامتعارف محسوب شود؟ آیا این قانون با شرایط و قیمت‌های امروز خودرو تناسب دارد؟
🔹
قسمت میانی
جاده خوشنام ملارد به سمت شهرک ناز فردیس
، به طول حدود ۴۰۰ متر،
بین دو استان تهران و البرز بلاتکلیف مانده
است. با وجود اینکه روزانه هزاران خودرو از این مسیر عبور می‌کنند، آسفالت این بخش به‌شدت تخریب شده و باعث آسیب جدی به خودروها و بروز تصادفات زیادی شده است. متأسفانه مسئولان هر یک از دو استان رسیدگی به این مسیر را بر عهده استان دیگر می‌گذارند و در این میان، مردم متحمل خسارت و هزینه‌های سنگین تعمیر خودرو می‌شوند.
🔹
من از
زاهدان
هستم و مشکل ما در این شهر،
وضعیت نامناسب نظافت و بهداشت شهری
است. سال‌هاست با این مشکل مواجهیم؛ زباله‌ها به‌موقع و به‌خوبی جمع‌آوری نمی‌شوند و بوی تعفن آب‌های راکد و تجمع زباله در جوی‌ها، به‌ویژه در خیابان معلم، محدوده باغ خانواده، واقعاً آزاردهنده شده است. وضعیت سرویس اتوبوس شهری نیز نابسامان است و مردم با مشکلات زیادی در زمینه حمل‌ونقل عمومی مواجه هستند.
🔹
شرکت
مدیران خودرو
از پذیرش خودروهای دارای گارانتی، به بهانه نبود قطعات خودداری می‌کند و در این زمینه نیز پاسخ‌گوی مشتریان نیست. خودروها معمولاً هفته‌ها در بلاتکلیفی کامل باقی می‌مانند و مالکان نمی‌دانند چه زمانی مشکل خودروشان برطرف خواهد شد. لطفاً با ارتباط‌گیری با مسئولان ذی‌ربط، این موضوع را پیگیری و خودروساز را ملزم به انجام
تعهدات گارانتی و پاسخ‌گویی به مشتریان
کنید.
🔹
مدتی است در
تهران
قرار است برخی منازل به فیبر نوری مجهز شوند. سؤال ما این است که آیا توسعه و
واگذاری خطوط مخابراتی و فیبر نوری
وظیفه مخابرات نیست؟ پس چرا شرکت‌های خصوصی برای انجام این کار از مردم مبالغ بالایی دریافت می‌کنند؟
🔹
از استان قزوین، شهر
بویین‌زهرا
مزاحم شما شدم. متأسفانه در پروژه
مسکن ملی ۵۴۴ واحدی
که در انتهای بلوار آزادگان قرار دارد هنوز از کابل تلفن و کابل فیبر نوری خبری نیست و آنتن‌دهی اینترنت ایرانسل نیز بسیار نامناسب است. خواهشمندیم مسئولان برای
تأمین امکانات ارتباطی
این پروژه و رفع مشکل آنتن‌دهی اینترنت اقدام کنند.
🔹
در
پارک شاپوری خرم‌آباد
، درِ سرویس‌های بهداشتی شب‌ها و درست در ساعات اوج شلوغی پارک بسته است. بچه‌ای که چند ساعت در پارک مشغول بازی و تفریح است، طبیعتاً ممکن است نیاز به
سرویس بهداشتی
پیدا کند؛ در این شرایط باید کجا برود؟
🔹
ما
کارمندان
معمولاً سالی ۱۰ روز تا دو هفته مرخصی می‌گیریم تا به مسافرت برویم. با توجه به هزینه بالای بلیت هواپیما و قطار به‌خصوص برای خانواده‌ای ۶ نفره، عملاً امکان استفاده از این وسایل حمل‌ونقل را نداریم و مجبوریم با خودروی شخصی سفر کنیم. متأسفانه با سهمیه سوخت موجود در کارت‌های شخصی و محدودیت ا
ستفاده از کارت‌های سوخت جایگاه‌ها در سفرها
با مشکل جدی مواجه شده‌ایم و مجبوریم برای استفاده از کارت جایگاه، مدام از این و آن درخواست کنیم. دولت باید برای فصل سفر برنامه و تدبیر ویژه‌ای در نظر بگیرد.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/462676" target="_blank">📅 22:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462675">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GglIBzNETOLBUeEcgcQN0djB3uu7yCbhR_JJO7OPtg2itLyGmiCInsWYijPA_kfEZc2warC5H0S1R97TTEXQlNCfY2JB66XaTAiUZqUnxZrdBiAsInGyxo6vmvKAU8UVLeD3rI-BR6MJW5ZfrWkdc8hlxMpcpzV8Y1opSQu8RF_6zLZk1WjRdtXWV_LDztD57-wCWSNlpEm4vrnHsWN8P_NkQTnqPmNM1RMylUYOlE3avm0TZMUvJkm1WCQvpkOLDsj9zdS3b32Nc12ALjJ1isXvybDY9fAEYE1TQ0aR6Wln2Uez6c77othFvp4FLFBCWRblEo1CgHRj179K_2XLgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر صفوی: یمن افسانهٔ شکست‌ناپذیری آمریکا را برای همیشه دفن کرد
🔹
از صنعا تا باب‌المندب، یمن با ایمان و اراده، افسانه شکست‌ناپذیری آمریکا را برای همیشه دفن کرد. این فتح مبارک را به ملت قهرمان یمن و فرماندهان انصارالله تبریک می‌گویم.
@Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/462675" target="_blank">📅 22:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462674">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935eb96623.mp4?token=hitrO5vshBpIBOPwJkElb8U8BQfqJsaLMuQl0P7hkwIg1wkqwpSo7X8fZVURWUt4bEUPXtqDT-2WKbX0BPsnf7tC7OeTkrwZ6XtsUX5iuoB_ArtVyc95zitZnl_83neVGGonjgLtT21_TJpavzHuQ0CRgzGF0VCe-n9YCJP7tTlFCwiaySKZ8QTvzTkz_JWijcWmzjVtEZpx2acFr8zMyaWv-mOH_X65WEvCFsPY-gKAnjNnkg4Zj9yoREMd2Au82IEcz15eHeTevx-5FKfOgrEl185nAz_5yWhluezYbDwNz1xlZAwWDsN9erAGCUgCm4weys6-irHtkaxSnekVQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935eb96623.mp4?token=hitrO5vshBpIBOPwJkElb8U8BQfqJsaLMuQl0P7hkwIg1wkqwpSo7X8fZVURWUt4bEUPXtqDT-2WKbX0BPsnf7tC7OeTkrwZ6XtsUX5iuoB_ArtVyc95zitZnl_83neVGGonjgLtT21_TJpavzHuQ0CRgzGF0VCe-n9YCJP7tTlFCwiaySKZ8QTvzTkz_JWijcWmzjVtEZpx2acFr8zMyaWv-mOH_X65WEvCFsPY-gKAnjNnkg4Zj9yoREMd2Au82IEcz15eHeTevx-5FKfOgrEl185nAz_5yWhluezYbDwNz1xlZAwWDsN9erAGCUgCm4weys6-irHtkaxSnekVQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۱ شب گذشت؛ اما صف مردم برای ایستادگی هنوز ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/462674" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462673">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3df65ffe6.mp4?token=k_8WpGGj2gn4LrlJaML_QoLDN7EMa40eYSeCA7hOxH-MRqsHVTRNGXbRN8jPQYUcBzWUYcGET8RwAVmTi5iEfGAB05Ov20svUXDt1WoqC2jvWLdwM79yg0l6O_GNcn1zAEB_8UvmmLSxO-7KYWwag3vgl0x9StOqf8KRqPJNVOj-MW2lTCeZFw0XCu0C_OZY43aNSwCNYOJ49D25nZu5sriDo64e6zQbiibqXQTR1KRryyKMb3zfH3A4tvx7sPyhvl4t5Z1cauDPP0muKW3-WBt0YTF3KbghRfA2gnTNDXxoa_5LkPgdEkfXkJsFESQnV10mpDwaIERsjxaOMurgt0VbbwXrQ9dApvNL-FucY4CT-qNcIoWX00-EazwzJNqhfTAMWESGerVIFplk_44ZcaLAwrTXsFnSFGqf1gw57Om7gZicp9pW4Atluzzow4PEp-qsnm0aoEsws-HYtyDVXf35oHWlQ_641Nfq6_7wcq3YJSaaJLBkqXuEcQ6cnXbtPFMpPBucFu3KxHfRsWMl6jUA0ajNWPPXnTNs4fWJxZhSjavSuZK5xRYlvXmVaE4DxeXm1S3utZ6GKY2rxqx-mjsLxpw1WxGGWaHkJK3YQOwsj-7bXc4BdABO_OgjlvVdpvr1PILKFY_wtnV1OgiQBfRnnwSxO7mLgnXWs40n8qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3df65ffe6.mp4?token=k_8WpGGj2gn4LrlJaML_QoLDN7EMa40eYSeCA7hOxH-MRqsHVTRNGXbRN8jPQYUcBzWUYcGET8RwAVmTi5iEfGAB05Ov20svUXDt1WoqC2jvWLdwM79yg0l6O_GNcn1zAEB_8UvmmLSxO-7KYWwag3vgl0x9StOqf8KRqPJNVOj-MW2lTCeZFw0XCu0C_OZY43aNSwCNYOJ49D25nZu5sriDo64e6zQbiibqXQTR1KRryyKMb3zfH3A4tvx7sPyhvl4t5Z1cauDPP0muKW3-WBt0YTF3KbghRfA2gnTNDXxoa_5LkPgdEkfXkJsFESQnV10mpDwaIERsjxaOMurgt0VbbwXrQ9dApvNL-FucY4CT-qNcIoWX00-EazwzJNqhfTAMWESGerVIFplk_44ZcaLAwrTXsFnSFGqf1gw57Om7gZicp9pW4Atluzzow4PEp-qsnm0aoEsws-HYtyDVXf35oHWlQ_641Nfq6_7wcq3YJSaaJLBkqXuEcQ6cnXbtPFMpPBucFu3KxHfRsWMl6jUA0ajNWPPXnTNs4fWJxZhSjavSuZK5xRYlvXmVaE4DxeXm1S3utZ6GKY2rxqx-mjsLxpw1WxGGWaHkJK3YQOwsj-7bXc4BdABO_OgjlvVdpvr1PILKFY_wtnV1OgiQBfRnnwSxO7mLgnXWs40n8qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدارهای صمیمانهٔ خانواده‌های معظم شهدا با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/462673" target="_blank">📅 21:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462672">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آمریکا به عربستان اف-۳۵ می‌فروشد
🔹
آمریکا ۴۸ فروند جنگنده اف-۳۵ به عربستان سعودی می‌فروشد؛ معامله‌ای به ارزش حداکثر ۲۴.۳ میلیارد دلار که اولین خرید اف-۳۵ توسط عربستان در تاریخ است.
🔸
وزارت خارجهٔ آمریکا امروز کنگره را در جریان این معامله گذاشت و آن را برای «بهبود امنیت یک متحد اصلی غیرناتو» ضروری خواند.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/462672" target="_blank">📅 21:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462671">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8043bfa4.mp4?token=buUpzfb2u_DJr6qnF1WI-rBguLGEZcEqJnHuUNmzpoblIpiotlAsvunkM3RdSzZ7bD3Dzeo3TeQlz-Cz-QPsg8lmwY7qDi6pX3KlsFc9Wlt6v2EvwFXKPo688RK9Df7KG-JqxU9SdyaD2Hae8LG0UE7JTfa4vVNQlocbRVvm9SWmLToLZEwRY_Hkzsnx8WIMKXlr_V0IIvf2-ygpcs2jBjibwkxjBAltZsYx5xjl6K04R3jx3UmsxjbMgcfajRjJ-DDO96xqdCO-5irA9nuE2nHGNSUJpt5fysfI-0xpDymHgNfyZ6Ze6cemUGk2OA7eHS27HBJcL6FgrFaMXRbpqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8043bfa4.mp4?token=buUpzfb2u_DJr6qnF1WI-rBguLGEZcEqJnHuUNmzpoblIpiotlAsvunkM3RdSzZ7bD3Dzeo3TeQlz-Cz-QPsg8lmwY7qDi6pX3KlsFc9Wlt6v2EvwFXKPo688RK9Df7KG-JqxU9SdyaD2Hae8LG0UE7JTfa4vVNQlocbRVvm9SWmLToLZEwRY_Hkzsnx8WIMKXlr_V0IIvf2-ygpcs2jBjibwkxjBAltZsYx5xjl6K04R3jx3UmsxjbMgcfajRjJ-DDO96xqdCO-5irA9nuE2nHGNSUJpt5fysfI-0xpDymHgNfyZ6Ze6cemUGk2OA7eHS27HBJcL6FgrFaMXRbpqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم شهرکرد در شب ۲۰۱؛ هم‌صدا با یمن
شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/462671" target="_blank">📅 21:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462670">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbNlH4QBnYOtproC9RO6kjw_owqOl2DBNtqRs7A4Egvaw3zsBh7q968dCxtlBfHjm2JPbvF5WNsmgIk8VMYcjyjPREVTHdZS9GUVrrOFywmHy4xA-KIZ7jY1S-sQh78rYyvyOp5zW5qZmc7ISReGdPg8srMnhJCDjKOYdRtAv5jb1lM3Ua4HiDBrs58p902fzeETODa8ucWG6EQM9ArejLdSDl1hzr7xo7EVe0iT83E-qiVlB_gXfFQ9wBh5iKBAI5XGoPGm4_qy5_7xcDEYM5PmCmztMPTe8eCZ55zc5PkuNEcx6K0L5AZcXdLvrntYx_no__6KkT96iPad0He8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جبلی: فرهنگ‌سازی و مطالبه‌گری اقتصادی در رسانه ملی تقویت می‌شود
🔹
رئیس صداوسیما: در سال‌های گذشته، رسانه ملی در موضوعاتی همچون اجرای قانون مجوزهای کسب‌وکار و پنجره واحد خدمات دولت الکترونیک نقش مطالبه‌گرانه داشته و در موضوع ناترازی انرژی نیز با تمرکز بر فرهنگ‌سازی مصرف بهینه توانسته است به کاهش مصرف کمک کند.
🔹
این تجربه‌ها مسئولیت رسانه ملی را سنگین‌تر می‌کند؛ اگر با پیگیری، تمرکز و استفاده از همه ظرفیت‌ها توانسته‌ایم در یک موضوع خاص به حل مشکل کمک کنیم، می‌توانیم در سایر مسائل نیز نقش مؤثرتری ایفا کنیم.
🔹
وظیفهٔ رسانه ملی فرهنگ‌سازی، مطالبه‌گری و معرفی ظرفیت‌ها و دستاوردهاست و در همین راستا پیشنهاد شده است در شبکه‌های اصلی، برنامه‌های تخصصی و ثابت برای پیگیری مسائل حوزه‌های مختلف از جمله اقتصاد، صنعت، کشاورزی، معدن و مسائل مرزی استان‌ها ایجاد شود.
🔹
در کنار برنامه‌های تبلیغاتی، باید برنامه‌های مطالبه‌گرانه اقتصادی، فرهنگ‌سازی، بازارسازی و معرفی دستاوردهای کشور نیز تقویت شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/462670" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462669">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb326ea94.mp4?token=Y7iRc_a9h_WIELbaQpK_vxJtjVafXe5Ax_tKq2MPv2WYTyvH1HUIfh0QQQkOXD8oGQYOUX4doC6lKDilbWypX2XbrYfDjMsMP9YcXrNJOhWuQS4YocTUxMb7vvpjhBt-4I5NH8BgP2P12RwFwrLMgORZ4OFjdluYV3vJLNXKBrKHzBYb7kpyyxHcXXWCHPUnLjV_WgmiTHnJCs2207S18gxzyX1FMhgHGjIsGEqV5lBWDCmbEiqzLQUhgaDDCWwvRsekCYuIloVPlWp9rjV0b-QXjDh7QrH4qEI6CUnmUFXIoe4nCa0qGMlKxyTIo6LSTjP6FnBcWdeJmuDTzv2sfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb326ea94.mp4?token=Y7iRc_a9h_WIELbaQpK_vxJtjVafXe5Ax_tKq2MPv2WYTyvH1HUIfh0QQQkOXD8oGQYOUX4doC6lKDilbWypX2XbrYfDjMsMP9YcXrNJOhWuQS4YocTUxMb7vvpjhBt-4I5NH8BgP2P12RwFwrLMgORZ4OFjdluYV3vJLNXKBrKHzBYb7kpyyxHcXXWCHPUnLjV_WgmiTHnJCs2207S18gxzyX1FMhgHGjIsGEqV5lBWDCmbEiqzLQUhgaDDCWwvRsekCYuIloVPlWp9rjV0b-QXjDh7QrH4qEI6CUnmUFXIoe4nCa0qGMlKxyTIo6LSTjP6FnBcWdeJmuDTzv2sfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شام شب ۲۰۰ فرق داشت!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/462669" target="_blank">📅 21:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462668">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1110a925.mp4?token=Hj4APfAy0vF7Pw8-qKWa-xH_Zf22yphcUIp28x3pE9hbsLzqENhk47UWzhWPaISFIoBomHSDiASA0fpOBOTC0MYTl05c_xkT9SKjJHzf10xSX4GAKvt7MD2Rc9wOSiUeCvXRKhTojAxkd1Y9rWEq6F5WfUkLc4Gv7nPaMfnJBAJfkghVRUEaymSEI9OTpwLFkSV7lq_uEg9vaT5YjT-iF47K5pjzPZBAb8G7KgqQapis2VwDbvkTP3J_foG203KLRu_m2fnZLgJGaix5SGFwSjf9NcNsjnDMJ99f68WYv79IsszVaLr6RI4jh5kiV39qvaInfKlFu2nAlRsf7-h8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1110a925.mp4?token=Hj4APfAy0vF7Pw8-qKWa-xH_Zf22yphcUIp28x3pE9hbsLzqENhk47UWzhWPaISFIoBomHSDiASA0fpOBOTC0MYTl05c_xkT9SKjJHzf10xSX4GAKvt7MD2Rc9wOSiUeCvXRKhTojAxkd1Y9rWEq6F5WfUkLc4Gv7nPaMfnJBAJfkghVRUEaymSEI9OTpwLFkSV7lq_uEg9vaT5YjT-iF47K5pjzPZBAb8G7KgqQapis2VwDbvkTP3J_foG203KLRu_m2fnZLgJGaix5SGFwSjf9NcNsjnDMJ99f68WYv79IsszVaLr6RI4jh5kiV39qvaInfKlFu2nAlRsf7-h8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام میرهاشم حسینی: بدترین طلسم زندگی گاهی همین زبان آدم است؛ یک تهمت، غیبت یا بدگویی می‌تواند زندگی را به هم بریزد
🔹
زخم زبان دردناک‌تر و اثرگذارتر از زخم شمشیر است.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/462668" target="_blank">📅 21:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462667">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e436cc3d33.mp4?token=GxpmtVlcnysPB1wSeLVibp1MBiiEzZHdy8OWL1-1KKOPgzO7zJhSqzOc9_3w3WETxD7RJ2Z5CHx2wh1SIdXp9co-jZKcQb-5UHLme_y7gBQk92NBtBP4dyIeCCmk7EQsCUE9YoD94w4tmylRG3ZL9JqjUAk-bHbL7BthAdb8ewFUuLw9-uDzN7d-TPIzrvvFBPHajNiBmvRLQ8p7rPzI3Ju_OHx3DjlA5IbMQLsV-mxsAMnxqMuGw0HUSZeYwjLrG2Gm5z8vhj_iWmMHL43Y9IM8AoaG04evouxQH5sokUAyVaqbm0FMX_Tk_3C_YSA2OLe__6q8t2ebjKA5n2CDcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e436cc3d33.mp4?token=GxpmtVlcnysPB1wSeLVibp1MBiiEzZHdy8OWL1-1KKOPgzO7zJhSqzOc9_3w3WETxD7RJ2Z5CHx2wh1SIdXp9co-jZKcQb-5UHLme_y7gBQk92NBtBP4dyIeCCmk7EQsCUE9YoD94w4tmylRG3ZL9JqjUAk-bHbL7BthAdb8ewFUuLw9-uDzN7d-TPIzrvvFBPHajNiBmvRLQ8p7rPzI3Ju_OHx3DjlA5IbMQLsV-mxsAMnxqMuGw0HUSZeYwjLrG2Gm5z8vhj_iWmMHL43Y9IM8AoaG04evouxQH5sokUAyVaqbm0FMX_Tk_3C_YSA2OLe__6q8t2ebjKA5n2CDcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهریور با سفرهای آخرش می‌چسبه
@Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/462667" target="_blank">📅 21:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462666">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8246fc0ad6.mp4?token=tDwpmHVMKDaQwJpJAIqcVIQxiEEy9MyPAy3StnmF7mfilEu6WcZ6SW6w-2zoqL5Tl82ravQ2GIZH8o9tK0po9MSvluzGbDdUvQZaQPDBLXAFp4Vi8Y2jlwZIkDrh7GoLDUqujY4-9gfi5OtxN_CSLFvjowe_FJK_RhuSvwm8sWOy8qBgel5Tq5YckTwep1_O0NM9rc01NO9wwDTbmMpiJEFPsz6RvZtbhefLdpgmZWBpdjMHE5TVC37kFHqlBGp__Ts7Ft0yvf3zyrPXjoxkPS5EmApLyxzd7BUvIWjza6F8tdar16yIXXAT9mqA0YcrLnWkx29aA7m0rxMXe5mzfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8246fc0ad6.mp4?token=tDwpmHVMKDaQwJpJAIqcVIQxiEEy9MyPAy3StnmF7mfilEu6WcZ6SW6w-2zoqL5Tl82ravQ2GIZH8o9tK0po9MSvluzGbDdUvQZaQPDBLXAFp4Vi8Y2jlwZIkDrh7GoLDUqujY4-9gfi5OtxN_CSLFvjowe_FJK_RhuSvwm8sWOy8qBgel5Tq5YckTwep1_O0NM9rc01NO9wwDTbmMpiJEFPsz6RvZtbhefLdpgmZWBpdjMHE5TVC37kFHqlBGp__Ts7Ft0yvf3zyrPXjoxkPS5EmApLyxzd7BUvIWjza6F8tdar16yIXXAT9mqA0YcrLnWkx29aA7m0rxMXe5mzfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاظمی، سخنگوی قوه قضاییه: پروندهٔ ترور امام شهید به دادگاه می‌رود
🔹
برای ۱۵۹ تن از مقامات ارشد سیاسی و نظامی دولت آمریکا و رژیم صهیونیستی کیفرخواست صادر شده است.
🔹
۶۷ نفر از این مقامات اسرائیلی و ۹۲ نفر آمریکایی هستد.
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/462666" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462665">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089efc431.mp4?token=glec24HgcdY3W5f89fmhcQdwA4lNM2fivmtutxh18o7iEZyyGuvKz0mu0SblAnKBEQt2lkc5YEy_MQTQ4M6BiO_rC0TpfehsCTo5eAo0BeFHwWISh4bJpgw4CrYDmLjRaZervV20xGoMaenCW5po7MTkMrOi0DHOtKP5_EUsvcDukktmBsdUE0lfDNnjWaiDbu1PbI4PI9E5dNrmKt5ZnJujQZQXbQr6Sal7dbadKhrHboAgX9hKVB2wpfKkIzGrPSiWaAsqB4iJF1am0SDWevu8QiRtGHrJHx8o99jaEal5Uo7yMQt-rpJ-IMGpn-p6MrGYSNqHhAFGYbHHrg8k0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089efc431.mp4?token=glec24HgcdY3W5f89fmhcQdwA4lNM2fivmtutxh18o7iEZyyGuvKz0mu0SblAnKBEQt2lkc5YEy_MQTQ4M6BiO_rC0TpfehsCTo5eAo0BeFHwWISh4bJpgw4CrYDmLjRaZervV20xGoMaenCW5po7MTkMrOi0DHOtKP5_EUsvcDukktmBsdUE0lfDNnjWaiDbu1PbI4PI9E5dNrmKt5ZnJujQZQXbQr6Sal7dbadKhrHboAgX9hKVB2wpfKkIzGrPSiWaAsqB4iJF1am0SDWevu8QiRtGHrJHx8o99jaEal5Uo7yMQt-rpJ-IMGpn-p6MrGYSNqHhAFGYbHHrg8k0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی براندازها برای موج‌سواری سراغ بنزین می‌روند
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/462665" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462664">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
در ۲۰۰ شب حضور مردم، خیابان‌ها چه روایتی داشتند؟
@Farsna</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/462664" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462663">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d30f65bde.mp4?token=i3m-xSh5dHd9omY2uDgQ2sCL57hH5ZlLkv7FNaN6xEXeW4_HA3ZH1tC-Wi8f1UsFTGw86PzWirDVx51O27x3PrqAYR4eQ64JjTWyIGBCWalLLUNWCMexPUCEuGdAZ2wlg1QhVSLpwbwfZxO_EdSRX1C6U5ur7brZhe5Pqmq4sVOJsxKtd4QyGzqJLYeBUQawSHou4bDxEs8-X2p2SlfuGYkA6T7BswZ0bWzJiH4x_SEW9MxYyCdzTQJR-2xQe9YepaMTYhOhmm_HHYiC5gt27Jb-WEdA9wy_vMG24-k3mklkTzwlGQUpMiNSJjY8PTlSMNN8eTs1XTeqkdAStoqBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d30f65bde.mp4?token=i3m-xSh5dHd9omY2uDgQ2sCL57hH5ZlLkv7FNaN6xEXeW4_HA3ZH1tC-Wi8f1UsFTGw86PzWirDVx51O27x3PrqAYR4eQ64JjTWyIGBCWalLLUNWCMexPUCEuGdAZ2wlg1QhVSLpwbwfZxO_EdSRX1C6U5ur7brZhe5Pqmq4sVOJsxKtd4QyGzqJLYeBUQawSHou4bDxEs8-X2p2SlfuGYkA6T7BswZ0bWzJiH4x_SEW9MxYyCdzTQJR-2xQe9YepaMTYhOhmm_HHYiC5gt27Jb-WEdA9wy_vMG24-k3mklkTzwlGQUpMiNSJjY8PTlSMNN8eTs1XTeqkdAStoqBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: همهٔ مدیران در تمام سطوح نیازمند آموزش هستند  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462663" target="_blank">📅 20:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462662">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343ca3619f.mp4?token=a-eEY13ASMSuGt8_0eQgg09XU4q7ilg6q0SD9r-a6H0-WmiJbNgfnkgo00dSoVt3nabr5oJUabHT_m8_97leGu4M0pm89uZ10N-REWRzE3oTjcJU23aETUipRlilmr37WbObyBa_gFJ04MO4qY1rPec_vggCnGkJUBxutyoOQEOXw06U4MoTjnPXa_LRIoOqkG6YIOcjY6tm99c3Tlaqr1VT5SwYHdpG1WMlwioRr4ZQ36LZUGVc9AfRZBwk-eDEj6Jyr-axxKu1KeMID2awRB-3DHVO7du7RbV5GS0HLDC7VufpN449WNOTnPg-QvL-RPs6AVFXmOAeiMQ680IKhGWs2hoJQyIWjJjgecn_x17rZH094rIDBgtLKC7HiJmkmm9uTvgkC6IpPa9OR9VzMEDsyLMjFN1C56nusl4LuRYJoNVZqO49X_uZBxIsGl4XypabZt5vcwWTJ7fWWd7Y8FkUVuESqjGYN0fq-bTdf8FQ91TNrlJIHzjh249tJDTHJ8WfzKBJR3MGQMUwPf2zcdeHFXVdasio-flhozDFULTLeMzqXFjmwaQK1Zztmq5VrA5btwH1XfXjXZVhVIpL9Fzr2JuRaxrd3jAyNWdiGY20iVrkc_UVIqHHXZF6PUM53k9xhuBL9k7klZeMgdeBfHfmw4qSmzJUGuO6j-cAcEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343ca3619f.mp4?token=a-eEY13ASMSuGt8_0eQgg09XU4q7ilg6q0SD9r-a6H0-WmiJbNgfnkgo00dSoVt3nabr5oJUabHT_m8_97leGu4M0pm89uZ10N-REWRzE3oTjcJU23aETUipRlilmr37WbObyBa_gFJ04MO4qY1rPec_vggCnGkJUBxutyoOQEOXw06U4MoTjnPXa_LRIoOqkG6YIOcjY6tm99c3Tlaqr1VT5SwYHdpG1WMlwioRr4ZQ36LZUGVc9AfRZBwk-eDEj6Jyr-axxKu1KeMID2awRB-3DHVO7du7RbV5GS0HLDC7VufpN449WNOTnPg-QvL-RPs6AVFXmOAeiMQ680IKhGWs2hoJQyIWjJjgecn_x17rZH094rIDBgtLKC7HiJmkmm9uTvgkC6IpPa9OR9VzMEDsyLMjFN1C56nusl4LuRYJoNVZqO49X_uZBxIsGl4XypabZt5vcwWTJ7fWWd7Y8FkUVuESqjGYN0fq-bTdf8FQ91TNrlJIHzjh249tJDTHJ8WfzKBJR3MGQMUwPf2zcdeHFXVdasio-flhozDFULTLeMzqXFjmwaQK1Zztmq5VrA5btwH1XfXjXZVhVIpL9Fzr2JuRaxrd3jAyNWdiGY20iVrkc_UVIqHHXZF6PUM53k9xhuBL9k7klZeMgdeBfHfmw4qSmzJUGuO6j-cAcEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیلی نوجوانان پیشوا به هذیان‌گویی «اینترنشنال»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462662" target="_blank">📅 20:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462661">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2TqcvKQaZQLA-wCXVla9h-5RwkUHu6OstqR6QBn5p7ZphvW-ZpfE9ukkCtIEplI1hjWBy1kNPVwkhgKqjMgJYhpg3zy7kJ_0Yt60Yr9XHt2sZmjZxvwBjey9OUeIJdipSoA6GO8hcpx6fPHehorclPHt8cSVXG15qmzyZGIxyGqxtaQi292m3dFuO0AR_XwSK1qxVbCCuB70vfHXAsSvnRlhXzTpbpU9i-FqW6AgcufOo3HyFGtONHJRqe1NYyqYWlFwGGNTgHtcS5Odz_KnsYnjuNBiS0MG-z5-9tY-0U_FluBDwShvRbe72o3J5R768pDji6ZAMiTtD6wL1SNYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجارهای کنترل شده در ساوه
🔹
ناحیه مقاومت بسیج ساوه: هم‌زمان با برگزاری نمایش بزرگ محیطی و میدانی «معبر ۳»، صدای تیراندازی و انفجارهای محدود و کنترل‌شده از شنبه ۲۸ شهریورماه به مدت ۷ شب در این شهر شنیده خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462661" target="_blank">📅 20:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
وقوع حادثه برای یک نفتکش در سواحل یمن
🔹
سازمان عملیات تجارت دریایی بریتانیا امروز پنجشنبه از یک حادثه برای یک کشتی در سواحل یمن خبر داد.
🔸
هنوز هویت نفتکش و عامل حمله مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462660" target="_blank">📅 19:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b4e86e47d.mp4?token=T548hUzdF9jRW09ODJVR-dcPBYbDKgqeuRART6OZP4dyMDwetRXx5dDpND_kmGN3wXAlemmipt5sGw2F9jxbjJL82p9w9QpiCWSCdCkb_02EOJOPq6vOjhMYOugc8_VRbmwHS_1FU54w6Uufpk_TwkVjb8Cc6XUKNuyQXYqkAyDZnnVCsmk6auaO8adFpxu8qkZ4S5l7KntN8T5ImJ0UXxda5iA35-ctzv1OfOhIj5Gb8-oFbHC_EiZzMY063h0GDT52DzW1g-NuqP4buyrO_esiVWqW-Y2X6f-zvxyjvOrLyaBXNANTbqogG7mNa9CJgBgyc_tOkO-P8Q7_7v6XNJhF72nTi6wamKEwL8-1b4KU8syD-TIpCWr5ard9Kc-d2_6uuqFvNMw6Yv4OE-OtKVsCbTZGWfdLHOzt3_7NVQsQ9DAxQez4wAsJI20K7VivNVxBljdAmML_7earo2Sbb46Q9i0_M_ZO55exF9cX95Et9D3vnAeTEFEewhBhjRu2W8uJ-Ca-bLyutwQAG-5LUN8XLH8K6w20CgKCNeghZeSB9nkgg2I-iHcO1iRS4jUPn3nP-25EMGhvmJuwOET5FVgniJuxb9GY7_w6N0DCFyY7Id-JvQYCiaKCcE8oPGWfdreCgLgtpSJYbwOiP4V8ihXKd8xYieFHMfzfzxPc50M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b4e86e47d.mp4?token=T548hUzdF9jRW09ODJVR-dcPBYbDKgqeuRART6OZP4dyMDwetRXx5dDpND_kmGN3wXAlemmipt5sGw2F9jxbjJL82p9w9QpiCWSCdCkb_02EOJOPq6vOjhMYOugc8_VRbmwHS_1FU54w6Uufpk_TwkVjb8Cc6XUKNuyQXYqkAyDZnnVCsmk6auaO8adFpxu8qkZ4S5l7KntN8T5ImJ0UXxda5iA35-ctzv1OfOhIj5Gb8-oFbHC_EiZzMY063h0GDT52DzW1g-NuqP4buyrO_esiVWqW-Y2X6f-zvxyjvOrLyaBXNANTbqogG7mNa9CJgBgyc_tOkO-P8Q7_7v6XNJhF72nTi6wamKEwL8-1b4KU8syD-TIpCWr5ard9Kc-d2_6uuqFvNMw6Yv4OE-OtKVsCbTZGWfdLHOzt3_7NVQsQ9DAxQez4wAsJI20K7VivNVxBljdAmML_7earo2Sbb46Q9i0_M_ZO55exF9cX95Et9D3vnAeTEFEewhBhjRu2W8uJ-Ca-bLyutwQAG-5LUN8XLH8K6w20CgKCNeghZeSB9nkgg2I-iHcO1iRS4jUPn3nP-25EMGhvmJuwOET5FVgniJuxb9GY7_w6N0DCFyY7Id-JvQYCiaKCcE8oPGWfdreCgLgtpSJYbwOiP4V8ihXKd8xYieFHMfzfzxPc50M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردمِ متحد، شکست نخواهند خورد
🎙
نماهنگ «خدا با ماست» با صدای محمود کریمی به زبان انگلیسی
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462659" target="_blank">📅 19:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e003523.mp4?token=Jq2f2I_2DNfFPnxIrO2BnKqx2uv6_X-CBRw2Rvy3I6qzmNxdkl6R2kj3FrJH4blU546dqVA-PhISNqLPtIgs4o5vBiE-VaMLGaC85AOVBWjnKmFIOdRAqDFLtoWcfJH4liIXyCHCZBSAaELFEP3-PqafuRQ8gsABQ9vcOzKPQE96zzBez7yz-5FqY9VKyFlzs6qvPBXJgU5HCzr_pgeQE8T7bL-8aSzg3PfCX1EFMd2sumUECu-xbVBiAsyeEcEPMBoY0kBFky0btJxA0aTMJPAlJy6gJYs0ayxvWrniQaS61p7EIbVHF7onFwPd6ojsQzdEEFLqjjWknpc27OZgOAQw_vJSxYqdrqiL0N031vk8ly11L4eamIaOoVgrD7TBzhLDIBhIx3TnTl3FEr6mRqMT2xdkJnEBH0p9TuD5-h8EDS-CDBDZzFNVSPaoU47atVpei3vSmh1QtJjEPUBdUsPPqFFVgKWcSyjrPCw20tjM3YgKOJNqkQJ7JWun6B5QyMj6cn7CvyGsdsx5bbnHnuiv7Aa91ge_dUjlnUTjpmSM8ocOGHZXBt2r1PeriDRja2aU9KPeFBK9n4OHezAwNlxgFTRk4tEajyYbxbQeXqkwGsh74stkkEOcBqGUjZ4-EdxpWoax1t1CmsK-sJ1y719r18NEqHY-JkG3Bz1NXNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e003523.mp4?token=Jq2f2I_2DNfFPnxIrO2BnKqx2uv6_X-CBRw2Rvy3I6qzmNxdkl6R2kj3FrJH4blU546dqVA-PhISNqLPtIgs4o5vBiE-VaMLGaC85AOVBWjnKmFIOdRAqDFLtoWcfJH4liIXyCHCZBSAaELFEP3-PqafuRQ8gsABQ9vcOzKPQE96zzBez7yz-5FqY9VKyFlzs6qvPBXJgU5HCzr_pgeQE8T7bL-8aSzg3PfCX1EFMd2sumUECu-xbVBiAsyeEcEPMBoY0kBFky0btJxA0aTMJPAlJy6gJYs0ayxvWrniQaS61p7EIbVHF7onFwPd6ojsQzdEEFLqjjWknpc27OZgOAQw_vJSxYqdrqiL0N031vk8ly11L4eamIaOoVgrD7TBzhLDIBhIx3TnTl3FEr6mRqMT2xdkJnEBH0p9TuD5-h8EDS-CDBDZzFNVSPaoU47atVpei3vSmh1QtJjEPUBdUsPPqFFVgKWcSyjrPCw20tjM3YgKOJNqkQJ7JWun6B5QyMj6cn7CvyGsdsx5bbnHnuiv7Aa91ge_dUjlnUTjpmSM8ocOGHZXBt2r1PeriDRja2aU9KPeFBK9n4OHezAwNlxgFTRk4tEajyYbxbQeXqkwGsh74stkkEOcBqGUjZ4-EdxpWoax1t1CmsK-sJ1y719r18NEqHY-JkG3Bz1NXNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکست فراخوان اعتصاب ۲۵ شهریور گروهک‌‌های تجزیه‌طلب
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/462658" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712ade6ecc.mp4?token=hnzZudYjgmzOHwDWH1ctjfX_CMfW0pXtLeFow73rkbmG5Pabs06bAJYf0wilGbGtpLVdQlc4LvCvk-_qlCBF0ugx0nIdimtqWFENVJ7xME4b_aEG3WUH9UblMx6IHD2CLs08LwF2yNFqIgBQgCLgPKdoU-LlwnorGisqERXgucyDZQkm5GJAe463sBdb5R-Z3kHk6baJLRAwC0nVd6kyegvchtQVcACJwaMLo5QVouAszQqzv-HcusNoJF5z-6XGsMMjPxp70Z9356aZBucGd45eAV3CIGVqnPgb4m6YzrE5nzC-WE4H_aU7jUHPQg8N-EZmRoL1tFwYF5ToneEkkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712ade6ecc.mp4?token=hnzZudYjgmzOHwDWH1ctjfX_CMfW0pXtLeFow73rkbmG5Pabs06bAJYf0wilGbGtpLVdQlc4LvCvk-_qlCBF0ugx0nIdimtqWFENVJ7xME4b_aEG3WUH9UblMx6IHD2CLs08LwF2yNFqIgBQgCLgPKdoU-LlwnorGisqERXgucyDZQkm5GJAe463sBdb5R-Z3kHk6baJLRAwC0nVd6kyegvchtQVcACJwaMLo5QVouAszQqzv-HcusNoJF5z-6XGsMMjPxp70Z9356aZBucGd45eAV3CIGVqnPgb4m6YzrE5nzC-WE4H_aU7jUHPQg8N-EZmRoL1tFwYF5ToneEkkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: همهٔ مدیران در تمام سطوح نیازمند آموزش هستند
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462657" target="_blank">📅 19:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec22c401e5.mp4?token=PyvytpfkydbLkkObhDcIC1DTWiPKEEIV_kclKjw6jYO3k9IwFPG9AbfCGIZ86TpWrPiqQWPCq45Ir2BxTfe0byQFQXR6YtfsZIlpUVp_S7p8VMUFuJkyaTIU0k7OWz7jrMMun-KPF3yIiQzJFATvD4nnnbXoy9ABWOJcZrnCT_8gX0_90b2l_aYTuqsiluYHbk4mNUJsbQX6qOCCYkFTOFDIEUzsldy5_1zP_96ZMEaDAvD_Lu4AviweXEN0au1d9i5JiFoWn8xLXcOjxIqOdf9CA7Cq2b3tE05tAv9_Y_3t7ZqfQG-wfGJl9EGjWnbORGZ77NOj9xHUngZrW2yR4IMpVtcyKvUsY-INwt-D_mk814_CAoYVlFvacUx2SNRECD89frp0x4mvC44m6zQkpkDDo0tLQh-F2NtLeb5zNi-QrTxA2wMvdeTkb_-Z4KGzW5c9CpQjCzOzag5h0OEhpOUuLSc6C85F0G1fEoGyK19YqUURpR2qT2KW-mRpo3fKy5cQvwmDqqc1XradAuO_tg4Kr_p0Z0tdqCWIHyH1Km8h6GoFSQ8VXYWpV_lbRyMX2GXvxV4NjuJ3tiBjKu0zg1IC5H3Lc1llCKaSqGSPIGnXZH-CeQz7HPS3I9pEFeuMX_wQYamb1Gom8KeZXJf6pIQisVRmOPa3gP3bLZd6jls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec22c401e5.mp4?token=PyvytpfkydbLkkObhDcIC1DTWiPKEEIV_kclKjw6jYO3k9IwFPG9AbfCGIZ86TpWrPiqQWPCq45Ir2BxTfe0byQFQXR6YtfsZIlpUVp_S7p8VMUFuJkyaTIU0k7OWz7jrMMun-KPF3yIiQzJFATvD4nnnbXoy9ABWOJcZrnCT_8gX0_90b2l_aYTuqsiluYHbk4mNUJsbQX6qOCCYkFTOFDIEUzsldy5_1zP_96ZMEaDAvD_Lu4AviweXEN0au1d9i5JiFoWn8xLXcOjxIqOdf9CA7Cq2b3tE05tAv9_Y_3t7ZqfQG-wfGJl9EGjWnbORGZ77NOj9xHUngZrW2yR4IMpVtcyKvUsY-INwt-D_mk814_CAoYVlFvacUx2SNRECD89frp0x4mvC44m6zQkpkDDo0tLQh-F2NtLeb5zNi-QrTxA2wMvdeTkb_-Z4KGzW5c9CpQjCzOzag5h0OEhpOUuLSc6C85F0G1fEoGyK19YqUURpR2qT2KW-mRpo3fKy5cQvwmDqqc1XradAuO_tg4Kr_p0Z0tdqCWIHyH1Km8h6GoFSQ8VXYWpV_lbRyMX2GXvxV4NjuJ3tiBjKu0zg1IC5H3Lc1llCKaSqGSPIGnXZH-CeQz7HPS3I9pEFeuMX_wQYamb1Gom8KeZXJf6pIQisVRmOPa3gP3bLZd6jls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژهٔ خودرویی رزمایش جان‌فدا در اسلامشهر تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/462656" target="_blank">📅 19:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcabdbd1b2.mp4?token=ig7LGiRorypyT29ww4W6fXhOrzxAeGZnuhF6JfpKrG9mB8c0Lq-7HLpPmMT9Lg1ABy50TrkrlGrfiyYy62axBDVB__eKjk2VOBReoIC_7fNkhYtT6rjwaun4YNjH7KOCp_NDhZwFVx7ctYFL8eorF8ZSCqqPmdJgM-IaZXYoeFNZfcgiD2V9kYtjuIX89grHh7R9xAEcLkF8h39E6wx9Bxm2xMXvRbsY_IQi_xuOsS2QKojompLUCWzgdD5fdNtZz2VMfvmRMTIbSOmiY2kJPP0-7yswhHG7iEXtVTbTSlhY5pgZkuWASIWIEV22HhO09b3LrhYo68KPNJQMrNQDfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcabdbd1b2.mp4?token=ig7LGiRorypyT29ww4W6fXhOrzxAeGZnuhF6JfpKrG9mB8c0Lq-7HLpPmMT9Lg1ABy50TrkrlGrfiyYy62axBDVB__eKjk2VOBReoIC_7fNkhYtT6rjwaun4YNjH7KOCp_NDhZwFVx7ctYFL8eorF8ZSCqqPmdJgM-IaZXYoeFNZfcgiD2V9kYtjuIX89grHh7R9xAEcLkF8h39E6wx9Bxm2xMXvRbsY_IQi_xuOsS2QKojompLUCWzgdD5fdNtZz2VMfvmRMTIbSOmiY2kJPP0-7yswhHG7iEXtVTbTSlhY5pgZkuWASIWIEV22HhO09b3LrhYo68KPNJQMrNQDfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس ترافیک شهری راهور فراجا: نظارت کامل بر ایمنی سرویس مدارس با سامانهٔ سپند انجام می شود  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462655" target="_blank">📅 19:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26a97aedf0.mp4?token=pZZoF4VGYQAMwM7iymqQPio3KKZcpklLPdMgsg2sJkKff9HuRwgvrnjHsSovT-8vH13fJX5Qw55NCRjUURs1-uGHhuNp_D7A_nxd6P_lTRfX-80ud8vrFyAei2Do6vhAHUjK_EAPPGdm5qJgLcATqGA1WFu8Oq59vpvl1EwRlFjZAudgJhVXMnqzHF4GOG1_aYdl1qaX5dNKu_YyaMmsNstlOtcOdFQXg1qt1BUopLwWfj-BkMgbYZYvk5SCvgStJIO-x9kLhNanOlKqLMgeARpZ_GNRQnLyXFuNYsPk1B1OU4GzGleIHyPZ2HAxxSJK5U7ZEDOy-CKdTtvh7OpQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26a97aedf0.mp4?token=pZZoF4VGYQAMwM7iymqQPio3KKZcpklLPdMgsg2sJkKff9HuRwgvrnjHsSovT-8vH13fJX5Qw55NCRjUURs1-uGHhuNp_D7A_nxd6P_lTRfX-80ud8vrFyAei2Do6vhAHUjK_EAPPGdm5qJgLcATqGA1WFu8Oq59vpvl1EwRlFjZAudgJhVXMnqzHF4GOG1_aYdl1qaX5dNKu_YyaMmsNstlOtcOdFQXg1qt1BUopLwWfj-BkMgbYZYvk5SCvgStJIO-x9kLhNanOlKqLMgeARpZ_GNRQnLyXFuNYsPk1B1OU4GzGleIHyPZ2HAxxSJK5U7ZEDOy-CKdTtvh7OpQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس
پلیس ترافیک شهری راهور فراجا: نظارت کامل بر ایمنی سرویس مدارس با سامانهٔ سپند انجام می شود
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/462654" target="_blank">📅 19:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edf6697b5.mp4?token=NU1gfLYsdQYnbDWBrY2BxJe719Rqs3DPoTEJkgeD-G-9zeIkTPkmyYmvsspOS8SzYTgFgsmASv8R6NWdldF3fZOJpCCtuGbyZ4aKQ3ZVpG3uqstGxa7YzfMN2cXztlpsR8hyLF9y2qTK_BauvxD6e5Cq3_dRBI0pwQeEIdm8lN9CGpOfXfmhe8IE9vAuCR9z11d-yhvoTUfl3pwah0T5GXvhywoBnJUupOWxT-Fe97GT66GkU6UsigD941vG5BV0Tmt99JN3ch1Ja9_qoDpEfF4rtFwMcAm3VB79fSXN7I_dlPDJBNV-3a3W4NRcgwqGSCDwgp56KT8OTHFo3WQszDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edf6697b5.mp4?token=NU1gfLYsdQYnbDWBrY2BxJe719Rqs3DPoTEJkgeD-G-9zeIkTPkmyYmvsspOS8SzYTgFgsmASv8R6NWdldF3fZOJpCCtuGbyZ4aKQ3ZVpG3uqstGxa7YzfMN2cXztlpsR8hyLF9y2qTK_BauvxD6e5Cq3_dRBI0pwQeEIdm8lN9CGpOfXfmhe8IE9vAuCR9z11d-yhvoTUfl3pwah0T5GXvhywoBnJUupOWxT-Fe97GT66GkU6UsigD941vG5BV0Tmt99JN3ch1Ja9_qoDpEfF4rtFwMcAm3VB79fSXN7I_dlPDJBNV-3a3W4NRcgwqGSCDwgp56KT8OTHFo3WQszDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ وزارت اطلاعات: خود را متعهد می‌دانیم تا برای شناسایی و برخورد قانونی با عوامل، آمران و پشتیبانان ترور مولوی «شهید گرگیچ» از پای ننشینیم.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462653" target="_blank">📅 19:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4729cd84.mp4?token=ApyAhU76o-46_oRuSDAgvOJt11eK9BHOteTwRPMzl9N9bQyfCOa5j_I-q_DI_YmJjQIpANHGLCfbHlrkHBBcyStnS0H1CwXLAU8aXiKUFQE_5OBPz-x_ApuBqTb8mgsAjlxkTJt0SDJ1vU4dkFWUeHtRGMN0ew9SB3nEC1KPGqhTFrJzkdbN-D86dLgZEtXULab2N4Yqy18GokK7w-Yov32ZoaRRRs2R0C7uWZqfQF2GuFHIXi6D_VVUakBgyWOzqBMQsgLQq1aNnPPx0HUIwzkLwvEm8BOV98m2jNATxZJOjzuKelwsZMbCEIyL6D0blHj8Lyg6g5mB4_qwGkmNhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4729cd84.mp4?token=ApyAhU76o-46_oRuSDAgvOJt11eK9BHOteTwRPMzl9N9bQyfCOa5j_I-q_DI_YmJjQIpANHGLCfbHlrkHBBcyStnS0H1CwXLAU8aXiKUFQE_5OBPz-x_ApuBqTb8mgsAjlxkTJt0SDJ1vU4dkFWUeHtRGMN0ew9SB3nEC1KPGqhTFrJzkdbN-D86dLgZEtXULab2N4Yqy18GokK7w-Yov32ZoaRRRs2R0C7uWZqfQF2GuFHIXi6D_VVUakBgyWOzqBMQsgLQq1aNnPPx0HUIwzkLwvEm8BOV98m2jNATxZJOjzuKelwsZMbCEIyL6D0blHj8Lyg6g5mB4_qwGkmNhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ ماموران خاطی برخورد ناپسند با فرد تبریزی در بازداشت هستند
🔹
سازمان قضایی نیرو‌های مسلح اعلام کرد که ماموران خاطی برخورد ناپسند با فرد تبریزی در بازداشت هستند.
🔹
تحقیقات قضایی در مورد این موضوع ادامه دارد و دستگاه قضایی وفق قانون با خاطیان برخورد بدون مماشات…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462652" target="_blank">📅 18:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سردار حسن‌زاده: ایران در آستانهٔ یکی از بزرگ‌ترین رزمایش‌های مردمی است
🔹
فرمانده سپاه محمد رسول‌الله(ص) تهران: اکنون نسبت به پیش از جنگ ۱۲روزه و جنگ رمضان آماده‌تر است و ارتقای توان موشکی، پهپادی و پدافندی همچنان ادامه دارد.
🔹
پس از ثبت‌نام داوطلبان پویش جان‌فدا،…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462651" target="_blank">📅 18:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شکست قطعنامهٔ ضدایرانی با وتوی چین و روسیه
🔹
الجزیره: روسیه و چین در شورای امنیت از حق وتو علیه پیش‌نویس قطعنامه پیشنهادی آمریکا برای تمدید مأموریت هیئت کارشناسان کمیته تحریم‌های ایران استفاده کردند.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462650" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رهبر انصارالله یمن: بیش از ۲ هزار مسجد یمن زیر حملات سعودی‌ها قرار گرفت
🔹
الحوثی: متجاوز سعودی هزاران زن را کشت و غیرنظامیان را در خانه‌هایشان هدف قرار داد و شهرها، محله‌ها و بازارها را بمباران کرد.
🔹
سعودی‌ها بیش از ۲ هزار مسجد در کشور ما را هدف قرار داد…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462649" target="_blank">📅 18:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عاملان رفتار نامتعارف با متهم در تبریز تنبیه انضباطی شدند
🔹
فرمانده انتظامی آذربایجان‌شرقی: ویدیوی منتشرشده از رفتار غیرمتعارف با یک متهم مربوط به ۱۴ خرداد ۱۴۰۵ است که پس از دستگیری فرد مذکور در جریان یک نزاع خیابانی رخ داده است.
🔹
مأموران دخیل در همان زمان،…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462648" target="_blank">📅 18:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdTQfu2hMZEmM3cTS3i3QgiKT3j4Tyw-7HeYsB_Y6tfFAuAlDZS77gcGnOjWDm_hoDf9-2OAZ4oyEMSBsY3ohHJgu4WLXORiDN8YxAvMRKGim0AE5TEBnLERp0wNSwkcHeM8ACIMGNAvK6Byf2SBX0OuyIY53S_7azIG89obLsdojvI6UHmmopLwyZum7010JpmGYb4WMfVxooJTutIVcTkfcJLyxkZoiX9VVaddPNIjfSlZhPOCFRECd7ahBrTFkaVjwRESdhhhKpWGsjGwtYGLAbC54eOFxaGxng4JGrfxixcydz_oUff7oi2h2YqzeDsnJXKKFY44IBV6SNGZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت دفاع:  ۲۰۰ شب حضور حماسی مردم، جهش قدرت اجتماعی در تکمیل قدرت نظامی و ملی بود
🔹
سردار طلایی‌نیک: تجربه دفاع مقدس نشان داد قدرت ملی صرفاً در تجهیزات و توانمندی‌های نظامی خلاصه نمی‌شود.
🔹
هنگامی که توان نظامی با اراده، حضور و پشتیبانی مردم همراه می‌شود، ظرفیت و قدرت کشور در مواجهه با تهدیدات افزایش می‌یابد.
🔹
مردم ایران در سخت‌ترین شرایط، با حضور و پشتیبانی خود نقش تعیین‌کننده‌ای در تقویت بنیه دفاعی و امنیت ملی دارند و این سرمایه اجتماعی باید همواره حفظ و تقویت شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/462647" target="_blank">📅 18:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آب‌شیرین‌کن چابهار پس از ۴۵ روز وقفه دوباره وارد مدار اجرا شد
🔹
استاندار سیستان‌وبلوچستان: این طرح در فاز اول با ظرفیت تولید روزانه ۲۰۰ هزار مترمکعب آب در حال اجراست و هم‌اکنون بیش از ۱۱۰ نفر در کارگاه آن فعالیت دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/462646" target="_blank">📅 17:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TADafW6sFGLKuKJ_IVQxOdnjb7hx67DX0P75ljow0gkMqAqfyZrNo-oLC1q9ByLt8iPd5uGtcVVJB6--mDODw1bS6ZMyAc_yNUtq8cyH0KK0KN2Ed2_sp-ecnR5BMKjXBaUVCzUmNhcmEJ_K7BwE9DEpcCmncjd0lQThvA7Q3VIM7r1DeEPQ7DYaEDxAnOgZhvwVahkYbF30fOWsA7_BCw90MFwUYqBAIFehhwc9CxsbDWd8W-KUXuQ5kOoum4qrw5KX9ms8qbB4HT3ifxOX7cn7h3BMuY2QlOAzATzRbZQM26sRJ4uXUoksZbQCcL5cL4ahhJW-1PX_W9OpNixquQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: عربستان آغازگر همه مراحل تجاوز به یمن بوده است
🔹
رهبر انصارالله: در مرحله کاهش تنش، عربستان به‌طور جدی به سمت صلح حرکت نکرد، بلکه از این فرصت برای تشدید اقدامات خود و تشکیل نیروهای نظامی تکفیری استفاده کرد.
🔹
تشدید تنش اخیر با بمباران فرودگاه…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462645" target="_blank">📅 17:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12f782a05.mp4?token=AzOV1U7T9rAcsWhzN1MIw6l3F7mBjmFktEhJEy6KjHesXtJmg2TCcfkiNFaICQkBVVckUo_opy2hVbrPkm4gdvCEvIxJpyDBGOD-Tz7IFzLfbdzcX42lW79cAmgymiPqY-xZJQ2IW1YQW5zSRhw_NR5_f3EfUqe59nuAj8zNzppR9qKxHngCABNB4ABrUUjsXlIx3L0anQNDWjUgxWEzxYRdwNRg0LANQGx92S3z42ZVzeAGk5wQ5UK-V0uwWah5YpvpHikszZ_sQHEF4LdYPlcE-MzkKHXG7ftKaP32XFfJticV4kKyzCbZcLLqf5F51gOw1JlGj8LuQSkwIQWEzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12f782a05.mp4?token=AzOV1U7T9rAcsWhzN1MIw6l3F7mBjmFktEhJEy6KjHesXtJmg2TCcfkiNFaICQkBVVckUo_opy2hVbrPkm4gdvCEvIxJpyDBGOD-Tz7IFzLfbdzcX42lW79cAmgymiPqY-xZJQ2IW1YQW5zSRhw_NR5_f3EfUqe59nuAj8zNzppR9qKxHngCABNB4ABrUUjsXlIx3L0anQNDWjUgxWEzxYRdwNRg0LANQGx92S3z42ZVzeAGk5wQ5UK-V0uwWah5YpvpHikszZ_sQHEF4LdYPlcE-MzkKHXG7ftKaP32XFfJticV4kKyzCbZcLLqf5F51gOw1JlGj8LuQSkwIQWEzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌نشان سبزواری برای نجات دختر ۸ ساله به عمق چاه زد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/462644" target="_blank">📅 17:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3bjgTt_L6jmogi5PZ2UFDHqeRRn7cYCVvFdVPpB7vaZRkmJBhW8gEybVWg7Dm_1uqIOZZ4MyhN7oq1M6lxsrp86BlJLH1QkClJISxTjNKb-xmT7ysvDxEtc89rNsDS1pKCiYofXlQMQmHBj7S2z2aLyA601AO4Tcere04yKrMFxZInyEQjoazZZvmNybNILE3MMddJNVNJ6zMS0HPrmPYLgBU_XpvoFWVSj5_2CdFvKq8Ci7eYMsLTd1_627yICqglS-jZHdTcPqR4P89CtlVlhqpspAmSmLG8VzAS6eWGTGyffzZp17rC-ClikW6XkEvXf5XGD-niT25i2zSxC2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انصارالله یمن: عربستان آغازگر همه مراحل تجاوز به یمن بوده است
🔹
رهبر انصارالله: در مرحله کاهش تنش، عربستان به‌طور جدی به سمت صلح حرکت نکرد، بلکه از این فرصت برای تشدید اقدامات خود و تشکیل نیروهای نظامی تکفیری استفاده کرد.
🔹
تشدید تنش اخیر با بمباران فرودگاه صنعا توسط عربستان آغاز شد و عربستان در همه مراحل آغازگر تجاوز بوده است.
🔹
در ۱۲ سال گذشته، با مقایسه نیروهای مسلح یمن و طرف مقابل، مشخص می‌شود چه کسی به اصول اخلاقی و دینی پایبند بوده است.
🔹
عربستان در تجاوز خود همه چیز را در یمن هدف قرار داده و هیچ حرمتی را رعایت نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/462643" target="_blank">📅 17:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🖼
پیام سازمان بسیج مستضعفین به مناسبت ۲۰۰ شب حضور مردم مبعوث در میدان و خیابان
🔹
۲۰۰ شب از آغاز حرکت عظیم و بی‌نظیر مردم مبعو‌ث‌شده ایرانِ عزیز در میادین و خیابان‌های سراسر کشور گذشت؛ حرکتی که از نخستین شب جنگ تحمیلی رمضان آغاز شد و امروز با گذر از دویستمین شب، به یکی از ماندگارترین جلوه‌های بصیرت، ولایت‌مداری و وطن‌دوستی تاریخ کشورمان تبدیل شده است.
🔹
مردم آگاه ایران مبعوث شده در نزدیک به هفت ماه گذشته، با حضور مخلصانه خود در همه شهرها، پشتوانه مستحکم نظام مقدس جمهوری اسلامی، امام سید مجتبی خامنه ای، نیروهای مسلح و مسئولان و مقامات کشور بوده‌اند.
🔹
در ماه‌های گذشته، این میدان و خیابان بود که به مسئولان و مدافعان امنیت کشور قوت قلب بخشید و دشمنان را در رسیدن به اهداف شومشان ناکام گذاشت.
🔹
وحدت، انسجام و همدلی امروز شکل‌گرفته در کشور، مرهون همین حضور خودجوش و پرشور مردم در صحنه است.
🔹
این حضور، نه با فرمان و بخشنامه، بلکه از عمق ایمان، بصیرت و عشق به انقلاب و رهبری برخاسته و همین ویژگی، آن را از هر حرکت نمایشی و فرمایشی متمایز می‌سازد.
🔹
سازمان بسیج مستضعفین از یکایک این مردم که چه در ساختار بسیج سازماندهی شده‌اند و چه دارای تفکر بسیجی بوده  و بدون ثبت سابقه ای که نماد هر ایرانی یک بسیجی است، با وجود همه سختی‌ها و مشغله‌های زندگی، صحنه را خالی نکرده‌اند، صمیمانه قدردانی می‌کند. بی‌شک این حضور، ذخیره‌ای ارزشمند برای نظام و انقلاب است.
🔹
و سخن آخر اینکه این مردم مؤمن و انقلابی، تا هر زمان که نیاز باشد و مصلحت نظام ایجاب کند، همچنان در خیابان‌ها و میادین خواهند ماند تا هم خاری بر چشم دشمن باشند و هم از آرمان‌های انقلاب، ولایت و امنیت کشورشان دفاع کنند.
🔹
۲۰۰ شب گذشت و این راه، به حول و قوه الهی، تا تحقق کامل اهداف انقلاب ادامه خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/462642" target="_blank">📅 17:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmjOLU3g-qMADBpsCi8BV4lzU-RjRxYjZflty_piPyreJFoyKVlbM4rYPJj5QHsY9lAgK4XXZfhMeu1d-I2j5aPgUgTeCPThgS3eoeJX6XdX0vysEOPqcnF2U_I1FsAaodDf1x4F2gQeZnQOXrOfNPlwqmuV6Ha_az9dx7uaGL2oMg-fCqvbFzdiKRxeMgr9tqzkyXLhm1n8dBdFetEH8O0F2uRZhr-BlNxkESCZoxr7BbUOCsDXIV6Uajy0TvCCghQKbHMIpkfPCeb5SlVy5mIFMu-e8VoWOwrbJgxPBjUodR7AjakdccfENcT3r3r130Zd-8_3vMuHT-T7_G59GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوغان در انتخابات زودهنگام ۲۰۲۸ نامزد می‌شود
🔹
مشاور ارشد اردوغان اعلام کرد که رئیس‌جمهور ترکیه در صورت برگزاری انتخابات زودهنگام در آوریل ۲۰۲۸، بار دیگر برای ریاست‌جمهوری نامزد خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/462641" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp3Jve188Bf4nNkEvILDgiz3iO_ecmtCUintbAhq4ivrph4oAFi_7lPKyLXKPgr7CHl_2RxC7cjqfrPR8WhPefatthK0GKn5CS0z_f6ELnXN1utaPiOzIyX5visW4JBqi8cuPMX2MOh3ZfPDnkvGOApp8U35G_cLf8iq-6p20m7mPDAJdvjFHzj0S3M_PfG-ncuUdJl8IMnzeYwnwEPnf6rYYeITqkzloJwTYzMCXMgP22Qw_vjI7FaI_85Z-ebjScmeQQLs7_YrhT4pwLTuXxNHoznHUmrx0ippVchzgm-vVqQm5e-N47_V-Z2-fGVMs_0301WkSnlSKcQl_FBFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش جدید ترامپ برای پولدار شدن
🔹
در جدیدترین بررسی نشریهٔ فوربس، ترامپ از آغاز ریاست‌جمهوری خود در سال ۲۰۲۴ تاکنون حدود ۲.۷ میلیارد دلار به ثروت خود اضافه کرده است.
🔹
این درحالی است که تا پیش از سال ۲۰۲۴، ثروت ترامپ در مجموع دوران زندگی‌اش(۷۸سال) فقط حدود ۴.۳ میلیارد دلار برآورد شده بود.
🔹
اما در ۲ سال ریاست‌جمهوری، این افزایش ثروت به فعالیت‌های مرتبط با ارزهای دیجیتال، دارایی‌های نقدی، باشگاه‌ها و املاک گلف و همچنین کسب‌وکارهای مرتبط با برند ترامپ نسبت داده شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/462640" target="_blank">📅 17:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234f267ed1.mp4?token=vZe9h_vbsbMkHqh1dHKdIqQ1TZhDMO6JeZDOzlOfMSroA1tpqlvmy1Hsh9KgNW6wP3Qbokz46KBlJM08L1qtqlT9HPxJy2w2JtdXV1Fx0Lm-4QPTuVI6zs_MsTGwjycJjidGsght1ITW3W_dcFohDIbNOiFUD4O-0waiw6yLOoAt_VhrbVRuvd9A8iMI1kiACbuW6CQI_aXG5H4zyY6RKHGdURF4bpQEzubulLpUOV2wI1naygu6sXpjVNpwe0Hq08ssPbvkrdehDPDl8tdPkXVNNLmOkqCtj39zNzMVn9YqPPf1fMjrypPUrGgMeEKuISdaEq4FDqp9rjYXmlzYXlo_zd7xdYqKONjIaC1iLtgF4X8rfxyp-cPnB5pjwy7k3sHASBZSI9VY3394Sx5HFvn_zLO8np9d4vtEcBhR8vo6hfAUU_LNxL_ZUwDiofpdkMCPP9A6Emem7Dls63BFPW6ED-8j1wDZzwoSeSyTjRSs9qIc05CQroIsRvqcGm3cWlQbqE7ykOc4vUCmPTfmnAlHdmhAsTfFPnD0bs52QCUzUgqcnEqrLKpeT82SEDk-G7sdTLWbzwG3gmKBrtvmyR-VyCMbcBWdz-ZVC1DgDPJLGks8GIMhc1AA49-gbXP9pjF_SwhHqDBB3Xs5TfWLZtd4wGnB7YOLV_Fun6mVWV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234f267ed1.mp4?token=vZe9h_vbsbMkHqh1dHKdIqQ1TZhDMO6JeZDOzlOfMSroA1tpqlvmy1Hsh9KgNW6wP3Qbokz46KBlJM08L1qtqlT9HPxJy2w2JtdXV1Fx0Lm-4QPTuVI6zs_MsTGwjycJjidGsght1ITW3W_dcFohDIbNOiFUD4O-0waiw6yLOoAt_VhrbVRuvd9A8iMI1kiACbuW6CQI_aXG5H4zyY6RKHGdURF4bpQEzubulLpUOV2wI1naygu6sXpjVNpwe0Hq08ssPbvkrdehDPDl8tdPkXVNNLmOkqCtj39zNzMVn9YqPPf1fMjrypPUrGgMeEKuISdaEq4FDqp9rjYXmlzYXlo_zd7xdYqKONjIaC1iLtgF4X8rfxyp-cPnB5pjwy7k3sHASBZSI9VY3394Sx5HFvn_zLO8np9d4vtEcBhR8vo6hfAUU_LNxL_ZUwDiofpdkMCPP9A6Emem7Dls63BFPW6ED-8j1wDZzwoSeSyTjRSs9qIc05CQroIsRvqcGm3cWlQbqE7ykOc4vUCmPTfmnAlHdmhAsTfFPnD0bs52QCUzUgqcnEqrLKpeT82SEDk-G7sdTLWbzwG3gmKBrtvmyR-VyCMbcBWdz-ZVC1DgDPJLGks8GIMhc1AA49-gbXP9pjF_SwhHqDBB3Xs5TfWLZtd4wGnB7YOLV_Fun6mVWV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفر عراقچی به چین و راهبرد‌هایی برای توسعهٔ روابط واقع‌بینانه
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/462639" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شهادت ۳ کودک یمنی در حملات مزدوران سعودی به «تعز»
🔹
منابع یمنی گفتند در حملات توپخانه‌ای عناصر وابسته به عربستان به روستای «الطریره»، ۳ کودک شهید و چند نفر دیگر زخمی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462638" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چرا شتاب‌زدگی در مذاکرات می‌تواند هزینه‌ساز شود؟
🔹
تحولات اخیر در دریای سرخ، باب‌المندب و تنگه هرمز، از نگاه برخی کارشناسان ظرفیت‌های تازه‌ای برای اثرگذاری بر معادلات امنیتی، اقتصادی و سیاسی منطقه ایجاد کرده است؛ به‌ویژه آنکه این گذرگاه‌ها با مسیرهای اصلی تجارت و انرژی جهان ارتباط دارند.
🔹
تحلیلگران معتقدند اهمیت موقعیت جدید یمن در کنار جایگاه تنگهٔ هرمز، صرفاً به میدان نظامی محدود نمی‌شود و می‌تواند بر بازار انرژی، کشتیرانی و محاسبات قدرت‌های فرامنطقه‌ای اثر بگذارد.
🔹
در همین چارچوب، کارشناسان معتقدند دیپلماسی باید به‌گونه‌ای پیش برود که اهرم‌های ایجادشده در میدان، پیش از دستیابی به توافق از دست نرود.
🖼
اما این اهرم‌ها دقیقاً چه هستند و چرا برخی کارشناسان نسبت به مذاکره شتاب‌زده هشدار می‌دهند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/462637" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4b87a7e.mp4?token=qYdjUfjPNBFH5Bf2DnBhqfTzgyYpa5QRqH_lu-uQMoVtig5-KxmY2lYsk15XnfFWyXBY6qXc5B-a4uJkEJNGcbcBZBD1AbzQ5Et5hD7ErYlUexH9gUxPRawyGDhu0yvmBYAha2T8pe1_R5LK4PpdJNv1OPnj6PTW_ucXLR9ZY1B9P-nVTexsCVa1vrqdLv4VGxMppI30by1JEWGT5ZulYn37gAsov5U9mzhmPbVbhuXVLG7qeQ5_QvCoVScXvrOLErv040V5JmHo8zCE0UovT7px-nMqeUfwOTN8bN7sope8S9XBRBCnAcOMQPcDCVPD1H2euLVA3PnqbQMuuFxp-GGITjha0msEBrbqYhgtkZ5E5RSgmUlgkxo36b49ZC8APGjQ0g9ZElzVL4N2ZVS7qtrVG2u-tqgwrv2RHkSXCUBbcsdnlWuQLwc3SYoS2FFGAbmBK8puz_Gz5kG1KK6JAwM3T9HYA_OETI-vigJY2qiCAMcDKMSSWRj5hpyqxVSGvzw7hWOk9MfA7LvKXYkq5dcyrfTRICBgDi0y_WMfmB7Bq3F4OOLNS2eQatauX0AE8LpAjTTnQ6hFGyUoE8lW-riIkib77FAssvrh7clKtLkdss8P81-jZygx-tP5-mDY8TRO0nG5-hIs9WJ9ifRlQu02L51mgCdEi7O9CpuGRv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4b87a7e.mp4?token=qYdjUfjPNBFH5Bf2DnBhqfTzgyYpa5QRqH_lu-uQMoVtig5-KxmY2lYsk15XnfFWyXBY6qXc5B-a4uJkEJNGcbcBZBD1AbzQ5Et5hD7ErYlUexH9gUxPRawyGDhu0yvmBYAha2T8pe1_R5LK4PpdJNv1OPnj6PTW_ucXLR9ZY1B9P-nVTexsCVa1vrqdLv4VGxMppI30by1JEWGT5ZulYn37gAsov5U9mzhmPbVbhuXVLG7qeQ5_QvCoVScXvrOLErv040V5JmHo8zCE0UovT7px-nMqeUfwOTN8bN7sope8S9XBRBCnAcOMQPcDCVPD1H2euLVA3PnqbQMuuFxp-GGITjha0msEBrbqYhgtkZ5E5RSgmUlgkxo36b49ZC8APGjQ0g9ZElzVL4N2ZVS7qtrVG2u-tqgwrv2RHkSXCUBbcsdnlWuQLwc3SYoS2FFGAbmBK8puz_Gz5kG1KK6JAwM3T9HYA_OETI-vigJY2qiCAMcDKMSSWRj5hpyqxVSGvzw7hWOk9MfA7LvKXYkq5dcyrfTRICBgDi0y_WMfmB7Bq3F4OOLNS2eQatauX0AE8LpAjTTnQ6hFGyUoE8lW-riIkib77FAssvrh7clKtLkdss8P81-jZygx-tP5-mDY8TRO0nG5-hIs9WJ9ifRlQu02L51mgCdEi7O9CpuGRv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پویش ملی «برای پدر به عشق پسر»
🔹
در آستانهٔ میلاد امام حسن عسکری(ع) قدمی متفاوت برای نزدیک شدن به ظهور مهدی موعود(عج) و نمایش همدلی ملی برداریم.
🔸
با ارسال عدد ١۴ به سامانه پیامکی ۳۰۰۰۳۳۱۳
می‌توانید از جزئیات این پویش ملی بیشتر بدانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462636" target="_blank">📅 16:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ0HWZxxzKdlsCJlY8L1a61agZStgpl_1uQIlQIzSD7h1-aonawqd-lM7Kkum2A3NSDraton32GvPKmXvoZYq69TiY41JYaDeQe1VFeIGAe99g3aRFqTHAdq75bdMwHnotT8n39hrdFlryPq2fPozyzAZvNN3HusS1uVAhxhriE21i9LpYCsUAos3SkLyTx9ix-ZeTjd9z-99d-zP4jj-sZlVtIG9ORt5v5CsES1N6spdb77BWsa049EIpArICwFjlHPUAdBA82uIpViXM-jGrTz3E2xfi_rW_UCjDwm4QguJupkf1eQo_E-nIlmyY-eeCC0gSyIZS0TwhtfjbCt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ذوالقدر، مشاور سیاسی رهبر معظّم انقلاب: تا به زیر کشیدن ترامپ و نتانیاهو، تنگهٔ هرمز را نخواهیم گشود.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462635" target="_blank">📅 16:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU7i5Y1JiQONQO3OnBhxDJ57T0uZPp1d2o2fjAxA36s8oxABUhx4sY05UDQAXyKsJGujGGy_XK1aZxmkqMWhGqFZ5jkFreUofe1ENMhN2rcWk6EO52PkIUX4tqEM7YBfkyeoPU3-BWE3pQ0sxLpAnlaPg70h0y_X_kexLqaO4JbPU1m9fgOqCD3MGfHFg8_cB2UWl34mhq_eKPbZSRL_-WVenCGtqRYMnSTRwlLewJi4t2cqn0BP8z1bbsIdImoXQeq8QxRHHBumBu945SQRaxNNFyEZc1NGei7VhxXrb5RBvomonsCC7Gazmm4PyBKZOycUfcgXX-p3_Tr5qemDrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین صندوق دلاری ایران راه‌اندازی شد
🔗
دوست دارید بدانید که چطور می‌شود در این صندوق سرمایه‌گذاری کرد؟
اینجا
را بخونید
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462634" target="_blank">📅 16:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
سپاه: ساعت ۰۲.۲۹ بامداد امروز پنجاه‌ودومین پهپاد MQ-9 ارتش تروریستی امریکا با آتش سامانهٔ نوین پدافند پیشرفتهٔ هوافضای سپاه در آسمان جزیرهٔ قشم رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462633" target="_blank">📅 15:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TctPHpDFkRd77prSZbkVupF5qwcS_flyO2ipHZ-xH04sY-Cug1T-SMN_BuMiHsdQ3BSw0P5KuH6fZ6XJ6GalLKtxb-GwEVVPFQKSCjm-vzctuGj-fabGDIPSFjjuLU5XUH_i1r7RW5Xi81Qkgk-nUOIGod6mwDZIlr-hciXGPfeTM0SNFJj4ZWbYXpCQL4kzPunS3YE-KXubmgcER00lJZX15rdfXEthO7wZ10MiaNH9z6Z3RhY6M-ls9vPn9H9JciCqiZxs3Dp7BulzC-3CU8ogVL5SjJ3-1o4FBgITSp2s6ctD0OboVzYWiVWPa8x3Sxk7uk50n0kCRIMQGZTegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رژهٔ خودرویی رزمایش جان‌فدا در اسلامشهر تهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462632" target="_blank">📅 15:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هشدار سازمان هواپیمایی نسبت به گران‌فروشی بلیت ترکیه و عمان
🔹
سازمان هواپیمایی کشوری: توقف پروازهای ماهان به ترکیه و عمان، مجوزی برای افزایش قیمت بلیت نیست و با گران‌فروشی در پروازهای سیستمی و چارتری، اکونومی و بیزینس، برخورد می‌شود.
🔹
در صورت احراز تخلف، مجوز نمایندگی فروش یا سهمیه پرواز شرکت متخلف به مقصد ترکیه یا عمان به مدت ۳ ماه تعلیق یا لغو خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/462631" target="_blank">📅 15:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxD-NO5KZYkactKVHIkVjftqobs_6pXcT42yKZpmzAMHaQA_3zMJPixsa3wfYWn7rwI6fr_MgfQhYHzAHqmYri2LCjiWi5inKE4o1SjlnicQR5pT0UN_VM0bVl9LqEkVUt1pgVuGa0q7GhedvdgZR80SYLCaeU_L1atcjf3sxLsJTNJouCdbu604f_FaegvmSw8n4Bn2CY-P5aEglfLUctUmeNCR6tPVapCxxE77JOWwSoj0wo8Eg8-mCN_oBwFbjRxeTkL2gFdRIAm-2lksyqPhdmbGv745bo53EwLIh7mnA45OuaHV4pzhwv434intwZMKCKw5NgrQ5i1SKWUOKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«پرسپولیس ب» کنسل شد
⚽️
باشگاه پرسپولیس که قصد داشت با خرید سهم یکس از باشگاه‌های فرد البرز و بعثت کرمانشاه تیم دوم خود را در لیگ یک حاضر کند درنهایت موفق به خرید سهم باشگاهی در لیگ دسته اول نشد.
⚽️
به این ترتیب پروژه راه‌اندازی پرسپولیس ب در لیگ یک، دست‌کم…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/462630" target="_blank">📅 14:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKYJM63qbdk_GwKaGP5fyzVMyyu8TXjwTLcEn5b2aOcqUK3OLQ-e0yfYKY-5F4wGiuWhe86G-k9i0LnNVIvaNB0rxfQB0Aps-pnyIOkWeRjjN2TfbiVsucVbtUed9-ESjVbxN0YSQThronuOx_VDgjxzmEaA0PfwdGDm6i3deUffmIsLDjIokayVTxqxqDUQ76Wpavnu88bRWpCMozPifUL6qefUEIk9ymXWLfYg14BRhsi4Q6BY8iDfbl7ARgvivOdLz4HD6_pQwwg0FoTWesPuMgCgO4GH5PvuFm7WMazPC0h1Cws4TB7DGcMn9Xp7VuwXIePCenvxFL-AaXdz2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاملان رفتار نامتعارف با متهم در تبریز تنبیه انضباطی شدند
🔹
فرمانده انتظامی آذربایجان‌شرقی: ویدیوی منتشرشده از رفتار غیرمتعارف با یک متهم مربوط به ۱۴ خرداد ۱۴۰۵ است که پس از دستگیری فرد مذکور در جریان یک نزاع خیابانی رخ داده است.
🔹
مأموران دخیل در همان زمان، طبق مقررات انضباطی فراجا تنبیه و «انتظار خدمت» شدند و اقدامات تنبیهی تکمیلی برای برخورد شدیدتر با آنان در کمیسیون قضایی و انضباطی بازرسی کل فراجا درحال پیگیری است.
🔹
متهم سابقهٔ جرائمی از جمله قمه‌کشی، نزاع، مزاحمت خیابانی و توزیع موادمخدر داشته است.
🔹
این سوابق به هیچ عنوان رفتار نامتعارف و خارج از استانداردهای قانونی مأموران را توجیه نمی‌کند و هرگونه رفتار خارج از عرف و قانون بدون اغماض بررسی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/462629" target="_blank">📅 14:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/API44INy6sZg0SDkYN8Nka7-_J-vpYtX6s7Fi3kCnRlrtuTo5amhwcFJO-sdjVorFyzpR0jQCzgKvn6YjGGk2hkiQXIlvjWj5fmaZA7pgapk8TLgj7aYBfgeDJvpQ2jfxSf072n0mr87zLsCl1JJ_AmC991n2Vexsl0teooajl5Kq2fk-FFxac7hbhxpiPz9VxLyLA-G46AHoaK1mORoU6itITVq245jWQaBNq8P5jHGxG2yJlJMqm9J0j98y37gdV6THGmvC3HsazSLNwn7NxtTz-_ux-i0-TYNbpGSkmpjXOA2zhpc0FJe4tJHJsbqfTySCXSnYwU92I65bezhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر انرژی آمریکا هم مجبور به اعتراف شد: فرمان قیمت انرژی دست ایران است
🔹
کریس رایت، وزیر انرژی آمریکا که به دروغگویی‌های آشکار در خصوص تنگۀ هرمز مشهور شده، مجبور شد به نقش تعیین‌کنندۀ ایران در قیمت انرژی اعتراف کند.
🔸
او در پاسخ به این پرسش که «آیا جسارت…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/462628" target="_blank">📅 13:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سوئد کارمند سفارت ایران را اخراج کرد
🔹
سوئد در حمایت از رژیم صهیونیستی، یکی از کارمندان سفارت ایران در استکهلم را اخراج و سفیر ایران را به وزارت خارجۀ این کشور احضار کرد.
🔹
به‌تازگی وزیر دادگستری سوئد، بدون ارائه شواهدی، ایران را به انجام «رفتارهای خصمانه»…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/462627" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSHM4FvYi2Fo0hykC3z1zYpI2djdR5ROK3dVgeiBjBsHKHJYMqzBRjZY-6RFA68UKPVltInPlW4ww_ze3KLP9S-PfWCt575d7jfcDlvj0K7Z43JMDAqpU6GBm0vL-M5a4gbpgi5AbJdLdJQVaIw3sv6tmaCdgdjiu_mUNySdXD1O0VK9gGpQ5c7nFD4UkMmjOWHLKuAdi9N8UpZBUaFxbpuNDd3BhOVpUPIt9DPMQ5_uckxytTc8jSrMyl-RvLNSQdLGJdIM17v7IwVuV0rgq3JuRvcLr5NKAjHFJzICD9X16THerB2UawcKzURhyfHb_uwAcnfTmx_skk8uUYkSxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال نتیجۀ شکایت پرسپولیس را می‌داند
🔹
با وجود اضافه‌شدن شکایت‌ باشگاه‌های پرسپولیس و آلومینیوم به دلیل استفاده از یاسر آسانی، باشگاه استقلال همچنان قویاً معتقد است که این پرونده سرانجامی برای شاکیان نخواهد داشت.
🔹
طبق پیگیری‌ها از منابع مطلع، باشگاه استقلال…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/462626" target="_blank">📅 13:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd00601681.mp4?token=BMqw7sgHJTztuHBP7pas-iSHRup87dZQkKyi5uaLRgCsJMhEBYJFKGlBEtArtGZZPxd_C-Dz1IW2pkIYyMG4g-1kbPefBVb2gqS69YakGCQ3uQpmhLRdvutZdicBiCftNmfR5qX4OE6MQE61UeQHnBXtlSEck3WcOFTN_Ueq8CL9U__hPNgbwSKsIJZGIcFGWEfLehJC1geeGis_ZUEnfTBdQc9DJDcWGNKpzw4XX5kwfouxyxE6Av7foKoEyvTRbG9E_4Ol-ZqGzssVf67fwZEjbAW9GanywzcNk0JMG_hQWR8vGNOT9XtY0ePfG9Iy50B14U88LbFkMb4x0dZZfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd00601681.mp4?token=BMqw7sgHJTztuHBP7pas-iSHRup87dZQkKyi5uaLRgCsJMhEBYJFKGlBEtArtGZZPxd_C-Dz1IW2pkIYyMG4g-1kbPefBVb2gqS69YakGCQ3uQpmhLRdvutZdicBiCftNmfR5qX4OE6MQE61UeQHnBXtlSEck3WcOFTN_Ueq8CL9U__hPNgbwSKsIJZGIcFGWEfLehJC1geeGis_ZUEnfTBdQc9DJDcWGNKpzw4XX5kwfouxyxE6Av7foKoEyvTRbG9E_4Ol-ZqGzssVf67fwZEjbAW9GanywzcNk0JMG_hQWR8vGNOT9XtY0ePfG9Iy50B14U88LbFkMb4x0dZZfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور احتمالی فرانسه: ترامپ تصور قدرت ایران را نمی‌کرد
🔹
رهبر حزب «اجتماع ملی» فرانسه و بخت ریاست‌جمهوری این کشور مارین لوپن: بهتر است ایالات متحده را متقاعد کنیم که به جنگ با کشوری با تمدنی کهن نرود؛ کشوری که بسیار قدرتمندتر از آن چیزی است که دونالد ترامپ تصور می‌کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/462625" target="_blank">📅 13:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDZLYsz0IDVsRtPc0XCZwX_oOTR-9sRNCFP5qkwQnNSS95Nq-uUH0-Yo201UjBRt2EEw7PgYl274mrTemQbAy4I4sCStc-WLau9lnIpcUpt3KFFCTdSIq1CBB_Z5dNs1gt-6_PCi_QcIRC1539C1Q7pE9FxIRqHi0HXUS5ILrDGKvCe6a-oxFRYDgoIdFPaA-KNLrPkPfCMR82_LdCdhaYQQi_bhHhpf2DPQ9YEV4Gl8PVHhsPqvEB_nOH0RGPSahQJuVz7p7KdYKWwW0e1X98t1iQ7d_s-LVRqhE1pXxW5qi4iSe7xysXDAjcuhr0etDFsOjN9tmjTnF4f6udP2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کانادا را به آغوش اروپا فرستاد
🔹
کانادا درپی تشدید تنش‌ها با دولت ترامپ، درحال نزدیک‌شدن بیشتر به اروپا و آسیاست؛ روندی که با استقبال اروپا همراه شده و حتی پیشنهاد تبدیل اتاوا به نخستین «عضو وابسته» اتحادیه اروپا را به دنبال داشته است.
🔹
جنگ تعرفه‌ای، تهدیدهای ترامپ دربارۀ گرینلند و کانادا و نگرانی درباره اتکاپذیری تضمین‌های نظامی واشنگتن، متحدان سنتی آمریکا را به بازنگری در روابط خود و کاهش وابستگی به این کشور سوق داده است.
🖼
فکر می‌کنید فاصله‌گرفتن متحدان آمریکا چه پیامدهایی برای نفوذ جهانی واشنگتن خواهد داشت؟
🔗
پاسخ را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462624" target="_blank">📅 12:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AG0ZBGJPYdycRBqv2Zzzn9cTh8l3wuBf3EeQsbWzVAAt-mcKn5HE8U3EGR0alxabqmGyHZiTevDFCnF7KkDpLFvvNWZk376Fc9ymt7wYipfgWp_1jpY6lv0XikhX8CIL5VkE_2mPq8zTGeMwsgD2ysQLIZJISux2hnfh-Xb43uUsFMU7jidpEpwYjBWJDUJ2aQNbwkUaaH_IhHatRTTJm7gnJD6NTITHqQ8qZB3a5eCnwVy1Y6zSb_9XGrXsFLvVFFUOZ7wTi6sgvm3XLC6JzC1-x3hfV4_51abheHLKRnXPg_Mc0oHdHVaIoe1IPkk17PytImFz2bCmnmFrlfNaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهش تازه: زمین دیگر شکل سابقش را ندارد!
🔹
ساینس آلرت: پژوهش جدید نشان می‌دهد بخش سنگی زمین طی دو دهه اخیر در حال تغییر شکل است؛ مناطق قطبی با سرعت بیشتری بالا آمده‌اند و هم‌زمان اطراف خط استوا بیشتر فرونشست کرده است.
🔹
بررسی داده‌های ماهواره‌ای نشان می‌دهد سرعت بالا آمدن مناطق قطبی از حدود ۰.۵ میلی‌متر در سال به نزدیک ۱ میلی‌متر رسیده است.
🔹
ذوب یخ‌های قطبی باعث سبک‌شدن پوسته و بالا آمدن زمین در این مناطق می‌شود، درحالی‌که انتقال آب حاصل از ذوب یخ‌ها به اقیانوس‌ها، توزیع جرم روی زمین را تغییر می‌دهد.
🔹
دانشمندان می‌گویند برای درک دقیق تغییرات زمین باید هم‌زمان تغییرات سطح جامد و جابه‌جایی آب و جرم را بررسی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462623" target="_blank">📅 12:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEcpX1QC5A2tONux8L4s85H2xZ7lKgMZvJGbRbjRCcMkR7Ot52D44pSiDZ-JYu-FRY5yUTzrr1tM4gchPVLNGigSZDGGfM8BHR-Y8bZy5DXeUbmyTRXiz3D94R7oRvVg5OQUmTjtT20KPMse-GSzxeYUBfg4h-jB4L6Msak-zmtOEHP3J5ZxZrCYiaTOlMN-PqgmJSoyeyFusGKD06GMEcLnlig6edLF2C8OG44TCOP9n51mWbohapZecvNCFJHG4rBKGul0XqtEQOTqVqdzP_h3TdDtNmW4FOXXFFbbtlLJjGDrXvJRLeLkrJSl6GcvT9OAaZ9mZ18tj4meBtPxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان غذا و دارو: واکسن آنفلوآنزا هنوز توزیع نشده؛ واکسن چمدانی نخرید!
🔹
سازمان غذا و دارو اعلام کرد: واکسن‌های استاندارد آنفلوآنزا از مهرماه وارد کشور و توزیع می‌شود؛ با این حال، در حال حاضر برخی دلالان اقدام به توزیع واکسن‌های چمدانی در میان مردم می‌کنند…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462622" target="_blank">📅 12:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36a94145e0.mp4?token=t1pQMR1LYxP_FGGfylbsqB1NXGGc_2hxd1zohJff1vd6sbMPcDO7Th1ei7ugvERaZ2YJNUo1uyl1uBqLXqePo62-eL74D9aj2QMRb_BMBli7gkQAK-hQMp_s7Q0ByL_aYOj1WzQfArMFBOYpkZ2v1BwRBgO9GXTBw2UC4mXlADLVQOR7BcVNXNtaxFr_Kr9Q0rd0dzVAcdi9bZ_oQRWEap1kMjU3J8GHnYv_voKQtmW-ACDNq9v3vIZg6ZmQtK8Mz0p0DQC3szL6em1Ok_Hm8X8JEcMwLQsdj1KKvwKOa0Q_-4s1q_Ru0JC0zv-rXsCRD-WIgQ_CL6_7o0wxQJ9AQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36a94145e0.mp4?token=t1pQMR1LYxP_FGGfylbsqB1NXGGc_2hxd1zohJff1vd6sbMPcDO7Th1ei7ugvERaZ2YJNUo1uyl1uBqLXqePo62-eL74D9aj2QMRb_BMBli7gkQAK-hQMp_s7Q0ByL_aYOj1WzQfArMFBOYpkZ2v1BwRBgO9GXTBw2UC4mXlADLVQOR7BcVNXNtaxFr_Kr9Q0rd0dzVAcdi9bZ_oQRWEap1kMjU3J8GHnYv_voKQtmW-ACDNq9v3vIZg6ZmQtK8Mz0p0DQC3szL6em1Ok_Hm8X8JEcMwLQsdj1KKvwKOa0Q_-4s1q_Ru0JC0zv-rXsCRD-WIgQ_CL6_7o0wxQJ9AQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پلیس فتا: در سایت‌های خریدوفروش آنلاین پیش از دیدن کالا، بیعانه نپردازید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462621" target="_blank">📅 11:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDW3aIT-tGEifgrL0125B-MN0hsaEcsQUrTl1GNcg4A-gjwag6ThP4YzpIJ_bfQlwTFWOwCOWGGpGRA0Cy8kEaHLefwh7kSBxLuafnMdIdVq_gIpfGIE3S5GJ0b2DTbABDlJ6Te9zh8fZDRyn4cxCnJHm_otn-jOXIg_6bbnlngv8zHCkkGLNM4j52sc0qqgbELySqP0B3Fq7llFaQzsHzdyULGdmWY9AdHByY8Of93965swIeXEhD5EyjX2X4fnhLpf6x26nbDT7ddMXRScApGTpcWMRe_5PKiwHMsdUJn3hdHS0ZThct-pB4ZUcjlcftnQqgx4w-VO6XB7ltfl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خصوصی‌سازی: ثبت‌نام سهام عدالت نداریم
🔹
سازمان خصوصی‌سازی: در حال حاضر هیچ برنامه‌ای برای واگذاری سهام عدالت به جاماندگان یا افرادی که قبلاً به هر دلیل از سهام عدالت برخوردار نشده‌اند، وجود ندارد.
🔸
در روزهای گذشته تبلیغات و پیامک‌های جعلی با موضوع ثبت‌نام…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462620" target="_blank">📅 11:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دعوت از ۱۸ بازیکن لیگ به تیم ملی
🔹
حسین حسینی، پیام نیازمند، محمد نادری، احسان حاج صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آغاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
🔹
اسامی بازیکنان حاضر در لیگ‌های خارجی هم متعاقباً اعلام خواهد شد و بازیکنان حاضر در تیم امید هم در فیفادی بعدی دعوت خواهند شد.
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462619" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDVmDejc_NtnO_xpVDRXfdAhC9Zwp3W3CDIjriaouN9Uf8PaGTJbFxbq0k-bK_5bS5NAWZ7tkSkji9xw0Pmj33GiCY_A-8-ee4z6GcexeIwDCfdgy0Lhs_3n7Kbfc5JJnkcjA8cWx7nJs_HFUhkvFem8m3zUBQXjWDBmYMTyusJ2xKF9dnu05oyqM-DNGOoA_YZ96dzt4yc3KV9G3OxGsw-SCJC0y0IX1LHFtd9cpL167Rn2_9is8dkbiumgUNYut_eBH_TgQGzrA9hAbJtpJWXgxkX9EbzWbP5hGAUTgV7vnhH1CiAVposQ_AgfE7KQffAOPiywV0AMx7yXa_CqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا آیت‌الله سید مجتبی خامنه‌ای کلاس درس‌شان را تعطیل کردند؟
🔹
حجت‌الاسلام محمدجواد قاسمی: آیت‌الله سید مجتبی حسینی خامنه‌ای در سال ۱۴۰۳، در نخستین روز سال تحصیلی، تعطیلی جلسات درس خود را اعلام کردند؛ درست زمانی‌که جمعیت کلاس‌ درس‌شان به بیش از هزار نفر رسیده…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462618" target="_blank">📅 11:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc48f9072.mp4?token=heKHOGyKe_cQDSImSEjLlkPvUz9UFUTrqeaC_6gWi8__y1X-5ZNIhNmf6vY97cVUHANEQoRx4Te0bOpuaEr84KUnBkLh2ljfJ0HT_JNrfFxWLhvW2u7xCRuKLChXpJ6u5gm_zLecct6k2aRAWF3ok0Wso0LfovlGV8DZVtdWqGwsST1QXaSpVkk5C_raOMOBDcaFBkJsD_zy_wiYV1ncV2Vq1q98bTBCqXbCGcltWgNM1ptjxtRAvV54P3IGiSP7lJmwrORovWiPONlchwEta6zUWyDPXhA7IBNjq6tbERHQogrquV_3gwenvauK6KktArBPcpA6zQnIbHb4PLg4A1fjq6nZ9XsVE14uiufJVWMiIBpCSjoGd6loN3rSknoOHW3FP82bpvoZu0O7uVJmnCS_8GHkUuZ5wtip_B9EWFhmg2bUnxxRxvC_uzGmY7h6XrPRoXFq4a4NK-i2n0ep01l7ebh1ygWuLO0Wm6zQI6MHAoc6ihWKNdFJFPJ-ZM7ulN42lNOqpoah4J7zXOlkvAOOAfO8ieD25KPyZ6TcT6wzL2IFvv_a-wTBKuWIr6gxPl99SBgpWhHmcfqXTuybBGJBAdbWykv904lvhAGQfHe2V749IbPisqiHImuJfN6pCqY2J3nZzwbOBJUA1LNZ_q0P7zyvLbUUxobl-TRQuK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc48f9072.mp4?token=heKHOGyKe_cQDSImSEjLlkPvUz9UFUTrqeaC_6gWi8__y1X-5ZNIhNmf6vY97cVUHANEQoRx4Te0bOpuaEr84KUnBkLh2ljfJ0HT_JNrfFxWLhvW2u7xCRuKLChXpJ6u5gm_zLecct6k2aRAWF3ok0Wso0LfovlGV8DZVtdWqGwsST1QXaSpVkk5C_raOMOBDcaFBkJsD_zy_wiYV1ncV2Vq1q98bTBCqXbCGcltWgNM1ptjxtRAvV54P3IGiSP7lJmwrORovWiPONlchwEta6zUWyDPXhA7IBNjq6tbERHQogrquV_3gwenvauK6KktArBPcpA6zQnIbHb4PLg4A1fjq6nZ9XsVE14uiufJVWMiIBpCSjoGd6loN3rSknoOHW3FP82bpvoZu0O7uVJmnCS_8GHkUuZ5wtip_B9EWFhmg2bUnxxRxvC_uzGmY7h6XrPRoXFq4a4NK-i2n0ep01l7ebh1ygWuLO0Wm6zQI6MHAoc6ihWKNdFJFPJ-ZM7ulN42lNOqpoah4J7zXOlkvAOOAfO8ieD25KPyZ6TcT6wzL2IFvv_a-wTBKuWIr6gxPl99SBgpWhHmcfqXTuybBGJBAdbWykv904lvhAGQfHe2V749IbPisqiHImuJfN6pCqY2J3nZzwbOBJUA1LNZ_q0P7zyvLbUUxobl-TRQuK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ۲۰۰ شب حضور خود در خیابان را معنا کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462616" target="_blank">📅 11:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
پیکر شهید مولوی گرگیچ در زاهدان تشییع شد  @Farsna - Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462615" target="_blank">📅 10:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMXc9I-leZ5W-X3W7nZC3-NJ-eRxmJMHfD816O3Yev4gB01W1mSW-Lm6eaPejL0zG2IHGo2QyCnFVStPyIDIUYBaNdRb56jkUq4xdWmfyzxVK-4AM2slDTezU76wW5PUGbd2Io5AO2zx_cb9SS64uv1Tk12eSZcowGJaB904cM0plFq2CFTl12Qjzyo6rGitwfCAfLpppIOufu3OwgHhBmOX5Er0E49MgzAq0-B-SsZ-yXXqPCaruiLUSB87NgcYhEBEZp7WenRP7g8-H0LAqkxED6s4Gb99lt6_fe52CpUqddC4vzukC7Fcv_CCyIAnXoHt-e_dXS1HyRi-9mehFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: حرف‌های ترامپ حتی در معیارهای جنگل هم پذیرفته نیست
🔹
این حرف‌هایی که با افتخار بگویند یک کشور متمدن را به عصر حجر برمی‌گردانیم، حتی در شاخص‌ها و معیارهای جنگل هم پذیرفته نیست؛ چراکه به هر حال حیوانات جنگل هم حرصشان حد یقف دارد.
🔹
نفت کشورها را می‌برند،…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462614" target="_blank">📅 10:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462613">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La6MRxMm6Z1irzNjxOvroSnowblRng50cTYsSmkSkSS5LsDW9oNvMj4lvgmhh-0GQRwqy0mG3O5pZiudoByvfWVmGPs2YTiAYPU4EGZQGQ5-YXO5dOS0IIVyjhZfoZjcOiUXtAxzzfNBYri4UR-t-jKd2K2378pokYjnNYBeeSVDOWh1zwZBtV4AJhiY1RDFAAvTX3cM7-aE4sIuYKrL-AJU22B2o6X3MhGWqQrZ4aU8D2H-ZyixbQoQmJRNQX0vS3YPil-YyBGADH2cilz9bkApKVxZ2BKs2X1GM4un0GtOd2wCYNNhWSKJ1C6Dwn7FiSr5hT26VsSuRvniv3ASKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادی که جایگاه و نسبت‌ها را کنار گذاشته بود
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان آیت‌الله سید مجتبی حسینی خامنه‌ای: رهبر انقلاب در سال‌های تدریس در قم، بدون جایگاه و امکانات ویژه و مانند دیگر طلبه‌ها رفت‌وآمد می‌کردند.
🔹
جلسات درس ایشان نیز بدون اطلاع‌رسانی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462613" target="_blank">📅 10:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462612">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVDB6Vnm-MRB0B5p8k3ZEXIRinR4mQy0OjibthEu6xI_M098J1zps4Wdc2E6gqbVx8kioPZfNSbWsgum5i9C3skin3uJHRSyTeRpfMoVwLnIW9LLSYHoopvpbIjjSvXUmNKohTZ1RT9II4FL7lnnUXRi8HIvu-wzYlEUNpM4s5i1lhqcKqZ--1VVh8HSyBxrpweXLj4YMx3U8t2uAFCpKqBuU6fU-TTpiEZ1SOL_wlmJqPj9Z1XQ-Dvjc7KaIiKuCSbwN4FZoOYf23PzrxxRLi7Kv2K6tDh0zMoGwXedQ7RQAdoTNJELknZa_kn8iYiPw2XW4LNbDGVTHtgqJCNMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: حرف‌های ترامپ حتی در معیارهای جنگل هم پذیرفته نیست
🔹
این حرف‌هایی که با افتخار بگویند یک کشور متمدن را به عصر حجر برمی‌گردانیم، حتی در شاخص‌ها و معیارهای جنگل هم پذیرفته نیست؛ چراکه به هر حال حیوانات جنگل هم حرصشان حد یقف دارد.
🔹
نفت کشورها را می‌برند، رئیس‌جمهور یک کشور را می‌دزدند و زندانی می‌کنند، ۷۰-۸۰ هزار نفر مردم بی‌گناه را در یک منطقه مانند غزه به شهادت می‌رسانند اما هیچ اتفاقی نمی‌افتد و باز شعار تمدن و حقوق بشر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/462612" target="_blank">📅 10:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462611">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">🇮🇷
پرچم ایران در دهکده بازی‌های آسیایی به اهتزاز درآمد
🗓
بیستمین دوره بازی‌های آسیایی ناگویا از شنبه ۲۸ شهریور آغاز می‌شود و تا ۱۲ مهر ادامه خواهد داشت.
@Sportfars</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462611" target="_blank">📅 10:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1zpPgRMIf9VpP1WjNBQGBzxGtM8ZRkbMnPDAJL9EaH5wUiHhgNKUqirFu14EQ9548T4c6nXSF60sY7gyAziCFyxRR6yq1vVPYRAwXmuaAi7CPQ9ClfX6a2IRfgkSgKD9U9L6o0IOF8UNR3wbyTB4x7TkQ-Hkkfs8B8vkFSrP5GL87CGNEmgT3JyQZJOwK6auvnT-qjHlLTX_cmo6nY_UMNRqzZFeaNhBDJDRvYNQyYamOIWwwWSX6uWOM4ggnmtf0SpUeOw_q8WABOukXCOVgMkMWxN12PdWMhKt0uPf0ROM_6LR3PsZvjyIHfOZ497k4OdrwoZdNkSHbFn5KiuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادی که جایگاه و نسبت‌ها را کنار گذاشته بود
🔹
حجت‌الاسلام محمدجواد قاسمی، از شاگردان آیت‌الله سید مجتبی حسینی خامنه‌ای: رهبر انقلاب در سال‌های تدریس در قم، بدون جایگاه و امکانات ویژه و مانند دیگر طلبه‌ها رفت‌وآمد می‌کردند.
🔹
جلسات درس ایشان نیز بدون اطلاع‌رسانی عمومی برگزار می‌شد و طلبه‌ها برنامه کلاس را دهان‌به‌دهان به یکدیگر منتقل می‌کردند؛ به‌طوری‌که جلسه‌ای که با حدود ۲۰ تا ۳۰ طلبه آغاز شده بود، چند سال بعد به جمعیتی حدود ۴۰۰ نفر رسید.
🔹
یکی از ویژگی‌های برجسته ایشان، بی‌اعتنایی به نسبت‌های خانوادگی و استاد و شاگردی بود. در جامعه می‌بینیم بعضی‌ها به‌طور کلی موجودیت‌شان با همین نسبت‌ها تعریف می‌شود؛ من مثلاً بچه فلانی هستم. من برادر فلانی هستم. من شاگرد فلانی هستم و... اما در شخصیت حضرت آقا اصلاً چنین موضوعی بروز و ظهور نداشت.
🔹
اجازه بدهید یک مثال برایتان بزنم. خب حضرت آقا، غیر از اینکه پسر امام شهید بودند، شاگرد آیت‌الله وحید خراسانی هم بودند و سالیان متمادی در جلسات درس ایشان شرکت می‌کردند. اما هیچ‌وقت شاگرد رسمی آیت‌الله مکارم شیرازی نبودند. با این حال، خوب یادم است که در جلسه درس اصول، به کتابی که آیت‌الله مکارم در اصول دارند به نام « انوار الأصول» استناد و از عظمت علمی آیت‌الله مکارم تجلیل می‌کردند.
🔹
آفتی که ممکن است در روحانیت شکل بگیرد، این است که بعضی‌ها ممکن است دچار توهماتی بشوند. مثلاً اینکه چون من پسر فلانی هستم ،دیگر از فلانی یاد نمی‌کنم. چون من شاگرد فلانی هستم، دیگر از بقیه اساتید یاد نمی‌کنم. اما این مسائل اصلا در حضرت آقا وجود نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/462610" target="_blank">📅 09:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462609">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
شما این مدال را گردن چه کسی می‌اندازید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/462609" target="_blank">📅 09:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462608">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGSWDscDuv8ZS9-Xa2qJiGbRvP2tysv5V_PlybjtB1PTF_hoor40VUd0vO9lkB8h0ocBFs9FiRChYHyh85NQzagQcLmaLy7Yiq4q88sPnUOfdQv6D8n7GaC6t7vV5IWaUNTvdpqF6w5yZDF4Kawuj87DmAfs_UUQWNfoKXTyDsPBO3SswmZ0vtdJ14ulmV-T8p0UQ2Qps1bgyezMmNz-6lgKJmQEQd4cV270P9tprCELh1bOkqpyzF0gBTIHr3bBUvvnhEgS-6zvQxqqBmIUP05aSx-xvUcWjZOA90Iv0lvIHPRQ1Y8S-u1OfXLdlnU77RJjC3ls4DZGhe5gG-M4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/462608" target="_blank">📅 09:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462606">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_36Pz3Hxnm9IZnjclWdDmgbuEG1vm0-ih6NRvC02evFqqntkDL3XfiM718mOr17r8JC1ZjsDvZx-UuQZ8ClA7jMNQhskk9kWV9fZrSbByeEHkTPLVqZMyvdZJru9t5HgDVZEG2DdACMbjnSr3GLbixYXZsXL5xX9tINZaKG5go-BopWT485-9Sgu3vd0ZbC8emL3KksMarc0itd6js4TkwVMJU1Pyu0IDaSDOGJ0inw31kc2gUdgA-rBuMCvYM_REem3rtKnQBOWRAr7Ft_IUkXD95PzoiuaTTaWpYsbpyyCKvGcgIoV8e-gWE8HRzOA6ZlKfqN1EnYD5ymvl38fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسبی سلبریتی‌ها همچنان روی موج زن، زندگی، آزادی!
🔹
همزمان با فرارسیدن سالگرد فتنۀ زن، زندگی، آزادی، بار دیگر کنش‌های گتره‌ای سلبریتی‌ها بروز پیدا کرده و افرادی چون تهمینه میلانی، دیبا زاهدی، بهرنگ علوی و زینب موسوی با انتشار مطالبی در صفحات شخصی خود، به استقبال آن رفته‌اند.
🔹
این طیف از سلبریتی‌ها که بزنگاه‌های خطیری از جنس جنگ تحمیلی ۱۲روزه، جنگ تحمیلی رمضان و شهادت مظلومانۀ کودکان میناب در حملۀ دشمن آمریکایی-صهیونی به خاک کشورمان را مجال مناسبی برای سکوت، انفعال و یا موضع‌گیری‌های وسط‌بازانه یافته بودند، حالا به شکلی صریح و بارز روی موج رسانه‌های بیگانه سوار شده و به تریبونی برای نشخوار مهملات آنها در باب فتنۀ «زن، زندگی، آزادی» تبدیل شده‌اند.
🔹
واضح است که امروز و پس از آنچه در جریان جنگ‌های تحمیلی اخیر به ایران و ملت مقاوم آن گذشته، دیگر حرف زدن از «زن، زندگی، آزادی» صرفا کنشی احساسی و هیجانی محسوب نمی‌شود؛ بلکه به منزلۀ همراهی مشهود با ادبیات سیاسی بدخواهان این مرز و بوم و تبدیل شدن به قطعه‌ای از پازل پیچیدۀ دشمنی‌های آنها با ملت ایران است.
🔗
اما علت کنشگری‌های کاسبکارانه و همدردی‌های نمایشی برخی سلبریتی‌ها چیست؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/462606" target="_blank">📅 09:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462605">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8OBxM_pszRR4pU0CSfc0LTYCT_-Zu09T0tFNHbFftfR51jW9bnbf4q6SxVIzbhu11Fsc0czBd_Q0mobTD-oiVkBrdk2ZypmNx-C_guv4RZK8IxjiUn74djuKjgOucTsylGvH0x-Lxs5ECAQNhXnUZxfvkmUME1pX7PErBips7Sapcn2uGZhUrIW7LBXKFGRHGjWaRHLrqtFkrn_jXDv-137xLEhrl-aFvGLSOVoOUvrtJaj7Y4mdu7ndDsqMuZ-RU5v3s1G_C8Foe3tp0DdXsuShctbXwCxITlQwVdCsToHZOtk3bmpP5OMH8W2HjjE4FtGpVSgLxLz0NjmUQJK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با سران کشورهای حاشیهٔ خلیج فارس دیدار می‌کند
🔹
آکسیوس به‌نقل از منابع مطلع مدعی شد رئیس‌جمهور آمریکا، قصد دارد سه‌شنبهٔ آینده در حاشیهٔ مجمع عمومی سازمان ملل با سران یا وزرای خارجهٔ عربستان، امارات، قطر، بحرین، کویت و عمان دیدار کند.
🔹
در این نشست دربارهٔ مرحلهٔ بعدی جنگ با ایران و راهبرد پس از جنگ گفت‌وگو خواهد شد.
🔹
همچنین نخست‌وزیر رژیم صهیونیستی، دنبال دیدار با ترامپ در نیویورک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462605" target="_blank">📅 09:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462604">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کرونا دوباره در ایران شایع شد
🔹
با افزایش موارد ابتلا به کووید-۱۹ در ایران، پزشکان و متخصصان ویروس‌شناسی بر رعایت بهداشت فردی، استفاده از ماسک در فضاهای بسته و پرتراکم و پرهیز از حضور غیرضروری در مکان‌های شلوغ تأکید دارند.
🔸
علائمی مانند بدن‌درد، سرفه، عطسه، آبریزش بینی، تهوع، مشکلات گوارشی و بی‌حالی در میان مراجعه‌کنندگان مراکز درمانی دیده می‌شود.
🔹
میرزایی، پزشک عمومی با اشاره به افزایش مراجعات، می‌گوید: شدت این ویروس در مقایسه با برخی سویه‌های قبلی کمتر است، اما بیماران ممکن است چند روز درگیر علائم آن باشند.
🔹
مرکز مدیریت بیماری‌های واگیر وزارت بهداشت اعلام کرده درصد تست‌های مثبت کووید-۱۹ نسبت به هفته قبل افزایش یافته و به ۱۱.۷ درصد رسیده است.
🔹
علی ملکی، رئیس آزمایشگاه مرجع کشوری کووید-۱۹ انستیتو پاستور ایران نیز می‌گوید: وضعیت فعلی نه به معنای پایان بیماری است و نه بازگشت به روزهای همه‌گیری؛ بلکه باید کووید-۱۹ را در مرحله مدیریت و مراقبت مستمر دنبال کرد.
چگونه خطر انتقال را ویروس کاهش دهیم؟
🔸
استفاده از ماسک در فضاهای بسته و پرتراکم
🔸
تهویه مناسب
🔸
رعایت بهداشت تنفسی
🔸
پرهیز از حضور غیرضروری در مکان‌های شلوغ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/462604" target="_blank">📅 08:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462603">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گفت‌وگوی تلفنی عراقچی با عاصم منیر و وزیر خارجهٔ ترکیه
🔹
عراقچی دیروز همزمان با حضورش در پکن، تلفنی با عاصم منیر، فرماندۀ ارتش پاکستان و وزیر خارجهٔ ترکیه، گفت‌وگو کرد.
🔹
در این تماس‌ها آخرین در مورد تحولات منطقه‌ای بحث و رایزنی شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462603" target="_blank">📅 08:22 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
