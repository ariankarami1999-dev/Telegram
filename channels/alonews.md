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
<img src="https://cdn4.telesco.pe/file/bdiIB1ufgds_E3tQk2lgIldjwrghyjnbu8VHMsHfO90aRfeGHMD78K1QwVAQdHyE15gIgA06awTCG08tFtHFacIggDVfS_ywEF7P_2gnhLHn2wEauSHUSxG-xGOsiXSQFJaRFliJOQLv4eyETUiPIPP-MbE3KHDsGBo6s8MpRroxOHMPO5RYSr1ZLj_aonFHwdRY6SNR02MGD8tmiSbdvgKrZsNU45rwFXAlL8-P0jEJWibaATh5U1FffdIvzVGbWHHmdYHKfvpQUOQCgiAGBjRxSHjWkEMRyokzky0bBf1sYlGj4pSHw4e-PyZ65qt4eO7QO4J-4dmzspcv5s379A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 937K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 15:03:20</div>
<hr>

<div class="tg-post" id="msg-122543">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ادعای واشنگتن پست به نقل از یک منبع:
بازگشایی تنگه به صورت مرحله‌ای خواهد بود.
🔴
در مرحله اول، آمریکا ۱۲ میلیارد دلار از دارایی‌های بلوکه‌شده ایران را آزاد می‌کند، مین‌روبی در تنگه آغاز می‌شود و محاصره آمریکا برداشته می‌شود.
🔴
تفاهم‌نامه شامل توافق هسته‌ای نیست، فقط تعهدی برای مذاکره بعدی درباره مسئله هسته‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/alonews/122543" target="_blank">📅 14:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122540">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2b6f9bc3.mp4?token=ERYrENRTSQk9KEQfN8s20NyiVRlR_eFwTjB22gZNATblDnB7uM5H-nKFXswFAxHvyCQkLFuUhDqSQKVVF24UOuJbHC_TLWXB5aCoTu3auWQsJ6-fB7gAukb0BYpeFu3Yb5lVe2gD_cL468-qthH88iRvsY4-_JbcXlaudGuwx67hrvH3pdq19DeBVNvEqx65mGrD7G0UiCBommojCjtbPOuQ-fJIV78lPWcdENK14flvEwj2LfIQpNmXeDu5Jx_-RGloKq_8UorJHgpREDoYjZR2svlqYNIRJ2ZXansV_hpXECs1f6kDgudRR1qfij71r0INyD8Ve1TUpn4-ZADqmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2b6f9bc3.mp4?token=ERYrENRTSQk9KEQfN8s20NyiVRlR_eFwTjB22gZNATblDnB7uM5H-nKFXswFAxHvyCQkLFuUhDqSQKVVF24UOuJbHC_TLWXB5aCoTu3auWQsJ6-fB7gAukb0BYpeFu3Yb5lVe2gD_cL468-qthH88iRvsY4-_JbcXlaudGuwx67hrvH3pdq19DeBVNvEqx65mGrD7G0UiCBommojCjtbPOuQ-fJIV78lPWcdENK14flvEwj2LfIQpNmXeDu5Jx_-RGloKq_8UorJHgpREDoYjZR2svlqYNIRJ2ZXansV_hpXECs1f6kDgudRR1qfij71r0INyD8Ve1TUpn4-ZADqmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد حزب‌الله امروز صبح به سقف ساختمانی در متولا، شمال اسرائیل، حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/alonews/122540" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122539">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLt1fGi8kkwjwYJ59OSVxDgBNU_bOJWnuv2IYC8NE-xGx-0Yx1qRnm4Wo2IhjuIqOffg7B6_SECuVeN-StG0Iqrtka2O5GPXRI-7d2TkzCaXFudN-UeG4iVooJSqJzpyKbscqq47wZia43cvrK-XrdeE76Dy4gz01hFGwS8DubtkUiv7OeCysL5Geda9czhoCdbirBku2dFYkLNzVKx5N0FxHPlcOG-dw2ttHItEaDU8VXp3CIqYFh2mNjodrbb99EyxRHxGr5O8N0dzaUDdbHc6rC6Z9dFV_0CAivWJJ6k7jXbaJL4MZCc0PegubeAw8Vs7IDSyqr0yxAcqg85Vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۷.۸۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/alonews/122539" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaG86VCOcVhWJmKpOkWe9Oh8MS3iZU_S-_7MLxbX83vS1m-dCPqYkkAlKoocVAP9p9pG8Q3W9mSYji1HAxejlNzwFA-du45js5jedSC0U7EGO67od9QvDKo1qW6G857TT9zkmlmIsiD9b8l1pUjU1m3QetBXN6_yMqdJsMeW8FdgiNjAafSw6dNufrVl0zddBnfMNvC_T6WZBibq-BGm1N9FIQXJ9pgo-yvvvDoe57dNYmmX0docnhf3WJh1Lw_00Vp2Xw94qjlC3rjnUdGA8uqc9zrj0yo_93A2GliyhiF9n4vhD5Hx5buVnfUc2df3I7wlgxleUBcAFzwca2lX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیئت‌های چینی و پاکستانی در تالار بزرگ خلق در پکن دیدار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/alonews/122538" target="_blank">📅 14:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZeRmNXyMa9Lej5CZKiDre2fKQ6BXhwXXPXNbbamFb0yz9zJ_uW0uZAoJCC754QtKcgFn_qNZ3mVpLtF0U6SbNKeDTtWEX3Veg3wLXUOn-3GO7dwLB_1_RS1DrFZrjdj04L07OXqmJBsq5O7cJ9V9w5entX-E-u83uew38MA75Uex2DWiyUvMtNN2bIwzvcbmuYSs3DyVDzLnY_VTQ7vsxZK6wVNcoYf9od68FndtCid1yAukkN5odb3X25PasAvW34n4u4dlBdqa4HlkwsEDNlrX_UbAfMirZSxWVc-S3BcPg4dkuTiaR_YipStqQAC2pYNEjfxcOXEMaercT2CWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: دموکرات‌ها سیاست‌های بد و نامزدهای بدی دارند. غیر از این، آن‌ها عملکرد نسبتاً خوبی دارند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/alonews/122537" target="_blank">📅 14:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDA8WROzE2agn7xvO5nHo-rcsTyGEWjDD2OS9SYMZv9ae6Y5JdAkC-vznkXkJoA_kTdfLtXhTvOq9vtfG4wKcB5tC35Zf_jVT2pDnfPwq6k7VltfB4vSwylRPOKJgaeQsi4LbW3v4U7EzuCEhxAlSpvYrhH4FD7bW1v7IQNFpIpWndWEqU1g3lf9bjrGl6duS34sRb0JZcndp3YcPC8kP_vhj5o9UO19J9vwzhAYD0y2MeYBXv7_dibGTVhHapkjJZmUpcPHl8FA-8z1LkVygrVGgKDOPe2n90YMlN9sAJW9V6nXTTbU9HiEqfrwWlKuS8uu1N9bG6MNYNCQLBnB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
روز یادبود مبارک به همه، از جمله دموکرات‌هایی که به ارتش ما و تمام موفقیت‌های عظیمی که در سال گذشته داشته است بی‌احترامی می‌کنند.
🔴
خداوند کسانی را که بالاترین فداکاری را کرده‌اند، برکت دهد. من همه شما را دوست دارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/alonews/122536" target="_blank">📅 14:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان در دیدار با رئیس جمهور چین گفت: پیشرفت قابل توجهی در مذاکرات ایران و آمریکا حاصل شده و اوضاع در مسیر درست پیش می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/alonews/122535" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دبیر کنگره موبایل ایران: برآورد خسارت روزانه ۵۰۰ میلیون دلاری به اقتصاد دیجیتال ایران در پی قطعی اینترنت و اختلال در زنجیره تأمین موبایل، با خطر لغو ۶۰ هزار شغل و توقف واردات در فروردین و اردیبهشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/alonews/122534" target="_blank">📅 14:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری / منابع پاکستانی به خبرگزاری آناتولی گفتند که آمریکا و ایران می‌توانند طی همین هفته، «یک پیمان موقت برای پایان دادن به جنگ امضا کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/alonews/122533" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سازمان توسعه تجارت ایران، ثبت سفارش واردات انبه را تا اطلاع ثانوی ممنوع کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/alonews/122532" target="_blank">📅 14:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یک دیپلمات ارشد ایرانی به خبرگزاری ایسنا گفت: اگر آمریکا به تعهدات خود در چارچوب یادداشت تفاهم احتمالی عمل کند - مسئله هسته‌ای و ذخایر اورانیوم غنی‌شده پس از ۶۰ روز در ازای رفع تحریم‌ها علیه ایران و آزادسازی دارایی‌های مسدود شده ایرانی مورد بحث قرار خواهد گرفت. مدیریت عبور در تنگه هرمز یک مسئله ایرانی-عمانی است که تهران با عمان درباره آن گفتگو کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/122531" target="_blank">📅 14:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: چیزهایی هست که از اول هم با ایران در موردشان مذاکره نشده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/122530" target="_blank">📅 14:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-v6eaSor75t8Q7grTvCFbx-o18v31R0YiTzXxID4q_F70Agh0naU6vYTaZZueJ8tNzgvcoaLNdbB1WDLYirMLfaNYljDIC6zOZWYAQGVsTYpmrq3YpAOfDolqKyAaiBcipfnHMU7OJKAgGhDemlKQlLnCWg1cMoVdI-lGwBZDtfEbgvi4i5Hc7CjW3CAkarHRCtm0oI2ylEPWxjXyL0sj2B87kHRHV_C_6HyTQ0uZVa36ivYnbcTHfpY2LSpGGCl3NWXUEHOtCO-BVih5AUEWcpZaQJlgwHwqBIdEadmq-RwpQviWsRVF4ZnHWG6YemvPouRIhQFhF9m1VyMJahSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/alonews/122529" target="_blank">📅 14:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNJtUHIXmBVe95SeWvYc1bSWUy-hnIaMA3mgNx42BW_fdaFHonDu5K7s91oWtnK9VjzSWGdggcKbAljtPb_mrfyMvuv6IWu51BeqMJ06dxwlme3-QrTACy1fiIGFYfU9E_38a8dV0TWJZtFq2r01wPDpckqW7EN2_h4EZISs5CmMZ2WpAeQ1vOZ2lPAO2HlVKl5-v9ncoyqa5O1XGBOAibjLARyVA-xdf4KROpc50vvrDbot8agrYl_Xlustn8Z9Fv89iXmrSdiB8KVYwCKIrSl0TpSvwwgCxVNhzjXMtxX6_8Xr70vOxpcsyvZnKkj4pBpW9nosysUXcAZ8xs7v5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری
Financial Juice
به نقل از ترامپ : یا یه توافق خفن و واقعی با ایران می‌بندیم، یا اصلاً توافقی در کار نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/122528" target="_blank">📅 14:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل، ایتامار بن-گویر: نتانیاهو باید دستش را محکم روی میز ترامپ بکوبد و به او بگوید که ما به جنگ بازمی‌گردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/122527" target="_blank">📅 13:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVW5280jwFmKQ7NwOZypOGFtlhAg83keAw3GuRbtMbSSi1YwETlk9MISwtTJW8zW1mAUDlLAGFUzpqDr9yzUyT_9KEBtd1fCzdiLGIxxicUzk_aTdrYT10w6BB_sqmt3ceYPKWJ3KDxxpg6Zu774z2R3DZGKs6xsIHkuVowPS4A1_lXD0_XPm0YWJDWXQcoxZs_sEI7JBDKKL5N9czizer9UsOqXWAD_nhX9BN0KLNc1qKrXail7ToznQhRR_hnfLPV0hGYpv382wAIj_El4c3smTbsNY7anZdWI6EXf5sseuKrfwdVLW-QFtktyT5jJB1GkhQd6iEEhruR0H5JtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ درباره ایران
🔴
ترامپ : به همه دموکرات‌های احمق، جمهوری‌خواهانِ فقط به‌نام، و ابلهانی که هیچ‌چیز از معامله‌ای که با ایران دارم انجام می‌دهم نمی‌دانند، می‌خندم.
🔴
معامله با ایران یا بزرگ و پرمعنا خواهد بود، یا اصلاً معامله‌ای در کار نخواهد بود.
🔴
این معامله دقیقاً نقطه‌ی مقابل فاجعه‌ی برجام خواهد بود که توسط دولت شکست‌خورده اوباما مذاکره شد؛ برجام مسیری مستقیم و آشکار به سوی سلاح هسته‌ای برای ایران بود.
🔴
نه، من اهل چنین معامله‌هایی نیستم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/122526" target="_blank">📅 13:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سخنگوی مجتمع گاز پارس جنوبی:
صبح امروز در عملیات آواربرداری پالایشگاه ششم پارس جنوبی، یک حادثه رخ داد که ۶ نفر از کارکنان شرکت پیمانکار مصدوم شدند.
🔴
۳ نفر سرپایی مداوا و ۳ نفر دیگر برای بررسی‌های بیشتر به بیمارستان عسلویه منتقل شدند.
🔴
علت حادثه در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/122525" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hL7q2ZFgO9PNCw27Hqg_ciRYqFze6RsQ2jF3oQUIaKVLyZe5AdsIun0DTnDsM8ru5cN9uSmaO5SmioF_4xICzBBalBZw1540AJWiNqFRfmCiNyh5aS1Kjj-v6tjIRL403XeshFNX2Dw0GFmkpHhpmhrfmvcNNVLvyK4zOnAOHN3oxtCW1vDNOoOUZwhAP7hK2cdJywcjPh5RACBsYQBup0Ne6z8A-7O-EFK8IAni2xfYf2Ww4HgHTzmCerI1qK0aErJmxGDsC2CHDCmmFmNLdX5TK-oOzPZ3x66sWeaiVPpBMQ-JysRX6VV5DaIawm4p-BtV9Dgi6xHgKjJGBcnXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۸۳ هزار واحدی شاخص بورس پس از پایان معاملات امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/122524" target="_blank">📅 13:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری/ بازگشایی اینترنت بین الملل مصوب شد ‌
🔴
ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد. ‌
🔴
این مصوبه برای رییس جمهور ارسال…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/122523" target="_blank">📅 13:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شاخص کل بورس با رشد 83 هزار واحدی در پایان معاملات امروز به 3 میلیون و 993 هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/122522" target="_blank">📅 13:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11c2bad0b5.mp4?token=IjB_Z1_Cdw8OBCghKFpHWxF1YBsRPCzl1yHP5riXYf7fAytukCIHFOyp4YviySrdP9ocXMdLgc4tuRoOIKASOfnOdHehT0lSuk8sEgk3xmQBUePhpgw3STNW0aXCkePQdlKORkQEiGG3o5WLr28ozPN8NZBVaM5WGyPnsEZ09RA8_HLMTgKpFxjCQRQEYC0Av1-GfmuHzlzPUAwa17o-u6QcD3dXgTETXPV3i5KOSD1OCVzSuBGanj_36O9zFFnCjdZk4rwvLSrKoqPhO9h2jpAmhrEHRGNHO33wVCe8qEJ_yzombzg2ohicv-2kZ9NsmVpCXOA2Rg0hGId5FDBxjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11c2bad0b5.mp4?token=IjB_Z1_Cdw8OBCghKFpHWxF1YBsRPCzl1yHP5riXYf7fAytukCIHFOyp4YviySrdP9ocXMdLgc4tuRoOIKASOfnOdHehT0lSuk8sEgk3xmQBUePhpgw3STNW0aXCkePQdlKORkQEiGG3o5WLr28ozPN8NZBVaM5WGyPnsEZ09RA8_HLMTgKpFxjCQRQEYC0Av1-GfmuHzlzPUAwa17o-u6QcD3dXgTETXPV3i5KOSD1OCVzSuBGanj_36O9zFFnCjdZk4rwvLSrKoqPhO9h2jpAmhrEHRGNHO33wVCe8qEJ_yzombzg2ohicv-2kZ9NsmVpCXOA2Rg0hGId5FDBxjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عوستاد خوش‌چشم، تحلیلگر مسائل راهبردی : تا پولای بلوکه‌شدهٔ ایران آزاد نشه، فعلاً خبری از هیچ توافق اولیه‌ای با آمریکا نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122521" target="_blank">📅 13:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4yMSOCafh6tkFcdUq9VgcOcsHolB-Kx6TB6IIzmm7RS6tKxYQHsUEMwU8ekdgVEluim-uKwDsPMq9NRcu5uHxlIx8gmn_FEpuWZHRVPur2r1wtGMkTFMNcZ3u5XqYS9r4I8nr08-08l4qQH80cnO9cy9f2hCuXcPlaTf97NHY1gc5qwIX3byQMUnue5Xu61VLCSFc3iSYmxX2LnVwDaz3YfFz5a0wafCB76QUlDhcMvCXDZDs3PHZwOxtbcV7dkbo1u3kBAwtj2lKa_kh-jgMYnbDftY7Y0IsaNu4Qc-jwQKlCyvkrINQV2D6krqhKBH4p-Paewdn5kXJhLNo7e2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آونر ویلان، مقام ارشد دفاعی سابق و کارشناس هسته‌ای ایران، هشدار داد که بهترین توافقی که ایالات متحده و ایران می‌توانند در مورد مسئله هسته‌ای به آن دست یابند، ممکن است شبیه برنامه جامع اقدام مشترک (برجام) باشد که در دوران دولت اوباما حاصل شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122520" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان: تسلیم زیاده‌خواهی‌های دشمن نمی‌شویم/ حقوق ملت ایران باید به صورت کامل استیفا شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/122519" target="_blank">📅 13:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
هاآرتص: افسران ارشد در نهاد امنیتی اسرائیل از توافق احتمالی بین تهران و واشنگتن هراس دارند
🔴
آنها هشدار می‌دهند که منافع امنیتی اسرائیل در طول مذاکرات لحاظ نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/122518" target="_blank">📅 12:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvvmdwWj2oHwfl44EVgPtzPyShKtKN212Yimts_THBZPatuMhPsdVY1ilrIkeo49U0nLO-Mwe30bx_9etr9MX4E341XIzU6VD1JNTwPGgjLp7-9OdyGaa2gdCUc3zSg7OhlW-Y16R3urPK9TronsyspVOL6ityd-cIMOIQ5kpkvHCk3Q2A--rUlF6kZQBlx0QPsUQwB83zmtL1_Ftie6In4C8FP-kyZ5AXkPA0Xa1PMx6xHc-Txm4ru0kTC0XsTbSSpNDvicIyMXHETyWCwHhmDIFp48T8DbOIgfNp4003tuILQmEVuAv5ty9Q_FMmX3dhSgLX-f7H9EoA053-PKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظرسنجی جدید نشان می‌دهد که تردید گسترده‌ای درباره آمادگی دفاعی آلمان وجود دارد، گزارش DW.
🔴
این نظرسنجی نشان داد که تنها ۱۷٪ از آلمانی‌ها معتقدند که بوندس‌ور می‌تواند به طور کافی از کشور دفاع کند، در حالی که ۷۲٪ گفتند که به آمادگی نظامی شک دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122517" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCN4_UwNwLViu95Ath-n6vDZ8m3kEoNuqxYKLpQXg2_NgeNmuEmfmZAP0hrt_3s2fDwtlxn70jZbicQcoLq9iT-Q1MTwQbgZ4uFnvN3AlIuZlc2_JCj21wOtBGDWWu3JTFHotA674CGdqM2yKaObl61YSMe4FqAzf5z9SXzSmEZVH_gzqUOk3cDrPFnRBVBi6eqmPwvq8XAa0qmPxGMoZN8IIp6u6X4b7SohY7y7HKoshDtezZLc1R7oGTP1SJo0vmQCyNt1wltKQ2KWzpYQh06BQxCGkzWHj8wKCMGqXA5h2mISbixnvgFDJKbM1YTONALcG6whkxkZDlJPijFrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، بزالل سموتریچ: برای هر پهپاد انفجاری حزب‌الله، باید ۱۰ ساختمان در بیروت فرو بریزد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/122516" target="_blank">📅 12:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122515">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f45a5fac.mp4?token=ZuS56hIDwU00dIXTMv6HMSKOXwgFt_pIVqTUldjCXUbAFEUo_9IBgon3UP7MJ9KH7-uE823UMmMlzSCYdcOa8-ZQDiRo8mRDDfboEhmI-jXX1kkt3M67SEmKFaCsdJSo9F6sAK79ChOYYrIfVYpZdVxYlnqoEjLctS_88MFWh74gNHmkFrQakuD4K08lyjqN42mEMTxPE8iatYiMxTTIMtTMZsQjt-hcFz6ZbnB_sYMW4bwYjlTi-hAm8PcDqKnj_CaKUk1K75-wHsz1HKq1NVtf--dXxTbp2yDO8aERgHJ5bCEUFN5zr0JWodagZG1tIMWnjFvGQy6kHMDG2kiaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f45a5fac.mp4?token=ZuS56hIDwU00dIXTMv6HMSKOXwgFt_pIVqTUldjCXUbAFEUo_9IBgon3UP7MJ9KH7-uE823UMmMlzSCYdcOa8-ZQDiRo8mRDDfboEhmI-jXX1kkt3M67SEmKFaCsdJSo9F6sAK79ChOYYrIfVYpZdVxYlnqoEjLctS_88MFWh74gNHmkFrQakuD4K08lyjqN42mEMTxPE8iatYiMxTTIMtTMZsQjt-hcFz6ZbnB_sYMW4bwYjlTi-hAm8PcDqKnj_CaKUk1K75-wHsz1HKq1NVtf--dXxTbp2yDO8aERgHJ5bCEUFN5zr0JWodagZG1tIMWnjFvGQy6kHMDG2kiaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو تو پاسخ به سوالی درباره نگرانی هند از نقش پاکستان به‌عنوان میانجی بین آمریکا و ایران : هند همیشه نگران گروه‌های تروریستی مسلحیه که از خاک پاکستان فعالیت می‌کنن و هند رو هدف قرار میدن، این نگرانی همیشگی اوناست
🔴
اما درباره نقشی که پاکستان به‌عنوان میانجی و تسهیل‌کننده تو موضوع ایران داشت، اصلاً مطرح نشد و فکر نمی‌کنم هند مشکلی با اون داشته باشه
🔴
اختلاف هند با پاکستان یه موضوع جداگونه‌ست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/122515" target="_blank">📅 12:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122514">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری/ بازگشایی اینترنت بین الملل مصوب شد
‌
🔴
ستاد راهبری و ساماندهی فضای مجازی صبح امروز دوشنبه (چهارم خردادماه) به ریاست دکتر عارف معاون اول رئیس جمهور تشکیل جلسه داد و بازگشت اینترنت به وضعیت قبل از دی ماه 1404 مصوب شد.
‌
🔴
این مصوبه برای رییس جمهور ارسال شد و در صورت تایید رئیس جمهور جهت اجرا برای وزارت ارتباطات ارسال خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/alonews/122514" target="_blank">📅 12:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122513">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عبدالناصر همتی برای پیگیری آزادسازی منابع ارزی ایران راهی قطر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/122513" target="_blank">📅 12:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEn_8ZHoaKTJEuyS76_hquilKhzipxeXCp_WSy3Q8wVm-_gHgMvAUcPsms6WlxKTdKM_2Pard_onhEcJI19uBgnYGGvswfFsjtjQ28ydx8AuDJyTntXlTvVdEKUkxj5x6xSgdO3uPH78ALL07XGgD8MrhDtMnT0L8exFlsPNPysnpHtzc2TkSH3K20LVXCkZFuuo2HSNWDn45vLDT5kOK9zwNhL54yZWrdTyRFMVzSSmO-84JsQmW1-1dA9xodBAtU6GbZvzBhPjjn7nlhKZzZwdzkwRQ0ZhYSUtieA_d7H0vnpyNLptK3P3Snp7vRstIDEm9tG8LO9QtMQhC8WebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohXDvQiuHSdxo7wrNeKHXWDRhwECKa12nzKs8kAUViRy6_yQZB7dBfNThnyialbtDcKuoqXhIyHY76BtfwcvQeWum7gjz1Dj3dkMsJTfk67D758kU2NKp_RYacC5azdqZHTRsjfAmDhxh5Fu-v7KCZ4OveH5lEB77JHkgCmnbw9I_8iHgOPm4NEWPiiXOUGT9c_kEcWxjXRHypiabM8HFSSY-z0li-cfVAxwsdfVYnfpjLBgCymR9IcmzeRM3rHn_HiOP-ZBxfOB7ZWP-rW3CG0aEN0Y8qGLYAS91mNGbD1omoF8i9yHSiBB1--KgXniM89EvGrbZFnzkrFhz8tG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lwoo5l2roPOjF4QmxiUsAVmQrXsO5xdt3Nf2zPKcZp6T2aHyM466q6LvAYGW_6QfPldKty4WRnxlKQwz5sUGDdZtpPrAjbVZtHexYI1U7Y0kgwuVVp29WJFsAS6t5DEHu7_iEhjq6pQU7lAOaqsLVFV1WdFJ-CkfsbOP7aiDxYCm0CX6x_u3pOU8MzwZqaKj9TsD7GB90EJvwboHk7fdcA0Dmc-zknyOtAMIv2m7XZl132Y_zJyxDMHPrKsTZ3lcDHSGRAbjj2ythzBQXJLwWgSMFH7_-tgnFJs7glfis0o6IlJ1_IaXIi7uM7rlwBBIk4BL1YhKgTB31SNln6XjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSQwfHbr3T4CNujPbXbpOMI54JTBYxoP4SZqCNOIoqlTYJZDZYqvc5z6anhkgnVHBtoZls1jKzfnuqRAFOiTHTLI0y4NKr4lBIoWOGu7EnteQymAv1LtckEJN7dE_GFAC2SrvH-Y4VTjd3wV32QG3G9XUOGeamRmT1Uo-94C5qA7VjiSIIgexGhl7kD_daMhY1jd9EaSVnZlpOMaQaufbBtlgLDUxlVc74qvLyPWkZmGWUbRxBpItGyanGO7nuFqhxRN_2ne7EADMs7goxxP-dCbxOKNnfys8kVSgWIjqa5Y4NmH1d0VTIVqSpAaAJ93d5vWW3Si4IdZemq3yRiQog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipQx-WJ7rPe982XSkL8tya9_-K3Fgiiwt_idezcuO7D4gZ0x1eOqRHq4lcgsgFEqQysHLALJVTuSgjg__0_yQbi_WItdZ4S9mBLyPswSqkbkeRNTj1CYWMqwb5rAsN6SwMyrYUyPAGAo5U6pfV9-movuBu-mbN2s2YYGVuJx_gmK4v6a0c2WTkVk0uRHJldek_lL4Wl0Vn31EcDnpklMrg9CyzFz3fmjAtW4p_ZL1rvvskNX3IdTwta8-2GKKnHeOprvdaprTObdTlb4nGLOaKu8s_O4v2T4VHnHoTZGb88JxTtPItH6pFmVUwb5iPPYTwxFE1rd8FsFguM3T1RQww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی را در چندین شهر جنوب لبنان انجام دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122508" target="_blank">📅 12:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=qmU4ql_0q7IHy4stfuZPrl-QfqrrGPyqU6kxXVun6m3BziNwMlbrLFZIuERlFmHX1hXGgjzjUKASQgh-p1WRJD93y1WtwOd1M1h6tJTD8gxcmYL_QKDrnBnrJQyqJmrhcdDWf5dafR5KWzJYJCbRZz5szOzKqbaQ5X8_TAynhL-PP2-YBv0307BhS7-aY_kN9Ycd03bXZYzN9jTxWo_9TmIsZqcUsjE3NFWJAkxIBIJ82vUBpgQX4uHaMly08khRp64MEJAZoR4sU_ohCNhO1AuQLHUWJ_UvGfD1kbYTF6D8QEpecx2q-dqsbevD7C63cBMR57w98KnvwRLBLIotCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=qmU4ql_0q7IHy4stfuZPrl-QfqrrGPyqU6kxXVun6m3BziNwMlbrLFZIuERlFmHX1hXGgjzjUKASQgh-p1WRJD93y1WtwOd1M1h6tJTD8gxcmYL_QKDrnBnrJQyqJmrhcdDWf5dafR5KWzJYJCbRZz5szOzKqbaQ5X8_TAynhL-PP2-YBv0307BhS7-aY_kN9Ycd03bXZYzN9jTxWo_9TmIsZqcUsjE3NFWJAkxIBIJ82vUBpgQX4uHaMly08khRp64MEJAZoR4sU_ohCNhO1AuQLHUWJ_UvGfD1kbYTF6D8QEpecx2q-dqsbevD7C63cBMR57w98KnvwRLBLIotCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
🔴
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم
🔴
ولی ترجیح ما توافق خوبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/122507" target="_blank">📅 12:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2989a06ab.mp4?token=bvDCeWclK0IeP-t0rGKECOu0zyWXp5YsWV7EQECmxx6BJYSSuISRPijYTh3pq8YY0xsiQfLIp8GF15iCj1Iwlk-e_R0yL2SpM7259kkqrUS5cYSofzL9zKHgB2k0kufKPgtTmFGcUGUTscVF9gmfdMNaW83WSdbFF5u3WsFLUDAfNmm8qVNV0sxDysf-6g3kY6gh0za73TLNlTr-NCeRsW6pCoBZgDDgWKQXFrbhvO6hEjlLA_DpnQTQJojwhpduAsdATzyr9j5wEJK32UMxMKWsRN1WsKPGYG0zFol0yJdkLGiVPVTaw-mIJ4kP9PibYGqBDBKoAfTci2z5Z9mIDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2989a06ab.mp4?token=bvDCeWclK0IeP-t0rGKECOu0zyWXp5YsWV7EQECmxx6BJYSSuISRPijYTh3pq8YY0xsiQfLIp8GF15iCj1Iwlk-e_R0yL2SpM7259kkqrUS5cYSofzL9zKHgB2k0kufKPgtTmFGcUGUTscVF9gmfdMNaW83WSdbFF5u3WsFLUDAfNmm8qVNV0sxDysf-6g3kY6gh0za73TLNlTr-NCeRsW6pCoBZgDDgWKQXFrbhvO6hEjlLA_DpnQTQJojwhpduAsdATzyr9j5wEJK32UMxMKWsRN1WsKPGYG0zFol0yJdkLGiVPVTaw-mIJ4kP9PibYGqBDBKoAfTci2z5Z9mIDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خارجه آمریکا، مارکو روبیو : هنوز همه‌چیز در حال پیشرفته، همون‌طور که گفتم فکر می‌کردیم شاید دیشب خبرهایی داشته باشیم
🔴
الان چیزی روی میز هست که به‌نظرم پیشنهاد محکمیه
🔴
درباره باز شدن تنگه‌ها، باز نگه داشتن مسیر عبور کشتی‌ها و ورود به مذاکرات واقعی، جدی و زمان‌دار درباره مسائل هسته‌ای امیدواریم بشه به نتیجه رسوندش.
🔴
این طرح تو خلیج فارس حمایت زیادی داره، داخل آمریکا هم حمایت میشه و تقریباً هر کشوری که در جریانش قرار گرفته فهمیده که این فقط یه پیشنهاد منطقی نیست، بلکه برای دنیا هم کار درستی محسوب میشه.
🔴
همون‌طور که رئیس‌جمهور گفت، عجله‌ای نداره و قرار نیست توافق بدی امضا کنه. باید ببینیم چی پیش میاد
🔴
ما قبل از بررسی هر گزینه دیگه‌ای، به دیپلماسی هر فرصتی برای موفق شدن می‌دیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/122506" target="_blank">📅 12:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
منابع خبری گزارش دادند که «بنیامین نتانیاهو»، نخست‌ وزیر اسراییل، فردا نشست کابینه امنیتی را برگزار می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/122505" target="_blank">📅 12:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ایران در دفاع از خود هیچ گزینه‌ای را منتفی نمی‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/122504" target="_blank">📅 12:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985125f801.mp4?token=SOZSSLWk4JynkWufm4ix_oYB19Jl7HHxJTNThC2cb5qQlVm5vGusGNlL45Au4GJvpxg22F71RJZu3ayTuX_gO2ZJQ8AYM7OXB7tJvRyDhqvDoayLw9gBeGC1tqu3Sb0qp4rkP1KADvYDhZ7HxIYBmmyZfl5To5SzqeUf2ows_eUcjHVmJ097SPs5YBKQCgnDC8pABYc113hjji4Io41POy2Gm7_pxPb9fjingQSN8Aj91WMJVrgZIc1gOMRWFa-FPyiNLZrrWwkiuLUV_l8z8lCsXcG9U3xkA_UMb7RsXK9yaH2yiTHaWdjuioigxVBwwZ_q81ZQt_mXwuMpWJYaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985125f801.mp4?token=SOZSSLWk4JynkWufm4ix_oYB19Jl7HHxJTNThC2cb5qQlVm5vGusGNlL45Au4GJvpxg22F71RJZu3ayTuX_gO2ZJQ8AYM7OXB7tJvRyDhqvDoayLw9gBeGC1tqu3Sb0qp4rkP1KADvYDhZ7HxIYBmmyZfl5To5SzqeUf2ows_eUcjHVmJ097SPs5YBKQCgnDC8pABYc113hjji4Io41POy2Gm7_pxPb9fjingQSN8Aj91WMJVrgZIc1gOMRWFa-FPyiNLZrrWwkiuLUV_l8z8lCsXcG9U3xkA_UMb7RsXK9yaH2yiTHaWdjuioigxVBwwZ_q81ZQt_mXwuMpWJYaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین
:
در جهان تنها یک چین وجود دارد.
🔴
تایوان بخش جدایی‌ناپذیر از قلمرو چین است
🔴
ما از طرف آلمان می‌خواهیم که اصل چین واحد را حفظ کند و ارسال سیگنال‌های نادرست به نیروهای جدایی‌طلب استقلال تایوان را متوقف نماید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/122503" target="_blank">📅 12:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
بقایی: برای تنگه هرمز عوارض نمی‌گیریم؛ هزینه‌های دریافتی صرفاً بابت خدمات ناوبری و حفاظت از محیط زیست است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/122502" target="_blank">📅 12:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه آمریکا، در شبکه تلویزیونی ایندیا تودی: اگر مذاکرات شکست بخورد تقصیر ایالات متحده یا متحدان ما در منطقه خلیج فارس نیست. ۱۰۰ درصد تقصیر ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/122501" target="_blank">📅 12:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122500">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
العربیه: اسلام‌آباد اصرار دارد که پکن نقش ضامن را در هر توافقی بین آمریکا و ایران ایفا کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/122500" target="_blank">📅 12:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122499">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بقایی: چین و روسیه نقش سازنده و مثبتی در تحولات منطقه ای ایفا کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/122499" target="_blank">📅 12:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122498">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فرمانده قرارگاه خاتم: سامانه‌های جدید پدافندی به کار می‌گیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/122498" target="_blank">📅 12:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122497">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بعد از ۲۳ سال، یک خانم (سمیه رفیعی نماینده تهران) عضو هیئت‌رئیسۀ مجلس شد
از مجلس هفتم تاکنون خانمی در جایگاه هیئت‌رئیسه حضور نداشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/122497" target="_blank">📅 12:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122496">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCMuf_xtYpdbz9dWtvCbzYtjIK_87zid1XeYCCKF6x_YS_rFlzF_wczcYanBkvizWhtU1qtFKcT2W-3hIy9zntyBXmHMLd9NLIwNjFOsUH5Fkd3y8VWrwAzPeXxw17kRmPvO6IUr7vupehNm0BTrqH45t2p6wF7JQ4uQnUdYBceJfcWTnMbfA6nNofj85gV8hLkTy-iXsxmP19wOzEV-YD8ySTsoYIjoNrRMwrkC0kZktJMBsAWK4wQ8mURZjFmQedVIrEYAEtagCIeBltDrbQcFx4hCJ8xicZGDRpYV5pZMhOVYNGRh9NSfO5eDSgV8xgnMxKOJVtI741DXQISexA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نت بلاکس:  اکنون روز ۸۷ام متوالی قطعی اینترنت ایران است که بیش از ۲۰۶۴ ساعت ادامه داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/122496" target="_blank">📅 12:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بقایی: حتما بخشی از پول‌های ما خرج موشک و پهپاد می‌شود.
🔴
اگر چنین نمی‌کردیم دشمنان ما می‌توانستند به مطامع‌شان برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/122495" target="_blank">📅 11:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: اینکه ما به نتیجه‌ای در بخش بزرگی از موضوعات مورد بحث رسیده‌ایم، درست است.
🔴
با این حال، اینکه بگوییم این به معنای قریب‌الوقوع بودن امضای توافق است، هیچ‌کس نمی‌تواند چنین ادعایی کند.
🔴
سیاست‌گذاری و تصمیم‌گیری در ایالات متحده دچار نوعی تردید نهادی شده است.
🔴
تغییرات مکرر در مواضع — در عرض چند ساعت با دیدگاه‌های مختلف، اغلب متناقض و متضاد مواجه می‌شوید.
🔴
این روند هر مذاکره‌ای را مختل می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/122494" target="_blank">📅 11:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تمرکز مذاکرات بر خاتمه جنگ است و در این مرحله درباره جزئیات موضوع هسته‌ای صحبتی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/alonews/122493" target="_blank">📅 11:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
بقایی: سفر آقای عراقچی به نیویورک به علت مشکل روادید منتفی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/122492" target="_blank">📅 11:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122491">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: فعلا سفر هیئت ایرانی به پاکستان برنامه ریزی نشده است
🔴
موضوعات شکلی، فرع بر اصل موضوع و محتوا است. ما الان متمرکز بر روند مذاکرات هستیم. اینکه بعداً به چه شکلی تفاهم اعلام شود یا امضا شود، یک موضوعی است که خب فرصت هست برای تصمیم‌گیری درباره آن در آینده.
🔴
اینکه هیئت‌ها باز سفری داشته باشند به تهران یا متقابل، بله ممکن است؛ اگر لازم شود چنین کاری انجام خواهد شد. ولی در شرایط فعلی، ما برنامه‌ای برای سفر به پاکستان یا سفر هیئت پاکستانی به ایران فعلاً چیزی را برنامه‌ریزی نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122491" target="_blank">📅 11:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122490">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: امیر قطر سفری به تهران نداشت
🔴
معاون دبیر شورای امنیت ملی قطر به ایران سفر کرد آن هم در چارچوب مساعی جمیله و تلاش‌های قطر برای کمک به پیشبرد تفاهمی که به میانجیگری پاکستان در حال انجام است.
🔴
میانجی رسمی بین ایران و آمریکا، پاکستان است و برخی کشورها نقش مثبتی در این روند داشتند برای کمک به حل موضوعات.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122490" target="_blank">📅 11:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122489">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
قسمت دارک ماجرا این بود که «منادی» خودش عضو هیئت نظارت بر رفتار نمایندگانه که وظیفه‌شون رسیدگی به رانت و فساد نماینده‌هاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122489" target="_blank">📅 11:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122488">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXniPoaUKRRyYQQejGaspeQArJURk01rr6i_rG78KUWVEHV8GYt_r7wA4-YuEvzNX-bqP8KrgcoCXhkQa7zAgeoxIX4Ted6Id2NpVtRtNZvTWGKKW5JCG0D0NykSj3QtzsOXGMe_eP_FX5k-ohc841JpqJiu3iHJ0wGou7Iozso8RZsUVHbNIsz0YitpshqFH6q3lZ3iibAXJjZRZZvvCzFoky8s_Axsu9lrs9XfwA6P-TvuT7svxi8Gv3Y1y-WKXysPt_Tff2jg1p3HSVRV8BL317Ai4oMvVcJ7uPoyOxqxc_ZAee33fKMcF8LLOyADshonMHuRjmU86l5KSmU11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کودتای رهبر بولشویک‌ها در مجلس جواب نداد
🔴
حمید رسایی سعی داشت انتخابات مجلس رو تحریم کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122488" target="_blank">📅 11:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122487">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
👈
تعداد آرای انتخابات هیئت‌رئیسه اعلام شد
🔴
محمدباقر قالیباف: ۲۳۵ رای
🔴
محمدتقی نقد علی: ۲۹
🔴
عثمان سالاری: ۷
🔴
رای سفید: ۵
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122487" target="_blank">📅 11:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122485">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiQc9kZomRgaigeknVx_wyUhSqOZ4T3Y-y9X0EzMRS1pBGebqK01v0cVeiTFuJufly_q4VWxB_mr_vAOXplspAYgETe6vQZcSDFoIjaQETX7I3PWKI0ahpLvi6-7vxb6LWgXeTU93KIsPFsBt7g_WzzlCLwJUiINYUyaGVnZfTjO0tNC0BmAZbb4bvci5G_QX1_1r_6ga4mx6GmFMhrE_bsujFJY3zLXD61iMlmm539hJ3iwMZb8bwGPf4cIWhans4AVWSn331GrgbhiyUDeDuBXGscqA1eeabMJhFD7coKVugTWL4FfJKUqMTqkG5gfy0Lry9-VoZn1MgX5R5IHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXKcEZlJlPpI25YlwB3-Kxvf-VQyJQ60CHSh_LXF8xtteW4kH_tC2iVAr1dDk9AiC5OsXo2WgkOSg6h3wLUwpEEtPL_78CAnK7BxdS4HFSmNcOk5OlY11d3Fyg0ILjQf-S9KO5RfB3J9_blcWuL9C-pM-0Oli8G6TuPpXNo7gXMEtQMMzFmEG6ppBN9gFKq1ELsyaNExrRsXJ9MPE_dBZ9rMLznctBDsGag1KrgwuATRSP8M1soge8O4Zpm3bK1drq8zDL2SKhv5b8G0SA_09FjpmsWHeT9tDxtz5-cWSulVLz9DneCWDXlQjIZta_lOmTun_1cn7wrSXns-j4YE3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خب منادی نماینده فاسد و پست تبریز که به نماینده‌ها وعده خونه داده بود تا بهش رای بدن، رای نیاورد و میتونه به عنوان یه نماینده ساده به فسادش ادامه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122485" target="_blank">📅 11:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122484">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
👈
تعداد آرای انتخابات هیئت‌رئیسه اعلام شد
🔴
محمدباقر قالیباف: ۲۳۵ رای
🔴
محمدتقی نقد علی: ۲۹
🔴
عثمان سالاری: ۷
🔴
رای سفید: ۵
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/122484" target="_blank">📅 11:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122483">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
مشاور وزیر قطع ارتباطات از احتمال دسترسی و اتصال به اینترنت بین‌المللی در هفته آینده خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122483" target="_blank">📅 11:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122482">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: این تحولات که در چند روز اخیر خبری شد، نتیجه چند هفته گفتگو از طریق میانجی پاکستانی است.
🔴
برخی کشورهای دیگر نیز در این مدت نقش داشتند. بنابراین اینکه در زمینه بسیاری از موضوعات مورد گفتگو ما به جمع‌بندی رسیده‌ایم، امر درستی است، اما اینکه بگوییم این به معنای امضای یک توافق قریب‌الوقوع است، کسی نمی‌تواند چنین ادعایی بکند.
🔴
تغییرات مکرر مواضع مقامات آمریکایی را شاهد هستیم. این روند هر گفتگویی را دچار اشکال می‌کند. با این حال، ما همانطور که در میدان نبرد با اقتدار عمل کردیم، در عرصه دیپلماسی نیز با چشمان باز و با در نظر داشتن تجارب پیشین برای صیانت از منافع ملی ایران کوشش خواهیم کرد.
🔴
کارهای مهمتری از پاسخ دادن به توییت های طرف مقابل داریم.
🔴
قرار نیست سبک و روش دشمن را کپی برداری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122482" target="_blank">📅 10:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122481">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تمرکز مذاکرات بر خاتمه جنگ است و در این مرحله درباره جزئیات موضوع هسته‌ای صحبتی نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/alonews/122481" target="_blank">📅 10:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122480">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
الجزیره: میانجی کلیدی آمریکا و ایران، به همراه نخست وزیر پاکستان از چین دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122480" target="_blank">📅 10:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122479">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/637c252247.mp4?token=pmUnXoC_ghEB7IuS_3OsfOMnj2vyipMk8dNU2bTfEmWuKr8lhFFfxK7sQyxkPEcpT0riMTpRj565DsK_QiBwOdFf0rHfuxVO3-YSzmoCyCr8FYmYjTQAtp-BMROwgmjoqwtl5kjz381X8_VXKnyi8U4sWJj5ho9CCQeILZO5AoEpAKfQvEFZka5LwkuHyg0pSEWYTqXSn8blam_Ax4EsTwGXzhNHPEi5QxUyEJVlvxW_W8aQ0VK2nyNm6NrcV17fG-XfRLkpQkLO1mNgNsuRCpr1mbrTDpe0d5QUYbcZE3hRqR4diVEVLpuXEYUikn7hx5IoUqd_wdeuWQWxu_D2ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/637c252247.mp4?token=pmUnXoC_ghEB7IuS_3OsfOMnj2vyipMk8dNU2bTfEmWuKr8lhFFfxK7sQyxkPEcpT0riMTpRj565DsK_QiBwOdFf0rHfuxVO3-YSzmoCyCr8FYmYjTQAtp-BMROwgmjoqwtl5kjz381X8_VXKnyi8U4sWJj5ho9CCQeILZO5AoEpAKfQvEFZka5LwkuHyg0pSEWYTqXSn8blam_Ax4EsTwGXzhNHPEi5QxUyEJVlvxW_W8aQ0VK2nyNm6NrcV17fG-XfRLkpQkLO1mNgNsuRCpr1mbrTDpe0d5QUYbcZE3hRqR4diVEVLpuXEYUikn7hx5IoUqd_wdeuWQWxu_D2ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از تیرباران مواضع حشدالشعبی در موصل عراق توسط A-10
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122479" target="_blank">📅 10:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122478">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpcJ8S5-VxhrI4UG_pmFRIniDJaPc1b_S6Ybcr2xpiLjuKp4eMd3MOOFrAd68wRFSVQ91YFIxil6WGR8DZpxKwBKu9xpUk9OIiwKtxNB0iWVdRc_o2ptMFMBybdKnQ851LQ7k70ASFjtgV4LcDo75uemTyXnszjLb73ckSGgcThrAwcmVClbEJ_FSJ_w7x4up61ch_Y9Gz1K3N5cIxQWKVgGu-f7abT3IYcNADV8Mqe5meL7k6983dVFieZxbqJiqhlPI9xl_7xifl9f2lEM9Ih82sBdjVjOxEJIk2-u-RWfBvRvxbyKgea2w2KugccHOuRnM7d_F4FrQlqD5g145w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل از کشته شدن یک سرباز در لبنان خبر داد: گروهبان نهورای لایزر، ۱۹ ساله.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122478" target="_blank">📅 10:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122477">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3a3zPk0aTLbtcrYeZmJnhaJLv1rxoZbKzDTspsQ58us5ymkt1hIgKwuWi2ffu1kEuqJJRLbHO3a0N5fw1B6346T6NRZHAPSZCJfQYSwGuBUDPCOdskG6EiD0DLD0JFEGHtxWqUxC265u86y6_yaTPTCl8J5_TVM01yNQYcaGSPhSuKyoDuxyH95yZge3O5bJEnp5-dm7kTAd2a3kPtIwPUMATTHCB3fNEFU64K2bPaPReC8ANpwouSDspNxt8NWcuPEwJcsYcjOGbqdC6U6qdLXsoiZsnOE8REjlOR40FSCeEDLbn3hf0o7zBWKd2aq9i6qExptj-bQ2HUUVp0jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:آمریکا منتظر بنزین ۶ دلاری باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122477" target="_blank">📅 10:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122476">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
انتخابات هیئت رئیسه مجلس که از ساعت ۷:۳۰ صبح امروز آغاز شد، دقایقی پیش پایان یافت
🔴
این انتخابات بصورت حضوری و با رای مستقیم نمایندگان برای انتخاب ۱۲ عضو هیئت رئیسه مجلس شامل یک رئیس، ۲ نایب رئیس، ۶ دبیر و ۳ ناظر بود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122476" target="_blank">📅 10:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122475">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی: فرودگاه‌های فعال کشور به عدد ۲۰ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122475" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122473">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZZ44_rnIsdjrQMNBTRL9xzzvPj93NA32bibcSD2HcmK2M_ilBMzoQurAau_3i10vtZhtdD1Rb-x6aGOrtyiZa6N14L44URDJnFsK3waqO08jhgR4Tm1HJkI0jG7_6sGatFfBUe5yxtL4rgntHt1WVMKY8sUkS68rkHG4mrqarUA6m_1-z1Vt7dJ5Q9cTTfzW9hF9m-MqJVe98S7i31HuO_KeQd3iTwj4Q8DwceH0CGHuwvv_knD_P8wGaKodDLUR55BYOpHJ7NsQKU3eDKfX0s8Ue6-zzD55TIlX8rALilhTVn-ASR6oH4EHdCI5iobybXaPYcx_ZdOXmBfR65Gqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6uZMHNoccHDiEl7FDNjE0xYfEj7rGMAy4A-3Crbm9GdbtYZ3w4RjKp4-KT65mDYF5nxDLb11u2j0g1ylw_3Mh9wS1ozz4N5w6u7QwJf_1zhAPDlj-gwNagwKtZmz4GE-PHvjcVnXIk1lW6s_wLnuwqBTWsvajoJuBq9ZteHWbS661Z_HDhogrnsi83F3TVQ3A6xVhqDQ5RTVimUZailWG_xg0kwY89awXQtep87888oZY7_5l7atocL3wjnPm6qyCLdORminWyuEQ9q4sPXFo-17qkPXfEu-Q9ck8txpZa-XBzIv2xU8xUEehf9lhW728jQYCI0CCZebdeVaA6ehA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قاضی صلواتی با رد حکم دیوان عالی در پرونده کشته شدن بسیجی آرمان علی‌وردی در سال ۱۴۰۱، گفت بخشش نیاز نیست و حکم اعدام ۴متهم را صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/122473" target="_blank">📅 10:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122472">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
وزارت امور خارجه چین: جنگ ایران هرگز نباید اتفاق می‌افتاد و نیازی به ادامه آن نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122472" target="_blank">📅 10:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122471">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
گزینه‌های نظامی ترامپ برای شکستن بن‌بست با ایران پرخطر، محدود و در نهایت ممکن است به نفع تهران باشد، که طبق گزارش فایننشال تایمز، نقل شده توسط ایران نو، چهل روز بمباران را بدون عقب‌نشینی تحمل کرده و از آن زمان تنها موضع خود را سخت‌تر کرده است.
🔴
از حملات هوایی تا عملیات دریایی، راه آسانی برای مجبور کردن ایران به عقب‌نشینی وجود ندارد و حملات جدید خطر کشاندن واشنگتن به باتلاقی پرهزینه را به همراه دارد.
🔴
ایران از روش‌های جنگی آمریکایی‌ها آموخته، در حال بازسازی دفاع هوایی آسیب‌دیده خود است و ممکن است از چین و روسیه سلاح دریافت کرده باشد؛ می‌تواند با پهپادهای انتحاری به نیروهای آمریکایی در هر دور جدید درگیری حمله کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/122471" target="_blank">📅 10:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122470">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجارهای کنترل‌‎شده در محدوده شاهین‌شهر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122470" target="_blank">📅 09:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
مرندی: نه به توافق با ترامپ امیدوار باشید، نه نگران عدم توافق باشید، به مذاکره‌کنندگان فرصت دهید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122469" target="_blank">📅 09:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
انتخابات هیئت رئیسه مجلس که از ساعت ۷:۳۰ صبح امروز آغاز شد، دقایقی پیش پایان یافت
🔴
این انتخابات بصورت حضوری و با رای مستقیم نمایندگان برای انتخاب ۱۲ عضو هیئت رئیسه مجلس شامل یک رئیس، ۲ نایب رئیس، ۶ دبیر و ۳ ناظر بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/122468" target="_blank">📅 09:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مارک لوین: ترامپ اعتقاد دارد که رژیم ایران را کاملا عوض کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122467" target="_blank">📅 09:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
عباس اکبری، یکی دیگر از معترضان بازداشت شده در دی ماه، امروز صبح اعدام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122466" target="_blank">📅 09:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ارتش اسرائیل: به ساکنان ۱۰ شهر در منطقه نبطیه، جنوب لبنان، هشدار تخلیه فوری داده شد
🔴
اخطار شامل شهرک های نبطیه الطحطه، لویزه، سجد، عین قنا، حروف، کفارمان و زبدین است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/122465" target="_blank">📅 09:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ارتش اسرائیل: یک هدف هوایی که از لبنان به سمت عرب العرمشه در جلیله شلیک شده بود، شناسایی، ارتباط قطع و حادثه پایان یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122464" target="_blank">📅 09:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فایننشال تایمز: عصبانیت رئیس‌جمهور چین از «افزایش توان نظامی ژاپن» در حضور همتای آمریکایی‌اش
🔴
پاسخ ترامپ: ژاپن به دلیل تهدیدات کره شمالی، به دفاع قوی‌تری نیاز دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/122463" target="_blank">📅 09:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUGtK5tMr829jruQqF4pUJWybSQWApfgeMeqcgpSIA2fcCRWmoCzPz4DRbfjM0OMDhXyX9smW2gKv0lf81BaRJq2Ky8rkjLvwmLQ_rJee7y3YpcTKzXy3M9d-yQRYpurFrli3d4cL_DmN01KDNAp050gvo5XMl-ML7KNcwOaYYkGnWT2BmZw1BQi_ooQKQVl1Y0DJoTKcSirv5Qx51cejQqta4B28d5Jp3fhMOl0ljFI8h_abuOwxBH3wF_-p6INoKuE7mAv2uB4SE8kXz-H9FEyhO2V4t0ZRpUPEA6veYguhoyNL4q9ZwAK0XAdJe2XbiZMuDgtnT68K7Raqi1MWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی
:
تماسِ نتانیاهو با ترامپ کافی بود تا سیاستِ جدید آمریکا به «بدون گرد و غبار (خروجِ ۴۰۰کیلوگرم‌ اورانیوم)، بدونِ دلار (مُنتفی‌شدنِ آزادسازی اموال بلوکه شده ایران)» _No Dust, No Dollars_ بازگردد!
🔴
آمریکا تصمیم گرفته دلاری از اموال بلوکه شده کشور را تا به «خواسته‌هایِ هسته ای آمریکا» تَن ندهیم، آزاد نکند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/122462" target="_blank">📅 09:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز: رشد شاخص سهام در ژاپن در پی توافق احتمالی میان ایران و آمریکا، برای اولین بار از آستانه ۶۵ هزار واحد عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/alonews/122461" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
مدودف: اوکراین عامدانه به دنبال به راه انداختن حمله گسترده به اهدافی در کی‌یف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/122460" target="_blank">📅 08:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4cgtxOuh_Bav05Q-o88uiN_zhH31r8DCNS6G8Bvjy6IZb7KgiH91ksHblpuAI-mhzQep4U6yz9YD3-cNcvnGMNYteFxOA0e8eIWp44W06JgdvLKT5m-Z_OIkHjY8EK_V3wIdH3XnBXCDedlwauUl1WcdZzz3Wwul1zLUGtLaR_VxB6nnAaq_aSZFFUxlO2p4k3KEpqm_H-B61zrxaN0WFgrQSvhfVwyUDDxAb8mLsB0wvQjccxCPYHxDmdfoSp0NDTtWfDI5zs4-2sUR6lEzTsT3ZGQKpqKAh-jjKFgumwrAwWVoG8YvAILCychSNSBV_ImRcNV7wd9mxMq5I7j1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: گزارش‌ها حاکی از آن است که عربستان سعودی از دونالد ترامپ درخواست کرده است هرگونه حمله جدید به ایران را تا پس از حج به تعویق بیندازد.
🔴
همچنان ترس وجود دارد که اگر درگیری دوباره آغاز شود، زائران در آنجا گیر خواهند افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/122459" target="_blank">📅 08:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89b8e994e.mp4?token=BIrzxA_lr2sVYrAfe0JJUujCABUvRJ7MJPNvWYD4wHGVpecAhEyZH331-dFgoRpjLFGIYm9ZSjtN7CAaNW72eLSITKl1OaHT_gEIUdoFZuX_Iw8VsZWuMPkdUGqzoqElEWBLd_qYgIhJCsB4-skFjq-I5A9U9Ie2VMhQljkzNNOoDTq3Nh6zTirUJmA3N6CHcuXGzd9ER3OtNTHWpfJnVTC6lZ_vGg54F5X4BIkYl03hYcjFvImPwBQ7Ea0ANcaM3LvUsicIn-eVPQAvbHHcaRFVFII3VJxsHjgPcZT457LJT5MmbdMb507CxiDNN9wGf6NFpqJWRQ8Jh89AEpNyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89b8e994e.mp4?token=BIrzxA_lr2sVYrAfe0JJUujCABUvRJ7MJPNvWYD4wHGVpecAhEyZH331-dFgoRpjLFGIYm9ZSjtN7CAaNW72eLSITKl1OaHT_gEIUdoFZuX_Iw8VsZWuMPkdUGqzoqElEWBLd_qYgIhJCsB4-skFjq-I5A9U9Ie2VMhQljkzNNOoDTq3Nh6zTirUJmA3N6CHcuXGzd9ER3OtNTHWpfJnVTC6lZ_vGg54F5X4BIkYl03hYcjFvImPwBQ7Ea0ANcaM3LvUsicIn-eVPQAvbHHcaRFVFII3VJxsHjgPcZT457LJT5MmbdMb507CxiDNN9wGf6NFpqJWRQ8Jh89AEpNyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو
:
باید به یک توافق خوب برسیم در غیر این صورت مجبور می‌شویم به شکل دیگری با ایران برخورد کنیم/ ما ترجیح می‌دهیم که توافق خوبی داشته باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/alonews/122458" target="_blank">📅 08:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122457">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رویترز مدعی شد: دو کشتی حامل نفت و گاز طبیعی، تنگه هرمز را به مقصد پاکستان و چین از طریق مسیری که ایران به کشتی‌ها دستور داده بود، ترک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/122457" target="_blank">📅 08:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ادعای روبیو، وزیر خارجه آمریکا: امضای توافق با ایران روز دوشنبه همچنان امکان‌پذیر است
🔴
پیش از اینکه گزینه‌های جایگزین را بررسی کنیم، هر فرصتی را به دیپلماسی خواهیم داد.
🔴
احتمال قوی برای ورود به مذاکرات زمان‌دار درباره پرونده هسته‌ای ایران وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/122456" target="_blank">📅 08:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmWkEOxYNPNu2rFtIpJKB-dlW_Plr1U4hgTrQeZyv6VdhMMo2a8_768K5AK29_iVF7Mi8dxPCmovWcqf04g8fsELPOYwqA0vSO_T7nwT-sUVrDR16IxlSoablUfh-yLo-JpbbPMnagMOwANyrAxIBLK_I75w_8gmnL9aZKL0TZNsIAQOZgDZqZmDSVrT9v3rVNijx_IWbEswyxYJ68jnhXa5bnx2yPwNnPt2QwrCJj1QWKvWcdg0EAAvxiKodI6HHWzOAkDpU4TvlETgQ4ZWzQNEai6y-mda4khClXNfpNKQe1EdzTLwznftFFviBZ1l95NNsIR7WNFBPswbWtyhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ رئیس کمیسیون امنیت ملی به تهدید اتمی ترامپ: قابلی نداشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/122455" target="_blank">📅 08:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هم اکنون هر بشکه نفت برنت 99$
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/122454" target="_blank">📅 01:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1GkbcPuMcbci7mCbmZlntHoP8Sx_i2kOra49h9bpmOTxQPVTFopdMS0xDyAYJlghFSc4KRtsPmtQKBakMstP6953xbeJudb3Unn6fRszyPbLUJLHxUg-gz5i8D61aFcev27_27pkUCTyqF1zR0yDPRoZ8V6SYvw49LhOBdIolRi8Gk6acbA9DCkd-WWzn09A-_ymSSl8V1iwEvzY8_LaXVZUx1k68Nb-qcE2O1785YjTtvrEukuKHxALpg5FvERHR5HTYKCX0y_Z6k76ByYMVpODEMML7G9l-jWXssu8Mwv_rhX2ORd7hiRvb0inHp2MT6miSONsCzhqfgG900Rsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: قیمت نفت در آغاز هفته جاری در بحبوحه امیدها به توافق بین آمریکا و ایران، 3 درصد کاهش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/122453" target="_blank">📅 01:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ntT1-8vCe8HXCdZnZ26dfnVfrkav7PpoqJ6KCA_IvHB6d2C0mc47Ov38uKjNuMNFAT-108BrxQyk4FWfCw6WPrQLXdW1tKRyC196A3zJCZUigM8B3nMRVWTURmmaNYh8-RWMG_fVilVXXhQf9zmcS74_Y0iMzmqrdg5dfbDPBPDcLDa7mL893q2p987z4OdT38nH8Ur0RMUW-r4tmPx1nyAehGsxoD6JE-6Gh-xBnlMuaVrD0NbBF17qPtagrXpnKpQgr-ewc0uNH0zbs8PKIyEeHpq9he0sFSY2Xja4dhG_EicBcEsZtjDkxGfaF0lp1r6cnnOk_C1OTigGdWUQaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکنون یک هواپیمای هواشناسی و کنترل هوایی (AWACS) بوئینگ E-3 سنتری نیروی هوایی ایالات متحده نیز بر فراز خلیج فارس در حال عملیات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/122452" target="_blank">📅 01:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💢
فوری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/alonews/122451" target="_blank">📅 01:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: آمریکا و ایران به توافق اولیه برای بازگشایی تنگه هرمز دست یافته‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/122450" target="_blank">📅 01:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نشریه آمریکایی پانچ بول نیوز:
کاخ سفید از قانونگذاران جمهوری‌خواه خواسته بود که آخر هفته جاری در حمایت از توافق با ایران توییت کنند.
🔴
به گفته دستیار ارشد یک نماینده جمهوری‌خواه، برخی این کار را کردند، اما برخی دیگر «از این هراس دارند» که پس از پایان تعطیلات مجلس، مجبور شوند از این توافق دفاع کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/alonews/122449" target="_blank">📅 01:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نیویورک پست:
ترامپ نظر خود را تغییر داده و احتمال توافق اکنون به طور قابل توجهی کاهش یافته است؛ تماس ترامپ با نتانیاهو تأثیر بسیار زیادی داشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/122448" target="_blank">📅 00:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56627faf8a.mp4?token=MwVnjxI-g5nwP3be-4LVG32w041mc9EsG2fjQO8vAHLee6AZ0RyjI3eDJWle7WqkCU9XtS1dsHKOAauYYgbunh5iq_cZa-OBtbX8rOZoV7hfHaj3olsFu3XY0mOqKK7RYvPhDHBaJzRU7KHipZ5asuiGKzbCMBCnW2D-tW7g1T9bbDkAk27OTkRUhx0o1WqwLJ2GCp9_Drr-DlclAXhX9ylv-IIICqb5WfOj53wUL3fa3M4MBQGMOZ33_B-_DJhqYcy1aOtz_DWHUFg91ngW0AK6lsllUH5g914-DsViPe3-yxVWeQ2eVqqfui8P7LX_qBaAMfiIePPBhRHfghem4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56627faf8a.mp4?token=MwVnjxI-g5nwP3be-4LVG32w041mc9EsG2fjQO8vAHLee6AZ0RyjI3eDJWle7WqkCU9XtS1dsHKOAauYYgbunh5iq_cZa-OBtbX8rOZoV7hfHaj3olsFu3XY0mOqKK7RYvPhDHBaJzRU7KHipZ5asuiGKzbCMBCnW2D-tW7g1T9bbDkAk27OTkRUhx0o1WqwLJ2GCp9_Drr-DlclAXhX9ylv-IIICqb5WfOj53wUL3fa3M4MBQGMOZ33_B-_DJhqYcy1aOtz_DWHUFg91ngW0AK6lsllUH5g914-DsViPe3-yxVWeQ2eVqqfui8P7LX_qBaAMfiIePPBhRHfghem4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش‌بینی‌های کاملا دقیق و حرفه‌ای نوستراداموس زمانه؛ استاد خوش‌چشم تحلیلگر صدا و سیما.
🔴
فقط اینطوری کار می‌کنه که هر چی گفت، باید برعکسش کنی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/122447" target="_blank">📅 00:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qyzpw32t_GGuPBZ_r88TjoSwv17wHAFwgKnTLplfvKf_AGJZchizzr-0iVuFvUOsmpk5yZviLujrZhHOM_q5cBUUXaRoLXvTP4O9mRXqp0oNaqRccMEmg98P9VGI6gnK3gL1cu1IVQzSqYinqmzrdnpyse-AZsXP06HsC3kx7Jg_T6l_T_5yVD35Zjb0GrphvYArUXryrCXAJmsybvwveSIZRetSQYBA-fnLAUPLZYWZrmWIOP9MUkbAGKvwrDSM8nzNUboITAg9sF2hUr9uY3dwQEVV2mBvKpzZgVYIFbD3HAxnCC1ItL5n3e1-xWTSt24DEBYhBRZ8ccrvKNt8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی : دست روی ماشه هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/122446" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
کانال۱۲عبری: نتانیاهو در تلاشه تا توافق رو بهم بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/alonews/122445" target="_blank">📅 00:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
تسنیم به نقل از یک منبع مطلع: تا این لحظه تفاهم نهایی حاصل نشده است و چالش در بعضی بندها ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/alonews/122444" target="_blank">📅 00:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqDXq7nErn2CnoysBPYDFYCuaVaAHzJFyeuBa_L0iB46jVFWcxn8V591IEWWPKqSCT67JA8c8-ISuBkuD5esynrk0ge0BjiUbfsjapdoqw6XAtsDRadGTuqEfA_fTdW5tyoyzq19BgAwY2XIhSk_ZBsOEciwYWIHrvqCT8ROvvu0s0e55ro092Hl9nf7v0L5NZLs930pHSAnSgbw9nDRtfqHLeOFDvS423WzWIUH-msoUgp82DkJtGtmUnh-rOATivWv6akLYma3vq-yKvO9JFIUGmvkO2BslvAk9ModIwp5EAwHyY7Kf9DCIamqR_KF7ajvNy8OuORbUXXwYT1Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییتِ سخنگوی فارسی زبان ارتش اسرائیل
!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/122443" target="_blank">📅 00:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
همزمان با سفر رسمی نخست وزیر پاکستان به چین، دو کشور تفاهم نامه‌های همکاری به ارزش هفت میلیارد دلار امضا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/122442" target="_blank">📅 00:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت خارجه قطر: وزیر خارجه قطر در تماسی با وزیر خارجه عربستان، درباره تلاشهای میانجیگرانه پاکستان گفتگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/alonews/122441" target="_blank">📅 23:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فیلمی که پیامد حملات هوایی اسرائیل را در شهر دویر نشان می‌دهد که منجر به تلفات متعدد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/122440" target="_blank">📅 23:48 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ae03c828.mp4?token=YAlzkOoM3jKklFlxc5Kex67dzcKtDtkNkghFimW5y68xd3QrlegmaIqfsSZkhc_lA7dnjw-5zmN64Lz6s61kk0ho48Q_MyvuDT9KELI_KQlHf6yb-46XUC7rZfCrKAzlc8uq8sKepZv6BO44NumA3c4kc6tO9H-J-RHzzUis28u9r2UfWzFLyPhc2GV96H9mNFtdvA_NFotJLfjJtvhN9OTHXFYzscIHQKDBs1HLFaCMhnKGVeYQ2NJAtxGyNP8GyKVP99y2jMyD0ZC4GVWljugBSjZ848UzL4UNNtnlgkOB9_1qzzl_C5pLAP1xwJ_eqYLOMR6cD0BP8aSGrg1b6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ae03c828.mp4?token=YAlzkOoM3jKklFlxc5Kex67dzcKtDtkNkghFimW5y68xd3QrlegmaIqfsSZkhc_lA7dnjw-5zmN64Lz6s61kk0ho48Q_MyvuDT9KELI_KQlHf6yb-46XUC7rZfCrKAzlc8uq8sKepZv6BO44NumA3c4kc6tO9H-J-RHzzUis28u9r2UfWzFLyPhc2GV96H9mNFtdvA_NFotJLfjJtvhN9OTHXFYzscIHQKDBs1HLFaCMhnKGVeYQ2NJAtxGyNP8GyKVP99y2jMyD0ZC4GVWljugBSjZ848UzL4UNNtnlgkOB9_1qzzl_C5pLAP1xwJ_eqYLOMR6cD0BP8aSGrg1b6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی که پیامد حملات هوایی اسرائیل را در شهر دویر نشان می‌دهد که منجر به تلفات متعدد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/122439" target="_blank">📅 23:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه «فاکس‌نیوز» گفت دونالد ترامپ، رئیس‌جمهوری آمریکا ممکن است به ایران هفت روز مهلت دهد تا به یک توافق «قابل‌قبول» برسند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/alonews/122438" target="_blank">📅 23:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
نیویورک‌پست: احتمال رسیدن به توافق بین ایالات متحده و ایران به طور فزاینده‌ای کاهش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/122437" target="_blank">📅 23:37 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به طور خصوصی اذعان می‌کند که اسرائیل در حال حاضر توانایی محدودی برای تأثیرگذاری بر رئیس‌جمهور ترامپ دارد و فشار آوردن به رئیس‌جمهور آمریکا دشوار شده است، طبق گزارش کانال ۱۳ اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/122436" target="_blank">📅 23:36 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
