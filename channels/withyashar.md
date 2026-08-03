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
<img src="https://cdn4.telesco.pe/file/dY4l4vfx1LLu86P3nolCTfId0RMjPQY1OecpXgfFa8f5Sld6U8_COjqmUDbFvYDMFRP4_qZZUKSY6GnW2WQKeim2Moutqvb31FmqyJx53pmZ2I1wm1AcR9oZbZ5F7Rnqdy4g_tv2nREA3R2i1pY2wzKSnID-U4LRA48Ee2BTNPi4uDRQXBz-zGVupQ7si20tHoVwrpwjnVFvQo6Cbu_yTcMO5q7uGNOxo7W4NNFMtYgh3Jt-6eqcNRIUuc3Fd72F037XHMUduokEQwIQPJvHbJ0iJUxmV0WnectyNnmxIUuiVcZX4CDIHriLsk7tEW_F66lEZpujVttJDeoFpdECKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 443K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 15:23:35</div>
<hr>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=Eqd9aHWliLzWNwysDcQGVdMmpBkWpoUX_GNo8YQLSSLoHEjBUH-bbMpNO28KXj7_mMuQWgPEIe_mczUTVtnnlR7abnlUT8uR-1jfN3VAu7GiQIwIW7rdEiIGz6oxM06YCnT3RH4qfsRGrN_wZrBhCdWVAC8fWkTUYP4ORJoJhPKgbgMXb17mYjTBOc-Da7gOGyneWYVIMIRv-BzevoojKA6MgDrrB7IbdiEGC-9K7YcaMiu9jAotD8BOHoNpUFdHM_0keZBeThmBy-rlBhKXR0d9yih4GKWjKW7bNpRF7BSnKDHB_vEFhq8P9RlTJMwKk8kPLnbfxWV25Ekf0saunRDE6lnl9GdeSU5SihG_807nMGjNvpb6uGn600WN2LcCTjEN5BDoDoelST1E5HQynYi2xcGd9EFNY2iSds2YYjOGuCGNUe9mps_fXDTRHZp6j1j62J6jUtrbGqH5QyxkuMDvGQvC3ZRYX8PVIFLJK1hhDhIYB094Bl1RYvLZpbG0eRcnA74BhObfuqattf7Rb4Q39XXIoXWFWx9cFMtFrVB3VdP_2tytkaYCJ1-rByOpUI3Nb58pFbNnPYZUDmpcxSm-99be0yIwrBJjfUgJ8seL9QCezGohyvztX9VWVCqXZUEByBrv5Gg4phjdg0ZQgfqEa1YuFUQ5Xpp1nxYhbUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1c503433.mp4?token=Eqd9aHWliLzWNwysDcQGVdMmpBkWpoUX_GNo8YQLSSLoHEjBUH-bbMpNO28KXj7_mMuQWgPEIe_mczUTVtnnlR7abnlUT8uR-1jfN3VAu7GiQIwIW7rdEiIGz6oxM06YCnT3RH4qfsRGrN_wZrBhCdWVAC8fWkTUYP4ORJoJhPKgbgMXb17mYjTBOc-Da7gOGyneWYVIMIRv-BzevoojKA6MgDrrB7IbdiEGC-9K7YcaMiu9jAotD8BOHoNpUFdHM_0keZBeThmBy-rlBhKXR0d9yih4GKWjKW7bNpRF7BSnKDHB_vEFhq8P9RlTJMwKk8kPLnbfxWV25Ekf0saunRDE6lnl9GdeSU5SihG_807nMGjNvpb6uGn600WN2LcCTjEN5BDoDoelST1E5HQynYi2xcGd9EFNY2iSds2YYjOGuCGNUe9mps_fXDTRHZp6j1j62J6jUtrbGqH5QyxkuMDvGQvC3ZRYX8PVIFLJK1hhDhIYB094Bl1RYvLZpbG0eRcnA74BhObfuqattf7Rb4Q39XXIoXWFWx9cFMtFrVB3VdP_2tytkaYCJ1-rByOpUI3Nb58pFbNnPYZUDmpcxSm-99be0yIwrBJjfUgJ8seL9QCezGohyvztX9VWVCqXZUEByBrv5Gg4phjdg0ZQgfqEa1YuFUQ5Xpp1nxYhbUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خودش بمبی نمیندازه ولی همه بمب ها پشت سرش می آیند !
@WarRoom</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/20404" target="_blank">📅 14:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اتاق جنگ با یاشار:جیمز باند.
قدرتمندترین هواپیمای جاسوسی تاریخ، ریوت جوینت، در حال ورود به منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/20403" target="_blank">📅 14:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/withyashar/20402" target="_blank">📅 14:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=EWFAVGsSSdIcbkLgGj63gOS4XyzW8jJQxtLPFUnEP29c-2Kgdx47bGMWQ1xmZP8AmrQWpMG6xBhWXln1YYCsy1NC_1rwtwYNT_5bpqFJzzUV_ISd5G6-0gg3PZOLpNIEZm_9X-GYFKKr9Qny5SoLsIb3K-rN0ZW01u1eI18t_IdDVCPZFM1z6KRvQZv2neSgbdyaqbwqbMM2M0foligX3IvRcGuz_s0ZXu09e8Ih48k_yGvZ03mEU_PVxTK25L91gcl-rfhVKXWTEKqJbcIG3KD9q3WwqHuxF29xWujvYYnmSNaXv-5u0hBxZbY2q3141aUUh1TVdeE5iD2M61BSFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9e4766f60.mp4?token=EWFAVGsSSdIcbkLgGj63gOS4XyzW8jJQxtLPFUnEP29c-2Kgdx47bGMWQ1xmZP8AmrQWpMG6xBhWXln1YYCsy1NC_1rwtwYNT_5bpqFJzzUV_ISd5G6-0gg3PZOLpNIEZm_9X-GYFKKr9Qny5SoLsIb3K-rN0ZW01u1eI18t_IdDVCPZFM1z6KRvQZv2neSgbdyaqbwqbMM2M0foligX3IvRcGuz_s0ZXu09e8Ih48k_yGvZ03mEU_PVxTK25L91gcl-rfhVKXWTEKqJbcIG3KD9q3WwqHuxF29xWujvYYnmSNaXv-5u0hBxZbY2q3141aUUh1TVdeE5iD2M61BSFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده دود بزرگ و غلیظ از سمت ساوه دید از قم
@WarRoom</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/20401" target="_blank">📅 13:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رسانه های رژیم : یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه بر فراز آسمان تنگه هرمز رهگیری و مورد اصابت قرار گرفت.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/20400" target="_blank">📅 12:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد @WarRoom عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20399" target="_blank">📅 11:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بقایی: ‌در وضعیت تنگه هرمز تغییری خاصی تا زمانی که آمریکا آتش بس و تفاهم نامه را نقض می کند تغییری رخ نخواهد داد
@WarRoom
عراقچی هم امروز به کربلا میره و مملکت تعطیله</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20398" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaf651e2d.mp4?token=fH3HiCH3UU5PlL9quMjk2qbKwqu_8JHUgWTMlnxMXc6WVjkaS7ghrasP4EVjwhP3Lz4HxNBDvScnG21nojBah0vwCaJApNQ5L6AScPQLYeW5lNxyj6ZuYNkHumF-MmLZMdwhMcU5Cjs6kWPpIUnxbyuhvRsUQYoWX5mBunOXYVKJMnUysW5V2tjyWnnE5YpbDZDbc19qZ1YKF-V25gUaByJ-ioXDUsc9BvYN9NFypD6sbeTKiBVxlWJMdDrHq5eZsx8eFrSgQYrgtf1HEfbHsYQYfS_JiYh_NLuEBkjqZmW8O2L2xMvT2iU3Hdj4tDDm9Q8esMlvsCswQTaefe0nemszG1hkqyI5ZtYiNdYRj_uJLCOozh5xAAn_SS6sDbGhKJjwULwJl008P8_qS44Y1lSAeU84ZpInGg5MqkUWEoTcXs57yYkeL77d3bhgLr4O5SYD4E0qBjBgwjJHLgER9iOa5GyHf54e1_McyuDues6MzbVeTbEpWrgGYTpgVibZKf-d_M63xXwyjEkfokBu9H5nmce_Jgm5xeCO057tBOpDyS8BbVrWXi9yODFyVYTCbbWLXYjUdw_txVBxPGbuvYOp9fNKGzXiH-L3B4rS2nPHEwir9es_L119fbuoe6All7NmADMSXrXhRl6_kwhSYuJ5nW_vz3kOb043PmcBfts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaf651e2d.mp4?token=fH3HiCH3UU5PlL9quMjk2qbKwqu_8JHUgWTMlnxMXc6WVjkaS7ghrasP4EVjwhP3Lz4HxNBDvScnG21nojBah0vwCaJApNQ5L6AScPQLYeW5lNxyj6ZuYNkHumF-MmLZMdwhMcU5Cjs6kWPpIUnxbyuhvRsUQYoWX5mBunOXYVKJMnUysW5V2tjyWnnE5YpbDZDbc19qZ1YKF-V25gUaByJ-ioXDUsc9BvYN9NFypD6sbeTKiBVxlWJMdDrHq5eZsx8eFrSgQYrgtf1HEfbHsYQYfS_JiYh_NLuEBkjqZmW8O2L2xMvT2iU3Hdj4tDDm9Q8esMlvsCswQTaefe0nemszG1hkqyI5ZtYiNdYRj_uJLCOozh5xAAn_SS6sDbGhKJjwULwJl008P8_qS44Y1lSAeU84ZpInGg5MqkUWEoTcXs57yYkeL77d3bhgLr4O5SYD4E0qBjBgwjJHLgER9iOa5GyHf54e1_McyuDues6MzbVeTbEpWrgGYTpgVibZKf-d_M63xXwyjEkfokBu9H5nmce_Jgm5xeCO057tBOpDyS8BbVrWXi9yODFyVYTCbbWLXYjUdw_txVBxPGbuvYOp9fNKGzXiH-L3B4rS2nPHEwir9es_L119fbuoe6All7NmADMSXrXhRl6_kwhSYuJ5nW_vz3kOb043PmcBfts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏سناتور ریک اسکات: بعید می‌دانم مذاکرات با رژیم جمهوری اسلامی به نتیجه برسد
‏ریک اسکات، سناتور جمهوری‌خواه آمریکا، در گفت‌وگو با فاکس نیوز اظهار داشت که تصور نمی‌کند دور جدید مذاکرات با رژیم تروریستی جمهوری اسلامی به نتیجه برسد و معتقد است ایالات متحده در نهایت بار دیگر به حملات علیه این رژیم بازخواهد گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20397" target="_blank">📅 10:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی : ‏نیویورک پست با دو تن از رهبران میدانی انقلاب ملی شیر و‌ خورشید در داخل ایران گفت‌وگو کرده است، افرادی که با به خطر انداختن جان خود، تنها یک پیام برای جهان دارند:
‏«ما در حال آماده شدن هستیم. از خیزش دی‌ماه درس گرفتیم و مصمم‌ هستیم کاری را که آغاز کرده‌ایم، به پایان برسانیم.»
‏«ما به‌خوبی می‌دانیم با چه خطرهایی روبه‌رو هستیم، یا این رژیم می‌رود، یا ما.»
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20396" target="_blank">📅 10:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری میزان اعلام کرد که صبح امروز حکم امید بهزاد و پوریا صفوت، زندانی‌های سیاسی اجرا شد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20395" target="_blank">📅 10:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مقام ارشد آمریکایی : هنوز به توافقی با حاکمان ایران دست نیافته‌ایم، اما تلاش‌های میانجی‌گری همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20394" target="_blank">📅 10:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20393" target="_blank">📅 04:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6507572.mp4?token=b7ucFD6H77wnY545sfh4cTNQpLZf1ZTbyiGGFzi_A6AeEBGKC-HgbdW89HjipY4FBt6jSEXe3CPH91yEzfkYCrFvFTwNdx9Re0QsNcgXa6ZSNhppXxd3kjKoY_97WdNvshdHtWEAzUTSyw-A7nkRGWZ-Q-pUqax7R0tTEkv6d7hH5oLyjZzEqtNXkzBzgFpeE25nvY4noDLggrrI7Hu0e3Uw5gcCiz32wKL_b1e_QbrW4Eat88a-z7vyJfAOzJNqAUHmUrbcM1pTjR0J3b4LrpSt94m97QPfHHtGClgCpafXp20WzQF0FbywilgaeK913S1GNa0H3XeEyWF2TtAw-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6507572.mp4?token=b7ucFD6H77wnY545sfh4cTNQpLZf1ZTbyiGGFzi_A6AeEBGKC-HgbdW89HjipY4FBt6jSEXe3CPH91yEzfkYCrFvFTwNdx9Re0QsNcgXa6ZSNhppXxd3kjKoY_97WdNvshdHtWEAzUTSyw-A7nkRGWZ-Q-pUqax7R0tTEkv6d7hH5oLyjZzEqtNXkzBzgFpeE25nvY4noDLggrrI7Hu0e3Uw5gcCiz32wKL_b1e_QbrW4Eat88a-z7vyJfAOzJNqAUHmUrbcM1pTjR0J3b4LrpSt94m97QPfHHtGClgCpafXp20WzQF0FbywilgaeK913S1GNa0H3XeEyWF2TtAw-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمو مارک لوین به ترامپ برای حمله به ایران پیشنهاد میده:
۱. تداوم توقیف دارایی‌های متعلق به ایران
۲. ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
۳. هدف‌گیری مستمر فرماندهان نظامی
۴. حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
۵. هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
۶. حمله به بانک‌ها و مراکز مالی
۷. دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20392" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عمویم پیت هگست
:
وزارت دفاع آمریکا آماده اجرای عملیات بود و همچنان نیز آماده است؛ در سطحی از آمادگی که از زمان جنگ جهانی دوم تاکنون نظیر آن را ندیده‌ایم. ما کاملاً آماده‌ایم و هر زمان لازم باشد، عملیات را آغاز خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20391" target="_blank">📅 03:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز: زمین لرزه‌ای به بزرگی ۵.۴ ریشتر قاهره پایتخت مصر را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20390" target="_blank">📅 03:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20389" target="_blank">📅 03:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAf0iVIjB2z2vrMwqIt4lxx6Sip4jNsflrUeBIXbbly0rz1sWi0LRQ2KaqP_ag2W9mtXJw6VKuAKthZmHiw0IKhul2CEvBXtEhJJew7lJHLstpbz90tbOiaq3eL7hWxt-538GUA1hMGhyULOLWGkQ6MqGbypMNDRI4sN9wKG5gIZNwBZf3xrCZ5aMwFNOjpNocPzbWfnLY_98K1BcPrl1GP9o0S39p4V53TGk9JOxD15F2t51_vSmxMfmbXNATIJdt8LFe3p9NJJAPyyU92IJ1g_m9BkYNQCGtPEo5I5DsOCk7wcZauDFujQj7vFhxOROXDPSxmHfG-1-35RH7Sv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۸۴$
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20388" target="_blank">📅 02:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ دم توالت: در حال صحبت با ایرانیم و قراره از فردا بعدازظهر گفت‌وگوهای اصلی شروع بشه. امیدواریم این مذاکرات بتونه جلوی کشته شدن آدم‌های بیشتری رو بگیره @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20387" target="_blank">📅 02:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فعالیت‌های نظامی قابل توجهی از سوی آمریکا در عربستان سعودی و خلیج فارس مشاهده می‌شود، به طوری که یک پهپاد شیلد ای آی V-BAT در حال پرواز بر فراز تنگه هرمز و یک هواپیمای E-3G Sentry بر فراز عربستان سعودی است. @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20386" target="_blank">📅 02:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJMmOkshpzVuYT9Q6H6oAVdfT9YHeFfhZlHXzJTcnNANIvh_qXSG4J2iXDzVIP-va_C-gPlcHhC1-OAnkzo5-Lsk59Uth-Ted7xINxY6EpnP7O3nafRS3JHkOL2OdIB44mcXKii5cBB4mC41oGSluA_DOYV9zgrI2RLBbnYsJ1m5yxa8Kiwas2UKbQyZ-9jxzmMle5PtvqeVCJRGrEFl0qIPh3IfzznHPoEZNjxJeFqA5skSBOnHXbZ7e9Rw-rXRbjJNZZYbkUHm3q7cEb_GWSWrrxMWESQ3SwFlyoXv3KPA7RLUfgq_IbUVabp_DfWH_wPt0U4gJfzHeqxcePATEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس  https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==  کارای اداری و اد استوری رو انجام بدید کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20385" target="_blank">📅 02:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پس از آنکه ترامپ تنش‌ها با ایران را کاهش داد و احتمال توافق پدیدار شد، قیمت نفت بیش از ۶ درصد کاهش یافت همکنون به
۸۶$ رسید
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20384" target="_blank">📅 02:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=qosZwCNAXtfqQdEIQk99YZ8sXLorvDWEHls5vZd9QQBkBfTdunrXFeeI5IjQ0YKTYjuKi-14Yhm17VEpe3rZ24hR5h0gvCA9qZyeqGD3T2xaQzxnKATN3s9DJMylzDjAMy_ww-UMcwl4Mdko0a4xTwTJ0lBVKCzDCWwHb05M_fjhHXG-1hD4eT-9WzFv98P7brJV_O6ja58Eo0mBDiTCMAct42cL8QbifudymclsD5qfFqAxZADkmqHPsnIBKYBFndWqwRJNgP9bs84PTq7G52V1QmwUUu86ljA9GZYOWfRpHLdy1qd-H_6PP_mcyy0ksElBlt37Nzbaz4gF4puUTTiYP-a1CyXqT6zKYyyOp2fNqAEKIYbuqL1xRkDplb8i_H34fxi71UYxOGv-J8TfSTIMK0UEwIyxncu9sqa3BaYsW11fiX0W7BkAIHAcHRFcvFTtTDPhgtPJxqKpmmAh2gVOwVnluF26NtWQBx7HLtkbm4EWqN5RJUldPU9Sa1w4Q1SHlKLgOfmEkIjh338c51u1Zw9xotTWrjOzDNV7TgO1tCNozeevDD0xAegzRJflAXlhLxPzw1jVQ6C7-ITLEO_nwg-G3tZq3lwK6goXri8jO3r3ohCQnub71EVPL6gu1ZoftRonYzZ9NfC4zTCSlUt3U6AWzVNbSz1IgItggoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28b4a7f0f.mp4?token=qosZwCNAXtfqQdEIQk99YZ8sXLorvDWEHls5vZd9QQBkBfTdunrXFeeI5IjQ0YKTYjuKi-14Yhm17VEpe3rZ24hR5h0gvCA9qZyeqGD3T2xaQzxnKATN3s9DJMylzDjAMy_ww-UMcwl4Mdko0a4xTwTJ0lBVKCzDCWwHb05M_fjhHXG-1hD4eT-9WzFv98P7brJV_O6ja58Eo0mBDiTCMAct42cL8QbifudymclsD5qfFqAxZADkmqHPsnIBKYBFndWqwRJNgP9bs84PTq7G52V1QmwUUu86ljA9GZYOWfRpHLdy1qd-H_6PP_mcyy0ksElBlt37Nzbaz4gF4puUTTiYP-a1CyXqT6zKYyyOp2fNqAEKIYbuqL1xRkDplb8i_H34fxi71UYxOGv-J8TfSTIMK0UEwIyxncu9sqa3BaYsW11fiX0W7BkAIHAcHRFcvFTtTDPhgtPJxqKpmmAh2gVOwVnluF26NtWQBx7HLtkbm4EWqN5RJUldPU9Sa1w4Q1SHlKLgOfmEkIjh338c51u1Zw9xotTWrjOzDNV7TgO1tCNozeevDD0xAegzRJflAXlhLxPzw1jVQ6C7-ITLEO_nwg-G3tZq3lwK6goXri8jO3r3ohCQnub71EVPL6gu1ZoftRonYzZ9NfC4zTCSlUt3U6AWzVNbSz1IgItggoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من واقعاً دوست دارم این مسیر نتیجه بدهد؛ چون جان افراد زیادی را نجات می‌دهد و از ویرانی و نابودی گسترده جلوگیری می‌کند. صادقانه بگویم، اگر آن اتفاق می‌افتاد، سال‌های بسیار طولانی طول می‌کشید تا بتوانند خسارت‌ها را جبران کنند؛ اگر اصلاً امکان بازسازی وجود داشته باشد. حتی فکر نمی‌کنم بتوانند دوباره آن را بسازند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20383" target="_blank">📅 02:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صدای انفجار جدید همین الان در تنگه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20382" target="_blank">📅 01:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtsODPuFibJ9jaTxBg1uPJiLxrGBiE4iTFYZgt9bcOgBbnSFaYpTkp-p6ajdIqHLbb0pGZtDIOOykxLvIdI4kGdbAqEs_y-1II8p3oHuFJUp2k5CImGIadqMrtsxi9aJTBqelCzHr2ooHsuD-MCaDl-T_MqKOBnFtjUrBSrpO7hRH8Nh-NuGfuUHEQsOrq-2k4nXzaC-sg1QTWl1tf1HdcRFL-Q8BrCgLfxyUEkIffdoALw5bhlmz2imabMbzQGDaRuorr3Bc6YBt0NsDKYbMUyggYNctGaT3xyS3hF87d9M8A8K7qo6dif9qF6qY2VZJmtvejQ3F5FvNjtPIrMaoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20381" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سازمان دریایی بریتانیا: گزارشی دریافت کردیم مبنی بر وقوع حادثه‌ای دریایی در فاصله 20 مایلی شمال شرقی شهر خصب در عمان.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20380" target="_blank">📅 01:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ درباره ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست. آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20379" target="_blank">📅 01:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرنگار : شما نمی‌دانید این حملات به کجا منتهی می‌شود. منظورم این است که آیا همسایگان ایران با سیل جمعیتی که به کشورهایشان سرازیر می‌شوند، مواجه خواهند شد؟
ترامپ : یک فاجعه. اتفاقات بد زیادی ممکن است رخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20378" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ در مورد ایران دم توالت:
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20377" target="_blank">📅 01:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: ببینیم که آیا می‌توانیم به توافقی برای خلع سلاح هسته‌ای ایران برسیم یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20376" target="_blank">📅 01:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ دم توالت:
در حال صحبت با ایرانیم و قراره از فردا بعدازظهر گفت‌وگوهای اصلی شروع بشه.
امیدواریم این مذاکرات بتونه جلوی کشته شدن آدم‌های بیشتری رو بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20375" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایگان آنها هم همین را گفتند. ما فقط فعلا می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20374" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرنگار: گزارشی وجود دارد که نشان می‌دهد شما در حال عقب‌نشینی نیروهای آمریکایی از کویت و بحرین هستید.
ترامپ: تمایلی به اظهار نظر در این مورد ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20373" target="_blank">📅 01:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خبرنگار: آیا ایران برای رسیدن به توافق، ضرب‌الاجلی تعیین کرده است؟
ترامپ: خواهیم دید. من قصد ندارم به کسی آسیب برسانم.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20372" target="_blank">📅 01:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ درباره ایران دم توالت هواپیما:
گروهی از افراد هستند که امیدوارند من این کار را انجام دهم - به عبارت دیگر، بمباران کنم - و گروه دیگری از افراد هستند که نمی‌خواهند من این کار را انجام دهم.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20371" target="_blank">📅 01:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس  https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==  کارای اداری و اد استوری رو انجام بدید کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20369" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KU-6N0RbzXnFUgZqPmSniqv5Ua8WinrA6MDSWHk-RDqWd0_BJbMxTYcqFngYpynmynfcEiyGsmZZKhQos1BIcRV8TA3JgPlBoqtgwUfv83Gr11zsFz1XeGzFSZBNIYLIQwQpW_rzgFT-hgsr2DUvLSBxZ461TkaV53peSBoENOrcVIvJqxfCJlihTEdOoTQgYdzLJEZgNhuM7yqNKTE_aGWFdSGZW9p_6dai2hIMZASgTFMZnFw4jhSoOASR_IHXqEzxpMy8207TLeqYaf9tFbdEXzMFhFj5qkixd4bzEe8mYor2bl2J06Ykuju2g0SZv8hE4aa2V6z8_3WzMCq1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ستاره شناس
https://www.instagram.com/reel/DbjVq_yxDKO/?igsh=MXgybDB5dGZ1cGVqZA==
کارای اداری و اد استوری رو انجام بدید
کامنت کنید کی میزنه</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20368" target="_blank">📅 00:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تنگه صدا میاد
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20367" target="_blank">📅 23:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">استوری ۱۸ بهمن ۱۴۰۴ اتاق جنگ با یاشار
۲۱ روز قبل از جنگ ۴۰ روزه !!!
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20366" target="_blank">📅 23:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانال ۱۲ عبری : مقامات اسرائیلی تخمین می‌زنند که ترامپ دوباره موضع خود در قبال ایران را تغییر می دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20365" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منابع اسرائیلی به i24NEWS گفتند: «حمله نظامی آمریکا به ایران هنوز روی میز است و لغو نشده»
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20364" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مقام آمریکایی به تایمز اسرائیل: قرار بود اسرائیل بخشی از حمله به ایران باشد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20363" target="_blank">📅 22:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تیپ ۳۲۸ مریوان : ساعت ۳ بامداد امروز، گروه کورد پژاک با دو فروند ریزپرنده انتحاری و شلیک راکت آرپی‌جی به یکی از مقرهای ارتش در مرز حمله کرد
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20362" target="_blank">📅 22:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال ۱۴ : انفجاری در اردوگاه تایجی نیروهای آمریکایی-ناتو در نزدیکی بغداد رخ داده است. این انفجار احتمالاً ناشی از افزایش سریع دمای تابستان و انفجار مهمات ذخیره شده بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20361" target="_blank">📅 21:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۲ عبری از قول منابعی در دستگاه امنیتی درباره لغو حمله آمریکا به ایران: "ما برای چند ساعت در یک وضعیت واقعی از عدم قطعیت قرار داشتیم. رئیس‌جمهور ترامپ ما را در ابهام نگه داشت. حس ما این بود که ما را نادیده گرفته‌اند."
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20360" target="_blank">📅 21:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کان، شبکه خبری عبری:
مقامات اسرائیلی از نارضایتی خود ابراز کردند، چرا که دونالد ترامپ، رئیس‌جمهور آمریکا، برای بار دوم در یک هفته، یک عملیات نظامی برنامه‌ریزی‌شده علیه ایران را لغو کرد. آن‌ها اشاره کردند که این عقب‌نشینی‌های ناگهانی، برنامه‌ریزی‌های نظامی را تضعیف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20359" target="_blank">📅 21:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saxKzv9_GdX2rTDYWzkcDYSsR8vyujvPOOf5wMmF3C9XxEkK2nstn4ktr03TEep4sxMPAVaccrUrspN8JIZun9fZuFTYIpd9G1czT-0bA2XV6NcqArkxM3TQIYlYFP5tXFUBwNqvyQQe0ZQ0GM-4VxrwVnzsmJEEiwXe8qRmhmfeQEKuode30kX7RGPUQQjLBZjDhG-gVBA5HI2zbhtzszzUoPBToXOeDSEQKy2JGDsUjLLmvURIhsgQgCjIiRy84qz91-N8uBWqRSgbNbZ4t2PreY9NXEL-hfzlMzkfZGP7kKjTc39llRlwlvsJvDYevSCxjT3qp6iLTpeGa46LlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره Sentinel-2 نشان میدهد ناو هواپیمابر آمریکای لینکلن یا بوش به 200 کیلومتری چابهار رسیده و این فاصله همچنان در حال کم شدن است....
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20358" target="_blank">📅 20:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfXmKUxGCjDDlYG-iNL6tndS5eHqHlyLDOO7IVz4uvWGUTUq8-AbP9l4uGoawtPjmTxOZHdhrMcAS276GnHbz72dv3UQRc0HZYA9TKQ-uRn9Apv9bykuJCYtYwkkc9gdf_WNKbO40oFvuTaP8hEIl5NA8CQxJOohcSK6Pobpu4XGCHgg29-gZeLLuyFg71xe-9XOl2adpCYEmPra6f86IuHzjRy3LvMT3Hc5oaQoUFCfYtZxkJ42faSJSqvJs6W9zV5FPrdWesJcb0N0bOA0xRZVgV8vMGjGIYdN4ecwNtNrCKYWQ5mKhfDPmedWwUI5wTBIL5Ni8tw2mTtKVPAPFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش در تنگه هرمز مورد اصابت موشک قرار گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20357" target="_blank">📅 20:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش پرتاب موشک از باغین کرمان @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20356" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKwDQs90u1TRh-0XBQphlDwOyuw5pn_vkAvU0D7AgNj-9Uvm2zyE4gz-jrSzZqVYWlGL9l3Pg4_SB9jQAT0lNk-H0k_H2M0vpRIigRTSgBBY2dpyyjD4SZ_DDa6QwPw2F-QGV0IsdHj_WpuGKGIpsd-QaaEd7B0MCrF9QK52Zo0GEJxtnW9ZjgrlFzjFrzz5245GBFDSYblm3BsYufjF0REBX87Poc1WSwTpgkpzYzJ_hRjg40BtX8UEEmQ8lG4DBoDZA-jvJQV68KFg15rlTX78uCNZPRtqm1N2n6ZqcYnlYv_0aTgeAMy5MM6Mlt5BdICMPCQRNpTFsq1RDZ_cXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbUA1Ng27SB8V1gKU9zCkgJNJzYyKGjS2WdH5wLJ7LzXMqmCQv7oo63btBnSJBxy2UGkx0tjIzpyoNsdqDrbE23f3T5WFpLQb0HK1fC9I3dhjhsk6lFrgbfzg7s1ztjXjfw0eOz7pT70pUBkASGt2dJjuBtNr9G_S05al4zz4Mrq8uBxK3GOY98iXCIMqiOXKG76xphIyuXpi6vw95hHnYI9MQj1H9PReAeWIWRVG2gtmHDA7zEAw9MLfXvqYBrD-06ObOwvoyihUeD74dZ6NnigoIjzXPYA_I_0lWLo2BZa9ORPEAo6gUs6iRtXIsEf9624pIzaXuB3_LdBkNqmgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جابجایی راکت انداز گراد در حوالی اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20354" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وال استریت ژورنال: ترامپ اگر فورا پیشرفتی در مذاکرات و توافق نبینه، میتونه هر لحظه عملیات علیه ایران رو آغاز کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20353" target="_blank">📅 19:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش پرتاب موشک از باغین کرمان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20352" target="_blank">📅 19:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92517c853f.mp4?token=KqkHhiLSKDfb7W0iN0LrXSXDnE5qHpc2WD5K5l4g2JQ-LMiGR1IU3u4c5Cvcb0EyhfANT2LsISdplMnhJqPvKkgE0Zw5RHkx9DNYnU5ZLcAyV-ibCkFi88lJNc49UsJdK7cQ6DdBqDQr4SHsCoMJ7M64P9NsUUA_NcZOqrCa94KGAMp2a26w58j1qjw6bF2RuiQnm3G8hoRvc4dFFGPIfoCSRrDefz7UOHSGlnlkagmfTu06wME9lO7Quyz3G47ZyshhWE4efALRwNilioxyK3mR-ZNtW6wvCOeWEm18g4Oygxvj5p9i0EOpejHo0bUmTWEUqdVZ7C15vYm9vzgXAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92517c853f.mp4?token=KqkHhiLSKDfb7W0iN0LrXSXDnE5qHpc2WD5K5l4g2JQ-LMiGR1IU3u4c5Cvcb0EyhfANT2LsISdplMnhJqPvKkgE0Zw5RHkx9DNYnU5ZLcAyV-ibCkFi88lJNc49UsJdK7cQ6DdBqDQr4SHsCoMJ7M64P9NsUUA_NcZOqrCa94KGAMp2a26w58j1qjw6bF2RuiQnm3G8hoRvc4dFFGPIfoCSRrDefz7UOHSGlnlkagmfTu06wME9lO7Quyz3G47ZyshhWE4efALRwNilioxyK3mR-ZNtW6wvCOeWEm18g4Oygxvj5p9i0EOpejHo0bUmTWEUqdVZ7C15vYm9vzgXAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : یک جت جنگنده رادارگریز F-35C متعلق به نیروی دریایی ایالات متحده، از ناو هواپیمابر آبراهام لینکلن (CVN 72) در حالی که این ناو هواپیمابر از دریای عرب عبور می‌کند و از محاصره ایالات متحده علیه ایران پشتیبانی می‌کند، به پرواز درآمد. تا تاریخ ۲ آگوست، سنتکام ۳۵ کشتی تجاری را تغییر مسیر داده، ۲ کشتی را از کار انداخته و ۲ کشتی دیگر را توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20351" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏وال استریت جورنال: یک مقام ارشد خلیج فارس گفت که برخی از کشورهایمان بر ترامپ فشار وارد می‌کنند تا اقدامات بیشتری علیه ایران انجام دهد. این مقام افزود که ایران تا زمانی که ایالات متحده اقدامات تهاجمی انجام ندهد، مانند کنترل تنگه هرمز و بررسی عملیات زمینی، کوتاه نخواهد آمد.‏
کشورهای خلیج فارس از فقدان یک استراتژی مشخص از سوی ایالات متحده ابراز نارضایتی کرده‌اند. به همین دلیل، متحدان خلیجی خواستار موشک‌های پدافندی بیشتر و تضمین‌هایی از سوی ایالات متحده برای محافظت از کشورهای خلیج فارس در صورت ادامه درگیری‌ها شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20350" target="_blank">📅 18:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۲ : مقامات اسرائیل خودشونم از پست تروث سوشال پرزیدنت ترامپ متوجه لغو عملیات شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20349" target="_blank">📅 18:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20348">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رسانه
Axios
در تحلیلی می‌نویسد ترامپ نگران از دست رفتن احتمالی اکثریت جمهوری‌خواهان در انتخابات میان‌دوره‌ای نیست، زیرا معتقد است نفوذش بر حزب جمهوری‌خواه حفظ خواهد شد. این گزارش پیش‌بینی می‌کند ترامپ در دو سال پایانی ریاست‌جمهوری نقش تعیین‌کننده‌ای در انتخابات ۲۰۲۸، هدایت حزب و استفاده از اختیارات ریاست‌جمهوری، از جمله عفو نزدیکانش، خواهد داشت و احتمال تقابل جدی با کنگره بر سر اختیارات نظارتی نیز افزایش می‌یابد
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20348" target="_blank">📅 18:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فقط خدا رو ببین
🙌🏾
🤣</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20346" target="_blank">📅 17:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شستشوی مغزی Brainwash چگونه انجام میشود بدون آنکه متوجه باشید
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20345" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">میدل ایست نیوز: دقایقی پیش اسرائیل با استفاده از پهپاد چند حمله به بلندی‌های‌ علی الطاهر در جنوب لبنان انجام داد.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20344" target="_blank">📅 17:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیویورک پست : انقلاب در ایران ممکن است «هر لحظه» رخ دهد؛ رهبران اعتراضات در تلاش برای مسلح شدن هستند!
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20343" target="_blank">📅 16:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صدای انفجار در‌ پارچین کنترل شده است و اعلام شده بود
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20342" target="_blank">📅 15:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlejandro Sosa</strong></div>
<div class="tg-text">هی میت ، داداش یاشار گلم چطوری من نگاهی به چنل های ۶۰۰-۷۰۰کی حتی ندارم رفتم بالای ده تا چنل میلیونی رو هم چک کردم، نه به اندازه شما ویو دارن نه مطلب و تحلیل مفید ، همشون فیکن!!! فقط یک خواهش دارم به عنوان برادرت در غربت… حرف آدمهای آشغال رو گوش نکن، همینطور برو جلو و همه رو به یک چشم نبین ما تا آخر با شما هستیم یادت نره تبلیغات منفی بهترین تبلیغاته برای شماست چون میان و حقیقت رو میبینند</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20341" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تتر : ۱۹۵،۶۰۰ رکورد جدید تاریخی @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20340" target="_blank">📅 15:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آژیر خطر  حمله موشکی پهپادی در اردن به صدا در آمد
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20339" target="_blank">📅 15:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فقط همین کامنت را لایک کنید و با نگهداشتن روی آن، اد تو استوری و کارهای اداری دیگر را انجام دهید.
https://www.instagram.com/p/DbiPnCyMgQw/?carousel_share_child_media_id=3954792076531598384_1638317016&comment_id=18015084023866564
ترجمه کامنتم برای بیبی نتانیاهو :
آقای نخست‌وزیر، بی‌بی عزیزِ جانم،
این رژیم فراتر از اصلاح‌پذیری است؛ شما این را بهتر از هر کسی می‌دانید. هرگونه معامله با آن، فقط خون کسانی را که کشته شدند می‌شوید و آینده نسل جوان ایران را قربانی می‌کند. یک عملیات سریع، قدرتمند، غافلگیرکننده و از هر جهت می‌توانست به این موضوع پایان دهد. اگر اقدام قاطع در ۴۰ روز اول انجام می‌شد، رژیم می‌توانست ظرف دو هفته سقوط کند؛ آنها در حال فرار بودند. لطفاً رهبری این کار را خودتان بر عهده بگیرید. شما این واقعیت را بهتر از هر کسی می‌دانید.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20338" target="_blank">📅 14:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رژیم ایران ایلان ماسک را به فهرست اهداف خود اضافه کرده و ادعا می‌کند اطلاعاتی به دست آورده که ثابت می‌کند سیستم‌های پیشرفته ردیابی ماهواره‌ای و شبکه‌های ارتباطی رمزگذاری شده ماسک مستقیماً توسط نیروهای اسرائیلی برای یافتن و از بین بردن آیت‌الله علی خامنه‌ای، رهبر سابق ایران، در جریان حملات هوایی دقیق اوایل امسال مورد استفاده قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20337" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال 12: تا زمان خلع سلاح حماس، اسرائیل حملات خود به غزه را متوقف نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20336" target="_blank">📅 13:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20335">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه،با تکذیب خبر بازگشایی تنگه به نقل از منبع آگاه، در واکنش به گزارش کانال ۱۲ اسرائیل درباره موافقت عباس عراقچی، وزیر امور خارجه، با طرح بازگشایی تنگه هرمز، نوشت: «هیچ توافقی درباره بازگشایی تنگه هرمز وجود ندارد و اخبار منتشرشده در این باره کذب است.»
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20335" target="_blank">📅 13:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رسانه های رژیم : سرلشگر غلامرضا رضاییان رئیس سازمان اطلاعات فراجا ملقب به «ابوسجاد» به جای سردار رادان فرمانده کل انتظامی در جلسه شورای دفاع نهم اسفندماه شرکت کرد و کشته شد
@WarRoom</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20334" target="_blank">📅 12:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20333">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تتر ۱۸۹،۰۰۰ تومان و همینجور داره میاد  پایین
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20333" target="_blank">📅 11:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">میدل ایست آی:ترامپ از اسرائیل خواسته به حملات علیه ایران بپیونده و یه لایه دیگه از فرماندهان و رهبران ایران رو هدف قرار بده
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20331" target="_blank">📅 11:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20330" target="_blank">📅 11:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20329">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20329" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سرپرست وزارت دفاع ایران: اظهارات آمریکایی‌ها بخشی از یک جنگ روانی است و ما به هر تهدیدی به عنوان یک تهدید واقعی نگاه می‌کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20328" target="_blank">📅 11:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خبر ها رو نگاه نکنید ! حمله ناگهانی خواهد بود !  خواهید دید</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20327" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20326">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">همشهری: از مجتبی خامنه ای هیچ صدایی منتشر نمیشه؛ چون آمریکا و اسرائیل از روی صدا هم همه چی رو میفهمن و جاشو پیدا میکنن حتی اگر فیلتر استفاده کند، آنها با معکوس کردن آن، از صدا الگوی تنفس و استرس او را متوجه میشوند. فقط ۲ یا ۳ نفر با مجتبی خامنه ای ارتباط دارن. اون احتمالا توی کوه های قم یا تهران مخفی شده.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20326" target="_blank">📅 11:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">در همین لحظه پل هوایی سنگین جهانی ، از آمریکا تا خاورمیانه.، شش سوخترسان که حتما هواپیماهای جنگنده جدیدی را از آمریکا به منطقه می آورند و همکنون در حال ورود به آسمان آتلانتیک شمالی هستند. همینطور هواپیماهای لاجستیکی سی-17 در سرتاسر این مسیر دیده میشود. @WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20325" target="_blank">📅 11:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال ۱۲ اسرائیلی: وزیر امور خارجه ایران شب گذشته با یک توافق میانی بین قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد. بر اساس این پیشنهاد، کشتی‌هایی که به سمت کشورهای خلیج فارس حرکت می‌کنند، از آب‌های منطقه‌ای ایران عبور خواهند کرد و از طریق آب‌های عمانی…</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20324" target="_blank">📅 10:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال ۱۲ اسرائیلی: وزیر امور خارجه ایران شب گذشته با یک توافق میانی بین قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد.
بر اساس این پیشنهاد، کشتی‌هایی که به سمت کشورهای خلیج فارس حرکت می‌کنند، از آب‌های منطقه‌ای ایران عبور خواهند کرد و از طریق آب‌های عمانی خارج می‌شوند. با این حال، عمان درخواست کرده است که تأییدیه رسمی دریافت کند مبنی بر اینکه سپاه پاسداران انقلاب اسلامی ایران از این توافق حمایت می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20323" target="_blank">📅 10:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00731102ad.mp4?token=WhHbwKN0OlN1B8xrndkiKgbxF_glgGS1fqtwnIP8nGDHFL231zocza9kPmxHwA93mh-iTChCVlFD845Sh-bZBfV8f0Bdx1ICzLBALbDrZ_q9fd3z4z7gXGcQ3D_FutIktyn4RuVDdj1eErQue5cNTKYmeBcdT-ej9urwCNuGRdhK1HAK-3m2HBJMIjVITZ8pjzyyU4ZhOTAUQTFpaf7iB02a8eWtkV-SQy2nSHgJwN4CEzKRSy9S-H7qCy6nYzWmBc9TEDsrF6Ulr48cK9F0d5HpvxFloWZcq7gsFbRwbjWZ8lnn8ysHRCt9RiJuw2Mir1ieSvT9xq_mDg62EdIf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00731102ad.mp4?token=WhHbwKN0OlN1B8xrndkiKgbxF_glgGS1fqtwnIP8nGDHFL231zocza9kPmxHwA93mh-iTChCVlFD845Sh-bZBfV8f0Bdx1ICzLBALbDrZ_q9fd3z4z7gXGcQ3D_FutIktyn4RuVDdj1eErQue5cNTKYmeBcdT-ej9urwCNuGRdhK1HAK-3m2HBJMIjVITZ8pjzyyU4ZhOTAUQTFpaf7iB02a8eWtkV-SQy2nSHgJwN4CEzKRSy9S-H7qCy6nYzWmBc9TEDsrF6Ulr48cK9F0d5HpvxFloWZcq7gsFbRwbjWZ8lnn8ysHRCt9RiJuw2Mir1ieSvT9xq_mDg62EdIf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو وزیر امور خارجه : حکومت ایران باید تغییر کند؛ ممکن است سرنگونی رخ ندهد، اما خود حکومت باید تغییر کند؛ آنها می‌خواهند انقلاب را صادر کنند؛ این موضوع حتماً باید تغییر کند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20322" target="_blank">📅 10:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20321">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری NBC به نقل از مقام‌های آمریکایی گزارش داده که روسیه اطلاعات شنود الکترونیکی و (SIGINT) داده‌های هدف‌یابی شامل محل استقرار، مسیر حرکت و الگوی فعالیت ناوها، هواپیماها و سامانه‌های پدافندی آمریکا در خاورمیانه را در اختیار ایران قرار می‌دهد، این همکاری توان سپاه پاسداران برای رصد نیروهای آمریکایی را افزایش داده و دقت موشک‌های بالستیک و پهپادهای انتحاری ایران را بهبود می‌بخشد، مقام‌های آمریکایی این اقدام را بخشی از گسترش روابط نظامی تهران و مسکو می‌دانند که در آن روسیه در ازای دریافت پهپادها و فناوری تولید آنها از ایران، اطلاعات اطلاعاتی، پشتیبانی فضایی و تجربه مقابله با جنگ الکترونیک غرب را به ایران منتقل می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20321" target="_blank">📅 10:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روزنامه وابسته به رژیم ایران ، نیویورک تایمز گزارش داد که هم‌پیمانان آمریکا نسبت به این موضوع که جنگ با ایران به سمت یک شکست راهبردی سوق پیدا کند نگران هستند.
هم‌پیمانان آمریکا می ترسند که ناتوانی در ایجاد تغییری پایدار در ایران، نقطه‌ ضعفی را آشکار کرده باشد که روسیه و چین از آن استقبال خواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20320" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20319">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGtYHvLYdK5D8z53mApI9QyEyMx9UU0P65uwW_MWCmTdl8ZnazHqtpiJd64GZmxbnAF2HTkmJRa8taLxP8ZhhmYQXsjec9aw03Hv_-L7PcHv0ukqktBjnD3xWrqU5dNTpwnGxXu0da-z_A1l-ujmw2zeabiYGC4WD-AOzqW_Gl_pNbTa5qEsUJul3PsgoMZK4AbImziflvv9dcR40wZggRJyCII13RLQ5hvjDlUK4jtPMnXvR0mWLY6yQWueH_31WcaeICNCb30aAZG-sk-xv1kVAKF4fkItRWlGjtjtReTDZ0vZUIgpUKSrtYsH-0tGCii3bGCyZlWQydsCfdhX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏در جریان مرحله نخست عملیات مرمت دبیرستان تاریخی انوشیروان دادگر تهران، کارشناسان میراث فرهنگی موفق به کشف و نمایان‌سازی یک کتیبه سنگی ارزشمند متعلق به سال ۱۳۲۶ خورشیدی در ایوان جنوبی این بنای تاریخی شدند.
‏این کتیبه اطلاعات ارزشمندی درباره تاریخ ساخت و افتتاح این دبیرستان، یکی از شاخص‌ترین بناهای آموزشی دوره طلایی ایران‌ساز رضا شاه پهلوی ، در خود جای داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20319" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20318">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایلان ماسک در حال نشان دادن کارخانه تسلا به بنیامین نتانیاهو، نخست وزیر اسرائیل و همسرش
@WarRoom
هم اکنون نتانیاهو به اسرائیل بازگشته است</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20318" target="_blank">📅 09:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20317">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اکسیوس : پیشینه لغو حمله ها ، که همچنین نشان می‌دهد چه کسی (عربستان) این روزها واقعاً بر ترامپ تأثیر می‌گذارد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20317" target="_blank">📅 09:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20316">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سی‌ان‌ان‌: عربستان به عنوان یک متحد کلیدی آمریکا در خلیج فارس، نفوذ قابل توجهی بر ترامپ دارد
وابستگی دیپلماتیک واشنگتن به ریاض در خاورمیانه، تأثیر زیادی بر تصمیم ترامپ برای عدم حمله به ایران داشت
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20316" target="_blank">📅 09:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20315">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqZfrhR-9LikGTNVqOvrq5FxmYU0J6jjpJEPLZzyGuVGQvfLYfjneJIaubkNSLOYAjVPa4_7K8JqccjihT8mGCfAb92XhgDOPmOjY921fZNyWx0vy2273WZjQz-YwLtFcuWuDX-NFlmmKXUyoHjH4OoTGM5auJ3qOjPcZRkhMX8m4soqgtFeNxcy_bTntc-Ua0Moe6ybVXvQp7mDow-ZNMHA1n2Vi1ngzDGXz2MofiFj9KQVWezuff_D6uIks4QqCoT3R7K8Ke9M4tLvkhANy5py2Pu6xuZDSL7NMrDSYGjRnSy_9Pf4bGZJaRycxT142AVIgtyvxsSJ1E7wv37kbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث: آمریکا مسلح و مجهز آماده حمله به جمهوری اسلامی ایرانه، با سطح وحشتناک نظامی، قدرت و زوری که از جنگ جهانی دوم به این طرف ندیدیم.
با این حال، ایران و چند تا کشور دیگه خاورمیانه ازمون خواستن حمله رو عقب بندازیم چون چارچوب یه توافق رو قبول کردن، این توافق شامل باز شدن فوری، کامل و تمام‌ و کمال تنگه هرمز میشه و تموم شدن تهدید هسته‌ای ایران.
بر اساس این درخواست، من موافقت کردم برای نفع آینده کل دنیا و همچنین بقای یه ایران موفق و آباد، حمله رو لغو کنم، به شرطی که بتونیم سریع یه معامله ببندیم. کشور اسرائیل هم تو این تعهد با من همراهه. همه دست به کار بشید و این توافق رو نهایی کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20315" target="_blank">📅 09:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فاکس نیوز:رژیم جمهوری اسلامی در واپسین نفس‌های بقا؛ در حالی که آمریکا قلب توان موشکی آن را نشانه گرفته است، سایه فروپاشی بر تهران سنگین‌تر می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20314" target="_blank">📅 09:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20313">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو : هر کسی که ما را دوست نداشته باشد، آمریکا را هم دوست ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20313" target="_blank">📅 05:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20312">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6MZ6kE7YD810nbt1g1kzjC9ukDBURXMC5Dh7p-v0zf1wpoKWxT51k5afCsuA11s6Ko3R_41MEJTgRANfGBEvOUjjP92iUhAMRr_-fRtt5w3qXt6dEf5xLuHzRKtbwgTd2DL4gKwjdSFveNGGCh5amy8T9wEwwgomSwYn3h9HF_ldUgFM3g6i7dAB1_tVKReEqD1hkAwcXul8IQbfQwYRk6jcokOrnQJIiY2acm5H-jdTvZ4ENvSEdAiM9slZDwFCkZcEiyIPplkwXfIfwbqLHBVQD1taICZV-uMaUcdBiDJRt0sGbpn2wLPaeEfIVLmlF7yDXYt6yqRRA3nwLC72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین لحظه پل هوایی سنگین جهانی ، از آمریکا تا خاورمیانه.، شش سوخترسان که حتما هواپیماهای جنگنده جدیدی را از آمریکا به منطقه می آورند و همکنون در حال ورود به آسمان آتلانتیک شمالی هستند. همینطور هواپیماهای لاجستیکی سی-17 در سرتاسر این مسیر دیده میشود.
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20312" target="_blank">📅 04:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20311">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال ۱۴ :
ایران مظنون اصلی حملات سایبری به تأسیسات آب آمریکا؛ رسانه‌ها از احتمال «پرل هاربر مجازی» خبر می‌دهند
حملات سایبری هماهنگ به تأسیسات آب‌رسانی در هفت ایالت آمریکا، نگرانی‌های جدی امنیت ملی را برانگیخته است. در این گزارش ادعا شده اگر نقش ایران به‌طور قطعی ثابت شود، این حملات فراتر از یک حمله سایبری معمولی بوده و مستلزم پاسخ قاطع آمریکا خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20311" target="_blank">📅 04:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">@WarRoom
😂
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/20310" target="_blank">📅 03:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20309">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آکسیوس: سایر قدرت‌های منطقه‌ای، از جمله پاکستان، ترکیه، امارات متحده عربی و قطر نیز بر ایالات متحده و ایران فشار وارد می‌کنند تا تنش‌ها را کاهش دهند.
واسطه‌های قطری، جلسات جداگانه‌ای با عباس عراقچی، وزیر امور خارجه ایران، استیو ویتکوف، نماینده ویژه آمریکا، و مقامات عمان برگزار کردند تا به توافقی برای بازگشایی تنگه هرمز دست یابند.
این مذاکرات پیشرفت‌هایی داشتند، اگرچه هنوز مشخص نیست که آیا این پیشرفت‌ها برای حل بحران کافی خواهد بود یا خیر.
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20309" target="_blank">📅 03:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/20308" target="_blank">📅 03:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20307">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMohsen</strong></div>
<div class="tg-text">آره یاشار تو کیش همه میگن هیچ باری دیگه از اون سمت نمیاد قراره کلا دریا تخلیه شه</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20307" target="_blank">📅 03:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20306">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مقامات آمریکایی به Axios: ولیعهد سعودی، شاهزاده محمد بن سلمان، روز شنبه با رئیس‌جمهور ترامپ صحبت کرد و نگرانی خود را در مورد برنامه‌هایش برای انجام حملات نظامی گسترده جدید علیه ایران ابراز کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20306" target="_blank">📅 03:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20305">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=NW1cOF8IC2RkJmv4MlTosIHRuFTODmBF6uv9Qkd2Rlh9ep0-maDZok7q1meeBdFaeSCH-UL-qWNWJTDV7uhtxHsZL7A8pTr4b3pSl-ApupWPpI_HbvRvTUyrfgEI5jpOzaki2CwxinD4dbpnQt_p998AXPlb1g-Jpz4MaeOOi2EN3IT7mWQYEEnUqo0qKMyq1HWVcZ_lS9RzfSq7UG-FyGD3bNPeG1zG0IK6iqIg0tvk2BNlk2j1qRkXvyFRObB8sn2LE1sCvN02Ok6MRenuZn-OdcK9jB5_g-nAalouTxyf8_Xs3au5e_84AhRmlUnzagQg8kIIyYlvclr8rYMCVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c3771c8f.mp4?token=NW1cOF8IC2RkJmv4MlTosIHRuFTODmBF6uv9Qkd2Rlh9ep0-maDZok7q1meeBdFaeSCH-UL-qWNWJTDV7uhtxHsZL7A8pTr4b3pSl-ApupWPpI_HbvRvTUyrfgEI5jpOzaki2CwxinD4dbpnQt_p998AXPlb1g-Jpz4MaeOOi2EN3IT7mWQYEEnUqo0qKMyq1HWVcZ_lS9RzfSq7UG-FyGD3bNPeG1zG0IK6iqIg0tvk2BNlk2j1qRkXvyFRObB8sn2LE1sCvN02Ok6MRenuZn-OdcK9jB5_g-nAalouTxyf8_Xs3au5e_84AhRmlUnzagQg8kIIyYlvclr8rYMCVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون فعالیت سیستم دفاع هوایی C-RAM در اربیل عراق برای مقابله با پهپاد های شلیک شده ایران
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20305" target="_blank">📅 03:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20304">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">قوانین دریایی امروز کشورهای خلیج فارس</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/20304" target="_blank">📅 03:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20303">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/20303" target="_blank">📅 03:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20302">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گویا لایو از سخنرانی قدیمی‌ بوده</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/20302" target="_blank">📅 02:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20294">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حمله پهپادی سپاه به اربیل عراق @WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20294" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
