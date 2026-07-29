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
<img src="https://cdn4.telesco.pe/file/EUTkv9_pExAVTzFRvVPwypqc9r5yOzF8Ov72Gd-vinh0CNWdaFAw7Q-0enw-ZMGxeK1EaiMAbE3PdLs3At1u8MEpBOK74y_Cufu6f9f4kjsG6rA-QAq4SMbNocB447Kfyz7aDXoq9Ywn_h1gkb3KYJ1jh3DRke3r0a7tm74cyFU_jhgUS7Q41nKyeAbCBpQytQ5q38OPbMFZZY8VZ231LzbSKb9fQUPJpjgHBfASUIv8Hf34oixz2O6n0HjktzuVsZXgWknt5bhd0ptQfsTSxZ4jWAOdRHo-BMWtNwJUgYjxViiWuwQ9p1Eu4QSTTP8jlO7EmyJhx93vyCwtqndt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 613K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=IE1kK04tUn2gm9jJKidvaeSWSSxNaCdVMtNOiHxhY8Ct3vaF_kzkHxn8kXCPh13YDf2YoIPI_m0YE9XhNSW2t6ArkSAbWsRymZa5sTUsmJ5uR9ppVMrXPoQIzhaUVWmNdS0h5eC-HGM-W3yrDayRa9XjZE1qBuzvOC0fB7OiHd_2KlYCzMZhYmjRXoPN8H86Datuo_t4zFA2SxNtIcXwYR7A19pGmugUG2QV9hf7gEyrStoEcPiQKCE-ePj7MiyVGq7i5jRmJpfsTnORfHfpp602cY4FvuNvA5LaxKhRkovgUYK_JTJmyVUIT5LyKtA9f5boTr_a1gVGtiHLJl3yEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3WjxLUR8ANyWMrTsGW5sqhcwsbcCJ1veo3yYbk3zCyxcr3FxDOAaZvab1-jmqvW1CQW4iqHZQIbxY68u17pCZw5iSHOusdEmYISOG3qBkfNWDit0tomdkogszFN3bN-GvodSZ3uNZtVJ9K1JDMVBXRayIuvLMzszBQqyZL_N4MbrYo0_0p3iI6sdGMEJ-kbTJKUQG2F8Uo_AIE6hBOVnQo58v3lg11PR1ws45OuQ0_VR54EpnryV_vCQnF4N1tYw1trQNe8kx0JxeG4IrCZfKq3UmchZB9Eiu5wLREGBRC-8e80jv3_tcuRZPq8p1gBOED_N8fxOc7PYHUycst0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BneAuHU406W6H8LXHJ2fEXrO39dP-7yqVcCvr9NUiuSQ4rXIqyh8fpYAiB2YF6f-ndj8KITWKjG-_9tlbl8g2BLn8m-jI5La9YqKAYQwVZ3m2HBMvh_v-gEEO0pjoct30NWusRb69SkyeWLBvKgUMShrTwRfgMAyl373JS7KGcfGHKYoB8rYMxyuXDVA5KHUZjg0L34Rc0Mbnb1b5reGwxWYpKxgd64b6CIxU_nu5yKNbpI_8eHtN_CFhqdM8TM-ZhTCjH5m6osbpiijawifC05xhYlw_2slbhFoK3dXmPK2PUiG46UiqCZYNyFdXULmGgTbCEO42xJZe0vDM-Z07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=e4Nqm2d9hHLsKJRblboK_64MMMGeLMJXGXfBpiJOyZhUpzLioe2Asfkx6ceBqOn9zJ6pauoNvCXbkOep2wD-tAI1hYrO2wj7lwRdRWZwQZvQgzV2P5Wpxoe-BCyPE2ftsrWzOXAq-Zm9ziwmSpfWoKRvQEcOG1_VsYxj_JsxZSn2Vrgfx0pcW06e7ovpNMY36RlrWZ23Ef0AO079d6TDGZDcBKyiMVxiSfhwrzBlQb6_BHgSFC9Xlnj5qn5j2UiopwKPTowh1IYIAXmbrzzNfuwbsSPJTesmCzhf8GNnCY-QDouBrSJGUnqUyZ2-eXl9ZikRlzQola-lQaVuD3bQkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Ho4vjv9vB3TjASE8vHv9YHgIXZ0F1yYCnb-mB-zGdW_pFPhfzeV9xrsEXa7X_Fo1nAeog_ErVFTIhr3tVk09J8L9_7yEekUFoWv1fWiKj8_4lNj3kIG-CpUl1U_o3UX8ai84iQqivOQMV1LRwxFTXvfqcRSgX1ePdvxTOdYQqlZWg8RWSrNGOXPTK3ketYIDjRa0j9TE23kjgRBZ1TdMwpw3cUCiQcNJEd1iXqut3vvaxOdqfG_ZywOgZHK8ewbk9Yb-LT5RIkKGXtbJxsOEfgQTkDrQIHfw_CpJjacfrSWEYMyjLNhe3tXNdNTRilhCA4OztcxFxZvvPmaxo6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aknC9ltuYi57cb0QG8CX0uhpd6aP_UTdz5baGB7YK2a7ahVgU2uQaPH0GzS0hxJ0U9zbefq12iu4tzgh1uDa8UfVm33c-Q17LodR4ayuBDkiDrytmeUbmGcdnPuk6__pnKdUQ2JiQ2wmZWHHCC0FnYcm9e_vp8a2SC83iK5lAleXYicUm7XbM-O2tqy4xJTQjFHZg8BVV3RqyqSv3Yac0z5pCbijr-voN75nqxgqPCusRwJwKt70S0x2GuUrnSN8xA6chACFqD4rZ2bHM84Or4hl874fSrN7LzTQXOoJNo8iw96R1k8xxNChBRC7OuxOtXaHTyT86BUg4XP5DpTGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jx07aEeIkAoCI58EOHj85eZF7h8S8-yIj6rTUldIs0P8fjmI9bbieUryERUkZa5qwfwkLHM6UltnCBQ7cx6LgoUF-k1h1Ur5woSuXPWsOeRulNJpUZJwsjo5O1I-6SKMUj0ZM3wkNyezmOsAtGux3TUu6FM86b9HoNslBLRQKXdAYMKlkIAaEGF8jQfIB0E8ROgzfWeSUID_rW2I5rUOSfvDWzjww7FUYTuGWsOoNj1fK2-QJ50gg53qpMjk_o6tIkimLIWFBeEmHowO9S23d_5kQR3ITNe8rfnKbD4gwbS0_jdh7yAawly1x1izASmDdYyZVT-jO6-9UzrecgohVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJF86rxGN9cGjhwYZZ3VCABt0UjtLI03pq5FDAgMjDlBFaTFCLfbOoeQYNux4hZWOtZ0RV_FJ9TMri6EIEGToKrYpUck0146MPQy125s8QxhThr91BU6UmDrdn_vI-SxHLA9bKKo6KXjZjL8v02-1sHjKtCXjeKuYBHXR4IQYGsEM9SVXi2zwqIPapqp6y2oAISDBbEhwKU0Ep83jLaEufhB02gKWwLE4a_f-HZBHdBx1gs_agY0U8Rutw8lVbKQbyY_TCwxLSNgThW3lEt4EU0ET3v7entXyjzJI-c2qM5Nw4jBkofOoFZmdqmIv3_noAlNWKzQPr8JISIz0nVJRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhCjIDt9twmOcctLL8h_dAM6V2CSRtiKHkiyOqgogge_AUMu2hk7a40bRZjZ0kVovsZJSJwMcYBZKuXNslWuDKg6HCt-jPak7v7Fk2eKB4RcquPYvLMeHr1XfQT4ZVkipR0gfulb-gGu1gmHzTzHHyncXvOJhDqm06-UMZ9d547NWKKtu-gd9IXhTvY2Kg8l-pW0_XYAY4BoFwYaprSPiHS6dCx2k5fc9RI3e4qoELfArJvvadH3xIw-5Q5Sd3WRsmLVnsRRwOmKyH0OyXmM6VG0LrcMhlCsxVaHcouiNhP7yE9q7UH1v7loWnb6BOCZGO6ZcM5lMPes-GCoC-of6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=kzl2cq3O7eyRQtB-aSw_o2yWN4KRMkHmRKEPtXjL4kzyaoL4oTWOnWWmh5q6GoLPaZAwrTyWHMpKmHDI5SWgcgigdLgL6tW_dG1BHDvgNdfcVTOkZnoMDpTVHHlrQwkHoDt_PeQ4c0IjMuo6nvOabKEc5B94a-47UC4TiF4Ndp-L33NkucXONxCb_IHcpqkXQYY5LRykCP-RBw77RKTc_wwo7OZHshw5VuypQjIVgSKE7poyWMEMld80NIgH4M9IpEEOZcFhNzNmtDAHvQisuNxWIq8bO5H1jTDNwwf70FTdBcEueT3rVINTkL6u1HKxkqOjdM9GGt-nFVGQh5OWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=kzl2cq3O7eyRQtB-aSw_o2yWN4KRMkHmRKEPtXjL4kzyaoL4oTWOnWWmh5q6GoLPaZAwrTyWHMpKmHDI5SWgcgigdLgL6tW_dG1BHDvgNdfcVTOkZnoMDpTVHHlrQwkHoDt_PeQ4c0IjMuo6nvOabKEc5B94a-47UC4TiF4Ndp-L33NkucXONxCb_IHcpqkXQYY5LRykCP-RBw77RKTc_wwo7OZHshw5VuypQjIVgSKE7poyWMEMld80NIgH4M9IpEEOZcFhNzNmtDAHvQisuNxWIq8bO5H1jTDNwwf70FTdBcEueT3rVINTkL6u1HKxkqOjdM9GGt-nFVGQh5OWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EH3BJGSWqYoutgI9r8-Otc4BI9IMj6rddID-Blw1cb6rj2ygSQJoxII5wxw2byz9mEzlhBwt1JSq8VvgBujvZ4lGi6UA8uQ0PwCx2EukAnL1ZyqJb0qWSoyNeFp-Y37jq2657BZsIP1odv5HjcyLXad67jjAkOMKxmFjiWG3BoZtlUx82Q4UjhQ8kcLQJ_tXXRh04V9RG358aiW5nRu2I3sjHLgogBS6gFh9k5F5LgHFhrmssZZSY8TyeXMNakeQrwmfvl5XTnmmz8nRovMoTgsKDVoGQt-NsNeLuXe3A9osWkTDMPG0JlBKg-0s5up_EZlM44-gmIB4DuQ45YRbnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juPhyuGkucOn07p6S4xROgtIRoHs3_r1DiSgP_UXtPteZTFmT1YVbAYHl5TKSR5HlzlTj5Mwt4OXPKvtoOVWqKPbJJb8lijDiQdhKS5CMx7katpI17GxljxKrpqmWQtuIwpgAHJpUUTjbV0nrfrSilm1zGgnJky2Cl2K9DlN13sWUGya-1jPxeA_H-kpXKy63CKmboauthgCOiiR9muAqIn3wWaYbffgkXytxi6BQkFEvYmlMrIYxd1kxaM3le4dL-uTZG4zI-9s3X8m6maEy6MyBFB2dHZEV6y5sFDPaX-jC-q18HLdCXINyZw-HLo5hvoYCMeLE0ZMYCwqLsL5Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=g3DwGNyBM4JRmL5XiwWrLndyWjELxINbJ6t8Y3b4Uy4f7mn8YxOYBO_qxnK-rblrv4bnSdwYT-VFf7KK3WoYduEHg7ZUJF2n7dRxzzhSLOomudOXNbIlZkGeUMsM2CsRozsoI5_U3WC74DNhjINOyC0wnnMY_qrEcztlbBIREF9w9f9EcDFd10ag2GcjyzFL2dhDi2G883ioznVTZuV3ySrnvt5b4zujuDr3tnz0SduWbwN26zf386BwgtOZYHJIE2lNqK-jyj2tbglGgaltmhFcJ351OqjjTJhSAW-mNIbQrWSqulcSfKA6Gvo7eYo4Zz6IVBIYnHMn9ZmjB5tnp6Z7g3la3uadKUXOJDCfGiEkzkGzOINp31W9JtUrle5P9u51HlICjmWAZ1voh1fYE3Cgoo59dzDMDKON0D-y-yufTZrOfWBtXjyDNIJn9CtOOeJeULZqgwNjXwRFvOl6h4a_nWvRIbljfbU7M0sojT6oxUTHktaKvclFU3z-iDf43HNYnh1pUwsn2GMNuwkaysR90sDllKqurNRvzVOsABxe70AwTMl_gBeiA5wPESv4ilpSOst__G63dCP6v4vc7z94vPAByNUsO2EfvKPjYJYv9KIpL7TQllb3QYvf8Jrg625I6ImMGwEmcDekbkczu4Pgperm-Lcnicxv58w7mzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0JvGmOW-sssEO-QTodu3KnwnpQx8K23chxDhcXoWWQux1A5nnxgmlqe3puc1OBuoPC7pvIGMFqCFLKQGm_9HyPWuwxXYvbonf0HN6065S-FTubLHXFzkebNcCCbz3OmLNMwCtfsx_jH37HJpg-7iji3XWagpOXV3no7d8_di6vdc931KiiBZRgX40uRlyXIeJMozNgI-vS_-OoMTap7qiZZEbKAaBembKCOmPz6ytqczCsuszDFcB3BLKnW-bhjPqfqOQrGRW4GOnaKfIj4ZFuA7QpqgZzxvbJk91E9pn83Ml6MJCpfAgAYs0wJYRpyFLFteaTBZM7qh2vGlWnJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gICxKefYIbtW0pQYauMQ1TkOhnm1jAP_--iO8r19NzHk1KOtyoXLYAQpmrNVqf03Vp-22p7Kifpy1MHmaawU3oX-DwxQSXpz8waz1bSzCUCjB08whVvZ6lcKWZgist5s_poD5fyI80slDqNaeK4WA5lokjuYQvcWBLF49IMUfk2dwO2LedQpI0q9Fao2SMV7D8tWToeQbBhFqly1QDMBcFsgpJpdRQILLoB7iOgAtzDZw7GPF5Kr2kcwZcdgA6HMko7leC13q6kelXplY4ST-S5D9OJuACFKVrdBovKKYVR9E9oLkhC2ZUh-N282dvkGK9mZiZNCCMDSGO3CnnSvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=Ys5tQWALWk1tYgkroqs86UvcNm4UeHN5y8Aq1fi8RVxkhPwFEtbRT-UcJTna9vRCV5QDk9bObJ20wIlTPj7nZu7mtU4kMam08mkNIDOkj1B3rMgj3r2X9KZYUN6GOkOGN4lWsDPaM13L5lDN3LLsFDtel-vPdvDwkPSusCn6mzechnUsl7vqd7i7YC9qTns9bjVZqfrPKHGF_B0TkdeXFf_eVFFCz7dWIjYh7rnqEjhOmTn5Y9yVvc3fo0EJOaIw706VRMHCHPrDRaGayb92HT8YIJsnSEGRs8Qx7tUHOcoTwwr5x0oiJMYS4rdHmc_xezFAg0cwnC_VzpfA7_T5OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=tmxiiD4tybqufyVNTrtxZy5jGWp1E78FyJqaDVJiImhlLL1pUewUDHSsDMfJ3WKy3OoumphXWNWwOPqWpHV57ypc8Q7QIM1xF34uNQFplENgJEczY14dsmt69jxe0Dh3HG79tcmPR670oVMcQsJo21Bc49vssJwGgjTzkrmVHkuMT2RJL9HgyPMWCFrjG8FjvkCjpflhjw-YBlRL_wfhKva6FJSpCRu0cQ_GTY1xXjir3HwGTRN_L9MMpI6QlJfHhyxHXfSGLJi_DINWnTE22O7HOKYoMOuNQGNZ5XGm9Hff1Ww7t5Vb1vz7fxMK8JD5jHN84gSEAv8gIxKHWFmZlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6A-dc0G77Z3YzAIYcFVjhnqAby_RIG-RHw5oRwORuxGNqwPbj_ZMyCVXbcYoaOMZTPGpgi1sTWTjdmYwWhyro7SP3TI1RBby6KqqOftd0NphP6MUAKLwPlkZElREAM56XJ1RVOLZW2FVZYE5wZlgE8r3_tCjmgACR6UgRHm4VRGvkwswJ5j-FeZcdeqEzHJEFS11v-moxwk-V3C8sNLlt_66-1zOw8l1pippMqPaoUdN94CLP3blS37Rzuovk0n3f2pYcnsugHqfuGAIzIeJci_6MfLoUGidUMK3PA7hhhw6EK4S192ax2kePGbv3TEY2IVW7whJkhO3zf5gHYLrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6ApQ-4gxhlfn2Xm6pNkFRserp3kqlAwUkRrpjiLsnsxziBvOhikZY_aaL06YpfXD257OfIze40TmFQEtqiDan3UgaQXs8oSi75DpxyPl1I03wfv3V8RRyXRg6Aj0WM-pMO36JPPdoBVaAyFo1mc_GZOY7_ivC8dq3zFeVV3cs0gXOjSWxtDBkBSRPZTs13IOd9rhgNum653GjPe9ERoIvJ4Ot_feXNHhOKL9bmm1QkaCGxs1NnL1h_K4GGPBfEnHV4Rz6ceKU7GNdpytXxQlN80bPAu2iroiZe2WUtlG8JUFjHBoLcZCOUGF5gciTfVTfEMab8_qvbS5_sAMA6bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26735">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1XWnD_JUCsJR11IbYfvw0yNL_K7vb1-fE6uGaLHtrXPEmtzrBECwqxssgGA63TrV57J15pE46LTbO9x6Dy-4qxfFQ4CPqF68v8i8EBIk-z-EKy25J5ZofAcZlpn9kCx3Ji3TGsc2u5U5D6O8KPOx_fMhOae-sfhK5Ry-ii04RY-3U0y_6C7Ruj_4JxlM496oNiTM8MAm2euq1UKUbAcyda0Ljcn9f540SasFoI0_Qrm3NcQUfa1XVYOkKbrgfl-hJb549yiiuPvxsLKIsL00QhoqbiDWyjqlU7volWwqKxTkvIBs1owwlKbAyIOC0LIAGYfhfSLmaqawJDm6oS7HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
🔥
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26735" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jvsb9SFsyqoVEAv5sFhnqB2EiFEcDmkKJR-Vi47BY7LxyJwn0CMuHGgyGcK2Tds25M89LjWS78g84orFA7Xq9lKwjiNxKyBAGL2iwpjbMdZCrBp10JQY-rzcbD8Ie3d96Ds7joRpqQaLfYXqg3F6Hd_muGJxOel7tk1hoaQyWhHgzjDiumbyFUpdJjnQoYxC-r74t2xzzOZI5Jrv1lNvMFsat6Elqmg2HZ4JJtDH1omYVbjMt7L_PxEO2IcU4YVP5rIvMQsmG2rFVtEIRchKxWEtbJ7UpGJPI9NN_a9ldlsefdIV8ZvYogv9YjFTswrUrHlCo67bIqzY9AsJWM_Y1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=n4zK1_3GGQ8zT5nRJE3bWrptWEYWfkBWir-DY8Wr7G2i4jgr1uWEx72SNTVVNUAgb8SkqHX2GvynPTYvRKCoIHVohIGimmIPWAFDvJGgwblW-TaW9jHa96DBnrgj2I08usUpu_HN5IP2aP-INulRZWzn6aNJ86wCrpDnk_Myn3-TpSMxgEMacTm3plxVyEX-BtTIf45s0MyIhYrq7OSSj6UGbHNy3upIh0jCvFtUugbaQBfm1Ybjl25rHyhyg9HwunwnHs6Jzp9o5irJjxOT52qV9cOYQcvTyig5dOxU7kHeyoQkUjXYUfrJHicquW4MGYQygU4blmYEChT53xNuAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=n4zK1_3GGQ8zT5nRJE3bWrptWEYWfkBWir-DY8Wr7G2i4jgr1uWEx72SNTVVNUAgb8SkqHX2GvynPTYvRKCoIHVohIGimmIPWAFDvJGgwblW-TaW9jHa96DBnrgj2I08usUpu_HN5IP2aP-INulRZWzn6aNJ86wCrpDnk_Myn3-TpSMxgEMacTm3plxVyEX-BtTIf45s0MyIhYrq7OSSj6UGbHNy3upIh0jCvFtUugbaQBfm1Ybjl25rHyhyg9HwunwnHs6Jzp9o5irJjxOT52qV9cOYQcvTyig5dOxU7kHeyoQkUjXYUfrJHicquW4MGYQygU4blmYEChT53xNuAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=X2lpUhX9D1Xe3WMm5O4VSEjJpY3Zeed7tjYWol3dsTXXBRYy4J3zIEBAp0oq9scMSU_zs6Bw79oDFjcBivBYgrzOl3N5zSaBPwx4soDKtiMjerm6wcIOIbPEmge6jDVc9ehybLFs8sS8NaGtY9hQnL3k_siMr6T1S2QTyrQ0T7jevLRuxOi5jOGITdqLF3WUVzQLG4jR1n2OUZkSSMX2LF069ywg4rG9_kFTAJvWwemII2i4792U-xgGBC_wReQACVtd4Ufl6FvkSLLhmHXXfl6vSi38s7BJ-dt5pStAtu2pYih9_HhA1qTXIgrtCRIC7iq3MNxGg2ir4bLkyKsfBbCQ6RTWI-TzlBjtNL7D7qCjyqX7_JR_qkfvqfcgqIct_fM-eDfPZr9EytwkDIb_z-K0mKTVPz-z_sB74OAROXVOg53CaZzqH39CYFDRAA0Kj7n4pmqti-NKQA4NEA9iuCTHo79BeTjwZgOltdYfLnP_PuD_735Q-nFSXek8D6kLolXLaaC7lP1Fqv29TSNgSRUFtZe4YcCgfx6Osg6Q-4wFXsGwyky24IgD2p0Ywk9CcUMd5QKxR7sidloW-kmQy_fTeiJI_sbIEICHfJP_ICkdVWrtQjZ0qLQA4q2CKT-C6m7rpKORmSmBBpuPhEV_Fr-jBnyIPt1yVqiQSSUdvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=X2lpUhX9D1Xe3WMm5O4VSEjJpY3Zeed7tjYWol3dsTXXBRYy4J3zIEBAp0oq9scMSU_zs6Bw79oDFjcBivBYgrzOl3N5zSaBPwx4soDKtiMjerm6wcIOIbPEmge6jDVc9ehybLFs8sS8NaGtY9hQnL3k_siMr6T1S2QTyrQ0T7jevLRuxOi5jOGITdqLF3WUVzQLG4jR1n2OUZkSSMX2LF069ywg4rG9_kFTAJvWwemII2i4792U-xgGBC_wReQACVtd4Ufl6FvkSLLhmHXXfl6vSi38s7BJ-dt5pStAtu2pYih9_HhA1qTXIgrtCRIC7iq3MNxGg2ir4bLkyKsfBbCQ6RTWI-TzlBjtNL7D7qCjyqX7_JR_qkfvqfcgqIct_fM-eDfPZr9EytwkDIb_z-K0mKTVPz-z_sB74OAROXVOg53CaZzqH39CYFDRAA0Kj7n4pmqti-NKQA4NEA9iuCTHo79BeTjwZgOltdYfLnP_PuD_735Q-nFSXek8D6kLolXLaaC7lP1Fqv29TSNgSRUFtZe4YcCgfx6Osg6Q-4wFXsGwyky24IgD2p0Ywk9CcUMd5QKxR7sidloW-kmQy_fTeiJI_sbIEICHfJP_ICkdVWrtQjZ0qLQA4q2CKT-C6m7rpKORmSmBBpuPhEV_Fr-jBnyIPt1yVqiQSSUdvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0u70MR0Pdb5k019MH48e6DhR76wYSN16pygZaadlix3L9NmA52kdkuHyeevwx2VW68NqK7yHqmIo6g_wWUr27Qi7TpaMAR4zO7U5XUq5OBqDqQsBrbIMDw0SCecKYmEK2nUYZf1_rjgkjA_PpVDoH7oM-4MV-QsHzeUaP_nN_mVaDVSzU7yVgaRRSVKFF4ZmEVC9BWyQ_uwKKu-2kI_-qrXDN8l2M3NDGaheJdsaV3xWH_GtE-nfT-Slwp7ah7xGs0nUpKnQWI1JmFcZJotmcaD7r6nol_vqSLTHHV6fqeluj3Zn1GM_yUFHqWJdi7hjr1NgwMAd0T9LiyGo5HdQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2jC94F4AkJSShlr7IMkc9Y6vAGTLHboY5FeeG9E2xvlqnf2vCexHN_fvI0Oa6HtIV6UdtY4bbKUKqGXqvFU78U6HnyGRRpJtyBvsXD32bL46eWTFadxWxZiZLBcxh3UlIJYZawG0ugYgIUaCKPSQEVAAvnL6EEGEVaxESuKYssvBr5xHzKBt49iayK-EB7aY_HfrAu513PKJGmMSUeIsJ9mKjo2Kikimb9gE0yBsQWYkqDHMcvnaANzMkorxsL1ruwIM2yZj_ir37QL3q6UGb8tAEoYBz-G8gCYK8CsBAlM9cpytvbF2K36__mYyr72WVOJQriSrXWsSbQZxoeSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqChZYv1xmm6wgD61GW6p22Ghc1fcC4MGHeHUxutqbLcYOGM88SkiHd-AH8GOF-9i_4ujUoUvCl6JafGl_OH2hL8W233EjD3ew8EIT2gvDwhKHutwo0eZcUKsnwzHOE-oxXN3dkaDomlAkIU22Htcw7QYr6QKGc7s8yVtE83csgQMizq6Kv4Ax4km_x39mkKBIVaFHbwF_hboZK2LDhrKodv43eotuJiNDUWtQsznLjhGkuLs1rU91sTXmIAk85ySiOc1GC3vDt9EbFOdEWrhFfDgc2HpWJi3MeI3j0Pqs52E5kkjQblXmr_npoVHPYYCHtoukS7qlzaDCZrV5ziBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_BV-2fr1qgKXm4ZjadW7KL1DBDveDgEkG6lx_4i9ManFVo5mFHa9vHHQRorxzZ-ScTkUw07xqi3t9KiLbQGoSM_jCx7C0l_TT8hbA8CAmL9O7Vm0TrsuJSjRTEjyTA9cqz9b6FGdl8be-KjMYaQxmp7OL91fct0COJ7YQm0kE5IOIL0Q1Cn_0EkjY0vvMhRiSiK1DGJEvMwU5NGF0x5A300YQrC71YMOX2vz35q7Zg4fghzoYxxSdSoDyUsmGVLQhBX9fLeDkj5qWvJZFZMhSaHkH5k6hHsw9BxZBq7Jbiih9HXRcf8mKi5ySozGaBT6mJCCet7FRl8MA50-MFNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hgqJ6W0YYwHItuk91_tHwBDNxyFLBKAOxTC3_1KOSMJUWNuYqZ8wj7I-Yi0eA1-CjmncK_tV1IrqVPjtTFh5vWv-prFwuZ25rLhXAnOzyVurbVDt7pAqBKx3kWI_XDo8ztF_7s3OPXsLKcGUJ6DEok8Cfz4eZD6HvQNMDgurlKZfIh62PvVwuN9-9eXDgp3hDbXDbxIZfj84utyAcGDJepHo43hzaLwezdFO07czv045UktMq5sGkIvKsrWkhcCW8nUfurTqMJRDxY8GDXKbcoXBJJqPsG3g3JaQl2oTYiGrfuBDiY1KYgofuaNPeItQsrswqvtJw0CGkdxS3sGx6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgs8wMbvXg0s5-nFecURiw13HueJATt1HDrKQ7YTJfGJ-AobxMO7j5IDQ71tJxGHosETo7Gppvhy8eSPL_keln6qwB7IHPvLI-g3AXFNVTPiZUvKgpxtsc-UV4tQw2d49Y71C6ke2b5Dre8premGWYtV5NwRVyc7Z0EkWZOrrjdlmzEYJv9DPLGcjwvGGqevOJNHBFOaBO2D39dYIF2jGec5uP3QNAwo6XvxTkf2xSVRePKPCrmWdJhtt-V2O8dSDKs-Mpl1V2iUV2JNCri0kFgdEQHzTgiUCiriOctsrgzREiCBGWgfvPplmKM35et3poEAo8mMp5K_eaHAiB9ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLqKoE0rQZgLZZB6E4wiOsIuOtTm2vKWjOd0RN0nHtXm9JgD_PUyB8voc6sZ4owX8rUcYaeNr-woAvVpDkXv59uaWpaRxc19tvmPyme4VXJzhiIYFk_99SQ0t4z5muJvFAvamS898yGnnhDzt_Y7yFooZ8uVvzqSTcs3zZ_ELdHo4U-iMiJ1k_x2uBkvReq8Ink3rl_Vxk6tHqclQP7fQlUxV79oeFsKX7frYej5xjdp0qg0AjboGp8XUPwDiA06csm9nNFPZp8Wxpb34_Q6JdldsW5U-Skz0nVIaZt7Bz_tWK3_HRz-wmBw7cXL9j5Ws9O6p1jAs0TqJICKxGKdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=eHqyhEL_atft_lVCqnnNxrh5q6ZtCsuq1EQzzSopf9V-Mp3vF2hxvKBTH_fY_j5DYhPDQ_9BKAZHAV2UTER85gAH04kW5hIjxPCU8vwTzxt9e9vXac-am4zTx53ahmdEMD6YvA9j650eHtCJnEOyrB73YZntk-JqrR30ugmv3eDHN-QUSZ_qW9GSVLgbCMPHBLLotLGkWxpptLpZ73GWQs1_fSEPL1HrH1TnXoTOL3eH-AA8shWQSi5hoRd7TkVdoFS6URgOhEvMa3Dx6VJU6s4eBNDWLbRx-Jl6Ns6fb4goXaUX6DTkzxsWqFUC9AdtdJOEDoj6CZ26Y1YvtfzUFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=eHqyhEL_atft_lVCqnnNxrh5q6ZtCsuq1EQzzSopf9V-Mp3vF2hxvKBTH_fY_j5DYhPDQ_9BKAZHAV2UTER85gAH04kW5hIjxPCU8vwTzxt9e9vXac-am4zTx53ahmdEMD6YvA9j650eHtCJnEOyrB73YZntk-JqrR30ugmv3eDHN-QUSZ_qW9GSVLgbCMPHBLLotLGkWxpptLpZ73GWQs1_fSEPL1HrH1TnXoTOL3eH-AA8shWQSi5hoRd7TkVdoFS6URgOhEvMa3Dx6VJU6s4eBNDWLbRx-Jl6Ns6fb4goXaUX6DTkzxsWqFUC9AdtdJOEDoj6CZ26Y1YvtfzUFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9FWvwtUVAtMxYEqONN97EzDYjIZCxASjwDTTK9BMiuaCntuhJM2rOpRL0TjdWrmjxZRFLt9iNtY9DAdYaXvG33bhLdxN0anwOZD10VHY9vKaBVFV6qaTxGqVcq0xVVUSMZUbH2DfrrM5cG8ZOrRVLQ_Jmod1qtcyZg3NQU86HK_0zJ4Pfuz200jK0Vay1HqRtJbITd9GVplb5zbweOcCTsJ2StbtZ-TyunveVAAg7K0hkvYkw6SzhuXJiOVOafBpLrKmP9HRNr_jFTD9legHOWIfBvUFnY9HKnPRk12x2d2DGjJbjh_Ft9S70TOfhWQFyURYyYylKcLX1ZQuc3-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNa-hyZk9lF4SNX8fhpWnuKGf95ebUfBfKq9XkH21ldlyex--GSlGGghRm3exrwAxGl1WA7luqP3aBtibrOLyeZx6aWnVatglhZ2gVqiXMchV9VJQXVGbsenoyh_AlR83ukxKWqWzGimIS-9yZw0XZikH3M-cLzdtEZz8CXXb7kfhtgI5o_xCGl0A_aZoLKkuRxhm1n06dEoeeWZiKAXt4mGp7lyJEvbE4uFYzGRpphtwLmr6OOEkZpl1QVGocs_CJqSWRYUufLSX7DsbVwQ-IJs_VJpE9Sn1o1Bl2azH_TBrziOlVQrVkH-zS0eRo3ykkOuHHCXTAex5lz697xqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfmkkiuxvcA1q3L4lwYRvD9A8qkOxHqA0oN1SWEIlr22OwOGD7xYYRY7bKPfZXRXXRF2N8Il48ynF-9kE5aQiDL6t7x_jUsLFdIJzY_ist3sTwZftR3gecxyqMGGkQP6QUAmS09O1gnRoP8M22yGEt4cPa4_r8A1yuwQ9lwtOuRxlWI6QzTdH3_V1DLsFZRQvDAcK3ZzXaX6zR-3VrMvDxsCiTsYb1DWmGZhGYPx4uyLZ0b7vSUdJetdxe6Kp_WAvquHWYy0i59H0sAm1P7-fPrN_2lECkZGmuR0A8MA_3hG3q0CvKaqgZQXnRRBPmN6S8Ut1t_GVlhGO-QWLe_IWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAEew684AbV91szv2AQxji0yOtvNcjMSb9TQB1tcHZK9ZCVtJPHe2c-J7FPJR0Q--bL7QvOxNzvxpOaMEP6RQwfpuKHeBQFZ_aJjnf4bl8QCjQU9K3oOz3ZZiyn-DY-_Tz8zO8ZGsRwXCnfz_invWP7h547iuLJR95g0d8JPSUltPDSJSFEKGRkL12GmGCzD5huOdLjnoF_V1G0KtFcZby5S11MMidyrs8-594qzAcUH9Ka08xrVDKmSw7qwa5uxnvyO1u8UOGTmzQpwIEOWI4-M8LN2rtuL26jvutQ4nTzqSzWKtI416Mmso6SUgBI28LU3gu7rutCh0cYyXCRz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=jrvatjKHZF4gnOtTD-vxCi1pSZzNU29JNzJHFomnsvbi7lclY0pmvGJchNdEcProMhSREmhMoXRbzickTMooj_Jj8ll2VNCry8u4qykTzM7J8s8I-5tCtrSiQUiy2KOiis2Jzn8YByEGkqnmVV3b3bfIPszt00PYN80QAmP64z1hQYmIEeaWXtDjmXqSGIn7gPUI05WIw-UIH4r2heeKcsTdvtvJDAdPBZs2Z6lOZRYE0UGs4EHzhEbT5uJZiShXrRMcOKmMf3pH073rR308NRkDpFC9AkBVp1ZSDYhZlj2v932mE7P3wWvOvxr_TBxJQOAQSFg8djqn4tvzrbw7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=jrvatjKHZF4gnOtTD-vxCi1pSZzNU29JNzJHFomnsvbi7lclY0pmvGJchNdEcProMhSREmhMoXRbzickTMooj_Jj8ll2VNCry8u4qykTzM7J8s8I-5tCtrSiQUiy2KOiis2Jzn8YByEGkqnmVV3b3bfIPszt00PYN80QAmP64z1hQYmIEeaWXtDjmXqSGIn7gPUI05WIw-UIH4r2heeKcsTdvtvJDAdPBZs2Z6lOZRYE0UGs4EHzhEbT5uJZiShXrRMcOKmMf3pH073rR308NRkDpFC9AkBVp1ZSDYhZlj2v932mE7P3wWvOvxr_TBxJQOAQSFg8djqn4tvzrbw7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV0D89T8-C6QnXu4QCbM6Wdo7XKoLOb5wBgW9oaihmtTO0URttaeMS05Rce6QwJ8BKcbeK_fQQdPqoAGqTrDE_Y9-XfJ-seuOjosSn6CxGlSC9Fm6i6P9qYvZm7Uf6-5_3rRURVKD7iA-36jBjjQr7hzQT1L1zkjhKage__202oUj1DRkB658RwaFu-xQ3VwesaQpwQWJq56zLlWMhMOIMENs-PVRfXWh1dAOk-hD-PSw4CxdQR0b1P-_1Cx2atPceo5PjH0ALcSfHgwSpmMz6iWlED3K-50MHLLe9XNo6_9KlFxWR2IC3mnEPb2DQxcTrirLTwHyhG_H_oNWq00wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcW_y96dV7OB8m92PxPVBa4xBoCh3Uqq3FsKlrQPRUAwn-x7VPGW9Xz4gP8wDL7f3jVFUrEv7a9b5XLjeM9iI3hDs0dM-vDSoEbHXSNNAT8aKFvh-iqr4l1QcgsNCPjq9CO9Zvk-dCPH5E3a38kF6QpN0wEsJquwNSas1xWli0XgUJJxwtr9t15HsrAE3qZcX7RHP2tcE_o4qq15BhOAh4E8AjvNkrTJbgepQxlXjDDoQ-eDpc2pqFjNvFqn1o7lj_XAPZJLp9ETXgqan-CYd9VUz8VShxg9Z7QR00yVqqRkKiNte5f3FiYq6IO4NoEPSOpx-Z5w7kP7JwFn5KXq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEDXVpXxyz6Wny9BvcXQdCziEqqzBLmCQ73qXIXZVEV16FQghrlSOdvICxQbqWolR_UgRv7FsMCdt6MFdjipWFAVI08ThRyjwi_1YuLAm5bYl7VRF39BmhhRuB8MnnzgccB34P6sCsNkkN00GzZstGJtp8lV4F97QY_CTX1lLHw4oL1F0mbWV-LxGAo8m4nlHwjiMLINnjB-fUvXXAhyXZWjpWv6jI088uwrwUfkuFZrPh_7p34GkDuD5vTOon58EPxlPyKVIUXUyzf_97lKkchVWIHlwNCq5_gG1a_gXUWCRUKSb3pEum6XYW9du0zh04RgX8U8aj2gwXU-F4iZuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=Kg441KAtKhqfjW5t0dnZcqYRMWGZjkYp-66c5r8YbWgP10LEqN9UM_FGsOWLxWvBwtQf7G6VfJQX8TA6lf54ypMQ1vrQ7VKy1b4V_8rJm5O_WDA0HQyulBzbaSNCBatw8aAHo3jafLoFIIqvzbwShLvMdsfHKV0BQQqr7MH0Rm90KTA-qyBsz7hh5dpsQko9fbiYby37VJKlVIxUKFaPwekJkkAImSuRH2RGY-mIp76GoHBvQCIWmW547sBjv6ImoYTJkuLdJHdaBgyabhp3HTPPIAN03VCPKWvXC8SI7iLr6BQBp2pZN5nHw8BPo7Yz0Vk4V1zvUYzKc0dCEmGXBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=Kg441KAtKhqfjW5t0dnZcqYRMWGZjkYp-66c5r8YbWgP10LEqN9UM_FGsOWLxWvBwtQf7G6VfJQX8TA6lf54ypMQ1vrQ7VKy1b4V_8rJm5O_WDA0HQyulBzbaSNCBatw8aAHo3jafLoFIIqvzbwShLvMdsfHKV0BQQqr7MH0Rm90KTA-qyBsz7hh5dpsQko9fbiYby37VJKlVIxUKFaPwekJkkAImSuRH2RGY-mIp76GoHBvQCIWmW547sBjv6ImoYTJkuLdJHdaBgyabhp3HTPPIAN03VCPKWvXC8SI7iLr6BQBp2pZN5nHw8BPo7Yz0Vk4V1zvUYzKc0dCEmGXBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=KojbbTSkWFwemTbDeDKFZYLNHOj3FMaReasaI1THYv6z-DABEK3Q5wkQk13I-sETSWUja9g6NwtfT33M2s_HDcw_ULaY6fCVOPKzAKud6D6lWhAV4olaUXMcsKz9kvAp67fVFk45t0qCC9X2FsXS2KuuVp3_dW4PoI1kZU8OJto_B1H2lIcitkX5MucCCxwkqVFmDiSMBoCQZS-6VHKnP53k48kyM1g2Xt4zHJ_xTkoJIizgAEcznpnoHC_wJX8aTnzTacIVyo0yXbFvhPhNN7osSE1dvWar3pVPOPm35uEbeSSMpIqZi0C0s33pGGsmg6IUz94VtB-_gchc7YUJ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=KojbbTSkWFwemTbDeDKFZYLNHOj3FMaReasaI1THYv6z-DABEK3Q5wkQk13I-sETSWUja9g6NwtfT33M2s_HDcw_ULaY6fCVOPKzAKud6D6lWhAV4olaUXMcsKz9kvAp67fVFk45t0qCC9X2FsXS2KuuVp3_dW4PoI1kZU8OJto_B1H2lIcitkX5MucCCxwkqVFmDiSMBoCQZS-6VHKnP53k48kyM1g2Xt4zHJ_xTkoJIizgAEcznpnoHC_wJX8aTnzTacIVyo0yXbFvhPhNN7osSE1dvWar3pVPOPm35uEbeSSMpIqZi0C0s33pGGsmg6IUz94VtB-_gchc7YUJ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWR_dKgF5wT5ylLJOZRCh7ff0rRobkPDCrP0p2pkf1-ZMy8z23_TQmViUi2xiuEc2F8JEiLaMpGS6E74pXzPzgpcf5XrRPCqO0475zx8IzmRSp1XIq58vwkxc5Ss3qob5RS6Zi1m2rBz2TMrhIEj85lP04uEj_wzfKAEMlON57yCExpvT6Ka_hwKpr7pfAumGi-68qI3fI6TAkhpigtxIBOnZ463wK6hPy_NsZAPIEvo5DyBqEcj187JCYZYdyzjT0bVMKPk8Scf5v2OqkjB8S43dNwAJBHXsZqcXPtN-cvQiwGPpVoHJKWSyiaAyVeski4AMItpvWCxNUEkwjnzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D55ce5HBrtB6VdH0QefuyEd6rZlO2C4AxKJxcBBW4SfVMTKbCUQY4JSAjJ_YlOc_Exhkor872fdAGb_vSv-RSwGZfdzrJcGnX3_F3PzcURYSSAmnWRbp6ywz3tJf3UaObLXnksvWTQ02dhmcflvD6K5icMXkhhBcPNDqn-ZZ5Q4yMDB55SKwzZHiiu2XuNVo53Yo_Ow8h9LTV5iCJDC6IOp8tfkxtkAOFQMHDG_aLVXuZyn3_aZvMGwpJG9bi6mDOxqDeNbfcqFH4YHDMsixgnrSinYnEt4mAWYL96X4CPvcfODcnGVqvjewhcbYet0yT94iYnQVkWbN_GMUpmRMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=uSeAV7nNXAfK5A_NwlRV3G5V8qsrqgkP1AMao0fdge2vnz6sl8UPRT-CYxXXI0zr_UCECxp-Go-IvVjvQ3OfoElwch-P2HOF1oH76FMB_YjqIv_286qQ0BlFBVOtGl-q5tcVWQW6x1LYqgc6MaEDpykxZvi5qjjlynZ7Z0X-ehYfPMxMU2lzN4zHei_Qm24gyramXTEyOjz8fUlSwNS6bK1Ydm56Xy1BVDl5hXjIuGfbZr1-q6YcbWwRxzVHxSMSCRwP1Is6ulxYJP_wYHfNrc8dEMuQWBoL4p_v0niRAIAnNDnxCQz8DRqtc5FGLkPpIaodYWn6CehcistcF8Bepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=uSeAV7nNXAfK5A_NwlRV3G5V8qsrqgkP1AMao0fdge2vnz6sl8UPRT-CYxXXI0zr_UCECxp-Go-IvVjvQ3OfoElwch-P2HOF1oH76FMB_YjqIv_286qQ0BlFBVOtGl-q5tcVWQW6x1LYqgc6MaEDpykxZvi5qjjlynZ7Z0X-ehYfPMxMU2lzN4zHei_Qm24gyramXTEyOjz8fUlSwNS6bK1Ydm56Xy1BVDl5hXjIuGfbZr1-q6YcbWwRxzVHxSMSCRwP1Is6ulxYJP_wYHfNrc8dEMuQWBoL4p_v0niRAIAnNDnxCQz8DRqtc5FGLkPpIaodYWn6CehcistcF8Bepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcvnUuF65lhN5H1ahoYzEo2Gug-aG3OFGMxmDM-8x6b42mxCHHs9mKKRN-xjiABZflmfrW8AwWLEl9C5KnyJNS2XVMdkSNa2CZ25phZtSgmCUHUXO0gVM-gsRmYYxTS8Yj1SvzOTn4x4tAQr56jnp_3St0ELB3M5RU4W_IYZzbWWQqOgkyr-5PpxAya374OYb93D3zqnQEdulcJn-LwFE_0asunLKfvwegDm1OlratoyiW7Zov5quSgZqZg49bwHJtTSW3ZHdJIgxObolGyrFS9yNSDq3B83pEXxh6y5m8PHL1eq_Hh0wtcdoeVlScPdvMgOGjdeIqEGKKHOHluJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ9OIYhyAAmBWqvYEhf1tke1tVFiR0QysiEPR6S_qhnHt1zNeqe0jxcNXpB8XSwrG9gdrRlAX3OuX2NJvaFEJB3474VIyigJxvXxYT30yL6bd8y4mWSiVItePV6i5nMKOPT5kEI5pfx3NsiV2gsgD8c2flcXkaBVJZVlDbW53UVgO3TEzSur5vKa8hTLBi8HA-8ZywbhK293cTI5hjCxDgcDqk78dRrxIhNdFY6NCcpO9xtQze0pTyIpDRgftGNLM5lYchuI55EJ9ZqT1svcbFkZH1TMlijHypjXKiImgb9j6OkWgVwWyxvnTWQ2ynI1Jds7A3F3jr5Ys6f0a8IJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLruRe_y8n3PoPOHs5ewtLx0eIuYeOfA6cDSQz7Sxi5Ia7AA_9bgUWGtS5VOiF9afoFEzrKPJQrdJhQ8UwrIicSiOk7FvSIHTGGq3Vw6-ShVhI74ZnjnIF7sOlZHN6w89kS6NhbbuYv_37eY9AX0OZ58ShMKe8wOpOwikss2P3O6Gp8raZfL-6y7SIJrXzAMfXSKFynl2ASFbXzjfiQinodH7zXqKpwEbDeSdke1qoGp5ns2c3Jq76B9ah8F4e18advhG5veG_sdpCqCW7BxPTxUVUpHT66tWlgVoo15ULwqXo62cRzVJSH73QX4Y1jaVowYYvs_XOluPiIdVJ64Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn36Mo4R89n9cr0obRLmns5_vClF3FTfWbNOL7QziU-qvfwzthYg0mZPOVA2fuqUTXONNqF0Iy13dAHrsQUNwXpE8HclNYFgAhhemA0flmK-gqsS1336Va7UMuEa3bYc-d1zfHJlzqrk6YaKfTOeKyGtUHMJAIEFxvdN-Q-ftN7US1fV4YAENlmwNBAwdiyrPQ1rKipAaZw8CJboNmibLwV5lvM7LijZFK6t23pg-5Y5Qw83axgpvXFPePPrnozKSbUgSLteOPzLJgEiWBX9n0YyNPdxOHwvW7K2Gyto0oNZvL6fVBfLfaRvi8mWATqL1-WsO3V27sydH8OcSgvfErdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=YNe5ALQkLsvrx3SOlGyyt-I2i2JgSRE84DTtkrKyzlBLPAo1xFuY7z_itrof5d_ZWaMw1F_VNcq1eX_Q3Vx9J8YheKOp63UEn9Uz_rVlkBzh7dsuWbbWYvYEaIhVNJ2mabaJPEFjTpgVGvjDo99mjzVw2DHtQxstgXZr9zVDGpnLN04uURfp6eEcXAFnbW-eD-XCMAVNTXWwWZ5rUlZI8NrfkBCRl2Pwhu2hJFxHpFrgKnE6OnrjqYHxDtZW3ygnRvrAeJ_wDD4GxvwQrtkYWfGGEirO_5PlJOVh29n4_OhDfTsDoScgxwmzXZSmMyG0xFJKMqEw-VJcx33mjhbDn36Mo4R89n9cr0obRLmns5_vClF3FTfWbNOL7QziU-qvfwzthYg0mZPOVA2fuqUTXONNqF0Iy13dAHrsQUNwXpE8HclNYFgAhhemA0flmK-gqsS1336Va7UMuEa3bYc-d1zfHJlzqrk6YaKfTOeKyGtUHMJAIEFxvdN-Q-ftN7US1fV4YAENlmwNBAwdiyrPQ1rKipAaZw8CJboNmibLwV5lvM7LijZFK6t23pg-5Y5Qw83axgpvXFPePPrnozKSbUgSLteOPzLJgEiWBX9n0YyNPdxOHwvW7K2Gyto0oNZvL6fVBfLfaRvi8mWATqL1-WsO3V27sydH8OcSgvfErdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc8i8D4eGHEl6ggthRyoGO9KHOHWbtGvYTPw74O8Ua3ALIhxTg-o8CPUfXQQSzVTuPkM82IV3YCIecC7y7TN8jVoGuivhT7iworhP4IwaeIwD_Mnxde4fgyfAoDrBOJBnxvkHQfjUZ7yCRNaHDdyleSY35Bik9BVytIISqb9sL_lZQ3Q1SOEb0TSbZaY0PXQI0uKdWCuU401AgI5IGlPpElNWsYlHpYD2S9vi-wtyTNFTo0ONHmpF8BnCrhG1BCo7D-NU9waxpmpJ6NuwwFod_MCH7Fmn3NWMv0n-NBJ9GSCVGA1_plxazrgoYqg4g5PRXa5-iRIagVQncs_cWHPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fd_qbDMT_QypdVb4BhsfIX8FjaDNtZN2oFeA2Gof_2dvG_NXOYh1W5Rynkba_QnU3HdMiDt0uiGqthL37LI9ptzpUXhuMF8YW1EoB_Wu6tdKBiHnp20kG-Nym0sPpltXHlI3Lb1WvT4SUn7nswKVowEriX4I5LnPKnL4MWHFGnFwnfOjRjaK3hvI1yDhhHJOvu-HFwXTub0t5rQjYR8Ln_berdAIzJkmDhz9ecXMezTMmApVKiQSBf5r1H7ntlMJBM8jFqt1jmlGJ8Are4TV2pylTVLqCtHkAb7HQh76KTbSlvXXPxrNDrPyoBP3XSUexUbky3ArblE7_CSXZ2h2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/akIh7G1BSLf1ws-VSytd6uPpYhx9_HbzQ-vd9wTDOGLbI3cZrvimCvBuKeLTppoa-9iwWiTwUYNIO-NI7E-8vHtWhI2d193aNRPNRUZBNVSaeyVipLkAsM-332KkN4de2yZ0fUGmmNCfWSvNyfgeScV8JqqevP5gaExTc1eiCdfq4TULpJfYeSeEfqDkNwqa0HGjEH7i_iw95UsuJIeM7Tsg9t8wYgXSRA_0S0V4ZTMSqzSyQyhNlCyIsBAoxoBPjbd17y1gekfhus6qQOT7pIPYvWhBRGymyeGva3wWBdPQwKQFLQSvDMDgzNp7vx0NEUeSKs-sL7-csbq0wjqf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhM9z2j-2KGRJqn_XYwBMDALYKjDY_S-9IXmgLzAQ5UDxdJTtJCOj4pG831OpgYoeAV_2a0Z4qhmCMpEMk0LXVwbHyRNRHVyuTQvPPAod6yBPclTfvTwM8ZjhgaUA_9wCwha9z1T5MwJnQ2xxKqyFFaF1ZSjBiZXzmq6Q32n_IsPPJUr6iH9OeaDIiA-rQDm6ZWaCZg9ED1OQ0Bh26q7UldyQ4hNc9GWoiKyHzZesAo7s_MpWurUNLpN6wjWhupxLV8rqMb_MZAMAGmx4ZKKwFEbr26GpEJ3mQWTrNBkLjAB0naAnlVeyhsjIwl6Nsk9W2zbc4c3g7pUzBuN-4Ihpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaTlN_CnVbo0fZ_8zP5LSkJsaCktEZfD7wm9eq06iYbC4BWU3QP28fv4hXk8cbPig1czo6Ad4Bi3NSsz_LxAGDh7LQWN8Iu58mMlh61FWUQPL33fXBLBjXvPYDmXlFtlUc0HGePbovk2UfF1pyQM0XoEfY4VNYjNXi6R86WaD4avqycHK32VUW_gpjKmOAoOaoBs36L-egzKBeEsVAlDUo1P9gR0rOs6W2ulXrIpHKyYkNG9U3W7bh2O1Mbn4vJ2ia6mAcMjiKCh75lNJBYz5FD7Tw7mu0YKtYpxv1IoGeHyr6Gq0dTWjhC3EAg6Ed1p-q4Dv0jTaEDkt0Z9QaqE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoEnx8SBGN-de_4tIv0INA7nkPmdIE2mGcO_VgrMhnn06EHQnibYmJK83b8sucfwyCd92KLMgswEnO8QR9fMxPIuzX2gJpVSNOysjKCXVJ-7Kc_nyn55FvHtN0YobgZUVjQrFI_w1iGdmvHrj5aH_kJi01hK0CmOueA2PZ_tbDkBhG2wdfwbDmnypuVV_MWV1yepVcYlUP2qCV98cyyvI-XpGz7w4YOawxUYz0YBRerp2Bmg-nBID5bVZx-Mo58Ob2ruHXQ1bNe6KR03-41xZ7ckHS70JqVAs4uIHpdIc7iXd6BhgUajXiq3uE7lcGxES-4V4dg7INih1041DRjBlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExPJzUfJ2-oyUxcQ4E0bIKsF9S82A2KeYa7-UjGe62N48peCCxqW1XO5x5dJ8dLdRkJU6ll8ax8dRS-A8cYvSlGd7F7XgsodcW2tlLcxEo4v3mrijf2c2XeZFIY3aw5j52TKDUzGlH805dh0MEKWE2JTNW8SOFF3siEZpADtTG8ashRsiuwwgqF77qWLyeNnrd1qXrvBEeOCAGYP66K_9KZRaDNTBV9TeX6sQBVQq9f7Pjkdn0Hs_AJr5p53Zqt6xTBq3O4lRYWEH7EXLtbgLITftsuJb211Mh9Bz-dqRWmNhQdh4zekdump8XlAXMeiWg3HAw4o5SFwBf1eR7flng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=tZRn1fnmlviFFB_ajCECTPIhCGa8UIg5VgiTmlivmlFowEmbBtZhqtD4QX_EIVucmv2YeClGip5sByrci1lW9AIi1BtL8qktp8yY0Z_gLGHlmksuHwkMRV4ImvjZYGmqcpYOVl5gm444HtlCiFFurHjuTw6azoFssmMyTediu12adi8dcRXZkZKatWa-uTp53OMl9C2zmFnAORHHZuyacX8lp-LPLoPn-1T2J3RCoyUlmMmUcWrj9Kft2TwiNaGR8-hfE_vgcs2vWogYfjGwopMjDpLuqh4FiAVwf8UPd5kJKyHvf51CnlC0rgww7_a0tmApAJljaFJOGpJx0PyaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=tZRn1fnmlviFFB_ajCECTPIhCGa8UIg5VgiTmlivmlFowEmbBtZhqtD4QX_EIVucmv2YeClGip5sByrci1lW9AIi1BtL8qktp8yY0Z_gLGHlmksuHwkMRV4ImvjZYGmqcpYOVl5gm444HtlCiFFurHjuTw6azoFssmMyTediu12adi8dcRXZkZKatWa-uTp53OMl9C2zmFnAORHHZuyacX8lp-LPLoPn-1T2J3RCoyUlmMmUcWrj9Kft2TwiNaGR8-hfE_vgcs2vWogYfjGwopMjDpLuqh4FiAVwf8UPd5kJKyHvf51CnlC0rgww7_a0tmApAJljaFJOGpJx0PyaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1Qqth7rjkvZBaPav4yGUPXFctc6XBDxYS7QSnHl9cOfXMGzFmBbR7ALdtu1m8cqN9T5Ec9uk1ts0uxbAN07-a4JuoabaQIPgRVnnzsxu1LZAh7BN4eyhiMi2Wk2xsR30ec-dggSw2uBSZJaTyeCZDiU9QBxAdzR9NB8CwjBWGrjZqyyvaXcMsNi1GR6L7Nz8z7UReyKwxTYgXrW9e7nMajqxjJY_EPwNnq2GIkMOZjGqjwkIhenNjCzXSwERlHSA7hotEzJVj-el6gyTXHZbHIctXYGPxCZWPpGiBrIjPg29OhGl4dNzstIH7-6sUZsCBALtgV1HT_xmZUAerbq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26693" target="_blank">📅 16:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26691">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQwaSH_6tVULaHJSO6oLC4PhocQxUkBM2NImiZxL-t6BDd1KBjdWWe8n6C26glB9Th0EyHK2KMTuBpqWRUykYrCMebgxYeSZddyo9ZT1_Nfzfn9wMpxVspuG8uEQ1wowM5-iGduvmtgNlxT-DDCwgf-obzeLc6F5ufLOG7ntGk60yKZQaYJVO7HH3V3QLiJCaIr3GjsmCyFBXIG3RjgN8ZEh8Cgp39c-82eWVfRZk9hPO8poe57wvYM9GVLKhCRJU_zKiDlGIfqxVsXy5CL7B1WBQC7M9yv3JMn5FEIR3yczgq9i-p2-J0rP99mMhJ9K0ATrKBMrFrvJiXw076JJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ محمد مهدی‌ محبی دقایقی قبل بالاخره قرار داد خود را به مدت سه فصل با‌ پرسپولیس امضا کرد. ممکن است باشگاه امشب یا فردا پوستر محبی رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26691" target="_blank">📅 16:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26690">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObqlhCJTJ0vnbatKhNjZ9an64IGr3OAiD5XCb5uE67x4apPdL5mNj8qBnRx7PkddRnJvw_Z-RsGnNjiKvNO7jcTvrxqqkyTSdhXOmDlRWAzApHQ36QAhcpDEHfCFD9Z47fcPh8P9czOxW4LHDJX3GoMq0UITry-cpWJpzy7CzB6wc3zyl1251WbiZG38l9K_1xY_mLdVtpIs7zootm5XLZhVQ6KXjrhxCgRRcDtjpFkwpMF85F3foiPsHuv6wUQO9sivNIrcH6CD1IjJT7sOhFIZAfEVdnaI3eyiGuUnZD55yP2P2b1ZxyLywuSa2J6x4ZqwtXLZqVPiHi39jT5wdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌عمو کسری‌طاهری ستاره تیم نساجی: مهدی تارتار به بانک‌شهر اعلام‌کرده با وجود علیپور، سرگیف و شهر آبادی نیازی به جذب طاهری ندارم. تارتار سر انتقال 150 میلیارد تومانی شهر آبادی به باشگاه پرسپولیس 35 میلیارد تومان به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26690" target="_blank">📅 16:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26689">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=eYVkh-P5BJs8v3TJnKKFEAoa5BpZL5302WdgBYXb7YAqQXoGJLIAflVrXqpMJZJDbj81n1NhvfhF5VRT106oeHHoNNp6kTjaDIqHrl7FhJ0mOV10yO7OBMvQIo-mrXd5I-gA6YiJeU0iZB4DqVorKBW8-ksDIPTxYU2hzWYmNE9AkSGzyR806wJa_1d24Hmkpfl8uWM5O3keFGpubd1rHQ0C6R5PWWe1umXbNXB4bbU23DtgNNbqZFiyBpnKH8M00LYyibq2v9YUEAoZm7Tg6eeOVolbKXP1qbiTDjcAizyUL3RRJBeMsHMDvy1UL8q8ssVoWrOanSTiY_zAH2ihkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ccc06fbcc.mp4?token=eYVkh-P5BJs8v3TJnKKFEAoa5BpZL5302WdgBYXb7YAqQXoGJLIAflVrXqpMJZJDbj81n1NhvfhF5VRT106oeHHoNNp6kTjaDIqHrl7FhJ0mOV10yO7OBMvQIo-mrXd5I-gA6YiJeU0iZB4DqVorKBW8-ksDIPTxYU2hzWYmNE9AkSGzyR806wJa_1d24Hmkpfl8uWM5O3keFGpubd1rHQ0C6R5PWWe1umXbNXB4bbU23DtgNNbqZFiyBpnKH8M00LYyibq2v9YUEAoZm7Tg6eeOVolbKXP1qbiTDjcAizyUL3RRJBeMsHMDvy1UL8q8ssVoWrOanSTiY_zAH2ihkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هر اثری هنری دیدنی یک کپی بی ارزش داره؛ در نقاط سخت زندگی فردی به دادت خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26689" target="_blank">📅 16:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26688">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3gVa3YFdEnNPQWKMR-wdlQ3vvoYHKljhFkXwOqUS_8VM4I3QlRODaeSd-0KsL5pbMZWL4p2k4b8-OAOCK2DqQs9OQcXO00m-jStCAfD75S3LahfaJ3sh9EeGNgqDzUhgHHVy0wc8vcm-c3TT6leYRinhsku2cPfKw2_I4qG_T37F1t5zZIHO3ALsK99apO5mSV2V0GgXVT3qdMjhrnJEi0G4x36q4wIqSAnhTBRRL_2Z9D8mXvCB6FfL5aHWkpvlEX6THEfJU0D608ykspYJiGtL3t9ZRUbQPwoDTjvvn07oKVGnC93Bp-w1yiqDLdixnnqb4HEGpmXxXZQ--sEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
مارک‌کوکوریا مدافع‌تیم‌اسپانیا: اگه قهرمان جام‌ جهانی شویم و همسرم‌هم مشکلی نداشته باشه میخوام که عکس دلافوئنته رو روی قلبم تتو کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26688" target="_blank">📅 16:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26687">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHYmuKz--6ynFnbMzihhSVz7RNdk9TLZftFPOUe-glgxFHWHrx8Wo3L-UabEmtvjTbrXbK06nhNnqPuus1DRmrz17e5zfn3Qd_pDrhc7NAr6DIGcqYenSeNAaL0Wf5ZyxfOnHfYqkf6O26pV1F20xMVvDBFo4k3uaE452-xZZKjeOpr22PJD3ZoUuC0h-0vUbrolUNCtj1q39fuiaqx5dsTwDo6vgNG6m38PcUwc_JJ99OIq9222wIu7FPAojz9wzTnG7lmIDpS_t0PThXlGbXNpEODTq6yCF-9kwso9KY5t3Ev9ofY0Ky38MuAhQYSlqi8Q7J7W_qqFOzCgEl4olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26687" target="_blank">📅 15:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26686">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7PTdEZ6I2dzD2ni1YDpPQhSmU2_EtjQjY-urgXkwJrRldeNj5aMzzF2D5j12Yp73ujsxWrNYca7fFcXz0gUTWKo1G0BlLFhghXo9ujp3fVuzDX8mQ87wu6foG6_kzjimQ-onA3CIU9V3DznrsmRNuVfiFNHMTnPrSvOIKnZU_dUu2Fo7H-Jy828cbdkbc7bsSoGwHkLezwyaVM7hFSJgiw9V3VY2Rpkgfm-xmfhxCsXBoMeroEocvGAygvPsTzTHOLmyAbsmk4LgzqnmqIdnrKDImZVRZbEKXxDA8I4pmpvWgRbh-70hMh7iLSQHzcTqFvjUNM2KKbKqG9JP_Cj_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛فیفا درروزهای‌اخیر رسما اعلام کرد که ازنظرحقوقی‌هیچ‌مشکلی‌برای پیوستن کسری طاهری از نساجی به تیم جدیدش نداره. هر باشگاهی پول رضایت نامه طاهری رو به نساجی پرداخت کنه باخیال راحت میتونه باهاش قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/26686" target="_blank">📅 15:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26685">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBKam9RIqhtwl66lgJvwSPxeZ7X91mF6X1IZOeo8jGOys2ndUzvLXGMr0tOLJG_fXMYOV3MvEh4lqPAn_yPzUtkZxj-0oIOdVsDB3rE74RJLkwtfRHjWjkYhslORI0ZTdCXpJZrmbfCpw9MTQNqj95q6kS52ra-fNAeVC8VjRscsYc8J7WMEbqKKECH_Y1UWNJhK4AFtJGdzRaBBcx191Lht7X3UrzHoRTL75FRjvNaS_G5HX_rLK8y3bXCUlOY6VNOAa125D0LmJe3zt9e3hC__6Aa2LZHeLhKYxi_LnH7nQB64wFiQshKZRIWWIOEGqaqM-NcWt7P3Tt6RDiJy1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس:
برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26685" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26684">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhIQjD1Pke8RBsMH_-fqycYmUm-KR-nIDuRiyGR1DWz9wFiXiO3SwKsRCLQNzUxyzumC8MUdG-kNZ9BjMywiGVnrdjmR7B4NEarqnpNJQvEc4UIBZpQ6hCWngLIdSxFNGqMTxXZZt-1-YiPqHOUVM0XpUi_7EZqgQIeE7IkidQHc-VGP0jr8P0yWicR9R9vBnu7XCwaVTMOLNsl389VvlPHZkZvKge-5MYwxxJ6TRZYYrBpWMZkWmpvt6Xm6azy4oM1Oxcs_MxAEpB56JGbBg1wSnoLXrUeYP3eh3L6vRdn-8xSGiTAoEMRGaCUFnDQWgkfHMXJzw_OzhEuBjmtpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگاروگزارشگر معروف ایتالیایی: فدراسیون فوتبال ایتالیا به زودی روبرتو مانچینی رو بعنوان سر مربی جدید آتزوری در یورو 2028 انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/26684" target="_blank">📅 14:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26683">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4VKO4T_Ji1O8cEJrz9Y2TEBCPfowNbCppSGt4KeARAJcwLdO1jrkV-3l3VXYa_viT9jxvQ6PEcruU-Y1xvgWWvvq59soiK8GkNPQLVB1srOAUHyNIN0l8Bte1xRkCViU83-vIUKmVc4cRBbwWq_aeHKWJeLmD08bYqADgJ2TM2CjJfI9HPO4P1kREoq5OyLb9gp7NPf1sKtJPxSdCAoatBxl0EZJgMQcm4YLpXBkRtqB1zATbWYmGhikzSZDK1TUzryZp7_zPQTgtmj0uyCQPPrBvVf_GlzSheizogDkFrcqPjqhG_3z6YfzLQPfEiFEj2wqv2xrCvJ07-nJf-2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/persiana_Soccer/26683" target="_blank">📅 14:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26682">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj2npeTGsIdw0dFX8dofLqxKQbPdhNrk-t4L1TXp3F7LCWzJJejwSXs33xnoie12sB3ZZR9d2mb8N5EooTek8NxAno3x9dBYo1c-SOUh8D-5NP_MTsyV5ZXkOH4cnAK0-Hr_gkV54Yl2xT8ipn10lY5NTUK6IJ3URnBAQdHXmZxHJ2-HU9_eAXBJffIh3q4afT-iacKNJEjPCRQKhiZEmAuZyzx62uhGysnVAiKnSYk2hLye9jht_ESirN0cecAxXBnYQ_ml88aQvG4EWjGtPSYMpvs_LfnJbab-vVfGYi33tuzMS5z5LeEajXmaYsrHLtZDkbwQJJ7iSLBqRk58Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ ایجنت رضا غندی پور به مدیریت پرسپولیس گفته درصورتیکه درجذب این مهاجم 20 ساله شباب الاهلی مصمم باشند با 1.2 میلیون دلار حاضر است رضایت نامه رو از اماراتی‌ها بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/persiana_Soccer/26682" target="_blank">📅 14:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26681">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw2j2aBC_BHgCx6VCTtbl06QYl0tgGXes7nB7FVPeEIxF_kWwxQ4JpAmnYugd5htTi2utgqwOoQa6Oye_Gu-sbf0extjfh_iocpg3uiCiLcits1Gqd2f97D89m4LOyw5ZEJTWhXo0Zy3YBQ7PTbD9ZxpnfT2p5h8fzH0ChVScRTLD1LZ_Ew3aTU-gbTTc37rmK10CTMN8TgFs-INy3pTsNMLpUfOBNzi2XAXWY4Fi_GvSAdwWWV66uy9vRzl0SmCteIJGYmsSSIETrQC3rvOu4hFsNCmTjMUYSii_9JEJmrreZA-uRMnL42YuQ7aiikEOXl9-KDTqtltnAC1AMo-Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/persiana_Soccer/26681" target="_blank">📅 14:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26680">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k211K2OLY5taz1WurLWWEyI5cJank0reNIOi9yraBX7XbiICGrfBQL-UmPg9YhwrU5r92amwLCpygLM0ufiSnS23yBCJ7Dh5T5Ct-23vTBJfywEB33TAfTURyTGICpqSL8cCFbrQeUlBs3Dics1kSpk-Z2vYgI3HD_oFWDGXxve3kjCWKTHRI9vxmprmrMQeydMpuAcITfVu3dI5iuCdGGaiYa7DHYE4z9CZPeHt85bgyAtKNYPEs947hzOWLzLTSlqrHW4BaMeGD8qFjuhUMAehnY5-nQUYjAv6x4B7va_8pgFKuUfLhPx4RGthwtgTUDDl9oWtKdpNLaP7GMqFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوریا شهر آبادی، ابوالفضل جلالی و مهدی زارع سه‌خرید جدید پرسپولیس که سابق بازی در تیم‌های امید و بزرگسالان استقلال رو در کارنامه‌ داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/26680" target="_blank">📅 13:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26679">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Al7317sicxiKWU5RCkD-gDaG9_s30TmqzBlWKjyLVFfjeyM5F1Z4oZfcuWume3jt4zo8InMkas1lhGlJ9kX_AZNLcQXk0G1GKxkBB6ptkomD4rCJ8FDLxgxTXZAfOr9-Fzc922M3fUex7oWMfqaCZZP7G89oZo2fWYDPmfckpb9Aq-SI2f7LwX1zjzdGSLETZELM7LI3QcxnneiY5Zmu32pyJxwVLXC7NiOSQ-tqTEbGQPDPki18a_BAMpf3ldgqAxc6QhkJgW4n4axY0M2yvN1CVNsvHNIFH6_oOx0DI4kswXvQt8lVNTiIji3FiXU2d1ZsNEQ8sZ6pb0dhkrYRFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/26679" target="_blank">📅 13:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26678">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVoLu6dpUqOK7QAfyFNW4OeGVbIqev5S1sesLBA-l_WrvGTwKV7wVq9NshhnbBLCfKleNQfsbl_N-jJ6i9AynHe_OMhBs12EL_A5s4r6x66rmcgxf4W0sEek8c34lZc7N-z1eSzPzGt7-KO2FAmkVqP-FAlvGRdPBS6zxl-dkhfh8hLF4st2Kj5h31q85rABPCGfaCr-BX6ksAHsrECI67at8HQh_nHH4yERxZZQsguzOC2N3VlCcexICM28FmeIdoBPEmFpFCNEBXRbh9yahKCAFUQC8DH4itzT2T85i9h7afZJqKUq5EUzONmsnFeAdSK66R8puQvZEQjDW60s_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمدمهدی محبی تا ساعات آینده قرارداد رسمی‌خود را به‌مدت سه فصل با پرسپولیس امضا خواهد کرد. تمام‌توافقات بین محبی، اتحاد کلبا و پرسپولیس برای این انتقال نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26678" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26677">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fkz1cygVGggA6L6LZwxHOElLXXwGV9-tUb2Pex7g4RNOkC2Ire3lmZ0V2LPJHLmNtQ0ob99VW6XaRXZKoSdPUlQGN1pGZ0JZqMB7alSFm-Z4pYOqAv3uzEmMfsAJfw0U0NYow6KXnwzSZDsvB_zx0zXcaTUpbH1MoWxLKnugPA-rSzX9oUnG8hfB3GfdGBbeMmyhZCPPE0MiMdaa92Hg1lbToRabcaIO1_Y83pO4W7njCU7xLNcLMG_p__yoDPW79UHth49l7EU4ZRhVJHkoLouBwjE801nT6G2VPylYDhprxoi0hxG48b3rMghnD-yiMcm0zv0UR9tj-5YGgmyRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
اینستا یه آپدیت جدید داده؛ میتونین تو قسمت «یادبود» اینستا یک نفرو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه و توی بیوی پیجتون هم میزنه صفحه یادبود و یا کلا اکانتتون حذف بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26677" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26676">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIMJDaa2C_62cc6oqcvFLFgzfBtLZHwshC4x5eJEO-pRps6kP4mrwWjcuEP7Ija5ogMLfOF4yzxhAuR6ox1lOFg-A9NEeijJ91OGS3WUqcU205g_GRIQsjcb6LAIL7aDv89gVeOiT99XzkcdF4QADgREFDDr7ydwT5OjxxDyslKDNsGe4WH7vCkS-qPXrq8rjagsAI5H16TDBHgDYJJ0wKywWW0UW09cd38NUM4qJfWJTKHZA1CmVXvqLdzSqIKE4gyXiEUKogT2TTzUlScBarYMYhBk43MvXzg508cqKjrGgCCtTincQwQDiANY8FlbmjF8qjoXoOJqIF3fkvpbeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌بورسیادورتموند درطول‌سالای‌اخیر عثمان دمبله، جود بلینگهام، جیدون سانچو و ارلینگ هالند با ارقام پایین خریده و با رقم‌‌های نجومی به بارسا، رئال مادرید، منچستریونایتد و منچستر سیتی فروخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26676" target="_blank">📅 13:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26675">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxqcluRFHjy2C0zOz0YCbHpm22X1jyEvkzP0TeEe1USacFzDQDwtDBoDVNEPTBM6ukMGRynisAULarimoo8hdy30yPaqnHRNg_ZQBHrf7JGw8I5gujd31wnmo-lJ4Nbxq9Lho_2j9eFvfb4pHMNGkut5oHXHvo4vwJ-_Y3ca7CKdEDAfyq7iCuU8odl_6jrSS8j96CqsiXHbOGoRazYuadlYZZchctWk7UxaS1jJA-ah3GEjtSbYEErZ45Op6n--yYEfwAcVEbnFZNQ3hil5kk04tQ4LaqRrG_3mGoe9Pmi_XbNPItrM8PMz2ZNgw6tSKfuTriuiLs0KmyzpQ-bqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو، توافق زیدان بافرانسه‌نهایی شد و این سرمربی جانشین دشان روی نیمکت فرانسه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26675" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26674">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWUL4YT1pUlWPar2a3vyM_8XHi1iU_GXba3AMQmXteB5GqxqJuOAGNviig1mlKfAHgy2qUb8QCl0kKyPrrFj_jVbGjF2fq3ybnBfmuWbwdA2ZpGvo5FhzYPdLPUbEcFdrynK5eqlRy0cfNHPnooMoH3LJP8_-dQQmpg4ssUyPEWDMCW9CWwvQwh-YfywtTf-G0KHdzydfO0VvmTLr2mjPyPWLVgfY-gn8bUrYCjRlGOvM1QsvmONPRsQNEdXKISi1gG6vxetfaR8DQ0RxNV1tf136QgXbBbB9m2ArSY6i6EoHfP4Ljyy9rAbvphnLWvfE9Z3iV5G3y5utNeiUz5i6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عجیـب‌ترین‌تولد ۵/۵/۵؛ یک‌اتفاق باورنکردنی!
‼️
صبح دیروز یک نوزاد دختر در تاریخی خاص، ۵/۵/۵، چشم‌به‌جهان‌گشود؛شگفتی‌ماجرا فقط تاریخ‌ تولدش‌نبود! مادرنوزادمتولد ۱۳۸۸ و مادر بزرگش که برای مراقبت‌از دختر و نوه‌اش در بیمارستان حضور داشت، متولد ۱۳۷۰ و فقط و فقط…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/26674" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26673">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6UEoFjQ9V3-ZwF1u8BGTZjrBxUT1spwYRthqL36h0kBbYE5ZJfH-Pl5Xz5wbeGBC1nTykrobRBkdH65Y4QZaeiadbw1zlakjJnqeMylFHcQgOvFd-7tF_VcR5k7wgvawlLEF9_rymMYvTBid664IwBOiIb3jlo_5KC_8-KcZvgkPZphqGTu9Jf6fbpVe102XGVCtVoMHw-pA-MEOCUl7BNUE0LTj5nzmdcRST4Wri7uocKo5fC184bBnm_dA4jtHFk73bpUdnKQ1DLNzT-DMjqVK74SKYcjz6LYF6-YpGW9R9FMnDuIit9ebu54NE_GhbGivJppnzQEuQWXUZB0mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
«گونزالوتورس»پارتنرسابق«اینس گارسیا» یه استوری گذاشته و خطاب به لامین یامال گفته: او عاشقت نیست؛ فقط میخواهد از تو باردار شود و با گرفتن نفقه یا حمایت مالیِ فرزند، تو را گیر بیندازد. امیدوارم قبل از اینکه دیر شود، خودت متوجه این موضوع بشوی. گارسیا فقط بخاطر…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26673" target="_blank">📅 11:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26672">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxyI74OCtaStIJYjGKNzDURaZ9eZLZ-u_TrVa2fBgv2RL_y8eDRHuxHFWga56E0Um6q3WRTkn0rn7_ryuzcsGh68P66_mUFNrvtUqLUGWDyKAiCzICOapncanJj25FclNP8_82q1_zp-JVjM6ypvvxNYvCWM4pZgGQl9aHr-Ua8BRYPDBs0KOTe2e9paM8R9LwNOkC2oUxtccKl6t6mNiY-ufRFeYUPw4ffbrz2EpdUoeIUtDsj27-g7F7myNBKtSyhKavr537qHgalrbDwj_TIhKe1IvOrfoI5i4yl797R5VAAbzc-b9bw4ZiR96DWILa8yGw8hC87m_5QUhUnp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26672" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26671">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=MDeBVf1jrem32NtWeEtaL9f7U6uC0SwiuOtJymVPXnni7BRAhusepHWBhzUpvs-Q40IdabLR_7v-ltP_T_bQSfXspTbxylQ1A3s38CsnO9xUouLZzfgGDQ4mCIQoE_obbzf-6hTcIQ5msS0IR7AdiDpQwvQUtVMOKqPuGrE6uMYhhOxrJ09HaKC8-IqTgb4QqzgkVhaaux_FJVl1vpFmHalv7L4kKBKFOcOQHOjJ9jkHj2Hujv202OwdWAiL4YDkwwU7mJbqs1kpM9k4QuT8anwQhPYejhUzPl1L1iSvSXqZAXL3g2w0V9uoIV1PWUbQR_qihSPxum3pm66-_EWJAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7fa18a77b.mp4?token=MDeBVf1jrem32NtWeEtaL9f7U6uC0SwiuOtJymVPXnni7BRAhusepHWBhzUpvs-Q40IdabLR_7v-ltP_T_bQSfXspTbxylQ1A3s38CsnO9xUouLZzfgGDQ4mCIQoE_obbzf-6hTcIQ5msS0IR7AdiDpQwvQUtVMOKqPuGrE6uMYhhOxrJ09HaKC8-IqTgb4QqzgkVhaaux_FJVl1vpFmHalv7L4kKBKFOcOQHOjJ9jkHj2Hujv202OwdWAiL4YDkwwU7mJbqs1kpM9k4QuT8anwQhPYejhUzPl1L1iSvSXqZAXL3g2w0V9uoIV1PWUbQR_qihSPxum3pm66-_EWJAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇦🇷
پائولو دیبالا ستاره آرژانتینی آاس رم قرارداد خود را به مدت دو فصل با این باشگاه تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26671" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1q3vhhMGvYG3Ndt_oZlBGF2dicp0BiGc38lOhypm4eJq4-ejgjoDLeAkc3aMEO4ref0iZ-n40FBUbCVotGauSLIwovtjMGx_f1zCO2cfJZk3o-DTXWaDVWb0MX4ADLHZfoIx3RftwSum24RheLSzZfEiNvlP4QCyh4F4j1AcnaVtqruSjPAJ64m2jKLXRSDyMmbioQrPP4w_DA6dWWur4Do3HjxCd3F-MNU2FNFXgp94vJFiYcSUJwdpjtow-WqapgUXwi8inUQKGhF98zCYoa1-ISSIbCxahgl8kYrrvSU_Br88QnRjewoqLbRESm0PHB9q_ACOQq1zPkxBQvJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وندا اکس مائورو ایکاردی: علت‌جدایی ما این بود که ایکاردی با شغل من مشکل داشت و شکاک بود که باعث میشد هرشب که برمیگشتم باهم دعوا کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26669" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkSK5_5Pu6BM41U0cPQydzEnGJpDTAO3cchV8gHv5_Har8PmxlTFqVqIijWLwZ8V5qnoeqxgqI7AW5ouD2kTwU0EeEfz4esoljKAbcjgBBq8nAC8gpqKFajreh5f7eer8Nh1UDx-WtDPIGEhn5WAdyY5z_Qel9-wV-JRLg9uY8PrwxdL5lC9vn_ZzD1rI4hXcoFevpnYRurFd_CxQS6nWM8M9R3Rbj0r6sGgc799c6K9TfdxPhc89qS0hpH0FoyFmfWLbMT51Q-7CLPAd0LJ_09pQuSjsIlzNP7TfhQQ__nszFpSJrbyehTq1elye7ofWsPrUbQWcQtmOQJ-kw9jGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریس رونالدو قراره وارد دنیای سریال‌ها بشه!
طبق‌گزارش‌ها رونالدو توی‌سریال‌فوتبالی Day 1s که با همکاری متیو وان، کارگردان فیلم‌های Kingsman ساخته میشه حضور داره. جالب‌تر اینکه رونالدو فقط بازیگر این‌پروژه نیست؛ خودش یکی از تهیه‌کننده‌های سریال هم هست و در کنار دیمین لوئیس، تیری آنری و رپر معروف Dave ایفای نقش می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26668" target="_blank">📅 11:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkTenY9ktOvz5GgtzrprKhneabO7ADIIcmWAGb2-ntCzxcDgV9qesf2-nXeMoSou2CBa0fww6aEzRpQylndc3ZrmQ4NIxNPPxjyNamBbxeWgZwrIy1uNhopjWn2bVsnin0E4kjCpgYyL0h37AI-haZW7JEHDutT5pXmTCB4TuIfONCTIJM_xNpwgAzzXu4ahBSL1SoVe0eDlreZjd6mfasYEaw7bxiJbdiHEemAgCI83nTjOTerCM_wxCfmYSpgHywxR8hQ0mKoxUu8OXoxTE60Qf2bI1kWLYawhG7vEuovfiAwKQoXIiqtJPl4p3f962_ND-pBPNuaN5H_Ez4hUow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
مدیریت باشگاه پرسپولیس تا امروز ساعت 14:00 فرصت‌دارندبرای‌پرداخت رضایت‌نامه دانیال ایری و کسری‌طاهری بامدیریت‌باشگاه نساجی تماس بگیرند و گرنه تموم توافقات روی هوا میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26667" target="_blank">📅 11:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0GkzqnWjTdwSbYJNSuSkObfuI_8Btc07peuGevfISvDtY12a83tsmKiyG9XIlYhyStUExqKCUTP3GOAScC0zWbgbmegmzglZCgWuca07hXIhpgAbPNXVcakGkj6eXddcSFwRaLuEwGvtmBNUeFJELuVpZQNPtlUS-QBDES2Dn31PndTCHbluEj-CrAErioSY2xZj_jY5eW4rVHvr5R4l6WGgJzYl41sq726K-SlOnE3pgQnL3krvbsVfUltM9OoDXWukjtSKqAWKneknSQDmL2dK_5pFEUbhUjr58Tk5LWpBbXsvVDnT1QQ1nj7vXgnpeC4vq2k-zsojtQF31lTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26666" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWMJYAtRBU6KnI2pSyLJrmTGt1Oh2Ot9YIjHc1DyjwQHWg2dK6T7WKgMo2Z70RFOvJd9UcGPM788H_sIIRBFDQA7oj1cc8SudWN5LD91FX3hSZ-wdgH2FbqoQHOTJMiunfYRTZhetkkW6iOrA3qtwvPenW5v7fxV1EoycY68HeWgwL3MP_XGoqGKu_ygXVV4DdgxJszXMiwPIpb3QklNg3HGRJBh7FQmNpisK6zMwVaEDW8hbA9W2LXdja-rvUiXO55mcQTYEtz66975oCtU1JVkPmnxDKWLohCQEG64S-n83Q-GFifE3tJwz6XHII3ZzDM6YhDcmkMf45YflAAt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26665" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26664">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnq40P-8rd2n5ajTaGDqTCyQ2t4_T0hdAHNZLmPVLW7p1WgmyHB_4-2kZ8AsPKMQJfWYh6ycV1YqayaCf8etTS1MFox_QsEsDeE-QknVFwA-M-_89DhjugsG49RFDcggrB-OVeROsqNTQs3lr9x5k9jZ4HMkfpCbKr2O574-jyesH6S5TU452W5v4TDtSthl_YEXA0vKA7StG56lm7sXIKmtUMBeUptcYPOIyLSJs5hWs8exiiw-rxqRk7EFQ7Kmyn3w-4-xI6qr16grKpWKXCrJ73cvoX7oW1nSRsNqaPm_RQKLGS7Du-vV03RmNH77EsfnIZQP6rB9nsmkmLVaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام رومانو؛ پائولو مالدینی اسطوره دوست داستنی باشگاه آث‌میلان از مدیرفنی تیم ملی ایتالیا استعفا داد! گویا قراره از بین مانچینی و کونته یکی بیاد بشه سرمربی و مالدینی باهاشون مشکل داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26664" target="_blank">📅 10:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6CY6nLLFtsu2KoneHxA3Dj4O7g8ZSC5g68iB7i5jLgLtXcSMvWCGDDlBFkvt81Kw34ZaTMSS7legEBA3kBL3MM_DiozFYifoiBhvLFbYOl4rYJLu5kw4eIvM-YL4D5AtXwNwkUSJRtDXkjvAiqhPqrDalIuTRJJYnTQL_lUpszVjNbiUUL3dbvKJyb0bGVPUVN5F-5FIrXwtthq7R6-mMzFnOwbJCla-nRaY9Z_AV_2a8omPcSqBkmmb9kuVO3SnbGsNl6RpJGrzeiaLfKFqKQMEbp5sM2Z6EH-v9i6ip5p1uFZdKEN4vg8FcRYZ0_NJ0gS2nTfGJr2pRdRAp7PNA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74f72d96e.mp4?token=m2B3rK7vPnaR7Z3Gq_TCZK0jeVSBYcRmxALBxJt8VbMjO1_eFkG99whsJkxoWEMkUobUogLgKFopA0PHoxzTffXfdop6eL86UXa_2TV9kbGNikVM8BC_A7zxnRXdnMpdxVE_uhJfU5-EIZnBLeLHdlGVADGfWMCTSS-xgcG0xXulXOyIPAp-xokIcGgx6ish8Zo5IAAuFifTOYwt2koflkBh_8X0upf8B59m1xWq3qdhlV-i0tkmFjDR-0ZIV3NfU553nN3tR-JoQrAtBjz3W444eJ407pxikyiTtapLgj7oHz2JGCA4We8bgPjTJX9Y8KI1md9abyLl1KdCyi6pT6CY6nLLFtsu2KoneHxA3Dj4O7g8ZSC5g68iB7i5jLgLtXcSMvWCGDDlBFkvt81Kw34ZaTMSS7legEBA3kBL3MM_DiozFYifoiBhvLFbYOl4rYJLu5kw4eIvM-YL4D5AtXwNwkUSJRtDXkjvAiqhPqrDalIuTRJJYnTQL_lUpszVjNbiUUL3dbvKJyb0bGVPUVN5F-5FIrXwtthq7R6-mMzFnOwbJCla-nRaY9Z_AV_2a8omPcSqBkmmb9kuVO3SnbGsNl6RpJGrzeiaLfKFqKQMEbp5sM2Z6EH-v9i6ip5p1uFZdKEN4vg8FcRYZ0_NJ0gS2nTfGJr2pRdRAp7PNA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26663" target="_blank">📅 10:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26662">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3qVMBJJHz4sFA7rcpFROGbXec--pCQnhrzLL5bpGQmAUpcmqwoVaKIjWODyAEEoA7WaDiQ3xSHaMFRDGscLOTzxDRc9ZUODX7pRQ9aoJo8YHPGk4pQ-uAKxpmT1LZ2uyW1b4Gjl6Q2-lvJcHaOYDmQssODLgWRjsyqr_NXwC2pu1YOg_yS0O3_Nwfx8ORzERBAf9RJjEUsaaEhYb8Xk8amZ1QfGpsuuAa-DLZxzmOx4VPK8S6YyTEyFoFGYReDQeWPE0xX2aS_bPL_b26bYZPts0u07lywmegWTtwalFm6aGOU1ooAfUelOswOQbDmlAgWupNyfMkiCEcCIRW75Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
یان دیومانده؛ از دزدی سیب‌زمینی تا تحقق وعده خواهر مرحوم و پیوستن به رئال مادرید.
❌
یان‌دیومانده‌وینگر ۱۹ ساله‌‌ساحل‌عاج پس از ثبت ۱۳گل و ۹پاس‌گل در ۳۶ بازی برای تیم لایپزیگ، راهی رئال مادرید شد. او در دوران کودکی شرایط سختی را پشت سر گذاشت و برای رفع…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26662" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26661">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeyzFHNMsgW8OKbd46C4OFsQ52CwdRqWyIEVou8_WDP_GDJp2cxchASFXjYsfICrsCO-wbZfq9KwwUu93uZgbCtsUPwAFD8OQ81SM4NvPTMDzsLLHrjESqDzfS4asMPAgf4vHZqrS5sAwGyZSgn8i5Kv1A_F44F7y1H_wD7UjS5-kxprRBRzL-C4cEzVdQLw3Mt2zqcKeSb2CIVgswDrLgcr-WFCAox9NzCV00KcgyFN-0qYvPtu8YXV3d4lsr_CKFgiFDewwdGsAvm7Bo1kHi4bF8Ph3FpEXdSu6ipPayiiwOOOedEIv9I0E_8cQcIpau8G4AmtmJOA8vWj7QUpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26661" target="_blank">📅 09:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26659">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5X0_l1h4X7EWWfouHnl_PHRZp9e065hwnIbI4cZiEWbPnS4MCLPXCGL6xN0uxCTmj2XJZBciGn8HCJgoerQMZKIrizRgvr44ih9A9K4o9RFf9IB5oBIA3zcc1Z0WFjaKG2feRPsPB04g6ygy-YPysgaJApf0d9WiCCUltX04DX2Uhcp7ajIfrKu9Bl5TJh-0fL4jbBNPdphB6BULA1Co2fe9Eo4sRTnOqC1UuLd0rHZjjp5FVZJuqPVuT04n4We2xYsXIbmgrFeGNSo1yykgCgQPAPUXBLHNrCd4ltpgNCXA-7xHVTux55_HI4nKjEG2YzmdIVRgM10r24JH4NNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26659" target="_blank">📅 09:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26658">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=ro92PmQqHQnRpwgDhFVMFMRPLe9pzdrKgXZr_X6NgisUfzUQIenGsJqNPZECMCwSzbnOoiAoq6IS_z6blVQE-Ooh1QnO0bWkB8jw7tYloZ2Llbu2GjhbNORtI-H1D8X-AMh5Tybgfowi23Mj-BQEnEFfqxdjWNDjK5T2ORRchnT8kMvLXCfjf_SjbVJWYaXvD8ixHY4ue9c1w86pV3XSnJmkm6VSd94ATEa7y8rr3TscxQ5yz-MpSd9aFcUc77hKZwMG7zq1iX0cczmXlt2I1k3Ac8Uq8fJumOtKAuU43BssMK3EEJxACN_X6RAmK8fgoVOkuWpBvDw6-pbfc7RrQWR5PBYuYde9m1WGjo223XVvGHKpQeQM8u6yeWVSxhgVN57XsxDtl0D1UZ4qNDLRzGRTM209aBP99laP1u912P2pva0eV4-ygFeaiwpH5S7LOEKNXZ61f37Y0dj97RIlKkgw1x3EIoElNY4AwgCUgsAwQIHsWRQFbAfXt9sA43JCJFRDW_54O7NZKof86OYKRx5Q9VZLVVB7ANLeweQ3l-o3_J3isGGHZL4koE_LMBHO6kScGrLQb4uLHdcXw44KLAaGHuDAPvBStSPN2wMUBB8IrsiDZATC0_i6KqCt1ekUNr3tX9dKmwlRlUhzCGwfpfAr2fd6wnNvfl236_9HyHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feaae9b61.mp4?token=ro92PmQqHQnRpwgDhFVMFMRPLe9pzdrKgXZr_X6NgisUfzUQIenGsJqNPZECMCwSzbnOoiAoq6IS_z6blVQE-Ooh1QnO0bWkB8jw7tYloZ2Llbu2GjhbNORtI-H1D8X-AMh5Tybgfowi23Mj-BQEnEFfqxdjWNDjK5T2ORRchnT8kMvLXCfjf_SjbVJWYaXvD8ixHY4ue9c1w86pV3XSnJmkm6VSd94ATEa7y8rr3TscxQ5yz-MpSd9aFcUc77hKZwMG7zq1iX0cczmXlt2I1k3Ac8Uq8fJumOtKAuU43BssMK3EEJxACN_X6RAmK8fgoVOkuWpBvDw6-pbfc7RrQWR5PBYuYde9m1WGjo223XVvGHKpQeQM8u6yeWVSxhgVN57XsxDtl0D1UZ4qNDLRzGRTM209aBP99laP1u912P2pva0eV4-ygFeaiwpH5S7LOEKNXZ61f37Y0dj97RIlKkgw1x3EIoElNY4AwgCUgsAwQIHsWRQFbAfXt9sA43JCJFRDW_54O7NZKof86OYKRx5Q9VZLVVB7ANLeweQ3l-o3_J3isGGHZL4koE_LMBHO6kScGrLQb4uLHdcXw44KLAaGHuDAPvBStSPN2wMUBB8IrsiDZATC0_i6KqCt1ekUNr3tX9dKmwlRlUhzCGwfpfAr2fd6wnNvfl236_9HyHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
دقیقا
20 سال پیش درچنین روزی؛
رود فن نیستلروی ستاره‌تیم‌ملی‌هلند با عقد قراردادی به رئال مادرید پیوست. این سوپرگل دیدنی او رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26658" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6UZL9Anomy_x1FpYtbhLpK8EHEuJTxOSdV6cnck49Qw9JkCiftBZFnMA2A5fYNemBT9eJzbhsuCR7nb0_di8WqivJDllK9OclVdcC2li3auFCS-EqJFCCnoiSxFFd4RVPTRSH-ZKrdsdU15BBBq1-aqpKr4MBIkU_KdXRx1VrbBNT4mmV3awxemzCQQSQVioConfYntinW8TQurqlW_K77_TSBcwjX4NS3mWAT4imGhTpDwL06X1THaK9bZWK5a3HkIqSw6fJbMSlhPXG_4HbBD6IvVk0ODulXeJNgcYmhlNfGVs1qHT79DrvXu5HVTl9-BBxGD7HztOhiO986Ihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPbGitZnFAuDm6CbIhuMOPmjmxLkKDPJWzYzvRxX7PCpBe99i3BfijC0ht-h25XQEF0HDG3BdCozj3Jbfdu-fPkALMuMfy0pmqZAwxhcSnOwBe_VaoGT72VTE3WsgzTkAzhk73bQEsAgoQbr-_S6MBud6WjHpm1LCBqQeiQLInpuxC9u1lTmXpJyG9vNyP-jAawbe1i8no6upWIu2WrjDnNgzUKuXaX-vApG6jqJd4Cbcc8Zvd4kopfnHWolyrChjT9o0pLNaW-oNTITpj3eVUZ-d_Mt8W9ZYXZk7XCubJlvTyI4xOYSagHRezpSfj6-98xZ0SrMDZiy50HcpOWTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=iatB8JLng44fo8drrkLkoX_yT2Uc08raoisqoGJnOLYdHvDad3up7z9UBHEDipnmFl4dBLTx911O-yhVCB1EOLyaUenb_TBzBf1pWzSBYDkg3H_wu-iaWaa2zAlGGht4z4rZZOgk9pPFAnyD0sSvvrI1BehEBQ6_lvyrOTwdzfKKIqEHTWSqbYYi2kkt504K1yj2vhz2lhM0hsZf57XDJ5XNjGipRkEToICy8bH3KFU1cHV-Ro8lfBBItLYtOldrfZ0dEgAqG1bWip-sNiBuCshRw3gIVbPE0LQBXshpUsQMNvzW0K0BeZWeVrZmX2bMepKo8DGNiCi_s858-DXzDEGev4jH5Rcj9ZsDz4xIq1vqgNAhFjpUDWMH6H1XmRAmw7JDrjyA4YbXYJz7pYV5YNgPD3CnhHJTmD_CJyXsH_CrfRo-lOiWkBb159sj6xYcKelFNGBhmZ2JUXbEosl6dbaYJL0PT-z-6YG_H2ttNLnnj3o7reNEw6ZQAJKiQUT0IIvTKWym_hiUYAoKsgzS4kZ3K2qEKmdLDAcrRkIwzwGCI8urmgJ5Ck8BfHlLCmHR3lFJVEDgvZQ8chdZQf5NZWPfDMZSaLyt2olk1a_oE-S_uQOqEldN9GG3oybl4rZktFOgGuhkWOf8Myi_Ip-aGZKt46spXUvU1P3rsXZaCyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=iatB8JLng44fo8drrkLkoX_yT2Uc08raoisqoGJnOLYdHvDad3up7z9UBHEDipnmFl4dBLTx911O-yhVCB1EOLyaUenb_TBzBf1pWzSBYDkg3H_wu-iaWaa2zAlGGht4z4rZZOgk9pPFAnyD0sSvvrI1BehEBQ6_lvyrOTwdzfKKIqEHTWSqbYYi2kkt504K1yj2vhz2lhM0hsZf57XDJ5XNjGipRkEToICy8bH3KFU1cHV-Ro8lfBBItLYtOldrfZ0dEgAqG1bWip-sNiBuCshRw3gIVbPE0LQBXshpUsQMNvzW0K0BeZWeVrZmX2bMepKo8DGNiCi_s858-DXzDEGev4jH5Rcj9ZsDz4xIq1vqgNAhFjpUDWMH6H1XmRAmw7JDrjyA4YbXYJz7pYV5YNgPD3CnhHJTmD_CJyXsH_CrfRo-lOiWkBb159sj6xYcKelFNGBhmZ2JUXbEosl6dbaYJL0PT-z-6YG_H2ttNLnnj3o7reNEw6ZQAJKiQUT0IIvTKWym_hiUYAoKsgzS4kZ3K2qEKmdLDAcrRkIwzwGCI8urmgJ5Ck8BfHlLCmHR3lFJVEDgvZQ8chdZQf5NZWPfDMZSaLyt2olk1a_oE-S_uQOqEldN9GG3oybl4rZktFOgGuhkWOf8Myi_Ip-aGZKt46spXUvU1P3rsXZaCyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1t18yf53LzXeTy8VMT8GQTh6SWoDWvtpZA6s2iY2xcgDUMhRSlnCDT5iUaTH2lVcEsFPFNbl5cpywd8wETA5lrm2SW4z2Nq8dzStDeu1XdGjFJDOOR4yxdS-1WwzjG0Ac4i-j5M7PYR4AsE4b1-hun9F6KIkkYayBCD3y7rotchpzNGyUjc1wAHmtonQ8ciA6tMYJETsBnVK0r6fVEzyCqO9GUb1rAqTQ7qOOB8MZdkVHVQueVTTK6pJx_HzKBEWro3Mf1dW4Rux6_vq3uOOQvAr6S5faFGTlgeVDc4m8XApwbgBIwVgK6Vy_QJM7VPx4Rvm9XQOdNIdqTebI8_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsEzjLafV0l0GxpYS2l7Q9NWSuFb21zzWZnrQJQ1nnjSI4LtgJIJAOejdpKqrAcISGDVNjgrO6WIMvYXbiZv7Fb81lI0ULRNcuhxk96yyQ3PSN9EQYXzKtylGwl4OL-7MJhUjpZqXFLL434rEWghgXHYyxZZ1Epf8fUbDi1x67eRhkZdxxJOikPZgsVMttK-w0ajV3Jglv6hysAzaO1bzUZVkH9of5PUIWeGXBEiuRqNxjfmpHQl5dqJ5CZpih9qy9vgzhOwSACBszYUI4H08g-V7VLioygZIoHQA8NsIXJjOGCqhsuuwKFhxDFSf5EtOF249ukTjW-mnEyYKUjhVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZHajaGSDwcj4r-WDbszqnUnmPSmCCgis3EHYNrn-sXQKqjVk2CZQdFkx3WcorA6a_xZaADi8h9BLn7J9eEllfp9qvfB66pjJ_SiCbuMHkHRXK4na-lnQGbOX1CjNh8g5oCCZiEuKHdxofAFkpBxqyPo1LVwKYaE2_3-Y-wOXxvK7MgHr0TTAXJ6WIuxF82-mOrupFU9ufnY5EE13GfWpgjo2OyFar31JD8Dy5F5LTG6SdKfuYcm1rTWQUHm58Exgp13kKTQ_hJhlMtgURAN21EIz-F14JNba62fto0MwVZYSFmSs6mMaLBqZ5H-Y6IkPhk9uEbde83CUFD-NomLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GgmZAm83CU24tUqzS5v2EFB5Jit4z2wBQdwIa07-bjUpkW6qwrx3vOEiWCPox9_7xnsLRyAdPrzjcBZAeDNeG0O_fwES5ijy3EnDaxR4pKNKLJEKXiqL2tb_Fxyqa5-QhO3Go2ONjSSpaRaReBqttE4NvQhLaVEBZ9hXbrp2cm4dGS5OzVzFkCKnkbCclE3F3E7hzfD-9xEWkJQEYWmN7E6gwZnsYGwWXjUOLpaath6P90ZE0q62ju9B7CSLkKzxqlTlsUyj5quol1TyEQFNFRCsXGC0v5nE7ifjQGHAIwMPmIImURhUT_AZpA4NJZERu6d0GvIqV3_qX_h5XREs0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GgmZAm83CU24tUqzS5v2EFB5Jit4z2wBQdwIa07-bjUpkW6qwrx3vOEiWCPox9_7xnsLRyAdPrzjcBZAeDNeG0O_fwES5ijy3EnDaxR4pKNKLJEKXiqL2tb_Fxyqa5-QhO3Go2ONjSSpaRaReBqttE4NvQhLaVEBZ9hXbrp2cm4dGS5OzVzFkCKnkbCclE3F3E7hzfD-9xEWkJQEYWmN7E6gwZnsYGwWXjUOLpaath6P90ZE0q62ju9B7CSLkKzxqlTlsUyj5quol1TyEQFNFRCsXGC0v5nE7ifjQGHAIwMPmIImURhUT_AZpA4NJZERu6d0GvIqV3_qX_h5XREs0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVKg5iXkckjpFbC9zD9KfzluTXrWw55WJccl-KJhJlrU79GCsi5HeILYNbgLV68GVY2KAAbisZLDF9ZjWVr8f8-1cSg-KYoazDC9jVpIC9hXRDxThPi1o9Jo7NjJvpEPXUriqYhBajPYnXx7CcFl4q2t1RcfU-hrx-_IWnDZgQdBL1Z75JqkZ_QyoeOBmRNt7nvpQ5Dowxw1V9GNcTMN9FmBB-wsXErchswJEtdzN2-ZqCtyoCeB3vGYjv46sV7sqeL2Kmafx0j2bg97qfV_TDeeReDF1il5HNKYAuvVViYj4gL2tFQJHoLISVxyKrtlILZZulEcn6sGnAq0ZaUd_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfbArpBhMomM8QmAavnyPD5FgErYXAYGF4t6EvhPok0ulV6MBvtlY-JklbZJin188-LsjQY70JjqlNIMx3DNYTmGCMiHVcpg6CE5JqS84HjokF0V6ZWTinI8CsjjwRP1aLCzRbKBCj2fyGfDVng1Ejkc4-B7FZFwdwfRdrk10GjfrdbTolOba4yQuBdKAIT5_Vv7H_YUw7hbwGrGgNUoMxXhJ0OKfr15YU-Tv3z4Tb_EQLaLXuD_XbecWcrq3uly2BUw4A2ovIT_CJmPTjcxA3xWCTkCEIJzKpKVilTaQzDi0B60gezWPsJwW0EPbkqeG9nU2v16pICOoCmcyRe9tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyDXjoJuacfYWHTs6jZ30lqHXFAevkCR-wlnBo9h4U_TyHyGDKvFDwAuo3-qRvVkTzKWPtl35yZbZnSQNIac0gBForQO2KHyUxdjQzZpiDNTiYHFqGQnhj5KE3tyYH24PG9g4QAIzfklj9I8KoP4VxXNaqeBPYLUJHnQ10ifiCu6ww51D-YwKsz6lvaaaNABmhOPXwczmdfvahzE3kDZYfnx0dG6pXzGVEY0b_c7UPTDaAgpJVCraMc4PUsnpTFFaLqZ217SbrcbVHY0A3BdEy-4ohupwCcVHvyAy80GiBhl67dyyUXmsvZPWYUuO4qVUAmS6AcVRNVaJbrNOCdwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=QdDVxrcUrsidxmVGCC9UloJsHUw7TjsKbQJvge_dOL_QL8IrkDKu5RerQ7nWwhL7OohJ3JR-eGv2M-OnNoLRIodhzvOAKsJ-muYAqct0CbsM9zxWaH-wxhgFaCidVYpivPStId6it8NTdcCys2oreSWbUsvWVcKW8zZJFCPiVLj9_lDH75UGokjuXtMdrFGrFX36IsdcXWeER79FSihEgZ6G7MMznGamdznyQwdw6wmXh8NVjscszAkPXaTjWo9R3OxpxY0AjXLXGrxzOL7xfLH8hnKadl-JpTL2GGvRWevKVpU57o5GzT48IPNssKGcxEIg6DbypzPjyqF6kz-XaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=QdDVxrcUrsidxmVGCC9UloJsHUw7TjsKbQJvge_dOL_QL8IrkDKu5RerQ7nWwhL7OohJ3JR-eGv2M-OnNoLRIodhzvOAKsJ-muYAqct0CbsM9zxWaH-wxhgFaCidVYpivPStId6it8NTdcCys2oreSWbUsvWVcKW8zZJFCPiVLj9_lDH75UGokjuXtMdrFGrFX36IsdcXWeER79FSihEgZ6G7MMznGamdznyQwdw6wmXh8NVjscszAkPXaTjWo9R3OxpxY0AjXLXGrxzOL7xfLH8hnKadl-JpTL2GGvRWevKVpU57o5GzT48IPNssKGcxEIg6DbypzPjyqF6kz-XaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sp76DjQw5BpzX1aiVniibyT04P9PMPXzjR4PW2VxhPDZ6YHpCI2wbouhXc-LE5z8S0Z0YNc62dRY5X9lGNSUhBFnROhGk22R768zuLszzq4oxFDtU4Z1W9Asw7-QgkfLcNoUsrVTAj9pNK9ClMMUzx0b8s7Zhtjylj4-mr96zP0yggR0sZmvkw0ObI18GSwIqpgBw-3yS0cxTTvR4jAOEg_EXUkMO4g9bN3iPpkNJN3Nbj8VTKpa_Qep64POkNrDZ0qBLYHnbNZUGxXBliZOkvvAo1z__xIhPW0i7ps_tJjdIIn8UFTvGTVQjiQC8TrACKMr3mw3Jy3KvJqcwER_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
