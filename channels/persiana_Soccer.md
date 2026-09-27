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
<img src="https://cdn4.telesco.pe/file/peoXE9vanxvysLb0_stXpi1BlvuRyLxwVF5e7TR_N3vGE1ytQtS3Exn0n58MdQa3yb4HRbjdO2Ts_aH51m7bdHrB6oZG5ZMyxnR3H3EgHK7guApVMjeQRrZFEmJ2f_1R1H5U0fKQlUHm62WTq4PiNKlXfL271Tn9ZzSKIe6IBztl75_LaHFIpEa6dPA57UPuz6yCzaRhsQBJMabDBn15lxVSjwmTVu8Xy573AhqlYr3qhoUimX7_UPIzcQ2Y1U91YLScDXOuf3vq2OsRAWFcNhw52CAjRytfL-TC5SKesMN1SQRML-YhNdWc-jS8oh5fQ11uf7AV4Upo-sYzT-0BRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 445K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 10:52:38</div>
<hr>

<div class="tg-post" id="msg-30532">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIDJm4iE7rmeJBx_vvOfIoNaaRfWCJo-mysxp02vkBIfi5Qw1uaFFZ0l0P7IR8J3XWDAr_V5_pvaHiqAeYf6YBorysxJRtd8NyPcyHYQvbXh4vylbYaY_aeJJqTDubx0f78AznnWG6Lw_n3c-5-11jrByLH2OOvIWsUpnUzhQV_6ThaagCYdAFcECDYzIzEwGmmGOpShanl2mqGglBAkETY-oY-gFPoWPJjqfB83EGV2cT9egZJ5esfY4x5XIsw857gcNUhx60PtNK1MCYFiJlpOfZr3KQB7xZo6VJqMKxcdFLYjiACt5vK-Doi4MXLKNjRNnYwvLB2y3wkp7fDgsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی رسانه پرشیانا؛ اواخر هفته‌آینده احتمالا "چهار شنبه" باشگاه استقلال قرارداد یاسر آسانی رو سه ساله تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/30532" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30531">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os_TQkfStR-grFn_xguWlyWZf_4hQZVUg56lRtls9Qw3alc48iJ9O0JI_By8AdHqyOtKaCFWDxVRQ88qjPH7oqKqd7dS60uq83HKG4xv_Yam_aAsOOKCkFKn7cPR1Hey6qPjQNAAFvUqCinb0i_QngiN3E31nOz4HCel6IrrD41o-4FsqMF2G19Cp1G0NGZ099oYy0lB-LEli8l4TxXcnsPrQAQNBfDZsQdWFHJIBG4yhrwYR1MMshiyN0iKtz5a3rPwD6hOFuKfVZ3laIFaud28_65ek1aCv5DynZLl5T-NxLZIr1_BMGMa4hc7B3JCVg91mS2t3ACV0WUaOe58ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/30531" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30530">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30530" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
جدید ترین نسخه
اپلیکیشن بدون فیلتر wepari
ثبت نام آسان
✅
📝
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا و یوونتوس
🇮🇹
🎁
بانس 100درصدی  اولین واریز
💵
Promo Code
:
sport100</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/30530" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30529">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmznZY5iiRTj90u1mGZXxGY4AWOEa4xAQbBPAyc8ttL7L40wIkqfMK6n1-WOBjqrUHUsD1vGyJkd8x7AdL5VkL1xup5ezwXmBmc-U0OwLQgAXNlpYpf7KBlRQE-bJVrO16bzT5kAGSuQodkHjkG7-5WMU6C_fa8j5bB7v7nh6IVNcjzz_keywJhym6FviyI8aJl9I9COf46obEwEiWbWieMQV754ChNdQKdVzNXf8yxnmpr-YrMSp_vea-OVkDyNvUR2OzLM4ygE8_hUUtMtC6Cdvnx--JsTifrsc83FFJjnGWPAgUUsmxiS5WFltXlKskLIx6GKrCFx8lbaN2-viQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازی های مهم امروز را با آپشن های تخصصی
در
wepari
پیشبینی کنید
👍
💵
امکان شارژ یوووچرپرمیوم ووچر ترون تتر درگاه مستقیم بانکی و...
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🎁
بونوس ۱۰۰ درصدی اولین واریز
🎁
هر یکشنبه تا سقف ۱۰۰ دلار بونوس هدیه دریافت کنید
📱
کاملترین برنامه موبایل
🇮🇷
پشتیبانی از زبان فارسی
‼️
لیمیت نکردن اعضا در هر شرایطی
برای ورود به سایت
فیلترشکن
خود را
خاموش
کنید!
🔑
❤️
🖥
Wepari.com
🖥
Wepari.com</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/30529" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30528">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYPMGGlYOBFaaU8_ZzidyrWCft-jWRviFvj1Y-6WzvHCAvDPYeorAT-8XcD-a3Mdq0zG3wp0diZYb7A-vKRqJ_Ie07okYdYJdKpT1xC2hMlIqGwe-ipnBg-8ReF-xrMTB12Q8vchYP5UgCbKd5jq9qE_2sTATrIBf_xELTbtvpmYAqrkajTRWwXiarzRlPg7P6O-Ykpj8gbV1gsgE6TciACQXxj2CG_zQ9YdhZ5fk441rBXW9kUzRR2SkThtbfZR3738Ttf0CfkrUDFizJZeBcRfLxczGx87EkrjgXLvt6OSuDYIHvsgQzyXbFxfcV5XPUfBFn7LV0JRBj-5p_QmMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان:
بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/30528" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30527">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifkhEDkexTeFRgOagTFF890cfO37qlPcmfhJGn-WmV8qO3nBiwB39i-8wqksClMdWP7RE1EZsTP4eEEUUV811q7yM67CXhUdbhKrJKqIjjR8LRQ-mM9apgg7gPd7e3J1CDVFBYISRFOgL76UqhA0R6Qxl5fysSBgZuFQcS7be3cwYmhWJyrB4wUXdIMN5PHWQIgF5B8QlZWpOWdznE0l2f2WvqAJ0CbI2aKCn0e74SyQTuMFiyk86w4eMzQt5KT3Kg0AY1waLLyZbjUY2QZ9UtgiAmfu-D1GWwx28tGNmJqbRC_RxTrv-Xosvb8IttJwfRSOSr9NSdaNT9TqJLvEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/30527" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30525">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo_3Qh-rxZJz0vdR9dWXaKwZCTqDuYZtWa9aUNgGdlOQ8qXeRTJIblI40_GNwyGE4bnq_2CpOwpE75xlqyn7rTBkRlKl_RW4xwKzXtdox_0gAF2HazCe5wB15TR1Ec30MLyJdDzD43Sc8WMVbLOPicaDWN16_RIv9du4itMOmIKyxWc9TCV4y3mziEjuqI2ckfvEx8jzK58S5ceXDaXzxM3oq8jQSEsNeqgScXozvs3RbkeqDPrIIppgGjEnwaMuik7ndtCTRqjDtHtFUvCPuilnpfU5Jxi3GxF2EEEckaQO5eFaiv6BgofleAfK8VlyL5BMsWOfpkKGyWzDjkF4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب اسپانیا
🆚
انگلیس و کرواسی
🆚
چک درهفته‌اول لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/30525" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30524">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAtiXx-twKRGBWc8XHi4iuLlFfbXw_dDscS1rvhyqFwRHgcbE0SFKCZHr8HUMSJM9oK3jwFoZMAJ2im11-iwaXCCDqqpYs2zY7znUKJe9XMnVJP2soLnY1SrzROkJSphLIymy3GWCIwny8C9eoKMC635oQq-a1ijn2tWZY-o8zQll9ZFjc_BAnN45VbmWtFmgvAuZclg_je9dUsJrLc0yQ9fmUrSx8a8nDqlOFzOafD_VzUmA8EP3OlsXDf8yF6Vs-ANCoMuBoLzoPzPQEOPJFDlDYEXkNvFJTKDCSn4SmfAsTMJXg3F6wSUZKIwAQ5yr6iuid5J7n27dU9MJyheGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/30524" target="_blank">📅 09:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30523">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826b26c676.mp4?token=gnSVHQbnAGUfAHKnNmkOa1uXtLQ3HhxiXLUfHavM8WuumMikYbkzkU71z9e_5q2WyBFKHi-mIXtffctEVh4B79bsgS9xRlCVlxMpbw3e8bJ2RPy1T2e-HGRGBCmoOUc1KMfu0a7T2EOoM6ZzyX5QdtznjlX33laq_JrMddmFfnv4bTxlUphEMzRuW3efw3CQUvDGCBAHIAosW_MgkG4U2YNdh9xP_JlIdsNeM3n_1O0XMaSEj9rjorWCCGKRDsWn7jDTMgAXpkbNzsrfj647O7JtV34PLDKkgKsA9TN2jLo-7n9MWlI6kSC6O-a-MypK3T0AEHLMevjSq8xe58yxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826b26c676.mp4?token=gnSVHQbnAGUfAHKnNmkOa1uXtLQ3HhxiXLUfHavM8WuumMikYbkzkU71z9e_5q2WyBFKHi-mIXtffctEVh4B79bsgS9xRlCVlxMpbw3e8bJ2RPy1T2e-HGRGBCmoOUc1KMfu0a7T2EOoM6ZzyX5QdtznjlX33laq_JrMddmFfnv4bTxlUphEMzRuW3efw3CQUvDGCBAHIAosW_MgkG4U2YNdh9xP_JlIdsNeM3n_1O0XMaSEj9rjorWCCGKRDsWn7jDTMgAXpkbNzsrfj647O7JtV34PLDKkgKsA9TN2jLo-7n9MWlI6kSC6O-a-MypK3T0AEHLMevjSq8xe58yxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل دی‌ماریا: اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/30523" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30522">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDD4pAtpUgNx-UVXplRwMSMe85IdzYFt7vhpEbjIg7gRpox9vLHSgmT28Vt2Y7t8od4J-Af-kt128-rCLaTyO1cucK6loC7kCHd2ffQ2JU9tYoo6C0SY4W3p0rIVlnyH6YQovS4Y02NPCbdmYFykIAEOJ8Kiix6gmZfc0MlB5HsPLndRxwBHtepI0HYjH5fxkIJ-YWIx3XqQhiqa7PoVB9pN-OpK6Byjvwrc_K2Vg2YyJECL852xs7z9YDjxTAcPW7pGDkzvxXzStne2wHvGOxFqTRELRSKpNdHahk1IRNNCwxOML4zhWI5LsTkr3OQnzI1J6-GaKmAJjc2xPOGSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی رضا دبیر رئیس فدراسیون کشتی: از تمام قدرتم استفاده‌میکنم تابیرانوند ازخدمت معاف شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/30522" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30521">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khPVRNmTH6brIPYKPOg70xGaaMJwsUDfJaGV7yWCjMOT8bCitPlwh7plnk-2NFCaUSCIgR3w-DrrPAGJola8R01XCrgU7Q8QJMZLovYYnzna8iLL-qpPoeStpUm5tW-hiPvC7f8aiWT6kiKxoSDGh0OaYBtTvQ4xJhgw247wXpf2SbaTWYOMXsnYJXbpTkRIHSLJoOcu3f_skVuc7-z_RCxkQI9rqBXhjUW8ClDGvYX0nnHAL5Nc_M6ryVt1o8JjglhZnGmIWud999ndqqlBIT2zszXE_s-lgRyzDfmGbMsbMNcb40IQJcScN5RCpHK0Cy8nzrljZroIbwr5UAn3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گوگل رسما ایرانی‌ها روتحریم‌کرد و از این به بعد مردم ایران دیگه نمیتونن‌حساب‌جدید جیمیل بسازن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30521" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c394c65.mp4?token=BVYnzoBlP0KHTMOMR_7tfSGQgfAP_K5p5QgIKbsEtyHbf4zIRfffCcLsgxtsbcGGgpbg2Z5Q-tjdIZXa4xG-IeO_RSTw-Q6WwVmG1c7mtHkVBAIZCwKkWR-H19PBz-QrAp1KXUqSNCqxXqz1r_HAXjClB1XW5TeTfbyJVb0vbFMLAcxye1x41eGARKIp9Io--qaoAtzo80oGcYng90l9ElU5nsN_5PWUFvI3DlpJW0ler_kC-RH8nqrultdVyOSqH5ujEF-0oB5QluhYoDyHqM4RJNOrtGYi6gtbYxDtlin8SrFTK8RP7PyFSKOBxNFMpZShwxV31-G10ATTakpE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c394c65.mp4?token=BVYnzoBlP0KHTMOMR_7tfSGQgfAP_K5p5QgIKbsEtyHbf4zIRfffCcLsgxtsbcGGgpbg2Z5Q-tjdIZXa4xG-IeO_RSTw-Q6WwVmG1c7mtHkVBAIZCwKkWR-H19PBz-QrAp1KXUqSNCqxXqz1r_HAXjClB1XW5TeTfbyJVb0vbFMLAcxye1x41eGARKIp9Io--qaoAtzo80oGcYng90l9ElU5nsN_5PWUFvI3DlpJW0ler_kC-RH8nqrultdVyOSqH5ujEF-0oB5QluhYoDyHqM4RJNOrtGYi6gtbYxDtlin8SrFTK8RP7PyFSKOBxNFMpZShwxV31-G10ATTakpE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30519" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30517">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5NfZeaNRNaMgEJd5nCKQFMfFei-wgpHwUxU4lhGvrqVLL5LlGyMebzuTY5odBy72cscFaPgvj8G1YFmRORxLlVANzXk2i3MswnbtyCcwkTvs9rvXhkhxqtmi1VkooEg6SVbgB0GJ8Ch0krs3nZM6Urmtqbjp0aVsHgwwKrPPIMK9qbZSJFTwX0ZqmBJmvC2DwFUZkggAtnXqggVecfMZNBQaX0AzNQydkKSjNVQ24G4NSZsd4IVdKiemslmjxtUvYNwt5ntnGlxDccneWXQ7aqpSw3MGEam5WTNCZPvnhF8-1ksOPja6d6Ofo2iOgsHTBYEVaLTsiVirIBb9241Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ اولین رویارویی رونالدو و ارلینگ هالند با دوئل جذاب دو تیم پرتغال
🆚
نروژ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30517" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30516">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr6XWJUtxJ2TFfmjoCQ2-14xkuD7OkIH8fB3BiXmJLCGLdZBvPJQuwFERSWDs1zEUyE-dsqF1Wtty0nOTRntsatrJLffS4o5k9SU9nBXR_NvRMYh2aMn8USvEk87cDLJdNEtIaccmijT7QRXRhU9DMGMaO2lp8LT4Xw6psLCNy82m9nj9Lqh17sIBg2AuaU7ChDBrU75T2tehhY7TcchXggl6qC8oXGEbQAGkke18cX6Ta9M0DpVBijgVa4XHNmEMX5qaULS-ewOdr3pyOBrkG9vrYJbWiziHnpI2594CaU54ngdGo-kZu6qykBmRZ5qLBiYAWjAqt8OrGBlyUVm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد ارزشمند ماتادورها در خانه انگلیسی‌ها بادرخشش‌الکس بائنا و لامین یامال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30516" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30515">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vstZws2s-QaZNaq1VawKHY93iuZOwY2FdlZyu_ukoUPCmF8EbTGrDm7sMfwbIAF7pxgSgMcq6guLtKKrRBH7ec3Bb66bBGx6at_3GoMnmEc8AyqAABUO_Ck7_4Dt2o0nslcPzhQLIKEfnqUz99axmCowZ0cnfBt0ZtQ88Ho3ZyvWt0juNUD7dUSinGgXznZDSXs5NvGS-fcWIqmBFWDmySuASO8SBHPxQKohlYe7umBGtEG35gYuvqSVGEZamZPGtxXQOLiXeaDHfNDP7F0rilsZLUsKNR8xV_lfx47TWsN_Pg0pP6_DzybBKBsrwB6Jg5-llJJj5Yb8N7eqi6M-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
داداش فوتبال می‌بینی ولی هنوز ازش چیزی درنمیاری؟
😏
⚽️
یه سر بیا ایرانی بتینگ
👀
👍
✅
تاسیس‌کانال‌سال 2020  اینجا خبری از حرفای الکی نیست؛ بازی‌های جذاب رو بررسی می‌کنیم و فرم‌های روزانه می‌ذاریم
🎯
📊
💰
اگه‌دنبال‌یه‌کانال فعال و رفاقتی برای پیش‌بینی فوتبالی، یه سر بزن… شاید همون چیزی باشه که دنبالش بودی
😎
🔥
👇
بیا داخل، خودت ببین چه خبره!
🆔
t.me/+3P2wZvzhZbsyY2Vk
🆔
t.me/+3P2wZvzhZbsyY2Vk</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30515" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30514">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVSCnzPtMfwxXPcBOtqS5g5SCLo8GS3jYvZpXn2tuChj18IBs9dXMev8CPRMnR5UD5Bv8fFvG9kQqiO7qOopXuNnwSZNK8NOBltgbKtketLe1qlZinRR6y0zN8BQ06zPI7wuQ4j8gFfsiNk6SjEmrsM2V1IMqnUmhuBPmx5R9WEzfWZKMjg4elwKTKpe69sWmxuwfxV_nNwaNjfpBj39gp8KMW2B1BXQI4gNQag23QUXDncJIaEnJ0PmxP7UM8MYHDzEEFXeCdMEX88lIZUVtmYhbgsj7NA0G7dR7jCZ09WrRc3pa7PNQnR9VArTKju1XnYKCyx2u5c1-TkLvIXkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30514" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30513">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wl1sriCXIXS2dmxciH6stRtet8POl83ApHl-xIZwHwxQR9F7bJs_aUbp-tdQGu-oHWDpUyS-PsXr9z84SG1Kj-FnoN8oqABu4YMJc9XyuFHzoOdR8b1vXJUbbCeOv0UQEq4qFnqC-xZKJWPCL7gkK_BS4vuBYfRlEClhyNj6PyMNe1WOmR20_U-kz5H6L0JT48DQhuCkeZgXdfS7q-G4Exy49B85is_TLv5td0o7VzcYqKgknHEpHhjpYiFe51HH6XAzFR0hccMv8zpiyY2ZBuSOE0Pw5sKPQkSyr70jMzO9ouxQeqJWiosqxbw91jMrhJOMksjM0-J1zIktayzIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛جام‌‌ملت‌های‌‌آسیا آخرین‌‌تورنمنت‌ حضور قلعه‌نویی درتیم‌ملی‌خواهدبود و بلافاصله بعداز اتمام این رقابت‌هااز تیم‌ملی ایران کنارگذاشته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/30513" target="_blank">📅 00:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30512">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCdfMZRBasNVSXjkA6hBbq0tKjdSQeWpI7qVXy5UQ-v-uo2W3nQOEqa-0wQLoX16fy2chxSjKZpRX9_7jnA3_OYnSz_hXNfn8bjsdkvdv3kNMGzzP4cdKEYvsxulaR-RI2yshcOzD4tV_Yi0czHFuv3Zx83xd7cmZy8Z3xDv5f_LjIjfcBFwyF0QtQLWYY56FIvxN_Gvh_kRfOZNu50JltcXnRQuKF4WBo55Rd82l_3euSZLm8OtnQ5gZHKr6SlDixlWM6r1H2uu_7yWm4GWwFmvftQKzNLFHslDSYliujDPSb5w1iDga30Fzz5qRCj657wtBROdcTGZIxHy7dnYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30512" target="_blank">📅 23:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2_nCCmU1u7welLvWvssxOCwufQANd5JwEgcDoxl3Pfq9XKfmN-9LudJDI9qYmz9ebB4Nre6yt9IfdQ9vfDolvbrVLwliOF9GAjjSJFhZ_J3XUWJZ7XNB6QEPXZY5nXHRjUjAZL8GdFwJPRpfM8bWeZNLRB5iAIdVLxi9kG2Uv2aP0ho_poqyA9fzCGuB8AgZABlbnpP65JAz7tEwRCkEOhsCAqh9GNSrRx4TqvShpNhNoVEBeBtSidsJ6AKKseU0RxX-JMLu5NDXN-0EdZUe-HX10KKFFMAitSr5R2m3HAbq1Z3ndyE8qvx_5sL1CTgm1V0Fk9VCXsGzE8uG7OrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#تکمیلی؛نشریه‌کوپه: بعد از آزمایشات گرفته شده روی‌زانوی‌مصدوم کیلیان امباپه مشخص‌شده که مصدومیت این‌‌ فوق ستاره حاد نیست و امباپه بعد از دو هفته استراحت به تمرینات رئال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30511" target="_blank">📅 23:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLMyPVImZjlIun7YN2JpiMdHsQXRykUqW5SJGJTnuAcqsU387FtwzcAZcXzmUOb7qgnsXOeFn3EDd4HfcfgoILv9sSI7wBI-i9PsZkhTvBZE3MooIcYvpAqdAlWDpCVctDgC-dHJUzawcWc61m12vDSfyM2WSGV2uLeYhBjBiohjHKolbP0Vr5QCFSPsx1u003jog4bhLwclFHIfx6VAdkTxuxHegN84C5XCj8s4V7qWGBMXgPNscN06RIiS-XHtY9Ncb-GR2rNJyrT1yg3lzwW_kPWUZc5pDEeKIkV8HD5Esp3xXsAjaEt83kaJ3fHFj2NuMT6wCgQ94D6n355xqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30510" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igkozzQ_wKlCj0hs6rUn8j8IjgPARTsY7PXj1GaI_BwXRds2VD7TAZkmhMymyLuZKu0NWelaXQqC0YxStHEps-_tqFvUJfTFa7wcR347e1KMlbYuJULtjjZq_d8_XzPhWKwAJrs_MT3yBoFwhgINXxhZsiQecpgvJLb_SWknqS-zICLoJv7Az5eo6jlBu3SaI5xWy5w0hJYVlMiBIRUBFniVgHvbefuEsZ8T0PY4i4KHLaXZ1SkBCvF57b1oU3Dwu3BD3GU7q9YUBR4I5DInIOaW49ma1n7yrMjSnuHr9Fjp9-walJhi7FHhMdU_B1zY4rXuD2zLwecBN0eBJYow_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30509" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSQEroSlMuSrvOdmBXHHmJqccqzwFRPBhBj_46PQCGZP8VjSTv4KHDYGMM3ZCkegTKf4FH7sSHdwwQ8r8fkJScO9QOOVn_SyN75K07Gw6upIAZm02oTTvo5aEa5wWg7oKmslK14Cz8lXzRifQVLb5v7Z0xTs60fSNeW0UKye9jiFGIFebPlihw3w0CSGulAIzHL3P_B_tJKWLruqBcKel4BW6oKwqGwVrFoxEfJE9u7GaWB0RySQ9Edo9hVFcOMCrQL3CYaCRBLygBOssOfIR9mpvlqdM4NAzm4Q2ctwYAcBP7jH9Ttbq5rR3dbjv26FcDfEdXPhXhlnZsl5ucZvJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30508" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMdKsoQCEKYBld4ct-0QSaFewYUwGZc1GNmNdiEdSUVm0Ub9dFkMFKHFi4C11GL27s9bH5ef2Ldeogr24uYqt9QqeTXsPlvDAlozTHyVCB4nM_Y_br3QMOSGX645_Jm3DftdpBT5eX6vw0gee5orcrKr4IEj9TKBQwVq5YkLZfwKA85ORJtplDkfXGrAiDwe7vEHk3M7vZTw0LsE0vAYJBB_E0GyQ53aobe4DRHqt-jR1kPfcFtLNbm_F2CFAOP5Oyzubwx1Y7DMHshRFg1az_7SaZ_VoGiG5y7NDUNaZ6_tLRlRPWlgn1Rc8kljykrb3CMIe7BphNYQuyq16fwJZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا دبیر: مهدوی‌ کیا یه گل به آمریکا زد و از سربازی معاف شد. حالا به علیرضابیرانوند که ۳ دوره جام‌جهانی‌بوده و پنالتی‌رونالدو رو هم گرفته و مقابل بلژیک آبروداری کرده نمیرسه از سربازی معاف بشه؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30507" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30505">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E-ZWPwSz_hMImVtKapUChW4TzJoqGlcFu2jfA1EbX7-EOFWqNXU3edE2xN7B1vh_ZrbTXKfu7NCSJR0r5tnDE6hDIbV2F4FCgTID97Hgq-mqrDwC7wcBul8ZjTszSSPXrri1hDM6BGINE0gadfeeiH8RMMB3Wo0XpRms-5UR7CEPMrA4hUJBzUbES0iVT_WYd2c3AKGsemxN95UM0D8jlAz_Nt5zB5Q5QDZo7Rt3RfAJ9MiZ3jiFxDruROaK-npmKLU9QwHJcO7XK-magUKCKDV-ScP0eeWTZkyZrN8dVE7Jy09ZnN_aapIkrguymhSXAY_iFryXqJrlDfaQDlfB-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFHr03HlYp9NqTezkeUf-k_K0yhQvYBLNxGqe0Jvew70OGkfbrKW4t64GsqUuluzu7WDQVW2fB7rURTVspSjb-mail0KbtIzU2eI-_8VgESbM8aniStFq_GZuflhoulRE8-1-nYrklx8jqQNlXccNAUinn7KuIbAeri8RDVJ5Z_8rm9DFsMezRzGyl04iPFLSBhiTxD9KDJTfMRrCeLQX8Wz0zKC290e2HRR5_4rdC3d16-V2HY3BK3A483Op0KDr2xZw5Fczijq5dBN0Sxv12bXOIChQYY0L4_RD9DZA0BXoD1qJrqNkKA19m8qJGKfxZkgBBw816Rh2CVcs38WzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30505" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30504">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vruW-sC8zfnD2KQn5yMl0M69jOzMMdzQR7Uys7wXlI3998dAgg-qMgKQIuBM4nFUxRBtUa5pWkN56myAn1p4wwpQopImjjS_Va2Tqxx9dwYG2yg73lPAWf2kiL9gtADm04zaKba4O_kjaIzl3wmtv265wJcHqJrbQ1hNe7HXYB3ZLCiyx2TryvBu3Jl9nPiekDi5_A6Ho_bmNFUEHzp0IwG8E-DAyVIlkcQ4J7nN0fVERVv2Fn1-X-UdmfUCm1dQBFB-i6oTjfdo3wVPk9G9bbtFIb7s2diPXn9bQyYS-5yyKKI50WlNBJ4IYrWZuc23nvdgJ09ogoSgC9x9z8lhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30504" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30503">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaBonKpR7E0-TaHfTIgUbS7o2mHTa5B0fGTF438bcpejlCZLArFqt6roZbNlzusjcV8JfswY8PrxpdmDDgRkPgVl9EkyAJsJlA3Ng8XGTCojiqPRvtOQ32tdcKiaWgAFM1VOh1bUCHRh6vA_bB7iK2Acx8TW8ZrWkztQM_JzwXWIRvNU4OP8_ZYliH6tP5KjsBeTxPW15vzuVm4JsKLkUrZDQXEEHfriiV9ZBV-zmsVvPmUAPlSXsWt_vX-ESnKJuB9DofZ_OSvwVW4DxpSK3Qhv8TOXFAppB2Rma3nKQuvEgkQQuGrKumkxbQY9tzE31TU8BuyxgecPc8_ryFRIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30503" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30502">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=oNKCPYWqBz-W_CE8TgUFloeYtL6w4cUTikkvqVbIE61Ez25nGHmEFVgDuWIWiYUQxOW5FQqV03KopV-rk9hAlkac_4wFQspmsrsTwEwcM0ro2EOXRNiiDA4UcMK_XnOiWftGL-iS4CDibSV86FxB0UZCZQsdPqvuPpjgDb83J9vr7azwWYy9UgGzkVWk7T2cSCrHbGOH5cUZ9l-cJ7b9eenJxpn5X4VyAuujbmErmxq4hh4xJTm0PDRFzFoXhvoZmxq-Faip4flQyzLXD_74ScPVae-Eb47aNt_4Rjgcf8x00S7Yi6U-yFbGeYoaBi57W8ELmhoAD7EpylyNRMyT6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=oNKCPYWqBz-W_CE8TgUFloeYtL6w4cUTikkvqVbIE61Ez25nGHmEFVgDuWIWiYUQxOW5FQqV03KopV-rk9hAlkac_4wFQspmsrsTwEwcM0ro2EOXRNiiDA4UcMK_XnOiWftGL-iS4CDibSV86FxB0UZCZQsdPqvuPpjgDb83J9vr7azwWYy9UgGzkVWk7T2cSCrHbGOH5cUZ9l-cJ7b9eenJxpn5X4VyAuujbmErmxq4hh4xJTm0PDRFzFoXhvoZmxq-Faip4flQyzLXD_74ScPVae-Eb47aNt_4Rjgcf8x00S7Yi6U-yFbGeYoaBi57W8ELmhoAD7EpylyNRMyT6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک گل فوق العاده به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/30502" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30500">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEGRTWKkmdNG-Xv7xI1L-JXxEw0Rv9YGFD7Dg8GBuG4nUMeXLzWBzyQvrVQYSbcnj_FZw5TfpLsF_vPwwGRmk5sGzDsiJh1ilQuYQ9dvPDnFLtdVxUW5hRm15v_4YZSQAgL9Xlf6E4LTMpDLwS0eYaMV3PtWbLRW9dp-fbT4a8zyZh8KKL2O-QgOJbLlgWuy8WyM3cwfrEeC4Box3XhhTUovtCcxwu7p9Cu7JigCoVUD9jJ5moVROZMPeKwoSQ6VbZZIxon6hKwFLraXxVVsICwWG9scYDQ1KOIHmR4MHMkLCn3UzoVAXCmeOWIFULjgjZnL2I0QtIpS5liioZbVKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30500" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30499">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITWkgojcOqkkhdUZ7XciR6xfm_V9VZYWOnWD0vmNmAa1ZQ5swuC7IkJPUbrithkXE2Z9krPhuQKU5oB9ZosgRCQ9lDoAMI3ZUm-oS3X9suLcYLKWQmCr73TQloyKtxnxm54V040rtAsCEz8p_oI9azp9bpG1LwaY6Fpe4AtckQuDUxGYrarPQWA1XqKVy2R1rJE8wljogZRqFhXxsIWVF-WlX_9nowc6D2XZHbwVb7eaRNebL4XjuNcs86QVvZHR70ErNhgs1OwEp_vjRQly--cAlfiNwInjWCy0yzjD-0OuiHLh4Ngp_OTz6LW_XJC9en5Fd2d78pemjj_kQZKsgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30499" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30498">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d92fMGvm-C6iJ8RHYkQR4TsbEJENv7x2EH6TNMjAcQIV60I3Xa_r1UiigKsATjrSV7eiOVIaEgDOLuzFKHQz-y7w79PuiRhNuO6s6LHZPtlx61ms8MNvHmNKsHsnqyjkdF568n2MmcmBLz0-O_lmEq4t-PKRo4S96d-KeUtBn-zysKk-jFH8THIf2R33cc5SAk1oHTtOuAPylZvsJivgM6726K-I4eBkdlg8kmEIZLhfqqGjI3oUnxoDYuPV4iECHaOfH9n3cMvn0_sUj-3UiGn4vxs3e2Pu3cabNMq0rWBkgigGp7VLC1xYZ8vez80gC_890MT_z_YbKMwAgVKPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
81 سال‌پیش درچنین‌روزی؛ باشگاه استقلال تهران تاسیس شد. آبی‌ها باداشتن دوقهرمانی درآسیا پر افتخارترین باشگاه ایرانی در قاره کهن است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30498" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30497">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=d-OpZZX8pUpFnClSP0KHrvoNAFWdi54_xAxVdM3tbKRlMO893fQXf7NO4xvutiBzI7lL1MjdikrXf4Cqf1Mcydcs9E8lpNMZNvbick4eQy_sJqFbD7Z1_UK-zmH29EKuCMHYf1-_sGypDdTqvMDRoQa4MXiOna8uvrocY7Aah4r6loPtYr5zOL7bktJ0WjgpiPkEh-s-vSBuBvhvRbmiHioUXAbSfaNMaAzwlHNKs0mS3yEipi1j5GPBjc5uCoTBmXaToSQztjeYSfLYv9D8Bj8S_sjiTsRBhrHRFRZKcWHK8gx2XU0OjBnMp_sm3XrWZK8niQqoD2XDsC_p8XyGQ0vyLZt4-HG1QOnbIvEq-ZUP_FpAb7FoRPuBLpirS1rx3P50iG2FjS8w6YOcDJdv6t6IXm8FzgMvajB_771Pw7oU6fDCR7n_BMWaS0AOx0dUYA9_xz3j4tBbWri-RZHBvH0o9L84av0JACuSniWuiURLIwfCNbvrRzgjvmbEdZ2KdckApeEaBa9tPBuyQOJ7jdbqI3kAJTkKmZXfm8DBGz19oVCUAzvKkxwZF4SvlJQaf2FvYVCiDAnKtue_BNYSSjBBL948tOA1e_Eq56Z8T6t71GuaykaWOPQQvtd9m7E8Fh75hKY3jY4nzD0tebyNgFU-CH8f43j5dCX2XmzErgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=d-OpZZX8pUpFnClSP0KHrvoNAFWdi54_xAxVdM3tbKRlMO893fQXf7NO4xvutiBzI7lL1MjdikrXf4Cqf1Mcydcs9E8lpNMZNvbick4eQy_sJqFbD7Z1_UK-zmH29EKuCMHYf1-_sGypDdTqvMDRoQa4MXiOna8uvrocY7Aah4r6loPtYr5zOL7bktJ0WjgpiPkEh-s-vSBuBvhvRbmiHioUXAbSfaNMaAzwlHNKs0mS3yEipi1j5GPBjc5uCoTBmXaToSQztjeYSfLYv9D8Bj8S_sjiTsRBhrHRFRZKcWHK8gx2XU0OjBnMp_sm3XrWZK8niQqoD2XDsC_p8XyGQ0vyLZt4-HG1QOnbIvEq-ZUP_FpAb7FoRPuBLpirS1rx3P50iG2FjS8w6YOcDJdv6t6IXm8FzgMvajB_771Pw7oU6fDCR7n_BMWaS0AOx0dUYA9_xz3j4tBbWri-RZHBvH0o9L84av0JACuSniWuiURLIwfCNbvrRzgjvmbEdZ2KdckApeEaBa9tPBuyQOJ7jdbqI3kAJTkKmZXfm8DBGz19oVCUAzvKkxwZF4SvlJQaf2FvYVCiDAnKtue_BNYSSjBBL948tOA1e_Eq56Z8T6t71GuaykaWOPQQvtd9m7E8Fh75hKY3jY4nzD0tebyNgFU-CH8f43j5dCX2XmzErgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌فوق‌العاده از آنالیز مسابقه شاگردان امیر قلعه نویی در بازی هفته اخیر مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30497" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30496">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=kstWO147ItG8YDyl7QN-lR4g1N6Ow6brXsTRj_FJUuB6EzokQKeiKVB95HjJ_eCUgXoEBnU1pW7ibK4XtWg5UMClstB8nblu5SV1iatk3B-L8HTItA-O2Rlx3qvk6tvVQ44uABwfQTAxyQrxUwO-bG8i1AGjrnyxUd9m5FQfI8lpBGN3oY_AgWCAwtcq6GS_6SMiouNv2j6LTMfKhYxOMMgQbo-G8ISBfR90wsE00dqeeVJmWNxdlprOmAMnRut2nybO3IC93UEO7RJLFYNQE33Gyuvfiyo0L68BM6lkMK_Bx4AAiowuNbjh2lT9bDJztF6OKWNffJhq1AX-9vy8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=kstWO147ItG8YDyl7QN-lR4g1N6Ow6brXsTRj_FJUuB6EzokQKeiKVB95HjJ_eCUgXoEBnU1pW7ibK4XtWg5UMClstB8nblu5SV1iatk3B-L8HTItA-O2Rlx3qvk6tvVQ44uABwfQTAxyQrxUwO-bG8i1AGjrnyxUd9m5FQfI8lpBGN3oY_AgWCAwtcq6GS_6SMiouNv2j6LTMfKhYxOMMgQbo-G8ISBfR90wsE00dqeeVJmWNxdlprOmAMnRut2nybO3IC93UEO7RJLFYNQE33Gyuvfiyo0L68BM6lkMK_Bx4AAiowuNbjh2lT9bDJztF6OKWNffJhq1AX-9vy8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇪
#تقویم
؛ هشت‌سال پیش درچنین روزی؛
ادن هازارد فوق‌ ستاره‌ بلژیکی چلسی این سوپرگل دیدنی رو در ورزشگاه آنفیلد وارد دروازه لیورپول کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30496" target="_blank">📅 19:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30495">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED_EKO70T3bOSE7_qvxspN-1dwemei5jY4krxihXNdYB98xpPibYvopMQaP2M97J9pgHu7WjXesXxq0SDdRnTyenP5KOvVpoJCe74rnoSaWFdyD5q0wclTVWzjiSSsJ02TH08KPS--Tl-qbuWUdeGXjYbCtv6yyKJxH9zRa2w_zyj8Viee8JiDZx3Jebj7Daal27WwXqwmklQpaDvpFkmnO-Q8i-v4fZdLLNnu-atdkfJ97r54DkC2EWfLSNuvEji6y98jV22HNYWqHUIOnTjVidwp5Grn-FQ6aSCTYnL0g-BYMq6PaJ8iMqa0Mf3w9A1jzNaHjUPJrStCqPsS3TDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30495" target="_blank">📅 19:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30494">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇪🇸
🇦🇷
تعدادی از کاشته های استثنایی لیونل مسی فوق ستاره آرژانتینی در دوران حضورش در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30494" target="_blank">📅 18:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30493">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAbI6ifJfmAHlO2nRyNFYf5FWj3Y4k9KEVyNs02VJEJJM_vcT4Dc0r6d0Vc0Z6WJ9X5XNuFtjbOXAzvmxtxcjept92fHW-3Mqzkfz4zEoGD3dQnrHiTBEQrlLVaj-x_bgTDxH9pOXwNedvWuabJJ43ENFte0gCc9KjNyguBbbabmwd9e7tgitNhMG1SussA9dujf3q8TckkdpQvqfLlNTdsSTUdLyL7Xa9nxsuROwD34xRHOyN7HpP-ge2xoct65vbOENSVk_XSzTB_8EM-xbPscjYYScHcMwWuj8aqJCYoJvPyw8Bh8WgeadE687Fzrur-InMQ2wWyvsCMQy8m4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30493" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30491">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg3aLT8B7IL6k2nYRZm9FBQJciH2P79vgLQB9jtAqPZuHSF5TqaTUx8Agx1X8m9YE9A-4tO3GRIZf9BVzeDjvc9_zQu0wj08Lk_1EkzwZLbEo1Z6pl3XT4ar2Kd6H5Z145RlbuCMVPjseXGUMDSSRI6m4n0XDp-KWDYW4EJKV5K-htfPB3DqPXknhf8B2giuz0qRNmSQrl2r9ylhOmSRCzP3Wyg6bTVca4tcF5CLuHka9vqaQn7bU0j6IDqEvdT3YqjqPX5D0p-YG8meSlIiV9dyiooK8xGjK0boSJrltVD-oy1vkXZnm4sWfofIgYPE_wtRgEI6cRIuevZNxk1v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LN0mztnn54mq_EFbb9JePTnc6MBVF4hxwmK4ofwxALseS1zjCDfhvsNirUlbpDQthjyReOEpADbyofsyWPDjmVasHHa_fDpC8bDdpVh6TtwZOqDT3ISfigYJqJHs4HoVfrjxGl2s15VwOnnA-xHqH9fMMxTTP9m7eveq55Q3tVdY5P4QZ7UbTRxEhfeaaLSwCQ17EdDpkVp_sZvGaEMhMSnKLZejxA08pvTwj-M12lhvgJokz7jwHkTtwynlI8_qAgSXiaU_TfDauoc648SAicN_slwogSS4U9AnoHpu7oGMKyVJVhsyH6Y0f6xVyFVJfxfzoq3nTrzoWDEVUlV7IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
رونمایی باشگاه استقلال از آیتک سلامت ستاره جدید خودبرای‌تیم‌والیبال این باشگاه درفصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30491" target="_blank">📅 17:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30490">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV3Yd-WsNkNoQzcoXo1Lchx10GTeZRZXBDbm5A6XjAxCCd0ojtWkfOVq-ToJUR-wkVQRyC0sVn2JWcKnH3Yfjt0P0zfEwl84roLSoyWd0QA1q1Sg9YrHrIk5bcQ13_OKVeIRzNRxcVVztu9482dnqsotPXCQqOtwKLqxVFjUdalhnwWbsxEQHCBGGQtySMZ0YlMrFLpTvyu9JpblQqMfgl9aprsqNQ0n0An1wXxqe93qM1L-gNtUIixgThsTjz7szM0GEdbo5z4Q93n2--Ko_Woj1OnOVeA8IeGlbmQI76LAdzIYyVeX_IgnuUcxFMvaCBcQDFMWpo4FqeCgZfQfjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30490" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5roCUt0B3pT8dyjilvwoaO-PWklojVQkHjXUYadwUIFiXYuGpQYOyBU7b98dLpmQvnSvT9lXMXk6xxNHrtzQ1ZWIJSABSuDGFitEvQLg8Mz8UJHmGEDUlhfEEJyC954vwp6BDZpEYQ1CSG_dnoRJ-T9veFfcRR0QhUPrE7CJJe9TjqkAQZEXPSbcx1ZAkyJheZBs3J_HGjGg86YE5Xp5cxiz7O9TxhTdN8ssogKSB120KtGO-wUrZG3eq4yEKHhRPxxRA_j1EE5pziaKC-f_EcvFU_M3yj2mv1FqVCSmA5MTjeLKFfdc379O6k0k9oc1m5_zWwES564k0sq1oEGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جدید دونالد ترامپ: پیشنهاد ۷ شرطی جدید ایران را رد کردم. مقادیر زیادی نفت هر روز از تنگه هرمز عبور می‌کند و شب قبل ۲۹ کشتی از تنگه عبورکردند. ایران می‌خواهد تنگه فورا باز شود چون خسارات زیادی از بزرگترین محاصره متحمل شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30488" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30487">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_yUByA_N8d0fOFr2gLvVeOygbKUUeproHmgpqIeBEvLm6CV-S4P4GrY1j5V4mdTHR-QV7PxSHm2WoMyijyPKniJpshYaWl4C_iMhy_7VvlpbP8eS-0AfS3FlVFr9eGXDw2kukgmzJiJ-UdVmKexSsk8qNDwtKGYCYn03y4tgsWl3JRlwfEwe_CL9PzUdttWsi7gTz5Z9kCeW89Kb-YA396dS6W5ngtIKTnRIkcLP1mDIV6x6WytB_Vt5lcaq9oaWw7T2PPVXbyuCAnNxP4vHW35s5x9yk9C_TF0SUm06Dyi2XVpoWeVW56kxiMgd_-Owkud_FBcre8rtZ0Xv2Q0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره: من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30487" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30486">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC-sivyCsdULjK8eLnTwHqZjnJX50B3OLXiOlKotpijyG1-Y2M2YZCCUa6cAhnY8o1sfGTw25IvucP2jZlmVzmEY7LPoWm-sI1CLi8wkI37Xv_TgWMoe1UpI08hr5IGSQnMoCL5fXsYVAGcDQynHMSGJbxXoCPGyGGfLiPx0Piffqnbm07j3akNgXNnI90SQwAfbcgQaBOuAWJkaBvumvh40Eq5MCJPmQrhwTrmvgoJpWlzADa2GuzjDb3DqKML4Nnc7jf6p4S6keY1-tTSn3a4Rcb_U_ewZQ5BqyroQGJ0V0LBq7rLTL5bfp4u9T2qEr0KLbMUfRbOrsOgdC_yfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30486" target="_blank">📅 17:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30485">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiooHh_Z3WQiGK7Oa8VC1P5mR7vC5sAj1SnHhLdqr8BBUo6ABhG9Lri99mr6CwiBYTgn7A9H3SuXpd0D3HJeyzPwPWc9Zi9qH1heAHW6WrSBDe2m-675bIverVinXPinzFTwDuVmlKAnFQdaKPRL1JcvzTpLKyq2Pa_48CBthNKxiA0qoxDXU0NcPmoJR6c-w_y-V3d-1wtHZmjMBJvlAzuDVFvkka9GWbIuYyrjrFEM9FpAFSr0owHUGYMTxmNw-dNDcJmDN5kAu27i0d7B8JR9FaRnq1HZKFV5HMYt-GpOleI22fX-f0FYuhlTm4u9LS2tRmXiMyHwAyzM2i6hfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار باشگاه‌فنرباغچهه که امیدواره هرچی زود تر انتقال کریس رونالدو به فنرباغچه نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30485" target="_blank">📅 16:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30484">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQH3QUxY5RsWlc5HNS-Gvn1s_XggF5U_WUkR0MCL0K7BbqG-zqcT9DmEfoYsaNPhrfk9nPVj9fqvfFoB5BTsnoh5VbgcSbhf1Het1Zhis0YpaIQ9sru0Sh6SjkYKnc9RDtJd8FGHfeLS9HN32mpK9RSppIrrpgDUkLY4AxBEgaZOa4DE0KCnh_6Ub60aWUaHEAL8HxyVosD9xg6eWPrG1QpT8-6iw7x1Ku9779itKmajOzjXgQhRCic7tQGTE5Lx-xCJQRHwXlwNktb5bbVvKIRCNSGRPnC3RdJnCZWyY_w-UqLAd-ngWdNO8YeDD_VnOgeg2TnJfbNziV0Ak2jAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام حجت کریمی مدیرعامل باشگاه تراکتور؛ معافیت تحصیلی علیرضا بیرانوند یک ماه تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30484" target="_blank">📅 16:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30483">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHuIG5Ink5lj_m7LGvj2Ms4zYkFiLsTBLBuTbVtvn_ZLbD8ilyXzPsKpb06TUYEX-fuXG4_6h_vGHUCvoQxiTNLmC7z90xmgHA15ckZl3gk13aIA3YeSSP3JL01tNyp2_hWF2e8Ej_7BBYYu1GEjFTuDVVpBnBtDt6ht4Zqh8WdWbmkacQp25Gi4bpDZcoP5BGfdKyopP2Ro3Gu7FhNYN7TVrP5369Ua9s0AEpLENgararLb2Xod6fc2_885yQN-L1maFRALps_jwkV7khyTOwMpyuPJfalRLnghID-Rnj_nqBwsSTO55jn2XzK0keyLPWXvH0aKQcpwzc4emf6UKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
👤
مصاحبه دو سال پیش علیرضا جهانبخش کاپیتان تیم‌ملی: بانهایت‌احترام بازیکنان ازبکستانی هیچوقت نمیتوانند خودشان را با مامقایسه کنند آن ها نه در لیگ معتبر اروپایی بازی می‌کنند نه عملکرد خاصی داشتند، آن ها توانایی شکست ما را ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30483" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30482">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNHw1aAVgpXhFfhJyBlfoNUGFW0OzSpwcGGiCn3YW_1PtvN8_ScpGWNiFYTNOkhW8A8luQk2TAVuL2l_PHtxb9mUS10eRHtdDpBpDRXacNY0GU5Z4TmgXeOe_GlSoZNi3HLv8ZMr9SfCl1bGw5ZDAr5exgWPI-DIFYQe3slspBWGVwa2G4mVm8FtgNWNzBRG6Pw4d1kIzzUZ5Bo9X0DXm_5w7pZ_3f1IsHj2FzKYgYjVmwUa9b_PePE5bBu2mJGbD8Iz8CxkaltRF1_dEwLbCE-qgNKdpP4aHzk6sS8ZCg3ss0rMtiM-bDdSggCgCVIEvcMYnJptcWJVBJGrEWZhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30482" target="_blank">📅 15:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30481">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpn6ZpjOdzXzD7-YpTTE1mNk3t1QOd0BKxSjdUMFPJLSctM8CjxKKKbitjAk5v1OrXAGx2I6kZGDrI4rXHLVxH1uZX1BXXPgLou9VBapD8vVc9f_VEND6tgwuMHeJuwL-yBwcclIQiQV_XN4BdWXOym5KCYcNStVp5_f2fYCZQgYBhpjL4gJd6hSGTX9J-3FMK5j0pB-0ZgIKDbQSQxQdJx_wrUKnHyPSYxtcTiZBBcsSsqsGdiypnQnNlp7j0nErsC2jRTAy8f2yyYoIqhPrD3XGUx2uGstIbce6qS56XfiR6bhlIl-ocVcmhZOpuDj8p1xau9KNiiOYTOu0Yfo2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30481" target="_blank">📅 15:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30480">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛
بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30480" target="_blank">📅 15:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30479">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af5A5YcsCTe1HUS1I3Turs3k4hU35Crq6ag2GqaU-6VdjyYradpFaX1f8rq3Jqp9LysS5g-OpGTwSsmzsExWJoaubUB7Gqw5ntGZiV2RBM0-mu1N-RzN8j-JaPFUYD8o3xUO1MCfN6GhuazRZoUTBqUMp0sJail3sOkSnUC4nZgS0CKtLrV2CYvP-k0_ur9jERz8qO2BggJH5JFVBUrgrB7u0-RlsbJATedZNtMlvjor3B8AJXGPeFNeKdONaWp8iczWPq8qT8IK_4Al_FGysY2jVr3MOmyQWt0DPCHHuZ3bJoXNItomT53DBZxjZDoGn9R2gCrz4rWfU7siruHaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
مقایسه‌تعداد جام‌های تیم‌ملی پرتغال قبل کریس رونالدو و بعد از اومدن کریس رونالدو به تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30479" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30478">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcFV7W5GGSHfJCNjmE6K_5AXcoJM1d5ZxbgnyEAx-AqlYtSZKEhckJDxggrO-mkMHSvMIbHcL8EEXZB80lnCSakQstXh3l2SGZFEQlC9csj0V3F7dX90ISyJpxKAl_KTrO_bqp9UsF36fH-vEiKB_13sldIdOKmopqNT01dmHj5hxmQ6TjVL2HWqV9DCxR5H3_ejpQiCC5M0RjTHXNFr_UUlB5tbN0CveAgAzoC8lT_4UwlX_OIovlmrnKfihsJXN1GFkplneSSzFU6d4G4mlceA-DAecwSC7oqZqd0fJoonMVPzcFAwEbU82SBM-vyQLO0hfAI6I-wAfo1pefk1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30478" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30477">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXVPrd_jzvmTt3RTKhFIPfEWPE2zNM3zyMGqwhjOTQvt8-yAh7Ai4Ebt7ZJSf0F_j4yGL7awf-nbgTM8jk-7JrYeFYsnsouKIfJjS2Vs8yaOyMQSEKxjC_YEg0Fs0DOfS-X5mM0YphP3LdZj_WqrR71_X4pDu_7zblaqmbdqrDcTSELOreuoXbQtL1bYEx_K_8H9aXXXe7Tp6kPhhSQg1dIqZ9Uf-SsNE9dxvcpzQxjGkv0EqtBNW17mhC2BEJYE9VsmsTf04dMqZ6h9PZbOxcwKwfIbl7tLvIZODvr6QX_y7nSJN7X1XVssr8vnibtSTemYOu61SJ109MmwzZVmGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30477" target="_blank">📅 14:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30476">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USHWxtuDroylHAab6NSFB4VhXb1OsJCRfS9t6a6IbqulKh-Fg1FgsSyMnFw21S2ck9FF6DFVEskSURZHYq8A70xGHPr_NMBUYyCFZj34KSF3YV6cdVWLrEvM9sHJ17yKlZmevWzT1rWiCwyril7mRZQdWY8vrHtp-qBFnXz3gmpx8C-6txdhHusTFb5s_xNhb_z7EopZduN1RvBXVafFnl7Ow6nRqtWzRDs9TMeWBIhkklkvb_EwJsMO9mpDIx7aERDiRy2N_UZzVv1zBkNJF2HLLmc0lig5DUB3oZUHmU9aFy075HNBdNM1LEP6LTlsheUKGlkoR9tgxTGHHJX7uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کول‌پالمرستاره24ساله‌چلسی:
خیلی دوست دارم که یه روزی درآینده نزدیک شاگرد ژوزه مورینیو شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30476" target="_blank">📅 14:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30475">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📌
قیمت روز خودرو/جهش قیمت خودروهای مونتاژی در بازار امروز
💢
آخرین بروزرسانی قیمت خودروهای پرفروش پلاک ملی طبق استعلام از نمایشگاهداران و دفاتر فروش خودرو تهران،/ ۴ مهر ۱۴۰۵
⭕️
این رسانه هیچ نقشی در تعیین قیمتها ندارد، بلکه صرفا اعلام کننده قیمتهای کف بازار…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30475" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30474">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-zCDaLK5rMy_e-pk33vdYb8SwopoqOLDBgsg6HnhwVwCbcEfW8MyYawscEajg0Lrc7ksLPwNzyMAlKniCe7dVJLgx56wBaMBbF0rb-43oXBBP3FrsAfkI70NlYouyNfqks3xn9NP18wRGCaVIe15KzZ0TDagk9DzosiRmiY7JZCve5SHnKTLLmHyIvadov5NDi03_WWwqOXYThoumjtAInIuWswWLMpmrKKGywhOymt2BgSfc9ABy18fjrO9kpFbs1Lndr1mgD4oLCaN8nqnhuqd691nbZJ6geAxpoNzAA7yYIPX9misiofLBh_k6tJ7DMWHA-7e8xf5xy2hEqc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30474" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30473">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIa9rh6lgi_pWyaG6Uyj4_QnDD_eI77fV7uX8ZOBAkeH59HBY1TaG26rvOj0BUEVzAbrs0sTdsXFSCPKEjLK3kF1_r0NTD6NYcLjffLBhxbi7_kOY2t0peD_iONnjmpdlahKPA6idDcu_T_j--E0XFKax76eWO9ao6mgFVztSCR3LnGmxDfW2rT6aIJz8TDqFiafMkjNa-QTFqHP7qF_RPfOIRp1IQtIPNCGSqCtYdwkRprrpHD3r0HRo0Ttzcay9DeuzN37VMJLFC8K57zZeX43RSAvHq9hOPdwVJMh1Dfu9BXc95sQ1cO6I3hBxbkwQWhhBsdV6qLmvH0zYaKvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🟡
#نقل‌انتقالات|فلورین‌‌ پلاتنبرگ: جیدون سانچو ستاره‌انگلیسی منچستریونایتد درآستانه عقد قرارداد و بازگشت‌دوباره به تیم دورتموند قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30473" target="_blank">📅 13:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30472">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e94cf509.mp4?token=EC-ukQASjMSnl-YEtKsh9kSvyH0rsgNXpt3bVj8jQw3wf9oDX95HcXeLm42GjxMUDmBGWZtVWULNZCGYZ-sPbhXSzwXuBqRtLom_VP1ihDryw0oJ9wsm02z7qf_GOt4mcmY7k3CM_piKT5QVQfmwaudY857BNznz7Cq95zAY-WNh1XQv1YPXOad0VtemlqzoIPGeJRitVbjx7TaMsQFZdFepZFKtkh_W3Bg5xfRar7nkNo57IKAun7mGjE6s0RUl5ZyagAQWKCJLXjCfczBWHuCafigSLiz_oY6ArkgejbdbfUiznqLcx6nMSX_MMrETGdIp0wODXC6Qo6Yo7YZboRIvSxsZxpaIPjBamyzn-A-91KLqFxLWRpcUKN05_KURDU_4nSfsd7ldZJIVJ6_9wlHzap_ctiuyL23UN2wxTv2Ed67jBZJef-HDioJo0ePU4DJDPTZqsh2OcQVqTzUHakAjgQoClkAFMliNMd-F6GNJi38IEqnpaWQzGTU0K1oblOrTcb7uk6u9Xp61Kz-2mFbXQafylj_0icoaoEVL8iOYTMaxc_G1SpSZNIzjZDkU4fMJ9RoOTY-jBdeu72iISAgj96hWXk0el7q8GDxT-y9fKsqL8P85WfTV7CuArOGSd6T9jKsB4_hmP0YgNdx5rE0BGDI6voUGMJ7VvcTBt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی آردا گولر ستاره ترکیه‌ای رئال مادرید از مصدومیت کیلیان امباپه در جریان بازی شب گذشته دو تیم ملی ترکیه - فرانسه در لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30472" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30471">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQTDJjHCR9xZGYs7pJxtSUbXhMP1GWNvy3XIjRXZEv6lTyPN7yi18GN7HOA6ZtSRV8C2HCTPnNGbZnAaKp3ZFnbQxnXhkoxWQ5R4bZvOMrArkoCk0nL2VOIqCEacThhMb3-BqsSrIFbe7WXhBEQOWkMv5qeoci0oBdGw4WEKkLe8N3gu5D8ARAoJcpLlC33khVqM11bzi_rtpWEuPXzK4gxQjuXS7SFaM1B8puQXKVMbT24mZKg3cw-NKMFuxrI5Z87svYeVwofFwtZq_VpP8DPfJ7vrUSgmy0SQ5AS3SuNoM4tAjCQET4HmRvd6QVYZJguxKtFsQ_Z_JixyxQrq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30471" target="_blank">📅 12:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30470">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWI77XTPzH9cMwdPZR5wNUyIK1lWal3oK3QYs5c7zMRlEWYA41XvwyKsyPCqXEdU4fOYgD4HNG3GwAUJs-WeeY_atx2OmqGzz2tkgr2cWeX-z-YxI5LhDqeOebOrSlY8_LQY8I82Oltyf2nSPdu6jhZb0I-_hhKF-TuT08ruPWmke3TNUtReE54wwYUyF0rd_hRaCfaSE6zp1qbG9ewgnrlNbn1stUGLhgqf5770ePM12PMb0NkHMMt-2nb8Xdo1Dc60wzyhWgoPWg_eGccmYYoK5CIp9IgJIcahdxmOClWHO_GlECa8PV-gh8v6tFY9aNzKRCXBCH5mODAEAba26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇹🇷
باشگاه رئال مادرید برای تمدید قرارداد آردا گولر ستاره ترکیه‌ای‌خود تاسال2032 به توافق کامل رسیدند و فوق ستاره به زودی قرار دادش رو تمدید میکنه. پرز دستمزد آردا رو حسابی بالا برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30470" target="_blank">📅 12:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30469">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWbo9fcojbNGxB0XZ_ub-OAhJoRRO_FfzhGVu8ott5-ByX0vOUUPMvCr94iXH4KlieWNp-izmRG0mEuXOW6VVJMNLumwBbzYGZf7Vs9ZAWhbwCSX8JwoWz-Omsadg1bRqMlCHhymiVo85teK9GCUk24_Gvo2TKLFqJI0vrTe0Lai3FHE7eZyqQ99KeDpC87sKBG3NKYG_-zvMsLqchdfS42JAEAYaQc4Aknbf46tKirrDXEex42uPwBXhS9vuYuTNAkMVGREqTmECVr_lxbrJC9Tn0qdTvF1anypn8L4-Pxw00fuX1JaCdzxVWx3NTyrimUlZ8fJbP3KDNzNgvBuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30469" target="_blank">📅 12:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4b13e0d2.mp4?token=HOnyAVdNRktEj0azqwZT0qqOXFIAarlKq1UKTcllNTg0M1XC-9M_6L_bODCBE4jEXuUAgGGBg5jvVH7bvL232pKrFDV-kZ2vdMAHNRx1mAZNa59Fucmg51rvssr8cAcprA_tT6yZB1z0yk9WtjBrTscsO2jLSvvnusEhu7KNt_s23Ze5-fGx4GAZ85evZeGdQ8tOwW109qYcFhO4FCjj18NVBFHtfeixteDLb-hRiPw9-6HzkCtFat-uKIdEMV3mE0fCQwISRjPEeTQ0GzJOQG5I04WNaQvpY4sF2LS6lPZ-UtRavhiqyZHqJlJ6BU3mEZEGYTjjOO2fsi7RvcXDzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
تعداد از کاشته‌ های استثنایی کریس رونالدو فوق‌ستاره‌پرتغالی در دوران‌حضور درمنچستر و رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30468" target="_blank">📅 11:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87985ff1a.mp4?token=slWFqzdcI6z2_0EShEfBdgWJYY6Lid7LGkHRc70pV6InPcf0KYsxzYj0dJzgLGz_sW1CUTytbfKBqUCA9rqWHJWzPymtunb8fxaDiW9sOIn6wKlev4b0ZW7uPbGp8cmEtkCyyps4sArTBrHzzRG9y3QNUjNu55oRnAKwpsga5F_tlEY0rVGpWKyOJE7SIi023CvUvGZPT_RAAzS3lghXeS1jZm1h3ERDf_ZhHy1GjDpP5zN-6zgVzjm20q4jJgBiY0AXBPq63I6rFtaiCSo2twECH068rw-TbCn9xkrQUy8RvVnDVomL4pWpGdW3OWQj3J-5JnmfOySZTGxAjXIbYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
چهارده‌مهرماه شاید یکی از آخرین شب‌هایی باشدکه مسی را باپیراهن‌آرژانتین می‌بینیم. شماره ۱۰ بعدِسال‌هاافتخار، جام و خاطره، حالا به‌آخرین فصل‌ های دوران فوتبالی‌اش‌نزدیک‌شده؛ جایی‌که شاید هر بازی، آخرین قاب از حضور او در زمین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30467" target="_blank">📅 11:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30464">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60d4945a7.mp4?token=VYVnIE0GdBzAQJszV-NEmd3T8drTENTasLg89ZT-5zEUBSbrDjcKrZoj3w5rxYNIczsQK6H6NmxqhDCQHeGDewcmR8SY1U8wHu4v5TOmvbrCwizD8ygo-zKDPWqsS3cp04DM2Kc1S9c8LNyVuaayrAMODKzfW8dkQzRe8ypLv23vixsqXXlq-SWam_VHqFFPBZDZvykSAa_TnkDHG_WwIb33N3EvJFc4X3ae70bOPfKRyIXpbPukiKgQOu4zlmF_QaliD2jYO-vUcVyETKR9vkrvaGoY_HZZ1shnWc2GPTb25gOqLE3y4I-Zr89P28EOGzw60ziKxcwXK09Ms9ICfSx1qPcakrLqllo4HAqv1nBWrcjQTWitaF9Cj5AgqSqpCYX0tcvN9ArdEBoTthba_YKaVK5E1EV1ytGam5wWv-tlnFBGCUeIVxXD1k-I6kbepteUGueys6Tbna-KJ2vHOnp1yejFmh73A1ko6hbJSPg8LOpYG1gKvPcUyhITZaBKszqt_dAXevo4pY_mly0upnSKnYEE7_K9Cnm8vnt9ih7gQR8ZdhLio_n_uFX9xQJpOaOS5jOtDj_rhc2xj2GDXU1GRi63JAosCpeY5NoPJ8vDJ_NyUsWrKcJ41MOAbVmlq1eSfnU-0Ntu2lr0-aPEHRaNpQEDfgB35Y2RvFDM30c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل‌های کیلیان امباپه برای رئال مادرید در دو فصل گذشته بعد از پیوستن به به این باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30464" target="_blank">📅 11:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30462">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvqJoTWWDWWv6AhY5Vt1gO36gmTb5B2-GhWE0MS5S8fYFeZYSX33e0quIeVMAWZ9MCFzjlZxyGP8jVV4vyzxNDyHveUUngvCAkMZsw-T4KdPEFnCMieWgZS_siak3fbBmYv-CX2k5bGwSYBTF2wnCyxh13uaRmscMQ5tN059upZIhUzSYCyPxxDznLmW4CTU5GXWIsSFtrwmPALm_gya__YWjDSghSJSLfZmzov-HA5O_Tji60wpr78m0bvndqzImqoD34RQT7TNgDHREiEqjMSLDSGUh1rFRuOtZfox8tjtLijxhti1bJqKIZksdZfF2uXjmtprdpAf2oz4bAaTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0TplsJ27ZIn23ScXfZ9FirUCYIUBRJgzftVAViqKRGYG6Frt5bUJDRSh2Z0YPWfBpMzq9KdFpLkZvh3AR54JHMJXJu3xVv7bII3ilefxGu2zYItGi8K-2x4uehZ_NCVJmVaunhjUywEmUh-OE4iBDIfxS01ZHSEYdtKKyrmNOpA6LP4y0pqRmxEqFDx-agKQ7L8BXQs4CGbTjcX-vx5NvF8Utkl5Na3wvE7AHeVBuwjc7vjJh1I6--V2efPCsSxDrU08C4Hkhh-qJAmEWUbzPUcgQIc3FoMo1G-fs6FH1dZiaJBEAshyozgsSGYrE_4mcnUWsICLZ9eb1-ImnN1NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
برسی کامل‌ودقیق سیزده سال ناکامی امیر قلعه‌نویی سرمربی تیم ملی در رقابت های ملی وباشگاهی؛ وقت بازنشستگی فرا رسیده ژنرال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30462" target="_blank">📅 11:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30461">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌استقلال تاپایان‌هفته جاری 400 هزاردلار به فابیو کاریله پرداخت‌خواهد کرد و پرونده این سرمربی درفیفا بسته خواهد شد. نظری جویباری پیش از عقدقرارداد با ساپینتو با این سرمربی برزیلی قرارداد امضا کرده بود و حالا بدون اینکه پاش رو تو خاک‌ ایران…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30461" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6160de2528.mp4?token=Bnet27vTmjBKSRyvH6hWEa-1y-m84V1Dh4aLmAUFdewRvPki-1VD6e7FKGA5wvFnB1CB8g-O3EQk8Lq5I4Tv6MDH_eLmOmF99MJw89i9mPmW3X2hTgTVA-0YOplXoJthtAae_WoSsEp73QJebKc_w_vC8cx2UZ1bxGC4At8Ww0zpiYKs06k7sMkdYuAuvX3Rw2qjjN-ch13N7Ngc1h4L1bKC5hWbu8kHBdGk8gEI1wqOhPkA6XHpIgU_nmOIPNUGF7HfsfAmVMz_F1R0zsHbFNoKmDqVriKvscmG8yOCH-dGpOC8v-N1vs3Xjm1Occ9tUGMPe-aGiG1l1wBtCDvUIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6160de2528.mp4?token=Bnet27vTmjBKSRyvH6hWEa-1y-m84V1Dh4aLmAUFdewRvPki-1VD6e7FKGA5wvFnB1CB8g-O3EQk8Lq5I4Tv6MDH_eLmOmF99MJw89i9mPmW3X2hTgTVA-0YOplXoJthtAae_WoSsEp73QJebKc_w_vC8cx2UZ1bxGC4At8Ww0zpiYKs06k7sMkdYuAuvX3Rw2qjjN-ch13N7Ngc1h4L1bKC5hWbu8kHBdGk8gEI1wqOhPkA6XHpIgU_nmOIPNUGF7HfsfAmVMz_F1R0zsHbFNoKmDqVriKvscmG8yOCH-dGpOC8v-N1vs3Xjm1Occ9tUGMPe-aGiG1l1wBtCDvUIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آلیشالمن بازیکن‌تیم‌بانوان‌کوموایتالیا با انجام این فری‌ استایل در اینستاگرام کریسمس رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30459" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldxBXFkykF0ZtoFuQy6BLxhuTo4iE9s8PHbHMV3keRhdHeWTAO1SIYxhs7y51cdwWF1JureKiNd6gtK7Nbe_Y64sPbqkgRJ6wcfjxiniFbdLZ6kf3bt59TM0Ga3fzVjG1BbZZ5HfLgdkKjWXV3lRadua7LPw0Q4HMTzZbs43SIG3I8JFjtcsuQFSObU6VY5A9E_bLHPKk1DI7-ibZtJ_ANvS8wvRrunTAm9g7teC51rLKlsV-43sTTPRb7k35ZIjVb0R5m98cp1Q0QqHokiUDTNcjXXJxzAVDZ65-vIQ6hsk9U6dgGkkHYpEL0fAiCpNQE6-2BeYn6Hj-1CM-VHJJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال مذاکرات مثبتی با فابیو کاریله برای تسویه حساب و بسته‌شدن‌پرونده او پیش از شکایت به فیفا داشته و بزودی با پرداختی مبلغی این پرونده بسته میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30458" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0gZFA3AIE4RyGD8e_Nf7D8fq6ptvCPp91jqUbS_pUXohH5_M5guFmGqAVaSQvz1tbdye9Mdauo486ZnbKCUeaQFB60nAIFOtCgbdivR9MvWQfvnay6xd3MSrrcFzMf83txDCrTqw4Nay-pGHyIa7Ol-lU0_9AOjrYmQC7TiD6EL_hvccMvGAX18jqwbhJVDRwGpS9JcqdZWuQd54TJu-5_zhkJvODwIsYBPxC0j_OGMYb145NWW0ktB6WyW68L38VsU6L7msq-uohp64n9PzKSW3MgTP_FrGoFfDK57rHyyyahpahsdnK1zOx0AdWKpRc-SEnDOeqOl3dyiyHf_8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درصورتی که اتهاماتی که به من سیتی زده شده ثابت بشه جام‌هایی که در لیگ گرفته به این صورت بین این باشگاه‌ها تقسیم میشه: منچستریونایتد سه قهرمانی، لیورپول 3 قهرمانی، آرسنال 2 قهرمانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/30457" target="_blank">📅 10:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=tkqr3OII8GEJm6k7dhHCU77wsO0mFlbOeEw4PPprNPJ9In8-lf9cqfPn26uQk08zotJ2P20r6ctP0EQ22QI9dkwr6aH5AD8qWC2jVlPGtmwjW9D-XtMfvut0O5j9QmpkhmbpoVu5gIHx309Ta2W5Z9g9I16ZSIdBpsYrPyy09MDGV2zsueoZMns2AXITCAKNTKJ7Azpcu1Fn3oOih7yH524WY5o2jB2ODeAPiqsSC0edGc2-JWfY7Ho-JBIZ5THDMFWD1-4HhH0P3CWX9CYaPgwOnCHOmViRoLZMW40HYJzsjDraRfgIyVKXy892JslNKy0Ue9QjsVAjtI3iCXsV-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59d54b38.mp4?token=tkqr3OII8GEJm6k7dhHCU77wsO0mFlbOeEw4PPprNPJ9In8-lf9cqfPn26uQk08zotJ2P20r6ctP0EQ22QI9dkwr6aH5AD8qWC2jVlPGtmwjW9D-XtMfvut0O5j9QmpkhmbpoVu5gIHx309Ta2W5Z9g9I16ZSIdBpsYrPyy09MDGV2zsueoZMns2AXITCAKNTKJ7Azpcu1Fn3oOih7yH524WY5o2jB2ODeAPiqsSC0edGc2-JWfY7Ho-JBIZ5THDMFWD1-4HhH0P3CWX9CYaPgwOnCHOmViRoLZMW40HYJzsjDraRfgIyVKXy892JslNKy0Ue9QjsVAjtI3iCXsV-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مورگان راجرز ستاره انگلیسی تیم چلسی:
کریستیانو رونالدو بازیکن مورد علاقه منه اما من در نیمه‌ نهایی جام‌ جهانی در برابر لیونل مسی ۳۹ ساله بازی کردم و باور نکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30454" target="_blank">📅 10:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZVD51zhphNQFrNUWdnKDQTJ632qNRANAI9g4rgQW9b44zn0oXZt4EwUiPTYrrldUTnuOI6z1puYRtN31fmfG8OTg2_9AC0joWNRnxPa5ZPK9UgmlH5gXR_874NG8_LWu0wiNDXdWS78gafSG4FVhBVF2Gf9fRKYnOwQZUxNtM2-f7GCjhsRUNAaPuyHigo9gz4KzYQgHunw6k241wt0eFdbf3BG4CG9y4gt1KoWp1aG6Alil9VFR1n9Jaf5SLylzCtFq6Noy0_2SH4tRincX3c3MQz_go4aaDkVOJC0BiVrlOd82O2mSa5MKEJV_gz1en8PQt3LB62HweHZUs-_9ndc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b295745c6b.mp4?token=MN6TORNuE4dlB_jK2iVS0Jk1qKZbVhSfulmCgL94ge0Brp1pwSb8JZQrPKfOG2IpeJAarIB5X-mtC77CiJY5cVFzflLip7AqFTPEMsZtk9A0TclVtvPHiK3U8sc7ErfXDwh3Lxj0Lmsh1xd5Gw-BGsyw7Z3Vo8OFdUoEPhRBrW2DtkmxH01iAv47vpDsrNQRjQRdfsu3cztw6QprS07rKSBh5QvGnd-3kvw9i_uhxgrzj2fwzxBxtzJ29mwPU3KfdOM4AtmwSoA-9ZAaDQXie3FrecGP2wCccfMY5jSg1mFNL2A5j_jTLJxyHl1GtektcAwk97iT9qkl2ZHkRJ-FZVD51zhphNQFrNUWdnKDQTJ632qNRANAI9g4rgQW9b44zn0oXZt4EwUiPTYrrldUTnuOI6z1puYRtN31fmfG8OTg2_9AC0joWNRnxPa5ZPK9UgmlH5gXR_874NG8_LWu0wiNDXdWS78gafSG4FVhBVF2Gf9fRKYnOwQZUxNtM2-f7GCjhsRUNAaPuyHigo9gz4KzYQgHunw6k241wt0eFdbf3BG4CG9y4gt1KoWp1aG6Alil9VFR1n9Jaf5SLylzCtFq6Noy0_2SH4tRincX3c3MQz_go4aaDkVOJC0BiVrlOd82O2mSa5MKEJV_gz1en8PQt3LB62HweHZUs-_9ndc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این چالش عبور توپ از اشیا؛
هیچ کدومشون نتونستن کامل توپ رو رد کنند تا بالاخره نوبت به اسطوره تاریخ باشگاه رئال مادرید رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30453" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrhjC5mLzpV0GLNZ8Sr3npR1l4R2YMycPcfGJe8npcFghjhwu5S0KwOnrAA6Gff4dG1VVzf33LbF6T5XFFSyeil2JdYIQUIq0fGPOHtr1pRKjrc80IguqcG0r5cwy38cBSwxslhs0MqdbMdzDK7oZDFfDa6IeQWHbl3NbARRNzT0QtRbvzr5AMD9wz_hsgpBlXcUQ8RypeTVYBW_5ZF7fGBd4Y-DAqvbZqTiM1TA74kmONCS51_KGx8m7YNRdlg6St8vV7xIrdz1pTk66I1rlN21of9qRb0c5DdQSCo-GlAvCS4gNqoX1anS7Zt8DlFNxF2j3JT8lI8mdGHOiVf3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30452" target="_blank">📅 09:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxiyEPxPsVwNk2EYowr3bkgJlGrdxiqzeBfzynUndKwKLGGehg1zwQCrJ99ls7fPZ0wB-n4SZDznQeDKevTxzPi0cPS0aqYP3HhYqtru5dMKLBD4KBpz9K1Q8iLby8kqfY8TYjrItP8aV2obwYkJsIYvDs1p0QnQZzq4GHmKIq-pbIfu987DRazKAnlDOG1pPRzE7siAjQofEEuAr7TZUzJIMG42RRBe-kQIuaSA7UsJwISJWri-Zmdybm0KmhMaJBqVCZih6gOMf8BDIvRrTjqyjxCjSGn3C5aclL6IxNmOEvTU1cLgOKwtKOSkUUJJxofojYqPCxjisvRNtH1L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
رسانه‌ های بارسایی در حال مانور دادن خبر انتقال ارلینگ‌هالند به‌بارسا درتابستون سال بعد هستن و قصد دارند بافشار به‌مدیریت این انتقال در تابستون 2027 نهایی شود. از نگاه اونا پرونده انتقال آلوارز به بارسا تموم شده و این انتقال هرگز رخ نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30451" target="_blank">📅 09:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ3m2ZuRa8x1BLK8NuhKF8b4XQVmyeH8IFqZ9C4DJyGegS-R-78YZgeCnchKkMCaMFYdaXiy0FHE1JSZtUaYjEdaxQIbeUdc5y3JRamPPfZL7T9BI6RlIY897E_Ybkp7EncPq0SvdvqbRJqqEaGfpQAFkfvYMuKPZSslXI97TTidSlrgLojmxKZwK7l7fiC_Gxq1DXIdCYnofivkx3d2CqjGhRdS17Yn1kkLZYuKQ_7l6q-jS4PLrQNxIqZKBTe0Kh7ml5YpQ_-T5H-_apD--D5NkRDDM4HZUUPxNLRuPrtQayUzjSYGKuseo_LuEA_5EBFLLS1w5NaPQ-wpkZy65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
شوک‌جدیدفیفادی به مورینیو و رئالی‌ها؛ در فاصله یک ماه تا دیدار حساس با بارسا؛ کیلیان امباپه فوق‌ستاره رئال مادرید در دیدار امشب خروس ها از ناحیه‌کشاله‌ران مصدوم‌شد و زمین بازی رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30450" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=NuBZFlaB3frzwMTU3dCfeyq1XKr1-9jBKlhUCGC53Wr0xV4K0xrj9r4_Ro4pA_GL7eOeAZnlCGLtsIYkstbwaf_eXTsP6W17qzTbnqPSzSvhKpsq6-J8DpfkG2BUPGlGJ7A6q1acUBy1AKuC9Q8km0PBkNbJUqkwdGusTsoS93puUEXlJrbFVsdh0ztKM8eT0QvcnpOSkevonqfwFNRGjEGVNoP3_Gi_NvO_UhsDUric56pLoyH_PX1oc84B_2Sfxx9VBiUAfHvyqLJD91A-CdvMM49ozl_jJ5yGT1YKoJ3D-DVuSqKAi8Gv6Fw2f1llHOMLsDNrhREj-LCeLXFXfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34b91abd7e.mp4?token=NuBZFlaB3frzwMTU3dCfeyq1XKr1-9jBKlhUCGC53Wr0xV4K0xrj9r4_Ro4pA_GL7eOeAZnlCGLtsIYkstbwaf_eXTsP6W17qzTbnqPSzSvhKpsq6-J8DpfkG2BUPGlGJ7A6q1acUBy1AKuC9Q8km0PBkNbJUqkwdGusTsoS93puUEXlJrbFVsdh0ztKM8eT0QvcnpOSkevonqfwFNRGjEGVNoP3_Gi_NvO_UhsDUric56pLoyH_PX1oc84B_2Sfxx9VBiUAfHvyqLJD91A-CdvMM49ozl_jJ5yGT1YKoJ3D-DVuSqKAi8Gv6Fw2f1llHOMLsDNrhREj-LCeLXFXfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش بازیکن شماره سه تیم ملی کبدی بانوان ایران بعد این اتفاق خیلی خوبه. اول برگاش ریخت بعدش رفت ازش عذر خواهی کرد بلندش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30449" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRSQGWuxDY6YPO3Duvb4lIjgtnOCHujl6Ogfy9Z3Y75EtZod0ec7Z8z4yRZPtaQZYzzoWcqMZF1TA-xIl1UbiiYP0dSeMDIuvmWkPvM6FAHJpGRybqILIELvy-PIugw-EgJC8rS8CBVvVRHUwNVfFzH5yMwHCn5JcenOcEUc0AlwyjTUCBftmxlt4-ByhHTjXqWbOnqzLzyovmdkfQACZttG5eQkfkSi1ujFy9Mx4FbFDafGRAbyT3Nx1fODAMfmgxUEKgQVmI8ajrrsd7WP_j-_CkeDZsRSU74SESR-yhvg_S0S_ytxpcklKNJDDT1F3zX5mvOI4tZvKQvNKtZAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛تاکیدچندین‌باره سهراب بختیاری‌زاده به مدیریت باشگاه استقلال: بین مامه تیام و فابیو آبرئو یکی رو در نقل و انتقالات نیم فصل جذب کنید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30448" target="_blank">📅 01:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtxosaN-xIWMnnddaZmwfQ4EXTXTBdWto0g1mSOAD53IqeRphBog_BeioZow3iJ5k8RR2YrsBI79Ts_9yOjMApoMIVH22JMrrmdChvi2Jev_NA4s86Q3RiW50jAcTbz7ejS0uI8tYbQts26N_6a6ck4xbZWsTcNZlrtA-jeiwsObOU6eF_Vx9EaoTMYje7PT-vcSZRP9Ya_S3PV3eDxubVRCh7BHX818deC1h_SVLVKTG-Q49Mh3uxduJcDQNPv4rLLcK4_BWyEzDHrZ3fNmCyISYdQfzrde2RTTtZMI8rPwB-J6KjOaRoK-zQ5el5bx8Pa1KgiPIff0tfEE3IDsQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ تکرار فینال یورو 2024 با تقابل تماشایی یاران هری‌کین و یامال در ومبلی لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30447" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XocCuFap9lodM3EJnPChzCLdtRxLGB9LKR93JB9ZDy9H30nAq8iaYe0vm7FB3FokTO6SfYnaiUrL35Gi00VhMN2XRRpN3h4-vJVB4PZYDIvsK4oKx_NELBuanCghodBwnV7S1Bs268ajaXDJcA9VXutDtf824HWxnPACDDZydOBBRXsdYhQDMwwvi9wtJENwuYaHewS0fhPfsJsYDEhywyPu7lgqYQgoqkY_5j9o8gFCt7Kp6htRjpKFRMJdvhOislZLo9EEyV_0oQgsSnDnHYoc38LlpNzo9MDcOv7Ck4h8FmU2xgy7kAJdcqzu4SjVHxerZteqrxh7e-EibmasJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد فرانسوی‌ها و شکست ایتالیایی‌ها دراولین تجربه زیدان و بازگشت مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30446" target="_blank">📅 01:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30444">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvXDQIYAQF4i3XJlAy0j-Nquwz8rLbIhk0pdmKaJD8VjhGheuCsFPGOS6L1ROVzG-1AKJ6C_LE51DqDYCx5_966jMFpPY7L04UulIMvXcaWBcbQHY_GhM-W6f6b0a5ht6Ml61sMEBcKNf8lPuEaMRFTmvKafJKeL5VIP1KXk-Y7PRRO0xHZ7xXz22JJfJK21FJiuvwrWuP8garA9Cs6so_jcXsCaCRQKxZwkRg9rB8ekXWhu2EMNflUmvpxI0Xrt-CjMbM9izf8IbF61D-uRHfFnWNo1TXLZn0sVzeCk34WKOKAQomlsb20GvfXoGsH3MV7jI1i-R793H-w5jDkJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازیای امشب هفته اول لیگ ملت‌های اروپا؛ مانچینی با شکست استارت زد؛ زیدان با برد. سوئد با درخشش گیوکرش و ایساک سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30444" target="_blank">📅 00:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30443">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHwJmohVx2A_uIjKuf04Dtw_iPHY3XTJp5pk_k8ajt3txf8pdv1RqLXkPZXrE-I-Jo00ZGgnGlWh6d3ggvVDP82bn4LqmnWVD1ystLtN9FVaIDS9IGJ-jg8dcEPrpFUQigqU_OT8B3uIuFuMgfoBRtk3GpyL4islsHcDdMA9viFootlRyrpQiedOI4MchJAF2h8gWqRUvzqC7tq7gd6STYKY329rYEBzhk54nwYm-IuPoI6IFXX76kur-DFM2VCs-UoNrbVRPwzEHTqgYgd3TeTYClhEXKaE8XoZ-A293HwSrK2BvspCC4CzP8uXO3x66MY3tc9qZE6UzTnzx7oYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30443" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYB4JbcIEC61kR5zNFiQpUdNhEOLh4ejoxZkkQzDp67iXPmDjKW-O-8NX8Bv60V5Posq_4E_ltrX8y15VHv5XjaJqRCfdWcuLWzbxx9CmNIESZUcnOs1R_visrx9Mouke9XNYozd4wExNGlOGBBYeEaPB0XT_meZAhy9H9JQWH14JSPEK9lkmduT-nU_1t7pepye57hzyhnKyDvLpEy_KtMKvOUlRWinliUMK4XMuXLMwg9URMGQ-jp-dmGe6OuicvG4ZngEVJHwBMMltmUDxFvNmRiAl6SMdeoygUtmkq9iRIy_gkxOe_LFXbuaTf2scAKhnlNyCJdc5NGReakZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ قرارداد مامه تیام با تیم چوروم اسپور ترکیه تا پایان فصل جاریه اما هر باشگاهی که او رو میخواهد با پرداخت 300 هزار دلار میتواند رضایت نامه این بازیکن رو از باشگاه ترکیه‌ای دریافت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30442" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSJyHPPN5XjtJN0iAliKNqYmiVLf7AyA4W1QJntk0lqIRdouAuPVT81EuRJIoR1K5bvvOmk3uVe4THaJ5BRuOzdxNewFmMSGA4zuuVP8KbL_T8XqcEeaLu1i3L5ui3Sdw0kxYFMhdweMngm49Gjv7OnkhWfa6-NqVUmhIPncuIyY4yfg4-Stiw-uTPln0PhSN029d_8ZKZ3z-z64Oa8KG6cPIy-lGa4t9MLEgxNUd4gOVB6SyquuB3oBzw2bQtaPqFL3JFSF9MVROVKjxOM5wBjmnnNFmbLguD5ZFuB28LaqQtk0WPrJ-dPNGb4-QFl2ibcku7_cuZpVbtSLQmlOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30441" target="_blank">📅 23:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30440">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpzcMz88kgNADCtaoEHpKVIZd67-ih9wFlJ-5plGGwcZPwqI52Bf-wTEocr1Zd_8KeXB-7NbVAA-nYO0Yq9DaJQt9F4zPxABgyID48-IUAdA0ZoERvz-fWmrB7WBJcYpHhbWtmzGNJLzY6rrqZ-PSWmdEgS3T3FewymqKVwqXr1hGoK9UILIvE6n4Zn5VQVIHK9TRF1TlluF8Q9SaB4JGs3p7uizkTVGNnthcB9CCre81D0gI20n7w_k-TXWvp_u3SIh4IgEn8jQTFZ7YuyYBovmjq7JRxRF1wkF4tVg5h02C1U92BXLOUw7ZBvWYcAQEfwKVBN8cby4QnibuafePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مصدومان پر تعداد باشگاه رئال مادرید درفصل‌جدید؛ فده والورده و ابراهیم کوناته به جمع مصدومان پرشمار کهکشانی‌ها اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30440" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30439">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔵
👤
مهدی توتونچی مجری شبکه ورزش خطاب به حسین گودرزی مدافع‌چپ تیم استقلال: مطمئنی استقلالی هستی؟ فردا روزی مثل جلالی نری داخل یه‌برنامه دیگه بگی نه من نگفتم استقلالی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30439" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30438">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSa1yIt7A-W10QZd2w73-Hkcb0HZvjOaAaRfowYqp24_fHYy3dPZiieyJDlnCGC4cYV0rjtz_oHfyyYodURsZUgP8SwLo_uBUaniZPjLwF5saNhFHn9E_0WBXlspxDUAd7Z2Nr_9wvHK7w7V6pwDoR5HxzM1LHdrRS51sZJYczaNX4rvSVZu-ijFRIxiijfaFdiQpTziddjf4LyfwpFOcS7PHMv2U6RVR4FXTAol8w4waRu2WnSVDV_LTCblHbJhNw0skXMJV62FzyIXJQaXnT06maSA5S9NlB6BGzzs0ClhU-9dmZn0fHBBOQb9Iukb3YMkGim4bL3c3ufXgICZBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30438" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30437">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN9qyHPXT-brKfHwRhueKDT2iu-e-5BWG8eRl9D7X2LXY25maY9-lWrn1QfOdjq0lTrab2DYhoRZaqcQzQuK8eeTCsXfqrYppP_K16yVia83Z5Okb5UaMhHM3092v5b22FgjLk8NgHmX2ApBhwqM0I5pz65zaCnf789p0ClbTFp4-6EfbcUzkg6KsR1CAtDA9zG4pnkwSoRwCgewuB7gOJj3wvhA1UoyR9Btw2Gr2p0ER6fXq57c_1R1FPTmHJgWRa7t5LBCOn2X5S_vcGVN3kzqtRJLXByo3k5mixc-BCy5KHJvcNcxea1MM27MKMs-GZr7ewYOdmBgUmKpcdfsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30437" target="_blank">📅 22:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y_ZQ_QCkczMHyKMbn8AOhlmtWwvj9UvzQ-gybalGfr2ZE5VW9Y6lk4g-xs4lFBhHsAYs_KCHFWihBsD5TyuR8Sm7U6lt6aD6w7xic4aKsaapWNsH_QI41LZ05w7sJMj2zkDL0bUDjvMNBCJ2ALpgYqe0z_OLYTyyi4yNDsbePrdSe0YJ-PbH5vzyEp6MTJAK0G1HrnepFgA9KuoWg-kXkqEhmEqC9rPXb6PN3PqlF9K2phu3Z89hQCmmBFU_kGPc0MsZLXFfHuXB5q8RyU13wleu9nHmBRDdWPgTaG7xpBSdx9NDK_gM23EPb449P_-NcqclGropCdNbFMODyBJHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vyqPEkm0Otuj_0U_moFtqzj3boi_E-JQsJU_YpCVGuB-aGgiCsiMXu8sAj22YSvnOJT2IYOAXL26OP0KlU1T5Cg3qVazDlhSKbumc_EJljTcemDzYGxcFPBj91oKd28kNOTa_LiEiNKCOS54RRoVNIwzxK98-Pi195antC415Oo0AFTzZkBkagtgyM5uiEOOSqrXvVKLPabMuQWAxeC4lIyV7sE4A8Lm8_VEVS-lFRItm8B6manBJuANqWasgaT9dUcuawHnuSpbchD86P5FwproYJIwhQeZ-bFiI5TIsagHFbEGU9x2pEwhHEPH_3xeULJX67QvZw0MDPdxZUIaiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛
ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30435" target="_blank">📅 21:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21cf909039.mp4?token=vHUO86Zl9uuyy5aGa0Zitf3q0G_Y_ToytjetfSgKmlb9X4GUlf0svCqtFT0sWI6zFmVr-ascJRiZjPUaQZB-TujDOJ31isXc6K5_C5Ag7G87a4aEAkPlfvyXpm66DiMe12NIykGI8IFdAK9XZSeqpvAA852hXqtFvyW-h6mxZ7VOFMzhX1QRuIivJKTgNIcG3tCzU5JDG_l0I3DtsJewiZBfsPy1QzTLKL46XRxaKxzjxtnArmOJIXEZ3YfDy2oWHVk1rGutgFnXIocNqZA0dsONfJXlxfgXfk3u1CxgrC4eeytswPUEgxeuJPaDNr7DZHpye2AQIv3YrY8x38Oc9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21cf909039.mp4?token=vHUO86Zl9uuyy5aGa0Zitf3q0G_Y_ToytjetfSgKmlb9X4GUlf0svCqtFT0sWI6zFmVr-ascJRiZjPUaQZB-TujDOJ31isXc6K5_C5Ag7G87a4aEAkPlfvyXpm66DiMe12NIykGI8IFdAK9XZSeqpvAA852hXqtFvyW-h6mxZ7VOFMzhX1QRuIivJKTgNIcG3tCzU5JDG_l0I3DtsJewiZBfsPy1QzTLKL46XRxaKxzjxtnArmOJIXEZ3YfDy2oWHVk1rGutgFnXIocNqZA0dsONfJXlxfgXfk3u1CxgrC4eeytswPUEgxeuJPaDNr7DZHpye2AQIv3YrY8x38Oc9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30434" target="_blank">📅 21:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNdT-31-voJqn3qTMY-HhC926zVXJFtrSk9A9YbA6e_DAxSaJQ10OHW_e0U7P1oxK-0onseZ91vs6POxfGJwdHV--wcYjkrRBZWj3HaaBEhONQMiwN82v8DTv6GWa1GCFg8rcNOc4824JTbOlBsZ8A2ntRllttQDWFRWQsMDyiv9tWogw9eXpU4rXd9SYjrthjNvR8BI2EDghLSEk84vd0ICG6P9uNQ8GbBJZhtLB4nq2VZ4QTb1qizfKgARycPbRSF_FUxfz3xh5Zw-QvteBt5nBugkrwGY302RuUQ1sBMa2G42cBh8EIuftjLbp4VFxn_UGHhg7SUHCqZVSRuSxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به‌مناسبت فصل جدید لیگ‌ملت‌های‌اروپا؛ نگاهی بیندازیم به پر افتخارترین تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30433" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jcz_OAR2ZCFe7JqdxP2GjMDHmFGZ_NGP1XMnUmoCcCDYXdJ-1Tk8oSq8bLgkXIxeqydO4b8a8Qmv0ZWUIHZNZjl49HxwNKTtAb3S9vE9b0gogRh08IGtQgn6CzUj2UKp0oJ7sbHzt2kxi_Bdmqll1JJhAjdqFgWTwrk93zqpA3YnNfGWbhibyQQt8ZUPIN4rfhSNPeVCXUmSWUG8MToTFVG9IzamGvIsFXoNVsPBPK3O03OB1o_Z7FOqFFwUsQbYKZmzMpnY5gJ6SvSCgiWHnlhXwCmRhTuu_mqhc5nL7Uc8m2nVzTMXb8gKDAe128ccnpQrAvYyI09uc3tAcOujdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30432" target="_blank">📅 21:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30430">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=g0hz6K1NvZkQHV6wBZajRCgoMzoNhhtSsPtXCpraYVd635ssyh56JZ4jZ0y4HUtivfEnmxuyfeVu9JNIQFljEMTAsDTb3M-brqo3krzhu9diBLt1YBsXwOfbxD7fs3PhcCwVJjKjOwwribvqJIWWLuEohT6d7vdoLEUbAw2RxX-NmZEw7XlwTk8g6UBp7IwUZFCXJCCLlZ-hT2NKWmA-DVh5GKvxmzCzLpZeSC-5mUUL8Zr1LZJbS_L2eWbm9HLs1hGPolp3-cvJw2HXnl_u3WUnx-BqTaXF2IPZaU7a0p0YTDIC6dZnF42TaEfNkPK2ATHzK4OItYseF_eUEM5_FShOQR2S10gnaD98LVd7Rwhooe16QjeqRd1F3OhKy-T62f6_EkTQ-MOdtmQvL5ubcvqBHi0dea_QP5-3e_MisPTfl_Ua6erAaJgnQ2M9RX2wpM3-vWgLhjnK7kcfSbz2Sb4pfyT7HiBgOYTwqoMoRjrNV-F9BXEKsg5JFIsnrr-wXZqRclKPi8cuhuGUTEvFy_THf4R7q9x47yRoUutRxxyqyK7r2Pa6hP60qARexurEQ0l3J2JmjdrXBqijy3Y_lg3qTFDOri8mrlpO5UHqGiMxFP_xa1Jf-Wcq4Dv-Lu99NhI8TbHQb7ltCE_KK1RZYGpn6IiuxEUOMg8rOo5DtRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ed2cb9e.mp4?token=g0hz6K1NvZkQHV6wBZajRCgoMzoNhhtSsPtXCpraYVd635ssyh56JZ4jZ0y4HUtivfEnmxuyfeVu9JNIQFljEMTAsDTb3M-brqo3krzhu9diBLt1YBsXwOfbxD7fs3PhcCwVJjKjOwwribvqJIWWLuEohT6d7vdoLEUbAw2RxX-NmZEw7XlwTk8g6UBp7IwUZFCXJCCLlZ-hT2NKWmA-DVh5GKvxmzCzLpZeSC-5mUUL8Zr1LZJbS_L2eWbm9HLs1hGPolp3-cvJw2HXnl_u3WUnx-BqTaXF2IPZaU7a0p0YTDIC6dZnF42TaEfNkPK2ATHzK4OItYseF_eUEM5_FShOQR2S10gnaD98LVd7Rwhooe16QjeqRd1F3OhKy-T62f6_EkTQ-MOdtmQvL5ubcvqBHi0dea_QP5-3e_MisPTfl_Ua6erAaJgnQ2M9RX2wpM3-vWgLhjnK7kcfSbz2Sb4pfyT7HiBgOYTwqoMoRjrNV-F9BXEKsg5JFIsnrr-wXZqRclKPi8cuhuGUTEvFy_THf4R7q9x47yRoUutRxxyqyK7r2Pa6hP60qARexurEQ0l3J2JmjdrXBqijy3Y_lg3qTFDOri8mrlpO5UHqGiMxFP_xa1Jf-Wcq4Dv-Lu99NhI8TbHQb7ltCE_KK1RZYGpn6IiuxEUOMg8rOo5DtRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پارادوکس‌شبانه‌ابوالفضل‌جلالی‌روی آنتن زنده: من هیییچ جایی نگفتم که از بچگی استقلالی بودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30430" target="_blank">📅 20:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30429">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNMig_6mjLdsYegNVxWf8iNVXpdaNTV40bsjptr2afaqtZ9UFTsfyYwwBYFlscEf-v0lyFoW-aGuojxIznskgGgnqe2b06x0JsNIENWvTmoJyNfjiZAagv6UmkvFCP10BIJmPcjfBAxYIhoF178AI280G-pqoeTNBFzV-9xubfiYGNd0sLJIfp6Z0UaqhZDogQQQ8YOarjDO7lEF02cZRakSXRniZNSysIBQJa4DIe37KI_ems0Ksc-7xBNzvm0lytNvqBZgajD73FXrPe5DfBaFWEUXLhMGIw9gLU0sTJ5SeyRbpDqHG7nrLUT6FkT8fzJrzcbx8m-nkHrFYW0P3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30429" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30428">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SF2PG8TP_ssP2_6Vs0US85nUadrlwGn3kKJypljEMGhPuEYZtfAbh4ZWHmNPLPWaYQ0NjNglqv2FyoL3ORIwA6DKKH1FIOZ_Y-SLwM_LtQxMWXhUpVL3Pj55-dM3fCXsuRS7IC2znm3XjULUvq_Nm6zJ349JR67h3d8_IinsEjJS10gYShFfeTuZZfj-SRUYTpmuVlEeVxnuNfbzquOZZheoFlsyCP355jERdCznUpngEGvj1CWOooYQ8FmWVgtFc9HvXFQxMELgjAjke_MqngMtH0HmtVe8f6Zr1Tx0CzDhZKVvxa6woFVYXDuIYs9h_HqtCv1Z80WAJyQuf6b8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30428" target="_blank">📅 19:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30427">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUmnCeIb3ZzgNPfLgrqmz47P-l9xgUQLKD4smbEdygkPcU_ol2TYFZeoWX6TjqxwpTpoi0u9RmqyGLQ9bE9h-90xThjVe-FecUWsbJm4GgLPtJXVy3RJ-2BrjQFR_m_s9iyoM2ENYHZq1tX0czj0rn984B6kRqSjcuxQYCLPngRuxjdhkmhLnD9qGXY_PyOCYfOuhMzyHLw5LgNeOflEikwfC2TcTRfdm65yVorF3k7g98jgZBxZ0QqEDiQ5eMCTDqDeeAKEhgYxBSzbxZ-pL-Z1H0bPNsKb69eNDtvFhGKYXmaSffLkCDxy0s136-Y862n4mg6R8rxl2gbtiYNtsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30427" target="_blank">📅 19:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30426">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcxb25Z0LlCC9LCXch6RG404MZRtk4Nt8Iu0DFBCnTHZoP3DNZ8mAS9Zm_S9Nn26wP3cBGkv5p2W8yQIOgmVy3ndtE3ZEpduwfgnEumcn_SAmC3rEUbLIOYayWRtJm4xdrcL6WbKhQfAT2otpJMBbadu5_c-5JwZf0H7xSpiQxYCO03IDxJKE02Kf2e6umocwSrc6TNHc5gXKRf2L7eVoBXvYpb0Gn7hHlB89LEccbILol4r7BOrtd_wzLzDnY4CNqDyZrmTsMMpxRSuKmYs5DrJYdjsrlS2lA4udb20vzO9B56mYprxhl0oj_GpkZnA9WIrqlI_iW4uBjiHdhBXPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ظاهر جدید وین رونی اسطوره باشگاه منچستر یونایتد با کم‌کردن 40 کیلو از وزنش در تنها دو سال. درکنار کاهش وزن رونی اخیرا یک عمل رینوپلاستی "عمل بینی" انجام داده که باعث شده همچون قبل خروپف نکنه و راحت کنار خانومش بخوابه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30426" target="_blank">📅 18:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30425">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMSpeK62UFQlfdUx2edokx66Zzy4E5p9EeGMu3E45erueN_N971dHJU7hFznLiUQAFhjAeg9s-TsaqN3Tz6LxThPoYh-yPr4TEjIVY6Ztl2norxhXyTYhZVI5t-Ts78s8vk70taeLK-6vJKFhdV6DYRmeNHcgnlg7WBBZ3bolXlyNQ_MUCipCTCQG7hE07PZKeT6y4C11Jzi8g9ciKj5Eixx76rLAUYpjEqVQejwHgqEsVtHGNAFuBOxkG5R7Sa0hCqBvKMU-hdnv8FQKCGyqgVwbb9doFDp9kbf68aDVvh4ChCLmB4fjVcP142H9Ky2scmmKsJRPewRd-5VjpZVpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
بعداز تمدید قرارداد اوستون اورونوف؛ باشگاه‌پرسپولیس قرارداد پیام نیازمند رو هم 3 ساله تمدیدخواهدکرد. تمام توافقات لازم انجام شده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30425" target="_blank">📅 18:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30424">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6n4qG1a3y6hKCOnoRkZy396zs0EM_yCT5gGBIQ-wihyswAhDqwam0-c1RSt5u_fwRTCRiZ78DEr57Mu86cGVGLHuFb8x0fkWxEWQgjyLxIBTIEFs-aPO_hrE6PO-uBRg-6Y8g2bQ5pxWHNGu0iU_9fDWWShJ6SE-It23RSFkzoZNGsZx-bdizY5MPSXlWV7Xhrdy1mkES01Kf6EBn36Pp-yvpYd-JP36n7HHLaEYNlOUNbg7dwJe3eTOafxk1Xt3ba8VhZXg1Yug4aVNbGS62F6Q2xDhuGRdnON3iBe4qlB2JA8Nn72_qDwp8YH7aayB-UJehJSQCf0e6rN2kIUTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛
آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30424" target="_blank">📅 18:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30423">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNXFu3BZr33nUAqYX6BulzGeH0AvjU5ou_hGVpCHnry4NSuw7X_UDlVkDqJHl1kvIu5yi5EfQwRShM4FJuOEOY6P2nd_Y11b5ATfxO57DS1mY5Ohyl8LilDwqTGSCx4sa5nc0utP6-8wS4uJi9TXcCDn6wgUc7wf-OL0Y5n8xTtprkHfNloxn_8k1WEMzUgP3ICvf1B0VRt8zvjvc9twXaeSBBp75Be9MSnR0M05anKxcT1Dzcz1zUKxGHgUWirP5EzAC3ATv16EUa8R9kbzTBe9NpLHj-iddloN2I9iyoo_sH0N93ryLgx5uxuG-rUqiCmte780wM-tS90_de0icw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه: امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/30423" target="_blank">📅 18:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30422">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va6hy6i1pRkgCSpizaxVwigCL1RJBtcksQHQY193bMmaYmjqsIqdqN2q7H1fXBaGDmjIzKmLI8qyEB8SkmNMsbcPv986aC1ZLBojwezuC209ZBSxwc2QUh97mjK6C1YxhOdpY83vrnhlUAa2o0HPvqio9sxn7S8ImU8XZK5N44emoF-3NT0hWvE8NGyAAQ1baBcSjeA7RB7zy99UftHF_th2_08iTT5K3I4MJD27sm2BcapT9c-HGAL4X3choihtLEd_4NAP3jzHgBpK_OY2GP9phqojYaHcqjZW1UnpZOm5gKjxcIUKVmgeA2Ebwi8ftFbljTH6O6av8GGoR5QtpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین: من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...! هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/30422" target="_blank">📅 17:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30421">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hv_pHESOV3Ek_jQ5xQIQkUdvNaIgfbMBmOd-FTc6jakmfKbF_3EUl6eGllpL6Dc36q9b9_gNgC73pJb4gP7StiM62WNpVd_RDsXMdg8RYsUcj6DV2Ps-DKW2pfustUjLTAVtGDyLB5tN5kMtwtt9LVaKjnjPctdaz0LtfO2f9uu2fyaeuIKAvQZt-GKbpk_Aem2pG__IGbQHuJy8RMEOPpqUNiuCf5GjOPFOzPiZ1jGrn4YFREQ4sgduK59RC65Xw05C-l7oei-D67klMFf2PQtWYksKCbGm56SG1djTYo-dHZQyBSjzbpGdaUslCExb0DNEJjgH_AU2_WGkB4cc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوید اورنشتاین:
من سیتی درتمامی ۱۱۵ مورد از اتهامات لیگ مربوط به‌تخلفات مالی، به جز فقط یکی، مجرم شناخته شد...!
هنوز درمورد مجازات‌ها تصمیمی گرفته نشده و تمامی تنبیهات همچنان روی میزه. این مجازات‌ها میتونه شامل جریمه‌ های نقدی، کسر امتیاز یا حتی اخراج از رقابت‌های لیگ باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/30421" target="_blank">📅 17:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBKuyznwUdnIUZMqdOaWl9RD9hhvPeM8WUmBWoDUHwe98tgHA0Vd17BianTEjOEPbPx6J2LdRPKqoBfeb5Iydq6NuTiBWxdOQaNTB8asL2rj7bjNx5P7fs_B6rR5frwJ1Hu81KBdRJ97QQ70crQeceSAKs8o6yXFnf5_7sJ1od_P6KlnTp6KGBbCiyxcZGrDkGW-Horq39tIe5gIAGiKoyXqGAdP3GP5sqAS2rQaAxucgFDxlECoCefVVrnPJFspIrswC3MXs_vUlmJjeSMvp2g-UR70-pYO-NRb3foUMmjBLy_VGp88SJ637G03A2ZZSlrUA5MxbfWT2BHvw_FTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
پرسپولیس دربازی‌دوستانه امروز برابر تیم چادرملو با این ترکیب بازی میکنه:
امیررضا رفیعی، پویا پورعلی، امیرحسین طاهری، علیرضا همایی‌ فر، میرشفیعیان، مجید عیدی، محمد خدابنده‌لو، یاسین سلمانی، محمدحسین‌صادقی،تیوی‌بیفوما و سرگیف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/30420" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bp-_4hPrL3J3zLpKjv_Hi0rMLjn5edQ10TXmUNTNA6X8szSS43d97pYx2Uor69At9Sli4nQHC3E9bny3wMIcinCxX6zxTyWtPIV2gXYiMPdoaco2_hR-h40F8jPU_Xw8eGhzw7mb0Ek3GUeHl1T4E3UYek_60BuautKqakv8p97gf7eV-eAUogkqIfhUTF4MetsgjMGrPlCKftuQdg5FiZ727rKINUR0N4anRVzeCQoOp4PW2GDxR_l2TucjxYqQyhm_hQGPh1pHI17toqYDp4ROVNg1KThMTksV5GZLaQKll78qn7UBe3I95Vr3fzZOh5Xq5WqBKVcVBK8svgZ-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاثیر نادر محمدی بر فوتبال روسیه؛ گل عجیب با پرتاب اوتِ آکروباتیک! الکساندر کوزمین، مهاجم بالتیکا، بایک‌پرتاب اوت همراه با پشتک حرکتی شبیه نادر محمدی انجام داد و توپ وارد دروازه روتور شد. دروازه‌بان روتور نیز بالمس‌توپ در ثبت این گل نقش داشت؛ اگر توپ بدون…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30419" target="_blank">📅 17:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=aax0FujZeUwNMEqsd2eHgconiRxETJ6L66NX1uu0QBn20pmM3hAoVG1BTgaBkaxYmbZA5_VVTKDd40YU4TACtkd2M0NKBY2wMqr1d5F9sx8DRgGuytvgq0C3A5tnCtUSPjzhAIrhWLYSPfv4MFZ8kGPrXMBUEXd_V2r9owvguqxgcyFJy2l-agddPonw-NuT506YzDO4DxiUrfmYzWmXahTGk2BsUOKId-RSOznKeoGvjSSZvssCh6t3KOKfSAHxvyL8Am8BPL-lGzVkcT1hhGEU9QIhP34XosYSVmHOw_OWc_HCft8mVR-yPmUdrlWPYDCdyJtnpnC2vXCiDwWBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e998b3c1.mp4?token=aax0FujZeUwNMEqsd2eHgconiRxETJ6L66NX1uu0QBn20pmM3hAoVG1BTgaBkaxYmbZA5_VVTKDd40YU4TACtkd2M0NKBY2wMqr1d5F9sx8DRgGuytvgq0C3A5tnCtUSPjzhAIrhWLYSPfv4MFZ8kGPrXMBUEXd_V2r9owvguqxgcyFJy2l-agddPonw-NuT506YzDO4DxiUrfmYzWmXahTGk2BsUOKId-RSOznKeoGvjSSZvssCh6t3KOKfSAHxvyL8Am8BPL-lGzVkcT1hhGEU9QIhP34XosYSVmHOw_OWc_HCft8mVR-yPmUdrlWPYDCdyJtnpnC2vXCiDwWBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بعد درخشش نادر محمدی درلیگ روسیه با پرتاب اوت‌هاش؛ حالا تو تمرین‌ماخاچ‌قلعه کادر فنی یه توپ دست محمد جواد حسین نژاد دادن و میگن هرچقدر میتونی پرتابش کن به سبک نادر محمدی. انگار فکر میکنن همه ایرانی پرتاب دستشون زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30418" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e769a610.mp4?token=Xwui-em5UAehmBN0TIq4l7zgPmPc3oae0F4lwikUt6m9MsijNVWhZRB95qo79F0ByAdbUik2uHJKCk38iNgedKFemKOSBfBKQpgUGyzFDj44IhsNL-NxscGPxsZCFT2AlLRIyMYDTog3Zbekcfwvwn3WFp_vju2mIwgg6TXs4AhA95JxX7dChfy1qEwWTmUzscZEi-E8G-op4l-XiGFhFedj_cfOVYSqAqoYTxnRoLN-NCuq8yzHd_7d2EUpqkar0cEodopIzQbQNI5EDfvfwUzfnR7Ujj8RLRMrYfd_0ZYTBpIFTbHuLQjQuj8P2SkMwmHUfzFcZbynPZgmIyv7Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e769a610.mp4?token=Xwui-em5UAehmBN0TIq4l7zgPmPc3oae0F4lwikUt6m9MsijNVWhZRB95qo79F0ByAdbUik2uHJKCk38iNgedKFemKOSBfBKQpgUGyzFDj44IhsNL-NxscGPxsZCFT2AlLRIyMYDTog3Zbekcfwvwn3WFp_vju2mIwgg6TXs4AhA95JxX7dChfy1qEwWTmUzscZEi-E8G-op4l-XiGFhFedj_cfOVYSqAqoYTxnRoLN-NCuq8yzHd_7d2EUpqkar0cEodopIzQbQNI5EDfvfwUzfnR7Ujj8RLRMrYfd_0ZYTBpIFTbHuLQjQuj8P2SkMwmHUfzFcZbynPZgmIyv7Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ساعت13:30 تیم‌ملی‌برزیلِ کارلو آنچلوتی با این ترکیب در دیداری دوستانه به مصاف استرالیا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30417" target="_blank">📅 15:44 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
