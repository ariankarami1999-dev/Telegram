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
<p>@news_hut • 👥 210K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 17:23:10</div>
<hr>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMscHHxFCL_aknogGU6wZWj2I7hoc_hGzYx267vywa0REDajKFUI36B4GAxoeIQsReEQ1LDc8PBttBYvBESo9_UnXoKB7uWeXQSneX88EF_IyDDWmI2THIQBZK3By7i24eKRSir_Lp65j3RhSsxSN2ymLq9YmuchuzxboZlq0jNI69TsLSGm4uNCCc6kaFSK4Gf1mIb3HLTyQbb_X_4mRqtBuvoNkenN6fPhA4xW6OHGA1H6FjdQPn3TUaK08qGyDwWTUGPaoy1AUTesAfA18A3QLluPsSsaOmYQqjZAZiwcMmx-jn7rrwSztIl5YnsDMrLIfxwob6cIOx3TzSSFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=dWihSjMn3UO9aIv-Z2ipIT4drV0PYV7nML9eyXlrtPlwN-MZKWEOWIXxJP0OtMsgRS2XDSFXJpili6m3-dsvfz-iFyjUDDIPdwj-iJsT4AaBpDJY7FYi2o_EddmErQluXj8laOEsvePkLUpRN5fmDeJoIcGIrB76lypraT9NlU8ezdAx227nhBMaPKQlToxcRpkcLOSqk_v_INEFfouDWUn5L27_4SvKRfUVNk4UppPHfoonXHEclm2uFQ_SA1UBEmuBfyQNTCmINo365FpGgOUIew22fWwnKAAtxi8VWnQ8fMlfZM72C6xhlRPePOS712yic0PO9PlE5vk8sR7LDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a43d73ec7.mp4?token=dWihSjMn3UO9aIv-Z2ipIT4drV0PYV7nML9eyXlrtPlwN-MZKWEOWIXxJP0OtMsgRS2XDSFXJpili6m3-dsvfz-iFyjUDDIPdwj-iJsT4AaBpDJY7FYi2o_EddmErQluXj8laOEsvePkLUpRN5fmDeJoIcGIrB76lypraT9NlU8ezdAx227nhBMaPKQlToxcRpkcLOSqk_v_INEFfouDWUn5L27_4SvKRfUVNk4UppPHfoonXHEclm2uFQ_SA1UBEmuBfyQNTCmINo365FpGgOUIew22fWwnKAAtxi8VWnQ8fMlfZM72C6xhlRPePOS712yic0PO9PlE5vk8sR7LDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
علی‌رغم درخواست ترامپ برای آتش‌بس در لبنان، ارتش اسرائیل دقایقی پیش مناطقی از این کشور را که در تصاحب حزب‌الله است، بمباران کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r889RVM95CtCiSE635dIcEPW-AGz7nAGtjH9PUgyGLXhPMRw9vXVp3y8ihKWLW7HygpH4pTpNcYUXqFte35Pgj6rUXbOFV9_Gkst34FUZZdk_oGHtFsxop2vejX-k-TOig84FXEbGsvulEgdf4k3Q51JXtEw6PewM-jBbF2UAdP8C1My_yOTs4QXnq9LsHI0P_w3gatL1wG41bNehIjOHRLqmZOXbYBM-5JmqEDZXWC_3784Gtlc89h7Pfq8BXvbpk4nE1fZWXRH1C4udQoJqnJMvlIzpVdjTH2pnZDm4Wa-HNU7MeU_XWsZ4hLWQN8KCf1LOUMBr7PON9ye5dFApg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mfd7Ayg99IpKPzw0hSnokEOInmZtlSLYjNJvY3wXSULg487aMpOhg7cmnv-ZJSVq3a4KYHA_KXKwnpKEiJOLaZ6unQP4EM9LzEU-st0UVdoU7xt9ua8Pp_TNGsSDHPzf7t_CBPlPaEbhNjf7Luf6gcZNcJOu6HRWfr_qYhBU3MigLbKdxV8C98FeGIDduBQz6ciTJe8GAJY642Jfuls6tscbSQ-AJ-1QE5r5FpTpY-qx4oY5nVF3ndbeRSPr_wtxMbfRGnvHArtq5Wtc28ruTMuLMho5GxR8dhdbaB3KOwg-P3vLk7wfb-0d3TZs8jFE7jJ48trkkn2lWA4SqmeI7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCRfN4yL7UMSfQKN_xBXzfg6n4phYcHswP_ZgeZeCdfP55P-84_CTU0B-53nXLZXHmQ6Ff39eSbAydVJZqTIJeMLGxyqy91Nq0aFJNpjJ_K2iEYL_mnxy0P6XleOuzvVBbSAIRCeNN4Otsq5wlmhe9gHKZQJgwC-bcDCGtOtj3ibYDmI2Y6t0OdKQP3sCQh88a1rMOn-TiBOEDP-XJS9qzgLG_gPixkJeOejZ1ArdEHgHOgW_zTadH3q1htse1UmVvsUUSmgLgwL2rPqfDuumcLqCjQ-_-MnhyOfNoIHkTiFCSLT_Pn5Eh1HdnyruQ2DArgakS16O6OFpRXrWO1u-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HKguuF7--CRyLFvjw1K7oqpBt84N7hqM66sbRZCysg_D4s2Uo4KKIsF3x_69HMws5_JkiiMC9kwYY_VCyryFQ0THKupl6xO6sfH1F2rvHDmE5REt2geXvB9O7_QBmBEHwqp5gul6K3DqUCzCC-dZ-J2igknP4uN7fj8T_KiMi4E8amJ-EK2xJ8LEdRip3fY2NXvefczn1O0QYmVNlGddI-69oKwBz66q349Kafxxl2hvSPOXEP2rN9fsVQ1lnkTKqXnfNBoSsq85DyHUJz-4E005VueO329f2ZZZPlJZl62EUTHNzSHplacrcOC_YRaqlpxiLPBzOuozFxyfmb9elA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyKnq7Y2aJsZyj0nPJpNAbod-nKoLUTcazkLmPIcgtN20Mp56KmcOsNk6XCxcN3YYhIYJ24MvccZYyPp5K7cS9BfWi-njxYTsDEIAEKbTla3rP8oqk48qlEENwnuh8KnnI15QFb1ZDuPMmfltuoG24bBTDL2zD1FUvE63cUQlLc2PfYa1h5cEIxPmLhr3IhCy_ogObcAABzdFJiI_a8CAt2IbmRCBWyZtORWFHYck19ixMFMDTS9ba_XzB5oVeySiSkq77IO7i8fcX1wIhcQbl1HsWvbXN5nnB1spZHGgKYRWtMmDlkx7a4R9OAb0b9iityfmsHfBxcBMSi_-JDBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rn_Jda-78_LNKLZwWIn4F6GaMby6OXZTG2TNs8iKzd9NNUY-kIMVfRj94WZBhO5-4YlKN8E-sywPbjB4Pp3U94w_EqQEUFkES7tYgFvSq04QOzfv_8qmP6g5arG2m-Y1CVRu6YlkxquFLzLR6TpFwOcauCNj2lgwt2_OJRllO8l3LE0sPQXE-7L2EdysT64w6a5xQVnjBOH1YvpuvjV1f8A6lHNN_i_KQVSReuzYxFaXSWpelj2PY2I6ioVhn5cjST3s3uK6GfLWxFmpljPRsEiVG5GsWEDb3dBx61a8Fu_Tl2MlKj9mG2i99sd_PY1hBRMFfmsSJkESwdrI8Nvq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyRVGKaGzyEYKD9AldytNWVJAfVLtKoojQW8k93Nf0AlAfLeHLVL1FSMzZmFChdyZtzN3WZtuKYjCgssCvP9x106IJzXo5PLTPpJaaRNrsQ9YpgVwCQZlbWGmPu9m0RAShjnKCaAHhJ5SOZYYsePfrzf0_jZ2o07Ikz5_P89ua1sPGN4zBb6sD3-DCpUbWOve18LLk5lfd8nTyh5piOmcF3Wl4nUklmckOaBWAa8NnCU5RqBxAwxVVUn47E2CYJpvLm6yxue0dWgNry2DZdDeKIeXLkg8z5Umae5j16UzyYFhO6U6qAi3RpvA5UQYqT3a_iilnO7K8jD1ljkz6TQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e89jHEQHz8gFnVPqYH2VKl8D4R_iePU5SPaBkyXSh8qlB8LFpOGxerGvUphHZpdoJTMixEbS7JleUNL-EtF3s73SK5ryMHALv2Z9maTeP7XhS76eThdLi8EuM9JPmA8_w0AWArwYhgEHb6MTJRTUYnUCAnRDqilDSWLm4Y6ODz3liWrwKtBqpHUtjOLjQ4CLEnOXxWg2bOiWhvaBnxzjZn_I1OxAvxhx_j0MumjRuVZCv-_xOucXeEpNNKn6sE5nBme9419P4fzEZNcJ-4z2hnsP_xj9HaA0f6xFIki3vIZdZDCMG_XFzrwn-rsiSvMzjgaK8s_OGNAiC68FGFV1_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWeUtRbJE3eKh_VrbspkAEep48uzPIRI6yCBOt7eQ_HCvKHUH4m_OQmf1U8Zxg9ZF70e4_1Qhc8fJN0hJstagnUE5pDd5ZAR_ypGEpvxg1UedNQMCSL5ocGpM8DOp0AfletjYU6unXtYaRjM43keCpnlQZHlpuJZWEwpwHX3LRiOkCigecH7nV2U9bvDNNc4C_Nxa1XKbW30wdoJjRZZKvbxH8sGQq6WEkT7qQ0flZszu3oFeek40TPyF9aquuqW-Wv34zpez0ieGBisDMm4yfQZZR3-hk2I2OSfGLRAS0pI9rXiDfbbeEzbXJn1iD6tLMp8XcS7embYpheGtk3pvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbUMPzZ1awSIw_JTFxv9zIpgC2YMWSqInPkwgaOVuDlMGT2rm9Nry0Ju19Ow20SgxFclCIdKoV5nvxaY5f1EhjQLQe2Gn5XeNn8TBO4RjoEPLC5GcIt5PHj8azdb4kxX2cqjStbptKqc1sb5BQcK4CwDujlIuiGlh3N8LSJSryYyPMCeboV0on8gGGhkh45WXy6uv9jtYpmO_RAukmYg2e9qZ3gjqTlvyDpm2xNi9we6WDc56pTgdfhaFB3UlYcVT9oGHb29tdlzacc2j6uCKuXMyj0oGK42W6366v0Q5h1-S6NOR5j_ptNy3RiTADc3lSZCkFlJCDeRgW59_l_tDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce9uHeROK8bJYDMHpxKkMoQSN-lTYIOjKdbhK0P9BnodheuGGymN3Rbrdl3DxGN1P1iBkg3pWLGK9PuX7eLuGcbysDJiRmwIXSlvhXVMP7lmBp8e-fbFcM-d_NjX7Eg2_cfxesO0WdA85yRzOOszuNNLpuGEqe4JCbD5770ewOMibUr882F52fliZNist5-hpU3I9Nh4V-D6DqQqfsQ3OWfpd4Ix0lUqiUjw5iVQAa9xQVsSH27n0poA-9vRhx0xPko2HFXSXQn4RIVN6vYMH-Q70DchSVDUrLIW6O-q7Pn2RfdaoGIwd35JdbU_q9mHS-jCjeVTdMmLOCcaPXX1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPr9gVmcUi-MlSQadogmJXMeY2wBRUHR1YUYXj8SeWZGSuwbe-eT37o_8nbh6nbIl4jMIoaHFsAbhM4eQ_FGNvRIZTNwdXymi6YaBdbudiALq1leO81C0t-B6JrXQ8Le-mOhy4TMY84a7TkWtmeRiNL8tcQ-mqe8BK5DMX_TRnyyNRu_3_ijkT7JVNoOpmHwrFMLDkr9FT__6kff3ert_8ex2p2QjUMUkusA9cfQQC6Z0vtB8aRrFWghL0Pt9JpD1JG804iizq67IveBU0Vrtu9KM-_GHyxhP88c-SC7GHxC1Ix-65AmjoTLVK2MwgeRpgZ9KJ9TIGr2eTfaczaoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldV0YsQJT2zrNOirYBDwDd-ypfD06H-pjkjKr3JYdU8VBlKkS04DwqGlVat4e0Ms5Z_zRqHhTHAtRqoZUMwnPjcsg2v0Wv7SmH-rVE3zm93XAhQBpGGer6J0zGk_h02NHS4pVGvlKD6XacOodJuVZNrMABcjQongkMConmxKf3daGIABoJ2Fw8VQEg7XIo4nEGtMRG9IGJrq-UI1g-ULjOQEB-q-3Bp7El65wnd3XT5xWjg4AL8-UHKPNF6J85KXjqTehTFal9Muli4f7dg0k1TlfItAS9lUhHZnVGD-jbwZF-5aZx725IUZnjbLCOEBVh429yZZpJp4TeAIeBQOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=D26CVRXSQdcbiDOW98S_ofWf_yI4AQ8kxVREtItn-QF_UEUo-Zsnsb82vNPSy6W_DGzEkSghHXs2Ey-qzgU_v7dOOJAibb7pUGNo5GIMRkEPY7aVEaJr3d59MKAabwKGb7zZ-RTG61uBOxDGv97BwGKZqKaAcTUptmC-TawWV9dE3b16pQYPHzzMoejp1uCfwfQiLzbOtK3g0uB96NYtiSE8kO08-63emyfBrJziMMF67fyN9lc82X2FazEszziVOp-r2C8s523yvLHFzVlW2ryXIn5WxOg34fsK4UVpN3Q6rovTdKcJXolvgPt6Z4_9A-mYi4jFT7KGbRJvOU0w4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=D26CVRXSQdcbiDOW98S_ofWf_yI4AQ8kxVREtItn-QF_UEUo-Zsnsb82vNPSy6W_DGzEkSghHXs2Ey-qzgU_v7dOOJAibb7pUGNo5GIMRkEPY7aVEaJr3d59MKAabwKGb7zZ-RTG61uBOxDGv97BwGKZqKaAcTUptmC-TawWV9dE3b16pQYPHzzMoejp1uCfwfQiLzbOtK3g0uB96NYtiSE8kO08-63emyfBrJziMMF67fyN9lc82X2FazEszziVOp-r2C8s523yvLHFzVlW2ryXIn5WxOg34fsK4UVpN3Q6rovTdKcJXolvgPt6Z4_9A-mYi4jFT7KGbRJvOU0w4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=OL2s-k6_sw1JvNbBBEz0NwkG1JWzFNKqUKgyCXmrtQ2gkeRldKylWOFLV670PMDat6aEG4dz4xqudBhDhWW1UcNtaNaD-eXAgSObWjW6QO6kyJ-OTzs1G74vDNK95zKZFVoA8db1NgPve1uM6_n1NBemXcSfQvqt1LV3AzZNkOrYPa4-5cAcz-9Sd737O3r7T5D2bI46abORKLfL3O-Mws6gxGecTR8Mrm4NkSLXaBdCqUUGDtgQZo3GqDrYIwhxMh2dior6mrR3WXaGyNBEPCmE4OWzhtETLqpWyjcTufxL2h8pBm1pZssOJBlmx1If9RYr3EzlQtWcJHrNMHfmow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=OL2s-k6_sw1JvNbBBEz0NwkG1JWzFNKqUKgyCXmrtQ2gkeRldKylWOFLV670PMDat6aEG4dz4xqudBhDhWW1UcNtaNaD-eXAgSObWjW6QO6kyJ-OTzs1G74vDNK95zKZFVoA8db1NgPve1uM6_n1NBemXcSfQvqt1LV3AzZNkOrYPa4-5cAcz-9Sd737O3r7T5D2bI46abORKLfL3O-Mws6gxGecTR8Mrm4NkSLXaBdCqUUGDtgQZo3GqDrYIwhxMh2dior6mrR3WXaGyNBEPCmE4OWzhtETLqpWyjcTufxL2h8pBm1pZssOJBlmx1If9RYr3EzlQtWcJHrNMHfmow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=FZbqDRVGFqPmSLU5QxPuTkOtxa41EqU4EQP3yh7MlzBc1ypjEBcxPGSsAHthDDrmvvdTGfqIWs6uRIr4IZ8BhkKUIscYIKeSUeTjFWX8RtCaVJnYgC1_63hI2exrzq3L09kDg-2ztPigvAXEhFdDhMBxJSTdiIHD4fAtoQ4Ilf42VJi-QWZo0hD-CRKlO6olLJp8CgJkX7eNCT4IpUELtiLLimiBk1y9hQqiGM1fiSc5XV9jtr8HHfdpEQSPEUyAgIxDEcLf2wpj0AfdBuSY1RfJfTdaF9cRxKA-mHTPdOXwhcVTTIe1eUteE1GNy-jM-Ogr4L_NmsOKDeWAbKbQog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=FZbqDRVGFqPmSLU5QxPuTkOtxa41EqU4EQP3yh7MlzBc1ypjEBcxPGSsAHthDDrmvvdTGfqIWs6uRIr4IZ8BhkKUIscYIKeSUeTjFWX8RtCaVJnYgC1_63hI2exrzq3L09kDg-2ztPigvAXEhFdDhMBxJSTdiIHD4fAtoQ4Ilf42VJi-QWZo0hD-CRKlO6olLJp8CgJkX7eNCT4IpUELtiLLimiBk1y9hQqiGM1fiSc5XV9jtr8HHfdpEQSPEUyAgIxDEcLf2wpj0AfdBuSY1RfJfTdaF9cRxKA-mHTPdOXwhcVTTIe1eUteE1GNy-jM-Ogr4L_NmsOKDeWAbKbQog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dLkbUN3xoHyQvcg9lhKsIl2u14zeh7alE6YByhMfh9yVTVeCuBE7xpSBG5UQ3O5mggCqALorCBuZu5vU0T4-P8ZbPWoCHFMqg27rL6nrJom2MbJ8VTZo0h0hhjwvwJRA2SuvCcMAI96RJIXCXULI2eEh3_Qx8ps7CBdoaRu3c-d3n9PU6Rp5ngyfiSTjqJ22c8u5NnSVVlyXUhB0IY43MS9BpDxo2dwuGFQdC79cr7WzvHd8pGhFRLm5w2MU0KR5H8YjaArO3_EvNgldo3VQUO8NeIp5_S90O9uBaMdu3TZiTOmeLEAR9-erdRucw77gdFmFXhI_wG6s_DUhF1G6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v_w_pCuwF05ChkuAm4YQk9qVBhLySj4X7q--YUQHghH8tb1BNhWCmev2nwIuPW9iN7kBwSBGLlAhuUyptlLmPEg2aHLfc2gtHRZsKbtC-8Feog9mjWC_HJS8fh6bX6fP5hlHqkJCx53P4bPmk6KDkzNAD4vQZlw_BAXFRn7nB2D9_eKMsboRmKn3mGNl-7n3CeoqQVf4P0LjZoH13g4yfcssO3BZQ6fm27sERJVWwI1UC7WOxobVQy6_gen2e8jAVrz7X9rJhra3_QG0Pmw6gi9ZKDQdnmZWVZSNXbn_7nyMCFHIXegP35zVXCeXFU6ly4ACsECiLE7vqJUyrUgQ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=VsehXv9feu01vT8ovW46E-N5fTrsS_h1ClMDK5-3MxQVVAGYgbpC8uDLcfPoEpKh1N88a2g5HmIhzQVhvDwLwwZkdUYB6OctNHjDXOP7rdXEk3BOcArWAvYOkljMgxxz1dsVcxgMD1cWMd3PwBQUh5y6e2tcQOCVDfOix8bwSidMemUeti3r9_BAQAq5Fl7mDaJCHFq3inGQNCzaHtgEn7EP8vnnKqoVNY3x3GPkPaS2Y_PVyQNRrpQUn25O31oZXeOosuAR6ko2bSAb9i8YOJAweIjz75H2JNCEBXrg_UAQiv3YyVWFxDOscm_m1v0j3OQ_DqrH52_x_T9DoHONBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=VsehXv9feu01vT8ovW46E-N5fTrsS_h1ClMDK5-3MxQVVAGYgbpC8uDLcfPoEpKh1N88a2g5HmIhzQVhvDwLwwZkdUYB6OctNHjDXOP7rdXEk3BOcArWAvYOkljMgxxz1dsVcxgMD1cWMd3PwBQUh5y6e2tcQOCVDfOix8bwSidMemUeti3r9_BAQAq5Fl7mDaJCHFq3inGQNCzaHtgEn7EP8vnnKqoVNY3x3GPkPaS2Y_PVyQNRrpQUn25O31oZXeOosuAR6ko2bSAb9i8YOJAweIjz75H2JNCEBXrg_UAQiv3YyVWFxDOscm_m1v0j3OQ_DqrH52_x_T9DoHONBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=L3YpyVbWucvBTzgYGcZFeR2wN1O9MK4JCgj5H9VDhP-U82_3Vook3ZMg0-pWjWnslhDKXXo9dixIfyh6QaebNMXfmdrN8W4kM20vnQuGKhXYTtXrE0c_u_7ciahQZLAysASn2Q-iLpnGHK8hkMHtFfXxNNTfj17_Qdfmg75ZUNU7M7rKF4hl9OxK7bkpz6zh9dN39KJ-WrexiFPYZcL8NF7a28WkZxtsjcFRQZtlBE5BxDRc8Rbp_VfEaAr7s6wbu6Gnop5FTonUvfqpa8YGI39Hlz0EiSYwa_3bDAcjusMqRIzrpd7hqbjWI1ykO8kj3gd_cR9Xlca-Jshjh-XGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=L3YpyVbWucvBTzgYGcZFeR2wN1O9MK4JCgj5H9VDhP-U82_3Vook3ZMg0-pWjWnslhDKXXo9dixIfyh6QaebNMXfmdrN8W4kM20vnQuGKhXYTtXrE0c_u_7ciahQZLAysASn2Q-iLpnGHK8hkMHtFfXxNNTfj17_Qdfmg75ZUNU7M7rKF4hl9OxK7bkpz6zh9dN39KJ-WrexiFPYZcL8NF7a28WkZxtsjcFRQZtlBE5BxDRc8Rbp_VfEaAr7s6wbu6Gnop5FTonUvfqpa8YGI39Hlz0EiSYwa_3bDAcjusMqRIzrpd7hqbjWI1ykO8kj3gd_cR9Xlca-Jshjh-XGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB6dWevUAOp7lHZCZ-fOUpbuSdRtd2RIvLnPccfYuOXcZ97TpU2jyva4Sy66Gw5HIqJ5c-1iqB13iihA0SiyDVTQNplpXG_4w7bIFTqHn440qIQYrN7SSDcrAo0jBiW4tBNGje8DB45ZQeyun43tvjDt3iWL15o-zLAMnE9V2kxgOcX2FwBNhP3b4TmDYw8eAnHFXlEBb2cMZ27JKjLbuFivNGTGSpmHLQtOZOb1wIAZhTMsEOAjzmKAvKfgD64nPbnJ5AY3T3se8DmYoGfPDPiU01fV-Ynk9s2KybXXF8ujLuTXtq5lbQxfi8N7_nACYvtDLJR9XN60rPOiOM_zQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exiyEtKSzwuF9by6SaLOcDA3K7GPg7kQrg2SuHKaJ_9Cf2g9zqTPWaLMsVa6qYVqshOWxhBmQebEcFo9SdhyFd4ESF0DL2VGJxU6ppBCHBxH13RE64GrFQ0kBtPbN3Nx9363zSSvBVrS027dFh880QjmsCXxR1HjQwmavwHnXTdvoTvssJ0L4NL8__D8C882XlN2FfudYKFvSDfYA5opwP_lQp2UW8go-TtYRM7ZrlMCuSEKpH5pLImRNjcFwwKgxjCWwKlu-cahlfx3lfXf4jCXcIyWN5v84TtMGiXI7D_cfWU_BS1cb11c9E9DMhnKmSczKrZlXPJ1NrpO1L980w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D7NuskppQ70RViLB06hIBwe1tyr0vV2F8JzIOb0ybxcAr003QkpOr3RyyiAzV6OGATGojSWPL6ikbQhPnMF9NtYE7redyHYvNUBbeeHVVKDYczBLkesOinZep7CCPuGDdyDH-i_ttbdIiZzaj1LB-V62nGXhLs8KjCOw13uR5Xb23HxJnrCjE3cb64k4yVzaUJXt23__Tx5VAjMY3s9hKQDQK4ZPizuugJ0e8UWcFRjl6vfap18fOrtgGIvE77bpY_T4qKzAAquIsn1hSMSQ3YhBe-9rMXo5ePDGIlH-SMD11nFkQdvZ4jZtEABh7Kmtuawb5gTOIKxaDY0-WS-xaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HLsRDRzV9QY1AwgZkORHQs95v4oU3ajEFcDBCIa_lgTwikeLdiDYe2gVIuFbEpAhjr0Tjb7TP9CCnSufjNqlPbkfZtaEYSqXnldQtvBB-ded29QctNkmZI4nJ4tM0xVVWoYWImU5qbkPX8LpgVLPqh40_OsjCbfFfKZzN8dRdCYwoc7A00gHApxkSo8i0NjNdGNGL6lVjCCtiCQiUhe8cSHG2xRNaakUDVvJVgZe6mEqBDC_EkBzLnLZpAmODWQeb7-tGhJUwLk8wLZ9sY83eGesZAG8uHitPmaZl7n1iUSGQ5KqSMU1aXY4jUExMgpOpoIt5TvQkJkdGwtqfIVlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H4Yg6UEQx8aipgtQBXz6W-Zp937uLCQRZD_meiwRfzdhWOUfYRlDM7vRLpU-rlMCOWKkct5K8kfeC1bAGbngyaIqp-C6Wq0JcYkkcQADPre5bpfeWvaRtV5kETOtboEIGILG7Fn8r-k8cogwtnVXljbUnNreUIYEhQLgEc7mP5pblYuQ39Ldqzk2vFr02ft63sLViQ9NAC-Qr4pS_H6KxO-Z5nSWol0ltZXDAnW1CTJSs8ZPRB2ArGlP0C5cLEgs1jO7cv-PnUp9QWGlducGXg8APiQau73p6iEgiX8PdUQzsLVGiAX_uDOe9yK3gF4MViDv4e5RT2_RwprQaWMHvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkuMkiVTjd2SDxvLv-SuOXh6_lRU0pkeB5aukXX6daKX7QmkYiVEhJLOxVjycF0kh3hKlYhhAUTakmaHXYK3IlSz6wahIPzXWaRcNzNO3-ZMryhnrxxF_zHq--M2q1T1eKuonRbS6hQfF3pNLFts-sMsFAz20CjLrVcoqUrWIR2DSb4jdqGOq-jaO4OONEVdGpUpdgrn8WDS1h15Uz2mYBof-V3ygtH17fUHMI6t-ZCGElIh4F-iZu5RldjKGRJeBZiMp0oHnhO6nstNOXGxDEqnYxuOgWn-Yf0WR-ygYloiO06HlNPn8yRkuPVABdN3U76vc2sfAV93o_fF-jZPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnx_ZqjLcHx1HrF1ttcZxd83WJnvhW3MLUkNSAX3pilARll898xNrC5IWTT929EZhal7JeoW9TwIaQPC8YlvN_yhA-Co0NLz2IHVSK1w3azbIFCkd9phsPl8bsiHlt4Xfed4q6NN_RAz_Ap_4igPPYSvUNk6n9zCdpby1Gm64fpXeCgumzLGRz9N4BHtktNQ3iK1_cLfaW3tfs1Oum8V3xZp9EeXgnWsLQmV0UUug7YkQxv7SFt2dWwhsiNvTto2XGGEZlDAQAiQYkSMWJiBeiQorg-Bw-CvU_AgFyzJxNtMqVywy1GXAhVQlTaAk_m3ybePJrcvuMqMiFgtyPnXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP7iqIYrzZ-BkQdhMDuZrjyavOHdS9JQLh5MIFDQby1wlxAI2dqG7aMcvXWRSLmwL93fBM57DGbYB22CdbpooPM5CTcLxHCTi-LGu-B7QfCQ2u-PnDR8cnRAoPvdPOWj5so-GvwyGbhkWrGKKNYRcIH0y_GGuiMV14GYSToX92wzv4uFST7Q9CPFuJ0XuIDmcwg5mVBl0kfgY1pYtl69198LaBzcMpHGOG7diLZIifeWqnUir6q54_J08MZOx3gSF18C9GdzPic39Oq2LwmRvg6zXV5fPD1UbkT5C_QFTt2S7doQw9GmAPNF7DOQYmQ_lDaHYz9RGCdGn6C2r4PZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgau3NhxLYyPd04pzjXWhhGO5mEOT1-ND1U9zjJ3fsLzTUx3a8w6KyWkVa2EFUZO2_WgQ7J9d_40BrMavK08-hF75qtSFTyrWKexYyJsKUdX6hgBrRtzKEnVWlj_oP031V82wfbont8cyuF_YSJEPOTIkcwo6xeP_Dun8QxV6YxViVuje3Ig-z72XQD2_mUcAiTx7GRHRUwOIrCEXv6CGHZYSakHP5TgW9RzPmDIJtR78qT_JqZ9fZipCNG8kkH9RgpoREzEKITe8przh4UIkKnzmJqpZXGkKJpcwlUa-gmvaQYCaapiktIwIdWYVjpIfwy3eRN54StOCwBhZXtfNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubnPVyhCCCg5SDIRaZB0r1wiwoQLhS8da1QQtmM0yZcXRbt8OqQLWa-Jufojm1aK03KrUXeDcFBaFytN7zBLmG50IbTOgvifECiw-0dCXT0Ie9mypHEppQbGpaM0W0bt_cSF9h26ZZn55GqfTJ-RJS8eI6AjhVsgDexVZQF00X2TmgER0Qy3X-zJHyzYty7hHxY6D6H1RuL5apvPXnYKCxtmL6dbGAz77aL-BAIegTm2ntV8qR6ES9kaNFgqC0uANclBnQVa6yp8DYe18_uSxDrN5-6Y3wwyU-1gO1Fv9UAFTRTdQ7pCiz8VRr936DX42k90B0UPVkfO2GuzLCuSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGHBmXcIQrXTEhFSpsrhl4mGLiYtZioDOFDF21lKrqwbxcXOvk19Alndd_zlIpCxEQl9gjYAaewe_mfcyRl15dFUcedoOsDyj3Vh9PSXnkZwvkzeBrrq-jEwqHUv_uqFcn0b2TbcKnFornxxzDFYmIMLrWFHZQw2QOZm_8XDIYoaEvfmFvyBss_vA9eU2c5wt04C06DiQ831fsQhha1KInw3NuXycvWaG5G0dCVYQ02bDqJl0RKE9VxQh5z1adB3Qs_Jga0T6tpFSYHDikyCJmBEWXX3pAWy13W_LXB6pDV4RoegXRw2NJ_brMid9tNuv7PDxCHWQvHWKqEMnGXlew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH15SscWBSNROntXz8dZTAfRXGR7rEpg9r7SPf8C_15jAgUOdiMHf_FeUIFBpOanI_SS2YOLin2umJunwdJNtbaEArjQrgp6Em5K-h89mScCdoKOO4M-zRMn8Ca6IpsezsDUwVuYD-gfEUG9dxiUnp7gsQeDZAf5U3yCjO0HBidPiysu60vO4QraDn28svihPa-xhC0QhcB0DKh7qGIpacGJ9CgH14qMbL3BZ2oi1paIQPxJnENefmvyN6EojFsM_rBrGroxjPUQte-yrW55kK4JQ1kxtQkretD7r78V2_XxupGa3v8_iaygJwVD1RAUKo4ctC592Bk6aY_7Q56rJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=oDBeEOsNED6kNQ9IKJEzUNNvjBqEV7CA1zeRd4hl53XalZvoIMZx6PTmG_LH2Xqaftu9cAK1qCOMPxBXv-3sQqRxKRBUeU-ZROdUjtXy1AZ_rKy9zJHsybiVZgDBNPmZy24eDV_zLaNSdf27PbjsWxSmd6aGKGAGbEPL3SkCgVzJIPAgq-wiYu60R1xoliiMPy_cJgexNcztkEuBh7AqPvqWdQK7A7_Y9FhRTIkER5y2szOm9GHwx5ILPlSdaMkgjWLe1NPxpV4raDYralBGKJg5jkYQXRGgJTS28i-RInyydu4EOom2t9e5xLKRbrwRYEA_RwDtrYwMTOLwn-1z-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=oDBeEOsNED6kNQ9IKJEzUNNvjBqEV7CA1zeRd4hl53XalZvoIMZx6PTmG_LH2Xqaftu9cAK1qCOMPxBXv-3sQqRxKRBUeU-ZROdUjtXy1AZ_rKy9zJHsybiVZgDBNPmZy24eDV_zLaNSdf27PbjsWxSmd6aGKGAGbEPL3SkCgVzJIPAgq-wiYu60R1xoliiMPy_cJgexNcztkEuBh7AqPvqWdQK7A7_Y9FhRTIkER5y2szOm9GHwx5ILPlSdaMkgjWLe1NPxpV4raDYralBGKJg5jkYQXRGgJTS28i-RInyydu4EOom2t9e5xLKRbrwRYEA_RwDtrYwMTOLwn-1z-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZ9u563krVhBtq6KWBO-Q3KjVfZ7pvhLpKQWxVn6-4GQk6C-fPmUppUWofglkZNcrqsuKw7vxyDveQlfg-UmYc9w24EBp3thuZd6PAPgk-0jgQfbf29lnEcKlG5Sf7dWsvWqciU48VOR_ujntY6IF0tw4rYoCtJlNTvfdzXOTy6ToYvk81sR9uEp2RSN6osDdo08TtgEuLX_-kctEZo31V-WhPW_S8v2DM8bPlNw5P2QzsIlED90RMp7D2jOWQHEwjWYg5yUz0_c_4_xkV1lZMWULQGVa5CCTRz2w-UON7UZxX2mkMG8gLVywsuN3cSHubiaNZgjBTd7N1RPPHxeRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=juogm2TpICxTXHXRnm0A2rPYlJiHMlkOG_P0-pBDuJVhRF-uQoRzC78CPzYdgxfsZwI7ZMTDEAigP58r89o9bGi6fh4WH4Q7n2oWVHc3xPekeZZi6-QRQnFP_apY7nTHoeZ6Qa9HE9c4UlU8O7IEOaF3Z3hGPGQy149Z1WZWKCVX2qRZciEVwO0qvHj2mkn749COj4zr5SEHwmqaD_B5im9SN442Ho51zvZ5DrwQqoJbaO1U8cqTU8Gkp0Pr0RolcQEdTcP4GwjdaReziK1dNO1C_7lh7joX5mDH34YJveT4XMbYpckaJxOqRw10u4SQxhHyoVwJu2MDSzLu8bETzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=juogm2TpICxTXHXRnm0A2rPYlJiHMlkOG_P0-pBDuJVhRF-uQoRzC78CPzYdgxfsZwI7ZMTDEAigP58r89o9bGi6fh4WH4Q7n2oWVHc3xPekeZZi6-QRQnFP_apY7nTHoeZ6Qa9HE9c4UlU8O7IEOaF3Z3hGPGQy149Z1WZWKCVX2qRZciEVwO0qvHj2mkn749COj4zr5SEHwmqaD_B5im9SN442Ho51zvZ5DrwQqoJbaO1U8cqTU8Gkp0Pr0RolcQEdTcP4GwjdaReziK1dNO1C_7lh7joX5mDH34YJveT4XMbYpckaJxOqRw10u4SQxhHyoVwJu2MDSzLu8bETzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4FiaCUMVkQTxlNdVQEFFH6xPklgB1arvjnYKoFtRuRJyS1qB25_-BVMA72FbV35ouUbOXPWrSCcfdeVNqTjH8HZKpMrk5u5DQjKfAQoe6BMdjt9dV--rsE9nSw7kx9xQcIUa5aiC_2JcB0rg1aV3qq-Db_g5pdrZ-QYolp81sN2ofHAMkd0_xxrFGvS9Bala6xxByVqw9ULOkhU5JrgJB3EUFlAoo9ruEXUy7kqO4Qx0suej2_RvXbnE0v3p9iBIP2zV91ve6VodbcFB02F0DmUQVef-69TUOAZfMJOf_4q6Ci3QQ6OLAZaXRDLSuOmyYuV1HQKFymx00DK_aCcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=nIE5kx6iHwcJF_N3N8534HlZgbEODZKhpM05FtvYDvVzaQ6yX9_mScdSAiltfycru-EYeen30kxALiJse5kn1PkIg20OAWuNJPxddRsKh_bCrlGzjocuuKkK_b89cvUZEP4f1D-01m0RnpfcazwqNU-JA-7zPsnE1p0LQL-RWkLiHrrL77AW8YJl3WJ21bOaMJLLZIUtXyS1nn19pIF38oDpWimkKuiHkiiN73NwtSON79F3Twh1gMsHMkvJShEX59GZuhe9KUrjWXa7DNaB4YkrVIDvs509oU2uODZAa3C4-cQXfmegqdMIXp7lB6ymYk_Q401monOz0XAlf1WxoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=nIE5kx6iHwcJF_N3N8534HlZgbEODZKhpM05FtvYDvVzaQ6yX9_mScdSAiltfycru-EYeen30kxALiJse5kn1PkIg20OAWuNJPxddRsKh_bCrlGzjocuuKkK_b89cvUZEP4f1D-01m0RnpfcazwqNU-JA-7zPsnE1p0LQL-RWkLiHrrL77AW8YJl3WJ21bOaMJLLZIUtXyS1nn19pIF38oDpWimkKuiHkiiN73NwtSON79F3Twh1gMsHMkvJShEX59GZuhe9KUrjWXa7DNaB4YkrVIDvs509oU2uODZAa3C4-cQXfmegqdMIXp7lB6ymYk_Q401monOz0XAlf1WxoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=F_X3avM7iz3vwAypum1NdSmEf3Fes8aCWNZ8ZJ3WEfGRpv4YxfZgfSBLI1iPLsc8wK1OBgS2rlPGylORnHsxpPXpUTVthIqtDz9EbTLrAHcBVBJGe6eK5IncsX76bRaKJRVs5Tjbfhasa_kJ5Q4REdKQjKgHebUXtMT2So11jMcxlyV_Mh1CsH2fxwkjdCfXESgX0aWeZJAW59PdkcwzmQfvZ1J0iVzwA2EkwPUn0VqN-T5ybLb5-k1kDfMkt7hVbo_AtGojpHT9mMzwnWBM8qEYMFB302Gs3kK-1_Ir8wtrWz4dEvQtY4xenY62zw1v8lhbUKeWUFxy8hzpGaSQuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=F_X3avM7iz3vwAypum1NdSmEf3Fes8aCWNZ8ZJ3WEfGRpv4YxfZgfSBLI1iPLsc8wK1OBgS2rlPGylORnHsxpPXpUTVthIqtDz9EbTLrAHcBVBJGe6eK5IncsX76bRaKJRVs5Tjbfhasa_kJ5Q4REdKQjKgHebUXtMT2So11jMcxlyV_Mh1CsH2fxwkjdCfXESgX0aWeZJAW59PdkcwzmQfvZ1J0iVzwA2EkwPUn0VqN-T5ybLb5-k1kDfMkt7hVbo_AtGojpHT9mMzwnWBM8qEYMFB302Gs3kK-1_Ir8wtrWz4dEvQtY4xenY62zw1v8lhbUKeWUFxy8hzpGaSQuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ7UrH-H_n4kVM2JPw7OsXRXduum9B4hrI3btZDmj7xxiMagO3PvooDd4Xeb4OpUNob2yrI7H1e3Jm7MQiAEcaw8GG5WRZGxHVo-f8E1TbIRRz04mTaOe9BEjfvPxuufocJR5VRRPP4GJ6w7d5Ob473VD-bGyMajQUNIxgi1TDG0Uzvz0zIQrcp6A99kRr5nDgydxoFCu3JcRbdY7-riV2sX_hMbhF3_auEXYldG5t0YJSc_yUmshnl4HzYgUqaYxrtjFsk24PYbEpDfUMM9a9CWE-J9nvLIp7izNgJA1N_r4o1nFO8hYi9DjFY8gx9KuhSflHci-9xcaCAympgaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJFiO3zyCchMF2It_BiJAsuoUQN56dTY5hLWAOBJMDC_5-iazwZ4QwNr4rH8QNAG6fAGVQ_plCElyOihzNKhHAx7UIgbGpLo-u6QIt5leHtnRkyVwCkNcbbNo0IIHRg8xp7YS0oFtV1O42H0pLpncFpBikyWHPQbGD3YQh8YvXR8cw3MTIzRrF-SkYR_yay-wqYYnArvSCIrEGinWrmje33GP_MRx3-_LpiptV_g4S08mHb34MUwLpFmlwiaAW-ziGnI6Fw9k69grxpJ4cr9W2o30ElgKBEnWetbWI3twZIh6ESro4lLJIEO4fkaq5Xo-Um8ibu9J1vSMCHvGRf3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFSDhbPFRJdntqLj5wMW-RlH39QL8xxqEG4oojag6IxyIEN2rEU2eI9lOjwAzvV83NclbyeVFp5d7rjmiyJAD6amhV8izwhmtRPAF0GrMnW_3OsX1PClsVDWL7PapUhlNFa6jbyYUS0q8VA52CueJO0mdOhJE32f_Fy2UkNzUWgNh8uBBH4y8hgCvD1Fonxp5MwJYiuWz5TkvbkBHlKlwY7MVE4qvj5vWNT22qaeXulXe0z6NHGBCdejmICHg_s-jIsYNriYA2ZKf4kVWJHNoVGJHgfzcXPkx0jp9at42KDSr4JgzgQnnc6IZGSQq_IF63YnajRK84cdSpiFQM-L6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6wxBGJnkC6DSnigst8bB2aM9om90rIb_OiyCcIOOVeaa8lykgEFROEBdnY0918p0_w7IrCrupDLFYKdcB3B5q0WS0OAJx5Ri1dnBcZ2MOWbznVp_lw7cxsn5Mw8p2aqoFDInMg8sMUKVaZAADvrJAz6CPWR72QV1eW73QxPF9Bv8LYh3FNgKhwi7aW6Y_hKOcALfwWBbvJIlN2Um5BEzxdwbIC8hBuYqjcL4nxE-Jt5Gv0V8h0-ummQ35RX9UglFonnCRQpuq4HzvIu6DLhR4gVmOcKGUrZltM4S_kLETdNL6cgshFyADcy6S0nRfxpUqoptrX9BiAZxtA92oEZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvJZ0AzsKn5HEqkKZHQDOcZg4PPSa3za9waafMyGoPUVODEZ_9C-YWx6_uWhJRCK2p07KyxenCnbnpm-MGaJlxfjl8wM_eLaE1nlNFYuYxl9QMQBb1OoRqblwqKA3WwykOkm3amjtRcItPNbDDuMDJiIOqSR2wG7OXg-ERFeMqlhMLpaJ2C_sXkyy98ORjD-Xug4RTPDCKfpSMuLaqNCUT2UzSB7jdT5sstpl8lglmESZGW2U4ryUl4skUlp5BraSKdNkoyuoEQVdeBH7J0gZHpk6dl4NSMV_q2yoLLwiheQBocufo8riDCd32bfEVoByPLFq_XfuAWj_SAfBeO8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hM432MWhmLdsnevgcoepJRatmPDE4TRnOylRPrAm2Z2HeIvzbrqLji7thUbzNpkaQhUjIozO04M-VxN6zZ_ITKVaWeOScxpgkWSiKEC2pDFoj6dWZVSA6p7S_r6b8bDWKG1O0lPZb5TEVDm4pbbacq5Yt7tpJUBECfDYdXkuuOldm11OzytWF8XK2Gky_onhKOGBTuqrdYY1nBj4LxQ_Vf8A-wI1Ojjsd_6-NulzProOMWDeSvfNjWO_vMLh05O4TXMS7iEIOcqOHniBKQifSy4IicYntGPlQLR3Pie2Fpr_EgdX4Z0TYhgJEP0nsZTxYcD8fhvuxA5EfzkNoBqYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9KYi7kQHHvZg9V5ZEn7iio6JQ779qHZnT8aAuRR8wNSLHaGNiSt77BN65u4a7uRXG8fYnFTubw-Xcl9HYZmSbiCpuHTT1v9I8ax2xzZojBjqSfSnCTmlnmygP5MbJ1dIBxC_RV7xq9_15S4E8_CVlvjppSQqxvzKGPMGnxp8R-In-4ig2p3dd_RuXWsbddQt4TPIG6JeZFI3Jwj1LnMadZaR-RztB-10ybqosTL5nvwywxJHxwHFsBt1o904-1rj0SUs36q_IhOvIgnNVnN_7CIwofI4ThXrWuUyREjiLHac4HUIGijtYfYg1dZpN0hZvdz7dclqn3NG7k0U6zv4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLPBEreIV31MPz8INXtuLKycoRskGKmshGGM66eWDlRBhDnkE9dJOLqX707ZoOdOTOzgfCoA329qnFPZsBWIbqXpEDTp870p-R-i6PGTXN0_MK-gJC28b0a-1-yXEEMyOxOouG6B-F4NTtipDM4WU53LpU-z2D6lC3Y8cdIBDUaekbABUeZj_5CZJT2AJ8_VY4buQOuYpj27TDX4xQYH5QtgJtI4V1w3KgYfLuoD_Fck-tI8HCGsKg5k_wLyzkTI_AimXbIs6MUVadCLaSMoromrnMW-Yq2_ONrf0tCxehzbCyGuFX1JKLCvjzq5kubCFg9ANUIHscLQO3N7h2jpqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=kibNw9wsIn_01td7cNmzHns9RlMw6s3IEn62R54HH8t9hg8ZleIEapiOxJqnZ7MPJbT3HAbK9J7tkhL6GWjLDPidof0sZK3p2P8cTMD1RUNabkULoHfOm8SlEXXH2pQl2ukLm3UKDEcTUSe4BvwKh_Ig-2iH_Jc0N7dV3P2tYDq5smFZxbtp6FIyOFnZADmNhXHPXHBuUbCmhNkLpFI-lYID8Y8x8RQ4_uw1FG0V_LekLAExBcuTbGTVoPK6yFH99ZU4ckxuuWGq-qAClhGuXSC7p0mAQvkkFia-GsdiAi6svtsUzEOzSWn7afEV2tJj5yhFgcIprMB87hTD6J6vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=kibNw9wsIn_01td7cNmzHns9RlMw6s3IEn62R54HH8t9hg8ZleIEapiOxJqnZ7MPJbT3HAbK9J7tkhL6GWjLDPidof0sZK3p2P8cTMD1RUNabkULoHfOm8SlEXXH2pQl2ukLm3UKDEcTUSe4BvwKh_Ig-2iH_Jc0N7dV3P2tYDq5smFZxbtp6FIyOFnZADmNhXHPXHBuUbCmhNkLpFI-lYID8Y8x8RQ4_uw1FG0V_LekLAExBcuTbGTVoPK6yFH99ZU4ckxuuWGq-qAClhGuXSC7p0mAQvkkFia-GsdiAi6svtsUzEOzSWn7afEV2tJj5yhFgcIprMB87hTD6J6vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
