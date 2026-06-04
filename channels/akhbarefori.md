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
<img src="https://cdn4.telesco.pe/file/JdMi9JV36DLpvEf5klHmupy0B3KUsp23BwKuBSo41U1KuiIAeOhyqPkeuzOydAcadUH9EbnNWkatbZbTHcSWhsD6OiKckGFcgdD2tTB4oOQCdxC5vL_8xBvkcsatyjQb54IV5E1sUUFvNlYqjl6X5T2jJ63jTG9PlC_tmLOvFM7nbPqEGtUApSw8v_fLZ02MQJUp_dqBkW79UI22_HcM4vR-6inq-0JDjDWDuFvtnbH5J5x-IuXYZrv7FK5Uc1ITRinyVRdJ8mmCgzc3aH9Ilqs2lZpv_MEg36nOiVwBLDX3xA7ObZ8KgNF0INAkKeRHxWtJrprEbyILGmcalMuOWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.15M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-656087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش مبلغ کالابرگ در چه صورتی خطر ندارد؟
کامران ندری، کارشناس مسائل اقتصادی در
#گفتگو
با خبرفوری:
🔹
باید دید مبلغی را که بخواهند به کالابرگ اضافه کنند، از کجا تامین می‌کنند. اگر از بانک مرکزی یا شبکه بانکی بگیرند خیلی فرقی نمی‌کند.
🔹
اگر از طریق خلق یا چاپ پول این مبالغ مربوط به کالابرگ را دولت تامین کند، آثار و تبعات تورمی دارد که فوری نیست و در اقتصاد ما نزدیک به یک‌سال طول می‌کشد تا تورم ناشی از خلق پول اتفاق بیوفتد. اگر از محل درآمد مالیاتی، ارزی یا فروش اوراق این وجوه تامین شود، آثار تورمی ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/akhbarefori/656087" target="_blank">📅 17:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJnZDd3IKDkOH4uduM-C9CbR4kMiAhIhJXBs_zTHb-xEJ9BwYdl6n5qzVa0oB84dSGcf1Fp70OfwoUs-3zIdIEEkMPtPGeAVrisEL-Hu-1MaK5f9Fz5VbLc9hStbYEj2NTq5WBURtqPuNUNEuE8XviC7iwdV_F_8hyfGz7KC2rZIwIU1s5p4n6Et-ARfR2sGZGASypmtrzPAztvsBwH8uZW7DpK5CzWiHWge50aG5XuZGhSpQ0GW5q_RqVm7Q_fvkzdqdn6rWa4P0aHR8JLG6COH6wc_GpGCPgCRUGBHLg37b2ph5bVAf7vhzhUUuyMy5iMvUwi7h19BYJs-LXtp5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نقشه‌ای از جهانِ غدیر؛ از نجف تا پنج قاره، یک پیام و میلیون‌ها دل #جهان_بر_مدار_غدیر #فقط_به_عشق_علی #LiveLikeAli #VoiceOfAli
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/akhbarefori/656086" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV_yUNbUKsIn6dwLg9UBLhtmR6O1jDuA1Xa0tYK8ci1pI1trl1IncmwKln_YPM4SCS-iSAzE7qF_TAqQI_x0-JRS_zSUWnpJDmS38x5iUSKtMnhcfszDkf3njZfrAJPVlYVpvaZ9tTPiujpi6lIW8VCKgC7gEltkKAWHS6iODd8A_qwst8kgHhPY06qemYliYpvxNv-Ex92Sk1B2NOb_T1ClpGyJ6jDPARwVXCy2Qe8zcXzkbV8QZsQnzZ0uTuDqLrQHthTr9ZS5Ujy5hU-GhSOn2n8trZyu815cH9KNNK2JCLFcisIlrKsuKxqblkJsKg5IylYMPfOgAaGqgZ0wyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مذاکره استقلال با اسکوچیچ/ چند مربی دیگر در فهرست آبی‌ها
🔹
باشگاه استقلال برای فصل آینده به دنبال تعیین سرمربی است. در صورت «فریز» شدن لیگ، قرارداد سهراب بختیاری‌زاده به پایان می‌رسد و آبی‌ها سراغ گزینه‌های داخلی و خارجی می‌روند. در بین گزینه‌ها نام اسکوچیچ هم مطرح است؛ مربی‌ای که قبلاً هم مورد بررسی استقلال بوده اما توافقی حاصل نشده بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/akhbarefori/656085" target="_blank">📅 16:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78d7f591a3.mp4?token=d4-LjfstopLymRneAJ4t3boR-qqIZTL-0sjiOktocBL02CAZtQu8wQfR8HvLyyemT2aC4cbWJKtQJ0g7ssxQY9Ks_A91ll4qvcRxO5ktCkF_MNVMhENmuDK9GsWnTonxTRymgqYvhwvClNFVyOkT0GC64Q_7Ime-sUc_-s0yfnnPGT1Rn3oW6yIN3lhMsEoAwvd_dDXjJv8EvfdiGCIOKgIjXgucUvO4nK0zj44NUQlAYE15OTYoZ-btPxOHpED1l4FXzucrP-Tdxv2aB2EXU28onsg0nIiFKQFOtYrmvtuG1GpMrIMqGp3jXR0vQ0bMw6RT2G5ylGdI3nOyIEPqAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78d7f591a3.mp4?token=d4-LjfstopLymRneAJ4t3boR-qqIZTL-0sjiOktocBL02CAZtQu8wQfR8HvLyyemT2aC4cbWJKtQJ0g7ssxQY9Ks_A91ll4qvcRxO5ktCkF_MNVMhENmuDK9GsWnTonxTRymgqYvhwvClNFVyOkT0GC64Q_7Ime-sUc_-s0yfnnPGT1Rn3oW6yIN3lhMsEoAwvd_dDXjJv8EvfdiGCIOKgIjXgucUvO4nK0zj44NUQlAYE15OTYoZ-btPxOHpED1l4FXzucrP-Tdxv2aB2EXU28onsg0nIiFKQFOtYrmvtuG1GpMrIMqGp3jXR0vQ0bMw6RT2G5ylGdI3nOyIEPqAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران بنزین در عراق
🔹
منابع خبری از وجود صف‌های گسترده و طویل در پمپ بنزین‌های چندین استان عراق از جمله صلاح الدین و بغداد گزارش می‌دهند.
🔹
مسئولان عراقی اعلام کردند که این بحران موقتی است و به زودی مشکل کمبود بنزین رفع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/656084" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=vi5Nr8sUjii9rlW6thvqeYDsurCSM-uW70QTD07SSaHgAwNkO-PgGXSR8BWaLizMtWK01-83RPald8XXRRq9PSBjv4q3dOUgv-jR3d1Y5WbRTihhNM2rR0bAO6sTv_p6uwdhfb2z6-zE8mWrwKP__5uQuBxCbkMTKht6C37GHMbOlkNEn-9zI7SDzZUfDe8ewqdFFy6dmQ5Wy2sFedCq1xR_nZcY9bHtphMlLbKo9gkMy82nu0hSwlpX5g0HPl-GbwKyB9OEE-e5LXO5HFiVpBXj-foJwMfDZs_y0QgKYD0DDLg1m9Twy1eBjMB-MxXiRqv64qCZRiZf3wiycn8GZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0631d4a758.mp4?token=vi5Nr8sUjii9rlW6thvqeYDsurCSM-uW70QTD07SSaHgAwNkO-PgGXSR8BWaLizMtWK01-83RPald8XXRRq9PSBjv4q3dOUgv-jR3d1Y5WbRTihhNM2rR0bAO6sTv_p6uwdhfb2z6-zE8mWrwKP__5uQuBxCbkMTKht6C37GHMbOlkNEn-9zI7SDzZUfDe8ewqdFFy6dmQ5Wy2sFedCq1xR_nZcY9bHtphMlLbKo9gkMy82nu0hSwlpX5g0HPl-GbwKyB9OEE-e5LXO5HFiVpBXj-foJwMfDZs_y0QgKYD0DDLg1m9Twy1eBjMB-MxXiRqv64qCZRiZf3wiycn8GZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
حنظله: مدیر ارشد موساد در عملیات بمب‌گذاری به هلاکت رسید
گروه هکری «حنظله»:
🔹
یکی از مدیران ارشد «واحد نفوذ جدید» موساد در بخش مرتبط با پرونده ایران، در جریان انفجار یک بمب کارگذاری‌شده در خودروی شخصی‌اش به هلاکت رسیده است.
🔹
این عملیات پس از ماه‌ها رصد اطلاعاتی، تعقیب و مراقبت مستمر به اجرا درآمده است.
🔹
حتی افرادی که تحت شدیدترین تدابیر حفاظتی و امنیتی قرار دارند نیز در سرزمین‌های اشغالی از دسترس مقاومت مصون نیستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/656083" target="_blank">📅 16:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
زمان صدور احکام جدید حقوق بازنشستگان اعلام شد
‌
رئیس کانون عالی بازنشستگان کشور:
🔹
احکام جدید حقوق بازنشستگان تأمین اجتماعی برای سال ۱۴۰۵ حداکثر تا ابتدای هفته آینده قابل دریافت است. مرحله سوم طرح متناسب‌سازی با هدف تحقق ۹۰ درصد همسان‌سازی حقوق‌ها، همزمان با تعیین حقوق سال جدید اجرا می‌شود. این احکام برای بیش از ۵ میلیون و ۲۰۰ هزار نفر صادر می‌شود.. / فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/656082" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Sejjeel</div>
  <div class="tg-doc-extra">Meshki X RaaSaa X Mofleh</div>
</div>
<a href="https://t.me/akhbarefori/656081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
سجیل
موضوع ایران باشه همه قشرها متحدن
تو رو چه به شیرهای ایرانی آخه سگ زرد
#آهنگ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/akhbarefori/656081" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b67ba91.mp4?token=U6VIaRS5tanwmdkTSf49SFLsmKn4JnCBaZn_Ueke4cFtWzLdK6NhkzQ4a6BdwpgspMogHNM1KU4EYMko79uNGj29K2AAqRhsB6l2ePn5ONWLCtESpHvGP1T4x2WQA1Uw-sxCZvZjWRkAAH3SbGVTWQSoOKvWotdq-7wKfJtTW96KIPCnKwIq_3KrnYutZASwN-zN16tE4PyF6BbVvwSffrukR5Tl5lZz4dhPzXhF5a0JP6MqlyKzifoBsvXpMIJD1GMlJ6u9Lr6TjMxjfZGLC_wQgZ19o3Ap2wjz3tfzRPiB8HpJDKjo_Fy1XimfQMw4-OiJWskrjNRE7KNY52Iwtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b67ba91.mp4?token=U6VIaRS5tanwmdkTSf49SFLsmKn4JnCBaZn_Ueke4cFtWzLdK6NhkzQ4a6BdwpgspMogHNM1KU4EYMko79uNGj29K2AAqRhsB6l2ePn5ONWLCtESpHvGP1T4x2WQA1Uw-sxCZvZjWRkAAH3SbGVTWQSoOKvWotdq-7wKfJtTW96KIPCnKwIq_3KrnYutZASwN-zN16tE4PyF6BbVvwSffrukR5Tl5lZz4dhPzXhF5a0JP6MqlyKzifoBsvXpMIJD1GMlJ6u9Lr6TjMxjfZGLC_wQgZ19o3Ap2wjz3tfzRPiB8HpJDKjo_Fy1XimfQMw4-OiJWskrjNRE7KNY52Iwtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عصبانیت شدید تحلیلگر اسرائیل‌نشنال از ناکامی آمریکا در براندازی حکومت!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/656080" target="_blank">📅 16:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6hA98zQIfuV8cx6zH5wkcxMtMIK5IWx9Ahi3gFIPE6G47subTRMKxHg9ijOCyZ0VKeD_C1HUxBf4zhSYFZFWGU0Xcdhh7L-p9ZQ4BtWLnmzZpL5rL9WVGpUCMCR0EmPEQFwwHx9-7tlBUnSct9-REkzYQvpf-JgtVwT1-WYoQRw167cd_4OIYqIwhn6SvXrMGBd4Y_KEhfCoXI8XZUKunmKBpV24q6gKgUs32wm-OGcEZn-pd1Ne1OuESYQ4SpVo4fBY039KgJ37Z0HVGRiXD9c24hO_5alBJhxpY9qraC7H2k-VDHJ1Gg96WcEvPufHQR-Cqj9UZg1ug8-aoR1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/akhbarefori/656079" target="_blank">📅 16:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656077">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVj7ncznE-6VSV0DlXCnevr2vQv4PLb427-AsOOomoHp9dI1Ol4GmuovVDIz-dpta8nuN4s64kwf6F7uXo7pUMdQ19v5hmFI2r45_HODUYOp9eN-RF0IQkZ4YT3t0c3nL-Eq0_s_llutzq2-kfdgm1DeuWm9Deze2wVFjGERhxYvpPa1QkVIMoX1vGX3EPWosLKb5JjOUX0pBkFEYM3z5HJgPo2sygU-WSuhqpa1s299BXjCENvlbAqqccDx7Coog1eujdXwA96KhWgcig-cuR0ZEsc31Vg0jQFKfi3-hHrMLEvQX_udt8Zhc4ZLB6LkkhIZZzqy8qtvFbuX91jLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
در پناه ِ غدیر، در کنار یکدیگر هستیم
🔹
در یازدهمین جشنواره مردمی اطعام عید غدیر همراه ما باشید...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: امروز  از ساعت ۱۹ هم‌زمان با شام عید سعید غدیر در خیابان فدائیان اسلام(بین چهارراه نخرسی و چمن)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/656077" target="_blank">📅 16:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656076">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
نعیم قاسم: چرا ایران از غنی‌سازی صلح‌آمیز اورانیوم منع می‌شود؟  دشمنان در شکستن اراده ملت ایران ناکام ماندند  دبیرکل حزب الله:
🔹
قدرت‌های جهانی و منطقه‌ای با تحمیل هشت سال جنگ و محاصره اقتصادی تلاش کردند نظام جمهوری اسلامی را ساقط کنند، اما این نظام با ایستادگی…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/akhbarefori/656076" target="_blank">📅 16:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656075">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgFsJnBvZGsOeNweIveL5sFO1T5dJ0btmYUek3MtiIaacFK-JCRaVKNRRLbreAlktoq2qeq1OkVWpfqdJzqJ4yuYO3N9gt2-WfwcQS0yUmqrWQusul4PfYn-LaAoFOAGvGfAYJ5-kB3igaoAukhqD6A9zC5q0fhZOWJ6QvWB_z0A_tT_LuMG6guzYFCM2nEJdqkKkfmQpyBJHm71rnCZjChpnjmmOIFUQ8IGVF2swwpkBmWcB50yeoNRa3egmJLQdgrrh9gkGOvzaGDzA0yYNUyb5S6rTKjYZqPpnAqGFKjv20t8EbEQRg1HKiXWiLkvWK8YBh1C9Imk1C1vXJ8mGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۲۱ درصدی کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد
‌
🔹
بر اساس این ابلاغیه، نرخ‌های جدید شامل تمامی مسیر‌ها و ناوگان مسافری اعم از اتوبوس، میدل‌باس، مینی‌بوس، ون و سواری کرایه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/656075" target="_blank">📅 16:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656074">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-xi0KlR23bIRDDWKcLo3FX6bJYbOdVvogN7mYkzxBIQlXxODsiR5ltvYrF9j5eIIe92BWnBFalG6RObHtrYkkwII4jkxKaR8USj_B54esm_1vZWUQ3IDSjR4Rl1lG4VLS8Vf6UHJrzk9YUOSV-IKaRMjHlbwik514bpCIObu59hIzCXgq0MnKa7CfjjrI_U-V79oquuA9gcuWpz3m_9r7GwP7Yv-64_SFEFVKnZ9PzRKKIyjmSfJdXw2HTQmGntfqzyvfv-VpBueW2clkeN5PtrYIA6HD_4DqSHala502PNWK8LK9HIrWbkucIEHddiT5B-7N5CFDK52r2lTo3HVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إِنَّمَا وَلِيُّكُمُ اللَّهُ وَرَسُولُهُ وَالَّذِينَ آمَنُوا الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَيُؤْتُونَ الزَّكَاةَ وَهُمْ رَاكِعُونَ
🔹
سرپرست و دوست شما فقط خدا و رسول اوست و مؤمنانی که همواره نماز را برپا می دارند و در حالی که در رکوعند زکات می دهند (آیه…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/656074" target="_blank">📅 15:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656073">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-T4PIlmIYOx0lsg1VTRLAK-A5PVIocXAqe678Cdjjy2sgdfud0fiTGXyWzaCya7QMj8ieaWtPGt_r0aIdGag53q9EhfR8FtLSqkJb5meaOxsHOYnaeqwTrQ2nDX5nTz-7lgi2sI3yQH291FBlYNctPq9xAitrqkeO5mDR2RRmghl3Ahb7AJfsaVfBpN-e0AVYDyk-z-MjwaElEwSMv5pmJGXAtBsp6uoT3gcPE9BPFLqUt7klCcm2siuZOGKQFKVQU2ITAZVcBBkP2OqDAiUijpQc0lMIE1EFDVXtrzodxa3-DeEoxgoarxd_gLytJ-OQ87fPo72IQvInQCbaboKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رقابت نزدیک ایران و مصر؛ پیش‌بینی اوپتا از گروه ایران
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/656073" target="_blank">📅 15:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656072">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o825FKf2yug5BHV7EyfJbsFO8xGVxeFVgEovLK3W4DkxYE0qAlFcin7YbMrH3A21O79KH0D3MGYUnazOYE73W-_Ng_dZjbksB9b4fhFAFRMtV-p8a7-p8pFxoR_2F_DDDQUDosbWjmpH7f2tRVOd6EEZgHrCCoXzb90vX27C1_JaE6wB0i0zpGFEO4QCjp_f8MpQoodsC4e4IaJXvcyiQlIbfdGKV1Tv2O5l_o6vdxyxXxPLTisj5b6LvgrQZb66RtilA8_C5FqZby5sHewxdK_Uie2IaGy7_3o8OxKlcSamWT_BT21b7ytdBwApDAeajxa87AsguAOZiRvnXGCT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نعیم قاسم: با وجود دشواری‌ها ایران، از تمام جنبش‌های رهایی بخش حمایت کرد  شیخ نعیم قاسم دبیرکل حزب الله لبنان:
🔹
با وجود تمام دشواری‌هایی که انقلاب اسلامی ایران با آن روبرو شد، ایران در تمام زمینه ها پیشرفت کرد و از تمام جنبشهای رهایی بخش حمایت کرده است.…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/656072" target="_blank">📅 15:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656071">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
نعیم قاسم: با وجود دشواری‌ها ایران، از تمام جنبش‌های رهایی بخش حمایت کرد
شیخ نعیم قاسم دبیرکل حزب الله لبنان:
🔹
با وجود تمام دشواری‌هایی که انقلاب اسلامی ایران با آن روبرو شد، ایران در تمام زمینه ها پیشرفت کرد و از تمام جنبشهای رهایی بخش حمایت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/656071" target="_blank">📅 15:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656070">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPdgGptIDHFEwdqB8X7NBip2n_mi_JE1P36fjZE0Btjl-R6N4sAWc4xLcppMNeobGjGxXDkcBLA9YqFICChCWvX_pIyGwn7HhPs-XudZBdwpuZIS5BTrlcewovwiM2us3jBCt0malPTQifDzFMZhqY__VxG4q2AsX0wzYcYDBwqT_xVXY7tkqg2xmgAhv7drdZTt4NJf2ej5w-IpJ4YlyyiRZ5GDaJOXXtGd3MIavK3uk7dJL4GhhrBuZzdeJb3uDS-ULvE-fI5JsW_vttloqwhCPPbYbCGSIWUgyy0gX9ctKGLGY9YUQGA2syXNSitPHZuw_QonIFOHONjsRoe6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراکش در حال ساخت بزرگترین استادیوم فوتبال جهان، با ظرفیت ۱۱۵,۰۰۰ نفره
🔹
نام این ورزشگاه گرند استاد دو کازابلانکاس، با هزینه ۵۰۰ میلیون دلار قراره ساخته بشه
#ورزشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/656070" target="_blank">📅 15:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656069">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA6D-Y8GukI4KYuOCa4Z9jyrp4QY0lrFbf5RlZucWuyVT5DF2iwk1A_VCBtkIja_UFWKif5wOGB54yl4m-oQ8wvfdNKnih7an4bu-AkV15t2rh6wdJvblb9m65zkZ25CHPWrTtyou8t5cGLBak6mFS1quy5-HeGOzsAwdKZVYN1aYbGsx-nhp1WdwFgzN_D88_J9QRHgZD_ceXXNdyornms7iUtFwDZR5LgzHcZgySpov2Ft0asoaUQhFMomXwAEFCbeTku2_QL2fgxkQ7j8F7GX35zUQ2djvd_TktsKTIu9EypYmt0j20YgDTVRnp6kZVng0RYz_F-G1bP543dOVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر را روایت کنیم
🔹
امسال شما راوی عید غدیر باشید؛ عکس، ویدئو یا حتی یه متن کوتاه ارسال کنید
💚
🔹
همین کارای ساده، حال‌وهوای عید رو قشنگ‌تر می‌کنه.
#فقط_به_عشق_علی
#LiveLikeAli
شما هم به این پویش بپیوندید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/656069" target="_blank">📅 15:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656066">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
آماده سازی مواکب مهمونی کیلومتری غدیر در‌ تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/656066" target="_blank">📅 15:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a644f3f57d.mp4?token=gDQgzsKpskoJef_qlujAoKLee7BkYR1A-uiN0htEG37gEwVCU37cWioLbEfIoEJw9vNtYW42Tl7-xMUSv2erzYpV19gxN2r6hErOUW5O6BNJrSIeYNw35MH7F1uFUYvTuTFxrZNfgS6bUOKccVjrs6KFapqidp_D3a4zpko7qgLWMXM-8W0b9Sce2Bm0BjmbIxmq9mKTK5kjg3g4r0eyhT4Dgr35A6WaFb3rRCyB0dfUb6yyQ6ae3ZXYGqgPaC4GEfiRnJ2eGKufhKqku0fiasGdOReJlXgslR-keG2DoCLpuxoglGSGQ74lWU9F8VLkvDgLN68_IDA2XT0zg-inXHLiN9fzbFhSMU9wLK_5oCV_GE57-sUIE3BhhAqw8vNl4paNjEUBkiLqk2BF_QSSLq2BVfkilwoWI1w-Amj8XWSaMM3afauElEG5t_4D36-W3DOslcJYPV2ZAPeBfOztNIvv5QmOr5vGryvgb8mHH4RldAq7jucS-jSbDorJ1dz0MqPeGsDIBNktOMQgbPn7qCitrnEpTuome2vACo9CkS8xbQTyF-Korg8wuxJbTxFdEJqwSm_gXcyTbmsHX5cYeEp0S3G_42mZ7zwUSVdB3Zl62lX6zq3dKwbKDI0DhpDiuuwvWABHQmX18BI_eEnzKCwQgt2P2NlngLFv1pX8t04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a644f3f57d.mp4?token=gDQgzsKpskoJef_qlujAoKLee7BkYR1A-uiN0htEG37gEwVCU37cWioLbEfIoEJw9vNtYW42Tl7-xMUSv2erzYpV19gxN2r6hErOUW5O6BNJrSIeYNw35MH7F1uFUYvTuTFxrZNfgS6bUOKccVjrs6KFapqidp_D3a4zpko7qgLWMXM-8W0b9Sce2Bm0BjmbIxmq9mKTK5kjg3g4r0eyhT4Dgr35A6WaFb3rRCyB0dfUb6yyQ6ae3ZXYGqgPaC4GEfiRnJ2eGKufhKqku0fiasGdOReJlXgslR-keG2DoCLpuxoglGSGQ74lWU9F8VLkvDgLN68_IDA2XT0zg-inXHLiN9fzbFhSMU9wLK_5oCV_GE57-sUIE3BhhAqw8vNl4paNjEUBkiLqk2BF_QSSLq2BVfkilwoWI1w-Amj8XWSaMM3afauElEG5t_4D36-W3DOslcJYPV2ZAPeBfOztNIvv5QmOr5vGryvgb8mHH4RldAq7jucS-jSbDorJ1dz0MqPeGsDIBNktOMQgbPn7qCitrnEpTuome2vACo9CkS8xbQTyF-Korg8wuxJbTxFdEJqwSm_gXcyTbmsHX5cYeEp0S3G_42mZ7zwUSVdB3Zl62lX6zq3dKwbKDI0DhpDiuuwvWABHQmX18BI_eEnzKCwQgt2P2NlngLFv1pX8t04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابرپرچم های خلاقانه مهمونی کیلومتری غدیر تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/656065" target="_blank">📅 15:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656064">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUayp2gegAI5oocHtPqoEt_K3eVQ2iueipTUR4cv3K_KRAxOWCEPOSQCB51Uie4QvzFOiru3b7aYsiP4YPwy1V7mQ2stKafr-B39E48e0YwGjEs4kHREQUwDLQ_OXQLXO-w1YFoQWoxM20RdzSuZObMpjf7hvMCkilcnArsIwZDc_NJl8-CR-oCW9geSqX9UIDeImzTUy7Nij-QSdAEuaAqajOXA00Z5HVyw0dWKj1-sQnBvINxUimae8OfGW0gryRl9w3erBwt20GZcwsu-meQCbQRAF7ezQsSqSTDbkwiCNS9swKXDVdkwxqHPe2QhMBTm-R1wQrFNxwlskapKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار تصویری از رهبر شهید انقلاب به مناسبت عید سعید غدیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/656064" target="_blank">📅 15:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656063">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس| خبرنگار الجزیره: حمله هوایی اسرائیل به شهر بیت یاحون در منطقه بنت جبیل در جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/656063" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656062">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
فیفا در آستانه جام جهانی ۲۰۲۶، ورود بطری‌های آب چندبار مصرف را به ورزشگاه‌ها ممنوع کرد؛ دلیل آن مسائل امنیتی و جلوگیری از پرتاب اشیا به زمین یا سکوها اعلام شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/656062" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656061">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مهمونی کیلومتری غدیر در پاکستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/656061" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656060">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7535f633d.mp4?token=oHj9mo2QCRg6utvGLxzVU5P7VKdS1qH8013-zc5TbJ8pnq8pU_sdFIDCNu_ZsVXHuVcBiSPacq0O-2AtObUnCL2KzlrWDupLPCazE1IAKy1I3myfkCCxe0kfwzugqAjB6QBxWLwTl3thgknvfJDfUB11IYR_M9YsZxNUubmF0YmnVZaX-_APOIwWLJfE2obf7lLR3DdaJH_YIkkOAxT-1812Qn-_xBqBlx8rl8GoRBusdA4axYxkbX6qHDzAgHlH7lrJReStdsQw9VAJsPQjhtxG9CdJjUyF22-FqpiiMhn5R8tB1nQersjojrengQ6BCiPJAdhP5EjxT6-knLoiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7535f633d.mp4?token=oHj9mo2QCRg6utvGLxzVU5P7VKdS1qH8013-zc5TbJ8pnq8pU_sdFIDCNu_ZsVXHuVcBiSPacq0O-2AtObUnCL2KzlrWDupLPCazE1IAKy1I3myfkCCxe0kfwzugqAjB6QBxWLwTl3thgknvfJDfUB11IYR_M9YsZxNUubmF0YmnVZaX-_APOIwWLJfE2obf7lLR3DdaJH_YIkkOAxT-1812Qn-_xBqBlx8rl8GoRBusdA4axYxkbX6qHDzAgHlH7lrJReStdsQw9VAJsPQjhtxG9CdJjUyF22-FqpiiMhn5R8tB1nQersjojrengQ6BCiPJAdhP5EjxT6-knLoiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای خیابان انقلاب یک ساعت مانده تا آغاز مهمونی ده کیلومتری
حتما  پرچم حزب الله و عکس رهبر انقلاب همراه داشته باشید، این بزرگ‌ترین رویداد خیابانی ایران است که به احترام امیرالمومنین علیه‌السلام برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/656060" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656059">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYQKBLtV8v3unvwAciZQVyHSvOKs_AcHD3HS7hk73aCONT8mTI4qZHSFstY6J8DJl7zAM7s5iZLx9YXCOxMCE38mE_ww1Ysp4HK-GDwk3bOTo6fQiANq4pyCLHz_LaVarPbCZQo5odzo0zw8XD0w-0CspnmsIqk5wkmT-__wAGyHXvA0uapV6C_67KzPfXvLgYdhZ8aRx9DZ29dfb24danWCRDSWjBcSA8jUp9PnB1cXFdX6evjsNryR96wVUhjUN3n4Sv03yEhtNo617Vui43QQ42dsdlLpOyZfbmsiXs7hzxtpSIO5uJKPLTTUK8qL_yjRjZK4989Q9GSqzZ6pNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آب زاینده‌رود به اصفهان رسید  #اخبار_اصفهان در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/656059" target="_blank">📅 15:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656058">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عراقچی: لحظه شهادت رهبری در دفتر ایشان بودم / ساختمان هدف قرار گرفت اما ما سالم ماندیم
وزیر امور خارجه ایران:
🔹
روز شنبه پس از بازگشت از مذاکرات ژنو، ساعت ۹ صبح برای ارائه گزارش به دفتر رهبر شهید رفته بود که ساختمان مورد حمله قرار گرفت.
🔹
با وجود احتمال بالای جنگ، روحیه ایشان مانع از رفتن به پناهگاه می‌شد./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/656058" target="_blank">📅 15:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656057">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
دونالد ترامپ: دیروز، مجلس نمایندگان با ۴جمهوری‌خواه بد و همه دموکرات‌ها به محدودکردن قدرت جنگ من در میانه مذاکرات نهایی‌ام با ایران رأی داد
‌
🔹
چه کسی چنین کار غیروطن‌پرستانه‌ای انجام می‌دهد؟
🔹
دموکرات‌ها با سندرم اختلال ترامپ پر می‌شوند. آن‌ها ترجیح می‌دهند کشور ما شکست بخورد تا اینکه به من یک پیروزی بدهند.
🔹
آن چهار جمهوری‌خواه؟ پوپولیست‌های خودنما، باید شرم کنند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/656057" target="_blank">📅 15:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656056">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e520b2e2.mp4?token=aRrFbH3-uX9Vlgt7qf9zxj2fDCj82_SdbPgfp2IidNKwuro3fJDs0VP02ACUXTkgX9p-x7FXjIrxf7WDuoYLu0sqIvaSi1b1x3DZzfIGtq0EwxKGIg971Mtn9FUgGwpOIzsoA0y6qiLhXG7lx2mmlWB67Qaz1Py5L17qodBUd0u11hQJ8zx_NRbns-otmzxAVhsxCZ3EKJKlNwoUmlFc5EvrvD08iI6Ui_idelu7Fzz8WPNeWc25yiHbPN2x8IJVGEXksYnoKEZdew92oGnuGfMSazI4Bs7kpMC26EMa4rOx7SnUTwRlE1tYzAC4PvFUHM4NzB9BEiqX5lo0lMBq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e520b2e2.mp4?token=aRrFbH3-uX9Vlgt7qf9zxj2fDCj82_SdbPgfp2IidNKwuro3fJDs0VP02ACUXTkgX9p-x7FXjIrxf7WDuoYLu0sqIvaSi1b1x3DZzfIGtq0EwxKGIg971Mtn9FUgGwpOIzsoA0y6qiLhXG7lx2mmlWB67Qaz1Py5L17qodBUd0u11hQJ8zx_NRbns-otmzxAVhsxCZ3EKJKlNwoUmlFc5EvrvD08iI6Ui_idelu7Fzz8WPNeWc25yiHbPN2x8IJVGEXksYnoKEZdew92oGnuGfMSazI4Bs7kpMC26EMa4rOx7SnUTwRlE1tYzAC4PvFUHM4NzB9BEiqX5lo0lMBq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار برای اولین بار؛ سخنرانی شهید علی لاریجانی درباره زنده و ناظر بودن شهدا، یک‌سال قبل از شهادت خودشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/656056" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656055">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJLQN9wZBjBQv8bWhzLWaS4qwbNS7Ak3sgZP6p7tNRLtkMlzeLg3uOwEqk5DAQiWVbEp37DY2qpTNHODyuIpXBoqfTIVdDJOPiPkASlE1cwQyvEtGDFWp_GxTyDZwxGbX3PRO2zgNyxhKzHQMOZrPluAseaXMExbawe9MuAWb1HL1QBg0FHoc970xf6Aw6XlSFktWFTe_5k3fDQ4UZ275BIa_GuMJiaroQF1vOW07kGuiigy9jlCejPWktR63zUEosVgPn3LPpYC7IxKb9mcZwEvQwGWMvs0xFdApJ-38744WvAQhkXajwG8QJzCJJgNcJAnZxMbG7OasXkhejcesw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز یک زیارت کمتر شناخته شده!
🔹
زیارت غدیریه؛ روایتی فشرده از جایگاه امیرالمؤمنین(ع) در قرآن و تاریخ اسلام است. این زیارت با دربرگیری بیش از ۷۰ آیه مرتبط با ولایت و وقایعی چون ماجرای فدک و نبردهای امیرالمومنین سندی بی‌مانند در تاریخ تشیع و چون نامه‌ای از…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/656055" target="_blank">📅 14:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656054">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
چت جی‌پی‌تی، دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/656054" target="_blank">📅 14:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656053">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
معاون حقوقی و بین‌المللی وزارت خارجه: اگر حملات به لبنان متوقف نمی‎‌شد، قطعا جمهوری اسلامی ایران اقدام می‌کرد
کاظم غریب‌آبادی:
🔹
پیام‌هایی درباره توقف حملات به لبنان از طرف وزارت خارجه و از طریق کانال هایی به آمریکا ارسال شد.
🔹
آتش بس برقرار شده بعد از جنگ، شامل لبنان هم می شود./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/656053" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656052">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sxy2hsbqFyneYwJOzqtBv7Ibgs4Y6NwJY2PoVcXrdimEOdf_L3bRmOBDb4DgIWMFMqTH-i1x-bT5kLOF80pIxmUKDhvGM24ipTrWgpxmIig1mLwLAYLhvihmEPTNbRazk9pmoxA51XYR3_rg4-7ntINHGVEW534kxiUaMaqDvHl8Qjr_9fyPHSx7bM8OE8j7csnhUiRFJr4I1l7UkDRmPy_X8dInJUpWvc_rFe1Q8AVVdtuJyuVBPuL54v2ZX1pjZCz_Eq2S_1cbqqhHALILE_4ZEIcvAWI3t3q1VtDAXjVTqhCVd4HbtqEC-ht30MB4OFkLQ1zeU6HqDlu6UZGWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر روز بازی فدراسیون فوتبال ایران برای دیدار امروز مقابل مالی با اشاره به ۱۶۸ دانش آموز کشته شده مدرسه میناب
🔹
ساعت ۲۰:۰۰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/656052" target="_blank">📅 14:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFMMVFW669d-nFOw9fs09z4Y5nj35k6TmKYmWwxKNYyhYk8DkPYHY3zmKC78uslvVpcJJNIQy_FbzO6dXQFxRtoIUGxyhrRg3UjMYXxuugW43XwgdVUg6BnCyossA0C3g_oIVRdHfcUGl-NAq9kajcUgBwl8PynMPxIien2ji8ge4hFk9ZVurATbbpZraqa6qFpifWKPq6_BaQ6ZTYUXE6SDpDyOpKWN-nMBTxz3odcCmTXaBoTAsfaLyjCtM01RwjcXrLRmzsCYbFFROnftVFTs7XLGbmpMd7-RLl4TMuSJda4VQH4PfnKEUngNdWDbpsEm9zRbCGv6RMZ4ofmGDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzZppaA_Y0HYYM87qbk6APb8cmy_hl6DRduysMuY11IzQMqrl1DntTLBFL6_5VcUpVVWnQ1cSIy9j2NAMuGZu9Ft2rQPic1VAwNzrDftSGjt62ndlwgQFhdXFxRFwPwWJRcVqX_eM1eqNv_KmhBJEkuTicdNYWPlD3DOGgiNJ2T43Le_kOpkSGB0YJziKXoF_n5f6p-uNolbqgppe53mYemZZq5iBpQGV_c5EApCFqQ-NlK_MaDdeN0101JhPce5HhsFF4a3iqSr3XoRnWCtLDR5jhVKC9TxkkwNdn8PdgOhps-_sEPzwDN8Uz0sK_9pDciIw970UwGjvET8C9rqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuXoP4-35k-J5NVRJD6IVQJtF6y-jU1-kxyJwW5j-MywHnfTBWghl0IdDiqBxOAn_15puqp9LP53DnmPWaIMXrVFejYROd0vIXjMH9l3UnXk5NtsWI9kAPRJGmKOfffhe3uTFkU-z6k7q7-xbGnVvLubzKQxFRdpu9Tj2zdV1gEEDW7cb7v6Ty7H9BbGf96-fU3AKXhV7ZxWvmjqQoiIeb92PI_TSfKspq3KWkJ17bm1rWmqklVLOWwOwxRE6rieDewD9x8Qg-7se-rf0E-EavaW0L8xByIjSU2aMCwU-IoGOGmWggN99m9IlgEi9gbDZGF48Uztk3JM7CL8UXZBlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دریاچه یخ‌زده قله سبلان؛ ۱۱ خرداد ۱۴۰۵
#اخبار_اردبیل
در فضای مجازی
👇
@Akhbarardebill</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/656049" target="_blank">📅 14:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر شهادت)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@abaratinfo</div>
  <div class="tg-doc-extra">Mohammad Reza Khameh Chian</div>
</div>
<a href="https://t.me/akhbarefori/656048" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">الْحَـمْدُ‌‌لِلَّهِ‌الَّذِی‌جَـعَلَنَا‌مِنَ‌الْمُتَـمَسِّکِینَ
بِوِلاَیَهِ أَمِــــیرِ الْمُؤْمِنِینَ‌ عَـلَیْهِمُ السَّلاَمُ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/656048" target="_blank">📅 14:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تصاویر تازه منتشر شده از لحظه هدف قرار گرفتن فرودگاه کویت در ماجرای پاسخ ایران به نقض آتش‌بس از سوی آمریکا
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/656047" target="_blank">📅 14:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22e6263214.mp4?token=ojtD8l_0OBcG6AzeeerxuzK2y-q3mkixC-DEW2Vu0h_dX3FKM1sgvl8A4YKyFbmxWr5ieNbZr2TyY4Wwwblvpp3jup6AKCd9YLrIM8nb5xPmDAuXXS_Ijg6B-wbHVtWeDx8MGvV6oSvGPo8IclY6exqqEuEzbC1xa7xFgAtHY9pKegqeTHeb_uFx33VKABOnYgKX9-YIbqhv6JhSaV7Q7lS18XWq5ijNG3oTpup3oen3TZcN56UAQpgkkaIef23R1S9RRHVlfl70XXFdInLRjcbF8o2g5niY9MSGbjfHE98NSBgRvtXnUhuL5YQ-zZz9mfR5rt82vQU5bO2U-idWFpPf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22e6263214.mp4?token=ojtD8l_0OBcG6AzeeerxuzK2y-q3mkixC-DEW2Vu0h_dX3FKM1sgvl8A4YKyFbmxWr5ieNbZr2TyY4Wwwblvpp3jup6AKCd9YLrIM8nb5xPmDAuXXS_Ijg6B-wbHVtWeDx8MGvV6oSvGPo8IclY6exqqEuEzbC1xa7xFgAtHY9pKegqeTHeb_uFx33VKABOnYgKX9-YIbqhv6JhSaV7Q7lS18XWq5ijNG3oTpup3oen3TZcN56UAQpgkkaIef23R1S9RRHVlfl70XXFdInLRjcbF8o2g5niY9MSGbjfHE98NSBgRvtXnUhuL5YQ-zZz9mfR5rt82vQU5bO2U-idWFpPf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یا علی
نام تو بردم نه غمی ماند و نه همی
بابی انت و امی
گویا هیچ نه همی به دلم بوده، نه غمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/656046" target="_blank">📅 14:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4-ABJAvBJVLB7CNDVfdHQyBMP_P_LSZ5_d2zC3DK1LynKYYTszyFRbTqwOfsw3SEcfy8SbEggPvkUbV5r5lLtbJqeUCqiFFNjDc23yytql-1BlUv2Z5PO7b_e2OslgOTdzl_ufxrAC61IwzFhUR10v9ydk-uZZhKyWJQegzupGmxLOtnAd-KlJ7J65bX_HosiibN5njnH1RFx0soYYkqm495TM9retR0N-lCJjZKsrChPe8Gof1MUs4hsicXTyc0B01H0gjtiUjga8WmIlAoqP83JtwWqaGA2tpxDc77V1rvz_JkNIMFAao__fT4g-KbHDLnybe-wvxFUMKDA7ldQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهرابی طلا و سهمیۀ جهانی را باهم گرفت
🔹
دانیال سهرابی در فینال ۷۲ کیلو رقابت‌های کشتی فرنگی رنکینگ اتحادیه جهانی کشتی مغولستان، ۸ بر ۵ محمدجواد رضایی دیگر نمایندۀ کشورمان را مغلوب کرد و علاوه‌بر کسب مدال طلا نمایندۀ ایران در این وزن در مسابقات جهانی لقب گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/656045" target="_blank">📅 14:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مبلغ جدید وام فرزندآوری از فرزند اول تا پنجم چقدر است؟
🔹
مبلغ تسهیلات برای فرزند اول ۴۴ میلیون تومان با دوره بازپرداخت ۳۶ ماهه تعیین شده است، این رقم برای فرزند دوم ۸۸ میلیون تومان با بازپرداخت ۴۸ ماهه، برای فرزند سوم ۱۳۲ میلیون تومان با بازپرداخت ۶۰ ماهه، برای فرزند چهارم ۱۶۵ میلیون تومان با بازپرداخت ۷۲ ماهه و برای فرزند پنجم و بیشتر ۲۲۰ میلیون تومان با دوره بازپرداخت ۸۴ ماهه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/656044" target="_blank">📅 13:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZeZJK8FeRCZURIVNBTs7um9970CKMrnWFJE50bzfLmE2hG6opwh8SY0aAnZtXpTZkYoesJpEfhdBiinhLFcDe38vrRHS5oae2nBJk57F7nhrRG13hH6Cj-j74BTL8XfFXnQOOMMEyddJ3hNIh6e7pahMO8GLaNst_J-x04hQjZBd4ARM5LB34F8wguOucFjYWOjKGEZobZ6uVRPtLG96OQsRmtmgOA7LQovSTSxRK5M5n-aUvD8BisRYNF3NUVNipcekpF7dELLdD_VSj20OWecJA_Ywrs2_OZfq172D_jtOyFNgQRgPxdXOv8Zrk9Vl8A2eZfGx9T60NeEfGqWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز اعلام ولایت
🔹
هر کس من مولای اویم، علی مولای اوست، این جمله در میان جمعیتی عظیم طنین‌انداز شد و یکی از ماندگارترین رویدادهای تاریخ اسلام را رقم زد. #روایت_غدیر #فقط_به_عشق_علی #LiveLikeAli #VoiceOfAli
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/656043" target="_blank">📅 13:51 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nN0X85uKoGOJqzYzcpmbyz3Ydxr9CVF7GTAW2DRQoKBDVC3SLFk3-_bUvixGAJhvXgIt0Fu8QVryxP5TMhuYBCroVZEirOenmyoTcmmPeQ3fmWP10QBV-ddkOpIZpt2KaJGCbkrDeVIIQqhYCyVa0Pl86nZY9PSAuI3U8sd5cWy2GT6lIUQUR6E-PQUv8pdEx_ws28w8LT9HDv0FYYuJpnL5-w8H7RUi-8Zk5pizyEzH6SUkNPpXOh0qz6ONyVFGjHo-08D-UFNgqolYzmWjdIMBgnI9IF8jEF3DWrr0-06xLX_QlInKVZkjP0PT-Rbp4_lRAWUjYOvxCDZbrYVflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: اسرائیل باید به نقطه قبل از شروع جنگ ۴۰ روزه عقب‌نشینی کند
📲
‌
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/656042" target="_blank">📅 13:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mohsen Chavoshi</div>
  <div class="tg-doc-extra">Ali</div>
</div>
<a href="https://t.me/akhbarefori/656041" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">علی آن دلیل رحمت، علی آن چراغ ایمان
علی آن که می‌درخشد به دل همه دوران
به ولای او قسم خورده خدا به روز محشر
که بود علی حقیقت، به یقین ره‌گشای جان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/656041" target="_blank">📅 13:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خسارات جنگ بر نظام سلامت؛ ۳۸۵ مرکز خدمات سلامت دچار حادثه شدند
حسین کرمانپور، مدیر مرکز روابط عمومی و اطلاع‌رسانی وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
۶۳ مرکز بیمارستانی، ۵۶ پایگاه اورژانس پیش بیمارستانی و ۶۴ آمبولانس در طول جنگ آسیب دیدند.
🔹
از بین آمبولانس‌های آسیب دیده، بیش از ۱۰ تا ۱۵ آمبولانس نتوانستند به چرخه بازگردند. همچنین دو آمبولانس هوایی منهدم شد و دو آمبولانس دریایی نیز دچار حادثه شد.
🔹
هر آمبولانس ما که از رده خارج می شود بالغ بر ۱۷ تا ۱۸ میلیارد تومان هزینه دارد. ۳۸۵ مرکز خدمات سلامت معروف به مراکز جامع بهداشتی دچار حادثه شدند.
🔹
۷۱۸ نفر از همکاران ما دچار حوادث مجروحیت شدند و تقریبا ۵۲ نفر از همکاران ما در طی دو جنگ شهید شدند که ۲۷ نفر از آنها در جنگ اخیر به شهادت رسیدند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/656040" target="_blank">📅 13:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
آکسیوس مدعی شد: دو مقام ارشد آمریکایی گفتند که در حالی که ترامپ می‌خواهد به جنگ پایان دهد، به نظر می‌رسد نتانیاهو می‌خواهد آن را از سر بگیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/656039" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53de2848c.mp4?token=UsqLKYsbl9FR_Fe0TdnEG6Cw1pCAbeZ-aNNDGBCw6t08Pf7GD4CEGeikm65UVyzre_PTXJ_wDH6DWnP8YAd9GaIjDfBqlJbKJBbwnBeAH2e1G5r5SCHK__tOu83T1KInc6ghGjLRhCgRJgwXJRKxxJCvcdV9lo7XnqQ-KvnJdFGRQIBXVYhj5KkgGB3BA_77zPXxCBfiZOC1JnBP4FfVzCwmq7cDFJngCnGZNlqtwsChOzsJBMHchkZa03oyFweuv958VNTVkETWnSAH65d1NyDto6Dqya6wqEoASjJWi9eaSg1mNnVDaCTBJlUmX5BU_ZNccs48f6pt65UZIsQ1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53de2848c.mp4?token=UsqLKYsbl9FR_Fe0TdnEG6Cw1pCAbeZ-aNNDGBCw6t08Pf7GD4CEGeikm65UVyzre_PTXJ_wDH6DWnP8YAd9GaIjDfBqlJbKJBbwnBeAH2e1G5r5SCHK__tOu83T1KInc6ghGjLRhCgRJgwXJRKxxJCvcdV9lo7XnqQ-KvnJdFGRQIBXVYhj5KkgGB3BA_77zPXxCBfiZOC1JnBP4FfVzCwmq7cDFJngCnGZNlqtwsChOzsJBMHchkZa03oyFweuv958VNTVkETWnSAH65d1NyDto6Dqya6wqEoASjJWi9eaSg1mNnVDaCTBJlUmX5BU_ZNccs48f6pt65UZIsQ1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی جدید از حمله هوایی به پل B1 کرج در جنگ رمضان
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656038" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80bea3aba.mp4?token=Zysbts1kQ1Jp1WaAd3nlKScTKmKI4wOfrW9-8Ds8b6vKzsvHQ-co4XUveStl662g8abPjS0aaugwHFHDkVGQPMY-9m8AHPG8w_493jnSE8LGEvnF3h3Jm1yfV9L74nbVtHg0kxa3aU7I6mYfdzcfJn095Tav08QD5J2RbS7bD-8siSzQnwwOqX6v-WiCLjTaR3KEbhOAcjlAArv6GuzK7z4TtHzfPSTtcDG-uIdCL1hZ429JF0mbMtprTqQd-CBozkWggtuaDZktvsmJsiYwNxXQqQBlHbu7KAWYqEM0SHeFJNx0WkfCwboqLI9BaCsD0M9ExBrKR-fCVpT8tZIhWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80bea3aba.mp4?token=Zysbts1kQ1Jp1WaAd3nlKScTKmKI4wOfrW9-8Ds8b6vKzsvHQ-co4XUveStl662g8abPjS0aaugwHFHDkVGQPMY-9m8AHPG8w_493jnSE8LGEvnF3h3Jm1yfV9L74nbVtHg0kxa3aU7I6mYfdzcfJn095Tav08QD5J2RbS7bD-8siSzQnwwOqX6v-WiCLjTaR3KEbhOAcjlAArv6GuzK7z4TtHzfPSTtcDG-uIdCL1hZ429JF0mbMtprTqQd-CBozkWggtuaDZktvsmJsiYwNxXQqQBlHbu7KAWYqEM0SHeFJNx0WkfCwboqLI9BaCsD0M9ExBrKR-fCVpT8tZIhWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی‌که ۲ تا دست میره بالا، ولی نه به نشانه‌ تسلیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/656037" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پیام تبریک سخنگوی وزارت خارجه به مناسبت عید غدیر
اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی به مناسبت عید سعید غدیر خم این عید را تبریک گفت و حدیثی از حضرت امیرالمؤمنین علی(ع) را به اشتراک گذاشت:
🔹
«اَلْعامِلُ بِالظُّلْمِ وَ المُعینُ عَلَیْهِ وَ الرّاضِیُ بِهِ شُرَکاءُ ثَلاثَهٌ»؛ یعنی ستمکار، یاری‌دهنده ظلم و کسی که به ظلم رضایت می‌دهد، هر سه در آن شریک‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656036" target="_blank">📅 13:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای العربیه: مذاکرات آزادسازی بخشی از دارایی‌های ایران به مراحل پایانی نزدیک شده است
🔹
مذاکرات برای دستیابی به توافق درباره آزادسازی بخشی از دارایی‌های مسدودشده ایران به مراحل پایانی نزدیک شده است.
🔹
رایزنی‌ها درباره سازوکار آزادسازی این دارایی‌ها همچنان ادامه دارد و مهم‌ترین مانع فعلی، نحوه مدیریت و استفاده از این اموال عنوان شده است.
🔹
همچنین پیشنهاد تشکیل یک «صندوق ویژه» برای واریز و نگهداری دارایی‌های آزادشده ایران تحت نظارت مشخص، در حال بررسی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/656035" target="_blank">📅 13:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
تکذیب اعلام برنامه امتحانات نهایی
روابط عمومی وزارت آموزش و پرورش:
🔹
جدولی که تحت عنوان برنامه امتحانات نهایی تیر و مردادماه با امضای رئیس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش در فضای مجازی منتشر شده است، صحت ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/656034" target="_blank">📅 13:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFmj6uIwVw5ZU3NNStGa97MmiCnNNldl85Vvxs7xVyfLrukLCClgJ3y8WLRQ6NAyL6p5xynBkTVeKdbG0aA8_LrUOfbExjZehbm4li2-gabePzWR7eiDTDq35SbrRHFD1noVzao9omWRys-dA6BdWk9h1jHvb7z_d4nKO6yCvPcA82RgOHUWOh3DZu2djKuNhfHuO_3-oIE9VW0XGbwt6igSX5whHzz4dTbkFvEd4miik-hT5bIs5NY5F9RaEpyLHQBgPs9jaNuFZDaE8JSX_GyTIGZzBwrD8IoVa2U_ZgTWZHAbQIPRY5faT45UlW4mXU82GMcZWKLo5mc6lL3jhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ترامپ ادعا کرده جنگ تمام‌عیار با ایران را از سر نخواهد گرفت مگر اینکه نیروهای آمریکایی کشته شوند
وال‌استریت‌ژورنال:
🔹
مقامات آمریکایی گفتند، ترامپ به طور خصوصی به دستیارانش گفته است که اگر تهران نیروهای آمریکایی را بکشد، پایان دادن به آتش‌بس با ایران را بررسی خواهد کرد.
🔹
اکراه ترامپ برای شعله‌ور کردن مجدد جنگ نشان می‌دهد که او ممکن است مایل باشد برای جلوگیری از درگیری گسترده‌تر در خاورمیانه، شعله‌های آتش کوچکتر را برای هفته‌ها یا حتی ماه‌ها تحمل کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/656033" target="_blank">📅 12:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uknVBtg-luZYFJNSda2ak8gDtJRO9_Y1JIx6ZS9akGkfWapQu7TZRoOeLFJ8xrtxRVOkuXvZ48wSOF60W8WDcQZKgx8p6yRBNlIrbFP7nbh10zYbwZlEjU-dRrkmtLpF-bmSGBUAq0mF6YHEmLmOGsGx0yOoq5ywNefgSm6QoewM7oZFmhJGuz3QloYOacPVUXL8g93tCzP1FhOz2SfWl89-NY92fhiWh4g8k6ODqb0RmwduYR114o_ruElqabs9hQwcZWN0SWZJY9pqUMEA0AeDeOLX5jN6Bnso_NcJLsNfnGuyRxI3Xe1nvgHGjTb7amO3FJJbEMHTgqu8Rot3Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
إِنَّمَا وَلِيُّكُمُ اللَّهُ وَرَسُولُهُ وَالَّذِينَ آمَنُوا الَّذِينَ يُقِيمُونَ الصَّلَاةَ وَيُؤْتُونَ الزَّكَاةَ وَهُمْ رَاكِعُونَ
🔹
سرپرست و دوست شما فقط خدا و رسول اوست و مؤمنانی که همواره نماز را برپا می دارند و در حالی که در رکوعند زکات می دهند
(آیه ۵۵ سوره مائده)
.
🔹
روزی فقیری وارد مسجد پیامبر شد و تقاضای کمک کرد؛ اما کسی چیزی به او نداد. او دست خود را به‌سوی آسمان بلند کرد و گفت: خدایا! شاهد باش که من در مسجد رسول تو تقاضای کمک کردم؛ اما کسی به من چیزی نداد.
🔹
در همین حال، امام علی(ع) که در حال رکوع بود، به انگشت کوچک دست راست خود، اشاره کرد، فقیر نزدیک آمد و انگشتر را از دست او بیرون آورد.
#اخلاق_علوی
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/656032" target="_blank">📅 12:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آستان قدس رضوی: چند مکان برای تدفین رهبر شهید بررسی شده است
🔹
در زمان مقتضی به فرزندان رهبر شهید و رهبر معظم کنونی انقلاب پیشنهاد خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656031" target="_blank">📅 12:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0A6zsPHo6-O2d4fwd1GB8g_63bxLduIbTQ4vWqMURm91kQuUOIxl-7H1tLp8JsmZ2DimebeM3A38C8ExK-p7uzVhhOwAIYrtPBgRyC1QRM7n0xzqGbJGi-WM2QskvVYESSknL4Q28q4lue7BXGNLD_NED3LHRTYqqgdVcEOjx043mLwnMpEAAjsTq9hXyP46yu1gGsa4z_pWYEhsmDIl918P6O_mW2nGpKpvJ55jSGnkYOAnVIeu3XUVohhEYuQwIUnIBHpU7i1xKdXb88D0lCrfRaO2GzdAgaBnQEBgzcWLIAYf9PtJU1RGuKlsqMh7m_Oli2Lwpbh3yEmYs0PqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: تنگه هرمز مهم‌ترین اهرم ایران در معادلات جهانی
سی‌ان‌ان:
🔹
ایران با کنترل تنگه هرمز یکی از مهم‌ترین اهرم‌های خود را در معادلات اقتصادی و سیاسی جهان در اختیار دارد؛ حتی در صورت دستیابی به توافق دیپلماتیک نیز این ابزار از دست تهران خارج نخواهد شد.
🔹
نگرانی اصلی بازار انرژی نه هزینه احتمالی برای عبور نفتکش‌ها، بلکه احتمال اختلال یا توقف کامل جریان نفت از این گذرگاه راهبردی است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/656030" target="_blank">📅 12:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f642f8f3.mp4?token=JeCidDAScuvrpdEkYNl1XWoW6dx67JeFDHKBeqfsz4R5MwNIXsMiXwKM_Z1WqUAefXlttBSc12i2mGKMUy9HRJrK3CcOhAMcV-FEnxhJxxt9vjfHi5br00VH6vjcVayrsxY8N0FKVrO4PZ3S5Z3dCj7_6Smmfey08RG11HgfJecy5Fz_JHXQZqOhu8dj7RVAVlj7_jy-cRAa_QlspMlosL9XTYd3iQ-_8WQldMWqo57Wiskiqe7y8Odak-wgpuQxNyNWqwZDwE0X0xR_N4-y9CRiM6jk6KRCJDKywr1yVX6rXgfhTE9saZeC-AjlNSzwzaIsQjYCqXj81s34zP_D6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f642f8f3.mp4?token=JeCidDAScuvrpdEkYNl1XWoW6dx67JeFDHKBeqfsz4R5MwNIXsMiXwKM_Z1WqUAefXlttBSc12i2mGKMUy9HRJrK3CcOhAMcV-FEnxhJxxt9vjfHi5br00VH6vjcVayrsxY8N0FKVrO4PZ3S5Z3dCj7_6Smmfey08RG11HgfJecy5Fz_JHXQZqOhu8dj7RVAVlj7_jy-cRAa_QlspMlosL9XTYd3iQ-_8WQldMWqo57Wiskiqe7y8Odak-wgpuQxNyNWqwZDwE0X0xR_N4-y9CRiM6jk6KRCJDKywr1yVX6rXgfhTE9saZeC-AjlNSzwzaIsQjYCqXj81s34zP_D6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان شیولوچ در منطقه کامچاتکا روسیه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/656029" target="_blank">📅 12:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp0jTrdZRr1Bk6t5br8dn55CH1vCMntYnorz1wN7u8se7QpbzHie87jfJH8XXrJEZ3zWYyKMTge5UG58n8PHzYaeWXZBdVt5xBrrWyiso0ORhx5aGnvLyP439arReRv7Q7fve57S5k0SDGMYbH1_gtovkWaTTp_ghPQvcyPYQLqytlXdLyNBzpeuQZqimf40G96eVQ2XyKzTjZGHTr3IRHRNlfSCiLnS46ofiTipt0xH3PwLG1nz0h5CamMyl30wxOKmCPPQBK9L96-1hpv7oqtR1AVgqjqMhX_tdhA4dFlWQe_Kw0jqqZPoOyzzRhpiCLuAVW6Zqqzdc0fpYD4b2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نکات کلیدی پیام رهبر انقلاب اسلامی به مناسبت سی‌و‌هفتمین سالگرد ارتحال حضرت امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656027" target="_blank">📅 12:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
تکمیل ویزای اعضای تیم ملی ایران برای سفر به مکزیک
🔹
با انجام فرآیند اداری معمول و صدور ویزای دو نفر از اعضای باقی مانده تیم ملی، روادید تمامی اعضای تیم ملی صادر و این فرایند تکمیل شد.
🔹
تیم ملی فوتبال ایران روز شنبه ۱۶ خرداد در ساعت ۱۵:۲۰ به وقت ترکیه عازم تیخوانای مکزیک می‌شود.
🔹
طبق برنامه‌ریزی انجام گرفته، کاروان تیم ایران در ساعت ۱:۳۰ بامداد روز یکشنبه ۱۷ خرداد وارد شهر تیخوانا مکزیک خواهد شد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/656026" target="_blank">📅 12:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656024">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
جزئیات رای‌گیری کنگره برای متوقف کردن جنگ ایران؛ ۴ هم حزبی ترامپ علیه او رای دادند  نیویورک‌تایمز:
🔹
مجلس نمایندگان آمریکا روز چهارشنبه طرحی را تصویب کرد که به موجب آن، ترامپ باید نیروهای آمریکایی را از خلیج فارس خارج کند یا برای ادامه عملیات نظامی در آنجا،…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656024" target="_blank">📅 12:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656023">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39d0b8201.mp4?token=flEa1bappwPqgpBCHgexoDr408PfaO2CvNN6SvwnN7S4TPOXoiDUOk8GeWqQVF7gXAbtI_cnJNrGORl2EIQxiOo4XO34IpKSTtYf-XCMlWqgyhrZaFWXuS0G-h2gafJvCza31eOfz6CW48nBd4w2WNRPii51TzuynXFL_WypmEtFOkpGqJ6WPV5zo0HWW5ffmbIcG52WpXTqMYtEwRJ8GKR4NH66400Ak_G4gv1Dcr6ni11PkfFBPpRHtuiJnHFUF76CtixHir-sbuVChGc81ReM022KDOLaNHbKQi1YyyC1M0OTWa_vq4_9bW9B2eulwhuzDpcNcT8JTr-pHFs6SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39d0b8201.mp4?token=flEa1bappwPqgpBCHgexoDr408PfaO2CvNN6SvwnN7S4TPOXoiDUOk8GeWqQVF7gXAbtI_cnJNrGORl2EIQxiOo4XO34IpKSTtYf-XCMlWqgyhrZaFWXuS0G-h2gafJvCza31eOfz6CW48nBd4w2WNRPii51TzuynXFL_WypmEtFOkpGqJ6WPV5zo0HWW5ffmbIcG52WpXTqMYtEwRJ8GKR4NH66400Ak_G4gv1Dcr6ni11PkfFBPpRHtuiJnHFUF76CtixHir-sbuVChGc81ReM022KDOLaNHbKQi1YyyC1M0OTWa_vq4_9bW9B2eulwhuzDpcNcT8JTr-pHFs6SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مازیار لرستانی درباره‌ی تغییر جنسیتش: تا ۴۷ سالگی خودمو تو آینه نگاه نمی‌کردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/656023" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656022">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
دسترسی به اسپاتیفای بدون vpn ممکن شد
🔹
بررسی‌ها نشان می‌دهد دسترسی به سرویس پخش موسیقی اسپاتیفای (Spotify) بدون نیاز به استفاده از VPN امکان‌پذیر شده است؛ البته نه روی تمامی اپراتورها.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/656022" target="_blank">📅 12:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656021">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/casd51aG3RGW3q6UNwOc4YKawSncveQEQ6GzgD4fb1Rm5ikoy5E5nKrDiW0_rJ2pvu-J-bpmERwm_xQQChB3ruDEEjkl46iJEjhFSorv1ixLHAAVJXgQIy9T4rG3hAutfrRMcBp_D1B9XYaCEpfMj75s985qwMOFtzoigfrWONikCWrr9CcEUXrkqVCZRKWj62Lpuc5LD-5tyWdF4HuC7g8kvmx1vZGR61pQqdSNM4FJZ0AuEPWo3ic83XIKNsLVUKkI6rt6fUGcjPIXkWzzWpSRr5U4kue2YvWHHJ99Inuhj5pL1zvqJ305W7nIf5VBGWdEuVpHTkAJtt4Y-Put7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام دستیار رهبر انقلاب به مناسبت ۱۴ خرداد و تحولات آینده کشور و منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/656021" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656020">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
دستگیری عاملان شهادت مأمور کلانتری باغ‌فیض
فرماندهی انتظامی تهران:
🔹
در پی شهادت یکی از مأموران گشت کلانتری ۱۴۰ باغ‌فیض در شب گذشته عملیاتی برای دستگیری عاملان این جنایت آغاز شد.
🔹
مخفیگاه متهمان متواری شناسایی و  هر ۳ متهم حاضر در صحنه جنایت در محل اختفای خود دستگیر شدند؛ متهمان در تحقیقات اولیه به ارتکاب قتل با سلاح گرم اعتراف کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/656020" target="_blank">📅 12:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7690bfcd4a.mp4?token=TjxVQDf0AU3_qmfDJKzsoO2GoJt_XTfuLC2ZEvVvmDymtuJkjRRxBbQf6VM9fZfIUN60kYg2ovAjooxVRqPJBZkZYTaZ_KdDHVVarA3vv7-BDczYRP9KdWBQpRAvwTegiACanpmBQTl5S5w4LermcfqXP9NkvLWiVY-OPeLRmRyyJ8dpU2KKMaGue5YGrLMEENSe6ECXFyMpU6cunPaXF4WmM-QSPmeWqQFrOrFLcK6rX-noVxGjWye2VARx5JSfy_CmJS6vs8KYg-9tbrRqATNwQjwzC_ZbzZF7uoDmKsglTPCGxeGlL3NC3mUv6iYcquf6TCcYKvf_60wGnfGNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7690bfcd4a.mp4?token=TjxVQDf0AU3_qmfDJKzsoO2GoJt_XTfuLC2ZEvVvmDymtuJkjRRxBbQf6VM9fZfIUN60kYg2ovAjooxVRqPJBZkZYTaZ_KdDHVVarA3vv7-BDczYRP9KdWBQpRAvwTegiACanpmBQTl5S5w4LermcfqXP9NkvLWiVY-OPeLRmRyyJ8dpU2KKMaGue5YGrLMEENSe6ECXFyMpU6cunPaXF4WmM-QSPmeWqQFrOrFLcK6rX-noVxGjWye2VARx5JSfy_CmJS6vs8KYg-9tbrRqATNwQjwzC_ZbzZF7uoDmKsglTPCGxeGlL3NC3mUv6iYcquf6TCcYKvf_60wGnfGNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غدیر خم؛ رویدادی که تاریخ را ساخت
🔹
برخی لحظه‌ها در تاریخ تمام نمی‌شوند؛ از دل یک بیابان آغاز می‌شوند و قرن‌ها بعد، همچنان در حافظه ملت‌ها زنده می‌مانند.
#روایت_غدیر
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/656019" target="_blank">📅 12:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656013">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lw_CWSBHFN1Eay8kpAlENDhWMiK3qTKmNpcnAM4PvNgnI7POXzaz00VOBztEFQYUbVW9dgTTOQX9aRv-7X15RQ75hVKE0W8JseBoOt_m7vZ4BYQ0-axJSwL-MydKMjNxMPnNdLjBysppDDPQNRllwulNXVVGqKv2HpRxNXMDQChoW81eOwKVCdAlmHZai4M9_EGziYlShTDmPhKJ2Jw_JHe5dBlsVHXzUDFR6mo8yCH_INnQieV_kSrPQvs6qiSoyl2CFFNImqCz82OOszqBmygMEo-xQmvaK29IWooC1W8ctlZLeldYx0NJFsmfbtHYU0NEsOBy4CFCQvVC7IDwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqkpQ9pZObupMVxWo-w4Cb2-elpZNf6qnmqpe_BmAUC__CuLFngw6rC6rEvTjl1xzygSKCNNBsOMnDUH8bhtaCuVdYSGjvJK6yHoD20uPSxZQgVTdNPDiRi5K1b8R8-26YX7Sm8c2waRyCuCqVsOFMbikU4JxQmz9Y0m_M-e-Rkn-O7TutahCXSiRa4epvPK-jhNCHsDDW-0wZK5Pe_wTIvK1OmEzWcUDTl0BrHvWT_Js5f6GDE--bXdHlZl3kvMrsQBeWgNwUADuey-F9An5jhYtzuI6I6pKSV907dZ6qKr4tnnQefYBWGvm8mL_KCzqq9_ilGDcTY0kqbixPdRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0-RI0tAaPuXmsX0Cx2uOFLHgXUnP7uMVyRDsvkIkqLSYC4qD-IQHuOYwpUNCkywY7ei1cs7Uz6JAM1WcxjTK1Jg-mhAou-il9ix-z6rqVW0Z8T4Pio6DKFjSpXYkXAbhLxdggTaR3RR_ee41tHRW81a1naiXX8rqrFZzsoSmxfrV5sJH_jG3ckmCAYr4Szw5CiDkJwFpcPZIWwgC8rl4bwRLL6Em4okLP8tw3Ka7Hu6dDxMTcAp5uwGYcvW6IjnKEBJAA-4rnfX14SqitPh143ZhcThbuO_eOYAR_ZwaVKHVyf_8K5Z_SECA778-hrjLlhs1PRGcqA3Pdpq751wMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXDSS8XCMIFpebZs-r88zkDCxpJfdICAb3r_u9Bcuav9w0aXdTkdCAu7v6YK6LvLH-TNUbN2uT_Q-xKYpg8868ji0pxIAnP8kFl0XxIFSjcD5qHgqdMX3CWvWSLZVh0wlki0LznhZljkYnUna-gKBUUzkhqFAwWHmhPM82w9k8C9rE_LaMTWPkeElPdglhddTdnV7iLrA1yT5WvEkJmpce19szCmqqtjl0yuuRwhf5yw97OapwhjfJuIhb92oGKrceAD9RTopwdQv7cKZllRnwwllRQN1g1_q97734CtBmSudh8aO6zO7X-KGAhQH9zjCPO2BFrwUV1tEHXRw5NExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLBu-MC28Cfue8bJzZZjr9rcAOc0BvchnRlIeyNnw-uxGaO2x9EmqMCBt4J6SqG-xiaYCHv69rxQCLHSSXd6-4CcjaFIJEU75TIu-7CUMH0Hb1yqMxHJyTS_ekhI_CrZfPKLEZblXTBzBN7q54XovjaOhXlbGYNr2IjlKqAdoxhs8xwXJjt5iI3UxeFJ_i6Q1XzPLqcV6jU36Bq4gZF1N1nWqo97q-wsN1xYpWTxCuEkMGzdyn3Q4hAtMOvLxFfVZdjmZBI6sA8w7-a_FfyZY8QgUBNZnOEJPRBFMqgpNjzx08XMlQMb1-V8-z9sW1aMDFSiAkLJvqMGHC72oh_vHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a6yJWiClwV78iubQbmQGAjuxGmwi-cubV8eevc6rVFVuZOO-suLXglm1yFXcR5kuLYVB2EWPIg59tGNQ0ICaiTR3MYTsiYpdBVfd6abjzIIeDrQeLv8_Ikdh9-ycvTK339BOI4kN4UdwitM3tgfhcxeOZ3bqHRdfuvKzqG9qL0yhNRHAVgUPmu9HUnWUnQOvfrGqCHb9OwE22fo-M67foZS8pcAr8FYhEducGegmZxMXhMkWk0P5cbDFDgxvCnxvPdlfKbOeyeW9PR0i00N6cg_A_wU1j_n6nrNhOFHMHLBcIDI8oVW6x8qJgJAF2O7KCK3ekxPJEylcQBuumYOtjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حرم مطهر امیرالمومنین(ع) در شب عید ولایت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/656013" target="_blank">📅 11:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656012">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af4175881.mp4?token=cFJFgrcg2fseyoOx48peEpV5s1nM9IpQil9dTldpbXI-CIhyyj-94AtGnUSnCVRXKdpbKUucvxlpQ1LyCFqYYvsantASnZ-V7d3oQehtEXoOcgd2jNfNzIszoXNaW2CJ-bvW0ZopXRdluWPozq2aKktQv6DGjJn0p6n9imsxhQlD6hyTWnEOK4mIKTQ0fhFvk793ZD5DCYMaUyuNMyhdn0Tt4lXqVypM3zpp6ONl2Wsl-Fi3wGfWlI15_sY3gIeT-1_nQVJ2YEpa0KY8CFRY_vHy4eUq-HEXj3z6IGmJe7cDE9l3Z66vQAZtK6POVCS8TqwgNXPHdWM8HMoOaewe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af4175881.mp4?token=cFJFgrcg2fseyoOx48peEpV5s1nM9IpQil9dTldpbXI-CIhyyj-94AtGnUSnCVRXKdpbKUucvxlpQ1LyCFqYYvsantASnZ-V7d3oQehtEXoOcgd2jNfNzIszoXNaW2CJ-bvW0ZopXRdluWPozq2aKktQv6DGjJn0p6n9imsxhQlD6hyTWnEOK4mIKTQ0fhFvk793ZD5DCYMaUyuNMyhdn0Tt4lXqVypM3zpp6ONl2Wsl-Fi3wGfWlI15_sY3gIeT-1_nQVJ2YEpa0KY8CFRY_vHy4eUq-HEXj3z6IGmJe7cDE9l3Z66vQAZtK6POVCS8TqwgNXPHdWM8HMoOaewe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جملات معروف رهبر شهید انقلاب در مورد امام خمینی(ره)
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/656012" target="_blank">📅 11:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhgf9jobYjCe9EqGSuYfd5AnaOWK_OWSAjaJHvAhanPokJL7binXpEp8Q_tp8nUNknsM-j8bPdtS4Y9P4-UJva5jLDIRTauX074HVZA0zOHc-rH9juqdYj6vmVWayhgGc8J3hX1XUoje0UL9PoDeuRbgh27KWRqkUCiB6fpoUWwpIJijoOfdgro5pYJYE7UFAmR5heqtLR3mpglT_XhOZFTBRevP-UuTevwRzFE6lET02A_rFsP8HvvVL6mBzCJJeAS1yAqYaOBfYqdfbe2wZ_t_GvSjOPy8t7uNNHYO5thdqBjwyTBpLRiGAjJip9rLhmVMO_FWP9Gc2DkoktZEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23a3791278.mp4?token=ivu6G7Gh2GyhC99DeYbA6RAuEiuRrjj3PLxwKT785Ix9CJjmOjS9aSFLnikLG6Pzp1z3Fk6Saad3-Ilc9s7SHAh4gYVeRjrb35p9cNGhZQJH0inLG-yjaaP6bbCZjA_avk9gu6lvxUOXOss0YvvogEIg2qOi2-w7WBfGAr4HiYpGzGK9eNyURrPDjM-Hztrxcaaw5FfKT2kdWylxU-uv0BKjcyMTwYx5Hl_AEqTHgYT5Wa7sagwtKNQFHqzq7IdYQLl3fFVlIfHONoXoT2Nh1HTAzwD9tSW9RTrRI4lBwDZLMfVnd_KkwbIbH7rZzjoLC3G33wOE4qLppwiMmif_xw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23a3791278.mp4?token=ivu6G7Gh2GyhC99DeYbA6RAuEiuRrjj3PLxwKT785Ix9CJjmOjS9aSFLnikLG6Pzp1z3Fk6Saad3-Ilc9s7SHAh4gYVeRjrb35p9cNGhZQJH0inLG-yjaaP6bbCZjA_avk9gu6lvxUOXOss0YvvogEIg2qOi2-w7WBfGAr4HiYpGzGK9eNyURrPDjM-Hztrxcaaw5FfKT2kdWylxU-uv0BKjcyMTwYx5Hl_AEqTHgYT5Wa7sagwtKNQFHqzq7IdYQLl3fFVlIfHONoXoT2Nh1HTAzwD9tSW9RTrRI4lBwDZLMfVnd_KkwbIbH7rZzjoLC3G33wOE4qLppwiMmif_xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل ۶۸ متری آردا گولر به الچه به عنوان بهترین گل فصل ۲۶-۲۰۲۵ لالیگا انتخاب شد
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/656010" target="_blank">📅 11:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPhzB1LvKwfa1Q9FMyWWe-pRveUG2dZhdVxEY605z4bC57tbG5VEAemyKjGOsgGQ3XN70UyzRRRmHwNSBV0R39R1AG0zk6cRwKVvUwJxpEk62wN29kZU63PB2iD9QDtVgnDCyLwgc8W08wB5hRPTmBPlEYagtCdBFoGME7hOlICKiKdK6_LxU6fmt9QYop1mpmBiZJZwzVfy2W1XirIazUrB8-QqDVX37tmbLNU8okMSh2s4AWl1O2OCIGhG_1w1FqCWsKqBPo0asHm7h2a4yMnGkj0e66D_22lNkT837yVCUleY106MGkIm1LQsfUdS1eVvLeJg87N5n65GHU7IWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات رای‌گیری کنگره برای متوقف کردن جنگ ایران؛ ۴ هم حزبی ترامپ علیه او رای دادند
نیویورک‌تایمز:
🔹
مجلس نمایندگان آمریکا روز چهارشنبه طرحی را تصویب کرد که به موجب آن، ترامپ باید نیروهای آمریکایی را از خلیج فارس خارج کند یا برای ادامه عملیات نظامی در آنجا، تأیید کنگره را کسب کند.
🔹
این طرح با ۲۱۵ رای موافق در مقابل ۲۰۸ رای مخالف، ترامپ را برای ادامه جنگ در ایران محدود کرد. آرا عمدتاً در راستای خطوط حزبی بود، به استثنای چهار جمهوری‌خواه که به همراه دموکرات‌ها به تصویب این طرح رأی دادند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/656009" target="_blank">📅 11:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzFq8lN-u-m7FoB_OSVa7nfvCpzXjBUs3Mq1hRHOOfXlwF5YfRwNlSewUEtoIFdFYYEJL3HY9sN6gE2aF_z0x0MXPcnqkI26U2LcYdWBPoSFTAOxZHZXQSc0QtHKGAdv3dlBMEUHB6hAdTc8PNI_6lsR2T6BFnS0WE5On-9JdbngqerLw2Uu8Ykgh01moQd94T_22yHa69ExBU1SuKGlZuH3e31OH7AiT21wwrJGSC5UjYS4dtUlUwo4tx6mgSEbTlBhFWDKw0UsAGr6hjj9KU9FceeK59df_b9CZMEieba_ik2anTdZFSw3REbFuE386HyTXPji8MFVtLvJTteRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشهدی‌های عزیز امشب مهمونی غدیر رو یادتون نره...
🔸
از ساعت ۱۹الی ۲۳ در حدفاصل چهارراه نخریسی تا چهارراه چمن
🔸
با حضور هنرمندان و چهره‌های فرهنگی و هنری کشور
🔸
۱۱۰موکب پذیرایی و فرهنگی و تفریحی هم تدارک دیده شده...
منتظرتون هستیم...
❤️
@Heyate_gharar</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/656008" target="_blank">📅 11:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-qtc5M0f0qVWFlAz2KsU_jWZsSUZrexHkAgOnA_w2svPa9EvCsq71f22bsn3nHhbWwvrJAN8920U4aKYCQ_3ZKuu0vtZVSjzPuzKTufyHCaDIDnB_tI_Ul5zKdxX9icvpIbJJMVCXFNo5XjAQn4-iN2wG19Mo392z5CvzcVBNx5GdImISS0R8xXj3lWixwA5PWT7e6zrZ4D5rkgHTWTc9AeK2_0Xx6s6tZgaRtQlMNbMQ8r4Hsy7LnIfe0pZeH4weIIDCP1eU_HOOyVYdnVLg89P-C6jdAVjNJyuPIIxpoTGqbwXogAIDVEQHt_P5D7cnUeah0ym-pDClz4yumRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نقشه‌ای از جهانِ غدیر؛ از نجف تا پنج قاره، یک پیام و میلیون‌ها دل
#جهان_بر_مدار_غدیر
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/656007" target="_blank">📅 11:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/656006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر انقلاب اسلامی به‌مناسبت عید غدیر،   سی و هفتمین سالگرد ارتحال حضرت امام خمینی (ره) و آغاز رهبری حضرت آیت‌الله شهید سیدعلی خامنه‌ای | ۱۴/خرداد/۱۴۰۵
🔗
farsi.khamenei.ir/news-content?id=62998
📲
@rahbar_enghelab_ir</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656006" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
رهبر انقلاب: از خداوند متعال پیروزی نهایی ملت بعثت یافته را مسئلت می‌کنم
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره).
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656005" target="_blank">📅 11:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
رهبرانقلاب: دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است   پیام رهبر انقلاب اسلامی به‌مناسبت سی و هفتمین سالگرد ارتحال امام (ره):
🔹
دشمن تحقیری پر معنا و عمیق را در میدان و خیابان تجربه می‌کند اما کید خود را در جنگ ترکیبی در…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/656004" target="_blank">📅 11:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
رهبرانقلاب: دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است
پیام رهبر انقلاب اسلامی به‌مناسبت سی و هفتمین سالگرد ارتحال امام (ره):
🔹
دشمن تحقیری پر معنا و عمیق را در میدان و خیابان تجربه می‌کند اما کید خود را در جنگ ترکیبی در دو نقطه تاب آوری مردم و ایجاد خطا در دستگاه محاسباتی مسئولین کشور قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/656003" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رهبر انقلاب: همگان با ایستادگی، روشن بینی و حفظ وحدت و اعتماد متقابل و هم‌صدایی نکردن با دشمن نقشه او را خنثی نمایند
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656002" target="_blank">📅 11:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656001">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رهبر انقلاب: رهبر شهید چهارده خرداد را به فرصت میثاق سالیانه ملت با امام خمینی (ره) تبدیل کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/656001" target="_blank">📅 11:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656000">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
رهبر انقلاب: ملت ایران با بعثت تازه خود در کنار جبهه مقاومت مایه مباهات ملت‌های آزاده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656000" target="_blank">📅 11:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
رهبر انقلاب: خمینی کبیر و خامنه‌ای شهید آمادگی ملت را کشف و احیا نمودند
🔹
قرائت پیام رهبر انقلاب به‌مناسبت سی‌وهفتمین سالگرد ارتحال امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655999" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655998">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe4240b41.mp4?token=Y6BY86LjdpBvvcxQjqdRUxduvYD8Wxvtzd3BkUWQVrB9welPyOOuzMD7GIhTrgmlRO9udlmGVpsA3Kb5lOQIUKr1F-6YzmZf7s8bJOw0jjBAAHTw_xpmI_MTD6iTY4ZoDi92C7aYmvRazhE5jB86Y2x8oCwIFx6iXQ04cw7gtkyG-yuEbo8eEmSIH85UrGa1JDHL4K0CdPuNxoYXzxeWWP1sTW6sPX4JYPIvUP2gEOYvfhkAPXuHPt8AvtIDYrxfUmPK5Eq_8Zp29mQctWiGMUaeydDAX5WUoB5Jkisbqe4ZI3ii1CkjWK0f5qbqNGrHQWJarX08CPRjBu6NUv2MAaF94DFZ7wL1rXQjckV8RIpi5WBxJGRVshNhv2Jw0kputWom4LoYKPlDplVfgqh8oFwkja2QFVqZkyUxi5gq90HsvTcWtYBX5X8eUuLQDkKHf8jytn8KSu6uW6edZX_zg0gMpLR8g_1O_EcpauJsP2mhzmRV3PeM5EeowYbyLbuEOHUqiUb7hHZNBLaZSbP35mY4h6yXhI28Yja4dih5CGnI19-MzyCZcu9NLo_9a1XNiYqBqL5nesHQSGmOOo72-UepcH5ZC_vb606z-dcJg_9Je9uLmUHjoJUhYopIDm1WEs4W08sqKSFQIsqIdDLuxGvKFHID8nf2ERc8XJmvOZk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe4240b41.mp4?token=Y6BY86LjdpBvvcxQjqdRUxduvYD8Wxvtzd3BkUWQVrB9welPyOOuzMD7GIhTrgmlRO9udlmGVpsA3Kb5lOQIUKr1F-6YzmZf7s8bJOw0jjBAAHTw_xpmI_MTD6iTY4ZoDi92C7aYmvRazhE5jB86Y2x8oCwIFx6iXQ04cw7gtkyG-yuEbo8eEmSIH85UrGa1JDHL4K0CdPuNxoYXzxeWWP1sTW6sPX4JYPIvUP2gEOYvfhkAPXuHPt8AvtIDYrxfUmPK5Eq_8Zp29mQctWiGMUaeydDAX5WUoB5Jkisbqe4ZI3ii1CkjWK0f5qbqNGrHQWJarX08CPRjBu6NUv2MAaF94DFZ7wL1rXQjckV8RIpi5WBxJGRVshNhv2Jw0kputWom4LoYKPlDplVfgqh8oFwkja2QFVqZkyUxi5gq90HsvTcWtYBX5X8eUuLQDkKHf8jytn8KSu6uW6edZX_zg0gMpLR8g_1O_EcpauJsP2mhzmRV3PeM5EeowYbyLbuEOHUqiUb7hHZNBLaZSbP35mY4h6yXhI28Yja4dih5CGnI19-MzyCZcu9NLo_9a1XNiYqBqL5nesHQSGmOOo72-UepcH5ZC_vb606z-dcJg_9Je9uLmUHjoJUhYopIDm1WEs4W08sqKSFQIsqIdDLuxGvKFHID8nf2ERc8XJmvOZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انقلاب: قیام لله زیربنای مکتب امام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/655998" target="_blank">📅 11:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655997">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf43b60997.mp4?token=NfBlnoF0MMkW4oSRIywPPI0JqQkovIP8ax2uFYREYp7TKOZPF65xME9ofG5foo1RlClpk5FEOgGKOEghGZ5s8ZRyD_RmD-bkjJ23xioJRFK5l5ldrQHJvq32juPIVHiH6k0r9xqn7pb0mJiUSLp5rQzfraHjEn0o5u3DMxHbiFEs8MDpl8vXkqWuQM4mUtAalXtUItZvkPT98ZlxNuU8Pz9DKrz6A-OQlBqdCgObXjSa9v30T1vjXZv3Dhyxh2Xq-ZCoLptRdaIbRclNhNzFIuRLGusZw7cEFXKTZC5z7pibU9dyYaAj_mhWWbllxtG78W8HPpjRGf8vQ2NnGf-f-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf43b60997.mp4?token=NfBlnoF0MMkW4oSRIywPPI0JqQkovIP8ax2uFYREYp7TKOZPF65xME9ofG5foo1RlClpk5FEOgGKOEghGZ5s8ZRyD_RmD-bkjJ23xioJRFK5l5ldrQHJvq32juPIVHiH6k0r9xqn7pb0mJiUSLp5rQzfraHjEn0o5u3DMxHbiFEs8MDpl8vXkqWuQM4mUtAalXtUItZvkPT98ZlxNuU8Pz9DKrz6A-OQlBqdCgObXjSa9v30T1vjXZv3Dhyxh2Xq-ZCoLptRdaIbRclNhNzFIuRLGusZw7cEFXKTZC5z7pibU9dyYaAj_mhWWbllxtG78W8HPpjRGf8vQ2NnGf-f-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انقلاب: درک و شناخت امام چراغ راه آینده ایران اسلامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655997" target="_blank">📅 10:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655996">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b13b3815e2.mp4?token=u7unjYUXTs6H67xii7PuDVoyYHbqer48aAvepE5Ga1x5eCBIyLePA71BCwzTJxGHS1p82MykyypXRXtsTRU9nh_68ZchY7rv_mgKDbqMp9ScC7XbEl7cfoqhunNOuNL9cqHaS0dFSD6LgDQ7ZA9WTjSKd2s7I9mV3SimROh2d1CWFtPQ6Y3uTVQgJuTD5t8u7v9kpicTb6TLo8L2K6nzNZaBi16jVZKE7RVbK94jij3H46u43u1avxQoLNUyf8uVjjlPsI5j7lxGv70F3c8Osh9zZ2VjbsQQhQBviJw2KaD6bTeJtxSVEIHwgvlm1jNjdG_5uUrkFzoZJN2kPQbyoaNafaIfcGmynwN8BKELSEkPBiUOjAAE0KkRw_ORYr1JkV0H97gVWFe0pv3eLyZtQd0-iwAOykXx8gxWtW6Hjnp4crgjNf-iFnTGVFfxNKSoiExleiacSUfhgxJHW5EW4iGe0voH-OGJMw1DlcIP3MEH4RqOrQrOteM8kAFhiTIPzr7fG0aH5u4H7ELVgJYrjtDB-h3lN4QWUyJipEXOv4wECyktozqtKEdg7OIHnmx0n_fUEptGa6ckjGahlsMdTFelbnhT0NLFV8L6jM8MN7bHb9yCX1KgTJg2Fw3sCz2zlyGWSaE25tDu3Y0JdQX6WAlhzaedb_zaagwmXEfgV2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b13b3815e2.mp4?token=u7unjYUXTs6H67xii7PuDVoyYHbqer48aAvepE5Ga1x5eCBIyLePA71BCwzTJxGHS1p82MykyypXRXtsTRU9nh_68ZchY7rv_mgKDbqMp9ScC7XbEl7cfoqhunNOuNL9cqHaS0dFSD6LgDQ7ZA9WTjSKd2s7I9mV3SimROh2d1CWFtPQ6Y3uTVQgJuTD5t8u7v9kpicTb6TLo8L2K6nzNZaBi16jVZKE7RVbK94jij3H46u43u1avxQoLNUyf8uVjjlPsI5j7lxGv70F3c8Osh9zZ2VjbsQQhQBviJw2KaD6bTeJtxSVEIHwgvlm1jNjdG_5uUrkFzoZJN2kPQbyoaNafaIfcGmynwN8BKELSEkPBiUOjAAE0KkRw_ORYr1JkV0H97gVWFe0pv3eLyZtQd0-iwAOykXx8gxWtW6Hjnp4crgjNf-iFnTGVFfxNKSoiExleiacSUfhgxJHW5EW4iGe0voH-OGJMw1DlcIP3MEH4RqOrQrOteM8kAFhiTIPzr7fG0aH5u4H7ELVgJYrjtDB-h3lN4QWUyJipEXOv4wECyktozqtKEdg7OIHnmx0n_fUEptGa6ckjGahlsMdTFelbnhT0NLFV8L6jM8MN7bHb9yCX1KgTJg2Fw3sCz2zlyGWSaE25tDu3Y0JdQX6WAlhzaedb_zaagwmXEfgV2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر انقلاب: سند افتخار زندگی امامین انقلاب تأسی به حضرت علی (ع) بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/655996" target="_blank">📅 10:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655995">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/212666adfb.mp4?token=TUR0idK2_8mozTvNnYQq0cxAkoxVkMkpqgvWcoIRfh99mRHXHj_g5_WX0SRIeyy6PkUSwb3J-ajF1p1G2qcyCAzHLR109CWTxtD4cMDEG_yzfnEx3cHbAoL8WVxyqT6U8CCqCxr1lq0PLDTz0E8ieA7mpCpy7j81kCoOW0AWwXH_fR_Z-KJMN8Vm_mrbrUFf9Z3gncwSLy-9uwZvlyUGOeQlH_oYHK7ejaGIwn8vGPk5Fss2JSOrYS73UxMXC8R1FZJcNK19X28zqvDl2GKETgdNsRRDdVBgL-fcxIO6LOVhpwOL84c6biMuTYrftDn0virYvtXlHZ0Ze8hE4jBvSSmjVLO0kUbDwCvFvRbr09atHfCAZPfORofefbJ8rZvhNrsKv8NZ1BHKWzJpI9kKSvo8nqTRqXDRd5t_ieNd7udvnkFI3fp_7p1dF2XKHuRfBqtlJwx5y3dJRMca5jjuvwZrtfvtgvnPuS6juIwgVkG2KYCa44lw1sS1DiCG8qMkcGGy655La7PWxOjMR7tCGEDgzWRhlHt-5cPjYqUD6nq13tNfW60t6kZDbgGV1fP6-FHdF-MGeuJSi_YTFET0kb7og0rImXuZU47CKjUuDBHj163KNihctzO0899xAWVUJ0qnSWvEcN-Og-IcGb0YEWDwRYSbvhq1EvsBEWF_zx8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/212666adfb.mp4?token=TUR0idK2_8mozTvNnYQq0cxAkoxVkMkpqgvWcoIRfh99mRHXHj_g5_WX0SRIeyy6PkUSwb3J-ajF1p1G2qcyCAzHLR109CWTxtD4cMDEG_yzfnEx3cHbAoL8WVxyqT6U8CCqCxr1lq0PLDTz0E8ieA7mpCpy7j81kCoOW0AWwXH_fR_Z-KJMN8Vm_mrbrUFf9Z3gncwSLy-9uwZvlyUGOeQlH_oYHK7ejaGIwn8vGPk5Fss2JSOrYS73UxMXC8R1FZJcNK19X28zqvDl2GKETgdNsRRDdVBgL-fcxIO6LOVhpwOL84c6biMuTYrftDn0virYvtXlHZ0Ze8hE4jBvSSmjVLO0kUbDwCvFvRbr09atHfCAZPfORofefbJ8rZvhNrsKv8NZ1BHKWzJpI9kKSvo8nqTRqXDRd5t_ieNd7udvnkFI3fp_7p1dF2XKHuRfBqtlJwx5y3dJRMca5jjuvwZrtfvtgvnPuS6juIwgVkG2KYCa44lw1sS1DiCG8qMkcGGy655La7PWxOjMR7tCGEDgzWRhlHt-5cPjYqUD6nq13tNfW60t6kZDbgGV1fP6-FHdF-MGeuJSi_YTFET0kb7og0rImXuZU47CKjUuDBHj163KNihctzO0899xAWVUJ0qnSWvEcN-Og-IcGb0YEWDwRYSbvhq1EvsBEWF_zx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغازقرائت پیام رهبر انقلاب: اولین چهارده خردادی است که پدر مهربان امت، مهمان ضیافت الهی شده
🔹
قرائت پیام رهبر انقلاب اسلامی به‌مناسبت سی و هفتمین سالگرد ارتحال حضرت امام خمینی (ره) توسط حجت‌الاسلام و المسلمین حاج علی اکبری.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655995" target="_blank">📅 10:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655994">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
پیام مقام معظم رهبری به مناسبت سی و هفتمین سالگرد بزرگداشت امام خمینی(ر‌ه) تا دقایقی دیگر در حرم مطهر امام قرائت می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/655994" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe969a8ca5.mp4?token=d7AZ6fH7BsWozHKqxJQsDAUEcJEWgr8opDznWIx-DLwezloKupP5oEEBdGgRUv8Bx9zFhtaBGzUD1tXFcI4TAgjgcxW9s1Cbs0hX9TDU68iz3c7lIvDRhvxOEVIZ9YaqpUiyU6KrEa323eXGtMkP7RKv_BxCMz_8qhE9XukrmdQB_cxxzbbX0ulv9-KBZU6drtuHOcgSeDXhRyxnbXerr46vPjfLixdVbiDGVY13Fmv2XuQiPOYnGTL91Ver8RSuV4FObVbkd8wm2C92XSZHupuuVhCcqzQlPlbN34KoQAPxpOD4N-9xzljxRjuCK0yFGqevykqnKN3BWHtSmZ24xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe969a8ca5.mp4?token=d7AZ6fH7BsWozHKqxJQsDAUEcJEWgr8opDznWIx-DLwezloKupP5oEEBdGgRUv8Bx9zFhtaBGzUD1tXFcI4TAgjgcxW9s1Cbs0hX9TDU68iz3c7lIvDRhvxOEVIZ9YaqpUiyU6KrEa323eXGtMkP7RKv_BxCMz_8qhE9XukrmdQB_cxxzbbX0ulv9-KBZU6drtuHOcgSeDXhRyxnbXerr46vPjfLixdVbiDGVY13Fmv2XuQiPOYnGTL91Ver8RSuV4FObVbkd8wm2C92XSZHupuuVhCcqzQlPlbN34KoQAPxpOD4N-9xzljxRjuCK0yFGqevykqnKN3BWHtSmZ24xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کشته شدن یک صهیونیست براثر انفجار خودرو در تل آویو
🔹
یک شهرک‌نشین صهیونیست براثر انفجار خودرو در جاده «آیالون» در جنوب «تل‌آویو» کشته شد؛ رسانه های صهیونیستی هنوز از علت وقوع این حادثه اخباری منتشر نکردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655992" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHUux9g5pU_tzqvovqN3M6U2q3SXYEKwFfaU8YDa1KelS-FxNSenGKkBacMX7kAPfeW1u-Bg9tzp-swhmJk1o9k7EK_84yvOKKx6BSw0zL68Wz5MdjghYFfomAce9K4tUwW_-G5v279Ud7Xp-rhsxImomtgwsWhtxye8oXfCCtH1seGb5W16LIW2O4s-Wrb06B0epOSbMIbFSwSrA80i8YhfHwg6xCRqgcPDIOrFFLLKa5oekr9LIyVMQXsbdw0qWriOJtcs486CX1cerNi_fA1znkjRiLTwD3FRaOqa4BORPItO4HSApKkyLuU2XxI-2N_SPs7a6edIAzgpdT7hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عزم بانک صنعت و معدن برای احیای واحدهای صنعتی آسیب‌دیده قم
دکتر شایان، مدیرعامل بانک صنعت و معدن در بازدید از واحدهای صنعتی آسیب‌دیده استان قم:
🔹
اولویت اصلی بانک در شرایط فعلی، احیای سریع واحدهای آسیب‌دیده و تأمین منابع لازم برای بازسازی و نوسازی آنهاست.
🔹
فرآیند ارائه تسهیلات حمایتی و استمهال بدهی‌های قبلی با هدف تسریع در بازگشت واحدها به چرخه تولید دنبال می‌شود.
🔹
هدف بانک تنها بازسازی فیزیکی نیست، بلکه بازگشت این مجموعه‌ها با توان بیشتر به عرصه تولید و حفظ اشتغال است.
🔹
بانک صنعت و معدن تا زمان بهره‌برداری مجدد و بازگشت کامل این واحدها به ظرفیت تولید، در کنار صنعتگران خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655991" target="_blank">📅 10:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e8261837.mp4?token=RVKViS-asKvwwfU1rPg3TdabofY39BHLKUzfSeUg3RcGgk32bTU2huzczCnCM62tLhsIrB_DymRcsGVLMNynPAw0hM9chHt6GXFnxD5fS8cNwmLa5TAZY5gZYV6k_zWtVC6b_5I_dBNzKNtEOAcwqSP1zkma-IgWqBVA0lU4wPoR6BOzZQMtpCyUK2akxf4t2y12OFdXMkydXMF9mPL2w9wu0GZqcvR8uMAud7nG91y3oWu8_JGR0E5em_oHpRv8cCE2xlYaEUMalsT230vd_slN21UxEOTaiQ4Q7w5EVZctNYpAXDbqpXvv9SKu3vobbKa0PsPWXkCXm7_gbkX3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e8261837.mp4?token=RVKViS-asKvwwfU1rPg3TdabofY39BHLKUzfSeUg3RcGgk32bTU2huzczCnCM62tLhsIrB_DymRcsGVLMNynPAw0hM9chHt6GXFnxD5fS8cNwmLa5TAZY5gZYV6k_zWtVC6b_5I_dBNzKNtEOAcwqSP1zkma-IgWqBVA0lU4wPoR6BOzZQMtpCyUK2akxf4t2y12OFdXMkydXMF9mPL2w9wu0GZqcvR8uMAud7nG91y3oWu8_JGR0E5em_oHpRv8cCE2xlYaEUMalsT230vd_slN21UxEOTaiQ4Q7w5EVZctNYpAXDbqpXvv9SKu3vobbKa0PsPWXkCXm7_gbkX3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیانات زیبای امام خمینی درباره امام علی (ع)؛ علی (ع) همه چیز ماست
🔹
این علی- علیه‌السلام- که در هر جا می‌رویم اسم او هست- پیش فقها وقتی می‌رویم فقه علی؛ پیش زاهدها وقتی که می‌رویم زهد علی؛ پیش صوفیها وقتی که می‌رویم آنها هم می‌گویند تصوف علی؛ پیش ورزشکاران هم که می‌رویم آنها هم می‌گویند که علی و با اسم علی شروع می‌کنند. این علی همه چیز است. و همه چیز ماست. و ما همه باید تابع او باشیم. در عبادت، فوق همه‌ عبادت کنندگان هست؛ در زهد، فوق همه زاهدها هست، در جنگ، فوق همه جنگجویان هست؛ در قدرت، فوق همه قدرتمندان هست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655990" target="_blank">📅 10:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIdZYRALGxA-pNXSy64bfp1aJUFju95GVZoPLg9vR0gsDCRPwil_VDWW8pLEvnQgvISrlNHiyo2_qluEyDsFL2HMX5zvsYAZjFWr94xhQt41BfBiaF8LI4VnTGeEodVC-OU6ofguw40wAvJwOP6NuFsVZJF6InCHDR6UkZDFs0DWryQAIjJCkYu9L2X0BGTuf2h7rsKiN3NdxQzdxzD3LZIfmJGgdwC6GBeb-JswclExxaFi8OhYu868gGLvtq9hxo4Biked2XqJnWDve_PnqUwFWSHalZqXE5oSes_18daXxhRaG_PK2DbfA4UFcUfogYEwrsr6PJerTm7zuaTd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/655989" target="_blank">📅 10:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_E0oCfXNkflIiMLaAV_DBcbf18vzMj5t2Sgx_GuK9GOaINXKlsnr75tuHbpzws3QiKNi4l9DdCMSiEJc1z9GRBE_3HrSZ0iafWNBmkmMWq0eAObaQiR9jIbO75WeYvwxfDyC6bKwSSmK8hI_nm1DMPPpwkc9SiHrJl8GK4pTFZ2ZA93DNalO4HqTSU20YV5y6i_1cx1lMRDkt8dHtdJnX3F9WQ5PqB7dty6Ye0JtGFhrkYvGheM6x-QsVqu7xBB49p7Ylax_vvsIHFmfo2L7LtvCTepNilmgWKhXjvySSbiCsxUgF41jFUqCQNLbXVrpZew_8mDfActLOKwAxIhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت الله فیاض درگذشت
🔹
آیت الله شیخ محمد اسحاق فیاض، از مراجع عالیقدر شیعیان در نجف اشرف امروز در سن ۹۶ سالگی در یکی از بیمارستان های بغداد درگذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655988" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8wJ_iVHVBZEWK_Qr9dsHuVZA3sDxGeTT3N33w44VnYS8YjCqehBYX0imzgY7_yPINupzs2eN3t--sHXyK2OEBq97dkEuCWpZVEGoi51kaOpSplRUmmCReYMYPQP0cTFrrmn3J-0O14QrDSyDirGP0kxHFTAkHgZm0c1fksz1mxWNeNLZfWuiBIvXGiXmGwVg2zcy8tYTelrjYwKi_tPYGBKjcnd4K90U5JaN0BP46heueQwxL5I7-Rosld-tLp35QGIlbM82k-D5E11iWh9aFiry4gQAeXb3i1PDwgVO5GCiNTYBchyLQkwxHR8T5R7B0H_TqVICZgOXXSDCduSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رتبه‌بندی تیم‌های جام‌جهانی در رنکینگ فیفا
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/655987" target="_blank">📅 10:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979e87b41f.mp4?token=mcVXVHUw4_3KEvBOO8x3Nj5nAYQ2alReI0pNlIz0w9COvWWE0eIDoAx6wBLyrm4TKuT28N9E69RGlIvzryMduX3lD8QeyrAydlGEf2GQ9jfelG_qneBCW3MerMYdhVAbN8P0cEBaiDsKAV8dlWTDJ2cxs2Q68vg3MDdw84DWDVnGhYbKFvLoPMLk6PI3VvnKrX3FrOfkwr17urQsshhnW9bwvLsXmixQpIzGRkJgkdLmv1PAPHMlSMwGRWzrQIlA5-ZtKLJfUAetsZZjLjzEs3XOruUeD5x03CieIZkfNQlRyUtQBLE33vAYonLVaF5DSxj1QOHwDbDUemoSUy8rIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979e87b41f.mp4?token=mcVXVHUw4_3KEvBOO8x3Nj5nAYQ2alReI0pNlIz0w9COvWWE0eIDoAx6wBLyrm4TKuT28N9E69RGlIvzryMduX3lD8QeyrAydlGEf2GQ9jfelG_qneBCW3MerMYdhVAbN8P0cEBaiDsKAV8dlWTDJ2cxs2Q68vg3MDdw84DWDVnGhYbKFvLoPMLk6PI3VvnKrX3FrOfkwr17urQsshhnW9bwvLsXmixQpIzGRkJgkdLmv1PAPHMlSMwGRWzrQIlA5-ZtKLJfUAetsZZjLjzEs3XOruUeD5x03CieIZkfNQlRyUtQBLE33vAYonLVaF5DSxj1QOHwDbDUemoSUy8rIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ جالب از هشدار امام خمینی(ره) در سال ۱۳۶۱ درباره اسرائیل
🔹
اسرائیل قناعت به جایی که هست نمی‌کند، قدم به قدم پیش می‌رود، امروز لبنان است، فردا سوریه، پس فردا عراق.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/655986" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655984">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ الصبوح الصبوح</div>
  <div class="tg-doc-extra">حسن عطایی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/655984" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
الصبوح الصبوح یا اصحاب
المدام المدام یا احباب
در میخانه بسته اند دگر
افتتح یا مفتح الابواب
🎙
#حسن_عطایی
#عید_غدیر
💚
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655984" target="_blank">📅 10:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655983">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQr4ekCczPr2r-Cb_P0JAkMhWxl2Ay_X9_3mB1R7BsJ21yMvmNfyJ9skjqpZx8uXRbuVpS_E6fh5EpK4TVCTEJtHaOmek7VJ38H8Q9JoVfFCXSozzRPpUOUCyKF6JQqEW24uTMA8UaDQt72UqDyGqg4WcrtNb3VUnMvSBk6UaOMk2_UgLQDRw6yI4ESDoZWx0FLJc39BH9AtL4Bm-bffOrzqeKsjby0lHbmwVoNDmZGMeOoMShj40EfP4ch3sswXO7rltCaXOoXzIMVznKyfRV49-IVgMW7ORIuhqVz2q-zBpML1WcPLThL3AjcemrP0OpSGCCHt6UmxzDyUFeMTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ کشور دارای بیشترین ذخایر نفتی در سال ۲۰۲۶؛ ایران در رتبه سوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/655983" target="_blank">📅 10:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655982">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38a7f9c8af.mp4?token=BgiQFWIYwGuciCmwDMfnrCIDCKTB71mGyMag3KxR4rTfmTABW_z4pnBXxSv_yRAUwtFV09Yi5FvX6McTjCYFEUJ0Ir2VnfWo8DhFFhAIwM8scBM5Op7AayItbIi-QbJXl7V6o8BOC3C6haxqDe6Mgs53Gn0tM2yr_OJ90KuxpYQresdotP8ffwjvjUpPBV0ft9UnZIVf95EVBfAmZs1R0_AdA5l6otQmu4ml91Q6fiNnWoA-XHiQzmlQu65oy5Icnwf6wjWhfRIrKh2spaAnsKhZRYyCDLfsdotbDDFlVoZrHT_dgv5wF9CbQEo9exOedG2ibszzBavOS9fgbxCTXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38a7f9c8af.mp4?token=BgiQFWIYwGuciCmwDMfnrCIDCKTB71mGyMag3KxR4rTfmTABW_z4pnBXxSv_yRAUwtFV09Yi5FvX6McTjCYFEUJ0Ir2VnfWo8DhFFhAIwM8scBM5Op7AayItbIi-QbJXl7V6o8BOC3C6haxqDe6Mgs53Gn0tM2yr_OJ90KuxpYQresdotP8ffwjvjUpPBV0ft9UnZIVf95EVBfAmZs1R0_AdA5l6otQmu4ml91Q6fiNnWoA-XHiQzmlQu65oy5Icnwf6wjWhfRIrKh2spaAnsKhZRYyCDLfsdotbDDFlVoZrHT_dgv5wF9CbQEo9exOedG2ibszzBavOS9fgbxCTXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بچه ها! قرارمون از ساعت ۱۵:۳۰ تا پاسی از شب شهربازی و ویژه برنامه مهمونی کیلومتری غدیر تهران در میدان آزادی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655982" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655981">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424979765e.mp4?token=XvIryGUXtLOGdE7JmxDLwhBhjTlNHI9QeVPnKG78lzWrc4acWywXMW6-K5ZFni1JDyBjh7A3fEts-8KcODxNC2LVRHNJ24ths00LyzhSKMiLjaNyZ1X3hA6sR9F8AZXUGzu2vqlZBZCDKTjzvEXTwkjD6UtocaMzjtR0Eu77k7OCIKTaiYopRE9X9bvZkHiTG_weuEs3YQ90K4w_8wuNs3Fr0hxcERjKGJ0XmSAyZ4TlXbsqutudPpCnxZml5ucphllQPGAzQcK5lwbASYaXtdh3bmZfhsUV-etPEsiunM281XWefvoQywJe41YvKwbLW8ZtMwC0cn_hEMojCFdKxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424979765e.mp4?token=XvIryGUXtLOGdE7JmxDLwhBhjTlNHI9QeVPnKG78lzWrc4acWywXMW6-K5ZFni1JDyBjh7A3fEts-8KcODxNC2LVRHNJ24ths00LyzhSKMiLjaNyZ1X3hA6sR9F8AZXUGzu2vqlZBZCDKTjzvEXTwkjD6UtocaMzjtR0Eu77k7OCIKTaiYopRE9X9bvZkHiTG_weuEs3YQ90K4w_8wuNs3Fr0hxcERjKGJ0XmSAyZ4TlXbsqutudPpCnxZml5ucphllQPGAzQcK5lwbASYaXtdh3bmZfhsUV-etPEsiunM281XWefvoQywJe41YvKwbLW8ZtMwC0cn_hEMojCFdKxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تولید یخ با دستگاه‌های جدید در مسیر مهمونی ده کیلومتری
برای اولین بار در مسیر مهمونی ده کیلومتری دستگاه‌های جدید ساخت یخ قالبی عملیاتی شده است و با استفاده از این دستگاه‌ها چند صدهزار لیتر آب و شربت مصرفی مواکب تگری و خنک می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/655981" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655980">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un5KrGe8TsDx3ux9zZos_aMWnZxDk4YzwIFeWOkAIanBaP-rBLrAndT3CoVwrYNvvC3DEisxvotyGrNFpOhqcHnROgdsLo5nz_K_R9AILESrAsMVQxKmL1FfdDzRQuwI0aulISJE9BrpX8aBIVUz8_WAQgZkGvaT4sWFPtLXH9xTSX9oyl5hlrGC92YxHGQLFnxpQ5RUUujRga8UqscrNwYg1D5i4SFQXGpALQW_N_mGqeD-tnjrN6EkQB-VhVB10xYkECHrNkaRJ28Ym_MUab1vsftJZkK6V78B-Fz_3z-XnhsggLuXLHbOumVMIS2mlWEzshghWzaVFhCPjaeV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور کشورهای مختلف جهان در موکب بین المللی مهمونی کیلومتری غدیر تهران
با حضور چهره های فرهنگی و رسانه ای بین المللی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/655980" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655979">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_cZs7Lhh-quSl77TjPbRaPpKCRl8oPNWSx-UGzUEePE4akbWDyAGY3yOvuVUL9ecITvdanqCWQzrGuR5X2fH3WJockwpG8NwHYth64guCdbZGZ3yrDqResbCNTpw-5JFIsYJpUVvNgkAXh1paEBGoycfna4cuFfzr_PtXj7paCmPr_gvyvKSMDiv8qn5IdQxvT-nGcyst1Xp8SEW2Bpki5Mt60RQRQ8GmEK3uJvdS4Fj8rfDMln0_AbquPuyYBHyURUDuE7On5W1rinbMdAbigRe4bXmesArp1t7BUuEBxtwhFlMb4fpcO-cn06EqqfOKCvbF22z_vi7rbfGXPRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوشش برفی دریاچه مام‌شیخ در دالانپر ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/655979" target="_blank">📅 09:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRfhGTX0c7KsK8W5kGNC-ej9rQ7fvuHDFPh2MRUzQi2MlKbI--syfM42fzRvMvRzqZTRSjWMBVmpOr56edIA3q_WDz10d7rffu65VxjvrnsL0iJlqvJi2dzqi9jxpnz4hJvM_R-yfmcuNmHoOv3eSokOUF0FFB2H3BODUjvSpOs3g1vFXeBIEgBIt1Njvazjvyqp4TAiQ1HcpKmf8tij6_cihW6jSnILdTVZsF3zZI3wt0Nin1rdH6K8jpACkA1JtLmz9swHN5n56dubuQcSJKg1LAeXQVQQwceWHjgE1yMSgj4C50KFdXT8mrfdLFk_-sbJRjPrNOL2iKiqwDAZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانی از آسمان
🔹
در مسیر بازگشت از حج، پیام مهمی از سوی خداوند بر پیامبر(ص) نازل شد. پیامی که خداوند درباره آن فرمود اگر ابلاغ نشود، رسالت الهی کامل نخواهد شد، قرار بود همه شاهد واقعه‌ای باشند که سرنوشت امت اسلامی را رقم می‌زد. #روایت_غدیر #فقط_به_عشق_علی…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/655978" target="_blank">📅 09:46 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
زمان‌ شارژ کالابرگ خرداد اعلام شد/ مهلت استفاده تا پایان تیرماه
🔹
رقم پایانی کد ملی ۰، ۱ و ۲: از ۱۵ خرداد.
🔹
رقم پایانی کد ملی ۳، ۴، ۵ و ۶: از ۲۰ خرداد.
🔹
رقم پایانی کد ملی ۷، ۸ و ۹: از ۲۵ خرداد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/655977" target="_blank">📅 09:43 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887fa91a3.mp4?token=Pimhilx3sj8U1SgtUPpd04al9dREAEbIT9hm5i0cXk6T47fsqdQMMIxvbrRbBd96dHBOn-yzGsTzv04TM6ducE6vVDpd5m10_q5Q9ZuEto4R-XUbxQJ3WzjWAq16YE_-u4slrHmy2Ww_WfcMSZ8kOqGCIRpa9hURmX7MtP2SDGb8BAI1k3QQIwLD5RgrT1DL01M5lCFU1-vI3Q0drnwD2b_M1edwvCjUyQwx8H041eL_IBi5rszw7BXWOEJzDpceHwrHd17cI5mP3-h7QmOKQWvOgRFBMfyxEPDuWeSECYsiKUqMYy9vhrb6QR44wILvFzx6LkZvSgd52XxNw0SI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887fa91a3.mp4?token=Pimhilx3sj8U1SgtUPpd04al9dREAEbIT9hm5i0cXk6T47fsqdQMMIxvbrRbBd96dHBOn-yzGsTzv04TM6ducE6vVDpd5m10_q5Q9ZuEto4R-XUbxQJ3WzjWAq16YE_-u4slrHmy2Ww_WfcMSZ8kOqGCIRpa9hURmX7MtP2SDGb8BAI1k3QQIwLD5RgrT1DL01M5lCFU1-vI3Q0drnwD2b_M1edwvCjUyQwx8H041eL_IBi5rszw7BXWOEJzDpceHwrHd17cI5mP3-h7QmOKQWvOgRFBMfyxEPDuWeSECYsiKUqMYy9vhrb6QR44wILvFzx6LkZvSgd52XxNw0SI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان ملخ در دهستان درونه، بردسکن
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/655975" target="_blank">📅 09:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8YWHvvNUQ25dpnAQQHgD47N7fmb1u8IqJbHk7GbFaH5UkhiMO_ZqNKGuKhe5rk229ljdCuMlQXOpcN_uAVl3EQsMpoRAodfOvVrC3A-RIFIF5e59h0bZ7cF8cET12hukqLB-Tnpqq9EX23tXyqeiRYmpONo2-mqZ9zN_4ey9zEOu7I8U5aC1rsCJp9iSBFV9Ct_9h-gg3MGQVkh8jr9RlnPuyhg_s-4SVF3KCf8ZsmYr9t2Cc06g6Wq5ZjPW3qlyoSQz0W_gGvlDUIVjSnY4zeAhD5WfuU0YPV99aya0RSxCOf7kcpEg5i0lAnMp5LUtk2coepTuR5Y-uAgJLZZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۲۰۰ملیارد دلاری ارزش بازار رمزارزها در ۲۴ ساعت گذشته
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/655974" target="_blank">📅 09:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kul_M8a7Xf7VzDUrMEAYzaC4K-IEors6Zh-DfraN1XDqZgzCByuKy1qArocmxJctqX626N2HNOp9c7hyefN3irHUtt3Esc3dbHB0r0_IIIp8sf5hHYvUNflZjbK13X-7myBuqF0T1Hc2BaRuYGWnSviO29WI-FqUeEupyTHDKLCVAMMccp-2NlK3AcsSTgLZBKz-a93kHqsQjTu2I5CzlRD6bYDpi2HG8WTftcfNWQoJ4c8_5Cr__f0wI0daP1akUujM0_enDTwLcBMHzJeRp2BeEQTfjNL9-UH8-gpDhUSCylME5YIpIWx8a7BbSMEKIP4I_5T6xS4oO_NmXQFOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیلمان، گیلان زیبا
🇮🇷
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/655973" target="_blank">📅 08:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b574136a08.mp4?token=XIQAH0W8-2QM3EsU-NmrDAMEoZytncbkRWjwcI_EhBvRBOo7aTHp9QQSGaBjdSOPGcnumgwn6bA_IlMghLfpIGrTETBUBIQRo6iRSxxLwxtrA8vXzfVoIt7Sy-DysjKQveEXblcu1XrD1478Mq_g_gpe5KNQzHYnZT3gVctIRAfeyVd2xiO6pRmEyZ2ZB2eCz4YlFHCXuGLuwGTOPsHksP4bGP0os3CBoRKdRDNZPzXOEXkpHflSQafnlBH30N7v81OmTAg6uk3dkmLkp2XjO7UjQnwDVo-U0E81ywAIKiPUznAlAD5vs2AbRjpWbygz7p6zGtvNaGSJLJo4yNuCgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b574136a08.mp4?token=XIQAH0W8-2QM3EsU-NmrDAMEoZytncbkRWjwcI_EhBvRBOo7aTHp9QQSGaBjdSOPGcnumgwn6bA_IlMghLfpIGrTETBUBIQRo6iRSxxLwxtrA8vXzfVoIt7Sy-DysjKQveEXblcu1XrD1478Mq_g_gpe5KNQzHYnZT3gVctIRAfeyVd2xiO6pRmEyZ2ZB2eCz4YlFHCXuGLuwGTOPsHksP4bGP0os3CBoRKdRDNZPzXOEXkpHflSQafnlBH30N7v81OmTAg6uk3dkmLkp2XjO7UjQnwDVo-U0E81ywAIKiPUznAlAD5vs2AbRjpWbygz7p6zGtvNaGSJLJo4yNuCgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اولیه از فرودگاه کویت
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/655972" target="_blank">📅 08:35 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
