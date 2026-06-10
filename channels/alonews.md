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
<img src="https://cdn4.telesco.pe/file/e6jl1dYsBZ9azK4PTMlG0qUNCGQ0njZ7HlM0oKxDhUrMXUwMpt50G8-4V5QwQ2UFpHcd2Gvpgw9E1-gMcman9ooMshQQumGURn1educ4WY4HuCGOOXd8YDpDBs1mNcznSCAQUw7WyUrc8B-RM7zHtBZEaLYFKnAVOLymFU26MD-fSQXV22aFwzCsWRz1xeFK1DmSV-9uT3owYeHUfQwM5iIwKSyghDSFM56Iwxnu6AmgV5kfLR0jm95-WyOKR9OVW3QqRQlzCrEIC_Dqaej5HOCpgvwk-PneUKFDXPFl00_dFWq2lzaHYSPxBM7rdS7IyQ9ih48DqJApWvYy3XO_eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 14:36:43</div>
<hr>

<div class="tg-post" id="msg-126785">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دیپلمات آگاه به فاکس نیوز: پس از رایزنی‌ها با ایالات متحده، مذاکره‌کنندگان قطری صبح امروز به تهران سفر کردند تا با ایرانی‌ها دیدار کنند و با هدف پر کردن شکاف‌های باقی‌مانده در روند مذاکرات تلاش کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/alonews/126785" target="_blank">📅 14:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126784">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فارس: ️انهدام یک پهپاد در آسمان خوزستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/126784" target="_blank">📅 14:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126783">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
خوش چشم تحلیل گر ارشد صدا و سیما:
جنگ سوم تو راهه. این سری قراره شدیدتر و بزرگتر باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/126783" target="_blank">📅 14:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126782">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-fWphkNSs6ORSAD7_tfBJGn9KOZGTFH5QAhD72Bbc7pcpVmDumJSSpZam9Zz4ulJze_iblPhEeCwixZO8aAzWF24KdAaP0KUDEHDeAKcSqHhGTbn03yoKjAWhq3dnS5ju8HltkmPB6eEzyoGWpZtNBqQ8erMLij4SgRLI-7fkgAtaPIu3seNNdemltjmH46nD3DkBFwV6ZrBJILRn8xnTHtfbzC4hmV2oEFfAI9KUWIvPqvRhh24HHIU4WiWWNQGCngWJy8aE9Etolmt6TfWKuEuY5PQlZQNm0uP_g0ghU6RZ3kYBZSW4578HVxY0ekAt3yPxsFSpyx4snQXdJ3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار به‌ روز شده از تجهیزات نظامی منهدم شده ارتش ایالات متحده آمریکا در درگیری با ایران (۲۸ فوریه - ۹ ژوئن ۲۰۲۶)
🔴
آخرین تجهیزات منهدم شامل چهار پهپاد MQ-9 Reaper، یک پهپاد MQ-1C و یک بالگرد تهاجمی AH-64 آپاچی ارتش ایالات متحده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/126782" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126781">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دبیرکل اتحادیه عرب، حملۀ ایران به کویت، بحرین و اردن رو محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/126781" target="_blank">📅 14:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126780">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=AN-xZp9HRVEOPUQhkkC91qD1PZ_kfsIM5-GMysmZKyhCiecZK2uhy-gKtn35erJeVa0an4N-VIhq7lXP9QFCL2NIfYNm3BGZ3Kbew86CMhzTS4qIgxeCCs3zkr_PnFKWEBK9k0UsWKMu-vNvOASGWvPz3pQWoFVzqIkvDwsBBptmbKHRXitkwuNMv4p5WvRHpQxLzHNfUR2S73rCn3JT2FbJZMxOT5Oo4KLOLKqU8CmSE_V3s-JVVJf5QtaWqh2pC1qsvk9h_KsXSbHUqu-1wFAlVw9SPE_kBBOKcAdkvM6Oq0eqlcNDLcn_OWmxDVq4rlx0Fvgbw8k28JRiRLushg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=AN-xZp9HRVEOPUQhkkC91qD1PZ_kfsIM5-GMysmZKyhCiecZK2uhy-gKtn35erJeVa0an4N-VIhq7lXP9QFCL2NIfYNm3BGZ3Kbew86CMhzTS4qIgxeCCs3zkr_PnFKWEBK9k0UsWKMu-vNvOASGWvPz3pQWoFVzqIkvDwsBBptmbKHRXitkwuNMv4p5WvRHpQxLzHNfUR2S73rCn3JT2FbJZMxOT5Oo4KLOLKqU8CmSE_V3s-JVVJf5QtaWqh2pC1qsvk9h_KsXSbHUqu-1wFAlVw9SPE_kBBOKcAdkvM6Oq0eqlcNDLcn_OWmxDVq4rlx0Fvgbw8k28JRiRLushg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس: مطلع هستیم اردن پایگاه و آسمان خود را در اختیار آمریکا قرار داده است و حملات به اردن پاسخی دفاعی بود/ تاکنون ۱۶ پایگاه آمریکایی در منطقه مورد هدف قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/126780" target="_blank">📅 13:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126779">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553c628858.mp4?token=la2hQACZN299M5hHoq6gswjOXNMXL5PwZ-8Z7Qn9y2-INhgbmA3u-DORFBI3XLKWhaf1LWurcWf2hxZoK4xnWItDCcc5Vx_PzFwEHO5nklKXXnppO-0DHOOhHRNwf_kW5VKoJRJxStVSSytFwXwZG6kHFwLKK52_eViEDzZ20SzsbGyA_G2NPviUPw1QpyETAzaMWGankVf9wrJkt5osWfxDwHJa0ajfFR9paAbkXPtARjqSR2J38TLuN5wWO9jmj1TVY1tOd-1ni_2N7fMF1vqFQpyOyswX-tlVWrANX8QcznE0EP1RXhz_XK4qQlwwRGJ6-_8bYzzzkMwkpwoemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553c628858.mp4?token=la2hQACZN299M5hHoq6gswjOXNMXL5PwZ-8Z7Qn9y2-INhgbmA3u-DORFBI3XLKWhaf1LWurcWf2hxZoK4xnWItDCcc5Vx_PzFwEHO5nklKXXnppO-0DHOOhHRNwf_kW5VKoJRJxStVSSytFwXwZG6kHFwLKK52_eViEDzZ20SzsbGyA_G2NPviUPw1QpyETAzaMWGankVf9wrJkt5osWfxDwHJa0ajfFR9paAbkXPtARjqSR2J38TLuN5wWO9jmj1TVY1tOd-1ni_2N7fMF1vqFQpyOyswX-tlVWrANX8QcznE0EP1RXhz_XK4qQlwwRGJ6-_8bYzzzkMwkpwoemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه: امنیت ترکیه نه تنها از هاتای، بلکه از حلب، دمشق و بیروت نیز آغاز می‌شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/126779" target="_blank">📅 13:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e17a15e0.mp4?token=LBJ0u25PWL9MZpzYMjkDiWYyOF5i6zm0BsAHIwMV3Nu7vF-CW97r_5Zl92fPZFMvEuvUE08W9YecQ4eOrQWe-cpxDFhd4a7hCSJEFzp5CywaAzlIrNwVKlk2gqrURp2X4kvedu7tXYmVUrbVf5jDoTS5mHZPB46SLcxHGFjntIwak3R2-PVNLI0Ok4RuJly5mgLulpykHaIX9yzfALwLOS_M9el3U3bExcDukp5AAu51tCGyKiVzYoorgd5Gck4psFblLBV6Gd-51tj7NaSHN3Ez2XgzKBepf0-kvPbTZ8ra-Bd_2fgyXZ7LvlHrNZ8UixJQTfLS4075N6ocFo3BlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e17a15e0.mp4?token=LBJ0u25PWL9MZpzYMjkDiWYyOF5i6zm0BsAHIwMV3Nu7vF-CW97r_5Zl92fPZFMvEuvUE08W9YecQ4eOrQWe-cpxDFhd4a7hCSJEFzp5CywaAzlIrNwVKlk2gqrURp2X4kvedu7tXYmVUrbVf5jDoTS5mHZPB46SLcxHGFjntIwak3R2-PVNLI0Ok4RuJly5mgLulpykHaIX9yzfALwLOS_M9el3U3bExcDukp5AAu51tCGyKiVzYoorgd5Gck4psFblLBV6Gd-51tj7NaSHN3Ez2XgzKBepf0-kvPbTZ8ra-Bd_2fgyXZ7LvlHrNZ8UixJQTfLS4075N6ocFo3BlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان: ما کاملاً آگاهیم که هدف نهایی توهم «اسرائیل بزرگ» چیست.
🔴
ان‌شاءالله هرگز اجازه نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/126778" target="_blank">📅 13:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bihr3WNM6a0V5HoKPKkV4W9750qK_xgOqf8cquAfrYgufrHWZ0-aRGlH7Kyoe8BdvN8pjF5qEXE18SWsOl-uWheoJ0taTJUdL9-rH_m61M6sx0rcgswPm-gGf78ffM5R3gFOgmyioCdM7OLJzXm0GbQhg9TnISnBfc3sMwEHIxaLpoXfr9bhUHyt8h6QswjLZjKQqjrh1nSEjXYMYhZeUObCKisLQGGzon6ow0nQCuP8rQPvliFqWMcAm_XdNIiFl5oAfc8dtKKgdYVlso3x3C-JrazoehVH0ANKaip62OYJdkRsE_1Rbih3fuBbgI6Oo9WcE_sG1roHuGz9aITQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuMtHiqbo-iESIPbJHTm4n2dy9Cp8jlKCm1K5gBoI0-N_m1JHSh2ujFR5fmY5_KW8RbpY9BkeKfLajVagOTPI0b98hAaJi_RKDjLzba5CB3HkNIy1dlX_K6sJNtlBWMoNlT-cxEUzRIOCVeYFCnGRC-cVSmnJ8jmXZTKW7BH3F_lBQYqAm6FgXiphllv6bAYGEEYV02jqU-6dD-K0B7v9BTmuDXbZfnoWuWcDtffSASIdXx2ylHMZDbzQB48K1xFzowVWKrBqHIW92OpmCX8FcZe4E4yRqrKsX4amJfxKRr9rhFa3xHYsJ5-_cw9adyd5RXKk6BNm6rE2mVDbNDw2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5241ba3243.mp4?token=TynWlZJG-t3uXXcwW4zqVS3lqXTKxmTB6fLMzTabfOqPrwTIlNILACk81cFUXEpE3J-iaV5GCbZ6PjlxHoLAap3AgP6vS5PsBnDQ2fl-TAH5c6ROODe9E4yXuz9s43IuGp0iG-wraQD2KjU0Wu-icR--5-dJyXkxhxUuyM0kPyEMWCpIs_zdARiKNhIp7ZULddiTq2yZj01eS2fWU4c1uWFxMv9yr6Bw9aZpd-w8h3wtzUkb5JduJNkuno3UBKNhGQD03YRTwfMqYZa3Jb9qZJB5WM0p_LJYCptGpQ6Up-37puiqjikqnTtL87NX-xWiqxBG2riCUd1k_jSiqzzSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5241ba3243.mp4?token=TynWlZJG-t3uXXcwW4zqVS3lqXTKxmTB6fLMzTabfOqPrwTIlNILACk81cFUXEpE3J-iaV5GCbZ6PjlxHoLAap3AgP6vS5PsBnDQ2fl-TAH5c6ROODe9E4yXuz9s43IuGp0iG-wraQD2KjU0Wu-icR--5-dJyXkxhxUuyM0kPyEMWCpIs_zdARiKNhIp7ZULddiTq2yZj01eS2fWU4c1uWFxMv9yr6Bw9aZpd-w8h3wtzUkb5JduJNkuno3UBKNhGQD03YRTwfMqYZa3Jb9qZJB5WM0p_LJYCptGpQ6Up-37puiqjikqnTtL87NX-xWiqxBG2riCUd1k_jSiqzzSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل به حملات خود به جنوب لبنان ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/126774" target="_blank">📅 13:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126773">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3800f788.mp4?token=U6FLc4pheES_tJmWe9aTiaSkID6hfI_SU9iVK0XovxLv3rPBmB_jHqw7uo9tTpLOMnNw9mKbtUQwDJcq1nc4S78PgmnIcyC4sR5Wh1icIwg9xaeYWckAG9HUlSnyTzu_KzBkMRPZzg9O4jZKlqMl4f6O1jj76iRJLVBv74IHDLii5d6ISeiIa7SsqBfTSNildZAx2FV_ukAVg4je5CmAIqU2AIBMPk7FPLZNmmoAhAQB6wOmDVIcN3yBYDEAoNGJW7U9amwX0-Nbmdepo3uw4fH8luWnyEI5wrgLHMv-JVBAQgr1X_kzauztvyvHSkX8fdSc8SnuRI1LUlZkg8mCCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3800f788.mp4?token=U6FLc4pheES_tJmWe9aTiaSkID6hfI_SU9iVK0XovxLv3rPBmB_jHqw7uo9tTpLOMnNw9mKbtUQwDJcq1nc4S78PgmnIcyC4sR5Wh1icIwg9xaeYWckAG9HUlSnyTzu_KzBkMRPZzg9O4jZKlqMl4f6O1jj76iRJLVBv74IHDLii5d6ISeiIa7SsqBfTSNildZAx2FV_ukAVg4je5CmAIqU2AIBMPk7FPLZNmmoAhAQB6wOmDVIcN3yBYDEAoNGJW7U9amwX0-Nbmdepo3uw4fH8luWnyEI5wrgLHMv-JVBAQgr1X_kzauztvyvHSkX8fdSc8SnuRI1LUlZkg8mCCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم از آتش‌سوزی کشتی در سواحل عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/126773" target="_blank">📅 13:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126772">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
اردوغان: اسرائیل از زمان تأسیس خود نقشی را ایفا کرده است که صلح و ثبات را در منطقه ما تهدید می‌کند و امنیت ترکیه از بیروت و دمشق آغاز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/126772" target="_blank">📅 13:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126771">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شنیده شدن صدای جنگنده در آسمان اصفهان؛ پرواز متعلق به جنگنده‌های کشور بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/126771" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126770">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اردوغان: حملات اسرائیل به سوریه و لبنان اکنون به تهدیدی برای ترکیه تبدیل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/126770" target="_blank">📅 13:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126769">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b592a4502.mp4?token=Ns45-Xg8ALB-gguKtCDeKufVlOr2rdR516FqjQmoH3GDfVxrvcHr9dXWZJ-gr7J-B5AjesEWoQuDEh7MUo0b5m6F55awfmZLKT23wFnOqP5p-yQlJY-BMQxoiHkPa32OmPr_7IOZ_lnr7nFlaX1i7T22DdQKQlIXgkJWgXj_VLKa5SL8DsfeZWbf_cAm2kRMqOk1H6SXFl0LbrlULc7PTlQmV3zst2QHhYcsdyYfxWNzolxdNWP3KGdDriK7SEZpYFMrDtpjZwsMATwG3IQaQV2kTgrqc3x-U5N5kjz7R7hMpM0oTHqNlL9VZjJECkdPoqn-pw-yisF3r9-lA6C2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b592a4502.mp4?token=Ns45-Xg8ALB-gguKtCDeKufVlOr2rdR516FqjQmoH3GDfVxrvcHr9dXWZJ-gr7J-B5AjesEWoQuDEh7MUo0b5m6F55awfmZLKT23wFnOqP5p-yQlJY-BMQxoiHkPa32OmPr_7IOZ_lnr7nFlaX1i7T22DdQKQlIXgkJWgXj_VLKa5SL8DsfeZWbf_cAm2kRMqOk1H6SXFl0LbrlULc7PTlQmV3zst2QHhYcsdyYfxWNzolxdNWP3KGdDriK7SEZpYFMrDtpjZwsMATwG3IQaQV2kTgrqc3x-U5N5kjz7R7hMpM0oTHqNlL9VZjJECkdPoqn-pw-yisF3r9-lA6C2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی شهرک حومین الفوقا در شهر نبطیه در جنوب لبنان را بمباران کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/126769" target="_blank">📅 13:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126768">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
افزایش آنفلوانزا در کشور؛ کرمانشاه و البرز در وضعیت قرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/126768" target="_blank">📅 13:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126767">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: ما حملات دیشب ایران به کویت، بحرین و اردن را به شدت محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/126767" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نماینده روسیه در آژانس بین‌المللی انرژی اتمی: حملات آمریکا و اسرائیل خسارات جبران‌ناپذیری به برنامه هسته‌ای ایران وارد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/126766" target="_blank">📅 13:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">خواستم بگم صدا و تصویر منم کسی نداره اگه لازم بود منم میتونین رهبر کنین.
سابقه اجرایی در خلوت هم دارم.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/126765" target="_blank">📅 13:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4WndFjmkSZMN6F1-VQHU2WryAvIRxSWFkQSYTeBsh1plmU3MnUW5qYLsrvPgM2Nr5g4HUQwlzNJEOph4-L53pDtsu_m_t4-kDzVKtxa_gZ4AMI8rPjBs7mCA4E9j6scz8W_TO20djdTsYCN-hjXwWfztO4NGzbh0TqIL-wNVf3OoB-XsOdgyAJGc9IQvE6qxVoRK7uBSe0QGRxsdTmzFUZ6heegF8YbbkdM7fDkLNqTVPVrQYlYChXuj7ogr4lwQsYmgOxVd9qsx5RmOluWavVsLVVP7vsjedgkn9nt9Pm_yI_Z5F4paFAUei8BuWeH26v_t27qDVE_Z5_I5KMuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی انگلیس:
یک نفتکش در نزدیکی ساحل عمان از ناحیه موتورخانه هدف قرار گرفته است و ۱ خدمه کشته و ۲ تن مفقود شده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126764" target="_blank">📅 13:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-mODZyCIXEcxY47Dxq-SQ1yVdNtpBG3v0lootUpd9Ob4IKknaCujHXsGduyuzb8Qj8J4M5lLd3qQYZWEPGb9EVH5HuvmTbjQJWCVlDOvxdpyxVGGr4GfPQfLV5zp-OhG50N_r7AStLL6LnB2BCDsBtV6YQAtA7MhCTalVfk3W1NUPoNfWADiaJRdxIbe6KqDQQRpiV0KilpcuKXEIq0Yu1Adc9iqhNyYoQH35mS9jiBijNspmWu230D6KtTejkpBJq2Wu6tf-j7iNV0IzNQdXqrJZ-TeDZd5FxWXexGLoEp_Qnh_CWORXyF7uPuWbgDlKK2FHbyTRFMTQtTs2DtXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل داره به منطقهٔ خومین، لُبنان حملۀ می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/126763" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فارس: منابع از وقوع آتش‌سوزی‌های گسترده در مرکز اربیل و شنیده شدن صدای انفجارهایی در نزدیکی پایگاه آمریکا در اربیل خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126762" target="_blank">📅 13:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126761">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
تایید نشده/ گزارشات اولیه از حمله  آمریکا به بندر سیریک در هرمزگان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126761" target="_blank">📅 13:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126760">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان: شهادت فوز عظیمی است ولی اینکه دشمن بتواند به این راحتی فرماندهان ما را شهید کند به هیچ وجه قابل قبول نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126760" target="_blank">📅 13:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126759">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR4juiw10g2XCktbbOQLVbHfdEkK64JdjYHqq8razj8Ajw6aIObpV9tHP4mpKRwph3BDlj8m-Tlqb5WCLiN4DBABuXjF2eutxW6o5ocwEGx-WH27IuWQPhoYqpjnm8azXQBQZhKjrtyKwJIhX7K2-1BuaZbWGbLIicydS71XtF33TTYC5JF7Y2LyrCpijdfqHDqO6hpxUlLI3yorNEGA1nVUWmyBM33HYLvZgqRggOv9CVuGcRdDfujcNnnanxU_SIs8N8HNpIyKbf7PaJtoFy96-fLv3hDwVIBTF9JWLGtJJ0PGN1FMU3puPLAUX7zWDjL0RUTFqqnfKIgFb1ibqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صابون گلنار ۱۰۰ درصد گرون شد و قیمتش ۲ برابر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126759" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126758">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: ما الان در تحریم هستیم، مسیر ما را بستند؛ امتحان سختی در پیش داریم/ نباید  قصور ما باعث فشار بیشتر بر مردم شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126758" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان: قادر نخواهند بود ایران ما را با تهدید تسلیم کنند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126757" target="_blank">📅 12:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126756">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
تایید نشده/ گزارشات اولیه از حمله  آمریکا به بندر سیریک در هرمزگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126756" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126755">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
روسیه: آماده کمک به حل درگیری آمریکا و ایران هستیم
🔴
واشنگتن و تهران خویشتن‌داری کنند
🔴
حمله به زیرساخت‌های غیر نظامی، کاملاً غیر قابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126755" target="_blank">📅 12:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126754">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
دقایقی پیش منابع محلی از شنیده شدن صدای یک انفجار در محدوده شهرستان قشم خبر داده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126754" target="_blank">📅 12:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126753">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbbdd0458.mp4?token=QxRifY_UBh2lCrttSfr7QAO-jqdwd37gtkPSJ4X9Ur-vxP-GWRevpgss9EGguXi2q8CqqH_-ujWrZG54ZuxI9Zq9tKQ3nfKNDhiAQI9rGdVup58gfBayWDTaIvfUyNXyjgtUvjRyorfWuULAUAohM352apnPL11JpnrBHLZIDO3GUS9lqRQU7YLjMexnO-Edb_vvsB7wxFr0NBzJB46oxv0rl00rdemGrmqTQaV7fKLDOgOJMbDN5ljlxQmlvKS68bTieRh4nXyOpmgdK2dDQodQtIc_O714X5ysbuESVEQYh1ig013y2To7OcYawq9JyvBO6JdG3ecyBKCBXhAYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbbdd0458.mp4?token=QxRifY_UBh2lCrttSfr7QAO-jqdwd37gtkPSJ4X9Ur-vxP-GWRevpgss9EGguXi2q8CqqH_-ujWrZG54ZuxI9Zq9tKQ3nfKNDhiAQI9rGdVup58gfBayWDTaIvfUyNXyjgtUvjRyorfWuULAUAohM352apnPL11JpnrBHLZIDO3GUS9lqRQU7YLjMexnO-Edb_vvsB7wxFr0NBzJB46oxv0rl00rdemGrmqTQaV7fKLDOgOJMbDN5ljlxQmlvKS68bTieRh4nXyOpmgdK2dDQodQtIc_O714X5ysbuESVEQYh1ig013y2To7OcYawq9JyvBO6JdG3ecyBKCBXhAYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: قادر نخواهند بود ایران ما را با تهدید تسلیم کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126753" target="_blank">📅 12:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126752">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
اوکراین :  یه نفت‌کش مربوط به ناوگانِ سایه‌ روسیه رو تو دریای سیاه هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126752" target="_blank">📅 12:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126748">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PI6cLFlHIkzO5HITcIzgCMLhPdx7wBidmawwaC27mTtUAvMD5aUoO-GA43wOQNEW6pbjfa9pcLBmtlBNCIguIsgG1tnUCcGq2mHUqIUZIerYcqDVfFfbz8yryG_hVD-EnfvC5yeSUY4Dt8QISZbWLdNHVM2X93P4lcPxcPQruoVl8oRADFbgSa9yzcaErYJGYX2VvKPrNt8Ge2mqZozVOBMVG8aR93oQc7iVCYTMS-p9Uv4G9-lHN8_qDAX3Fq0PfozKJVdVEwwhgyDuThu2B-b9NKDLTHgU7S76TwcSnRgJtPnem0BeqDqa9oxgzcm9hxNw6q6m-YMSv9f2fT8NkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfPASS7b2YnmctTp4oSh7Bjr7kzIkkk7QmIqzRldPXu-rQThSEd5O2gZ2hiAohW2we208mKYEvgk6_Hyj_046tfkfx7UoZTtjnXRdX1jw4prGhiKVcevEp1DZeTQFfDT8gONI2Ty_h_TRzpSxlzX4Q0AJYCGkl7sScj4YGdJvX0zs4Bhe_MFwg3IPwwNmqHX2l6hL1eHlYKLgPz5J3BFY6BjKuNdOa-_RJVorVwpWjT9mfWLAk9CzcZmGT2rhzVtGbK8Tvh42dktCcayNoeMA08YTIv8gpmZY_09cFEnlWCQgENA5c7Kp8C7xS41DZ-deAKpcPZ-__aer8akdfb8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvuzyEPLQl4wJKZHDDOcnsHc4wVQFI9KiVns2HYJtohHYYgb-m3WUhdGs2mrYawoPVnPHVwybqWbj7-6R7rOOCIYWOdZo7kkTgntbIhVjbRdmfUZ6Z8a185p06L0SZ8ubMbyK8WN9rUhFf7sG6Pptvcg2T_y4VDgFj4ziFMFy5qhqHWf7gqSb-CW8_PQJQ7bd0f35bd7krZAx9tzXmClh0RrCnlFKR7siA0mpPdIhsrKewsB8cAZbRLpYa1Q7FMtzKvXpCY_wNyKfld282Y22yeQ99nuNx66zSFzb7pGrTfLVmba4PCN7hRA6L_C857oyRZnPiF81fnVSW4Caz88Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUxLjRgnT9rEVdFDnQO1DBJ1YLENhl3mMiRmqG0IQvEBHg7bIJ0xGZY6ZcshGf9LHR6jjif75DkGovRQERUz1uTXTKMsNcaPQcwuz5GVh3XJNIvl8zd2fDZeFnTeherVFmVs9nBwqlw_TDx3tjLSDc-m8K4R8oU2_GhxN-fMmhRs0CUu7xBHu39V2_1SI7tbWtA7fyzOATGXPolHoXU1WYWD0_GoOvok0YuEQ2nSMZq5IF5zVuAE-GRuOrSFgE17fjIcnkHf58xEwJnJX6AQd_ztyO-wK2zHeV3T0aj0-HVqj9fXjmWmJxB1rr0UwivDqvHFheZtnz0RvvUQXOQ62g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملۀ به منطقهٔ طیر دِبا تو جنوب لُبنان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126748" target="_blank">📅 12:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126747">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ایال هولاتا، رئیس پیشین شورای امنیت داخلی اسرائیل: وضعیت امروز ما بهتر از یک هفته قبل نیست، و تمایل ترامپ برای ورود به دورهای بیشتری از رویارویی اکنون کمتر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126747" target="_blank">📅 12:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126746">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrKEfSP-U04wUH0S8azO4_syPyr4zsmtZAPyj17cOrUJsws1KY8dAHl14WlUNOB2P-C9Uxzr8GXF4JChBKeHvJevJRwj7IuDMkaNPERgoHfI-YE95ATpEjSHtrq8jDIWMQr2dCFyORK2daT2c_INX4DrZJQ1vwKk5y1PWhd-giue_vG49R8M0AgeEDKcKFbDPOxcQNwm04MlPhGYpFWoBQCefuNDrsGIU7PHJ3GV5mCp1LzsS0hhtvsYbSkmhkeRMDNtUpYFIDPAUHxdEbG_G_j0f5YCQgN0Mdhnij6nR88g-LdW5vnLG5C5hzsk24AIQY71r6oktDT_VOpG6saiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از کشف تجهیزات پشتیبان هدایت جنگنده‌های اسرائیلی در لواسان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126746" target="_blank">📅 12:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126745">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سخنگوی دولت: لایحه منع خشونت علیه زنان در مسیر استرداد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126745" target="_blank">📅 12:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126744">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cl3Rb1pgayhlOOnPJAufjQzgUFGA_BzQQqvYIz6kqo3mWkHwsEMFEQ869EGORjVD1TgUzvPHgnbNCJYWS2eynPq8KW5SbP-ADKAn0j0frj6SDHqw4D_4zT7z-t4Mmw7LGn72tz2Z-w9kNQKCezIHMIRLsT8xYS5qlYZ4Ad-flt-jIp4q63ouLFrOZ56_KZsRI3nHfiRp-CjPkWu9OYZ5esQ8IOStbKuTvT6I9m2LISR-2zeD4Rsz7SqMXKz66epd85rBeklEG6aRUoWwAlLNfRYPKknDRv8tx3t1EW0rb9Bd03qisirG96L-2bv8hNtt3fPZBJYzu7lsIktT6qjskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان کشورهای منطقه بعد از حملات بامدادی ایران و امریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/126744" target="_blank">📅 12:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126743">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:
🔴
دیپلماسی و میدان دو امر جدا از هم نیستند؛ این دو در کنار یکدیگر، ابزاری برای صیانت از منافع و امنیت ملی ایران هستند.
🔴
در هر کجا که لازم باشد، نیروهای مسلح ما با اقتدار به دشمن پاسخ می‌دهند.
🔴
اتفاقی که دیشب رخ داد نشان داد که نیروهای مسلح شجاع ایران در دفاع از کشور درنگ نمی‌کنند.
🔴
در حوزه دیپلماسی نیز ارکان حاکمیت کاملا هماهنگ هستند و در هر کجا که لازم باشد، از ابزار دیپلماسی و هر جا که اقتضا کند، از نیروی نظامی برای دفاع از کشور استفاده خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126743" target="_blank">📅 12:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126742">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
شورای امنیت روسیه در بیانیه‌ای که توسط خبرگزاری «تاس» منتشر شد، هشدار داد آمریکا و اسرائیل از پوشش دیپلماسی و مذاکرات صلح برای آماده‌سازی یک عملیات زمینی گسترده علیه ایران استفاده می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126742" target="_blank">📅 12:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126741">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3507988ffb.mp4?token=FD_rtjTb7A3ZL7wdBs1JJyl-41nUCi2Qt60d3xTNPM5DAMIYDCzUzrvZVsqEmaY2Ua_MHYU8FCagM2PrjCYnxeFfsAYups4A5Oim2lZ1NlKcYfEVSfbvEfNodsevcAVHNh_3y6Z4o9s4eh7MEH2Z9CxeVogUw3KcGMgrwHxmq4ywnFCDKNx63zjTtBegolG13vzM8UJSZfZcHvfBwLMBt3kgOw1j8Swtx2SM3cva1SDcu8kKTW45RLy1Vp4lRUjwjd2Oww4DAst_9zqzjf5CgPpkkwMZyfrbvoJmjG6YcOtdku4nPr04aQBDenHyguF1V2st9zF9O_FR8T7ZCjxxTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3507988ffb.mp4?token=FD_rtjTb7A3ZL7wdBs1JJyl-41nUCi2Qt60d3xTNPM5DAMIYDCzUzrvZVsqEmaY2Ua_MHYU8FCagM2PrjCYnxeFfsAYups4A5Oim2lZ1NlKcYfEVSfbvEfNodsevcAVHNh_3y6Z4o9s4eh7MEH2Z9CxeVogUw3KcGMgrwHxmq4ywnFCDKNx63zjTtBegolG13vzM8UJSZfZcHvfBwLMBt3kgOw1j8Swtx2SM3cva1SDcu8kKTW45RLy1Vp4lRUjwjd2Oww4DAst_9zqzjf5CgPpkkwMZyfrbvoJmjG6YcOtdku4nPr04aQBDenHyguF1V2st9zF9O_FR8T7ZCjxxTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه
،
بقایی
:
با توجه به اتفاقات دیشب، باید برای ادامه مذاکرات بررسی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126741" target="_blank">📅 12:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126740">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
چندسال قبل ولایتی یه توئیت زد که مردم ما باید از یمنی‌ها یاد بگیرن که با پای‌برهنه و خوردن نون خشک دارن مقاومت میکنن، اون موقع خیلیا گفتن چی میگی بابا، اما انگار داریم با سرعت به اون نزدیک میشیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126740" target="_blank">📅 12:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzHhichJqull0BC6H83-0Ww42hM-P8B6tuKRGCBswgLG3lM6lwoF_sZfBddCsk11drShkv_JjY4bRgg8iHQGtw7zTsAkg88csGC6KQd13Nl50OBJNMHC3kIAXiBuhrH9-5v1FKO7xlZyQo490AkcRCIb8dpNM0xacrP93aTNi2blzQp8yHJooexU0kfG19aW6XCkisMD1J_-XguxSIuGxbfU0L2C26iIf00ceyzIccE2Tp48l9pU5tS0h7mQqRoX0XlVl2CDn2ov8jez3S9GUF17a_npiKVPTlRAGtA-EQ7aw9Q-JY3rnTchW7PW5Ao7TYbbj9mQC3_--54avAtgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hovAHmEWnRJoXq-312pW41S6qU0_RurFjZVkTheZrTyWz_tLb9yY81dSMst_sw5qoxJ5qKg2VEQE_KVP2lqDYdwkrOj6RWL-niVYe4sMuitDpsdXMMPAp-N-poeeflZNhXtiW0wIzteuAX4YzRh0W7GgoPx9geRqb_oMS2Id6BHewjMQNEGmolf7ZxxHKhfiTBuZ_I6zLftk28zROvxrXfbCp2ilvfhQGUQMAyB2huCQTCobLdOoZUvoo3inER7Ypolq_NkXHjFNjOaMiXTZEQ9VADIJZcEp4GAQxqUmNR_aRn0pzi82xNGvR12T1J-YrrVV-HqCsQe2EMOjZn9IfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9aO7Ab8VKyxpd4wjr5gOYGQXd_JJ40u3FJh0IaUE1alB7Jm6v9bwX70yy_hbuYvAdMC0LCpro8DwH_fbGCkrOMnho1MRASDVB8FnX8fFfj5fpxlShlaBRcI1HkhUaHLL6VlDhZ6Qpt_ygckYACzJdAN4-Snz6XtFPSisQiLpWKl7te6OQVjTka_8PX_Ye5-eZU7QIB7VqasNaTYukn9tIrrVoZv-l8YfY_QFLkBp3MZ9W76dXqbJokbIB_uBiXywsU-6DArxOQf-V-Km6M2omAd0z1tDE_HgntW8NkniE2UrTgDxGaiqzEfOpCGvvmR9Xygo2qs_Wfzzaii22Q1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8TQtwcb1FXK6V7YGcjm9nPoQ-C-GoftvEX9DmjzkArHLBBzh7D8wuD50jySDPli7745q3vma24PRYxDNIN4IPMu-kp4IvD5lR1AtsXjtb63vZtLcyYpvcU3aueDeO62xeL0kZt5aOZqHSrTQ8J1_H_HWCbTuU2mp18p5mK0WFUzqFr1p9MeUnJSOWgbnvdoaAtzsUSGu3edOIz_tdkp1FgdD1zZmoza7DV7RUjZ-vNjzBClKNI6G8kJpNzZLRxlLv9jLuOZIi4ItLQ7ptIib7BETtMv9Aeg5JVKjRN8NGIMUxUlpE8tW0N1HNcNzhEeRT9WBGnJ6UCr7ETCmVEnKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwGv76vJz1UAjif8ShgcRbzNI3jt61xSsov4-3oGhd0fdet-HCuW8tmOqqDzxkG89G-AH4v_cukQjuh-BlFAXQwWFLU_Fc1qPpRwgFqo3fu5CW1lhd2XazmWEEYUboWeZBQHnmIyp88jaTxtsyVzb7T-Taw1hWuyHzZ9DtyoAdcKeBHggcB1iC8QLJTYXR-nInyM8yiz3txhqeofk04pcvT0yFhrX3xTGLnR_W6B4joHXBafF5A_bGF897KnytHJP8d4CJEulPKngjw67LEdfiZ9fVDtudKzZr3jwcgNHF4KeZCRUhvHr8rcJS9WgsSQkI0KhhNDWz7aJaB84L_7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khw6Smqc0D6cWxaaBDTQDCE6bOB64cAQz-P7foe0VWWs9y1PqNE3nbYb7l0dxl7QjyYs1DS0f7Ybzr2QktKVkEp6rj1X_nJYp01WdNogUZizhAYqqfmkiuWSXBYpd3IbW7GSv7E3QXgqdxX4ZCvKaCnOblZbaRWga67GTJGPG9A2UjpjyVR_C_OvQXRXtEFdbTqAgH6Ee07E69x6qHbkrSkKTd3HhKEWQ_D7arBiu-EmDqU9q7w-NOVxCJPlqaYiar9uOFOvZbmmMyQijJW9583gM3V_TBjh3d1zrgssO3Nn4lBx2VkXhFdJSLLZxay7jBTfIJl4uCLwsYPU0Lba0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ASbpzT9bl1K-iD_15RV3uPz-mD-2MJKA4ON3PnWZ-ZtM54d7r0NLvLqB5ER7b17J65yJ29dP8YID4nBNLVZyhRy6m0xStOgyMnIi953qv17GBSyLej_W6vlVtC8PSJWT6tnOkbU5lW1uYRuveeRj5_U97_BwKfasf0BimjQ1ORtpLnbtXKk3lJ98ayqLTo681Fia8pJTfpVk-AdMyqS1eJFXFMLpkl2PCaZDlxKVDuVYl9bf3E5rQeK56OJ8wl2H_8c8etYSlWf9VwIR5Ub08VpbuLmmLNR12AEx3kY-0Tnl31t7PK22QyuDxsmn60Bv0IP6vRe0x6JkVst5eFJWVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در حملات هوایی دیشب پاکستان به افغانستان، ۱۱ کودک کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126733" target="_blank">📅 11:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMQfrH_ZYtqpiM-eHuCjTKvpPoPBO4Av8iMbWFoEAFTNc110LbC9Y8KSw77NyBJ1USnBbMMBA65niQjVUP41HaBcvVGPxFVPLxn0BBf5Jg5bmCEvwV-m7wDby7GUVnvf5qes_G2j4zvXrR7K3nwNg3zpxRdBz0gh9wrAhd5YMChMmm9-Sa5rseOiyQ_Iw9HdjZCplGILG5b3zmZUf3w4xcGuRUPofCsQCnTW8hJNfGuVOAeEnimQgKq6R5JRqoQE7RmdIuV3H1-GDEMhtZFZIJwMS0gJ8pQRBFTdUVfC9gxamn89uLJTP02CDscLM5Oxcz_bzLSq39OcpXtnzm4O7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به ۹۱ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126732" target="_blank">📅 11:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCFDbOB94h49x1FVvQZaJg4pS1K10sLIxv-ut396W_KSPRaYGGe8tb4y-O15ZUtNi5Rtog3q0E9TEaapooTiWSa7MB-A6r4WmJzzaw90_zJKXKYhAfOjbu2CEMZgONdoqMrYr2jqMdSDM8TNRvnt3YIuvfosL_1vcT-F_Ldw3ehpifSotyN9qT8WqaCiqljZ2t_JT6vQ9XpKqolGc2_oTpRxZWWn_ZK6BCnk8xoYQqyjgKbKOfOZATdvQhvj9cewMg1oXAapy0C1fbgqp47Uk5d9txH-q63ecyHj-Vcjc00cP1C6JDXai9qmS-s9TlE4seYyH1M7Q7YbQhlpL3g-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت خاورمیانه واقعا عجیبه
‼️
🔴
افغانستان و پاکستان که دیشب باهم جنگ داشتن، امروز بازی دوستانه دارن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126731" target="_blank">📅 11:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124deefd6f.mp4?token=d9x6bN6tyO8aMBOUg6TrbfCQjr_vq2c3cgr8TEElrtGryaVtUWH6dIKU9tSQbLwO-Gade3CeCclCt-nf65dVEQXE8XnfD8fgtGGEq496eXN0PnornZYPhJVGG1iNCooVPElZEg2aXWSFGPUorzJl-cq5T-gRpr_SwQX5QKTv3ATPwRhwVs8U57m08KMKtpJ1HG2ajEJ-aCjQKA0e_LQuEFNttud_l8SEdmGgpjC-9ul1i5aiKQAzL2YgSnZOitwqcCa1VPjebigvycStJn1PlQt6wobUw_XtOXuUkHbWJR890HZcW-Ak-Eyc8-6oCjlbg4t0jyPbsYj9s9WI4XgjHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124deefd6f.mp4?token=d9x6bN6tyO8aMBOUg6TrbfCQjr_vq2c3cgr8TEElrtGryaVtUWH6dIKU9tSQbLwO-Gade3CeCclCt-nf65dVEQXE8XnfD8fgtGGEq496eXN0PnornZYPhJVGG1iNCooVPElZEg2aXWSFGPUorzJl-cq5T-gRpr_SwQX5QKTv3ATPwRhwVs8U57m08KMKtpJ1HG2ajEJ-aCjQKA0e_LQuEFNttud_l8SEdmGgpjC-9ul1i5aiKQAzL2YgSnZOitwqcCa1VPjebigvycStJn1PlQt6wobUw_XtOXuUkHbWJR890HZcW-Ak-Eyc8-6oCjlbg4t0jyPbsYj9s9WI4XgjHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر لحظه انهدام پهپاد MQ9 آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126730" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkHII2LPmTecX46aXcbTbepgBfHUonYqoaH_gq7F5tSdIWDdSE6g7ugvWCK3Jy8HfICiRNGUGdi-z4Perw1c6TedU3SoKUzpcm2t_UQixxpXYMH4Yvo6u_s3MD8w2RmUs3c07Uo-g5_8Slcf9KxPT-lzR6Tv-bmqGnJEgaExy9xvyPLy1xxZzzaF8PR_rVyo0tu3xhVFOTjt233wLRLBsiELaCTuTEphrm2UIbgMfEdKVGNUAYnvysI2BV4IW9XcfNPRNIrOWHtibRM9FUsdC__7phN_hLkgS_6AVqsJMrb6pMfRFSTex77lg_Zx8jN2ZTGPfwwWtr4XnV-dg3O1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هنوز نگران تموم شدن حجمت هستی
😱
یا استرس ضریب و تایمشو داری؟؟
🥸
کافیه اشتراک TVPN رو تهیه کنی
نامحدود واقعی با ساب
🔥
که دیگه نه نگران حجم باشی نه تایم
🎈
اشتراک نامحدود فقط 290t
🎁
😀
حجمی از گیگی 2t
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126729" target="_blank">📅 11:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d417fd03d8.mp4?token=ISObWWjWw9sXFNTV4e_d_O1v4nGCacrBqN9h_7W5WMk4Zg2obSajbQ9-1K-PZhiZdNdQHTqH0h5zw62fhNL0FRhY-iFQXhYTOR2Oo5UlKphUDtHtlFN5KglZdbv_irkhEqcjaKwd0fYLhFX2aZpT2OZ2r1ZCx_7AbBV-ZbXzjSfBCXxopJjXAgF5wOdGs0TWzDrPCnqITpTg7f31fgCpMBmXSjdLWpwGKBjV03Jd1zLlvovcHcHISfqh9V03fVuEBn3yC-ruvPyyaAPcDzpV0uGsBIr0ebWfi_Wjebrj6kxAlAWYvioYFsD1RTVDtBVsppMIHqeuj8kr-JSQO2xgqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d417fd03d8.mp4?token=ISObWWjWw9sXFNTV4e_d_O1v4nGCacrBqN9h_7W5WMk4Zg2obSajbQ9-1K-PZhiZdNdQHTqH0h5zw62fhNL0FRhY-iFQXhYTOR2Oo5UlKphUDtHtlFN5KglZdbv_irkhEqcjaKwd0fYLhFX2aZpT2OZ2r1ZCx_7AbBV-ZbXzjSfBCXxopJjXAgF5wOdGs0TWzDrPCnqITpTg7f31fgCpMBmXSjdLWpwGKBjV03Jd1zLlvovcHcHISfqh9V03fVuEBn3yC-ruvPyyaAPcDzpV0uGsBIr0ebWfi_Wjebrj6kxAlAWYvioYFsD1RTVDtBVsppMIHqeuj8kr-JSQO2xgqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئو جدید
:
- صبح حداقل ۱۱ موشک سوخت جامد دوربرد به سمت اهدافی تو خاورمیانه شلیک شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126728" target="_blank">📅 11:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
دقایقی پیش منابع محلی از شنیده شدن صدای یک انفجار در محدوده شهرستان قشم خبر داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126727" target="_blank">📅 11:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEmzHfKLsFAWv7a6HQr2YGnbS2xsSZCVV_Mi5Ycl14s88-aa-YasC5pML56hyNfudxvmpytz2T2NwWikO7rakGaIZsXU3JgLPljf0O1B_850G2dkMRMosMi9OLINeweYRbgJeilEAB2Hh3wVRWkETEIu8ycfHP8OQR9D0nLmEbGHt3EiHtj0l8uB2150usulKzj1H06xea1hE6Vw_TT09lyqenEuxAwduKUpJWwSfWvoLK4oh-9BLmQnniDgPEnEt1m7HqQRoZrfYy6vhuoj2MnERqlR_f7Ez8rdC9rCTS_m4YCF62oZZ9QdXUuNr2J0wd5L7omI36VWKZ7KoMm2dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روستای بیت یاحون در جبهه بنت جبیل، قبل و بعد از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126726" target="_blank">📅 11:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزارت دفاع کویت نیز تایید کرد که کویت هدف حمله هوایی ایران قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126725" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
چین: از همه طرف‌ها می‌خواهیم که به تشدید تنش‌ها در خاورمیانه پایان دهند.
🔴
ما نسبت به تحولات جنگ در خاورمیانه نگران هستیم و خواستار توقف تشدید تنش‌ها هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126724" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erDi7Dy8vqFICSkoXcu9msX17Fdj1xpCklFwb9duxWZl1GGk82zsb3GFaWH7rqHwIe78OOEpD7VKM60TpP9qdUIWTBN9iPVHNxQyhsaUnxHYBbzrcmBGGWkO9Bb7GhEX4ljJM8LWSGZSPTN4MlNSOewG4lqTSt4ku4L9YTMwEv47mAXAV-Xj-ASJx5xV2RfHxNbPLRG1GhkUvHcG3XummdGDqNxJTEHfIgl9__NJQZQTkU4WaIAXnEAvr7CqQOXkBzEq7MzkYLwnMGL8Wc1D0cmcvZGcJmvzry_OwltRtWpr7vUuAzUatoozs_Fj0E3UqUFNV_BOaYc5SOWNDQKSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۱.۳۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126723" target="_blank">📅 11:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت امنیت داخلی آمریکا: بازیکنان تیم ملی ایران مجاز خواهند بود یک روز قبل از هر بازی وارد خاک آمریکا شوند و در هتل‌های تعیین‌شده اقامت کنند.
🔴
این تسهیلات به درخواست ترامپ صورت گرفته است و دیدار ایران با نیوزیلند، اولین فرصت برای اجرای این برنامه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126722" target="_blank">📅 11:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
سفیر پیشین آمریکا در اسرائیل: وقتی به آنچه در خاورمیانه می‌گذرد نگاه می‌کنم، می‌بینم که اوضاع همچنان آشفته است.
🔴
اختلاف نظر بزرگی میان اسرائیل و آمریکا وجود دارد و کاملا روشن است که دونالد ترامپ مدت‌هاست آماده پایان دادن به جنگ و رسیدن به نوعی توافق با ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126721" target="_blank">📅 11:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
پولیتیکو به نقل از ترامپ : با وجود حملات تلافی‌جویانه بر سر سرنگونی هلیکوپتر، توافق با ایران «همچنان نزدیک است»
🔴
ترامپ با وجود حملات تلافی‌جویانه ارتش ایالات متحده در واکنش به سرنگونی هلیکوپتر نظامی در دریای عمان همچنان مدعی است که دستیابی به توافق صلح با ایران در دسترس است.
🔴
مقام‌های کاخ سفید با تفکیک مسیر نظامی از مسیر دیپلماتیک این درگیری‌ها را صرفاً دست‌اندازی در مسیر مذاکرات می‌دانند و معتقدند همزمان با پاسخ متناسب نظامی می‌توان به گفتگوها برای بازگشایی تنگه هرمز ادامه داد.
🔴
این خوش‌بینی رئیس‌جمهور آمریکا در حالی مطرح می‌شود که تهران با لحنی تهاجمی از آمادگی برای تداوم درگیری‌ها خبر داده است اما تأکید مستمر ترامپ بر نزدیک بودن یک توافق قدرتمند نشان می‌دهد که دولت او همچنان اولویت خود را بر مدیریت این تقابل و رسیدن به نقطه تفاهم در روزهای پیش رو متمرکز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126720" target="_blank">📅 11:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
منبع آگاه نظامی: ایران با استفاده از موشک‌های دوربرد سوخت جامد خیبرشکن، آشیانۀ جنگنده‌های اف۳۵ آمریکا در اردن را هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126719" target="_blank">📅 11:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEFgfh3I-vcIp1cP-lxVs5GBhRGmibkMnF5cYNVTqwO9yMeN2ZtpWj3IypZ1LEQbo6uIH4cetieNzUCYV-9fxHz43_1g77jRk2QBlDzpgoNsutIgyXgdD-eqWoiSKLaUsb-mY-A_9-n46FNdk6pGQkYIkoqA5MT-fi2VuYeuvZ0HWyGd4A72mlv4uWBktrvHUBLE8lcDaNZ3xSOUKOVVdrBgtH0YZ2RdtsRlSo3nxm_TrO0VVkkg7wO1q_OA14hP5YXfpVxtzk8_GYd64Hh_VEmn-J_keCoEKHhd9LAE1lcKYFOrRZ45pqG5KIyunIUzq0z0VZR_ou-_Ya9iTHlcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0B0ZobvEo8DJ_oCyCdRMU7mllOssN9Qvq_cJh5xrDR2zk74Vb6KNfDoMOSQXmIktu9fmfxObZLvvUz_Onr78sbUEvljYM0XpwHFiIyLuuHjjx8YD0azOjBBn9zige4EIUvoD6gNySkl4QVpc1VmbNB0kGXB4VSTGk85zSv3RnDgRlMDKzT9WwcFu8QkEOSRIkwEx7x6JAmoPOlYplgozNd8aBPZfC8rAMWkXJzvXUScJz2P9u87prLS8ATd67rsn7lgukpSzLFNvO-QEq8XO7lPNFLxc_zYEjJKli15yU1AORSqdrZZ0q3vNlOFbed7fdugi_7eHNFJBLEcV2LnFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
لیندزی گراهام دوباره به عنوان سناتور حزب جمهوری‌خواه در کارولینای جنوبی با حدود ۶۰٪ آراء انتخاب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126717" target="_blank">📅 10:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126716" target="_blank">📅 10:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMIUpcvcrPJMBDaRuTdhx0BUA9V3GeKj0t4jwcVOTq-ZHV8V00edwOy3_iAeaw-JpwQSd8uZ-LSp7TJx_Ry5Nj44km0ndtUE42mjenpdyqJtPm-3baytFaeEoyOkHPJQLIVIHHMyu4wvFHwu2ZdoxaqJF-otV6RxWhu0zo0lfhiV_uI7C2mGTyys3nmYel7vTsk9pWJOouA-uNNEZ3l7JRmpnfJbNPVmCcAw1ItSDyL2y2dhNGk4p_wTNWg3-vhzJSqDP2fwgtbEgZ7S12xxz0NbgGUusNhPHtAwMbjsvABvBTrRMLaC8XbX3X_THntWy_0WPGgGwJwhf4agavirGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل و شاباک رئیس زیرساخت انتقالات مالی در سازمان حماس و معاون او را در نوار غزه از بین بردند.
🔴
ارتش اسرائیل و شاباک در شمال نوار غزه، خضر جمازی، رئیس زیرساخت انتقالات مالی و معاون او محمد خرازین را که به عنوان انتقال‌دهندگان اصلی پول سازمان حماس در نوار غزه فعالیت می‌کردند، از بین بردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126715" target="_blank">📅 10:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9ZWyDEoFB8-SY2HzL-hkDuMVorqWbMynOAoCIn-MfEURuRF--tHw4XlNgKzKQis4S6MW27SFX9ghyXs7-ienBvWodPIdpGi1Bp1yjp1cMvG9xOux-ScBQ_pR4ZJBJ4bdoaYH5bTetLZNe0QvxJFXaqZCJgaFKEiKGbV_rGxhUH8jLfw3sGO8usn_W0QN9_mC3OtvsQU5l7Ow5lpEAWbnPLgYu6zFrc65GMp6QkUXzGdw17UhHM4IoU-H1Ay5-WsDVBjW0WdVG_yotwoktK_llu9lYVQRERxvvTtRiGhKKyNwTZUno_o9GCU1UKyIpm65qOHxbc60lDp_P5MLD26Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاهش قیمت جهانی اونس طلا در ساعات گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126714" target="_blank">📅 10:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126710">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIGuoGirqsyMz_r4ecCxroA72vgx9vace8z5ncfDwzzgUD6bHUq96V26Rv0-ZrKStapDg7T-41ZpIxwTSO4ylecMQ8JHrfs8xddz-dv7R68TrC6yy_4Swt-lT-A-pj-m7uzOWpw5KLtaON0h3lBeLJoc4T3m1ihqQvex5zjTZzZxQXwY2blR5Huq6KUJMNu7seHo2kRpl92I6S-1OOpl5THwJ3dMKT-t_BfBS8d5nZw8Ebu0krQTA0kDv8Vq9Gd60XBqxPutNz8epPHVKdG19EjK4v18hzrXbEVrbeuKP1LSUJImSd5lOiacTjdR9OmHr9TxwvAy-_Jjvi1WQRKGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZpWeGKN5G6pmyJk_YA42BOjJjnY7J6oUpE90j7mb48nqITkRaXPCdxTKdgIYZlV38P-wQYCpmNivkeMMNuveKQSkbFvaAm4zKA6Mb0LT6GRJbDWBnOjh40BKPew9DMw_U_y3R2385_PfgZ4xxxFJtDLyQ5EmtCE4IvaR3qf3lvs2V8-Y_z34QyWl-ZpqRPOzNVUInrOQWIqdf6lBWTPXYMKTWDZVoKT8LTFUKI7tq5l8LpOZis8Lmn0x3V4n8My6CsGMaDmMBhe5Wzd721iM52seWNy4PD9Nx1H231Aye7aHx_oOWHs7EAs175CkVrQ_Vbbkwd4YrD6rNE5TKclDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgPaGrsy5yi3gJDGjjgBhbYY8xf3YZk-aYqyQR3V2VBS3opsEKLLRk0QuC-9quACx7DUOqFEwHQMj0ySCseqtm6Pon7dl0Y1CEa2fr25Nvt23NmktRPbWpThVujtiL-4GmyMrxu9x-vAudajXufHnpfoVG4rpLuSfw2w85DIA_R7xTq-AcGnLqrpkX5lNOZYdT3gw11feUkHdnVDuPvPLUMLDFxpNCqJ1DVS4vNVrusGthXX4HTMFdQPSUscD_7_UY3BzZ3pm5jV4Zby3MV5iZd4I-d47EYqqiDrKJAT-s2Oj4T-je0oCl1tgIT6vOGWEPybRsCM9KLgkMs9PG7Qeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7A2PBP6iT0AdPndopgPF6hbYjshN9hsIy1MH9ugTBUIu-ft6Sh_zbSjT60IOA27w_iDGw7v58ATZAHV7ws7FtQwR8T5G3L8nD8c9yUZW40haG3tg8FKH3I0wEoxg6TBiT2X-YSDLYVi7DAm66BPmAWaOWlZnDOPLIDsCUuW3srimGSoPUhRnIHTV1NcHBIa6nQDzdhnZ8sLQfkVogulTIhEM4x_INrTQj1hmX-bgeQEA_e2F-wefMuIzSbNwqnsnNaZ3zrQm92jE1IeFj4PMOOdZMPqDSOj0FwlX_BGFrmhDJIy_kdsuYMiTuf8_4eg1RvNvV8PXkrlX4ORHctv7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات امروز صبح اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126710" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126709">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ارتش اسرائیل: هشدار فوری به ساکنان روستای انصاریه در جنوب لبنان برای تخلیه و رفتن به شمال رودخانه زهرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126709" target="_blank">📅 10:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126708">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی گزارش داد که ایران دست‌کم ۴ موشک بالستیک و چند پهپاد به سمت پایگاه‌های آمریکا در منطقه شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126708" target="_blank">📅 10:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126707">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e7c0550f.mp4?token=oAVFUSBMyGN-eNO9f__tjhAaGwiMdaHREApF5H6gQrKSjCJvEbXzOf5JvSoEodlpLj6kNTl6bNwAAYetfqU7n7G7TszrJuUqihAsjZPFG3eTobfHJBVx8fxQqY2BpOD3yFg1OjG-D6TggeAUzDhRxDyelayXK3YZuumO6RkFeVi5ON12150trQ8q76y7Hkbgyc-8dY5YBx_B4B-_3VmiWNeyhrEpyZoV7BArfIWbzbeDbKoTVAABctG3eI6DLW108NmZjfYyVb-kP3WN0FcNEI-r1JIAHKHnd7o8dee128fhLW06IIUjbcqIcsPWeP9VeE0xKAn98P2gv2Apo6d7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e7c0550f.mp4?token=oAVFUSBMyGN-eNO9f__tjhAaGwiMdaHREApF5H6gQrKSjCJvEbXzOf5JvSoEodlpLj6kNTl6bNwAAYetfqU7n7G7TszrJuUqihAsjZPFG3eTobfHJBVx8fxQqY2BpOD3yFg1OjG-D6TggeAUzDhRxDyelayXK3YZuumO6RkFeVi5ON12150trQ8q76y7Hkbgyc-8dY5YBx_B4B-_3VmiWNeyhrEpyZoV7BArfIWbzbeDbKoTVAABctG3eI6DLW108NmZjfYyVb-kP3WN0FcNEI-r1JIAHKHnd7o8dee128fhLW06IIUjbcqIcsPWeP9VeE0xKAn98P2gv2Apo6d7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله  آمریکا به مخازن آب آشامیدنی بخش بمانی شهرستان سیریک هرمزگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126707" target="_blank">📅 10:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126706">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت‌و‌گو با شبکه سی ان ان مدعی شد: حملات آمریکا با هدف ارسال یک پیام هشدار به ایران انجام شده است. معتقدیم حملات آمریکا روند مذاکرات برای پایان دادن به جنگ با ایران را مختل نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/126706" target="_blank">📅 10:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126705">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا:یک کشتی تجاری گزارش داده که در جنوب غربی بندر بلحاف یمن، یک قایق کوچک حامل ۶ فرد مسلح به آن نزدیک شده است.
🔴
به گفته این سازمان، بین قایق مسلح و تیم حفاظت مسلح کشتی تبادل تیراندازی رخ داده و در نهایت قایق از محل دور شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/126705" target="_blank">📅 09:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126704">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از پلیس آفریقای جنوبی گزارش داد که در تیراندازی در ژوهانسبورگ، دست کم ۱۲ نفر کشته و ۹ نفر زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/126704" target="_blank">📅 09:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126703">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade34d5585.mp4?token=AZn8Zh7Tsme5nbD1tKVxSqopGZyNH_D97iWCjMpg0DlFXwuzl2ds2oK6CAwTEKDlU-93rBwjSbcPu7s8L40yk_6HK47RRtttFGkcrgB7WU2RCXWzcwVZ8EmUmLSNb_nlKAP0rphWnjvw-Dpbc2j--_ZKcBzE70O1tO8EOdejUTAgMsumcSqZdL3vAyYn7eLyInPEYqAR3R_3wDEttYkw7MWYEPYYQqVgUQWH5pfKu0OaaRTY7O8rwJAiPbTFZt68wg6Ne7YUKNn8tAIlcD3xFB3OsOc-z8t5GjNOHiNoKoqZm45qBet5gQfaSYdMCHqX8lqrjwzOfXmnPWBirk2wHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade34d5585.mp4?token=AZn8Zh7Tsme5nbD1tKVxSqopGZyNH_D97iWCjMpg0DlFXwuzl2ds2oK6CAwTEKDlU-93rBwjSbcPu7s8L40yk_6HK47RRtttFGkcrgB7WU2RCXWzcwVZ8EmUmLSNb_nlKAP0rphWnjvw-Dpbc2j--_ZKcBzE70O1tO8EOdejUTAgMsumcSqZdL3vAyYn7eLyInPEYqAR3R_3wDEttYkw7MWYEPYYQqVgUQWH5pfKu0OaaRTY7O8rwJAiPbTFZt68wg6Ne7YUKNn8tAIlcD3xFB3OsOc-z8t5GjNOHiNoKoqZm45qBet5gQfaSYdMCHqX8lqrjwzOfXmnPWBirk2wHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی عجیبی از یک انفجار اتمی در بندرعباس که ساعتی قبل در پخش زنده شبکه خبر منتشر شد!
🔴
در حالی که خبر درباره سازمان توسعه تجارت ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/126703" target="_blank">📅 09:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126702">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7YX7ThFoqaDoX1fjNseEUBvog4K68kvBudnUywaLA0y1-bcw_pLk5u06wG41yJ2q8wOYADO_ig3N-VMLylBuTh9ZkQZswTee90twf1PuhYeW1qL9_YmqGuLr0Hu52n7QMZE609NS7paJp8bGFAAxRG-cKTkHsGC_vKwr4uoDOHQnGS7RA0SkAV8HBqGvfa9XtZo7G3QMCWD6VSczLJPMHlBQzk5WLIvGZdpYUj5hRLYrRipMmdc2ERdGsNIJm6mX16V7u32l3mRLJttElbCCuZ-XF3Wmkt6k_xae1BwETS15fXiHJN512oAcW8Gs3U9Q9YeY_ZZ13JXK_elBFMW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه نفت سامارا روسیه پس از اصابت پهپاد‌های اوکراینی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/126702" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126701">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شاخص کل بورس در این دقایق با عبور از  ۴ میلیون و ۶۰۰ هزار واحد رکورد تاریخی جدیدی را ثبت کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126701" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126700">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شبکه عبری کان: عربستان سعودی نزد ایالات متحده به رفتار «اسرائیل» در لبنان اعتراض کرده است
🔴
عربستان سعودی گمان می‌کند که نتانیاهو، تلاش می‌کند از طریق جبههٔ لبنان بر تحولات و اوضاع منطقه تأثیر بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/126700" target="_blank">📅 09:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMCLzDU78uPWaxyfW86JVPkGcMaQ_24H8CsdLiAZx2Ft1lIhaGqvy-bNJXrkcmAQ96-aJXx8ldIwXtD96MubS1YsS1OJsvrzNLheweJ1aW8BJ9WEXO4X3TL3hEBXH38I5qjUzCz-Jt23rvAlhtEymuZFue3fd9UVXUCCBcaklgdmmYr14AhIls8LQCPhBN_we_Gfw5v7403btdASJmph9UOiaCF_fvGfH8xwaSVdCKJKvyh38YT0FQ38Kr2DS_vhR_rRj83IqvTrM68ocX8m1g_E4ioOKseNusC1MJHAi6D0Ek5c8dKdUMOfp-RVSORrYdBQ_bgKdROXp1vZdZloew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که فاکس نیوز از آخرین آرایش سنگین‌ ناوگان‌ دریایی آمریکا در منطقه برای "محاصره دریایی ایران" منتشر کرده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126699" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی نوشت: ترامپ تمایلی به حمله به ایران نداشت، اما پس از توصیه وزیر دفاع و رئیس ستاد مشرک، نظرش را تغییر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126698" target="_blank">📅 09:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۲ ریشتر دریای خزر حوالی شهرستان آستارا در استان گیلان را لرزاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/126697" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر علوم: سهمیه جنگ ۴۰روزه در کنکور ۱۴۰۵ قطعی شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/126696" target="_blank">📅 09:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی با وزرای امور خارجه ترکیه و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/126695" target="_blank">📅 08:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
طالبان افغانستان: در پی حملات هوایی ارتش پاکستان به سه ولایت افغانستان، دست‌کم ۱۳ نفر کشته و ۱۴ نفر زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/126694" target="_blank">📅 08:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEtc40SLGiBla0mOMod9pfccmvVYRQ-nFB_xTKHCFncxy-3MzCNv0MiMHh2BKi0LROqiuy4udC7Qn5Sop7G3iQL4V7kfMhjeudAo9eiWA6UVdCXDIXXhG7a1meXzXJm-xuVHEWdfZw-R2UuADi7ViV9wuBbCnW-ue0E0dQx47GzvuZ5BFTfF4g5hH-4KTPe8RA3WW42zHnSfp6l8_COPKEnawQ19AVWVWVm1eG__w1wXnC1pkOFuPgeazSZEOQHgYItgB9RTablOBUXmIMSYJim6CT8WZDAvdrEZE8ZrN8GRvlqC3tWNe8CdcdMjTLNjMv1I4K6ucUYGYgSs2ib15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منجیل که تابستون پارسال داشت کامل خشک میشد به لطف بارشهای فوق‌العاده تو سرشاخه‌های رود قزل اوزن کاملاً پُر شده و الان ۱۰۴۰ میلیون مترمکعب ذخیره آب داره، ۱۰۲٪ بیشتر از پارسال این موقع!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/126693" target="_blank">📅 08:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126692">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9b1ee28a.mp4?token=oHn1hpBK8bKkFtPs43V1i84jfhlCmPJGalSn3phzgAHAgfk8kj7iWvdX-k8e9etx3XYL7esaqv_4-oGcj2sczI14n6MxHsJTxhKaDVRKUYYtJV8Ha_pTw83QjGW3chraJwz7ePY2TI3BcVnfak7s3rJJNhUTo0onmykC9tVqqLGn4we4VEAff5zjYmSz_yMzpxzQB1F1N3URiF5OTD_rHSGhkP2KsOK2KsAhKAgT_JjAnwIWTX2i0cAn2xfU3SaZwkSr-lHACc6MgzhAF6-5vx6g9XM78wGLRf4Xr9yc72-7b-Qq2DH4f6CnCta43BjcV5gRNtgJd83NM9D7GPYulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9b1ee28a.mp4?token=oHn1hpBK8bKkFtPs43V1i84jfhlCmPJGalSn3phzgAHAgfk8kj7iWvdX-k8e9etx3XYL7esaqv_4-oGcj2sczI14n6MxHsJTxhKaDVRKUYYtJV8Ha_pTw83QjGW3chraJwz7ePY2TI3BcVnfak7s3rJJNhUTo0onmykC9tVqqLGn4we4VEAff5zjYmSz_yMzpxzQB1F1N3URiF5OTD_rHSGhkP2KsOK2KsAhKAgT_JjAnwIWTX2i0cAn2xfU3SaZwkSr-lHACc6MgzhAF6-5vx6g9XM78wGLRf4Xr9yc72-7b-Qq2DH4f6CnCta43BjcV5gRNtgJd83NM9D7GPYulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت موشک‌های ایرانی به مقر ناوگان پنجم نیروی‌دریایی آمریکا در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126692" target="_blank">📅 08:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI3ME9siwK8N9rPB9VxcoqmT7nNeYpBsLD0akRtMVeRifFKWYTX8at6MZb8O5xOlI9NffqhAixWW3O_TJZZM24Ef7YDEyRLPwJQrQxsxjYPPUdtVPCYX_dOZQKmuy4S0cpy0jXrOd2t51BD15H9tWMQxhVu0DXBzVbFap6RozQTFfOE5ooHzGSXRw70_IGAQ2LTfwpEOkOPcCelmGlMUifViwAFN6K7ei7OPbck8YS8nX739lGo6ARClEMau63VT6UaQD8FBTvd3v3B7e6scuEmU-g8CxvEurNOu1I2fPBi4qwXIaZs7GTwfTdbweTLWOvTo8Fs1TjI191qpoDq9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه جدید وزارت خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126691" target="_blank">📅 08:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126690">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مهر: منابع خبری از شنیده شدن صدای چند انفجار در شمال عراق خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126690" target="_blank">📅 08:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126689">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام آمریکایی: ۲۰ نقطه در داخل ایران هدف حمله قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126689" target="_blank">📅 08:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نیروهای مسلح اردن: پنج فروند موشک ایرانی که به سوی پایگاه الازرق شلیک شده بودند را رهگیری و سرنگون کردیم. در پی سقوط بقایای موشک‌های رهگیری‌شده، هیچ‌گونه خسارت یا جراحتی ثبت نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/126688" target="_blank">📅 08:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تصاویر شلیک موشکهای سوخت جامد و مایع دوربرد قدر و عماد و خیبر شکن به سمت اهداف امریکایی در منطقه در پاسخ به تعرض بامداد امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/126687" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
پاکستان: عمیقاً نگران وضعیت جاری منطقه و درگیری‌ مجدد هستیم؛ دیپلماسی تنها راهکار مسالمت‌آمیز حل مساله هسته‌ای ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/126686" target="_blank">📅 08:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126685">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ارتش اسرائیل: به هدف قرار دادن زیرساخت‌های حزب‌الله در جنوب لبنان ادامه می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/126685" target="_blank">📅 08:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126684">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9fb4f38b.mp4?token=nZ6G-9Ic20JtHjVLkb4NWUYX0OEfhbfmlwiedw3yZfRDOxRlQY8qQsQWDgJzx7h3OlY3QQ7D2ZxxX967WoNsz3nY6XReykKXDFyIhwWhuv8tUC3_1B6RrugT1tbhpYrfP6HbwgW3zf9-Dl8f7tLt9-RCYrR30gNkcaqI2QJTLQJBDTJ5bQ0t4k6uL7JK_Xj7nQ3bUYyFXfHbVC3iRcEZYVymQd8Q3IlBYTXNtESw_9Jtd5r5CWTfIOCfegkdaFBBV_K6X5vAZptDTOjp1NRItmKu8Uidez7o5H_vDDK6qDKWQl7KiQYsX1GvQzmQKZg8h_iJGSV1yxRdrBl-_uzlGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9fb4f38b.mp4?token=nZ6G-9Ic20JtHjVLkb4NWUYX0OEfhbfmlwiedw3yZfRDOxRlQY8qQsQWDgJzx7h3OlY3QQ7D2ZxxX967WoNsz3nY6XReykKXDFyIhwWhuv8tUC3_1B6RrugT1tbhpYrfP6HbwgW3zf9-Dl8f7tLt9-RCYrR30gNkcaqI2QJTLQJBDTJ5bQ0t4k6uL7JK_Xj7nQ3bUYyFXfHbVC3iRcEZYVymQd8Q3IlBYTXNtESw_9Jtd5r5CWTfIOCfegkdaFBBV_K6X5vAZptDTOjp1NRItmKu8Uidez7o5H_vDDK6qDKWQl7KiQYsX1GvQzmQKZg8h_iJGSV1yxRdrBl-_uzlGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد از حملات آمریکا به ایران، یه تیکه از سریال «وست وینگ» رو تو تروث سوشال خودش پست کرد؛
که تو اون سکانس رئیس‌جمهور بارتلت میگه؛ اگه یه آمریکایی کشته بشه، ما جوابش رو در حد همون حمله نمی‌دیم؛ با یه فاجعه تمام عیار برمی‌گردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/126684" target="_blank">📅 07:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126682">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ57MeKoggMCwyI1bpG5PDLkuvbw149nhrRn9_tCrsn1c199JrW6hAoUS9t2YA5qO42HvqBTjTU0I6jUXDPjH9ASD4vyqpQ1VAWq3K8JrFw_GxjLm89FRvlDr7crZi30NOWT_ejgr6yyR5BTuTWWjYPoltbhgOEl-vBIiyJcYSVyoJ71LT0uvz5zuQZaWUTjUDXir2b2qyi652-droHqQ0w9bwv9GjszD72ZHRZrwz5IJJDYYidDokJJCOR1KybTLXiTeucZ3DPH8XSIlw1L3Kr3qODz62vgK10bFfDAzEGH1WswywAx4Bo-lBUYtxDF6RmUDAoPNfBJbo226fmWkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZf3_LhciJBJF-dT6dKsW46Oh6hyEaEoMNwS7dWJLW1T2Qdp3mKYzKIJXwPWR4GMwDJJEkDUzh7QWttahrhYwOKw8nbwvdA2sWfcChhkBH0tmtmssoAHw-hSOhjXD4QZLU9Sj73ssbgYUYUTidmx2ximgOTiLu9HwMrZd9ccjChelsXQi3LjEDBkTDDSg-2a1VObWQSOoNMVQRYYByN6zgnBvAc5pBFU1NjP5miNu1spgEk5zNc9mOrUYE9Ws7ztKizm8K3j0EuHT1Pu6QVc3BbpVoguwodVgTidZUdSTpKIh1p00ooYItcwEZzxfPmddDyC0bjkJB-WxpAioH1qyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکس‌هایی از فعالیت پدافند هوایی بر فراز بحرین در حملات ایران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/126682" target="_blank">📅 07:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126681">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38746437b0.mp4?token=SK8kfowUeo2vJSqFUyC2W-lqXVOSpecdlMgh4O6oUfzp2SzZnzzcqdzAFjt4wUpv-s3H63kWGD8mxlueOBnSC9wp52XSRfK5nrHVy5ebHhVkLNuiH8U4QVKv4LTFkMBuI_3hWGPqlonae6DLYRsPluibyUSk-HNgjdlDcDMZmTw2GvwyhkPZSc1lGq6Ge2ReqKrfXwc5Zf141bETQocM_3xTDBO7mtOyRtGtdeZn3fxo7hh471No6CUM6py2slt7zRRvC06gqQalpjuie1ImMaHnXTNQR8K5LNjlI3a4RJNLDUjqmTEHIlfq5GAlaWegI4Xb7dlcEy05pHjyfrcASQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38746437b0.mp4?token=SK8kfowUeo2vJSqFUyC2W-lqXVOSpecdlMgh4O6oUfzp2SzZnzzcqdzAFjt4wUpv-s3H63kWGD8mxlueOBnSC9wp52XSRfK5nrHVy5ebHhVkLNuiH8U4QVKv4LTFkMBuI_3hWGPqlonae6DLYRsPluibyUSk-HNgjdlDcDMZmTw2GvwyhkPZSc1lGq6Ge2ReqKrfXwc5Zf141bETQocM_3xTDBO7mtOyRtGtdeZn3fxo7hh471No6CUM6py2slt7zRRvC06gqQalpjuie1ImMaHnXTNQR8K5LNjlI3a4RJNLDUjqmTEHIlfq5GAlaWegI4Xb7dlcEy05pHjyfrcASQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت موشک ایرانی به پایگاه ناوگان پنجم نیروی دریایی آمریکا در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/126681" target="_blank">📅 07:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126680">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WycRbjsDN224K4iZpvGPAkTP0R4oLm5P-qQVJtzG4SAmrDkUzP0p5HhRxBkcJho85bEp6EtEqEkcCJIHpIFCO5uPUEnEjdm-oQ0HY7O3JobuAwX6zYIznnKRRmWEyabtniQGZXrCGTO1uxQIBmbXXa2BPFKc1_OVRsp8W5taGwb4Bqeo-GGR6vVh-Jf4OQQwL2yseRx5Rt1LbS6zMByCj2kCsc29I4oJvmhGa6YsGp_qPL6Rmc7dZItR8JhXqz1rlUFjAK9wQQi77mRbfi8243tLqEVjDBKYtKd1AN1t5afd3FHGOTHtMbrPGanE2gjFkN-6Hd09GrjZLpE3VVdQbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به نیویورک تایمز
: ایران اوایل چهارشنبه چندین موشک و پهپاد به پایگاه‌های آمریکایی در سراسر خاورمیانه شلیک کرد و تقریباً همه طبق ارزیابی‌های اولیه آمریکا رهگیری شدند.
هیچ تلفات آمریکایی گزارش نشده است.
هیچ خسارتی به پایگاه‌های آمریکا از حملات ایرانی تأیید نشده است.​​​​​​​​​​​​​​​​
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/126680" target="_blank">📅 07:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126679">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/126679" target="_blank">📅 07:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126678">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUKNJy7PaN1dIh8HR-tcUcDVlTR7jb6dMYs0fqmC54Qy_dTped-yJzEbCqORIqF-YIWEWzcSD34jjd8SgjI8r3Ww-SDhe1QOrLcHsWKdF4WiSwFRCrcVA5ayk-c1hVouzO-3ofl8JoS_vmNRl8xaW3XReCK4xSCxxH4w11xVt-9p4MeFgIkzFZUXc4vjh9QgTGmc1HVi4BCQR0QLSHEQldzdTQ-TmXQxXtV08vKwhXqsVCxRr8WXncV447Xf8J7b29xUAl_SdfW1E51cWER39S4OSiYAA0VoJbwPV7tr9_HtCHY1oxjJeGsC4KiPROawhIuQDIeGSxoE5wXKGsJ7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
✅
این آفر فقط برای ۵۰ نفر اوله رفقا
✅
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/alonews/126678" target="_blank">📅 02:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126677">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7bc9515c9.mp4?token=QdP1vGLrjlcuYcL5yc7S78lC7d9U9AKniV-1qjxDeam8JoCKcrQLYi6DhpluFjEnV5cllviHDnbTROkb9ObFcFkzCkOsvPtdH1kjHMQw_o0aZvLQSIkK4FQByOnPC9iV-PkvVSsrpcMxGr_3FVIcgQTwEKoJvFRCaM2PrxnADrmDtaK9ITqnn64RDGor_WBslhbhu5wU9RbHkqRihLyY0OKGNQx6lcoFHLNVekageF_2CZGxj1SWuxve15Q0oZl4rVcWVGG34cdKG2qi64q_bm3rrLptmxtPavcgC_SoQv8MYMwNTK5o5KcaLQDWjiYo0ImM61Ywl00hcHHHXjPs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7bc9515c9.mp4?token=QdP1vGLrjlcuYcL5yc7S78lC7d9U9AKniV-1qjxDeam8JoCKcrQLYi6DhpluFjEnV5cllviHDnbTROkb9ObFcFkzCkOsvPtdH1kjHMQw_o0aZvLQSIkK4FQByOnPC9iV-PkvVSsrpcMxGr_3FVIcgQTwEKoJvFRCaM2PrxnADrmDtaK9ITqnn64RDGor_WBslhbhu5wU9RbHkqRihLyY0OKGNQx6lcoFHLNVekageF_2CZGxj1SWuxve15Q0oZl4rVcWVGG34cdKG2qi64q_bm3rrLptmxtPavcgC_SoQv8MYMwNTK5o5KcaLQDWjiYo0ImM61Ywl00hcHHHXjPs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اوکراین به روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/126677" target="_blank">📅 02:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126676">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
دو مخزن آب در بخش بمانی شهرستان سیریک در جنوب ایران هدف حملات هوایی آمریکا قرار گرفتند و طبق گزارش صدا و سیما، آب آشامیدنی در این بخش اکنون قطع شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/alonews/126676" target="_blank">📅 02:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126675">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3t1ZMb-tP8rGnDD8Gn4qeQ_dXJSM-RsoRk5GOkqUbT0vNKMhHLPk33eVBceYNY0i8Ni1wAnRv1NJxQKTYiARXnMn2KKiycSC-HbuAwx_vnSvKtaKi6hqTCUsnIilgKwrt2LlbOaBRF0o2hIjIxhQoOqbhl9nFkVA1pPD58HHRWaBo6bowmAfNBiACEzFmGqRZStRmHVFR1fFQJQtqr_WVpxbPV3DErPbm9CZcBfnEzPp77dPORwMTkec2HafbkyCr84YRlNNiuVE7NL09l3l-GASaaIueMpPM-u2rWAYnYdWjh_ShuDE8SeMiRX6gtWpL6NlfbJIpQLXK0BRjiL0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/126675" target="_blank">📅 02:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126674">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND0m-zDfgLpCU1s4HoxQg-upApfX0RdBQfK63ta5aGsoe_ASpKLOe2gRPA8LPqhbqHoW0QYy-dYNadATvEEJMlFKdYmbfUkvvxUjDw6VgDcY_IiESTFAs010jBIWEumJVkb9TkPv5ISUDuPI-k_bS37Xi81sAPn4jciT5MVbTfo95gqE_8CJZGHVGS-Ze6eZqStt50t4f6VaPBn-JCFVxj5-JVoOYnq6z1SyEah4prC4tw7g3B-QmtnGcVvp__EG2hdXXfF1AKrEPwwAKU6PkMyLHxsgHl1ZAOVBX2-ipRpFzGsIiDbhCOqQjOa4G2vabyqqwWv7KIIjotPWCp7vUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : با اینکه توی میدان جنگ شکست خورد، آمریکا باز هم تصمیم گرفت اراده‌مون رو امتحان کنه
- نیروهای قدرتمند مسلح ما هم هر حمله یا تهدیدی رو بی‌جواب نمی‌ذارن
- اگه می‌خواید سالم بمونید، از منطقه‌مون برید
- تاریخ خلیج فارس پره از سرنوشت‌های تلخِ خارجی‌هایی که چشم طمع داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/126674" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126673">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اسرائیل هیوم: ارزیابی اسرائیل این است که ایران به کشورهای خلیج فارس حمله خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/126673" target="_blank">📅 02:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126672">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کاخ سفید: ما معتقدیم توافق با ایران بسیار نزدیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/126672" target="_blank">📅 02:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126671">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پولیتیکو به نقل از یک مقام ارشد در کاخ سفید: هیچ تغییری در شرایط بوجود نیامده و آتش بس کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/alonews/126671" target="_blank">📅 01:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126670">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/ گزارشات از حملات توپخانه ای عربستان به یمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/alonews/126670" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126669">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گویا اسرائیل به سوریه هم حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/alonews/126669" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
