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
<img src="https://cdn4.telesco.pe/file/kq-TLgnxTQKix_8NehwwZtXcnZP_ybdflKCc8zOrPVDPYKKu5sQOM6-OkvAS52GTnX-vdvvD_DjZL4VNgk5QunWhmJr7gZePtOqJhkO2mUd62yB3dk4UrZ5BYMBbEr_F4FK846amyD9xcCxNMI7B_RV7KLapgT18xVQfuaivOrQ_aLAEKE2NDjjkWvuKAeAp89rNWMjGwE3eNJTg4pT9EYYLLc4lvZvzVSLH2trSV4YGSdJeR2LGeGe0g19UBceP-wYSbqAURI2DBZUUOddj46Ve8WQM7P6xtw8HRG57ef3sG9blqzX1wy0ldL-0l2puCW8FwPq2-JdtA873C3QWbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 19:04:30</div>
<hr>

<div class="tg-post" id="msg-146911">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnEYEddVORO5spW3dddJdU3-NVY6A0b4i5RH-3F6xP_fUhb-3NCvV6d-KSqEUsqyKhf9Si-zS_tiM3vdp-9jJaF_sR749RY3USPp9M1EwrpmY-qofFNO17WeIDLt7uEIfpVZ0CZpcTyJBGDMTSR2JiAFpU5zYfY6uD67_QBre4uj96Tdz489LTwMn6_0xmraI3FqZSfwYKR6Bw7WbdY1Ars2puTVPnl-YsvMYHP5Bq3xDDkvmn0etpmmzAn3VktM48dP2oghFcsWttX78CTAwWtIObI_oKX2zxo6beC0lLWy4WfOG7OgkmBzy9K-lzdHd0MgZlGHYdbLrjZ6T4X4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیلی به نبطیه الفوقا در جنوب لبنان، ساعتی پیش انجام شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/146911" target="_blank">📅 19:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146910">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1X2k3iTgn6Yr_mdXYLPQ4XDKtp500XNCXqGzzUalLnzlb_gncg8r_NWa4RpQRksbieEGxow9pcT0SuLRyornIl1iJTNl5McGzqK043IU1sjaleTIXeqpzUY0tP31WwiGvvNm7hmaw8UD-8pi5HhJ6AGjIzy7yuUw4mgZn1qC0kSVkonbGJk0uM03ZJsRbKAQqTENB2nrHBQyyOnXTFZWglzVkxK8U-IElBYXqV8Qdir2XUSaI5C1qEXUgcCQHrUNwzGJNt1AO-dL6P5iYe0C4ktCPuEqgnHOZIzwXgucElorrYS8eXHzee8dyO7S6082Rn_cS7BwhIZHQdQ6ZGLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل:
اوکراین
مرکز کلیدی لجستیک جمهوری اسلامی و روسیه در دریای خزر را هدف قرار داد.
حملات شبانه‌ی اوکراین به بندر مخاچ‌قلعه، پل ارتباطی و حیاتی دریایی میان روسیه و ایران برای انتقال پهپادهای شاهد، آن را از کار انداخت. در همین حال، ۳ ناو جنگی روسیه در نووروسیسک به شدت آسیب دیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/146910" target="_blank">📅 18:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146909">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HkskbwmMIuIhzgN7uEEdO3dMSTfoLXLFTTPamwR7oM-UjawRHq9w9QPTkc92ZTSwuYnHj0j8MEl83EmHkn8blxFxBPHXwBupTGQX6sHuF4uXe2h5CZaYgEA81_06WNqwR5IOZY77vTNOfCWSeM-Fu6QkyhZrDIh4VmknkooD2I2TGFeMgQmOeH05f83g2tfyCxGpKNqkNZdWlsf04QhXap2e5mKpsUyq_oxcq1ODoBo33kC5Ih4koRgG9aGeH3bU_SYD4oj6e2M91rxjk3VYRsp25OTAq-Mt8ywZkdJWxOoK2HJhc932ug5CNOE9UYtvX6mzvVs6Fn1NG0RGnyl29A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
VIP مخصوص روزای قطعی و اختلال اینترنت!
😍
اگه نمی‌خوای وسط قطعی اینترنت بدون دسترسی بمونی، از قبل
VIP
تهیه کن و خیالت راحت باشه.
🚀
سرویس نامحدود با قیمت فوق‌العاده
😍
قیمتش حتی از
پاکت هم کمتره!
⏳
ظرفیت VIP محدوده
و ممکنه سریع تکمیل بشه.
❤️
برای خرید و فعال‌سازی
👇
👇
❤️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/146909" target="_blank">📅 18:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146908">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2f8a98470.mp4?token=GAjZUFjHmXXqF_KRrNhJNDcvowLqTHO8EHfuknRMd0gsXW-5GkSTxfzci_g3Cq6snjd3TSXCyQv6w5B6x3rcPJqvPiqQHLlYmG5cHK7TTIKPyzLzHVuIf4eb_U__51Qvgcs5H2TF8SLKJW8oiCNbor98opuvZ9MwEdXzYRnG6CrTzTFmkIRvpt1TaZx3-vlY7J-33Nou_bYvyAh0eD1AjAcYHFyVsGX7LMcth6dBIRUUC_iZSBUowjAKMMv2LucMs2K3Tqjb10kgYDANlQ16GtG3eDePNc-wEaV3ub1K-aNhfk0sGSz6qEH3fWYH-V_XY6Pa6hjjhfRG6r_oKAvLvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2f8a98470.mp4?token=GAjZUFjHmXXqF_KRrNhJNDcvowLqTHO8EHfuknRMd0gsXW-5GkSTxfzci_g3Cq6snjd3TSXCyQv6w5B6x3rcPJqvPiqQHLlYmG5cHK7TTIKPyzLzHVuIf4eb_U__51Qvgcs5H2TF8SLKJW8oiCNbor98opuvZ9MwEdXzYRnG6CrTzTFmkIRvpt1TaZx3-vlY7J-33Nou_bYvyAh0eD1AjAcYHFyVsGX7LMcth6dBIRUUC_iZSBUowjAKMMv2LucMs2K3Tqjb10kgYDANlQ16GtG3eDePNc-wEaV3ub1K-aNhfk0sGSz6qEH3fWYH-V_XY6Pa6hjjhfRG6r_oKAvLvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر هگست:
تاریخ به پایان نرسیده بود؛ هیچ‌وقت هم به پایان نمی‌رسه. مبارزه با شر ادامه داشت و الان هم ادامه داره.
🔴
و این مبارزه تا روز قیامت ادامه خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/146908" target="_blank">📅 18:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06eee79e79.mp4?token=CRXzeH_5tUbFwbn39h_w3Zt8rSPjWBk-MpR91mHa9S6DPqqQMafgguh3RboJn08qkYt4LYuhVBiiWdt6yOJbY2pCOA6C6yC_XGBwKI0bZ56m8JzlzMH39k92-1e5OrYjmO7BwztynqwDOZuvgHTWDwTGmzYt_X_w2GETufz6mYYGuSpMndrONkR5dI1_lrZv4j7tjoqzGEwbvzFBVRuSBAgq37y6W8wH19bdNyuhjw1-q7K364SFcOjX2ucL6mB0xSWlbFJ-3nE82bcQi2pRNNqAYhYq6isvhsyona6c9vUIbvVuAlIldTppCADWdCplpCbKgCEAGXgh34X3W-EXng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06eee79e79.mp4?token=CRXzeH_5tUbFwbn39h_w3Zt8rSPjWBk-MpR91mHa9S6DPqqQMafgguh3RboJn08qkYt4LYuhVBiiWdt6yOJbY2pCOA6C6yC_XGBwKI0bZ56m8JzlzMH39k92-1e5OrYjmO7BwztynqwDOZuvgHTWDwTGmzYt_X_w2GETufz6mYYGuSpMndrONkR5dI1_lrZv4j7tjoqzGEwbvzFBVRuSBAgq37y6W8wH19bdNyuhjw1-q7K364SFcOjX2ucL6mB0xSWlbFJ-3nE82bcQi2pRNNqAYhYq6isvhsyona6c9vUIbvVuAlIldTppCADWdCplpCbKgCEAGXgh34X3W-EXng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
هگست درباره ایران:
تنگه را ما کنترل می‌کنیم و این نبرد را نیز تمام خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/146907" target="_blank">📅 18:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4eb98a5d.mp4?token=gU6G_XvJmcRxUcDpHLL3AgpXS7eHmQN3jH2aETOiC8guK2tO2H3LVML8Gh-L-9RjF4OOaTBb5x9gNeETuAyz0lVx9HJjFdsyqY0tpElukB02jDl1-dgFiwCRbh1RWoj1gt-pLEytEDPiij_uXg7WX8W2lD31whpwei5mb_scbdT3iOCgLjn4AQwOQ_Yb4ngDiUCGpj5jtZKFfT4yShROV7BJXgBnYEC0wUVZErUFOyv6rym4Z6o6RcXJVzDTdwIGgD-YeRG19gvn8GkRIGnf_EKLza3nvWM-Dy7i5ogmpAK8Y9KzYGQz6in16goqZgiCuVMEYbwTQDBe10KGIexvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4eb98a5d.mp4?token=gU6G_XvJmcRxUcDpHLL3AgpXS7eHmQN3jH2aETOiC8guK2tO2H3LVML8Gh-L-9RjF4OOaTBb5x9gNeETuAyz0lVx9HJjFdsyqY0tpElukB02jDl1-dgFiwCRbh1RWoj1gt-pLEytEDPiij_uXg7WX8W2lD31whpwei5mb_scbdT3iOCgLjn4AQwOQ_Yb4ngDiUCGpj5jtZKFfT4yShROV7BJXgBnYEC0wUVZErUFOyv6rym4Z6o6RcXJVzDTdwIGgD-YeRG19gvn8GkRIGnf_EKLza3nvWM-Dy7i5ogmpAK8Y9KzYGQz6in16goqZgiCuVMEYbwTQDBe10KGIexvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما هیچ‌وقت، هیچ‌وقت فراموش نخواهیم کرد.
🔴
به همین دلیله که ما امروز می‌جنگیم. ما انتخاب دیگه‌ای نداریم
🔴
تنها چیزی که می‌تونه وجود داشته باشه، پیروزیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/146906" target="_blank">📅 18:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dd01ae09.mp4?token=pJk0fS2w8AF5xrQJB7VqNqDDxUMXHXRp4H6_7FmROKoZXvDAkA7YIk5o88_N5TnPfpgNPeaHJ-NF26hUroV-irsrroJcso4yfEsfC6VdkzdtObWWxuT8NnaWS8j4LzRhB0cIJpTrdhANDTcSSnxW_hQSAZMd1wTnOFLqEKjzSMtRetWlfgeSooRUT5I-6u1mLMuIdpTIJVVxaRfGfE68c9iytGQCptRxV8YnlEcUAl3AEZFQhc8vkof21wkcKa6rUVuTNmZ-w8LJjVcAqeOk-xb3Zqaxc4W4MM3S7TJaE7MqiC79PMAQUAq1DH3axZf2uWWWMUAuLqvVjh8CO98no7QS6RBSfEWG9XGQWclgQhKdFC2e3fTiJ7r6xPGTFoCOkZLffZPDCp8cP85z5y2zSR6GMdBCHcs8XrOh9EVy1_TBNJxpYY3zSYWdJpKyZ8h-FgeylK--YSAmch8RSBQbt-U--M4KpVDCE-DQq68WAO9qzj2kB0Eu_OVAs5aTg3UGZHALXV12qRFy-4Vf7JPGjB-CbWc3rPmCOpWFCIrRl17Gcs1Lkt6USFAzuZxPrm-Rp4JKl2k7VTLLJRJmiTL5rjyBvZCIDHNxrTuBTzasXlsIIwCwojAnCwY2208cGjV1NBBK4docEnZY5-0zR3L9vrLDYDYBKoAtvz24EQAhRIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dd01ae09.mp4?token=pJk0fS2w8AF5xrQJB7VqNqDDxUMXHXRp4H6_7FmROKoZXvDAkA7YIk5o88_N5TnPfpgNPeaHJ-NF26hUroV-irsrroJcso4yfEsfC6VdkzdtObWWxuT8NnaWS8j4LzRhB0cIJpTrdhANDTcSSnxW_hQSAZMd1wTnOFLqEKjzSMtRetWlfgeSooRUT5I-6u1mLMuIdpTIJVVxaRfGfE68c9iytGQCptRxV8YnlEcUAl3AEZFQhc8vkof21wkcKa6rUVuTNmZ-w8LJjVcAqeOk-xb3Zqaxc4W4MM3S7TJaE7MqiC79PMAQUAq1DH3axZf2uWWWMUAuLqvVjh8CO98no7QS6RBSfEWG9XGQWclgQhKdFC2e3fTiJ7r6xPGTFoCOkZLffZPDCp8cP85z5y2zSR6GMdBCHcs8XrOh9EVy1_TBNJxpYY3zSYWdJpKyZ8h-FgeylK--YSAmch8RSBQbt-U--M4KpVDCE-DQq68WAO9qzj2kB0Eu_OVAs5aTg3UGZHALXV12qRFy-4Vf7JPGjB-CbWc3rPmCOpWFCIrRl17Gcs1Lkt6USFAzuZxPrm-Rp4JKl2k7VTLLJRJmiTL5rjyBvZCIDHNxrTuBTzasXlsIIwCwojAnCwY2208cGjV1NBBK4docEnZY5-0zR3L9vrLDYDYBKoAtvz24EQAhRIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ از ارتش آمریکا تقدیر کرد، اما هیچ اشاره‌ای به نیروهای کشورهای دیگر عضو ناتو که پس از حملات یازدهم سپتامبر در کنار آمریکا جنگیدند، نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/146905" target="_blank">📅 18:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146904">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: ایران بزرگترین حامی دولتی تروریسم در جهان است و هرگز به سلاح هسته‌ای نخواهد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/146904" target="_blank">📅 17:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146903">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e991788b.mp4?token=a7ch57Umu53k2-spBKMNkur1Ci_vnu2Lq1_1jlhf11r8YQD2XTR9l8vxGuplPT0YwC4YfAwkDOvwFoi097S2ORwofL-UqBMA6t_Sdh1EkjO5il3Bd11XiCYYbgHfgtWhTKWzGr-ToxK-kkwEr2YOvLeYJawT1qMcauQ4Wifa3xuNPME6Sic5bJL39FLzYP7hm7HaOVlQtHT6R54hKUb_81ys_2BurIi_j5OIEPOPNU6t7jmmk-B6Hf1sVQPAGinw0W0Clb5bTn2eqzcv42rZaOsI3H4SBv49941xQVpAGbVQR6DGLCPlu2lkzBKWRd4JqiXhrc-rME9WIahR2Sm-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e991788b.mp4?token=a7ch57Umu53k2-spBKMNkur1Ci_vnu2Lq1_1jlhf11r8YQD2XTR9l8vxGuplPT0YwC4YfAwkDOvwFoi097S2ORwofL-UqBMA6t_Sdh1EkjO5il3Bd11XiCYYbgHfgtWhTKWzGr-ToxK-kkwEr2YOvLeYJawT1qMcauQ4Wifa3xuNPME6Sic5bJL39FLzYP7hm7HaOVlQtHT6R54hKUb_81ys_2BurIi_j5OIEPOPNU6t7jmmk-B6Hf1sVQPAGinw0W0Clb5bTn2eqzcv42rZaOsI3H4SBv49941xQVpAGbVQR6DGLCPlu2lkzBKWRd4JqiXhrc-rME9WIahR2Sm-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره حادثه 11 سپتامبر:
ما همیشه قربانیان و خانواده‌های آن‌ها را که در حادثه 11 سپتامبر سال 2001 جان خود را از دست دادند، به یاد خواهیم داشت. متاسفانه، این یک تاریخ بسیار مشهور است.
🔴
آن روز، در ابتدا، روزی بسیار زیبا به نظر می‌رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/146903" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146902">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=jpgCMU_p7DaMJ0EG1JkZsKtC80tQWqEkXXXE4xozCBS9zeqBg1nAtcoxqwHEg2lXlpADVWM9wFJ3l4x1qemEUqyJ1UH71nKcIIhhOj-eFpEHH8rdT0IVSl8YRA9YLkzaaZOYUnnkjoEqnXJbX6t8z_GTaSljiwwkiNcNSAojDX6Ph9U7fZqBAfkW0_cVnVYA8h_hqq4L9R_BoxlkeZ6Y-S3saa4oLrvIr0qu6oEbqTDyvmVw16Gv6hx5_fNTdTexdOqwe2CuyoRQIc1LD48JZboKA6-9NIcpy7JXCFS50pjZRxLk-0-Fpv8X53OYLazsl3xuYC-ye3lH5qILK09feA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=jpgCMU_p7DaMJ0EG1JkZsKtC80tQWqEkXXXE4xozCBS9zeqBg1nAtcoxqwHEg2lXlpADVWM9wFJ3l4x1qemEUqyJ1UH71nKcIIhhOj-eFpEHH8rdT0IVSl8YRA9YLkzaaZOYUnnkjoEqnXJbX6t8z_GTaSljiwwkiNcNSAojDX6Ph9U7fZqBAfkW0_cVnVYA8h_hqq4L9R_BoxlkeZ6Y-S3saa4oLrvIr0qu6oEbqTDyvmVw16Gv6hx5_fNTdTexdOqwe2CuyoRQIc1LD48JZboKA6-9NIcpy7JXCFS50pjZRxLk-0-Fpv8X53OYLazsl3xuYC-ye3lH5qILK09feA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، حملات 11 سپتامبر را با جنگ خود علیه ایران مرتبط دانست: ما هرگز این واقعه را فراموش نخواهیم کرد. به همین دلیل است که امروز می‌جنگیم.
🔴
ما هیچ انتخابی نداریم. تنها نتیجه ممکن، پیروزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/146902" target="_blank">📅 17:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146901">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU6XvKQvy3yM8lqW01chd8GronMwizD0oUwKTQ-kr-JOMR_p2Cy9ottk_eTHuFjQtC2Z0WHdSC91BROCkfZ0K05xA50hVFBq_z_qIfqBX0TKWrS2b1ZX_VcOaTB8pManw5rXVTxA_bd5UPz0285ztCMRyhvHPnH9IyPcuSBw2vWvTZK8tTxC3tXkbat8N2G_ceKRHv8YgSaQPczDbI4eWG7vOX9WYp1Zqt1CGWXRQWMHmCSd5SFnjOX0LW8V9anUT4-7_bkp99_yySe9WKFHLGUn-j2zYyLA-AdcDL3EI40VUJ1mvacr4Tir0k2hT2MnKU7re-tEbxp1bauR4R75FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:  اخیرا محسن رضایی از عاصم منیر گلایه کرده که چرا صرفا طرفِ ترامپ بوده و از نقشِ میانجیگر خارج شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/146901" target="_blank">📅 17:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146900">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس جمهور اوکراین از حملات شدید پهپادی به تأسیسات نفتی روسیه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/146900" target="_blank">📅 17:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146899">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e35d7d19.mp4?token=IzP1Q8-tfNA9c1nXZsgWvC8OwO5aaMheXtveYjjfdHJ3c7fwqhNZiYEh9d2FFugaBoebJRKCGuOhGTW1ZyAJLO3a6sDWZ_VL91rmHcbPULJnoHQq8X2WA2-gx8lDQXEO9f4xEPlPRWEK1Nk8VMsylxw46O8MyBksl2EXqH73J0Y33jcPk_8FeG_BYdYh_wM8UmFqJ7UyrZxxqNq-FdPcDE6kyteEDuc6_luDCDhbct71G3vQ5-gYc61G_G3WtsJYGfibfoO-G3D4U3dJgpvDEd0BkxT69xGWnVg7BsX5HHJHP3-boU2ZP_BEP57kREsxR9GAjcp64UlvUOUAyLyYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e35d7d19.mp4?token=IzP1Q8-tfNA9c1nXZsgWvC8OwO5aaMheXtveYjjfdHJ3c7fwqhNZiYEh9d2FFugaBoebJRKCGuOhGTW1ZyAJLO3a6sDWZ_VL91rmHcbPULJnoHQq8X2WA2-gx8lDQXEO9f4xEPlPRWEK1Nk8VMsylxw46O8MyBksl2EXqH73J0Y33jcPk_8FeG_BYdYh_wM8UmFqJ7UyrZxxqNq-FdPcDE6kyteEDuc6_luDCDhbct71G3vQ5-gYc61G_G3WtsJYGfibfoO-G3D4U3dJgpvDEd0BkxT69xGWnVg7BsX5HHJHP3-boU2ZP_BEP57kREsxR9GAjcp64UlvUOUAyLyYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: طی پنج سال گذشته، بیش از ۴۰ درصد تولید ناخالص داخلی جهان توسط کشورهای عضو بریکس بوده است
🔴
در حالی که سهم گروه موسوم به «هفت بزرگ»، نمی‌دانم چرا به آن «بزرگ» می‌گویند، تنها ۲۹ درصد بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/146899" target="_blank">📅 17:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146898">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=q3ZAhzzxC1XxHJebpIMN1Y1U7KYcrZufUZKj_4LWDpxuq_czqptQwJbB62vej80J7hmArdhJNPcr_6DP0ripCdWuPMsu4F1i3Ay9QqbJ9qHUnrW7QdYyqUFpEGsUPUDjnW-NB5uzHHURN0cpoUSQF0K3EA_oaoI1XU5KDtbv3ITlDxazlct6qL2-zuzVB_C5ViKXeEInMVrxCPMJLEMo0AUeGfSo8J4U4AH_kCpmI8gSv3kR8Q9QTzev-UXPFwnAqIm9hb0z7FKEyqDLkb7nM27PF7ULv_a0fhuu7Ujtp3AMbYhbtTZbQeKq9VgdwHnrqtX79XaBf8iwV6VZVs-0-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7637eba24e.mp4?token=q3ZAhzzxC1XxHJebpIMN1Y1U7KYcrZufUZKj_4LWDpxuq_czqptQwJbB62vej80J7hmArdhJNPcr_6DP0ripCdWuPMsu4F1i3Ay9QqbJ9qHUnrW7QdYyqUFpEGsUPUDjnW-NB5uzHHURN0cpoUSQF0K3EA_oaoI1XU5KDtbv3ITlDxazlct6qL2-zuzVB_C5ViKXeEInMVrxCPMJLEMo0AUeGfSo8J4U4AH_kCpmI8gSv3kR8Q9QTzev-UXPFwnAqIm9hb0z7FKEyqDLkb7nM27PF7ULv_a0fhuu7Ujtp3AMbYhbtTZbQeKq9VgdwHnrqtX79XaBf8iwV6VZVs-0-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایرانی‌ها در تلاش‌اند تا در آمریکا مشکلات اقتصادی ایجاد کنند
🔴
اگر به حساب‌های کاربری ایرانی‌ها در توییتر نگاه کنید، می‌بینید آن‌ها تلاش می‌کنند در آمریکا مشکلات اقتصادی به وجود آورند؛ چه از طریق تغییر نرخ بازده اوراق قرضه و چه با دستکاری قیمت نفت.
🔴
رسانه‌هایی مثل بلومبرگ، فایننشال‌تایمز و وال‌استریت‌ژورنال تا حدی به «سندرم اختلال ترامپ» (حمله به سیاست‌های ترامپ) مبتلا شده‌اند که حاضرند به ایرانی‌ها تریبون بدهند تا علیه ما مانور بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146898" target="_blank">📅 17:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-zEWriLsWCd5So2cHiNgJM77oeWYEyuEEsB0_5AZ9UzZStgyR4wKQc9H5BVV0AFIigz_qiHl28ywIHpDNhicCirb9RhJBNQ6slBT9dQK_Q0iYveJKiFN9USpYVk09bqxdJForAhKRXk3U2Q-3w3gM4c-yxIYbFuVIQdYzB311T4qug1GTxBXu1XhlpXolMho4k3rsQxRl-F5Fh_9lwMSSXfwkx4ZGTB-K4JcMoa-YBu17hP8kQNsbZ-nXn7YwFX780BEzAHO-OV9pAUSqfE9c9ks9y2ZeAQlIi-ds9_Hq0rF4R3KzLTYeVTKonaNVuT3vyzprc8OgLDE68zoHhyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان با نخست‌وزیر هند دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/146897" target="_blank">📅 17:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت امور خارجه : ما روز دوشنبه، با همکاری عراق و کشورهای خلیج فارس، نشستی در مورد تنگه هرمز در عمان برگزار خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/146896" target="_blank">📅 17:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146895">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
امام‌جمعه یاسوج: اقا مجتبی روزی ۱۰ ساعت فعالیت داره، تو ختم پدرش هم حضور داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/146895" target="_blank">📅 17:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146894">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d562e33a76.mp4?token=tGZpsbGxb-AzgbdGnYPgCoWDwLzeFrWhdHekPo_8VDRDbiLIo4InWXo9WTDAa91tQdHS27c0jMqEp2Nv5W13QfsMVfWy8VQa0mgqelM1o4AQXzEiIVc79jCOhz7S6e2rBYdbrHjVdGFdirxzIlCLisF1h9X03TrVhj7kROnraCUuL_zzWbjIQINKzxL0YfsQX2l8rIwtWzYQ99HqhfZFY9LqxcjOZ_E6BeSv4aDNEaCmSPO2PeO8_7tnjYGE9cXljvCvNDIThIYSZndwW1Cp1K8Ei6HEtLyobvS-1gccBBjuyFLvB_d3KS45SIsfjUF9rAkil_0qzgx3cymCaGXSzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d562e33a76.mp4?token=tGZpsbGxb-AzgbdGnYPgCoWDwLzeFrWhdHekPo_8VDRDbiLIo4InWXo9WTDAa91tQdHS27c0jMqEp2Nv5W13QfsMVfWy8VQa0mgqelM1o4AQXzEiIVc79jCOhz7S6e2rBYdbrHjVdGFdirxzIlCLisF1h9X03TrVhj7kROnraCUuL_zzWbjIQINKzxL0YfsQX2l8rIwtWzYQ99HqhfZFY9LqxcjOZ_E6BeSv4aDNEaCmSPO2PeO8_7tnjYGE9cXljvCvNDIThIYSZndwW1Cp1K8Ei6HEtLyobvS-1gccBBjuyFLvB_d3KS45SIsfjUF9rAkil_0qzgx3cymCaGXSzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ا
سکات
بسنت: ایرانیها، اگر به حساب‌های کاربری آن‌ها در شبکه X نگاه کنید، تلاش می‌کنند مشکلات اقتصادی در ایالات متحده ایجاد کنند، یا با دستکاری در نرخ بازده اوراق قرضه، یا با دستکاری در قیمت نفت.
🔴
و می‌دانید، صرف اینکه رسانه‌هایی مانند استیفانی، بلومبرگ، فایننشال تایمز، و حتی وال استریت ژورنال، به شدت تحت تاثیر "سندرم اختلال ناشی از ترامپ" هستند، آن‌ها می‌خواهند به ایران‌ها بستری برای فعالیت بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/146894" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146893">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03112531a9.mp4?token=U79zsmzK2-k_jRVkIpZ4FSjL0amuPNxIV2xOHvfddhQ4FKOrmiB6mvrFy6L5RZ5TIBILdeddTD3LW2ffmbgJDR8tPSK9Ma_DSV7mORGSpYTu5IanB1chLNU8cy7eTIR0iVCZeDGGYFos09t3qu5T_EMy5uxCwUki2jjnKGVHFYOMSarVLlUTH_vHvQ6Mzt7vlpUmo_ny6Fyqs2UY3inY1TcaS7texNGq2w_RXoTMCdPGERnv9WC0X23IzEVlXSDupHpu05g4fRd0csDLO2UJvPCOSN2pKjn5WTBoHXMlNZLuAHLgT1yyjKL4KtUoYvM0w0eIzDp3F-8rG12g04VeXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03112531a9.mp4?token=U79zsmzK2-k_jRVkIpZ4FSjL0amuPNxIV2xOHvfddhQ4FKOrmiB6mvrFy6L5RZ5TIBILdeddTD3LW2ffmbgJDR8tPSK9Ma_DSV7mORGSpYTu5IanB1chLNU8cy7eTIR0iVCZeDGGYFos09t3qu5T_EMy5uxCwUki2jjnKGVHFYOMSarVLlUTH_vHvQ6Mzt7vlpUmo_ny6Fyqs2UY3inY1TcaS7texNGq2w_RXoTMCdPGERnv9WC0X23IzEVlXSDupHpu05g4fRd0csDLO2UJvPCOSN2pKjn5WTBoHXMlNZLuAHLgT1yyjKL4KtUoYvM0w0eIzDp3F-8rG12g04VeXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: استفاده از ارزهای ملی در تجارت بین اعضای بریکس باید توسعه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146893" target="_blank">📅 16:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146892">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDbdxI4_70D2lWmDWw6GAIAMfDZEQ0oiU2fESrz-kJCBd1ChdGH6ipmdybdRWDk6GexwiKsNGUmXmdkQ_lNXUaZqAzPUaHk1-zdwQVQQxWimYWSr5dr7hYjoeiWOCt47Tzg7FvNJb4LsyjdHLzeFTPPhRqAg8EvgJ54Y3rstxo1QZfhuELAZoOWrRUk8tzTu3qkfDvk_LsKhoXdFP9DAGN972MoG-ETniIbv7kl2FXTpYs7jC0KgT-EpgLTe3NZIo9UuOo7iHYwrjfSfr791_zhZi0tsnMJL2c3McOGJR0dAJtDKlZ1gQQ93J6rn0p4KbLijj6nDl6CsWvuWqAjkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: وزیر خزانه‌داری آمریکا با خوشحالی به خود می‌بالد که می‌خواهد ایرانیان را فقیر کند و اقتصاد ما را به فروپاشی بکشاند. اما در عوض، او درمانده و ناتوان در برابر افکار عمومی قرار گرفته است؛ در حالی که جهان روزبه‌روز اعتماد خود را به نظام مالی آمریکا بیشتر از دست می‌دهد.
🔴
بحران ناشی از هزینه تأمین مالی بدهی‌های آمریکا تنها آغاز ماجراست
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/146892" target="_blank">📅 16:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پوتین: کشورهایی که فشار تحریم را علیه روسیه و ایران آغاز کردند خودشان با افت صنعتی و کسری بودجه روبرو شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/146891" target="_blank">📅 16:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cac53a8e4.mp4?token=N4hacsl-8hZ6jNdjZB6OQwwrAHKW6n2bcUanSNUoH_hqfbJ6ExVPoKULgjD3IS_TX3fBi61jt3bZwsCtPjAs-XrkYeAsQ5H4VIhOeNCSMGGdiSVpWqRuRYmzH-Rrpy1_yq2nZT3TUkNuFvaQ6H4zL0GMieBvifLdF162baJUn-e_Y8zTRkYJJnnDu8bNOq04Ej5d2VF7TNoZgZeUcxyP40P4MBu4xE2syF8xkDpEiQbtCeNmfioCaMKgbFPSZ-GRt1z2p9OjGly3I6ap6gVLnrgN0_oDaPnADRjKZl-IS2b8eLfaUwb247k1rXtJR4TkBfI3YDxa9qkRpQEC4wxGS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cac53a8e4.mp4?token=N4hacsl-8hZ6jNdjZB6OQwwrAHKW6n2bcUanSNUoH_hqfbJ6ExVPoKULgjD3IS_TX3fBi61jt3bZwsCtPjAs-XrkYeAsQ5H4VIhOeNCSMGGdiSVpWqRuRYmzH-Rrpy1_yq2nZT3TUkNuFvaQ6H4zL0GMieBvifLdF162baJUn-e_Y8zTRkYJJnnDu8bNOq04Ej5d2VF7TNoZgZeUcxyP40P4MBu4xE2syF8xkDpEiQbtCeNmfioCaMKgbFPSZ-GRt1z2p9OjGly3I6ap6gVLnrgN0_oDaPnADRjKZl-IS2b8eLfaUwb247k1rXtJR4TkBfI3YDxa9qkRpQEC4wxGS4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ما نفت صادر می‌کنیم، ایرانی‌ها صفر؛ نتیجه ۱۴۰ میلیارد به صفر به نفع ماست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/146890" target="_blank">📅 16:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146889">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fe8f52d9.mp4?token=nB8ukwdpAloy1WmjOx8XZstGqT_3trzE6q4E4RzGA_TSOUxpdAdbH5Lc7eHKyeI2a7_e3AXnLg3k6XiPwAzan-2P40jgKoAdnOD9vNQNtfuIi1Kjjjmq1UrL4X5GIvAeFQEftmFdJDMk6jvo8HKwaqaZUixsxPWOeS8Dak75yLpnjZKCHWdhX5Fb_6yDJF56-AIGgK5_q8zTbCKLY6qmY8ORZPQ1PWV76MArn2FfTkY3_UJ7Hcjlq2EJ1Mb-RkMvAlz4Mkab2nXXPBHV8L41-OSMdGNDalGNc6v-Jnzmyu1LbvIRjjQO8Xknl3EDZ_KC2E7Zb5Yes2n1-eXbMzkOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fe8f52d9.mp4?token=nB8ukwdpAloy1WmjOx8XZstGqT_3trzE6q4E4RzGA_TSOUxpdAdbH5Lc7eHKyeI2a7_e3AXnLg3k6XiPwAzan-2P40jgKoAdnOD9vNQNtfuIi1Kjjjmq1UrL4X5GIvAeFQEftmFdJDMk6jvo8HKwaqaZUixsxPWOeS8Dak75yLpnjZKCHWdhX5Fb_6yDJF56-AIGgK5_q8zTbCKLY6qmY8ORZPQ1PWV76MArn2FfTkY3_UJ7Hcjlq2EJ1Mb-RkMvAlz4Mkab2nXXPBHV8L41-OSMdGNDalGNc6v-Jnzmyu1LbvIRjjQO8Xknl3EDZ_KC2E7Zb5Yes2n1-eXbMzkOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت: هر آنچه که ایرانی‌ها می‌گویند، بیشتر یا بخش زیادی از آن، ریشه در خیال‌پردازی دارد.
🔴
بسیاری از این حرف‌ها، آرزوهای دست‌نیافتنی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/146889" target="_blank">📅 16:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146888">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1144f5e406.mp4?token=o9rjquLW98pS16BruycVN5F0TZQVF8Gl55mVsFmbVSgiGh8O-JkKBx9miIvYH_dnOLBDAN_MKZ8jUfPLF0rwDdPKFXbGhX9tTB5uGrEwjOON-NS1-QkbfvC4qXG92j8p7KxnhYK0oj2VGbmIL1hddMG-Iivm9TOtDb1OzIl8IpmVBzutP0am02ac1FDXoKd0xvplecDdR0klsCwNNSGRx7eBDvgRFimrZHG22njobVD1_WvWy2DdltbIqQ3vzlguYDSghqy6pF509MrlhZk-nZKA6m1rnsxeXdEJsXpQrQg7G7m2mqi5KTAC4Ze4SRxnAiKfVaFfMlH7ovrg2ah4OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1144f5e406.mp4?token=o9rjquLW98pS16BruycVN5F0TZQVF8Gl55mVsFmbVSgiGh8O-JkKBx9miIvYH_dnOLBDAN_MKZ8jUfPLF0rwDdPKFXbGhX9tTB5uGrEwjOON-NS1-QkbfvC4qXG92j8p7KxnhYK0oj2VGbmIL1hddMG-Iivm9TOtDb1OzIl8IpmVBzutP0am02ac1FDXoKd0xvplecDdR0klsCwNNSGRx7eBDvgRFimrZHG22njobVD1_WvWy2DdltbIqQ3vzlguYDSghqy6pF509MrlhZk-nZKA6m1rnsxeXdEJsXpQrQg7G7m2mqi5KTAC4Ze4SRxnAiKfVaFfMlH7ovrg2ah4OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت: روزنامه وال استریت ژورنال گزارش داد که ایرانی‌ها در حال بازسازی ذخایر موشکی خود هستند.
🔴
شاید همینطور باشد، اما میزان و گستره این بازسازی چقدر است؟
🔴
ما ۸۵ درصد از کارخانه‌های آن‌ها را نابود کرده‌ایم. پس آیا آن‌ها هر هفته یک کارخانه جدید می‌سازند؟ آیا دو کارخانه می‌سازند؟
🔴
می‌دانید، این‌ها فقط تیترهای خبری هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146888" target="_blank">📅 16:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146887">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a99219ae2c.mp4?token=TrPEWQ_tcU6XYQrFkD90W4qzE0OagQHDZhCAyHH9cCugmPD-DwUr2HSFPlLvAF4P4me0J4mO1Kbb64ZoaMLDL6-w-Wyz8pyN_bxOzRZ_yj7CaKvggUTfvdIZVZUZ7Y2DWJ2SGdJUWNOhYPyfMoTtTe_qtNeu2cQZFUUeBml6_XU-RHCpYcv6vtuJAor5zsdvihfRShsGQyOl6Ve6RweVZ_UaGrSuIU35OnVhtHoMMb1a_enYSOg1C7McfTD61RP61nzE6cKo-hcLQaVRV8GtNVwoMzLsiqSBVUPIpFbGc-qU8CMVLUDX2WTHoJqRNB_JNsAKf_MgDvJrcqUyQ9R68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a99219ae2c.mp4?token=TrPEWQ_tcU6XYQrFkD90W4qzE0OagQHDZhCAyHH9cCugmPD-DwUr2HSFPlLvAF4P4me0J4mO1Kbb64ZoaMLDL6-w-Wyz8pyN_bxOzRZ_yj7CaKvggUTfvdIZVZUZ7Y2DWJ2SGdJUWNOhYPyfMoTtTe_qtNeu2cQZFUUeBml6_XU-RHCpYcv6vtuJAor5zsdvihfRShsGQyOl6Ve6RweVZ_UaGrSuIU35OnVhtHoMMb1a_enYSOg1C7McfTD61RP61nzE6cKo-hcLQaVRV8GtNVwoMzLsiqSBVUPIpFbGc-qU8CMVLUDX2WTHoJqRNB_JNsAKf_MgDvJrcqUyQ9R68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بریکس نباید صرفا مصرف کننده فناوری باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146887" target="_blank">📅 16:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146886">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان: ایران آماده است در کنار اعضای بریکس برای ساختن اقتصادی بازتر و عادلانه تر تلاش کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/146886" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146885">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29761d0702.mp4?token=grlYjGCUXfcmLHAGF7eIv02cuUv4S6RbiYMqO2TTVYEi9sfHoIKKy5ioQ76ymaDUlBHXt1wWqcanaHvDgYZSXx9jVw-raAWfOWNt5NMM5p6VBbx4-Z1KmHX5IehCyBbcxYstXoY8JTBwUhVG5WgWVNkJ6dzhiXdwcUw0Y5ckviRoqlrHpfKWwc2KJtHiU23ssvK5sNfNOp_FstSYOgqydJTHverK-PVbqwMG5mXP5fwmxItiKd2-J5V2xbApu9-672sgS2lYYiezrg1AkakPqoPSZtYUwXb3cHKvYPFQSj6dLNBIBjvIjyWQ3Vm3SJVZ3HM3Ixy1SUxYx__h7SC30w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29761d0702.mp4?token=grlYjGCUXfcmLHAGF7eIv02cuUv4S6RbiYMqO2TTVYEi9sfHoIKKy5ioQ76ymaDUlBHXt1wWqcanaHvDgYZSXx9jVw-raAWfOWNt5NMM5p6VBbx4-Z1KmHX5IehCyBbcxYstXoY8JTBwUhVG5WgWVNkJ6dzhiXdwcUw0Y5ckviRoqlrHpfKWwc2KJtHiU23ssvK5sNfNOp_FstSYOgqydJTHverK-PVbqwMG5mXP5fwmxItiKd2-J5V2xbApu9-672sgS2lYYiezrg1AkakPqoPSZtYUwXb3cHKvYPFQSj6dLNBIBjvIjyWQ3Vm3SJVZ3HM3Ixy1SUxYx__h7SC30w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: بریکس باید فضایی را ایجاد کند که هیچ کشوری نتواند تجارت مشروع کشورهای دیگر را مختل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/146885" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJ_iIRLfhD_CKtzFrXUA7qhcfFKhuDR9H8TKr4F0Yf-FjBLHRq9b2ovrNpYh1RLyViiqf_KI35sDgsjOevBvTqWfeCTZAZCF5Z-3wt5IdVJPFt73JjRRXVyocEAGKDw8ABXwYkmurETa2HtoBBln7sp_Kez6WLSjUDnBmaW-qmBk5tF4VS59sMCcuyRjMO7C9VUGLRIxXsLRz9L7xx6QAWKkY9EG8nD3-G78NUlAP69yABNGXeA1Fh61X_uqMsCpCCWVOVW2IExKzt3xPAxaxbEg8_sqWa-hjJP8Vs7rJ436JVM4e7dOJGaOMagWjZWsDBDq8FIleSxEbZ2FwWaJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان‌ملل با ۱۶۴ رأی موافق در برابر ۱ رأی مخالف تصویب کرد که نقشه مرکاتور کنار گذاشته شود و از نقشه "Equal Earth" استفاده شود که سایز واقعی کشورها را نشان می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146884" target="_blank">📅 16:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
علم‌الهدی: دشمن تا ۲۰۰ هزارسال هم بجنگه، باز دفاع میکنیم،‌ تسلیم نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/146883" target="_blank">📅 16:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5d711ee2.mp4?token=kS0oJBEdx5Iep5ekEYZHwUsuBO2Xmfe3CchZTLX_epmB2XpQWfdCAPYQUkB5gOj5iOykNjPiIN1cMilsQ8KfZmWXAnrKV-YzqZ2TwAgSX4BhXy5jGNKeohe6Wt6hDNugw_w1mPlziA_hPjlQ43tPtmJ7HvrL6LX13bwbuPK85lMktiYpC1ytkqrKsjVxA9KMPZBYhj8nYnwleEyHAsIcATiHIPfptQcr7I9Rx9j84jbH7w8YJoXe8e_fMxIXNDvO3KOMM2uDt0HRA5ObXH5EMKh10efE0nksd2nsbjiuD5ggPOxe3yC8IFxNsl07iiFI8Q8zb3-OKn6uMGc4hmortg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5d711ee2.mp4?token=kS0oJBEdx5Iep5ekEYZHwUsuBO2Xmfe3CchZTLX_epmB2XpQWfdCAPYQUkB5gOj5iOykNjPiIN1cMilsQ8KfZmWXAnrKV-YzqZ2TwAgSX4BhXy5jGNKeohe6Wt6hDNugw_w1mPlziA_hPjlQ43tPtmJ7HvrL6LX13bwbuPK85lMktiYpC1ytkqrKsjVxA9KMPZBYhj8nYnwleEyHAsIcATiHIPfptQcr7I9Rx9j84jbH7w8YJoXe8e_fMxIXNDvO3KOMM2uDt0HRA5ObXH5EMKh10efE0nksd2nsbjiuD5ggPOxe3yC8IFxNsl07iiFI8Q8zb3-OKn6uMGc4hmortg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عکس یادگاری سران بریکس در دهلی‌نو
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/146882" target="_blank">📅 15:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcf6775e9.mp4?token=fjs7Qm6xu7sE5Y7XW-7Hv9WL4lTH-GWJR2Mnt2mj6yPahI0tkI1G_VWNNv6zCM1YBiNKdJk7pT_DHXhrBqw8Eahl3qgRhRn-Op5KXh4abVFbMRZOWRXWacUlpn3YCZq8ib36EyA6eu36vsbex-8tw1e9RPW-HB3R-1GCcFVYNoDQ64kEblTx2xiDOtX1B8ep2JZ1ad3Fq8Pm0QdJehZ-H4sgyVbdieQSOzIp_d-hyoTf-lwqwNgsRC95GLG84bzWthA59icqitqIOqyR_HfVp9u3qN8rIbZOngbdHuYtE7roo2RTSaktDq7ofwLNkctjKEcJZ8z2v5ERXKIfFvoAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcf6775e9.mp4?token=fjs7Qm6xu7sE5Y7XW-7Hv9WL4lTH-GWJR2Mnt2mj6yPahI0tkI1G_VWNNv6zCM1YBiNKdJk7pT_DHXhrBqw8Eahl3qgRhRn-Op5KXh4abVFbMRZOWRXWacUlpn3YCZq8ib36EyA6eu36vsbex-8tw1e9RPW-HB3R-1GCcFVYNoDQ64kEblTx2xiDOtX1B8ep2JZ1ad3Fq8Pm0QdJehZ-H4sgyVbdieQSOzIp_d-hyoTf-lwqwNgsRC95GLG84bzWthA59icqitqIOqyR_HfVp9u3qN8rIbZOngbdHuYtE7roo2RTSaktDq7ofwLNkctjKEcJZ8z2v5ERXKIfFvoAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترکیه مرز بازرگانو به روی مردم ایران بسته و اجازه نمیده مسافرین ایرانی وارد ترکیه بشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/146881" target="_blank">📅 15:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت امور خارجه : گروسی گزارش‌های به اصطلاح بی‌طرفانه آژانس بین‌المللی انرژی اتمی را به ابزاری برای توجیه آغاز جنگ‌ها تبدیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/146880" target="_blank">📅 15:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REPpIp5andTEJDXkobcEm3Fj0DcObBNSyaP1Of1iouWu7bb2jcFudQpZJgDUj4BGz7UeVnlIBjSSoyT5O6a-KLDQTrdUqK2Iq87-2mPMaq37VglYBlWlT31ZdqBhzoV1OQUV-dMO4Dh3MkBl317O6bF-4lr9mgnGP9Rkn1zXfYY9jHNkNtEl_CGj-V9cUgs_JqtEl0-Fza-0XH9LK81Et5Uf1_q1KWIxRQ6j1BgmhswQxSL4SorExRHWg2GvseuMVcnugPaLkAUbdIse9vTeEBfVDFzVARnXhuOJjAhjP1BBdQGSUeSRMjFjt17JbHxatoRIXOTVwmuuBX9W9NjoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین انفجار در شهرک المنصوری در جنوب لبنان رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146879" target="_blank">📅 15:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فوری / وزیر جنگ اسرائیل: برای حمله به حزب‌الله در سراسر لبنان آماده ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146878" target="_blank">📅 15:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be2bebccb.mp4?token=EU-e2tpPOGP-8LOG9YFr9X0NewSzf783tWNVdTT2QvELibZQQCCcxoD2kDT7HYPN0urfEbxicfJ7vTRZ4r3ImIJ9gVqegncIYZdMtteNeDlaKu84AcPurokcV8VBMlfraHB2V7irUh7XPNvzUWzM_H1wwdXovihvGCe1rUI_x-yKmXhe83Ev3U11sCFpPWpgCQJW3IEL4S1-wJKggfHqc9ph3dEzxgHRcNHoC9u9Smd_WCLyjSTYVoqTBANIoEKXU_J3WlOD7blcL_hQ42L3ytWwtUroRjsHNvugMPFNKTlxzRrdLHpgtzWCg8iC_HaANDahdjZa8vEswOvUNqFB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be2bebccb.mp4?token=EU-e2tpPOGP-8LOG9YFr9X0NewSzf783tWNVdTT2QvELibZQQCCcxoD2kDT7HYPN0urfEbxicfJ7vTRZ4r3ImIJ9gVqegncIYZdMtteNeDlaKu84AcPurokcV8VBMlfraHB2V7irUh7XPNvzUWzM_H1wwdXovihvGCe1rUI_x-yKmXhe83Ev3U11sCFpPWpgCQJW3IEL4S1-wJKggfHqc9ph3dEzxgHRcNHoC9u9Smd_WCLyjSTYVoqTBANIoEKXU_J3WlOD7blcL_hQ42L3ytWwtUroRjsHNvugMPFNKTlxzRrdLHpgtzWCg8iC_HaANDahdjZa8vEswOvUNqFB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسموتریچ وزیر اقتصاد اسراییل : وقتی مردم ایران چیزی برای خوردن نداشته باشند دیگر چیزی برای از دست دادن ندارند و این باعث سقوط رژیم می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146877" target="_blank">📅 15:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146876">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLiu8l7Gg47h-OT6N37At5CR5o6BARf7jcm9tqdODRRk1ymLv9-KnIprAbXIB9ac_NKf0u2YmNBMZUdAx-T9vJ-DHgM55imjgC4VJ657LZcj9XUAPSYxTmt9MsqYw6CfFHjXZMkDs1L4OxFqK60M8Yv8O2sVBDNG9hu44e7GSB3iprAH5quR2R6XVAyYEFkbUKoGEX4cdJT9ZFTe4jOqbjoeXlyL9fN3XSwLdRTSiL_TJdKW1TBhA4SmWjZFkWxZSEf1Ds43CgV14adAstdJgN4RusUWLAQSk6T_mwlBhtLcOWm3q89wkuti-UaVCOCJ1iyLPGlAr_VU1z5VMuQg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای یمنی به شورای محلی منطقه "ذو باب" در نزدیکی تنگه باب المندب رسیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146876" target="_blank">📅 15:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
المیادین: امروز نیرو های تحت حمایت عربستان سعودی در استان البیضا، در جنوب یمن پیشروی گسترده ای داشتند و به ورودی های پایتخت این استان نزدیک شدند، دو استان الجوف در شمال یمن و البیضا در جنوب یمن در آستانه سقوط قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146875" target="_blank">📅 15:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
اتحادیه اروپا ۶.۱ میلیارد یورو دیگر به اوکراین اختصاص داد
🔴
اتحادیه اروپا اعلام کرده ۶.۱ میلیارد یورو اعتبار تازه برای تقویت توان دفاعی اوکراین اختصاص خواهد داد.
🔴
براساس این بیانیه، منابع جدید صرف خرید تجهیزات پدافند هوایی و موشکی، مهمات، پهپادها و سامانه‌های جنگ الکترونیک خواهد شد و خریدها از شرکت‌های مستقر در اتحادیه اروپا و اوکراین انجام می‌شود.
🔴
اورسولا فون‌درلاین، رئیس کمیسیون اروپا، گفته این تصمیم به کی‌یف امکان می‌دهد تجهیزات مورد نیاز خود، از جمله سامانه‌های پاتریوت، را برای حفاظت از حریم هوایی اوکراین تهیه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146874" target="_blank">📅 15:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fWYyb0FJ5YhRwM-VxMFA9Ut_Lz753GdsE8kUfI7oyhnglW9JNs3XMulcE1FaIQGctUjg1we7JbU0TrNveknb3gGEGWwp0ghtJ36oynrPztYfTIifLBVS10JRr8xtNLF-ecrtLyBSQHNrH1qe-63zGKLQAm4gW931NkRSljDmCO8y_GyicEWVz8phPRbLddD0rKfJI2qm5mZbCo2V3nrOIINQQme78DO_rsI7Q_93-g-buRWAwNPr6GzfHjULWG4UFrQcGOkAetu3zGM_Nccvk4tPH2OmmfzKyag6EOYPC9DQ-qRyRrb_DK9I8M6Er9oqmgB-N3AIwX7g-FZGGYS2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fWYyb0FJ5YhRwM-VxMFA9Ut_Lz753GdsE8kUfI7oyhnglW9JNs3XMulcE1FaIQGctUjg1we7JbU0TrNveknb3gGEGWwp0ghtJ36oynrPztYfTIifLBVS10JRr8xtNLF-ecrtLyBSQHNrH1qe-63zGKLQAm4gW931NkRSljDmCO8y_GyicEWVz8phPRbLddD0rKfJI2qm5mZbCo2V3nrOIINQQme78DO_rsI7Q_93-g-buRWAwNPr6GzfHjULWG4UFrQcGOkAetu3zGM_Nccvk4tPH2OmmfzKyag6EOYPC9DQ-qRyRrb_DK9I8M6Er9oqmgB-N3AIwX7g-FZGGYS2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا و سیما:
گازوئیل تو آمریکا ۵ سنت گرون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146873" target="_blank">📅 15:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5db101496.mp4?token=hHZ7U2x5cFHVLuyh-XoCGVhv8e7q6ElCNUq9SdjFWCFFEjfhf511Wtt2IXP7FrXjZ9jpulVkcJXxtlO_9U9F0bWXppLV1PWx_PbNbN-SvLlmZ3S5IBAOcg3Xs2NYWzwHOorkOinGmlf7GfCfWforF9L9_SIFb6vIL05V0tIIc7rOZzGupNU7frB71OxLs9GObcNF_WSyam7i5zTkH3UmIAl8kbRMc9TglaMa0L33-71zAiiBiInrwRq1Y7ON2VmE-D8jsMq-QCDNHfkFJXAEVhiZktA1faa3kVK7NQVH-08fPszfVYoG9fZAebIIkPXz7seRWsFikzHDgYx9eSPtp2lGTqC2_jMUp7OP21YOFCorcGu0lw9aJBPCOD6XGiZjzj9pxNAG-11wsVzgLzNX3YPfOH7Q8pybAfKUS-cxbawtlIrRvQBxHOnWKYLhMBi4exuM6BApo3NPtp98DMC3rJAOpJn83sbAWurfl0QtLIxpVP568ezHhCiW5J3itLOjx0OuEjp2dpcs-7PcZmBWfuQhdP_YwB9bXdDGzzHUbcq2rzpiVtEYn5lpCTZF9kOLmyMnU9rbtgLW1z5SqZOwpcPNaYx_v1ZvCAcjX03shgYFQ0ZvbUAYygRVlKd4ZV8S1KrF41gw55JQ3pfkbbSrRLqe44mtTyXCplqM15g903k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5db101496.mp4?token=hHZ7U2x5cFHVLuyh-XoCGVhv8e7q6ElCNUq9SdjFWCFFEjfhf511Wtt2IXP7FrXjZ9jpulVkcJXxtlO_9U9F0bWXppLV1PWx_PbNbN-SvLlmZ3S5IBAOcg3Xs2NYWzwHOorkOinGmlf7GfCfWforF9L9_SIFb6vIL05V0tIIc7rOZzGupNU7frB71OxLs9GObcNF_WSyam7i5zTkH3UmIAl8kbRMc9TglaMa0L33-71zAiiBiInrwRq1Y7ON2VmE-D8jsMq-QCDNHfkFJXAEVhiZktA1faa3kVK7NQVH-08fPszfVYoG9fZAebIIkPXz7seRWsFikzHDgYx9eSPtp2lGTqC2_jMUp7OP21YOFCorcGu0lw9aJBPCOD6XGiZjzj9pxNAG-11wsVzgLzNX3YPfOH7Q8pybAfKUS-cxbawtlIrRvQBxHOnWKYLhMBi4exuM6BApo3NPtp98DMC3rJAOpJn83sbAWurfl0QtLIxpVP568ezHhCiW5J3itLOjx0OuEjp2dpcs-7PcZmBWfuQhdP_YwB9bXdDGzzHUbcq2rzpiVtEYn5lpCTZF9kOLmyMnU9rbtgLW1z5SqZOwpcPNaYx_v1ZvCAcjX03shgYFQ0ZvbUAYygRVlKd4ZV8S1KrF41gw55JQ3pfkbbSrRLqe44mtTyXCplqM15g903k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از خودروهای متعلق به نیروهای سعودی و اماراتی که این نیروها در هنگام عقب‌نشینی خود به سمت شهرهای جنوبی، آن‌ها را رها کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146872" target="_blank">📅 15:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
خبرنگار صداوسیما: یک شهپاد آمریکا امروز توسط نیروی دریایی سپاه مورد اصابت قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146871" target="_blank">📅 14:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBPb8Rt6BD7YL6f-hRTYbYLW-JunmnxJrJaT05uxj_eZso9wCFfGoFjt-P45-zUj5ovh3KeZ0WBgRX-FXPR_4MHFiCuxTVcN4btln3iJXZw9hwN-GiZVl08Bl6BeTrX-bqcXFe44r9dJfm5fvLcst1_U84yNiM4ooBBRwpTSJf-vVUSQZ1EZS2DKR_GJ8lfyF_9-ovykyga-uw9Szd4uAnM4s9AgzDXV6sAYRUU6utaijuX63b1zfTOKbUmSA2C5LJRGVqsh7BC51Gf7BQpUq1ZXxGy0NntP8uEIYIDQ-QMrEvaD5RWJWyi7pm_v87ISX9rBHr-thivlfIpMRkwABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUy0O0tWLkKEUAFnA04JCp2q8y9N7bb3zQX29B8NNOXnKzWldtQMq8wMqcgj8COM-GCLOYm3wGr-_mGN-fsOP6b6wSRLwqrWG2bpHMXr6es6t8P4t68PMBGg_pYlsbulS35wOH9Ze9L2e4wpnWvbhQJYcXRqDtFd3ycIVGjGBAnxmDl8dXvQ62MzbEj0rs-UkFe83Lw3tvLyuZb1roFXVzD0w-wWUlS-1ahwVHORZgd7nZf0ZLAX__i7h8nGr3EmC2OtYQclN-HyxG-Nsj7yIjHo0veo_jUxOBA9g4KRRlRcuwmZg_bKfzfbmPyWoj7vdqstRU4nFxxiqVoOG-DG1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انفجارهای ناشی از عملیات اسرائیل همچنان در شهرک اشغالی المنصوری ادامه دارد و از بامداد تاکنون بیش از ۲۰ انفجار در این منطقه ثبت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/146869" target="_blank">📅 14:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146868">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faeb6ddc51.mp4?token=m11n1amkcNeAwpLQ5Sn8PcU7cePKhHKNMbRG8oE78PRJU_Dd7W6eni9J1rpAbswHsvvwRx_9xzNimfRAJZ_9XKzBr6Rw0vRNsEyqHsgN-uRMxMuRweFlgwDX3JR2UjQTHYgcotsUiUj2NCZQwlyt8L-52kgELUC9WwQvhzzauIT0eufy0Zxf88wpX2sDGHaXiPVE7LgejwBYViQzzu47XEt3ZHm1Zi6FiHfSfqJK8bLQaEkz0bF4XpRJNP52-DlciZcAK353WvhF8OFwXPfI0YBw5OlvuWKZLSAEl3rRSz3motfIaHlNd1ox-_EigVGU2KDYQ8HJQiWskXav5gqr5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faeb6ddc51.mp4?token=m11n1amkcNeAwpLQ5Sn8PcU7cePKhHKNMbRG8oE78PRJU_Dd7W6eni9J1rpAbswHsvvwRx_9xzNimfRAJZ_9XKzBr6Rw0vRNsEyqHsgN-uRMxMuRweFlgwDX3JR2UjQTHYgcotsUiUj2NCZQwlyt8L-52kgELUC9WwQvhzzauIT0eufy0Zxf88wpX2sDGHaXiPVE7LgejwBYViQzzu47XEt3ZHm1Zi6FiHfSfqJK8bLQaEkz0bF4XpRJNP52-DlciZcAK353WvhF8OFwXPfI0YBw5OlvuWKZLSAEl3rRSz3motfIaHlNd1ox-_EigVGU2KDYQ8HJQiWskXav5gqr5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین پیش از برگزاری نشست سران بریکس، با نارندرا مودی در دهلی‌نو دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/146868" target="_blank">📅 14:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146867">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اکسیوس: فرمانده سنتکام برای بررسی پیشروی‌های انصارالله به عربستان سفر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146867" target="_blank">📅 14:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146866">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGD6K2A_qB05pbUyd7ZPu-U71Bbb71zYTCBiTmge7IGrEd5BMmePSp511OFeeRMLQpUL5dKCnvkFMyJmJ43ckYEYgyJDgAoGhowWNqGN9_XWlNfx83-NI9t_hUVKC_TCC6yWeqwZj-rGDWLknxiYShj-Tp8Gmb2pQrXh2_PbneigJwLYOnI_d1h5WbspRM7_JmuUb3IZh3oX3BOefKxdYCu7irTmN6pdkwQGG9WMLpJqdfHyT-ZtxzJhqLFotUc0CHYyKCPmTNoO86kdSqCsyKsQVZCZsn_m0kv5yPOsXL1oWYVG-tiBPIsiR313pssNncOtVns9WqLv-Djd9JZJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به دلیل جنگ‌ های ایران و اوکراین تولید نفت خام ریاض و مسکو مجموعا در ماه گذشته حدود ۵.۵ میلیون بشکه در روز کمتر از ژانویه ثبت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146866" target="_blank">📅 14:22 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146865">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b97ba68995.mp4?token=QktY6uGqeRobWrD82S1zPOKj7H1K6sKCUUKkyI8ZE7FRR9I9yuF2ejeZpZlSgxKsYMPx4_F0ynDIsg-NAz5kgyFWADdSvngbiOBIbNcQ3EltyhCRXzix-ZIKwN-vehY-KSWpkuEE22yziHwREe6AhJy9slA8gnuUo0nEkK1f4M5QtjA4zkHjlwjmOuQHBLTh0goCBJsIcgnLFpPuvcm3z51OKSI8oM9yH48UANR784bu3S_LnM6FOms81fA6Ny4A_gsXm26ickq68L7cBht1T0A569zNfqIu312h2wO2V3L0KZmArpbhi1-lzzE6icSTVQk8WUz2G9PMQtdwEmRV4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b97ba68995.mp4?token=QktY6uGqeRobWrD82S1zPOKj7H1K6sKCUUKkyI8ZE7FRR9I9yuF2ejeZpZlSgxKsYMPx4_F0ynDIsg-NAz5kgyFWADdSvngbiOBIbNcQ3EltyhCRXzix-ZIKwN-vehY-KSWpkuEE22yziHwREe6AhJy9slA8gnuUo0nEkK1f4M5QtjA4zkHjlwjmOuQHBLTh0goCBJsIcgnLFpPuvcm3z51OKSI8oM9yH48UANR784bu3S_LnM6FOms81fA6Ny4A_gsXm26ickq68L7cBht1T0A569zNfqIu312h2wO2V3L0KZmArpbhi1-lzzE6icSTVQk8WUz2G9PMQtdwEmRV4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا نگرانی‌هایی در مورد این دارید که هوش مصنوعی ممکن است منجر به انقراض انسان شود؟
🔴
ترامپ: خیر، من هیچ نگرانی‌ای در این باره ندارم. نگرانی من این است که اگر ما در زمینه هوش مصنوعی پیروز نشویم، در موقعیت بسیار بدی قرار خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146865" target="_blank">📅 14:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146864">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ : لطفاً دست راست خود را بالا ببرید: «من به بزرگترین رئیس جمهور در تاریخ ایالات متحده، که ما را آنقدر دوست دارد که حتی نمی‌تواند نفس بکشد، تعهد می‌دهم که من با خانواده‌ام، با دوستانم، به هر شکلی که شده، این کار را انجام خواهم داد - مهم نیست که آیا ثبت نام کرده‌ام یا نه، من تمام تلاشم را خواهم کرد تا مانند آن‌ها تقلب کنم... من خواهم رفت و رأی خواهم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/146864" target="_blank">📅 14:18 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca989d528.mp4?token=AicuX37NC4mcoG2gj7TyfIcUVxGSPcHWimF4EcN-LzScGV5QpUrUeLN3ZuhKA2r9ovHorYUgf1KfwmFSPlwiQPSbERIW3ouWZGw6F73U6oTZMELiDk_YcagjX0lE7uACLKxqDIfi0DUrHO5egeugh2Eo-PRrHPnUD5A05b4F1Zfh3vG9_VLj_nWW9L7dg5vN1EKpmxZqXFUyClxoCd-wl8_ekeUnxfgc2bu9wpFyKVIhuY19HIQ13_5xNuu8BqguZX-Yh9wlN_z3q3y4bUc9upitEWuLvKE5IWxofMtT69xjh_fyey9ROCZ-UVTacVDyYRSERQYSlCth5qREUaGjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca989d528.mp4?token=AicuX37NC4mcoG2gj7TyfIcUVxGSPcHWimF4EcN-LzScGV5QpUrUeLN3ZuhKA2r9ovHorYUgf1KfwmFSPlwiQPSbERIW3ouWZGw6F73U6oTZMELiDk_YcagjX0lE7uACLKxqDIfi0DUrHO5egeugh2Eo-PRrHPnUD5A05b4F1Zfh3vG9_VLj_nWW9L7dg5vN1EKpmxZqXFUyClxoCd-wl8_ekeUnxfgc2bu9wpFyKVIhuY19HIQ13_5xNuu8BqguZX-Yh9wlN_z3q3y4bUc9upitEWuLvKE5IWxofMtT69xjh_fyey9ROCZ-UVTacVDyYRSERQYSlCth5qREUaGjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما تنگه را کنترل می‌کنیم. من آن را "تنگه ترامپ" می‌نامم
🔴
ما "تنگه ترامپ" را کنترل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146863" target="_blank">📅 14:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64134abd7d.mp4?token=aI01aiGeIoNlyqenuQVm_02r2LYJIhI96e5AyLuVcuFfDb9ULPaTpBSYkTujV1wRUixh5ssHufEiBoOFaelm8wMctxAgl4kenFm9hvJbWvsWMFGX6l8fVcDIrABCmheNvsfUXRS7KcyX3UJkhCMxbVIIECDcXNQDRXtzIL1qhSQyzGFORZevchTjNWVUW9gtTqAbUMLwsCG3YMLUPiX1btBxRIhdjTwokdh5VFGvGH8piAnkg6411sZRUzZVMHyfdQHMpou5pfbUAT2KoW8gwJ2qf6wWUuV6IajyJ5y42Gs21t1sZYdedemocTJg5-NFINIifZEfn7K4L2U8tnQEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64134abd7d.mp4?token=aI01aiGeIoNlyqenuQVm_02r2LYJIhI96e5AyLuVcuFfDb9ULPaTpBSYkTujV1wRUixh5ssHufEiBoOFaelm8wMctxAgl4kenFm9hvJbWvsWMFGX6l8fVcDIrABCmheNvsfUXRS7KcyX3UJkhCMxbVIIECDcXNQDRXtzIL1qhSQyzGFORZevchTjNWVUW9gtTqAbUMLwsCG3YMLUPiX1btBxRIhdjTwokdh5VFGvGH8piAnkg6411sZRUzZVMHyfdQHMpou5pfbUAT2KoW8gwJ2qf6wWUuV6IajyJ5y42Gs21t1sZYdedemocTJg5-NFINIifZEfn7K4L2U8tnQEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما کنترل منابع نفتی ونزوئلا را در دست گرفتیم - ۶۵ میلیارد بشکه نفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146862" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566fe0667f.mp4?token=lXp12xOEMGOoS0pada7iNmlRJJbfabMeEJOKy5tN7nGw0mncyMOfd44bPNYoyx3vAetwsTDW0tPMCy9h1hzzcnrs6buoatj5SgyjY0KXkwd2PFQG7-u_vyjQokjs3D2pjk4jutVzebRHBIL7REVpoN1KkfiABeFxmp1JP4L-KEewYGO5wDM5zRaRBfcTzExUws8glMj_szBGzi8eQyHfZlxLkyoC61Gc05IlHly9saoM-8AqWrE3fZrM0XM99yySosuD7tH6iSv1RcVdnoFuRFxWTopmQ7ae_rNpMpL30JlMiuCqYCsFzU2xJP1XNukAm70T9cv6jxdR6n_SQ5HOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566fe0667f.mp4?token=lXp12xOEMGOoS0pada7iNmlRJJbfabMeEJOKy5tN7nGw0mncyMOfd44bPNYoyx3vAetwsTDW0tPMCy9h1hzzcnrs6buoatj5SgyjY0KXkwd2PFQG7-u_vyjQokjs3D2pjk4jutVzebRHBIL7REVpoN1KkfiABeFxmp1JP4L-KEewYGO5wDM5zRaRBfcTzExUws8glMj_szBGzi8eQyHfZlxLkyoC61Gc05IlHly9saoM-8AqWrE3fZrM0XM99yySosuD7tH6iSv1RcVdnoFuRFxWTopmQ7ae_rNpMpL30JlMiuCqYCsFzU2xJP1XNukAm70T9cv6jxdR6n_SQ5HOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: شما می‌دانید چه اتفاقی می‌افتد اگر رای ندهید: شما به جهنم می‌روید.
🔴
من نمی‌خواهم این اتفاق برای شما بیفتد، پس لطفاً بروید و رای دهید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146861" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146860">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اکسیوس:فرمانده فرماندهی مرکزی ایالات متحده دیروز، پنجشنبه، به عربستان سعودی سفر کرد تا جلسات اضطراری درباره پیشرفت‌هایی که حوثی‌ها در یمن داشته‌اند، برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146860" target="_blank">📅 14:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146859">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، درباره ایران:
«در نهایت، ترامپ کاری را انجام داد که هیچ رئیس‌جمهوری پیش از او انجام نداده بود. ما در این کار، شانه‌به‌شانه یکدیگر پیش رفتیم.
🔴
او این کار را در شرایطی انجام داد که تنها ۴۰ درصد از مردم آمریکا از آن حمایت می‌کردند.
🔴
من سیاستمداران زیادی را نمی‌شناسم که حاضر باشند برخلاف پایگاه سیاسی خود عمل کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146859" target="_blank">📅 14:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebf8674ee4.mp4?token=TovOl9SlEXmUKuiBszxOFtMjrFymW45msc81w_UmJokIcEBuJv0BDSTWtOnOLnWs811qisV-s2IOVyOGSXkLMeaAVntClPBYroXAuZs8HYxX4fipZNtk5iHtEB3Edd97wVtTCMnQWWudq2MGCw-ryXwbiWhxXHtJW9KUE-cydH6upG9Aw97rggC8X8vFcJcEPMAWQ4dyP9AB7eTKDoA4XWKmaQ9RfK77s5HT5og7GPSn_AdCKqamjicuJvynWDtaUK5yF3crNOJ-J9jx6qkcEXOP-oeo_rH2GG9gPYL4J972y9PH6lf7SoLZ6NhYy648jv27nzCBaXW8-i2PniaMsnx6CaLYEWCzZWOvUhDOTMtOBDGJRmvwqa7cJA797FBgVcDkmpMF4dIyMF5Jnol-nq9q2naKrJkh4_4b23-Qc1CXh_vXK2ggDQh95z5bcp6OyjzliKASiK8AIYpdtu6kf-DHYO-OJDV_agqWBOAoO9d1k6TvFcO_oWyRDi1ct-CcT6Fkp6DTJLHl-vo4bBZvPQ5Gxy2BOd2HompUU-mkQs4Nh-xB66asai1aMYicfdaNd-lSH_-kmfGj7b64X2PYqnCl3Wf9rCRRoxOupnnOseDl43jPfS2itxo-MsymU4twKVZvWJ-xdnRRD34Bjoot__j6S-HVKZYhi4QGmOUoWts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebf8674ee4.mp4?token=TovOl9SlEXmUKuiBszxOFtMjrFymW45msc81w_UmJokIcEBuJv0BDSTWtOnOLnWs811qisV-s2IOVyOGSXkLMeaAVntClPBYroXAuZs8HYxX4fipZNtk5iHtEB3Edd97wVtTCMnQWWudq2MGCw-ryXwbiWhxXHtJW9KUE-cydH6upG9Aw97rggC8X8vFcJcEPMAWQ4dyP9AB7eTKDoA4XWKmaQ9RfK77s5HT5og7GPSn_AdCKqamjicuJvynWDtaUK5yF3crNOJ-J9jx6qkcEXOP-oeo_rH2GG9gPYL4J972y9PH6lf7SoLZ6NhYy648jv27nzCBaXW8-i2PniaMsnx6CaLYEWCzZWOvUhDOTMtOBDGJRmvwqa7cJA797FBgVcDkmpMF4dIyMF5Jnol-nq9q2naKrJkh4_4b23-Qc1CXh_vXK2ggDQh95z5bcp6OyjzliKASiK8AIYpdtu6kf-DHYO-OJDV_agqWBOAoO9d1k6TvFcO_oWyRDi1ct-CcT6Fkp6DTJLHl-vo4bBZvPQ5Gxy2BOd2HompUU-mkQs4Nh-xB66asai1aMYicfdaNd-lSH_-kmfGj7b64X2PYqnCl3Wf9rCRRoxOupnnOseDl43jPfS2itxo-MsymU4twKVZvWJ-xdnRRD34Bjoot__j6S-HVKZYhi4QGmOUoWts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، درباره ایران
:
«اگر ایران به ما حمله کند، ما به‌سادگی تمام تأسیسات انرژی آن را نابود خواهیم کرد؛ حتی تأسیسات داخلی.
🔴
نفت، گاز، پالایشگاه‌ها؛ ایران دیگر چیز زیادی ندارد، اما هرچه باقی مانده باشد.
این کار می‌تواند یک کشور را به فروپاشی بکشاند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/146858" target="_blank">📅 13:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ae746b81.mp4?token=FNOeic67WzFiIru0DCIVArcIcxkLLMYmLJu8G7GvDbhnv-onCv8anPId6A7-E-TSvh3OVNKuDoIGUZil8sEJxmguIrlKJWAJM2AhZeam7azX24wwx3GvSvr5lTDSepMQupYQ2q3cwmBxhRKCUViw0zfUXupXDYIjrDK8nrybl6izwQsLNjZlm1TjMQceeYjl6m9U5g14CIEAeB7iM6Gb7KbF3nBYO_jDRWnp4vMTtPbPhkX0pua2lCn9Qs6o6waEh9XOwkzhdglWxJkmXCkQhXNWuNEaCN1xm0qNia4finuyC8D0NoWiLWpnI07ETAfiwQtH3gilhBGLi27nWuOx3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ae746b81.mp4?token=FNOeic67WzFiIru0DCIVArcIcxkLLMYmLJu8G7GvDbhnv-onCv8anPId6A7-E-TSvh3OVNKuDoIGUZil8sEJxmguIrlKJWAJM2AhZeam7azX24wwx3GvSvr5lTDSepMQupYQ2q3cwmBxhRKCUViw0zfUXupXDYIjrDK8nrybl6izwQsLNjZlm1TjMQceeYjl6m9U5g14CIEAeB7iM6Gb7KbF3nBYO_jDRWnp4vMTtPbPhkX0pua2lCn9Qs6o6waEh9XOwkzhdglWxJkmXCkQhXNWuNEaCN1xm0qNia4finuyC8D0NoWiLWpnI07ETAfiwQtH3gilhBGLi27nWuOx3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل، درباره ایران: «ما تحت فشار نیستیم. ترامپ تمام زمان دنیا را در اختیار دارد و
ما هم تمام زمان دنیا را داریم
؛ این آنها هستند که تحت فشار قرار دارند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/146857" target="_blank">📅 13:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2c659dfc.mp4?token=r-Ehke8FTBtGccbw7dbYQOxV3HXNBpFKnWXOYHkvvTnzNC2gV7pKy9Q-eN0_xy8W9vuRaOaV1m81aoVpb4ydg3vlZ9PqDlOZ3xpvYQk9qsfbegNIWnk68eJYQQdChmmVx9EuGpBPd22-rIDYz1ygvfyEG6uFtXp60w_BYtOWxTBjuLAXCAOnv0wJ7TrUhOyCY-8A5-rxhnZCc7B7kSo40D_5j23cDckAaU55m7K2MTaYPa6bz3I6I5DqMOHx03X2sJwIX7D3sXEvJnX9Qv3gqYvPbl43vF4xXdYHIYh64xVahIF66Y2ujP50vagVIhIxZ5lZcf2sRkmjA1lyUCTXVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2c659dfc.mp4?token=r-Ehke8FTBtGccbw7dbYQOxV3HXNBpFKnWXOYHkvvTnzNC2gV7pKy9Q-eN0_xy8W9vuRaOaV1m81aoVpb4ydg3vlZ9PqDlOZ3xpvYQk9qsfbegNIWnk68eJYQQdChmmVx9EuGpBPd22-rIDYz1ygvfyEG6uFtXp60w_BYtOWxTBjuLAXCAOnv0wJ7TrUhOyCY-8A5-rxhnZCc7B7kSo40D_5j23cDckAaU55m7K2MTaYPa6bz3I6I5DqMOHx03X2sJwIX7D3sXEvJnX9Qv3gqYvPbl43vF4xXdYHIYh64xVahIF66Y2ujP50vagVIhIxZ5lZcf2sRkmjA1lyUCTXVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «هیچ زمینه و توجیهی برای زنده‌زنده سوزاندن خانواده‌ها وجود ندارد.
🔴
هیچ گلایه یا نارضایتی‌ای نمی‌تواند قتل عمدی افراد بی‌گناه را توجیه کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146856" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0f323683f.mp4?token=BGGELqsJMdokj0p5ttgKxWkyYSSfWGMSF-6hSbNI4yU9fnHoQLQLU87uRUyMQ4IJnp5jpgva-6cKXm1vlCJcEgvCudo-jokABX6uG8pOL3_D6CMX_ZZFETmm2Zy6dPVWH-0cV9qIzyboghSrTfvQapmIZK244RsEJTDVj-h4nQPHTjoeddMMdC96q14dJkSQbu9aL2hCkyZUtmGtGZjD9mX76Vq-TIJLqGJaQfdhf7Mb0YVf-tOOJ8m62yro1W5AaI25qjupMQ3qpYp6I9JLDrc_if5XNNOb-01BvVg10TMQfgg8EZCmxLjfwnRrpdoOzbzrN9ryfaKddzQkNovINA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0f323683f.mp4?token=BGGELqsJMdokj0p5ttgKxWkyYSSfWGMSF-6hSbNI4yU9fnHoQLQLU87uRUyMQ4IJnp5jpgva-6cKXm1vlCJcEgvCudo-jokABX6uG8pOL3_D6CMX_ZZFETmm2Zy6dPVWH-0cV9qIzyboghSrTfvQapmIZK244RsEJTDVj-h4nQPHTjoeddMMdC96q14dJkSQbu9aL2hCkyZUtmGtGZjD9mX76Vq-TIJLqGJaQfdhf7Mb0YVf-tOOJ8m62yro1W5AaI25qjupMQ3qpYp6I9JLDrc_if5XNNOb-01BvVg10TMQfgg8EZCmxLjfwnRrpdoOzbzrN9ryfaKddzQkNovINA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «در ۱۱ سپتامبر، آمریکا هدف شر مطلق قرار گرفت.
🔴
در ۷ اکتبر، اسرائیل بار دیگر هدف همین شر قرار گرفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/146855" target="_blank">📅 13:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
علم الهدی: اون ۴نفری که کنار خیابون ماشین بهشون زد شهید هستن(چون سمت ما هستن)
خدا:
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/146854" target="_blank">📅 13:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
نتانیاهو: مقادیر زیادی تسلیحات را که ایران برای حزب‌الله فرستاده بود از تپه علی الطاهر استخراج کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/146853" target="_blank">📅 13:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73948ccb6f.mp4?token=gPuL8OD8aP1gU8w4kqvGoI0pRMf9lVkIeYmslXm227jyQM3Zboj1PS4V1xEOmi0v7kZsZHSw7GAsjonZYe9VoCOn7LoEwvsV5tEvLHFDT0ZhzFUuLY6I1eFw3JzTNjlYczJZcSLFgebwNcksUnm_VJvK4qb-Fv_khuK5-VqHgwhdBfjeNfV-5hC8hRFMFtxSIPRj3PsvT3aVk7w7EorG-Zjc8HKP-hfAZbEBjWEMKUPN2CfSUioN3dpeCt7CMW5b1NkNig7EmmihZPN1pI0iOaz2jbdN69fy3GSR2JzuOdT8KfRMW7hTqzPoYfy-iwwtRJ5KXl7RFX5WKDI7yPYwjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73948ccb6f.mp4?token=gPuL8OD8aP1gU8w4kqvGoI0pRMf9lVkIeYmslXm227jyQM3Zboj1PS4V1xEOmi0v7kZsZHSw7GAsjonZYe9VoCOn7LoEwvsV5tEvLHFDT0ZhzFUuLY6I1eFw3JzTNjlYczJZcSLFgebwNcksUnm_VJvK4qb-Fv_khuK5-VqHgwhdBfjeNfV-5hC8hRFMFtxSIPRj3PsvT3aVk7w7EorG-Zjc8HKP-hfAZbEBjWEMKUPN2CfSUioN3dpeCt7CMW5b1NkNig7EmmihZPN1pI0iOaz2jbdN69fy3GSR2JzuOdT8KfRMW7hTqzPoYfy-iwwtRJ5KXl7RFX5WKDI7yPYwjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ارتفاع دود ناشی از آتش‌سوزی در منطقه رأس العاره، واقع در استان لحج، پس از هدف قرار گرفتن آن توسط ارتش یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146852" target="_blank">📅 13:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146851">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گرجستان اعلام کرد تحریم‌ های جدید آمریکا علیه شرکت‌های هواپیمایی ایران را اجرا می‎کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/146851" target="_blank">📅 13:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146850">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فایننشال تایمز: به دنبال گزارش درباره تلاش‌ها برای دستیابی به توافقی موقت با ایران پیرامون تنگه هرمز، بهای نفت بیش از ۲ درصد کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146850" target="_blank">📅 13:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146849">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان: هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146849" target="_blank">📅 13:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146848">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=TvJ0WewAWMoaXy0XO8qqOnVOZMUDalXplnhnnIL-rEwgfB9CsgY9b6spAAQyBGNyA0Lqfgn8AuiDpdi54uT6fpPVuQvbp3XqI0OPJPrOwRFWuWbHd8SHP3LQbioGNsxuFiminscsqBmbpfNX0cl6igKYmFiMcHjmOQYpzFSrKChT7QV-mx4cKIZUPFzDcsJU_elOzhxNhHNYWoYctkQyOQjjCW_KrrH-V1zEcWfE92wH_vcv4DPxwjKdby5cLw7NSZlI_NZHgH0-NYYro1EF_vHloVEKT6v0QaHrSMfIKQGl5qWTUshFYiG891SkPDjgKPLdw8stkn1SLjhNXrFphw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb4e73a23.mp4?token=TvJ0WewAWMoaXy0XO8qqOnVOZMUDalXplnhnnIL-rEwgfB9CsgY9b6spAAQyBGNyA0Lqfgn8AuiDpdi54uT6fpPVuQvbp3XqI0OPJPrOwRFWuWbHd8SHP3LQbioGNsxuFiminscsqBmbpfNX0cl6igKYmFiMcHjmOQYpzFSrKChT7QV-mx4cKIZUPFzDcsJU_elOzhxNhHNYWoYctkQyOQjjCW_KrrH-V1zEcWfE92wH_vcv4DPxwjKdby5cLw7NSZlI_NZHgH0-NYYro1EF_vHloVEKT6v0QaHrSMfIKQGl5qWTUshFYiG891SkPDjgKPLdw8stkn1SLjhNXrFphw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان:
هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146848" target="_blank">📅 13:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146847">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
رویترز به نقل از یک مقام پاکستانی: اسلام‌آباد تلاش می‌کند از کشیده‌شدن به درگیری میان عربستان و انصارالله اجتناب کند؛ زیرا همزمان می‌خواهد روابط خود با ایران را نیز حفظ کند
🔴
هرگونه مشارکت پاکستان به دفاع از خاک عربستان محدود خواهد بود و شامل اعزام نیرو به یمن یا پیوستن به حملات تلافی‌جویانه نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146847" target="_blank">📅 13:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146846">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP7QWEvlIdyf19ddYjrh2KVCK_nmrUVH3QevyzUcPqxomZf-MM2ij-2OM61VJA1MGUvuKcT6vcniol533wbCV8cGdKkBhgTMiQFdEyuvr3DxTaEPRPvJwc6Pk03H2EU48u0Iy-Bd4wGTMOtob2QqTuSZZJCKv1c4W417GZPR7zzhVhBhbJUNjzfG1sp6Ptu7QI49FAYXn8JcwVR_OeLL-EyLf0li0TIjkxUJnBACYBWC0V6UtedYwUmed-FHBz8Eedv9F9foBjVTp6gf4kVId_27W6RE9rw4dMu41efpzj2utWRh8AOu9DiP074lUA776rd4_PWwesC42jdTwQd3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باز هم شعار علیه حسن روحانی
🔴
نهپاد: نفوذی هدایت پذیر از راه دور
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146846" target="_blank">📅 13:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146845">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
رویترز به نقل از آژانس بین‌المللی انرژی:
ذخایر نفت جهان در ماه اوت ۹۵ میلیون بشکه دیگر کاهش یافته است.
🔴
بازار نفت بیش از هر زمان دیگری به پیشرفت در مسیر حل‌وفصل درگیری‌ها در خاورمیانه و همچنین جنگ روسیه و اوکراین نیاز دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/146845" target="_blank">📅 13:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146844">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: دوشنبه یک بانک بسیار بزرگ را به دلیل معامله با ایران تحریم خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/146844" target="_blank">📅 12:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146843">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbEW6dzaw9VcJ9BW3nZGhz3am-0uAdEe-vVpMzrAVDN76m9khGuEA_A_8i5_Sb2pezJhcUulVj2yzQn2wfgihkn3w_-YTAKAMuDq_hx8M9cfv2vWv3K_xbhDad2w1uk3XFThK-6pSJt6Aj_NqYdvRzSK0WMe6SeoAQH5fqp0dLKh7IUxrAejIY7tm00LVWlrIT94f4m5oustgBGh9UVxYGQ29hGOI55xI5plts-E9nAaVUq18ZcSR70CG_6kAYoW4SbC5kVLQ_smNZNOjwDL6OYH1lfPHVWA6mHZOzfJ2gN9KqOrlIpfT9-TwLW4GylLSiJ0Muvp8jEfqf6BHoMR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صادق محصولی رئیس جبهه پایداری درباره مفقود شدن ۱۶۰میلیارد دلار پول در زمان وزارتش:
🔴
اون سهم امام زمانه که دست من امانته
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146843" target="_blank">📅 12:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146842">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/146842" target="_blank">📅 12:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146841">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd237427b5.mp4?token=qB94fkK_tNI-a2qNLGR1v0YkIjGsDKVk45mcjc_EBfamkj83My1zxL2mqk2UzR5nmn3CH0rraV9mTNGNocMFgu4CFbNuchSOIqjYg0f7vctj1gbkbyJM4LvFbt0CTkFnQZ9q6zjJTTSTWOA3Z3SAb7wBOLoJckfTdJ4jsWpOl7p1abwEdZv64yzILsf01GicJX0tAF_EiIHlqJyAZRqRRPVhu78MOrxwJab4Xu35V-jaWB8GYnIGHkIJ6T8UJpBXhUcMu6Ie9tl8XyW8kmBu_25qzatQ4aaJpkPfHFW6M4gGrDvItPuaLDUod6tOm7mCX5lNFq7vz_YDJO8g32vXwzbCKln9e1XhBS1qdZF9vknhkmpDWtqhjVL7TZmjdDUupMK4qC8y5CXpN6h8mueiQkVF-oxiGFXj7YxECnvOpK6JDoe_YK16M_vkUJF4Jpx6jKS43HbtY1foW8YSITG7D90TmTlr6yvjXXADD56dV1gmFm5vZxdkrUfg26qWfB1KDPeitqUDo7Okjk4pIPjv4uoYBMrJIuzdwy_eEMw4B_dimfckwnfd3NHP6mZNHJIavkTm8-tL0CJsyO8-VxLwRtRVbXWxrYXh-MYhrlNV1TLwNhfmfCRZ2Dgym9zol9vRJwN_QZLZBvAOSRDjqKe9Z6rP3lvGEdcpnlJJChTVW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd237427b5.mp4?token=qB94fkK_tNI-a2qNLGR1v0YkIjGsDKVk45mcjc_EBfamkj83My1zxL2mqk2UzR5nmn3CH0rraV9mTNGNocMFgu4CFbNuchSOIqjYg0f7vctj1gbkbyJM4LvFbt0CTkFnQZ9q6zjJTTSTWOA3Z3SAb7wBOLoJckfTdJ4jsWpOl7p1abwEdZv64yzILsf01GicJX0tAF_EiIHlqJyAZRqRRPVhu78MOrxwJab4Xu35V-jaWB8GYnIGHkIJ6T8UJpBXhUcMu6Ie9tl8XyW8kmBu_25qzatQ4aaJpkPfHFW6M4gGrDvItPuaLDUod6tOm7mCX5lNFq7vz_YDJO8g32vXwzbCKln9e1XhBS1qdZF9vknhkmpDWtqhjVL7TZmjdDUupMK4qC8y5CXpN6h8mueiQkVF-oxiGFXj7YxECnvOpK6JDoe_YK16M_vkUJF4Jpx6jKS43HbtY1foW8YSITG7D90TmTlr6yvjXXADD56dV1gmFm5vZxdkrUfg26qWfB1KDPeitqUDo7Okjk4pIPjv4uoYBMrJIuzdwy_eEMw4B_dimfckwnfd3NHP6mZNHJIavkTm8-tL0CJsyO8-VxLwRtRVbXWxrYXh-MYhrlNV1TLwNhfmfCRZ2Dgym9zol9vRJwN_QZLZBvAOSRDjqKe9Z6rP3lvGEdcpnlJJChTVW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار مرگ بر «هیلاری کلینتون» و «مرگ بر حسن روحانی» در تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146841" target="_blank">📅 12:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146840">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / نیروی هوایی عربستان سعودی دو حمله هوایی به بندر المخا انجام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/146840" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146839">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890ff4c6d.mp4?token=Y8xu3TKjewP_dit1qXhkPWe0yC34DrQ1lFYL4OAvYp-JUxk6QgIr-JUf7rOpw2t53iz3gs3luQvrEvY6jJq1cBDewGY6NFOveaqd7ZhPh7XwMBMLwFbhpQW2HZYVB4LLwX7IHjai8Qeo7rYbm9Vej25BdFcQZsunC31tlLCA2dYq8se9rG_ii1uAw9UgyVk12RdLnFvJ2ilnY3xQWeClA34OpIDuF35LmOkX4ZCu1q94UPmFGugOJqA4q_roDN7RF7PUA90FOhuwZkP7JcrKCAqdHuxd3P3du7KDyuVRROm_x5sJUDf5odrx1ZEajqab5CSpOfwTNiLA5zXDd1NBeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890ff4c6d.mp4?token=Y8xu3TKjewP_dit1qXhkPWe0yC34DrQ1lFYL4OAvYp-JUxk6QgIr-JUf7rOpw2t53iz3gs3luQvrEvY6jJq1cBDewGY6NFOveaqd7ZhPh7XwMBMLwFbhpQW2HZYVB4LLwX7IHjai8Qeo7rYbm9Vej25BdFcQZsunC31tlLCA2dYq8se9rG_ii1uAw9UgyVk12RdLnFvJ2ilnY3xQWeClA34OpIDuF35LmOkX4ZCu1q94UPmFGugOJqA4q_roDN7RF7PUA90FOhuwZkP7JcrKCAqdHuxd3P3du7KDyuVRROm_x5sJUDf5odrx1ZEajqab5CSpOfwTNiLA5zXDd1NBeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پست خواهر امیرمحمد شاه‌کرمی از جانباختگان دی ماه
🔴
۱۸شهریور، برگشتم به همان خیابانی که اخرین نگاه های برادرم آنجا بود ؛ تا صدایش را از همانجا دوباره بلند کنم.
اینبار ایستادم برای صدا زدن نام امیرمحمد شاه کرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146839" target="_blank">📅 12:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146838">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
یک منبع پاکستانی با اشاره به گفتگوی عراقچی و عاصم منیر گفت: این مذاکرات بر جنگ میان واشنگتن و تهران، امکان بازگشت به مذاکرات، و همچنین حملات انصارالله و عربستان سعودی متمرکز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/146838" target="_blank">📅 12:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146837">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
روسیه،‌ لیتوانی را به حمله اتمی تهدید کرد
🔴
سخنگوی ریاست جمهوری فدراسیون روسیه: استقرار سلاح‌های هسته‌ای در لیتوانی قطعا علیه طرف‌های خارجی خواهد بود. بدیهی است که این سلاح‌ها علیه غرب نیستند، بلکه به سمت شرق، یعنی روسیه نشانه می‌روند.
🔴
اگر سلاح‌های هسته‌ای در خاک لیتوانی وجود داشته باشند که ما را هدف قرار دهند، آنگاه خاک این کشور نیز در تیررس سلاح‌های هسته‌ای ما خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146837" target="_blank">📅 12:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146836">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfKEElizM8yIRRd2b1QyzOr6bg-mv65zSQg7vlrz56hR3tGLcQGTAGMiVN-ndiFKsbgoVZNbsETFpdUcjnZkIevA34JfhQNqLc10AyBzDeo9RnmxBJ9LrnESDuQ3uZpmtZiNRBBLM0jyRXQPtFssIw6Zf7mzNSlNnha2dkHwxwdr2mqMmCUEPZdSP4huW6PldpDzv9EbXijX3xgNE2qJE2PMqEI5zsy49RaxpyfMGridMcYuY3wPZ_UwOdjH3nXXc0s579DiT-bAG5cZEtbHT9_yz_Bf8AHkjcqXfmDyUcJxxySlTkusq8qm7zGfattwnAdbHWwpGxXl8JdIuKCsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت 5 دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146836" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146835">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcxCvdeCkJxMFYGkLzwP6Hod894l2qXrBq1lg6TUBQilWdnrKD9F4EPUOrfdudy6O180sfBjnCpDaQWqcCQJQkdCfCPvhtgjBEdgkicVjxLltGDpUpzvQnmYcmljj422yKvCjNmlGWzKWlvOxOUC4cGAjWDLObYt0OtcbZJZTYxjiiDJLfFVc8O9G9Omt3h0cJSI4mpHbLbL3EL_VTEfJT5vLmEuTZRYWdwDhdbPmTOwSePwZKiDAy8QlW9X7pht03EzxugRDRAhqTUOvO0vpY-cyas1fX8pOfPBMRElUhpwxiKOWoOzpFNoYEUQjsbent98k9L-xJgdiNRmzDdzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای دو منبع دولتی یمن به رویترز: نیرو های دولتی یمن از جزیره بریم در تنگه باب المندب عقب‌نشینی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146835" target="_blank">📅 12:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146834">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان دقایقی پیش وارد دهلی نو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146834" target="_blank">📅 12:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146833">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLg1jrjVLicD8_gEJr6CpmHXTP8GTb9X-4dPJ_CNvwr_jUa7f9d-7kJBn0qyinll1psYOCMZCJK6UmoAsc9n21koPzUZk1qBG3u759Y65eT4E9JPh0JQsndbyQlWJ2h7YA28rSAbXMGi-iO55WJsY3d9zoz8BAd_SaRlUftggjt9IFP9MRZhpAfAWmZetIQZpxrcqVIy1P1kZhJC8eVP_YNaa2m6S8SWAkFt__xxMBJLRgbFh0Vmb5nRYZtOgKfP9sDZCve872q8IMuqSWscLwoJT6L6G31-O--QZfpQ2WtRcn6u2yexSTjE2D46tYQwngwZPJYfVuYmcE3Ey2rSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
25 سال پیش در چنین روزی گروهک القاعده توی 11 سپتامبر به رهبری بن لادن، برج های دوقلو آمریکا رو نابود کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146833" target="_blank">📅 12:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146832">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
پزشکیان: موافق ادامه جنگ نیستم؛ اما باید تاب‌آوری کشور را افزایش دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/146832" target="_blank">📅 12:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146831">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
وزیر خارجه مصر: باید به یادداشت تفاهم اسلام آباد به عنوان روند مهم برای رسیدن به توافق فراگیر بازگشت
🔴
ما به تماس‌های خود با طرف‌های مختلف برای پیشبرد آتش‌بس ادامه می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146831" target="_blank">📅 12:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146830">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک منبع پاکستانی گزارش داد: وزیر امور خارجه ایران و فرمانده ارتش پاکستان در مورد راه‌های احیای تلاش‌ها برای کاهش تنش‌ها گفتگو کردند.
🔴
در مذاکرات بین عراقچی و فرمانده ارتش پاکستان، احتمال بازگشت به مذاکرات و حملات حوثی‌ها به عربستان سعودی مورد بحث قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/146830" target="_blank">📅 11:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146829">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc4MiSBq1nUS2H_vHcBpyIjfqLTk8UILj1miV_CiiFhB4YZNslDHA6Q9CkJPUpTRz5goh7wuXWTXzhLEaZJxC_slwstQJP7hq9Z11a8vzlD3dwM1vaJ5Nj1GUrXfOvP-07PnzB5cPaCNy4okxI4MKDrQt0oS4PLlrLYnUc7-mkW_uIP7PMuvxNVM2RAGvEy6AdRm7kFXX7RHt4KN9KprIJ3-ZOdu5noEmJ7IePwvatMfJipRZtL4hcSfin2dAEUsEdGN3_5zHhE9Da1ATpPvD0lJl_V6bYl_TGCLKHg8pek7JVMbQjoQ6JWqSdig62gB1onF8NMcAg1bNnvgzUYYnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فرانسه با استناد به منابع خود اعلام کرد که ارتش یمن کنترل جزیره میون را به دست گرفته و بر تنگه باب المندب مسلط شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/146829" target="_blank">📅 11:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146828">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پاکستان: «کمی عدم تمایل» برای اجرای تفاهم‌نامه اسلام‌آباد وجود دارد، اما «پیگیر» هستیم
🔴
اگر توانستیم در آوریل در میانه جنگ شدید، ایران و امریکا را به این تفاهم‌نامه برسانیم، هیچ دلیلی وجود ندارد که نتوانیم دوباره آنها را به میز مذاکره بازگردانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/146828" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146827">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
خبرنگار المیادین: نیروهای انصارالله(حوثی ها) یمن به شهرستان ذوباب در ساحل غربی این کشور رسیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146827" target="_blank">📅 11:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146826">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyITkAwXAu7NhCPEv83bQUDb-TwpcGUl7igqFT0u7elCzZ4TYoU8KM3JRSopgYKp33rDKtxI51fv8VG90pzwdW9VMlF8j68jm1JpUHKlbEVontq33PgrNy9wmJA3WFqXhiwDAbIbEpB7X2oSEF3uu_i8WW-oj_PvJy-Jx2znuU_ImnRTgzBHgTmkAQGLEHvn6OYEI-5dc0iunolk02lqTmlptnVWECUNX3qRvaiGmw1TriVskgcz0XeGPCtUzzm8aplVtzKuHnG4-VBaaFfUPo0g5ZU6TaGOj2W75mN33uUPOricAlX_XNuk5zhhIBn4KZ13PfLwD_jrLAmCekhO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرمانده تیپ خان‌یونس حماس در حمله شبانه اسرائیل به جنوب غزه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146826" target="_blank">📅 11:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146825">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZYxGXwtgcTlpbjGOhLtXZ-5CyROO4iNJQzg5ypXeNadBzS0qcno1OjCX4BCgXGNCQVCntyPbtTX-ZWNZ7vuJMbujPLRoTO9rdfCYYFCvt3suuf7enH26iueI3V6cI8fq99HUoqW9ZtpDZO1A5W32-yrS_Xko4LsgcUQBofNB1vW887VhKZmi1K_TgMvtUerobWGDpBo_mqhi7MAXVPyOW2i4a60_TrRNLlI6_z1McM0Q8j2A4QnVCTnnRR_hdD0nLOFdPDeKV-cxH4MTEFLQKEKc8mBLO3wYimeRWuF8RLgaiyYQAA6MvL9RvVHwFQG_q0o1xcD4mtBH10d9pBWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دستیار قالیباف: تفاهم‌نامه‌ای که به قول خودتان مرده است، چگونه مقصر علی‌الطاهر است؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/146825" target="_blank">📅 11:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146824">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزایر حریم هوایی خود را به روی هواپیماهای اماراتی بست
🔴
این اقدام در پی قطع روابط دیپلماتیک الجزایر با امارات صورت می‌گیرد. الجزایر، ابوظبی را به دخالت در امور داخلی خود متهم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146824" target="_blank">📅 11:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD8HRDaBK8CeBnHrRhVnjvk8gzJzgOJ4RYin1b8jJ4qKBP7meK9NhNbIutqBSyQ8JhKmyGoTTRWzuHFjXvNtJCq2yomBWwek1EVBADERokb-75jwqyBupyPKSMppqc_mFwPWla9dOohBU9nMNsmJdDQ4x84sUmRt_O5SwVjP_HtaE9c0SICp0nk0OAsfkXP1nvWDhdQzq24w19obe1g9Mlv95Hcxc4WdDwZ53rYtqsJoQ6EeHg0eWdze3tF1hYxkmmpXCUMOle2JahW8_GZtfpecxI0QWAIsMDf80P94mjMiDrcfCQ_-v7K_2NvlutBOTW4iPYAS-8BXhCg-LHVJUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff55988390.mp4?token=kWm5Bas_X7gPggPgz3ylWBszjdXy46OGIAXBYkIRt8LaiPQmNkSzL0nuSH6K3bolEUK9AQ8Tq9lZJuAYYJCOI5MHG8BKvQT55nbrqAMbGcOTB8W6vTX1Wh7cAbq33pm9o-rjWDn324UEFNRTN7kKqvESaz49Kciv0hKc2rD2CzQFFC75O8IXt4lh4DddmbycarMX8m_w_lRKtdwTVYarFW_35OKzSf7wefpoy05q2wczl0F-9pMFo7FnC_63fdRTW2j9o5T3NmBkEZb9ABUn9-jYeUkgdKROaNV76RgobqCnfqvJTMaH-oxP5bmO_1wnkapaqyNGOrmTo5qnVGW8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff55988390.mp4?token=kWm5Bas_X7gPggPgz3ylWBszjdXy46OGIAXBYkIRt8LaiPQmNkSzL0nuSH6K3bolEUK9AQ8Tq9lZJuAYYJCOI5MHG8BKvQT55nbrqAMbGcOTB8W6vTX1Wh7cAbq33pm9o-rjWDn324UEFNRTN7kKqvESaz49Kciv0hKc2rD2CzQFFC75O8IXt4lh4DddmbycarMX8m_w_lRKtdwTVYarFW_35OKzSf7wefpoy05q2wczl0F-9pMFo7FnC_63fdRTW2j9o5T3NmBkEZb9ABUn9-jYeUkgdKROaNV76RgobqCnfqvJTMaH-oxP5bmO_1wnkapaqyNGOrmTo5qnVGW8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار اسرائیلی‌ها شهرک المنصوری در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146822" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146821">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
پزشکیان: به جلیلی گفتم هرجا می‌تواند برای حل مشکلات اختیار می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146821" target="_blank">📅 10:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146820">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز به نقل از مقام دولت ترامپ: حمله ایران به جنگنده‌های آمریکایی در اردن آسیب زد
🔴
یک فروند هواپیمای A-10 تاندربولت ۲، معروف به «وارثاگ»، هدف قرار گرفت و یکی از بال‌های آن از بین رفت؛ همچنین حدود هشت فروند جنگنده F-15 دچار آسیب‌های جزئی شدند
🔴
حمله ایران، نیروهای آمریکایی را مجبور کرد برای مقابله با موشک‌های ایرانی حدود ۳۰ موشک رهگیر پاتریوت شلیک کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/146820" target="_blank">📅 10:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146819">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9cab6fc4.mp4?token=s0FPBsjSH50XAUSLVok540OV5wr0KMcPvfNMHLYgvFyjxyUiE7-RePvXejjP6SxtRYDqHX8Arz4sqsWPN_nZgZU0Z8Gs9IlyB_7FPsLe0JBX3BqmrcrXxcnQgMfmnhLBQCW_GamDqnUdOz-fyJNYaKPVwG2oPuLwv3gKFB0OKonaXpLPsa49lNA0w7vEqxfQzzFnX0sGCd-NAaNUHXU9hxz-TVU4fIbFwfxA3pROwFSH3hIRoKRbiu0hR61JMLzq-PZ1kHKCO-AOwBfr8rFU0oqFvYnxLcsdv6gbI_iSG2OW-tRO8KdFWspkS1OK6IhDKyUyMrK2zc5ZZznIwVQ8MkuCc6Fq5ORChhfDNg70ftXIsKWdSY5BuICO94TgTzuwUo3lQDFwvd7mE_JWkWB0xJMSPLNaOGxYn3qawVztpQuF3jwE1bIcwkkHIWr6-3Zd3q4AwQTBLIPzi38cIzKmj1RRCK5gruAKlmIxePjdlnN3AeJzqMIFMlACD487yICsYgDMpbnVEbo68vrx1m8ovkdawTQA8JAJh_nNy2gayLhmb8Ee_W_7v05j0WnEdrooDLIvgjV9F-vHJwKOYFtpTcwCoPikai7MPJsz8V7bigfhe0IZCgDHyj4vuUEGEKroI9uRUCKtVrRnHh_dpP1yJLxdD27ylUORWKRrJbUNLPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9cab6fc4.mp4?token=s0FPBsjSH50XAUSLVok540OV5wr0KMcPvfNMHLYgvFyjxyUiE7-RePvXejjP6SxtRYDqHX8Arz4sqsWPN_nZgZU0Z8Gs9IlyB_7FPsLe0JBX3BqmrcrXxcnQgMfmnhLBQCW_GamDqnUdOz-fyJNYaKPVwG2oPuLwv3gKFB0OKonaXpLPsa49lNA0w7vEqxfQzzFnX0sGCd-NAaNUHXU9hxz-TVU4fIbFwfxA3pROwFSH3hIRoKRbiu0hR61JMLzq-PZ1kHKCO-AOwBfr8rFU0oqFvYnxLcsdv6gbI_iSG2OW-tRO8KdFWspkS1OK6IhDKyUyMrK2zc5ZZznIwVQ8MkuCc6Fq5ORChhfDNg70ftXIsKWdSY5BuICO94TgTzuwUo3lQDFwvd7mE_JWkWB0xJMSPLNaOGxYn3qawVztpQuF3jwE1bIcwkkHIWr6-3Zd3q4AwQTBLIPzi38cIzKmj1RRCK5gruAKlmIxePjdlnN3AeJzqMIFMlACD487yICsYgDMpbnVEbo68vrx1m8ovkdawTQA8JAJh_nNy2gayLhmb8Ee_W_7v05j0WnEdrooDLIvgjV9F-vHJwKOYFtpTcwCoPikai7MPJsz8V7bigfhe0IZCgDHyj4vuUEGEKroI9uRUCKtVrRnHh_dpP1yJLxdD27ylUORWKRrJbUNLPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
«آیا ممکن است جنگ با ایران تا پایان دوره ریاست‌جمهوری شما ادامه داشته باشد؟»
🔴
ترامپ
:
«نه. حتی یک احتمال هم وجود ندارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146819" target="_blank">📅 10:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146818">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
خبرنگار: «درباره پرداخت‌ها؛ آمریکا ۴۰ تریلیون دلار بدهی دارد. اگر سیاست‌های اقتصادی شما موفق هستند، چرا باید برای حضور مردم در انتخابات مشوقی در نظر بگیرید؟»
🔴
ترامپ: «من این کار را به‌عنوان پاداشی برای مردمی انجام می‌دهم که مجبور شدند پنج سال شرایط وحشتناکی را که بایدن ایجاد کرده بود تحمل کنند.»
🔴
خبرنگار: «شما همچنین وعده چک‌های بازپرداخت درآمد حاصل از تعرفه‌ها را داده بودید…»
🔴
ترامپ: «نه تو. نه تو.»
🔴
خبرنگار: «اما این اتفاق نیفتاد.»
🔴
ترامپ: «نه تو. تو بدترین هستی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146818" target="_blank">📅 10:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146817">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
گفتگوی تلفنی وزرای خارجه ایران و کره‌جنوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/146817" target="_blank">📅 10:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146816">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhDzZsf-fQjHQXCaOkFjz5AL_eKTq31jcC4-hnXR_yZnVKALoGmyu5MhlTdZajvqYIVpYpnC9QWfjCnxLgHIRF7DGGt8t8eAOcdRbfStMYSotoKgH6capItHzQmyOx6M4Ah9pCH9S7DEfAr5gokmYS6VV0Nvn9DGrLtlLOYKKm7zxFXf727zp9LwrdCv4Ql0yQ14oZrG9ACT6_XRX2gGbi8hkm7-_mlJbku82VQQogiBPVb_odF3Ja3hP0RdUDw8hr4d_ckaWKP9-fNkAGy0ARjqYlneEWwMYQj5M9MXOVUnM2VgBxwKsPqQ3atVMY_RThgF2mOurW3BkQpUrnxCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آموزش تیراندازی در شب نشینی شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/146816" target="_blank">📅 10:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146815">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بر اساس گزارش رسانه‌های عبری، دور جدید مذاکرات میان لبنان و اسرائیل روزهای سه‌شنبه و چهارشنبه در رم برگزار خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/146815" target="_blank">📅 10:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146814">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اکسیوس: ترامپ درخواست بن سلمان مبنی بر حمله به مواضع حوثی‌ها را رد کرد
🔴
دستور ترامپ این است که نیرو‌های آمریکایی بر ایران و تنگه هرمز متمرکز بمانند و از گشودن یک جبهه دیگر خودداری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146814" target="_blank">📅 10:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146813">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79badc7e41.mp4?token=uvmc9YneM_lvYhm72g4F2tHdW4fgJnWWCdt-QOCa6nr3wxaVt5s5KE7KJmtAh8drQieHGfKddkge3Kc3l7WRuEBgSQtBo4IWcQWl47K13ojf82JfVlE50BDLKocbxoSmaRx3PWtb_qjU9063xFNh8HSsqt7FGN0N-9DlBa7YBRtVgvw-x-Rh_0Qr0VTFDUFzykXg_iL-GSl2FYkOWNWZZj4aVzXCAuDxyxd4XJ_eJalC6GuSzrq-g3niEHFfWlZhUvAZO3SXHVDZWXTq6fyvtIXCuI1kM0jsKrKXrYcZAFFjBsjfK9VAzPF3VJY_Metd7hReNYSEx0eySZESPmdtZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79badc7e41.mp4?token=uvmc9YneM_lvYhm72g4F2tHdW4fgJnWWCdt-QOCa6nr3wxaVt5s5KE7KJmtAh8drQieHGfKddkge3Kc3l7WRuEBgSQtBo4IWcQWl47K13ojf82JfVlE50BDLKocbxoSmaRx3PWtb_qjU9063xFNh8HSsqt7FGN0N-9DlBa7YBRtVgvw-x-Rh_0Qr0VTFDUFzykXg_iL-GSl2FYkOWNWZZj4aVzXCAuDxyxd4XJ_eJalC6GuSzrq-g3niEHFfWlZhUvAZO3SXHVDZWXTq6fyvtIXCuI1kM0jsKrKXrYcZAFFjBsjfK9VAzPF3VJY_Metd7hReNYSEx0eySZESPmdtZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، خسارات وارده به تاسیسات نفتی جازان متعلق به شرکت آرامکو در جنوب عربستان سعودی را به وضوح نشان می‌دهند، جایی که تعدادی از مخازن نفت تخریب شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/146813" target="_blank">📅 10:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فایننشال تایمز: ایران و کشورهای خلیج فارس روز دوشنبه در عمان درباره تنگه هرمز مذاکره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/146812" target="_blank">📅 09:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146808">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LSV6xfAHLDynPlNQacFKD11c2MujdWykZKo9GIjgJeVboVR48YlkkFf6AF4OyQrQEciuO4cV_qvXemDCiuo6ZhHg_kumJHMd77z0RwzoV5pos71QMwdngfveWP4azY3o3WwgVdT4CRHtrY68vL_qhshT3pWLwFQi8Ua6escSrGTb7KKyGsPP5vZLX8MZQ1X0ArU9xng89c-bZkOGBuZ-pNDUS2sCe-iFn7_xLY6fJ9iTiZx-_SvGYnBGrXwrOtxvY7sPl0j4WMdOuIQd-XtKGAOYX4DrHDAEEW0IH467C6SJb_j7ZP1073Ro17StD2G7-XxCGoEcmMZ8RqPjVP3f5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_qEKvtkQMln-zHLLHrXppzni16O8dB5fyJG0bbx7ms5oe2B9CdOxlDsVVRyFkerxSix9WMWuhvFAPp3heNHuBUwLj9jOA4D3JjHoeok4dlcHe1aG6XHy9jXR_YYN5KYFY4jowPH8XRf45wENIE9Emv0bYE8DEtwMpmlopyQ4-GJcRR9F-p_6i8AgBJPyjn79F-h2zw0yqg9IC06ecKGNuRzr9LtoeTy1GR-y_ZD59iLyi-9k5baRYGQqE1ftWCZY5ceA9G0qei9gudtqkzzLJEG4YRfrbF3l8zRU5rBacSukA0MO7k3Mks7DIwkLJ2DXEGo1syF5uU6l6jUbHimKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uP1bAal2U7TnJT6eag5yz72jkYu_F63H9Phdk21U3HzlJX880wgEpg9iD33l0yCX4dvsVdrKHe4bIhVKhgEOgr1uuPD2nlIOo6owetRmLNyonpxVYGvl2vCC0i2Sr_uMBFVvMaQA4g9uH9VlhDBwvEF0gurBvoUZUQoKOOWwNMsRBhKr0gD4IZXYXCe5vUsuOMcdogVZDJKDN4dJua4YB9Aq3tvtgGCLsnLqPKXO5nP-gWgjgeATPQI__qOQLez0PBeOaMRsTy3jDjJV4Jw3OHyjlBvhXoEwm7sx67wsfX1BaX3CWA7L3Tgu4qMEmmy3eudqz4RzP9vJOZlI67oAPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d91da570a.mp4?token=l0Fw2jPZxPDOOaU4FAVxmWX79LouQb5olzfVeZ6dRqKFozA4jhIYHh524qIxvF49Da0JloOiA-rdMJBhPl7sGAw3RepTA8YtIG_udV09IbUXSZ4HdR3c_-g4NzQZB5fE5CDjdTbh34hZvxTgBsR76j-6GNdU9DNlaWQYL-iLVtIpVRAcxHVRJddDeoFc_sXXwQB6_VmJJwWIOpadha2qDD5u67OoIew5V9ycODBXvHLFe7ByhKx-1hQ5v7zrpirAxCfgEDAdVN0JpLLRamwexRNByUwAS02jeZFqqCz5V2pQcPWbhgnRLW_8TrcBoQjsjP-T72V9VraWHRtewDzdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d91da570a.mp4?token=l0Fw2jPZxPDOOaU4FAVxmWX79LouQb5olzfVeZ6dRqKFozA4jhIYHh524qIxvF49Da0JloOiA-rdMJBhPl7sGAw3RepTA8YtIG_udV09IbUXSZ4HdR3c_-g4NzQZB5fE5CDjdTbh34hZvxTgBsR76j-6GNdU9DNlaWQYL-iLVtIpVRAcxHVRJddDeoFc_sXXwQB6_VmJJwWIOpadha2qDD5u67OoIew5V9ycODBXvHLFe7ByhKx-1hQ5v7zrpirAxCfgEDAdVN0JpLLRamwexRNByUwAS02jeZFqqCz5V2pQcPWbhgnRLW_8TrcBoQjsjP-T72V9VraWHRtewDzdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کلش ریپورت: تصاویر ماهواره‌ای و داده‌های حرارتی، از مشاهده ستون دود بسیار گسترده و چندین نقطه حرارتی در مسیر خط لوله نفتی شرق–غرب عربستان در جنوب‌شرقی مدینه خبر می‌دهند
🔴
برخی تحلیلگران از احتمال ۶ تا ۸ نقطه اصابت و آسیب یا پارگی خط لوله سخن گفته‌اند؛ با این حال، تا این لحظه آرامکو یا منابع رسمی عربستان این حمله را تأیید نکرده‌اند و رسانه‌های معتبر نیز هنوز تأیید مستقلی ارائه نداده‌اند. گزارش‌های شبکه‌های اجتماعی نیز همچنان متناقض است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/146808" target="_blank">📅 09:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-146807">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رویترز: عبور کشتی‌ها از تنگه هرمز به ۷ فروند کاهش یافت
🔴
داده‌های اولیه ردیابی کشتی‌ها نشان می‌دهد که روز پنجشنبه تنها ۷ کشتی از تنگه هرمز عبور کرده‌اند؛ این رقم در روز گذشته ۱۱ فروند بود و همچنان بسیار پایین‌تر از میانگین ۱۵ کشتی در روز طی ۱۰ روز گذشته قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/146807" target="_blank">📅 09:47 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
