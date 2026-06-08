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
<img src="https://cdn4.telesco.pe/file/t_lD_O9vtDOjG8xFisZ-Zi4gbfTCblaJ6Fi9AnO-jDVbp41P-ahX7ZFCsWHxa6SPcq5eFQ0FIuoMfQ_9okzyTw0KdM6NLJvLNExhWVmVR-wFeEg1bqiQoy8FlkQTFFnvDTJZs5tcJeGY8VRQ3w2g06yJ0N52qeukL4eUXIZhTD6XoawNCGJKfxPPt6cY3ipeGSn_2QOCVeXUbTSWWVv9TmfD7l5MueIsGGt2AFoGHN0M_c2Pf4s8kBVU9aXRGVqBMlEp0u7jrycyDhrkDP74WtsSSbZAD3Y2_PFnub2SneWrvF3Eu1XgURznkpVByGaP8RCnF6D6tgDVW_AivWz5QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-126309">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
نتانیاهو ساعت ۱۸:۱۵ به وقت اسرائیل قراره یه بیانیه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/126309" target="_blank">📅 18:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKun9pOJ5drY_59pGTD3428Zlp1uvuOYuR9S8QzCV5H7xdgFuzIDrNb9oSv7PJkFbap0fE1bwiPvoByLETiePo6I5_VOaD1JP7JmEkXFpByn1pMhIq16LC4U9apdAz5edLl8Jy3zx1vtIsfIYKO1Y0349Jo_xGpyv-l_J4CcUTqxL02emravZl4M_QztaE8E30MkPeceOft7gMuWvOs5Q_5DTL3e5CVGrF9ik2EZ4gorBQJO0BBlYnxewO-27sFV6dvctOdi7_iDRzmmPVWJ5snvxWJXsc-bn4e03Zy-FwgYNMtnHdRL3qWzVQv_871I_JQGxDUWhDblJyzkeHAhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: اسرائیل به طور قاطع تهدیدات ایران را رد می‌کند.
🔴
هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همانطور که دیروز اتفاق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/alonews/126308" target="_blank">📅 18:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126307">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq8oQPC6FjSbVkiJPSa_SNGAjSBCERMpHe8VaA8bl2ZJqcz4ToGU8_XuTGEh7cW7N611B8UFZ8TbpHoUZUATkChtjQnl3xHis_ZNKm-hk1kNcYHCVzK9-vf0351h1VZiREQr59AoLUzQU79sSP6Ti2zYyHB26uXl-aY64cO2i-lp1K2pgAc51HyCvZQ5R0milhZai1xklVA0KREUiCz6jh_T3IVlQHoIwLChMOj1WLxm4Gstvyw-t-iW3Jv4cMBdjmN7Ix15pk32teYXKo6LDemG4K85OTdzqjOImfcJBw6_IfSI-hrpQNhCwvCv7lUwNzbJgIGlO4yjPAC9ESU_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را برهم زدیم
🔴
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/alonews/126307" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه
🔴
اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/126306" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126305">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=usxD_oZbT8jiw0bNCSCYBlRHGV7VJY-1EIIWR1NQiVQ-UDxaZSwh-2mJ9B_sf-ou5Sw01nKXO_mnY95VxxGP6nv_v_vKIrd_z4Y6jt-ZAqr7Q36LiHvDcw354ynf6dnHMLDfrsKsxKOKDkpSfB0QONayaR9fhcA2EWRoCKimP82IhQuaageWOWkLng6dSgASpyz7FX2sfxShHjbeUTQW10oTeIrigBghArW6zLOs2q-eTfXb7H-IGpIOcRnEVbD9RY8bZpkl9OC3JkptEssKJgOuCnonHnO1Fq53n4DB270UjTHS64GViwsqNt4Xg3n5WHxix7vcCikO06uryOLMJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=usxD_oZbT8jiw0bNCSCYBlRHGV7VJY-1EIIWR1NQiVQ-UDxaZSwh-2mJ9B_sf-ou5Sw01nKXO_mnY95VxxGP6nv_v_vKIrd_z4Y6jt-ZAqr7Q36LiHvDcw354ynf6dnHMLDfrsKsxKOKDkpSfB0QONayaR9fhcA2EWRoCKimP82IhQuaageWOWkLng6dSgASpyz7FX2sfxShHjbeUTQW10oTeIrigBghArW6zLOs2q-eTfXb7H-IGpIOcRnEVbD9RY8bZpkl9OC3JkptEssKJgOuCnonHnO1Fq53n4DB270UjTHS64GViwsqNt4Xg3n5WHxix7vcCikO06uryOLMJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال هدف قرار دادن یحمر الشقیف در جنوب لبنان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/126305" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126304">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
خبرنگار الجزیره: آنچه ایران به دنبال آن است، تحمیل یک توافق آتش‌بس جامع در لبنان، در هر توافقی با واشنگتن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/126304" target="_blank">📅 18:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126303">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJTct8zOMqqLT88zZlw6TDz14s2UMdR7KgYRKL4NkYn7utkDVuc03EMFryFLvFWnITvEcRT8ZeZwk_l705aiL6TENJlIJCiQNH32ev-ENZsWka87prrcuK_1vnHeccAqJeRS1TgMp7rCd3vzelcGHVwebvvYtGeRQMN_7hsety99b_4ZYz0nOiN9jVcr7sXQicWnqLo-rqMS0c1fYaoW_o-F5To3bAOHX-5wTUagonNdroKoYMT-mkAaMy-QhT1Xs8yOo7bdKMCX3A_HKy2Gi4eYtqbrBQ01bnvm8VpIqpe1LnJfaX0Mm2Isx470x4fQSVl3OsF4lV32jjIYbw0uOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای عالی امنیت ملی: اگر ائتلاف شیطانی خطا کند، منطقه برایش جهنم خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/126303" target="_blank">📅 18:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8C2ReXEZn_1iOskrjkevgJtczQ3RHR2gVHd4ncuxIiS8RItIZDLa_9xq0LynNfi9Oa7IN3OIcm9liRKuX1-rnm_h9bPEr7lYBudYn-oYW4qBnO6yjekVOOrjrlmEwpxYlvBC40b3_Z6__X4O5Q0JVAZX4kRi3lmEBwZBtElc5ijvzBFHFd3ae97KcRGQKbOKdHB6d4dhbt2BGjtvXijxoTmNXy11MP0XVpclBBLW6hnNWAQI8shSPu-x8lUS36p7zG6r2Z6NkQpcqWsEbl9mk205Kn4owpJ8WKu1ergYHKm7sIl7J452siaJsC7kG-xloOSV0ZWGMtGDd0UZFU6gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkDkcGMFGHvwrQErDyVHZj2BKupJdOV_ssiUHIpVcfOQekpv8fYRPhV_jPBjXgnJ2jcnhQwZUYKfwRgnErvIxKz4QYydKmF5HacVFtBU7ALIlbJnqU_nVKv7sqADI7JY-gSIH9OD-lrGDUfXDbpgiteOdZogcIUNqI9qw8XbPQjUCEUh7fjON-cY3MiEy3xq7bQz2fkUAsYoYnBhQq3915_k638jJP7U1fu9bOC-Sa1zAU0DXg0xRh6zNRuYtfQTylEVB-8x8cWpqkBWZnvbkmlF6nR3_72qVBLlMixdF2aiTyYR4QwxEF2UldkuUity-deU4-mdVxJl5-z_dKkbcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d52e06eb0.mp4?token=Ccy9pLRVY_7RGhDOLKtEXrmaj1sX3RF8RiI24U3btLK_iiYjOuRHKmY9XuUfyYDkkp3ry04GZT1Gi-2W3T6Wr39prCxtuYMRGBk8cab0Iae1Znb9fIL3u-JSBhfjPYmAfX_y4hygNJiiLsAEmi3swWttckSfl8ZNXaGYcgU5iTAzfs0O0ZFcqPbm0Jvn3aHfYvte-eUJQey30Vy7qbdCC7oA4f6gJX3CKQmk22WIjXE4AIw7i2B3DezyLUPhTG-rWQW3lJkv-T5HzOM_wae2ydxFxPmnBfw6nIu5UmyvL5m8GFWYL40NPheltL2ntPND7UZMdAp9Myycod2-i0LytA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d52e06eb0.mp4?token=Ccy9pLRVY_7RGhDOLKtEXrmaj1sX3RF8RiI24U3btLK_iiYjOuRHKmY9XuUfyYDkkp3ry04GZT1Gi-2W3T6Wr39prCxtuYMRGBk8cab0Iae1Znb9fIL3u-JSBhfjPYmAfX_y4hygNJiiLsAEmi3swWttckSfl8ZNXaGYcgU5iTAzfs0O0ZFcqPbm0Jvn3aHfYvte-eUJQey30Vy7qbdCC7oA4f6gJX3CKQmk22WIjXE4AIw7i2B3DezyLUPhTG-rWQW3lJkv-T5HzOM_wae2ydxFxPmnBfw6nIu5UmyvL5m8GFWYL40NPheltL2ntPND7UZMdAp9Myycod2-i0LytA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله پهپادی اسرائیلی خودرویی را در نزدیکی مرکز صلیب سرخ لبنان در ورودی جنوبی صور، جنوب لبنان هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/126300" target="_blank">📅 18:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شهباز شریف: هدف نهایی صلح نزدیک است/همه طرف‌ها خویشتنداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/126299" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که ترامپ و نتانیاهو دقایقی پیش تلفنی صحبت کردند و حملات به ایران و جنوب لبنان بزودی به صورت کامل قطع خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/126298" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYDInFC1zlYANFPYshASvac0Qz_20uQcjmNMMqeygTzdxOq3oOcezU_MjBHXWD0BYpRXzIt3DJA7N9U8vjHc2xUmBBY1hzTqJj-X-7ZJoW-i9jd1yMKtiQ_NJpIv-Rl65Pm4z5h3LkoleFR0n4a5QPucgz1XTiw4rQEnAYZwk9J3rQJbhxCIC9Os4DI1MCjw5LpEPRmlzc91YCkuiI-va3pfcil1SOOKG5K62cwOEYq_wUg0SVCoS_6jIu7j1J-teuEClgG_i-O9tOzN2oq-RBW_HJd2K6lIBYlbkDWUw1n6hkewRGHCKkqObRPmKHizjY6XYFI4vzjl40-B01ZLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=eH6Po4Uuq4UcXNo2j8Bh4k8-yNhdrdzlstIQboFamcMJecHQfghUbv7-rdIqQaPCdEoIocUoETkwCpCz_QQ2ZKVFJPyOIJ212aoROmyt4gn1iXilhAoSxVTZAt7eYg6sIdcClMzET73HoODFpSMkWC-Y_Q2e7udOgBfgvRRRi1l4OonAzOYpJXZg0c1MylJ5apaWARSeS1zWevqsebcCsLrShuiDYiRfNVJ6mFtqwK9p9m00dLv7vLfsbD2cgXE5Ki2nkbN36_taOLE-sIUoMl5PxX_aVWb9QNn7GWYmmARK2aWxan57YH7Ya0DBalH5n9_fY6z61pxWHkM3mdH-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=eH6Po4Uuq4UcXNo2j8Bh4k8-yNhdrdzlstIQboFamcMJecHQfghUbv7-rdIqQaPCdEoIocUoETkwCpCz_QQ2ZKVFJPyOIJ212aoROmyt4gn1iXilhAoSxVTZAt7eYg6sIdcClMzET73HoODFpSMkWC-Y_Q2e7udOgBfgvRRRi1l4OonAzOYpJXZg0c1MylJ5apaWARSeS1zWevqsebcCsLrShuiDYiRfNVJ6mFtqwK9p9m00dLv7vLfsbD2cgXE5Ki2nkbN36_taOLE-sIUoMl5PxX_aVWb9QNn7GWYmmARK2aWxan57YH7Ya0DBalH5n9_fY6z61pxWHkM3mdH-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال هدف قرار دادن یحمر الشقیف در جنوب لبنان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/126296" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزارت دفاع عربستان سعودی: آنچه درباره هدف قرار گرفتن پایگاه الأمير سلطان در الخرج منتشر شده است، «صحیح نیست»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/126295" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/ایران اطلاع داده است که در صورت ادامه حمله اسرائیل به جنوب لبنان، حملات موشکی خود به اسرائیل را آغاز خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126294" target="_blank">📅 17:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام آمریکایی: ادعای اسرائیل مبنی بر اینکه آمریکا موشک‌های بالستیک ایرانی شلیک‌شده به سمت اسرائیل را رهگیری کرده، صحت ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126293" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از یک منبع اسرائیلی نوشت: نتانیاهو عصر امروز در جلسه کابینه امنیتی در مورد تشدید تنش با ایران تصمیم خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126292" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75c4ec36b.mp4?token=GeNeGv4v8zSIIWvITPhOpIOUpDYCIJ8YddWX-TCGZEQs_jlg85m0JPaApm7LTpcjOz8oX3vPa_yPeIQrxSZjEBsIH5KwTSt3tNPEvkw4eA8mC0wwahRfGtMNaSy0dcQRTn6WNWJohOCPOY15ndt9BQOfcY57VixyLwgBLb4xe_1fhhkLQB1Vm_njrBsYd45mO113U42o6uFtdWcO_S1j4O_3MWbiIQS5Stb2upZRynN1h_1YcYDtXsXkTooaYCsUUcM67H5AzDS6JzDmgBl9Sb8bAr9GBUe6GgRj5hr72nGMdpGk3tgK0dHpgrarXaohVdSeiHDCj2T27Q1JaDl1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75c4ec36b.mp4?token=GeNeGv4v8zSIIWvITPhOpIOUpDYCIJ8YddWX-TCGZEQs_jlg85m0JPaApm7LTpcjOz8oX3vPa_yPeIQrxSZjEBsIH5KwTSt3tNPEvkw4eA8mC0wwahRfGtMNaSy0dcQRTn6WNWJohOCPOY15ndt9BQOfcY57VixyLwgBLb4xe_1fhhkLQB1Vm_njrBsYd45mO113U42o6uFtdWcO_S1j4O_3MWbiIQS5Stb2upZRynN1h_1YcYDtXsXkTooaYCsUUcM67H5AzDS6JzDmgBl9Sb8bAr9GBUe6GgRj5hr72nGMdpGk3tgK0dHpgrarXaohVdSeiHDCj2T27Q1JaDl1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کالاس از اتحادیه اروپا درباره مفهوم ارتش اروپایی: چرا من از ارتش اضافی حمایت نمی‌کنم: هر کشور عضو یک ارتش دارد.
🔴
اگر این ارتش را به ناتو اختصاص دهید، دیگر نمی‌توانید از آن در جای دیگری استفاده کنید — همچنین نمی‌توانید ارتش دیگری ایجاد کنید، فقط یک ارتش موازی.
🔴
خیلی مهم است که ساختارهایی ایجاد نکنیم که ممکن است باعث سردرگمی شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126291" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c5fd0563f.mp4?token=EdXMmfYlSSipJb8Y7z7S0j36FXENMXntT-H3CTHs6VBIvt-uNIe-QZWmQJibL7aurouw-NCgwX6MrvkkLcS_8l4c80TsgFTDBrrBbV1SLbhf0UgM0l4Soeegm2SRUmPANNxZeIOC0jIgl0MutNJMv-5Q--jw4WRWRRaqRbgFoOUXcyl5UPKGKR51u2ySR2j_fAF4qPA_wjqKyL00O7ib8o-FTD_ttfTIVhQelwwdMRSBZ1ckiVGXpuH-y1y-83TC-DlWSXoM1TawdD1CG7yxNK8Ulhwaa_0L7HFYzj1JgU7yies-TIu2a5HRH7PD6R66hN9YpZP3A1VUsP8-8a_CRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c5fd0563f.mp4?token=EdXMmfYlSSipJb8Y7z7S0j36FXENMXntT-H3CTHs6VBIvt-uNIe-QZWmQJibL7aurouw-NCgwX6MrvkkLcS_8l4c80TsgFTDBrrBbV1SLbhf0UgM0l4Soeegm2SRUmPANNxZeIOC0jIgl0MutNJMv-5Q--jw4WRWRRaqRbgFoOUXcyl5UPKGKR51u2ySR2j_fAF4qPA_wjqKyL00O7ib8o-FTD_ttfTIVhQelwwdMRSBZ1ckiVGXpuH-y1y-83TC-DlWSXoM1TawdD1CG7yxNK8Ulhwaa_0L7HFYzj1JgU7yies-TIu2a5HRH7PD6R66hN9YpZP3A1VUsP8-8a_CRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد شاهد-۱۳۶ مواضع گروه‌های کرد مخالف ایران در شمال عراق را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126290" target="_blank">📅 17:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126289">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
اسرائیل هیوم: شورای کوچک وزیران تصمیم به توقف حملات به ایران و ادامه عملیات نظامی در جنوب لبنان گرفت
🔴
هیچ محدودیتی برای عملیات ارتش اسرائیل در حومه جنوبی بیروت وجود ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126289" target="_blank">📅 17:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126288">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فیدان: به تلاش‌ها برای میانجیگری میان ایران و آمریکا ادامه می‌دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126288" target="_blank">📅 17:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126287">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تامیر هیمان، رئیس سابق اطلاعات نظامی اسرائیل: «ایران در پی آن است که جنگ را نه‌فقط با این دستاورد که شکست نخورده به پایان. برساند، بلکه با پیروزی‌ای مبتنی بر دستاوردهای جدید خاتمه دهد؛ از جمله تثبیت حاکمیت بر تنگه هرمز و ایجاد بازدارندگی گسترده‌تر که لبنان را نیز در بر بگیرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126287" target="_blank">📅 17:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری / سی‌بی‌اس به نقل از مقام آمریکایی : دولت ترامپ دستور داده هیچ اقدام دفاعی برای محافظت از اسرائیل در برابر موشک‌های ایران انجام نشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126286" target="_blank">📅 17:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نخست وزیر پاکستان: ما با شرکای خود سخت تلاش می‌کنیم تا یک راه حل دیپلماتیک صلح‌آمیز برای این درگیری پیدا کنیم، زیرا به هدف نهایی نزدیک می‌شویم.
🔴
ما صمیمانه از همه طرف‌ها می‌خواهیم که خویشتنداری کنند و به صلح فرصت بهتری بدهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126285" target="_blank">📅 16:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سفیر آمریکا در لبنان پس از دیدار با نبیه بری: آتش‌بس برقرار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126284" target="_blank">📅 16:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بریتانیا به شهروندان خود توصیه می‌کند از هرگونه سفر به اسرائیل خودداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126283" target="_blank">📅 16:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d160fb5d.mp4?token=O7B7MdZZxoTPxrBBVDoiC2xEqLIrZWiMvcvf4p79b4z9vKhrcSFvlCLOT_4lNvlO1iRpxwFjaIG25jUPh1g5hZu3HFGq1m04SsR4zzgE0mpd8bOpNOgiJgMZP7nVXj5DzpTmGyadA4k-eq_f4P6N1blX_Q6CNceyjRzK1wsUJY2yKQPIk8kruF_2ao_hEy4zFpcwr0sl9Mbh5Scz_AShjmk2FQBGwatDto5ocTxNV4OYmxc7buqyfc2VOtP3YLVNsRltwb4wUYMFTZBhGH8F1Rk3gxXZhRFaKkOa9N7SwF3naZWIc8k9QatjKigfDUW8quiUPHdq5gtUwyuRJvg9p4YHeNemUEgdxo0lNbFYtxeA6PdVHpbGpbF9UJ2gs6Wuk6sArCbLjrGTpCTc1UAhH0JqhLEuGfC8lqyi1ysG6VTMvkuDKS3ZMop5KfU591snMdcB8zNjoqtn6bgbpvuRmXLVnKJ3tYSomBC3phYqtTEWetbLS-1F1tfNgKolXQ4dmtUO2r9eMLHAEGVc4RyuOt9EbB9uw1WQzYqdkqne4Vvc5vfGlXVoDCZTc0ADW5s2r_LH80H95YBtTAjut52-P3GmODS6XMIMThkkJOe_QXxq_EfEkoATz1MVOmCGwVqGzPW0Sv50kBvqBcqPxeZWFokwMpsXNCV-gVrzX5VEQ0U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d160fb5d.mp4?token=O7B7MdZZxoTPxrBBVDoiC2xEqLIrZWiMvcvf4p79b4z9vKhrcSFvlCLOT_4lNvlO1iRpxwFjaIG25jUPh1g5hZu3HFGq1m04SsR4zzgE0mpd8bOpNOgiJgMZP7nVXj5DzpTmGyadA4k-eq_f4P6N1blX_Q6CNceyjRzK1wsUJY2yKQPIk8kruF_2ao_hEy4zFpcwr0sl9Mbh5Scz_AShjmk2FQBGwatDto5ocTxNV4OYmxc7buqyfc2VOtP3YLVNsRltwb4wUYMFTZBhGH8F1Rk3gxXZhRFaKkOa9N7SwF3naZWIc8k9QatjKigfDUW8quiUPHdq5gtUwyuRJvg9p4YHeNemUEgdxo0lNbFYtxeA6PdVHpbGpbF9UJ2gs6Wuk6sArCbLjrGTpCTc1UAhH0JqhLEuGfC8lqyi1ysG6VTMvkuDKS3ZMop5KfU591snMdcB8zNjoqtn6bgbpvuRmXLVnKJ3tYSomBC3phYqtTEWetbLS-1F1tfNgKolXQ4dmtUO2r9eMLHAEGVc4RyuOt9EbB9uw1WQzYqdkqne4Vvc5vfGlXVoDCZTc0ADW5s2r_LH80H95YBtTAjut52-P3GmODS6XMIMThkkJOe_QXxq_EfEkoATz1MVOmCGwVqGzPW0Sv50kBvqBcqPxeZWFokwMpsXNCV-gVrzX5VEQ0U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی رئیس ، جمهور چین  به پیونگ یانگ رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126282" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=kQV2ajsJsQSmxZ6Gq2j6coTQArdgRNzsB9vR9zUAOTsSm6MapNZaZ72jmjQxOay7EiJhg2Yh5c08PEfeMPA7iyL9-E8fYroU9StY-tFEY1vp720PRDmWkN3oKIuiDX0zLqaBOQFFavbrxNhyukNGx1PeZIY2lzAnEj-LFlC7y5oG62KqNpB5eGnaO9W79ug4u_pZXy_UpXf3nDaY2-uDbnr-K_JOuYFgN42VNCMMu75k3Ql3C2Rf3bf5_ELeGwVgyV7wc1NfrMGy1gvhKA0zplnFvjt9kDvA8PLug8eEN8vCzyVXOTvTPnu87-zrap6Ogq8Gq9iTORtkzIzWxXIu6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=kQV2ajsJsQSmxZ6Gq2j6coTQArdgRNzsB9vR9zUAOTsSm6MapNZaZ72jmjQxOay7EiJhg2Yh5c08PEfeMPA7iyL9-E8fYroU9StY-tFEY1vp720PRDmWkN3oKIuiDX0zLqaBOQFFavbrxNhyukNGx1PeZIY2lzAnEj-LFlC7y5oG62KqNpB5eGnaO9W79ug4u_pZXy_UpXf3nDaY2-uDbnr-K_JOuYFgN42VNCMMu75k3Ql3C2Rf3bf5_ELeGwVgyV7wc1NfrMGy1gvhKA0zplnFvjt9kDvA8PLug8eEN8vCzyVXOTvTPnu87-zrap6Ogq8Gq9iTORtkzIzWxXIu6Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صدا و سیما: آمریکا هزار کشته و ۸ هزار زخمی داد و این برای ما کاری نداشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126281" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بن کاسپیت، روزنامه‌نگار مشهور اسرائیلی: ارتش اسرائیل به سرعت در حال اطلاع‌رسانی است که شلیک‌های اخیر «به سمت نیروهای ما» بوده است. یعنی نه به سمت شهرک‌ها در شمال اسرائیل
🔴
این یعنی انتظار نداشته باشید که به ضاحیه حمله کنیم. یعنی ما را به حال خود رها کنید. یعنی ممکن است الان مجبور شویم به «حملات چند وقت یکبار» به جبهه شمال عادت کنیم، همانطور که قبلاً در جنوب به آن عادت کرده بودیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126280" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ترافیک سنگین در محورهای چالوس و هراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126279" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سپاه : طی 5 ساعت گذشته سه بار مواضع گروه‌ های کُرد را در شمال عراق هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126278" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
مدیرکل مدیریت بحران هرمزگان :
حدود ۲۴ میلیارد تومن خسارت ماشین‌هایی که تو جنگ آسیب دیدن پرداخت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126277" target="_blank">📅 16:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دیر قانون راس‌ العین، در جنوب شهر صور مورد حمله هوایی قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126276" target="_blank">📅 16:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کانال ۱۲ به نقل از یک مقام ارشد اسرائیلی: ارزیابی غالب در خلال مشورت‌های امنیتی حاکی از آن است که دور فعلی تشدید تنش را پشت سر گذاشته‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126275" target="_blank">📅 16:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
لغو تمام پروازهای کشور تا اطلاع ثانوی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126274" target="_blank">📅 16:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
اورژانس ایران: ۱۵ نفر بر اثر حملات اخیر اسرائیل مجروح شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126273" target="_blank">📅 16:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSuAN7qIE1dvpMDMtxXPrGrAawZVxeKcy7ffvIZwpMqMHGGpFOT0_sz9DK8bjK751I_zZwyvBovq8joJ_nRhhaZzlgZoEx2pp1SR0XTVLeLhtdA5_EV5_7BxmiEsBOCz3C09iIkmL6-A-woeIZiOtaWtedqs1Z1y6Vu1qslxI3mPrK9fHmYO7V7DIC2BULj8o92IyEQsxmoYq2OGMdWBfRKxreIrcgsir5XG7oDB_nw5x_TJUJSKds3Z14hUsp4Q9yz7lEc_BjxDEYAg-7Kk2yLIGUViuvA2skQdMuiC2hOn-aDvEMLtHbVvdADN1hoKjZvRKmOsoYY44iT4yc7bcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لارنس نورمن خبرنگار وال استریت ژورنال: پیش‌نویس قطعنامه آمریکا برای نشست این هفته شورای حکام آژانس بین‌المللی انرژی اتمی (IAEA)، که کشورهای اروپایی (E3) چندان مشتاق آن نبودند، اصلاح شده و به گفته منابع، اکنون به قطعنامه مشترک سه کشور اروپایی و آمریکا تبدیل شده است. بنابراین به احتمال زیاد تصویب خواهد شد.
🔴
بر اساس برداشت من، فشار آمریکا برای ارجاع فوری پرونده ایران به شورای امنیت سازمان ملل، به عنوان یک مصالحه، از قطعنامه حذف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126272" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5aNipuVp5A0MFE3p6l_dHfy_ileqCzFMmNKUCfNduk-s2SxMO2B1DeWmwHCDIwwpedLlaajAB-8boC0pP28UvulSZWXijjuy4OcpPI7EDxHUMed-3fn7EW3VRL759RDwSCMeexmmkvfQKU88pfRi-BLx_t2M1CoirAAq7m5-cT42tiEk0dBY9KDuXLrIwpIlwiu0gVKkKABCF2K78xSbTbkCeVxHP18w6h5L9gWh0r-ITs8RKg0uUdDng-CA2IYxlZmpdPL7WM2sgtY0WHXDGIq2x-QxSTwAGze5MbOY_Wfq4HaT6bTx8AMcGy7NGzcIpESlq1TtHIfuaR4ppVbNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تخریب در الخریب، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/126271" target="_blank">📅 16:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رویترز به نقل از منابع:
اسرائیل تصمیم گرفته است حملات خود به ایران را متوقف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126270" target="_blank">📅 16:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
منبع عبری به i24NEWS: نبرد بزرگ با دولت ترامپ از این پس، ادامه جدا کردن مسیر مذاکرات تهران-واشنگتن از جبهه لبنان خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126269" target="_blank">📅 16:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال ۱۲: به درخواست ترامپ، اسرائیل حملات علیه ایران را متوقف می‌کند/ حملات در جنوب لبنان در روزهای آینده با حداکثر قدرت ادامه خواهد یافت
🔴
اگر حملات به شهرک‌های ما ادامه یابد، ضاحیه (بیروت) را نیز بمباران خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126268" target="_blank">📅 16:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv4e6abhksKBi4ITsKyJbITJOeQ-QbDg4Zplsx1gHrC2YA0q-EdbGbLYkSbVTmtb7dM2dIy7XFfIliVlnxApYbK0f_QOhgmsUtgTtp-6xNq-LXOaBhtRfUWMqi8Gs-ztS-DdPW7d2cSLtv9NAje1teHy4qiw9t8PKOKlmTSFZNtim_nemRmcoqv0q9H0OGWxJJfv7cShYyA_p8Gm4_lSiJK1eYc8onTiR7wYoThClS0Em0gxWmvHL_M6Z9d5LbO2XOU_bVAfmYDmH_Ev5ACsZ6MGtdhU4jt6mK6ocZS3vn3MBt9ZK7ecsJveSFigEOjBbpjiKWdnrsrm5QHdpqeZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام اسرائیلی به شبکه ۱۲ : به درخواست ترامپ، اسرائیل فعلاً حمله به ایران رو متوقف می‌کنه
- ولی حمله‌ها تو جنوب لبنان تو روزهای آینده با قدرت ادامه داره
- اگه حمله به شهرک‌ها و غیرنظامی‌های خودشون ادامه پیدا کنه، حتی ضاحیه رو هم بمبارون می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126267" target="_blank">📅 15:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کانال ۱۲:
آژیر خطر در کریات شمونا و حومه آن در شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126266" target="_blank">📅 15:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126263">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpfpUBS4UHLNb37VZt8fQzsvuOCmfmsA3G89Nv_noH7yuBRM11Luhoc1MyayIizOmL4E-CsF8z1zgx_i-ybChaqlzNb1NG0ln-9tWGeK0S9y57ZNlWQ8wkwArjjBM49_Cqk53KdY1RPtmb4kGqDr07_PKtri4vxBhjoT-1OZR5GEmA1NJ8SMh8IhWnzdiI5qbvVhiQxRa5a4tfJu0rSta70PszmTtQffqKx-0JpI78vMkMPj6vk2_HcKmNv9VMu5IU27FkMb8jzQqZktl4B08XMprDp7aUI-iSElp3QZZ7TgM1q54qK1X3bUp7LCSTFPuUHAZFu0Rh65-U5tzI4VYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDojKYg1pfNoT_IjTcT_GsQiRw0wr8iT8bu5z5MbrXDlSVf-yX0Nmr7h-O4_xcoeFLk5GrxnAu_eExKCoLnlQxn9VNWKwjUlFwinMDu9nm-pUDxsdZFNB-LR-7SpbShN6N1gC9cKSFyCg0vzQZxlwT8r7ec0T7aQRmzrU0Ip_Yh048DQnxXOt7zmbfiZLAxRk2KJUai4IzERWLFkXVwwrfJnEo4ZWIi4d5G7Edk5OpAjMyLSphjQk7u2wIwFszc6TL8GzmFrS8uwnofdd03LQ1Tnou6Tp-t4rXyYKMm-A02Pvqy4XgswX6p81tRYs4Gr1CsrEC_Vp0GZbShaZgyV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TjEaWaCGSdY0sSxkR3gOnV5sJJdv5X_Rn9KDw6OlpqDNoDyGMastOKkJ-IXKLf6-CXbw0_n1h3koONJdL5Z0Wmiodux8rNEd7OvYpDkrvRNlc-1R4tGU4mQx3e00mWTDR6La-duWGfUsVbsXpAntw_5TWh2hF6CHYl9xUHxd0qRwfi9Yp-6KjS8W1XJcUaInYH3oQdBX74eIkHvBHADv0RHZTHbdLQx9DAZDTiwLF576DCDFKhRegUw9ZAhe8bwGhx5aY28vwT7MSGtna0_gmjJRyyRl-CqYFFDPOl-drHcK4Y2JzhherLF7M7O9lk6i6eQCxtAP8dKFD3Q66dn15w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات به لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126263" target="_blank">📅 15:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126262">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله هوایی اسرائیل به منطقه مسکونی در صور، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126262" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126261">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWWilQnuZ0zAwTrNLo1vAnUg4iuU2hzMkTplzJgZqaiN4nCuKbsgEuQQMuHCtNB8ZyL5-kOYmFyOPIupD9fLctYT-ZAlAo5Q2FTpmsWMGDUnmiE6ZSGDLBdyxCh7PzKa91vA7JYS5f8UZ7diVFp-mQ1gYTBxnMbvnaPILWk-Fq8ofqoImClgCUtkf_gt8NOv250gCqHr0BPBUALIL304fmBTnHZF6BggBxvToiWgqWYbrOjdPZ4ghecD1KQz8b6KEDkZFAEMMj0CqAI7VLLuLUqkGsfU2bTJn22Y_WFz-Vf70L0CF85t-5ZxMdkEPA0oV5kXLc_TCce51g0O96h2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی فیفا :
دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.
کاپیتان های هردو تیم باید بازوبند رنگین کمونی
🏳‍🌈
ببندن
@AloSport</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126261" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126260">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
عراق از بازگشایی حریم هوایی خود خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/126260" target="_blank">📅 15:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126259">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzE9fS-OrXcJ7OzGGUFHwXV5Pv5Oaow2wcBUeT3i9G5Rj2nAXivpLGLleat4UNnIQGqlyzK0Fz6PGrmVYLKyR45FQH-_9_yldCBZ9QprfSAPFUajsOLmUgtfpic6woCLQSw6wn_7PcFhSKJA8OQfq61v71EIlgdFzEw6Sppec4Yy3VmYDMSgiSuasaU4DEnGA19CR-nSUIU2QtttK3GcqWkvymb66ORfOHcJOdMB6qo55U1jPtE3yu0WMU2ws6wXtOCRIt8_Tle-AeW9RCpgO2Sz0x-haKsdKhwKyt8_rRAiQRWZtpBe2f6BotFtpgEbxQNdsNhWcXo1n11sqm1twg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رادیو ارتش اسرائیل:
ایران می‌خواد دامنه درگیری رو گسترش بده و به حملات اسرائیل فقط تو ضاحیه بسنده نکنه، بلکه تو جنوب لبنان هم پاسخ بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126259" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126258">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
شخص دوم مملکت،پزشکیان: در برابر هیچ تهدیدی عقب‌نشینی نمی‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/126258" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASTwLU53ToDhrbWNLVa10IQ-RvpBkBKJ4imAfX81FR057bY-KkWAPNdvPkVxkq6OwKtEvYWU-4oVx8AmK6DL7KXkoVw9yceST5QzK7I1KW5R1ef819u-Mq6fvgfvIG8u4tfYv4cFh5Xx__GrfPAot2snf8-_TQZ-ld4Bc7Yp0CcUqN50jkt4lHmAMPiG7wK81nGUYYXwv5AzmJBaSGZ2Fxfu9PTcCamKK-QXF5TmkQ3ItmSfMhXZyZ0OsTEkZPu0sXjFUAo08I2m6oW-YoIcod9ejU7P9kOAfdwhMTkbMG2KxwjHGFdytjCreJD1d9mm8dr5noxCUS_t9b2bReJrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/126257" target="_blank">📅 15:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCkN-_dswMj1UF4UyEWkag4QL4cjh6SHScSqswPscpbJ4rkk_egn0tzHYS09xcDIVWf8RJEB1iEqrRvxnFNPfuCLKd79qh2XEAy4JRlO_vMgeEo3IkapTwvs8gixyoU6TDEAYxDv0CwrphzSjf33VUkP06PPQ4p8cvlFh6Zn_aphuhVmCemQbewgmSZG_J81vhXByd2Iiq8j3dJqapp5XIImrcIG2fkmvGei6hWcD4cs5FLNmQ9Tqh0ZxCvGtRGADtpJO8q_-K9Gntffu-wXF-YwRXFAuH_wqkXgEYS8yxb69GqiyxRbvzfwj8InC5tG0OT5pC4eU38AT1K9Vn_vOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتشر شده از حمله نقطه زنی به تاسیسات گازی بندر حیفا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/126256" target="_blank">📅 15:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126255">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
صدا و سیما: جنگ پس از شکست دشمن به پایان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/126255" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126254">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
از ساعاتی پیش تاکنون حملات ارتش اسرائیل به سراسر لبنان متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/126254" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126253">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cd2922db.mp4?token=rA2r-Lk7Ipj5x1WudWBESK00_t901LlcypgARSIHT2pTsA3Rdtz2bCVVssuh9KdYBntMyQiIY2f7kTjtlKB4K3GpkYmo2Y0KOmr9b_e0gonjhFo57TjBlmYM_vCqJZps6jJVaUMCRYg1-S_jktc6_JS5cmPGNPZb4YhB8SsaoGV1HsGdM7-O4kU3r0AUyOsO6wJR_MzfLQr7eSbnW4HZeW6X1RnsZJPwue71_PMzMHw6BPBlAl8TECZpyx4j09vXDMD_-crYBI5RmqGwTzz364D1-Cdkq2yyzpOnVG2QVyk_UbHXN2hLUdUPWH6xNKBVN_Z4hU7048jXb76Amgig0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cd2922db.mp4?token=rA2r-Lk7Ipj5x1WudWBESK00_t901LlcypgARSIHT2pTsA3Rdtz2bCVVssuh9KdYBntMyQiIY2f7kTjtlKB4K3GpkYmo2Y0KOmr9b_e0gonjhFo57TjBlmYM_vCqJZps6jJVaUMCRYg1-S_jktc6_JS5cmPGNPZb4YhB8SsaoGV1HsGdM7-O4kU3r0AUyOsO6wJR_MzfLQr7eSbnW4HZeW6X1RnsZJPwue71_PMzMHw6BPBlAl8TECZpyx4j09vXDMD_-crYBI5RmqGwTzz364D1-Cdkq2yyzpOnVG2QVyk_UbHXN2hLUdUPWH6xNKBVN_Z4hU7048jXb76Amgig0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل این ویدیو از حمله به سیستم‌های دفاعی هوایی ایران رو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/126253" target="_blank">📅 14:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126252">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayRfs5DJBL5syxrG91ngq8a4DnqQQQGfTDpYZnYMmFjiOPSirLwOuGXTRHTyCc9WSWb1p6aKyNqNbuedUPwGHQxRVsSjKkQN1CkQ_y8wZCnYg9A0CTT0pwKLT2DlPA5E2w_sUPczevLrUBepWnvud41lhMoWJS72as60o6rId_bh4J-xMyZdGBZY1w80v1ujtDL8UaS-e3Iv8M1D5flbaBJEjOAnilTqPr4hw5Zy2-H2cGNtdV-ReiB9wSR1me2c3jzkzBQ25TMDhsMWLWWJtIJu5Gtw9W1DGgyDFBbvbwBmCUolHNy9KDF1VQUaaCIFfTlOkfpxq5VFdLQ3Jbqc1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: جنگ ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/126252" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126251">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiK3m-dLfOthp1T6_yl9-WZRfM-BaRzybjb50pWr2XkDCjGerBUyPiZkVlgMqaSOwIAh8-ZlGhR-e3UJIzdq0IDot_Qw1tnVxp9_rttnNVxbn6k6sC8yPw0XHR0vhPY7thGzAlX0c35byUga56FDWEQzRlAsXD79RCBCRyKxQnZ5JLwUOQPQ5tepwyEf_XzUUv72xY3jR82n-kIi8bmpHAANQVi9fAjATHX5bUPgkZj5VPAey0Qk3lcZn7SwGpTbrdww8JMrEcn3_Q1VR75Kv5DzUcbe13fvppgOy-1ldGzNFLgwx9gHaKyKaQiAH2cqSjZ02u-QHpeToRlkqWBFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/126251" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126250">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/126250" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126249">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اکسیوس: یک مقام آمریکایی گفت که تماس ترامپ و نتانیاهو «مودبانه» بود، اما نتانیاهو در برابر درخواست ترامپ مقاومت کرده است.
🔴
این مقام آمریکایی گفت: «به صراحت به نتانیاهو گفته شد که این چرخه باید پایان یابد. آمریکا با این حملات موافقت یا از آنها حمایت نکرد.»
🔴
در حالی که دو مقام آمریکایی گفتند نیروهای نظامی ایالات متحده در حملات اسرائیل به ایران نقشی نداشته اند، یک مقام اسرائیلی گفت که آمریکا در رهگیری حملات ایران به اسرائیل کمک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/126249" target="_blank">📅 14:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126248">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری / اسرائیل هیوم: اسرائیل و ایالات متحده پیامی به ایران ارسال کردن که اگه تهران حمله دیگری انجام نده، هیچ حمله‌ای علیش نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/126248" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126247">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سفیر آمریکا در لبنان: اگر حزب‌الله حملات خود علیه اسرائیل را متوقف کند، اسرائیل نیز ضاحیه (حومه جنوبی بیروت) را هدف قرار نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/126247" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126243">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4rgDGhWTsiptVu8w_dDugCqKyfCNpS9nU-JuDKLYr76Q-mnp8TjoFd5bc0qV4ckEtzywdHXzWBOpAkayyifrJfVNbLk82H4SMuxGmQv6qO7r-yTtXXB0H6FtgcAWFFs1PYWp7B4kPj4KstSEw6DmR_zNsuuEDOw6B4hy4LpfjCnlXLZ8ahq_eLlmSMz6kJAtJlpLFMv7BA3ewXrAgUuDAlXol74ozZn1oZdS5B0bUayoxHK4mlMposvUC9FlWGp7ooZqUSTKUU02xCxied3xIJ4OvGIqLadOHY1BWDAZTErk4sKuGq0bLpf8QQm_ao-xdwMcTiu0XiKRsrazGek5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhuWd1UGvWEmpz-DRytpMChFS-shsshaliUZeT4lYMK4lWtCOQJBpJ3AgUCayxMWL3sp3B9mI2_JGl2oQRp-FLdA3VJD_2-PeV6YcEbko1L4x6KcN8yTt9wlzPmMIxYs_0Tpru7H5Ni6ibsnmvitT_YJ0j2lOPP58UCX5DF8Bxo8-iUvaWYUelNodYoyGOFwL5hYgy1vkqvW0Wqgbzk1mBiUgPa9CkoVnsRXJAkx85xDrGCAR_IpkGr5DNvvgHT9CT6v-J1sV5WoGK50WyTUS_pqfqBKXQtDm3d15YIqApFLNpSMpARRjyUiY_dwGb7w7KgSyIPmzfpWMDOlGkZWTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqIVD6F-FR2pLoGaj3E85FTjwESSxoslAPyFvXbb04gKQ_aRiC329XnYoPCK956Gr8u5J2oo8M7H9y6ySzXnn9X6k1_2ccxKYD1H1fdtAwV1ISOV0mR0LCpVmSvbLbukYRi41hJchjX5T2S2evIwOhKjY5hE_LZy3usd54MUGSSvXX3uqDgReiPOzGM8HpnN_T8iEBsBX_jt5IJWP9sIQh1HIjmLGlwHMCKZXzKT9NN9f5IpdX9OmKScmos2_dOh4QP6fIcuR9pRWLi7gOrjlwUfXVieu8uakCeJmZB2qJQfe-_U1OpxR6cNEtsSwMmCS5Ksfgaatd8bDPP87svZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DW1dW9Lv_-WTP5dtBrGTDAsCGCbJh3w1TFb24UORzRxMd2WInOHbCd9C2gAcXRNfxTEMziz8B0PK9k3U2v6o7E6WlD5qoENNp8GxLQd9KUHfP6CzJ9zDXB_Elw8aoCJ03YINRp7sVXYT_BGJmPt53kbIHbxTePJGiHbPClLBipKsZobg9eKXvkYU7-9Ff19nPSesnvtcZA0LHov7JOXrWG4xSka65QDamL7jrsh6TOsW08JDR7Ml6aZZYpN6dDT6M_ogoYoz13KmsuaKhTIilgS8xrrwniwsOqAkpAAJgH_MMwraQ8iBkAuEF1-YcIYJ0DhD56I4iAThMQLAUbkejw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکاس
اسرائیلی
؛ رفته کنار یه پوستر موشک ایرانی که تو اریحا فرو رفته، وایساده و عکس گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/126243" target="_blank">📅 14:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126242">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
فرماندهی سپاه تو خلیج فارس : هر شناور رزمی متعلق به کشورهای دشمن حق ورود به خلیج فارس رو نداره و در صورت ورود، هدف قرار می‌گیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/126242" target="_blank">📅 14:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126241">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
کیر استارمر ، نخست وزیر بریتانیا: مذاکرات جدی برای صلح پایدار در جریان است و مهم است که به آنها هر فرصتی برای موفقیت داده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/126241" target="_blank">📅 14:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126240">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: ایران باید به تعهدات خود عمل کند و از فعالیت‌های غیرقانونی خودداری کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/126240" target="_blank">📅 14:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126239">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اگه آمریکا، اسرائیل رو بمبارون کرد تعجب نکنید چون ترامپ رئیس جمهوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/126239" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126238">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ: به اسرائیل میگم بس کنید تا برخورد نکردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/126238" target="_blank">📅 14:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126237">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری/معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔴
نگرانی برای قطع اینترنت وجود نداره و اینترنت قطع نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/126237" target="_blank">📅 14:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126236">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
🔴
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
🔴
محاصره به قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
🔴
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/126236" target="_blank">📅 14:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126235">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvV_1ex6NxWl1ZsExuyR2Nlvc2Fe46pzPwC-MJrHE34FNlLwJwCkIk06Cycdz_GVUXLzfy6yJfgHaNWiQUFyYoZLqhbeTZYTgsmSTbuQqlXVQrRDnHfavFcWncmZ5rKeedP-4-zK6YuGIwn1_2HzbGL_S5Z_OAmhXEiec0YskZWY0uBmoZ2nuEVviugmUBqb0GCRoGxjZlYGB2mwkpF5gsYHBK_bBhkxPjRFdRf-olyk6HLQFlF7LwSr1rDzr-tywUKCy4mR4VZDoCVI2vLB_FjFsVuvbNax3txQLUxWzflXnlmdC66BFaOt2v7n7PHWkJWXOuZpUCaeDcONhhRbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / یه جت خصوصی از امارات ،با وجود لغو تمام پرواز ها داره میاد تو کشور  و نزدیک تهرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/126235" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126234">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
زلزله‌ای به قدرت ۴ ریشتر ظهر امروز حوالی مهران در استان ایلام را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/126234" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126233">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه چین : پکن به‌شدت نگران وضعیت فعلی و از سر گرفته شدن درگیری‌ها بین اسرائیل و ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/126233" target="_blank">📅 13:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126232">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/alonews/126232" target="_blank">📅 13:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126231">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
انهدام یک پهپاد اسرائیلی در غرب تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/126231" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126230">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
یک منبع نظامی به تسنیم: ایران برای جنگ طولانی مدت آماده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/126230" target="_blank">📅 13:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126229">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
فارس: تو غرب تهران پهپاد زدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/126229" target="_blank">📅 13:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126228">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdqowOAE_eFfnvg_LiLDNsm2lVTcciXVxO_M-V4TPVllSfStW9AsRWTh4V5ULMQ68Xw_RKeeG-ZR1_aoQEHEbkrO5A1_cqPcwg4cypczfbmHtR-vzMnvPPZ_5bwR7C1v7HCL9tdX1irsaJ5Y1ZDnD1zfDxqDM7xCnz2AucqlSWsisjMrGosfCT3p92_s55iCaKF7SkG-4ISvIKuljbYVVBXT1gWj-pfhCJcLVk4cQCSAUlb2kqofVF6qAMdguwV_fWpoBfh6QH7wkzV4XXuSsI7K0PNDjcZI5ojlMHHgQa6Loe7IroPea6R5-tH6u3ZkPzpHsyCTS-gzj-oRGTYOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال ۱۲ گزارش می‌دهد که ارتش اسرائیل برای احتمال یک جنگ طولانی با ایران آماده می‌شود، در حالی که «عملیات شیر غرش‌کننده» ادامه دارد و اهداف جدید در حال حاضر تعیین می‌شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/alonews/126228" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126227">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نفت: ۹۷ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/126227" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126226">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
آسوشیتدپرس: سوریه فرودگاه دمشق را به دلیل درگیری ایران و اسرائیل موقتاً تعطیل کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/alonews/126226" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
لغو پرواز‌های مشهد به تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/alonews/126225" target="_blank">📅 13:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126224">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ: اسرائیل و ایران باید فوراً تیراندازی را متوقف کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/alonews/126224" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126223">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: اگر فرصتی برای ترور رهبران حزب‌الله در حومه بیروت پیش آید، در انجام حمله هرگز تردید نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/alonews/126223" target="_blank">📅 13:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126222">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اورژانس تهران: هیچ مصدومی در تهران تا به الان نداشتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/126222" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126221">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سازمان ملل ابراز نگرانی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/126221" target="_blank">📅 12:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126220">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV7hUSa2cRP2ZfTs6JlTB9znhZTbqlofy-lrydta6cU1hi6oqBaHqZEU6cZo6cGliDw1O4w-vER24PplqMaGkEsbxo_lV-3010xMcmY63VruuefmOIzAt2Q8eH_WPba5HnqK4wrxPJCHxQMmhGqBPe87fUR9tnoPOBQMaKS-i09JHw-HuRIbeY2BTm1iaOtLSSLC2jvfI7wur7ta6n0XPomTWMwhl2D3MqPUDvNsY12yqF16GEL7znjYCBcBSGb1wxc6VoqJyiYuNWbRFB1U3vRuZx_QCLcyFmWhqfzd5aWSXb52L1sp8XOKwHlJ5e92C_zL4B6s4j0eUPRo-w-krg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان منطقه ؛ هم اکنون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/alonews/126220" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126219">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
منبع ارشد امنیتی ایران به المیادین:
ما قاطعانه تأیید می کنیم که معادله قبلی  «زیرساخت در مقابل زیرساخت»، همچنان معتبر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126219" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126218">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل:
تاکنون، ایران بین ۲۲ تا ۲۴ موشک به سمت اسرائیل شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126218" target="_blank">📅 12:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126217">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12238f728b.mp4?token=RkUeBlKeXorn1UlRIYqANagou4EjkPKm1JQJX0G-7h-He4DR0fCR_s8JGmJrqPbGjQCuvD9z8Z_eZ-HNhz4LvJWPw6YV6jwmt15qRI5FkmR0hRdCt1mxivn88OaIZcYJq9GyQnk2r7hVcoL3wmRpTA3Wx4kYhA4sUfGCjN0eu8ZVUxEU80Hbgb4G1Q-_83Uk6QrItVrk6T4SxtRkkFPnl_aglFDKrFAo5YNqMd5fXW2GoRCPzh6X39bo-fZZ_pomC0b-BGtlCOMvfj_C5-jZiiQZS4HLXlAIdGl2HLpbYx67X8nDr-BMzvfL7fUsamsanvRMUxosa24Tm4Khgdg09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12238f728b.mp4?token=RkUeBlKeXorn1UlRIYqANagou4EjkPKm1JQJX0G-7h-He4DR0fCR_s8JGmJrqPbGjQCuvD9z8Z_eZ-HNhz4LvJWPw6YV6jwmt15qRI5FkmR0hRdCt1mxivn88OaIZcYJq9GyQnk2r7hVcoL3wmRpTA3Wx4kYhA4sUfGCjN0eu8ZVUxEU80Hbgb4G1Q-_83Uk6QrItVrk6T4SxtRkkFPnl_aglFDKrFAo5YNqMd5fXW2GoRCPzh6X39bo-fZZ_pomC0b-BGtlCOMvfj_C5-jZiiQZS4HLXlAIdGl2HLpbYx67X8nDr-BMzvfL7fUsamsanvRMUxosa24Tm4Khgdg09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا: «فقط کشورهای احمق وقتی به آنها شلیک می‌شود، پاسخ نمی‌دهند»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126217" target="_blank">📅 12:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126216">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
هشدار دادستانی کل کشور درباره انتشار تصاویر محل اصابت پرتابه‌های دشمن: با متخلفان برخورد قاطع قانونی صورت می‌گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/126216" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126215">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6yV5s0_MWPVJ12r8rp9iuSvAEvYeEqXa7mw3TzUiMw6-yQAp6dz5MZt25YlkhSOOehLhSVM-Dzx_osaeGW96Ln8FfxUNODknsVLzm3ezkytmtQVW_30I0EwoTOBhEWMjDao7_Mi_01LlEhQaIj3CGdaNhJllKUo-wKZL2TDf63POgyN2w8NG9TsfMSDwltKOw-HZ4nA8xEppbMuKI27C1DIuT4LEfIAYjvaZleBXnymMc9VUoZECerXfiWYSTQdNq4C966MKEGh95749PsCSlMPejdb3WVNpFjEwKkIQDudrwtYUkbZrN_GVOfPEA7BUacYR_Sdz5P6HAZpkxFclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: اوری گلدبرگ، مفسر سیاسی، به الجزیره گفت که پس از تشدید تنش‌های نظامی اخیر اسرائیل در ایران و لبنان، روابط بین ایالات متحده و اسرائیل در معرض خطر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/126215" target="_blank">📅 12:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126214">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
رسانه‌های عبری: شرکت هواپیمایی ویز ایر پروازهای خود به «اسرائیل» را تا روز چهارشنبه تعلیق کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126214" target="_blank">📅 12:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126213">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=NLljvNTnva16ezdnAmTQGeH9qQCr4mAITJdEN5fGhElEI85TNf5tHz2BBB7pUlODUh9kUrUGRKNemdj48UtRIBxasTuXkZRxn8b568ZKPdKQye1oibWaWiwoM-YK3OlHAdMdbjNWfwgYCsEJwqip8he8Oa_iNOuhBSbCd6loiKyBz6GMY8Byq_zA5hX5yu_ELN4bOWz9Yy3WBGyKiCSOwvZaaVYdVZrbU_PykzK-Gp1ZvFSYHNX7WX_Dta35wa5ZNRl6sD6KriTdtwHt6U1froNYuzuAHYTzmojQp_4rY2jZ9SZoIDopTTFwnqz-qnqkeByz2tbTk6oNd3sfrmtKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5391f1a037.mp4?token=NLljvNTnva16ezdnAmTQGeH9qQCr4mAITJdEN5fGhElEI85TNf5tHz2BBB7pUlODUh9kUrUGRKNemdj48UtRIBxasTuXkZRxn8b568ZKPdKQye1oibWaWiwoM-YK3OlHAdMdbjNWfwgYCsEJwqip8he8Oa_iNOuhBSbCd6loiKyBz6GMY8Byq_zA5hX5yu_ELN4bOWz9Yy3WBGyKiCSOwvZaaVYdVZrbU_PykzK-Gp1ZvFSYHNX7WX_Dta35wa5ZNRl6sD6KriTdtwHt6U1froNYuzuAHYTzmojQp_4rY2jZ9SZoIDopTTFwnqz-qnqkeByz2tbTk6oNd3sfrmtKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تازه آنلاین شدم، آتش بس نقض شده؟</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/126213" target="_blank">📅 12:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126212">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">من تازه آنلاین شدم، آتش بس نقض شده؟</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/126212" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126211">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rktq-1pvZ2fIgTPFWlxk3UuQmK0C-Rc_buNmK-DjdYEo4FaU8Hnim5jQBj9ukm2QUgLoxmPIBv-gYsfIASiku8cLuaQJxIDTzqqq7OebL6DffJhYN7di5NQguvzbSrSPtxvpYK0njpWO7iwa1W0rcdQ1xlj9WwofUiWyQ2cPRLye8W5K6TR45JurfZAESQ-CHklr9y0jv0-gbAdLOzyzbVoGUJlVM8ZtHjVVUzPx6IgAN5Dah84YKhsaiJ8f1KhJJ2Sl-OGyrsvdiqiz4BT3iXg9SXSbxEzDVDjb0DGmyOqGyi63g_x1cYTWnxZbf8fO-j7_WNIWxRQNRbiJrdDuzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در حال حاضر جنگ ایران و اسرائیل را رها کرده و پست های مربوط به انتخابات منتشر می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/126211" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126210">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
آکسیوس به نقل از رادیو ارتش اسرائیل اعلام کرد که ارتش خود را برای چندین روز درگیری در ایران و احتمال بازگشت به یک نبرد طولانی‌مدت آماده می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/alonews/126210" target="_blank">📅 12:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126209">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل گزارش می‌دهد که حملات به ایران تنها توسط اسرائیل انجام شده است و هیچ مشارکتی از سوی آمریکا نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/126209" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126208">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
الحدث به نقل از سفیر آمریکا در بیروت:
قرار است مذاکرات لبنان و اسرائیل در واشنگتن از سر گرفته شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/126208" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126207">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۷۸ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/126207" target="_blank">📅 12:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126206">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری / روسیا الیوم نوشت: ترامپ به پیاده کردن نیروهای ویژه در ایران تهدید کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126206" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126205">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی ارتش اسرائیل: حملات به سامانه‌های دفاعی استراتژیک در ‌ایران را تکمیل کرده‌ایم
🔴
نیروی هوایی به حملات خود در عمق خاک ایران ادامه می‌دهد و این حملات شامل فرودگاه شیراز در جنوب ایران نیز می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126205" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126204">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مهر: هیچ اصابت یا برخوردی در فرودگاه شیراز رخ نداده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/alonews/126204" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126203">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری/نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
🔴
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/alonews/126203" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126202">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
دقایقی قبل، تهران
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/alonews/126202" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
