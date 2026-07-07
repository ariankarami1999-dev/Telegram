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
<img src="https://cdn4.telesco.pe/file/osdWt1GLC7NyW_x5VFgBwooyo6rUnF4bJBGE1lSt8yaqkk6BKtJolol1lI9i1kG7WeTmX8XWljmYa-KpL3jSyaNLhhuh5CmDIFMJwOHf-gD_A2r0ZprT7MEiRCGtX6KVubnCivqRF4xpLOI0nFBtVVu5F7_1NYAf36t1E14Xed-7-uyyTD9CLVtFjwHYMnOMgU3vqi3nPutrGcxPpcoKAffnIzn2Lu93C_kyJiu6ro5bNQm6J0n1rCF9guBQOQrHYE1XHxWJI4UdMCnm2jLnP8-X2b_vEORvuaVG06XtwoOPWdYW10UAXRf923PCYBK6M-EftC36TwPbqKerLh7Rjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 338K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 11:29:05</div>
<hr>

<div class="tg-post" id="msg-16617">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: کنگره باید بودجه ۳۵۰ میلیارد دلاری دفاعی را تصویب کند
@withyashar</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/withyashar/16617" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16616">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شبکه الخدث عربستان سعودی گزارش می‌دهد که رئیس‌جمهور ماکرون، ربع ساعت قبل از وقوع انفجار، هتلی را که در دمشق اقامت داشت، ترک کرده است.
در سوریه‌ نیز گزارش شده است که رئیس‌جمهور احمد الشرع، دقایقی پیش از رئیس‌جمهور ماکرون در کاخ ریاست‌جمهوری در دمشق استقبال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/withyashar/16616" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16615">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4093af6c8.mp4?token=h3cYolUcr2Tbjp6IpKSfwb1iUzZOvRB_uRYXMtqkFe9Hgkh-5eFvI5zRND-1IkUWq-ZRjpPUmzmfNPbbmJLCpSRVyJux9KSnUK2_qczidlQVHl7diKV1RqNRYpfDjFqa59XA-2Sv_zUcArfwoPCM183xj9b7D1JsYFbx4vKlDJsdufGO0iAHzoUfbzbFf-ygQzb1c1qID6I9ZaLYdbJ64tXvAMXDlzUMxYiUWr1FyC2-P9VhIgpG_dHv-A5smqYatpL5SUWu5yBQQV3-mqo9oT6Vrw9i7-cDOokL0F_zVIvzucYq8Dd91Y5M_m4V8ucQkj5aRAc-yEO2NKoFQKZT6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تصاویر ماهواره‌ای رویترز از تهران در بهترین ارزیابی حدود چند صد هزار نفر را نشان میدهد
@withyashar</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/withyashar/16615" target="_blank">📅 11:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd6db78ff3.mp4?token=LkU70ypk24I5dGRNROX-Y3668KJiJlfgYjxQbm2lqj0m1rcE6wTDjsvR1TZO3wKRtLgJWE8hNfgj_VoVNVHC4JemmY3eOjfqmz8IPytU2Tkv-ZQT4tZZZIw2zinNXQm_KcaMNrOINqTTRJvU9BxjEP9HdCgHrArlsQJvN0YTUy6cmbkOjKbvcSg2QP-kawPGvut_Jr81jiOrpaeNXadxxMmnsSBzsqwbiovCSORVwWgMpesww40Nf-r0XkjoRwbhCR4-rypClYfh1FmDmH4jKcRIaaVywixtY_FpvG6SnZu32edLkDvaKDvkf4wh8gzWztn5s3H-u2KrE_Tbqh5ZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند انفجار در دمشق، در نزدیکی هتلی که رئیس‌جمهور فرانسه، ماکرون، در آن اقامت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/16614" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک منبع امنیتی ارشد لبنانی امروز به روزنامه "ال-جوماهوریه" لبنان گفت:
"ما در صحنه، هیچ اقدامی از سوی اسرائیل ندیدیم که نشان‌دهنده عقب‌نشینی از مناطق مشخص شده در توافق‌نامه باشد. برعکس، شاهد تشدید عمدی تنش‌ها هستیم."
@withyashar</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/16613" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رویترز به نقل از یک منبع امنیتی: انفجاری با استفاده از تعدادی مواد منفجره در نزدیکی هتلی که ماکرون در آن اقامت دارد، در دمشق رخ داد.
@withyashar</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/16612" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
@withyashar</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/withyashar/16611" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a464e4c27.mp4?token=IjRupySFkfV_gddBm9hsyQrXZ0XHDmx1usUC1NbWJOw4Yq_8MjEReq0uY2qZhPZFQthI_SOeVbTTVkpEedTKir7eKVrDtftvZfelkDUnfPGvq8FayfTubz8Kl68UmzxP-LjFu6gzlMDpzgaQZ49pJOsDsgdhahfCi6tGoDw3dG0sQoWukfW9n0HKOgc9lHUAIbHluyotBGRPIAXO9-OscCcqS79MAeUCOEjG-m6oEcNhduWerkaxgdmW1YFGUFdGwBUflg5xN7EOg3tgGBh7qW0T9dc_MSE_xMoGrR8MMD73jOLwMHf7_wzGfk7hqC87WXcUc0wystNtHjqq3m_HuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره ای از ۶ ژوئیه دیروز ، چند هزار نفر را نشان می‌دهد که در نزدیکی برج آزادی در تهران، ایران، برای مراسم تشییع، جمع شده‌اند که کاملا برخلاف ادعا های میلیونی رژیم است
@withyashar</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/withyashar/16610" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN3m7ICGIsYpIddRTA2xNyw-bbHsM1twKEyGpQNh5bBuXCe4djNA-p317rxqoGnWTm2iXSy9P_PzUbaiQGGyupzO8nyK6_zUJLWCpnOv33GjvxohuZSTvXCKaM4dfL-VpN5sk1NsxOgDbhkT4v7ZPO-tMsVHxl469MqzUCr1USK4zFpBON8gie-tpfFJ4W5AaQDj7V0TsByB-YkL8G5biQ75BlnkNJhNnB1niI3mE4WP8CKgnSdAQ5acPJXnD9pCcnMDJl9-X4XL1OkKQX2aKu8b47GUQrcEibMWUnpXGpo-7-9FSwZgL3rdjhbjgzAM5AxkILkECMmyGtcUZV6KIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدل ایست نیوز : تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
@withyashar</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/withyashar/16609" target="_blank">📅 10:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kB7GtZtQ7gV2uuFzx8a-JytthMDbpAGtclfZtfJWGIy3tTi5fgWCw20SFYmebTBADpKX_XMun_OxHolXDqLZbnsgOX8FNdrIjLh4sfxJRogIxIPumfdSdZkx2ArHo-AN5l4ofYWzkulfMU6AsBy8QKtUXcKY55w7wdnTE9lDVo87M1CW7gXk3p_83LCBGMZEmgGwnslIHSXn0lTbXbE5mEmxTXWWbSUUkOXTZBFYS4jgNJE_utRAB7ZC0z47Qdl8OlvGaDqAdal5EehyiJFizwvQAhxYaQSSxsvIj7OKJ_a7Gq-xeHhgoc_-Jp4wkd7EkpUm_Y_2L6UL5KLlI5p8dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/withyashar/16608" target="_blank">📅 10:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عراقچی به ترامپ: به امضای خود پایبند باشید
تا زمانی که تهدید‌ها علیه ایران ادامه داشته باشد، مذاکرات برای دستیابی به توافق نهایی آغاز نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/withyashar/16607" target="_blank">📅 09:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به وب‌سایت والا گفت:
حماس هیچ قصدی برای خلع سلاح شدن، تسلیم کردن سلاح‌های خود، یا تخریب تونل‌ها ندارد.
استعفای دولت حماس یک اقدام نمادین است که با هدف نشان دادن تغییر به واشنگتن و شورای صلح انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/16606" target="_blank">📅 09:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/16605" target="_blank">📅 09:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTWHSiItylAfhanwHch8it4yaJZ7xRwr1IQKt9jhu4Qwury5nNTQI8vtxn5mTvklhN8fwSe_65zFXNys0eQagcyLlidvovB9DNcsDMvateWaaaZkHta0g2oYTNnIA8Bu4ONw00SwmT4_kuU5h_yWVMkrVfu6kXiJcy2-EI5WMLe9lJqYTc7qGKgtA5pb8IW8w1lz3dHnYu4hg6Vd3u6ALGnnfXgdBqssQhiSNmFN_83A0SKhu6lo9kMcabzG5Z-gfEQ0rdSwac1oF1cirUsW0iOYuoGkzlyOjU71fDgOASD9zDWnKZMhv4cnL34rv-ulMM0pv0DR2d2VzF_awmHc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک نفتکش در تنگه هرمز هدف حمله قرار گرفته است
مرکز عملیات تجاری دریایی بریتانیا: یک نفتکش ساعتی پیش در فاصله ۸ مایل دریایی شرق «لیما» در عمان، در کریدور جنوبیِ تنگه هرمز، هدف حمله و مورد اصابت قرار گرفته است
گفته شده نفتکش مذکور حامل گاز صادراتی قطر بوده است
@withyashar</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/16604" target="_blank">📅 09:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=BguXC3BvyVmGH50YCg2xkEoJvHOrX7ocJLHaO2JXxOdWOVIxXYbqI-sQW_PFSVH87axDWRIYPv5EIfdaAJTxKGLRwASmT9be_l5r4iV5n09ceBR5gru_ZY0jJSMv9E5e-OYS1b1zcP5gcBpAKYdko02evZLt_3g9kJixSWw6wIJrwp0ZgwrTuMeAQt-Yix84b1Te3xzR64Mwj3YPQaSztuNN1dp76xRD47B0K4CmS8whPH7tTMU6x6fZU7HwCNnw9oENxRcq_uzV1l-lAZ3urUJ28LNJfjTOiKhTTTXeMrws8DDBe-e9KMsOYaUcrFCyCkmkGxgsbJh-vofLqXtkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd75af4e28.mp4?token=BguXC3BvyVmGH50YCg2xkEoJvHOrX7ocJLHaO2JXxOdWOVIxXYbqI-sQW_PFSVH87axDWRIYPv5EIfdaAJTxKGLRwASmT9be_l5r4iV5n09ceBR5gru_ZY0jJSMv9E5e-OYS1b1zcP5gcBpAKYdko02evZLt_3g9kJixSWw6wIJrwp0ZgwrTuMeAQt-Yix84b1Te3xzR64Mwj3YPQaSztuNN1dp76xRD47B0K4CmS8whPH7tTMU6x6fZU7HwCNnw9oENxRcq_uzV1l-lAZ3urUJ28LNJfjTOiKhTTTXeMrws8DDBe-e9KMsOYaUcrFCyCkmkGxgsbJh-vofLqXtkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوایی که ما تنفس میکنیم سیاسی هستش !
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/16603" target="_blank">📅 02:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=anLyq1cqxsBOOwSTmQ5LFVqInnim43coJB3AoVZEywDFgJw38XA1cAmrszd94GyICN0lG1nSh9kU2z9Tqj0UBdnYvydnykELsRJmOnQ6YuC6d1dhAOCLGV1L7YKfyyeuRUSXxT9IVfkBQw8wZFZS3D1rZW3VYNPa0ZNEng7yTT6A0DLlJfvQ0I2gU6glGZpDi_ASec9Vre0wXmf5-1YDuzKmnYApAtxnhwSn-FU0WNY_K73tWyKDHuwVZ8MEEHxlO-BH2WcbOE7oNo_O1cvAgu4q-uAWohjbjrgYP3OoCKZ4xzMYaBi2rfcWI8KpCCSrM6kOxELvegGm9rjp0BsBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd4aa6711.mp4?token=anLyq1cqxsBOOwSTmQ5LFVqInnim43coJB3AoVZEywDFgJw38XA1cAmrszd94GyICN0lG1nSh9kU2z9Tqj0UBdnYvydnykELsRJmOnQ6YuC6d1dhAOCLGV1L7YKfyyeuRUSXxT9IVfkBQw8wZFZS3D1rZW3VYNPa0ZNEng7yTT6A0DLlJfvQ0I2gU6glGZpDi_ASec9Vre0wXmf5-1YDuzKmnYApAtxnhwSn-FU0WNY_K73tWyKDHuwVZ8MEEHxlO-BH2WcbOE7oNo_O1cvAgu4q-uAWohjbjrgYP3OoCKZ4xzMYaBi2rfcWI8KpCCSrM6kOxELvegGm9rjp0BsBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع جنازه انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
@withyashar</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/16602" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDNVcoHcnzyCFw4e4eytzPPncgycHWpYwLBXsBZSH8RYh-sFbnATMKK7oOQBYY2XXszdNDdq5nli3RjpbdKhn-REWpiV1lYnVclIh7ADtCLUSfxwK2GLEiYQzm6NWd7vPKJZK_5MulrNBHH9KiU5tJ7GTLcZYN92KZd-sRMFFIo_B-sKw0MtB1SPE4S9QQo47xrVXA3WMN-dw51caOwTsBryxSXuHgXQGD2Rw1-T7SpH13tadfN7JffzivH2l7C893H5VOzYRswM7zTkTzIARBPiqxuLcRExG1ynujdlo21sBVtqKzI8ySOajn0HJgEsUQ6M-mPEqXaVm1RA6kEqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر هوایی از گشت زنی امروز گروهی از قایق های تندروی نیروی دریایی سپاه در تنگه هرمز
این شناورها در دو گروه مجزا به حرکت درآمده‌اند؛ اقدامی که توجه و دقت برخی رسانه های خارجی را به خود جلب کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/16601" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وزیر امور خارجه آلمان:
ایران باید تمام هزینه عملیات‌های بین‌المللی برای پاک‌سازی تنگه‌هرمز از مین‌های دریایی را پرداخت کند
@withyashar</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/withyashar/16600" target="_blank">📅 01:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c696b52038.mp4?token=Kg7_W9hIjqlGYATWyHS7_DPhd5x_cU5ZBXIaKReFjEufWJg6M5LIkH97PqqSYZ9PKDYNvgYYDA50Atib5fNsBZagMAtO5fXGB6VET31GUtbLvTBxUMIFgsnq1rfoJwfyW98g_VoIZY08KlnvNwDWVYtKV9WmvC8zRerFjWdAUr4p4dQtAa1IBchGGFaYWw4A66BdNu7VyyIXa2aBWuepsOJOnPuhF4LNxOD1pFfpV_UPULw5CEEDUq-8G1jhl8UwzUbgXSlRwR_nzugNdfu7ah0kCeQtI06ttH2FucNjRCF3kXNyWQ-1TYPVsOlUpzSi_FpK-mqptGAXKHc_G7u9_ldLk23xozue226t0OImGPWZclq8dVA9nUmz_AWM3ZtcztHGD4ICFO0mej3sx3xAUgaKOD005j6d-YaqslYFiBxgE-CdtvcqVvijTsCQKj_br9gd5uhHiNRTCy5xMECNTzu26-kvaagt1zkySv0YvbLP7i16Gt-vdvFlypR7bThYNlXGimFu9-h4sXtDMImf67IE4O08594QJQETkNo2qAqW8GSwpWRuFC_0t2umAraMm1VVkRDzhL5_OV42HK3HXvsVhiVX_MCCueDEyvrOJhn8XIsAjonnP0UvLElvYMPE_07qWoKj8I0X7EJEfng-X_CEIP5MKDsusqOvb8GHfD4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو لوئیز نازاریو دلیما</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/16599" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/16598" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from~‌🇭🇦‌‌🇦🇳‌~,</strong></div>
<div class="tg-text">طرفدار کدوم اسطوره ای شما اقا یاشار؟؟؟</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/16597" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نانا کوآکو بونسام، جادوگر مشهور غنایی : کیپ‌ورد آرژانتین رو حذف میکنه، من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود! @withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16596" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up-Fq7812k6gyJifo6kWmAQdMraZaNEAdAc0DXDhL3m2t8nUnu4VJ538H61hsCWzeI7uOKaD90UK01ivUI98RK-pnX-E6jcHSou9YXmh8VsdR1kGApPVROqL3JXz4QMIcB1fjKzb2nAHGPbzvAQMYhVHz91xJarxRNcgYhmSRxXk9ZewrGJarN7AbNUWmC146WGZ73u-rolQkawunBm_mbk_pN6zovK3B6NUO-gFpYQ2oO4_sXM_DjEdngDtJxo2bQzCzfEGezDbDrJfpR-HCUIs1jhtEy2h4Ke0TBlqiZ_kXgpbPPjsMQpnpYxL8fhcgt7Zmku1hymrvDQiO0e_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ پاسدار صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@withyashar
🚨
🚨
🚨
🚨
سربازان گمنام حضرت موسی بد فرمون دادن</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/16595" target="_blank">📅 00:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آکسیوس : نتانیاهو در تماس تلفنی با ترامپ؛
- خواسته که به اردوغان «تذکر جدی بده» یا «جلوی رفتارش رو بگیره»
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16594" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شاهزاده رضا پهلوی : ‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی هایم، تصویری نادرست و گمراه‌کننده ارائه کرده است. @withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/16593" target="_blank">📅 00:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">استان هایی که تاکنون سه شنبه ١۶ تیر را تعطیل اعلام کرده‌اند:
استان تهران
استان قم
استان سمنان
استان خوزستان
استان مازندران
استان اصفهان(شهرستان های آران و بیدگل و کاشان)
استان یزد
استان مرکزی
استان بوشهر
استان لرستان
استان هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16592" target="_blank">📅 23:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیوید کیس مشاور نتانیاهو:
بمباران مراسم ؟
شوخی میکنید؟
صدها مامور موساد توی اون مراسمه!
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/16590" target="_blank">📅 22:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b93d61ac.mp4?token=IWyWkvx5O7NAZwDfyN7Wcn6MBwDe1sEr7yPW44yHtGSRfs1btOTtk-u4qW_nR13LIFDI-8A4UW0xhsRthJpoSJQ8IXPnQry7xKBj-rKJegkn4f5nlDCAi68kb3A1HzNxzFDNoFPiVGFxji2mRCAeQQ8wR2-cVAziHFd21XLhgFk67NRhdfOArdzuU7I8dPgini_vg8ijEfYqNl-Wv40fku9OYQ5yd512sR8V9ZmCGvmbWqStrY-pMKcJLFapK16ixv14c9v2R6gLgTzA0d2adfvmGNZ3-swcj4uGXF9e3pyCdSzSrzh5VeY6mxsBtoNfvDnvlExCZiVvStAR8SgWDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/16589" target="_blank">📅 22:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم. @withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/16588" target="_blank">📅 21:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36f95eb134.mp4?token=S7G6KcQLGCCJCh3MyUhOxq4u65TWf1_1tUv4tONCbOykYgaklOPMkFxf3HKfUH-FqdK-V5zlEzn5zMd55M_W73xzf1T6pfZ4Kj4fanw3KD9OQFMS-2F9FOusYdlCuVpZaUTIX6pykN8cJZ10gBl4tYNISv2K2Ja_C2_3PuHs7dimkl7WjCZgMqa0_RqxIAp97yPtUWTkGVuvrtjoggxjfBCwlLNHLqmAkT3PZVVlihCfIb22fMwq44_viKs4JoRLgwOs0jeMDqcZr_6hKECXWrnFKnJiK_0_XTQi_yyrH6KaDgUrlq0_NdBPy_IhHgFo04w2l6KzuMm_N3lgUQ6MYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکرون با عینک آفتابی معروفش که ترامپ مسخرش میکنه وارد سوریه شد
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16587" target="_blank">📅 21:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رئیس‌جمهور فرانسه پس از ۱۸ سال وارد سوریه شد
یک منبع ریاست‌جمهوری فرانسه اعلام کرد که سفر رئیس‌جمهور این کشور به دمشق با هدف از سرگیری همکاری‌های اقتصادی و تجاری با سوریه انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16586" target="_blank">📅 20:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a3ca4796.mp4?token=lGW1ZniRVT5tVJVXbnwlEoHL4DgHBXnSoQA4NDeWxT_p-XkoYyfcKbe1dUItkYMtVCojMpMj2HDbuB3rA7D_WwE_zdhOaBJjccxPdLaLf-LBht_B-RyzIqCGGF3XN-1p6EVM3GXrLEgsN7-op9tNoaOrMFEORdTaFKKd8lFLlbfw59bWE2p0dAXmPoHacGJh9KV37jG_YBdhqq2t0lgWU2ZsPrSBqbiE0HzSj2Sz3F_75O42hxmpiFux8yMmWz_hsRvmVCessRwpbWvCBUgYjzPEmji-cj4YzMX8TU32Dx5bz7_xJ2-oV1-gq6r678DEBpAc1Gogho54AtQwhrrOqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنازه خامنه ای برای همیشه تهران را ترک و برای شروع تور ‌کنسرت ها کمی پیش به قم رسید
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/16585" target="_blank">📅 20:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34927b66b.mp4?token=lfSKNQqUmD11BvQUw6DLJEA0VI5fHdQS6ypNP51v38ng1YyFRQAOtDad7wJXsHQ4pnm_ys5LG4Z1L_YafYCZC7YnZwNc24bfYE0JzVDM8E9vhmi7DIrdKCDKgMPff2L7uHL-sABDHMUKSaCKNWNP15s5IK_vLFdx3YMMFXKJpm36tD-SZPY50aTmIDaZSmxBg6TDrC1VQWKGuvmXNcWpSw7Q7u4l0_jV5qqcd6Gd3gErBbr8-p-z3Kv_zEZRKxyQ7GWx8xoRu-EVsnZe5GQ-RjNB7q8QeOT-3KH-d7TDA4CGE5dhUjehnhxR00VZSdParS9g1pYU2ybhnlmPlB7Nwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این نسل چی میخواد از جون ما ؟
اومده تخم مرغ آبپزشو بگیره…
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16584" target="_blank">📅 20:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8667c144e.mp4?token=qWPGzXijIEG2TSxn4XcDHv5rfbqE2BoYuLZN6AqUnia_ZP74GwcA7-yotbBemcIueJCSKwMVjoq6fvn7Iwi-Rvj5n3l4U5tXLqSeVZmm8vnJkz32J2_bruOS-FPiOrCXM4IAg45HPppV62Ma4q16foqzkIbNgK9W5sByOn3Out_ea9MhFXSJeQm-h9Nz3pWsyoxOOx3BxRNEynT8w4j1bkPuJKGMDVmpg2JBWYc4a5M2ZFeocrEqFgRaxRamc34IMdSFFQjqTXhtVmUMCAf7XJJbXMBy1I5JKHo6E9oNCifw2pUS0E0SqMZfz5JfB0__VcIlH-5s_tFStc77XHFgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی  @withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16583" target="_blank">📅 19:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiOBNdlHcj2u7by0c4i4-lxjxQ63elvO7pHn28CxBpMxmkSdBgm70TGz9Fl9yWgWHr7xr6wzhBTtuezc94YEZ5WkDFHJXW4bnr5xogobq8Em1sYHqL9JVFeLLtTljoxu1iarqdS712jB9FVNWXsX4UM4jIqWM_FQ8GIBMl6L4jg9kZHPeCsXNGDkEWctlfAbZasGa9atOUPtsyddS5a570zWXU-b6AuaenMOsiNIPOtoOHQR82x8sDJeltZZeelVtqm4-z4HKEaZ_pKA7Zxnw4oLgJcjhEel9qfwOlExMSb4jcC00gi96D0yE932DCfKuer5lw7iXjdthyGwz1uZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهام شرکت دل پس از اظهارنظر دونالد ترامپ مبنی بر اینکه «بروید و یک کامپیوتر دل بخرید» ۸.۳ درصد افزایش یافت
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/16582" target="_blank">📅 19:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ : ما از ایران امتیازاتی گرفتیم و آنها باید به آنها پایبند باشند و ما همچنین اورانیوم غنی‌شده با خلوص بالای ایران را دریافت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/16581" target="_blank">📅 18:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ae96c363.mp4?token=cmmPNKE5I2zG8nc56EnY60tWVZc36fezl1KT7qzG4yZx_MutWlD32sy57PcmYm161QaOiVSWffQcGB7LsP2a44DN091NflZoBWc-C1J3v0k1VnNcKCqJOFRe6iS_mNm_RanUF0lsVnkKOnP7DayEB2UNJ0J7239WirLqyIlTlLAhlnhk3F98NL1da_WsuDOyaTGoUnR38_W3m8HmoBPDPt457nSxgJ9BZvCORaS9OT2E6Gatkj-sutVKEzcIi6_tne0r48qkPyVrtyo-sTNNXRI4Cec7Kp7MBWxC3aZSwSzZNYL5YSeUaz_XyoIQGtzGf3CH0Bq5ycyf5Qn7iSb1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بررسی ترافیک کشتی‌های تجاری از طریق تنگه هرمز طی ۲۴ ساعت گذشته که از طریق مرین ترافیک قابل مشاهده است، نشان می‌دهد که اکثریت قریب به اتفاق کشتی‌ها همچنان از طریق طرح جداسازی ترافیک (شمالی) ایران عبور می‌کنند و تنها تعداد کمی از آنها کریدور جنوبی تحت حمایت ایالات متحده از طریق آب‌های عمان را انتخاب می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/16580" target="_blank">📅 18:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cbbf8bec.mp4?token=L0-jp0NcQOu_5AQ-49UNtekpl6eWdBr6J0bjD9VKzvZPQEex6Lct-XnMoOt4H_R0vTkgdJ1pp7ia8CL83Aivl02mBIwnZyJVLuXQvT6ztjktSeWZWO7mAAYy8PdeJUL8y_nrRPVB4JPNasP0x242m7putGZ4ATMzuGJrpQT915C6B3QtRXHQ5sCGUZvXULRNSwcvB2oTiWNoqT2uLBdSju_4dm3fY8m8niFelzSIhLMc6AFOav2oCFm6782PGKG5oE8Q04xzt_oZL8zfHQYgBkptdisxnPR0mywaU49Ul9Cnl7AYGQbprJWR59LnjPRrGi252DQoFmzMsj4UPEGIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد جنگهای پهپادی: چه کسی فکر می‌کرد که پهپادها به چنین عاملی تبدیل می‌شوند؟ آن‌ها ماشین‌های کشنده هستند.
شگفت‌انگیز است.
شما پشت درختی پنهان می‌شوید و آن می‌آید و شما را می‌گیرد.
و من صحنه‌هایی را دیده‌ام که نمی‌خواهم ببینم و نمی‌خواهم شما هم ببینید.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16579" target="_blank">📅 18:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: نیروی دریایی ایالات متحده بزرگترین محاصره‌ای را که جهان تاکنون دیده است، علیه ایران اعمال کرد و حتی یک کشتی هم نتوانست از آن عبور کند.
هیچ پولی به ایران نمی‌دهیم
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/16578" target="_blank">📅 18:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1c3a4bd0.mp4?token=cyZ5vI6tobojHGPA3f9rfT0USClVX9w2pIehVRar6cpp2lqUplHOd9EwDEaQ-LN_nd8dER7aR_LwCB4Zu67G9aVxj_2V_dEpU6fvS-taptxgBWnuBh1slbQt6lQxD0W4Hd1PNAnEi31JeJ_AFVegC69MZlnfdaURMtUeWws0Hy5X-qQ4yyi8Ai1PjfqFB1PUk2aOe0mVVD65f6q5tD5r-RqQjZ00BFRaaA79c3tamLg6RZ_f2VcIPPwyGGoXxRSQ7wl-gZQ3q-idhrgzfApqPBdGghB_15_erKIXeAoXutTTTbtCT1Dg1DUq5v30l2S8eAO81mTOzV9EjIYceA8b0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره اورانیوم غنی شده در ایران:
ما قرار است چیزی را که من به آن گرد و غبار می‌گویم، یعنی مواد غنی‌شده، به دست آوریم. من به آن گرد و غبار هسته‌ای می‌گویم.
من به یک دلیل بسیار قوی وارد عمل شدم و آن این است که ایران نباید سلاح هسته‌ای داشته باشد. من به دنبال تغییر رژیم نیستم، هرچند این همان تغییر رژیم است.
رژیم اول رفته است. رژیم دوم رفته است. و من فکر می‌کنم رژیم سوم منطقی‌تر است، اما خواهیم دید.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16577" target="_blank">📅 18:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6831709af6.mp4?token=adc-0rJb2TNKYOhJD3RKR1E-3QcEj9q7oIigDN003uhYuJBKUvhkXPxexZlGEyLEpezTEpT3GZOj8zq-gOBP7Ys8V8KFpnX6gbSs3oDXjo0m_WJ_I4Hq45MInpYj0OgBkVxPcnNdYbJjuO7KOtOXSDj_BaEiMXx0BYYNbSlddUHfXZui6D3twZix9Zr_9VgjAUNLm87IBadGvKQUCN4J1ZtFTE2BULuO0hj8DQJb0SfELBCQf1CfG6iSP5JGuL6C02ZmIZv5OfLMdRkNZydufpyMzCARcEgThaFf9ARfHEs3jtWal1BVQLDv8INiNfSoXCf04cJ6Vh4hr0DQ0CedFVYgAZ2t4HXm3EROoctAvqf9jp-olePM5VcnKfky1M6Rx49KpSVwteg7eYjU7TLcCmi5UztCCNkn-5ZPortuQN3pzj0uk-WsfRbxZ31yjyTmtacIvama8PFCM3-TL3GrW1hCYzd1AvMw-IftDIqwdGVHXqHl7LY7mHBuC9uIg8HNT3vkAcf1jFROA32PjXU5pmZe3R8ax7ntu-Wbx_hNN1ZtktYgyuks2uCrevox0ltb6vy1pgnTioJYLvTxTZVzcFdj0BSYOu_heZrOPJy5HRxFCQcySh5b9fPLlbBjcjD1ILPnbjZTaPGXSBS7u171xTCJahJ4TxMSyPOyg9OZyhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : یا توافق میکنیم یا کار رو تموم می‌کنیم، تمام کردن کار سخت نخواهد بود.
من ترجیح می‌دهم توافق کنیم چون نمی‌خوام به ۹۱ میلیون نفر آسیب بزنم. می‌تونیم پل‌هایشان رو در یک ساعت خراب کنیم.
می‌تونیم تأمین انرژی‌شان رو قطع کنیم، تمام کارخانه‌های بزرگ که ساختن، کارخانه‌های بزرگ، زیبا و مدرنی که پول زیادی هزینه شده بود. حالا دیگر پولی هم ندارن. ما پولی به آن‌ها نداده‌ایم.
می‌توانیم برق و نیروگاه‌های تولید انرژی‌شان رو، به قول من، در بخش کوچکی از یک بعدازظهر از کار بیندازیم. هر نیروگاهی از بین خواهد رفت و آن‌ها این رو می‌دانند.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16576" target="_blank">📅 18:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:من به دنبال تغییر رژیم در ایران نیستم و ترجیح می‌دهم به توافق برسیم زیرا نمی‌خواهم به ۹۱ میلیون نفر آسیبی برسد.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/16575" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال ۱۴اسرائیل: مأموران اطلاعاتی خارجی، مجتبی خامنه‌ای را در جریان مراسم تشییع امروز در نزدیکی میدان آزادی شناسایی کردند.
گزارش‌ها حاکی از آن است که وی با پنهان شدن در میان گروهی از افراد حاضر در جمعیت، تلاش کرد از ردیابی بگریزد.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16574" target="_blank">📅 17:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fx5Qb9zl5O4UgLEiUTLGlPe7aIhNfDDKTPlOFD1C7yut57YZChNF6MX6DlMQaKQIh88d57ArC1kjCRaxnaYVl3qB0CKXdr66WmYfuLqu0GNv8CcPX5kBshsX_kllVDtKm9oiszDQGXDjKJrHlvMfZ3r7uljsuLG8GWJ5xt9WrhAw46uqh5FBjFAqQ6JkcHCW3mFl3Y_Lznwj8hjhtiRC0BcoOBimLwGn5aaHZT4faHdp-NoI9KXU4FzVnTn7gCnUJhY2_7WNMqSoNnIhvkezld8ndB14UqzYg9dDV5EeAAT46w3huUqcggMDn_sPotLOyNEXogqj3cEalqFho0REcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاه وشی این استوری حقیرانه را منتشر کرد …
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/16573" target="_blank">📅 16:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مجری فاکس
:
چرا این حکومت هنوز توی ایران سرِ پاست؟
نتانیاهو : چون چند صد هزار نفر نیروی سرکوب داره که وسط روز آدم می‌کشن و شب هم مردم خودشون رو به قتل می‌رسونن
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/16572" target="_blank">📅 16:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a33dabae78.mp4?token=PejF73Gh-leUA9yCWIRchoilsE2hz02ZJ_br2vhTXyrYJMLGuJMRteYMwg-wtGr4zTEx3D03CiZZZ3FruIGH9BwSvgH4EWR8KoSCbvKOTrF8JdYN6oMLhFtLyZYkwEa6uMqJNZlnSqJk7btX5vaaB_oYDOBnte_ZiPlOp0N5vKSsak0HUPHdEopP7I9JXK0ulVtn1I4tpAS6RCx6UtJURYCUU-ducDO1ADbnuOzCw9RkrxDpulcr84-ISkPRTMzHdvG3StrNXLeuwhWIhMyNAIXHyW8WlSfAT5Q49QZqkwP3cxMs5XslZGnUaIqoX2SFXqGwARIcDGdUmlIYu2_Vf1MNchqjalHMBAFzrJGLbttP4v0A7WnpnHvSik2N2Z92eGiDm6xu3wbSdyNsroRUkMYVbqzd41bEHWBPQ8TPFZxpy1jNpYapfNsKs07HiJVZqEv5QntBah3CTctghQmJR6tSXTHV5Vwe7ar3Z2gnO3RrwjiSwArsytH6ufkvHv-2jEErBAXl7oQ8rSeNcBuBZBESAdhGMZ5wswgf0t7EiOkWkUCmygr8LB0UJKq9zXxiSYVwNCNbgZovOhXZnb9cRbKtU17CY7U0JFMt2xVAquHsAK2fKXJjGjfxCUxgem-TQMHKoFZC-cmu0GuWuAN4zuDZQLB0xhfnQskixepy6Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎نتانیاهو به فاکس : ایران حدود ۹۰ میلیون جمعیت داره
- به نظر من حدود ۸۰ درصد مردم از این حکومت خوششون نمیاد و مخالفشن
- ولی بازم چند میلیون نفر هستن که حکومت می‌تونه بیاره تو خیابون
- اون‌ها هم شعار "مرگ بر ترامپ" و البته "مرگ بر من" سر می‌دن
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/16571" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حماس: رئیس کمیته پیگیری امور دولتی استعفا کرد و این کمیته منحل شد. همچنین اختیارات این نهاد به «کمیته ملی اداره غزه» منتقل شده و تمامی مقدمات برای واگذاری مدیریت نوار غزه به پایان رسیده است. @withyashar
🚨</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16570" target="_blank">📅 16:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwuoRGQ8XfDkuN1d18gpw_DS8HnHachji7PD10S8iPVpPPS1Wvp3ZI1AlU_7b0b8Qd0U2Cg8LwLJc_mtDt6MiiNpbiIJzmacEVtXj-q9OD1eWYVkRHlBul1BkYrzHPXqrilzrs7SMXn_nSg08WOmDx45_QkPw2xN25_AFtQGYHcbDVfbfTPa9lC8eVngXs3SQyH9D3vgGvQLTJWF55jAkO7PkinjRdwkZUh2pu-VykblquACTyhTP5khd2r-Xa85tvgOoft_alzEoIecwRKyHW-x5m5-DdTmWFAvYci28OYr1EFTOIloshI7PZWlqyhRYG5r43AelrEJmnTzfiLO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم @withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/16569" target="_blank">📅 15:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">روزنامه الاخبار خبر داد: پرواز دومین هواپیمای ایرانی به صنعا در ساعات آینده
@withyashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/16568" target="_blank">📅 14:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92eb08c456.mp4?token=pTz_kp5xZaN-RhHwj0ppJ1JwmyN34TbiFcQG99hsmzLLXPnNii3-bZIHtn2jW8sxaZzsJ-GrB_Ji7vyLcwRPMToYqK0kdaz6YqRRV0FebicOpKuXP2wUGykj5aA-qoOfQWtPFPcGcar-FLlPF3I1mP3k_F6mlHJGN3LLPSbYOL-caIU5YQ-pDq-ETHw-JiU7VANUnIli63wu3rLhLH2TzCSNwZVsEB3MCB8xHP3wNM7nWy0U5OuG7Gm2WB_N5QWOF5fOdkv9IgeNzSmvNs6uJ9baQoLu4-sf9tHp86ZS-XA2BJexJtoPkycVrdLRgaqdpdbq0d9n_AIY1hcQnxtwfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکیه در مسیر تبدیل شدن به جمهوری اسلامی تخت گاز پیش میرود
: ویدیو تعداد زیادی از مردم ترکیه در یک تجمع اعتراضی که هدف آن، وارد کردن یک ضربه به کیسه بوکس با تصویر نتانیاهو برای نشان همبستگی با ساکنان غزه  است
@withyashar</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16567" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش هایی از حمله و درگیری بسیجی ها با قالیباف در میدان آزادی
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16566" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn8Mqk31UeyNQ9iH1aaH5SKCvtBZXWmrEazfMYGDRDZBROXbKyMGNDS2O38h7eVRYGIloCz-Bfg12iEBiaDqdmlPPPx2l9j3lKNpLfnYhDePx0PIDFW1kkunrNurUrcugPZo2J9tDn5eDGMs3hcRYX_wbhMN-wQBVpJZg1ncRM2oukdXZf6Bc7K128ASPy7GFRnkCeAalhETHxcdunC26WZqb2IeTRNEjPCMNJXmKpNrTCh671_evf3ld9FDK7xesBoeOa9xvF1q4qSk-HNY4lCHLfK6Jtav1s2ufVfVGDcOp192WTqVDYcrjuQCFROe95iUBqyCA_LkKRqboTrTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=GI5mp3UlSxm8wlALRC3GR1DR2v3qolVULY0gFWJfKYL1hsn3l_EqoL5H0RPdSo5r4EUKyHn2h0qk6-cYOEkQL6TRuOZot9cSWfpXvEzCfAzT5tD59sFRt3dOPnYlVKZ7vCsZQU3DSQTKixoaSKczizkHA_K1j_9ZA4WlBe9VdNszuHUPVCBAtw-KpxJ6V6U84IUFhT8xNVIbgwgpo2FRklzmMDVOvwpcoTozqd4t_cC92ZcB1syDeEUbWjjH1ddVHMXfBku88YI8XauQMonbqCv86N1swqBm6Nb7V60tMyY3mOkLJkE7gJDSP1V3CDVydpoGwSworEyGo6MRoOKuwDLfQ9BBTzYgOjkHcP_D3N5PkyitvJwzMVjWAIHmj3YglmvT6WFhHbAnmhFpy3OWbSHNQ12Zm6Hae0t-hicCotdJnn7trPFw27awLMTdNsXGbWKg7yWUclyZjjCv78h7QW-gjN-0Ekc3d1t-IRWUq7rS0ApwyPx4QZ3WT8g3uQqfxaDg7VbKkEespY1Nh-MWFxonvUZOxErwx27cX3odYq8N3fwL-iqz5uhwPJX4tYQwOoT00I1367XEnfByhBvXaLmThTlkbSCInSoX3tcu8dLiYlYi2jFCkHf1P8Ptsh6jx0A6ZhoH5oWYY-5UEwESDX9n3t-AzMblbiRWX8CU3vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5278196c6e.mp4?token=GI5mp3UlSxm8wlALRC3GR1DR2v3qolVULY0gFWJfKYL1hsn3l_EqoL5H0RPdSo5r4EUKyHn2h0qk6-cYOEkQL6TRuOZot9cSWfpXvEzCfAzT5tD59sFRt3dOPnYlVKZ7vCsZQU3DSQTKixoaSKczizkHA_K1j_9ZA4WlBe9VdNszuHUPVCBAtw-KpxJ6V6U84IUFhT8xNVIbgwgpo2FRklzmMDVOvwpcoTozqd4t_cC92ZcB1syDeEUbWjjH1ddVHMXfBku88YI8XauQMonbqCv86N1swqBm6Nb7V60tMyY3mOkLJkE7gJDSP1V3CDVydpoGwSworEyGo6MRoOKuwDLfQ9BBTzYgOjkHcP_D3N5PkyitvJwzMVjWAIHmj3YglmvT6WFhHbAnmhFpy3OWbSHNQ12Zm6Hae0t-hicCotdJnn7trPFw27awLMTdNsXGbWKg7yWUclyZjjCv78h7QW-gjN-0Ekc3d1t-IRWUq7rS0ApwyPx4QZ3WT8g3uQqfxaDg7VbKkEespY1Nh-MWFxonvUZOxErwx27cX3odYq8N3fwL-iqz5uhwPJX4tYQwOoT00I1367XEnfByhBvXaLmThTlkbSCInSoX3tcu8dLiYlYi2jFCkHf1P8Ptsh6jx0A6ZhoH5oWYY-5UEwESDX9n3t-AzMblbiRWX8CU3vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخی رسانه های رژیم از حضور جمعیت ۱۵ الی ۲۰ میلیونی در مراسم تشییع صحبت میکنن ولی اگه مراسم حج امسال در عربستان که فقط ۱ میلیون ۷۰۰ هزار نفر توش شرکت کرده بودن رو نگاه کنیم میبینم جمعیت چند میلیونی خیلی خیلی بیشتر تر از چیزیه که فکر میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16564" target="_blank">📅 14:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پاکستان آبزرور : احتمالم میرود برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) شروع شود
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/16563" target="_blank">📅 14:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">توافق اوپک پلاس برای افزایش محدود تولید همزمان با بازگشت قیمت نفت به سطح قبل از جنگ
هفت کشور عضو ائتلاف اوپک پلاس توافق کردند تولید مجموع نفت خود را در ماه اوت به طور محدود و روزانه ۱۸۸ هزار بشکه افزایش دهند، همزمان که قیمت نفت خام به سطح پیش از جنگ ایران سقوط کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/16562" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwTgwufaQorpe-1rThnWNhZCAWryf-5kwPYJx2lcYuaXOtX3X99Sen4ssJpsLNWZrkWgyhRiFJc9w0FU7ZfVtSzkpq1YslBLw7dMYty2mg_Ecu7fodzYW4Jg5rCQXk3yF6jvcmE8E8Dm8GdjIgvU4NIvbpyqVzjterQEkMbAnG0m9fkBry-txaRhy8jEc5HJrbcHF8GCHTwSApa6ceMZ0iemlO2IA52VBeqfthm9-fRmD1HjHbwE9YVcyMdNya55E2PmdCDa1t1AAA7yBCxW_EmM8pGWDQA0TmAlBlPyk0RuUsAXvNVtE6rrAc946S-RyMrTEA8HnobgEC2FWAHtlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی همچنان با مشکل فروش نفت روبه رو است
@withyashar
طبق این گزارش ایران ۵۸ میلیون بشکه نفت روی دریا دارد که ۹۰ درصدش رو هنوز نتوانسته بفروشد
از دلایل مهم این موضوع کاهش واردات چین است. از دیگر دلایل هند نفت ایران را یا روسیه جایگزین کرده است
اروپا هم در شرایط فعلی باتوجه به نگرانی از فعال شدن مجدد تحریم‌های نفتی از خرید نفت ایران خودداری می‌کند</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16561" target="_blank">📅 13:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کره‌ جنوبی:ایران برای مراسم وداع با رهبرش از ما دعوت کرد ولی زمانی که میخواستیم هیئتی برای مراسم بفرستیم به ما پیام داد و دعوتشو پس گرفت و اعلام کرد حق حضور تو مراسمو نداریم
@withyashar</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/withyashar/16560" target="_blank">📅 13:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCHIs-mJzz6MhqA7khm29fgDFteo2nLWI6F0GMOu8UaBLj8c17zwepDoqT6q7klBjyZbMecCWFhMuLZEbSgsmKOs-SulDPXfHYD-YnW9N1zuk0Gs4MRccFNM_YeC8REPMbIB0WHaX1KfaNtMYPQov6fdon5gfAzuIGSsZebWOgco_bNggNe5KzIx3HsriYg8lG8tR88zuJgXyfH5xl2B5hfNDcK5iAuXRxJ7iKuaJr_58QbKPSrnzAwQ5AYHKJRVWGOIquObSxDYy5-otyltMDk8FloG9AE2DH4gCAvpGkGXIt1m60odWJL4jPifwKP0IZiY-5e0G7C82j--LfpU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور میم معروف این روزها در مراسم
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/16559" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است. @withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/16558" target="_blank">📅 13:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دفتر رسانه‌ای دولتی غزه(تحت مدیریت و کنترل حماس): تمامی آمادگی‌ها و ترتیبات قانونی برای فرآیند تحویل و تسلیم سیستم دولتی، انجام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/16557" target="_blank">📅 13:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyS4o7qKc4ylwLjniCk2y1CqoQQqNkap_SI-pdwCdqNyeAysYXRtT_dkEJyEq39KKbk0lO0WpKQMdmzTIKrlOhPYSRsoRtAMB_J2R5EFN8Ee1ivimSgXlFaKfPJ6Hmks4devIjN8jcEUTA-P-1MNxZUY9E32zclV6BdagikTliS20b0_ujpm6oYa7R6HYYTkm0IWB0bTC1nsWrXOYVl8azIuMh8lD8zrR77bJbOZT5w9fBTQAQLxxPnRdzT01rkDlcChVJn1wZeI4JvBKQIMAbkWi1S-7xiCbGN0cnWjxgUc7eLAY3jy3y_Mlc6NT9cT6ng1mb4sBywRZAkPOrP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حمله پهپادی هدفمند اسرائیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/16556" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=oD-wJLk0WpuYLIBoBvkAlLGHnoR9X-qbNR0GI9vmE5V2_LEVYg8N0jX7CgLD4mC784sk6rrmXwRszMIFQ2DToHxKubkeRQQm7x5nkx39zk-nv41BOWZYSN5OY449NwzZIQEwmUR-xzbD8qwW5hgf2JhTBeMKnOO-Lg953OOrTxsLR7Fsmgh5ifOOggIx_GCi3ZUGlnoEq_7BwJ5GYlkH_k-JOGGepaMPaJMSVccTPox0RmyaHWBQBJaFAlt_RUW0fVWlmxADWQia_CNFt_Glm5ksiEdvwmuHSGGp6Qg1l8cpBpxs9bHcJqaw6JPAVmwASAcY9-wJsKaqP-75oueCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bbec746d.mp4?token=oD-wJLk0WpuYLIBoBvkAlLGHnoR9X-qbNR0GI9vmE5V2_LEVYg8N0jX7CgLD4mC784sk6rrmXwRszMIFQ2DToHxKubkeRQQm7x5nkx39zk-nv41BOWZYSN5OY449NwzZIQEwmUR-xzbD8qwW5hgf2JhTBeMKnOO-Lg953OOrTxsLR7Fsmgh5ifOOggIx_GCi3ZUGlnoEq_7BwJ5GYlkH_k-JOGGepaMPaJMSVccTPox0RmyaHWBQBJaFAlt_RUW0fVWlmxADWQia_CNFt_Glm5ksiEdvwmuHSGGp6Qg1l8cpBpxs9bHcJqaw6JPAVmwASAcY9-wJsKaqP-75oueCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر ماهواره‌ای انبار مهمات پایگاه هشتم شکاری اصفهان که توسط BBC منتشر شده است، انهدام کامل ۴۶ انبار مهمات و سازه این پایگاه را نشان می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/16555" target="_blank">📅 13:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خبرگزاری مهر: پزشکیان، قالیباف و فرزند رهبر انقلاب فردا در مراسم تشییع عراق شرکت می‌کنند
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16554" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کاتز وزیر جنگ اسرائیل:
خامنه‌ای که مراسم تشییع جنازه‌اش اکنون درحال برگزاری است توسط ما کشته شده زیرا او طرحی را با هدف نابودی اسرائیل آغاز و رهبری کرده ، اگر رهبر جدید هم از عاقبت پدر خود عبرت نگیرد به سرنوشت آن دچار خواهد شد
﻿﻿﻿﻿
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/16553" target="_blank">📅 13:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=hLBUiSnb6-yEGqjt_0mu_O3TLHDSyVFs9LJNh_meCDqDRzrZDA5iOiJLCmbdgIFhvDCYT8qGpQp2iJPwPzeu3MIlFRi0NPgF--AJwaPncgS8tafzF-f-9o4T12Srm51EwwQOxt2DMQstrg_ehaK0jlUVyAE7LNxPkhYauYLr2owfuZPXcbhexPUjTkZijSjyc01MncpyKsk5rS6eilDMVlA2qLPuhzRXVB92GNdi88JrwqC4Ujr9yWf2bdT143wbCX8_gkYvYvNKOUuGa4-39pXv4Oe81viYhmaF_mfk2r5hIsGsR2Yohkyg8SjoxqWThnsDvm5xr7LKCgVsmawcZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0de6a03c0.mp4?token=hLBUiSnb6-yEGqjt_0mu_O3TLHDSyVFs9LJNh_meCDqDRzrZDA5iOiJLCmbdgIFhvDCYT8qGpQp2iJPwPzeu3MIlFRi0NPgF--AJwaPncgS8tafzF-f-9o4T12Srm51EwwQOxt2DMQstrg_ehaK0jlUVyAE7LNxPkhYauYLr2owfuZPXcbhexPUjTkZijSjyc01MncpyKsk5rS6eilDMVlA2qLPuhzRXVB92GNdi88JrwqC4Ujr9yWf2bdT143wbCX8_gkYvYvNKOUuGa4-39pXv4Oe81viYhmaF_mfk2r5hIsGsR2Yohkyg8SjoxqWThnsDvm5xr7LKCgVsmawcZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با شما : یاشار جان سلام امروز تو مصلی بعد از پایان نماز ، بلندگو ورود مجتبی رو اعلام کرد اما بلافاصله هم صدای مجری قطع شد و بلافاصله آنتن ها برای مدتی قطع شد... @withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/16552" target="_blank">📅 12:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDKx_SeC9SXBL8Q6gLwG2B6XSVNB-m2-TDe1piGZZNSkTlzbZAOWEYNlJ5VkvIBd1plRo88VWmRLkyKemrpNTZsOpHexd6EjyHbMIeDIXkQdO1TlnGgEgHydVtgoQcIzbRe_B8oCnBdFO0I_sD93DI3THYp0klB_nkzfO8JHLK_KIuotLqyQZ2BLNZg0fJ2NpaEhvWOzw5ChAlC3Q69Hb9-puwzRo0ROC1pYB5ckQakYOi_d3q3Dem_TIlTQJxAeuvjLMKFqEO8vSkbL0Zx1rJyCSrSa7Y0t0OWJGeW2wApJHZjoFJS_YbrX2SgEvT-Q0mXqbRTsBa0G0o2waHhwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به حملات خود در جنوب لبنان ادامه می‌دهد.
انفجاری در پی فعالیت ارتش اسرائیل در منطقه بنت جبیل رخ داده است.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16551" target="_blank">📅 12:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/061472f621.mp4?token=QvMKHz4WXLao_nGgRTDhuXQA3ta0jpn-HHouAlM5zWAOW4Jkdu_pAYgKnvz-di45OamFpSZCJC_wvtMoUHCUh2aieY1fcCbzyW3qSqge5T7yR9TuDjDBeJb_ZZurfiI0dAUctUNtSM5emw-9cdBkijLg0ooY1IktoiNrkSHfnGI8LSmBMGuRVTPMYTtrDt7rq697fNYi4VETmNIQX4cxVWlesGEtDujb08t9bZHY4SlgTxKBm6bVcQzjk98YAn6eMx8Rq5Ox15rNqLpbSNm7H6GXduITPjrHbdetOkT5z8U39w87tNRE-WWRIxCX_nVZDvxkVcCy4BVbANMW3zkuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/061472f621.mp4?token=QvMKHz4WXLao_nGgRTDhuXQA3ta0jpn-HHouAlM5zWAOW4Jkdu_pAYgKnvz-di45OamFpSZCJC_wvtMoUHCUh2aieY1fcCbzyW3qSqge5T7yR9TuDjDBeJb_ZZurfiI0dAUctUNtSM5emw-9cdBkijLg0ooY1IktoiNrkSHfnGI8LSmBMGuRVTPMYTtrDt7rq697fNYi4VETmNIQX4cxVWlesGEtDujb08t9bZHY4SlgTxKBm6bVcQzjk98YAn6eMx8Rq5Ox15rNqLpbSNm7H6GXduITPjrHbdetOkT5z8U39w87tNRE-WWRIxCX_nVZDvxkVcCy4BVbANMW3zkuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور دایناسور جنتی
@withyashar
انگار دارن به ۱۸ چرخ فرمون میدن
😂</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/16550" target="_blank">📅 12:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=GVMr9EfI_9D7b6sxi3MpPi50Pys0Y9zE6inJRkxermCc1IDFUlW4Q0czIo_tgxskeg42wNdNrgAM4zYVj647Bh4U3sr7xnYm90BP-VeFd3_AyqT8z_0306qqz8xhQqmOxheajseiu4FIZ4DucxU9z-Cun4tW_Sv4Hlq8aa-IgE9HfXKM7Jb-8pPKO1vzeU3lRGawA4051-y4QPdPkV2NM2L7869QAaVqMOPdY2GzApQUlDWS-88A6gbjOTKhpAc0PQQSrVZI0yAS3s8uoQVkYrvrrs9qWQU4O02hVDye7z3M0KfoNjiDKoPaETj02F0EJQ9bzySvpJ8BhJALtxIzDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ab53f55a.mp4?token=GVMr9EfI_9D7b6sxi3MpPi50Pys0Y9zE6inJRkxermCc1IDFUlW4Q0czIo_tgxskeg42wNdNrgAM4zYVj647Bh4U3sr7xnYm90BP-VeFd3_AyqT8z_0306qqz8xhQqmOxheajseiu4FIZ4DucxU9z-Cun4tW_Sv4Hlq8aa-IgE9HfXKM7Jb-8pPKO1vzeU3lRGawA4051-y4QPdPkV2NM2L7869QAaVqMOPdY2GzApQUlDWS-88A6gbjOTKhpAc0PQQSrVZI0yAS3s8uoQVkYrvrrs9qWQU4O02hVDye7z3M0KfoNjiDKoPaETj02F0EJQ9bzySvpJ8BhJALtxIzDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدیو از احمدی نژاد
@withyashar
یاشار: من چیکار کنم کاپشن پوشیده ! روانی ها
🤦🏻‍♂️
😂</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16549" target="_blank">📅 11:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=NOszab7VBcCxn_VhvvFsEojufX1D9rFiUWJP34iHnhE1HYlZXun-C96v4pfng3RH1W55EaI3lhtHz2Ge19bsztvMNbOSzqc6hlQvE0jqRIU2RRnN9Gnv4RkKtKqv0__cyLMaxy1ozH3c5Gci2pCXMIEsQZEDle9-Myrp8ZVbBGdXWn-Lt7ByoDgbv-RLQaN1SqxqyCVc86hJyoBxyqBZ3s74spTOvpdZV5LHYUjUY2zFr_BbepgqcNsYtq5pYdBlJHfrfu0hX4w9Pas5d_1H0T_wbBLeNNnFWryJQsNGsxqo4c9T1eKPEO5IfLO1Y66irzAHpnD5JXDxIR0jyjDYHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c911eae2a5.mp4?token=NOszab7VBcCxn_VhvvFsEojufX1D9rFiUWJP34iHnhE1HYlZXun-C96v4pfng3RH1W55EaI3lhtHz2Ge19bsztvMNbOSzqc6hlQvE0jqRIU2RRnN9Gnv4RkKtKqv0__cyLMaxy1ozH3c5Gci2pCXMIEsQZEDle9-Myrp8ZVbBGdXWn-Lt7ByoDgbv-RLQaN1SqxqyCVc86hJyoBxyqBZ3s74spTOvpdZV5LHYUjUY2zFr_BbepgqcNsYtq5pYdBlJHfrfu0hX4w9Pas5d_1H0T_wbBLeNNnFWryJQsNGsxqo4c9T1eKPEO5IfLO1Y66irzAHpnD5JXDxIR0jyjDYHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودرو ضریحی عظما
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/16548" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=KA0w_Jj88miQAz3ZFXM0HzcQGiZlTfrNZH-KwT35UUq-IzitkNCZ-fDPB8C2_ut3t5rWyKJP2onM__mmNuT-3kVHcNj_Bvx0FN0j65RynBrnAzAY38oIBHiyCZOvtvI0CZ-poiJtlOoL9UxCqbV8qdVnTK4e80kxkvV6Y8OrjWu1xpVJvduE2kmEqtg2vMI2aJReAKRERndsOxJ2wkrv1vSdjZ2z_iDzP2XaI-edpplsm3KIBxWXnBCMGzMg2lveVzawuUZ10Vcb31XzuBhuLoz_P4W0zKcVpptJzSCrfWRVAz1v4axVwSc_ncPGpFy1TihZr9RMyDluUc4OvAyZPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbc5efdc9.mp4?token=KA0w_Jj88miQAz3ZFXM0HzcQGiZlTfrNZH-KwT35UUq-IzitkNCZ-fDPB8C2_ut3t5rWyKJP2onM__mmNuT-3kVHcNj_Bvx0FN0j65RynBrnAzAY38oIBHiyCZOvtvI0CZ-poiJtlOoL9UxCqbV8qdVnTK4e80kxkvV6Y8OrjWu1xpVJvduE2kmEqtg2vMI2aJReAKRERndsOxJ2wkrv1vSdjZ2z_iDzP2XaI-edpplsm3KIBxWXnBCMGzMg2lveVzawuUZ10Vcb31XzuBhuLoz_P4W0zKcVpptJzSCrfWRVAz1v4axVwSc_ncPGpFy1TihZr9RMyDluUc4OvAyZPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورود وحیدی‌ با موتور
😂
@withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16547" target="_blank">📅 11:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الاخبار لبنان: یمن در حال بررسی بستن تنگه باب‌المندب به روی کشتی‌های سعودی جهت فشار به این کشور است
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/16546" target="_blank">📅 10:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyl7FCyih-D0pat2rMg5Ggcg0Xm3ptysHI-wG7oGvevaTHVnJhpJRG3OnNdPAvxkfX44AJTlwBYTC3YkfPeeDKocCtrCd92YvyHHT30w0qEa5ktpLrm8_RRBqgkHVTzx4xk3EzskBN0iXIZHsleh87GjJ8Fw99lhgx4b-rLKcBBc-IRkCtmqSQB5tFHeG3CqkyPS-ly77kllk3OkmamQ70Z-A4GTtNrw91nwnQKim4wkQW2AaMcfG1u2X5ZfOBQu1JCDb81O2aN12XwfzL12DhM22H-JVX7NCrIEw8TKN2q02ZCi2XB2MZr0ZwOvOzenZPD5k5R7mVKAp5zhokQyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار گزارش‌هایی مبنی بر اینکه اسرائیل و آمریکا قصد داشتند او را در طول جنگ، به قدرت اول ایران برسانند : محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، در مراسم تشییع جنازه علی خامنه‌ای شرکت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16545" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1qjeBc-aZ5z_N_1JBGtMqWe3AyH7pljGMDZKjNY4ylWgXnC4lLHRE59C81Hp254bwLI5ff9vcgg4duOVfYa1ecIPS-400A1ZNYC63yp6h6MLTtYoUKYYtYFKcCdAlrmghdGPDo1XGLvzGlhHyGhUjL0VASGgOOasEQjwGpy-qq2bLFdlWeQaNTQwBJm09b_Y69lmlzApS34KwKrJYn4brnCPwi_qOpnbbtGoBd0b7ej-tpM_zl7cK2gsg2Hr3ydOrN62qgFINvDGKZaB1tOuS8mlRPP8jkmv6DWdKF9xiydQ7cB_zhsrAogF12vct3e_umyJ3Ml03PmCoKBTDjnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO7cU6FpSEFRyn9FTqewavrVAjjH782q-abPnbBAgTldpc9I_9ZhlzNI9hjJLUB-w_s0Ben42SItd48xuVZvRdrGjC1fA7KAPKK72Vi_2MmMzlvtu5WTh5jKqpBqfQ6MXPyBhfdG6eUJlxxbnyyWEXl8_T7pncvAB3a0B9iCnDtnrurgqlGxmwjASPTjk55AwG2Ck0x8BYTIiF7J2v_gkkvhF_pqh_4Z5sbyN2yFAoYtGecAOH2A2bgXhA14s7WgmgL6wqmEhQYCuPyr-eSCUCAhsNeCFyGVME9cS9s6UpE-h5lK7u5MJGM8WQKXlBDQGPgGjvqCA7NxZW_fRA7R-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمایش قدرت در برابر اردوغان: ارتش اسرائیل در تمرین مشترک با ارتش یونان.
در طول این تمرین، هواپیمای تانکر اسرائیلی در حال سوخت‌رسانی به هواپیمای F16 یونانی بر فراز دریای اژه فیلم‌برداری شد. ارتش اسرائیل گفت : "این همکاری بخشی از یک برنامه استراتژیک گسترده است، در دوره‌ای که ترکیه تلاش می‌کند قدرت بازدارندگی خود را تقویت کند."
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/16543" target="_blank">📅 10:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این آخرین تلاشمه …
@withyashar
⚠️
یاشار : عرزشی ها اومدن ریکشن فیک زدن رو این پست ، اتفاقاً این کار ارزش این ویدیو رو بیشتر می‌کنه و نشون میده چقدر سوختن</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/withyashar/16542" target="_blank">📅 02:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqXXnWTMNO4z4Y_Ha7t8l6ywCEttkoOoC4yODRidEVNmnVzhtOBdT2ebCm7vvmP07SZ6bTALi717wdDsuwdeWIjg1rVwCH2CASZtnBOpNi0erp9w_HwmwnQRgEvetxu0gXQrteMiKbRygzHgvRPoBlrIYhpywE3G49A95bvAQEriV6hIDXErFyasBP5o3lyLxEM7bZShS1Ghoz6wlaweEzSpYKxVEP4UkbsEpaDpagmqYp37NFOg6SUruya2EVK0Q-5y2vxdlz8X84Du8UZh0K_6lSfirdJ9eHr0helBWdcM9fRAGMSmVclxQtW5o28RZNUMn0eYizkrbtfDE50zxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواری شبانه روزی نیرو هوایی آمریکا در‌ تکیه تنگه هرمز در غم عظما
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16541" target="_blank">📅 01:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXhMiW9yrv4RZ44auRdNHLRyb0THjH6HaepQvsGekIceV1-5t9RuJ7WHX_bkQ0J4SOso9shJDFxEg92duKVdESvjOLRtYlWlCWKZDw5N1k7AH_FREGgEgmPFHX2-5pWYPQfF1Nr7lsUu8U7i1AdeHkKLGrYEwNm40GaS9apOu-5jK0VO7Jz3n--iSB6k-UjHHWfN1JmNCIt4XdcS0dkQNLriFOCUt7jnHxCftrrUGOm8q2iddVX7nBB9TkbXfjudfAj8mSr7BvhjKIg9HthnudkBQw9h1hOA9g_iaHpWANWvl1WmEbD4iHqxrKUCzAtssnTF9f72uaQX7qOST4RTnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفلی جدید
😁
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16540" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش ها از آغاز درگیری شدید میان حوثی ها و ارتش یمن تحت حمایت عربستان در جنوب یمن،ده ها کشته از هر دو طرف تا کنون مخابره شده است.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16538" target="_blank">📅 01:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEIuZCQpYWdFOsjco5C9tEEioCY8oPIf2FJkX4KCwH29lgG-gzPryHDIi_3wgnOUM6_fV9VhLkn9x_vckbAcCAEbGmyiHc-RjZhlNkzlrHqMpb4O9sonlVyVCPxtriBhKN0wmRQH8rnH2jXlPIinaIp-BF52Efd05aGyD7VCw3WEJLgg1h80zohkucp9yxt11PH53oO_-ZLX_WIjA-aeXvjgTDK_AtcSsa4Z-NjNHo70JPMTl9m0Jcigk9VKqddF6U-7tnEF8bKolCT9ys_ejUUVa75RQ2wCcZOZHaF37RdSFnUF0KpkyLkWpxrOhtmU9C-O-37iazodAwxgjmb72A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پستی از خانواده خودش در سال ۱۹۱۵ (۱۲۹۴) منتشر کرد و نوشت : پدرم، پدربزرگ و مادربزرگم، عمو و عمه‌ام!
@withyashar
یاشار : میخواد بگه ما از قدیم پولدار و با اصل و نسب هستیم</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16537" target="_blank">📅 00:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afjbCzW4JWJsplaUWmqXZLHY9rplI0GoNA4K142FWNQsKlrwgWMp03BcOQnZmrEJpDNHoLXCMQypWblzNbvj9-1lhj9fUVzl0sEHmCnqMuFcMoF7Lm68Ww_CCtAoXet1i5LrspeioF9W279r-L1peqxv9Rlv8y2hrruG89VczBPDjCj2_adMUt731DQHiNM_3yeg4o-QeAgVKaoGM_I6KlAMtXWyH758xphSg4fnCHXBxjKdr6oYsnnDZQwe-FEGpXFWuGjivXo-Epz0b9Gh-lq1jYgBp_0J7K5fKwJ0q4ZUIubEh3KJFBd2sFZAMaBhxhHGjGllKXPwhTDC4FG54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهیه غذای «هانی» اسپانسر تشیع موشلی , دسر هم حتما با «میهن» بوده!
@withyashar</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/16536" target="_blank">📅 00:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcAtx8Psw6UzIdYi6wjrShMzZSmY29EzBCFKQilZAa2WnOt_-qPcuElYi6P9JSYWAG9XRaaGUgV1H2MYTwOF7yShGMh3KFOHvEmhckRsZV80JTMLCtBdUDqRC3Vz9bFL-8i6oLd9cTO0lfz_3Ffqoe__EcGm9pu62ANB1mN-PUMj5UTZWr2O1f0FPWxDo2uLV89oOstS0Z_hfHGEs7lkhdeIIEIkWpoWWK2We8G-ZkockgOPiU-GKJ7ulHTLwpy7NaEVBvHnaPqb66vNMa7qa_F14EHLUSMGdN_9v0Y4k7vP5SOs5AalACiUgV7FJTdrAe-zgNG4hKIPsyUPQtravQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پستانداران انقلاب اسلامی
وضعیت بدنی نیروهای محافظتی امروز در مصلای تهران
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16535" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در پی گزارش‌های منتشر شده از عربستان سعودی، منابعی در نوار غزه که از جزئیات ماجرا اطلاع دارند، به کانال۱۲ تأیید می‌کنند: حماس احتمالاً فردا اعلام خواهد کرد که کمیته‌های اضطراری دولتی منحل شده و یک جانشین برای مدیریت این کمیته منصوب خواهد شد. این موضوع تا زمانی که کمیته متخصصان وارد نوار غزه شود و اختیارات مربوط به اداره ادارات دولتی را به دست گیرد، ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16534" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند @withyashar</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/16533" target="_blank">📅 00:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uoy-MBoThgGZ8fE2GIvowgjeIlADdUBWnAVpzXZDMmTl3wnlgkWazpGYFfpKFknHlZiE-Tl7NGTOLcdEmJOn6g5ycTXCcO677t073UgW82yMkHMUyatN7ejz2zbXNAdJapw4E9pVeoB_4B8ZYe9ifuYup9R6aWLCNvaGdPbpuftonGwViJEw-KRauUh0rL5ADyjfI4KZFZrq3CA5TysBWPdfr2wTsqVzOTUU4joVcL9NS6yvQm_NCy4RsXOXGasQED4g_qg71weaRqWe_GBd9qof6_W9k4oj1Vpxf0eN1gMgaqHRVGP_lZnylznoyAB4DPTiz5vfi1hlvprwqX9CXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از حدود ۲۴ تا ۳۳ هزار سال از انقراض آخرین نئاندرتال‌‌هایی که در منطقهٔ جبل الطارق دوام آوردند ، امروز یک نمونه در
تشیع جنازهٔ آقای موش علی دیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/16532" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9jFPWSI9je8KnnKHlNWGqJjwOoYr3auf76L1ldHmRXNyVGHH4F_ejxflmp8A0wik-gFt9oun-JDnQ2uAPXlA8zQVMTq3ct4NIS--5mfC4sk6ICYHyES7kxUW2jpch6f4EWw_A5FGKZk_0oFUtgdSYeJHUUpd6-Ze0U5Ao-FV8fQRL3T-c0fPVTowNngJE52a-GSn7UbotQqNRZS1J-vtukTuLKbjbOjcouKDMKhnGuf760JWDlJoiL2dh8ZTWo6aDj0V2WWTCQdNmM7_u7efVQqaAvnzUTzCMlxrLWGDD6CXgHOJNaiFL5PYlB7pKPXO5DG1wqpZOPwDzt-Y3l3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/16531" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJefl9RroxoQ_ZEUg9ToF_XQhO0MkDWKO7pkM_y9NgVxpJ75Oazw_htevDksnkiGn3awan5y18mw9dgaZkc7I-yB8wGbD1YYhUeCW-JnzA-0LaaCe1efFugATHfXWnf5LbRBNPbngBNsVBM6fi43Iz6iOa8hXbtJssxBHsl3fRRGSuUwzO-fqXfp0VBq76YQ7CvZ8VgISeqnEEHSvmztBlv7s97ajmqF_Lf4B2B_6lHKurY62vEpNfytxNE0DKUre7XNhl1F3sBF_ObswKmq_GnmZwk79ma82bWnZbdltEQOCVV3sVGcpJFUrI59_bpP8UP2EBgDwjOwIRZzEF-a7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت هواپیمایی سعودی اعلام کرد که هواپیماهای بوئینگ 777-200ER از رده خارج شده خود را مستقیماً به ایران نفروخته است.
‏این شرکت در بیانیه‌ای توضیح داده که این هواپیماها در تاریخ ٧ ژوئن ٢٠٢٣ به شرکتی واسطه خارج از عربستان سعودی فروخته شده‌اند. پس از اتمام این معامله این شرکت دیگر هیچ ارتباط عملیاتی یا تجاری با این هواپیماها ندارد و برایشان اهمیتی هم ندارد آن واسطه این هواپیماهارا به که فروخته‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16529" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV8P5aM41h4J0KiU2xZN9b4BijDceQB4yt0oGPSj6xqnh84cyrQBoX2mWBZJvmZgASDV1VvJsy6CJTyhWEIFD8l-6fYAAns_3_VbYu1FGy6rx7gV1qiOQypTrCRFVYcU2Yl4OO32Y4BRmqhxQeFxIzfUeaTD_Rjcbxwk2hOJTUTHPUz_YOvUCyAK1BLbFaATZdonWxN9NNkO7cBHoov9G4KJGoTyFW1gEqhfOC72q-wtzQ09SWFr2LWOW82O0aZ9erWkwnY82gqsY5Pb61wMZy7OY98e2AqEak8tCUULOGfQVQ95PqfSQZY8qwwS72DCS2jIeGLIBEdn-nvCEyIofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته مانده جمهوری اسلامی …
🗑️
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16528" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">صابرین نیوز: محمود احمدی‌نژاد، حسن روحانی، محمد خاتمی، محمدجواد ظریف و اسحاق جهانگیری در مراسم وداع رهبر شهید انقلاب شرکت نکردن
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/16527" target="_blank">📅 23:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کریستیانو رونالدو به گمانه‌زنی‌ها پیرامون آینده‌اش با تیم ملی پرتغال پایان داد و به طور واضح اعلام کرد که جام جهانی ۲۰۲۶ آخرین جام جهانی او خواهد بود. این بازیکن ۴۱ ساله فوتبال در کنفرانس مطبوعاتی پیش از این مسابقات گفت که قصد شرکت در جام جهانی بعدی را ندارد، اما تأکید کرد که هنوز قصد بازنشستگی از فوتبال را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16526" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یک مقام ارشد کاخ سفید گفت که دونالد ترامپ، رئیس جمهور آمریکا، در دیدارهای خود با رهبران در اجلاس ناتو در ترکیه، موضوع حفاظت از ترافیک دریایی در تنگه هرمز را مطرح خواهد کرد و خاطرنشان کرد که متحدان پیش از این تمایل خود را برای شرکت در این تلاش ابراز کرده‌اند. با این حال، وی گفت که بسیاری از آنها کشتی‌ها یا منابع لازم برای مشارکت در یک تلاش دریایی قابل توجه را ندارند. وی افزود که واشنگتن همچنان به متحدان خود فشار می‌آورد تا قابلیت‌های خود را تقویت کرده و در دفاع از خود سرمایه‌گذاری بیشتری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/16525" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام کیان ملی در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16524" target="_blank">📅 21:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=ARqkXwFBoa8HYctsm5Isk8pBfP7V6WvevGubIn21iPQK_oupt3A4IERvUlNFnvbQl3MNvj5zO6yVLHLhyc7rjWzGam-oX5XNFgIubnBgDyjLRiVK3n4c_2Jnj1wON4ysd0tZFGhLlm4QSfosQOlVS-OO8pFdRcy-Tmu7ZNP1KU0042YfoI80SMPGKFv5cO-0Oa8QgW0ZdqK59Kya7CblN4skKzaxEX2sggctnOIrk58HIEX4NHXCL_ANl3mkwDNe6oI7KNpnrizHvd5h_AytEKQTC9M_stJZdYdi1xV0_sjyvI0i2ZbaicLvGAMeDqTqyBeDP2WSevD7Sz2lH0pefYvfV96lmOz8Z5_KpasN2lxxPcghhpPCsO9Q6YtxbvFz93q1UvvlcsECsecjaNjxUUhkRuuX5ntxQRyPnqn2aBtUgsjtVUiqy-dka_NqT8b2mZTGFLwGJ4TADPE0whdw-dm5v-TSO80Q41-nvA3sT26qxdOB_x_h2q4I7RGUjc0-6erGABGj24O9pYkGQXqLk1Wz7U9bhpcBtqpjblCrdQILrcB-eMlpqLRlzsp0hAsFiXowE1BQWsil0rgRL9b-KxgSwAdtF1KYEwrYY5bBYa7Q8Une9jkQMPugDrXqFZdhDozrtRZvFcvDPko1i79ej5MUOwqfQ95JYpXiUv04lkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ca634efc.mp4?token=ARqkXwFBoa8HYctsm5Isk8pBfP7V6WvevGubIn21iPQK_oupt3A4IERvUlNFnvbQl3MNvj5zO6yVLHLhyc7rjWzGam-oX5XNFgIubnBgDyjLRiVK3n4c_2Jnj1wON4ysd0tZFGhLlm4QSfosQOlVS-OO8pFdRcy-Tmu7ZNP1KU0042YfoI80SMPGKFv5cO-0Oa8QgW0ZdqK59Kya7CblN4skKzaxEX2sggctnOIrk58HIEX4NHXCL_ANl3mkwDNe6oI7KNpnrizHvd5h_AytEKQTC9M_stJZdYdi1xV0_sjyvI0i2ZbaicLvGAMeDqTqyBeDP2WSevD7Sz2lH0pefYvfV96lmOz8Z5_KpasN2lxxPcghhpPCsO9Q6YtxbvFz93q1UvvlcsECsecjaNjxUUhkRuuX5ntxQRyPnqn2aBtUgsjtVUiqy-dka_NqT8b2mZTGFLwGJ4TADPE0whdw-dm5v-TSO80Q41-nvA3sT26qxdOB_x_h2q4I7RGUjc0-6erGABGj24O9pYkGQXqLk1Wz7U9bhpcBtqpjblCrdQILrcB-eMlpqLRlzsp0hAsFiXowE1BQWsil0rgRL9b-KxgSwAdtF1KYEwrYY5bBYa7Q8Une9jkQMPugDrXqFZdhDozrtRZvFcvDPko1i79ej5MUOwqfQ95JYpXiUv04lkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو توی بازی ماینکرفت از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین @withyashar
😂</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16523" target="_blank">📅 21:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚠️
ادمین کانال تلگرامی به نام
کیان ملی
در تاریخ ۵ خرداد(۲۶ می) دستگیر شد و  از تاریخ ۱۷ خرداد(۷ ژوئن) این چنل توسط افراد اطلاعات سپاه کنترل میشود و مطالبی ضد انقلاب شیر و خورشید منتشر میکند. به هیچ وجه به این چنل دایرکتی نفرستید و از آن خارج شوید.
⚠️
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16521" target="_blank">📅 21:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم! @withyadhar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/16520" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJL3u_JpEdQSues4ZnbXX2m6en0TXamJMZXq_z6M16Ac4oqiBhsXRE0awrQgqCq6K0SvXX3zxmDqj_yp6oB47azCtWmRNZa2dUeQxCEbxL2F11SXmNah4exJByxOK9ZUmacahVGlA7oZ1LTgKLAPwsqZ-zDq_vh5xoNpOe6Mv7SlL2b3BF7MnJ5CgXoSb98UO_fEmggCWbGObp_thODQCnr-J1p5i9LWKnN5_8kpTTTSZaTVgWZvP3wVkeeHq-tqDTg_ew7TA7R3rON_br4Uaj7UmUk0j1inM8X5-7qpeujIrq4EYOzB6qZvIEDxWGDWW0g8n063y7_vC8tZYOaH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
@withyadhar</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/16519" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کاخ سفید : ترامپ قراره تو اجلاس ناتو با جولانی دیداری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16518" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارشهایی از مشاهده یک شیع‌ ناشناس  نورانی با سرعت بالا در‌ آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16517" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsEaNeeIu0tw9yf_3W5DPzvUzBZIPEE24KsTcQ-UScI2uZl7jVfp0pbhICx6Rw6dkeTiRlOERB-3WoIUbJZXHFWbhqGRV2o5bT8qlNmPTxpPIh15B0jbO6qiY_v36xGdefhKcYM7_hUqFwGTL_NaCeOD-cd73WbFIfymgIdEwfWiKU3rnHDMHcjqwofrJarv0tjME7ItfqsjB78PVmcY1lnmf5MnwUYAsYIPcPUnLggU9D4vvUognTmP6unhMe9B2U-M89eyxr6m7Rs6bPpI99aDtTSVg4MUBzKTNuRs-WUJeRduea0X9I9rja_bsdBU7XnS2RvQ8sN3RFtAKCxNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما : انتقام رهبر شهیدمون رو
توی بازی ماینکرفت
از آمریکا و اسرائیل بگیرین و فیلم و عکساشو برامون بفرستین
@withyashar
😂</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16516" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨
🚨
🚨
گزارش انفجار سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/16515" target="_blank">📅 19:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هرجاى اين كشور بگى نور به قبرش بباره همه ميفهمن كيو ميگى؛ هرجا هم بگى ريدم به قبرش، باز همه ميفهمن کيو ميگى.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/16514" target="_blank">📅 19:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16513">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfrNhbaqciTTi-XTDutp2YuxIA1dA50mnmauKR2AUKpBVQ6LX1FF7VkPgT_lTxpo9g5WTtpL4Rmyuo0ArMW5TXm-NLcwWUhTNyx-sW-TptIy0yD-O-KVxkicNjYCy__fR5W4QLfR2IyR7hro8zUVWBeSPoqPvrmY85FLYN6zYr4K4n_smGnrzr3yC3-0Fq1ON15fyPVU8NWfNJtBm8WHn5aot0y5NwFxnOHvDMCgzVsyMQ8nCXr4Zts3WfN8o5dQznjZjW8kXm030XNScLL7zvqED7TyQ3j0MPdk4Y4xlVskloSu0nv5FwubRKPl_JfPZYEjdRGMacnOVxtAQjeOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن امير اصلانى سال ٩٣بخاطر اين نقاشى و توهين به حضرت يونس اعدام شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/16513" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk2UteF1wsMNTnXJ4qUPU5GHAM1H4krm6Yr1jipfw2x4_44N3Udgb4YDDUXEDRELF-uAvdxXLdaslqQMhDuy3j0BYCTTBzbH6v7UyaPhFguL3TM9suwLPZtGBUbS7xaFHtyrbPpCWYyOiQLTRPAh_QA6yxIaDIdR8gb2-OO66ZTRLKtap9CLx4l2q38hv32RbEsm5E9x1FIWJyBuclMG7Dpe7H8C_PAsBcuykma7tl59mpkOoETevTSa1QHVn_9ASP6kKGt0kCVQtVmPIatFncN_Wk4YsBdLDCCDB9eVNNKNBfeCeiswe8Rd96C8hnqMoOBjYEBuN4djOFhNFPz6cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حادثه در فاصله ۳۰ مایل دریایی جنوب غربی الحدیده، یمن. یک کشتی باری، درخواست کمک ارسال کرد و اعلام کرد که مورد حمله مهاجمان مسلح ناشناس قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/16512" target="_blank">📅 19:10 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
