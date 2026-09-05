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
<img src="https://cdn1.telesco.pe/file/GWBdriJHlNJWL9irtjG6cd1oTKd85SHuLdLEK03twVBME3rtRrn9UboeZsLHCxcubm9S6BwTqOwW2ENGeUAXzRfBMNA7NlbUknO1XqBdpb8pA1HIrE10G4WW3DMQmzzqa-GxmHPTAb1dlgZUjNXE4vadZmGiBoqqzczRDRI8baTyu7W17BCw_SrpHuFxzIjWkNH6j6oUwIC241cKqhuodbkEs1326dVWiF9NT96dDOACqEG_nUTEenBuHzKhUto5GkmDI3Hdri366ncN4dAfNhjc1rEYSwUEk6veZZ-i3IUepDeZSnuKTuTa7p9b6DPcBDwPlDGOd-Z-MxHmG5nWgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VJkgGKydP43D2StRwhmBOaugMa0EI6Uccg9lUtnG6oPeWAGVxyQDPrM-4Odrluu7WulOmWLlNTZvP2jvtrhn9KVpZJejqRYtFZU7dH823_bvfUz30zz30HA1ozfjLymEFLaNLRvHGSO45cgKH79GNGTriMbb9OgPjUrKM-W6PgEaB25m3bK0qkiDgEk-0Q3xWLmsCMGq1Suv6ePIIa5quZ_tVsl1FUZEj6K9KT63bBHnZQ7yJ0DqUF1DrzkDVPkm8WTU5XJwfj0vHfQnibqGxM9inSLZIe1uhtkY9RYikaYn6qiiqr69ZqiBg1EfkOmh9ONxuh55Be0BoPQ4WsEMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJHFUutslTShsbvS-2_brr1cbrQ7qH4qJZGQe-6nISuXCTclzH8pnFwnmHYpP-oYcamvX-CkGq4K28uDkYqNSzmLXBnRVVQqWHB9BKzneILn2zId3zdEucDFinzaxAnqsdKXhyykkBvi2eHH11WuLsLneHVUitQi4wkCV6t02vup5_tBmrBERUIAqlpYrNsfQYTb0OoF_xw0rFf4BLWICu3I3s8Py9FLI9spMNVYADJwuNzb7BZb4-wOgi-t2IyRapQts-WsmhcJx7ws6sHDF1PLNltzsNl5-dfehL5lzSR8Ye2hdWOkMAFsOQa9UGOU8QOkh1HtCML7pyEET2ISHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AA8r5r2UEgq5dmWsKsqZ5i6Jbu2hDhvaZPDjoybRJQ3gk_d3Qm1IYCup2OMmpX5mmCrxFqBMRu6o35-E8JXgsRSiKaOw5xI_1vDsZgiB-dxQPW_NIu6KSugHjazA1rVPpui-f-B7kGH3HlQc7jDTlDF0KAwQjC8hy2WV6g_Z7STSqkw5HnPYIoieUVkQK-ic35udjpsHO0fpFk00i_11R7TTQRTlwrNnZhkMZmYwuX67v-QcqAalCbJfwftSGt4yo-j0pqYuDIX3Zm_GftHd47ojVV-bUl3ZntnFvwqQbQe9XRFq4E1hTRoBxrpz66gqP4xk6nslt6NFK6nOGorYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WuldWzX_dVtA4gUrgiTPTsM6W8ByWPYfYpErJZnEvqXeJOyZ9IzipfUTcutlEIy1ctAsKnVVH3y_4qDqtvwUOZNPUxujIFohuf0b9HWDXW6qaF36GOBNjdbBtqG3OkU6wBKRh5teCLcpoGrjXg3YZJ7_ueJ5WU_7EBWWNC-M2J4Z6F9Ik-csd-rR9F1WdB6ChsKOwMqOTGq1phpZUN_4pNWTJzWRMDrKrMHKumZO13btcOYr-jAhbCzS1UmJXJ9JmyLSjVZgzoUoYnAJ4LJmKxtBUCX7UPnpNqCITMQ_zjQleKYDETPyKREVRnsuEz1OIj4eAA5ZKny6nJ17M0DIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SC2W95hP9vBt00vmCJ3NJbr9daOf1HjPlaN4B0YUUArXPBgmNHvkXZvSYCOEvEGmdCGt6vxjSCi4doj27tE9pbozYP5pKcA7ZjFwrRlhvmbMBHt-HEhuKMnsla5CTH3Lt0zts4gnXhtSfyrXYnL_ImSi2hAL6iCNCviQ24IjGYTFsWfnx760BX52w2cFdjk5Dc0rMvxhgQgp8j6KzUnoAnic8iUXreWRwOQcxH6bQCXFBRlSiukZRcpnR2pTL1W_ZPODt_d_bwMCDRHs_NdfsKqZB46a5gTYBTEo1ssWNTQWw0C6-Qtvvv74ouPpHNp3_nuzuNTn8iQDcm2tl26-KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJvh3YoEnR38M4oAwq5ye3R5qKFqUg2tHeDqG05weXqr92J2hL8mFZLQZKHa1s4pDSfo2EqrCppiUU1AXUG_JQPFVtztko7Hdbqx7-_6H8kZZb4kK7m10z7GaQ2_ZM2-Kk0457pvxVMHnRzKoviDw-3eATol4V1bfVf7urtMlDcxNsgCRyBxkdWvCafnSxXU4alzRNLlt-OsLsMG4l1PyMwxw_fikQkAxxJy5SHxCTOlx4a3iuWDDcDZEBhnmxnFFu17RTaGsb7w6OBbVUKcZ3_wh3uKxz9juz3kDfrMea2p78tmL89hDIwuK2ujPRIsfzbg9crPEkADBd6PJt9--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wicv-54oANmrz0JUbLDgkfsNDUjC93nExByzIk6Ny4D-mfqf39PHlKizgtMAE_lUqFu4QVsGtP6dl1HiDy9k0Nm1ZjPqD-T6jafMD2dSllHYBFmYCadfLrwx8WSSU4M0WedymAoTMS1SsWHwPY86AzkBKXyu7Vcdy16nE-1xri_5dGX-8PqjPZf5Mjps87Rx3j0YelOO46nvDR4ODLJ32Kfi8VC3F6zKkW4ApdXBtDi_Wd9Hy6NoRl0M2wiZ2pJu2L_NHofMO7jSHFR23pOwyN_R1rPCTOGoZ_1V8aBJo-i89m3OlARt0EKJ63diXKxoBRSlHPF7vpauQomie-6RYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v1WXCde0-v8l-S7u0bujmIOMks6tpqcIR4AGxB6TL9Ts6pl7rCJrGZMxmtCcvpnYaNSSBKFDGKOsr82GSu89Mu8r06wSnHXgO5mw5nU4T4J6ZULnjoPkjoCT0yI3Kn6EBWqA86PNiVWhkd8jku4vO4I5E4rP7FPa0AVDFJ6b3Fds1-vOPwpAPq8pGRBdG7I5Z0y3QzOF-QnY0O4d_dP8aq6E8x4YGjoqkgstggHTXeCutfhQ0C0sRO8wXKUwuvC5E4XegR0RrvNnjz1oKiVcpM4e2WME5sYXDlE_jljCQ85r_COxv0p-0oxU_I-ifm0zaKmzrY9kfayupLoB1O5rhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EVPzilIbGfJ95mSPSihKvK29BkO0ABkpi5qwsF4FEAy0N7LmHyeYchifR_SztBbQHlEmsMTxkeGYdXFWhoMwae5F6NKCnnF7Tnrzwz8WQJNo8rhRwG7dLtnHHiCLAYeKYl47oExg4SELbOQm_Q7QOsct__2ArMg1dFwE_fYLWky7_f7szbMje4llvDP07rMLoQM7oaUa6i86d1SgeToSWoUi_d5c2Ncvr-uDxcLTO2frVORxWl7jVPIuVfuvXIhNzxqG51rijDtZIJ6YLzfLsl3nmBOCO5X1aRQKj1fiCtsVaLwtVflWIDCkiUz14GaoNLLe_7k4712TUIvpgggmVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BIeQ3-y_hwkhHJ1xMZs03kiTGZ5XxOGrE_vMgGgFjFVY4N3RaA_6dw3zMIgFaekJVZh2c1Ei8QRTx9i7U16OZHk-ay7s9uGftsdBcO4hycKMJJl2indwOTcUI0NmpnjJ3p_HVxfrkOrvh09cFUKGFC2daw52DD5UUgAv7h9VNxweOBgLe-XqsfTMb_yLlBnYCaN9ZTICygYBm8BVL9_knBx_Uz_jziMJeq6OMspoqSwXDOIUrgKbGtezEnHBGfNm8IevikwE_U8RvVuvjK45hC884N6Fded2-AX6F7vGVN-qwigAmyCGpMcqdxWqudwTm52YMfaj6-0ORLZyd-TjNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/snE85oaRbmXCr2J4dx_ZBwFGO-TLLWc1ea9BPqSCa9-C93-yrrGO1URMZDZ3LfBzcp55uO6wEQ56o5M3rFUj3s2G6PCsN0vzCYaAvh51xjC3MD8EnpO6qkrqUFo1MYVFTD8cO44iFnTz6jrU3yY8GA0mpP7bv644iPBP7JJhLkfhW0uusAOfgvoL5Gz8AFmoHudY2C7m6jlMwwnZBBHAkML-WbzUKu53TTA3W2XL-y7qLrT4bUQ4DDbmk6drAAj-pE0shZV3n9VDzh1Ed3NtkiDvTaC3pJL9QgORxmyRlemDh3h3pitnmRSn6wFhXgyGd4uNMVnnUCCroWT0p9VnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y9H5Y1oJpOW5EwiZB0UMvnW22aYKfcE5jgkNNgIov9P1kh2hZ_CtFSP2lxfuUvVpLQ03x7eCk26ELealg_Z4lbaTP3lxn4tOthJoBqkj5t4NSF0bUn206mko8wz2VYzSv29O5yDl3E_a7UOR-qxNKfQLqZXp6FeXNH460-HCv0gT7NHBPa4hTBuDRC4-VdGbaLMqnj8Av7zO3Re5GOVP_3NTwnCgi7Df95Luda-ToR48QoO86ELLNLO6PrxN911VqS0Sr-AGQgIWMbBHnld6OUfeUDrSZ6xJ9hWd_1UmDCZAymMW9hw67aLUqu_jdN5whU1Z9AhRrwHgaTJaGVLjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JQ1gwwISc_fmELOS_O0b7Ly2b3zknvHCy26aH0EjLKkPUlyG2YNrh3yQI4k7elrsnqoNfr3aKud7gwsDqTOl8p02-NMZpaSjR253DnKEoqzXmO7AO_kyJ2CtIx6DDA6u6AsOLUZX0hbmYmPPfPdJzKscptFCRl7SKCsOh3QFh9oF-V4Zl_TkLzQK6VVWaeIFVXOPUOMtbMEEaV6gZxkiySkEjpjwv5lFs3zt2cPLVXNl7bcuvoZU8ySaGPRfCMQ8gwzF2xjWDD_88ZOFGZ0ed5oMPFlY_4_jjxOl8EFWLkBF2_QGqfd9uRYXGLLJ4MnTteOwC0meqgKjzZyg0DQzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OfgyEazKAzT07ov0gdUQ61Zhmh3zt8L_3Ovau5GgqLO_46SfmlXf09RZw5F3ewbWSBuzcp430WV5lQnzNgrzxWpHyslaov8Ew6quArVWyFEFmkv9tLDNoK406XFx12yuS7iiTUeAEhMogHYhJFOCQkPAR7e67sEmCxYrMUX4i6G1D_3d9txZwqzfGdtA2dfLAcDExz0azW6SDtV9fRXparJvI0tdMHzv_C85VcGsPVJwkVwjCq6XM9hHKWyg0-2V7_ikl7prXwZInqFm-oEtcFmoOqaTKJAL6odsu8D6XA-4hiRDv0fhYgwW8pmweStTsbXQWJTXM99t53JZVirFJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TsRpbudMVsjcQqve-2nNcb4WkPqnwjYC7hyq2yOrI-eXSAgDYC2mhph1oTBnmXYbbUp6huPadtu7ilN1ic06mpV9MENaCzwyRwtv3QWJpwx5Q2v5JsciYvURyVseoPv0AQheaQsPxoDD5sT1jxQydtnDfJrIiutNi5XmW4H9Byq8K4F25Kg8NUpHe-BdhCNnPJfL9hme9IJk6im6v13oHPxBVLnIQ2LOdNerenxak8URmhL7ccj8CxXqs8fvj94IDH8IcyVWxecSsYwtzZ1FY2wb-tkiP5v3mcWkJ5QibaGbu58I-rM4p0HvV2XLpby0czQDt246udIRKCH0tUisWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ed1Z1xlYroZy6tAbqzuYYJ0PHESj7zPkVuWmGLAz1Fo-eVpt7cWt95CfQLTdQAMD_zT4DmZ4jCKI1qc1-x4aplQVGtoYly8GMfYKTZ4vESPLOhL4DjO11peSDE3_yCG1WmlTod9BDZfdtzEYBF6e7hGWxcwZR6B1i9TpOODlkEeN43_K4fSEVdUTZsWKFYgf8KoUY6tK3yDJNP16hTPnTt9DPJR1JZXAbq6kG1_oTbQuvo1CNSN8pY6_r23AoOTMcFqQ2rFY5L-UiChWlDp1nm8w7XCUeWjbKZGefcrlu_jtQXdz-AW392jesqliPXyswXEiZj32SpT74T9BxUltGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D3YxrZDuAhdXGCA_NO65JNk6IwZEty6ZbnQeCRkleimiygx7ACbYpCT7dHRRzeyhT4aPAczNjdiMKH2tr75DarXp77KxRAuVOgrvOt2zwF78eqKEIVibz8lW8U1qvSzPNiqMRIaxIgGsgPxOv_19JAqY6Vi_oI3YIATARdjaVAWKuDWcq-3Ve1H0X7rZh-CqetOYGOjw5ukdCbHN6nrn4h8wZZGXpqTSyK-bklzsuCOeBnqOewhoM7fRm4uVfqlbJNCNOIU2ej5_twxPo0xKuLF1_uLsf9wJN4_BI2srIBUbtJEAXzbtNaOyabYqBPWT6ymhX4Fa19XlhUyuY9IDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=eYR6hpiJCcEYvqatY5V1BkzAf9XVKti7EEHoNr9KZXVZ_0_5gSrphBM_UpRuImX7ZbB8L9mMxYIUy39lvHU0RBdM1lDbOHelQkKbo-lFsvcc8s9nCczJlQMK4LwmFfzqzWwIqMy-CV6ToIuzTh4hMrbo6zBjMiW0ozSUCf75NwRs88CDvgiukV9KvHCk-vSt95v32ZuEYCdqblF6JNJXneAlS2FpuWX7SpCXydJOSrnNM85FvUb55Qv0ZrfIW-6269gRvcq1Ia-PjoYFaa0cLqb4ifu6wYyjYoorRfLcVTsvEEovyfXMr7RxYzktBa9CA8POqVxaMq5Xb5c-_fOTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=eYR6hpiJCcEYvqatY5V1BkzAf9XVKti7EEHoNr9KZXVZ_0_5gSrphBM_UpRuImX7ZbB8L9mMxYIUy39lvHU0RBdM1lDbOHelQkKbo-lFsvcc8s9nCczJlQMK4LwmFfzqzWwIqMy-CV6ToIuzTh4hMrbo6zBjMiW0ozSUCf75NwRs88CDvgiukV9KvHCk-vSt95v32ZuEYCdqblF6JNJXneAlS2FpuWX7SpCXydJOSrnNM85FvUb55Qv0ZrfIW-6269gRvcq1Ia-PjoYFaa0cLqb4ifu6wYyjYoorRfLcVTsvEEovyfXMr7RxYzktBa9CA8POqVxaMq5Xb5c-_fOTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TKQSqrE-Utuw8wp2KATUjMaXSovn-v23VdlU6PWYjMgSbgtueuFxPY2LOjaRZTevfz4lI1AB5Z_VUVpdIok2VjdWMVkqe5n4X3Zi6eeo2cRZ4J1hQqlOClTIOF-lOjd7TN1QvVK9u2DaEEyDQ7KuVQTKvBw4mAahCtzQmx3Etds2JtYTjRWfQFK5zDbySLn3v_BQE5cUEoLUoA2r9RMdW5p510MWn7nace21gCoQseujwpgkO1h41Xh-rUl6dbfSHZzTSxhNqzQeMM9IpOX43lV7YcTQPEmhEzmdi_lvJmrnOT3LZBDM4Mpfe6KwHFZOd_gzPEVcv1wfzJLHka-hHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jfRLgM4DRPy04zST6J6nVRsGRy0aRRIHONhMfaGhKSj0boHS2f1zziT5Aj9WfX5_50YCe3yBTga43uEwzu-7dV3papeFi0yXx101Lwl06oDsutT0ZDR4egULr4k88mwdBokPOQVK_hfWUtC7drg8-I4kwAu2DcMrrm4Syukkz-flt_XuufnnBschft-0QR1W2JjfsjZErHgWSz3_WImg6DE-C_eaoxzaeOj4bHu3i_BzylL-r6Xd7QKrnt1KSdgB3bJM9ONefugx-X5v_MTNxBE__P1-46Nz8bhyjjr0moJRHyrBfgiqIlqmF0VbRYwvs6C9uMBlgsKDDGYMdoe_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VinYBAM3KV9UxvRu3o6srfK99yowHl-bG-gkJe4bF7QWY22dDBup29x5QpEl30NDukhubBWgG0IEWs9nbOoPb56pIrMW844EkLKWw_ZDjSuzo2v77axiI-NpJnndgrcIqD7CYOWN3C_zjiZJ8E1bByyGsJQfCRKynw2M8W_LrM7szEuBqfZzHYZ411K1I0gt0ZcFkb0rqHh3EvZAvaA1ilRHz1ZKw9nQNH-KfCxXMpYFnj7MqdJ1gAIZBXJN8V71vuR8V9izci1KXLAlyVdg8GdUO9_8Yo70tugcZ5N27BnLUkJO0jq6Ya9PhuAabC49AxcFuY_2IZTNo2Ku_LJOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MkTfImDNdPRpGBJcptWcBtEppZw4eNDgbrEGr8zGIkMH641cy3EPFJG6PthpeMc_WGRiqJorunFsdR5BgtB7OxNGZHXkeYiD2xPKXf6-E2Yb2S0B0erTWZB07i9Is2QNuqVHjyN7tQZCcr7V2HWaTFI_kGqt-PMDtGzJiEiTrboKefAF3R8S1oUY3bpO8U3fbU8RZk9H_M1LJhScaI3oba4Z97TVXIhGGYMTLKTq3R4U8tMkTYOE4Ig7ADYHNqCfT9yNqy-cypTv5slOYPKy7udLPVvvxK0AU-zH2Es07-R186XX2vKg3TiJtSpy57UfDCuAAa5OxLpIpR0pvcEFLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1ao1-GgDS7PwJyJEHJSq_hqABqkurQb_NyosR7GP4dnbU28wB2vd0qFTz_FS-hwl5e90NMY-g5QrJ8g4YBvgfmty8rgHFqqUFmJhAJapomZ-k1VOsuchkDFHfrr322h18GDLIF9YT82dFKHdCA6hpI7wYxNJ2w59UG59VSzaf_Z9jJ3JnB0BDKjao23ow9BfvRDWN_xuArv0Rc6ae3jkXqmy8UVK0z8LLmSoilLKqQ5jRb_7mYfYgD3RDIx-a-S6tM8T30qyZux2AJ70YEE3ShcD6tUp7ht4YdINrmnvji5CDjFpJz1k4jT0jHxnzTU14u9DaSLLTLe_M7vyQJiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNke6sqTTe9V-TrEWeLR2MCA31oapNRXXov3tGai_NxHk_2r08fibNFSJvDpJHpcJkvHAePM-YhIgV5x6qonL8wgHoHZUtxLRQJ7BsobQFknj8IudvKqp24bv8hHDpSLVHeDgm3W7O3a5C2ULHFxcr2mRiOaYptYyvTG9sDtjCmn-ES3EzpBrCLZo-l7C_LxBsGG9L5v_QZphWXDXwYfS-GGjO-d8kQXZmodjAk4gi4VWdrs8-O-qtu4CcrQXQJrpy39wfAaQDmAMIA8KQ3C90EIN002Qt65rVn4asRXjfdMfkm5h4R7xboC99Rrxz6VNvK8HshOYLY45lNKcJGdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tlVsJgEbadOw8_cdJk4MXRA2JdF8ak2T0wIfJAauCbgW-DazqHYi5Jh93Fp7ZHGyu95fHmVPq9CQFOdvkYfLIwfA4psHk0bol0CjkEvp3DhSlXp29zv9DUJ7Pp45QpVRhbRJwHhUDgsuO4BQqhU7h_MrU-cSyTGwkYs2ucCq96RNW03JZXx7bn85MPLHYkM1eodmCLh88IFEl_e43O2gFpiFdeqQ4QtyBddtFsh7xwZ0-O4yKs0jV0XCQsu9CkuXH8e7-kl_Sx04Br5gwpOwvqSObguJgEC7I6WiJYrb0V0-4_7sQrHY2OHHVwyXBPQLYakNgSMswa6022vio4KDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ign9z6B6r4yUN_0jI8wccsBuzWASFIA6yT11trXSLjvmRrHyLTKmgiam9ghZKksg9a17SK0T5tDs8PRuBgKOzERvg8_r0FWhTNDPdExtDw77L-bcvi95wgd_DT-ApVkPAcA6JFNiu93hUa_BmRjUR8uYtsnQFle2elUqlh_7C4HUrcl8727EjNK8SmJvySu8Txtrv8Dru5Va1_x8rwbdb-EOzC6CvsODTWDwy9Ss_k4EoJn9wrkTGmvFEJWRST7aqpJ_YtQemUMMq5g-DJgEMztUXMcQbyyy1mFAi5JCRQQCkxztHHXAthGRvUckj2h9KRmK3oKhFudPrrk2zIx8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XFy251ivyNFQ1nYBcizlUveklPH0UEdaefPv2bzN0WB-WZ2hOEpFxo6dmky_Re1wR2tjJF0hLK7fc_USORO1QJbqNSUsaVJggRmAnMpV10JG4jK9Vbc9DsQCcgmXSOUARjKK9-8xItFDJJapbLsK3HaW9L3gq5CmBivW-1t76hrmd499z63m8O9T08UVev2BF1lHgY-dPRfRFGY_u4SbAemNROTrduUzXG-ruedbzJe78E2OPbmHFCmfUOUTWtXs4WO4SJq-YHzy1vg8IBRV9TJwX6SabEQ8joRSd-_ZemH45zFPGcK2fF5Stpp0lejdBmHF3IEyeJtwDtFqPNH9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXRoSeqtahcEw0lntm82U_FFXT0uwJMPilCrcWNTXfqkSgW1wTl3jNP5_P2sjo6qk-lY6Jx9119q58h4OeghxKl7mRjpDfhQyioyL1bFvNFYyquocpk2Y9x3maqCuAR9rsNqztIPJ1VQBUORU_ptYlU1CGrCSlOxcgAqAwRfauthAyaLtCguVQS6tGttxUQZsln_q3xQ1PXEw2LjwTaisfv_-ejWtmA_ujZH2YoVapXPQNo9GPo7jlNj89A-jrqzm7swdVzilGrl7LIWVcSZzHJa3yk1ckg1_eCE4Ni70KK4DwaQSqX9WAijG6uNRmINinKayOS2KZ0qs1r9rwHh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6wqHSA8Ai9KifaZhgri6uYY7PowucB0F3V1bh0Q2fKOQztUGA0sjhiVRxpEu425CO22ct59jzqMq-R0GWSnZCwh6bhunok8lSSMdBAspo5OP-VCr9znm-bT4e52jLH8MJJVUSAd9VnqbDsjkFgQEbswULYMmzTE9ZN0lg_Hur99LhGNpeMXx4BIoWXA_OA_BHV4F7WlKtRxPatARe0R0itvN11gwTsGsWrjtKadQiUITqh1d-IEH_AfhQM0SULlWPAxENrGLx7eCp4eGMlMffR3DiLOkA5u094inrWkPRfbkf9FkaFOPFaWBbG3v-q7rcO5IDv2lpdLyR59gnwWSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rCP45Uh82r8ffYRXucw89O0cSomuA9qP7YYd3C6xFLpwwc28C9OIDmAni5SCv1mV8aA47L4z_ML-BBbmOnPIaCd9YOnOTP0SVSYhUet1uMp2tNKl2_NKf8ijuk_tQpzdS7FyLtiAPMhwxZWfq5jJyj3gaa7hUwYnJ1Lyhspjbtf9Jq7hELaHpSxMLs1Hjggal1dCrvptF6aWC5oqh2fbiNSg0Z5E7WtfieltQXlsNiyG7dD3SurnBX2dOwcje6LzoCrm9PiR2yr0nnprxseuhBQWgXADxEck3vm0KBez59_ViFMPaFupJXq-4w98uKoOft_J-3UYWJ77SuDxhiSbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ej1ISC766JGN6F7JEyUbaiH5joNUd1yXhLt770yT2dJCIgPYb32Spc1Gs9Mh7GReC7958EB-fxwzs15BZY-ovygUVAmjwXlO6Pvhqrx4ij2Zk5qhhEq2tEKw1FJPEDZ9t4NgrWhtIX7YD2kV_ZkbIyJbCMuOQ9nGTVxgQFFl1bsg7rmNbNAfXGsq08E4HCswKhk84iQHFQWNcWIDp5suHvAvGlXEEfLpvzrhYKUULr5lyZ6XP_g_T4fpoIQns86TVyOmDM3QFmvN4lxiGArDaI5H25vZcl3aogWnwvRdiegkbBqlt2pe95EfnqMnLvm7-kNR5GxdkE6ZBM0Xedg8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dNJJdIx5X4EYaYE4yAIQrCPiIqk8IhUmEMNvel2BH8T4MkR9KK5-1BNO1y1T-HUQveRathKtWzXv5F0JlrE8Nw8JuowLn-aLGly22fo01WtHxDkZXPA-4P0BpttttA1Nl6WvHJPc5xRIfueYpIwRRQXYpdV54SLhhTp8LbRKFqRt7z7WU51ugADx0NRH5O4fzE9mSgbD_OjBKU6wNxa-AoX_cCAFg7Q1cRznvHTXrWGJWZcnAP233UPHICbe244iMpXdvZKYVJjoScN50Fj_LzI_U1KBZvA4UVzy3jUI2_75AU5liVX06nehNX0QBEWpEfX61wOQvVEXVyZKiDLzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJN2XsS-NBFOtcTf5LZWVL3PC_wH3RK8HtNHBeNvDSxvuYj6w7mZWzSJbgqmKjpOSnhWDLg0pvw9lZQPXeeUTuk-5G3APTU-Y5Goso7_DOdOYYYkz0HqTWVbKFJwxbqEKLTVbLUnhysKnHqOAkiJw5yeksFhNpaY7DksMrOLfCiXAxILP7cHcUGdQzgVHl7GMukcvmWEsfFgcvBAGwvhUY1kML5jULIbBY7UeuAIu7nMNRWUI32xfkx9uR1xkmmgK8Azrovr3vrCm9fedOvIyFRjAAMS2WcJT_tDmBBeQ0xRyK8wuxUDm4hH4OycGkL-vCzG6kaD-dYntutffp9eQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ReKyTuXGNW46bj8vGP_7v9TY9G8K9oi2a89qHLyx2hJsj9at8vyQGSV6w_ta81KyJeGJ-Xff3BqebZ69pNVX1z07iWwolHdbeITHRHkbbTT901t8KGGoyRv0lkH8_n0Iw41fRjn3kjQvllfyd3S9YxKVpzn1jWxzwCzS27RIyCjR24a4wzpcvybxxf0WxWw2PL79lR3RXkgAp1QEZDVjLwyW4o71qVLxOFaV9Q0paKtWQTpiV8TJ_wXrB0gHMzzjwbJ4ExjhBHU49JpajJIGcbLRrNu3JpcJR1wTIIwIQth3QJl5FSGZK7rU1HPy9GmG2CHPkBbTBFBVvlt53fd8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LU467rnQjt4z-T3b1Oe6ruzbHo_xVKQJwFvEMyVjj89y0Emu-fJ35bURMO02_C7a0XU57iGCfk83CWe4eVtuU8kjBWM_7PVw635lcTfixxvMhxhDAZzjKhrGjDf8mqAOgBKb75nANSr4OXfwtfzVT4fdx3XbAC8mLme3pi9GhTw6d7hF0K9_RNeMrYNwv-teK_L8BBhP8FtGZREdzgNuI4ImgHXv-LB6kLuLdbCqA-mjoeTvzTNl9E44qCp9wNHzQMAa3RGhCEBpZgxnXBBFu1NJ6lcSjHZMDxR8Sbz2bX1RKQiDIX_efvkx3ym76RSiAyWOzjNLcQfkigGeRc2Wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jAG0v7mv74EgQ2CJJsGIuTJEiyQS9qnp9gjkUbP7tWR2dCLndM7cpGs6PoMDMzLbP_EKQ-trIbQNS43qiwdDLxQ4gRJgzB8vwQsog3vSe5sVP1O-yKPYoFlo5dk-YlDuCN9gDn5XQatuGPOmEVZ9X0k95eVllqydjucj5CtiDHwqfwmHqc-mLsp05b_F6Yx1oUIzC2ZytXpFd-LVRIhHKNA59GRdmPJdpmU5fO_VtSEuRu_yYWYCvJdKZj64XDWBAQiy_ugldVbDqIPNPv9MKhGAHv4fMn0HBEQ3pQQ9ZYgwW4aUeeHTss1aGUt2miJIC4XozLYfinZprmv_3IGQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MX4moXXEJ3_Y85phcgo5dmUFFQ1YokXi__oUVSwLeBR7J_m7vcHw6cKgNksofif0j9gONIHgkbd0PjX_Nor1u37ilSSms5X_RdgLmxelzgO-b0k-_qEwT6ucAMZbHTtGeWJ97sf2dMjZLK8n_KNTPqYIW6ksRCHVYT0HDoWRfE8i30T7The496ILY1cnAle5-0YjdRz_iyiXzuhaGprtO9IWapnKc1lyAi4w2YAVOHJIQSoFMFS7Dvq1T6Ib0wEsLAA0cyC9XVfdG23qQx4h863wemetzjJMXcuX4dlOXk7QIWueA2RtKsN51v-LsL8kzzksY3g-tODT7QBC07CE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvThDUFDgCw7VtkQ9dqGfun3ljEFfOJ2l5nx8BJRIpQD-6k6vG2AyVmIBGaCf1toV8t1w_1yry9XC1EbTXLRWxgMlLeptp4F3vyUxRGxSVACFiRDnkLvahZwh_Tlot0IaIoyEFtFxK7n5QgpMKfrY2m-oAqk-JEnxHYRr-IeRZ6dMFxqMYkGKGpcC0cwnCjeZMsLW34qfAeRwqsDOobrqiIPGXKp6j4Qs0lfi890WfubucgGGuv_SG879_dyLIOX76EI0lYAZ6jXo6fQATcAxQwFtBHYXY66d6IIhhSL9GuRmABE0osy6OHESpe_iz59tl-5K9Aipr-zAvGEloguSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q9zUbfTS-yQdcphFDGluUYpww_7EVixSTWju22LQuVrabFUXkTZn47rY1eVUyqOT-Zzo3jxGlfU_uSjtqBG0l2_7O7MIQ_4sMEl_wxjDP-4WeeXXQJ5iBtD-XQp2EBNjeNfd-SSzHqnrKLH26omCEKYA6tfKI0OjpJKfHY5Li4laSYF_HCMvoOAYWLk-kYRVTIDuqeGCfs5dIgSNDI2NrBzLhixjgrqnVSGFg42vnv_Ss7AS1SNHH3Cwyv6ZB2ky_lmdsAyR8tFO1izDv2sICx852RDWaHFkOifuoqYmzs2EuUDxqrwt7dUdnFE_Wuyu_dkSAhMHiF4syzhPrFOFrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uqDsOj31sx0pnfWvCiCNFtiIfKU8mEraIZ0pg9opPkLWZHPMACC--zY5HPO-uAVg0njjzzm3L9Tj9vf2ZeAFGls7zXC6DljNHc8yGuaJt4jx24DbDnF3jgXbklbfvUMYxlqN5IPfhMEoRYKjZh4ZG1dlIlpQ5wEYzCVxCPpnoRJQFGc53niVEsxTOu7B-RQw1dluT-ehjWziDvZnhgV4cDliUBVcWHQXB35ognbmxlTwaVbFnzdXJvWqoa6dU2utsDSDCX9W9UymteXvRDOJzC2uzZ1uTOTrhE3imevApbO3BOOTFpvM3SXUs7dLTxdAzr987jxy6aoadtOLKKiwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ksqc-sBtfpsGBHR3KdRpHya9OAul71sl-pdV89V03iFDWiaXkx8phWiKDEZ32IE09mPhVGv3xwaRNzVooieSVL5a2jPRpc3Zb05Awe_bUfC_POUKvkwfg_kQ_CWjWdUz9GwSPCx_5uMF8ErLcSLJDoQzbiHrpw9hYDQhWMQH9OH5FXXVUWWUFOyTs9aOOmEEvmDbJZ5bQH-yrc5cOLgig3SXLnW9Is2M6wcG-bwTbfSEtg1GzBJcXJcADmPUdkktbrkyGOPDfbwpUtGguTDQpWlLSA0RYUgWsoZmcfa4PrBE7WSl_97sMJ7HSU4HpcAx773NQ9oeKZAdkqpM8L44Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ss9rBn1-2MLKvomBIDg9Bo4u3EFaUW0oAuxgYQJugZvMEf-Xw64ZH-obEDhGbeMpXxiilDNjC9bNcW0OjR_ksTbLTV6z_850xHS8l-r-1UyUSQn7M_i7FdsmX_aXFVQVGRgFOxPM09eKI5bPtPymv_E99W24td7huKI1kLXDhWhn4X2bHYqi6O3vNJD8E_KI_OMBLpdRsp44Ii2wFxDzubIDU5HXbub4R1oM-53br0fTMI0hdslZ9mygg6DJ69jRKSmXrX77jGy980OzK61jC3TbZUUoBa0vM8vC9NCDSkHLcBA1faEMQTheB_JpXF0UWJyOraGPrv39bCO6M-9Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPucz4MowvGgH4YvYobEZM0vd9ZRUVPfpbhr6BypMmVeW4_gme2lxTPtPDICW_ES4MNBDLb3oGXx0n26cUUiho-uE9299AcerXt_pes8JJ_Uh131KP783zWQq0ElodQ8B7AwAogAMl6NjO8NG328SQ2JL7gQL143B2SHs4s_4WUSi3D52YhVrsjSphDeX045VwBnvohP4JWieQ9aZ4y1SJNTP-cAuA4evxTmBWhiHNlYh5eI4zl8csJH5I7HSLa8yT4A6qnr512MuQ_BzCLdWENKCRMge354xEO7ZQCP5-axkKS07HhnB-T81lJM1w-nFpM-M4JBrwBGbJQ6mDlecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rCNSlrj97Qrwf8foIPCJfysLKYcfvJNVLhIc8gPuEZe8_F66fiKhNSaQK07BB00nGjmAUv2vOdfNccvPxrUiTuPlT8noycPzijC4fv-c6wWma6vUTIf2d21RhRRTLzO4icXH3D_XW3NPljt7-Opa_P4kEPSckKbapNaquv3xFcXRh2Ww_YWj1lfiUANgLojbw39jl2PseOYGSCWmUY7cGTQm8s5xM6-YaYXoEPduJW6fR3TRFmHoShfFPSzicU2O4qBNguF1LLxoraT1QfuwopSjYT6jLcPUUWGPdgKdBBGBdgadFOqsZixbe1cw8Vv5uo2QTf5VXzYcNhgQSMmn2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sCHqlel_VKnaCKtvRTvofFt538qaOHCkeHubzHKvDJD49fMRMmQr14dHlAg0T8-hSVfIw-odjhoYHU_gTtHUgmds75yS1dou1WytDfnicEz0_RNNz8NjTqjgjlAG3GBob4d1JMs_3zdyDqJG7Ljv9CCeYBTPoX6LoArzzv3ciy5Qb6_s2mOSjSoyee2RRUIxYmX1RugEmvvhJVHgv5miBI29SWaTRS40Q0O1-y1WmAOXx05uaY6W0N1LBElVt2tXjUWMjx2WwG-5b5Dc7vOsPeP9NSSrsqfVLNMJe8WLfAiJwxdM4CagWv-TX0C7ma81RjMzTKmJOBRao8c24fNqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPXpJs69v-bJmu9eZi05XhSs0r1MHcMyU6H5iFnQjGtAbeaVzyVwUphxnRN-mGEu84Lt1xZYb9-bOgnRZIcN3FurdyHWseaUvQ_ylvJwIJR5Ix10Ka2aCO05-UQ0cta_lPq7EESL2UUegL67s4GQTSQTwyRti6I6v-BtlP4XQMF48efHBxaJxijlPMS1XwU1Hws1QM_EIhEGVgUYhKRM4VwDNpY-_Z-kfw9uOMWZkXpe-gpKGiGxLLdncAxgEQ5J4gcCB5zHWj162yiCxPeLrywPs6rwPw21egCgAasG0MS-BjIHwmZury7Zi3gzXZycxJNml0W76AKLccXQpYxrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SizYGzifaORag5pP9eP30SoE2sYdEWiYj9e5ticPcDcZuho5h5xS0frxIs8sE2MUhd9NzqgnkmPDWba7c-OZ3KZ9cIA9YMFGaQ75dZ08OAgv-XThiYHx-9O_woI7AEPYCLK0-x7_RBS4vdj_eDaTkt-F-X62807IPaO6gP6MJB2zP_7-nU_PHANIJm4rZS7DKVx7oGHh3rv5wXnLlBCITcYUqm9V5JRNPhJRZRifjnaBiK3pvJSKk7bNl4FjthbJzEA-FXlPPC5CtkQZBrGX0F4Xc218Hxcr2jaAtNc50beP4NJK1jL5i_aYn2Sreeq8mAZuzYgSD_XM8h5zPshVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fcGmeC86uiluukVV-QNmiAXMvt6vHcxMPnn7XIspg_xDs-eNlFJBWl_Ws5mf9xG6AuLydNXuhKVpCMTgv3u--53NaSeR5QZiPoXO4cnKJDQYpw1siCD8jTb0y9Z4sbyOSZHiD-PHIOAwltiNiWmdewj6IMdXea7Y3h5gT0CDPsrmfO91hxHP4QDuMoAREv-bO18hct04CxrJ3n_7fFiZXxd7autd7s29KLZGdaNQe0ZedX-jFZWuS-6oOc4WnXczK5m1HUZeb46GQJzz_4yunSq-RzMfZJEJGxIO-iSGNYJcDcLIOe8NHUSmfLUTStO6uE1xwD3-Z-ilPM3wtJj_5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/deqDI-yMiE1tT1JdoBgQQBOtfAstilGawVXwYHEEJPD79CtM6l8w62Y-2X5NHy61iWCJFSXUrXASIJ33QP9HF6yP_Kun3GuYl7C3l0hy5fFTJ91JaYqtKR_zVaRJbBvMsa7oJ3vmdJ4r-ceSnZbKIx30jGHqJvUmTcn3zK-WI7itoK01EWRjIVNDkQ-TKqv0pl3HiQKYQwAtlzJWsGrernp9Fi63YKQPBhftVvvnRI57dLZBlFNghr2erVcmReCd-qL6hN9994eF_6EQ9xcVNzKJK3_bduNm2s_NgQDPjAG99lh5gapkeVA3mUjc6Hbd6AaHu81ICb5PlUSUrealsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2fih7hFYlp-sSZ5vjhwxnRjKA7rQQLWj1zNV1vJHMkwpgFFSi_HMnTO3Y8wRfHoh2K1R4YQs5V4X9QWuCq7UF_ZRK4YmCmi8uhngzNKaMkhAQuRdP1-gBceggEw9AunixLy9Pi-0WU0Gi0grddEf4nf3gzJnQrX0Fu49Ei__IOPhfRLUMEEnwmZJ9C0YgYL8oD2POQ2eglTv3V-JeYqL26tFH5yhwbAe1U1N_Eg7TUZ7jyKMIXkBBSLDREWbWKNplr5Gxp4CskjMmL9zcXMpf_zFfk4dLWF3oKNdzNW6WyibQ7dcr8IvZgYeZtIISZjsQoJCPCjEJEiIqnnqqdl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ooxsFjlU4-Bbd2oQ2hd1FlkSDiU_zlooLtHYI9w5W8SbjdD0R_BvwWEVbpKA5XGcO32G1-GM6IP4Wupxk7QfTUZevlFaJj-1NqAUN5JyFhTB4n7gzDCXlZ5Nyxyc1zkD9c7ho4A2bUg74SKnw02HcQRCNunOcsS-81ELM7kVx-6zMZyBeW2x8GXxO-sWro0YHt21Mb4g_NyKi_SOM_3wMQS2EkT6eIxN9rLQk-GJ-qqygelSlPkh2wb3B2BjipkEpwGH-_vIu5krEUD5xBwOkdArXLkhVfUZPv9lUxrWVzk2rn-VT0XXmCgDwclYJ58Es6lEnhrDbM6yUFFV0L6dQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/thsuVad6aDaOqGNihBC1T9usA7oee0yDV-R3vGE13tdpObpWL-Ya6RfwuSUFIKL_Mq9fNEaq5CUmPtS42Fm0MLxYRXYkD7bs1RJMM1sYDAUSYAmPkR3v1xnJWzP14Oc3xG3-8qoaQPY6lEpw0_Zuc61ddgw09Z-kBQBTxknvN8c4V07fZmQGrncjdU6iH3MpnEGJ6pGWxZrb3x0tx56THMPTJM2E89TCA8AiPlLsqLrmujgPpSRZIwwzp0suXaxXKxLH3MweduBWpy3CK7LRp1wJUeNlFZIxdLgKQf57iGQnMGIVLt7oYTaE-0xLsnkhnIq9KrSb0mVG3GP__roFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAH850KWGMZi7Goe8TxNb-gKKc9AQb1-OUW6gJ0vD9m3kV-TFKUmDXbTkyCAUMBRpUtvsybAKmWkewFK8bSEfWoIvvr91LuPI1rsypljjTCvYZ-ghgHCFrsdY9dth3dNaJ1PAQ0RdkbgnkCDkF88BXgGvWOEC1-ANAsC_cH-uNPKaTkl87Ai_zIGKXKrmi_603gpsINO9it0XVScObL_kw-rWVVcrxRXA5IuLIjPRzH8wvmnqqIaB4AdrgprTlGJfvxx2543jGwCBOee00Ks3QYgN8awdlWamSvdP5HQhMlK4DtCtkEoffkM1W07rkGTs-9N5yD5ADQln5v-9W8-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hP3ZOxJMMKn-9VrFWbrK2gkw-Mq6QIY72Nx5tDBa-EDm4fWYW7flK_JAB6U9SHNlzBi5UY1Gz3tCC-D69iXFuL_WMAfYD8T57pa9J-2PpzCppuwgzf58XokNud_Amwq8NVqIriYBeUTuLGvap8-SOo97tVavQP0nuB6gGIPAGjeEA3uJU3TVuGWk91oIbqMhDFjG3qC0Yk8SDOPQ7iTorrOnebsv2A14w0UHdWu_tSuKB1qJtsAQ1j-w8-UpSOFZSrjxjZY-i40_prKlxMEvc8u7SWmqmP3f9I1hZzMO2XJDmlkEt_rPxZFEV9rkwq28QM1nNhiUzjsYXrevwazHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QSkeife2JSksxK9eIGt9pvMIfqh1kXrQvKf9jOePB_CruM4fg0vPPXdgPPjTUejE2qtpkECNmWEM68gBZ-9pJxwUh_3LkqqUBpZuGjEc9Ci-MjBc-yhCyqMJnKVuo0qXDA8u3OqMbxfOwCiL3VL3CeOnt_BonE-YUbUb0nF-ZkaJawIWlKkORI1NYlTBMgvwFzY8MLrYBDjEaF_OvTGnhRq4i6kei4277CiWhB6Al2EpyIYiqDPWuEwnrC-j947GcMmTxy90pFZfYYGQDUg6we0Q6GotcRMN2pTbX5NJPZ-rcICTJTeB6S6wPUBRFQ7qs2R-5g1hA-mhNHlXwGcF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIJ9J-UPktoiqPiQBSdabQSuD0i02BUXkecthN55Fwu1V4rdoiSM4Fz75EDtnsaENvJP2Z4yXiTWZz7HT8PQX_FMQp3P4V3Ho2PqpDYc8ebGgfT4hQ-5p9EkecXTv3Xm9Fria6Saw6Le0DpszFNNZq-6h3Fxo1Gi_dsh7KTbuM7BFM1EA93JeLZW4f2G-Tvb53-96S7Dhu40A06ToY1UgKoEw3mxfE4s3Z_lp24su5fGGaN4AjlPaHVDzJreiwCD8EldjC6SHWUC1RzMFO-_Uycc0KLOseI90LKA97XJnqTgimIuQZw8gzoWbDcjOY5ph7-jG6iSP9pqHFfqgSCYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UfhfBn7q-KiDiKpGOVsNNwggHM9Ofs8UVipH3HwZ8SgZZamzBa7aozHNa4cYtC_3YlTQO_v2r1ROjDJtBwF4AcHQR4e3PspNcbLcCmakP7dJAz1dQv5EDj_hP-BLf7XWKxsiupWVBLrBd26wIkDmKBJ471iu7Uu10f5cIuRUvE3e9V4kxrepZ-tlq-pbkzeg92sZQEs8rRhaDpXU-vFec42fE8i-9GnhbgNDXg_g8tsP4Os_TM5dFPdCKVhaijRRakBNrQgaztGxaaT_Sct2ZNRmImfpK1YVf2ZXUrCUDyVGReudeYllblaq3y-ZK2hS4Z4zBmHixcUSYIpFauelTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cn_mj273KPXJQIKe6gRLcvjGblOSUAi-WUtelQvOMb5hUrewsfFgb7Go7VAfyNijDPpluikqGyKMLWmOGiUEo6i_Ivb928qihCowAmS5LNjBA6EYYgTvzpmjqNg7ZmaI2sA8KjP7wj4ixgugsMrNwxebZQGH__qTZWo8aBXjg8JGffVPIpI8xKrm1atyXiXtwW_6hT668GkBMK4XH7oLvK1zPufG08TBWuFZ3SOnFSfJicXM9cfeJ48ezmx-1V0iiSh28VD1yt8sVnsPdIDsh_fyHlR6N3GIGSNGxGQAx2BrHWlQJ4Wk6vaQlEk-jORCNg3hRHaTSUdz8ukPpRRDKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfTySO9lhP0aP_P4WuChTZ3MbROK9bmtI1kXmNm0ogrvyvPnJv6bLCWrYbCXTaSGdx6BJOupx9EfQQ-TGdDGLODEB-EweXmChRL7JjKluXA4RcTwZ4hYI6KOWlYtZhXrmD2RH6adPwOOEQ7eHhOH4ezcpaiRlUhRm3W2ooId-l-_nbMv5_a230kvfL68-6J-tus1EnUc3psOCI_cdilVZPuODzbkersEMXqHCBUIlZhvvQ83W5lHUujl-7fIaSA_6c5K-XzATrrQls3G-aJ7rf5xoJWtwN2EOTn9IWfzlbSKo9WMXtUP9Qb4ewtanE5hGLXosbPOzk2ieRPR9Jb_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TrXcGSr5FmhcEiojT2_5455H648luOGTd6nWnreobG2N_5bQ6BO7CfuRihgSsXPniX4zL225d5cDIEzzfjzXJo41VFQ3WwspyJuoQiNUetZofNPkfMM-IulFQW6GF0snpaei82T5yYHwCiN5VzHzTiKPgtgiwTGWv9brpv8_Y79rjItHV7EjLFDqQGqaEmSlrhSC-_TwbYhxoEBejv67kyBWfTvH2kz8Int7oTPrSvXUIjrXzHbUxJeyV2NymsUR3tGoicNncusUD8YXHyUYUfPKK2ZoaUsfEPiqiALcBSaaO19IbuSkUzlxoPnkd4jdCZxGYqRrMSIGljHjKbWDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L6w-Ql3EwN7KMoEI1pfCKQT3eZuK-VFWMa_IH1SsxaWzSpJpSpmpmhbCs2wa7UpF7EvJqsF1dR_fWEKdB8YO6n7PUWTflj19pLwp-WSiGB_VHMWPDQkE9OCS-PhrFyrE2p7cj0276b8Pa462dHhID1SOXZqYPYnnpnB4sBXajDi3PJ13YjnI4tF_wfwxCbaRc9NO3j9_ej4Ul8zqdRRk4BUeEXbX4A4Uiqt_rrUTrnTtyOQsjXS1nv-w_ttCWb2v11GVFd_b4sHq1XUufP9bgBS066-5wJChgPT-qjuOxfQCiV3svysQ5aXHTJ_E3frT817BYlSAV3avYimRQXxUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i7hUHgKW96YPZx5nbcoeKOrXVAZnnMBGAq9n4uVAjtHouMqzBkXGM8dNjsGg5elWFCFQfEBoIOQ0J-G573P3-7YLvku--aXCD2hM4EJ6ZfBtcz8Am2bzYXXvMDYHgcDXILAzvWDEy2rWRuLc1XCHnTmPjcXpneSF8KrInGubQqlHP2qwPbrA_Xy6bf2sJYJhcJlqifskZ7kjsvFbZLZoo3tjqupRRZW2jDKOinRtj5vfkBp0rJM5mrazp2uYyuNAKgg-YfylrRXO6NmiTSE4_lMg0JPW5Jk2WfU7UaRjsewQWLS5oaAyVoPwvPUsgBHpBVRs8GH5HqTUbKoyKE5KjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gYCtqWmgGpifAjHF91Fncm7Lcf31D2aLo7nLp5Uftx8ShV1goPXKIjR3R-GunLAJ_2S4pWB044XWFkcGJ-L2-VSPn7jd8K4OwAEZrkM5LkOMdLm4b0YTlxaAvZ2lR0Bf0G2vMkpHqJ7_nx0u6h3EkUO8R_ee8tYB1aTSYOraf4sm36ygaqWqkQ5e6Ij5aIBgF39q0EgPUSTxbbq0pt8DoLHwtJqVn9hBWoB2vOrPgkFiC9Obuy90LzVDGTO5Il3AOUNRG1FvAQpL055_Bd2lH0nIDVy2byy79wj6binfNNp7sziZDydJO6jOXlcuRcn6dlywBcvaPgOpIdxfprN6cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M_z4gKKY3kwd3fuom9-2-xWWJ-pPlqn9orPeY4jzcU8g8SgGOpDInvPQFzqqEZtxLVzfYPeJDDqdIuHO95GEx5j8BFWhsUQzOF3EbYyzVhnwMGCI_TS7wmU8bEmRxH70HTroHYuLNRJSx8ivW1HnpDHj9LQEhtMY_jprbJhv7Id3gCEMW4msYwRopJeXJMjMFIi4i9-BKxetKrhrqjDTWcg3yAtiElMcsLYWyH4H_gx19SydCe-tu4xbX0V56A6Ik9Ngp8EZLtHL2ckkoEYFp28ziL39mBRNY7USwg-m2lyF5uZKj5UIPxdLdl_esl-A1-1tRZOOKcXM1huPCpQRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bA4VKie7bt12usvvNHw1ZJHzfp5HzXVups5VHnD1I4j_6_JLHpLNQPl9G70JqOIxIFDlxFYvwOOVs6eai1YPMb0bk5JZ49O_JSHndhGfSKhIE9bLMA7zFqhQD6RmiiIUWbTrkaXjunqQfgEHxjWReZ68U17EskQ6d3vfx13aVnt64prozjUyQVHsKzD6Fjkdhhx6DwuXPCPmrUsuv4qUgf2AKy9_2LEmjrqKoNNNYWzx8MhQUpgkpdxLEAmfJdGzyX1-tPhPB7cNchqBeM2MklXzKL3fvcv7iAAV-GlLu5ucNvugXot096wNkj4n27Uhwmah9b7mz-rgPuA4Y-nmsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K8bZmFrhs7M3-347cKFgcXHNA9V9wB4pdYlqoDOzdIaK5oygq6ou3w_QlraInFz7S7Xyh5jqOaNiCvzemHULR33c9dmzeEkcRDIvWcAtFc6IHkz-o5QTkxIqKK_wFBEUp8zZJxgpAFcAL-u88rzFLFuth5n0q7MOLDV3rfWlqwgI3XccvZK9S_Qaw6hPfAGywa7CzHptwgXhr39sOdLt4jwNIxpIcEZKdjpDKrhdUJ1iJMe-IKHjPLdMF1MjU_czzX96E77pjum1kyQBeUtvhgsf8g7ZB189b0s3AL4gG2oCcVIKjF_DkPCSM5zevG4zPBxpxxgzVUB01EQQBs2muA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GZq7k-hXGNmPbYzd44GjhT2HYqojAV15JXmTu3VOjIq6xSAlluYAAKJuDOcC1vHoU_2qvtPPiAuzdLO0Bx8UdC3-YyzuTYdZVWdBOxHupL2kwMPXOKgczJiVr5m5jHsissLp-qVGLk45HBjqhfcELsBqB1hwhJJcUkLH98373jqLhdDqGJ98OLZ0rf-DL2zZd8jZdNC95HZjTCoz5AIdKtXbDy03ixIZ2G-UgBjMDY098laPdllVDvRn4_PN4tQ1p14PVBPvv-DZvMkVLnw8-R3R558m84wFfYm_xF_ie20yBzeCuCLqBqwoTe4Grzul5aw-0cSHyqeHt1JSRcTUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U5Z1ceSYPVf_Ywj8RNU9fWRtZyxdBzPs55yzweHkV5qWIWdwPSFQkZeejMVyC1gppKN8IbJrLzujnTWF4Tl1RolHz0nU56znE6zEbCv7c3N9_7YU0AV-e9XGmybYkbtFdnj75NuHT-M0iMHCqlChW26zon6mivOIADCQNhPBlYFwRVTzxOWPzc1_xjeFPPSmfHL-7_O9E1QVpmYOWu_oFYfpAmB2_kgwMcTo2sxpI2ZtDN4xu0SXaniDfiiX4_xkc2a5MdTP3YVqtNpOJcO-Ux9YVoT697VrCz-4Y5L-bKXrV9CZsuYXIbDM2_ivwDqTeUBWJ-dlBvzT5Oc-6N8jCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3T7wEDV3qFazJDP1KMs3oQU3Am6-Q9WjOu7pjnvFV3s8uGSSvHQ5aZpxkG5FDX4jHz__wWqmZokl5kDxqCXznYHLHKgbAV1DFTtbxOB22eHRnLmz-WDwOBMa7cPPxePiZ9NzXvCYRREfQikbY4xWKEWdDwZcdBg-ffhWvAW6B2yUvi-nmDf9ArmNrbg2oK_3sAA8qZ7j37FHaBuZHN8kCxo7aTVYkDmjh12xt7fEFUNDadAbafyJ1Kt5znNCyn8nGvfvnJyef-LzaDvuPszlnY7aiozRA7YV3Yu1vicSWf4nyLIf7XZ2RfikaPeYnJkWDRtfldoj0bxL3jTtCVtxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A7yYG_ImRceB6iiTVL65E8V9BDRKTWIsSBM3iV5Wdo8wf5hBpdfJU1wgyMuF_xD4E-Ll1aVH-Mg-EW1SuYAIZQZJkxn_0uvfoyEPEE6PLALB_QXSuCUxu6c_9QdMfwOWhONq_BWOrHnRLy0pvVYOzbpP5U6eqGg3AsJC8rkwsY7G3jirEH1ZBkU8uR1eJolzGM_rwT4Rb6nkrY7NhC66A0N6WCwI1eG17EzJZn2EoignOY96MKJoflX8Ahuw4ytSwmlY9XzX7F-6Gk2Phz1tpXs-LhlDx8GxpXLHngAl_oERDWLMPFHoWpxH4qH9fuHQAVILktYCTj2bt29uJAAVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gmQNB8iB9Yq8PIa0ZOQqy4PcVeq5VA5cIpa73vqOCV6X3bOeNyEUZgQBKwiBXzR3J5YyYD-OCAnylFd37xRyJ4SYvmKsvMsG2jwKUyiOU9Ai_ijIwo89Wh3ObRLz8blj27fqKMIcFXP1rfwBMzgXnt9_9HslE3PUwfpKjtNgdzk-XClBNJiEEHN2Qfi1j0l4a0__72srtdFnHBC75kVq0HPeQEussu9kJVbQ99L4tw84q1066d8V9mG1ku6RJr6RlXJIWKRk4i6KgxW7qUzZ2X05GJ5_lnDee2fVuBa6X-VIxz5zMgYivImrnfHcGYQq86ZDfAoVTW02FA3w5tYQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BnmoXymoWxVvMtyEdnUm27Z2euvkVCmBaFHT0dOcgGF-5jaywnI6pbcD87dtc8p8zLq5T1-9Pa4BwluO3_TZhivjJyvaN8p0gRKP1zQFBJEDpeB5QrbXQop_2fhD3MTX7ZjU3hRivtR1GOb5xUNnJb8eeOimE45ZGOrOyrXitbFlZR5xgh-kKUrgMcPHomeGvvMELDYFb3RFpvi3KjEz0YP2xcJA3f2fLCVgeWZKjjGAho3ps9hYa4Uasgo4xcLtrk56rBdVa0-OjUPQ3bdS02vDw0O8vtzvQXq-Zb_oDveiiVQx4pfF9jIeNNG2wUV9_VJx08jKcpNqUyPTPlAZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OAE3Hq-NFhPIBTSOY9576Ev8LaIMP6x6xQO4iViOKAO1XNEVVDXm8GiqQZXq8GniR0JwW_tfDZOw9uTPF2eCtIDhCvKdgfM6ympp0Zlxtdlbiuc_acdSifUve6uyGrAgf0S0fCFZw51hfC0BkyNNVFvEcUu6sLeSZtZdQawTcTFfDJRDrmja0B8u0magJZbb9jwBsRGyj8EaSvF59VUovu8HPVpLCziYrCjv2webCS5bq_bMVYYkkJKZo8CoRI7_W3-OvsOgyc08BPFupDfC9b9lGu5AwikHpsZNdKvtt6wfmse5zjTuQvOPj84DsyalUy1ogVof3sngQSaUGCR6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
