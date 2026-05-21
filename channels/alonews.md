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
<img src="https://cdn4.telesco.pe/file/NaDwbfPmI2EfXR5CuA6pz9kb3wddb3RksZ7gpIj7a4dYGBm3Ma9tBqYcm_OrtAavKcwfAww8OqdhPlccBb7xxL6P4ygm5fS2F7PAgJIQBnodV9WFxudUBO4yXTFNU1ElUaQzt0kbPsOI2hSRyxhkqKOmfJja9TBCbJnUY_mRu2PBdyYHNPY0X34yNIkSBP8Z2L5drA4nk2IuSSkFw-zzINcdYVLAXMuWp4pC1ikMSklWMfM34tI_8_NlR1dESRd2sDFD2_7Tsx3QUyC4d2bCIkg8kogrgc22QGLc7UXA95Kt9-3i92UMKullQjKqdSiam3M9PC6b0hCCW6OJiWM1QQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 20:07:52</div>
<hr>

<div class="tg-post" id="msg-121613">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnskMCuShN9306cu7Aw3iHGTGytUfU7GNW8gREwg2R6Z4HTnAevq8DFRyREOlM1uuknS0nIBujou2VF78grabs0G7WqnBivhuNCPprOMYs5ogtmSICMl5bqR0P9wsZ-gPGfbFykQXwiuY1sRU58DLipoFizkUFPWAyaO6xy3ZfwUav-hWB0z_CQnnfPDxksuf97Xz7j5vElXUDT-horNzA-T7Auuq9p4j-CfzP7VbSCpPEyj-IGFxTECALxzfB_BZCB4Wqp4fgzvLzcv5v56aEgEGuRdFkvoy5cUcEdo1cinXRyxO8qr7Y4fXSmt2S3KixT3ajWkEXkKB7VwF2rKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال
:
دولت ترامپ به بزرگترین خریدار نقدی کشتی در جهان برای اوراق، مجوز خرید چهار کشتی تحت تحریم به دلیل حمل محموله‌های ایرانی را اعطا کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/alonews/121613" target="_blank">📅 20:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121612">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترامپ : قیمت بنزین در آمریکا بعد از پایان جنگ ایران تا حدود 1.85 دلار سقوط می‌کنه
🔴
این وضعیت خیلی زود تموم میشه و وقتی تموم بشه قیمت بنزین حتی از قبل هم پایین‌تر میاد
🔴
چند ماه پیش تو آیووا بنزین 1.85 دلار بود و دوباره به همون عددها میرسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/alonews/121612" target="_blank">📅 19:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121611">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ: ما عوارض‌گیری در تنگه هرمز را قبول نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/alonews/121611" target="_blank">📅 19:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121610">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: ما تنگه هرمز را از طریق محاصره‌ای که یک دیوار فولادی تشکیل می‌دهد، کاملاً کنترل می‌کنیم و ۷۵ درصد از قابلیت‌های موشکی ایران را از بین برده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/alonews/121610" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ترامپ: ما تضمین خواهیم کرد که ایران به سلاح هسته‌ای دست پیدا نکند و می‌خواهیم تنگه هرمز بدون تحمیل هزینه باز شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/alonews/121609" target="_blank">📅 19:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121608">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: نیروی دریایی ایالات متحده کار خود را به خوبی انجام می‌دهد؛ به دلیل محاصره دریایی، هیچ کشتی‌ای به ایران وارد نمی‌شود و از آن خارج نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/alonews/121608" target="_blank">📅 19:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: اورانیوم بسیار غنی شده به دست می آوریم، آن را نابود می کنیم و نمی توانیم اجازه دهیم در ایران بماند
🔴
برآوردها نشان می دهد که ایران روزانه ۵۰۰ میلیون دلار ضرر می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/alonews/121607" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121606">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: درگیری با ایران خیلی زود پایان خواهد یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/alonews/121606" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f431a2f476.mp4?token=uFj9jHm5MxWIUocpJj8CAtXPQ7TRC8CU07PZDmmhppkAQEvtS7WfVuM4x-waiUeEwFAUEoffjtHSdUxvdtSzIm1lK66yfOaSuV4RJSB1KSSwwpxwxgIosL_njvtIPVtkBUo77ujGw8XhA3lOIl0UYbvdm-FwzIJQne3g1fGayNg--fVIv2NlvTmelKhqnxLODzCqg_rmFrcCutlI9fNchdrKPX6PqAJsAJXv5tu9-28YdMn2EwL2OzccnI6lD0IQqfpnQcE4QudhdSnNCd35QwIixrI0vRdrkvgZCTBfvUlBCjgOSTEexNNvvg_f77EK3J37tX67Vxs0A-X79KmJxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f431a2f476.mp4?token=uFj9jHm5MxWIUocpJj8CAtXPQ7TRC8CU07PZDmmhppkAQEvtS7WfVuM4x-waiUeEwFAUEoffjtHSdUxvdtSzIm1lK66yfOaSuV4RJSB1KSSwwpxwxgIosL_njvtIPVtkBUo77ujGw8XhA3lOIl0UYbvdm-FwzIJQne3g1fGayNg--fVIv2NlvTmelKhqnxLODzCqg_rmFrcCutlI9fNchdrKPX6PqAJsAJXv5tu9-28YdMn2EwL2OzccnI6lD0IQqfpnQcE4QudhdSnNCd35QwIixrI0vRdrkvgZCTBfvUlBCjgOSTEexNNvvg_f77EK3J37tX67Vxs0A-X79KmJxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما کنترل کامل تنگه هرمز را در دست داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/alonews/121605" target="_blank">📅 19:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121604">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: من می‌خواهم به کوبایی‌ها بر اساس اصول انسانی کمک کنم
🔴
در حال مذاکره درباره ایران هستیم و به هر وسیله ای که باشد به هدف خود خواهیم رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/alonews/121604" target="_blank">📅 19:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121603">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6a2a9ae6.mp4?token=WD5oo_5SXweYx8y-EuJwY2bMuqe_IEdSR9hs7zomGoONYs5RXNfoMBpX-e9ab6ezBG1Csv6L1XkqIjaVAKUkINDEkXhqahPXO-g7nhNvFzRZqgas_2dTwjb7aEfOKuVxwVBX5JDs8yZOOgeaRmZ_RxNurdeuAcLo8fXhwmRAJNBDfaC_eeqxDeJRm-vTJXfS4uZo3-Pd2a0g6OyBN-22UGWWU7oil-x3lXUngLPKzFGdeCMtb86ab_-2xIFLhlSdXYKq3p_R0eUJEYYq7s0DZUXNZriKxU-yFpWhwKwF7BlD44Y0ijO1ZLw8ELtgBmUICQS3h10KBOuquG4JfdYJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6a2a9ae6.mp4?token=WD5oo_5SXweYx8y-EuJwY2bMuqe_IEdSR9hs7zomGoONYs5RXNfoMBpX-e9ab6ezBG1Csv6L1XkqIjaVAKUkINDEkXhqahPXO-g7nhNvFzRZqgas_2dTwjb7aEfOKuVxwVBX5JDs8yZOOgeaRmZ_RxNurdeuAcLo8fXhwmRAJNBDfaC_eeqxDeJRm-vTJXfS4uZo3-Pd2a0g6OyBN-22UGWWU7oil-x3lXUngLPKzFGdeCMtb86ab_-2xIFLhlSdXYKq3p_R0eUJEYYq7s0DZUXNZriKxU-yFpWhwKwF7BlD44Y0ijO1ZLw8ELtgBmUICQS3h10KBOuquG4JfdYJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: می‌خواهم به کوبایی‌ها بر اساس ملاحظات بشردوستانه کمک کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/121603" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474b633de8.mp4?token=NuYEhhhL03McXOdISM9cI4HL5hjDOUmrn5MsFbPjE6hLz8Bl3JmpaQ-6WE_qKYp8yqqgCjXHAScxoa_cRvZU5oO3MX_viYxGrzZbpx9E5AfJV0oPSK_RBedjJ8sJ-APN724U0WUYvBv8Z2LaiYwzzQW0w-3OZ3EbEXWwvOGqG7KQoRHFQs9K4Ek9V_Uyrd_MZ9lj0bkjgjSaBbK43HqjkxuPkxCRcF9fEKgdWNJFgaYKt1R6S4xNcfiiR38HNCZAL_NcTvq4beIuOqxjqqmGO4fnaDwIneMaCm9ZrVzuwDSGND3i0t8zSYkhGWQtvGVGTt5AO1sUR9m5_uGzWt6yLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474b633de8.mp4?token=NuYEhhhL03McXOdISM9cI4HL5hjDOUmrn5MsFbPjE6hLz8Bl3JmpaQ-6WE_qKYp8yqqgCjXHAScxoa_cRvZU5oO3MX_viYxGrzZbpx9E5AfJV0oPSK_RBedjJ8sJ-APN724U0WUYvBv8Z2LaiYwzzQW0w-3OZ3EbEXWwvOGqG7KQoRHFQs9K4Ek9V_Uyrd_MZ9lj0bkjgjSaBbK43HqjkxuPkxCRcF9fEKgdWNJFgaYKt1R6S4xNcfiiR38HNCZAL_NcTvq4beIuOqxjqqmGO4fnaDwIneMaCm9ZrVzuwDSGND3i0t8zSYkhGWQtvGVGTt5AO1sUR9m5_uGzWt6yLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا کنترل سنا را از دست داده‌اید، جمهوری‌خواهان سنا؟
🔴
ترامپ: نمی‌دانم. واقعاً نمی‌دانم. من فقط کار درست را انجام می‌دهم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/alonews/121602" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
جمعی از دانش‌آموزان چهارمحال و بختیاری با تجمع در برابر استانداری، لغو امتحانات حضوری را خواستار شدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/alonews/121601" target="_blank">📅 19:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121598">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOSfnj8Ou1ietzyF-MIfZSBpcRkTbgpBI0-U-1269hfPfC0i4pSd1n3uDlLgtJOR735tYI_dfKpVgucUvNHH2hXThM3HeNvRiGhLY4trXVgUbPgmF5Y30-E3KEWjeFFXS9fblxezONFHtEgLIxWg6m-u5CcZ6eQF1nmbzaoxD5z0aEZKD2-S2oSKjFXL2f5pggGgrjTcn_Ms0v9GKBKCLmorSXGG1ytMYekMd_I4w9O2IA6sEkfzvn5FmGnTmFl-nWg1x2LCgE1egNgkzWJ3XPTa-xMfQXc2kOWRKBr2p10P-QScxfIUJfGyQDhiXQl5bQbwmH3EgJtej6so1QJWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NswX0D5UB9euEuNAIkZQS7xCHLxa4OrU4zXFNjq-S_GdpBNPvg-uaREx1FwVtviSyTvw0p544zJS3lCC_wyFQyLQakjYGhF5JxBuvGRG1YZdSlXHR-JgkQL9br5p82FWCSv39mlrP4V3ShKhpD4YZ2eKDu_yxOn1hKiOTUCTbgX54WtYlknX5xI7vkwKkNtaIEQ1GnxZcm6TzKmtzLWc1oHyEEPZq46u2shUH_G2oPldXIo7mQzOvAjnVo3ZT2A1awLR2n6kLwHKPE0fWrfrZUXOIfJuC8RobHhvD7MI1hJIkouGzQlsH9KIcYKRlDUNYksJtiqMX8VWGal0X8vsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jc65LVuiDqJpBJ3qc35rGhG4P_c2yqCDdOS2J92OipsRr0yck5LYbBz2XhqoFYCfWr0BLOZu7unftsTk4WvSofTf2LxJGk07j1L3ctzT5pPq6Q6L3Mv8101aiuHLrDhWXV8mbErS2WDi0sYJQ2Ry2mkTPB1gOaYYPTxhlDwuLY4VqgINlrHuF7XqXJD6IMlPsnivaWtW7_i-2uoq9rS1JZegk5cGxLxdb6nvkm3Z3w3rhj2zMeZH9Hx12nhA2lF_-svDnv1o0-0eMtvvD4tCYZkPF8rXdOqwX_MkKAKqGMR4Ug0mz1OUjWkcvVIPhonbbQoa7zQfR3C-i_YMR8MWhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌های ارتش اسرائیل به جنوب لبنان مواضع حزب‌الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/alonews/121598" target="_blank">📅 19:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121597">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
استاندار خوزستان از صدور مجوز نهایی برای عملیاتی شدن مجدد فرودگاه بین‌المللی اهواز و آغاز پروازها به مقاصد مختلف از هفته آینده خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/alonews/121597" target="_blank">📅 19:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121596">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
استاندار خوزستان از صدور مجوز نهایی برای عملیاتی شدن مجدد فرودگاه بین‌المللی اهواز و آغاز پروازها به مقاصد مختلف از هفته آینده خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/alonews/121596" target="_blank">📅 19:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121595">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745e6e3332.mp4?token=pdOyOgqR_VQrC0yTPoqnJf09zV4fKz26nA3DGGf3qulMiCG3MRUvC3pxkn82JhAFkFnu-gF4YpB-dSeaJE74dHKyrfkXJ_vmZ14GNn6XFqH6l9DPfwxrBNGvXYswusrasV6HkjTHvuMzSs1w7ct0C4X62NXmkS5Uf_uRnew_7JsZIBk-rh4cZ2pDrcERnXr6hAQ9Rs2E1eLBKWfoEdTc3qinttIAjUPV2p8Mpm66M8MO0kkStFAgIGprBUfVCMSawbM5NYE4WfsbS0snipSHOZaXgY-lyjyC_ejTo9Lf0q3hxRNFQRHSrBu_MAEJau82GpK4y85XhO4aOPg34Ndb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745e6e3332.mp4?token=pdOyOgqR_VQrC0yTPoqnJf09zV4fKz26nA3DGGf3qulMiCG3MRUvC3pxkn82JhAFkFnu-gF4YpB-dSeaJE74dHKyrfkXJ_vmZ14GNn6XFqH6l9DPfwxrBNGvXYswusrasV6HkjTHvuMzSs1w7ct0C4X62NXmkS5Uf_uRnew_7JsZIBk-rh4cZ2pDrcERnXr6hAQ9Rs2E1eLBKWfoEdTc3qinttIAjUPV2p8Mpm66M8MO0kkStFAgIGprBUfVCMSawbM5NYE4WfsbS0snipSHOZaXgY-lyjyC_ejTo9Lf0q3hxRNFQRHSrBu_MAEJau82GpK4y85XhO4aOPg34Ndb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو : کوبا نمی‌تونه ما رو معطل خودش کنه یا وقت بخره همونطور که درباره ایران گفتم
🔴
ترجیح رئیس‌جمهور همیشه رسیدن به توافق از راه مذاکره و صلحه درباره کوبا احتمال این اتفاق زیاد نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/121595" target="_blank">📅 19:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121594">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e2afb4479.mp4?token=Veajmx9OI1LjD0lA1A0ZYWeZpGbZoN2JBCEC94j9vVkGT6nkNCh_SoaOCue4YkHaqALMnf_7NaUrjFDcytA88RLbJUzX0CA8Wk4iLohuhkzKf8naqorB2F3N88ipxu0YG8X097kFzxUnlmo1QfQWMosVXAoRtAskP6Z0I9l6AjwY0_7ettbhIFLWEYjGnbQcIVr4XR0yXCuWfTWMfAlAIoWebweF8Ki_H3qsYwIR6v4dck2x0BQGdu9s7aYAF_sWQes0ajF9OUNqnUqkonEqYGsBz0K4LpM9ye7FQwqOnImxI77IZr-gMo_IUWxN0ieaj2mPregF64QT9BEjPmAgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e2afb4479.mp4?token=Veajmx9OI1LjD0lA1A0ZYWeZpGbZoN2JBCEC94j9vVkGT6nkNCh_SoaOCue4YkHaqALMnf_7NaUrjFDcytA88RLbJUzX0CA8Wk4iLohuhkzKf8naqorB2F3N88ipxu0YG8X097kFzxUnlmo1QfQWMosVXAoRtAskP6Z0I9l6AjwY0_7ettbhIFLWEYjGnbQcIVr4XR0yXCuWfTWMfAlAIoWebweF8Ki_H3qsYwIR6v4dck2x0BQGdu9s7aYAF_sWQes0ajF9OUNqnUqkonEqYGsBz0K4LpM9ye7FQwqOnImxI77IZr-gMo_IUWxN0ieaj2mPregF64QT9BEjPmAgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آیا دولت آمریکا هنوز معتقده متحدای ناتو ترسو هستن؟
🔴
مارکو روبیو : رئیس‌جمهور خیلی ناامید شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/alonews/121594" target="_blank">📅 19:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121593">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: در صورت عدم دستیابی به توافق خوب با ایران، وارد جزئیات گزینه‌های پیش روی رئیس جمهور ترامپ نمی‌شوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/121593" target="_blank">📅 18:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121592">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
روبیو: ببینیم آیا می‌توانیم با ایران به توافق برسیم، نشانه‌های خوبی وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/121592" target="_blank">📅 18:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121591">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: مقامات پاکستانی امروز به تهران سفر خواهند کرد؛ نشانه‌های مثبتی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/121591" target="_blank">📅 18:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121590">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر امور خارجه آمریکا: ما در مذاکرات با ایران پیشرفت‌هایی داشته‌ایم
🔴
گزینه ترجیحی رئیس جمهور ترامپ دستیابی به توافق مسالمت آمیز با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/121590" target="_blank">📅 18:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121589">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
روبیو: سیستم عوارض‌گیری در تنگه هرمز، توافق دیپلماتیک را غیرممکن می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/alonews/121589" target="_blank">📅 18:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121588">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سی‌ان‌ان: یک منبع گفت که در سطوح بالای دولت اسرائیل، تمایل شدیدی برای اقدام نظامی مجدد وجود دارد و کلافگی فزاینده‌ای از اینکه ترامپ همچنان به آنچه که آنها وقت‌کشی دیپلماتیک ایران می‌گویند اجازه می‌دهد، دیده میشود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121588" target="_blank">📅 18:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121587">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر دارایی لبنان: خسارت جنگ به این کشور تا ۲۰ میلیارد دلار تخمین زده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121587" target="_blank">📅 18:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121586">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpm-9OYzXfPeMj9ZyFxrfp02h8eb_8oXxBJ2Yvd9G-UG-Bzkd0N2zRK06F_Dv4nSp-njM79v_Qd1CmntSvNDabI-SA5OwSyflKAq3OyYr83Qq5KyFqeSjy6ppmcs1q7y-8nzHXEZZUpdINQGNzZgC3duw7ZYVizHYHhJ2V1JhF1q2hjZ59P8pfujuffns82aODUQLAOZgFCVC1D70vo20jXqMOtPl4U9Bx2l6ueuGGuLVxGKjtNkhMt1yj7fMnUDNJxfPHZVDCoKAYgOu3gTSSLkrc0n6lCEjjaqTx4dlHJ8zLAqhbvCwtLEv7x2N178JfLvIkKGs0ySAmDWjTwPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا، پیت هگست : "آماده و مسلح"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/121586" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121585">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcbJOV5WU6Z3fKlCDgIyexR6ekMcQHpMNRUPzy70_IliwCqB8QnBfDyoBJVaFi-bxD8w3JlDf6DKub9w5rbuP-wriPfedP6SdcmCq6d_YUFfH6gihMeKX2mzs35c_J8CWUS4m5n4QsrtW4FQFsufjDr4EFtZyC9bcyfOWHNb9wglawZdChJtDRIKXMgVKR2MhbU5Mljx7OHCoWpj29dEaGHYqRUKqMdFD2Is632HQYR97-mFR-9MC617bSpbWJArFlEVZnxe7t385tc0fDwK1g7TVYZjHl0Z44X_-WRetGzTu-MZGjdbDJx8helPvEDzuNp3rKrPZU6YyzEbxdHDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی سازمان آتش‌نشانی تهران: ساعت ۱۵ امروز، یک مورد آتش‌سوزی در انبار کالا واقع در خیابان ملت، اعلام شد.
🔴
با حضور آتش‌نشانان، عملیات اطفا آغاز شد و خوشبختانه آتش تحت کنترل قرار گرفت و از گسترش بیشتر به اطراف جلوگیری شد.
🔴
این حادثه هیچ گونه مصدوم یا تلفات جانی نداشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121585" target="_blank">📅 18:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121584">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر موقت نیروی دریایی ایالات متحده: ناوهای هواپیمابر لینکلن و بوش به همراه گروه طرابلس برای محافظت از ناوبری در دریای عرب هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121584" target="_blank">📅 18:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121583">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
روابط عمومی نیروی دریایی سپاه: طی شبانه روز گذشته ۳۱ فروند کشتی با هماهنگی نیروی دریایی سپاه از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/121583" target="_blank">📅 18:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121582">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرگزاری اینترفکس: پوتین و شی جین‌پینگ درباره نتیجه سفر ترامپ به چین گفتگو کردند
🔴
سران روسیه و چین درباره ایران بحث و تبادل نظر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/alonews/121582" target="_blank">📅 18:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121581">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
انگلیس کاردار اسرائیل را احضار کرد
🔴
دلیل؛ رفتار اهانت آمیز وزیر امنیت ملی اسرائیل با بازداشت‌شدگان ناوگان جهانی صمود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/121581" target="_blank">📅 18:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121580">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت دفاع روسیه فیلمی منتشر کرده که نیروهای هسته‌ای این کشور در حال انجام تمرینات اخیر را نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/121580" target="_blank">📅 18:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121579">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df359f5799.mp4?token=WnjxgHnFlIaEUR6igibSUHHsvhJH94dOROpEaaIlPax5NfE-mvntUVo7HeiLwO5DntwjeRCiPZX-LXx3Qmk-6qpVeEiFgokz7bbWlTQBqtp2Io5mEmNurD5-l4OoPMzP1nK8AsYSxhbbUyC-ozp8DtxFjB_sjBoHeibzAjWyXmFnvt0BAFWwHi4yxiAVcO3q21RIeL9BtwSF-y5hVskQ_dRlZNDbTOFX9V00q1pQdI9yovkdQgbEvoH8LLKlwTE-e7_mGVM4IyI9k3RXyj-FPAnu7HNg8L0HVD1Zqqvsqw2iaYMIEYDjoIzwD06ElSLnTt_7g1ZYReqU_uJfHrYJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df359f5799.mp4?token=WnjxgHnFlIaEUR6igibSUHHsvhJH94dOROpEaaIlPax5NfE-mvntUVo7HeiLwO5DntwjeRCiPZX-LXx3Qmk-6qpVeEiFgokz7bbWlTQBqtp2Io5mEmNurD5-l4OoPMzP1nK8AsYSxhbbUyC-ozp8DtxFjB_sjBoHeibzAjWyXmFnvt0BAFWwHi4yxiAVcO3q21RIeL9BtwSF-y5hVskQ_dRlZNDbTOFX9V00q1pQdI9yovkdQgbEvoH8LLKlwTE-e7_mGVM4IyI9k3RXyj-FPAnu7HNg8L0HVD1Zqqvsqw2iaYMIEYDjoIzwD06ElSLnTt_7g1ZYReqU_uJfHrYJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی زینی‌وند، سخنگو و معاون سیاسی وزارت کشور : تو مرزا فعلاً مشکل خاصی نداریم و اوضاع کامل تحت کنترله.
🔴
از قبل هم همه چیز پیش‌بینی شده بود، قرارگاه‌ها فعالن و روی همه مرزها تسلط کامل دارن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/121579" target="_blank">📅 18:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121578">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزیر خارجه پاکستان:
ما تمام تلاش خود را به کار می‌گیریم تا واشنگتن و تهران را برای رسیدن به یک توافق صلح گرد هم آوریم، چرا که ما میانجی هستیم و در این نقش ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121578" target="_blank">📅 18:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121577">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUTWyk3V7quvDfKfH5BCOVoXPEVkL2rGakctPE-__EUebBsy_2KUDDnJfAf4vQHxbLXTozyKmLzCDyNaWDXe6B6m3M627BQrhZxoIh0kd2axLs2Wmgm7DvpvjZACb4lpdvmRjrsiXfq7roafphEV_q6bTe2_miI6UbX0JOUJ_4cieWaA4TafqPa9WPytfEWgekNbcIsZxxWDjRrqxSa8D35dmp-X6HUwojyV9PGWpFleF-CoKZCfOQgftf-4cfqs9-sNG6qHj3FCOwUoiTscstyCi76lBxGQ04QZZUK52PK8g8TH9yc6AbSo92lrxNjYwnjKh7hZtsonKu2mu1AVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تقاضا برای خودروهای برقی در اروپا به دلیل افزایش قیمت بالای سوخت که ناشی از جنگ ایران است، افزایش یافته و فروش خودروهای برقی نو و دست دوم را تقویت کرده است و به گفته روزنامه لس‌آنجلس پست، این صنعت را جان تازه‌ای بخشیده است.
🔴
این جنگ به طور بنیادی تفکر اروپایی‌ها درباره امنیت انرژی را تغییر داده و خودروهای برقی را از حالت «شاید روزی» به «همین حالا» منتقل کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/121577" target="_blank">📅 18:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121576">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTWmBYly0q8lJmy3dW-ZeeHsKp2VUfbHjP5RoBG0fsZ1wqG5Zj5GqXD1oX-lX71VioJGAKNim-bX230KMjFz34vDIHkW9DpZ-Xls9Ca6s_mspGMhhsHPQw2pYO4EAhjlEsa8fNzYiBGNiGL8a1imNWhcCn4pilMOPZuKRTwnquQTnZ55NOET5ZyJ3VABS1Tmkj4R6nkPJX4bEafCorqFSemo1HH0GWNao8EH4O5B5QcW_NvuuriOWYY_EH2PP24LTIqwyHwdUhSiA-TwhzY75-BE5VIcGWcb6DFfQAhpvONG0V28zjir6Hqf1GjxrFkqX2k0LJC6JxQhso02l9CAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ مقاله‌ ای از نیویورک پست منتشر کرده که عنوانش «چطور می‌توان تهران را در سه حرکت شکست داد» می باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121576" target="_blank">📅 17:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121575">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323f9d6247.mp4?token=Z1fy2a1scGaXbxbScD0sUi693-gj0mXdgzmSZmLCYzk1H2eDR2Y-CVKAtQRrq89wGFQPNjZsVDwzN8ArXQKJZO2zdSDMH0Dz-svANgraHF45UCAInueA765f-AMC7gMV6sFukz88swT8QvBee-YAhe-3LW3AkP6BiSFRtqWmnKZ3eOUc2aIF49By-ToomD56peUHrVl9lTpLgnkhlejr8loi30JV4_uksLQ2xMOro82IMUPXYyThnSbblnhVM862vv8rhlUSRUQy4hQxo4GBDNMMBwHAbPti71IP6zA6CdUk5dDPOM32QWLxQkByFQfNwXzH-eI1ZmUFL0xoPpPZqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323f9d6247.mp4?token=Z1fy2a1scGaXbxbScD0sUi693-gj0mXdgzmSZmLCYzk1H2eDR2Y-CVKAtQRrq89wGFQPNjZsVDwzN8ArXQKJZO2zdSDMH0Dz-svANgraHF45UCAInueA765f-AMC7gMV6sFukz88swT8QvBee-YAhe-3LW3AkP6BiSFRtqWmnKZ3eOUc2aIF49By-ToomD56peUHrVl9lTpLgnkhlejr8loi30JV4_uksLQ2xMOro82IMUPXYyThnSbblnhVM862vv8rhlUSRUQy4hQxo4GBDNMMBwHAbPti71IP6zA6CdUk5dDPOM32QWLxQkByFQfNwXzH-eI1ZmUFL0xoPpPZqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: مهم است که سطح آمادگی نیروهای هسته‌ای استراتژیک و تاکتیکی را افزایش دهیم و تمام اجزای آن‌ها را توسعه دهیم.
🔴
در عین حال، قصد نداریم وارد مسابقه تسلیحاتی شویم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/alonews/121575" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121574">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
گزارش فیگارو از تجارت مخفی اسرائیل در خلیج فارس
🔴
امارات ظاهراً دو فروند هواپیمای هشدار دهنده پیشرفته از شرکتی اسرائیلی خریداری کرده
🔴
این هواپیما‌ها که مجهز به ایستگاه‌های شنود هستند، می‌توانند ارتباطات را در آب‌های سرزمینی خلیج فارس رهگیری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/alonews/121574" target="_blank">📅 17:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121573">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بلومبرگ: ایران در حال مذاکره با سلطان نشین عمان درباره نحوه ایجاد نوعی سیستم عوارض دائمی است که کنترل این کشور بر ترافیک دریایی از طریق تنگه هرمز را رسمیت می دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/121573" target="_blank">📅 17:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121572">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سنتکام: از زمان آغاز محاصره دریایی، ۹۴کشتی تجاری را برگرداندیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/alonews/121572" target="_blank">📅 17:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121571">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر خارجه پاکستان:
ما تمام تلاش خود را به کار می‌گیریم تا واشنگتن و تهران را برای رسیدن به یک توافق صلح گرد هم آوریم، چرا که ما میانجی هستیم و در این نقش ادامه خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/alonews/121571" target="_blank">📅 17:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121570">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آسوشیتدپرس: عراقچی، وزیر خارجه ایران و قالیباف دیگه به هیچ عنوان مذاکرات رو در داخل ایران پیش نمی‌برن و کنترل کل ماجرا دست سپاه پاسدارانه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/alonews/121570" target="_blank">📅 17:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121569">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
علی‌هاشم خبرنگار الجزیره درمورد ادعای امروز رویترز درمورد ذخایر اورانیوم: یک مقام ارشد ایرانی به من گفت که ادعای صدور دستور جدید که بر اساس آن ذخایر اورانیوم غنی شده باید در داخل ایران باقی بماند حقیقت ندارد و گفت این گزارش‌ها «تبلیغات دشمنان توافق» است
این مقام افزود:
🔴
«هیچ فرمان جدیدی صادر نشده» و موضع تهران همواره ثابت بوده است:.
🔴
ایران خود مواد را کاهش غنا خواهد داد.
این مقام تأکید کرد:
🔴
«این موضوع در مرحله بعدی مذاکرات مطرح خواهد شد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/121569" target="_blank">📅 17:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121566">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNQlOSfa6qZjH8IuEfcpRljsj0CE5wDhavJMs0ITk0TMhBbEpw0WgA3kD2WVKawQt5LX2W5KSr8pK-KlS8eKxQbh_7wUa3HllalfFLnVT8-C4-cohGHJhIoUtorv5VuWrWFIJ5LkTMOfj_KXN8QhJeGHkZ_u0GmjXI2lCfgCRK6X1upWMrwAYgUeGbhzzTYVRA0TsAD32kgmLqBPzFqig28d1-rvA2iCsDuvGjswWtT2JccW7d2WkqRLfZhvsRrF1hEy-_EFoXlI42MW_Dfj2CE0EYy6846qKRyWTvg0iZiyqsR9BpIx1NJyEGosYe4Ta52Aw0aoIGts6PgjWeFGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qqA5kPfR-dL7x9Xb-i2tRARjaMAXpsKS8X4cjtQdYw7MJt4LtJN81pJaGs0NesljphuGzb6ONV5erEXihtimrkT2IWGlpWdwnquI67nXn8L3AtXYUZIVyqXnnQx2oE4JrAKNnDk2CzRoHKj-A_4Ee55kL71qVBnoLDiK4M7DE6qy3kApw8gN8IgT0alwUGHUalsgHREq1H_exjRDgX1AmAqJxFyESx-VAlOju0XjeIO4fbg5-1dGt2r7BoAvlIYzapeKKd6okiQZxPSpE6K3bCUFy7Aw8QqmaKg6npe4HV0bWlZuY2mMkZ-1w_Z7XcPHqz_yzCjqfj3qGcecnCz12Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47d204b50.mp4?token=lziSWrAKn5keBZhEoW9ARdPoI5uRjwQrfW2SAY3pgeCwo5Lz0e08wrqJfhU5vL53-MDIQLrUcRJ6AfeuckMIWE1XLAWaBmjG4HXHOUEA7ksNoDCY_-a0N83HBnfPPrrxcCBnskUqOk8xYz0-Hacqkd69TSxjEjjuAhyTX0enNKpBwYHUZnyG38QMl6dkQ0pZHAGvYhM0_Tv6BOaEfatyhk1BOlQvnw3XI8pRGJT7eDixTWf0Thpmc68EpMAoaATi1NkPkJVIKjfUHGsRE4g1JDrfoJiXsFAGU5Ykdo7krr7mJP5toYTvYHGwRI3SN7HHsXJjqcNnoAJSjOv3UWYuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47d204b50.mp4?token=lziSWrAKn5keBZhEoW9ARdPoI5uRjwQrfW2SAY3pgeCwo5Lz0e08wrqJfhU5vL53-MDIQLrUcRJ6AfeuckMIWE1XLAWaBmjG4HXHOUEA7ksNoDCY_-a0N83HBnfPPrrxcCBnskUqOk8xYz0-Hacqkd69TSxjEjjuAhyTX0enNKpBwYHUZnyG38QMl6dkQ0pZHAGvYhM0_Tv6BOaEfatyhk1BOlQvnw3XI8pRGJT7eDixTWf0Thpmc68EpMAoaATi1NkPkJVIKjfUHGsRE4g1JDrfoJiXsFAGU5Ykdo7krr7mJP5toYTvYHGwRI3SN7HHsXJjqcNnoAJSjOv3UWYuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌های سنگین ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/121566" target="_blank">📅 17:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121565">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-Sv0JdfdCu9tKVBZdcdwjsW5sm8rXDLjoURBk9qnAUFTUcikCY1F6yQtxeJOLecLpZ-N9-5CwfwSGviDMONDjKAFSc9CUMuvB7J6nRlokCjYeppfHlzgMlu-I3CHM7EXUThVIAuzjEpFtr0yZxxyoj6yM98YMWmJyOIjJ3dDbba-MPtRgxCDYEaIIGTuOMC6ObGthyOEpt_tjPrvJmksVFEQqnLHVgXHYBB5_636xDUbsZjtoKJEOBpWQE3ATU6436jmciYCbYEZAJs-OB8p3cRH-JpnkVG-KQdMzWSGQBIm_aTZ4GknxhFEikvEjWIz9nhblgHfkPnU_BvtDtl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک نظرسنجی از فاکس نیوز نشان می‌دهد که 60% آمریکایی‌ها اکنون با اقدام نظامی علیه ایران مخالف هستن
د
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/121565" target="_blank">📅 17:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121564">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqCAFG6Xzs76N1CuIpbDfhwzUV2aCZbcCdWNx11gtqyqQUzw0TfMLPJj9loja7nCLmaohZGAoaz59bik0sS1AeKUgMzHyj6ZILE_UIeKdPWhyBa41-wO-iwKYkkySnxCsyDNoMqlyPKTDUozcU7W2ivwkAH-dEiyrFGkQ9j0z2TVddrNnmc1_uk7QQY7l7f73OhRy3UAXBCWGrtVTW9soRh8BzQu_ytu1BSWntjMzP8BhLSGq9GGlviQaQn51wLtsCVANhs1QBLQWBFSBsvJGw14LR0RXnRd6UJPOowU3qQ3iHQO2376K--WSkDENuoSylnZOGLC-iv24_ZNsqfmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی گیگی
9️⃣
8️⃣
1️⃣
تحویل زیر یک دقیقه
✅
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
💤
این تخفیف فقط تا ۱۲ شب فعاله
💤
⭐️
@Napsternetiran_bot
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🔶
@Napsternetvirani</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/121564" target="_blank">📅 17:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121563">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGJSIHdGekmkuhpLSDLLYAZ_az-Kcuaj_F1q73SgHv3Lihy1YlETON2eKR8OC4vHOFzj_GNBUWQSrVFSbuvUc_DJQoj7Cp-d6ckb_vqBdsOoyZeUuEg_NMCNyNXfx4u8FdBeikPEPw2UBfxN3np4Vmtd35qN8ny4WYANusbW12_EvHZ-9kqwevZFmojDk8O8PKXzHmtXqMHwhpyEI213iq2yFHAyJFDVRVQaLZ0_USg5nDss6uNtwsCw2WeA5nJuXqHasFQphrW5OvknZTd5KWga1aVb17spVa2GJcZ1bADsp6aIItB_m3skwPuWhAHuDUmy7NjdTQvNkrojOoMftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک :
انسان‌ها به زودی تراشه‌های سایبرنتیک کاشتنی خواهند داشت که قدرت‌های خداگونه را ممکن می‌سازند
🔴
این فناوری می‌تونه انسان کور رو بینا کنه ، افراد فلج دوباره بتونن راه برن و ناشنوا ها هم بتونن بشنوند.
🔴
ایلان این تراشه‌ها رو به عنوان «معجزاتی در سطح عیسی» توصیف میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/121563" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121562">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها،…
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/121562" target="_blank">📅 17:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121561">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها، حساب‌ها یا حتی دارایی‌های کریپتویی‌تان در خطر قرار بگیرد.
🔴
قبل از نصب هر برنامه یا باز کردن هر فایل، حتماً مطمئن شوید که منبع آن قابل اعتماد است.
🔴
امنیت را ساده نگیرید؛ یک کلیک اشتباه می‌تواند خسارت زیادی ایجاد کند.
⭕️
تحریم ها ارتباطی به موجودی کریپتو شما در تراست والت یا سایر کیف پول ها ندارند.
🔴
درصورتی که کلید والت خودتان را در برنامه غیر مطمئن وارد کرده اید حتما نسبت به تغییر کلید و انتقال موجودی به والت امن اقدام کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121561" target="_blank">📅 16:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121559">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYHdo4GFMZeawncpoO11lqihHajh83lhdcz2jmE1J0mW-rzRwNQ-xlhf19Q6_3PxLxKIeuUTS0I-9QjlyDYX2dzDccireYitfGKZYLOeX4YLfaeEsJdJkSuT-E-pjeI7oTPaPiU5uYOSvHq_-ZVxrwRpDxXEWWLORDNoBuPAffXINyOn7ZOk2hWxYSG6ZQ6rWRZtTQVoNjkyh7gOJAGGVYrTG7MidCwhMEb3ZENLbPxPfCpBqktrAJrjMzkJlXrT01EBTd2hr9Vi7N_vUf23dfBvNUBTbwLfpB8BqI-DVC_FcSCMVwoREnVCXMNcQcIzLtLUO4dhd405m1_4r_i7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ht6-U6-JeaNNt4Q5gljxl-QdMvBTXvQhClu2YuLaJ__zaeuPhcYVphmfuruWDvKXChuletXkSOj4kUzSxvELux1eVjDS_nty-SgYFvcV-9cCeeRCRGVnxYZNjGbwS5IadGDTF5kjCOn36TIJc-oBzlZWWaeVom-D2a8xGTQyUHXoOwOUN8GOBzePswu9Un5aFof80vuHnaX2XOSNvAMX1Srv8utNeZpfg_HvG4Ndp7g2p5yvJ3fG9EAkJ1ovG3TB0pXEwVa73YtTwzR1ep3_lb_a80sQYmUgeKDicFEQ5B_qZBLzyZMMNFVnpoUTrbkFNbHWxD-IuNSdSxmuYXk1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از حملات به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/121559" target="_blank">📅 16:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121558">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLQ5cNIGCcjFk_PJnJvAfawVcdANsj57lIsMg3hPcqaxyv8SOjOg_KkKyCDvD1vUppUUxWwgpS4_F1BIen7n6Zw019A5RM7GJltbxqdNe6TwK_p4aLyFi0dCnHKAkhqv4MfhJoO54ktwzFzES7HN6-bNOmjbkVph0aBE5DNr9pWB51XHDT1srGDg10XiJn2YCSuPbS13GaUzR-8B0Rh7gf0eR41Kj_UWwap0RJVPPVTte3Qo5bVGx4GO7Y-sxc49igE95uivy4DmQ4IVzQP2528HG1DJnfxFIKGN76CDIotCIISZVDdgDAs7iW6nfcUqbMIhIdo390JcH1TkrGk2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان بعد از گرفتن ویزا جلوی سفارت آمریکا در ترکیه:
پدر یعنی عشق،جنگ نکنید.
@AloSport</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/121558" target="_blank">📅 16:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121557">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxChMzTKJdGKDC0D0Uv0l18ov8A9FDKfyDRVmGKlcxABmErEuN81FdPzh102H_Kx4dqgYTP9SyLozm7L_sfykPRyGFqbD2wnReSQiz7q_mGUfs3Ybf9SEhZ7kbHG45PiljCb6oRJfk9iZRqMzGXW0Rn14WFMJzCFhCgeMrMQYzQRbz8pX9TYQgRcS0UUJficNAP3iy7olch3xNIayYhycg9epOJA2xDDrgwdpjcPv1kw72tRPE-dpzNAAzkkBUrdXsm1tKGOVEfJZT_IeSnjEGCGyI7k_igLpl4MuRoTZKB75PbSZ8bxYezUzrTNSQJvqnAUH_txoOXgGXk3uYHa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکانت کاخ سفید عکسی از ترامپ با کپشنِ "عدالت اجرا خواهد شد" منتشر کرد؛
متن داخل تصویر:
🔴
دشمنان خنثی شده‌ی آمریکا توسط رئیس‌جمهور ترامپ
مادورو رئیس‌جمهور سابق ونزوئلا، دستیگر شد.
علی خامنه‌ای رهبر سابق جمهوری‌اسلامی، کشته شد.
ابو بلال المنوکی از رهبران داعش، کشته شد.
کاسترو رهبر سابق کوبا، علیه او کیفرخواست صادر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/121557" target="_blank">📅 16:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121556">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بنده با قهوه و اینترنت زنده بودم یکیش که شده کیلویی 4 میلیون اون یکی هم گیگی 200 هزار ممنون  [@AloTweet]</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121556" target="_blank">📅 16:36 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121555">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
فاکس‌نیوز: ترامپ و نتانیاهو، در یک تماس تلفنی حساس، درباره گام‌های بعدی در خاورمیانه گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121555" target="_blank">📅 16:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121554">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/یه مقام آمریکایی به فاکس‌ :
خبرایی که میگن مجتبی دستور داده اورانیوم تو ایران بمونه، کلاً الکیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121554" target="_blank">📅 16:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121553">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw4DRIvmzf88eJ3_rM1vQfEPmXoZGi7xx_XgxXSJGS4nDscVLlrgRBoWnAa2-5ThWRD6PGArBXzUGsunGRerol6oNr_RTRDlt_ECS9aCKb5g2iM-kT3BJKEY1tEVk8n3wdSpYCLnxptt8TzD9GVF8UeOcky1u0YkUUi-KsClDn7XlGAOjl0b2QtYxgGcB5a3qdZ1TbboEzMZoWQr5NWNdCbbpmBTXvbj_QJg6wWiBMGZuN6GFVtxqZnuG-9owaDd5nstMg-hAelfVx9DhK526QpqhtYFtoZuR7iKPawmbDPF5OSNLgzbwqnFphrwlHQ5ELwcCRDJtBdvUUqrCB2C5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز
:
بعد از اینکه دونالد ترامپ هشدار داد که «اگر ایران به توافق نرسد، یک تمدن کامل امشب نابود خواهد شد»، در پایتخت‌های اروپایی نگرانی و اضطراب ایجاد شد.
🔴
یکی از دولت‌های اروپایی فوراً از دیپلمات‌های خود در واشنگتن پرسید: آیا آمریکا در حال آماده شدن برای استفاده از سلاح هسته‌ای است؟
مقام‌های اروپایی برای توضیح به سراغ وزارت امور خارجه آمریکا رفتند و انتظار داشتند پاسخ روشنی بگیرند.
اما طبق گفته یک دیپلمات اروپایی، مقام‌های وزارت خارجه هم گفته‌اند که خودشان نمی‌دانند ترامپ دقیقاً چه منظوری داشته یا بعدش چه اتفاقی ممکن است بیفتد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121553" target="_blank">📅 16:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121549">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdczBurW3355DvREBe-VDY1aJa1BMvvIlzZzyBdPJauMxZ7Lqz0NsI9sY6t_msqC4CCwaTrFQKz3vRRF-ibBXsynpFAIUjWsUHVQNsy8-IGTHf_08Wlp1BM7S0lngNkF2RVHojwkS_F3PRtnJjG_rC3l-UokC3xMTd1dOQMHSUQRbgljFAs6GlYECZU-h6s42xJ-uuOkH7Cn6sLbgZA9GK5BJ0vXUFTDxAjXcbELaxrTeiV9ZicmkbZNcbcsvgCA5PALnv3GCyK1BFGmOaNIlc3SeYEO65Rx6rA_goXCIE75eKHOjjXA1x0dV85S9tzYENYZFKWohx7LbMYy45owSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SUA7tgA_j3HrdEe5ojcttP63RvrN3ytvhEwb3hh4rCiPK-lS5VmB3ThoTG88H7lLGokPm0nBqBEcqgdrelUFvg5eFijQ9O1jobfgW7D2Gg5-pUCGR_7evpnaVTiqecuesGsf4fsnz7gkW1yyfv0Qk5Kp3ZfVYAatGCX6JASlM08fXt1rZhi-oCe49OD5yr70Ys0HDS3pqUQcYfI_2PmnKKDutpPsQfkr8DDl_VPMX9CIJ4expiWJ7e8i8kcmswaZfx0AKCIlbGOUD2iuTwLtd4hCelXVq7nJPQ0M_9qr2o6X-QFwAHNb_jlFN1LHznhc3CVv4ZLCbI5_xUHoGwjejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EHr22RhQcooGGynIrhUvjz30KR2pnghWDjTZCLcYnujzcSrAUGvSdLp4-gLRW8lNGisqV6191-KRLFY5I1CZsEMoeIu8yFMKn1Tcstbd__m6LpYuuYNNUe9p0sO9RQOmz9Pk-qxZo1p0VpiTu5FkvjtzS-spPWdJVEZU9CBwjHFmhKXitigX7Ds1afHwMPb7GKjUqRclqjk5tp5qetPY6LTnCPQ-fGWcvA6msQ2ZeTwOllFrMz02ZpLD9ZFJU2Ej4oQ41WbJ_MeCrsmqG9RrQzQ2MOhqeT4aS2At3mcDCn_eW39u6m8DFmMD3uUh8V9-YWRgLlr5bzWcqyPBISdZLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f9410350.mp4?token=h7J_TewxMtkokuFANFD2U0dfhXre052KM4XcJIgAkDF3VI6UkTbhW0OFo-oY0_JXn4SbrmdB9fOlkVYt5HqM2nPPygIl-LEI5uuYO8dv2d5iRsenmlSg3PDR4ixKfmBrtV67VD-GenmhcPkf22jLBIJ1NoLdanV_JynKgpAJXCK_XFn1gZtn4IS48GxigddaEATpcnngyXiy1x-y5z2A3DfsOkOxSyEiZeGdWi2w-Q6PlaskGbymbY3GXXDRiEtHy6DRxSN42TUFek7N7H3rHgomcKQ-p4jtt1jwkKP9yk10XXs-7U_wOgigdhzfqbxqvkzG2BkznUWabahKCa297A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f9410350.mp4?token=h7J_TewxMtkokuFANFD2U0dfhXre052KM4XcJIgAkDF3VI6UkTbhW0OFo-oY0_JXn4SbrmdB9fOlkVYt5HqM2nPPygIl-LEI5uuYO8dv2d5iRsenmlSg3PDR4ixKfmBrtV67VD-GenmhcPkf22jLBIJ1NoLdanV_JynKgpAJXCK_XFn1gZtn4IS48GxigddaEATpcnngyXiy1x-y5z2A3DfsOkOxSyEiZeGdWi2w-Q6PlaskGbymbY3GXXDRiEtHy6DRxSN42TUFek7N7H3rHgomcKQ-p4jtt1jwkKP9yk10XXs-7U_wOgigdhzfqbxqvkzG2BkznUWabahKCa297A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی دقایقی پیش حمله هوایی سنگینی به تبنین در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121549" target="_blank">📅 16:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121548">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGSVSndT7lrNCLdQf6x-NRKxhldp_dQkdVhNWWuXFbWi5eIPogmDsIizUcb4P4HDSKqPKuformFM9HGk5xdh_y5DWk3WrTla90-Uc6lPtRdIxQE_sI8z6ZM05fqkoooKDjA1DpQZTF_1no_EXtU3JAD7j3JSJoBkObWSoG35jSvgQMqh20nTh7q8HOE3BvTv-43VT69-J5Ff0nwolD3KRmvHMwl9hYDS_aOZN3a3Hnp2gEfhRiXnEs2_4jaFXiASvXCMQV7TXKLB8BZXIu9NelBh-Vw7yEhrPwbRijJ7yX0OUDwDmVPyniDcGykspV4he3GCocVkHwfY4Mhywk-LSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز
: وقتی دونالد ترامپ ساختار شورای امنیت ملی آمریکا را کوچک‌تر کرد و جلسات منظم تصمیم‌گیری استراتژیک دیگر برگزار نشد، مسئولان داخل کاخ سفید در پیدا کردن جهت‌گیری سیاست خارجی آمریکا دچار سردرگمی شدند.
🔴
کارکنان کاخ سفید مجبور بودند صفحه شبکه اجتماعی Truth Social را روی صفحه‌نمایش‌های مخصوص باز نگه دارند و پست‌های ترامپ را مثل دستورهای لحظه‌ای سیاست خارجی دنبال کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121548" target="_blank">📅 16:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121547">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مقامات اسرائیلی به رویترز:
ترامپ به اسرائیل قول داده است که اورانیوم غنی‌شده از ایران خارج شود و هر معامله‌ای باید شامل این بند باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/121547" target="_blank">📅 16:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121546">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6Ct3fap2o77KPiNHxyUltvuai0X9Yh9HFaSA78_Y6kTSVyJ3ccXXdkurQsMH8X5qfpubrYz8bynQ40gJmV0pjP1pjpQFjTmD_4Ch8nZCppgNKWiuHd-hrvtnFzenKeCVSNv90Ayz2YHBvFccwQko2wSWTuszmij8OvkMw9eT9pn2huSyIPHtZphvoFX9vCbrhW1bNioPAgVCD8bVwKg3wffg0RmWu11sf9-aUykxtpCfttvrtGcPBlPzxEQE1R-G-HvsG4oPkhY8SYBuu9I4y8rVG-jRYO4LVO0Ie3U6ggOpOTGPGJYnkrDLMFrJskpTas2KiQE7rIm7SGrxxq9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایتالیا خواستار تحریم‌های اتحادیه اروپا علیه وزیر امنیت ملی اسرائیل، ایتامار بن‌گویر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/alonews/121546" target="_blank">📅 16:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121545">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
انیمیشن هزینه نجومی شهرهای موشکی جمهوری اسلامی و تبعات آن برای مردم ایران
🔴
تمامی هزینه نظامی فقط برای تهدید بود نه دفاع از ملت ایران، چون امنیت مردم هیچوقت مهم نبود.
🤔
مردم ایران میتونستن سالها در صلح و صفا با بالاترین امکانات رفاهی زندگی کنن ولی حکومت اسلامی جنگ و ساخت سلاح رو انتخاب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/121545" target="_blank">📅 16:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121544">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3399d3dd7.mp4?token=WsyuRMUTBO506Rh_Jts8KSz2ZmNPLJmQ09qttZlt-ndylNA1rRmo2-trnXYpKBItqGh48qGvGqL4h17ijm_XCzv03yGk9so1KWSDTidzhI6_sqmDwEQCcpr6VysAykcSqOkKREay-XCqQbp-SxrTNfuWD73oYJclPNiWLDYse6Y3LOwwQrlc3pV5MIDDmjrTab_r5KZEA7YZMXf97AXPOmXSqUqOVVBxnxcxa6YWKdHNR16LWdT3YbFgKJRiRqaqRygKq1oVWW2bbEu9zdmyxiliUWaEIMB5ptkeoIOtBQsRcym2IEmWy4kcpVUJVR_SDqGglLmS8eXMm_mIqFQvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3399d3dd7.mp4?token=WsyuRMUTBO506Rh_Jts8KSz2ZmNPLJmQ09qttZlt-ndylNA1rRmo2-trnXYpKBItqGh48qGvGqL4h17ijm_XCzv03yGk9so1KWSDTidzhI6_sqmDwEQCcpr6VysAykcSqOkKREay-XCqQbp-SxrTNfuWD73oYJclPNiWLDYse6Y3LOwwQrlc3pV5MIDDmjrTab_r5KZEA7YZMXf97AXPOmXSqUqOVVBxnxcxa6YWKdHNR16LWdT3YbFgKJRiRqaqRygKq1oVWW2bbEu9zdmyxiliUWaEIMB5ptkeoIOtBQsRcym2IEmWy4kcpVUJVR_SDqGglLmS8eXMm_mIqFQvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غرفه‌های همسریابی یا همون .... در تجمعات شبانه تهران برپا شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/alonews/121544" target="_blank">📅 16:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121543">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
امارات از پیشرفت 50 درصدی در پروژه ساخت «خط لوله دورزننده تنگه هرمز» خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/121543" target="_blank">📅 15:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121542">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
آبفا: آب رو فعلا جیره بندی نمیکنیم
#آب_پرو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121542" target="_blank">📅 15:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121541">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
بحث عضو پایداری شهرداری کابل با یک مغازه دار به علت نام گذاری مغازه اش به نام فلامینگو
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/121541" target="_blank">📅 15:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121540">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1p0_o-MdvAe6QXEB8xJphtGoEvgNkuvhU4kvgGhIWYF6lqIBwLUQHYM3URIuWvgEYu3yVc3OHSoQbAlTEl6_b6GjyzUONJ-bbn-EzDGp3_lLqp0I_DeYWtnPpvfP-25s2qu5-xSj8Llk9FApr6tCHSziOGiAphHn4VPcBvZ45jLbKcgA4Xh6XBeYll_540J7KtECYITzmsIXHxjE5veJ6raHuowGfqEeDNZiVAu_mccbrebMzu9b3J8pO0bB4XHnUP_Pu_UavtpcVjlkBmzstBP-0AvZ7k2A-Qca-IdK2xY1_EVCwdfGBtYELtvIrgbTWpIPzdwLZyN8lW6bO_uZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق ارزیابی‌های اطلاعاتی ایالات متحده، ایران به سرعت بازسازی توانایی‌های نظامی خود را که در جنگ اخیر از دست رفته بود، آغاز کرده است.
🔴
از میان این توانایی‌ها، طبق گفته دو منبع آگاه از ارزیابی‌های اطلاعاتی ایالات متحده، ایران در طول آتش‌بس شش‌هفته‌ای که اوایل آوریل آغاز شد، تولید برخی از پهپادهای خود را از سر گرفته است.
🔴
چهار منبع به سی‌ان‌ان گفتند که اطلاعات ایالات متحده نشان می‌دهد ارتش ایران بسیار سریع‌تر از تخمین اولیه در حال بازسازی است. یک مقام آمریکایی گفت: «ایرانیان تمام زمان‌بندی‌هایی که جامعه اطلاعاتی برای بازسازی تعیین کرده بود را پشت سر گذاشته‌اند».
🔴
اگرچه زمان لازم برای از سرگیری تولید قطعات مختلف سلاح متفاوت است، اما برخی تخمین‌ها نشان می‌دهد که ایران ممکن است ظرف شش ماه توانایی حمله پهپادی خود را به طور کامل بازسازی کند، همان‌طور که یکی از منابع، یک مقام آمریکایی، به سی‌ان‌ان گفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/121540" target="_blank">📅 15:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121539">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Egezs3AVZGEvR5kkZJraZihDowD2Hfvobjqn62EHittcyRD7rme4pJpez4DjJg3bd_GNVn6j-hNWjEavrI-TDI-4DraoFKbEfgLEdfGf9N1YhRIXIohrVEWYCHdfODGv0EvOtKniZsTH7Dj8-d3B7zGZebGsvvtSDNpUw0bl67UCra1mGGH7uLZJGiF3qznTdX4g_BlYpJVtQ53e9dhcbWFz0IwzxhPYVx_4-Be0vQzPTMjJA2sxHPf7onB5ryKethyW1VXtWss1gPzPfrzdc8-fy6IoG6o3IRPUQU7SJkQ537sln4YU2Wgoh-ex7rzVkNJRezbPdwA7dXI5lBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یزدی خواه، نایب‌رئیس کمیسیون فرهنگی مجلس: اینترنت جهانی فعلاً بازگشایی نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/121539" target="_blank">📅 15:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121537">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSy_J_OfnxHZBn4DTZYQVnqhZLg39b-_YWmnN9FQAD2ykR3-HL0YH8b0xFQu3nexkbNzSDNopG6kmvjScXW6XT2uVAAhmztIMmkb2rfoH4auuRlmlq1E3zDsMPrPiLMOPRM3PpNwWhYktyG_vYrrFD8efpqTwMcyvvI1mao0EgzvPjAft-_0GeXJPtzBv7hnXdItWwUzrB_EPucqY0Tlvfa8BpdpwmdIjhvMg0PeenO8sIVJpddARG67hvJdI22zxR4AlEWCTceHE-bWIpUJR6o0skQlVZZq1iaIneb8f-OCIvknon6pXlPqXyobLN1zRTkoz0Sbo-z7K9-ATLlRJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8IEQXQNox_HkKKth4-H26MRnsNagAeXabGYvcvNWF25V93gdJ3CRMz74nkzATf0TqHJkdZ-T08GQVYkbCj3hlihju2CLzLGenlaAgZhA2gTt1uGt39QGJ6t0pZydGgZ-AKPvMBzm0O-ZhhiRgV5qH-RAxsfJr2r6L1r-OB8gK5vTEWWTbvlgsV4mNsFWLFDvBb1XezykeAfTi4zkiRTRRzeUMnY2SOXEub0jT58D5m6WsuCY61vwcR98ckQIPiCWPAF6awuQk0SX8O4k6zDtKL1GtE5VASLTWINeav9375U9gvX72kLNUOt67jTgS95tWsiRR3pqoRkglxRDmHOBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
مهران سماک متولد ۲۸ اردیبهشت ۷۴ در بندرانزلی بود. مهران لیسانس معماری داشت. او جوانی آرام و عاشق زندگی بود.
🔴
پدر مهران در خیابان پاسداران انزلی صاحب متل کاسپین بود و مهران در مدیریت آنجا به پدرش کمک میکرد.
🔴
در شامگاه ۸ آذر ۱۴۰۱ شبی که تیم فوتبال حکومتی باخت مردم برای خوشحالی به خیابانها رفتند. مهران آنشب استوری گذاشت و نوشت:
«امشب فارق از هراتفاق و نتیجه فقط باشیم کنار هم»
سپس با نامزدش سوار بر ماشین در خیابان به جمعیت پیوست و با بوق و شعار و علامت پیروزی جمعیت را همراهی میکرد.
🔴
در همان زمان نیروهای سرکوبگر با موتور به میان جمعیت و در خیابان آمده و موتوری از کنار ماشین مهران رد شد و با گلوله به سر مهران شلیک کرد. و مهران غرق در خون شد. تصویری که از این صحنه بجا مانده خود یک سند جنایت است.
🔴
قاتل او فرمانده انتظامی بندر انزلی جعفر جوانمردی بود.
🔴
مردم کمک میکنند و مهران را به بیمارستان میرسانند ولی او آنجا جانباخت.
🔴
خانواده مهران سماک خود را به بیمارستان می‌رسانند اما نیروهای سرکوبگر از تحویل پیکر شهید خودداری میکنند. پدر مهران با دیلم در سردخانه را شکسته و جسد را که هنوز داغ بود بغل کرده و با خود میبرد. آنها نمیخواستند توسط نیروهای سرکوبگر پیکر فرزندشان ربوده شود.
🔴
برادر مهران آن شب تا نزدیک صبح پیکر او را در ماشین در خیابانها میگرداند تا دست قاتلین به او نرسد. نزدیک صبح مهران را به خانه میبرند و مادرش او را روی یک فرش میگذارد و تا صبح او را بغل کرده و میبوسد.
🔴
فرماندار انزلی از ترس مردم نمیتواند از حضورشان در مراسم خاکسپاری جلوگیری کند. مردم در گلزار شهدا جمع شدند و شعارهای ضدحکومتی سردادند.
🔴
پدر مهران پرونده قتل فرزندش را در بیدادگاههای حکومت به جریان می اندازد اما تا این لحظه هیچ حکمی درباره قاتل به اجرا درنیامده و او همچنان آزاد است.
#علیه_فراموشی
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/121537" target="_blank">📅 15:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
طبق گزارش دو مقام ارشد ایرانی به رویترز؛
ایران اصلی ترین خواسته آمریکا برای توافق که انتقال اورانیوم 60 درصد است را به صورت کامل رد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/121534" target="_blank">📅 15:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac46jgqQrxRdvl8nlsNptHmtQ_99QoC5R0J6GQr3FJAF6sfMEMvC_0jHKkJNmCFMHzs65c2AC4hasa976B_02r-oCuGGpqoVqyAlusaAwO9UgW4xe6s1lChMSGkQL9Xc52kuboacta5HE-_Qm5j9WqHa1SmdoREyPL18Fv2u2RnikTqn4owb9JR5OEK2cN7QjNitiJRwv2JL7aIAKGMtpluxheL5aMnJepl7R_g9tYmCBa_5BHdciCLnE9M4mtE8pUIwMQvmNTVyBu0P1oducKj1HmtwgbtOxTLdcS8yccPYuBPF3HycFvM1XQrE67PwmmfCOxXab6uce9ZFMUFpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۱۰۷.۱۵ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121533" target="_blank">📅 15:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
آژانس انرژی بین المللی: بازارهای نفت ممکن است در ماه های ژوئیه و آگوست به منطقه خطر برسند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/121532" target="_blank">📅 15:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121531">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سفارت پاکستان در ایران: وزیر کشور پاکستان با «اسکندر مومنی» همتای ایرانی خود در تهران گفتگو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/121531" target="_blank">📅 14:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121529">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTsD31gRPxCj5cybJ0th7IYKLBgFaxHE-KSEOS2cW8a3b1BOg9KkaBRxTGC9DjHAPNOUBwRxnODNevUE4UeW6avHgTcBywmWjl4_MsmtN59bhR7jYeLBHOllafWHl5EdE9nuDCt4MBXny0-JOP0Z4lwjiOaMBAA9vt63yqOjlycUuaMNA5cjN7Qqe8JazA9Wg62Gk8LBsS_bNH8T8kkSm3SGM1LZLJbKOH4ZvgCnWtv78KWq2CEm7mRCJDcNr4M6HE2rN-G7if6E-Vtxqq847_Tn6vOrTEZ7tgT5DDSNjV6V3QYzsF3aRbmBQZmSOUx9mq4ImIxmPj8aOQHfkNL_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae2aa00265.mp4?token=JmYmPlg5M18dB5jEyOBPgbw6YXdcnZkyHg6ixv-lqea1mjUZ-ROngtsiloMymg8TpBSunGZhO8YZOr1WlI1lR1HwLgd1IxfxMQ0pdw1D6ixfNfKzZkSgc_vPTfWKoJixIDw1xr7Rtt4vjZbFQXhTDbLOL_4WOBd6K4TuLO8O7RDdTJQsP7zJw5m1cQiTJBFrEoKC1DlnIA4KpIfpAtuARBT1giWHI4URMrtjKKoU-u87Z_cQsm729GfEeQotMrdIF_sEaLg1DAsv_StSCrhvE-fXeqR8C1Lzh-minbfjkUfqFKdypgMa_tc2o7uSu8NHE2vVJ4L13eumJQxavNMfHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae2aa00265.mp4?token=JmYmPlg5M18dB5jEyOBPgbw6YXdcnZkyHg6ixv-lqea1mjUZ-ROngtsiloMymg8TpBSunGZhO8YZOr1WlI1lR1HwLgd1IxfxMQ0pdw1D6ixfNfKzZkSgc_vPTfWKoJixIDw1xr7Rtt4vjZbFQXhTDbLOL_4WOBd6K4TuLO8O7RDdTJQsP7zJw5m1cQiTJBFrEoKC1DlnIA4KpIfpAtuARBT1giWHI4URMrtjKKoU-u87Z_cQsm729GfEeQotMrdIF_sEaLg1DAsv_StSCrhvE-fXeqR8C1Lzh-minbfjkUfqFKdypgMa_tc2o7uSu8NHE2vVJ4L13eumJQxavNMfHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی در طول شب به پالایشگاه نفت سیزران متعلق به روسنفت در منطقه سامارا روسیه حمله کردند و آن را در آتش فرو بردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121529" target="_blank">📅 14:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6420bc13f5.mp4?token=mYYnV_PXJZ_Onj-Df50v1h6EHP7q2EZth_rUtFUrU9hT0dMu12DLul-Xl3ZUnAS1eSef-xEP5TvY4IpjPPZZiO8S2fljS0VPpkao9GR8p3_DElwae6BAskx7XS8PXLUTI5RTH3cGvAVMB0H_U2f22ek6ATBCmCt6LUPqU6qNj0IFXIiM_dwadAmQa4jImytdcidhYYlT2ldyYJBZMdyJLoOoXImtw2btNnjJmx26dPd0cftUo74R4XYnoDIIUxWTtYXJiy3eUTU2t3qW39X-oMq2TCqf1kQX1rS_hOQFttAvdEPYSpvGMSzP-S3Ld0R9BtU1b5PCBfaIoJWB7-3ltw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6420bc13f5.mp4?token=mYYnV_PXJZ_Onj-Df50v1h6EHP7q2EZth_rUtFUrU9hT0dMu12DLul-Xl3ZUnAS1eSef-xEP5TvY4IpjPPZZiO8S2fljS0VPpkao9GR8p3_DElwae6BAskx7XS8PXLUTI5RTH3cGvAVMB0H_U2f22ek6ATBCmCt6LUPqU6qNj0IFXIiM_dwadAmQa4jImytdcidhYYlT2ldyYJBZMdyJLoOoXImtw2btNnjJmx26dPd0cftUo74R4XYnoDIIUxWTtYXJiy3eUTU2t3qW39X-oMq2TCqf1kQX1rS_hOQFttAvdEPYSpvGMSzP-S3Ld0R9BtU1b5PCBfaIoJWB7-3ltw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرینات نظامی اخیر کوبا شامل مدرن‌ترین سامانه دفاع هوایی آن، S-125-2BM، نسخه ارتقا یافته سامانه SA-3 دوران شوروی بود.
🔴
اگرچه این سامانه نسبت به مدل اصلی متحرک‌تر و توانمندتر است، اما همچنان در برابر حمله گسترده ایالات متحده با استفاده از هواپیماهای پنهانکار و تسلیحات هدایت‌شونده دقیق محدودیت‌های قابل توجهی خواهد داشت، به‌ویژه که جغرافیا و توازن نیروها به شدت به نفع آمریکا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/121528" target="_blank">📅 14:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
امارات از پیشرفت ۵۰ درصدی در پروژه ساخت «خط لوله دورزننده تنگه هرمز» خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/alonews/121527" target="_blank">📅 14:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121526">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kguZZoWNXPdYUVBotnCIzWwY-VpOeis71Vk36-xupttVj5gGq42a5Q7fDe0zP8YjKbrSnf4vBJpjwaE3LHVH5thC4htrTN_hMZRtHt54YEtGbpP4zGU3LwmmTSXW-gwOleRq_oT96eyGjTgzlve7-71BsMF3KO0FhyHVyBC-EU2D9hK4nReVKzjOfy5dabKerbT7iabX1_aSOxaNvW2ven2uVlw89LR_T4FMyPHLdNlTdABY0vwXjyhqx9CybRY0hDAqQJP19xQ0WRDUlvLbUMExbkOhAF7t6tLiwoqkutLesm8BDLgbHepwctwTx59BIC9S2bvwUP2aW91flGdW2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور رئیس‌جمهور امارات، انور قرقاش:
ما طی دهه‌های طولانی به زورگویی‌های ایرانی عادت کرده‌ایم تا جایی که این موضوع بخشی از چشم‌انداز سیاسی خلیج فارس شده است و اعتبار میان لفاظی‌های تهاجمی و اعلامیه‌های توخالی دوستی از دست رفته است.
🔴
و امروز، پس از تجاوز بی‌رحمانه ایران، رژیم در تلاش است واقعیتی جدید را که از یک شکست نظامی آشکار زاده شده است، تثبیت کند، اما تلاش‌ها برای کنترل تنگه هرمز یا تجاوز به حاکمیت دریایی امارات چیزی جز تکه‌هایی از رویاها نیست.
🔴
و هر کسی که می‌خواهد با محیط عربی خود همزیستی کند باید درک کند که اعتماد از دست رفته است و بازگرداندن آن از طریق شعارها حاصل نمی‌شود، بلکه از طریق زبان مسئولانه، حفظ حاکمیت و تعهد واقعی به اصول همسایگی خوب به دست می‌آید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121526" target="_blank">📅 14:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121525">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نایب‌رئیس کمیسیون فرهنگی مجلس اعلام کرد اینترنت جهانی بازگشایی نمی‌شود و تنها گروه‌های دارای نیاز تخصصی به اینترنت بین‌الملل دسترسی خواهند داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/121525" target="_blank">📅 14:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121524">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل‌شده در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121524" target="_blank">📅 14:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121523">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ادعای رویترز به نقل از سه منبع: فرمانده ارتش پاکستان، عاصم منیر، روز پنج‌شنبه تصمیم خواهد گرفت که آیا به عنوان بخشی از تلاش‌های میانجی‌گری به تهران سفر کند یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121523" target="_blank">📅 14:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121522">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نماینده دولت هند : ۱۴ کشتی هندی تو منطقه تنگه هرمز گیر کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/121522" target="_blank">📅 14:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121521">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
علی هاشم خبرنگار الجزیره: بر اساس منابع من در تهران، پاسخ ایران هنوز به میانجی پاکستانی تحویل داده نشده است. رایزنی‌ها همچنان ادامه دارد و تلاش‌های جدی برای رسیدن به پیش‌نویس نهایی در جریان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121521" target="_blank">📅 14:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121520">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
رویترز: رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121520" target="_blank">📅 14:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121519">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d126d72a1e.mp4?token=q1I8s7w-6b9krD7-tMFovXSw4xxORDmSzAIxsK8cRSweowuWOy1slggwfH3fNlkBdnfUDmmP2RMyDuGajch_LpM6K-yooGHzogZTAMofMkpCBa1M-qjGKKsKJ8LYm9YBYCEL6WOfvqtFN7cyPyOO0BvczmvyHZ8qm_n04nAeTMbC65Yzxlv-d3yjsJOugx_6FgE9Iy3XcZ8toRHTJ22x_X6mRtMtRb-qTmhFn57CZr4wLFxqp9b4fgCfCZFYiKLoRNLhmuEXnn4GptVsRy4WJS83lx3OmIZQ6W1sWquhI2r5EdR73gilCiu1o6oTnqoa2eyzvyFKtH4obBicuAcPxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d126d72a1e.mp4?token=q1I8s7w-6b9krD7-tMFovXSw4xxORDmSzAIxsK8cRSweowuWOy1slggwfH3fNlkBdnfUDmmP2RMyDuGajch_LpM6K-yooGHzogZTAMofMkpCBa1M-qjGKKsKJ8LYm9YBYCEL6WOfvqtFN7cyPyOO0BvczmvyHZ8qm_n04nAeTMbC65Yzxlv-d3yjsJOugx_6FgE9Iy3XcZ8toRHTJ22x_X6mRtMtRb-qTmhFn57CZr4wLFxqp9b4fgCfCZFYiKLoRNLhmuEXnn4GptVsRy4WJS83lx3OmIZQ6W1sWquhI2r5EdR73gilCiu1o6oTnqoa2eyzvyFKtH4obBicuAcPxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه : ما همیشه از صلح و ثبات دفاع می‌کنیم و جلوی کسایی که روی جنگ و هرج‌ومرج سرمایه‌گذاری می‌کنن می‌ایستیم
🔴
تو غزه لبنان و جاهای دیگه منطقه کسایی که زن و بچه و پیر و جوون رو بدون رحم می‌کشن ما مقابلشون می‌ایستیم
🔴
از ارزش‌های مشترک انسانی دفاع می‌کنیم تاریخ هم پر از اینه که دوستی با ملت ترکیه سود داشته و دشمنی باهاش ضررهای زیادی داشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121519" target="_blank">📅 13:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121518">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
معاون وزیر نیرو: به ادارات پرمصرف برق، اول اخطار داده می‌شود و در صورت تکرار و رعایت نکردن، فهرست اسامی مشترکان پرمصرف برق به صورت عمومی اعلام می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/121518" target="_blank">📅 13:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121517">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بندرعباس لرزید
🔴
دقایقی پیش زمین لرزه ای به قدرت ۴.۶ ریشتر بندرعباس را لرزاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121517" target="_blank">📅 13:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121516">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
کامران یوسف خبرنگار اکسپرس تریبون پاکستان: پاکستان در تلاش است اختلافات بین ایران و آمریکا را کاهش دهد. با توجه به اینکه دستیابی به یک توافق نهایی ممکن است بلافاصله میسر نباشد، اکنون در حال بحث بر سر یک راه‌حل موقت هستند.
🔴
این توافق، در صورت نهایی شدن، به هر دو طرف اجازه می‌دهد به طور رسمی به جنگ پایان دهند، در حالی که مذاکرات درباره مسائل اختلاف‌انگیز ادامه پیدا می‌کند.
🔴
نقطه اصلی اختلاف برای توافق موقت، وضعیت تنگه هرمز است. آمریکا و سایر ذی‌نفعان خواهان بازگرداندن تنگه هرمز به وضعیت اولیه (پیش از جنگ) هستند.
🔴
ایران معتقد است در صورت بازگرداندن وضعیت این آبراه کلیدی، ممکن است اهرم فشار مهمی را از دست بدهد.
🔴
در همین حال، فرمانده ارتش پاکستان قرار است روز پنج‌شنبه به تهران سفر کند.
🔴
هدف سفر او یافتن یک راه‌حل عملی خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121516" target="_blank">📅 13:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121515">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نتانیاهو: اقدام اسرائیل در توقف ناوگان غزه درست بود اما رفتار بن‌گویر قابل قبول نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121515" target="_blank">📅 13:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121514">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
دولت پاکستان توقیف  کشتی‌های ناوگان جهانی «صمود» توسط نیروهای اسرائیلی در آب‌های بین‌المللی و بازداشت خودسرانه فعالان (از جمله یک فعال پاکستانی) را محکوم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121514" target="_blank">📅 13:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121513">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرگزاری آلمان: کمیسیون اروپا به دلیل جنگ علیه ایران، پیش‌بینی خود از رشد اقتصادی اتحادیه اروپا در سال ۲۰۲۶ را کاهش داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121513" target="_blank">📅 13:38 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121511">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
داده‌های کشتیرانی LSEG و مؤسسه کپلر نشان می‌دهد سه ابرنفتکش حامل ۶ میلیون بشکه نفت‌خام قطر، کویت و عراق، پس از بیش از دو ماه انتظار، از مسیر ترانزیتی مورد تأیید ایران عبور کرده و راهی بازارهای آسیایی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/121511" target="_blank">📅 13:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121510">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d52e08826.mp4?token=pF9tRn35tND5tJLN8hWxQiNojW-IpAUfOaQzzDY7MkGfamv2zO-49yXU5nQ3SMyjlO0rP7yvkrwQZ2zxng5Eex0Zmdfa6BtTaKhHiksfOb5WsgN5j8Aj5M4SKVbiqPT7FNi-w61M3qqBtzKa1Mi1aGnLjXmM1JCngdtP3Y-lvt3bNTr7j2yYKHCE_ER1JSGGTwnjLoKPBXMVT_pI-8pS0WXcz5-d5vXIqyGxGtndMNBH1tT7dZKxf-73uAxnbthAg5CPr7AH29naryPDOunjCKGoccmQCoB2boyF-bZLmpoWyk7g56R17Rt7mKqcW-sHh6TG2oRKNoX-wGoaXfrHYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d52e08826.mp4?token=pF9tRn35tND5tJLN8hWxQiNojW-IpAUfOaQzzDY7MkGfamv2zO-49yXU5nQ3SMyjlO0rP7yvkrwQZ2zxng5Eex0Zmdfa6BtTaKhHiksfOb5WsgN5j8Aj5M4SKVbiqPT7FNi-w61M3qqBtzKa1Mi1aGnLjXmM1JCngdtP3Y-lvt3bNTr7j2yYKHCE_ER1JSGGTwnjLoKPBXMVT_pI-8pS0WXcz5-d5vXIqyGxGtndMNBH1tT7dZKxf-73uAxnbthAg5CPr7AH29naryPDOunjCKGoccmQCoB2boyF-bZLmpoWyk7g56R17Rt7mKqcW-sHh6TG2oRKNoX-wGoaXfrHYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع بریتانیا اعلام کرد که جنگنده‌ سوخو۳۵ روسیه چندین بار و به طور خطرناک دو هواپیمای شناسایی بریتانیایی را بر فراز دریای سیاه رهگیری کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/121510" target="_blank">📅 13:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزارت خارجه روسیه: بحران ایران تنها از طریق کانال‌های دیپلماتیک که منافع ایران را در نظر بگیرد، قابل حل است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/121509" target="_blank">📅 13:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
عضو شورای عالی فضای مجازی: رئیس جمهور نتوانست مشکل قطع اینترنت را حل کند، معاونش هم نمی‌تواند!
🔴
«محمد سرافراز»، عضو شورای عالی فضای مجازی، تشکیل ستاد راهبری فضای مجازی برای حل مشکل اینترنت برای حل مشکل قطع اینترنت را بی‌فایده دانست و گفت:
وقتی رئیس جمهور نتوانست مشکل قطع اینترنت را حل کند، معاون ایشان هم نمی‌تواند.
🔴
رئیس‌جمهور هم نخواسته و هم نتوانسته از اختیاراتی که در قانون اساسی پیش‌بینی شده، به طور کامل استفاده کند و به سوگندی که برای اجرای قانون اساسی خورده، به نظر من پایبند نبوده.
🔴
مسئول نهایی قطع اینترنت و سیم‌کارت سفید و اینترنت طبقاتی کسانی هستند که در بالاترین رده‌های حکمرانی تصمیم‌سازی و تصمیم‌گیری می‌کنند ولی پاسخگو نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/121508" target="_blank">📅 13:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121507">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر دفاع روسیه: ایران تنها کسی است که سرنوشت ذخایر اورانیوم خود را تعیین می‌کند و روسیه آماده کمک به تهران و واشنگتن در اجرای راه‌حل‌های احتمالی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/121507" target="_blank">📅 13:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121506">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouxOeYuIaEu0HMGwQoCISsQDnG0v7i8bOrVD5uqgxREJ-qesC1RQtRYW3WtncFhWyHoErkw3D9FH245-1w0B23TeIrIuAlqNX2cgFQ_McZIJq74N6pzURWWnPejYwvVTyyAjburjaArTuPnQYvH3ClIS7k8Lri8TgA6PlnEQmGHZkLMNZ6GtdA7VwttI-bwau3kbhJjTGW2HYnbojwGN1gTanTCuExXwt1xjm5PzI18GZdC1BrJJ2Q3CGtRT_XYafsPxMFNrCA9y9Hrwh2L0WLxIPmhS1d6jY59eMUJsV9heLHkjRO_gfRWyeHmSeTaOmtrdE3MFjaF_v6ZqMxrluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی تا حدودی متن توافق احتمالی را منتشر کرد ...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/121506" target="_blank">📅 13:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سفیر ایران در پاکستان: من صمیمانه قدردان اقدام انسان‌دوستانه و خیرخواهانه دولت محترم پاکستان در پیگیری آزادی ۲۰ ملوان ایرانی هستم که به دلیل توقیف کشتی‌شان در آب‌های سنگاپور در وضعیت خطرناکی قرار داشتند.
🔴
در این رابطه، مایلم از تلاش‌های خستگی‌ناپذیر جناب نخست‌وزیر محترم، محمد شهباز شریف، و وزارت امور خارجه پاکستان، به‌ویژه جناب آقای اسحاق دار، معاون نخست‌وزیر و وزیر امور خارجه محترم، و دیگر نهادهای مرتبط تشکر کنم.
🔴
این ملوانان پس از تلاش‌های دیپلماتیک از سنگاپور به اسلام‌آباد منتقل شدند و چند ساعت پیش به میهن عزیزشان بازگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/121505" target="_blank">📅 12:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارانوت به نقل از یک مقام امنیتی اسرئیل: ما ممکن است جنگ‌هایی را با سرعت بیشتری علیه ایران آغاز کنیم تا تهدیدی ایجاد نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/121504" target="_blank">📅 12:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ورود ناو هواپیمابر «نیمیتز» به کارائیب همزمان با تشدید تنش‌ها با کوبا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/121503" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع پاکستانی:
مقامات ایرانی از پاکستان خواسته‌اند تا مهلتی برای ارزیابی و بررسی معیارهای آمریکایی برای مذاکره دریافت کند.
🔴
اورانیوم غنی‌شده، گره اصلی در مذاکرات آمریکا و ایران است.
🔴
فرمانده ارتش هنوز در پاکستان است و سفر او به ایران بستگی به نتایج سفر وزیر کشور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/alonews/121502" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-121501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/882a666404.mp4?token=WiZi3x195w0IYvfEzyguP-NS7rLLqkhXcDVuxh2w2yGvl5aXMMfNoggBMcXQjCjNSBuN4vNSeELnzcz3XnZL4zAqFL2FXLgKQLACS2Jnx78F2W41aed65UTvYWrpLXpuEMLdr-lutHqywE7OItD_StO-o8ijlZ30ndPRQ1RKsS6Zx1wXomLRBbxZ-K3eyxUwhnLMMkzvKNKIxtVTn9CMnARCebzLuSv9D64aYYVDqzV7tX81TB85pJO2Rg3pBFL3TJaGCVIcudQfdTKpLwEthbJUVyeMoMx0aQXCKWYMCALrEbhrCTE8HeOf7SbibvfbdsFdWttnlPTsc_GenaqE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/882a666404.mp4?token=WiZi3x195w0IYvfEzyguP-NS7rLLqkhXcDVuxh2w2yGvl5aXMMfNoggBMcXQjCjNSBuN4vNSeELnzcz3XnZL4zAqFL2FXLgKQLACS2Jnx78F2W41aed65UTvYWrpLXpuEMLdr-lutHqywE7OItD_StO-o8ijlZ30ndPRQ1RKsS6Zx1wXomLRBbxZ-K3eyxUwhnLMMkzvKNKIxtVTn9CMnARCebzLuSv9D64aYYVDqzV7tX81TB85pJO2Rg3pBFL3TJaGCVIcudQfdTKpLwEthbJUVyeMoMx0aQXCKWYMCALrEbhrCTE8HeOf7SbibvfbdsFdWttnlPTsc_GenaqE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رامی گرا رئیس پیشین سرویس اروپای موساد: کل این داستان غیرقابل باورست. احمدی‌نژاد هرگز به عنوان یک رهبر انقلاب معرفی نشده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/121501" target="_blank">📅 12:39 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
