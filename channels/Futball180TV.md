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
<img src="https://cdn5.telesco.pe/file/KdZubS7lfsRTbfAjkIXcZWNpnTocd6t8JsdiL96uR7uYqpQB40aC0vIDKoYCcMT_D9FIt7TuLRe1Wxo0P0E-VyYJJxQA1tGomU8q9Fs-jkyC6Leg3Uz3zQrTZ6Y_MZYwlxKsUfafeN7UChnCQH1CO7Ec59rUoVqX3uLJAKzeMcy9z9uuM2MqlGgzFm_SDWbdkATNrB0fCQJbJlI5rbnV4iSw_vIZM-l2lc6hQ8-o-qHYfhtYQzR6c1wtk-6Iz0Fmds9UkzRFaHgdVW8bJixRFyNE7C0_KwQPqBVo_Pbet7Ilealv2VU-YvSrqL64jQt558ffRFy3KmgGir8VMK1v6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 406K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-106968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh32ypLj425u0cgrpaMUtV5og-XS4Gd1u0xe2mw_sM984d1xICHCtyLTh85WtLbNB4nRuBYkowvHXa7vDgVRJddy0UNh_nE1wm6PwvYHfGjpqy6z1JBpHV2xQdWqJThPwOgcd5hviEQniT70xWcN5HxUdVDC9pRvLZ8BAemRzLwGvYs8DGNAvGDvFAKPtVTvkYT5FwCQqCVsxFwoAsQ80g_d-wa1vR7W350rZaKRo6le7BBPk71x1YcDajJ11BjBJJK_wnYS2BZudz5AVcB8YkoEKqWcoc3Ll95VpGcxSZ2sD3ldKftl7jrX3xwra3K7UDmCFbr4rn_Lok5oT4lC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج درخشان منچستریونایتد در پریمیرلیگ؛ عجب کسشری شدن بعد فرگوسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/Futball180TV/106968" target="_blank">📅 20:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b23f273f1.mp4?token=OWSgxmKYVCguHvfApVI9QfPXy7K0ZdCwfa9V6UY-IrKou2OdnliF8lELe18GGU5iVhBGKYcOMZPipJsO01S_C43dpvEeT1CSiQOE91m4fA1UtyeN89SkeBsStzZgZe97L6lwX0zsInRsDTiFAnWjIe9viA8SsA8fglOg1h7vnZC1qAIZutlaLjA_eQ7OT2x4H2qInvPPVWAKB9VrQZAZWvE4U4sgi401tL1A_UflLl_GE304UY8RMaNxFfkE_PiSbueljB4_GxMPHrcyBiMIQ2GpSuJZUAiX8D8TFJUjwQ56vrPFvU-9wVR3ryKWjqMdqw7LedYXWW1lD4mruaGtww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول منچستریونایتد به فولام توسط متئوس کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/Futball180TV/106967" target="_blank">📅 20:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kghxmY5iStH4jZjkWZWl8pZiNmtHEjgcqreSOxbdy3jT4vMKnA3SENDBWmh1YZAgIBzGSkWR2tbH7zS8W5rFXHEpYILd6PGqa4vU7uuURHjXpcTVzrxxGeteK59L0JPf4LqfKzDKjtp9wIcUwuYpVa-OygyKfqFQ1xotDa8kOSTM3qLSQITwhfB7EPsztxKOvpH_HA_su_lzwG6RE4WJeEFZ6GMDTqOeCW54J6yT3WTfgVR-1N9pVctd_f7MOvlnHZ31FKMCpYhTE_MVwiwScLRbEt061E3JPDwk5v2yjnCrf6siALw2hkwBZuEwu8i1qgjjb18ohiDYJovG4Rpmfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇪🇸
رئال مادرید Tv:
🔹
وقتی پای رئال مادرید وسط میاد، برخوردها کاملاً متفاوته.
🔹
لالیگا و فدراسیون فوتبال اسپانیا اجازه نمی‌دن رئال مادرید رقابت کنه... اون‌ها یه نقشه و برنامه از قبل طراحی‌شده دارن.
🔹
دیدن همه این جریان‌ها حالت تهوع به آدم میده... اصلاً براتون مهم نیست که کثافت و مزخرفات تمام لالیگای خاویر تباس رو برداشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/Futball180TV/106966" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34da8be998.mp4?token=dj3tIGBvB7kbjatfIbYEgbu6euQDgvMKrbfmbO1BMckjN7lzY9HWaA0ICNHCaPjZlzZNI4hefsWRrPqdTfD15ttjCQCZGN1WF5sHknuwY573xnMR4dIzGmWFPzRljB3pH8bJBotyGmP6G_n887c9C54xX1Z-EFqOtr2NJLInfXe63zeTGPPIIgOgZKJvRlPXCQ2CSoDyVZInb8ZVLHkRuT7p8boYVFMfCsbooBeWGElINzFK-ivw0MHUF9MA6T8i6fP0fH662L1bsrWjkkkrco2967X0nSqOtLxUIJwZ4rkx1u35Lzel028QDXUzulhZQy_vgDmL8cHEZP8azICptQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
حالا که بحث جنگ دوباره داغ شده؛
اگه تو آسمون یه جنگنده دیدید، سعی نکنید بهش شلیک کنید یا سمتش سنگ پرت کنید، فقط این فن استاد رو بزنید تا خود به خود به آشیانه‌ش برگرده :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/106965" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=X3isTsXjAh9FXdZO55seNUv3uyNvJpKwYrfMFfBJpn4BZfFKhlkfVgUAzkP4pwrY4uDocwU3YUX_GQTcQLvRlSSDMSkoVVVaTf0vkqbIKiH8uqVtTud_hOYVcjuxSBHctih70WqyuJ8HWoi-YLEMGS8P9OXthdFhIcQ29b0aCDGdNbUe2ajqJRxJBtRyOe4VTJcjOi604jnwU04QIbDL9YR0P-qqlnMMCyV5SgQU7SO9mhgVEEgQHdTBGHvblWE2-jXwiwtKoVbzN3jkPQMnZhmEolQssjpwcGuwR6y3__ykMZXB9rWcL19ftBznaJPRwfFBosOq2TWY0eQLaeHafWYZacMUMRpEOz5tDVbaHdsGx1D8OLtCFA0H86GkA2i6tO9UM0qNRJkbTY78BfF0a8IdpgMRed1VOssUd1sBCtcJRBikJ2gRo9133MBPcGTSVlyECAc0tjJYuzbHVd8slK4v2J8Ex2TzD1WW8C9jg5MTGZVtIUTAjPRUH4fk_Ag5Kcde3_FPQd77FyqGAWjfch7G1sk9SEU_UsFXNqGlY9jlgapc-eI5rxr92R4uCkO7XQMiSOZMehbHLCENk4tMZveZxWTy2TTHQXr8oJBDZUFcUE0E9o8S8o4Kx5L7TXsPtgAXfCMsKqnIy8pyIfLCXcKkoOgPml02xTQFZrSZrZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cd75fe80e.mp4?token=X3isTsXjAh9FXdZO55seNUv3uyNvJpKwYrfMFfBJpn4BZfFKhlkfVgUAzkP4pwrY4uDocwU3YUX_GQTcQLvRlSSDMSkoVVVaTf0vkqbIKiH8uqVtTud_hOYVcjuxSBHctih70WqyuJ8HWoi-YLEMGS8P9OXthdFhIcQ29b0aCDGdNbUe2ajqJRxJBtRyOe4VTJcjOi604jnwU04QIbDL9YR0P-qqlnMMCyV5SgQU7SO9mhgVEEgQHdTBGHvblWE2-jXwiwtKoVbzN3jkPQMnZhmEolQssjpwcGuwR6y3__ykMZXB9rWcL19ftBznaJPRwfFBosOq2TWY0eQLaeHafWYZacMUMRpEOz5tDVbaHdsGx1D8OLtCFA0H86GkA2i6tO9UM0qNRJkbTY78BfF0a8IdpgMRed1VOssUd1sBCtcJRBikJ2gRo9133MBPcGTSVlyECAc0tjJYuzbHVd8slK4v2J8Ex2TzD1WW8C9jg5MTGZVtIUTAjPRUH4fk_Ag5Kcde3_FPQd77FyqGAWjfch7G1sk9SEU_UsFXNqGlY9jlgapc-eI5rxr92R4uCkO7XQMiSOZMehbHLCENk4tMZveZxWTy2TTHQXr8oJBDZUFcUE0E9o8S8o4Kx5L7TXsPtgAXfCMsKqnIy8pyIfLCXcKkoOgPml02xTQFZrSZrZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول فولام به منچستریونایتد با گل‌بخودی لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/106964" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyjIsSWkrT8MEemGwQtXUPgiMsDvlJCbpg8LJ5-BAr-6PvAp9hhgLOUoSQDmwS72x-2WjFibeT5TnXWLYzWpyIp1x8_umqc9FW58Ay3owzbIb5CfvV-GOvCGkwLAyMWogNJdnw7qajNArEbHDmnryJ3Ew_-I-hhk5eEuU7U6CT4YAyK9P-Z-qJzmqdq5dQhyWE3MdRoJ31ZmuEsKFtV8twgxh7BeMxtCxqqcKU6nYhZBxNRv8thxNAlpSKyguXIvBAk6y_ZwriUQnUGTvqjG5hKAQbRcZgFhkGZ9zrPgcGSuTLvfjbVsMiGFyQlR6P-obSeUNsWWg8jN8OF811w_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
خوزه مورینیو
: به کمیته داوران تبریک می‌گویم. آن‌ها باید از این نتیجه بسیار راضی باشند. همه‌چیز بسیار عجیب بود. بازی باید ۱۱ در برابر ۹ دنبال می‌شد؛ چرا که اتلتیکو از دریافت دو کارت قرمزِ مسلم قسر در رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/106963" target="_blank">📅 20:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKDFhWimLVqIUDHWeV4bZD6VGJwOWbw_Yf6gXzVoDKYwEydsyWm-mzoVX_B4d_OtLSCUnEwcdJlAgRl7HtAC-jkthzpjeGHopFhmnCp5toEw3sfbWSw37TYTUaLkganb0LmL_FLwIHX2VmYHBI-6lXZIke7WFbEVMd-MdOqIBvTLfqn1fDvkms6kBo38A-XKU1Usd30U_2dtznhUF438TYrLjgnVPkftDXhmvfMyswT-7NLsCNzqq-dG6HkP1kGVnVNTpTNgBE7dDKNYsMJ6q92yQSOw6B2C57LSOrdCaAYPtKPGqzISTAlFt4s_6NHhcl56wvssOGD3-Y8vfZLLyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رسمی رئال مادرید:
اورتیز آریاس داور بازی، رفیقِ لامین یاماله…
😆
😆
😆
😆
😆
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/106962" target="_blank">📅 19:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9TyQCgZqag6oAxE0aD3izFTCA0EEQKkgMCfX7GVFkLkIgY5dJbnxNa872W4qHQ9if1HcH5AibvpPsfDfoWt8Y3hOjRcI_Ct8dJH6pXYh2PNiQRIXVeJuhEPntoP-f7tOj276oZscL4MpUVXwsns2SB1Gm2bEb1-muvbsbyZFj9XmKnCrGtsKVgVzjKFM5_GVkoo05KQIDWZU4MvodTaA21cYu6lK8QG1jahSDhMNnZb1pTsYcqiog6adi63qL_YacXqe4nW9F4_rGXfdVyH54AOycmZ-IPNCSPdDLKPPTt487FYep_tAdf62XkTEWaGZekxbcZJZl__gMgboOpL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/106961" target="_blank">📅 19:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3b_VN5d_ii3YEkXqhCOtjtwdk4Yvu2A4H_HX1aPIgW1Rjj0W_-A0knz7gdkLGaTi928fEU42-MmyZXx_oM7dAVdv96qmzz0Psv2dVIqnuQXVRzIRci-MuMqyu0mfLAjMxwiR77OuUZV9xTNhKwSekX6ybZRhrnSvLdj8ePmvdxs_CvjRKng7ibg28vjDOtoPhZTum2N4WcgecwRQ3bb8Oc7EvtWBkOJlwsgGadC-ucIQA2DjFE5hpn-ZQGde81uc2ui8aBF6ZJQAXN6xtpoE8yXPMOXwPX6z0MrryETDi6elqTXT_TSDP2CidI1JXUto6QDFdp23pp4n6x0Fmi_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/106960" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCjxrM6C20cGXVeLgtD2gL_8wVALYnYR1rChDrFSMnpG191zveL9KXUEfQoVwTyGfAfvNIOPUk-ZSst1xCVGpPXTQWYx9nV2JnidqJHYa-0KzEEuQxR7-DygCohT0mTALg2CGSGVXOrgvs7dj4FvaQ1z_Y8krrcNb3KJWFJ2kA0cfJnmXfcUuttbluUcDsSwoRrq8r25_4S_dV6c3Og00wbEfPvEqY83A9abm46UqGunzOx3cs_oIQqBDZBivOBXxRTfF4hnkdNoahuSY7zbY1vgxS9MqYODfMmijpt8vujAF6YqtzYzQ4gWeMAi8b-0Z82kXT-tsNbEGSmTh20Mnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هفتم لالیگا؛ دربی مادرید به سود بارسلونا شد؛ رئال بازهم شکست خورد و فاصله تیم مورینیو و فلیک به ۶ امتیاز رسید!
🇪🇸
رئال‌مادرید
😃
-
😀
اتلتیکومادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/Futball180TV/106959" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/Futball180TV/106958" target="_blank">📅 19:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دقیقه ۸۹</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/106957" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رودیگررررررر</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/106956" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رئال یکی زددددد</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/106955" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/106954" target="_blank">📅 19:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یا حضرت عبااااااس چه توپی گرفت کورتوااااا</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106953" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اتلتیکو دومییییییییی زددددد
🚨
🚨
🚨
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106952" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106951" target="_blank">📅 19:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=TG72Y5Dfgr90mu7LVtyqu4C-WorrulQI4uqQx4rLSHEu4TAKnGJH330VZzENqNtP5vY50dTr2ynS06CzRW16yVZjEFaTbFzwhQUtv5mgzlH74ie3l14pxc756rH7jE2jvbRJykekOdK7Qc_iaOTl78u204Ug6K22hDkzDU953kXxQzKEFQwKwsfFSuhdNsh3KuqXJ68bfldJxpI5YzXjN62hgpdnstkyElqpvBslotfsDKWBtJhJhzPZb00glGdGOdHr9HTdlgjgerhbLU1SzQ6qeHIsqhMjRO8t-QyPPq3Ij2QIa6cAwGbYVr0U4_3vBVVvEGEocODfqUvJdrbxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7be2074ac.mp4?token=TG72Y5Dfgr90mu7LVtyqu4C-WorrulQI4uqQx4rLSHEu4TAKnGJH330VZzENqNtP5vY50dTr2ynS06CzRW16yVZjEFaTbFzwhQUtv5mgzlH74ie3l14pxc756rH7jE2jvbRJykekOdK7Qc_iaOTl78u204Ug6K22hDkzDU953kXxQzKEFQwKwsfFSuhdNsh3KuqXJ68bfldJxpI5YzXjN62hgpdnstkyElqpvBslotfsDKWBtJhJhzPZb00glGdGOdHr9HTdlgjgerhbLU1SzQ6qeHIsqhMjRO8t-QyPPq3Ij2QIa6cAwGbYVr0U4_3vBVVvEGEocODfqUvJdrbxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکومادرید توسط گریمالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106950" target="_blank">📅 19:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اتلتیکومادرید زدددددددددد
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/106949" target="_blank">📅 19:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلگلگگلگلگلگلگگاگلگاگاگاگگاگ</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/106948" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دین هویسن اخراججججججج شدددددد
🚨
🚨
🚨
🚨
🟥
🟥
🟥
🟥
🟥
🟥
🟥</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/106947" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پنالتی برای اتلتیکومادرید
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106946" target="_blank">📅 18:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
کانال رئال‌مادرید: وقتی داور طرفدار بارسلونا باشد، چنین اشتباهات خنده داری کاملا عمدی بوده و پرونده نگریرا رو بیش از قبل بزرگنمایی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106945" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106944" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFjCg3MRPFQA-XZYsmyzkNhAXjx_NPyD9i8IbKAAC8vj2SEGxv3A_Qa2iG0I_MgODdcU1PtaIHP4EawDiStXPwAR-ioZQLwZdTXfJ9dCkywK3dPcpBs-v30THcB2Ywu7-ArPnzGe8wDi7FhDIlnIZqgIKGdSKMlAAqqfSyyl52MOEOlX0Zn7oUXdH-gKpNWwqkLschzWWjgrXoIaWtJPaWSUspfHXoiuVf33XsZluYkBe6y5doskT4Rh4tKDnbadxc3lH4HsWygF_66xZaAPuP-2jqoDOzKHDnvy3JeeN3_KvzB2wwTJdWljbgg3kjwUktJ006FPz8LkeTH0j8XzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106943" target="_blank">📅 18:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV71cQYXwXjXfbms3096YhIfW0lSzWRJrJGhbOGJmHw8y9G1lUOxIxGQSGae8vO5M4VeuXzq8szkmHbcZyRfaFxX6OlkkK2bptcyWlwrDueTaSktTzPABYeeMK9vyTML989HWIfDAMp7prVcwnaEnN4RTRsZF3AGb6Nmrxa8cDdQBv0FXhFmdCISipXzxkwOm1IbF3-dNosVfq_MJTvVh5yCsS7XHDctQdBxgvJ86qDnHb63oUnTA0V-ynrra0d3EMu-EhRE8ncr3luIDCC6f9eIiNUtlBNaws81FdvOCn5wiAwunRIxlOciaklGguoZ6Q9wa3zRlSZQ59CPzN9Rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با گلزنی به ساندرلند؛ ارلینگ هالند اکنون مقابل تمام تیم‌های پریمیرلیگ که تا به حال با آن‌ها رو به رو شده، گلزنی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106942" target="_blank">📅 18:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106941" target="_blank">📅 18:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brDLFZi19NhunRRJFDe1I_o9K5C2UjOloB4OA67F8Hf6ciAEDRPocmkj89nZaadKbziBJJplgENoznDReR484PL2wmJuFMfXKGch8u9H8p75QUZstTajUK4rlJlzzWyy_1qQGQxy2tw_0DzRcrFBk4tvqp_jodkolJqkiwebhnnfPxLmh-MbZvAlDZ4jSGCZgLKpHxTpD4e0mjUNCNK-E5nBf1vPoy2J_yNCeLBwjxjnBdKHsgyW2V33hhaUImAWH8GPBcXMtnv73Uv5TcIOLJdhp5g1sTa5wGw-268czx4Mc928WRp3M0-xxvJj9MeLZE6iGspHqCLCgSApU4HqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
احتمال اخراج مدافع اتلتیکومادرید</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106940" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتلتیکومادرید دقایقی هست رئالو لوله کرده
😐</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106939" target="_blank">📅 18:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf562p7dtZAkCy9ZtVdUMmnm_litPsXSPwpYSTgCCE7cd5JDZtnwZm6lnEkFpAPGeEBkGI11Bu-ISQ9RQc8u3CNk-lJG8jCSrCQjX7ujtUAeL7KqDbt6WlOB_5eLlA5liUNTy6nxs3wXbET24R5h7bfTGetD-ZGzy_1Cz5YkF2P8K-RlcpUva-9FcffGKSosoHcufybq1zcpkw3m_GMaNu3zCZbptmjevNB_hY2_DJwak81PI-lo0LKkC46r5amF5KjrKdqCCtwCxP07_NRUfptynU_x4uKDic3nu25dlE8uyhv0TIvx1fzpZVtotj4Z1mJDdklbTYiUd0_p4sZuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106938" target="_blank">📅 17:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=H-HFsMyJlW3NyXK_AQ_UJkH4jIm-N4VmhGaVqlV1krNsu2lAxlF1Qs7q1zTixqgM2j3DC_zjKOqFvX4Y9uA68WZgS8yQDHqZeA8bDiZb7ullhnfqKN-tMDL4hXa16StA04VeInMVT1glA6OcseiF617tH5QQEtiNJrI1YmD6IG-b0T3w8WDwrKHAy_mKqQ1ihqwmjGfSvS_5fBuNsDmD7hNz6IkVQm2J7YEy2X_WaP3BpyvJQsUyFRUnoK70PW5rvYui75Wwb8aD9Pvc0NjWjDl_xB-4g9PZVmQ8pzKpAUrGTFmSYzOO0a03b4mTPB3YSCg-Eau_mJBhvpo9FIZeMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787e254f6d.mp4?token=H-HFsMyJlW3NyXK_AQ_UJkH4jIm-N4VmhGaVqlV1krNsu2lAxlF1Qs7q1zTixqgM2j3DC_zjKOqFvX4Y9uA68WZgS8yQDHqZeA8bDiZb7ullhnfqKN-tMDL4hXa16StA04VeInMVT1glA6OcseiF617tH5QQEtiNJrI1YmD6IG-b0T3w8WDwrKHAy_mKqQ1ihqwmjGfSvS_5fBuNsDmD7hNz6IkVQm2J7YEy2X_WaP3BpyvJQsUyFRUnoK70PW5rvYui75Wwb8aD9Pvc0NjWjDl_xB-4g9PZVmQ8pzKpAUrGTFmSYzOO0a03b4mTPB3YSCg-Eau_mJBhvpo9FIZeMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🏆
پیک‌زدن هری‌کین به سلامتی توپ‌طلا احتمالی‌ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106937" target="_blank">📅 17:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106936" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106936" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFnlrRR-Z4RBLXciJ8WAk0FTeATzK6WuFAAJfvG4QlyO9J6ITFIyo0jzG37gd893yoVlDVFmWuaV2SFBjMXg0RTuMadAF87iuUo8-KkxTWfEr0F3P-aMIj4sgcBI4i_1k4L8NlZ9G-OFNv_2RBQlFmadh9-Os5Yg8sF1hXtADrAsSZmGcBIfThOkK8GGN8SlJ0ipyTCssxWQ2CgPYSEWd1F4HR0cmQ4rYQhM7WdRo33gj5SVAs5F4kBbc4kWpvAN1UN1yvoZP2OiWDrRcMVPoU4DgRfQtd-iCHI8721D01JtIoBKtpD5F0EHu2n1bhmGsaY2PAlaPIoe9h6FnobdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106935" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برررررریم سراغ دربی حساس مادریددددد</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/106934" target="_blank">📅 17:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106932">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUs95whhT5D3GVmL544FIGpL1IellY8fmR-OX9_M3BFYm_8Q0n4IDmsrueva-fiaGSfxAWQBBB2xPiS0QATL_oiMeuqGffNKxtzeY_7KDH0pdGrBHCBgii_i6SS4fDhBl9dejYiWhK3_Y-K4tJj5x0L1nXBzk7tF1ZiH06Kb-Fk1GBB9n3jOOlC3UYGcbHFj3rju2qZ6IvZ558BY0dr3H_dc0Z0dkPTObccvoK-AhYHTOzMgybEfPekTczkA8boCGTA0U__jE7fzRQ-lMVX61U8kN9U83LF8Dsi61LdJRIsO6ik5OxFUE0CHi_oacsUlspQ89QtBDlf1U_6wMtRdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhV3KKWvIln2XvnymP5wvK3W6_tjfpfFjRbHT3HUgBaVky_RNB3RTLgZuFwN9h8tNATSObo8dKRLveXaAEroZY7g8CIVJEEfEjB5BhXPG8vXiAN8eN1VVM-1bqJy1murh6WNtmnyqIrnmvAaby_YTkLCYUMKf76AAHeHAAshZAAQ64V6wNDbW5BJj2ntoSQxZkkA2UDqJzZkZdnsLDVO9vEZXo9Z9HHZVgCtvi49lUuUlKEN_yWQuZsObPZAS4AzzWBooTyxvVETAwvCujy_5A96S7lHYG1K1mGt8tOmXwvpzcISiFsgWLSbcNxsJOQo4jLNC639FpCN15KOWmrTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
ترکیب دو تیم رئال مادرید و اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106932" target="_blank">📅 16:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106931">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c42dce9e.mp4?token=fZaSs0GoahiUdKUfBBhWGsWDX3hAA8z3n7nlUq4nFLgGcruvlf4xJNDhwmEkiQPr5l82059uzJAQitSb5TLY25A0DsMxvH5aU4J2ejsf2w3CvFF9R3naWdRwG5XC4PzKIwNcyGQAfGMEiqY_oKH8_50BTcmc5zEVyTOL51gtGC9G_3_ZZEMuQLO0iZiiINJJXHCiUCMVOoDbueIgny_MEl7rXMU58LAdhJuCs3qDkpJ6zXw2J1JCq01eI0maR1uq-J8PXLR1kXnuC9dDxPzR3WIFp43wWldtPzGABEYHwC7XdNFzhYVHHFvgUULDTzUp4-_rr84qERc2fdAKiYbP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
دوباره از ایتالیا صدای گرگ میاد.
🔥
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106931" target="_blank">📅 16:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106930">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=LujImQncATJxsDas9QTaJJTaQH1Nh7dLtUomBa35QfgzqAFxUh-CKHOpmX6o35co6PgfiprmpEgM8pOInYVAjzdNN55moVNJ9Pm2Ml0I71XQrZNecJyj2nokHSkMs4XviIbk8ZnkNl2D7crg9y6Mu56Me-ekXZa1VndNovFckaA26lyxA_65Cn4cSlYDVYfm5khgxw3hrXT2LvSj3FgGpkxFyDn-kjS9WPcGvfPbj-jjY-Uf_SLCEvDKFR3z1qdF0ukaK4MhT7_RxawzYull2Sabo-IBIOA7wpszqv1DOMKAVoLADYUP7QNQ7HXLHb9rStPQ6LzSplWkW1p-gABaJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27b89b6e77.mp4?token=LujImQncATJxsDas9QTaJJTaQH1Nh7dLtUomBa35QfgzqAFxUh-CKHOpmX6o35co6PgfiprmpEgM8pOInYVAjzdNN55moVNJ9Pm2Ml0I71XQrZNecJyj2nokHSkMs4XviIbk8ZnkNl2D7crg9y6Mu56Me-ekXZa1VndNovFckaA26lyxA_65Cn4cSlYDVYfm5khgxw3hrXT2LvSj3FgGpkxFyDn-kjS9WPcGvfPbj-jjY-Uf_SLCEvDKFR3z1qdF0ukaK4MhT7_RxawzYull2Sabo-IBIOA7wpszqv1DOMKAVoLADYUP7QNQ7HXLHb9rStPQ6LzSplWkW1p-gABaJoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
بغض ایراندوست از طلسمی که شکست
پدر و خواهران مریم ایراندوست در ورزشگاه، برای اولین‌بار؛ خانواده‌ای که بالاخره برای یک بازی زنان دور هم جمع شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106930" target="_blank">📅 15:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106929">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=LYXFg4tyxwWZjdshWNIiEXuGlryB6cTWcNlesOUbU6t0WlrnBQHK6O9dWXnWPVRvlcLkppsZql7aik90ZSkMO7qt7skBb7n04eTpy9lJHfgQQwfJVHzDa1XlEjioRzYAxITNyGNZ-2408JV-OJChnB1X6ANOj0fH8XEBeB_KS3EgxrWTdwXq8izA0bTiLhkxGXFVCH5va4rPpAhxKMp-9V0S4JHp8DD5xfHGxQYK3wlSektow3Jo82pwOC-cV2URRrnhcQO0EmoCyv_Xypk-vLxXH_w29Ld350eWVplimxPvOlReXgryW9wu0o4B1MReKBJqehhNFEc7EogwfeGVdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e67d6e531.mp4?token=LYXFg4tyxwWZjdshWNIiEXuGlryB6cTWcNlesOUbU6t0WlrnBQHK6O9dWXnWPVRvlcLkppsZql7aik90ZSkMO7qt7skBb7n04eTpy9lJHfgQQwfJVHzDa1XlEjioRzYAxITNyGNZ-2408JV-OJChnB1X6ANOj0fH8XEBeB_KS3EgxrWTdwXq8izA0bTiLhkxGXFVCH5va4rPpAhxKMp-9V0S4JHp8DD5xfHGxQYK3wlSektow3Jo82pwOC-cV2URRrnhcQO0EmoCyv_Xypk-vLxXH_w29Ld350eWVplimxPvOlReXgryW9wu0o4B1MReKBJqehhNFEc7EogwfeGVdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
🇮🇷
فرشید اسماعیلی: یک‌زمانی در زمان رویانیان در آستانه حضور در پرسپولیس بودم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106929" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106928">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15GtKUD0HvUTmdzT7M4lIOTGksS0bRRBCgSCO7L9eEsAWfSanO5fVOIWJHcsrk-ej_vkqaIhftDkpmRMBMApe8T9ayU7biIp52qhXLOqCYSk7f6f_0mzsIsdk9xRMWnKhdDkOyAOwJSViD4ZYgZOWkah1PcADqWOr32DGsheuEIVZa5lg0iFO_i08emMAwcLzDn2hZvObaw_Du2zR7wSJ3XBect9wkTUHrlWNRD9EeAz72PAOKXT7NshBD4n-INXFHl8pvPdOusmP7taJGGH1kKR1C6WQn_DUiQLohfYQKLZM7qie6IyGj39Z1LgnBGpNB7QpjVLVeSrYfzB6s54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشون زید دیومانده هستن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106928" target="_blank">📅 13:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106927">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=JhoYQtNv8GcS_9jNrTW6qtwmha6zqXY1wi4uIqCXy8vY89iXtCYGPFb0BRm5WK6QaB-s7IYdVt5Jwg6vo2EGDQaSwQ_ql8usuCod2yoS3QK3ItqRph9_-krOixB_6vpWzNYtpdl3n-jkcXpQHBEehTk7DPoQl1YWEk7uFqNT7kQGtxShxc03MQ3XzqHLd4nRKc7DCf70BjMoi7ZneDRk7ZXCCEvhWodRN7iLc4FudMFLgaPG97ZwEq8rJPDkj99VLAZwpz1RZA0odZTanuPSRrJP0j9Q1eL5plFErCpnsWMqElsp59xXEmuUtq5bBxT8Qa7VkBF2-MLrHEX0aFdqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2519e30b.mp4?token=JhoYQtNv8GcS_9jNrTW6qtwmha6zqXY1wi4uIqCXy8vY89iXtCYGPFb0BRm5WK6QaB-s7IYdVt5Jwg6vo2EGDQaSwQ_ql8usuCod2yoS3QK3ItqRph9_-krOixB_6vpWzNYtpdl3n-jkcXpQHBEehTk7DPoQl1YWEk7uFqNT7kQGtxShxc03MQ3XzqHLd4nRKc7DCf70BjMoi7ZneDRk7ZXCCEvhWodRN7iLc4FudMFLgaPG97ZwEq8rJPDkj99VLAZwpz1RZA0odZTanuPSRrJP0j9Q1eL5plFErCpnsWMqElsp59xXEmuUtq5bBxT8Qa7VkBF2-MLrHEX0aFdqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رختکن چلسی بعد باخت جلو برنتفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106927" target="_blank">📅 12:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106926">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=ETF9-mpnCwieix9wbTmewedhxmAlH_ouDkwn6XydJbErHXhjcBguJQLjdp0xM-yCOB1meT3Rxz6ySz2mg4961UpTAYToDc740-Lv8ru0wWDC21Yr60brlIqnjo216A96RyFAml-U_gehlhzMEw0KqRQP12dwmNEM8dJ9TmqvXOaPH30G0_XB6Iu-m4YrB6EJobxp_7z2qsZYndu_4tpzA_1gE_t6HTS90FBKMX-cZScSAkdUrLNdl_MRYHrCUgSXbZZ3iGr9zyHtVbHWZl7raszNYsAGeMvIpb-MSszMGmsohNojpoPLxMouwA9QG9FjWj8-1FuWjhc1ZRcgd-0KaEUQx0tDl12YLYyo9G0I6AIctL4nHylfMl4tVTuS_cBlNgPYqPeXdLjsQ1v7zO6FOID2rrdrl2erCSV6ISWzXEvAADQWwAvlrOmvcs8WCd9ejGgDOGp3macPFGpsXXxknOTWF-UiLFV8pL5WqatvIr48kyUaoRjrEpICQsy786H_VjDxhQYyml2ti_UYO1EBZCQnHLgaoEpHb_aCrfwZK6OhpjaojmZzLGGLkHI78Eps4EbJez9UDmxlJQ4PN3kvrExK8z9lhWoj877lJjbgUG1oM-vJ2fX-C0of7MPF7CP-1_N84OvkcW8MYjEVUma2nqVx07vKCtBu56CfVI6UDR8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3686f3655.mp4?token=ETF9-mpnCwieix9wbTmewedhxmAlH_ouDkwn6XydJbErHXhjcBguJQLjdp0xM-yCOB1meT3Rxz6ySz2mg4961UpTAYToDc740-Lv8ru0wWDC21Yr60brlIqnjo216A96RyFAml-U_gehlhzMEw0KqRQP12dwmNEM8dJ9TmqvXOaPH30G0_XB6Iu-m4YrB6EJobxp_7z2qsZYndu_4tpzA_1gE_t6HTS90FBKMX-cZScSAkdUrLNdl_MRYHrCUgSXbZZ3iGr9zyHtVbHWZl7raszNYsAGeMvIpb-MSszMGmsohNojpoPLxMouwA9QG9FjWj8-1FuWjhc1ZRcgd-0KaEUQx0tDl12YLYyo9G0I6AIctL4nHylfMl4tVTuS_cBlNgPYqPeXdLjsQ1v7zO6FOID2rrdrl2erCSV6ISWzXEvAADQWwAvlrOmvcs8WCd9ejGgDOGp3macPFGpsXXxknOTWF-UiLFV8pL5WqatvIr48kyUaoRjrEpICQsy786H_VjDxhQYyml2ti_UYO1EBZCQnHLgaoEpHb_aCrfwZK6OhpjaojmZzLGGLkHI78Eps4EbJez9UDmxlJQ4PN3kvrExK8z9lhWoj877lJjbgUG1oM-vJ2fX-C0of7MPF7CP-1_N84OvkcW8MYjEVUma2nqVx07vKCtBu56CfVI6UDR8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اقدام عجیب و جنجالی سیگار کشیدن مجید واشقانی با اردشیر رستمی در برنامه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106926" target="_blank">📅 11:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106925">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1S4Iw_slfXumC44s0F5NrewQFjcTfHDpRtFwEOHoVg7bYxOzAfroQ55pT2yJqcCiMFWyMnhb3HUG2btbfNXO3pOeZq-Miq8pGqsJTJ2xVzjCYKMxK6waqy5QqEsTI5Pax8gdO8nURWyaJpEAvsGHLuTwnpV8iBe6U1Tqv8MWxb_9EpOAcTd5lTn8CTNcTERZOo4CrBbTDn6uxfkCE5lRuoARt7aPTrEYOBcKyxpVxD0A9-W7UBkQ-ToqtB9szjPy1qXUCeZeNfZphBofM5J_JeRIXUO9DRUBS6ltynF00aB1T459Hcfr-aE1xTYUwkFZ2E4L_DtCzK7g9Kes6huGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تیم‌ملی امید فوتبال ایران در دومین بازی از مرحله گروهی بازی‌های آسیایی برابر چین با تساوی بدون گل متوقف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106925" target="_blank">📅 10:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز متفاوت و جذاب از تاتنهام که برخلاف نتایجش، فوتبال نسبتا خوبی ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106924" target="_blank">📅 09:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106923">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=T60kH4uVgFNqSyp6D19b9dEVbmpDWvjqL20fyi16nIHzXusKHMzRK5db3EnZG1vvaumvIFrHuiT9OveX22Q_SOM54iF-RewsgNNLrrli0anwkrKzZwGuB053hzARZmQSh609VGn5uiIq6F6_w4hU-knLHD8ujc61aqbPzPTkieTgKuFXBIU-ymRFkC3HB9pZhAkRIuhlFA9-tEO1tKZEsHHi4wavZdvKGB499Ie2UB0ySSVfFMlWh8TFb_Up89EnwFTNRYM54BzaP0Xb8uuZcVzVFsykSn78EACWLXAACM4B88id8zBDZxpGpQTdQIYzxFbOZd6E6LvBOoEHsSzAlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf2bd4a2.mp4?token=T60kH4uVgFNqSyp6D19b9dEVbmpDWvjqL20fyi16nIHzXusKHMzRK5db3EnZG1vvaumvIFrHuiT9OveX22Q_SOM54iF-RewsgNNLrrli0anwkrKzZwGuB053hzARZmQSh609VGn5uiIq6F6_w4hU-knLHD8ujc61aqbPzPTkieTgKuFXBIU-ymRFkC3HB9pZhAkRIuhlFA9-tEO1tKZEsHHi4wavZdvKGB499Ie2UB0ySSVfFMlWh8TFb_Up89EnwFTNRYM54BzaP0Xb8uuZcVzVFsykSn78EACWLXAACM4B88id8zBDZxpGpQTdQIYzxFbOZd6E6LvBOoEHsSzAlzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😢
جوآنا ویتژیک ورزشکار ایتالیایی در مسابقات چین یهو وسط کار اسهال میشه و بی‌اختیار ازش خارج میشه اما با این وجود مسابقه رو ادامه میده و قهرمان میشه. در نهایت از مردم عذرخواهی کرده و گفته امتیازاتی که گرفته رو ازش صرف نظر میکنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106923" target="_blank">📅 09:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106922">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106922" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106921">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNggQyWyHlEyUiSuL6gVNQmdaaeTcYvRwwEDK9BqVAFZyxQfNomWhP8B5iu147aHwzJz0qrUQPCNRbZFmegJyGBoRPZeaIWQujrYPwgPdDTOosJYFVUuZ1rR5AkifXcdco0imGyD_8EsKS8cALxgK6xbeJbzl7vX5yrqosZw2jq9oWm8VbIDocCPo0VIyiANQYjVqxjrsUyBVRG57kturJR-xtlEaeu_Fthx-f4KLY2QVAipWU9qgpXLDsZO0uffHme7Pzfnp1ufeA1aSIT3plokITRRff5qvCSVQzekLPC-3CCNuG2GnR4JJaVXg8BWUTtbquhbk72NsMGKtupFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106921" target="_blank">📅 01:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571388041d.mp4?token=m1N37iKAjZKT-ctbA2B8bjKuBStgMF9zuvAbMzoxsJ3NYtn6iob2r0YHrDK17-rTik6kcMw2_qSKthJGsOrB250UON3aHD-PezeBSojRmtp5D1cvN28qrIxN0wnpQTDVicbtXHk6SX3beQaX3tmROHA5QlFpsrQyB396lbb65I7hf5scytrvu7U_tnTkb7vt0UlA8Zq9F3wSrqlOhpFPeW7lUAVSUAtNUcPamEAzJQq3FKbZGqMLfiQWJ8ueBCp2rqatE81zzYmRDQ1gFsjad_2CwJ-DflpVfKtmI2Ut8ectowAesvrJhnr_qG_YGAnBAP_164NMecGKW96wjZIrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
کار جدید حمید سحری از برد امشب بارسا: واقعا کی میخواد جلوی این بارسا رو بگیره؟
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106920" target="_blank">📅 01:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106919">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iitqhZeAqWIL7H_KMOnmjdmZ3fEaet__KvmJS1KyvjQBe1KktfUtty1hCqq_UemIK1gMmUm99c4WTA5Wr6jm9lj07YV1dcBfJmwkyUUUsNJG4XuKDah0AQ9XnI9OjcnL9UOnB7k6LwC176CK-AZGZ5ZIYkLxT1ecOsdo_tcoGai3QYFwF13-rzRFsJ8ZVpnk2je6WSDWF9qFRW7qC9q19HcmM0ulCvoc0oGzz0FX3LH3IO7E0Pd32PVsl8JBNhft1aIJvRwrYpFurLJt0tMPgcJQN0CXqRdPUGa0um8XzjlIjLSIK_gI8LwCNaY3HgoSb0XecLklsVg4dYZ8wucZbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
براساس معاینات اولیه، کریستنسن به مدت حداقل ۴ هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106919" target="_blank">📅 01:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106918">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwoqs_iI-79DrxjjnDtZ3mLVFQ_C5hfc_nlfxsCnqMI6Ck-RJa7adSvAxejqH8Vl5Ik75_J8K2HWuSynizQWiFipwHXgutceLapuuANsZfN6whWOab_i73e_rrkUq02xRnSVrAH9fe23n0olu3RoeA467QoA0yHT1VyDhZONKG8awq_vKbUJySAWfTP0PkvD4H0nGhvURfA7uVND4JnGPeoh50i5kAlleP5eWMs8Ml76rHGjXEb9B_Gcl-jjHyxSj9yAROLtcInmD6-BFarF-OMEr0MUb1n3tAW2UTTdg2OFePYis5v5dZD5iOn9HUhWbwFcEnvZfIUG6-eQonz2VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🇪🇸
هانسی‌فلیک: شگفت‌زدگی بابت عملکرد رافینیا؟ بله من شگفت‌زده شدم اما نه امروز بلکه دو سال پیش و هنگام اولین تمرین با این بازیکن. او و لامین دو عنصر فوق‌العاده تیم ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106918" target="_blank">📅 00:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106917">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxuVVLkRzcX3ijjOENM1cJ1UlJ1L6Vo_hUOUrg81cA3_u-d3tZDWmC7ocpPg4OuLBTvdjQ2Qk9GJjWqa1C3sSAWlZpMRiFXWGxzvQ0VoYqesmg8Lp5TfPLra_iGf3drEKFem4LuWrnDTKaaRSXFp6Ai6PsRlrGNxqminchyXBwEqgCrlbO70OT_NXZ3AwQW5N546ZxrJqJO3ft8POve-3KIe3pArT_fDITdD9ktxJ4zyYc8MYtlOOjmtLSKWpCsUJfDjwGBahv_dwoIptgrqjjAUlRWM3RlSzZ9SBjIO2xHLRSPLBpLUbAAe92zWDdYW12zQtFg1qIq30OVe4IAPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
عملکرد بارسلونا از شروع‌فصل تا امروز؛ بازی بعدی تیم وحشی فلیک ۲۰ روز دیگه مقابل ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106917" target="_blank">📅 00:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106916">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnUR6Y4X_iynVwb0WEWyzDD0lpgme0PZS8qaaw4FVBGjNKQJl1V8Wh3Z6H8Lswg0VdEwZ7X7Nr9x3ehhDoP0a6we2KScQ2h7RHR-Idn3a6OZXXqdJjJhoZ5PDr32VnWBdpfNJ-x4Jg9bjvd-BM-0Z4ND6faF0rBHQJZimVhSF2cFNozIbexYTERe3G3P_XopgInwE7z0oNddl8snbP1c3pZ0mo-W3fGpp3-z8WcUaWWR3uJ_maoqj6UTRcyRkMpCcV2Gx71_fEt-vw1P5S00abcyppjYJv4ebMbzedT3kV-ZLf05XNI29BiF-JI6_4mz1jGOCmeejasy1HpTIpyc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
هفته‌هفتم لالیگا اسپانیا|یکه‌تازی غایب بزرگ بالندور در این‌فصل اروپا؛ بارسلونا با هتریک کاپیتان رافینیا در جهنم خانگی سویا برنده شد
🇪🇸
بارسلونا
😆
-
😃
سویا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106916" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106915">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCmLAhIwuF2UKEfLAoM4BEwQWXH_b-UZUWjikJv0Rs0-Z6G0_0fDSOFa7zC6xfN2jQg6lE58TmVWUWqLwqbt0KJGdrj2_VNkY3-pyCPbo2NA71f0Q1_xHXrSUq-8gF-G1ffodHDpSUVIa39mK45VTY9FyRvLzvCwKWMFBvBSxepFuGz_aI08Ey_cKME8880ywb7vuic0Xa_4QnRU1SJmJoLVQuWTjrgtKh6Yukgzw6VBD3Q_ensnxaNa03jofvnCrjCqribI8kywsmpRGMgGqnv34nMtGvU5Pod-LsuRQnJ2_rnoBEumm3C2c9FVvsfVF0YvVpx8VEnDF6Y87CKJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
😳
😳
🔥
🔥
🔥
🔥
🥶
🥶
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106915" target="_blank">📅 00:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106914">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Govy1_SgFGvkumRjJvsfQXntfChtyseBKPyd74-1QpvYQ-jtjXEB2mJGrDAtY4YIdWHLL5oJFHmuSW-L0NZdS3iUhcMnNpl6S_7CkBmwbDNses-a-3G-L12s2iw7RzwpQd222a_HkscC6Fl_JezDIQEXY5Q2vqb0ld-NzamNByEGDzgycMfVi5_Q4Iokgx1aGjNg-ugwduZ5pU8w51Bs6JGNGBqjs4bMrOT9t3rkLfRRzmTqQAMYU305yaaavYY5lsl6Stm6t4TRcZukL45sQ6wJOmBy6Y3UKxNO1qQ5KV2xrBkohcb9f0OzF5PPK-EqejEJoMbXNDzma0We1wpRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106914" target="_blank">📅 00:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106913">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCgQKh7g8MMhzLFpyuvtZnVU8T_RohyvRxoXUS4hdVoWVUdmeXHHeBBm4D_g_7msNHjucC2cV7NJ2kgrU15NjytYNcPmKZReIPiJURzzAJajteQAt_8iP2mtEXp1IhlClSibf73XlpjdzV015239THeryDpYPpgnnLTs-d677-F1xH8DbL0jVoD8GpANDjwzCfoBE1F0Br4nIRTespROx6ZcCTxYvxQt6IKY2_ZynTJOoCEtQ8uNFVlQMwG8iEVh8NpCnCxB1q69eZYEaklJKszOhJtjsbDhtq4SaILdNIpX9foDEWQwRLiW-LUSlamfDbQ3MnaTJskuOsz7vVj_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
📊
🇪🇸
رافینیا اولین بازیکن تاریخ بارسلونا شد که در ۸ بازی ابتدایی فصل موفق به ثبت ۱۴ گل شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106913" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چه پاس گلی یامال داد
😐
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106912" target="_blank">📅 00:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چه چیپ سکسی زدددددددد
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106911" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هتریک رافینیااااااااا
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106910" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106909" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=ST19CnnTFZzaZUy5CK1UZwosEoA8OjTy6nyrLkUSNBHW5xnBzOOPDxAYJkMuyFfnQjSOy0bmLvWww1pZwZ4zz5X0Tm8ODK32iLACgtPkS1pLOuv2b2O8wC0tIzDWkhJH-6jEbHuCrkSIYaHc17wTVnPuVjF-hV_eezFWkA3aFkbNWZvQCwwsAPpmZeyU4PhES0bunkJTEfpYEfNw_9P_sG1bUTdHO4ndDIeJ0xGYqSBUEjyqHrG6J2Df9PPKrdwKLySrh4gGL7jHmZXrdYs6EsNHaarcYgobhIVLyTu167ULiHTaXxIl78eS7-kMO0n4rupwvkTzmyDmfivTnEYI_yNpXmgenc4zl0sYHaAzh4dJbDNHefdQhjkCVf7bpdH-Yp9Ko9VSjKdoJPR1ToeWlxS0ViztD8oNdWUdG0xcrrnU1PeULujEmwTRBLfws0C0oElU2zvMY9aZiYNBQ9HueTRNPYaeFLmL7wfAZE6JICEd_LRj30nbNsJi175gGNQNAAGd_W43mdbQP0wRhGovdMYahKb2QnZ1HpJ8h3cHStFO16QTFsES42TtZ3x1DhsJpOns9f5VhHIkx9mAA273GOTdjrkAEBFhWy8GIfJtvfosU9hHnFcjWVzCp2upXlTvCkaT_sS1mQ79Ad4gS4f2fUjT-A9vsl8Evdc-LeSW3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c2fc4a5c5.mp4?token=ST19CnnTFZzaZUy5CK1UZwosEoA8OjTy6nyrLkUSNBHW5xnBzOOPDxAYJkMuyFfnQjSOy0bmLvWww1pZwZ4zz5X0Tm8ODK32iLACgtPkS1pLOuv2b2O8wC0tIzDWkhJH-6jEbHuCrkSIYaHc17wTVnPuVjF-hV_eezFWkA3aFkbNWZvQCwwsAPpmZeyU4PhES0bunkJTEfpYEfNw_9P_sG1bUTdHO4ndDIeJ0xGYqSBUEjyqHrG6J2Df9PPKrdwKLySrh4gGL7jHmZXrdYs6EsNHaarcYgobhIVLyTu167ULiHTaXxIl78eS7-kMO0n4rupwvkTzmyDmfivTnEYI_yNpXmgenc4zl0sYHaAzh4dJbDNHefdQhjkCVf7bpdH-Yp9Ko9VSjKdoJPR1ToeWlxS0ViztD8oNdWUdG0xcrrnU1PeULujEmwTRBLfws0C0oElU2zvMY9aZiYNBQ9HueTRNPYaeFLmL7wfAZE6JICEd_LRj30nbNsJi175gGNQNAAGd_W43mdbQP0wRhGovdMYahKb2QnZ1HpJ8h3cHStFO16QTFsES42TtZ3x1DhsJpOns9f5VhHIkx9mAA273GOTdjrkAEBFhWy8GIfJtvfosU9hHnFcjWVzCp2upXlTvCkaT_sS1mQ79Ad4gS4f2fUjT-A9vsl8Evdc-LeSW3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا توسط رافینیا با پاس یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106908" target="_blank">📅 23:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106907">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رافینیاااااا دبل کرددددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106907" target="_blank">📅 23:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106906">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگلگگلگلگگلگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106906" target="_blank">📅 23:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106905">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoFnbas6Ion6k_QIntLDPFx1hO6tuDfuqyeiWa3ky50M5RuTXYZzhpRrajbNYN2vENC9lq8ecQE3WsEFiAw1p24rilDZfNHwwubLLGyPFGtbfPFs_UHUOh_wALNEQHudlMQ3X5lS-dzEYrHy_gXyqtkSny5up43Shth8l5xFvHNDoO7Jp4v3MRXkgDbrN2dgYJunDNkbDZGD7s-Cd7YyybJizJbM0d1ird2RNs9d4ds6EFuudsLDVhu0euDH6E_GywOtnsikS2V8GLmkOh-aK3HGl1Ll7OgIaBqfxxqFfXxOkJ3-BKSqqceZy_H6pPHbvm_kAXH_o0TInPakK7wt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
سعید زلفی و نیما تاجیک ۲ گزارشگر مطرح و باسابقه تلویزیون به پلتفرم اینترنتی نماوا اسپورت پیوستند و از تلویزیون کناره گیری کردند. پیش تر محمدرضا احمدی هم از تلوزیون کناره گیری کرده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/106905" target="_blank">📅 23:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e51312166.mp4?token=RXxvGg-HLyyARdktzuHd-hyBn5NqwiXAe5Foe-T19U720VfENo8h2vBAmnq4NP2kk2ydRSIzkVyqcjumnUb6MsHRbOGnf_q2esL5Yx8vhSpR-1LsqBB1wjcDJEYRFUKSEubv1C_qSt44Hh-gyt758bFUxbjfnveiYLx8VubMWeItX0jv8FapKQ9m_o1qAqOEsNjjE7h0Yvdv_byy-gTBRrwu9ewz3SNLNIH8zNNJ9EiflxRpBFPJfuyfa5X-gnQqY-KOluwmgNYOho5XIyxxgEl86x41jN12skeJMoeEgHyaP6DHLIY3Ir4O5kTJqbOy3UvtH29gT66a78SqsVV3omtuSd9lW2HKtv2cb6y-5YBSeaplbjA0ypeXKz088BkNYB5fYCY1INhpYZ6Ixow6euhCBBIrGav7tSJ-o0wAc5Wg6SyDkhS6knxE4dw0jtppnbgSnqFUQrxOTOR6QNu2D_fHfJzZPlWDDpf_CC1DD9_veY8pqHCVidi82df_PtGS6MiS_qU6oqA4sPju3jmNOVBpdzo19FleeNcOi-_Chf7AJpjj_JSP8980GBNdsBh2KrXKy-3TQUIJd7K3PxqYz9xL-XB3dMC7Xl7KxV8zcIma3ZUwBLnESZxH7yayZ0bOxsIRZcNsioQdvYKsEjaPbbeh42CKfDcJ2wYiS9OnR5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e51312166.mp4?token=RXxvGg-HLyyARdktzuHd-hyBn5NqwiXAe5Foe-T19U720VfENo8h2vBAmnq4NP2kk2ydRSIzkVyqcjumnUb6MsHRbOGnf_q2esL5Yx8vhSpR-1LsqBB1wjcDJEYRFUKSEubv1C_qSt44Hh-gyt758bFUxbjfnveiYLx8VubMWeItX0jv8FapKQ9m_o1qAqOEsNjjE7h0Yvdv_byy-gTBRrwu9ewz3SNLNIH8zNNJ9EiflxRpBFPJfuyfa5X-gnQqY-KOluwmgNYOho5XIyxxgEl86x41jN12skeJMoeEgHyaP6DHLIY3Ir4O5kTJqbOy3UvtH29gT66a78SqsVV3omtuSd9lW2HKtv2cb6y-5YBSeaplbjA0ypeXKz088BkNYB5fYCY1INhpYZ6Ixow6euhCBBIrGav7tSJ-o0wAc5Wg6SyDkhS6knxE4dw0jtppnbgSnqFUQrxOTOR6QNu2D_fHfJzZPlWDDpf_CC1DD9_veY8pqHCVidi82df_PtGS6MiS_qU6oqA4sPju3jmNOVBpdzo19FleeNcOi-_Chf7AJpjj_JSP8980GBNdsBh2KrXKy-3TQUIJd7K3PxqYz9xL-XB3dMC7Xl7KxV8zcIma3ZUwBLnESZxH7yayZ0bOxsIRZcNsioQdvYKsEjaPbbeh42CKfDcJ2wYiS9OnR5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🇪🇸
گل‌اول بارسلونا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106904" target="_blank">📅 22:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چه گلیییییی زدددددد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106903" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106902">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رافینیاااااااااااا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106902" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106901">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگگلگلگاگگاگاگاگا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106901" target="_blank">📅 22:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106900">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگگلگلگگلگلگلگلگ اول سویااااااا</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106900" target="_blank">📅 22:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106899">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXmoTuQ_xTWnqUZvNyJg7NpG6RPtt4BCpQ130rjmOEF_9nU6KqDytP2shUa7niBKjQ8fbShNOjaNeltWNXPoMozbA-egNrI1a8HFggQ8LH3sas0c29JTR8qkdfVo10ovmS15TPxSOCY83F-leV9QhecGUknb1yomP_RDnUP4bY3PhVKkH_SzBzYJuAg8CpoK27rE9QCxWauqr8zFpU4DTTJ8i2fYqjJEpUlk5kc6GGOxyLWBRHttgK83-WmfaUrOqmtAIzUWbj4Si8t1y9CUcnm8wSMglOOAZU6OLs1Rf4y7kpRMChJxMeDCCNnRTWFeUz4LUK86s0-RwlW-6Ev8rYI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f072da801.mp4?token=Mm8tkozMkq5BJ9KA9o6pOflZTeFJLJVpsr7b04-MLCuGHGM-JEdkRVib1KJiy9cZHfyadLl7XQGtQPcSwIanAxj--DJ19kLYPfjYdpgqR2I-xjgMee189KkDP42c9z-5J0bLX12etb-OZXaCF9r3OmdxQqhxhbQoeAX8Gqsl6NTUXde5hoFlVG1FcnK8dEcuYqAlJ5YDo6gMJIs8tV4VXSEhzXHqgO_vfOKvWn-GXN_IIaL383HI9rNIAJ1SKvZvPtUcrcvalo0XZBx-M2Q-rn-OtvlxlK071WYAgbUp8Z0nycnwqeBz0BtCfY5H8LUNfa3NAdCiXImEc3MTEITKoXmoTuQ_xTWnqUZvNyJg7NpG6RPtt4BCpQ130rjmOEF_9nU6KqDytP2shUa7niBKjQ8fbShNOjaNeltWNXPoMozbA-egNrI1a8HFggQ8LH3sas0c29JTR8qkdfVo10ovmS15TPxSOCY83F-leV9QhecGUknb1yomP_RDnUP4bY3PhVKkH_SzBzYJuAg8CpoK27rE9QCxWauqr8zFpU4DTTJ8i2fYqjJEpUlk5kc6GGOxyLWBRHttgK83-WmfaUrOqmtAIzUWbj4Si8t1y9CUcnm8wSMglOOAZU6OLs1Rf4y7kpRMChJxMeDCCNnRTWFeUz4LUK86s0-RwlW-6Ev8rYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوووووف صلاح ببینید چیکار داره میکنه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/106899" target="_blank">📅 22:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106898">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106898" target="_blank">📅 22:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106897">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlcsvUzMdmg5HBJxGprtXjWciRn8uxbBuvSNMOXvcdIzRhvuP-tOx0NLKvnrD-1HetEUX4zByKtjviX4ZQlP4hUroNXF-K6s_AwPTRgCNhNrNIDex2XCvPJV9_i2C85YaOviyL4EH34vwgso1IIx5qZkQYbuFitFr0evSww9WcREDDvBt9ywYjHvy6vbuVIeHG8L_t8AhgwSMHAyVhSA4ykdl347jmo5smUxR-Jmf40lMQQlENbYKJuJhB0Ge5787YVISyYsbhsWEjxzFFTa6EjyxlTymw8JMUGf1OH9HbJEznt3ZjYzXnrsYe-wdYesI3BFCdGRifq4afcMfb-qGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حمله شدید دی‌زربی به بازیکنان تاتنهام:
🔻
ضعیف‌ترین تیم‌تاریخی دوران مربیگریم رو دارم. اصلا نمیدونم این بازیکنان چیزی از فوتبال میفهمن یا نه. اصلا امکان نداره یک تیم اینقدر بازیکنانش ضعیف باشن! واقعا براشون متاسفم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106897" target="_blank">📅 22:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106896">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=IavIAsB9Ut04PbXvnwZonH5gAs-8FvQOZzS2MWrSC60tCN4D7v4O-f3ckhcigTuZ3WX5-FFeCxuJm7WlpznHdlGDSDEND8Fhgc0T8FN5nGkIJewdU5EYUZk-bojJXyzElQEi78PG8pGsOvDXr5aD1He6_xjRJN1lhgZnHM2G-RWccPWdQG516LHXPvKLkamyRdlyoPewqIxrHMUJlyIRYMzu8z7qJfxnvyA9K6JYLUUMS1LP8OG5a3rn4MLLQL09ONTv4PwfIjwR0jJdwjIoWs0MpFDkgn8fRBrONdfBSlx-8oEgFEbR4u05oCGCxuSE1hMarWLpEyMzd30yL0L6Or7jhSrA4jepnfKPJhdnPZf0v6Bba-5BjrdFCy6xhBzlwAoIOgaFdtk6hXwk5FG4wXKsNMDTXpQTp1Ry_FALQgXnl5gTluFxnLKP4uIBH60mu2NY5yuMR059PNVzux06fo0J_UnUAU_xli_-6Fwb3afec4eZg2yExs7N6ax8c2MsPOJZr8el06xBjdi_YKbPiIPnAIPI7LNbWhxpmEa-7PqC3r_hICroEBAreQ6Al3jlWBFUyG444cwMt3X82sQkQMSqg5ixx_UtatMcoODG1LrsfWJYA7rtl90zzUo1bPoYsC74Yz-Z-T_gaSQrRDZ2BugBANyMcrD2OPUlnFbpUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f38027f14b.mp4?token=IavIAsB9Ut04PbXvnwZonH5gAs-8FvQOZzS2MWrSC60tCN4D7v4O-f3ckhcigTuZ3WX5-FFeCxuJm7WlpznHdlGDSDEND8Fhgc0T8FN5nGkIJewdU5EYUZk-bojJXyzElQEi78PG8pGsOvDXr5aD1He6_xjRJN1lhgZnHM2G-RWccPWdQG516LHXPvKLkamyRdlyoPewqIxrHMUJlyIRYMzu8z7qJfxnvyA9K6JYLUUMS1LP8OG5a3rn4MLLQL09ONTv4PwfIjwR0jJdwjIoWs0MpFDkgn8fRBrONdfBSlx-8oEgFEbR4u05oCGCxuSE1hMarWLpEyMzd30yL0L6Or7jhSrA4jepnfKPJhdnPZf0v6Bba-5BjrdFCy6xhBzlwAoIOgaFdtk6hXwk5FG4wXKsNMDTXpQTp1Ry_FALQgXnl5gTluFxnLKP4uIBH60mu2NY5yuMR059PNVzux06fo0J_UnUAU_xli_-6Fwb3afec4eZg2yExs7N6ax8c2MsPOJZr8el06xBjdi_YKbPiIPnAIPI7LNbWhxpmEa-7PqC3r_hICroEBAreQ6Al3jlWBFUyG444cwMt3X82sQkQMSqg5ixx_UtatMcoODG1LrsfWJYA7rtl90zzUo1bPoYsC74Yz-Z-T_gaSQrRDZ2BugBANyMcrD2OPUlnFbpUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
در هفته چهارم بوندسلیگا، دورتمند با یک گل مقابل اشتوتگارت برنده شد و به صدر بازگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106896" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106895">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gheOMi9XghpkbWQjKmEYjNDBD5tTIFpu0qRjETk9kzpn7iwBFtyw_kXTaDq9zF9rK49OvtubZUDabXA9ZlIZuC02fGfXj6DzujfdW3ykigURTSpFGvxL5L82u0iaNKxTwW2D8TmzFgrIumrq0HXFWXZm869-eGtVHPEsaHi0l0BSDH0rsj1XiQhehTY1LTc8tLubt8Vm1kVEKjZFK-nUryEo8I69_CoiywAFn1eJaOntdSwrZjficImw52jUaCMXPSNY0flYhClvgpYYFmbaWplUQEomN6g3zpns3nyU2kc99q5T4AkXSAu9gk8b5Bx9_HXvAlirY-s8pOSOzYxhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست اتلتیکومادرید مقابل رئال‌مادرید با حضور خولیان آلوارز و غیبت سورلوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106895" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106894">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
نبرد اینتر و رم با تساوی دو بر دو خاتمه یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106894" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106893">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106893" target="_blank">📅 21:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106892">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otG_JQIKR0z3YzyhuHRZoiuVszbKDzMao5ieRBtiGJnATxT7A2niKbkg2YNnmLQa5-jQZbpyia1y-4L8HRCKCr72Yv4UeAc5AllnHblmEJyd-Y3hH0ZiPZ2i652NJI2gxHWdHRMwX5j4Y73SMwH2zPHmrOjPab_q_sMaCq9EzGql7fnOsqOdeofHKduYJX0y39L5DTGw2uXXg2S6-bNpHbO7Cjezd0jerch_zLK3zc_IiTCof8536SpDrgDMc3EhM-pgEN6kc7TrOhUXVZGdCGVkx62FnOpAfutRnvjmPfi8nbtToIFkbsTu_A6023wXOngm8bSBkZOC5Jn_0AMdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
شماتیک ترکیب بارسلونا مقابل سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106892" target="_blank">📅 21:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106891">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d419048b91.mp4?token=hSWWWML0KM96LhMIyhsF9X7e6wJyPLBl6XaeQmlUTMJnu4dNuEzA0319D786saYo85cq3e75ysP0TBhiqRNsY5hDtdiReTPc7brlE3x-7ACk62T5vK3B7uuJ4C9ryeflJY5u1QdQz5TW_xKY2S4zVfB0_htAOP2ac0AaHYatneITTSvooAa3VcYcGewN4LjjN3LS-qQbXmsTJ3fletAd0SLJEb6JXLa2PQSsQ6kS64zIUF619NHa-do4tistDxA1zMhQH9sJhfd0yWjEJWIV606mBOnFRFmN-RnTaY_Vkzc5uFBYeD7ik6xfSMrldxUdwxzZmPvE2YrS02lMRNYL4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d419048b91.mp4?token=hSWWWML0KM96LhMIyhsF9X7e6wJyPLBl6XaeQmlUTMJnu4dNuEzA0319D786saYo85cq3e75ysP0TBhiqRNsY5hDtdiReTPc7brlE3x-7ACk62T5vK3B7uuJ4C9ryeflJY5u1QdQz5TW_xKY2S4zVfB0_htAOP2ac0AaHYatneITTSvooAa3VcYcGewN4LjjN3LS-qQbXmsTJ3fletAd0SLJEb6JXLa2PQSsQ6kS64zIUF619NHa-do4tistDxA1zMhQH9sJhfd0yWjEJWIV606mBOnFRFmN-RnTaY_Vkzc5uFBYeD7ik6xfSMrldxUdwxzZmPvE2YrS02lMRNYL4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
گلزنی محمد صلاح مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106891" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106890">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WPDKikyRHW2G9sZydkDYVyqs7e76G7neokmCK6lc011MUQ00v0qQ9AvmKeHzkSsjkXu2Y64bnAmSYK6CTStgogOwXIUvphhkpXMHbWmVjPEWjH3mx0y_fFPlPSU8zFNmlr4gYjwTIfIYEwgpi_6wXjqPzjhMhtjgneWo2je4OZI6gwDf7g6bmdi3sWEkj1abj4UrFfXzj35PzVGGE0Krhk6Z8GpoS1tTPWqcrGKyyEgHXYdLjCUIvLLVTep1Yp9p33TRVhzbP25Fbbv0bIBSQX6PHW5Y5ql9yR_zv4kwRMeNJsxbaP6llFzS-96m5zzS9s06-PNuEIS1eI_RAMzgSFI-zqW9XH1NdWQUmgxI1blhGLP8gH-ztVBqzsfOCGbBGSLKazuzXyYZ7tPWWLU8hrqeUlJwNRXeugqFtnwuNT1P6722SIJOYRBzZq1id7DiFrTI2rtDKszcMG8nTcjfkZCDJiioWSS5TPf3GagqBxyx9yzciUuLcUHn72NxG3esPij7xAj4KZh_mUUBFcfnGTnP2jRTWwnkBeM1_nkeXtGIH3LZoDkzsTm0HpP4uicN_NcwZUe7oVyiIzYxYbOM-XWrjxC7qa_5SkchQmBA34Qv2mjm2ioylN4yIAtLfz7xTdx7V7Ysn8BufW3hIlOPyIyxIOd8YqmbkPwMkvUYkHY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WPDKikyRHW2G9sZydkDYVyqs7e76G7neokmCK6lc011MUQ00v0qQ9AvmKeHzkSsjkXu2Y64bnAmSYK6CTStgogOwXIUvphhkpXMHbWmVjPEWjH3mx0y_fFPlPSU8zFNmlr4gYjwTIfIYEwgpi_6wXjqPzjhMhtjgneWo2je4OZI6gwDf7g6bmdi3sWEkj1abj4UrFfXzj35PzVGGE0Krhk6Z8GpoS1tTPWqcrGKyyEgHXYdLjCUIvLLVTep1Yp9p33TRVhzbP25Fbbv0bIBSQX6PHW5Y5ql9yR_zv4kwRMeNJsxbaP6llFzS-96m5zzS9s06-PNuEIS1eI_RAMzgSFI-zqW9XH1NdWQUmgxI1blhGLP8gH-ztVBqzsfOCGbBGSLKazuzXyYZ7tPWWLU8hrqeUlJwNRXeugqFtnwuNT1P6722SIJOYRBzZq1id7DiFrTI2rtDKszcMG8nTcjfkZCDJiioWSS5TPf3GagqBxyx9yzciUuLcUHn72NxG3esPij7xAj4KZh_mUUBFcfnGTnP2jRTWwnkBeM1_nkeXtGIH3LZoDkzsTm0HpP4uicN_NcwZUe7oVyiIzYxYbOM-XWrjxC7qa_5SkchQmBA34Qv2mjm2ioylN4yIAtLfz7xTdx7V7Ysn8BufW3hIlOPyIyxIOd8YqmbkPwMkvUYkHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول اینتر به رم توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106890" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106889">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/102cd70646.mp4?token=rRHPu0XsKV_RJOTdFmEsa1KhsuYlpxU-V1Qn9RckSaUJ4FeqV2CkBYqOz07skRZVpl1bGHo7mIuIbo7YxBnK51wjkJ6F9oDD6H2rF1nK_6WjjI3wnyYh0be-TGHr-VV_qSWZrIrstdDCL2nS59MyECoVC025zLspXXdY2YEHFbl3A632Hc4spmGRa4bHR8rlXDV-jpWJ6tlEwhs30qpYvGBbUloefPk8N0XAlVJQ_N_CriOxYwAcOOguNu8EjrWlJBPiaWnyGyZPOcwttsoQYlOQyEWDhwg_l8ySiw7ZngHxapFzwUTIPz616rQ6Bu1tMMOf_Cv1UXa05pkb5-poUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/102cd70646.mp4?token=rRHPu0XsKV_RJOTdFmEsa1KhsuYlpxU-V1Qn9RckSaUJ4FeqV2CkBYqOz07skRZVpl1bGHo7mIuIbo7YxBnK51wjkJ6F9oDD6H2rF1nK_6WjjI3wnyYh0be-TGHr-VV_qSWZrIrstdDCL2nS59MyECoVC025zLspXXdY2YEHFbl3A632Hc4spmGRa4bHR8rlXDV-jpWJ6tlEwhs30qpYvGBbUloefPk8N0XAlVJQ_N_CriOxYwAcOOguNu8EjrWlJBPiaWnyGyZPOcwttsoQYlOQyEWDhwg_l8ySiw7ZngHxapFzwUTIPz616rQ6Bu1tMMOf_Cv1UXa05pkb5-poUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106889" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106888">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=B_5p2DXdJCjDQlGYwWv9odNlQ1aqYGrQAOanuuTwVCW59MQUVQ0DhDzTO4I8NJxn5wQRk6hTAXaFktAAUjM5lwq5xE81XDF6ZkCDhV0_W493y-t1XLqVjkjUpIYjA4LS6iFvJQeUjoeXBPEXwxsfaZmNkZPceP9p2rf4RNK9BID16WF0uGi4E64HDEvaEHn6OF6y8UWqhcF-fh_ZFrAECGQQ7QvgIv_hc2PykkO3IMPZmDwtIc1mHOGuOvlZs3WtV0OjCEnd8GN-NWLxhhfRog3fWVJ2BjCr0i9zIyKfM230I93HYMTqV08d3pJFMfQT6RXjHslZ8kbsMiPun5McVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=B_5p2DXdJCjDQlGYwWv9odNlQ1aqYGrQAOanuuTwVCW59MQUVQ0DhDzTO4I8NJxn5wQRk6hTAXaFktAAUjM5lwq5xE81XDF6ZkCDhV0_W493y-t1XLqVjkjUpIYjA4LS6iFvJQeUjoeXBPEXwxsfaZmNkZPceP9p2rf4RNK9BID16WF0uGi4E64HDEvaEHn6OF6y8UWqhcF-fh_ZFrAECGQQ7QvgIv_hc2PykkO3IMPZmDwtIc1mHOGuOvlZs3WtV0OjCEnd8GN-NWLxhhfRog3fWVJ2BjCr0i9zIyKfM230I93HYMTqV08d3pJFMfQT6RXjHslZ8kbsMiPun5McVoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
⭕️
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106888" target="_blank">📅 20:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106887">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=T2au_wPKdy6uFSsKJzGcWTQmRuouQQRSxU4XshG1IyN9hWT5V4GUJN7QuWpLpyB-tgFKy6OJOaBHqultYzAuXlkpnoagLt5P3iuGGfzEuLIl1i08xV2nGHbgdDt46Yxsq71LRwzXQ_QeOJcpkPJF9gZ1bRipoVCnEhjxEeZFUCwY3mmyqwzNncpeINfJM8HOYyOIM-2wI925j61rt17ZLeeT6gy_W8IHx5Yw9xil8jh3DypRhZYu-VatlQwKpumPH-HQS-H7sXfY_nroosE3DUttgSeEBfcGOGS9bVZvdxsmWaneCfx9eZYWkePgJGSpCW1NNM4Ray8QiVIyVkcfgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=T2au_wPKdy6uFSsKJzGcWTQmRuouQQRSxU4XshG1IyN9hWT5V4GUJN7QuWpLpyB-tgFKy6OJOaBHqultYzAuXlkpnoagLt5P3iuGGfzEuLIl1i08xV2nGHbgdDt46Yxsq71LRwzXQ_QeOJcpkPJF9gZ1bRipoVCnEhjxEeZFUCwY3mmyqwzNncpeINfJM8HOYyOIM-2wI925j61rt17ZLeeT6gy_W8IHx5Yw9xil8jh3DypRhZYu-VatlQwKpumPH-HQS-H7sXfY_nroosE3DUttgSeEBfcGOGS9bVZvdxsmWaneCfx9eZYWkePgJGSpCW1NNM4Ray8QiVIyVkcfgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
انتقاد کاویانپور پیشکسوت پرسپولیس از کامنت‌ پرسپولیسی‌ها در پیج السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106887" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106886">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzD9hx_nhqtw2Wiczu2NMfc5eTUYPVHccnM2MilfB7JiJsnV-1jiRI-N2qvW6OF0vKQuC96WSbcT5fusfov0n3T6uBd6qN5fKjdceZrTxSz0mWkLb5-qXhqQz0YvTaAS_xp1pBuMBeMQcJAghC_6omevj3Dn9ZDd_fbp5l7Qq89L0iBwipfx8aH_eCXGp-c9KAFY_yFmNgWFGYdloXsOeuYDaT427wEyHX927lkey6rsm3rc_Ham5tDA86URJWSreIQQpFrXYpT7BEmfkAvsSnCQnSj6y6rb05u8jjYiw7520ReFZZbMK2p4tiaG6j-vdBzW1U0yfNzc1wLKpjR8L-Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzD9hx_nhqtw2Wiczu2NMfc5eTUYPVHccnM2MilfB7JiJsnV-1jiRI-N2qvW6OF0vKQuC96WSbcT5fusfov0n3T6uBd6qN5fKjdceZrTxSz0mWkLb5-qXhqQz0YvTaAS_xp1pBuMBeMQcJAghC_6omevj3Dn9ZDd_fbp5l7Qq89L0iBwipfx8aH_eCXGp-c9KAFY_yFmNgWFGYdloXsOeuYDaT427wEyHX927lkey6rsm3rc_Ham5tDA86URJWSreIQQpFrXYpT7BEmfkAvsSnCQnSj6y6rb05u8jjYiw7520ReFZZbMK2p4tiaG6j-vdBzW1U0yfNzc1wLKpjR8L-Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل‌اول آاس‌رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106886" target="_blank">📅 19:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106885">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947613cda4.mp4?token=E2veE-pdAg26PAcVvnuV8mHxZn9EPpljJYLPKLT8rnw0dQMLteKKhz-yCElYwclPxJgedaRa7ff68rkl2BSHxcdDXz21mo6DBvxBV0HexcQJnk3jYDdM9muumJtBwk6Q2ZeSDPf1Vg12ZHZ-yNamaOao3X9VxDIx5j_IU26mslc-ZcTzTniqZVoz3MDIk4YBpkfegFA8iVDRUVbfLjnGZ60j-ZQHBSYyaJfaVQkx3YCpAe-htcWJTd_RDSeCGsyayfDca8vMy_n_ZuTtyFzPyU83_yWDhY1_PM9RUzGcI5H4lOimgeWXeW3KAzm0Z6mp6j8Yv43f52_t2nsqFy1N9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947613cda4.mp4?token=E2veE-pdAg26PAcVvnuV8mHxZn9EPpljJYLPKLT8rnw0dQMLteKKhz-yCElYwclPxJgedaRa7ff68rkl2BSHxcdDXz21mo6DBvxBV0HexcQJnk3jYDdM9muumJtBwk6Q2ZeSDPf1Vg12ZHZ-yNamaOao3X9VxDIx5j_IU26mslc-ZcTzTniqZVoz3MDIk4YBpkfegFA8iVDRUVbfLjnGZ60j-ZQHBSYyaJfaVQkx3YCpAe-htcWJTd_RDSeCGsyayfDca8vMy_n_ZuTtyFzPyU83_yWDhY1_PM9RUzGcI5H4lOimgeWXeW3KAzm0Z6mp6j8Yv43f52_t2nsqFy1N9DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خواجوی گلر پرسپولیس: الگویم نویر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106885" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=Fsw4jtHX_6RgZlytHrqbWnmX33NLupmH1kInSGrcLSHeQKmzgkX_eOpGHq5tb1MuMtcG8hhT7eLtvjuYLctqHG-fAln2gd2-qrDh21HV2QIZ9E0WxtUF9bez5SHYuqB_XdwYY3JY1WO-4W4mcmk2LH5jD38gmLpRLr9yA1xWIrvfbLAdm78hW64Vo6ad8CBacCBIHY0oNf_CiTmHsT_W7AhjRRO72UHlAyFbo4y1VThlfxSgIghLsyigCCEsiQmkVOIZ64bIaH4UCM9Mn2Yrgb3smGdDGpr6NE-_8wihqnPKvrjDlc0KEYRnwR2fnHVBJt3L2ogRIVxPxzcpJExn6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=Fsw4jtHX_6RgZlytHrqbWnmX33NLupmH1kInSGrcLSHeQKmzgkX_eOpGHq5tb1MuMtcG8hhT7eLtvjuYLctqHG-fAln2gd2-qrDh21HV2QIZ9E0WxtUF9bez5SHYuqB_XdwYY3JY1WO-4W4mcmk2LH5jD38gmLpRLr9yA1xWIrvfbLAdm78hW64Vo6ad8CBacCBIHY0oNf_CiTmHsT_W7AhjRRO72UHlAyFbo4y1VThlfxSgIghLsyigCCEsiQmkVOIZ64bIaH4UCM9Mn2Yrgb3smGdDGpr6NE-_8wihqnPKvrjDlc0KEYRnwR2fnHVBJt3L2ogRIVxPxzcpJExn6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جنجالی یاشار سلطانی خبرنگار، درباره چرایی برهم خوردن توافق پایان جنگ از سوی نیروهای سپاه و جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106884" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7X5RwcsiFvLwn58zXJyu8dYqDTD4HiLdtvSkXi7m2nrZpacUb9yN8kzdJceZuXfM_Bad_bcuD3Aj7rCbJa4J_JeBVKEbL306IA0AITdcR1aqbZR1K71Malt4hRWuhSMmNXlHawlljRM8MGk4Jku169EUAiKBbmSptu3KOknVpjlktHDSkBJa_mT3Bt1YZ20iCVPS1lrgyb_VHPktOqQ3TJS9Nc8GENw5onC2R3r6HTXrnauBi69mWigvi_uKTLRPEhV-cHMQ0hq0FBrqc_pnwvvdKpMbLVkbv4kmMsY7-NS5QQed7WWjoOQIeNs6J_ZzlBpL6BTejSx2or3NZsFjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار جدید کاربران برای تأمین نقدینگی به جای فروش طلا
🔹
با روند صعودی قیمت طلا، فروش دارایی برای رفع نیازهای کوتاه‌مدت نقدی توجیه اقتصادی خود را از دست داده است و حفظ طلا و استفاده از آن به عنوان وثیقه راهکار جایگزین بازار است.
🔹
وال‌گلد و بانک کارآفرین امکان دریافت وام تا سقف ۳۰۰ میلیون تومان را با پشتوانه‌ی طلای کاربران فراهم کرده‌اند. این تسهیلات کاملاً آنلاین، بدون ضامن و بدون چک از طریق اپلیکیشن وال‌گلد ارائه می‌شود.
برای دیدن شرایط وام کلیک کنید
برای دیدن شرایط وام کلیک کنید</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106883" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8b096322.mp4?token=K7JGHe-1Z1b7HdeYl16Qz5VKxsHsEShnMyyaur4hO92-9xBKWUQBhDRmgEltchKrt0l4p5WygezVl0vt2MAShNz-t5sNSWq64D1BIXyfKTkvabzzn-j_mWb46laTL0gIo93c-_lsv17DNtdrNx7Xk4urecFSmgiPmaaL6qKtA0LNE_Mn26Yjp1Kzdu94lpVBqJdBCXaQP91WAvT1P6eVPfUchKljMgpHd1tGF_yx3kntVD_EzCz6GSwsmluuhIYqP-vax1NTfBQrZcAI9TQgVsRcCUfEpPFbp7P421TgmlL-Z1lMLESG9Kw-NuOAZ9-CKarG9bbvbOGHKb06yidUfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8b096322.mp4?token=K7JGHe-1Z1b7HdeYl16Qz5VKxsHsEShnMyyaur4hO92-9xBKWUQBhDRmgEltchKrt0l4p5WygezVl0vt2MAShNz-t5sNSWq64D1BIXyfKTkvabzzn-j_mWb46laTL0gIo93c-_lsv17DNtdrNx7Xk4urecFSmgiPmaaL6qKtA0LNE_Mn26Yjp1Kzdu94lpVBqJdBCXaQP91WAvT1P6eVPfUchKljMgpHd1tGF_yx3kntVD_EzCz6GSwsmluuhIYqP-vax1NTfBQrZcAI9TQgVsRcCUfEpPFbp7P421TgmlL-Z1lMLESG9Kw-NuOAZ9-CKarG9bbvbOGHKb06yidUfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106882" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmPnz6EfMlz-39wQzwwdvN6K7Cyv06EB1YPGtmcGj1bne5d5OwE6upSS34KC-aU1NtOdoItoD4UdwVI52oeObceIv1ZHo7kdSvlu-YFHezuGDh3lIf2fPpZoDGXqUJnr8iE689vvRAmUrbc7YURu2hYjPpsPqFI3mBfkEDGXH1ZvoEi-IlX3XPJReZrbeUQzP5QdxOuNwLJS_Pkk-4ylVmC7SDfG9gpN5ORqKSr3xd3bY5RzzBK7o8dbDETd3bjlOJ5eDqYeTyTPxSOG0qBkz3dt39ns_ot0shg9CrI0xXaA2FyYdjf7QP-Ybu4B56j7bXJQvnsJePgLHe_ZAMDwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اینتر مقابل رم؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106881" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=HEiIURnHjMAVLC0milgRgMUc-rShfqQ6QsHiPgP_Tmc76gUrWdxsovX2p6C8k-H17JamwrDT7MlaquGHzOMEVaySbw9ZH1CO_2oYO0LFHBPztPxJm3VmNJqOmN3ICE1E5Y51vHeHfGuMgx2qqwITPTSCiAe_ewgVbtmBGo3OsPJ2sYf_L0domfsKYT20vIz5U-DdGj-G7zrcoSsgSeWMa1n5tBPT8TewUCtRIn4p6DBq1LbwgC-Th6DlnS1mJCoMYG_xhhca49RGn6SB4rMm2UdNppA62DopDfJHHbW3M9XJACT73_7ztH1TQ87-3pnpcO7oORVuSW8TVzj3ysM9jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=HEiIURnHjMAVLC0milgRgMUc-rShfqQ6QsHiPgP_Tmc76gUrWdxsovX2p6C8k-H17JamwrDT7MlaquGHzOMEVaySbw9ZH1CO_2oYO0LFHBPztPxJm3VmNJqOmN3ICE1E5Y51vHeHfGuMgx2qqwITPTSCiAe_ewgVbtmBGo3OsPJ2sYf_L0domfsKYT20vIz5U-DdGj-G7zrcoSsgSeWMa1n5tBPT8TewUCtRIn4p6DBq1LbwgC-Th6DlnS1mJCoMYG_xhhca49RGn6SB4rMm2UdNppA62DopDfJHHbW3M9XJACT73_7ztH1TQ87-3pnpcO7oORVuSW8TVzj3ysM9jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106880" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگگلل آرسنال دومییییی خورد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106879" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106877">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3613208345.mp4?token=E5uTplTXyDvLcZfnb0yrtXfHt4xJ5HTaNboKL79TXdxF5w_f1w0UwyluGdxpvhy7_lZpNnbBKxfJ0lGi7wGYip-hjsWX-jj5ccQZc3jBqzK2BnAwHtxjYVcQtlukd50ldb_ZW79Xhu6IgpkuPdDSlhVt0Jb8dNL8PKuUfUpxPBFDMysCDx1FvX6OOn6VzUPZwvq0YJOv7LPFFHQCZtMwwtLHrOk13bALQE7L7whF_4TZeJ4gs8Magb0sz0N_7WpgotcfYUEebLVOlU_LC2YJUG8r5U4dE67z8hwHwMDxM1pgC56Ib1DZbVGRn0EOQ93XboDoZ8z5IDUCjVp2SYfbxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3613208345.mp4?token=E5uTplTXyDvLcZfnb0yrtXfHt4xJ5HTaNboKL79TXdxF5w_f1w0UwyluGdxpvhy7_lZpNnbBKxfJ0lGi7wGYip-hjsWX-jj5ccQZc3jBqzK2BnAwHtxjYVcQtlukd50ldb_ZW79Xhu6IgpkuPdDSlhVt0Jb8dNL8PKuUfUpxPBFDMysCDx1FvX6OOn6VzUPZwvq0YJOv7LPFFHQCZtMwwtLHrOk13bALQE7L7whF_4TZeJ4gs8Magb0sz0N_7WpgotcfYUEebLVOlU_LC2YJUG8r5U4dE67z8hwHwMDxM1pgC56Ib1DZbVGRn0EOQ93XboDoZ8z5IDUCjVp2SYfbxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل‌اول برایتون مقابل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106877" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106876">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox-mM4p2QFpege2j9ayrc26HNYBkVsZoVbXv5hB_0KXzJdGZ3igTpTt1OdsiDOa1QeVFh5o6fnXEl4Do5oFCt90ScvURy_OHStYaEv7i2KaSDaz2bOlSDyC-Z1PrkP2llqYAL4YHp76uFMVXPz5Ms1Ai6ephNryO73if4Z3cnoWbfxfMS8dhKOgbk0Z3MKd9dsN90l6QHbOrT0q0NAGh_Q-ewBKfZV-p5IPI3Gb53OheXnOB7gGkb2yQciqnbdoq4iuVBU6eb0WrUzZ_pfHudQ1nHNkzgrzLEeVn75SDIuIoQ7Ke6x7x9WprcfXTp8jmmSQX_SQNAP1IA1mahs33Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106876" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106875">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyvyKUb0NRwIAelvYsCj17NN1EKhmw30o9SNN9MZgQBQUY9R0ltzLJFxf0IqkjYV27yR0dulAsD-IG2KRq3Hu0yrUj3MJCoBw5UB-WIZaj5JcZK05HKMNy1G6pKpIL0WCF5cr7Hc1atk6RhIi4_wMGrIPYxHshvwPn5w8pO04aTYGKvI8CSZxWRMXyxoeotLRGA1hESKZWVKFH-K3j5zSCFWr1w-dNMvt5HW9ttaa2vnCVw3T4xVl0-wO_Se_IKEp6oCbYFL0L6ry2T0d7pGSIiRUS4RsZlWg-WvJuGkpOMQomLMbP1el7Obnkr4sE6bK5WdSCdah320XYoYPrbZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106875" target="_blank">📅 17:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106874">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=n4971dJlbJN6tlrnKxI_L-h5xUcre6LpbxEQy-f4CA8gqTTk3TPT0sb97RZsNA3HLkkQxrDLnelLEIqzwjTJyhG_vx_EawOT8cRxGFk-fQHgBcKsy0S-zzeSdJDyN8F352hrjPpBiD0vquiSuNXvxG9OZfau-HdS8Ak6pnLWVHKXKymLCnIIcLUIqgyGqZ8kdN3LLkeKFaUAfhiwFHVjpxKvgfL08dQmBJoK6sa15dukCqtFxdiVL0JfRYekoMLCnSXdCVLtZSAuuJyMUCMH-IfWCAt_U3wQIsNW8NXSNUw4JlUFQ8xF4TziCJgGj_BK4e0zuvUdeiHIilpuXDE_goWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=n4971dJlbJN6tlrnKxI_L-h5xUcre6LpbxEQy-f4CA8gqTTk3TPT0sb97RZsNA3HLkkQxrDLnelLEIqzwjTJyhG_vx_EawOT8cRxGFk-fQHgBcKsy0S-zzeSdJDyN8F352hrjPpBiD0vquiSuNXvxG9OZfau-HdS8Ak6pnLWVHKXKymLCnIIcLUIqgyGqZ8kdN3LLkeKFaUAfhiwFHVjpxKvgfL08dQmBJoK6sa15dukCqtFxdiVL0JfRYekoMLCnSXdCVLtZSAuuJyMUCMH-IfWCAt_U3wQIsNW8NXSNUw4JlUFQ8xF4TziCJgGj_BK4e0zuvUdeiHIilpuXDE_goWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
‼️
🎙
ماجرای دست رد مهدوی کيا به قرارداد ۲‌.۵ میلیون دلاری!
🔻
مهدی مهدوی‌کیا: مدیر باشگاه داریان چین بعد از دوگل من به این تیم پیشنهاد قرارداد ۱.۵ میلیون دلاری را مطرح کرد اما بعد از جام جهانی به دلیل عملکرد، خوبم آقای عابدینی رقم رو به ۲.۵ میلیون دلار افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106874" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106873" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106873" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFJJ3xU18GR2K0niJazUxVNX1Nj7z5d2SBIEFji7D2ON9WknbCaFgTQRdj9eH8ZMJQBKaNQUCmsC4_G6Ie4b6hv7GqcqZ2Jn8eBQNto5NkD4yXM3OkE2AvFOzOzoVaydFDSuZ4jlt2rCz0FFcp6iZoefWYea2mMiKRxMnqAaPrUEEaowEtadtv0Thb2iOlFKmbC3GYf0_AI91HOJrj6s5anZRdNANti7En4FVt56-yAk7gMtxSr25745OWiqyXHfgUNtPLewbogrRi66KkV_lF9HVc1uDXtwGFJVkjKTz8tPwQXooiax0K1B2DNTHfCHWvv8da3AlDcB_vNB9nYPSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106872" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLNxK-gqC4nnqW-6VONnfEQktg9SwsKecau7cK8wF6yVoE823U0v2rXa4renFrfYrEqhw6GglzqLx8RE2aHEy9wuFtBEkSWBv80vJGDIESL1pT3y1HktlFSgU_oWry8h_HOCqMkt3ntS1H6GwU1iA5R3w1ZJzv3skBsrXQwzHOXsjtsr9FPC46rIY4C4tds1lvJBC62qqSvMdE1ONhcUlVT6qGGB36Cc8Psr80NSmLr6jzkVVurEdkkGGdTmnI5JJty-jaFJh25eQuoDBe6Ap1HoXYl6bG4b0_cPreikP3oDZ4P5nZgOiBdJMtAH4N3o4CDw7luk8WLL4zDhfLQbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
ژوزه مورینیو در پاسخ به اینکه آیا از شرایط بارسلونا نگرانه :
🔻
از نظر تاریخی و فرهنگی، رئال مادرید قابل مقایسه با هیچ تیمی نیست؛ بنابراین من هم خودم را با هیچ تیمی مقایسه نمی‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106871" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwDZl4Y_-oXr7bEspDfvLtNlCPDm9CHSZ1b2RCyZrFaVACU4L1rvyDxRXQDJbkB1wRtLwXmpKbZBwfcF06anbvNQhWyctPPi3dAbW0wTcyqm-4ifWtylyOecTt8MlNqoLQd5idJLqF3DLm9ghFn1DtEdF4ROEqXIYCuVIlc21HcKDGVV6rDZPEIn_WOZs66351_nR4c1B_Gq7cNdYp3Sft7v1brvlu_iLT3KryrFqWP2hOabnmgGMB457v0gVGnDEcbuK6LNrxrbRBNbNuOdqWbwSx0Rtt98e0H5dWwuwYQ6t5HQsx_xP1da-wuCDBbj3ILFcI5PVoSN5ZtDlN5BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❌
رسمی؛ مجتبی حسینی با توافقی دوجانبه از نساجی جدا شد
📊
2 پیروزی - 2 تساوی و 3 شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106870" target="_blank">📅 17:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf935413.mp4?token=k29PO5LMDNOvi2FVwi73BGP_0D2hu5rEbKCoaEDq7n4UVfLJhVG6SkGrRLfW6x1-6rc-pBk_K3ChqhIETCxQlbv8AHlMJJDSYoRr54LK_WZOj9a_4tbjs-GhHt-BrIfRKfd5aN6Q5hPFhdmKpMzgu9zEgtoao_eDhvrN3oZyzWBCVLUEnRY3AKkvNHd-r-1_UUWgRqKhJrP5zBPnm70zs2PvHNmw-sJJ5NhM0L0Ov36N4tTpQsc0nTqE7wOSLOafv1Tha2JwL4-UPWrY5TiHYRYjE5sIVGZ9GObzX2sqhgGnDcglkhOPpPUOm9I24eccC4m4o8PZbNARxQl_lspf0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf935413.mp4?token=k29PO5LMDNOvi2FVwi73BGP_0D2hu5rEbKCoaEDq7n4UVfLJhVG6SkGrRLfW6x1-6rc-pBk_K3ChqhIETCxQlbv8AHlMJJDSYoRr54LK_WZOj9a_4tbjs-GhHt-BrIfRKfd5aN6Q5hPFhdmKpMzgu9zEgtoao_eDhvrN3oZyzWBCVLUEnRY3AKkvNHd-r-1_UUWgRqKhJrP5zBPnm70zs2PvHNmw-sJJ5NhM0L0Ov36N4tTpQsc0nTqE7wOSLOafv1Tha2JwL4-UPWrY5TiHYRYjE5sIVGZ9GObzX2sqhgGnDcglkhOPpPUOm9I24eccC4m4o8PZbNARxQl_lspf0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
سکانس‌جالب از قسمت جدید مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106869" target="_blank">📅 16:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106868">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=mV2bgomnV3lLEZ6AB82EfKldIU1jgSDUfKmLAJyM3uvraoteCFP7UCZx2RNLAklxIxYEPjkMCflAvrs4Vo0ds5eRPrCv7fJgB3XtyxE1f9l-OQBx9jCHPdstH3IVKwaa8uR4wMZxyY3GfThe_wuzQEwzk6r5wcFqk3pIHfWSGB2n9gD2ZeTK_IfT6Tp5rO4CxY6qMsxs73urzrmohf1foToPRyC7vGlxZXWmMZ0WyTlkNbBDdxqDfgzV1ZCzsmdYir-Ms0O0q3srsICVOrjlfPMAGfUuLxqlBLFJESmwwHcmw186xE3vHkauGNcXEcMKSsyIvPxUJRAlnNo4esNf0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=mV2bgomnV3lLEZ6AB82EfKldIU1jgSDUfKmLAJyM3uvraoteCFP7UCZx2RNLAklxIxYEPjkMCflAvrs4Vo0ds5eRPrCv7fJgB3XtyxE1f9l-OQBx9jCHPdstH3IVKwaa8uR4wMZxyY3GfThe_wuzQEwzk6r5wcFqk3pIHfWSGB2n9gD2ZeTK_IfT6Tp5rO4CxY6qMsxs73urzrmohf1foToPRyC7vGlxZXWmMZ0WyTlkNbBDdxqDfgzV1ZCzsmdYir-Ms0O0q3srsICVOrjlfPMAGfUuLxqlBLFJESmwwHcmw186xE3vHkauGNcXEcMKSsyIvPxUJRAlnNo4esNf0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ژرژ ژسوس سرمربی تیم‌ملی پرتغال:
🔻
کریستیانو هم مثل بقیه بازیکناست؛ اگه عملکردش خوب باشه بازی می‌کنه و اگه خوب نباشه، بازی نمی‌کنه. آیا جایگاه ویژه‌ای داره؟ بله، دوران حرفه‌ای متفاوتی داشته و پنج توپ طلا برده، اما آیا این چیزها روی تصمیمات من تأثیر می‌ذاره؟ نه، اصلاً.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106868" target="_blank">📅 16:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106867">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=Kh7IRgdB6i2zFQcyOMxyHDWSbjWqhuIwGsnx-HaN4jHIkJ_J0iOcFu7WmTjzoXp8KOVp0G_dhQEi_0be9MZ4gvtMK9g2YHueBt73uEhExjtE9MjjNdTZ7GR4wfGuSxqpf3PU_sKrDKvafDnuG9L1vt2mIjnxfu5VpUjXFgOeR2oiZiKZtMO-Y4UUgsuzD0lR-r4izYrxs_OO438uztuBQ2UuRRL8BkP6-B7qC8T0wDRo6vhYNYJ-lnpKAMUmsVSorQ7mImjrObWefLmTbCPENWaMk1atpmcQH9rHeCIpPAKEsItbryw82Rpx4hlAKlm6X_Fw5EsiTTP_38ZArKVGRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=Kh7IRgdB6i2zFQcyOMxyHDWSbjWqhuIwGsnx-HaN4jHIkJ_J0iOcFu7WmTjzoXp8KOVp0G_dhQEi_0be9MZ4gvtMK9g2YHueBt73uEhExjtE9MjjNdTZ7GR4wfGuSxqpf3PU_sKrDKvafDnuG9L1vt2mIjnxfu5VpUjXFgOeR2oiZiKZtMO-Y4UUgsuzD0lR-r4izYrxs_OO438uztuBQ2UuRRL8BkP6-B7qC8T0wDRo6vhYNYJ-lnpKAMUmsVSorQ7mImjrObWefLmTbCPENWaMk1atpmcQH9rHeCIpPAKEsItbryw82Rpx4hlAKlm6X_Fw5EsiTTP_38ZArKVGRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
جمله قصار فنونی‌زاده خطاب به امید عالیشاه: با آدم بی‌ادب باید بی‌ادب رفتار کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106867" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
