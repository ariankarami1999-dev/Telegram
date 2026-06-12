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
<img src="https://cdn5.telesco.pe/file/Cma3ZbAAk513kQ8tQvaGzZrD5R_o1snNfZmEamQr3sXUGZ2vLuDMoE8xUp7II6gDfjdlvOp5k5nJkKImFx_vOR8OcEsxKYL1Pe4x123V3KKawuueCwfwLBJ3yicHXLqQLpn7Yv5mZvxL4coOTxBnzX1SBzNVMmKujf7Wcoud4Iqwbbo_Dh0p7CaJUnrMhBMrAuL1_4aAKUVvTExF_YEgjhcbN_n_GAj73bM751lMxTifE6mf0lITj9BjM2gjzpQ8aURY3SS-WY46UNRACeM8OqK9Fgoeqr1HgpI1XPBFji3mZnn1EzcPM0qIhMw6MjXpqDR3SCndDVbsFHSWhOZ2Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 459K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
<hr>

<div class="tg-post" id="msg-92435">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZF953ukFrXePehMcTPZA2oK2BM0xQ3VKLLSENg_O_vZhyuNlhEI4Mq_OoKmm4YghPeY2rIAYTQDSgWqPHESlhcsY-r4AIVnhSeEuwol0TcwsMMflPiHUbp_Nwq-0Ku7csJE77L0kIOsNG7g8kmMNO3vAj2GgZm18zD5Hu_--3t7AEJMt4QmPS3N0eO6ep2js5CULKaXdQ4za0aiyTCWv6f2IQF2rzWzU7axkXfBpjatxdKk3t3q8BlQzB2zZnxrhvkeDtYtB1KKk9HRUkEXYHsZyKM4PHbgFomxGkwmbVvoRno3uoQKrYWUjX0k7sKjjUa9l1a8khwMBOEbzPwXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کانادا بالاخره در جام‌جهانی نباخت!؛ میزبان مسابقات در بازی افتتاحیه دوم مقابل تماشاگرانش به تساوی رضایت داد!
🇨🇦
کانادا
😃
-
😃
بوسنی‌وهرزگووین
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/Futball180TV/92435" target="_blank">📅 00:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92434">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#فکت
🇨🇦
کانادا اولین مساوی تاریخش رو تو جام جهانی گرفت همرو باخته بود تو بازیای قبلی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/92434" target="_blank">📅 00:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92433">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdWtnqBBKDOIYus1VllaHoo-u3G2wHMyJ_cCZRAwMp5YAyrHfugCtdy-3smkHSXxvKC9xCTBXy4lXHnHG7xXgiRq7vfg6x3TL3PxI6VZcmoY-hXaYQqpQApAtjXwebvwROtgWOrFWClTKHIAH-y7vEkfVK7FRF3Gee0SjhTvhZjVfuSvkiOkkc85EClee_lps6xesrjUAs4FfdF0IsVPRjJdCL5llwxp3-qI0Ya5yRMibYrjrLA9lPyfa8NoPuxt2a9xAz77RWpxpHgiALMDQ_OBa_ym3pJ8nljoZeq6QfOSOQetmBWE3wcwRo6oB_Sd4Zgqr7C9Wq_aXhTW1LervA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|کانادا بالاخره در جام‌جهانی نباخت!؛ میزبان مسابقات در بازی افتتاحیه دوم مقابل تماشاگرانش به تساوی رضایت داد!
🇨🇦
کانادا
😃
-
😃
بوسنی‌وهرزگووین
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/92433" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92432">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrreH3y8uFTw-TN594KBO5u27CS1TrWdZ99xdYBixQrS-w3eFCjsDdc_fdWcWlJJwfUOBzpG4ZxgZQk1vhDsANtL-pRYNa0wMnrNYDIBEc5OlKsSTT_T0PQL9Vfp1N7Jb0C30Y1QXq9q6OfFV6YBFObBefS-7nqT1rzyRSwRyEl4NxnTJbZhGr5dnlpS-xR7PITDFyJ5LxM5C5eqXb4skCClWpbejTzB7E_cGmy8U2EVGLU-l6Ju29eFOl4wckagIpkGQ4tCUC5Gw2t_4zmG2pevV8qnNc5WjAReyy_8WyYOa2JECY24bzZ8uKCSQeFd-oXQoVPxgBBxDxhBbYI6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل
🇧🇷
-
🇲🇦
مراکش
🏆
جام جهانی ۲۰۲۶ - گروه C
⏰
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه متلایف
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
- برزیل پرافتخارترین تیم جام جهانی با
۵
قهرمانی است و در همه ادوار جام حضور داشته است.
- برزیل در جام جهانی ۲۰۲۲ از گروه خود صعود کرد و در مرحله
یک‌چهارم‌نهایی
در مقابل کرواسی شکست خورد.
- مراکش در شش دوره جام جهانی حضور داشته و بهترین عملکرد این تیم کسب مقام
چهارمی
در ۲۰۲۲ می‌باشد.
- مراکش در جام جهانی ۲۰۲۲ با حذف اسپانیا و پرتغال به
نیمه‌نهایی
رسید و یک شگفتی بزرگ خلق کرد.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/92432" target="_blank">📅 00:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd9wns6g-O1wlXyFIsbDKy7trdwanunczbVP-3rEPl-U0Jo5pQl2tz5NoaulFt-2eTo_QsVJqWZGv9q-OfcTRemWNgysQszisWWZxf5SQJD8U1uGo3z7vIkg01RBrsjy5gi3Wjvb3Y-V9kansnIkKwzGS2YHwtJGx1krxvR3_EMvGOGllcVw6U37gDyODdfillD22VEqrDyzylbxnsqQE5hCpAHemEr0JJsj-_DeCBJ5d284p6vwEZzdZI6jEwkGaOZ5N-ZoaX9K3gtmg8CwkBw4qimB2jiUWaAJwpFiWvizoWeBSO33x6kSX3SLh9QDwW8pjqhzithKheiv8OaDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/92431" target="_blank">📅 00:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsuqLp23T9mvWV7ldq-q5h8MhxnjcBku4CgLn2zOUqU8XY0AeZQRMQg3nb2uaL-OaBQeb14qIa8_ZJHkqjrA10YRJYxEALEk6ykYXBlPHZBgErpljEu2vK8IS9YDYtZhZKQh_FZebX-Spl56cBUWRy1TfkPQTKIbLULWX2zb5CjfARJE3hqSh0WuJkyXATUuDGcJhuGSYHeuEdd2bJ4e2m7FV2K0FfRufFo5rKmg3D5TDeRJFbe9TAS0OPYyORYjdp3gESiRLCU843oA736xDSq4cHhdydnGM_i08_TtJtBV5n3zWnb9fx4ulDiqGInKXOrrvro-3bjv5CrIF3AfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/92430" target="_blank">📅 00:17 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇨🇦
گل‌تساوی کانادا به بوسنی دقیقه ۷۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/92429" target="_blank">📅 00:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92427">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گللگلگگلگللگل تساوی کانادااا
⬛️
⬛️
⬛️
🇨🇦</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/92427" target="_blank">📅 00:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92426">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/92426" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92425">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=cFL9bt5hxynCWakGdV4a3fs3lwVs1ambz3MdfOzTm4t3ajKgeCrPLQKbAMNL5gKl2Wz9_1BFGsWe_OGJzcnwgud_c1SrJZxhpXZeR4nF181fHM1StjhWpX_F9cG3p9IEOtmkuDYobNiFwpFbhkbUmrBVbEyfkyNpio33YirI_WbJnovfvL5kZcVGaV8nyrHbiGgYyW5J1CkH8fF36RqiE8mZgAzbJJzY1pNojVpvbyI5V1e0i8O22tpbz_r_jKgWsZkuo5L86nl2lC3weWMTrnJQAqh5e7fiMfVo61Yd8DMVa8Y5hYV6SyqrN6LXeqoCPnw2cw7keBjtMlZF418u_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c23cc9050.mp4?token=cFL9bt5hxynCWakGdV4a3fs3lwVs1ambz3MdfOzTm4t3ajKgeCrPLQKbAMNL5gKl2Wz9_1BFGsWe_OGJzcnwgud_c1SrJZxhpXZeR4nF181fHM1StjhWpX_F9cG3p9IEOtmkuDYobNiFwpFbhkbUmrBVbEyfkyNpio33YirI_WbJnovfvL5kZcVGaV8nyrHbiGgYyW5J1CkH8fF36RqiE8mZgAzbJJzY1pNojVpvbyI5V1e0i8O22tpbz_r_jKgWsZkuo5L86nl2lC3weWMTrnJQAqh5e7fiMfVo61Yd8DMVa8Y5hYV6SyqrN6LXeqoCPnw2cw7keBjtMlZF418u_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‼️
توهین‌ناموسی محمدحسین میثاقی نسبت به منتقدان تیم دوست‌نداشتنی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92425" target="_blank">📅 00:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92424">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUwHbbM_jcdsNUP-GPMoIaed-PFFWVLXm3Oms_4Y2YJjWdEx7Uj2rrxKHBnTbQbCZleAVsfTtsdBQy7_tMkgB_fLtYLZNBGZmnmDH_CTi3JlmfgbmaOgyfmrRdPIDv843OcGsV-N8VBfgEYKJF7z5hpL1VjddxR5YbRe-ChidpUhTPTZnAd-K6cxel6u_82RG-jXqyXKnKEcVDngEUCcjTLB1WUoaCIFsmLF1nmVtmoD4ODhTNHHhv3Xv7z0CKco4RwHjFzi22trKMS5pY_f3nUSSymBTPxrIACi-O74GNnbXmgq4PkqIWT2vUG1R5Cw5ZJvjb_mLvbw_qz0QEExcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لواندوفسکی دقایقی‌پیش با پرواز راهی شیکاگو شد تا قراردادشو با این تیم در فصل‌آینده MLS امضا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92424" target="_blank">📅 00:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92423">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wgyb1FE-At39DVX2ym35ePfiRqFpHp_jUwSxRCf-2g_7g2PsYFidSjPluwotza0ML3ty1W3hvEvRYvMlYcpQAt9fcSVc7OKhkFkn9fhrJWCLToeNM36oix4rK7WBywIFFBsS-8FFvx9vaU6nC-eMi_hDZJWdTYN2Db9k1vNN5fHNnXEGdUNRmr4oTUgiLNgDZs5hJNd7iw4b2Va-gcPf5os54DXwR2mAyczsMMqvZv6cBnysZmrcT9nJEmEPTzZJdfBvY3L_q_kuLdFYnK2nu0RxvanVymhD_TyfzTGS5GoXEjfwJSzJKwaDj5_4Bi81MP3LlVwqxZXvgmPUSJfcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیش‌بینی کن، رمزارز جایزه بگیر!
کمپین جام جهانی اتراکس با
۱ میلیارد تومان جایزه
شروع شد
🔥
جام جهانی با
ربات اتراکس
جذاب‌تره؛
۱ میلیارد تومان جایزه
متنوع در انتظار شماست
🔥
🏆
۲۵۰ میلیون تومان قرعه‌کشی نهایی
🎁
۵۰۰ میلیون تومان جایزه با
جعبه‌های هیجان انگیز
👥
۱۵۰ میلیون تومان جایزه برای دعوت از دوستان
📊
۱۵۰ میلیون تومان جایزه لیدربورد
⚡️
۱۰۰ میلیون تومان جایزه هفتگی
همه‌چیز داخل ربات تلگرام انجام می‌شه
!
کافیه ربات اتراکس رو Start کنی، بازی‌ها رو پیش‌بینی کنی، دوستات رو دعوت کنی و برای جایزه رقابت کنی.
👇
همین حالا وارد ربات شو و پیش‌بینی رو شروع کن
👇
https://t.me/EterexBot</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/92423" target="_blank">📅 00:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92422">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نجات دروازه فوق‌العاده مدافع بوسنی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92422" target="_blank">📅 23:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عجب کون سفیدی داره بوسنییی</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92421" target="_blank">📅 23:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c6c690d9.mp4?token=WJt-Eyp1dH29hVxnlekesWaznT0_cBn-oX436ZRtPe9yyOiRRMY6ZEQ5SuEiB1naSadvXyuOrpAEojGCtGWjwbNAIrQzsmnARwJzIxKCF--DB8vMuivRngQFOO8xFfvTj_af6ZeM7phX20V-tenQ_UYIy5X3QJHcS5KGJxSpZTF6sJVcGYvY__Pj2rRQgk24wggInGcf5GbGUJ7nEQjxPrJCyitl0gcd40aTGKpI6VyW3xcxiUv-8FLq136XSAv-EP1WvX7j9lC3RcPQ7B20gsBwOSTOhsFPKEthtvowB-eDRajC2SUagDvOC836YI3_1xDSDKfThKL1OQTqX7slFpqFO9acurw07DUjf-NMQzoJuzWx2ZnHr0e8lFOvad5rzef-Vyr16Zn0K04WGSUwsYXs_DAd3_ACiw3IAWnfAQtB5LVdVstR9WhA22uz5HtXGDsa9M30GRshAi3z8fSvcz94t7YG79MGGy5-PrCxk9Br4wh3-6YiCn1Lj1riUgexLlFIr6M3dFUY41cfmgnINLeQ8UDeqM-VfIUcpSjIilKRRNGEKwZhNuIKQAQck00jkCNwRl-ZzxcQsVKnsiTaSYO0YFUhxfywlSQN8N7zzzWYJ0GfgEerQ-kvi9WaG0Ics6s1v5bhyGlOXIU0vRtplUu-2vnRnuULRaPyLsKhVXI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c6c690d9.mp4?token=WJt-Eyp1dH29hVxnlekesWaznT0_cBn-oX436ZRtPe9yyOiRRMY6ZEQ5SuEiB1naSadvXyuOrpAEojGCtGWjwbNAIrQzsmnARwJzIxKCF--DB8vMuivRngQFOO8xFfvTj_af6ZeM7phX20V-tenQ_UYIy5X3QJHcS5KGJxSpZTF6sJVcGYvY__Pj2rRQgk24wggInGcf5GbGUJ7nEQjxPrJCyitl0gcd40aTGKpI6VyW3xcxiUv-8FLq136XSAv-EP1WvX7j9lC3RcPQ7B20gsBwOSTOhsFPKEthtvowB-eDRajC2SUagDvOC836YI3_1xDSDKfThKL1OQTqX7slFpqFO9acurw07DUjf-NMQzoJuzWx2ZnHr0e8lFOvad5rzef-Vyr16Zn0K04WGSUwsYXs_DAd3_ACiw3IAWnfAQtB5LVdVstR9WhA22uz5HtXGDsa9M30GRshAi3z8fSvcz94t7YG79MGGy5-PrCxk9Br4wh3-6YiCn1Lj1riUgexLlFIr6M3dFUY41cfmgnINLeQ8UDeqM-VfIUcpSjIilKRRNGEKwZhNuIKQAQck00jkCNwRl-ZzxcQsVKnsiTaSYO0YFUhxfywlSQN8N7zzzWYJ0GfgEerQ-kvi9WaG0Ics6s1v5bhyGlOXIU0vRtplUu-2vnRnuULRaPyLsKhVXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد شدید بازیکنای دو تیم با همدیگه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92420" target="_blank">📅 23:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اوه اوه
گلر بوسنی بگا رفت
😐</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92419" target="_blank">📅 23:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92418" target="_blank">📅 23:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4eqVtxNFutYmNgLzst3CB1l5Uak_v4g2LXwzIdmEu5CHsAIkUZBXlFbLSqy0lGjW4P34XrVsWu6oulC4SCF94Xn49s3g7PeVrMcwj8oxH1Yh2aR5BLuQ9MOU9XRmEd2R113jfKQAW_pYmTe8nqkbKg6o5DgypAmNS1tXqgjQLSUFccLLvAnZOLzWYOTBY9TwLrPYM1Hwh9CoR4K1vKLRYut9wyX2nHw1c7eDFTpdWUHu8t9dPxm84Vq0MO1syfbKD90jsSBMZKMlTdgvB1QXmlvxJsGWZ79et9d0w-vwEG8MUG2UyoQX0vtsxvQG_WzDy0v026TUT-5Rtq9GA_lIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییی سانتی اونا
🇫🇷
:  بعد از سیلوا حالا رئال به سراغ متئوس فرناندز می رود!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92417" target="_blank">📅 23:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92416">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk5vUQeFPlt4oGlCWDKvhavqZG_T7IQYpZ-_EZ_GccT8b7oQI1yguKUzR_1drNfnaWbWwoiHMjcjNXhtPrmeTI6RbQ4E8AxD6KZ7XyFK0aNLODdiTGGogS8k4wY0XDZbTXieZsoR4_oxUyoZsg6I6MwumF-3BkwcLGZU5_tXAbOCeoOE_8mKOMEnCrpUt3Q9Q2EKJPaALySqVOkKGdX1O7MdwqNKGOSW5gmqYWfr7ydt3jhcX9lXTslNDjOwy6sN7yorf0EcKCOKheUR3q0qizuhtTzwmKv1tZfp47xN6de9ORzySd7JWtwjzlAYWeIXR7c4-50MtVRjAUvXs9tdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇵🇾
آمادگی ورزشگاه لاکچری سوفای برای بازی بین آمریکا و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92416" target="_blank">📅 23:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92415">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BenrODIbU9fMvvUBuSbSUDMY8jB1qViKZgOYdCu2B5fOpJeiSxvVN_lEEbbAcmJGVIS9JZhWplsqV-z66DnSV0b-RO5xvQ2TIY31dz9R-3EviC2ZTo1QmakjDZUs0P4NdLTXjgGVhF25atL-G_Rz2DciTmhi81q_Q9vB3w5K94kWvGMua8fM2SCqJgNRHU0T5pJe4KnAAGZajdlbXNbjXHjPgqX2Pm7xOD6EMIXS4uLpopx9dm1i_7J4hvw2tIRJ9b8s-qorDYhGA9YOZgeWt07m3im7exdGHvTAjtSwhmulZCtw-Gm_z7pe8IWmXRM2BQkaQSkz508SfECUeRILNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه‌اول بازی امشب بوسنی و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/92415" target="_blank">📅 23:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuMyF-H0NLBfnl3NDeD-ODA-RDQJ3qTFtG_R0OptXFpvITliaP8Gond4i3GmZKZ-VIvvHIXIV82LNPhqgbElj6JsXOMaVwajLzkzT3BcEdQEY2E0tThDgDu_ZpUnYZysC__kMwnRRm7qGvz0zgrrZ5WFiRt2rIV2NUEm2IHk9_UISL3qb7_tCTCUbPWKDgXO463fW3qJumx4PlVG7nzqQRiULHxJgTyZMjH73SC_hr6ko1oveZ_JEX7mL5dzvHeSsM8j-96NNTmqlAI4EhnqYC3YSWUFNox3le-k0rMe9MIRYaFHSk50SyIhZ2HFONpS-f5PzAQhqAiLFqNC0mzlTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
طبق گزارش میگل سوریانو، ژوزه مورینیو اعتقاد داره براهیم دیاز در حال حاضر بازیکن چهاردهم یا پانزدهم تیمه.
✅
مورینیو با فروش دیاز مخالفتی نداره و اگر این انتقال به تأمین بودجه خریدهای جدید کمک کنه، چراغ سبز نشون داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92414" target="_blank">📅 23:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🏆
پایان نیمه اول
🇨🇦
0️⃣
🏆
1️⃣
🇧🇦
⬛️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92412" target="_blank">📅 23:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🎙️
عراقچی:
🔴
ممکن است ۶۰ روز مذاکره تمدید شود و ماه ها ادامه داشته باشد. ممکن است تمدید نشود و دیگر مذاکرات را ادامه ندهیم. باید ببینیم بعد از ۶۰ روز با  چه فضایی مواجه هستیم
🔴
از تنگه هرمز هزینه خدمات رو میگیریم و احتمالا بزودی برنامه مشترکی با عمان درباره مدیریت تنگه هرمز اعلام خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92411" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgJ-_Rfz7RkHo37c4YeowQWiKZnBiHFumAQQ7AhM2VkWCY-8DmDqjS4dlPLIkHh8o0Ss3MgRxkaH-7atYmae_y7hDbqSpUVjdVHYkOziK3M4mQemW69nyOts9K0sgf8X-iGDX8-_hviFAMjPl__9bUwnR01gkeoStkxLfLcSpjrhEndZ5u10INKvivzqhVGEOXwmhWZ2LO_mnh4L7R-f-EZUClHuqUXv07KEYov9lcIUoWbMaA5QKgs_KonFqTMi_DxsiExCJj9oG3bjBnquzZo-J2Xx5ihcy5nRbDA0Y6HReihTT1mgVV76AKjZszULO3dmo9fjhDt3GZW4lIY9cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایان رینولدز دلها بازیگر محبوب ددپول تو بازی بوسنی و کانادا حضور داره و از نزدیک بازیو میبینه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92410" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRbeaRbB51y9SCPj5V5uDHEpIvQSIHcInKVA1RSrG0IZnd3cGmPCNLLJywMZRY67vKpm46wl5-5UTlUp6QV8CoHJ_ywgfr2wIHjXoRLV2ZqZS2vmyU65KC7VMbDakHLU7T1ScJYnX-Mj-rnmkifBDnaT-lV7QCzrQcdy13gGL4z5vuQe3yQWLTTrITounT3gpgQ3CFJSwFW2mMwOTcZJ0Hc0w9CjPbZAjXgCjAtngrIYXwRXHMcGpJU-hxqQvjeJ2c7snc5eXVkfxetbmvvSKPP1iti8JheO24rcW57oJU8y5268vyvNHxLVCXVrRrOmnPX4cpSHVeOQ-ttddC6hLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمت بد ماجرا اینه که مکانم از خودشونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92409" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb9e5acac6.mp4?token=mVE0WSXKDjvaNIAFgxGQ2GU2278Wm1uaWutJZXVkMvYr-AONYFjcS0zwhewJj-IZkGskrAfM5piDmpzvYo_-CDsh_tzvB70n2Evd5mDL0zD8iNUYrk7dNbVmOGEm7csIbeVyF_TQQmFlP81ELOR3Wi9gpQGqiUHYIS8697N1rBg2LOtbAZx79XXE3I-GFW5IpSkQAvKhhEvs9TB8tQaDFJHNF9hYdI6g6UCfpY0FQVKcr20E18smAWkhaPT_PMA_xsZF5nj0dZvR38BiXcOWyUjjvTjYqX8PKWKKf-jaFxB36AyJ04FZM6JNUWIscKy_7fVfveoI6ZU8MbZpWa4zh1VA8A3LkPQwkoF0CKYmEtc0v5nuROqsDPaXFCrZAdVMmsHTkzWkEzfuY4jV-_n6Ux6VJ_llqfgK32zOM48etCiN0bz01MthuTrkDkoR4uAvfbXMAiqz_6qwqaVipCqjR6W97vwrRe9xRFbJMB__ObOPWA1bRW4GKSCa6-5gklFCOGIaWZ7-MLiR_4inio7ovp7meiSp5M6Z87_YnT3QjCzghUKwJl4AE9bUPlqJTV5DX9AbhX8GX52B8EmSkDqyfzDbA4V9EdYQmNlBIegveXJDCyqJE1Zpru69U7870d2hTktdnoPukmNOmW7LgWIotOnOLLeOMTGalSBmD878Q5s" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb9e5acac6.mp4?token=mVE0WSXKDjvaNIAFgxGQ2GU2278Wm1uaWutJZXVkMvYr-AONYFjcS0zwhewJj-IZkGskrAfM5piDmpzvYo_-CDsh_tzvB70n2Evd5mDL0zD8iNUYrk7dNbVmOGEm7csIbeVyF_TQQmFlP81ELOR3Wi9gpQGqiUHYIS8697N1rBg2LOtbAZx79XXE3I-GFW5IpSkQAvKhhEvs9TB8tQaDFJHNF9hYdI6g6UCfpY0FQVKcr20E18smAWkhaPT_PMA_xsZF5nj0dZvR38BiXcOWyUjjvTjYqX8PKWKKf-jaFxB36AyJ04FZM6JNUWIscKy_7fVfveoI6ZU8MbZpWa4zh1VA8A3LkPQwkoF0CKYmEtc0v5nuROqsDPaXFCrZAdVMmsHTkzWkEzfuY4jV-_n6Ux6VJ_llqfgK32zOM48etCiN0bz01MthuTrkDkoR4uAvfbXMAiqz_6qwqaVipCqjR6W97vwrRe9xRFbJMB__ObOPWA1bRW4GKSCa6-5gklFCOGIaWZ7-MLiR_4inio7ovp7meiSp5M6Z87_YnT3QjCzghUKwJl4AE9bUPlqJTV5DX9AbhX8GX52B8EmSkDqyfzDbA4V9EdYQmNlBIegveXJDCyqJE1Zpru69U7870d2hTktdnoPukmNOmW7LgWIotOnOLLeOMTGalSBmD878Q5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
گل‌اول بوسنی به کانادا در دقیقه ۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92408" target="_blank">📅 23:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سطح بازیای پریمیر لیگ ایران از این بازی بالاتره.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92406" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگلگلگلگلگگلل بوسنی زددددد
⬛️
⬛️
⬛️
🇧🇦</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92405" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oar_J-AC5qUNYMRoFaQxPcjtTBd8MPLOfAc2FoVVX2sLCmLWK6SUoJ8ZY46oIpORjyqfNlIhxpHrvG09uGYXe1pzigPwRgryso9P0Rq5fzvUmYqXZx-c9CQajB8x2ai46F4soj5eC7sAB02sqh6XkfLRutGwYVmiXdYjWitUQPT-Mmq5O0_DpotJlxnbtKrMZu47rnh_gT3St7pmNYjPVxwYbzS58gMEQkzLlVSUElh3Z3yQsnMbNzJP0PsRpYbAI15FjDK-ozJ75p3Na7nC1i-8uiHbdTwCZOOGzKBTa4T6J8soDctYTjvmnNIXj9GfQl1GjJhlBZM4evJuMyHqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکن کانادا این توپو از بین اون همه جا دقیقا زد وسط دست گلر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92404" target="_blank">📅 22:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92403">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سطح بازیای پریمیر لیگ ایران از این بازی بالاتره.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/92403" target="_blank">📅 22:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سطح بازیای پریمیر لیگ ایران از این بازی بالاتره.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92402" target="_blank">📅 22:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازی تا اینجا کصشر خالص بوده.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92401" target="_blank">📅 22:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYWZ0rwFhlg7EdPfZ6F3oV5gjPWFki9wZdLl3Y7-hhfIV8Un8iqNRBrMFAL6l06dbnWbWIYRkznMRkn4uH0we0bPw7ikELc--UHPYtV_P_s3UStLJsvVTj1F5lHTo6cUYqVhCECGZGxq5DxbkFURNzcvpnif0IQyT2RpCbFZVPAJgitSFvhQ4lp8X6-l6lWL0d5rR4BzwIpqWSRSKc6gB4_93QIPFyjnjXR-3WX5JUt0R-nIRD7K3S2qfQejiwjZpQFEGvYLO9HEYvCrG0U-7f8xQUvGQbBTfftpVZGgeenab5l7-jxwWLnM0cgmITf8Daz4V4UzH615hjWHaa4fQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار کانادا تو جام جهانی تا قبل بازی امشب
6 بازی
6 باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92400" target="_blank">📅 22:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6nVZdmEL1K0Q252btkHb_-TlZ5Q7xkCTa8aY10hMk6tZLm6OZ4RGGQebo801nAwfcqkfZegiDRd2dlZORClmFEDAHlIfHsnYYSZq2vWhZrUJtnUPDeHA3eW1Mri5zKxYjrrZYnC_JtUtul-eBlWs4AwPKB7M4sbu-QZDfTLJuIMn1DUFDZ2hDl64UmXYgOq58GQ5Nl50X4sA7HvlzYzKUk-KJde80H6FbFPwM1s5DfVLK6dPP7ZpTLrg9uHL4RO5Fat5FVzAXD7_tIhuqHMSL7bi2cCUM0U13fTmccjTPKHgYOo5ULjwjric2uUhdigsY8HUcgrZVaAyRldW6pSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکیرا : از وقتی مسی اومده آمریکا، همه میدونن GOAT واقعی کیه، دیگه تام بریدی و مایکل جردن نیستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92399" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری @kavianivpn  جهت خرید اشتراک پیام بدید
⬇️
…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/92398" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhfiFyco7VFY--1MWc4dLG8eIsaspca8EPKwRXsuvHNabuJFkWvGZuEdB2G2twMxmIyRFNmjkQfqxKvBC285BlMZK5W42zi2fUtmZKQ8Uh817ND5beOGc7eT4450IPtGEVVgGH2e5ggFzggJfl_ziTd7WUoD8HK_cVJ4QTVTmDC_pPFZ77SEvSrYXMoh0Dxc5QhG-wzpiFoalNAF1AWl4ykGy8I6JYn0R_E8A9mFozvhC0O-Tp_nClKgmeCEEQZjo__fOL7u_UOLO5FkhzQDo4nRWpmBwDhnwl8Xxh_8OSUcv-3UewaTSutlhSR4tjUEclq7jMvTQoxMKOgew_O94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 450 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری عالی
✅
مناسب برای گیم و استفاده روزمره
✅
تحویل فوری
✅
تست رایگان قبل از خرید
❗️
پشتیبانی 24 ساعته
📣
کانال رضایت مشتری
@kavianivpn
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92397" target="_blank">📅 22:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAFo-gXBgfQk0dQPdC6R_i9FBdx3R1VNzuPGCOPourtOk8iWJi2rSbI_znbDB5M4MI-8_o1MrDv8Zf7-kMdD9UDA_QMzbv3bH-DbECaVgTvh8ybPRXpB9-ZTejduHbVeN-XdRpZHxikOcnc-ch2UdtWK5JpvAld2R16iHkYDII1M_qL3qdqzAb9m16tVFSu60s4PDIesaagVuT55sP2YkSjCANv1ojYgya4yB2fhDxbi6CE4tn1Biv9a_lYdFm7DIpxBVVYZKDNZgqmVdiK7QapsE8gIm2yM9SEJAYDAI25iNCMyfCI2UsDLAWF8x9ea1wBwlYVFAPFWuQz0tq-p9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فورییی خبرگزاری نزدیک به آرسنال:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به بارکولا علاقه دارد و میخواهد جذبش کند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92395" target="_blank">📅 22:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=H5E6tywjqT18jaQf00fGsDNM3P-4m3mSjn9URUfWZa8BxwDviqKQ0M1j1kXCss5aaWKtewb0yrv2vAxFs7P71_-K-ow2BKDGRKA6i922MOu_M-FxaJmo0mCkI5TovaGiww82H3CnNzbTRXGHKEYx6gjFkkEryVt4bXMnEQSXw6fNzEP_CC3pwoHg3WesJT1iPl7GPek2Owl-iinc5fLGEx3Ahbxfq9MDRSaJN0_lMJv7Il0NlRjnQ-KjR0nkxBfWfsQb8cDkMz2f12fyAVGY4hbPFgCkITi3MogwrAqVR_UCiDgm90qNtn2PVxCpK90RrOihClTro_EtqAMjmOlT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=H5E6tywjqT18jaQf00fGsDNM3P-4m3mSjn9URUfWZa8BxwDviqKQ0M1j1kXCss5aaWKtewb0yrv2vAxFs7P71_-K-ow2BKDGRKA6i922MOu_M-FxaJmo0mCkI5TovaGiww82H3CnNzbTRXGHKEYx6gjFkkEryVt4bXMnEQSXw6fNzEP_CC3pwoHg3WesJT1iPl7GPek2Owl-iinc5fLGEx3Ahbxfq9MDRSaJN0_lMJv7Il0NlRjnQ-KjR0nkxBfWfsQb8cDkMz2f12fyAVGY4hbPFgCkITi3MogwrAqVR_UCiDgm90qNtn2PVxCpK90RrOihClTro_EtqAMjmOlT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی عادل فردوسی‌پور:
فدراسیون بعد از اتفاقاتی که افتاد تصمیم گرفت سردار آزمون رو به جام‌جهانی ببره اما فهمیدند که گاف دادند و اسم او را در لیست ۵۵ نفره نداده‌اند
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92394" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=bq9DRd8hxrmCozQ2YNbRHt540dvqqlSmrzXKRIe91vNrG5MdYIDgfXo6dVeYtwoQw7awYkX8WDGVHIMtxnXDNlyBoSLr2OOspD0pJ0CEYUg0PZ2Z93KM6eq0gi9zCUCx3CqAXbc4Kd89C-ptu6RRXFL4V2_3kJt8gFOFerU8i9CjUWgsA3qW8r9HaPJsGoSLRa5KXbv6tzD0Lg_CQLHn5meRf7gmvYFww6e_6bd3HmSGdyj9WqwoYQl1So4Bw0ZSmbdSdPordXgixSnqXJgmpyhhzwwqN3RhP1JBREfaw89nPhdQFwAmtk7CK5AnjPFpHHCnIBYVI965Rm6TMfTtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=bq9DRd8hxrmCozQ2YNbRHt540dvqqlSmrzXKRIe91vNrG5MdYIDgfXo6dVeYtwoQw7awYkX8WDGVHIMtxnXDNlyBoSLr2OOspD0pJ0CEYUg0PZ2Z93KM6eq0gi9zCUCx3CqAXbc4Kd89C-ptu6RRXFL4V2_3kJt8gFOFerU8i9CjUWgsA3qW8r9HaPJsGoSLRa5KXbv6tzD0Lg_CQLHn5meRf7gmvYFww6e_6bd3HmSGdyj9WqwoYQl1So4Bw0ZSmbdSdPordXgixSnqXJgmpyhhzwwqN3RhP1JBREfaw89nPhdQFwAmtk7CK5AnjPFpHHCnIBYVI965Rm6TMfTtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش جدید لب گیری در سریال های خانگی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/92393" target="_blank">📅 21:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92390">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stXHlOYRrn1FVgYoXBplEioQGFavSljKp0FC26Zvm_5b5-fVr4_MRn7vthxGJKX92k-0WqXuUWmn6Gu-WnbbbbSnbGIsebwYYhDKISol1ZNmMG4mUAMfGTy4GWqvSrAncuc-4vopR1Cl9f7Hm7PlxIcptIa65vWPB84hFEJFAbTMca664aSdQtoL5V0Yd_G_eNVljVUZS-uRMjMs4sHqk0lJ4gU03THPwqSUdbWCvMVba9hBVq1GI38i8ScgEJsWLNzOGe4AWl3feP5sANHDCxJkAmAAIfkpbKPoGHRKrQt6lIxck_GT2co45ZLLtDog0AH1G4Gz_YzN3vvSqlXDbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljA32dl31ptuXl4uif3XkXZo4mfVasZVu0BC_gEm659Kzk0pOzHW4mC3VDjoYE90k2IHjbrrMObTER27ovRME6c-EaKLWygY3wHMFGMNN08GHULp6Aicard9uzf-Ugb4-LTQWueb9I_sPc4hua2F97wSG6DP3_ojUqUlhDyogtxM9-cVfT9acdbKuTHzwDESHnieQJNs50DfkORIXSOc_jeKa9Ya2mW-6vCNvQD_lD0HHEtgFlbZVBiUGfu9afvcEBwRonnKcWIfGb7h0_NqnJiT0hRDzAuT9MXLADIDuPTaedl8tK_Lgu6mRrz1MLZOq1WfgZMrGaw7uH4JZ0C4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrTECSa6uZUAijXe2HANFSOeW77_bibVTsfQU7fDFDQvpU05uo4gYF5qyaGxJu3Zo8KhXn99amqdaAHnUsTndN0HB5mwbgQjwfecUyHHM-MOHIA0AM4BL1LN_M-lPj7xVhJNPhZHOxIU8fOKdj5ayN2IhQqt6lwlh4Caxs4t338g-epiR7tr80mzfqJ9wVSc42ZCdHhZASOThzse9J1G6RenrLHwsNRRQcMKH-YGuQ4vZ38LFH_T2lnkvtC5vjPCF_-fntjWMSoC2mhu84DHHYeL1ku2K6sq1rJffLHGc9W9VonZ58HBc4SP_SOojtuNx3U-Hd0vPYT2FJ5Aetod5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔺
فتو‌شوت‌های لئو مسی با کیت آرژانتین برای آخرین جام‌جهانی کریرش؛ البته که قطعا به جذابیت ژنرال قلعه‌نویی نمیرسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92390" target="_blank">📅 21:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92389">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b3801082.mp4?token=jz3RITrqN9422Pc-D_qjPGocTTaDPzFEOjrUwcLGKYf5k2grPyHxWoAuSplkbMXj85uMHq47GnfX92msbk2YB3T9i8TnAzr4e5h3CjNEzDheLKIEwY_mmI7b74HI6y9pOWjK8WpO4GgV_ct4OrNxUMpeM2sE7qjkmPSfkyvQgxMLV3c0vgjH_53vFMfyOfMQukggc3VydsLjqOBCpVZKPOS0XrYQ1oMax7daO4qAbQHZLu4pp5x9OW_bY5oAfC2RiUoOyslo1MX-a9MyObbxFGjC8dgB-DQR4CKOeXfExS83u9kcifQvLfVNXQEfQDf32FzIg4tCZTlhc9OuP3_dng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b3801082.mp4?token=jz3RITrqN9422Pc-D_qjPGocTTaDPzFEOjrUwcLGKYf5k2grPyHxWoAuSplkbMXj85uMHq47GnfX92msbk2YB3T9i8TnAzr4e5h3CjNEzDheLKIEwY_mmI7b74HI6y9pOWjK8WpO4GgV_ct4OrNxUMpeM2sE7qjkmPSfkyvQgxMLV3c0vgjH_53vFMfyOfMQukggc3VydsLjqOBCpVZKPOS0XrYQ1oMax7daO4qAbQHZLu4pp5x9OW_bY5oAfC2RiUoOyslo1MX-a9MyObbxFGjC8dgB-DQR4CKOeXfExS83u9kcifQvLfVNXQEfQDf32FzIg4tCZTlhc9OuP3_dng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گوشه‌ای از مراسم افتتاحیه جام جهانی تو کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/92389" target="_blank">📅 21:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92387">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqNGr-DCuxv4CTDcmIktEUI4HNwd16bIBWd2W-niL8WtOyoVIYM9-3ZW9b1ZuZD0aqYetwaNnWfXvvsbuH-blKrfmMFgD8x2eacTMDj506Wq9_yJWB_1n6r7mLltCRBbAAB0x9VqA0mOQ78zsTjvf1ZURyyIhXjxzA45ielaC4-MWfQaYB9y4KUQrBbcyZ8-xX4tlx9225Kvugbq6A1q-_h7xeJY4WnAIOkBUvWlQp9maY80giRY7zKITmQALT9mQZziIyS73REP8QlrTSGeSYxRKF0oZpGNR8waKO1mDx6oRmmFETqpiCzw-kpkl_B4LhVI2-xEIY8Ir_9BVBCErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qusQOTYDh5gVGp3Oer-dHPIpSU0BVbu1Cob-uqlkv3O5FUEf8j_uNZKl47X7STAhtjaBxDnQlYBDn-CCOg8ZA5s5tWvAK-ScwBB5vflur4GZ7u82EbOvjfcNgWZY_DZVBBb7xrUt2Ou3FPsjxTo5_rgcsi-uufn1uZ7wWjyyfYLpWTgYQ6dU8PCK6qtfIpEycDQnTnH2Q2CwDbaGrwiIEQQWx58SoU47jwYbt3DHeDfG1IM7xgB7MP4OAh0Qt5zaitV34y34XfLs2ZsXO5wLl6cN_H37m7MCAApKqDGYEGVT3I3SvTZ1D7qNEglagXBsHKKYbYNoP6Qs7xdcBiS78g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر شاهکاری (رامین رضاییان) یه کپی بی ارزش هم داره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/92387" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92386">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffaacc1d36.mp4?token=vU88kCLcnZ9QJ0vVOjD3WBfnGRUPAGJ4iUqDNUIUAAvEUx4aK4W6yiQ22tI3Cix3-4Ah_iBeiM7rsDqb5N02mlkh0O5HGA1h-Bs6TJ0aa0XlBzFNMwowDy2MaVV-zbc5NhvME17ui0-4nj8w2_rbVsB2C0mHf8q0n1X9QCB-vlUtBtVn3srugIUes8ocYklE5RkqM62QQC_O61Ig4-ORkRiN_0e9auKlQu3q9k-o0TGw7et44Y8eYsme13QK6azSpNl4LcjXbpm9Zv0mVP3bkJnXsqKRiZkpzenjo7G8P2rs55BMwEShq0t0lJzEPEZ5Lyum4iCRQuUCBDcOi_90tQ60OvSaui56SQKClHzFZUwImvRDOaQqHQSh2As44R1fGGuva0iVFwUyd5EcqEUBHfriRWI1BFE7wANHA0yZzNSJf0J3XYJX1wORNEqNLuu8TSgpDOOD6v-DIomXU_yyZYfE2ZYRzf_yrJ1GsyQgx_0aAuHluPIhjEyNv66up4CS--hwLL3HkICYz_r7lKCXcoQgngkq_AZXaYkmCPogyHO3fM1vRt74Lu5_DHGYhPbI_32yAh7sONdtWfcLvSgLxFWcsIJDksC-XLmaT8UyMxqNS3WJcPpl66uRcGH0WNshGaTd5OYZnXTb3H4d_-iE1r72QjX0uhcEM4ru5zWqQGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffaacc1d36.mp4?token=vU88kCLcnZ9QJ0vVOjD3WBfnGRUPAGJ4iUqDNUIUAAvEUx4aK4W6yiQ22tI3Cix3-4Ah_iBeiM7rsDqb5N02mlkh0O5HGA1h-Bs6TJ0aa0XlBzFNMwowDy2MaVV-zbc5NhvME17ui0-4nj8w2_rbVsB2C0mHf8q0n1X9QCB-vlUtBtVn3srugIUes8ocYklE5RkqM62QQC_O61Ig4-ORkRiN_0e9auKlQu3q9k-o0TGw7et44Y8eYsme13QK6azSpNl4LcjXbpm9Zv0mVP3bkJnXsqKRiZkpzenjo7G8P2rs55BMwEShq0t0lJzEPEZ5Lyum4iCRQuUCBDcOi_90tQ60OvSaui56SQKClHzFZUwImvRDOaQqHQSh2As44R1fGGuva0iVFwUyd5EcqEUBHfriRWI1BFE7wANHA0yZzNSJf0J3XYJX1wORNEqNLuu8TSgpDOOD6v-DIomXU_yyZYfE2ZYRzf_yrJ1GsyQgx_0aAuHluPIhjEyNv66up4CS--hwLL3HkICYz_r7lKCXcoQgngkq_AZXaYkmCPogyHO3fM1vRt74Lu5_DHGYhPbI_32yAh7sONdtWfcLvSgLxFWcsIJDksC-XLmaT8UyMxqNS3WJcPpl66uRcGH0WNshGaTd5OYZnXTb3H4d_-iE1r72QjX0uhcEM4ru5zWqQGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتیش بازی کاناداییا در مراسم افتتاحیه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92386" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92384">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNlZGgt42W8t_9KYjBbJL4VBR4v626N5jPKQWleb3FtevUYdf1Sa2hx0N6HdKZ-CgDGjo8exjts466874SJkBLvoTfxt1uAmeRAgdYYqgllcRFBMz03W6lQi8oHzoIVwEmm85xlcWp_fEGDE6X_7MhXzSbsd4tmsLmSdXPG96Dd74_VsthWQq7S-ZHR3oRWcwRLJdFhDuBSMtByAwG_E5BW5XOk--VnIagT2KmCGUFhR819fPff4VS0mJQFQoBUeQOQ4ysR5q1saCtJ5y2dd-SzUMfwCCS2y28-tAd_SHT5u47YTI8awTZO7AvL4ZzloFbqB9ynvOHHGBaN0ga_efQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdE-kzrJWn593yrTxNecBKU4P2PQkt3vTNklX-OV-inUFC0hbGsOHV-5tbmak4jOSwhHS2_fOk3FXuq54pvlN-WtOYXVaUtrGiObc_L-D072iWFWwLBkf9EC5wwSjCYzZ75V7SjSqZi27lKrsRLm8hGFAtnSqctoWfl2AXLzZd7P9n0uBNuuqiKV-doLJ_mZMJCF1c4yejXEAZ-CAEwT2pImQ5pRnfMaxjSNcEDAXLlyi4IMlQSa0vgtK9FO4tQf_ivPQny6NKw3mLd1SKYF87Hiqcg20T1lfgv2lEQW6Oe-pvAlWJ-pUjPcAeOiQoDmrKf8-1OgSgMGLLQ8b9vw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
🇨🇦
🇧🇦
هفته‌ اول‌ مرحله‌ گروهی‌ جام‌ جهانی | ترکیب
کانادا و بوسنی؛ ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92384" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92383">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92383" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92382">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym39Hqo9Ys2lNIyOrOH4N2dZV5BUxNiMfQMwp55_8HoJUUP_SoEw2jNKdXA_fwH1rN7Vnb-yetFb1fewYpmzs4iLgdLMxPJHsgTpx1CakIWSiVpuo133d1bVDE1bzsY-T5c-tvfJKYurTiPs03Ce_QsPPvd-jPSTLzWj2X3Mqb7ws2-porQuNnD6g8mJQIctMdVoiTGEJoeN63bZ-tx4fXHphJf6BYXf_WHhePpgVAWzClt7M8yG4L5YpXnTfs4u4MRMXScEmCjna0IUDDC6qTyg2OxKiMdsQAyCSyemRV7j_sJLr6iluKu4oGSrvhu366Pgem4-D-1291fylwfHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92382" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92381">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0q-2SMZJ_Bsdou2bcBuIjmlQSf8fhyeO6w_dv6I1hstEAEJmdMRNv5Mf04qFMUTr6CT5V2qjxgHYFQksih0A8OyRDa_mm3WKSheZfam7WZQdSqpCe-PSH4yMdj_40Dca_L7nPMnhqZ6Xns9S9mwIF0lqkgOw90XIjzuFMMFQl6ZBl_-nfN21uOpdfqD3hAgXXUe_TxQcuqO5T_C6OtXEpN-w3vTdx8fs4rpX1MSz3e4EfeTfsPwSEmCxFrchqnRcGwp70wy_6CsmhDUs7WVobah3bu8_8BtRXMKGD8q0U8or2DetJNvLF-U989kqKPXeIzEx2-RX4Iau0nC7VSYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
فلورنتینو پرز می‌خواهد مودریچ پس از بازنشستگی، زمانی که تصمیم به پایان دادن به دوران حرفه‌ای خود می‌گیرد، نقشی در باشگاه داشته باشد.
این تصمیم در داخل باشگاه قبلاً گرفته شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92381" target="_blank">📅 21:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92380">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5fvaJgIMFdwTxNdpOoLVnDnP8IAxhpIpQVGWOWhQ4UOd-obxZkU_jdTJSGeHjEqckyc8lHmeye1btkpy81Cv7uZcS41_N6JvztFAvGgOG1GOjsQRGMf6334SfzNgooJ5seRhXZE0nvozOvk0oRsEaJpws7zI-ooL_ruWGaLh81apA4VJ6JdocMSswOql4EDTexYvVVjLeS2pDWFNUv3aTDrFUQhnQhcLtrOQYWBpxkhSc8t-wi6EsRl6fFBx0mPy8spwVLcLVTL2SaSIK01No_nwO8Rbe_f1HAAuvPddVK6hVhru03i_0ER35meDhZydeJr2M-WLJsa-uq1eJozqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیانی اینفانتینو:
هر وقت جام جهانی 64 تیمی شد ایتالیا هم صعود میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92380" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccaw-oOH7v3NeyT1EK4Qkh8jIDV4aBxwezuk57IrIY97eDR96g5TmDWvx8KFigaC5v8HTRmadW4zuGZGD8Z8ggK3IaKUwwlrn7tv21zNfG3-0Rvq4UKmVSSapkPtA8ThHevJv3lnju46ec-lHMO9reMkNFW7oiJ3L4IQwsvVDtaq5180wAWSJEpCdUI20zJ9I9E-ZSDsbnCGoZdFWD-M69bkj-6YjmhrTtZgQg42tv3jsDnRhL--jFKR2RROS25-XzyWyr_OmxjhK9EwKvqoPmxEIbqzLpexJTdkKO4PDL3Nk6oQxkBKfmpT48byArRSvcxrih3EqXzs_7IvjuQ1sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
منچستر یونایتد نگران احتمال اقدام رئال مادرید برای جذب ماتئوس فرناندز است، در حالی که مربی جدید، ژوزه مورینیو، به او علاقه‌مند است. با این حال، منچستر یونایتد در حال حاضر نزدیک‌ترین تیم به نهایی کردن این قرارداد است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/92379" target="_blank">📅 20:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92377">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f444195b78.mp4?token=cRnnJsh5nPBquZimtMck9kzLYFxn5zJIPoA-apR2IXKARlb43ipTwyLmO7hX4viTZu0AgW3jTR7Hv6S3SPB6qHloOfAv-QIkn8VvMu8M1pJBsgdpWkmpuZPqi-6TT1Mgczk6TX5oAZmq5peqmTUBKcNfDNvsHFE5RWjNSbb3DDPAf6uF8Sf5k_ajaGSIpI_QJl1GU6306VmlGKDR-mgR7IztrVoIdtCZK98ywUQi2o5rBifnb1SjZHNi_1kKpNCEzL9NDDajPsC88zDfwELeJ3yqe795kkb7HDuZk9wZ-58JEnxxL09kKBC7arrCxsC8TR8skeXJzSEAubU0cPPvV0V_DjlrYhW46rQP3U0m2doHasiS8Qpa6Kq0Xr8yYQb5QmD294_cKWuUFmb8N12T7pQSxDbzjKIdWYdECv3sslukm310ZkpOtX5_dMgUswvV6pg06Yzk0_x1l4KM2Bh40akme-rWkpdiBzh2EBKT-FrKd2Taw40wM-_uNsep2_VsD_ZKHWd7z7joyPebajHfTevGJ4svkXgVZQAGhecHl2RU16RGjjS25zxUUZMs2NoxwXST9SYerBb8mSC4E8v6PKUkozuw3i5T47BXB_o5RPnbwWijt-ltIrZzDbOvBjjytJttb5ARK08HYr8ajXgK_S-bQvuY3FsqdK19y0r1SWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f444195b78.mp4?token=cRnnJsh5nPBquZimtMck9kzLYFxn5zJIPoA-apR2IXKARlb43ipTwyLmO7hX4viTZu0AgW3jTR7Hv6S3SPB6qHloOfAv-QIkn8VvMu8M1pJBsgdpWkmpuZPqi-6TT1Mgczk6TX5oAZmq5peqmTUBKcNfDNvsHFE5RWjNSbb3DDPAf6uF8Sf5k_ajaGSIpI_QJl1GU6306VmlGKDR-mgR7IztrVoIdtCZK98ywUQi2o5rBifnb1SjZHNi_1kKpNCEzL9NDDajPsC88zDfwELeJ3yqe795kkb7HDuZk9wZ-58JEnxxL09kKBC7arrCxsC8TR8skeXJzSEAubU0cPPvV0V_DjlrYhW46rQP3U0m2doHasiS8Qpa6Kq0Xr8yYQb5QmD294_cKWuUFmb8N12T7pQSxDbzjKIdWYdECv3sslukm310ZkpOtX5_dMgUswvV6pg06Yzk0_x1l4KM2Bh40akme-rWkpdiBzh2EBKT-FrKd2Taw40wM-_uNsep2_VsD_ZKHWd7z7joyPebajHfTevGJ4svkXgVZQAGhecHl2RU16RGjjS25zxUUZMs2NoxwXST9SYerBb8mSC4E8v6PKUkozuw3i5T47BXB_o5RPnbwWijt-ltIrZzDbOvBjjytJttb5ARK08HYr8ajXgK_S-bQvuY3FsqdK19y0r1SWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از خواهران منصوریان به کسی که واسه سوپرایز تولدش هم اومده بود رحم نکرد و کتکش زد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/92377" target="_blank">📅 20:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92376">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJdPAiBN5eranipxVIyUEUpekEdV5EY4WWwq6j5L7VD6-HX6ee49gl7wtrFbkqJmxt_ZjtkmOeWn050LgxonmdU2XDPU3TYMUVjH8a9be7KstnFgEiBih6OqB7CMxM1uXWM4vFktJLC4J4XoTfgv6v2iZ7fUwc1pQ1iC0wv0SYMDZGFkDM0bl8hd3tv9VW9Zsr7xudQ2js-DPMn86_67RvJEAYq-YVFj5WW4W9D9_YCFWBNCs-51nCNuS4mezRSwFqbjWJgkY8am9vlOQilzzsFcIPu7nlABotc2TiQW8d9dmFUDaemZ3f3BaJvt6tgj67uo-yn9bVT2hOl-IoVgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
از حضور هواداران سنگال جلوگیری شد و به آنها ویزای ورود به آمریکا داده نشد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/92376" target="_blank">📅 20:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92375">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFZajieInMmZyEJAA9iHAfG1WzV9XzW4LZPan9a5iJnMuhPbT4ZQ89DtKOcRWohDSAl-kiwaKqad5AFIc1MLK4py0eDj-q2EZbnAbukcFPlSCIvXaZUHx0dfkDNy0XwdLADgCwMaVrxNI8_QoXy5X_NboHFJ1FE5sVuzuyzvxrx03yQ9llq_IjDKKGqN-iYEjFvBrHM0dnKbITMnZUmNiTANs-2IFNfRMbksg8tJ49IBM7wR2S8U-ljd9XYgMzCBge62R04Ivrdo3nC7aJ9DcitPKEj2jvxnEsSxzEh9EmqR8L-M-TCYUuHA6-tjqoEXYUOElsZXyEszyEckqXWwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
بن جیکوبز:
اتلتیکو قراره مذاکراتش برای جذب کوکوریا از چلسی رو در چند روز آینده استارت بزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92375" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cG4OHMQEQSy5KDHFHW8XyB3YuO--KZzvA65g32n6y3HycWNGd7YbprN_VFXIKAdFke0OW1F2xW0AMKHgdxBCq1iTeZ0WlKjuFZqYxvtlEvMEyETqXiwgaayXiZoMTjDsFOIdxFfAvrnbAwvjXCX-55t9ORuilyL2Z9qHl38u3TvXEaE9vu-76lZdDopxU2vPGWJw1mjF9uggTUBKo5kahbhhS4rKWFmiYVApU67vN0mYy_zRq0QPOZ6h2V5vLzgcMX2Z6SCF3sJQBFaex89QcY7NzlIfQ26x-817kn-7FaNyrvFKtP7qQGx2DbruViZrIaMkA6joWW-Q98DDTg9g7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVk8h-P3G00mXwns3-Ka_jg2GBIiUd856ckSk-GNHj6XyhYe6Fipk1H1vvnMGHILXcgSW6ORvLa-HTK-iuB5L5zBqOK1xAyIro-kYypbK0e5dsw3Lsg9W0fjL6v1wXZvJH989txK9aE_1SBL6xi3MgV_Xgzhrgv3Q4HlR0H8rtqyobDaAv-vNq2UsAw4F56JdQuScRJaqoo4K_ZloRhfk-ewb4-14HslJ-l9nN42rCh9eMfgt2pQXu8rL06Vs9uo9u-GRtV52vpjZAC2pnTshA4TBN69wF04kCuPecDOCs-M7JIkalzuZ5mLU5nRrSEUJ2uMWTLyIGya25IIBP-hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYfsH-lt82RQeWTDv9co74GvnupXw1PwRjF25PPTTEteUdWXH3EHy-av90T-ofccN9kIfyPn3104wb_mqxrYndB7DanjQ6hv2zu1-7MTzIMTV48sak9F18gh-R52gEBCH51R0JiUvafryVFI2DYWzW1nW8qysMV8YhmDdB9ClgwJvXfTHw1bxVNcsJcSF92OXbXKklu1ZAs5AHJj0cK-hc5b-oc1CizxFkvFxHi5HzcDbuD2_O4nnwKlKk3U2RhQ_Vh083y7-6CqTNBimPFQsjoXn_bynwce0NCYZ9_b0TnncIns36QwTG1e0aYcodttg2dtrMn6QAhCqG2eq-c8iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکنید آقا
😂
😂
😂
(بازیگرای سریال دبویز هستند)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92372" target="_blank">📅 20:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92371">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1cf8Quk7Q3PdNTUbIY5s5-Zp3elLfrlnJO0J06Pxjx5XmYmfTMZeT8rRtuCLZdVKQ1hZ68_i55WZpHDhyLh_3YJo4rqyXMkNpXpUdrY-XCaF6Da1wxA85tobPHi8MECutG-FI8DNWeLOeBB7EmC_lfD9l2FhAY4SYRyQQDTen5bLl85uQTTAZWcBzR_fnF7uPdY6ZmNvyNc5zW8skkp_r3Hci4duP3ne3lasBxt8CqBs3xHjPe8_FmZToFjkyTpbALYgxaRTeiHDQSVr7ktvqsFAvEqHpXyfUvZ66rWEUusOqxHEQob3eC6Fl9yj0ecdbMKU1C5IqeP4CFgfXZEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توماس پارتی به دلیل اتهامات تجاوز جنسی از ورود به کانادا منع شد.
او بازی افتتاحیه تیمش مقابل پاناما در تورنتو را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92371" target="_blank">📅 20:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXuQuNCMHaHIHHf2w0EgkLiFb_m8g2ehFEaJN3Hafx6MNGUSzuazbCvpN9ivD7xT5AVzSDxipu1VCvm0jYiENdXGIcncUTQWCPLk52VTXSTQnqTn3N00vMbuema9o1tv6vaMAu9eL51nVwtyHxn5_hAGYd0BGKTE0LqPjwjv3CEd1wF8F3Q8fqwotL8rquff1flMhXaDcr8JykUuetap2ranHu7n_zZn5L1RP8g3ybe2x0u1zu8JjiejQcygLIG-AxfNFycAEzHDBZv43H_4uQiFAfyRLwiRM16hm4ylSeJkOTXTnfmugRTXR5ZrebpSKAHBBVxGewnvVmndPLf-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
🇧🇦
وضعیت ورزشگاه محل برگزاری دیدار کانادا و بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/92367" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOjo5EzwBu_Jss0nrR6wdHF4ZeRQTgMIwFlzq-cZVXOlR53N5iGQWLcguncJXnXh7DwdlhrD_-RtvpE0vJIEnSsraDVd41Kk9EAcs9J4dZVkmLj0E8V3OUuOsUAMSmVoipU6aF1cYQKfnq9fJidwxl0yAGMPawfwArIj15WNnP_t4hKMeGRSNoyJkwvIRl51X3Q1xJni7RbtXXuwxt3gAABtcsRV-P1hdEOYtaLTpe0XyNe-NRa6-Qtp-IbJuTqRw26LFuMjw-jIwREnsoIDZmkv7fghWvEhkxFoaKSICeWn7I_VfBhGngzYSLSPDuMHzN5dEULqCTszt5iDRLfJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
خولیان کوئینونس:
برای من گل زدن توی لیگ عربستان سخت از گل زدن توی جام جهانیه.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/92366" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92365" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETA2BVREoHIwdbYrDO1ATI3SIjSHLEFrUZUKa8Gd_rkOcE4HF84gAVQlYhpVXSS7IZtTj5l5jQ0FYoX98S3iSIBeoJo6reo5Sk7MT_3_caAA2jBYAZeGyCgJv6B5MrbBb4rzBm34kfLA4IplsS_7DZ0wlDZsTptB_Y2eeMYy_7tU6zI1KqN8Fj5c5s9pkTbwaaiIUp9bHAiYzbd9Fa1QlEwVkE3G1gCHyNXX_rZDf1C3FIHiQ8b6kyRd8kFW9sXhQOIKQf28gY4NGNIT29mhs4sdUXuznvUc5RpOF4rWB32zXFtIMjEzP5zH6tL5Sdshv4QN9iQx24MBbs5_GYaCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/92364" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhCNc7_LAvOKBl3_QqOhY3nZr_GMvfOGOOEpRJmEzGrXE_RX4nPIwVTqHWHkM_L8-flD1pTiWvpz6TMTjYwSRmiQHbcqByt-93jploubmKeo8OVV4bFvqlH7x7PhN8yL2MzA4cAugP39RckdIsDmbPHAEafH5egG3oHlnGLA6MaF1zmDjXKQklQKZ8GljtFDddRlG3AFqrPZBvL7XhYmTQhaKZs35b32Xp-xiyD_ptJm6tWC5Ac5Ti2l-lGJJ-hOYNrd9fSyh_n3Q0bYQahbNkcu2SOv-C6sK26PIA9zfuN9htTGecUYxUs5vGiVgN-ydNgfwLQlr7QC6qhytOtRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سیرو لوپز (خبرنگار نزدیک به باشگاه رئال مادرید
:
🔹
یوونتوس ادواردو کاماوینگا را در اولویت‌های نقل و انتقالات تابستانی خود قرار داده است.
🔹
اسپالتی شدیدا به کاماوینگا علاقه‌مند است و برای پروژه‌اش حساب ویژه ای روی کاماوینگا باز کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92363" target="_blank">📅 20:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPQjrq4yO4P9WcijHPlwTGYCAzHAQHcej4AAU-F6iK7YBedVtgioIewprS75v-NOZ38coZH8YqafUKzttz2WbhSd27JW1TO3RuLLL1Vy30yswJlt1lzChgLyVcgY67UR5KGjNqZOyldFtq5fxUQgKZAfXH0s5-os_q4QHQ5AjgD2bGHOTdGf37WmCy-lINsT6-P4RYC1dRyD3AJ2NH79LdDFaMI49vYpVKA37NcEuH_Ys2n7R2iflJ3JZNE92oDpqHyzvl3jUtE6Mw7UL9Ak1Hb-REVxWBxv60JBJZLSVwzecL5C1R74HSnC05Rc25UsSirGKsGKcL_lkvjhJ-oubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
عکس رسمی تیم‌ملی کرواسی برای جام‌جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92362" target="_blank">📅 20:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇨🇦
هوادارای کانادا کمتر از 3 ساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/92361" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-jdPk0ux-azu7-mDKSqRAlr94e-7eT7qCQ_R2yHpe530ra73cedCLcCUvWcYqJGUVpt-1i8gy3EO7MsYSvtiGZyw9HszUZkuWJgmYMy-WSSSVjbX8UlNuGsuGCNa7KMaql-C76s2ch9IulSBxLpNT6GVWw8b67dqyi-mWHpzYC91i67lEqnilkWI1r9S0gf2IxYD8mU-o9ixSbZL9SooLWuOrLCWNz466YwRpPgBlYq30ZXQpNerOBYF70E2zrnv_xJlzORjsnm0ZsrSX3GFplspOEiq9sTes52hjgEpsjbOF7q4-I1fhcfPLBbtMt9gCUJIq9-aQCjRvf33n_MXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
رودری: اگر ازم بخوان توپ‌طلایی که گرفتم رو‌ تقدیم کنم و در ازاش جام‌جهانی قهرمان بشم، قطعا اینکار انجام میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/92360" target="_blank">📅 20:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c3684885.mp4?token=Fe-99b7znW8GrOsEDExqWAWpSWmWQHvdrCDv2oaNh16oaBy3Pk5F-jF0j_RC7lrHBXExyfyyQaB3yxIGFHbex2zCFKLA-fk11xpvvJGKNtNQD5AyiFBUP8SHvZgqVHMLzDaNWESTxFuT4tX57D0p13V1NV8TWAc4y3WWIS6WKdgolfPNdvwy-WKLojMlRm0yFKvqr_xuIVTpiU_XTv6VEfomSaTs3zHhrgji3slHfHMu7WS7Q5pi6GDRzly56dxgAXCMSGIbgz0MGm4v9fyr92OPgJLcaSFRFvDZfseWnz42fuVJ8XKtcp0CNQNi8aorJFUtG4fp-u7v7qo8tCcgeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c3684885.mp4?token=Fe-99b7znW8GrOsEDExqWAWpSWmWQHvdrCDv2oaNh16oaBy3Pk5F-jF0j_RC7lrHBXExyfyyQaB3yxIGFHbex2zCFKLA-fk11xpvvJGKNtNQD5AyiFBUP8SHvZgqVHMLzDaNWESTxFuT4tX57D0p13V1NV8TWAc4y3WWIS6WKdgolfPNdvwy-WKLojMlRm0yFKvqr_xuIVTpiU_XTv6VEfomSaTs3zHhrgji3slHfHMu7WS7Q5pi6GDRzly56dxgAXCMSGIbgz0MGm4v9fyr92OPgJLcaSFRFvDZfseWnz42fuVJ8XKtcp0CNQNi8aorJFUtG4fp-u7v7qo8tCcgeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
پلیس در حال بازرسی بدنی هواداران حاضر در جام جهانی:
آخرش فقط
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/92359" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ لیست اولیه بازیکنان مدنظر اعضای‌کمیته‌فنی تیم استقلال که به علی تاجرنیا سپرده‌شده‌که بلافاصله بعد از باز شدن پنجره‌آبی‌ها درهفته آینده برای‌جذبشون اقدام کنند.
🔵
پست گلر: محمد خلیفه یا علیرضا بیرانوند.
🔵
پست دفاع وسط: مجید حسینی یا…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92358" target="_blank">📅 19:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf073331.mp4?token=t04m7Uwf3-XSNFLwF0txINoHc4l5vIN9V-IGeU2YS0uxZe2tLj2Ym9SJ3sKItATg4FS9g9CoZSE4_IfgNMV1TCo1Mbx7POvb37Io-pMge1lSAkqmF7tDiouY6wWKCX574Tz8c2bsAhZPBWl0Hbe1GSyO9TtwdTk-2GH0z2CNSC543JMGuOO6Pey5sdaetujIu5za4EHtqFOv4K8KedaKh6mx-qbhN-gRnE7lI8Llqwi0MrNk_rTDBbrH0cWXRSfRJrTgXM4iC7Dta4y0LohBXNnJRCOOdV14N3fnL41ndIA_plYERquCxuOayd5KMlL6IZGm0sjEvTtXALN2KN6k5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf073331.mp4?token=t04m7Uwf3-XSNFLwF0txINoHc4l5vIN9V-IGeU2YS0uxZe2tLj2Ym9SJ3sKItATg4FS9g9CoZSE4_IfgNMV1TCo1Mbx7POvb37Io-pMge1lSAkqmF7tDiouY6wWKCX574Tz8c2bsAhZPBWl0Hbe1GSyO9TtwdTk-2GH0z2CNSC543JMGuOO6Pey5sdaetujIu5za4EHtqFOv4K8KedaKh6mx-qbhN-gRnE7lI8Llqwi0MrNk_rTDBbrH0cWXRSfRJrTgXM4iC7Dta4y0LohBXNnJRCOOdV14N3fnL41ndIA_plYERquCxuOayd5KMlL6IZGm0sjEvTtXALN2KN6k5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
احساساتی‌شدن عوامل‌برگزاری افتتاحیه جام‌جهانی حین برگزاری مراسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92357" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ3z_qkliz0FbGa7ngXbvDT3LfiaiT7cqz1LCpzK9Mgu3XMe9pfZfI1zTkiuORX5bdoo77z2nlOjgarr9q3aemW8rbJTN-p-Or9ztNs_7ssCQYj50oKYj64MT8HHrALnilD9_g2-S93uT3ninBo52TV-U6nHxzeThRShKCQ6A6wJ1YmIPmBqTwJF6LOYIYivEYjujOQVVihqA3shT41VlMWcpZhv8YD4CLpi0PXbs4ZmRydUs0fNkiORbSZi1eP6AkHdOTGmaF1oYyhjadBlVc_NlMLuVZ5xg1ixSFeNa_sZVfPEKzknhVQ45FNHVMApzeshHUDcKCsRJvnmQM5tJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رسانه‌های خارجی از تصویر قلعه‌نویی که منتشر شده شاکی هستن. این رسانه‌ها نوشتن که سرمربی تیم‌ملی جمهوری اسلامی برای نشون دادن دارایی‌های گرون قیمت خودش که همون ساعت رولکس رو دستش هست، تصویر رسمی جام‌جهانی رو خراب و زشت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92356" target="_blank">📅 19:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92354">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-VayGHLq7PgRQ6cEGnlEnvgy-Nl38ukLwIkVIIHtnJTODZgCymesCR6tyMINYS81yhG4XJA-bBrLshXBcNj59l9cfZudgXSJsohB0CqsKw2OL1jwvQKe7XrvsMGI5hVt74cnZpxTq6mTNiX24JEPBreCW_Xw0B7oazG8ZUABR6IRf_X43r7BAxgzPZUQJM_FFanaQyLNshibSSg-Nb3AzS2ld9EGMA6dUcGce6N0WDO-6QdRyrrhjyoV0Vo8EQc_Y9y2AGTryb2ArXojy6HooD72Efc9_LdGxrrPazUqxzDJFmku6Xvn2yWaTlb4XQ-4NqttPABNeRiZ9b5OvVIHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فووووووری
🔴
🏆
هکرهای مرتبط با جمهوری اسلامی، مسابقات جام جهانی ۲۰۲۶ را تهدید کردند.
🔴
🇺🇸
گروه حنظله ادعا کرد که پهپادهای متعلق به دفتر تحقیقات فدرال آمریکا (FBI) را هک کرده و تهدید به هدف قرار دادن رویدادهای جام جهانی ۲۰۲۶ کرده است.
🔴
❗️
این گروه تصاویری و ویدئوهایی منتشر کرد که ادعا می‌کرد از پهپادهای هک شده است، اما نهادهای تخصصی در صحت این ادعاها تردید کردند.
❌
🇺🇸
در مقابل، مقامات آمریکایی پرواز پهپادها را بر فراز استادیوم‌های جام جهانی و مناطق اطراف آن ممنوع کردند و همچنین جایزه‌ای تا ۱۰ میلیون دلار برای اطلاعاتی که به شناسایی اعضای این گروه کمک کند، تعیین کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92354" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری: باشگاه بارسلونا قصد داره به اتهام افترا از فلورنتینو پرز شکایت کنه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92353" target="_blank">📅 19:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92351">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8SCehcOoXI-clMSqFMDcRMOaVlb853TNaKrGCMEsvBow_fdtKSl-RACltfoz6QiC1tx1QMIXGCEFevyV5ud6oBolYpKpB7o2gBNr8aluqvb8fi0Ss5nXkHApP06YZkeADCnydswqhsDL_OXYCtshgE1Z40jG6lvmaZfSo7jheOTcyyOYRUwPeYybtS9Q1Wb7ns5CTIri98WqHgShonn9cEpWwXeuCH7X61gVOfpvmj2QHBEJ39vlDdYXZ1b8_xeKLPgI4rvJ5yAmrKmBy_WDobqhmh17kA_OP3kUvbgvzbxPphHrmfFBeYu0WNoyuyUCiXkawObZkQbik4SCp3tfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#
فوووووری
: باشگاه بارسلونا قصد داره به اتهام افترا از فلورنتینو پرز شکایت کنه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92351" target="_blank">📅 19:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92350">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY0g4p_E4wIRZolI7UlgLVIGMBxhirAR1Efb_TStUqjBYdB_IPiYJAgSNKZxHvjo_g5Qvz4XXT36EK7EBQy-e5f9Z7qqsUL4F6is_iq67Ya4FEY0uB4sCDExHUohub7P_dpCQ2oAcPNdB0HyiB04GFllemL3LSozEVfKWE1YXnjteeg_xllOFz6SoXmS1RP4sZkBhrvOP5nbEQOOO3qO-MAUNjlADwvvvOeXHL2Md5BHm5avAKR8udSon5tbGY1PKu0Oxu9iQbTEST-kGh8bcX55Dr6gX7DLDTXmLyvTWu2SVxDMZ_4X0bCSup_zW064ptQ0n2E-Fn3--ksDJS0NNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موندو دیپورتیوو |
لامین یامال دوست دارد در دیدار اسپانیا مقابل کیپ‌ورد از ابتدا در ترکیب اصلی باشد و این موضوع را به کادرفنی هم منتقل کرد، اما لوئیس دلا فوئنته با این درخواست مخالفت کرد و از او خواست آرامش خود را حفظ کند و به تصمیمات کادرفنی احترام بگذارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92350" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92348">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BqVWLYlq-H_L31X0IZnCMhLUia5nKy8Y4SZ3n-7FqvGsk_FiBMSGBUBaFJhF_8TuSxXD7jTrNSWFhMbZOauSc2Egx72C1lYWHRaghOTiBSo-PACC4eEl2pRVAG2CSdDLSY_1fQ8ILlPrUqnft_CoWl2UCMjBQhBo5XWyB8GnsyKJXeN9tdm7YE0nbISgA1ncoL0dR21Sfx6K3D8lXbV7MFSeV9P4gHnfDwbb_XgF44zfLAN9MRY9gpEr4IVYUFf-sgRzoK-1SlFkqZ6ArXpcZIjOOP35WObE3EmCbluUODizfImIlLxRR1NeHX7J_Bmj07QfSzTM9ybK6k2r6ftIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VEUGu88nQ5W1SHPUOcAs0IE_7FzMEwW-lYd4u6l-4WqbBVReDvci30N9qcEtcf_iNZDz2HIROJcIl0sTzDvFCcqriRH7_eqij3rjk_cJvLDR2yRCzuh1-I78jOzisboNjQtuzp0FBIYzRpGFCXnmfkAhVxgahHRcDGfIKgSWky5Y4HBxx3Jglgf1UNs9zZ2OHHMc4WUklB2-0lXiw9ROfF3IjpFGtPvsIEMr5wdm8aJDxJHnMIELRatpyIY4adtIuiDnjeuxYd2Zx6yjUbiU6ekx26N-YV86mGPBkHLe8fZ4beWcGoEVyC6voSOfUnM0pYRGkdBLE8ikbQU3e2K_mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏باز خداروشکر Puma کاندوم نمیسازه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92348" target="_blank">📅 19:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92347">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ByEYa8a1s0yGndEFdvjH7IOOxv8URhqGzc7d1B3APxeDSpq4Mrd37Gn-T0QL5WH1ImOqwHv1yaqbHwZb6oTtlI-y7uBeGZNmaFYSa8Cv6DE4dKjjhdA3H2gplhxi6ilp2yfnXw80rvhNAlt_W4qNC81xFaXQ0lGDsnXISMTU3OhRJZpxMxJqGspPLYkMZipLoG0a8TLKARwQh3QwnghCgiSSlRTBaytTdNPqxtB12ey6JSD9aJigF2M87GADs4rpzTBBJaW1NPwdsuSEmo1NcC2MMufBsP7OK4Bh9AKW6xB8m3iQBhxEkR-O-cdHiLXFH_8jmMCkW_ZRV9pipTuYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فورییییی از عراقچی: توافق اسلام‌آباد تا حالا هیچ‌وقت این‌قدر به نهایی شدن نزدیک نشده بود!
در ادامه ترامپ هم توییت عراقچی رو‌ بازنشر داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92347" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92345">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0OPMD-txCyJmH4dWadu41868XWiR0qwWKofmac_tQ4kt-zgD6_eSnn1GOAFuPYSgcIpdUhM7ieuRRoadaR7RP-UUkMgw32s1oKmK6lBf-5pgGQftaJtfDPnX17UF2wyTlPN-MJ82ckZp2RPEv_lhUxCWjC1UWJM0L2kijYyQDAci0ReUC9n4DsBfUqGNSmzUHg9AiFkcY5tKCMKiaVOmYHIrehjr7NktmAhLjrc4tA3HUJZwDHBT52mZGJmz9mjkld-tA4R8oaQe6dTvhuirbjANEOTCxqf0_l5Wpi5ixSyQGJ-RCQ3kVkBRzRpVpKvQq6L3_-_VK4B8fnOZOJDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFT1mi8mRX_27IpClGmy_SPaTdKleNxuS3RYWES43afMvX5p6keO75l1nBwUUqlzo2B4iGLn5wq2X40I-Ek03hDs8s_eQXL7pnrmlHiTMx4wVRyHyD-yYiQNU-Pj4zvWTn3eXpK_Xyfvc1qr4_Qt1ZeGq3rk3wiBi9J4_c-NrWZyZgIFeL7WgMKSXK4BvLLZOabKTNGcUaNaT_EXgwECYX4pssWws_QjoNp3CgS6du-lNwxEKYiTO2ZtRA7CNNnM5VEfUxwivsVmXqapMuSx2kKyGRBsMmcbdEtLn9ePzgb8Kq4MABemMfmpnhQfM9XuInIldFNGYjYO3idgUBkJFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🔥
بازی فردای آمریکا تو ورزشگاه سوفای مقابل پاراگوئه‌ست. بیشترین هزینه برای ساخت یه استادیوم تو جهان برای این ورزشگاه انجام شده، با مبلغ تقریبی 5/5 میلیارد پوند. استادیوم سوفای متعلق به استن کرونکه، مالک آرسنال قهرمان لیگ برتر انگلیسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92345" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92344">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🙂
🇲🇽
🇿🇦
داور بازی دیشب افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92344" target="_blank">📅 19:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92343">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyhe11lF0gqT9chJg0R--cVqMf7zbdzH7X_8GpEABR1ZfQOf_sZ1g6vpJkcviJsOcNQHtF7Aw-IdzzeHvZM6vnROx46EMVWRnBDrVFeiPgsNc_iHXqZ4lb-mXX8SC1NNnaGjd57El2TCEGn9E9T14Laz87WwK79AN6XvxTo5OFqLE8eRx4hO9Wr6zPAbegkiBNJfN28F8o7gxgKs8VdyX0i5oTVj3m3VfntPzOevvONrnY0Fx0imsVHL5fph7hLg01ttdO5l1iy-BANxkT5IAX0MFYZ3-kAn66JRM6FiDGH8UK_jO0p5HG-ayqO_d5aMl6BqdqxrmCqk-s3LUGmy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاکا:
🔴
اگر بدترین قراردادهای رئال مادرید را جستجو کنید، من ابتدا در کنار هازارد ظاهر می‌شوم.
🔴
تجربه من در رئال مادرید کاملاً کامل بود. من از میلان آمدم و در اوج آمادگی بودم، و اگر اکنون به بدترین قراردادهای رئال مادرید نگاه کنیم، من در صدر هستم در کنار هازارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/92343" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92342">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=C5ZNjXBPsciIntwFVWJiTXMybVvNgNFxoUMgjtA8RiQv8zAkZ9lAADiAzlNd0ogh82fzjAU0lSuSnYPY8IW3nE-8mnMWvdBE264bT2S14otVGTHkM3rhgNTiSwnbB7swzoOsTgrAU4o8vl1zIdONep5vVuxj04l5yq6CA1FfCApcJaWf_L3O4kiNaeeoYsCnO8JZmjc6hfrrFEndWP_4vA3SVgrbhVN8ZamQi3vSNlWT8_OXE2XZ7lxRyqMgBWIovTamCpCd60HufqwHqNPGmg9uERAxrPiSNqX2g6xBGCuXy_1VAbHpLyCWWgYvVmDucbNA7cZRUwOVjgLbWeFd3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=C5ZNjXBPsciIntwFVWJiTXMybVvNgNFxoUMgjtA8RiQv8zAkZ9lAADiAzlNd0ogh82fzjAU0lSuSnYPY8IW3nE-8mnMWvdBE264bT2S14otVGTHkM3rhgNTiSwnbB7swzoOsTgrAU4o8vl1zIdONep5vVuxj04l5yq6CA1FfCApcJaWf_L3O4kiNaeeoYsCnO8JZmjc6hfrrFEndWP_4vA3SVgrbhVN8ZamQi3vSNlWT8_OXE2XZ7lxRyqMgBWIovTamCpCd60HufqwHqNPGmg9uERAxrPiSNqX2g6xBGCuXy_1VAbHpLyCWWgYvVmDucbNA7cZRUwOVjgLbWeFd3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
فوری/ "
یک کیلو طلا
"، جایزه باورنکردنی برنامه جدید ابوطالب.
استودیو "
پامپ
"، این بار ترمز بریده و با ابوطالب برنامه جیمی جام رو ساخته.
🚀
🚀
🚀
جالب اینجاست همه میتونن، با روزی چند تا کیلک ساده، بدون قرعه کشی از این یک کیلو طلا سهم ببرن.
🔸
بزن رو لینک که زمان خیلی مهمه تا بقیه سهمو نبردن. ...
👇
👇
👇
👇
-
لینک شرکت در مسابقه ۱ کیلو طلا
-
حتما بدون فیلترشکن وارد شوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92342" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92341">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c13f2711.mp4?token=ir0NPEftxSuN94o9njQMle8XjoIhIpRkLcyrBIFhOU7Iu2Hylxsv0-JPVevpIlk8_BQGAUlWddigsu6vPv3olRn7iqmTHVgTZQ9Hmlgq7vKD74BeKpjHCEF2rtNYoweiqHNoSzgAck0wTd-90yLBu71C5JR7l5oVXMAo1xq1B3EI5JJiD0vbZg-p6TvBB9RRDXhhk8YYcsM8vDb6-V__lwD95N6V99oQupJGSiaHx_1BqNRmNHNdHQZm9qMJP2ktqvUfjNyrtUx7TMDRaK0x6c6ngpPFAgp5rPJ81uTEfjOnMFaIijXLXZxUTjcpE5f4xK-UO2mWL90YNM_5FywgmpPZGFEVxco7pbN_V2-dG9XOaNS4BHdlPz9WHyABttQSX5Fev_wViMbnAL6qqU-5nmrLi_MwdBPw8WdH3jckV3yKrBuPx9FreG745tRimxNlJzRTjh4_iTU7zlnvJi0udFG-zheea9Wj2po0pQhMov-vxEn73Zz57r3BDlhkjjVwQlNBg4Ct9NPElPQ31z5mNJKKx9QYulu0b3_s7MjjmoGiSYMkVHhin2su37KApfo--V1z2l8fvjTIcRxirANLAk0Tdai3FurgsoFvk9yF4Y_Kdr9CsoLNiMNGPix_2GmDnZ_XKqUr_xGmzEi2mN0xS7qnAn9geQt1n_v5wkvthjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c13f2711.mp4?token=ir0NPEftxSuN94o9njQMle8XjoIhIpRkLcyrBIFhOU7Iu2Hylxsv0-JPVevpIlk8_BQGAUlWddigsu6vPv3olRn7iqmTHVgTZQ9Hmlgq7vKD74BeKpjHCEF2rtNYoweiqHNoSzgAck0wTd-90yLBu71C5JR7l5oVXMAo1xq1B3EI5JJiD0vbZg-p6TvBB9RRDXhhk8YYcsM8vDb6-V__lwD95N6V99oQupJGSiaHx_1BqNRmNHNdHQZm9qMJP2ktqvUfjNyrtUx7TMDRaK0x6c6ngpPFAgp5rPJ81uTEfjOnMFaIijXLXZxUTjcpE5f4xK-UO2mWL90YNM_5FywgmpPZGFEVxco7pbN_V2-dG9XOaNS4BHdlPz9WHyABttQSX5Fev_wViMbnAL6qqU-5nmrLi_MwdBPw8WdH3jckV3yKrBuPx9FreG745tRimxNlJzRTjh4_iTU7zlnvJi0udFG-zheea9Wj2po0pQhMov-vxEn73Zz57r3BDlhkjjVwQlNBg4Ct9NPElPQ31z5mNJKKx9QYulu0b3_s7MjjmoGiSYMkVHhin2su37KApfo--V1z2l8fvjTIcRxirANLAk0Tdai3FurgsoFvk9yF4Y_Kdr9CsoLNiMNGPix_2GmDnZ_XKqUr_xGmzEi2mN0xS7qnAn9geQt1n_v5wkvthjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
برخی از گل‌های لحظه‌پایانی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92341" target="_blank">📅 18:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsW2gqeYtAOW7HbFdEhOO2kyCdgVm2gbkrZRAhRKX86wyanAk39NSQE-7XdLjcvwQXNzUcZhHJZYKfzWDlZuVUy9FV4hopLNoqBupwXP1459glEwoqftomOjekK5g0H8-4kBG34UJtqaokqWzYhb7l41nmy-Q4K004W2lxoqCx1Sj8k7IermOSfFo-QDR65Hyx5alwbUAoinkzrp6_mphMDVdM1CF3JOWEj9O6qZ6uhFiyruEBUiuNk_Ysr8Wwm_2zcSJJ10-BbBxuuzVXBTFpKrxnwJtZPnVBD4HXFZhVekHjLqfYUG0sWB7u93id5cu9DrvGUkVhKZS8gndJ-qNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پلیس پروئی دیشب طی یه عملیات غافلگیر کننده با لباس عروسکای جام جهانی یک قاچاقچی مواد مخدر رو حین افتتاحیه جام جهانی دستگیر کردن.
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92340" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Psawa6hyLfxx0BRGdhAxdXH99prrE5shHYEvbEsTIWZL5ELc0GypxmmU0l_V_uzSD6TkGGu2DL5WqlOgM0cciNeA3-eybPL_DI7gEXcTgEe3t04ddZJklOovShzOXK0ZPkYv1LfWCCuoGUxkJx15jJyNJudNV9zYTefhQRjgRiVYf68Zsbusl1ugD4ZtPxNduF9GcDsGcIBPUOV1yxWodwGpQmLfdq2-QhbHyLrS1ONhXRm_KHOTq02g58c9GR_ubUd6ut0c8Xl7yTXK0s2fnJDL7z2DqGwPeeS9Nb2xh_clY1JMakQfBEiHF29EhmpRPrIcoTFfSkGyVzL25FCrvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رسانه‌های خارجی از تصویر قلعه‌نویی که منتشر شده شاکی هستن. این رسانه‌ها نوشتن که سرمربی تیم‌ملی جمهوری اسلامی برای نشون دادن دارایی‌های گرون قیمت خودش که همون ساعت رولکس رو دستش هست، تصویر رسمی جام‌جهانی رو خراب و زشت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/92339" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-l4pMAzQJ43wZ8v6TY3Ay8romytX4woUvHQk1LJFD4-kaX_WBK17QsL3JZMoI-5W5oGgBQMeYh2ro7jbj-CnEm7-c7XCGo8SnGRcDI_44L2yTja_Z1RrndhOwrpYcWlqmGCC05GNL7GfHbtpkU73XVfPENo9R60Ajb1g6uyBPxNnkX1d4abQBUxEjPOTU0OUYGIsXZZgmjRjt4QFKPJfyCkxVP-55suVKeNh19dwGev1yZnKhPOcf5EhEw8zkG5pNkFKIEtTsjHv2O1q-cxRn_81c-8_vBn77WorufagnXCNdp4k5SKDgMvTqHZJr7QNKFCNUPARsHqo6FKEoVJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏆
تو کل مسابقات جام‌جهانی گذشته، ۴ کارت قرمز رد و بدل شد اما در بازی افتتاحیه امسال با سه کارت قرمز داده شده ظاهرا قراره مسابقات‌ خشنی رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92338" target="_blank">📅 18:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92337">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rai-n1fTmqkIUuhw3wkWKx3h7NQaY2PQtHI9KqUoRgqSi8fIyZVgUOxSyOmpE2bcpsogfe_VYVmowN69s_AbkI383yfqGW6dlqq7trIKdhfcNWGHXfUKJh8JDTXuK1O0htyXMOtMXMLFWwwxqZ6SOy4AEz2CfrtwAJVrZMKsVt1bVGZVV2SfP3HsWqbd5ZMeUx080GP7_bKa-3kwNoEjGIZz5eydHlvMMBtyfdVWeNWpPGVblu2gkci_2lE21m9hGZoqMZbgIj38VeUF86biA8Z_sj9cmHW1w1wr6m32nZ8PfGVG1M4qLZcg-UABnYlyIg9u2cNEnpPibxlWaEc9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
🏅
🏅
درآمد تیم های ایرانی از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92337" target="_blank">📅 18:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92336">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLKJFk5PLKDWXkklkfoOtFbGYPDgp5cDSiFN9TPxyBd6_0Zwz4G7LQUkTXP-p48KIIefG9a2MFOCzWsYerGLERxz9A4aPOp3rSBXrYKYBQCY8A8OdBd0pigGJE-i8ACDTBnnh-vZQ_YurGSeJvx52xzq5vHOM6sGV8syPDvNBwK_mqLaAm7gVCq01bXktAhpTVahTH8xfc8ewxpW5o8DMx1cEfTB4DAZp66qP15JMUQcwQdVziFPlG7UlNfa-8EqpMIkHnR5sHgBdsl9-v2V3PJpkI2RvgvyClFzi9TScR1KmthFksB6c-9pUXOk7aOne5lLPY1TBXSf1wTBc489MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
سوفیان آمرابات:
رویای ما قهرمانی در جام جهانیه، اگه با تمام وجودت بازی کنی و همه چیزت رو در میدان بذاری، همه چیز ممکن میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92336" target="_blank">📅 18:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92335">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0993fc7eca.mp4?token=gJeK_XNRn2ljv9Jr61YCnpJUp55mCHNdFwbSi-Xw3u_Kqd2g7lMDwXUKCCr8htrFEY9wg9MX7aO5BivXEDA1JCJig5xveXTni43KyYICqGz9UcmvtvMMqBGrWHtwyjlAPwvOZQ-adq1h-y4653eJoKUUkRCn9o4HMw03ov0ZbrBbsAKMMCavV4ZgEYzARtD59JIzIAfy5lS4fB8qry1iiLWL0LAGfx92r6f7-eLE8-x48_uwejJ5FeVTOT2kaoQMixzowOwfOU2uni29LKVfOgC2fgfEZuonbbNA0JyYbdOQLtwcZuufyi0dimmVhs-F_QuSQrm3RW0S7c7R3PTDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0993fc7eca.mp4?token=gJeK_XNRn2ljv9Jr61YCnpJUp55mCHNdFwbSi-Xw3u_Kqd2g7lMDwXUKCCr8htrFEY9wg9MX7aO5BivXEDA1JCJig5xveXTni43KyYICqGz9UcmvtvMMqBGrWHtwyjlAPwvOZQ-adq1h-y4653eJoKUUkRCn9o4HMw03ov0ZbrBbsAKMMCavV4ZgEYzARtD59JIzIAfy5lS4fB8qry1iiLWL0LAGfx92r6f7-eLE8-x48_uwejJ5FeVTOT2kaoQMixzowOwfOU2uni29LKVfOgC2fgfEZuonbbNA0JyYbdOQLtwcZuufyi0dimmVhs-F_QuSQrm3RW0S7c7R3PTDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهرا سامی، مجری شبکه عراقی برنامه جام جهانی هستن
🥰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/92335" target="_blank">📅 18:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92334">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051f0d1e00.mp4?token=huJ0LGCJpBEJakGcSYMTl9-4DtNn2b4NoXBS1sa-6_h_12YtoqDP7eLxly5InS-d_Qrx9UfXgPnSkqBbJc0TRJw9H184Q1jhOlPJ8X8404GlPPEcudzoUlYacmZNgiMagh-ERFYqCyZLdZ04tQIb5LLY4pE-6kVdJduvggzOIK4Y8utc3u5_5Sojnm1s1zo0CZftRHzEITvO6xaRNDUE6EtGzrIyss3tqvfdDkOQqJOwg7SaDgGoZQVGeZiJAUw_fgcyrThDmYIZqG0tho3Hut8qf1d_6TvAZzqnJFeg-OF27JRISGQmKPztbV4o9fzaDD4BKce2NGAqqiM6bHWNEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051f0d1e00.mp4?token=huJ0LGCJpBEJakGcSYMTl9-4DtNn2b4NoXBS1sa-6_h_12YtoqDP7eLxly5InS-d_Qrx9UfXgPnSkqBbJc0TRJw9H184Q1jhOlPJ8X8404GlPPEcudzoUlYacmZNgiMagh-ERFYqCyZLdZ04tQIb5LLY4pE-6kVdJduvggzOIK4Y8utc3u5_5Sojnm1s1zo0CZftRHzEITvO6xaRNDUE6EtGzrIyss3tqvfdDkOQqJOwg7SaDgGoZQVGeZiJAUw_fgcyrThDmYIZqG0tho3Hut8qf1d_6TvAZzqnJFeg-OF27JRISGQmKPztbV4o9fzaDD4BKce2NGAqqiM6bHWNEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکالمه اسپانیایی جواد نکونام با پائولو دیبالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/92334" target="_blank">📅 17:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92333">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718ad0590.mp4?token=q9l3P8wzJ4sWkhrRw47Svbzz0doJLiExRiqakmRuyk1t7WE_NaGRM-Q1hE91SsaD5aGj1fbuX9hgqgHqVB5FUM6F3mC_nefx8Q0KXAA7JuF-wb88ttyPuk77OgAHtKgoFBIiBhTO0n55EaIH_ORsKjZOTDhsKA0zJNaex4avH69yB9fql0hSiZwUqsYdcxqvvRBfmQvW1-Km7kj7wznx4h-L61xh-x7De4BYwFfM-Ad5chwS5TVKtwsbQJ6HrF4VhZXcGwKSTRDOVkaTy1__cAAcaWA2SJh1ogZ63QoGBz6mHaG6IR3ofzk3LGox3ZAjweGlaa0zvSyNRbpzC5qTpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718ad0590.mp4?token=q9l3P8wzJ4sWkhrRw47Svbzz0doJLiExRiqakmRuyk1t7WE_NaGRM-Q1hE91SsaD5aGj1fbuX9hgqgHqVB5FUM6F3mC_nefx8Q0KXAA7JuF-wb88ttyPuk77OgAHtKgoFBIiBhTO0n55EaIH_ORsKjZOTDhsKA0zJNaex4avH69yB9fql0hSiZwUqsYdcxqvvRBfmQvW1-Km7kj7wznx4h-L61xh-x7De4BYwFfM-Ad5chwS5TVKtwsbQJ6HrF4VhZXcGwKSTRDOVkaTy1__cAAcaWA2SJh1ogZ63QoGBz6mHaG6IR3ofzk3LGox3ZAjweGlaa0zvSyNRbpzC5qTpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عیش‌و‌نوش کره‌ای ها و مکزیکی‌ها در‌ روز گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92333" target="_blank">📅 17:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92332">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2cc8b70f.mp4?token=UaStG10PCwRIBF_2CqntdonCArGkNSN-Z4l784O2gOy-9hjBF3BhyBkc68XNKTPCc-vb9G9wySi7hiJaFesavuDDPGFOvD2Ku3yF_6HR56TWnHmwu0MlgDPu9VVIsQpPJixFGokv0cn-aTQtDXQ5dgW1wQWeppA9g6ge4G7_0WSrp2Rg-vY_a0cenV78dyQ45TFUMxPF_hKAdzFo16ClI9JEwcVeMFxBHwi5E79MLrW_Go7lTntg-YOi8QxN-4f9QRgaUL4CbJsnhw66qF4fQmVIhzaK0_Mxt7Vs9j-D1EhJquQz75AXEIPkkUPQI0E0yc_OxQwrDABhJbnP6w-sOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2cc8b70f.mp4?token=UaStG10PCwRIBF_2CqntdonCArGkNSN-Z4l784O2gOy-9hjBF3BhyBkc68XNKTPCc-vb9G9wySi7hiJaFesavuDDPGFOvD2Ku3yF_6HR56TWnHmwu0MlgDPu9VVIsQpPJixFGokv0cn-aTQtDXQ5dgW1wQWeppA9g6ge4G7_0WSrp2Rg-vY_a0cenV78dyQ45TFUMxPF_hKAdzFo16ClI9JEwcVeMFxBHwi5E79MLrW_Go7lTntg-YOi8QxN-4f9QRgaUL4CbJsnhw66qF4fQmVIhzaK0_Mxt7Vs9j-D1EhJquQz75AXEIPkkUPQI0E0yc_OxQwrDABhJbnP6w-sOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری نیکو ویلیامز از خروپف یامال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/92332" target="_blank">📅 17:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92331">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=YGRLqRTDzV0JibC_YQACF6uYC-RU9PGuIT2iOdqbrEanhajwRqudq73HqVzyhmeImWpa6iFLDgwJMYRmviyHdFHuh1L-uzaLU8hgHi7BDGOjZUQaiYDqA8RTRCwgHcwCned_aL6ltYeumN27qkKhTUzL82Tk9Co84v01h4Kz2MAquEqdbRqM_e6E6WVSqW2Oq9nlETfnkWEXcOIvq605cdbhokcn5fTat1nMNQ2GbDN7JyO_Eekyp3g5TvtbkGn6A93QDqOGrb_qr0W1B_FpPW0o5V2W3rF-2lDOd7l5mIEkIXyvXkowYx1quoUCRSWARUsLApRJoHCsm-kRmbx1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=YGRLqRTDzV0JibC_YQACF6uYC-RU9PGuIT2iOdqbrEanhajwRqudq73HqVzyhmeImWpa6iFLDgwJMYRmviyHdFHuh1L-uzaLU8hgHi7BDGOjZUQaiYDqA8RTRCwgHcwCned_aL6ltYeumN27qkKhTUzL82Tk9Co84v01h4Kz2MAquEqdbRqM_e6E6WVSqW2Oq9nlETfnkWEXcOIvq605cdbhokcn5fTat1nMNQ2GbDN7JyO_Eekyp3g5TvtbkGn6A93QDqOGrb_qr0W1B_FpPW0o5V2W3rF-2lDOd7l5mIEkIXyvXkowYx1quoUCRSWARUsLApRJoHCsm-kRmbx1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
🟡
اون چیزایی که ج.ا برای رسانه‌های فیک‌نیوز درز داده، هیچ ربطی به مفادی که به‌صورت مکتوب روی اون توافق شده نداره. حرف‌هایی که زدن، از جمله اون بیانیه ضعیف و رقت‌انگیزشون درباره توافق، هیچ ارتباطی با واقعیت نداره.
🟡
واقعاً آدم‌های بی‌شرفی برای مذاکره…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/92331" target="_blank">📅 17:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92330">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
فووووری از رویترز: توافق بین ایران و آمریکا توسط جی‌دی ونس و قالیباف امضا می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92330" target="_blank">📅 17:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92329">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e50671e6.mp4?token=uKrBYGUW604tt8_WQed2dKrMeR07U1fmVSfAHuEYiFn_ufjXUbiIMHY3wpC1CRa1Q60Yppg-9In2XEQpvTiVQbWxUbSle3F48mS_Erfy4HPoqnOhmgmbcJ7KiWpJ75S16Ldogtdd1Pjfu4LTxqhvTXhJWXwkhkrAZuzJkusrJvKrCc2kueOF3Pciaj3V-GIv9JLAmY4IU96nyv9So7Sz68FohKbJu8OKA9AiaOA4_Sq5USIFOZbVqpysFTcqItnVZAmzYpuPI4xhCXHx4DoScQSXzRmFGvLc3AhO7DHCAwiGHiBd_b6Xr_fjiPv2YGVJiULg7bfBW5_sTr6uBo0ytg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e50671e6.mp4?token=uKrBYGUW604tt8_WQed2dKrMeR07U1fmVSfAHuEYiFn_ufjXUbiIMHY3wpC1CRa1Q60Yppg-9In2XEQpvTiVQbWxUbSle3F48mS_Erfy4HPoqnOhmgmbcJ7KiWpJ75S16Ldogtdd1Pjfu4LTxqhvTXhJWXwkhkrAZuzJkusrJvKrCc2kueOF3Pciaj3V-GIv9JLAmY4IU96nyv9So7Sz68FohKbJu8OKA9AiaOA4_Sq5USIFOZbVqpysFTcqItnVZAmzYpuPI4xhCXHx4DoScQSXzRmFGvLc3AhO7DHCAwiGHiBd_b6Xr_fjiPv2YGVJiULg7bfBW5_sTr6uBo0ytg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
ورزش‌در خانه پارت‌ششم؛ برای دوستان گشادتون که‌ورزش نمیکنن حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/92329" target="_blank">📅 17:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92328">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e115a319.mp4?token=RgFPX_N6z3k2-TToL6f3QraechP_o0S1p8aRRiS-97Nl6yxfYw3FQekQ46s6sI5o7mfHJygRkqOzEBHSD6hjPCIHzsw-wyXH--x30kQ0mamkVp3CYbufWPPE4m_fC4m9woCPSkUznIFY28YLeFHKEeQPes3mFc5INObCRJltbgqFrEF90XFLqFpFLFbD0yprMMu-cqzwUYrr0hzYjfCKI0b0CuFcyoc6-fsc5wVYar9py37gjRQWrbPZznNseG4aKx_zGjAGGk1XVkq8o87EPzVy9N_jNECT4ZMbp8zu1kgUJK3gB8j2z0jxB7Zun3Yei27FN1a-R5WivJPoMl4SOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e115a319.mp4?token=RgFPX_N6z3k2-TToL6f3QraechP_o0S1p8aRRiS-97Nl6yxfYw3FQekQ46s6sI5o7mfHJygRkqOzEBHSD6hjPCIHzsw-wyXH--x30kQ0mamkVp3CYbufWPPE4m_fC4m9woCPSkUznIFY28YLeFHKEeQPes3mFc5INObCRJltbgqFrEF90XFLqFpFLFbD0yprMMu-cqzwUYrr0hzYjfCKI0b0CuFcyoc6-fsc5wVYar9py37gjRQWrbPZznNseG4aKx_zGjAGGk1XVkq8o87EPzVy9N_jNECT4ZMbp8zu1kgUJK3gB8j2z0jxB7Zun3Yei27FN1a-R5WivJPoMl4SOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناموسا اگه اون ۲۰۶ نمی‌دیدم فکر میکردم خارجین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/92328" target="_blank">📅 17:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92327">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHh_Aw7LJErEDQi6x5ox5RPZhvMI4qvwiW5tAMzYdUYU51alEivhbBjssOIgEsMk6o1NSZfbCQkm2zcXQCh1Aaeqj0hBlMrcxynqQiu37xTE_H-xa-LMvcmql6RAPbTHCgvusCX4rgpcD5RZm22EwpiYC7qMW2mGWy0bctOSUQNPmI8SJHVveqdGDLEtSF7D8xoECmz-DH6H9ht_VRhAmaCxHskgNAdTZhj1EqYl5apLUAcTZ1WauPxJrKOMSWkaAiqsGWPuzhZwo7UFeCjmFXWFQXdaRea_PXujaz0xuyaLNnannzh0Ddrfy-7b2UL2Bc_ahFMMwgDNKyCG0icD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏆
با اعلام فیفا ادهم‌المخادمه داور اردنی بازی اسپانیا و کیپ‌ورد را سوت خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/92327" target="_blank">📅 16:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92326">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukMlo2-CO2tTm230drA3hYoX_qAiL7YpHflGwS6RPT9fhPA1xu9qeaL4lqaHcfY37dU73MH2Y-0clK2Zw3h-8GxcWuhGFWd_gejQW55uL_NBwJ1oam8Nigr3PYTzuWyD15VBTipGdW-NTA_SbLV3Osvam3b17z_xeqIa_TSkkv9meNJchHa8MJjVHT1WDuHt_VK59z4BF1-vekuXbuR4mLm0KljUFi2pISlymouYDV2SCjF8oDCamUg9fisQziUO9crDA5z0RKaHn5gCS8rRifO41zZHeD1XBWhE1pHwlxNRkFMeWSZ3MVcFR990nCjqIrqXRxyamvV7tFhpXGqD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇧🇷
#فووووری
؛ رسانه‌های برزیلی: وضعیت جسمانی نیمار خوب نیست و احتمالا سه دیدار مرحله گروهی رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/92326" target="_blank">📅 16:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92325">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tchPx9yFCHmmPWRwGwbOc7GRARQ-qS0IRL0Oli5mb6JbmAIViFlmBktKEjaQlBlA_pdiEkCnzx2_wGkcK_CptB3b4mvVi1JoJvIi-q2Xk0YAUiGmoJ7SX9XKMgo2dUuMDx9fueYpbiXINPCtYzX3E6P3fth1abATveEturu3vctZCKlMs_vGuOQMjiufrjSU7UdmFI59Se4RlHxC4dNyPaUsSyPwsmbviRefRNVhJ5YpDcXMjN_l3YxqFodc8n9POrKJ_SJHomprCclmuEX56t_2Jh3JfoNN50H0cPhjlsEqTqTjwnIRv1ZPCUDn5NQAL_LiczUFU-lYl4KF9f-hDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
🇳🇿
سزار راموس مکزیکی داور بازی تیم فوتبال قلعه‌نویی و نیوزیلند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/92325" target="_blank">📅 16:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92324">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbGYc8y5vJhMQiFs8Whq1rR-67y7SWq1qud19JEpBVUUiq2Oj2h6SFdyr6EFcsMWq2u0QLtuk3PAySWcH2Yl2GfmvbGDResTYa7xCSVJx4hF3MSQfILkHGYk1z-WUfz54OsCUjmc-_uOHz82dGiCbDKQZdROrNtF98Vgpa0ZqGndL9NL2R8aYLqe6_fcNkMUNXSMguuERl9IqbYaD7lOKuGFiF80uACdXhWn67yDSQAfybJh4yd3WNfm65Mvea36itDJ6IiW9MQ6PS61gcAbmhAr-K8R-hiKHcOuDqZ8BEQSQ2YSNCEJmN8NmywQWe__nYmCRiZ43TDArbQU6-dgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از رویترز: توافق بین ایران و آمریکا توسط جی‌دی ونس و قالیباف امضا می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/92324" target="_blank">📅 16:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92323">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8fe0259.mp4?token=S5hG_uyJUr6vrXrvPTbZom12zUNFtsCYtKJaRRMfj24ksRcC7uwQ6EALJ-bPw7wVholfLtobYSxRVl2yYICtpEg0mbvhbvXsnHi4edPXCsyM4cQdv6knzhJ4ihZEcf5xWtRxii26GBnpAF4a9CO9teEk-huysab4Fu6URadVNHQo3jBSG0vmG_8xsrmnOt8ilRH_yp4wKNR72zprWd9gnakYk0gJoyM6F0sUKCXILBQtjcTq_-p9W2q78Tm7LLncToR38gh3lqOXnidQT1itqjjhao7AtZXFhgU-YXWopp6fIDIHq7RdsjfNBVCvEt-GPg3ZXsMpDA7EI-LKFMJCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8fe0259.mp4?token=S5hG_uyJUr6vrXrvPTbZom12zUNFtsCYtKJaRRMfj24ksRcC7uwQ6EALJ-bPw7wVholfLtobYSxRVl2yYICtpEg0mbvhbvXsnHi4edPXCsyM4cQdv6knzhJ4ihZEcf5xWtRxii26GBnpAF4a9CO9teEk-huysab4Fu6URadVNHQo3jBSG0vmG_8xsrmnOt8ilRH_yp4wKNR72zprWd9gnakYk0gJoyM6F0sUKCXILBQtjcTq_-p9W2q78Tm7LLncToR38gh3lqOXnidQT1itqjjhao7AtZXFhgU-YXWopp6fIDIHq7RdsjfNBVCvEt-GPg3ZXsMpDA7EI-LKFMJCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
عشق‌وحال‌ این‌روزهای هالند‌ در آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/92323" target="_blank">📅 16:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92322">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7Y64qnPJWxJMrsoHG7Dm77UJmyIoX2yRir5SwgsC1wjLc0plzAJQ6GhvEb5n0262Yl4yp2Zg6hjUZVSDQeKCwiS1lFaHss3BKjwwlhG-RHGeo3L4JMA0ZiO9MXTxDjutEN3SEUSg0Cd8uFw6E-EdO8gfU-KImybgEsmJI1OP90H5WXhz3p5SoDjj87lqfAWQS5qImdPe8zbzAxp0RaQ1CtZH_cBclNf4yJWHGMDLA1sJ25hFIAHIDfBOmTcGFw1fNwmu1xPJf8hZ-PbS9YNelmAEk99gjsksJjsFWpip9okWdgmHiGuA2T_dyQc8fR5-REHU4NYM5TJlMeMqpBJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣️
عثمان دمبله درباره انتقادها از امباپه در اسپانیا:
آنها با او بسیار ناعادلانه رفتار کرده‌اند، مردم نباید اینقدر سخت‌گیر باشند.
ما کمی بیش از حد به انتقاد از او اهمیت می‌دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/92322" target="_blank">📅 16:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92321">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyeMEVBuUFf0Afc21eEdGOiDatRJaqtgic-C_J3994Z0BctZOYa0OtBnJiqtIMqmojh9EYaxeTmQWpjds3IRZXd27BzZql85uMb-zDl08LzUVpC1hry0vA8P_IVQGUa058vw4wWajvnv7no1-dGlJvI-f3E3MrZeQrz7GxL0wREaNezPslu7jskN0fLnrQ7XHGEg-WWUBZftqlftu13iLtzOy_9AcLQbjlzNg2P1ZW_PgkMEeQ69OoYXzR4vt42WpQkvEzJ2G6TtlgT4iT-UhjsZ215wpmJ8IyILxV8PmMxMUGaypdJL6BKVn3blLug8-jdgdBdi0eTF6HLvUE5Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
گاوی:
اگه با اسپانیا قهرمان جام‌ جهانی بشم موهامو صورتی میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/92321" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92320">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDQ5LHZpdzKouk0C8SSIDJbWN_R2jvWXfDZpGLukxMqRiJ5mUfrJBSkvMei_RGgy-qDUwxv-h1suy4pDNQ7UJie5sy-zWYhfSeHHryxsCfb6qHg6mfJ0EXkzt0g9AmMDXsnlq5k_3S0fzF0rJmb1jpsAuE5ZXzSN3cUm9mwR2zhXnJlzQPMqsZ7OtGW6Y9R_MeEeLzWXVQlG1srGr1D4lk1PYoLGdc09D8nM4thd5QMB7FBe7Nk07esQuem2-l56qfheKUZ9rNEHYe_GSsfRcAZ6BR2wNCze2gL2a5dY9JyogzD-eGzU3MKN7H_eJ0ZG4puSrNLSh3tGvZey-aqd1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
این مارکوس پترسن نروژی است - او در پست دفاع راست برای باشگاه سری آ تورینو بازی می‌کند.
🏆
✔️
او در هامرفست نروژ به دنیا آمده است، که به این معنی است که او بازیکنی است که در جام‌جهانی از نظر جغرافیایی در شمالی‌ترین نقطه کره زمین به دنیا آمده است. هامرفست یکی از شمالی‌ترین شهرهای جهان است - این منطقه به خاطر موارد زیر مشهور است:
❤️
خورشید نیمه‌شب: از ماه مه تا ژوئیه، خورشید هرگز غروب نمی‌کند و نور ۲۴ ساعته تابیده می‌شود.
🌏
شب قطبی: از نوامبر تا ژانویه، خورشید طلوع نمی‌کند و دوره‌ای طولانی از تاریکی ایجاد می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/92320" target="_blank">📅 16:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92319">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6xEirFMzH5N1Rui5j_X7XBocFj0ZbWlwD98Knk3VTtP2TKZbNx7l2PJ6r6CBwf0stZSZZ5gZXZXizubBq9yVGIQGAOHZoK-1Bh6cy_rV7grHMpGc2BQX6CJGvwUoDIia3Hxd2wnoq2bnrRaTAQRVkNovvW2D-LJsCZmaWgb4ytqDazB8Fs1bnOwm61LwSAj2CmYRLHpxenM4zd1U_LpfZ4JyanIEbU4u-CjUoJTZ31VMv8qJX2upnRzDCLZHuyXsrdbtACsA1nkqcRHf3-UVKqbzPn25HFRKB1XVsAMYaFne3d36wVN0MEblO85U9zGGCj2j7szLJ6lm66Nqo-dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گویا برنان جانسون هافبک کریستال پالاس، با لیلی فیلیپسِ پورن‌استار که رکورد سکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/92319" target="_blank">📅 15:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92318">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a9fa2e76.mp4?token=riMJNzEycfgEMw_SaCemw1Q4Za5WmkcfwPQY0OMrHQnVpC0Xjb7UJ1suxZRZJOOYzYL0zJVhhSk5PcRXjxvK06fK0y3Bm3YRCGgJz-xNCthDMrYpQsTVxZ0-1limYHuIk9Dz8PqDn7youZXVBFi4JQrVyvJ9nGXYSvu4Vzz9IdtuUcZL9fOBbZt3qpWU57hgkZAS-HN876drkA--yHm1QARw3WhRGccvTEgZrWNpJ7hqSSUofrQZOGbn9aAkJS-unjTs8C9MAMRtbYpMosswD8tcbiOCaBN4FhVEjX6KKF_6PcQkmTvO2BqDOl8lixvspMJsLm8z7l_XzNIP_T-NDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a9fa2e76.mp4?token=riMJNzEycfgEMw_SaCemw1Q4Za5WmkcfwPQY0OMrHQnVpC0Xjb7UJ1suxZRZJOOYzYL0zJVhhSk5PcRXjxvK06fK0y3Bm3YRCGgJz-xNCthDMrYpQsTVxZ0-1limYHuIk9Dz8PqDn7youZXVBFi4JQrVyvJ9nGXYSvu4Vzz9IdtuUcZL9fOBbZt3qpWU57hgkZAS-HN876drkA--yHm1QARw3WhRGccvTEgZrWNpJ7hqSSUofrQZOGbn9aAkJS-unjTs8C9MAMRtbYpMosswD8tcbiOCaBN4FhVEjX6KKF_6PcQkmTvO2BqDOl8lixvspMJsLm8z7l_XzNIP_T-NDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سی ان ان یک مونتاژی ساخته از صحبت های ترامپ که 39 بار گفته به توافق با ایران نزدیکیم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/92318" target="_blank">📅 15:33 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
