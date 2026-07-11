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
<img src="https://cdn4.telesco.pe/file/tqyPWGgS29dBqWB_cTpsyJeCKGnSmYnqJUY7dm68an3Yvw_gsguum4DbR6seRAcB7lMzB-eAiRQU7PgmyKfPLjo4oExLBH5KPKsFFCmhc-L1PK4-8O99kf4dxtHeTbaM7Px9FJ-RgjybB_7Et_oJsNmzGVaZqhhGn3qLpVWeFjGqfSn4rRTnDy9g_n25Hv1_xI5U_MNWrEnps7wo7QVEyBOu8-jOS6VzKhDpb2zgyKrqmHIksFyJ_1DAnqyYOSMpXPmmVe9GRW1yzbFppZS0nosustvNTnqRLNKJ7aUy0rwaLkZ2fyHWOFcwI_Ju4Lwoa-Bzc862PgU6vuVpPPmQUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 182K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 03:14:36</div>
<hr>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=hbze7NT9gZ2jNZPs2qgbFQazIUgPghANlrbYxPUewXWh-JSscbwvpyMSEbL7o6ym5ZpaatLY3APv_SW9h__tRJ1ijl0CSZGK7xYLtW5hqKKatq20NXvWO1rOWW9XQuWjMpbcTdLzHlIoXnjq60QI-QNKu5hG7bUghN0N9jg_A23kZUSZPfX8DezhrW9KV0U6b5Nn2buccJz_hVUpU3DEu5W3-NM5JGlrLuNuhsVEglm1PhFzVt0-56fgFrkMa1BW0QyPT_Kh1X7GA5SbtJrrJMkqjzTXq3Gxaq5X8Zb1BNMkLZe7LJHrU6sUchx0jNkFtLPupDE119Qw08TVbMauww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=hbze7NT9gZ2jNZPs2qgbFQazIUgPghANlrbYxPUewXWh-JSscbwvpyMSEbL7o6ym5ZpaatLY3APv_SW9h__tRJ1ijl0CSZGK7xYLtW5hqKKatq20NXvWO1rOWW9XQuWjMpbcTdLzHlIoXnjq60QI-QNKu5hG7bUghN0N9jg_A23kZUSZPfX8DezhrW9KV0U6b5Nn2buccJz_hVUpU3DEu5W3-NM5JGlrLuNuhsVEglm1PhFzVt0-56fgFrkMa1BW0QyPT_Kh1X7GA5SbtJrrJMkqjzTXq3Gxaq5X8Zb1BNMkLZe7LJHrU6sUchx0jNkFtLPupDE119Qw08TVbMauww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=oX53L49BjNkuJXYCIDaRuFekIRZCFKe5dyuJUCXzKJ-bgTkffRBXocdQpHNPX3lQ1jWiIfKKF0uneUqkioA7cnnUEaB_T6Ymo7Ki_qilPYsOvqYhFnRb4hWD8b47IFrJC5vN8SWqQpvO6G0guFwuh5-1oEQeGcpV7N0TEjSnCm-0sqm7q2k6zXxvOsX2wK1xFiK0t3zTZJD_g3_XQdqcDh67i5TB0hf9Tyn12chlCziwLisBKNH4BI6_ntpVwJAzqtRTfhVJvO0e4X77yzY1tFS3sA7LFd4Wj-53T6r-JWukKQiE_K-hBZVfH9EOlSM5X3MaRyioGXrXCkrD9smbI0WWS0ejOjQH0OxaxjN2sD556wNc7XIlyjKXe9p8Kn2S1ndTFBYs6fgW8yKwbb4x6u52z78eZQNtxkgkqDxubL3HgIkacLPSOmV1H_YmROKFbi4x60olk1fFP_bsIEndBWbjTRtbKVYR0SEDNWY8WuE6Zr_HdX8YrOuvruf_y_LIa8jP02JGU2D1K2DPCwPb8UgLDZ7YqLgS5iFpViIsvWoheoVUsQfuOe5oTXZYuQ1jTbcpBiEdGcXGdqilOVOJ40fSD87S9xBys5847Uy0vM_pMtoewO7vOCBFxnCfjKB8b8EXEsbOJfhZJw5yYWV6PsmMnXgmyDN2nGM4u1caLgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=oX53L49BjNkuJXYCIDaRuFekIRZCFKe5dyuJUCXzKJ-bgTkffRBXocdQpHNPX3lQ1jWiIfKKF0uneUqkioA7cnnUEaB_T6Ymo7Ki_qilPYsOvqYhFnRb4hWD8b47IFrJC5vN8SWqQpvO6G0guFwuh5-1oEQeGcpV7N0TEjSnCm-0sqm7q2k6zXxvOsX2wK1xFiK0t3zTZJD_g3_XQdqcDh67i5TB0hf9Tyn12chlCziwLisBKNH4BI6_ntpVwJAzqtRTfhVJvO0e4X77yzY1tFS3sA7LFd4Wj-53T6r-JWukKQiE_K-hBZVfH9EOlSM5X3MaRyioGXrXCkrD9smbI0WWS0ejOjQH0OxaxjN2sD556wNc7XIlyjKXe9p8Kn2S1ndTFBYs6fgW8yKwbb4x6u52z78eZQNtxkgkqDxubL3HgIkacLPSOmV1H_YmROKFbi4x60olk1fFP_bsIEndBWbjTRtbKVYR0SEDNWY8WuE6Zr_HdX8YrOuvruf_y_LIa8jP02JGU2D1K2DPCwPb8UgLDZ7YqLgS5iFpViIsvWoheoVUsQfuOe5oTXZYuQ1jTbcpBiEdGcXGdqilOVOJ40fSD87S9xBys5847Uy0vM_pMtoewO7vOCBFxnCfjKB8b8EXEsbOJfhZJw5yYWV6PsmMnXgmyDN2nGM4u1caLgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEi6iznbuXtLo36aVp-Pdhu7bkCIaxgAE4F8ehAnV474LwQ_DR62V3ZF55d13nsWY5rWc-vuM1n8SOnUHYTYdyk3Tnuxt-x2H-yXwrPS42-Al4sC8dmiZvYT2DpWH6pmkoX0I7o5dahgirYVVpJGsB0GHJS7oEo1ora-faqI8TvttYLs3TdVjfIXEiZjP7RwnyES5-th4_XajW89tj9b5lwwAfNRK-z-OMlowjVgW3yEY8u92gREN9U4TfhbH1EhXjwoP5gtsuHytKbXMRODucKEHqkzsbBcjAl87TIQDkA3-YDBiBQZAwV5wlL1GEkgWJZln7PBzCII4q7P2WpsRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=LLQkp6rvU9hM8PhAW5SYegRFFh4vA7Ovpl_bu23DjHxzbhEwIJsDnotlMRZcxeDCH5jfIOP5Jh-EJhznIv4qbS4UQrAI1V5RRQRyX30BghEaVqj5FWGz-sv7X8GZNMDKvu_taMPPpZ07K2Uo0FPSPBO0VEKVgDG3AMqdFrWWzkIqldIaG28NKHBPhzwqVaRZjdHMDdrTr_L2XPR-g3jbNDr0WIsvZd8Fpu3hGtbFq09vJ63IQWwW9g1w0t4EB6zC5re9dCzzZTHdxBAMLaONJJ0WdYVX2obhc7LVSr1wzZ5IkWIwNW-5z91LiPYYMYY3htpgrta4nnq4blnlFY2EFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=LLQkp6rvU9hM8PhAW5SYegRFFh4vA7Ovpl_bu23DjHxzbhEwIJsDnotlMRZcxeDCH5jfIOP5Jh-EJhznIv4qbS4UQrAI1V5RRQRyX30BghEaVqj5FWGz-sv7X8GZNMDKvu_taMPPpZ07K2Uo0FPSPBO0VEKVgDG3AMqdFrWWzkIqldIaG28NKHBPhzwqVaRZjdHMDdrTr_L2XPR-g3jbNDr0WIsvZd8Fpu3hGtbFq09vJ63IQWwW9g1w0t4EB6zC5re9dCzzZTHdxBAMLaONJJ0WdYVX2obhc7LVSr1wzZ5IkWIwNW-5z91LiPYYMYY3htpgrta4nnq4blnlFY2EFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stOnr5Y1BX_VOc5QBKwVDa-uvMLz_9MIxWtu-5ZcLclqabvo14I9-el1EqoXtqOEdDFzoZpeFdVdjF5_W1wSKLQbtBWKNMbzazRX_7A8Mw0NGDz3Ua0DfLVLVMNtahM0ItEh95WorjoSf6XeygOHf8QDozMRNzXdEvq_Y0SY5RDS-l1RFZ6i6QqyhVdTR7-iM74lA_VXxMw-AJDuJEEY7TUFxLnr0O9VlEv_uSpZnd05zxHEHK1glVnUHkOQ0zWqUreU3-6q5Er6wSsu7ZHLdMmYKgo8Agf8Pt7lHnGxluC-vUyraJiJo0wW9T347JoCQCGQkmzrIln_qcr1i78m-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1InL_zxX_6EHUOQ6b4g8CO1EBoW3x0w_0dznK26xlpmoy7JUj3sLB6UWDnAXk_xmaT-U0sth4UfwvJIUKrZ_53R7F4YnEWSUVhbMMDLFnaWZmFJCFyPWAMQKWaa3VJW23mlZzRLYcKchhKrfyT7SipjNA-t4g0WTlv5VO9zKj6w4N5KTAtmjMD6ydzE_eVJSqsHH-kKjE6Ktaa4gOsy5mttog-Ad8FOSRwovdq0EOfgb8ls3eMxY5g1t-7TTudp5uAVpTyDLIIeD8_gWLgLKgDT-yP7rEP4cpKlrVGBj-9BJUS-M3SLh9LxolMieP835DuhYQIJw1I6p2eGxuBpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYNkFOYpA8Fcb3FxNINQEVUhBHG8rSu0nr8wzXPIBQfLgfKFedsruHV5Roo5wI3tyF5oIH4tSN14DAw6zUvalaOaU-YWQf9KE1Ig1Ceq2-kQjw2cvHtQmP4os1d_Fd6uyUKj_hxMxt6w4dToP9OKcOnF3Gb0M9HH9nmrUn063dlIrDF1_KHqC9HPSuuwTII6NxuUyg8-HABd7wBgOrnq_hJmg_D5Vt6AjyivGYiMUgbM6zNrucYIiuHrsuLKDIpv4FAkrkEzarzirjhT6qcVZ9bdmPUJ_ksvy-LNLXYAjsYW-yXyIUj52xXaZvgxSd1AuH8o8XtqHhQNQaNu2s7cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67819">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3WwLHtfgNUvZR7CH8rQXbEsRStNM2fG-MxSD9FbtY05NJTMGyNXumld0Za-qg05YhqbTTFwNS2W4x0hqiO4AaYCWceWWzUAPluNAktL078q_o5BUxfqPZ6gM0labFQuOrh6sAfE20C1rvURWmOuPMurUUlux3SSGT3Nn_JTmuzPlQfyhR-W4THUOwTMo7hREagzm4wjxMkwMj2jjr3VGrC6v-mc0OfsJ9Uv_dzq4McNNq40fGb3AIksLIcLxKTp2ahYZx6B9dtSjKJkZc8tC-3F__UnuAEVJrDpz2B19qNANu6TQSqfqebCxbihJDlJVdwBsL-XPY9xo6hlIbv35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67819" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2G5aJQs4QaiXU8alxvk9Iix16QFXcbj_Ueud_zKejfd6QKzTfNSR3EKfa5hBwK-OHyA6RjG1qzs4koqjzj5LLs3e2U-IzuiYXYpPGErgy6IMGXgzj1fwNpNuh8Cplo9qXKepE9I4eN8BOukm4sE0HXHqyIyjcfBuDUegDbAFRiyDeL-Zst-xGS68XpCdC3iq34VDON7AdOk3w6yBlYfhYmB8I9c85QdTg49qt_M8CC5PMas2k4AvZgeX0ZIqg8TUxvlKVzJZA6MYl1oykzQHUw9gv4N0yDwRqf4upSLcBAga7m_b10FaLcb6Jt3g1rrdUbgYIrLT-WUQtiaVWsNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTDRD5hbtc3zNuLXNIQ81luRd2GpWSl1DSC9s6Y4FNT-XotQuaSsOgMfU7KMs_LXzGYeR-DyKZjuBFcHLCxkiEdujQnfMqRkp6C5J_pGIdeUdnWqBHMG06BpmsEi358IUlN40AnN_-V-XtdJVzNSEuFJ8J9cKCbGcccALd3MqhO93gh8X6CA9TGqFgBJs2msd77zIcClOzlII4No8A94QOck-JsFM0ljKl2X3QS2E9Zry3D3K-5kxpLqU6fIGoa7FAfxqnhve9apCbFpMnxnzjzPaw8_WWxPRrsAm_7f5YcRz9ezZ312qkNzeICnTdh2Hlpnaa62ssGUO8PORLfdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVKeY4sg-BMnG02YajuWP7rt8xIVunozg9AtxXY9pgo7FXCWSAKtKbCzPM3w5t8I0y5FxFc-mk1YBxAJ6x5ZglCMUw4VKcdkbAZxPomPyVfq7ZHjvIBdRvj3SmaR0tAIuFt2W2PzKONqN_Q9kAgL9wuFYo2CzUAQakLNGTux_ynDvIlDvrHeyIQLmsOaipRrZN8ONk2mVfQSo8sHkvIXfFZLbS2AbKq3TV43ezIAOeZrUQ9frOZiqetl0WHsBkLRoxlhoJ3CWbdmSEoHbD374AtO4HYgkxw-LETie9ZOVmwCkcaLouFppflsdiUbVPixYidyyK7EXeXzRpi0LmKiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMfapwhErKQLP4ZuV79kj594HvL44AfID_Kh2Db4g0anGBf6Y3JLTM5oO6uKasq1wQUozLIPBsgevV3rkcWnbvtzqqBD2Wh05Ywzl9yfm7jUvmRh1s6HwrrDLk5EFC4rvpGifKpmqx9Zs_XBSxEhD3L0hsbiwf3SQmFAZLD6M8a6kmZ-_EGrBCLRIenIW5PlyVw_ah2B16k0XvYPZlYHrzTCc4w6sqL_iOaf3CECrJdG6eqKzx-ujdAcPaBKaIgrgJcaM7Eac0orJ1GFzzzgVIYzJJm8h4zWSLNwDIR6etpR45wGfr_MXLK_O2Q3SXa5npymA8B8Jj_vR9PoRmdknQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=humdFprYduvy1vLGanHwNISfP30MoesgUBcPHAQeyh7JD2Yj_Ay7InJMlmDQohNRmcAynOkPyYaKyjpAIKWkqD3L2Zm2Bf2Thy4_IdYQuc6O24bMVjlh11cezP0Nht3SntdRa1wv4CbDEqRhkVLpvtVZp1ooYznszwQSZQoyBDWkVyuz2bv1G35KOenHrK2prPhPF5NispMJHuDqDV_W7i4hXHwsFtH06x_gVqAleCH3ElrD8NuITNG1_yN1xEHSh5iWkh-AuohvzvtJ6LcWcc5aNmQH2Okn3TbgCszPknTg31wNnqcnq8OlapSF6sCM9FamX7Rtc6xo2kYImVkfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=humdFprYduvy1vLGanHwNISfP30MoesgUBcPHAQeyh7JD2Yj_Ay7InJMlmDQohNRmcAynOkPyYaKyjpAIKWkqD3L2Zm2Bf2Thy4_IdYQuc6O24bMVjlh11cezP0Nht3SntdRa1wv4CbDEqRhkVLpvtVZp1ooYznszwQSZQoyBDWkVyuz2bv1G35KOenHrK2prPhPF5NispMJHuDqDV_W7i4hXHwsFtH06x_gVqAleCH3ElrD8NuITNG1_yN1xEHSh5iWkh-AuohvzvtJ6LcWcc5aNmQH2Okn3TbgCszPknTg31wNnqcnq8OlapSF6sCM9FamX7Rtc6xo2kYImVkfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTwwQCV3_97xVktyLNW26IMNq9JqI-FofyvrCtrmglRhuGnFav_8C_qUynClfyT0NEct5OsazdmEESCWapcNBzRa7bnVyFo3LKp1X7vr_8GvxOovt_nMwN_Vfl26m0E9wykGbRQ04DWOCYRfmNS3VspuoxJgNNyHO3vo__CcceqLgAHB1abXJNTlAqtc__t7y7kKnn-zDMh-PYW00SASW7-Q8G4gDmxMZ-XAVuvmQZVSxLb4GpR0NdL4hWaPL9-Xc_ObJiBHiB-O9Jt-sTfXRBF7b5acr_k8VFMdu2gfB_pOt9GKJpaxyLqG9OLxmbEIJ0Id95oDFiCn4fsd9zKseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSaeq9_lx3B74WbosOjnaZROFUFG3Wd8VwaIK8oY0sgELkMs6mVFQ2D8MVokOal1tv2sv9UaCcrQgHLsVGju3dOR3NfMsL-IO7703kbrih1IrdhBg5Zsf2l4jUeNkARFao8ARMOSSxCeCFl8HPxZ7nCVeMWMHR7nP-p_qMO7oJiWm15txI4DWB4hTmqLwnoaB1cwj9heRHl9JEjxiJHWLOOMo7XBC5SdGdVmIgU7E9bf3KsV8KcmJyi40aMHcm-Dmhj4C8Pemj1DseIBjfaZSm_gPB5fohqMK7XcmILKrJ1ZeMiEs4_r6HGgEeZx8REZL3TffJM5zx-s-lsvKW4I4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6SQAYQEacjJIYewbt08DmeYsnXCPconFZFu4DaSj2WxAcuwlKJnwGaHhcRF3p-uhZmR6YNn1CSuL5IzMBNH2pnCAWBqhKhKel9jbLwW4D8Vk5zVsRuYQRQIWZWI4AnhIOfyIJQvKE4Lv3n_rWE9CWfew-Gj_36I2X6UV2SD3vE9eRPDJciU5GDhduyDBCGdkva2l4e7SebSAPr3LKCXBVC4DhRlxxUqPIjz586yyZ9YuFzSP7xQQRKeEESIbgIoK5UzM1S8tn_MqwwMQK2w9J8Qleataxjx3RH17nXSz86_l0yF7iSYKuyJFptSwFwCeXObtVySDBupuOV0RK4pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHZbzYSGDz8f-9G5srP9cFpHBl0kBs9jVnTeE_Va4wJjyE9FqWS3UVPYiUMUA_VcpRuG8fvPHjbSfXA9xEELec193cseb37jxJyn9fyIAG0LoKPbjzQbtyyna-wv3Q0vTlnILu4-fh1FJZBlQ4MBYZm4K9HWcDGZHVWPCUl9XPzm3LFNqxVjxa1DrgHNJnx1i6KUXerEUcX2sidmTfavHPfewvGf31blWVS3icn5a6S6k_r_aC9WZcAQKfXzPbhLMdXI0AClY8HAvuoLRGSi4USIqRj34RuiEchm7Ksb6hPvoJnB9XR9f_B1oh671onzjjbGsjQwvi-haJVyeKQfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=OCOIYXEXZ1uii4GXh-5RxmTv3g9OqR0AbUrf9hfHSEOjsBkFEtOJDJ_Ew0lWrcRI03zGXAiyKtdPLnIzIf6kxSmOLg2ks5gO9OhrEe_duRUN6DKNHb8QUHPJqxjdXumt2M-7iA7hLWHBCW5lFU9feffh34NPFZn0iO01fN13yG1hii36wFNKnltOLSDNkNqgbZUUYhVWK7cv4QrRISURgabsKOxx3ZX8dHt64Q4tvsJuASOhQ4x7b2CDnDbOKueKtn47DImMvhUyPRPNNFvFDWMStJ4Q_jYuU70apR4HNW0pJRnI9lncmdp66CpU82RkSQRvMMd34BkPpQWzMeUpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=OCOIYXEXZ1uii4GXh-5RxmTv3g9OqR0AbUrf9hfHSEOjsBkFEtOJDJ_Ew0lWrcRI03zGXAiyKtdPLnIzIf6kxSmOLg2ks5gO9OhrEe_duRUN6DKNHb8QUHPJqxjdXumt2M-7iA7hLWHBCW5lFU9feffh34NPFZn0iO01fN13yG1hii36wFNKnltOLSDNkNqgbZUUYhVWK7cv4QrRISURgabsKOxx3ZX8dHt64Q4tvsJuASOhQ4x7b2CDnDbOKueKtn47DImMvhUyPRPNNFvFDWMStJ4Q_jYuU70apR4HNW0pJRnI9lncmdp66CpU82RkSQRvMMd34BkPpQWzMeUpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz47oX4HCwlfkPryYs7n9U5n7J2U5tT5z8Grm_ewaNuF5hMtmAl00JuZl2fxrciAXrnrAxMr_pKAU0psEUwj52obDXIJBFyAZAaloBY0M291PiwLDEHBlD1ym_k7WYaaGttDQwNN9Q11WJSHnGDGnpP3_fchB4LB_Ub0L08AsxZNnyj3MSamSX6FwacP4dNoxxFN58iNLpbaajet-R1cx_GZH-Tthue5ea8V4wzhTqzV_1pxUSXv_LIXrOqN1laRQ3qSxbuAAaNQJ_qXh4ryaSoT2V3xXPvf3iqQJtF6F_lwmk8NIp7QRbg-PcE6_TPCNjeRTGLYMjNdKceDUXu46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQg1odY-yEUCL-LYsgG9F8cquKXFPWK6_PuzMb0zDFsYCpz_xXeg-f6eeJImnXpWffpzKX7H3SQDVAVa3L3I07iT-H79akB-Zf017DsfAQAINwCgv85gXWCQU1bsY3apepDv0LMxY10CS5Xz2J4BEm3A46n33dV_eaEnD6VxsRUXg_LlODD4LpCwGaK6ZDSia0EoM-KtNamBQySeXaTRln6-Cs-Q1k9DkEB9bMvf-LJGt957yefaoBuFebaclFPbq8XiZRGrxDMVd9uEoewT_XdN7mc7JZiAhwiJpvVPHOqSu3FL2yhhss8-plMctu1XLIKt3MEn1UfwkAwsOzjcSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2TcBq79wEhytebcB7FQbq8WXShpBg9uRIhACJytvxYB_mFT4yNOccNBLQrF8X8A_XhiUlovw7kqkVVFs3GdnRZD2DRq_U7217v4MW7w4lhLtAJ3ZrctoISdWW9XzeGGsrRmsMlnWDv3RAkK2hhvgAGHaIHPQCJc7YhdzLzM16Lb5HShckTZV2zEkyVdsZhYGP-pFSBPglrMJmPx4DCyjjQe-cxewhD6YvKWU9jU7mTfM2vIrGxL8kY-fUS4MgWDyFHUvi0LXabeteImvWbkEt450Z057WCfZVRnYed1fXQSSbvL5VkCyAJul_e0cA5-uQcu6GJEsagrR5hxjNkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgD_8dv7aLb8S6xzrgq-OFTHueI9s9WVu6uwbWtMcguMQ5wFo7oizJSTq_-lnI_lF7vPGqsZXPlrZBorcGWvNCljQ-IUYFGhFChwsvDRSYXZ14wp-mheXV34YZlpwvGx7xBgrMSCv3rXci-J0h3DLW6we4uEf-kLRLrhbdkIgnaeeXb10dMfK_ra2BfbrNjcB0Wpg03NQZ0bfLaGdFiwYMTkTueyJcv0SjEeaY4bhXdROAhuHoFbvKCuTSPVDZPLvwUfTLV0e0NjiDYXuMJEf8ADzHx_mkEpfGojgPnWQIqI-HzwLmr8ssHRJimgbMRhIDocBFVa9B1sC5fG0xAVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KySb-tBVe_lgLfk3Q-0xfTvWBdP8P8leVnsU7w-u3CbqrZlIKzDuiCQjF-8F-OGYGTcQ1MtNy62BmfDwVybsDEQ3AXtKtvMGGOESvl3oVhLC65lD-2YHO2HOIMd8A9i5XbapJgTGi9NfZZYK8rWS9mp1zcHeg4QmLQ6glHuonlmLn599BFSdi0aJ1CAemUv1kaTVv1YJhOPmA9tDQ2TCTkSLJ4hlNsuc6lxE0ttnAOpvzTsr_9gVJYq79FX3hAlkHTGSdwIUAjKsAcg-hYmoTN8PCb5PeEAhuOiiIgkfTMS5P91VdsTJV9SOaIJKT9HOyjGVBhp-NrKLbzScItrePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJUvuQzhnslbkp4rMznMiIBNOvAETStYvkvPUQM9veLN0euFmhog0K6I17oR4lV56eC5giZvY-8cU8-uNthIZby3JIkiT0HRiRCFm7wL5z0g1Pb0Qsv9SpTWmptCSz7-m7Y0U0s9k_4Bgw3Xat9ce0wzclHdPRW2fV5FBfroRzjQHbnTO83cxboe5liifN2xsLG2iugynAhdhexaXzYNoxorDspeu5DOikZKjjGc_Jvi2hYTaKZbQIlZvxZcq4NeSSBaErUkR6f_K82eWRp8TGd9h5xFuNgYJSfq9hD2pIdh2ZaJ3iquCEIGtL6g9IXk75gJj3WEXSyUOAN5nRztmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgBw3TheJ3ib4Fw5_CVPkw9neAYRmLohZMpGlTEHASQenJO0OQyrEDk-hCdfWe9M5BGEH7y96je5GTjlqOfA7AyasDXBI0-Xs0XuJURsOwJg0Gn90uPvS7KG18lB26vOCArWWwoYgrHV4a8imJgQXexyCmg0DDO1kyqFI46SJixpuZcyBrGdATYGcdWGO4wKJN-0ZPvFtytrWn3VsPC0gZHCsFwHU1u2NHmncFg6-YhBH9WfvfDgCeCn9B5LK-tDcz9edsZW51szpEBjI4EKHDnT_7GeBbfOSuNKtveNoj2lls7nAwBq_GylOuhQwtK03nEGIz-WY3rygZP-jN-jTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=hZxnILR8SSS6nztueKT2NMJIeYCi_Vz4VnlAR96N9tifKEJXkLIodTPgTJVkHWYD0_xf6IRfcIibIVBOtVmg0YBy3ZUclHh_Wc2EI4t8pe2y145Jgs5lgkaawbE4jfJLMBlrR6GUpZROohFGMMEPcxpckJFYdzohZHNDXOEgAtHqKuAGHsAWEM_wVi0bO_AUVGLXyI1Yhj4Pge3zXur2WOKkRkVAb3-tT9E19eCnK3Cl4Fv4R5-A1lNPScIw0qB7pOW7VBab4ZluK0ofXAtd0rMTd62vGxcc-Fj1K0CZ9ma5VXfLE4b8QG7wA_uMcNArHvJfWPMHgZpNoj3gF6vaKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=hZxnILR8SSS6nztueKT2NMJIeYCi_Vz4VnlAR96N9tifKEJXkLIodTPgTJVkHWYD0_xf6IRfcIibIVBOtVmg0YBy3ZUclHh_Wc2EI4t8pe2y145Jgs5lgkaawbE4jfJLMBlrR6GUpZROohFGMMEPcxpckJFYdzohZHNDXOEgAtHqKuAGHsAWEM_wVi0bO_AUVGLXyI1Yhj4Pge3zXur2WOKkRkVAb3-tT9E19eCnK3Cl4Fv4R5-A1lNPScIw0qB7pOW7VBab4ZluK0ofXAtd0rMTd62vGxcc-Fj1K0CZ9ma5VXfLE4b8QG7wA_uMcNArHvJfWPMHgZpNoj3gF6vaKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=OEZsxJon_7lc9kOSenL308nSepiVO16LyNtaF9mGLYkXuP65sj5Brp9gmLVWCGLDfAmLY85NCBoUvtxdaCi9zEGInHp6x60kNco57sVp6TOK0luYCq-G5ALOMgZ678JOBWAbKs3TOa6T9ZGZCxcnm-lAekoUzXup2EO7Nx2STKPJPMJiUcyJhBT_CiF6bWGD-A7JFxbNGDLvANKrqoVnQTdBY7gQawVwVaEgpttrceG_ZufioQfU-VbyMlB0brmmVPnVgRBuEDQTEykAfG6nzWh6sNroxd2d4Q19PJM2ji5Q33sPbJqJ44J5sjzKbwc7veDWhnmhPivjbuQi1fsAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=OEZsxJon_7lc9kOSenL308nSepiVO16LyNtaF9mGLYkXuP65sj5Brp9gmLVWCGLDfAmLY85NCBoUvtxdaCi9zEGInHp6x60kNco57sVp6TOK0luYCq-G5ALOMgZ678JOBWAbKs3TOa6T9ZGZCxcnm-lAekoUzXup2EO7Nx2STKPJPMJiUcyJhBT_CiF6bWGD-A7JFxbNGDLvANKrqoVnQTdBY7gQawVwVaEgpttrceG_ZufioQfU-VbyMlB0brmmVPnVgRBuEDQTEykAfG6nzWh6sNroxd2d4Q19PJM2ji5Q33sPbJqJ44J5sjzKbwc7veDWhnmhPivjbuQi1fsAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLEHfARz3jb64BoYFXOnUcV084qIXHXGWcKg4tPO48XhNmQk5JYl0KJH_0CyRuVQgI3UrbAtSYVtDJp_DR0HE-0xrVooRXaq2PIJkuD0HlYZJLiijWJ0yebAMSScNNDkXA1tK3RCx2-an17aAo7lrRsqieKcSoP-RHWxQpHvEe74obxekTRKp0tdU-lI5C56yRqlV_HVHF8rywgNbaDlTwDTB4GWJTvZkEyrF-2-Yix7dsx0RSURikTEB05brzwTj-ZgQ-IdxuT58U8uIQpTKDrzKplpCv80oqLJdYIo2mTAQL9j7hCOfYkDjM7NEUk73d9bEHnKzeuu2FuRWvfRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب رو باید تا صبح بیدار بمونیم که ديگه کم کم جام جهانی داره تموم میشه؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس vs نروژ
🇳🇴
| 00:30
🇦🇷
آرژانتین vs سوئیس
🇨🇭
| 04:30
🇮🇪
کانر vs هالووی
🇺🇸
| 02:30
[این فایت خیلی مقدمات داره و احتمالا ساعت 5 صبح شروع بشه]
🇮🇷
دانش آموز vs دین و زندگی
📚
| 07:00
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqNwnQvmoTCgFesfL9YIP2F0Dc0_YkpQQSPo_UXP1bzROD6Nbt6tDH6M8yzHAbax0KnGuUU8SSCf4BUy5MqcLd0W0iYNB4joJeIP204ZH2SIGJyrlNK7cl56mdU7j87onnaGHjK08hOeBEpIoATmb1Dozxt6UkXE3UKIIFE6Aq3bUAxizFalMe-WMwpPQtl9sGe4ePMh5bgmvSZl6KPwuHAAY0Ehw7zkqyCkF_OazGuxapXgTBqB2MbHVdmt5fTORA8zDKo1BRRuDxTTMwdnHEbfaYsEKFiGb90n9OhWcOJVvkfD4ajBeGepxCjxp4V04l-TUklQcMfnX9hKOZSA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfcsfrOlAPPQ6_j26U9E8q1kZ6mJwWgh9GYmVfKlhq2MXSLQFcBJj6IBDvrv7TwFpwzwofe6Z9oQ0NYYY1eP_CZLvtZQtPxY8ax9b6tU-N8zmXw-Z2J5LrLDsrll0agjFAo5H3mDN9vX6xmkWE8N1G3uqXGnchIINeTxMYl_XUIDVYzGRqHGFPmEGnbC5bo1jZ2z5pYl3SLcrZNa2EjjNfVMFqni1gskGW2tzkTmWMDuotQWQF5xAdq_t0BTZRL_Pjl53XX0PM-a2Gfayj3cBkBNHJ5VUzWRJUyEIqPv8CTBZYNa3db5S02TaKsKe4_5WoCntMTQzjYPYxaqh5KYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2gMhdm4QJlQte11G4BKVfP-iwldSbFoZvUccA2PP9h-tmaH6TyylAKaBrhA9oy_nQmakrEX8RECMamcmnNTipv4GVTSv8O1HyWUk_MIvU6s60BYihPVbyIkJ5Us5qDn7520HYyKzMNmxkOQue2zIyR8VvpUCAY6lsEALqqpgbCI8mdqbvd5fKZeiH7UY23d_o4QpEouuxG97t9c80gsRosNZZLBlQkfOzm7U697j7XLaR1gQyd5P4oasehFSNqWDaZwzTfkt87lzlwtLf1N3odU1OH8QGZmUBwj1orbYF2-az39nLsjsL8YjN7sy9uaVX3iBErZzGPb1zVbVUAw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از انتشار ویدیویی که توش یه فرد ماسک‌زده برای علی خامنه‌ای نماز میت می‌خونه حالا طرفداران حکومت مدعی شدن که اون مجتبی خامنه‌ای بوده و بصورت مخفی و بدون جلب توجه توی مراسم حاضر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOOli3eL4X0Ixtq6p5_vF9B5fTt8sD5wN6p3yDB5oxx9RHG_KAZ8mw0daqYNr--3F19gun_t3aOA0uQHrGbPBD8X6chPfLTlPDg6GQ0o4xp3Mhfdp-KvYaVd4h-f6WTWmYsAppXlYSpBCsoffbliyLo23XUYdBn_wcfdlwmcKtpfb7ubavVC5Ql-VCb38-ljyXAhU8sWeBI-7bGmTozBioi6rykjvS9KsBfPmLPxh0PRvBty8C17aJaUYr0q7qDDYLCmSgtt3XEnRpTxOUByCU-iNfCqNJEHgV0FAnSd5nKFhFbNxPRpSBgBJVcEC75Z6QXat8LlVundBhv_RP7L3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67770" target="_blank">📅 11:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn6N8MTa_GBRr7Ncoq7sf-2FkSLUvew9hT_3dxbxH8t6frjpvxASFRBj3BnmD8Hhf-8PmUnZeU3P1T8wVa22SpQws67YSmd-t8B_hGQn-2DWRmpbmZAgfxXLb7QbLFcvdNkVM1R9lRg0tSH01jxwxF2lVw0AzlnI7n4X7L5fBoN0iONWNPuaNWqxhFinqKiy3g5NudvoIaj21L8uDLk0-_UjEfM9WCIjY18f-wMSRX--fyTTuGxHVX5ncmYTk_6YAGHgOlEmFOkuhRKDDSPOlFpjAqQUa0fEsuN7p3H2nOtZI7ywI4vh9aQJTzRB9FPop7I7n9uQz88n6J-M-qjXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
صادقی رئیس مرکز اطلاع‌رسانی و روابط‌عمومی آموزش و پرورش: آزمون‌های نهایی  بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67769" target="_blank">📅 10:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=DELjExlqY9BAsf1tNM0GvLxKAeCR1JxP8h7lDa7aL6arxiAE1Cn4pwFFass73yiA31Td5GfDnhDsATa0JPBFm2oV2A8VmR8kDwpc_XqIaj0okHuZuq1q2hibemRjz5S_IFMBfjO_6VYPAMDXT2BK9L2IcWghqrIE9EbO5SHIYfOLy1PVV9S39lBavks0F08Lp6Dz319_DbyBJF2RNS4D23zHzD28vhbfruoSGsH0Jc1919INGQFWQZjEfhOtXoapvmtAL0HDAzdehQXNx4y9qxBpLubk2AixJoyQ6K50i5nC39NGKkAEC3AeED640O-TdzrUGDvdVO8_Z_59TtfSAnCQLjZXihG8LQKjenv1wJz3jxOR2r21PUd_Z3UfJjRMb7nvEjTckRs2E_CfjgdZT_ehclmT4UpdMy1MlSRPFcT8bCgA2blSkGmiG1nu9mV1e3yKybT9vKMrYhPzWzPFOR3jkB9zME9I-qy7afuAVIg9U2XWYdX1qiyNlJB8rZdle2OXZBO-GtYOsuzYR2kNxdpnxorRAYlFGanyu70n7duOd6bLUFPBoUWgbxT5HeSovJzBIVaSeVf7MMZgcIBxdkBR44ocUVcMqNlEkM31KahVNcpoHk2rfo0XugpR4i9m4gzGJesIZndLf53y2OHnivnWhq29rEXA84KH5MQlwa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=DELjExlqY9BAsf1tNM0GvLxKAeCR1JxP8h7lDa7aL6arxiAE1Cn4pwFFass73yiA31Td5GfDnhDsATa0JPBFm2oV2A8VmR8kDwpc_XqIaj0okHuZuq1q2hibemRjz5S_IFMBfjO_6VYPAMDXT2BK9L2IcWghqrIE9EbO5SHIYfOLy1PVV9S39lBavks0F08Lp6Dz319_DbyBJF2RNS4D23zHzD28vhbfruoSGsH0Jc1919INGQFWQZjEfhOtXoapvmtAL0HDAzdehQXNx4y9qxBpLubk2AixJoyQ6K50i5nC39NGKkAEC3AeED640O-TdzrUGDvdVO8_Z_59TtfSAnCQLjZXihG8LQKjenv1wJz3jxOR2r21PUd_Z3UfJjRMb7nvEjTckRs2E_CfjgdZT_ehclmT4UpdMy1MlSRPFcT8bCgA2blSkGmiG1nu9mV1e3yKybT9vKMrYhPzWzPFOR3jkB9zME9I-qy7afuAVIg9U2XWYdX1qiyNlJB8rZdle2OXZBO-GtYOsuzYR2kNxdpnxorRAYlFGanyu70n7duOd6bLUFPBoUWgbxT5HeSovJzBIVaSeVf7MMZgcIBxdkBR44ocUVcMqNlEkM31KahVNcpoHk2rfo0XugpR4i9m4gzGJesIZndLf53y2OHnivnWhq29rEXA84KH5MQlwa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رحیمی (زاده ۱۳۰۰ تهران – درگذشته ۲۶ بهمن ۱۳۵۷ تهران) سپهبد نیروی زمینی شاهنشاهی، آخرین رئیس شهربانی و آخرین فرماندار نظامی تهران بعد از ارتشبد غلامعلی اویسی بود. وی از نخستین افرادی بود که پس از انقلاب ۱۳۵۷ ایران و در ۲۶ بهمن تیرباران شد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67768" target="_blank">📅 10:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=mGA4VfUjRAMWG7TCYDpyo8ZOWkDtlZwowHt3yxswmA5Hrspfwu-L6IyGpDqWb6fOA9nIJIoA35PuMjhp3dMU7omBKWan3xEJ9PFi0xxc3-CIKjGZQ5V6LRcUfISByue2i6vsamT3vtH2nj-yTpwJIM6jxKitEm79eUSE9GB3yGDUBf7FPgb_aZJeb-5BMqR3LTF40QIjzT7wSGDmoEKlhuAmMDRYLpU645lqdxC4i-oH9LlmJfPNI0SlFrMUNl6rJ_Amg3Z75WFhYUWx21JEh8RDYPArbPB6dn7gxeYGFpZ9zXnwqFird1mOdGK4k00OUXUE9LJGYozkRDNJyQkbzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=mGA4VfUjRAMWG7TCYDpyo8ZOWkDtlZwowHt3yxswmA5Hrspfwu-L6IyGpDqWb6fOA9nIJIoA35PuMjhp3dMU7omBKWan3xEJ9PFi0xxc3-CIKjGZQ5V6LRcUfISByue2i6vsamT3vtH2nj-yTpwJIM6jxKitEm79eUSE9GB3yGDUBf7FPgb_aZJeb-5BMqR3LTF40QIjzT7wSGDmoEKlhuAmMDRYLpU645lqdxC4i-oH9LlmJfPNI0SlFrMUNl6rJ_Amg3Z75WFhYUWx21JEh8RDYPArbPB6dn7gxeYGFpZ9zXnwqFird1mOdGK4k00OUXUE9LJGYozkRDNJyQkbzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انفجارهای دقایقی‌پیش در مناطقی از تهران بدلیل خنثی‌سازی مهمات عمل‌نکرده بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=FIid9s17v6pBsfpVGASBt5KUySuw8bOBfVJZrqymgUlyWkGO6LFaub6ANYuM3lN8B-ONn8qEmJPbC-UfJjRLqaMtSvdtoXkHX2USfYAxrcS7MGDIsdEsy918PsSaxr_KLKTT87qVNM7Ax7_EiQOd6FGERKSZTk-BB2mln161lzBdJ4L5MszYDLl7ua0ianJU6Nx7ElyntCyVnz6kdrN-Is2pRdsJUGqNj-CiZ3kq1KBu1_aHR5IyBWveQcBavAAb6dyaFftGq0SQ-bGMMQ69wer66lqaxbdMFEL3UxgkIjVJLqBccJMWPtwvq_KQbo7eauNh429_wcaU68TWAYdTuwcKGU6a6ruisq9eKS2uUixv_jxpNI9ohWRAcbVvIe2SExRFmUGQHM-Z-t1GkfmRYLkoqDMUDj2qNtr1rvuBhz8eKNyZxW1lZNytkxoOaJ3sm3ctYiTxEDZApc6YPNuvQe6bZ2U_is6mz9vkrjuiNVvt5IWToN1QBfyDFv2TFPztYv0NYCHvYfcNk4T5d0HkGifaD864Zp8UPBtRmNsbxlhWTf8HdFAKR7mMS2aXvAAW8XAlqcB-cJCF5zzP7PlfkYiqNBo5Hb9WegmeEap-hxoUizRempLQ6EOXLkdGrk0dzsfl8EQ5LBZh29hLZsGotq5szs3NPDP5WmS2C_Ev_cE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=FIid9s17v6pBsfpVGASBt5KUySuw8bOBfVJZrqymgUlyWkGO6LFaub6ANYuM3lN8B-ONn8qEmJPbC-UfJjRLqaMtSvdtoXkHX2USfYAxrcS7MGDIsdEsy918PsSaxr_KLKTT87qVNM7Ax7_EiQOd6FGERKSZTk-BB2mln161lzBdJ4L5MszYDLl7ua0ianJU6Nx7ElyntCyVnz6kdrN-Is2pRdsJUGqNj-CiZ3kq1KBu1_aHR5IyBWveQcBavAAb6dyaFftGq0SQ-bGMMQ69wer66lqaxbdMFEL3UxgkIjVJLqBccJMWPtwvq_KQbo7eauNh429_wcaU68TWAYdTuwcKGU6a6ruisq9eKS2uUixv_jxpNI9ohWRAcbVvIe2SExRFmUGQHM-Z-t1GkfmRYLkoqDMUDj2qNtr1rvuBhz8eKNyZxW1lZNytkxoOaJ3sm3ctYiTxEDZApc6YPNuvQe6bZ2U_is6mz9vkrjuiNVvt5IWToN1QBfyDFv2TFPztYv0NYCHvYfcNk4T5d0HkGifaD864Zp8UPBtRmNsbxlhWTf8HdFAKR7mMS2aXvAAW8XAlqcB-cJCF5zzP7PlfkYiqNBo5Hb9WegmeEap-hxoUizRempLQ6EOXLkdGrk0dzsfl8EQ5LBZh29hLZsGotq5szs3NPDP5WmS2C_Ev_cE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سید علی خمینی، نوه خمینی:
«هر کسی که بخواهد برای دستیابی به صلح با آمریکا مذاکره کند، خائن است.
هر کسی که پیام‌های دوستی برای آن‌ها بفرستد، دهانی نجس دارد.
مشکل ما با آمریکا، مسئله امروز یا دیروز نیست؛ این مشکل دهه‌ها پیش شروع شد، زمانی که آن‌ها کودتا علیه ایران انجام دادند.
اما با آنچه اخیراً انجام دادند (ترور خامنه‌ای)، بذری از دشمنی کاشته‌اند که هرگز از بین نخواهد رفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67766" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-0c4NjWv3onzgAPKcHn2L-aaSLejePPQua_lAJJiwutTzddOyTRzK0fRCO-MI9RDhyyGe0LLnULUqyk0U_xNzv5cxWYzyq4EkETnunLPe1noZPilZFI9C2Yrai9YCmva2vh0jDKLcaMZU8iwBrbiM8AlEZhpjE0N8XnRP2x9m8U-u0FpZhRrJcf5reUU8IM1Gf-Z8aZPWIWYqbjAQedTCRzhcg69WVW700swJtub6G-pUG694HTrIkGsQ2-w01l4EovqwI9xbijYXw-rKkKZatyKWxYKdHKI01tPkAd8WyqXdsP6aIYxqb9fYjD1EguLS6u9ZcfFp4e3Y2sv98FBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
فردی که «رهبر عالی» خوانده می‌شود، در حالی که رژیمش رو به فروپاشی است، در انزوا پنهان شده است.
وزارت خزانه‌داری همچنان از تمامی ابزارهای در دسترس خود برای منزوی کردن او و دیگر نخبگان رژیم از نظام مالی جهانی استفاده خواهد کرد.
ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67765" target="_blank">📅 09:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/news_hut/67764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Wqck-uTnVKr1JCreDj_0AUmXlGvFjRkgybwdH-i6haXSReQvkRer6AZkoc5uWEGcRL6Evkf3oAZ4achfQB7QFDX6xiRqZTVw9BuHn1anBZcaUWVKttX_3QSlEaRQzXeIIS_TDthG_WPSOeicrLG542JF5MSfw8WK-mceaeErri-md8WWOJTbgVwBm23UxDxjvAMrT_prZEvA0p_GQHc3qNhjjNtkhRFhE_vTLa4H2bgLlfY4K7sJFmWdvrqqWEvvbfSDFalHHIoYy2aa5DiUF1xZWY1QmxKU3462M6EMwLN7u_i43BryCEeWTNB3JUCPh9RO8Fuw6XDrmDnRLvXYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZDNNgFoy4A_3CGopMjYjPjbIsiwShBOWJen8znfU6uaSzmlU1F--qENgTkPXIkNA-87C37zbAdIIC0ss0TW-0xZEzWxy54YEJkopZHiC1NlhI2xQTuYifBKebpfOXc3aMT9UB44C1rorWVHhzMrVR3t6cWTALAlvBaofkXfXm3ySOVobodb7I0ggwnuPzkr6Jrrx4x4So7iUZBXQE-SsLCt3BnTlNamGeIPC1c4_mXJXvBumW44S15a56SacWhE2_fWA-yrUvyuXBDQY7jM0aeGHpSgBrjUqema0BV1RhWdAXhOcAmCAOmxfOWGMbCcSFDrEVX3chXj-jRQ5HKoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUIi_kmBwaWolF5_yqfFsBkqxZsC15p_OxNxra1TvEHveXjaQThQqtf6i4Q_Y16s8818F1dwiPqeI8dnWNgHIKpowY2qBxalVEGAegWZHgVzxNdBivYT3KVEnJ_KfcZbVm3v8tAO0IobQX-9oXavJiW_pQg1fVNjfNudSqUO1BLmUm9iAGpgi4Sz21iI5tlUVwjy37iMKr-V9UGInqAovdyFd_NrF9pfeA45oC7f7_GQgX8WsH4Fg3bqOmBp_YF8HuV2vpoJxXNtoFlPHg0BlqZc5TK5RXUQvi-78MnHQuQ3_hCy92MKXTWPw46GxMIEnJgQPo6Q-XfaeublYDhIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=kP-CCBIiSu6wriNVS66ZHX0I4j30KQltu92pNJ6RwwnEjnMumCSCPdphOmijTvL5lJrqVs8zuy43wk7ick5WqRY-u-VSKsPDSjcg9C1r0BSF0PDeCjsWNI_K8i7n7g22rXv2gxrFxjaNaw3SIIvhiJ6fF1IAfiFswaJ23VN6si42PwVfYqjSDh8y1TcZG4KkuFv5gwTblE9uJAcrGPrX_0ii8VV2mkvht3a4cXlzK-ON-hymfwDX9P3Ib1DX0x6qqKFSSVwqyDatyWXdw8dnNEXd0sZ-1wGbjVb8MhBrBYwhZrfnT3xjrzN4xqVzTirj86D1-oaEV4Dx6hon7ED7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=kP-CCBIiSu6wriNVS66ZHX0I4j30KQltu92pNJ6RwwnEjnMumCSCPdphOmijTvL5lJrqVs8zuy43wk7ick5WqRY-u-VSKsPDSjcg9C1r0BSF0PDeCjsWNI_K8i7n7g22rXv2gxrFxjaNaw3SIIvhiJ6fF1IAfiFswaJ23VN6si42PwVfYqjSDh8y1TcZG4KkuFv5gwTblE9uJAcrGPrX_0ii8VV2mkvht3a4cXlzK-ON-hymfwDX9P3Ib1DX0x6qqKFSSVwqyDatyWXdw8dnNEXd0sZ-1wGbjVb8MhBrBYwhZrfnT3xjrzN4xqVzTirj86D1-oaEV4Dx6hon7ED7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tczWbwV-XDf8zdkjzy5YgDGLyZ6fBcJ0fVtCf_pEq62vWxOQ2_46Hbte-kTo5UytHin5MWwMvPFjfq2wUwkeE_WMRKpHXrgQ5CjrSbJJj0yJjM1BMeP0PPSx7cNXc7M5P71kGhWDjzHWJLqyHPBqt7GvaA1xVWGz-3qQNUb3pixUEtzshJT5o59v7-2UZNxWCprjQi4CRPJBaIxcMK_YheoGrEmS4Oo4JAi8Xb39p2sud4mrS-fKTNbii6WDEwIXCxdZaoe7pBbKIAxdZsSA044WaNdD6pqGLDTefsWKVyZY_Bzou2JDG_WicpQcdOYspJV8cq_vUmNTazeg9vsknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHKLz5CdJ_6ECpA5DbussvBZwl14TfV477zuXYOooWV6Yyw-Z-TQULTcd0ztyO7TrEh__QNsJ2RB7DcQCrsThPQ5r1vhIi9AYqhAKEU62Klkadf14uWiC9y6-YIBGklL6i6ZxzY_fjHcOx09ioio76bjx4lyeSKVou_8LaUUxuFHfWqwUhbBEk6xvSyO9PLaTEyO383OJ6jE08BsnCu3tPHY4eJF10PX3H1BeJgFJQhWSRgS6S68D8-cRnCQfoL-yX90rQR5Rm5ZCZOvIDI20mQXJmTl52smaZZsxQ1p7Hl41IciKbqxm3QgMYTttpISQpzTPAVvfUIUOQBIc8ZlqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guamvWbTTDiVqR_dWiwDOGByN8Y2yzZdhFYyztDciv8-DUXMQ_NerNN-1Rk0M0clvLZLmK1TxfVY5TS6FzYK68peIYQ1h43zhHEoNec-xf4OmgT7isrizbiq1KfSuurvl2KQ9Y3guFUj0HjZDFnIhpyPJmI9_KQiBq_RMB3CyYmTu80aCOyzHpD9ykeyCY_NyQAv2i-G-iu8gzwMypm8LfHBKqPIEIwXVB1W-4DGdLYCtDkhd6e1O5ldtkR8cov9ZLhlQe2vu1PBW6TI1DIx6Ip9Jrj_NFMg3xm9lsVFM4hg2jZCe6_gjq2AUaVrNb4VgauBpnxTy1eilticND9yqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=n3eQgoukz0J3NGOXlfFAykLfkI5IoWf53B8Bgg3Qw4w8B-8RS28sr7btlcp-niCuX9Q3oPqs8DPgJlHvjnD3gfmrSFOeFCwTeugrRb3polHsWwQESRB2QPs7TwrpKQJ9yXI_fHhJEdGptVda7CiOu5Eqi9AbLv7THs_2zf-7rRqHh_sWhLcF3br6FSvfMraVrMXjxPzothcxuJni_a4mHXFrsX5Ms4b5-npuEHLFxGoy1a0DGtfoQrhm8ptr6NEK59z6NQUZkQuGrN4ckQLs3VEuZb9zUURe9PLOO8a1Ha90gp8T0Ks36RHkicuWyhXyLs1oVAyU4mYRfrG9AdtRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=n3eQgoukz0J3NGOXlfFAykLfkI5IoWf53B8Bgg3Qw4w8B-8RS28sr7btlcp-niCuX9Q3oPqs8DPgJlHvjnD3gfmrSFOeFCwTeugrRb3polHsWwQESRB2QPs7TwrpKQJ9yXI_fHhJEdGptVda7CiOu5Eqi9AbLv7THs_2zf-7rRqHh_sWhLcF3br6FSvfMraVrMXjxPzothcxuJni_a4mHXFrsX5Ms4b5-npuEHLFxGoy1a0DGtfoQrhm8ptr6NEK59z6NQUZkQuGrN4ckQLs3VEuZb9zUURe9PLOO8a1Ha90gp8T0Ks36RHkicuWyhXyLs1oVAyU4mYRfrG9AdtRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imhgex8VOf_8L_Xr_dWGbiVibTT3KbeoOP-8tzBnYSff82J2MX9hn1HaWQ8-tRIxaF8FyIYpg4R1XIx66NNvtfyOyph_XVTpG-tuIfC04U-Pdnfk3p64QKsFrU-Pu1LD1JKVCTt5FoNDTUdq-q1NwJgNwJxGga9ghNkGup8D2H48J70430QzThJqDwIxwW3hT2H6y6eNKNv5odqnqTj-e1V1040DWdzW5yVK5p5acjSeTq_LrNibDNrhehyHe-YBKu5ojFr5IOwjRXHjIx7amf21TuE5mYxwiamzLDSMN3vHjDutyTkOg8ml9AIp1GBiN9dh70Kt-mcxuN3eMq6ANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5YBt4Fj405l5ofOCcN6hGs28xPpa3MXKioguLz1p1lOmpa46QhGkW3ZlpR0nds0sh0wCkP-Q_hLLXY4-XV6ozEbH4cly-wQ-wOQcJq2lZ2czRIAcG6apOVD77HZlp20ncTORu_YkfeLDHcxDmSOKmmr6dKR-b40N5589djKNnqe9Q9bitPFBqcBE_Syw-HxrAWkKlQ5HvUOOtURjsWm3S41iQxImDyKyzjcsfcy4Mh5ls9kqi28z3O8nzbt-xi98UcwjE_Yfo0iV_qp8EUoPN7bTXR6rAYPU9JH0MQgnreDHcl4x8EVbbA3pG_Z9eihq_IOiCA80p7_OfdDfzBvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=dKFFgd6zPwl3K5QRfbE8ivSggYPQ7kWO2LW4j4jTjnN5pUoB0Aiz9gnitH7vwsxIkBgBWqaWfqm69mNLdEUmxqG7rDW9Fd14ASAeJmcgCsHJh1axZQBY8rKdjobbTrOTPIrPWh0uaPddRnOEI-rWnkTPGzdrbsF96f66ZjBtUF181b5Ttb9iw3rZasajiT6zxG1E-8WgEJIGKrkzbcZrFwIcrML4dnCD54QIo63G35X3OcDODWsfKyb3tYjqrYA_9lrWYW8HHsXzJCUvNb4G6-2J_iG_-aaCd_BZjCAuo02GwcU0KB6TCEssLkEUyFQXysfu-Wsx0rX2oejY8uwGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=dKFFgd6zPwl3K5QRfbE8ivSggYPQ7kWO2LW4j4jTjnN5pUoB0Aiz9gnitH7vwsxIkBgBWqaWfqm69mNLdEUmxqG7rDW9Fd14ASAeJmcgCsHJh1axZQBY8rKdjobbTrOTPIrPWh0uaPddRnOEI-rWnkTPGzdrbsF96f66ZjBtUF181b5Ttb9iw3rZasajiT6zxG1E-8WgEJIGKrkzbcZrFwIcrML4dnCD54QIo63G35X3OcDODWsfKyb3tYjqrYA_9lrWYW8HHsXzJCUvNb4G6-2J_iG_-aaCd_BZjCAuo02GwcU0KB6TCEssLkEUyFQXysfu-Wsx0rX2oejY8uwGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROhn94SEZyv4HnjMCc-nZRSF4J31D4_QmMeC2ZJqCdM11dUKnb_aXTDS4YdKlHGZxDGaUf-YJIr2pLw4lGOXsz90VOz-gy3S4iF9JyN2H4p7VLZ9ZrmnJjG64NLz1Z8McQ62NQznvb1_ahsP6fxogEqzQc7FM-7lAshe_IwuGAnQ2Ttdb-wa2QOzwAqpTe9OjnjHgOYlemYhpdrFOcPKAwNSHPalLGhJ2FtKJsIwIBmuH23_sfhlYVapfq_Rv9QzJxQDGSEZCprA5YCn3R4O7VE8FqC__1F4xViDHYwbuK7r1b7tB7CruJNmXihXa2gVbo83a39nWwc8dvWmOcHUVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpV2xrcZ2qnKJvCO3YQO_YNSBdUMutdyCXc5fau-d0KZSVwNcWhULJcx-gciZ0c4OyEanYTTl9c-1R68PksN7s5E1pHrSZlHvUIbx7hyCsAZDLrPhY-Vx4duTw5FX3bDZqoYemvnvBWvwU2bNEazcdYMsXsdDf_chFUm8ZKKmCsbF7-RXDJ3e4NMh7nYc5R1l_pQf6rlX9uEcU8tYjp2roxR-LHagdRtFFCz6o29154G1j8nptipEOJWuUkme9Hyrc_oFMeWsNGhkmAUN_ZPwHvhWN_x5gjLOreDIeQ0AJWeE7Hz-N7-cgdEX3Noa1CAFhOPiRpTyqCGXOpjeUQSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoQChLLmORuQyPUhuXvJnRiNs68ESGR3JKQtbWK8RX3zWFx6nf7dSq5-3Zg8wrI_29wrflVvfGOOf3Vi62A4-5qvQ57FyUzy_ozkXxG4ygBItcp23AH3f4T3iN9XSMWuiLS7C-aBYB19VDl4TB_NlvpKsoOILDGp084O6JwX8drAkpGeH8ICO82zQvkBWN4Kn4txAAuBZqwg4KwUcqMULiMKm1py-_czCzAyfvC63WAuit_Tq4hBlUP21vV2Ko2HBazXtrPj9CsrloTaZHppOhtQCeGUqigFcfbSKUPhmRipKpR9uD880LL0-F_IgNQfN9T2zXNohJBrUld6zHRRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXLNrSA9WabA_lSUIOjf9G3NF9gOZTWM7vxL037bMubnxeH0SYCaNUiRJ81gKzOaQO0dvwMga9w7ab-_YXsvUE03viqYXZixuXlKj83KOqfEXNn0YBZS1T_s8GqYhDGTR43oBeEpiiIajLNFjU4z3pBDLi6MgDMpLMjkFiBv0hHI7Y1JwfyRY5HmwrlACeKLimh0Ybmb-InocJUcJeyyQ6-eW_ckR5UZUFhaFxbSuTtePoP4IfwxRiyU7LlchD7Ax2eN8fckGSiEsaph7Snl5T8-lHb2Us9iBC8w1CArnodh4NOiy8YRPv_uaVsMTbhHvHzDVRPyRXffsfeTCxhgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=WzVBMEAZDFLJq1rM4Hgq46U50XMz7DEny75QstdO5Cww7uoNmusWzTYlVPZ0eLDBylAlTUy8I0YzPDAsow6_28cIxTC6IRnodNWeSSeHraGsU5hPVp4vDE7-_1SKRo31SpW6X2ZkdfNYKx7to9roGhzh3cw-dJ1S2BF3Rh5XoXavSoUktg7RJjI98yOo9gLGk-7R6TonuqmucoQSreVsUfW_0bqkWz-OpB3I-ZorzZIzNWKiBMZa8Fvk_ShhkSDLtAvE3zjGy800s2-MmIcMcQfhhP6bbhXvmKZLD5Ue7kjJv4mBiDJk2EAfj5Tjq7etAaLgeiXbuMl9g9d4NgwzEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=WzVBMEAZDFLJq1rM4Hgq46U50XMz7DEny75QstdO5Cww7uoNmusWzTYlVPZ0eLDBylAlTUy8I0YzPDAsow6_28cIxTC6IRnodNWeSSeHraGsU5hPVp4vDE7-_1SKRo31SpW6X2ZkdfNYKx7to9roGhzh3cw-dJ1S2BF3Rh5XoXavSoUktg7RJjI98yOo9gLGk-7R6TonuqmucoQSreVsUfW_0bqkWz-OpB3I-ZorzZIzNWKiBMZa8Fvk_ShhkSDLtAvE3zjGy800s2-MmIcMcQfhhP6bbhXvmKZLD5Ue7kjJv4mBiDJk2EAfj5Tjq7etAaLgeiXbuMl9g9d4NgwzEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDNrQRcflT-io3arzKu54yVgfWw4R_nLd_1hPTybHsNx_AWgXVvC3AYa9TlV2bkk848x4x-gST7sqVsFrP37D06NWO8B4158hCUzcS3_SNtl0WLWTCXdcT4OXRHAkvRsIPPufGfs8UJ8M04bOT0TfFuKfUHxciOXD40qzOBa_I89uMC9ZMiaOd-QFr5SfJlD1nuCH9Utt3wfPjI3XheTRSDDkjCLE8l52vjyIi3BK2-AUTb99zh8ObQvytgcyDSYxLh14hkD_Qa0gniknnt8nvIBHPI1ozrqDWlwfnAWSXme8NvrUpLrR5gEVfIB_EQ1kUss4a5875ZEhSpHLvL5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owb7HrW_6adHhlTZnMuEQihfAEQI-P46k4gNG5YOvxrcKPcWtZw2GG7SrX_lRYQYuUACtJ5QdRIwhWJUTTqRT6KDVap_4g2vwhmXksF9glHzx0yGEpAUx_M4Ai6w10xlJ8g4aZz-xuBa6VoHfqt7w7aK0jG9pwRNeQwLWA3_CSGbZjj0Qbt3IYlPnvsg9FtzgjFwVm9VIbic-IeFRUWaiT3FoQgzM2_ggiBd39_VPY-D_3EGQNqNJhYO7OnvnK27v7vKQZah53nd4ovYs-ya4NBeshKBAl50kiTmTiiuiQ1wJrS1Eg9wchdl5SPCPhnQmj8e2RaEPdfrdiIuzBIm0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=OpAqa96jGb3kqZLn4nHDgKaMumWctyNtEf_8iJt-13ibQGV6fcQMOVwToHuQK3jzjcKaIs1M-k0v9EOLm9J5TVmJj6e9EI-lOWiDuEyky1v82B4Lvbenrzq7xCJTA5hYDVi-ziDcnTRDgosREwZ20z59oaJbkJ-4nkprWpwbRCWA6eBu844hCFtY2sCQHqECpIUoGwfbx46DSpnlLR_2xmB_LjChTx3v8889c_JtGX3m8i4MClDM3Ciu0OPDdT0PouSFF_1kln-S-4SNBkmQXGRpBUERks2qqeTAlJHLmDSsK3Prf3zIecocmefxGyL2uO4hA1ynZFCRI2VNhB_4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=OpAqa96jGb3kqZLn4nHDgKaMumWctyNtEf_8iJt-13ibQGV6fcQMOVwToHuQK3jzjcKaIs1M-k0v9EOLm9J5TVmJj6e9EI-lOWiDuEyky1v82B4Lvbenrzq7xCJTA5hYDVi-ziDcnTRDgosREwZ20z59oaJbkJ-4nkprWpwbRCWA6eBu844hCFtY2sCQHqECpIUoGwfbx46DSpnlLR_2xmB_LjChTx3v8889c_JtGX3m8i4MClDM3Ciu0OPDdT0PouSFF_1kln-S-4SNBkmQXGRpBUERks2qqeTAlJHLmDSsK3Prf3zIecocmefxGyL2uO4hA1ynZFCRI2VNhB_4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWiy0duELxxs460Q7aEmvMpX4qpyBQ3OMuw4E3RCOyVR-Clt9w4ewjjKk8Jhet5-Wj87Uc9mqC6mn9XhUr7f3pxUQj1Kur2aByJqYpxFaYiMVCbzm_c_z1sET1dMy9Os2G8TFEnEQPE6s0IqL-AubySSI66u32nSMGiDEEaUQr8HFWcYYz4oVqJAt27oJ_XiO3-y2W1oVPgkN3qb2kEwfudagRl0DpFUKy9ODP-mblJL4NzTVpQXk6sCvFjqIr0aBUfSr6SnEhXZwYZPd1yL10a-ITkrYonvxvxnukEvQlmNbGZn95seRpBIV8eOlv_FNoys7SeRHzmB2xynDi8DyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgeUyVGuMZFsRRnrwRqBKAg_tdie0PoX6G5CJjIUhbgu-yoVx5doMnLkyCuBMiHCHAceCqpy9AmhOsAZOJtrbTM4pFzb2MGQ2WXgG6eOYO_y9q_J3WkwQ_2nntOnt7iFJyTNpOrPyPQymFxATfKmbgGLpuUgRbMBFaEv0P4YNqnTyfbpxPrUHic8LxDzOQdjCU9a2f9DeXf3F9IGVmPWIcBIRLW9vPAF6VS-mgX35ppoNHsegbVjHKL2XenhkGrn3bMl-JZ5bkA-E8RPIL93wp_0iOOPA5DQwEWH9nB1XVuarOKFCd5e8eRBrLjASr_Z5clp_AJZyihppUFHwVYyXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=Kkx8vBJhdDsB4Bk_IIE6CyrQwcWfB9pyuaZ_zo5tCuyXIudZQKXe65oHjd6pioRmtrvPU7w-qLxUoXSjI8aJ7ILUsvJJ3mfl_HQA9mssuygpMcWv4lAdipENrv20m9IP5w_UvUQoNTckKGJ92UHsBa9wpnIS5hSxGwLlBEwLcldTefbrfuNBAVaFvjDZfX4vtxlwXLL_GOF1Y4Iay7rPVRtrYG4kK2u2oXjh988FDYnXiTTAVGk9v2Fmb__eKXlPgU3wfrfc1GZFTDIIyZVHyorqvyyTLrjWXD__pQX9TPJ1HKLl9UaVinyo4gP9V9enxr41U16sjZKYTyOmpfAF4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=Kkx8vBJhdDsB4Bk_IIE6CyrQwcWfB9pyuaZ_zo5tCuyXIudZQKXe65oHjd6pioRmtrvPU7w-qLxUoXSjI8aJ7ILUsvJJ3mfl_HQA9mssuygpMcWv4lAdipENrv20m9IP5w_UvUQoNTckKGJ92UHsBa9wpnIS5hSxGwLlBEwLcldTefbrfuNBAVaFvjDZfX4vtxlwXLL_GOF1Y4Iay7rPVRtrYG4kK2u2oXjh988FDYnXiTTAVGk9v2Fmb__eKXlPgU3wfrfc1GZFTDIIyZVHyorqvyyTLrjWXD__pQX9TPJ1HKLl9UaVinyo4gP9V9enxr41U16sjZKYTyOmpfAF4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
