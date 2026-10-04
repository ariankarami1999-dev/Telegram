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
<img src="https://cdn4.telesco.pe/file/Z5P0Rgbq6jBZCK3Y3sNxSfo0pwNkRda6IAY61ySDJd2Oomd3KaMMbvalNPD1_liIuTZYsSkk0P8zSQbwWlip0RwXSJ_3XJ5B_q0YiHVlxXhLKXstFxmptKrhIYAm9O52AWsxZmElfXXKaoMu1Ph1kWVjy2jve_n-J7Y7e5fI83ujI2a5_Y-SjXXhwg99HhJdB4Ivs4GJ88a4UabL0biuBJpvSTbFgx4ErrzY0s7LYIQhfpW8RZ8Li8ueSFu0JYeIi3484mFT5uJE7HyKhfEyMgjgV_8A3N7hxTAQl-Tv4aPrFW7YIkKIJqh7vCNC5S32YzglLZDHaDWy_xT9CRWXHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 16:08:11</div>
<hr>

<div class="tg-post" id="msg-150935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
اصغر فرهادی: آمریکاییا خودشونو برتر میبینن و اصلا دموکراسی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/alonews/150935" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muZGp55rbL4yM-8mLIBMSKC9hjosKW4o1NXshKftu4s4cIvYltk3nhBVlOs9nCbZoRFLm7FCpb0Q2NLkliZo1rAk6H5d8HoKnjqncURqgbfRB1PRCm4aqGQUrsjPtjiMytioDizf1Hy5ksHGwmiuUCOnsz3-GKpIn3B-YutAXc0g-ba7irOg-cmfMb7kdLahaZ2xymojIE7MYsnZQz4Lnj9kPIgUt5b-IrXp8gcprrhjBYInIOpX_f0ZOsZJHaaZI8W-Wly34rVoa4L8c4ldAdr1zbmiq648ubzOjhoNzQptFXIWAg49A0dBipRdxUfiQ9Nbye7vx2_ecQ8_r2ObxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، جان کوال را به عنوان نماینده ویژه جدید خود در امور گروگان‌ها منصوب کرده است. پیش از این، آدام بوهلر این سمت را بر عهده داشت.
🔴
ترامپ گفت که بوهلر به عنوان مشاور ارشد، "به انجام وظایف دیگری نیز ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/150934" target="_blank">📅 16:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
گوگل دسترسی کاربران رایگان جمنای را محدود کرد
🔴
از ۹ اکتبر (۱۷ مهر)، کاربران رایگان جمنای تنها به مدل Flash-Lite دسترسی خواهند داشت و مدل‌های Flash و Pro برای آنها حذف می‌شوند
🔴
مشترکان AI Plus نیز دسترسی به Pro را از دست می‌دهند؛ کاربران AI Pro و Ultra همچنان به هر سه مدل دسترسی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/alonews/150933" target="_blank">📅 15:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=pZxM2pNBJjem7sA61xSB12S5OsKKSc-Mjt7MSvYa0fzFVdvSkNEmU67-z4SED77NDUYDQcVU8PSG6U7mly3vEie_ZEjhtAgvL5CMmvoK0puea8sw83mjqVK7i9i9khgmi12ei5At62T5jDtYTLyVmlWbDEzr2e4u5PWc2nbrpQmUD2t2T17LO3Kd1H5ZllM0AqVjBF90-_YiRJX90CESPWR7KVRn2BNYqrxAB7qM5wNMijmhLyWqjOEsrRjxzVJLqc6e5KkcgSiEnJRVGNN98rx1pr2AorRdPe5R3z8rkAsBrcCyb2XIvAZagMl5eOmxktc9zWuR5u9aj50_L5k6HkiaNQ0uoWAsMtJm4x77huiq9hDxTNW5_pjx2dByWuks_AG2tAvG5PA8et1_PK3Snno4E2RUeg-VSWRt7zbXwyGyPuKp2N15tmRQdPm57hpuyw_YXhoCU2iZqZHrYPF5HfnAanxKBS4DFJxgUxyRG7MxSQ0dy0-didZ0UDhwE77lpX4NCU8x6VIb8rfLU-PG9Z3AKBAmtwxrgAPeHPqqOgU9k3tMhCHRh2hM9tRDMhgyrQHsgChrc54yvjhzSgNMU3Gcqe2pYwjVikXKmPzzy8_CXweDqrjgE4Myo_ebYAaqKBYV2IroYj1uYJFp4xBtmFdT591pVUf4qXH1nk4L6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=pZxM2pNBJjem7sA61xSB12S5OsKKSc-Mjt7MSvYa0fzFVdvSkNEmU67-z4SED77NDUYDQcVU8PSG6U7mly3vEie_ZEjhtAgvL5CMmvoK0puea8sw83mjqVK7i9i9khgmi12ei5At62T5jDtYTLyVmlWbDEzr2e4u5PWc2nbrpQmUD2t2T17LO3Kd1H5ZllM0AqVjBF90-_YiRJX90CESPWR7KVRn2BNYqrxAB7qM5wNMijmhLyWqjOEsrRjxzVJLqc6e5KkcgSiEnJRVGNN98rx1pr2AorRdPe5R3z8rkAsBrcCyb2XIvAZagMl5eOmxktc9zWuR5u9aj50_L5k6HkiaNQ0uoWAsMtJm4x77huiq9hDxTNW5_pjx2dByWuks_AG2tAvG5PA8et1_PK3Snno4E2RUeg-VSWRt7zbXwyGyPuKp2N15tmRQdPm57hpuyw_YXhoCU2iZqZHrYPF5HfnAanxKBS4DFJxgUxyRG7MxSQ0dy0-didZ0UDhwE77lpX4NCU8x6VIb8rfLU-PG9Z3AKBAmtwxrgAPeHPqqOgU9k3tMhCHRh2hM9tRDMhgyrQHsgChrc54yvjhzSgNMU3Gcqe2pYwjVikXKmPzzy8_CXweDqrjgE4Myo_ebYAaqKBYV2IroYj1uYJFp4xBtmFdT591pVUf4qXH1nk4L6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رشاد العلیمی، رئیس شورای انتقالی یمن (PLC) که از سوی عربستان سعودی پشتیبانی می‌شود، آغاز عملیات نظامی گسترده در تمام جبهه‌ها را برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (أنصارالله) و احیای اقتدار دولت PLC در سراسر کشور اعلام کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/150932" target="_blank">📅 15:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
اگه از بازار جاموندی اینجارو داشته باش
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/150931" target="_blank">📅 15:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
نتانیاهو در حال زمینه‌سازی برای آغاز جنگی است که برگزاری انتخابات را به تعویق بیندازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150930" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilkw364O7cQQUSS6Y0eDoldZ-FNUuqznUV8MOPkTaGpMleXBwnND3kE37i4SRqYnD-B4AV_rHMLTJ2FInOidPrHEIes8aJoyIr1zQspx4YNShlynF6r-Q0mvL67wvtRsQXEUcAVBMi5-0l9S07yT1lzwk00yBW2cgJ-PbCF5xITIqN6oKfHUOMFZjyof15RAkCZP73sIhfOh3yzXtA2Yk3HwrjYaQgXKI5my7QlDSMO7Jvl8WAk5R2L9YO8lVKH0QeqBJ6ojBxfJh3u1F5c73dkHHzjw77ct8hQFTsceoEFNFWgjKhbE1hN9Vgue1bNRbQmR0pEqnIt0OTCeyl4bCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین برف پاییزی بر دماوند نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/150929" target="_blank">📅 15:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کوچک‌زاده، نماینده مجلس : مملکت رو دارن به آمریکا میفروشن. من گفتم این جنایته. به خدا اگه از جهنم نمی‌ترسیدم، امروز خودم رو جلوی بانک مرکزی آتش می‌زدم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150928" target="_blank">📅 15:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e6ff2766.mp4?token=PitSHUvJYAQQF4MuAq9Ftv-JwLs9S4haJWp4mubmBvDzvMoSFXU_gRyF1mWlB6ti_hczo0xfa8DBwpZGn6V_yS6LYZPzAz-flBh-m7F9aVSJGCPGp6FUXqt_YK1-72mQBUw-GRxa6dXJSGuIZDh6APcyt8hmaoW4wl_xIuSdCwUIgB-rvqHxSn3H2OtL46bi_F8n8ouxY2phgeV-JBq1THPsSdo-AMKWPWSKKC-6eM4iMsgOxBqoujBr_HxFdBADZ8J378vg1huaGHoU4YTvb2dPjPACc5BztGe_faSHxkxzZ4pse_SFdaKF4Hx668UROaSJa18vTGIZVNinBeaE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e6ff2766.mp4?token=PitSHUvJYAQQF4MuAq9Ftv-JwLs9S4haJWp4mubmBvDzvMoSFXU_gRyF1mWlB6ti_hczo0xfa8DBwpZGn6V_yS6LYZPzAz-flBh-m7F9aVSJGCPGp6FUXqt_YK1-72mQBUw-GRxa6dXJSGuIZDh6APcyt8hmaoW4wl_xIuSdCwUIgB-rvqHxSn3H2OtL46bi_F8n8ouxY2phgeV-JBq1THPsSdo-AMKWPWSKKC-6eM4iMsgOxBqoujBr_HxFdBADZ8J378vg1huaGHoU4YTvb2dPjPACc5BztGe_faSHxkxzZ4pse_SFdaKF4Hx668UROaSJa18vTGIZVNinBeaE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از پاکسازی یک سنگر نیروهای روسیه توسط نیروهای ویژه ارتش اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150927" target="_blank">📅 15:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نایب رئیس مجلس: وزرای پیشنهادی اطلاعات و دفاع تا پایان مهر به مجلس معرفی‌ می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/150926" target="_blank">📅 15:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150925">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
تابناک از احتمال بازگشت گلشیفته فراهانی به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/150925" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150924">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا از حمله موشکی سپاه به یک نفتکش در تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/150924" target="_blank">📅 15:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150923">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnX3DP-Mymf6UrK-N7zK5ARQJePVYPi4EwJfrXFUmJZpewQjo-1GMtIqBTgQ5nKNsDnKIs9OQAo5Q7H4DYSXThAjafWyjlIqC6XpxivmWxWElCCVzCT7RSslAz_cN3mSZI6-5t1UA4_ekiCXLEOQvg8VhpgUz-k1yFqv8NTTHcBiQkSIYZTE24hgULAiD9_mDmVVAXyCO6mG3tVsvLv_AcDZcdDJyQhJgflpcquyo3GumDT95-mJ6w_-V40RekAKmprKV9VBOgtiIv-j6FcskYismBHyHT1gp8v5b3Najx2OE73nalWXT3JhjFrTLPkwep4SW8dwAXYV3HJctguphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی ها کنترل العزاعز و المنصوره را به دست گرفته‌اند و به سمت الاصابح پیشروی می‌کنند و به حومه شهر تربه نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/150923" target="_blank">📅 15:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کارشناس صدا و سیما: تو راه قله‌ایم و کوهنوردها میدونن که نفس آدم میگیره تا برسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/150922" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150921">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
نیویورک بهترین شهر جهان در سال ۲۰۲۶ اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150921" target="_blank">📅 14:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a486bfc79c.mp4?token=CP43feDyzLzhYcSyMqyUipgY7gfpbqNMaFIN2SnB3TloNhqr4Qyq98rDmqcDsIjnK23DCJ1Vt3ioClPbJ3E13oq-kt6c2eoPOCJqkSxPrdBKDv-NhCQ6FiNjC7bvycS1wJt6n1_qikdIZs28GOJlJmqQX_5m6c4C7uB1Ms6tYsI9iImVKUucT-fHJl7WqvCxsxt-IDZEsGqf6oSvlcs9RBoWhP3kAPW_55pq-NkkKUq7EaSWef5M_Z2j66YQCBA_YxaRUr6EBEJzn0ajOj0-XUy8ns5hANVfBsGcIlF0p9U8DTjJcWKb6N_OG3Y9yrIvJmh0a8HRycp0nQZKJdmoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a486bfc79c.mp4?token=CP43feDyzLzhYcSyMqyUipgY7gfpbqNMaFIN2SnB3TloNhqr4Qyq98rDmqcDsIjnK23DCJ1Vt3ioClPbJ3E13oq-kt6c2eoPOCJqkSxPrdBKDv-NhCQ6FiNjC7bvycS1wJt6n1_qikdIZs28GOJlJmqQX_5m6c4C7uB1Ms6tYsI9iImVKUucT-fHJl7WqvCxsxt-IDZEsGqf6oSvlcs9RBoWhP3kAPW_55pq-NkkKUq7EaSWef5M_Z2j66YQCBA_YxaRUr6EBEJzn0ajOj0-XUy8ns5hANVfBsGcIlF0p9U8DTjJcWKb6N_OG3Y9yrIvJmh0a8HRycp0nQZKJdmoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثابتی و شهریاری تو کره باستان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/150920" target="_blank">📅 14:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecd2cc8b.mp4?token=okZ05fIhVyHD_ePpMoSb7AqHL9HwUXA8gMbo1-K8qx250EUQuMRKcgFbWgkOYqpEJS6Y12KgmwgnJ5gLLzIfPdlkSH7qwdqu10rU4hqWLn1p5m4naAV0rNIDg4tuduUy1iacu53TWLwo5iaazvizJtT4PWq0KmpdnHXH4N4e3X_TSQ2-wvLHcRIsvebxmrRhdpxsEG-yJVtqxQP6j5_EAn2qEdsF7bZjgC-C_JHqOxQ69LqTk7en68ZvngP4aKhWGn0drmgVE1tvQXinnK7g5chTmxUKmXjXYsg3TY9aW3yEqzYLRnGyJ9ymu8UOGEbt5PcHgiIU3RLF6YvZage5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecd2cc8b.mp4?token=okZ05fIhVyHD_ePpMoSb7AqHL9HwUXA8gMbo1-K8qx250EUQuMRKcgFbWgkOYqpEJS6Y12KgmwgnJ5gLLzIfPdlkSH7qwdqu10rU4hqWLn1p5m4naAV0rNIDg4tuduUy1iacu53TWLwo5iaazvizJtT4PWq0KmpdnHXH4N4e3X_TSQ2-wvLHcRIsvebxmrRhdpxsEG-yJVtqxQP6j5_EAn2qEdsF7bZjgC-C_JHqOxQ69LqTk7en68ZvngP4aKhWGn0drmgVE1tvQXinnK7g5chTmxUKmXjXYsg3TY9aW3yEqzYLRnGyJ9ymu8UOGEbt5PcHgiIU3RLF6YvZage5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
عرزشی‌ها بعد از ۱۰قرن حرم امام رضا را از یک مکان مذهبی به یک مکان سیاسی تبدیل کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/150919" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZNSyXGzd2qhjTltKX-jz2k0YPqhWJ7g_Cy9GiFkzIFvohOt7scegyaFrcUd-QAtuykf5oQo9TylrS1aYO4gANsxY4IijzFMwhv_S8YBwsNEcwkC_LA1x5qrNpqZfAnxntn2adUWRBGIQPWem43aQ6qo3dvbiWNtUZ1_XMYCtNqQbDOQ7wVAczjnK-i5c4-Chh93Ca_llk81yXeHAtqksf4uNIA1xp6wtId_dB1PgtOIA1XMlstAH8YjYGtFnzOGrKQjX_e7J8Bq6gQEls7rQwi4NWkZa_1hHraoQE71FBxmCbHX4XmvBxAtjDzQCQJESIcIVRYB6U3ZnZu5uWGgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه اجاره یک سوپر نفتکش برای حمل نفت از خلیج فارس به خاور دور به حدود ۱.۳ میلیون دلار در روز رسیده است.
🔴
پیش از آغاز جنگ، این رقم کمتر از ۵۰ هزار دلار در روز بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/150918" target="_blank">📅 14:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0558dea8d7.mp4?token=Obk2i5VR-DKNWBIQvCJK_oJn8bCPJHqiTnW1nCB9QGr8Y-U1xZNwjHNTuBBsuUuyPpUQ1BoYne7JtfIvEallsH-cIuZiaGu_jsoRDBjCZy7ISQ3s3JI79QpFCzB3tNwrL10UBjSbohSRqey-afMoEPXVl-m2C6OeQKMnuYJu6WdcYr2yR7NKVhUiPOsI-INvoh9h_F3by4dXPMS-b_qqU-xqLwQftR2lvMqP5Ug82flO_lHXJpCDvCiXV_EebacGAVlsAy3pZTplXuhbQfMLPQi4W9SNnDFWs5FA7lf2ELRg6QZsyGyftLiRL7zZ-bEdcdRJWu1iSN47ALBqrXjqwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0558dea8d7.mp4?token=Obk2i5VR-DKNWBIQvCJK_oJn8bCPJHqiTnW1nCB9QGr8Y-U1xZNwjHNTuBBsuUuyPpUQ1BoYne7JtfIvEallsH-cIuZiaGu_jsoRDBjCZy7ISQ3s3JI79QpFCzB3tNwrL10UBjSbohSRqey-afMoEPXVl-m2C6OeQKMnuYJu6WdcYr2yR7NKVhUiPOsI-INvoh9h_F3by4dXPMS-b_qqU-xqLwQftR2lvMqP5Ug82flO_lHXJpCDvCiXV_EebacGAVlsAy3pZTplXuhbQfMLPQi4W9SNnDFWs5FA7lf2ELRg6QZsyGyftLiRL7zZ-bEdcdRJWu1iSN47ALBqrXjqwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به صدا درآمدن آژیر خطر همزمان با دیدار زلنسکی و مرتس در کی‌یف
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/150917" target="_blank">📅 14:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بابک زنجانی: وضعیت گاز خطرناک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150916" target="_blank">📅 14:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
پشت پرده ترسناک دلار
😳
‼️
خبری که بازار رو ترکونده
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/150915" target="_blank">📅 14:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کارشناس صداوسیما: تمام اتفاقاتی که داره میوفته از نشانه های آخرالزمانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/150914" target="_blank">📅 14:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=kfJzraNLr4z7iv-5NiCPK83lZkTy_pR468lNqICl5TBGk94mkZWASDaBttNY0fxfIxDPiMGN0cTsbPl7zDf246qDubxIduReZ3gQotROssKiHrweHGSS2nt8bBs2B4REBCLrpdxxHuYI6D9beZFWpbC870V4MuOapmEQLll75XfpSNkuowCKBvq5IYpAWpt1EmYNx1kHSKuSnvZBI0UtIlcTinjdwqP7t7YVJWtEnZcftDfBqm1KADstXQttEpF6WZwrG3QdEWy6C8yx4dq-FqjsRmTpJnyxqVFGy_t88CWMxS2801LrzCaTA-vZL2DSbyHzzS2dXynYjBidz89h722SjaTQtrcTC5I4hf2gKICE-P0sY_AFpSjLSm1sXM1y8h0ERS7WCQENp3fHO4jt7Tf14NLDtTZEqKgkH671CUE5SsfgLzgUN5S1a91ibB2HF2mDLPmTp53SXnjxuqu5N7gQDyRrD1jK1EorLB0N2mXXLQkrHSx4ejJvicibhxq_D0wEXCElqx_r4yhH_G2cUlMFsIsbOx-fXNF866msaz93nPwcroL2opALaQ5DNYeBdRWF-KPIbJWjkf18LKIr2FftWYi36ZaDoOh3GFHCLnIc2P54BTaGrFvEQeOlTllgeGfFqPLrJZnrqVdTrgshGpXgRMhBY6zyiClbnto8NDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=kfJzraNLr4z7iv-5NiCPK83lZkTy_pR468lNqICl5TBGk94mkZWASDaBttNY0fxfIxDPiMGN0cTsbPl7zDf246qDubxIduReZ3gQotROssKiHrweHGSS2nt8bBs2B4REBCLrpdxxHuYI6D9beZFWpbC870V4MuOapmEQLll75XfpSNkuowCKBvq5IYpAWpt1EmYNx1kHSKuSnvZBI0UtIlcTinjdwqP7t7YVJWtEnZcftDfBqm1KADstXQttEpF6WZwrG3QdEWy6C8yx4dq-FqjsRmTpJnyxqVFGy_t88CWMxS2801LrzCaTA-vZL2DSbyHzzS2dXynYjBidz89h722SjaTQtrcTC5I4hf2gKICE-P0sY_AFpSjLSm1sXM1y8h0ERS7WCQENp3fHO4jt7Tf14NLDtTZEqKgkH671CUE5SsfgLzgUN5S1a91ibB2HF2mDLPmTp53SXnjxuqu5N7gQDyRrD1jK1EorLB0N2mXXLQkrHSx4ejJvicibhxq_D0wEXCElqx_r4yhH_G2cUlMFsIsbOx-fXNF866msaz93nPwcroL2opALaQ5DNYeBdRWF-KPIbJWjkf18LKIr2FftWYi36ZaDoOh3GFHCLnIc2P54BTaGrFvEQeOlTllgeGfFqPLrJZnrqVdTrgshGpXgRMhBY6zyiClbnto8NDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور بیژن مرتضوی و همسرش در دربند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150913" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkVha8_GWs6ZG7Tz3mKlOmje8YvmCv1b4oWqkzdfxAv4ZltWQpI--8-M9x2K-H0tc86PTRJbsfE741_PgM3YmEo9ZVoam2kxU3flWwHQgOb6rKULilZL1Hl8h155WV93EIldIB6i5uUfROpShx6WUc56z_eoWRE71bOnkPJyEVlQUCo1wW-dEX1t7pc9WHeNYVsLhz7qMquxLmIbNAlRdJ5C54yHFbloqCXj_IDRDhISKV4XaPc3okbPBwNIq3UCN3RifIik8oEdpBEBET8HMRB8HOdEE0A9z70UFa6wJBjxFKe9CMs4PPFRCSBhzk27VUOJLBdC3uA_wUP3BzQKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای حوثی به منطقه العزاعز، نزدیک تربه، رسیده‌اند و در حال درگیری با نیروهای وفادار به عربستان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/150911" target="_blank">📅 14:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
قسمت ترسناک ماجرا اینه که با وجود خبر تزریق بانک مرکزی و جو امنیتی و بستن صرافی ها و عدم نمایش قیمت، بازار بدون واکنش به مسیرش ادامه داده
🔴
قبلا این کارا یه مدتی موثر بود...
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150910" target="_blank">📅 14:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: بحث خروج ایران از NPT بسیار جدی است و در محافل سیاسی کشور مطرح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150909" target="_blank">📅 14:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
نایب رئیس مجلس، حاجی بابایی :
هیچ‌وقت مذاکرات ما با آمریکایی‌ها موفقیت‌آمیز نبوده و دلیل آن این است که آمریکایی‌ها صادقانه با ما مذاکره نمی‌کنند.
🔴
هیچ‌وقت ما با آمریکا به تفاهم نخواهیم رسید
🔴
اکنون در واقع مذاکرات با آمریکا در حال انجام است
🔴
برای اینکه به یک جمع‌بندی برسیم، لازمه آن این است که از یک قدرت بالا برخوردار باشیم
🔴
تا وقتی ما از موضع قدرت و اقتدار با آمریکا حرف نزنیم، آمریکا همین روند خودش را ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/150908" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9J5jp2vakHWlqykC4eTzUbPXZ-WTSbzpwVg5w2HXCC-epDSNyE8_vACXW8E0PgOTjxsQnAWjpLHdKfa6SgMNgQVGr1Qxzqza71HYM93bGyrETFqBqT0n4wyH0UhbeEfN9JR5C0Z_tDkzin3RjQPhAVBP8tdI_0wEJ4jGbJPNuDqjRUYcD8S-WhkRD2kcEn-xT3-8AFaYb7kOu--U__C6prxjmpDQ1uNGzODuJgxV4N9KkL4JvX94FHR22EvwZ5PllY2NBy257-Vn34APY7aFEtSgDiT9SrNEN9lowkNi2ZnkgpiX1nrOSIz-hDQsrskTzmU6dqlQzDo-dCXrKjQeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی: حملات به پالایشگاه‌های روسیه را افزایش می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150907" target="_blank">📅 13:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سخنگوی ارتش: برد موشک‌هایمان‌ را افزایش خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/150906" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حادثه‌ برای هواپیمای اماراتی در پرواز دبی-استانبول
🔴
حین یک پرواز شرکت هواپیمایی امارات از دبی به استانبول، ناگهان آب از سقف هواپیما سرازیر شد.
🔴
نکته قابل‌ توجه این بود که آب دقیقا از محل قرارگیری تابلوی خروجی در داخل کابین می‌چکید.
🔴
برخی مسافران برای در امان ماندن از ریزش آب مجبور شدند پتو روی سر خود بکشند در حالی که خدمه پرواز در صندلی‌های خود نشسته بودند.
🔴
هواپیمایی امارات علت این حادثه را تجمع بیش ‌ازحد آب اضافی اعلام کرد.
🔴
با وجود این حادثه پرواز توانست پس از حدود چهار ساعت به مقصد برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150905" target="_blank">📅 13:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قیمت دلار به 272,500 تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150904" target="_blank">📅 13:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
منابع عربی از توقف فعالیت‌ در فرودگاه بین‌المللی طائف در عربستان سعودی خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150903" target="_blank">📅 13:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ما و کشورهای غربی باید در نظر داشته باشیم که همسایگان ابدی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150902" target="_blank">📅 13:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8d1fjnYqqndSmXgoMu0NXa_E4cSJF9oD-pO6Z0QCtzRQ9-WO24ecixByl7hEtYP_gSVMHSOAq1aIRKfJ_jI2wWTAJhCUgQWA_87MoR8_wlgvzRPwrwTflgouVVOmEgRVodLi-F6-IpKuM9GNkFWvNRWq5urrmGaBxB94gS_wpUO3OQkdH4ZGJdAJDSxTHmRzBCJWDleyMtj0uymoMM6zZlpTWGEMUtlhFy9q_MqzyMsOCAdAKdezDrJdkM5luykIvDdGfn-w-DdmBhLSO6Y5Ldo3vrx2IqstOl1OWc7BD4Em0GPxBlS1ZI9S5Bsa8lfPJiNbB74doWtOaFUU6OZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نظامی سعودی در منطقه بنی بکاری، واقع در کوه حبشی، غرب شهر تعز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/150901" target="_blank">📅 12:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EysiYdyWZQIiHhqSNDI24bQmTIXckPOwacmgELMz2ENSoo2BcE-kds3XqkEg-V6b4dJ-WMm6idDU-5d3xL1TfSQHgCjIKy_biKm9QHZ1ZBPuCV_0fAYXk4SUEaCnmBIJo-1TUmO-D2iL7bSHj55iHhjN6vLqqL-ChugYu7te7z2JEzU3bvP007xALAcXaJpn_oPnNq0VSbvY0UR5Qbsr1KCSJMc1bac5j7Y3kivXwUU7UlpFjWQ7sEsaN5T85gBBkXTgcWEL5h5CPMaUfIP-ZnvDeY9DPSlqhOXUQ2DcWDfCyLIUfy7qRohNlW_unsw3DrmnBCdzrnSAVG-K1pxmpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز تهران _ نجف که قبل از محاصره هوایی ۷ تا ۱۱ تومان بود ، دوباره برقرار شده اما ۴ برابر رفته رو قیمت و شده ۳۰ تا ۳۸ میلیون!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/150900" target="_blank">📅 12:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شوک تازه برای رانندگان؛ قیمت باتری خودرو تا ۲۹ میلیون تومان رسید!!
🔴
قیمت باتری خودرو در فهرست منتشرشده برای 12 مهر ۱۴۰۵، از چهار میلیون و ۹۰۰ هزار تومان آغاز می‌شود و در مدل‌های پرظرفیت به بیش از ۲۹ میلیون تومان می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150899" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150898" target="_blank">📅 12:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ec665133.mp4?token=dMqlQRqrBT85tseeCwHVmFoluBmYWW1Gb_pvZM0gaAciTqCn4rfsSn7Ishozsq1AvNo1F8TdBQOukzNQd8mfUVe3uZYsbOl65qhIBhjMafj_MpH49SKondz2mYaRaAfBZVJpjjmCitCeDDuNTkgZJFQfMxD1cgqc1d_z9ggSGrVCSVQNRpzckpnxi1fStBbj9nRc-NIgAQOgS3yjrTRm6nvTPH8hg9hASA4p8fFFZd6XI3MDSjGvlhgd9UB6QTDOmjnPW-iEyYLtMLLRiDnCEJt0RQBKaNCZsIfZTSEXquWMM-xQ1m2IVk1yOft7nwdCiVuC28eqQCU1vf-WrGI2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ec665133.mp4?token=dMqlQRqrBT85tseeCwHVmFoluBmYWW1Gb_pvZM0gaAciTqCn4rfsSn7Ishozsq1AvNo1F8TdBQOukzNQd8mfUVe3uZYsbOl65qhIBhjMafj_MpH49SKondz2mYaRaAfBZVJpjjmCitCeDDuNTkgZJFQfMxD1cgqc1d_z9ggSGrVCSVQNRpzckpnxi1fStBbj9nRc-NIgAQOgS3yjrTRm6nvTPH8hg9hASA4p8fFFZd6XI3MDSjGvlhgd9UB6QTDOmjnPW-iEyYLtMLLRiDnCEJt0RQBKaNCZsIfZTSEXquWMM-xQ1m2IVk1yOft7nwdCiVuC28eqQCU1vf-WrGI2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌های مداومی در پالایشگاه آرامکو در ریاض رخ می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150897" target="_blank">📅 12:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh3K_u67nXF8IByHQR9G9z53bPpnN8QFVDUk-WYk5yCUp5vmleclzuRHN33vN9x2EGy9A8OkIkB-rFuRvmWJ_mUI-u_iAIyISFGB12A_5ilQ_BLNhdIudKwCmpn0j8_6awfDTTeD7iPVRvCKjIXhSs_RvYKuvXSq7BV2QW_v3w74YC81di8Ni2xZvhBRcQz993JaMXG6l-lvSAEDLKVyp-Dg0nQDNFN8mUwu9ZKi-m6v3R4zST4UnmlEObgwXiPjreKjsKZosCwSX-zSErHf6J4riEW1UODxhd0-PjXUQIZQVfJx-tGf1NmHZ4WuZya3QwTk4RG950oPIETYQSUEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس جنجالی از بنایی در ترکیه؛ شباهت عجیب به آرامگاه خیام در نیشابور
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150896" target="_blank">📅 12:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/631cd6d323.mp4?token=mYRtob7BvlCkMs5gUxj5IBVNXDd7TslCoJUZBllMtx5Enlba80I8Tv4P7-AzDGCEav4fBUJ1lWDu0OuuYWaJB0-gzdxV-0xC92uPcsHBQgBM9V2AF6CJ0iFMnG7oBO2cBleDVPGZafWkVQPEHfWHISs2OKWDz51SpinXG9KQ5GdsP1dV_MnaH1vcUzZdjVkeI24T1Kt20XUNBs84jmYZ5wSdElXC735IaywZI60StboqKwmToNG08VEJvW5G183sMejaVedgz9u4lQEo5Ik8OsX12w6QmJLDnW27QgNXZHGeLaziJo8XAb4_HYMVMbGSg6MofJd4T_EvvWh9wqHqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/631cd6d323.mp4?token=mYRtob7BvlCkMs5gUxj5IBVNXDd7TslCoJUZBllMtx5Enlba80I8Tv4P7-AzDGCEav4fBUJ1lWDu0OuuYWaJB0-gzdxV-0xC92uPcsHBQgBM9V2AF6CJ0iFMnG7oBO2cBleDVPGZafWkVQPEHfWHISs2OKWDz51SpinXG9KQ5GdsP1dV_MnaH1vcUzZdjVkeI24T1Kt20XUNBs84jmYZ5wSdElXC735IaywZI60StboqKwmToNG08VEJvW5G183sMejaVedgz9u4lQEo5Ik8OsX12w6QmJLDnW27QgNXZHGeLaziJo8XAb4_HYMVMbGSg6MofJd4T_EvvWh9wqHqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای حوثی به پیشروی خود ادامه می‌دهند، پس از اینکه کنترل دره البرکانی را به دست گرفتند، و به منزل رئیس مجلس نمایندگان وابسته به عربستان سعودی رسیده‌اند، در حالی که درگیری‌ها همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150895" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
رئیس هیئت‌مدیره صنعت برق:
احتمال خاموشی در زمستان به دلیل کمبود گاز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150894" target="_blank">📅 12:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مجری شبکه ۱۴ عبری:
ما او [خامنه‌ای] را کشتیم اما هزینه خاصی پرداخت نکردیم او که مرکز رنج ما بود، درست وسط تهران ترور شد در حالی که فکر می‌کردیم ایران کار دیوانه واری کند تنها 40 روز جنگید و سپس به توقف جنگ رضایت داد، 2 دهه ترس از پاسخ ایران در صورت ترور خامنه ای اشتباه بود، ایران اراده لازم برای انجام کارهای دیوانه وار ندارد فکر می‌کردیم حداقل کاری که ایران کند خروج از NPT باشد اما این کار را نکرد به هر حال باید از نخست وزیر شجاع خود بی‌بی نتانیاهو تشکرکنیم، زیرا او بود که ریسک کرد و پیروز شد، نصرالله، خامنه ای، فرماندهان نظامی ایرانی و دانشمندان آنها را کشتیم و پاسخ تنها چند موشک بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150893" target="_blank">📅 12:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بقایی: امیدوارم خبر اعزام ۴۰ هزار نیروی پاکستانی به عربستان شایعه باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150892" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
بقایی: اگر در آینده باز هم شاهد حمله به ایران از خاک کشورهای همسایه باشیم قطعا به شیوه‌ای متفاوت پاسخ داده خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150891" target="_blank">📅 11:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150888">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=evDhAfgEghMSgK8qU92KY2Oa7ZfBlDTTSem-6tg783rzczBLwl1frcEUiyBBHHOodk_L9Kc_q3Dbnxmdf9z8FEP9fxv1GwF6T_7giqzzCaID785drSK8vC465qZhp7Lh9cUrn8qU6wUZELB4wzbvp5DfRzFcZqpYVBWul1ITRySbqFVMVZq6bhfkM97Z_T8eGfLd589_C71eTc6B78ZOqAr4SmkIdqHJ_uLyxGhd1d4dx6GWJbAbuvlDJFU6sgyAo5k3_6NE5Ud-Ya9SKohhefdZTWBcmeEpZpWCtbSRbqVXSBnC9DUxorGrBtK0Y5t5eUOthLVheUX5Yt7pL9bRpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd3dfb4ffd.mp4?token=evDhAfgEghMSgK8qU92KY2Oa7ZfBlDTTSem-6tg783rzczBLwl1frcEUiyBBHHOodk_L9Kc_q3Dbnxmdf9z8FEP9fxv1GwF6T_7giqzzCaID785drSK8vC465qZhp7Lh9cUrn8qU6wUZELB4wzbvp5DfRzFcZqpYVBWul1ITRySbqFVMVZq6bhfkM97Z_T8eGfLd589_C71eTc6B78ZOqAr4SmkIdqHJ_uLyxGhd1d4dx6GWJbAbuvlDJFU6sgyAo5k3_6NE5Ud-Ya9SKohhefdZTWBcmeEpZpWCtbSRbqVXSBnC9DUxorGrBtK0Y5t5eUOthLVheUX5Yt7pL9bRpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارش باران و سیلاب شدیدی که توی شهر ایذه، واقع در استان خوزستان رخ داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150888" target="_blank">📅 11:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150887">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: پزشکیان در روزهای آینده به ترکمنستان می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150887" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150886">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: در مذاکرات ما به موضوع هسته‌ای ورود نکردیم
🔴
ما فقط شروط ایران را به آمریکا ابلاغ کردیم
🔴
ادعاهای مربوط به موافقت ایران با بازرسی‌های آژانس بی‌اساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150886" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b636ea50a8.mp4?token=aL4UkdVlh9_XNRXLQK01tRCeW0Ell_10mATqsm8X2FIee__pjDN400BYc_8UcZOIZhezW6_bNJIiH_Qq4EzffqcbepKuuYOJimdV7k7YMQDibWyYv4sTplFvQlIvRHKlo6PBcINlLYUp0zwVaMK-o4Umm65qT6flpXtomUgLjplXdfWWqZ1sExYPG5KVTgMfEZKP0GeDZHSMfoeF9NpPFDb4Am6_W9UxKRdFUMoFkNpNNwLSxWov0v-qre-odGis8HkbRJnRmT-3_OxyBZbSTVIgACRbRhcVCFAr2k8imJu8TMGFQjB8ibl6QF-m5Tmo5wpyiDhIxtnF10XZjDmSxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b636ea50a8.mp4?token=aL4UkdVlh9_XNRXLQK01tRCeW0Ell_10mATqsm8X2FIee__pjDN400BYc_8UcZOIZhezW6_bNJIiH_Qq4EzffqcbepKuuYOJimdV7k7YMQDibWyYv4sTplFvQlIvRHKlo6PBcINlLYUp0zwVaMK-o4Umm65qT6flpXtomUgLjplXdfWWqZ1sExYPG5KVTgMfEZKP0GeDZHSMfoeF9NpPFDb4Am6_W9UxKRdFUMoFkNpNNwLSxWov0v-qre-odGis8HkbRJnRmT-3_OxyBZbSTVIgACRbRhcVCFAr2k8imJu8TMGFQjB8ibl6QF-m5Tmo5wpyiDhIxtnF10XZjDmSxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله موشکی روسیه به پل مهم کی‌یف
🔴
پل شمالی کی‌یف، یکی از مسیرهای مهم ارتباطی پایتخت اوکراین که بر فراز رودخانه دنیپر قرار دارد، هدف حمله موشکی روسیه قرار گرفت.
🔴
این پل از مسیرهای مهم تردد میان بخش‌های مختلف شهر به شمار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150884" target="_blank">📅 11:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بقائی: کمیته ۶ نفره شورای عالی امنیت ملی پرونده مذاکرات را هدایت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150883" target="_blank">📅 11:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150882">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رویترز: ناو «جورج. اچ. دبلیو. بوش» با ۴۸۰۰ سرنشین خود وارد جزیره تفریحی پوکت در تایلند شد تا پس از شش ماه پشتیبانی از عملیات‌های آمریکا در خاورمیانه، تجدید قوا و استراحت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150882" target="_blank">📅 11:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150881">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkAonu5ZXwhPuGGzYIu_3j4scLuI1P7HYEpK00sDrS3oRdQdwdXiJnt0JWRt4-kTXvjSFI2DI8lZNsbmGKz13pQiHxNYIPSX6DCQO-pJDj3-W-r1X-X8oUybKwZR3F1sKJWH2fx6gJRvUKflp5dOh8nSKckGFX83EOCLjqrmOqZbuBq4lcLJJvf2mKheIf-PMFwlCuspMUAhCNRAv4w49nVVgQzcKAlkJWoxIcMsBLIKG5phUaAyoaMklvkcZbO-FDYO0ZbS1gKxDPMC_Ufpch5RLMkB5EfBJQnlLfaH2DD1SA-c8nK-Y52NwmI3zdCcB0gc-6eZcA8tI2patmxY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران‌خودرو قراره ماشین جدید خودش رو به اسم «پژو 207 الیت» تولید کنه و با یه قیمت نجومی بکنه تو کون ملت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150881" target="_blank">📅 11:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150880">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219d012c04.mp4?token=tPUhU1v1wllw25YMx_4G-CyzxjIjF5uaSElC4L1sl_UVOtA-e6T676Asfsdcn7C7q3-0MKvzGeBNjyX5U2k8qczv0qVVnChW7BAfL9ryisEskWeygHRecQrfW5sEWHlLaDeM_Jb57y0rfX0vnzL6UdVRnJqX8gVBxRxtyjtwv_iEfxxZA3dD557dlugWgo3NgPilFi_BjlIhP2jYYjtvHfHElStxmr-sxEfqfMkeU2-6SeonUDovL2knxjiJ9qdR-g7RGCZdoSugdsYo3e8-giydD37eAmhUkV50Y3xE75i1GraSFjddfVEAuir1w80J8QYee-STHCocWJC8U-z2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219d012c04.mp4?token=tPUhU1v1wllw25YMx_4G-CyzxjIjF5uaSElC4L1sl_UVOtA-e6T676Asfsdcn7C7q3-0MKvzGeBNjyX5U2k8qczv0qVVnChW7BAfL9ryisEskWeygHRecQrfW5sEWHlLaDeM_Jb57y0rfX0vnzL6UdVRnJqX8gVBxRxtyjtwv_iEfxxZA3dD557dlugWgo3NgPilFi_BjlIhP2jYYjtvHfHElStxmr-sxEfqfMkeU2-6SeonUDovL2knxjiJ9qdR-g7RGCZdoSugdsYo3e8-giydD37eAmhUkV50Y3xE75i1GraSFjddfVEAuir1w80J8QYee-STHCocWJC8U-z2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار هم اکنون 271000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150880" target="_blank">📅 11:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150879">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQJuVOvK-vNpiZEsFHWIokp72x90Lmu-U2DyM_7bGS7lLKWubI38l-UvPaHV3o35gX9JpyxlwmgoP8H5obGQDNJz171h8Vgi2_GkmPrEJWbGD1NwD2u-hD_VzOhq8z7YQ1OUFNblNYtpnxSkg7INcIuPHTmZm7W3zYIPGe2xFJicK1L7YO6cvL_01V8RmPQkCbTuVO9tmPduSYVkNw4SJWA6Jg7bvPWl6V9LjQvv3g-uzY6dKR0Ik5QS-zAoXNnqz-_yY_3w5AvR2Lpkouby8-7TwKEnz0cqdR9EdJ3XTYawsyUnI6bFxPZghBJLz-BzOZxRpK09Dc7RjbQw5LO8-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان دریایی بریتانیا گزارشی درباره وقوع حمله‌ای در تنگه هرمز دریافت کرده است.
🔴
بر اساس این گزارش، ناخدای یک نفتکش اعلام کرده که کشتی بر اثر اصابت یک پرتابه ناشناس آسیب دیده و اتاق موتورخانه آن دچار خسارت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150879" target="_blank">📅 11:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150878">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
دلار به 271,000 تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150878" target="_blank">📅 11:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150877">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
عراقچی: بیش از ۵۰۰۰ جنگنده آمریکایی برای حمله به ایران از پایگاه‌های اروپایی بلند شدند اما پیشنهاد ما به آنها برقراری گفت‌وگو با ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150877" target="_blank">📅 11:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baeeb81cb5.mp4?token=NlI20ejBhdPiOe3jOTx189zDOWOCgNj3RrquOGbHETki6cr5rN1Yz7KN0SnvdTYfY3dA9fWjKfIRuomXJBjc6ZWBKj9KkP5DrvSgkX8vOACt6hZl1yoyDGY0zQ2eMzsHVrFiH1X1tyxX3-2JKDFrhJs9zL4m7KSfHly152at1Y8253-SeU78AsF3tN6dYW9SgSlpynE0ssGl4V5miYIcL_UWxRuU39OPAXz299Wbj56o6SjQ5A0EBb96h1zF7SW9Y2_EQmwZ7oi3wR7OGrhYleClWCiNu4yUiFK_dfNSKMF21lRc6aC29hhpnYFnvEUs8afgXfz3H_ure2z3HdCJbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baeeb81cb5.mp4?token=NlI20ejBhdPiOe3jOTx189zDOWOCgNj3RrquOGbHETki6cr5rN1Yz7KN0SnvdTYfY3dA9fWjKfIRuomXJBjc6ZWBKj9KkP5DrvSgkX8vOACt6hZl1yoyDGY0zQ2eMzsHVrFiH1X1tyxX3-2JKDFrhJs9zL4m7KSfHly152at1Y8253-SeU78AsF3tN6dYW9SgSlpynE0ssGl4V5miYIcL_UWxRuU39OPAXz299Wbj56o6SjQ5A0EBb96h1zF7SW9Y2_EQmwZ7oi3wR7OGrhYleClWCiNu4yUiFK_dfNSKMF21lRc6aC29hhpnYFnvEUs8afgXfz3H_ure2z3HdCJbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در پاساژ خلیج فارس عسلویه
🔴
مدیرکل مدیریت بحران استانداری بوشهر: از ساعت ۵ صبح امروز، مجتمع تجاری خلیج فارس در شهرستان عسلویه دچار حریق شده است.
🔴
بررسی‌های اولیه حاکی از آن است که اتصال سیم‌ برق عامل شروع این آتش‌سوزی بوده و شدت حریق به دلیل سرایت شعله‌ها افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150875" target="_blank">📅 11:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az1DwErC0A3SqXmniQguJVbzz2FSHYy8Wd-eN0DUEvVztKIsFkAKwqhd6AVz4_3R_UZo5cJV5Gu50z8fDhCo3hO6Vx2rmDL5hgyEWH1awPqABOlF5iYdpT9Qds6HkNbrxfGEQubN94MgaMiXbhgiFCWjKX19qH1qwX4V14gg7txdidbBH3e9rjkabuR7CJEChlHtAybWdzGqU2zR3-di0CJt9VBdKiLZLKrNamu48Q5kTZv7Zap55di0SkKzsXgM5FlekoskLGctDJ8KSqGN1y3-T4r35EiCdW980jrZBegS6Zq33VeZ_QX4FwFOHc6I0PW3E3LqBfrGRqTu4hjxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماهواره‌ها، دمای بسیار بالایی را در منطقه نفتی خریص، واقع در پایتخت عربستان سعودی، ریاض، در ساعات اولیه صبح امروز ثبت کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/150874" target="_blank">📅 11:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روزنامه یدیعوت احرونوت: یک نگهبان امنیتی سابق در دادگاه بئر السبع به سه سال حبس محکوم شد، زیرا حدود دو سال پیش با یک مامور اطلاعاتی ایرانی ارتباط برقرار کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/150873" target="_blank">📅 11:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgf4-IzGsnp1VEetBoSg79C3_yUH4DaVlJQ8ulX3MFzCJmHM9kkOjkC9rJWeo8Ow6uOdcX_UB260VUBFUQf0l8w4vsIIaOC8FpYENQWtA8MTima4wmo-JJpm3t1Qt8VplKe4ufM-3Kc8h0DGTQhIrFVcZ7TvHfJNWHjSJ4QKgQ7PJakH4mY4haoYgsmwmTUwuPhsnJDnnkMgfkkJY0YM_E3EjW-wOHXOZzHCr_Pjz3U11UmXD0tb2O7fBHissU7zJqgZH5q6aOkUMjxmeNIcMT5AFz9NpmIO_-vaUmKyqJLBHwnt_tSXXWRlF8UtRGtSUcowK39XUbfyXky1oVquow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسامی جدید تو تهران
🔴
میدان نوبنیاد=شمخانی
🔴
بلوار دریا=تنگسیری
🔴
خیابان ارم=خرازی
🔴
یه بزرگراه جدید=موسوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/150872" target="_blank">📅 11:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
قالیباف: در خصوص استیضاح وزیر کار تصمیم‌گیری می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150871" target="_blank">📅 10:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عراقچی: هیات ایرانی از آمریکا اخراج نشد، ما طبق برنامه از پیش تعیین‌شده خودمان رفتیم و برگشتیم
🔴
همه شروط ایران برای بازگشایی تنگه هرمز منطبق با تعهداتی هست که آمریکا باید بپذیرد
🔴
امیدواریم که آمریکا راه خرد و عقلانیت را اتخاذ کند، هیچ راه‌حل نظامی و راه‌حل مبتنی بر تحریم‌های بیشتر وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150870" target="_blank">📅 10:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68bfbde948.mp4?token=m2HiseqFkhGvBtHe2L6frcJpxDqkjCpvxg1rkGostZQSN3Cf_peQo6rWXUpPh1LZ_it4xo9PJzPXcMF9DOrJ6jX1wbkdf2DWp1ZmWqmQJa6XQkzVhIAWtehu0uZaxYPuFF54BfCIvnd_ebS1M21gOsB2J7o19oq0ybKQ1DUe4qJl3liDH19LWr14aFzd8sG7iD8bgw436ZTvnRqviqHIg0A2gxHZK_qELjoN3oarZ9PXWxTvPgUaiJ6lhQwHUCr6p8R0UgrIK8I-akLmAZXOKF4celeSpX361q0OGXjkSTHrmpB5n5Lmaub3PYqay_n-qFuYDxixlHISgMgvL8Nh0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68bfbde948.mp4?token=m2HiseqFkhGvBtHe2L6frcJpxDqkjCpvxg1rkGostZQSN3Cf_peQo6rWXUpPh1LZ_it4xo9PJzPXcMF9DOrJ6jX1wbkdf2DWp1ZmWqmQJa6XQkzVhIAWtehu0uZaxYPuFF54BfCIvnd_ebS1M21gOsB2J7o19oq0ybKQ1DUe4qJl3liDH19LWr14aFzd8sG7iD8bgw436ZTvnRqviqHIg0A2gxHZK_qELjoN3oarZ9PXWxTvPgUaiJ6lhQwHUCr6p8R0UgrIK8I-akLmAZXOKF4celeSpX361q0OGXjkSTHrmpB5n5Lmaub3PYqay_n-qFuYDxixlHISgMgvL8Nh0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: از امروز خنکیِ دما در تهران کاملا حس خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150869" target="_blank">📅 10:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
عراقچی:‌ اگر ‌آمریکایی ها مجدداً به سمت راه‌حل‌های نظامی پیش روند ما آماده‌تر از گذشته هستیم
🔴
برای دفاع از خودمان هر اقدامی که لازم باشد انجام خواهیم داد؛ اگر راه دیپلماسی را انتخاب کنند، ما همچنان آماده هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/150867" target="_blank">📅 10:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gxiyr_p0oFCaTulFQlRLYsTaJFhm_cILZi3t04uyFviFK3RsH5sN6z1vHJwbgwvtxxCPYNDiNuWtCIZEhZR-oRq1Stiwl3m0BW-1O4y3J90CO2UTR1A1dyxnXDh2pDjflIJ43T3bHSxy0vOYQe_drlZdsRKX1gEr4NZ4h3pmH2_G-O38jPZSiqO7yBIdugwZvxn9oaQmDsntQnVwKx6b8zgbJmS0wkKwfA1AjzS1XZp-7TaRDEcMal68tjvE42R3p6l8gpoKvnfwVYmytpCzLbPrLDWscWdYV_aEG1ce7kytBHB5HPQJmNTHAQnsArt1l6Ugbc22q-R2UKLimKa40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: کل پایگاه‌های آمریکا تو منطقه نابود شده، من خبر دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150866" target="_blank">📅 10:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150865">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
عراقچی: حضور هیئت جمهوری اسلامی ایران در نیویورک امسال یک حضور بسیار قوی و بسیار موثر بود
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/150865" target="_blank">📅 10:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150864">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/v3VWnBEOemf3NjFCFy8upxxXysY_iF3Mp1CP6zSAK8IhbhqW66jqPdM5aeBermPilx89k8L_jn4UBEENCUn5Mcyjs7-tv4ItLyN2YFzVB4l-aSiFLfytg7STyYKMSF7aszSKIq2hmaWTJaVcKvvv2pCTCJRFDBp7mQl7qyw-en8DBbpJpg_6SfZ2P4CMmoeyNtUbTqxNyrRyus0yNBfJqvn4EcYqi4pWdc2JmgJvzhwhrXaLfdUjA_QkgRScFkFFSyEsws_uKBah2m6kjG8zgDXL-x56W3LIFfkk3GqTKvAR-1OgzPKMj5iXsextg9yJQYE19CQV10yI91PcIZsG7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای انصارالله (حوثی‌ها) به تقاطع الصفیه، السمسارا و کوه سمدان رسیده‌اند و با قطع آخرین مسیر تدارکاتی نیروهای همسو با عربستان در محور تعز–التربه–عدن، در حال پیشروی به سمت العزاز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150864" target="_blank">📅 10:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
الجزیره:میانجی قطری یه سری پیشنهاد برای نزدیک‌تر شدن مواضع دو طرف مطرح کرده. تهران هم الان داره این پیشنهادها رو تو شورای عالی امنیت ملی بررسی می‌کنه.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/150863" target="_blank">📅 10:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nmcn-8Wtc8w_d2XE8lIteN5PpcF5Cg1u1MXOwYIjj3yp1rsju5JOBiQEVtyVE9BVKuEj9O3DFxbbTATpH7d3lwzV9HWwL62Kn0sH78OuLGhzDFY_gxAwMci0HSNSxsYGXd9Jsf88RyoBfQvlgwyK_30iJ7LclrvVUemn7HlgAtqfeAEA8pPPReWcPzsaF_uDq01bV4DfAkYfL4hYBKvIZnQGqw6fuAx9idBFYHdnc1pI34HmB1i0xnyAXzkM1u8xg-jIxzwFBYRrlJNeBuj-_F5-CgoCMqf0JHpBW1irISHYt9kvmtHgpXX-4dzWVOW0dWeWwiisB5MVwLpTYcM44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای نظامی فرانسوی مدل A400M در پایگاه العدید در قطر فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150862" target="_blank">📅 10:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9890ea86f5.mp4?token=O-qgoIUYxOqbuQYyzKb2wPz5ZY14fN_v0G2HrkkZR7hLhi5xoNkzlO1UlaRddLqgpM3ZNCp04C3rDwXMgqNwAENxK7VYJh33saW62qr7f7WNtDz55zypZhEvN_Uma-9pjqe1BgPyoDaQEU6lfsfBqdYZ8MVkpzvfFQuMtQutZL6M6OaK1v1dulBzVa-PJLDUUz5BDIS5eqWOsxe5ZBBiKmKDK0dNdlaDFoGQ_YNPmix_SQop5atzYeutCqlc4xZbNGDxdFjsyRKGjoAHql4LpN3mJeP6FnYSZj6f_NQwp5uZXfa-QF9lonFgzrwpc1iJvwZx8kCQp_mgX9aKG2fopg20b0dAhXZ8Yw4S-wD0mw0zwEebUY4Ic3D_k1x9nulAzleHJjtGTqa2qxWhzZiRACGKy_XTYwBizmaCn_60y6mNQLAb_m3HoquG5jnYgEzpgFeIfTTb5DAlChRB6_VDn55EGke017NH7yp9gh_96IKIAM3Zh9hMdcIyJ_dcE6s9G9K-DyPKuWSYyFcEWJBwa0n3hVIaT6PtdroalZnAdA5QwFzdeweviivq25Iiz3rbwqZjSFmKqaXQi7qkpyhNgCxs_3dD0PMgQZ1ZOxX8M5MCrw-vwjCU6Z7H8Ua_BRsR9xglwZExBrcj1kGddWJqgrZXK3p5psoubmbMy2uSYl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9890ea86f5.mp4?token=O-qgoIUYxOqbuQYyzKb2wPz5ZY14fN_v0G2HrkkZR7hLhi5xoNkzlO1UlaRddLqgpM3ZNCp04C3rDwXMgqNwAENxK7VYJh33saW62qr7f7WNtDz55zypZhEvN_Uma-9pjqe1BgPyoDaQEU6lfsfBqdYZ8MVkpzvfFQuMtQutZL6M6OaK1v1dulBzVa-PJLDUUz5BDIS5eqWOsxe5ZBBiKmKDK0dNdlaDFoGQ_YNPmix_SQop5atzYeutCqlc4xZbNGDxdFjsyRKGjoAHql4LpN3mJeP6FnYSZj6f_NQwp5uZXfa-QF9lonFgzrwpc1iJvwZx8kCQp_mgX9aKG2fopg20b0dAhXZ8Yw4S-wD0mw0zwEebUY4Ic3D_k1x9nulAzleHJjtGTqa2qxWhzZiRACGKy_XTYwBizmaCn_60y6mNQLAb_m3HoquG5jnYgEzpgFeIfTTb5DAlChRB6_VDn55EGke017NH7yp9gh_96IKIAM3Zh9hMdcIyJ_dcE6s9G9K-DyPKuWSYyFcEWJBwa0n3hVIaT6PtdroalZnAdA5QwFzdeweviivq25Iiz3rbwqZjSFmKqaXQi7qkpyhNgCxs_3dD0PMgQZ1ZOxX8M5MCrw-vwjCU6Z7H8Ua_BRsR9xglwZExBrcj1kGddWJqgrZXK3p5psoubmbMy2uSYl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما یک طرح واقعاً عالی برای مراقبت‌های درمانی تصویب خواهیم کرد که پرداخت‌ها به شرکت‌های بزرگ بیمه را متوقف می‌کند و این پول را مستقیماً به خود شما می‌دهیم
🔴
این میلیاردها دلار را در اختیار شما قرار خواهیم داد تا بتوانید بیمه درمانی خودتان را خریداری کنید و حتی مقداری پول هم برایتان باقی بماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150861" target="_blank">📅 10:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150860">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b254466b.mp4?token=HiWRVRkv5G4aUDdvPSF0QyQmn5BeF_dU4l9hvvuj5O7gp9KJqy-d4v25UUZDU4XB0Q_0746XdBe_v0mJHMywG6WnBWFZlN8Tzf_GmqC6Z4oAp-iklBvSSSUzELUF3aaeZMyjyes8G2hdR-8MRSr_X30MThOojqf9baWyRNP1ZRKM-4ja-uLfaJe9Vg-F-Q_giRmwq_E3Ktk2prYOx74Ecl4t8Zls7s0G5DCCXPiaTbTbVqVzpbnIbhJW8r-xMPc5t8F2Wp_naHsLrKTET6kC57Y0b2RIh7QSOBdzR6Evqg0hRNfbZT9rKUjRA7nAnAcORvcPiJCUSHJwdRZdHDwQ9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b254466b.mp4?token=HiWRVRkv5G4aUDdvPSF0QyQmn5BeF_dU4l9hvvuj5O7gp9KJqy-d4v25UUZDU4XB0Q_0746XdBe_v0mJHMywG6WnBWFZlN8Tzf_GmqC6Z4oAp-iklBvSSSUzELUF3aaeZMyjyes8G2hdR-8MRSr_X30MThOojqf9baWyRNP1ZRKM-4ja-uLfaJe9Vg-F-Q_giRmwq_E3Ktk2prYOx74Ecl4t8Zls7s0G5DCCXPiaTbTbVqVzpbnIbhJW8r-xMPc5t8F2Wp_naHsLrKTET6kC57Y0b2RIh7QSOBdzR6Evqg0hRNfbZT9rKUjRA7nAnAcORvcPiJCUSHJwdRZdHDwQ9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما مجازات اعدام را برای قاچاقچیان عمده مواد مخدر، قاچاقچیان انسان و هر کسی که یک افسر پلیس یا مقام نیروهای انتظامی را به قتل برساند، تصویب خواهیم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150860" target="_blank">📅 10:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150859">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، درباره دموکرات‌ها: «آنها یک مشت حروم‌زاده‌های احمق هستند.»
🔴
«دموکرات‌ها به نفع بالاترین هزینه‌های انرژی در تاریخ آمریکا رأی دادند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/150859" target="_blank">📅 10:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150858">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قالیباف، رئیس مجلس: آمریکایی ها که در رسانه‌ها حرف دیگری می زنند، اخیراً  از طریق میانجی، پیشنهادهایی مطرح کرده اند. اما باید متوجه باشند که دوران فرسایش زمان و دیکته‌ کردن مطالبات یک‌طرفه  گذشته است و موضع ایران کاملاً شفاف و قطعیست و تا زمانی که هفت شرط ما بر اساس تفاهم نامه اسلام آباد، محقق نشود تنگه‌ی هرمز باز نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/150858" target="_blank">📅 10:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150857">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872a74a295.mp4?token=Zo1wM_9AqUMW-8p2LCjsr9cSE0tdQASs-DTCACLefi1gSre5gjb-tTtNQ6pp2xdx9XpoYqZZ86RFGtW7Vg413Hh6ozzVLzc6tLNA1rmMH6HpLxIQKYwJ79MUT49Ua5-UDLZw2uMcTQV-nTdasU_RDaaXexiWo1JpDc49zy3fXD1kwHZPCLKFfwSMJ1gWD_DjAQtZ_pFcTcUjCXhEErJ9qdXKu8Fe8VO6VLDpN3OnWR-DE42WVh71lu-Ef47aC9P1pFkTsPr_PfC14i-O6Etefq9TAxStTaXIX1JwlH2N08mkxiwL64RQ4aXSlgQ2W-PwXic-3YiIzQgqd1085xGKkDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872a74a295.mp4?token=Zo1wM_9AqUMW-8p2LCjsr9cSE0tdQASs-DTCACLefi1gSre5gjb-tTtNQ6pp2xdx9XpoYqZZ86RFGtW7Vg413Hh6ozzVLzc6tLNA1rmMH6HpLxIQKYwJ79MUT49Ua5-UDLZw2uMcTQV-nTdasU_RDaaXexiWo1JpDc49zy3fXD1kwHZPCLKFfwSMJ1gWD_DjAQtZ_pFcTcUjCXhEErJ9qdXKu8Fe8VO6VLDpN3OnWR-DE42WVh71lu-Ef47aC9P1pFkTsPr_PfC14i-O6Etefq9TAxStTaXIX1JwlH2N08mkxiwL64RQ4aXSlgQ2W-PwXic-3YiIzQgqd1085xGKkDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «یک نفر گفت: چرا او با شی [جین‌پینگ] خوب رفتار می‌کند؟ خب، آیا خوب نیست که با رهبران کشورهای بزرگ و هسته‌ای جهان روابط خوبی داشته باشیم؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/150857" target="_blank">📅 09:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150856">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae5e0e61f1.mp4?token=oDV4yG7uOd7YStusOB2shWkUwAk8vk5qIQCTAjKOHrjkh-_7mWyhfdDBG2mcgeq05pdpCA0P9jNU5hj1EN5NtuOuAy_gbbfpiM7bSkscfITVaaP2YCI0j7_zID0s_Qt_kR90vesZTPs8_K70HROJfBrmav3pvqBzjp7sHWXEsRyFAy6Xz26dcMJduUUU6OY0JEhUotc4bugFihl8FR3eB6S0FMF-RN9mEbuYw-sPuQa9YNfYMI7M2GjTV05XPxqM-gw_reSuWBFdrV3qogOezpRMDMezk9IqEzyVWJNtzTkAaNU2WGpSzY7AD0vy5Du8h3chELFiEbYfjdKeBQkL8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae5e0e61f1.mp4?token=oDV4yG7uOd7YStusOB2shWkUwAk8vk5qIQCTAjKOHrjkh-_7mWyhfdDBG2mcgeq05pdpCA0P9jNU5hj1EN5NtuOuAy_gbbfpiM7bSkscfITVaaP2YCI0j7_zID0s_Qt_kR90vesZTPs8_K70HROJfBrmav3pvqBzjp7sHWXEsRyFAy6Xz26dcMJduUUU6OY0JEhUotc4bugFihl8FR3eB6S0FMF-RN9mEbuYw-sPuQa9YNfYMI7M2GjTV05XPxqM-gw_reSuWBFdrV3qogOezpRMDMezk9IqEzyVWJNtzTkAaNU2WGpSzY7AD0vy5Du8h3chELFiEbYfjdKeBQkL8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اروپا می‌خواهد از ما الگوبرداری کند. همه می‌خواهند از ما الگوبرداری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/150856" target="_blank">📅 09:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150855">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/927804d2cc.mp4?token=j1IYeXnL8IrjRBiAwdQyhEUO9GzLZUI1OHEH3weaUagKj8Hj3FAy1-GI9NuS3Mt4dWcwFALjbiSPH8HgWxmvV2Wi8vVJpLopLnLpO0KPpl8dwVZi-PoDFK1YtdF414OLUbstlTR0defWiQfbBHmpZEgD7F_7PEmcNValHvjT-wV15a-oUSl_7HP4crKdWz-eOTaTaa_NjwFmcpJkKc78i7wy9s_4a5CIFGSnUrqNskusvQtDlMaYrms_YtsrLKrxIs8g8uk0n55Dl96LV8x79G8bghLRNeuiXK8ZA0x1QACKBqKnhvN4ghqO_fBppz2kWd1G0j23DO5ALe2b1jhAH24XWdyWwSQL5JWZvkvYC_sT2d6nXRdHjDPh-qiWA4WigjL5ghpAAC6VyBTn-b9x-JK4hSzNicE85skvKQq0wDPBHczTulx2znMe_Av1yCxAfgC7ztuHoOs37uIyRPXYMMb16ce-jcld-Mz1OluUI9QZ4vER4ut7TTr5sg79Ct2BWR5EDE2YSWsI8Zjd1a-Q9cmtDuqp6_tfTxXMpn5NNC3qMW_OZNP8kozcdPlMjkQuJR0OUMgiAeazFdsBI8mFj-8IqIZKNRi4g5kexCIJ0ry-CB5EvdpeMs1XlrAjVtgBXKqgUeHvlJ0CeHt1c1LIubW1kyjzbh5ofzKFcsqocN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/927804d2cc.mp4?token=j1IYeXnL8IrjRBiAwdQyhEUO9GzLZUI1OHEH3weaUagKj8Hj3FAy1-GI9NuS3Mt4dWcwFALjbiSPH8HgWxmvV2Wi8vVJpLopLnLpO0KPpl8dwVZi-PoDFK1YtdF414OLUbstlTR0defWiQfbBHmpZEgD7F_7PEmcNValHvjT-wV15a-oUSl_7HP4crKdWz-eOTaTaa_NjwFmcpJkKc78i7wy9s_4a5CIFGSnUrqNskusvQtDlMaYrms_YtsrLKrxIs8g8uk0n55Dl96LV8x79G8bghLRNeuiXK8ZA0x1QACKBqKnhvN4ghqO_fBppz2kWd1G0j23DO5ALe2b1jhAH24XWdyWwSQL5JWZvkvYC_sT2d6nXRdHjDPh-qiWA4WigjL5ghpAAC6VyBTn-b9x-JK4hSzNicE85skvKQq0wDPBHczTulx2znMe_Av1yCxAfgC7ztuHoOs37uIyRPXYMMb16ce-jcld-Mz1OluUI9QZ4vER4ut7TTr5sg79Ct2BWR5EDE2YSWsI8Zjd1a-Q9cmtDuqp6_tfTxXMpn5NNC3qMW_OZNP8kozcdPlMjkQuJR0OUMgiAeazFdsBI8mFj-8IqIZKNRi4g5kexCIJ0ry-CB5EvdpeMs1XlrAjVtgBXKqgUeHvlJ0CeHt1c1LIubW1kyjzbh5ofzKFcsqocN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «این دیگر بیش از حد پیروزی است. ما بیش از حد داریم پیروز می‌شویم؛ دیگر نمی‌توانم تحملش کنم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/150855" target="_blank">📅 09:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150854">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ : راستی، ما تقریباً هیچ تورمی نداریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/150854" target="_blank">📅 09:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150853">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7f0f9ea7.mp4?token=qXp4d4Z-DyEbC3xW_onZFjaLLtNsfSQalfWRToDpNR611ShPodzMgk9vpNz87paPMwQjbildDJ-TTo3d-VqbtCfuhgL7VJIjyfIAtyk-LAgs1mBjVb4sQ6IZTDrU-GNSnxAhGtwD0rWdZvaHCtl_DlTEOZov8xhKIMxzxulD4_SvR2sxHgyYSdDU4vr_LsuPaY5SN1Ih_vqXWgL21vOE7ZlGtmFWGRMlD7KpptI056RQfgogerPtn7eGqZ-Xs5UPxo-VO2Q7CaBc38076YgvU7VoG7ePdPDzB1WjjU9Att0ivEHbsHklWswhXTqHuk0X9qYQG9S_iI0lwmGEJug0Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7f0f9ea7.mp4?token=qXp4d4Z-DyEbC3xW_onZFjaLLtNsfSQalfWRToDpNR611ShPodzMgk9vpNz87paPMwQjbildDJ-TTo3d-VqbtCfuhgL7VJIjyfIAtyk-LAgs1mBjVb4sQ6IZTDrU-GNSnxAhGtwD0rWdZvaHCtl_DlTEOZov8xhKIMxzxulD4_SvR2sxHgyYSdDU4vr_LsuPaY5SN1Ih_vqXWgL21vOE7ZlGtmFWGRMlD7KpptI056RQfgogerPtn7eGqZ-Xs5UPxo-VO2Q7CaBc38076YgvU7VoG7ePdPDzB1WjjU9Att0ivEHbsHklWswhXTqHuk0X9qYQG9S_iI0lwmGEJug0Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا:
«فقط بروید و رأی بدهید. اگر این کار را انجام دهید، ما پیروز خواهیم شد، آن هم با اختلاف زیاد. و حسابی آنها را شکست خواهیم داد، متوجه شدید؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/150853" target="_blank">📅 09:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150852">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a8e2d39ac.mp4?token=lCgOgNtwSinP7qXEQKNDtQz_gAccT-7rK8602OI6l7P697W07Ti-C-W1h4lOVhl2bli_U5XOuKEW-7yMiJq3k9RB78xkrrmjkAjoxxagcK7Gx1_K4dGdvJcdTQ0VI6OCVb20o6bqfs5K7YHSInRuj8oTJaI5Nbq3MFcFjl3MQAkqqvCef7r8m6DRWnc5KHeHSU7dK-RsteYS08ZYf_vYCLK8HXsp2fTxG0f6Ihd8TA4dr87C7-p268L9cgN-OxoFcgMr8BksGzBzxsidmGxM2nHryPetryrx7SVMwS_arPBhI5dcTpXf32tsWgse3-sRXF7DorzB39YI19GFahJ8-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a8e2d39ac.mp4?token=lCgOgNtwSinP7qXEQKNDtQz_gAccT-7rK8602OI6l7P697W07Ti-C-W1h4lOVhl2bli_U5XOuKEW-7yMiJq3k9RB78xkrrmjkAjoxxagcK7Gx1_K4dGdvJcdTQ0VI6OCVb20o6bqfs5K7YHSInRuj8oTJaI5Nbq3MFcFjl3MQAkqqvCef7r8m6DRWnc5KHeHSU7dK-RsteYS08ZYf_vYCLK8HXsp2fTxG0f6Ihd8TA4dr87C7-p268L9cgN-OxoFcgMr8BksGzBzxsidmGxM2nHryPetryrx7SVMwS_arPBhI5dcTpXf32tsWgse3-sRXF7DorzB39YI19GFahJ8-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«
آنها من را بازداشت کردند و حتی فکر می‌کنم تلاش کردند من را به قتل برسانند.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/150852" target="_blank">📅 09:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150851">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رئیس‌جمهور الجزایر: برای هرگونه میانجی‌گری در موضوع تنگه هرمز آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/150851" target="_blank">📅 09:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150850">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کویت با صدور ۶ فرمان جداگانه، تابعیت ۴۱۵ نفر را لغو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/150850" target="_blank">📅 09:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150849">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌ شده در شوشتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150849" target="_blank">📅 09:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150847">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پولیتیکو: ترامپ از مداخله نظامی در جنگ عربستان با یمن اجتناب کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150847" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150846">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a30f759b.mp4?token=Bh_d0Pe2Zf9_1HGUeafEb6xXLr0L8FVM7z9PzhvKMcdM7gcWj0LfO7pAkqnbjWqtYeQoGQlb7TCNWViopohAqQA9mFMso1eiH5WMbFkSH_-ktuXP9ieiK83aYbolw4MdtOT_FA-bLvcsjlHYf3PSUKpnpxdS17RLWr31is9R0kSu3B9vWmkpcnh80psAf8lDj7KAOxTZTXJ4xXdzlMfrxPw-cZG0F_2BjxrN9Tq4h-DTwbPgIwvM9uOrdFNfJo2O6kbIbdLcPkdilznJjiLOCWzsu2guczUuZgOt6paVn6zb7r9P1VlD3i2AudD9wRv4W7KUT1dpCt0v119fhxpn4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a30f759b.mp4?token=Bh_d0Pe2Zf9_1HGUeafEb6xXLr0L8FVM7z9PzhvKMcdM7gcWj0LfO7pAkqnbjWqtYeQoGQlb7TCNWViopohAqQA9mFMso1eiH5WMbFkSH_-ktuXP9ieiK83aYbolw4MdtOT_FA-bLvcsjlHYf3PSUKpnpxdS17RLWr31is9R0kSu3B9vWmkpcnh80psAf8lDj7KAOxTZTXJ4xXdzlMfrxPw-cZG0F_2BjxrN9Tq4h-DTwbPgIwvM9uOrdFNfJo2O6kbIbdLcPkdilznJjiLOCWzsu2guczUuZgOt6paVn6zb7r9P1VlD3i2AudD9wRv4W7KUT1dpCt0v119fhxpn4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طوفان عصر دیروز در دریاچه چیتگر و گیرکردن گردشگران در قایق ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/150846" target="_blank">📅 09:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150845">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsZroL9wPl5e5gFt0mBeKYIjCqfRY0KaF1TW2TP_CWLxVfHKS1JeOxovqDPUeM8-fm31nEEFSZjoDisKncI3LCGKsQps7hIzZLKPveitfOp8Lc1OPfjCL1VSRHeLJ18W4DpHBkxhZ7r-PjbgxnDxcwoGlVECDAd8U2lPescyLZaN3HCMs4cm-v2ILEnYlJ-EyHKedjRRy51rxaUmWGmXx8ncAr26_-fuWgtl5Ye2ew63WdITGxOSumzDQl3uP88etLVA6J6MxUS8-OfXeAPWML5EEQSoZAroxvoY44fULjN9Yx2nZhpHHZ9PPCMz1KiSMaktuNHBz-hh5bCB4J1LaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نجومی و عجیب کوییک
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/150845" target="_blank">📅 09:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150844">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08259e56d.mp4?token=tDcILyKiGzhbzYcqx-2kAqu8rQoj1Je_bFQdRdJ7_EFpWtEmYMplE-sO0btoydLhcc-PgKkl_8J_KaYgZSkRDs4YpUDqjjHLO2N_heiwf08nU8W61nkiQhadlllR81-01lf7qlRCQqA9QEXyHKaLy4rFVpnQ2iKGlXfRT7uv5JU9QUnWsxBHD6TP6clIzjhaNU6ggIPXSLQfruJrrGORyFG-A1x0R3hdBMlgkXe4rNFCNbiLFKHR9pSwjv5btSQQ_qxdXVD-L9u_iZSgEAXY7G5bBOo-iZJ8uToL-rTAuFjpxFphQAXvwbS9RU28tbZ4dG8cd9kcp4FWaFvCYAFbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08259e56d.mp4?token=tDcILyKiGzhbzYcqx-2kAqu8rQoj1Je_bFQdRdJ7_EFpWtEmYMplE-sO0btoydLhcc-PgKkl_8J_KaYgZSkRDs4YpUDqjjHLO2N_heiwf08nU8W61nkiQhadlllR81-01lf7qlRCQqA9QEXyHKaLy4rFVpnQ2iKGlXfRT7uv5JU9QUnWsxBHD6TP6clIzjhaNU6ggIPXSLQfruJrrGORyFG-A1x0R3hdBMlgkXe4rNFCNbiLFKHR9pSwjv5btSQQ_qxdXVD-L9u_iZSgEAXY7G5bBOo-iZJ8uToL-rTAuFjpxFphQAXvwbS9RU28tbZ4dG8cd9kcp4FWaFvCYAFbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعتراض دانش‌آموزان در فرانسه به درگیری کشیده شد
🔴
اعتراض‌های دانش‌آموزی که از چند دبیرستان در منطقه پاریس آغاز شده بود، به شهرهای مختلف فرانسه گسترش یافته و با مسدود کردن مدارس، آتش‌سوزی و درگیری با پلیس همراه شده است.
🔴
وزارت کشور فرانسه اعلام کرده در جریان اعتراضات اول اکتبر،  نفر بازداشت و بیش از ۳۰۰ پلیس و ژاندارم زخمی شدند. همچنین صدها دبیرستان با تعطیلی یا اختلال در فعالیت روبه‌رو شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150844" target="_blank">📅 08:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150843">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
الجزیره: میانجی قطری مجموعه‌ای از پیشنهادها را برای نزدیک کردن مواضع دو طرف مطرح کرده است/ تهران در حال بررسی این پیشنهادها در شورای عالی امنیت ملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/150843" target="_blank">📅 08:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150842">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3459b87732.mp4?token=m3ptSV5OdUBP8T-gt4HaG4zLwHpvpkwhVYZrxwMFvRRLYIpLv0iGSxbgKH15-XfUBEKJr8CLsTNuBVoMKYUoKLfmZ38m1M2Fhm-Ow0HFZ7NuQghGuVSj12zrpsC7w-oBU_zkuPDOZiPB0J2avJkY_V3VTcBcMmiHRVuRZ7Ybj2JlmDoWN1AfsZfSFj5I-h4WaF1RYcDeamel3u3pDXX-GEEHUkA9shqxD_w9KXyvzWw2EaOVmNhhrxeXzYkLV0hnlqGJigtTUE9GZFn6BB4dvdddd4XJ7m0RIBMwflCvIwME0LqgjkWlDaVGumDrx_xBVzw_Kw7V0kHqt5pqQ8SOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3459b87732.mp4?token=m3ptSV5OdUBP8T-gt4HaG4zLwHpvpkwhVYZrxwMFvRRLYIpLv0iGSxbgKH15-XfUBEKJr8CLsTNuBVoMKYUoKLfmZ38m1M2Fhm-Ow0HFZ7NuQghGuVSj12zrpsC7w-oBU_zkuPDOZiPB0J2avJkY_V3VTcBcMmiHRVuRZ7Ybj2JlmDoWN1AfsZfSFj5I-h4WaF1RYcDeamel3u3pDXX-GEEHUkA9shqxD_w9KXyvzWw2EaOVmNhhrxeXzYkLV0hnlqGJigtTUE9GZFn6BB4dvdddd4XJ7m0RIBMwflCvIwME0LqgjkWlDaVGumDrx_xBVzw_Kw7V0kHqt5pqQ8SOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کره شمالی: من ارتباط بسیار خوبی با کیم جونگ اون، رهبر کره شمالی، دارم. وقتی یک کشور ۱۱۲ موشک هسته‌ای در اختیار داشته باشد، خوب است که روابط خوب باشد.
🔴
اما این تفاوت را در نظر بگیرید: ایران هرگز موشک هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/150842" target="_blank">📅 08:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150841">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یکی دیگر از اعضای یگان‌های پرتاب موشک جنبش جهاد اسلامی فلسطین را کشته است؛ این فرد از اعضای گردان شجاعیه، وابسته به تیپ شهر غزه جهاد اسلامی، بوده است.
🔴
ارتش اسرائیل همچنین اعلام کرد فرمانده یک هسته موشک‌های ضدزره جهاد اسلامی در شهر غزه را نیز کشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/150841" target="_blank">📅 07:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150840">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXm16B1Mv04oFz2nWcMqKdhoRmgj7u-ZwFtSQiQmBmzSx_KrET79FtIdTXX9M-L8dNroly3cxWnNIHGgyXlGk7vFcpAeGcP8ivUNntuk4aVeegHtqZH8wtfW4ZeFzAX9FP7ye1FkNzvvZ9LjdobGpnRSO7EP8K8QG-NbtG04rbgebWwcSwLrJoY8RnW6YMrN51sbsNvnGVNwmLPSEdIrrtXXTTr4-1i1TZDd_2sKy07cXd-kq90qL75GIcPqrmY0CWnySVPiLR-iNMCMpbPLT-eIMeWRcgcJyXto8GlAx5luHYDhAD85Qb_CFLoUEG9_EmcNbCFR9Ha8Jg_0JdXJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیر ارتباطات کاخ سفید، روز شنبه با انتشار پیامی در اکس نوشت: «حرف منفی‌باف‌ها را باور نکنید. عملیات طرد اقتصادی در حال در هم کوبیدن رهبران ایران است، در حالی که آمریکا در حال پیروزی است.» استیون چونگ با تاکید بر اثربخشی فشارهای همه‌جانبه علیه تهران افزود: «جریان نفت از تنگه هرمز همچنان برقرار است، صادرات نفت ایران به دلیل محاصره موفق ایالات متحده به‌طور کامل متوقف شده و تورم اقتصاد ایران را فلج کرده است.» چونگ گزارش بلومبرگ مبنی بر تورم نزدیک به ۹۰ درصدی، استقرار ناو هواپیمابر و تفنگداران جدید آمریکایی در منطقه و مهار صادرات نفت خام ایران را بازنشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150840" target="_blank">📅 07:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150839">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس ابری ProNet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWWMHDZxTXC4zKEle0QteU5kUBUymPh3ZtTPaqUJMMZQCE2qeP1AzxWT_urGk0jvpW-WzFVPkXgH5Qj8wXHQ4TLnUOHjU2C08wx9lhFrEZFKmeQ0XVDVdru6pTcFenesognac1AbQX4whNR5aGIk2CHrAzehIq0DAabuMI73Lm_bUZBrjQPdqoM95SHZLweK9OoglTdeg44dFP-P9VOaTWUY5FCl1DEfEkKkDg1rfEavHD4V76pQeIXMNgCr9g2-KuEhekK5uDLdsOikoTcfih6kOw2PZGgdJP_2eJkj_d6fS3djYJvLD8o08C1wpHuSNYNxLdyfep5xc3NGP7nJYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین فیلترشکن پرداخت به ازای مصرف ایران
🌎
پرلوکیشن‌ترین سرویس ایران
🌎
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🔴
دسترسی 75 سرور با خرید یک اشتراک
🔵
قوی‌ترین تیم پشتیبانی 24 ساعته
🔴
مناسب برای تمامی اپراتورها
🔵
سرورهای ترافیک نیم‌بها
🔴
سرورهای ویژه زمان اختلال و محدودیت
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دریافت مستقیم اکانت تست
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🟢
مینی اپ حرفه‌ای مدیریت اکانت‌ها
🟢
اشتراک فیلیمو فیلم‌نت رایگان
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/150839" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150838">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGgsYqYTy_yNsUKCOM10pIgc1SM3pvHriIA0gNbZkhNQ4FNd-t937-eMgK61ldZdBwgXHnYYsjhnduJMXrgfByiJE8xL4dXKSfciHVuYXCJBDFTnA0enFQRsrW9u7NiB9gq7xGQiQCkvB9q9Z8-EVqLmdQoKo-6dYI9ylBrJGAzA7p9hNFiDRefsI8_lUHfFCE5A-WZKP9ozyNcBEfNwcuo8SQ30RbYvNfYqLR1sxuSS5J-b7-ytaefKfNGO23_b_HnvV9Ypzq1NzicaNRR2fEeHWcFrBwMD4VdgX0wQZd6P9auRpSvsKhAnQ24muRDYb72K7H7afwcS-W4N2VLgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: ضرب الاجل ترامپ به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/150838" target="_blank">📅 01:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150837">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmGA3xx-S7G5FFaMO8IDZx1mhpHI6Wih-82cxmq4WWGI9aAXdhlsApROCT85ISsgmLe-LsEzi2-uumBU9g0oRCA1B6Cvy1Wy2pE134Clt4KRgGqNslz-fojxWZAFKUwwtGr8l096gxR2cWTL4_zjHApe9DhIM-Bt8kasPaP-6WbsU4uAxypcUavjXCABboZPayXXDk2pxZgnNPJV0i07DfZQ6DIw9zcAPXhtQYM6uJiPzXpl9coNynDbq7C6kca1tPm7twCd8jNRlZfUSlHZZkXPYtRdmurDJDLVRy7xhLgViZFdDqYUMA6kQ0cyPlrD6B4xpyVdiLd5Zij6Ro4rIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام‌های اماراتی تأیید کردند که کمک‌خلبان عمانی با استفاده از تبر اضطراری کابین خلبان به خلبان اصلی حمله کرده است.
🔴
این تبر در مواقع اضطراری و وقوع سانحه برای خروج از کابین خلبان استفاده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/150837" target="_blank">📅 01:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150836">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این وسط فیلم....... بازیگر تگزاس در اومده
😐
📥
مشاهده فیلم</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/150836" target="_blank">📅 01:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150835">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7807e352.mp4?token=YCQWtCI5RKjk9VeLoVHKxG2nbB1vk54POfmOkYzeNO1ISH6CfHkZCFh19wiEXL0Ti5Zd4_lTcHfc4HifSwF4p74b3JUoMZkyx3YFlfxGkBzq3E7DiEazNWIjHFobTuZ3SWB7_bmD8cVFnr2Tub-Ai5ElDUkZuCfp_WPK1hRvCCR2m2J5RIZZDNEDBSHSORCqScmvF2mVVjB6kruTo1tiQxtSvNIrTFjKnkru3PfTqCWF93dGeazSSzakbo2C42NFoGtYqYgoV9oAXSWgoeICF_E30qLAlbAVm5gP_OMqsOWbRpjBkM835-B6qJnBxJ8q6Phw0ZTp4fqrmW40HSVFqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7807e352.mp4?token=YCQWtCI5RKjk9VeLoVHKxG2nbB1vk54POfmOkYzeNO1ISH6CfHkZCFh19wiEXL0Ti5Zd4_lTcHfc4HifSwF4p74b3JUoMZkyx3YFlfxGkBzq3E7DiEazNWIjHFobTuZ3SWB7_bmD8cVFnr2Tub-Ai5ElDUkZuCfp_WPK1hRvCCR2m2J5RIZZDNEDBSHSORCqScmvF2mVVjB6kruTo1tiQxtSvNIrTFjKnkru3PfTqCWF93dGeazSSzakbo2C42NFoGtYqYgoV9oAXSWgoeICF_E30qLAlbAVm5gP_OMqsOWbRpjBkM835-B6qJnBxJ8q6Phw0ZTp4fqrmW40HSVFqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیوید کیز، مشاور سابق نتانیاهو گفته بود جمهوری اسلامی، ۲ هفته و ۳ روز و ۶ ساعت و ۱۴ دقیقه دیگه سقوط می‌کنه!
🔴
الان این تایمی که داده بود تموم شد و جمهوری اسلامی سقوط نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/150835" target="_blank">📅 01:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150834">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD4OT-hLa8CfW2pcJ68eFCqTi-33SJ1txWpWsEgT3ZshrIyB8JGYTa2ln9wg2D4HlPei5hgGZSP62pVyZ2VuqNYSGp2Uv130WfSH5dV2eOTzGx3C-DLxS1StRyohkxpdESdS-uro3u08YTMEkwSyceqfxQEcRbg-xmvn_1Pl-Qdk10R3r_bur38dAsht8SSg3aUx5i7wXG25dWEilubEB6bexscHo7xl76KYO5OdZKUboAcDc1lGFtgsf4NxeM4xz4tQJT_g0wCGIyHukprVKCwcRVHloPUU6rxaJ2rFPR0b3yF32b4lyHDdMUYEfU9fM3L1jQitl4TF-eM0w9JPig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار کلاهبرداری
‼️
🔴
دوستان تبلیغاتی که پایین کانال نمایش داده میشه و غالبا کریپتو و سیگنال هستن، تماما کلاهبردارن و تحت هیچ عنوان توجه نکنید
🔴
این تبلیغات در پایین کانال توسط تلگرام منتشر میشه و از دست ما خارج هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/150834" target="_blank">📅 00:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150833">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prZruT9aPx0j6tAP4wuUNM2oI2L__be_7luyGVqmhlTQOspZhLZyOfXjkb8k6U0UViwDWzGhK5AJVbNnxKwsEj_hlwo6piAadoyfntFfb7sfyxyGQ6dKOTi5gIbQfgmixjSWbLh50yw7BEq3q0egaFjeV9rfl05NkwC7LwykA5tEXqfzFdX8jGIZKblz9uL33OcVVwaWPHQnhw8VX3oCBZwpmzRuHcbIVY0PDcpPlsXy53lkHT1PRur27lgrYWjx0PgiPSA-j_O2l9ct4JR3ilCFYq1bzBrN58OKVR4L5OcoywIgCUQDaEPPBI4VKfBkJ_CkK67Ad0MZZxdHZ9cAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه‌های اسرائیل: مجدد به آسمان تهران خواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/alonews/150833" target="_blank">📅 00:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150832">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: ایران بسیاری از برنامه های تسلیحات هسته ای خود را رها کرده است و من درباره آنها تصمیم خواهم گرفت‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/alonews/150832" target="_blank">📅 00:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150831">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: ایران بسیاری از برنامه های تسلیحات هسته ای خود را رها کرده است و من درباره آنها تصمیم خواهم گرفت‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/150831" target="_blank">📅 00:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150830">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOo7dDiF8FdUVvZW8zTfDPyLxmofYZntLEFB4MzeVPHP0VCymqEo8Wk-L0pLqTmCyIxxQXEnrWKqF92oPCy_-m6DYS7IPlCqYz7xzxIoJnzSgbdF6bFO4zDaLDs_Q6Og9ugQmEd-GtP-VwcTgPauw98CI2UrE4fd8CZIZhpVla_Rcjco3DN_5xphXIvebYpxKVL7XsQ4rLFfa1j5V61et1cSGAHC8ms-gYayK5YfM5mHcaAS3HEiNe-nbTahw1T5r-bH9LBihQEwbH6DQrSh5GrFercI0QhGDe57vEfzunYaD9t5QVIUvoHy6aPT0sa5-SEVqgKRq87mPxIiJUNfZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: کمک در راه است
🔴
روسیه اعلام کرد آماده میانجی گری بین ایران و آمریکا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/alonews/150830" target="_blank">📅 00:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150829">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qhgt8nEardA9CJGlKrDo3jkav8PZb2GfMqTQq7yOv1-p1HVxF4e7pLfwT0XtX_rdMcNrKs769aCebuFh1najt3K6nFHI6HkFkdEI59qWBPvjTEWVrTmxsBVouG1s49difD_L9afCSx8ZeKHF8-OwRqOEYXUPSQHrZ6UpQiw4bDrLBMMOe1VFdMiFTotgottTABbtxXOls9UpRobwBFEYFfq4OV9yGGoEeo8hubNIsOTbtvCUEwsQgOAhusEpkzmm2cIxrxMR8bZxOmhu7AK-yFf1e0uhY-BXfChzN4nRs4l7XJVOm6t0ORKZjbWsTg8bolNfZFHymE7hYlZgIR4nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هر کد ملی، یک فرصت چرخش!
گردونه صراف رو بچرخون؛ ببین جایزه‌ت طلاست، دلاره یا یه هدیه دیگه
👀
شانس‌تو امتحان کن
👇
https://r.saraf.app/s/agrd348</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/150829" target="_blank">📅 00:27 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
