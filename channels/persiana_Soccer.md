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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 01:08:36</div>
<hr>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLIuunfxjuG6ukPRieIfnqzIYpVncUqPPAD55msckHLO8f-907knZycd_UWMVSuC2S-DnIkzLgxuBBQi59QVnkShUatHr63do4H-ZS_M8EOVg6bc80YtMKXhPbw3-hGcK_wzy-gVr0v4DxVdKHGyd0fz2w-iEF4XiK_IeE_l9yVb-2ponoEgMRNLnlUdjuKOpjRiz4VnPYzJg3YxNcF3mDTIV1_LAX8Z_BdLMF46m_heidGgJtKk7cuSOf5Zugx2UB8XDbg9J5k3gX76zzQZ1Ajn9t5ZrqBxx52pmjUAIl80yyeLWEE5Bm6Lk7maaXfNgFQpiVQM1OeabCm5afwLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wxWjSvo3G8glKAeIAAdEWP8A-htiAXQVUrvPS486QpjDRCbRhdMguexT1bp9HRGoGQmNFp9OzA6iQXOIwxzaJmvSRFk1OsnrviYlSD0CB9mtMHumOdK4lEhOMoEvQI7K2X2ckZ-ShZfLWZzzBsK4ViHi6KiLfwuhXuvI__ui1oAwGsVx2C3UYd5i14qgeQcl6z0SHcSQoZHzcmht9HNOO8B8ODs6uK0oPyUL3OenNMmKcN9rlPWTzjR3grn6Bn0DoQlPg9nMwpJIuaiM4djvR3B_ZpURzBFg7g3s8DLkwunJx9Qlk0D7uymtshU0Sk1VQ2VVOapb-N6SxQhGbS4Deo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t8wxWjSvo3G8glKAeIAAdEWP8A-htiAXQVUrvPS486QpjDRCbRhdMguexT1bp9HRGoGQmNFp9OzA6iQXOIwxzaJmvSRFk1OsnrviYlSD0CB9mtMHumOdK4lEhOMoEvQI7K2X2ckZ-ShZfLWZzzBsK4ViHi6KiLfwuhXuvI__ui1oAwGsVx2C3UYd5i14qgeQcl6z0SHcSQoZHzcmht9HNOO8B8ODs6uK0oPyUL3OenNMmKcN9rlPWTzjR3grn6Bn0DoQlPg9nMwpJIuaiM4djvR3B_ZpURzBFg7g3s8DLkwunJx9Qlk0D7uymtshU0Sk1VQ2VVOapb-N6SxQhGbS4Deo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ol-Wjk_y5vFzpU1A4ces-dPib-HLPV81VPYWQuRhPkLVOzsRFMQswsLodUP3dLd-O5AMj3EH1mOQmuUMXXNBwsnlxgyuYG5Sy6baZsruG4LWISIdt7hISKg1CcE_apV2BkNofsuhLTMeNnEjYlOQ1srYXQGRHjRyHQtJ9aWNn9TLXLALuWtbV8RSJgklrOQb57Dq7oseiyCLhFsA626tFo9mWqmjM3u2lfRhnLFbyTatdX2eBiYEHItem-GrwPW0VtZuwdizBVlgCIXJoDXhwbc8auufwahjJqYIvnhGIvBb8sRt-mZgSuXPIwverdSSp0V-1Prk7vbFR2ulvPWrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1Got-z9q1q3fd2Zi_UQOealoB_yIwPkPW70DZJkEgTYCiOuCzq6ad8DDrHczmgsBA5WOTzmlaQ5Cb-Yuqt0Y2XE1WkzDdvTwxdWU9B5NsZ_hWVHrS0UnZV45Bq-rn67C0KgYwOyzMHTpMGeXxQcfxw3z7_mcpHTgLN5uoowYp3ftRH-GtO035k3hjj-6izpvx2roo577MDDQZsVROJCS7zZSmPaYyfBZHrZKqWRklSEpbYB2bzmHbS9Hm7t6tIoDuWDAF07TaPvZeFcD4Qc-JsSTn6y9reC7FLKJSFfop_LIFFeBbbwu9rmtFmazWeyKzbkbzKdPhLSGeFyQnOdSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBX6P3XQ6KewSczJlS-jsyF6bEpG8m2TzqmkQYog4c5i62xKjpXy7tBvRZsihsemx9cQEttiIG5hUsXVGf1MXfKTL1aJhc2iSOI8fsx-O1T-afVbGKWEL_V51LBpqw78XKhDZcVKORFIXk9TQkFurTjA3-nbghei9eXUR0_ov2S0DDCOzM-9tHP4Py-b75n3DStIn2JwyFoGApXVPeTHlMaY1idiR6ElKCaZTNy1rsTBnSqE3AvNrJKdzhQeyQYXhxrva7k2uYu7hCxYpO6BjvBnKyblgt6Xiq4EXUFdgXIqNyExJ_IN82hH6QAkkBk0Ip3Udv4uaG9RdAjllG-Rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKhPC2kTVuKNFa5jO0OCEaIdjTqE02sZTArXVAT1S9ZCZRNzsYvwOYUTWxa4k7Uz4Me2Wwiy8RDqtshNROwup55Fi2YBnHz0L4lUfIx9yqFkl1X71Ci4CNtRJAEbWuetVjQcgUspOzQV9_dDb6X_mzBL_0qSHNW90MES0eMib5SaABihrzfJDzly-T4eSiHvC-IaAfg_jYS4wGLrNEwBUgyWFqJrXZNubtNAQ3FjuGSjI00h7KDvmEOGrdFZXq1qaeZ0N0TCbV_UAC3knjGRt98RNtZPNeUyEGAub-A3RJIEQiAqBpjgFpdGEgjZUUA87gUBjxnWk5WT6_jVXCdDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eniSSEHLNdYSVF-gF9hB-pN26jmHKmTRa0sGdcHyr4bnqH6y6aan1AmjeDcmGSlKheoh8XEK6SqoNNsxexePZRU0DKhgJ7eI__ZaswUoj2nnZaNHvPZ15Jj9qnEZmXlRNrWk9oq5nHEpoubYvDbNRuTw9m1nF6Gso_tmg67dBQva9j35GBlDjXlAn7O7C67nTcbGhll9b4R_3IagbUEc09YYGPkbJjarE04wVceLz-69k41VI6qTCqyp1-4S9nMHZS3NOQFLfsnhn3rDkRprAf9VKKU8CrkgwsuanzCblQS4X2zZbnjODxVrgU8ngQj9EhuieaY47G62pW6_z28Xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzI6gH2FyOllQAcazWbfOsqx0Xp-gqRycyCE62_LbLLOv0L2GWiRTVmGuvzgEswn8axgSIvuYsU4IZaFMgV5IwwjJCOLCf05e7PgRmHS-s8abKoNSLfOAoe-YpJ1K6WGZTQvr8NnMoCfU8gFHPibe4s-Vu5nD92IWmRicedaAbayQrFFC80tba5kxrIKTol07UknIohBSfIaRDnqTymZXi74PpJR3ncMAaj3TtECkjmtDRNuaeIBjhyB5zz8SyoRdjv8YXGP4dWNTaB6wERigu3AvFhlwulPdKbVis9C1awFiRdBAFOppjyVNffsESvpu1x-bh5nFPubPzItiYdeaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POPEdQE00uvwXeMSQ7Ki6XrKUZlG8qViZMyRQX3kW_wO2wmZYrdYhUVW-Q8cWv9AvMjtIDM_b3pqcrUW-g-0afTtv3qW4YNQwDx8sx2FOzjrC9oDlmK5ydtCCZ-pCqtlcdTSnuUZ7w7ftQWv06lATIcBADGUIjnjJDVuXfTolkbbvF2g-AUGb4S5u3uUnFCegjLYN0aatgTwE7ZVq5AKdI9dPkkiJFBqY1zX6KgS-DKHK52pyGio1mt8jRGzbNNnrI8TuQYdtyLzMLLzRcqLSVI61Yj8lCjrKhzYCx5yp4AK3KKZVrKDf1rfkWw_BGuc_GLeGLc7M8d9A3A-l0DLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqS8sRrVRy5vrVYFO8ANhfqpRkWS9p3x3-X4KV1BDmOGaESKaZkXr5edto7gGKY1VQrRfEoTM2sWVZlhXCVX7F75TiwPOn8fU7HDYOgLPbjmz0UmH6tzSiPD326MC2RILGFyGQUe4thglDrz-GLTsdRzsNfbbD7XiSghOHUiSj-u8uyzrYUmn4B5pCv5vaO1EQyQsQIpH6SghFVx4ZVL8179C83z-TfbfBveWFRI0QBHb11Vgx2AkZrm0zX6a3-S5JCFApSbxIdf3oxmiUDQkHXES75NbR4Si_6M1GIdCzmCI6TmoNicd8MWNWseepCky8idqt0JPxBSxCKyMbPTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4isEYp0s-xZLLlzq2Di7I2THPTywQ-Hb7i9wF45J4TGZOzoeVWSHWi2j3XW8Bc-f5llxw4nSbz5FKxW8gNryA2D4Dv4Et3c701QQ0ucVzmbGNqextyyPY_3V8MjWNu5enulXAPTSaEB1Vj08z0CvkvuveFphgGjoBEXUZPcKG9SYP8wL137q3EkbjbysWZjKKJi0gy_hG2KvVSntn88VHKVGaSWVDUpmXyTNYD0B3RDI7nCB9kjaw8ffGHPkr_7Bddn5E_E8PeJIdnZr78-FsvSaEN68ara5-Pc-jqJX0sApovSAhSmogRYDcuvWdX850MNjry4p3VqlxJuHnedhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDNLBSHn7CqbtP-LJH_IlkL51XrLIDj2vIldPRcc72f7Y6iRcr3nTcOrFRS_RSyN8TmTVvxhVGEXT1bpt-gluq1JRuU-mFD1DHfq7locnaiw7tS_xI3xajtbkfS8ZFbMLuDkryoAfggaqJGEZVPqqsNg_zlAnRZ6IwMJiegsDY3AMKIixAISi5P_hi1EF50OGOna4XFJnANmp2gHtWUBCtLPxrTReqExz4aVVmrReHwx-TI3yD9FTXUSEZ3DN9oDWr1PNuW2xDD1Vw1YCYfI9mkL0Nblq3S6txC81co3loGeHatqn2sRH5oxR4zBHXe-0zp2VVX_p4ZOCBk1i_yzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgakwr1s6-mQ5Y0r-t8g2SiHGm43u2XGxsxwnj9vRVAPP2E3TLPmb9ZwzzrK0OCBQKvFOXpy6cNIhwVDAXBVjZ-W0wrDn9-v3TYJSpuxFcFe8sUFlP0dHY-d9s4PHR2dD6na1fHRkM6nF9kNzimcGqKo-qNzF9-bYpseCeNJgIcrezh7gn-pS1cCANOEiBpYoRDVTeueQBtFwowcjqGpeGUUH6XzT4AI3OAnO4lprrsERZgT5QAG2lmfm6OuJgAp39w1la8Dme6d51aPkgvEXEdXM7YbKKGmd7QtZxhcFAiTpEZS2OwlfkjKPQ5VRh1ds5_-s5JC-eFMTH3Koo5LqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=fPdPcXiP40f0IPW9Mw_eWKp3MMFbVZL2GfAlLBwHYNLvay4mUxTknh0DUlKGmalqC0mSTwT4JiyF-oxyBBYFISIKbvTksR5qBuDemVWBlzcc7nN-sti4jCcM6TIee5S1MOTvqYO4LWhx83sl7qcjn82WEn2SP1Um8uyQD3gYCyZDglD3BpziiEp_TiHHPcvEU0tfP3k9EUdnR7V33xY-KdEUM_LyvYhCLQQEzhM69sF6lSzNg_5IvRcAMXjqpWsDL8VZASINvz3yipfMKGP8jo98asfalPZjn6tlkWdf2okmCu0Pg9oPniiwQWTTZ9aDGRPk9a3KwVkhj4FFPG8rTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwaFqYb5pvwYCpJJqiQg4-q589168mhir3aIVBv9N6gzxOtKmRWdETp0Zt47Om18aQlHGDk_AD1JkagZq1GmLtwUNo8DA1FSzUUpwsVWNfDM4zNt5OVpbn47wZh-1oi6PhRU3h_CbuX21DOsK4hxGsSlzw3f3zASk8HgbfXb6cXCBNBmOvmZU4i8NHEQs221_ABDHrt9Mx01VEkGQMRrtcYi6y2nN2x-pX9OYEE96oISeUP22iZC9nWD6jnmWTRd5JUqvQwj-nDfzUIL5m3X21uOBRrht0ZhWwvtpMm4h7B1iNwQo3buGDuiq1_CmsudJNprfVlzxeiy3uAGQOSPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN-VoIX_PKsJKYMQnjmk-DJEJN5MjfVjxGB12oMT698r-NF2s89FUcTQ2G0n7Ygyo739Pji1h-IyYa2y0izIqgAh5nzRMoOOECyBknn8PbyQNascpF8GfBrqU6GL1CJ0ytl-20b2AwQlMNAaYsKpsO-QQuEOjFAJwHz3pEUTOGiQq1yi62p3JtwDaWBSk9O4URqBDH9sLf-p8TT7cRbOWcvZUvCw40m7-2TafufHSjRboNKGqreFGaVadnYgjifLTbDTWyx12LNPZ7G_nthtCO-K8nSHSYkt32U9NHCbyRlI8hmI2Bt3lmIuqElDOkp0ng8lxo8WiXG5Ya35VHKrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdQ5HU6xbeUIQEIYpsqQ63L7jB1yQWcNiTqqPbaCq9iQKl6O2cfqH1aLulBz-6UCaoDhTk409RoC-_nKPE66s-Xs7YrYfazYso9xaJY4hOxOWCgIzX4M9TwvGVjl8Kay4p-5nkfdsnb0_oyVs0AhqY56wj817aoc56NONMkBfk7vp9JAi4_rmRUEUxc_-fW0reZSRit_sAXKKzMsPSqXhwRyUDvtI_phrQ47_9yEbWneESvjsc8yup-H7B03F2h7zMERoUhsbiPP3-BZoD99XmWagB1J0Ykfes9agA5rIZUgSaWUq3Z7Dzu4C6qt2H9kN-WwXrpdQsXSOBs_Xc-f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=jI3kZ0u3N094ldqM6Gi-7yXKO95EI69TYAx2zzAaEPBQtATswd4epL9Ax0xGBC12s8Eet-buiorwEaL4l8Aw_UurEXriWr0bXQvj4A8uHt4v1hZGVTUtdN_Bmg7XoxKu4rTmEG4aJXInhKpTbdatR5K8JSF2qbqlkpdgE0DWRD_JuRpL7mMH8s-P-OWZn1ERb5kU47f_SHex2gR4c19-PvGL48fMg-4XUOLrESmhI09x2EYeXopBk04R6iI-Hs3wVCxTMQgVdyJllOrhX2PT8pG-gPQOEMc3FjEqMPM8p9L_3X9bKZ0hdq8wI67QPhTVJLzXD80KKwacUnSfj3MgEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRtqEdq0qkVD20Wp77paUnkfx_2rFhDb46Ev_jmQigViCpARdI7ZowrVqT0hG8z0ZqCaEm_pTs2LmbO_HeT75fhq2UVNgeLVmeoIU--d4maJf7Dkns2ZAAowJtkvmp9sRkdxYM-g2BkENbGjAEQPSXApI_Annimjqur-yh6F61sPfTF-1mq0hOZ6PTXz4UVKQQF6aqOfJE0zPrWaT_nXt7yh3laD6W8MxtemS27WLUWbwoDQTqy9eG9b1YPD_0ovRtI44i4TItwRuaavqkfQr5NtBS8LKom8UxZ4l9JTClBuaosvQShLkx3KfIszJlcMTyYek3ySBuasBKvrj3gCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26829">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPfxCx_-Ahoxj7VP5BDT8A5fwR5H87T0T6LbfV28CFobn41KOLwtoQ62V8ph9HD95IX_Hkgo8XrQrYUcBiJZYIv0lgtvC6Sz7JFwgO2QZ8qUymp4_de_m3wKimSXtLVSCx97QujTxnBlyy5GGiB-aELjcf_2uQrmAu9BrQE2Z82BWxDrVYd1LTl8766Vx6byaCcyzAGUHTrwoXCj4upIelDGiPchWJTgVD20GW4qzR_vWuA_eaY4_p5JbEpubIax3oMxihLa-mwf7HLYHaO6xVnrzwEVsc0yvCYW5U46Et5yb77GuWClpWxMYbdAqSRCzt3qTodtShCCEEA0ftmxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/26829" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeqhjGsS-1tR7VVlei0Sx5M4jKZT5oZrLY9zGwwDnMdtMWR4_PDa0qKIwDEEHCQMVxZsf2NzmnIFsUO1NJtQUCkw79fCYqPyDQemHVCEZkD8U46Mj7QUZtrGI2UVxhg1wGg44p40aUqATGuSpn2CAmvYf5a0G7OdqCfxVJ9ZYeJ_wKt9rSpdPGR9_BF99GOWrVCjrRrmTs-HK-lObDXv0bYDk06VoKsfipi4c5OIPzqM9FI3eQog8FMa85OlquP57K0CdyioLMgLl-8VJN5s_sN9srgpQ-9EYOgW0lpb9bm5_SEWnk6e7AENWeRrNfYCSdKRpd0wnBuoZfiT5qiAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWuiiR5v7JNVv90V62DUm6FBfSWwJjNMNhF5Io5kA5Rg99jN_lG_nL4sAcQK_ANYyJwu5Uu48tz--A8ziOMb1we627xMBXe9gXVpF8lOovWw2Y1w8XPGxd5ovHYQZyMFt5qs8Md8aUHDg5JKszZz87VjuN_JrR_A1VB2uTZ2zP7ii2S2bkATG8hVlThgEMWTdpHffG7grpErgIA_52uQSCA86uxP_9k3Pm6DQyIMjXQ9l9JRZjgLOD3UXINTYnrjblRhr20hGqCBANumqYgooxMJsY7njINWIth4Qq3aBwiK11utfwg64x0hvIRE4JJVnzyszBhJS_tKT5AQGJviaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=XlhnWBEQ4TDWmZwwVdIFOETBKQWE9s2Fyxyzt2HGrA4zcnN-g2gen9UqFLmCZYTozuZ4j5vlIQPEZWOi3WA4vyUn8r5-1UE5q9EjBogzlfylkJib4usRv7a8Y6yVoZC5KANW2ZOFJxwSFwgRXW7k_0_aU6Emsxb8ABs7vd8Ff4ArLsk2YCf5Jkecrt61kZGLqGsJLH5I6xbZJTfHNqW2Pu1vDf_Y79p8NPAp-k4no-xryQws0-MfuMMn9B5kRRZ4BxzJaTRg9A2nWMkbm0YgOrgD68VYf1Wh1IDsZdIPoOKYjK0Zo7N9Jt_jTgFyYOd6mFxL8kif3W2XAfIgPU6ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDz7VcMTMIivY_0ieRuoVgg6DCyAY2I2fVk0GJItEPfp5cICzcW20F0G8V0CkZDoT7G3naWMfMEe-Fd_mky6-H2dg8EsZ5qzd5sZPStGSTOvgqrJ-uuX0SyPxzfH4nAwxWJjL9MDjRd4Impy6bPY18fS8ACSAvvBBczItMmNELtqJkYMkAPYs_fSyCjPCi1Exn6jF156gYzsTC1oykYYoNp-mbBRmr0QKRUcup2i1RQUTl5k2mgbMO3KqhF7SL1QpUSF83q_J7plrYFoj81plDuzNrMA8r2VWkEtm2NmT5L8Td481C969HXbyKTzU4O72Hz45DdlAWUMlIJdYuA1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=b8-UqMNwB_RMaLn1_9fNiN4qS65YHrNaS8jXR7hY6hfDfogBTQOQxBQK-fOSwYiu24caVz2ynZo7U26_eS6_Pkdlt5xE9Ab-4m10KSE6qrte0ORNMN_k0J4tbyoZYAwnvDYljWzAymUIZ9t4VSq9fcqMofTJCV18KKXC4HaJBpQh9XTCAFp65UHRcZqsF62-a2f7RmG5kGKzphYKRJTqZd5hhbi5cHYeKehRtEDz7plRfUAM-_sgnaa26EygCTOOiKOT90y3ENdG6hKrYBIIjJalm75UOBNG30twq8CQhSG5YHUgWGs9vdYz0nE0hZAv2AK1gwPkBRNZ-FsVs4s9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKWme0TEH_Jg-8QPA4e9JThdX-Kt6NO_BBH2JIjrpJFlIkEuIgKwDlRXdQRL5DdaeyBwsq9ymEZb3pP02atK7Z0cCEwOApi7koEo2Lh7V2zrc6c06iTZom7dE5xbUYR5xIQTY6DxDISt-Rnpa7wvUuD2538LFSwmTFV_3EZ13111QRn2681mkO8w4qPtMA-CP-h9tAIIuTBcqCq34pzKxqt0sjftlLZGeY38IAuCY3ayi5bU4cgUhI5Nl9DvY20JJuUNuJcOx7Z2P4BkDjGRdjaGdJ51tBOmGhKy3G_HE-XoYIOSV2tg-wR6img9f-UAXYr06gjIih1fcExuRfPEyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1HpVsRpDDNDUP4U7KBDjC0kJwcxnZZJ-X4l_zbYg8j4nrVMMBaurdJZJhE3wF5oFptXUHscqplyxKeWvMf7u9RbM_OGH_PC3dxpaXszOjQ2W9X09xz5vMp-MLbKWlWd24BE5Hh8RhoFryUtlVlGDwJzf3LeKpQKT1ye_-HXeB8bOHTko7fCQLDiZXgxTDcKDOnpDK7b5zGn6MvaAMgT21qhaK0AVjxsiLUFC4e1u6ak9mwgI809CfFpTYHIjZ37y_kf8qtrvui4VELJh5eWxItbQvWTwbtg7xDr7HfXXYxRQsXPB1iYrnrC8fQ8mJNZgEyAPKKbTNNY6gj1Wmxyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=pQZFSC-stVz8UeE-URCl21zQKohkZAiXC5ZMicFqN7ktSZv1UEb4AOHneF8uJW1Axm4jzf9cozU4BddLE4bjw9e8Ta8ZIB8GJY53nP1zbNOtvNt-R3913R28mJZNropuHNXEYTnTAjngq9MSYo2pvyTN5fyt3vICKciP_ZjsV2s2g3OAViPmuv8WlQiRwY3nQ90lik3hsnEad6vwHmr6ZwG2sKSb4bDNw_pHQ3igul5OZLrhXtZ8XZnXpqELohPlFQwtq8cZICPJ0zTZ14WQ5kW8-k_fp76xVSBo_yXPX2HFWwOOhjIJYvf1Djc2PNXMD8_Ql7g4PQuAom1xthBcDq3I_VxNt9VP021Gfi4ueBgw6ySDYgfYTxk8rGTfhQauMOLd7hdXaf5-ogP68WKyUIqtFc98Rq6wctWrxNsFP9k39xRByo02zkm3nU_ouZOo3pOrS6kcJ2VWl5w3PyV0h4PS838bsDWrU9X04eyx8POAaoIEqovmCoMijzoEEzhrYz2zXiAPULGqScczTZ28wT2GHl4Iqx1h5DclAwypXWIj-YoiDTpJ80k5tR2HKYYgSRY8vz82Mvh8R4tzsQqYphjBdRlQXxGyB9SIzHdBKP2AfKoGPE1LRzB8GWUvycfYuo_K9GY6SRyo8jB4E4Py8GX75NkRTbzi1XxEdWvOwU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=Syhj11ecZhLyhLELzi63Wypi7wdb-Ee8ZmcjE--gObq_KrgdAX2HVyc0gqbneCl1QRIjRAhJ0sEyn6s8opW0RUnwtWLKGwASjC1t9puwI_wR9wiCO5oP30rkSJcj24og6fs1xh1LAL1Dk2YKfl_e9LbjgwDkze6VpD8F3S7EZ5phNgShY4iXWXUDI5ndtrRHtdFij9M7GFawjoBkc3k5l02kwQtSfV8xEvmUVdz7RLVSdKv4JBZNLOP3XvifDwvBISuk5bcSIOevbL2IK_Mco4f0B1M65dkN3uKXhlrmg1nkxc35f_7FpKSvQHt7hdsq1ikAUUodchUuzo7Q68OMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4W2fumHRq5cUrz5IA8jIb-CGoXV5mC1xXmfMHst50SYt420xy3qIHWr7osrg31Rp9naShJRKjx1Uiso6nrGQKwAO-v7270enVKQmM4XYQudmGlH53xQso1oOrIp_hC_2PMcdKmHPaAT7Dhk8YY9p1Ov0khQZfCfG968Q6O8uy4Cp0HVbU1UOaPWP9wqMGUgM4JD5jJjVCdmmmjyLuFMzgNdLuBscWUgbFfUb5ZETg2VDP_BneD83U8y6BL3PNk8qLgElId6BA7JVlGp4gSbxLguONEdXzxSDqGQc3HeCvZr599kwYM6HdCSg0STe1_oFzG6AsYYSPQTocuEKB4HkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhGF50jp9ycu7cbd56G_4H_S8-Sw5pY-b0BlSEET8jkmjI1AMx1NXP5Om02v5S8W7_oRQ9H01n4IOER-HHG-qdYh0oYhVWzW3wRBoFKXrncPKPvVMYguQ5oonlt5wqnaMRSnLrvJfHfYA8NTqcVxZ8s5ZfBAQM-yQI_3MeJkcRvi0BXeO7AzEJZKDGmx_9RIeP-wGjjx9iS6JKfhpa4JbFRTWRAZz7efRXJZ5uLBuMhDSRonbiUL6OANsJZ5axzSRjZcUTm5vMMaVCYQNuryCdZEE6wgxrGjPNZYHg1Ooll02_GEUx_1XMOAJG8IXpK9XL7uDm4q0Lk_bv6WqMSlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax5TwQhfiBtAaurLEcFU5J7YwVToA7hygV3yuUqqyfvwBbdaxwDfEE04XKtGBatwcXndzYXnD2cd_5gAwpx9vA4f2bXpr-v2hO6LsQiqjfQ5Va-180sfNmVxwcmPuP3Q1O3m5IBqwNRrUfiQULX0hoXmgUITqrRthKQqb6nNwRotQAjJT3F64GX6EjUKPqb3kuGBJiHNuZwDn6N6jy-iJlQCJ4IgnYYFaxzpyWryd8qI56f3lp0VwtaHigrpA8gM4QneO2ejghjYvj7I4Y0raZDuvn41114hA3BW4W0twpq4xqyIL-eka0b9s3cOGyoNiBmtyKL5VHCAsuIVxVAWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fvsq_PqlYWkSFU142De9mrVd19dz73UXQyLk-RHXKxtWQ_mni4VinjAUOTI_-whrEA1_ngJ_cfRpqW9mHKwSSi_lkb2TlJo0ly3QLFpxqGQmjqircElMwtTarKX1feucjAVSTSf9QVlgpjeWCXuq_-Gg3QagVQYot7CfU_UeSnb7a6rfPitScvkURXKnBEZZ9qiGxV2M9bXSl432RGOzxUZ8hI_pQfqFOI60Sp6nl7hJRMuxM7gkGnUY7T_--WcMMdSN5KMq0HyPdgLyoh-I8-p3mVhCF9d42rqEpvelp199ZdVBxx4G7hOOgZvQMiip1glueJsr2WlblXa1l_Ydmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjOM9ic8-rou644tw9MsuYLwPMYa2LgrtR29lKUxLZuQYTogdYd_R6SllmHD9ky3_TT58WHD4hlonTy7OLAzTdxZ-NizqGFgJzQWu_WCTVsAfHhKKQSyXzEYMYcV4ktIO_qZkfmW-NYxKFtXWCRnjyRE4VODXFe6Xj3_1ur3rQNIsuS7kbKX5gAb9dipjzYaJfOvKpYIvBgl1AR-iqHZdXwNLWymZTqFAGuKhQ28S8_-wJz9-81GzQ7OHfOrIj7b44NCjeN7_cMJvMxfq6BfuIXqgKclK1cTYTVMSZ4bQa87MWGK41p3DMkXMwHNzJF2wjxbsPCWzxPdgPgL0v3URQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drEpuKrEVlapZIIPU-5PUWDgWzSfKfaxKjj_Q9sLYwgRWDhxCJgZyhqmQZkA-Wn1KNDrBX60mlKHgA3yQwln-RBkdk1H3H_A_57-FpFyl6vLd5xyL0j1qz8jnXILS-kflLw2QMTtPczc1BtKDHVX6FULiU1MpuKuJWMcH_9ooqpHXWoOWQD28XIB0ZqOSEbJ6EHy3je77-GZN5LIQPypYWGGd_c0-7CdbrRkQAppqeboMCrFd-arGIWA8JQjZFMLXbFTUng6bjb_5Pi7-RV5U-79cXS-pCudB32xGB-wqib1c06SEYQnCGRB427YEp4JzfmHqVOIMk4wyVpJ_90AIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyRzXvBzn_7RwFZ6QGGtHQZGSnwDRa6uuSypUnqNHNLBc7GN2Kj7aQNydYdBMnbNO_i8GwXj85EXuf6IpjISmfNtj0DPpvs-SL3obchKCIxL0s1TXUbuZyekV2ZXiexqErrcDX9R2kskVRWIT8XSX89Cl90vauWUFU2bBLYLwqQK3y7KjFTFhkcJ5xR49t2BfHPmwxPIuSGt0YTxpYV_K_Qws7r-1GYIMSwHjXUNYo7E-ThhaJjB8OIppetDJtTaSPGCS8LnepysJngJctN3yfAvNUxVg8zi2X425isBBJQi3uBUmIUhQJIkxYJAGjC11pcP8-Dw8nCvm76RzGZl9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmpeU4MBQRJs-hkdpqH5EhRp5HVyNNQ63Y0Xr8pRGDrMSPWqbkJT_tXu-QBxejKKLMaLldu1DdYy-kekMB9YHUB11F5rn7JKYvDDhtmJVteB5tTqZB-C0xZkmGhkJ19yOnAPEkMyzxCJXE2mgG1CybYu8sr0aCErdhw7FPATH_gT-9WTEx-Z0xyRubLZXuyVMz-x09XUqcFY5ZDOhD2vjtDnrYQwGDuNCJ5VwlD39fYUwZXzXa2loJebzhqHRFd9iHvri5FvBNJH1rTHzy4Y8t5ZLHtsPO7KnRnPl6eYLhsirat02u57qB6VwvEZwVDmp4CSgZV_hwmjKT55EKwT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsACNJ4YoHSjKfAX_iZ5HTKzCT_L3WFMnN6lcmHQFs0kZnWWoMmsEyckprrJAnnZuZ677fKzd84qWNSJ6NaeDOsT-Q8tCCVXwFxZ5CYMch7qjNODxOVJhaPyiioa_ADM9cIk6mRqI6ytACzqOxYy1wXZGhFkPFlo0V2F0A3lV4KKA9ZmfPZ8fRixMrXxZu5Drn6lnGMaZPsh-OmjAwiA1p1oRVvHjxB_dU4cMZj9BS6ldknNpOx2W3VYecAaLSdfz9otjJ9dimlKp0Bj087Fyyp_KTmKUd_9el0sXOSLql3t8XsBU_4X4_a-AjIzCXz7cgTIGuM9uyNADRLOXLvQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBcTR-r6hd5DRAGavn04h9FrXVCTqm5zE1k6pGMAz_iKtWdFQKxTtz_3VZDiNVlV4qZWBm7ZR3JHaO9C-9hHIIX6N13NmOGhnckkzd_53h6vtG0nsLzCFzFgdWoLp5mYog5lWp8zIcVFFhMHRCQTi4Z6ecUL_xkJl73SmsVMO3UyCNi94EGqnMxep8BVB140Hohu-05f3YC6MEGx5SwfMSleXfU0uIrBUPpCvWubg80Vd9brveF-y9HsE6LLLlwRjrLvw7lqI66moETnsKJIiZQz556TfUrE0NTfxsp0kgPEHxjVH8mZf_HY9emo2XIqyPqIVh8f2Ad9qVwiZNY55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=NYlMmbZtNPVMi9fi-iAUWcve6uczhaZw1BYwkAa4gSzwL3VgRcGTCX4rqBHajqhZ8ixCuuqVEw6CI7m7JZ3e8wN3HHlnKQs07FPHmaD-A4HWcXeozdVcqWLNk-qfzFpkZIdIMuPezcNQNz1PKpZdz4b4wJVHLhHnvSr51D3atNANMhbcvOg6e5UZF4WTxlVm7RhibboSUj_e262Wp5qk-tYphbv5tgn3qFQD6szAxQNoMi6pcbusfb47yR-kl28bETtUfgzZVWFi1bkH1p6Bx60q4WYyvSgoSSEja6mTGcphozVtakZ2zRTfVMFc6neYEIlesY2AJ8KoFT4ypSiDjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=NYlMmbZtNPVMi9fi-iAUWcve6uczhaZw1BYwkAa4gSzwL3VgRcGTCX4rqBHajqhZ8ixCuuqVEw6CI7m7JZ3e8wN3HHlnKQs07FPHmaD-A4HWcXeozdVcqWLNk-qfzFpkZIdIMuPezcNQNz1PKpZdz4b4wJVHLhHnvSr51D3atNANMhbcvOg6e5UZF4WTxlVm7RhibboSUj_e262Wp5qk-tYphbv5tgn3qFQD6szAxQNoMi6pcbusfb47yR-kl28bETtUfgzZVWFi1bkH1p6Bx60q4WYyvSgoSSEja6mTGcphozVtakZ2zRTfVMFc6neYEIlesY2AJ8KoFT4ypSiDjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXOfp94oinrIAP0vWzYCqqZsHW7voi6HuIFgXNDb_lSIBKxi44hKLZvMoJtAt18sTJQyd_r-_7xow1wSjzVJx8OX8zRPgAGUo7oCbz0SXMoj2okJUkiQRhSP-SyesfHzauFQzcJ38EUVtQBRgfSOjLA1PQGPPBu9mkQUWA_LjJjpEiwoC-4hk9Rp0ueUzZX9qe6Kxq4wqR6fzYqYjjQ2JsXFS8BpB8DAUSqaBNP-gj-t7V9_vqcPQwyv9Tnw7T1UzNA4WPgwFsHuj1q3NOT78JmWcOBbcPrmAuPGC93awTkCJx6lMPCsh_XbKZih_I-ZQDn5kmP97W9UBuocbw-FeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU49xYALl_zbqfSiOIbPx-Mc3leYBRCAYtXOElYiyaG3LO4tNE_YDNKjZinqvZd-KH2KE2qseMPW1UZIx-Rdn-GBE9Beai5OlEdfx8tvn1eWmorGkikCbFQSGfu2x8lQVLLmHlX7eJ2ONu_WqBEF2UIpmek3AlSP9BZEkTRsFbygZGx5gdrm3swljch7es5JIz3H2-HgC7_PMiQpEu4gKIV9EA-pL40r4q5x_M-TYwzXtj__dcCBI0lGmdiXn51Y90OwRS38EX_EA7bbhMOJX0SabaD9wtr167FDaQcADJur7DR9YyxYDceBJLLUNMlWc2AQOUSbqH_BY4VbitGtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUXQGVhLIcncGWXSJ5wNkPG0pNgqN6WEFzq4HOKsN9ZgKNa5PX5rKuMqbvAGf06_h9ZsgU_ckyVp2P_lZFjC13SSfVb6sy7XkoMLAQA_p-yNLBZtQqd4YXm6RU_ki6BJdz329umQ0nEK-wn9DYhUv6ULfiXMmXl7QW012DeHq06SFicg-Mrvpbg6wE5Yb4R2VdcRzBBoPyLEvaH6mRAUYgNZ9Kjkei1gqEM1AE1hNnQucviJ4i118ZyV8wf6Cuox6xc99hjwhgaXPg2kURe79ok4Sr7Tu8Htw8_fjDdGAdnEFQXYHXJByPJ_sxSHd-SH0JT9pfc5TlKvT8T7loQIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ct8zf3cSCHhuDeqAMF8qxmrE3fMcpXxhxxbpTTLv9m0_6zL_h9K07-ShENrxG7iJpO1modeLdL9vlAv6cVfj0EgblG5qzJJALFjMPxM0RSbgVc2GcbTWFZGGe9Ib1whF6t0Zi6embDrWNj3aNjcXC8l_5BrqoO7Z-sYtkgaX258Aa4Kvqdu0SrWQs15cAXb9OC0pdTYAhZei73PL0xLWpdGivnZoolZ-ps-0CmB3cj7kyhkwAVnLf3ZnZ7CiRS5nVT67UI5_xKzDrBVfdTzApSw5dYSc6eW-p6sEp1RfpjzLjE8tdYLR4qX2B12emWfZJffe5q7VtjIhpU7iPblNmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=CTtwwmq_HjAPsfexhGubY-GStRNmIdIU9jrhJTtVLQCVYwiA4Mi5mX6Rz2r7FGbma-hLjWPltlnMwG65gE_j2xKP1FiDKKnN6rb1VtuMj-jclBqdMSOMElJ2_KM4uf5Qwjp4jUKFSHOyRgtez7uIMui7YtW7b9jNuifBXUDSyrpwyiNKTLDqO1zztz1AsD07WKXW1yNMoo61-WNuv4poYIUSmMAL0WcZWEmWPqIxor9J6-CgaC8mAEOGUu-UMXCnLTFb3xW5wB2jj3BK_DjkXodIwQHhameOeyz2Z6aixaY3lUaLwETtClHmpLj2WDZrxJAQJZO2JBE03EzkAmOdJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=CTtwwmq_HjAPsfexhGubY-GStRNmIdIU9jrhJTtVLQCVYwiA4Mi5mX6Rz2r7FGbma-hLjWPltlnMwG65gE_j2xKP1FiDKKnN6rb1VtuMj-jclBqdMSOMElJ2_KM4uf5Qwjp4jUKFSHOyRgtez7uIMui7YtW7b9jNuifBXUDSyrpwyiNKTLDqO1zztz1AsD07WKXW1yNMoo61-WNuv4poYIUSmMAL0WcZWEmWPqIxor9J6-CgaC8mAEOGUu-UMXCnLTFb3xW5wB2jj3BK_DjkXodIwQHhameOeyz2Z6aixaY3lUaLwETtClHmpLj2WDZrxJAQJZO2JBE03EzkAmOdJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=iZMhowXJ7cYhBi9qpx-jVC2LYe1nwmZECCasM2wX3_jsB-OgH9yQKqvlz6DYQ1ALadNSB_Gmd_6mEPzQk4SuI9QhTNmfxQ00GvnquLTWB-ka5S_EfH7PQh5a8qpquIslHyH-UHyRG4JeFw2ReUwZOFdfY5HpeuW2YeRSpP7iDcvP6J5yLPqOsnYlbqh0Uv7WRYC2U05e9rAWB1GWLrEaPL8gZSlqtJV45MrOwnmpQad0oJM8JMkD6CltMoB3oBNeqJM98k7dO4QW9l2o3fXJPX6JGjqC60SvbueRqV4RK5mT_inR9vVmNfkAuwuAZE1_RodMui7p_sAwQYFsBm6sqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0yKQqSeQqHdHLLh3VlRJNv2Y9CHlonWJzsrak3oloe-rLNGyu0Ic6NEPWMtpaMZEzwllSBQjBR159JcgJqf221E6Ei6b7SSXn1KHKWaEeIxrju4bOq503UChkmeRCshOoyPxI3I40hMrtj8oIz8_poVoH9dosoJyFabANGM9w06zHxZMnhru1bM8wqd-g6UOGgyoM4-GWOy3pd_3KEN5y00f44E-z0WsWGwwRUwoXvRAy2GonquHwy0i4u6TJDQIvfvtSQpq5Inq_e4AJF0c2alp2K3rJg-vbg2DmXqxdaQty6NMk_YWl_3QwRrTcMOVFC16xxrk0KEKDCDKcxeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB1iEw_gQwnAr4hLECf0FPJEcR2Z9wcalLO9kPAPycfz1g7KJFUOujhwehaKxOzP8UGYakBzShi76mlfGHW7w-Y3NOcvN6jJbQcq2NGE-BJElCvsvg_XhEF82tTR7fa6eHy0EWliZH7JLSeVS32mj0PIzu5pi3MfHcGgSx1xYZbydZG0oA3qc22PbiatX6kwkbv8TOR5OjatG-7V38DF7BvPsYezTJsr_5GfNYDQpOdXFmbBqqFXPHvnJ6FY_7Wln2nGrLUjMeLtRKVpE5dhJgs_ijoUF--LWvzept1IACi7ei-qdOJkcdzu1RXKFvuW6LStzHtYdoX39zS0Y2LQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=mauAhsPJKkDGQpNypgFCO90BL8ps3wf0tpc18uNzMRDpKxf1KIERXVaKz7IH0DgmRu-KO1GhJpqTehTPDksfchK12TyCBf6RJOcWQa47JSqg1suJVA5Nnt4Unh4UQxYu6kpWPHy9P8_dXIM3XRHnOphtC0U9q2hBNEQIQGFpD7YKX1gQe6bP7ky8mtL0RlQHjNapd9wHhcDX4t3KhLDtxRRjo5b6qMpwiPBZ7kEITz-MPtaYgx7f7DqRpmwxkthi6FMrHep_G13YgYL_3hClK_PLWCzcc9hm_8IoUkygrFrcNHpnyXF_f9wmvSo1gnb6cSxa67eZimXoHmaPRTgfHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=mauAhsPJKkDGQpNypgFCO90BL8ps3wf0tpc18uNzMRDpKxf1KIERXVaKz7IH0DgmRu-KO1GhJpqTehTPDksfchK12TyCBf6RJOcWQa47JSqg1suJVA5Nnt4Unh4UQxYu6kpWPHy9P8_dXIM3XRHnOphtC0U9q2hBNEQIQGFpD7YKX1gQe6bP7ky8mtL0RlQHjNapd9wHhcDX4t3KhLDtxRRjo5b6qMpwiPBZ7kEITz-MPtaYgx7f7DqRpmwxkthi6FMrHep_G13YgYL_3hClK_PLWCzcc9hm_8IoUkygrFrcNHpnyXF_f9wmvSo1gnb6cSxa67eZimXoHmaPRTgfHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=MKT0O8HqnQqRUGC2c928toRZZZ9kpgL8kInN-pZ5zxktLTygdiSgpkajgN_SeJ_ShR9zbd-kYsltHgXnA6mr1bewnDZC3R1GrmxRr6EbuTT0PqkGLPvFjBYZD8snrM-QMWiaRyCQlTdD5Bmz_N0nuJzaSbSMV3f6JDyfFmfa9F3fvlCuvurmDmu5HrLWugFjApRisLw3tVyF4URDcyJ3lzZboUGp3euOrDxLhgd8ZlQJLAsNPqB0FHlf6u1fGlAqfePp25oKD_qpDJVjt-SxjfNCboL1INV6LH5pkWqWrF_xeqnVPpI0vWSAQ_jXJWVcY5zd65rgSYq_ZHpDPyZM9TMMpczdxWn6oThEMg-4iPpU9BHlUBgJFO3Bsl9Bh6r2-4vWXFVmUdeSH9qkAb8GyG7N_apW-cYpFDWePE8Dqgv9webYa_bwvkZ1GC5W5AeV1rASUMUnwM0b8XqbDknsRVvpln2OIXutIWZjTGxt5l_afyh6GcwADIm32UMR0glShNfo0K872lPZP171uCpLXfa8jJSRZJawbRx-cQumMgTf4yCXwOhnzvWiHOuj-V6OXcTSKHenAHDSAJm6-_M7q6FgflHud1IKTp2G347hwJneAwu7wE69X0KD-N6d6460q9DbTqZhixHbx89iNq_y9cngzW6AWSlwNqYLEyg1HAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=MKT0O8HqnQqRUGC2c928toRZZZ9kpgL8kInN-pZ5zxktLTygdiSgpkajgN_SeJ_ShR9zbd-kYsltHgXnA6mr1bewnDZC3R1GrmxRr6EbuTT0PqkGLPvFjBYZD8snrM-QMWiaRyCQlTdD5Bmz_N0nuJzaSbSMV3f6JDyfFmfa9F3fvlCuvurmDmu5HrLWugFjApRisLw3tVyF4URDcyJ3lzZboUGp3euOrDxLhgd8ZlQJLAsNPqB0FHlf6u1fGlAqfePp25oKD_qpDJVjt-SxjfNCboL1INV6LH5pkWqWrF_xeqnVPpI0vWSAQ_jXJWVcY5zd65rgSYq_ZHpDPyZM9TMMpczdxWn6oThEMg-4iPpU9BHlUBgJFO3Bsl9Bh6r2-4vWXFVmUdeSH9qkAb8GyG7N_apW-cYpFDWePE8Dqgv9webYa_bwvkZ1GC5W5AeV1rASUMUnwM0b8XqbDknsRVvpln2OIXutIWZjTGxt5l_afyh6GcwADIm32UMR0glShNfo0K872lPZP171uCpLXfa8jJSRZJawbRx-cQumMgTf4yCXwOhnzvWiHOuj-V6OXcTSKHenAHDSAJm6-_M7q6FgflHud1IKTp2G347hwJneAwu7wE69X0KD-N6d6460q9DbTqZhixHbx89iNq_y9cngzW6AWSlwNqYLEyg1HAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o5WBJsBxkmqbDAcDN9nM8blwla_gjzUASlUuc9TqR6YuYXxeUqx9hGKbxcPk_DkiYy3FYSviasY3--IytMndvYn4Ly2rFUBt_N4XlxRcBIfbMHbCJShpWqQVGlKvRrmp7rXoDt98qCLIkQRsnAQv93m_B4zROCRv7bZcbvwZds9AeKUTzi5TZmpS74MVlNCrZTTBjO2AuK18UZJYkAOmRchYuvvHPnbAxX9UI4iJIJx8IeRq3e5301YBlGDb_K6NQZvdU2Fio3b97uczciPgNmmUQq4UZQIu7fvj9zCjyK5mqL0GJ2G9AkVsvJ0yGkoBPKnlbDbj1v7ULJl5UXtwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0_wSU0BlUHim4pLJWLgoXkLpWe36zJQPtdnpNhuYg2D6jBZnXWdb6jYWZUbmc5VWnmOCNQUPA-LSaax3ZuOxSc3BMNt2So2FnKIP7hc2nGvnTZ4ha4bTqHZ41s-xSF1oDcJteofMz2uNYI_s8yfQ_I85iiXKbX9zx3eJxDsnMhJZDJhCksNiW7C0HUVxhLVCM1VRpeSoBYKZ9IfbbkGATRSadkA0wGBZpY6vpxUuYyHguTFSTd1XQ9jLQKb1m7xeAW4PsE2DY3cZmvrx08APisOaqABF2v0KADnKP-YZZZw4y6q94NXZl3v693PpSe_Py1rCSo9QuncMpJcT3w0-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpRfwn6QfUjpSJFlFI21ZJfX_gwW55tLRS7rcuMlkZT-WuJoG0HIkP4OZ-1Y-m-grMUO-WMJkIo1QqDUk0uZt-nbGQAv-huNH7Xv9WCm9kjLFSoYroBAXOYLG7lcUebtT8MebhFGygyCoXDiQ06VdItRHzqSmVRiQOKsD3zb01dQuTBqsNRKekyiqpsEHP0K3y-pC-6-IeeNkqKAfK_rFEqqn9x2vJPtBf0u4uFvFqm6fTruoHCy1bQ2opHhckjKIjzP3G5E4rcFOv6m0ZX1jKGrtBn9hLGyLyzde4RYsUASMyaW397GKEa0dgJOVUy6sl4SUyZZX9RVmSpeLMqfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F30EWuzwY06_xef03YXm_1AJUw5KdEgz2VyBOniobyOE1PcSc39hNbxKGxWDlLPBQpZjsP8m7Nf_M8YKY58nKlKR-eyx1f_vhPOQbSRdLCnYMaEVWgdiINdwAQHHsZy-Ua0ziQHqgkQEAWg3Ut-s-vNsmNv2dz0d_sP6XMISk14KEFnnVaGfQY5J6CQ9myzR4Wg47_0jxQAvf5E_MhbUXleFN6i69h_CXyD-kf6BY1fyYZLkN1bmJI85B9qPP2eykVF3Q-plCFsHLCcfAA5C2L8KLnp-5Of5twgNruSo_z5j6FZMiO-S9xFBUJrCX06M9lvPkmf_yA9nXDqFUBuKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1SRw1Vv9olL596Nd6aleJAjxCyO_tpVy2qfISjXZtsj91VePQ-D6II1FB0gUP2eTg1igdUbIjo_UwTnFqTGPFmDqTzfFzfpgDXVLjVzPf6kTzH5SKYQztdevy0Zd1WwRnYw6yJeyMUfsu5chfCJzmPwnehcTmoRtRc1Fw3UEFBMf30VODn6iFeUBiW3f5ZdAshMEcVtor7gk74Ud7cOTK2Zcw_AUdyWDrbnfNWI4ZQtQAiKuPKT-Fzi8X38OcJjYQv_0i2Ag9aCN1zB4CkQi39NOTVFQ3DpTK8qufseW4xKFeUN8KvOOpVLgJB4NUPZJ_r4a7JeNhzR2EBNvnPxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1Jasr9aZuIVNcvnCf774SxyuCjVlAOQT8pfKNxIRLa-NXkk2A2PaYTP0McMtCqTjMQXwXzSWOIyKoMueKOgpSCWSk0W5_0TVqnV1GCzx5U8jXLgjND1TWqQPENzsmwMCtv-R8hwm1kvKeq0ez3EDTcxiJO6-4qcIbp_dO3ZKmNjQ2JmMK5cWUoaiEFKh3WTSwRKGPaIeCeuRwcmuBrX_RrWG8Dyq9rIzbR7PQ5sfKsIFLOg6lfT5It--xzamyde_is6-MhqBu2mX2qOMs6xjs6ze6tZHNFKaJNj4Ec5hHwvHv0jFUnVIR8q_yhE_45Vl3R5F10TAd6AXiiZ7h-ysw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ovcBfNzdYfSP9Z5ZWWE7lVvNY7W-nLyXxNC8pSGeU1ZHcKnMd2garMgPSGsAxejXvAuoY6I8Qem28SaElWTOqBO89OWYqi7alk6zF7u6iizjCqzfLHJ9e-y7sX5BTMO82qh0-tBRd42dkERebv5kFQTblTLavHSPq3eC9ELicLUjJK1mSeDjCmD6ojFl6b4IFiJzlMKqabSProsiyT7T49WNL3Y3bYH5rA-lWuMU9OLmrhjH4WvbaVO2Fw1k-VDWsWr3zbAAaAK-kkgjKM1ac56eiypb_Dk7B5fG_HcGwfqZUQaJImZ-74s_b1g6M27a4lsxM4UFVpl0byWzraupTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ovcBfNzdYfSP9Z5ZWWE7lVvNY7W-nLyXxNC8pSGeU1ZHcKnMd2garMgPSGsAxejXvAuoY6I8Qem28SaElWTOqBO89OWYqi7alk6zF7u6iizjCqzfLHJ9e-y7sX5BTMO82qh0-tBRd42dkERebv5kFQTblTLavHSPq3eC9ELicLUjJK1mSeDjCmD6ojFl6b4IFiJzlMKqabSProsiyT7T49WNL3Y3bYH5rA-lWuMU9OLmrhjH4WvbaVO2Fw1k-VDWsWr3zbAAaAK-kkgjKM1ac56eiypb_Dk7B5fG_HcGwfqZUQaJImZ-74s_b1g6M27a4lsxM4UFVpl0byWzraupTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=GfPXy0kI4YyJ1ewkCmbP1yM7liu-ishW9U4YASQO3kqwqW8eFWywimzwT76U6CwsdvOyKU3M8pi-RPlYp6YYXJCK9THAzJuqn37eefjuwqXZwrtWUtBN82TUy4sADXM7uhkPEIPmV8vgy4Elk00DasqUmmlzNXN9MLIN6hrTUrJch8reQCXTYA45MgpIJd2c4YDXld8oU-JxKnD6onI6ZygY_V4Vv5B6vt2jBlPlCZu1voC9lVi8m3zJ5bLHCpmN5h2D2Y0qF7C68oc5uz7eVGaXiKSYYmnT6jxrAoj9AyRrC7P_v6p6CXZzV2ZAecWW7CfcVoXn3yO75LLmQMMMCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=GfPXy0kI4YyJ1ewkCmbP1yM7liu-ishW9U4YASQO3kqwqW8eFWywimzwT76U6CwsdvOyKU3M8pi-RPlYp6YYXJCK9THAzJuqn37eefjuwqXZwrtWUtBN82TUy4sADXM7uhkPEIPmV8vgy4Elk00DasqUmmlzNXN9MLIN6hrTUrJch8reQCXTYA45MgpIJd2c4YDXld8oU-JxKnD6onI6ZygY_V4Vv5B6vt2jBlPlCZu1voC9lVi8m3zJ5bLHCpmN5h2D2Y0qF7C68oc5uz7eVGaXiKSYYmnT6jxrAoj9AyRrC7P_v6p6CXZzV2ZAecWW7CfcVoXn3yO75LLmQMMMCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4UDsHHD8so0lItGoYdVyfBGzQNNtB3N9FxdhGUC8AYW98cHbb9rixzH5EGAX02WZFNmxiIjKKWpUVNpQkwzvIiKnaMWvJMlWpCRBjpMi14eM9wPNvvBPEFfen__b0ydOKHjYglCWBdLerDImNVyMO1LS8VSObQVsdP9ssJyB_NoSDVVcaB6WI3pVcAeY_xrLNEjjEapj_2wUN_PuXfoEq0oKswNbFyVBgTE-nPEHx9Vl-z1F4B913lwhsKye4y281uTwr_UhmCHz-U2HXr3kavvbxWpWCuVvSKM11X-SN4iCR4JWwQTdNZeuPwZplyMdGhRiaiZn_qI2xx5I9RsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAr886JK7p7NcA_nrNosn-7bTiSZIHNYOWTqe98v7WKVU5hAb0yhZwFdHOflH1t7B7_3Y36KJ5tYMuqhoep0zdF2zgmKDEjn4QOtfJO3jkMOhdtoDJns3J9gJdCwgXPU4nRBJ9z-cTl7aslVipPVcUwYZyU9kA7pj9EBaUbF91lMfFByk07nAzBpIby6HVKx6T1zOejth9vK3kbtBWNwSDbVYOdM7vhJk-g-BGjtx3CLn_KacQ-kjwwr09GZkE8q53urfB6X18cQD9YSgO5MBl1KUZmPNkFrSEFW2wVPKyLWxq85RYejraAhtf3bO2BAQr1hlv_SeybTsZBYu8BN3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jB6Wjdr23HQzoCAkueTSrQbJ7YQYBBP19DXsitXc2rf5AmV03scnmx22O7lp7Nhq-TRETtWHJWbGk7SGPT9zrPy9e0dnuQhKpoOMknpOZ9kTozADuXJYXWeAj8g2sJzPXJZEGDKppO5M7ZbL2XnlChFsYX2m4z1JUVEgckxKmDU4z7oSa94BsVfzqjUi_oFVUVav0PpTQreKrAozuYdXHLN0QiKbMj6Wv4T3UsHUBI7bcca1KXjMHB6uWIiPXnZQfiA03WcuVMURmYPuGYGjfDDz1Nkpa4BRhWZ0Wr929cUDvkCFv76K4I8FgKyQ8uRqdbv1EzIG-UcPWsie_lt_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=jB6Wjdr23HQzoCAkueTSrQbJ7YQYBBP19DXsitXc2rf5AmV03scnmx22O7lp7Nhq-TRETtWHJWbGk7SGPT9zrPy9e0dnuQhKpoOMknpOZ9kTozADuXJYXWeAj8g2sJzPXJZEGDKppO5M7ZbL2XnlChFsYX2m4z1JUVEgckxKmDU4z7oSa94BsVfzqjUi_oFVUVav0PpTQreKrAozuYdXHLN0QiKbMj6Wv4T3UsHUBI7bcca1KXjMHB6uWIiPXnZQfiA03WcuVMURmYPuGYGjfDDz1Nkpa4BRhWZ0Wr929cUDvkCFv76K4I8FgKyQ8uRqdbv1EzIG-UcPWsie_lt_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2O3AC9LC_RoNFZH4dVxhIZnnhUZzeYB1PrxR4SCWNjMzk3j2Pbf6pSkzchm8IeG6ivDWL66DO1zyZtyZBj9kOwE-6qUd7Gqd5y7iEJ-aNOfl1bEKy8GtMAZjm3Ppb781ywiZIjlGXbkd5rTfHwlRjuPTTbLaE2vHN_TplajFYHn3aCmiWJdYzhlH1IVzjTRcO9H6JKqmc4snTDmXZFufFM6ffVE3XwUj5A_8Hjz-qJbRw3_QUDr3AWMBe-HZN0DBJVdqSNtsQr3oPtxRrI58XdI3_F8PqXOgjXlbM3YIccrv0PclcZHaEUVRBnozJsqna0qbjpHveDGGbFPALlm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLW-XOss-X7GSOCvg6eZLqK8grj1d0OxOEQsVuwm41NhpjxeFpjYPf6D7GqWs2QUzRJvoODSLypMdnjEIc8yUm_Es8hrhqkteX5n3ttQAweLxuufQz8p_p66b78kGYCEdYrOchPjOGcK2G0IAi7w9P4JCswTKy6M7swkEKUAua7_9fdSPUGZRgtWU7jaSCrOZ0AM7FkXOnWPq9dpoIFCeinlGdHjKMPolEkAGisaFgoFzJQFgwlXE5rXm1PKmgzKLT1hXweK8iFfFAa7RfSi9l5w2tvAwLe36h-8BG4CqSCxF1L9_fC4OsHR0FNWSj3vMYr87faMYtvVVL5fD3E2rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=E5igeqaW3ReWFrOQvFigXNkETSjhCOOwvlPhZmAdtR5DELuSBocK5gg4yCLHkRCVgAPOBgnsssaumz3CkKbBy-ugN2FC7sZBajwDPgrDW5QnsGjTAYVVau1HMp25qk7_4IAxlsvwrHUFWo86c9Dg_9vY-xc69b6txK7ZHAuc_sOw5G1xuMjfEluZnH4JWg6XT35EPTldTtVbgqALT7Zw3HgPiLapWNvFNjJNwT-kxjGd5NE9K0MOpxuuMEC-IdxQLd7AAsNugoUqqbpjC0ecDSZnIEn7C_7mq8Y9cCVTkquDqsHSHbGkMGmsRh1XWS6CXNUjnJstxaC4fg8wYKGwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=E5igeqaW3ReWFrOQvFigXNkETSjhCOOwvlPhZmAdtR5DELuSBocK5gg4yCLHkRCVgAPOBgnsssaumz3CkKbBy-ugN2FC7sZBajwDPgrDW5QnsGjTAYVVau1HMp25qk7_4IAxlsvwrHUFWo86c9Dg_9vY-xc69b6txK7ZHAuc_sOw5G1xuMjfEluZnH4JWg6XT35EPTldTtVbgqALT7Zw3HgPiLapWNvFNjJNwT-kxjGd5NE9K0MOpxuuMEC-IdxQLd7AAsNugoUqqbpjC0ecDSZnIEn7C_7mq8Y9cCVTkquDqsHSHbGkMGmsRh1XWS6CXNUjnJstxaC4fg8wYKGwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vp62php5bdm9euunRamC4xtdt11QguK_KQswR067zKicxB_Sm1CDrpVJ9qX8kBNhDckBxxgkP30gAu7I7bC88ramU2CH098cqj8Ev8cOm2WxSwG2-K8xGq_zUbbSNM9qA1fLRdasX4J0sum4zlhz0SmCVDV1EEMifRdzB4_4UoU2i9jtgygQzPWZGev-3ct9JoiAaE2MlOFC9rixVkzA1zE5q9byWuD7OpvU9573JqPyWkjSZy8flHxq53lZjGQtKEYmNJUotV-_870CpQp-vpniIOpZP9jy5a0CGfynMU-tob2OkqM6jznGdGn9TVIUISmuLvmwU49VVBFrX69TIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI4jLHKx9PoRWdM5wzVPTtS17G06xIK1NTZVg0jz_2wa14LGX0INNuSMs0-G8pBBsgE2eXLs1bUhlexm9C-G_iM9RKyjmMTVxorFqHD86wepY_Z1xyx_lPCfGBYystXqhUFUFsHhwD5nF2u1c7COKorfKPnEHKjVMD_jrCupk0hdLu1gVi_iQO0jdH7FrRvpyoZW5dTdCcuCxIqxipI0bRuqxecRfE3-VJiheCb0clXcpH6mhvWEE3TQxiUWTNtYpWjucmysy56JAFR6G_SshoA8H8Rdj7Rl3H_M6wpiA54yoUVrhbAZfRypfm0rmXODG_Ssi9jR8QfCk0DjYx1Kpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=MblpFr2SnWH3F4ZhSxbTnISWVYL0ZtAgAsivAHQ45T99uYa6v9SMQBVesc1HpjlAiivmdUboMD132Eq_3EORLFoDtj1zJe3gcCbrJc0uK6M1VTpN9qSdmOk3-hDQ_ZeqWIr0BRKdTvZJcs7ChaVtpuFDHUftBZZcPHiaFYGNhwp3wEeeoq33-IEs0YPR53qywUkl9YkGlqjBP4cs6KKGmztbLIPwcV3X9QGLAGllApUmhRujn6egGO9CjTycJXgenL0W-atBAFy-b3ypRM0n_2LrbaeuJp3PaFj3uNu23P_S3e7IZM4BA97wf7Cm8Ox-wCVu7USBxbhnQJd3a8n_bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=MblpFr2SnWH3F4ZhSxbTnISWVYL0ZtAgAsivAHQ45T99uYa6v9SMQBVesc1HpjlAiivmdUboMD132Eq_3EORLFoDtj1zJe3gcCbrJc0uK6M1VTpN9qSdmOk3-hDQ_ZeqWIr0BRKdTvZJcs7ChaVtpuFDHUftBZZcPHiaFYGNhwp3wEeeoq33-IEs0YPR53qywUkl9YkGlqjBP4cs6KKGmztbLIPwcV3X9QGLAGllApUmhRujn6egGO9CjTycJXgenL0W-atBAFy-b3ypRM0n_2LrbaeuJp3PaFj3uNu23P_S3e7IZM4BA97wf7Cm8Ox-wCVu7USBxbhnQJd3a8n_bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8aa96CtsWqN6rf1W5VQpSR9axD8KiC5X8nBAb89d5CurRTIUIxICRLL-X0bIef-EecJ4i5Ol3cdJf2THwT_U1xvim1b38WEz4aHSH2YTBkjW9IOzwbqtiUuEsRdk3k6AXx1gdAR43o2Xpx1HcJL5xPA9kn6-wJjv4pbQ31oLJ17AjhLpYXdu2eiZhSTU_chNB3rTb_9zq_xxCNIHxDWbCpIvicmlmXiUqgCX7YxliT4J_yjKf5VUY1qQeYMn0vZInkcoHXqzFgNSwr1BnIC3cG2PvITAhub-fk2cV2iuF9tol_61qvD8C_116M3wGdlkkd5FdK2F0vjskruWTfsng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4YK0lREWJARrz8_22garqw9MBAxm9fcNpYCqTLNessyaxWgTdnoQuTkNeF8ZTYayhzQJ6kn771zV7Yua8y-unVsUW1eU2F7-dwCQnmStWZKTG9h_zhywZOEMiNoBD7xJiylVrdjpW_PAwbYkbwaTAi9BOU6s57J7NMD23bzd8JftySUkhuxBdZop4yLoPtfSX93AK6H5B6IgxdNKy-rFpEXjBuFqLdjeUQtIeFf2LiAj-haSxz7R7dj3G6f_rF5nwHP_Rzf_VbPCqqFpo5OhjKNK_Pg_3JqBV5jlAmYg4PErUhXFWXxN3CoiTWh95tdQp0zk11Y3NHvrOIf3mZxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6E6s-gJgfAyddAYhopBWkTCRvtzHEwXnT1-MaGpuqf3IS_JKOQxSj1hCWgXfcYnTkLhUfUXklyRSZM2MtworkexFudJaGCq42dS_5KSdBkhgRFsVnxER3c_q8mh5UBwcsJMomgrhrj9cIainqz2z092MPJmCIRA7Je7wW7Ge_4ch0ChqrykMsv5qXliQHaPFL1rJg5uHDKKL2ekHX94Brh5ZDFCQbI0eaeQ9aU45ntlMATIAVjYBHYBw9swc-oL4Yi-Id3BP1diyJ8EggjeaDUdmiwDSkegXELkJ4cwZNTadkcyIj97rzk313QyK5oky1cW_2rZRhcfo6-HZ-WT_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2Q4-2pgnH5excs7mUenuHlZagVhQj-DJE8OBitTZ3o6gaAWQhJ5t3jBhaXUGT_ZwKSGWv--OTdt2NGA6twUeGhwskjxobQm0fhfq8QnDjJ21LbkMpmSJOFq7HwidS_-cmLauGmHp3eRjjJESHGqyrIwl8ps0iLkcrixubk6yIjFsfNgbgubFdLA1t8tfKFfRA3TnviURQy_AZS96Ks3SwME6FCwR1FO0vOntPp3vfDnXbx00X5sjGQyv5NuAdn_FHyDbqoeLkO7Q7JMnNrr9TBGt_josDk83M2QkxRrNXwnuhUOP5AGh3u0xfRi9yXjNY3wDfr3YaMQUIHfQD-CKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aN4yVnak2y1r75JkVXtZi2FPphwRZMJ1NMNhyDDAJpRyyWxgdYXt3FWgKYI0famq-RPJkP3J0KNj9whaNm6QcK68KkXLWqQ-46Hy-1gsQq_4pDyKRVltKrtB5txVhNNHzE2H9JUYG8UEMm433ontkkHUZJtiNyoSscf6l6lf7OToNUYIY4L4s07KKUM_rTiklXR7UgC52Yl3eBO5-Ma1NfAA8tJ1002FIciwwDzd39a5VrfXgCMBytPdnKkHA-Sj0TvEYrSRZjpoddE_UOP43AiSdzioKHw_YIW7ubfGao3r1O_PhUoiNx0tDI8UHhF3QcuaOACH_LEC-ghmG7HH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MfOAVrpd9Bhbxcp09Q3GWAXxrrgk5PlA450znqlmciDfUZusUPKvdKouBTbpFd7A8lpYjnAAHz_iZHZCLFsQ3NYZzXSNEn1Ae01b9jZtDuhRY6cYfsCCcOowHD9hWyLa-GbRLAxA2VwfJhtFSvHcyOWhPj2IamoeRv10AfoLpNetiSCIvb-yg73s2ALf-I_PysBFjxlJI2nDMGZE1Cy9JBt1nakf4Rdev8SzfgV7AOSImIOckBRLC7SqDYtyXQgk0k1OAqenn3JnIAtsRFT5kVbNQPqjqFQt6LqsT81CiDOyi3hnNSWbPpi_ndFzD3fKY2J205g9qpVHQZyVrypGoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=GYOzQaLOt0d1yexC9wbUHWIXEo7EPeC3z2cK0a4JEgWxAuPbTzu0hj7P4yhnzVdo1SaiFnUaPLFd_ZLuWimCp2S4k2cukeloLHY_ACmyRjK8jV45-ziTwMz1yuZ4GqtfxCWzi8N5BZ2Rs8_-sU6jxi_ZWRhHFeyczoqO4astMq4w0WjRPhiMnxxm9SfQkf9Kf71bg1vRvFl77gd8IgaSJpqwC9PYgJAANYgpTlEfvrhceDFIspHTMTI-m9ST-OAfIVGzjCtdasZgbIi2dJEusCUe-mWRQCT-SWmA5wwahXvvX30TONaEkIJ0ha0VG7ZF-QQ3VZMuXC4kEaNAMX6rfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=GYOzQaLOt0d1yexC9wbUHWIXEo7EPeC3z2cK0a4JEgWxAuPbTzu0hj7P4yhnzVdo1SaiFnUaPLFd_ZLuWimCp2S4k2cukeloLHY_ACmyRjK8jV45-ziTwMz1yuZ4GqtfxCWzi8N5BZ2Rs8_-sU6jxi_ZWRhHFeyczoqO4astMq4w0WjRPhiMnxxm9SfQkf9Kf71bg1vRvFl77gd8IgaSJpqwC9PYgJAANYgpTlEfvrhceDFIspHTMTI-m9ST-OAfIVGzjCtdasZgbIi2dJEusCUe-mWRQCT-SWmA5wwahXvvX30TONaEkIJ0ha0VG7ZF-QQ3VZMuXC4kEaNAMX6rfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUMLhNjdbe731U7KwVKv93w6G141igEU0gZZHBliM-lgV2jm8NH54ZA8tqvwQJmvPJqlNOhebGyAL9CsWwXLb5t_aQJHoycDtydoGeCNpIr__9v3FI4LkwrCnqhqUly5N8Ee9nYKJow3NVOg575VuQ_Cv_RcxTUOJRfZJDbrDXX9IMpZwNTXZpDrAcLf4X9VucJQ_YsaiRcjn07oeN3I6-EiYZXrWPsv99e0Qbh3tl0AnP4iYPKCyH7Q5wOnOfGzdRpcQXkYpGdGioHX1_ONELHrrzlfbiGNCaeDh-a9NcAWQA-asT7VpMsrF19w8om_1SDrPki3gwNCkK_w4fSiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwchrsYU5nCUa20jNu4oFAQQBsVEm5-r2X6nIO49zVOSCpkGX7iASnN8cVX6e3oRNgHvvLajyCn8hnqwz3QLxT_mNZPlXRypw6xE552oQo6bNox2WIWJfISWfPXV2-I7CQf4Zjt8z4HxC74iTJuJuONzYw-9NCIOS3K852K0KkQXe-Ww_Y8oP49Eah5er0F_IMktiSXUV7UCJiiyh7roqr0QCewZfSW98SHrfaU7nTbr801LomFvTODVQ3q1z0LVw7SUxTvJiU25Umuyc2pArX50zQE3W-PIMIQt6FGPpT_bouWRx2US_itibie7iTENZ98ndgb3EhDjlXZ3w461LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=Gb0Z4oX-GkSk4c-3zhWcTwxuoh3PKLdSKVvfzFOl_1rEfABGhX3wB14hJMX6KrAKrsd8u_ZKMkBku3jfZxiMLHKbsVIM438XbLEypl_1PUl5eQ2oeiUaYJY6OFymkhxq6HOBgI25L2Wlq4MChg745rw5d61aQf7SVFzj8dLColRuE2AVqdLgGTlRh47p6J8OQ0Hs1d0RtcEnQhBdsB4W7kU0hPVYDBnfTG_ZMbdhOWeZBNzvTVdATqpeO9sh903W65J9AyMo7xeAteEQU1v2j_XRpQu2HEIr50HxrfZkapf_KCXwpaJrbw86XNddBT7i1Z5iSvshJ44_l5tVOt0UcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=Gb0Z4oX-GkSk4c-3zhWcTwxuoh3PKLdSKVvfzFOl_1rEfABGhX3wB14hJMX6KrAKrsd8u_ZKMkBku3jfZxiMLHKbsVIM438XbLEypl_1PUl5eQ2oeiUaYJY6OFymkhxq6HOBgI25L2Wlq4MChg745rw5d61aQf7SVFzj8dLColRuE2AVqdLgGTlRh47p6J8OQ0Hs1d0RtcEnQhBdsB4W7kU0hPVYDBnfTG_ZMbdhOWeZBNzvTVdATqpeO9sh903W65J9AyMo7xeAteEQU1v2j_XRpQu2HEIr50HxrfZkapf_KCXwpaJrbw86XNddBT7i1Z5iSvshJ44_l5tVOt0UcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAsKBK1PHWjyjlhQVRKcFlODcSM8aAsmHcP9YOYwxikeTCrKfE-1HZgy7fgGG0h3p7hie74Hq7BZd2xIcCyroyPTuCvv5tMW7_I-8ZvFKl8nZYERDUUTR8cFiBZ1pymUglwsXoQtTZ8bD9WLo6v9Ozemc6Ny9I_UE1Q6bgx5xbNQgSeX3TY8E7BTQg3fS2Ie6nXuALx90aMyV4bxzCXrpA-UfXC5rHLv6SFzYpeNl-15cQaXlYdCAChMgRcIRZp0_dWeGaKeq5yjahtthHRksnHthdrUun3O7ICeBcyqajKRudrZOgxtVfP61Bo0u1pme3FAf-wCVT-9exF6D5aKjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Le3cH0mpE1DRc-jGVdIbRRy9-rGX7ppD2ktdhSzjXB3JxEBLeKQ46BYIIsUEWlUZlE1WL1VPrKcS5I9ypxz8SH6u_WoZ2Ui5o4DYHLKrVTR-zcYt0pZUG-oT7WpGM6U88KvvcSMZ3VzkK3r2uEz0r_TAKE_gTzopOZqJ5CSI75d79UyJZziPkvj30cknFL3OFcdfdkUIFjzfB4TschhBAD9tJZjzbMaNttS8qUApoFXJ7w9O1Kysa4BGzOYYYc1k0oCQ8gRTtFke49qQuvrX6el8yGWayWgqbzhv7vmocyrxfa4GUzZsB9a5qzpBnx8guMh6j06j83c_dFpS9ux19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZaf0yTnMsxcdHZ1SaAymQVC0Ro98cM81AYETgjlDkBBDwANLV0x7I2k5_Msq3IFt7hsg_BwPRxVg0FtR0L_lbbFQA99gnLFCiNHANeyFo-lmrZOm-gp4dRHL42XZ8zav-z98PcOdAceaWDu-ZgcPvr0z41BQiYZd63kb6mAMiawIMJVjugE9qPkzSbT73sDJVGEU482Q5AD9HJJVCQZosAvggaKX-_oix-1IYrhlh_2-DjQo4o6hPxsz-tGfnM4HdHn7arFTjX0D0bWw2PQqBzb15MpNlkLjiQ5U97VBA1afjOQJ2pxQfQdPO6m8pbRVGQWzU-jbPedDxu85ztDtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T94xm0t4gERPndFE8dod1CQ2oSxA06wLEj58eD4tuFcT3UHn-pEFQ__vs-382Boib4QoDX9eX89yILUJzmDGl5P5y7jw5dqyMVtB0fIxoeT_2t4S8vb-MMtRdaSGYYaa4D9Xqc6Brw_l0LE1o3PqQOMkmmucS3qpjNf9KLrB_VrRIzBB-jCHja8ry_xJWnRFyEZXwg3Cjei5exWSrjxCMbP1PayA6UCHY2cQ5ltJ_U7lXuDsjHecChDAYvNniYGrKIV_XYnl6uUKRC1tzZhdWKHeXGoydeydyUGdDioQ2yTDnboclnR7vRbBZCNJr5alVevzDAb6VWigH2qoeGWIMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ0OS60jsZQ62kBz6FPQZ1Z1a9xlXbPk-V6Jm7rqoy7CYmgDZ2pIZgY9_a_1vbBjGT_QCO4_XJNz96jpB6utaf-9lTEsB-R4Knzsn_jbN0fDWI4jtr5Iw6FVZS4n1AgDQYZWDsicPMc0dM8omrr2gMTmc1spSeHbioxunsYw92424oaYCl3VgDg-KAC2F_zJ5qS5jknJDE3aeieYW1ZARxmer-5ODuHJAnJqa1RvbNU5fTybmSnF4iVf_7hiWjNe6tbZ_Dr--DhOoeC0hcJyKODBIrlJyPssrqNuyp_UTYI5ht6zsrXe2lBkU_COTNVAxnR9ElqJDaDJd425oYkehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=asNPzyQ7ClZ1yVq-EpimO-AtjSMNRFKrPvjUqsF8hPKO9apG2UnGM22npITnixFe8v0XrcJ6V0Ot5CybK3u7F1DQM5vruNbTeqeQyU_1Cb_H395WIFUX_puf8oKrOLfOxysKbQGRi22ejXErqMsgMyrleZueDXVza1uVRAOI6IC8RbZjQE0HHYlHqDqy1BrUsZ9_M4mdkK27f2uiSynb4t6b58kIRh7QT6dY_EHTGJlBNboW2_J2MbbjbhCx7kzXg51QOfU2JsdAEqemXUroP-Gd9dbkEH0gAYovwESiZ320LNGboTc-WLAx8VEROQQn-z9NCRBf1Eu6vVdu32fjoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=asNPzyQ7ClZ1yVq-EpimO-AtjSMNRFKrPvjUqsF8hPKO9apG2UnGM22npITnixFe8v0XrcJ6V0Ot5CybK3u7F1DQM5vruNbTeqeQyU_1Cb_H395WIFUX_puf8oKrOLfOxysKbQGRi22ejXErqMsgMyrleZueDXVza1uVRAOI6IC8RbZjQE0HHYlHqDqy1BrUsZ9_M4mdkK27f2uiSynb4t6b58kIRh7QT6dY_EHTGJlBNboW2_J2MbbjbhCx7kzXg51QOfU2JsdAEqemXUroP-Gd9dbkEH0gAYovwESiZ320LNGboTc-WLAx8VEROQQn-z9NCRBf1Eu6vVdu32fjoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPcYHOO_YQ29Ccxdmuxjo6afn8PDnFgi-MAuAvXimIOCq91Cz1p8yG84hXjFNEdKAp0dTThhGznoKLLP_Z3x5gTg2Yg6IuYEzj7LrtbH0KlwLqRu_eDkvTE_hfKvjePu6NVeyV3IIBrvWvEzwEW1fpliBnuQcU8yEQkdLrq0LY9UK2enDxkCl92t_9Ak0dj5XZK7JMMP4rPfheMAmtyJMV6LiMpFKsNHJ8HVbBTcJJAxcUlx7ekda_ZPW5u2VBuW3rHY8Z0LjLWk-BlXTrTWJ9vOKShkfn7lEg2_7_kuw9Cc8LEWgsvAZNB2QICE_0nrrYhWx8BBd7DRmroNjWuy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEW_enOEP5j7G5655kPELq1K3WYuYoSUcvrQOOoehxkE1IAikVssCKJ3cm47vvFIWKFiggYdwWzEjugoCo8zPlqcZqPVVN_C7meSQqC63jejlkmoBjuEnB7ZeD8JyCwUD_dLx0jptfObJIbnTdOj5pKT6fNQPCdw5sCoGR-TVwN2TtI5g_2Z8_XtdYCbdwh80Ai2Yjw047zulwSSHlwcYk3R-LZogkyzljLp3Zfu6_yJ3AkGVL6I3dKOzC4XQKf4NAqnjGd02QpeUfCZw2XtGsCL_ouTgmtOyLBtdUFoqTtT3YV2V4iqAW_Ua_-3kDekxtln3Fb9pG6V48X-WuPzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=lwMspWhKCmZlVWKwvcpphIQE5NzlcesQyWzzZIgIkepTpyMLOqHk4bZEnFiDfm3lTjcG3m665tICOzS4rxq4-4SMCbXxOB-i8oqcEvrUFiAIBjcIheq-8pBEUds2Qy-UvijzXWQOqB_lqx1MdabJ89-dzllzJNaQ4HPh8oz-kxKab6yPMLkHXgf5dLJJSoPMpKf46ccll34G4VDDfvztz4FanZfIAvoWSpIGVxNRHr3-g0v-x5Cflab2tL9NaldWBhGtuZRtlnj7rGca_dJzOExf9lTncYVixAVm6tX87jS2VSr4ZgIS8BA7Cktq-Ggn6xA0zN98pk0yS9tQrguCaE2--yy_bWXt-mhDKlzAbYgd__2Xd2hmKVIQrFm4YmDK6AztP7uSmm1a1N0AAnMIhGizE0hMiZqGZYpS2T3Oi698peYLiqFSwTryKn35hjay6Y6X9DSuN9D9hDfAtX-4wLDb9MfSJ6D_ZgaKUsiuBDgH_ivpAFJRnEXaXChpLTeM9t3TUIh6c9ozMvjQuXPSYrpXTO56anIhH-oi9ey4U_I7Sx6874-VCaKH0LRkfh4IbHTmfTQFtbSv4EA3jA-NFJ6tXtq2YTwbj9xDfG_rwy9W5hFs6oFYuo56DGufgFkOGjonKJKwo3KlR1tDE1zDNOwJSbGP02RJzSfUj0qTVkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=lwMspWhKCmZlVWKwvcpphIQE5NzlcesQyWzzZIgIkepTpyMLOqHk4bZEnFiDfm3lTjcG3m665tICOzS4rxq4-4SMCbXxOB-i8oqcEvrUFiAIBjcIheq-8pBEUds2Qy-UvijzXWQOqB_lqx1MdabJ89-dzllzJNaQ4HPh8oz-kxKab6yPMLkHXgf5dLJJSoPMpKf46ccll34G4VDDfvztz4FanZfIAvoWSpIGVxNRHr3-g0v-x5Cflab2tL9NaldWBhGtuZRtlnj7rGca_dJzOExf9lTncYVixAVm6tX87jS2VSr4ZgIS8BA7Cktq-Ggn6xA0zN98pk0yS9tQrguCaE2--yy_bWXt-mhDKlzAbYgd__2Xd2hmKVIQrFm4YmDK6AztP7uSmm1a1N0AAnMIhGizE0hMiZqGZYpS2T3Oi698peYLiqFSwTryKn35hjay6Y6X9DSuN9D9hDfAtX-4wLDb9MfSJ6D_ZgaKUsiuBDgH_ivpAFJRnEXaXChpLTeM9t3TUIh6c9ozMvjQuXPSYrpXTO56anIhH-oi9ey4U_I7Sx6874-VCaKH0LRkfh4IbHTmfTQFtbSv4EA3jA-NFJ6tXtq2YTwbj9xDfG_rwy9W5hFs6oFYuo56DGufgFkOGjonKJKwo3KlR1tDE1zDNOwJSbGP02RJzSfUj0qTVkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS81l_zNFgObWoj-3rpHRY8YPZZt5ZgICqdVAbQ1XhNhBBZLnZQfVuo62GqCx2VgpTPSBAGuEtN5QnyISiuys8GF8Q9wkldjUhf1s5WUkyrLyKmfvpavCO-Olx2mcNGpCzAnr_4MhAxfXdxUb1TSNfo_qXGIjRL8JTMjZO9jxtO-JgfSogvD4s56S7NpuHDWa3I68ObMdNOPmZ4YlE0fJWSXOa5xQiRGaDvIG4QYZDTnsrog-5-TiYbfYuqKRyPoAO05nGmdrDbSj6Rd-aLVdxp_ZOGTqX1yiMmnLtf4A73ubYLb29OWBz5LV8VAqJlxwlUV-AnfSUmeynlCds7UEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dW1YiaLDdZ6i4NEPCRMp0b7RGs6KJqdk361Doq7tG49Bagb5r3xvdctDtp6HNCKEtQpEYSeu3k8Hu6lzHZ-rI-o1BbvWp8binynlS1acJpLCzP1JOw8Pv3dDoDODzUqEZ4nO-ozQlETy_xv2a2QHuBX6Y0ewf_8xR0JwP7K34puru2oIglFZxyYn3bpAzCikda8AGCBM3jqR5aAhRCOw9X2EdGqfYGc6skrTJDpPcmncno-2ktqwfuGXHst59lmix7wXiZM44IGkPlkfpxzQnUbllkBnVYncYso3ff_7YrIiInxxCPI3WFbYeXiJcItpnrz2crI3_bYmj_WulKGG0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=XLsF3pkKT4YwVWivYpV_nByE7LO9E4Gvo2XwgXKM6de-m9GtItnPg88Cbtnzkjt5t9LJ8OTGiAa7LlaekRN7eGfhNNKZ4vSEVEjknMlJqhJoMz8OjWZzCaTURdCa1gN-UVIsmxIi8PSlknPZqKip6mTbfChFY-2K0u5Tr7h5SlAXE5HDAVqwbjrGpGvXJtVRJjZL6xDSu0ZwoBQEVl-POHdW6ljiVCKN0I0xwKqu7Fah1uQ8gomgt8INJqWA1BS4LOrhonsZJ3gVCnKhsqtMrLEl12VkIoQN6ka31EWhwLhh8Agz6PWcvmJqS5tPVsjYD-KNNq4sAsY40XhkBAqCpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=XLsF3pkKT4YwVWivYpV_nByE7LO9E4Gvo2XwgXKM6de-m9GtItnPg88Cbtnzkjt5t9LJ8OTGiAa7LlaekRN7eGfhNNKZ4vSEVEjknMlJqhJoMz8OjWZzCaTURdCa1gN-UVIsmxIi8PSlknPZqKip6mTbfChFY-2K0u5Tr7h5SlAXE5HDAVqwbjrGpGvXJtVRJjZL6xDSu0ZwoBQEVl-POHdW6ljiVCKN0I0xwKqu7Fah1uQ8gomgt8INJqWA1BS4LOrhonsZJ3gVCnKhsqtMrLEl12VkIoQN6ka31EWhwLhh8Agz6PWcvmJqS5tPVsjYD-KNNq4sAsY40XhkBAqCpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=OtWQE6ytYz_nELscYXtEqNxKguf_OED9D430rhtsMAU1bsnaKiXYPrVungnVV6z8w921Ma6xx1jQXfkNXZcmX_rlqI1OtZl2_Rpd3OB_OjVM-6hH5D-TpNx2D4nd_nFsP_Ts2ngcjEIVUG-BbyKHat7ME5X2TOl0BUPrJeh9Fox3rOcJFjD8BADJ_8aYikXmRRd1HXUa8CWkyzD2lDf9-5caBCAKTLtygORK8Y5ncNASqQu94w0Q02OyASyDwTD8QYYEmx32DApm5pVuG3b5f3ZgG9idyM3AQ7hmg48KFpu9NfP056d2dZuDjvX6GxqpRo6VAQ7kWKy5Z3YFnES0Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=OtWQE6ytYz_nELscYXtEqNxKguf_OED9D430rhtsMAU1bsnaKiXYPrVungnVV6z8w921Ma6xx1jQXfkNXZcmX_rlqI1OtZl2_Rpd3OB_OjVM-6hH5D-TpNx2D4nd_nFsP_Ts2ngcjEIVUG-BbyKHat7ME5X2TOl0BUPrJeh9Fox3rOcJFjD8BADJ_8aYikXmRRd1HXUa8CWkyzD2lDf9-5caBCAKTLtygORK8Y5ncNASqQu94w0Q02OyASyDwTD8QYYEmx32DApm5pVuG3b5f3ZgG9idyM3AQ7hmg48KFpu9NfP056d2dZuDjvX6GxqpRo6VAQ7kWKy5Z3YFnES0Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrCKPdwhRlNK380jTHCdgdWIWZkAQRqIBxIGp-GRLStFSJRQ_VG56g5bV9j6iq-jR0dm59CDEtPRXqVUyupPu0HQy4jwJEctbHrE6W11iRENeMxSUR2HWglPUwiHwu6D-RIZcT3DZX61ZNh2aZ6UgXA96Nx-yCox-7YqBS9_ivA_ldJMZM_ilz_gssLK1dQwqXNw0BmFX5lY20wxftxIpHxfpwqVnJ97nyFw4LiZ6xZDjwNE94Pv-gc8oaaYIPpgjaqbqoA0mIJCipikq0rCJKHHg7-qej9Q5eyT5K7IKnyVdl1XOSCIPsoXJeIbYlcg2tVBXRNDq2Td9XgSSd_LGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNbYQ2_zNnS_YwT7aJFRWDj7gBdfxnKAUfmCD3hyt06M0s1_1DhdLLiKdZs8UxZ5gIojrMprKhWj43tOeXs2Y7OwgVjsg3WvNrWWInAbHyyoeixTT8kYbFvd7bMQQzBYu4IVtX1RKeVymsg76I82AUiTkR55vrj2vmDVnFV8mFrPTbIbfWiakhDaCMalv-l2PCSeb2LoVcQ5GTxR-Dap2-UCt7oJkkKAivCyFruMKRna4oWG2FaPQzyBsBL4AdkwfI0SBmopWYAklSMydP4o1SWpjtfvTdK4QR2juyvf_HacX803dU2LSL0JE2H8-gB7h0QSdN2QICsJwSJGpnFAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
