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
<img src="https://cdn4.telesco.pe/file/FdIAWlFSCBICML9vV8hJlvgG7q5eTRbInBmhSXZ8CeCHBe-1Yn2uZo17fMFFT2FdIp3plK5Q2ZLL4lDSFc-7z-QuJTQEWREIve3hyqHfZUiOoJ5PvjhhKWUlGR0D9T9ro1BHsumxmM7sq6g5T5SR2OGen2q5mL-FYB93ckaz0aLDaKJ3OHfUbYFkzvYjIbGGY5zDHTF7whLr4fufr6Za5VH_jtoiwA7RIc98dCnJ0eJB219PKcHRqRjcd2AFiELjKe2TXX_957Da2e4CyV8W796AOe81JTjAl2hnng9W9C25k9qNrctRn_PrTnz9Vs2qYbiRc_N0M0kWdv9JLfbbGQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 02:47:57</div>
<hr>

<div class="tg-post" id="msg-465782">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQoP4i799DZRE8z0JgtyX6W3OUAlwtg-banG0bWCK4HvkPHPFhBeaRApBu2j6CABnxNeR2yBrs9fjgm9EaX7JJYYgpP5q3wXmLCSJ17KD6gy67_SlATRFE7C_9ixtIm3kJWh32vWzJ9n_mkF2KSgeGVHDMESTdR0EAlueiJDwFMXjIblu5NHwwrjETR2aQy_w9GzOJ4a-sxrO0kSqM-SJ1JiMY4sKnf-NNc7KmBiV740adpfR5TqtQHc2mcVbc9WMhZoxl_1D2a8DsNdLvaBQlOVhffL7EWXRO3ftDGlVRo98QsCYO841uTetv6Z-ipwZPNWhf-q9CQuaUB8wQQHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف برلیان‌های قاچاق ۱۰۰ میلیاردی در فرودگاه امام
🔹
فرماندهی پلیس فرودگاه امام خمینی(ره): مأموران گیت بازرسی به محتویات چمدان یکی از مسافران خروجی به مقصد استانبول مشکوک شدند.
🔹
با حضور مأموران و بازرسی دقیق بار، ۹۷ گرم سنگ برلیان که در جدارهٔ چمدان جاسازی شده بود، کشف و ضبط شد.
🔹
کارشناسان ارزش این سنگ‌ها را بیش از ۱۰۰ میلیارد ریال برآورد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/farsna/465782" target="_blank">📅 02:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465781">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSGtKEtSnYNpIJYygg3bj6sUONPFjRRvqTogLjWm0fWSIjiIxk9hbJXTr8cs61_wCrTD9R6yDSNLQnbbpx0dk78SKpRK8PUvzl7AoDX1BkHg2sPhIF3Kfm1jK8bqGQd2yAHyORMOHI6CA6C-lEsF7y0y_06ehki66YTUvfBkd1qa_vrCwYSKPf9ij0geNwqxU-zk6cC9mnr5YaWlc4Ph2X0F4PQZAHDlOXbjIE6vw7AUgrKvHOjb2Ox6vu2cpb52yBIj9I1g9ypeDC-vhnBMzDXuv5aiJ0DBiWO7j2lNrfHCqs1_gabWA8VELV4WPQ6BgeYNCQDe0vG6YcabrgSl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نقدی: رهبر شهید فرمودند انتقام خون حاج‌قاسم اخراج آمریکا از منطقه است؛ امروز شاهد گام‌هایی در این مسیر هستیم
🔹
مشاور عالی فرماندهٔ کل سپاه: آمریکا سال‌ها در این کشور حضور داشت و هزینه‌های سنگینی متحمل شد، اما در نهایت مجبور به خروج شد و این تحولات نشان داد که قدرت آمریکا آن‌گونه که تبلیغ می‌شود، نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/465781" target="_blank">📅 02:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465780">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2WkbqKhM_F1POq9zqMpCTqCKfqu10Nft8kv6MJIz5dBUj4wVA3MY-4sEgV43i39xF5-y5pHvIYgkh1noJ2Yb5lfVaPG0Xi1vMJjXAg4IHF6_eCVychaOjaXsZYk3M707mi56_v-RuMfXcmierGW4lgpjkJKrBfIY0QwIHhtE-M6S6v2G5BuL6vr_wW9bDOUtzbRkW4iaKmO_qg6ufB2659Sr4lDV0F4BCIZRU1eOhgm0mMA_Tfu-OsTcpwTQesj5GD1nVcUUush-W9_4eOLhHIh5vfooa4aVrqW64NIGO-zBugOdQyxJ6uz2_JFJU42Cj-s5IVMh77qEVC5BMYeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توهمات ترامپ: ایران آمادهٔ تسلیم شدن است
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد: ایران آمادهٔ تسلیم شدن است؛ ما الان می‌توانیم به راحتی پیروز شویم.
🔹
من معتقدم بلافاصله پس از انتخابات پیروز خواهیم شد، اما شاید حتی پیش از انتخابات.
@Farsna</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/465780" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465779">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مخالفت حدود ۷۰ درصد آمریکایی‌ها با جنگ علیه ایران
🔹
نتایج یک نظرسنجی جدید نشان می‌دهد نزدیک به ۷۰ درصد آمریکایی‌ها معتقدند جنگ آمریکا و اسرائیل علیه ایران ارزش جنگیدن نداشته است.
🔹
بر اساس این نظرسنجی که روز پنجشنبه از سوی مرکز تحقیقات امور عمومی آسوشیتدپرس-نورک (AP-NORC) منتشر شد، ۷۱ درصد از بزرگسالان آمریکایی از نحوهٔ مدیریت ترامپ در قبال ایران ناراضی هستند و ۶۹ درصد نیز معتقدند جنگ در ایران ارزش جنگیدن نداشته است.
🔹
این نظرسنجی که با مشارکت بیش از ۲ هزار بزرگسال آمریکایی انجام شده، همچنین نشان می‌دهد آمریکایی‌ها از عملکرد دونالد ترامپ، رئیس‌جمهور آمریکا، در زمینه اقتصاد و افزایش قیمت‌ها به‌شدت ناراضی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/465779" target="_blank">📅 01:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465778">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFSO_0PI0PxncNEaPEju4H8LThrvLgPgdwFLkNfLZJ9aFwxhWtKWTLQKpY6iI11tUoTdW0hb27xwQCGxL73Vt6yBpeHlq0EAyO-t_VeNunqmLlPSC6kji3XHwWzl9SrkgOYk_HnnCiCwRc0SQ7n7U0BmDixyT53uEUpuSwZH8BgKcfp3TXOr4HY-V8kSlhJm_6S5L9KWN-p3Gp02Hxq053JW0POm3OQxGeexvTO60MU6Umny8HOJ9XKePJnLFR3jhkKZg3tcO1jRWbpiMaydFQKwO2yUkgxdy9SE0Ventz8f0eNiGVRPQ8HYGeFUei_du0flvkdSCFpHE0ZiPsP4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشاگری وال‌استریت از دروغ بزرگ در مورد بازبودن تنگهٔ هرمز
🔹
کیم فوستیر، رئیس تحقیقات نفت‌وگاز اروپا در HSBC گفت اگر ادعای عبور زیاد نفت از تنگهٔ هرمز درست باشد، قیمت نفت باید ۷۰ دلار می‌بود و نه اینکه از ۱۰۰ دلار بگذرد.
🔸
وال‌استریت ژورنال هم در ادامه نوشت: به زبان ساده، یک جای کار می‌لنگد. بازار چیزی متفاوت از آمارهای ظاهراً چشمگیر صادرات می‌گوید. اگر واقعاً این حجم عظیم نفت به بازار برگشته و عرضه به وضعیت عادی نزدیک شده، چرا قیمت‌ها هنوز این‌قدر بالاست؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/465778" target="_blank">📅 01:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465777">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdc659a405.mp4?token=ocB6-kRrEck6uTh-KVrhJHVZ237JO3DNQ-SK1L-Bdj1rSBSMspDbp5yDaD_A037dfEcP4GS0UHHnCNEHBTIoOZRClIMW9uxe-id3hH-ySLpRu8ebgpzRBnK8sHon1OtqdnFA4f_YaMAplXi91ghPoFikIWvmtPt3csuYYSVne4aJy6nig-WQh51XLZxZ6I4H6UOYciI5wK_iqcR43HUhNqaf3HlLkPSNyk7ZAXMlzy2T_xPBLj4O7mzEn0plktTxqGKKaTxRDmBQCU1UIkJzEr10diml9YfBWVPHor6GT8sFQONfksZhAdyG6j3_FqUGJhFEwF1tffTwMM8WXu_CGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdc659a405.mp4?token=ocB6-kRrEck6uTh-KVrhJHVZ237JO3DNQ-SK1L-Bdj1rSBSMspDbp5yDaD_A037dfEcP4GS0UHHnCNEHBTIoOZRClIMW9uxe-id3hH-ySLpRu8ebgpzRBnK8sHon1OtqdnFA4f_YaMAplXi91ghPoFikIWvmtPt3csuYYSVne4aJy6nig-WQh51XLZxZ6I4H6UOYciI5wK_iqcR43HUhNqaf3HlLkPSNyk7ZAXMlzy2T_xPBLj4O7mzEn0plktTxqGKKaTxRDmBQCU1UIkJzEr10diml9YfBWVPHor6GT8sFQONfksZhAdyG6j3_FqUGJhFEwF1tffTwMM8WXu_CGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظلوم‌نمایی سعودی‌ها با شهر پیامبر
🔸
رسانه‌های عربستان درحالی از حملهٔ یمن به مدینه خبر داده‌ند که نیروگاه برق هدف قرار داده شده، ۱۰۰ کیلومتر با مدینه فاصله دارد.
🔹
پیش‌تر یمن با حمله به خط لولهٔ نفت عربستان، صادرات نفت این کشور در ساحل دریای سرخ را مختل کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/farsna/465777" target="_blank">📅 01:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465776">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6414482cf.mp4?token=YFcHDRhlyuL98phYp1Na8vMOIj1LJwkHywqGzRibzBcVzWnNQU_vGf6_j9XXq93cf5XpImiLpGgVJMQGLjAOgMa27dYwMebJ5TxR2-drh0lu2bw3U84A8KFs3SyGkqwJ453YrV0zkPTUjRUsrr11M6EIgSutt3JdoAaZ_bGb93UY4mhPCQa6RMbUHo6jz0l9hRiaTxgtXF89KN4dznlBQRuqbo11eT8Kr6qQIJO9_N_jy2r9OBKI_0DLAD-B5brk6hJwix4H0pn0Yxvgd-paX8MGrDWmqnVRZfAA5haZGbbuU_ZBESPWyv5VL1YPLcVBKz_NA_cXwqR4jxjdWxE8Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6414482cf.mp4?token=YFcHDRhlyuL98phYp1Na8vMOIj1LJwkHywqGzRibzBcVzWnNQU_vGf6_j9XXq93cf5XpImiLpGgVJMQGLjAOgMa27dYwMebJ5TxR2-drh0lu2bw3U84A8KFs3SyGkqwJ453YrV0zkPTUjRUsrr11M6EIgSutt3JdoAaZ_bGb93UY4mhPCQa6RMbUHo6jz0l9hRiaTxgtXF89KN4dznlBQRuqbo11eT8Kr6qQIJO9_N_jy2r9OBKI_0DLAD-B5brk6hJwix4H0pn0Yxvgd-paX8MGrDWmqnVRZfAA5haZGbbuU_ZBESPWyv5VL1YPLcVBKz_NA_cXwqR4jxjdWxE8Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زارع: سلام نظامی به پرچم ایران از قبل تمرین کرده بودم
🎙
امیرحسین زارع:
🔹
سلام نظامی به پرچم ایران را از قبل و حدود دو ماه پیش از مسابقات، زمانی که جنگ به کشورمان تحمیل شده بود، با آقای درستکار، تمرین کرده بودیم.
🔹
در سالن تمرین یک پرچم شهید بود و با سرمربی آن حرکت را تمرین کرده بودیم که ان‌شاءالله اگر به لطف خدا طلا گرفتم، احترام نظامی به پرچم بگذارم. یک خوشحالی دیگر هم انجام دادم که تاجگذاری بود و آن را در سال‌های قبل هم انجام می‌دادم.
🔗
صحبت‌های امیرحسین زارع را در
فارس
بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/farsna/465776" target="_blank">📅 01:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465775">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌ سردار قاآنی خطاب به عربستان: جنگ با یمن را تمام کنید
🔹
شما یمنی‌ها را خوب می‌شناسید و ما نیز آن‌ها را خوب می‌شناسیم. به نفع خود شماست که محاصره را تمام کنید و جنگ با برادران مسلمان یمنی خود را ادامه ندهید. توصیه ما به شما همین است.
🔹
فردا چه پاسخی در برابر…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/465775" target="_blank">📅 00:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465774">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ سردار قاآنی: جمهوری اسلامی حتی در اوج شرایط جنگی کنار ملت‌های تحت ظلم ایستاده است
🔹
جمهوری اسلامی در اوج شرایط جنگی نیز دوستان خود و کسانی را که مورد ظلم آمریکای جنایتکار و رژیم صهیونیستی قرار گرفته‌اند، رها نکرده است و پس از این نیز در کنار آنان خواهد ایستاد.…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/465774" target="_blank">📅 00:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465773">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌ سردار قاآنی: حزب‌الله، لبنان را به قطب افتخار مقاومت تبدیل کرد
🔹
لبنان زمانی حیاط خلوت بسیاری بود، اما از زمانی که حزب‌الله قهرمان تأسیس شد و پا به عرصهٔ مقابله با اشغالگری و مبارزه با رژیم صهیونیستی گذاشت، این کشور روزبه‌روز اعتلای بیشتری پیدا کرد و امروز…</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/465773" target="_blank">📅 00:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465772">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ سردار قاآنی: آمریکا با همه امکانات از عراق اخراج شد و از ایران هم شکست خورد
🔹
آمریکای جنایتکار با ذلت دم خود را روی کولش گذاشت و از عراق اخراج شد. مردم عراق امروز به برکت مقاومت آن ملت و قهرمانان جبههٔ مقاومت، اخراج آمریکا را جشن گرفته‌اند.
🔹
آمریکا موظف…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/465772" target="_blank">📅 00:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465771">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سردار قاآنی: با حضور هرشب مردم در میدان‌ها، شاهد دوره‌ای جدید از مقاومت هستیم
🔹
فرماندهٔ نیروی قدس سپاه: آمریکای جنایتکار با این فرضیه وارد میدان شد که ظرف چندروز ایران اسلامی را به تسلیم بکشاند، اما ببینید با چه وضعیت خفت‌باری مواجه شده است.
🔹
این مواجهه…</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/465771" target="_blank">📅 00:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465770">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758fa0c934.mp4?token=VZhT9W4Vo2lNebY3XhYdd78u-sWrQtn68t8LfEdEJgJgs0Qo8lwyJWUjWhTyOHDYS4dytFkmqgO2LsQnYv2mSlsE-PIhxZgXSptnlRECi_gRSzo3pHoBi2So8PvHixtsgSYk5zvamuBfldUEvItgo1DSdrEYc35TnbHJPD3Xcpkbptqx4_jSvGG2qZV7MrdZz2URtKTbheNuIbqMk3ZlmdMq55EAT6jfSu32kouwmWuQ83eOl1AmnA8HM3txZNaadVBpuP1W049GYBl6aFe2vDhq1jS9TX3yBxNI9zL4XiMW8OavIg2A7xjlpJt6jE4fadYadR9Ro-Ww2xEz_I-K-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758fa0c934.mp4?token=VZhT9W4Vo2lNebY3XhYdd78u-sWrQtn68t8LfEdEJgJgs0Qo8lwyJWUjWhTyOHDYS4dytFkmqgO2LsQnYv2mSlsE-PIhxZgXSptnlRECi_gRSzo3pHoBi2So8PvHixtsgSYk5zvamuBfldUEvItgo1DSdrEYc35TnbHJPD3Xcpkbptqx4_jSvGG2qZV7MrdZz2URtKTbheNuIbqMk3ZlmdMq55EAT6jfSu32kouwmWuQ83eOl1AmnA8HM3txZNaadVBpuP1W049GYBl6aFe2vDhq1jS9TX3yBxNI9zL4XiMW8OavIg2A7xjlpJt6jE4fadYadR9Ro-Ww2xEz_I-K-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تلاش ناموفق برای عملیات انتحاری در مسجدالحرام
🔸
منابع عربی، از دستگیری یک عامل انتحاری در مسجدالحرام خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/465770" target="_blank">📅 00:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465769">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت ۴</div>
</div>
<a href="https://t.me/farsna/465769" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۳ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/465769" target="_blank">📅 00:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465768">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTWaTddu2Y9jYr0YUWlDv0ZiAdYAQBEXb3dzMU7-3N55BC_yj6OYxkEnccBrOmM1yINtdc9_syrHbklV8KzQ-uOIEQWPApaiPJAqWLDRjWWmrBzjRWMNaGm06WJYgMHSa4WIfWfx-sggpq3OSKoS2QsNMsGzlWYBLqVkxnFVJik5hIbwxsQ878AufVo7-wbx47QvN52Ma7pR7vrqLh98FSexR60-S8Xnc-9iBn9KuGjDWAxc3-r2oByM8JK9arTK4YobLb8J1qGpxiqiBrEou9a_68SIvy2g-6-Fj8dZlfx9p1N2m8gnTt9tI-YyqA8GuZ9Mn7W2rvgecme83tUkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ممکن است از اروپایی‌ها بخواهم اقدام به آزادسازی ذخایر اضطراری گازوئیل بکنند
.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/465768" target="_blank">📅 00:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465767">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حملهٔ جنگنده‌های سعودی به یمن
🔹
رسانه‌های بین‌المللی از حملۀ جنگنده‌های عربستان به صنعا، پایتخت یمن گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/465767" target="_blank">📅 00:27 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465766">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVFiGXNmHOwktj69wzPnC4JMyrOyRYv1ARayuZ44BXMn5deNWvAxPoqoMv3Y2y_cf70EI1xyhEPNiEpmqyHFN9v1IIAbjW-7fRVPRhOA-M5Y1voMOMpJwe22LWPSVuvgMVk4Y1-8hWH6kGCuGK-yScFNZjc8s6J5XS0ilYexlAggsmVtEeb400rSE1YptKcUUy1tcEpvY84l5kV2k1k_zeWfeMqJ6r63jE7WZSQxJiJn-aSnpCgqjlL_OJdlIdQ0EDWlNN_b01nDiUHM9SafHaX9K083thaATThhN3fYoyFHOINViU33oS-9LCT69IROb-IFFTTAW5e2BNBMO5s9Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار قاآنی: با حضور هرشب مردم در میدان‌ها، شاهد دوره‌ای جدید از مقاومت هستیم
🔹
فرماندهٔ نیروی قدس سپاه: آمریکای جنایتکار با این فرضیه وارد میدان شد که ظرف چندروز ایران اسلامی را به تسلیم بکشاند، اما ببینید با چه وضعیت خفت‌باری مواجه شده است.
🔹
این مواجهه را در دیگر صحنه‌های مقاومت نیز می‌بینیم. در لبنان دیدیم تبلیغ کردند که حزب‌الله از بین رفته است، اما شاهد بودیم که حزب‌الله چگونه ایستادگی و ضربات مهلکی به دشمن وارد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/465766" target="_blank">📅 00:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465765">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRYNATafQFp3piVwv3iJuHZRsSXNWEZxKLhJCTt5VQ6ekRQemmGSadGDw_sVfw8wadBDoRVnxtE1yvOFok7y0ZQw1QCyXkDY2p7JX1KP21BeYGdxndmxtnsMdOAQaMv8i_plGAbBzjBzVsfzEd36yDnqH8jWgcljozhwS7TDVEtkQwDGtAw06S1RxBnGEW2RW9_VuswnLgo9CA2xshg88yKIKQdPLxAfRRtowwlr78Ghp7dz2Wp6IkD_9PUBnDkv35pfPNQOFyhBrOXaN3PLr_mV_RhoSFzGU3yL9xu6Ll3r-NxXf04lMjmJQQkSkbWyFoq6rhPFM_O1jPjLrjX0uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه همین لباس زیباست نشان آدمیت
🔹
روزی ملانصرالدین با لباسی کهنه به یک مهمانی رفت، اما صاحب‌خانه با داد و فریاد او را از خانه بیرون انداخت.
🔹
ملا به خانه برگشت، از همسایه‌اش لباسی گران‌بها و فاخر به امانت گرفت، آن را پوشید و دوباره به مهمانی برگشت.
🔹
این‌بار صاحب‌خانه با خوش‌رویی فراوان به پیشوازش آمد، خیرمقدم گفت، او را در بهترین جای مجلس نشاند و سفره‌ای پر از غذاهای رنگارنگ جلویش پهن کرد.
🔹
ملا که متوجه شد تمام این احترام‌ها فقط به‌خاطر لباس نوی اوست، آستین لباسش را جلو کشید، داخل غذا برد و گفت: «آستین نو بخور پلو، آستین نو بخور پلو!»
🔹
صاحب‌خانه با تعجب پرسید: «این چه کاری است که می‌کنی؟» ملا گفت: «من همان کسی هستم که چند دقیقه پیش با لباس کهنه آمدم و با داد و بیداد بیرونم کردی؛ حالا که لباس نو پوشیده‌ام این‌همه احترام می‌گذاری. پس این احترام و غذاها مال این لباس است، نه مال من؛ آستین نو بخور پلو!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/465765" target="_blank">📅 00:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465764">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOQlld6_NYeT1iHL5fcN7xumn5eF6EG-BRLkZh_GF2BnMsIfijcrlQ5fehh42xvlNV9XvFNL6herKjEiROnLoAepk3Q-HUEWwBM9czdHRQ4XE7AVr0UQHPci8MilaSoln7jNm-LfSJauO0qLlBT1ntg3_ft8XgH53QolIDAtu3ucSSG8mGYVVweXWxdFaK1OjojahKYtPVr1YAurfV5nsQt84iz1aV0v2Gu2SMl39Di73KCJJKbyym7se4j3ZLop2ypZnOu2RnTiztfnaRBBOZ2aUVXS2det-HHLV9GdIQZ2lYh9y4hdl69yh8dXeCuAmxgVKN0sw1qFu-n1AX9XfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/465764" target="_blank">📅 00:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465763">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLBWn7KS6JndWKZXp5XsxgihsWHduaduNNjTSVjVeCp8B7HcKmW3IsNEh9qG3wS06UXvydtIFSWQRPoPHpRq9qkD5le7dH5F6Sxwjly5HPEp7dGBaTkakz73AIy6mw-T3-rb2COay5Bcv53JmCPgDtIVIebhxG1ZGvjUxsVmbbvr5-f4vDAka2zybnc1uigjJsPJEcHCQldQv7shnNefKL5FahtDNzmCupnpMI0rpbm34FOMo8biAhnD3csaWF3AYqg_20o5Osmt-zxeOAc-w-FOz3f19oiSxyz-vd46RtfoyRU6VhWlK3uhPv0hWHZDOgVn275OMKt6DbWhjPm14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سوپرنفتکش متخلف در هرمز منفجر شد
🔹
منابع محلی گزارش کردند یک سوپر نفتکش با ظرفیت ۲.۵ میلیون بشکه که در مسیر غیر مجاز تنگه هرمز تردد می‌کرده در ۸ کیلومتری سواحل عمان مورد اصابت قرار گرفته و در حال سوختن است.  @Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/465763" target="_blank">📅 23:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465762">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
منبع آگاه: برنامۀ نتانیاهو برای پیروزی در انتخابات، کشاندن ترامپ به یک مهلکۀ جدید با ایران است
🔹
یک منبع آگاه منطقه‌ای در گفت‌وگو با پرس‌تی‌وی: سناریوی مضحک ربایش هواپیما به مقصد سرزمین‌های اشغالی از مبدأ امارات و فرود آمدن در عربستان در حالی روز چهارشنبه اجرایی شد که ۳ روز قبل از آن، نتانیاهو با همراهی چند مقام ارشد امنیتی و نظامی خود به امارات سفر کرد و این پروژه در آنجا بحث و نهایی شد.
🔹
در آن سفر علاوه‌بر موظف شدن امارات به نقش‌آفرینی در پروژه‌های منطقه‌ای رژیم صهیونیستی، مذاکرات چند جانبه‌ای با حضور مقام‌های چند کشور عربی دیگر  برای طراحی یک عملیات پرچم دروغین و انتساب آن به ایران برگزار شد.
🔹
هدف از این عملیات وادار کردن ترامپ به مهلکه و دور جدیدی از جنگ با ایران است چرا که نتانیاهو به شدت نگران است در صورت برگزاری انتخابات کنست در شرایط کنونی، ائتلاف او قادر به کسب اکثریت و تشکیل دولت نخواهد بود و در این صورت، با برکناری از نخست‌وزیری، باید ادامه حیات سیاسی خود را پشت میله‌های زندان طی کند.
🔹
نخست‌وزیر جنایتکار رژیم صهیونیستی امیدوار است با تسلطی که بر کاخ سفید و شخص ترامپ دارد بتواند بار دیگر او را وارد یک جنگ گسترده کند و از سلاح، اقتصاد و اعتبار رو به افول آمریکا همچنان برای ترمیم وضعیت بغرنج سیاسی خود استفاده کند.
🔹
در ایران، با رصد کامل تحرکات دشمن آمریکایی و صهیونیستی و سناریوخوانی از احتمال حماقت جدید به بهانه پروژه مضحک نتانیاهو در ربایش از قبل طراحی شده هواپیما، این آمادگی وجود دارد که در صورت هر گونه شرارت دشمن، ضربات سخت و ویران کننده به‌گونه‌ای به رژیم صهیونیستی و آمریکا وارد خواهد شد که از پرچم دروغین و بازی جعلی خود پشیمان شوند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465762" target="_blank">📅 23:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465759">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lwn_5XnWwlIrDyrWU8Vr_tF_wpEjlXEMQIaCbGjqUTi9R6o4mA6D0kEMWDuP9atDOYcu0gh6tLqK4FN28Uh0u1Ybhh02h8OI-GwkmoYljMoSIHwYIu9iAjpcSDzufZeoQzWOFAjL0cHTv_j1T0WAOH-jT03cNFgt4ifsxhrQkKKwF3U-6P-m5nbNPxaC1k6COYr7apu20m13wHm2AKccwiTzwAY0r_PSgWEk1HRMOvxvQ1UClSGa4NlGdMy3Z9g1gkCOkBmtE1CkJKmG4gIncrD1_ylaYOIMWhJLQefKGcn4Kz03sEoca4waL3fF7X0Ike5NTyNC14tz0PXvVPHnsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WxDXl0CoIQSOZ1LTFdfMpFf_KsUWCyHPjhUIwuHQVlGriGSz8nsqi54mG2xQ4VJVGdyJByONCboM0WG91ytWj_hIPPfhpwkqBY46LA8r0s2gtfbXgvtqmUMAbhwwGsfn49j6eaNwNNw21Qfaykl7xCiNVg72xjBLQ2HO4GV1BgiUftKii_dmsGM0_fOO5glGUtqjGj2HcnhQ2wpkg2CZ7Dj_p8LYVDeMudF-KHSQixIOYVvyabOtXXMMnhPjki1G9d4-sEj1FkBIXiC8P8hnSKBS1aAnQal2ZFKndGiRTrYyDHgtFKst7sgMUl2w5jvQNa8YYPWHrEvqbdwtEOCzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hs5UHJvVNTw4pv8EIQCmnrwcWdOoPlFvzznjB6DKJwhmWRB8Z430DEK1ssvot_9uGkR3Iu83GIRImqXBXxDyOzQ7-vaYURU20rDpjTF23G0hPfh-YY8msGZMhORpl1XuvqkNollFXUVSURm_BuJ8wtXgt-NAI0B0ENlQZcQ0oNs7__1_tlhKSL7LX4EA70fhVzmgWI43X4RVGuZJSonQLGoWA8OlHQPtUe4LJ_4qQsKC81Ue3CCE1Q_2a2ZZgKOyCHKUvBP5j24t8Gs70M5usPGez5n2GO4BWkoa7xoZcCCV-5jVxu5s16ClJap31TZJLxrTf0wPvjC_-0kqc03zyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/465759" target="_blank">📅 23:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465758">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‌ ادعای بلومبرگ دربارۀ پیشنهاد مذاکراتی عراقچی در نیویورک
🔹
بلومبرگ مدعی شده، وزیر خارجۀ ایران، در دیدارهای خصوصی با دیپلمات‌های اروپایی و منطقه‌ای در حاشیه مجمع عمومی سازمان ملل، پیشنهاد بازگشت بازرسان آژانس اتمی به تأسیسات هسته‌ای بمباران‌شده ایران را در…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465758" target="_blank">📅 23:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465757">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
سوپرنفتکش متخلف در هرمز منفجر شد
🔹
منابع محلی گزارش کردند یک سوپر نفتکش با ظرفیت ۲.۵ میلیون بشکه که در مسیر غیر مجاز تنگه هرمز تردد می‌کرده در ۸ کیلومتری سواحل عمان مورد اصابت قرار گرفته و در حال سوختن است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465757" target="_blank">📅 22:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465756">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حملۀ موشکی و پهپادی یمن به جنوب عربستان
🔹
عربستان سعودی مدعی شد که پدافند هوایی این کشور با ۴ پهپاد یمنی در آسمان شهر خمیس مشیط (واقع در منطقه عسیر) مقابله کرده است.
🔹
طبق این اطلاعیه، ۲ موشک بالستیک نیز به‌سمت شهر خمیس مشیط و جازان شلیک شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/465756" target="_blank">📅 22:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465755">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aESZEGrjSEKHS3x2o3i1-1XaYCMC383P6vHQe1_kcdTQ-Y2Gs6lWhSBQx8r8JE7MT41Jp3r0h-OtJEUJvM4uXXvLcWNq-gkHxBFXwQwsyq9JgFqwdwQlrSgSgZTG7bf9XUqaFrKCFb5Sqr4xpRbFZ5YdWC60mhqxFQgCNFWon-ciYXRhi_JHE1XHAL_KjSq2hXf0zU8hV8rgaSsvJbZTiRyf2gKaXk_UtBEl02skZE10dCneeB7Zk7TIWBQTLTYXZhLkWKPcsMQ5cM2kSKCWkeHeVH9Xh9vqBn7OlKUki7xOhLuFxcZXvDMwlZzKv2GdQGtEWZp_l7oLF68EH2LkMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار نهاد مدیریت آبراه خلیج فارس به مجموعه‌های مرتبط با شناورهای متخلف
🔹
فهرست شناورهای متخلف در آدرس www.pgsa.ir/non-compliance-list به‌روزرسانی شد.
🔹
به شرکت‌های بیمه‌گر، کلاب‌های P&I و همچنین موسسات رده‌بندی هشدار داده می‌شود، به‌منظور مصونیت از تبعات…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465755" target="_blank">📅 22:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465754">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb3816caa.mp4?token=t4QeqUj1oc2N0yDbl7VAtui0wF0_CMRzEAUx7eOMa5PfPMGomjkOxg9z30EPnOAxwPmdZI_iADkBg2e_H1Xy2OpMco6ghbDzAnCysSVzLan-TTIzxH_AtjnUJ6FiAqeAWppWv-GKCQZLp_wUKS8wfvEStFu504eVfZTyeSC7NY_oW08RNVYIT11LuM9p8-OPl3kMWDvPBCf_LHOhbPmpB7bzZk4Dhe3G9rjTPZ_-UBzQK1dzjo7SindQWy1nuE4dXRpt5KN560j26GwFOJYJxzwE-QrIfh2KS5z5PeUYahzrbeN1eZkpmaDA4N1TzogN8RJY5Vr21tK13JLNyDKB3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb3816caa.mp4?token=t4QeqUj1oc2N0yDbl7VAtui0wF0_CMRzEAUx7eOMa5PfPMGomjkOxg9z30EPnOAxwPmdZI_iADkBg2e_H1Xy2OpMco6ghbDzAnCysSVzLan-TTIzxH_AtjnUJ6FiAqeAWppWv-GKCQZLp_wUKS8wfvEStFu504eVfZTyeSC7NY_oW08RNVYIT11LuM9p8-OPl3kMWDvPBCf_LHOhbPmpB7bzZk4Dhe3G9rjTPZ_-UBzQK1dzjo7SindQWy1nuE4dXRpt5KN560j26GwFOJYJxzwE-QrIfh2KS5z5PeUYahzrbeN1eZkpmaDA4N1TzogN8RJY5Vr21tK13JLNyDKB3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خالی‌بندی با طلای مردم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465754" target="_blank">📅 22:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465753">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‌ ‌عراقچی: مواضع ایران هیچ تغییری نکرده است
🔹
از چندین ساعت قبل ادعاهایی مطرح شده که با قاطعیت عرض می‌کنم که هیچ تغییری در مواضع ایران رخ نداده است.
🔹
شروط ما برای بازگشایی تنگه مشخص است. در خصوص سایر مسائل نیز موضع ما مشخص است.
🔹
درحال حاضر فقط موضوع تنگۀ…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/465753" target="_blank">📅 22:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465751">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbbcf0fa2.mp4?token=ShGszfMONgE4KCYCfwW2j9LCHuPropR3wulHtjLsVKcl0qnW_3TIYWj0H1o46A_OXVdjnbE87HMG8PAtKA-MdS4wYhMbBaSWpCuMdSGbkTj1-cB0hY0c0yGHlYTHJFG6__7QO_jhhDwHlYhUqlNV12vTcyqGp59DPN3B3ats6nfXFUrCCldHX_YZOQlSUH4xiy-ZhKxZmV9rtoVr-O5j92T54-QSYV3p7d2hKH6IRrXpaJzdlm9dxBcbGLAFNr_l0Y6mc5mHoeQp59FdD__RuV3ma6fTJYBUcoht66As1D08AjJGPqYmoD6odC1O6p5OR57oNsRQ3b5jcdZmRp7FwaNWi7SL2aY_6qpygVsePVao1Z4OrbXVErSWqLBQExP6gZLaYTMJh5G2vfXbm9fzXUgFEN3gXZVdr7WMOTa6s1bXB7aDMI47vHikd960KVrciF7i_BAWcbT2sjxJ--_sm46U6QYhN-jQy6NNKKdYjHhS0zsAGtmYnxo0e4KUenXyrvuXu8ahDiFIDSzWLtd60Bl8G6CnIFGbHJ1eSV2SuvWUdXEdMy2NzX8vAj3Q7wrjnjygGTX0YHquzZqO9-To2C1_RTZLdmuZPRbbxmWJc1mV4KPxNy5rWHA5pDIO2rOgufQy5lMImGC_uDkjakiYStFm7rlHQWvyYDbKU8dC6UE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbbcf0fa2.mp4?token=ShGszfMONgE4KCYCfwW2j9LCHuPropR3wulHtjLsVKcl0qnW_3TIYWj0H1o46A_OXVdjnbE87HMG8PAtKA-MdS4wYhMbBaSWpCuMdSGbkTj1-cB0hY0c0yGHlYTHJFG6__7QO_jhhDwHlYhUqlNV12vTcyqGp59DPN3B3ats6nfXFUrCCldHX_YZOQlSUH4xiy-ZhKxZmV9rtoVr-O5j92T54-QSYV3p7d2hKH6IRrXpaJzdlm9dxBcbGLAFNr_l0Y6mc5mHoeQp59FdD__RuV3ma6fTJYBUcoht66As1D08AjJGPqYmoD6odC1O6p5OR57oNsRQ3b5jcdZmRp7FwaNWi7SL2aY_6qpygVsePVao1Z4OrbXVErSWqLBQExP6gZLaYTMJh5G2vfXbm9fzXUgFEN3gXZVdr7WMOTa6s1bXB7aDMI47vHikd960KVrciF7i_BAWcbT2sjxJ--_sm46U6QYhN-jQy6NNKKdYjHhS0zsAGtmYnxo0e4KUenXyrvuXu8ahDiFIDSzWLtd60Bl8G6CnIFGbHJ1eSV2SuvWUdXEdMy2NzX8vAj3Q7wrjnjygGTX0YHquzZqO9-To2C1_RTZLdmuZPRbbxmWJc1mV4KPxNy5rWHA5pDIO2rOgufQy5lMImGC_uDkjakiYStFm7rlHQWvyYDbKU8dC6UE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران: در پاسخ به شهادت اسماعیل هنیه، سید حسن نصرالله و شهید نیلفروشان قلب اراضی اشغالی را هدف گرفتیم  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465751" target="_blank">📅 22:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465750">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c68b1085a0.mp4?token=X-JwgNjphDKPlpjnU7jT9550xv4ycRTUZph6rWd6mrgQ1WR2RedZko3DwLkkL1AHB9COrmEFgHlPtt1UeNgqchZs9cFuqQzOVeNreeQYAF6ow2ImoKpIT-3OAD6D-qIkZfbOPdA-N0dnIQM15_zmALkSrPuulVyL5fy7p4MZofTP_xEJ5fPvmsL4nQdnkrJDmBzYwGlTpifmvrK0M-xE0sBdmCu1O1ItvqEEgNqEfHb5fy7Hi2vZBsr0en_gxuRjqQM8YCiTOeZunwL5uR9MVO9LwHD20Q_tdwuw1_EzNd3YrrgP1RCxig2aBU_aQRxu8p1hFS2_tjMFE-5xdwwd9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c68b1085a0.mp4?token=X-JwgNjphDKPlpjnU7jT9550xv4ycRTUZph6rWd6mrgQ1WR2RedZko3DwLkkL1AHB9COrmEFgHlPtt1UeNgqchZs9cFuqQzOVeNreeQYAF6ow2ImoKpIT-3OAD6D-qIkZfbOPdA-N0dnIQM15_zmALkSrPuulVyL5fy7p4MZofTP_xEJ5fPvmsL4nQdnkrJDmBzYwGlTpifmvrK0M-xE0sBdmCu1O1ItvqEEgNqEfHb5fy7Hi2vZBsr0en_gxuRjqQM8YCiTOeZunwL5uR9MVO9LwHD20Q_tdwuw1_EzNd3YrrgP1RCxig2aBU_aQRxu8p1hFS2_tjMFE-5xdwwd9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یمن تصاویر شکار مزدوران سعودی را منتشر کرد
🔹
یگان تک‌تیرانداز نیروهای مسلح یمن با انتشار تصاویری، از عملیات‌های خود علیه شمار قابل‌توجهی از نیروهای مزدور وابسته به سعودی، اعم از عناصر یمنی و سربازان سودانی در جبهه‌های جیزان خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/465750" target="_blank">📅 21:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465749">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=V55279ChSivcPMLH_l0Sm6fTvqE-aSjsGwJfYDO5-WZ1_UNme7i88g5PtoZozIPLHEYAkWKiqrmqRJFeEqqDFNcB9JWWHtEmTiQcpjOy-Ck6JObM31X8xH-2XjLp3vDmkEvQbt2xFxuZRAgRYvBrm5HQoOxmEY5ruwrGUQGQjUn-fABsVkg67-H5a1DrES0DdPFisyFP4n_voX9LfASW_3KJPwbtqtxgDHa37ftvToBJY9_xNSSERGgybrd6jbj23oQNfmR2ibGnpDgVbWb2lhDvQd8j1Xpk7qpUgMAnN9A7QpQNyajsuEqcJhXByAIFPompneOvn4QTham2LZWPUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f37f482f.mp4?token=V55279ChSivcPMLH_l0Sm6fTvqE-aSjsGwJfYDO5-WZ1_UNme7i88g5PtoZozIPLHEYAkWKiqrmqRJFeEqqDFNcB9JWWHtEmTiQcpjOy-Ck6JObM31X8xH-2XjLp3vDmkEvQbt2xFxuZRAgRYvBrm5HQoOxmEY5ruwrGUQGQjUn-fABsVkg67-H5a1DrES0DdPFisyFP4n_voX9LfASW_3KJPwbtqtxgDHa37ftvToBJY9_xNSSERGgybrd6jbj23oQNfmR2ibGnpDgVbWb2lhDvQd8j1Xpk7qpUgMAnN9A7QpQNyajsuEqcJhXByAIFPompneOvn4QTham2LZWPUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا در شهر صور در جنوب لبنان: نگاه ما همان نگاه آقای شهید است؛ آمریکا از منطقه اخراج می‌شود و جوانان به‌زودی در بیت‌المقدس نماز می‌خوانند
🔹
آنچه امروز در جنوب لبنان می‌بینیم، روحیه پیروزی و مقاومت در میان مردم است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465749" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465748">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9ajTHBWCGTjVpKXm7HicwieBYj91qZF-PMrQgDDZ2jZs20OJ_WFdeO31O-FQn6rRnjmoVe-gdKNI69hx8XkNjdPCVIzVdIx_8mSrKrLfFUGHs-ZfwuuyJwEfsnXygOilC3AE5JXE_dpE89sZk1O5YA0n7qFlCwirpSuj30QiPQh895nBqWIpQ02lYcWPUIHdk6CFpuV9wtGZlt28Yioohok1LH9CN0hy09UMnhFwkAfWV8KTRM0tuOE6K9AjlZaDEpzlwOdGGkxHXYEJPzd6FjDCxhHf3ZnQZEIQep1U84HYJGvbe_7FD8osdjF1__bcAxv6HvTHTteMj3e5FJ5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پوتین: جهان از شجاعت و قهرمانی ملت ایران و مقاومت آن شگفت‌زده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/465748" target="_blank">📅 21:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465747">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/465fb0908e.mp4?token=fbZfcWJFZ9kX7ye_b95c6h6FDBiOVz_Lny7j63qr-_Yj_XxYTJ0TmtTdnK0sUe-21yOFCK6r3eiiEBHQf9wbp1WpxNJvxryyiYrkcpahiZPEgHJte8EekkhZc1Bk0JGlHOOROvvXpruXYGVYwqXQXtir8kD_-KyueEO8qdQaqS1WuCa7nBReQKVdGDes1CM1O1XTx3IGA-_lGbc7IcB5KglzvEowNZi0_5oDjMxQcjSq9r9U89CN1-G7qQORCCML54Q_YNvlnYosG4Jwyf66jnfKSuRtXcZTsXUUqAsZU8w7qpwkt7_0KoNmQI62-JqW_aD0gMuYULw-9vwgEi7p1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/465fb0908e.mp4?token=fbZfcWJFZ9kX7ye_b95c6h6FDBiOVz_Lny7j63qr-_Yj_XxYTJ0TmtTdnK0sUe-21yOFCK6r3eiiEBHQf9wbp1WpxNJvxryyiYrkcpahiZPEgHJte8EekkhZc1Bk0JGlHOOROvvXpruXYGVYwqXQXtir8kD_-KyueEO8qdQaqS1WuCa7nBReQKVdGDes1CM1O1XTx3IGA-_lGbc7IcB5KglzvEowNZi0_5oDjMxQcjSq9r9U89CN1-G7qQORCCML54Q_YNvlnYosG4Jwyf66jnfKSuRtXcZTsXUUqAsZU8w7qpwkt7_0KoNmQI62-JqW_aD0gMuYULw-9vwgEi7p1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی بازگشت بدون پشیمانی هنرمندان به وطن، دغدغۀ عدالت و اجرای قانون در جامعه را بیدار می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/465747" target="_blank">📅 21:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465746">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b6b8f25a.mp4?token=FZJbt7kzFWjaVHccHs7MbRJCO74fcW5bGHAFrKaQmKxueFmoP0skcMhPuK8uhlO4x_WmE2Qlh3Zh8rpYw1gQqusKAIn9DaGCYc2j6FXzZ98-2evjHzz6fdxpA_Oi3LPZjUt9v7NbQkFhIioacfi8m-6aoNiLR5JK-fPHKb4OWOxKcqs-LUa3As-j8d-_hc7TwPkIUCSFm3wfgJhwc6O62Vqe9Ai29KB8XQRPqjqaIq2wU_n7ZS1UCVzFmVlMTKv-MeZvuDzSGUVJeMySGF3PExdpabHMEiAzzHPi6hZ_ctorQinNx90I3lM9e1nhaucbCKWm8TRf5MsXz_uAYAhGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b6b8f25a.mp4?token=FZJbt7kzFWjaVHccHs7MbRJCO74fcW5bGHAFrKaQmKxueFmoP0skcMhPuK8uhlO4x_WmE2Qlh3Zh8rpYw1gQqusKAIn9DaGCYc2j6FXzZ98-2evjHzz6fdxpA_Oi3LPZjUt9v7NbQkFhIioacfi8m-6aoNiLR5JK-fPHKb4OWOxKcqs-LUa3As-j8d-_hc7TwPkIUCSFm3wfgJhwc6O62Vqe9Ai29KB8XQRPqjqaIq2wU_n7ZS1UCVzFmVlMTKv-MeZvuDzSGUVJeMySGF3PExdpabHMEiAzzHPi6hZ_ctorQinNx90I3lM9e1nhaucbCKWm8TRf5MsXz_uAYAhGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین: پیشنهاد ما برای انتقال اورانیوم ذخیره‌شدۀ ایران به روسیه همچنان پابرجاست.   @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465746" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465745">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0e7d1f59.mp4?token=Dm-ax7P3VcYzWbmMAAT6yVgIIiZHnVFdNDRYESkJxd5taE_ouvWQDqzTCVzara7nqVW3Kgaj327gtUjW5DYoeRQum_03unz88KzXog-6ghB0uK1tDSNsP1NCPAmtc91gabFsLtn7st1Ziv0t1oYtieUcMFbe4PauQoZch5u2yBtpBM9i7POSVBIyuIwAFfJVFYeBfSCRQ_DKYLe9YLvVpZipEz5QmRMA0TU9zScYz8Htti5aWOSas2G3njw8spyfSmiPZXGj4I2sR5FcZcgtkgh1gyXHudXOw47LJDo4dLs_V8lpi-UuE_stvIlk4RFImEgXMmjAfHhHfBMuFIGjtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0e7d1f59.mp4?token=Dm-ax7P3VcYzWbmMAAT6yVgIIiZHnVFdNDRYESkJxd5taE_ouvWQDqzTCVzara7nqVW3Kgaj327gtUjW5DYoeRQum_03unz88KzXog-6ghB0uK1tDSNsP1NCPAmtc91gabFsLtn7st1Ziv0t1oYtieUcMFbe4PauQoZch5u2yBtpBM9i7POSVBIyuIwAFfJVFYeBfSCRQ_DKYLe9YLvVpZipEz5QmRMA0TU9zScYz8Htti5aWOSas2G3njw8spyfSmiPZXGj4I2sR5FcZcgtkgh1gyXHudXOw47LJDo4dLs_V8lpi-UuE_stvIlk4RFImEgXMmjAfHhHfBMuFIGjtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دومین پادگان آموزش نظامی «جان‌فدا» در تهران آماده می‌شود
🔹
پس از افتتاح نخستین محل آموزش نظامی پویش «جان فدا» در میدان امام حسین(ع)، آماده‌سازی دومین محل برگزاری این آموزش‌ها در میدان هفت‌تیر تهران آغاز شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/465745" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465744">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">منبع نظامی یمنی: اتهام حملۀ پهپادی به مدینه پوچ و بی‌اساس است
🔹
یک منبع نظامی یمنی در واکنش به ادعای عربستان سعودی دربارۀ هدف قرار گرفتن نیروگاه برق «طیبه» در مدینه منوره را بی‌اساس خواند.
🔹
او در گفت‌وگو با خبرگزاری سبأنت، افزود: عربستان با طرح این روایت تازه تلاش می‌کند ناکامی خود در پیشبرد روایت قبلی درباره حمله به مکه را پنهان کند.
🔹
این منبع نظامی همچنین تأکید کرد نیروهای مسلح یمن در برابر این بهتان سعودی سکوت نخواهند کرد و حق پاسخ به این اتهامات واهی را برای خود محفوظ می‌دانند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/465744" target="_blank">📅 20:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465743">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465743" target="_blank">📅 20:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465742">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf4a9a059.mp4?token=chkaP-BH7-K1ujZpQqLez-0GdgczBJjHkG8NFn1qSWx2xpeLcrUG9nVBFeARvUEdJ8PO0e7h0-HwUEPdoXofnJa3kuOMExVVXduGpOhMGnMKn5UFL2oMcT0kd6ZGQxYFQ_mLdwHJORg2xY4t2IQ2FxWBZup_imy9h0P84QIOdTEBHKrGkl6kccdHAMBP3a3fJikMMB3C52uAGrXg9Lj6nGlLPx3aq9FitdJaOC9XM6srHiFgjmhty8oYRCXGU508tPYcMPqyGddqmLw1zNnPBxyHyJq3xCPQjPKdH3lmm6ar5O856Tcwr2BdS-imnqtlr0vBeGok9BGhdDOTSMq2tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf4a9a059.mp4?token=chkaP-BH7-K1ujZpQqLez-0GdgczBJjHkG8NFn1qSWx2xpeLcrUG9nVBFeARvUEdJ8PO0e7h0-HwUEPdoXofnJa3kuOMExVVXduGpOhMGnMKn5UFL2oMcT0kd6ZGQxYFQ_mLdwHJORg2xY4t2IQ2FxWBZup_imy9h0P84QIOdTEBHKrGkl6kccdHAMBP3a3fJikMMB3C52uAGrXg9Lj6nGlLPx3aq9FitdJaOC9XM6srHiFgjmhty8oYRCXGU508tPYcMPqyGddqmLw1zNnPBxyHyJq3xCPQjPKdH3lmm6ar5O856Tcwr2BdS-imnqtlr0vBeGok9BGhdDOTSMq2tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهنام ابوالقاسم‌پور در لبنان: به‌عنوان نمایندهٔ ورزشکاران به دیدار خانواده‌های شهدا رفتیم و انگشتر متبرک آیت‌الله سیدمجتبی خامنه‌ای را به آن‌ها تقدیم کردیم.
🔹
تازه از نزدیک فهمیدم مردم لبنان با چه شرایطی زندگی می‌کنند و چقدر نسبت به ایرانی‌ها محبت دارند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/465742" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465741">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTw7QJTjVhpkw-1PalkIJxcAxtU36eM4O71cl2HgfPvIyu-jW7w6I_OZu5mEKJ73gbvMevW3g_vBaGZzTNvCkEHhKOIZRrVJrWJ4a3PydAUJSnpq7P5GtZrJB8oxpLRJkH-t2qcq5x4FNWtRfrw8x56R-cM3r1pSXjE3z-Tk_1cYlncuMwaYo33Kgeqj7YRRwwgk0XngUHZ6MY5NfXzpGmovrjx2KN3rMdse_RnCFy5lbZ6FEGbx-VEU6TIbJrN5eWAH2QJ03hVUyTtfC7qbeJ_Dt4srA9Ev8wsPt-YN1jy-D6CDVuAkairB5jjL2LRO5Nsg8UV9yvY7q2vARyvWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت دوباره به ۱۰۰ دلار رسید و ترامپ‌ حرف‌های تکراری‌اش را تکرار کرد
🔹
رئیس‌جمهور آمریکا: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و آنها با این موافق هستند.
🔹
بعداز اتمام جنگ با ایران قیمت نفت افت قابل توجهی خواهد کرد.
🔹
میزان نفتی که درحال حاضر از تنگۀ هرمز عبور می‌کند بیشتر از قبل‌از جنگ است.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465741" target="_blank">📅 20:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465740">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd58b284a4.mp4?token=bT7kL4KwR8ZQdnOmyfOuH6heXV8dtIsb_rmQKpwKo8GiDy3oOGsUIGnCajvD5KJcdil5iJnD4SDW4iwjt7BsS9BYwcm3AZxDbsG9JDglm_i1yRB1iTptRSqrfn4Drm4SZOo_1Cxbcy3InhjKO6fT3r0yUezQfi9EB1w7-btuHdbZcVrlc813v7Scu8k-3Y7OhAbnr-yy9Fkz9IKTT1yKjoESWDkk6mxRAYtyQIfyiNkQXIkgB117NSsvc-z8r5BWOYQSXYwVgJHqhggPubv_KY0xWOZUGV5dCk5v64EY0kDw2bqUwkkzl6TsipPYCUVomGBjKU7dQgeKLNUeL7npkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd58b284a4.mp4?token=bT7kL4KwR8ZQdnOmyfOuH6heXV8dtIsb_rmQKpwKo8GiDy3oOGsUIGnCajvD5KJcdil5iJnD4SDW4iwjt7BsS9BYwcm3AZxDbsG9JDglm_i1yRB1iTptRSqrfn4Drm4SZOo_1Cxbcy3InhjKO6fT3r0yUezQfi9EB1w7-btuHdbZcVrlc813v7Scu8k-3Y7OhAbnr-yy9Fkz9IKTT1yKjoESWDkk6mxRAYtyQIfyiNkQXIkgB117NSsvc-z8r5BWOYQSXYwVgJHqhggPubv_KY0xWOZUGV5dCk5v64EY0kDw2bqUwkkzl6TsipPYCUVomGBjKU7dQgeKLNUeL7npkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین: ما آغازگر درگیری با اوکراین نبودیم بلکه آنها درگیری را شروع کردند
🔹
ناتو نباید روس‌ستیزی را در اوکراین ترویج می‌کرد. غربی ها خود را مرکز دنیا می‌دانند.
🔹
اصل توسل به زور رویکرد بازیگران بزرگ بین‌المللی است و باید از آن جلوگیری شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465740" target="_blank">📅 20:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465739">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه ایران
🔹
آمریکا نام ۲ فرد و ۲۸ شرکت را به فهرست تحریم‌ها علیه ایران اضافه کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/465739" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465738">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b7e32e56.mp4?token=giSoGoxJbrXZAZerfdNaZLzdSTRdPgX4QAv7UIhaiJ6fmhAS7iCbGVJFQsfCVfYVRiBFBNIoee0YxEM6c2Q11DZjqYWAD3FaX77wau1lCTsaZ61ICT8qg4Lt5FZjHyD7zjSpL_1ambMhWxV9e7MEMEEgJOkisXIqr3dVYs9TyGA6FvBkYsRkYw0KyrLgYfw4J_zRAPkmH492qI6vhgrWSSZs-nrX4NKYaVhe6J8FOHFmXicG9JGtYUtVXkRieaB7o6RcvEQ4ouzhpoGrW_sn1I7_R-s2vDAqxJFdKFAiuFZmrVZc8n1XRsAR-ObkTtmzvZkCwrHROPVwqQ6gLJbJVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b7e32e56.mp4?token=giSoGoxJbrXZAZerfdNaZLzdSTRdPgX4QAv7UIhaiJ6fmhAS7iCbGVJFQsfCVfYVRiBFBNIoee0YxEM6c2Q11DZjqYWAD3FaX77wau1lCTsaZ61ICT8qg4Lt5FZjHyD7zjSpL_1ambMhWxV9e7MEMEEgJOkisXIqr3dVYs9TyGA6FvBkYsRkYw0KyrLgYfw4J_zRAPkmH492qI6vhgrWSSZs-nrX4NKYaVhe6J8FOHFmXicG9JGtYUtVXkRieaB7o6RcvEQ4ouzhpoGrW_sn1I7_R-s2vDAqxJFdKFAiuFZmrVZc8n1XRsAR-ObkTtmzvZkCwrHROPVwqQ6gLJbJVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین: ما آغازگر درگیری با اوکراین
نبودیم بلکه آنها درگیری را شروع کردند
🔹
ناتو نباید روس‌ستیزی را در اوکراین ترویج می‌کرد. غربی ها خود را مرکز دنیا می‌دانند.
🔹
اصل توسل به زور رویکرد بازیگران بزرگ بین‌المللی است و باید از آن جلوگیری شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/465738" target="_blank">📅 19:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465737">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e690d320e1.mp4?token=I77iL5DTQh_L8V_HqkGJnNVwv7QbB6X5UB8-NemE4NpHeD5Huh4Hc07PE_b4saYBbK4VEOHLrXm_BggxaTRf4wwzp2Ps2Z5fOO2SB3fzQr4T2sRrw8xzjNr6w32r7PgoxKY0OdDm96RnuK-4R6OZj-IXA9xZwgp4gUS1WE11ynknIAmRNeElXado8G2i7gMQAUa_Er7u6m-nk4ktEG8Z8wZjwCDrvD97x7AIqr6FvYrHR-kzKjgj9BIEVTKz1o5DnUMlRr0BEhdfyQc6AQ1j_Dqh6-0i1grlR03zQC0Pj2ga8nPOeMurZ1OGtmw2N-YTXmPV6rluYd_Jhckkn4p3Bn-RfDBs2f-S0kHlj88XjrRAqV_XyEYgkqC22Z0QHg6vhtXN74EGGsFZOhNBhkuu0RSPv4yHJTyHrjLg7W2-9W48FqgnoJrzMRiKIMvz1LuURXXYpDeWlMljXSSZGQ7Do0oVo-bOQvhYn0ZxgLC05ussXhrWyVquJHmt6Ka1M6Zv2NHLMOiVixHTi9i1oPE95ImB9vf8hUHGY5Y5DxKQv0FxTJF00h0LF0VPg28aKumfdoaKm0RCo7ZkK0nKDcRNcejg1Uy2Hc3d4gHCH7OK3UprqdkSnYXaPB7kDo0z7fO_MX7I82gmmBJr_lnSUbNWzbVmrVZqoKY9XKW4tcowHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e690d320e1.mp4?token=I77iL5DTQh_L8V_HqkGJnNVwv7QbB6X5UB8-NemE4NpHeD5Huh4Hc07PE_b4saYBbK4VEOHLrXm_BggxaTRf4wwzp2Ps2Z5fOO2SB3fzQr4T2sRrw8xzjNr6w32r7PgoxKY0OdDm96RnuK-4R6OZj-IXA9xZwgp4gUS1WE11ynknIAmRNeElXado8G2i7gMQAUa_Er7u6m-nk4ktEG8Z8wZjwCDrvD97x7AIqr6FvYrHR-kzKjgj9BIEVTKz1o5DnUMlRr0BEhdfyQc6AQ1j_Dqh6-0i1grlR03zQC0Pj2ga8nPOeMurZ1OGtmw2N-YTXmPV6rluYd_Jhckkn4p3Bn-RfDBs2f-S0kHlj88XjrRAqV_XyEYgkqC22Z0QHg6vhtXN74EGGsFZOhNBhkuu0RSPv4yHJTyHrjLg7W2-9W48FqgnoJrzMRiKIMvz1LuURXXYpDeWlMljXSSZGQ7Do0oVo-bOQvhYn0ZxgLC05ussXhrWyVquJHmt6Ka1M6Zv2NHLMOiVixHTi9i1oPE95ImB9vf8hUHGY5Y5DxKQv0FxTJF00h0LF0VPg28aKumfdoaKm0RCo7ZkK0nKDcRNcejg1Uy2Hc3d4gHCH7OK3UprqdkSnYXaPB7kDo0z7fO_MX7I82gmmBJr_lnSUbNWzbVmrVZqoKY9XKW4tcowHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت مأمور متخلف به‌خاطر رفتار غیرقانونی با ۲ نوجوان سنندجی
🔹
دادستان نظامی کردستان: یکی از ماموران در شهر سنندج با نوجوانی که بدون گواهینامه رانندگی می‌کرده، برخورد غیرحرفه‌ای و نامناسب داشته.
🔹
با وجود اعلام رضایت پدر دانش‌آموزان، مامور متخلف پس از طی مراحل قانونی بازداشت و به زندان معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/465737" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465735">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qt7pYnHby6TtF3AzlxenA7Xyapf43WlrY0THN3aq0rZ6pXoKAEQhSRouryBpLp2c5u4f1jt31MTPiIHNElnzdRewaRJ3utnYahUfXPphRzO3S3qEfNv4Tt8afo1yXn_hT9yC4VfwaqF3sHgpeUOVbxIskn2K8KXaY8uKnIi9SMUAoPyNIDFgskbQK8yjnKqEOatTiHJC628WsPME76lV_yjYMrHZB8Jn--bAgqc-4L_0X0ezUTZ8mZR6XRG7qg9a1BGc2Q7_GPHxufHcfSsVGBP-sOg3Pbr5ppQ6aaYQs0l5wyYD7iykbS6PVNtjm1jPQFelWdF9kQG7LvV03ea8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLlMvHVY34ncgKorAejV5_2UAPkLQd647dgp26Ul77g8pbfQBze3SgYCJn4XH-k9mhJcoaYfV7_ZyLpyIuA6fYv4-vKAHhdjGCDuVZoa3YnM25W_z97GDfba-WiEuCR8dJKJWaP-pqTXdKAIHuwpMk5PkPIXJJKAmC1wJc74OCv6wtmV3h3cQ3FLDu_TEhCJugZPtU0YkGo2FtIWwZDKnwaBh-OuJKqmNB6k6Y1v0LMJpr9H34ZUPrgR0bxxZb95U-1ZirhD-UFaHEcCiHjpYIsFEHow3dT00IN9I71EvHsMwcpCpohXbVevCV51zswLt12-iOvkoFV8U5msJL-QxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
مس ایران در بهار و تابستان | ۲
🔰
کل استخراج از ۱۸۴ میلیون تن گذشت، تولید کنسانتره مس از ۸۱۱هزار تن
🔻
کارنامه عملیاتی شرکت ملی صنایع مس ایران در نیمه نخست سال ۱۴۰۵ از رشد تولید در شاخص‌های اصلی حکایت دارد؛ به‌طوری‌که حجم کل استخراج به بیش از ۱۸۴ میلیون تن و تولید کنسانتره مس به ۸۱۱هزار و ۶۷۶ تن رسید و در چند شاخص نیز عملکرد شرکت بالاتر از برنامه مصوب ثبت شد.
🔹
بررسی عملکرد شش‌ماهه شرکت ملی صنایع مس ایران نشان می‌دهد حجم کل استخراج تا پایان شهریورماه به ۱۸۴ میلیون و ۲۵۸هزار تن رسیده است؛ رقمی که در مقایسه با ۱۷۷ میلیون و ۴۷۴هزار تن در مدت مشابه سال گذشته، رشد ۴درصدی را نشان می‌دهد.
🔹
استخراج سنگ سولفوری نیز در این مدت به ۳۵ میلیون و ۸۵۴هزار تن رسید که ۲درصد بالاتر از برنامه مصوب و ۶درصد بیشتر از رقم ۳۳ میلیون و ۷۵۳هزار تن در مدت مشابه سال گذشته است.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6TL
@mespress_ir</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465735" target="_blank">📅 19:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465734">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzGHotTjlHgciwaMD4Ad06nmhZxzaAadvAMLaPMUfyls8Ek-B2nl9VvbYJlGrz-VieSKib_dfqBveh7Lnrae9V6QldhMDt8LdPTSZDH48iuz3vFa_FXVLKCnlMsZNPs1eeAKgsCoqo1U0vHLELklVHC1_OotJNTEFEjIra8uLuFFLF36XI4IJDRTSIbX6R38UarlfUFSNcoBLR--XEq2skcfCQ87F2ZpoIK0h7BwNRM4v94q11JuZ_pQN0uf5PSMMYVki37JIUiB-c4lNeXB38NJr647fTNi9Mp92rZ_Ehtd5jXT1JxVM6O7mEx2DRKCBvh0ZhcmCQEM2Xsc0y3j6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت تسهیلات ازدواج بانک پارسیان به حدود 11 هزار و 500 عروس و داماد در نیمه نخست سال
بانک پارسیان با هدف هموارسازی مسیرآغاز زندگی مشترک برای جوانان، در نیمه نخست سال 1405، عملکرد درخشانی در حوزه حمایت از خانواده‌ها از خود نشان داد.</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/465734" target="_blank">📅 19:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465733">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/465733" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465732">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG0mGhD5Er_eiczEaZPVV9q-6fp0ylga5H0xlcqMD0fmA3WvmUE_viJTTsgGaVp-veWu0RCqVYFnZ2z7zHdRwfRC997mEn6xQDtKKvtiPYXb4BLINVEqHjpifzbEb-J_-nwgACe_TsgrP5Y6tGsiJnFee807x0tEPJRxP2VEz92mRZaOWqgbdPq1l0Bti1IeAjWLxIeUu65ebUF0Gro93tntI_LJ5Mtlfr1y-oHiLfGgDR1gs5k3LlFQyJ6ioBdT1hjvjlNPb7k7oei6UggVn9M0OEEuMyycGSC_ytU3wQOmVclmCuiUcOPIKMpo18yRfaCbX5VlW-BlUk45G3Fcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا مقداری از پول فروش نفت را به عراق تحویل داد
🔹
دولت عراق اعلام کرد یک محموله دلار نقدی روز گذشته از آمریکا به دولت بغداد تحویل داده شده است.
🔹
حیدرالعبودی، سخنگوی دولت عراق گفته این محموله در چارچوب تفاهمات موجود با آمریکا و با هدف تداوم جریان ارز خارجی و تأمین نیازهای عراق به نقدینگی ارزی وارد کشور شده است.
🔸
دریافت دلار نقدی از آمریکا بابت فروش نفت، رویدادی است که بیش از هرچیزی عدم استقلال مالی عراق را نشان می‌دهد، به‌طوری‌که آمریکا پول نفت عراق را در یک حساب در بانک فدرال رزرو نیویورک نگهداری می‌کند و اگر بخواهد، عراق توان هزینه کردن یک دلار از این پول را نیز ندارد.
🔸
ارسال محموله‌های نقدی دلار نیز به شکل منظم و همیشگی نیست و طبق سابقه، آمریکا هر زمان بخواهد می‌تواند انتقال دلار به عراق را متوقف کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/465732" target="_blank">📅 19:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465731">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa30ede670.mp4?token=lkJ_ronaArgU-LnwPARfxEbpRYpSRCUeRSOMcD4pi-hVGNxMBPBWWutsAQiSMGBkWQrMwXmH7-zFliM_1j11H5avdFV52yAGBuNPQEfnnE4BTJMQmg_QPKT_S4MqGpc2SbEoOWH5aVSCdx-06hF1dztGIb7r5Wy_skREiQbhi-3SwYY6vYIa8NMjXJyiA2hqlFZ0_nU2D4-MxrMBKZyijfFnTYF_xPv_QrgvqTX92qlqQW1negNVcNNK7v5f6rvzPqsRCSzxOYg7B5vQsVrapuCQFenBOms-c3eh0VnTQrmNaOUVvqpbf0G7IcILniIc4jPVGvuixkOE_4VCCKWzoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa30ede670.mp4?token=lkJ_ronaArgU-LnwPARfxEbpRYpSRCUeRSOMcD4pi-hVGNxMBPBWWutsAQiSMGBkWQrMwXmH7-zFliM_1j11H5avdFV52yAGBuNPQEfnnE4BTJMQmg_QPKT_S4MqGpc2SbEoOWH5aVSCdx-06hF1dztGIb7r5Wy_skREiQbhi-3SwYY6vYIa8NMjXJyiA2hqlFZ0_nU2D4-MxrMBKZyijfFnTYF_xPv_QrgvqTX92qlqQW1negNVcNNK7v5f6rvzPqsRCSzxOYg7B5vQsVrapuCQFenBOms-c3eh0VnTQrmNaOUVvqpbf0G7IcILniIc4jPVGvuixkOE_4VCCKWzoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژیلا صادقی در مزار گلزار شهدای لبنان: آنچه در جنت‌الزهرا دیده می‌شود تداعی‌کنندهٔ اتحاد و غیرت است؛ در ورودی این گلزار مشغول نصب تصویر رهبر معظم انقلاب هستند.
🔹
امیدواریم جشن پیروزی جبههٔ مقاومت را در کنار مردم لبنان برگزار کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465731" target="_blank">📅 19:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465730">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abfa3096a2.mp4?token=Gsrmou6P9qDFwe16s9jBVFPj0Z8cNZODJj8vfCfW9GpEIdvgypg6bt5P7Xa8psrYacfReL_Sn5tiM9eDIPZyG4CXhSvIK5ocuU6G7-USPcO-eY-E9Qg9r1-SQUwqYNgYMTN67ihu0262fi6MCJim_R-1KT9P0gg6pYB9coYzJEQ_mCk1yJstnZQ2EhzDYgh7k5NQwOpueiHYbXjpq8ZZxWPGKbuDrFvEY97-Z7m_RQcXaJMCuLouuis-ENwqjnxx1uGN6_plCdLfBWxu3m8xcJ4UcZYWG9zBVQGtgmyT9P4zC_bartwX7IepaMTCIyJUhLHLizkvxC1obPZtg2ITwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abfa3096a2.mp4?token=Gsrmou6P9qDFwe16s9jBVFPj0Z8cNZODJj8vfCfW9GpEIdvgypg6bt5P7Xa8psrYacfReL_Sn5tiM9eDIPZyG4CXhSvIK5ocuU6G7-USPcO-eY-E9Qg9r1-SQUwqYNgYMTN67ihu0262fi6MCJim_R-1KT9P0gg6pYB9coYzJEQ_mCk1yJstnZQ2EhzDYgh7k5NQwOpueiHYbXjpq8ZZxWPGKbuDrFvEY97-Z7m_RQcXaJMCuLouuis-ENwqjnxx1uGN6_plCdLfBWxu3m8xcJ4UcZYWG9zBVQGtgmyT9P4zC_bartwX7IepaMTCIyJUhLHLizkvxC1obPZtg2ITwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قدرت‌نمایی جان‌فدایان در اصفهان
🔹
هزاران نفر جان‌فدا عصر امروز در اصفهان به خیابان آمدند تا آمادگی خود را برای دفاع از ایران اسلامی به جهانیان اعلام کنند.  عکس: حمیدرضا نیکومرام @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/465730" target="_blank">📅 19:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465729">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ade31890.mp4?token=htCoS-xeWs8y6gJL_RDGC0UrjDiCbEcf19HL0v2B3M4XPUBrKjIl5_OWQin6cc04F_jPCWa2Z49pfGF5K-c_dJrduDuKf2XnnYd-I8pKNkq4Im0M6fHI2cnF0d5ZdiR7l8Z36Mg3tSb78ZC4EBLX9OLGcRm2V5uaPjYPWbI5CHSXnmlZOHhjT74jREbCkPm83voJHgncD7uEt9qw4KFABDhSQNF5SPMdhTtdrzyzjb5PD-SauI1t7lhsxKX5HGkKjzWs4YjA4xj8F8W4YslQVVWrrdvFVTwOG5ILRT0rUzp_hyWPOoaIB7q3MnmbaevnGT4PyJ1az1Q9K-bNbJw18g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ade31890.mp4?token=htCoS-xeWs8y6gJL_RDGC0UrjDiCbEcf19HL0v2B3M4XPUBrKjIl5_OWQin6cc04F_jPCWa2Z49pfGF5K-c_dJrduDuKf2XnnYd-I8pKNkq4Im0M6fHI2cnF0d5ZdiR7l8Z36Mg3tSb78ZC4EBLX9OLGcRm2V5uaPjYPWbI5CHSXnmlZOHhjT74jREbCkPm83voJHgncD7uEt9qw4KFABDhSQNF5SPMdhTtdrzyzjb5PD-SauI1t7lhsxKX5HGkKjzWs4YjA4xj8F8W4YslQVVWrrdvFVTwOG5ILRT0rUzp_hyWPOoaIB7q3MnmbaevnGT4PyJ1az1Q9K-bNbJw18g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در دیدار با خانواده شهید در لبنان: بدون اعلام قبلی وارد خانه این شهید شدیم؛ مادرش گفت «دیشب پسرم را خواب دیدم و امروز شما مهمان من شدید».  @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/465729" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465728">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDEdxxj2XUOm10RJE-LnMVr5WHSJeEGkaAiYDOKFS_qz098Ost4CQHAJiGj1GvLFkiFdD98ewoMdaLIsiULOBndq1H4mxI26judRLtWEiAzDNRHj6MHDi1hZoCmIxpJCkoJNTTtcaZEaK_lcj46rw-kYQcG3od2NuQx_a-hdr5dvfn7DDizwPBgE1ZkE9OZbmN3nAYNioiXhwpTToL57PYu_k0yXKADRmxmp2WqKj9ZHCc_Ge6ak2FOqaiFfcvJe9L7h8PJ1vmm-PKtx_PAskdyMCyuLs6bTONEJQyjuGe4wXpa_zY5IZF4ugKKzVwLgPhHriNy3-JNYOjsl18fOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رژۀ بزرگ الحشدالشعبی به‌مناسبت خروج ارتش آمریکا از عراق
🔹
بغداد، پایتخت عراق عصر امروز شاهد رژه بزرگ نیروهای الحشدالشعبی به‌مناسبت «روز حاکمیت» و خروج نیروهای نظامی آمریکایی از عراق بود.
🔹
در این مراسم، تصاویر و تابوت‌های نمادین شهدا بر روی خودورها حمل شد…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/465728" target="_blank">📅 18:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465727">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuNF9E8CZT2cs2GIZH0vBI-LeQyVjt8bDZr4aqK8mTWjcoYqCCxxFDiMkw_7Ynfh3JtNhv0ofq1H2nwFwHVmVe6FqIxwN6qsD3rsj6mWjsU5zqeR3MzULQdwijr8ZNHV0aAKVccGXIrAiJebw5awXFBasRnkksvVnYO_TlubGaBUSPvWhAzaUjdWwNcXBMXvr6EKnWkpVhaNBzIgGr1VHA5bn-iioM0Fjkszvf4xb9bbasSABXDcKA2PV_nk8-UldAx9h5DWLqB0jz7DvweVHvMZMWFdmVsar-g86PJXoTpihZZevgrBtGo7lcEAbHqKQBemm1H24gC-x-JZMTMuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز روس‌ها به خلیج‌فارس از آسمان ایران
🔹
شرکت هواپیمایی آئروفلوت روسیه پروازهای خود در مسیر مسکو-دبی را با عبور از ایران را از سر گرفت؛ مسیری که نخستین پرواز آن پس از توقف، امروز پنجشنبه ۹ مهرماه از آسمان ایران انجام شد.
🔹
سخنگوی سازمان هواپیمایی هم می‌گوید پروازهای روسیه به ایران و عبوری به‌طور کامل برقرار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/465727" target="_blank">📅 18:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465726">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XouldBNB7-dO2YdUObs2vybtzCi5MumWdXAKWK9qZChgjJWBrBi3gDPAM7h1E24iORDw0158IffJ2W7eoXRyoKVEDPez68Wmoo8nU-dWaAk5yY9d527JbBmWeHQP8vy0C5Xu2GBOCKRP853kApcu8k-LjWYEwqyagKNSyImSPwA93ZELUFn-kz2kg_vgjSJjnLxmRphx0vV_oOyoeLXh_ATUqIeeD6sfLuURn5Z28lYip3Y-vpzT4llJ7wqO1QpD-TCrbKiVBsfORyASDJll6t3-UzoRc4icTYBZCoupboXPz24MoiIpKyOZJq-4DgyoIZIyxabZtd81rIpvtb8XWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: جان‌فدا بزرگ‌ترین پویش دفاعی در تاریخ جنگ‌های دنیاست
🔹
رئیس سازمان بسیج: بزرگ‌ترین ارتش‌های دنیا ظرفیت و استعداد مشخصی دارند و در میدان‌های جنگ، نیروهای دشمن با فرسایش فکری، روحی و جسمی مواجه می‌شوند، اما بسیجیان جان‌فدا در مواجهه با خطرات، شاداب‌تر و سلحشورتر می‌شوند.
🔹
پویش «جان‌فدا» انعکاس جنبه‌ای از بعثت و برانگیختگی مردم ایران است و این پویش را می‌توان بزرگ‌ترین پویش دفاعی در تاریخ جنگ‌های دنیا دانست.
🔹
این حضور، حاکمیت ایران بر تنگۀ هرمز را تثبیت می‌کند و به دشمنان اعلام می‌کند تا زمانی که خواسته‌های ملت ایران تحقق پیدا نکند، تنگه بازشدنی نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/465726" target="_blank">📅 18:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465719">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HD8q5RWXFmMb4GZflNDClmnrOaFMO2AJx3wGppkMrf0XYSocT1OLGtx_Xtv6YIawJADtNB9IVNz7ouIRDqbkLN4lZJgAgQ8OCtTEeXtxFZJJ7aOrAc5cIt0Uy6XXrAikAXQoL3blOXe3f_nDhgycJrq_pEyHkD8X4h3UHajfL_SdBAnVaJIi_a922sFK5vyysS6uhJLrmOdLG6VsQTS__-QjbA3RAiDxJ1mlDehxddcbGsOD7DmoCj-ZCwfBLiU1NUsb9GTDeNi2wwpc34GMUWye1Q0bdKiT6RltboediXoK25juZv1ngvNIqPGVOqEcYQ0E0x8-fF73_-zPkGu6LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYICjclaF0z77HzUyvHp9YZSEV-MBNOFaDQCiy7tM3UWtR57vK_2wCllJEXiAXMrS21Kmv6hLYnG0_rxS5l9zfhwCQMd567sHfnbdGsRr2jq_1XQvXPAXPF4ONWwMCt7nBVW_mHS5pqeqV21uGMd9-WJTsVJbfRoa7-GVlAOI7S5q9ja1qw-GG1QNcoTAqCRbQqi_4BIC-XQ9kHnhtiW1yziY7E_OocbWec2WfZdO2q9OYfhps1ft4WOW8bHUKHJUnjmzBBYtQj46GNGCBxz0UEJuvKpFnH1TV6f8t3Lzn2WDyHOHCX5M75e5WY9mY8hkuAPOBW8StkrJi8DGwnHkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YINg-rdaDFbnC4sS2-zj1AqkiD-N0rdeM49TJhlP9iiMt87gunDaYLDG_Mnq0kNu36Unb_EMi2krOZPwe1yWAMa8_BOB4NA5sCaLwZFRMeUL2xhqYxd6RdKm2s8BqNcohYL9ATQwu6qhXKB1x5E_nsaOVGKB8aCZxvbZ7DNZwxZiagRqRFEmSsuFGs0ZsOuGuVuOgp_Rbf-3yFbeWuTi-xj--ep0WGGz_AriR42y_lCm-lJmfI9dtpu0aArXE1JP4G3E0V0Putq6VYBhrNTbsB6GVzD1LDrW3qRkIBVFC9PwsXBAQE76pzL6gtpCINwJe5Lh-2NdhgDOhA4IL9gLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_kUzuWu35ZSzdJJmuylM8oAxmnLPLN013biY4GUaEt-X4UIoa1XZL5y5uSsrIC_av2UPfoo77jnDm2fFAAeGqRyjD8g5QAM4pLsAKGTKYiHefRjcJm2az8diPq7c5vr_nAOcBkyviPgnI-10WOEM2MR5U8Jg7wJybC_RiDIXpsNZFlqiNYGPcqlWMF4CCo2cnqnPfKtuXOVOnMw1MCwGHAtdxaMErqVG_5wDEuyWsoFK7qwv9L3FG2M6N-8Usa09GMrj-phurFwerUIm9mjpg-U1oNLkLmO6_tufAyuwCmGK-EJGHw6ZufNSL15_bAlu22L3gkLm3mDvmAqhlW0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja2YujYzKaWZLRz5YxZr3QgUK26_2iWZRs1uYxs0a2S6p3Jr1-k0KaIghxKCmY6pG096_UOZWfRmvSWzL6GJia2YDTNq6SGos6LZiD2juOLA146COtfEGrLoL7E29zQw_rrl-hc3EJjPUE4FrIh85AkCQ-NJNqL4QRTzlEIwcJPUMY5B8aBITWuo5enSqC7_giEmFPiHSI238OgNzA178BaxUK3Jw2E2IOWbm2wqjbvZ6skbGlfGzBpQDysIsf4NY_dHrEZBVy0CtelvMZfZv00BO5rA9x8oejbpNppNJz1FJ2Ner4xsyLr0G_cDQifKpAvB6jvf9Gur4i-hk8t7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hbysXjwZUz9BG5yGKGWN0In9XZtq4YZ7U51Qp3y7HoQfd25uk_EK5-DjcvFGo03eBEF-dYrrUAAyoMMggRl5K3SykGIF_YjCZ8Ji0kwxwf08CgwMBQzzJPzZjgJoWuZqHjJ7TmOrUFmy527Rq2XNaMC3mhwHgSuQXLUtrs8c-dPj7v1Yt-q1YNfx4FZggoWX1IyTx1sPaLtVFElz4W8kTb5Uo6iwD70WNISMsoE_nOBP5zau8QEIQrshl8JC88ghAw6h0uzo4Cxs_KzUo4WNQsZwmTqcrRWW5s7GmL-y05CwN2l00s6NJ3fvB2GdMXjNYMbrdVcJnXscODN8OVRlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2mvfOw8L4Eo8uyWrEAK-9oQFrUzh5rMU3BZnfMGItaq-GUbPb8ZDvPJoJoeqcWW0KXwcfR_MFrgYpIz_mH0TO0xiY1Dxuz1DIvXJ78XdieowidS4KCHBQTgEJdKtZXKJfuKeCZCzbQ3GftcX_mxHNJz7l1KGVo60UDjfL-dWxtoBrpk7SVwGjIcdRYAjuwRssx4y-RQ6-N1zAsy8pfgzGYVf9mUdDY3bNTJeBHJPWB3Z5kuU_vaefy8juqqaOGlw4oVuNFapmoFk-DyjslzeQRLqpE9atEqyhqAw-frdfTzIPcxZ_yFJAY1PcF9cYLCnXPeXUHu-xL4DD3m93yaJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قدرت‌نمایی جان‌فدایان در اصفهان
🔹
هزاران نفر جان‌فدا عصر امروز در اصفهان به خیابان آمدند تا آمادگی خود را برای دفاع از ایران اسلامی به جهانیان اعلام کنند.
عکس:
حمیدرضا نیکومرام
@Farsna</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/465719" target="_blank">📅 18:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465718">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGWzWvKe9Ct41Q91byP1bHXVi1vi-mZUqpgKoTKy3tCUrdSD35j48nmGxHIpicLXFjtCHjzopFVcmK6S26In12ig6ShSaK8FKG2T3dv750mhgFVgEgIjlH0qJ-jyOhjOGkDxZHsyXSIOtT-adIngO9TPBjLpKOkynBEwnvppoOgOo7HpcG8mDO7p2H4aqrzLrENwiZbrmuhfT90AkvXQhlyvn-rWR9vZS5FSdp9nHrh1f1iIcdYWXmhVR6uYFHlUj5xP1kFGbNysn0LnMcHhxo9aPxwNL_sOCg9cirvNvazq3IR3IEFhAZ6NeIc2VOrQNuO4E9iQuIwvy6ehW4Lc0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی: تلاش می‌کنیم مبلغ کالابرگ برای اقشار کم‌درآمد ۵۰ درصد افزایش یابد
🔹
رئیس بانک‌مرکزی: در حال بررسی و تأمین منابع مورد نیاز برای اجرای این طرح هستیم تا امکان افزایش مبلغ کالابرگ برای اقشار کم‌درآمد فراهم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/465718" target="_blank">📅 18:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465717">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jde0Hg27os2ThEwB_TOvX1vSMZN8GPQE2muAZwDxU4OF7uNibMa7w5JKEDr0c-mq5ahSaYDqk_gNYnNyIuntM551NlAfk1dwLq5diGO-f-oBVjohhQtJcEeX9JkMuIAXiA3K_dyvkie06XWBCKA39JCZL4L5HbZ2i0wE4qsHkOkIgPBGmLHLI5yEvPEdoGHcgxT3ZQckQjp-Tx-EF2GXPQ9cT58AvVxZBbPZYzoVOC-9MrJjWhMxxw5l7VXC0k2XerACbI1K_7BOYlMlzULb3nLTHDcTtdJRHyTR45IIaefHEPmT3m91XtYo-bNb_hRFzD2m0XZWeHwxfb9voEBkzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار شکارچی: شهید شمخانی توانست رویکردی راهبردی در ارتقای توان بازدارندگی ایران ایجاد کند
🔹
سخنگوی ارشد نیروهای مسلح در آستانۀ روز ملی نخبگان با حضور در منزل خانوادۀ شهید شمخانی ضمن ابلاغ سلام رئیس ستادکل نیروهای مسلح گفت: بزرگ‌مردانی همچون شهید شمخانی با اخلاص و درایت، نقشی ماندگار در تاریخ دفاعی و امنیتی این سرزمین ایفا کردند.
🔹
شهید شمخانی از نخبگانی بود که توانست با مدیریت جهادی، رویکردی راهبردی در ارتقای توان بازدارندگی کشور ایجاد کند؛ همین مجاهدت‌های بی‌وقفه و موفقیت‌های راهبردی بود که خشم و کینۀ دشمنان قسم‌خورده انقلاب اسلامی را برانگیخت.
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/465717" target="_blank">📅 18:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465716">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a377b35550.mp4?token=kOWrUkQ6fNGoEskQH5sBcIBocXafiiw_roPQVGxj_zgM021jKl5D4gGjBaSYBTfLXyNbfpsV3bmmi1qI7lIi8rPhfEWWH_NmhWdx-C1EL7kdopf2Bmq3VbJdgyJnjWE7Xrg1o2JWqKTaKrBSfudFBZeMtWw9aK3ULaNoQgedcMTbGa4QI8VZBw5ryjlmTi8p-aSM8RejzGzisjn7C43hgHgNJxYReQ8IUbgdaZNwqpIb8t-IkrFeHpuc6ftDb7_YQX9QqU18AJHP00i3VRD9KF-Qv7ih46BHMhahjzI-CIBwscsgWmjvapMgYSC2NCdRyB0JeeAO0RDfCfjmOY2pqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a377b35550.mp4?token=kOWrUkQ6fNGoEskQH5sBcIBocXafiiw_roPQVGxj_zgM021jKl5D4gGjBaSYBTfLXyNbfpsV3bmmi1qI7lIi8rPhfEWWH_NmhWdx-C1EL7kdopf2Bmq3VbJdgyJnjWE7Xrg1o2JWqKTaKrBSfudFBZeMtWw9aK3ULaNoQgedcMTbGa4QI8VZBw5ryjlmTi8p-aSM8RejzGzisjn7C43hgHgNJxYReQ8IUbgdaZNwqpIb8t-IkrFeHpuc6ftDb7_YQX9QqU18AJHP00i3VRD9KF-Qv7ih46BHMhahjzI-CIBwscsgWmjvapMgYSC2NCdRyB0JeeAO0RDfCfjmOY2pqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راحله امینیان همراه هیئت ایرانی در بیروت: پس از جنگ چهل‌روزه و شهادت رهبر عزیزمان، دوباره در کنار خواهران و برادران حزب‌الله هستیم به نمایندگی از مردم ایران به دیدار خانواده‌هایی رفتیم که چندین شهید تقدیم جبهه مقاومت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/465716" target="_blank">📅 18:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465715">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai6LVKEI_wvJE5tZq8xv0MZoBfCNXlx86UM_DB9OBp21_1z8V4AAoKYHJp2-On3faY4DRDtm7A2t_vNJ1oJ0K7yRTfmY3m8HB2kLAj_G7rls1D0MdNGaRs0sUrrck7ReRddBQDb9nyQJlYVTB3q_gqLFGXeHS_vny-FYySq9JWKXbGqR10WfBYFbMBBcCgE-qWG2rHqfJg5fePaFu6BDIDihnbMxQELPY1o73bwL98Rt8eLfr2Bm72V-IPM7oTCHNX0lv6GQKuBtw2w8le9HDh0UEaYHTOMfr_RzugZVEmKxPepihfGREZ96NSalei7-Rfy7wUwv_ll21Qjx5SXWpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوء استفاده از برق شهرک صنعتی برای استخراج رمزارز
در حالی که دولت تلاش دارد برای حفظ تولید کشور برق شهرک‌های صنعتی را با اولویت تامین کند، اما متاسفانه برخی افراد سودجو در قالب شهرک‌های صنعتی اقدام به استخراج غیرقانونی رمزارز می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/465715" target="_blank">📅 17:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465714">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCw9Y3lPeTZtv4giFXdMDLr3SibYlDI3ZqV-WvV1Ztf6PNrHfx3KWiBm-SX_z5ssJvm5gCQdku2vsfIcBcZB5yGnfCVlT-8XDuu1wmAKy40Ji2pauRDa8QuZaxqta58srgyBC-b_QKAtrsYnu7i8P5KgUELCnpdlwgwgnn7R4SQ7CJnxBpdSQd-c5pT-pJ0JhL3OJU2eLZO2TOekNeu_wqbZsnk8ktYKXLqVqkx_SV3ILeQ2MOQmkpeIlnGyOB8W1zGUXyA9lD9Ha-IYF2e0GwgNEQHmDrt8yafR2VBwuRp-V5s2fcPJuhMwib0ZB_3iXWGEWYAvii6KDo7MGGCx1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/465714" target="_blank">📅 17:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465713">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/465713" target="_blank">📅 17:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465708">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sTwMmBNnyabpg-56nKOmtwHHglFNUXkSWJEyu5Xj7BQsNr9FjIR6RVMATQIoajeTg1WarZWQ55eCNnjXtChC31zLCK804Amy-SzgmEWVoQWHBwJlj08AY600btULZHz4wmrXpB5ZwOPcMOQtlKKArDTo6za0Y5vL_4PymCY6nE8LOoePFtwQnY7F0pQ2hJamZue6wrc3sz7JerJ-5WvxK7OgiphICJFgV17KyYIrFa0Ag9Ay0Ao00IMzOm83lobDKzfAn3pTCDg3nDNfYZJRGzcBbnP2ORdwpFDBSQsJq1cx3amF1trHhIbvDpmzCaUbsCP5x12EzROfHS97rLzjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/droyU9-xzO1N2oTQqtXyBwqb9uiennIzSfbfDGtMu-c9H3fZ8yddoZH0s0xHO6GLvdbQRUrF1tY39KIUoW7qhc_DNZRojzvGqFqIGMkQGarL2YAfDZJCoizijs3kSiLJkxKEVE2s5OqUE_AVNMRXx4M81PtgzhdEdDJck3zlhOo36l-5PRr_5GksKO4PBfAOwooa_4ec9QafzdhZJAZPVG4cZNq8gYXGMLwBJOLe4bPB3NFhewGo0mxcZwaNb6sG7VN3dMQ30XUZ4YYgUhK9VB0z7sZ98WId5KKktRAYefCgY6PteobT2qjMFaBnWiJPHCfdv5b8Hpgy_c1OqFFXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tchH1FYiTTLpmjIsI0Acp0IoHpnJEQYJ2aPBnIUD-gJNpXqmMB1MHISgcgXcngQx9a7JTF4z65eLDoaFwWpoYalh462Hq84BFc6D3kY8qeLSdeNYp2qpQWuax3VxXyIfiZNJ49WyT_f6B0C72i_xArr7A1CsbvaE9tc5IgvTraI1Kx1ftdBnw7WXqHVNwxMSR6eorDXLQ_0vmI09U5EcSbJOIa0Yildg-VJODrBqM1Nk7vHjIPvSPYumZFX0T4YoMLWPH3pt7b1dJRjYjfS_1BYQXFcf8DN2z1nlIftrNulhIoqKLrlQjNG5Mh5TlcIXp80DTSwlCLERfOmfMAPyhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9JGptG2ceYJrtwR7G1SbVPJxzw9mj00TiOoxQLyqyZ0fVGv_fOFO3SOXi2qBo_sBsCw-vsRp2XmA6W1Evpvxbp_1iVPLdx7SGqNzTfmvd2v7251Xe6OpLuQ3SB2uyaDs1LZFJxSEmDQ7FOEDFP9FVlaaJJ2mGxlxT48iPyN5fpIgMqXAf2Yuw5A90xpys7UQdUHUOMs-GNfr28Clme0Q4DJU0ZFvMCH6zAPFBUa9mNzqwvHpWmy1AjpvqkeczYvTuBi4KcgafcP4h4mstMICHyVXYNL5N8w_4yaq2S0XkpEg91TbASY8gEL888KfQSzif7ScslNnGRu-kTY-w4eqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad9345050.mp4?token=C00b-JcSME25WpQUTk5hbS0jzpqF2coQssMP_DePwZ0RYFz7bsfZehu8mCISEUfalG_mKqHmXyflcbWLBcsZwJAdxUISj5gIY8Y3gLhJAnF_YbJIFRmawyi4VyOFqgVsD2vqosDO98K-epZyUXgHZs3sUEB4Lg5El03zQ4mSzTRPAf_SP147_lCytbhM6848-L1fcdW_ezPJgvb0V-8wCkTj6UhCbF9UECpbjMLF3U87yGCc7WxY3-ucQPrB8VHDHuKVsHCKeAWbU5vbjmWY5eMsMcSe5MDxZgnTUvIOPfJInj9vN-gsU4Xjjl2lPruS2EywvZ0PgFRK17j5KTv_-4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad9345050.mp4?token=C00b-JcSME25WpQUTk5hbS0jzpqF2coQssMP_DePwZ0RYFz7bsfZehu8mCISEUfalG_mKqHmXyflcbWLBcsZwJAdxUISj5gIY8Y3gLhJAnF_YbJIFRmawyi4VyOFqgVsD2vqosDO98K-epZyUXgHZs3sUEB4Lg5El03zQ4mSzTRPAf_SP147_lCytbhM6848-L1fcdW_ezPJgvb0V-8wCkTj6UhCbF9UECpbjMLF3U87yGCc7WxY3-ucQPrB8VHDHuKVsHCKeAWbU5vbjmWY5eMsMcSe5MDxZgnTUvIOPfJInj9vN-gsU4Xjjl2lPruS2EywvZ0PgFRK17j5KTv_-4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رژۀ بزرگ الحشدالشعبی به‌مناسبت خروج ارتش آمریکا از عراق
🔹
بغداد، پایتخت عراق عصر امروز شاهد رژه بزرگ نیروهای الحشدالشعبی به‌مناسبت «روز حاکمیت» و خروج نیروهای نظامی آمریکایی از عراق بود.
🔹
در این مراسم، تصاویر و تابوت‌های نمادین شهدا بر روی خودورها حمل شد و از فداکاری کسانی که جان خود را در راه دفاع از عراق، سرزمین و مقدسات این کشور از دست دادند، تجلیل شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/465708" target="_blank">📅 17:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465707">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsM4BLOESOmQYuswte1AcOScJvFCQMc-Bat_gGlVNpQA66eF_E0A_P4QRAZJ7ZLQwKwJwh_IPd1-1PNW6NahsOatqhalupf8CbrwbRnUJrcAnTLeUNjC1AK6buCDe7gE-uTTKBtvD6UgDYQomIo69SLwCk02OcIVgAoDnCVLtCdgoHm9jtweSMqdu81SSWwV1g_5injpZBHD5napbGKYeE2aKRV0RectyVqPPKAF32nI0et9qMX7_KZl4pSJTepiw-sOCapv58q69zvLK2uZYk1bWpuVEO7-tSgMHB9WHvVUFxx7xXn4fwOKTu-GwiV8sWXsZmBlVFm-SyoIlm8zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: ادعای نابودی صنعت دفاعی چیزی را تغییر نمی‌دهد
🔹
توان و ابتکار عمل ایرانی را در میدان خواهید دید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/465707" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465706">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRRj1samKknU10eWg93vluyenvHDW7XtjxAL231-70_1gBSY-I0Paoph-CYV6M-UoTHBb3g0ApeVENnRtQWDlDzTzmH1PzH-fF5vPQLwq8GjBqXZzSd8KP8oowMvQ_uoaMqfsPWRjHnun-nPaPLm_UIBpTU2aPNg63E9crx3IQ45FFmbMqFhKiFShvlCiBoI_kctQCBamJHroAkbks0AVbToyXMB6IwFWPKFHk_IAlNKbZXs-KPe49hkhIGnrOdHf0dyHPUNCQ51L4hinpmDfoHbnW9w0dG_CGo1CZhFW_ym26OxGUO0zC5X18xVT8cZkAPLpDiGFhcwG4gkCLc3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوش بنزینی برای موتورسوارها
🔹
شرکت ملی پخش فرآورده‌های نفتی: به‌منظور رفع مشکلات سوخت‌گیری موتورسیکلت‌ها و کاهش حجم ترافیک در عرضۀ سوخت، استفاده از کارت اضطراری سوخت خودروهای سواری در جایگاه‌ها ممنوع است.
🔹
طبق این دستورالعمل، جایگاه‌های شهری دارای سکوی اختصاصی موتورسیکلت باید به ازای هر نازل، یک کارت سوخت اضطراری دریافت کنند.
🔹
همچنین در جایگاه‌هایی که سکوی اختصاصی موتورسیکلت ندارند، ابتدا یکی از تلمبه‌ها برای سوخت‌گیری موتورسیکلت در نظر گرفته می‌شود سپس کارت اضطراری متناسب با تعداد نازل‌ها تخصیص می‌یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/465706" target="_blank">📅 17:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465705">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اتهام انگلیسی نخست‌وزیر انگلیس به ایران
🔹
نخست‌وزیر انگلیس مدعی شده که «شواهد قوی» از نقش ایران در حادثۀ امنیتی در نزدیکی پایگاه هوایی آمریکا در انگلیس حکایت دارد.
🔸
این ادعا درحالی مطرح شده که مظنونان این حادثه با قید وثیقه آزاد شده‌اند و مقام‌های انگلیسی…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/465705" target="_blank">📅 17:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465704">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e71b1f12.mp4?token=alGzjiPSfo49dDmG0G2rUguiGpxXo1hm3KH7jaWEvsVisdEpYgKkvaFBfJmtnuCO2JV7zL2qxz2tb1WBJEP-ICNH6xsscz0PzJWXG8UxsrDhqE5-P-oBuXEg2m3GObInbEdJ5vc4F1GX13qLKXmI2Jf-aFDeDUM0z_gV6QSSfoWy4x4zXq3j_Fydwp_y4Qq_hCHZKMQbGIymE8srKq7cMYLk3MCtbdiUhq6u4XtngSNkkEuLCDmLNO79nuMdYnmpjS3fwp0vV-EjSi8xT_LjW-suLb9X3klTN1ZW6-YWnXShes57PjaIqXX2KJGrWBisiceL34pIxJl4Sk6ZRZjWZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e71b1f12.mp4?token=alGzjiPSfo49dDmG0G2rUguiGpxXo1hm3KH7jaWEvsVisdEpYgKkvaFBfJmtnuCO2JV7zL2qxz2tb1WBJEP-ICNH6xsscz0PzJWXG8UxsrDhqE5-P-oBuXEg2m3GObInbEdJ5vc4F1GX13qLKXmI2Jf-aFDeDUM0z_gV6QSSfoWy4x4zXq3j_Fydwp_y4Qq_hCHZKMQbGIymE8srKq7cMYLk3MCtbdiUhq6u4XtngSNkkEuLCDmLNO79nuMdYnmpjS3fwp0vV-EjSi8xT_LjW-suLb9X3klTN1ZW6-YWnXShes57PjaIqXX2KJGrWBisiceL34pIxJl4Sk6ZRZjWZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام پناهیان در دیدار با خانواده شهید در لبنان: بدون اعلام قبلی وارد خانه این شهید شدیم؛ مادرش گفت «دیشب پسرم را خواب دیدم و امروز شما مهمان من شدید».
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/465704" target="_blank">📅 17:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465703">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyu_YhRZye4SXSYYRQam5SC-xsJuoESzNGr2FLxj31XZyPtvbZ_70kSnsTj8XI1sMj63yfGH7k4vbFjvNC89mvMGeFUUyj3KtwJl7kosddKEByqonIf5LW1NvCRc7aA1qAH7oYWhj5vQMC7bA5fEaziq0ON5rVDxuhVkJKirKLcOlFv5w8ugWohi1YIsKVRyrkNdwo7H4OzsMTGwz8QZ9emGZ-HrxuBoOa90h-dwlC05o3lVgImpAf0uI6LGXHMUV1yhW_XyT10bgfmFoeZM0pB2TYtNUig7ksIpuMqxh0wMgTTkUd6vIMfcXiXb81alo_fQrsbB9b0v-TNRFtMn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایی که یک اختلال در آن می‌تواند گوگل را بلرزاند
🔹
تنگهٔ هرمز فقط مسیر عبور نفتکش‌ها نیست و بخش مهمی از کابل‌های ارتباطی و انتقال دادهٔ منطقه نیز از این محدوده عبور می‌کند؛ مسیری که هرگونه اختلال در آن می‌تواند ظرفیت شبکه و کیفیت اینترنت را کاهش دهد.
🔹
براساس مستندات گوگل، این شرکت در شهرهای مسقط، فجیره، دبی، دوحه و دمام ۵ نقطهٔ کلیدی دارد که بخشی از زیرساخت ارتباطی و انتقال دادهٔ گوگل در منطقه را تشکیل می‌دهند.
🔹
آسیب به کابل‌های ارتباطی هرمز می‌تواند با افزایش تأخیر اینترنت، کاهش ظرفیت شبکه و اختلال در خدمات ابری و اقتصاد دیجیتال، هزینه‌های قابل‌توجهی ایجاد کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/465703" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465700">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxeleqNYIGK8SbebSq6-9QyZLwQpgkvpWYmAV1ksamObeG9VbkzkUvTQN16Cu4qNt7RCqRItyDNHaLilcaDVA3HWnnqjHXqP3WKxyHu5zKkxI1-j7IwgrYsvphNA12A7hatQ66y679lmKqK0tA3bP0tVEvZzybXSAgEgMormdmf8mIaj_3ADJRk2cjPEUT9-HcA1CmHY4jSYvPgJGYtvDzd2ez-duAS6n0edEVFvpZorF92RNQKXDB18ip__K0U-TnYIFyT8eEN3yIYSabiZ9izmtJP6vur9trxTvjHtgFw2JMAxeaiDlyMmn3CmWFK1IJsU4YQ3Pp9todZXL9tbEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUteLjya9Zx6J6jeJBGDXJQec93SDyUkZoCGyC81_D9aCtcaeqetlMj769G1F262Ik7A0kH9aMrwjQMMm4iMqKPi3tH_QE0aJCbYEJsvm7ulxclcqRhvKUSzcRR8LUyk6yZjkSNdISGzmNn0nfZuVLR9PBQdQGECqlybqSkYJK4pMJXvWM5sPa3tpvmB8r7_PALSFnYPkapO6Xxdnu4mOh-Xu2nLqCw267uO8WcjBZMpB3rHffWAH-OWR5frCupX9auKBbamiN1Yxr8BacfBsAMhgnuHEEEnqq5pwlwU-Hkc6gTB1QRUNZFE0B3xUWj6D_0MBLHGsi_adjOb2i7UVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2OrYYmYkufRma6RSVH0s2DaTSee-S10e2y4CeM0X1rrPsw5o4dpDvsVGm07FDeUjnCbvrdeIu-Xa_u5uU4FvHACJxd2QXNOvkKmhrFGfacQZqN66wWua0ya9JhLt8cQMHfA7joTo-rvpNTkeBP0j7l4OIzm71YBPKBHQbZoDx1jn7bU4PjkJGdaXRwhGODVYn8NKo7ojrPBrf7uuiLX-_jF2rNvDwLsyhBugJ3AVmWkysLbXYDhedtuVtn3Qq1RW9tIsnT8Z86boQheYNVilg202Ckjd7UPifxpOQx7ghCLfWZAlPvs5PYVsuK38iPM1RLbRHeoGoyCc30MXUd0vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یامین‌پور از اهدای انگشتر متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به خانواده شهید حسین هاشم: دیشب را به زیارت خانواده‌های شهدا گذراندیم.‌
🔹
الماس‌های درخشان در خانه‌های کوچک در کوچه پس کوچه‌های ضاحیه...
🔹
اینجا خانه‌ی شهید حسین هاشم است‌. سه فرزندش در سکوت آمدند و دل ما را آتش زدند.
🔹
این شهید به‌خاطر اینکه در ویدئوی وصیتش مکان و کیفیت شهادتش را توضیح داده، در بین شهدای اخیر مشهور است.
🔹
با خود چفیه و انگشتر متبرک رهبر عزیز انقلاب آیت‌الله سیدمجتبی خامنه‌ای را آورده‌ایم.
🔹
هربار نام امام سید مجتبی را می‌آوریم صلوات می‌فرستند. همسر شهید یک کلمه هم حرف نزد، چفیه را روی صورتش گرفت و اشک ریخت.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/465700" target="_blank">📅 16:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tVV7XR6rs1yLsqxrMfnphVL0LTOv2j0xWT5envj3Fdpj6HxK7gM3ErkIZBAn87FvMq3n8c_y8nuFJ9Tbv_KPA0UTmPvDpTxhENbq71qyaPb_DgoXf35X4-JtWDYAcXZ2m3q3IpksZ4IjTTnHYb7OJSBttI7ZgL4Mn-4DywvvkAIik2Gzcyf2gjoNbZTHlCs64v6HKk5B7DmRrG9U5_AulDs22kHojifIgXrfAUd_duW4MFs9BQILTDftuDoFCWTyIMvzGX7mpDANMOBR5yiNH8K67E3Fv4xGrm88qpesAxu0E2XEwdF80Nlu2gMTe_DhcGBHtdBSh0ZyTKoQM9qs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KtIMXaetCfBtyjbcy8L_CI7hRiyUBungCITRI731wc35J0ZozOhIbjf7ytlA4STytlSDyhW7ZZoGcarnQu1IUssEHCyUD-ENV6NFEzevCA1AkMJaVS5hMAh8cBB6Hjfh8pxfYoODoj-7MGpts0zbKDLVmGphP83esWdv0RSjD2GMssjzheZGzqYS6tgwLh_v9GqGiDk4PvBIbYuuvAMaI0tmk54vg64fyecMrHyQtBBgG3izovBFn0GBSoAVrVz_jE8TgJ5r1X1NGAHtJcQGfdBWwVbIM8wLgk1m5E6RIzz7VXkJopwCF4QEA6zSf4mBAHyHRIgmuCrGzkc6YV-cGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MxYd_ywfSTSDypN7ve1qPEtWEpdWvysP_Z9apNd1efLlIxwMMt2zUcpz5J5fFDV2127rlhmHuRsUilM1BYyQV6Hf4cmugjWqc260HuEmYKu7F1IfyjaORGdxfChRohhbc1-GT0GE3cGbW6eIC-jTIvhzqh-PBgtm5ub7JvdfSCQAb6xWwBGDSO-MeftjV2vCphx38QcB5TNqw6qpAA_VF1cAdiziRWJ7RnDTPbRcgk1edvrD_oMvk5WVovrUncv0osXG_iht8-H-sGZnExVRWiIhxR783wokyFMyGHbmABBFh7LCYE_PJYcDAnepWqE4ho1owcUmgj_O7TLdB1MFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDx3EXnc2qhAQgXXFTCpkTOiAeNnWkoy73guUmHZiuq_82n1MJ4neZZRG2WdMPd3z698zJyv7tGQ94yPANqziPJqS1g2CT16Bb1AjIEHZ2Kxn1yp8uNLsHBsLatKO16B-a-0IMV-pT9GjnweIrceL04F7oMzBgWUTEPjAagWpSZZbIqWdI4irBmp8HNifj_HW-Cg2WM5AVOsirdoQuLYFy-zoKH4NT2h64Idv6Ushoyvk1JcOjbT5LK6OAh6kZWoTzfEDQRXB5PeeTEN-9-VjO5bDER0t1dg7qvL0fOnmRC7lbbjmql9XU3tjCa0U0bOcwYQg2cNEP2evSPoKgsS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ppXwy3I8poM2KDPcgy0jxqcUtG_4bZBNjdybueqB05HR6Uz_IP-uAGysRGsFeXKEvkeEvRrT_LOliDE3f27wqcPXEYqqZX6WFSzpY7BsTOXJaMmrtryVvmskPRjR9acSZTlx8d1qJBkRUiuZ6FI6vNqdAKWvxbFgttQlj5nxwyhVi-h8kief-na0X68Zt9y5TpxNCPbBsQUTci-Iz8iJm737ab8FxqGP60rtCurVoCxXNn9six_BkA0B91-H3xZsQctk5s8IYAIhMDrosoh8TSVT1SK7L2UBFdD97jwbyh1JTBS0nSwHc_WbC7NNplDKfR4ix6THDiA81LFBZ4Ii5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDZY5khLzN6tXhZTKmSzbvnfc0_5PZOLdkpmlCrbsOjVVa1LvgSu2-mG9txZJEeQg1f-LcdfCESi0rKWpDNY9bsTkWyR_8I082rszLXLTbEqgSJ0zTgr15NrlzdeG8-fZ2HoeEkW8W7WHhHXoK1aBuWPKMrm-4C9-izpZMd0eJVu7Ku7vs_alLrF8rtksurnQuxNE9ekT_n89HoXFquIyAM3nqfPDCQvqDv3mwdu8m6jc4pZ0DWtYzplUi9wBdlmpYqOTOHAfPv8rtMxFgyzuqJZ7E-roEod24y5TVWSqFDXeMPUoPpwgI11EYC6ZjlB2IQmJ2__8jxBbmdajjgDPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قرائتی: مهم‌ترین جلسات هم نباید نماز را به حاشیه ببرد
🔹
رئیس ستاد اقامهٔ نماز کشور در حاشیهٔ اجلاس سراسری نماز: نماز نباید صرفاً در قالب مجموعه‌ای از مطالب و معارف دینی مطرح شود؛ بلکه باید در متن زندگی انسان و مسائل روز جامعه حضور داشته باشد.
🔹
بررسی زندگی…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/465694" target="_blank">📅 16:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8093416765.mp4?token=USEQ3RLurVILBJp5VOIPh2XCJGV1YfTN4Qa34TNCnCNyr7Xrl4lBC1ARWdvIy6lrTz7EGShgZLledktno0afk-Kqei7Prcfy6KYx4obm2vag_lZOoqCTbFexk6kBsowFBca1SbnsNsfl0AmJKIhURImtgGORenWKT-uk1UmIQW2CB-YOKzxtWzsjqL4vWYwPjsDoyfgkDGB3gbqLAGFEBam6V8o0eCOKddp39_uJMrSsjmPxnfyI-N4hzhOZP-qkTNfXyWqa3kMb_sdskLOPqBiIshv4e3_R5A-i0x7CyAd3Pdxr2UxB7P4TGK2VEtzspGJ0k7C2y0PD14QUf7HZIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8093416765.mp4?token=USEQ3RLurVILBJp5VOIPh2XCJGV1YfTN4Qa34TNCnCNyr7Xrl4lBC1ARWdvIy6lrTz7EGShgZLledktno0afk-Kqei7Prcfy6KYx4obm2vag_lZOoqCTbFexk6kBsowFBca1SbnsNsfl0AmJKIhURImtgGORenWKT-uk1UmIQW2CB-YOKzxtWzsjqL4vWYwPjsDoyfgkDGB3gbqLAGFEBam6V8o0eCOKddp39_uJMrSsjmPxnfyI-N4hzhOZP-qkTNfXyWqa3kMb_sdskLOPqBiIshv4e3_R5A-i0x7CyAd3Pdxr2UxB7P4TGK2VEtzspGJ0k7C2y0PD14QUf7HZIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چه رفتاری در مترو سالمندان را آزار می‌دهد؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/465693" target="_blank">📅 16:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">۶ حملهٔ هوایی عربستان به شمال یمن
🔹
شبکهٔ المسیره از ۶ حملهٔ هوایی جنگنده‌های ارتش سعودی به مناطق مختلف استان صعده از صبح امروز تاکنون خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/465692" target="_blank">📅 16:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36647abbcd.mp4?token=tmZrEyMWgW7O1L5s4K3daCJIHMFnI54X5NLLZH6ww-6hfs-V9b6HPpKMeFHrBwzfuoZg0VuATMpDfBtDc72qugzRqtCMzMan-RkLCHQa32Bt9mEvSBIsoR98VDAOaW2BgITtsASoc4SMRiItX3NsVoVIVvQta1AsKDGJQUiw_fObneg388sS7VbBNSTza6u1s1afcEJbxDBhaNdFuqYGrCDcMUMl6ytsqLi_ZfGPb2pxvzWspvEKZdFvGoWAMSYBFnqUghGM-nCASmxUZzTtTNN8zsn5JBROFSmMBcZyzoaq25kGsg12Y2L4hn1ivu6dhPkOA-fjRTq87la3n6GpDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36647abbcd.mp4?token=tmZrEyMWgW7O1L5s4K3daCJIHMFnI54X5NLLZH6ww-6hfs-V9b6HPpKMeFHrBwzfuoZg0VuATMpDfBtDc72qugzRqtCMzMan-RkLCHQa32Bt9mEvSBIsoR98VDAOaW2BgITtsASoc4SMRiItX3NsVoVIVvQta1AsKDGJQUiw_fObneg388sS7VbBNSTza6u1s1afcEJbxDBhaNdFuqYGrCDcMUMl6ytsqLi_ZfGPb2pxvzWspvEKZdFvGoWAMSYBFnqUghGM-nCASmxUZzTtTNN8zsn5JBROFSmMBcZyzoaq25kGsg12Y2L4hn1ivu6dhPkOA-fjRTq87la3n6GpDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصفهانی‌ها در رزمایش جان‌فدا حماسه آفریدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/465691" target="_blank">📅 16:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49959e28c.mp4?token=UfS4vWn8pD-CpwfrhKZVOved1paJ8uWfEW2O08ftk5GpJdWDFswPfEGERZ3BMLPRUnCQuv7zljrKyw2t7UZXnq_72un7VroBoDzojWLhCEhJk-pr-3OyLmFX3Z39LGxPVpVfH-TL_8-qRiZvAqHq4u5EKK90rUDUSd0hcRQkHj9QrJZ-hGsS_H6dF9AjY-5KgEf-84xGms8bWP1uAgqhPwL_kDXtpBBVIMJ25QiCI83BrMuYSopDhKnvJQBkvFIW2KDYU_yJ3XBIy-z8atxv14Gmjpg5PafRKzqJFM4Ce6n_QCUVQKW4FUvRo8iyrhS11WeiuvbhYscE8rOeCOgtBnsIPN5OJiqp2wiuSNqMbzEckEP2BPl6vh33dFtWNpYRDt7FHHfeT9HqqkfFNFbgbXUDSCFjguqPH_eMxzhGV7FgUrMuYezIOR24N-ndRsrZlzNXxQuNZXkJsnllaI52hopbu0VdxNr1BkmfptnRz-9QJCnzFlUPS7xTJgIhY0mmamYCFNR0eEFqZIgLPIEjnw2JQpn8ULpohFDSx9sYQCkU8C7jR_5_Tczf1MJgFL5ur0vHmoH_QZ0DG8bfiqCQh_JJEVjNRCvUOKX_xu2lGyW9QE-H_zg6Z_NoyU6ymbaA2uVUzpZnuOBBmTCar2jwftIHrn1AD0JzK9RoHFzMy7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49959e28c.mp4?token=UfS4vWn8pD-CpwfrhKZVOved1paJ8uWfEW2O08ftk5GpJdWDFswPfEGERZ3BMLPRUnCQuv7zljrKyw2t7UZXnq_72un7VroBoDzojWLhCEhJk-pr-3OyLmFX3Z39LGxPVpVfH-TL_8-qRiZvAqHq4u5EKK90rUDUSd0hcRQkHj9QrJZ-hGsS_H6dF9AjY-5KgEf-84xGms8bWP1uAgqhPwL_kDXtpBBVIMJ25QiCI83BrMuYSopDhKnvJQBkvFIW2KDYU_yJ3XBIy-z8atxv14Gmjpg5PafRKzqJFM4Ce6n_QCUVQKW4FUvRo8iyrhS11WeiuvbhYscE8rOeCOgtBnsIPN5OJiqp2wiuSNqMbzEckEP2BPl6vh33dFtWNpYRDt7FHHfeT9HqqkfFNFbgbXUDSCFjguqPH_eMxzhGV7FgUrMuYezIOR24N-ndRsrZlzNXxQuNZXkJsnllaI52hopbu0VdxNr1BkmfptnRz-9QJCnzFlUPS7xTJgIhY0mmamYCFNR0eEFqZIgLPIEjnw2JQpn8ULpohFDSx9sYQCkU8C7jR_5_Tczf1MJgFL5ur0vHmoH_QZ0DG8bfiqCQh_JJEVjNRCvUOKX_xu2lGyW9QE-H_zg6Z_NoyU6ymbaA2uVUzpZnuOBBmTCar2jwftIHrn1AD0JzK9RoHFzMy7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ پلیس به ادعای میلی‌گلد
🔹
پلیس امنیت اقتصادی اعلام کرد نظارت بر سکوهای فروش آنلاین طلا، تکلیف قانونی این نهاد است و ادعای «کارشکنی» یا «محدودیت‌سازی» را رد کرد.
🔹
به گفته پلیس، اقدامات انجام‌شده پس از هشدارهای متعدد و در پی عدم‌تمکین میلی‌گلد به برخی مصوبات و ضوابط و در چارچوب قانون انجام شده است.
🔗
اگر شما هم جزو افرادی هستید که پول و طلایتان را از میلی‌گلد تحویل نگرفتید، برای حمایت از پویش فارس‌من
اینجا
کلیک کنید.
@Farsnews_My
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/465690" target="_blank">📅 16:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJL1LNfHkmTUgLXzwCLiMpS2bstiyqM8VVlQ2eaGZsk1MZWZusOwH7tIJcmLeeQwBxvY9-MiyVpPJxaU8TYGGRYZguFbZbwDsoIe5DLpy9W1Dlw0heORWdVvVmE8fUWqBH2ZkVmxZcntHrg2wj4fx_cmVuLe0JHVqrh55z8UEpan4JkaAs6DUgWDWt4jgEKFCiY83IqNVLiiLSXVx2JJoJ368zCLDba2Fbf0iMRfIw9LvXB_P8Q2-MP8BB6sGO69DmnpL6K1JBAcOf6u3yZCCBcJrfP1waNItgoiJ9W5j2AHkGS-IUMtEUGWICFekvBHdk3tN51yZRpkQfc4Qw9U9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا اصلاح‌طلبان قواعد مذاکره را رعایت نمی‌کنند؟
🔹
مذاکره در سیاست خارجی صرفاً به‌معنای نشستن دو طرف پشت یک میز نیست؛ مذاکره زمانی معنا پیدا می‌کند که هر طرف با اتکا به ظرفیت‌ها و اهرم‌های خود، برای گرفتن امتیاز متقابل وارد میدان شود.
🔹
با این حال، بخشی از…</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/465689" target="_blank">📅 16:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شناسایی ۵۱ صفحه و توقیف ۲۴ صفحهٔ مجازی فعال در قیمت‌گذاری کاذب ارز
🔹
قوه‌قضائیه: در طرح ضربتی برخورد با قیمت‌گذاری کاذب ارز در فضای مجازی، تاکنون ۵۱ صفحه فعال در این زمینه شناسایی و ۲۴ صفحه نیز توقیف شده است.
🔹
۱۱ نفر از گردانندگان این صفحات نیز تاکنون دستگیر شده‌اند.
🔹
در یکی از موارد شناسایی‌شده، فردی که در حوزهٔ قیمت‌گذاری کاذب ارز در فضای مجازی فعالیت داشته، دارای ۱۶ کانال تخصصی در زمینه قیمت‌گذاری بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/465688" target="_blank">📅 16:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f67b218df.mp4?token=FNE9RQNhd0Tn3UCKfRql7KvY6knK8LF6k7FSC9IKAOPoq_9uRDf0paj4Tigno_u73SF-OLEzlI-CXn6oTL3vXFBrq9yxlf3MiysBWx-nl65FLbrv-Rdx2jyfb4WzBau8vM1vj0la3jeDcmP049MEr3gDcAAtHvwW0ceNDKfms3HTpIoqOo_KE0snX8EuYg1_Qq3E5KRAuT0iuCLl6_CUyoWbL-dMUMKDQIBpwLHlRevfC9Zp6eqDLRpKBmJPkubzv8NCAfX3yk0LywmMqlC5O43PwL7gnYBsskWsTg_BiMXI-bjMCP5oOrSgxsLyQ2IyovOc5M0oHTWoN8HykGbpNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f67b218df.mp4?token=FNE9RQNhd0Tn3UCKfRql7KvY6knK8LF6k7FSC9IKAOPoq_9uRDf0paj4Tigno_u73SF-OLEzlI-CXn6oTL3vXFBrq9yxlf3MiysBWx-nl65FLbrv-Rdx2jyfb4WzBau8vM1vj0la3jeDcmP049MEr3gDcAAtHvwW0ceNDKfms3HTpIoqOo_KE0snX8EuYg1_Qq3E5KRAuT0iuCLl6_CUyoWbL-dMUMKDQIBpwLHlRevfC9Zp6eqDLRpKBmJPkubzv8NCAfX3yk0LywmMqlC5O43PwL7gnYBsskWsTg_BiMXI-bjMCP5oOrSgxsLyQ2IyovOc5M0oHTWoN8HykGbpNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهنام ابوالقاسم‌پور در منزل شهید حزب‌الله: قهرمان‌های واقعی اینجا هستند؛با وجود حضور در خط مرزی، خانواده شهید خانه و منطقه خود را ترک نکرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/465687" target="_blank">📅 16:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c459f0d9c.mp4?token=evYBhDnm_yQJfcnX7q5rN0yeFjjeiSH-zdoQnDVDCcJy5afzD43Ij0Hqws5LQCQmMKulMRTUtpvJ2qKocH3JMhXr2t-pbdcA1t9FN6VK2rnb-zDBf50Vyws6MCJCNXzhATUYh7ZQNxVcpstkRuq1SZwTwru2m6CP1HWl9PG7kS3NHSFIq4NhOFhU_2jS1UIIz6WBE_2jwgWQ5CQV5BwK74W2p1J7CYw-F5h_Nvdn2mTwe0r39fPFxpfK3INOg4cwEN-d9h9bP6jkfkg6pdOyBepUj9PhMiDMLDg8NcbFKQpgjsTE6HUuqqFK8kjyHjejuLrYuHqN3sqBJK7sx1DUtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c459f0d9c.mp4?token=evYBhDnm_yQJfcnX7q5rN0yeFjjeiSH-zdoQnDVDCcJy5afzD43Ij0Hqws5LQCQmMKulMRTUtpvJ2qKocH3JMhXr2t-pbdcA1t9FN6VK2rnb-zDBf50Vyws6MCJCNXzhATUYh7ZQNxVcpstkRuq1SZwTwru2m6CP1HWl9PG7kS3NHSFIq4NhOFhU_2jS1UIIz6WBE_2jwgWQ5CQV5BwK74W2p1J7CYw-F5h_Nvdn2mTwe0r39fPFxpfK3INOg4cwEN-d9h9bP6jkfkg6pdOyBepUj9PhMiDMLDg8NcbFKQpgjsTE6HUuqqFK8kjyHjejuLrYuHqN3sqBJK7sx1DUtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روسیه یک پل مهم کی‌یف را هدف قرار داد
🔹
خبرگزاری فرانسه: برای اولین‌بار «پل جنوبی» که شرق و غرب پایتخت اوکراین را از روی رودخانه به یکدیگر متصل می‌کند، هدف ۲ حمله پهپادی روسیه قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/465686" target="_blank">📅 16:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9cXQ76y7gK792k8Axe9H7nWqS3aIToJVXJ75BlC9KhER0MDpBMYrf7ZrU8_LE2nBDoPeebX5Hl50-DqSb7_Q2y1xjVzj-Xnd1x-kudre7BlL-5mmXsfHm_QXiMviUd-gxrmU2q_5C80F0X75UHrN38fJJ2rOWiKno_fgtYOnsb3kzSMNElxJc5JiObiPK6ieRSvVOmSIwbNl05q4Gyw1V4bUdvrzBQ4sVr0TmSWvK2LB8HHo8kyxB9wRA-0kWB9RlUzmNp2sY_cDHAY45PCbDf3_kjciDxABdJh4HN3EQKTcftsMNI_sCv98PXocuPpJ9v7YcsCREHMuf1CE5IPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات میلیون‌ها نظامی آمریکا هک شد
🔹
اطلاعات شخصی حدود ۲.۸ میلیون نیروی نظامی فعلی و نزدیک به ۳۰۰ هزار فرد فوت‌شده آمریکایی در یک حمله سایبری به سامانه اطلاعاتی پنتاگون به سرقت رفت.
🔹
هکرها از مهر ۱۴۰۴ تا تیر ۱۴۰۵ با سوءاستفاده از یک آسیب‌پذیری امنیتی، به اطلاعاتی مانند شماره تأمین اجتماعی، نام، تاریخ تولد و سوابق خدمت نظامی دسترسی داشتند.
🔹
پنتاگون اعلام کرده تاکنون نشانه‌ای از سوءاستفاده از اطلاعات سرقت‌شده پیدا نشده، اما هویت مهاجمان همچنان مشخص نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/465685" target="_blank">📅 15:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=rKvcQX9pTFBc__nHyofojd8Mvr5Emt3L1CGU9gfDPF3tTSCv4FLsy1X8-JiUXBCCNida8qTOgnDBGTEXMYLbaSeKgvHjGCEXnfOT8QTR6OPZv2qDpAbWsev_mj76yP3EFEE9sPEoAYtHWTpE34Emb3yxQpAWt0YjEsxrQSeS-AAe4MaRWx1VsM1YW-7tBy-nDYvFQJ8n5j9lLWrGTYqNYoF62GHGoRyVW6P8i7dFTG8lK6AoZ5WKmzTa-nPOt__QEQei1_lYdDU7oJ1G_hP7-Y1VoKj7QpE58yfupCsmu1_4KuIPE734r6z-IWN5xE-U7LNjjOv6JDE7Ri-Riod28E0SfJeh6X3MfBp1bVPpo8Mq5I3Ljfgd4SGShmU-3B5Qsk6lGb0qWC7JjqvaC-za6P5U9xBFiSm3ZmqD6vqAfoQ3RO3R2JgKp66UHHjnChz9gf2zUpg83fnARpgwiYyKH3kcekxi8s_Xeky3Z75RYfRgN_5lYOFM7_ZA6hBXVHt4Ji--vPicXxA30Io5iv0gPwT4ax_A_mPP1zcGJRS4FBsYhHZRFGaIzVRM3C70H74S9lXLbBDPxP-Tb8zLSdbk-LDoctHJhfI_tvKukz1uUqZ2o4Zln9sF4nwg7gPD3UwYAHxTRvTsZRTqavvNV87n-_O2NgJijnC4yMMQJkMpOt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619042ce0f.mp4?token=rKvcQX9pTFBc__nHyofojd8Mvr5Emt3L1CGU9gfDPF3tTSCv4FLsy1X8-JiUXBCCNida8qTOgnDBGTEXMYLbaSeKgvHjGCEXnfOT8QTR6OPZv2qDpAbWsev_mj76yP3EFEE9sPEoAYtHWTpE34Emb3yxQpAWt0YjEsxrQSeS-AAe4MaRWx1VsM1YW-7tBy-nDYvFQJ8n5j9lLWrGTYqNYoF62GHGoRyVW6P8i7dFTG8lK6AoZ5WKmzTa-nPOt__QEQei1_lYdDU7oJ1G_hP7-Y1VoKj7QpE58yfupCsmu1_4KuIPE734r6z-IWN5xE-U7LNjjOv6JDE7Ri-Riod28E0SfJeh6X3MfBp1bVPpo8Mq5I3Ljfgd4SGShmU-3B5Qsk6lGb0qWC7JjqvaC-za6P5U9xBFiSm3ZmqD6vqAfoQ3RO3R2JgKp66UHHjnChz9gf2zUpg83fnARpgwiYyKH3kcekxi8s_Xeky3Z75RYfRgN_5lYOFM7_ZA6hBXVHt4Ji--vPicXxA30Io5iv0gPwT4ax_A_mPP1zcGJRS4FBsYhHZRFGaIzVRM3C70H74S9lXLbBDPxP-Tb8zLSdbk-LDoctHJhfI_tvKukz1uUqZ2o4Zln9sF4nwg7gPD3UwYAHxTRvTsZRTqavvNV87n-_O2NgJijnC4yMMQJkMpOt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژیلا صادقی در لبنان: مردم بیروت عاشق وطن، مقام معظم رهبری و سید حسن نصرالله هستند و اجازه زورگویی به باورها و سرزمینشان را نمی‌دهند.
🔹
مقاومت ادامه دارد چون هنوز شهید می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/465684" target="_blank">📅 15:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8aa171770.mp4?token=RMH1Jt20QLDBVNUNCMxjyjA9D9Rl_CE2WZTtCAERbWFpI2gmkC2C39R7I73ESJW8ML2NWfBLpIEpOj1cPXWAwlPU_JorNiSLrJe8Ki2AmtvbDNyaum0DEEMnvdbYcLO85Aac3wAeSrpHzgf4qdUAYVNDCleNSmYH9u5LSyTlTH5rSJgFx8NTeJUK-93VH9vrJQx0X-2-hY71ooakRbMsHb4lUT3kWOnv67zK6IuMSxf5kz4zjJNGv2Q1q5b4EjbnXSnG0Vh1axWDRuLVc6Wk1r-NSZ3QTOmne6m8ofC32p6IYABUks6yClFISD_Ih0mi51K2s-4k8JkWpcCJ_MTxiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8aa171770.mp4?token=RMH1Jt20QLDBVNUNCMxjyjA9D9Rl_CE2WZTtCAERbWFpI2gmkC2C39R7I73ESJW8ML2NWfBLpIEpOj1cPXWAwlPU_JorNiSLrJe8Ki2AmtvbDNyaum0DEEMnvdbYcLO85Aac3wAeSrpHzgf4qdUAYVNDCleNSmYH9u5LSyTlTH5rSJgFx8NTeJUK-93VH9vrJQx0X-2-hY71ooakRbMsHb4lUT3kWOnv67zK6IuMSxf5kz4zjJNGv2Q1q5b4EjbnXSnG0Vh1axWDRuLVc6Wk1r-NSZ3QTOmne6m8ofC32p6IYABUks6yClFISD_Ih0mi51K2s-4k8JkWpcCJ_MTxiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رضا علیپور پس‌از کسب مدال نقره: سرباز مردمم و پارتی من خداست.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465683" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ca4b25d5.mp4?token=O9siD47w08NZ2fHky_89Fg0EDlUYCDstL-B9nH26zoJMqPKdxc4FSYUG33r8pxw6Rt3yTj4SsBkXn5wNbYWjY7srl3pKAc4iK4vRKhWpxHWea6OfP5ConX368Qs8GY0s5ISEHXXzewOwWb5HygLK6l9MDVx4ssFefyx4muj3Yp5YsWz5GIqbH8jhKdPMkwIi0_6QDMiODYqOK4g_Hy65tch8zwXA6aE9zVc6YRLAnBQpiUstLpI1YKKaDW1ylbq0eXcKAhCygDYT24Jbhxz0VktG6HQIxsnKASfmHxX31-_vmNsfdvKbOMrc9QLt5XpxcOGl4Ky3AtUNZvoVTVo8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ca4b25d5.mp4?token=O9siD47w08NZ2fHky_89Fg0EDlUYCDstL-B9nH26zoJMqPKdxc4FSYUG33r8pxw6Rt3yTj4SsBkXn5wNbYWjY7srl3pKAc4iK4vRKhWpxHWea6OfP5ConX368Qs8GY0s5ISEHXXzewOwWb5HygLK6l9MDVx4ssFefyx4muj3Yp5YsWz5GIqbH8jhKdPMkwIi0_6QDMiODYqOK4g_Hy65tch8zwXA6aE9zVc6YRLAnBQpiUstLpI1YKKaDW1ylbq0eXcKAhCygDYT24Jbhxz0VktG6HQIxsnKASfmHxX31-_vmNsfdvKbOMrc9QLt5XpxcOGl4Ky3AtUNZvoVTVo8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور نقره‌ای شد
🔹
رضا علیپور با ثبت زمان ۵.۳۶۲ ثانیه به مدال نقرهٔ مسابقات صخره‌نوری آسیایی ناگویا رسید. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465682" target="_blank">📅 15:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاکری: از امروز تا انتخابات آمریکا باید سطح تنش را بالا برد
🔹
مجید شاکری، اقتصاددان: تا زمان انتخابات میان دوره‌ای آمریکا یک گلدن تایم ۳۶ روزه باقی مانده است و جمهوری اسلامی باید سطح تنش را در این ۳۶ روز یا حفظ کند یا بالاتر ببرد.
🔹
تاکید می‌کنم که این افزایش…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/465681" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad297dc73.mp4?token=amzPwvI4Jsv1dAQc6ye4yfjBsbfHwhDAX3jU-7F0UjyggiGHc4-IPdpUJ4iU5SDhfEFk_bJl7SOyiXyTdrFlnAxMSsGwTVUfagCBFzV7vKLtDyZg4a5lGpNjBpLDWSdpXpn9ZKTfVURgwJvwWuRsd_JTvpT7kqRC7vS1p-3Gc5UTiGWo1XvKw4QXTHEeZb7rAeyCbz7c1M89l5Lk1LkXwrpuwWEIyPHLLAeBoUGSSPfz5GDeSBAaxehjYxJ2xxeWbA8StnsXOA3lHTivRCLItCH2DRtu1pfiUXH1dk0mAF8pPwyF7x2k5OqB0KsWPYid8C_bUgJY0LReeQoJ2tJXhB-uzKfeGqWycOqBsJu_BP7bjiPHFAhpMHZ9PYJwfJ4oXg5PLb76tknG-1msU3mafOO2rE8U7qJdlXTZyaub65qvDYM3YVXSKKc0ndqCqZb8lsV_tD-v5PPD9rDwjgIez2pKwN0Ov6_LAl2B8Ck1XCK9Byq7PWV3FV8RTzxt87RkoEp_BRtxL9CnPBYMHKa4Jwo00ktAcilkdsN_KWlNiJpJ5xoN0rJ0TdUAIuCBm1PtIKgXZxKtpsDg50DXK8iH6dzMbfKFuKW1PPvR_iQXP9XK8JYroRMTor6qBn1reIeVSjLcOyRTLU7JzcM958KZjWeGjxPdpKnLWdnFPxDVnk8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad297dc73.mp4?token=amzPwvI4Jsv1dAQc6ye4yfjBsbfHwhDAX3jU-7F0UjyggiGHc4-IPdpUJ4iU5SDhfEFk_bJl7SOyiXyTdrFlnAxMSsGwTVUfagCBFzV7vKLtDyZg4a5lGpNjBpLDWSdpXpn9ZKTfVURgwJvwWuRsd_JTvpT7kqRC7vS1p-3Gc5UTiGWo1XvKw4QXTHEeZb7rAeyCbz7c1M89l5Lk1LkXwrpuwWEIyPHLLAeBoUGSSPfz5GDeSBAaxehjYxJ2xxeWbA8StnsXOA3lHTivRCLItCH2DRtu1pfiUXH1dk0mAF8pPwyF7x2k5OqB0KsWPYid8C_bUgJY0LReeQoJ2tJXhB-uzKfeGqWycOqBsJu_BP7bjiPHFAhpMHZ9PYJwfJ4oXg5PLb76tknG-1msU3mafOO2rE8U7qJdlXTZyaub65qvDYM3YVXSKKc0ndqCqZb8lsV_tD-v5PPD9rDwjgIez2pKwN0Ov6_LAl2B8Ck1XCK9Byq7PWV3FV8RTzxt87RkoEp_BRtxL9CnPBYMHKa4Jwo00ktAcilkdsN_KWlNiJpJ5xoN0rJ0TdUAIuCBm1PtIKgXZxKtpsDg50DXK8iH6dzMbfKFuKW1PPvR_iQXP9XK8JYroRMTor6qBn1reIeVSjLcOyRTLU7JzcM958KZjWeGjxPdpKnLWdnFPxDVnk8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل در دبی زمین‌گیر شد
🔹
شرکت هواپیمایی «فلای‌دبی» امروز اعلام کرد که پروازهای رفت و برگشت به اسرائیل تا زمان تکمیل تحقیقات جاری دربارهٔ پرواز جنجالی دیروز به‌حالت تعلیق درآمده است.
🔸
روز گذشته پرواز فلای‌دبی با ۱۷۰ مسافر در مسیر دبی به تل‌آویو، پس از…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/465680" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f679fd6ff8.mp4?token=GPjdAFuWZbN81qCVjd_WU_hJ8e9ztksXEdW70ksrY4sIZQa_xXyXf60wp3kQavRLzz6lE7mS8ghNC3Qd1tA6GIpcOO18rYkGWaow7sjwqBFzaUra6bdY_RRN43uzJhk-edZIM8B7-bokxzXvXyciTIgETne01ADpEcRBMT12NgazTGQHCOshpyU-i9zo8gSGClXRQgzbi9GpAGdd6GdYtNi-IJXzNXmVIDDBjnWuKUOmGRr3IQioYlE1eTa2xvaG3IKpb0Mc1znWla7MRHsKc8SRcrD6Q58o-dgk-rEurPTOot3LU9ZD1fyfgHJcY-ECz1f_zmqXb9MuQBu11-2BcY2LF92k-oHbwhRf_g5KDVu3VF5o4kfGNPLPr_4UnbnaNoc6rXpE087CCR56XM5pZ6rEEdWR0Fq9hEm-uWAK8v8Ei7JdZwXFbbY6KzPuh_P9rwt1p8orwK2z92Fh-Jme8osyHLgWT-dXfY6bYN61TTTRQ3yXy9B9zK0uLi2TTYX0e6ylK-UZyLqUs5BH_Om13-2gVuO3wMDFz8R_6oJusfzEET46lU8MyW5bwhhM5miGUADV9Qom0XAbj9LL54mH6rOgVXjTc3eCP6uKc0ds60a288oC9lEow-mhTk2yOFbnspprm6McObdI3mziqM00RkYJzJsfYSAYxecd8DNGCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f679fd6ff8.mp4?token=GPjdAFuWZbN81qCVjd_WU_hJ8e9ztksXEdW70ksrY4sIZQa_xXyXf60wp3kQavRLzz6lE7mS8ghNC3Qd1tA6GIpcOO18rYkGWaow7sjwqBFzaUra6bdY_RRN43uzJhk-edZIM8B7-bokxzXvXyciTIgETne01ADpEcRBMT12NgazTGQHCOshpyU-i9zo8gSGClXRQgzbi9GpAGdd6GdYtNi-IJXzNXmVIDDBjnWuKUOmGRr3IQioYlE1eTa2xvaG3IKpb0Mc1znWla7MRHsKc8SRcrD6Q58o-dgk-rEurPTOot3LU9ZD1fyfgHJcY-ECz1f_zmqXb9MuQBu11-2BcY2LF92k-oHbwhRf_g5KDVu3VF5o4kfGNPLPr_4UnbnaNoc6rXpE087CCR56XM5pZ6rEEdWR0Fq9hEm-uWAK8v8Ei7JdZwXFbbY6KzPuh_P9rwt1p8orwK2z92Fh-Jme8osyHLgWT-dXfY6bYN61TTTRQ3yXy9B9zK0uLi2TTYX0e6ylK-UZyLqUs5BH_Om13-2gVuO3wMDFz8R_6oJusfzEET46lU8MyW5bwhhM5miGUADV9Qom0XAbj9LL54mH6rOgVXjTc3eCP6uKc0ds60a288oC9lEow-mhTk2yOFbnspprm6McObdI3mziqM00RkYJzJsfYSAYxecd8DNGCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور فینالیست شد
🔹
رضا علیپور در نیمه‌نهایی سنگ‌نوردی با توجه به خطای ۲ حریف خود همراه با دیگر نمایندهٔ چین به فینال صعود کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465679" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=CUPUOvHyAbl3JYYiVsSmMhrKTE5PZZnWT-qd05GMBTzdgOYoNRrB7KWmW_u4KYPlynGGc-VJ2kYRkUzTkwa0SoFiBoHs4P8X3_4E8VjkF0vD3gnStKl2nfJaT7pBaHxFnI0lAVyfw2r_SadJondt_SSAjBcscxk9MkNkPRxwxC4wojxq5z7gyO9AJNeo5RHwJRauATj4Hwmh6jKXiH4gmOl_3Li56Yv8NhvCe4pROj3Xn2AqQESSk-bUwvAkuNttcRoNh938XoF2lOop-74XeCmwblwVbe2HUBVS-3PeNtUyQgYFKilA-qp-5Qs6euiVbeIYnecRQJvwApYi8pO3azVoClpHFoi3Kn7vKAseXK0YNXbnlnl3tR9IHtlSuCvIW7rtMY1Ii9Wxai82BTUv3AxwukZvaPCaO76GW5QE6waITgHz832SQqzPvpnrFrVy6krVUd_ClRb3qKfeXpifgb6Cmu-Txf14QKfBhJiT4R96qIKrFwxCvqKNqpT5dhR_xJdxhIWsnohmF0MgiZDL5UR-QgEgrgtDOghrnmIE_T4-0QGjtKVslPLkFEFttkbTQTHOgtDq-E0wXmMExV_d-xjdrfs69EpDEa7USpyMsr3gPFryRhsIvjgCNn7N7D4toAiUvr-wK6hfCRAhSkbPYYgWjpaSzZnLCq_-0NWdqVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed9d34d24.mp4?token=CUPUOvHyAbl3JYYiVsSmMhrKTE5PZZnWT-qd05GMBTzdgOYoNRrB7KWmW_u4KYPlynGGc-VJ2kYRkUzTkwa0SoFiBoHs4P8X3_4E8VjkF0vD3gnStKl2nfJaT7pBaHxFnI0lAVyfw2r_SadJondt_SSAjBcscxk9MkNkPRxwxC4wojxq5z7gyO9AJNeo5RHwJRauATj4Hwmh6jKXiH4gmOl_3Li56Yv8NhvCe4pROj3Xn2AqQESSk-bUwvAkuNttcRoNh938XoF2lOop-74XeCmwblwVbe2HUBVS-3PeNtUyQgYFKilA-qp-5Qs6euiVbeIYnecRQJvwApYi8pO3azVoClpHFoi3Kn7vKAseXK0YNXbnlnl3tR9IHtlSuCvIW7rtMY1Ii9Wxai82BTUv3AxwukZvaPCaO76GW5QE6waITgHz832SQqzPvpnrFrVy6krVUd_ClRb3qKfeXpifgb6Cmu-Txf14QKfBhJiT4R96qIKrFwxCvqKNqpT5dhR_xJdxhIWsnohmF0MgiZDL5UR-QgEgrgtDOghrnmIE_T4-0QGjtKVslPLkFEFttkbTQTHOgtDq-E0wXmMExV_d-xjdrfs69EpDEa7USpyMsr3gPFryRhsIvjgCNn7N7D4toAiUvr-wK6hfCRAhSkbPYYgWjpaSzZnLCq_-0NWdqVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهدای چفیهٔ متبرک رهبر انقلاب آیت‌الله سید مجتبی خامنه‌ای به رزمندگان مجاهد حزب‌الله لبنان در خط مقدم نبرد با ارتش رژیم صهیونیستی در کنار رودخانه لیطانی
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/465678" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465676">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8830ec81.mp4?token=fyXSqp3r0wmKjNIfreFe0I1bV1pMwCeAIva4395hsoTsi3d-gr7F86_bxBCbcHg6yVyI0ai6uwZiJoW8j_4leh4aMHsTJj2XhHZ5l2LeD-XvF5uEJg61dqtDMxudCEikJvArqTnwHAGCv0rqAm98ETz00ZnCXTaVVeo5YKbI7pRV5HhIcySIFBJUuLSwitRIiwLpsoOHjPyIMD9bwCrkhZvaWvPlCu8_NJ_LFmn3uW4o9D488fpoEz_cFAXtKW0qtkmNjquMH-RrbWanx8lPBphXVJvckRC4FVbqPdJ7jceE4nNXVnVYtjRnesimkqKatkwU32hn2mjhaBQVoi4B2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8830ec81.mp4?token=fyXSqp3r0wmKjNIfreFe0I1bV1pMwCeAIva4395hsoTsi3d-gr7F86_bxBCbcHg6yVyI0ai6uwZiJoW8j_4leh4aMHsTJj2XhHZ5l2LeD-XvF5uEJg61dqtDMxudCEikJvArqTnwHAGCv0rqAm98ETz00ZnCXTaVVeo5YKbI7pRV5HhIcySIFBJUuLSwitRIiwLpsoOHjPyIMD9bwCrkhZvaWvPlCu8_NJ_LFmn3uW4o9D488fpoEz_cFAXtKW0qtkmNjquMH-RrbWanx8lPBphXVJvckRC4FVbqPdJ7jceE4nNXVnVYtjRnesimkqKatkwU32hn2mjhaBQVoi4B2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور به نیمه‌نهایی صخره‌نوردی صعود کرد
🔹
در ادامهٔ رقابت‌های سنگ‌نوردی رضا علیپور، در مرحلهٔ یک‌چهارم نهایی ماده سرعت مردان، با ثبت ۵.۰۴ زمان و قرار گرفتن در جایگاه دوم گروه خود موفق به صعود به مرحلهٔ نیمه‌نهایی شد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/465676" target="_blank">📅 15:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465672">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGDcWYQbbIPFUVoiiSavKxp580f_K3NAau2wCufZMT8Us_MaAoLpPB3RUTfIz-ctp47aiaaN93e-x9850qS5ky-lHrgOkZiNoKbo_wPUIcaLVBe4pSDhjMY7IhMy1uXxILtRX72IakSrkQg6V_Bs9HoKho_B4o8zondsnNVxOU3r1ttwbGDV1eoMyulrShimtW9--LomR_S2F4saOEU6tQbFQLhruVZ9PR8xy2Ua4OjjObmBNc3mp1vckoPr1rUefbeo_P6FS4pFD4t4cBjtl7mzDkLen41NnHPHKr3QFD1xYsiA2Dxmk3FnLi8eb0Y1rfvl7POCaShFjUhTUkPRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzIJpDa8H6Ub-ows0VgtcgumrQs8bUvgHuDJTnmUOW4-_5sNT-LFBZ74JRcQtWkybEzRJSlV4fejzQQwWfvFcAhfpdfbuMtHvzjTYnrh7zFKrUcSHo0zsTFOp4ngdC3xFII7ZjYTLW8_HzjOGPAka1C26Wd8HEs6VsQ2PjYtphNAnI_7YXGMZpYe1stQV_xpSVzuFqDXGtwD3rhzcyOqyXaZijB_uCDPPqAqZqOQev8_kiBFQ_z1QAl_qcg_50zlq6ZRjC6m6vPkhZssF4g_aLYWMqd0hVEPSdJuH8SyXfIOwiI0UDKIekwKpVjevXrcxD1SblUIlkdy4aHy0LAWDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXMWHRsLWWxT62rd0FuF5RWTL0aMydQVy44rzDk0Z3BRN_0WUPbWdG9Qklbj7t3WKbNf60uY5vLsiNuK2CR3gBy5qdbH6H1HwVZAF2zlNGe6OkW2CEC7_UXPHefe7vkKFbJBvg-93RBMYTZ2cz1ct31NnnqqB5Y2vIPwO9v9qEB_Sp0LkQkxj7MqH7silwvxK-ayeswJ2fwVY4pTj6CVkMliu7bS7ivl_B6JK4767DqdU0T2rbup8gbvgJ6fS_hSXC9u5_bgdjbpSklAFdqIEr1KEUxHH-C0D26xWkayQHcpBEewLpwRWGHzmyzWsBMscE5py_iIh_SNya4yXho3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ns6qg4TmNieS4TRv3wbIx4uiHj3omCgV8NodQyEbEVF-vT6xwIkbvXnnYj10kxaoc3Hd5oHeOrVgY6N39kbzZG1hcaAnc6NOEHaBc6279vh4IXRTDcW4ByQsAtM7BDzNfA6Lh0ufbBypj4KTY-Xq1STWr-JxubGLlwt2Ph1o7Mn9jYwl4p8K2uFxC7TIwLHmWoG10KZaVC22Z7dpOdcaGSXu9Ev0UGtJ44ZZvZ_q6m7R-BdZ9n_9aOckY5PI8gTsNYqcFhBX8ezhiuOlyBVJCG8m1KBjURVEqjS7-PGaHEcQlbpOZyLz25Hr0yTcOgNeZzW4HFHwTF0GkX2XvA0NJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: به‌طور جدی دنبال برطرف‌کردن موانع کسب‌و‌کارها هستیم
🔹
رئیس‌جمهور در جلسه با کارآفرینان و صاحبان فرایندهای اقتصادی: مبادا تصمیمات اقتصادی و مداخلاتی که انجام می‌شود، خارج از حد تحمل جامعه باشد، زیرا به ضرر خود عمل خواهد کرد.
🔹
به‌طور جدی به دنبال برطرف کردن تمام مسائل و مشکلات مرتبط با حوزه کسب‌وکارها هستیم.
🔹
بیشتر موانع را از میان برداشته‌ایم تا با وجود محدودیت در دریا، راه صادرات و واردات و تعاملات اقتصادی با کشورهایی همچون پاکستان، عراق، ترکمنستان و آذربایجان از مرزهای زمینی گسترش یابد.
🔹
برای آنکه در مقابل دشمنان سر خم نکنیم، همه باید دست به دست یکدیگر بدهیم و موانع را از سر راه برداریم؛ با هماهنگی و وحدت می‌توانیم دشمنان را ناامید کنیم.
🔹
سران قوا به دنبال این هستند تا مسیر فعالیت‌های اقتصادی و بهبود شرایط و معیشت مردم هموار شود؛ بنابراین از طرف سران قوا قول می‌دهم با تمام وجود موانع را در راه خدمت به جامعه برداریم.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/465672" target="_blank">📅 15:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465671">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e7deded0.mp4?token=J5dYhYLvmk4Thrh1V62g0rLon4Qd1xcrH5V9KDb3lJrS-0nikSwP42G7gQfVmiq-vlZ7QDozjAqDPffmxph17gdeeQYetlE9JsTtgfCUavaAMiHQ-lVSu-9sfkQG6fnNrQQSGT63sjbeYj4-Z4zqxKkKE4D4D49b8ADIPOymGRorLBwa8x7yxn-aXwHfGHy9J12CavJJjHBaHssXvX29ZHh7T-D1caC9jIBLY5wMIRBD7jJSjZUrTZVuSFNNqjiURjGFI-3xoS2eJu9aA_ShM52X1NMN-MMwyrMtSYri7afCzhflycvGZHQwO2mOStHSlvHNauX0sXO2iy4W4nt-3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e7deded0.mp4?token=J5dYhYLvmk4Thrh1V62g0rLon4Qd1xcrH5V9KDb3lJrS-0nikSwP42G7gQfVmiq-vlZ7QDozjAqDPffmxph17gdeeQYetlE9JsTtgfCUavaAMiHQ-lVSu-9sfkQG6fnNrQQSGT63sjbeYj4-Z4zqxKkKE4D4D49b8ADIPOymGRorLBwa8x7yxn-aXwHfGHy9J12CavJJjHBaHssXvX29ZHh7T-D1caC9jIBLY5wMIRBD7jJSjZUrTZVuSFNNqjiURjGFI-3xoS2eJu9aA_ShM52X1NMN-MMwyrMtSYri7afCzhflycvGZHQwO2mOStHSlvHNauX0sXO2iy4W4nt-3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیپور به نیمه‌نهایی
صخره‌نوردی صعود کرد
🔹
در ادامهٔ رقابت‌های سنگ‌نوردی رضا علیپور، در مرحلهٔ یک‌چهارم نهایی ماده سرعت مردان، با ثبت ۵.۰۴ زمان و قرار گرفتن در جایگاه دوم گروه خود موفق به صعود به مرحلهٔ نیمه‌نهایی شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/465671" target="_blank">📅 14:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465670">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
صحبت‌های شنیدنی حسین یکتا در خط مقدم و  نقطهٔ صفر  نبرد با رژیم صهیونیستی هنگام وضوگرفتن در رود لیتانی
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/465670" target="_blank">📅 14:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465669">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2906dbbe59.mp4?token=mfNBOLMoKnq69QzJJjXSxDtoFN-jpA4ksy_Bd25BW15rkwxVqLwaGRN1u82kBAYBASA3CEvvW1A78xtYa7lBxi8S3CKW_VdG066Q_8RYMvPScT5BIP5FjmGbpFZCuNefsboDHb8gA2fkwSOsIMKOyQRR5N7lsDVOSdXpuvORx9UlB0BNNnw4xH0oJGWcSXwClDT6PCrG0CqCsYgDBSoeAeJvEM-wOTuNSgbFGkRMdedpgQRR5stTYYx_qUYq0yCvBWY_efy2edTiQKMv4jYieTKxfE8lMwxaR7FscDxdUdmzUUXcNw8ddvPtB_hPlkWun6dZPvCqLQZYcYb_60mEi2rXSsjkkj243_9a8XvqHSb_SMsjb--ANc3e14iKMwC39vtKibLH5R5BuaKbkTuLXMsojBCrMBLSosRKhGsTDWMP59pDRt2FciA6ld7Aco4HUXZP6vLt6ObhuBrFEgC5swaUOGem73jQoyE-EsWJQThbgX-_sn7VTCUgBhn_ytLw_WwlIX7ST7SmqB8wXwaLPskf9CTBlASe1SHmJ8SFS8exGiayLDJ0Zg5J_hFlYsiZmQyP7Jrt_zKTmoXhZTeNBz8MTQ06XHs66thlf2k8nGVNh94hLV_k2VNOIIUfEpLBngrbOKaxP9qtzUTp1kYcCUZcpmNldND_dUP6jCW1__Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2906dbbe59.mp4?token=mfNBOLMoKnq69QzJJjXSxDtoFN-jpA4ksy_Bd25BW15rkwxVqLwaGRN1u82kBAYBASA3CEvvW1A78xtYa7lBxi8S3CKW_VdG066Q_8RYMvPScT5BIP5FjmGbpFZCuNefsboDHb8gA2fkwSOsIMKOyQRR5N7lsDVOSdXpuvORx9UlB0BNNnw4xH0oJGWcSXwClDT6PCrG0CqCsYgDBSoeAeJvEM-wOTuNSgbFGkRMdedpgQRR5stTYYx_qUYq0yCvBWY_efy2edTiQKMv4jYieTKxfE8lMwxaR7FscDxdUdmzUUXcNw8ddvPtB_hPlkWun6dZPvCqLQZYcYb_60mEi2rXSsjkkj243_9a8XvqHSb_SMsjb--ANc3e14iKMwC39vtKibLH5R5BuaKbkTuLXMsojBCrMBLSosRKhGsTDWMP59pDRt2FciA6ld7Aco4HUXZP6vLt6ObhuBrFEgC5swaUOGem73jQoyE-EsWJQThbgX-_sn7VTCUgBhn_ytLw_WwlIX7ST7SmqB8wXwaLPskf9CTBlASe1SHmJ8SFS8exGiayLDJ0Zg5J_hFlYsiZmQyP7Jrt_zKTmoXhZTeNBz8MTQ06XHs66thlf2k8nGVNh94hLV_k2VNOIIUfEpLBngrbOKaxP9qtzUTp1kYcCUZcpmNldND_dUP6jCW1__Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/farsna/465669" target="_blank">📅 14:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465668">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZS3E_bb6q5vI96EM2i-ckY1yVJ0CBSTeaJ4kj1mT6detJf12at6Pd5HCiwuvxjshbGTw5kOGZLa51-f5jiDLa0eSiQjQdS_ksAPVhIF9LxYnn3nbvPvWehd41EFQfy-GJTnH3f2Vbs2vOE0SKycDffLeW9lSOm1KH8kJU1Gk4mhdg7Vr8EGr_1BZWVB2A4nxUbLJjYFCH89Pffj4vKeOFTTkHmI4vg9FMwoM78nez7nmNYLRcAb-JXnEt1MXP4D8qlIw4wg6EBN1_lbSwbIhm5Vyovqz64MIawuFmpAb4Dus5MI4LgOX_E_wf8UizPVmlLDCspeI0RLqKrXehDsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف نیروی دریایی آمریکا به خودکشی ۸ ملوان در پایگاه اوکلاهما
🔹
نیروی دریایی آمریکا تأیید کرده است که در فاصله سال‌های ۲۰۲۵ تا ۲۰۲۶، هشت ملوان این نیرو در پایگاه هوایی «تینکر» در اوکلاهما سیتی خودکشی کرده‌اند؛ رخدادی که بار دیگر نگرانی‌ها درباره وضعیت سلامت روان نیروهای نظامی آمریکا و شرایط کاری و زندگی آنها را افزایش داده است.
🔹
به گزارش «میلیتری تایمز»، این هشت مورد خودکشی در واحدهای وابسته به واحد «ارتباطات راهبردی یک» نیروی دریایی آمریکا رخ داده است؛ یگانی که مسئولیت بهره‌برداری و پشتیبانی از هواپیماهای E-6B مرکوری را بر عهده دارد. این هواپیماهای بوئینگ ۷۰۷ اصلاح‌شده که گاهی «هواپیمای روز قیامت» نامیده می‌شوند، در صورت وقوع بحران اتمی برای برقراری ارتباطات امن و فراهم کردن امکان فرماندهی و کنترل نیروهای هسته‌ای آمریکا مورد استفاده قرار می‌گیرند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/465668" target="_blank">📅 14:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465667">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec8467d36.mp4?token=sQsNsP6gMYx8v4eDDXb0_zYR17KlFTkPtkaxFEtsxWhEF14F7JjVVP7sFzfOEzVe6xw9J2v_Tp1-JrvXiAAqk7dPINC0FRrb_XYVm1yPkJA7onxulOp57OnT2EDlbVV2xwgk-oQ98UhZC0Ebz5g9UhWJZO9mDSCzV0NlqZldMGz9tAbRseWMDyyjMmjaCffmnh7mR4jl6fJlsfOJSSf21X5JZb-3lCq2etN0GtRwZlPKbde3R9DntgnmCyqFF1iOyfp72xXcr8-A9F1DsMYAQxorUe0AVZ3xtS6WXLhdULOGowj_Z5EHLgY0_XoPY3wU1ccwJhqYd1YU3azpBPPt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec8467d36.mp4?token=sQsNsP6gMYx8v4eDDXb0_zYR17KlFTkPtkaxFEtsxWhEF14F7JjVVP7sFzfOEzVe6xw9J2v_Tp1-JrvXiAAqk7dPINC0FRrb_XYVm1yPkJA7onxulOp57OnT2EDlbVV2xwgk-oQ98UhZC0Ebz5g9UhWJZO9mDSCzV0NlqZldMGz9tAbRseWMDyyjMmjaCffmnh7mR4jl6fJlsfOJSSf21X5JZb-3lCq2etN0GtRwZlPKbde3R9DntgnmCyqFF1iOyfp72xXcr8-A9F1DsMYAQxorUe0AVZ3xtS6WXLhdULOGowj_Z5EHLgY0_XoPY3wU1ccwJhqYd1YU3azpBPPt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سقوط مرگبار بالگرد پزشکی در کالیفرنیا
🔹
سقوط یک بالگرد در کالیفرنیای آمریکا به کشته‌شدن ۲ نفر، انتقال ۲ نفر دیگر به بیمارستان و مفقودشدن یک نفر انجامید.
🔹
به گفتهٔ مقام‌های لس‌آنجلس این بالگرد اندکی پس از برخاستن از جزیره کاتالینا در نزدیکی لس‌آنجلس سقوط کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/465667" target="_blank">📅 14:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465666">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDtbewkIxLBTm5n-YG72m3QmiScOt17QIR65xcTdVBPB5dOJ5WtZeV887SzhRmgbvy-epOgBNBl6gY3O0UuScZ1HlMMwTrF_g7-goi-YgDcOvus0lPMR_bqu5bw5Nt76ee1Ds_BDlE76nCNmRBISW0wESRCWL059CI8zIqLthScL5wLn0G4HV38WaZHqc-R1ru6FyT9z075mCFzjNL0simgbUS2PllTmVsTS0DND1H2ftT1d4pIEAq7YbMmZBGGwcTeM5h2_qqPojg90NnKYtRZyNCzXQqjxoYx0SzwqSqn0eLXYO1PbC_hkhG948H_-iFxUe5q6QL9oSM3UUuxlVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اجتماع گستردهٔ مردم زنجان در رزمایش جان‌فدایان  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/465666" target="_blank">📅 14:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465664">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9669fdc33.mp4?token=R6JEmsTnzVSPvae2cTR217rOwSEXDanEOVVHiihT-rbGJEEnvQ7VP5c6tVzhzCr9aXELvWwQEkIwy_9tXG6bpI_iYcwT9dyD7XWRfKTRoRZXtdiEfSBh_HJkocSonZzE1RXCBsql0EzrxDXb-p7ibJlS4ak1d1WlzzHXXT8jmxTuZ3M2T5b86bba0U4vt6pTpIhAodsQvnG0hn2qgg6Mhqa1ie73qNMBGBVpQUuCozL-83GSmlxjpGoJ7x6BmyM2PsbL9hSgPC8C6FBvlwyj1xCTtB6mN5ZwGsw1jTc9h5cHS0M5fDJ8OGfWjT14EsaZydQDcbg1jvi04cWWIA6JGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9669fdc33.mp4?token=R6JEmsTnzVSPvae2cTR217rOwSEXDanEOVVHiihT-rbGJEEnvQ7VP5c6tVzhzCr9aXELvWwQEkIwy_9tXG6bpI_iYcwT9dyD7XWRfKTRoRZXtdiEfSBh_HJkocSonZzE1RXCBsql0EzrxDXb-p7ibJlS4ak1d1WlzzHXXT8jmxTuZ3M2T5b86bba0U4vt6pTpIhAodsQvnG0hn2qgg6Mhqa1ie73qNMBGBVpQUuCozL-83GSmlxjpGoJ7x6BmyM2PsbL9hSgPC8C6FBvlwyj1xCTtB6mN5ZwGsw1jTc9h5cHS0M5fDJ8OGfWjT14EsaZydQDcbg1jvi04cWWIA6JGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ کشتی‌کار ایران هم راهی رده‌بندی شد
🔹
مهدی بالی در نیمه‌نهایی وزن ۹۷ کیلوگرم کشتی فرنگی مقابل ناکازاتو، حریف ژاپنی‌اش ۵ بر چهار شکست خورد و به رده‌بندی رفت. @Farsna</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/465664" target="_blank">📅 14:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465663">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL-1Ik8oDlNCo7iuvMXdrEVv-ijWbnY7T_c5pqnQhi_boP2-f9jREM9DvWtlnKuPIQq2wuc3mudaP2uoixRqrsCF43hdXOAS9DE1dnvDXqpdh73pOYCaI1tTjXjy7O10WBQfkju66tLU26vwoGRA35xC3mub-jJLbGtnf03K0jSZj2oS_0bqtZKbzrPkJPl7M00q2UH2hyVXPfNl2ALkX3U-mJQFjCG2jBm6op9y9jldcwvI708O4P9_SMYzbSQT7n2OLbdWM3UoAOIMA7rIW9oFvFzmK6HVwafMx1Smq61jwk0RHiPFasTgstZrkraBpGxSoiEOm39tfNBE-rDXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قاطع تهران به بغداد: برای صیانت از روابط تاریخی فوراً اقدام کنید
🔹
در حالی که آمریکا تلاش می‌کند با اهرم تحریم، روابط راهبردی تهران-بغداد را  محدود کند، سفارت ایران در بغداد با رویکردی قاطعانه از دولت عراق خواست با اتخاذ یک تصمیم فوری، از روابط دو کشور در برابر پیامدهای این تحریم‌ها صیانت کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/465663" target="_blank">📅 14:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465662">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb78d8f11f.mp4?token=ZN-VbZu3lVKWwHZEaMt9SGImrdXW4f5pq3NXTUMd8IOxBBBq57XaBLLouMv2IzmGYtboFw8u1RBpx1zNwBhXoiRmOdLlSEpl6riH81sBEzUZXtUo0X-BN69mX4eV5nxf-ZW7a-0qIZoP6DRR-mt5j3JRRNp7zkVVEOS8y3NsXs6TcwpXNYnlLsnxdqQIcAxOXN0dsedF7iIKqZr7p9DDx0-bjResePO_vf_Xu46UCx2gwLreEKV4eZtwbiPn6tkBkPjYP3HQ_sCSFrlmCrmhWZDSldc7Kw6jmv8CQNkDM-wfuJdAkl4HfmfoR_9THwx0jBRU77LZYkxRhH4sVdngYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb78d8f11f.mp4?token=ZN-VbZu3lVKWwHZEaMt9SGImrdXW4f5pq3NXTUMd8IOxBBBq57XaBLLouMv2IzmGYtboFw8u1RBpx1zNwBhXoiRmOdLlSEpl6riH81sBEzUZXtUo0X-BN69mX4eV5nxf-ZW7a-0qIZoP6DRR-mt5j3JRRNp7zkVVEOS8y3NsXs6TcwpXNYnlLsnxdqQIcAxOXN0dsedF7iIKqZr7p9DDx0-bjResePO_vf_Xu46UCx2gwLreEKV4eZtwbiPn6tkBkPjYP3HQ_sCSFrlmCrmhWZDSldc7Kw6jmv8CQNkDM-wfuJdAkl4HfmfoR_9THwx0jBRU77LZYkxRhH4sVdngYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هلاکت ۶ نفر از اعضای گروهک تروریستی در زاهدان
🔹
قرارگاه قدس نیروی زمینی سپاه: ۶ نفر از اعضای گروهک تروریستی تکفیری به هلاکت رسیدند و تعدادی هم بسته‌های انفجاری از آنها کشف شد. @Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/465662" target="_blank">📅 14:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465661">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de848d651.mp4?token=KOlwfJlZtcFLHx1XiTrMkwB2ohDtNKRCKqgZUp8uThANQ_c9k8xuwDq1g8_HPRhWTqgG1d0LBgiJZpLvAPyy3zriJHdnsN5ybPFwSncev8YMq1UWrvgArrylGtKQBS-f6Q2VS-jyShoYTT10YRCkt4sxxAdGDJkVBfkqVRTfnwTiRskzxpPqUYISIlM8NMJ-Au0LRYvGJKLyBUjoXIP8L9P2OPVgX8501Ajd_xlQ-auaYYBQcFTI7imS3khqU_rBEvRTUqfKlzqiykxyf3XFZ1S_qzp2c5faGRERrl2SJal9EVn42M9TWX0vNiKkbCP0fxC5JTpqIi8BKO1eUDpeICutIs7lwiNLN15Rk-ZyYD6LM4UyV6-es54wYK5rKn_R4yqFQOdBj5Rf-rcC1qKWMEeT5QJdUG4XbwjKx8PHjv5WKG9KkZEA_bBtiErKMSuyfjVFmYrRGeac2bYSmpuQJV6D9wZG9r3poYNyx6GidUKhLLMwTf5zi2W7d_mK8qEauR4M_2ziAC0ruLofqCXi5YBrFrQowTgP3yilI5x_MkoTwBBG3KE0CkaEz5rZr9PMC6hszrOW18rcbUexlzaURCHsqB_QkM3Lzs3ONT2C1qSyPRWTI1rsYjcILcdsCNn-6ywp_7MkBtV4ct9j9cV-P94gRoABRr4U8fi2gurwo2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de848d651.mp4?token=KOlwfJlZtcFLHx1XiTrMkwB2ohDtNKRCKqgZUp8uThANQ_c9k8xuwDq1g8_HPRhWTqgG1d0LBgiJZpLvAPyy3zriJHdnsN5ybPFwSncev8YMq1UWrvgArrylGtKQBS-f6Q2VS-jyShoYTT10YRCkt4sxxAdGDJkVBfkqVRTfnwTiRskzxpPqUYISIlM8NMJ-Au0LRYvGJKLyBUjoXIP8L9P2OPVgX8501Ajd_xlQ-auaYYBQcFTI7imS3khqU_rBEvRTUqfKlzqiykxyf3XFZ1S_qzp2c5faGRERrl2SJal9EVn42M9TWX0vNiKkbCP0fxC5JTpqIi8BKO1eUDpeICutIs7lwiNLN15Rk-ZyYD6LM4UyV6-es54wYK5rKn_R4yqFQOdBj5Rf-rcC1qKWMEeT5QJdUG4XbwjKx8PHjv5WKG9KkZEA_bBtiErKMSuyfjVFmYrRGeac2bYSmpuQJV6D9wZG9r3poYNyx6GidUKhLLMwTf5zi2W7d_mK8qEauR4M_2ziAC0ruLofqCXi5YBrFrQowTgP3yilI5x_MkoTwBBG3KE0CkaEz5rZr9PMC6hszrOW18rcbUexlzaURCHsqB_QkM3Lzs3ONT2C1qSyPRWTI1rsYjcILcdsCNn-6ywp_7MkBtV4ct9j9cV-P94gRoABRr4U8fi2gurwo2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار بلالی: هر چقدر لازم باشد موشک می‌زنیم تا دشمن ادب شود
🔹
مشاور فرمانده نیروی هوافضای سپاه: نرخ شلیک موشک‌های ایران به‌گونه‌ای است که حتی در صورت تداوم رویارویی برای چندین سال، امکان ادامۀ عملیات با همین نرخ وجود دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/465661" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465660">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d49320b4a.mp4?token=d7Rp1m5WaPL8prqb34zsg-qOy4gyLETIWqmXHOWAfeS-MhLMUoMpYNy2GKHV9bQSxbxM_t-6t8jdwxMQ_FhFiD6qWHNUSQJQnDKakrP8p88HO0_I759XBtKV_h5QNqIVoC9b9rgqxCrY_zwKcrUFGIuA5FgsMg9Zr_GLXxkuTTnHjIazcUnxzCdWxUpBALd-wwE4_7GPDzrxutrTMwmRu_HHM4PPwfpot6-W9pSokTZ4XSZd7JOkOFqYUcsji4hMGO1VOYWk-AilK-6zX5tpXhziWBDHkXec-muap4fPCdBrheF4JV5yV7Gs8FovfJGBfTKYkqa_QqBU8D_3Lf28dR3TNY-hyVqy14J9WBok-D22PmG2EPvWN_4G7YOXW1BTzjuqA8vCtTqq2MYyvyesxymdhihUB8os2pTROUA559Db9I92rpjd0VxPxiANnrtnDsP2eKEB9wFr_XmfepaXiBIXmKdZyKmFJecJLI9jQKJuFzE0DYTCVbxl6jcFkrFkfaPNkugxKrM3-eBZR3eHPAc_hChr9KBsIVCAh_srQ66diqFI8Jb9-k0SL_bKkL3wxOM8DAbMBOSNDDuRzCnPqSJkRZ5q7rbBkGbUduWxDLCa0CjmRaYn-qbt72LJyIneiQbQ3AW3ki_WJJX0vPrTbUd-m1KTf0_kyRWNYytd4QM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d49320b4a.mp4?token=d7Rp1m5WaPL8prqb34zsg-qOy4gyLETIWqmXHOWAfeS-MhLMUoMpYNy2GKHV9bQSxbxM_t-6t8jdwxMQ_FhFiD6qWHNUSQJQnDKakrP8p88HO0_I759XBtKV_h5QNqIVoC9b9rgqxCrY_zwKcrUFGIuA5FgsMg9Zr_GLXxkuTTnHjIazcUnxzCdWxUpBALd-wwE4_7GPDzrxutrTMwmRu_HHM4PPwfpot6-W9pSokTZ4XSZd7JOkOFqYUcsji4hMGO1VOYWk-AilK-6zX5tpXhziWBDHkXec-muap4fPCdBrheF4JV5yV7Gs8FovfJGBfTKYkqa_QqBU8D_3Lf28dR3TNY-hyVqy14J9WBok-D22PmG2EPvWN_4G7YOXW1BTzjuqA8vCtTqq2MYyvyesxymdhihUB8os2pTROUA559Db9I92rpjd0VxPxiANnrtnDsP2eKEB9wFr_XmfepaXiBIXmKdZyKmFJecJLI9jQKJuFzE0DYTCVbxl6jcFkrFkfaPNkugxKrM3-eBZR3eHPAc_hChr9KBsIVCAh_srQ66diqFI8Jb9-k0SL_bKkL3wxOM8DAbMBOSNDDuRzCnPqSJkRZ5q7rbBkGbUduWxDLCa0CjmRaYn-qbt72LJyIneiQbQ3AW3ki_WJJX0vPrTbUd-m1KTf0_kyRWNYytd4QM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقدامات قطعی دشمن در روزها و ماه‌های آینده!
این ۳ دقیقه به اندازه ساعت‌ها دوره عملیات روانی و سواد رسانه ارزش دیدن دارد
@Fars_plus</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/465660" target="_blank">📅 13:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465659">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI1odwbmaWuYzahdVz1C3QEnAoMZCMvYSMIJLcr0e_TaNZqvnt2gIbuQfsybjBko1-lDjLTriMjmKWXwQ6UoAl2fhVTBMgw7gz_rLDIdOMPTU9YKDyQmc1jNTSY_Ps6jIPyNISg25lLb6ZZxJ6e1nPUg_0JD3ujxXuMuOD2-ntHvazOHF1J5_uyAl6p5HwPwLTJf0uMY4qPhyl0Cmb0RGzoFDqlK4XQ0wxUIq7YzuIAGY4dCMBMpxa6WfpbqTvEcPm70SRpdB0SzsGz4n3arG8OKtGTWc2xv7Gz-dq_v81JBubZ5zPMl8jmYLqLUeEtvRdDLNvFF04dq2BlxsxUi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عبدولی طلای آسیا را صید کرد
🔹
علیرضا عبدولی در یک کشتی حساس در دیدار نهایی وزن ۷۷ کیلوگرم بازی‌های آسیایی ناگویا، با پیروزی ۵ بر ۳ مقابل قهرمان المپیک از ژاپن، مدال طلای مسابقات آسیایی را شکار کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465659" target="_blank">📅 13:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465658">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b271ab9f73.mp4?token=PUZmqd0TbXADQoGiFQySkoMQuTPTkIKOWlvoTiCnJFJuzqHLB7xu6i8SIslfol1DtODeU_-ixu4Gs9S4g-obtV69Nd4CENBoKJSMLJ1g5Vz1wKtUYwOP-ZGSI997--8WY8ubppLQnjd_BxgseF5ENypjzOeBSMulhcS2V9HZdWgfiDPUEowAUZ2s7xwbkgRzhnZDiBamTNzU78v8zLCQQMN0f4wSh4ZgwtuF4lYe1LNSzxXY9VCcJc7RWcgJRMOEjuTN2BNSs4APffgpk-vFDtO-4ILPkieCTHPayUjDyt1g9E-F5aZHjN3wFdWi2Hbns9e7KC6E33gxVGcbkgvY2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b271ab9f73.mp4?token=PUZmqd0TbXADQoGiFQySkoMQuTPTkIKOWlvoTiCnJFJuzqHLB7xu6i8SIslfol1DtODeU_-ixu4Gs9S4g-obtV69Nd4CENBoKJSMLJ1g5Vz1wKtUYwOP-ZGSI997--8WY8ubppLQnjd_BxgseF5ENypjzOeBSMulhcS2V9HZdWgfiDPUEowAUZ2s7xwbkgRzhnZDiBamTNzU78v8zLCQQMN0f4wSh4ZgwtuF4lYe1LNSzxXY9VCcJc7RWcgJRMOEjuTN2BNSs4APffgpk-vFDtO-4ILPkieCTHPayUjDyt1g9E-F5aZHjN3wFdWi2Hbns9e7KC6E33gxVGcbkgvY2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ عبدولی همشهری‌اش را برد و فینالیست شد
🔹
علیرضا عبدولی در نیمه‌نهایی وزن ۷۷ کیلوگرم کشتی فرنگی بداغی، کشتی‌گیر ایرانی‌الاصل قطر را شکست داد و راهی فینال شد. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/465658" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-465657">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOPuubrnGJSzNY8QWchdcC1U0vxwGdoNWkdMMvcvtO3a4lfkFp-4ni-HnJnOO3lBSW99J6b_UGT-8jMRdUfqoYjP8ad5yCAyhiZLmRI-EgHl9UG8aUPAO_TXKMRjZ9mxXgQqjdNtOYCmdypeXAQf71xRU58-r02Q6bGCa_6x9QZsJa_rUEWbBJu8O23nEc8J37uo3JhQmDitotiQPiER9p6TbQumilRdZfXYE5BZz1tHhpqFuInJTWJJ0oBn0sFOu6Sk5PazG8FLNINF75loTRZ1RRBy1j6iyVQwRnDSfB34NRh_fmWPZHL2bjR1VUPS4c8RlufaXqo5LD9tBN7QOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام ۷۸۰ باند قاچاق موادمخدر و کشف ۲۵۰ تن مخدر در کشور
🔹
رئیس پلیس مبارزه با موادمخدر فراجا: در ۶ ماهٔ نخست امسال بیش از ۲۵۰ تن انواع موادمخدر کشف شد.
🔹
در این مدت بیش‌از ۷ هزار قاچاقچی و توزیع‌کنندهٔ عمده دستگیر و بیش‌از ۷۸۰ باند فعال موادمخدر منهدم شده است.
🔹
همچنین حدود ۸ هزار خودروی مرتبط با قاچاق موادمخدر توقیف و بیش‌از ۳۳۰ سلاح غیرمجاز کشف شد.
🔹
۱۹۶ عنصر اصلی قاچاق موادمخدر در فضای مجازی نیز دستگیر و بیش‌از ۴۶۰ کیلوگرم موادمخدر از این افراد ضبط شد.
🔹
در یکی از عملیات‌های مهم، یک باند قاچاق شیشه که از شرق کشور به‌سمت مرکز و غرب فعالیت می‌کرد، منهدم و ۱۱ عضو آن دستگیر شدند. در این عملیات بیش از یک تُن شیشه و حدود ۸۰۰ کیلوگرم تریاک کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/465657" target="_blank">📅 13:40 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
