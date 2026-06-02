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
<img src="https://cdn4.telesco.pe/file/pUdZ3zBioOzRsxJo2WVcvnVfoAvoJaQGSPR52ImHFzLgNXWK1oWuAYXoErm29hY545LbsLyvhZt8lgWI2pSIUdFnFg9mJjYmMJZ3b_j91hl7jahyPFPrO_uBpU_Ng3-Kl6xy8ZzkFYjX9xl3HBCFBn51CQoTsFuPCkg66zl4q2uLYgItnAoI9XuH-j94PmwMenia1vYLWKVHw8dkHg9Oo82YsYzXnO1Pfqg1rj8u4SPADi3k4jOWF52WXaJ2TayF0N8vArtexMUrqrvwIZYM6JiRdA_NAinozhJ5grOyDixlrmxLEOyUcF4ghBAcHPQJV8_fj7TyFhIBTv4iwNbSOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 212K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-65240">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etu05lbtOvyBbiUa8o5fbQR7tmHbcxHgsA26GYvtaahKgW4-TnZwHfvLR5F-z26I6VkJ6dPeMIMgsQvbfVflzMaq2vnwF8Sou7nw2b57qKiJIYE9iY_IbvJemI0CY5Eh5oVHlRatxNOdyz-SdUxf5ISvSXfm_NYG7JPveZsCwZRQlt8lfCRhWva5Y0VCdHR8N3uayZlSkqnSCRnhmyJN20gRTzvy7PzeF80mRDZ5gnX01rpSUx9WlaTNC3t10AVsVz-HB9cF_wI1w_N3Qkud3PXBm0griCI8MVeDr0JQzOMkMebvQVUF3V31FKnCnkQjc1u-ZJoJYFWYT9OLurKwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق آمار، سالانه 60 هزار ایرانی بر اثر مصرف دخانیات فوت میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/65240" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65239">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/news_hut/65239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
#اپلیکیشن
اندروید سایت جهانی دربی بت
👍
اسپانسر لیگ انگلیس
👍
🔥
امکان شارژ امن از طریق کارت بانکی
➖
➖
➖
➖
➖
➖
➖
➖
➖
🪙
همین حالا عضو شوید
👇
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/65239" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65238">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ax3l_9pjVyrvlUn1BQAFlYod7_6PkMBscGDNQsgvupI30KklaQKN4g5i2PM6ihZpwBZVZcSLCPs5OFL_cIm_iOTRWiDeFZHwYnLtcC-DrCfmzM729l9wrN7MwetzplqmHwVVlayP5R2_tUElQMmPqn6oam1fGi8BKkPeB2UJPlfwGe_BwszpQYleV-nzXVeIodiPFrZvPF_3w_0m9KVZYvrZG5znwTMokyA6hkY2UQLMM5BIO_4j0Hes0sEXjDFkvzt0KnWLyfZJN0GXWPUXSlNHq-vWF7K7HCVIWx2Ggd6wiSrjtv-WxAt1KdX5Afl2l_rCF8AY9_gK6KSes-sgXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت g12 :
🪙
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/65238" target="_blank">📅 20:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65237">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
امتحانات نهایی که قرار بود ۲۱ تیر شروع بشه جلو افتاد و رسما از ۱۳ تیر برگزار میشن
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65237" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65236">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMscHHxFCL_aknogGU6wZWj2I7hoc_hGzYx267vywa0REDajKFUI36B4GAxoeIQsReEQ1LDc8PBttBYvBESo9_UnXoKB7uWeXQSneX88EF_IyDDWmI2THIQBZK3By7i24eKRSir_Lp65j3RhSsxSN2ymLq9YmuchuzxboZlq0jNI69TsLSGm4uNCCc6kaFSK4Gf1mIb3HLTyQbb_X_4mRqtBuvoNkenN6fPhA4xW6OHGA1H6FjdQPn3TUaK08qGyDwWTUGPaoy1AUTesAfA18A3QLluPsSsaOmYQqjZAZiwcMmx-jn7rrwSztIl5YnsDMrLIfxwob6cIOx3TzSSFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
داعش با انتشار پوستری، جام جهانی را به بمب‌گذاری و پاپ را به ترور تهدید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65236" target="_blank">📅 14:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65235">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65235" target="_blank">📅 13:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65234">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65234" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65233">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65233" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65232">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65232" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65231">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65231" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65229">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65229" target="_blank">📅 10:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65228">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65228" target="_blank">📅 10:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65227">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65227" target="_blank">📅 01:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65226">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/65226" target="_blank">📅 01:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65225">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 اخبار جام جهانیو پوشش بدیم</h4>
<ul>
<li>✓ 👍</li>
<li>✓ 👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65225" target="_blank">📅 01:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65224">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده آمریکا یک «تماس بسیار خوب با حزب‌الله» داشت، که یک FTO (سازمان تروریستی خارجی) تعیین شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65224" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65221">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbl4PsbquC4mz0muOoRR3_DoLGEa_FvWKedTndHj8LcthbwdHf7SG_BEevZf0Kx1WUgeeUsmtHEBtBcbr5Dy8uWSKwhgnvMpw3zzj3bL8m5DUlPWePJCYLKRxeKyqwYqNA3pCo-83G45BJJf3Bt-uBhMKAtWbzpCsgbSdb-SlP5BhrbmOa6RcN_ByJiXVS7QiE7Y5U6OjLJOXwvu_c3bviF8871niK8sp_DHmLfmy1nv5g7P3yM8oDDUkuEcXGb2icsHxesKg9_-SvOCYCnGd9PKnktvOxXMmwIBuYnNj4zs_396Wini_Mgz37fA7m5kJN4qS58wuOnpWz8A6Yp9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: گفتگوها با جمهوری اسلامی (ایران!) با سرعتی بالا در حال جریان است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65221" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65220">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZFpjN70IYsebvtxBxl1mdqP5GKgjE5p5IDIYuvOu4y8iZzJu7wueogz52H5Ijb4OH07BecxZCcaYH0KUGuNXl575Rr57ytV4NSdMaLe370iXT_IhGQ5i15_1QbWQhmrugBAwZng8zr3NVk_DhiIOyJBi56qUkFWPKi1IQGkwBh3S186BsL8gLssm6eDRvOMmInsYTifQPUA0DyNQgqDDaTiGTb2ZdIrv5UnvCuFb8QatH79TK_bzlsqYnT4JKGSjtQew3j61aTcmgac1FCRs1liZuaCJAxzJx2nYunt9w6Du8Ib6Sei43P39qkdaJnPeCDJsdCOpg5Lupf4G8spDJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فووری
؛ ترامپ: با نتانیاهو صحبت کردم و دو طرف قرار شد به حملات خاتمه دهند و آتش‌بس را اجرا کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65220" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65217">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDD1ovtvFSUowgsUgJvBa6rhB3S-xq1kS17DdC1rhFt28ILdWnuY3tJw7WRPkpDnbuN4udE_BaLr3M6EWGciqVuzp1mH7ZYGhShJnaJ5cRFMEMsOAQlxgcIX96Yh2onc0nweG-6SCr_Bmo79pH_jhKxS9WQbTI01b7PIDCEzTotcHkLXC-wjsuzR6uZlcoQhyj8A9ptN6g2nthHNzT-yd_hO31LyZiBvuUXpkW7IoFxhRNajOmeqdktrR0mR6ou7kIAp_tYY6mkS__QOM_mp1Ilk2nSH584TjnhBrtzw7HlHdh8AS0uMjX7jMyMDO1n9QzGyBot8TpYZ_ybqr1DOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایزدخواه، نماینده‌ی مجلس: آخرش که قرار است فلسطین اشغالی را بصورت زمینی آزاد کنیم؛ چرا همین الان تمرین آن را از امارات شروع نکنیم‌؟!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/65217" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65214">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
📰
مصاحبه NBCNEWS در گفتگو با ترامپ درباره تعلیق مذاکرات:  فکر می‌کنم ما زیاد صحبت کرده‌ایم، سکوت کردن خیلی خوب خواهد بود. سکوت به این معنا نیست که ما شروع به بمباران کنیم، ما محاصره را ادامه می‌دهیم. محاصره یک تکه فولاد است. فکر می‌کنم تا هر زمانی که آن‌ها…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65214" target="_blank">📅 20:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65213">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65213" target="_blank">📅 18:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65212">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IiqwHqP9XrRmTeixN68z_kYePBSSjuSAqLheIWUtEpgFEUQ4ih9rqIvhRuPdA75K2Px-TWd097srClkooMXgOrc_EDWE4WU40KAbwy5GPZ8SjzuOYmHYQ7kKbQtRxndRDsFKe3S1s0QDyAFKQbz_CuWFQD6XsZzciPxHQZdI2Iran1bdyK8YVJc99PIahAy-BTU8NU1KUqG39IutTq934Vdo_zaF3r7EUtNp9WQogNVl-SPKeWVlThm6Q4UQZsVa-CVAxuu0FUDe19WWOaFD9YCy2joY1yf6Pid46G2gNNd42y6s8FEoR_XEXXsJ-1JAYqt2Ys53sCcbf_Lda_GODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سنتکام: دیشب ساعت ۱۱ شب به وقت شرقی(۶ صبح به‌وقت ایران)، نیروهای آمریکایی با موفقیت دو موشک بالستیک ایرانی را که به نیروهای آمریکایی مستقر در کویت هدف گرفته شده بودند، رهگیری کردند. این موشک‌ها بلافاصله منهدم شدند و هیچ یک از پرسنل آمریکایی آسیبی ندیدند.
فرماندهی مرکزی آمریکا هوشیار باقی می‌ماند و به حمایت از آتش‌بس جاری ادامه خواهد داد و در عین حال از نیروهای خود در برابر تجاوزات ایران محافظت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/65212" target="_blank">📅 18:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65211">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeOFoyaLF0-hDqn0nlgfOW9IB9sgYjN0AIHFoZgA__QlBVKP7nMKkVpJoDcm6c8_8kr6IigwYvDpLKbSFAUk_yqkZ7O6hRhfavfa5xpotUN-Z906HSt7z6kCi74docBj84C5d_g4YBou_NrS7RIusiqOHmkTI1McFQxHf44zXgR0pgTOFWaGn1LjHcRCMB1dTCVjVgcRFCcak1omOzUuNidTpV8WMarm_uNDQFFI8jjF4s7EillRB6gZCb8JJyPBMXWhAr2Y1LW9NAyC94xD2xHMD9ipbsDQrb5gXhMQOy_jQ2yALnpn82Fxoie_pHn5s6CCFx0VTGmEL7dqrP6yyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس فوری شبکه‌ی خبر به نقل از سخنگو نیروهای مسلح: تداوم حملات اسرائیل به لبنان قابل تحمل نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65211" target="_blank">📅 17:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOxHRHj1RoJ2xH4GmPrFVgPAY3rpQmgggXvOMLTSaX6rTZYfZYZaMOcnDnFnAw-NNE1A41Eji9zo9hE6dc0AGvh1YGYcv9dkSMRNtPW9haFJ2qHiA_-wCTF_pKsuPZWfAGh4aAB7m9CxKNJOezzHhKf7G1JKKadUHQnz5YfTPjYzQf94sQDy-pp_2i3FUL6xTDyfoq5D_5V6fwb40gf7McJjLh8TwN1YdmgA0gs9wFxISo8DVMl5TRy2j6SFUJwPb48t_nAIhMr0MwtNdszWSJqhbj4deHWQNVmP_p4IXK2recdqwaEM_Ad42nOUSTgER3DKYarPtk87yhFQ36dQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تهدید امریکا توسط باقر قالیباف: محاصره دریایی و تشدید جنایات جنگی در لبنان، گواه عدم پایبندی واشنگتن به آتش بس است و هر گزینه ای بهایی دارد که پرداخت خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65210" target="_blank">📅 16:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65209">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyBFegYa8LmDIjkBZ3aGZYocBMzLmYllXOYo0Bf_qi5wl2l-QGjJpiNMmu4xpLBRhDDs1uef6GvwFX15fUSpWd9XMF0LH-ecwT6V-RDaUpgfCkLagktXFe-RXanYoVmJrhyPBm8mZ-mojhLwSj-5-UmCAjjLWr-MUPSqfZp6S-udK7sKOJLR-uRASSZhutHUJIP8j4yiqLwTRFxU077cDVHP7vEypCusPUHWql60WmYpcU3zBHQj3tzjnN5GhoNsez0_ub-_c5vHhTX-1wMHsQE7m-k0SP3JBcVC7pmPTNOJYxiWJv1E7Zr5eLcWTozABtc7zoqDapi3kAI_PdRQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی، صبح امروز و همزمان با اذان صبح، مهرداد محمدی‌نیا و اشکان مالکی از معترضان دستگیر شده دی‌ماه رو اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65209" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65208">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/65208" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrk9z2EKPKeU2UfDrwoBxZAZ771ZkGa6WuLU70Pp6YiQI0_u2qI7A3NoPYUpEWBIPTHi1a6B7ZEYLGJ91EjIuvhraP4WHY47fP2JyKAXUJYeuRe-U75WvFIGldowIVZMAvEV3SEF2py-03JhAGBv1sWQzsAHqbyYLgjyVBNbU_vvG4axXCev4Ct2tBCpaOOlKHDp1DsflBCfT1drLtgGDriLMwDTpUyRprs6SZDauBxHNddlwdvkYsWQ78THh9MhwxYWyS5RQAzUNYqUUNVDpLg-neXvLwHX-7Tq4z6PJY0_ti_rM0c8ClQGMIBWIig46URVhMPB_eR5d-hYoOnD3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65207" target="_blank">📅 14:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD_Osb6jotLrKZPno9WNi6lloV67FM4yWFqepdGmqAlRN0G9KWoWp3moQVZOa4Ee9PtdxT4wlL6u2sKeP-hioqbvHjq6OPhfjujRhR7ai0zC1l9CZ2dGn3Zi9d11yPzaxB2vr4REsmYnDWYA3fY0mziGWoOkanyPm1Gay6yRW0dtnspFPnRKowhydoo56R-srsQGqGx1rBk6wi7E1DHk_TMMRrnoruj8UmWJP_R65eYAqGYYfhmbO2CscJs06oqVpjRqnMckawerxh7AuTVh2cUfKgUEaY2WnAXcCM5zq_xn5GpzsqNhx_BzwcsRf-Ud_99zRKBHHrQL45Bwr1bDBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: ایران واقعاً می‌خواهد به یک توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهانِ به‌ظاهر میهن‌پرست نمی‌فهمند که وقتی افراد سیاسیِ فرصت‌طلب، به شکلی بی‌سابقه و بارها و بارها به‌طور منفی اظهار نظر می‌کنند و می‌گویند که باید سریع‌تر عمل کنم، یا آهسته‌تر عمل کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست وظیفه‌ام و مذاکره کردن برای من بسیار دشوارتر می‌شود؟
فقط آرام بنشینید و آسوده باشید؛ در نهایت همه‌چیز به‌خوبی پیش خواهد رفت، همیشه همین‌طور می‌شود!
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/65206" target="_blank">📅 14:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
شاید باورتون نشه ولی ترامپ و کابینه‌اش همشون خردادین!!
• دونالد ترامپ: ۲۴ خرداد
• مارکو روبیو: ۷ خرداد
• پیت هگست: ۱۶ خرداد
زندگی ۹۰ میلیون ایرانی تو دست خردادیای مودیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65205" target="_blank">📅 13:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇺🇸
گزارش سنتکام از درگیری‌های دیشب بین‌ امریکا و سپاه در قشم:  در این آخر هفته حملات دفاعی به سایت‌های رادار و فرماندهی و کنترل پهپادهای ایرانی در گوروک، ایران و جزیره قشم انجام داد. این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65204" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=StAjDNLvDV7RgB6fBwaSK5tebUcfYNuqNceI1jxjv2e0f7JnFahMgtjiXlK5w71ZEFUOQUlCuCatU0HpKzPj05hZ_pQo806SehPocx0OyZUYCyRQUPApRSOYY_ySpfU9FGLvwWAqBVw4VhxqmUhAqCnZYTVhRf2WXvakWXaXTojvn5BBTydPcbOSSgIeMeMpwWv_qoUxa9aOCk5Dih9_zDAgUWu9pcPuUzexmcF0IeMhDrlh0dqMLQVg4HmsWuvnL7BhYsBL9DW08MTDyt_7XXfbvfyZNi3xFl-g5SSJnyORSA8VvyCPAdhN72lRlRkzuAXJyI4bq0aXlskF3ov6xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4c45b1ee.mp4?token=StAjDNLvDV7RgB6fBwaSK5tebUcfYNuqNceI1jxjv2e0f7JnFahMgtjiXlK5w71ZEFUOQUlCuCatU0HpKzPj05hZ_pQo806SehPocx0OyZUYCyRQUPApRSOYY_ySpfU9FGLvwWAqBVw4VhxqmUhAqCnZYTVhRf2WXvakWXaXTojvn5BBTydPcbOSSgIeMeMpwWv_qoUxa9aOCk5Dih9_zDAgUWu9pcPuUzexmcF0IeMhDrlh0dqMLQVg4HmsWuvnL7BhYsBL9DW08MTDyt_7XXfbvfyZNi3xFl-g5SSJnyORSA8VvyCPAdhN72lRlRkzuAXJyI4bq0aXlskF3ov6xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف در پاسخ به سؤال میگن شما پشت پرده مذاکرات هستید، گفت:
من اصلا هیچکارم
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65203" target="_blank">📅 10:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65199">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بر اساس تحلیل تصاویر ماهواره‌ای CNN، ایران ۵۰ ورودی از ۶۹ تونل موشکی زیرزمینی هدف‌گرفته‌شده توسط آمریکا و اسرائیل را دوباره بازگشایی کرده است؛ در ۱۸ سایت زیرزمینی، عملیات خاک‌برداری و پاکسازی برای بازگرداندن دسترسی دیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65199" target="_blank">📅 23:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFZw6xltFMRKYN3oWH4257VLpiv03gQle5C2kZHl2JTyOq_eQ49PhDfkwzGSAK25u9Mduqk4g-JExwFQzPgfLlmOivT4OMzf-T3ZMUHmC-vNgQDx2eTXL0UUqpOcyes1L8HNYn_10T6IJrjzJCkyWQVETqMYI8LrkWLGVVr8NGyl-isY_s6Rb9G-OKF9j6oS7EuGwNZ3kaOeACXFBJXqyvfEUVthwX-dW1TODmN2PpWXUaWSaE_tZh6TJfRWsRvuC6DSf-Dkc9C6Enbn1giI2o9OKqSFyORzbKV2gQgfiHq2Vo81nJjdXyiHJajThjl6BZKbeCfGBISnuW4uIye4cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طباطبایی، معاون پزشکیان: رئیس‌جمهور ‎از خدمت به مردم عقب نخواهد نشست
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65197" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65195">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">طبق گزارش The Jerusalem Post، ایران ادعا می‌کند پس از بیرون کشیدن/مرمت تونل‌هایی که در جریان حملات آسیب دیده بودند، آمادگی شلیک موشک‌ها در سطح منطقه را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/news_hut/65195" target="_blank">📅 22:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65191">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
📰
#مهم؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد  @News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/65191" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65190">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEe8PIxcd2l93aVUXEccwWqfCS_5zlEehc3LKkiyv8bCfeX8Mn90X3DwpSML7nQYnaTiwnD_69CEI-no2SU0BzU44J5DVvUHKYjEbC59FqOCYYj318CyUrkz9QXMk0jJFPqyqO4mhJ9hUHYYkq-UoG0dOE3LJuDF50dZSvkVKDr10MaJFQkVRNLSbrPkkFBm0CN8_-pE4TAI7TiJayzA7WUvxI6LYtcXA339ChssWtD-u-0_0zL2tysA-whddfGU3vlvnxgy5aF3jitbyXbuJOeWVGriXXMTCL1fa8_cL-UpI8mVesOpQ74D-b1VgeoQPVPlS_aP14U1rvKBQ-8Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
#مهم
؛ ایران اینترنشنال: پزشکیان از سمت ریاست جمهوری استعفا داد
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65190" target="_blank">📅 21:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65186">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBK_C4UaK1_QwKaXimIVbt4yj_FfYVZs4td9bccR7HwGX5B-MKm8Qe5Uheiw9mMfjA8pFzi276vjYjc67smzlGgOUbydOtbL21rCi7euj7kY5WdRvhiYkjl7ZSEweSXoUmydLkuYyxT2_4qfR23gOYjfA-TCD265iYHQ_4Wd_vZa__PPFVgjvB98wCb1ulTbi6PSlPNP1N6v1oqPug6f9PG5uGzsF0IZiGLkLkbvmNq9K711lMBtFwvVYFCv0XSLv4UGzc-zfa-mwwTHyDmTHX_84vnpJ6AZTdAzUEMcvt6qWun9yG6CLa2sPO7zOxSL4MmJ37bUWCt0QwZL7rFMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6GmXqG67VpMg1LM2GDba12MdLNpydBtEvHVlWcJFUymFlSsCVpWVVsGnmP94HLAO54NGqP3zVKp5ExedrDmGObRxGVkSZRUxp2HpHBrzITn1PYR-vLO-uAhRttvkO-T0BddZBLdjMgg00k2mDJ4tAXngvftsdbODvFhQ2_ob_8vJmJ32sFNEkyC8htSIHUF4E4jqqPlLplMziriwvLsO_jDn9AhMeE51RWASd4NfguxkB9jHiPTaVAc7rT75Lrt4MyCwR0uKnMERBL1701S6JPr05j0ba8T7Ewjy_3P-DF_KYonWub0NOt0vRiN9nfM8DmHBExEfkTJs7fdrn0dAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=qj9Qjbmpgj0_CcmCQB-HBaLOqRNcgY77kFIAzs2QrH42o03C2rsy6g3TMYbZTuj0_XpT-uN4Yt5IqtzzUP7srGxhSBWA9Vt7nsXV4WVBEt1F38GxWQMXtmyGKZU5klgd0XszrCh7yYleB3uXUhoDk4ctOBdsbcNDfwCYaKtIE2N2HfueZVpRcM_mKjHIBmrULNiTbYqapm1WCY-ddZj8PCIaFSoSgnTSs2jhYLbOetTPpjzyg-s_sWKn2uZk9siGfrx8kJe5nBItsrzE5VGx6ZtlelSXGfHUEdjbTyfYHTN-lwPtfgqQLqi3PaVXli10VXBuXJSdfYfF4-JQ01sJHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a589784b7.mp4?token=qj9Qjbmpgj0_CcmCQB-HBaLOqRNcgY77kFIAzs2QrH42o03C2rsy6g3TMYbZTuj0_XpT-uN4Yt5IqtzzUP7srGxhSBWA9Vt7nsXV4WVBEt1F38GxWQMXtmyGKZU5klgd0XszrCh7yYleB3uXUhoDk4ctOBdsbcNDfwCYaKtIE2N2HfueZVpRcM_mKjHIBmrULNiTbYqapm1WCY-ddZj8PCIaFSoSgnTSs2jhYLbOetTPpjzyg-s_sWKn2uZk9siGfrx8kJe5nBItsrzE5VGx6ZtlelSXGfHUEdjbTyfYHTN-lwPtfgqQLqi3PaVXli10VXBuXJSdfYfF4-JQ01sJHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل رسما داره حزب الله رو تو جنوب لبنان به شکل خایه‌فنگ‌طوری با خاک و خون یکی میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/65186" target="_blank">📅 18:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65185">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTgLO3-AAEVgVmWvIuAgSHkY0jl-JD-kV_upLoUG5DPdOiAwftkQWB3FRquAAiQo2whFEkTxd57GrMOVFsAUjqZ61P1S14n17ZAwhhpLaK4GnKd2T7ew1hLykMyIVsYdV81JoFPnyi0rBwJrXAlUswjhjaULGsnbgvIbHmSNhWPdJE8WrUDzk1nrzPAeeMSBwxNljC4nVuPqCF8aQ14HjoMdcJFeLRIws3MiIqi0m5BUTMMmOlSXoDRkf3vDhNizrWUXG52yX9G45QKAbmlmb5OzJ0mNqqyoAA297-B6A9Tctu1D5EJF-QngHR9uNNiqrXaaBS1Iz_KcDuLcbbVP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست قیمت جدید خودرو های مدیران خودرو با ۸۵ تا ۱۰۰ درصد افزایش قیمت
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65185" target="_blank">📅 15:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
گزارش شنیده شدن صدای توافق‌های عمل نکرده در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65184" target="_blank">📅 14:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=pNmBO9Sty5Q2JJMEhsnFKV6ZMarCmYwOt_MZl8QQHQNGw5QJmfnNon_Ln6ENN9kHS5VmUUMgyYunrFYjGAQqXsLy3fPhOx1PzZqx5u6elXkpSIQcimH4g84OMm6ZSqF2JQPbPT6Iu8vVH024Dsw-Jr--TOA5GBpcDD0A0kWYSy8Bs0lhghF8zmE8usWqAQ_cLLEm-4KBYOdvlyha6hEWi4wENbQVbn_rKNlSIXjlXa49stxOshNEtT75RXbQmhU9K-_xa0DodvyCBJFrXk5YZP-vB6aCsQzzsaRyuf0thtcOu_E5kPzrImIHUEJp69zHVwiuKXBHsc_U5ig-qBiQqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec47112ddd.mp4?token=pNmBO9Sty5Q2JJMEhsnFKV6ZMarCmYwOt_MZl8QQHQNGw5QJmfnNon_Ln6ENN9kHS5VmUUMgyYunrFYjGAQqXsLy3fPhOx1PzZqx5u6elXkpSIQcimH4g84OMm6ZSqF2JQPbPT6Iu8vVH024Dsw-Jr--TOA5GBpcDD0A0kWYSy8Bs0lhghF8zmE8usWqAQ_cLLEm-4KBYOdvlyha6hEWi4wENbQVbn_rKNlSIXjlXa49stxOshNEtT75RXbQmhU9K-_xa0DodvyCBJFrXk5YZP-vB6aCsQzzsaRyuf0thtcOu_E5kPzrImIHUEJp69zHVwiuKXBHsc_U5ig-qBiQqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: بزرگ‌ترین سرمایه ایران، «رسانه‌های فیک‌نیوز» هستن که مدام موفقیت‌های آمریکا رو کوچک جلوه میدن
شما یه پیروزی بزرگ توی یه نبرد به دست میارید
ولی اونا میگن شکست خوردید! این واقعاً چیز بدیه برای کشور ما
@News_Hut</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/news_hut/65183" target="_blank">📅 14:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65182">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7-3ELsutOVlvrPQTSgGtud-1KKvIieBEeh_O3JxoJfNLtngmwdhQ2vJQjuTRMbwPs0wag0LD9ufaZf76AOffhu2DdCbznlRxSTQv7Bh85OWhTxq97Jsc3jVWfH8eTPiQnsy2FN_c0VNqZNvjr8CK1K5tlCQ2yv8TZ1uO6L1L1y2dykkhVWqitD7CeazKwH-jGsnLgYVkKk0b7a6vA3p3FtRBW4Xs4s-H4UdRdkEpgAgmTcyWr0_rSsR-UGzVETISUTHUpIcwmVw0q4HLw8M7LKgputQYKt5OS14mcnadHSLgGtq90dSOkfqeP2JTBSYBfB3qby49xQxxYIkYhWcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد خودروهای پلاک مناطق آزاد  تا اطلاع ثانوی تو سراسر کشور مجاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65182" target="_blank">📅 12:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=iUQrRvxypDjMLCiEjt9gwV4UXSOCRnPn2srS6QWc8Zh5b7J_wz-mvSutJc10n4KHjkSpk-7DwgZ2StSkerSDaZwyqGqcwQhaW-XCejSC8VqmbCTg1vtCmCZnPo6Uaaw5kZobZp_Ols8oDPljo-7ccPzlIVQhVbMeLPvssSYO4zARY3mxcSiHOgSww2RFdRdyVQE3qnj3cVWX-kJr5sRlplVEFDqn9Z3YdqhBZfMcYbQ8uD7LRK-0HrFPVLsteCzDnLL4s0546BwGh5cZmo6BKMLzan0dGh0Caku9yaNuCyjj9E7AixcgDVU-s8_Iux0bVang_McAwoPVNRQlQRUSDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/473b1fd669.mp4?token=iUQrRvxypDjMLCiEjt9gwV4UXSOCRnPn2srS6QWc8Zh5b7J_wz-mvSutJc10n4KHjkSpk-7DwgZ2StSkerSDaZwyqGqcwQhaW-XCejSC8VqmbCTg1vtCmCZnPo6Uaaw5kZobZp_Ols8oDPljo-7ccPzlIVQhVbMeLPvssSYO4zARY3mxcSiHOgSww2RFdRdyVQE3qnj3cVWX-kJr5sRlplVEFDqn9Z3YdqhBZfMcYbQ8uD7LRK-0HrFPVLsteCzDnLL4s0546BwGh5cZmo6BKMLzan0dGh0Caku9yaNuCyjj9E7AixcgDVU-s8_Iux0bVang_McAwoPVNRQlQRUSDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ: اگر عجله کنید، توافق خوبی نخواهید بست. اما به آرامی و پیوسته، فکر می‌کنم داریم به آنچه می‌خواهیم می‌رسیم — و اگر به آنچه می‌خواهیم نرسیم، به روش دیگری به آن پایان خواهیم داد
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/65179" target="_blank">📅 11:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65178">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=qe94tLWh1RWE0Yqx3rHwmzufHp3UZajgEcAgJ__U4ViRM3QS2QhEp5jE2cO2o_07-LXfWcRyit8-DuUF02grL2w2BipH7vfhmHy_abgRFKj-38cdhtHVwCBSgusS5Z3ZfbxdMK6VW2t1Hxvg5p0R70RvowWXll0-N4oVZxoowJaOimqUKRs8ENxrHsa-cOSk7sUs1gh7tPlnFxWrcuFaU7IE8GF3wtrAToAON64Wc_1iKP6tgkMenxpZtJsQCHA32VuRFLSCKNAsewwSEeP-GgbBLG-U2Igf47y-PpV7Q85SU5wHHNRy4JgHEkeKbqEYjKCmoSIPmgvnBl7drUhr0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4173e3828.mp4?token=qe94tLWh1RWE0Yqx3rHwmzufHp3UZajgEcAgJ__U4ViRM3QS2QhEp5jE2cO2o_07-LXfWcRyit8-DuUF02grL2w2BipH7vfhmHy_abgRFKj-38cdhtHVwCBSgusS5Z3ZfbxdMK6VW2t1Hxvg5p0R70RvowWXll0-N4oVZxoowJaOimqUKRs8ENxrHsa-cOSk7sUs1gh7tPlnFxWrcuFaU7IE8GF3wtrAToAON64Wc_1iKP6tgkMenxpZtJsQCHA32VuRFLSCKNAsewwSEeP-GgbBLG-U2Igf47y-PpV7Q85SU5wHHNRy4JgHEkeKbqEYjKCmoSIPmgvnBl7drUhr0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسین علایی: ۳ روز قبل‌ از جنگ رمضان‌ به آقای شمخانی گفتم آمریکا و اسرائیل با ترور رهبری جنگ را آغاز می‌کنند، آقای شمخانی گفت «نمی‌توانند، پيدايش نخواهند کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65178" target="_blank">📅 09:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=iIqTTQMRLGNmXNQ8PaIhoa9S4RXtlFCEfzeiF03rSu4kdjbLd8x5G0ZtaMTNOhIdqu1QYC8K38WYQzfiEap2lUD6aYRu4WrwazqhfGjdrmEQSq1uzWyuAekwzkd8ZdBGnGYfVKWHVwPDad4brHDrvqgUr1em7QuoQ3PjFvXfzRG_y45IiEbWt9ZJuTHOfc4CxnvYt-UxzmNovPFCBuYn_KwawprD40RiLphqGQ9OJS0dpQfadMFAGrG4IwTjwXdGPTaCXfj1KgGHhXifUmGzgsGcpHrKShw5Bf1fCddyPV-qYlsDLwUE7zr1CJUUVb_N72ytj_ool6S0QVQiDqwsSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9b4e22f8.mp4?token=iIqTTQMRLGNmXNQ8PaIhoa9S4RXtlFCEfzeiF03rSu4kdjbLd8x5G0ZtaMTNOhIdqu1QYC8K38WYQzfiEap2lUD6aYRu4WrwazqhfGjdrmEQSq1uzWyuAekwzkd8ZdBGnGYfVKWHVwPDad4brHDrvqgUr1em7QuoQ3PjFvXfzRG_y45IiEbWt9ZJuTHOfc4CxnvYt-UxzmNovPFCBuYn_KwawprD40RiLphqGQ9OJS0dpQfadMFAGrG4IwTjwXdGPTaCXfj1KgGHhXifUmGzgsGcpHrKShw5Bf1fCddyPV-qYlsDLwUE7zr1CJUUVb_N72ytj_ool6S0QVQiDqwsSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تجمعات شبانه حکومتی‌ها، دیشب سپاه یه قایق تندرو آورد وسط میدون و از نسل جدید قایق تندرو که ساختن رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65177" target="_blank">📅 08:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65173">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZxhyptQmoZUvGic3bCc_YNSp3JCtSRq1ZcO3HzOnsibzNgZPbihQ_03Pg_nKAfimt3P3CTsHk5yrNhrAXnt-eIIpXfAWm0n_6WxpoLOPkTx0114arKgXzS-s4IPsOfFcKUf5Qtl-oHQVMw55-DoRwOGuLFtYN7nRl7EzEdsScyVK4t2BTjDEBhC3uBmwbTyXEvRql95YPKiHhzn0C6q4n2haovYAWfQ1LdzvnrBmwavD0mNW_7CB6giOMQPRq_e04aOrVGEqkaPr2nODEtP401zKsuLutFiofBHUTaMpdMhkpheTiIchobAT-o5AJ6WAx3WrlQge2s8DLck0XLJb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M7qTOvgGQretcDp-A8uDhGj34B-4h7xP4DW4SJTiMZ3HGySVjz2V-KCMy_q0x4-MQPUWURdiKuaVjrYoTJYtR5YH6m0MaFMTHSEENRVXwAhXsKDM-IjhEbu4wkDyBLXAcMDg7AFv2msUKKLGJIyyHqrqywC9IAOlNRzf0F3DeySmeZDy_26cYR1GX5cEUxqCIxfymmqx8n2IazwS3SCXsVN70u9-PtVUGxvQ3zKWUx8mLgAltLaYiR1JSsgmXyO2MLgd9p-HR_RDVqINxsy9dRMMuVT6v8vDaJTGCarDPDvbmTTOJtlZ3vsnfQgOWQ8rPUw-lDKj3dHZoYdrlz7Ijg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های رندوم ترامپ دلقک تو تروث سوشال!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65173" target="_blank">📅 00:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65172">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=hpwpIz4WUvFoDlpOo1BvrvvDeNrpDXqDiNhQTPUZVv35jIprX5VBWe0srf9WP491YbkeAabx4oZx-kiRARnkpI_msH7CjMMunaR4MJI6syWcussd_XC_jQTnyYjTFDqwFKO3f7aNgE3GvZv6dVdAS8cmSHj1ccbDFZCKjfr6g0NyI-rC3wcFN8oYkUbyyiLHX2ul6vJVKzMFfBa93vfKmPYYuXodRRlCAsaSJtIlU297BNlVq4c1DtQGfI06Iqs85WJr5IqG1alGYQXULKu9lAkA2bzfy2uKaStePyqNtdW7cDZmvyU1kLiP_vmZSDdrdeSCDFd4ITTfic9cIfSWnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2f73449d.mp4?token=hpwpIz4WUvFoDlpOo1BvrvvDeNrpDXqDiNhQTPUZVv35jIprX5VBWe0srf9WP491YbkeAabx4oZx-kiRARnkpI_msH7CjMMunaR4MJI6syWcussd_XC_jQTnyYjTFDqwFKO3f7aNgE3GvZv6dVdAS8cmSHj1ccbDFZCKjfr6g0NyI-rC3wcFN8oYkUbyyiLHX2ul6vJVKzMFfBa93vfKmPYYuXodRRlCAsaSJtIlU297BNlVq4c1DtQGfI06Iqs85WJr5IqG1alGYQXULKu9lAkA2bzfy2uKaStePyqNtdW7cDZmvyU1kLiP_vmZSDdrdeSCDFd4ITTfic9cIfSWnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عده تو عید قربان خاتمی، روحانی و ظریف رو بنر کنار ترامپ و نتانیاهو چاپ کردن دارن بهشون بعنوان شیطان سنگ میزنن:)))
خوب این ۳ نفر همینجا تو کشورن برین خودشون بزنین
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65172" target="_blank">📅 23:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65170">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=pA2ZMDeGnwG0KlY8-Mt0j3Kgsibh7LlXpuYJm7ZqeKKEW7OiK_Dl0wUzmpjdX-sfnP3LLyR2nHH-fq2wUdZ1dseJZ4HYK2aFwQSLslm6eQ6Ht2ObHNM2D9D_9nRcXKQd5XQn0aUh7Ousnueb5JgZUjJTC3E6hlMFFDV9WtXpb3qwjEIcZac2kCazpre6y2Be1aWU09lQtBM_dD7HmeorHgIZSrQF8m2sGBUF4NG0pOVLrgxGN4NupB5HuQTdkSV292pwNYcXu3EabsaqjjHCv8DD5YL2ES4ySCELeE6wOCH-Hd2aznEEgWVrT10eiQq03KbnAxfjJ_0PHukT3jh0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dd6247ddb.mp4?token=pA2ZMDeGnwG0KlY8-Mt0j3Kgsibh7LlXpuYJm7ZqeKKEW7OiK_Dl0wUzmpjdX-sfnP3LLyR2nHH-fq2wUdZ1dseJZ4HYK2aFwQSLslm6eQ6Ht2ObHNM2D9D_9nRcXKQd5XQn0aUh7Ousnueb5JgZUjJTC3E6hlMFFDV9WtXpb3qwjEIcZac2kCazpre6y2Be1aWU09lQtBM_dD7HmeorHgIZSrQF8m2sGBUF4NG0pOVLrgxGN4NupB5HuQTdkSV292pwNYcXu3EabsaqjjHCv8DD5YL2ES4ySCELeE6wOCH-Hd2aznEEgWVrT10eiQq03KbnAxfjJ_0PHukT3jh0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه‌ای که معاون رئیس جمهور آرژانتین نزدیک بود ترور شود، اما اسلحه در چند سانتی متر جلوی صورتش گیر کرد و زنده ماند...
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65170" target="_blank">📅 23:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65169">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نماینده زاهدان: برخی مناطق شهر ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند
🔻
بحران کم‌آبی در سیستان‌ و بلوچستان وارد مرحله نگران‌کننده‌ای شده و به گفته نماینده زاهدان در مجلس، برخی مناطق این شهر بین ۲۴ تا ۴۸ ساعت با قطعی آب روبه‌رو هستند و زاهدان هزار لیتر در ثانیه کمبود آب دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/65169" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65166">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۲ اسرائل: نتانیاهو به زودی جلسه‌ای برای ارزیابی اوضاع در شمال با حضور وزیر دفاع، رئیس ستاد کل و روسای سرویس‌های امنیتی برگزار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65166" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65165">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شاهزاده رضا پهلوی در اودسا: دنیای آزاد هنوز ماهیت جمهوری اسلامی را درک نکرده است
🔻
شاهزاده رضا پهلوی روز شنبه ۳۰ می در نشست «امنیت دریای سیاه» در اودسا، در جنوب اوکراین، با انتقاد از جمهوری اسلامی و سیاست‌های غرب در قبال تهران، گفت که «دنیای آزاد هنوز متوجه ماهیت واقعی جمهوری اسلامی نشده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/65165" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4qan4Ylg8w8G9ThNJeAq9_yRSI_rOJa8BCTNw7HxmHd7-Zl7H7hf0eI1XKzAXr-vOzJoedyJn_Jjhx4H-QVH7sa1hzDX3WMJDxz2UWsCOYXag6C9L8gvQUQk7hYoQAvBqwv_q_QCe9PJ0osMVD3pGOWHYdnvoFiCXa6drxJdfD9tw8mqnCbc62WdjB1zpDpk87qQSwQ7esNetfTBw9REKo_rOfSpOKeljCEmfqEfazh8tfTTv4Yw8w-GOcBCokMtR_nTI2sEcaVDm6lFVYHvr8EnZXw14rvvZnEauryhlLC3CSTwQM7WO2Ddo21NeOwgYZc6iGsdaZ2X4wSDOs9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته‌ای که تو تجمعات شبانه دیده شده؛
والله هزینه مذاکره بیشتر از مبارزه است
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65163" target="_blank">📅 18:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
پیت هگست: وزیر جنگ امریکا: محاصره دریایی همچنان پابرجاست و به‌صورت دقیق انجام خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65162" target="_blank">📅 18:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLPQD1vnyeonc3ULg-9jPBTMfD1E2XJw42XdlN1W8jN4RGIWGMNcrXA9Zyuv1cwo3Xr9laSjKj7ajPRhbs-eoOnw-GK17xJa3rb6vcmxc49Tpb0tXzS-pTHkLuNg0AYZ2n6foDYLwf8ln1MQlF6A_I7CNQ9P2vm3HDCenzw35RkM1BaCOObwXCPIvfSk43UZyVMXODtg1Uz0EnFA7lJwwt1TKcmcCp600Ye0sDxp5tmPkecDMCcUMVJu0ngSQNBrHI2nTheJVpH23I5ftP5N5TDdkWGJjRVkwtvtX4-4z3XGDsVrvq0yaW31nzqK9ROFjVQyZ1IEOV_FjQgFR17T0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی: من فهمیدم ترامپ برای بار سوم در حال خیانت به دیپلماسیه.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/65161" target="_blank">📅 13:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65158">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cal_F9buXZcGufCzszQLqCVqSJfsPkCdKvy3MUJdJIRf8lEr2RG7_mGimSiKAP5W6LdLUruVG5WltciRAELodCwTGnJFOpQMQAX6m3OOzGVU7uwbW-VeAr8lCHOoQ-08sUKa0rWUSwexQ6zkFHXKUk65XwXddIqVGvfdQgPVRaEToMEYk6ld2FgSM4MPi-KzJEdtzymJlsCdl__4t_Fdko1pO9L_7gHfWN3nLUbTWWlD9thAZ4pjKyhxoPwZJ2UtDXYTohLNDdvD7cEVgmqoFpc7IhjlO-zGeYsSUCMorg1sqf1kg8Jc8eEl98KIw1BwEzeZFPOKhSnvyScJK60liw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاخ سفید آخرین معاینه پزشکی ترامپ رو منتشر کرد؛ ترامپ ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار داره، و قلب‌ش۱۴ سال از سن‌ش جوون تره
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65158" target="_blank">📅 13:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65157">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
سازمان سنجش: کنکور ۲۹ و ۳۰ مرداد ماه برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65157" target="_blank">📅 11:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65155">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nq5OzHd1PostkCm2k7fLQgU-hT-ASk0yQpiwfAZvGLPzFZK9me28vhXgjC7aj_PITOlz8sKUqxh0c3Ke0gpsFIbRfIdOZHjfocxQ8J31HPnIU0U0rDdVBaDcvk9IclhOMcOJ3RokJUB2y3jMaGyqYm9u9qq6nvxFYAQ8m_BXOoxyLxVTB-jKd-B30AwJY2UpluIEi1hbKLai0EIbVreyWACCWN0BC4gmWhPY_WmKV24luFCwUnCPLUzTwiHdYg5ieGPAAcd2LS4hRlSTpukjfPPwfcrf3B2INU938_eoYGoSCV9sbm9e6ndA_kOQ80LGo54opPAdlXRYRIWIC_NkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CM5A0KIAQ-JpViQo1n55iaNxDWln12wfXJ57S8LAiT3V_N7UHKc31W5eliHjADvpCydjjwn0aZu_Nus-tHj-gZVpCzqr2GRLmMC2adAz7Zan56ZaprVDvGO5-J_hjZVzxf8-jsFdQDZq4xcADw9HqRTdJVfcm2trqEuIfUyT16CO_zP6iGAP6p6-WsOUk7OBFcHxrrqir49MZXOPyDPPEengpvVBUhjUzofpFTrQAzC0XTbQY1phBY0-nYyTQwhhtIp_xVOYQy10fxO_ECLbTRUVLnU1KALIdSrV-aM2ubceOSdfX-DJBkQcjEk9k5YA6iqCBGjZGpWT7UwyNzguiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ملت اینجوری دارن قربون صدقه‌ پزشکیان میرن چون حق مسلم مردم رو ازش گرفتن و نصف نیمه بهشون برگردوندن!!
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65155" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65154">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qke95xr-kfC_0V9MCIskRV5eFln17_ox4vDkUZYxR3VuY4VICgPmkPXDfERfLKyOrOwtBMFbMkxgC8j4vaWXqBi52lpKEtxOn0HEYx6JfW2p8CKXbjWR9kaghSlm3-GlqEhPVx2vBup7NXpSkKckpFzvVXn_OikP0S0rMIUttf6fIEJ39nwkbvEE4v5HPxn2YnNrCkAo86o5v12APH8XX_bV1tmoNiLradgPTVRrVeooaSz6Rup8jrwgi2omlmLJhIEXG-d58mIx2YEAU_A1znbesQxgfXTjqSRW37iP-1BqM2DT0lGykswrLzL5rpNUGNMIL0q6Dm4XJx-PZLdyDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از عروسی‌ها و صیغه‌های نمادین تو تجماعت شبانه حکومتیا یه پسر ۱۷ ساله با یه دختر ۱۶ ساله تو تجمعات عروسی کردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65154" target="_blank">📅 08:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65151">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=ixM5UtV_mfVgU6HI0hgsOd9Z84XrjXuxeyCJVD0xy8PqSRaIzzWN94guaysc-2gvx3Jiti2DYkKbWm886f8DQyrnbFAnENnz8uZwGcK2BQ3h963HRSOFkUNXc7FgzVt--JytVV_lqCofQWl_nPJ-S2jfpytm2vJWrJVOvNV1HCeq2_Z1Ol4UmbVqYY6GBjxI6XkTyFiXKjrO35Zs7HpnrWbul69H117nODBtX11iwhaqwopHplr9pxumkntFHK3fuWWnUBy_vf-ctHuEkM9eEWx8vCYHh3NeTBFsbcqwqXawURjojIr-WKwcfhyPlil37NLxq9fgicjjpnjvQx2ZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38baf3c3a.mp4?token=ixM5UtV_mfVgU6HI0hgsOd9Z84XrjXuxeyCJVD0xy8PqSRaIzzWN94guaysc-2gvx3Jiti2DYkKbWm886f8DQyrnbFAnENnz8uZwGcK2BQ3h963HRSOFkUNXc7FgzVt--JytVV_lqCofQWl_nPJ-S2jfpytm2vJWrJVOvNV1HCeq2_Z1Ol4UmbVqYY6GBjxI6XkTyFiXKjrO35Zs7HpnrWbul69H117nODBtX11iwhaqwopHplr9pxumkntFHK3fuWWnUBy_vf-ctHuEkM9eEWx8vCYHh3NeTBFsbcqwqXawURjojIr-WKwcfhyPlil37NLxq9fgicjjpnjvQx2ZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اسکات بسنت، وزیر خزانه‌داری امریکا:
ما حدود ۱ میلیارد دلار از ارزهای دیجیتال ایران را توقیف کرده‌ایم — کیف‌پول‌ها را به‌طور کامل گرفته‌ایم.
برخی از دارندگان ممکن است همین الان در حال تایپ باشند و ندانند که کیف‌پول‌شان گرفته شده است.
این پولی است که از مردم ایران دزدیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/65151" target="_blank">📅 00:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65150">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3SuOs_qfdtwYAt9P8HnjZua6h62WDDXs52wUEZNWFqsl6cpvYLWVooCjUUs1tEcj0KF2zB7ipW7HZQ0_G6NyJ2Ebk1tpibmSn2XlCuQe7k8u_fEpUczbrKUTktwR4GhahhzLKOykjMDgJY-GA0vZKHwduTKe-IGFhe6nfpApt4mHMqzT2onbWGU39ld_Qz2rRg6PXcsr2Fw5tdMhelV5dLbYbcN78GYynG2hDNlvGVlKaqB8sEfoRaQts0weKXUlGjciRyWmL2gcj90a38HWr7b2X5-VI4sW03Xc-tsU1H7peQGW6--exweK_0ETn9PmTEgNq5sxXw7l0vd_efp0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحویل بگیر آقای املاکی!!
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس:
ترامپ باید بدونه که ایران به عنوان پیروز میدون شرایطو تعیین می‌کنه
نقد مقابل نقد، نسیه مقابل نسیه، هیچ مقابل هیچ
البته برای موضوعاتی که مورد مذاکرست نه آرزوهاش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65150" target="_blank">📅 23:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65149">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnLeJXwfpJFPTR0IYC5Sj9gwtf-_Mr8QW1AtGbeYmHY7ukL58LO1oTbFKtx4TMBY1Y8MdHglL6iqBuO5ZrCbFLRtsZtPs2D7nC5KJO2jznIrxgH3z1FmeLs8h_NPwYqCc3Pgvge3prk3sx0nR5NYmF9A0n8TchcrdnGqCfXwH224nNhCR8cTRn0aGI7aeHFwsv8dUzr4uCHXeO_-IyfuRHCPO6EAFh59Gic4XXqvTIIZ0YYg2psII-N6RZg-yiKj66vUzjuG5QXBkSlaJbYKGP38_JP6HdRPLzyEO0YG0FVseUNCfsZwF86qU7RwMr2Bc1V_GVGdasSI1faTfnoPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمودی، رییس شورای هماهنگی تبلیغات اسلامی تهران: ستاد آماده‌ی تشییع جنازه‌ی علی خامنه‌ای هست و میخوایم با جمعیت میلیونی برگزارش کنیم ولی زمان‌ش هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65149" target="_blank">📅 21:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65147">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
گزارش فعالیت پدافند قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65147" target="_blank">📅 21:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65146">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
بقائی، سخنگوی وزارت خارجه: در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد جزئیات برنامه هسته‌ای مذاکره‌ای نداریم؛ مدیریت تنگه هرمز باید بین ایران و عمان تعیین شه
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65146" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خبرگزاری فارس به تازگی اعلام کرده ترامپ مفاد توافق ایران را تحریف می‌کند.
او ادعا کرد که ایران موافقت کرده تنگه هرمز را به صورت رایگان باز کند و مواد هسته‌ای خود را از بین ببرد هیچ‌کدام در متن اصلی وجود ندارد.
ایالات متحده باید فوراً ۱۲ میلیارد دلار از دارایی‌های مسدود شده ایران را قبل از ادامه مذاکرات آزاد کند و آتش‌بس کامل در لبنان (طبق شرایط حزب‌الله) نیز الزامی است.
این توافق هنوز در انتظار تأیید نهایی در ایران است. منابع آگاه اظهارات ترامپ را ترکیبی از حقیقت و دروغ توصیف می‌کنند تلاشی برای ادعای پیروزی زودهنگام.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65145" target="_blank">📅 20:42 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65142">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE0oTu7NrWyWnl99bV58UcQJwrrHx8I9tHX1WcLefo26JPrTBkN4mg7hXnAPXnuxMmD0XVc7oNCdjcz6CC4dfoOWXLAjECEjjNYiJZ6TAizore5KGEOgRXXZ2wn6aoyYfagzz2nexxc2mScZP1d7qk5q0b3Avd89vkqN7cgNk0e61Q6xD797m0Q51h9MHOv_oYzNWfpCW21xfH0vK1j-z3osOeWnud03zGsjpVfZA9zAWxHno6qhK-ft5ZqE6iU5Jq8guWbAT1hKvQhXLmNO8rsOjJEeLz9wjYSfE-gPj76xabJeIY2AtDhHw6atN21N5A1IgWaguag8cFw2vYGdhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
۱- امتیاز رو پای میز مذاکره نمی‌گیریم؛ با موشک می‌گیریم، مذاکره فقط برای اینه که طرف مقابل بفهمه قضیه چیه
-۲ به قول و قرار و تضمین کسی اعتماد نداریم؛ فقط عملکرد مهمه. تا طرف مقابل کاری نکنه، ما هم قدمی برنمی‌داریم
-۳ برنده واقعی هر توافق کسیه که از فرداش خودش رو برای جنگ احتمالی آماده‌تر کرده باشه
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/65142" target="_blank">📅 18:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65141">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65141" target="_blank">📅 18:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65140">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuJH2gsNpFLZyhQeMl3PKCIVSNci4MCd223JpeJ4LwJRyNDwxBi_7QOlpZ8kxz-_s0efwsFR0-7OZcdEQRj0DlYa0tu-yhlO4k58TEYdu2B_O-x-pXpYj07z1YZzNass9xMZvG3QMDTDXxkClr1UPfQJSlKCN_B8tzdHaaaNMJNZgScZq4qKbuoHjtYOwVbDn2MBJD-E7TNwvZaAPhEHARArkrSDOh_HVhxztl-NIrcXZ8I2kMxAuktHtvkru_cv4Kmx-u4WpQnm-_qUzSFVGguVjSxO2-aVGy83C2JdbhzfoRSULdNZ4LfVaEFKR7lmUoRygL1-oqtfvqwyY3Fo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز روز جهانی مشاورین املاکه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65140" target="_blank">📅 17:53 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65137">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/maUKChpQb1ikyyzrbiCRm2E3G0FaMKjhB_6e-ppbRjTkks2Z35aa7WEdTLqVnkIFB6fZZfzikD6bQI6ZvilsQ0YniKIMA13aLjbE7_ibRuvVPwSpiX2iKAmNbZNZTaXAZ9Icu5C0Ypqi-jnCkPSm7n5hw3Ojs_8AvKND2TYahOZUCsnF8tUOl0NqdlMid_mrCNsn1jUtcnUf--sQ1xnFJekcmOSsbWQf0-NejQNHNok7JhBY8aMh-sYKd21ZKp85qpSPDdaPLa2Foib6q0KvVm6kaUsdbjBM00UKtB7pblfX0CJCfZwz3iPv4mQZbWBKlBSXwI3KrJYAMj1ozNvffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی شما نت نداشتین این دوتا شده بودن سمبل شرافت و نجابت حکومتی‌ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/65137" target="_blank">📅 14:12 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65136">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdyLq8aa1kz9g1XXbyYBb3W22idUz7g2EAZxnaW_ZLBPl-OyIvb53LQNl2t5IUxQdvkK8yhamjBz_YJXkNZZfBezVpg2VREmqqSTYb3chS8Fx9IgMcDPpkxfMtbvy2_6m6NFg8EORsOSc2OJ6f7FhyaodlDethTDLhsOPpn5FEVMJ-XjQxwRuX4Ph9oThJlghAgBNAnwczvG_BgrXskAk7dQmTi0psG31eLHN1cB6getwOHRtmrniyTHKd78SgHLErHw4koPPHZ95BtgmaEmAG-BmGTEgFSoLi_BUy-6YSeWk6prKprksSgh-vQger4tR5Z6fV4f63Y2xRXezN797Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های حمید رسایی تو کانالش درباره چه کسی شایسته جایگاه رهبری است با آیه‌یی از نوح و پسرش که حتی صدای خود طرفداران حکومت رو هم درآورده
خیلی‌ها میگن مجتبی رو به پسر نوح تشبیه کرده
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/65136" target="_blank">📅 13:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65135">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=E9iuBNN3v4l6r6YejeLnhw9hdiQJBs7Jk1tmHMUhGZHPr7r0WnffoYe36_JYPbfVJxqECDEFNUKGS0FX0WD3kld-G1ijYGh2yVYoOpj0oeMrEgWPRLTX8UwMrJ1HP-nWHWD8WNP9GTNa31OoDkfq4nkKlDq-BOtjOB2RT4dIx2Kyww7XhVa1mMPYQ0XEaLRqb3G5tbJnTGmRb0QeXIIcALm4XvaX9itUE8VLqUTmQeXy2dg8VPMBypkjfKGipDHoQjop-C-QKJFzJSbKFhvHYI54xEze4XSkUbqTHZWLQTrwbRbxK_wUJVkgbytmRmXjzHNobny2aEasTv69Ll6sQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6374d1.mp4?token=E9iuBNN3v4l6r6YejeLnhw9hdiQJBs7Jk1tmHMUhGZHPr7r0WnffoYe36_JYPbfVJxqECDEFNUKGS0FX0WD3kld-G1ijYGh2yVYoOpj0oeMrEgWPRLTX8UwMrJ1HP-nWHWD8WNP9GTNa31OoDkfq4nkKlDq-BOtjOB2RT4dIx2Kyww7XhVa1mMPYQ0XEaLRqb3G5tbJnTGmRb0QeXIIcALm4XvaX9itUE8VLqUTmQeXy2dg8VPMBypkjfKGipDHoQjop-C-QKJFzJSbKFhvHYI54xEze4XSkUbqTHZWLQTrwbRbxK_wUJVkgbytmRmXjzHNobny2aEasTv69Ll6sQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماهواره فضایی شرکت آمازون دیشب حین پرتاب به این شکل پشم‌ریزون منفجر شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65135" target="_blank">📅 12:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65132">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_j3jcgdGL61OfowPhMi9oalGOys-ryvrRtv3_hqkXwhyCxDivMK4xXZZA1JE8q4JAELcmDLQVX7VzOVetLNeszM0fFlOSjhpP2p4CVq3DRysVip2W89eoqnw4BGp4w8zJx2rI6qFOviXnq_F43287wG-WnbIRN84temdEFqMdVrasa-27wDRLJTXrOxzJzdpJW2NzIa2NAQ_wEjC8Yh9Dk_1PE3ufCgWHfB8WMiapo1uzlqW16n8uLGbayjGivZW8lYmHjiB798Gxor_ZV0SUCyhAimJ_bQQg9poMJ5Z3NqdwrOaumz86h2fhyGlmvDYXzoBBxqgdlaSXzD8SYeAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
واشنگتن پست: دولت ترامپ داره به اداره چاپ اسکناس فشار میاره تا ۲۵۰ دلاری با عکس ترامپ چاپ کنه
قبلا ترامپ ۱۰۰ دلاری های با امضا خودش تونست به چاپ برسونه و اولین فرد درحال درحال خدمتی بود که این اتفاق براش افتاد
همچنین طبق قوانین امریکا عکس افراد مرده میتونه فقط رو اسکناس چاپ بشه و از سال ۱۸۶۶ که این اتفاق بی سابقه‌ست
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65132" target="_blank">📅 10:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65131">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=fzI_eJRZJbH8qf74Y0O_9R-Wzry3FSosKPbBsPAZe4jnKBBk0ixPJzFP3KTAvwkIvBjVsb8zQgG2bFGO4rKekpiOMvTMiwYv0l6j7q-c4CQ-eVZ7s3CuHIDtUmVrdCw8TMNy1px2xwR7h93p61Xbhto_4-ScHszypF8U5eHbcIlFP0rUdRH539Lc_RLgOqepFzUDTyGGdU9oKahl3FSGdAwSryIsiE_T2MFKajf5dDwCCTRvT17ZNbASM85gmNnLErseWyzU78Bk-XCxEoNB2B21TiD0K-16P0KjYQEsXe49qDZXDBxyh-EDyovrudzKXf2-omr7smHPumY52DXj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d098f5f90.mp4?token=fzI_eJRZJbH8qf74Y0O_9R-Wzry3FSosKPbBsPAZe4jnKBBk0ixPJzFP3KTAvwkIvBjVsb8zQgG2bFGO4rKekpiOMvTMiwYv0l6j7q-c4CQ-eVZ7s3CuHIDtUmVrdCw8TMNy1px2xwR7h93p61Xbhto_4-ScHszypF8U5eHbcIlFP0rUdRH539Lc_RLgOqepFzUDTyGGdU9oKahl3FSGdAwSryIsiE_T2MFKajf5dDwCCTRvT17ZNbASM85gmNnLErseWyzU78Bk-XCxEoNB2B21TiD0K-16P0KjYQEsXe49qDZXDBxyh-EDyovrudzKXf2-omr7smHPumY52DXj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: کشور‌های عربی مثل امارات و بحرین و مراکش برای تاسیس دولت فلسطین به پیمان ابراهیم نپیوستن بلکه چون اسرائیل رو یک متحد قدرتمند علیه ایران می‌دیدن به این توافق روی آوردن
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/65131" target="_blank">📅 09:54 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65130">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxU1JQnp58IXRKJUnZTF4QRJmmBgfl2_eGcir17wZxVgZBZQGOHxLcb2c_olQno8Tm2uoCpioXHsTE0kT9ctnKybY6sZSt4mw0KQEkHKLoi1w-fUtU5tQOCqtK3FDfBOFe-nV2AZEvqH35I13kEAmCaCWrEQv3nIFeyX9PAJrEEikrqEj11B_pNjlqvP7w4CTFANtqw83bYau4yYmtMvLMunmUltQ0y5KFByiCSCEAcjTvB-mRlWtHLexcZyRj7yHuAJrts0vZfaNmeelCPZtUOc0AI6TFxEW2NfYjylNAZ8WqlLdQTesU2ZSe0AChqaWUii6Le_2nNq4jEnvFPFhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش دفاعی اسرائیل: از زمان عملیات غرش شیران تقریبا ۲۵۰۰ عضو و فرمانده حزب الله و ۸۰۰ نفر از اعضا رو از زمان شروع آتش‌بس حذف کردیم‌.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/65130" target="_blank">📅 08:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65127">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
گزارش صدای انفجار و همچنین پرتاب موشک از شهر جم استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65127" target="_blank">📅 23:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65126">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011753724a.mp4?token=lZKDhNNn97dAVOLP17v1EgLJ3YOxE4hMXFfGKpijiXn2xUJZ_Y1TbplpvHxcuubXO-XAfFvuZh1NXNg-_238DJocCn3aG0YhZZHGCXSFQlqEsZHyUnWzpuhSEH-dHC7uObjh0tMPH9ikJtVa3mL8VO0vQ_3R-vZ6H0SMsvauxhEMba86gcoDhrfDstspV-4UHzRabRCY-YN9Uv75qmmariynntp3mnyffhyLoafdHLJ1DFpL-0M2q7s20UC1eLpmdTt1t5oshSOIdN48z8kJyfR4imk6lIjEwXKCmOvN1wxVO1w8N699hDlbLVzwSfty21J4D8dyVnEIZsRXPus5Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011753724a.mp4?token=lZKDhNNn97dAVOLP17v1EgLJ3YOxE4hMXFfGKpijiXn2xUJZ_Y1TbplpvHxcuubXO-XAfFvuZh1NXNg-_238DJocCn3aG0YhZZHGCXSFQlqEsZHyUnWzpuhSEH-dHC7uObjh0tMPH9ikJtVa3mL8VO0vQ_3R-vZ6H0SMsvauxhEMba86gcoDhrfDstspV-4UHzRabRCY-YN9Uv75qmmariynntp3mnyffhyLoafdHLJ1DFpL-0M2q7s20UC1eLpmdTt1t5oshSOIdN48z8kJyfR4imk6lIjEwXKCmOvN1wxVO1w8N699hDlbLVzwSfty21J4D8dyVnEIZsRXPus5Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا کاهش تحریم‌ها برای ایران روی میز است؟
اسکات بسنت: هیچ گزینه‌ای روی میز نخواهد بود تا زمانی که تنگه هرمز باز شود و ایرانی‌ها موافقت کنند که باید اورانیوم غنی‌شده با درصد بالا را تحویل دهند و نمی‌توانند برنامه هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/65126" target="_blank">📅 23:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65124">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇺🇸
#رسمی
؛ توافق موقت ۶۰ روزه‌ی ایران و آمریکا نهایی شد و متن توافق، فقط منتظر تایید ترامپ است، هرلحظه ممکن است خبر اعلام شود
@News_Hut</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/news_hut/65124" target="_blank">📅 22:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65121">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=KRoOEc7k27-JLcEQ8wDSMFIRJMhwTjtjuMtLy4ppDAsJn9-r6Y0HNmn24QQsBFcPxN6fuqp1OEyMETthcKrg-bP90YZU54Ym7fiFpKRs8GGqLpL9632vs_jMX8NsrT1TQgO7aIRUbYRTUH6k86YDExUw_PPAIGjrZxztZH4U-1nVHSKjkRWrx6D93VlOLNWNRI1tfLb2-ttyG_9Ug-ED_MZk1SUopRw2J2RGE3vCP-YUtlIhH2ThS3RzSu0Ldu3r2BfjMe2S77sH9HxNQZ_FYKlrpzCwHJ9Ta64B0VxcCbFtrOh_kmJ-terGZh5m_xqOoCde1Yk9b5rC5joZZr7NnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fbdc689a0.mp4?token=KRoOEc7k27-JLcEQ8wDSMFIRJMhwTjtjuMtLy4ppDAsJn9-r6Y0HNmn24QQsBFcPxN6fuqp1OEyMETthcKrg-bP90YZU54Ym7fiFpKRs8GGqLpL9632vs_jMX8NsrT1TQgO7aIRUbYRTUH6k86YDExUw_PPAIGjrZxztZH4U-1nVHSKjkRWrx6D93VlOLNWNRI1tfLb2-ttyG_9Ug-ED_MZk1SUopRw2J2RGE3vCP-YUtlIhH2ThS3RzSu0Ldu3r2BfjMe2S77sH9HxNQZ_FYKlrpzCwHJ9Ta64B0VxcCbFtrOh_kmJ-terGZh5m_xqOoCde1Yk9b5rC5joZZr7NnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالی که جمهوری اسلامی اصرار داره یکی از بندهای توافق آتش‌بس تو لبنان باشه  نتانیاهو و اسرائیل در روزهای اخیر بشدت حملات رو علیه حزب‌الله افزایش دادن
@News_Hut</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/news_hut/65121" target="_blank">📅 22:08 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYD3y-ff5a5nPZcUpjchmkTcW85Td45oWQ_XHwVCEjvt75RvKA_rv8H1OyuCB0QDKpxUEsNF4HHUxBk7TYacUxam5y3AhsFYrVbtmjfJJSSuX6gZIWqqPa-6-bkf-msUI_9nJdRIYoaaNHvrjmXwZeN_-kNjcnpsr4L5qClu4o4eZ3qjjJMYStqmeakRPl-EwNqa8VfES4pXCwNZ_86R1_SezjdgkOpXr6vhL-jGoyULJaYBGKjlCraDyAXqgdjJkLldSVGhMkdlh1W2efrO1aMDaM3lSO5DNaCV2RSu7bWrLhyydpv0dK85pHe6Ynkv6W3Ga1V43QGWq9vpZueZRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZyuxADIZ3t-WKY6rBfoSkQPS5idZU1oOm0p-5aG3M5N15ldi6y_NnGnKg9rl0n63Cwuvva8r8fsZL7w7PZmmZxVQd6H0bvMb66_pALXcX22seRezQOB6QUSThfHwTDIpBfW6G4z8RjrelarmB7tsFpsm3gUo9o9z02tE8UAcw4zUw8vkUr0b2r9djRGiKmk7DrdhLkdKrPMQ63taMDaSMgyKVjFs1fTgAEhg4Qmvff_Ag0PqxQ_7mOmu9F1z0rHGX69am25Pxf0GNPUe5cpTfCv8vhI-Szuagd1qToxl4Rd-Zuo1kCOEP5eVMitLMDJndyI2TqIkCNXt9ysK_O2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M342MCgaEsbG_ZNL8PxZCw1lqQKm_-TL-SCQEUymRoC2Cs8k92DpzfOHTi_KVipkJDjmoFHy2CzmCGXeITHY497SPkML7DNg39SGsDiFky8Xzt2pi4fV236zrD6fVO3ljY4M4o6-c88yvSlHPKSsLPbke8dcO8Ni117b1SfkM-rnqHD4rDoENZjS_stIVKXrd_9XWWcBX01JL7oIAkObET80ywlvtxsP2p142zbKYdHIaGC5RP3TsHa_KbQp6jhWyqiWry7Ev327ZZMf_0asbOEekf5qa_s3Hi92Dx0jTPcIgLbj7VBi7OQh0Qr9CFXjgIvNrkzjfBvqTQKqJgut-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJehYIdPbmlubhHor9CPeI4oUqR8Gr0qLolwAho-uNDoh3XrNlUVzWk5PPDjBhrkkCBbVoAc9IfnDGZ_O3sYgr11wp3U8hU82EdghWn4jS49idyz96ygcRLyM-vWair1SXxIZr9xJs5PjR6_kw4Y8gbgnRMIvjvx70i6koAI4QP1Zi48KqOS14-5Hc7AaCX3vrfjzfmI3dr-MXkYHXP-GqcFnhAWMoI6D_FBxlBTVbaomokCe2xc--8cDOepf1sFhD23xOzcFz26GKyXr_42LxLDtKQtldsAPaLoChx2LsIRreIOmE4N-azf5OUfdPuVlJSv00uXNUmjcBUfcCPLzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcryVhTvJ2CKWU7L61oOgQYxgdZwIqGLUtST0YJ2-2Me8VUZxHcXt3kCOgALzt0ODO6YoP113gcogynZ7ax1juQ6UR0aRqi1fkhLgDzRS9zUa4ErMK630jAXVvKQ25sya2zPS26-7WQNiKvZiF2jKkb8KJdBHgKwprqBawHd9J5MRdNibZFCh5OhRGqrhlbxn3ncpmqirXTNiS3EiAmDJ_OG1JS8UsHf0_T3g-NolTFBIzjdsY7gbSmT_J2jrFHy8aOapSNVWd0uSaPVJ3UA_5F_R71tI3ddXlJhWrGsMgI1TUn1i0CU2faz8jVClfcMEaASz2JoZIQ_kGNRwPDP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GLG4ACU5RfyHaIPCv1x7ePgk_DAcfAdRrK5XAUzUSF1CwmBpNWZL2bvTwL2n4qxtIkeCiqa1Cr2UdgEEiHindUeZVw3gFDvHYyniv1JTZKyCZtesXmANvBW7fkbbYroRxRcnF_-OqcDBFX26yDW3cMDjtr-DBxeAH5kavwofH3HO9J-jl7DpukZK8zD87CfLLEBgMd_cbKcvcso0csD2sGTKNS3IYy7cF7RRvPcF36Z4MpT9dKKA6Iie2t22s_7XdqM953_Wstv_Mje3bL-Rcc64cf6XnH4Tz-KrGZfWvcc-8JIHG-h4Sa4s0zbQjIpjECifgk_qt01oEt8DttfAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJkC5OOu6Bl3i5d9sjfLgQwy2SPEjKY6LrJOA949MSrern588R7I8dUdmNU03G8MBMRGxh68j0wrLwoSayJAQfBpz5uIuN_bMUxq3EZy03f49BcLyG2x5HXOhMTBQ0ADT7J0MG2j_ERYH0aiyWL66LjqUTuG8M2y_coPPqCVB-nKn5-HaqRtsUtR7TYi7Y4bPs8xs0wknXnwwLOGI06nFqScBFq_URYVSTc8zboCsbsaFYGmAWYrAB_IU-acT7gbfiozryTxAZkVPDSIN0S4wHEETMXSJ0NNLkAZdyZrXcuzNeTr6sBemsRP2aa0adHuVutq7BjNBhGYEh6shhY3uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQcaW5zGEgSIgwEdXtNY3uM718fTyjfl1wW3UtagSd4-hZFtS4bJOtCDOjKnKblSI3NFINvbFrREhthGDnxa8JH3pvthApVIv4CvlAd67uKZjH_MP0BWnZUqDiyP_uPg57n_Kt7jjr2MumlPL5MryinZDVdfb4qIZg1TI8Nk6bjyzlgjUf6UKiDajExuk9RdA6FQPp2gpvdMSsfGfZTzIexOjahFmezvJs99xIRG2h7Ek2fBRETKSq58LfH56eBen-N6IQTq01pI-SURTVzSDtNXR4g5cQV9-8tO9yKvP2l5qdJ--InswEfMcLGY1pZOlTHEIiFn4Ric9SYNk9mFxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
