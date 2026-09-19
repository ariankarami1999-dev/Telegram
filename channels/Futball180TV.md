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
<img src="https://cdn5.telesco.pe/file/AtBtclqpxnk9Jj6d9e8QzZgQw-PQJlCREz1-OwRiiOvCDHa-2LUGGqXei-vdfZex3Vh2cS0-OMDW-zmZUSU50UwFKw7QH4Z3gbmU_Vcd4HlIbRaGgUWUd-LBCBaEb5vws9F0Xb1kaQ5HRM5eTukJI-hXaJLlrsjij6Pting6lTd36gPLQxqjZqVPJgdDSif7LGZFzUKm_-pXZxU9jiVqE4KygDK1Wtz6ObfPk6W5oZOf1HR-eCF-o8Z__gT0aow8t8S1BgSYS40BPh-oc1trTDip2_5-nypjiWjUnPHwlgMEEXytjGkxA6Zh-gOCdzAoKxrZrF0T1Q1vX-kkePxw_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 408K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 10:56:22</div>
<hr>

<div class="tg-post" id="msg-106847">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
استادیوم آرامکو عربستان که 2 سال پیش یه زمین بایر بود حالا تبدیل به ورزشگاه لوکسی شده و در مراحل پایانی واسه افتتاح هست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/106847" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106846">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
🇮🇷
آنالیز فنی جالب تراکتور در بازی مقابل شباب الاهلی امارات که باعث شکست نکونام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/106846" target="_blank">📅 10:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106845">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=RMZgKx47_ifRSgJ5yAmzk_H3Z-kDgPQQw8SRNiq7_BVkCgL_7Wcw6i7irzSR_8uE6ywckm0kKiGltLMT70LR5ArkYakgdPvpfP_jOjQzqEkWdpli009VNoBtHgs7z7adden7CwwyfPsu9llJDnxhPayoZGJ6lZQ_X6mLnXzmVdnAaQmKSY-H96cUosgcUobaxZ3x-m242UtjJfj62Nhp4zkuQe4qBwImhoHfhW8az21iwxT9YlHNo4X8YhrbCnstPQ6LgQr3SWsrECY5fy0gOFK-J7fiblQYFAwGjm75Pl_BBnH5PGiERSA3rXOWVB91_gn4ZYbG5W9XnmaJhWM9Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=RMZgKx47_ifRSgJ5yAmzk_H3Z-kDgPQQw8SRNiq7_BVkCgL_7Wcw6i7irzSR_8uE6ywckm0kKiGltLMT70LR5ArkYakgdPvpfP_jOjQzqEkWdpli009VNoBtHgs7z7adden7CwwyfPsu9llJDnxhPayoZGJ6lZQ_X6mLnXzmVdnAaQmKSY-H96cUosgcUobaxZ3x-m242UtjJfj62Nhp4zkuQe4qBwImhoHfhW8az21iwxT9YlHNo4X8YhrbCnstPQ6LgQr3SWsrECY5fy0gOFK-J7fiblQYFAwGjm75Pl_BBnH5PGiERSA3rXOWVB91_gn4ZYbG5W9XnmaJhWM9Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
امباپه: "اگر میتونستم، کریستیانو، زیدان و رونالدو رو به رئال مادرید میاوردم. من فکر می‌کنم آدم کیفیت و مهارتش رو هیچوقت از دست نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/106845" target="_blank">📅 09:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106844">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSeg6JXpZiFUvncOx6Twn86k8NO-UuoVk9Xommj8SXqfajr7FjpJ6l2cMsSXhJRbhpireLAgixAOJ9Vq_KDwezAZwqojxX00k3GHqyaB1ZYpU6WdvX0wpNXiKB3RJyrDUkfF1EQHcad8yCO_TrFg5x3AbqmYLLhyktWSnabTRl85cL-OQ3Z-9B_z-qvwSv9y3yWlXhSfYTf-2Zjq3AspXNrBcwU2i-yuWa6-HUthg5pbvTvu49E7ft8RS9BRsFyEHE6U7YtmlXcL0KT2giyYU9SN4vvagaIcceLDvmGcuj24PCrqBwbI2Ynt8U79w3J6frUSFkviA-aykZ1RVSZnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
از عجایب مملکت؛ یک‌نیسان آبی با ۹۵۲ میلیون تومان خلافی بالاخره توقیف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/106844" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106843">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=HsJv1nXhjlIos5fzeA2crMFH7QOYHtOSd8aZYCeo51ZgjE0q17aXKHrF3AhNGeWsQEA3HM_20LIOee9VMbvZCkWblU6EDNUjzMuOKjn7oUM0nw7XPfUwccT81mBgZgKnBM6HmNHqJI697JvDiRZlSy0ZvEWx4I1n6FQKlwKvhMNcUCLlfvRmpHznxQNxm8UKs3KxllAyVhmU1_aJqiOgv5tGgBlAvh9ete-dB6vkMMEUi2_NP5lTEFcQfbRMgx7xiM3wYwioD0XfCyeoVTEvp8UgHp72AVd7iv9gDbHm3RTMvLZW8dvSbhGSVEG95gbLcm1lvZmoPyaJ6CXtsMwlhrOEo0MRGo69pBdGxPvx729_Vjla3sf3C5KCticxrB5J_t3ivaWA82kt1t3sUhVtL3iZhWojvJ1n9-8KWrMmwtXn79eeV-k7ZRuEErsYgUGhkznkHD_TKO3yWeNqtYelpRiF38HaAiiLlX-YV0ZhesAuph8okXth4i2JgNocud-bEsmzh8K5_yz4Ma9P1PgypC1wuDo_rimwPRM6kJB5oyzpBHG5dg8KNdj1cCo0Jxx0RhBXQNL99ILYBm0YGcjXkCQEYSy0reg87DS9NelSozGJHUy4LvcPGPhBjOT8KWzf2AaJKw91wtQi0JqYNAskYEGpKftSl2yBOi-GilGt_xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=HsJv1nXhjlIos5fzeA2crMFH7QOYHtOSd8aZYCeo51ZgjE0q17aXKHrF3AhNGeWsQEA3HM_20LIOee9VMbvZCkWblU6EDNUjzMuOKjn7oUM0nw7XPfUwccT81mBgZgKnBM6HmNHqJI697JvDiRZlSy0ZvEWx4I1n6FQKlwKvhMNcUCLlfvRmpHznxQNxm8UKs3KxllAyVhmU1_aJqiOgv5tGgBlAvh9ete-dB6vkMMEUi2_NP5lTEFcQfbRMgx7xiM3wYwioD0XfCyeoVTEvp8UgHp72AVd7iv9gDbHm3RTMvLZW8dvSbhGSVEG95gbLcm1lvZmoPyaJ6CXtsMwlhrOEo0MRGo69pBdGxPvx729_Vjla3sf3C5KCticxrB5J_t3ivaWA82kt1t3sUhVtL3iZhWojvJ1n9-8KWrMmwtXn79eeV-k7ZRuEErsYgUGhkznkHD_TKO3yWeNqtYelpRiF38HaAiiLlX-YV0ZhesAuph8okXth4i2JgNocud-bEsmzh8K5_yz4Ma9P1PgypC1wuDo_rimwPRM6kJB5oyzpBHG5dg8KNdj1cCo0Jxx0RhBXQNL99ILYBm0YGcjXkCQEYSy0reg87DS9NelSozGJHUy4LvcPGPhBjOT8KWzf2AaJKw91wtQi0JqYNAskYEGpKftSl2yBOi-GilGt_xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پورن‌استار ایرانی که در ایام‌جنگ اخیر با دختران خوشکل و زیبای اسرائیلی رابطه خشن جنسی برقرار می‌کرد، دست به توبه به درگاه خدا زد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/106843" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106842">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5fGN2inmCjsg6fKLaRLXZFbxWjhtqDs2PeWBfCZk5dVXF-b1P5nbzL_Yon_1TgxZzPLAzvkjo-x6c2x1zIJyH29p0-1H15FMWFfjDDtje5EY12pqIMLso1I91gI25vPmmmGz3wlwmjEgZ5Jibn5PjJtAfFdoTqwxr35NyrLCchtfS04T9rnJeB2_zqUQB30vGYJ0jM20fTaXvFtWYc441KsSQ5IEBS4YZfBF1aYWgZ04WbbmrTqpHKabxLgvVB5_dFQLvq6oYNAxiauXz2uh_dfgR4szEVrrtsKi56rFHubAXyYKel5PBBsO8dBmdgVmIuGUAzp-jr3UtXm5vFvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
فیتیله بعد از ۱۱ سال پخشش رو دوباره از شبکه ماهواره‌ای Fx2، شروع کرد.
هر جمعه ساعت ۱۰ صبح.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/106842" target="_blank">📅 08:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106841">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=G6RzpKdkoB3ui7DPvDTz_RmcqSTQJjGVwtG-VJ1iartmHuqIBsgxF2qTh8oOxDCWk20FkcDfMOqWnnZppUP0tzO1JWV3Stl5q_kJdanvsRsyqKYzxilJyvACeLJ3gqz2r7C0lcNky9WbWhaMEhHjPOHPe5f4KvG8JcozK_X01NyMN4rYIhh4oj5xcHKY0ghl0oavxvuLw3BlK3bIfEZYMrmp2wp4a0l9HVox2iE5d5Y8BAAOYl51O28mP7qFDoSQtfm89pYFLgxDZCosxYRbfv7WNb5u858zH8hgtuXcINzsn4wnJiSpkQitDIuK4UAbsJzyAqmujM8LTBgBEJbqyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=G6RzpKdkoB3ui7DPvDTz_RmcqSTQJjGVwtG-VJ1iartmHuqIBsgxF2qTh8oOxDCWk20FkcDfMOqWnnZppUP0tzO1JWV3Stl5q_kJdanvsRsyqKYzxilJyvACeLJ3gqz2r7C0lcNky9WbWhaMEhHjPOHPe5f4KvG8JcozK_X01NyMN4rYIhh4oj5xcHKY0ghl0oavxvuLw3BlK3bIfEZYMrmp2wp4a0l9HVox2iE5d5Y8BAAOYl51O28mP7qFDoSQtfm89pYFLgxDZCosxYRbfv7WNb5u858zH8hgtuXcINzsn4wnJiSpkQitDIuK4UAbsJzyAqmujM8LTBgBEJbqyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پاس گل جالب دنیس درگاهی با ضربه سر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/Futball180TV/106841" target="_blank">📅 08:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106840">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106840" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106839">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/Futball180TV/106839" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106838">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106838" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106837">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRbEAC5kXoCvqpWB1qCoes0J2rN4e_HuRoDuajVwvbkUDG9AZzMdWyXuj9ond0bUnklITa_9Fyne-Ia61voi5mLDJTpo1obLwfvmXTwTfE9zvLPJRm-_Ruk0OL4bh_-eqiDJiDO1qoLH-aeHbWL5juWmlXybxuiFKnbxZ5ccaNInes5KuqyRPYe6JS4fAvS-uUhl8m2bnnGF2lb-Pj-P4lYSdtTgnfGLkc-Eoyi8sWlFS_7EOuRcYchgwUH-hjgYFRi1qUYOiusQA2vWAqu3lGx5HSnZksdJF5pYgfvI0yRFm65JkSO0Bp9_8_jn1CEddEImjgsp11YSj-PiELW7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال درباره علاقه‌اش به نیمار:
🔻
همیشه سعی کردم بازیکنی باشم که با خوشحالی بازی می‌کند، و نیمار تجسم واقعی شادی در یک فوتبالیست بود.
🔻
نیمار از آن بازیکن‌هایی بود که فقط با دیدن بازی‌اش لذت می‌بردی. نوع بازی‌اش باعث می‌شد تماشایش سرگرم‌کننده باشد.
🔻
تقریباً تمام دوران کودکی‌ام، صبح که بیدار می‌شدم یک کلیپ از دریبل‌های نیمار می‌دیدم، بعد یک کلیپ از گل‌هایش... او واقعاً بازیکن خاصی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106837" target="_blank">📅 00:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106836">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRZ52L_Vq8RJe2opxgdFiUmIhkTQRArZr641rPx58miCQzv8sEoNc5hENwYdI8ITf1H3Zll3FTKxz-dA1J6uEUAPNsNUej7cwaAxrwB7Ce2ZpDILrhfOHVfck6gB_dUOKrPYNYcwtSt0SvGADDpaN6_JiL-QXINA6xlFGd9fySaFgLkejonjkW7w19EyyTXrh_1vFYhwbW2un_n4x-6zWiwtaXLRO8P1RuGirBeCKALmEDde-nxoBqboJftlIySbyBZJ-xEPNNaclYyBiVnHc6Rl5e_1Wt-sz9zMpQ7G_Ty7CTr1SiO1rvDibxl3-ez_d4ljhdNfOrUba9jsEYzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
يحیی‌گل‌محمدی و تیمش دهوک در هفته هشتم لیگ‌عراق مقابل حریفشان به تساوی رسیدند. این ششمین تساوی یحیی و تیمش در لیگ‌عراق بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106836" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106835">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl9jAfSQUaWJ_lOthIyZat1gnTqg0W-5ajlbcmHtD-fopakMPrUWaQAo6i16o2BYjs9dlIVEPCTKdAv8o7BKCNab7D15QRWeo8eGNGc2AkG5ANIpNHwzCxXKojzC_F41sebKiPQhSt4zZz1r_c7EYofQ03UOO34D1LWOsYltWWIdjpFNZ2whbLs38EJypP7X0H9cKrDcULdYqP2wDMbBmvKpdk9OrcODzWXdf2FtnUj9SuJHfKb1iBDa7ewY_vbW6x0MDbR2Jr54MnA7Mllw8K5RVJf8pt5xMiw2PRXJKSqqEhtA9HlKLU6nkq8hem7VPWSZMi19rehOYzjIf08W7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
‼️
لامین‌یامال: تا پارسال پاس گل و دریبل زدن را بیشتر دوست داشتم ، اما الان گل زدن از نظرم بهتره ، گل میزنی و تمام، کارت را انجام دادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106835" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106834">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=hficH2fe1yynsgjLOhfIiFVT83g9ObvFTy7Cy5lrt0w-bYcdB_q9oyzpTGcCzvn7EERZ3fo8PhDpIm63WtoCj8ShJXPa7RMPNdSEaYtR2X6ksaTzwEBdwjWmMuBhMmqDlhHrpG8SdIorXEZajCa64qrKM1v_2K3A9ikQLHnpPFCVY8RuKg5RWH3uDcd5ujLKuG-K-I-3RF_gJydwxB1IOVx9GDm8-Bg9br0NpuWYGXU_J8khwHQGcV5gPtp0R33_lmW0LKambHvFls_rqyFe3w5dfyBeDQddO6NkrZZ5DjdCTHviG-MpkviR2lVHe9MMbaGvpvyZiksFJqM7KrVs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=hficH2fe1yynsgjLOhfIiFVT83g9ObvFTy7Cy5lrt0w-bYcdB_q9oyzpTGcCzvn7EERZ3fo8PhDpIm63WtoCj8ShJXPa7RMPNdSEaYtR2X6ksaTzwEBdwjWmMuBhMmqDlhHrpG8SdIorXEZajCa64qrKM1v_2K3A9ikQLHnpPFCVY8RuKg5RWH3uDcd5ujLKuG-K-I-3RF_gJydwxB1IOVx9GDm8-Bg9br0NpuWYGXU_J8khwHQGcV5gPtp0R33_lmW0LKambHvFls_rqyFe3w5dfyBeDQddO6NkrZZ5DjdCTHviG-MpkviR2lVHe9MMbaGvpvyZiksFJqM7KrVs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمد تقوی، در برنامه هت‌تریک درباره پیروزی استقلال در برابر السد در لیگ نخبگان آسیا گفت: «استقلال نمی‌تواند در لیگ برتر مثل لیگ نخبگان بازی کند، چون نوع بازی تیم‌های ایرانی متفاوت است. دفاع منسجم استقلال اجازه نمی‌داد بازیکنان السد، به راحتی بازی کنند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106834" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106833">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=k9grUfUNanTxQ60QWbN4xQxkTORrftG57mje8nBjWhGYY1R1oz1G1Lh4ryfuETl-L4sVHuLlKNs3NxH1aiPcXVZsp_bCDPpf0QY0bn8BTDmGDLh2Ug9nca1MYlxH5rfomF0_S7zvP4fac_FhqFE6_Lmv79pc1OBZwGQUiG62D-09RQ9XXkSyHl-IOLKzCMRYghnEnuUPZEO8JT_prEk9QnEqfGZzNHHgarFs5C63wJVwhOI_xZ5tcyHqNDVrzlTOQ81bTsjqKRirxV_Us40grO5fDJ6OLW-Mfhr4o3HnFOa0E5mYpXeaRaQTQE7uWDbQonvVA48EyIiha4uXPqgxog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
گل‌های دیدار بایرن مونیخ - بوینیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106833" target="_blank">📅 00:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106832">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇪
سوپرگل دیدنی اولیسه مقابل یونیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106832" target="_blank">📅 22:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106831">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz0U6vJTtl_PxTpZRlGLnDCxwq9kXkOKFDbEaZd_2MDM3rfU4HYHn4tQUGPRZiXmPzune2l_82aK3amz4uKXoYZ-btqWkOO_DGZ7EVQW4KaL19R2KPnghzOZNaFazgcTHed1QGzzZasinpaARgIVpKsh1SMbPJbjAB120rp8CWCDsrg4fC38Ux_ym7h5QDmwCwzEuD-j4lh5MgzTdy_YyPSmJxfWmZgPuNMv8-WYVjc_jToI3RGE8YaJUwNKUW_SqlSI1xY_cGtPMNrafMdcF2hdqgvEKlDbQJlnWfIZXt9n_JiPXk_qbpe0CcgbdCut-u8nxmeDpLoYtVPIEG3L7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
🇪🇸
پس از دو بازی غیبت بدلیل مصدومیت، آلوارز به دیدار یکشنبه مقابل رئال‌مادرید رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106831" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106830">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfXfqBC2VOB4ly3KOyK1tcqboRZUKk_KvUmrf71dpMXVZKNUH3_wVMHGDji_k69_uEtImvKIs77jNCBmR60Pthpb-QSZaK4bk4ZfsDavFJVYCdtdVAmAtUItEfiuYT4MU74gsw4at-eQiynuW732eGPoZnh5SHNZcIxvNKTHddKF8Ih6Pp_34Mk6unUun4HmsfRJz4tVqF1SFdlMQDXLAehQ287VrGm7Ad-gULpYTA3hekBjaWDA6zakkUcCMgThTWrAfMLYIA3NxdTd2BxCN8Gibiegl1zS8nE28M4qnBapZIAKsb-4BuBvTwX5igP_aa36HHPI1ON8FmsUDSq3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
داکنز نازون پس از عدم موفقیت در بازگشت به استقلال، راهی النصر لیبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106830" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106829">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=f5Z499pxEHCzIb-VL9PqEW72MFlbCtauo71Gmoe481J7J_6-4C66JxbmDLa27D7QXREtWTzATJw92IbXqjk9iuJDKNTf0yn1A9n9e-YA0YxIT9rVYXc-d5bgQjKpPQodH4asM5AMpz9WfPdwK7lR5E36ZGYjL5ECtPScLICJSN0VuaAPtWtnQ7vlNAsHTru5Z2zYocGWE809dC_9RQng_-1MExxIXhNwLqvKk66r0mnZ2sYUaNbw06EMBh0LGESjgwxiGgCfz0WXkSEacm7rA3-g0_5pGieMcKmOSgCasyW-ZOzj02HY1P9L-GCEuo4U8_YZbG94N_pWlU8d1T85Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف‌فروش آیفون ۱۸ در اولین روز فروش رسمی‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106829" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106827">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdZBu29iEzGAe1jVv0VT7c14cOSSvtlZpFFQQw7JDYoFryNovBTyE50NyxLxVQUW6Bcu8rFg99lC-jcHRDhnemBjgqEHlCcgsn5wWr-ZBmI8CEfplZ6FQse6MLQPNFwPKTI0QwLKQ7UOUMW-DhX67M21AnX4kzLY2YZMqctni23nSQiYEXwwqElu5tZYlwYJ1vpOsKgeaimwY2WosNliIrA71Q4A9QtGjy5uFmf3xcM2jgXEeGVlNlaEN2PdMBNgduXTdOtxjeL5boR503qfDNX2Aej6V23O9t80lJ1LPkf43F2W2Dakn6w5OobUpLAvQP0F2qWB3OKfQClGSl8ufA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/etq-oAnmSrRsazwCpqD6EjWyCGg3tIcWgXyZYkeNnYguAeNE0AJyrj4Zg4cUEEx4QVPkmOwvlSeXFzK3LvuF6I2FMjoz1DJjN4zNVpPlbOxMgNKIzPZQ9dhjO649GDUco4xxyXttISWteHmGMFUCXRaq_3nygtcqcdPNEFXBNyGDfIIkwwzkBCf_1-bba-G3zgD-hFKQuVKgrIbdXLakW-qx0P-khIMlXNTy6ZqgS6_JIh0XpYc_gj-7cl3ZJpVLpjcx8dDhZK0XdkCubMBONa7oXFp0Ahc1e2HsJd2FBZ6qvPjna0ewiq0njPAmDqnx7QsrDjo51c1otsaG2mWasw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🗓
سه سال پیش در چنین روزی
رونالدو برای اولین و آخرین بار اومد ایران و دوتا بازی بعدی النصر تو ایران رو پیچوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106827" target="_blank">📅 21:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106826">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNpL2an3seBKGgsa8SHASLrvYQcWxtMdqIRrq65DeoVLBsjrnrR05B4lAkkwjFlJyYk-9TuAvhXN2qbit8L8vmR3UUGgdllC3Y3szrVePTd4E8zarmAogGbCx1HrhMKlLrmAFUtCLqrDWDN9fDfSPFOPF91aE6XHT1_8kwIVugOcGc4fxuWqvlpntfPJg4F9ePK3im6fDQWwOrDkGunsL-F9PxJabPMyaTP1wfVsr9UcwQ_EdoTV4BuzQowofhIbXmabjme_zKvM7m2ddaX5zMcpjtNsB93ms72Emn5tWefpjbzdVy8nXJDNxvYryUzvozhIIJfrWQtDGevgH23EDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌ مونیخ مقابل یونیون برلین | هفته 4 بوندسلیگا 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106826" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106825">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9ikpv3GROMz4yfNRH5_MM65NSqIAtwJk4HP2bEE4hgX8Ti0zki8RQrFBAddSyQJntQYJ-E3GcPnuR2Nxnb3hSNB0bJ4zgQDPuNLNQmogGgZwcdugTUeXjOy2bjuATnB1Kio20sXN0HTDKUBm1Ele0L3m1JfIQGlEqs6nKFtELEsSqjDLQJOJOck1PL1O1eVi2JPCsAbhak_75ZJ_2tOwYnQ1m9fQ3i2HgqWXIeObAdbXRBVXGSeUt0Lr2VMLaFT5qozOehtbUPfx5JIwI5blbWEecZBQ6UZ5fgROwhUBvjMknmxC760yAV1cxwkph5V2FRMEWh810sTx543vINY7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇹
لیست تیم‌ملی ایتالیا برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106825" target="_blank">📅 20:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106824">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=E6u1l4oRfsomWIKClWkLw2SBDRGoC2W-u0MXLkVFdxTvzbnNdAH3WLVmWReF9ZdoOQYkaQxKT-TBXIswn-SWC8gHYRuHWd0Rzd7enJWgQSJMmK__63N_fVyIz0cVLbXXbpXhms0SL6wwtdxTbYnI3iZW5TK8TipOzj7iDO-hctWiXtPyBqtouhWOfgvKCJFvMuim4zgOX-IvuDoCd9e3L944FWqpBXPWNDmZ9Uryh7pl5xc6qIaeR56zYWMOFXFfzIZ-2Pu7Hsg6V_aeqyU0QGSwZ0nud-0gP_tOO-NzkeehecLlZWxEUCqB4csUcJdRiBY_Lao3V2fCudYp65S67Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=E6u1l4oRfsomWIKClWkLw2SBDRGoC2W-u0MXLkVFdxTvzbnNdAH3WLVmWReF9ZdoOQYkaQxKT-TBXIswn-SWC8gHYRuHWd0Rzd7enJWgQSJMmK__63N_fVyIz0cVLbXXbpXhms0SL6wwtdxTbYnI3iZW5TK8TipOzj7iDO-hctWiXtPyBqtouhWOfgvKCJFvMuim4zgOX-IvuDoCd9e3L944FWqpBXPWNDmZ9Uryh7pl5xc6qIaeR56zYWMOFXFfzIZ-2Pu7Hsg6V_aeqyU0QGSwZ0nud-0gP_tOO-NzkeehecLlZWxEUCqB4csUcJdRiBY_Lao3V2fCudYp65S67Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎬
👍
پدرهای عزیز به این‌دیدگاه عقاید جالب علی فروتن حتما گوش بدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106824" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106823">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=oPd6kRKwUQLPDYrfgX-ETSVffpComYCIzgZaQxYarWMo69f7ACeS2z9x1IqhG23cqpY7wW6dJFZ_7-G8hi-eVnwR3-kdyL5D5XP3L_ZpwN9Fg95tIpplXLvslvrrKVoOIWo-ezw7Ze7uRmfpZqvE7dneqwsNjcUjkJ7t7bxhF_Zuwv_fThelEoUandHsGPCh-eL_4uecJUj2QT0FkqAbiipqU49LG4VGYxHOmF3DhQXekdJ9sdR1_G-05DsaohP5iuN9afWAzDPvAizyY8ekynBNQsP_hAZSXoNv6FNeNiAbDj0JgU90ZAhMiyNNZJ_47PNiqCJefQo7EutIvO1gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=oPd6kRKwUQLPDYrfgX-ETSVffpComYCIzgZaQxYarWMo69f7ACeS2z9x1IqhG23cqpY7wW6dJFZ_7-G8hi-eVnwR3-kdyL5D5XP3L_ZpwN9Fg95tIpplXLvslvrrKVoOIWo-ezw7Ze7uRmfpZqvE7dneqwsNjcUjkJ7t7bxhF_Zuwv_fThelEoUandHsGPCh-eL_4uecJUj2QT0FkqAbiipqU49LG4VGYxHOmF3DhQXekdJ9sdR1_G-05DsaohP5iuN9afWAzDPvAizyY8ekynBNQsP_hAZSXoNv6FNeNiAbDj0JgU90ZAhMiyNNZJ_47PNiqCJefQo7EutIvO1gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106823" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106822">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC320vUAABf0IEFZa6gvCnXZuZwBvima50IbNvTjyrRRtGYve8QBMUHiYPnn-xGN5D7TuxUqpWVTWNls1HcgWMK3ou3zfxnJ0BPcfMIy-W1ahIADbYji6PWh0pupowyr6H5ZjmzUvy9agAqAH8C_1oIwsHS0psDaBM645HHxU9928Uvz1SiSJ8yCRW1DVY4cU5G_tVSRXIU2_gFo9FAUEZPAgTqqdnrBvDn51o_MK1urof-6h8jpRAwVUfUU_SGgehe_bxlRPmINxwWNFK39Nv871lW49XrQQJclsBHyqDZpIjDtjXxv3m3VUigaRBLlWMAvIqV0QSSS8PwxKryHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست تیم‌ملی فرانسه برای فیفادی در اولین حضور زیدان روی نیمکت سرمربیگری خروس‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106822" target="_blank">📅 19:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106821">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69347998c.mp4?token=imf3oRM2XKfR3cRGJf1x650hldwlpTgjDz8HCfTtOBLKdKlzDogU4uMBMlKpGnhId_dh_2lde310UVR4epoHmm4WrM0u__LkLzJhftv_Gn6xzsBJ1rqahxQ_apMieoq7OXP9jwWJCXhHubaHZap7qhYDtlasZfD-Bnh4vLL8J72JHyWgbXpX9IHDQeo1pULcX4Smp-xh9d3NE5tdX8hueIjcofMXUIFM9cTIRA4bJFB3XV5llFIDYCunTEnyXQ__TaetUIVOcbxaadF9q2j0lrdkxjaWWMpHVubjymTNFn3h1g3ARtRIb6ygIhf-_wtkZ8X-7PCfGof9MjtqjO06rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69347998c.mp4?token=imf3oRM2XKfR3cRGJf1x650hldwlpTgjDz8HCfTtOBLKdKlzDogU4uMBMlKpGnhId_dh_2lde310UVR4epoHmm4WrM0u__LkLzJhftv_Gn6xzsBJ1rqahxQ_apMieoq7OXP9jwWJCXhHubaHZap7qhYDtlasZfD-Bnh4vLL8J72JHyWgbXpX9IHDQeo1pULcX4Smp-xh9d3NE5tdX8hueIjcofMXUIFM9cTIRA4bJFB3XV5llFIDYCunTEnyXQ__TaetUIVOcbxaadF9q2j0lrdkxjaWWMpHVubjymTNFn3h1g3ARtRIb6ygIhf-_wtkZ8X-7PCfGof9MjtqjO06rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد عزیزی: دچار شرم نیابتی شدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106821" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106820">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=pqhnkZ7D3e_w9buO1G5YzU_hKv80oOCOySma-pRoMT4suA4rfnxoiXN9GVR-1raIbc0bv8_XYxRi-cMTSBs_o-o7p88jF8g7LiYSYBHXBvCGbor2mQdbAElVRdZoNzecEUVukPPbUJZAIHO5252cApeqhzgr-TEYfXhh7knLrE4uOaQeyeydZbGreAqmDoxpZyt6rCa5kMgCiAbOx3dglE7AjUQC9dihRDoBq8zIkFN2b-_uQr4WnSwxooLv-OrIPgcBJz7hTa28gW8olsHxrlswNV4K5lXPcTdsBKoYV56X6lObYjdWltHgLMQdMYwymLnk5mSoaByulfzwkEyO5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=pqhnkZ7D3e_w9buO1G5YzU_hKv80oOCOySma-pRoMT4suA4rfnxoiXN9GVR-1raIbc0bv8_XYxRi-cMTSBs_o-o7p88jF8g7LiYSYBHXBvCGbor2mQdbAElVRdZoNzecEUVukPPbUJZAIHO5252cApeqhzgr-TEYfXhh7knLrE4uOaQeyeydZbGreAqmDoxpZyt6rCa5kMgCiAbOx3dglE7AjUQC9dihRDoBq8zIkFN2b-_uQr4WnSwxooLv-OrIPgcBJz7hTa28gW8olsHxrlswNV4K5lXPcTdsBKoYV56X6lObYjdWltHgLMQdMYwymLnk5mSoaByulfzwkEyO5IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
دیوید بکام: "من هنوزم باورم نمیشه که اونو اینجا تو میامی داریم و داره واسه تیممون بازی می‌کنه. همه ما دلمون می‌خواد لئو تا ابد بازی کنه. هیچ‌کس تو 39 سالگی همچین کاری رو تو این سطح انجام نمیده. پس حقشه که کاندید توپ طلا باشه. به نظر من که باید ببرتش!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106820" target="_blank">📅 19:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106819">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=MoCf2SmwBiPeQzh6VmpZ4MjyFbMIwPDqP2RROzIjvCjZFCNmtyxgaDzJfvnR7IAO7soYz9x8LFE9mctAu6NYGkhtS8ssj7fgCbKwuQdbJebtlcss0WGBPv-IT70G6f2NulMA1o-6aS8leO82GJerQUyJemIdYS-pIcRrLq7kKfT7rc4ZVlpJF-cNgh_FvPHDdzEofHFM0UjWIQ3TIyxkYbYpT4l6UksEpezFKe-__cL-znZ_DVKJTDJ2QYaqW31a4rUUs26ygG9yhU6wVDo45nQIRxaJYbsSX81AnEUMhzXqgxJ3bP4446m1gw0QkOvu76QLkfGBBtNRJnexR8b9iYNN419cmMaEvzV8_UcOrSBxDvMQRqZlhQbrz3_RpXhgiqGz5VeAAoquGmKnhwCVKFm2RH95Q1QcZGM46EVqDNQlxg9W9xUeWCnDp27f_OKi1YR6Z8wkUXPjY7B-H4grjb6bOnX5OuV2_tR6SaSrGo_TiTUOG2JYAgqYCrkqsOVn2zsOeQWhlOiHx9lLDZ3i2VyLXX8MQYhDt2lcsjgD0tf9ncirhsfj0h_mhm595GV9gyUAj3unHgFOiQQ5ZxWlKlsG_q_DWMbx8F9EbDZIP06JAmfsNqLOe7ky_3L03-BTU2-aI5FoZfunLSYif5MgAhVH1NbN1-eAobmWYLriZ4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=MoCf2SmwBiPeQzh6VmpZ4MjyFbMIwPDqP2RROzIjvCjZFCNmtyxgaDzJfvnR7IAO7soYz9x8LFE9mctAu6NYGkhtS8ssj7fgCbKwuQdbJebtlcss0WGBPv-IT70G6f2NulMA1o-6aS8leO82GJerQUyJemIdYS-pIcRrLq7kKfT7rc4ZVlpJF-cNgh_FvPHDdzEofHFM0UjWIQ3TIyxkYbYpT4l6UksEpezFKe-__cL-znZ_DVKJTDJ2QYaqW31a4rUUs26ygG9yhU6wVDo45nQIRxaJYbsSX81AnEUMhzXqgxJ3bP4446m1gw0QkOvu76QLkfGBBtNRJnexR8b9iYNN419cmMaEvzV8_UcOrSBxDvMQRqZlhQbrz3_RpXhgiqGz5VeAAoquGmKnhwCVKFm2RH95Q1QcZGM46EVqDNQlxg9W9xUeWCnDp27f_OKi1YR6Z8wkUXPjY7B-H4grjb6bOnX5OuV2_tR6SaSrGo_TiTUOG2JYAgqYCrkqsOVn2zsOeQWhlOiHx9lLDZ3i2VyLXX8MQYhDt2lcsjgD0tf9ncirhsfj0h_mhm595GV9gyUAj3unHgFOiQQ5ZxWlKlsG_q_DWMbx8F9EbDZIP06JAmfsNqLOe7ky_3L03-BTU2-aI5FoZfunLSYif5MgAhVH1NbN1-eAobmWYLriZ4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو مارسکا سرمربی سیتیزن‌ها:
🔺
تردید هوادارا پس از رفتن مربیای اسطوره‌ای طبیعیه. این شک و تردیدها برای هوادارای منچستریونایتد و آرسنال هم بعد از رفتن سر الکس و ونگر وجود داشت. برای هوادارای سیتی هم همین مسئله صادقه، چون پپ هم یه مربی معمولی نبود. اونم مثل سر الکس و ونگر، یه اسطوره بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106819" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106818">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106818" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106817">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPXR_Nme2ou5s9vM2nrxXrngCS_5xqHYozUzOOrM8XlDhUfnepNSMb2mAX2QFoTanEpmWGbuRNfDuiL1PQ73s0ZPo7MSTGsHYV4668Clstj1-DToM_7Rbq0-VMtjJsbFHDuHe-aGWlDHFFOo3RPybETFNsR-cIvAcNfLBc5ggOpNGYGqfRbkGADEuMeaXzrK-V1f8gkrP4Bp3bDQJaXmnVEo_aNM6yvbmOCQHFARwPHhKB8-NXcMITl9U_eNVARakNPtl5i8Tod5fW1n2TX5JPYNu7jvWWliOXjbxLkQM4rYHLFTGChk8Uvr0xwpEge2S394IqH0saPpO8WKjQ3ffA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106817" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106816">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=QfWpANYdI-S8H8s_lznq9NNy6OCK9BFWm1CMN2_TQZffl9Kt35bypgsjuBGgwXhf8xZ86zw0iaJI-0nKIfJflRpKlkqfLYtedfo5jHurXPgj6fYZgc4t8VKinO90yoXZPOr8voujXJHkrWQ-0JTuouPQ9Cb9UsPEmpUyV-M335oLQB1B9PpHEx88T6ZsQcbg_Mg-e58kr8TXsyR0Vc_QGsge28FL1QGW6yCuBJITkBHPx_FfmgTXw4RwkU7ujdMsS3lUbDpauTUUX8nDCNyLPoSjiNTvk4OKBhP9KDoHSC-smO7UykMt7miL-QAUG2Zxn0rifHt0VhzSbbWoPWXbyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=QfWpANYdI-S8H8s_lznq9NNy6OCK9BFWm1CMN2_TQZffl9Kt35bypgsjuBGgwXhf8xZ86zw0iaJI-0nKIfJflRpKlkqfLYtedfo5jHurXPgj6fYZgc4t8VKinO90yoXZPOr8voujXJHkrWQ-0JTuouPQ9Cb9UsPEmpUyV-M335oLQB1B9PpHEx88T6ZsQcbg_Mg-e58kr8TXsyR0Vc_QGsge28FL1QGW6yCuBJITkBHPx_FfmgTXw4RwkU7ujdMsS3lUbDpauTUUX8nDCNyLPoSjiNTvk4OKBhP9KDoHSC-smO7UykMt7miL-QAUG2Zxn0rifHt0VhzSbbWoPWXbyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فرشید اسماعیلی: دلم میخواهد دوباره به استقلال برگردم و دلتنگی شدیدی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106816" target="_blank">📅 18:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106815">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO78jWhcTNKGNWc3X0DrZdKEBpY6CJOVYY35gZTXk0Nu_C3KZVTF8zoxlUHL730lbepEJTvObQD8IGW-6B6D55FOfFECB-PVyqRu2kyN24CIydDZkdHRISH6nOu-XuL4vfQda_v0BBTYX3AVZebY5poL5yx91XjNEVtKCRqA5z2Djnmcv3_5ZWSzOGfFZO4JhBM9ApibHSo6q8sAVNwCpcpPcQ5LcB6SGYi8OF2udka31p-dMdVNClAV7vo7GlWxU4oHEtA-IMhy6w7fWZyi4FwlW1Y0Wlj4E6OA1HYH-UwD6PihC57ZT_zzNCgSMpZZJ8CuAYilgazYnLg6CHzYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین یامال: من در تمام افتخاراتم از امباپه پیشی گرفته‌ام. به عنوان بهترین بازیکن جهان، شاید فقط دو نفر باشیم. من فکر می‌کنم که امسال شایسته توپ طلا هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106815" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106814">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=N_cTgY_dg04aY-hXHY702Yuw0otXwIJXffSL-JhTe3sryauUQuVjDFwOC47pxs7z9njMbw8jtsCE07ds1XUx45wQYkZy7Ke1o6m5-25n2qas7oXdaqJSXTV7-eE7GW1cFsSwKecLK4Xf_gEmK4W-APUsJoS_OvKqQ9vXYlraMDHWqb9qv3787IZJAuAtpSppjknrbthhzg-AzAGNCG1_6cMhgdSkylYlzU5NczAuJSavVqNnKTQxaqBH1jWZY-FyiUCTuc__28IXzKiFFrPUV-fEiPhLNaZU1_zXgV3y9IQPkWUHZ2l7-5RywTAB4F0GWhU4Faqu5ynoBCW7ArDWxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=N_cTgY_dg04aY-hXHY702Yuw0otXwIJXffSL-JhTe3sryauUQuVjDFwOC47pxs7z9njMbw8jtsCE07ds1XUx45wQYkZy7Ke1o6m5-25n2qas7oXdaqJSXTV7-eE7GW1cFsSwKecLK4Xf_gEmK4W-APUsJoS_OvKqQ9vXYlraMDHWqb9qv3787IZJAuAtpSppjknrbthhzg-AzAGNCG1_6cMhgdSkylYlzU5NczAuJSavVqNnKTQxaqBH1jWZY-FyiUCTuc__28IXzKiFFrPUV-fEiPhLNaZU1_zXgV3y9IQPkWUHZ2l7-5RywTAB4F0GWhU4Faqu5ynoBCW7ArDWxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر ژابی‌آلونسو درباره مالکیت جدید چلسی که به یک فرد ایرانی واگذار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106814" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106813">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-SCdtcTB8tjQlZM0-xeL8Abr0_FaVeWsIc7M20h7kgGdvikTRG9FwT10NBHu8upzOt6mQuY07eQEs6CwIqiAjNAhcd_TqfM_NkAOUXBvUb8_HskDXmkkMoFg5lJhwnxckJL0GBP9bJiBN8LB37jhrb1WtW5jvvq3CqsG_jxlIYtpz6T3vIUm5txDYEh85m2DcgNK8W6gDutvnvAKJ1I7iCI1YiRF3kit0puVec88T09RDfSy-pKJrsuCM3rygJ6hK3NpyhtzojbPQxMruG2bM6aEA9Zi8NxSGDN8lWafUctM_vraY_El94-6sciITwuAD_mx_3hiZdOKppAEb8jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رافینیا: می‌خواهم قراردادم را تمدید کنم و دوران حرفه‌ای‌ام را در بارسلونا به پایان برسانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106813" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106812">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=N3nSMtb_59dfBgkJy4nBmAu0aWNL2-QdHojq-eOwA9qeVe4HEuCmuQGNdBwwdEFug6LEDHm_nnJDz5zlX-lAjIv4MHqeNa94vFJowl6UTAqQlyY49PxheaALYisNf6BE2JpzEKntX0B_tIWRoOhhYN6ZEzYooXWS5V0hiqUQBZGQ6Rook2C1x8iggt5N_ZrWP1DhGysmUCkbQ5IiFh9r7Jih5DGDmP01XIl8iUVCH5pzUzhjlqswTIrYaJ6g6tuFfCjeRLuIgmq-rNxXZ-Q8VqFTiU3TtkvAAt_gQOH3aEE3DgO7fkqhEYdXUVOZWzNEt0ck6pmCUEqBEJ4D0vXlNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=N3nSMtb_59dfBgkJy4nBmAu0aWNL2-QdHojq-eOwA9qeVe4HEuCmuQGNdBwwdEFug6LEDHm_nnJDz5zlX-lAjIv4MHqeNa94vFJowl6UTAqQlyY49PxheaALYisNf6BE2JpzEKntX0B_tIWRoOhhYN6ZEzYooXWS5V0hiqUQBZGQ6Rook2C1x8iggt5N_ZrWP1DhGysmUCkbQ5IiFh9r7Jih5DGDmP01XIl8iUVCH5pzUzhjlqswTIrYaJ6g6tuFfCjeRLuIgmq-rNxXZ-Q8VqFTiU3TtkvAAt_gQOH3aEE3DgO7fkqhEYdXUVOZWzNEt0ck6pmCUEqBEJ4D0vXlNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بابک مرادی بازیکن اسبق آبی‌ها: یک کیلو و ۸۰۰ گرم طلا بخشیدم به استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106812" target="_blank">📅 17:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106811">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=ZV5FotvpgSRx_gkr3IEAewFLeIXcvp4Zi1etkpCiU0BxJU-kR8QxJxjs-UAdhI7lIvZROn4gk7ex_OJQ5Nc3HW4s_7E_GXMLlPMt9JLVW3G2gPLhrIXspyXqt-hdlHJamj7GGUTbjiOVxiArL4zZQ47gNd4gEZEMLhh-QbSMEcuCq_QEiWP0T8WGDAuDY_i3Em0UnIu_8v2u1uzrpysvr7Ewp93rK6LgpBQ7_umiqfo7GpYAG8F2Q83oU28GYtVyKiw6HTtJSlZ6gsHb4TA8yAgIp1-XCLW8S7tPk2W0zGbi9GhSsgHNoJ_qZftqE5-yFma0XvxTMqExLZS_AC9UHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=ZV5FotvpgSRx_gkr3IEAewFLeIXcvp4Zi1etkpCiU0BxJU-kR8QxJxjs-UAdhI7lIvZROn4gk7ex_OJQ5Nc3HW4s_7E_GXMLlPMt9JLVW3G2gPLhrIXspyXqt-hdlHJamj7GGUTbjiOVxiArL4zZQ47gNd4gEZEMLhh-QbSMEcuCq_QEiWP0T8WGDAuDY_i3Em0UnIu_8v2u1uzrpysvr7Ewp93rK6LgpBQ7_umiqfo7GpYAG8F2Q83oU28GYtVyKiw6HTtJSlZ6gsHb4TA8yAgIp1-XCLW8S7tPk2W0zGbi9GhSsgHNoJ_qZftqE5-yFma0XvxTMqExLZS_AC9UHIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
چرا فیتیله‌ای‌ها دیگه پخش نشد؟! افشاگری عجیب علی فروتن از سکانسی که باعث توقیف برنامه فیتیله‌ای‌ها شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106811" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106810">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3_uxCwasajqVzYv3Tw-97AJ-cdO1uaSubLLdqOVui7YXuZcCqnJ4YsJPtFN4Uvd4wVaslVMAmojjqNFaZYiCmmVfDuNPhlWb25AtodCKBbcu7KyQPWnsRY9At-Xfr1kvcBpdluKclodW3VrKn8CbuAjw6CYACr0a9gFMN0v41pIMuGZIbjmCUR0pJVrdQC0L1rRHehKUNc1DlpNMQBYgywx6-2CQY3kHYo-sr6vEdSVWYa01lU4-r4uKLl6vxwK1wNf6VQw1lYTyyXJiKXLy-o_eSl5B2XD2d55gnlG7FlHwOsCaTeEDBVnvKCt_1Api0mq_-aYhSUAeiT7id9BKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
۵ قهرمانی لیونل‌مسی در ۱۱۵ بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106810" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106809">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171fd833db.mp4?token=WNSHRWE2kVwW3wUiEoL359junnK2wEQxNeXwgEU37IpyrtED2A83oyvQMe85UcZaRXHuRuwoIA7R1o3FmMOC6B3KTC9WTH5w9xMcO4fkGJjo_Q_vbrSKjuku5LiB9IOXNCVESl3eUNI2Slj_WZS-fMh33ABDi5xemO-elSMIqcJuWkYckcokFgNnPm5wbrI25ae6sMC1C1ngFvGrK9ygw0PU7-N6djXhI5HdH7OqC_uPDYOCAPeP7bpo3w3o2e0RSG665w0gTDbt7d6YtNQ34e565z7_2UzMJIY0Qj8VnNTZwjoI-AT8c_o5ONcyDfAsWb_EYtRuKl4OvchnEmjg8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171fd833db.mp4?token=WNSHRWE2kVwW3wUiEoL359junnK2wEQxNeXwgEU37IpyrtED2A83oyvQMe85UcZaRXHuRuwoIA7R1o3FmMOC6B3KTC9WTH5w9xMcO4fkGJjo_Q_vbrSKjuku5LiB9IOXNCVESl3eUNI2Slj_WZS-fMh33ABDi5xemO-elSMIqcJuWkYckcokFgNnPm5wbrI25ae6sMC1C1ngFvGrK9ygw0PU7-N6djXhI5HdH7OqC_uPDYOCAPeP7bpo3w3o2e0RSG665w0gTDbt7d6YtNQ34e565z7_2UzMJIY0Qj8VnNTZwjoI-AT8c_o5ONcyDfAsWb_EYtRuKl4OvchnEmjg8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی نشون داد پَرش و ضربه سر هم خوب بلده.
😮
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106809" target="_blank">📅 15:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106808">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=sYszOFH3iMQ1ErdtbVzJNZ1Rq-3xZcd7PenmBqRPD_X_eQBi31nNiS97snW2cZzH911LITtmgLrk6G-QuPegh9eXAkiSRrcf7lrULklP9m2b3ONgx-DArg1bRIdpvHyPZambWh3JewPF87CddpZ87mz97iffZ2pXNLmOahGjEXRDLXf96gd-swhm26BQbBXT8YhSBvvkAZm_iubJhtNihM9ifdx6Ozjthc-9n9-TpkvLNM0SH7roTYRvDypUJSrJtiYQxKHiAhJv0lYViY-W4QKzm_o_QLQbGJyZhwN5hJ3K_o-WTTOospl4CFkbToY8TGzzUH5aBuDBBIiOPamm4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=sYszOFH3iMQ1ErdtbVzJNZ1Rq-3xZcd7PenmBqRPD_X_eQBi31nNiS97snW2cZzH911LITtmgLrk6G-QuPegh9eXAkiSRrcf7lrULklP9m2b3ONgx-DArg1bRIdpvHyPZambWh3JewPF87CddpZ87mz97iffZ2pXNLmOahGjEXRDLXf96gd-swhm26BQbBXT8YhSBvvkAZm_iubJhtNihM9ifdx6Ozjthc-9n9-TpkvLNM0SH7roTYRvDypUJSrJtiYQxKHiAhJv0lYViY-W4QKzm_o_QLQbGJyZhwN5hJ3K_o-WTTOospl4CFkbToY8TGzzUH5aBuDBBIiOPamm4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
اعتراض تند رسول خطیبی به حمید مطهری و تیمش بعد از باخت لحظه‌آخری فجرسپاسی به فولاد در اهواز
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106808" target="_blank">📅 15:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106807">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N98BjJOfPpix7Gm-5fdFCfiariPegrqnfknBwfFRbeYtJKogsFUpjk-AmOrI_fdSICvaswk6RekAkNnea1gsTDC7sDKTuVjym2Fd7oSs-8aZl14_Q8zKDcXjijN6DWbXKkbre5loGlIstOFZhs96TKMuCsBSwtslvMEfCPr-uvzJzEK3IBAJPKqAolUlTT2_96NMTMZBFX84BBFpj0E5_M-YUgYGGm5nzF72zQNrd89_JfXePo151iVoKq-7Lr0Z3tWUD7tMKjNrmerITVxJ-Hw14YjvqkhDrVNUjCtqEv86q0BCNLF_7JK4Zd-R7MYIcbUAine9jbazG6kmA3gUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌐
گزارش هیئت مستقل حقیقت‌یاب سازمان ملل درباره مدرسه میناب: مدرسه یک مکان غیرنظامی بوده و در عین حال این مدرسه در مجاورت یک مجموعه دریایی وابسته به سپاه پاسداران قرار داشت. اطلاعات مربوط به مدرسه در سامانه‌های هدف‌گیری و بانک اهداف آمریکا آپدیت نشده بود. هیئت این حمله را یک حمله کور/تفکیک‌ناپذیر اعلام کرده که موجب مرگ غیرنظامیان شده. بر همین اساس، هیئت آن را جنایت جنگی تحت حقوق بین‌الملل ارزیابی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106807" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=gF4WgVfkvjl6kASi964BUVmWaz469WX8SOITeXWFkt5zbsbvRJJydn8BamlpetOCDfqLG-EErXBggCbuV6ek3Jfa8eG6lGFfwQLNE4ADw7zED8FJ5wfHRg9mIFcIuslsBvPzo6Uwv_FoDmrm-Z8dMDCLMSEUoOJpUsKciJL34x23Rep9237kD1tEOzxaitsgBY5PxksANpu5bgtci6PSwomHVMWjp3Cfw9YPYHhQssmQqHwpLN6RakJKQCVK1UcXHYdAX-H4BnUMy0kZHasHyBjWtg1RA8cl2-CwDvbNApGutEBxeiG6U3S_VUxaAb6QWBfj4b7W8XcSi5NhdjZp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=gF4WgVfkvjl6kASi964BUVmWaz469WX8SOITeXWFkt5zbsbvRJJydn8BamlpetOCDfqLG-EErXBggCbuV6ek3Jfa8eG6lGFfwQLNE4ADw7zED8FJ5wfHRg9mIFcIuslsBvPzo6Uwv_FoDmrm-Z8dMDCLMSEUoOJpUsKciJL34x23Rep9237kD1tEOzxaitsgBY5PxksANpu5bgtci6PSwomHVMWjp3Cfw9YPYHhQssmQqHwpLN6RakJKQCVK1UcXHYdAX-H4BnUMy0kZHasHyBjWtg1RA8cl2-CwDvbNApGutEBxeiG6U3S_VUxaAb6QWBfj4b7W8XcSi5NhdjZp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
▶️
مهمترین اشتباه در محبوب ترین حرکت بالاسینه؛ به توصیه استاد هانی‌رامبد عزیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106806" target="_blank">📅 14:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106805">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIe1NQNRWMXm6vHDQgm3PF3jbltSCttLTP0odcoPK0uQCy0reKjEcBVaPZNOGo_uuTkDLNVbH616THsBwg-FZzjTsSYAIzqeLFac6myAWBLPUYl4XBaSharC1I_E0jI84jOmllku7A5ySfoKT5LNNzqUhF5Ig759618I13oPcGPNNqTusKuk4y9ihLCQt4BkNPQ8-l4r7LzQ3mbmyJ1wxE_g6C4pZQiRbPvLB9DTMtetF0S3e9z1HjlTO5ZLj-4HIdF2E2js2E3bqUO9eGyFlNoHWWs_5MGfvEJ5TJuyqEYrFYTBMoMkk34-zyYCQVsZtnJXA96P2FCTQ5AAG0YQOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیبو کورتوا درباره برنامه‌هاش برای آینده:
کار من بعد از خداحافظی از فوتبال؟ شاید کار توی بخش مربیگری دروازه‌بانان رئال مادرید و ساخت یک آکادمی درجه‌یک تا به جای خریدن یه تیبو کورتوای دیگه، خودمون یکیو پرورش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106805" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106804">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNx3CYJxLMgnXE0fUuW_hHtZaCA6oEgKW0bjKPk8vaDUfG3UF0b49Cn9E7DPa79uKQNsoasRQDYkcdcGS3c_rjssYL3yFU7C1ABEOusTyzsYDf3j4w53Ha9Nahe4A8a2HtcTwchtB3gDlmtBXLTTPkYSSEq7NujOu7a070Kj4DjMRuUncfEQx9s7_iYELfAAvHAjCfLH5cHWy22EvAyg3BnBkfTQwrIhjRss2mVHEZV5GweuGUEGgmDcHu4Al2zFD4RLhkpNy0MXwCHj7mkejn4vFEeQ0uzcOTkKejYe_BwEkmeg8Y9X7XemteTFNyqW-9dgl6VAtbNIFROlNR4WaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هری کین درباره توپ طلایی:
"من دوست ندارم درباره خودم صحبت کنم... 73 گل، خودشون حرف‌های زیادی برای گفتن دارند."
"این بهترین فصل زندگی من بود، و این تفاوت بزرگی ایجاد می‌کند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106804" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106803">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=WA5igbSCeWCdfVnw-pONZ3qYD46rxRDoWe_blBc2eT9mxGnnwuj4vjd_3WZJCrjdJB3QsMZFgcW35TwHrXkO5M-pmzPhI_FD7EFIel6cRDbBPlPCNW9Lf3UggAcc809QhigI33XFdxiu3deS3eJXyiH1H2_-Y84BFaYNtRhYZF4DpRICE46nPGhXl43EinmpQ_ix42Z5zCnOiYx7_V4khwB_uRCs8UX-ogBQSf8PVF7BKTFJ17B2nwa7SnbGG6W_nLF7kAPHB4fb9p2SibXYlMdC7V1-Cdjnh4HDhfwyHBzJZUkSy5J_rHH7AxWCXTRF7xA6onN2jwLR9YfR7mGligcjy6Cs7TPu1qo0VH6uNeyCtylN7yndV_LiFoF5DyXz8TGKUwntFZN_XJ94yW8j2_Y9MkjtQOjf3fNMO80i0FZXR6lTIRp8kS0THI1jgwQjtkXcqyMhQraHVArTTJ9plitHLtFS6jlogkutYPZLODZ0MLwMOGEUBukjzY-_o1hq8hTd158ic09oHXyTg4n38kTk1Hh1Fh1H2RxdCm8EQsj4E3JYJuM9Cl2NiUeU7LAep9yy2MTAuA9T8jtvA-FW6A2PpqPPTGHuUwdEDj9wWZ5fQLCRsCZ-zvKJmMpDfRvs90zEX0FQGq3-encjmFXQ9BQf_LCieR43PhZhzxzFLTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=WA5igbSCeWCdfVnw-pONZ3qYD46rxRDoWe_blBc2eT9mxGnnwuj4vjd_3WZJCrjdJB3QsMZFgcW35TwHrXkO5M-pmzPhI_FD7EFIel6cRDbBPlPCNW9Lf3UggAcc809QhigI33XFdxiu3deS3eJXyiH1H2_-Y84BFaYNtRhYZF4DpRICE46nPGhXl43EinmpQ_ix42Z5zCnOiYx7_V4khwB_uRCs8UX-ogBQSf8PVF7BKTFJ17B2nwa7SnbGG6W_nLF7kAPHB4fb9p2SibXYlMdC7V1-Cdjnh4HDhfwyHBzJZUkSy5J_rHH7AxWCXTRF7xA6onN2jwLR9YfR7mGligcjy6Cs7TPu1qo0VH6uNeyCtylN7yndV_LiFoF5DyXz8TGKUwntFZN_XJ94yW8j2_Y9MkjtQOjf3fNMO80i0FZXR6lTIRp8kS0THI1jgwQjtkXcqyMhQraHVArTTJ9plitHLtFS6jlogkutYPZLODZ0MLwMOGEUBukjzY-_o1hq8hTd158ic09oHXyTg4n38kTk1Hh1Fh1H2RxdCm8EQsj4E3JYJuM9Cl2NiUeU7LAep9yy2MTAuA9T8jtvA-FW6A2PpqPPTGHuUwdEDj9wWZ5fQLCRsCZ-zvKJmMpDfRvs90zEX0FQGq3-encjmFXQ9BQf_LCieR43PhZhzxzFLTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تأثیر غیرمستقیم تحصیلات بر فوتبال، از زبان بهترین بازیکن جام جهانی ۲۰۲۶ و برنده توپ طلای ۲۰۲۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106803" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106802">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=KOlPV3kIk3eeEYLcB_ifvGRfIHk_3FjuCMQXg95DNIqdcHxk7iiwSCJIk6CRifYU0TSwZw-eBsp__I_7K40EN_DgOIh3MZ2VpOY0CsgsBmnt6Zy-IFolGTvj1feMkFz-HqWvxg9fbhWFx5rNdec17rRq0DJl39grnugy489XCDTLETuK9Gxx76aFux0rdjW-ZFesZpHo4AhihmSJHsWPiHq8-Mk-aCpQmsFNf3oyAwPxr-7pmyx_b9lppYcIQSnRIOoLkyWcpOAcJ8J1NF9mXPw73GfwNQklq2whtxQFGp8qTHTkK7gJDCz8Gh-K9f1-WOBGypxDhZofnZArfJ8abg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=KOlPV3kIk3eeEYLcB_ifvGRfIHk_3FjuCMQXg95DNIqdcHxk7iiwSCJIk6CRifYU0TSwZw-eBsp__I_7K40EN_DgOIh3MZ2VpOY0CsgsBmnt6Zy-IFolGTvj1feMkFz-HqWvxg9fbhWFx5rNdec17rRq0DJl39grnugy489XCDTLETuK9Gxx76aFux0rdjW-ZFesZpHo4AhihmSJHsWPiHq8-Mk-aCpQmsFNf3oyAwPxr-7pmyx_b9lppYcIQSnRIOoLkyWcpOAcJ8J1NF9mXPw73GfwNQklq2whtxQFGp8qTHTkK7gJDCz8Gh-K9f1-WOBGypxDhZofnZArfJ8abg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
زیباترین گل‌های کاندید پوشکاش سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106802" target="_blank">📅 13:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106801">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=sxq_lTxraCDzlfQn8hJRgjx-X4eI083Kwt_UFZcR9-a3DXU163T3y7hQcCUWrIFbYn9bo63J5hh55RQSqvCAhcWzICzSaIvtV2kamx3LZ1b3pbOxeschqkSYP_AeP8zcv70q7klXByqFLUKRcejmwTYBRHydNQr7hVlFodVDshRy3D_Ha_DC9Cdblh-XtPVwD3HfOIBzEa2ny3rFm5F073yvEnOYlMzznkfIrWwBUHoTUzYqgY94vT-r2SLZHipn2P6lGulhORth33gEFWVTeQO0tDl_zgsKflBF0xLmVWnrXmnvw_MbgRyycJX5weFlFE1a-2pNfMUCdUEKEUtjPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=sxq_lTxraCDzlfQn8hJRgjx-X4eI083Kwt_UFZcR9-a3DXU163T3y7hQcCUWrIFbYn9bo63J5hh55RQSqvCAhcWzICzSaIvtV2kamx3LZ1b3pbOxeschqkSYP_AeP8zcv70q7klXByqFLUKRcejmwTYBRHydNQr7hVlFodVDshRy3D_Ha_DC9Cdblh-XtPVwD3HfOIBzEa2ny3rFm5F073yvEnOYlMzznkfIrWwBUHoTUzYqgY94vT-r2SLZHipn2P6lGulhORth33gEFWVTeQO0tDl_zgsKflBF0xLmVWnrXmnvw_MbgRyycJX5weFlFE1a-2pNfMUCdUEKEUtjPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
توضیحات مجتبی‌پوربخش مجری اسبق تلویزیون درباره افتخارآفرینی کیمیا علیزاده در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106801" target="_blank">📅 13:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106800">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9960QSC-MFI7AI_I05cpYfuTYElxVdNsny640X54SF8IlwbPyYtS7B1OqN_cSdpTRVX3hzQLpA43EpS_q8U2dpRuVByhT6XiygZ9Eg32sWs1MvJjdquXIiW3TzInMSK9aL67JfRqlfdDMfsoFAC3NX4s36XzgCVm811uDl5m04pxRU_euyo2lnd8yazKrQs6vtUaPU9hgOwZxqbDqLjSnSO_UBpgAq5tMuOEv2q_A33rmAyR6Rp2HHgxQW_K6CIX5g2Z4e6FPClvzL0FDr2mvlMQxeIuyFlWVSegrDXtyitsWOIObjTr4uFtL9qAfxHaZ2C4mNzWR-L2gw6vjonog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیست تیم‌ملی انگلیس برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106800" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106799">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
🎙
صحبت‌های عجیب و‌ دردناک مهدوی‌کیا از دخالت خانواده‌ها در مسیر رشد استعدادها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106799" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106798">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106798" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106797">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVxe_er6hiiOI7h8cstlFEFrvML12c2EOsZSoKd-TXPqQWzerHsUEQYihlk5nTza22R36LgSJMM5eUmRkfFv2ZCKMvNgvbw0LNU-1NGVV3elxB-_q8C8sAyerXTPszcb8eivuGKwTCQb5848pjOle_1XXJeAP9EX5aDsAQfdcegnfWQxxKuV-DxJ0FcO13GG0wuSnaLg2d47CSz_U1tByvZtWFy270l6Qw0mVVijmcbqVYUwpsOFdsHMh5S4T_rUlbPFoxC_yutW0h37JKVnzWvihxZheMjJuG_5ap-DEFBMAUvNjxmeCV-UjhmLcerzl7NVOhT2ekpiQxjQuawdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106797" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106796">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjpbjAdZMgVsgIytVD0puujvDqLgDPNOmMWE2uIw-YUVf8bZrTL32-oCuLFqPbGba2abILYLWiAK-fQpi5gRA3gTjDWMaIPkCAcrviCrlMhiok6EJa9JR4Gbv-q609n3uqXSP3EUp2VDNTzHfzUQv1UlikG7sQNYNq2W271nmju0UuvNlyonIooC9TzGDJ4RxxP6i42V26m2IrHYcECuXEDxCLjwbFM8H2g8YjdsvHKHg3WOlJ3PFE12UuzzBXygmZNHosnpLQ2KiRM5UmrRpksO20BQAT4ClB_YdmJFZw0Oy3FXQba4pymYBPj0kc-73OZPZD33WvanlXtCcVVJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
رافینیا، با هت‌تریک خود مقابل راسینگ، در 7 بازی اول فصل 2026/27، به 14 گل و پاس گل رسید و رکورد بهترین شروع فصل لیونل مسی در باشگاه بارسلونا را شکست. مسی در 11 بازی مشابه، 11 گل و پاس گل به ثمر رسانده بود (فصل 2012/13).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106796" target="_blank">📅 12:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106795">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=jgg3WnCpqN1Ul7W_1hrtswiz-xb6xaSYF-4robWniChXqL4Fr9ZrmVCOAJUJVMVYSeOdgus7LUZmeFkYJiGR7L1lcLJmQXQpJwzzBixSUgFJuCUa5YG1Fifj2gHtZ5kxqnEkfz0Spjx3MwUe0inD0_NFf2-XhTyO6RXKbAd1VYeOJc_ijj0uB-CGq3-p7Fmr1deBLHU_MkK5bflM4qyb_dLOXXgCBzBOaVBeGDzleklXgoHmw4T9PuqhH9SIlyF76O6a_q2PELYSTD1qBv8YBlyROZ5oqXo8MQBRhAKjWuJqmyS7fDy8HBWCauxs2uESEpaNyjihFYYqGZZ1vokNHHz21CS5lQAyyChIRXlGz0APsHQNizjykpFx_p2T5lsSGZ59gpjXe4BpRXuGR7n2UTrRXSiwA1aCIZ9qKpYP9aVWdrn4q1nKC7gBBq7sG_jdytTkrA_WughVsu0gkAHAIiRdhiRmMrQvxip_rM9cNnTzJzZTOjtaZXeS7wMId5218Z7CQhWIr2DmQ0Y6HQpbkEi5pmlJmKTeMZ6W11kBu9gHbDuHgOTRCvpSxnVPRBk6-ueCKytGIoDgIxwVlD43pAxVjKlz0wJXulx-7H7ocrxrkEg5hZi1s2AwUbAAbyJu2vyHo3PyWUjix6XKLxbG7JsRM_MmeBlcr90BZ3t0yCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=jgg3WnCpqN1Ul7W_1hrtswiz-xb6xaSYF-4robWniChXqL4Fr9ZrmVCOAJUJVMVYSeOdgus7LUZmeFkYJiGR7L1lcLJmQXQpJwzzBixSUgFJuCUa5YG1Fifj2gHtZ5kxqnEkfz0Spjx3MwUe0inD0_NFf2-XhTyO6RXKbAd1VYeOJc_ijj0uB-CGq3-p7Fmr1deBLHU_MkK5bflM4qyb_dLOXXgCBzBOaVBeGDzleklXgoHmw4T9PuqhH9SIlyF76O6a_q2PELYSTD1qBv8YBlyROZ5oqXo8MQBRhAKjWuJqmyS7fDy8HBWCauxs2uESEpaNyjihFYYqGZZ1vokNHHz21CS5lQAyyChIRXlGz0APsHQNizjykpFx_p2T5lsSGZ59gpjXe4BpRXuGR7n2UTrRXSiwA1aCIZ9qKpYP9aVWdrn4q1nKC7gBBq7sG_jdytTkrA_WughVsu0gkAHAIiRdhiRmMrQvxip_rM9cNnTzJzZTOjtaZXeS7wMId5218Z7CQhWIr2DmQ0Y6HQpbkEi5pmlJmKTeMZ6W11kBu9gHbDuHgOTRCvpSxnVPRBk6-ueCKytGIoDgIxwVlD43pAxVjKlz0wJXulx-7H7ocrxrkEg5hZi1s2AwUbAAbyJu2vyHo3PyWUjix6XKLxbG7JsRM_MmeBlcr90BZ3t0yCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فرزانه جمامی، سرمربی پیشین بسکتبال زنان استقلال: تمام اعضای خانواده‌ام بجز من طرفدار تیم پرسپولیس بودند و هنگام دربی اذیت میشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106795" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106794">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lktPfLnH9sWPReawaFKaAHg-dzY-1uN6_xI00cYVe4Jray2cP_e0zOlbWSk1NLeBT8LuUdE6SgBRT1hhnhoQDJRfgWVGXmRDDZry01w-Pt3ZRgeVXdnrThhyXsxXYDwg-hx2SQPdyqxSel1mY2DVlHQnwMpicTf24emy6x04nne5oAL4Vm774OcPactlumbH6vNF09wgj99vlAc_oPd37ycZAKvfmh1ZrnxHxW_I45XSCJ0z2mpduDF8f4_2-MUcdxDmrpFCypdMpriEiyDREfhhNu1RsfyM_8ssWOuV0fIGqW5XArDU6EjiRwq0P5a9ldtTc6r6ojq2ALMeyitQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه شروع آموریم و کریک در پریمیرلیگ با منچستریونایتد؛ اخراج بعدی در راهه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106794" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106793">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=Bf0BTEcCTgWR8xvHQyLI8tzTkFKhHHv1UTNYl3Y4NcIuJs9kejS2U4DEMSuUkNvaZAS5aDqiIv8EHv8yVfXVGCEZL_IGF9KxX_WGH2hkyIUL3THrzOGBBL1FbGVzSC5VS-ksyb9LSpL6iA3ZrjUf_DW0Qvyg8sRjqipYm4nsR2-7G9ypSxouHiAEzSeoAJlJQqzVnr3N-xDJKyKp4_CUrKK7Um-Sc3yavI1IdSyG89M_PuSf7qpZkD9pJP5e2xIEwVsAxxGmUC-qJ66OLd3PvDJAJfL3v5QRMHMDxjYBl3qKVEfktGyQxnsSDy6kqjj4SGlTRUXi8GLPO6w5L-fNsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd63d44791.mp4?token=Bf0BTEcCTgWR8xvHQyLI8tzTkFKhHHv1UTNYl3Y4NcIuJs9kejS2U4DEMSuUkNvaZAS5aDqiIv8EHv8yVfXVGCEZL_IGF9KxX_WGH2hkyIUL3THrzOGBBL1FbGVzSC5VS-ksyb9LSpL6iA3ZrjUf_DW0Qvyg8sRjqipYm4nsR2-7G9ypSxouHiAEzSeoAJlJQqzVnr3N-xDJKyKp4_CUrKK7Um-Sc3yavI1IdSyG89M_PuSf7qpZkD9pJP5e2xIEwVsAxxGmUC-qJ66OLd3PvDJAJfL3v5QRMHMDxjYBl3qKVEfktGyQxnsSDy6kqjj4SGlTRUXi8GLPO6w5L-fNsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پاسخ بامزه علی دایی به یک سوال عجیب
طرف انتظار داشت علی دایی چی جواب بده؟ بگه نظرم در مورد خبرنگارهای مثبت، منفیه؟
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106793" target="_blank">📅 11:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106792">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=EebIsyeGdg3UWW3p_3eIBBrrLaP2hLp2Ffgxh3_lyMO8Ce-GzF98JizZNdlo5CceGE_Jkt4ANCZ2IGsu0UWxwfHO-XjyCCg7E1AOTUR8Kh4p2SyTT7lOv6IZIqlYgkKPatCag-37KvBJYbt3nArLRpUP8jykByMXFCZXAMHl5J8-GHiGcambuyK41q9lNNmsMa3kVTD_txRCCnURXfiOVlvtAUO2KvdY2KUoxri3j2gPlbN5cQBXYx2gegm4FjebyfU969ujxkZojJmzZbutMErTIs7LpQNq7W7dXnRd81M4gno-cICNbtQHyb7oPHUrGuO7TkdBiyMJyA0_2W1yxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2af4be6.mp4?token=EebIsyeGdg3UWW3p_3eIBBrrLaP2hLp2Ffgxh3_lyMO8Ce-GzF98JizZNdlo5CceGE_Jkt4ANCZ2IGsu0UWxwfHO-XjyCCg7E1AOTUR8Kh4p2SyTT7lOv6IZIqlYgkKPatCag-37KvBJYbt3nArLRpUP8jykByMXFCZXAMHl5J8-GHiGcambuyK41q9lNNmsMa3kVTD_txRCCnURXfiOVlvtAUO2KvdY2KUoxri3j2gPlbN5cQBXYx2gegm4FjebyfU969ujxkZojJmzZbutMErTIs7LpQNq7W7dXnRd81M4gno-cICNbtQHyb7oPHUrGuO7TkdBiyMJyA0_2W1yxoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دلایل جدایی اسکوچیچ از تراکتور
زنوزی: اسکوچیچ شخصیت ماجراجویی دارد شاید می خواست با تیم دیگری قهرمان لیگ شود اما...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106792" target="_blank">📅 10:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106791">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=rXXu5aMBaUVkx2sgmVBnPZWHs5g6MTTK5-V2_a5iqBNMPTV0Cm0FU0WmO1iPpGu339LKVDoFT2EL9FZZCufhR9yh-MZtYT1XOJkrjo5w8ynZntgbK5KGpNBAjzycbpPJU1nnCK23aR7HFu6wfgBpVEZAfA9vX-A55QA3MF-te3hZFErXol5kvrmOvehe0MxLbgjXZEs3rCJuDyhh9pQiqXwatAWGJLuc1XgCDugu69Gxpv_ngGU8XeAwHHs-3Vcl29BJPhUoUNI1TI51MIF6sWEj1MhYNeYX5U-wgpBJULUH0qLHN2lniXKXSZ0TUkqk2_6hHLZew1NpBzVZd7QlVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebaab7dd8.mp4?token=rXXu5aMBaUVkx2sgmVBnPZWHs5g6MTTK5-V2_a5iqBNMPTV0Cm0FU0WmO1iPpGu339LKVDoFT2EL9FZZCufhR9yh-MZtYT1XOJkrjo5w8ynZntgbK5KGpNBAjzycbpPJU1nnCK23aR7HFu6wfgBpVEZAfA9vX-A55QA3MF-te3hZFErXol5kvrmOvehe0MxLbgjXZEs3rCJuDyhh9pQiqXwatAWGJLuc1XgCDugu69Gxpv_ngGU8XeAwHHs-3Vcl29BJPhUoUNI1TI51MIF6sWEj1MhYNeYX5U-wgpBJULUH0qLHN2lniXKXSZ0TUkqk2_6hHLZew1NpBzVZd7QlVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
روزی‌که استقلال تحت هدایت جواد نکونام قهرمانی و اورونوف رو تقدیم پرسپولیس کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106791" target="_blank">📅 10:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106790">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv7T2HwYDHw1U0t0qX9xp6wNlpIuwcOVAJ4M0IrZQDmHz4oRUNBlFcaI-Q1UaHqWEq_mj494PM4rUqfINQrc-5SGE6fPxZDjurG4S3MUZ7wCxiwmbSJuEpD9UtH5qiwUPTfXDqzAwcoSigiwdA6G5o-rG_HXHA1sVcH6VbrwRWQ6aOByZd2fuhqVm0hqXO5CvER9pEKP7jGVIJnTcW6Ondxe7cSmjS2YTatwWJ6AcSmD0tIWiTpJUlVonerVHkIrCgfaTOECPVHDsj-MGKR68II19Sx04szGlN2rDEvrl-1RUGXRyGoANE8jll1PoroO_2dFx8CZAn6GlK_u10oj9fCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c341c5cc5.mp4?token=ZSxxg0yQa1XyOelCHOV77SaLgrdSMjv8K8YvKvIIDzzq9u3OUZpCOTxHAEA3kJulE47gvNBRQLAh13gQf82papXI5z7oimN6SjbjD-OmZTAkM0h5yIhqZ7GFKpdU1uMA1ihkylQfCzBu_v-bLwQDTUmM-byQGTScMjHmNWb3cutMD_nYvpvfjuPOZ1jlH2fF7g8L90XGLn6Dz1sE-KuegL800UfTQ6-3ZBY4BdZWoz-JBEAFZIzXV6pRN9gUTCGNMP8bFqIBYoEFHfoQwu482Qa2IgpAyIfctdGfRqw03DcsUpmQS3vf_NGoRY2jtmW_v2zLg9GWTLaNU347Tquuv7T2HwYDHw1U0t0qX9xp6wNlpIuwcOVAJ4M0IrZQDmHz4oRUNBlFcaI-Q1UaHqWEq_mj494PM4rUqfINQrc-5SGE6fPxZDjurG4S3MUZ7wCxiwmbSJuEpD9UtH5qiwUPTfXDqzAwcoSigiwdA6G5o-rG_HXHA1sVcH6VbrwRWQ6aOByZd2fuhqVm0hqXO5CvER9pEKP7jGVIJnTcW6Ondxe7cSmjS2YTatwWJ6AcSmD0tIWiTpJUlVonerVHkIrCgfaTOECPVHDsj-MGKR68II19Sx04szGlN2rDEvrl-1RUGXRyGoANE8jll1PoroO_2dFx8CZAn6GlK_u10oj9fCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداحافظی خامس رودریگز از تیم ملی کلمبیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106790" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106789">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0579123b95.mp4?token=Rak7InNqU8zczZYxpVi1MYpxWVBDh64liYJccdhfCy8FoZ62Hu69qr6zQlRByH-Gby36yLg-JpYaeHMfqjjw3cC7f49Ueht00dsias0SEmKWJLrNbO1Edo_hFinCekHjHpknogYeqb5h_GH9QIOI_qZS59JAbnXLSgGE6EOJ3va79DLQMiQIBI31vC41SeMJejNf6t3pKHJYGCLXmHY5a39A3lABhiRTHqUwAMsJ5Wu7KFBDbtYaeSUK2IgoEQx_kyIPOB1xdZR0Vt8Nqu5j_Mu9OpWgrzXsOv6njhSdx48Y1ScI-NnfacCtGi11a8FyBDalAZAdd4kRQJ3SIK83VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0579123b95.mp4?token=Rak7InNqU8zczZYxpVi1MYpxWVBDh64liYJccdhfCy8FoZ62Hu69qr6zQlRByH-Gby36yLg-JpYaeHMfqjjw3cC7f49Ueht00dsias0SEmKWJLrNbO1Edo_hFinCekHjHpknogYeqb5h_GH9QIOI_qZS59JAbnXLSgGE6EOJ3va79DLQMiQIBI31vC41SeMJejNf6t3pKHJYGCLXmHY5a39A3lABhiRTHqUwAMsJ5Wu7KFBDbtYaeSUK2IgoEQx_kyIPOB1xdZR0Vt8Nqu5j_Mu9OpWgrzXsOv6njhSdx48Y1ScI-NnfacCtGi11a8FyBDalAZAdd4kRQJ3SIK83VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حمله تند فرشید اسماعیلی به شفر: قبل از فینال جام حذفی گفت یا قراردادم زیاد می‌شود یا روی نیمکت نمی‌نشینم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106789" target="_blank">📅 09:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106788">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=KHI2YXV7J5kcKQWhZFUwv1tLzTdhfY0_j_gWJU33DdvtPdLXSsqXQgCDwDqPPfni7B86OfY7skIdC700ug2-T-5o_W4jNQCoMPcWoaulCOS6d_jmjbxbVlZviPwnPml5wZyFqUD4AABU49ws4S09wGPceqh65VjJ288zcd0nhghpE46CZzak4-15ESwryavhdxa56XPq8xdvQowlY8X6punczeUi8Y_4HZGGVMQSA_VbDAivOl0TFD0oKW46e4E2oouo8n00Ga_0WbdiAQbW__6Zsc-iDQl7RT5FsNHxOgmZQUeOyYYkMAhEroOVHNzC3oAyOQzcWvS0lY9lJTqFPD8PyqlFi2fE5mn67HuJiZCT26ifJ8_fkT63X7ZdNSZ3BzrQOOpA6Af2T5AV4HebZhaoA7wL2UImkk8j5oNqj12fWoV8tlCbWp9pVzgM9SJv8brInEXrgd0lSe_FDkZwQm_xXnIq66MY1CtnIZlgMHyFxMM8g52EfM3F-32kTluE2Y5xsu9xlZElj9WibLLjw_fPqmcjNeZihfy3feSFaFQuJ9prjeDaGQRKnWRRVfJ_cxu01oiUqT5A9SX2_Ck3SruFvew4pGbJD4N0ZblXYvSWwq1oMxYmlG14q3ZPjg-jiMHByanSbHBrkvcAKE9GrZ-vI_8tU_-ZsHttYygJd4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1063b33e5d.mp4?token=KHI2YXV7J5kcKQWhZFUwv1tLzTdhfY0_j_gWJU33DdvtPdLXSsqXQgCDwDqPPfni7B86OfY7skIdC700ug2-T-5o_W4jNQCoMPcWoaulCOS6d_jmjbxbVlZviPwnPml5wZyFqUD4AABU49ws4S09wGPceqh65VjJ288zcd0nhghpE46CZzak4-15ESwryavhdxa56XPq8xdvQowlY8X6punczeUi8Y_4HZGGVMQSA_VbDAivOl0TFD0oKW46e4E2oouo8n00Ga_0WbdiAQbW__6Zsc-iDQl7RT5FsNHxOgmZQUeOyYYkMAhEroOVHNzC3oAyOQzcWvS0lY9lJTqFPD8PyqlFi2fE5mn67HuJiZCT26ifJ8_fkT63X7ZdNSZ3BzrQOOpA6Af2T5AV4HebZhaoA7wL2UImkk8j5oNqj12fWoV8tlCbWp9pVzgM9SJv8brInEXrgd0lSe_FDkZwQm_xXnIq66MY1CtnIZlgMHyFxMM8g52EfM3F-32kTluE2Y5xsu9xlZElj9WibLLjw_fPqmcjNeZihfy3feSFaFQuJ9prjeDaGQRKnWRRVfJ_cxu01oiUqT5A9SX2_Ck3SruFvew4pGbJD4N0ZblXYvSWwq1oMxYmlG14q3ZPjg-jiMHByanSbHBrkvcAKE9GrZ-vI_8tU_-ZsHttYygJd4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👑
🇮🇷
ینی بهتر از این خانم بنظرم کسی نمیتونست تمدن کهن ایران رو بیان کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106788" target="_blank">📅 09:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106787">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7912d30312.mp4?token=mhmktq5zHM9m_HgeVG84PKXgrgOHBw3im4YOjemAlUvzQriU9alqdbCbHUut4QwdDEoaNZu0rTF6rRFM6EawGmNGFOXZLUQQ88b4f9f1aGG5XJ7ZLUmEMKzUl1LcGN1AEZG2xfSZnJx5MFbGI9iSQzllZf-oGUK1HfZN_Vr6dfLOYi-aSQkx73F-RYcJb4DBE-l3rm7nEik9JKj9iP8NeGC-5cTINEfsktqZW8ENCK2hFVCbxJamARd5Oqn3qCMl2ivihVz7ugBFtfrOuxrEFTvg2JPc0zaCC9Tv8afahhrYF7DhAasxhjsWeK6PFqe9jQgX99ijKgT99MUj1Ft2ZgJDJOw6cPr78MefXiaDXrW3SCg7z0XXATM6VUZC1K4pFh05_xgs59V6nH5MlWGvxcaybY2GccMPCbNnxQ1QLT_Sa3Op5rSEhbrxRDA1pNXkPVH0Gm2bkBup6HaREhkFV6QzCckfodhWJDJ6IAMdvFluhbUgEtKe_-RWt25hTNWuS-O19B0qzwo3_MYHoeXZDYSPzB1N9QE6PImwDOkxnCohu2vRX8yeTfUKcsJ8od5pwEeBPwQeiisfm59KGAR_L5GfTma45TO5Y7C1GM3lYYTnvJjlY8OWZep4vOHLNgr0_Zic1V75pfRPhZBRQYmggIskF4w3butKLpyp9Y2fDMU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7912d30312.mp4?token=mhmktq5zHM9m_HgeVG84PKXgrgOHBw3im4YOjemAlUvzQriU9alqdbCbHUut4QwdDEoaNZu0rTF6rRFM6EawGmNGFOXZLUQQ88b4f9f1aGG5XJ7ZLUmEMKzUl1LcGN1AEZG2xfSZnJx5MFbGI9iSQzllZf-oGUK1HfZN_Vr6dfLOYi-aSQkx73F-RYcJb4DBE-l3rm7nEik9JKj9iP8NeGC-5cTINEfsktqZW8ENCK2hFVCbxJamARd5Oqn3qCMl2ivihVz7ugBFtfrOuxrEFTvg2JPc0zaCC9Tv8afahhrYF7DhAasxhjsWeK6PFqe9jQgX99ijKgT99MUj1Ft2ZgJDJOw6cPr78MefXiaDXrW3SCg7z0XXATM6VUZC1K4pFh05_xgs59V6nH5MlWGvxcaybY2GccMPCbNnxQ1QLT_Sa3Op5rSEhbrxRDA1pNXkPVH0Gm2bkBup6HaREhkFV6QzCckfodhWJDJ6IAMdvFluhbUgEtKe_-RWt25hTNWuS-O19B0qzwo3_MYHoeXZDYSPzB1N9QE6PImwDOkxnCohu2vRX8yeTfUKcsJ8od5pwEeBPwQeiisfm59KGAR_L5GfTma45TO5Y7C1GM3lYYTnvJjlY8OWZep4vOHLNgr0_Zic1V75pfRPhZBRQYmggIskF4w3butKLpyp9Y2fDMU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
صحبت جالب رسول‌مجیدی درباره تواضع رودری ستاره بارسا در دلجویی از والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106787" target="_blank">📅 09:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106784">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axUevwwvtTFpKgi5Qyti5Te6BLiggDr_hanRk2oiNaJWi9tuoUpRFq3j2fOJtxCBW6SNmwdF55sk50i3fN7bWhG0BCvdABF7dI0qa9d4yz2ecwL7rNP028DFjgDXEtJwx2RycvCEREweXztsbphLYbaJyWYwmKgtBERI5hkplhyB3SSPhPGkbWUUWStqh8ilapA2f44chzD3M79lv7w6PExtsYmiNq1tTjP_-20i8bZ0VYrDUeFbPKW1gAe5YBqx4Pl-odhZu4MMPpt9J8eqfqJh_uPKxY004qfbl0AIw0N4enSjfNIQRxjqtQNuDhTPVdF9NYVGBHyd2Oqp5lkCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
🇪🇺
نتایج هفته اول لیگ اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106784" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106783">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=D_S7uqCNdzh1yEZCuC154cECRxmy5nowClT0eq9I9ExcP-dmP9QcfqZRDtiTuCdf6XelY549KEdiKs8dV0DsM7ukJVP8URwyvRitJA2zfDMKasPETB4rK3ofkLqM_gh2934Bp9HzWwST3lAjlOdlIc2jQTowk_p70vFeMcYMlAkVH6P6FbpK8UNUVNovPUgwVhGhyohjXh5aGXhC86cU2u1iZ6b3ML4dMjduQiTvtwleUfrGsAE3ym-S4Mg4Li07Iks0j76pS1ZFXJQ5QnPNf9NVWfU28n_-aiZUAViWGN3QDtlUB8sjVS5FzcHduPINPgVAC_MgCoE4VtG_Yb-0ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea7884a87d.mp4?token=D_S7uqCNdzh1yEZCuC154cECRxmy5nowClT0eq9I9ExcP-dmP9QcfqZRDtiTuCdf6XelY549KEdiKs8dV0DsM7ukJVP8URwyvRitJA2zfDMKasPETB4rK3ofkLqM_gh2934Bp9HzWwST3lAjlOdlIc2jQTowk_p70vFeMcYMlAkVH6P6FbpK8UNUVNovPUgwVhGhyohjXh5aGXhC86cU2u1iZ6b3ML4dMjduQiTvtwleUfrGsAE3ym-S4Mg4Li07Iks0j76pS1ZFXJQ5QnPNf9NVWfU28n_-aiZUAViWGN3QDtlUB8sjVS5FzcHduPINPgVAC_MgCoE4VtG_Yb-0ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
ادعای هومن افاضلی: ایران در آمریکا از ورزشگاه آزادی هم محبوب تر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106783" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106782">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCvd4iFw8Eii8lVqQK3qPh2179_4KftOz_4S5LcvyLRZKDIoxZV5u4-9kzg98lhgAvJ-YoQFpBfPaWuAZKig2umEIgiNpEwaE85jFta_obabk1nbi383QDDl8pGSBdsNdJF_T2COFpc3ubWHhbbO2chgOLOJEek-g7tuUZVc40kZS28Mfhizzz1sTa_hoH0CnI77zgNKFIV8mr1jze0jVZtMJBcD8xH_pbpKXr_BH8Jc2UCH8VJMWlM5CMFqSgpSpqzKCcEFuDMxtHnYQwWxVu3-1V1QIUpjTR7bdkymzivbdGIokI2Zo91mVAvVt8wmyNsefXor6qkTgs-ywNVRkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام‌اتحادیه انگلیس؛ سیتیزن‌ها در یک بازی درخشان و با گل‌های بازیکنان ذخیره خود مقابل نوریچ پیروز شدند
منچسترسیتی
😄
-
😏
نوریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106782" target="_blank">📅 23:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106781">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UASHGEzCGUpAaaYlFe0psOKnCE_fd7wFjuUW4-tuZjIf7xHTe4l7nIl5q3UssffQs71E7ew9himvR0duetsikUSwMbZxyPDYPucsi7ulGTdHRpDWJojA42ah3-3XbZwVluare8s9FSI3JTYekQ_KcFm8GzOuQtg_W8NUp5fFNHJLDozb6mZawWEPA3fscrXPuR3I7qd_e9g0fYAwd1jZVfIbNHDkLfnFd0wwpUrf4Gd1SkcRhB_fC7n6zfXchGlqvaXhdtcjb25YMIjZ5Uh-wWqzrEJxMLh6Vds8rHrS7IujPYfFNXXflJhJLxq8fPAr4h1iuMyWs9lJNzJlal065A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وقتی لیونل مسی در سال ۲۰۲۳ به اینتر میامی پیوست، این تیم در قعر کنفرانس شرق MLS قرار داشت و تا اون لحظه هیچ جام رسمی‌ای در تاریخش نگرفته بود.
✅
مسی پس از ۱۱۵ بازی، به ۱۰۰ گل با پیراهن اینتر میامی رسید و این تیم را به چهارمین جام تاریخش از زمان حضور خودش رساند.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106781" target="_blank">📅 23:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106780">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=o7sxpVOJjd4b1dPpdVq8Z3KDS_Gzi2kao0YHnmV5aPwFIsRsCw_jEbk5KN0uFrhzVWpkA4FmOLw7QUIFxAGFjeiiM4ESVL5zNO55jsEjbSPw8Tby5QIFoodyeHV_8ase0rc6eHyqof6fkbNFBsyNWOEWRqAfhQaWheU5ifymLYRfZ7-rB21wkzl11yo5zoMEg0KfMBjVSBom-BEGEqnXtirEwkoFqHOPpz248RE4DvqwSMCn0_orVOzorl03YG50C6EGW04f7sA__L0grjRiCoWitDAKN3PuG7FfXm0Ag1W5L8WCe4557luMIWFyU9jWr3t5o-TOCZAzfBmXRn50-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af53c1869.mp4?token=o7sxpVOJjd4b1dPpdVq8Z3KDS_Gzi2kao0YHnmV5aPwFIsRsCw_jEbk5KN0uFrhzVWpkA4FmOLw7QUIFxAGFjeiiM4ESVL5zNO55jsEjbSPw8Tby5QIFoodyeHV_8ase0rc6eHyqof6fkbNFBsyNWOEWRqAfhQaWheU5ifymLYRfZ7-rB21wkzl11yo5zoMEg0KfMBjVSBom-BEGEqnXtirEwkoFqHOPpz248RE4DvqwSMCn0_orVOzorl03YG50C6EGW04f7sA__L0grjRiCoWitDAKN3PuG7FfXm0Ag1W5L8WCe4557luMIWFyU9jWr3t5o-TOCZAzfBmXRn50-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🟡
دفاع قاطعانه بیگ‌آنز پوستکوگلو از رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106780" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106779">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAKxDGPu_Vxt5ACghAvEoDOsDcKPyAjzcV1uWxic9Koz4tTnsFbRZ48ZjFXVvvwjFLP_MFD0LqXUVxrXJKUrTIHjWWjwsRraI9jrNdzur-veoIWcuZUL6RR0PeppXUADyylGVZCZ7th55klNg-0SImeeCXf8Z6B_JMco2fv2aU0EdmdMj-l-IIp4Sp62iSeCbMBFWFkT_SJd0MlvUjVsSNkONst_VQMWtjI_uFBRMjTFh-mHPr1GEJFCCZ7KrfvbgKeSH4sv8EWkIjvzmMxI-6xwiyfH95j1jLjOdQHNYetI-8ou2S5MlXYS9tb3rZmmWg4THF_znsGlio-nkMY1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه اسطوره مسی و رونالدو در سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106779" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106778">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQNoQ92ispXmUcxw8bW3XvlBWpIOjvAwjtBall-BSO_5MsgpDUDbO5JsTS2c_UvUPNx_rYw6Ga-aeU_Ca73PuFwY4haN2t9_lN9NRIFzg-A6gvt539u6QVY1pHkAfkwtddWf6woxrdxlkSsErsJdcnwVdpsBCL-gP2wU4SUyXOlIpSL0tkLESBPZUj7YZ18HIrPJZrioYSeYlCVXUuBSgQXT9m5rHdj7x0qn8l-XjBaIsqqYKAnPhB89qEAbmkDj3oCR8aARh_sHA1W9WhApjZnKw0X3z5X4G0-kv5pQ7Fk06aOsmFNItrjxbWk6u0lZ-6NgsK6dKLwKxRPJqykvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✅
⚽️
هفته اول لیگ اروپا؛ ترکیب لخ‌پوزنان مقابل کریستال پالاس با حضور الهیار صیادمنش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106778" target="_blank">📅 21:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106777">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
🇮🇷
🎙
صحبت‌های جالب نوید استادرحیمی درباره عملکرد درخشان یاسر‌آسانی در استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106777" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106776">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGCFJjbPJ6aQ1Prl2LAyE51dqJTQqihI6uXJTqGCvrD45mYYHliwt1CC2pJG5K6yerkzSzYWVc0jhl3vhzXDJTaN2vw10K_4_yt5eWjIjkd7EXCXpIcl_islerYN0aNR9Wf6huGeAAXHdukEshlqV2BD79Pc70AjPC95MuOj6Afkec5ZxgseFVZnl1aKIjQMdqoupjhbnKtQsp7EzWKXDPWlnYwgtcOsGH85mUu-SptXaJ5iLSk_J0F-y4Z2EVtp2RSXoA2krN9vuPSMGHCI-J-j2ImG7nWRZe_IZE_3bAXzkUQV2zvzXam7rUYj48htwF_cyRV0BjufXGaUHvYsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جام اتحادیه انگلیس؛ ترکیب منچسترسیتی برابر نوریچ؛ ساعت 22:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106776" target="_blank">📅 20:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106775">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8c416616.mp4?token=Wnt6jY1GLSKPMmtVtqhTbPucnLH5gSK1WVP_dlaBT4ts6ZjfjCQxOE84SNKnBv7E_r5hEse_6Zt9d-sxb28L-FEnOY9atHGhOlgQP9l4-c5aPZdv7bHf7ghWubwOeXzAiXVkY7pc6p6xLA0WvYUpq7zStx7a3ZVATkNAZsh04a3foDudzxSu71whMbjbtS1DxhoaJ5uWdLwFqyTAV9bcmps5hfQ9pRQSkp2WHNjKyDGZ2hFxrmB9lYQ0HPa68uaQanMnsdz0UuBsXDUNSMuWaCCS2uYjuf_KXy-4iIVCEe6vYA4DuoLxYtqnQxJ_D_xUe253LVSEl1_ph1tBsF0seG8QTWleXQTvBfad-q635b8uhHBePx63cAEL7iKGOsq5XmNO_BcgAn7Ne_MvRYfE3Srtgj8oCawhCnZH_sJaIMsulJd3wnLkxaipMYsBXtQxO1HTbURtWfK7I8pBiNUgDON8sQE7DOyxMi6ofnPb2GX7W0YqaUDDXearB2j5KWnS99zoWRxfgRUk73rmfOTBXvWzx06H2RnqKhoo0kRTr3_UhCy7p_bTXoM_vO3LSBXwjrDk9BswFLtjJAe3Wbm5l5z-tVR60ooumBLFMHvTFtOMMQ_jjSad7RVOGKMIwcFyguijimmgelfV-Bngsi1QLmW9uD4LCSV09Rf-4nfyA5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8c416616.mp4?token=Wnt6jY1GLSKPMmtVtqhTbPucnLH5gSK1WVP_dlaBT4ts6ZjfjCQxOE84SNKnBv7E_r5hEse_6Zt9d-sxb28L-FEnOY9atHGhOlgQP9l4-c5aPZdv7bHf7ghWubwOeXzAiXVkY7pc6p6xLA0WvYUpq7zStx7a3ZVATkNAZsh04a3foDudzxSu71whMbjbtS1DxhoaJ5uWdLwFqyTAV9bcmps5hfQ9pRQSkp2WHNjKyDGZ2hFxrmB9lYQ0HPa68uaQanMnsdz0UuBsXDUNSMuWaCCS2uYjuf_KXy-4iIVCEe6vYA4DuoLxYtqnQxJ_D_xUe253LVSEl1_ph1tBsF0seG8QTWleXQTvBfad-q635b8uhHBePx63cAEL7iKGOsq5XmNO_BcgAn7Ne_MvRYfE3Srtgj8oCawhCnZH_sJaIMsulJd3wnLkxaipMYsBXtQxO1HTbURtWfK7I8pBiNUgDON8sQE7DOyxMi6ofnPb2GX7W0YqaUDDXearB2j5KWnS99zoWRxfgRUk73rmfOTBXvWzx06H2RnqKhoo0kRTr3_UhCy7p_bTXoM_vO3LSBXwjrDk9BswFLtjJAe3Wbm5l5z-tVR60ooumBLFMHvTFtOMMQ_jjSad7RVOGKMIwcFyguijimmgelfV-Bngsi1QLmW9uD4LCSV09Rf-4nfyA5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
توضیحات فرشید اسماعیلی درباره چیپ معروف در دربی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106775" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106774">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=Z5ffx4CFHilmDOIzfa-9sCwj3fkf9t4dcVMLEh1UShbU42K8vfTAKrNNG_tTJG42ntk7zcZg4NZesN4MOkcb39z1eaQzotAVmTXUJRa1oP7P_Gcbb-hYXYmjp3Hq3Vm7MAv9AJFenf_jgk4FpRZj10qbVhArtycVd0GgNDfV-O_ttApKut2epCs8_s0DMRg2hCNRn074_F6DMVhA1ikpZ4jEWzsA_jMnn8exipdBBZ2BClRIzGIWojw5LzEW-LRT125bidohUG4WnsD4qI0gFniLkgTmGcKLaiQdx7mK-RRajhA_25d8z2hYZKm0-swvH50fviENM-5JI8tGBVmgcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d822ce6be.mp4?token=Z5ffx4CFHilmDOIzfa-9sCwj3fkf9t4dcVMLEh1UShbU42K8vfTAKrNNG_tTJG42ntk7zcZg4NZesN4MOkcb39z1eaQzotAVmTXUJRa1oP7P_Gcbb-hYXYmjp3Hq3Vm7MAv9AJFenf_jgk4FpRZj10qbVhArtycVd0GgNDfV-O_ttApKut2epCs8_s0DMRg2hCNRn074_F6DMVhA1ikpZ4jEWzsA_jMnn8exipdBBZ2BClRIzGIWojw5LzEW-LRT125bidohUG4WnsD4qI0gFniLkgTmGcKLaiQdx7mK-RRajhA_25d8z2hYZKm0-swvH50fviENM-5JI8tGBVmgcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خوبه قبل گفتن یه ببخشید گفت
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106774" target="_blank">📅 20:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106772">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=pevxRj5g7Mtw3RFlpfRs8HDa2XMynv-e9-k28GEy_y_5GNFzs9WFtB2SX2vQpMSBo-34-wmIUf8R7_LLFfZQVYw1Ax1weL3zXlhlLgGcQgRjazcwNLVrnWB2N3UilUCNz5jN8dDun8WxKy-5SQorUOsJtqYAIdP1Y4TF3rhPVC4YHWTjKQkSud_4iVKI_-QEJiaS6O-aE3by6kgqBNVI3IvwQOKc3OMZAgEJEUtoxyNIWofwhBBv0Z3XMGclz81lLKYiYO0FHGoFoJDzbsKOUYqJv7oPzFylKQ5Q93-O1QVUMd3zOOTrekoRuL5b688glriKMCbjRfLywwtgkiLIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae6b91a252.mp4?token=pevxRj5g7Mtw3RFlpfRs8HDa2XMynv-e9-k28GEy_y_5GNFzs9WFtB2SX2vQpMSBo-34-wmIUf8R7_LLFfZQVYw1Ax1weL3zXlhlLgGcQgRjazcwNLVrnWB2N3UilUCNz5jN8dDun8WxKy-5SQorUOsJtqYAIdP1Y4TF3rhPVC4YHWTjKQkSud_4iVKI_-QEJiaS6O-aE3by6kgqBNVI3IvwQOKc3OMZAgEJEUtoxyNIWofwhBBv0Z3XMGclz81lLKYiYO0FHGoFoJDzbsKOUYqJv7oPzFylKQ5Q93-O1QVUMd3zOOTrekoRuL5b688glriKMCbjRfLywwtgkiLIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یه خونواده ایرانی عروسی گرفتن، بعد اسنوپ داگ رو به عنوان خواننده آوردن
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106772" target="_blank">📅 19:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106771">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=KYUuCVeyAqCjYSpH4gXR38YaCtpTeYtJ00BAVMyFG3blNybpsfvdi6pbjlqT62hEPWHQ9xJV9lF4vASq_6ZpOgC-5N_rJlLwURbphkkqOfqppZ2WwlD_Nuc-NyJfhPFJsEzbr1ihNOd3QUr1vBMCWlzlOXPR9rQRRjL03zjBKrUQPTxxgb9J4CrKaH8cUe0vLVMWyeGi4RFRhDRIM9j-wFi2UM11CAdLctJn-tqEafVUEoBJLritfV9AVYIctEQ4CVt77P1cDeLtZtfOYTt6u9WfDG42H79a7bmtVjBxvCU0Szjk446IXRzeeUlWdLZpLce6MO1n1gyehaRlEmjudZsygX3-0Y9lHd0eOz-DNT7ybN_CCdfqYLGitakyUzioFDa3wV74Yn2_YWm42VSjKJLFs4PMDCdPScSNYY7ZDi40mtP42EnFZy_LtyC7bRd3MVbKAn9lTtu5rw75C0cwG3VzyKOf0gueRFUiP8I6lgMYI9MlA_iyuwAq2fXLu2LSPIkaPILJDPWnrZdT3rv69hrUz6WAjygzFJG8AtTd_sn1WcEDKAfULnVbS5PQlHCKZm7mTw8E1QaOMsWHB38rv7uxlWbKvVIpRCTE1RiN0EnSf0YmZ7Pxk86WlDQH1fY9d_xBVdymYGbNTIE_Jt2zOXSFqwcMCa2hJV5j-GtZ4Qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd7aec7c83.mp4?token=KYUuCVeyAqCjYSpH4gXR38YaCtpTeYtJ00BAVMyFG3blNybpsfvdi6pbjlqT62hEPWHQ9xJV9lF4vASq_6ZpOgC-5N_rJlLwURbphkkqOfqppZ2WwlD_Nuc-NyJfhPFJsEzbr1ihNOd3QUr1vBMCWlzlOXPR9rQRRjL03zjBKrUQPTxxgb9J4CrKaH8cUe0vLVMWyeGi4RFRhDRIM9j-wFi2UM11CAdLctJn-tqEafVUEoBJLritfV9AVYIctEQ4CVt77P1cDeLtZtfOYTt6u9WfDG42H79a7bmtVjBxvCU0Szjk446IXRzeeUlWdLZpLce6MO1n1gyehaRlEmjudZsygX3-0Y9lHd0eOz-DNT7ybN_CCdfqYLGitakyUzioFDa3wV74Yn2_YWm42VSjKJLFs4PMDCdPScSNYY7ZDi40mtP42EnFZy_LtyC7bRd3MVbKAn9lTtu5rw75C0cwG3VzyKOf0gueRFUiP8I6lgMYI9MlA_iyuwAq2fXLu2LSPIkaPILJDPWnrZdT3rv69hrUz6WAjygzFJG8AtTd_sn1WcEDKAfULnVbS5PQlHCKZm7mTw8E1QaOMsWHB38rv7uxlWbKvVIpRCTE1RiN0EnSf0YmZ7Pxk86WlDQH1fY9d_xBVdymYGbNTIE_Jt2zOXSFqwcMCa2hJV5j-GtZ4Qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇮🇷
۸ سال پیش در چنین روزی، کامبک پرسپولیس مقابل الدحیل. اون دوران الدحیل تو ۵۱ بازی فقط یک باخت داشت که اونم جلو پرسپولیس برانکو بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106771" target="_blank">📅 19:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106770">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=OIT9eFkBccMD3g87sOdVnX952kajE94CQILm_Ddc4eMQZ4tZ2npex3FDiQFUqIfr5RklH-UDqxHIvIsNsCWKZsMzoyy8etTrZCq2X3I9XJfIQyXFLBG5iiE7_0Wq5bkKoz_YVtxErJQiK3Lr-p51lLx3NH0CNn8SvgYP6zABXlzpvtEalCOWU0FUJRdqGa0yFvkjUCeQJHELGgnUzGkoZ-aJVu5gO8UY1LbuZAm9Eb-yumYkyifkHwvtGKr8YJ5zDbIVHfz1cOc2npiqM3DQI47mHLj-cSqdTjBLPARvcTgEfhGilrC3n4IMoK8Woo14ikMCfiwnOvMIk6ijOmFLxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5345b9e16.mp4?token=OIT9eFkBccMD3g87sOdVnX952kajE94CQILm_Ddc4eMQZ4tZ2npex3FDiQFUqIfr5RklH-UDqxHIvIsNsCWKZsMzoyy8etTrZCq2X3I9XJfIQyXFLBG5iiE7_0Wq5bkKoz_YVtxErJQiK3Lr-p51lLx3NH0CNn8SvgYP6zABXlzpvtEalCOWU0FUJRdqGa0yFvkjUCeQJHELGgnUzGkoZ-aJVu5gO8UY1LbuZAm9Eb-yumYkyifkHwvtGKr8YJ5zDbIVHfz1cOc2npiqM3DQI47mHLj-cSqdTjBLPARvcTgEfhGilrC3n4IMoK8Woo14ikMCfiwnOvMIk6ijOmFLxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایانِ عصر خامس رودریگز در تیم‌ملی کلمبیا.
💔
🇨🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106770" target="_blank">📅 18:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106769">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=lPOiBel2WAHa6LpGHP3h0VHymox0j478ZuVt1EJ1424yXXMZ40YqF2-exGKEIhjOQbxuAkTlPPuDoRuU276h7jqcPLvKIgEDo_Nl1i-bBR0IgB3DbBxMUzLEjUbYxV9J6TGRBDZKHHRPfPZnSTcHJUaD_Sqx4P6c37BH4GrOAyQ4d2y-KIey1aR0DM1xAjHxZd-HD-3olr-x4DbMEp9QlMBN6Jj3oeovAko_hrv8XnQ3BmSlDSY-JpR2Ve-3Qkwsge-_SjWbsPjaPkHk6BEEuPJ2BDdfngV27USnwxdGAj0FyndTteb2VrzRhRkd2fgIMZXSmij9UM3GyBJaesWScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9692b0808.mp4?token=lPOiBel2WAHa6LpGHP3h0VHymox0j478ZuVt1EJ1424yXXMZ40YqF2-exGKEIhjOQbxuAkTlPPuDoRuU276h7jqcPLvKIgEDo_Nl1i-bBR0IgB3DbBxMUzLEjUbYxV9J6TGRBDZKHHRPfPZnSTcHJUaD_Sqx4P6c37BH4GrOAyQ4d2y-KIey1aR0DM1xAjHxZd-HD-3olr-x4DbMEp9QlMBN6Jj3oeovAko_hrv8XnQ3BmSlDSY-JpR2Ve-3Qkwsge-_SjWbsPjaPkHk6BEEuPJ2BDdfngV27USnwxdGAj0FyndTteb2VrzRhRkd2fgIMZXSmij9UM3GyBJaesWScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
بابک‌مرادی بازیکن سابق استقلال: ذهن فرهاد مجیدی را خراب کردند؛ خیلی آدم خوبیه اما یه دستیار مرموز و بی‌شرف در استقلال داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106769" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106768">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTc1m38lIfsxFfTqHs6TKODTM3QZXgaQFrNFj74q3TLVNOEsX3SQIOSrK-eGqR7U3r7EmVDblqrXL5nN4b0sHaRSWEn6wVpQAZ_aKlUkCFTNTgUD1rg6fnqyB3eDm_2Znlew04lUg5DG9bBUGW47bmFN-O-G-FCMZjm9o_UPTq8FPhYHhx14Plb77m_CL9MLSJ5HExXMIaSFI0lOCZPWjX6cshY2pNtAqey2Z0Jm7NJ5_UgcGC4GdwHaAxtbSCExYe_djnsvRcINocms-rn-GtjQLW0HO4DvLFXR6Q0naWxTgjlUoOJi58WQPQoWBoJCBIdn5T9h2h-Ujgpk1orgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
برنامه سوپرجام اسپانیا 2027 اعلام شد
نیمه‌نهایی اول
🇪🇸
بارسلونا_ اتلتیکومادرید
🇪🇸
⚽️
13 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
نیمه‌نهایی دوم
🇪🇸
رئال سوسیداد _ رئال مادرید
🇪🇸
⚽️
14 بهمن 1405
⏰
ساعت 23:30 به وقت ایران
🇪🇸
فینال سوپرجام اسپانیا
⚽️
17 بهمن 1405
⏰
ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106768" target="_blank">📅 17:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106767">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=B5iavsDuMuY2zCEiS_GI9b_PIQZO72mmBR-fbk4WPo4IzhSODnrorI1WhrShH4rdjPjTFpwC_TFiR1ObbSiEvt7fvFme2KONxVQEbXq0T4Rc52K_tQzJ2JAwO-jQd7EulTLVnemvyhPCnEo-RyDIzCHjMsVag2sFZRocsVmmgOX92SLXZejil-BxQJeph6VcA2utbLPQtFyYRUCZpg9rHmt0AO2dMFX4yniYBRl0s54JvmVHf0pv8rlZp5DhQy4vVKqrU88ziC3oMMynz-uO7C60iU7AIfh0s1fvXHk08p70kEzQYXo-qyYngrTdbrw7jfegdSSnNm1ygTfRScFBrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d8b49aaa0.mp4?token=B5iavsDuMuY2zCEiS_GI9b_PIQZO72mmBR-fbk4WPo4IzhSODnrorI1WhrShH4rdjPjTFpwC_TFiR1ObbSiEvt7fvFme2KONxVQEbXq0T4Rc52K_tQzJ2JAwO-jQd7EulTLVnemvyhPCnEo-RyDIzCHjMsVag2sFZRocsVmmgOX92SLXZejil-BxQJeph6VcA2utbLPQtFyYRUCZpg9rHmt0AO2dMFX4yniYBRl0s54JvmVHf0pv8rlZp5DhQy4vVKqrU88ziC3oMMynz-uO7C60iU7AIfh0s1fvXHk08p70kEzQYXo-qyYngrTdbrw7jfegdSSnNm1ygTfRScFBrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
انتقاد جالب میثاقی به زمان‌بندی ارائه‌شده از سوی سازمان‌لیگ‌برای هفته‌های آتی لیگ‌برتر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106767" target="_blank">📅 17:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106764">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=qb_Uuha8_eXcQOKneCXpoEMqhzVE0KZT4KUmkJPdT46nF7tdyTxWNsTLiSf8ATluKfCsbwGhVjUAD7CsG3RQ14pQGQ9pFD-2D083lJ8btYxVCA1kz8QheApTCnI3FfanhW8yKGTydT_kUF7rQkJB1S7PhTxOw_n8_zbhfLj87SDv6PwNv5qMrpH1GCajYUtc0E5Vr_Cdef4iq4uuE9zPC7N47GnZpAps6Rzccw8KppaH00Scn0GXhBbvFXaLG70aCQSWRPFWl-Ix5iI9Ujvs3MhZitK2tCWuPnKyzs9wCFe5Z4OALp_3Fjs_u1DR7RHbfOoQln8lKwegVcul3KFr1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acdc40365b.mp4?token=qb_Uuha8_eXcQOKneCXpoEMqhzVE0KZT4KUmkJPdT46nF7tdyTxWNsTLiSf8ATluKfCsbwGhVjUAD7CsG3RQ14pQGQ9pFD-2D083lJ8btYxVCA1kz8QheApTCnI3FfanhW8yKGTydT_kUF7rQkJB1S7PhTxOw_n8_zbhfLj87SDv6PwNv5qMrpH1GCajYUtc0E5Vr_Cdef4iq4uuE9zPC7N47GnZpAps6Rzccw8KppaH00Scn0GXhBbvFXaLG70aCQSWRPFWl-Ix5iI9Ujvs3MhZitK2tCWuPnKyzs9wCFe5Z4OALp_3Fjs_u1DR7RHbfOoQln8lKwegVcul3KFr1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
واقعا چیشد که به اینجا رسیدیم که یه بازیکن فوتبال برای خودش آرزوی مرگ میکنه!
صحبت‌های تلخ بابک‌مرادی بازیکن سابق استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106764" target="_blank">📅 17:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106763">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFoR5F3fRu4aLSPtqS2DiPHEE0S19VACsCkla8hb7wDvOrn1rIBDzXgrRALOlVS-i3acAFPkzHwyKiDxECO768Cs1ZPq6zDbrg92OFBtw0uqlWV9gZqb5rGZeIdyr0nWT8KY-tSz0nmkQMum_XBlI-SD9CtoBCC8PJQn0Roku8d-hOA_mYuJQA_B56OCB4UYKgmIFvNpdJvc4Mi1WTv4CpLG9_m8RdoYprp8HlSVGnb-i1j6l2iXruxQAG1V5plUPpdOk2xGEBYDUTkl2FmrjHHw_2gOem3nAKAKn-tl0_V4Uo_geDrUjxICANPfrqoQVu9DQ-d1z9bLCMBkBTeJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📊
🥶
کیلیان‌امباپه از زمان حضور در لالیگا به تمامی تیم‌های حاضر در این لیگ گلزنی کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106763" target="_blank">📅 16:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106762">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=kSc_JN-ZfRmCiCDcdJXCXSIvfPGURvbkT2AOZL6HGzUTMg_4GSJd3-8_PQma0FLUr0tgOGA9CRKrHEcPfkKePH3qlHmYHvKeCd9ZN416fVd9Z9zz9U1PMKcTwAegryw221UfTTxEaN6kR7_gtTnU0DN3yGt-W-4r3lkOnV2Lc7PRNiFaCVasgu3sPXgVC8ej1FOYL81KgSD5uavoUex5jrPULrjnj96mjCHGW7QQnZpynhU2HVFPtysoksBP-EUd6LFJDILTIwq0zlD_vwAtoaupTx3A-Zcw1v5HJpTUe7Jk6KR6MaLUJJjZ7iTmeXDjhl5bGLeM0GGJ4I8Kj4uA5wnneTHw-qMsfalTolqGiMR2R2OWMtGtU1IfG0TdQ2ZcjZFE_oJMIUqIvbE5qeGIEB7ZDXxTEi3eV3rlCbUNg1eCP9XUGdF9E_vWMs3K5lQpFRwoLYvvShKy1hjckH0hAh99OJKx8huLYN9HOvLSVmw-D2AVG4T0YB77lwNtemIbZy1SovYBDtNO0eGBw1M6LnvKyb_M37Xm910vAouOhH_ptSyMg3hVmTAkAj4icmGfWCDivyCcXYPq-Vu4SItLh40tCufwrNeY7R_El74fCUTGsFwwVoQQflszu3puFyfVudDQEk0_MB5g0vJMHAB08H3EN1CPGSzqfX7h_x1TYxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db11bb42ef.mp4?token=kSc_JN-ZfRmCiCDcdJXCXSIvfPGURvbkT2AOZL6HGzUTMg_4GSJd3-8_PQma0FLUr0tgOGA9CRKrHEcPfkKePH3qlHmYHvKeCd9ZN416fVd9Z9zz9U1PMKcTwAegryw221UfTTxEaN6kR7_gtTnU0DN3yGt-W-4r3lkOnV2Lc7PRNiFaCVasgu3sPXgVC8ej1FOYL81KgSD5uavoUex5jrPULrjnj96mjCHGW7QQnZpynhU2HVFPtysoksBP-EUd6LFJDILTIwq0zlD_vwAtoaupTx3A-Zcw1v5HJpTUe7Jk6KR6MaLUJJjZ7iTmeXDjhl5bGLeM0GGJ4I8Kj4uA5wnneTHw-qMsfalTolqGiMR2R2OWMtGtU1IfG0TdQ2ZcjZFE_oJMIUqIvbE5qeGIEB7ZDXxTEi3eV3rlCbUNg1eCP9XUGdF9E_vWMs3K5lQpFRwoLYvvShKy1hjckH0hAh99OJKx8huLYN9HOvLSVmw-D2AVG4T0YB77lwNtemIbZy1SovYBDtNO0eGBw1M6LnvKyb_M37Xm910vAouOhH_ptSyMg3hVmTAkAj4icmGfWCDivyCcXYPq-Vu4SItLh40tCufwrNeY7R_El74fCUTGsFwwVoQQflszu3puFyfVudDQEk0_MB5g0vJMHAB08H3EN1CPGSzqfX7h_x1TYxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎙
رست‌دیفنس در فوتبال از زبان رسول‌ مجیدی از معدود مجریان باسواد صداوسیما؛ خیلی جالب و شنیدنی برای عاشقان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106762" target="_blank">📅 16:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106761">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106761" target="_blank">📅 16:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106760">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915324d20d.mp4?token=J9HikILXa3qw4XR43l3PpcpdZ2i99bxffnJHXZ5NIWsRhrPpmTPAoIC7RfRU2r_Png1iC2fUbS82C7VQPqtTHKV9-K-d2CLy6SRrmrBlPL28jwscvA0YqB22xPKy53oxlK8YkJcQXKt4nrsoxodcjGpZwKbso2f1butNHiyG_buq0uoOGyRTIqDRa3x2Vwq8cAH0hzFsU6F8kRaFe4JR8BCWcCuFprxlibCJ6Tda07kxtxevNul4f5jLwugmv55XQOgZfKnyLq4Vz4EX1xlDLeFOvslpMLIpJcb1j-aBQi9VhbC6RVlsD5LQMBKuabPJJOt0JXk3fx670YrhKEG9hbKYj700fPTptbg5PcGoAgnKec7xr3cN47yg8sVB7vWKZZtcRUx9-hNeBy0sxi1hGCtKkJXH0u7OzW-zoENniyQXOmn68TTHCz_s5NksY01e5HsNDIbMTmeW6uX7MpVNze2DQrds2-zJi9sxhbYJWUNDpPQeuj77Q6lbUGTQM_UxXltf-3MGIj-sA-rK-aNKFsw6lU-jpvieL6Sq32y1S-8rQaJITdXgx4p2OhJ6K_7LznS8K6PnLY2a0x_UDL3ipv0cay3qmCX10KhbPR4elhFBP19OZhn7tGvQoV2L9I5LP0Z-Luo3x4LLw_t4EMcO7LINvfsPfDthnjqsreGnoec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از راکت‌های تماشایی سوبوسلای در لیورپول؛ واقعا عجب گل‌هایی زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106760" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106759">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8wuGrlCIxD5BwsMkvDWkhEWKQETi1oBsJpmk4Eo6rW1ZFLO7AL3nZ6DMjkyZdhkE5MIYXHxin0kjoF4mp9zEjH359fj8XVXweIo2tfZW8tuyfmqcoJWSw1AvMs6AhSxDvoct2CtO6wWF30BFPZ5yL3lis7LCNZwmp5uFKJ-_-AK_AqJNipTGPX0IAk7sVoEEwnx0kW0QYQxJyAn_mNW671CyYuEvUD1lkqyXMCL4fSEw8I4weBXaOKPdlVsG8h9bZuJ8NK1vsR0blzUK63Nh7lNHfyyRyZowislpLZF5NLO6ZJYGirBWvZSLtZnpQpZaDFkxcE3POH0rxAhEenk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
سال 2018 که فرانسه قهرمان جام جهانی شد، کل مردم فرانسه برای امباپه دعای خیر کردن و نتیجه دعاهاشون شد این بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106759" target="_blank">📅 15:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106758">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=N6Ej57aYt9P55jzygKTg6166W5dBOyZRGKaQ9H9YFmUpcCYvITyC13WCDG-rOTmGWCyIO_z9TsYZ6w7SRG_QeUkx1Cjq64GzxOCxAasg6t5FrJQ7HzD2jNmZn2rI_1gWCWXIk6zQ4_PX4rrctmn36-oNrahmkLxqUeSIcTC6dlNY-28nZ1UEVhRdjnats-u2jklnnowZ-6Be3yJf7eL-AjKQF2GFDn0DtWpUBPD0mEosRF-g7vautXlnTsoDvVVL-qY8TtkKqNN_0UDLYOB0gIXahlkyPkIPO8sJ_nSvDKXMMU9S6SumDbNG0wW1T6HTpTSE2cVMFUKrXL_mYJpetiVoQXuFWYwnwqd0tXOWd_j-S6vSGDxxBIGOCxX-INL2-tgAxLSH8kk9EHC5EV598rdpbbEWSn3io6GedTyIpb9zkp2qyEyWaIFrOy7Gm2MJt0RfNeDJdGQp8AOwFFuB4iJzSRIGo4KqkYtd6p9Ysf-K8X1ZcVtVjBPxarie39LeDyRQoNwSi8gpfU1wuKjMsJbr98rJOk7u1zpL_GPgLijWft90nq3UTPLW74fBIZMQ-ja8qsu_0luggOiNqdbEKgjxBxbnVYVd6zemzPHJR7ND1RcWrORIo3BaJCytR2z137EUzll41J2UntSQbT9ovwgfTE-RClvxqBY4ym-hG94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab14c70f7.mp4?token=N6Ej57aYt9P55jzygKTg6166W5dBOyZRGKaQ9H9YFmUpcCYvITyC13WCDG-rOTmGWCyIO_z9TsYZ6w7SRG_QeUkx1Cjq64GzxOCxAasg6t5FrJQ7HzD2jNmZn2rI_1gWCWXIk6zQ4_PX4rrctmn36-oNrahmkLxqUeSIcTC6dlNY-28nZ1UEVhRdjnats-u2jklnnowZ-6Be3yJf7eL-AjKQF2GFDn0DtWpUBPD0mEosRF-g7vautXlnTsoDvVVL-qY8TtkKqNN_0UDLYOB0gIXahlkyPkIPO8sJ_nSvDKXMMU9S6SumDbNG0wW1T6HTpTSE2cVMFUKrXL_mYJpetiVoQXuFWYwnwqd0tXOWd_j-S6vSGDxxBIGOCxX-INL2-tgAxLSH8kk9EHC5EV598rdpbbEWSn3io6GedTyIpb9zkp2qyEyWaIFrOy7Gm2MJt0RfNeDJdGQp8AOwFFuB4iJzSRIGo4KqkYtd6p9Ysf-K8X1ZcVtVjBPxarie39LeDyRQoNwSi8gpfU1wuKjMsJbr98rJOk7u1zpL_GPgLijWft90nq3UTPLW74fBIZMQ-ja8qsu_0luggOiNqdbEKgjxBxbnVYVd6zemzPHJR7ND1RcWrORIo3BaJCytR2z137EUzll41J2UntSQbT9ovwgfTE-RClvxqBY4ym-hG94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپر گل پریشب سوبوسلای به تاتنهام رو از این زاویه باشگاه لیورپول ببینید
🤌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106758" target="_blank">📅 15:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106757">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2j9e73iacSFhRYJJKkgfYoFFaXAw7SJxSKzv9Gxinukt_j-JUdcDBSqlA6r4YuK1p1aa4-9KQazFXGjqtUT3KrcqL40dRmfzHteU2ym3R1U9R3fsDnl1ENjT8eSivsn9_NQyNIMlomZ0tQdvqemNS1XAgLpt7K066BR3WscuwzxtQdod-JcJuUiAzTHYIX2uFO1rUP2dnK2yHhRU3j45NwQZBzzt6PC-Mv3BYwJgVqh2YRrvjshtq1LOammaAnMtacvlloUJoQBOe4AJAMObhgBVQ8m1R70qNeQuPhnpbmWOSbs37KCOiJ3XU2faI2zlI5L1tEH4nwrTkUPa-SPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙
کیلیان امباپه: "جایزه توپ طلایی؟
به نظر من، امسال زمان مناسبی برای من است تا این جایزه را ببرم.
بهترین کسی که از من دفاع می‌کند، پای من است.
هر چه که بگویم، مهم‌ترین چیز برای من این است که توپ طلایی دوباره به رئال مادرید برگردد. باید به سانتیاگو برنابئو، به هواداران مادرید، بازگردد تا شادی را به قلب همه آنها بازگرداند.
آنها بیشتر از هر کس دیگری، شایسته این هستند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106757" target="_blank">📅 14:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106756">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=FF6msfiuC1pAl55ZIkJr_ZI6iy1BCF-5UN8uPXLW0A2AgP7MiSkhwvojdHXCMr_zW-39hF646H1hx_DiPWrSTgRX4xccnwJD0YGjCFV2xwkoq33e5yzjomwdJo8gcDQQckLaC5Xmwfshlxt8Fm1Jy1I65P3TNXkEmmBJScsublww9OqqoGyrO73G4QVvmdQ4vtGJceUjcdcYV0cLQubEIWrYCbUSCXXILoGcHox8CR9_ywvKL6tMNKj1KKx2J4PfAmyr60TZynaPKxB8NVZeZszk7MaR5xHvVF0h1nKLHXr4NuzLbkm4JrQ5GyS_BKqlOlSr9UzS6J1bwAx9hPidXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758a2aee2e.mp4?token=FF6msfiuC1pAl55ZIkJr_ZI6iy1BCF-5UN8uPXLW0A2AgP7MiSkhwvojdHXCMr_zW-39hF646H1hx_DiPWrSTgRX4xccnwJD0YGjCFV2xwkoq33e5yzjomwdJo8gcDQQckLaC5Xmwfshlxt8Fm1Jy1I65P3TNXkEmmBJScsublww9OqqoGyrO73G4QVvmdQ4vtGJceUjcdcYV0cLQubEIWrYCbUSCXXILoGcHox8CR9_ywvKL6tMNKj1KKx2J4PfAmyr60TZynaPKxB8NVZeZszk7MaR5xHvVF0h1nKLHXr4NuzLbkm4JrQ5GyS_BKqlOlSr9UzS6J1bwAx9hPidXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇮🇷
🇮🇷
مقایسه فالوورهای ده ستاره سرخابی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106756" target="_blank">📅 14:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106755">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeirErzKf8LyJx1xTgRTceok17VBdZgCQvcLeGvquty4qiXUgsX3HkkMLBAjLU_YN1pLLmVf_qZSZ5-X7SlQ0_jH2db29eGZcfTQl0dleldq36DNqgVoy71ebVsAtjlp_S_rvEafTqcVetU0ir_rPlM-hS4AcCGO8JHIikEyyGEKd4Sl7-ykcy_pS-lCZtFCwZH1XFtyx4Ba5aX0EWIhfj3EcvwVO2iceC4czr3kO75jaoFaL84Gi0m-qjDefVA_rBhp3iNiliKVbslOzb2yyauGArRb0Z9fRay3IQroqM9cn8MBbHDgG0SvySdvk2K___rVR1OArDesIRxP8gQP4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
شبنم‌علیخانی کاپیتان تیم‌ملی والیبال بانوان ایران به تیم استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106755" target="_blank">📅 13:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106754">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=FgLYk1PlP_4d8TA2DDpKf-jgxBHDcN-UUPV-mczTXo7RjxLJmyDiBsMB1wjyFePpZ5GFM8dCv3F3cfvHTFVCMEaDNL7Ur3pNw-NUJEWOUPZNq_gB3x3ykhNDmPKZB-Vs1EF0G3wZSxEY-z_viZzcORFEV2el7IeZmkOksPZ2AuiwNerD0KA_gDHBrWRhRF5LPmC8nB2doQQICBoT6yOHWi4VuGTB0jK2aItVjsg4YeVpY6bS5RDs9nJbgOyAiCa8zHXEvTlxogp0Pl6I-fbKeyQ48Z1NlhNXwdx8oIIw0fVMWCUVhrDPrHKJS2mmJiPcTCW5ZnGyFPlfaA9fyUTmyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=FgLYk1PlP_4d8TA2DDpKf-jgxBHDcN-UUPV-mczTXo7RjxLJmyDiBsMB1wjyFePpZ5GFM8dCv3F3cfvHTFVCMEaDNL7Ur3pNw-NUJEWOUPZNq_gB3x3ykhNDmPKZB-Vs1EF0G3wZSxEY-z_viZzcORFEV2el7IeZmkOksPZ2AuiwNerD0KA_gDHBrWRhRF5LPmC8nB2doQQICBoT6yOHWi4VuGTB0jK2aItVjsg4YeVpY6bS5RDs9nJbgOyAiCa8zHXEvTlxogp0Pl6I-fbKeyQ48Z1NlhNXwdx8oIIw0fVMWCUVhrDPrHKJS2mmJiPcTCW5ZnGyFPlfaA9fyUTmyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106754" target="_blank">📅 13:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106753">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=lstSW5wmiuLN0vVc535sy8v5v1xsKcAFHJJ3CNc5vlBDdmpa12ar09Fr-iPrev4qUt9E043iMfFrjKbPpzlUYdk7oyrpi0Ost2ibl571hlsbvDBi7XdHP2SnGmM0NlvhpnJmfZhZBwIzDDSWy5y3t68Unc5rPel9yZjfeyj2KGhuazvPMKZSdZOWsX2TEUb9nxDgno97p85z8mT-AlXCQItF25kBZBHpYUEq8t9tNY8SPkA1iTkpo_lcD6w5_xbM2K8HHPS9e5kBWTWp4oeBjP4rNIpWwSrCchNRnso9pPmu1zowEWae5qzYcDYTdGws0w4qmu0lXY-PIh5S_Qlx-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2975c02c1e.mp4?token=lstSW5wmiuLN0vVc535sy8v5v1xsKcAFHJJ3CNc5vlBDdmpa12ar09Fr-iPrev4qUt9E043iMfFrjKbPpzlUYdk7oyrpi0Ost2ibl571hlsbvDBi7XdHP2SnGmM0NlvhpnJmfZhZBwIzDDSWy5y3t68Unc5rPel9yZjfeyj2KGhuazvPMKZSdZOWsX2TEUb9nxDgno97p85z8mT-AlXCQItF25kBZBHpYUEq8t9tNY8SPkA1iTkpo_lcD6w5_xbM2K8HHPS9e5kBWTWp4oeBjP4rNIpWwSrCchNRnso9pPmu1zowEWae5qzYcDYTdGws0w4qmu0lXY-PIh5S_Qlx-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
▶️
✅
بهترین مکمل برای جایگزین کردن قهوه قبل از تمرین چیه؟ به روایت استاد هانی‌رامبد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106753" target="_blank">📅 13:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106752">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMQJmloHrXirS7yQ5JHhJD0UXsRtdqu39RHOnGsHCUFD-gsDELm42OmHWsb2aGCRvXOWIRRpsc_prXrmzzfYoAC1J7KsGNFVmWQMNDVwHQl_yq9SXgmNGlIWuPS7HfMbmffwSHWHjALXYfLKz2CihJBDNk2t4tMd1xj7qlS6et1ROe9GHPXB--2RHu8QR-lzZ2op7E5NkuSloRAHEX580DCaRqshjd9xgUw9IpdcabNDmbSxF4knJn3ZXOLdjUSLKSLcbJPajNjbX5KtX9RXUeHoNP-p5wcreH4W-axfrGoHyAg7UMNXJK1GK_iTaJqAbs85KnJG0G2XHfuixQAtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106752" target="_blank">📅 13:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106751">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zxj67lE63otZXSa_vth3CfskZ5-y2yf56TKPADwN1zub2Ry92_LiMVD13KKj-XQmxKR_4fVdWGLF4bf5RYD2Kw4qAy3afarYJlGT8ngoKHheKIXFe4vEVdaNzv7t4N4zozDfmEd0wprM3Bv_AeqsJYi-4y_1FNNg141rEty3Yz701xwfiVgnm7NXnt4CTiOJJ-dWfFT-6lQj1nbeQLCvJZUYmG2LcKYzNhzoDdgnRwPbuiX3isBdssFoQ4ABI1Qadu6p96WzkQLZCQh_lS7vhstCgp4FWHGMovI4n9k3b5-uCuyJ5hTSMsfQ6atJF0LDgDbC1BJrU_qzYLaTaPT_8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇮🇷
با اعلام کمیته انضباطی فدراسیون فوتبال، شکایت پرسپولیس از استقلال بابت یاسر‌آسانی رد شد. سرخپوشان پرونده را در CAS پیگیری خواهند کرد و به تیم‌های عربی نیز کمک حقوقی خواهند داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106751" target="_blank">📅 12:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106750">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob15GmbvocqW8WesZtUTUyFBkHueqQWifWuJ2fXYLbilaz0p0APa99MDh3AXF7NxMTzvDCVR_gsD4AEWypcmtvNwJmNanfycm8WDu4WafxuINcBumNLvzdMbo36ARW2P7BXuQCpjcxfhmJMwcDbVo8Noq7uRJJWoqmRyIm2GjhCxEMoBZAMlJxGUYx8NwdFyc0WYhAKZm4lrsyQX4xMSNJhfcSFfHKbniRr85qCfzpgA_UB3Dpu2fZ9FiXbKYW6ys1gDmQPgkns9FwjlpMuqUsHymTt2JgFoIjLYe4zCnGqsVmqHpauoxud-KBGCrlav5RTHkF0fOYXffZlq3uJCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🫣
بالاخره روز پسر شد
😁
👍
‏در تقویم هخامنشی روز ۲۶ شهریور روز تولد کمبوجیه پسر كوروش بزرگ می باشد و این روز را در ایران روز پسر نامیدند. برای پسران عزیز زندگیتون بفرستید که حداقل تو این وضعیت کمی خوشحال بشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106750" target="_blank">📅 12:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106749">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuZvrsbX5jDvY4yFHiA4547O-KjAuFI5jijoujPMF9TMSaVPKTS0vnhKSW9xEIAbKnqT6XzKpdgiplVmQtvtHshpNg-oN_xNhW-GwNTKzzXbYgBx0DB6vSGM-3dMpPje2kiej88YAJzAJ8rAUdP48eFSdbZYCa1FW6m7EpyhYLwRxmeNXEabkeOslyL953QTSHXrbsZ1XUFNcw4JeaHpPM80iXCMiyUh2wYJAUbp9O8Tk4jPts7LSZH5Gl8zyQO7_ar3idHKjopAFde4b-z75qyI_yqQs2FAA89GDbdkPK9tnWRy7BK-_F3F9IQY6xrhuMjUC1FrsdrixID197n3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
💵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بهداد اقبالی میلیاردر ایرانی به طور کامل سهام باشگاه چلسی انگلیس رو خرید و الان تیم کامل برای این آدمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106749" target="_blank">📅 12:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106748">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎙
🐐
🟣
دیوید بکام بعد قهرمانی دیشب تیمش:
🔺
هنوز باورم نمی‌شه مسی اینجاست و برای اینتر میامی بازی می‌کنه؛ برای همین هر وقت بتونم می‌رم سر تمرین تا ببینمش. به نظر من، با وجود بازیکنای بزرگی مثل هری کین، کیلیان امباپه، جود بلینگام و سایر نامزدهای توپ طلا، مسی باید این جایزه رو ببره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106748" target="_blank">📅 12:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106747">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb69509038.mp4?token=Btd-tKOPKiaNWWoHIqHUbfsK8iPQdGT1leltO5KzUSW4geiI8BIK-Idfrq5RRfxMQ0NszNLUyW7PDo10UzFGgjQtAazTRXsZ-P9Mpd7AwnwiPVCooOm2Ebbghgak1SVWnna3gs7dZMxBWbmV6-SMbU0C4UXwbkrEt9Bjz_aQitC-i3rG1VE7Zin9uX8hiOfOjTHhS0QSLXbEPDcFGkuWF5XRAutKfM0txc7108AdaBf6yO0M6EeMwdGqeupfZiPzri9aqBEy-5wuabjEPSpXFAHsSaKn3LeaNBDnf18RQ5AZp5g_YvFHgaff2YsZDnOOX8vbdv9WXLcQpji1H5lFE7ez-5ye_j4eT-gTSBDUydNNk8QwEWHdn0GQILCko6j6MiEWl7-34wKiu2bg2pCWZIuLnwRhuDf2eqLc8m-ERVmSY9PjJ3yKszlgnQqbqZYWG50xNjZk-mNUHRg2OUIqoaGb4lhLNnaJ5iLNaWj6T5z05QTZa-S8PYSdWTY0TFvsmg6dK5a143DltykVF-2TjpzGTdJYG0cnLqNUjqI7eWNH5zkMdWXVcaWOOf1zwoHUhEC3iwPEzSyI3oYNz1rOOknUxmaFKQTgjtQZ79uC3jOw7nOUNj8dmiQ4fMQhA3B-jr2bMwI_u1ke8tcbiHUQHGdtNqdixKoIKC7RrjWz1XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb69509038.mp4?token=Btd-tKOPKiaNWWoHIqHUbfsK8iPQdGT1leltO5KzUSW4geiI8BIK-Idfrq5RRfxMQ0NszNLUyW7PDo10UzFGgjQtAazTRXsZ-P9Mpd7AwnwiPVCooOm2Ebbghgak1SVWnna3gs7dZMxBWbmV6-SMbU0C4UXwbkrEt9Bjz_aQitC-i3rG1VE7Zin9uX8hiOfOjTHhS0QSLXbEPDcFGkuWF5XRAutKfM0txc7108AdaBf6yO0M6EeMwdGqeupfZiPzri9aqBEy-5wuabjEPSpXFAHsSaKn3LeaNBDnf18RQ5AZp5g_YvFHgaff2YsZDnOOX8vbdv9WXLcQpji1H5lFE7ez-5ye_j4eT-gTSBDUydNNk8QwEWHdn0GQILCko6j6MiEWl7-34wKiu2bg2pCWZIuLnwRhuDf2eqLc8m-ERVmSY9PjJ3yKszlgnQqbqZYWG50xNjZk-mNUHRg2OUIqoaGb4lhLNnaJ5iLNaWj6T5z05QTZa-S8PYSdWTY0TFvsmg6dK5a143DltykVF-2TjpzGTdJYG0cnLqNUjqI7eWNH5zkMdWXVcaWOOf1zwoHUhEC3iwPEzSyI3oYNz1rOOknUxmaFKQTgjtQZ79uC3jOw7nOUNj8dmiQ4fMQhA3B-jr2bMwI_u1ke8tcbiHUQHGdtNqdixKoIKC7RrjWz1XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت دیشب نیوکمپ که هروقت بارندگی بشه اینجوری استادیوم به گوه‌خوردن میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106747" target="_blank">📅 11:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106746">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن،…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106746" target="_blank">📅 11:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106745">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEjVZv26wQp32HTE_oMerp8Rg4p4L9bCi2ojxJlb8BaEJDHxsglQUii6Tae-ldkuBANTF9NbUMaG9HO-R2Ax0UdhzBbp9ZPMgVSp3k7JqNZgRyI7-WpBMFZRgqjx2jt0RN9h0yT-IuvCxZHvq-eJP-phKceQZCtSrMGteXsum6IhAhQYaZH3DrhXnSgdDiyca5fHTZr3HoYc-nqh4RBRtmjutfVpPkR7Ct-lcau88eaZvdR9b9VrPJLO9gi5kJMTeARUOx2Ne6AIj55z-iily2a9G8fNeHX6IdEeF8kFqNRTI3WPlULsBNvUukGqG1_wnbcqEElOAwjK2diDNdXByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
اعلام فهرست بازیکنان لیگ برتری تیم ملی
🔵
علیرضا بیرانوند، سیدحسین حسینی، پیام نیازمند، محمد نادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمد مهدی زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، عارف حاجی‌عیدی، امید نورافکن، مهدی لیموچی، مهدی محبی و امیرحسین محمودی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106745" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106744">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=Hd1ZmZ9gKnEUcCSTjhNB4aRU5x0VRkq0SMLqJVt47njOGT2c-cTeRax7m-g24zyTxox-4_8Hh21_FGl6bS_hnMNDO3ZVlns7ObKSzxYOdaSQJD7059MqApd7M74BW8-InyGmipAqI86d6svTAFtyDCRErrVoe4vp76_glB0rfibFMWY5Yh5eQoKTEeYZ_VTAlvXm-s9ZyPErmwSmDU795OxOVTJ_zCT7yooNTZYEVJ00FOp96iCKTnTzlFoBPDPLIhH8gOTeD0-jM4DerhbA6wNzxWxsNXR12D5w6P5g8sX0lDs14O5XQtCF0khnsT4-DwsdFHJKP57Py542Hhn5M2mWJQlj8fsQGJSwAI3-jmlXDX-mi-ehlrZf0pMqWLqcA5ZEGsb_hQyxtLRtniyzyMLRMjddxvdPWyyRDDxl1HH1R-c7monetONkGWYC5LvJJOZWynBSIKyah7f3v0E0pt3f_8c2zVY9kMhlZ5mufT9h7YNNDWc-XsqcdwaSSYOp3t-aTQ1N-xQdMPBF9A7WxeqNUJmFLVcCWv4tR3eYLodj1pg--yt1PNVI2uXSjj-hsbi-EeYPWwmggug1ztPEXcINT92cg81p5TDmL9FYW3ti-z2uJqRjZ5fwWSId3r47msRDZXi6UKJO4COruv1urvFIJjfuDaaBLlm-GVRCzCI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b540a014a.mp4?token=Hd1ZmZ9gKnEUcCSTjhNB4aRU5x0VRkq0SMLqJVt47njOGT2c-cTeRax7m-g24zyTxox-4_8Hh21_FGl6bS_hnMNDO3ZVlns7ObKSzxYOdaSQJD7059MqApd7M74BW8-InyGmipAqI86d6svTAFtyDCRErrVoe4vp76_glB0rfibFMWY5Yh5eQoKTEeYZ_VTAlvXm-s9ZyPErmwSmDU795OxOVTJ_zCT7yooNTZYEVJ00FOp96iCKTnTzlFoBPDPLIhH8gOTeD0-jM4DerhbA6wNzxWxsNXR12D5w6P5g8sX0lDs14O5XQtCF0khnsT4-DwsdFHJKP57Py542Hhn5M2mWJQlj8fsQGJSwAI3-jmlXDX-mi-ehlrZf0pMqWLqcA5ZEGsb_hQyxtLRtniyzyMLRMjddxvdPWyyRDDxl1HH1R-c7monetONkGWYC5LvJJOZWynBSIKyah7f3v0E0pt3f_8c2zVY9kMhlZ5mufT9h7YNNDWc-XsqcdwaSSYOp3t-aTQ1N-xQdMPBF9A7WxeqNUJmFLVcCWv4tR3eYLodj1pg--yt1PNVI2uXSjj-hsbi-EeYPWwmggug1ztPEXcINT92cg81p5TDmL9FYW3ti-z2uJqRjZ5fwWSId3r47msRDZXi6UKJO4COruv1urvFIJjfuDaaBLlm-GVRCzCI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
آنچه در بازی دیشب بارسلونا رخ داد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106744" target="_blank">📅 11:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106743">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tlk4Mnod6ifhNFdfEsJpddGcPnJTN0VVpYeLcE6eKUU6SLIJZxTy9s8eQCOZfUgj5G2PgLrUwNTV6AUl84pGenzjeVE4uPzOEhVCdI_By6EKP0DD5mrdBIAXWJaN19CTSP2YLaEyA-SA7JtI3vStiKEsNf9RFhpcoO3Q2-HGlkii8d582-XzMes-SdUiLODC38eiHcPZ8S7wA42iriCTfel3P2c5T2znHQ6S_YrJ7yEDoZLkx03RjuJtsZ4jAv8WVHOXU69OhTLjS3mgRTeAKlowVjKZHCLet5HI3pccJOegNpP0ksOwWzJxqnsfzG4IZme8U70k0MguVLJkXvH9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
علی‌ضیا هم رسما با انتشار این عکس اعلام کرد که زید زده و دیگه سینگل و این‌چیزا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106743" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=l_cBiPtO6PFB2Rcr8LIl7Vs5U8-Zv8r14Pdsb5ecjFi4ZdRWsdz3RFdGOKwpSyF39nfG-E9B_d-G4Xc3yrZgz0GLcU7jnKWIz6xkoGs0btNdYjqfJSFYE89WsUjCjQJwW6U-3lLIEE8YSaqh30T1yDIALZ0YXAllVNcjmgGN0kjAqWcXOdF8yEW1_9nnei6no2cv3zgIAzsSdwRY5BI5GxLi6W_du1N5ZnxWMUMhK5e5fqmE0UHALKqggdCU8F_rmHe07dAEDmQr-ZEILGcGCf7drkx5L4l1S9TDdauSBsP2fCOwUSwSqtvMwZo4freuv0w8z1ExQNTNKETieaXnGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3ee373ec.mp4?token=l_cBiPtO6PFB2Rcr8LIl7Vs5U8-Zv8r14Pdsb5ecjFi4ZdRWsdz3RFdGOKwpSyF39nfG-E9B_d-G4Xc3yrZgz0GLcU7jnKWIz6xkoGs0btNdYjqfJSFYE89WsUjCjQJwW6U-3lLIEE8YSaqh30T1yDIALZ0YXAllVNcjmgGN0kjAqWcXOdF8yEW1_9nnei6no2cv3zgIAzsSdwRY5BI5GxLi6W_du1N5ZnxWMUMhK5e5fqmE0UHALKqggdCU8F_rmHe07dAEDmQr-ZEILGcGCf7drkx5L4l1S9TDdauSBsP2fCOwUSwSqtvMwZo4freuv0w8z1ExQNTNKETieaXnGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
از عجایب فوتبال ایران؛ دیروز حین بازی تیم بعثت کرمانشاه و نفت‌وگاز گچساران یه نفر درب اتاق داوران رو شکسته و تمام وسایل قیمتی تیم داوری رو دزدیده
😐
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106740" target="_blank">📅 10:40 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
