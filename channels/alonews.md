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
<img src="https://cdn4.telesco.pe/file/SCNDJvpLe9ryw6ZYHRC0G8-arji2s-I_48XobwpVxRZzDzjW8RmIIHtsYH1CozwxvER-GNVtP5C9uUO4JUBoomHneXtD7ilh-UTw0nxwpXnav-YBn7xTtwxzCrbLAF8n_8FfDMhjrz7XmGGosLG8Z41KV4iEwIEhOd7zpb7SVlUxYZyCKJmhq2AhzW2go2Wc0Bhr1RieNNz24xL60wrxl8tjiq9BITvcpyJQQAjBsou88LF0ktPzN9k15lBtOxfCYNW65W7KqNSfI2m9F4j307IsOuId6p7r7celpO3Q1NPzbqrp6816p3jzWKUcR6aRkoMF8Opk_q7hdEhIWxeoqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 14:34:53</div>
<hr>

<div class="tg-post" id="msg-135616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
عراقچی: وظیفه تحلیل جنگ یا آتش بس بر عهده شورای عالی امنیت ملی است اما تصمیم گیری نهایی را سید مجتبی خامنه‌ای انجام می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/135616" target="_blank">📅 14:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cac25a379.mp4?token=n3eEf5XrO9O3l5T7rc1C6-RctqirHcX_vxlkdpsL3wHJWKn6iPSyiq5HlD5gqSvxyLNQz7-5ILgYpU4fTdOm4xLCXBOKq5WKjF8XkHE6x-XFm-TnH-Fjtlse4a8X1GnONCMG8TrCY19h_rrEPFpNW44EeK64JG3jzo5SoykvJZglObROLbK3VAIpG9WnrkTK8_LmhSnjft2pwyPZw5clk8aIftQPnqKEHrB-rswpZYQR28HPSbw4HQDn9eOO1aiMvlTVDDtARg1SD8KLsr6cCHlF-d6NLWrDkFgXVeXGPiloGtoy2siuuztbNEZ3xli51cVBzp10hralQkDccEQ8Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cac25a379.mp4?token=n3eEf5XrO9O3l5T7rc1C6-RctqirHcX_vxlkdpsL3wHJWKn6iPSyiq5HlD5gqSvxyLNQz7-5ILgYpU4fTdOm4xLCXBOKq5WKjF8XkHE6x-XFm-TnH-Fjtlse4a8X1GnONCMG8TrCY19h_rrEPFpNW44EeK64JG3jzo5SoykvJZglObROLbK3VAIpG9WnrkTK8_LmhSnjft2pwyPZw5clk8aIftQPnqKEHrB-rswpZYQR28HPSbw4HQDn9eOO1aiMvlTVDDtARg1SD8KLsr6cCHlF-d6NLWrDkFgXVeXGPiloGtoy2siuuztbNEZ3xli51cVBzp10hralQkDccEQ8Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شاهکار رو از بیرانوند ببینین
بعد متن اون استوری که در مورد اسطوره فوتبال ایران علی آقا دایی ،گذاشته رو دوباره بخونین
خودتون حساب کار دستتون میاد که چه آدم دوزاری هستش.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/135615" target="_blank">📅 14:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سفارت آمریکا در اردن: مقامات پادشاهی اردن، فرودگاه بین‌المللی و بندر دریایی عقبه را به دلیل یک تهدید مشخص و معتبر تخلیه کرده‌اند.
🔴
ما به شدت به همه شهروندان آمریکایی توصیه می‌کنیم که از سفر به فرودگاه یا بندر دریایی خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/135614" target="_blank">📅 14:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135613">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVlIfWLDgg_ZfFim1h2qf3AjHhMYu7NrG-51r6J9RSwS7pkcVO9rehH4A9N8D1IcmVZXVC8njWZH1LzzfwCuptMZ3f3e-URGDZVbv-N8VXKZHieLOcRvIhPY0fjFW9P9YNl8zh1_-be77Z82DvRcm2A8NNME3EP6Dj2r-bH0PVPLuEXYH09hRkgbo2y1D4ja4xmZwrHxR7_Pe8VQa_lKBoBWpmm0tJPICbphO8hxieHWJRyuzx-rnUuT9dQCi03QXteakauItg0eZF19FqCTwYNKSlt20a5FkZmal2Fg4WawYuFd35jsmcOV-n8rYkx5BF9Fq4gPZZa793ecjtoUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل، با توجه به برنامه‌ریزی برای یک راهپیمایی شهرک‌نشینان به سمت غزه، منطقه نظامی "نِقاب غربی" را به عنوان منطقه ممنوعه اعلام کرده است. این ممنوعیت از ساعت 8:00 امروز، 19 جولای، تا ساعت 8:00 فردا، 20 جولای، اعمال خواهد شد.
🔴
این محدودیت در حالی اعمال می‌شود که برگزارکنندگان "راهپیمایی به سمت غزه" اعلام کرده‌اند: "شهرک‌سازی، امنیت است؛ شهرک‌سازی، پیروزی است."
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/135613" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135612">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF9XjPrej1aeYxrgiBhf-_YohuBvjoG67d8G6_Itxk3vhnNaXPNThsLt1ZdYsgxO3N6OPSgdFvp2EFYLE2ZLHGblANMJWTBKEEfk4uMJ97jIqJ2hSiJ85FDwTTKOWPZeyh6RgApjE-HJP-2X1bRC2PST38WEQpdAWa2EmIztqxn38NELBksey6AzLpxNRyVioBFtYgqAYN4CLz1RF9cQeIkOzn4d4qGuKaUYKCCQOWnF4PkSzJz54qgqSbWLlejR6Ejj7F9cHnmsvyErobkzo86kqsoiFBvcAQ0DW3hjIMaEfZxRuTbzEXz0ujXNzwOPeDrFeuCWZ54S7devllr_jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید ماهواره‌ای با وضوح بالا نشان می‌دهند که یک بمب‌افکن استراتژیک Tu-95MS متعلق به روسیه در پایگاه هوایی انگلس-2 در نتیجه حمله پهپادی اوکراین در تاریخ ۱۶ جولای، که پیش از این توسط رئیس‌جمهور زلنسکی اعلام شده بود، منهدم شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/135612" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135611">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7Vy6KWPb5ps90qZZKwcUSXXKQf327jxFyCx3jlxMIpHyusb7lLEA2PVQ834zoGnNx8GVQYQ6oBYvAVPtvqeHgIo0bQHH4TAmyaoPDshC2u9dzlC8Dv9rZ_fR787VIanqlAqIy3CnzL3fm8U0_6mO-jSKGFIPm_4JLmvNdCJPdFk9p3JNsjrv40n7a71I-v4nHbumSe7Ddb7s0dFTTgnpWcO3jaSnzcSMTPz9gMLpT1S07Av3d300hVtQys1Wuck-Xy-DMV9J-Mg0dSjTNHC8yDVcqknVPggZkBelwlVy8rlLEMLoXZktd9h6M4EksV8aS5AjRl4BhO5daeotTSxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش خبرگزاری رسمی سوریه (سانا)، نیروهای اسرائیلی با استفاده از پنج خودروی نظامی وارد روستای "ال-سمدانیه الشارقیه" در استان "قنیطره" واقع در جنوب سوریه شدند، یک ایستگاه بازرسی موقت ایجاد کردند و به بازرسی افراد غیرنظامی پرداختند.
🔴
به طور جداگانه، نیروهای اسرائیلی که در نزدیکی منطقه "الحمیدیه" مستقر هستند، یک گلوله خمپاره و یک نارنجک دودزا به سمت منطقه‌ای بین "الحمیدیه" و "السلام" شلیک کردند، اما این اقدام هیچ تلفاتی نداشت.
🔴
سوریه این عملیات‌ها را محکوم کرد و خواستار عقب‌نشینی کامل نیروهای اسرائیلی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/135611" target="_blank">📅 14:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
دلار هم اکنون 193,150 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/135610" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عراقچی: از روز اول تصمیم بر این بود که اگر رهبری مورد هدف قرار گرفت، تنگه هرمز بسته شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/135609" target="_blank">📅 14:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951d681504.mp4?token=JxFg2-HRwecz8WmB-lVqyC_ykgp00M-vFGd-kaeIZ9sSsl7yeygwLr38IaYOtGDwMWgs_BaD7M8QJftFB_ez9O8Ckkep65hI8MN9-Wo2WUycsoVVo8dt3YMjcP5di0lwRT0SOcuzpVu3d1evPLtCky4up2JyNFlnDrDTwmEHsZM1GHg_K4svOCUtng0rSe4L4RqRbO9ZAhpDf9Y2xCpwYxEheVkNE-AzTB5TuaU0OV1hwuTS-_0lB2hzAvT_cPFamGW5LMKrdTJg46ZVAfifWuW2eWXNqbUHWtQtjZayYVqpRw63vQ7NWaj50xHkH9VCecA28pLfWGuLXNr40OM6aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951d681504.mp4?token=JxFg2-HRwecz8WmB-lVqyC_ykgp00M-vFGd-kaeIZ9sSsl7yeygwLr38IaYOtGDwMWgs_BaD7M8QJftFB_ez9O8Ckkep65hI8MN9-Wo2WUycsoVVo8dt3YMjcP5di0lwRT0SOcuzpVu3d1evPLtCky4up2JyNFlnDrDTwmEHsZM1GHg_K4svOCUtng0rSe4L4RqRbO9ZAhpDf9Y2xCpwYxEheVkNE-AzTB5TuaU0OV1hwuTS-_0lB2hzAvT_cPFamGW5LMKrdTJg46ZVAfifWuW2eWXNqbUHWtQtjZayYVqpRw63vQ7NWaj50xHkH9VCecA28pLfWGuLXNr40OM6aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
همه اون مسؤلینی که میگفتن به ایران حمله نمیشه الان باید باشن و بیان جواب بدن که چی شد؟
🔴
چی شد که آینده یه ملت رو از بین بردین؟
🔴
حاجی زاده و سلامی مگه نبودن میگفتن اگه جنگنده ای بیاد به ایران حمله کنه موقع برگشت دیگه اسرائیلی وجود نداره که فرود بیاد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/135608" target="_blank">📅 14:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سازمان انرژی اتمی حمله آمریکا به نیروگاه هسته‌ای دارخوین را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/135607" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX-y-eeC5wwCiyJ5DoesxPubseHGmJcgskfduU79cmTUmsPsL02JFNEvKJ_D3YKSv8WFdciiOdXxiof8W9TeborGeeKa82Gr_iJEBPxqf-qP7XqYdb3rjv3BPt0Lr3I7bI7OeQSyfvTMGbWz5yIlR-jCNfN08jFAef0qqqDJd-QIFplJ4hkFTv2wiY7pqsd1S7ZmPx_m4jgM5liQekHTVKyNVtnrlz6_HXv2U3NsSschOgoXdBwey0b-03KlSaeuUQ_suEWGH_LiHIPqn9fK99J2nX2DAit5UHVdAGZPV7t80_IWl1tuf0AN4h6YUT8-jBEnxX3G5pv32ubFMPn9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دنا کراری، یک شهروند ایرانی-آمریکایی که نزدیک به دو سال به جرم جاسوسی در ایران زندانی بود، با انتشار تصویری در فرودگاه‌های آمریکا‌ خبر از آزادی خود داد.
🔴
پیشتر ترامپ مدعی شده بود که ایران قرار است یک زندانی ایرانی-آمریکایی را آزاد کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/135606" target="_blank">📅 13:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراقچی: پس از پیشنهاد آمریکا برای مذاکره درباره به صفر رساندن غنی سازی و تهدید به حمله، تصمیم بر آغاز مذاکرات گرفته شد تا اتمام حجت شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/135605" target="_blank">📅 13:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135604">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cab27f5ed.mp4?token=mgR9iOG4_e-MYcApDNdh1FAQWWyjhPM8sMhI1Qqcm6DYjyWHapU7GC-SxcVrNpCsMOb08L-wrKHUcdDoDj3gLj3WpxDXeiulAgtKkZBQQlSRBguJzBWzGxATuV6P8u3s60in7BiNy4yc6Vh8DJerPgnTYCTap0CEqwOMQxFcs8w_UnD6rwYn5llCJBUWmm7OqB84dnR9BpOp2pP7RkXLgi9hSVZwH-EE12Hw5rapj4qtlKi3gEkhQUkOIrwr46d1jyJX_KFeUfgomXaP7wGdcAw0M4Z6ALISf489VdEqjjE3LfMG4e3uOy8w52IbTiK0xr4571tZuWKjcPg_r5zYfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cab27f5ed.mp4?token=mgR9iOG4_e-MYcApDNdh1FAQWWyjhPM8sMhI1Qqcm6DYjyWHapU7GC-SxcVrNpCsMOb08L-wrKHUcdDoDj3gLj3WpxDXeiulAgtKkZBQQlSRBguJzBWzGxATuV6P8u3s60in7BiNy4yc6Vh8DJerPgnTYCTap0CEqwOMQxFcs8w_UnD6rwYn5llCJBUWmm7OqB84dnR9BpOp2pP7RkXLgi9hSVZwH-EE12Hw5rapj4qtlKi3gEkhQUkOIrwr46d1jyJX_KFeUfgomXaP7wGdcAw0M4Z6ALISf489VdEqjjE3LfMG4e3uOy8w52IbTiK0xr4571tZuWKjcPg_r5zYfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پل در تگزاس آمریکا به دلیل وقوع سیل فرو ریخت
🔴
وزارت امنیت عمومی ایالت تگزاس (جنوب ایالات متحده آمریکا) از مردم خواست از تردد در یک منطقه از شهرستان اوالده خودداری کنند، زیرا یک پل به دلیل سیل که در رودخانه نوس رخ داده بود، فرو ریخته است.
🔴
این حادثه پس از چند روز بارندگی شدید و وقوع سیل در مرکز و جنوب ایالت تگزاس رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/135604" target="_blank">📅 13:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
تسنیم : انهدام پهپاد MQ9 در دهلران
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/135603" target="_blank">📅 13:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135602">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی هیأت رئیسه مجلس شورای اسلامی گفت: جلسه علنی مجلس سه شنبه هفته جاری در بستر فضای مجازی برگزار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/135602" target="_blank">📅 13:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135601">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
روزنامه والا به نقل از یک مقام ارشد امنیتی تایید کرد: ارتش ایالات متحده به طور قابل توجهی نیروهای خود را در خاورمیانه تقویت می‌کند، این در حالی است که تنش‌ها با ایران رو به افزایش است، 10 ها فروند هواپیمای سوخت رسان آمریکایی روز گذشته به خاورمیانه اعزام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/135601" target="_blank">📅 13:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135600">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سفارت آمریکا در اردن: مقامات پادشاهی اردن، فرودگاه بین‌المللی و بندر دریایی عقبه را به دلیل یک تهدید مشخص و معتبر تخلیه کرده‌اند.
🔴
ما به شدت به همه شهروندان آمریکایی توصیه می‌کنیم که از سفر به فرودگاه یا بندر دریایی خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/135600" target="_blank">📅 13:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135599">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
عراقچی: آتش‌بس اولیه با آمریکا در جلسات کوچک‌تر از شورای‌عالی امنیت ملی پذیرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135599" target="_blank">📅 13:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135598">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
جزئیات گفتگوی عراقچی و ویتکاف
🔴
عراقچی : به ویتکاف گفتم تا حالا شده در جلسه‌ای شرکت کنی که هر لحظه امکان بمبارانش وجود داره؟!
🔴
با ما طور دیگر باید صحبت کنی؛ ایرانی‌ها را نه می‌توانی تهدید کنی؛ نه می‌توانی تطمیع کنی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/135598" target="_blank">📅 13:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135597">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
عراقچی: بمباران بیت از طریق حفره امنیتی صورت گرفته و این حفره امنیتی همچنان وجود دارد
🔴
این حفره امنیتی در جهت‌گیری در تصمیم‌سازی‌ها هم اثرگذار است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/135597" target="_blank">📅 13:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عراقچی: من هنوز آقا مجتبی رو در این دوره رهبری از نزدیک ندیدم
🔴
چند نفر معدود فقط با ایشان ملاقات کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/135596" target="_blank">📅 13:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135595">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
دقایقی قبل دو کشتی در مسیر ناایمن تنگه هرمز مورد اصابت حملات سپاه قرار گرفتند و دو کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135595" target="_blank">📅 13:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135594">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796f478a7d.mp4?token=RJWkJJgjiiTuWKTsuYh5LWMxeaBcAifiaYGDnOcH8laKOmDHxA0j3waMoEISenBPLzAPTp3HZE7-1UN8y4c0EoAbruYya09Q2HICA_XuVgloxlSusBApHEoP1pybS2L2UYry56khKsIHBbN65dHiPICZZX99OPjFQg2YdA-b-RjaQUzDSXPrjnHDmV3Bo6Nyo4KQ3jGFqVO2R1NNg0NplxyFdXnj1DKvBUz8bl4A3MFErBO5HV4sUS9qljOXYVqb7mZB4mAgVTpkE4iw9bqW_0ax3ZIZIdp256KFdhdintvXQbTabLqOU-1j_B5CR1KzeKxRwnJV9ytbSBl95GNCu52uV7C2mi8aNYFK6tbrCSF0gUQKY25uAT1qYpHzPgi_OOp_PTbTEzENLO87YluSNcFzPqAmfr65CHUwEarmLsMiT1THEpoTyMbpmeU-3GxAH4p4UAF3-M9k5ORXURvT78tZ_ey0INMBLGILggSO3Th57T5cPLsosU9UBm5EmnUSIQpfdnjmiZHxxcAm_dP-UaZHZi4iaohVVBIr06i2jdR6wQluXsgcDZ-ZB-0jO5P3pCJHwcBYCfa3VvTbwGyq40DFh_hRfFI70D_3u2eMyPMDuAiFeZqsF6TLa1x-YzpZo3IePjLLEIV8nt4kWN0gqbffCtB7HT-jY36UWuXljY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796f478a7d.mp4?token=RJWkJJgjiiTuWKTsuYh5LWMxeaBcAifiaYGDnOcH8laKOmDHxA0j3waMoEISenBPLzAPTp3HZE7-1UN8y4c0EoAbruYya09Q2HICA_XuVgloxlSusBApHEoP1pybS2L2UYry56khKsIHBbN65dHiPICZZX99OPjFQg2YdA-b-RjaQUzDSXPrjnHDmV3Bo6Nyo4KQ3jGFqVO2R1NNg0NplxyFdXnj1DKvBUz8bl4A3MFErBO5HV4sUS9qljOXYVqb7mZB4mAgVTpkE4iw9bqW_0ax3ZIZIdp256KFdhdintvXQbTabLqOU-1j_B5CR1KzeKxRwnJV9ytbSBl95GNCu52uV7C2mi8aNYFK6tbrCSF0gUQKY25uAT1qYpHzPgi_OOp_PTbTEzENLO87YluSNcFzPqAmfr65CHUwEarmLsMiT1THEpoTyMbpmeU-3GxAH4p4UAF3-M9k5ORXURvT78tZ_ey0INMBLGILggSO3Th57T5cPLsosU9UBm5EmnUSIQpfdnjmiZHxxcAm_dP-UaZHZi4iaohVVBIr06i2jdR6wQluXsgcDZ-ZB-0jO5P3pCJHwcBYCfa3VvTbwGyq40DFh_hRfFI70D_3u2eMyPMDuAiFeZqsF6TLa1x-YzpZo3IePjLLEIV8nt4kWN0gqbffCtB7HT-jY36UWuXljY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی، رئیس‌جمهور اوکراین، اعلام کرد که نیروهای سازمان امنیت اوکراین (SBU) شب گذشته سه انبار نفت را در منطقه استاوروپول روسیه مورد حمله قرار دادند، در حالی که نیروهای مسلح اوکراین نیز یک تاسیسات مرتبط با سوخت را در همان منطقه هدف قرار دادند.
🔴
او همچنین گفت که نیروهای اوکراینی با موفقیت سه تانکر نفتی متعلق به ناوگان سایه روسیه را در دریای سیاه هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/135594" target="_blank">📅 13:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135593">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b37d820b19.mp4?token=db7B65f1e2SrvCiWeqUkqvM0xObAbPYCrsw9wj_gbu5uBnyKrNqkJ-KX-t8aCALxbtwGiHpSfqWG0CpwWOc6FtI4ndlSycIPLMUEJzNdF_jCGN6v1j0x5GaJR48jA_vWaWCRXrp63e_ZnmGlIWQ7uHrZfeNHHC2TfbRVa5tMYFLlI9--98iEZhCyHZPTn10ipHR-enOATKhVtc79_TdTyw2pOUoc8yFEcYYLKRD4ewAPkGAvo64rvmBS0-uXMdwtIcbFjWOkIqSFlmTKEuxl6bPElDE3jSRHBvXxdIDkS-2YauZB5QNFGxfaCWZ-CytL-PLD6Txxe2UN__xCpk7BWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b37d820b19.mp4?token=db7B65f1e2SrvCiWeqUkqvM0xObAbPYCrsw9wj_gbu5uBnyKrNqkJ-KX-t8aCALxbtwGiHpSfqWG0CpwWOc6FtI4ndlSycIPLMUEJzNdF_jCGN6v1j0x5GaJR48jA_vWaWCRXrp63e_ZnmGlIWQ7uHrZfeNHHC2TfbRVa5tMYFLlI9--98iEZhCyHZPTn10ipHR-enOATKhVtc79_TdTyw2pOUoc8yFEcYYLKRD4ewAPkGAvo64rvmBS0-uXMdwtIcbFjWOkIqSFlmTKEuxl6bPElDE3jSRHBvXxdIDkS-2YauZB5QNFGxfaCWZ-CytL-PLD6Txxe2UN__xCpk7BWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واژگونی عجیب کامیون با  ۲۰ تن بار در سه‌راهی کمربندی سمیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/135593" target="_blank">📅 13:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135592">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjMBV4QZrPd6mpIMpZNARCh7uOKh3w5ku450Y5DAsy4EgMEY_WXS4uFiD4EqMMYbh7bJgKpZhrlivp480bOUhUPmljSIF9dWLPOe817ZDxf5vMgvqYwxbmaBKTZVv5qgV3Ka6Gj6EgEFWlpzPBxzZWrtRDlvQC_ZGgjxgPS0NqEXeS_t0B4fvXZ3m4YsVr4K1Z1YiU3vgXKIIrah80vZksKv3gDhXQfTXATRtDWs8btevfvur-doUXJA37n5AZ8R5lt_--xiPVmvPLnt5jguocHWdGrI1Q0exaK3DN9EWsCDAvIQFc5sUAQif3vypNjBimqKP5LoMAWZvD3nHCgnnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: اطاعت از رهبر یعنی اتحاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/135592" target="_blank">📅 13:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135591">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تلویزیون بحرین از دفع حملات هوایی ایران در آسمان این کشور خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/135591" target="_blank">📅 12:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135590">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toRP_Zgd6QVrq9-Otc0TURf2JQsd1IsNC1c6HlwZM09tfpfOGi1zeDwX8zujbr5XhQQi20GypODfESZnS-uxSeIb6rcowalLGWKRkAaMPMAEw8FF4Y91GJGsW62_ONFKzViIe_fpgxdx09-sfLCU_-1vOEZRRt18QPLJNi-UyGPiy9SDZjQ5LlFRImmHI0tvPwb4YBGclWr0xOR98Rs5jGLdQfvmTglAPpaCFTLsi1lcRN5MJxfKR1yIe03rbQvTYMtVUH2C66kYdMr8UMfBB0z0O0QGLGTiDPqgg9KN477HQv0uNj9fOyfboVzZNGm1HN-PJs9V3I-OgraLgZ-NUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
براساس گزارش Downdetector، اینستاگرام و فیسبوک دچار اختلال شده‌اند و کاربران نمی‌توانند به‌درستی از آن‌ها استفاده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/135590" target="_blank">📅 12:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135589">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=RunPJcMlN0qUpmqllq6YoVVRqZMkDjgBlwGgpVUfS1xJ9_KPkpywtLncUTU01jDB__1T3U5EfYBmJ4Vj_19HPVe_EWY_Ks5qztBlvXlkJdq9fIb3rpMR6bt3YQ3u0I_qWFV-zPLCyFWqyt8H0CNFF70NoBgypmusXDrKyo3bel3-S-4-vVTrj2b07xxY_D4uxWkZl5HTGASghAiV1TfeEqKlUprMm6mRHRR-FnVUl3NrHFz3D6-BUNr2Kn1qLRcpUQs07nnIiQ7EhAXOxGX8U9WISfxVFio501zeKSm0gQGBOIe0-3sWS_15lol2pXEVK4yniXmiRX3RnlKrTO-YlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=RunPJcMlN0qUpmqllq6YoVVRqZMkDjgBlwGgpVUfS1xJ9_KPkpywtLncUTU01jDB__1T3U5EfYBmJ4Vj_19HPVe_EWY_Ks5qztBlvXlkJdq9fIb3rpMR6bt3YQ3u0I_qWFV-zPLCyFWqyt8H0CNFF70NoBgypmusXDrKyo3bel3-S-4-vVTrj2b07xxY_D4uxWkZl5HTGASghAiV1TfeEqKlUprMm6mRHRR-FnVUl3NrHFz3D6-BUNr2Kn1qLRcpUQs07nnIiQ7EhAXOxGX8U9WISfxVFio501zeKSm0gQGBOIe0-3sWS_15lol2pXEVK4yniXmiRX3RnlKrTO-YlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود
🔴
حملات از کویت را حملات مستقیم تلقی می‌کنیم و بدانند که به‌صورت ویژه ادبشان خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135589" target="_blank">📅 12:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135588">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از داده‌ها و تحلیل‌گران: ایران از آتش‌بس برای تسریع در صادرات نفت خود به چین استفاده کرد
🔴
حدود ۲۰ نفتکش ایرانی که حامل نزدیک به ۷۰ میلیون بشکه نفت بودند، پس از لغو محاصره، به سمت مقصد خود حرکت کردند
🔴
تهران رویکرد همیشگی خود برای دور زدن تحریم‌ها را در پیش گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/135588" target="_blank">📅 12:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135587">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گزارش از انفجارهایی در شهر حمد، بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/135587" target="_blank">📅 12:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135586">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وقوع چند انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135586" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135585">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: جنگ با ایران ضروری است، اگر ایران را متوقف نکنیم، کل منطقه را به درگیری گسترده تر می کشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/135585" target="_blank">📅 12:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJZnzRsDv5nmXEtrVOOxV-SpZ-PV7P1QtBtYcEIikVma466rGO5caQufD8SWk66Oi8vfLkkIknMkagYgT5SU0HqbbXUFcjrLL2DhO96MzdjNC1SCTTP589l78c2WnZVn6kCopir1UtIcnX-N2z5A0X7EWmVZ220PZXk7Jmx4lRCrUse0_5GdaFS9K37vjefYYEuNGfBx7fLYj3FySD_gCBy41kCQ1ORuPDkopV1k36LEJuEAHvtgV7RQGPxIloVcHKiba-L4cLQ_CUf9X_t8hQbhyxHouR_QA0shwl20_GDTlXj4mUIoLtpNgvkQ86bJ7JEOjs4LSZVMRuz562IT4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: هروقت انتقام بگیریم و ترامپ رو بکشیم، وضع اقتصادیمون خوب میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135584" target="_blank">📅 12:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135583">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/652941e29a.mp4?token=ao7i_e7asCVhmvj6jbQYOk93wM1xzV7GrGAvn5mNz7g5mnk6a7HJx2jNcHBDF4kt-1Abf9G28WrKLDZZ2kukKxZn56GGscv0qXVtBLd1CPy-_thZGYInvI9raPOdbLMfc1E9mtyttY_ub9pX2rpWv_M9R_1fNnIZ7y7L3XVoej86Yhhw-wOurLHOl_CEW1u3wxhbTJzxxwMkxmp7mTQffEk_WV_7UgXfvsTz3e_hgoX2EUuhvQmE_MO3qiyDZWs5yxAR07tVRrvBhaiQbg80MYAtEAjN8fOwKGeVrt1d1525aiACvzAHWF3XZlnRDikAsc-NMgQQEyFliTDphs_-qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/652941e29a.mp4?token=ao7i_e7asCVhmvj6jbQYOk93wM1xzV7GrGAvn5mNz7g5mnk6a7HJx2jNcHBDF4kt-1Abf9G28WrKLDZZ2kukKxZn56GGscv0qXVtBLd1CPy-_thZGYInvI9raPOdbLMfc1E9mtyttY_ub9pX2rpWv_M9R_1fNnIZ7y7L3XVoej86Yhhw-wOurLHOl_CEW1u3wxhbTJzxxwMkxmp7mTQffEk_WV_7UgXfvsTz3e_hgoX2EUuhvQmE_MO3qiyDZWs5yxAR07tVRrvBhaiQbg80MYAtEAjN8fOwKGeVrt1d1525aiACvzAHWF3XZlnRDikAsc-NMgQQEyFliTDphs_-qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اونایی که جان فدا ثبت نام کردن همچین تصوری از جنگ داشتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135583" target="_blank">📅 12:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5a8f95b1a.mp4?token=XSrB9DXP8EpRVTGpTueHm6hTf0R1gANXcfsISUWju-3Pl0g1YWAesm4rXpV9q-FE4EFOff1uUKG1RTo3bswb2ElnaAUWfqVdh_0BuYNA-PaRvGw1Kl98rP3WJlT1Ex9bhcxOh2Ar_DZc9f9v1rArf1BI6ZjUKXz5fylp5Y7eV5AqxxCIzndo-IHMw88hGO4241oI1FggF2-2b4zwXnqS6pGiVxpEdzZn73MvvVY1JykLE0uar6c2Dxb3dbEw1eqaE1GMBaye6luYcEKzX2-lTHJVla0ox_TwjzkVxPagyQGabZMlhdfv9q5XznqnwwIHp2Jxnzr2xqRjkvHGLTky2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5a8f95b1a.mp4?token=XSrB9DXP8EpRVTGpTueHm6hTf0R1gANXcfsISUWju-3Pl0g1YWAesm4rXpV9q-FE4EFOff1uUKG1RTo3bswb2ElnaAUWfqVdh_0BuYNA-PaRvGw1Kl98rP3WJlT1Ex9bhcxOh2Ar_DZc9f9v1rArf1BI6ZjUKXz5fylp5Y7eV5AqxxCIzndo-IHMw88hGO4241oI1FggF2-2b4zwXnqS6pGiVxpEdzZn73MvvVY1JykLE0uar6c2Dxb3dbEw1eqaE1GMBaye6luYcEKzX2-lTHJVla0ox_TwjzkVxPagyQGabZMlhdfv9q5XznqnwwIHp2Jxnzr2xqRjkvHGLTky2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ضبط‌شده توسط یک سرباز آمریکایی در پایگاه هوایی موفق السلطی در اردن
🔴
حداقل دو سرباز در این حمله‌ی ایران کشته شده‌اند، بسیاری زخمی شده‌اند که حال تعدادی از آنها وخیم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135582" target="_blank">📅 12:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فرودگاه بین‌المللی بحرین در پی تشدید تنش‌های نظامی در منطقه فعالیت پروازی خود را متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/135581" target="_blank">📅 12:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شرکت برق: قطع برق بیش از ۵۰۰ اداره بد مصرف در شهرستان‌های استان تهران با محدود کننده‌های هوشمند
🔴
این محدود کننده‌ها در صورت عبور مصرف از سهمیه تعیین‌ شده، برق ساختمان‌ها را به‌ طور خودکار قطع می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/135580" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وقوع چند انفجار در اربیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/135579" target="_blank">📅 11:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
العربیه: به صدا درآمدن آژیر خطر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135578" target="_blank">📅 11:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135577" target="_blank">📅 11:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
العربیه: به صدا درآمدن آژیر خطر در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135576" target="_blank">📅 11:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
به علت گرمای شدید هوا فعالیت تمامی ادارات در استان خوزستان فردا ۲۹ تیر به صورت دورکاری خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135575" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
نیویورک‌تایمز: دولت ترامپ نگران است که افراط در استفاده از تحریم‌ها علیه روسیه، کشورهای بیشتری را به روی گرداندن از دلار آمریکا ترغیب کند؛ در نتیجه اقدام به کاهش برخی از تحریم‌ها علیه مسکو کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135574" target="_blank">📅 11:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عراقچی: اگر آتش‌بس ۱۰ روز زودتر برقرار می‌شد، خسارت‌های کمتری متحمل می‌شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135573" target="_blank">📅 11:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba05e4f8b.mp4?token=aXUpx1nt97m6V87YDov3d3KN7jPfvmODIcZEscL4yTbw7jQSfrWPEHLfPQtb38OJGgG4WG_s58Xvn-Pw88TljVvsu6cwdry37XfxZYx24JZMW3kaKC_v2EZ0VUeh6ZN5sY6QNcJDYdQNJCLKuFoDAd4c_v9YoCHwR5nfQMLcMXyIcB3CF4syHYPvCTUJN36GNNRQ4JtsZqjmlFM9ky3JV8OXPdJJtL1LB9cSefJEMsWD7CrOfd1qWRZT9vh6gy_C-L-6jXipgwsSE8iipFMO4QZ16ImP7sCz4OH4yislzl8jQ9IlJixdXW1RR3HU1za7RLQj6EomjzPnRrRg_o60yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba05e4f8b.mp4?token=aXUpx1nt97m6V87YDov3d3KN7jPfvmODIcZEscL4yTbw7jQSfrWPEHLfPQtb38OJGgG4WG_s58Xvn-Pw88TljVvsu6cwdry37XfxZYx24JZMW3kaKC_v2EZ0VUeh6ZN5sY6QNcJDYdQNJCLKuFoDAd4c_v9YoCHwR5nfQMLcMXyIcB3CF4syHYPvCTUJN36GNNRQ4JtsZqjmlFM9ky3JV8OXPdJJtL1LB9cSefJEMsWD7CrOfd1qWRZT9vh6gy_C-L-6jXipgwsSE8iipFMO4QZ16ImP7sCz4OH4yislzl8jQ9IlJixdXW1RR3HU1za7RLQj6EomjzPnRrRg_o60yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس جمهور لبنان، جوزف عون، و همسرش در ایالات متحده فرود آمدند تا در یک دیدار با ترامپ و مقامات ارشد دولت آمریکا شرکت کنند.
🔴
این اولین سفر یک رئیس جمهور لبنانی به واشنگتن از سال 2009 به این سو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135572" target="_blank">📅 11:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: تعویق سراسری آزمون‌ها منطقی نیست؛ برگزاری امتحانات متناسب با شرایط هر استان دنبال می‌شود
🔴
اگر امتحانات نهایی تا ۱۵ شهریور در چهار استان جنگی اخذ نشود، به صورت داخلی و با اختیار معلمان برگزار می‌شود
🔴
شرایط جنگی ناپایدار است، به همین دلیل آزمون‌ها را به صورت مرحله‌ای و درس به درس مدیریت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/135571" target="_blank">📅 11:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
تسنیم : حمله موشکی به کویت و اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135570" target="_blank">📅 11:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
انفجار هایی در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135569" target="_blank">📅 11:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وال استریت ژورنال: اسرائیل حدود ۵۰ میلیون دلار برای یک کارزار نفوذ در آمریکا هزینه می‌کند تا تصویر خود را بهبود ببخشد، زیرا حمایت آمریکایی‌ها در پی جنگ‌های غزه و ایران کاهش یافته
🔴
این کارزار که تا حدی توسط برد پاراسکیل، مشاور سابق ترامپ رهبری می‌شود، از پیام‌های تولید شده با هوش مصنوعی، تبلیغات در رسانه‌های محافظه‌کار و ارتباط با اینفلوئنسر‌ها استفاده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/135568" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۹۳ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/135567" target="_blank">📅 11:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7NKeTL7Q_1fGWvx-eg86V9-Ph29AQoUs0YR-OC3cefj0tIojrwk7zHXLyFxk1qcbrSBFrrlEYEKaxnZkNjkt0a1FXA-4Lj8PAgza4sqpHY2lYt3CjMyFkdZ8OVPBpp5Yeah3C2LXv9EHGyVDpndqFqzOANPtF4Vn3C0gnxWeBAeHRJa14hEC5CE6h1WaNY_RadxcTkX_cdmBYbypkOguH1mHiYdWuQkGjQcmz8IrcNQ8lKStJUmcT6KxTUgb-ukDxrz1e9tO23nRMuyvlDYQ-Nd2At-S55WvoojFnHma5EVsA4dyAHJ-adAdneGz-Q2adL1CVWgWY3aAEi-nPL0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انرژی آمریکا (IEA) اعلام کرد: ذخایر نفت خام آمریکا به پایین‌ترین سطح در بیش از ۴۰ سال گذشته رسیده است.
🔴
ذخایر نفت خام آمریکا، شامل ذخایر راهبردی نفت (SPR)، به حدود ۷۲۶ میلیون بشکه کاهش یافته که این مقدار پایین‌ترین سطح در بیش از ۴۰ سال گذشته است.
🔴
برداشت‌های گسترده از ذخایر راهبردی در جریان جنگ با ایران، حاشیه امنیت اضطراری آمریکا را به‌شدت کاهش داده، در حالی که ذخایر تجاری نفت این کشور نیز به حدود ۴۱۱ میلیون بشکه رسیده است.
🔴
ترکیب کاهش عرضه و تداوم ریسک‌های ناشی از درگیری ها در منطقه‌ی غرب آسیا، زنگ خطرهای جدی درباره امنیت انرژی در آمریکا را به صدا درآورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/135566" target="_blank">📅 11:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مهاجرانی سخنگوی دولت: دولت بازسازی مناطق آسیب دیده را در دستور کار قرار داده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/135565" target="_blank">📅 11:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سخنگوی شورای نگهبان: مجلس از هفته آینده به کار خود ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/135564" target="_blank">📅 10:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فرمانداری شهرستان چابهار :  انهدام‌مهمات عمل نکرده عامل صدای انفجار در چابهار بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135563" target="_blank">📅 10:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bb4b1ef0.mp4?token=VF2tLn0KcEWwj1xVXn4VruefHC58peg9okiG8403a0JN91IVm6yQmdr1mVJbLY2l1vcHo58vl-n7tvzqlvhGe_f5iPQv-cYmug-KM8oU1Y64Rf9qXmabv1wdGOoymKuCZMN4-pyOKZBO7sJc13aIZdS4e_bKBfeX4yzVfkPhxVg9Lmh38hykd2ymOoEaeBXI1S4IvfwtmtAxOhpCxalTLyQ9PT_0fi153B63QCgq23WI3vJR7PF0Uejxl5tv1CvbrJCLDBwZukaFRT_2SbGc_Dmgvjh_O3i8OlT0h_vo-Q80990KRVOnK9nbGJnt2WGc7R7JH2BZAeARGHA6NmkiZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bb4b1ef0.mp4?token=VF2tLn0KcEWwj1xVXn4VruefHC58peg9okiG8403a0JN91IVm6yQmdr1mVJbLY2l1vcHo58vl-n7tvzqlvhGe_f5iPQv-cYmug-KM8oU1Y64Rf9qXmabv1wdGOoymKuCZMN4-pyOKZBO7sJc13aIZdS4e_bKBfeX4yzVfkPhxVg9Lmh38hykd2ymOoEaeBXI1S4IvfwtmtAxOhpCxalTLyQ9PT_0fi153B63QCgq23WI3vJR7PF0Uejxl5tv1CvbrJCLDBwZukaFRT_2SbGc_Dmgvjh_O3i8OlT0h_vo-Q80990KRVOnK9nbGJnt2WGc7R7JH2BZAeARGHA6NmkiZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشر شده توسط خبرگزاری دولتی «اسپوتنیک» از حملات موشکی روسیه به کی‌کیف
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/135562" target="_blank">📅 10:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcsHsFDk6i6rgI6faL2S__RsBnuyZGhy3wDiDXXnb3ntA5n39_QIg6GSAJiS_y8RgIiLwfmrF4WuD_3r15NN21xFYs-mZTVrZlTe0hFpRYouGbY45_ZSC16n1TnjYHW6D5-u9zNxz_tBmugbLJ3GcFU8HNWfOF09L3fQVVKzXtzocseEBqDtSIOLmPT0Y_NbN6I9hISpwPzy500cO__r9s33BS7MMQL-R_ewq1mLtmVNLvsaq607i83phD39XDtpBdrTFgX41zcxb1v2byLN_pD1Mqly6Dx9ellD8ZyS3PieA3kEKSUrmwo1e9-u9CT5SOEMWxQQb9MyWxMmBY2Byg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور لبنان در آغاز سفر رسمی خود به امریکا وارد پایگاه هوایی اندروز در واشنگتن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135561" target="_blank">📅 10:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135560">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20f81bc403.mp4?token=CokeDACLCGTDxJwcNitwcsTyhUlJV0boQYRtMpWw-g9bTfGpfpXapc2OEN4Gbk-e5TwLYszfSkNBihghFwJItAP9y7DvGk3gvg9Gwim2EWA7oW4jzrMRpVrZ_dTf6h2Sqry50MhvYaogTBskKOh641bQx2HzUe3NX21pjNOqKAQfvDuNZrlp4H5n_C8uYZkqEMnnP8FEVBXNUrL3IOSOhWDM5FiToz6eyhHvapxnadCQsQxCwM_ay7x3V_zrQ0l76hwkhLgMXWy_n61lKamxb8XFooeKGq8PPm20HT4vQ6DBlzPd1zETpk_MmTihpc9QBtG7j1PlUC4_TI09Pi4c0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20f81bc403.mp4?token=CokeDACLCGTDxJwcNitwcsTyhUlJV0boQYRtMpWw-g9bTfGpfpXapc2OEN4Gbk-e5TwLYszfSkNBihghFwJItAP9y7DvGk3gvg9Gwim2EWA7oW4jzrMRpVrZ_dTf6h2Sqry50MhvYaogTBskKOh641bQx2HzUe3NX21pjNOqKAQfvDuNZrlp4H5n_C8uYZkqEMnnP8FEVBXNUrL3IOSOhWDM5FiToz6eyhHvapxnadCQsQxCwM_ay7x3V_zrQ0l76hwkhLgMXWy_n61lKamxb8XFooeKGq8PPm20HT4vQ6DBlzPd1zETpk_MmTihpc9QBtG7j1PlUC4_TI09Pi4c0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌های ایرانی بر فراز آسمان کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/135560" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135559">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
دقایقی پیش یک فروند پهپاد MQ۹ در اهواز منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/135559" target="_blank">📅 10:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135558">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عراقچی: اگر آتش‌بس ۱۰ روز زودتر برقرار می‌شد، خسارت‌های کمتری متحمل می‌شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/135558" target="_blank">📅 10:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135557">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ادعای شبکه سعودی "الحدث"، به نقل از یک منبع امنیتی اسرائیلی: "مجتبی خامنه‌ای در ایران نیست."
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135557" target="_blank">📅 10:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135556">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YriGz7XC061WrX6n4Euf0hr5g0Z3S92Xk-apcPZgEK0_decuzACpzyA-9XTv_ttboBsuQxhfbXabuVDZwGEQYNsv2KE5yZTaaO4lMf2ANlpH8k7LlBHFltGmGbG7Mk9JXVC41pRmH1PxWkw38J0UnVBAeeJHVYBfCFo0zqT4z-ISs2236Nj9c2N75zdy3zNvizYK6F17vYlSN1TEfoKrluy_5PbRxAI_vsIQNhOs3YDGk4NH9Tg7sLJ0uRtU-WMM9-mpe4lHbQsgGILcdmEGeB8HH4JGOquNuaC9dnCoXpOunbxotREYeVSKpqMgbJESJNRsTk5rQqhEDLJNn4I0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ‏«امارات» بابت خساراتی که از جنگ رمضان دیده بود، به درخواستِ خودش بخشی از فرآیند تامین مالی «تفاهم‌نامه اسلام آباد» را بر عهده‌ گرفت؛ حتی یک قدمِ موثر هم برداشت
🔴
ولی دیده شدن پهپادهای ساخت این کشور در آسمانِ ایران نشان می‌دهد که در بر همان پاشنه می‌چرخد. باید دید واکنش ایران چیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135556" target="_blank">📅 10:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135555">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / انفجار هایی در پایگاه علی السالم کویت گزارش شده است
✅
@AloNewa</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135555" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فوری / انفجار هایی در پایگاه علی السالم کویت گزارش شده است
✅
@AloNewa</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/135554" target="_blank">📅 10:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ادعای یک منبع امنیتی اسرائیلی: ایران، ترور چهره‌های اسرائیلی در تل‌آویو را برای انتقام خون آیت الله خامنه‌ای، برنامه‌ریزی کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135553" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ترامپ به نیویورک پست: کشته شدن دو سرباز آمریکایی مایه تاسف است، اما ماموریت نظامی همچنان ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135552" target="_blank">📅 09:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DapN4fzIVtFGUKpDEQcxwMI-SguBbY7GJcETKHNDdztMj7e97jsKU2udQszm6kJkuk6-2artC0C7iQcR2ciX5C2SaN3B6ntYDDIWHtwmZuLI1y74ygwcmE1DlilVmdQVoFGk7N0ZpvESWLryGtHu_zXIaVCWAbEM3ajk1Z2FfbMqea1WFcq6otZkk-pPfJd-B_ftsvb0ZLxjOECYXnQcDS8oLLk-Pj-k9PUsep-ad_tpzM8EUEZV7_dEzNJQPR7OOfdbhM5DMZzW0H_1aNmGiSZke5LIodX8gri0a1vSJ6SL-ZWUwhOOw1WY0A_Bvh-x9jLSG_KCkwDFdu7Xw7BUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی خطاب به سربازان آمریکایی: فرار کنید؛ حتی یک ثانیه را هم از دست ندهید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/135551" target="_blank">📅 09:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد بر اساس ارزیابی‌های امنیتی، از ساعت ۸ صبح امروز یکشنبه تا ساعت ۸ صبح دوشنبه، محدوده‌ای از تقاطع «یاد مردخای» تا «شاعر هَنگِو» و از آنجا تا گذرگاه «کرم ابوسالم» منطقه نظامی بسته اعلام شده است
🔴
بر اساس این بیانیه، این محدودیت به‌دلیل برگزاری راهپیمایی جنبش شهرک‌سازی «نحالا» اعمال شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/135550" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5_RUfXznY4hA8pJjPZ1rtHypynhOXGJQcIazttxJmhG0aPCOJ_Jy9ZUQfzLRcb2m3roE0Tt8_BHW7-8gxSE58caocKxxT0hkFN1Aw_EBMHeyFm7qQuNExJWoO4RyqDbpLQ4OFZIw8_GOaFMlC1U1Fojr8XRrMaj0jpmeteNlKFrB2AcWHEvYOXTbBOXY7d519kwDyhSWDc5zcJmnINt0qwE3mG84441UkSiI42sO1ziSMUQQb3UssUcWPQx_M_s1vJ69XBItZy2o4F0ezVKDHoK4DFgAKkNmBP3nSdshICS0XwRjq-hSN8wIv5ssEOzHU8kMwVMteObnnpdMX3D-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پارس‌خودرو هم محصولاتش را گران کرد
🔴
شرکت خودروسازی پارس‌خودرو فهرست جدید قیمت محصولاتش را اعلام کرد.
🔴
پیش‌از این ایران‌خودرو تا ۷۰ درصد و سایپا تا ۲۱ درصد قیمت محصولات خود را افزایش داده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135549" target="_blank">📅 09:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
روزنامه یسرائیل هیوم اسرائیل :کابینه امنیتی و سیاسی اسرائیل به صورت غیرنهایی تصمیم منع استفاده از پهپادهای شخصی به مدت ۶ ماه را تصویب کرد.
🔴
این تصمیم به دلیل نگرانی نسبت به استفاده ایران از پهپادها برای ترور شخصیت‌هایی مثل نتانیاهو است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135548" target="_blank">📅 09:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135547">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
روزنامه "اسرائیل هیوم":کابینه امنیتی و سیاسی اسرائیل به طور موقت و غیر قطعی تصمیم گرفته است که استفاده از پهپادهای شخصی در اسرائیل را به مدت ۶ ماه ممنوع کند. این تصمیم به دلیل نگرانی از این است که ایران ممکن است از این پهپادها برای ترور چهره‌های مهم، از جمله نتانیاهو، استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/135547" target="_blank">📅 09:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یک مسئول اسرائیلی: واشنگتن درخواست اسرائیل برای مشارکت در جنگ با ایران را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135546" target="_blank">📅 09:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135545">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
العربی الجدید به نقل از منابع مصری:
قاهره تحرکات دیپلماتیک و امنیتی خود را برای مهار تشدید تنش‌ها در دریای سرخ و تنگه باب المندب، همزمان با افزایش حملات میان ایران و آمریکا، تشدید می‌کند
🔴
مقامات مصر در روز‌های اخیر اقدام به احیای مجدد کانال‌های ارتباطی با انصارالله یمن کرده‌اند
🔴
بستن باب‌المندب به اختلال در کانال سوئز منجر می‌شود و خسارات سنگینی به اقتصاد قاهره وارد خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135545" target="_blank">📅 09:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135544">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1bc04e22.mp4?token=m0TsIuyAS2i5voSwv_jcoroUpbffUU8rw4EimX_QRa0P-0nestMoZU2EH1D0MhvYqJna90I8nDVXaTRgAmEf1GvnE1dzFvrnb5AwmCVdMs_KrRnu6OivcHc3TPbrYLu-0aL-mhKQXIRjvHUXWWK7yL5A08nHE-abJWagDZGYxjBZ7T3-Wqzs8vPM7Aq-SXDGf-u8wm4NTbnhG8Yo_H2aYxJI7TynXPoP5JoK0JTe2zC-E7CsWJxHJLIKzwAe9ZkL-kC8YKD1bP-1_7MvxBD2I9r4F_Z6ZecxUbQtaWZgkZFHvtmvgorQAAwsyTRtLwA3x1fI6bmydliQS4omb9JqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1bc04e22.mp4?token=m0TsIuyAS2i5voSwv_jcoroUpbffUU8rw4EimX_QRa0P-0nestMoZU2EH1D0MhvYqJna90I8nDVXaTRgAmEf1GvnE1dzFvrnb5AwmCVdMs_KrRnu6OivcHc3TPbrYLu-0aL-mhKQXIRjvHUXWWK7yL5A08nHE-abJWagDZGYxjBZ7T3-Wqzs8vPM7Aq-SXDGf-u8wm4NTbnhG8Yo_H2aYxJI7TynXPoP5JoK0JTe2zC-E7CsWJxHJLIKzwAe9ZkL-kC8YKD1bP-1_7MvxBD2I9r4F_Z6ZecxUbQtaWZgkZFHvtmvgorQAAwsyTRtLwA3x1fI6bmydliQS4omb9JqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک پدافندی پاتریوت در رهگیری ۲ موشک بالستیک ایرانی ناکام بوده و هر دو به هدف اصابت می کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/135544" target="_blank">📅 09:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135543">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وال استریت ژورنال: بر اساس اظهارات افراد مطلع، در حمله ۱۷ ژوئیه ایران به پایگاه هوایی موفق السلطی، علاوه بر موارد دیگر، هواپیماها و پهپادها نیز آسیب دیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135543" target="_blank">📅 09:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135542">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
روزنامه اطلاعات : مردم ایران «تاب‌آوری» بالایی دارند و آن را در جنگ اخیر نشان دادند؛ اما این موضوع نباید بهانـه ای برای تحمیل فشار بیشتر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/135542" target="_blank">📅 08:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135541">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98f94ccdab.mp4?token=Mh4SRxp6NAy_UC2BnpL_S3d7neuVDgZpI11UYW9toXkutrXGBujmefxjFigZSnDlLyUAG2jHSj1qXg5PZIg2qOoOctsztQTcfI5BUwwipqhQ4ttiKNhcJ57_1A0Fyz_Eds7dRcPtDz-NFkcXac-9H-rOMMCT_HlECJjygj_3ghdwzaqGJEJV7Y0uj9XPQpUV7eKZAzmZ03nqyDx30WzArnJbWM5CxwpVIyJYo8UA2BfxJT34dVVVPrQTyATx7oM78EkpJc8A146_GQAQVhNbknH3aJmr6mXL2ocxOD1cpWXw-wW58CaQrjGmJN8jGVP0bKsf7ZVUdoo6_Et5f3YpGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98f94ccdab.mp4?token=Mh4SRxp6NAy_UC2BnpL_S3d7neuVDgZpI11UYW9toXkutrXGBujmefxjFigZSnDlLyUAG2jHSj1qXg5PZIg2qOoOctsztQTcfI5BUwwipqhQ4ttiKNhcJ57_1A0Fyz_Eds7dRcPtDz-NFkcXac-9H-rOMMCT_HlECJjygj_3ghdwzaqGJEJV7Y0uj9XPQpUV7eKZAzmZ03nqyDx30WzArnJbWM5CxwpVIyJYo8UA2BfxJT34dVVVPrQTyATx7oM78EkpJc8A146_GQAQVhNbknH3aJmr6mXL2ocxOD1cpWXw-wW58CaQrjGmJN8jGVP0bKsf7ZVUdoo6_Et5f3YpGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خسارت سنگین به آکادمی امنیتی کویت در حملات موشکی ایران
🔴
منابع خبری از وارد شدن خسارت سنگین به آکادمی امنیتی کویت در پی حملات موشکی و پهپادی ایران خبر می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135541" target="_blank">📅 08:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135540">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دقایقی پیش یک پس‌لرزه ۴ ریشتری در عمق ۸ کیلومتری سالند در استان خوزستان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/135540" target="_blank">📅 08:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135539">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سرباز آمریکایی خطاب به ایران: حمله هوایی آمریکا به زودی تبدیل به حمله زمینی میشه.
🔴
خیلی مواظب باشید و از سربازان آمریکایی فاصله بگیرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/alonews/135539" target="_blank">📅 08:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135538">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
به‌دلیل شرایط خاص استان هرمزگان در وضعیت فعلی، وزیر نیرو دستورات لازم برای خروج این استان از برنامۀ خاموشی‌های برق را صادر کرد.
🔴
بررسی وضعیت سایر استان‌های جنوبی دارای شرایط مشابه نیز در دستور کار قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/135538" target="_blank">📅 08:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135537">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70e002a969.mp4?token=knPi41w6n1hRR7eAlLwPCoRt_2yvEDLA9eoJOTvtGbCX3bPvGc_3aI_un-vAyw76RPivj7yWw6I1C2ZlU_cRV60oS7cn0AzOrCbqvkcgAaaUhOouJEi93-I9ks7BUVQL_HX1_m4x5xmCO0KO9RJTTb1hjIYGX5YpYEGgSJp3DII4pWYbXZfGyPgARhS_z3hGdd3eUr8JRIuQWn0qLg2Oo5NoFc7Ze1DQQkLS-HigdANMWR3C7JTgl6cPhj4Q1mzSwpB2UN2gOl0pIaewZnjeSsPfmnG1ERjOglWsPAwpCZeon0okB4NoZAvYUlb1wLz8v7FoAexO27BHk4YoYJIfRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70e002a969.mp4?token=knPi41w6n1hRR7eAlLwPCoRt_2yvEDLA9eoJOTvtGbCX3bPvGc_3aI_un-vAyw76RPivj7yWw6I1C2ZlU_cRV60oS7cn0AzOrCbqvkcgAaaUhOouJEi93-I9ks7BUVQL_HX1_m4x5xmCO0KO9RJTTb1hjIYGX5YpYEGgSJp3DII4pWYbXZfGyPgARhS_z3hGdd3eUr8JRIuQWn0qLg2Oo5NoFc7Ze1DQQkLS-HigdANMWR3C7JTgl6cPhj4Q1mzSwpB2UN2gOl0pIaewZnjeSsPfmnG1ERjOglWsPAwpCZeon0okB4NoZAvYUlb1wLz8v7FoAexO27BHk4YoYJIfRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی سنتکام از دور جدید حملات خود به ایران
🔴
تجهیزات مهندسی برای باز کردن در یک سایت موشکی هدف قرار می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/alonews/135537" target="_blank">📅 08:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135536">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1F06QkxljC1mzss0LR61w6GUzzHKXSqQYEXjdgsbwEa7Me4ysBmw4Gp95GqAhqvR0mBkoZXO-7fB82we9OZzIjbFpz4vkpoteihGpkGBruhMIOGQicKIphp0eanmuogEOjfqHZ7jDOyvEESnEnAV2P9u3Mfs6ose_nRAWrqI-EzrEB2rR766faj1luWOQln1cgTe6X444Amg2pEaI-awuu6y3IEVz5hK0IzRJC3QdVRgxs7C4PGG9jes8PygOWXzqOPZ1-EoueCUFx61flP-zrEr_knhGen0A66-RlGXNSyisej-om5u62gDzTyMJUQtUQ5Qh0JOZDx4TGbovRb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده آمریکا یک "هشدار جهانی" صادر کرد و هشدار داد که "گروه‌هایی که از ایران حمایت می‌کنند، ممکن است به سایر منافع آمریکا در خارج از کشور یا مکان‌هایی که با ایالات متحده و/یا آمریکایی‌ها در سراسر جهان مرتبط هستند، حمله کنند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/alonews/135536" target="_blank">📅 08:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135535">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سایت موشکی حاجی آباد در هرمزگان مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/alonews/135535" target="_blank">📅 02:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135534">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
انفجار در خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/alonews/135534" target="_blank">📅 02:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135533">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
گزارش انفجار در چهارمحال و بختیاری
✅
@AloNews</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/alonews/135533" target="_blank">📅 02:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135532">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbFDHczJqefzoWsZ5yhyUtok5ys4YZ3oInkJ8IdtsBxDgyv8ONObV0tnS7GgnrNW78UdTkztnTafpGwN5quocUfLTlAlYR-d9--tnpq03v2r4OGek74KUMDcS0-RxhI0L9Xt2NamWyH_C-kjWhMYDhsxkuje-9oQzML_LgPcAjrsmYqfl6wASCNgAusUCu8LRaz7hUeLZ20LIMxpODRTPKKIcBSK0kcaKTXJfeXzrC5fp0oRpll1TSG40gbpLXEF8pSyrI57G5gcCprpQZ1BNQN8L6tlU9DnfZf-rcElPE0bbUoZYLgWY6lzyzzgVAQDA2nzTnT25CLOZOV6ZDYxdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پایان بازی
🇫🇷
فرانسه
😃
🆚
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس به نقام سوم رسید
@AloSport</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/alonews/135532" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135531">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/alonews/135531" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135530">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سنتكام:
به سرعت نیروهای سپاه را که دیشب حملاتی علیه نیروهای خدماتی آمریکایی در اردن انجام دادند مجازات خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/alonews/135530" target="_blank">📅 02:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135528">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
۲ انفجار شدید در بهبهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/alonews/135528" target="_blank">📅 02:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135527">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/alonews/135527" target="_blank">📅 02:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135526">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نمیدونی طلا یا دلار بخری؟/
اینجارو بخون
تحلیل قبلیش همه سود کردن</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/135526" target="_blank">📅 02:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135525">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شنیده‌شدن صدای دو انفجار در بندر لنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/alonews/135525" target="_blank">📅 02:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135524">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
انفجار در بلد اراک
✅
@AloNews</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/alonews/135524" target="_blank">📅 02:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135523">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=XHJ8NHtyxLVXa4JqnmyZF9A1XR88ohc2OIF16NTu9XWovLZQcEpUN_OACDxXSMflm7flAU5jZvL5-DO_iRq5ptO_Uun0GPHaae9k5foQhiwYsRa-cGCc5b4YN6tdRbPxJLPwRKOchHFQV_V8W9W-hw-KFwmmx3I8T7FN3l8n7AGHCmEiWrFWs3nKcXK7TW0O4Ru5wsIs-PYW8VN0cfB4CxSV2dePC9tEmtf5WaR3irxW_1CTq24oVUCGIvvI6-e4fu2egnSmLD-xVJMCqJ23BgOcVCQEbfWbbejMHR1L-4PxNd8vEvJA_Sp6Lo5pRaKc4erWd1AyF5o2N1QV1dSxCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f9afce47.webm?token=XHJ8NHtyxLVXa4JqnmyZF9A1XR88ohc2OIF16NTu9XWovLZQcEpUN_OACDxXSMflm7flAU5jZvL5-DO_iRq5ptO_Uun0GPHaae9k5foQhiwYsRa-cGCc5b4YN6tdRbPxJLPwRKOchHFQV_V8W9W-hw-KFwmmx3I8T7FN3l8n7AGHCmEiWrFWs3nKcXK7TW0O4Ru5wsIs-PYW8VN0cfB4CxSV2dePC9tEmtf5WaR3irxW_1CTq24oVUCGIvvI6-e4fu2egnSmLD-xVJMCqJ23BgOcVCQEbfWbbejMHR1L-4PxNd8vEvJA_Sp6Lo5pRaKc4erWd1AyF5o2N1QV1dSxCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فووووووووری/چند جنگنده جمهوری اسلامی به جنوب اعزام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/alonews/135523" target="_blank">📅 02:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135522">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فووووووووری/چند جنگنده جمهوری اسلامی به جنوب اعزام شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/alonews/135522" target="_blank">📅 02:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135521">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
هم اکنون شدت حملات به تمام خط ساحلی جنوب رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/135521" target="_blank">📅 02:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135520">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
صدای جنگنده در کیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/135520" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135519">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/135519" target="_blank">📅 01:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135518">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/135518" target="_blank">📅 01:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6QZDxhslfmbD_N9qTf3OcZ5e0Y5MBYKm00zF2JDS8NrWUbrj4mA41s2_4CvL2TSRpR-6cpDTSz4IcKYRJbDgauv-t43S-FE1nHo_1VMaOWYF3Vn1Q2nLfOI4XJKhXnvW6YrTkiW0M5ufp8LCMyPeGMTZkKpBb_ioKro5oNwo8JFCkvdhw-7cQevjtJMsURidrBfV1xIfuyVzmay83yz0tKJRIbd3fqYritgCOdQaUydQv6bPljP-1NCY8SmhRMac_IHpXsYvYq4E6T8lYmKxT-TAyndKkIF0x-8EhYTD78x_B1LlEXJRmoE2KECFktLsr-XqK_d0ysAuSSJki3tyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام از آغاز حملات علیه ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/135517" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb7277feb.mp4?token=Ec58qTZcBZsjwpznSuTUzttHCtuIPPw2mzivIZ1C1jf7Rq-jFORCh97AntGAy5K-z_K_x9uQXOs_q9k6V_YM932IBBrACJtUY2z0rjSKBlZ4HD8ACdpuxiiwNz4MIvowjVpFHWoNHcUqctmwib1TNlMwxKYko6RALSO-ZCjFL2jcdl1Aby0t6CH30L7LFwLPHJH0bRt190QwxUfFJrGcOMh2VQouTs7nDVHvr6icxYzB0f5VT6LmnSIdtmyDw8cC62KTToXUA_Jj4D2oc2IxP44ygly0GIdSqyGPfZhYZQvzoPUyGvZtPNFXUP4rxndYxHMhL8rIrY-dp-bqPB7lzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb7277feb.mp4?token=Ec58qTZcBZsjwpznSuTUzttHCtuIPPw2mzivIZ1C1jf7Rq-jFORCh97AntGAy5K-z_K_x9uQXOs_q9k6V_YM932IBBrACJtUY2z0rjSKBlZ4HD8ACdpuxiiwNz4MIvowjVpFHWoNHcUqctmwib1TNlMwxKYko6RALSO-ZCjFL2jcdl1Aby0t6CH30L7LFwLPHJH0bRt190QwxUfFJrGcOMh2VQouTs7nDVHvr6icxYzB0f5VT6LmnSIdtmyDw8cC62KTToXUA_Jj4D2oc2IxP44ygly0GIdSqyGPfZhYZQvzoPUyGvZtPNFXUP4rxndYxHMhL8rIrY-dp-bqPB7lzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت پدافند هوایی C-RAM در اربیل، کردستان عراق.
🔴
پهپادهای سپاه در حریم هوایی در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/135516" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
