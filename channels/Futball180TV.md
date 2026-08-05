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
<img src="https://cdn5.telesco.pe/file/iTBzodE_UCx794G3vGbEbUCKZIZSVFLA0j0AHhZq8l4mOts-zDCa-Qq1pMB_hKWwAmIswISzzkha4X57htRvf3lyytkH4UgnZQDXkDEml35A9JrfHtem5bM5vIX33sAw67DSHSO1CHlXCxC0Y-JSTVmThfvC5O8G5gjRgc__W_iDL1irWry24y7L6va47caScFBjUnoX4sGnsP228kTK7P5AlCrbT5uqgF7MNgiZR9AHdMLtzo1F4U5ByUG1hSZVHJMRMy8kdv0QFy7l6NzxLuKkIOhIkVFbQHO-r_QvZs321DES5hX0dxPSfrpUHT1kcOvPTYBMr0m_67uD13Tq1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 494K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-102771">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk0Ht8wM6WfATOrXKeCpJZgllY0nKBsd_p4-UvAjZfaIioq1II1DrQQvvJGN2ZACVcLdSGX3bi3z_O_9Wnrho2S6OiEasAuNzgIGLVRTCQH4xyAir9u5LVQ383PwEy6IkTXn3lqJMy79QQ7JVNydMWbY6f0WnbK4tSCS67KZzJmLVu9Sfd1ZJw5vJD-2aFlXlLsYCvOV7KG6lcJb7vpgEqhWvL4o9dBXOZDad72mkmeVDgrpd1dKMZb2FVnISe1BJ3T5Ksqe85fHO_NpYzaTf5za-6yDzYjMEXeBoNtVySz8AUxU7yTtdmUCkz6PM88-GMx5BLfDeIxCc3HqaN6tsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس در واکنش به هوادارای رئال که فریاد می‌زدن: "وینی، بمون"، با علامت
👍
بهشون پاسخ داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/102771" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102770">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی نیازی به تست دی‌ان‌ای نیست:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/102770" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102769">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ياسين‌چوکو بادیگارد لیونل‌مسی این‌روزها علاوه بر بدنسازی به تمرینات دروازه‌بانی مشغوله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/102769" target="_blank">📅 15:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102768">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
▶️
#نوستالژی
؛ مروری بر آخرین تیم قهرمان پریمیرلیگ انگلیس لسترسیتی دوست‌داشتنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/Futball180TV/102768" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102767">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
خیلی از بازیکنای جوون دنبال اینن که سریع‌تر بدَوَن یا تکنیک بیشتری داشته باشن، ولی فوتبال سطح بالا بیشتر از هر چیزی به فکر کردن و تصمیم درست گرفتن توی زمان درست وابسته‌ست.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/Futball180TV/102767" target="_blank">📅 14:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102766">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وقتی میراث فرگوسن نابود می‌شود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/Futball180TV/102766" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102765">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWLVSjpY8R-fTH6MeBdDzPG-8uswfQGLKQ8Z0e7TooU3YRSZ1t_Z70XRwZMrdA81nsWn5J3362sgaNHM0dtW1Cv2lH2b3nqg2jAYq1sxCQddG54v1D8y_jlOvzk5L-f8DHYTMbFxbF648C0fZo1oo_XY6jJ7ivIx2xCDx43i8lWDRbxSin-iwp_M_VeUUoVW_O0UokA1TMemUXsnS4k-wicT2CZxfTrin9dDkzUlauX9DCXsIKfhuBBi8o4fvND4HffCQW8RpRuzmCpMLYu8_WTrohFU-nNrT_6kpETk_WmPFFlGBAsiQZ0HmQ9nLda9mhRVoYPbU6LkAUPwimmOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔴
7 سال پیش تو چنین روزی کینگ هری مگوایر اسطوره فوتبال انگلیس با 80 میلیون پوند به منچستریونایتد پیوست و تبدیل به گرون قیمت ترین مدافع تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/102765" target="_blank">📅 13:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102764">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctDVQIuEVBf9PpBHSqIwcXZzfdnb5XndiO59QEDaryP165XTkxldn7AlccIjhYiittBsVGpkybOWV6FI2RaswmlSLLaaHVISCRG8eOmf9hnQJtSLLtoM0BwJ9rPiEnJExbzOGAj7vkqhQnVk8qmmIoQvbnmCSkK0Ed9BLOlL9uPWzVWyaC9xu9hDGNnC6_hW51twvfTtaNRKqn8vZPSqXuZgcpJrccjrIk3t46DL_Lis_zuctiVnFayXMQnfqZlfx6Svv13PNSoti_8B52Pi8bzUq97SSX-KkZoQneenbfjk_jT6b5sfhYnmyYJHfURKqAOZBHOpUWepRWWsqllxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/102764" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102762">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0EFZeN3xeLeUGJdDzn8tLmoMj1drgpK-Kmu-HXgg6wOePobzMGQhQeuGTNLQEs7J9ksuQB59Nuc8w09uMvCncWDprDvlHI2nKb5v1EQtAYJqa8npeG042epiMzkKiMDxlfSMzOMeW2Xz6eLH7MIUyRLUivA16GFEjkeK3jet328IVExHga83WhzPSb8-nc1xtGKIcyJflf6PgwZDFsHbQygvW7SRoAKsIAFJDoDmBMwIQ1G3VHd-Gy9p4-5G2Xxlpa1do0f27CyTvzBQm6qcrONC1kYubeT_07-8CGSPqirQX61kO7DjO0fi84NNHErIpR8lngkdeQMv0WEhcjT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه که بدونید فصل گذشته
فران تورس لورد بزرگ ۱۵ بازی پیاپی رو بدون گلزنی پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102762" target="_blank">📅 13:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102761">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
😐
⚠️
ارتش‌روسیه دیروز با پهپاد یه سبزی‌فروش اوکراینی‌رو تار و مار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102761" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102760">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkYjwiq0J5LPSPOdGRTa26jMTjxNR4AEasVyFHPu5FkvzG0QyhTgaAx0c5y3TiRGi--GIMyy4DcOm7tOrrNMfJzwsFjQntfpWLzF0d0cc4TRfi51cIaxoBevwVWM9G-orfDGvo_GamIxiDkby-hHcT2E98N2eKX9OAsqanW9zwBUhDyUnknzfibflz58WAiDgz6a_owDBcxQrGp-_GzZpvity7wSK-sl3Ai9BFJs02guUSfRShtukk9PtNejvljHXAz2peBawFBGmt8gDlQ9rNSc8kVAz5EHryipIoqnXYEQpuVPqVdXxWQTyEJuWYou_XEeBS7k7xSrW7pFLbgjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102760" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102759">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPujSNbe-ZyZYG-4f6FMpP9RbMWS4xCOXtY_-_pOr6OTJ4iFLyUFPb7vBF1alcX6plDOzA6XfRuAH8qIfrKFgNyEBhrObeCpytarQZOg7y5yKgYS4Svu1OqflenYGLRpqGPQeEMxW1XIq5PUt9YFjgLNtPBqwamVw207kepcWsvS8kXk5H10KHJqVGKG5k3xu82L-LFOIhAjYfFNfDEngWh3QIswAAnsGLnmz1W7kmZVxavxXo0QkTi2dnO_wpvnkXc4ge7bjuZRzoR351SU_8Mc4QVUMULTXCXX3BmLB_nT4zQSGjSeyF20bTy-5ekvk_UUKDPzXZhWXWWesqv_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بازی‌دوستانه؛ ترکیب منچسترسیتی مقابل منتخب ستارگان لیگ‌کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102759" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102758">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfQTDFqT15Iab5cY22cCWv8Rqz39gGqEniLvnsQwiTH5ZJlV4jEpnlfBxaL8lKrrYVOu7gEc-5h6y71mHYYSGOe3yC6KhtSL7rugBm1oylQ4MdsLglMjjhyco3V5Y5sGYE_F3a1gWA3lwu9mnw69WPWjUb20gN0lQi6Ideinl1cYiJNR2tURQj5Lu6yM9OXfIyeRa5m8HhM9EJqVt4d2mp8iyhSmP8d-HVuo3CWvZikqNwSNNvdDEdl56wa01VNtMEL4pznMpVuGpNKePEjIs6I3twpTSAOo6VbN9h8zjJKro8A9iy5IIPSboLSKOfaNbEX-O5nLm8JFILVvNAGcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
متئو مورتو: جاشوآ زیرکزی بازیکن شیاطین‌سرخ در آستانه انتقال به یوونتوس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102758" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102757">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽️
روایتی از تحقیرآمیز‌ترین گل‌تاریخ‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102757" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102756">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
تحول تاکتیکی تماشایی انریکه در پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102756" target="_blank">📅 12:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102755">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇦
آردا توران در تمرینات شاختار اوکراین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/102755" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102754">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بنده خدا احسان علیخانی خوب مچ میثاقی رو گرفت قبل اینکه بخواد علیه عادل کودتا کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102754" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102753">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpSa68N18Ni385jC-I9XFsK93hsPVoO9mwOxYwsCdsJC-MSeoQzGi8MIem5yOqlMEo2zTb9daJhEJlQizfQriG22oadLWFh_NbVH39c4i_1AtDeEGMj7lT8_GEbUCIEEfNvjHyCFAgzmQ9kyqfO7l3IzsaynTnHPschNzFFnXkfwP6Pg65ppqpnwqyteBPjQKvIHzrc6AkfSaSUn-uya96pldEhvvapbFkrYdWHxL8vEHwt1lWNK2eFtksyhH_JYZXAuPFkq3GEStZ7j7r-AubdgyfHBq_tM2bVoGEC5jLS8nBWk_LKD6ydRbwn9Z1xu1XPeVRhww730xaFMB142Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
بازگشت دیومانده به کمپ‌تمرینی لایپزیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102753" target="_blank">📅 12:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102752">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7jA_Dri-rABMwaaREtZH4-i-TRJsArb1LcAyrVemQi4VgQ4KDS50D7w2j9gx7DY7avEUd2MRpE-c3Hway-S5ze4O6fydr1pxP4wB-JrM43KXzPiR1E-QvIHlAQD3yx913LLzNlnUURN5NVIi5nl7DQKNvLYwl0xmapMb8SP-GMn1tbUvp3IebrX_oqyQPBwbM92MXihY_VDK6-IhlQ7L8HkGIOFWvNeMpzLsMx3_LBUigR6qLUzCIFhdJme1Y6wFXcnanrZTH6fLZARbuoP5FHvlmHXH86iC2UASshp36_ZXIFbUjEyD3MHVVbL0DJf8dFA_tPtHP7VJddOukMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
با اعلام رومانو، ماستانتانو بازیکن رئال‌مادرید با قراردادی قرضی راهی فیورنتینا شد
Here We Go
✅
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102752" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102751">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co_13zn0NENMR1Tj6xFSFyuZkzkUpot-bkeZ23kZtOhp9MtXEMgp54oeeJlQ4sZ6zOi__3VmDdazlCLs3Upmlai01t95wjswAIg4UlOid2SSm6OYXqJTuTqjl81G6XOl6mkkEdED07DpeJwyw75WQ5aa61MHyPLw-RqoRa1qDxafCqmLpCB3j2cgpPDs7fAVwc58AAUPyjboiiyuyvKiew5GCK2kDD-eH5pPAmSg8mmkZ-SqBvbts0GM7vsgJcsVHIOXxhbTURegxNBicxP8FcwltOi753tHN9FNuwGvzMO4XyB6wsKq7dwd8ZhBg-ijJoCdx9eRAGgQZnxW1U7qvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامین رضاییان رسما از استقلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/102751" target="_blank">📅 12:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102747">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YL5lan6UvaTHgo1s148G7UJZ7HeUmuYA1tNlT3maxCmQRAdrWE46EN-pVroSzxc9LZQ_0UAvvQ13zaqHMlDBGhnRu5nO3SfqigM2Dnf5eTc2iUV5MhIWR0HqdBQh5Rn8ttbwTGqLrIT_B7u9xA2PnHCjZU0yT83KEHbz4In3-ulORI_jcUAcQW83GS50lITXPlwXP9562lTp3J9V3VMimmaBcHUZVdQ-FBQW5EJ92sN5-P-Hy19W-JDT6BgJgE8dFcA6TOy0r0G1mIQQpKjY-4SUcsaGXxw-kLmreS9pl2bvPxGYdYACUuEMdSWVZiFrb0SI9qFm509fkQ_qkHb7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sii5pMjVrHeo5GNFhB8BXbgQ6gcAdOzMLgquI9_fm4vPxkQB_yRTVfupEcBqHIMxRFkTco0KhhlCnzUc4Bn2-CV-WY6yZQdy4zhz4KO7pwOS-Fd15MBCZWrX8uC7QPtqdqT46U5TmFwExdIAU-SEjiIwhBK3qxVBFpbmvXGLtE2Asb5SM9ECujExdjirIvZ69YfpkDjgnE6h0SQR4nXqHm5g1JCMpZUR-xeJqMJjeaVvUHI6YYgZLO7prYhsrkqiWULVcqVN3wBwKPRKP-k5awzjLxPvntgbTEgtY4KduYWbCuqRFrBxAFXzjkEKaizXI9QmyQR9q6EL3vIQkRVJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqYmCAp5ni6ukfeB-94lFL-lnX6QhMIwFY-bcI16UIkweNo42cNc8mlkBbIIeH6oOpuy4OHDYL6r80g0ry2pF8PHvBdbU5Igh0R-z-_24c6yjfbp-FOuYehX8qTi3bnWP9fUFd9939YPmBkvUtV92hCWqGYSmTJIVkXvhJv82N2i3flDzfAX0_9B_bgX6Cnwo69O9Sdi4NX0viu7eqHGe4gXG7HncWkZhBEcVpe1uxPY1ow0jDVGthd6UxO5bHdBbR1V7KtMyWTvlO--vM6HOeb-fGLzc-2yQFX2XvX29by-ZTddef79_OMeqV1OLqnEClS3vBpRiwd74nA1uTdP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d56wTIX-rWPEewTFbPyxpsXA19ff3_qgosvS5lpmWG9f1WXAXQVdZUJcb4U6wFczREpvJsafVki_7iZRdtWCD1vSfMx467BdEWyLSeY9EmcrnhG1bB4GDFwaIg-PgKTEOu6hZINTZKM8Ob2-VhF-cNLqaknloK4u9f_5Nhs00iexiqzZHTyCdWgDnyvaRF-7h7Kr298Bv3PkPhbEZdcVmO7JyvIE4Fj6Uxc_exQueOxPX_CHIny4pdTHoYwytgtWMEXrdFsXyhT4J4ul4hxwmoNQFcslkntsWN-IFhNN0pIp_we7SnDkBCklt1uziqAP0KYpSVN2qsQLioirpXvKdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔺
تیم کومو 7 سال پیش تو دسته چهارم فوتبال ایتالیا بازی میکرد و حالا به لطف نتایج درخشان با سرمربیگری سسک فابرگاس اونا فصل آینده یکی از تیم‌های حاضر تو چمپیونزلیگ هستن.
🔺
جالبه بدونید مجموع ارزش کومو تو ترانسفر مارکت تو فصل 2019/2020، 2.4 میلیون یورو بود و الان به 489 میلیون یورو افزایش یافته
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102747" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102746">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=CdPZtuUiHtjcU0Se74MsqTFrN_9wuE4mO240e-zy4xj0o7sm3nF-FR6x5kw73Vdwa59VILu53U8cFbOlsxBlMdWr_J5JXJl0WraqYGRm0nvUMAXj4dZm9W6TrKaarthux-KS-OU17qwjxY1qY7ZFY2QPHz_Hcgs53sb9T7JbGRFF5S31NIo0W9sSTgThIdLL3U2RJ2Q68YabJrmCVph3IM5gZV9eq-Wi74FL5gQIfIa0JXiTXkS9jR8MZzsh4vtECL68poDmRNjg5FGVFdYGMz76onfwbMnfHttkN1RfTiLaW7Bw2v6x6GogAVXWwAzNI6bICSVgBDU25Keng0tdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=CdPZtuUiHtjcU0Se74MsqTFrN_9wuE4mO240e-zy4xj0o7sm3nF-FR6x5kw73Vdwa59VILu53U8cFbOlsxBlMdWr_J5JXJl0WraqYGRm0nvUMAXj4dZm9W6TrKaarthux-KS-OU17qwjxY1qY7ZFY2QPHz_Hcgs53sb9T7JbGRFF5S31NIo0W9sSTgThIdLL3U2RJ2Q68YabJrmCVph3IM5gZV9eq-Wi74FL5gQIfIa0JXiTXkS9jR8MZzsh4vtECL68poDmRNjg5FGVFdYGMz76onfwbMnfHttkN1RfTiLaW7Bw2v6x6GogAVXWwAzNI6bICSVgBDU25Keng0tdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
✅
رونمایی رسمی باشگاه ترابزون‌اسپور از صلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/102746" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102745">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=VanuIwCO30UHezWf-xQQrwbejrr9ei77rH_Ee3Ilgy12RBHi0gKUlBSb8MT9pkPbwuLxpckt9vjW4YV7p3x-cuZWkUOV_M0Ko6HNdZIvB7UodnzPXz-rEuUxeMBmJt5riQzMDQUEdulGadEb6fr_C648fIof2BOYbUHS5xuJlMXZL5F3hQD5KdHYncUz5sfQT2gutGs09iVruVCV48vMWsuLMFzX9oMmhjLo6PT_FA7D6cgR70IMItuM9DtArEycT-1rRAlk86QHPm5WcwYTDOhrcoUMozYJMkbydSwTK1PgOWh4UBZKx9DBA_-OSJrGghsjxysk7LHqioQkd9i-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=VanuIwCO30UHezWf-xQQrwbejrr9ei77rH_Ee3Ilgy12RBHi0gKUlBSb8MT9pkPbwuLxpckt9vjW4YV7p3x-cuZWkUOV_M0Ko6HNdZIvB7UodnzPXz-rEuUxeMBmJt5riQzMDQUEdulGadEb6fr_C648fIof2BOYbUHS5xuJlMXZL5F3hQD5KdHYncUz5sfQT2gutGs09iVruVCV48vMWsuLMFzX9oMmhjLo6PT_FA7D6cgR70IMItuM9DtArEycT-1rRAlk86QHPm5WcwYTDOhrcoUMozYJMkbydSwTK1PgOWh4UBZKx9DBA_-OSJrGghsjxysk7LHqioQkd9i-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این وزن و هیکلش یه حرکتی کرد که واسه نصف بازیکنای لیگ مملکت قفله:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102745" target="_blank">📅 11:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102744">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcgxfao7r5GzxsxAyi5UWkDSCwxBiPv_X3E4l3kFu10a4GoSHk8weGy0tGyjCCecCWoC2KaiaqohqKN2NYwiIUEvACPbwHHJhKQmJiaFreTSHSD2b1QEpXMLAqv4nvGPe2QqetSQcZpiS5or2Hkv5pykn_NuWcVf4bgRnmAd_v31pNDNp-uaLzFZzi5YmYmfFC6A2C1ymke6xo-MtjBc8O98jNkYH4oteuuDkCMDr9zgErJQJPsgHp-43xt-6Yhl4Hd9TKn_g0RbndtWH79uxsN9MEcVLJdg76RMGS6C6M_XKJdPuSclEyXe_3muzUyPjrrU5k1owFo0TSCZCKknzQos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcgxfao7r5GzxsxAyi5UWkDSCwxBiPv_X3E4l3kFu10a4GoSHk8weGy0tGyjCCecCWoC2KaiaqohqKN2NYwiIUEvACPbwHHJhKQmJiaFreTSHSD2b1QEpXMLAqv4nvGPe2QqetSQcZpiS5or2Hkv5pykn_NuWcVf4bgRnmAd_v31pNDNp-uaLzFZzi5YmYmfFC6A2C1ymke6xo-MtjBc8O98jNkYH4oteuuDkCMDr9zgErJQJPsgHp-43xt-6Yhl4Hd9TKn_g0RbndtWH79uxsN9MEcVLJdg76RMGS6C6M_XKJdPuSclEyXe_3muzUyPjrrU5k1owFo0TSCZCKknzQos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚽️
⚽️
روزی که لیونل‌مسی به مورینیو در الکلاسیکو درس فوتبال یاد داد و پاسخ تمسخر سرمربی رئال‌مادرید رو با درخشش فوق‌العاده‌ داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102744" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102743">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102743" target="_blank">📅 10:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102742">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5hCqh6hweY2ROIYdQKKh60oRPP5qxThc56eESm1INiJgq3tYeD7oLFTzYVJGD17ihtxZKER3UsUQDHj1IZAwtXJ5U_sxTbg26vdVRS2FaW6hVDYM9s0lQnyw1I2sDJ2vNWFAfEqpgMRLsgMzYKRB3xgKab_OkZU9BuUps-HA17CaWebSQ_s7vo089re3ZnlFmfEKhaVtINzePm-ZfGAqnSEDAZSk_9fadWfB4Gga7aIHT9V6GdItEFEC5FP_XqKG8r5DojRU3SN0lZqmDVsFjGPhKMahiAFNHQbvSl5ZoQnZTgeBq-zqOuntylB_OabGD61_qrubLmMCH7_enpDqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102742" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102741">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=mxXnIw23c4QuXeQy4QSL5SdI-5ChX4SWg5wKNFq00haNrAZVwk4N5l5LvYWXrLNfZNrhAYoToUh_AXYz9r7Qp3avRCYs2aIP7lgVsaQkv4ToGG3ernEdSySxFM3-reCp1dx5DIdnYSIdCxcb8_G341cFWIuNkAGwNNbDRhnIs4K2PohstYwjaR2yCoY48wmO5jPbT_L2vmkC0XOQBaKQolG8p-HPdtsYIZKmn0AR7yUfmasykNjfFqkWeQQAcHlF8lcf1MSbkSZEnd6juGp3GnY3hQd2Uz8F8bC3ZQqmCHBYy8sdNLmEmmwH1xHfAZ-5sbHC7m3B_23Rsr2ZPTckCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=mxXnIw23c4QuXeQy4QSL5SdI-5ChX4SWg5wKNFq00haNrAZVwk4N5l5LvYWXrLNfZNrhAYoToUh_AXYz9r7Qp3avRCYs2aIP7lgVsaQkv4ToGG3ernEdSySxFM3-reCp1dx5DIdnYSIdCxcb8_G341cFWIuNkAGwNNbDRhnIs4K2PohstYwjaR2yCoY48wmO5jPbT_L2vmkC0XOQBaKQolG8p-HPdtsYIZKmn0AR7yUfmasykNjfFqkWeQQAcHlF8lcf1MSbkSZEnd6juGp3GnY3hQd2Uz8F8bC3ZQqmCHBYy8sdNLmEmmwH1xHfAZ-5sbHC7m3B_23Rsr2ZPTckCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
▶️
تیزر دیدنی ترابوزان‌اسپور برای محمدصلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102741" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102740">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op_TosdOOSN4vP8WV__uBjUE-z96cT7J-uZpgKa9_X87Sm2ekc-bYL_0n-SO9fmwIUZHmhzV4dM-blHh7RUm4ecAA1l468z3-ZandS5FrvXCY35Q7s4yWMU-qq_txT7CEwQ0FrGJHvYsEjBHgUkB_Fz4i0GJiZvhnmZJ85FwKe0abe2TKNT6t7hYn3B9bIiXv11ZNd3qNgFV_tEc1WPBLRPOKTGPppxZ1nPMhKrUyQ7jqHYA4dmiizUJdz5K6MQ1T_hzAqmvyr-NCPQFcAUXKCisoKPbcglosVYFBbzBsuS2ER2ndw8lliF0LjH6h1lklQMaDiimnivKUsMKGmKdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ وینیسیوس و وکلاش برای مذاکره با رئال‌مادرید وارد کمپ این تیم شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102740" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102739">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=gJVLkwOhndoFKZnDa_5Mve5NGebeH_RFb7Zs80fBUBAt6ZZzdoTnyGfOE3mdMUVQSG8Gy8zYMusxoNSZPvxdU4IkPK67bebTWTZ3HbUrhQHODDkGml83YoBySL9Ir1e69a5bWkvTxFyQmONlaa-2lxkVJHtAGIO8D93LjwMo9VhNjCRn9Y5gHlWFf3lCPKhad9QdxifvxuWev_zKjP4cZPE47BT02lefRdXaThtSu5jNHaf6jvGlMeRNuvWBwpJV1Q9UUvuHEanFrgOrPKlSs2atD_cMKHd6XVONKAU7Q3rcS4e4-bwrgbsN5KQL7TNd1_AUugf3CLL1Cj9se3f0c6AXZ-im2fcfja2midlPlXRqQxjuZBfr_CDOBY6Do8bH8UrrrriEBoDj0-evHx1jQHTnW6G0t0z1iN61cd5OzbbcQUqI8RdkxLXiiNp-s6On-3tbT1FuRlgK31lG2IslTuiwp-un2ZoUbYxvNsRu9y8UOqhJFP7Eih7k4MII7ZICjmNvnlJ1XOVLXcGXGco2P2QM1mOSOF1GyACkbWF6sQnABHopmeyu_OUVA2DEXGSRJJkJymRu2hBifKn90y2MQXZ6gi7Avmkk5WoT7OIyfz8PfKo1lmLrFUQNP6jJRa-Nx9YWHUm_ZPrBbr4v7fZLt16T1Exlxz03bzzqzfLkbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=gJVLkwOhndoFKZnDa_5Mve5NGebeH_RFb7Zs80fBUBAt6ZZzdoTnyGfOE3mdMUVQSG8Gy8zYMusxoNSZPvxdU4IkPK67bebTWTZ3HbUrhQHODDkGml83YoBySL9Ir1e69a5bWkvTxFyQmONlaa-2lxkVJHtAGIO8D93LjwMo9VhNjCRn9Y5gHlWFf3lCPKhad9QdxifvxuWev_zKjP4cZPE47BT02lefRdXaThtSu5jNHaf6jvGlMeRNuvWBwpJV1Q9UUvuHEanFrgOrPKlSs2atD_cMKHd6XVONKAU7Q3rcS4e4-bwrgbsN5KQL7TNd1_AUugf3CLL1Cj9se3f0c6AXZ-im2fcfja2midlPlXRqQxjuZBfr_CDOBY6Do8bH8UrrrriEBoDj0-evHx1jQHTnW6G0t0z1iN61cd5OzbbcQUqI8RdkxLXiiNp-s6On-3tbT1FuRlgK31lG2IslTuiwp-un2ZoUbYxvNsRu9y8UOqhJFP7Eih7k4MII7ZICjmNvnlJ1XOVLXcGXGco2P2QM1mOSOF1GyACkbWF6sQnABHopmeyu_OUVA2DEXGSRJJkJymRu2hBifKn90y2MQXZ6gi7Avmkk5WoT7OIyfz8PfKo1lmLrFUQNP6jJRa-Nx9YWHUm_ZPrBbr4v7fZLt16T1Exlxz03bzzqzfLkbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
نیمار دیشب اینجوری بعد برد تیمش برای هواداران رقیب کری خوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102739" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102738">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102738" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102737">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiIFWRS_ucmlZTnd_BK3z6FkYViJ0tpPApsAEQOdQIlB9olxF71xhRFp5rRmXPNGgOEdwF5I-Sp1zLCGC-29dFGi2FUnIa1reYcRAJsq-kY1qpcuIqU3uA_05Bm858YSkLBOIFtyzxv2q_pltzLHFDGOtLkp8IIgjSbK1X21XNvijAq7Aww7hmY6FzWQ6MtL9iQvm-0WgtEmEXia67h9NT3jm77dZ0zm9sSTdY5hRTEeDKjxj85fLdOLGX7qYtnBeAIfzUXyKqBYiCI3F5hTOnu8khIhFXKbpNWMhMaUbRvpknUarKqlMGokbow1kvBljqN9_UzeXVKVbRrXoRs8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102737" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102736">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
🔥
نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102736" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102735">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45508d652.mp4?token=H4l2AAGwvkbDYgv-u9qAb611oRD-TrU2OFCr-AAX6iNPIgx0jBAhn57NAOj1pR6_DXq5lTf4w_T9_7WWo0n678ifrMyJ5kZyro0Ec_mUwOz9aQ7Rh0_bWuX-_uhNIXJYIhO-gElMdLmZjJ6_2H7f29Yjpwrd_awQ2sMEiiY0qm4wAV_njPDT5dJS32rWmYg_9wOau3axahw08rChpixPKkyjEjcd-a1XacdNSUlbjAiMOUpICDByKrSowWHpenbzLG3Yx-PTAmbWtKmT-y7BM_nVC13aRDeJ6ovC0SK0F-4357yLyv3yun1Yu6aKoi6IIjNgUrzP6XQGwHHc8mfxMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45508d652.mp4?token=H4l2AAGwvkbDYgv-u9qAb611oRD-TrU2OFCr-AAX6iNPIgx0jBAhn57NAOj1pR6_DXq5lTf4w_T9_7WWo0n678ifrMyJ5kZyro0Ec_mUwOz9aQ7Rh0_bWuX-_uhNIXJYIhO-gElMdLmZjJ6_2H7f29Yjpwrd_awQ2sMEiiY0qm4wAV_njPDT5dJS32rWmYg_9wOau3axahw08rChpixPKkyjEjcd-a1XacdNSUlbjAiMOUpICDByKrSowWHpenbzLG3Yx-PTAmbWtKmT-y7BM_nVC13aRDeJ6ovC0SK0F-4357yLyv3yun1Yu6aKoi6IIjNgUrzP6XQGwHHc8mfxMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل مدنظر شما چیه؟
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102735" target="_blank">📅 09:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102734">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNQeJHdyp9muzkZy1Zp2Q0xGhyZDbSpIU0BZZ-7GIAvU3m3dygSECzaOVtkow_2ovT0juHckrr8Uaf-DjA7Mm9zuSFHVE-cQ9TPI49GVry98cLRY37-f5uHZ6udu_rEgyL9GTP8cVxm9sQHMJqdVbp0cnu9Tj6mAnzISWYe9Ndw3cyxm-Uw9P1DggbMn3C1hHesk54GXM9FGChA3VRaufVVDzfIe4dArc_HRr1popCQI7X2P4yZr83omF68ugW1Pql2moTOtuU1bG7IVagqI0kbjcIFgB2IHC1ehNc9XKeRY7mV7QmuBw9L0S8a-t2Vc_PM29zcyDn5VaksT8g_SdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🗓
روزشمار آغاز رقابت‌های فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102734" target="_blank">📅 09:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We2VHkbWPbPomLXdpthdLemoHycfiqL8nZkScy-6q9yXv-b9PEmNyfl1SpPZbXJDdWSoTC6m4FyeeeFTWjkaOybH98tLjB-Rnf58m719LUymANVfVaSN024e9FvgUEHhngUApNlt70EyUqfn1Snk-blv_tbiz0VU2IDwO2hSMPrQVRmZiUR31YU1Jk4I9iU_oWaxdwd3RSf50pjsX7Ex8--LaAMR76l3qo9lL8EuyXafMz0Go9RYfoubUgX6-xlNY7Oq-fOYXaxCdtfyHsWzQUrQBTkUjElUAXQpI1qvMNPIbtjybsoCTNHDkAu5xNlIRX_G9B2DbIMAPc80hjqzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیم اگه تا الان مونده بود کنار هم شاید یه لسترسیتی پرومکس میشد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102733" target="_blank">📅 09:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663702a362.mp4?token=nhFFO6n64Tyns4GC_vIs3re06ySMt0gVPtJj84vx46Kx7HwnzSdZc8Kvl5ciEl2-ERhBEvCEsexpkTJobWEOdiKUFIt2C3zixYpKuJHMBsyqIUYC1nvJ7E7hipSUovDWDE0QPLbBi1_EQMI4YUlJd_QBFZarcdxnRu8sKjNUvQqGdsKX28S9hA16GLBD-g1FU_x2TyJcuBVf3F_OhMS2AR95Gx_zmgD_GnuvcssrygSrIKsdoOgqibrS-ANmtEQqdh79q8xk7VZaVn2pZP3ZtbYRM-p5N4WgdPYFaEJcVLwV5zbhLFenwDf9StX-omo88rgT0rR4YlVcLF1ByWCHqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663702a362.mp4?token=nhFFO6n64Tyns4GC_vIs3re06ySMt0gVPtJj84vx46Kx7HwnzSdZc8Kvl5ciEl2-ERhBEvCEsexpkTJobWEOdiKUFIt2C3zixYpKuJHMBsyqIUYC1nvJ7E7hipSUovDWDE0QPLbBi1_EQMI4YUlJd_QBFZarcdxnRu8sKjNUvQqGdsKX28S9hA16GLBD-g1FU_x2TyJcuBVf3F_OhMS2AR95Gx_zmgD_GnuvcssrygSrIKsdoOgqibrS-ANmtEQqdh79q8xk7VZaVn2pZP3ZtbYRM-p5N4WgdPYFaEJcVLwV5zbhLFenwDf9StX-omo88rgT0rR4YlVcLF1ByWCHqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
دیماریا: دربی روساریو با حضور مسی خیلی سخت میشه، چون ما همه آدمیم اما اون از یه سیاره دیگه است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102732" target="_blank">📅 09:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZBQ0UvPjeSkAIM5XXQ05YZY0GM-uJoIobbeZkM-j09BjKf1kzh2FzAP0IsTzNEFBWHEbg0P6JPhcpEtjNvnA_TguQjRZs6_33zay_bPCly3f5oR9y7dKKNApxvQ5C8fkhCv_EJbrxZFdlgOExRZO3NDuugY0UyTn9HNxT4qZFW-O-I1OW3RYfWJG9foN44wJS3xHy8LaYoY5oLQav3f4CqCukR_JL7vZ7drWwF1XJJ2L-OZFPQUyrQM-iutuIdzRHfNr6uEXRFJFn9EvLfk2RPYtqf1CFDNpovvBvZOL7tPiBGupvuuAzX9w88PiCiORVvXkq43GaFAgle3v58npA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
💔
#رسمیییییی
؛ اتحادیه فوتبال اروپا، تعداد کارت‌های زردی که منجر به محرومیت می‌شود را در لیگ قهرمانان اروپا از 3 به 4 افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102731" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102730">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYxRQ_qsTry8zeXsnrjWUic4g9S7IonhTZ9SMBdFeZyyGWbcnovX6wqVQScVOXcWeSEiSecOmYThrKlexzKQT1PXSeamZZ23Ih0C0Af70cWodBLSj6A051F7rWmi8MZ3od8_ALuZ3zLajpGS49qiXo5ZCjZthYhbQQ7UUqfC4E3ISzX9kWxfbfyBaLF0QrYxLm90KUMCXGAarunLPliYMVfRmzoctfvejiTPNNDKQC6pK_zBohjCbRSUq623Fl9GqfURtn4ZfJa4xNHs6UGDlxX9oGLmChIfvKB2znJyiUuxTizIeeM3VaLHOXCwbAeDQz4QbmeMFrOcfYGIN9fs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ به نقل از روزنامه SER، جلسه سرنوشت‌ساز رئال‌مادرید با نمایندگان وینیسیوس جونیور فردا چهارشنبه برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102730" target="_blank">📅 01:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102729">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffk7-L3npFGMy0Flq_mWoy05F2RMmpl-LHSR0RJWoflP20YmUAPYzQRKUNCSuWJ_JeHhaSFDiF49inpzxv3sLlMrXQBVfz-7TScOYriOZm7Md33feTKsgJwIlkJcL_EmoSpCkfqp-ioBHl-Ux_NaQIiIj2QeFA7QBBTfl5s1OvEFGw9-1gZyDJ44-1-ReUZhc7T7pPqhBi4Lp8eakJPWw1__O7OWY24Ssq4cryHwGTFwED0w3-CksCDpRdkP_1tTib-HN3zBIhwI7QfmyDaMV8GwrZHn4SDXLbpEXLxCjAINbtWgORa9VqXSkyTswJvcDi2RsOwGGFJI5yEhhSsmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
👤
جوادحسین‌نژاد در مراسم رونمایی از کیت‌جدید تیم ماخاچ‌قلعه روسیه حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102729" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102728">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0hnk9ShkY1fzA7xMKcKzetk9dIdI2Vcd6ByScyE9BlBNfVR92_MAz9qmljanHcauAm3DurxUFxuPAzYG5m4tFfeCONJhlK6WLIE865hd0ORP5NoD0pumO66Wn1rDKirnYqJ9UzmYbM_-Fm7Yw5AqCQRlp2R9vetq1m-jyvhPlDcm8X8UNK66Wa40_x-29q3dTQ5IpgJU61HU2Q01JZZpym3WjbYkWgN-CHx6uAhNqZCl4kKgUOPHwCfZUA4CEJOYu6dilPqbRevUxr3PxmiAaVE6aGY8LyfyG8-ovX6iwdjgUg76kurVtjqynS_XoaGgF6WVtGs8zo5RP4OpteEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت انگشتهای دیدا در مراسم تشییع بارزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102728" target="_blank">📅 01:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=E14PUGz4yIVFO2LAAoORoo8injMsEWdIfNQ8NBbuOaTV_QUXKSdaH5C-GxEpImIHH9JLDec0Ur5aeHpDoQ2IXgQg85q4dEHcxxJ71XLgv0t83-_uRfILyaurE0xYUrtkaB5v7CC9c5HA3HEWg-IkJt-PV39Ffqg-6dSrzhfyL9Lh_EFrz4jUuECTD2XUur1X9SuQGwlfnwiAQJKNrmFOBpqVoPpdAJZXdrm8wTONeGaI8sWTuQCmQMYlk0F6eCeIVcRm91Z2dh7HNd-R1jyTIfaYPsRaDReRJ9vR0TmqKbduyEq2utY9BN5jUao6qAeoBYgptXbYBoyg_2oYIrzDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
فریادهای مجری کشمیری تلویزیون جمهوری اسلامی درباره تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102726" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5XIXA2DSq7M6FhIrJJSlyrKhvzzQqP4W58NrGobspwdImmBDpanBv25uZk0CsDeUbxI1BIL89QLqUDt_i5aHhawsQg5OunaSHI1N-3FsnXCNEUZljlThfCrDCoAMBXGwfCW-jzBIGwFEEjdTQCLAkis3o0kKwtJ_Dd-b3rsqwrVNFx5WcDnYTT6P0UByaQS3K1IRtxxwF9h4eKPCGwuVw5HzWAAkrJimY9iywgj0UlXcbVRLxWpa2l8cmVtHTycdjei2y0Ejz3Ta_GkwcFpwUFOG-apN8RCUS2Ec42ZG3kOq5ANl_C7ZnvY8NyTzTei6mgL3iQONrRCx3lOfKA6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
باشگاه لیورپول درحال تلاش برای جذب ابراهیم امبایه‌ بازیکن PSG است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102725" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
بازگشت ستاره سابق استقلال در آستانه بازگشت دوباره قرار گرررررررفت
💣
💣
💣
💣
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102724" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qWfzYlPl0Kvu7gJ6oRJFPqJngKzIQtRGeCqvUTCZEYAz1VgDuwLKH9XPZ5_dGkE3VG05ffE5VblPQ0thJbngueXg-Gtxqt457Yn_qyWTdZONkhe8Z0KHf6Rie6UYC1JKsuiflQ9-ZWqY7n4TN5Oqs1zWNnW50kvn7tkBSo4sUBkJDvEtIO506n2aONexXw0ty1121U6fpVGpaO-OJMVVMsdMtmJ0Moz6jWPEcKXMba7lT-hVOt5rA9okUuBPyDr9sg2MEDGN7DDiYdsCSKj5m1QPqIno9Z-WkSR6MspGukXbbokC2K3BB_K-RRxWdM5ztk5NeGEEqL2jbCzmzhHcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیکن را به استقلال پیشنهاد داده است</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102723" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102720">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUrPfvyjyjHWhr-To9k7TIIhq-6BkJFvqVduwjqd3YBG92LZYA7ggcAJob7y5zCEUB-AVAwioIK5a4PXRgjRaCKE8ffI63zTj-SxMirL6VT-d1OFHzQW6kDbO1UgDbW8ZcOMr0p4CWZKlxfdRjLDGXcj4dygW3sOMnFq02YC_LLiwpD1xyJqBCwOqozDHbiOs5bVTNk_I5CRf9UNhTCdYL6uWss4D0Mf2Yg4o7fJtak8aIwhllIYRJN8UJdWewLaFxSd41FDtqN1YwmDSj861Gk_FlkDksEI1GQih8UUNWngEukkJWy8kbsCHyV9Jq-AsiVdSUfHFKSpFGeq8ht6zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMIfFiIo9fn-Z9WaloJzMk60EIxUH8kEA2XZbp1ErWMHiaW8w3at4vLO3VVumQ9kyQQMXmqSY73Je_daIJdH1ZfK-eta8S6s1IFp36sccdCwYviX4me2h34_u41d-69tmOla17BL1_tHgZ2OBDWanOzzd3gEL4eO9pOzuoUTEkaUmabLk6puVNHvQ-AMCOUmTy4VocU2Bhq7nxFu-uvKEa7quzqB4fGNQ29o91Q8e4rgQEaDqbiPCmbNTgv2RRn_jsAB9xpWLM6-pFZsN_ugvYRyfWQZLfINiV2bejOLikUkMoEp5zW0bK4L6VKztQSkk271_G9i37nhwk7y4BFczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUrsmRM4w9VPn-Pl4b6TUn10qQf6JSmArSWtXUpCSHH-yrSAR0uO80w7CXX4-s0V0KaU7Omn1RR4__riTUDEAmx3Z273GoDZJOiU_ojNOkhNNYOKqcGYp2VlK54RSKK5kELQlxv4CSOZ7Dc3i5n5rQyj56sI8euLg0K36EqZWExr_-hFO-J7mtGFBcz_iuLW_mUu3EfnX408m7Ii_0h7yo_MuTDxz3ygBGoCfkbpVVycOcQ_pHkkp-fLUzMFewsj6KD6ZegmKM-UebKMYUXP-h9Iyntb-XmiCVwtraKr7TAUO8k4W-1_P27yaoJgOCSbXuxTUO6dtGWzSa44k4dzyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو اینا رو با کپشن: « اسباب بازی های من » پست کرده
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102720" target="_blank">📅 00:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102719">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhu0m8nJhuIwdyxLKTZkg-JDCLu-QGqKPt5AZO0zrhCf00Bet7g8O6Fu7YAT_HOvds6X6ayFZHcp1d4vZKie3SddOfjZ5lyXnSZeZiRjBT5YYhOz_9b5Upr_HYyWzWz5oWgMyrXPhChq8_SZp3mq3u1FPj-laA26g9HNkZZlhsZJgsV_dJZrqta5eYBKehR3oosjAMF13OFg8ty_k7ojBfwoiNRSP3tfzmWEvJabNagHWWIAtXPRB7cR1yDWM99e5aON2gzNlz2EC8ByP7szJfzjwdKjSTyA1o7UG0NPw9_W6vUafXBYsuPN2ZHxz3Jg4kxqKr49cN_5HYRjCUA6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
۵ سال پیش در چنین روزی؛ لیونل‌مسی اسطوره بارسلونا پس از سال‌ها درخشش بدلیل مشکلات مالی کاتالان‌ها از این تیم جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102719" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102718">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSu_oe_Auh7UGBMdqZtGESjxg3D3_xfnxPZrNIe75_RqGlU1RukzhB4oAT2sSl1L50Rz9U7bwnoHw94y_PAomZjIYR4C_R1dRu02R-Tl0F0dHYag6Uq2Gxye2ohyrWsxoQqiBxigXCXHvCfmX9uyRN4w5CCTUKnjXFUYh4o3v2sUYKshBCG_TP3Y8a06WrDkt04x7e0J1i6pU0nq_im_7wm5Vfa2AUSIQ2AHb5B4OIbjIDLh7xtDr1Ng3krfYvpST1ti9OZlzKqSa7OR6lt4Th1xtQ_fr_SrmFYu4EDLoI5ltDloATPtp0dBDFAJaLocW0IuRKCNiYD9Eb76WAydGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
فنرباغچه ترکیه بدنبال جذب پاولیدیس مهاجم بنفیکا هست و برای این انتقال باید رقمی بیش از ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102718" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102717">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfkrmJSN7-i8EOpu4q2hffjxJ9gEO7_ndi-d4nzTnTt1FjSFAeAWlvCBm3SJHRlnu492L4ySLJ5sIrWqNZV5m2uvJs60S096dE9bfrLjgvw-7IO05B1dAVmKfwG0S9ED-LIMETKCJH_OrGNuXJgTSjQ2JcqV6J69By8KfrJ1dqO29BCxI-7POBz3i5ggWAAAzCH5su-hwdk6CxDXu343L-84KFps3jZugBrThJgfpc4eMWMGY1M2WQxmnHTqDZIGuscEWb6J5QCy-39djqskQO7QHQ17y68J1wW29R0mSJw52S_z9s5a420SZJFzwsGO8JW_yOcH6H3qzAoRIPn9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102717" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102716">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NTHnxdxM5M-huQtcVp809YTbWQ6kB1C0HilXnsSshgFE5fgssC-0VZMqE2LgHiaPjEHFw-Q5RbVqSJeuemhdegJG_KfbVsrxkzEAeKKS1rLohyS4rQftuULAdw6q-xZEQ9xvg7k671-i5EbWchJr3UPqUZ79sUv5UpWxvLvudchHECkxXKQp757ELAzu2rEqCSRFSPayLg8vtp3-d5PEvRVvHQ_a-oULqVRfZ7Nv-WjNxO3S7k2D2wBcBt6hYkuD3pDUiSV4WlHCYHAgF04Rv3YypYw_UShFsXMhQ3YHkPTyE2Q8UhjH9LDZ1SKGpWDhE7zEPitSe5GiF58D1jlEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
جرارد رومرو خبرنگار نزدیک به بارسلونا: امروز تو مادرید دکو با ایجنت آلوارز دیدار داشته. طرفین میخوان هرکاری برای نهایی شدن این قرارداد انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102716" target="_blank">📅 23:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102715">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5UP0zJBsVhzhz1rvsLhaif0yXTvndCI01nd_n1ZuqRrlqhy33-eK-qq8uPHObNG8wHpVZw2i0KXN15DxAv-juTRQHXSYOshw9UYVXT0CbvZzJJiESsTLgU9Lu0RPDz_5HEUEhxLnpoX3Iky1paHvPqB91e-atji6Zwq1aik5PxWYcdiaW4-cgGpug0xXOjbocYy_H6w8Rw-XzG8QofYBGEYDQYpFi9ETchgGZeYo2wWa4Rs213UTB3INB2Cr8DDznetiLZWxwtluH4A42ahgYSMF4WCAbT7_BOL225FdVdmZQ2158va3KAMZOsZ7qrQdG2H4lvdybDTPyqHbXXvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو و پوستکوگلو تو تمرینات النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102715" target="_blank">📅 22:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102714">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hge0yQmggCcbhCBCydkdrx_dRg5IaEyciZgGKwobSeNuYC6pbTP5UQ95vfDtLdxzuOi9d8fE_KZJ4Pay9yXN3Dm8H2RHogQZt9QcfwXVNX1Xkbir4hBMa6vrwncpnALFaQIfPT26tTIarJbzKWiIYloivh1DjrXFA88myZ8b2y1o-qqNPe-TQC4XhF0O16_pANSr-lHboHJfiXt5LSMjvU7WSTdC0JZtJPebEl7Ro_D5rgfE6iYdeHsj-YuLO87N9gf0pzJWozVmrKH6XALR0VTMobRrf0F1E7D2hIlXdepRymflr7mZgzRV7tlkUcXOuMpTQ19q3A-4qEqviSWz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102714" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=hcv9ZNzKKEYGx3fQ1mEsPRuO4IebKZA7-9dwGeTBWNugq1vazLpo5NjBaMFeb-Vi3uy8KHXfF2df7ZJVrU8u3dQJZiGY8JA63UueMXhBU9DZ2-EA4-oT5fCtz-XatOqbbFog9fO_kxmQqnUcF67DvD8wj975NLjs1Pw3S-J8gjG8X7BacfddJIYkobRV-l1JD0X3K39BPRSS-tLVzvzyARAuWibE9q9TvR59jzPZ459SajXG8cBbIKyJekAoI6Dl0I9xdsYRWHx9on_M7KjasH0OrcX_-UwvZgoklHSgjaDLxCrVCsgJWmtde34BbU7a5DwFNOXBlRyfA1sOIO3igA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…..
❌
تصاویر مناسب دیدن برای همه نیست.....
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102713" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIHMkWJ2vBmylzIS-Xlvo5D7p9svGngx2OEn72UtQ1JclTUL2_fOozf7iyIRB6Th_R82lk-_m_nPe7r9qXY7n5Qe0rhoUxfwRzGL6wFOKMNFMHWrTJDUpJ_pQvjXburYMeRjBLKZVXwlRD2Iad-JPV1kZZJ3k70Cm0-f6UjRegAiVhqhfBDVxN79EbTe-fBQ-HAJOsLIBlfuZZ36VomZ6gCQNJ0dwrQQV5qM2fD-oALEuyw_f2GnP9e0Znyyp2rU8IMwB2zs7O91xl2OS9MH03YGQxfNYJnpMIB3y1SCieaeHI9PVv5egfgdaCwrfUmreU-mlfNt64uQ0x5m7F4SiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری از پسر تبدیل به مرد شد
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102712" target="_blank">📅 21:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrjYYzzm4Nojd3rztrjdBYfJnNfvme-4nxML7MRHOl2wqZfDUjHgSgnHoq2IHKmtSHQF6jiLXmb8IdelnaacpsmeQLphBBKdsLAzhXwE6_5labmj8hF7BuwTPUf0v8ytOgm7AxEGAzcUELlzAvhD4a-raebtZ0vNGUSA9cMwDmwbc1acOsFny3pox-cMUn5gXJkru_HyCidIRxzOgfR1OPmwf2HkOz06apYyvGNMMVmpc3rYDCsEZyAcnzWrlk3ViYyb4IQfX8tOFQsDXf-NEJbolmhhrslqY-HybN5bWRtLZCqamOQpGYSNOQsqa4Kg_QQWC236qTy-FxSWA9Yzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at9g2xbaGzqwp3pA95rm4JHP3PUxNMk5BA9tpjOtdtHECQ62WvfhXNi3tH2CZs3mpwWIchcvKAdfUYx7YC4Xr0pxghzWrgtEo_MP1ekXPw8RDIEAJqaTh7t1bhPvX6e4cK9PhEjvZeDatsJpfaAn2h7_gzJ4a28tAcXWKzQgOxLc89p4AeU7Z-LvMVcA4Of6j-ukvLLLuQ7XwdTMwQtMaqXR7u_0ywNQpfSaMLFIzpsSQ9Z6VTCMiZ30Wd_Kk4wsfAil6QOkQ4nGD4Tozqy-QdFCfwyac8QpFokTIamZTm_DxHn69GSpXxWEjzPiqQKtWTePak8BClW0cXdA96UxtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQXHb_NrD88CtofjrvHxRP-lOWSntXMUGfnWA8dps4UotwrkvWIRohHDRWNN6lzmteW4ovDNqkqO-sGh1MRam_l_loGAEkAtk3DC2PsTE8eBUhbPO-DrEcDovSJ7Vr6aT1GyhXXeAYCH81RtlYc5X5CYRbsAvolYRLmwOuniuE5ugp8hsjOMBr1Qpx-ukBVaOy8YC-B5vxRJZ-tQjQfJUWE59LCUgXVZCyZJtip5gegdq-xXmgN_mEPt2LKjyscFQf9Zm6yV1cDHws5fD_jlqZQ9CnK3qKT_jc5b1-fymLTM7mgrWmgPmTRmp-N-WvuFvtORGLZ2EhHeEz4ps4ELEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PVndqOc5tM-lc1bpiJVz2fkk3_j6d72rJAeqNJWZwrPGf0JR6aw6MAdxqhAhoEgLbWJ71tb2WLSeSXCyv5znKaaRnf3EoPtKulsTFjE-rES-BwrRErsJmSmPYY9q3kBgLjBMTYtdc0w4OmJVbtxJb8VihOYRwNT6vIu3BviIx0s6M_l24iAuYVRxgDswHO2UhadCJQtOsH_gvndxcmaRsydYePvZgkzqWAhmtkV8buUZh0IzmOK1Mp-hhfWom0HcbvxgKZfoyjjJU_MF03p4GLpuKL348B4nG8HP0gpuUFQY344dNGM0fM8zA-9DdM4IT2qpeFOOW3RInnnPzCX0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGJG8gxBc8UhysTcR_LEgrXKpz9qDc3g5q66ADYBHn1VfBoV-jXE5AaJbOHTY8bCNkUQj6FgdvZTjRAZiOI73k0i_rjA2iREuhzFzvGzhJ3Z8_88rWvySzGDt_bJ4YJWnJf7uRhdpkW9RvMtCgZulrtst4imTR3A2powATfkN7MgeMztg-6mBjiN16vujjUmHzVZdjN8f7j0hlqLPiuEMMv-QlSJXzzLLcaBJhulYliaD8LKDhJcIxifrJ51pgygGK2Up_9Egy9Lvdo2gfgjMCvdwLQWAvYpDCmWI3QXms8gl5qyItm1EBhZOdQS4KfDrU8iZRxoQts_PyXZ0C4iEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW7_qQzPAOvHv6eiVHq6vhkD8R77o12bHAQbNxY1uSL_UUsBZk6cZnnT9lEr0OBWA2E1KQQxzo7Om8xOsuIK8ID2hiG_Iz2alqM4xkURMfNoEfKd6q9hjhmjzapjN8LuTTc9TePwagW4sdK4dX_KgCaGOL1FKfrWW52TyOxoDmjC1cfJkqzHC3hukCrAsC4fSoEIOAU7TWacAguJOr2eN7CXEcTPz2KbBi966oOc6vvVS9e-07Nj-NuzO4whSR57iWPs6-48VN03VKcY_7Gmm3xYH0Ys6VRFhJ7jClJbYBuQOsl_D4d-L3S9xUlz5O2W2i6OU1OwG_cGBMIuA3RBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=Yc31eviIVhlxLTqxJyRiYyAUMjWy8l9vjgHviaPXX_NKYevmBdpM8QY-SxbwW-ln6q7_195SBCh-dkKolddXegl1NnavRzDmbQ4W1DgSf_GV1qi8UVemT3cGYs29ulUSkUc1CTzh9mTy_ougGVCpyTEBDZBaPlvWqWRQXZXnFODIDyXqeQpf2bH9Z0GOf7MT1tjGTjO7w4R-jBG2wUlwxUPwR-7BHrrCd53GxzBSVMVllyoeG2NIzEf1KUlO_rAJhQje22YXQrnqjTGGgv7sfd6JF0Y8cv4tXB8hbKca-bpVCCE-k5jygLjY3urfzltbf8uzL3clE7b_kabjtrlF2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
و
#رسمیییییی
: تریلر جهانباز FC 27 منتشششششر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxYPZRyLEnyjoegFslWzIXUmbgdmZhyjS0NU54cj-Q3oTVtFW440Ovl9gSQeqCdJvEvc4RmMXKbPTPrqhOJnb-VunjPrEbxKXsjuVsRz_qsIoqYAUoCJZo69aYDE-6d6Em0xYXFKmEpp0jAv5sCaTJu-rh_5qHv72rNzQkRBGo_XXaku7jjEDShBB44ShT8gWGt-t2XjVZ64NDZ_8U8i5UlLSL921f3GiyY2On6YDVv-veRJ9_bSkyOjGbRZ2SCkTwDF5H121p5CGaKNvcn0vAwxApR1h9o_sLHXg375D2RNqWzLDZshWnB8uPquI-4t3Iby_4DJ_eGVXiVrH1KKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udC2iEzlXsGo3MclYwAjaoD7CauBrAN8ik3qBprejzLcYtSalXlaCBOVgiUWvivlH6gbTccEb0cOH0CU7YaCAxq2xtQD3ZjeMYFPVNXoJ_W-_bUnYxk_Pq3fki0l3z6uBfNSdIy-BJhmjFAOq1p3iSDIuPaF4pTsWegcyjxuKa6LNe2et1MAoVSUrEMmAsT1VLNGEcLJsJ0JdMw_5knRQtt4m8ZTRXbrT6KpeFBwVsMokYYrUXipds2-MzXT_QRi7gh7OQ6qC8ji9gaYBkHxJxYeGHszl3ogSEx-s3g26iwH7DyzR4m-id95k4qeVnjkcIBoKCA9YhDBc89pkrr2Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8lxRnwBA5QHIglGFVopTlnKNKI1jZOsaLYYDD9OPK_a7qXGuaEH6i26K-b6LKHtgRackHu3yWqfg9iSoR1tQc8mkuuZQGIBSQXrk6yIHCQW48uE4kyR0hzCxzCbarAdb8RcuUjLANYO5Zut0EHZvAh8KnvhgCW2pQA0mz3hbOB89PFDve3u92_iAXwnd7t0IsayFAm8EwHRKfiliCrvcgU9E3NvgmPwg3o1eOmrJoC9S_1t-OsUPhf2gbTKwK4r3k52yUST7TylzYR2OWK4zQs6YSwZ2OgTk_gtc7x2WOmiAN9_ftPNQdDCx6ZTkMneFhzTcIX4SuVZWt1YR894vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=cSVI2q85NQPYa_IdIk7ldRRrT4UE4oj0P-EG6Y6kP5Z2muclC8QhIRlWoNA2F4kB0mOBt2tFbCtU5vpBKFeiocp-TlfJS_DXGIHBQG-7YgLp7PMisiS-tyuglu17JkxJyYrgYE8TAvkfIl5t6CtSy5j3PwAgYUtlNgIw2hcdGQp1v8V388cDPZoxnC97yjGwHknPIT1le1wYAH25InJ0yOayBvNbmD68GVW50nezzDYTg4-Cg1OhnbwvOzeGs7-siChMlI643wSFFIEM5xnYGSn6ijY9E7VeM5ya3TaKgGGrhA1l0mk4oJ0n9rJ1l494v1hd5_TawW_KoNbOC_I8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=cSVI2q85NQPYa_IdIk7ldRRrT4UE4oj0P-EG6Y6kP5Z2muclC8QhIRlWoNA2F4kB0mOBt2tFbCtU5vpBKFeiocp-TlfJS_DXGIHBQG-7YgLp7PMisiS-tyuglu17JkxJyYrgYE8TAvkfIl5t6CtSy5j3PwAgYUtlNgIw2hcdGQp1v8V388cDPZoxnC97yjGwHknPIT1le1wYAH25InJ0yOayBvNbmD68GVW50nezzDYTg4-Cg1OhnbwvOzeGs7-siChMlI643wSFFIEM5xnYGSn6ijY9E7VeM5ya3TaKgGGrhA1l0mk4oJ0n9rJ1l494v1hd5_TawW_KoNbOC_I8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=KBiEVuE4LY2hAYkf468MEVZK_l4RclIPkvMQ0I4LJfeSCPIz4LNhH0bD3eY1DArY6yrxnJ4lYIbJvB1DecmiQKmXH9oPYNIwRCG7zchJM0dDnMwHgvsVON_o6oLO4HeiXPTzHRfAK8pGfydLx3YcKABu1A3i342HYIaMnMJSpM3ziPjNcfbhJtucmDZlNDE--9ITVPupj7BbXU0n2OA7f2VBtdAI0lk4fXV5VRUwTiyl6Tb-cWYPfMOI901wA1sXzwjIcadtwmzQLzeeTRJmjCTmfuHHcHEsrKNr6Bdrd7M4UsDv_aXkj2EOwW1hWFr_hDEnEIG9jDMYpAsJb6gXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=KBiEVuE4LY2hAYkf468MEVZK_l4RclIPkvMQ0I4LJfeSCPIz4LNhH0bD3eY1DArY6yrxnJ4lYIbJvB1DecmiQKmXH9oPYNIwRCG7zchJM0dDnMwHgvsVON_o6oLO4HeiXPTzHRfAK8pGfydLx3YcKABu1A3i342HYIaMnMJSpM3ziPjNcfbhJtucmDZlNDE--9ITVPupj7BbXU0n2OA7f2VBtdAI0lk4fXV5VRUwTiyl6Tb-cWYPfMOI901wA1sXzwjIcadtwmzQLzeeTRJmjCTmfuHHcHEsrKNr6Bdrd7M4UsDv_aXkj2EOwW1hWFr_hDEnEIG9jDMYpAsJb6gXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaBKm6yHi-qwQ7tMt04JUzoxEMlFZunwW7tRw7mQWbd3IanmNjeZJWuib4JlXKrBYrs21aQTv1IJw9vPwAOmLgrGTH6-g5WQWKaci4JB-m_zwPQsyXBPYj_wWOS_e_MIUD-2-Rv-jNTFnaMSmIhgFHLJQTJ9EhxwXgDeCzW7scAvjeNtUG08G9IAUr5RcscSlu3j22R-mRJO6Hq1y35Jo7ZpGdZBbSKrUsaJI-33vLN1bb6VTK6kmj0aO3dMhDA-0zQ8adOQvr74f6yJRYOzl-JJL-fNa_uPcfc60oSRaNcG-5AE2Tcnzo8Ma5U_4G9LpT0FrmGCf0qM513lDyHG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHBZx22Vo3z-rseXlI6OKPTXb3-Ty_exDeYyh3rt4-2Iu9QH7_TmaN5ZiJKvfD2fAc_m64G5I2hQfdEs3nor_KIsO0Rn0e3Fq8dT1iHtdvB1bTwfgsNHBzz-3P36qP46Rg_JjlaY5CFunK2MGrAR9hNisHQr0EzIZzbInXu_QTzAjxxWVAYy0dHU3JtY3Cws_oLSta1rn0CoXzo0UvBebeW3wvqjoh9vNCBNRB7zdwIRFr_a0MmZivf3raCqMbhqyDopx3W93r3dku5irQ0mCd1Mz8KQ-YlH6b_Sz5BIFm9I4r9o5Qv2wi6omTSWoxAjg81BKGJMsvTVbChotUtJbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKjdVgMGX_HZCAomRP_oz0TpnzVwuOuRId3ubmB5bfa8-BOdXEjxA74SobrzrYPJlahIHmhy59Mp-757wN0Zk5EK7XghvO7kBXFK_aTJBPK07NWyYhwR7AYLXkl5u6iFermFfagIitq3fdG5o3vBQpvCgKEFQ-tiEj2sqUSioy-4XE9odL6fVRBt00DZq4NSISZgD0mRK_gW7FTuVm4rRt7GDTb7tTV5_8Z6MVhGxrfRi_--SNuVXxWb7L6mLbfaW2uhc6sjn3jCfnw9KJP6GTxf1eTZE79MNKKsuA9CYGiRkIbSMlFqF58o_TbjGSjZUzenI9VUmYV-yPfSWvC7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b46370582.mp4?token=uXER2SzFNAYGUkTeVpMnwC8d4H7XfuMJv9MoeexQ733dFUCeJsGs02YZLSQqPWfWLjTxQBGcFEL3E74USWTNo9a1JkqTbCQ4lZISysqPRTWp6eZ1jZNWPC2ePWTMPBgGS_nRIyzH87pnmZYt37IFbqnkGS0EyuhXCuJCXj43aAOz_PZB2EJ47VuF4KNAofEp56aZDnVAoP9VcGGEKvIQ2Z2XELkYRdlfuey9AbtJQHiID73lsKWorY2alOypqW6DDK8VjLzQY8azSekeNHhqKf5d-uoPMG44jS6Kdl-LA5Me4NVgT1mx0MvaQL3Ln_anfjTOQxhOOVDtnpLwkp88z0uJNXzGeM9QWBWSim9cV2_jBlQrd8OfJGdbUVyFayozWW6gRSd65wus0N6XDzjE0T5OK-zAbkh0es-_fAyY0IyKzJ9TLpF-Bux5iP2Rb7b_DxkszvRsUqZfTTBJ2Q2ZT2gHpwiJQsqYPcXK6SKzF62P__3F_zb5Pqah0V0K2L2aMXsyyrHe2G_l85QeZPAW2CK1smFZi4T9zzBkEIt7zaM_fb8jk_73AmhwUs0AoJ0e3uS3l-fbFCSZtcbaKqg8OGg6o87BfBNteUaBYgu6kThs3Kr-zF-Kl3Q2eFC6T41OTiYA_GWVlhinq62TfhjCHKjzehmZwP8_oWc1R_nbfo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b46370582.mp4?token=uXER2SzFNAYGUkTeVpMnwC8d4H7XfuMJv9MoeexQ733dFUCeJsGs02YZLSQqPWfWLjTxQBGcFEL3E74USWTNo9a1JkqTbCQ4lZISysqPRTWp6eZ1jZNWPC2ePWTMPBgGS_nRIyzH87pnmZYt37IFbqnkGS0EyuhXCuJCXj43aAOz_PZB2EJ47VuF4KNAofEp56aZDnVAoP9VcGGEKvIQ2Z2XELkYRdlfuey9AbtJQHiID73lsKWorY2alOypqW6DDK8VjLzQY8azSekeNHhqKf5d-uoPMG44jS6Kdl-LA5Me4NVgT1mx0MvaQL3Ln_anfjTOQxhOOVDtnpLwkp88z0uJNXzGeM9QWBWSim9cV2_jBlQrd8OfJGdbUVyFayozWW6gRSd65wus0N6XDzjE0T5OK-zAbkh0es-_fAyY0IyKzJ9TLpF-Bux5iP2Rb7b_DxkszvRsUqZfTTBJ2Q2ZT2gHpwiJQsqYPcXK6SKzF62P__3F_zb5Pqah0V0K2L2aMXsyyrHe2G_l85QeZPAW2CK1smFZi4T9zzBkEIt7zaM_fb8jk_73AmhwUs0AoJ0e3uS3l-fbFCSZtcbaKqg8OGg6o87BfBNteUaBYgu6kThs3Kr-zF-Kl3Q2eFC6T41OTiYA_GWVlhinq62TfhjCHKjzehmZwP8_oWc1R_nbfo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این خانم باتجربه نکات خوبی رو در مورد دفاع شخصی به خانم ها میگه، حتما ببینید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubrriheduvuqr28jDqCBhKOvSXKPQlSyJETbiRA1qqCWBiCXXkHSEJhBc8pPi_ZHoJKDMq-uZHQmhFt7pcaAzFOIm8mSbUSpLssCqDin0PpMqlotpYLk9WADfiW3tv-eXr5u9UkqmL7vn-Saf7IdL5VlyzhPsQykYy4A10Oys30P8E23a4KVO-Uyc6Y4MAskPlsCMCUkDpkfGJ-EQMuBiNN9lwxYqKzitKedXzKa9S7FuTQ86QaVjVu-kTZ83yS7uUuzkTuVVTNDYVgOZe6LMiPJkQ3Krv4tGqN_dDp3n14r0evpnM5Uj5koGiYogrWAb9vYtOSDaDc4rEzkLNXSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRHQXUerFzmptBumTxmS0tKKly6zB3pUhAUGgq3hiyMNPddIjfnpT1sRkQZsUEvjVMHoDZkyD1ZQcHiD996PKkCCEewq-IQeBdiZG9tCB97fC0NHnQRltP_hpXnZcuR70X4pSfvV6qu1c7uX-F0WziLFxUPcXR05Gsneyk2Km4fXxpYNmUb6hul9ADLXefozOQdOkRLuqvmoobmoof79Cam90ZkrYYOuD-8HzUc4HXX3ioG3imEzxLjhbvT82F5rBhd-hrByKutyfJQii1h8Jvg89jnWgp18taZy0d6vP8DqXvZdkbupjOmhz8HoeeImd7CU_hbO9HfN4TU2ecXqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
هروه‌رنار سرمربی تیم‌ملی ساحل‌عاج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102693" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=goBBM5eLIKiybcsYKa8RA5UgzeQ9IA9EeKyydSgJGqsGgXtkPLIVwZJxlIgGHqudtIkXH8pR6NN9Whyqywo8va9j37NciJvbYVpi-UdfdeK1Lujs0n43SPUvd0bJy2W37Y2iTx6VKgMD0IE2b9UqAkgtZXfb24ggJ2TWZstDdHqxNzpOF3pU9_lspM3tvn5ZRFP7xV_4hs5ysuSYA0LKxcwn1ibk_-v8gGBlNpQDXsryizPc1giIqyAtDTX_X2vJa0xF4ZTSZoYHvf2i8MQN6RzgqSlAKTgsuN1IGJ3IurXLmliSJiUk9U6kYG3XOnl_XgBUyvJs4OaTeGQBi-ts9q8Ve8WqEComhUvzSLC8yGHOIr553FU4uySskTU0jrn0hguq1ry2-4RxL4ahaGTRXSqFKZLEyUP-pqRilwlzMDJwahz0N90tLp7p6DV_LYJdmw0TP691b7mLIxhH2OFn-Zd5Lmx0j1NsFrKfZ7jqe2FpjKPvMvze62shjcypC5FH-0TXs8W91uSYCjnRYNs3LGwRDp6KUEPAVIn7IDbsjEduDUCgTpKXgFlpht6IA3107uBEYbBKKFUo9nB3EApYF0bzEXuFE5nkzboPeQWHHG9jAY81KKz56BBqw5khTmx1WkL4IArJ6O_keiDUya23-hCMGIjRjC49N8agr53B3GU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f0d298b0.mp4?token=goBBM5eLIKiybcsYKa8RA5UgzeQ9IA9EeKyydSgJGqsGgXtkPLIVwZJxlIgGHqudtIkXH8pR6NN9Whyqywo8va9j37NciJvbYVpi-UdfdeK1Lujs0n43SPUvd0bJy2W37Y2iTx6VKgMD0IE2b9UqAkgtZXfb24ggJ2TWZstDdHqxNzpOF3pU9_lspM3tvn5ZRFP7xV_4hs5ysuSYA0LKxcwn1ibk_-v8gGBlNpQDXsryizPc1giIqyAtDTX_X2vJa0xF4ZTSZoYHvf2i8MQN6RzgqSlAKTgsuN1IGJ3IurXLmliSJiUk9U6kYG3XOnl_XgBUyvJs4OaTeGQBi-ts9q8Ve8WqEComhUvzSLC8yGHOIr553FU4uySskTU0jrn0hguq1ry2-4RxL4ahaGTRXSqFKZLEyUP-pqRilwlzMDJwahz0N90tLp7p6DV_LYJdmw0TP691b7mLIxhH2OFn-Zd5Lmx0j1NsFrKfZ7jqe2FpjKPvMvze62shjcypC5FH-0TXs8W91uSYCjnRYNs3LGwRDp6KUEPAVIn7IDbsjEduDUCgTpKXgFlpht6IA3107uBEYbBKKFUo9nB3EApYF0bzEXuFE5nkzboPeQWHHG9jAY81KKz56BBqw5khTmx1WkL4IArJ6O_keiDUya23-hCMGIjRjC49N8agr53B3GU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
شش سال پیش در همچین روزی ایکر کاسیاس از فوتبال حرفه‌ای خداحافظی کرد.
"عده ای برای پر کردن زمین می‌آیند٬ عده ای برای تاریخ"
⚪️
🔺
ایکر کاسیاس از دسته ی دومی هاست٬ خیابان ها هرگز ایکر مقدس٬ یکی از بهترین گلر های تمام دوران رو فراموش نخواهند کرد :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102692" target="_blank">📅 18:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=tv-VBAaiH9MOk6Ig0rMP665yKM-cQ-QjTCQGpL8jH_XG7_gefgH47TEaMIw5TRfXIYGqAXl7MFR3wZWrL8p1c6suzrDBoe1VTd9rOB2I1uvw0xAs8qp_UIpTej-RfQPcpbIrDOWROTNrKs_JN5dxVbmEx_J3aC03v0b4ymSOu6hVatZV3IGzHsK1XxnIkG78cYy5hHzwFbPDZyFur5hSiieqU9iYr0SQqht5CJdfahuLPAUH2wmYqwoDqCHjlD9TsnIYUBahDsM-wnSOr_2NwpM2hIH6NI2mhACfbC9ARxM8H4pjyfw4qJqPus78UmO81J1F6-7LhLPomaswqFrLSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e14ddfd.mp4?token=tv-VBAaiH9MOk6Ig0rMP665yKM-cQ-QjTCQGpL8jH_XG7_gefgH47TEaMIw5TRfXIYGqAXl7MFR3wZWrL8p1c6suzrDBoe1VTd9rOB2I1uvw0xAs8qp_UIpTej-RfQPcpbIrDOWROTNrKs_JN5dxVbmEx_J3aC03v0b4ymSOu6hVatZV3IGzHsK1XxnIkG78cYy5hHzwFbPDZyFur5hSiieqU9iYr0SQqht5CJdfahuLPAUH2wmYqwoDqCHjlD9TsnIYUBahDsM-wnSOr_2NwpM2hIH6NI2mhACfbC9ARxM8H4pjyfw4qJqPus78UmO81J1F6-7LhLPomaswqFrLSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
#نوستالژی
؛ دیدار فرزند رونالدو با مسی فوق ستاره فوتبال جهان در حاشیه مراسم توپ‌طلا سال ۲۰۱۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102691" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APvB62g_SOV4T1sZc4X0kEkUYeKm6_mGRzCr8ArJlG34Sp6JofxTIhzASRep8k0uqPSdRJ8TPSxHX_WnsLErcmzbGfqBMHsXM1liAAHKc2vx3e-QUw3bWVoxtCIjDKuv7VjWI8W2JBXhAHoD4v69BLFBILrzAWrHk8OJ6UpvD-TNtF3BaCWbvEFYcP3CbPDkOSefmdB57f3bvBEyNG7IU6_T5W5WDoigB4Ec1venXCr82DIC_N-yqIKwlZukwYA5ivwF1Ou3wKBPl1P_0CZqStZaM8V6jarxoOnSExsNcHDtQuxGpVaEhlY6Zdrn0i3UVgwUbHaFlOVeLC9nXCnyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
بازیکن سال 2003 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2004 آفریقا: ساموئل اتوئو
🟢
بازیکن سال 2005 آفریقا: ساموئلاتوئو
🟠
بازیکن سال 2006 آفریقا: دیدیه دروگبا
🟠
بازیکن سال 2009 آفریقا: دیدیه دروگبا
🟢
بازیکن سال 2010 آفریقا: ساموئل اتوئو
🟢
بهترین گلزن ساحل عاج: دیدیه دروگبا.
🟠
بهترین گلزن کامرون: ساموئل اتوئو.
✨
بزرگترین مهاجمان تاریخ آفریقا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102690" target="_blank">📅 17:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
⭕️
🇺🇸
روبیو وزیر خارجه آمریکا: مذاکرات بسیار خوبی برای بازگشایی تنگه هرمز در جریان است و احتمالا امشب یا فردا یک بیانیه مشترک صادر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102689" target="_blank">📅 17:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvfCrgzpcvsLSv2cXn6HnTPN_FnJAqZqu33Ja2S7DP4VvqpSymW3CL4wmJIr53qBxU40n5m0A-ox58Pdb28p879vOeq1rO3lMXdC87Zrr1YalJgbk3akthYLmKPeQYCPJHIiVUO8Re6NA6NN0dMT14rDc0pME15KHZKgEFkLz71ddd1QCANkJN7PVeVY7BjNgOUySZ6BhMbc2TZNUbGj5pcw177z4mp6Sh19f2DxM8V-aJKSRpUJRBqYV5bp5HZLOC10kkz7k3vcRUtLTBsaO72sqldhWGOhExB-sLr7wQW1XaZK62efveDEBlDRGwvC2M5aQfNbbv6BkSg1Ap-fKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
چلسی صدر جدول تیم های با بیشترین خریدهای بالای 100 میلیون یورو در تاریخ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102688" target="_blank">📅 17:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDdAj1t4vPQakrhA8rRtN5CSHvYNO4XyrstrhTbsO-lw51rF5-rIG6rIqXUb2X37hIS04_g02fTYMPLZlPdXdsZopD-Klwkp5SozKKIdq0GM0zH00e7fbXLh0lKYrq-G3AaUJ7NlX8cL3yz1h3h5Py_yXs-PPn_OpK9px9jnr4qjim2zeSiBJftpYEQyNu8fy73gwyKaAoqdNbGogx1-iDgi1Uo9gYaHUUQt17paLZe1rOFpjR3j260S4bb-kTnXSItxJkPEM1Hx2IL2rv6hqnRDR0ccOkkrPK2mdc4UYMYZcUQ9fNCxC9Sr53X8tkSd6w0b5lsS22K8SMHPYUkmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vN1sN0nTKaADWapJ8GCLvolJ9qSL7P0htarMPika9V_W7R8S4e8gd9f3fHVP4idCZipSzUxUooR_A-UR2ays9Z3H-4DPn11JdQrBYTN_moZSPuP55Ns6HxX1vclVF1v8CbVyBnGKC0X1KbiZ9v-OkeVRLCAEGMGJ3dPHM8aL1_ZAE2CmLTwiJiltDMeKfIBPeFyDukBw-AJim9NwbqNOHSg8oxMn0hHfb0igT0rmo2W8R-EbJcytR8pcXJ8Hf12ZfkAqThjrtaL63HLUiVLcJjWl9foGRJvkALy8EKZ6RJ-CPcn1XMLirMS8Q8Ny76fXlN772wVi3xndmuhv-3nwCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
تغییرات رودریگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102686" target="_blank">📅 17:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA2VENqspe-PIBnRPsscu81XYMgH-KAejxMs_A8w7YV_pYgsKlrUFDlaWr_inm8q93AIeR7UK_LRA797aHP9ySoKMLqC6-Zr0YmAH9P4KX7E3hmsmtALHwZi0DS1R473Vw1jwrNu5dSrCmwiVHu_JsRyOeDKmlaPSQsKLlwDxTAC-u6Jtrfbf7G0jA7U3oASGf-ewRTOES1L3HBF31xqP0ZwMj3nrHIcOdWQ8oojNHFvWUPFKpu0a2T2GJYNBMlEWHUyPMfm0rSjhv7mdNrhzMYWmya9S_V6X-AB0DEtiwwlp_gafBV1TC5tsU9_HJDYV9KNCwqMWz_6LFNQs-zGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
14 سال پیش همچین روزی؛ باشگاه یوونتوس پل پوگبا رو به صورت رایگان به خدمت گرفت.
🟣
پیرلو: روز اولی که پل پوگبا با ما تمرین کرد، همه خندیدیم چطور منچستریونایتد می‌تونست اجازه بده بازیکنی مثل پوگبا رایگان به تیم ما ملحق بشه؟
🟣
بوفون با خنده به سمتم اومد گفت: واقعاً پوگبا الان مجانی به اینجا اومده و منچستر اجازه داده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102685" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78b336809.mp4?token=jfMkwJNRZHljjmiJa0rbnTmGVi_yQ4Ya1pjXEtYsX6izGrWcddAZXojj_MWPMh7owRAMOEcjQ4cBaSK_UFNfTTQJ_FQaT8T0vT6cXKMxeV0PBdJ3sxXz9Squ4Z1aMRAjF2anOWqelWU1CIdoKzi62bsBhZEpGObT1OV-DSMlum2FfGRy-7949ltyYiYZPjcJI3EsmkFrSXSy0pg3AhZfxgQzF9qHsjhhSVlaz2G2x1jyfTqg7oXE_a4vlUJnOeW7WR4wut9dX4fSBY60zjW7fvqoGZvQW_e5CCz2Mn4Pq_YTG-cIFCV0ofqoD42h3ZZ2Pg4dkKQZhG9_kGLY0xVDJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78b336809.mp4?token=jfMkwJNRZHljjmiJa0rbnTmGVi_yQ4Ya1pjXEtYsX6izGrWcddAZXojj_MWPMh7owRAMOEcjQ4cBaSK_UFNfTTQJ_FQaT8T0vT6cXKMxeV0PBdJ3sxXz9Squ4Z1aMRAjF2anOWqelWU1CIdoKzi62bsBhZEpGObT1OV-DSMlum2FfGRy-7949ltyYiYZPjcJI3EsmkFrSXSy0pg3AhZfxgQzF9qHsjhhSVlaz2G2x1jyfTqg7oXE_a4vlUJnOeW7WR4wut9dX4fSBY60zjW7fvqoGZvQW_e5CCz2Mn4Pq_YTG-cIFCV0ofqoD42h3ZZ2Pg4dkKQZhG9_kGLY0xVDJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
امشب، سالروز تولد پهلوان مسعود ذات‌پرور است؛ مردی که از باورهایش عقب‌نشینی نکرد، شرافتش را با هیچ چیز معامله نکرد و در کنار مردمش ایستاد.
🔹
نام او برای بسیاری، یادآور ایستادگی، غیرت و وفاداری به اصولی است که به آن‌ها ایمان داشت.
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102684" target="_blank">📅 17:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP7j4QvlL5Guhp2wfQABkSyrAGkLpyanF4fXneDK65lPzQgEXcy45YfOe7EkWkjARWzIFtnWQgvazCL3dKEBaVcK-r7-VRZ9vFK1kgtw5_AKIz1FvqG6OfAwqNOfCUi4dd2knmEudoUFpGC9QjEykxmtg51-OoFXgNzWUWITWaXHB2_ih2EeWVmSZW6aXQGZ9CpcdSE5CJ2wWq0OU6wEWJN5Sc3ZK-bda-wSjJJ7YF5YDMJQuJZvkaTnMLwgenG8XVaJyBCtOrigmIm22PphpPnIXEThb6sB9RXCqPcOk02WFlDt7cU0vjIufK2x1rIUd_SpVd8CR-p_u9sublxaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پست جدید بیژن مرتضوی درباره مصاحبه همسرش با مجید واشقانی و شایعات بازگشت به ایران: تا وقتی جمهوری اسلامی حاکمه به حرمت خون‌های ریخته شده در ۱۸ و ۱۹ دی‌ماه به ایران نمیام
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102683" target="_blank">📅 16:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=HX7SyTQDh1c7XEAcRs_li79QiRMmUDygP9rBVmi6qPAMTZ1UVVPIRUqE55E6ozjjWpv-DzioDzMUaCCQ_N78Lxf75_TCn_JPGvkbhxPs2sb71UJUH8ypx2ccp0iM7fgK4j3lSbJ3oWighvpq2auAEh_je020oblx4zlNrhChrfUunxIJe7TiKzWaqwlxVnJCEbQhXW7z3e8BVYhZLn1_XCDnRHSQzsR8ricZggaw2mhc3z2iJLjczfx2dfHpD00hVmWg_8_7neCjr0d2pl7Llsg_4T7_XmNl2MViSndz2OLfwRQulK_w45aEAC9InvA4DlHmzzGak6963i-9t1_Oeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3348f33cc.mp4?token=HX7SyTQDh1c7XEAcRs_li79QiRMmUDygP9rBVmi6qPAMTZ1UVVPIRUqE55E6ozjjWpv-DzioDzMUaCCQ_N78Lxf75_TCn_JPGvkbhxPs2sb71UJUH8ypx2ccp0iM7fgK4j3lSbJ3oWighvpq2auAEh_je020oblx4zlNrhChrfUunxIJe7TiKzWaqwlxVnJCEbQhXW7z3e8BVYhZLn1_XCDnRHSQzsR8ricZggaw2mhc3z2iJLjczfx2dfHpD00hVmWg_8_7neCjr0d2pl7Llsg_4T7_XmNl2MViSndz2OLfwRQulK_w45aEAC9InvA4DlHmzzGak6963i-9t1_Oeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#نوستالژی
؛ هتریک رویایی علی کریمی جلو کره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102682" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102681">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=jV1lzf8_LFJ9F8KLSRp5WJatEa25OGJikOFoT4SwyWgzro1foZcLCmQsvM2l1MkxS4q6Mt-pa42YbQfUQ8ULg7lAEaNkETQCy4FP3KELkhSr1JDP4bEqWlN2RCzFHQvwZHBmC116_g9-TSfLDM_9iKgyWJMyK2p5Wc0DhbLNBjPYg5fZIs1EvUDc0W2uHNNDxn7qdgcStqz-dVcOumoSzeVh1ko59wPKCOjze_Juzd1DdCqprQBdQeyKAOevw0yxvqm7uJYFrB0K3pdo8f1wM0blYctAwzndHFxsCOtmYI1KPsS5T0hSWT4IGtacpmJ-06tNMa9vKzbXb7gE_s-9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018847c7b0.mp4?token=jV1lzf8_LFJ9F8KLSRp5WJatEa25OGJikOFoT4SwyWgzro1foZcLCmQsvM2l1MkxS4q6Mt-pa42YbQfUQ8ULg7lAEaNkETQCy4FP3KELkhSr1JDP4bEqWlN2RCzFHQvwZHBmC116_g9-TSfLDM_9iKgyWJMyK2p5Wc0DhbLNBjPYg5fZIs1EvUDc0W2uHNNDxn7qdgcStqz-dVcOumoSzeVh1ko59wPKCOjze_Juzd1DdCqprQBdQeyKAOevw0yxvqm7uJYFrB0K3pdo8f1wM0blYctAwzndHFxsCOtmYI1KPsS5T0hSWT4IGtacpmJ-06tNMa9vKzbXb7gE_s-9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
عشق‌وحال یامال و زیدی همچنان ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102681" target="_blank">📅 16:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102680">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODUPCqMY74RvvceZbX-SR0OzNED1AqOV_TirEeIYztXdMvGN2d0IzGW5BAKkGYB6HiNKiod7AW2NL700jVHcXnourjomPfOOh_FsLMSjhFYeqMS3XnbNXRC5OB0St-zu_EkquPdz3Ii0oo9nQzQQjzexcWOS6VmOQLRNCVJxrvCo3vH_t_e6JBc3Kr5VfOx73Z_cNwj1DkpwYKtZxhBHcHhP1XsBQhyO17NmxUe14KNYte9N1aNO3Raq_oIJBGPiEneh60tFOiUHBRMgF7L2k6iZFg44IqBJjyk0jVmHOeaj-1GBlo7lkLfBsFMR2YjrXViicS2OudXCptO31R7aeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
🇪🇸
آمار جاودانه کریس‌رونالدو با رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102680" target="_blank">📅 16:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102679">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=c6HNfmUKP6SV9tmtEcZwa_cGioXvRUqDshLlOQrw6a5MkUbXoLjcjYblWRtZqDAKh_tWIwOgRRHh4nPiU3W0N4PecXpPP1nwc2WIqb0FKZ_CXLleqURdBo4EV9FN0B20TsrRf3dtEg0XYFgov_SEbOfd50x2ONwYBcYj7Xw-tNErm8zuwKbADDhXmw0A2DOWawOPBLW_F52rpJkN7woWV94CySBduuklXnSGeY6FbClaefPL5OVYnti5W7GFnEEKpcQfJBmrLpaZNb57QF_i7VHClkw96BeFkWuaWVas-N8OgOYRgk0wrQLlMaseEWYpp36K8rktevoSXhz5_iZcqFyu-wYZa2cTzociECPbFnOCUxTXRn0JHCSXqFZxXfhncPEj4htrOe97Uy4N54Q_j-heuQDwZkw4IhfWYndGSdyd4NS78v3mI1Z9z44WZRnpTyTUv8CWJqnsQHBRR-HpkN0_B9cVNHu0ePd4Ux62rc9Y5y0JZIs1l53LjqyyDW2Z3gdRlw5bfXK_2D7Tw7PDYIjdi3IcCspaiDA3Myy1lMw5ByMi4-C7Pf3VH7gJSsD_n6K7DCwsog9GcQRV0DTPRuo987Hi1ODYaQn8lqKl7ZbU143U5QBJAZXnF7D77bMi8o719q8YtRTzFuoGv9_fsW5-1Bjs60VSfE1zaDxgMMY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5903f6c3b.mp4?token=c6HNfmUKP6SV9tmtEcZwa_cGioXvRUqDshLlOQrw6a5MkUbXoLjcjYblWRtZqDAKh_tWIwOgRRHh4nPiU3W0N4PecXpPP1nwc2WIqb0FKZ_CXLleqURdBo4EV9FN0B20TsrRf3dtEg0XYFgov_SEbOfd50x2ONwYBcYj7Xw-tNErm8zuwKbADDhXmw0A2DOWawOPBLW_F52rpJkN7woWV94CySBduuklXnSGeY6FbClaefPL5OVYnti5W7GFnEEKpcQfJBmrLpaZNb57QF_i7VHClkw96BeFkWuaWVas-N8OgOYRgk0wrQLlMaseEWYpp36K8rktevoSXhz5_iZcqFyu-wYZa2cTzociECPbFnOCUxTXRn0JHCSXqFZxXfhncPEj4htrOe97Uy4N54Q_j-heuQDwZkw4IhfWYndGSdyd4NS78v3mI1Z9z44WZRnpTyTUv8CWJqnsQHBRR-HpkN0_B9cVNHu0ePd4Ux62rc9Y5y0JZIs1l53LjqyyDW2Z3gdRlw5bfXK_2D7Tw7PDYIjdi3IcCspaiDA3Myy1lMw5ByMi4-C7Pf3VH7gJSsD_n6K7DCwsog9GcQRV0DTPRuo987Hi1ODYaQn8lqKl7ZbU143U5QBJAZXnF7D77bMi8o719q8YtRTzFuoGv9_fsW5-1Bjs60VSfE1zaDxgMMY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
هفت کارت قرمز عجیب دروازه‌بانان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102679" target="_blank">📅 15:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102678">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBOzjJnE4qGvFs75CR_S8N4vkLPsiqFMJxR3AKrfDZdPR-RoVhRK5i5XyHPO6-GVQe0TWzvItMuaoWdzyv9-uMIev7Nu-m-oQC3E76JkaOF7r0h3j5umteB2z6JFgLpinhj-__oHzgjEQxwmNu7uevxTE2Vbzh7m1MaQQd3jqeUWUkokLES698SZpC9cN2Q_8fm2Y5XzdKi_PxVrc0sI05fuEMIZfFhi0NxXTQy8aAlYBsor8aPu6MR61hTu5t5WwJt-d5tIgQMZq083EvMTGyP74tMLsM9087KK04TJDUDAojSCplGUCsdgH4FhQ_KM5sDcRvn_5YE-Czx-oxwgaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
💥
عملکرد ۴ مهاجم برتر دهه‌اخیر اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102678" target="_blank">📅 15:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102677">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2wNItc00fD56BwZXAtSBWkDgS4_FDv3t1lTVO8HlhnL3VZw3kDURumrI1BP96-pkkMX0uc-5__f6A2bvyRgS_dhlYAFx0YK5O_7Lombkalw5w20Ci_ZzXIONpbuFosAtw3dz8uXdkrdUj3ZLQG1SN1Ko9UZEiu55eHwxYX7xDzhFSn-XTFB4oUyEfpQCr6oHBClPbMS91Z9aQJJ9S2t_66hLtow831o5dTaW_usuQQmPfmdit6TCB9zJX_y_oH_LIPXkbQK0BVpAOYHFllcXHfzSa7IRL6WTUu7fkydkAkZAMBw2xA8SZfHh9kuvFplIu772I915-W7BNY2MQqG8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس: خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102677" target="_blank">📅 14:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102676">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=k9nbtwTIvu--2qv8CIp19F5-arVf1vAELQGxvr38lUdz3Pq4yQ9t_niz6wcr5vS0_-vQf4htD7tfhMRE48RH7_p-avqu3mu8hnlGqc8wvL90zMuvkI_abtbHpYEefWVcwiUGUqtNzgjiMUusDkWsVnr4u_dFK-bYopvKvpcILo5tc0ZBB28Cli4KRt3z8AlhyGQT407lHKm_FBj4nG_AwIgmI8pJoRS_aDq617fj9hP-d_sMHUOEHxUX_yIze96syp5BH9eF-GtkJhGSQIMC5HncF9j_dGd7bKIy8cd1KFnlPu58i-Wtrp_IcOy0GUFu152AYIDbzbL__trx2q2dIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b59000aa4.mp4?token=k9nbtwTIvu--2qv8CIp19F5-arVf1vAELQGxvr38lUdz3Pq4yQ9t_niz6wcr5vS0_-vQf4htD7tfhMRE48RH7_p-avqu3mu8hnlGqc8wvL90zMuvkI_abtbHpYEefWVcwiUGUqtNzgjiMUusDkWsVnr4u_dFK-bYopvKvpcILo5tc0ZBB28Cli4KRt3z8AlhyGQT407lHKm_FBj4nG_AwIgmI8pJoRS_aDq617fj9hP-d_sMHUOEHxUX_yIze96syp5BH9eF-GtkJhGSQIMC5HncF9j_dGd7bKIy8cd1KFnlPu58i-Wtrp_IcOy0GUFu152AYIDbzbL__trx2q2dIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
برخی از ریدمان‌های اساطیر‌فوتبال :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102676" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102675">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1-e2jlgBpqsg7jBZXUaOqcYnVbGE2nxaKUkyKpCkSRnOB4BlnbkuzYFY8CoR9LTu9W2SVm0re7XF-_mAuA3y6lqoVRW4p5qbnpGBaq5GNbHv-PmWxE3Z-aJLcNJ-CzykBDIIeSc-vKuTLRIZPod1TfD6PohBb0IQMHiSVQ7cwICnMwVwdhg9xh4OPhnE5n7fLOP4N9OjsIWaWE775zCF917uyJ78T2PHCWvj6JthDAgWmHYM4ZeDAJXNxcu6lkG8owHb3hnR73aME0lyw94iZjbvOBJSIN3QsfGDyngmbE4mvYBCUTjBb-x6EgCKMeoRMh33uJ4vCh1nKuYKZCPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اولین جلسه تمرینی ژابی آلونسو با تیم اصلی چلسی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102675" target="_blank">📅 14:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102674">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=DSsAqETy4koP3LbYTlJyAU-YYXn7afcgnn2WD5tmqmEyYP0cgHUQHp6g37vyhQGdkR2eLZSeHo0M07jj2WgG9GeimCq8z-cJDBeTcFouaW_XKyoBUCeqMAie8iTFC1reHDLofFIolOMTay-n5RoJM0SW7dvqaBbujm6jkAhJcU68lmcUUecV2qRt_0vYlpOGZHdyG4Q6I7E7nYTjGuNJx60lqjrLhqYWXsaGgkDi8VNK_-sBZ6dowQmFHdLiu7mHcF3UrA0GgjHOQ4tGXc9ocyFma4TuRJEf6r19NiiElfAiohGvr7kroVwM7OnlcuyrSzFb0uUReepwdOhWVDe8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb25fb54e6.mp4?token=DSsAqETy4koP3LbYTlJyAU-YYXn7afcgnn2WD5tmqmEyYP0cgHUQHp6g37vyhQGdkR2eLZSeHo0M07jj2WgG9GeimCq8z-cJDBeTcFouaW_XKyoBUCeqMAie8iTFC1reHDLofFIolOMTay-n5RoJM0SW7dvqaBbujm6jkAhJcU68lmcUUecV2qRt_0vYlpOGZHdyG4Q6I7E7nYTjGuNJx60lqjrLhqYWXsaGgkDi8VNK_-sBZ6dowQmFHdLiu7mHcF3UrA0GgjHOQ4tGXc9ocyFma4TuRJEf6r19NiiElfAiohGvr7kroVwM7OnlcuyrSzFb0uUReepwdOhWVDe8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
مثلث آلبا، سوارز و مسی که بارسلونا رویایی فصل ۲۰۱۸/۲۰۱۹ رو رهبری می‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102674" target="_blank">📅 14:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102673">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VusMZ1k0pWj7SO46cnaYGy4tyFmeujO2GczvwOJxBU1HRzmVw_1AF2Xvsiot26fZt2k1osGFxgMViKmz9udEryOfHEnUiulPJ66ToZfIgRfj7xxPQiaq9C4SygEZmA60O5c2lvygOTaBPrhBin95sxt5_jLT7otAslV4hTFTlDsv-41_k03SAJTukpP1yXQ_PhmWS7AQ_1EgpPnTsejy23xm5QSOuF5euoMNaX54a-7pD7522w04gkUR6-OXUaT2NoYDLi_5mYRJML1GnRcJx7PiYHbizHKw3kK8ouX6n0FRnSd7NW1T_N-pfAKKH5_NmH7XvCIBbBydA9ZrzBWxoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس سنگین ایکاردی به وندا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102673" target="_blank">📅 14:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102672">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
شهرک صنعتی شمس آباد انفجار رخ داد که عضو هیات مدیره شهرک اومد مصاحبه کرد و گفت یه مخزن ترکیده و چیز خاصی نیست نگران نباشید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102672" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102671">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJ1Y2-LCHP5YT9yqQZuRB51s8i5gHYcogUDU4iObGdrfwKbVfl8Zcm-SHd5jbEzumsGQ8EJ6L_L6RRhGr_scFHrVtnzJYzcu1LWLSyVWz9u4MUfA54jRUDJgpkNATd4zBLafNoyDYfS94yyrtqmerolm55YXbayJEOLV1q5cIFEHEFfYjzQUdt4qpLbWmYn6Jr85QTc7WhHsuI5dmY2adUxxKAYITp7-_-pm4BhabhL6hq1ImI3Zw2umfx8rEJusZInotaMFlfrGSyz970XbWx_0wGWkQX4ch9UVcZyrtCAKpbklAdI2p3dNxUokSLk4qXaOI37ysRDDRDZNoLnzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
تو سبزوار یه مرد بخاطر اینکه زنش پیراهن امضا شده پرسپولیس رو به اشتباه شسته و امضای بازیکنان پرسپولیس پاک شده، درخواست طلاق داده و به زنش گفته که کل مهریه‌ت رو یکجا میدم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102671" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102670">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=bhiHwBNoiTs0uqlgKMxElIK7F8YmO91aoIPc3iVxfMnfSaxk-F0MXyvTcfE4oy1s6vjkFR2YbgmHX8OIreNB_sp_1bWVV72LtT4ZvI1_f4ypOSKF34HaYymWROIfxaSx2Ieg-ktG8eieHHXZXGAiV4zkNLi4Vgb2KP2KO6-u5KsQW1TxT8UrJUkhese1TsfZnFj8hQlBoQffX1hRvd7uqNg3zye0aourIemt57nCrAlSQCoI_-a0izedkl1xCd4m5-nPVLZbb6mfo6Cy4sBZbxbMXoHiE3kU1SIq4OaEiOlSjPZDEnAOSDvL1tVyI9eiTVPh7gMoG5vDiyQdztAF1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627a83e0e2.mp4?token=bhiHwBNoiTs0uqlgKMxElIK7F8YmO91aoIPc3iVxfMnfSaxk-F0MXyvTcfE4oy1s6vjkFR2YbgmHX8OIreNB_sp_1bWVV72LtT4ZvI1_f4ypOSKF34HaYymWROIfxaSx2Ieg-ktG8eieHHXZXGAiV4zkNLi4Vgb2KP2KO6-u5KsQW1TxT8UrJUkhese1TsfZnFj8hQlBoQffX1hRvd7uqNg3zye0aourIemt57nCrAlSQCoI_-a0izedkl1xCd4m5-nPVLZbb6mfo6Cy4sBZbxbMXoHiE3kU1SIq4OaEiOlSjPZDEnAOSDvL1tVyI9eiTVPh7gMoG5vDiyQdztAF1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
روایت‌ایووبی بازیکن سابق آرسنال از تقابل با مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102670" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102669">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3cXsbMfLHZRsi6BieQeUSMCQDYuIRYomy2lRVfGu3BJQmE8C9RiIbF2szPaKxtnPB7RTV3jNh4jmo88kK0pd22231kyhEFJh-fpPatDLXvMIrUwX_xdzl_wUsG6tNpf_3_TFsbmMGHcwwVOeb22e2laVZ-eMpoSs-ItE-i2p-YsB2EsLMkV6JSWnj0Irf8N-q9p1uRDgs3LegKqGCRdPh54rYb3wtldh6xxruUSMlvt-2z8TAB3G4oPNCigt-I5_L8xvt-C2p8u-L6hR7RqJp-IQ2-J_6fLXhjr37e1GdLsk3rRTIVaCj5BmRWKaGV33-c2HrzGaadBIYKV7gUepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102669" target="_blank">📅 13:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102668">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=Y53OvjOPvsQ0TqjDgO4ZPPYlPGWC6gkiWpydRq--K6RhhC_Qk-Uq1VQUIoVeCRme1bls9ImUMWBRbAy52PoBQqaCVToX6c63RhFY29fn1wNhb0frs_PlfL_vR9LoytBNlBMYHQantgow_UBrwZ1RvzihMUX1q_QuoFZ55CkD4Pj3SfSG1keLqd32YwJyZHagYUgK9JWbCE5xmiY30AJ80qWMEXxJqVi3nLmoLGcddZrU1L-NEKRhArh4lZbl6C4FL1l2e27AFP4_NBPPW0ihFslinbszaaZB23YfWUcaEnvIsaAtN63kkB60tVNLAUd8MSQiSfWiNnRJ6kIeJ7X2MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e611ac196.mp4?token=Y53OvjOPvsQ0TqjDgO4ZPPYlPGWC6gkiWpydRq--K6RhhC_Qk-Uq1VQUIoVeCRme1bls9ImUMWBRbAy52PoBQqaCVToX6c63RhFY29fn1wNhb0frs_PlfL_vR9LoytBNlBMYHQantgow_UBrwZ1RvzihMUX1q_QuoFZ55CkD4Pj3SfSG1keLqd32YwJyZHagYUgK9JWbCE5xmiY30AJ80qWMEXxJqVi3nLmoLGcddZrU1L-NEKRhArh4lZbl6C4FL1l2e27AFP4_NBPPW0ihFslinbszaaZB23YfWUcaEnvIsaAtN63kkB60tVNLAUd8MSQiSfWiNnRJ6kIeJ7X2MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
اوکراین دیروز کسخل شده و با پهپاد یه ساحل تو روسیه رو هدف گرفته که چنتا مردم عادی کشته و خیلیا مجروح شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102668" target="_blank">📅 13:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=NNooRiTZZFInACdnqWrdxmB7vcBGWk3sDXWqST41D4YJvLMWLMJziB7GT6cgYdGNCzSVf3dbsXL6eswEFt0hxFj5cJXTAKQaOVp3RVvgDS6AaPN1pqXlaAUcQ5Gek3SMGobyfdgQLCyqsW-L2y30kPI9vzqFWXOBE2ezQicv4lP5L9RDkmxCYymIY34w01TaFrA4emdPvB0u8jhhMRMY9N5M4ZFgyV5CgNjCGLnXkZdjWffuXPqMaUf7AVdiIPxC59QtP_hYJC9ggo6mINWoSLh1Ja2XuOST_YmFjHUAOo8i6HPN7y2xR9X939ZVncmdZ7EJ3gfaNLhwa4qjNgCQfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=NNooRiTZZFInACdnqWrdxmB7vcBGWk3sDXWqST41D4YJvLMWLMJziB7GT6cgYdGNCzSVf3dbsXL6eswEFt0hxFj5cJXTAKQaOVp3RVvgDS6AaPN1pqXlaAUcQ5Gek3SMGobyfdgQLCyqsW-L2y30kPI9vzqFWXOBE2ezQicv4lP5L9RDkmxCYymIY34w01TaFrA4emdPvB0u8jhhMRMY9N5M4ZFgyV5CgNjCGLnXkZdjWffuXPqMaUf7AVdiIPxC59QtP_hYJC9ggo6mINWoSLh1Ja2XuOST_YmFjHUAOo8i6HPN7y2xR9X939ZVncmdZ7EJ3gfaNLhwa4qjNgCQfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
دلیل اینکه چرا کورتوا یک‌دهه جزو برترین دروازه‌بان فوتبال اروپا قرار داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=lW6kJO5nlIv9uqSaBhlFFxjrEtJQkElWGq5i5y7yFxFkWD61YYvqCZWiY_ha_HuQ2YknZavxXrJY289modCZcXjF6Fi_PlSkEZ3uWavBad1CpeWwIxPT8AgsxNWABg3jcPSkyS-YzemXm2fqaIYIzZevBYBJBE8CsTbYIYt4rRK9Y_hyJE3CH8ewdUQvNBj-vTvSJJMdpSeTAUtZoBojtJ-ypSeRNvBi3SmdD_gR_rbbdM0QwxxMceWUD4lpogGG91SK2V5pkHCy9iMBpSEmG9cwEx6i-Ma31fGwjZkHu1lbxKX7f_8zOPo3DOPS-hGXv_ZPvstNIJtewRysZW-leQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=lW6kJO5nlIv9uqSaBhlFFxjrEtJQkElWGq5i5y7yFxFkWD61YYvqCZWiY_ha_HuQ2YknZavxXrJY289modCZcXjF6Fi_PlSkEZ3uWavBad1CpeWwIxPT8AgsxNWABg3jcPSkyS-YzemXm2fqaIYIzZevBYBJBE8CsTbYIYt4rRK9Y_hyJE3CH8ewdUQvNBj-vTvSJJMdpSeTAUtZoBojtJ-ypSeRNvBi3SmdD_gR_rbbdM0QwxxMceWUD4lpogGG91SK2V5pkHCy9iMBpSEmG9cwEx6i-Ma31fGwjZkHu1lbxKX7f_8zOPo3DOPS-hGXv_ZPvstNIJtewRysZW-leQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇰🇷
هونگ میونگ-بو، سرمربی کره جنوبی در جام جهانی ۲۰۲۶ مجبور شد در برابر مجلس ملی کره حاضر شود!
‼️
او توسط نمایندگان مجلس درباره تک‌تک تصمیمات تاکتیکی‌اش بازخواست شد. از تعویض‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت.
هونگ در ابتدای جلسه از مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=mf7AfhSeIZnoNpRaVVwwpGG9Il4FnydFfcZXh3vmNj4PhpMz9juChDM_QI_AOPMR-y-2Ar8CpjxYS3K1P3OIzlCh_CvOfNGH4okB12qMZrPYJlxK_DsThSQCC5xnD8Oi-zcUzWvdOsjKTuxpvA2oJSCDWr1Cx-zgQ3fZXqzPrPxFH8_mu2iRmcF5G-dThNLlXVowOkesk6faS9jgWY7iXZE7HUrAo8UhhzyPVS5clvvDG-dNhXyK3R7SW6ao1bchc8goJ2Xj9qi-BNTqO29utS7_Re8LflKdm-wcX2J3lDfUl7Rb54_Vbr37cdIl3PBUSh7_8b_JVEg1kCeBooEpvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=mf7AfhSeIZnoNpRaVVwwpGG9Il4FnydFfcZXh3vmNj4PhpMz9juChDM_QI_AOPMR-y-2Ar8CpjxYS3K1P3OIzlCh_CvOfNGH4okB12qMZrPYJlxK_DsThSQCC5xnD8Oi-zcUzWvdOsjKTuxpvA2oJSCDWr1Cx-zgQ3fZXqzPrPxFH8_mu2iRmcF5G-dThNLlXVowOkesk6faS9jgWY7iXZE7HUrAo8UhhzyPVS5clvvDG-dNhXyK3R7SW6ao1bchc8goJ2Xj9qi-BNTqO29utS7_Re8LflKdm-wcX2J3lDfUl7Rb54_Vbr37cdIl3PBUSh7_8b_JVEg1kCeBooEpvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
گشت‌وگذار امباپه و اکسپوزیتو کف بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAE1KkyHyJvtUunS9LhYZfYWWmLP_mwyW6YbTTf2DQ8_CucsGk_fq3OzIC49J6hnQcHMart9QtZ4drwATMIQB0FdQqfaBiBOKiwjTDSr1kib-rGF8ACvvR4_NtEn8OYCfOOq-nAEyDF2iTwRAS5cZyoOkt-HW89T6-JJtrCC4DIU2cByEYoL3s761DlHdF7Ef8zCxQjoR72CThk4sBK3N3ClCdPHX76Lbx9zUeKAV56LpriNiPzf2s4YFT4p5IE3ExjPT2YU--ainGw6mvlHiiaVYQvKSdoiYjlisNWdnTO8gBmvpozxjHZStTaaqPe_0sZGkXZltC4jLWy1We08Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ4TlzBThyXLYabla1UwA8hXrTrgFfATdVrAJ0ICtR8p0S6f-MbFBdqEes7-r4-gYZ_jIxe3LANUdf0dqIdwZ6JMt4HjxRcfLS0-mKWmreeFqmonzgD0dob_PoKG7CQHg2aSchPdfkEIrUB7_-1Adb4Bv50xcYuohOd0wbRMxYp_0FhNgG54hFwEfieEgjrq_6843umN-HdB94wwvmqOUCwTqAXFGHOtgeJCME16-jxAJkn53OfT9tsur1yXS-wMhxjoOEFqZeWlUklROBtjfU8IODnVk9YEgGKy_jv9mJ_3DwzV_mAx4Zvzk3Qy-ea4BnjE3StZsWorMdYlE59RGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov9tWd0AWuvRTqLU6ZCERBy-n47FQLwVLd88dcPZGWDMxEwykzdl-jZZxI1xKDFxT6b3HbobVPM-0XngyzBoAeWWmYf1Z4UwBuNHoRrFnmdfQmhqHnudnLVujFxCoYYtLgntpEp5YHCXP-vYSim9Bbp8_PoNLK5387n1oJPyswK9PfTX9cR-KK34F1Y6a3DDR6qo-sUUS4sbfrIe8wuIL2c7rUd7sIZKWMYrttjpbErCT-afjvcaiRfJBPmkpLZCTcHtGUhEOb7i9MgQgr_PiPLkiGhZnSpp71N3gjP0CC2NmLQgpgTWp-mFRA1rNP2adJ9-bllYqsMlS0miUWy03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pUOW1AwHRP6Ec9Qps1Kv8SU3XSeNqJvIFxP9dfXuY-f4K0P1kblUYuipi4jdlOTA6g002ju_GWY7yFVkNsKszzJGKzGAlqyyCcJyYO_1btBEBkk1n8X_Opoojg38Koz_TuKW4c44Ze_ZHWJAyOQlHmd9x0JRs1-p5MO5Ps5XjLhJDfyAULwI6rBGfoWFBnAwInxdPnW6YBs5MnuQ8WpcgkuiX58PCGOSVJO-CAW5EFYv7_K3OxOl-sFKb4wO-APnOiemO2g86ZSkJtNul2xgkbsLOCfs-ms7FLxbEZpn4BvkVPWoGOm65aKB-FP5LGYacI6pA0aPhzeh3luFlLFUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
