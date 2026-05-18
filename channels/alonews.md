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
<img src="https://cdn4.telesco.pe/file/sDsm_-keZKlNr-QSejrR9gTOXDRKiVP4oS_kEgmYxkv5yQ6DrIJxYLxyJw5RNNGVp2N113yJD_U1tQGuoI6phqBSQ8Q--AFGo-FpGzLKHpvrFVvF6eKjCwc5bfcXBOJu7wQ-9y-Jo1Bz1gLBw9NeHbfRe0ahU72475GOkFHgbVNEdN2PeW92HmCpRh3YGI0IgNb3h5IzXiHznyQ7uLQXe-I9pl1EIUmDLFGOI3LEsIhmuLqdix0xQWT2fA3xCXSs0wnQFuMhKfFTwyWXaM6bMuheuDumHYldqGp4sW0UACHKDpT-5LgTEVf0Uuo7DgwAERmSZXsKz0ZJvQNviV7txw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 950K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 13:12:49</div>
<hr>

<div class="tg-post" id="msg-120814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت علوم: در ایران از هر ۱۰ بیکار، ۴ نفر دارای مدرک دانشگاهی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/alonews/120814" target="_blank">📅 13:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120813">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ممنوعیت هرگونه تبلیغات اپراتور‌ها و دستگاه‌ها درباره فروش اینترنت پرو
🔴
اولین جلسه بهبود فرآیند اجرای طرح اینترنت پرو به میزبانی وزارت ارتباطات برگزار و در این جلسه مصوب شد که هرگونه تبلیغات توسط اپراتور‌ها و دستگاه‌ها در زمینه فروش اینترنت پرو ممنوع است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/alonews/120813" target="_blank">📅 13:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120812">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
رویترز نقل از مقام پاکستانی: ما زمان زیادی برای پر کردن شکاف های بین ایران و آمریکا نداریم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/alonews/120812" target="_blank">📅 13:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120811">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرنگار کانال ۱۲ اسرائیل: به گفته منابع غربی، پیشنهاد جدید ایران شامل تعهدی با ارزش نامشخص برای عدم تولید سلاح هسته‌ای است، هیچ اشاره‌ای به اورانیوم نشده است، هیچ اشاره‌ای هم به هرمز وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/alonews/120811" target="_blank">📅 12:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120810">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که نیروهای مسلح این کشور حمله‌ای گسترده را به تأسیسات صنعت دفاعی نظامی اوکراین و همچنین زیرساخت‌های حمل و نقل و انرژی مرتبط با نیروهای مسلح اوکراین انجام داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/120810" target="_blank">📅 12:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نیروی دریایی اسرائیل یک ناوگان به سمت غزه را نزدیک قبرس متوقف کرده است. ۶۰ کشتی این ناوگان قصد داشتند محاصره اسرائیل بر غزه را بشکنند و کمک‌های بشردوستانه بیاورند، طبق گزارش الجزیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/alonews/120809" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4jjy--VZaLSTViqoM6hW_vAG8z13HHpaIL2TWJBY8te7wVr83L6rCkh2m6OFOECt1eQbRJKw94qypyEHnxwSuSShTi7V02q2x9BFGXmV-ONDB0xUSibROBNM6dbMuoBBL0hTGVnIR3TLzA_EHSgNnEl5kSnPtUfKyYRIs1wjSrXG5jjHhVPGpB1_FwzZa_TM2tWOc8YUrRuwRpHm5WaPd1K-tOfU-O13UnOyrd3RywIvOqUH4TJklqZwA-_GCmDubOq8znxFU_b13VkEmnP_Tp8X-OQGwvjAY2l9wYTkEHBwBXQrui_S_ANIy-g4NqqhjIAk9MEf9CY4--hoU0dRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش سردار آزمون به خط خوردن از تیم فوتبال ایرانی:
پاک کردن پروفایل با لباس تیم ایرانی و آنفالوی پیج های تیم ایرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/alonews/120808" target="_blank">📅 12:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120807">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
پزشکیان: نباید به دروغ ادعا کنیم که هیچ مشکلی نداریم و دشمن در حال نابودی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/alonews/120807" target="_blank">📅 12:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120806">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78d5c5526f.mp4?token=VpBzACjF4sFSI_k8eZE9g36BmBieYL2HFcB0_VzpT1grx9mr72tFCon0h596WsdvcJP_b4SGiZxuRr_1Ghsa9NUojl-1cmlDSBvQXnNA_nwTs8YGxswxPEOpjVTS0f4ebAqqeTLooULwrAezpOiCT9UfzuZVH9u7g3trze73CHclchcSuADlKsHj9qmrdP318CGFV08tcW5zQErsE6OmvrTfoApJ0smOckJdVjMqetEIqKvVuFPQ6IPpDE8OBBRh4jSfAeltTooYisdSSwhsL_KhqOHVV9YPFVey10r5Tjd8TkF-CR0Z7EYt1g0SJ_z2tLGVtGkXjlnlxiqDz-jIhw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78d5c5526f.mp4?token=VpBzACjF4sFSI_k8eZE9g36BmBieYL2HFcB0_VzpT1grx9mr72tFCon0h596WsdvcJP_b4SGiZxuRr_1Ghsa9NUojl-1cmlDSBvQXnNA_nwTs8YGxswxPEOpjVTS0f4ebAqqeTLooULwrAezpOiCT9UfzuZVH9u7g3trze73CHclchcSuADlKsHj9qmrdP318CGFV08tcW5zQErsE6OmvrTfoApJ0smOckJdVjMqetEIqKvVuFPQ6IPpDE8OBBRh4jSfAeltTooYisdSSwhsL_KhqOHVV9YPFVey10r5Tjd8TkF-CR0Z7EYt1g0SJ_z2tLGVtGkXjlnlxiqDz-jIhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان اگه پولتون زیادی کرده و نمیدونین باهاش چیکار کنین، کاخ گوتیک امیردشت با قیمت مفتِ 1500 میلیارد به فروش میرسه، حتما بخرین.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/120806" target="_blank">📅 12:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120805">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/120805" target="_blank">📅 12:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120804">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آن چیزی که با قطعیت می‌توان گفت، این است که بحث حق، چیزی نیست که بخواهیم درباره‌اش گفت‌وگو و مصالحه کنیم.
🔴
حق ایران برای غنی‌سازی بر مبنای توافقنامه NPT شناسایی شده و نیازی نیست دیگران این حق را برای ایران شناسایی کنند. این حق وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/120804" target="_blank">📅 12:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120802">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfpAmMsqdAfwthyDV0IS26QixuqK6QifTU4dG5MPRHIJwThnTXRpk-_Wz6xtSxUemtX6diyy0tkr3cktpmULsVO9Y8ah8Fe7bb1_ynJ7cd32SsXFIWmW05QwfxDY--HWwUVBp255Re1E8eQ-sFDsmP88USSP5fbGEV1M4BqH5coNnm1p3w2pEnK9iZoZuRO0XcQzA5mL0rUAZvJFvpIueZv9txH5I6uU1_sYe41domSUJG3igslKIEe37sl982w1u0qzIW0Z5VQyduthZMMPfd9kE7a2fPSTNETxS9O9oCy9T7OGICP2ecIin_5p2lRqzQYcfIW6vv_kHNEAPmuHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرزیدنت پزشکیان:
کسی که شعار می‌دهد باید پای شعارش بایستد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/120802" target="_blank">📅 12:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120801">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ : اونا یه برگه می‌فرستن که هیچ ربطی به چیزی که توافق کرده بودیم نداره
🔴
منم می‌گم :  "شماها دیوونه‌اید یا چی؟"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/alonews/120801" target="_blank">📅 12:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120800">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دونالد ترامپ به مجله Fortune: «ایران مشتاقانه در تلاش است تا قراردادی امضا کند. آنها بسیار به دنبال یک توافق هستند، ایران درباره توافق صحبت می‌کند و سپس یک کاغذ کاملاً بی‌فایده که هیچ ارتباطی با آنچه ما بحث کردیم ندارد برای من می‌فرستد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/120800" target="_blank">📅 12:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120799">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
امروز هشتادمین روز قطعی اینترنت ایرانه که بیش از ۱۸۹۶ ساعت ادامه داشته...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/alonews/120799" target="_blank">📅 12:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120798">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b932112c5.mp4?token=YbBdSeh7CAF3XAR_0MJB-7-EYpjHI9vKtAiVsGCRYp9EhvIx7U1QskTkglIKibKT6K8awo4afsArOy-2YWiu-upV117dzcmAUwfTgJD5SGJH2X6gsR4dNrHk2ffuIdpuDMSyqwx7lQ8C9aHsqbJohsGtyDYbYXMxyEqcKDxxhb2IqqhXDzQVSuP6zsZXSMyFwNGQcm0Nw5BMaw9uodYrS9dTnW11I6Agq9xJfzxHCOUxJMGimZZBP5XJ0eXafZy0Ml2FBz4oN823HQTV6FiLiuV8Jt555J8hCTQcLgeOAFM4kYHqS8znNuYXYLqJUkqhPtTTH5-V1WxIHuy2FXHY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b932112c5.mp4?token=YbBdSeh7CAF3XAR_0MJB-7-EYpjHI9vKtAiVsGCRYp9EhvIx7U1QskTkglIKibKT6K8awo4afsArOy-2YWiu-upV117dzcmAUwfTgJD5SGJH2X6gsR4dNrHk2ffuIdpuDMSyqwx7lQ8C9aHsqbJohsGtyDYbYXMxyEqcKDxxhb2IqqhXDzQVSuP6zsZXSMyFwNGQcm0Nw5BMaw9uodYrS9dTnW11I6Agq9xJfzxHCOUxJMGimZZBP5XJ0eXafZy0Ml2FBz4oN823HQTV6FiLiuV8Jt555J8hCTQcLgeOAFM4kYHqS8znNuYXYLqJUkqhPtTTH5-V1WxIHuy2FXHY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت امور خارجه چین: تایوان بخشی جدایی‌ناپذیر از قلمرو چین است. تایوان هرگز کشور نبوده است، نه در گذشته و نه در آینده.
🔴
استقلال تایوان و صلح در سراسر تنگه به اندازهٔ آتش و آب ناسازگارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120798" target="_blank">📅 12:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120797">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت امورخارجه به تهدیدات ترامپ: خیالتان راحت، خوب بلدیم جواب دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/120797" target="_blank">📅 11:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120796">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a457e4dfad.mp4?token=SUeojIcRHQEpC71KxWBLodxApndoJPT3wG8Cf8NYQDNGH9G44GDmReRaKdPMMVlryZsVgaCsoFVgwFW_jzmVe-zaXt4_OgMP5Mv1MouPjCUVn_0_GYjMI10ep1hYlzDk5M0JhVtnegT1d-ItyI0wSOsl_C9nc6RNKBEnhQ2EDNxruZdmhVlM-ZH41hjNALnYvULgopRUr5zrG_1sNnbpg7TtwItb-zuoDrZeG1vKkNOA-nsYW38EnL6-vojmNxOIPcftt5aBPEofKtPAfO9uhXDobqdXFaLcNDqC306sllHdiWhOrfMg3QzAtdAAdaQSC9SskuS23yGbUW0cWKJoLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a457e4dfad.mp4?token=SUeojIcRHQEpC71KxWBLodxApndoJPT3wG8Cf8NYQDNGH9G44GDmReRaKdPMMVlryZsVgaCsoFVgwFW_jzmVe-zaXt4_OgMP5Mv1MouPjCUVn_0_GYjMI10ep1hYlzDk5M0JhVtnegT1d-ItyI0wSOsl_C9nc6RNKBEnhQ2EDNxruZdmhVlM-ZH41hjNALnYvULgopRUr5zrG_1sNnbpg7TtwItb-zuoDrZeG1vKkNOA-nsYW38EnL6-vojmNxOIPcftt5aBPEofKtPAfO9uhXDobqdXFaLcNDqC306sllHdiWhOrfMg3QzAtdAAdaQSC9SskuS23yGbUW0cWKJoLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: منشأ حمله به کشتی کره جنوبی را بررسی می‌کنیم، قائل به برقراری امنیت کامل برای کشتی‌ها هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/120796" target="_blank">📅 11:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120795">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
آخرین پیشنهاد ایران برای پایان جنگ، یکشنبه شب(دیشب) به طرف آمریکایی ارسال شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/120795" target="_blank">📅 11:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120793">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2HPUHJVhDXZXGdC78c9n4Jw04EYy6I88DT7S26sI5K4EFfXOs-ad8ERLVRHvHSd8bxNKd5WPdYUvuaVF4aeREZLbAqb7ggoK9VqLevHbAJdFz6IaI50GsQj7fTKAhK3xDAY5qH1DvFT2-UxRZYI-a1oxof3IgDsQtMKYI6Yx22SwDR5uMsCjblk3zSlN2zZVXerlvII4B732uDGhK4v0WGXkxDNrdwoMu26p3QF4x-zPgapjiauYsnCAywApB0oqhofKUBolWCM2EBRxOXL5BfumH5Gv5SI56ZJnclHil_g5gGnjWPYwvlRmHm0miVF-tZVxyReut9Xa8ngDJlpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/رویترز: پاکستان پیشنهاد به‌روزشده ایران رو به آمریکا منتقل کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/120793" target="_blank">📅 11:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120792">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUa0oHSKtUYm9bOdw6OEHiHmGHTzbE0TRBcwAsy30dqSAitwu969V2JTN3qC9EAsTR7IWePZSLV_eIvSjtV-dVbA0RcyAEHrRRxmGJmwMPotEPSTJHYF84bovcbMbGDrF5Rn0cCb8K3hlZFwSN3PxgYCwEDE7L_uv6Vylctra5FwXPd2qydU2wLnTW5epiTSm2HtRwaPgx6vy4KmRpc3SQ7QeCkbWaHgRNZ5s7gipEDo_8MfYCiwPkV8Tr6Ayisaf45Rad1aYjHlzFcl7ZKg-tnbFTjpa0YwbQV931j61k0IhBHR1gAWC_ZFS1ACMvOBZOwOOgfsSR4Doh47zm_y5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی:
هرکسی که ضد جمهوری اسلامیه و باهاش مشکل داره، ضد ایرانم هست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/120792" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120791">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
انجام عملیات انفجار کنترل‌شده در اندیمشک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/120791" target="_blank">📅 11:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120789">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lasmEeKh2VBpNaZAEOSM-1hTCT-w_LZLY0tDuppx7uXZT6FdQy3QSgShKwfTEyCegsrxpvziOaDUgwyNIRXk1RozoJpA3ulT4mvLEpHjSprI3qVqi6IqesmLlTwp903emWqE-UqziAbUgQbmn1sqVp8x2BQIOZO4SQqgNwDkiPeFljmXWppJWGwoEk6FT02UHe2yvxrITx9EUE-OZl17X2i1-YIA7jCDHfLh0dPHyqk9izAEuitNeSkBoTJMQto2TtAsMHnrU4cxmoN7aXSrpTg64tNt3wHEtgzY3WUly3XHSYVMA_M0ekqJgpWVDg7ceD4TNdAtdlLZ0ium7bWglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
امروز فقط با گیگی
159
تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات:
@manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه مشکل:
@Niiiiiimaaaaa</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/120789" target="_blank">📅 11:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120788">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما در تماس مستمر با عربستان و قطر هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/120788" target="_blank">📅 11:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120787">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f97d83b5fb.mp4?token=jmJeLWksSToJrQB8Ci31IcFDDVe5AQxIrdHPpR_kxSlgDjj9Z0hGbQAdCLOwk0Dg6uQw2CxqU5NcaCJ8xFKHIvZxXOyjFCCNrWQ0aD1Mq7Xj6pcUSXpc2wk0h6A8PaeBonpGy7HuW4mXd99qRGmCOQjHiyIA45P4QfU3qZIkM1ESGZDvGgbqC3ZDVBOs64gAh71JLLChYlfjB0JXCMRtX1Ce7zRM_bTSWJx7suayS9hEaLqTTYvDHPKVRgO3HhYA2V0jXDzwPkcLBChbEtpwjJnK4EIgQuBOWiCqJEz-Y-xIKAtdabvb8ebzgtR7upaWLQeWaXO6kNUxc03sJ8bDaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f97d83b5fb.mp4?token=jmJeLWksSToJrQB8Ci31IcFDDVe5AQxIrdHPpR_kxSlgDjj9Z0hGbQAdCLOwk0Dg6uQw2CxqU5NcaCJ8xFKHIvZxXOyjFCCNrWQ0aD1Mq7Xj6pcUSXpc2wk0h6A8PaeBonpGy7HuW4mXd99qRGmCOQjHiyIA45P4QfU3qZIkM1ESGZDvGgbqC3ZDVBOs64gAh71JLLChYlfjB0JXCMRtX1Ce7zRM_bTSWJx7suayS9hEaLqTTYvDHPKVRgO3HhYA2V0jXDzwPkcLBChbEtpwjJnK4EIgQuBOWiCqJEz-Y-xIKAtdabvb8ebzgtR7upaWLQeWaXO6kNUxc03sJ8bDaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز جنگنده‌های اسرائیل تو ارتفاع پایین، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/alonews/120787" target="_blank">📅 11:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120786">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ادعای شبکه سی‌ان‌ان: پنتاگون فهرستی از اهداف برای حمله به ایران در صورت صدور دستور ترامپ آماده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120786" target="_blank">📅 11:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120785">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: با هیچ یک از کشورهای منطقه دشمنی نداریم؛ همسایگان دائمی هستیم
🔴
کشورهای منطقه به شمول امارات باید از اتفاقات دو سه ماه اخیر درس بگیرند و دیدند که حضور نظامی آمریکا و اسرائیل در منطقه امنیت آور نیست و باعث ناامنی برای همه کشورهای منطقه می‌شود
🔴
رفت و آمدهای فراوانی بین رژیم و برخی کشورهای منطقه وجود داشته و دارد که از دید ما مخفی نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/alonews/120785" target="_blank">📅 11:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120784">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
الجزیره: نتانیاهو روی جنگ با ایران برای تغییر معادله سیاسی شرط‌بندی می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120784" target="_blank">📅 11:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120783">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
اوکراین: یک پهپاد روسی به یک کشتی باری چینی در دریای سیاه برخورد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/120783" target="_blank">📅 11:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120782">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: با عمان برای تدوین سازوکار جدید تنگه هرمز در حال مذاکره هستیم
🔴
اقدام ایران در تنگه هرمز بر اساس حقوق بین‌الملل و حقوق داخلی ایران مجاز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/120782" target="_blank">📅 11:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120781">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
معاون وزارت نیرو: اگر مردم ۱۰ درصد در مصرف برق صرفه‌جویی کنند تا ۳۰ درصد در‌ قبض تخفیف می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/alonews/120781" target="_blank">📅 11:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120780">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/529e7b5993.mp4?token=C8O98HlTFdfSjgEONWjT3cuWayKwnBinfJkPOmZ3bvJZVAvx8Zl_q4LcTP-a11fVKlVyWQeoASgL8ZHXTDP25znsPRJ9A-2eoyi0cy_gimGx4jrXOdclhURZO4-qrSC2iUh6fxTB4jq895Dv5JvrM3vZWJz_rlIFWNutNtkWcnY4LPGoMP_Oyc89dfZvT2dzFv0_xUHmJzZTy9lRvGRILVDh10XPQqLDkW1GRzysej8UOzJQS8N8BAOf5cqgNXuISBxEleksg10sesMoV3UX0lulVfZQbSY4w4iSPwqqO3m8roxbXyQ6uQVeRL0ZjEuhFBuHQXgXZA8d2iYp5cD9Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/529e7b5993.mp4?token=C8O98HlTFdfSjgEONWjT3cuWayKwnBinfJkPOmZ3bvJZVAvx8Zl_q4LcTP-a11fVKlVyWQeoASgL8ZHXTDP25znsPRJ9A-2eoyi0cy_gimGx4jrXOdclhURZO4-qrSC2iUh6fxTB4jq895Dv5JvrM3vZWJz_rlIFWNutNtkWcnY4LPGoMP_Oyc89dfZvT2dzFv0_xUHmJzZTy9lRvGRILVDh10XPQqLDkW1GRzysej8UOzJQS8N8BAOf5cqgNXuISBxEleksg10sesMoV3UX0lulVfZQbSY4w4iSPwqqO3m8roxbXyQ6uQVeRL0ZjEuhFBuHQXgXZA8d2iYp5cD9Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس پلیس راه راهور فراجا:
شب گذشته، در جریان یک تعقیب‌وگریز برای متوقف کردن یک دستگاه خودروی شوتی بودیم. این متخلف برای جلوگیری از تعقیب پلیس، اقدام به ریختن میخ سه‌پر کرد تا بتواند از دست پلیس فرار کند که در نهایت این اقدام منجر به پنچر شدن تعداد زیادی خودرو شد
🔴
در نهایت خودروی متخلف توقیف شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/120780" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120779">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: آمادگی ما از ابتدای جنگ رمضان بیشتر است/ از سختی‌های مردم مطلعیم کاستی‌ها برطرف می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/120779" target="_blank">📅 10:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120778">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0L_cUhez7v3cK05ickDvrATrx3QqMrecJigWcaoUX8L1tR3C5UzPU9wNLhM1nWKB0DQSDMHVaSQKQgiKbwR1PUw5TyxS55Ef0rr0Y-6w0L8KTxB2tHwhYYh1s-RWESUCbwO9RbLH4pEqFAwkfSqD6ytLNcqR50a2PoWiXm5pCzaQBhAi9GRsUuA6naxADnHnCBct5m86ueyC3_oP24ix0nBl9OH2GMz4CVs8Z5bxXu1VI3EYgz5vCxHwkwdfqq7kSyLnKLP9MEl3RKZid2J8ZZAPoRbXtXjloH54KOH78Ed0NR88pBzhwJIZr_1tY95LyBE5ebXGFXmdo-PkX60Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طرح جدید ایران برای عبور کشتی‌ها از تنگه هرمز
🔴
ایران اعلام کرده به‌زودی یک سیستم جدید مدیریت عبور کشتی‌ها از تنگه هرمز راه‌اندازی می‌کنه.
🔴
طبق این طرح، مسیر حرکت کشتی‌ها مدیریت میشه و کشتی‌هایی که بخوان عبور امن (Safe Passage) داشته باشن باید هزینه پرداخت کنن.
🔴
گفته میشه این طرح با نام Hormuz Safe معرفی میشه و در قالب آن کشتی‌ها باید بیمه مخصوص عبور از تنگه هرمز دریافت کنن.
🔴
نکته جالب اینه که طبق گزارش‌ها امکان پرداخت این هزینه با بیت‌کوین هم در نظر گرفته شده.
🔴
از طرفی موضوع دیگه ای که چند تا  خبرگزاری فارسی روش کار کردن این بود که جای هزینه پرداخت کشتی ها بیمه ایرانی بشن و ایران اونارو بیمه کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/120778" target="_blank">📅 10:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120777">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
حملهٔ هوایی اسرائیل به دیر الزهرانی در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/120777" target="_blank">📅 10:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120776">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: از گروه 7 می‌خواهم از رژیم تحریم‌ها پیروی کنند تا از تامین مالی ماشین جنگی ایران جلوگیری کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/120776" target="_blank">📅 10:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120775">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
کانال ۱۲ عبری : جلسه محاکمه نتانیاهو که قرار بود امروز صبح برگزار شود به درخواست خودش «به دلایل امنیتی و سیاسی» به تعویق افتاد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120775" target="_blank">📅 10:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120774">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انجمن خودرو آمریکا: قیمت بنزین در ایالات متحده افزایش یافت و میانگین قیمت هر گالن را به 4.5 دلار رساند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120774" target="_blank">📅 10:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120773">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7iLDWMqKIL0IAKgo0WaGBrA8kwVFVzv9NtGmaxKLF9jh6Hbk6CV65oGUvsPx6PAjGbUTRIlGrx046OrArFTHq83OC3YOb6wBoX20eYgd3Pkhg68h2Nq9W2lP_o-hyIJM4fLFi9BPImCg4Q29-KzhVAs4wW76whvmkR6NMU0VfsMJUF9YgH6iDA2IrgJ_2x4W4dHEAkvaftilFDMp680qgxwKgUwxEaA-HYVz_Ge2YXyoFHMMW8G4PILZk-qO2_SyCZc8Ns61hHReEDl1DUdl_wEJ-b_G6sXBCkiBjCE80HHwje7deFxpGGiOtg6Tlcdxn9zwCbPniqOi-eNG8qazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان نایب رئیس کمیسیون امنیت ملی مجلس: مجدد، تهدید رهبر انقلاب و فرماندهان نظامی از دهان نجس برخی  مقامات دشمن شنیده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120773" target="_blank">📅 10:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
از ساعت ۱۰ صبح امروز انفجارات کنترل شده در شهرستان دزفول انجام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/120772" target="_blank">📅 10:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbff622c8.mp4?token=DdoTmdd-XQYZaeTvX6sbLZHDsvFEVOqvbgiIXktsPF3W2AgS5Jn1fAnO47v4FbdeBRy8VWX0G8ylwLvwQDT2PtalaEs7jS11FCUNmLcdFO4Vs_7TiFwnklOOmWCEDbOc6cI1FlAHy_MTskK2dkvsM2_4DkxMCuKnLKAHXkomzK7c-jjeA3YVGtvG8Nx1gyjR0L54CEobY0p-XelZ80aTUsIy5bMM3qdWhi8kVwpYe0mBBxelnJR6wDA-tp7WAYTmiTGCR14H9eqhbgbHZmoaUPQTE7_9Rq8O7kLwWWorF_3oi4imsb7zoaZhlq_ifvQMEtocHzkD4XZ-7qOnTlDoVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbff622c8.mp4?token=DdoTmdd-XQYZaeTvX6sbLZHDsvFEVOqvbgiIXktsPF3W2AgS5Jn1fAnO47v4FbdeBRy8VWX0G8ylwLvwQDT2PtalaEs7jS11FCUNmLcdFO4Vs_7TiFwnklOOmWCEDbOc6cI1FlAHy_MTskK2dkvsM2_4DkxMCuKnLKAHXkomzK7c-jjeA3YVGtvG8Nx1gyjR0L54CEobY0p-XelZ80aTUsIy5bMM3qdWhi8kVwpYe0mBBxelnJR6wDA-tp7WAYTmiTGCR14H9eqhbgbHZmoaUPQTE7_9Rq8O7kLwWWorF_3oi4imsb7zoaZhlq_ifvQMEtocHzkD4XZ-7qOnTlDoVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از زلزله‌ 5.2 ریشتری در جنوب چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/120771" target="_blank">📅 09:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120770">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
بلومبرگ: بی‌ملاحظگی ترامپ درباره تایوان اشتباه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/120770" target="_blank">📅 09:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120769">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بیت‌کوین به پایین‌ترین سطح دو هفته گذشته رسید
🔴
بیت‌کوین ضعیف شد و به پایین‌ترین سطح خود در بیش از دو هفته گذشته رسید، زیرا ریسک‌های کلان گسترده ناشی از جنگ آمریکا و ایران معامله‌گران را وادار کرد موقعیت‌های خود را کاهش دهند.
🔴
این ارز دیجیتال اصلی در روز دوشنبه تا ۷۶,۷۱۱ دلار سقوط کرد، که پایین‌ترین سطح از اول مه بود، قبل از آنکه بخشی از ضررهای خود را جبران کند. سایر توکن‌ها، از جمله اتریوم و سولانا، نیز کاهش یافتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/120769" target="_blank">📅 09:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120768">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b623dbe873.mp4?token=H_a99jnzf7znojxvvTbgj9kdEb0FTbuf6dyHawc1p6BU4leX6oBMRaW9MFgQfdvLaULtEsRbRm0Kr2WxJbNg3_6FhW0EyQQuj4V1PGn0m11eAWpGK6nsvi1yR22UKPUU8ECo3ELOT_3ylrHDd7jhDvkmaEAKLzL0jaI7QVwFoOCpzv60Pk1wasATddzouKDGWt52CdS9addblhMx51KF-eJ9ZXPx73J_QL5eK647zZF1oG_8xjV9hj4gLyqq9BK0g_42BoTQmmCtQk7q2ASZrEjmDjEYAeFAkeA8b4SHf-ZFKP11ZgG-dMWnK2ZvcTz18jaGLnfuB2y0Cle49B7NMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b623dbe873.mp4?token=H_a99jnzf7znojxvvTbgj9kdEb0FTbuf6dyHawc1p6BU4leX6oBMRaW9MFgQfdvLaULtEsRbRm0Kr2WxJbNg3_6FhW0EyQQuj4V1PGn0m11eAWpGK6nsvi1yR22UKPUU8ECo3ELOT_3ylrHDd7jhDvkmaEAKLzL0jaI7QVwFoOCpzv60Pk1wasATddzouKDGWt52CdS9addblhMx51KF-eJ9ZXPx73J_QL5eK647zZF1oG_8xjV9hj4gLyqq9BK0g_42BoTQmmCtQk7q2ASZrEjmDjEYAeFAkeA8b4SHf-ZFKP11ZgG-dMWnK2ZvcTz18jaGLnfuB2y0Cle49B7NMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدراعظم سابق آلمان، آنگلا مرکل:
هیچ کشوری در جهان نمی‌تواند همه مشکلاتی را که با آن‌ها روبرو هستیم به تنهایی حل کند.
🔴
حتی کشوری به بزرگی و قدرت ایالات متحده نیز، به نظر من، باید علاقه‌مند باشد که چند دوست در جهان داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120768" target="_blank">📅 09:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120767">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26a53fc05.mp4?token=g4xpO_tu7xnFj4Hy9Ic4lJHirHvdM916lsDpnP3CKr5NNeIqhkSpJVLhxHOWIFYrJA8MwAxhDrIoxBNUMAdKaRFsUz0AaXzUw3TAH253CZ1Idar5WcknsmKbbmoV1DmbRhPZfr_LSuvjwKVpuMg6lywmgaPXcdMR483HdqstP3VXySMuKko022v1fE23UWQYWPx82QYA2opRgti8c4W_nIlSgJGXtV8NA3rJP_OaATbPNHjLo6XPd0Ob18pTVbvgVVUIdMPMvXuh3UkDy8m3t2ugnypeZReImKFwyMW6KcQmuFUCDJ0Jitl1wqc70PqgAs63bdGgA16kOOfooaeH5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26a53fc05.mp4?token=g4xpO_tu7xnFj4Hy9Ic4lJHirHvdM916lsDpnP3CKr5NNeIqhkSpJVLhxHOWIFYrJA8MwAxhDrIoxBNUMAdKaRFsUz0AaXzUw3TAH253CZ1Idar5WcknsmKbbmoV1DmbRhPZfr_LSuvjwKVpuMg6lywmgaPXcdMR483HdqstP3VXySMuKko022v1fE23UWQYWPx82QYA2opRgti8c4W_nIlSgJGXtV8NA3rJP_OaATbPNHjLo6XPd0Ob18pTVbvgVVUIdMPMvXuh3UkDy8m3t2ugnypeZReImKFwyMW6KcQmuFUCDJ0Jitl1wqc70PqgAs63bdGgA16kOOfooaeH5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدر اعظم سابق آلمان، آنگلا مرکل:
ترامپ فردی است که با شدت بسیار زیادی اهداف خود را دنبال می‌کند.
🔴
هرگز نباید افراد در چنین موقعیت‌هایی را دست کم گرفت. کسی که به موقعیتی مانند ریاست جمهوری ایالات متحده رسیده است، قدرت بسیار زیادی دارد. و به همین دلیل باید او را بسیار، بسیار جدی گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/120767" target="_blank">📅 09:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120766">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قیمت نفت خام برنت ۲ دلار و ۳ سنت معادل ۱.۸۶ درصد افزایش یافت و به ۱۱۱ دلار و ۲۹ سنت در هر بشکه رسید
🔴
در حالی که ابتدای معاملات تا سطح ۱۱۲ دلار پیشروی کرده بود که بالاترین قیمت در بیش از دو هفته گذشته بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/120766" target="_blank">📅 09:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120765">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پلیس راه: جاده قدیم چالوس ۳ روز مسدود است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/120765" target="_blank">📅 09:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120764">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
جروزالم پست گزارش داد: نتانیاهو خواستار لغو حضور خود در برابر دادگاه طی امروز بنا به دلایل امنیتی و سیاسی شد
🔴
دادستانی اسرائیل با این درخواست مخالفت کرده و جلسه را به بعد از ظهر امروز موکول کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/120764" target="_blank">📅 09:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120763">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وقوع انفجارهای کنترل شده ناشی از عملیات خنثی‌سازی در یزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120763" target="_blank">📅 09:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AE5V5j3U3i_EiFqNx_zc2BnAjob7J5rYVcSwJFwKrkey1k5I6s6XETdImsj3QtJ2lTTDBevpjj_exX1upUWUgbgY3OZDxHn0mEQXZNZbrs2gaUSEDaugMsZeYiY3_YYBbWuFgtlW72VOUbE6uoC1lPqEtU9pFB4X5UM_M4lDYxPFJ4m9fd1f_DyqsrljURiIFHA30K2XElywtB9KWYdseQAGMmYhlU9zfXSbyi5KIgsuZvhnWX9Kue-h35wxYTQXXwSFA9FLlXvWh9FUgCY5IlOCl1s0knVa6n11hO836bYKJEyEX-wppZwV67oubobS4OzAHyHVvLNDEa56URwHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOLe0BsaQNOmSkVRkDHy0DbYwZFyXPqGQ4ykfwdpxvnZyfdbJ2sPS41IL9vqvLDhjlgWfVP4dqSumcFvInSf4f7Gxpb0pOvLX_nr0N66QwU9BJSn8OShlGxfewqyIYb9Z1nh1bLy5H87OaD1Kq69ytI7YcWHB_XG9lM24CBF4uro56-UGBRiHe1u5DZ-A8vLbAQODmqHyLuWB91QarYaFoZUwRkmgY8x9TIkJbEj2HYFB-_5KRC-9jnESNXOlxfko-er_KiNOUetRGiKM-KPLedBSzagUpouh3URRhS1ngIMwGkY6XjpmTTaQIBg1VME51OW03PycSzWKA8ZxYiQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_PKt_pFVXklTTIyDph4ga09RWWH31_6Pv9W5OvccL5m8Ix4pwL2OGNq5B7GAxDrnpRw78iChSfNw34kEgFvHhKx7fSLYs-dIlAM9P-Sc7FfYSkLvxJIhZHVxiO82QZP32RRZIyaqjPzcMOlGp4V3xnVVtdkwgYYb5PZMH1GWafkhQTGDZGOi42lYsPZ1nPls3KWVVTweVI1bsavoQrtZqeQ9xCVZ2nQHPRWXKCUAiCI0EfzbzvjEGMMeNt0v9eBaf4iKMsetGac_3nNdr2ekiDpSxv_-ahCuOl_D08__9l--gjc6iq6YeauTJH9ND5vKCqZOC9Klje5o-xP9ZWFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZV2yr4N7bgp7e2F_ADZDUz_hbO725vV9e11xHFPLJHEFUEof-yvpDTCi1ginJUrPrVnK3iNopbyMJwHHMVHWxsS0p8HJUN-w1CwkH2R5HiRgcCYLwqBbenufSAM3E0lIm5cy4kieSpQHX-bUjOnPUlIju5tTJTGdVUvhUZSdu7_tWlL8ygOHnShO8-AHWmM_4RjOYONmeci3viW7smzRCEbVafDz6pKOpKR8Ofap5MCXrHsfyqzlftLUMnz36Bkf8DB4C-iVeiz98pKAQZ7ZeZUCu1mITjZpegNBNFvzZEkBxm73rhSr1gZNbjpL3Yxf68nWR9kd2f-eqf6_nLb68g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTUbwHOSJmIXgx1YPG5Ijq4RUF1Y5SonXJ-YQKIOc1hMOwBWp3eT3DMEbo6srIOCusfW7N5H-m6owSYRQwSf3NmtehrW0DNq_JJ6dir2OaApJuf923JtOb9NoEsYVBnLMyTqs4gk526rb-raLY1ukZ1S6wCIgCPTfAcnmNV1CPcpXiE3Q9Br367EU-vkZ67eztUlJjhi1ijtAkF0SUikHFzsCEgYGEzFAU8NaR5ebXr9XX--MyQYpEmzMNV0n6VWKdeedKJC1F2mUjNamxu38aSV88GoVvBnu6jVTbUiiOqFhRpzVu6aDzvzUQG-M6vVc4JqmekCjb3-ecpy7P2haQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wdk76tDPwUgl5S8wOEQakVY9LMSUN83rRcqE-fkQArhvzerhjXpn4TtD_hqhSdDj-spavWcWEmUyE-ZZ0MFV2tDtTvNAzRTXlHHZ1tR62h5a1c836UoNstepx5EjRiNGZlgi-FN1AKEr6bhTD1OR_GfZ4C0XuRvz6gZF894003scnyzPYcp31ZIj8xaKMut3IfGgWpm5Ad3Ptu2XFwM8tXrQt1g2azibx_R-gpOEJif-pNNh8NR5f8ybMbgtOri3S4gZseT5oQ6ZkIwJ04m6rZ3HzlwRH5e0Gt8ovMmfdfF5xfiJJsMgGuKwMwuL-K7V1TGJB_wFdqGf0yZEvFZ-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsmV2FVgpwuxD_Ac8gKd3r9Z5reHTigCDgB2ifC0gsVt3ngTtl3W4fh7m7p3xGXvgenx0R8mBzEMFljnzupEI02xVZ-EXK5CC_0-LqkQd8wwRlY8YFpW6uRtkaYHuJSp-1BJZMGkwTWrfuTm6gRoAqCtgSBzzXJHYerc0NNJ3eZ4IZT-8uAMZmBj9SCAdCg397fBzOp6_sjTtPJ36uks_EbMvGO8AePKD29AjYJLWF0Jeb3XQl7Em0OSnc50HvkQuk6SMsvBc13sWr9KbQb53i_gMWfprDzZF-ryeuqDrIl27d-e6AjV4wd6eel6v4ZxA7mZXO-lq5tnRLopc1uIVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O8LPlm8I-QP99Ceh1zP1iE6NF1-xzUmK2POq7gRXVV1HKDSi2TvEeL6HYGoZ7YyrnTbNnfzA_cArzo6yyWsMoUOkIXwbORPiLzpHNxACFo5-spn9y3LFCcW3QO7g_A0hIF5RQsJZz2lmYrKB_0WPfo5s5XsWycidCMdpZGRRWx_rw6O6RlM-mwoDqcwiXzaj44C2L0bqIJlGdjd5FelNiqeAbnHk-5VxhnZhuk7DQ8OrpjI2kfuJiBelwrryalL3H74jS4XLT89L0prYW8-DeBY8-HCeNs6veaXSVi9ta51lA2VZ2EPwG1g6_Sroh_4wtKap0yAq2SznlO5zzj1G6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_sN7yOwOdo1sIC8SNhupYoWgaDGGFvSbAZ0a9QqslI2nh6NMqg4D_oIFK20y5uoBHIb0xnhPM7iPdlaUWRwbLaQpKutMmu_5aEIhhOIDa0_Ivo2Y5iGyim5kM2WUsfRGJgfatjYL72d91QLNji2oj0asoOKfqpwC8wILgQQvLHfku7MZygFuJPzN6q-RfFDDMnPxBY-wi30vevZupxhliKHM8SF8MOum1Y97na9B9H8X_IKkluemUFDfPOVT08yVUSGj_CJfr7015bzJkP7xT2KPqE8tue0HNO9PBlovbPgbh-YSUkEU_oIEcr-LI1UYKxaIzF4n_vS6Ueq7jTUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ldmi-FAQzoYl76LpVfHzU5oEJm9jk5P3-1f0njC-KK_EOeYC8d_TLtWtQKh5xFbZ40qLAbPCZjVNlyxoHnJdIKzHK8vsaUZuJ5NxqX8Boycj_u89VG84WLl_pf0bdHSL7Ge3NwYRLrBz9yWkp995oQ6kgm70ZQN_-OZ0LfwWAqbPDxHeMY-Oxax_FDKJPbCx_yosAitORlRyfAKl2wI8NcDzlMuM364Cnk-_oDPCXlwgs7Oxb5P5k7LbvmQs4NRXUfp4AKBHgUY1j03B7wg68u4AxmzyLXvqbQQSvVWcCsUBYpyJQDF6K1IWNXdBi53falFqQv9HEQygGZzY-SNG3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
مجموعه پوستر های ضد آمریکایی، اسرائیلی شورش جهل و جنون کمونیستی-اسلامی ۱۳۵۷ به رهبری روح‌ الله خمینی.
🔴
طرح پوسترها ایده گرفته شده از کمونیست
🤔
هیچ چیزی از انگلیس تو پوسترها نیست که انگلیسی بودن این آخوندها و حکومت فاسدشون رو نشون میده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120753" target="_blank">📅 09:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
روزنامه ایران: در پی محدودیت دسترسی به اینترنت، بازار خرید سیم کارت‌های عراقی در برخی مناطق مرزی غرب شکل گرفته
🔴
در بعضی نقاط مرزی، سیگنال اپراتورهای عراقی تا دو کیلومتر داخل خاک ایران، قابل دریافت است
🔴
ارزانی این سیم کارت‌ها در مقایسه با هزینه فیلترشکن‌ها، از دلایل گرایش برخی به آن‌ها عنوان شده
🔴
استفاده از سیم کارت‌های خارجی می‌تواند چالش‌هایی را در حوزه نشت اطلاعات ایجاد کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/120752" target="_blank">📅 09:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up56hr1LnLSXtdstg8ejz3MHxBdsAfYp-n-x4YH4zTU5pTheAHgOYlTDmmp2dZDr8Bh3DQiifOw09R7mjseYj7np1nSe_IXtnYmgpLjd8zUvJ9VBFlzrL4UmSF6byj_4a7v_ps_29V22RlHKfl5jTAm6YplH8iUs6YY_csv1KXJX64XEfN1Ihba8Os4XjpXLUU-pOg6bi0n3TgYBzPGEuQQyXmhqLzB5x1_MhNxp_SXkYmsFzVC6VXXFZ-2CVd0sbc146DejCfDClqGUXKPLQBXuyYHujyr7Uhza6LImV9qgmSFgbFMxQ2XjEtHxaSGlytFklpERE8iXatp9lkdy3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت به ۱۱۱ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/120740" target="_blank">📅 09:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / کانال ۱۵ اسراییل به نقل از یک منبع: نتانیاهو به دلایل سیاسی و امنیتی خواستار لغو جلسه دادگاه خود در امروز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/120739" target="_blank">📅 09:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdbbc8b30.mp4?token=bW3c2wWKRpYJA2L3IWMjSDvZv0dGrWGAejeOEZKUmwREuBd71uRvuM5B_TOQl-JougSpBwqq5mj5GErCODZ2qflnvUEephUDpERp47_MsifRs86pERNgo___otjjHZsjQCeXizwcjBKrAZObMa27LvpX69Az4uBzQ_yS-PpuiQedkdENJWtYtVMk3PvBcnIhM5lkn7GtcESx0i9OTBpTiyskXpwwKPfO2dnn95e3H2xJdmingQt2E66vxj8QYHyRAurVRGTJw8EuzI0wUyhdQdibgt3h2ByGnfQXHtE5Catf-9sUKFCS-vX4Rmj84yBl1StY98JcvXhvyVwmENTX93XFIqUOIOQyCYsFh_uX8pbX9cUpW0Y5QjuNAcUNc0l1tXGgkTpbyA7lRisKUSh_vfm1O80y_zNQkEEu-EO8530BKNYuKJQAk8GRNeDQnO9Lmo3AwxzwzBW3x9wTcWY4CA3-SrhihZfqaHtB7pZpj0htYvQE8_eqhlkPP8-Et5BiO4TSpYFJVKhuDb8oGlxL4WnmZYNW8hF4RKGrTzGOl2eEN27tsRLndMZGnZk8uRZ16ddMvBVEgYn0DXToqY-V-rIZuwRid1J4xw2IZWIasMJDJBKrCCE440Jypeyq0swuLQ1d5NYnp92fFOaiQutJjqxu7M1Giu7A7gPTmWyUTf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdbbc8b30.mp4?token=bW3c2wWKRpYJA2L3IWMjSDvZv0dGrWGAejeOEZKUmwREuBd71uRvuM5B_TOQl-JougSpBwqq5mj5GErCODZ2qflnvUEephUDpERp47_MsifRs86pERNgo___otjjHZsjQCeXizwcjBKrAZObMa27LvpX69Az4uBzQ_yS-PpuiQedkdENJWtYtVMk3PvBcnIhM5lkn7GtcESx0i9OTBpTiyskXpwwKPfO2dnn95e3H2xJdmingQt2E66vxj8QYHyRAurVRGTJw8EuzI0wUyhdQdibgt3h2ByGnfQXHtE5Catf-9sUKFCS-vX4Rmj84yBl1StY98JcvXhvyVwmENTX93XFIqUOIOQyCYsFh_uX8pbX9cUpW0Y5QjuNAcUNc0l1tXGgkTpbyA7lRisKUSh_vfm1O80y_zNQkEEu-EO8530BKNYuKJQAk8GRNeDQnO9Lmo3AwxzwzBW3x9wTcWY4CA3-SrhihZfqaHtB7pZpj0htYvQE8_eqhlkPP8-Et5BiO4TSpYFJVKhuDb8oGlxL4WnmZYNW8hF4RKGrTzGOl2eEN27tsRLndMZGnZk8uRZ16ddMvBVEgYn0DXToqY-V-rIZuwRid1J4xw2IZWIasMJDJBKrCCE440Jypeyq0swuLQ1d5NYnp92fFOaiQutJjqxu7M1Giu7A7gPTmWyUTf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلزله ۵.۲ ریشتری در منطقه گوانگشی چین
🔴
بر اثر وقوع زلزله ۵.۲ ریشتری در منطقه گوانگشی چین، دو نفر جان خود را از دست دادند.
🔴
هزاران نفر دیگر نیز مجبور شدند خانه‌هایشان را ترک کنند و تخلیه شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/120738" target="_blank">📅 09:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وال استریت ژورنال: صادرات نفت آمریکا قیمت‌ها را در داخل افزایش می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/120737" target="_blank">📅 09:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روزنامه خراسان: احتمال بروز جنگ و ترور مقامات سیاسی وجود دارد اما غافلگیر نمی‌شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/120736" target="_blank">📅 09:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120735">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در سردرود تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/120735" target="_blank">📅 08:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7d61b2b1.mp4?token=seU_iPQ3k-dBikavVkQuDLo1qBrV7OxNrapltyuqpfJM75mbksZZnnbKH39vcV6XF90B_A7ofGFPWHYFC3M-uSTgd30uvxIPWPD1-rAI8J5DnGs5drjOwXmxQjvaOGEM-ffloqwSBejxN7Bdjb4Cxm4K-_4bBvSJlgCs0HySd0ItCb5uPM_Lj3V39DzMNo2-8FirDXBiYoRzP34Gu4G--mA-fW2n3dGagi76-bPIdbE_wtiBiREyg0tl6dptsLqfmYnzKCLnKPtsf7txldLcYJFJmrCvze0Wwx5WXxNa1tuJWT3p45rxWQK2cy-D9DmuKnefY01RCkdtnT8nVsbBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7d61b2b1.mp4?token=seU_iPQ3k-dBikavVkQuDLo1qBrV7OxNrapltyuqpfJM75mbksZZnnbKH39vcV6XF90B_A7ofGFPWHYFC3M-uSTgd30uvxIPWPD1-rAI8J5DnGs5drjOwXmxQjvaOGEM-ffloqwSBejxN7Bdjb4Cxm4K-_4bBvSJlgCs0HySd0ItCb5uPM_Lj3V39DzMNo2-8FirDXBiYoRzP34Gu4G--mA-fW2n3dGagi76-bPIdbE_wtiBiREyg0tl6dptsLqfmYnzKCLnKPtsf7txldLcYJFJmrCvze0Wwx5WXxNa1tuJWT3p45rxWQK2cy-D9DmuKnefY01RCkdtnT8nVsbBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی‌ها از سرنگونی یه پهپاد MQ-9 آمریکایی بر فراز یمن خبر دادن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/120734" target="_blank">📅 08:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_WE3PXBkiL--UAUijeebanDufwSfCMKruEWiKCLr83Z8UfiQ0aCsBerXdClRatam7eADSSmWz2RHH-V3HpgzK8ROIAgQCHaDgxOIlU3Vivn45lsCMJ4zinOC8ByWtyJ4t8xCHHjV6ugSOfqHGBq_SpPnut7PRX-ZJpJYXiGwBzN_LHpxdnmBKVvRlpC5OjvajJUbR2ENRIGTaQqFi-xmMv7-Hr4B1NI26eQG-ekI8kaKOTagf5JXDht8tISGCFj9_Egka9qTyHx0BCX5KrnpnwKF66IYLNudsrd1uU5LKTIT5SINpiCtznqryTWz9tbIHKEbISuUV-OXJnuELzZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b5a516aa.mp4?token=hHsqZjFJJfeF1tgF-JTM9M2I2NwaCkG0BtxkqjvemEWpGm-cCLhwoJrfxsyJ1RY_PdhnQ1ydvGA5app6B3woarX8R82DvC6LoEfP85Ry_6Lb2nT6a36DnZ5PN7hdMVAi5Rg3ReFmfzkVZJY_XRTDM9mTOdCuArJ6bX7CVodrvWYM0dVEbFMBrRorf8Ar7bzWx5neF6nrGWRhr5OmesylXY7PfHiWr5Be4fuU88BThyI1ZbQuFa19naurYYQ9hQfqnZbScMMmIor4ndvM7UDPhllk5z_pg6oKTq_k_v5YpyFiKYMLzgwrzzG-QqbGI-KddsdNGmq60PmvWtCIitf9MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b5a516aa.mp4?token=hHsqZjFJJfeF1tgF-JTM9M2I2NwaCkG0BtxkqjvemEWpGm-cCLhwoJrfxsyJ1RY_PdhnQ1ydvGA5app6B3woarX8R82DvC6LoEfP85Ry_6Lb2nT6a36DnZ5PN7hdMVAi5Rg3ReFmfzkVZJY_XRTDM9mTOdCuArJ6bX7CVodrvWYM0dVEbFMBrRorf8Ar7bzWx5neF6nrGWRhr5OmesylXY7PfHiWr5Be4fuU88BThyI1ZbQuFa19naurYYQ9hQfqnZbScMMmIor4ndvM7UDPhllk5z_pg6oKTq_k_v5YpyFiKYMLzgwrzzG-QqbGI-KddsdNGmq60PmvWtCIitf9MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله موشکی عظیم روسی کمی پیش به شهر دنیپرو در اوکراین هدف قرار گرفت.
🔴
حداقل ۶ موشک کروز اسکندر-ک و ۱۰ موشک بالستیک اسکندر-م به این شهر هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/120730" target="_blank">📅 08:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R1WJ8vX2t1TjtCNhma2Hs_g-35ecOq6VA_kP0QYNDiF9hq4OPlc1Ju5g1JKnZvu2OWvIoM7ODaGhcbnfOezSo6Qc86tKrEv7CzNj1_h82_syWAnhfrNnN1L73AbnbL06uqSzT85utlMd8oAF_oRYPdGpyMTWwD3q1i7LOhsG2aA37RHlxjJ0eQXMUvhrMBWhR8uhD2S8o4jhe_9cmOn-NaDnQvpCGwysYFoxUxFNcNUoG-TkMg84LTb109xs3q7AnFVTnorjdWMz97QU0XEbh1OQ4nj8kGKICBFxVQJezddn5SLo1fiHX1P4Acfb5-men3U1SrPeYT8DaVB0cM6h1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ev-dhQWf6QbKpvQfwmuA4S1VZHu8QdPYBXeN8xtmdpdbj0m_AbMumwurKG_htnXIPF6yvorV3K3wB8mIXttLVhaDOd9HDIXEwmeryxsIfVZLSl46ktV67Y8ZAbGFGbP4Xu7U34XJoFd8TTy6rq89wcG3x5fCQ6orY67OfT7s9JnHVHWgk7WKnHWqfM6MyYKYJGHErDtncUjNbMm2dLxpiODssf0LyD5tp5pFm_6LHz66EyLU_5sno3Cix2RLxIR-FazRJ6qQMuC9vl-B2kOh-YoHjOZP-cz7JOVcNLYbpBaSsRwPxk2JIwhr9X1rxwVX1LfEY4U6oO_qags_LIROKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وضعیت عجیب صدا و سیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/120728" target="_blank">📅 08:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cy-cBaXyNJTDSADPmIlk09dNVGka7drvQo-aKhoLWvgnOcZ5OLM2m3E1KlTia8IIcyr1UFu4DCpMmnMKMo5FQl1WcI4-ZlBo1BYWqaLm6g6yoKAdXbDXkqIjkpqashRNn_aShX3wKdeY6UjP_mGE2lUC8-UT5xL3H3BYmotBkN6XI2VrjnuJaePjiy4-Vm5_nlBXsI8SF7Yumc4WK0aYXJWz_hSvb-GtowNrgVC7jaZZ8zuFv3biuPQ-N6Vr6bhh7xYBvqHcnDACml7Rhl8WUCOw7IrCTkEXI0c7Ic7dUPJhpnrANq3XUui4QNWqG1FgA7vJ6nZMVTvzhE90p1XaSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تحلیلگرا عرب:
احمد خلیفه: داره اتفاق میوفته!
امجد طه‌:
⏳
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/120727" target="_blank">📅 07:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRTuCZQTGOATGdaugZTljhnt6mFphawHdIv1Fc4cjOCHYgxcIRGMotsC3XKgnm1yNKkcBX5ivdchkpkMrggcVi2RFM_QUhKCha-z2GBgKlvO5PBL_JIxfkJR6p0Hxn8-lJst-0nUZ4DbUiNdVSwQ5WeJiyYMFxx1S0fec61edv-QIRkR5QLKnGzH5qYir8DpQBKZOmDGvDMPqaxx0QhMK6rDOzHGwAO5n7TJqxIE1fCXfChN1JG4GzTxkMWONaLWsWm-hI_zo6ZolLAI3tHoab5vZlGavOYWMqBP_WcM8cHp88wJ4TB69BqcqOKHfYT4lLgOXyycmHYNL875uEuGVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مترو هم پرو می‌شود / مترو تهران برای برخی افراد رایگان می‌شود
🔴
در طرح پیشنهادی شورای شهر، گروه‌هایی مانند اصحاب رسانه، خبرنگاران، پیشکسوتان ورزشی، بازنشستگان لشکری و کشوری، امدادگران و داوطلبان جمعیت هلال‌احمر، افراد تحت پوشش کمیته امداد و دهک‌های درآمدی یک تا سه مشمول استفاده رایگان از حمل و نقل عمومی می شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/120726" target="_blank">📅 07:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fouF9S0NRnODqK35BwISQd8HpTw-ncxj9KaY7zzwGt7DSSMZ0AdXFFukUeFxShxkDboOucFLrJmE2Kx3DvwcZgLzq7YUtaswYPMSwE5BJf8sK3eus0kRWmJmGz2_7-tJSQj6nSr075DM7y6zcyoeyvpOElJqsDubiXdVSuiagsTdpdtQj6drRcthYWkkPiPceVMA5DJs62aMVGpmTIdvQ-mp8kstOL9Dc0IWSVaSIWKZlVgJC_pv9wolGRCMoU01C8SlbYhdXxoWZyUPrpivtF1SmARoWdEdADE6VTkpJ8Kz0UzQ0-9oNALcG-K8KaXumfG92OqsHgPbkNP9LQcDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💥
اینترنت آزاد و رایگان
🌐
🚫
تنها جایی که کانفیگ
رایگان
میزاره
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot
⚠️
هر ساعت 100گیگ شارژ میشه، رباتو داشته باشید تا مطلع بشید</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/120725" target="_blank">📅 01:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftFk48xRUReHEjF0hBIeVNHXnVXHsAVbv2tafd8OUXNOERQrBE3teDcfYAGLpkV-hOgT2a96XUsSFwEOVNE10a8LvoxwmW_7vommlSs_GhidI2jK5Z6Ac6tHYPsGg5nuYyPpA6TuDn-0-SVC76htxDQuCVXw4zLtTFyUrE58lrhVP3guRLi0ShC49dvCCrBIF-X145U_--iokAgtaluSZ7j7mJ-g-mmwrKxEh-HF3os9twkHnOr9LoTsjzXcN7S49sHsofC1kjuuRTqXwXeyUCwrEM1lab6zTA6ROPF7VNykInqqt0WX8Xyz6anIjvJliNDBCwZSIMIqJ_AiaNwcdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست عجیب حسین دهباشی سازنده کلیپ تبلیغاتی حسن روحانی در سال ۱۳۹۶: حملات و ترورهای دشمن تا رهبری حسن روحانی ادامه خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/120724" target="_blank">📅 01:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg8z11rJnmV4NMh5dJZKdTL-zv7O37amvTiHl2Luq6SoQPjnveb87yg14g_eN7qBbSCZ58ThgeNBJN54lw7ezAjM9Mx84IEs_J72HXC5v7QOj65he3wlnFBvRFG5qETpJYfip9GV6DsLX1tS7OKpRA_GNGNqtuuN3tGyKExj-e54PvKqhXmDJozNjHfgxppCOuiv2MusCORIORD_dtk9HinYFhNOG-hqVf2oijSKhZtJUkyvJBAeLEy2xgcjCm5T3UANcwW93oJPI1SWwRlFmnWVEZNQXRRL3A6qEN2ExYJKXy12JpFs5qqiokeehR4GQT-sRRy07iPh7_tk7FOeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت ایران در روز ارتباطات و روابط عمومی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/120723" target="_blank">📅 01:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سفیر ایالات متحده در سازمان ملل: هدف قرار دادن نیروگاه هسته‌ای براکه در امارات متحده عربی، تشدید تنش خطرناک و غیرقابل قبول است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/alonews/120722" target="_blank">📅 01:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9PkTQLtU8BaCkkk3yOUEVVHzrtVH011vxwQAMivAWIe6AqpUEEf_E-yFOV5hzhyOabqytcmbOocWIs9ICBVWv1vUncqi1FTt5_Occk7JWxba5cmb-_w5CgUekykzb39yn9mseo62Vt4BNgpYvut1NjdEFlsb162mVhqFIqywlhYDOjzl78aSn4rK_nBlU2KaGfsUyI5FjqPR5WAoFZ5wG3sswYVL6CAlw8dptNolRKTFwCtypc6FSCf4UDsE7XCqFk8tvjrX4f6nbFDxEqKq3qZgqY14NzJyaBIIw0jOAYU2a9OwvF85ESVByoQ_HbB7upr_lkZSFbzNNu2RBT3gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خوش چشم: قالیباف هَوَل مذاکره نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/120721" target="_blank">📅 01:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/alonews/120720" target="_blank">📅 01:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/120719" target="_blank">📅 01:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFkxezN3rVcXvoee8FtkiS8jT0wfqZfNvJ_iyiO1ox0vEzaSZ-XH77zj1O8aO1lzWvON2sqYZFIHtTjd6YoiG-KHsUrtUR30t0G3YOKKq66Obg0ft-w_4i6hDMENGy8YaovT8wohE3k_eOEd6Umxkk6SJkYy37ZeZUgUaWRxYTKbARqZIX7_IX8YcUl0hbjYbhdqk7FxE0tf0buf9cGT-dkx5pb8HxyVPNS0JnOkg4E9uQuksIKrSHzW_mBsasz_6Xf45W9JYhVp2EU0eAFrIcdtKOO29i2g4Jw-Tl0xqncveXEaYiGyT19FmDXJA54TmvAG9v46RI7TDmshxv6v_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/120718" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtGYQsKeGuVXnW3wlkLDFvBZC-inlq0xx-eKb7fURYEVDvv7vyMVoXPmZnkhEQnrtA-f--4cJ7iGpei4aKiLKpnp3o4Hi5Si5gCh_EWgJgFNUkRkObOd7xHpC7Rj8HmiuoN2PRyEV5ABZbqjhcwGVqBkRDVuTtTnWBesu8FZCPXxRiLBeHI_Kw8anDn50vLCpWgy7FulLz8z5h54YTUFh6MU9mXbW80Y5fbEPgTXUNavyOmKyLwOK3f5hAGINGrkHFOe9E5OVgbViaCv6pTWuGpdNy0grXzUokQrWbGOdNDxNoRKuc1edvTLMDrQnoMaPV4y00PhSqdaonEIZLIQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ دوباره این عکس رو پست کرد
🔴
دموکرات‌ها عاشق فاضلاب هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/alonews/120717" target="_blank">📅 00:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💢
هم اکنون تحرکات شدید ارتش ایالات متحده در منطقه
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/120716" target="_blank">📅 00:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGmnZnIKaKnpBmJ6G0XkcbXeuJxqHS0oA5sKY3V3yjXu1NxYehtrTv6GhzRvr8cSqEA9Z0U6wP1NKgRDcQb85M5UkTOFxc9diyXDZFYBc6QB3MidPYTf4_ln6ZRDLOWaBYqutAvgyAI8Os4HIrCkEDbCcOdQ2acJEmo-85JSPvcfUgXbV4s_QNlOz0Q90gKpPVzDq4gEz83A8WFRHTHAZrtUYnE-ja7dVbsmgG2MBDL7rz-caBPTRJwA_EtZMU7cfwQpekp4-SLXAAFO-P-M_5zM7BoWKHEvG0_gj-x7-8DdFFDLlPFAhXy10jC4v5Mwx62PahPjrodftZ7RzMvMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ به کانال 13 اسرائیل:
فکر کنم ایرانی ها باید از اتفاقاتی که الان داره میفته بترسن
🔴
اونا بايد از من بترسن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/alonews/120715" target="_blank">📅 00:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F400VktaizL1EeNY_ikKwfo5o6rw5AC27RQERDk1xFug9zKVjyLUX1ZJQTEwBSddqTLXXPhwdxaONGioqQDKTUV8wnSM1leCQSZe0UThxtYHVLGPaFNHo6xo0nWhJmxmSERkqlXWTjSR9DOb07qLqXQvWY8ehKTRruSOFE4G8jbVacYJV5nwQySuyW5gc66OFfgmjR4zL5CMgAGVY4zFYulAu0ghNoBWYQsnchVCvODaG7SnBFJ8y81qdYATnpn0v6t5h1V30IoGFM9CEmIhhEnJvEFjcX7Lt5ioUY1g1hx_iYg4D2gp_zVwqvQVjDHVWBcEug_TyorbrytyOO_HxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بازم پست گذاشت
🔴
گفت حکیم جفریز، رهبر دموکرات‌های مجلس عقلش کمه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/alonews/120714" target="_blank">📅 00:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خبرگزاری فارس: در صورت جنگ مجدد آمریکا و اسرائیل شانس پیروزی در مقابل ایران ندارن و دوباره شکست میخورن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/alonews/120713" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtnI2PeG-j-rf27k9ZBynpXPJ930fp874iKmvlR9IBTjWbJdj7tNtEjH-xHLes1JGGAPLJ5J2rGEpat8g152TF8OMJIEsrZJgfr5wl4M6RR2bEpltB8xzT6LTJ4WWG-tr-mV5M1Faa0GU9ghE4SzCZebQ_Bk6T6F_CRFSQNq1YMdQe_jdYHxshQ9-rWZytUUJcOQ1nWoXA5LTSNOLKcpBCWoHZXcG8jzdsj0yLC8TKvqRGkv6ajLU0xUSnL4Fx7G18dzX8ExZKEFwhiOze5_5uKzOYNaQ83-r3d0WvZMdUbnpKuTT4Cc8luOW6rq0gwC6q79G_c-pVaI54Xcj1Vr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نروژ مرفه‌ترین کشور جهان در سال 2026
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/120712" target="_blank">📅 00:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ecfa8c85.mp4?token=vHDaA2APAeB898Uoce3YfWRtU4RlWUn8pPblef5pYs1bahZqCHusQAxpLn6t48F7bTA_lCBtszI3i1O0U6TXnLkEPaE6S3Tv2iwGnAcpp25RddH_sCWFE25FK2pQzRdGznE-i8jyrfrPq3G7_ZZzPvmqIWj5oztMs1ihOW_-RRZWxRCShVxWiE43dm0lBiLo3xr5xDcgwLEcpX1_JGknwNbD8IgmUROIQdPEyB5Mnp1AE9ODO7FzTFKBl7G6u_AGLow0wd4HKvXf9_4OiunexgG4AArW0uo0_oeXZejdTVYM8ll0R1DOM7O19ugptuS1hOe9o2wwfIgeP2n5aOdnBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ecfa8c85.mp4?token=vHDaA2APAeB898Uoce3YfWRtU4RlWUn8pPblef5pYs1bahZqCHusQAxpLn6t48F7bTA_lCBtszI3i1O0U6TXnLkEPaE6S3Tv2iwGnAcpp25RddH_sCWFE25FK2pQzRdGznE-i8jyrfrPq3G7_ZZzPvmqIWj5oztMs1ihOW_-RRZWxRCShVxWiE43dm0lBiLo3xr5xDcgwLEcpX1_JGknwNbD8IgmUROIQdPEyB5Mnp1AE9ODO7FzTFKBl7G6u_AGLow0wd4HKvXf9_4OiunexgG4AArW0uo0_oeXZejdTVYM8ll0R1DOM7O19ugptuS1hOe9o2wwfIgeP2n5aOdnBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بیشرفی خاصی می‌خواد به مردمی که اینجوری با دستای خالی جلوی رگبار گلوله وایسادن و 40هزار نفر در کمتر از ۴۸ساعت کشته دادن، حرف از بیضه بزنی که طبق معمول فقط از یک چپی برمیاد
🤔
حسابتون بمونه با همین مردم فردای آزادی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/120711" target="_blank">📅 00:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120703">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0ixMNDOWubmvPdPHcEjdgUam3FPPQgsmL1ztyB0AnOBfU6vtGJ0O9oINq0XynRr__2BszxcXHI38jcclNuSn6QDHPyHNqtT09aJq4Pf-e0e_0rTAoMuGS48fK8nnIz_kMImNKTDF-msdEF6-N2Q09wH9bxfPbnJTd36xvRvJVAADoLS8hTsE7-vZ8XAvUE6fv2kOVWrAzdWpNGf_TMiMtFEBfBmnZzZoFu3RU-ZcaZL4-MvEsVcdDC5v1lIpQFDxk1HpuwuZ9jRla1BkPtrM6vb3n0bAhIB3I61ls2puEvh75oJA3xGJwZFczOFhRKAm7ENJSG7YJYzpRZ5H1cLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NG13vRr4hA3B8ceLnMfZiMGPC3WbfzEqOWHuXz7xAhEVwRoMGLUjRWKcNLlW0Qw7w1kI93Rg2P6XqK0wC8_uET5Kcka6Q15Cn1ouAF1G9oYfzOoA82jxwRx8ad4Xxo5lKh-hk3Wa9Hz-XzaBOXOa1Ude9rRana6wuLZweJXEOJIvI4mN4CY7FWoWMgFVr4i9U8R_GtYz2Qg6WtCJHRcOquNXyNQ2pM2MynrC-q8ufr9slKhZeGn8JtDusHB5HjK6IfvL8P8ubFK1BhHh4TEeya2rH3uVgi4OmUhE0Uw1cp-B87wOwSMrZIWk-1od5SKxWLNYJBf-X9716rd80eJhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ErM2QrmvJ6_4c7Qak-O5meWpNA0LGazBP9Q6W471j-utY4YK5tXOZLMG14aRVmDVgBtTVr-xugMMTJtdl_JFKC2qOwF0H1-v7x70o64WMJuzmm4liQCNH2Gog5MqthosdFgUulZXF8mkh48Y_3WAddyUbrbxP_LgoxFVfUOkQBDDyZRSPeQpmLvOeg35aF8H17Zj5QwDdOQBNBVVcx2Msm8yY31EdpHlc0LEisyj3MxnKbXDgsz2CqneCh1EYSe3PzuaMsgIMHK1jrFOKd0syuMMP46XmDScFXctDJWgrLz07rIA8LQkCcpDYSSvNyGkaGI9h-J40qCoDGZnkeb3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Czs2Y1s1iRaLW8kqG_myNzpF37a6WVAlRVkgwZUSwjgBDj9Pht8Ti59SJmqj9ymAN1U4HOZVM07WyMPdTvGjVFTa5spr7TJ4qcFxlbxpwtmxJTZzZZAnmYD5484puWoP0XEncp74QRUGB6Mmt1_3XsvZ8gbzcPqFS6tp4WUW-xSDbCnA5rMRRWb7-RZrvS4EMHUEbA_VIf_GR4uOlWmxLvdN_JKkaqq91fxDshadUlR0lk7e9DULYSkcFA48L3ED_S1FzHfKMLcIAVhVFr0Sr0ZjUuevgqA83PeFu3S0eknPuO5ZTa7sZrhi8iyB8Q6oqHQfujVfkvoUKzuojoA4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTWnIcqb7KhV5sEzt1nHKT1PvgCT2DUJlfVioAaQ9XqQrJ-3eMRw2k6nFiqf1U4JmNwSPb7-7z2F5WGc3HaG07o47pdlpdHLN5Ue3CNsvbQVAaElo1t47FctDck7k3nORuu-lvO-oG8KO7fsnJH7KcGW7aXMxstt6-r1xlOWljMrRzjeZVqLUAquFO5hOgeRZAwmevdYo5-B98UulH_i2b01gTSnZUfhW2deNQK8b4D12GbbYFWy_jg20jx9s4wkVFnkxtumClw_YDGg93b2zZ7HWaJbhcQnMctsPWAjbJNM0MweXfMyMmyz9_d2rzZpmB8SmF8OtFGCvha0MbDvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exFkGQwIjR-V5L69A07-LI4eh6k6Hmp7O_jibn27tll7CWXFHnwH5Kt5vK3wG33b5k0gnmqldSfO4cxxf2KH_Bziu7tkGSV0xSq_b--G2ZUI80iwVNgOVqnmMTpJ35pBB3qu48fSW3LHl1x-qCYb2WfVAAM7twcg0xDHamPcF771R3ISvkErMXskcCjuK2N_ZT7JdSbNy2tARBPA_I9lCC7ULotGvVohHRLoHmeM944c84I6CReyWH26DAVdxaBHpEOCAY1KgK3q9OmPxnkCUVkf9IVbMaH3f-8wwoLuGYm5Xg4GVbNP1plJGA9xpwR0l70AkdAJGpg_hASWcReHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wh8YSAeX0V3hufAXpf9_k0bvlGcjCeRJ_lCfhCVdFJ3WwskomhrWqy_kBVebnl5jumxzsFyvGwv4vXfF529KzrnnTOTH33f0tPtXeYxyAkJsQPvVybBUDXORGuM-0I1rkBbpn4ZLNXWOrkGYiDZ78WJQlV3Og52zovFfkilhnKZYPpPkrLBWVzXW4nkOIkUITWWZoWWGWrbe6AAQgR9pvc8v33oyEvzVI1z7ONokKQTaKVE2OMV2LYK4Ge2NI0XfA1Yh4khNxZGNhhBjHJ7bSOK16X-J9ClOpRaqSsnPnZINOQbxL1hR3y_dAwHrDBzm_3YgkWeiRtMHccseV3bmsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QlLr79L5Tbt8F23CjRC5uaAvkKq_n4TiRWMAKLTOB1SIXyDbljPS2XU2zGio4oOkODhmANqBqtATcZPdflpNe_0F6AazGbf30KfrFMSkOfEFkxwqg-2gr6kSNrXRznQu4WMLsT_Rf64gaHjGaEdHSRj2cRD0bVGy60-74tezJZe5R9mId1ug6spS8n-FXIGzOQUg0UM1DxgeFCcfBVdRYWft-4fPicJalQuygSV30GR4sfrWNryzNeHAhlPwj-br-pbxnAGz8viUV0tJAZdT-qCVU_oar-DqNxDSsUC-Zy1rX3pkTIVUgiRfd_p7nuV87aSWkwIAO2vnVWZN8qIwXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ یهو ۸تا پست گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/alonews/120703" target="_blank">📅 00:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120702">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDD_LTo3mXoQwZYEQX4rd6-2353R4VbEzj0t41Fc8_zNJIyDFponwvym9R0iQNH-wfvK5vYPvbrGtnguASR5oqjtVtOpsNcTxX-9J9-NemWuu_1gO_8UW-yYX_B27EvcmsH4NKedlooe59Wl7_jWs1Te8BbH6RW6nRC6v6F83rTD8X7fDwUFBMQmoUoO7lTJzlGlYbLkgsx3NdlxO8cp8CKC1tY9118LHOqBqlZdn4HmPu9bI_tUlX5_EbVxZGRGrc-OLI7cfhSmUDeC52grLTTy21QjIi_pDo41Y2vDoMrPmAawSjqG3mwMQca2lfm6z-DO_wxa07xFABhmm9gnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی
:
اون دسته از مسئولینی که دلسوز کشور هستن در معرض ترور قرار دارن و نباید از موبایل استفاده کنن
🔴
مجری
:
پس چرا شما از موبایل استفاده میکنید؟
🔴
رسایی
:
😐
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/120702" target="_blank">📅 00:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120701">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سی‌ان‌ان: ترامپ به طور فزاینده‌ای نسبت به نحوه مدیریت مذاکرات دیپلماتیک از سوی تهران بی‌صبر شده و همچنان از تداوم بسته بودن تنگه هرمز و تأثیر آن بر قیمت جهانی نفت کلافه است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/120701" target="_blank">📅 00:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120700">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سی‌ان‌ان: منبعی آگاه گفت که دونالد ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
🔴
این جلسه یک روز قبل از آن برگزار شد که ترامپ ادعا کرد تهران «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/120700" target="_blank">📅 00:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120699">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBfjxzb6ChEu-j2c7NtDY8LPQRSJXPqDtwqx1IL7N5NLH8tFfMQvRfGCfUd7LIn2z5ldv5JVNTV1ceJ4p-GpiH1iDY5ti668QJeJH-Fz2fNzKzcfpFL5GT4IDoYfNs1rSytXX8aJXLDfp1iLHC-ya_lusnzheVvgB0m2bQ9RJiw0ggh26NFmyyh9ZJieBPWG0MzQiKuBa13QPSovQzozxGPnHiPfUX4-J9xv2_bl5JL3nfBNVGLs5De0r4-BT8oLphzwRwy_iakBNCF1oiUyhU2bF5zPwfD1v5VohbUEqE_l9wK-63Lx6FbwkhNxXziz-Xi8CkKnkGvnBJtkwHFxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سی‌ان‌ان: منبعی آگاه گفت که دونالد ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
🔴
این جلسه یک روز قبل از آن برگزار شد که ترامپ ادعا کرد تهران «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
🔴
به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
🔴
این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/120699" target="_blank">📅 00:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120697">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jIBDObc7xJH0XD35_uIxP_YZaC7yP--LlhksFHYfqHwHV0qn3WjWVaEas8VAvuf1kpq8pMWtlt2j8DHFdch_rCRdvMtOSWS4gXmLEtXaCwJ1pE3xwYA06Lnu96kKSJgX3grRl0jQTVkG2qDnDtk1C7JDVaU7r3277qwiozUaT5-KsFyT7_6QB8bilsc3cl2XNyeH6J4VEs8jpzOade5Qph_sgUjEItqFUp9BW5mXt2SdqzTUxgRKsfLi5VYoP50nEm2bfRLzLdNVpfNWXw_OoONiUQvlBRHkHa7CTos4uCnRsVh2KmcrchTME2dx79-LJL1uZvo8ulduln_UwCdHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33b6744dc9.mp4?token=BZhqecfTcR2XuxbRxCRAytB6v2bNpN7cAD5LsyO_BFBysvGQjBXxcdKkXcAHo8XcFwgX3NV4yr6jcfxiHl5Ov6c4rSgNJGSPu49eIxagTVNAGWL8t6TMj1ZNbTcPnJmBNV0HLzv67lrKU7-bNvtZXnzfDV3KbiWmGKY0TbecdDjpbjedZyA_qmAo_o64-vr9ig9t5dtv9SYdXtud0Wpt7btHvDwtRDEIHpcgTdvjO-aANRY7K09hN6LuJdj4pfPAshfytjv-v-yzs6kTB6v-9YW_PnKJZ-B-cZN7kpINRuiHa5JBGX2MlueTdq-p54IY7gkox3mbRycPXAex8ykSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33b6744dc9.mp4?token=BZhqecfTcR2XuxbRxCRAytB6v2bNpN7cAD5LsyO_BFBysvGQjBXxcdKkXcAHo8XcFwgX3NV4yr6jcfxiHl5Ov6c4rSgNJGSPu49eIxagTVNAGWL8t6TMj1ZNbTcPnJmBNV0HLzv67lrKU7-bNvtZXnzfDV3KbiWmGKY0TbecdDjpbjedZyA_qmAo_o64-vr9ig9t5dtv9SYdXtud0Wpt7btHvDwtRDEIHpcgTdvjO-aANRY7K09hN6LuJdj4pfPAshfytjv-v-yzs6kTB6v-9YW_PnKJZ-B-cZN7kpINRuiHa5JBGX2MlueTdq-p54IY7gkox3mbRycPXAex8ykSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ و نتانیاهو ترور شدن
‼️
🔴
امشب تو پخش زنده شبکه افق، نتانیاهو و ترامپ توسط صدا و سیما ترور شدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/120697" target="_blank">📅 00:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120696">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d3cdf36e2.mp4?token=fXh0yeAbjxPxvBZc1e0BXseTpVimhbg8PK4t9u-5m-nv7CvkI8uEO2FJs9cjmKjDeExEOUTskz9NRUueako8yvhFaG8Q1lStvXcV5oXVp_UMQttc2txblEIAhgzalhm0BD1jjTMpZhHSV1v-bUD6kMD0IhTC19I7tJOYm-B7vFx9shFbZ8_PywNCLbYi-aAkSWk0_GOBZnAAXrXJPvxnkkZXpaCxeqeKFSlJFWupo09djQpxC8jTD1Dp08UhdFfIXLN6wUZLYxSEzNQs6aw7dihi_mw6H3TfjKbpRE8NEhbgnfhCD9gMcu21XiDpZ-uNvEunlP4xu8h4CHXU5cHPTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d3cdf36e2.mp4?token=fXh0yeAbjxPxvBZc1e0BXseTpVimhbg8PK4t9u-5m-nv7CvkI8uEO2FJs9cjmKjDeExEOUTskz9NRUueako8yvhFaG8Q1lStvXcV5oXVp_UMQttc2txblEIAhgzalhm0BD1jjTMpZhHSV1v-bUD6kMD0IhTC19I7tJOYm-B7vFx9shFbZ8_PywNCLbYi-aAkSWk0_GOBZnAAXrXJPvxnkkZXpaCxeqeKFSlJFWupo09djQpxC8jTD1Dp08UhdFfIXLN6wUZLYxSEzNQs6aw7dihi_mw6H3TfjKbpRE8NEhbgnfhCD9gMcu21XiDpZ-uNvEunlP4xu8h4CHXU5cHPTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
علیه فراموشی: نیزارهای ماهشهر، در 25 آبان 98، 500 نفر توسط، عوامل سرکوب جمهوری اسلامی قتل عام شدند.
🤔
جوان مملکت جونش رو جلوی دوشکا گذاشته، بعد بهزاد فراهانی (پدر گلشیفته فراهانی) که با دیدگاه چپی داره، میگه ما بیضه اش رو داشتیم شاه رو سرنگون کردیم، شما هم اگه دارین انجام بدین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/120696" target="_blank">📅 00:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120695">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf54c97bb9.mp4?token=FRsrX1vffD4qkc_zvNhTabuks4w1f_BtFWVoDYvt2jvsabHsBwM3cGOwBm3Za8lUMZZCd1iwioM-3YGTL0A7ImlgwwxnXHyFf-E20oLpcZk0bGjstv04xAVJ-QUyvmKUxbY4VBVPLAfrbnVowGiCB3zkCERA1mRGtxJCuWytnM584WqmFW-hpqN2I6mB52hb5tH_WfOgqk2uy7usnKWTQMJXVgdsSXIcyAKgiR5tY03pHjrGEMg6K4C_9er6Dp1vIBHVdmZ1qBXI5woJv-4pVTEl5fg96e87pQ3KBZbvmGDaY36TYyKseKdQ9qd0oNThp3ozkwM_6hzNB32_tinxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf54c97bb9.mp4?token=FRsrX1vffD4qkc_zvNhTabuks4w1f_BtFWVoDYvt2jvsabHsBwM3cGOwBm3Za8lUMZZCd1iwioM-3YGTL0A7ImlgwwxnXHyFf-E20oLpcZk0bGjstv04xAVJ-QUyvmKUxbY4VBVPLAfrbnVowGiCB3zkCERA1mRGtxJCuWytnM584WqmFW-hpqN2I6mB52hb5tH_WfOgqk2uy7usnKWTQMJXVgdsSXIcyAKgiR5tY03pHjrGEMg6K4C_9er6Dp1vIBHVdmZ1qBXI5woJv-4pVTEl5fg96e87pQ3KBZbvmGDaY36TYyKseKdQ9qd0oNThp3ozkwM_6hzNB32_tinxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رضا پهلوی در مورد مشروعیت خود:
این برای هیچ دولت خارجی نیست که تعیین کند چه کسی باید جایگزین باشد.
🔴
باید مردم ایران تصمیم بگیرند‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/120695" target="_blank">📅 00:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120694">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
رضا پهلوی: در ده سال اول حکومت من در ایران آزاد؛ بیش از یک تریلیون دلار منفعت اقتصادی به آمریکا می رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/120694" target="_blank">📅 00:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120693">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مارکو روبیو، وزیرخارجه امریکا: دلیل توقف «پروژه آزادی»، این بود که پاکستان چنین درخواستی کرد. پاکستانی‌ها گفتند: «اگر شما پروژه آزادی را متوقف کنید، فکر می‌کنیم بتوانیم به یک توافق برسیم.»
🔴
ما موافقت کردیم و آن را متوقف کردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/120693" target="_blank">📅 00:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120692">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
هم اکنون گزارش CNN:
ترامپ تیم امنیت ملی ارشد خود را برای بحث در مورد ایران فراخواند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/120692" target="_blank">📅 00:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120691">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=iFwCJN41HeQSR-r01whZdU62zEZPtZY_Z6qvtbz32hcsRRGQ5jMq7jpptiu5DxOp8BdiaEO6ns6JmxDo0dEHzIwbL0bGAR2hB0ANUfdUNaMANqxNdfNs-wAMv56Tc7UfOEHw7cYa5epnGdIblVjT6VbB3jiJzztII4VIBwdIoJDGlhj8Mz47mo6o3LSTFTFr7lj6n-hrNhG2tB3buBPBN_UNG9z95wSISbZCd7i7-rI1tnjIhFg6V3iM3oecwXhU4jOPFn3AF0QPqzLQDvH8wDwH2_tXdS1iuff4HrejKepMWMHLU2AziKkAF7aCCelDO3-dVId9F2wwjLtAthCEaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=iFwCJN41HeQSR-r01whZdU62zEZPtZY_Z6qvtbz32hcsRRGQ5jMq7jpptiu5DxOp8BdiaEO6ns6JmxDo0dEHzIwbL0bGAR2hB0ANUfdUNaMANqxNdfNs-wAMv56Tc7UfOEHw7cYa5epnGdIblVjT6VbB3jiJzztII4VIBwdIoJDGlhj8Mz47mo6o3LSTFTFr7lj6n-hrNhG2tB3buBPBN_UNG9z95wSISbZCd7i7-rI1tnjIhFg6V3iM3oecwXhU4jOPFn3AF0QPqzLQDvH8wDwH2_tXdS1iuff4HrejKepMWMHLU2AziKkAF7aCCelDO3-dVId9F2wwjLtAthCEaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/120691" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120690">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8E5mTVgY3QQq6Vt6MOUaxp0axq9_IduPkxYyRH06Nw11Sz9pgU89ZiH_AJN8SLnCsUOg8WTJZvM8byYFDrZXXrmX7VY6RxD88p4FJe94ePbDBdLMoEqFgUxifUvWXaalvht-D1YvqnwtkvKobA5-Lq6RXBHI65Hv6MltjymeN_dKTKFYDiECKY38tuF_Deolddp08iSffp_sRq8a9Gr1qKpxZQ9CkNX77z_O0ypR92noysK8rBYDK4VlWzPCV64Gj0dULsNnSstfyO7zqifVMdJbiY2wA7aqP06Imo73bt2hDMF2MkiaDywhlpVlCgbKP0Vaoj-UDP-nqZiDWu_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سنتکام، «تیموثی هوکینز» به العربیه : ایران موشک‌هاشو از مناطق شلوغ و پرجمعیت شلیک کرده بود
- ما خیلی دقیق حواسمون به هر چیزی که ایرانی‌ها دارن وارد یا خارج می‌کنن هست
- توان موشکی و پهپادی ایران خیلی شدید کم شده
- توان تولید تسلیحات ایران رو هم نابود کردیم
ما تو زمان آتش‌بس با ایران دوباره مسلح شدیم و نیروهامون رو جابه‌جا و مستقر کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/120690" target="_blank">📅 23:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120689">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/120689" target="_blank">📅 23:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120688">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0SEC5pdgZP8D-rMJ5ieJXWwEtCMBtCv07r1l5l-yHyJfVoPZiY0uLOc9aTmKVTgsm8kvUIiBMv_d7t5rIl2o52qLOWged2KDIEUPUpSYaDKkg30lT6eP9NxqCzQl8bqLGJDR4z-83H4zi0FxYb4J4faGba5KuvMrIPwqtb5WfkZV8CZDCHjUhgMuh10NEtX2-yxsRSNUcj3Ze6dkDE5lyIHNX_N5ZoaxjTFTr7qwxyDU5xRqdqcszzAAN0RSb2kJworfxCHP15HBjNRN1WJeHvVY9NcKrSGuRHu7ziH2K3Z1xXZYJp20Wawpo6HmmUnB_sLh0jyRSOVsSDIXCoQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ترامپ لحظه شلیک مجری صداسیما به پرچم امارات را منتشر کرد و گفت خواهیم دید چه خواهد شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/120688" target="_blank">📅 23:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120687">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزرای خارجه ایران و فرانسه در خصوص موضوعات دوجانبه، آخرین تحولات منطقه‌ای و روندهای جاری دیپلماتیک رایزنی و تبادل نظر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/120687" target="_blank">📅 23:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120686">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2yCBSwTvjN6oQ3Tt7CmN1fDCYf8x_y84jBm9WzjKqTZGpNWbnfB9hU7L6kmA7nI4WDbYn3ga3GKZ6F6JERhH8gd-e_i5pQU4iMhN0mxJT6eAtePp2PDckKuRUMNsDSSfAIfn9KRfg_1QE6FF5h-KpC4gbKms_z-SfJtWY0ptsKqPmP1h6DUN8fFxeWQl-v8iQEAtpprPT3oa8cXs4ffq5lP7EYX5o692MgwokBmRTKa5dNtGJZmXNpoPiU3se3kpgoHFBZVupKoT9zzMvvCpu2Q3bgTGvHHYIOMFBhjKLgT3-_fCYuDawQ8uwvRh7RJkYK2QceGqubkEMLeW3apfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیلد مارشال: محاصره دریایی رو میشکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/120686" target="_blank">📅 23:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120685">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی وزارت دفاع عربستان: رهگیری ۳ فروند پهپاد که از حریم هوایی عراق آمده بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/120685" target="_blank">📅 23:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120684">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9guFapxHwbaIFZMg4McNz5jcyN3_fqlOVZa5-D5DAJdlIL1re1D_3V1BGy4S3I2x_Y5bfTjxp1uw6TETLibiN8XLnCidDJ0JzqB_VgALuzMovk5No_QG7FKCaygmVLr-4tjd1MvJdDssKuLIEhWY0N4UoEAH-aSlTItKpdPLXaoGrI5hqf-4tUNu3J7qxBlegCyTClpNm_NEOJkKxRfVXQl9HoHu_7NuT7iT-rb8eMzbpR8mI7U6yRf189q0yAZaCNB4Fx6FLnbq3K9BwR8TdBRtKY2MMMX-pfDIBSeqCmKxwbj9UfmXKppp6_-Bc_zT0ZH-i0rqHmuUhcMTo6IGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/120684" target="_blank">📅 23:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120683">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل: به ارتش دستور دادم برای اجرای قانون اعدام تلاش کنن؛ دیگه اونایی که یهودی‌ها رو میکشن قرار نیست تو زندان‌ها راحت بمونن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/120683" target="_blank">📅 23:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120682">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
از دقایقی قبل بنابر گزارشات تایید نشده؛ صدای فعالیت پدافند در اهواز شنیده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/120682" target="_blank">📅 23:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120681">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02686941d8.mp4?token=KrwnytLAfKGBuxYHVfSww-ayFXWxG7n9VA56O7mhl55nqBAcQ2waM-qFgLHNaNVq35XmqxFgitinl2R4ITtuWVIbHKBV43bthf3-f5jkKSHlgGI9i9O5WaoI4OOkhI5WWqJGg-ktR2UWUGyqK3ai0-EjRgTjKq4xu3qrEdZ_2wITK3O-S_ZWYlXmhWmsoSmufgm0Ljo_XpL4P7kJlSgknPvhNiGWF-nPxxyDVrNmhGi5KHjLYj5HK_bltrzhi2aGxctR1CrX8Qhx1jNdgOdiu9Xem7pndpMaa-1GUWBdEW_ysQnL3m-O-abQ4u0ccBKWLAfXYSLmMIaBuMR-kmwt-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02686941d8.mp4?token=KrwnytLAfKGBuxYHVfSww-ayFXWxG7n9VA56O7mhl55nqBAcQ2waM-qFgLHNaNVq35XmqxFgitinl2R4ITtuWVIbHKBV43bthf3-f5jkKSHlgGI9i9O5WaoI4OOkhI5WWqJGg-ktR2UWUGyqK3ai0-EjRgTjKq4xu3qrEdZ_2wITK3O-S_ZWYlXmhWmsoSmufgm0Ljo_XpL4P7kJlSgknPvhNiGWF-nPxxyDVrNmhGi5KHjLYj5HK_bltrzhi2aGxctR1CrX8Qhx1jNdgOdiu9Xem7pndpMaa-1GUWBdEW_ysQnL3m-O-abQ4u0ccBKWLAfXYSLmMIaBuMR-kmwt-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی، سخنگوی وزارت خارجه ایران، کلیپی از فیلم The Apprentice محصول ۲۰۲۴ را منتشر کرد که بر اساس زندگی دونالد ترامپ، رئیس‌جمهور آمریکا ساخته شده است.
🔴
در این کلیپ، روی کوهن، وکیل دادگستری، به ترامپ جوان می‌گوید: «مهم نیست چقدر کتک خورده‌ای، ادعای پیروزی کن و هرگز شکست را نپذیر. می‌خواهی برنده شوی؟ این همان راه پیروزی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/120681" target="_blank">📅 23:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-120680">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51979debc7.mp4?token=HAAHMzV99WOgvnjEiU2_InjL3spZVYcIoDt3YQEUQmY8l6EJLomNPaw54hLsxBC9Pz4rmwibvRMEZ63d4i7Q4aN4_OoJdJIsEykSQ8jY6kLI8_ojpMN2UToguQBwNeuVKn2TT3b4GTlV975wv-edEkpIZjSpOyJiCnM_Jev9z1Gyz3uJmUZ_iDMH4gQ956H4Llj3cJmIsbf7j3L4oWzRO4BsBYQNl3RAFe5HLyTVjeVKcShTSTEI2eaMxY048NyE85k9b4hxKhEz224sKFCh-QbZIgZGfBbpwJ9gGL7HLaWq-4rmCM3rYk0hTILuWLxEDy8yAWk6SMitvmJ8DabIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51979debc7.mp4?token=HAAHMzV99WOgvnjEiU2_InjL3spZVYcIoDt3YQEUQmY8l6EJLomNPaw54hLsxBC9Pz4rmwibvRMEZ63d4i7Q4aN4_OoJdJIsEykSQ8jY6kLI8_ojpMN2UToguQBwNeuVKn2TT3b4GTlV975wv-edEkpIZjSpOyJiCnM_Jev9z1Gyz3uJmUZ_iDMH4gQ956H4Llj3cJmIsbf7j3L4oWzRO4BsBYQNl3RAFe5HLyTVjeVKcShTSTEI2eaMxY048NyE85k9b4hxKhEz224sKFCh-QbZIgZGfBbpwJ9gGL7HLaWq-4rmCM3rYk0hTILuWLxEDy8yAWk6SMitvmJ8DabIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت، رسانه ترک: برخورد دو جنگنده آمریکایی به یکدیگر
🔴
دو جنگنده اف/ای ۱۸ نیروی دریایی ایالات متحده در جریان یک نمایش هوایی در ایالت آیداهو، در هوا با یکدیگر برخورد کردند.
🔴
هر چهار خلبان موفق به خروج اضطراری شدند، اما هر دو جنگنده سقوط کرده و منفجر شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/120680" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
