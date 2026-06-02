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
<img src="https://cdn4.telesco.pe/file/jIHNrJjaDHSiMTTl-U7W8-YEkEgFSA0KHHR7_Md-IYUEAU7VNqpgHWsraJSfe6bXEwP8hjlILrktoDLeaU-PmRnZEofvhzy-nT1aXMkKSjFKqFgl9Zig-p5lHOUhT-MASen0ndIEO6_ZN3LTSXNiYmwbwWcaDuh-GQU6LIz7a5CEelUowM9PzPBr4X3Y2N64WMa5O1270KC0WRcgTnNYvfqIUxUtdz5BVgw4LVP2YDW88CSsWgDL497xZ8HT_TqXr5ntq1c7ym5GuPnyaAThBzFjnL_caXqU0VfFHZpucCnuOoehJmjYoXPd-outwHQHueOwCmEVbBC_GItKo-N7sw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 205K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14e605921.mp4?token=i_oVP4NXlYOsiXFj8w-qy54D1bHX7pCmmZc2jXP7OlrCUUqvzRXYkAa6lIiERnhYYI3kd1KVEWciCnTsmri12O2uiFz7sa4fuNLYzbgTYyzVgP5WhMUc_hOZvV4XwbsHV2rxr5AmFSBH-H9oW-u32SaMrJvLvm1rQUbLtQwYSiPChg3vj05YuSjBsNLEztOxcJ9ikbKCcFzui0fZfyY3PbsqC7kzKXnwv36vPWMCZdOyGaU2fe9N0iDD9jqNk4DwHjOjE72UwERreZ_ZoVn9MhdyBcWxpLLnMM6ri1kogZ1VSIMCZ436PaATQotPQwkpcK9RryZfouKRc5vb7HWrFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14e605921.mp4?token=i_oVP4NXlYOsiXFj8w-qy54D1bHX7pCmmZc2jXP7OlrCUUqvzRXYkAa6lIiERnhYYI3kd1KVEWciCnTsmri12O2uiFz7sa4fuNLYzbgTYyzVgP5WhMUc_hOZvV4XwbsHV2rxr5AmFSBH-H9oW-u32SaMrJvLvm1rQUbLtQwYSiPChg3vj05YuSjBsNLEztOxcJ9ikbKCcFzui0fZfyY3PbsqC7kzKXnwv36vPWMCZdOyGaU2fe9N0iDD9jqNk4DwHjOjE72UwERreZ_ZoVn9MhdyBcWxpLLnMM6ri1kogZ1VSIMCZ436PaATQotPQwkpcK9RryZfouKRc5vb7HWrFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔝
دیوید بارنیا رئیس موساد:
تغییر رژیم در ایران یک هدف ممکن و قابل دستیابی است. این یک وظیفه قابل انجام است اما نیازمند تعهد، صبر و فداکاری برای هدف خواهد بود. این وظیفه باید در رأس اولویت‌های ما باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=eIg2RWddJ4l1MogXlXl6cEMuORtsGobvXRcopA38uQZTjNcrrZL3okCqVrUA-iUVuAQeWWMTd2n04T4bKLEHwRyIN1YPsb22Q85kLGvdK9OxJGNXClFiS5h-btOKw3yxmdOqBjsMCfITP-yWO6WGvzK_cGG6mkXO-gUXqk_b9ArSoa-deM16zYCgK5qUOCxfir4OnwRZtOgagI-Md19gH3MEK43BAh85IBslDVTV2K7mWvzWIpT3BltfOrAiWzJc17LiNNS7o6dItYMIIO26lHoAORmrYxM2K4rfyrBAaETm-8nF0KnUqxCfYEXCRhQWIRJlN10OwvfGhHDejusGhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=eIg2RWddJ4l1MogXlXl6cEMuORtsGobvXRcopA38uQZTjNcrrZL3okCqVrUA-iUVuAQeWWMTd2n04T4bKLEHwRyIN1YPsb22Q85kLGvdK9OxJGNXClFiS5h-btOKw3yxmdOqBjsMCfITP-yWO6WGvzK_cGG6mkXO-gUXqk_b9ArSoa-deM16zYCgK5qUOCxfir4OnwRZtOgagI-Md19gH3MEK43BAh85IBslDVTV2K7mWvzWIpT3BltfOrAiWzJc17LiNNS7o6dItYMIIO26lHoAORmrYxM2K4rfyrBAaETm-8nF0KnUqxCfYEXCRhQWIRJlN10OwvfGhHDejusGhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز دانش‌آموزای تهرانی در مخالفت با تاثیر قطعی معدل، جلوی وزارت آموزش و پرورش تجمع کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVZvvDHgZ5Jwg9yTDpv2Oy17aG_xBP9Gm1ZJWf39Xv-lnrO6BK3pkHg_Fd_XMwSBlC8ow2N0PGZ8Gx3FhUGvjUHOjabZA_pRAg46Js06RQBZqj3MSiRmfsIzPBxA5Uqqg_7wa9gJZgq2cXj_8vjWErLVfsilbakvE3yrfcr70CI9pFYDrA-lcR8mEEJKs199nD6g4_lSzU8W4jI7vr5-QClqjl7zORTrh0DturiTvfS5JQgkk8MZz-ZvYDkJh2d4hdGwHKD0SwKSVUahpibDjIZ9lolb62sXcgA4VrGToiqjV-x0mj6x--WcBQdNnHqcKs1vohArfccDf-0Y-oA-yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
روی بهترین مسابقات ورزش های الکترونیک پیش بینی کنید و برنده شوید!
🎮
تنوع گسترده از بازی های انلاین  CSGO, DOTA , FIFA وMORTAL COMBAT ...
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
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=q9m_XUUh0k9T0-3X5RiJh6fbIHAmuF2xekVV38alOFOfE6yp7Hux8NyaGb0Q80qgSWViX1II80v0-s7_i4BE-k3anbxOg16SJVvgZYknp3R681aOQdEITQAgcq8nL_TqgPjeTYD1c4srB0VDIQ6IiY5MCDvTO8rd99tQqQRMgDRCeaziqZHGo3xsaz1VcJJvJWYPAG0D8xdhxkQ-yv404XuJKRadB7RCX6ksmooDxGKyfRNUWF9QscUxGjhzQaPQ-yPlz4NJPJa_Sis6BFxSPtHf284VUZG0KSbHnH6I3rPzh3cC1lxspvWrgL-19atEdVSYcegc4PcPjvOxcxOr-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2d6ed8f2.mp4?token=q9m_XUUh0k9T0-3X5RiJh6fbIHAmuF2xekVV38alOFOfE6yp7Hux8NyaGb0Q80qgSWViX1II80v0-s7_i4BE-k3anbxOg16SJVvgZYknp3R681aOQdEITQAgcq8nL_TqgPjeTYD1c4srB0VDIQ6IiY5MCDvTO8rd99tQqQRMgDRCeaziqZHGo3xsaz1VcJJvJWYPAG0D8xdhxkQ-yv404XuJKRadB7RCX6ksmooDxGKyfRNUWF9QscUxGjhzQaPQ-yPlz4NJPJa_Sis6BFxSPtHf284VUZG0KSbHnH6I3rPzh3cC1lxspvWrgL-19atEdVSYcegc4PcPjvOxcxOr-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
واکنش یک‌عدد ملا در تجمعات شبانه حکومتی مقابل یک ماشین با چند سرنشین زن:
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=nlT1eNFgJEGdsfYKNm0trqdWNKnvLWmdQf1FkMPUWuiEfmfAyVSGkYDGZmaHGBU3_ntoPzuZnrs75I3lSlDkAJd2ke1oJWgLlRmCqTGBogX5AOSFSf_FTJ1oh2l-bh7wh0AWiWknWNalLJI_M380MwkfdE9yd6mnHbzGuKsTZTmu72gLCeW1l2wYSdYhyNooO9c4SxDsAg5gIHlTBmlhCzekqx8CAZ9cCcxHIZvDPXK5JdJh4EJXE1nyORaQMIFHD02xqeMbelkZnlFClTK37xrl4hOBAqAPhI_WcGQIgbITdvUVzW6sA6l-vkNEuUrcQdAYoQXvguvNoK42_3L1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e2983c9bf.mp4?token=nlT1eNFgJEGdsfYKNm0trqdWNKnvLWmdQf1FkMPUWuiEfmfAyVSGkYDGZmaHGBU3_ntoPzuZnrs75I3lSlDkAJd2ke1oJWgLlRmCqTGBogX5AOSFSf_FTJ1oh2l-bh7wh0AWiWknWNalLJI_M380MwkfdE9yd6mnHbzGuKsTZTmu72gLCeW1l2wYSdYhyNooO9c4SxDsAg5gIHlTBmlhCzekqx8CAZ9cCcxHIZvDPXK5JdJh4EJXE1nyORaQMIFHD02xqeMbelkZnlFClTK37xrl4hOBAqAPhI_WcGQIgbITdvUVzW6sA6l-vkNEuUrcQdAYoQXvguvNoK42_3L1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
نواب دبیرکل حزب باقر قالیباف: آماده بازگشت به جنگ هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=mmPcCkPdnC_pMKeeDK-192HrGpp7N-JOTd37W-Afd8TIg-xYoOiv6lEUnvjZJ2rbhKqdHgJpPErlQuC6Z82YolVI-pW-Z-rDVM5azV6nWk9QYR9X3KwP50qZmzsO0OYZCi-rf-HVXmidb-vG9ogW66DZwHmbQJVpOo7PnSLfZaFpDBOSCcDo6tG4nfcjv5MZ86wAXXrHvxJ4TwNSSWdMcUZqehdvTm0p2aCw8fq1MhNsJqYifsS1qLAD8NzcbswFRUpelpHYABgy8pT_t9j4r3-tpw8N16cy9H1jdPkKEIAqPF9JT5r1sSPrTOITZB0R_Pd21PcmJJmmtKEreXTkCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=mmPcCkPdnC_pMKeeDK-192HrGpp7N-JOTd37W-Afd8TIg-xYoOiv6lEUnvjZJ2rbhKqdHgJpPErlQuC6Z82YolVI-pW-Z-rDVM5azV6nWk9QYR9X3KwP50qZmzsO0OYZCi-rf-HVXmidb-vG9ogW66DZwHmbQJVpOo7PnSLfZaFpDBOSCcDo6tG4nfcjv5MZ86wAXXrHvxJ4TwNSSWdMcUZqehdvTm0p2aCw8fq1MhNsJqYifsS1qLAD8NzcbswFRUpelpHYABgy8pT_t9j4r3-tpw8N16cy9H1jdPkKEIAqPF9JT5r1sSPrTOITZB0R_Pd21PcmJJmmtKEreXTkCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
درگیری تن به تن نیروهای ارتش اسرائیل با حزب الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f218bec310.mp4?token=veCPnEUV4cpojdLmHvthy0yUr-FpRbXGB6OeqaOszyHrzUmZxDAE3C4kpxw3DLayAl1sPsJXVgGhrceulvf1BH5s4CRvf6C3xIUyUhC-hCBZTwyhEQg4NEaNXLV1nK6MLOMffnyPZZNTdqyiIyqsVMXqbfIAr58Au1dOzhWHNYInNLTD9whICKZcBlKxT8XFn4VoWNzjN1AHa-xFtT-5otEsovDHtgbONSoLYfe2wCNzIv96HJP6chz9ql5igLCtCc8QKbgrl87fRdnDwDYSxOzKiorkt89QVxbaOYq8HJoLAYF4CpV1679bSd5EHCycMd-33J2aN9J-NAWBus8AUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f218bec310.mp4?token=veCPnEUV4cpojdLmHvthy0yUr-FpRbXGB6OeqaOszyHrzUmZxDAE3C4kpxw3DLayAl1sPsJXVgGhrceulvf1BH5s4CRvf6C3xIUyUhC-hCBZTwyhEQg4NEaNXLV1nK6MLOMffnyPZZNTdqyiIyqsVMXqbfIAr58Au1dOzhWHNYInNLTD9whICKZcBlKxT8XFn4VoWNzjN1AHa-xFtT-5otEsovDHtgbONSoLYfe2wCNzIv96HJP6chz9ql5igLCtCc8QKbgrl87fRdnDwDYSxOzKiorkt89QVxbaOYq8HJoLAYF4CpV1679bSd5EHCycMd-33J2aN9J-NAWBus8AUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
وضعیت عجیب جنوب لبنان پس از حملات امشب و امروز اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r889RVM95CtCiSE635dIcEPW-AGz7nAGtjH9PUgyGLXhPMRw9vXVp3y8ihKWLW7HygpH4pTpNcYUXqFte35Pgj6rUXbOFV9_Gkst34FUZZdk_oGHtFsxop2vejX-k-TOig84FXEbGsvulEgdf4k3Q51JXtEw6PewM-jBbF2UAdP8C1My_yOTs4QXnq9LsHI0P_w3gatL1wG41bNehIjOHRLqmZOXbYBM-5JmqEDZXWC_3784Gtlc89h7Pfq8BXvbpk4nE1fZWXRH1C4udQoJqnJMvlIzpVdjTH2pnZDm4Wa-HNU7MeU_XWsZ4hLWQN8KCf1LOUMBr7PON9ye5dFApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mfd7Ayg99IpKPzw0hSnokEOInmZtlSLYjNJvY3wXSULg487aMpOhg7cmnv-ZJSVq3a4KYHA_KXKwnpKEiJOLaZ6unQP4EM9LzEU-st0UVdoU7xt9ua8Pp_TNGsSDHPzf7t_CBPlPaEbhNjf7Luf6gcZNcJOu6HRWfr_qYhBU3MigLbKdxV8C98FeGIDduBQz6ciTJe8GAJY642Jfuls6tscbSQ-AJ-1QE5r5FpTpY-qx4oY5nVF3ndbeRSPr_wtxMbfRGnvHArtq5Wtc28ruTMuLMho5GxR8dhdbaB3KOwg-P3vLk7wfb-0d3TZs8jFE7jJ48trkkn2lWA4SqmeI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCRfN4yL7UMSfQKN_xBXzfg6n4phYcHswP_ZgeZeCdfP55P-84_CTU0B-53nXLZXHmQ6Ff39eSbAydVJZqTIJeMLGxyqy91Nq0aFJNpjJ_K2iEYL_mnxy0P6XleOuzvVBbSAIRCeNN4Otsq5wlmhe9gHKZQJgwC-bcDCGtOtj3ibYDmI2Y6t0OdKQP3sCQh88a1rMOn-TiBOEDP-XJS9qzgLG_gPixkJeOejZ1ArdEHgHOgW_zTadH3q1htse1UmVvsUUSmgLgwL2rPqfDuumcLqCjQ-_-MnhyOfNoIHkTiFCSLT_Pn5Eh1HdnyruQ2DArgakS16O6OFpRXrWO1u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HKguuF7--CRyLFvjw1K7oqpBt84N7hqM66sbRZCysg_D4s2Uo4KKIsF3x_69HMws5_JkiiMC9kwYY_VCyryFQ0THKupl6xO6sfH1F2rvHDmE5REt2geXvB9O7_QBmBEHwqp5gul6K3DqUCzCC-dZ-J2igknP4uN7fj8T_KiMi4E8amJ-EK2xJ8LEdRip3fY2NXvefczn1O0QYmVNlGddI-69oKwBz66q349Kafxxl2hvSPOXEP2rN9fsVQ1lnkTKqXnfNBoSsq85DyHUJz-4E005VueO329f2ZZZPlJZl62EUTHNzSHplacrcOC_YRaqlpxiLPBzOuozFxyfmb9elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyKnq7Y2aJsZyj0nPJpNAbod-nKoLUTcazkLmPIcgtN20Mp56KmcOsNk6XCxcN3YYhIYJ24MvccZYyPp5K7cS9BfWi-njxYTsDEIAEKbTla3rP8oqk48qlEENwnuh8KnnI15QFb1ZDuPMmfltuoG24bBTDL2zD1FUvE63cUQlLc2PfYa1h5cEIxPmLhr3IhCy_ogObcAABzdFJiI_a8CAt2IbmRCBWyZtORWFHYck19ixMFMDTS9ba_XzB5oVeySiSkq77IO7i8fcX1wIhcQbl1HsWvbXN5nnB1spZHGgKYRWtMmDlkx7a4R9OAb0b9iityfmsHfBxcBMSi_-JDBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3xSzT0lg8HzWxemYwG0oihUTwpo_PlUxwXafOij8XXaGkJqpsdyjoUtoStEKJwezEQ_GS2dvy_mCmncau0vpwQK6lnxyQ6tXWXNjmwwkg1UV7xFqwvrCgftujfO0k5y85M-GMr4fbt8IXHwHdblPWT2wPWcjiuyBX_cHiooxNLMDAFGp4E497X1s5GVPBAg_Afgiszp-K7HMJTPHB-4fzqCgl_P2hih-F5M4cy4D7Kh24M3TV-qcmW377OVS5-Clh1gi3pT17tTJzDCwPOV35b8ocpGI-jbvXsreKfuNbecQVMn2CLyoByPHL7WkLKEW3C1opt3DHOCAuO0WU6VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhxllV6SEUFYM-NeBUqKJxZE4c8pwmEp92fFJllfEIyn8GV6xrfRvkcFPeBYP5pcdNQtYSjfWXuV3-Ha3_rwcBPNBOap3glSkh6Aei0tzn1ZTc8JlmlcAF1Qq4uOfqulb6KseZL_3Js6Pr0msudJtnttNsmAEpEXBqlnIMfFamg4ppXVt37KNqY-tDho0SOWhUdTkNEjGGLk-vSUMVAVnhtdyjbj0LuQ4z_zWD7mwMmL9L1F76noq-YqNPmbYBG3BZ1dZSRXOaq4ntFtnJs_HjPieuddtm-mmhPqWjKYtifTSlaH3sA1HH8K5jchKlYPzk_EA21_KU3mdWLmtgz47g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjUigbcdUKAFwsqR_BPh-PC6aQZW4kLxhAmCBTDvmo8_s70iiA-Q-JrFbWwK258bLV2HHDYbUK7ZEufPBnq2vAvlALFIE9y6L1m3kR8IBVR_jwSL_koj9OpOkBOB2HOO1k_WasDDAT4x4KgUCdIuW20B5U8FVu5-ZE9gfNP-ARtqytN4xCE1wMAjAgk18569fIfUaPcn8Yx81a7fF906kaWQaDhbpO8pDKtyRetRwVDSFE4J01x0fGk6PEy63B-fKusYwkQ971FSTzYJw_RDpKnbMDbF-TT93Dqx7CfyMtGOBHZ3RGvYdNboYHN3zQCbhmmuzI3rTk26SWtJSnzCmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CITB5Dq0KRKYet24iiZcPuzjFXN4G8oGkn2Qd1CgZvc0-YrUB9Ee0dEyAZ87SnqTEQEz2Qq66P4MvieFh18C9HOe4Ngr_64fARxRlNHLXlOzp88y_FhuhPnA3YFKXecYcHZdMeJQCbEtf60XsT7_8qtXikqGwoMryXoJKooynDVTLUAnJjbvrpWoiWIqGV919edsbpLG6rCnpIC4hzYWu2xM0hPp51s8G5HT99ABuK9I9BlxYCEJN4G53-w9xvx7hfcZVxMYm8EnFPMlEJ1txeg4eeeg67mDbeO4pw95NmBsHPXyEXdvsb9ulLmG9E9QJDeJhuPtc0R1rLvBQibuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=eNYsi_8fCOTTafPqc0LaHX5jLfxR-qj0gIIy_kCCjEa46XdF6lm8yEgxBUTgyZ3skGVomPZyVfUoPkMcDkz1Mm2svNARKnTErO8HIE1-cBz4xnq0_xFkTdGH5XyqELJ0M0Xz5_ELN5UZUqiFsMx7DLCe7otxotjpEow5GUDEj0x-2RuMGJXR_nmN4icbpNuc9X7_gyNTJAKG6eKd5ikl7meqiKRAayT4TVecQjQc2oXW4QunuUPuCeUIeaQbfUzRJT0XOR0yNYCrRa9V-9otn6ens8VpyQza-Lrp4IpKZEpVA-neLdrIDv2tv1eEfdUws_lI645IVaANR1Vf_86dDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=eNYsi_8fCOTTafPqc0LaHX5jLfxR-qj0gIIy_kCCjEa46XdF6lm8yEgxBUTgyZ3skGVomPZyVfUoPkMcDkz1Mm2svNARKnTErO8HIE1-cBz4xnq0_xFkTdGH5XyqELJ0M0Xz5_ELN5UZUqiFsMx7DLCe7otxotjpEow5GUDEj0x-2RuMGJXR_nmN4icbpNuc9X7_gyNTJAKG6eKd5ikl7meqiKRAayT4TVecQjQc2oXW4QunuUPuCeUIeaQbfUzRJT0XOR0yNYCrRa9V-9otn6ens8VpyQza-Lrp4IpKZEpVA-neLdrIDv2tv1eEfdUws_lI645IVaANR1Vf_86dDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDFis0ljxsPperT_njeP5wuOpbxmGhJKWf1_zK4VyAYfrBiQtfPHjOF0oJuHWySi_Gldam-pUNAFq8VzWsTQfdpbECpKDMLsMsHLYeJsfPeimO7LFVyxQRzPVlTsh_pzXPjBZhetaP83ObWnF6fMDRoCJsA3daHUAlWBbaS1LTsyDAgJsrLdHSYv5lV2fxhpU3ewlqo-ZLi0AuoCK0dVI2ylSlUQYfjRL9zCVslGg9S_3Dv0z3kdxpT20HbcxQC_At_eTZcL34uyVu4YpCLTuJCubvCGTpzWn3fHJGcWUU7Xt-wmdmtHyOMxH_oL9F8B3YwVWKv3okMK0OfgqkY62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce9uHeROK8bJYDMHpxKkMoQSN-lTYIOjKdbhK0P9BnodheuGGymN3Rbrdl3DxGN1P1iBkg3pWLGK9PuX7eLuGcbysDJiRmwIXSlvhXVMP7lmBp8e-fbFcM-d_NjX7Eg2_cfxesO0WdA85yRzOOszuNNLpuGEqe4JCbD5770ewOMibUr882F52fliZNist5-hpU3I9Nh4V-D6DqQqfsQ3OWfpd4Ix0lUqiUjw5iVQAa9xQVsSH27n0poA-9vRhx0xPko2HFXSXQn4RIVN6vYMH-Q70DchSVDUrLIW6O-q7Pn2RfdaoGIwd35JdbU_q9mHS-jCjeVTdMmLOCcaPXX1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SG9sVM38ENXMAOjZeZgOex6xtw4yUUSAWzs806YBValtJLtYoIOyrO-4JSDw9EpIo-0Pvfw8j0RHFvMMc85VZGilRim2F_Z6dzkhNnUdIZ5c51zAvpSRbN4GXpcYoYuNgFfT6_dZ59Gqedr5i635RE1CqrkbWoPU2kNBsUsNJiNMrzCv9jt4CQLPTlRlfSJsB7tQG4NKp_luzPL_VgP0f4_UXIieoge3jKGiwJWbOjWgy9UGzg9wgfs_864_iPfZgk_h48w9CY0WWNsG7B8BQGJICBY7WGq30PbH7S0UzTuWLyBK3Azn3pXz3ESH69WIUlUxgE7lPaMdMXNnXozsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dduARpSxeWhPgyRnGaH4qkIe1xCyaZL0dcBKZftWpeudUGVMcjuuUpjncjwlMwQDSzjNn50fglOQ3DD50kdmXLfMSM6Or_ZEHvivyTOs4hPbCpHdWS9MqM6Jzc5N4ezNEt8qfB1D_k4boxVx65bvDFToAYQNwivSCTn0BvwyiBib1SRvWK4K0DHlxnrawLrttRYEkkP66hWxk1H6mArDBJmNzZ5QjxZFLtJ97iSt8VtdqBVMrtylK9FFxhVgWYFummjQCOZ7JSidZN5MnYD5RkEpKPQrgFaBkvl9REUYbWlxfqZvNmk7b-svJROA9ADIc0r3WzuU8ydsS5Akz5N3mA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=gEj0YIQRoo2LjyX58-KkFAx3C9Q2gEfUzAz703sW5sdC6wuGCSh0AmoxcZOZl4JEQ4wX7U5fkLySbansbkpPzQsnPaeFKVYS_79aN72-3zTD8PXug2PDgd77K--evbGNmlE9oZZMLFH-0iM1U1QmfyVlNjAM25ErLHwSSE2xMn7F9AUGGrhlUoEepVkFZtKX8XJFeWE6HbOT4J1WGCXTsq5dNjJaMl9chDWjSMSFt_99jewWkTarpiFaem0tAUq7-ZAvAWCfbeoveJx2x8afavCpt28eer9j-h-pv8_S1LM6fJ6p1B80TnJ3U64EjGzIFRwDxC03NwauV9WXucaJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=gEj0YIQRoo2LjyX58-KkFAx3C9Q2gEfUzAz703sW5sdC6wuGCSh0AmoxcZOZl4JEQ4wX7U5fkLySbansbkpPzQsnPaeFKVYS_79aN72-3zTD8PXug2PDgd77K--evbGNmlE9oZZMLFH-0iM1U1QmfyVlNjAM25ErLHwSSE2xMn7F9AUGGrhlUoEepVkFZtKX8XJFeWE6HbOT4J1WGCXTsq5dNjJaMl9chDWjSMSFt_99jewWkTarpiFaem0tAUq7-ZAvAWCfbeoveJx2x8afavCpt28eer9j-h-pv8_S1LM6fJ6p1B80TnJ3U64EjGzIFRwDxC03NwauV9WXucaJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPr9gVmcUi-MlSQadogmJXMeY2wBRUHR1YUYXj8SeWZGSuwbe-eT37o_8nbh6nbIl4jMIoaHFsAbhM4eQ_FGNvRIZTNwdXymi6YaBdbudiALq1leO81C0t-B6JrXQ8Le-mOhy4TMY84a7TkWtmeRiNL8tcQ-mqe8BK5DMX_TRnyyNRu_3_ijkT7JVNoOpmHwrFMLDkr9FT__6kff3ert_8ex2p2QjUMUkusA9cfQQC6Z0vtB8aRrFWghL0Pt9JpD1JG804iizq67IveBU0Vrtu9KM-_GHyxhP88c-SC7GHxC1Ix-65AmjoTLVK2MwgeRpgZ9KJ9TIGr2eTfaczaoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=IGMsCFQOXcuc3vO3PQKfyETXvx9WQJwoBtlIYhVlme2NhCn7Cd3s40ugmA-DztRooVOgB_1KxPJqfrQdzfT3hYtjHvlzLseJ_tJN5Tx2MUNF7oi2FiG_SyhlvVFWchtJPlV8DhZPJsnZcqdYrxSLb9xP8MirvjK05EQ3f-160MBIZbNnSLjQFURRcr0AZHXYJqsTu7aVJGgmx24CkalVFvAY5noEWqVaKHAzE9UpqOmESOmxN1WnRg1eHXe54MGw5KIHwYxYGqhlDddMf3G_GhhEx3RX-fDSJqDWmtddNaz3EAnAluAddOTYlygACQwJF1aYulp1kynh1bJCrCFgZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=IGMsCFQOXcuc3vO3PQKfyETXvx9WQJwoBtlIYhVlme2NhCn7Cd3s40ugmA-DztRooVOgB_1KxPJqfrQdzfT3hYtjHvlzLseJ_tJN5Tx2MUNF7oi2FiG_SyhlvVFWchtJPlV8DhZPJsnZcqdYrxSLb9xP8MirvjK05EQ3f-160MBIZbNnSLjQFURRcr0AZHXYJqsTu7aVJGgmx24CkalVFvAY5noEWqVaKHAzE9UpqOmESOmxN1WnRg1eHXe54MGw5KIHwYxYGqhlDddMf3G_GhhEx3RX-fDSJqDWmtddNaz3EAnAluAddOTYlygACQwJF1aYulp1kynh1bJCrCFgZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-tMAByUkaj1ILQ8IBP8ryb93TLfVqZ1NlmVBlV12p3Hnn9mb9gaQt4-PPA5MJwY2h2sHmVlbejmZGp494DPrv5FhGBOPDny08po-ofXYX1hlJ9O5gjxyGbg4ntVFIaR6TW0wi0IM4BgGP0cq6sZwau-FB3HjHBreKLddc_460IIVxV7nTmoWW9IwJ9r9PoyWD9WJ7NafntRXP1cgTL9xdXbTx9PY19LnpyIEl4X-PZOQs17FVHZFWVnpvx626rql7vLD4HedeGCSxZj0FFW3kUDRllXmuRzAzQf0hYol2hTkt3tTwhxyFv_2ekGkAh37EvXnHwSyJ9Smg2yGf-VSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=ngW0xNfFAqnEUc96hfI7VllDGm8sjPEQv-yttq_0uTO6yDE93HNMY_poEuPwUUekYPAKsIbS2Wygs2ib1ivvAr-8VBJCbNL0A6jrcmytBGzxK8AnsOW3fqL-ZohxoAmdlBO04LJS4pDrMnp0nJSb6ax9jWQlnYCx4zIItId2JQByxqK7_CEc0hKzrxDsdQ9yKiuLl89KOFJ-vn3RO3G2lKPi5NpZs98UuKh9xS2Kw5unWxKozbnqb20RX2xikC8H4sRLzHf_RMr9Pv1p_RhRlnMqFjDSdaxmVSEi7gps56515n7Qa2dmIY39YR4-gwea-MGZcHVdZp2pKfvLUngp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=ngW0xNfFAqnEUc96hfI7VllDGm8sjPEQv-yttq_0uTO6yDE93HNMY_poEuPwUUekYPAKsIbS2Wygs2ib1ivvAr-8VBJCbNL0A6jrcmytBGzxK8AnsOW3fqL-ZohxoAmdlBO04LJS4pDrMnp0nJSb6ax9jWQlnYCx4zIItId2JQByxqK7_CEc0hKzrxDsdQ9yKiuLl89KOFJ-vn3RO3G2lKPi5NpZs98UuKh9xS2Kw5unWxKozbnqb20RX2xikC8H4sRLzHf_RMr9Pv1p_RhRlnMqFjDSdaxmVSEi7gps56515n7Qa2dmIY39YR4-gwea-MGZcHVdZp2pKfvLUngp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=dPc_PogRDJQ2-pGF0kA5ehBnarNy01LCHqPQqUMr8xmkIRLw9GgnaKF1hKQgcgVUokhswNHJN8tg91LTGJg1egebuojIAp7PR7bl4iW9pYO0tN8gTLX1tB8Jji1l8nx3klDlChSaEN2NmEQH78UuWbFc7MdKirzOSl_2PVjqQe4XfIN139sB_s9C-C9C4rMEatFZAOWzc77jPOPPcni1xVyPiFQl28H_9C8vsYuTv7MdbRdZ_mMmIJa_MueDW1SDUfr0ZOJHp0hPF_P9f_YbS2OQc_93lHtFIVjm9E3mUsGO8v4Mw2cCkbH8Rj287bzc9yFv18A_bS3n6rHVrCewYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=dPc_PogRDJQ2-pGF0kA5ehBnarNy01LCHqPQqUMr8xmkIRLw9GgnaKF1hKQgcgVUokhswNHJN8tg91LTGJg1egebuojIAp7PR7bl4iW9pYO0tN8gTLX1tB8Jji1l8nx3klDlChSaEN2NmEQH78UuWbFc7MdKirzOSl_2PVjqQe4XfIN139sB_s9C-C9C4rMEatFZAOWzc77jPOPPcni1xVyPiFQl28H_9C8vsYuTv7MdbRdZ_mMmIJa_MueDW1SDUfr0ZOJHp0hPF_P9f_YbS2OQc_93lHtFIVjm9E3mUsGO8v4Mw2cCkbH8Rj287bzc9yFv18A_bS3n6rHVrCewYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=kaaFhrCfhRrqV9bMVxqMHKEtlk9dR9rCesne_-obAN0RbZPgpv1eIYqBFxE_hoqq5NstXr2ryMlpDZpFU6j_TOW8AVjc0gsPeZ42LWjqGqMAmpQKBlXLQxAYJMklCK3hIXwaX43tQ0_HwmYdXQ-Gox4FfOlQfowVcQw_qsxj19BiQmvBJt9P23AddxtDEQ2R7IbcsxA8PFZtAdSLvjiNNi7pyXj-SgGdhj38aQqJD59iGGAz73ZLOdyFiy3nhElVWOMSPPVDQEF9xInJL6KqrpjUi5CUuyNxgI67Vc5frDvzyKrmKPkF73h4CvGQx_-YdR0pfx8zYfNeP7FTWniZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=kaaFhrCfhRrqV9bMVxqMHKEtlk9dR9rCesne_-obAN0RbZPgpv1eIYqBFxE_hoqq5NstXr2ryMlpDZpFU6j_TOW8AVjc0gsPeZ42LWjqGqMAmpQKBlXLQxAYJMklCK3hIXwaX43tQ0_HwmYdXQ-Gox4FfOlQfowVcQw_qsxj19BiQmvBJt9P23AddxtDEQ2R7IbcsxA8PFZtAdSLvjiNNi7pyXj-SgGdhj38aQqJD59iGGAz73ZLOdyFiy3nhElVWOMSPPVDQEF9xInJL6KqrpjUi5CUuyNxgI67Vc5frDvzyKrmKPkF73h4CvGQx_-YdR0pfx8zYfNeP7FTWniZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y2yGBADES24p_l8bDahGf6hZVJ_FuVTqcQ7GAFDz_pNy4GpprrFxGbRLtUSN8Q-qjliJFhiBfdgPtNkCxJP4_2WDTOun6HX901HsbeBT7JwvamQf0AK8_gvlpwz2XyTeoqa1karWyIrv3_JdfJMIvDjXhlM7QFTUfDfWbK-l5tHAt2_gdHol94cFZ_gyHD87jlssw-SzWkefZpynbmvffkmMxY6NsJVAdRXKWSkXwE_nQZ41NZY0t08c78b6aIrEUI8ty8LHW6IBeqeKNRyWR6h-Xf7GEhZM4e294InP4M9Q664CkPKQy7SQ2cVt0qHSX5lTfjhWKilRK2PNP5_R0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mrP4JUM5xH-fTijV5rRD_0691H8x0aSbAU3jeRDAQJUwb8FCrQGowXwW4pnNigt1DY2DKbAA2PTI_uEZcV20uNOLWJBLwwfo1tF8cHTM8OFt_fyVTbLcU71RFdmq_3FvN5xWlLEbcmhW59sXE7nYYK17hhpPb03M1sePX4kH236vrTaU0gCEO8179KLFZk64GGJygMVACryp9UKIOmuWZSJaOGH3YvJ7a6Ybp0w5UawQZh9DxehqrR1BjDUu1FmVMqoEND96_31oAPWuYOfHWq6W6unmuhGE8XPJpWumMjxNKDGzO3WoGkEEmoScua0fQKIwvrCfDCuilwId1qHwwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=W6t6x_6XvqWgAkwNR0EU1HJxhEIf5-rvugyjIuDTIwwOr6spWihSMkp9ojNq9fRWv0VWM0zZt-Lf3TcM88SS-0cpEy3hjbRrGWYGKsX1e3DgXifN21xb8cCKQTRfzjw-vHbiVSzwvEY6Rhc8QceEzUTurUUv5XPdnoYNMwmfsS0lUFvbS9NK3qHv6XuOiUymLhJz8jM_UmY8JoqGFBlR3wWTWFPkfllU-l0FdiNHJNl5RXbZDdGZnwXjji25YwR6QYDLJcIxliiaiUGo3RuZoUnc4v3pTCHPzov4uEbJWhAAi9qUtZLJf3nZb-aawDmsmScVs9xNPr0xH1JgQ8GxJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=W6t6x_6XvqWgAkwNR0EU1HJxhEIf5-rvugyjIuDTIwwOr6spWihSMkp9ojNq9fRWv0VWM0zZt-Lf3TcM88SS-0cpEy3hjbRrGWYGKsX1e3DgXifN21xb8cCKQTRfzjw-vHbiVSzwvEY6Rhc8QceEzUTurUUv5XPdnoYNMwmfsS0lUFvbS9NK3qHv6XuOiUymLhJz8jM_UmY8JoqGFBlR3wWTWFPkfllU-l0FdiNHJNl5RXbZDdGZnwXjji25YwR6QYDLJcIxliiaiUGo3RuZoUnc4v3pTCHPzov4uEbJWhAAi9qUtZLJf3nZb-aawDmsmScVs9xNPr0xH1JgQ8GxJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=SG7v8fyXCi6tXG9YJQdAUMeWIjLjXUv2-uPrOkdQeVqwi9rixDa_IDMZ_cwngo9_mF_qKho0Bhggb14fWByCTCc13cXpanBHwAjrWjOssHT5FcllkKMUF_fpkuQ36s3GK3h8uxKjXCMb2uknfVcXRhgAsp9KY0lk9h5m18fA1HLwLZItNee1llXTRoctmWSfdgORBhRLtr_xiKugcF10DoI1Onc0x7uc26sqS9b1CqFgaT09BWjWVcky9q4lKrcjeTK62V-hrc5hv2gfPQ2ZsCud08YFTwBLqEbCk4SOmkj5aYupGLR6EzieZsXVHCYqTwmwzsMoxVJ7DPcBpXk0lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=SG7v8fyXCi6tXG9YJQdAUMeWIjLjXUv2-uPrOkdQeVqwi9rixDa_IDMZ_cwngo9_mF_qKho0Bhggb14fWByCTCc13cXpanBHwAjrWjOssHT5FcllkKMUF_fpkuQ36s3GK3h8uxKjXCMb2uknfVcXRhgAsp9KY0lk9h5m18fA1HLwLZItNee1llXTRoctmWSfdgORBhRLtr_xiKugcF10DoI1Onc0x7uc26sqS9b1CqFgaT09BWjWVcky9q4lKrcjeTK62V-hrc5hv2gfPQ2ZsCud08YFTwBLqEbCk4SOmkj5aYupGLR6EzieZsXVHCYqTwmwzsMoxVJ7DPcBpXk0lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMHPln24nxDJRC3uY61i7mw0CFUAXsZvl0z7vSJKZi86DecPV4B720tO614NyQrLTvbBM2e97C9h2S0hrzSf1iM77U9QfsMnH2XbxQgLa5-PPANtPVPsOOWt9hFJUwjXsgAAwJmo0sxCKkrSt9G84ZXte1t3-SWNCADpHlFSMzkPy-dQaYiGtyysFZlCfexlnBONK2kP268gFlxZYTE55h37h5p-nLDjpk76vGYrcJVs_ybE0-C0PUJ-28VSgSfjcsTMRa2q7v-3lJEbD1qZpOhTusWJ8ne2eJlu0Uq8wo-1ruZeTY2pRuxe5_VZLaKwuHsETyWcmDGMGYCrYldvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WInSW48jshj2Q11Dyv_aaKs3_yB_k04FEh_MReh11Uwzd9PJf5cHZE-YGADuWAc0bYda83jgXEtjW_59hVtiobN9TBW5vg4nPACBfltdcRRXlMzVwWQx0DqhDErd1rCJ4S3sknyDOS5fNP2i-794VSkp4vGyXmrPL1aNL0BbY1-WPu_g7rjIs6mw5A1DdiqrHTEgTx4MCh9jrvyooszvsFxoGZ_zpc3geLvE_DgIx72isuQPHGCcMAJXE_6wkDhbpB-SGQOPtx-bFrz7-0l4a4UwncSCll1odDEGSA1qSI3kkGxZDhmbPZcTOV0LpPAXsiFljZhRBTR5bTtMt6JWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cub0s-0u43sWKjN-VIM4-23EDj_tHffTNZo2xJl0Fj7HpGKRgvB4vTjnHkbJhOwl4LnCT4grrMnFevb7n23_ocuyBOJD4j0s5cct1ZUOWxpk6GmwFg464eyKsBqUJQyaySniN83sv5wrphISa-8E-obmep0InQZSWhNvs9hqlfy1GnyttK_7oEWqn136rmXZKLe7ewI543QOMTJlUMbecQVnhyRQncZ5PlVghrNeHqZByfm_Rjrc7vs-EagNq0f2T22nXL9c7qy31xM1oXVCK-t6rhUUR4_EHnfyyEHvTFMzOsVtma9SsKtvyI7WeFP2DNxh2fCCZZu9iRVPdRhm7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahDLjwXdvaX5cPGPGEoYWBVJQrsRW1Xw5zdD4Gg0bsNVKKz8dHB3afQAWPlo5wmtizI5aiYrxTsC77gZlrlkprrDaFKgOO3w4nCbu2uUFkRNPl64KRMpF3cBI1l_RlMlz5h37_n2ogrjF_F78e5oef37zHHPUviyKEs6uu7gEdyhUW7p2MnB5ckxDALiYyQ_KPRlRMsVMrw5i8o3RG5WWvhBC05Auf7FB1QHgzlEdB1F5TtV2QPMlJ6umxEYQIV5-VJpg-fUHIsyxFBN91bm9Iyj2iYCALONEXJBH4Az1XKbwxHne3tbaynZ8O8UyNVv5R6tlXZhgHMzzZuEWGcUIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1_BWVMUXt1Xr4LWsQl6Y8vVqg7OoA9dZwJCznEuHY3M6mF5_GVNbc-NbHsLleZDxl0r0qtFWMVxiQ7m4imNyLGM801-Us-ZW40MmBGQRfmrgQHJ7YzVk-OiAOhWGnjoz4-vSJ5wZnk3YMP7q0Rb63o2g_STMhFzGxhplMEQbgdK6iByQGUdQHivp9ooAicViCBxvz0JTQUOEGb2OgPIZ92rAS1YZeHk5OLy25NZSAT7BmRIop91o27CdTBK72NJ3Yaemf2XFBMGCg9zfH-8Ds3c_iXiShCXDSPLqHSdfrmtKctATlDaQs6nQgdJ9Ltgic7WOC3BND5USaqrz_inng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EHjnujpBgMjzS4f4CCdJbZb70gKWYSgUVL9mJZTHm3xdGDdlazDQ7CaxeMIU4g5PxyhxVcceDBLYLpFvnrAZkydwwPAGZ4MY4_TtIyuWvjA8FxyJWQ6NRI8ZTJVh1YHVqlkPlV-jrOb6edLgTLafoQUHTPZmUi9uld3gjDLxtpGOhNQcaGlaj5FnmPRtpI30xD3udsP4wOA1Cj-26n0UeDknaldrPK_JdYcSjpaRQAE9x4CMCR-k9Yh-ldUX35ZWfbHlxIkuSBZaN7cQcihKlqvYXL6FPtLFqI1zJD6Kiq4qk__YpWiUvuoQf5IdYfVXOBPWTvUKrR2QI7anAf0YNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=GMHoJ8tnO6JCt5np2Us9gV68nm6Fq4NGFImyRlnydpDGaZO7R31r62TWcPaE5xOoFyVUGdvKJVT6Osy3grzAWTljzRtw2GTLolcvEHhzUAkfG5IqmCMLoGpM97IZL2NZwoh7OPS-yYopWErL2TesbbX4Ppv7iYuCzXkCN81jwpd5SmSeam_fIphf7T1IFaEg7Eou7uiXjhJhAN0RvuWu1BQGmAwPKv_ZHsVoCYj1ArKehoLuGGxQXNQUnyuVYODLE0Df1mGc6a-afPM-7qDB6hxvgv3Hc4dTuc60TUniXBc1mgP7XOqjjX3iULFWLmB_uFA6icK0SPw-MeZR7bnpGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=GMHoJ8tnO6JCt5np2Us9gV68nm6Fq4NGFImyRlnydpDGaZO7R31r62TWcPaE5xOoFyVUGdvKJVT6Osy3grzAWTljzRtw2GTLolcvEHhzUAkfG5IqmCMLoGpM97IZL2NZwoh7OPS-yYopWErL2TesbbX4Ppv7iYuCzXkCN81jwpd5SmSeam_fIphf7T1IFaEg7Eou7uiXjhJhAN0RvuWu1BQGmAwPKv_ZHsVoCYj1ArKehoLuGGxQXNQUnyuVYODLE0Df1mGc6a-afPM-7qDB6hxvgv3Hc4dTuc60TUniXBc1mgP7XOqjjX3iULFWLmB_uFA6icK0SPw-MeZR7bnpGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkhEm__0rav7H3vpGMIxLMsI_P0gzkJnwFhV1Bt5MBARGDwHvwJvOxDkaoHBeISJfD4SltGiDSaj83913fG-hG30pyC6FCFAk0vh2E3t-Jk055BmhgkU5xtpYLUYZIexpoHm58Ow91oufpjs33E53mobVy1D5Xj8CU19IsILyhAAFo_C_PP6Js1-BolbzhUJk-xKE47zjO7_guvVyEZxfsAfa_C4IUXUdbVEhQT4z2cA2EuM7VUKgtN7MdAwBV3_-VgkrrMjy-6rCEvxJXi8Ohi3GE5h4Uj5MVuVfgwS2FmgwdQHu1gCnJaQMoyW5xP62-T1L6O4o60YHV-9MrRSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTsF0WSyWp8KqIwWSJF5ohZpVl8OzCG9SgkomgAiBkTCn_h3P6uqOjfKYr388hW5_3XgK3zHqBlicwOnBpBU7W08RIfA1mloVQfLw5R9n4ygCY7YdSWBrjnejwLZXEPEKz0TkwMxhYJbEt5M7Jsns0SVknt_bRzhibdfrdsy5ru1qcsJ29Y5efguYIMsj4U7fkO-mhp__M4iJuYV2JzDwQkuHfHX0hNyvmou08rA3SHTT-Fi7xKDJ7SLurY_mjBzGUPPSyUppIlLA66qTKGUbelFsNG7lTC2XGiJO2SFkREgvTtiDa_c--J0BH6Pj609CWXgzRv2W6PPdUyjSFJ7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb67T3vUbkNJMU0GTvwqa5enHnSBmmkLlCcjNdFX9MXDrOt7T6cwm7_ZvD6ydAgybyb77ii5pGwVzKAQPxKdR1FzYYkuP85bT45A_smQqUyucJTis5b9YoZUD7FKi5V1Sxokx5Xn3HNSoTKyctiHkspl9dXAbHuCmsVoOPbTj3pBLzyRHaNFv1JvfU4Kp2RU-PoGkXH_itQhEJSfT30ov30BRvJ172hITtTKT0iDW6QCvXdHCxjcTxTkW7Yih1UCxAZxhlEF2H_JdTNlp4p0ulYaRgNBhSg9LjaEe55iMUsENCeFLo9slhtvAfe2sTHI8qx9l7LbCtzf2kylRQcIUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⭕️
🇺🇸
🚨
🚨
ترامپ در تروث : «ایران باید موافقت کند که هرگز صاحب سلاح یا بمب هسته‌ای نخواهد شد. تنگه هرمز باید فوراً باز شود؛ بدون هیچ عوارض یا هزینه‌ای، برای عبور آزادانه کشتی‌ها در هر دو جهت.
تمام مین‌های دریایی (بمب‌ها)، اگر وجود داشته باشند، باید از بین بروند. ما با مین‌روب‌های قدرتمند زیرآبی خود، تعداد زیادی از این مین‌ها را از طریق انفجار نابود کرده‌ایم. ایران نیز فوراً مین‌های باقی‌مانده را پاکسازی یا منفجر خواهد کرد؛ که تعدادشان زیاد نخواهد بود.
کشتی‌هایی که به‌دلیل محاصره دریایی فوق‌العاده و بی‌سابقه ما در تنگه گرفتار شده بودند محاصره‌ای که اکنون برداشته خواهد شد می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدر و مادرها و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده‌ای که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین، زیر کوه‌هایی که عملاً در اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فروریخته‌اند، دفن شده است، توسط ایالات متحده بیرون کشیده خواهد شد کشوری که طبق توافق، همراه با چین تنها کشوری است که توانایی فنی و مکانیکی انجام چنین کاری را دارد و این کار در هماهنگی کامل با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام شده و سپس آن مواد نابود خواهند شد.
تا اطلاع ثانوی هیچ پولی رد و بدل نخواهد شد. درباره موضوعات دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
اکنون به اتاق وضعیت می‌روم تا تصمیم نهایی را اتخاذ کنم.
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVPn_4WXbWOX_vYiySvRdnpDowZb7GF0b25VzvlkwGnACX_k5GktYOHeyHudSKF8XI6TXDAnsVdhu9mQxZDnaDJP2lXZVye7w_unLRHbCtts7qpNXTQGTtZMvWsGjVR7mLrJZnAMamoDMu2byfaqCxgii5RCix8fzhTPXByCeB2qBXvXRHlUCCvLoS17yCOvfBcZRfSreRpS8oWVN5w0-ymU4IzjXyjOlHzsI8LZvohidCgL9vY5BYtezwm6m-k6jRm1w2HK8Oz9DSXzpyOpNEi1uwj_iakPBVqu-EaCJoaQiMyb4Uw-pUGBGPCOi-Ymi_Plh0NI9WM4M8NfB1-PNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sCmAub0yReGrckR5HN9sJWiIHjbLS24UyKmgWG_qnw9lHr-juccxnR9G1NJ_Tf6SX6LNFZlMOPGjh3GatwFe627TQmtuZpFMpYGdsoCCnn_Vaa_iIKdFNxlhHBLil1z2gfSpPcaq61SA_ksnZH3-rNLXnlmVL5T7m_Rpsy-feb8hDarDNFLdOCbiCH48l-org5cFlzCpvllJopHh_l7KKX25z92btV9OOjVQNey78bZra_5WoOWwByFxoo6TFxJASK4ZZ07qZWweXabZYnLjEXbs_zUvL_cgFtMP0ub6r3tgrp-Tw-pi-pxJ9Ava2ovz-pJqI4uMITQf79eB4xPHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU63kv_5M1Eq5ga_MIhr9tiMRiDhmUHS1gqOkMfbHyKB3yGHn_HUZF6HRdWE68nMrhE4NqNy-0xBklTmSDiWnM212-I-EpYGWJhfcQOHjzLV3aIL4JThUHeaLQCxprAMNo9CCGxiJemPhqgWahu93mXjx_vztgz0GuYHZLs-0BLcUD2jPAy5ziXwXBe5YTuF3RA8b4PvF8r_A7JL2DpHml619GVCOo4w80YMGN6AUs3RlfcQhpXxWV96Ss4xoMz6s4IeAIS5ZjbQCz7VoMouI7AIfrSb9yyoN2Mot-pdxk9r3AGUXt2XHjtQh5P6lswsFxMVKgJp4MgzT1Fu5iLK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=rblqm4Ln1t_pntacFbErpl_vEzgHKDrjUyz7vd8XPbQp-p1tdZvP-HjZTyyEN35_0G1O6pKA3Njgd-QzLypC6sEu5BsAi0Y1QQrk_VK8WaAl8nQcSbony3Fk4zzxJB29YCBD__djlCBGXJep6z3r8BqO6UpETYKyIhm0tVTVvHRUYAPku_hL0akwpBmcynna3lMJE5yc-p1oak_smgDEJzu-6y0G0BanvkMAy9BWEr70oszhQS929B_INPbk8gN1rBoK-RaiM7T5MAPF3RfS3V9q7FFSI1ZZ__VfkcbYyOQqC0MxIVKVoQvNxAf0ieAZGdATdfVMFxethzVSQd0Fbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=rblqm4Ln1t_pntacFbErpl_vEzgHKDrjUyz7vd8XPbQp-p1tdZvP-HjZTyyEN35_0G1O6pKA3Njgd-QzLypC6sEu5BsAi0Y1QQrk_VK8WaAl8nQcSbony3Fk4zzxJB29YCBD__djlCBGXJep6z3r8BqO6UpETYKyIhm0tVTVvHRUYAPku_hL0akwpBmcynna3lMJE5yc-p1oak_smgDEJzu-6y0G0BanvkMAy9BWEr70oszhQS929B_INPbk8gN1rBoK-RaiM7T5MAPF3RfS3V9q7FFSI1ZZ__VfkcbYyOQqC0MxIVKVoQvNxAf0ieAZGdATdfVMFxethzVSQd0Fbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo-sq1VvMFY_kl_GDTxRboCskJOQnLQFI8swhfxBQXIFv9IIBH9Fqasz2DzoI4uo4exFdZ1DwC8LpmKWr8r9SdmJFbAM6OrzQ4rryQqKLiR3OudSaDtTPXTSOr7xKE5GtjJ2T9RrEuVH5GPrQJUlHTOj7IWN25PUDOibzTBeJjvhKxbTnXTfbrr9qAmd83hIrjv7z-3299UCLoYzdSNrpj8Fl_WAGMQraJRNbpgw6efpUG9R_MrPcIUXISX6H3oJwbVdMaNKGwI7R4zQn-P-82HQO_zeBvdf7g9qtVOGbc3Bl4n_EuoZP_VXgi_B9FG4MIqYqxp6OcrCVXoSCfUrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=ZFCkdGMZthUwKXTD6JROCeP-yHN9vUVPv7C-_bb-jvC7HxwPN9WP2eZX4gRdlwSBqSYTeKBWFtKeGoXRzOZzYAHEunsWEe01Y7Snz_iuRzd3W0d0unC4SwrId561VwogYstLHVeG3ZYf7Tts5s6-vrLijlaeBUA8a7jeGWvoUCDbOgWhLx36ppz0ukOb7Ylz1Pri1DQdBzeJDShsLbjj90q6sEpDfpyKdHZsyUh2CtHq4r69kip6HWtQazTOMkFs2CM2cF0vNii9zmOHe9Dz7wde8IIkyeVmKDAcXD848yIb9oaSKv2-zssuvhyESz6bJfnk6Y1K2IHRkXwmJ0mHQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=ZFCkdGMZthUwKXTD6JROCeP-yHN9vUVPv7C-_bb-jvC7HxwPN9WP2eZX4gRdlwSBqSYTeKBWFtKeGoXRzOZzYAHEunsWEe01Y7Snz_iuRzd3W0d0unC4SwrId561VwogYstLHVeG3ZYf7Tts5s6-vrLijlaeBUA8a7jeGWvoUCDbOgWhLx36ppz0ukOb7Ylz1Pri1DQdBzeJDShsLbjj90q6sEpDfpyKdHZsyUh2CtHq4r69kip6HWtQazTOMkFs2CM2cF0vNii9zmOHe9Dz7wde8IIkyeVmKDAcXD848yIb9oaSKv2-zssuvhyESz6bJfnk6Y1K2IHRkXwmJ0mHQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPrm7ago94_PE8ESczShdMERlwRhDN2pPsW-TOOyKeyXpd6FMZIC8VVUhXaCClVVMawlpJu-q77wdrZ8zgYt5j2YvcNQzwnqUmIW4H0NP-gs5l3wN2NatruxakvE6uUjGAalHF_7C1dv70tWOk3pLGQSujNexhbXaEUv4IC25ptd2tAhHjg7EhNiAhP_2cNQEjESAF27SBN8x2gwxZEXOez-PoHNI0ugPky8FTXAjjJc7EOvcTQUpLGR_7TuyrnmkgTF178ZCv9NNpR6fDz__4g36STbTFa7DUYUpOTxrgKminMNfFrIiAxebO0nRtxnnvpzRB55i18xt5Eiq1odOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=d0Hn8cXceEKovF4uaBpkMc8JZKQ9wmFiiomvFaV9XI6eix3-RvpnbYvQepn-DmBtzpA_K8yVCqOdVEVSt5jlNkfVg36H2hFAiLMpTSOqxaGkHaUOoIjZwboc0C2lqQdgHnohhE5VW7q2nQJ11niVAHJgjGCiYneJdE9_H4Rxs9VirvMtg70PhB0fHpdhi4NpgthlruCiIlFSiz2_bHzut5D-ya2wi_MglUUPt8_jOze2nJ4Tx_X9q5EgyQuyCzwn3F73yN7anxecpg7DEzwSrLiyTNlUYbCkKU7akf6t7QgwOjbgwOG8e4WumCauVuYBdm6LoU5fugS2OCwZTb72Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=d0Hn8cXceEKovF4uaBpkMc8JZKQ9wmFiiomvFaV9XI6eix3-RvpnbYvQepn-DmBtzpA_K8yVCqOdVEVSt5jlNkfVg36H2hFAiLMpTSOqxaGkHaUOoIjZwboc0C2lqQdgHnohhE5VW7q2nQJ11niVAHJgjGCiYneJdE9_H4Rxs9VirvMtg70PhB0fHpdhi4NpgthlruCiIlFSiz2_bHzut5D-ya2wi_MglUUPt8_jOze2nJ4Tx_X9q5EgyQuyCzwn3F73yN7anxecpg7DEzwSrLiyTNlUYbCkKU7akf6t7QgwOjbgwOG8e4WumCauVuYBdm6LoU5fugS2OCwZTb72Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=b7fJH0ST0r2lqFZgKwxBbKL5FL4YJqUvgm-FRuCFz6V79X4nOzVOjHjxa6uWQbygicb3nnTPcYk4RlGNW7dQzAR2Ed88uHOHy_1b39zL231CXBSXJ-j4BWqHGvP-uLfbp6nB46dr01EvrchFN0ZUzjX_zSBrU1MIj8ZwHCimO5tlPcMN7vQjuQ2MX8JRBAsTuniuByNRLRKl6O20O2wZD7sMw1jmvIpcJjt1qVt8JOchcJhmivRUQjcNRC0eRb0YWCp0RxZ_BGjZliowN3-LLpxBgoV2zHDx9ieHQR22DLQyI3532p8YC8xGXOpwITo4te_muKtgxel3NlYhHrRL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=b7fJH0ST0r2lqFZgKwxBbKL5FL4YJqUvgm-FRuCFz6V79X4nOzVOjHjxa6uWQbygicb3nnTPcYk4RlGNW7dQzAR2Ed88uHOHy_1b39zL231CXBSXJ-j4BWqHGvP-uLfbp6nB46dr01EvrchFN0ZUzjX_zSBrU1MIj8ZwHCimO5tlPcMN7vQjuQ2MX8JRBAsTuniuByNRLRKl6O20O2wZD7sMw1jmvIpcJjt1qVt8JOchcJhmivRUQjcNRC0eRb0YWCp0RxZ_BGjZliowN3-LLpxBgoV2zHDx9ieHQR22DLQyI3532p8YC8xGXOpwITo4te_muKtgxel3NlYhHrRL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQTIEAp-OLwedf7HD0Vuet24YWJKoeSRQBVKzvyMu4c1HUhH5QVZBG-9pYkdEumgTweLz3y3yrPBLlMNmqntf_QaP2EsN5bjMgsmmvb6lE4JW4_XEUN4eLrehfkHXN758opw8O7WL5GtID2X8k9DL36lePMBpSe-R_0kaV-lnS11oIvwHd0I_0xqfqDA1_GDbUp_Gq2To1eDsrEYxp4dFK8iEgiVePdnVACwuoFG8IYXDxoCNyEIJiIhWFg9iTG0BXl_b71xba6YMPxgrk7hNro1_F8qw1Hx4eP6hLPifi-3bjW3N7MpjjtXfqYZWjVxR8LMliuodX62FeFm3LpyyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL-q3Ka5kgK4Wi0akgJxO4H95Z9iV8W0z1-du34cCpWOxGLkLzCxabAUZYZPjxjyhqXtSfnFkHY-YSE4pT0A89Ef6ShHfnXD_LD5sw7DOiMdD8h_kzqP4M3b0WiThIAPZRF0_s85BSXcRIRrBvRNv7ylTg6n9DQkdEW5SCtw7uizSaPs7_n3m21Rtg8RYrz7-6OPy6-Cv65obM1hqCiF9YGWrW9HzDWjRFE_ZatAxPwuIZk0QXM7jwENgOhOovDhCKyCi-InJLlgxQyT5muz5gxvV8kl2dpVdGkWuzMNlKwmpAlmaZhLPgIhKIsfVtYYPLnWpu9VOn6qaZzq1n0tKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ6fzEYrNsf2oRzaAq6Ac4LXlc1lJaBs837mhgLgGnR2a9zcTB3xttT92rxaQbGXMVpwFBcns93OyombsyFAU8xYUTrRgi3DUuwdAAXt_TKyoi2dECS0TrZ8N57ecUyZ41yJnRdZGa5A5dgMt6Y-Eo38Sorf9qLXbrL6vQzuhuK4q7IbvU_34myWOkDrTPyy0nbQLzXZhJyWaFOc9nEUqZGABcpbD9dHHzvy2YRuGoUt6wAedYEGJaFldhcnSo8ApZ5HUuBNpkHZWrslwb1tOTU-AJeQKBhFot1XgcLiKw3wvg_GTNE1wLuBHtw8iYrpFcrTWAN6DDpsvWZs9Pa24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQcXe0b-vCKupVJyJl0ZiTfntMKrCL1EZLZmY6_VzRi6TEMO1mSOLrQdhxTRmUyl6qZuXCb0qBIqBwpLZGxtRgJvW2TRsOVclgSk1t3j2dQrsorVhltFMlzdBZIWKNop_QSdKpY97oTMwYIBGuLUE4wRv05sqeltUJxj2Fk_lrmIxdDHXU6RfVh5_5z-DZL-D76-uATAxfM3EPvBHsNVXmDpqp4-YdZmt2mtlb-lbXEqmlZNcKGhOF6lIJfnKXOtJbuUYrc_A8ZLeRNLXD0zSVQZ35unZHl0fDsrG7eKu3b_L0-Tec-xCe4QJQjKQcQoT8ZS0gB05NRlU8NqE4reXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDQzoSggcp-7TqErANmUzTQrnM4_FF_RIyYudhNCPYjxJoABogpOM7Z9e2ASrjKzLDXWo3uUmHGQz9r4uGXNFZD88DL9F_gdZbVGBpH9lOdH6p-f95H9D9UvYf3ATOt0gjH6Uny1iA1n8Zu48p7rWthMZD_zMIuvPJ5-U_uvAqwuDU_7kEzttUjRH3LFyXcX9-jrjNuAKfga8SulVTEML-sWuDqgLsLfijVJPTqNoavKsYKWbJRAe7Z-VdKnnUfDfkqRCZEG9FV89QyoVk5srVDaXpL9P5riOsAsTIgG2GgCBx6AE4bh5Y7bLj3QsqnSgDCcQOjDBWpuC1xeZF-j_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KiiBrFE3iqGr8cJjcImIB_2YsLYF1U2Su_WZwdgSYg-ERmxM8ozgq5RG0rNoDkJ4JVJW-YYGivWtaaRol5m-yV21TNPh2lmmfhWl7zm_6JU13GxffRsLw818ZPhj5_M5ditUJRvQQuJu1pKvZfuaCri9n2vwj2OjexV7rsCdcZkU6BfWdFqjchC4b16Fx5SZXeiP61LsjucivlVuTwJxnOB6Sp5cl7Mu4H-YwysU1dbQ2XDM3ek56PHfJlZYn6dCNN26m9gjYacYUAn8wOUxiSjuCOTpzlPwdZEK8ir1k3q7S1pD4OhxssnVMeEbsAdX8hYwuDPRat3V5yiZXH3SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ-e__qndtTJ-05qtNlgfybdpCV8rpQnlrkrai3yPzumHRB2_jlUH9RPyOkLAK1h1t_LcR05ew7thwcolB6KPUWjdw_UCF41ZslQTh-RUyjo-Q4i_GD7wLGv5wOGFBkn6KvXQ550it_OgJD0daIcir-sGFgOtF6_UBq6fgtEiObZVHM38NG7C1SU8BYO4rrGL-OKQsfy2u4X3wsjI_wo8bTYkNILkwt-r4cvMDJr1x9lK3OdDSOS5uXg2b316poaFaigGp4kNGAgohG-YV33hhwYov2DcUZthIAT6f5xl7a0ICij9c0nuSnHeJ7Dua_sj-kibO8CuGsUxb8bF-cmJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-_psT_T2JDgtnmePP7hHBwuTxagJFJOsZdrdCi5MiP2CqXy5OJtWTzCS5C2pdAbp5ixz4AuHviF08ObiMVvVjI5kTiKG2g6qIpt7FE0prAC2VkxCaB6quwCV6jZgHVi_8fuTobLiiiUtXqI00w_hBoYOFd83scxSAulNQa34VbMb8ryWQRlTUCep_dyH1_0XAcYUvWabldN9u_L2RNsHDNz66MxiAbDgvNgzb-rHUt1ocA_zQ_Da1vVrz_RVrpQzB_DMKUu6bzDvJ0x_ThEwoodxcMeD3tvjOwvd6QXNQ-kbg42_K5ZHzZUiWE9D85CbqcJ0GO1NuC8YdvfZrbZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=F4q94DaPXGKkV4rZNETyViou5MWYMSlCLZ3wdya4nqoBFYv70Dw2JKzrw7HwJnUDql7Gj1JnyecIszskDB5OMHC9kNfmj_1nvljVavxkAiQ3IjpvrN5UK06YLVjkPC3i71-ofU5PqiF6-JIlI1oobX-gYEs5SLgioAo6zm57zQ5aBhvlCfWif4A3dwNoycvd3JmddP9Uwe07kIj4Zpi6YSFbaFlAU_QjaFgPYxMAl7G8o13H1wuM6I0aMuWzWEHQe6WIgdBCuEs5mEk0CApsJX14QXC0OweKQ_VrVxA-5yD4V0g8RWl5731n94FWFXI4FY_7ru6HTqvV3qRbENmRIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=F4q94DaPXGKkV4rZNETyViou5MWYMSlCLZ3wdya4nqoBFYv70Dw2JKzrw7HwJnUDql7Gj1JnyecIszskDB5OMHC9kNfmj_1nvljVavxkAiQ3IjpvrN5UK06YLVjkPC3i71-ofU5PqiF6-JIlI1oobX-gYEs5SLgioAo6zm57zQ5aBhvlCfWif4A3dwNoycvd3JmddP9Uwe07kIj4Zpi6YSFbaFlAU_QjaFgPYxMAl7G8o13H1wuM6I0aMuWzWEHQe6WIgdBCuEs5mEk0CApsJX14QXC0OweKQ_VrVxA-5yD4V0g8RWl5731n94FWFXI4FY_7ru6HTqvV3qRbENmRIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMrM0Fuiluolwm_qs0ha7h1SfTEchmlLLpDcS8RHnocZrzb-tE1CyW5pyWPEYaDt0JSjtggMC5Bm9LNYwB-WHx-UlcTxvnd8lriX1Xi_Ywl_prJEo9Z-IiGZp8bc1iFKuDxAx-wXwY7jd8g9BFbLWIaaSOdhVq_lFYPuzrhitgxPBY-7FF2zmLyb0nrow_NR2KFW0kwhSj9sUzxkrtFlwiVZUoX5q5vgUOy32wHVWvp5gzcHwRcInEgJngi329nAT5DhTZ9-xypW0XAmKptAqAJ4dQ9qB-zz83kOG85NJESU7JpfjnKeOFUa0uSOlgQhLLEs6cJMNkjqLNnO3hrQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
