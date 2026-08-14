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
<img src="https://cdn4.telesco.pe/file/KpebWi3jpUVCimGycKlS_HxOxJKDa8hBP1YHkL9Jfol61RhAAff9XI3AQ1RgSg4_ctR2S--424UtHzSjKOalZxVdKMCmWro5iDkjlG4ScG-MumznVo99Dl1mJZcDp47GS5Dp-5PvKkOGNmzR_84vqAUPxN7hG7GtJZdCNZ0wc8YW5gPkM9KFxl4E0H9Eou0nixA-eBu9bmKBdZDIw-h_4rPCbDNiqKoRJkqOH3Z08nLw8PhIc3YNawXnE6ia3Xz44Sq9MbpHh_fiZNBSnMmgHy5CIqbl-dN4kq9S7fMZFlvTKyEGnfuFz0Rg2BZe_Cm8TGOEWGT4JAfKgXqBW_ukxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 19:41:56</div>
<hr>

<div class="tg-post" id="msg-141685">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سنتکام :
۶۲ فروند کشتی تجاری رو تغییر مسیر دادیم، ۳ فروند رو از کار انداختیم ۲ فروند رو مورد بازرسی قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/141685" target="_blank">📅 19:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141684">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
نخعی، نماینده مجلس: بخشی از قاچاق سوخت تو کشور «رسمی» و با مجوز انجام میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/alonews/141684" target="_blank">📅 19:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141683">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz-PU4_bH8JM3oLEu5U8tUOzU4ugPi1vr8fZhNl1zjAXtolzR2j74_iFajDdUjkSww5RzmDa8lFETo8pkbxiAYCaEg_B_M9FODiISvbAUkfg6hONcAt_1gRwEvBv056mxtdFQkk-vW3t3N8AssIrncvWgFXRSdtoEsuj8K3_GkqM7FJXIMAw336oCS5WdeurP_K21jJN9LPXd2wqbyUZ3IMXGjgaqPouAJP8X07JsI4gUlXlvAs5OuouOaNq0pfUCg58hN-evsM-IeOm0QA--7znxLLoE3ew_TbtwEdQZjoFvoRbeDu9xGywKpdnzJuT7nlXNdxvhA1JygIcV6Mobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/alonews/141683" target="_blank">📅 19:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141682">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
حملات اوکراین به بنادر روسیه واردات نفت ترکیه از مسکو را کاهش داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/141682" target="_blank">📅 19:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141681">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgE4MNcPP-QTnKgDUCdEKgbqYDCuIIWKa5nG90OZXCBVQsJiE7olDB9ChH-tSaFRuei9IIIpjbhsZzVmHQr9ivMmAS7P75BBlcIeGYRF7xx2DcSQaoLpP8c5XEa3Gf7Km8Um4H2tMWNkmfkBVDIIxaXiFPHS9qemuSvBrZV5rfqxIhLekcmpCcVuZ8prJd6zq_dB-2MHpyZQoBCHH3JiKRuXuE9bTtV3COKXpa7nkR6dV3wOIbEXNcFWQx37_3JtA3Je4ME_YayahVSDf4vWESYYKnwMOSWZ6lZQT_824MVIPW8EUiTpi2FoeNNl9ugrvNJxdRq8AefJM4KHPobwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع روسیه: دو بندر «اودیسا» و «یوگنی» در اوکراین را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/141681" target="_blank">📅 19:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141680">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
فرودگاه بین‌المللی قشم با پایدار شدن شرایط امنیتی، آماده ازسرگیری پروازهاست و برنامه پروازهای تهران، مشهد و اصفهان طی روزهای آینده اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/141680" target="_blank">📅 19:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141679">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری / وقوع حادثه امنیتی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/141679" target="_blank">📅 19:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141678">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35437e583.mp4?token=nlpneAc5dXFk_Z-o3EO_41Ek1OZK-ZGfFk8xu4KZwJcXqLZt0JsF5PSewXTK8C47xCDy2rUmP3FZOGOi7v5_WpV_8GVKHYBTCLQmjBuwIWIvkg_UxXi7JmB5om6p2zk5RN_Fj8pWPygzFF8Hbt4Nc7FRV0Bg6vp-jjGs2vPTSelkTlvqnytD2PTrjDPbjBpgBgWkM4CGUV8zJaczXykQ2sRIvqm_VV5aqPQtP-o2O-oqplauqO9p5DVgIrBx5nZ19SqesCMt17VtlDIFP4yPwZp4AUv3Hr2Yxo-1k4foVKcYuoIv9sLdu0kxqUyJbbqynAqRAbzuBnTuPZrVw3m1J24FHL-GaA1aoj_zzlEajFTzPH8eQ7A1vb2wP9EeT4myVYSKMRCS3X3jkBaODZ0ck59h3GTdMcT0R1C6HeGHOWWsyFInbnkrKY90M8DYpOuQC7XJoXA-IqY119zuYsC5d682ggKhldo4ryV66Nft5IdijXsY-rdZQ2ny-weLleIsFHDL_cPFSkKPZeL0hA5OqxEYS5XEUhgYPO3c3BmAfXHsyxlewg6L3mmf7lpT4QfJpI7kdOLgiAHfIUyomNAzyPxJv-LeycRrWrBKl6Ck8eSixnvwo2BOgbpezqq0fBxMjaY05tAfC5v6uegdcQn98uWh0YnAp6c9uozTW5tnhfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35437e583.mp4?token=nlpneAc5dXFk_Z-o3EO_41Ek1OZK-ZGfFk8xu4KZwJcXqLZt0JsF5PSewXTK8C47xCDy2rUmP3FZOGOi7v5_WpV_8GVKHYBTCLQmjBuwIWIvkg_UxXi7JmB5om6p2zk5RN_Fj8pWPygzFF8Hbt4Nc7FRV0Bg6vp-jjGs2vPTSelkTlvqnytD2PTrjDPbjBpgBgWkM4CGUV8zJaczXykQ2sRIvqm_VV5aqPQtP-o2O-oqplauqO9p5DVgIrBx5nZ19SqesCMt17VtlDIFP4yPwZp4AUv3Hr2Yxo-1k4foVKcYuoIv9sLdu0kxqUyJbbqynAqRAbzuBnTuPZrVw3m1J24FHL-GaA1aoj_zzlEajFTzPH8eQ7A1vb2wP9EeT4myVYSKMRCS3X3jkBaODZ0ck59h3GTdMcT0R1C6HeGHOWWsyFInbnkrKY90M8DYpOuQC7XJoXA-IqY119zuYsC5d682ggKhldo4ryV66Nft5IdijXsY-rdZQ2ny-weLleIsFHDL_cPFSkKPZeL0hA5OqxEYS5XEUhgYPO3c3BmAfXHsyxlewg6L3mmf7lpT4QfJpI7kdOLgiAHfIUyomNAzyPxJv-LeycRrWrBKl6Ck8eSixnvwo2BOgbpezqq0fBxMjaY05tAfC5v6uegdcQn98uWh0YnAp6c9uozTW5tnhfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره هند: این هفته، من مکالمه دوستانه دیگری با دوستم نارندرا مودی، نخست‌وزیر هند، کشوری «کوچک» با ۱.۴ میلیارد نفر جمعیت، داشتم.
🔴
حمایت‌ها در آنجا عظیم است. ما در حال تبدیل آن به روابط امنیتی و اقتصادی هستیم.
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/141678" target="_blank">📅 19:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141677">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: با توجه به نظرسنجی‌ها، نتانیاهو در انتخابات پیروز نخواهد شد و ترامپ نیز همان حمایت مورد انتظار را نشان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/141677" target="_blank">📅 18:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141676">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رئیس صنایع نو سازی ایران: هرکی خودروی فرسوده خودش رو اسقاط کنه بهش ۴۰۰ میلیون تومن وام میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/141676" target="_blank">📅 18:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141675">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آکسیوس: اندی بیکر، مشاور ارشد امنیت ملی کاخ سفید، در هفته‌های آینده از دولت ترامپ استعفا خواهد داد
🔴
این در حالی است که او نقش مهمی در سیاست خارجی و تصمیم‌گیری‌های مربوط به امنیت ملی این دولت ایفا کرده بود و شخصا در مذاکرات با ایران حضور داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141675" target="_blank">📅 18:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141674">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
الجزیره: اظهارات ونس مبنی بر پایین نگه داشتن قیمت بنزین به عنوان هدف اول درگیری با ایران، نشان از تغییر موضع در قبال جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/141674" target="_blank">📅 18:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141673">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری / وقوع حادثه امنیتی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141673" target="_blank">📅 18:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141672">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خبرگزاری هندی: پزشکیان به زودی برای شرکت در اجلاس بریکس به دهلی نو سفر می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/141672" target="_blank">📅 18:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141671">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزارت نفت عراق اعلام کرد برای صادرات نفت عراق و عبور از تنگه هرمز، با ایران و آمریکا مذاکره می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141671" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnbZwwlslvlsEzwnzs0GkLG2b_nRoMpVX0jCg3kA-qwgTdU8RIz2R_W8odfoXkdBSwB1VMr38vWm7JITAreTyYfZ1WoMnLZTwNbyrlv3fyJcrJeNkoppE3le8IbgNsT2KNZZgx2sGfeSL6kxZVBiHVDVupd35Z6SzYBIIIB9Kyyhs7N5IttDkOll8FxB1EbOjJXjy-QzIzeFCpNJtMGoCTQ3b119eAq_wzprLyFIVxzPV5ot-we-vZ09YE210LmhfoJOxi-8j2W-bYkjM8MfJAsyUdE2txMqQnnoGSA2DDGgfNuxkNr3yeyiYnSjOSN0v-wAnojqrnqbVD_EPOfnig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آمریکایی: کارولین لیویت، ۲۴ ساعت پس از آنکه متوجه شد ترامپ او را در هواپیمایی که فکر می‌کرد ممکن است به آن شلیک شود، رها کرده تا بمیرد، استعفای خود را اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/141669" target="_blank">📅 18:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رویترز: اوکراین از روسیه خواست تا در دریای سیاه آتش بس برقرار شود اما جواب روسیه مثل همیشه “نه” بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/141668" target="_blank">📅 18:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام آمریکایی و یک مقام اسرائیلی گزارش داد: مقامات کاخ سفید به نتانیاهو فشار می‌آورند تا خشونت شهرک‌نشینان در شهر قصرا را محکوم کند.
🔴
واشنگتن پس از اطلاع از هدف قرار گرفتن خانه یک آمریکایی فلسطینی‌تبار در شهر قصرا، اعتراض کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/141667" target="_blank">📅 18:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=q8A2dxIz2leWihiKMcbbpaRB8vo4rVT4ExC-TdJjJuwNdbWQvKVvMf0F1D8dYIzIEZYQ4NoltNk08fsgyEfISCnvjNsuNJh26JOq6sDwIKHy0WNn3ZRjGsAY09E4Wgq9rkj6kHSw6aMDY5DZAW6dta8uOxd1mrOjwCuxvaGDddMIMzO0EQfF1ZCFSuvE5U6fEIbgDWPTf4Dd5ciz2D6sie8NSEO6rd-xkuvOsIRhYb0Wn_348CXljjD9a17EPqX19NiegCWuyoH2TZeuI19AfwwoI_oh_pFE1e1pHNvGoaVfLKEsugbbujXfITKxzWDDfwFHhe6ttrGRY5AjrnOKJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c20969ce7.mp4?token=q8A2dxIz2leWihiKMcbbpaRB8vo4rVT4ExC-TdJjJuwNdbWQvKVvMf0F1D8dYIzIEZYQ4NoltNk08fsgyEfISCnvjNsuNJh26JOq6sDwIKHy0WNn3ZRjGsAY09E4Wgq9rkj6kHSw6aMDY5DZAW6dta8uOxd1mrOjwCuxvaGDddMIMzO0EQfF1ZCFSuvE5U6fEIbgDWPTf4Dd5ciz2D6sie8NSEO6rd-xkuvOsIRhYb0Wn_348CXljjD9a17EPqX19NiegCWuyoH2TZeuI19AfwwoI_oh_pFE1e1pHNvGoaVfLKEsugbbujXfITKxzWDDfwFHhe6ttrGRY5AjrnOKJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک فروند جنگنده
MiG-29 اوکراینی
امروز در منطقه اودسا در حال تعقیب یک پهپاد روسی Geran مشاهده شد و در نهایت موفق شد آن را سرنگون کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/141665" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3z84ZGg4KlrTuBHGhm6EdzvygbLka3N097lk7KyyYk3sn5lVUNixvv9xFRItKr9cU87hvTA5XQWMRq5xjUvJ0_9aHltOrcAVV3lVXK6gYy2y-LbVMehfNIrgKvd2DrepJ0-jW4aYOmZSjE42klnKy9-A2UAPU5v1SFySi6jcMl7nXtDoiZHW1gHbQW0n6Uzh-3Nhl03-YzbCMQdJ7rgC7qAInE2RjOwsYvarxFg8wDDBb4m5IkHqbZ_Ixk8rfg9n32xZq-TZ1J6uQFVSFxQnQjyLH7oEX0pQNepjLzcRD3rGBzkLbRNCir9aJinV-SMDd2T77nWW6_GUSoQy_seVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازگشت فعالیت هواپیماهای سوخت‌رسان آمریکایی در تنگه هرمز، همزمان با نزدیک شدن به پایان آتش‌بس ۶۰ روزه میان آمریکا و ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/141664" target="_blank">📅 18:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms1w8YbLLqLK6rTJC_9EWPprx7dxz7nVmKaITsOsarqUgu1e5tDO4lw519F6AG1o-klvNent8KFMxEraPiRgJvPd_zxWY1YxDtX-lvnL9fxjNOF1QrGupHdMFqOfEojpF7Su6O5Z2aZqPfR7zWTmNkEw0go4FoLA7BRskAHR7DFusXTkgOrWb5xygSkFi88AygWtIzHAoudTgNNVRUvfvYi12Qjm_1w_zgYofw9_O82CSWBQ5-Uzpc-ztXPo00UioG1HPwX4LhGyXdau5uy6tS1kKr7YkIs8YblKjFusPpp6skcmziPw_d0-_xXwpvwyfcmdnPyNLk74rR5kL4JAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: امروز (۱۴ اوت ۲۰۲۶) یک ابرنفتکش از نوع VLCC متعلق به شرکت ملی نفت‌کش ایران مشاهده شده که در حال بارگیری ۲ میلیون بشکه نفت خام در اسکلهٔ آذرپاد در جزیرهٔ خارک، ایران، است.
🔴
اگرچه این اولین محموله‌ای است که از اواخر ژوئیه در این جزیره مشاهده می‌شود، اما ایران بارگیری نفتکش‌ها را در سایر پایانه‌ها ادامه داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/141663" target="_blank">📅 17:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQNkCsX71nbFbUGyt1cmQQUUPcxmGF4b5O3iUFgmIu_YNd-jPP3_duhbft71NwBUw0vfYVtg_r-t8tv8wVgshIlNHkUsMCBbCTZj6I-qcZxJqM6DVKcw5EkyPNoBv1A9TgqybwO1nFMXR1P-5DSKAKsuKMPRu10ZkJWIUTI1GcxcyBkn1Kp6lXCDBz_yug9FcXKWvfL66ckdy2gpcfOfh59xzGpaFwP8D2TA4Zbp-AbYBIS1cTNuis3x6FSSm-weBQ3zxlX-jxbxOzBrA62h9qycrjUTYJi2zZSaoyCZjX4eXaIGtdMnIS32skYxy8BkCCif5H4WVj4l7nplu0bfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
خاتمی، امام جمعه تهران: آمریکا بیچاره و بدبخت شده،  جمهوری اسلامی به یک ابرقدرت در جهان تبدیل شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/141662" target="_blank">📅 17:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سی‌ان‌ان: هیچ مسیر واقعا امن کشتیرانی در شبه جزیره عربستان وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141661" target="_blank">📅 17:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/len4Uir4rO1TVDcvs61E-OrKIjJknKjWIp3Rcd8O5dRL3qevTW2TLB1p0L1g8md9aP7zAzoTJA4sZLSlrzVkYh45W2l68SQ4WMlDmFuVlKRVSBBHNxudxzO7LcEVqyj4r2ZUTTmplvsqmCAgD6X-pochLIokgDB-IVaIQExcAhkirtNtutAoTLcO6VDZQ5m4JLZFh4iA3KArsmdkfyNNJ3F9rMnU0ZoePSsXSc63qFlY8SNDy8CubRPuEl5AmPZGxeQR6rlJeB2s_vPkHt9qKhDnE4s0jb94ea3keu6eN2zSAn7Qa0klDmcmoJ0i_bsmviYicsxEuPraXLcRdggP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتقال تجهیزات نظامی ترکیه به عربستان سعودی از زمان توافق اخیر مکه همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141660" target="_blank">📅 17:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نیویورک تایمز :
پوتین به نظامیان ارشد خود گفته بعد از تموم شدن کارش تو اوکراین، می خواد کشور مولداوی را تصرف کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141659" target="_blank">📅 17:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141658">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZYRm2F4sxDpo3PlORZjKriG-1Sk2qvM87tpbDevIKYrEbn9AKXxuyH6kUPqNwzq9cP0owWKJ7S22eIUkqiYgJ3pmkWHdnv0MuynIEoA3HEvNlcyBpTg2Ua_9B5AdgTnn-GmD6aZZlieHPFhBbforc7bO5sxiZ8FruUSqKlkNmj8kMFW7eODBcbYRFSYAjzEN0Inddhb2K6PEfugiJtVKD0AH5DGClio7pPyMlXLtp4tGhGMxPvnhbpNacwsdkSMwQE-DP5Er3ytgIymlmLXBLzdN3EHYFkzd4p0k_boa2zzgwj8_OOMnvFVWjVDXFg6oK_atuUU6LzWXNJaWXsgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: دشمنان جمهوری اسلامی مفت خور و شکم باره هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/141658" target="_blank">📅 16:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
واشنگتن پست:
حتی اگر جمهوری خواهان در انتخابات شکست بخورند و سنا و کنگره هم رأی به پایان جنگ دهند باز هم ترامپ می‌تواند وتو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141657" target="_blank">📅 16:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW68-mmoUzr4mwwdBQMjJgYvHgYptxuZgxJAJnB_7_NPERjC4jutW8heh-hH0IPjnBTwkQC_4HW1hTtOKwl6VkQszFfQS8QjMYBsT67CvYlVvq1RPUQXYvHeRGSAC_tq63sOorwUrTD59-jn4MkC6bJfGtLsxtm_Gz_9XL6qeQahrZJph_5X5cfLKGfCDuVCeXo3WJJ2EM_rOvAqpFd-cMRXY9cCBWNo1CUOV1jfqo2viCjVJI8YYCR1bS-Xswpp05xgWzXeNFeQyTluXE4sMYw0xfFCw_gp2HSSVseU7AOJCnCoD0YdOyVdOKdFuuuQxQUOXEaL75EBZeZpLha0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منطقه علی الطاهر هیل در جنوب لبنان، تقریباً هر روز مورد آتش توپخانه‌ای اسرائیل، حملات پهپادهای کوچک و حملات هوایی قرار می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/141656" target="_blank">📅 16:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea185b49e4.mp4?token=JW-wK_fok3p4wJZEOO3MIPgKL9cS-jcYtzAIplJSkxLQCmLgvKDqtJEmBddVBrWJ6CF6oma_6bLPOrRGr8VVT4WBiI9Qj5EE12ci5FzGYh7xV0sxOcQ86IBNrGQ-IkhA0Kk67MPnOrNqs5aBJtc84JrpBmblon8bMy1LEivzp63CF-c35UdR0JVJ45wIoKRfVvygsC10fYf8CzRAlOhmPCT5DPR4dZLT9OVVn2zfm2xAouozMxbeB2Jhe_R6yzAawuat6NJ-lXGvoVrYTR2UZmxvlZyYTXe5g_mdaFs1WBBRnxm2X0Dtu-MsVl5V6IydasJB2vJq2gHRrxQ9oDm39jtX2uXoWgSLngNtiAbgZalb0z3y_cXOicZhgt9P_QaOROeAlDELdv1B1H4-jfPgOxAYusA9DNBuvxSkVfmuSB6uwA_cIuJXs4ZI5q1fXVR0IB1eDqRq7u9Fxc0XVWwr5oI0ndGU5mMVFxZGQnAVyPEESRundT8q6COBDIdsauTQ64meY5XFwVF7sW37gX51kOVcym5-iat9FbPooSQU-WotJGn5YjmHsVKmskTd6l0EjzQjS3WEJGHprk5xd1lONH9f48Y1_uRx-MTO3jn-z33aRt1kQZ6S6vMU5lR2CX3hCz2_xszNUk0Vk-jQ5eYF3bp9sWi7I88o60IWHelznBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea185b49e4.mp4?token=JW-wK_fok3p4wJZEOO3MIPgKL9cS-jcYtzAIplJSkxLQCmLgvKDqtJEmBddVBrWJ6CF6oma_6bLPOrRGr8VVT4WBiI9Qj5EE12ci5FzGYh7xV0sxOcQ86IBNrGQ-IkhA0Kk67MPnOrNqs5aBJtc84JrpBmblon8bMy1LEivzp63CF-c35UdR0JVJ45wIoKRfVvygsC10fYf8CzRAlOhmPCT5DPR4dZLT9OVVn2zfm2xAouozMxbeB2Jhe_R6yzAawuat6NJ-lXGvoVrYTR2UZmxvlZyYTXe5g_mdaFs1WBBRnxm2X0Dtu-MsVl5V6IydasJB2vJq2gHRrxQ9oDm39jtX2uXoWgSLngNtiAbgZalb0z3y_cXOicZhgt9P_QaOROeAlDELdv1B1H4-jfPgOxAYusA9DNBuvxSkVfmuSB6uwA_cIuJXs4ZI5q1fXVR0IB1eDqRq7u9Fxc0XVWwr5oI0ndGU5mMVFxZGQnAVyPEESRundT8q6COBDIdsauTQ64meY5XFwVF7sW37gX51kOVcym5-iat9FbPooSQU-WotJGn5YjmHsVKmskTd6l0EjzQjS3WEJGHprk5xd1lONH9f48Y1_uRx-MTO3jn-z33aRt1kQZ6S6vMU5lR2CX3hCz2_xszNUk0Vk-jQ5eYF3bp9sWi7I88o60IWHelznBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رو خانا، نماینده مجلس کنگره آمریکا: اگر روزی رئیس‌جمهور آمریکا بشم، بلافاصله حمایت‌ها از اسرائیل رو متوقف میکنم و کشور فلسطین رو به رسمیت میشناسم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141655" target="_blank">📅 16:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141654">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💢
زود بیایید اینجا خبر خیلی مهم
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141654" target="_blank">📅 16:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141653">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزارت جنگ ایالات متحده با شرکت‌های "بوئینگ" و "آر‌تی‌اکس" قرارداد بست تا تولید قطعات یدکی موشک‌های SM-3 را افزایش دهد. این موشک‌ها برای رهگیری موشک‌های بالیستیک در خارج از جو زمین طراحی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141653" target="_blank">📅 16:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141652">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnZ1GKoE5ZebT0VncwJ3BYYN2tPBz2GOt6iwKCHZ7sX6b9tLC9xnLKE7Kdfr4s-6s6A701_jnN-t7QPlg2tPnaj7TQbzMdLmYUJ99cX_LEhFHt84luG35NKU5cPeECJ1Bl-XBJ4n09-YsJfAFyd2zA7OIXn-E0Z7am-TtGSB3skZlO80Jjxrstva0GuVgueFuEyeUd-7CKdVYd3M_IcCE6bRJTU9qZEtBuYKi3pNbeF8evnY06adTZP6b6_86TNSBMz67LSXfG5mV4j70bz7Rl430ssYK5-sarRyJ5hkw8_o4c6VC9gxkAaCXvX5GmivrUIHD9HuTk4pNZWwRmXtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیران خارجه ترکیه، سعودی و پاکستان با هم دیدار کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141652" target="_blank">📅 15:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141650">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm8p_WC6czKsuC5R6pbYpfP4mktnLGcApvpCf1Jz0k25mHLCqFYlxoQWVxaDeU0zJ5D5VQxeSTocxk3_RvBQu8WtChtk5vjm2dx-Cw8uhTkkgXYKkFYrlVLeTuGsGEhpHr-A_trjwCOGSe3vqP6wNlHk-Qc3u1SJ67bArCbzDq3fgPr5sGsNm4bYpSrDFSPsJAQnr_kCSjCFKeK5gRY6QWUyiM724WwDQ6k7jin_pxMLFH6RU55dCEYxySAphzNctNUZnop3swCCH1bhYmkJZVuyKA10yAIg7PAyN_PAJ_XgympzJlHmFgKnbsYkKmi-I1Ui91nL_ldy42_-NKSLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی امام جمعه مشهد: آسایش و زندگی راحت بدون داشتن انرژی هسته‌ای محقق نمی‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141650" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141649">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
به گزارش وال‌استریت ژورنال، ناتو پس از ورود یک پهپاد خارجی به حریم هوایی لتونی، چهار جنگنده را برای رهگیری آن به پرواز درآورد.
🔴
این پهپاد در نهایت توسط جنگنده‌های ناتو سرنگون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141649" target="_blank">📅 15:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141648">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وال استریت ژورنال: توافق ایران و عمان برای بازگشایی تنگه هرمز در حال نهایی شدن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141648" target="_blank">📅 15:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141647">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqsDyTXQlanMTK8zBHkdC78bxzJgEZJrXNhK8_MhyL7G-gb4EHp-2KV_nuYoARgOG2M-2fcRCR8Osp5s0z2PUhFKQfHmLmWTyMJ9p7UAtQC4SEDpWAYG0zkCuWe_xaSIZbkjXgODrKfAhSo6ZZww26wufjcjrXyzDe-T2LMnrC_Vdx8hdLwtBqaydim75OpqIwh5YMpCVlEtwoIpvANIesB2WNjk2EpKmu36WPqxTaM7xkWx42sf1hVNZQu76IufggsRRM1iM5ZixOa4GTmzkcKe8KNXxjTTQfunCe5uaK3kuDrN3CIJmRgliv5pTTpebvk-g5seTHSWSiH9VaG4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از نسخه افغانستانی دیجیکالا به نام افغان بازار رونمایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141647" target="_blank">📅 15:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141646">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اکسیوس: فاصله‌گیری ترامپ از نتانیاهو؟ او هنوز از نتانیاهو حمایت انتخاباتی نکرده
🔴
رقبای نتانیاهو از ترامپ خواسته‌‌اند بی‌طرف بماند
🔴
ترامپ از تصمیمات نتانیاهو کلافه شده و گفته «بی‌بی بزرگترین دشمن خودش است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141646" target="_blank">📅 15:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141645">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
به گزارش بلومبرگ، روسیه هم‌زمان با ادامه جنگ در اوکراین، هر ماه ده‌ها هزار نیروی جدید را به ارتش خود جذب می‌کند.
🔴
این روند نشان می‌دهد مسکو همچنان در حال تقویت نیروی انسانی مورد نیاز برای ادامه جنگ طولانی‌مدت در اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141645" target="_blank">📅 15:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141644">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پلیس اکوادور در روز سه‌شنبه، 469 کیلوگرم (حدود 1034 پوند) کوکائین را از یک کامیون در نزدیکی مرز کلمبیا کشف کرد. بسته‌های این مواد مخدر با تصویری از ارلینگ هالاند، ستاره فوتبال نروژی، مهر شده بودند.
🔴
مقامات ارزش این محموله را بیش از 11 میلیون دلار آمریکا و نزدیک به 20 میلیون دلار اروپا تخمین زدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141644" target="_blank">📅 15:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141643">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سپاه: بازم پهپاد زدیم الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141643" target="_blank">📅 14:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141642">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">💢
تحلیل عجیب از اقتصاد آینده
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/141642" target="_blank">📅 14:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016cac103e.mp4?token=snY3u2plfyK5YRMImNuVyvIL60RvfyxkciYYcvnKtDB9Db-3bJ20-xyXiEMZsQo0hmgZplvXoPLlFk0IBEMDJGX9DdgyrpSYowe3IuMfN7xSW1cgCuURTz2NMDMii25f1j7n2QM6B4cIBS0Vv4a4Ih44Dvczy7n0luaytUz0Lgtx9mhw8wPB47vagS9XMYl2Rd_8CCHD6p0uwMYiwG3itmPoeY7rZBoBZYVDZFl7Jloo-Mr6naOFEvC8pqzxAg8fOVGrtHEPdeYwPGJ58fgk9aIfks6Ie4-gjvmUJ6YW_4wO4FkHa9PbkE3iQWHG-_RKgs9r4OASZHFjIIdfOJBUVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016cac103e.mp4?token=snY3u2plfyK5YRMImNuVyvIL60RvfyxkciYYcvnKtDB9Db-3bJ20-xyXiEMZsQo0hmgZplvXoPLlFk0IBEMDJGX9DdgyrpSYowe3IuMfN7xSW1cgCuURTz2NMDMii25f1j7n2QM6B4cIBS0Vv4a4Ih44Dvczy7n0luaytUz0Lgtx9mhw8wPB47vagS9XMYl2Rd_8CCHD6p0uwMYiwG3itmPoeY7rZBoBZYVDZFl7Jloo-Mr6naOFEvC8pqzxAg8fOVGrtHEPdeYwPGJ58fgk9aIfks6Ie4-gjvmUJ6YW_4wO4FkHa9PbkE3iQWHG-_RKgs9r4OASZHFjIIdfOJBUVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سفیر آمریکا: در صورت تحویل سلاح‌های حزب‌الله، حملات اسرائیل متوقف می‌شود
‏
🔴
میشل عیسی، سفیر آمریکا، در پاسخ به پرسشی درباره زمان پایان حملات اسرائیل در لبنان گفت: اگر حزب‌الله سلاح‌های خود را تحویل دهد، «همه‌چیز متوقف خواهد شد».
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/141640" target="_blank">📅 14:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2252485e79.mp4?token=mCtKLucJQQDcMbLDw4S8-3H71mB6QYVKpH7IwEQ1Uubch7t1pMJg0SMSMNw4mrelQNelYXsuRJVS_-jQ4khgNRhDBaZ-cY6tEAlRQDUUgWrs37N9xVGp_mzknoUELq0OgVlu30yXhYb8ZpEb2AKFnra5dZ_FszrnXxtGEXSc3aVru-CysjzcR9KQIH1ts1RB0_vlNutT_NNJ3SkzSXUBZjHJfHJ5qy_N535_PAZ83Szd3bJIi1FDBPSe7QZghUo3l6abag6T153RqwwborQjAD1v4f7XQbU68b9u8W2vUzTLkBtJtZ52LJGvjgIj6ajMMk38y_btsZ8PDZzd1vkIIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2252485e79.mp4?token=mCtKLucJQQDcMbLDw4S8-3H71mB6QYVKpH7IwEQ1Uubch7t1pMJg0SMSMNw4mrelQNelYXsuRJVS_-jQ4khgNRhDBaZ-cY6tEAlRQDUUgWrs37N9xVGp_mzknoUELq0OgVlu30yXhYb8ZpEb2AKFnra5dZ_FszrnXxtGEXSc3aVru-CysjzcR9KQIH1ts1RB0_vlNutT_NNJ3SkzSXUBZjHJfHJ5qy_N535_PAZ83Szd3bJIi1FDBPSe7QZghUo3l6abag6T153RqwwborQjAD1v4f7XQbU68b9u8W2vUzTLkBtJtZ52LJGvjgIj6ajMMk38y_btsZ8PDZzd1vkIIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از بقایای جنگنده اف۱۵ منهدم شده آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/141639" target="_blank">📅 14:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ در حال باز کردن در برای نیروی دریایی ایالات متحده برای ساخت کشتی‌ها در خارج از کشور برای اولین بار در چند دهه است
🔴
سازندگان کشتی خارجی که سرمایه‌گذاری سنگینی در کشتی‌سازی‌های ایالات متحده انجام می‌دهند، می‌توانند تا دو کشتی نیروی دریایی را در کشورهای خود بسازند و به ایالات متحده راه سریع‌تری برای گسترش ناوگان خود بدهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141638" target="_blank">📅 14:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر خارجه روسیه، لاوروف، در مورد اوکراین: ما روش‌های خود را بسیار سخت‌گیرانه‌تر خواهیم کرد تا هر چیزی که ماشین نظامی اوکراین را از سوی غرب تغذیه می‌کند، نابود کنیم
🔴
و ما همین حالا این کار را انجام می‌دهیم. و آن‌ها همین حالا شروع به ناله کردن کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141637" target="_blank">📅 14:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnbICnGPkPiOJqd_o_s304sAQOXhS01akJmpRZzHMuO__Beb_JHiMorbaatDGxd5D2VRbjTRL6zILEeIUoG3RiMx9xSTm9SCcRpVwSbw-GopuvnuqZTnwSlZSsYI-bRwVkxWR8ovFwj_TXRyCYnq0LSxrw5jXi7FjKZ1d6QkZS1ZyZLkG6bzXo7M6VNs4mug_MNq6CoKso1QGbv3csW2dGUaCEsYwWQPUYWMqRg3mIzDJ5dL4xkbM3gf2kffksVCQ8uvk6nGmrWN9nLsn9u-14n_kQSoyjD8EMY1T8pLV_GQQjL21yGdVwco4ticAp8DUxIZuzcGB24DaqhYR9iUsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت، بحرین و مصر حملات ایران به دو کشتی اماراتی را محکوم کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141636" target="_blank">📅 14:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141635">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سخنگوی وزارت آموزش و پرورش: مدارس در سال تحصیلی جدید همزمان با اول مهر، به صورت ۱۰۰ درصد حضوری فعالیت خود را آغاز خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141635" target="_blank">📅 14:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141634">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejo5iTuXM3UCZq51Xl38HYZLO7ZbfH0msPTGvpFOOJogyt4-Z8qjY-8pD9msJ0n7prVMa4-V0Ud_5rjnSHjloXsF3r1IwZPLtdHyMeFl2TZx2K61UZLbtrZE1nOEdgo9tr4dXdikqEXFRz3zFDtMAL66hHIrZ6v3qkEOxyzLf7jnobnEISRymQwLXLx7JOwCBJ-PpSJEWVwUEpbNV7R-4kmAD6mc_f9iEb7T79l02rSSlLbvYP_msy5wyjiEZ2fQeIiY9FR5-g7MXStyVqfGVawvYYnVffEJncvFFTRFPdgwTyH9gcGtMV3PQyVJic4fpIAvxy9SRSjAXzSw8yzgoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لهستان در حال بررسی انتقال یک دسته اضافی از موشک‌های رهگیر دفاع هوایی پتریوت به اوکراین است و انتظار می‌رود تصمیمی در سطح بالای دولت در چند روز آینده اتخاذ شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141634" target="_blank">📅 14:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141633">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
دیدار کاردار ایالات متحده با وزیر خارجه پاکستان درباره تحولات اخیر منطقه‌ای
🔴
اسحاق دار: اجرای کامل و عملی در متن و روح تفاهم‌نامه اسلام‌آباد تنها راه پیش روست
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141633" target="_blank">📅 14:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141632">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان سعودی:
ما با شدیدترین لحن هدف قرار گرفتن دو نفتکش متعلق به شرکت اماراتی ADNOC هنگام عبور از تنگه هرمز را محکوم می‌کنیم.
🔴
هدف قرار دادن دو نفتکش شرکت ادنوک تکرار غیرقابل قبول حملات ایران به کشتی‌ها و نفتکش‌ها است.
🔴
ما ایران را مسئول ادامه این حملات می‌دانیم و خواستار توقف فوری آنها و احترام به قوانین بین‌المللی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141632" target="_blank">📅 13:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141631">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شورای عالی انقلاب فرهنگی: ۷۰ درصد مردم کشور تو تجمعات شبانه شرکت داشتن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141631" target="_blank">📅 13:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141630">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به‌بزرگی ۳.۹ ریشتر در عمق ۱۱ کیلومتری زمین، همت‌آباد خراسان‌رضوی را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141630" target="_blank">📅 13:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141629">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ان بی سی: بخاطر نگرانی از شرایط خدمه، ناو آبراهام لینکان به آمریکا باز می گردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141629" target="_blank">📅 13:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141628">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd7a971f8.mp4?token=En5HIkbmFw95ZC67nsdFfp3rzm7FRkHp5gJvkFop4OstlVpRG2Lj4d_bRG4gnpFbqd2Nj-qCPChbK-lC2Iw0hlJhdw1ePiMc0Zu88Vatz67NlW4O5eOErnsPKQTC22rO7Xpuxy8kaudzNiiRC0pup6BghLeTz6mq1tDDKUxmOCW6rj-ZmIor-T-S9FpzAZVntNn_ZGxN26GUkiSl8c1na9jybXJG4ppqcc6iUn-0GcdGuFMwPP9KPdvNQxTs0qGzBlWPx8ftc9aEkoIub-PWwgFduct61BkRjalbqIEvhHq99dOpWoTRHosn_68hvdrAAvVyWezZEzafEXCVcJznow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd7a971f8.mp4?token=En5HIkbmFw95ZC67nsdFfp3rzm7FRkHp5gJvkFop4OstlVpRG2Lj4d_bRG4gnpFbqd2Nj-qCPChbK-lC2Iw0hlJhdw1ePiMc0Zu88Vatz67NlW4O5eOErnsPKQTC22rO7Xpuxy8kaudzNiiRC0pup6BghLeTz6mq1tDDKUxmOCW6rj-ZmIor-T-S9FpzAZVntNn_ZGxN26GUkiSl8c1na9jybXJG4ppqcc6iUn-0GcdGuFMwPP9KPdvNQxTs0qGzBlWPx8ftc9aEkoIub-PWwgFduct61BkRjalbqIEvhHq99dOpWoTRHosn_68hvdrAAvVyWezZEzafEXCVcJznow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: همه چیز دوباره گران خواهد شد
🔴
رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141628" target="_blank">📅 13:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141627">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdwFxJ2O1I52QW8bLgkCNlWPEAdW4dXGJJXC2-6PpbVcJuWnD64V90ApHUkdimxIsCNDOgNvpYVJVUTQQuaurw5_Fz1odIt9CHGdzGEurL6wU9VZCRxefPkmsgZ3cfqYdRRDPsb9sxI9x9j_0Pdu9z-uIm-AOvlvIyvbf7MeS4vQ72VtpZmYvN-wYN5kLdpypKx7YD1OrYDssbKCLEpU24ZP7fcL95XWPxiXkdAOu1VOys_FDW0J-gelEI0pZO-IePdK_xs1DAG7YyAwhnR4BGvnPPTeDJuOOK2oRjmO94ortvwLVVspsbmD4AO-eay6IM111GptLU1G9Im4M2JHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه قم: آمریکا و اروپا و اسرائیلی ها می‌خواهند از قم انتقام بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141627" target="_blank">📅 13:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K0B5TtkuyH_O9za2hQxoj2frfowLVWi4_B97jQANB7eWaiWA6Z13UfHk2XRsT_IRkAwH96jTjH8rZdt-bhTDZI-ZaEVJQFuzT0TbWV5sxdvmfSQZlIdC3H_bPw_c2gXOV3p9JTFlIG8v2zTnKPlNH5m1yTZkglosFy-cnwMnPwErOnrBksR2NuRKa2GKCvHxEF6T9J9MzEquE0swJaL4oKeWEqydpDU5FwaVRv5YTb7pSsJLFR9xSxLzZxHhSxPjIr4k4uhWgNyUDysq2XLDu6sJImm8nHWULvBu3NZGkcO-2f-xgWkkN88Y2Ma956Zwhtqh2UBmXrei4BMuTliYXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EADHLwurSDo7D7WQ0jdcov-a9q74Qe5SJ82rKb0ScHBKrP8sR9P0moXgshJQmUDC9PRBzhxaosYYyVEG4-LgM2NLMB0vdObQ5-dSuPyHmDlBS2ia0YG8-RASGUk7-m2XQdcOIEsKnwnyEMnpiPzmCyC8PO1FMcXf7RB70A3ZXoVJj4HcwhDy8v1fwp3P_ETNOHhojgKIqdXX5HNfcvVvMXVQ6yiN1_9_O8hZggufH1i-fLV7voURkh2YD8-CrqZ0UiCL-gERZi4MLuTmyPMnzdoKTubdiic2kZSCDS_TYDr7gtYJ1QcRaxuMl3n28sRHuVFAkAlgY31FyHHv4fkULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9TieTSM_fh2jygiga_vTja8flAU5Wfy_JMZgw6ahxBhRJQ0YZ2AC5umPR2LXuRjwvpOIY7eGPV4E8tUJDyd7XLNIYbBJPJh8YZtuU3fHarrMhbzIbVR-jKrLg7gV_MlyV7Bgf-PKiqknl-Bs2gVZhTCyFQu2Oiw7QhOV0hkM0a-3pXB8CIlYZapDpR24ukh6WHRKO82tEHbDlybyGnuYetq8K0VVLZ5cpNXV4M0EQv9stwr7K9O-sGzyj-mcjiAs9Vsr4qQgqHEf1JHh8ywyubysK92bLWt9P1zO1WortuWyvj5006rO_-3wubnoHrijmk2GiHvmc9PsIQyY7lk3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1c3QaDZAY6vnpqQXk7zKU6-0bNOgsyVjeg6ysU-K-NUruHG4HyebyYjHNxc1CSTY5LykHdnghq3Qx7lS1THBb1YHp-IEkz2QcMRHgvagzBhm791r2v3HKPxgj9VTXnFQfzOr-Q0wIxB3BjttxHarKPIRTbmm3bZSsRcBl7iWhzclaLMD2lPHmoa4ZRIUJEoLv_hd4u01_2_IQZs205LDa_2JlPJQWzHEAE5kbT35n2D3oStedOGKCIYAm_wyLjYG6u6-qWs-EJHapRMkrxANaKzC-Gz2IZjJKiAoeXwqj6zyvQ9wh1gdCaICgirm9abmB38uWomc-faKvuEfJCCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هگست (وزیر جنگ آمریکا) این‌بار داره شنا میزنه
:
چندروز قبل از جنگ 40 روزه 143 کیلو پرس سینه زد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141623" target="_blank">📅 13:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c22R0tIUbD6d8TZ3zVGfIcx5ZR9PGy37gMJ7hbG6nSwHPkwiA8sfSkvoy27EgUxSx6tuXpcjlh2gRThQ9RosN4i1G1xrsoDTlc7c1dtvp5wksDxE7B9swyVUbuAF8rpkkiUj8Xlgqzo_YI5ovU2fV2lmMjciBPhGFj8GJQfDLGZ7kGW00IGPI1w-I3cH-KwbSz97HGVqndwZWbhT_MkgNKKXPSuYHaLgpLlk40QV_AxkdsDM3vb3ZbPT_sECPGYGX_G3kVOrKRB9kyaVxr5uRg4kXFeVGIfJUMsIi1Ti6_vJzLswm7tqmLohxhgXg1zgiOzGx8vmfis8iMRRdFNaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تولد بهترین پیامرسان دنیا، تلگرامه.
تلگرام امروز 13 ساله شد
🎂
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141622" target="_blank">📅 13:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19124ce5da.mp4?token=iGiMH9Q1EvwLilVo_7iaUPO-uQQyfbI7JFhMM3gG2bm9Jqvocwy7ELFXTtcFkrZ5l2seXScGHk2RLN7bKEGdISn_lNu42bIwhMMkpz1iGh4-uWTvA-kM-2c9oDPxcE0bwAe5zTZCZw1JW1yuoP_hPgCV8xdUoOdnEwY10BNgHV19WuECya8fEkd6cLEm3GqS5VBAZ7uq3K6xmCJAaCCEDdgSwDeIeGFxIojJG2u3nWd74iiaTAbkfVyQ91cUdq2xwZZfaT56uMIv2LGWCN48YyYmENXkPOOwjzGiap6k5dkmGJsSpUao33szBQXSWgD_wtnXh73MiWa11Jwdv0zaXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19124ce5da.mp4?token=iGiMH9Q1EvwLilVo_7iaUPO-uQQyfbI7JFhMM3gG2bm9Jqvocwy7ELFXTtcFkrZ5l2seXScGHk2RLN7bKEGdISn_lNu42bIwhMMkpz1iGh4-uWTvA-kM-2c9oDPxcE0bwAe5zTZCZw1JW1yuoP_hPgCV8xdUoOdnEwY10BNgHV19WuECya8fEkd6cLEm3GqS5VBAZ7uq3K6xmCJAaCCEDdgSwDeIeGFxIojJG2u3nWd74iiaTAbkfVyQ91cUdq2xwZZfaT56uMIv2LGWCN48YyYmENXkPOOwjzGiap6k5dkmGJsSpUao33szBQXSWgD_wtnXh73MiWa11Jwdv0zaXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای تایید می‌کنند که یک رادار در پایگاه هوایی الظفرة در امارات متحده عربی، پس از حملات موشکی ایران در ماه جولای، تخریب شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141621" target="_blank">📅 13:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5PGiEYJmx0ivWGoz-pzoC22pQ63WXwf7qXNoLws-9HSK3qFnCh31GqLT9lYsDo0zyqOZXhePBoMTLr9ZbAUYUmNrgZ8XlpprHVYEMVgMB5bJbzuHUcWdWUhqr5fyWeveJcpP7e69vVhCeuznM3EJscSy46H6YSiOahLr0AOqV99meXHMvqYThheYQ36fhGkheq4wHfK9jbQYgWTvoakwQ4rXS2AqNmu5kuJ4GjLoe4a742sd0dapH_27yjZmWjj9sgffJDhVtn5ip3dm_g4ueWHNMaOc_5Vg6l_h9A5GLsn0GiHw84F4WWrLLLCiaUQM30ZgxElB2CdIzl4JAJhBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری که خدمه ناو آبراهام لینکلن از داخل ناو برای خانواده خود فرستاده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141620" target="_blank">📅 13:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سطح آب دریای کاسپین به پایین‌ترین میزان خود از ۲۰۰ سال پیش رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141619" target="_blank">📅 13:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCGUxTHZ-nMqAB2CUIcpM6K60Jn8p-fyR17_HbH8bDYLkMAskQBIu4hbOretdFYaSpAlUxr-VKBK2PVWT9IrkO1GXYh5Eh86J4qwqTSJX-gmy5BuYxadVO2G2ei3l8Lp8Oo3QzP0POTHszLjAIlMpMeOXWE8tpG-DJBFX2P7mkA-aSKbFJB8dHIaAai4_FEAweQfNb32kgUOGqTvwLayE_HlG5JbL07FOh3FaqvBuDkU3aHiaKbZMOJzrwUa8AWR24qqinbOUt4YfoFwu3U8wcx3k3_O6k8zAmRFwuxSmaPHstXw54ZLB0AUfLDsbQrfhi6grOswisNYRBn4s5uc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین طاهری مداح: خون آقا مارو ۶ماه آواره خیابون‌ها کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141618" target="_blank">📅 13:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6-nOsPSlk0DSEQj0m2KGkuL7PLCc54eLmLxeu-_Th8VS5mly1Vw0zUkpM-It1qmsy2k7PtGZ8Sr7LU4Vxouz2qqj3bnBDNFTtmNF55V7dfpWHWGRRZhHuwRqoh87UsbAbNA3AabT5EqGBEAf2pDnuS6bmsEheL81MNRD3vzlUX8OQGzR0QIHKiHSFiEa28B5wvF8DWUT7RSBx4iOC86t84EqBsei9q5ap2x94r40IpDy-OX66v9NknkHKyy8XwtnKG8pknMpUBA9e17hJ9LuJOhDVT_9E78Wyr8gi4efDJ7pQ5K3BM1SX5Uhu9CssdG5F6PwjNotfdoW09vtfGDIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجری تلوزیون: مردم میگن حاضریم نون خشک بخوریم اما مقاومت رو ادامه بدیم و رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/141617" target="_blank">📅 13:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23bb362bf7.mp4?token=n--7_Ickrvw7fx5vBXHPmcFIymrxBvxKgiPF2WoWObjZ0XbdPX0MMXdmHWvUqy_DFSwmwR1T3HxE1pb13gYyvnff8Qs671Ujrygm1AsBJ-FGOUqzCJ1WJ9INJj58ehHXd0aPbUTVrj9ymzLqjptthRDAWd_RGdxsOmBQyMk32LRQ32LWo7MXYrp6fmqcxrfulH3Ml9LskxrnV8rN408of539DGW_H9uleWYgp06gNtDB4lt_Q1VtA54-2xvaHkHPfeTjt9PtAEf-jwNo-IivzEONsLXuBHlS2kDUgRFYRhUZMo1X6WhwCIx_IgKlLSU1_zaoMaai6xobDYYJEu49Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23bb362bf7.mp4?token=n--7_Ickrvw7fx5vBXHPmcFIymrxBvxKgiPF2WoWObjZ0XbdPX0MMXdmHWvUqy_DFSwmwR1T3HxE1pb13gYyvnff8Qs671Ujrygm1AsBJ-FGOUqzCJ1WJ9INJj58ehHXd0aPbUTVrj9ymzLqjptthRDAWd_RGdxsOmBQyMk32LRQ32LWo7MXYrp6fmqcxrfulH3Ml9LskxrnV8rN408of539DGW_H9uleWYgp06gNtDB4lt_Q1VtA54-2xvaHkHPfeTjt9PtAEf-jwNo-IivzEONsLXuBHlS2kDUgRFYRhUZMo1X6WhwCIx_IgKlLSU1_zaoMaai6xobDYYJEu49Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم یه عده مردم برای‌ شله مشهدی به داخل مسجد طرقبه که باعث شکستن لوله علم گاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141616" target="_blank">📅 12:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
عملیات خنثی‌سازی مهمات عمل‌نکرده در کنارک از امروز تا ۲۶ مرداد انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141615" target="_blank">📅 12:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141613">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ونس، معاون ترامپ:  درباره ایران هدف نخست ما حفظ ثبات قیمت انرژی و هدف دوم این است که اطمینان حاصل کنیم ایران هرگز به سلاح هسته‌ای دست پیدا نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141613" target="_blank">📅 12:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141612">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
الحدث: وزیر خارجه پاکستان پس از بازگشت از سفر به ایران، با سفیر آمریکا در اسلام‌آباد دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141612" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141611">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‏
👈
ثبت ۲۱ فوتی به دلیل غرق‌شدگی در سواحل مازندران
‏
🔴
همزمان با اوج‌گیری حضور مسافران در سواحل استان مازندران، گزارش‌های رسمی از جان باختن ۲۱ نفر در آب‌های ساحلی این استان خبر می‌دهد؛ رخدادهایی که ریشه در بی‌احتیاطی و نادیده گرفتن هشدارهای ایمنی دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141611" target="_blank">📅 12:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141610">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سخنگوی هیئت رئیسه مجلس: فرایند قانونی استیضاح وزیر کار انجام شده و عملاً باید در دستور کار قرار می‌گرفت، اما بنا به هر ملاحظه‌ای این اتفاق نیفتاد
🔴
با این حال، فرایندی که طی شده همچنان به قوت خود باقی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141610" target="_blank">📅 12:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141609">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
اینترفاکس به نقل از لاوروف: ما تلاش‌های خود را برای نابودی همه چیزهایی که غرب برای تقویت ماشین جنگی اوکراین ارائه می‌دهد، افزایش خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141609" target="_blank">📅 12:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141608">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یورونیوز: جنگنده‌های ناتو در مأموریت گشت‌زنی هوایی بالتیک، پس از ورود یک پهپاد به فضا هوایی لتونی، آن را سرنگون کردند.
🔴
جنگنده‌های اف-۳۵ هلندی مستقر در منطقه برای رهگیری پهپاد به پرواز درآمدند و سپس آن را سرنگون کردند.
🔴
مسئولان لتونی در حال بررسی منشأ پهپاد و شرایط مربوط به نقض فضا هوایی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141608" target="_blank">📅 12:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6pKHmQCZBSyDCN_scjz7ng1PdoguNlsOj5PU0Bq5hOuiPTOAzgTPfsmxwtk2oYDZL4XqxVYVe_evaSpsPNna75Eo3BcA1VbSVRqwHVaOXfCbuoj2LTnV36j9GXJrp_OfKRzkclJ8E2CWF_ZVGNtSCz5DMORpb62jf0Uf12bIwsj-Abr6WAONf4AZSuHhOYwSx4gsZ-q440qv1zzdyuealPcj9nnHRhQMXIfSkNnJgys4FvwCqqyzPyh4TBWQWtim6e3C40Uqd5tQ0nAP-xvXqIM0dvJYDEwA2fMFWK3Ir4KBMFm0dPPPcPbj0RHOdLDfhkJH8i_fIDmKXzSJq8vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به‌گزارش سازمان تجارت دریایی انگلیس یک نفتکش حین خروج از تنگهٔ هرمز در آب‌های نزدیک شرق شهرک بندری «الخصب» مورد اصابت یک پهپاد قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141607" target="_blank">📅 12:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0o6kVE9eipmMkhEtmymIRlBN2hF_hnr4wpNG5nVPM6Y5edNVAxEDyM_u7H8fVz3WlZ97sD-98EQQlRsdQzCadOcuHIBTrnzGaP16EjB8gVxODkOSXFePKmg5nxC31aNHtE7XW3Ckjnva6AfRhbnCjC9TF7dqkv_pTr35dOntSCYuLOCO1PhbTojtabsm61XCcRYKCj0Pnh0X1v0EQyGClzfxwtbNg5dpbe2xM64nvzaHVIoT6FCpYu4PFSuFw9aoFsYqN3aUxtIC3GuXaUdPVDBxLRmd6g1drhaPk5QhMDquvUUXu7jmCmgoOyuBL9sKavZCv0xoTOn5grkqXE8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رهبر دموکرات‌های سنای آمریکا: وقتی پیتر هگست نامزد شد، همه می‌دانستند که او کاملاً نالایق است.
🔴
اکنون دریانوردان شجاع ما به‌طور وحشتناک و غیرقابل درکی در حال پرداخت هزینه این موضوع هستند.
🔴
پیتر هگست باید فوراً اخراج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141606" target="_blank">📅 11:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141605">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
رویترز: به گفته منابع، اپل مدل هوش مصنوعی خود را برای بازار چین با پشتیبانی علی بابا توسعه داده است.
🔴
این مدل برای تقویت هوش اپل در چین و در عین حال مطابق با الزامات نظارتی پکن طراحی شده است.
🔴
اپل در حال آماده شدن برای راه اندازی این سرویس در تلاش است تا موقعیت خود را در برابر رقبای چینی گوشی های هوشمند تقویت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141605" target="_blank">📅 11:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141604">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
یک تانکر در حال عبور از تنگه هرمز مورد اصابت یک پهپاد بدون سرنشین قرار گرفت.
🔴
این کشتی آسیب جزئی دید، در حالی که تمام خدمه سالم هستند و وضعیت آن‌ها مشخص است. هیچگونه اثرات زیست‌محیطی گزارش نشده است. این حادثه در نزدیکی شهر خصب، عمان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141604" target="_blank">📅 11:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141603">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
شهباز شریف، میانجی‌گر ایران و آمریکا: هند سر عقل بیاید وگرنه پاسخ مستقیم می‌دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141603" target="_blank">📅 11:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141602">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804aec2cf3.mp4?token=diAKQm9ZH0maoY36SBgvElQhX_dwtrEkb9QotXiwFHva0dxx76bzzXe-G5qib-FPUmfF5AswHciTKTowTcdFKAilg0-ClQm_Z7ojfBLiS6UcD6mmmAik6pfPmmlNUlk_N6cT9M6WgLZtJwu245cj8p-fsXac5eKD5Q5tBUkCdj34utqJ-KlcsnK96eb--IZ6pjD0E5dj2AlMw3-KwcL2WC_YTHbVvcG1cVLvGwLXJLeJMEoPMX0bHVCJ-rLU-mpKSg1Rkn4evyPWnR3PvNtyniNLw-fJxLefup7p5W123GkgVeLyXycngMLZjoq3pDmDTNkKiwJ1F4sGzb3klAh8Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804aec2cf3.mp4?token=diAKQm9ZH0maoY36SBgvElQhX_dwtrEkb9QotXiwFHva0dxx76bzzXe-G5qib-FPUmfF5AswHciTKTowTcdFKAilg0-ClQm_Z7ojfBLiS6UcD6mmmAik6pfPmmlNUlk_N6cT9M6WgLZtJwu245cj8p-fsXac5eKD5Q5tBUkCdj34utqJ-KlcsnK96eb--IZ6pjD0E5dj2AlMw3-KwcL2WC_YTHbVvcG1cVLvGwLXJLeJMEoPMX0bHVCJ-rLU-mpKSg1Rkn4evyPWnR3PvNtyniNLw-fJxLefup7p5W123GkgVeLyXycngMLZjoq3pDmDTNkKiwJ1F4sGzb3klAh8Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چین برای نخستین بار تصاویری از بمب‌افکن استراتژیک H-6N مسلح به موشک بالستیک هواپرتاب JL-1 با قابلیت حمل کلاهک هسته‌ای منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141602" target="_blank">📅 11:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141601">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شرکت ردیابی کشتیرانی کپلر:
ترافیک دریایی در تنگه هرمز در اواخر هفته از میانگین ماهانه خود کمتر شده است
🔴
روز پنج‌شنبه تنها ۹ فروند کشتی از تنگه عبور کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141601" target="_blank">📅 11:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141600">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزارت دفاع امارات متحده عربی اعلام کرده است که به سربازان جدید برای پیوستن به نیروهای زمینی نیاز دارد.
🔴
رسانه‌های عربی علت این اقدام را فرار بخشی از سربازان بخاطر ترس از درگیری با ایران معرفی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141600" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141599">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رویترز: ایالات متحده با توقف مذاکرات، محاصره دریایی ایران را به‌طور نامحدود ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/141599" target="_blank">📅 10:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141598">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc7dcbf49.mp4?token=N8HAnSI7KQH7RPAoV9a5711RErXArYrxTG18C5hMfnBJqss3WC6bGoj6pbgDFCY2YARJHuMPIMQWmkBhpYkb02WJapGVvF-83Q1HSBGJcHGwi3el59qVio8L54y54wn7xwfnJ-n1XF9GSmcgJM2EfYVU6kILHGAr3Zs_EzwUBOLQcFwqBzszUxuXgbIEvTuPBamrRCgLe_X08d0YbEA52n6JPPxPePzVyyj41MCQAR-4aSpzYEdDd1YPGbPi2ZuPuenAaoVUK2TcPLh7bzI17EKOvFBlW7THzI_mFk9ponq0zDPgezl5KKInRmtIwx75nnPXe4Mc5ULkeyoLyQiSRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc7dcbf49.mp4?token=N8HAnSI7KQH7RPAoV9a5711RErXArYrxTG18C5hMfnBJqss3WC6bGoj6pbgDFCY2YARJHuMPIMQWmkBhpYkb02WJapGVvF-83Q1HSBGJcHGwi3el59qVio8L54y54wn7xwfnJ-n1XF9GSmcgJM2EfYVU6kILHGAr3Zs_EzwUBOLQcFwqBzszUxuXgbIEvTuPBamrRCgLe_X08d0YbEA52n6JPPxPePzVyyj41MCQAR-4aSpzYEdDd1YPGbPi2ZuPuenAaoVUK2TcPLh7bzI17EKOvFBlW7THzI_mFk9ponq0zDPgezl5KKInRmtIwx75nnPXe4Mc5ULkeyoLyQiSRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرای حوثی که توسط ارتش یمن اسیر شده اند به عربستان سعودی درود می‌فرستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/141598" target="_blank">📅 10:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141597">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
شرکت دولتی نفت ابوظبی (ADNOC) اعلام کرد دو فروند از کشتی‌های این شرکت امروز هنگام عبور از تنگه هرمز هدف حمله قرار گرفته‌اند.
🔴
‏ بر اساس این گزارش، احتمالاً نفتکش‌های متعلق به ADNOC با موشک هدف قرار گرفته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141597" target="_blank">📅 10:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141596">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزارت جنگ آمریکا: در حال بازبینی استراتژی هسته‌ای خود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/141596" target="_blank">📅 10:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141595">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgCQZ1Ruez45yZfMcBiuBYy8AvDn7cdsIcE4EDZNECBbJssVqSrsTOFYPvD7Do9w2XqCgb4IsQXOvi6SQn7r1O1GnZH5LOHcrrHeUNt68-LvonmziN6NNDirvF-gnq14kD4PrgC57cH-7Mr8n6wGTxP8QkF2RBXPj-Ph9dFyXlKjgybLu6eFkYCi8nZ_wkTIXfFbyXarBtUvW7Gn4KntoDbJMWkvhg43ttPXRLs19is1myyRIziKLiI4EtrJXcExZ_T4TGEUy4VygsiGtiFHk6I4YzLV_-7lVhTjMF8lQ5zb8ta92_NJM3J3oX9CYrjOJS1_fTz9zUQr8o5mAIJU9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشک دیک چینی، معاون پیشین رئیس‌جمهور آمریکا، نسبت به وضعیت جسمی ترامپ ابراز تردید کرد و گفت تورم پاهای او می‌تواند نشانه یک مشکل حاد باشد.
🔴
به گفته او، تشخیص «نارسایی مزمن وریدی» با گزارش پزشکی قبلی ترامپ که اشاره‌ای به تورم نداشت، همخوانی ندارد و همین تناقض احتمال بروز ناگهانی مشکل را تقویت می‌کند.
🔴
سلامت ترامپ حالا دوباره به یکی از موضوعات بحث‌برانگیز سیاست آمریکا تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/141595" target="_blank">📅 09:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141594">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
دیدار محمد بن سلمان با فرمانده سنتکام
🔴
طبق گزارش خبرگزاری عربستان، در این دیدار درباره اوضاع منطقه‌ای و تلاش‌های صورت گرفته برای کاهش تشدید تنش و تقویت امنیت و ثبات در منطقه گفت‌وگو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141594" target="_blank">📅 09:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141593">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رائفی پور: ماهم باید یه ارز دیجیتال مخصوص کشور های اسلامی بسازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141593" target="_blank">📅 09:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141592">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvixxSZFYSoD8zAVgLAGHcWXmZk_lCNMiaNYczLN0t0Pr9In2WDVNvycEyPU4H8C8xbVjtjAJvQhHUa1swuF3MVmZmnne8VAdVNBplRSjppBjBARZOBxsp_cBJ76UwND0WEiAZ166qZd-sRFu6FFr5e-peyrowgQfMFl6dTqkSNMS_VfmEyXyVjYzamigl5Jranr9V4wWiDoclHPjNJ8CFxxsaecA734i6NzYZoqrmo05g8H0vr--olWDipxjnJQfo2vo8jV-O7_n-jm1UsX8MEGXyGHHgo6aMnyLPGBXcqxJN_VgVOOKkTZYeRMCS3Q6YnjMMjXgWC3YvAshlZlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تلگرام ۱۳ ساله شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/141592" target="_blank">📅 09:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141591">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4970a84a03.mp4?token=je5I7694mngec6BGiemkx2RNTS86nl8YFEtyMEOi8J1Fuw2Gzad6iuyqjLYPeCYBpFTOo5bY_jwxIrrn3PQCPsduXHvqD_zSdT5GJHapia6zud5oYxATlF1lp-vz4WjqrwGtuatIEoGQeO0U7snxTIXD5Wbo4Fs7wRFVHXqoyf8LmHPFbliZ5QMRMR9NkYkXrzVJ9CMLYniGIBkexyD1t9I13Jg8Jn-ougBadjiWwZoVsgV8urGT_QLwwo0ZYmMd8yJd4xix_Y79yX_mSk0m738dJlzEIOocFM_NQTC5xZ5FDqZ_6FKC6oLrizXIhvzYMjqtRfVHlEjjF0-XYuHqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4970a84a03.mp4?token=je5I7694mngec6BGiemkx2RNTS86nl8YFEtyMEOi8J1Fuw2Gzad6iuyqjLYPeCYBpFTOo5bY_jwxIrrn3PQCPsduXHvqD_zSdT5GJHapia6zud5oYxATlF1lp-vz4WjqrwGtuatIEoGQeO0U7snxTIXD5Wbo4Fs7wRFVHXqoyf8LmHPFbliZ5QMRMR9NkYkXrzVJ9CMLYniGIBkexyD1t9I13Jg8Jn-ougBadjiWwZoVsgV8urGT_QLwwo0ZYmMd8yJd4xix_Y79yX_mSk0m738dJlzEIOocFM_NQTC5xZ5FDqZ_6FKC6oLrizXIhvzYMjqtRfVHlEjjF0-XYuHqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد هواپیماهای سوخت‌رسان آمریکا این هفته دوباره به پایگاه هوایی «الظفره» در امارات بازگشته‌اند.
🔴
بر اساس این تصاویر، از ۱۰ اوت دست‌کم چهار فروند هواپیمای سوخت‌رسان در این پایگاه مستقر بوده‌اند؛ تحرکی که می‌تواند نشانه افزایش دوباره ظرفیت پشتیبانی هوایی آمریکا در منطقه باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141591" target="_blank">📅 09:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141588">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b327ec33.mp4?token=eQb9c1KZ6VlyiNOZVkfBKNwDh8biE6I7cIfJN2kLOpL5WJh7WPReI9_lJIxf3uYQkc_kGvwNP67OuUoi4X_0HJbROtt_wL3B_nf0N1oBwQAUvO62R7ZA013KPrwyNgNar2FrE4odgzdHLVfeY5wmiGl4LDgk35usfPwr-2Zbx2YbopmkIicO3pK-C8P22iAZeXkmro6xXhdwVmuD0BydqjVi3GDpIOnkv8GZxiQpewoSlW-4CGPd2l6fWkLNBGDPDomt0hgfrUjMOA5mZJmvEoRCnn213ambHrcNvySH6UpKcT2MkxyryA9g89DEA795rWRENbb7GHau8M-yEv_WQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b327ec33.mp4?token=eQb9c1KZ6VlyiNOZVkfBKNwDh8biE6I7cIfJN2kLOpL5WJh7WPReI9_lJIxf3uYQkc_kGvwNP67OuUoi4X_0HJbROtt_wL3B_nf0N1oBwQAUvO62R7ZA013KPrwyNgNar2FrE4odgzdHLVfeY5wmiGl4LDgk35usfPwr-2Zbx2YbopmkIicO3pK-C8P22iAZeXkmro6xXhdwVmuD0BydqjVi3GDpIOnkv8GZxiQpewoSlW-4CGPd2l6fWkLNBGDPDomt0hgfrUjMOA5mZJmvEoRCnn213ambHrcNvySH6UpKcT2MkxyryA9g89DEA795rWRENbb7GHau8M-yEv_WQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم‌های اضافی دیشب از اربیل، کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141588" target="_blank">📅 09:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141587">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: در هفته آینده منتظر اعلام خبرهای بیشتری درباره ایران باشید؛ ما اقداماتی را اعمال خواهیم کرد که در تاریخ انزوای اقتصادی یک کشور تاکنون سابقه نداشته
🔴
این اقدامات ترکیبی از انزوای اقتصادی در سطحی خواهد بود که جهان تاکنون مشابه آن را ندیده و همچنین محاصره دریایی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141587" target="_blank">📅 09:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141586">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سنتکام: ناو آبراهام لینکلن با وجود ۲۶۰ روز حضور در دریا، یکی از بالاترین نرخ‌های تمدید خدمت را دارد.
🔴
سنتکام اعلام کرد خدمه این ناو با ۸۴.۴ درصد تمدید خدمت، ۱۰ هزار سورتی پرواز و مصرف ۱.۵ میلیون پوند مهمات همچنان پایدار و مصمم هستند. هیچ نظامی روی این ناو جان نباخته و ملوانی که ۳ اوت به دریا افتاد، سریعاً نجات یافت. سنتکام گزارش‌های منتشرشده درباره شرایط ناو را «گزارش‌دهی نادرست گسترده» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/141586" target="_blank">📅 09:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141585">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fc5bfffff.mp4?token=n2wb2TY-c1B7UEKFBlCrHmpuvjoiG6WUogJ0o6acUdf6w1t0qOBElytEtyJXOU9Wu67ottuE4AvzrQuLTqRUJgP8w0MglUoK9R9uJ2_NTL0FVJ2wTLgcPGDkQmD2gskk0-ev9AI6F_AzaTkz8qEQrerVI6hHkVmPxiYVxdMJlTVoT_h0gy78DQVxRChK0xjz50KfpAeoPAWH4-ciKWOYHtXJFELuxZRLCl_lIt-fItYdgjgjHEH5iI5WP1q9lZKa7E-9aP6kiuKbbwjiiE8d-AXho7Nwq0wcPseh2uVjF8ca6q6FDhrek083NsdngAGkk8u7etN55nfriHEhaxJ9Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fc5bfffff.mp4?token=n2wb2TY-c1B7UEKFBlCrHmpuvjoiG6WUogJ0o6acUdf6w1t0qOBElytEtyJXOU9Wu67ottuE4AvzrQuLTqRUJgP8w0MglUoK9R9uJ2_NTL0FVJ2wTLgcPGDkQmD2gskk0-ev9AI6F_AzaTkz8qEQrerVI6hHkVmPxiYVxdMJlTVoT_h0gy78DQVxRChK0xjz50KfpAeoPAWH4-ciKWOYHtXJFELuxZRLCl_lIt-fItYdgjgjHEH5iI5WP1q9lZKa7E-9aP6kiuKbbwjiiE8d-AXho7Nwq0wcPseh2uVjF8ca6q6FDhrek083NsdngAGkk8u7etN55nfriHEhaxJ9Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری پهپاد شاهد-۱۳۶ در اربیل، کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/141585" target="_blank">📅 09:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141584">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
الجزیره: در پی گزارش‌هایی از کمبود غذا، خرابی سیستم‌های لوله‌کشی و بحران‌های سلامت روان در میان کارکنان ناو آبراهام لینکلن، اعضای دموکرات کنگره آمریکا خواستار شفاف‌سازی در مورد وضعیت این ناو شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141584" target="_blank">📅 08:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141583">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b62202eee.mp4?token=edQ7Q1MZLfFoNNXMULy4wgveYpEK9Q1puRJo-xnLtyCNIqJ3CjP5FWQ3iG2w_jICH_VgDhYvNn9_50FIJMcM0-uTXiYZAR116_8mItdS-_AutcZSsNB6M6PsTCg2ESzXWqVc8LWRrFMCdRhtkR21ACvHxfRMi7R82H1IGwfuOfrEAeai-WAiyU2ff4289HdT7YpFoDZdgLslqLIWixG1MASnMXRu2K7VPNmkqXCEKQkt7FVcK-J7rCJuLoAmfL6tBaA5Wx7yyaEbnGJ9i25qBkYah50R0FRGR4vroEqy6ceZko6Mti-RzoALAw7CLMfst2J0YuL8Wz6bnHTwqlWMkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b62202eee.mp4?token=edQ7Q1MZLfFoNNXMULy4wgveYpEK9Q1puRJo-xnLtyCNIqJ3CjP5FWQ3iG2w_jICH_VgDhYvNn9_50FIJMcM0-uTXiYZAR116_8mItdS-_AutcZSsNB6M6PsTCg2ESzXWqVc8LWRrFMCdRhtkR21ACvHxfRMi7R82H1IGwfuOfrEAeai-WAiyU2ff4289HdT7YpFoDZdgLslqLIWixG1MASnMXRu2K7VPNmkqXCEKQkt7FVcK-J7rCJuLoAmfL6tBaA5Wx7yyaEbnGJ9i25qBkYah50R0FRGR4vroEqy6ceZko6Mti-RzoALAw7CLMfst2J0YuL8Wz6bnHTwqlWMkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات پهپادی شب گذشته به مواضع گروه های کرد در سلیمانیه عراق!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141583" target="_blank">📅 08:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141582">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرنگار روزنامه جروزالم پست:
تیم هاوکینز، سخنگوی سنتکام به من گفت که گزارش‌ها درباره اینکه برد کوپر [فرمانده سنتکام] در جریان سفرش به اسرائیل گفته است که برای از سرگیری حملات علیه ایران تلاش می‌کند، کاملاً ساختگی هستند و صحت ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141582" target="_blank">📅 08:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141581">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d86cbc5f3.mp4?token=eCCAKJJRldK1hh6VPaHMWNmeWlMJSji4M0BUX4ehCevYKBsfNcsnK1XFj0sv9w_x69t2nj_XVz1BRL1LzZ-ZOLCDHa27bC4Q-MZdyjLTKa71wR8Zb4_jeS5lRCxC0lvpwBNYuef1W-QTgLQzYh6B0QHRQr_ZLyLOTPCOQ9gigRrW5SZcuvnpardmxKE4ZgniANEg7gtUglhdnnilcyhg8KZSnLmxyD3mBOfLYgbqH6wSbK87ZaR0cxe-__3LxeXm-cl6CYFrmAZuG3u2x-GCLjTBf30IK7bot-1EggTwtWHQFWEfJ7H9HYMCb-XIxB1CucZbujSVude8DtbTEPPMsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d86cbc5f3.mp4?token=eCCAKJJRldK1hh6VPaHMWNmeWlMJSji4M0BUX4ehCevYKBsfNcsnK1XFj0sv9w_x69t2nj_XVz1BRL1LzZ-ZOLCDHa27bC4Q-MZdyjLTKa71wR8Zb4_jeS5lRCxC0lvpwBNYuef1W-QTgLQzYh6B0QHRQr_ZLyLOTPCOQ9gigRrW5SZcuvnpardmxKE4ZgniANEg7gtUglhdnnilcyhg8KZSnLmxyD3mBOfLYgbqH6wSbK87ZaR0cxe-__3LxeXm-cl6CYFrmAZuG3u2x-GCLjTBf30IK7bot-1EggTwtWHQFWEfJ7H9HYMCb-XIxB1CucZbujSVude8DtbTEPPMsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هشدار عضو کنگره آمریکا: ذخایر موشکی به‌طور خطرناکی کاهش یافته است
🔴
راجا کریشنامورتی: گزارش‌ها می‌گویند ذخایر موشک‌های دوربرد ATACMS و همچنین موشک‌های تاماهاوک رو به اتمام است. از سوی دیگر، ذخایر رهگیرهای SM-3، پاتریوت و THAAD نیز به‌شدت کاهش یافته؛ سامانه‌هایی که برای مقابله با موشک‌های بالستیک حیاتی هستند.
🔴
در نتیجه، قدرت بازدارندگی آمریکا کاهش یافته و این وضعیت می‌تواند دشمنانی مانند چین و روسیه را به اقدامات تهاجمی‌تر ترغیب کند.
🔴
آنها میزان ذخایر مهمات آمریکا را زیر نظر دارند و کاهش خطرناک این ذخایر، آمریکا را در موقعیت آسیب‌پذیری قرار می‌دهد."
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/141581" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141580">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAtMzluOZU6dvuLSTaPjGG_HeIfZYOeAigYUioQsrnlrkvJN0EX-kiJt6s7gMTM6rEpag07Oww530wnzil_hI0xRAXmp33k-M4NiJZN_710sX4x6fG_5Z3yQPqHI8IQbgUae43_JdXzpYsMjbm6xcsoRhqAyp-0dMM_ksno1ytqeDstyXvSSn9wK0H7sWPDt7uXOG76p8FJkbvWM0TSUAvRf4lkBfoBMGXb2hwZob1PQMZRh48PmqbuTTIEKENnxcG3snfps1EOHWHLdRrhDDERvxaRWh3TFbtLY9Mg1hahSHDWlVVOgqknqB9i2JJA1kKdJgYJHivr3nvXrrHISHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوتی عجیب شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/141580" target="_blank">📅 08:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141579">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bcc1ba8a9.mp4?token=qBe04Qgdr5HCqPpYy2Yd4S9qtr8swB_8iFUC7gqRWsAt-SLf2fwhFILv91fxF7kJWfsWF0uuLAkfepu_NPl1M8VmRdZxbyenMLflAUka3UORw3aclJdNoPCQal3bmmUwRpmjyaenmF2hqjQ_4JrcgMIjN9iHtBZmi6OH_WUbnpPmAa-q1fhp4pmZ4PfT3yrxZ5FifzrrUs5rNiUr69OcFIBzqGRmo8XZ3asO9iBoD3Vnx1JNcRdjL-MyAwty3AkaouoJLgzVyQ4g4aoZDgm3-vW4xQLkSwG-UEou3_f_5PCDyOPlBNrqtdFsE0hnXaf-bTIMoeVIXTEXKUt6JHGL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bcc1ba8a9.mp4?token=qBe04Qgdr5HCqPpYy2Yd4S9qtr8swB_8iFUC7gqRWsAt-SLf2fwhFILv91fxF7kJWfsWF0uuLAkfepu_NPl1M8VmRdZxbyenMLflAUka3UORw3aclJdNoPCQal3bmmUwRpmjyaenmF2hqjQ_4JrcgMIjN9iHtBZmi6OH_WUbnpPmAa-q1fhp4pmZ4PfT3yrxZ5FifzrrUs5rNiUr69OcFIBzqGRmo8XZ3asO9iBoD3Vnx1JNcRdjL-MyAwty3AkaouoJLgzVyQ4g4aoZDgm3-vW4xQLkSwG-UEou3_f_5PCDyOPlBNrqtdFsE0hnXaf-bTIMoeVIXTEXKUt6JHGL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط پهپاد روسی در خیابان‌های کی‌یف پایتخت اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/141579" target="_blank">📅 08:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141577">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f61ac0c79f.mp4?token=EmJBZnQma_hNkCnoe7Q4DZZ4rK_jTyCL4T8ZV2m5SFb5FmodFTzbRJD5TZ9o-eQNAAtU_yqGqrvQ333ux1Hsvgdx0YqvjvZ1qLJyNPvmRsHUxk2EQr5x-FEW_S9u8endVTNVaYhD3sxU04ItGXGCenqy5XLrE9-sHbBnvpc5bQ3grkgB7uwkv1--QVIrdm_u9v6yCe0VRGjRzZOp1d3-zHn9RZIFVedpSgtnTPW-fgW1pnfom5xKXgHP2X-qftTMoh7yA5tZ7c3JiB6x8ghrw9ul_L22n8w4kfoXC9TKj0bkyiLhBybKeGERrQLDWraqB9Q_2NjxqryzYpXnLeMzKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f61ac0c79f.mp4?token=EmJBZnQma_hNkCnoe7Q4DZZ4rK_jTyCL4T8ZV2m5SFb5FmodFTzbRJD5TZ9o-eQNAAtU_yqGqrvQ333ux1Hsvgdx0YqvjvZ1qLJyNPvmRsHUxk2EQr5x-FEW_S9u8endVTNVaYhD3sxU04ItGXGCenqy5XLrE9-sHbBnvpc5bQ3grkgB7uwkv1--QVIrdm_u9v6yCe0VRGjRzZOp1d3-zHn9RZIFVedpSgtnTPW-fgW1pnfom5xKXgHP2X-qftTMoh7yA5tZ7c3JiB6x8ghrw9ul_L22n8w4kfoXC9TKj0bkyiLhBybKeGERrQLDWraqB9Q_2NjxqryzYpXnLeMzKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب تو صحن امام رضا مردم داشتن با چوب عزاداری میکردن
اما چند دقیقه بعد بین یه هیئت یزدی و تبریزی دعوا شد!
بعدشم شروع کردن با همون چوبا همدیگرو کتک میزدن و پرت میکردن تو سر و کله همدیگه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/141577" target="_blank">📅 02:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141575">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7_B3HBVFNUUEWaUt8qAJa7SvLbxtpgqiBdVbUez9XCuw2qYOIcB3id2_bgB2mxXBUFCu0-vNEIhVvIx95zQm847gIW1dkVbLdXfsaSVcLRAJY-7QpmNVGcoanWbeFpHmnfwneleegU3b9mR_zqFyCj_vmf7DNgF3zjKIselKHeSnVEtFuwtPZqAOLjnGOHHz6IEfihyUzmjqSu81j7jj0jHeeF0sHbNb0sQtzUNWMkX1KgQRrM5RENqXy2TXII-LHr6ENT2rwim7whUlOn-1bjOOkYEChPmtL0OEpMI_eJFd7IpEddjSC994SEeCKAriA0y_BX2wwacUgQbp7nvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjH2ru6G3mNTDTawa-I8a75qLEAYeKdDn66mn27jLTZgPCvGmrEBm-QtmWkM3omjgcDt46bqLzLUDTE6Ytqf8m31G2g0Cj4yCMEkts8ZygZNC_lKpMpX9GCO_ZyZGr0r_91KqKu7IjoDzaweB1Hk5-2YyE0yPx6pgIYzekKQrWd_xRB1DG-vp_cEltVZTkL_uAlgJXlgOJIli-B0oua7Tb__2KHVWxyyZginn6VxAlDDr1zQKfQZPGT15WxYfBMGQNvWmJue1myzvSab30B_Xsx-7010PUnp6FJ9zFdUFuJKWcKziwtWFhAtsl7FTEF47LvYd8hC7EkvKMEpoUmYpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
صدا و سیما به دولت، خوارج گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/141575" target="_blank">📅 02:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141574">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAR0-nHaU_wKpIrQB_9V7JMOn84OMPdXw3zxSX_Q6fqdM4fqor-DNH_EATXzqa6bMM-G5E_cELSg40slR0ko-Y1chsjsqQFvklc7ykCYPcxvI2d1MZqsJCVBc9pRbAsfZ-TcIpUMncPnVNgiuZjE8aN4J-bbA5qejNy1BZenWhQPH5joSm-jiD7GCclBi6ovuZQ2bPrVp-oCeXuP_Wdx8Ccvv5BiG4G_-B1ObjPJFbD0poRPoEGuAzJjRfhLXcdRFpC2R_G8co37uqX5CQ-WXfpaqzElw501jI8N15sbFKmiAOpzw0pEbwlifBVFlTwrFa5COdoDJKSs7WGHW2OehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
7پالایشگاه از 10پالایشگاه اصلی ایران قبل انقلاب ساخته شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/141574" target="_blank">📅 01:36 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
