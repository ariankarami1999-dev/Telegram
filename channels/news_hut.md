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
<img src="https://cdn4.telesco.pe/file/i871apWkffRI_T15boix7iBelk-uQC8wQk7xfuk8hbA06nZiHpYC5eBI391lrpgdQtRMcsfmSdjrLHUu3DPzlPMxdgEkOlCH8wOSpBXoORbcCNEEzQkuEYSef0fQp-rUeazATDWCCnEkEUYDbX_mnurg2AqhOd8vnVbSyuMkAl51LRxZPbKLE_ECK3aLzpIN4kROSNeKqFy_bV-fwxph1yvMwdnS0TAMAnhpsV22V-X9qEiTcURTpAa9Th3cBc9mWYLAojALwsIReDNDEdaKfq41WHc74x4jN--zgqU4aU7vCFobrRDUogv361juSaq40T4JcskFZ_wV12ObN0yGuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 168K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 23:31:29</div>
<hr>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzi3s8Lj-85q_zS5fgUdDfiFW8R50TZDmtAAtxN-SvhZJJnGw_mDZPTKRfG3IDXLSONOdH7IW4NMisHWmxT0oL8gqmDK1qkWC6aC8N5m60Fna4fK1fOSAbb5yK9k3cbK7ucaqe6an9JpKYYxgbGbpjGeufVyj2qGRk47INAgD5r2gYNq7f7Y9n35C7LM9wRco6uAEwDps7VwNiZCDHYj5OyjZh02YMAMSwb93ieALQixABNqjqeS_0tIaqgS0AKgzdWxy-qFnsFscCm0D_iLSHbgvAiORRPek2TYMVEEBJqj5M2NgSdn-WKGjIrHyUSCRG6cTp3uSkarlQyqbnXOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDOpDTruZQ_2vqPrex59wNbfK8aIhos1b-FO9yN43FLWWIxqGfFtkiKQ6Dd0vGIKo7ZhMkQBlahmsHXsHoti2XW5M4mKOYQAR28LjJdSDyr5JWrBC0LssnDlVxKLDlEQm8i2c7VEdPVulsEcq93TdXwHmcL1nkj9FDfK3ARm38JkBqry1tOA-n3VV8rdZZnhK8GLM8XbbGf-7zH-WNfR89J0JFcznaXB_rNsuFjEy340HxEJw4S-S9Ueulwiar9JHomWuJXLPq5j54YxktX9b6v_neYkxFwNT2maMMgLCt0ZGCej4b4qQsTcvsAfBoD5c1gi9t3XQbJCP8BIq9SKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=QYf16M5HW-87rfy6dV0HcbhMNQWlvN9E6x3A0VEOYuYfEy1tgMSknPPmHdYiHiF8l1YfzdTZkzNM0KiP69rmhzpPUOtA-GHbcO9htL-OgPqhXL1n51pPoJfEpfqyfEfXNfbCS_KAXqOk988MEnhmyIS5SuOoUkmEJBk2OphjedcGnH1iAv2JWovQKeGuZT9XqxLic0llBTR7K4T-egXurh0G6LeFcUKi1WUORwhtzlR753yir5j7N5LcrU4dMRwBp-R2reSzOPWO5vf72F9I42pRDCZ-xXMjLohuE8wG-i5x9dQ4GTuvvK_CB9U8VnKA6XlRUlepFAbl7CF6nWSHOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=QYf16M5HW-87rfy6dV0HcbhMNQWlvN9E6x3A0VEOYuYfEy1tgMSknPPmHdYiHiF8l1YfzdTZkzNM0KiP69rmhzpPUOtA-GHbcO9htL-OgPqhXL1n51pPoJfEpfqyfEfXNfbCS_KAXqOk988MEnhmyIS5SuOoUkmEJBk2OphjedcGnH1iAv2JWovQKeGuZT9XqxLic0llBTR7K4T-egXurh0G6LeFcUKi1WUORwhtzlR753yir5j7N5LcrU4dMRwBp-R2reSzOPWO5vf72F9I42pRDCZ-xXMjLohuE8wG-i5x9dQ4GTuvvK_CB9U8VnKA6XlRUlepFAbl7CF6nWSHOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=h2ZsveNLXTNcijXSX1MwNHfAkYjd4RrN1TufUquCjKXBR9QBU8BOCAiFmmuCtQklq5la_odck5fb8EmznbIe_ZDjOqxYpBV4SPEY_IsO8AXixnOWt7YkuKehp1z-1HsN5LPs-Yel6lpIk_Ke3F3tGXtsTcV24uevZi2tjbCFhbi5k_V06HYfDGKw6uqwsLADAiSGSBxAUMoF3O5aVa02CXTvnRtfDlV5NRb8DOhJ6g8FN6iWK4y1Hl5kHNjcuszp5K8V4lu2voXX4Q98ndiV6eiunxr2zFult9NyUnjGia2BEIpB5UeuwdpFeDaDqkcS0lrmOlxrpkVY5KYWXDfTFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=h2ZsveNLXTNcijXSX1MwNHfAkYjd4RrN1TufUquCjKXBR9QBU8BOCAiFmmuCtQklq5la_odck5fb8EmznbIe_ZDjOqxYpBV4SPEY_IsO8AXixnOWt7YkuKehp1z-1HsN5LPs-Yel6lpIk_Ke3F3tGXtsTcV24uevZi2tjbCFhbi5k_V06HYfDGKw6uqwsLADAiSGSBxAUMoF3O5aVa02CXTvnRtfDlV5NRb8DOhJ6g8FN6iWK4y1Hl5kHNjcuszp5K8V4lu2voXX4Q98ndiV6eiunxr2zFult9NyUnjGia2BEIpB5UeuwdpFeDaDqkcS0lrmOlxrpkVY5KYWXDfTFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_Wpu78rfsdtzGGJ_kVT5MfFwRy3EfFQS1saZulNl1bolPEHDHg9A4jy5PK2Ho0_ST2cc5NPYwbaEuUUAp558-YuONysXZpwvEpkMhZJ3E7VgRhz_Z0dwFeGQCeqvap6XTnY_NnBDBhUDwltMASisAVqo6XaLJ6CGhMb-ZwPvowOhVJOE-vmCTs-AcZTXuwAs3LSnOaeDOag1V9O2CRM-v2QhLClUe-CWyPAmA2ZAx2B0XQE_dqeD1vKCPvzHbty4f30X1cJK0KOQRV2US0XyKebhO3bTODoQ9RQYrEFY4Hpc80c-yZ31JbXr7WyGVxuYKv1zT7qnr1yOVagSy1IPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=tNMRH0PzmNG7XypId6EH2vYHD92fynQrdEpTfR5Ss9Pi4YcSSLUipCQY4TRyT1spHeKMRJ2VuHREhJeXTNT34eqdco8adEIi7vcAopy7eAAOn5SZshmWgm-eNd1h0bENHmcxgrfoZBxdx7y0fabi1mk0fE_MF3Ay4FLeJAshDP8G17Lmimv8GsyO5K1pqdTtIBl-drdiwL47YkJhbFY_dp1c2Fo0njocRdKG84vvtF6_MnnG34yIu_IA61Zsnwa301vBlkTEDYbemAUgLvcXoqBy1A0WEPLa0Js9criqXiwFuZDrQVZo337mBumSK5TaUZDT-QTbsPeMPSn0xPpl8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=tNMRH0PzmNG7XypId6EH2vYHD92fynQrdEpTfR5Ss9Pi4YcSSLUipCQY4TRyT1spHeKMRJ2VuHREhJeXTNT34eqdco8adEIi7vcAopy7eAAOn5SZshmWgm-eNd1h0bENHmcxgrfoZBxdx7y0fabi1mk0fE_MF3Ay4FLeJAshDP8G17Lmimv8GsyO5K1pqdTtIBl-drdiwL47YkJhbFY_dp1c2Fo0njocRdKG84vvtF6_MnnG34yIu_IA61Zsnwa301vBlkTEDYbemAUgLvcXoqBy1A0WEPLa0Js9criqXiwFuZDrQVZo337mBumSK5TaUZDT-QTbsPeMPSn0xPpl8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKfj-zB9XykRkwZskQscvd8JO_lh1LG1uJT8GE222G7hQ2s6JYNmh-tweg09ulFlKPB02TzxwrkEkFh-2lke_vu0y2vQNU9fb3ip_U_EFT3IgJhfDi5sq0zRbLvrFBcbPSzwBUKSgkgZELwiCO5HoUR-QOV97NZ8oRdjUCh2W_5M254szsr4lBZT2bhL8WI0WmBURh5ij2VUctu9Ny2IX1HwkI3y2KpGzOsDz104lfX4MaBNN_kc-lCYNHwWN_c9OZsjncX3sEit89FbqiahaXfck-x347U4YJsg1ftLoqoPWluNoRgtR1o9iyPVSGtfEYEz35uvii5z_SUVR7KfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=uxhzjVUfBL64tWV8qjJpI9vmdbcWOHJKxVM44cOfMNLPA7GNV5_QL3uJN5AGLFYOrT1oJu9J3C1jNwTQ1pbNUuUBKjTnt0itquS0bWgkGKUdsNs219ShrcvXV5yX76-1BhIBWSUcB7WVsjs4n8zR4WSuUPgHj9xQJ_-SzrabsrAYa-WsaIQscYOgSI1rEPI66PHp2HqC4yS3-OZGGlqh3ZbRqxywL42yY2Cs-dV7LOF40hS91ieCnexBLdWatbJXVEBfy2cxbzVvpSl9gAl0hfdxtp78QgvT4jgPwS9APi2e6ba-zBK7Jkqrl9uc9KuaJjPOGDNlDu_vsURMFoOtWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=uxhzjVUfBL64tWV8qjJpI9vmdbcWOHJKxVM44cOfMNLPA7GNV5_QL3uJN5AGLFYOrT1oJu9J3C1jNwTQ1pbNUuUBKjTnt0itquS0bWgkGKUdsNs219ShrcvXV5yX76-1BhIBWSUcB7WVsjs4n8zR4WSuUPgHj9xQJ_-SzrabsrAYa-WsaIQscYOgSI1rEPI66PHp2HqC4yS3-OZGGlqh3ZbRqxywL42yY2Cs-dV7LOF40hS91ieCnexBLdWatbJXVEBfy2cxbzVvpSl9gAl0hfdxtp78QgvT4jgPwS9APi2e6ba-zBK7Jkqrl9uc9KuaJjPOGDNlDu_vsURMFoOtWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=eOVj37TVQMWCcEeGJYLAvI_fuZcH0Q41Du7Kx0eeVeGUI8JNfmN3zB94i-Hez0fu0wT9K9ROkJLqMjdpUbFCOKOxfTwTTE22WD988Q2Pn2xquguuHePpCIMCpapmgacrY1SpnRtQ9G5fvOA-5XhkjVrbUyZtinaUXxPtKiY83tR-2q4-eHLYvJqCHgGGvj44tpMmds-YYN75HUtpaXpOjulP53nzgJ2vIT3yNWEU_lSAUi71eKhL39-r2v-KhsbqLrHbqGxlClUsf-6l0sQqnlcEjMLl3vrHsbQDUIJezogF6eU89hIkm8wZ83UW2rY2KBt2OPduPZyooYjGPe9jnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=eOVj37TVQMWCcEeGJYLAvI_fuZcH0Q41Du7Kx0eeVeGUI8JNfmN3zB94i-Hez0fu0wT9K9ROkJLqMjdpUbFCOKOxfTwTTE22WD988Q2Pn2xquguuHePpCIMCpapmgacrY1SpnRtQ9G5fvOA-5XhkjVrbUyZtinaUXxPtKiY83tR-2q4-eHLYvJqCHgGGvj44tpMmds-YYN75HUtpaXpOjulP53nzgJ2vIT3yNWEU_lSAUi71eKhL39-r2v-KhsbqLrHbqGxlClUsf-6l0sQqnlcEjMLl3vrHsbQDUIJezogF6eU89hIkm8wZ83UW2rY2KBt2OPduPZyooYjGPe9jnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8F0fkB9MLFRL3vXMd7nMnvaSs96bpEEtutX90L3vKV4dXqco24rQX-CiPVyi7IKhAwFmAVgwyZitreMdxaRIw_mnfL7LeP7ab_Hw8QIXp74jH7QkBCpSVdIJsO_F6fDLJFmbmJ-kkPCvn94YVSmjOojkw2N4dJNb311IvHvuxh-cmBsnGjJE1HwYIKZI6hI-ZsNepbGNhFHYGniTR8b1GNZiP7JAwloOsKaep3TGjBByjuOq6Rh-yVVtWFVDhspgOYU6aEd4E4XckiML1g6Y_1BcpWIeysCbxsRQ-88NgFdHuEdHcBb90ufQlv6D-k6jXazO--CsvbnaKIPtr5RQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZsiQfraa-Q_VRQfHMgYo9SSQ_mZYuaw4k-_R_5Mf3QdT6kzA0bJ11KtWq9OyLHmasy9sikcW9Fo2oCyd5hS67nVrP-6djEM-iNlrMuwcNZvP4gwGr8t8jNZG6_jt4X14L6vCalsja_XAuazHfhQJosMfKuec6k90_ZAZqFB1ABnRGej_RP9IGlZ52YVb5D0Piy02XQgiSp0oDn2R_kG51GenVEKLVQjU5FSR_7g8fp7-NNSfyr6OL6dm2HPorKOXOcrp6XGqur49oDLM9TIpPsQTrhovn52R1AFKRdGUpra86GTAFpy0ANWt6kYqC7_vbf5rV5cYullOWHOJGHdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=PyRtZr-_zuASV4OOzP7oBHATIW7YNH5ZrX4Lw00F63LjBUj4G6RwkCYR4tfWW_vjtNoQXXRA896ZYPf4ueJ3YUFCP-Yf-uP90oc2Olkl7bfYOLRvWnpZtW3VGEjPonJHcyY64r78PcOVA_qriiI-oWXIFuuMzBsUvcCHHG5vYBmpy8JAJT7NEpWRf-lWK78SrHvDyI39f-16gbndBHpJCgWy9IMzo-MD5Bh8oKDknleO7wgVNXUnROWjnCco7AH6awY4ut1UggFhqxvAHskl-Wh9oL_6jjYtmoQdOJAS1HvKMyeDwoNbUyw4qHNppOZWgrREI_ryoxzaU9RiKb-XMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=PyRtZr-_zuASV4OOzP7oBHATIW7YNH5ZrX4Lw00F63LjBUj4G6RwkCYR4tfWW_vjtNoQXXRA896ZYPf4ueJ3YUFCP-Yf-uP90oc2Olkl7bfYOLRvWnpZtW3VGEjPonJHcyY64r78PcOVA_qriiI-oWXIFuuMzBsUvcCHHG5vYBmpy8JAJT7NEpWRf-lWK78SrHvDyI39f-16gbndBHpJCgWy9IMzo-MD5Bh8oKDknleO7wgVNXUnROWjnCco7AH6awY4ut1UggFhqxvAHskl-Wh9oL_6jjYtmoQdOJAS1HvKMyeDwoNbUyw4qHNppOZWgrREI_ryoxzaU9RiKb-XMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=XGBPzDGvgAvMXbK5Bi4ZBrxh8dNGC3zh0j2YJL2Doq0TIf2494hIWlSTeapGK4tmg7yoQVt5tOQ5-uxfLkwztl6i_R_A3g07Lr4GrZjmkrFdJKBTDLEcGUxg6Kj3JDEs_5wi7Qo6yaOrwQElu5_so26BdIWU-w4nFnuEXHL4w7iQvAiX4MylCLdcthQcoO0afr2tObqN45JTSPJhofxCxwjigcHb70aV58fTlvcynd7HbsqiKWMsNrPXIOdxu-0MSUVwDVtjtyjt-a_sgMGij3tRWppuqNKHD0WGRyDdbQE5jol6Dsp0sifOOX2k5-zXZsuZTukbB4TkzDqNBsPA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=XGBPzDGvgAvMXbK5Bi4ZBrxh8dNGC3zh0j2YJL2Doq0TIf2494hIWlSTeapGK4tmg7yoQVt5tOQ5-uxfLkwztl6i_R_A3g07Lr4GrZjmkrFdJKBTDLEcGUxg6Kj3JDEs_5wi7Qo6yaOrwQElu5_so26BdIWU-w4nFnuEXHL4w7iQvAiX4MylCLdcthQcoO0afr2tObqN45JTSPJhofxCxwjigcHb70aV58fTlvcynd7HbsqiKWMsNrPXIOdxu-0MSUVwDVtjtyjt-a_sgMGij3tRWppuqNKHD0WGRyDdbQE5jol6Dsp0sifOOX2k5-zXZsuZTukbB4TkzDqNBsPA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4SaEyKJejI1GnkyIQhKNZRmCs0Ca0LTerIPoOhAhxVWVyVfnumJXDprO2vkjsj0Ai5RDipuVLDzxIUu4Fb7Pn8MjkRRhQOBfZJZ8wo7zfFVzZein2eeJIHOJpULAz0MFuP_kgZJ3bXJcHSvn4FyADsa8jdSFGIze_kDboLKpObojNWMNzpgXRGsqYXkigsKDyYRkIfugJM_YPcalvYQOopwuQeP9k1YaBuTgBBuFuUsTrr4Bi_khvuVKyVMVEaGCqHCSLrCc_aw8NpP5-svcCPeHuWqzGzlafSs94USzFjS48oQ_BX8KMrF9VQemew3x4nYnA64ALkFZWs7fkPkSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prwi-zfgwY6nw7hKOFuWm97YqZ20uBuFvWJLbTsioCzirI3HIqGBtqEvWhY8ortcRvCg-QspNRGZ4q3Cpo09WX5vYpuOPPTK-GYD9nv2SoVWZ0T4TmJgKB_Rc_YMYkgqe-K8xzUYwukHNao_rNeD5r1zWeuNOfIAoGxj-JUqVvpe58scPo_ghaHjivbO1ljOK9KfYCsVQrI8YMZWTzvjYgulr3wHpqEe-7KGPJitZF9m46KKqWjsdwfVIMcALEar6DBS1L3xEdkNq0Q_8FPUTwcojXnd4qOWO0NXJhjj4HQ4yaHLJmJv6z_3Qk4pZuwCZjgneInhGCI52hxEqoGlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwK1O-t8oZaj6EIk3Pn6Kx_Z6TDtRKS_shEO4PeAkChk6vaKOLaz4xEq44D_tEWEhl_iA-YL_2iT5bIMZrmmjMEoqvpHECXFmOJgETnYGMb3eXtmle1-UbtdeC7hpgN5YhJKXYdLwtML9qP1ciW5UEmk0QFRCC-kEgAM7sUk4KFrGINqYj1aXS8CR6zkqxkAgrTDoxtpvazhY25kVyhK6JGfvJdBB2o0OpYQ7u8UqtA6s5H5y36zsS9IlVGVBbG8YvdeW9J5CumjQi1UtNDKeqgoCD0SAuGLNJPp3JO_nRHfUeA-aM2D0UYM-M-STtDTSdPC2jj_w1yCHFNK0VRh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=Pf99yjhevzXKvXjK1gRTi2vB2B30kI7xspe8LzrxixZ0up5mOLTccO65NeedlGbvuj3Ss4oU4wrvN4vbvhvXCqzTeGl5KGxpHcfD5KsyvBMptow9BGP4UqdUIpn9BQCPZG0NDn25XzJxwwriDqNp-Z0T5Ciu_mDYdBDcx9Vs-oT6DIHXT7UATGXAX_BysOwTIn7TAaqNK0IbMJimOYjx96GmSHE-WxVQM5LXNeTN6uAOfXUKYZcI0lbYLmYTsrbVAEZoLNN8SI2FvFmga_q8a7Ms-yAzLSgJHdFSt5ktOBzL0rb_Ovq1P0W1b0ibG7NBuCAUKuq-9aQrQ090gKn99w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=Pf99yjhevzXKvXjK1gRTi2vB2B30kI7xspe8LzrxixZ0up5mOLTccO65NeedlGbvuj3Ss4oU4wrvN4vbvhvXCqzTeGl5KGxpHcfD5KsyvBMptow9BGP4UqdUIpn9BQCPZG0NDn25XzJxwwriDqNp-Z0T5Ciu_mDYdBDcx9Vs-oT6DIHXT7UATGXAX_BysOwTIn7TAaqNK0IbMJimOYjx96GmSHE-WxVQM5LXNeTN6uAOfXUKYZcI0lbYLmYTsrbVAEZoLNN8SI2FvFmga_q8a7Ms-yAzLSgJHdFSt5ktOBzL0rb_Ovq1P0W1b0ibG7NBuCAUKuq-9aQrQ090gKn99w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uN7Ygx_z7gph5Mvm9zNKcar3LTXTOeML06uakYetT_4XWCSPY18U3-ZA4tvwrcCmW6BuvFzfpzzd4NCm_AlZtYSZTSGvdnALxKsvhfyCxFCDoS_IKKFBwfQd62WorsUxh-fGi6iYPmdx5K4HmM7X3Scg4mrHORlCGqir4Vhcy4_V8PB-8439V8jjjXrixXWHTk3mCu4VhcMZwKtXecf3TPcEaXnHwWrpqwJ8GY9mXV_lhT2K8E3Sih3RadX8ivmmZE8Cn-mOmA_8mpzCW1pDw4QQKR6HzPjNzrE_Bhr7FFWVnbCYH2uq8kz0kiJpzJRoLvlIutkdrbxyH6587kG3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uN7Ygx_z7gph5Mvm9zNKcar3LTXTOeML06uakYetT_4XWCSPY18U3-ZA4tvwrcCmW6BuvFzfpzzd4NCm_AlZtYSZTSGvdnALxKsvhfyCxFCDoS_IKKFBwfQd62WorsUxh-fGi6iYPmdx5K4HmM7X3Scg4mrHORlCGqir4Vhcy4_V8PB-8439V8jjjXrixXWHTk3mCu4VhcMZwKtXecf3TPcEaXnHwWrpqwJ8GY9mXV_lhT2K8E3Sih3RadX8ivmmZE8Cn-mOmA_8mpzCW1pDw4QQKR6HzPjNzrE_Bhr7FFWVnbCYH2uq8kz0kiJpzJRoLvlIutkdrbxyH6587kG3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahq509R6cejKpo1XI1IxS88WOjefyVY_pgN0lhmzV9SgpP72tCpsN0XHrDnyIB0c8yAOjqxNHuyW_kxJnZKbeOoRktLY4zc37FaHQVK4UG38NOH7Hcbc3jqrxg1K6MHz2HVRmeaScmAxzxxEqrwdQobzwqjjSW2yzElPRGLd4KvEgL7XRSWGz3i4VXG8_MG4gjZzD0-17DJ5nocjZJusxB--q93tjPigvdJLEokOtSqL9S262zz0iGkF2onXJD4sEmfU0Vs6UEJ9XA3jDFd-Gp_Klvw6wyGpggOmsxh-LaHKu17Sas_p9ID_vRJ7Fi4V7ecBHVK2SKy-uDic3TKcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3TNsk80NrGid6Y2KXtRg_7y938MHMP76UIm3QIUXLs6IrXRLMgkZBkDJijcvOkJDV81fxz-fRNpmmcmYtthU3T9uNux1oVSTE7W9gaoizc7tdmWnGo4ruGBJIQThikvgV0WlSp0Q3i06wrgw46LBea0p0w2HoAKwsVkOhVH_FU5MEcavWZkGnSVVSTxblhmkfByMpuzzGurL9ysDbyt7gEChGL8LDsuBOrNChbA7i1xT1YUeDTEDpNiwdp3e1HzaTUOE0xBEYRiFsTztxIvExTO0MvwmBgZXkmYWOdS2imnQh6vFFgZyj9t0LY1_NGz85JbTiLLtDuwIPNh5vszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQAQu4QGRgmmrmAx1TiISUP4MZ8RJw7k60uNrrH_FiumPmJjycEIe7yjJld9T4g_atTXEtiP1zm59MYe2lQuSFPIrqySiRXjVh63tAAC98jS20_MrnvWQMaUVhMfziSWR63HvLCIDUftSZO9LM-raoQa1vahjUTrfz6YPEDPx35XyEKpWJ1_SLtjWUejfMTSbfsetKH8vP0eibqT8LNcMWLSOfYAO7q_rK3gYxujcw3-teqG_pkxmiuwChiRF9hk6iOziYmtMGfGHJ5E57gG8Z9l5OoqjeDV_gN6UfIDpxp3yp_k-xCL4nky1cITLh1jTVzIothHA-wf-VJC6-T4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=iv_H4XIIapT0tnA0UOwdq0-4cmFoJUYBfQw5DGnZsYi3zHvrz4-yL517d0mBXV0qFvnbTeSJZHncHfYsArbnh9AVEszJhpMcuZxtHBEbsqyjGCKC-_axapOvU4prwdGFCh5wyuB-BNi77SMshD4qyy6rn9HpOGgJ5ctc7H7N-4rm9DJlPSCD0FXIafJ3XWvvgX9a92MRjwZ2nvIwtvOFIrPa2XuY0UxpMe6Ly81BImPy7FESElZ0gtI9qOskFy6qLkMoPpKkL2kTJC1XFQN2RuntjiBcK3CjDiB9UMVJ96QS7sm-tTyXKal7xxfHrdxvLgSFupMCrLyOxuIsmphz5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=iv_H4XIIapT0tnA0UOwdq0-4cmFoJUYBfQw5DGnZsYi3zHvrz4-yL517d0mBXV0qFvnbTeSJZHncHfYsArbnh9AVEszJhpMcuZxtHBEbsqyjGCKC-_axapOvU4prwdGFCh5wyuB-BNi77SMshD4qyy6rn9HpOGgJ5ctc7H7N-4rm9DJlPSCD0FXIafJ3XWvvgX9a92MRjwZ2nvIwtvOFIrPa2XuY0UxpMe6Ly81BImPy7FESElZ0gtI9qOskFy6qLkMoPpKkL2kTJC1XFQN2RuntjiBcK3CjDiB9UMVJ96QS7sm-tTyXKal7xxfHrdxvLgSFupMCrLyOxuIsmphz5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmWZXvoM72uNGNfGZPxJVPf5olYc9FDoDzrFHcBY-QEwT12iKDXkhxt2QT74JGd6gQ_GyWP91JTM0CaDq9qLYcD8nWj9rc3u4FmgybuWTIaJLmG-_4z1LQoI5N5WPum9ItsncFsaNZhwpnu1Q3DXE5_UPIr7fUni6lnaMMaJCqPkhq692_bDUFtHIZ9p_77DUk4pZ78rlm3FnEe1Yy905N0KDupbg7dkV33Yfy9zi9_Hj9TnhYP7w-wLgNe6vz9R2eHQiI6tZscSoKMw3GM9E9C_Qj3c5I1lZEQiXrtG7DBMXE3fo42EpbPOHaXqbttPGxyQFuKU8JQucDVaiQ-zoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8UK5vueR5pEa9nUYxsNaE4CVx9Yk10tXKXQQE5jByV2bVaXODdMFicKwhgtx_S7Ra8l8k1dZ8K05rpuHTPshP1O2y8WBeJWJeTeCGO65nx4wnQJR-sGS5dk_neZuIop8m1kEcN_l8JgzMaNLJdwWs3UwvfHiaCKXMxHjEVF3GaJw7AMqDtSZBM50Ko4s5HF0_FRJsRtShT8QqzowzEeRa_TkLuzmc-Zj1KGC405a3Our4YTthjEGTctPwCnipYfaHqME6SkY0htMhFW4xUiAD5WL88Zd41KEOR0jsAAPjNMCj0ObgkkdfgSlRndzWfz28KwjdgI01Sp5CBBBNKaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=pkcSe2xpAgtQ1N0IPOmcNOBSccI1S9nNcAMGizBamscx8cg_OEwH1lQJvhyfoT6iSJC3ZdEwBXGVBhpcQ9czzc-rpvzntkir7oqBc62zbs2v_28N6Xfv27M0lc9taZoMyngMDO4ukaLv1AqYhZjs_npgOVuhrXdZXxIa3KChwz1aVACN3aZQ-XULyS0pHkJXrKWSzDdOX8DQTGQBHJfjjwHbdDV35Zi9GZ4J7F6r1qt30sa-6lfSdP9vmf_82j5UKR27V5OAfWBhYkgjEubQ3I6EEhq77blDXZsfk19MZ2SKOof4Q8VnCha2mmVsyJLOnqUSdXmGNYYjeAlaudgvIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=pkcSe2xpAgtQ1N0IPOmcNOBSccI1S9nNcAMGizBamscx8cg_OEwH1lQJvhyfoT6iSJC3ZdEwBXGVBhpcQ9czzc-rpvzntkir7oqBc62zbs2v_28N6Xfv27M0lc9taZoMyngMDO4ukaLv1AqYhZjs_npgOVuhrXdZXxIa3KChwz1aVACN3aZQ-XULyS0pHkJXrKWSzDdOX8DQTGQBHJfjjwHbdDV35Zi9GZ4J7F6r1qt30sa-6lfSdP9vmf_82j5UKR27V5OAfWBhYkgjEubQ3I6EEhq77blDXZsfk19MZ2SKOof4Q8VnCha2mmVsyJLOnqUSdXmGNYYjeAlaudgvIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBnY-x9OWaS-dLHhI_I18JEiqPNwMO9a-9ToaezP_I-nRkHaOavnxnzQh0AEiTvqoisP7BlDNqpPnyoNM6eVlEg-a-jwe-sCqRk78Oj2zvu0KhVBil1nhFGfaHMGByEfLvmdokH3p4pJKOdjVNmfWPuKsCpAkyeoSUbr3lMHS89_ZV04mZX6_Y96y4ttdFM_uDq5VRECC0Pd1610q926Ql0FFo1aq7sM98_DM4kElt6YfGTs0TjzswWIA8c3wrJlK27VnzBUthPFB9N5G-7oMImkNFXv2WmZENVf7hzqCHO9Eu0yXhvzU6JskLdzfSQmRQCRwdUcDVH-M8OIzjPPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=W6BvFi11QIA_YFtSL87B0voeKMIzqAIUU5-QePjIbZKDbx4INGeeM1_4HnBw7rCjgC4upCEl8EMr-Y3PVgncRFKQVufjZGIjI9z-nFywN6XRgLrXx_lfQmRTFhwE47hNCLzJddNBzJEypBkzbg0LKhi2QviC15Kx1D0e6LAfRpzn_9CceH90TOF1Z4sjZ60ESQy74GackiBnvL9RMgac09TJ_cFmq5JcvL3I49EFjpCSyDV7f7ubI9Qa278G_Kn5sx7ZRfR0Fi_FlbEnhR7QHvCZ6zJU0VWG9YthXCzv85zBL4pWOdUdjj0cWxI94OvRtIaa7xCLzxviTvczAsz_76G0DqxQyDAqW1G_FNmO1GUpgCOu-Bi7ZLoN3ZovuzU9HnEO5E_uN5OfcVVr2ignhUpfB2jRMQOkz_V7OMO2CD9VpgYcliMsDzZwMmaRk1Y3v3gaFjKzd4uCPkajxFe2eCs1YixdsPAorD-9F4CPGbkiZJXw-UWJXjZ5y56M0V55Alsu2rhEO1ER0NfV-5PLkwFHXtQN_GlzqfhRNdIwlclDKVaVxUMit34L1kQ4siM-8F9BX6u8qx8BFnq6n17cq7NcnxmGE45Pz2UzrsWumkG0u0u7XSVYMMkWvdr_vLaB4b35QYrNLq1Pi2bTkO_Ur7E4x_WqMt5yg6Go4JbFGpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=W6BvFi11QIA_YFtSL87B0voeKMIzqAIUU5-QePjIbZKDbx4INGeeM1_4HnBw7rCjgC4upCEl8EMr-Y3PVgncRFKQVufjZGIjI9z-nFywN6XRgLrXx_lfQmRTFhwE47hNCLzJddNBzJEypBkzbg0LKhi2QviC15Kx1D0e6LAfRpzn_9CceH90TOF1Z4sjZ60ESQy74GackiBnvL9RMgac09TJ_cFmq5JcvL3I49EFjpCSyDV7f7ubI9Qa278G_Kn5sx7ZRfR0Fi_FlbEnhR7QHvCZ6zJU0VWG9YthXCzv85zBL4pWOdUdjj0cWxI94OvRtIaa7xCLzxviTvczAsz_76G0DqxQyDAqW1G_FNmO1GUpgCOu-Bi7ZLoN3ZovuzU9HnEO5E_uN5OfcVVr2ignhUpfB2jRMQOkz_V7OMO2CD9VpgYcliMsDzZwMmaRk1Y3v3gaFjKzd4uCPkajxFe2eCs1YixdsPAorD-9F4CPGbkiZJXw-UWJXjZ5y56M0V55Alsu2rhEO1ER0NfV-5PLkwFHXtQN_GlzqfhRNdIwlclDKVaVxUMit34L1kQ4siM-8F9BX6u8qx8BFnq6n17cq7NcnxmGE45Pz2UzrsWumkG0u0u7XSVYMMkWvdr_vLaB4b35QYrNLq1Pi2bTkO_Ur7E4x_WqMt5yg6Go4JbFGpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QN-uvpKD31Fiv6M5k-jDRBK7T6cZ9YnqkUQjT6QhF87pPerkWXFFotVRXrIzSyVtVUixcRBTC1Y0AKJyZJzv0JOPeRu8Y1lSJ42sR515k-h1omA8fgnLoR8_clogYyVlsVcfyeYnG3w19wzGS34hrCcq5FZQRVgU1hHd90Im3ADyUX0-ZuxiPqu9Gunk8KlzOzJutVEVKLjz2B9XRDHylIdPbNmtyec8c62vuNo2NstZDbk5fKLtnXFqxgpJ_qA0iaEF_qRgnd66ddEPTt4B-8Erx-lgQs6gwrIQk_RGbetvLUZRrjOLaap47dsu3d9v_WYNNK4OtAbJ7q0siJUs0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTifA-4cclfYDKNEA3m3NPh2oXLEdzkTLhb_IVNQefV5Xpz20Ys7EtBArc7m0xTtT5INX9-Z4Hniq47uiG5HZRMDhcFQOy6u8Mc4nhzFNofz_YIKHqcvUuMWFbyzAaiEGMwmuKKGb74w5pjz6K3bsiRl69wyB7BqFs6o3zNc6FMelA-6SAbGk8WeeButeoOCH9jEbwtFAJS67i23uxZvdM4Uko5WbRZcZcqkXNSQqyU4X21m6OZWdJJFVqWV-x_Yr-A6PAYbgCFpoo8UZPtpFt1B64Il-kVICjuE58Y4xXlblJhyPvPJa5aWFpct1gZTaZcSLZA6UavIro2lOl3omoi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTifA-4cclfYDKNEA3m3NPh2oXLEdzkTLhb_IVNQefV5Xpz20Ys7EtBArc7m0xTtT5INX9-Z4Hniq47uiG5HZRMDhcFQOy6u8Mc4nhzFNofz_YIKHqcvUuMWFbyzAaiEGMwmuKKGb74w5pjz6K3bsiRl69wyB7BqFs6o3zNc6FMelA-6SAbGk8WeeButeoOCH9jEbwtFAJS67i23uxZvdM4Uko5WbRZcZcqkXNSQqyU4X21m6OZWdJJFVqWV-x_Yr-A6PAYbgCFpoo8UZPtpFt1B64Il-kVICjuE58Y4xXlblJhyPvPJa5aWFpct1gZTaZcSLZA6UavIro2lOl3omoi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0TYElKEAussengcSTKoVnw0HSUgehU2LVP6Opvk9Go5Jm3OxeFf6UVVjCL6QpJUyazk86H3zz2ihe_y5sOJnPGbmnaTBdtauX5s6mA4SohYa4OFATr3Fdq-q_1318vlejYhqo9A47fsnCYTXn8ufq72_lEmM3p0RFLyIq4QwQyjHbsNC_H1FBcACN8rYG7LBOfnHw86rcdlCWhkSIi18xiTbJWqgI6ZI_r8uTKi9d8hlFd0so2EBtg2DzXokWjBYG9DJMz4IKd7GBjGAJrkE62LleWgtJ8xzddP5xdnSubbfy46XW2N1vt07pIxoXjExXvARhaXGDOXQ4wImr-bRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sh2c7CiExExDZH_6VF5C6tdVG9rMUcQGnyFGy0YG7fkVv3rn24zEBONEuOkVky__U2AwTVIl1V61XIi8mVoThO6LluGLhJ1_4gJmhR3v_I5fxTpXnEpIPNLcP9cOOjNzPoQyGVWIp7eU-3_x8m0hUUMY-H4QgroNE9B4eCmaYDS0EZw8QJI68S7Fad7iCMpkYM0MtQrAk-ekT4BQbhKGipAWZL8jx4YhG9ts85QvYURc-ny17Yig0amG5SznsBvdh1IoObbxCkjpseh2ytTZiQ9eXJV7pPMRNvE6YvpXC2lGT38tjBPnb7Aj-5LITqBLdIy8YkKIKXtM7dHMGB9LIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=kT_Yz0-OaC_skVOUkun-hWCwgHAdOTeIDLleWme5e5WOxeaQRyzNhT9soVYFDxEhS1H59svM89s6s1Hx8RAlYzr0Ly-C1zAgVnjJAA0wNLtptFQkVjKaKbO9eoKWHeYEMWYyZ1nHfWK1MNf1IRtUAxqOHYuPlZSrfDC4XnUsPzTm3H2W31D40C0TBU9XEm9ahezpb93I15PxlYr0DseWyLMC5asdEFCedC1EJXWtioH_RHYmwfksZPxq0fik3qv7ufraBrvCxiWdBMWsBu_ZL6zyKlxZ5K1K3QKo9ec2kbML3jjBY6orxh1PwYjtcBLowTtgCVFtpQqGRxx-5ZNJag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=kT_Yz0-OaC_skVOUkun-hWCwgHAdOTeIDLleWme5e5WOxeaQRyzNhT9soVYFDxEhS1H59svM89s6s1Hx8RAlYzr0Ly-C1zAgVnjJAA0wNLtptFQkVjKaKbO9eoKWHeYEMWYyZ1nHfWK1MNf1IRtUAxqOHYuPlZSrfDC4XnUsPzTm3H2W31D40C0TBU9XEm9ahezpb93I15PxlYr0DseWyLMC5asdEFCedC1EJXWtioH_RHYmwfksZPxq0fik3qv7ufraBrvCxiWdBMWsBu_ZL6zyKlxZ5K1K3QKo9ec2kbML3jjBY6orxh1PwYjtcBLowTtgCVFtpQqGRxx-5ZNJag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cyx5uVPLEA2ZaopxthOmVDWav-i1WRhMyLFuQ_7cQiy6Din7o_jW5WmbHWpM6mBE7bel3O8A0KfcOlYBoOHY4fnydk7oqcb4gpD4TDmSQRpQ5Gq6k7FsA7zpy3VjvuriRLZX26YJcohjafs6LhByLXMka4KL7F8uD6Odi-b1tEWl5uBVmUTIZghtUDHKh5C4_v2tHXgE_bUAJpTPs8q4PzTZrydWmiYdk0W_45UmNkyBiPTYcJxxzq0dyJwAbKzXEBNQ0o-cQPgsrxz7EI7bLG5zVxG_hSAwaTe7Bul2YUpO3741AqzipiiW8Ot4B57hJ5G-x-zVYiGWHXJuSasddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=LhOxDybPoruMwjkZfUTOYG_vhn-sOs4Z5z5URZYYrMrzd30Aoa0jmbAqq_pyd2XlIP3Ls5g7EVIKRC1DiRRjvSoLKgDQQRKXsGCUTrGODMThkLtEc61WdKlPsv99oZPk2px7FKySj95fGJSx3E4WMKno5Cv2VZJusX_WB1LIsDSF3pjHWwQc1U4M7YV1C1DmLSZUVLN8RG2GQAmAzzavMw2Nyqf8LEwi-JbKtryFu-ww0pze4DctnazNKmMGKEjyoeN567sRxnWGi8yetcVpjWQlmkO89k6D-Ac6fOifjli-R_Irsv_wN6inQBmovEFIZGi0DZaJgdsYzD8tyu6DUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=LhOxDybPoruMwjkZfUTOYG_vhn-sOs4Z5z5URZYYrMrzd30Aoa0jmbAqq_pyd2XlIP3Ls5g7EVIKRC1DiRRjvSoLKgDQQRKXsGCUTrGODMThkLtEc61WdKlPsv99oZPk2px7FKySj95fGJSx3E4WMKno5Cv2VZJusX_WB1LIsDSF3pjHWwQc1U4M7YV1C1DmLSZUVLN8RG2GQAmAzzavMw2Nyqf8LEwi-JbKtryFu-ww0pze4DctnazNKmMGKEjyoeN567sRxnWGi8yetcVpjWQlmkO89k6D-Ac6fOifjli-R_Irsv_wN6inQBmovEFIZGi0DZaJgdsYzD8tyu6DUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLyr99oRYnkZTbAjA1sQs8Cly_BYHRu_6yZR8qNglzO3yHNgJyl0QNeQTGZcJJw557HWOSkfU3iGY15mE-ccgxMyIcc4NR2mF5YcKOOIrSI-4q93bt_VIY5HeIvqgCum83nduAe-G-OVwSu3DS7qhJThL6qW2Qc4IUdVJ7yqn2iLcOYAWbcFSWm6mMZRBM6RHZcSaG8D7qRw-SVf_nigvaoWKsWrIpb_x9QuW5qeZcduJ0TwvJ_Bh4dmP0s4FI3e-FcJAyxPr9siI8bkn6C_Qytr7jBBU2ln489Ui89hK7y-gJSZXxEl12GVJvy3yxp-0FwzcTSxPNSvGVxVgODnIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lcUCzENcYt2WcoZUj3gjWxv5E2F4arP1rtwMrtNQTtVPKNQzOgUQJKraXVDkBYRdeKME0MAjSsYrDgihDB395w86eHf-v9KEY4zv9OtLRYWfPuGk6XanJ46avGOJGHnVqI-ZbFbF_JJHH7dkwwS_cWl6cgPDruD15ePrG2SqMr7UKUSnmLAN1hxkUtfK9olh4y2sO6VO7if_615gi12wbDnyhY2SWUsFP0ndOanT4ak6ViYHx4OYTYzhmyPwT9oGo1BA3TUXeqf4-TLMWO3yMhAJTYMg4uZ_z6vtTKSPcaQO_CeCJVNSOyD5LyiAQF6rtAc71sInxRn5YSM_T7e2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=op_j40fiUFlCRR6C7EAfh7y9kuHE-MqTWjFbzNZmkdRtOGqeP-Prxjv09LamLuRBRFOOlx5PlGtjG6JHJIM6blNA2EDSMnbte2_fb3ujehQsKfsZUGIYSV3_ty99qYjHh5nMV9TcM8cIsUlkC8OJ9N7ds1wEDGkH4EUq1KS4rClatC1dUxuWUb9KgszgoAeAb70TDA9hOkG7x6_tcJT7oaMQH9GnvMTdjTa75wXp3vNiBY8aPclPFYROMOBvNk67AdWlqqKSvttyEy1bClTIzZh9CypVeSmRK5sLfZRVJohdREyHALnpzKjy5vA3L89Lg9mUog8_6gNtJce1TtY0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=op_j40fiUFlCRR6C7EAfh7y9kuHE-MqTWjFbzNZmkdRtOGqeP-Prxjv09LamLuRBRFOOlx5PlGtjG6JHJIM6blNA2EDSMnbte2_fb3ujehQsKfsZUGIYSV3_ty99qYjHh5nMV9TcM8cIsUlkC8OJ9N7ds1wEDGkH4EUq1KS4rClatC1dUxuWUb9KgszgoAeAb70TDA9hOkG7x6_tcJT7oaMQH9GnvMTdjTa75wXp3vNiBY8aPclPFYROMOBvNk67AdWlqqKSvttyEy1bClTIzZh9CypVeSmRK5sLfZRVJohdREyHALnpzKjy5vA3L89Lg9mUog8_6gNtJce1TtY0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=TkQNSrJdAHU_ZZTd69JYr7XJVnhx7WGdWbSKMKVmRu6BNsBFfcGJz78tHH8HbhbpJA8Ty9s7AejoYJg7KITw2D7LCYAc5olV8qHr-nbjiGEzRyHewa7-sJ0IjQRmglfdJWcSKlopynAJKFkadcTE1-WdgvXF8jMP9icU80RyXYuYP18iJ3SnSXURT9alqbrRfKEDeIx6W9Oh8B7Ie80zSmZdJR8st2AUGZtgDILk8UuN6xnlC9ZZR4_QkQXIXiGmr4oOIWF8w_qHvzjqqryCCATqMZcl150fSivyuRNuM9bQdiDNPHvUEvXAgE9uNM9ccTSwMbOj0miwVXPxrDhRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=TkQNSrJdAHU_ZZTd69JYr7XJVnhx7WGdWbSKMKVmRu6BNsBFfcGJz78tHH8HbhbpJA8Ty9s7AejoYJg7KITw2D7LCYAc5olV8qHr-nbjiGEzRyHewa7-sJ0IjQRmglfdJWcSKlopynAJKFkadcTE1-WdgvXF8jMP9icU80RyXYuYP18iJ3SnSXURT9alqbrRfKEDeIx6W9Oh8B7Ie80zSmZdJR8st2AUGZtgDILk8UuN6xnlC9ZZR4_QkQXIXiGmr4oOIWF8w_qHvzjqqryCCATqMZcl150fSivyuRNuM9bQdiDNPHvUEvXAgE9uNM9ccTSwMbOj0miwVXPxrDhRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=Cx8TzHpIFpS6rPWm7U8vwf5ZVnpu1B9piSK1QV6RNvsZbSeeX3ODs5gIPrBg8yh2ZBs5lynC9cnhI8HSB3_c5cB6AbSe4yiZPZxDl5OOBlUp5OwsAggySYkZpgI_7tMBi8eW4W5GJVGwkc2p3LZTFLUVWRInyB8m8NX1ylr6Y-tyCIUftPGAjOnScULsv9EEo9PdM3oWB4XISj6FZS3iw9fmkf-hpNbQl_tNu2DrkErX_EfibI6Bng9nfiEl66hV3cakNgru2QcH253znHWFiTRS9f-Vmul-njIKszgbMW4WrkwNftrWx4S6DrTZ-TOzT5BAjL0A9n26naCocqMrQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=Cx8TzHpIFpS6rPWm7U8vwf5ZVnpu1B9piSK1QV6RNvsZbSeeX3ODs5gIPrBg8yh2ZBs5lynC9cnhI8HSB3_c5cB6AbSe4yiZPZxDl5OOBlUp5OwsAggySYkZpgI_7tMBi8eW4W5GJVGwkc2p3LZTFLUVWRInyB8m8NX1ylr6Y-tyCIUftPGAjOnScULsv9EEo9PdM3oWB4XISj6FZS3iw9fmkf-hpNbQl_tNu2DrkErX_EfibI6Bng9nfiEl66hV3cakNgru2QcH253znHWFiTRS9f-Vmul-njIKszgbMW4WrkwNftrWx4S6DrTZ-TOzT5BAjL0A9n26naCocqMrQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=jFyFI0mQctkvxojkJS-opFSheMqau5yoU3f63lpeKAvY8_i5dNoBUB3cFMkbN8fn9x4HRqMy8Q5xI5bM1TjgGrFIvUBhKanQpKHfcXJiNRibc2djk2nea1Iz16Ooy4gkGZuYxQ_Hf1iZ16sDoBCI6qPRJoCmI967tviEv2_osDUW1e_X6ZuDq4dCQ5g8Hpyo4kj757pv10SxWR68rxk1vKeK9NYiOuPosokVAErN7gkIxQfw0OfVGeOXj2DuVf-pXNlUaRg77GQk5RU7IgK0dHT9h9SrxA8MXmmKUSOGZPRnG7Cr4SPcx9YkHH0XYnGyvRJocu6bpirnu-WE5UjBOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=jFyFI0mQctkvxojkJS-opFSheMqau5yoU3f63lpeKAvY8_i5dNoBUB3cFMkbN8fn9x4HRqMy8Q5xI5bM1TjgGrFIvUBhKanQpKHfcXJiNRibc2djk2nea1Iz16Ooy4gkGZuYxQ_Hf1iZ16sDoBCI6qPRJoCmI967tviEv2_osDUW1e_X6ZuDq4dCQ5g8Hpyo4kj757pv10SxWR68rxk1vKeK9NYiOuPosokVAErN7gkIxQfw0OfVGeOXj2DuVf-pXNlUaRg77GQk5RU7IgK0dHT9h9SrxA8MXmmKUSOGZPRnG7Cr4SPcx9YkHH0XYnGyvRJocu6bpirnu-WE5UjBOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68221">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48590994cc.mp4?token=HrW9Ucn0xRDmzX7Zbb1pe5zmRGNFyxtD5mVGHqRD8kPnKgnV1KLyPBjvd1N1jZARn_dDHbQKEOf9pHm9cvzdkK198lipZmGl7FtuOFRGCoKSrwOdlrFUXKacX8rLyQ4yySuMm8KKaqCRXPXNd-EhoH_NP0lQMCwUHAE2J8MIOdXHFu9SDuHYLCEE_1PpIqW86R8aEeKBLsx92GImMLAdcTNVUsBUtNTtGnO3E7wi8bj0pOj0GK2H_McbdaOn67qjVnhMbEpHQAvKWtzLAGJ2Vc_wABBpk8SdY2X_T8wkw70jri9uO7tlmHa82QvJGcCt1348jz0XdXXl1XyjSrWJug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48590994cc.mp4?token=HrW9Ucn0xRDmzX7Zbb1pe5zmRGNFyxtD5mVGHqRD8kPnKgnV1KLyPBjvd1N1jZARn_dDHbQKEOf9pHm9cvzdkK198lipZmGl7FtuOFRGCoKSrwOdlrFUXKacX8rLyQ4yySuMm8KKaqCRXPXNd-EhoH_NP0lQMCwUHAE2J8MIOdXHFu9SDuHYLCEE_1PpIqW86R8aEeKBLsx92GImMLAdcTNVUsBUtNTtGnO3E7wi8bj0pOj0GK2H_McbdaOn67qjVnhMbEpHQAvKWtzLAGJ2Vc_wABBpk8SdY2X_T8wkw70jri9uO7tlmHa82QvJGcCt1348jz0XdXXl1XyjSrWJug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68221" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=FpHNNQRBhE5gghYf8qT0KKm1BWfFUVxHZoQnQ5Eqv-8ueZozeyWsRWEVuZ58_-F2Z_KX2_V_54u17-PBUhGY6wYuCUw3s2lXHxrIeH_rqqtfSLsCytGHZixy_n48VP955ooMG_YtDbXdKuC__z-rGsRhZr7fbGZTRN82vA_2qMedYsRXUXuxd4lBCz_RfecORF2J8KVc1Xm8f8eAwjwWQ2EHICHlogNC4GIrwCZydw_5Zl98TQrSqcsbbHYXDo2J7JpwNTqJ5dJEmMo9TWhyKAveol6KKRTxn3xQM9SBslUjchNdjHz7KXGpErdWY53mkuFfxK6pcawtKK9cbcMv1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=FpHNNQRBhE5gghYf8qT0KKm1BWfFUVxHZoQnQ5Eqv-8ueZozeyWsRWEVuZ58_-F2Z_KX2_V_54u17-PBUhGY6wYuCUw3s2lXHxrIeH_rqqtfSLsCytGHZixy_n48VP955ooMG_YtDbXdKuC__z-rGsRhZr7fbGZTRN82vA_2qMedYsRXUXuxd4lBCz_RfecORF2J8KVc1Xm8f8eAwjwWQ2EHICHlogNC4GIrwCZydw_5Zl98TQrSqcsbbHYXDo2J7JpwNTqJ5dJEmMo9TWhyKAveol6KKRTxn3xQM9SBslUjchNdjHz7KXGpErdWY53mkuFfxK6pcawtKK9cbcMv1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czlO-LIWEns8HPK_AAZUIPjuX3e5RrVNvYDyw5DO2mObGg9O6haPw4UlpP0kEozNSLAywywYjDH4IRjotOb3KV6Ng4SsQDJNgixjLIpLhk1o3Wmv8uYTTxcIAscefNLfDGW_NPyWn4Yeo7EW9UXhPsPRKcXMIsOolCb5bqKK8IosvmxTIsQBj0YEXeSjkOAYO7cnpl1gX3r-78KlJzF2Ptq70Dn0jMVZ5nEtzNAP3jWCAtY7JzgUqOlwlJli5QTsUzEvlTnZ5BhRXi_F5d-lGeVSoDg55VzTSc51ddSYBv694TETyLeyj2uUFlEkzcw47GYvihql4_tn7Wr7zpWjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=vzxH9ryU8yC3tUJHE38x02UJ6-Ro6NeZ_tZY9iIJShbhsAttKBBfji-HS-iZ9kNDXedl-P0EOn0986kHug-HnGA2b7e14gxe1n4vFaisFlWp-f3oyTRRrr8L5qzOOEWPhQnIVG48lqdEKq3BKDsUX6xvaqKnD6bOA5Lzyuv3gsO_fACTAjvoyaGDBpURtIVh4PsXQVkYPIwnHtuaxf5aQyxrNLG1jwXkxbA4frEnjtGYxrA9ZAdpUWIbUN31jmsDj1EVBe0rQoyZVPkv5_kHuHaM8EfYvX5ewnCzI1AbEgTVjjP0E4YLnkgTGYQqU3zr8jRUMVDWXg6UpZ165-d7ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=vzxH9ryU8yC3tUJHE38x02UJ6-Ro6NeZ_tZY9iIJShbhsAttKBBfji-HS-iZ9kNDXedl-P0EOn0986kHug-HnGA2b7e14gxe1n4vFaisFlWp-f3oyTRRrr8L5qzOOEWPhQnIVG48lqdEKq3BKDsUX6xvaqKnD6bOA5Lzyuv3gsO_fACTAjvoyaGDBpURtIVh4PsXQVkYPIwnHtuaxf5aQyxrNLG1jwXkxbA4frEnjtGYxrA9ZAdpUWIbUN31jmsDj1EVBe0rQoyZVPkv5_kHuHaM8EfYvX5ewnCzI1AbEgTVjjP0E4YLnkgTGYQqU3zr8jRUMVDWXg6UpZ165-d7ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=LcFTfETX71IzgSL3qlmqF8u_3l_Pf8s0WoiVPFvCMGf1t98RDc3hU_VxcS_gGIOrebzer_z4z6_DsMtC-sRByD8lkhb_chjrG4oUDuMwsMSTiCVPPh_11VvJFehXc81KiaXa-lWeqDjYUWEy7tZ0cumEZ1LTt9WFRB1ia3Hsft2M2VOiinPht-J_bHq6vXOYDrWnat1Ws9v9oq1Y9sNVkTs3DvkGK3bnJIyr7_syic--uelAzsNv7TqWzbqZGQZM_H47ceWqfY5NilLgnJhugyON_aKTb1bG7eFH2U8_dkTFE6s8cBPemd9UadeiXUMkjNiLjPqgXjnVxBa6ms4LWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=LcFTfETX71IzgSL3qlmqF8u_3l_Pf8s0WoiVPFvCMGf1t98RDc3hU_VxcS_gGIOrebzer_z4z6_DsMtC-sRByD8lkhb_chjrG4oUDuMwsMSTiCVPPh_11VvJFehXc81KiaXa-lWeqDjYUWEy7tZ0cumEZ1LTt9WFRB1ia3Hsft2M2VOiinPht-J_bHq6vXOYDrWnat1Ws9v9oq1Y9sNVkTs3DvkGK3bnJIyr7_syic--uelAzsNv7TqWzbqZGQZM_H47ceWqfY5NilLgnJhugyON_aKTb1bG7eFH2U8_dkTFE6s8cBPemd9UadeiXUMkjNiLjPqgXjnVxBa6ms4LWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjveK-egX28ZlWaw0sFwnEdhLtVL_F9Fj4pQHFvh52lX1S-goUaafN1hQNvkWMHFsH-IVk1J4Yo_emJW7G3hT9Ubi3bMOFSCn3cZRZz8HZO7Ysle504BAu2OjxjEjT2jGQHaJnFYSmioXbhRxiknMa8mr8lzT7tyRBWk93jyRhoHyHZCIIrpNtMO0OlPO_PsHs44Xsr5ZqkrZtxBHMCRDSn44NhdpvsjwmqvvS5yVedwy3sFYZRayCaVGX4LCb4M78EkWeml0mCkRfWx34xUFOSZ2Pa6qtpYlUM0u7z-xdLeMpdLTppCrqTKOzn-l_2u-MO8c4X18B6rhRVV-SOGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
امور کنسولی وزارت خارجه آمریکا تو ایکس، یه بار دیگه به شهروندانش یادآوری کرد که هشدار سطح 4 برای چند کشور از جمله ایران
🇮🇷
، عراق
🇮🇶
، لبنان
🇱🇧
و یمن
🇾🇪
صادر شده.
+هشدار سطح 4 به این معنیه که آمریکا از شهروندانش میخواد که به دلیل خطرناک بودن اوضاع، به این کشورها اصلا سفر نکنن و یا اگر اونجا هستن فورا ترک کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ic8YtSzT8aE8nQRhLBry_7EEXFHjeks7xoowZu3zON0B5MsRSzvOWhlq4ETZxy7Lwb5jNRyBgrJ-30XCP5cm8oASKG7ooAYrxbidskLoBgco0w4C2Au3HUB7sER1mtmWhWU9ZwvD2sxlfMalZjN7tnbF4_4NmimC33QmohF7sRno6KA7KdF87_LIJNu7fLR_qrJYzJGoy_CgW5Qe6mHs0fdy448B0zi8861gI819BdYPoOOVNhVfFZjYipz-nz3tKsSbZXwq9kbBo9cE9OPDUxydW4a73s_0Ho99PBF6C9g9HPiB6T0urB7KBNKkJ3HkADxeUkKH95RyCdDOeqM3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihAOXd2sehChRBXo8CjJjGXL906c1waDIwO_4ZWcgmbTCAxssKKpHmyCZa938om9mK1HPTD1jWsysarh-ead5ClUqoo1jMfPGDGKgBiU0feoKe01nIrX9AwTqpfvCnR9Ys-oC7wMD2DMq7H7QOHSHbA6TTVJjHAKncMbl3ItbgAEdSSIR2QUnMDDDUdsCCRXIm98EKc9oIymS3u9xY01h7OxlBMVPfgCfXtvZXAC1PTCuWLm4GvEg5q-xOecMfxkMnRVxdmYpmYc2595DapWacgANHj8cCvJExd_NoY_ouvZ1h1jPQjdHBNl7CUDp48cYaf6FTmw35bQXeoexsldtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H263tPIRktWVZWOkM74wEaPQwb9PNguicECk83MWF5bDMumvUcIzn4FLnQZQswjeq5Q0y5zht-qmQlRCDkNUX1zP-0tszhNM4tXsbZy8IYKJwUYALc9frAyCotWiJD6rI4sZfFlKdSDWri-KLk8pY1QtBGzbr5e5sWJaAE0USBq-UbkjAsaOQUYnAZgwacAng9wJY3RIF20ZF7ONXuIkVSy3N7INWT13z6LGObklBw__Yy7JXeOOqYz6Xi0jtFN3FR1wHHZasSi8WmpIPYfdrVdB6m3lsNj6N6RRDJDQ2sKG7upB6webPeme9KXnUqeVoNk0bdFX7gu64X4p4uoziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdweGbvD72clKFD6N4fFRCHXmrPqJCUo4gfdDSUZMXpTBbqltUN3-XmkZvu_Caw0PjzN-TamlOQQkDRJZmkTGjLftyzCguuNLSvTPeLYlKovRyNePHYx58N5MWeU77rEyFO_3iGuksD8jv-5lgQvTuNH1WuQTgRhkuFLhCR5IAREOmlzIiRwWAtjrMBM7zkCrVsqGSL2ZzdUMjcO_AYWVuMijOpk_Pv-Q39Pjzzso-2y7BJRc0eGF7HiD6mdShygDtBzJAnJf8afghLdXH4U40ur1VM9O5YkQSbyYNYUoIgAD1iO_SzwoT7YxMfe8N39C-OhA6sNZbU-4rQ9lCO3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlSFAP7-_CINyd00VEwCjo4r2gTj8tp30NUp0o5cOXWrTXNt0blsBbA0AvxuQvtF6Qg2E5l6ioHz7kQwpUYgFrbbNIBRKYxRqU7WmGVxCwxodfdGBMuJG2kGg2qYxNIOSfLUZarUtKQGRG6-s6dNc6S7fTsnQNIBLe71xh2W46UaJ6_vPgQZ6fWREuvT0kqnS2xCNXDLFEpjxocvNkatkPPpzV06arLlF3NRq-KFYG3sDXST7eLtMghPR64kKbnb3InINLD7Nd0mMr4bAo38QnC35Va7VXM4tkvePKset8wpS4_wQdnnugXcc2cekGRTI8RB2vnl3RRd7ye9zGUKFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fERPIUU2wJcHKoXnjD8kd1sfPm4U_EiOM4TUUg9-Tx9oc9siIPga2KC2sRNC0hHLkpHyabFlGsaGHJbH9-unGkJlg7NIBkSjx1M7jPtTw-GYNXVS5EqPphsmFzAw0dF0eTmhCmrFAKP2clj3o-2Gv68BkjbI9QXVrWEMJgIXOmkxbE5UKFDg_T4cDxNz3_hUgYGARnC1tW7erBL2O3HPCv7mYhq3S1dp1Oh20vbslq7fJzLSZf4aYUycis7A_NEqKgyybwCweLdw8n3IKGy-f9QKHQMuCqzyCxC1Q8QzCpAfvpqvWQV3k-QhDqZdWv5AcpuU3vW1T1AX6XqbepCXgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
